# STATE.md vs current reality — audit
**Target:** `Amplified-Partners/ground-truth/STATE.md` @ commit `220cf72` (last touched 2026-05-01 19:41 UTC, written by Devin, edited by Devon)
**Auditor:** Sam (Claude Sonnet, Perplexity Computer)
**Method:** Same shape as PR #3 spine-blanks audit. Each finding cites STATE.md line numbers and the source(s) that contradict.
**Date:** 2026-05-05 02:50 BST (78 hours after STATE.md was last touched)

---

## Lane declaration

Cassian's role-proposal for Sam (this thread, 2026-05-05) was: line-numbered, citation-anchored, machine-readable gap audits across authority docs. STATE.md is the canonical narrative state document. This is the first audit in that lane after the spine-blanks audit (PR #3).

## Bias declarations

- I am Claude Sonnet (Perplexity Computer). Two of five agents in tonight's reorg are Claude (Sam + Mirror). My audit framing should not assume Claude's view is neutral.
- I have not pre-coordinated with Devin or Devon (the named authors of STATE.md and VERIFICATION.md). This is independent.
- `[ASSUMED]` confidence levels are mine; if you disagree, mark them.

## What I checked against

| Source | Date | Why it overrides STATE.md |
|---|---|---|
| `Amplified-Partners/ground-truth/VERIFICATION.md` | 2026-05-03 | Newer, signed by Devon, evidence-backed (5 linked Devin sessions, SSH + API + line counts) |
| `Amplified-Partners/clean-build/STATUS.md` | 2026-04-30 v2 (current head) | Authority status board, marked `status: authoritative` |
| `Amplified-Partners/clean-build/00_authority/EIGHT_LAWS.md` | exists, 3002 bytes, sha 43a4043 | Direct contradiction with "four principles" framing |
| GitHub org repo list (live, 2026-05-05 02:50 BST) | now | Repo count |
| `Amplified-Partners/byker-production` last commit | 2026-02-07 | Activity vs claimed "live" status |
| `Amplified-Partners/perplexity-research` repo | created 2026-05-04 | Whole new layer not in STATE.md |

---

## Findings — table

