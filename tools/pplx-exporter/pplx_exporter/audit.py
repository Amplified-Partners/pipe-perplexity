"""Audit log — JSONL append-only accountability trail."""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path


def _now() -> str:
    return datetime.now(UTC).isoformat()


def _append(path: Path, entry: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def audit_run_start(path: Path, run_id: str) -> None:
    _append(path, {"ts": _now(), "event": "run_start", "run_id": run_id})


def audit_run_end(path: Path, run_id: str, total: int) -> None:
    _append(path, {"ts": _now(), "event": "run_end", "run_id": run_id, "total_exported": total})


def audit_discovery_complete(path: Path, count: int) -> None:
    _append(path, {"ts": _now(), "event": "discovery_complete", "thread_count": count})


def audit_thread_fetched(path: Path, slug: str, byte_count: int, sha: str) -> None:
    _append(path, {"ts": _now(), "event": "thread_fetched", "slug": slug, "bytes": byte_count, "hash": sha})


def audit_thread_failed(path: Path, slug: str, error: str, retry: int) -> None:
    _append(path, {"ts": _now(), "event": "thread_failed", "slug": slug, "error": error, "retry": retry})
