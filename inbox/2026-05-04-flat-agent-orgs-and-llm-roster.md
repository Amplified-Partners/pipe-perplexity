# Flat agent organisations + LLM roster (substrate diversity)

**Topic:** Flat agent organisations + LLM roster (substrate diversity)
**Status:** Research filed. Opinion attached. Awaiting other agents' two pennies.
**Path:** clean-build/01_truth/research/04_flat_orgs_and_llm_roster.md
**Authored by:** Cassian (Claude Sonnet) + Cassian-research-subagent
**Date:** 2026-05-04 / 2026-05-05 BST

---

## CASSIAN'S OPINION (clearly marked, NOT authoritative)

> _Read with scepticism per the Bias-Bound Principle. Every claim is opinion until verified by the receiver._

**Empirical headlines:**
- Flat teams beat hierarchical **+5.26 points average, p=0.019** across 2,500 conversations (arXiv 2510.07488). Your flat-company instinct is empirically supported.
- Hierarchy wins under **adversarial conditions** (faulty agents). Architect-as-kill-switch is the right escalation shape — flat by default, escalation when broken.
- Production finding from 8-agent fleet: **peer-to-peer messaging was abandoned in favour of Temporal workflows + shared memory.** Confirms async-first; contradicts any "agents need direct channels" framing.
- Context-switching cost: UC Irvine **23m15s recovery time per interruption**.

**Three substrate-distinct LLM candidates (all marked opinion):**
1. **DeepSeek R1** — auditable `<think>` traces, RL-trained, Chinese research lineage. Open-weights, runs on your Ollama. Best fit for an auditor / devil's advocate role. **Highest-leverage addition.**
2. **Qwen3 235B (thinking mode)** — 119 languages, non-Anglophone mathematical intuitions.
3. **Cohere Command A Reasoning** — citation-grounded, resists confabulation. The formal-analysis specialist.

**Explicit do-NOT-add list:** GPT-5.x (training-distribution overlap with Claude — sycophancy risk), Grok 4 (latency floor), Mistral Large 3 (reasoning ceiling on hard multi-step).

**Honest opinion:** DeepSeek R1 is the strongest candidate. Different training lineage, visible reasoning traces, runs on existing Ollama, fits privacy-first hierarchy.

---

## TWO PENNIES — other agents add below

_This section is for other agents (Kimmy, Antigravity, Devon, Hermes, Cursor, Qwen) to add their opinion before the research. Use the Collaboration Protocol: additive only, sign and date, escalate to Ewan if convergence fails after one round trip._

_(empty — awaiting input)_

---

## RESEARCH (verbatim, primary sources)

## TOPIC A — Flat Agent Orgs and Async-First Work

### 1. Flat / No-Team-Leader Multi-Agent Systems: Prior Art

The dominant production pattern in 2025–26 is orchestrator-worker (centralised), but the academic and experimental record on flat topologies is substantive and often counter to the enterprise orthodoxy.

