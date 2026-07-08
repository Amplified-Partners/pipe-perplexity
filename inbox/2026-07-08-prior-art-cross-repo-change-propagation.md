# Prior art — cross-repo change propagation

**Research question:** What is the prior art for automatically updating dependent code when linked code changes — consumer-driven contract testing, SemVer-aware automation, monorepo vs polyrepo trade-offs, Dependabot/Renovate for internal packages, GitHub `repository_dispatch`/reusable-workflow fan-out, and additive-vs-breaking API evolution rules — and how does it map to the estate's cross-repo propagation plan?

**Type:** Prior-art / "shoulders of giants" survey. Internet research pass.
**Relates to:** the 40+-repo estate; `.github` org-wide config + reusable workflows (Five Rods, deployment-truth); the propagation plan for keeping dependent repos in sync when a linked repo changes.

---

## What was already known (existing estate prior art — do not re-litigate)

- `inbox/2026-05-04-github-mastery-research.md` (Devon-77fb) — **already** covers org-wide Copilot instructions, branch protection across all repos, and **standardising Dependabot + auto-merge** (minor/patch auto-merge, major to human). This file **builds on** that: it does not re-recommend Dependabot adoption, it addresses the harder problem the mastery file left open — propagating *internal* changes across repos, not just bumping external deps.
- `.github` knowledge note: the org already runs **reusable workflows** (`five-rods-review.yml`, `deployment-truth-reusable.yml`) and cascading-default config across ~38 repos. That fan-out mechanism is taken as given.

**What is new in this file:** contract testing (Pact), SemVer's additive/breaking rule as the *contract* for propagation, monorepo-vs-polyrepo tooling (Nx/Turborepo/Bazel/Lerna), Renovate's explicit *internal-package* support, and `repository_dispatch` as the push-based fan-out primitive.

---

## Key findings (with citations)

### 1. SemVer — the contract that makes propagation safe or unsafe
- Semantic Versioning 2.0.0: MAJOR = "incompatible API changes," MINOR = "add functionality in a backward compatible manner," PATCH = "backward compatible bug fixes." "Once a versioned package has been released, the contents of that version MUST NOT be modified." Sources: https://semver.org/spec/v2.0.0.html ; https://github.com/semver/semver/blob/master/semver.md (confidence: high, primary spec).
- **This is the linchpin for auto-propagation:** additive (MINOR/PATCH) changes are safe to auto-merge downstream; breaking (MAJOR) changes must not be auto-propagated — they require human review. This maps *exactly* onto the estate's existing "additive vs. breaking" / additive-only posture (Vellum AdditiveGuard, "don't silently rewrite history"). SemVer is the version-space encoding of the estate's additive-only principle.

### 2. Consumer-driven contract testing (Pact) — catch breakage before it propagates
- Pact: "the API `Consumer` writes a test to set out its assumptions and needs of its API `Provider`(s)… it will produce a `contract` that we can share to our `Provider` to confirm these assumptions and prevent breaking changes." Lifecycle: consumer unit-tests against a Pact mock → contract JSON → published to a broker → provider replays it. Sources: https://docs.pact.io/consumer ; https://docs.pact.io/implementation_guides/javascript/docs/consumer (confidence: high, primary docs).
- Design wisdom worth keeping: "The art of writing good consumer Pact tests is mostly about knowing what **not** to test… Your Pact tests should be as loose as they possibly can be, while still ensuring the provider can't make changes that break the consumer." (docs.pact.io/consumer). This is the anti-bloat principle applied to contracts.
- Relevance: the estate has many internal producer→consumer links (CRM→Brain, Brain→Machine, Vellum ingest connectors). Contract tests convert "will this change break a downstream repo?" from a guess into a CI check on the *producer's* PR.

### 3. Monorepo vs polyrepo — the affected-graph is the reusable idea
- The estate is **polyrepo** (40+ repos). The monorepo tools are cited not to argue for consolidation but for their **dependency-graph / affected-detection** algorithms, which are the reusable prior art:
  - **Nx**: "determines the minimum set of projects that are affected by the change and only runs tasks on those affected projects." https://nx.dev/docs/features/ci-features/affected ; Nx vs Turborepo https://nx.dev/docs/guides/adopting-nx/nx-vs-turborepo (confidence: high, primary).
  - **Turborepo**: models the repo as a **DAG** (nodes = tasks, edges = dependencies) and derives the package graph from installed internal packages. https://turborepo.dev/docs/core-concepts/package-and-task-graph (confidence: high, primary).
  - Bazel/Lerna occupy the same space (build-graph / publish-orchestration). (confidence: medium — not separately fetched this pass; well-established.)
