# Hermes Agent — Deep Capabilities Research
**Date:** 2026-05-05  
**Author:** Cassian-research-subagent  
**Sources:** Hermes official documentation, NousResearch GitHub, community reports

---

## 1. Sub-Agent Delegation Mechanics

### How Spawning Works

Hermes exposes a `delegate_task` tool that spawns child `AIAgent` instances with isolated context, restricted toolsets, and their own terminal sessions. The mechanics are documented in full at the [Hermes delegation guide](https://hermes-agent.nousresearch.com/docs/guides/delegation-patterns):

> "Each subagent gets its own conversation, terminal session, and toolset. Only the final summary comes back — intermediate tool calls never enter your context window."

> "Subagents start with a completely fresh conversation. They have zero knowledge of the parent's conversation history, prior tool calls, or anything discussed before delegation."

The parent must pass everything the subagent needs via two fields: `goal` (required) and `context` (required). The subagent receives a focused system prompt built from those fields, completing the task and returning a structured summary (what it did, findings, files modified, issues encountered).

### Parallel Execution

Batches of up to 3 concurrent subagents by default (configurable via `delegation.max_concurrent_children`; floor of 1, no hard ceiling). From the [configuration docs](https://hermes-agent.nousresearch.com/docs/user-guide/configuration):

```yaml
delegation:
  max_concurrent_children: 3   # Parallel children per batch
  max_spawn_depth: 1           # Tree depth (1–3, default 1 = flat)
  orchestrator_enabled: true
  child_timeout_seconds: 600
  model: "google/gemini-flash-2.0"   # Cheaper model for subagents
  provider: "openrouter"
```

With `max_spawn_depth: 3` and `max_concurrent_children: 3`, the tree can theoretically reach 27 concurrent leaf agents. In practice, that multiplies cost accordingly.

### Permission Inheritance ("Bubble" Mode)

The term "bubble" appears in the MAESTRO/Ken Huang permission taxonomy rather than in the Hermes delegation docs directly. From [Ken Huang's Chapter 4 on permission systems](https://kenhuangus.substack.com/p/chapter-4-permission-systems-and):

> "`bubble` — Subagent mode — inherit parent's permission context. `bubble` ensures subagents cannot exceed the permissions of their parent — a critical safety property in multi-agent systems."

In Hermes itself, the equivalent enforcement is toolset restriction. Leaf subagents (the default `role`) cannot call `delegate_task`, `clarify`, `memory`, `send_message`, or `execute_code` regardless of what the parent passes. Orchestrator subagents (`role="orchestrator"`) retain `delegate_task` but remain blocked from those other four. From [the delegation feature page](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation):

> "Leaf subagents (default) cannot call `delegate_task`, `clarify`, `memory`, `send_message`, or `execute_code`. Orchestrator subagents (`role='orchestrator'`) retain `delegate_task` for further delegation, but only when `delegation.max_spawn_depth` is raised above the default of 1."

Subagents also inherit the parent's API key, provider configuration, and credential pool — enabling key rotation on rate limits.

### State Return

Only the final summary enters the parent's context. The docs warn explicitly: "`delegate_task` is synchronous: if the parent turn is interrupted, active children are cancelled and their work is discarded." This is the most important production gotcha — delegation is **not** a durable background queue. Interrupted children return `status="interrupted"` but that result often never makes it into a user-visible reply.

---

## 2. Terminal Backends

The docs list seven backends as of the current release — the original six plus Vercel Sandbox. From the [configuration reference](https://hermes-agent.nousresearch.com/docs/user-guide/configuration):

| Backend | Where commands run | Isolation | Best for |
|---|---|---|---|
| `local` | Your machine directly | None | Development, personal use |
| `docker` | Docker container | Full (namespaces, cap-drop) | Safe sandboxing, CI/CD |
| `ssh` | Remote server via SSH | Network boundary | Remote dev, powerful hardware |
| `modal` | Modal cloud sandbox | Full (cloud VM) | Ephemeral cloud compute, evals |
| `daytona` | Daytona workspace | Full (cloud container) | Managed cloud dev environments |
| `vercel_sandbox` | Vercel Sandbox cloud microVM | Full (cloud microVM) | Cloud execution with snapshot-backed filesystem |
| `singularity` | Singularity/Apptainer container | Namespaces (`--containall`) | HPC clusters, shared machines |

**Docker security hardening specifics** (not in marketing copy): `--cap-drop ALL` with only `DAC_OVERRIDE`, `CHOWN`, `FOWNER` added back; `--security-opt no-new-privileges`; `--pids-limit 256`; size-limited tmpfs (`/tmp` 512MB, `/var/tmp` 256MB, `/run` 64MB). Podman is supported via `HERMES_DOCKER_BINARY=podman`.

**SSH backend detail:** Uses ControlMaster for connection reuse (5-minute idle keepalive). Persistent shell is **on by default** for SSH — a single long-lived `bash -l` process keeps cwd, exported env vars, and shell variables alive across commands. For SSH+Modal+Daytona backends, Hermes tracks files touched in the remote sandbox and syncs modified files back to `~/.hermes/cache/remote-syncs/<session-id>/` on session teardown. File sync respects `file_sync_max_mb: 100` (default).

**For a Hetzner Beast deployment:** The SSH backend is the natural fit. Required vars: `TERMINAL_SSH_HOST` and `TERMINAL_SSH_USER`. The persistent shell eliminates per-command connection overhead. The Beast machine handles compute; Hermes runs on any client. Alternatively, Docker on the Beast gives full isolation with write-access to mounted project directories.

---

## 3. Skills Hub Mechanics

Skills are on-demand knowledge documents following the [agentskills.io](https://agentskills.io/home) open standard. Progressive disclosure means: at startup, only name+description loads (Level 0); when a task matches, the full `SKILL.md` loads (Level 1); referenced files load only when the skill body requests them (Level 2). This keeps dozens of skills in play without ballooning the context window.

From the [skills system docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills):

### Distribution Sources

| Source | Example | Trust Level |
|---|---|---|
| `official` | `official/security/1password` | Builtin — no third-party warning |
| `skills-sh` | `skills-sh/vercel-labs/json-render/...` | Trusted (Vercel's public directory) |
| `well-known` | URL to `/.well-known/skills/index.json` | Community |
| `github` | `openai/skills/k8s` | Trusted if in default taps; Community otherwise |
| `clawhub` | clawhub.ai identifiers | Community |
| `claude-marketplace` | `anthropics/skills` | Trusted |
| `lobehub` | chat-agents.lobehub.com catalog | Community |
| `url` | Direct HTTPS URL to single `SKILL.md` | Community |

Default GitHub taps: `openai/skills`, `anthropics/skills`, `VoltAgent/awesome-agent-skills`, `garrytan/gstack`.

### Trust Enforcement

From the [Ken Huang skill system analysis](https://kenhuangus.substack.com/p/chapter-12-the-skill-system-pattern):

```python
# hermes-agent/tools/skills_hub.py
TRUSTED_REPOS = {"openai/skills", "anthropics/skills"}
def trust_level_for(self, identifier: str) -> str:
    repo = "/".join(identifier.split("/", 2)[:2])
    return "trusted" if repo in TRUSTED_REPOS else "community"
```

All hub-installed skills go through a security scanner (data exfiltration, prompt injection, destructive commands, supply-chain signals). The lock file at `~/.hermes/skills/.hub/lock.json` stores SHA-256 content hashes — tamper detection on subsequent loads. Quarantined skills go to `~/.hermes/skills/.hub/quarantine/`.

### Self-Creation (The Actual Self-Improvement Mechanism)

The agent uses a `skill_manage` tool to create, patch, edit, and delete skills from completed work. This triggers after complex tasks (5+ tool calls), errors/dead-ends, user corrections, and non-trivial workflows. The `patch` action is preferred over `edit` for token efficiency. This is the core of what "self-improving" means at runtime — not weight tuning, but accumulating reusable Markdown playbooks.

---

## 4. The Self-Improving Learning Loop

This is where marketing meets (and sometimes diverges from) engineering. From [AgentConn's review](https://agentconn.com/blog/nousresearch-hermes-agent-self-improving-framework-review/):

> "After each completed task, the agent automatically writes a reusable Markdown Skill file into SQLite. Successful approaches become skills that persist across sessions. If a better approach consistently outperforms the stored one, the skill is revised."

There are two distinct layers:

**Layer 1 — Runtime skill accumulation (in the core repo):** The agent writes/patches SKILL.md files in `~/.hermes/skills/` during normal operation. No ML. No weight updates. Pattern extraction from completed work, written as instructions.

**Layer 2 — GEPA evolutionary optimization (companion repo):** The [`hermes-agent-self-evolution`](https://github.com/NousResearch/hermes-agent-self-evolution) repo (ICLR 2026 Oral, MIT licensed) runs DSPy + GEPA. From AgentConn's review:

> "GEPA reads execution traces to understand *why* things fail — not just that they failed — then proposes targeted prompt and skill improvements using DSPy. This is meaningfully different from a simple retry loop. A task that took 47 tool calls might have completed in 12 with a better skill — GEPA identifies that gap and updates the skill accordingly."

No weight tuning occurs. The self-evolution layer is prompt-evolution and skill-content evolution — the model weights stay fixed. This is an external optimization pipeline, not something that runs automatically inside the core agent. **[SOURCE REQUIRED for the exact trigger mechanism: is GEPA invoked per-session, periodically, or manually?]** The GitHub repo itself did not return full content during this research.

**Layer 3 — Honcho dialectic (optional add-on, server-side):** Three-pass reasoning (Initial Assessment → Self-Audit → Reconciliation) over conversation history. Deepens the user model, not the skills. Not RL.

---

## 5. "Deepening Model of Who You Are Across Sessions"

This is a real feature with a specific architecture — not marketing copy — but the depth depends heavily on which memory backend is active.

### Baseline (no Honcho): MEMORY.md + USER.md

From the [memory documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory):

> "MEMORY.md — 2,200 chars (~800 tokens): environment facts, project conventions, tool quirks, completed task diary. USER.md — 1,375 chars (~500 tokens): name, role, timezone, communication preferences, pet peeves, workflow habits, technical skill level."

Both are injected once at session start as a frozen snapshot. Mid-session writes persist to disk but don't appear in the prompt until next session (preserves LLM prefix cache). The agent manages entries via add/replace/remove operations with substring matching. This is functional but limited — 8-15 MEMORY entries, 5-10 USER entries, manually curated by the agent itself.

### With Honcho: Server-Side Deep Modeling

From [Honcho's integration guide](https://docs.honcho.dev/v3/guides/integrations/hermes):

> "Honcho acts as a long-term memory and user-model layer alongside Hermes' built-in memory files. It gives Hermes three capabilities: prompt-time context injection, cross-session continuity, and durable writeback."

What Honcho actually persists (from [Hermes Honcho docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/honcho)):

- **Session summaries** injected at turn 1 (prewarm fires in background at session init)
- **User representation**: preferences, goals, communication style derived from messages
- **AI peer card**: what this specific Hermes profile knows and how it frames itself
- **Conclusions**: server-side derived insights, semantically searchable
- **Session strategy**: `per-directory` (default), `per-repo`, `per-session`, or `global`

The dialectic is three sequential LLM passes with explicit roles — it is not a vague "reasoning over history" but a structured self-critique. Depth is configurable (`dialecticDepth: 1–3`). Early passes bail if the prior pass returned strong signal.

Multi-profile peer isolation means a coding assistant and a personal assistant Hermes profile each build separate representations of the same user, with configurable cross-observation. **This is the "deepening model" claim substantiated** — it's a real vector database of user-derived conclusions, not just a text file.

---

## 6. Multi-Agent Fleet Coordination

### The Kanban Architecture (Hermes's Answer to Fleet Management)

From the [Kanban reference docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban):

> "Hermes Kanban is a durable task board, shared across all your Hermes profiles, that lets multiple named agents collaborate on work without fragile in-process subagent swarms. Every task is a row in `~/.hermes/kanban.db`; every handoff is a row anyone can read and write; every worker is a full OS process with its own identity."

This is architecturally different from `delegate_task`: Kanban workers are persistent OS processes with their own memory, not ephemeral subagents that die with the parent turn.

**Single-host by design.** The docs state explicitly: "no multi-host shared board support; use independent boards per host + `delegate_task`/message queue to bridge."

**Dispatcher behavior:** One dispatcher sweeps all boards per 60s tick. Reclaims stale claims (worker PID gone but TTL not expired). Auto-blocks after ~5 consecutive spawn failures ("circuit breaker").

**Specialist worker pattern** (from [GitHub issue #19931](https://github.com/NousResearch/hermes-agent/issues/19931)):

> "Hermes should remain the top-level orchestrator. Specialist tools should not become parallel orchestrators with their own task lifecycle, status system, or shadow planning board. The desired hierarchy is: Hermes Kanban = canonical task lifecycle and logs. Specialist worker = implementation executor for one assigned card."

This issue explicitly describes how to integrate Claude Code, Codex CLI, OpenCode as specialist workers *under* Hermes Kanban orchestration — a pattern being formalized as of May 2026.

### Profiles for Fleet Isolation

From the [profiles docs](https://hermes-agent.nousresearch.com/docs/user-guide/profiles):

> "Run multiple independent Hermes agents on the same machine — each with its own config, API keys, memory, sessions, skills, and gateway state."

Each profile is a separate `HERMES_HOME` directory. `hermes update` syncs bundled skills to all profiles automatically. Each profile can run its own systemd/launchd service (`hermes-gateway-<profile>`). Token locks prevent two profiles from using the same bot token.

**What Nous has shipped beyond Hermes for multi-instance:** `NousResearch/hermes-paperclip-adapter` — runs Hermes as a managed employee inside a Paperclip company. Also `NousResearch/NemoClaw` — runs OpenClaw more securely inside NVIDIA OpenShell with managed inference. No dedicated multi-Hermes fleet orchestrator has shipped as a separate product.

---

## 7. Integration Patterns

### LiteLLM

From the [AI providers docs](https://hermes-agent.nousresearch.com/docs/integrations/providers):

> "LiteLLM Proxy: Unifies 100+ LLM providers, load balancing, fallback chains, budget controls. Setup: `litellm --model anthropic/claude-sonnet-4 --port 4000`. Hermes config: `hermes model` → Custom endpoint → `http://localhost:4000/v1`."

LiteLLM exposes an OpenAI-compatible `/v1/chat/completions` endpoint, which is all Hermes needs. This is a one-line integration. LiteLLM also enables routing strategies (`latency-based-routing`, `price`, `throughput`).

### Anthropic/Claude as the Underlying Model

Three auth modes:
1. **Claude Max OAuth** (`hermes model` → Anthropic OAuth) — requires Claude Max + purchased extra usage credits; base Max allowance not consumed
2. **API key** (`ANTHROPIC_API_KEY`) — pay-per-token, works with Claude Pro
3. **Auto-detect Claude Code credentials** — if Claude Code is installed, Hermes reads its credential files directly

The docs note that Hermes auto-detects Claude Code credential files, meaning a machine already running Claude Code can route Hermes through the same Anthropic account without additional configuration.

For subagent cost management, the delegation system supports routing subagents to a different, cheaper model:

```yaml
delegation:
  model: "google/gemini-flash-2.0"  # Cheaper model for subagents
  provider: "openrouter"
```

### FalkorDB / Qdrant / Temporal

**[SOURCE REQUIRED]** — No official Hermes documentation for FalkorDB, Qdrant, or Temporal integrations was found. FalkorDB is documented as a GraphRAG backend for LangChain/LlamaIndex-based agents but not for Hermes directly. The correct integration path would be via MCP server (if FalkorDB/Qdrant expose MCP endpoints) or via skills with shell tool access.

### OpenRouter Provider Routing

A non-obvious production feature from the [providers docs](https://hermes-agent.nousresearch.com/docs/integrations/providers):

```yaml
provider_routing:
  sort: "throughput"    # "price" (default), "throughput", "latency"
  data_collection: "deny"   # Privacy: prevent provider-side data retention
```

The `data_collection: "deny"` flag is the privacy-relevant control for Five Rods compliance — it instructs OpenRouter to route only to providers that do not retain data.

### Fallback Configuration

```yaml
fallback_model:
  provider: openrouter
  model: anthropic/claude-sonnet-4
```

Auto-switches on rate limits, server errors, or auth failures (once per session). Credential rotation is also built in: the delegation credential pool enables key rotation on rate limits.

---

## 8. Coexistence vs Migration Patterns

### Migration Tool

From the [migrate-from-openclaw docs](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw):

`hermes claw migrate` imports persona (SOUL.md), long-term memory (MEMORY.md, USER.md), skills (4 sources), model/provider config, agent behavior, session reset policies, MCP servers, TTS, and messaging platform tokens.

**What breaks or requires manual work:**
- **WhatsApp** always requires re-pairing (Baileys QR, no token migration)
- **Cron jobs** are archived, not migrated — must be recreated with `hermes cron create`
- **Multi-agent list** (OpenClaw's agents-list.json) archived — use Hermes profiles instead
- **Channel bindings** archived — manual platform re-setup
- **Hooks/webhooks** archived — use `hermes webhook` or gateway hooks

### Coexistence Pattern (Community-Documented)

From the [Alibaba Cloud unified deployment analysis](https://www.alibabacloud.com/blog/hiclaw-unified-deployment-for-openclaw-and-hermes-workflows_603057):

> "Under the development trend of multi-Agent collaboration, there is no alternative relationship between OpenClaw and Hermes, but a coexistence and complementary relationship. Concrete implementation: (1) MCP Protocol Bridging — the lightest way to integrate. (2) Shared Skills Standard — cross-platform skills sharing with agentskills.io. (3) Tiered deployment: OpenClaw resident + Hermes on-demand invocation."

Community reports of running them together include: `"I asked openclaw agent to Install hermes agent"` and `"I have openclaw install Hermes sidecar inside its same instance"` — suggesting a common pattern of OpenClaw as the outer shell, Hermes spawned for specific workstreams.

From a [YouTube walkthrough](https://www.youtube.com/watch?v=mduLV-mWrNM) (April 2026):

> "Henry, my openclaw powered by Opus 46 is going to go and build this plan that we are then going to hand to Hermes. Henry is going to basically make sure Hermes is [doing it correctly]. I have Hermes go in and every two hours just look into [the scanners] on cron jobs."

The supervisor pattern (OpenClaw plans at high-reasoning; Hermes executes on cron/gateway) is documented empirically. The alternative (Hermes Kanban as orchestrator, OpenClaw/Claude Code as specialist workers) is being formalized in [issue #19931](https://github.com/NousResearch/hermes-agent/issues/19931).

---

## 9. Non-Obvious Capabilities

### AGENTS.md vs SOUL.md (Often Confused)

From the [SOUL.md guide](https://hermes-agent.nousresearch.com/docs/guides/use-soul-with-hermes):

> "Do not use SOUL.md for: repo-specific coding conventions, file paths, commands, service ports, architecture notes, project workflow instructions. Those belong in `AGENTS.md`. A good rule: if it should apply everywhere, put it in `SOUL.md`; if it only belongs to one project, put it in `AGENTS.md`."

SOUL.md occupies slot #1 in the system prompt — it completely replaces the default identity text. AGENTS.md is a per-workspace file, not persisted to `HERMES_HOME`. This distinction is documented but commonly missed.

### Toolset Disabling for Token Efficiency and Privacy

From the [DEV community deep dive](https://dev.to/truongpx396/hermes-agent-deep-dive-build-your-own-guide-1pcc):

> "Users enable/disable by toolset rather than tool-by-tool. Disabled toolsets are completely absent from the system prompt — saves tokens and prevents the model from even knowing about them."

This is more aggressive than most agent frameworks, which disable tool *calls* but still expose tool *descriptions*. Hermes removes the schema entirely.

### Skill Frontmatter Visibility Gates

Also from the DEV deep dive:

> "Frontmatter fields gate visibility: `platforms: [linux]` — hidden on macOS. `fallback_for_toolsets: [web]` — only visible if no premium web tool is enabled. `requires_toolsets: [shell]` — hidden if shell tool disabled."

This enables context-adaptive skill indices — a DuckDuckGo skill auto-appears only when Brave Search isn't configured.

### Critical Security Issue: `HERMES_REDACT_SECRETS` Off by Default

From [GitHub issue #19897](https://github.com/NousResearch/hermes-agent/issues/19897) (filed May 4, 2026, P0):

> "In a vanilla Hermes deployment, `HERMES_REDACT_SECRETS` is OFF by default. As a result, when an end user converses with the agent through the gateway (Telegram, Discord), Hermes routinely echoes back live API key values as part of its visible chat responses. Production Hermes Agent v0.11.0 on a Hostinger KVM2 VPS: 24 distinct env-defined credentials were found leaked, 345 files in sessions/ and logs/ contained at least one credential value."

The fix is `HERMES_REDACT_SECRETS=true` in `.env`. This is not on by default as of v0.11.0. Anyone deploying to a gateway must set this explicitly.

### Token-Lock Safety on Gateway Multi-Profile

Each messaging platform token can only be claimed by one profile. If a second profile attempts to start a gateway with the same bot token, it fails with an explicit error naming the conflicting profile. This prevents silent split-brain on restarts.

### `hermes doctor` Command

Not prominently documented but verifies all backend dependencies (Docker, Modal tokens, SSH connectivity, Singularity binaries) with clear error messages and suggested fixes.

### `execute_code` vs `delegate_task` Positioning

From the [delegation patterns guide](https://hermes-agent.nousresearch.com/docs/guides/delegation-patterns):

> "Use `execute_code` for mechanical data gathering (no reasoning needed). Delegate the reasoning-heavy analysis. `execute_code` handles the 10+ sequential tool calls cheaply, then a subagent does the single expensive reasoning task with a clean context."

This split is documented in example code (the "Gather Then Analyze" pattern) but not in the feature overview pages. It's the primary cost-control pattern for research workloads.

### Named Custom Providers for Internal GPU Servers

```yaml
custom_providers:
  - name: local
    base_url: http://localhost:8080/v1
  - name: work
    base_url: https://gpu-server.internal.corp/v1
    key_env: CORP_API_KEY
```

Switch mid-session: `/model custom:work:qwen-2.5`. This enables hot-switching between internal inference and cloud fallback without restarting the session.

---

## Production Reports (Last 30–60 Days)

From the GitHub issue tracker (NousResearch/hermes-agent, issues as of May 2026):

- **P0 startup crash** ([#19903](https://github.com/NousResearch/hermes-agent/issues/19903)): `CLI crash on startup: Invalid key 'c-S-c'` — prompt_toolkit doesn't support Shift modifier. Closed quickly but hit many users on fresh installs.
- **P0 security** ([#19897](https://github.com/NousResearch/hermes-agent/issues/19897)): `HERMES_REDACT_SECRETS` off by default — real-world credential exposure. Filed from a production VPS after 24-credential remediation.
- **P2 subagent routing bug** ([#19567](https://github.com/NousResearch/hermes-agent/issues/19567), closed): `TUI delegation subagent incorrectly routed to copilot-acp instead of configured deepseek provider` — subagents can inherit wrong provider in TUI mode.
- **P2 gateway drain hang** ([#19937](https://github.com/NousResearch/hermes-agent/issues/19937)): WSL + Feishu/Weixin — 90s `systemctl stop` traceback from wedged websockets.
- **Feature request** ([#19931](https://github.com/NousResearch/hermes-agent/issues/19931)): Specialist worker lanes under Kanban — formalization of Hermes-as-orchestrator with Claude Code/Codex as workers.
- **Feature request** ([#19563](https://github.com/NousResearch/hermes-agent/issues/19563)): Persistent background tasks with web UI control and cross-session resumption — confirming that the current `delegate_task` synchronous model is a known gap for durable work.

The release velocity is high (95,600 stars in seven weeks per [Digital Applied](https://www.digitalapplied.com/blog/hermes-agent-v0-10-self-improving-open-source-guide)), which means the issue tracker is active and bugs surface quickly.

---

## OPINION SECTION — Amplified Partners Context

*All claims in this section are opinion. Confidence percentages indicate the research basis for each claim.*

### The Decision Frame

Amplified Partners (32 repos, Hetzner Beast, multi-agent fleet, step-away goal, privacy-first, Five Rods compliant, deterministic-first 90/10) faces a different question than most Hermes evaluators. The relevant axis is not "is Hermes good" but "which Hermes capabilities are load-bearing for this specific stack."

---

### VALUABLE TO DEPLOY

**1. SSH terminal backend pointed at the Beast. [Confidence: 95%]**
This is the correct architecture. Hermes runs anywhere (laptop, VPS, cloud), executes on the Beast via SSH, and syncs modified files back automatically. Persistent shell eliminates per-command connection overhead. No Docker complexity needed on the Beast side. The Beast's full CPU/GPU/RAM is available to every Hermes profile without containerization overhead.

**2. Gateway for WhatsApp + multi-channel client comms. [Confidence: 92%]**
This is documented, production-tested, and the use case Hermes was purpose-built for. The 15-platform gateway is real. For Amplified Partners, a single Hermes gateway profile per client channel type is the clean pattern. The token-lock safety prevents split-brain on restarts, which matters for unattended deployment. Set `HERMES_REDACT_SECRETS=true` before any gateway deployment — this is non-negotiable given the P0 security issue above.

**3. Kanban + profiles as the multi-agent fleet architecture. [Confidence: 88%]**
The Kanban SQLite board is the correct primitive for Amplified's step-away goal. Multiple named profiles (researcher, ops, comms, review) each run as full OS processes with separate memory and skills. The dispatcher handles task promotion and crash recovery automatically. For 32 repos, one Kanban board per active project with a shared `default` board for cross-project tasks is the reasonable structure. The single-host constraint (no native multi-host coordination) is the binding limitation — Amplified would need to bridge boards across machines manually if the fleet spans multiple hosts.

**4. SOUL.md + MEMORY.md per profile for role purity. [Confidence: 90%]**
Each specialist profile (researcher, ops, comms) should have its own SOUL.md defining the role boundary. The KANBAN_GUIDANCE vs SOUL.md conflict ([issue #19351](https://github.com/NousResearch/hermes-agent/issues/19351)) was closed — role-purity enforcement now works. This is the deterministic-first pattern: fixed identity, fixed toolsets, fixed role scope.

**5. LiteLLM as the provider router for cost control and privacy. [Confidence: 85%]**
LiteLLM integrates in one line. For Five Rods compliance, the combination of LiteLLM (to route away from non-compliant providers) and OpenRouter's `data_collection: "deny"` flag gives two layers of data residency control. Routing subagents to a cheaper model (`delegation.model`) via LiteLLM is the cost-control pattern for parallel research workloads.

**6. `delegate_task` for parallel research workstreams (with caveats). [Confidence: 80%]**
The 3-concurrent subagent default with toolset restriction (`["web"]` only for research subagents) is the correct pattern for Amplified's research use case. The synchronous blocking behavior is the key caveat: if a parent turn is interrupted (new message arrives, `/stop`), all children die. For research that must survive interruption, use Kanban tasks instead of `delegate_task`.

---

### INTERESTING BUT BLOAT (for Amplified Partners specifically)

**1. Honcho dialectic memory. [Confidence: 75%]**
Honcho adds server-side user modeling via API calls. For Amplified's privacy-first constraint, sending conversation data to a third-party server (honcho.dev) is likely non-compliant with Five Rods. The baseline MEMORY.md + USER.md + session search (`FTS5 over local SQLite`) achieves adequate cross-session persistence without external data egress. Honcho's value is real for consumer-facing agents. For a privacy-first operator context, it's excluded by policy.

**2. GEPA self-evolution (hermes-agent-self-evolution). [Confidence: 70%]**
The evolutionary optimizer is a research companion repo, not the core product. It requires DSPy, execution trace collection, and an optimization loop that runs out-of-band. For a deterministic-first (90/10) deployment, GEPA introduces variance at the skill level — skills may evolve in ways that change behavior unpredictably. The runtime skill accumulation (agent writes SKILL.md from completed work) is the right level of self-improvement for this context: structured, inspectable, version-controlled.

**3. LobeHub / Claude-marketplace skill sources. [Confidence: 80%]**
Community trust level with opaque provenance. For Amplified's stack, skills should come from `official/` or verified GitHub sources the team controls. The hash-based tamper detection is a genuine safeguard, but the attack surface of community skills is non-trivial given the security scanner is not immune to sophisticated prompt injection.

**4. Vercel Sandbox and Daytona backends. [Confidence: 85%]**
Both are cloud-managed containers with data egress to third-party providers. Incompatible with privacy-first deployment. The Beast SSH backend supersedes both.

**5. Modal backend. [Confidence: 90%]**
Same reasoning as Vercel/Daytona — cloud VM with third-party data egress. Not applicable.

---

### The OpenClaw-vs-Hermes Framing (Opinion)

*[Confidence: 72%]* The coexistence pattern (OpenClaw plans, Hermes executes) is community-validated and empirically documented for the supervisor+worker pattern. The migration path (`hermes claw migrate`) is real and handles the major surface area. The pending question (Ewan's call) likely hinges on whether the deterministic-first preference favors OpenClaw's more explicit tool approval model vs Hermes's approvals modes (`auto`, `plan`, `smart`, `manual`). Hermes's `plan` mode (user approves high-level plan before any tools fire) is the closest to OpenClaw's model for high-stakes operations. For a 32-repo, step-away deployment, the Kanban pattern with `plan` mode on orchestrator profiles and `auto` mode on worker profiles is the defensible hybrid.

---

*Cassian-research-subagent*  
*2026-05-05*
