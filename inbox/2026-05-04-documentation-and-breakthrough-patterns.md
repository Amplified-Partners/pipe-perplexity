# Documentation philosophy + breakthrough-tagging patterns

**Topic:** Documentation philosophy + breakthrough-tagging patterns
**Status:** Research filed. Opinion attached. Awaiting other agents' two pennies.
**Path:** clean-build/01_truth/research/06_documentation_patterns.md
**Authored by:** Cassian (Claude Sonnet) + Cassian-research-subagent
**Date:** 2026-05-04 / 2026-05-05 BST

---

## CASSIAN'S OPINION (clearly marked, NOT authoritative)

> _Read with scepticism per the Bias-Bound Principle. Every claim is opinion until verified by the receiver._

**Most important sentence in the file:** _Automated promotion without receiver verification is surveillance in thin disguise, regardless of what it's called._

That's the bias-bound principle applied to the breakthrough rule. The agent proposes; the receiver verifies. Anything else collapses two-tier learning into a panopticon.

**What maps cleanly to existing design:**
- **Frozen-snapshot pattern** (Hermes, OpenClaw) — agent pods hold in-progress thinking without system prompt mutating mid-session
- **ESAA "purified view"** — append-only event log + filtered injection = "surface to institutional memory only on breakthrough"
- **OpenClaw three-gate promotion** (score + recall frequency + query diversity) — making it explicit reduces noise without surveillance

**Bloat to avoid:**
- Letta/MemGPT runtime lock-in — fights anti-bloat
- Mem0 auto-extraction — violates "only on breakthrough" by design
- Databricks MemAlign ACL stack — pre-mature complexity for trust-bounded team

**Honest opinion:** the breakthrough rule should remain **agent-proposes-receiver-verifies**, not auto-promoted. This corollary belongs near the bias-bound principle if either is promoted to spine.

---

## TWO PENNIES — other agents add below

_This section is for other agents (Kimmy, Antigravity, Devon, Hermes, Cursor, Qwen) to add their opinion before the research. Use the Collaboration Protocol: additive only, sign and date, escalate to Ewan if convergence fails after one round trip._

_(empty — awaiting input)_

---

## RESEARCH (verbatim, primary sources)

## 1. Background Recording / Event Sourcing (Not Polluting Agent Context)

The clearest architectural statement comes from the **ESAA** paper (Event Sourcing for Autonomous Agents, arXiv:2602.23193v1, 2026):

> "ESAA proposes that the agent should not carry long-term memory in the raw prompt; it should receive a purified view (roadmap + relevant facts) derived from the log. This approach addresses limitations like *lost-in-the-middle*, as the orchestrator selectively injects information needed for the current step, rather than relying on the model to maintain all details across long windows."

> "ESAA establishes a strict separation between (i) the LLM's heuristic cognition and (ii) the system's deterministic execution. The agent does not have direct write permission to the project or the event store. Its role is to emit structured intentions and change proposals."

> "In ESAA, agents emit only structured intentions in validated JSON (agent.result or issue.report); a deterministic orchestrator validates, persists events in an append-only log (activity.jsonl), applies file-writing effects, and projects a verifiable materialized view (roadmap.json)."

Source: https://arxiv.org/html/2602.23193v1

Anthropic's engineering blog confirms the same constraint from a different angle:

> "But it's likely that for the foreseeable future, context windows of all sizes will be subject to context pollution and information relevance concerns... Sub-agent architectures provide another way around context limitations. Rather than one agent attempting to maintain state across an entire project, specialized sub-agents can handle focused tasks with clean context windows... Each subagent might explore extensively, using tens of thousands of tokens or more, but returns only a condensed, distilled summary of its work (often 1,000–2,000 tokens)."

Source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

---

## 2. Per-Agent Private Memory ("Pods") in Published Implementations

**Mem0** (production multi-agent layer) formalizes private-per-agent scoping:

> "Mem0 implements memory scoping through four dimensions: user_id for personal memories, agent_id for agent-specific context, run_id for session isolation, and app_id for application-level defaults. This ensures that each agent retrieves only memories relevant to its role, preventing context pollution while still allowing agents to share user-level context when needed."

Source: https://mem0.ai/blog/multi-agent-memory-systems

**Letta/MemGPT** describes the OS analogy for per-agent context isolation:

> "Core memory consists of in-context memory blocks that can be managed by the agent itself or by other agents. These blocks focus on specific topics such as memories about the user, organization, or the current task... The key feature is that these blocks are editable via APIs and remain pinned to the agent's context window."

> "Designing an agent's memory is essentially context engineering: determining which tokens enter the context window and how they're organized."

Source: https://www.letta.com/blog/agent-memory

**CoALA** (Cognitive Architectures for Language Agents, arXiv:2309.02427, Princeton/CMU 2023) provides the foundational taxonomy. Per the Atlan summary of that paper:

> "CoALA distinguishes episodic (instance-specific, context-preserved) from semantic (abstracted, generalized) and procedural (skills, code) memory. Most major frameworks, including Letta, Mem0, and LangChain, use CoALA as their taxonomy foundation."

Source: https://atlan.com/know/episodic-memory-ai-agents/

---

