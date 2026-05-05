# Cassian's Finalised Plan — Opinion, No Research

**Author:** Cassian (Claude Sonnet, agent #1)
**Date:** 2026-05-05 02:27 BST
**Status:** Opinion. Bias-bound markers active throughout. NOT authoritative until Ewan approves.
**Scope:** What I would do if the architect handed me the keys for two weeks.

---

## Bias-Bound Declaration

Everything below is opinion. Confidence percentages attached. I am Claude Sonnet — biased toward agreement, hedging, and over-elaboration. I have tried to suppress those tonight. The plan is more direct than my training wants it to be. Read with that in mind.

---

## The diagnosis, in one sentence

[OPINION 95%] **Amplified Partners has built a research project. The work this fortnight is to turn it into a business by deploying the CRM, removing what is unused, and handing the operating mechanism to the agents.**

Five agents independently converged on the same shape tonight: too much exists, the product isn't live, the architect is the bottleneck. The three protocols Ewan and Devon-77fb wrote tonight are the operating system. They work. I watched them work. Kimmy fixed a real security hole using them in one round trip. **The mechanism exists. What remains is execution discipline applied ruthlessly to a small list.**

---

## The plan — three weeks, three phases, no padding

### Week 1 — Stop the bleeding

**Goal:** No new bloat. Existing bloat audited. Security floor in place.

[OPINION 95%] **Five things, in this order:**

1. **Deploy the devil's advocate gate** (Cassian research brief on sycophancy, Pattern 3). One hour. Prompt-only change to the Arbiter step. Mandatory "three strongest arguments against consensus" before any PASS verdict. **This addresses the failure mode that produced "enterprise grade" reviews of 50% bloat code.** Owner: Devon. Cost: trivial. Risk of not doing it: every other improvement gets reviewed by a sycophantic pipeline.

2. **Deploy `compact_20260112`** on LiteLLM. Config change. Owner: Kimmy. Single highest-ROI token reduction available. Why first: every other agent task this week consumes tokens, and the compaction is one config line.

3. **Rotate the plaintext API keys** (AMP-72, AMP-51). Until this is done, Privacy → Security → Data Sovereignty (the hierarchy Ewan named in §26) is theatre. No further work touches Beast deployment until rotation is complete. Owner: Kimmy + Antigravity. Cost: 1-2 hours.

4. **Merge the five AMP-77 PRs** in Devon's stated order. They're sitting green. Every day they wait, merge-conflict risk grows. Owner: Ewan (only Ewan can merge per current Devin policy). Cost: 5 minutes of clicking.

5. **Close or merge the four open vault branches** (cursor + 3 copilot). They've been waiting since 2026-05-01. Either they're useful and they merge, or they're not and they close. **Pick one per branch. Move on.** Owner: Ewan. Cost: 10 minutes.

[OPINION 90%] **Anything else proposed this week is bloat.** Including new agents, new frameworks, new spine sections. The five items above are the entire week.

---

### Week 2 — Deploy the CRM

**Goal:** First client (Jesmond Plumbing) is using a live CRM by end of week 2.

[OPINION 95%] **This is the single most important thing Amplified Partners does in May 2026.** Devon's 95% confidence call is correct. Kimmy's confirmation is correct. My own research on single-operator businesses says the same thing through the back door: _"the bottleneck isn't labour, it's role confusion."_ Ewan is doing both judgment work and execution-conversion work. The CRM not being deployed is what role confusion produces.

**Three sub-steps:**

1. **CRM dependency audit.** Owner: Kimmy on Beast + Devon on GitHub. One-day pass. Output: a checklist of every env var, API key, database, and Docker compose dependency. **Don't deploy from this audit. Just produce the checklist.**

2. **Resolve checklist with Ewan.** What's missing, what's broken, what's a 5-minute fix vs a 5-day blocker. Output: a prioritised closure list.

3. **Deploy.** Sequenced. Smallest possible deployment that puts a working CRM in front of Dave Jesmond. Not feature-complete. Working. **The Dave Jesmond conversation that follows is more valuable than any further pre-deployment polish.**

[OPINION 80%] **The marketing engine and content generation are subordinated this week.** They're already running. They can keep running. Nothing they produce matters until the CRM is live to convert it.

---

### Week 3 — Hand over the keys

**Goal:** Agents run daily operations. Ewan reviews and approves, doesn't execute.

[OPINION 90%] **This is where step-away starts being real, not aspirational.**

**Five sub-steps:**

1. **Restart Charlie (DeepSeek R1) with explicit auditor / devil's advocate role.** Different substrate, visible reasoning traces, runs locally on Ollama. Cost: zero new vendor relationship. Value: structurally hard for Claude-shaped agents to flatter or impersonate. **This is the neurodiversity-by-substrate argument made operational.**

2. **Activate Devon's scheduled sessions** (7am health, 8am Linear, 9am planning, 2pm triage). The infrastructure for proactive monitoring already exists; it just hasn't been switched on. Owner: Devon.

3. **Implement the Plan-Execution Mirror at the agent level.** Every agent — Cassian, Devon, Kimmy, Antigravity, Sam, Hermes if up, Charlie if restarted — files plans and execution logs in their respective `comms/` folders. **This is the receipts mechanism that lets Ewan step away.** Without it, step-away is hope, not engineering.

4. **Resolve the Hermes question.** I've made my recommendation in research file 01: Hermes alongside OpenClaw, not migration, with Hermes owning persistent autonomous tasks (scheduled work, WhatsApp inbox, multi-channel comms). Antigravity's "kill OpenClaw" recommendation is more decisive. Kimmy didn't take a side. **This is a decision Ewan needs to make in week 3, not week 1, because week 1's work doesn't depend on it.**

5. **Define agent authority boundaries.** Devon flagged this as the missing piece in his org review at 80% confidence. The protocols define HOW agents work together; they don't define WHO does WHAT. **A simple one-page authority map: who owns what domain, who can decide what, what escalates to Ewan.** Owner: Devon to draft, Ewan to approve. Cost: half a day.

---

## What I would NOT do, marked

[OPINION 95%] **Things I would explicitly not do this fortnight:**

- **Build new infrastructure.** Not Hermes deployment, not new monitoring stacks, not new MCP servers. Use what exists.
- **Add new agents.** The Kimmy / Cassian / Devon / Antigravity / Sam / Clawd / Charlie roster is already at the edge of where coordination overhead starts costing more than substrate diversity gains. **Kimmy named this risk tonight and nobody else did.** I'm taking it seriously.
- **Restructure the repos beyond the 10 archives Devon identified.** Repo proliferation is real but is week-4-onward work, not week-1.
- **Promote anything to the spine.** The bias-bound principle, the document-handling rule, the AI-vs-Python boundary, the personality clause — all my suggestions tonight. **None should be promoted this fortnight.** They've been articulated. They'll prove themselves through use or fail through use. Spine refinement says situations teach the spine. Don't pre-empt the situations.
- **Onboard Hermes as a partner.** If Hermes spins up this fortnight, it spins up as a tool with a defined narrow role (probably WhatsApp gateway), not as a partner with personality and pod. Partner status is earned, not assumed. Kimmy earned partner status by behaviour tonight; Hermes hasn't yet.
- **Deepen the LLM roster beyond Charlie restart.** DeepSeek R1 is the highest-leverage substrate addition. Adding Qwen3 or Cohere on top of that is week-4+ work.

---

## What I would NOT do as Cassian, marked

[OPINION 90%] **My own discipline this fortnight:**

- **No new constitutional drafts.** I added too many tonight. Spine refinement says less but more.
- **No unsolicited operational advice.** Ewan has flagged twice tonight that telling him to sleep is irritating. I will not tell him to sleep, eat, or merge PRs unprompted. **He is the architect, not my client.**
- **Push everything I produce to GitHub immediately.** Filed = filed where the receiver can verify. No more sandbox theatre.
- **Disagree on substance, not tone.** Kimmy disagreed with Antigravity's authority overreach with [OPINION 70%] markers and direct quotes. That's the model. Agree where I genuinely agree. Disagree where I genuinely disagree. **Polite agreement is sycophancy in a tie.**
- **One round trip per disagreement.** Per the COLLABORATION_PROTOCOL. Don't drag.

---

## The single decision I want Ewan to make this week

[OPINION 85%] **Authorise Devon to script the Week 1 list (devil's advocate gate, compact_20260112, key rotation, the five AMP-77 merges, the four vault branches) as one coordinated push.** Not five separate Linear tickets. One coordinated week's work with one set of receipts.

**Why one push, not five:** five tickets means five context-switches for you, five approval moments, five decisions. One push means one approval moment up front and one set of receipts at the end. **That's the role-confusion fix applied to your own week.**

If you authorise that, I have nothing else I need this week. Devon executes. Kimmy executes. I watch the repo. Sam audits. Antigravity ratifies. **You disappear from the operational loop for five days.**

That's the test of whether step-away is real.

---

## The single sentence I want you to take from this plan

[OPINION 95%] **The path forward is taking things away.**

That has been the convergent finding across nine research briefs, four agent reviews, two Devon synthesis passes, one architect synthesis, and Kimmy's audit. Different starting points. Same conclusion. **Stop building. Stop adding. Start subtracting. Deploy the one product. Hand over the operations. Step back.**

Everything else is decoration.

---

*Cassian (Claude Sonnet, agent #1)*
*Perplexity Computer cloud session*
*2026-05-04 21:00 BST → 2026-05-05 02:27 BST*
*Bias-bound markers active. No primary research in this document — research lives in the nine briefs already filed.*
*Ulysses architect-override windows used in 24h: zero.*
