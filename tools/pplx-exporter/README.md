# pplx-exporter v0.1.0

Authenticated web conversation exporter. Exports Perplexity threads to Markdown + JSON with full metadata, checkpoint resumability, and audit trail.

## Architecture

- **`curl_cffi`** for all API requests — Chrome TLS fingerprint impersonation bypasses Cloudflare bot detection
- **Playwright** only for initial interactive login (grabs session token once)
- **Fingerprint rotation** on retries — each retry uses a different browser profile
- **Checkpoint after every thread** — interrupt anytime, resume where you left off
- **YAML frontmatter** on every Markdown file (slug, URL, title, space, timestamps, tier, hash)
- **JSONL audit log** — append-only accountability trail

## Install

```bash
cd tools/pplx-exporter
pip install -e .
playwright install chromium
```

## Usage

```bash
# First run — opens browser for interactive login
pplx-export

# With options
pplx-export --output ./my-export --rate-limit 2000 --batch-size 50

# If you already have a session token
pplx-export --token "your-session-token-here"
```

### CLI options

| Flag | Default | Description |
|------|---------|-------------|
| `-o, --output` | `./pplx-export` | Output directory |
| `--headless` | off | Run browser in headless mode |
| `--rate-limit` | `1500` | Milliseconds between API requests |
| `--batch-size` | `20` | Threads per discovery page |
| `--max-retries` | `5` | Retries on 429/503 with exponential backoff |
| `--token` | — | Skip browser login, use this session token directly |

## Output structure

```
pplx-export/
├── AI-Research/
│   ├── How-does-RLHF-work.md
│   └── How-does-RLHF-work.json
├── unsorted/
│   └── ...
├── manifest.json
├── audit.log
├── checkpoint.json
└── .token
```

### Markdown frontmatter (per file)

```yaml
---
pplx_slug: abc123def456
pplx_url: https://www.perplexity.ai/search/abc123def456
title: "How does RLHF work?"
space: "AI Research"
created_at: "2026-01-15T14:32:00Z"
updated_at: "2026-01-15T15:10:00Z"
source: perplexity
tier: INTUITED
export_tool: pplx-exporter-v0.1
---
```

## How it works

1. **Auth**: First run opens Playwright browser for interactive login. Extracts `__Secure-next-auth.session-token` cookie and saves it locally.
2. **Discovery**: Paginates `POST /rest/thread/list_ask_threads` (offset-based, batch_size per page).
3. **Fetch**: For each thread, `GET /rest/thread/{slug}` with cursor pagination (first page 10, then 100).
4. **Render**: Converts to Markdown with YAML frontmatter + raw JSON alongside.
5. **Checkpoint**: Saves state after every thread. Resume anytime.

## Rate limiting

- Discovery: 1 request per `discovery_rate_ms` (default 2000ms)
- Thread fetch: 1 request per `rate_limit_ms` (default 1500ms)
- On 429/503: exponential backoff (base 2s, max 32s, 5 retries)
- On retry: rotates browser fingerprint (Chrome TLS profile)
- Maximum concurrency: 1 (sequential)

## Resumability

Checkpoint saved after every thread fetch:
- `checkpoint.json`: processed slugs, discovery state, run ID
- Restart: skips discovery if already done, skips processed threads

## Dependencies

- `curl_cffi` — HTTP with Chrome TLS fingerprint (Cloudflare bypass)
- `playwright` — browser automation for interactive login only
- `pyyaml` — YAML frontmatter generation
- Python 3.11+

---

*Signed-by: Devon-0730 | 2026-05-10 | devin-073070e728fc44baa43c95536b8bb623*
