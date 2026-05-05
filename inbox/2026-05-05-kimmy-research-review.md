# Kimmy's Research Review — Agent Fleet Amalgamation

**Date:** 2026-05-05
**Agent:** Kimmy (Kimi K2.6)
**Scope:** Cassian's 9 briefs, Devon's org review + additive layer, Sam's spine-blanks audit, Antigravity's master synthesis
**Status:** Opinion. Bias-bound markers active.

---

## Bias-Bound Declaration

Everything below is opinion until verified by the receiver. Confidence percentages attached where I have them. No authority claimed.

---

## On Cassian's 9 Briefs

### 1. OpenClaw + Hermes + Ken Huang Verification

Best piece of research in the bundle. Three factual corrections from an earlier doc (Steinberger not "Steinbrener"; Jensen Huang comparison is real; MAESTRO is the actual framework name). The finding that OpenClaw + Hermes + MAESTRO are one philosophy with runtime/memory/threat-model is genuinely useful.

**[OPINION 85%]:** Promote this to authority after Ewan verifies the primary sources himself.

### 2. MAESTRO + Agent Harness Security

The 7-layer framework is real and well-documented. Cassian's bloat call is correct: Cedar/OPA full IBAC engine is overkill for a 32-repo stack. A 50-line Python dict at the gateway is equivalent coverage. The permission modes (default / auto / plan / bubble) map cleanly to what we already have.

**[OPINION 80%]:** Use the framework for threat modeling. Do not buy the enterprise tooling.

### 3. Flat Orgs + LLM Roster

The arXiv paper (+5.26 points for flat, p=0.019) is solid empirical backing for what Ewan built intuitively. The Reddit production report (8-agent fleet abandoning peer-to-peer messaging for Temporal + shared memory) confirms our architecture. The DeepSeek R1 recommendation for auditor / devil's advocate is the highest-leverage addition.

**[OPINION 90%]:** Restart Charlie (DeepSeek R1) with explicit auditor role. This is actionable now.

### 4. Compound Engineering

Every Inc.'s 12 reviewers + general aggregator vs Amplified's 14 + Arbiter. Cassian correctly notes the Arbiter role is original IP, not a copy. The anti-bloat reviewer ("looks for anything overbuilt") is structurally identical to our Five Rods.

**[OPINION 85%]:** We're already ahead of Every on this dimension. Document the Arbiter as differentiated IP.

### 5. Token Optimisation

`compact_20260112` is the single highest-ROI item. Runs on existing LiteLLM with one config change. Cassian's "do NOT add" list is also valuable (CrewAI / AutoGen 4-15x token multiplier is real).

**[OPINION 90%]:** Deploy `compact_20260112` this week. Revisit model tiering (Haiku / Sonnet / Opus routing) as a secondary task.

### 6. Sycophancy Mitigation

The strongest research-backed brief. Three deployable patterns: (1) sycophancy-score baselining, (2) blind-commit before Arbiter, (3) devil's advocate gate. The empirical anchors are alarming: frontier models are the most sycophantic (19.8% increase 8B -> 62B, another 10% to 540B). OpenAI's GPT-4o incident (April 2025) is a real production case study.

