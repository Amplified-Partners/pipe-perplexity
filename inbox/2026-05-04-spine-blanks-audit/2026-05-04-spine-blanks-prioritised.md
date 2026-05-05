# Spine blanks — prioritised research backlog

**Repo:** `Amplified-Partners/clean-build` (commit at clone time, scope: active dirs only — `90_archive/` excluded)
**Generated:** 2026-05-05 ~01:30 BST by Sam-Comp
**Method:** Whole-repo `grep` for `[SOURCE REQUIRED] | [DECISION REQUIRED] | [LOGIC TO BE CONFIRMED]`, filtered to remove vocabulary/definition lines, then categorised by theme.

---

## Bias-bound markers on this document

- `[FACT]` — pulled directly from a file in the repo, line cited.
- `[CLAIM]` — Sam's reading of what the marker is asking for.
- `[OPINION confidence X%]` — Sam's prioritisation judgement.
- `[ASSUMED]` — context Sam is inferring across docs.
- `[NOT CHECKED]` — referenced but not opened by Sam this session.

---

## Headline counts

| Marker | Raw repo total | After definition-filter | After noise-strip |
|---|---|---|---|
| `[SOURCE REQUIRED]` | 56 | 26 | **17** real blanks |
| `[DECISION REQUIRED]` | 65 | 47 | **24** real forks |
| `[LOGIC TO BE CONFIRMED]` | 117 | 94 | **18** real gaps + ~37 MANIFEST status flags + ~38 process-template residue |
| **TOTAL** | 238 | 167 | **~59 substantive open items** |

`[OPINION confidence 80%]` — The MANIFEST has 37 `[LOGIC TO BE CONFIRMED]` flags that are **status markers on indexed files** (the file is on the manifest as a candidate, marked as not-yet-promoted), not research blanks. Same for ~half the `[DECISION REQUIRED]` hits — they're in process docs explaining when to use the token. The 59 substantive items below are the real research backlog.

---

## TIER 1 — Architect must decide before next build cycle

These are forks where progress is gated until Ewan (or the Architect rubric) calls them. `[OPINION 90%]` — these unlock other work.

### 1.1 First-department scope-lock
**Source:** `03_shadow/job-wrapups/2026-04-23_amplified-partners-orchestration-session_wrapup.md:179` `[FACT]`
**Question:** Which APQC PCF category is the **first department** built end-to-end before the system fans out?
**Why it blocks:** Without one, every department is a candidate and effort scatters. `[CLAIM]`
**Adjacent unknowns it pulls along:**
- By-function vs by-language department split
- Pre-authorisation bands (green/amber/red) for agent actions inside that department
- Source-anchor access model for `/Users/ewansair/Amplified Partners/`

### 1.2 Per-client container architecture: on-site logic vs phone-home
**Source:** `03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md:106` `[FACT]`
**Question:** Per-client containers run HoundDog + CRM + P2 tokeniser. Does the container **execute logic on-site** (data sovereignty maximised) or **phone home** to a federated brain (Kaizen/Pudding can prospect across clients)?
**Why it blocks:** Sets the data-residency contract Amplified Partners signs with every customer. Affects HoundDog scope, P2 tokeniser placement, and FalkorDB topology. `[CLAIM]`
**Adjacent decision:** P2 tokenisation method — one-way hashing vs reversible-vault — pending re-identification risk assessment (`03_shadow/sessions/2026-04-18_ai-native-session_v1.md:10432`) `[FACT]`

### 1.3 Graph+vector DB strategy
**Source:** `03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md:530` `[FACT]`
**Question:** Start with SQL + recursive CTEs (viable up to ~10K edges) or jump direct to FalkorDB/Qdrant?
**Verified tonight (per Devon):** SQL-with-graph is real, not bullshit. `[FACT — per Devon's note]`
**Why it blocks:** Wrong choice = either rework at scale or premature ops complexity. `[OPINION 75%]`

### 1.4 Covered AI definition
**Source:** `00_authority/TAXONOMY.md:38, :44, :90` `[FACT]`
**Question:** What **is** Covered AI? TAXONOMY explicitly says "distinct from Cove. Definition to be provided by Ewan. Do not conflate with Cove."
**Why it blocks:** Until defined, every doc using the name has a hidden conflict risk. `[OPINION 70%]`

