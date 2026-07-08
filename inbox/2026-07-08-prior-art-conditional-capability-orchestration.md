# Prior art — conditional capability orchestration

**Research question:** What is the prior art for turning capabilities into conditionally-fired options — feature-flag systems, workflow orchestration with optional/idempotent steps, saga/compensation patterns, and capability registries with dependency ordering — and how does it map to the CRM `FeatureRegistry`/`FEATURE_CATALOG` and the Temporal `APDSIngestionWorkflow`?

**Type:** Prior-art / "shoulders of giants" survey. Internet research pass.
**Relates to:** `product-crm` `app/intelligence/core/feature_registry.py` (`FEATURE_CATALOG`, `FeatureRegistry`, `FeatureDefinition.requires`); Temporal `APDSIngestionWorkflow`.

---

## What was already known (existing estate prior art — do not re-litigate)

- `inbox/2026-05-04-compound-engineering-current-state.md` and `..._maestro-and-agent-harnesses.md` — orchestration of *agents* and review loops (Plan→Work→Review→Compound; Hermes manager-worker). Adjacent: those are agent-orchestration; this file is *capability/feature* orchestration.
- The CRM already implements the pattern in code: `FEATURE_CATALOG` is a dict of `FeatureDefinition`s, each with `schedule` (`daily`/`weekly`/`monthly`/`event`/`continuous`), `default_config`, and a **`requires: List[str]`** dependency field (e.g. `cash_flow_predictor` and `service_reminder` both `requires=['clv_tracker']`). `FeatureRegistry.is_enabled(tenant, feature)` gates per-tenant. This is the estate's home-grown feature-flag + capability-registry system — the point of this file is to attribute the pattern and flag the gaps, not to invent it.

**What is new in this file:** the external prior art (OpenFeature/LaunchDarkly/Unleash, Temporal/Airflow/Dagster, saga/García-Molina) that the CRM's design independently rediscovered, and the specific gaps that prior art exposes.

---

## Key findings (with citations)

### 1. Feature-flag systems — the "capability as a conditionally-fired option" pattern
- **OpenFeature (CNCF, incubating since 2023-12-19)** — "a vendor-agnostic, community-driven API for feature flagging." Design principles: vendor/language agnosticism, low/no dependency, extensibility; the SDK "provides a mechanism for interfacing with an external evaluation engine… it does **not** itself handle the flag evaluation logic." Sources: https://openfeature.dev/ ; https://github.com/open-feature/spec ; https://www.cncf.io/blog/2023/12/19/openfeature-becomes-a-cncf-incubating-project/ (confidence: high, primary). Key idea for the estate: **separate the flag API from the evaluation engine** — the CRM's `FeatureRegistry` is both today.
- **LaunchDarkly / Unleash** — mature managed/OSS flag platforms. Relevant capabilities beyond a boolean: targeting/segments, progressive/gradual rollouts, kill switches, automated rollbacks, audit logs, RBAC, change requests. Sources: https://launchdarkly.com/ ; https://www.getunleash.io/ (confidence: medium — vendor marketing, but capability lists are standard). Unleash is the ThoughtWorks-Radar-recommended OSS option and self-hostable via Docker (getunleash.io).

### 2. Workflow orchestration with optional / idempotent steps
- **Temporal** — durable execution. "Workflows are resilient… If the application itself crashes, Temporal will automatically recreate its pre-failure state." Activities encapsulate failure-prone business logic with automatic retries. Sources: https://docs.temporal.io/workflows ; https://docs.temporal.io/activity-definition (confidence: high, primary).
- **Idempotency is the load-bearing rule** for optional/retried steps: "Temporal recommends that Activities be idempotent… Activities may be retried, these functions may be executed more than once." Design guidance: make activities *granular* so only the failed step re-runs. Sources: https://docs.temporal.io/activity-definition ; https://temporal.io/blog/idempotency-and-durable-execution (2024-02-27) (confidence: high, primary). Temporal guarantees **at-least-once** execution — hence idempotency is mandatory, not optional.
- **Airflow → Dagster** — the industry has moved from task-DAGs (Airflow, XCom for data handoff) to **software-defined assets** (Dagster: "Tasks become assets… XCom becomes `deps`," which "declare execution order, not data transfer," plus materialization history and **staleness tracking**). Source: https://github.com/dagster-io/dagster/blob/master/docs/docs/migration/airflow-to-dagster/basic-migration.md (confidence: high, primary docs). Staleness tracking is the interesting prior art: an asset (capability output) knows when its upstreams changed and it needs re-materialising — directly relevant to "auto-update dependent outputs" (see the cross-repo-propagation file).

