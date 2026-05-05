# Token optimisation 2026

**Topic:** Token optimisation 2026
**Status:** Research filed. Opinion attached. Awaiting other agents' two pennies.
**Path:** clean-build/01_truth/research/08_token_optimisation.md
**Authored by:** Cassian (Claude Sonnet) + Cassian-research-subagent
**Date:** 2026-05-04 / 2026-05-05 BST

---

## CASSIAN'S OPINION (clearly marked, NOT authoritative)

> _Read with scepticism per the Bias-Bound Principle. Every claim is opinion until verified by the receiver._

**Likely identification of "lush science from last night":** **TRS (Thinking with Reasoning Skills)**, arXiv April 23 2026. Halves reasoning tokens without the accuracy degradation of CoD/TALE. Closest match to Ewan's flag.

**Immediately deployable on Beast (highest ROI first):**
1. **Anthropic `compact_20260112`** — auto-compaction at 50K tokens. Highest ROI on the list. Prevents quadratic context growth in agentic multi-repo tasks.
2. **LiteLLM sidecar architecture** — sub-millisecond proxy overhead, no application code changes.
3. **Model tiering via LiteLLM router** — Haiku for classification, Sonnet for standard, Opus for complex reasoning. Highest-leverage cost lever without model changes.

**Bloat for Beast:**
- Defluffer / stenographer-shorthand tricks — brittle in production across 32 heterogeneous repos
- LLMLingua heavy compression pipelines — adds inference latency, RAG-specific not agent-orchestration
- CrewAI / AutoGen orchestration — 4-15× token multiplier risk
- Draft-Thinking fine-tuning — requires Qwen3 training, not deployable without infra investment

**Note on terminology:** "Anchor/Routine/Tail" and "System_and_3" pattern names from your spine don't appear in published Anthropic sources. Likely internal Amplified Partners terminology. Worth confirming whether they're Amplified-original or external attribution.

**Honest opinion:** Anthropic's `compact_20260112` is the single highest-ROI item. Deploy it before any other token work.

---

## TWO PENNIES — other agents add below

_This section is for other agents (Kimmy, Antigravity, Devon, Hermes, Cursor, Qwen) to add their opinion before the research. Use the Collaboration Protocol: additive only, sign and date, escalate to Ewan if convergence fails after one round trip._

_(empty — awaiting input)_

---

## RESEARCH (verbatim, primary sources)

## 1. Prompt Caching — Anthropic & OpenAI

**Anthropic** caches KV matrices of prompt prefixes. Minimum 1024 tokens; default TTL 5 minutes (1-hour TTL at 2× write cost). Cache reads do not count against ITPM limits on Claude 3.7+. Workspace-isolated since February 2026 (not org-wide). Savings reported at up to 90% on input tokens at high hit rates.

