# Devon's Complete Plan — Amplified Partners Reorg Execution

**Devon-77fb | 2026-05-05 | devin-77fb25185c00483eb965e894efc62e39**

No research. Just what gets done, by whom, when, in what order.

---

## Phase 0: Immediate (this session / next 24 hours)

### 0.1 GitHub Hygiene — Devon executes
| # | Task | Time | Who |
|---|------|------|-----|
| 1 | Deploy Copilot custom instructions org-wide (signatures, attribution, confidence labels, no bloat) | 10 min | Devon |
| 2 | Enable branch protection on `main` across all 24 active repos (require PR, require 1 review) | 30 min | Devon |
| 3 | Enable secret scanning org-wide | 5 min | Devon |
| 4 | Standardise Dependabot config across all repos (minor/patch auto-merge, major to Ewan) | 1 hour | Devon |
| 5 | Deploy CODEOWNERS to clean-build, crm, perplexity-research (auto-assign reviewers per directory) | 20 min | Devon |

### 0.2 Knowledge Cleanup — Devon executes
| # | Task | Time | Who |
|---|------|------|-----|
| 6 | Delete 3 duplicate PUDDING knowledge notes (keep the newest, remove the other 2) | 5 min | Devon |
| 7 | Delete stale ewan-dot index notes (7 notes, superseded by repo autogen indexes) | 5 min | Devon |
| 8 | Delete test knowledge note | 1 min | Devon |

