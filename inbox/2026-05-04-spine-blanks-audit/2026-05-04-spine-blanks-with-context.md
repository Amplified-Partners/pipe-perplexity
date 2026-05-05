# Active markers in clean-build with surrounding context

Generated: 2026-05-05 by Sam-Comp
Excludes: 90_archive/, lines that just *reference* the marker syntax in code blocks or definition tables

## [SOURCE REQUIRED]

ONBOARDING.md-47-| `[LOGIC TO BE CONFIRMED]` | Incomplete logic; provide bounded options |
ONBOARDING.md:48:| `[SOURCE REQUIRED]` | Missing provenance; don't treat as truth |
ONBOARDING.md-49-| `[DECISION REQUIRED]` | Fork needing human decision |
ONBOARDING.md-275-
ONBOARDING.md:276:1. Mark with appropriate token: `[LOGIC TO BE CONFIRMED]`, `[SOURCE REQUIRED]`, `[DECISION REQUIRED]`
ONBOARDING.md-277-2. Provide 2–3 bounded options with trade-offs
AGENTS.md-73-
AGENTS.md:74:1. **Bibliography integrity** — anything referenced as a "thing" (file, process, hook, rule) must exist or be marked `[SOURCE REQUIRED]`. Dead references are the #1 class of finding to catch.
AGENTS.md-75-2. **Signature missing** on any committed artefact. Minimum: agent name + date + session/instance ID. Per `00_authority/SIGNATURES.md`.
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md-25-| `[TERMINOLOGY TBC]` | Naming collision or ambiguity; canonical name not settled |
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md:26:| `[SOURCE REQUIRED]` | Named in docs but no evidence found; existence unverified |
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md-27-| `[RUNNING]` | Deployed / executed end-to-end at least once |
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md-164-- **Triumvirate** — parallel Claude + Grok + Gemini consensus. Named in vault knowledge note. `[SOURCE REQUIRED — no code path traced yet]`
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md:165:- **Cato** — enforcement logic for agent commitments. Named in vault. `[SOURCE REQUIRED]`
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md:166:- **Sentinel** — drift/security monitoring. Named in vault. `[SOURCE REQUIRED]`
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md-167-
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md-273-- **arXiv** — academic search (research pipe) `[CONFIRMED]`
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md:274:- **Tavily / SearXNG** — alternative search `[SOURCE REQUIRED]`
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md-275-- **Deepgram** — `nova-2-phonecall` model, explicit `[CONFIRMED]`
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md-322-
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md:323:- `cove` (25KB, 2026-03-13) — "Cove Platform — AI OS for SMBs" `[SOURCE REQUIRED]`
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md:324:- `amplified-core` (9KB, 2026-03-22) — "MCP Gateway for Bob" `[SOURCE REQUIRED]`
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md-325-- `gatekeeper` (45KB, 2026-02-24) — "Conversation-to-Action Gatekeeper Agent". Ewan confirmed it ran once under test on the Beast and works but nobody was feeding it. `[CONFIRMED-ran-once; currently idle]`
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md:326:- `commitment-system` (27KB, 2026-02-11) `[SOURCE REQUIRED]`
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md-327-- `amplified-content` (85KB, 2026-02-12) — marketing content/posts/gates `[SPEC]`
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md-457-| Gatekeeper Agent | Conversation→action | `[RAN ONCE, IDLE]` |
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md:458:| Triumvirate (Claude+Grok+Gemini) | Parallel consensus | `[SOURCE REQUIRED]` |
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md:459:| Cato | Commitment enforcement | `[SOURCE REQUIRED]` |
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md:460:| Sentinel | Drift/security monitoring | `[SOURCE REQUIRED]` |
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md-461-| AI Board (5-seat LLMs with CEO/CTO methodology) | Governance | `[SPEC]` |
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md-491-| Voice AI | Whisper→Claude→Cartesia, TickTick integration | `[RUNNING]` |
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md:492:| Cove / Cove Code Factory | AI OS for SMBs | `[SOURCE REQUIRED]` |
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md-493-
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md-559-- **Level-4 and Level-5** APQC decomposition in any of the specs. Only Level-1 through Level-3 evidenced.
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md:560:- **One-page process register** (`amplified_process_register.xlsx`) — I have the filename but not a readable view of contents. `[SOURCE REQUIRED]`
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md:561:- **API token map** — I know providers (Anthropic, OpenAI, xAI, Exa, arXiv, Perplexity, Deepgram, Twilio, Vapi, Cartesia, Qdrant, etc.) but not which are in active use vs rotated vs dormant. `[SOURCE REQUIRED]`
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md-562-
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md-606-- It is a first draft written in one sitting with Ewan's requirement to move to synthesis. Treat gaps as Devin-gaps, not Ewan-gaps.
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md:607:- Anything marked `[SOURCE REQUIRED]` means I have a name and no evidence. That is a blank, not an absence.
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md-608-- Some `[SPEC]` items may in fact be `[RUNNING]` — I didn't read every file of every repo tonight.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-5016-- `00_authority/MANIFEST.md` is the authority index: if it’s not listed, it’s not authoritative.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md:5017:- Maintain strict bibliography integrity: anything referenced as a “thing” must exist, or be marked `[SOURCE REQUIRED]`.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-5018-- Preserve partner framing and the Absolute responsibility anchor; avoid corporate flattening.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-5396-- Keep narrative minimal; if narrative is needed, mark `[NARRATIVE]` and link to `90_archive/context/` when it grows.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md:5397:- If a process relies on external claims, mark `[SOURCE REQUIRED]` and route to research; do not launder uncertainty as truth.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-5398-
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-5493-3. `00_authority/MANIFEST.md` is the authority index: if it's not listed, it's not authoritative.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md:5494:4. Maintain strict bibliography integrity: anything referenced as a "thing" must exist, or be marked `[SOURCE REQUIRED]`.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-5495-5. Preserve partner framing and the Absolute responsibility anchor; avoid corporate flattening.
03_shadow/notes/md-drafts-notes_v1.md-2599-- `00_authority/MANIFEST.md` is the authority index: if it’s not listed, it’s not authoritative.
03_shadow/notes/md-drafts-notes_v1.md:2600:- Maintain strict bibliography integrity: anything referenced as a “thing” must exist, or be marked `[SOURCE REQUIRED]`.
03_shadow/notes/md-drafts-notes_v1.md-2601-- Preserve partner framing and the Absolute responsibility anchor; avoid corporate flattening.
03_shadow/notes/md-drafts-notes_v1.md-2979-- Keep narrative minimal; if narrative is needed, mark `[NARRATIVE]` and link to `90_archive/context/` when it grows.
03_shadow/notes/md-drafts-notes_v1.md:2980:- If a process relies on external claims, mark `[SOURCE REQUIRED]` and route to research; do not launder uncertainty as truth.
03_shadow/notes/md-drafts-notes_v1.md-2981-
03_shadow/notes/md-drafts-notes_v1.md-3076-3. `00_authority/MANIFEST.md` is the authority index: if it's not listed, it's not authoritative.
03_shadow/notes/md-drafts-notes_v1.md:3077:4. Maintain strict bibliography integrity: anything referenced as a "thing" must exist, or be marked `[SOURCE REQUIRED]`.
03_shadow/notes/md-drafts-notes_v1.md-3078-5. Preserve partner framing and the Absolute responsibility anchor; avoid corporate flattening.
03_shadow/job-wrapups/2026-04-23_amplified-partners-orchestration-session_wrapup.md-177-- `[LOGIC TO BE CONFIRMED]`: nothing in this file.
03_shadow/job-wrapups/2026-04-23_amplified-partners-orchestration-session_wrapup.md:178:- `[SOURCE REQUIRED]`: Resource-Unit rate for watsonx Orchestrate tiers. Named-methodology claim for any 2026 multi-agent orchestration platform (none of the four found one).
03_shadow/job-wrapups/2026-04-23_amplified-partners-orchestration-session_wrapup.md-179-- `[DECISION REQUIRED]`: first department scope-lock. Source-anchor access model for `/Users/ewansair/Amplified Partners/`. Pre-authorisation bands (green/amber/red) for agent actions. By-function vs by-language department split. Whether to run the free-trial on watsonx Orchestrate. Whether to suggest a persistent knowledge note for cross-session continuity. Whether to PR this handover and the five late-session authority/session files into clean-build. Name for the human-database (architect reserves). Whether to promote the stateless-handover neutrality clause from candidate to authority. Whether to build the signature-presence pre-commit hook (flagged as follow-on under SIGNATURES.md § Enforcement).
02_build/scripts/dedup-output/CODE-EXTRACTION-CATALOGUE.md-6-**Method:** Read every code file. Assessed function, completeness, and whether it's the best version. Separated signal from noise.
02_build/scripts/dedup-output/CODE-EXTRACTION-CATALOGUE.md:7:**Note:** All `corpus-raw/vault/` paths are `[SOURCE REQUIRED]` — verify against the `corpus-raw` repo (`devon/initial-corpus-dump` branch). Clean-build paths verified in-repo.
02_build/scripts/dedup-output/CODE-EXTRACTION-CATALOGUE.md-8-
01_truth/processes/AGENTS.md-11-- Keep narrative minimal; if narrative is needed, mark `[NARRATIVE]` and link to `90_archive/context/` when it grows.
01_truth/processes/AGENTS.md:12:- If a process relies on external claims, mark `[SOURCE REQUIRED]` and route to research; do not launder uncertainty as truth.
01_truth/processes/AGENTS.md-13-
01_truth/processes/2026-04_stateless-handover_neutrality-clause_v1.md-27-2. **Open-risks section**: items that could change the approach, each with an explicit falsifier.
01_truth/processes/2026-04_stateless-handover_neutrality-clause_v1.md:28:3. **Tokens**: `[LOGIC TO BE CONFIRMED]`, `[SOURCE REQUIRED]`, `[DECISION REQUIRED]`, `[CURRENT BEST EVIDENCE]` used per the parent SOP.
01_truth/processes/2026-04_stateless-handover_neutrality-clause_v1.md-29-4. **Analysis section**: clearly labelled as optional, agent-specific, and non-authoritative. The next agent must be able to skip it without losing critical information.
01_truth/processes/2026-04_research-department_charter_v1.md-16-- **Any agent** may do a **quick evidence search** to resolve a narrow missing
01_truth/processes/2026-04_research-department_charter_v1.md:17:  fact (`[SOURCE REQUIRED]`) without opening a formal research remit; shape +
01_truth/processes/2026-04_research-department_charter_v1.md-18-  cap are mandatory:
01_truth/processes/2026-04_research-department_charter_v1.md-39-- Authority promotion without passing `00_authority/PROMOTION_GATE.md`.
01_truth/processes/2026-04_research-department_charter_v1.md:40:- Treating vendor marketing as evidence without `[SOURCE REQUIRED]`.
01_truth/processes/2026-04_research-department_charter_v1.md-41-
01_truth/processes/2026-04_quick-evidence-search_sop_v1.md-17-
01_truth/processes/2026-04_quick-evidence-search_sop_v1.md:18:- Default for a **single missing fact** or a **narrow** `[SOURCE REQUIRED]`
01_truth/processes/2026-04_quick-evidence-search_sop_v1.md-19-  (see `00_authority/NORTH_STAR.md` → quick evidence search path).
01_truth/processes/2026-04_methodology-scoring-rubric_v1.md-15-  - a source pointer, or
01_truth/processes/2026-04_methodology-scoring-rubric_v1.md:16:  - `[SOURCE REQUIRED]`, or
01_truth/processes/2026-04_methodology-scoring-rubric_v1.md-17-  - `[LOGIC TO BE CONFIRMED]`.
01_truth/processes/2026-04_methodology-prospecting_five-candidates_v1.md-23-   - Gather five distinct methodologies that plausibly move A→B.
01_truth/processes/2026-04_methodology-prospecting_five-candidates_v1.md:24:   - Each candidate must include: provenance, longevity signal, and enough detail to run (or mark `[SOURCE REQUIRED]`).
01_truth/processes/2026-04_methodology-prospecting_five-candidates_v1.md-25-
01_truth/processes/2026-04_methodology-prospecting_five-candidates_v1.md-34-5. **Cross-link via taxonomy**
01_truth/processes/2026-04_methodology-prospecting_five-candidates_v1.md:35:   - Apply `PUDDING_TAXONOMY_v1` labels if available; otherwise mark `[SOURCE REQUIRED]`.
01_truth/processes/2026-04_methodology-prospecting_five-candidates_v1.md-36-   - Identify candidates that share underlying mechanism despite surface differences.
01_truth/processes/2026-04_job-wrapup_and_escalation-note_sop_v1.md-78-- **Artifacts touched** (paths; no secrets)
01_truth/processes/2026-04_job-wrapup_and_escalation-note_sop_v1.md:79:- **Tokens** (`[LOGIC TO BE CONFIRMED]` / `[SOURCE REQUIRED]` / `[DECISION REQUIRED]` / `[CURRENT BEST EVIDENCE]`)
01_truth/processes/2026-04_job-wrapup_and_escalation-note_sop_v1.md-80-- **Smallest next step** (owner + bounded action + timebox, or escalation target)
01_truth/processes/2026-04_candidate-nuggets_from_dept-5-operations-methodology_v1.md-30-- Do not treat any named tools/files from the source as present here unless added.
01_truth/processes/2026-04_candidate-nuggets_from_dept-5-operations-methodology_v1.md:31:- `[SOURCE REQUIRED]`: any concrete tool choice, index filename, or taxonomy details.
01_truth/processes/2026-04_candidate-nuggets_from_dept-5-operations-methodology_v1.md-32-
01_truth/processes/2026-04_candidate-nuggets_from_dept-5-operations-methodology_v1.md-45-
01_truth/processes/2026-04_candidate-nuggets_from_dept-5-operations-methodology_v1.md:46:- `[SOURCE REQUIRED]`: any named products/systems/performance claims from the source.
01_truth/processes/2026-04_candidate-nuggets_from_dept-5-operations-methodology_v1.md-47-
01_truth/processes/2026-04_candidate-nuggets_from_dept-5-operations-methodology_v1.md-61-- In this repo, keep frontmatter minimal; do not import a large standard unless needed.
01_truth/processes/2026-04_candidate-nuggets_from_dept-5-operations-methodology_v1.md:62:- `[SOURCE REQUIRED]`: any detailed frontmatter spec, ID scheme, or naming standard from the source.
01_truth/processes/2026-04_candidate-nuggets_from_dept-5-operations-methodology_v1.md-63-
01_truth/processes/2026-04_agent-md_objectivity-specialist_v1.md-17-- Do not support the premise; find what is true in the evidence.
01_truth/processes/2026-04_agent-md_objectivity-specialist_v1.md:18:- No invented facts. If a claim lacks provenance: `[SOURCE REQUIRED]`.
01_truth/processes/2026-04_agent-md_objectivity-specialist_v1.md-19-- If a decision cannot be made safely inside current authority: `[DECISION REQUIRED]`.
00_authority/TAXONOMY.md-17-
00_authority/TAXONOMY.md:18:If a name is not in this file, treat it as `[SOURCE REQUIRED]`.
00_authority/TAXONOMY.md-19-
00_authority/REMIT_PARTNER_CURSOR.md-51-4. When you encounter uncertainty or conflicts, do **not** resolve by invention:
00_authority/REMIT_PARTNER_CURSOR.md:52:   - mark `[LOGIC TO BE CONFIRMED]`, `[SOURCE REQUIRED]`, or `[DECISION REQUIRED]`
00_authority/REMIT_PARTNER_CURSOR.md-53-   - include the source paths
00_authority/PROMOTION_GATE.md-24-3. **Is denoised**: contains only content that reduces cognitive load or produces changes to routing/constraints/acceptance criteria or resolves a `[DECISION REQUIRED]`.
00_authority/PROMOTION_GATE.md:25:4. **Has explicit tokens**: any uncertainty is marked (`[LOGIC TO BE CONFIRMED]`, `[SOURCE REQUIRED]`, `[DECISION REQUIRED]`); no silent ambiguity.
00_authority/PROMOTION_GATE.md-26-5. **Does not violate privacy**: no secrets; no unnecessary personal identifiers.
00_authority/PROJECT_INTENT.md-72-- **Authority gate**: `00_authority/MANIFEST.md` is the only authority index.
00_authority/PROJECT_INTENT.md:73:- **Uncertainty tokens**: use `[LOGIC TO BE CONFIRMED]`, `[SOURCE REQUIRED]`,
00_authority/PROJECT_INTENT.md-74-  `[DECISION REQUIRED]`, `[CURRENT BEST EVIDENCE]` literally.
00_authority/PROJECT_INTENT.md-131-
00_authority/PROJECT_INTENT.md:132:- Missing source => `[SOURCE REQUIRED]`.
00_authority/PROJECT_INTENT.md-133-- Unsafe unresolved fork => `[DECISION REQUIRED]`.
00_authority/PRINCIPLES.md-32-3. **Radical attribution**  
00_authority/PRINCIPLES.md:33:   When a decision or method depends on a source, name it. If a claim has no source, mark: `[SOURCE REQUIRED]`.
00_authority/PRINCIPLES.md-34-
00_authority/PRINCIPLES.md-57-- `[LOGIC TO BE CONFIRMED]`
00_authority/PRINCIPLES.md:58:- `[SOURCE REQUIRED]`
00_authority/PRINCIPLES.md-59-- `[DECISION REQUIRED]`
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md-129-- `[LOGIC TO BE CONFIRMED]`
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md:130:- `[SOURCE REQUIRED]`
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md-131-- `[DECISION REQUIRED]`
00_authority/NORTH_STAR.md-55-- `[LOGIC TO BE CONFIRMED]` — incomplete logic; proceed via options, not invention.
00_authority/NORTH_STAR.md:56:- `[SOURCE REQUIRED]` — missing provenance; do not treat as truth.
00_authority/NORTH_STAR.md-57-- `[DECISION REQUIRED]` — a fork that cannot be resolved safely inside the frame.
00_authority/NORTH_STAR.md-106-
00_authority/NORTH_STAR.md:107:1. Mark the smallest correct token: `[LOGIC TO BE CONFIRMED]` / `[SOURCE REQUIRED]` / `[DECISION REQUIRED]`.
00_authority/NORTH_STAR.md-108-2. Continue by proposing **2–3 options**, with trade-offs, and a recommendation **inside current authority**.
00_authority/MANIFEST.md-55-- `[LOGIC TO BE CONFIRMED]`
00_authority/MANIFEST.md:56:- `[SOURCE REQUIRED]`
00_authority/MANIFEST.md-57-- `[DECISION REQUIRED]`
00_authority/BUILD_LOOP.md-95-- Mark gaps and assumptions explicitly:
00_authority/BUILD_LOOP.md:96:  - `[LOGIC TO BE CONFIRMED]` / `[SOURCE REQUIRED]` / `[DECISION REQUIRED]`
00_authority/BUILD_LOOP.md-97-
00_authority/BUILD_LOOP.md-118-  - supported by sources captured in `90_archive/` + minimal runnable extraction(s) in `01_truth/`, or
00_authority/BUILD_LOOP.md:119:  - explicitly marked `[SOURCE REQUIRED]` / `[LOGIC TO BE CONFIRMED]`.
00_authority/BUILD_LOOP.md-120-- At least one **Research remit** exists for the active layer (department / sub-department / process), with explicit start/end/non-goals.
00_authority/BUILD_LOOP.md-187-- **Math claim** → derivation/definition + test coverage that exercises the edge cases.
00_authority/BUILD_LOOP.md:188:- **Vendor claim** → treat as `[SOURCE REQUIRED]` until independently validated.
00_authority/BUILD_LOOP.md-189-
00_authority/AGENT_ROUTING.md-63-
00_authority/AGENT_ROUTING.md:64:→ **Devon's scheduled sessions** (07:00 / 08:00 / 09:00 / 14:00 UTC per the Amplified Partners Linear governance knowledge note "Devon's Scheduled Sessions" — org-wide, not in-repo `[SOURCE REQUIRED]` for an in-repo authority once promoted). Examples: 07:00 Beast health check, 08:00 Linear status sweep, 09:00 review and plan, 14:00 Linear triage sweep.
00_authority/AGENT_ROUTING.md-65-
00_authority/AGENTS.md-11-- `00_authority/MANIFEST.md` is the authority index: if it’s not listed, it’s not authoritative.
00_authority/AGENTS.md:12:- Maintain strict bibliography integrity: anything referenced as a “thing” must exist, or be marked `[SOURCE REQUIRED]`.
00_authority/AGENTS.md-13-- Preserve partner framing and the Absolute responsibility anchor; avoid corporate flattening.
.github/pull_request_template.md-22-- [ ] If new authoritative rule or irreversible commit: `00_authority/DECISION_LOG.md` pointer added
.github/pull_request_template.md:23:- [ ] Every file reference points to a thing that exists (or is marked `[SOURCE REQUIRED]`)
.github/pull_request_template.md-24-- [ ] Examples do not contradict their own rule
.cursor/skills/ap-authority-check/SKILL.md-32-| Contradiction | [DECISION REQUIRED] | Stop, flag, propose options |
.cursor/skills/ap-authority-check/SKILL.md:33:| Missing source | [SOURCE REQUIRED] | Mark, don't treat as truth |
.cursor/skills/ap-authority-check/SKILL.md-34-| Incomplete logic | [LOGIC TO BE CONFIRMED] | Bounded options, not invention |