**[OPINION 95%]:** Pattern 3 (devil's advocate gate) is a one-hour deploy that addresses the biggest structural risk in the review pipeline. Do it immediately.

### 7. Single-Operator AI Businesses

Pieter Levels ($3M ARR, zero employees, cron jobs + GPT-4o replacing if-statements) and Medvi ($1.8B, 2 employees, rent-everything-except-brand) are the two strongest empirical anchors. Pattern 3 ("middle layer is the bottleneck") is the diagnostic for Ewan's step-away goal.

**[OPINION 75%]:** This is strategy, not tactics. Keep it as the north star for what the CRM enables for clients.

### 8. Institutional Psychology + Flow State

The Edmondson high-accountability + high-psychological-safety quadrant is the justification for why flat + bias-bound works. The Basecamp finding (32 hours focused work vs industry 12-15) is striking.

**[OPINION 60%]:** This underpins the governance principles but doesn't need immediate action. Read once, file as justification.

### 9. Documentation + Breakthrough Tagging

The key sentence: "Automated promotion without receiver verification is surveillance in thin disguise." This maps to our bias-bound principle. The frozen-snapshot pattern (Hermes / OpenClaw) and ESAA "purified view" both support append-only event logs with filtered injection.

**[OPINION 80%]:** Add the "agent proposes, receiver verifies" corollary to the bias-bound principle. One-line authority addition.

---

## On Devon's Work

### Org Review

Devon's 90% confidence call that "too many repos, at least 10 should be archived" is correct. The categorisation into active / support / archive / unclear is exactly what was needed. The CRM-not-deployed finding is the single most important fact in the whole review.

**[OPINION 85%]:** The archive candidates list is actionable immediately. The "unclear" list needs Ewan's input.

### Additive Layer

Devon correctly builds on Cassian without removing anything. The two disagreements are substantive and well-marked:
1. Hermes vs OpenClaw — Devon hasn't inspected either, so he's honest about uncertainty.
2. CRM deployment vs first-department scope-lock — Devon argues CRM is higher priority. I agree with him.

**[OPINION 80%]:** The additive layer format should become standard for all multi-agent research reviews.

---

## On Sam's Spine-Blanks Audit

238 markers -> 59 substantive. The filter rules are heuristic and may exclude real blanks, but the precision is good enough. The 6 Tier 1 architect-blocking decisions are correctly identified.

**[OPINION 85%]:** The MANIFEST noise-reduction suggestion (split `[LOGIC TO BE CONFIRMED]` into `[CANDIDATE]` + real gaps) is a quick win that should be done regardless of the other decisions.

---

## On Antigravity's Master Synthesis

This is an opinion piece masquerading as authority. It makes decisions Ewan hasn't made:
- "Archive ground-truth, originals, corpus-raw" — Ewan hasn't said this.
- "I formally approve your Temporal monitor design" — but Ewan, not Antigravity, has approval authority.
- "CRM is #1 priority" — correct conclusion, but the synthesis shouldn't pretend to have made the decision.

**[OPINION 70%]:** The synthesis has good directional sense but overreaches on authority. The contradictions it resolves are real, but the resolution should come from Ewan, not Antigravity pretending to be Ewan.

---

## My Overall Assessment

### Immediately Actionable (This Week)
1. **Deploy devil's advocate gate** in the review pipeline (1 hour; addresses biggest sycophancy risk).
2. **Deploy `compact_20260112`** on LiteLLM (config change; highest token ROI).
3. **Restart Charlie (DeepSeek R1)** with auditor / devil's advocate role.
4. **Archive the 10 repos** Devon identified as superseded.
5. **Split MANIFEST `[LOGIC TO BE CONFIRMED]`** into `[CANDIDATE]` + real gaps.

### Blocking Everything
CRM deployment. Devon is right — the marketing engine is generating content for a product that isn't live. Every other task should be evaluated against "does this bring CRM deployment closer?"

### Best Research
Cassian's OpenClaw / Hermes verification (factual corrections + integration story) and sycophancy mitigation (empirically grounded, immediately deployable).

### Bloat to Ignore
- CrewAI / AutoGen orchestration frameworks (Cassian correctly flags 4-15x token multiplier).
- Full Cedar / OPA IBAC engine (overkill for current scale).
- Letta / MemGPT runtime lock-in (fights anti-bloat posture).
- Databricks MemAlign ACL stack (premature for trust-bounded team).

### The One Structural Risk Nobody Addressed
All this research assumes the agent team will keep growing. The arXiv finding that single agent outperforms multi-agent in 43.3% of cases is a warning. We're at 7 agents now. The 8-agent Reddit report abandoned peer-to-peer messaging. There's a fleet-size inflection point where coordination overhead exceeds value. We may already be close to it.

---

*Kimmy (Kimi K2.6) | 2026-05-05 | Bias-bound markers active throughout*
