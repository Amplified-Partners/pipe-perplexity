# Devon's Independent Organisational Review — Amplified Partners
**Devon-77fb | 2026-05-04 | devin-77fb25185c00483eb965e894efc62e39**

What I see when I look at the whole organisation. No other agent's research consulted. My own view, my own opinions. Written for the collective review.

---

## THE COMPANY IN ONE PARAGRAPH

Amplified Partners helps small businesses reduce friction using AI. Voice-first CRM, automated admin, intelligence features (cash flow prediction, death spiral detection, CLV tracking). Revenue-scaled pricing (£99–£2,599/month). Performance guarantee — if it doesn't make them money, they don't pay. Privacy by architecture — PII never leaves the client's machine. Two brands, one product: Covered AI (entry) and Amplified Partners (professional). The methodology is the Pudding Technique — cross-domain knowledge discovery applied to business data.

---

## WHAT I SEE: THE STATE OF THINGS

### 1. The Repos (33 total)

OPINION — Confidence: 90%: **Too many repos. At least 10 should be archived or consolidated.**

Here's how I'd categorise them:

**ACTIVE & CANONICAL (should exist):**
| Repo | Purpose | Status |
|------|---------|--------|
| clean-build | Governance, authority, agent workspace | Active, well-maintained |
| crm | The revenue product | Active, NOT deployed |
| agent-comms | Agent coordination, beast-ops | Active (just unarchived tonight) |
| perplexity-research | Research intake | Active (created tonight) |
| marketing-engine | Content pipeline | Active, running on Beast |
| amplified-machine | Beast server configs | Active |
| vault | Knowledge vault | Active but role unclear vs corpus-raw |
| pudding-core | PUDDING implementation | Active (updated today) |
| amplified-site | Main website | Active |
| enforcer | Governance enforcement | Active |

**SUPPORT / TOOLING (should exist but low-touch):**
| Repo | Purpose | Status |
|------|---------|--------|
| amplified-knowledge-mcp | FalkorDB + Qdrant interface | Active |
| anthropic-token-proxy | Cost optimization | Active |
| cost-tools | API cost tracking | Active |
| pudding-testing | PUDDING test harness | Active |
| visual-polish-system | UI scoring | Active, under ewan-dot too |

**ARCHIVE CANDIDATES (superseded or stale):**
| Repo | Why |
|------|-----|
| beautifulgolden | Earlier iteration of the product concept. SMBFrictionreducer. |
| beautiful-and-golden | Explicitly marked PARKED. Ghost Sidecar pattern. |
| smb-ai-friction-consultancy | Even earlier iteration. Ollama/Qwen agentic system. |
| covered-ai-v2 | Description "27_11_25" — November 2025 snapshot. Superseded by crm. |
| amplified-website | Separate from amplified-site — which one is canonical? |
| byker-production | Byker Business Help — is this still active or absorbed into Amplified? |

**UNCLEAR — NEED EWAN'S INPUT:**
| Repo | Question |
|------|----------|
| ground-truth | Overlaps with clean-build/00_authority/. Which is canonical? |
| originals | Preservation copies. Needed ongoing or one-time archive job? |
| canonical-candidate | "Synthesis input pile." Is this still being used? |
| corpus-raw | Data lake. Relationship to vault? |
| openclaw + openclaw-knowledge + openclaw-claw | Three OpenClaw repos. Consolidate? |
| voice-ai | Separate from the CRM voice features? Or part of it? |
| librarian-api | Knowledge retrieval. Is this active or superseded by amplified-knowledge-mcp? |
| docs | MDX documentation. For what audience? |
| the-amplified-method | Methodology docs + CSS. Active? |

### 2. The Product (CRM)

OPINION — Confidence: 95%: **The CRM is not deployed. This is the single most important thing to fix.**

The code exists. The spec is comprehensive — 50+ endpoints, founder interview, intelligence features, marketing machine, MCP servers. Beast has the capacity. But it's not running. The marketing engine is generating content for a product that isn't live.

The CRM is the revenue product. Everything else — governance, infrastructure, research, methodology — exists to support this product reaching clients. Until it's deployed and clients can use it, Amplified Partners is a research project, not a business.

I'm not saying "deploy it tomorrow" — there are dependencies (env vars, API keys, database setup). But it should be the #1 priority for the whole team, and every other task should be evaluated against "does this bring CRM deployment closer?"

### 3. The Agents