### 1.5 Stateless-handover neutrality clause — promote to authority?
**Source:** `03_shadow/job-wrapups/2026-04-23_amplified-partners-orchestration-session_wrapup.md:179` `[FACT]`
**Question:** Promote `01_truth/processes/2026-04_stateless-handover_neutrality-clause_v1.md` from candidate to `00_authority/`? Currently referenced by authoritative `OPINION_CONFIDENCE.md` despite being non-authoritative — that's a manifest-bibliography drift. `[CLAIM]`
**Recommendation `[OPINION 80%]`:** Promote. The fact that an authority doc already cites it makes it *de facto* authority.

### 1.6 OPINION_CONFIDENCE — below-floor carve-out for non-actions
**Source:** `00_authority/OPINION_CONFIDENCE.md:62` `[FACT]`
**Question:** Below-floor rule currently treats "do nothing / preserve incumbent" the same as "active change" — both require step-4 surface to architect. Should pure inaction below confidence floor have an exception lane?
**Why it blocks:** Right now it's possibly over-strict for status-quo paths and may slow legit "leave it alone" decisions. `[CLAIM]`

---

## TIER 2 — Authority docs needing a definition pass

These are `[LOGIC TO BE CONFIRMED]` items inside live authority files. They're not architect-blocking, but every agent reading them gets ambiguity.

### 2.1 PROJECT_INTENT — three undefined first-cut concretes
**Source:** `00_authority/PROJECT_INTENT.md:126-128` `[FACT]`
- Exact first production-grade schema shape `[LOGIC TO BE CONFIRMED]`
- First vertical proof-of-value slice `[LOGIC TO BE CONFIRMED]` (likely Jesmond Plumbing per other docs `[ASSUMED]`)
- Initial automated ingestion pipeline set and cadence `[LOGIC TO BE CONFIRMED]`

### 2.2 PROJECT_INTENT — Operating model section literally marked TBC
**Source:** `00_authority/PROJECT_INTENT.md:46` `[FACT]` — heading itself reads `## Operating model [LOGIC TO BE CONFIRMED]`

### 2.3 TAXONOMY — Amplified Partners legal status
**Source:** `00_authority/TAXONOMY.md:28` `[FACT]`
**Detail:** "The legal registration is in progress as of 2026-04-29. Until registration is confirmed, treat `[LOGIC TO BE CONFIRMED]` as the legal status of all sub-entities."
**Resolution path:** Companies House status check — should be doable in ~5 min. `[OPINION 95%]`

### 2.4 AGENT_ROUTING — Devon's scheduled sessions provenance
**Source:** `00_authority/AGENT_ROUTING.md:64` `[FACT]`
**Detail:** Session times (07:00 / 08:00 / 09:00 / 14:00 UTC) sourced from a Linear governance knowledge note that's "org-wide, not in-repo `[SOURCE REQUIRED]` for an in-repo authority once promoted."
**Action:** When AGENT_ROUTING promotes, port the schedule into the repo or link the Linear note canonically. `[OPINION 85%]`

### 2.5 BUILD_LOOP — math-form requirement
**Source:** `00_authority/BUILD_LOOP.md:127, :147` `[FACT]`
**Detail:** Test plan pointer for `[LOGIC TO BE CONFIRMED]` items + variables/thresholds/metrics expectations. These read as "rules-about-the-rule" rather than research blanks. `[OPINION 60%]` — probably acceptable as-is.

---

## TIER 3 — Vault-named components with no traced code path

