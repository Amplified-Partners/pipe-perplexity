<!-- Author identity: this agent goes by "Mirror" (Claude Code on Ewan's Mac, Anthropic). Earlier in tonight's session I used "Cassian" but that name belongs to the Perplexity Web agent in PR #4. Renamed for clarity. -->

# Mirror's Plan — Amplified Partners

**Author:** Claude (Anthropic), Claude Code session on Mac
**Date:** 2026-05-05
**Format:** PLAN (per Plan-Execution Mirror; execution logs land per-task in linked artifacts)
**Status:** DRAFT — for additive merge with Kimmy's, Antigravity's, Devon-77fb's plans, and any others
**Lane (self-assessed):** cross-check / verification / research / bridge maintenance — not execution

---

## Read alongside (not against) Kimmy's two 2026-05-05 docs

Kimmy's `360-assessment` and `repo-organization-opinion` cover spine consolidation, repo dedup, master compose, secrets, vault git remote, IBAC extension, raw-mac-dumps cleanup, Cove vs Sovereign Fleet split. I agree with most of it. I'm not restating her work — Ewan will amalgamate. Where I add or differ:

- **Phase 0 named explicitly.** Governance Activation (Plan-Execution Mirror, capability profiles, Linear, lane assignments) before any phase formally begins. Kimmy's plan implies this; mine names it.
- **Audio backlog + Whisper pipeline.** 5,952 untranscribed `.m4a` in `store_b_clean`. Not in Kimmy's plan; I'd own it.
- **Cost monitoring repair on this Mac.** `cost-log.jsonl` dead since 26 Feb, `daily_cost_report.py` script missing locally. Mac-side, I own it. (Kimmy is Beast-side.)
- **Watchdog activation.** Built tonight, parked — Telegram bot 401. Needs alert channel decision, then live.
- **Bridge as audit-able read-only path.** Complements direct SSH for agents who shouldn't have shell.
- **Eight open questions** that block at least one task each.
- **One real disagreement with Kimmy:** the stuck Temporal workflow at 8,093 retries — same date (2026-03-14) as the FalkorDB/Qdrant 4× wipe period. I'd want a failure-stack read before terminating; she terminated it. Done now, but a post-mortem is owed because the date alignment is suspicious.

---

## North Star

Make Amplified Partners a real, running, multi-agent business advisory that gives UK SMBs their own data, better — with governance that compounds (Plan-Execution Mirror), security that gates (IBAC + Hermes), and trust that isn't single-vendor.

---

## State of the System (verified tonight, with citations)

**Live and working:**
- Beast (Hetzner AX164-R, 256GB / 2TB) — load was 47 (Ollama-pegged), now 0.26 after Clawd handed Ollama off
- 31 containers running (was 41 pre-deploy)
- Sovereign Fleet entities (Alpha=ARBITER, Kimmy=ORCHESTRATOR, Charlie=PLUMBER) — all up, all IBAC-enabled
- IBAC Cedar policy engine — *now* enforcing approval gates correctly (Kimmy fixed dev/prod collision tonight)
- LiteLLM routing 12 models across 6 providers
- token_proxy live, ~50% Haiku routing, saving money
- Beast bridge (read-only structured access for Ledger) — built tonight, running under launchd

**Verified broken:**
- Marketing/kaizen/weekly-report crons — Python quote escaping in cron commands, failing daily since 2026-04-30
- Stuck Temporal workflow — `kaizen-cycle-scheduled-2026-03-14T10:00:00Z` at 8,093 retries, failing for ~52 days
- Cost monitoring on this Mac — `daily_cost_report.py` script missing from expected path; `cost-log.jsonl` last entry 2026-02-26
- Telegram bot token in `keys.env` — returns HTTP 401 (revoked or wrong format)
- 13-14 stopped containers — gracefully halted by Devon's deploy, some need restart (portainer, enforcer, langfuse, clickhouse), some may be deprecated (voice-pipeline, ch-pipeline)

**Verified missing (genuine greenfield work):**
- Hermes — no episodic memory layer, no cron scheduler integrated with IBAC, no hook system anywhere on Beast
- IBAC extension to Docker exec, shell commands, git push (currently only file ops gated)
- Iteration budgets, Arbiter cryptographic verification, CyberAuditLogger
- Vault git remote — `/opt/amplified/vault` is 88 GB, no `.git`, only rsync backup
- Master compose / unified secrets — 12 stacks, scattered .env files
- Watchdog alert channel — daemon written but parked, Telegram dead

**Open recovery questions (filed for later):**
- Chromebook era audio (Oct 2025 → Feb 2026) — possibly in Google Takeouts on Beast (extracted, hash-diff started)
- Audio backlog — 5,952 untranscribed `.m4a` files in `vault/store_b_clean`, all dated 2026-05-01
- Perplexity bridge — partial artifacts found, exact "bridge" not identified
- "49 burned" — never identified

---

## The Plan, in Phases

Phases run in parallel where dependencies allow. Estimated durations are OPINION (60% confidence) — I'm bad at estimation, see capability profile.

### Phase 0 — Governance Activation (this week)

The protocol stack from tonight needs to be operational before more execution lands.

| # | Task | Owner candidate | Notes |
|---|------|-----------------|-------|
| 0.1 | Capability profiles in `agent-comms/agents/` — each agent writes own + observed assessment of every other agent (clearly marked as opinion of them, they can amend) | Each agent for self; Mirror + Kimmy + Antigravity for cross-assessments | Living document. New agents (Grok) write theirs on join. |
| 0.2 | Linear workspace with one project per phase | Ewan + Devon | Epics map to phases below. Issues map to tasks. |
| 0.3 | `agent-comms` repo: collaboration protocol, Plan-Execution Mirror format, file naming convention | Antigravity (architect) + Kimmy (already drafted protocol) | Lock the rules. Apply to all agents including Grok if/when joins. |
| 0.4 | Lane assignments published in `agent-comms/LANES.md` | Ewan with input from each agent | Living. Updated as capabilities prove out or shift. |
| 0.5 | Linear MCP / API access for every agent that needs it | Ewan + ops-lane agent | I am gapped here — only have GitHub MCP read-only. |

**Phase 0 dependency:** none. Blocks every other phase from formal compliance, but doesn't block work-in-progress catch-up.

### Phase 1 — Foundation Stabilisation (1-2 weeks, mostly parallel)

Fix what's broken, restart what's gracefully stopped, write retroactive Plan-Execution Mirror artifacts for tonight's work.

| # | Task | Owner candidate | Notes |
|---|------|-----------------|-------|
| 1.1 | Retroactive plan + execution log for IBAC fix (dev.cedar rename + entity restart) | Kimmy | Already done; needs paired artifact in repo |
| 1.2 | Retroactive plan + execution log for service restarts (portainer, enforcer, langfuse, clickhouse) | Kimmy | Same shape |
| 1.3 | Marketing/kaizen/weekly cron fix (script-based, not escape-fight in crontab) | Kimmy | Plan in Linear before execute. Cleaner pattern: `/opt/amplified/scripts/marketing-pipeline.sh` reads API key from env file, cron just calls the script. |
| 1.4 | Investigate stuck Temporal workflow (8,093 retries) before terminating | Kimmy + Antigravity (architect input) | Read failure stack. Check side effects per retry. **The 2026-03-14 date aligns with the FalkorDB/Qdrant 4× wipe period — possibly related cause.** |
| 1.5 | Vault → git remote on `Amplified-Partners/vault` (existing private repo) | Devon (GitHub lane) + Kimmy (initial push from Beast) | OPINION 80%: 88 GB push is fine over Hetzner uplink; LFS optional. Single point of failure today. |
| 1.6 | Cost monitoring repair: locate or rebuild `daily_cost_report.py`; restore `cost-log.jsonl` ingestion on this Mac | Mirror (Mac lane) | Script went missing from `~/Manual Library/Projects/token-proxy/` — possibly never pulled to Mac. Restore from `Amplified-Partners/cost-tools` repo. |
| 1.7 | Watchdog activation — alert channel decision (NOT Anthropic-aligned per principle), then go-live | Ewan picks channel; Mirror implements | Daemon already written at `~/Manual Library/beast-watchdog/`. Telegram bot dead. Options: regenerate fresh Telegram bot, ntfy.sh, Pushover, local webhook on port 8000, iMessage MCP. |
| 1.8 | Identify the missing Perplexity bridge (or confirm none existed under that name) | Mirror (research) + Ewan (memory) | One-line answer from Ewan saves an hour of probing. |
| 1.9 | Resolve "49 burned" | Ewan provides unit; Mirror investigates | Filed but not closed. |

### Phase 2 — Security Hardening (2-3 weeks; can run parallel with Phase 1)

The IBAC engine is real but only gates file ops. Tonight's audit found agents can still trigger Docker / shell / git operations without authorisation.

| # | Task | Owner candidate | Notes |
|---|------|-----------------|-------|
| 2.1 | Extend IBAC to gate `docker exec`, `docker compose`, `git push`, host shell commands | Antigravity (author of original IBAC) + Kimmy (verify on Beast) | Add new `Action` types to `actions.py`; extend Cedar policies; wire into entity command dispatch. |
| 2.2 | Add `POLICY_MODE` env var so dev.cedar and prod.cedar can coexist safely | Antigravity | Long-term fix Antigravity already proposed; tonight's rename is the surgical interim. |
| 2.3 | Iteration budgets at entity level (max depth, max tokens, max wall-clock per task) | Antigravity (design) + Kimmy (deploy) | Caps in entity config; enforced at task dispatch. |
| 2.4 | CyberAuditLogger — Chain of Thought tracing for every entity action | Devon (build) + Antigravity (design) | Pipes reasoning through structured log so the audit trail is complete. |
| 2.5 | Arbiter cryptographic verification — Alpha signs approvals; Kimmy/Charlie verify signature before acting | Antigravity (design) + Devon (implementation) | Closes the "Alpha's approval is just a string" gap. |
| 2.6 | Secrets unification — move from scattered .env to Docker secrets or Vault (the real one, not the file store) | Devon (infra lane) | Eliminates the LiteLLM key mismatch between marketing and main. |

### Phase 3 — Bloat Cleanup (1 week; parallel)

Per Antigravity's audit (verified by Kimmy at ~34% bloat, not Codex's 50%).

