# pplx-exporter v0.1.0

Perplexity conversation exporter for the Amplified Partners knowledge pipeline.

Exports **all** your Perplexity threads to structured Markdown (YAML frontmatter) + raw JSON, with full resumability, audit logging, and a global manifest.

## Architecture Decisions

| Choice | Rationale |
|--------|-----------|
| Playwright persistent session | Auth without cookie extraction — rides browser's own session |
| `POST /rest/thread/list_ask_threads` | Reliable paginated discovery (not DOM-walk) |
| `page.evaluate(fetch('/rest/thread/{slug}'))` | Clean fetch inheriting browser cookies |
| Checkpoint after every thread | Full resumability from interruption |
| Exponential backoff (2s base, 32s max, 5 retries) | Rate-limit hygiene on undocumented endpoints |
| YAML frontmatter + per-thread JSON | Dual output for both human reading and pipeline ingestion |
| JSONL audit log | Append-only accountability trail |

## Install

```bash
cd tools/pplx-exporter
npm install
npx playwright install chromium
```

## Usage

```bash
# First run — opens browser for interactive login
npm run export

# With options
npx tsx src/index.ts --output ~/my-export --rate-limit 2000

# Headless (after first login saved session)
npx tsx src/index.ts --headless
```

## Options

| Flag | Default | Description |
|------|---------|-------------|
| `-o, --output <dir>` | `./pplx-export` | Output directory |
| `--headless` | `false` | Run headless (requires existing session) |
| `--rate-limit <ms>` | `1500` | Delay between fetches |
| `--batch-size <n>` | `20` | Threads per discovery batch |
| `--max-retries <n>` | `5` | Retries per failed thread |

## Output Structure

```
pplx-export/
├── manifest.json          # Global index of all exported threads
├── audit.log              # JSONL append-only event log
├── checkpoint.json        # Resumability state
├── ai-research/           # Threads grouped by Space
│   ├── how-does-rlhf-work.md
│   └── how-does-rlhf-work.json
├── _unsorted/             # Threads without a Space
│   ├── random-question.md
│   └── random-question.json
└── .browser-data/         # Playwright session (gitignored)
```

## Markdown Format

```markdown
---
pplx_slug: abc123def456
pplx_url: https://www.perplexity.ai/search/abc123def456
title: "How does RLHF work?"
space: AI Research
created_at: 2026-01-15T14:32:00Z
updated_at: 2026-01-15T15:10:00Z
source: perplexity
tier: INTUITED
tier_note: "Exported from Perplexity UI. Content not independently verified."
export_tool: pplx-exporter-v0.1
---

## How does RLHF work?

[Answer with inline citations]

### Sources

1. [Title](url)
```

## Resumability

The tool saves `checkpoint.json` after every thread fetch. If interrupted:
- Run the same command again
- Discovery is skipped if already complete
- Already-exported threads are skipped
- New threads are appended

## What This Does NOT Do (v0.1 Limitations)

- File attachment download (planned v0.2)
- Memory/personalisation export (endpoint TBD)
- Comet data (separate product)
- Space-only threads not in main library (needs endpoint discovery)

## Attribution

Design brief: Ewan Bramley (Amplified Partners).
Research: Perplexity Scraper Landscape analysis (2026-05-10).
Best patterns taken from: simwai/perplexity-ai-export (checkpoint, pagination), kylebrodeur/perplexity-exporter (page.evaluate fetch).

---

*Devon-0730 | 2026-05-10 | session `devin-073070e728fc44baa43c95536b8bb623`*
