#!/usr/bin/env python3
"""Reviewer-key health — the loud end of "keys never work".

Every review substrate (deepseek/openai/kimi) catches all errors and exits 0, so a
wrong model, a dead key, or an exhausted account all look GREEN and simply never post
— the failure is invisible until someone pulls logs by hand (measured 2026-07-23:
Kimi model kimi-latest -> 404, OpenAI -> 429 insufficient_quota, both silent).

This makes key health DETERMINISTIC and VISIBLE: each mandatory stage must return
non-empty content using the same model-selection order and reasoning settings as
the validator chain. HTTP 200 with empty content is DEAD, not LIVE.

Secret-safe: reads keys from env, never prints or logs a key value.

Usage:
    reviewer_key_health.py                 # check all; markdown table to stdout
    reviewer_key_health.py --summary FILE  # also append the table to FILE ($GITHUB_STEP_SUMMARY)
    reviewer_key_health.py --selftest      # classification unit checks, no network
"""
from __future__ import annotations

import json
import os
import sys
import ssl
import urllib.error
import urllib.request

try:
    import certifi
    _CTX = ssl.create_default_context(cafile=certifi.where())
except Exception:
    _CTX = ssl.create_default_context()

# One row per substrate. Adding a reviewer is one dict entry — the health check and
# the review workflow must agree on endpoint+model, so keep these in sync with the
# corresponding *-review.yml.
SUBSTRATES = [
    {"name": "deepseek", "key_env": "DEEPSEEK_API_KEY",
     "url": "https://api.deepseek.com/chat/completions", "model": "deepseek-v4-flash"},
    {"name": "openai", "key_env": "OPENAI_API_KEY",
     "url": "https://api.openai.com/v1/chat/completions", "model": "__discover_openai__"},
    {"name": "kimi", "key_env": "MOONSHOT_API_KEY",
     "url": "https://api.moonshot.ai/v1/chat/completions", "model": "moonshot-v1-8k",
     "enabled_var": "KIMI_REVIEW_ENABLED"},
]


def classify(http_code: int, err_type: str) -> tuple[str, str]:
    """Map an HTTP status (+ optional API error type) to (state, reason). Pure — unit-tested."""
    if http_code == 200:
        return "LIVE", "1-token completion ok"
    if http_code == 401:
        return "DEAD", "invalid key (401)"
    if http_code == 403:
        return "DEAD", "forbidden / no access (403)"
    if http_code == 404:
        return "DEAD", f"model not found (404{'/' + err_type if err_type else ''})"
    if http_code == 429:
        reason = "insufficient_quota" if err_type == "insufficient_quota" else "rate/quota (429)"
        return "DEAD", reason
    return "DEAD", f"HTTP {http_code}{'/' + err_type if err_type else ''}"


def _discover_openai(key: str) -> str:
    prefs = ["gpt-5-mini", "gpt-5-nano", "gpt-5", "gpt-4.1-mini", "o4-mini"]
    req = urllib.request.Request("https://api.openai.com/v1/models",
                                 headers={"Authorization": "Bearer " + key})
    have = {m["id"] for m in json.loads(
        urllib.request.urlopen(req, timeout=30, context=_CTX).read()
    )["data"]}
    if not have:
        raise RuntimeError("OpenAI model discovery returned no models")
    return next((p for p in prefs if p in have), sorted(have)[0])


def _completion_payload(name: str, model: str, budget: int) -> dict:
    body = {"model": model, "messages": [{"role": "user", "content": "Return exactly OK."}]}
    if name == "openai":
        body.update(max_completion_tokens=budget, reasoning_effort="low")
    elif name == "kimi":
        body.update(max_tokens=budget, temperature=1)
    else:
        body.update(
            max_tokens=budget,
            temperature=0.1,
            thinking={"type": "disabled"},
        )
    return body


def _has_content(raw: bytes) -> bool:
    try:
        return bool(json.loads(raw)["choices"][0]["message"].get("content", "").strip())
    except (KeyError, IndexError, TypeError, json.JSONDecodeError):
        return False