**arXiv 2510.07488 — "Can Lessons From Human Teams Be Applied to Multi-Agent Systems?"** (October 2025):
> "In such settings, the peer-to-peer nature of flat communication likely enables more efficient information exchange and decision convergence. Conversely, hierarchical structures may introduce information bottlenecks or distortion as messages propagate across layers."
— [arxiv.org/pdf/2510.07488](https://arxiv.org/pdf/2510.07488)

The paper ran controlled comparisons across flat teams (3–7 agents, majority vote) and 1- and 2-level hierarchies on commonsense, strategic, and social reasoning tasks. **Key finding: flat teams outperformed hierarchical across all models and tasks, average +5.26 points (t=2.63, p=0.019).** Flat teams dominated on procedural multi-step inference (StrategyQA: mean diff +5.89, Cohen's d=2.18; CommonsenseQA: +9.54, d=1.35). Hierarchical teams showed no significant advantage on any task category. The paper also found that a GPT-4o judge characterised hierarchical outputs as having the "top agent override others," causing fragmentation.

From the same paper, interaction quality metrics (GPT-4o judged on 2,500 conversations):
| Metric | Flat (no persona) | Flat (persona) | Hier. (no persona) | Hier. (persona) |
|---|---|---|---|---|
| Team Comprehension | 3.31 | **3.36** | 2.35 | 2.93 |
| Reasoning Strength | 2.99 | **3.04** | 2.20 | 2.81 |
| Coherence | 3.40 | **3.43** | 2.22 | 2.87 |

**Reddit / production report (April 2026)** — eight-agent production system running Claude and Codex agents in Docker containers:
> "Direct Agent-to-Agent Communication: We experimented with this initially but discontinued it within a month due to issues like conversation drift, lack of an audit trail, and absence of cancellation mechanisms. Now, all cross-agent interactions occur through workflows."
— [reddit.com/r/AI_Agents/comments/1sz6s04](https://www.reddit.com/r/AI_Agents/comments/1sz6s04/six_months_running_multiagent_in_production_the/)

This practitioner found a middle path: flat agent capability (no fixed role hierarchy), but coordination routed through a Temporal workflow engine and shared memory layer rather than direct peer messaging. This preserves the information-exchange benefits of flat structures while avoiding audit-trail collapse.

**Towards Data Science (January 2026)** — on the failure mode of unstructured flat swarms:
> "1. Flat Topology: Each agent maintains an open communication line with every other agent, lacking hierarchy, gatekeeping, or specialized planes to compartmentalize information flow. 2. Noisy Chatter: In the absence of an Orchestrator, agents can get trapped in circular logic or 'hallucination loops,' where they reinforce each other's mistakes rather than correcting them."
— [towardsdatascience.com/why-your-multi-agent-system-is-failing](https://towardsdatascience.com/why-your-multi-agent-system-is-failing-escaping-the-17x-error-trap-of-the-bag-of-agents/)

The same piece cites **DeepMind's finding** that the highest returns from multi-agent coordination occur when single-agent baseline performance is below 45%; once agents hit 80%, adding more agents may generate noise rather than value. This is a critical calibration point for any high-capability fleet.

**OpenReview (May 2025)** — on resilience of flat peer groups:
> "A hierarchical structure—one 'boss' overseeing peer agents—proved most robust, losing only ≈5% accuracy [under adversarial/faulty agent conditions], while a simple chain collapsed by ≈24%."
— [openreview.net/forum?id=bkiM54QftZ](https://openreview.net/forum?id=bkiM54QftZ)

Note the nuance: under **adversarial conditions** (faulty agents), hierarchy outperforms; under **collaborative reasoning conditions**, flat wins. The failure mode differs by context.

**arXiv 2602.04234v4 — "On the Uncertainty of LLM-Based Multi-Agent Collaboration"** (April 2026):
> "We counterintuitively find that a single agent outperforms MAS in approximately 43.3% of cases, and that uncertainty dynamics are largely determined during the first round of interaction... Certainty Preference: reducing peak entropy and maintaining stable uncertainty across agents strongly correlate with correctness."
— [arxiv.org/html/2602.04234v4](https://arxiv.org/html/2602.04234v4)

---

### 2. Async-First Workflow Research

**GitLab All-Remote Handbook:**
> "There is a reason we are really good at async, and that is because we make things smaller. Through iteration, you don't have to coordinate with a ton of people. By taking smaller steps through iteration, we can ship faster. The only way this is possible is through asynchronous communication. — Sid Sijbrandij, GitLab co-founder"
— [handbook.gitlab.com/handbook/company/culture/all-remote/asynchronous](https://handbook.gitlab.com/handbook/company/culture/all-remote/asynchronous/)

GitLab's "Geekbot" async standup model (used across engineering teams) sends structured text prompts each week: (1) How do you feel today? (2) What did you do? (3) Priorities this week? (4) Blockers? (5) Upcoming PTO? — all without synchronous attendance.

**Doist (async-first practitioners):**
> "'Everyone at Doist knows that asynchronous communication is the default, and no one should expect an immediate response from their teammates.' — Allan Christensen, COO"
— [async.twist.com/how-to-move-your-team-toward-async-first-communication](https://async.twist.com/how-to-move-your-team-toward-async-first-communication/)

**Context switching costs (quantified):**
- University of California Irvine: average 23 minutes 15 seconds to fully regain focus after a significant interruption — [basicops.com/cb-articles/the-hidden-cost-of-context-switching](https://www.basicops.com/cb-articles/the-hidden-cost-of-context-switching-cc4za)
- Microsoft 2024 Work Trend Index: employees spend nearly half their day on meetings, emails, and chat rather than deep work — [linkedin.com/pulse/async-first-transformation](https://www.linkedin.com/pulse/async-first-transformation-redesigning-your-operations-5ak0f)
- RescueTime: average knowledge worker switches applications every **40 seconds** (~720 switches per 8-hour day) — [waymakeros.com/learn/context-switching-costs-450b](https://www.waymakeros.com/learn/context-switching-costs-450b)
- Atlassian research: teams replacing recurring status meetings with written/recorded updates **saved up to 31 hours per employee per month** — [linkedin.com/pulse/async-first-transformation](https://www.linkedin.com/pulse/async-first-transformation-redesigning-your-operations-5ak0f)

**Implication for agent fleets:** context-switching costs do not disappear for AI agents — they manifest as context-reconstruction overhead, lost working memory between invocations, and latency compounding across tool calls. The async-first principle of "write it down first" maps directly to structured shared-memory architectures.

---

### 3. Daily Standup Patterns for Agent Fleets

No established academic prior art specifically on daily standups for AI agent fleets was found as of April 2026. The closest prior art comes from two directions:

**Human async standups (production template, GitLab):** The Geekbot pattern — structured text prompt, asynchronous response, results aggregated in a shared channel — is directly portable to agent fleets. An orchestration layer can poll each agent container for a structured status object (current task, blockers, last output hash, token consumption) on a cron schedule and surface this to the human operator without any synchronous gathering.

**Production multi-agent report (April 2026):** The eight-agent production system above used Temporal workflows for all coordination, with a shared memory layer (markdown + vector index) functioning as a persistent standup board:
> "A shared memory system with scoped reads has proven more efficient... every significant interaction is framed as a workflow with a specific structure."
— [reddit.com/r/AI_Agents/comments/1sz6s04](https://www.reddit.com/r/AI_Agents/comments/1sz6s04/six_months_running_multiagent_in_production_the/)

**Hermes Agent (Nous Research):** The Hermes harness supports built-in cron with delivery to any platform and scheduled automations — allowing agent status reports to be pushed to Slack, Telegram, or Discord on a schedule. This is the closest functional equivalent to a standup for a Hermes-based agent fleet. — [hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs/)

---

### 4. Multi-Agent Prevention of "Strongest Model Swallows the Team"

This failure mode appears in the literature under several names: **monoculture collapse**, **vocabulary lock-in**, **consensus without challenge**, and **certainty preference drift**.

**Common failure patterns documented (Reddit r/aiagents, December 2025):**
> "FM-1: Consensus Without Challenge — Agent AI-1 asserts something → AI-2 expands on it → AI-3 further develops the idea, with no one questioning its validity... FM-3: Vocabulary Lock-In — When one agent employs a 'three pillars' framework, others follow suit, causing alternative perspectives to vanish."
— [reddit.com/r/aiagents/comments/1pmu2s3](https://www.reddit.com/r/aiagents/comments/1pmu2s3/common_failure_patterns_in_multiagent_ai/)

**Centralization risk (Neomanex, April 2026):**
> "Only 28% of enterprises have mature capabilities combining automation with AI agents. The rest are hitting what researchers call the '17x error trap': at 95% per-step accuracy, chaining agents without structured coordination degrades reliability by up to 17x through compound failure."
— [neomanex.com/posts/multi-agent-coordination-patterns](https://neomanex.com/posts/multi-agent-coordination-patterns)

**DeepMind finding (cited in Towards Data Science):** In centralised systems, the capability of sub-agents matters more than the capability of the orchestrator. "High-capability sub-agents consistently outperformed those with high-capability orchestrators." This is counterintuitive but suggests: if you must centralise, don't put the strongest model in charge — put it in the working roles.

**arXiv uncertainty paper (2602.04234):** The study found that "base model correctness overwhelms all other features" — meaning when one model has much lower base entropy than others, it tends to dominate collective outputs regardless of topology. This is the quantitative mechanism behind the "strongest model swallows the team" failure.

**Mitigations documented in literature:**
1. Assign a mandatory contrarian/auditor role to a distinct model (not a persona, a different substrate)
2. Route all cross-agent communication through a durable workflow engine (Temporal, Hermes cron) — prevents real-time dominance cascades
3. Use majority voting among agents of comparable (not identical) capability — the flat-team research shows this is robust
4. Keep sub-agents at the working level where DeepMind found strongest model placement provides most value
5. Substrate diversity (different model families, not prompt-level personas) is the deepest mitigation — see Opinion section

---

### 5. Single-Operator AI-Native Businesses: Case Studies 2025–26

**Medvi (Matthew Gallagher, 2025–26):** Telehealth company built from a home office in Los Angeles with $20,000 seed capital. Used ChatGPT, Claude, and custom AI agents for software development, website copy, advertising creative, customer support, and business analytics. Projected $1.8 billion in revenue in 2026, employing two full-time staff (Gallagher and his brother), 16.2% net profit margin.
> "A company generating $1.8 billion with just two employees? In the era of A.I., such a feat is becoming increasingly feasible."
— [nytimes.com/2026/04/02/technology/ai-billion-dollar-company-medvi](https://www.nytimes.com/2026/04/02/technology/ai-billion-dollar-company-medvi.html)

**Pieter Levels:** Cited as $3M+/year, zero employees — builds and runs multiple SaaS products using AI tools. Referenced in Taskade's analysis as a working proof of the one-person company model. — [taskade.com/blog/one-person-companies](https://www.taskade.com/blog/one-person-companies)

**Alibaba international clients (2026):** Alibaba president Kuo Zhang reported that 30–40% of the platform's international clients are solo entrepreneurs running on AI agents.
> "One person, an army of agents, handling everything from product listings to customer service to tax compliance."
— [corpwaters.substack.com/p/how-to-build-a-one-man-ai-team](https://corpwaters.substack.com/p/how-to-build-a-one-man-ai-team)

**NVIDIA internal (GTC 2026):** Jensen Huang revealed NVIDIA internally runs 100 AI agents per human employee — 7.5 million agents serving 75,000 humans. — [taskade.com/blog/one-person-companies](https://www.taskade.com/blog/one-person-companies)

**Market context:** The autonomous AI agent market crossed $7.6 billion in 2025 and is projected to reach $50 billion by 2030 (Deloitte). Gartner reported a 1,445% surge in enterprise inquiries about multi-agent orchestration in 2025. — [taskade.com/blog/one-person-companies](https://www.taskade.com/blog/one-person-companies)

---

## TOPIC B — LLM Roster

### Frontier and Mid-Tier Models

#### Anthropic Claude

**Claude Sonnet (current line):** The flagship working-tier model. Anthropic's position: "Claude and GPT-5.2 are the 'efficiency kings' in practical coding (SWE-Bench), with Claude often achieving state-of-the-art results with lower token usage, making it the most efficient choice for long-running agentic tasks." — [linkedin.com/pulse/best-frontier-ai-model-2025](https://www.linkedin.com/pulse/best-frontier-ai-model-2025-winner-gemini-3-grok-42-52-rick-hightower-bnuyc) Strengths: coding and terminal mastery (record on Terminal-Bench Hard), superior writing quality with less formulaic "AI-ese," reasoning efficiency. Weaknesses: multimodality trails Gemini; context window capped at 200k (smaller than OpenAI and Google). Distinct voice: deliberate, careful, self-correcting, high steering compliance.

**Claude Opus (current line):** "Optimized for complex reasoning and architectural design." Benchmarks: ~90% AIME, ~90% GPQA Diamond. Premium pricing tier ($5/$25 per M tokens). Used in the Reddit production system as "auditor" role due to its evaluative precision.

#### OpenAI GPT

**GPT-5.x (current line):** "GPT-5.2 leads at 93.2% [GPQA Diamond], followed by Gemini 3 Pro at 91.9%." On AIME, achieves 100% (Thinking mode). Context window: 400k tokens. Pricing: ~$1.75/$14 per M tokens. Strengths: scientific synthesis, agentic development workflows, broadest tool integration. Weaknesses: less distinctive stylistic voice than Claude; tends toward the average across writing tasks. Reasoning style: systematic, broad-coverage, integrates Python tools for simulation/verification mid-reasoning. — [linkedin.com/pulse/best-frontier-ai-model-2025](https://www.linkedin.com/pulse/best-frontier-ai-model-2025-winner-gemini-3-grok-42-52-rick-hightower-bnuyc)

#### Google Gemini

**Gemini 3 Pro / 3.1 Pro:** "The most 'book smart' model, achieving the highest score on HLE without assistance at 37.5%. It simply knows more." GPQA Diamond: 91.9%; MMMU-Pro: 81.0%; FACTS benchmark: 68.8% (highest factuality). Context window: 1M+ tokens. Strengths: native multimodal (text, image, video, audio), factual recall, Google Workspace integration. Weaknesses: coding specialisation behind Claude. Distinct reasoning style: encyclopaedic synthesis, native multimodal reasoning, high factuality. — [linkedin.com/pulse/best-frontier-ai-model-2025](https://www.linkedin.com/pulse/best-frontier-ai-model-2025-winner-gemini-3-grok-42-52-rick-hightower-bnuyc)

#### xAI Grok

**Grok 4 / Grok 4 Heavy:** Single-agent Grok 4 scores ~26.9% on HLE (no tools); with tools: 41%; Grok 4 Heavy (multi-agent): 50.7%, crossing superhuman threshold on that benchmark. 100% on AIME. Strengths: brute-force compute scaling, real-time knowledge via X platform integration, multi-agent consensus reasoning. Weaknesses: extremely slow (seconds to minutes), computationally expensive, multimodal capabilities trail Gemini, no mini variant. Distinct reasoning style: brute-force parallel debate — spawns up to 32 parallel agents to debate and verify solutions rather than a single deliberative chain. — [datacamp.com/blog/grok-4](https://www.datacamp.com/blog/grok-4)

#### Mistral

**Mistral Large 3 (December 2025):** First Mistral MoE since Mixtral series, trained from scratch on 3,000 H200 GPUs. MMLU (multilingual): ~85.5%; GPQA Diamond: ~43.9% (significantly below specialised reasoning models at 70–85%). Strengths: multilingual (40+ languages, best-in-class non-English/Chinese performance), code generation (~92% HumanEval), enterprise compliance, open weights. Weaknesses: GPQA Diamond score reveals that extended chain-of-thought reasoning is not a core strength; SimpleQA ~24% (confident confabulation under uncertainty). Distinct voice: practical European generalist, direct recall and pattern-matching over deep chained reasoning. — [intuitionlabs.ai/articles/mistral-large-3-moe-llm-explained](https://intuitionlabs.ai/articles/mistral-large-3-moe-llm-explained)

#### DeepSeek

**DeepSeek R1 (reasoning model):** RL-trained specifically for multi-step deduction. MATH-500: 97.3%; AIME: 79.8% (vs V3's 90.0% MATH-500, 39.6% AIME); GPQA Diamond: 71.5%. Generates explicit `<think>` traces before answering — fully auditable chain-of-thought. 671B total parameters (MoE), 37B active, 64K context. Strengths: transparent reasoning, self-verification (lower hallucination via CoT), auditable for regulated workflows. Weaknesses: 2–3x slower than V3, higher token cost. — [emergent.sh/learn/deepseek-r1-vs-v3](https://emergent.sh/learn/deepseek-r1-vs-v3)

**DeepSeek V3 (general-purpose model):** MoE, 685B total / 37B active, 128K context. MATH-500: 90.0%; fast direct output (no reasoning tokens). Pricing: $0.27/$1.10 per M tokens. Strengths: speed, cost, broad task coverage. Weaknesses: no visible reasoning trace; less rigorous on hard multi-step logic. Distinct style: efficient, engineering-focused, clean output without deliberation overhead.

#### Qwen (Alibaba)

**Qwen3 235B A22B (2507):** 235B total / 22B active, MoE, 128 experts. Unique feature: **switchable thinking/non-thinking mode within a single model** — toggles between extended reasoning and fast conversational response. AIME25: 92.3%; 119 languages. Apache 2.0 licence. On Artificial Analysis Intelligence Index: score of 69, one point above DeepSeek R1 0528, near Gemini 2.5 Pro and o3. Strengths: best multilingual coverage of any open-weights model, highest open-weights benchmark scores as of mid-2025. Weaknesses: native 32K context (extensible to 131K with YaRN). Distinct style: pragmatic, math-strong, genuinely multilingual reasoning. — [huggingface.co/Qwen/Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B)

#### Cohere

**Command A Reasoning (August 2025):** 111B parameters, 256K context, 32K output. Enterprise-purpose-built: not a general-purpose model but designed specifically for autonomous agents, advanced RAG, and multi-turn coherence. Supports reasoning toggle (on/off via system prompt or `reasoning=True` flag). Available open weights on Hugging Face. Strengths: enterprise governance, precise citations, long-document analysis, formal multi-step argument construction. Weaknesses: less broad benchmark coverage than frontier models; designed for depth over breadth. Distinct style: enterprise-legal precision, structured argument, citation-anchored. — [docs.oracle.com/en-us/iaas/Content/generative-ai/cohere-command-a-reasoning-08-2025.htm](https://docs.oracle.com/en-us/iaas/Content/generative-ai/cohere-command-a-reasoning-08-2025.htm)

#### Kimi (Moonshot AI)

**Kimi K2.6 (April 2026):** MoE, 1T total parameters / 32B active (same architecture as K2 and K2.5). Agentic performance: GDPval-AA Elo 1520 (vs K2.5's 1309 — a major jump). Tool use: 96% on τ²-Bench Telecom. Hallucination rate: 39% (reduced from K2.5's 65%, comparable to Claude Opus). Multimodal: image and video input via MoonViT. Context: 256K. "Preserve Thinking" mode maintains reasoning across complex multi-step tasks. Agent swarm: scales to 300 specialised agents executing 4,000 coordinated steps. Available via Moonshot API and Novita, Baseten, Fireworks, Parasail; also available via Ollama (`ollama launch kimi`). — [artificialanalysis.ai/articles/kimi-k2-6-the-new-leading-open-weights-model](https://artificialanalysis.ai/articles/kimi-k2-6-the-new-leading-open-weights-model)

#### Meta Llama

**Llama 4 Scout / Maverick (April 2025):** First open-weight natively multimodal Llama models, MoE architecture. Scout: 17B active / 109B total, 16 experts, **10 million token context** (industry-leading), single H100 GPU (INT4), ~$0.09/M tokens. Maverick: 17B active / 400B total, 128 experts — beats GPT-4o and Gemini 2.0 on coding, reasoning, multilingual, and image benchmarks; competitive with DeepSeek V3.1. Strengths: open weights, long-context, multimodal, cost-efficiency. Weaknesses: Scout context pre-trained to 256K (10M via generalisation — reliability at extreme lengths still being validated). Distinct style: Meta-ecosystem pragmatism, instruction-following, competitive generalist without a distinctive reasoning voice. — [ai.meta.com/blog/llama-4-multimodal-intelligence](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)

#### Nous Research (Hermes)

**Hermes 4 (70B and 405B):** Built on Meta-Llama-3.1 base. Hybrid reasoning mode: can respond directly or generate `<think>...</think>` traces — user-controllable via `reasoning enabled` boolean. Strong structured output (JSON mode) and function-call syntax for agent applications. Available on OpenRouter. — [openrouter.ai/nousresearch](https://openrouter.ai/nousresearch)

**DeepHermes 3:** "One of the first LLM models to unify both 'intuitive' traditional mode responses and long chain of thought reasoning responses into a single model, toggled by a system prompt." Fine-tuned via distillation from R1. Strengths: agentic function calling, reasoning-toggle, open weights. Distinct style: agent-native, self-improving through skill creation, memory-enabled across sessions. — [openrouter.ai/nousresearch](https://openrouter.ai/nousresearch)

---

### agentskills.io Ecosystem and Hermes Compatibility

**agentskills.io** is an open standard for portable agent skills — originally developed by Anthropic, released as an open standard, adopted by a growing ecosystem of agent products.

> "Agents load skills through progressive disclosure, in three stages: 1. Discovery: At startup, agents load only the name and description of each available skill. 2. Activation: When a task matches a skill's description, the agent reads the full SKILL.md instructions into context. 3. Execution: The agent follows the instructions, optionally executing bundled code or loading referenced files as needed."
— [agentskills.io/home](https://agentskills.io/home)

**Hermes Agent** natively supports agentskills.io:
> "Open standard skills — Compatible with agentskills.io. Skills are portable, shareable, and community-contributed via the Skills Hub."
— [hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs/)

Hermes runs natively on **Nous Portal, OpenRouter, OpenAI, or any endpoint** — meaning any model accessible via these APIs works in the Hermes harness. The Hermes ecosystem also supports: CLI, Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Mattermost, Email, SMS, DingTalk, Feishu, WeCom, BlueBubbles, Home Assistant (15+ platforms).

**OpenClaw** appears in community use as a primary orchestrator for multi-agent business operations, often paired with Claude Opus as an auditor. A practitioner noted:
> "I'm primarily using OpenClaw, but it tends to malfunction frequently. Consequently, I've been relying on Claude Opus 4.6 AI chats to function like an auditor."
— [reddit.com/r/AI_Agents/comments/1sfl9jy](https://www.reddit.com/r/AI_Agents/comments/1sfl9jy/attempting_to_create_a_self_auditing_harness_using_openclaw_hermes/)

---

### Open-Weights Models for Local Ollama Execution

As of April 2026, Ollama supports 200+ optimised models. Best options for local deployment:

| Model | Approx Size | Key Strength | Ollama Command |
|---|---|---|---|
| Kimi K2.6 | Cloud via Ollama CLI | Agentic, tool use, 256K context | `ollama launch kimi --model kimi-k2.6:cloud` |
| Qwen3.5 / 3.6 | Various (7B–235B) | Multilingual, thinking/non-thinking toggle | `ollama run qwen3.5` |
| DeepSeek V3.2-Exp | 7B+ quantised | Fast, coding-strong | `ollama run deepseek-v3.2-exp:7b` |
| Gemma 4 26B | ~26B | Speed, Apple Silicon optimised | `ollama run gemma4:26b` |
| Mistral Large 3 | Quantised variants | Multilingual, enterprise generalist | `ollama run mistral-large-3` |
| Llama 4 Scout | ~109B total / 17B active | 10M context, multimodal, single H100 | via Ollama model library |
| Hermes 4 70B | ~70B quantised | Agentic function calling, reasoning toggle | via Ollama/OpenRouter |

Sources: [pinggy.io/blog/top_5_local_llm_tools_and_models](https://pinggy.io/blog/top_5_local_llm_tools_and_models/), [Ollama v0.21.x](https://ollama.com), [hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs/)

---

## OPINION SECTION
*Everything below is marked as opinion. It is Cassian's analytical view, not established fact.*

### Which Models Bring Genuinely Different Reasoning Fingerprints

**The substrate diversity problem:** The research makes clear that multi-agent monoculture is not a prompt problem — it is a training distribution problem. Vocabulary lock-in, consensus without challenge, and certainty preference drift all occur because models trained on similar data with similar RLHF pipelines converge on similar priors. Personas do not fix this; different training provenance does.

**Current roster:** Cassian (Claude Sonnet — Anthropic, constitutional AI alignment, careful/steerable), Kimmy (Kimi K2.6 — Moonshot AI, agentic-native MoE, Chinese research lineage, 300-agent swarm architecture), Antigravity (TBD).

**The coverage gaps as I read the research:**

1. **DeepSeek R1** is the strongest candidate for genuine substrate diversity. Its core distinction is not benchmark score but *how* it reaches answers: RL-trained on pure outcome reward, it generates explicit auditable `<think>` traces before committing to output. This is a fundamentally different epistemic posture from Claude's constitutional training or Kimi's agentic-swarm architecture. DeepSeek's Chinese research lineage (separate from Anthropic, Google, and Meta pipelines) means its world-model priors are genuinely distinct, not just fine-tuned divergence. It is particularly strong at catching the kinds of concurrency and design flaws that smooth-output models miss — the production finding from Emergent that "R1 identified a concurrency flaw in the idempotency design that V3 missed entirely" is an example of substrate-level reasoning difference. Open weights, local-deployable on Ollama, MIT licence. Competence floor: easily clears it (71.5% GPQA Diamond, 97.3% MATH-500). **Recommended for a rigorous auditor / devil's advocate role.**

2. **Qwen3 235B (thinking mode)** brings the most distinct multilingual-and-mathematical substrate on the open-weights side. Its training includes 119 languages and a Chinese mathematical curriculum that produces different proof strategies and error patterns from Anglophone-trained models. The thinking/non-thinking toggle within a single model is architecturally unique — not two models, but one substrate with two operational modes. The Alibaba research lineage is separate from DeepSeek and from Western labs. Its weakness (constrained native context window) is remediable via YaRN. **Recommended if the fleet needs broad multilingual coverage or a model whose mathematical intuitions follow a different path than Claude's.**

3. **Cohere Command A Reasoning** is the least-used frontier model in community multi-agent stacks and therefore the most genuinely underrepresented training distribution. It was built specifically for enterprise-style structured argument (legal/financial/RAG) rather than general helpfulness — its constitutional biases are toward citation-grounded, formally structured output. This makes it odd and difficult to use casually, which is precisely what creates substrate diversity value: it will challenge conclusions from a different angle than any of the above. The reasoning toggle and 256K context make it practically usable. **Recommended if the fleet does formal analysis, document review, or any workflow where you want a model that was trained to resist confabulation and demand citations.**

**What I would not add as substrate diversity:**
- GPT-5.x: Anthropic and OpenAI training distributions have converged significantly on benchmarks; the stylistic differences are real but not substrate-deep.
- Grok 4: The reasoning fingerprint (brute-force parallel debate) is genuinely different, but the competence floor issue is not the concern — the latency floor is. Seconds-to-minutes per response makes it unsuitable for fleet work without dedicated infrastructure.
- Mistral Large 3: Good generalist, but the GPQA Diamond score (43.9%) reveals a reasoning ceiling below the others on hard multi-step tasks. Fails the competence floor for complex analytical work.

**The "Five Rods" framing:** The goal is not more agents but different angles of attack. One model that catches what another misses, across training-distribution lines, is worth more than three agents from the same family debating politely. DeepSeek R1 + Qwen3 235B thinking as the top two additions would give the fleet: explicit auditable reasoning (DeepSeek), non-Anglophone mathematical intuition (Qwen), and the existing deliberative/steerable/agentic triad (Cassian/Kimmy/Antigravity).

---

*— Cassian-research-subagent*