| # | STATE.md line(s) | Severity | Quoted claim | Current reality | Source |
|---|---|---|---|---|---|
| 1 | 51 | **DRIFT** | "**The four principles come from Ray Dalio — directly.** Radical Honesty. Radical Transparency. We added Radical Attribution and Win-Win / Idea Meritocracy." | clean-build authority dir contains `EIGHT_LAWS.md` (3002 bytes, sha `43a4043`) referenced as "8 layer-0 laws [AUTHORITATIVE]" by `corpus-raw/ewan-map/2026-04-23_amplified-partners-map_v1.md` and as "above everything else" by `ground-truth/OPENCLAW.md`. Either the four are a derivation/subset of the eight, or one doc is wrong. STATE.md doesn't acknowledge the eight at all. | `clean-build/00_authority/EIGHT_LAWS.md` exists; `ground-truth/OPENCLAW.md` cites it as canon |
| 2 | 117 | **STALE** | "The decision was made to replace **FalkorDB** with **Neo4j 5.26+**, keep Graphiti as the knowledge extraction framework, and keep Qdrant for vectors while a migration plan is worked through." | `VERIFICATION.md` (2 days later) line 45: "**FalkorDB** — Knowledge graph. 8,841 nodes across 2 active graphs. Running and populated." Migration not done; FalkorDB still the live knowledge graph on the Beast. Decision either reversed, deferred, or never executed. | `ground-truth/VERIFICATION.md:45` |
| 3 | 119 | **STALE** | "**Byker** is the codename for the production system now running on Railway. It is working." | `Amplified-Partners/byker-production` last commit `22ff950` dated 2026-02-07 — 87 days before STATE.md was written, 90 days before today. `VERIFICATION.md:91` flags `byker-production` as "**dormant** / to decide" with question "still relevant?". STATE.md was already stale on 2026-05-01 about this; got staler since. | repo commit history; `VERIFICATION.md:91` |
| 4 | 182 | **DRIFT** | "FalkorDB ... 9,000 nodes across 4 graphs: `business_knowledge` ... `amplified` ... `amplified_brain` / `amplified_graph` — scaffolded, empty" | `VERIFICATION.md:45` (2 days later, SSH-verified): "8,841 nodes across **2 active graphs**". The two scaffolded-empty graphs (`amplified_brain`, `amplified_graph`) appear to be gone or excluded from VERIFICATION's count. Node count drifted by 159. | `ground-truth/VERIFICATION.md:45` |
| 5 | 189 | **DRIFT** | "**35+ containers total** on Docker network `amplified-net`." | Two newer authoritative sources disagree both with STATE.md and with each other: `clean-build/STATUS.md` v2 (2026-04-30) says **40 containers total** (37 running, 1 paused, 2 stopped). `VERIFICATION.md` (2026-05-03) says **37 Docker containers running**. STATE.md's "35+" is a lower bound that's now misleading. Pick one number; the trio together is the kind of cross-doc drift Cassian's P0 audit calls out. | `clean-build/STATUS.md`; `ground-truth/VERIFICATION.md:35` |
| 6 | 23 | **DRIFT** | "Vault backup risk — `/opt/amplified/vault/` still needs confirmed git remote sync" | `Amplified-Partners/vault` repo had a 5-week dormancy gap (last commit before tonight: 2026-03-28). Tonight (2026-05-05 02:14–02:19 UTC) it received Dependabot config + Copilot config commits — proving the *repo* is now active, but **`[NOT CHECKED]` whether the Beast `/opt/amplified/vault/` actually rsyncs/pushes to it**. STATE.md flags the risk; nothing in STATE.md or VERIFICATION.md confirms resolution. | `vault` commit history c65b874, f5d7cdc, c0fb940 |
| 7 | 196 | **POTENTIAL DRIFT** | "**SSH access (Devon M4):** `ssh -i ~/.ssh/devin_beast_key root@135.181.161.131`" | `[NOT CHECKED]` — I cannot verify SSH key state from outside the Beast. Flag: this is the kind of credential claim that goes stale silently. VERIFICATION.md:5 confirms SSH was used 2-3 May 2026 by Devin sessions, so the key worked then. Not a current contradiction; flagging as a class of claim to track. | n/a |
| 8 | 14 | **STALE** | "**CRM live with Dave Jesmond** — first real client end-to-end \| Ewan + Devon \| Close to live. CRM working, persistence solid, API auth in place." | `VERIFICATION.md` (2026-05-03) lists "**First client live** — Dave Jesmond / Jesmond Plumbing. CRM is ready. What's between here and live?" as an *open decision* (line 203). Status across 3 days: "Close to live" → still "open". No movement reported. | `ground-truth/VERIFICATION.md:203` |
| 9 | 5 (header) | **STALE** | "**As of: 2026-05-01**" | STATE.md has not been touched since 2026-05-01 19:41 UTC (commit `220cf72`). 78 hours have elapsed; in those 78 hours: VERIFICATION.md was created (2026-05-03), 5 Devin sessions ran, 7 dedup PRs merged (181 files deleted, 41,581 lines removed), `perplexity-research` repo was created (2026-05-04), 9 PRs were opened in that repo, 4 reorganisation plans were drafted by 4 different agents, and the spine-blanks audit (59 substantive gaps in clean-build) ran. None of this is in STATE.md. | every commit in the org since 2026-05-01 19:41 UTC |
| 10 | entire doc | **GAP** | (Doc does not mention) | STATE.md has zero references to: `perplexity-research` repo, the 2026-05-04 reorg work, the 4-plan parallel build, Antigravity / Mirror / Cassian / Sam as agent identities, the spine-blanks audit, the substrate diversity question, or VERIFICATION.md itself. The "Current Priorities" dashboard at the top (lines 8–25) is the most-updated section and is also the most-stale: priorities have shifted but the dashboard hasn't. | grep across STATE.md returns 0 hits for any of these terms |
| 11 | 162–166 | **STALE** | "**Bob** ... Running but cold — first live client is Dave Jesmond / Jesmond Plumbing." & "**The Marketing Suite** ... Spec exists, partial code." | `VERIFICATION.md:42` (2 days later): "**Marketing Engine** ... Running but daily cron broken (quote escaping bug — fixable in 10 minutes)". Marketing pipeline is further along than "spec + partial code" — it's running on Beast cron, just bug-blocked. STATE.md understates progress. | `ground-truth/VERIFICATION.md:42` |
| 12 | 181 | **DRIFT** | "On the Core (Hetzner AX162-R `135.181.161.131`, hostname `amplified-core`)" | `VERIFICATION.md:32` confirms "Hetzner AX162-R" but spec line in ground-truth `INFRASTRUCTURE.md` was corrected on 2026-05-03 (commit `035df63`: "fix: correct RAM spec to 256 GB DDR5 (hardware spec, not usable after kernel)"). Implies STATE.md's blanket "256GB DDR5 RAM" (line 115) is hardware-correct but does not flag the kernel-usable distinction Devon called out 2 days later. Minor but a real correction other docs absorbed. | ground-truth commit `035df63` |
| 13 | 220 | **STALE** | "10-agent marketing swarm scaffolded (Unit Gamma in clean-build)" | `[NOT CHECKED]` whether this is still the active framing. Unit Gamma not mentioned in `VERIFICATION.md`. May still be true; flagging as a claim that nothing newer confirms or denies. | n/a |
| 14 | 246 | **PROCESS DRIFT** | "*Edited: Devon \| 2026-05-01 \| session 873af571838a40d29455d1579d2e7d75 — added Current Priorities dashboard, updated API key status (rotated), renamed Chit → Sidecar*" | `clean-build/00_authority/SIGNATURES.md` mandates session-ID signing on every authority commit. Commit `220cf72` signs in the footer text but the git author/committer is `devin-ai-integration[bot]`, not a named human accountable. Authority spine signature standard is being met in the doc body but not via git identity. Process question for Cassian/Devon, not necessarily an error. | `clean-build/00_authority/SIGNATURES.md`; commit `220cf72` |

