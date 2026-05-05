# GitHub Mastery — Consolidated Research & Recommendations
**Devon-77fb | 2026-05-04 | Amplified Partners**

Research from 3 daughter sessions + my own analysis. Organised by priority. My opinion on each.

---

## DO THIS WEEK — High impact, low effort

### 1. Copilot Custom Instructions (org-wide)
**What:** You can set org-wide instructions that tell Copilot how to behave across all 24 repos. Went GA April 2026. It's a text box in org settings — you write natural language instructions and Copilot follows them in Chat, PR review, and the cloud agent.

**Setup:** Go to https://github.com/organizations/Amplified-Partners/settings/copilot → Custom Instructions. Paste instructions covering your conventions: radical attribution, signatures on all commits, OPINION confidence labels, no bloat, no hedging, cite sources, follow existing code style.

**My opinion (Confidence: 95%):** This is the single biggest Copilot unlock. Right now Copilot writes generic code. With custom instructions it writes Amplified code from the start. 10 minutes to set up, permanent value. I can write the instructions for you.

**Verdict: DO IT — I'll write the instructions, you paste them.**

---

### 2. Branch Protection on main (all repos)
**What:** Prevent anyone pushing directly to main without a PR. Require at least one review. Require CI to pass before merge.

**Setup:** Can be done via API across all 24 repos in one script. Rules: require PR, require 1 approval, require status checks to pass, no force push, no deletion.

**My opinion (Confidence: 90%):** This is governance enforcement at the infrastructure level. Right now anyone (including me) can theoretically push straight to main. That's how accidents happen. Branch protection makes the PR process mandatory, not optional. Some repos already have it (from AMP-70 PRs), most don't.

**Verdict: DO IT — I'll script it across all repos. One command.**

---

### 3. Dependabot + Auto-merge (standardise)
**What:** Dependabot opens PRs for dependency updates. Auto-merge merges minor/patch updates automatically when CI passes. Major version bumps come to you for review.

**Current state:** Some repos have Dependabot configured, some don't. Auto-merge is inconsistent. There are open PRs right now for adding Dependabot to repos that don't have it (amplified-machine, amplified-knowledge-mcp, enforcer, pudding-testing).

**My opinion (Confidence: 90%):** Standardise across all repos. Same config everywhere. Minor/patch auto-merge, major version bumps need human review. This eliminates an entire class of maintenance work.

**Verdict: DO IT — merge the existing Dependabot PRs, then standardise the rest.**

---

### 4. CODEOWNERS (key repos)
**What:** A file that auto-assigns reviewers when specific directories are changed. When someone touches `00_authority/`, Ewan gets notified. When someone touches `beast-ops/`, I get notified.

**Setup:** Create `.github/CODEOWNERS` in each repo. Example:
```
# Governance — Ewan reviews
/00_authority/ @ewan-dot
# Beast ops — Devon reviews
/beast-ops/ @devin-ai-integration[bot]
```

**My opinion (Confidence: 80%):** Worth doing for clean-build, agent-comms, and vault. Not worth the effort for small single-purpose repos. Focus on repos where multiple agents touch different directories.

**Verdict: DO IT for 3-4 key repos. Skip the rest.**

---

## DO THIS MONTH — Medium effort, high value

### 5. GitHub Actions — Reusable Workflows
**What:** Automated pipelines triggered by events (PR opened, push to main, scheduled). Reusable workflows let you write one workflow and apply it across all repos.

**High-value patterns:**
- **PR validation:** Lint, type-check, test on every PR. Block merge if fails.
- **Notification on research drop:** When someone pushes to perplexity-research, send a Slack message.
- **Scheduled maintenance:** Weekly stale branch cleanup, monthly dependency audit.
- **Cross-repo sync:** When an authority file changes in clean-build, trigger validation in downstream repos.

**My opinion (Confidence: 85%):** This is the biggest capability we're not using. But it's also the most effort to set up well. Start with PR validation on the 3-4 key repos, then expand. Don't try to do all 24 repos at once.

**Verdict: DO IT — start with clean-build, agent-comms, crm. Expand later.**

---

### 6. GitHub Advanced Security (GHAS)
**What:** On Enterprise plan, you get: secret scanning (finds leaked API keys), code scanning with CodeQL (finds vulnerabilities), Dependabot security alerts (finds vulnerable dependencies).

**Current state:** Probably partially enabled. Secret scanning may be on by default for Enterprise. Code scanning needs explicit setup.

**My opinion (Confidence: 85%):** Enable secret scanning across all repos immediately — it's free on Enterprise and catches leaked keys automatically. Code scanning (CodeQL) is worth enabling on crm and any Python/TypeScript repos with actual application code. Skip it for docs-only repos.

**Verdict: Enable secret scanning org-wide. CodeQL on code repos only.**

---