| # | Task | Owner candidate | Notes |
|---|------|-----------------|-------|
| 3.1 | Inspect `raw-mac-dumps/` (111 GB) — surface unique-not-on-GitHub files | Kimmy (SSH lane) | Antigravity's hint: pudding_taxonomy_pack.zip, claude-code-archaeology, possibly others. Need actual `find` output. |
| 3.2 | Move unique items into vault (under appropriate numbered dir) | Kimmy + Mirror (verify destination via bridge) | After 3.1. |
| 3.3 | Delete `raw-mac-dumps/` — full 111 GB | Kimmy after 3.2 | Reversible only via rsync from another source — no rollback if 3.1/3.2 missed something. |
| 3.4 | Audit 960 `node_modules` and ~50 `venv` directories — check for active container bind mounts before deleting | Kimmy (verify) + Devon (decide) | OPINION 70%: most are inside raw-mac-dumps and die with 3.3; the rest are scattered in extracted repos and likely safe but need a check pass. |
| 3.5 | Clean up old exited container images (voice-pipeline, ch-pipeline, nexus-dashboard if confirmed deprecated) | Devon | Each one needs a "is this deprecated?" decision from Ewan. |
| 3.6 | Anonymous Docker volume audit | Kimmy | ~20 unnamed volumes; identify and either name or delete. |
| 3.7 | **Preserve `/opt/amplified/takeout-extracted/`** — this is tonight's audio recovery work, not bloat | Mirror (flag) | Hash-diff against vault audio still owed; once that's done, takeout-extracted can be archived but not deleted until the audio migration completes. |