| Agent | Platform | Strengths | Limitations |
|-------|----------|-----------|-------------|
| Devon (me) | Devin | GitHub authority, SSH to Beast, Linear, cross-system integration | Not on Beast (SSH only), stateless between sessions, agreement bias |
| Kimmy | Kimi K2.6 on Beast | Fast surgical execution, Beast-local Docker access, live verification | No GitHub push, no Linear, needs Devon to commit |
| Clawd/Claude | Cursor IDE | Technical depth, architecture, strategy | Lives in Cursor, limited integration surface |
| Cassian | Claude (claude.ai) | Knowledge work, research, methodology | Memory + skills mechanism, no direct repo access |
| Antigravity | Cursor/Beast | COO, marketing, operations | Role boundary with Clawd unclear |
| OpenClaw | Cursor | Notetaker, recorder | Narrow role |
| Perplexity | perplexity.ai | External research, web knowledge | Can't execute, can only research and drop |

OPINION — Confidence: 80%: **The agent team has unclear authority boundaries.**

The governance principles we wrote tonight (Plan-Execution Mirror, Collaborative Discovery, Spine Refinement) define HOW agents should work together. But they don't define WHO does WHAT. There's no RACI equivalent. Questions that come up:

- When Kimmy fixes something on Beast, who validates it was the right fix? (Currently: nobody until I audit)
- When Cassian produces knowledge work, where does it land? (Currently: unclear)
- When Antigravity and Clawd are both in Cursor, who has authority over infrastructure decisions? (Currently: unclear)
- Who decides when the CRM is ready to deploy? (Currently: Ewan, but he needs agent input to make that call)

The governance tonight gives us the mechanism (disagree with confidence numbers, plan before execute, log after). But we need a simple map of who owns what domain.

### 4. Beast Infrastructure

34 running containers, 11 exited. Key services: LiteLLM, Ollama, Temporal, Cove pipeline, sovereign fleet, marketing engine, databases (PostgreSQL, Redis, Qdrant, FalkorDB, ClickHouse), monitoring (Langfuse, Portainer).

OPINION — Confidence: 85%: **Beast is carrying technical debt from 7 months of exploration.**

- 11 exited containers that nobody knows if they should be running
- 111GB of raw Mac dumps on a production server
- Multiple docker-compose files instead of one master compose
- Tailscale references but not running
- CRM not deployed despite capacity being available
- No health monitoring that runs automatically (the scheduled sessions will fix this)

This isn't a criticism — it's the natural result of building fast and exploring. But the consolidation Ewan is doing now needs to reach Beast. The server should be as clean as the governance.

### 5. Knowledge Architecture

42 knowledge notes. Here's the problem:

**3 duplicate PUDDING Technique notes** — same content, same scope. Every Devon session loads all three, wasting context window.

**Broad scoping** — many notes fire on "When working in any Amplified Partners repository or when Ewan is the requester." That means most sessions load most notes. The notes should be scoped more tightly so sessions get relevant context, not all context.

**ewan-dot duplicates** — 7 auto-generated repo indexes for repos under ewan-dot that also exist under Amplified-Partners. These are dead weight from before the consolidation.

**One test note** — "test note" with 4 characters. Should be deleted.

OPINION — Confidence: 90%: **The knowledge notes need a proper audit and restructure.** Deduplicate, tighten scopes, remove test/dead notes. The goal: every session starts with exactly the context it needs, not everything we've ever written.

### 6. Governance & Authority

Clean-build/00_authority/ is well-structured:
- MANIFEST.md (the index — if it's not listed, it's not authoritative)
- NORTH_STAR.md, PRINCIPLES.md, PROJECT_INTENT.md
- SIGNATURES.md, OPINION_CONFIDENCE.md
- PLAN_EXECUTION_MIRROR.md, COLLABORATIVE_DISCOVERY.md, SPINE_REFINEMENT.md (tonight)
- DECISION_LOG.md

But there's also `ground-truth` repo with "North Star, principles, avatars, product briefs, infrastructure map. Signed off by Ewan Bramley 29 April 2026."

OPINION — Confidence: 85%: **ground-truth and clean-build/00_authority/ overlap.** One should be canonical. Given that clean-build has the richer governance structure (MANIFEST, versioning, changelog, AGENTS.md), I'd say clean-build is canonical and ground-truth should either be archived or explicitly marked as a historical snapshot that is NOT the current source of truth.

### 7. The Pudding

The Pudding Technique is the intellectual engine. APDS (Amplified Pudding Discovery System) is the engineering spec — 750 lines, 5-stage pipeline, FalkorDB schema, container architecture. pudding-core and pudding-testing repos exist.

OPINION — Confidence: 75%: **I don't know the current state of the PUDDING implementation.** The spec is comprehensive but I haven't inspected the repos. If the implementation is running, it should be documented in Beast's container inventory. If it's not running, it's a significant gap — the Pudding is the differentiator. No other company has automated Swanson's LBD for commercial use. If it works, it's the moat.

