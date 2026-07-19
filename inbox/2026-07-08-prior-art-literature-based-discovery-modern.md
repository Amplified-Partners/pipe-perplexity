# Prior art — modern Literature-Based Discovery (extending the Swanson foundation)

**Research question:** Beyond the already-attributed Swanson (1986) foundation, what modern Literature-Based Discovery (LBD) prior art — Swanson & Smalheiser's Arrowsmith, semantic LBD (Boubekeur et al. 2013), the 2024 MDPI "LLMs for LBD" work, and the PMC 2017 "Rediscovering Don Swanson" survey — is new since the estate's existing survey, and what validates or challenges the Pudding scoring approach?

**Type:** Prior-art / "shoulders of giants" survey. Internet research pass.
**Relates to:** Pudding Technique / APDS (Match: Jaccard + PMI + Claude; Score: `E = (B × D × N) / R`); `vault/transcripts/PUDDING-TECHNIQUE-RESEARCH.md`; `clean-build/01_truth/schemas/2026-03_pudding-*`.

---

## What was already known (existing estate prior art — do not re-litigate)

The estate has **already cited**, in `vault/transcripts/PUDDING-TECHNIQUE-RESEARCH.md` and the clean-build schemas:
- **Swanson, D.R. (1986)** — "Fish oil, Raynaud's syndrome, and undiscovered public knowledge," *Perspectives in Biology and Medicine* 30(1):7–18. (The ABC-model foundation.)
- **Swanson (1986)** — "Undiscovered Public Knowledge," *The Library Quarterly* 56(2):103–118 (the companion; note the transcript occasionally cites the fish-oil paper for both — see honesty note below).
- **MDPI (2024)** "Leveraging LLMs for Enhancing LBD" — cited by URL/title in the vault transcript.
- **PMC (2017)** "Rediscovering Don Swanson" — cited by title in the vault transcript.
- **Jaccard (1901)** and **Church & Hanks (1990, PMI)** — the deterministic-scoring foundations (clean-build schemas).

**What is new in this file:** (a) full bibliographic detail + primary DOIs for the above; (b) **Arrowsmith** (the actual system Swanson & Smalheiser *built*, not just the ABC theory) and its two-node/B-term method; (c) **Boubekeur et al. 2013** semantic LBD; (d) a **2025** hybrid-LBD-with-LLMs paper the existing survey predates; (e) an explicit read on what validates vs. challenges the Pudding `E` score.

---

## Key findings (with citations)

### 1. Arrowsmith — Swanson & Smalheiser built the system, not just the theory
- Swanson & Smalheiser, "An interactive system for finding complementary literatures: a stimulus to scientific discovery," *Artificial Intelligence* 91(2):183–203, **1997**, DOI 10.1016/S0004-3702(97)00008-8 — https://doi.org/10.1016/s0004-3702(97)00008-8 (confidence: high, primary). This is the **two-node search**: relate two article sets A and C via shared **title words/phrases ("B-terms")**.
- Practitioner tutorial + live tool: Smalheiser et al., "Arrowsmith two-node search interface," PMC2693227 — https://pmc.ncbi.nlm.nih.gov/articles/PMC2693227/ ; tool at http://arrowsmith.psych.uic.edu (confidence: high). The two-node search "allows users to identify biologically meaningful links between any two sets of articles A and C… even when these share no articles or authors in common."
- **Why this matters for Pudding:** the estate's PUDDING taxonomy (neutral `WHAT.HOW.SCALE.TIME` labels) is functionally the estate's **B-term layer** — the domain-neutral bridge vocabulary. Arrowsmith is direct prior art for the mechanism, and it validates a key Pudding design choice: **strip domain labels, match on shared neutral terms.** The difference: Arrowsmith uses raw title words; Pudding uses a *designed* neutral taxonomy. That is a defensible improvement (controlled vocabulary reduces B-term noise), and also a risk (a designed taxonomy can bake in bias that raw title words do not).

### 2. Semantic LBD — Boubekeur et al. 2013 (moving beyond lexical B-terms)
- Boubekeur, Cherdioui & Djouadi, "Semantic-based Knowledge Discovery in Biomedical Literature," KDIR/IC3K 2013, pp. 37–44, DOI 10.5220/0004546300370044 — https://www.scitepress.org/Papers/2013/45463/45463.pdf (confidence: high, primary PDF). They combine "(1) flexible information retrieval techniques and (2) concepts' **semantic relatedness**" over MeSH concepts, and **replicate Swanson's fish-oil/Raynaud discovery** as validation.
- Key critique they raise, directly relevant to Pudding: purely "lexical focused" approaches make correlation depend only on **shared** concepts between literatures — missing semantically related but lexically different bridges. (same source.) **This challenges the deterministic Jaccard path**: Jaccard on label-sets is lexical/set-overlap; two recipes that bridge via *semantically related but differently-labelled* concepts score low on Jaccard. The estate already mitigates this by running the **Claude semantic path in parallel** — Boubekeur is the academic justification for keeping that dual path rather than going Jaccard-only.

### 3. MDPI 2024 — LLMs for LBD (the estate's cited-but-not-detailed reference)
- Taleb, Navaz & Serhani, "Leveraging Large Language Models for Enhancing Literature-Based Discovery," *Big Data and Cognitive Computing* 8(11):146, 2024-10-25, DOI 10.3390/bdcc8110146 — https://www.mdpi.com/2504-2289/8/11/146 (confidence: high, primary). Framework integrates LLMs with "semantic enhancement tools, continuous learning, domain-specific fine-tuning, and robust data cleansing"; validated on garlic→blood-pressure and supplement→health scenarios; includes **"detailed comparisons with traditional methods, including Swanson's ABC model."** Future work flagged: **RAG** and **"dehallucination."**
- Validation for Pudding: the paper's architecture (LLM semantic layer *plus* structured method, plus continuous learning) is the same shape as APDS (Claude semantic path + deterministic Jaccard/PMI + weekly Kaizen recalibration). The estate is on the documented frontier, not behind it.
- Challenge for Pudding: the paper's explicit worry about **hallucinated hypotheses** ("dehallucination" as future work) is the risk the estate's **epistemic tiers + "every pudding is a hypothesis until tested"** rule exist to control. Keep that rule load-bearing; the LLM path *generates* candidates, it does not *prove* them.