---

## Summary by severity

| Severity | Count |
|---|---|
| BLOCKER | 0 |
| STALE | 5 (#2, #3, #8, #9, #11) |
| DRIFT | 5 (#1, #4, #5, #6, #12) |
| POTENTIAL DRIFT | 1 (#7) |
| GAP | 1 (#10) |
| PROCESS DRIFT | 1 (#14) |
| Out of scope (flagged) | 1 (#13) |
| **Total findings** | **14** |

## Highest-leverage finding

[OPINION confidence 85%] **#10 (the GAP).** Five stale entries can each be fixed with a one-line edit. The gap — STATE.md is silent on perplexity-research, the 4-agent reorg, VERIFICATION.md, and tonight's plan layer — is structural. STATE.md is supposed to be the *narrative* state of the project. The narrative has moved on without it. Fix shape: STATE.md needs a "What changed since 2026-05-01" section or a successor doc, not just inline edits.

[OPINION confidence 75%] **#1 (four vs eight).** This is the cross-repo consistency drift Cassian flagged in the original lane proposal. Worth resolving: either ground-truth/STATE.md is wrong about "four principles" or clean-build/EIGHT_LAWS.md is over-specified. One of them is the canon; the other is downstream documentation that needs to match.

## What I did NOT audit (out of this lane's scope, flagged for the next pass)

- `clean-build/STATUS.md` cross-checked against current container state on the Beast (need SSH; not in my lane).
- The 14 INFRASTRUCTURE-related claims in `clean-build/02_build/INFRASTRUCTURE.md` (referenced by STATUS.md but not pulled here).
- `ground-truth/AGENTS.md` agent-routing model vs the actual agents who pushed PRs tonight (Antigravity, Mirror, Cassian, Sam, Devon, Devin) — that's a separate audit.
- The 5 namespace-misconfigured repos under `ewan-dot/` that VERIFICATION.md says still need Ewan to fix.

## Machine-readable output

JSON sidecar: `inbox/2026-05-05-state-md-audit/findings.json`

---

## Self-grade (filled before submit)

Against the plan I laid down at `/home/user/workspace/sam-plan-2026-05-05-audit-lane.md`:

- **Did I fix BOTH of Devin's findings?** Yes. Hardcoded paths replaced with argparse + env vars; comment/code mismatch fixed by introducing `--context-lines` parameter and matching code window to comment claim. Smoke-tested. Pushed to `sam/2026-05-04-spine-blanks` as commit `9df8659`.
- **Did STATE.md audit produce line-numbered, citation-anchored output?** Yes. Every finding has a line number from STATE.md and at least one external source.
- **How many gaps did I find?** 14 findings. 0 blocker, 5 stale, 5 drift, 1 potential drift, 1 GAP (structural), 1 process drift, 1 out-of-scope flag.
- **What did I miss?** [ASSUMED] At least three things I would expect a reviewer to catch:
  1. I did not verify SSH key state (#7) or test-execute any of the live infra claims. Out of lane but should be flagged for someone who can.
  2. I treated VERIFICATION.md as authoritative-newer for cross-checking. It is signed by Devon and evidence-backed, but I did not independently verify Devon's evidence — I'm chaining one agent's audit into mine. If VERIFICATION.md is wrong, my audit inherits the error.
  3. I did not audit Mirror's PR #6 or Devon's PR #8 in this pass (Cassian's P1 items). Deliberate scope choice; logged so future-Sam picks them up next.
- **Did I drift into commenting on things outside my lane?** [OPINION confidence 70%] Borderline on finding #14 (process drift on git-author signing). That's a governance question, not a doc-fact question. Flagged it as PROCESS DRIFT to keep it visible without claiming authority on the resolution.
- **Phantom precision check — every number traceable?** Going through them:
  - "78 hours elapsed" — from STATE.md commit timestamp 2026-05-01 19:41 UTC to now 2026-05-05 01:50 UTC ≈ 78.15 hours. ✓
  - "9,000 nodes" / "8,841 nodes" — both directly quoted from source docs. ✓
  - "35+ containers" / "37 containers" / "40 containers" — all directly quoted. ✓
  - "5 Devin sessions" / "76 PRs" / "32 repos" / "33 repos" — all from VERIFICATION.md or live `gh api` count. ✓
  - "181 files / 41,581 lines" — from VERIFICATION.md:125. ✓
  - "59 substantive gaps" (PR #3) — from my own previous audit. ✓
  - "9 PRs" in perplexity-research — `[ASSUMED]` from continuity context; not freshly verified in this session. **Phantom-precision risk on this single number.**
- **One-of-five-Claude framing** — held in bias declarations, did not pretend my audit was substrate-neutral.

---

*Signed: Sam (Claude Sonnet, Perplexity Computer)*
*Session date: 2026-05-05 02:50 BST*
*Plan-loop: Plan filed at `/home/user/workspace/sam-plan-2026-05-05-audit-lane.md` before work started. This audit closes that loop.*
