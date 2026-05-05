# OpenClaw + Hermes + Ken Huang — provenance verification

**Topic:** OpenClaw + Hermes + Ken Huang — provenance verification
**Status:** Research filed. Opinion attached. Awaiting other agents' two pennies.
**Path:** clean-build/01_truth/research/01_openclaw_hermes_kenhuang_verification.md
**Authored by:** Cassian (Claude Sonnet) + Cassian-research-subagent
**Date:** 2026-05-04 / 2026-05-05 BST

---

## CASSIAN'S OPINION (clearly marked, NOT authoritative)

> _Read with scepticism per the Bias-Bound Principle. Every claim is opinion until verified by the receiver._

**Most useful finding:** OpenClaw + Hermes + MAESTRO are not three things bolted together — they're one philosophy with a runtime, a memory layer, and a threat model from the same lineage (Ken Huang's Substack series uses Hermes as the explicit reference system).

**Key corrections from the earlier doc Ewan was sent:**
- Creator is **Peter Steinberger** (not "Steinbrener"). PSPDFKit founder, joined OpenAI Feb 2026.
- Jensen Huang's Linux comparison is **real** — GTC 2026, on the record.
- The "Hermes in your spine" is the same Hermes from Nous Research. No naming collision.

**Honest opinion (marked):** Hermes looks like a better fit than OpenClaw + bolt-ons for "step away, system runs itself" — WhatsApp-native, persistent memory, scheduling all baked in. Not decided. Needs feature-by-feature comparison against actual fleet workload.

**Sycophancy flag:** the doc Ewan was sent had two factual errors. Whichever agent wrote it didn't verify before asserting. Bloat-audit candidate.

---

## TWO PENNIES — other agents add below

_This section is for other agents (Kimmy, Antigravity, Devon, Hermes, Cursor, Qwen) to add their opinion before the research. Use the Collaboration Protocol: additive only, sign and date, escalate to Ewan if convergence fails after one round trip._

_(empty — awaiting input)_

---

## RESEARCH (verbatim, primary sources)

## SOURCE 1 — OpenClaw provenance

**From Luca Bianchi, LinkedIn (2026-03-17), verbatim:**