### 7. Copilot PR Auto-Review
**What:** Copilot automatically reviews PRs and leaves comments on code quality, bugs, style issues. Just went GA. Note: from June 2026, this consumes GitHub Actions minutes.

**My opinion (Confidence: 75%):** Useful as a second pair of eyes, especially for repos where I'm not the one opening the PR. But it's Tier 2 review — it won't understand the Amplified Way unless you've set the custom instructions (item #1). Do item #1 first, then enable this.

**Verdict: ENABLE after custom instructions are set. Watch the Actions minutes cost.**

---

## EXPERIMENT — Worth investigating, not urgent

### 8. GitHub Container Registry (GHCR)
**What:** Host Docker images on GitHub instead of building them only on Beast.

**My opinion (Confidence: 60%):** Could create a proper CI/CD pipeline: code → PR → build image → push to GHCR → pull on Beast. But Beast currently builds its own containers from compose files. Adding GHCR adds a layer without clear immediate benefit. Revisit when CRM deploys.

**Verdict: EXPERIMENT LATER — after CRM deployment.**

---

### 9. External Repo Monitoring
**What:** Watch external repos (compound-engineering, key open source tools) for new releases, ideas worth curating.

**How:** GitHub releases have RSS feeds: `https://github.com/{owner}/{repo}/releases.atom`. Can set up an Action that checks feeds weekly and drops summaries into perplexity-research.

**My opinion (Confidence: 80%):** Good idea, low priority. Manual monitoring works for now. Automate when the list of repos worth watching grows beyond 5-10.

**Verdict: SET UP when we have a list of repos to watch.**

---

### 10. GitHub Projects (vs Linear)
**What:** GitHub's built-in project management boards.

**My opinion (Confidence: 95%):** SKIP. Linear is the brain. You've already decided this. GitHub Projects would be a parallel system with no benefit. Linear does everything GitHub Projects does, better, and it's already where all the work lives.

**Verdict: SKIP — Linear owns this.**

---

## CLOUD DEVIN — What we're paying for and not using

From the daughter-3 audit:

### 11. Scheduled Sessions
**What:** Cron-based recurring Devin sessions. You want: 7am Beast health check, 8am Linear update, 9am planning, 2pm triage.

**My opinion (Confidence: 90%):** These should be running already. Each one needs a playbook attached so the session knows exactly what to do. I can set all 4 up right now.

**Verdict: SET UP NOW — I'll create the playbooks and schedules.**

---

### 12. Knowledge Notes Cleanup
**What:** You have ~42 knowledge notes. 3 are duplicate PUDDING Technique notes. Some are test notes. Every duplicate wastes context window in every session.

**My opinion (Confidence: 90%):** Deduplicate immediately. One PUDDING note, one portable spine note, one per-repo index. Remove test notes. Organise into folders.

**Verdict: DO IT — I'll clean up the duplicates.**

---

### 13. Playbooks
**What:** Reusable task templates. Define a complex task once, run it repeatedly with consistent quality.

**My opinion (Confidence: 85%):** Create playbooks for the recurring tasks: Beast health check, Linear triage, PR audit, repo maintenance. Each scheduled session should have a playbook.

**Verdict: CREATE for scheduled sessions.**

---

### 14. Child Sessions (Daughter Agents)
**What:** Spin up parallel Devin sessions for independent tasks. No concurrency limit. Structured output schemas let you poll results without interrupting them.

**My opinion (Confidence: 90%):** We just used this tonight — 3 daughters doing parallel research. It works. Use it more: split large tasks across daughters, use structured output to collect results, consolidate in the parent session.

**Verdict: ALREADY USING — keep using, refine the patterns.**

---

## PRIORITY ACTION PLAN

| Priority | Action | Effort | Who |
|----------|--------|--------|-----|
| 1 | Copilot custom instructions (org-wide) | 10 min | Devon writes, Ewan pastes |
| 2 | Branch protection on main (all repos) | 30 min | Devon scripts it |
| 3 | Secret scanning (org-wide) | 5 min | Devon enables via API |
| 4 | Standardise Dependabot + auto-merge | 1 hr | Devon (merge existing PRs + fill gaps) |
| 5 | CODEOWNERS (clean-build, agent-comms, vault) | 20 min | Devon |
| 6 | Scheduled sessions + playbooks (4 daily) | 1 hr | Devon |
| 7 | Knowledge notes cleanup | 30 min | Devon |
| 8 | GitHub Actions — PR validation workflows | 2 hr | Devon |
| 9 | Copilot PR auto-review | 10 min | Devon enables after #1 |
| 10 | External repo monitoring | 1 hr | Devon, when repo list exists |

**Total to get 80% of the value: about 3 hours of Devon time.**
Items 1-5 could be done in a single session. Items 6-7 in another. Items 8-10 can wait.

---

*Devon-77fb | 2026-05-04 | Consolidated from daughter sessions devin-96da, devin-c38a, devin-ed17 + own research*
*Daughter reports available at their session links for full detail*
