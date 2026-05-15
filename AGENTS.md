---
description:
alwaysApply: true
---

# Partner instructions — Perplexity Research

**Repo:** `Amplified-Partners/perplexity-research`
**Authority:** Portable Spine (`Amplified-Partners/portable-spine/SPINE.md`) > this file > session instructions.

## What this repo is

Automated AI-native governance and research platform. Multi-agent Compound Engineering pipeline enforcing constitutional principles, managing PR lifecycles, and conducting structured research via Perplexity integration.

## Five Rods

1. Radical Honesty
2. Radical Transparency
3. Radical Attribution
4. Win-Win
5. Idea Meritocracy

Ulysses Clause applies.

## Data architecture (canonical)

- **One engine, three capabilities:** PostgreSQL + Apache AGE (graph) + pgvector/HNSW (vector).
- Do NOT introduce FalkorDB or Qdrant dependencies — both deprecated.
- Source of truth: `clean-build/00_authority/DATA_ARCHITECTURE.md`

## Repo-specific rules

- **Research outputs must carry provenance.** Every research result attributed to source + model + timestamp.
- **Governance files in `00_authority/`** require version bumps and changelog entries on edit.
- **Five Rods review** enforced in CI — PRs checked against constitutional principles before merge.
- **UK English** in all user-facing content.

## Bounded authority

- Research pipeline changes: act (reversible).
- Governance rule changes: surface to Ewan.
- New model integrations: surface (cost/privacy implications).
- All commits signed with agent name + date + session ID.

---
*Devon-4c30 | 2026-05-14 | session devin-4c30b171b2074de7842c99f77e5093c1*