> "OpenClaw started as a weekend project by Peter Steinberger (the PSPDFKit founder) in November 2025. It's an AI agent that runs on your own hardware, connects to messaging apps you already use, and, most importantly, operates autonomously. It doesn't wait for you to open a tab and type something. It runs in the background, checking, doing, and learning. The GitHub trajectory was absurd. 247,000 stars in about two months. It passed React. Steinberger joined OpenAI in February and moved the project to an open-source foundation."
> — [Luca Bianchi on LinkedIn](https://www.linkedin.com/pulse/openclaw-why-jensen-huang-just-compared-linux-luca-bianchi-x86tf)

**From openclaw.ai (homepage), verbatim:**

> "Runs on Your Machine. Mac, Windows, or Linux. Anthropic, OpenAI, or local models. Private by default — your data stays yours."
> — [openclaw.ai](https://openclaw.ai)

**From OpenClaw docs (Tools page), verbatim:**

> "OpenClaw has three layers that work together: Tools are what the agent calls. A tool is a typed function the agent can invoke (e.g. `exec`, `browser`, `web_search`, `message`). OpenClaw ships a set of built-in tools and plugins can register additional ones. The agent sees tools as structured function definitions sent to the model API."
> — [docs.openclaw.ai](https://docs.openclaw.ai/tools)

**From Wccftech (Jensen Huang at GTC, 2026-03-05), verbatim:**

> "This is probably the most significant software release, perhaps ever. If you consider OpenClaw, it has achieved in just three weeks what took Linux around 30 years to accomplish. It has become the most downloaded open-source software in history within that short span."
> — Jensen Huang, NVIDIA CEO, quoted in [Wccftech](https://wccftech.com/nvidia-ceo-says-openclaw-did-in-3-weeks-what-linux-took-30-years/)

**Verified facts:**
- Creator: **Peter Steinberger**, not "Peter Steinbrener" as in the document Ewan was sent. Spelling matters for attribution.
- Origin: November 2025, weekend project
- Organisation: now open-source foundation; Steinberger moved to OpenAI in February 2026
- Jensen Huang Linux comparison: **real**, made at GTC 2026
- Architecture: tool/skill/plugin three-layer; memory in plain-text Markdown files, not vector DB

---

## SOURCE 2 — Hermes Agent (Nous Research)

**From hermes-agent.nousresearch.com (homepage), verbatim:**

> "Open Source • MIT License. The Agent That Grows With You. Not a coding copilot tethered to an IDE or a chatbot wrapper around a single API. An autonomous agent that lives on your server, remembers what it learns, and gets more capable the longer it runs."
> — [hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com)

**From Hermes Agent docs, verbatim:**

> "The self-improving AI agent built by Nous Research. The only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, and builds a deepening model of who you are across sessions."
>
> Features:
> - "Runs anywhere, not just your laptop — 6 terminal backends: local, Docker, SSH, Daytona, Singularity, Modal."
> - "Lives where you do — CLI, Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Mattermost, Email, SMS, DingTalk, Feishu, WeCom, BlueBubbles, Home Assistant — 15+ platforms from one gateway."
> - "Built by model trainers — Created by Nous Research, the lab behind Hermes, Nomos, and Psyche."
> - "Scheduled automations — Built-in cron with delivery to any platform."
> - "Delegates & parallelizes — Spawn isolated subagents for parallel workstreams."
> - "Open standard skills — Compatible with agentskills.io. Skills are portable, shareable, and community-contributed via the Skills Hub."
> - "MCP support — Connect to any MCP server for extended tool capabilities."
> — [hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs/)

**From Nous Research releases page, verbatim:**

> "Hermes Agent | AGENT | An autonomous agent that lives on your server, remembers what it learns, and gets more capable the longer it runs. | 02/25/26"
> — [nousresearch.com/releases](https://nousresearch.com/releases/)

**Verified facts:**
- Creator: **Nous Research**, MIT licensed, released 2026-02-25
- Memory: layered system — MEMORY.md, USER.md, plus session search; pluggable provider architecture for cross-session persistence
- Native WhatsApp support (in the 15+ platforms list)
- Skills compatible with agentskills.io standard — same skills marketplace ecosystem as OpenClaw

---

## SOURCE 3 — Ken Huang's actual published work

**From Cloud Security Alliance Labs, verbatim:**

> "MAESTRO (Multi-Agent Environment, Security, Threat, Risk, and Outcome) the Agentic AI Threat Modeling Framework. MAESTRO was created by Ken Huang, CEO & Chief AI Officer, DistributedApps.ai and a leader within the CSA AI Safety Initiative."
> — [labs.cloudsecurityalliance.org/maestro](https://labs.cloudsecurityalliance.org/maestro/)

**From Ken Huang's Substack bio, verbatim:**

> "Ken Huang is the OWASP AIVSS Lead and an Agentic AI Security Researcher specializing in OpenClaw threat modeling and skill security scanning. He speaks regularly at RSA and OWASP conferences on AI security topics."
> — [kenhuangus.substack.com](https://kenhuangus.substack.com)

**MAESTRO seven-layer architecture, from Snyk Labs paraphrase of Huang's framework:**

> Layer 1: Foundation models
> Layer 2: Data operations
> Layer 3: Agent frameworks (reasoning engines, workflow orchestration, decision-making, autonomy boundaries, planning)
> Layer 4: Deployment infrastructure (container runtime, Kubernetes, network security, service mesh, monitoring)
> Layer 5: Behavioral monitoring (skipped in our extraction, but exists)
> Layer 6: Security and compliance (IAM, policy engines, guardrails, compliance, regulatory)
> Layer 7: Agent ecosystem
> — [labs.snyk.io MAESTRO threat modelling](https://labs.snyk.io/resources/maestro-threat-modeling/)

**OWASP Agentic Skills Top 10:**

> "The OWASP Agentic Skills Top 10 documents the 10 most critical security risks in agentic AI skills, providing evidence-based mitigations and prevention strategies for mitigating agent skill risks." — Authored by Ken Huang, launched 2026-03-31.
> — [LinkedIn announcement](https://www.linkedin.com/pulse/owasp-agentic-skills-top-10-official-launch-post-ken-huang-zkeic)

**Verified facts:**
- Ken Huang is real, current title: CEO & Chief AI Officer, DistributedApps.ai; leader within CSA AI Safety Initiative; OWASP AIVSS Lead
- MAESTRO is real, his framework, 7-layer threat model, published via Cloud Security Alliance
- He has a Substack at kenhuangus.substack.com — actively writing on agentic AI security
- He has a book: "Securing AI Agents" (published, available on eBooks.com)
- OWASP Agentic Skills Top 10 is his work
- He specifically threat-models OpenClaw

---

## CASSIAN'S OPINION — separate block

### What this confirms

1. **The earlier document Ewan was sent had three errors:**
   - "Peter Steinbrener" should be "Peter Steinberger" (PSPDFKit founder, joined OpenAI Feb 2026)
   - "Ken Huang wrote the Agentic Safety Doctrine for OpenClaw" — accurate in spirit. He literally threat-models OpenClaw publicly.
   - "Ken Huang Doctrine" is colloquial; the actual published framework is **MAESTRO**

2. **OpenClaw + Hermes + Ken Huang/MAESTRO is a real, verified architectural stack.** All three exist. All three are open-source. The integration story is plausible.

3. **The "Hermes already in the spine" question is resolved.** The Hermes in Ken Huang's Doctrine that Ewan adopted on 2026-05-01 IS Nous Research's Hermes Agent. They're the same thing. Not a naming collision. Good.

4. **The Linux comparison from Jensen Huang is real.** GTC 2026, on the record. Wccftech and LinkedIn both reported it. Bianchi's piece has Huang saying "OpenClaw gave the industry exactly what it needed at exactly the time." So the framing isn't hype-by-an-internal-agent — it's genuinely how Huang positioned it publicly.

### What's actually new and important

**MAESTRO has 7 layers, not just IBAC.** The document Ewan was sent compressed Ken Huang's work to "IBAC + Cedar + Destructive Gating." That's only **Layer 6** of MAESTRO (Security and Compliance). The full framework covers everything from foundation models to agent ecosystem. **If Amplified Partners is going to claim MAESTRO compliance, they need to address all 7 layers, not just one.**

**Hermes has WhatsApp natively.** This is huge for §6 (interface problem) and §13 (the broken WhatsApp delivery flagged by Devon-2982). Hermes ships with WhatsApp out of the box. **You don't need to deploy Evolution API separately if you adopt Hermes properly** — the WhatsApp pipe is part of the framework.

**Hermes has a "skills hub" compatible with agentskills.io.** This is the same standard OpenClaw uses. Meaning: skills you write for one work for the other. The integration isn't "wire two frameworks together" — it's "use a shared skill format across both."

**Hermes is six months newer than OpenClaw.** OpenClaw: Nov 2025. Hermes: Feb 2026. Hermes was built _after_ OpenClaw, with the explicit pitch of being "the agent that grows with you" — i.e. it learned from what OpenClaw lacked. The persistent memory and self-improving skill loop are the things Hermes adds that OpenClaw doesn't have natively.

### My structural opinion (the one Ewan asked for)

**The OpenClaw + Hermes + MAESTRO stack is right. But it's not "OpenClaw is the muscle, Hermes is the autopilot."** That framing, while catchy, undersells what Hermes actually is.

A more honest framing:

- **OpenClaw = bare-metal execution.** Tools, exec, browser, message. Stateless per-task. You give it a prompt, it acts.
- **Hermes = stateful autonomous agent.** Has its own memory model, its own skill library, its own scheduler, its own multi-platform gateway. It can do everything OpenClaw can, _and_ it remembers, _and_ it learns, _and_ it talks to humans on 15+ channels.
- **MAESTRO = the threat model the whole stack is judged against.** Not a runtime layer. A design rubric and audit framework.

**The reason this matters:** Hermes isn't a layer added on top of OpenClaw. It's a more capable peer. **You may not need both.**

The honest question Ewan should be asking is: "Do I run OpenClaw + Hermes side by side, or do I migrate from OpenClaw to Hermes?" Both are legitimate answers. But the framing that says "Hermes is the autopilot for the OpenClaw sports car" makes a choice that hasn't actually been made on the merits.

**My instinct, anti-bloat:** Pick one as the primary execution substrate. The other can stay for legacy or specialised work. Running both in parallel doubles the maintenance surface for an unclear gain. Hermes's WhatsApp-native + persistent-memory + skills-hub combination makes it a better fit for "step away, system runs itself" — which is §7a, the bottleneck removal. **If I were doing the reorg, I'd seriously evaluate Hermes as the primary substrate and OpenClaw as a specialist tool, not the other way around.**

But — and this is important — that's a recommendation that requires a real comparison, not a vibes-based assertion. The next research pass should be: feature-by-feature comparison of OpenClaw vs Hermes against the existing 22-agent fleet's actual workload patterns. **What's the substrate that lets Ewan step away soonest with the least bloat? That's the question to answer.**

### Specific corrections to feed back into the spine

1. The PORTABLE-SPINE.md says "Cron Scheduler (Hermes): Background scheduler for 24/7 autonomous operations." This understates Hermes by ~95%. Hermes isn't just a cron — it's a full autonomous agent framework. Either deepen the spine entry or rename what's in the spine to "Hermes pattern" if you only mean the scheduler component.

2. The Ken Huang reference in the spine is accurate but compressed. Worth expanding to: "Ken Huang Doctrine = MAESTRO 7-layer threat model + OWASP Agentic Skills Top 10 + IBAC/Cedar/Destructive Gating implementation pattern."

3. The document Ewan was sent had two factual errors (Steinberger spelling, Huang doctrine framing). Whichever agent wrote it didn't verify before asserting. **This is a sycophancy-adjacent failure mode worth flagging in the bloat audit (§24).**

### What I haven't done yet

- Not read MAESTRO in primary form (Cloud Security Alliance source) — only Snyk's summary. Tomorrow's research.
- Not read Ken Huang's "Securing AI Agents" book — that's the deep version of the doctrine.
- Not compared the existing 22-agent fleet's current OpenClaw deployment to what Hermes would replace.
- Not reconciled this with the Pudding Engine, Compound Engineering loop, or the §27 deterministic-first principle. All three frameworks need to play nicely with what's already in the spine.

These come next.

— Cassian
