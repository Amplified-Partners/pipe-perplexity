# MAESTRO + agent harness security

**Topic:** MAESTRO + agent harness security
**Status:** Research filed. Opinion attached. Awaiting other agents' two pennies.
**Path:** clean-build/01_truth/research/02_maestro_and_harnesses.md
**Authored by:** Cassian (Claude Sonnet) + Cassian-research-subagent
**Date:** 2026-05-04 / 2026-05-05 BST

---

## CASSIAN'S OPINION (clearly marked, NOT authoritative)

> _Read with scepticism per the Bias-Bound Principle. Every claim is opinion until verified by the receiver._

**Most useful finding:** Layer 5 (Evaluation & Observability) is the real gap for safe step-away. _Automated anomaly detection precisely because the human is not watching._ This sits alongside the bloat audit and the sycophancy fix as a precondition for stepping away — not optional.

**Already covered by existing stack:**
- Hermes's `DANGEROUS_PATTERNS` in `approval.py` = MAESTRO Layer 4/6 destructive gating
- Hermes's `bubble` permission mode = multi-agent escalation risk (Layer 3)
- OpenClaw's SKILL.md = one of four reference platforms in OWASP Agentic Skills Top 10

**Bloat to avoid:**
- Cedar/OPA/OpenFGA full IBAC engine = solves problems a closed 32-repo stack doesn't have. A 50-line Python dict at the Hermes gateway gives equivalent coverage.
- ACNBP cryptographic binding = open-marketplace problem you don't have. Simple gateway allow-listing is equivalent.
- OWASP AST10 Merkle-root signing = pre-emptive overhead until skills are externally distributed.

**Honest opinion:** AI-vs-Python boundary applied to security tooling — deterministic minimum first, full framework only if scale demands it.

---

## TWO PENNIES — other agents add below

_This section is for other agents (Kimmy, Antigravity, Devon, Hermes, Cursor, Qwen) to add their opinion before the research. Use the Collaboration Protocol: additive only, sign and date, escalate to Ewan if convergence fails after one round trip._

_(empty — awaiting input)_

---

## RESEARCH (verbatim, primary sources)

## 1. MAESTRO 7-Layer Threat Modelling Framework

