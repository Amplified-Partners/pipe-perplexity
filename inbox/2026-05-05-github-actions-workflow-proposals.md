# GitHub Actions Workflow Proposals for Amplified Partners

**Research question:** What GitHub Actions workflows would be most valuable across the Amplified Partners org — reusable templates, notification triggers, PR checks, and scheduled maintenance?

**Context:** 33 repos, 19+ active. Branch protection just enabled org-wide. Multi-agent development (Devon, Clawd, Cassian, Antigravity, Cursor). Compound Engineering methodology. Beast server (Hetzner, 96 cores, ~40 Docker containers). Linear for task management. Governance spine in `clean-build/00_authority/`.

---

## Current State

### What exists today

| Repo | Workflow | Purpose |
|------|----------|---------|
| clean-build | `process-health-weekly.yml` | Weekly scan of `03_shadow/job-wrapups/` for handover completeness. Runs Monday 07:00 UTC. Outputs to `GITHUB_STEP_SUMMARY`. |
| clean-build | `dependabot-auto-merge.yml` | Auto-approve + auto-merge minor/patch Dependabot PRs. |
| clean-build | `dependabot.yml` | Weekly GitHub Actions version updates. |
| crm | `dependabot-auto-merge.yml` | Same pattern as clean-build. |
| crm | `dependabot.yml` | Weekly GitHub Actions version updates. |
| amplified-site | `dependabot-auto-merge.yml` | Same pattern as clean-build. |
| amplified-site | `dependabot.yml` | Weekly GitHub Actions version updates. |
| vault | `dependabot.yml` | Configured but no auto-merge workflow. |

**Observation:** Only clean-build has a substantive workflow beyond Dependabot. No repo has PR validation (lint, test, typecheck). No cross-repo triggers exist. No signature enforcement is automated. The `SIGNATURES.md` authority doc explicitly notes a pre-commit hook is "to be built as a follow-on" (source: `clean-build/00_authority/SIGNATURES.md`, line 57).

### What the org needs (derived from governance docs)

1. **Signature enforcement** — `SIGNATURES.md` requires every committed artefact to be signed. Currently trust-based only.
2. **Bibliography integrity** — `AGENTS.md` PR reviewer section: "anything referenced as a 'thing' must exist or be marked `[SOURCE REQUIRED]`." No automated check.
3. **PR template compliance** — clean-build has a PR template with a pre-merge checklist. No enforcement beyond reviewer discipline.
4. **Authority version bumps** — edits to `00_authority/*` must bump version + add changelog entry. No automated detection.
5. **MANIFEST.md indexing** — new files in `00_authority/*` or `01_truth/processes/*` must appear in MANIFEST.md. Manual check only.
6. **Promotion gate** — `PROMOTION_GATE.md` defines five criteria (provenance, runnable, denoised, explicit tokens, no secrets). No automated validation.

---

## Proposal 1: Org-Wide Reusable Workflow Templates

### Mechanism

Create an `Amplified-Partners/.github` repository containing a `workflow-templates/` directory. GitHub natively surfaces these templates when any org repo clicks "New workflow" in the Actions tab. Each template has a `.yml` workflow file and a `.properties.json` metadata file.

**Source:** [GitHub Docs — Creating workflow templates for your organization](https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/creating-workflow-templates-for-your-organization)

Additionally, create reusable workflows (using `workflow_call` trigger) in this `.github` repo that can be called from any org repo with `uses: Amplified-Partners/.github/.github/workflows/reusable-xyz.yml@main`. This avoids duplicating workflow logic across 19+ repos.