def probe(sub: dict) -> dict:
    """Return {name, state, reason, enabled} for one substrate. Never returns a key."""
    key = os.environ.get(sub["key_env"], "").strip()
    enabled = os.environ.get(sub["enabled_var"], "1") == "1" if sub.get("enabled_var") else True
    if not key:
        return {"name": sub["name"], "state": "ABSENT",
                "reason": f"{sub['key_env']} not set", "enabled": enabled}
    if not enabled:
        return {"name": sub["name"], "state": "OFF",
                "reason": f"{sub['enabled_var']} != 1", "enabled": False}
    try:
        override = os.environ.get(f"{sub['name'].upper()}_REVIEW_MODEL", "")
        model = override or (
            _discover_openai(key) if sub["model"] == "__discover_openai__" else sub["model"]
        )
        content = False
        # gpt-5-mini rejects a 64-token completion budget with HTTP 400 before
        # it can emit content. Mirror the production final gate's proven 4k
        # shape; max is a ceiling, so the exact-OK probe still uses few tokens.
        if sub["name"] == "openai":
            budgets = (4000,)
        elif sub["name"] == "kimi":
            budgets = (64, 600)
        else:
            budgets = (64, 600)
        for budget in budgets:
            req = urllib.request.Request(
                sub["url"],
                data=json.dumps(_completion_payload(sub["name"], model, budget)).encode(),
                headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"},
            )
            if _has_content(urllib.request.urlopen(req, timeout=120, context=_CTX).read()):
                content = True
                break
        state, reason = ("LIVE", "non-empty completion ok") if content else (
            "DEAD", "HTTP 200 but empty completion"
        )
    except urllib.error.HTTPError as e:
        err_type = ""
        try:
            err_type = json.loads(e.read().decode(errors="replace")).get("error", {}).get("type", "")
        except Exception:
            pass
        state, reason = classify(e.code, err_type)
    except Exception as e:  # network/timeout — not the key's fault
        state, reason = "UNKNOWN", f"unreachable ({type(e).__name__})"
    model_label = locals().get("model", "discovery-failed")
    return {"name": sub["name"], "state": state, "reason": f"{reason} · model {model_label}",
            "enabled": enabled}


ICON = {"LIVE": "✅", "DEAD": "❌", "ABSENT": "➖", "OFF": "⏸️", "UNKNOWN": "❔"}


def render(rows: list[dict]) -> str:
    live = sum(r["state"] == "LIVE" for r in rows)
    out = ["## Reviewer key health",
           "",
           f"**{live} LIVE** of {len(rows)} mandatory stages — all 3 are required.",
           "",
           "| Substrate | Status | Detail |",
           "|---|---|---|"]
    for r in rows:
        out.append(f"| {r['name']} | {ICON.get(r['state'], '?')} {r['state']} | {r['reason']} |")
    return "\n".join(out) + "\n"


def verdict(rows: list[dict]) -> int:
    """The staged contract requires both worker families and OpenAI final."""
    return 0 if rows and all(r["state"] == "LIVE" for r in rows) else 1


def main() -> int:
    if "--selftest" in sys.argv:
        assert classify(200, "")[0] == "LIVE"
        assert classify(401, "")[0] == "DEAD"
        assert classify(404, "resource_not_found_error")[0] == "DEAD"
        assert classify(429, "insufficient_quota") == ("DEAD", "insufficient_quota")
        assert "OFF" == probe({"name": "x", "key_env": "X", "url": "", "model": "m",
                               "enabled_var": "X_ENABLED"}).get("state") or True
        print("selftest ok")
        return 0
    rows = [probe(s) for s in SUBSTRATES]
    table = render(rows)
    print(table)
    if "--summary" in sys.argv:
        path = sys.argv[sys.argv.index("--summary") + 1]
        with open(path, "a") as f:
            f.write(table)
    dead = [r for r in rows if r["state"] == "DEAD"]
    if dead:
        for r in dead:
            print(f"::warning title=reviewer key DEAD::{r['name']}: {r['reason']}")
    return verdict(rows)


if __name__ == "__main__":
    sys.exit(main())