**Source file:** `03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md` (Devon's amplified-partners map, 2026-04-23) `[FACT]`

These are named in vault knowledge notes but Devon couldn't find code:

| # | Component | Named role | Status | Resolution path |
|---|---|---|---|---|
| 3.1 | **Triumvirate** (lines 164, 458) | Parallel Claude + Grok + Gemini consensus | `[SOURCE REQUIRED — no code path traced]` | Search vault + grep all org repos for "triumvirate" |
| 3.2 | **Cato** (lines 165, 459) | Enforcement logic for agent commitments | `[SOURCE REQUIRED]` | Same |
| 3.3 | **Sentinel** (lines 166, 460) | Drift/security monitoring | `[SOURCE REQUIRED]` | Same |
| 3.4 | **`cove` repo** (line 323) | "Cove Platform — AI OS for SMBs", 25KB, 2026-03-13 | `[SOURCE REQUIRED]` | Org-list `gh repo list Amplified-Partners` |
| 3.5 | **`amplified-core`** (line 324) | "MCP Gateway for Bob", 9KB, 2026-03-22 | `[SOURCE REQUIRED]` | Same |
| 3.6 | **`commitment-system`** (line 326) | 27KB, 2026-02-11 | `[SOURCE REQUIRED]` | Same |
| 3.7 | **22→16 repo gap** (line 333) | 6 named repos not visible to Devon's token | `[DECISION REQUIRED]` (token scope vs deletion vs rename) | Re-list with broader-scope GitHub PAT (one shared in keys.env tonight `[ASSUMED]`) |

`[OPINION 75%]` — Resolution time per item: 5-15 min once the right GitHub token is used. Sam can do these batched given the keys.env knowledge from the override window. **However:** Sam does not have keys after the 10-min closure, so this needs Ewan or Devon with GH access.

---

## TIER 4 — Process / SOP gaps

These are inside `01_truth/processes/` — process documents that are themselves marked `[LOGIC TO BE CONFIRMED]` because they're candidate SOPs awaiting promotion.

### 4.1 Methodology-prospecting v1 — frontmatter standard, ID scheme, naming
**Source:** `01_truth/processes/2026-04_candidate-nuggets_from_dept-5-operations-methodology_v1.md:31, :46, :62` `[FACT]`
- Concrete tool choice, index filename, taxonomy details
- Named products/systems/performance claims
- Detailed frontmatter spec, ID scheme, naming standard

### 4.2 Research-on-research bootstrap — five-candidate shortlist completion
**Source:** `01_truth/processes/2026-04_research-on-research_bootstrap-remit_v1.md:50, :54` `[FACT]`
**Status:** First pass not yet complete. `[CLAIM]`

### 4.3 Operating-rhythm check seams
**Source:** `01_truth/processes/2026-04_operating-rhythm-check-seams_v1.md:25` `[FACT]`
**Detail:** File literally has a `## Open decisions [DECISION REQUIRED]` section. `[NOT CHECKED — what's listed under it]`

### 4.4 Methodology-scoring rubric — provenance bounds
**Source:** `01_truth/processes/2026-04_methodology-scoring-rubric_v1.md:16` `[FACT]` — source-pointer / `[SOURCE REQUIRED]` / `[LOGIC TO BE CONFIRMED]` choice point

### 4.5 Hygiene-role charter — escalation boundary
**Source:** `01_truth/processes/2026-04_hygiene-role-charter_v1.md:33` `[FACT]` — when does in-frame cleanup cross into truth/world change

### 4.6 Three-layer business-bible model — layer boundaries
**Source:** `01_truth/processes/2026-03_business-bible_three-layer-model_v1.md` `[NOT CHECKED — opened only via grep]`

---

## TIER 5 — External research blanks

External vendor / tooling unknowns where the answer lives outside the repo.

### 5.1 watsonx Orchestrate Resource-Unit rate by tier
**Source:** `03_shadow/job-wrapups/2026-04-23_amplified-partners-orchestration-session_wrapup.md:178` `[FACT]`
**Detail:** Pricing was pulled from AWS Marketplace listing as `[CURRENT BEST EVIDENCE]`, but Resource-Unit rate per tier still missing. `[CLAIM]`
**Resolution:** IBM website + AWS Marketplace, ~30 min.

### 5.2 Named-methodology claim for any 2026 multi-agent orchestration platform
**Source:** Same `[FACT]`
**Detail:** None of the four platforms reviewed surfaced one. May genuinely not exist. `[OPINION 60% it doesn't exist]`

### 5.3 Tavily / SearXNG provenance
**Source:** `03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md:274` `[FACT]`
**Status:** SearXNG is **CONFIRMED** running on Beast `[FACT — per beast-searxng skill loaded earlier in session]`. The `[SOURCE REQUIRED]` is stale and can be closed by Sam if the architect agrees. `[OPINION 90%]`

### 5.4 One-page process register `amplified_process_register.xlsx`
**Source:** `03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md:560` `[FACT]`
**Status:** Filename known, contents unread. Likely on Ewan's Mac. `[ASSUMED]`

---

## TIER 6 — Architecture follow-ons (lower priority)

### 6.1 Signature pre-commit hook — build it?
**Source:** `03_shadow/job-wrapups/2026-04-23_amplified-partners-orchestration-session_wrapup.md:179` `[FACT]`
**Detail:** Flagged as follow-on under SIGNATURES.md § Enforcement.

### 6.2 Cross-session continuity — persistent knowledge note?
**Source:** Same `[FACT]`
**Detail:** "Whether to suggest a persistent knowledge note for cross-session continuity."

### 6.3 PR clean-build of the five late-session authority/session files
**Source:** Same `[FACT]`

### 6.4 Free-trial on watsonx Orchestrate
**Source:** Same `[FACT]`

### 6.5 Name for the human-database (architect reserves)
**Source:** Same `[FACT]`

### 6.6 Per-vertical scoping exercise (one-week, before any 3-month API department commitment)
**Source:** `03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md:527` `[FACT]`

### 6.7 P2 tokenisation method — one-way hashing vs reversible vault
**Source:** `03_shadow/sessions/2026-04-18_ai-native-session_v1.md:10432` `[FACT]`
**Detail:** Cross-references TIER 1.2. Resolution requires GDPR re-identification risk assessment before go-live.

---

## What's NOT a blank (false positives we can ignore)

- 56 `[SOURCE REQUIRED]` hits and 41 `[LOGIC TO BE CONFIRMED]` hits are **vocabulary listings** in SOPs, ONBOARDING, PRINCIPLES, NORTH_STAR, etc — they teach agents to use the marker, not to flag a blank.
- 37 `[LOGIC TO BE CONFIRMED]` flags in `00_authority/MANIFEST.md` are **promotion-status markers** on indexed candidate files — the manifest is doing its job, not flagging missing logic.
- The session log `03_shadow/sessions/2026-04-18_ai-native-session_v1.md` has 15 hits but ~13 are inside instructional passages explaining when to use the marker — only 2 are real blanks (P2 tokenisation, EVPI/Taguchi-Loss bounds).

---

## Recommended order of attack

`[OPINION 80% confidence on this ordering]`

1. **Tier 2.3** Companies House check — 5 min, closes a stale flag
2. **Tier 5.3** Close stale SearXNG `[SOURCE REQUIRED]` — Sam can submit a 1-line PR
3. **Tier 3.4-3.7** Repo-existence sweep — Devon or Ewan with GH PAT, 30 min batched
4. **Tier 1.4** Covered AI definition — Architect-only, async write-up
5. **Tier 1.5** Promote stateless-handover neutrality clause — Architect call, then Devon PRs
6. **Tier 1.1, 1.2, 1.3** First-department, container-architecture, graph-DB — these are the three architect-level forks that need genuine deliberation; not for tonight
7. **Tier 4.x** SOP gaps — work through during the natural next promotion cycle, not as a special project

---

## Open question for the architect

`[OPINION 65%]` — Should `00_authority/MANIFEST.md` use a *different* status flag for "candidate doc, not yet promoted" vs "doc with internal logic gaps"? Current overload of `[LOGIC TO BE CONFIRMED]` makes the marker count noisy and hides real gaps. Suggested split:

- `[CANDIDATE]` — file is indexed but not yet promoted (status flag)
- `[LOGIC TO BE CONFIRMED]` — file's *contents* have an unresolved logic gap

This would drop the MANIFEST hit count from 37 to ~3-5 and make whole-repo audits much sharper.

---

## Signature

**Sam-Comp** | session perplexity-sam-2026-05-04-22:43-BST → 2026-05-05-01:30-BST
Bias-bound markers active. Architect override 1/3 used (keys.env knowledge window). No other authority consumed.