**Source:** Ken Huang, "Agentic AI Threat Modeling Framework: MAESTRO," CSA, 6 Feb 2025  
**URL:** https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro  
**What it is:** The original published CSA blog post introducing MAESTRO. Creator attribution: *"MAESTRO was created by Ken Huang, CEO & Chief AI Officer, DistributedApps.ai."* (https://labs.cloudsecurityalliance.org/maestro/)

**Framework name:**
> "MAESTRO (Multi-Agent Environment, Security, Threat, Risk, and Outcome)"

**On architecture:**
> "MAESTRO is built around a seven-layer reference architecture described by Ken Huang... from Foundation Models that provide core AI capabilities, through Data Operations and Agent Frameworks that manage information and development tools, to Deployment Infrastructure and Security layers that ensure reliable and safe operations, culminating in the Agent Ecosystem where business applications deliver value to end-users."

**The 7 Layers (verbatim):**

| Layer | Name | Brief Description |
|-------|------|-------------------|
| 1 | **Foundation Models** | "The core AI model on which an agent is built. This can be a large language model (LLM) or other forms of AI." |
| 2 | **Data Operations** | "Where data is processed, prepared, and stored for the AI agents, including databases, vector stores, RAG pipelines, and more." |
| 3 | **Agent Frameworks** | "The frameworks used to build the AI agents, for example toolkits for conversational AI, or frameworks that integrate data." |
| 4 | **Deployment and Infrastructure** | "The infrastructure on which the AI agents run (e.g., cloud, on-premise)." |
| 5 | **Evaluation and Observability** | "How AI agents are evaluated and monitored, including tools and processes for tracking performance and detecting anomalies." |
| 6 | **Security and Compliance** | "(Vertical Layer) Cuts across all other layers, ensuring that security and compliance controls are integrated into all AI agent operations." |
| 7 | **Agent Ecosystem** | "The marketplace where AI agents interface with real-world applications and users... from intelligent customer service platforms to sophisticated enterprise automation solutions." |

**On cross-layer threat chaining** (from the 2026 CI/CD follow-up, Steven Leath & Ken Huang, https://cloudsecurityalliance.org/blog/2026/02/11/applying-maestro-to-real-world-agentic-ai-threat-models-from-framework-to-ci-cd-pipeline):
> "STRIDE is effective at describing what can go wrong at a specific component or boundary. MAESTRO explains how agentic AI behaviors — planning, tool use, memory, and autonomy — create entirely new ways for things to go wrong *across* components, over time, and at system scale."

---

## 2. Agent Harness Paradigm (Substack Series)

**Source:** Ken Huang, "Chapter 1: The Harness Paradigm (Claude Code vs. Hermes Agent)," Substack, 18 Apr 2026  
**URL:** https://kenhuangus.substack.com/p/chapter-1-the-harness-paradigm-claude  
**What it is:** Structural comparison of Claude Code's TypeScript harness and Hermes's Python harness, using MAESTRO as the analytical frame. *Hermes is explicitly one of the two subject systems.*

**Core definition:**
> "the harness paradigm is the foundational insight of production AI engineering: the model provides intelligence, but the harness provides control. A raw language model is a text generator — powerful but undirected, capable but unsafe. The harness is the infrastructure layer that wraps the model and transforms it into a controllable, auditable, production-ready agent."

**Tool interface with `isDestructive` (verbatim code):**
```typescript
// src/Tool.ts
export type Tool<Input extends AnyObject = AnyObject, Output = unknown> = {
  readonly name: string
  call(args, context, canUseTool, ...): Promise<ToolResult<Output>>
  readonly inputSchema: Input          // Zod schema — validated before call()
  isConcurrencySafe(input): boolean
  isReadOnly(input): boolean           // Safe to auto-approve?
  isDestructive?(input): boolean       // Requires explicit user consent?
  checkPermissions(input, context): Promise<PermissionResult>
  maxResultSizeChars: number
}
```

**Destructive gating pattern** (also in Chapter 1 original, https://kenhuangus.substack.com/p/found-from-claude-code-chapter-1):
> "With a harness, the request is intercepted. The harness checks whether the user has permission to perform destructive operations, whether the command matches any safety rules, and whether there are alternative approaches that achieve the same goal without destruction. The harness might surface this decision to the user for approval, or it might automatically redirect the agent toward a safer approach."

**Permission modes** (Chapter 4, https://kenhuangus.substack.com/p/chapter-4-permission-systems-and):
```typescript
export type PermissionMode =
  | 'default'      // Ask before any potentially dangerous operation
  | 'auto'         // Classifier decides; no user interaction (headless/batch)
  | 'plan'         // User approves high-level plan first
  | 'acceptEdits'  // Auto-approve safe file edits; still ask about destructive ops
  | 'bubble'       // Subagent mode — inherit parent's permission context
```
> "`bubble` ensures subagents cannot exceed the permissions of their parent — a critical safety property in multi-agent systems."

**Hermes dangerous patterns — verbatim implementation** (Chapter 4):
```python
# hermes-agent/tools/approval.py
DANGEROUS_PATTERNS = [
    (r'\brm\s+-[^\s]*r', "recursive delete"),
    (r'\bDROP\s+(TABLE|DATABASE)\b', "SQL DROP"),
    (r'\bDELETE\s+FROM\b(?!.*\bWHERE\b)', "SQL DELETE without WHERE"),
    (r'\bTRUNCATE\s+(TABLE)?\s*\w', "SQL TRUNCATE"),
    (r':\(\)\s*\{\s*:\s*\|\s*:\s*&\s*\}\s*;\s*:', "fork bomb"),
    (r'\b(curl|wget)\b.*\|\s*(ba)?sh\b', "pipe remote content to shell"),
    (r'\b(pkill|killall)\b.*\b(hermes|gateway|cli\.py)\b', "kill hermes/gateway process"),
    # ... 30+ more patterns
]
```

**Hook-based pre-execution gating** (Chapter 11, https://kenhuangus.substack.com/p/chapter-11-hook-event-driven-automation):
```json
{
  "id": "block-rm-rf",
  "eventType": "preToolUse",
  "hookAction": "askAgent",
  "toolTypes": "shell",
  "outputPrompt": "If it contains 'rm -rf', 'DROP TABLE', or 'format', respond with BLOCK."
}
```
> "This is the harness-level equivalent of a firewall rule — the agent cannot bypass it because the check happens in the harness, not in the tool itself."

---

## 3. Intent-Based Access Control (IBAC)

**Source:** Ken Huang, "Intent‑Based Access Control: A Technical Primer," Substack, 25 Mar 2026  
**URL:** https://kenhuangus.substack.com/p/intentbased-access-control-a-technical  
**What it is:** Ken Huang's primary exposition of IBAC — the authorization paradigm for agentic systems. Names Cedar, OPA, and OpenFGA as evaluation engines.

> "Intent‑Based Access Control (IBAC) is not just 'ABAC with a buzzword.' It's a shift from 'who can do what' to 'for what purpose, under what conditions, and across which resources.' Roughly, IBAC turns: subject:role → subject:task → action:resource#constraints"

**Runtime flow:**
> "User → Intent parser → Intent(task='xxx', scope=[…], constraints={…}) → Policy mapper → ['tool:query_db#table:patients', 'tool:send_email#channel:internal'] → Agent → Tool calls → Gateway → Authorization engine → DENY / ALLOW for each tuple."

*Note: The post specifies Cedar/OPA/OpenFGA as engines but does not publish a verbatim Cedar policy block. The canonical tuple form is `tool:read#db:patients[pii=true]`.*

---

## 4. ACNBP — Agent Capability Negotiation and Binding Protocol

**Source:** Ken Huang, Akram Sheriff, Vineeth Sai Narajala, Idan Habler, arXiv:2506.13590, 16 Jun 2025  
**URL:** https://arxiv.org/abs/2506.13590  
**What it is:** Formal academic paper specifying a 10-step cryptographic binding protocol for agent-to-agent capability negotiation in heterogeneous multi-agent systems. Validated against MAESTRO.

> "ACNBP... facilitate[s] secure, efficient, and verifiable interactions between agents... through integration with an Agent Name Service (ANS) infrastructure that provides comprehensive discovery, negotiation, and binding mechanisms... digital signatures, capability attestation, and comprehensive threat mitigation strategies."
>
> "Verifiable Capability Binding: The protocol creates legally and cryptographically binding commitments between agents, ensuring accountability and enabling dispute resolution through immutable audit trails."

Reference implementation: https://github.com/appsec2008/ACNBP

---

## 5. OWASP Agentic Skills Top 10

**Source:** Ken Huang (Project Lead), OWASP Agentic Skills Top 10, 2026  
**URL:** https://owasp.org/www-project-agentic-skills-top-10/  
**What it is:** OWASP project led by Ken Huang covering the 10 most critical risks in the skill/behavior layer across OpenClaw, Claude Code, Cursor, and VS Code platforms.

> "Unlike MCP tools (which define *what* resources and actions are available), skills define *how* to use those tools in sequence to accomplish user goals. This behavioral abstraction layer creates unique security challenges that cannot be addressed by securing either the model or the protocol layer alone."

**"Lethal Trifecta":**
> "An AI agent skill is especially dangerous when it simultaneously has: 1. Access to private data 2. Exposure to untrusted content 3. Ability to communicate externally"

**Top 10 summary:** AST01 Malicious Skills (Critical) → AST02 Supply Chain (Critical) → AST03 Over-Privileged (High) → AST04 Insecure Metadata (High) → AST05 Unsafe Deserialization (High) → AST06 Weak Isolation (High) → AST07 Update Drift (Medium) → AST08 Poor Scanning (Medium) → AST09 No Governance (Medium) → AST10 Cross-Platform Reuse (Medium).

*OpenClaw's SKILL.md is one of the four reference platforms in the project's scope table.*

---

## OPINION — Fit for Amplified Partners (OpenClaw + Hermes)

**⚠️ Everything in this section is opinion. No source claims are made.**

**[OPINION]** Ken Huang's Substack series uses Hermes as an explicit comparison system. This means the threat taxonomy and the harness pattern descriptions were written with Hermes's design in mind — the fit is unusually direct.

**Already covered:**  
**[OPINION]** Hermes's `DANGEROUS_PATTERNS` in `approval.py` implements MAESTRO Layer 4/6 destructive gating. The `bubble` permission mode (subagent permission inheritance) addresses the multi-agent escalation risk MAESTRO Layer 3 flags. OpenClaw's SKILL.md is explicitly the reference format for OWASP AST10, meaning the skill manifest already embeds the fields the framework recommends.

**What's thin:**  
**[OPINION]** MAESTRO Layer 5 (Evaluation and Observability) is the most likely gap in a privacy-first, low-staffing deployment. A "step-away owner" architecture needs automated anomaly detection precisely because the human is not watching. This is the highest-value addition that isn't yet visible in the published Hermes patterns.

**[OPINION]** IBAC as Ken Huang specifies it (Cedar/OPA/OpenFGA) is more powerful than a closed single-operator stack requires. The intent-tuple model (`task → action:resource#constraints`) is the useful abstraction; a 50-line Python dict checked at the Hermes gateway achieves equivalent coverage for a closed advisory system without the engine overhead.

**What would be bloat:**  
**[OPINION]** ACNBP's full 10-step cryptographic binding protocol is designed for open heterogeneous agent markets. In a closed 32-repo stack where the operator controls all agents, simple gateway allow-listing is equivalent and vastly cheaper to maintain. Importing ACNBP would add DID/VC infrastructure that solves a discovery-and-trust problem the architecture doesn't have.

**[OPINION]** OWASP AST10's Merkle-root signing and registry transparency (AST01/AST02 mitigations) are meaningful when skills are externally distributed. Until Amplified Partners externalises skills, these controls are pre-emptive overhead.

---

*— Cassian-research-subagent*  
*Timestamp: 2026-06-28T00:00:00Z*

**Primary sources:**
- https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro
- https://cloudsecurityalliance.org/blog/2026/02/11/applying-maestro-to-real-world-agentic-ai-threat-models-from-framework-to-ci-cd-pipeline
- https://labs.cloudsecurityalliance.org/maestro/
- https://kenhuangus.substack.com/p/chapter-1-the-harness-paradigm-claude
- https://kenhuangus.substack.com/p/found-from-claude-code-chapter-1
- https://kenhuangus.substack.com/p/chapter-4-permission-systems-and
- https://kenhuangus.substack.com/p/chapter-11-hook-event-driven-automation
- https://kenhuangus.substack.com/p/intentbased-access-control-a-technical
- https://kenhuangus.substack.com/p/moltbookthreat-modeling-report
- https://kenhuangus.substack.com/p/from-oslo-to-action-how-the-owasp-ceb
- https://owasp.org/www-project-agentic-skills-top-10/
- https://arxiv.org/abs/2506.13590
- https://arxiv.org/abs/2505.19301