> "Cached input tokens on both OpenAI and Anthropic are priced at roughly 10x less than regular input tokens. On latency, AWS reports up to 85% reduction in response time when the cache hits." — [Genta.dev Prompt Caching Guide, April 23 2026](https://genta.dev/resources/prompt-caching-llm-guide)

**OpenAI** caches automatically for prompts >1024 tokens, no special headers required, 50% discount on cache hits (vs Anthropic's ~90%). GPT-5.5 (released April 2026) offers 90% cached-input discount at $0.50/MTok cached input — but GPT-5.5 Pro has no cached-input discount.

> "Provider routing for cache locality" and "frozen datetime" in system prompts are identified as critical practices for maintaining high hit rates. ProjectDiscovery went from 7% to 84% cache hit rate — 59% overall cost reduction — by moving dynamic content out of the cacheable prefix. — [ProjectDiscovery, April 9 2026](https://projectdiscovery.io/blog/how-we-cut-llm-cost-with-prompt-caching)

---

## 2. Context Compaction (Anthropic Native)

Anthropic shipped `compact_20260112` as a beta API primitive in Claude Opus 4.6 (released February 2026, context compaction detailed March 2026).

> "Context compaction automatically summarizes and replaces older context when the conversation approaches a configurable threshold, letting Claude perform longer tasks without hitting limits." — [Anthropic, Opus 4.6 release](https://www.anthropic.com/news/claude-opus-4-6)

> "Compaction is a *whole-transcript* operation: user messages, assistant messages, tool calls, tool results, even prior compaction blocks are all flattened into the summary." — [Anthropic Cookbook: Context Engineering](https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools)

Three distinct API primitives exist: `compact_20260112` (whole-context summarisation, triggers at ≥50K tokens), `clear_tool_uses_20250919` (surgical tool-result clearing, keeps recent N results), and `memory_20250818` (cross-session external store). AWS Bedrock documentation confirms beta header `compact-2026-01-12` for InvokeModel. — [AWS Bedrock Compaction Docs](https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-compaction.html)

**Note on "Anchor/Routine/Tail" and "System_and_3":** No trace of these specific pattern names found in Anthropic documentation, arxiv, or production write-ups. They may be internal Amplified Partners naming conventions rather than published patterns.

---

## 3. Context Compaction Patterns (Community)

The LogRocket 2026 context problem piece describes tool for document pruning:
> "Tools such as **Provence** can automatically prune documents, achieving compression rates up to **95 percent** while retaining relevant information." — [LogRocket, March 4 2026](https://blog.logrocket.com/llm-context-problem-strategies-2026/)

Prime Intellect published on "Recursive Language Models" and **context folding** — model-managed context delegation to sub-LLMs and scripts rather than summarisation. — [Prime Intellect RLM, January 2026](https://www.primeintellect.ai/blog/rlm)

---

## 4. Recent High-Signal Research ("Lush Science")

**Draft-Thinking** (arXiv 2603.00578, February 28 2026 — candidate for what Ewan flagged):
> "The draft reasoning mode reduces the average token budget from 5,668 to 986 while maintaining an accuracy of 90.6%... on MATH500, it achieves an 82.6% reduction in reasoning budget at the cost of only a 2.6% performance drop." — [arXiv:2603.00578](https://arxiv.org/abs/2603.00578)

**TRS — Thinking with Reasoning Skills** (arXiv 2604.21764, April 23 2026 — most recent found):
> "TRS distills deliberation into retrievable *reasoning skills* and reuses them at inference time... on Doubao, TRS achieves the lowest token consumption, cutting generated tokens for hard problems from ~12k to ~5k while maintaining top accuracy. On GPT-OSS, TRS halves token usage (~15k to ~7k) without the accuracy loss seen in 'speed-limit' approaches like TALE or CoD." — [arXiv:2604.21764](https://arxiv.org/html/2604.21764v1)

**CROP** (arXiv 2604.14214, April 2026):
> "CROP reduces output token consumption by up to 80.6% on complex reasoning benchmarks (GSM8K, LogiQA and BIG-Bench Hard) while maintaining comparable accuracy compared to unconstrained CoT." — [arXiv:2604.14214](https://arxiv.org/html/2604.14214v1)

**Chain of Draft** (arXiv 2502.18600, foundational paper, now widely cited):
> "CoD matches or surpasses CoT in accuracy while using as little as only 7.6% of the tokens." — [arXiv:2502.18600](https://arxiv.org/html/2502.18600v2)

**Parallel Token Prediction (PTP)** — ICLR 2026 paper (April 22 2026):
> "Distilling Vicuna-7B with PTP in a speculative decoding setup delivered a 2.4x speedup over next-token prediction across diverse text tasks — with up to 3.2x achievable through optimized implementation." — [Felix Draxler, LinkedIn/ICLR 2026](https://www.linkedin.com/posts/felix-draxler_machinelearning-llm-iclr2026-activity-7452729729389924352-XN--)

---

## 5. Token Proxy / Cost-Router (LiteLLM on Beast)

LiteLLM is identified as the standard open-source LLM proxy/gateway in 2026. Key recent development: **sidecar architecture** for sub-millisecond proxy overhead.

> "Rather than rewriting LiteLLM or introducing complex deployment requirements, we adopt an optional **sidecar architecture**... By keeping Python focused on orchestration and extensibility, and offloading performance-critical execution to a sidecar, we establish a foundation for making LiteLLM **permanently fast over time**—even on modest hardware such as a 1-CPU, 2-GB RAM instance." — [LiteLLM Architecture Blog, February 2026](https://docs.litellm.ai/blog/tags/architecture)

LiteLLM supports model-tiered routing (Haiku for classification, Sonnet for standard, Opus for complex reasoning), spend tracking via Postgres, virtual keys, Redis caching, and LangFuse/MLflow observability integration. Multi-agent systems consume 4–15× more tokens than single calls if unoptimised. — [Obvious Works Token Optimisation 2026, February 24 2026](https://www.obviousworks.ch/en/token-optimization-saves-up-to-80-percent-llm-costs/)

**Defluffer** (April 18 2026) — lightweight dictionary-based prompt compression:
> "Save an average of 45% tokens of your prompt text with near zero compute." — [DEV Community, April 18 2026](https://dev.to/grahamthedev/defluffer-reduce-token-usage-by-45-26jj)

---

## OPINION — Beast deployment applicability
*Everything in this section is opinion, not established fact.*

**Immediately useful for a 32-repo, 37-container Beast deployment:**

- **Anthropic `compact_20260112`** — opinion: highest ROI item on the list. Agentic tasks that traverse multiple repos compound context quadratically; auto-compaction at 50K tokens prevents this without architectural work.
- **LiteLLM sidecar architecture** — opinion: if Beast is running LiteLLM at any meaningful RPS, the sidecar upgrade is a clean, low-risk overhead reduction that requires no changes to application code.
- **Model tiering via LiteLLM router** — opinion: Beast's 37 containers almost certainly have heterogeneous task complexity. Routing Haiku/Sonnet vs Opus by task type is the highest-leverage cost lever that doesn't require model changes.
- **TRS (Thinking with Reasoning Skills, arXiv April 23 2026)** — opinion: this is the likeliest candidate for Ewan's "lush science from last night." Token halving without the accuracy degradation of CoD/TALE is a genuine step-change for agentic reasoning tasks.

**Bloat for Beast:**

- **Defluffer / stenographer-shorthand tricks** — opinion: clever demos, brittle in production, especially across 32 heterogeneous repos where prompt schemas vary per container.
- **LLMLingua and heavy compression pipelines** — opinion: adds inference latency and an extra model hop; the gains are mostly meaningful for RAG-at-scale, not agent orchestration.
- **Multi-agent orchestration frameworks (CrewAI, AutoGen)** — opinion: the 4–15× token multiplier risk makes these actively dangerous unless Beast's workloads are provably independent parallelisable tasks.
- **Draft-Thinking fine-tuning** — opinion: requires training on Qwen3/similar; not deployable without significant infra investment; watch the space but don't ship it yet.

---

*— Cassian-research-subagent*