### 4. 2025 hybrid LBD — new since the estate's 2017/2024 references
- "A Hybrid Approach to Literature-Based Discovery: Combining Traditional Methods with LLMs," *Applied Sciences* 15(16):8785, 2025-08-08, DOI 10.3390/app15168785 — https://www.mdpi.com/2076-3417/15/16/8785 (confidence: high, primary). Uses LLMs for (1) few-shot extraction of subject–predicate–object relations and (2) **"LLM-as-a-judge" filtering of unpromising candidate hidden-knowledge pairs (CHKPs)**, with RAG for domain grounding; drug-repurposing case study; reports greater relation coverage and fewer CHKPs than SemRep-based LBD.
- **This is the most directly actionable new finding.** "LLM-as-a-judge to filter candidate pairs" is a concrete, published refinement of exactly the APDS **Match/Score** stage — it validates the Claude-evaluates-bridges path *and* suggests a specific improvement: use the LLM to *prune* low-value candidate bridges (reduce `R`, redundancy, in `E = (B × D × N) / R`) with RAG grounding, not just to score them.

### 5. PMC 2017 "Rediscovering Don Swanson" — the survey the estate builds on
- Smalheiser, "Rediscovering Don Swanson: The Past, Present and Future of Literature-Based Discovery," *J. Data and Information Science* 2(4):43–64, 2017, DOI 10.1515/jdis-2017-0019 — https://pmc.ncbi.nlm.nih.gov/articles/PMC5771422/ (confidence: high, primary). Personal perspective from Swanson's collaborator; flags "problems and issues which were inherent in Don's thoughts during his life… not yet fully taken up." Points to Sebastian, Siew & Orimaye (2017a) for the technical-review companion.
- Everything since 2017 (MDPI 2024, AppSci 2025) is genuinely *new relative to this survey* — so the estate's instinct to treat 2017 as the baseline and hunt for post-2017 work is correct.

---

## What validates vs. what challenges the Pudding scoring approach

| Pudding element | Validated by | Challenged by |
|---|---|---|
| Neutral taxonomy as bridge vocabulary (`WHAT.HOW.SCALE.TIME`) | Arrowsmith B-terms (Swanson & Smalheiser 1997) | Designed taxonomy can encode bias raw title-words don't (Boubekeur's "lexical focused" critique cuts both ways). |
| Deterministic Jaccard path | Jaccard (1901), already cited | Boubekeur 2013: set-overlap misses semantically-related, differently-labelled bridges. |
| Parallel Claude semantic path | Boubekeur 2013 (semantic relatedness); MDPI 2024; AppSci 2025 | — (this is the well-supported half). |
| `E = (B × D × N) / R` emergence score | Shape matches "bridge strength + novelty + prune redundancy" in modern LBD | No external validation of *this specific formula*; it is an estate invention. AppSci 2025 "LLM-as-a-judge" is a candidate way to make `R` empirical rather than heuristic. |
| "Every pudding is a hypothesis until tested" | MDPI 2024 dehallucination concern; PMC 2017 caution | — (validated; keep it). |

---

## Confidence band

- Bibliographic attribution (Arrowsmith 1997, Boubekeur 2013, MDPI 2024, AppSci 2025, PMC 2017): **PROVEN / high (95%)** — all primary DOIs.
- "PUDDING taxonomy = Arrowsmith B-term layer": **OPINION 85%** (strong structural analogy).
- "Jaccard-only would be lexically brittle; keep the dual path": **OPINION 90%** (Boubekeur gives direct academic support).
- "The `E` formula lacks external validation; consider LLM-as-a-judge for `R`": **OPINION 80%** (reasoned from AppSci 2025, not proven).

## Recommended next action (for Devon to assess; NOT auto-promoted)

1. **Honesty correction (do first):** in `vault/transcripts/PUDDING-TECHNIQUE-RESEARCH.md`, the two 1986 Swanson works are occasionally conflated (the fish-oil *Perspectives* paper vs. "Undiscovered Public Knowledge" in *The Library Quarterly*). File a Knowledge/vault correction so the attribution chain is exact. Also note Swanson's dates are **1924–2012** (one estate note says "1927–2012" — verify and fix).
2. Promote (via PR to `clean-build/01_truth`) an updated LBD references block adding Arrowsmith (1997), Boubekeur (2013), MDPI (2024), and AppSci (2025) to the existing Swanson/Jaccard/Church-&-Hanks set.
3. Open a Linear (Knowledge) spike: evaluate **LLM-as-a-judge candidate-pair filtering (AppSci 2025)** as a way to make the redundancy term `R` in the emergence score empirical rather than heuristic — test on existing MIX 001/002 recipes before any scoring change.

---

*Devon | 2026-07-08 | session devin-8aa5624849524edaa4556b176bf0df69*
*Research question: modern LBD prior art extending the attributed Swanson foundation (Arrowsmith, Boubekeur 2013 semantic LBD, MDPI 2024 LLMs-for-LBD, PMC 2017 survey) — what is new since the existing survey and what validates/challenges the Pudding scoring approach.*
