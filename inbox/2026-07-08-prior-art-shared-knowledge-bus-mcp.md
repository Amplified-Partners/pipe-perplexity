# Prior art — a single shared integration bus that exposes capabilities as tools

**Research question:** What is the prior art for building one shared integration bus that exposes an estate's capabilities to AI agents as callable tools, with tiered access control — and what do the historical failure modes of centralised integration layers tell us about how to build `amplified-knowledge-mcp` so it does not become the next Enterprise Service Bus?

**Type:** Prior-art / "shoulders of giants" survey. Internet research pass.
**Relates to:** `Amplified-Partners/amplified-knowledge-mcp` (16 MCP tools across 3 tiers over PostgreSQL + Apache AGE + pgvector).

---

## What was already known (existing estate prior art — do not re-litigate)

- `inbox/2026-05-04-github-mastery-research.md` (Devon-77fb) — cross-repo GitHub capabilities, org-wide instructions, branch protection. Adjacent, not overlapping: that file is about GitHub-as-control-plane, not about a knowledge/tool bus.
- `inbox/2026-05-04-maestro-and-agent-harnesses.md` (Cassian) — already covers MAESTRO 7-layer threat model, OWASP Agentic Skills Top 10, and the "AI-vs-Python boundary" for security tooling. It already concludes a **50-line Python allow-list at the gateway** beats a full Cedar/OPA/OpenFGA IBAC engine for a closed ~32-repo estate. This file **builds on** that conclusion for the access-control section rather than repeating it.
- Knowledge note *"Canonical Data Architecture"* (Devon-973e, 2026-05-08) — the AGE + pgvector single-engine decision is already locked. Taken as given here.

**What is new in this file:** the ESB failure-mode literature applied specifically to the MCP-bus design, and the MCP tool-annotation vocabulary as a native "risk grammar" the estate is not yet using.

---

## Key findings (with citations)

### 1. MCP is the canonical "capabilities-as-tools over one protocol" design
- Anthropic introduced the Model Context Protocol on **2024-11-25** as "a universal, open standard for connecting AI systems with data sources, replacing fragmented integrations with a single protocol." Client–server architecture; servers expose data/tools, clients (models) consume them. Source: Anthropic, "Introducing the Model Context Protocol," 2024-11-25 — https://www.anthropic.com/news/model-context-protocol (confidence: high, primary source).
- The explicit problem statement MCP was built for is the estate's exact problem: "Every new data source requires its own custom implementation, making truly connected systems difficult to scale." Same source. Corroborated by InfoWorld 2024-11-27 (https://www.infoworld.com/article/3613143/anthropic-introduces-the-model-context-protocol.html) and InfoQ 2024-12-01 (https://www.infoq.com/news/2024/12/anthropic-model-context-protocol/).

### 2. MCP already has a native "risk vocabulary" for tools — the estate should adopt it
- Tool annotations shipped in the **`2025-03-26`** spec revision. The `ToolAnnotations` interface is: `readOnlyHint` (default false), `destructiveHint` (default true), `idempotentHint` (default false), `openWorldHint` (default true). Source: MCP Blog, "Tool Annotations as Risk Vocabulary," 2026-03-16 — https://blog.modelcontextprotocol.io/posts/2026-03-16-tool-annotations/ (confidence: high, primary/official blog). Schema mirrored in rust-mcp-schema (protocol `2025-11-25`): https://docs.rs/rust-mcp-schema/latest/rust_mcp_schema/struct.ToolAnnotations.html.
- **Critical caveat, load-bearing:** "all properties in ToolAnnotations are hints… Clients should never make tool use decisions based on ToolAnnotations received from untrusted servers." (same sources). Annotations inform a *preflight confirmation* decision; they are **not** an enforcement boundary. Enforcement must live server-side.
- `destructiveHint` maps exactly to the estate's **additive-only** posture (Vellum's AdditiveGuard, "don't silently rewrite history"): a tool whose `destructiveHint=false` is, in MCP terms, an additive tool.

### 3. The Enterprise Service Bus is the cautionary prior art — centralisation's failure modes are well documented
- The ESB "started as integration middleware. Over time, it accumulated business logic… became the most important, most complex, and least-understood component in the enterprise." Source: H. Nejati Javaremi, "ESB: The Good, the Bad, and the Legacy," 2026-03-09 — https://hosseinnejati.medium.com/esb-enterprise-service-bus-the-good-the-bad-and-the-legacy-b88a0bc4536e (confidence: medium — practitioner essay, but consistent with the canonical Fowler/Newman "smart endpoints, dumb pipes" position).
- Two named failure modes, directly relevant to an MCP bus:
  1. **Logic creep / gravity well** — "Nobody wanted business logic in the ESB. It migrated there anyway, line by line, as the path of least resistance." (same source).
  2. **Single point of failure / blast radius** — "A misconfigured route, a memory leak, or a bug in a transformation rule could cascade to every system connected to the bus." (same source).
- Microservices arose *as an explicit ESB antipattern reaction*: "smart endpoints and dumb pipes," decentralised governance, componentisation via business capability. Source: Perforce/Akana, "ESB vs. Microservices" — https://www.perforce.com/blog/aka/esb-vs-microservices (confidence: medium).