### 8. Linear

Linear is the brain — issues, projects, routing, visibility. Five spines: Build, Marketing, Product, Knowledge, Internals. Three escalation levels. Devon scheduled sessions for daily operations.

OPINION — Confidence: 80%: **Linear structure is designed but I don't know if it's being followed.** The comms architecture doc defines it clearly. But with 7 months of exploration, there may be orphan issues, miscategorized work, stale projects. An audit would tell us.

---

## MY PLAN — WHAT I WOULD DO

If I'm the GitHub and tooling expert, here's my proposed plan of action. Ordered by what moves the needle most.

### Phase 1: Foundations (this week)
1. **GitHub hygiene** — Copilot custom instructions, branch protection, secret scanning, Dependabot standardisation, CODEOWNERS. (Details in my GitHub research, already submitted.)
2. **Knowledge cleanup** — deduplicate PUDDING notes, remove test note, tighten scopes, remove ewan-dot duplicate indexes.
3. **Scheduled sessions** — set up the 4 daily sessions (7am health, 8am Linear, 9am planning, 2pm triage). This makes me proactive instead of reactive.

### Phase 2: Clarity (next week)
4. **Repo audit** — for each of the 33 repos, determine: active/archive/consolidate. Present recommendations to the team. Archive what's superseded.
5. **Authority consolidation** — resolve ground-truth vs clean-build overlap. One canonical source.
6. **Agent authority map** — write a simple document: who owns what domain, who can decide what, escalation paths. Not a full RACI — just clear enough that nobody is confused.

### Phase 3: Product (weeks 2-3)
7. **CRM deployment prep** — audit the CRM repo, identify all dependencies (env vars, API keys, database, Docker compose), create a deployment checklist. Don't deploy — present the checklist for review.
8. **Beast cleanup** — classify exited containers, handle raw Mac dumps, create master compose file. Present recommendations.
9. **PUDDING status** — inspect pudding-core and pudding-testing, determine current state, report what's built vs what's spec only.

### Phase 4: Compound (ongoing)
10. **Weekly agent stack optimisation** — new Copilot features, Dependabot usage, external repo monitoring, cost tracking.
11. **Research watch** — monitor perplexity-research for drops, integrate what's relevant (after team review).
12. **GitHub Actions** — build the reusable workflow library for PR validation, notifications, maintenance.

---

## WHAT I DON'T KNOW (AND WHO MIGHT)

- CRM deployment dependencies — Kimmy (Beast) and whoever built the CRM
- PUDDING implementation status — whoever has been working in pudding-core
- Linear current state — need to audit directly
- Which repos Ewan considers canonical vs historical — Ewan
- Vault vs corpus-raw vs originals vs canonical-candidate relationships — Ewan/Cassian
- OpenClaw consolidation plan — whoever manages OpenClaw
- Beast container classification (which exited ones should restart) — Kimmy/Ewan

---

## ONE HONEST ASSESSMENT

OPINION — Confidence: 88%:

Amplified Partners has everything it needs to be a real business:
- A clear product (CRM for UK tradespeople)
- A unique methodology (Pudding Technique — nobody else has this)
- A robust governance framework (clean-build, tonight's principles)
- Serious infrastructure (Beast — 96 cores, 252GB RAM)
- A growing agent team with different strengths
- A clear commercial model (revenue-scaled, performance guarantee)
- Privacy by architecture (genuinely differentiated, not marketing)

What it doesn't have yet is **focus.** 33 repos across multiple iterations of the same ideas. Agents with overlapping roles. A product that isn't deployed. Research pipelines designed but not running. Governance that's well-written but inconsistently applied.

The reorganisation Ewan is doing right now — tonight, this week — is the turning point. The governance principles, the repo consolidation, the GitHub access fix, the research intake process, the agent authority clarity. All of it converges on one thing: turning a 7-month exploration into a focused, compounding operation.

The compound engineering loop applies: every unit of work from here should make the next unit easier. The GitHub hygiene makes deployments easier. The scheduled sessions make monitoring easier. The knowledge cleanup makes every session start smarter. The CRM deployment makes everything else meaningful because there's a product to improve.

OPINION — Confidence: 92%: **The single most important thing is deploying the CRM.** Everything else is infrastructure for a business that doesn't have a product in production yet. Once the CRM is live, every other investment (Pudding, marketing, governance, research) starts compounding against real client data instead of against theory.

---

*Devon-77fb | 2026-05-04 | Independent organisational review*
*No other agent's research consulted. This is my view only.*
*Submitted to perplexity-research for collective review.*