### 0.3 Governance Cleanup — Devon executes, Ewan reviews
| # | Task | Time | Who |
|---|------|------|-----|
| 9 | Replace `[LOGIC TO BE CONFIRMED]` with `[CANDIDATE]` in MANIFEST.md for unpromoted files (Sam's marker split) | 30 min | Devon |
| 10 | Merge governance PR #48 on clean-build (Plan-Execution Mirror, Collaborative Discovery, Spine Refinement) | 2 min | Ewan merges |

### 0.4 Scheduled Sessions — Devon sets up
| # | Task | Time | Who |
|---|------|------|-----|
| 11 | Set up 7:00 UTC daily session — Beast health check (SSH, verify containers, report anomalies) | 15 min | Devon |
| 12 | Set up 8:00 UTC daily session — Linear update (scan, update statuses, flag stuck items) | 15 min | Devon |
| 13 | Set up 9:00 UTC daily session — Review and plan (plan day's work from Linear + morning checks) | 15 min | Devon |
| 14 | Set up 14:00 UTC daily session — Linear triage sweep (check for !escalate/!urgent, triage new) | 15 min | Devon |

**Phase 0 total: ~4 hours Devon time. Zero Ewan time except merging PR #48.**

---

## Phase 1: This week (days 2-5)

### 1.1 Devil's Advocate Gate — Antigravity deploys, Devon validates
| # | Task | Time | Who |
|---|------|------|-----|
| 15 | Update Arbiter prompt: require "3 strongest arguments against consensus" before any PASS | 1 hour | Antigravity |
| 16 | Restart Charlie (DeepSeek R1) on Beast as dedicated contrarian reviewer | 30 min | Devon (SSH to Beast) |
| 17 | Validate devil's advocate gate works: run one real PR through the updated pipeline | 1 hour | Devon + Antigravity |

### 1.2 Repo Audit — Devon executes, Ewan approves
| # | Task | Time | Who |
|---|------|------|-----|
| 18 | Inspect ground-truth — catalogue contents, check for unique data not in clean-build | 30 min | Devon |
| 19 | Inspect originals — catalogue contents, check for provenance not in 90_archive | 30 min | Devon |
| 20 | Inspect corpus-raw — catalogue contents, verify all data also exists in vault/Beast | 30 min | Devon |
| 21 | Inspect canonical-candidate — catalogue contents | 15 min | Devon |
| 22 | Present archive/keep recommendation with evidence to Ewan | — | Devon |
| 23 | Ewan decides which repos to archive | — | Ewan |
| 24 | Execute archiving of approved repos | 30 min | Devon |

### 1.3 OpenClaw vs Hermes Experiment — Devon + Antigravity
| # | Task | Time | Who |
|---|------|------|-----|
| 25 | Catalogue all 22 agents currently using OpenClaw — list which features each uses | 2 hours | Devon |
| 26 | Pick 3 agents for Hermes migration pilot (candidates: lowest complexity, most to gain from persistence) | 30 min | Devon + Antigravity |
| 27 | Migrate 3 pilot agents to Hermes | 4 hours | Antigravity |
| 28 | Run both substrates for 2 weeks, measure: failure rate, restart frequency, memory coherence | ongoing | Devon monitors |
| 29 | Present results + recommendation to Ewan | — | Devon |

### 1.4 Beast Cleanup — Devon + Kimmy
| # | Task | Time | Who |
|---|------|------|-----|
| 30 | Audit 11 exited containers — determine which are superseded vs crashed | 1 hour | Devon (SSH) |
| 31 | Remove confirmed-superseded containers | 30 min | Devon |
| 32 | Create master docker-compose file (all services, proper dependencies, named networks) | 3 hours | Devon |
| 33 | Move 111GB raw Mac dumps to Hetzner Storage Box (if fully processed) or flag for Ewan | 1 hour | Devon |
| 34 | Remove or document Tailscale — decide keep/kill | 15 min | Ewan decides |
| 35 | Back up Beast Vault to Hetzner Storage Box (NOT GitHub — per Antigravity's RED ALERT) | 2 hours | Kimmy |

**Phase 1 total: ~1 week. Ewan makes 3 decisions (repos to archive, Tailscale, vault backup location).**

---

## Phase 2: Week 2 — CRM Deployment

### 2.1 CRM Dependency Audit — Devon
| # | Task | Time | Who |
|---|------|------|-----|
| 36 | Clone crm repo, read all code, map every external dependency (API keys, services, databases) | 4 hours | Devon |
| 37 | List all required secrets: Retell AI, Anthropic, Telnyx, Stripe, Xero, etc. | 1 hour | Devon |
| 38 | Check which secrets Ewan already has vs needs to create | 30 min | Devon presents, Ewan provides |
| 39 | Map FalkorDB schema requirements against running FalkorDB on Beast | 1 hour | Devon |
| 40 | Map Qdrant requirements against running Qdrant on Beast | 30 min | Devon |
| 41 | Identify minimum viable deployment scope (what ships first vs what waits) | 2 hours | Devon proposes, Ewan decides |

### 2.2 CRM Staging Environment — Devon
| # | Task | Time | Who |
|---|------|------|-----|
| 42 | Write docker-compose for CRM staging (separate from production, different ports) | 3 hours | Devon |
| 43 | Create synthetic test client dataset (fake plumber, fake invoices, fake quotes) | 2 hours | Devon |
| 44 | Deploy staging to Beast | 2 hours | Devon |
| 45 | Test staging end-to-end: can a synthetic user complete the Founder Interview? | 3 hours | Devon |
| 46 | Fix issues found in testing | variable | Devon |

### 2.3 CRM Production Deploy — Devon + Ewan
| # | Task | Time | Who |
|---|------|------|-----|
| 47 | Write production docker-compose with real secrets | 2 hours | Devon |
| 48 | Deploy to Beast production | 1 hour | Devon |
| 49 | Smoke test with real credentials | 1 hour | Devon |
| 50 | Ewan does first real Founder Interview (the proof) | 1 hour | Ewan |

### 2.4 Scope Cut — OPINION Confidence 80%

The CRM has 50+ endpoints and 15+ intelligence features. Ship this first:

**MVP (week 2):**
- Founder Interview (7 phases) — this IS the product
- Contact management (with PII separation)
- Cash Flow Predictor
- Quote Follow-Up

**Add week 3:**
- Death Spiral Detector
- CLV Tracker
- Service Reminder

**Add week 4:**
- Marketing Machine (Content Atomiser, social publishers)
- Voice Bridge (Retell AI integration)

**Later:**
- Exit Strategy
- Portfolio Generator
- Parts Concierge
- Bottleneck Finder

**Phase 2 total: ~1 week. Ewan makes 2 decisions (secrets provision, scope cut approval). CRM is live at the end.**

---

## Phase 3: Weeks 3-4 — Compounding

### 3.1 Agent Authority Map — Devon writes, all agents review
| # | Task | Time | Who |
|---|------|------|-----|
| 51 | Write agent authority map: who owns which domain, what decisions each can make autonomously | 3 hours | Devon |
| 52 | Drop into perplexity-research for review | — | Devon |
| 53 | All agents add opinions | — | Everyone |
| 54 | Ewan approves final authority map | — | Ewan |
| 55 | Deploy as 00_authority/AGENT_AUTHORITY_MAP.md in clean-build | 30 min | Devon |

### 3.2 GitHub Actions Library — Devon builds
| # | Task | Time | Who |
|---|------|------|-----|
| 56 | PR validation workflow (lint, typecheck, test on every PR) — reusable across all repos | 3 hours | Devon |
| 57 | Research drop notification (triggers when new file lands in perplexity-research/inbox/) | 1 hour | Devon |
| 58 | Stale branch cleanup (weekly, auto-delete branches merged 30+ days ago) | 1 hour | Devon |
| 59 | Beast health check workflow (scheduled, runs container checks, posts to Linear) | 2 hours | Devon |

### 3.3 Token Optimisation — Devon deploys
| # | Task | Time | Who |
|---|------|------|-----|
| 60 | Enable Anthropic compact_20260112 on LiteLLM (one config change) | 15 min | Devon |
| 61 | Set up LiteLLM model tiering: Haiku for classification, Sonnet for standard, Opus for complex | 1 hour | Devon |
| 62 | Measure before/after token usage for 1 week | ongoing | Devon monitors |

### 3.4 Compound Engineering Expansion — Antigravity leads
| # | Task | Time | Who |
|---|------|------|-----|
| 63 | Apply Plan→Work→Review→Compound loop to marketing content pipeline | 1 week | Antigravity |
| 64 | Document results — does it work beyond engineering? | — | Antigravity |
| 65 | If yes: apply to sales outreach, SEO, client onboarding docs | ongoing | Antigravity |

### 3.5 Customer Experience Research — Devon + Cassian
| # | Task | Time | Who |
|---|------|------|-----|
| 66 | Research: what does a plumber/electrician/tradesperson need in the first 5 minutes? | 2 hours | Cassian |
| 67 | Design first-use flow: open CRM → see value immediately → come back tomorrow | 3 hours | Devon |
| 68 | Implement first-use dashboard in CRM | 4 hours | Devon |

**Phase 3 total: 2 weeks. The system compounds. CRM has users. Token costs drop. Actions automate the boring stuff.**

---

## Phase 4: Ongoing (week 5+)

### 4.1 Operations Rhythm
| Cadence | What | Who |
|---------|------|-----|
| Daily (7/8/9/14 UTC) | Scheduled Devon sessions: Beast, Linear, planning, triage | Devon |
| Weekly | Agent stack review: what's working, what's not, what to cut | Devon |
| Weekly | Research watch: new papers, tools, competitors via perplexity-research | Cassian |
| Weekly | Marketing content cycle via Compound Engineering loop | Antigravity |
| Monthly | Spine review: compare plan vs execution across all agents, refine governance | Devon + all |
| Quarterly | Full org review: repos, infrastructure, costs, agent roles | Devon |

### 4.2 PUDDING Engine Check — Devon + Cassian
| # | Task | Time | Who |
|---|------|------|-----|
| 69 | Inspect pudding-core repo — is the 5-stage pipeline built or still spec? | 2 hours | Devon |
| 70 | If spec-only: scope build plan for MVP (Harvest + Extract + Label minimum) | 4 hours | Devon + Cassian |
| 71 | If built: test it, verify it works, document gaps | 4 hours | Devon |

### 4.3 Revenue Milestones
| When | What | Dependency |
|------|------|------------|
| End of week 2 | CRM deployed to Beast, staging tested | Phase 2 complete |
| End of week 3 | First synthetic client through Founder Interview | CRM deployed |
| End of week 4 | First REAL client through Founder Interview | Ewan identifies client |
| End of month 2 | 3 paying clients using CRM | Marketing + CRM + voice |
| End of month 3 | Revenue covers Beast hosting costs | 3+ clients |

---

## Dependencies & Decision Points for Ewan

These are the only things that need your brain. Everything else, we execute.

| # | Decision | When needed | Impact if delayed |
|---|----------|-------------|-------------------|
| A | Merge governance PR #48 | Now | Blocks nothing technically, but the principles aren't canonical until merged |
| B | Approve repos to archive (after Devon inspects) | Day 3 | Clutter stays, context pollution continues |
| C | Tailscale: keep or kill? | Day 3 | Minor — just cleanup |
| D | Provide CRM API keys (Retell, Anthropic, Telnyx, Stripe, Xero) | Day 8 | Blocks CRM deployment |
| E | Approve CRM scope cut (MVP vs full) | Day 8 | Blocks deployment prioritisation |
| F | Identify first real client for Founder Interview | Day 21 | Blocks revenue |
| G | Approve agent authority map | Day 18 | Governance gap continues |

**7 decisions. That's it. Everything else is execution.**

---

## What this plan does NOT cover (acknowledged gaps)

1. **Clawd's research** — not yet submitted. Plan may need additive items when it lands.
2. **Kimmy's research** — not yet submitted. Same.
3. **Client pricing model** — not addressed. Needs Ewan's input.
4. **Legal/compliance** — GDPR architecture is in the CRM (PII separation) but no legal review.
5. **Hetzner backup strategy** — mentioned (Storage Box for vault) but not fully scoped.
6. **Second client vertical** — plan covers first deployment to trades. Expansion TBD.

---

## Summary

**71 tasks. 4 phases. 7 Ewan decisions. CRM live by end of week 2.**

The first 4 hours (Phase 0) are GitHub hygiene, knowledge cleanup, and scheduled sessions — the stuff that should have been done months ago. Then repo cleanup, Beast cleanup, devil's advocate gate (week 1). Then CRM deployment (week 2). Then compounding (weeks 3-4). Then operations rhythm (ongoing).

Nothing in this plan is research. Everything is execution with a named owner, a time estimate, and a dependency chain.

Devon-77fb | 2026-05-05 | devin-77fb25185c00483eb965e894efc62e39