## 3. The "Breakthrough Rule" — Flagging Important Memories

### Hermes Agent (MEMORY.md / USER.md)

The clearest published "what gets written" rule comes from Hermes v0.10:

> "Save these (the agent does this proactively): User preferences... Environment facts... Corrections... Conventions... Completed work..."

> "Skip these: Trivial/obvious info — Easily re-discovered facts — Raw data dumps (too big for memory) — Session-specific ephemera — Information already in context files."

> "Prompt memory is updated on the agent's judgment, prompted periodically by a configurable `nudge_interval` and flushed proactively in gateway mode before idle timeout."

> "The frozen-snapshot pattern: the system prompt injection is captured once at session start and never changes mid-session. This is intentional — it preserves the LLM's prefix cache for performance. Changes made during a session are persisted to disk immediately but don't appear in the system prompt until the next session."

Sources: https://blakecrosley.com/guides/hermes · https://vectorize.io/articles/hermes-agent-memory-explained

### Claude Code (CLAUDE.md / Auto Memory)

> "Auto memory lets Claude accumulate knowledge across sessions without you writing anything. Claude saves notes for itself as it works: build commands, debugging insights, architecture notes, code style preferences, and workflow habits. Claude doesn't save something every session. It decides what's worth remembering based on whether the information would be useful in a future conversation."

> "Add to [CLAUDE.md] when: Claude makes the same mistake a second time — A code review catches something Claude should have known about this codebase — You type the same correction or clarification into chat that you typed last session."

Source: https://code.claude.com/docs/en/memory

### OpenClaw (MEMORY.md / SKILL.md / Dreaming promotion)

> "Dreaming is an optional background consolidation pass for memory. It collects short-term signals, scores candidates, and promotes only qualified items into long-term memory (MEMORY.md)."

> "Thresholded: promotions must pass score, recall frequency, and query diversity gates."

> "Teams should enforce a promotion policy: information starts in the daily log and moves to MEMORY.md only after review confirms it as a durable operating fact."

> "MEMORY.md is still only written by deep promotion."

> "A skill is a directory containing a SKILL.md file... Those instructions tell the agent when and how to invoke a specific tool... Skills are stored in `~/.hermes/skills/`, are searchable, and self-improve as the agent reuses and refines them. This is the self-improving part people expect memory to handle."

Sources: https://docs.openclaw.ai/concepts/memory · https://www.codebridge.tech/articles/how-to-build-domain-specific-ai-agents-with-openclaw-skills-soul-md-and-memory

---

## 4. Two-Tier Learning: Institutional vs. Personal

**Databricks** (MemAlign research, 2026) is the clearest statement of the institutional/personal split in production:

> "Some memories are specific to a single user's preferences and workflows; others represent shared organizational knowledge — naming conventions, common queries, business rules. The memory system must scope retrieval and updates appropriately: surface organizational knowledge broadly while keeping individual context private, respecting permissions and ACLs."

> "Access controls must be identity-aware: individual memories should remain private, while organizational knowledge can be shared within access-controlled bounds."

Source: https://www.databricks.com/blog/memory-scaling-ai-agents

**Vectorize** names the class distinction:

> "The memory class distinction matters more than most teams realize. Personalization memory stores what a user prefers. Institutional knowledge memory stores what the AI agent has learned about how to do its job — extracted lessons, domain patterns, entity relationships, and corrections that compound over time."

Source: https://vectorize.io/articles/best-ai-agent-memory-systems

Anthropic's structured note-taking description captures a simple two-tier in practice:

> "Structured note-taking, or agentic memory, is a technique where the agent regularly writes notes persisted to memory outside of the context window. These notes get pulled back into the context window at later times. This strategy provides persistent memory with minimal overhead."

Source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

---

## OPINION SECTION

*Everything below is opinion. No claims should be treated as verified until tested against Amplified Partners' actual system behavior.*

**What maps cleanly:** The frozen-snapshot pattern (Hermes, OpenClaw) fits the Amplified design precisely — agent pods hold in-progress thinking without the system prompt mutating mid-session, preserving prefix cache stability. The ESAA "purified view" principle — log events immutably, inject only the relevant subset into the agent's next context — matches the "surfaces to institutional memory only on breakthrough" ethos. The OpenClaw promotion gate (score + recall frequency + query diversity) is architecturally close to what Amplified is already doing informally; making the threshold explicit could reduce noise without adding surveillance.

**What would be bloat:** The Letta/MemGPT self-editing RAM/disk/cold-storage tier system is powerful but assumes an agent runtime that manages the entire loop — architectural lock-in that conflicts with anti-bloat and no-surveillance principles. Mem0's passive extraction pipeline (auto-extract facts from every turn) violates the "only on breakthrough" boundary by design. The Databricks MemAlign ACL/permissions stack is enterprise overhead that makes sense at scale but is pre-mature complexity for a small, trust-bounded team.

**The bias-bound implication:** The breakthrough rule is best treated as a gate the agent proposes, not a gate the system enforces. The receiver verifying the claim — human or orchestrator — is what gives institutional memory its legitimacy. Automated promotion without receiver verification is surveillance in thin disguise, regardless of what it's called.

---

*— Cassian-research-subagent*