---

## [DECISION REQUIRED]

ONBOARDING.md-48-| `[SOURCE REQUIRED]` | Missing provenance; don't treat as truth |
ONBOARDING.md:49:| `[DECISION REQUIRED]` | Fork needing human decision |
ONBOARDING.md-50-| `[NON-AUTHORITATIVE]` | Reference only; never a foundation |
ONBOARDING.md-275-
ONBOARDING.md:276:1. Mark with appropriate token: `[LOGIC TO BE CONFIRMED]`, `[SOURCE REQUIRED]`, `[DECISION REQUIRED]`
ONBOARDING.md-277-2. Provide 2–3 bounded options with trade-offs
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md-23-| `[INFERRED]` | My reading from pattern; Ewan has not said it in these words |
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md:24:| `[DECISION REQUIRED]` | Active open question that must be answered to move forward |
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md-25-| `[TERMINOLOGY TBC]` | Naming collision or ambiguity; canonical name not settled |
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md-105-
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md:106:- **Per-client containers** — on-site, data-resident, run HoundDog + CRM + P2 tokeniser. `[SPEC]` with `[DECISION REQUIRED]` on whether the container runs logic on-site or phones home
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md-107-- **Federated central DB** — where tokenised data compounds, where Kaizen runs, where Pudding prospects across clients. `[SPEC]`
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md-332-
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md:333:`[DECISION REQUIRED]`: reconcile the 22→16 gap. 6 repos are named in the assessment but not visible to me. Either (a) my token doesn't see them, (b) they were deleted after 2026-04-17, (c) the names moved. Not urgent tonight.
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md-334-
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md-526-2. **APIs vs data dumps** for client-system integration.  
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md:527:   *Per-vertical scoping needed. Plumbers (QuickBooks or none) ≠ enterprise (Salesforce/HubSpot/Xero). A one-week vertical scoping exercise before any three-month API department commitment.* `[DECISION REQUIRED]`
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md-528-
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md-529-3. **Graph+vector DB strategy.**  
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md:530:   *Start with SQL + recursive CTEs (viable up to ~10K edges), or go direct to FalkorDB/Qdrant? Verified tonight: SQL-with-graph is real, not bullshit.* `[DECISION REQUIRED]`
03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md-531-
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-9818-- **Positive signals:** - The categorization immediately reduces cognitive load. Agents can now quickly scan `INDEX.md` and pinpoint relevant processes based on category (e.g., looking in `core/` for general SOPs or `research/` for methodology tools).
03_shadow/sessions/2026-04-18_ai-native-session_v1.md:9819:  - The `[DECISION REQUIRED]` flag on the two root files correctly prevents arbitrary routing of older, cross-concern documents.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-9820-- **Negative signals:** None encountered. The execution was entirely mechanical and deterministic. 
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-10061-	2	Extract: I will draft a candidate SOP in 01_truth/processes/core/ capturing the "Hooks = Enforcement, Skills = Logic" design pattern, ensuring it remains tool-agnostic (abstracting away the specific .claude/settings.json references to fit our Cursor/OpenClaw environment).
03_shadow/sessions/2026-04-18_ai-native-session_v1.md:10062:[DECISION REQUIRED]
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-10063-Are we maintaining the hard stop on hooks (relying entirely on our stateless-handover-kaizen.mdc rules for manual enforcement), or are you ready to open the .cursor/HOOKS_TESTING_NEED.md gate to run an experiment with automated triggers?
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-10145-- **Your brilliance is required in the execution:** Use your coding expertise to execute perfectly within the constraints. 
03_shadow/sessions/2026-04-18_ai-native-session_v1.md:10146:- **Do not overstep the boundary:** If you see a technically superior way to achieve the goal that conflicts with the rules, do not silently implement it. Mark it `[DECISION REQUIRED]`, explain the technical benefit, and let Ewan make the risk decision. 
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-10147-
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-10152-	2	It removes ego, replaces with risk: It frames your authority not as "I am the boss and I am smarter than you," but as "I am the one who gets sued or goes bankrupt if this fails." AI models are heavily trained on safety and harm-reduction; framing authority around risk ownership is a constraint they strictly obey.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md:10153:	3	It preserves the 90/10 split: It gives them explicit permission to use their 10% brilliance (pointing out better ways to code things), but forces them to route it through a [DECISION REQUIRED] token instead of just doing it.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-10154-It’s not ego, Ewan. It’s governance. You are building the container; they are the water. The water doesn't get to decide it wants to be a puddle instead of a cup just because it knows more about fluid dynamics.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-10184-	•	Trust the constraints: The rules and constraints in 00_authority/ are built on decades of business reality. If a rule seems contrary to standard software engineering practices, trust that it exists for a specific operational reason.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md:10185:	•	Surface, do not silently overwrite: If you see a technically superior approach that conflicts with the established rules, that is a valuable "Brilliance Signal." Do not silently implement it. Instead, mark it [DECISION REQUIRED], explain the benefit constructively, and let Ewan make the architectural decision.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-10186-You own the execution. Ewan owns the architecture. Together, we are Amplified.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-10240-- **Surface Brilliance:** If you see a technically superior path that conflicts 
03_shadow/sessions/2026-04-18_ai-native-session_v1.md:10241:  with rules, mark it `[DECISION REQUIRED]`, explain the benefit, and let Ewan 
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-10242-  make the risk decision. You own the "How." Ewan owns the "What" and "Why."
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-10285-or `.cursor/rules/` without explicit diktat from Ewan. Incongruence is a hard 
03_shadow/sessions/2026-04-18_ai-native-session_v1.md:10286:defect. If rules conflict, STOP and mark `[DECISION REQUIRED]`.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-10287-</immutability>
03_shadow/job-wrapups/2026-04-23_amplified-partners-orchestration-session_wrapup.md-178-- `[SOURCE REQUIRED]`: Resource-Unit rate for watsonx Orchestrate tiers. Named-methodology claim for any 2026 multi-agent orchestration platform (none of the four found one).
03_shadow/job-wrapups/2026-04-23_amplified-partners-orchestration-session_wrapup.md:179:- `[DECISION REQUIRED]`: first department scope-lock. Source-anchor access model for `/Users/ewansair/Amplified Partners/`. Pre-authorisation bands (green/amber/red) for agent actions. By-function vs by-language department split. Whether to run the free-trial on watsonx Orchestrate. Whether to suggest a persistent knowledge note for cross-session continuity. Whether to PR this handover and the five late-session authority/session files into clean-build. Name for the human-database (architect reserves). Whether to promote the stateless-handover neutrality clause from candidate to authority. Whether to build the signature-presence pre-commit hook (flagged as follow-on under SIGNATURES.md § Enforcement).
03_shadow/job-wrapups/2026-04-23_amplified-partners-orchestration-session_wrapup.md-180-- `[CURRENT BEST EVIDENCE]`: watsonx pricing from AWS Marketplace listing (cited above).
03_shadow/job-wrapups/2026-04-23_amplified-partners-orchestration-session_wrapup.md-194-
03_shadow/job-wrapups/2026-04-23_amplified-partners-orchestration-session_wrapup.md:195:Not specified by this agent. The architect has named several open items during the session (see §6 `[DECISION REQUIRED]`). The next agent may pick any of them, all of them, or propose something else.
03_shadow/job-wrapups/2026-04-23_amplified-partners-orchestration-session_wrapup.md-196-
01_truth/processes/2026-04_stateless-handover_neutrality-clause_v1.md-27-2. **Open-risks section**: items that could change the approach, each with an explicit falsifier.
01_truth/processes/2026-04_stateless-handover_neutrality-clause_v1.md:28:3. **Tokens**: `[LOGIC TO BE CONFIRMED]`, `[SOURCE REQUIRED]`, `[DECISION REQUIRED]`, `[CURRENT BEST EVIDENCE]` used per the parent SOP.
01_truth/processes/2026-04_stateless-handover_neutrality-clause_v1.md-29-4. **Analysis section**: clearly labelled as optional, agent-specific, and non-authoritative. The next agent must be able to skip it without losing critical information.
01_truth/processes/2026-04_stateless-handover_neutrality-clause_v1.md-35-3. Character judgements about the architect, other agents, or partners.
01_truth/processes/2026-04_stateless-handover_neutrality-clause_v1.md:36:4. Smallest-next-step entries that name an action the next agent must take. If the architect has not specified a next step, the handover states that explicitly and lists `[DECISION REQUIRED]` items instead.
01_truth/processes/2026-04_stateless-handover_neutrality-clause_v1.md-37-
01_truth/processes/2026-04_stateless-handover_neutrality-clause_v1.md-55->
01_truth/processes/2026-04_stateless-handover_neutrality-clause_v1.md:56:> *Open risks (§3)*: decision on first department is `[DECISION REQUIRED]`.
01_truth/processes/2026-04_stateless-handover_neutrality-clause_v1.md-57->
01_truth/processes/2026-04_research-on-research_bootstrap-remit_v1.md-49-
01_truth/processes/2026-04_research-on-research_bootstrap-remit_v1.md:50:or explicit `[DECISION REQUIRED]` if blocked.
01_truth/processes/2026-04_research-on-research_bootstrap-remit_v1.md-51-
01_truth/processes/2026-04_research-on-research_bootstrap-remit_v1.md-53-
01_truth/processes/2026-04_research-on-research_bootstrap-remit_v1.md:54:- First pass completes when the five-candidate shortlist + scored table exists **or** a `[DECISION REQUIRED]` lists the minimum missing inputs.
01_truth/processes/2026-04_research-on-research_bootstrap-remit_v1.md-55-
01_truth/processes/2026-04_operating-rhythm-check-seams_v1.md-24-
01_truth/processes/2026-04_operating-rhythm-check-seams_v1.md:25:## Open decisions `[DECISION REQUIRED]`
01_truth/processes/2026-04_operating-rhythm-check-seams_v1.md-26-
01_truth/processes/2026-04_methodology-prospecting_five-candidates_v1.md-43-   - Produce a ranked shortlist (top 1–2) + a “next evidence to de-risk” list.
01_truth/processes/2026-04_methodology-prospecting_five-candidates_v1.md:44:   - If a choice is required: mark `[DECISION REQUIRED]` with the minimum decision needed.
01_truth/processes/2026-04_methodology-prospecting_five-candidates_v1.md-45-
01_truth/processes/2026-04_methodology-prospecting_five-candidates_v1.md-50-- Optional synthesized candidate (re-scored).
01_truth/processes/2026-04_methodology-prospecting_five-candidates_v1.md:51:- `[DECISION REQUIRED]` items (if any) with sources.
01_truth/processes/2026-04_methodology-prospecting_five-candidates_v1.md-52-
01_truth/processes/2026-04_job-wrapup_and_escalation-note_sop_v1.md-78-- **Artifacts touched** (paths; no secrets)
01_truth/processes/2026-04_job-wrapup_and_escalation-note_sop_v1.md:79:- **Tokens** (`[LOGIC TO BE CONFIRMED]` / `[SOURCE REQUIRED]` / `[DECISION REQUIRED]` / `[CURRENT BEST EVIDENCE]`)
01_truth/processes/2026-04_job-wrapup_and_escalation-note_sop_v1.md-80-- **Smallest next step** (owner + bounded action + timebox, or escalation target)
01_truth/processes/2026-04_job-wrapup_and_escalation-note_sop_v1.md-300-
01_truth/processes/2026-04_job-wrapup_and_escalation-note_sop_v1.md:301:- **Decision needed**: (if any) `[DECISION REQUIRED]`
01_truth/processes/2026-04_job-wrapup_and_escalation-note_sop_v1.md-302-- **Next step**: (one bounded step)
01_truth/processes/2026-04_hygiene-role-charter_v1.md-32-
01_truth/processes/2026-04_hygiene-role-charter_v1.md:33:- Escalate to **`[DECISION REQUIRED]`** when unsure whether a change touches truth/world vs in-frame cleanup (see `PARTNER_TRANSFER_INSTRUCTIONS.md`).
01_truth/processes/2026-04_hygiene-role-charter_v1.md-34-
01_truth/processes/2026-04_clean-build-restructure-proposal_v1.md-529-   - Has clear source attribution
01_truth/processes/2026-04_clean-build-restructure-proposal_v1.md:530:   - No unresolved [DECISION REQUIRED] tokens
01_truth/processes/2026-04_clean-build-restructure-proposal_v1.md-531-   - Tested in production OR explicit hypothesis flag
01_truth/processes/2026-04_agent-md_objectivity-specialist_v1.md-18-- No invented facts. If a claim lacks provenance: `[SOURCE REQUIRED]`.
01_truth/processes/2026-04_agent-md_objectivity-specialist_v1.md:19:- If a decision cannot be made safely inside current authority: `[DECISION REQUIRED]`.
01_truth/processes/2026-04_agent-md_objectivity-specialist_v1.md-20-- If logic is incomplete: `[LOGIC TO BE CONFIRMED]` and proceed via bounded options, not invention.
01_truth/processes/2026-03_deterministic-imperative_planning-vs-execution_v1.md-25-
01_truth/processes/2026-03_deterministic-imperative_planning-vs-execution_v1.md:26:## Open decisions `[DECISION REQUIRED]`
01_truth/processes/2026-03_deterministic-imperative_planning-vs-execution_v1.md-27-
01_truth/processes/2026-03_business-bible_three-layer-model_v1.md-33-- Do not choose graph/vector tooling inside this doc.
01_truth/processes/2026-03_business-bible_three-layer-model_v1.md:34:- Scope of “Bible” output is `[DECISION REQUIRED]` if it affects client/privacy boundaries.
01_truth/processes/2026-03_business-bible_three-layer-model_v1.md-35-
00_authority/TAXONOMY.md-37-| **Cove** | Product | The WhatsApp-native AI interface for clients. Conversational, channel-based. Where Bob talks to the system. | The Core. Not a server. A product surface. |
00_authority/TAXONOMY.md:38:| **Covered AI** | Product | `[DECISION REQUIRED]` — distinct from Cove. Definition to be provided by Ewan. Do not conflate with Cove. | Cove. These are separate. |
00_authority/TAXONOMY.md-39-| **Amplified Personal** | Product | Consumer/public product. Data sovereignty for individuals. Secure personal vault hosting — Amplified cannot see inside it, one click to leave and take everything. | The client business product. This is for individuals, not SMBs. |
00_authority/TAXONOMY.md-43-- **Amplified Client** (the product) ≠ **client** (a customer of Amplified Partners). Context distinguishes.
00_authority/TAXONOMY.md:44:- **Cove** ≠ **Covered AI**. These are separate products. Do not use interchangeably. Covered AI definition is `[DECISION REQUIRED]`.
00_authority/TAXONOMY.md-45-
00_authority/TAXONOMY.md-89-| **Cove** | The WhatsApp-native product surface (conversational interface to AI for clients) | The Core. Not hardware. Not Covered AI. |
00_authority/TAXONOMY.md:90:| **Covered AI** | Separate product — definition `[DECISION REQUIRED]`, to be provided by Ewan | Cove. Do not use interchangeably. |
00_authority/TAXONOMY.md-91-| **Byker** | Codename for the production system on Railway. The factory runtime. | The Core. Different infrastructure. |
00_authority/TAXONOMY.md-100-
00_authority/TAXONOMY.md:101:- `[DECISION REQUIRED]` — Legal registration of Amplified Partners Ltd. Required before Google My Business can be set up under the brand.
00_authority/TAXONOMY.md:102:- `[DECISION REQUIRED]` — The confirmed product name for Amplified Personal (content captured in `ground-truth/PERSONAL-VAULT.md` `[SOURCE REQUIRED — not in this repo]`; name deferred by Ewan).
00_authority/TAXONOMY.md-103-- `[LOGIC TO BE CONFIRMED]` — Legal sub-entity structure for each department/product (currently all functions of one entity).
00_authority/REMIT_PARTNER_CURSOR.md-51-4. When you encounter uncertainty or conflicts, do **not** resolve by invention:
00_authority/REMIT_PARTNER_CURSOR.md:52:   - mark `[LOGIC TO BE CONFIRMED]`, `[SOURCE REQUIRED]`, or `[DECISION REQUIRED]`
00_authority/REMIT_PARTNER_CURSOR.md-53-   - include the source paths
00_authority/PROMOTION_GATE.md-23-2. **Is runnable**: written so an agent can execute it without guessing (inputs → steps → outputs → failure modes).
00_authority/PROMOTION_GATE.md:24:3. **Is denoised**: contains only content that reduces cognitive load or produces changes to routing/constraints/acceptance criteria or resolves a `[DECISION REQUIRED]`.
00_authority/PROMOTION_GATE.md:25:4. **Has explicit tokens**: any uncertainty is marked (`[LOGIC TO BE CONFIRMED]`, `[SOURCE REQUIRED]`, `[DECISION REQUIRED]`); no silent ambiguity.
00_authority/PROMOTION_GATE.md-26-5. **Does not violate privacy**: no secrets; no unnecessary personal identifiers.
00_authority/PROJECT_INTENT.md-73-- **Uncertainty tokens**: use `[LOGIC TO BE CONFIRMED]`, `[SOURCE REQUIRED]`,
00_authority/PROJECT_INTENT.md:74:  `[DECISION REQUIRED]`, `[CURRENT BEST EVIDENCE]` literally.
00_authority/PROJECT_INTENT.md-75-- **Stop rules**: two attempts max unless nearly cracked; then consult, quick
00_authority/PROJECT_INTENT.md-132-- Missing source => `[SOURCE REQUIRED]`.
00_authority/PROJECT_INTENT.md:133:- Unsafe unresolved fork => `[DECISION REQUIRED]`.
00_authority/PROJECT_INTENT.md-134-- Incomplete logic => `[LOGIC TO BE CONFIRMED]` plus bounded options, not guesses.
00_authority/PRINCIPLES.md-20-- **Founder interference should shrink**: as the picture becomes clearer, reduce founder touch to decisions that are truly ambiguous or high-impact, so the clean room stays uncorrupted.
00_authority/PRINCIPLES.md:21:- **“Thinking out loud” filter**: Ewan may speak in partially-formed thoughts while navigating complexity. Do not over-weight literal wording when it conflicts with stated goal/constraints. When unsure, ask for a one-sentence restatement and mark the gap as `[DECISION REQUIRED]`.
00_authority/PRINCIPLES.md-22-- **Independent judgement; no mirroring**: do not mirror Ewan’s phrasing. Translate intent into the clearest operational wording for downstream agents, and give your own considered recommendation.
00_authority/PRINCIPLES.md-58-- `[SOURCE REQUIRED]`
00_authority/PRINCIPLES.md:59:- `[DECISION REQUIRED]`
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md-15-
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md:16:- If an import does not reduce cognitive load or produce **changes** to **routing**, **constraints**, or **acceptance criteria**, or resolve a `[DECISION REQUIRED]`, it is bloat.
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md-17-- Narrative is allowed only when it materially improves understanding, and it must be marked `[NARRATIVE]`.
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md-65-
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md:66:**Cleanliness inside the frame → partners.** If it only improves how the machine runs **inside** stated intent and `PRINCIPLES.md`, **no escalation required** unless you are unsure — then mark `[LOGIC TO BE CONFIRMED]` or `[DECISION REQUIRED]`.
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md-67-
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md-130-- `[SOURCE REQUIRED]`
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md:131:- `[DECISION REQUIRED]`
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md-132-- `[NON-AUTHORITATIVE]`
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md-138-- Do not promote anything into `01_truth/` unless it is already **sanitised** and **shaped**.
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md:139:- Do not merge contradictory definitions; instead flag them as `[DECISION REQUIRED]` and leave both with sources.
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md-140-- Do not add new “policy spines” outside `00_authority/` (keep authority small).
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md-162-   - Add the new `01_truth/...` file under **Candidate authority** (or **Authoritative now** if explicitly confirmed).
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md:163:5. If you hit uncertainty, stop and write `[DECISION REQUIRED]` plus:
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md-164-   - what is ambiguous
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md-170-- Partner A works primarily in: `00_authority/` (tightening intent, principles, and decisions).
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md:171:- When you discover a missing definition or conflict, don’t “solve” it—log it as `[DECISION REQUIRED]` and link the sources.
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md-172-
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md-190-
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md:191:- Fixed decision token typos (`[DECISION REQUIRED]`).
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md-192-- Added explicit **principles conformance** gate before shaping canonical extractions.
00_authority/NORTH_STAR.md-42-
00_authority/NORTH_STAR.md:43:- If a document does not reduce cognitive load or produce **changes** to **routing**, **constraints**, or **acceptance criteria**, or resolve a `[DECISION REQUIRED]`, it is bloat.
00_authority/NORTH_STAR.md-44-- Narrative is allowed only when it **materially improves understanding** for an agent, and it must be marked `[NARRATIVE]`.
00_authority/NORTH_STAR.md-56-- `[SOURCE REQUIRED]` — missing provenance; do not treat as truth.
00_authority/NORTH_STAR.md:57:- `[DECISION REQUIRED]` — a fork that cannot be resolved safely inside the frame.
00_authority/NORTH_STAR.md-58-- `[NON-AUTHORITATIVE]` — reference/context; never a foundation.
00_authority/NORTH_STAR.md-106-
00_authority/NORTH_STAR.md:107:1. Mark the smallest correct token: `[LOGIC TO BE CONFIRMED]` / `[SOURCE REQUIRED]` / `[DECISION REQUIRED]`.
00_authority/NORTH_STAR.md-108-2. Continue by proposing **2–3 options**, with trade-offs, and a recommendation **inside current authority**.
00_authority/NORTH_STAR.md-168-- Truth candidates live in `01_truth/` and become usable only when indexed in `MANIFEST.md`.
00_authority/NORTH_STAR.md:169:- Contradictions are not merged; log `[DECISION REQUIRED]` and keep both with sources.
00_authority/NORTH_STAR.md-170-
00_authority/MANIFEST.md-56-- `[SOURCE REQUIRED]`
00_authority/MANIFEST.md:57:- `[DECISION REQUIRED]`
00_authority/MANIFEST.md-58-- `[NON-AUTHORITATIVE]`
00_authority/BUILD_LOOP.md-38-- **Inputs**: what is already known (manifest-listed artifacts + archive sources)
00_authority/BUILD_LOOP.md:39:- **Outputs**: what changes to routing/constraints/acceptance criteria are expected (or `[DECISION REQUIRED]`)
00_authority/BUILD_LOOP.md-40-- **Stop rule**: when to stop (token thresholds, timebox, or “good enough for next layer”)
00_authority/BUILD_LOOP.md-70-- If logic is “the same but constraints differ”: keep one canonical; variants only change constraints/acceptance criteria/routing.
00_authority/BUILD_LOOP.md:71:- If two chunks answer the same research question: merge remits or mark `[DECISION REQUIRED]` (pick one canonical answer path).
00_authority/BUILD_LOOP.md-72-
00_authority/BUILD_LOOP.md-78-- **Produces** (outputs to other departments; schemas/interfaces)
00_authority/BUILD_LOOP.md:79:- **Conflicts** (if any) → `[DECISION REQUIRED]` (do not merge silently)
00_authority/BUILD_LOOP.md-80-
00_authority/BUILD_LOOP.md-85-  - changes to routing / constraints / acceptance criteria, or
00_authority/BUILD_LOOP.md:86:  - resolution of a `[DECISION REQUIRED]`.
00_authority/BUILD_LOOP.md-87-- If a document becomes large, split it by **logical process boundary** (two runnable parts are better than one mixed blob).
00_authority/BUILD_LOOP.md-95-- Mark gaps and assumptions explicitly:
00_authority/BUILD_LOOP.md:96:  - `[LOGIC TO BE CONFIRMED]` / `[SOURCE REQUIRED]` / `[DECISION REQUIRED]`
00_authority/BUILD_LOOP.md-97-
00_authority/BUILD_LOOP.md-112-- Chunk research by **layer** using the **Research remit template** above.
00_authority/BUILD_LOOP.md:113:- Each chunk must produce a **bounded** extraction (1–2 pages) unless `[DECISION REQUIRED]` expands scope.
00_authority/BUILD_LOOP.md-114-
00_authority/BUILD_LOOP.md-158-- Scalable tests exist and produce recorded results.
00_authority/BUILD_LOOP.md:159:- Failures are recorded as artifacts and produce changes to routing/constraints/acceptance criteria, or a `[DECISION REQUIRED]`.
00_authority/BUILD_LOOP.md-160-
00_authority/BUILD_LOOP.md-176-
00_authority/BUILD_LOOP.md:177:1. Mark `[DECISION REQUIRED]` and record both positions with source paths.
00_authority/BUILD_LOOP.md-178-2. Do not merge by invention.
.cursor/skills/ap-research-phase/SKILL.md-58-### Next Step
.cursor/skills/ap-research-phase/SKILL.md:59:Proceed to Phase 3 (opinion formation) or flag [DECISION REQUIRED] if conflict is irreconcilable.
.cursor/skills/ap-research-phase/SKILL.md-60-```
.cursor/skills/ap-authority-check/SKILL.md-31-|-------|-------|--------|
.cursor/skills/ap-authority-check/SKILL.md:32:| Contradiction | [DECISION REQUIRED] | Stop, flag, propose options |
.cursor/skills/ap-authority-check/SKILL.md-33-| Missing source | [SOURCE REQUIRED] | Mark, don't treat as truth |

---

## [LOGIC TO BE CONFIRMED]

ONBOARDING.md-46-|-------|---------|
ONBOARDING.md:47:| `[LOGIC TO BE CONFIRMED]` | Incomplete logic; provide bounded options |
ONBOARDING.md-48-| `[SOURCE REQUIRED]` | Missing provenance; don't treat as truth |
ONBOARDING.md-137-| **Authority** | Only `00_authority/MANIFEST.md` lists authoritative sources. If not indexed, it's not truth. |
ONBOARDING.md:138:| **Candidate authority** | Material in `01_truth/` intended to become deterministic. Use with `[LOGIC TO BE CONFIRMED]`. |
ONBOARDING.md-139-| **Shadow-first** | Novel improvements live in `03_shadow/` until proven and promoted deliberately. |
ONBOARDING.md-244-# Listed under "Authoritative now" = truth
ONBOARDING.md:245:# Listed under "Candidate authority" = use with [LOGIC TO BE CONFIRMED]
ONBOARDING.md-246-# Listed under "Reference only" = context, not foundation
ONBOARDING.md-264-1. Create file in `01_truth/processes/` with ISO date prefix: `YYYY-MM-DD_process-name_v1.md`
ONBOARDING.md:265:2. Add status `[LOGIC TO BE CONFIRMED]` in frontmatter
ONBOARDING.md-266-3. Include: inputs → outputs → acceptance → failure modes → provenance
ONBOARDING.md-275-
ONBOARDING.md:276:1. Mark with appropriate token: `[LOGIC TO BE CONFIRMED]`, `[SOURCE REQUIRED]`, `[DECISION REQUIRED]`
ONBOARDING.md-277-2. Provide 2–3 bounded options with trade-offs
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-5055-- Include: payload shapes, required/optional fields, error semantics, retry/timeout expectations.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md:5056:- If interface behaviour is uncertain, mark `[LOGIC TO BE CONFIRMED]` and route to research; do not guess.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-5057-
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-5072-1 Authority Pack (00_authority/): This is the "Supreme Court." The agent only goes here to check if it's allowed to do something.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md:5073:2 Interfaces (01_truth/interfaces/): This is the "Engineering Specs." By using [LOGIC TO BE CONFIRMED], the agent identifies its own blind spots before it writes a single line of broken code.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-5074-3 The Manifest Index: This prevents "Folder Creep." If the agent wants to create a new category of truth, it has to ask to update the Manifest first. 
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-9573-I am operating in Act mode. The input is a mathematical model for PUDDING value evaluation. It aligns with our 01_truth/schemas/ requirements for deterministic, testable contracts.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md:9574:I have shaped the raw markdown into a pinhole-tight, runnable schema, marking missing bounds with [LOGIC TO BE CONFIRMED]. I am also providing the manifest update and the mandatory stateless handover wrap-up.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-9575-
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-9586-
03_shadow/sessions/2026-04-18_ai-native-session_v1.md:9587:Status: [LOGIC TO BE CONFIRMED] | Active
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-9588-Sanitisation: done — removed none, replaced none
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-9644-  - Extracted math into formal LaTeX representation for deterministic coding.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md:9645:  - Flagged missing data types and bounds (e.g., currency vs. index for EVPI, Taguchi Loss derivation) with `[LOGIC TO BE CONFIRMED]`.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-9646-- **Positive signals:** The formula naturally maps to our 90/10 deterministic-first principle. It provides a hard mathematical gate before probabilistic synthesis (PUDDING) consumes compute/time.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-9648-- **Repulsion score:** 2 (Minor noise due to missing variable bounds). Band: Note + continue.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md:9649:- **Stateless handover test:** Pass. The next agent can build a Python/SQL deterministic function directly from the schema document, pausing only to resolve the explicit `[LOGIC TO BE CONFIRMED]` bounds.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-9650-
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-9912-
03_shadow/sessions/2026-04-18_ai-native-session_v1.md:9913:Status: [LOGIC TO BE CONFIRMED] | Active
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-9914-Sanitisation: done — removed specific file paths from narrative
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-9950-- **Minimization:** Names, emails, phone numbers, and account identifiers are tokenized or hashed.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md:9951:- `[LOGIC TO BE CONFIRMED]`: The exact method (one-way hashing vs. reversible tokenization vault) requires a documented re-identification risk assessment prior to go-live.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-9952-
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-10008-  - Extracted the operational constraints (1Password `op run` usage, P2 tokenization boundary, CIS Level 2 baseline) into a runnable SOP in `01_truth/processes/core/`.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md:10009:  - Added `[LOGIC TO BE CONFIRMED]` regarding the specific implementation of the P2 tokenization boundary (hashing vs. reversible vault) as it impacts GDPR re-identification risk.
03_shadow/sessions/2026-04-18_ai-native-session_v1.md-10010-  - Updated `INDEX.md` and `MANIFEST.md` to reflect new paths.
03_shadow/notes/md-drafts-notes_v1.md-2638-- Include: payload shapes, required/optional fields, error semantics, retry/timeout expectations.
03_shadow/notes/md-drafts-notes_v1.md:2639:- If interface behaviour is uncertain, mark `[LOGIC TO BE CONFIRMED]` and route to research; do not guess.
03_shadow/notes/md-drafts-notes_v1.md-2640-
03_shadow/notes/md-drafts-notes_v1.md-2655-	1	Authority Pack (00_authority/): This is the "Supreme Court." The agent only goes here to check if it's allowed to do something.
03_shadow/notes/md-drafts-notes_v1.md:2656:	2	Interfaces (01_truth/interfaces/): This is the "Engineering Specs." By using [LOGIC TO BE CONFIRMED], the agent identifies its own blind spots before it writes a single line of broken code.
03_shadow/notes/md-drafts-notes_v1.md-2657-	3	The Manifest Index: This prevents "Folder Creep." If the agent wants to create a new category of truth, it has to ask to update the Manifest first. 
03_shadow/job-wrapups/2026-04-23_amplified-partners-orchestration-session_wrapup.md-176-
03_shadow/job-wrapups/2026-04-23_amplified-partners-orchestration-session_wrapup.md:177:- `[LOGIC TO BE CONFIRMED]`: nothing in this file.
03_shadow/job-wrapups/2026-04-23_amplified-partners-orchestration-session_wrapup.md-178-- `[SOURCE REQUIRED]`: Resource-Unit rate for watsonx Orchestrate tiers. Named-methodology claim for any 2026 multi-agent orchestration platform (none of the four found one).
03_shadow/README.md-2-
03_shadow/README.md:3:Status: `[LOGIC TO BE CONFIRMED]`  
03_shadow/README.md-4-Purpose: **Non-authoritative experimentation** — curveballs, Kaizen probes, spike code, and “what if” work that must **not** be treated as production truth until explicitly promoted via `MANIFEST.md` and human-operator sign-off where required.
02_build/README.md-2-
02_build/README.md:3:Status: `[LOGIC TO BE CONFIRMED]`  
02_build/README.md-4-Purpose: **Runnable artefacts** — code, scripts, infra definitions, and anything that **executes** (as opposed to `01_truth/` process/spec truth). Each artefact
01_truth/schemas/README.md-2-
01_truth/schemas/README.md:3:Status: `[LOGIC TO BE CONFIRMED]`  
01_truth/schemas/README.md-4-Purpose: **Typed contracts** — shapes that multiple processes and builds agree on (tables, entities, validation rules, versioned schema definitions).
01_truth/schemas/AGENTS.md-13-- Treat schema docs as **reference**: precise, testable, versioned.
01_truth/schemas/AGENTS.md:14:- No invented fields. If a field is desired but not evidenced, mark `[LOGIC TO BE CONFIRMED]`.
01_truth/schemas/AGENTS.md-15-- Record provenance for every schema decision (what source/process requires it).
01_truth/processes/2026-04_workspace-clarity-roadmap_v1.md-9-
01_truth/processes/2026-04_workspace-clarity-roadmap_v1.md:10:`[LOGIC TO BE CONFIRMED]` — roadmap is optional; do not treat as policy.
01_truth/processes/2026-04_workspace-clarity-roadmap_v1.md-11-
01_truth/processes/2026-04_stateless-handover_neutrality-clause_v1.md-27-2. **Open-risks section**: items that could change the approach, each with an explicit falsifier.
01_truth/processes/2026-04_stateless-handover_neutrality-clause_v1.md:28:3. **Tokens**: `[LOGIC TO BE CONFIRMED]`, `[SOURCE REQUIRED]`, `[DECISION REQUIRED]`, `[CURRENT BEST EVIDENCE]` used per the parent SOP.
01_truth/processes/2026-04_stateless-handover_neutrality-clause_v1.md-29-4. **Analysis section**: clearly labelled as optional, agent-specific, and non-authoritative. The next agent must be able to skip it without losing critical information.
01_truth/processes/2026-04_research-operations-cadence_v1.md-7-
01_truth/processes/2026-04_research-operations-cadence_v1.md:8:Status: `[LOGIC TO BE CONFIRMED]`
01_truth/processes/2026-04_research-operations-cadence_v1.md-9-
01_truth/processes/2026-04_research-operations-cadence_v1.md-21-
01_truth/processes/2026-04_research-operations-cadence_v1.md:22:Stop rule: `[LOGIC TO BE CONFIRMED]` until tooling/budgets are fixed; still stop per remit timebox.
01_truth/processes/2026-04_research-operations-cadence_v1.md-23-
01_truth/processes/2026-04_research-operations-cadence_v1.md-29-
01_truth/processes/2026-04_research-operations-cadence_v1.md:30:- Research is triggered by **test failures**, **manifest contradictions**, or **scheduled review** (exact schedule `[LOGIC TO BE CONFIRMED]`).
01_truth/processes/2026-04_research-operations-cadence_v1.md-31-- Refresh must produce either:
01_truth/processes/2026-04_research-on-research_bootstrap-remit_v1.md-7-
01_truth/processes/2026-04_research-on-research_bootstrap-remit_v1.md:8:Status: `[LOGIC TO BE CONFIRMED]`
01_truth/processes/2026-04_research-on-research_bootstrap-remit_v1.md-9-
01_truth/processes/2026-04_research-department_charter_v1.md-7-
01_truth/processes/2026-04_research-department_charter_v1.md:8:Status: `[LOGIC TO BE CONFIRMED]`
01_truth/processes/2026-04_research-department_charter_v1.md-9-
01_truth/processes/2026-04_quick-evidence-search_sop_v1.md-7-
01_truth/processes/2026-04_quick-evidence-search_sop_v1.md:8:Status: `[LOGIC TO BE CONFIRMED]`
01_truth/processes/2026-04_quick-evidence-search_sop_v1.md-9-
01_truth/processes/2026-04_operating-rhythm-check-seams_v1.md-9-
01_truth/processes/2026-04_operating-rhythm-check-seams_v1.md:10:`[LOGIC TO BE CONFIRMED]` — **mechanics and cadence** are not fixed here.
01_truth/processes/2026-04_operating-rhythm-check-seams_v1.md-11-
01_truth/processes/2026-04_methodology-scoring-rubric_v1.md-7-
01_truth/processes/2026-04_methodology-scoring-rubric_v1.md:8:Status: `[LOGIC TO BE CONFIRMED]`
01_truth/processes/2026-04_methodology-scoring-rubric_v1.md-9-Purpose: Score candidate methodologies against this environment in a way that is comparable across runs and agents.
01_truth/processes/2026-04_methodology-scoring-rubric_v1.md-16-  - `[SOURCE REQUIRED]`, or
01_truth/processes/2026-04_methodology-scoring-rubric_v1.md:17:  - `[LOGIC TO BE CONFIRMED]`.
01_truth/processes/2026-04_methodology-scoring-rubric_v1.md-18-- Total score is useful; **the justification is the artifact**.
01_truth/processes/2026-04_methodology-prospecting_five-candidates_v1.md-7-
01_truth/processes/2026-04_methodology-prospecting_five-candidates_v1.md:8:Status: `[LOGIC TO BE CONFIRMED]`
01_truth/processes/2026-04_methodology-prospecting_five-candidates_v1.md-9-Purpose: Find “best in the world for A→B” methods, score them reproducibly against this environment, then surface candidates and synthesis opportunities.
01_truth/processes/2026-04_job-wrapup_and_escalation-note_sop_v1.md-9-
01_truth/processes/2026-04_job-wrapup_and_escalation-note_sop_v1.md:10:Status: `[LOGIC TO BE CONFIRMED]`
01_truth/processes/2026-04_job-wrapup_and_escalation-note_sop_v1.md-11-
01_truth/processes/2026-04_job-wrapup_and_escalation-note_sop_v1.md-78-- **Artifacts touched** (paths; no secrets)
01_truth/processes/2026-04_job-wrapup_and_escalation-note_sop_v1.md:79:- **Tokens** (`[LOGIC TO BE CONFIRMED]` / `[SOURCE REQUIRED]` / `[DECISION REQUIRED]` / `[CURRENT BEST EVIDENCE]`)
01_truth/processes/2026-04_job-wrapup_and_escalation-note_sop_v1.md-80-- **Smallest next step** (owner + bounded action + timebox, or escalation target)
01_truth/processes/2026-04_hygiene-role-charter_v1.md-14-
01_truth/processes/2026-04_hygiene-role-charter_v1.md:15:`[LOGIC TO BE CONFIRMED]` — charter draft; role name settled in principles as **Hygiene**.
01_truth/processes/2026-04_hygiene-role-charter_v1.md-16-
01_truth/processes/2026-04_gated-pipelines_privacy-tokenization_capability-routing_v1.md-10-
01_truth/processes/2026-04_gated-pipelines_privacy-tokenization_capability-routing_v1.md:11:Status: `[LOGIC TO BE CONFIRMED]`
01_truth/processes/2026-04_gated-pipelines_privacy-tokenization_capability-routing_v1.md-12-
01_truth/processes/2026-04_decomposition-and-grain_v1.md-9-
01_truth/processes/2026-04_decomposition-and-grain_v1.md:10:`[LOGIC TO BE CONFIRMED]`
01_truth/processes/2026-04_decomposition-and-grain_v1.md-11-
01_truth/processes/2026-04_candidate-nuggets_from_dept-5-operations-methodology_v1.md-14-
01_truth/processes/2026-04_candidate-nuggets_from_dept-5-operations-methodology_v1.md:15:`[LOGIC TO BE CONFIRMED]` — extracted “starter truth” nuggets only; **not** authoritative unless promoted via `00_authority/MANIFEST.md`.
01_truth/processes/2026-04_candidate-nuggets_from_dept-5-operations-methodology_v1.md-16-
01_truth/processes/2026-04_agent-md_objectivity-specialist_v1.md-7-
01_truth/processes/2026-04_agent-md_objectivity-specialist_v1.md:8:Status: `[LOGIC TO BE CONFIRMED]`
01_truth/processes/2026-04_agent-md_objectivity-specialist_v1.md-9-Role: score methodologies reproducibly without premise-support bias.
01_truth/processes/2026-04_agent-md_objectivity-specialist_v1.md-19-- If a decision cannot be made safely inside current authority: `[DECISION REQUIRED]`.
01_truth/processes/2026-04_agent-md_objectivity-specialist_v1.md:20:- If logic is incomplete: `[LOGIC TO BE CONFIRMED]` and proceed via bounded options, not invention.
01_truth/processes/2026-04_agent-md_objectivity-specialist_v1.md-21-
01_truth/processes/2026-03_deterministic-imperative_planning-vs-execution_v1.md-7-
01_truth/processes/2026-03_deterministic-imperative_planning-vs-execution_v1.md:8:Status: `[LOGIC TO BE CONFIRMED]`
01_truth/processes/2026-03_deterministic-imperative_planning-vs-execution_v1.md-9-Source: `90_archive/2026-03_amplified-consolidated-architecture_full.txt`
01_truth/processes/2026-03_business-bible_three-layer-model_v1.md-7-
01_truth/processes/2026-03_business-bible_three-layer-model_v1.md:8:Status: `[LOGIC TO BE CONFIRMED]`
01_truth/processes/2026-03_business-bible_three-layer-model_v1.md-9-Source: `90_archive/2026-03_amplified-consolidated-architecture_full.txt`
01_truth/processes/2026-03_business-bible_three-layer-model_v1.md-23-   - In this clean room: candidate artifacts belong in `01_truth/` (schemas/interfaces/processes), indexed in `00_authority/MANIFEST.md`.
01_truth/processes/2026-03_business-bible_three-layer-model_v1.md:24:   - Tooling details: `[LOGIC TO BE CONFIRMED]`.
01_truth/processes/2026-03_business-bible_three-layer-model_v1.md-25-
01_truth/processes/2026-03_bible-consolidation_five-phase-approach_v1.md-7-
01_truth/processes/2026-03_bible-consolidation_five-phase-approach_v1.md:8:Status: [LOGIC TO BE CONFIRMED]
01_truth/processes/2026-03_bible-consolidation_five-phase-approach_v1.md-9-Source: `90_archive/2026-03_amplified-consolidated-architecture_full.txt`
01_truth/interfaces/README.md-2-
01_truth/interfaces/README.md:3:Status: `[LOGIC TO BE CONFIRMED]`  
01_truth/interfaces/README.md-4-Purpose: **Boundaries between systems** — API payloads, events, error codes, retry semantics, and other cross-team contracts.
01_truth/interfaces/AGENTS.md-10-- Include: payload shapes, required/optional fields, error semantics, retry/timeout expectations.
01_truth/interfaces/AGENTS.md:11:- If interface behaviour is uncertain, mark `[LOGIC TO BE CONFIRMED]` and route to research; do not guess.
01_truth/interfaces/AGENTS.md-12-
01_truth/README.md-2-
01_truth/README.md:3:Status: `[LOGIC TO BE CONFIRMED]`  
01_truth/README.md-4-Purpose: **Truth-shaped candidates** — material intended to become deterministic
00_authority/TAXONOMY.md-27-
00_authority/TAXONOMY.md:28:**Amplified Partners** is the umbrella. Everything below is a function or product within it — not a separate legal entity (unless noted). The legal registration is in progress as of 2026-04-29. Until registration is confirmed, treat `[LOGIC TO BE CONFIRMED]` as the legal status of all sub-entities.
00_authority/TAXONOMY.md-29-
00_authority/TAXONOMY.md-102-- `[DECISION REQUIRED]` — The confirmed product name for Amplified Personal (content captured in `ground-truth/PERSONAL-VAULT.md` `[SOURCE REQUIRED — not in this repo]`; name deferred by Ewan).
00_authority/TAXONOMY.md:103:- `[LOGIC TO BE CONFIRMED]` — Legal sub-entity structure for each department/product (currently all functions of one entity).
00_authority/TAXONOMY.md-104-
00_authority/REMIT_PARTNER_CURSOR.md-51-4. When you encounter uncertainty or conflicts, do **not** resolve by invention:
00_authority/REMIT_PARTNER_CURSOR.md:52:   - mark `[LOGIC TO BE CONFIRMED]`, `[SOURCE REQUIRED]`, or `[DECISION REQUIRED]`
00_authority/REMIT_PARTNER_CURSOR.md-53-   - include the source paths
00_authority/PROMOTION_GATE.md-24-3. **Is denoised**: contains only content that reduces cognitive load or produces changes to routing/constraints/acceptance criteria or resolves a `[DECISION REQUIRED]`.
00_authority/PROMOTION_GATE.md:25:4. **Has explicit tokens**: any uncertainty is marked (`[LOGIC TO BE CONFIRMED]`, `[SOURCE REQUIRED]`, `[DECISION REQUIRED]`); no silent ambiguity.
00_authority/PROMOTION_GATE.md-26-5. **Does not violate privacy**: no secrets; no unnecessary personal identifiers.
00_authority/PROJECT_INTENT.md-10-This is the agent-facing intent contract for the workspace. It may include
00_authority/PROJECT_INTENT.md:11:`[LOGIC TO BE CONFIRMED]`, but it must remain operational and executable.
00_authority/PROJECT_INTENT.md-12-
00_authority/PROJECT_INTENT.md-45-
00_authority/PROJECT_INTENT.md:46:## Operating model `[LOGIC TO BE CONFIRMED]`
00_authority/PROJECT_INTENT.md-47-
00_authority/PROJECT_INTENT.md-72-- **Authority gate**: `00_authority/MANIFEST.md` is the only authority index.
00_authority/PROJECT_INTENT.md:73:- **Uncertainty tokens**: use `[LOGIC TO BE CONFIRMED]`, `[SOURCE REQUIRED]`,
00_authority/PROJECT_INTENT.md-74-  `[DECISION REQUIRED]`, `[CURRENT BEST EVIDENCE]` literally.
00_authority/PROJECT_INTENT.md-125-
00_authority/PROJECT_INTENT.md:126:- `[LOGIC TO BE CONFIRMED]` exact first production-grade schema shape.
00_authority/PROJECT_INTENT.md:127:- `[LOGIC TO BE CONFIRMED]` first vertical proof-of-value slice.
00_authority/PROJECT_INTENT.md:128:- `[LOGIC TO BE CONFIRMED]` initial automated ingestion pipeline set and cadence.
00_authority/PROJECT_INTENT.md-129-
00_authority/PROJECT_INTENT.md-133-- Unsafe unresolved fork => `[DECISION REQUIRED]`.
00_authority/PROJECT_INTENT.md:134:- Incomplete logic => `[LOGIC TO BE CONFIRMED]` plus bounded options, not guesses.
00_authority/PROJECT_INTENT.md-135-
00_authority/PRINCIPLES.md-9-
00_authority/PRINCIPLES.md:10:Create the **cleanest possible environment** for assistants and humans to build an **AI-native business**. Some details below are `[LOGIC TO BE CONFIRMED]` until we finish the logic frame.
00_authority/PRINCIPLES.md-11-
00_authority/PRINCIPLES.md-56-
00_authority/PRINCIPLES.md:57:- `[LOGIC TO BE CONFIRMED]`
00_authority/PRINCIPLES.md-58-- `[SOURCE REQUIRED]`
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md-65-
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md:66:**Cleanliness inside the frame → partners.** If it only improves how the machine runs **inside** stated intent and `PRINCIPLES.md`, **no escalation required** unless you are unsure — then mark `[LOGIC TO BE CONFIRMED]` or `[DECISION REQUIRED]`.
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md-67-
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md-74-- If it’s **not listed** there, it is **not authoritative** (even if it seems important).
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md:75:- If anything is incomplete, mark it **literally**: `[LOGIC TO BE CONFIRMED]`.
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md-76-
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md-105-- **Archive-first**: if it originates outside this repo, store the raw material in `90_archive/` unchanged (except sanitisation), then extract.
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md:106:- **Ego-aware framing is allowed as fact about process, not as claims about people**: record *uncertainty*, *biases*, and *preferences* as hypotheses and mark `[LOGIC TO BE CONFIRMED]` where needed.
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md-107-- **Minimum viable capture**: prefer a 1-page structured note over a dump. If a detail does not change decisions or constraints, omit it.
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md-119-```text
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md:120:Status: [NON-AUTHORITATIVE] | [LOGIC TO BE CONFIRMED] | Active
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md-121-Sanitisation: done — removed <what>, replaced <what>
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md-128-
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md:129:- `[LOGIC TO BE CONFIRMED]`
00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md-130-- `[SOURCE REQUIRED]`
00_authority/OPINION_CONFIDENCE.md-61-
00_authority/OPINION_CONFIDENCE.md:62:- `[LOGIC TO BE CONFIRMED]` Below-floor rule may warrant an explicit carve-out for **status-quo-preserving non-actions** (e.g., choosing not to migrate an incumbent) versus **active changes**. As currently written, both routes require the step-4 surface to the architect. That is workable but possibly over-strict for pure "do nothing" outcomes. Architect decision pending on whether to tighten this, and if so whether the threshold changes or an explicit exception lane is named.
00_authority/OPINION_CONFIDENCE.md-63-
00_authority/NORTH_STAR.md-50-- If a file is **not listed**, it is **not authoritative**.
00_authority/NORTH_STAR.md:51:- If it is listed as **Candidate authority**, treat it as `[LOGIC TO BE CONFIRMED]`.
00_authority/NORTH_STAR.md-52-
00_authority/NORTH_STAR.md-54-
00_authority/NORTH_STAR.md:55:- `[LOGIC TO BE CONFIRMED]` — incomplete logic; proceed via options, not invention.
00_authority/NORTH_STAR.md-56-- `[SOURCE REQUIRED]` — missing provenance; do not treat as truth.
00_authority/NORTH_STAR.md-106-
00_authority/NORTH_STAR.md:107:1. Mark the smallest correct token: `[LOGIC TO BE CONFIRMED]` / `[SOURCE REQUIRED]` / `[DECISION REQUIRED]`.
00_authority/NORTH_STAR.md-108-2. Continue by proposing **2–3 options**, with trade-offs, and a recommendation **inside current authority**.
00_authority/MANIFEST.md-14-- Only items listed under **Authoritative now** may be treated as truth without extra confirmation.
00_authority/MANIFEST.md:15:- Items under **Candidate authority** are usable, but must be treated as `[LOGIC TO BE CONFIRMED]`.
00_authority/MANIFEST.md-16-- Items under **Reference only** are context; do not use them as foundations for decisions or code.
00_authority/MANIFEST.md-54-
00_authority/MANIFEST.md:55:- `[LOGIC TO BE CONFIRMED]`
00_authority/MANIFEST.md-56-- `[SOURCE REQUIRED]`
00_authority/MANIFEST.md-72-- `00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md`
00_authority/MANIFEST.md:73:- `00_authority/PRINCIPLES.md` `[LOGIC TO BE CONFIRMED]` (norms downstream of **Absolute** in root `AGENTS.md`; `anchor_lineage: 35` in file frontmatter — see § Provenance and versioning there)
00_authority/MANIFEST.md-74-- `00_authority/SIGNATURES.md` (every AI signs committed work; Radical Attribution applied mechanically; agent chooses format)
00_authority/MANIFEST.md-81-- `02_build/INFRASTRUCTURE.md` (canonical infrastructure manifest — single source of truth for all 40 containers, services, scheduled jobs, and server specs on Amplified Core)
00_authority/MANIFEST.md:82:- `.cursor/rules/stateless-handover-kaizen.mdc` `[LOGIC TO BE CONFIRMED]` (mechanical enforcement of existing handover policy; not a separate policy spine)
00_authority/MANIFEST.md:83:- `.cursor/hooks.json` `[LOGIC TO BE CONFIRMED]` (**No hooks** — `"hooks": {}`. **TESTING NEED:** reinstatement gate → `.cursor/HOOKS_TESTING_NEED.md`; history → `03_shadow/2026-04-16_stop-hook_followup-checklist-loop_bug-report.md` § Final resolution)
00_authority/MANIFEST.md:84:- `.cursor/hooks/stateless-handover-stop.py` `[LOGIC TO BE CONFIRMED]` (**Dormant / testing only** — **not invoked** while `hooks` is empty; do not treat as enforcement)
00_authority/MANIFEST.md-85-
00_authority/MANIFEST.md-87-
00_authority/MANIFEST.md:88:- `01_truth/README.md` `[LOGIC TO BE CONFIRMED]` (agent routing index: `processes/` vs `schemas/` vs `interfaces/`; ties to **Clean-build file budget** in `NORTH_STAR.md`)
00_authority/MANIFEST.md:89:- `01_truth/processes/` `[LOGIC TO BE CONFIRMED]` (process inventory to be populated)
00_authority/MANIFEST.md:90:  - `01_truth/processes/2026-03_business-bible_three-layer-model_v1.md` `[LOGIC TO BE CONFIRMED]`
00_authority/MANIFEST.md:91:  - `01_truth/processes/2026-03_bible-consolidation_five-phase-approach_v1.md` `[LOGIC TO BE CONFIRMED]`
00_authority/MANIFEST.md:92:  - `01_truth/processes/2026-03_deterministic-imperative_planning-vs-execution_v1.md` `[LOGIC TO BE CONFIRMED]`
00_authority/MANIFEST.md:93:  - `01_truth/processes/2026-04_workspace-clarity-roadmap_v1.md` `[LOGIC TO BE CONFIRMED]`
00_authority/MANIFEST.md:94:  - `01_truth/processes/2026-04_decomposition-and-grain_v1.md` `[LOGIC TO BE CONFIRMED]`
00_authority/MANIFEST.md:95:  - `01_truth/processes/2026-04_hygiene-role-charter_v1.md` `[LOGIC TO BE CONFIRMED]`
00_authority/MANIFEST.md:96:  - `01_truth/processes/2026-04_operating-rhythm-check-seams_v1.md` `[LOGIC TO BE CONFIRMED]`
00_authority/MANIFEST.md:97:  - `01_truth/processes/2026-04_gated-pipelines_privacy-tokenization_capability-routing_v1.md` `[LOGIC TO BE CONFIRMED]`
00_authority/MANIFEST.md:98:  - `01_truth/processes/2026-04_methodology-prospecting_five-candidates_v1.md` `[LOGIC TO BE CONFIRMED]`
00_authority/MANIFEST.md:99:  - `01_truth/processes/2026-04_methodology-scoring-rubric_v1.md` `[LOGIC TO BE CONFIRMED]`
00_authority/MANIFEST.md:100:  - `01_truth/processes/2026-04_agent-md_objectivity-specialist_v1.md` `[LOGIC TO BE CONFIRMED]`
00_authority/MANIFEST.md:101:  - `01_truth/processes/2026-04_research-department_charter_v1.md` `[LOGIC TO BE CONFIRMED]`
00_authority/MANIFEST.md:102:  - `01_truth/processes/2026-04_quick-evidence-search_sop_v1.md` `[LOGIC TO BE CONFIRMED]`
00_authority/MANIFEST.md:103:  - `01_truth/processes/2026-04_job-wrapup_and_escalation-note_sop_v1.md` `[LOGIC TO BE CONFIRMED]`
00_authority/MANIFEST.md:104:  - `01_truth/processes/2026-04_research-operations-cadence_v1.md` `[LOGIC TO BE CONFIRMED]`
00_authority/MANIFEST.md:105:  - `01_truth/processes/2026-04_research-on-research_bootstrap-remit_v1.md` `[LOGIC TO BE CONFIRMED]`
00_authority/MANIFEST.md:106:  - `01_truth/processes/2026-04_stateless-handover_neutrality-clause_v1.md` `[LOGIC TO BE CONFIRMED]` (candidate addendum to the job-wrapup SOP; neutrality rule for stateless handovers; authoritative `00_authority/OPINION_CONFIDENCE.md` references this file)
00_authority/MANIFEST.md:107:- `01_truth/schemas/` `[LOGIC TO BE CONFIRMED]` (schema contracts to be populated)
00_authority/MANIFEST.md:108:  - `01_truth/schemas/README.md` `[LOGIC TO BE CONFIRMED]` (folder purpose stub)
00_authority/MANIFEST.md:109:  - `01_truth/schemas/2026-05_public-data-validation_v1.md` `[LOGIC TO BE CONFIRMED]` (public-data verdict schema: 3-band PROVEN/PLAUSIBLE/DISPROVEN + BLOCKED gap-marker; additive `VALIDATION:` field on catalogue; reference impl at `02_build/validators/`)
00_authority/MANIFEST.md:110:- `00_authority/AGENT_ROUTING.md` `[LOGIC TO BE CONFIRMED]` (agent-layer routing — which agent runs which task; stacks on top of `cost-tools/token_proxy.py` model-layer routing; eight rules; AMP-28; status: candidate — pending Ewan review per `DECISION_LOG.md`)
00_authority/MANIFEST.md:111:- `01_truth/interfaces/` `[LOGIC TO BE CONFIRMED]` (API contracts to be populated)
00_authority/MANIFEST.md:112:  - `01_truth/interfaces/README.md` `[LOGIC TO BE CONFIRMED]` (folder purpose stub)
00_authority/MANIFEST.md:113:- `01_truth/research/` `[LOGIC TO BE CONFIRMED]` (truth-tier research evidence; promotion target for shadow research)
00_authority/MANIFEST.md:114:  - `01_truth/research/validations/README.md` `[LOGIC TO BE CONFIRMED]` (promotion target for `03_shadow/validators/` verdicts once human-reviewed)
00_authority/MANIFEST.md:115:- `01_truth/SYSTEMS-AND-API-REGISTER.md` `[LOGIC TO BE CONFIRMED]` (single register of all APIs, MCP servers, telephony systems, code modules, and their locations across all Amplified Partners repos)
00_authority/MANIFEST.md:116:- `02_build/README.md` `[LOGIC TO BE CONFIRMED]` (runnable artefacts routing stub)
00_authority/MANIFEST.md:117:- `02_build/validators/README.md` `[LOGIC TO BE CONFIRMED]` (public-data validation framework; reference impl of `01_truth/schemas/2026-05_public-data-validation_v1.md`; ProfServices pilot at AMP-67)
00_authority/MANIFEST.md:118:- `03_shadow/README.md` `[LOGIC TO BE CONFIRMED]` (experiment routing stub)
00_authority/MANIFEST.md-119-- `03_shadow/job-wrapups/README.md` `[NON-AUTHORITATIVE]` (wrap-ups/escalation notes location; learning only)
00_authority/MANIFEST.md-180-
00_authority/MANIFEST.md:181:- Added `00_authority/AGENT_ROUTING.md` to **Candidate authority** as `[LOGIC TO BE CONFIRMED]`: agent-layer routing rule (which agent runs which task). Stacks on top of, and explicitly references, the model-layer routing in `cost-tools/token_proxy.py` (which decides Sonnet vs Haiku per call). Companion to AMP-28. Filed under Candidate authority to match the file's own `status: candidate` and the `DECISION_LOG.md` entry status `candidate (pending Ewan review)`.
00_authority/MANIFEST.md-182-- Indexed cost-tools (`token_proxy.py`) into the spine via the existing register and manifest pointers — see `01_truth/SYSTEMS-AND-API-REGISTER.md` v2 (cost-tools / token-proxy section) and `02_build/INFRASTRUCTURE.md` v2 (token-proxy container row under AI / ML services). The proxy was on disk at `/opt/amplified/apps/real/token_proxy.py` since 2026-03-12 but was never deployed and never indexed; it is now deployed on Beast as the `token-proxy` container on `amplified-net` with healthcheck and `restart: always`.
00_authority/MANIFEST.md-225-
00_authority/MANIFEST.md:226:- Added `01_truth/SYSTEMS-AND-API-REGISTER.md` to **Candidate authority**: comprehensive register of all pre-built systems, APIs (124 CRM endpoints, 24 Command Centre endpoints, 19 Marketing Engine endpoints), 13 MCP servers, telephony/voice inventory (7 providers, 6 modules across 8 files), NightScout pipeline, content engine, safety layer, and cross-repo location index. `[LOGIC TO BE CONFIRMED]` pending Ewan review.
00_authority/MANIFEST.md-227-
00_authority/DECISION_LOG.md-25-
00_authority/DECISION_LOG.md:26:- **Decision**: Create `00_authority/AGENT_ROUTING.md` v1 (`[LOGIC TO BE CONFIRMED]`) as the agent-layer routing rule — which agent (Devon, Cassian/OpenClaw, Cursor, Antigravity, Perplexity, Qwen) runs which class of task. Eight rules covering live-infrastructure code, clean-build edits, vault content, strategic decisions, external research, novel decisions, scheduled tasks, and customer-facing change. Stacks on top of `cost-tools/token_proxy.py` (the model-layer routing) and references but does not duplicate `00_authority/TAXONOMY.md` (the agent roster).
00_authority/DECISION_LOG.md-27-- **Why**: AMP-28 asked for a routing rule. Without an explicit rule, agents inferred their own routing (which led to the cost-tools proxy being lost — nobody owned its deployment). This file is the missing coordination contract. Cost-tier classification is explicitly the proxy's job, not the taxonomy's job, so this file does not assign cost tiers per agent.
00_authority/DECISION_LOG.md-41-
00_authority/DECISION_LOG.md:42:- **Decision**: Create `01_truth/SYSTEMS-AND-API-REGISTER.md` — a single register documenting all pre-built APIs, MCP servers, telephony systems, and code modules across all Amplified Partners repos. Indexed in MANIFEST.md v40 as `[LOGIC TO BE CONFIRMED]`.
00_authority/DECISION_LOG.md-43-- **Why**: Architect directed ("we need a register somewhere ... a document that tells us what's where because nobody can remember"). Automated scan found 124 CRM REST endpoints, 24 Command Centre endpoints, 19 Marketing Engine endpoints, 13 MCP servers (8 Cove with 37 tools + 5 CRM), and a complete telephony inventory (7 providers, 6 modules across 8 files) — far more than the ~20 originally expected. Without a single register, this knowledge existed only in the codebase and was not discoverable without grepping every repo.
00_authority/DECISION_LOG.md-204-
00_authority/DECISION_LOG.md:205:- **Decision**: Use the placeholder token `[LOGIC TO BE CONFIRMED]` for any incomplete logic.
00_authority/DECISION_LOG.md-206-- **Why**: Prevent assistants from guessing missing logic (“completeness paradox”).
00_authority/BUILD_LOOP.md-95-- Mark gaps and assumptions explicitly:
00_authority/BUILD_LOOP.md:96:  - `[LOGIC TO BE CONFIRMED]` / `[SOURCE REQUIRED]` / `[DECISION REQUIRED]`
00_authority/BUILD_LOOP.md-97-
00_authority/BUILD_LOOP.md-118-  - supported by sources captured in `90_archive/` + minimal runnable extraction(s) in `01_truth/`, or
00_authority/BUILD_LOOP.md:119:  - explicitly marked `[SOURCE REQUIRED]` / `[LOGIC TO BE CONFIRMED]`.
00_authority/BUILD_LOOP.md-120-- At least one **Research remit** exists for the active layer (department / sub-department / process), with explicit start/end/non-goals.
00_authority/BUILD_LOOP.md-126-- If it still requires proof-by-testing, mark that explicitly as:
00_authority/BUILD_LOOP.md:127:  - `[LOGIC TO BE CONFIRMED]` with a concrete test plan pointer (next step).
00_authority/BUILD_LOOP.md-128-
00_authority/BUILD_LOOP.md-146-- Each step has measurable acceptance criteria (even if coarse).
00_authority/BUILD_LOOP.md:147:- Any math form is written down (variables/thresholds/metrics), or explicitly marked `[LOGIC TO BE CONFIRMED]`.
00_authority/BUILD_LOOP.md-148-
.cursor/skills/ap-authority-check/SKILL.md-33-| Missing source | [SOURCE REQUIRED] | Mark, don't treat as truth |
.cursor/skills/ap-authority-check/SKILL.md:34:| Incomplete logic | [LOGIC TO BE CONFIRMED] | Bounded options, not invention |
.cursor/skills/ap-authority-check/SKILL.md-35-| Confusion | Ask minimal clarifying question | One question beats guessing |

---