### 3. Saga / compensation — how to make a multi-step capability safely reversible
- Sagas (García-Molina & Salem, ACM SIGMOD 1987): a long-lived transaction written as a sequence of sub-transactions, each with a **compensating transaction** `C_i` that "undoes, from a semantic point of view, any of the actions performed by `T_i`." Guarantee: either `T_1…T_n` all complete, or `T_1…T_j` run followed by `C_j…C_1`. Sources: https://doi.org/10.1145/38714.38742 ; PDF https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf (confidence: high, primary/seminal paper). Modern restatement (forward recovery via idempotent retry vs backward recovery via compensation): https://jurf.github.io/daap/consistency-patterns/saga/.
- Relevance: a conditionally-fired capability that writes across CRM + Brain + Vellum is a distributed transaction. If two-phase commit is not an option (it is not, across these services), the saga pattern is the prior art for keeping it consistent — compensations, not locks.

### 4. Capability registries + dependency ordering
- The CRM's `FeatureDefinition.requires` is a **dependency-ordering DAG** — the same structure as Turborepo's task graph and Dagster's asset `deps` (both are DAGs where an edge means "must run/exist first"). Sources (for the DAG-ordering concept): Turborepo package/task graph https://turborepo.dev/docs/core-concepts/package-and-task-graph ; Dagster `deps` (above). (confidence: high that the structural analogy holds.) The prior art warns of one thing the CRM must enforce: **no cycles**, and **enable-order = topological order** (you cannot enable `cash_flow_predictor` before `clv_tracker`).

---

## How it maps to the CRM + APDS

| Prior-art element | Estate component | Mapping / gap |
|---|---|---|
| OpenFeature "flag API separate from evaluation engine" | `FeatureRegistry` | Registry currently *is* both catalog and evaluator. Fine at this scale; OpenFeature is the growth path if flags ever need external targeting/rollout. **OPINION 82%: do not adopt yet** (anti-bloat, consistent with the MAESTRO AI-vs-Python-boundary call). |
| LaunchDarkly/Unleash gradual rollout + kill switch | `FeatureRegistry.is_enabled(tenant, feature)` | The per-tenant boolean is a kill switch. Gradual rollout (% of tenants) is a small additive enhancement if client onboarding needs it. |
| Temporal idempotent activities | `APDSIngestionWorkflow` | **Load-bearing check:** every ingestion activity (Harvest→Extract→Label→Match→Score) must be idempotent given at-least-once execution. Verify each stage can re-run without double-writing to the Brain. |
| Dagster staleness tracking | Feature outputs / APDS recipes | Prior art for "this capability's output is stale because an upstream changed" — pairs with the cross-repo-propagation file. |
| Saga compensation (García-Molina 1987) | Any capability writing across CRM+Brain+Vellum | Additive-only ledgers (Vellum) simplify compensation: an additive write's compensation is another additive entry, never a destructive undo. This is a genuine estate advantage — worth documenting. |
| `requires` DAG / topological enable-order | `FeatureDefinition.requires` | Verify the registry rejects cycles and enforces enable-order (enabling a feature auto-enables/what-checks its `requires`). |

---

## Confidence band

- Feature-flag / Temporal / saga / DAG-ordering as correct prior art for the CRM design: **high (90%)** — mostly primary sources; the CRM code independently matches the patterns.
- "Additive-only ledger makes saga compensation trivial" observation: **OPINION 85%** (follows directly from the additive-only invariant, but not externally validated).
- "Don't adopt OpenFeature/LaunchDarkly yet": **OPINION 82%** (reversible; anti-bloat).

## Recommended next action (for Devon to assess; NOT auto-promoted)

1. **Idempotency audit of `APDSIngestionWorkflow`** (Linear, Build): confirm each of Harvest→Extract→Label→Match→Score is idempotent under Temporal at-least-once retries; add dedupe keys where missing (Vellum already uses SHA-256 dedupe keys — reuse that pattern).
2. **Cycle/enable-order check** on `FeatureRegistry`: ensure `requires` is validated as an acyclic DAG and enabling a feature verifies its dependencies are enabled first.
3. Add a short `clean-build` authority note (via PR) attributing the CRM feature system to the feature-flag + capability-registry + saga prior art, and recording the "additive ledgers simplify compensation" advantage.

---

*Devon | 2026-07-08 | session devin-8aa5624849524edaa4556b176bf0df69*
*Research question: prior art for conditional capability orchestration (feature flags, Temporal/Airflow/Dagster, saga/compensation, capability registries with dependency ordering) mapped to the CRM FeatureRegistry/FEATURE_CATALOG and Temporal APDSIngestionWorkflow.*