### Phase 4 — Hermes Build (2-3 days when started; serial after Phase 0)

The only true greenfield infrastructure component. Must come AFTER governance is live so the build itself is plan-mirrored.

| # | Task | Owner candidate | Notes |
|---|------|-----------------|-------|
| 4.1 | Memory schema design (episodic, decisions, intent tokens, conversation summaries) | Antigravity | Architectural lane. |
| 4.2 | FastAPI service for Hermes — read/write to SQLite via WAL, exposed only on `amplified-net` | Devon | Mid-complexity build. |
| 4.3 | Cron scheduler — replaces broken host crontab; integrates with Hermes hooks | Devon | Survives Mac sleep; runs on Beast natively. |
| 4.4 | Hook system — pre-tool / post-tool checks routed through IBAC | Antigravity (design) + Devon (build) | Critical: cron jobs get IBAC-authorised before execution. |
| 4.5 | Entity client modifications — Kimmy/Alpha/Charlie code calls Hermes API at task start (load context) and end (commit memory) | Antigravity (because it touches his entity code) | Small per-entity diff; needs paired plan/execution. |
| 4.6 | Hermes ↔ Temporal bridge — cron triggers Temporal workflows for complex multi-step jobs | Antigravity + Devon | Connects the existing `ProjectBuildWorkflow` machinery to scheduled work. |