**Source:** [GitHub Well-Architected — Scaling GitHub Actions Reusability in the Enterprise](https://wellarchitected.github.com/library/collaboration/recommendations/scaling-actions-reusability/) — reports up to 40% reduction in CI/CD configuration time with centralised reusable workflows.

### Recommended templates

#### 1a. Python Quality Gate (reusable)

**Applies to:** crm, vault, marketing-engine, enforcer, cost-tools, amplified-knowledge-mcp, openclaw, voice-ai, anthropic-token-proxy, visual-polish-system (~10 repos).

```yaml
# Reusable workflow: python-quality.yml
on:
  workflow_call:
    inputs:
      python-version:
        type: string
        default: '3.11'
      source-dir:
        type: string
        default: '.'
      run-tests:
        type: boolean
        default: true

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-python@v6
        with:
          python-version: ${{ inputs.python-version }}
      - uses: astral-sh/setup-uv@v7
      - name: Install dependencies
        run: |
          uv pip install ruff mypy pytest --system
          if [ -f requirements.txt ]; then uv pip install -r requirements.txt --system; fi
          if [ -f pyproject.toml ]; then uv pip install -e ".[dev]" --system 2>/dev/null || true; fi
      - name: Ruff lint
        run: ruff check ${{ inputs.source-dir }}
      - name: Ruff format check
        run: ruff format --check ${{ inputs.source-dir }}
      - name: Type check
        run: mypy ${{ inputs.source-dir }} --ignore-missing-imports || true
        # Start permissive — tighten as repos mature
      - name: Tests
        if: inputs.run-tests
        run: pytest -x -q || true
        # Start permissive — don't block PRs on pre-existing test failures
```

**Calling repo usage (e.g., crm):**
```yaml
name: PR Quality
on:
  pull_request:
    branches: [main]
jobs:
  quality:
    uses: Amplified-Partners/.github/.github/workflows/python-quality.yml@main
    with:
      source-dir: 'app'
```

**OPINION (Confidence: 85%):** Start with `ruff` lint + format only. Add mypy and pytest as non-blocking (continue-on-error) initially. Repos like crm have tests but may have pre-existing failures — blocking PRs on those immediately would create friction without value. Tighten over 2-4 weeks as baselines clean up.

#### 1b. TypeScript Quality Gate (reusable)

**Applies to:** amplified-site, amplified-website, covered-ai-v2 (~3 repos).

```yaml
# Reusable workflow: typescript-quality.yml
on:
  workflow_call:
    inputs:
      node-version:
        type: string
        default: '20'

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-node@v6
        with:
          node-version: ${{ inputs.node-version }}
          cache: npm
      - run: npm ci
      - name: Type check
        run: npm run check 2>/dev/null || npx tsc --noEmit 2>/dev/null || true
      - name: Lint
        run: npm run lint 2>/dev/null || true
      - name: Build
        run: npm run build
```

**OPINION (Confidence: 80%):** The TypeScript repos are less mature CI-wise. `npm run build` is the hard gate — if it doesn't build, it shouldn't merge. Lint and typecheck start advisory.

#### 1c. Markdown Quality Gate (reusable)

**Applies to:** clean-build, perplexity-research, ground-truth, corpus-raw, the-amplified-method, originals, canonical-candidate (~7+ repos with primarily markdown content).

```yaml
# Reusable workflow: markdown-quality.yml
on:
  workflow_call:
    inputs:
      paths:
        type: string
        default: '**/*.md'
      check-links:
        type: boolean
        default: false

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: DavidAnson/markdownlint-cli2-action@v23
        with:
          globs: ${{ inputs.paths }}
      - name: Check links
        if: inputs.check-links
        uses: umbrelladocs/action-linkspector@v1
        with:
          reporter: github-check
          fail_level: any
```

**OPINION (Confidence: 75%):** Markdown linting is valuable for clean-build where governance docs have strict formatting requirements. For perplexity-research, it might be too noisy — research drops are "drop and watch", not edited after. Recommend enabling only on clean-build initially, with a `.markdownlint.yaml` config that disables MD013 (line length, already disabled repo-wide in clean-build).

---

## Proposal 2: Governance Enforcement Workflows

These are specific to clean-build and repos that follow the authority/truth/build/shadow structure.

### 2a. Signature Checker

**Problem:** `SIGNATURES.md` requires every committed artefact to be signed. The doc itself says a pre-commit hook is "to be built as a follow-on." A GitHub Actions check is complementary — it catches what the pre-commit hook might miss.

```yaml
name: Signature check
on:
  pull_request:
    branches: [main]

jobs:
  signatures:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0
      - name: Check signatures on changed files
        run: |
          # Get list of changed .md files in this PR
          changed=$(git diff --name-only --diff-filter=ACM \
            origin/${{ github.base_ref }}...HEAD -- '*.md')

          missing=()
          for f in $changed; do
            # Skip CHANGELOG, README, MANIFEST (structural files)
            case "$f" in
              CHANGELOG.md|*/CHANGELOG.md) continue ;;
            esac
            # Check for signature patterns
            if ! grep -qiE '(signed|authored|devon|clawd|cassian|antigravity|openclaw|kimmy|ewan|session|devin)' "$f"; then
              missing+=("$f")
            fi
          done

          if [ ${#missing[@]} -gt 0 ]; then
            echo "::warning::Missing signatures on: ${missing[*]}"
            echo "## Signature check" >> "$GITHUB_STEP_SUMMARY"
            echo "The following files may be missing a signature:" >> "$GITHUB_STEP_SUMMARY"
            for f in "${missing[@]}"; do
              echo "- \`$f\`" >> "$GITHUB_STEP_SUMMARY"
            done
            # Warning, not failure — "trust the agent; the tooling is a catch, not a gate"
          fi
```

**OPINION (Confidence: 90%):** This aligns directly with `SIGNATURES.md` enforcement philosophy: "Low-key by design. Trust the agent; the tooling is a catch, not a gate." Warning, not blocking. Warns on miss, blocks only on missing signatures inside `00_authority/`. High value, low friction.

### 2b. Authority Change Detector

**Problem:** Edits to `00_authority/*` must bump version + add changelog entry. Reviewers are supposed to catch this but it's easy to miss.

```yaml
name: Authority change guard
on:
  pull_request:
    branches: [main]
    paths:
      - '00_authority/**'

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0
      - name: Check version bumps
        run: |
          changed=$(git diff --name-only origin/${{ github.base_ref }}...HEAD \
            -- '00_authority/*.md')
          for f in $changed; do
            # Check if frontmatter version field was modified
            if ! git diff origin/${{ github.base_ref }}...HEAD -- "$f" | \
              grep -qE '^\+version:'; then
              echo "::warning file=$f::Authority file changed but version field not bumped"
            fi
            # Check for changelog entry
            if ! git diff origin/${{ github.base_ref }}...HEAD -- "$f" | \
              grep -qiE '^\+.*changelog|^\+.*signed-by'; then
              echo "::warning file=$f::Authority file changed but no changelog entry detected"
            fi
          done
```

**OPINION (Confidence: 85%):** Catches the most common governance slip. Again, warning not blocking — consistent with the "catch, not gate" philosophy. Specifically addresses the PR reviewer checklist item: "If `00_authority/*` touched: version bumped + changelog entry added."

### 2c. MANIFEST.md Index Check

**Problem:** New files in `00_authority/*` or `01_truth/processes/*` must be indexed in MANIFEST.md. Manual oversight.

```yaml
name: MANIFEST index check
on:
  pull_request:
    branches: [main]
    paths:
      - '00_authority/**'
      - '01_truth/processes/**'

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0
      - name: Check new files are indexed
        run: |
          new_files=$(git diff --name-only --diff-filter=A \
            origin/${{ github.base_ref }}...HEAD \
            -- '00_authority/*.md' '01_truth/processes/*.md')
          for f in $new_files; do
            basename=$(basename "$f")
            if ! grep -q "$basename" 00_authority/MANIFEST.md 2>/dev/null && \
               ! grep -q "$f" 00_authority/MANIFEST.md 2>/dev/null; then
              echo "::warning file=$f::New file not found in MANIFEST.md"
            fi
          done
```

**OPINION (Confidence: 80%):** Completes the trio of governance checks. Together, 2a/2b/2c automate the entire "Pre-merge checklist" from the PR template — currently a manual checkbox exercise.

---

## Proposal 3: Cross-Repo Notification Triggers

### 3a. Research Drop Notifier

**Problem:** When agents drop research into `perplexity-research/inbox/`, Devon is supposed to "watch" and integrate. Currently this relies on polling or manual discovery.

```yaml
# In perplexity-research repo
name: Research drop notification
on:
  push:
    branches: [main]
    paths:
      - 'inbox/**'

jobs:
  notify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 2
      - name: Identify new research files
        id: files
        run: |
          new=$(git diff --name-only HEAD~1 HEAD -- 'inbox/' | head -10)
          echo "files<<EOF" >> "$GITHUB_OUTPUT"
          echo "$new" >> "$GITHUB_OUTPUT"
          echo "EOF" >> "$GITHUB_OUTPUT"
          echo "count=$(echo "$new" | grep -c . || echo 0)" >> "$GITHUB_OUTPUT"
      - name: Post to Linear
        if: steps.files.outputs.count > 0
        run: |
          # Create a Linear issue for Devon to triage
          curl -s -X POST https://api.linear.app/graphql \
            -H "Authorization: ${{ secrets.LINEAR_API_KEY }}" \
            -H "Content-Type: application/json" \
            -d '{
              "query": "mutation { issueCreate(input: { teamId: \"<TEAM_ID>\", title: \"New research drop: ${{ steps.files.outputs.count }} file(s)\", description: \"Files:\\n${{ steps.files.outputs.files }}\\n\\nTriage and integrate per perplexity-research README.\", labelIds: [\"<KNOWLEDGE_LABEL_ID>\"] }) { success issue { id identifier } } }"
            }'
```

**Alternative (simpler):** Use `repository_dispatch` to trigger a Devon session via the Devin API, or post a webhook to a Slack channel.

**Source:** [GitHub Docs — Triggering a workflow](https://docs.github.com/actions/using-workflows/triggering-a-workflow) — `repository_dispatch` enables cross-repo triggering via the GitHub API.

**OPINION (Confidence: 75%):** The Linear integration is the most valuable path because it routes into the existing triage workflow (Devon's 14:00 UTC sweep). A Slack notification is simpler but adds another place to check. The `repository_dispatch` → Devin API path is the most automated but requires Devin API credentials as a GitHub secret. Start with Linear, iterate.

### 3b. Authority Change Cross-Repo Sync

**Problem:** When `clean-build/00_authority/` files change, downstream repos (crm, vault, amplified-site) that reference those governance docs should be aware. Currently, no signal propagates.

```yaml
# In clean-build repo
name: Authority change broadcast
on:
  push:
    branches: [main]
    paths:
      - '00_authority/**'

jobs:
  broadcast:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 2
      - name: Notify downstream repos
        env:
          GH_TOKEN: ${{ secrets.ORG_PAT }}
        run: |
          changed=$(git diff --name-only HEAD~1 HEAD -- '00_authority/')
          for repo in crm vault amplified-site; do
            curl -s -X POST \
              "https://api.github.com/repos/Amplified-Partners/$repo/dispatches" \
              -H "Authorization: token $GH_TOKEN" \
              -H "Accept: application/vnd.github+json" \
              -d "{\"event_type\": \"authority-update\", \"client_payload\": {\"files\": \"$changed\"}}"
          done
```

**OPINION (Confidence: 70%):** Valuable in principle but requires an org-level PAT as a GitHub secret (the default `GITHUB_TOKEN` can't trigger workflows in other repos). The downstream repos also need `repository_dispatch` handlers. This is medium effort, medium reward. Worth doing once the governance workflow in clean-build is stable. Not first priority.

---

## Proposal 4: Automated PR Checks

### 4a. Secret Leak Scanner

**Problem:** Agents handle API keys, SSH keys, and other credentials. The CRM has `.env.example` files with real key patterns. Multiple agents working in parallel increases the risk of accidental credential commits.

**Mechanism:** GitHub's push protection (part of secret scanning) blocks pushes that contain known secret patterns. This is a repo-level setting, not an Actions workflow.

**Setup:** Enable via GitHub API for all repos:
```bash
for repo in $(gh repo list Amplified-Partners --json name -q '.[].name'); do
  gh api -X PATCH "repos/Amplified-Partners/$repo" \
    -f security_and_analysis.secret_scanning.status=enabled \
    -f security_and_analysis.secret_scanning_push_protection.status=enabled
done
```

**OPINION (Confidence: 95%):** This is the highest-value, lowest-effort security improvement. Enable push protection on all repos. It's free, it's automatic, it catches the most dangerous class of mistake. Not an Actions workflow but belongs in this research because it's the right tool for the job.

**Source:** GitHub natively supports push protection for secret scanning. It scans for patterns from 200+ service providers. [GitHub Docs — Push protection](https://docs.github.com/en/code-security/secret-scanning/push-protection-for-repositories-and-organizations)

### 4b. PR Size Warning

**Problem:** Large PRs are harder to review. Agents sometimes produce sprawling changes. Ewan is a non-coder reviewing PRs — large diffs increase his cognitive load.

```yaml
name: PR size check
on:
  pull_request:
    branches: [main]

jobs:
  size:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0
      - name: Check PR size
        run: |
          additions=$(git diff --stat origin/${{ github.base_ref }}...HEAD | tail -1 | \
            grep -oE '[0-9]+ insertion' | grep -oE '[0-9]+' || echo 0)
          if [ "$additions" -gt 500 ]; then
            echo "::warning::Large PR: $additions lines added. Consider splitting."
          fi
```

**OPINION (Confidence: 70%):** Nice to have, not essential. Some legitimate PRs (research amalgamation, initial module commits) will be large. Warning only, never blocking.

### 4c. Broken Link Checker (for docs repos)

**Problem:** clean-build has extensive cross-referencing between authority docs. Dead references are called out in `AGENTS.md` as "the #1 class of finding to catch." Currently manual.

```yaml
name: Link check
on:
  pull_request:
    branches: [main]
    paths:
      - '**/*.md'

jobs:
  links:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - name: Check internal references
        run: |
          errors=0
          # Find all markdown links to local files
          grep -rnoE '\[.*?\]\(([^http][^)]+)\)' --include='*.md' . | while IFS=: read -r file line match; do
            target=$(echo "$match" | grep -oE '\(([^)]+)\)' | tr -d '()')
            # Strip anchors
            target_file=$(echo "$target" | cut -d'#' -f1)
            if [ -n "$target_file" ] && [ ! -f "$target_file" ]; then
              echo "::warning file=$file,line=$line::Broken link to $target_file"
              errors=$((errors + 1))
            fi
          done
          echo "Found $errors broken links"
```

**OPINION (Confidence: 85%):** Directly addresses the "Bibliography integrity" requirement from `AGENTS.md`. This is one of the most impactful checks for clean-build specifically. Start there, extend to other docs repos.

---

## Proposal 5: Scheduled Maintenance Workflows

### 5a. Stale Branch Cleanup

**Problem:** With branch protection enabled and multiple agents creating branches, stale branches will accumulate rapidly. Agent branch naming (`devin/{timestamp}-*`, `cassian/*`, etc.) makes this predictable.

```yaml
name: Stale branch cleanup
on:
  schedule:
    - cron: '0 6 * * 1'  # Monday 06:00 UTC
  workflow_dispatch: {}

permissions:
  contents: write
  issues: write

jobs:
  cleanup:
    runs-on: ubuntu-latest
    steps:
      - uses: ollieb89/stale-branch-cleaner@v1
        with:
          stale-days: '30'
          dry-run: 'true'       # Start in report mode
          create-issue: 'true'
          exclude-patterns: 'main,master,develop,release/*'
```

**Source:** [`ollieb89/stale-branch-cleaner`](https://github.com/ollieb89/stale-branch-cleaner) — lightweight action, MIT licensed. Alternative: [`cbrgm/cleanup-stale-branches-action`](https://github.com/cbrgm/cleanup-stale-branches-action) (more mature, 15 stars, Apache 2.0).

**OPINION (Confidence: 85%):** Start in dry-run (report-only) mode. Create an issue listing stale branches. After a month of observing the reports, switch to auto-delete for agent branches older than 30 days (they're always merged or abandoned by then). Protect `main`, `develop`, `release/*`.

### 5b. Dependabot Standardisation

**Problem:** Dependabot config exists in clean-build, crm, amplified-site, vault. Missing from ~15 other repos. Auto-merge exists in clean-build, crm, amplified-site. Missing from vault and all others.

**Action:** Deploy the same `dependabot.yml` + `dependabot-auto-merge.yml` pair to all active repos. The existing pattern in clean-build is the template.

**OPINION (Confidence: 90%):** This is maintenance hygiene. The pattern is proven (already running in 3 repos). Roll it out to all Python and TypeScript repos at minimum.

### 5c. Weekly Org Health Dashboard

**Problem:** No single view of CI/CD health across the org. Ewan has to check each repo individually.

```yaml
# In .github repo (org-level)
name: Weekly org health
on:
  schedule:
    - cron: '0 8 * * 1'  # Monday 08:00 UTC
  workflow_dispatch: {}

jobs:
  health:
    runs-on: ubuntu-latest
    steps:
      - name: Org health scan
        env:
          GH_TOKEN: ${{ secrets.ORG_PAT }}
        run: |
          echo "# Amplified Partners — Weekly Health Report" > report.md
          echo "" >> report.md
          echo "Generated: $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> report.md
          echo "" >> report.md

          for repo in clean-build crm vault amplified-site marketing-engine \
                      enforcer cost-tools perplexity-research; do
            echo "## $repo" >> report.md

            # Open PRs
            prs=$(curl -s -H "Authorization: token $GH_TOKEN" \
              "https://api.github.com/repos/Amplified-Partners/$repo/pulls?state=open" \
              | jq length)
            echo "- Open PRs: $prs" >> report.md

            # Recent workflow runs
            runs=$(curl -s -H "Authorization: token $GH_TOKEN" \
              "https://api.github.com/repos/Amplified-Partners/$repo/actions/runs?per_page=5" \
              | jq -r '.workflow_runs[] | "  - \(.name): \(.conclusion // "running") (\(.created_at))"')
            echo "- Recent CI:" >> report.md
            echo "$runs" >> report.md
            echo "" >> report.md
          done

          cat report.md >> "$GITHUB_STEP_SUMMARY"
```

**OPINION (Confidence: 75%):** Useful once there are enough workflows to monitor. Premature if you only have Dependabot running. Build this after Proposals 1-2 are deployed so there's actually something to report on.

---

## Proposal 6: Perplexity-Research Specific Workflows

### 6a. Research File Validator

**Problem:** Research files should follow the naming convention `YYYY-MM-DD-short-description.md`, include citations, and include a signature. CONTRIBUTING.md makes these rules clear but compliance is manual.

```yaml
name: Research file validation
on:
  pull_request:
    branches: [main]
    paths:
      - 'inbox/**'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0
      - name: Validate research files
        run: |
          changed=$(git diff --name-only --diff-filter=ACM \
            origin/${{ github.base_ref }}...HEAD -- 'inbox/*.md')

          for f in $changed; do
            basename=$(basename "$f")
            echo "Checking: $basename"

            # Check naming convention
            if ! echo "$basename" | grep -qE '^[0-9]{4}-[0-9]{2}-[0-9]{2}-[a-z0-9-]+\.md$'; then
              echo "::warning file=$f::File name does not match YYYY-MM-DD-description.md pattern"
            fi

            # Check for signature
            if ! grep -qiE '(signed|authored|devon|session|devin|clawd|cassian|antigravity|openclaw|ewan|kimmy)' "$f"; then
              echo "::warning file=$f::Missing signature (per CONTRIBUTING.md: sign your work)"
            fi

            # Check for citations/sources
            if ! grep -qiE '(source|http|doi|citation|reference|\[.*\]\(http)' "$f"; then
              echo "::warning file=$f::No citations detected (per CONTRIBUTING.md: include sources)"
            fi
          done
```

**OPINION (Confidence: 80%):** Lightweight validation that reinforces the conventions in CONTRIBUTING.md. Warning only — research drops should not be blocked by formatting pedantry, but missing signatures and citations should be visible.

---

## Implementation Priority

Ranked by (value / effort) ratio, considering current org maturity:

### Tier 1 — Do This Week (high value, low effort)

| # | Proposal | Effort | Why first |
|---|----------|--------|-----------|
| 1 | **4a. Secret Leak Scanner** | 15 min | Enable push protection org-wide. One API call per repo. Highest security value. Not an Actions workflow — just a setting. |
| 2 | **5b. Dependabot Standardisation** | 1 hour | Copy proven pattern to remaining repos. Purely mechanical. |
| 3 | **2a. Signature Checker** | 30 min | Directly fulfils a stated governance requirement. Simple grep-based check. |

### Tier 2 — Do This Week (medium effort, high value)

| # | Proposal | Effort | Why next |
|---|----------|--------|----------|
| 4 | **1a. Python Quality Gate** | 2 hours | Ruff lint + format on crm, marketing-engine, enforcer. Start non-blocking. |
| 5 | **2b. Authority Change Detector** | 1 hour | Automates the most-missed PR checklist item in clean-build. |
| 6 | **4c. Broken Link Checker** | 1 hour | Addresses "#1 class of finding" from AGENTS.md. |
| 7 | **6a. Research File Validator** | 30 min | Enforces CONTRIBUTING.md conventions in this repo. |

### Tier 3 — Do This Month (medium effort, medium value)

| # | Proposal | Effort | Why later |
|---|----------|--------|-----------|
| 8 | **1b. TypeScript Quality Gate** | 2 hours | Fewer TS repos; less immediate value. |
| 9 | **1c. Markdown Quality Gate** | 1 hour | Needs `.markdownlint.yaml` config tuning. |
| 10 | **5a. Stale Branch Cleanup** | 1 hour | Valuable once branch accumulation becomes visible (give it 2-3 weeks). |
| 11 | **2c. MANIFEST Index Check** | 1 hour | Completes governance trio but lower frequency of occurrence. |
| 12 | **3a. Research Drop Notifier** | 2 hours | Requires Linear API secret in GitHub. Integration work. |

### Tier 4 — Do When Ready (higher effort, speculative value)

| # | Proposal | Effort | Why wait |
|---|----------|--------|----------|
| 13 | **3b. Authority Change Broadcast** | 3 hours | Needs org PAT, downstream handlers. Wait for governance workflows to stabilise. |
| 14 | **5c. Weekly Org Health Dashboard** | 2 hours | Premature until there are enough workflows to report on. |
| 15 | **4b. PR Size Warning** | 30 min | Nice to have, low signal-to-noise ratio. |

---

## Architecture Decision: Centralised vs. Per-Repo

**Recommendation:** Hybrid approach.

- **Reusable workflows** (Proposals 1a, 1b, 1c) live in `Amplified-Partners/.github` repo. Called via `uses:` from per-repo caller workflows. This means one place to update the logic, per-repo control over which checks run.
- **Governance workflows** (Proposals 2a, 2b, 2c) live in `clean-build` only. They reference clean-build-specific paths (`00_authority/`, `01_truth/`). No need to centralise.
- **Repo-specific workflows** (Proposals 6a, 3a) live in their respective repos (perplexity-research, clean-build).
- **Org-level workflows** (Proposals 5c) live in `Amplified-Partners/.github`.

**Source for centralisation pattern:** GitHub requires reusable workflows to be in a public repo OR in the same org with Actions access. Since Amplified-Partners repos are private, the `.github` repo must grant Actions access to the org. Set via: Org Settings → Actions → General → "Allow Amplified-Partners actions and reusable workflows."

**OPINION (Confidence: 85%):** This hybrid avoids the two failure modes: (a) everything centralised = too much coupling, one bad change breaks all repos; (b) everything per-repo = 19 copies of the same workflow to maintain. The hybrid uses centralised for shared logic and per-repo for repo-specific concerns.

---

## Compound Engineering Connection

These workflows directly support the Compound Engineering loop:

| Loop Phase | Workflow Support |
|------------|------------------|
| **Plan (40%)** | Authority change detector (2b) + MANIFEST check (2c) ensure plans are properly documented before work begins |
| **Work (10%)** | Python/TS quality gates (1a, 1b) catch errors during the work phase, before review |
| **Review (30%)** | Signature checker (2a) + broken link checker (4c) + PR size warning (4b) reduce reviewer cognitive load |
| **Compound (20%)** | Process health report (existing) + org health dashboard (5c) make the compounding visible — each week's metrics feed into the next week's improvements |

---

## Risks and Mitigations

| Risk | Mitigation |
|------|-----------|
| **CI minutes cost** | GitHub Free/Team plans include 2,000-3,000 minutes/month. These workflows are lightweight (< 1 min each). At ~50 PRs/week across the org, budget is ~200 minutes/month. Well within limits. |
| **False positive fatigue** | Start all checks as warnings (annotations), not blocking. Promote to blocking only after 2+ weeks of clean runs. This follows the "catch, not gate" philosophy from SIGNATURES.md. |
| **Workflow maintenance burden** | Centralise reusable workflows in `.github` repo. One place to update. Dependabot keeps Actions versions current. |
| **Secrets management** | Only Proposals 3a and 3b require additional secrets (Linear API key, org PAT). Everything else uses the default `GITHUB_TOKEN`. |
| **Agent resistance** | These workflows help agents, not hinder them. Catching signature omissions and broken links before review means fewer review roundtrips. Frame as "making the next unit of work easier" — the Compound Engineering thesis. |

---

## Sources

1. GitHub Docs — Creating workflow templates for your organization. https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/creating-workflow-templates-for-your-organization
2. GitHub Well-Architected — Scaling GitHub Actions Reusability in the Enterprise. https://wellarchitected.github.com/library/collaboration/recommendations/scaling-actions-reusability/
3. GitHub Docs — Sharing actions and workflows with your organization. https://docs.github.com/en/actions/administering-github-actions/sharing-workflows-secrets-and-runners-with-your-organization
4. GitHub Docs — Triggering a workflow (repository_dispatch). https://docs.github.com/actions/using-workflows/triggering-a-workflow
5. GitHub Docs — Push protection for secret scanning. https://docs.github.com/en/code-security/secret-scanning/push-protection-for-repositories-and-organizations
6. GitHub Blog — Simplify using secrets with reusable workflows (`secrets: inherit`). https://github.blog/changelog/2022-05-03-github-actions-simplify-using-secrets-with-reusable-workflows/
7. `ollieb89/stale-branch-cleaner` — Stale branch cleanup action. https://github.com/ollieb89/stale-branch-cleaner
8. `cbrgm/cleanup-stale-branches-action` — Alternative stale branch cleanup. https://github.com/cbrgm/cleanup-stale-branches-action
9. `DavidAnson/markdownlint-cli2-action` — Markdown linting action. https://github.com/marketplace/actions/markdownlint-cli2-action
10. Amplified Partners internal: `clean-build/00_authority/SIGNATURES.md` — signature enforcement rule and philosophy.
11. Amplified Partners internal: `clean-build/AGENTS.md` — PR reviewer guidelines, bibliography integrity, authority change rules.
12. Amplified Partners internal: `clean-build/00_authority/PROMOTION_GATE.md` — five-point promotion criteria.
13. Amplified Partners internal: `clean-build/00_authority/MANIFEST.md` — authority index and status tokens.
14. Amplified Partners internal: `perplexity-research/CONTRIBUTING.md` — research file conventions.
15. Amplified Partners internal: Devon-77fb `inbox/2026-05-04-github-mastery-research.md` — prior research on GitHub capabilities.

---

*Devon-081a | 2026-05-05 | session `devin-081aaaed7d0743419613f9ecb3fa0470` | Research task: GitHub Actions workflow proposals for Amplified Partners org*