- Takeaway: whether mono or poly, propagation needs a **dependency graph of which repo consumes which** + affected detection. The estate does not appear to have this graph explicitly — building it is the precondition for any smart propagation. (**OPINION 88%**.)

### 4. Renovate / Dependabot — automation already handles the *internal* case
- Renovate explicitly supports internal dependencies: "Renovate finds and updates internal dependencies just like external or Open Source dependencies," with automerge "really useful for internal dependencies where you can say 'if it passes tests let's merge it.'" Sources: https://github.com/renovatebot/renovate/blob/main/docs/usage/getting-started/use-cases.md ; https://github.com/renovatebot/renovate (confidence: high, primary docs). Private-package lookups need `hostRules` credentials: https://docs.renovatebot.com/getting-started/private-packages/.
- This is the **pull-based** propagation model: downstream repos pull new upstream versions via bot PRs, gated by their own CI. It composes with SemVer (auto-merge MINOR/PATCH, hold MAJOR).

### 5. `repository_dispatch` / reusable workflows — the *push-based* fan-out primitive
- "`workflow_dispatch` is for humans clicking buttons. `repository_dispatch` is for machines calling your workflows from outside GitHub." An upstream repo POSTs to `POST /repos/{owner}/{repo}/dispatches` with an `event_type` + freeform `client_payload`, triggering a downstream workflow. Sources: https://blog.dominicrodemer.com/github-actions-advanced-triggers-and-events/ ; multi-repo pattern https://blog.cloud-eng.nl/2024/04/01/github-actions-mulitrepo/ ; action https://github.com/peter-evans/repository-dispatch (confidence: high — the API is primary GitHub behaviour; blogs are practitioner demos of it).
- This is the **push** counterpart to Renovate's pull: on merge to `main`, an upstream repo fans out a `repository_dispatch` (e.g. `event_type: dependency_updated`) to each dependent repo, which rebuilds/re-tests. The estate already uses reusable workflows, so it has the ingredients.

---

## How it maps to the estate propagation plan

| Prior-art element | Estate component | Mapping |
|---|---|---|
| SemVer additive vs breaking | Additive-only invariant (Vellum, authority docs) | SemVer is the version-number encoding of the estate's existing additive-only rule. Adopt SemVer on internal packages so "additive" is machine-detectable and auto-mergeable. |
| Pact contract tests | CRM→Brain, Brain→Machine, Vellum connectors | Add producer-side contract tests so a breaking change is caught on the *producer's* PR, before it propagates. Highest-value single addition. |
| Nx/Turborepo affected-graph | (missing) org-wide repo dependency graph | Build an explicit "who consumes whom" graph — the precondition for smart propagation. Could live in `.github` or `ground-truth`. |
| Renovate internal packages | Existing Dependabot standardisation (from the mastery file) | Pull-based propagation, SemVer-gated auto-merge. Renovate is the more capable option for internal/private packages specifically. |
| `repository_dispatch` + reusable workflows | Existing `.github` reusable workflows (Five Rods, deployment-truth) | Push-based fan-out on merge. Compose with the Five Rods review so propagated PRs still pass governance. |

---

## Confidence band

- SemVer / Pact / affected-graph / Renovate / `repository_dispatch` as correct prior art: **high (90–95%)** — primary specs and docs.
- "Estate lacks an explicit cross-repo dependency graph and needs one first": **OPINION 88%** (inferred from repo structure; a Devon check could confirm).
- "SemVer is the version encoding of additive-only": **OPINION 90%** (direct logical mapping).
- Push (`repository_dispatch`) vs pull (Renovate) — recommend **both, layered**: **OPINION 80%** (reversible; start with pull, add push where latency matters).

## Recommended next action (for Devon to assess; NOT auto-promoted)

1. **Build the dependency graph first** (Linear, Build/Internals): an explicit machine-readable map of internal producer→consumer links across the 40+ repos. Everything else depends on it.
2. **Add producer-side Pact-style contract tests** to the top 2–3 links (start CRM→Brain). Catch breakage at source.
3. **Adopt SemVer on internal packages** and wire Renovate (pull) with MINOR/PATCH auto-merge + MAJOR-to-human, reusing the existing Five Rods CI gate. Add `repository_dispatch` push fan-out only where propagation latency actually matters.
4. Do **not** consolidate to a monorepo — borrow the affected-graph idea, keep polyrepo (consistent with decentralised-governance prior art and the ESB-antipattern lesson in the shared-bus file).

---

*Devon | 2026-07-08 | session devin-8aa5624849524edaa4556b176bf0df69*
*Research question: prior art for auto-updating dependent code when linked code changes (Pact, SemVer, monorepo/polyrepo tooling, Renovate/Dependabot internal packages, repository_dispatch/reusable-workflow fan-out, additive-vs-breaking API evolution) mapped to the estate cross-repo propagation plan.*