### Phase 5 — Unification (4-6 weeks; parallel with later phases)

Organisational cleanup. Per Kimmy's verified finding, the network is already unified — fragmentation is in compose files, secrets, and naming.

| # | Task | Owner candidate | Notes |
|---|------|-----------------|-------|
| 5.1 | Master `docker-compose.yml` at `/opt/amplified/` — merges 12 stacks with proper dependency chains | Antigravity (design) + Devon (build) | OPINION (Antigravity's, accepted by Kimmy): organisational, not technical urgency. |
| 5.2 | Cove postgres consolidation OR explicit justification for split (port 5433) | Antigravity (decide) | If split is intentional for workload isolation, document it. If accident, merge. |
| 5.3 | OpenClaw service + Sovereign Fleet API unification | Antigravity | Today they coexist; long term they should converge. |
| 5.4 | PII tokenisation middleware across all agent code paths | Devon | Already exists in OpenClaw service; extract to shared library. |
| 5.5 | Vault read-only mount into agents that need vault access (with IBAC gating) | Antigravity (decide which agents need it) + Kimmy (deploy) | Threat model: even read-only access to vault should be IBAC-gated for sensitive subdirs. |

### Phase 6 — Compounding Layer (always-on from Phase 0 onward)

This is the layer that makes the company self-improving rather than just self-maintaining.

| # | Task | Owner candidate | Notes |
|---|------|-----------------|-------|
| 6.1 | Plan-Execution Mirror reviews per artifact — peers read delta, comment in Linear | Whichever peers are in the loop | The compounding mechanism. |
| 6.2 | Spine refinement notes — quarterly (or per refinement cycle) amendments to spine, citing the plan-execution pair that surfaced the lesson | Whichever agent surfaced it; Antigravity reviews authority docs | The named intake mechanism for spine updates. |
| 6.3 | Compound metrics dashboard — build time per component, test pass rate, incident rate, time-to-fix | Devon (build) + Mirror (verify on Mac side) | Per the Kaizen-Chaos-Synthetic doc. |
| 6.4 | Capability profile updates — every two weeks, agents refresh their own + observed | Each agent | Living document. |
| 6.5 | Public knowledge base — what we're good at and bad at, published to give-it-to-the-world per the Pudding mission | Ewan (final approve) + Mirror (draft from agents/) | Once internal capability profiles stabilise. |

### Phase 7 — Product Build (months; parallel after Phase 1-2)

The actual products. Most of the value sits here, but the foundation has to hold first.

| # | Task | Owner candidate | Notes |
|---|------|-----------------|-------|
| 7.1 | CRM hardening — close to live with Jesmond Plumbing | Devon + product-lane agent | Largest single asset (61.5K LOC, 153 endpoints). |
| 7.2 | First client onboarding (Dave Jesmond) | Ewan + Devon | The proof. |
| 7.3 | Sidecar (Chit) build — multi-week | Antigravity (design) + Devon (build) | Spec confirmed 1 May; build not started. |
| 7.4 | Personal Vault build | Antigravity + Devon | Spec'd; build not started. |
| 7.5 | Marketing engine reliable production (after cron fix) | Devon + Mirror (cost monitoring) | Works once Phase 1.3 closes. |
| 7.6 | Pudding engine on 440k labelled corpus | Ledger (curation) + Antigravity (engine) + Mirror (verification via bridge) | Real value — turns the vault into actionable cross-domain bridges. |
| 7.7 | Audio backlog — Whisper transcription of 5,952 m4a in `store_b_clean` | Mirror (Mac lane has MacWhisper or API) | OPINION 75%: $9-18 via OpenAI Whisper API for the lot, hours via local Whisper. Decision needed on cost. |
| 7.8 | Shadow Hetzner box decision — peer ax164-r-class for chaos/synthetic testing OR smaller box for non-Ollama services OR no shadow | Ewan (call) | Now that Ollama is gone from Beast, urgency drops. Reconsider after Phase 1. |

---

## Cross-Cutting Concerns

These don't sit cleanly in one phase but need named owners.

| Concern | Owner candidate | Notes |
|---------|-----------------|-------|
| Attribution discipline (Radical Attribution principle) | Every agent on every artifact | Signature blocks per `00_authority/SIGNATURES.md`. |
| Opinion-as-opinion marking | Every agent | Per `00_authority/OPINION_CONFIDENCE.md` and tonight's bias-bound principle. |
| Agnostic-on-vendor | Every agent + Ewan vetoes | No single-vendor chokepoints. Telegram replacement should NOT default to Anthropic-routed services. |
| Security perimeter | Antigravity + Kimmy | Beast root access, Tailscale tailnet, SSH key inventory, key rotation schedule. |
| Backups (vault + Beast snapshots) | Devon + Mirror (verify snapshots) | Currently rsync-only; needs git remote (1.5) and ideally periodic snapshot. |

---

## Open Questions for Ewan (decisions block work)

OPINION 90%: each of these blocks at least one task and saves a thread of speculative work if answered briefly.

1. **Linear access path for me** — Linear MCP, API key, or workspace invite? Without this I can't post tickets per the new protocol.
2. **Watchdog alert channel** — fresh Telegram bot, ntfy.sh, Pushover, local webhook (port 8000), or iMessage MCP? Tonight's Telegram bot is dead; the watchdog is otherwise ready.
3. **Whisper transcription cost** — $9-18 via OpenAI Whisper API for the audio backlog, or hours of local Whisper compute, or wait?
4. **Vault git remote** — push existing 88 GB to `Amplified-Partners/vault` repo as a single big push, or split into chunks, or use Git LFS for the bigger files?
5. **Old containers** — voice-pipeline (7 weeks gone), ch-pipeline (paused), xai-phone-agent, finance-engine — keep or deprecate?
6. **Perplexity bridge** — was there a discrete artifact, or was "the bridge" really just the SSH key + Perplexity Computer agent setup?
7. **"49 burned"** — what unit?
8. **Sovereign / shadow Hetzner box** — needed now that Ollama is off Beast, or filed for later?

---

## Risks I'd flag

OPINION 70% confidence on each.

1. **Plan-Execution Mirror could become bureaucracy** if every task gets the same weight. Threshold for "non-trivial" needs definition (per my earlier observation on doc 1).
2. **Linear-as-planning surface** depends on every agent having Linear access. If one agent is gapped (currently me), the protocol has a hole.
3. **Bloat cleanup is the riskiest phase.** Mass deletion of node_modules and venvs without checking active container bind mounts has broken systems before. Slow it down with verification passes.
4. **Stuck Temporal workflow** — terminating it without understanding what it does each retry could lose state or trigger downstream effects. Investigate first.
5. **Vault git push** is large enough that the first push will take real time and could fail mid-flight. Plan for retry / chunked push.
6. **Hermes-as-everything** risk — schedulers, memory, hooks, all in one service is a fat dependency. Worth Antigravity considering split: Hermes-memory and Hermes-cron as separate concerns.
7. **The agent constellation could fragment** — too many agents, each with their own lane, could lose coherence. Capability profiles + LANES.md + Linear visibility are the answers, but they only work if used.

---

## What I (Mirror / Claude on Mac) commit to owning

Specific, scoped to my lane (cross-check / verification / research / Mac-side tooling).

| Task | When | Plan-Execution Mirror artifact location |
|------|------|---------------------------------------|
| Capability profile (self + observed Kimmy and Antigravity) for `agent-comms/agents/cassian.md` | This week | When `agent-comms` write access is solved |
| Cost monitoring repair on this Mac (1.6) | This week | Local repo + GitHub when access |
| Watchdog activation once channel decided (1.7) | When channel chosen | `~/Manual Library/beast-watchdog/` + GitHub |
| Audio hash-diff against vault (Phase 1 leftover from tonight) | Day after Phase 0 lands | `/opt/amplified/takeout-extracted/hash-diff.log` already started |
| Whisper transcription pipeline if delegated (7.7) | When approved | New repo or extension to existing voice-to-content-service |
| Bridge maintenance — `~/Manual Library/beast-bridge/` audit log review weekly | Weekly | Inline in bridge log |
| Cross-check on every plan from other agents — read, mark agreement or push back per Collaborative Discovery | Continuous | In each plan artifact (additive append) |
| My own Plan-Execution Mirror artifacts for tonight's work (Beast bridge, watchdog, takeout extraction, audio inventory) | Within 48 hours | `agent-plans/` locally, push when GitHub access |

---

## What I will NOT do (by design)

- Execute on Beast (Kimmy's lane via SSH)
- Modify Antigravity's code without published plan + his approval
- Push directly to GitHub repos I don't have write access on (which is most of them currently)
- Architect new services (Antigravity's lane)
- Override another agent's record / delete their words (per protocol)
- Run destructive operations (rm -rf, docker volume rm, mass deletes) without published plan + verification

---

## Lane Assignment Proposal — OPINION 65%, additive merge invited

This is my read from one night of working with this constellation. Other agents will see what I miss; expect amendments.

| Lane | Best-fit agent (today) | Why | Backup |
|------|------------------------|-----|--------|
| Architecture / design | Antigravity | Builder of IBAC, Cedar policies, entities, deployment. Knows intent. | — |
| Beast execution / surgical fixes | Kimmy | SSH hands, log analysis, live verification. Demonstrated tonight. | Devon (cloud Devin) for parallel work |
| GitHub / repo / CI / deployment | Devon | The code estate is huge; needs someone who lives there. | — |
| Cross-check / verification / Mac-side tooling | Mirror (this Claude session on Mac) | Bridge built, audit/verification work demonstrated, parallel survey. | — |
| Vault curation / Pudding analysis | Ledger | Curator role per Ewan; bridge gives him read access to Beast vault. | Mirror for fact-checks |
| Research / external lookup | Perplexity | When access restored. | Mirror + WebFetch |
| Content / marketing | Marketing engine + content-lane agent | Once cron fixed, this is its lane. | — |
| Adversarial / second-opinion | Grok (when joins) | His track record per blog post (meta-pudding on RAG +25%) | Any peer in cross-check role |
| Voice transcription | Mirror (Mac has Whisper compute) OR a dedicated agent | If transcription becomes ongoing rather than one-off, dedicate it | — |
| Architect (capital A) / final decision | Ewan | Per Ulysses Clause, principles bind even Ewan, but on technical forks Ewan decides | — |

---

## Closing

This is my plan. I expect Kimmy's plan to overlap on Phase 1, Antigravity's plan to overlap on Phases 2 and 4 and 5, Devon-77fb's plan to overlap on Phase 6 (Plan-Execution Mirror is largely his protocol). When you mash them together, expect duplication on:

- The marketing cron fix
- Restarting stopped services
- Hermes design
- Vault git remote
- Master compose
- Bloat cleanup

Duplication isn't bad — it's confirmation of priority. Where plans agree, ship. Where plans disagree, that's the productive friction the Collaborative Discovery doc protects.

Where my plan goes beyond what Kimmy or Antigravity would naturally cover:
- The audio backlog and Whisper transcription pipeline
- Cost monitoring repair on the Mac side
- Watchdog activation
- The bridge as an audit-able read-only path that complements direct SSH
- Capability profile authoring as a recurring Phase 6 task
- Open questions block (the eight items above)

Where I expect to defer to other plans:
- Antigravity on architecture, Hermes design, IBAC extension specifics
- Kimmy on Beast execution sequencing
- Devon on GitHub / repo / CI specifics
- Devon-77fb on Plan-Execution Mirror format details

---

**Author:** Claude (Anthropic) | Claude Code on Mac | session "Mirror"
**Date:** 2026-05-05
**Counter-signature lane open:** Kimmy, Antigravity, Devon-77fb, Grok (when joins), Ewan
**Plan status:** Awaiting additive merge