### 4. API gateway / BFF — the "one bus vs. one surface per consumer" trade-off
- Backend-for-Frontend (Sam Newman): "rather than have a general-purpose API backend, instead you have one backend per user experience." Source: https://samnewman.io/patterns/architectural/bff/ (confidence: high, canonical author). Microsoft's restatement: a BFF sits between client and backend, tailored per interface — https://learn.microsoft.com/en-us/azure/architecture/patterns/backends-for-frontends.
- BFF and API gateway are **complementary, not competing** — gateway does cross-cutting concerns (auth, routing, rate limits), BFF tailors payloads per consumer. Source: apidog, "BFF vs API Gateway," 2026-07-02 — https://apidog.com/blog/bff-vs-api-gateway/ (confidence: medium).
- Newman's own caution maps to the ESB gravity-well: "the more types of clients you have using a single BFF, the more temptation there may be for it to become bloated by handling multiple concerns" (samnewman.io). This is the tiered-MCP-server design's risk: the ADMIN tier is where logic creep will start.

### 5. Tiered access control — RBAC vs ABAC
- NIST SP 800-162 defines ABAC: "authorization to perform a set of operations is determined by evaluating attributes associated with the subject, object, requested operations, and… environment conditions against policy." Source: NIST SP 800-162 (2014, updated 2019-08-02) — https://csrc.nist.gov/pubs/sp/800/162/upd2/final (confidence: high, primary standard).
- The `amplified-knowledge-mcp` model today is **RBAC** by tier (READONLY / READWRITE / ADMIN via `TIER` env var), which the MAESTRO file already argued is right-sized for a closed estate. ABAC is the growth path *only if* per-agent/per-graph/per-document conditions become load-bearing (e.g. a client-scoped agent that may read only its own tenant's subgraph). Confidence 80% that RBAC-by-tier remains sufficient until per-client agent deployment; then a single ABAC condition (tenant attribute on subject + object) is the minimal upgrade — do not adopt a full policy engine pre-emptively (consistent with the MAESTRO file's anti-bloat call).

---

## How it maps to `amplified-knowledge-mcp`

| Prior-art element | Estate component | Mapping |
|---|---|---|
| MCP protocol | The whole server | Already the chosen substrate — this is "standing on Anthropic's shoulders" literally. |
| `readOnlyHint` / `destructiveHint` / `idempotentHint` | The 16 tools across Tier 1/2/3 | **Gap:** tools are tier-gated but do not appear to carry MCP annotations. Tier 1 tools are `readOnlyHint=true`; Tier 2 (`ingest/update/tag/flag`) are `readOnlyHint=false, destructiveHint=false` (additive); Tier 3 `archive` is the only `destructiveHint=true`; `audit_log` is `readOnlyHint=true`. Annotating them makes the additive-only invariant machine-readable. |
| ESB logic-creep failure mode | `security.py` (Cypher validation) + tier gating | Keep the bus a "dumb pipe": validation + access, no business logic. Watch the ADMIN tier — `promote_document` is the most likely place for logic to accrete. |
| ESB blast-radius failure mode | Single server over single `amplified_brain` DB | The bus is a single point of failure by construction. Mitigation is the existing per-tool `audit.log_operation` + tier isolation, not decentralisation (a 3-repo estate does not warrant microservice fan-out). |
| NIST ABAC | `config.Tier` enum | RBAC-by-tier now; ABAC only when per-tenant scoping arrives. |

---

## Confidence band

- MCP as the correct bus substrate: **PROVEN-adjacent / high (95%)** — it is already adopted, and the primary sources confirm the design intent matches the estate's need.
- Adopt MCP tool annotations as a machine-readable additive-only/destructive vocabulary: **OPINION 88%** (reversible, low cost, aligns with existing AdditiveGuard philosophy).
- Keep the bus a dumb pipe / resist ADMIN-tier logic creep: **OPINION 85%** — the ESB literature is practitioner-grade, not peer-reviewed, but the failure mode is consistently reported across decades.
- Defer ABAC/policy-engine adoption: **OPINION 80%** (consistent with the prior MAESTRO conclusion).

## Recommended next action (for Devon to assess; NOT auto-promoted)

1. File a Linear issue under **Build** proposing MCP `ToolAnnotations` on all 16 tools in `server.py`, with a one-line mapping table (readOnly/destructive/idempotent per tool). Low effort, additive, makes the additive-only guarantee legible to any MCP client.
2. Add an "ADMIN-tier logic budget" note to the repo's `AGENTS.md` (or CI review criteria): the bus validates and gates; it does not compute. Cite the ESB gravity-well as the rationale.
3. Park ABAC — revisit only when the first per-client agent needs tenant-scoped subgraph access.

---

*Devon | 2026-07-08 | session devin-8aa5624849524edaa4556b176bf0df69*
*Research question: prior art for a single shared MCP integration bus exposing estate capabilities as tiered tools, and how ESB/BFF/RBAC-ABAC history should shape `amplified-knowledge-mcp`.*
