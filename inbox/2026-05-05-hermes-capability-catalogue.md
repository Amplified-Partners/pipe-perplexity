# Hermes Capability Catalogue

**Date:** 2026-05-05  
**Author:** Cassian-research-subagent  
**Purpose:** Wide inventory of everything Hermes *could* do — not a role description. Ewan picks.

---

## Memory Architecture Constraint (Known — Do Not Revisit)

All capabilities in this catalogue sit on top of a fixed memory model:

- **Working memory:** context window, volatile, per-session.
- **Portable spine:** `Amplified-Partners/hermes` GitHub repo, loaded at every session start via git, regardless of substrate or platform. This is given to Hermes by Amplified Partners — it does not ship with one natively. Mirrors the pattern at `Amplified-Partners/mirror`.

The spine is permanent; the agent is replaceable. Kill Hermes, spine persists. Respawn Hermes, load spine, work continues. **All capabilities below assume the spine is present and loaded.** Writing to the spine (per the breakthrough rule) is a baseline capability, not optional — Hermes reads and writes `Amplified-Partners/hermes` as part of routine operation. Other agents (Cassian, Mirror, Devon) can read the spine repo at any time — this is Radical Transparency at the spine level, observable state without requiring the agent to be alive.

---

## 1. Business / Commercial

### Built-in to Hermes (no skill install required)

- **CRM record management via MCP:** Linear skill ([`productivity/linear`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog)) provides GraphQL + curl access to issues, projects, and teams. Airtable skill ([`productivity/airtable`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog)) provides full CRUD, filters, and upserts via REST. Both can stand in for lightweight CRM.
- **Document drafting:** File read/write via `read_file`, `patch`, and `terminal` tools. PDF editing via `nano-pdf` bundled skill.
- **Contract handling:** `hermes-legal` (community, [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)) — contract risk analysis, risky clause identification, English and Turkish support.
- **Google Workspace integration:** [`productivity/google-workspace`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — Gmail, Calendar, Drive, Docs, Sheets via `gws` CLI or Python.
- **Microsoft 365 integration:** `microsoft-workspace-skill` (community, [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)) — full Outlook/Hotmail/Microsoft 365 via Microsoft Graph API: email, calendar, contacts, user profile, free/busy scheduling, OAuth2 with auto-refresh.
- **Shopify:** [`optional/productivity/shopify`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — Shopify Admin & Storefront GraphQL APIs: products, orders, customers, inventory, metafields.
- **Stripe monitoring:** Automation template available for payment event webhooks — `payment_intent.succeeded`, `payment_intent.payment_failed`, `charge.dispute.created` — delivering summaries to Slack ([Automation Templates](https://hermes-agent.nousresearch.com/docs/guides/automation-templates)).
- **Financial basics / daily briefing:** Cron template for morning business metrics — market prices, pre-market status, industry news ([Automation Templates](https://hermes-agent.nousresearch.com/docs/guides/automation-templates)).
- **Business operations skills:** `cognify-skills` (community, [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)) — 19 business operations skills covering CRM, invoicing, and project management (beta).
- **Startup kit generation:** `hermes-startup-architect` (community, [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)) — generates investor-ready kits from startup ideas: market analysis, pitch deck, financial projections (beta).

### Buildable on top (no shipped skill, but composable)

- **Quoting and onboarding workflows for trades:** Composable from Google Workspace + Linear + file templates. No off-the-shelf skill; requires custom SKILL.md.
- **Cash flow and VAT:** Composable from spreadsheet manipulation (Python/terminal) + Google Sheets skill. No UK-specific bundled skill found in catalogue.
- **Companies House / GDPR / UK regulatory:** Web search + document synthesis. No dedicated UK-regulatory skill found. Buildable as a custom SKILL.md with guidance documents bundled.
- **Win-win deal shape / negotiation support:** No bundled skill. Composable from research + drafting tools.

---

## 2. Marketing

### Built-in / official optional skills

- **X/Twitter:** [`social-media/xurl`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — post, search, DM, media, v2 API via `xurl` CLI.
- **YouTube content:** [`media/youtube-content`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — transcripts to summaries, threads, and blog posts.
- **Content pipeline automation:** Weekly cron template for researching, drafting, and saving blog outline to `~/drafts/blog-$(date +%Y%m%d).md` ([Automation Templates](https://hermes-agent.nousresearch.com/docs/guides/automation-templates)).
- **Landing page / HTML artifact generation:** [`creative/claude-design`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — design one-off HTML artifacts (landing pages, decks, prototypes). [`creative/popular-web-designs`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — 54 real design systems (Stripe, Linear, Vercel) as HTML/CSS.
- **Image generation:** Built-in `image_generate` tool ([Tools & Toolsets](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools)). [`creative/comfyui`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — ComfyUI for images, video, and audio. [`optional/mlops/stable-diffusion-image-generation`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — Stable Diffusion via HuggingFace Diffusers.
- **Infographic generation:** [`creative/baoyu-infographic`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — 21 layouts × 21 styles.
- **Text humanisation:** [`creative/humanizer`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — strip AI-isms and add real voice. Relevant for persona-aware copy and white-hat posture.
- **Songwriting / audio content:** [`creative/songwriting-and-ai-music`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — Suno AI prompts; [`media/heartmula`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — Suno-like song generation from lyrics + tags.
- **FLUX image generation:** `black-forest-labs/skills` (agentskills.io ecosystem, [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)) — official first-party FLUX model skills.
- **Meme generation:** [`optional/creative/meme-generation`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — real meme images via Pillow, `.png` output.
- **HyperFrames video compositions:** [`optional/creative/hyperframes`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — HTML-based video compositions, animated title cards, social overlays, captioned talking-head videos, audio-reactive visuals.
- **Animated explainer videos:** [`creative/manim-video`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — Manim CE animations (3Blue1Brown-style math/algo videos).

### Buildable on top

- **LinkedIn:** No bundled skill found. LinkedIn has no public API equivalent. Composable via browser automation (`browser_navigate`, `browser_vision`) with rate-limit awareness.
- **Substack / email newsletters:** Composable from file drafting + Google Workspace email skill + `send_message` tool.
- **WhatsApp Business broadcasts:** Composable via WhatsApp gateway (`send_message` to WhatsApp contacts). Bulk messaging explicitly flagged as account-risk; limited to conversational patterns ([WhatsApp docs](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/whatsapp)).
- **TikTok / Instagram:** No bundled skill found. Browser automation path exists but platform ToS risk.
- **Anonymised case-study generation:** Composable from document drafting tools + humaniser skill. No dedicated skill.
- **SEO basics:** Web search + content drafting tools. No dedicated SEO skill found.
- **Ad management (Google Ads, Meta Ads):** No bundled skill found. MCP path possible if a Google Ads MCP server is available. Buildable.

---

## 3. Organisation

### Built-in / official optional skills

- **Linear:** [`productivity/linear`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — create, update, triage, label, assign issues; manage projects and teams via GraphQL + curl.
- **Google Calendar / Gmail / Drive:** [`productivity/google-workspace`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — calendar management, email triage, Drive access, Docs and Sheets.
- **Notion:** [`productivity/notion`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — pages, databases, blocks, search via REST.
- **Airtable:** [`productivity/airtable`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — records CRUD, filters, upserts.
- **Webhook event subscriptions:** [`devops/webhook-subscriptions`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — event-driven agent runs.
- **Cron scheduling:** Native `cronjob` tool — natural-language schedule parsing: `"every 30m"`, `"0 2 * * *"`, ISO timestamps, one-shot, interval, cron expression ([Hermes cron module](https://kenhuangus.substack.com/p/chapter-11-hook-event-driven-automation)). Persists to `~/.hermes/cron/jobs.json`.
- **Nightly backlog triage:** Cron template — label, prioritise, and summarise new issues nightly; deliver digest to team channel ([Automation Templates](https://hermes-agent.nousresearch.com/docs/guides/automation-templates)).
- **PR code review automation:** Webhook template — review every PR when opened, post review comment directly on PR ([Automation Templates](https://hermes-agent.nousresearch.com/docs/guides/automation-templates)).
- **Kanban orchestration:** [`devops/kanban-orchestrator`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) + [`devops/kanban-worker`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — decomposition playbook, specialist-roster conventions, anti-temptation rules, Kanban lifecycle. The "don't do the work yourself" orchestrator pattern.
- **Plan mode:** [`software-development/plan`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — write markdown plans to `.hermes/plans/`, no execution. Produces implementation plans with bite-sized tasks and paths.
- **Todo tool:** Native `todo` tool in agent orchestration toolset ([Tools & Toolsets](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools)).
- **Canvas LMS:** [`optional/productivity/canvas`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — fetch enrolled courses and assignments.
- **Maps / routing / geocoding:** [`productivity/maps`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — geocode, POIs, routes, timezones via OpenStreetMap/OSRM.
- **Job task management (execplan):** `execplan-skill` (community, [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)) — manages complex, long-running task execution with progress tracking, checkpoints, and failure recovery (beta).

---

## 4. Coding (Full Range)

> This section is deliberately not curated. Full spectrum of what Hermes can do in code.

### Built-in tools

- **Read codebases:** `read_file`, `web_extract`, `browser_navigate`. Codebase inspection skill: [`github/codebase-inspection`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — LOC, languages, ratios via `pygount`. GitNexus explorer: `gitnexus-explorer` (optional) — index a codebase with an interactive knowledge graph.
- **Fix small things / patch:** `patch` tool, `terminal`, `execute_code`. [`software-development/systematic-debugging`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — 4-phase root-cause debugging before fixing.
- **Build dashboards:** [`creative/claude-design`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) for HTML artifacts; `creative/popular-web-designs` for design-system-backed UI.
- **Write features / TDD:** [`software-development/test-driven-development`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — RED-GREEN-REFACTOR enforcement, tests before code. [`software-development/subagent-driven-development`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — execute plans via delegated subagents with 2-stage review.
- **PR reviews:** [`github/github-code-review`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — diffs, inline comments via `gh` or REST.
- **PR lifecycle:** [`github/github-pr-workflow`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — branch, commit, open, CI, merge.
- **GitHub issues:** [`github/github-issues`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — create, triage, label, assign.
- **Repo management:** [`github/github-repo-management`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — clone, create, fork, remotes, releases.
- **Pre-commit security/quality review:** [`software-development/requesting-code-review`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — security scan, quality gates, auto-fix.
- **Spike / prototype:** [`software-development/spike`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — throwaway experiments before build.
- **Writing plans:** [`software-development/writing-plans`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — implementation plans with bite-sized tasks, paths, code.
- **Node.js debug:** [`software-development/node-inspect-debugger`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — `--inspect` + Chrome DevTools Protocol CLI.
- **Python debug:** [`software-development/python-debugpy`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — `pdb` REPL + `debugpy` remote (DAP).
- **Integrate APIs:** MCP integration — any of 6,000+ MCP-compatible apps reachable as tool sources ([Hermes Agent guide](https://www.heyuan110.com/posts/ai/2026-04-14-hermes-agent-guide/)). Native MCP client: [`mcp/native-mcp`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog).

### Delegate to sub-agents

- **Claude Code delegation:** [`autonomous-ai-agents/claude-code`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — delegate coding (features, PRs) to Claude Code CLI.
- **OpenAI Codex delegation:** [`autonomous-ai-agents/codex`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — delegate to Codex CLI.
- **OpenCode delegation:** [`autonomous-ai-agents/opencode`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — delegate to OpenCode CLI.
- **Blackbox AI delegation:** [`optional/autonomous-ai-agents/blackbox`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — multi-model agent with built-in judge; runs tasks through multiple LLMs and picks best result.

### Automation templates for CI/CD

- Auto PR code review on webhook ([Automation Templates](https://hermes-agent.nousresearch.com/docs/guides/automation-templates))
- CI failure analysis on `check_run` event ([Automation Templates](https://hermes-agent.nousresearch.com/docs/guides/automation-templates))
- Docs drift detection — weekly scan of merged PRs for API changes needing documentation updates ([Automation Templates](https://hermes-agent.nousresearch.com/docs/guides/automation-templates))
- Auto-port changes across repos on PR merge ([Automation Templates](https://hermes-agent.nousresearch.com/docs/guides/automation-templates))
- Issue auto-labeling on GitHub webhook ([Automation Templates](https://hermes-agent.nousresearch.com/docs/guides/automation-templates))

### ACP editor integration

Hermes runs as an ACP server, letting ACP-compatible editors (Zed, VS Code integrations) talk to Hermes over stdio ([ACP Editor Integration](https://hermes-agent.nousresearch.com/docs/user-guide/features/acp)). ACP sessions track working directory, model, conversation history. Hermes tools map to ACP semantic types (`read_file` → `read`).

---

## 5. Inter-Agent Communication

### Native multi-platform gateway

Hermes ships with a unified gateway across the following platforms ([Hermes Agent guide](https://www.heyuan110.com/posts/ai/2026-04-14-hermes-agent-guide/)):

| Platform | Status |
|---|---|
| Telegram | Native |
| Discord | Native |
| Slack | Native |
| WhatsApp | Native (Baileys bridge) |
| Signal | Native |
| Email | Native |
| CLI | Native |
| iMessage/SMS | macOS via `imsg` CLI ([bundled skill](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog)) |
| Feishu/Lark, WeCom | Native (listed in awesome-hermes) |
| Matrix | Not confirmed in official docs |

### Agent-to-agent patterns

- **`delegate_task` tool:** Native subagent delegation — isolated subagents with their own context windows, max 3 concurrent ([Tools & Toolsets](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools)).
- **`send_message` tool:** Outbound messaging delivery to any connected platform ([Tools & Toolsets](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools)).
- **agent-comms folder pattern:** Not a native Hermes feature — this is an Amplified Partners convention. Hermes can read/write a shared directory observed by other agents as a message-passing layer.
- **Perplexity-research inbox pattern:** Git-based — Hermes can push to `Amplified-Partners/perplexity-research/inbox/` the same way Cassian does. The spine repo (`Amplified-Partners/hermes`) gives other agents (Cassian, Mirror, Devon) full observability into what Hermes is loaded with at any given moment — spine-level Radical Transparency.
- **Pets-to-cattle implication:** Agent is replaceable, spine is permanent. Any other agent can inspect `Amplified-Partners/hermes` to understand Hermes's current loaded skills, memories, and operational state without the agent being alive.
- **ACP (Agent Communication Protocol):** Hermes implements `HermesACPAgent` for editor-native coding agent behaviour ([ACP Editor Integration](https://hermes-agent.nousresearch.com/docs/user-guide/features/acp)). ACP is also a broader protocol standard (RESTful, SDK-optional, Linux Foundation governance) for agent interoperability ([Agent Communication Protocol](https://agentcommunicationprotocol.dev/introduction/welcome)).
- **MCP (Model Context Protocol):** Native MCP client — connect to 6,000+ MCP-compatible servers. Hermes implements `SamplingHandler` for server-initiated LLM requests ([Ken Huang Substack Chapter 13](https://kenhuangus.substack.com/p/chapter-13-mcp-integration-connecting)).
- **evey-bridge-plugin:** Claude Code ↔ Hermes context sharing and task handoff (community, [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)).
- **hermes-agent-acp-skill:** Multi-agent delegation skill bridging Hermes, Codex, and Claude Code — routes subtasks to best-suited agent automatically (community, [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)).
- **hermes-plugins inter-agent bridge:** Goal management, inter-agent bridge, model selection, cost control for multiple Hermes instances (community, [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)).
- **Paperclip adapter:** [`hermes-paperclip-adapter`](https://github.com/0xNyk/awesome-hermes-agent) (official Nous Research) — run Hermes as a managed employee in Paperclip companies with task management and governance integration.
- **Global Chat / agents.txt discovery:** Cross-protocol agent discovery across MCP, A2A, and agents.txt; 18K+ MCP servers indexed (community, [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)).
- **Yuanbao groups:** [`yuanbao`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — Yuanbao (元宝) groups: @mention users, query info/members.

---

## 6. Client Communication

### Built-in

- **WhatsApp triage and multi-channel comms:** Native WhatsApp gateway with two modes — dedicated bot number (recommended) or personal self-chat ([WhatsApp docs](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/whatsapp)). Streaming (progressive) responses. Voice messages transcribed automatically via `faster-whisper`, Groq Whisper, or OpenAI Whisper.
- **Autonomous reply within bounded authority:** Allowlist-controlled — explicit lists of authorised users per platform, configurable per-platform allow-all flags, DM pairing with 8-char cryptographic codes ([Security docs](https://hermes-agent.nousresearch.com/docs/user-guide/security)).
- **Dangerous command approval (HITL for destructive ops):** Manual, smart (LLM-assisted risk assessment), or off. Default is manual — human-in-the-loop before any destructive action ([Security docs](https://hermes-agent.nousresearch.com/docs/user-guide/security)).
- **Escalation rules:** Configurable via approval modes and gateway allowlists. Smart mode auto-approves low-risk, escalates uncertain.
- **Multi-channel drafting:** File tools + Google Workspace skill for email; WhatsApp, Telegram, Slack, Discord all deliver via `send_message`.
- **Email with own inbox:** [`optional/email/agentmail`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — give Hermes a dedicated email inbox (e.g. `hermes-agent@agentmail.to`); send, receive, manage autonomously.
- **Himalaya CLI email:** [`email/himalaya`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — IMAP/SMTP from terminal.

---

## 7. Security

### Built-in security architecture (7 layers)

Hermes ships with 7 documented security layers ([Security docs](https://hermes-agent.nousresearch.com/docs/user-guide/security)):

1. **User authorization** — allowlists, DM pairing with cryptographic codes, per-platform controls.
2. **Dangerous command approval** — hardline blocklist (no override: `rm -rf /`, fork bombs, disk wipe); curated approval-trigger patterns including recursive deletes, SQL DROPs, piping URLs to shell.
3. **Container isolation** — Docker: `--cap-drop ALL`, `--security-opt no-new-privileges`, PID limits (256), tmpfs mounts, namespace isolation. Five backend options with varying isolation levels.
4. **MCP credential filtering** — environment variable isolation; credential pattern redaction (`[REDACTED]`) in error outputs.
5. **Context file scanning** — scans `AGENTS.md`, `.cursorrules`, `SOUL.md` for prompt-injection patterns: ignore-prior-instructions, hidden HTML comments, secret reads, exfil attempts, invisible Unicode.
6. **Cross-session isolation** — sessions cannot access each other's data; cron paths hardened against traversal.
7. **Input sanitization** — working directory parameters validated against allowlist.

Additional: SSRF protection (private/loopback/CGNAT ranges blocked), website domain blocklist, Tirith pre-exec scanning (homograph URLs, pipe-to-interpreter, terminal injection).

### Official optional security skills

- **1Password CLI:** [`official/security/1password`](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/security/security-1password) — install `op`, sign in, read secret references (`op://Vault/Item/field`), inject secrets via `op inject`, run commands with secret env vars via `op run`. Service account recommended for Hermes (headless-safe). Preferred over plaintext `.env` for production secret management.
- **OSS forensics:** [`optional/security/oss-forensics`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — supply chain investigation, deleted commit recovery, force-push detection, IOC extraction, multi-source evidence collection for GitHub repositories.
- **Sherlock OSINT:** [`optional/security/sherlock`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — username search across 400+ social networks.
- **Domain intelligence:** [`optional/research/domain-intel`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — passive domain reconnaissance: subdomain discovery, SSL certificate inspection, WHOIS lookups, DNS records, bulk multi-domain analysis. No API keys required.

### Community security

- **Anthropic-Cybersecurity-Skills:** 753+ structured cybersecurity skills mapped to MITRE ATT&CK (agentskills.io ecosystem, [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)) — most comprehensive security skills collection available.
- **Deepfake detection:** `resemble-ai/detect-skill` — AI-generated audio, images, video, and text detection; source tracing; invisible watermarks for provenance (community, [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)).
- **hermes-incident-commander:** Autonomous SRE agent for production incident detection and self-healing — monitors services, diagnoses failures, applies fixes (community, [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)).

### Automation templates

- **Dependency security audit:** Daily cron — `pip audit` + `npm audit`, flags CVEs ≥ 7.0, checks for upgrades, direct vs. transitive ([Automation Templates](https://hermes-agent.nousresearch.com/docs/guides/automation-templates)).
- **Weekly security audit pipeline:** Full codebase scan for hardcoded secrets, SQL injection vectors, path traversal, unsafe deserialisation; combined with dep audit and recent commit review ([Automation Templates](https://hermes-agent.nousresearch.com/docs/guides/automation-templates)).

### MAESTRO / IBAC note

The MAESTRO doctrine (Ken Huang, Layer 5 observability) is addressed via: structured tool-call telemetry at the agent layer; logs to `~/.hermes/logs/`; Repello AI research recommends memory-provenance enforcement (trust-tagging by source), prompt-layer monitoring, and hash-chain audit logs for tamper evidence ([Repello AI](https://repello.ai/blog/hermes-agent-security), [DEV Community 5-Layer Model](https://dev.to/thedailyagent/the-5-layer-security-model-every-ai-agent-needs-in-production-36l3)). These are architectural patterns to implement on top of Hermes's built-in logging — not shipped features.

---

## 8. Research

### Built-in / official skills

- **Web search:** Native `web_search` tool + `web_extract` tool ([Tools & Toolsets](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools)).
- **Browser automation with vision:** `browser_navigate`, `browser_snapshot`, `browser_vision` ([Tools & Toolsets](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools)).
- **arXiv:** [`research/arxiv`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — search by keyword, author, category, or ID.
- **Blog / RSS monitoring:** [`research/blogwatcher`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — monitor blogs and RSS/Atom feeds via `blogwatcher-cli`.
- **Polymarket:** [`research/polymarket`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — query markets, prices, orderbooks, history.
- **LLM Wiki:** [`research/llm-wiki`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — Karpathy-style interlinked markdown knowledge base.
- **Research paper writing:** [`research/research-paper-writing`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — ML papers for NeurIPS/ICML/ICLR, design to submit.
- **DuckDuckGo search:** [`optional/research/duckduckgo-search`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — free web search, text/news/images/videos, no API key.
- **Parallel CLI:** [`optional/research/parallel-cli`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — agent-native web search, extraction, deep research, enrichment, FindAll, and monitoring.
- **qmd personal knowledge search:** [`optional/research/qmd`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — hybrid retrieval engine (BM25 + vector search + LLM reranking) over personal notes, docs, meeting transcripts. CLI and MCP integration.
- **Scrapling web extraction:** [`optional/research/scrapling`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — HTTP fetching, stealth browser automation, Cloudflare bypass, spider crawling.
- **Competitive repo scouting:** Cron template — monitor competitor repos for notable PRs, features, architectural decisions; daily delivery to Telegram ([Automation Templates](https://hermes-agent.nousresearch.com/docs/guides/automation-templates)).
- **AI news digest:** Weekly cron — arXiv scan, GitHub trending, web search; structured digest delivered to Telegram ([Automation Templates](https://hermes-agent.nousresearch.com/docs/guides/automation-templates)).
- **Bioinformatics gateway:** [`optional/research/bioinformatics`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — gateway to 400+ bioinformatics skills from bioSkills and ClawBio.
- **Drug discovery:** [`optional/research/drug-discovery`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — ChEMBL, Lipinski Ro5, OpenFDA drug interactions, ADMET.
- **Domain intel (OSINT):** [`optional/research/domain-intel`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — passive domain recon, SSL, WHOIS, DNS, bulk analysis.

---

## 9. Personal Assistant

### Built-in / official skills

- **Calendar, scheduling, reminders:** Google Calendar via [`productivity/google-workspace`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog). Apple Reminders via [`apple/apple-reminders`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) (macOS, `remindctl`).
- **Apple Notes:** [`apple/apple-notes`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — create, search, edit via `memo` CLI (macOS).
- **FindMy device tracking:** [`apple/findmy`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — track Apple devices/AirTags (macOS).
- **Travel / maps / routing:** [`productivity/maps`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — geocode, POIs, routes, timezones via OpenStreetMap/OSRM.
- **Document drafting and editing:** `read_file`, `patch`, `terminal`; PDF editing via `nano-pdf` (`productivity/nano-pdf`); PowerPoint creation via `productivity/powerpoint`.
- **Summaries:** Web extract + document synthesis tools. YouTube transcript summarisation via `media/youtube-content`.
- **Transcription:** Built-in STT for voice messages — `faster-whisper` (local), Groq Whisper, OpenAI Whisper ([WhatsApp docs](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/whatsapp)). `optional/mlops/whisper` — full 99-language Whisper model, 6 sizes, transcription and translation to English.
- **Spaced-repetition flashcards:** [`optional/productivity/memento-flashcards`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — create cards, chat with flashcards, generate quizzes from YouTube transcripts, adaptive scheduling.
- **Fitness / nutrition tracking:** [`optional/health/fitness-nutrition`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — 690+ exercises, 380,000+ foods, BMI, TDEE, one-rep max, macro splits.
- **Spotify control:** [`media/spotify`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — play, search, queue, manage playlists and devices.
- **Hermes-life-os:** Personal OS agent detecting daily patterns and learning routines over time using Hermes's memory system (community, [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)).
- **OCR and document extraction:** [`productivity/ocr-and-documents`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — extract text from PDFs/scans via `pymupdf`, `marker-pdf`.
- **here.now static publishing:** [`optional/productivity/here.now`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — publish static sites to `{slug}.here.now`; store private files in cloud Drives for agent-to-agent handoff.

---

## 10. Data Work

### Built-in tooling

- **CSV/Excel manipulation:** Python via `execute_code` tool (pandas, openpyxl, csv). `terminal` backend with pip install persistence in Docker.
- **Jupyter live kernel:** [`data-science/jupyter-live-kernel`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — iterative Python via live Jupyter kernel (`hamelnb`). Persistent state across cells.
- **Light analytics:** Python execution + web visualisation tools. `vision_analyze` for image-based chart analysis.
- **Dashboard generation:** [`creative/claude-design`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) for HTML dashboards. Baoyu infographic skill for visual layouts.
- **Vector search / RAG:** `optional/mlops/chroma` — open-source embedding database. `optional/mlops/faiss` — Facebook's dense vector similarity search. `optional/mlops/qdrant-vector-search` — high-performance vector similarity for RAG. `optional/mlops/pinecone` — managed production vector database.

### Against Beast services (composable, no dedicated skills)

- **Langfuse:** No dedicated Hermes skill. Composable via MCP (Langfuse has [OpenTelemetry-based integrations](https://langfuse.com/integrations)) or REST API via terminal.
- **FalkorDB:** No dedicated Hermes skill. Composable via MCP or direct query via terminal/Python.
- **Linear:** Full native skill — [`productivity/linear`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog).
- **GitHub (32 repos):** Full native skills — issues, PRs, code review, repo management.
- **Marketing Engine:** No dedicated skill. Composable via browser automation or API calls.

### Report generation

- Cron + file write tools produce scheduled reports to local files, Telegram, Discord, Slack, email, or GitHub comments. All automation templates support `--deliver` targeting.

---

## 11. Voice / Phone

### Official optional telephony skill

[`optional/productivity/telephony`](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/productivity/productivity-telephony):

- **Number provisioning:** Twilio number search, buy, persist, set default. Import to Vapi.
- **SMS:** Send from owned Twilio number. Poll inbound SMS (no webhook needed). Checkpoint state in `~/.hermes/telephony_state.json`.
- **MMS:** Send with media URL attachment.
- **Outbound calls (TTS):** Twilio direct calls with Polly TTS voices. Prerecorded/custom audio URL. IVR navigation via DTMF tones (`--send-digits`).
- **AI voice calls (Bland.ai):** Easiest outbound AI calling. Place call, check status, analyse transcript with specific questions (e.g. "Was the appointment confirmed?").
- **AI voice calls (Vapi):** Better conversational voice quality. Requires Twilio number imported first.
- **Inbound handling:** Twilio polling approach for inbound SMS. No documented native inbound call handler for Bland/Vapi in this skill.

### Voice on messaging platforms

- **WhatsApp voice messages:** Auto-transcribed inbound `.ogg` opus; TTS responses sent as MP3 attachments ([WhatsApp docs](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/whatsapp)).
- **Whisper (full model):** [`optional/mlops/whisper`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — 99 languages, transcription, translation to English, 6 model sizes.
- **Text-to-speech:** Native `text_to_speech` tool in media toolset ([Tools & Toolsets](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools)).

---

## 12. Operations / DevOps

### Built-in tools and official skills

- **Docker management:** [`official/devops/docker-management`](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management) — container lifecycle (run, stop, restart, rm, pause/unpause), container interaction (exec, cp, logs, inspect, stats), image management (build, pull, push, tag, rmi), Docker Compose (up, down, ps, logs, exec, build, config), volumes and networks, troubleshooting (exit codes, resource issues), Dockerfile optimisation.
- **SSH terminal backend:** Remote execution on any SSH host. Recommended for security — agent can't modify its own code when running remotely.
- **Five terminal backends:** Local, Docker, SSH, Singularity, Modal — plus Daytona and Vercel Sandbox (additional options in toolset docs) ([Tools & Toolsets](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools)).
- **Webhook-triggered deploy verification:** Cron/webhook template — CI/CD pipeline POSTs on deploy; Hermes runs smoke tests, checks service health, reports to Telegram ([Automation Templates](https://hermes-agent.nousresearch.com/docs/guides/automation-templates)).
- **Alert triage:** Webhook template — correlate monitoring alerts (Datadog, PagerDuty, Grafana) with recent changes; draft root-cause + escalation recommendations; deliver to Slack on-call channel ([Automation Templates](https://hermes-agent.nousresearch.com/docs/guides/automation-templates)).
- **Uptime monitoring:** 30-minute cron template — check named endpoints, notify only on outage ([Automation Templates](https://hermes-agent.nousresearch.com/docs/guides/automation-templates)).
- **Inference.sh:** [`optional/devops/inference-sh-cli`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — run 150+ AI apps via `infsh` CLI: image generation, video creation, LLMs, search, 3D, social automation.
- **Hermes AI infrastructure monitoring toolkit:** Infrastructure monitoring, cost forecasting, and alerting via Telegram; continuous checks via cron (community, [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)).
- **hermes-incident-commander:** Autonomous SRE agent — monitors services, diagnoses failures, applies fixes (community, [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)).
- **Fast MCP server builder:** [`optional/mcp/fastmcp`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — build, test, inspect, install, and deploy MCP servers with FastMCP in Python.

---

## 13. Knowledge Management

### Built-in / official skills

- **Obsidian vault:** [`note-taking/obsidian`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — read, search, and create notes. Supports multi-layer vault architecture (raw/wiki/output). Daily arXiv scan template saves summaries to Obsidian notes ([Automation Templates](https://hermes-agent.nousresearch.com/docs/guides/automation-templates)). Compatible with OMI memory capture for continuous context ingestion ([Julian Goldie](https://juliangoldie.com/hermes-omi-obsidian/)).
- **SiYuan Note:** [`optional/productivity/siyuan`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — SiYuan Note API: search, read, create, manage blocks and documents in a self-hosted knowledge base.
- **LLM Wiki:** [`research/llm-wiki`](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) — build and query interlinked markdown knowledge base (Karpathy-style).
- **Agent-managed skills (procedural memory):** Hermes writes new skills to `~/.hermes/skills/` after completing complex tasks (5+ tool calls), when it hits errors and finds the working path, when the user corrects its approach, or when it discovers a non-trivial workflow ([Skills System docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)). This is the primary knowledge accumulation mechanism.
- **Spine repo as knowledge layer:** The `Amplified-Partners/hermes` spine repo accumulates breakthroughs per the breakthrough rule. It is the portable knowledge layer — survives agent restart, readable by other agents.
- **qmd hybrid retrieval:** [`optional/research/qmd`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — BM25 + vector + LLM reranking over local knowledge base. Personal API pattern: `personal-api` plugin (community, [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)) — turn Obsidian vault into an identity layer any AI agent can read.
- **Honcho cross-session memory:** [`optional/autonomous-ai-agents/honcho`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — cross-session user modelling, multi-profile peer isolation, observation config, dialectic reasoning, session summaries, context budget enforcement.
- **Chroma vector DB:** [`optional/mlops/chroma`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — store embeddings and metadata, vector and full-text search, metadata filtering; scales from notebooks to clusters.
- **hindsight long-term memory:** Long-term memory layer with retain/recall/reflect workflows; semantic, graph, and temporal retrieval via plugin or MCP (community, [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)).
- **SkillClaw evolution:** Post-task skill evolution loop — auto-evolves, deduplicates, and improves skill library from real session data (community, [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)).
- **PUDDING labels:** No dedicated Hermes skill exists for PUDDING taxonomy. Composable: Obsidian skill + custom SKILL.md instructing labelling with the PUDDING 2026 taxonomy. PUDDING is an Amplified Partners pattern, not a published Hermes standard.

---

## 14. Non-Obvious Capabilities

Capabilities documented or discoverable in the Hermes ecosystem that are not in the marketing pitch:

1. **Self-modifying skills:** The agent creates, updates, and deletes its own skills via `skill_manage` tool. The learning loop is bi-directional — skills inform the agent, agent refines the skills. This makes Hermes qualitatively different from prompt-based agents: the procedural memory grows without user intervention ([Skills System docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)).

2. **SamplingHandler (server-initiated LLM requests):** Hermes's most distinctive MCP feature — MCP servers can request LLM completions from Hermes mid-task. A server says "I need you to summarise this data before I return the result" and Hermes complies. No other documented agent in this class exposes this pattern ([Ken Huang Substack Chapter 13](https://kenhuangus.substack.com/p/chapter-13-mcp-integration-connecting)).

3. **Cron jobs carry their own model, provider, and skills:** Each scheduled job specifies `model`, `provider`, `skills`, and `deliver` target independently. A nightly vulnerability scan can run on a different model to the morning briefing. Jobs are isolated agents — `skip_memory=True`, `disabled_toolsets=[cronjob, messaging, clarify]` ([Ken Huang Substack Chapter 11](https://kenhuangus.substack.com/p/chapter-11-hook-event-driven-automation)).

4. **RTK shell output compression:** `rtk-hermes` plugin (community, [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)) intercepts shell commands via `pre_tool_call` and compresses terminal output before it reaches the LLM context window. 60–90% token reduction on shell commands; benchmarked at 96.6% efficiency across 11M+ tokens. Zero config — auto-loads on gateway boot.

5. **RL training environment integration:** Native `rl_*` toolset ([Tools & Toolsets](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools)). `optional/mlops/hermes-atropos-environments` — build, test, and debug RL environments for Atropos training. Real agent trajectories become fine-tuning data. Tinker-Atropos standalone RL infrastructure ([awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)).

6. **autonovel:** Official Nous Research pipeline for autonomous long-form manuscript generation (100k+ words) built on Hermes's agent loop ([awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)).

7. **NeuroSkill BCI integration:** [`optional/health/neuroskill-bci`](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) — incorporates the user's real-time cognitive and emotional state (focus, relaxation, mood, cognitive load, drowsiness, heart rate, HRV, sleep staging, 40+ EXG scores) into agent responses. Requires a running NeuroSkill instance.

8. **Hermes as ACP server for editors:** Hermes can behave as an editor-native coding agent inside Zed or VS Code via ACP — full IDE integration including file diffs, terminal commands, approval prompts, streamed thinking ([ACP Editor Integration](https://hermes-agent.nousresearch.com/docs/user-guide/features/acp)).

9. **Well-known skills endpoint discovery:** Any website that publishes `/.well-known/skills/index.json` is discoverable by Hermes — not requiring a central hub. Mintlify, for example, publishes its own skill endpoint ([Skills System docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)).

10. **Home Assistant integration:** Native `ha_*` toolset — control smart home devices via Home Assistant ([Tools & Toolsets](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools)).

11. **Hermes-agent-self-evolution (GEPA):** Evolutionary self-improvement using DSPy and Genetic Evolution of Prompt Architectures — the research pipeline for optimising Hermes's own prompts and behaviours ([awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent), official Nous Research project).

12. **here.now for agent-to-agent handoff:** `optional/productivity/here.now` publishes static sites and stores private files in cloud Drives specifically for agent-to-agent handoff — documented use case, not a marketing feature ([Optional Skills Catalog](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog)).

13. **LobeHub agent conversion:** Hermes can search and convert LobeHub agent entries into installable Hermes skills — 24,000+ indexed agent configurations become loadable skills without manual authoring ([Skills System docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)).

14. **AgentCash — 300+ premium APIs with wallet:** Single skill giving access to 300+ premium APIs (web search, image generation, email sending, etc.) with a free USDC wallet via x402/MPP ([awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)).

---

## Opinion Section

> **Everything below is marked as opinion. Confidence percentages are estimates, not measurements. Ewan picks.**

### Obvious load-out for Amplified Partners (load immediately)

**Opinion (80% confidence):** For the UK SMB advisory context, 32 repos, Beast deployment, Five Rods framework, deterministic-first 90/10, and step-away goal, the following are almost certainly worth loading from day one:

- `productivity/linear` — 32 repos produce issues constantly; Linear is already in the Beast stack. Loading this means Hermes can triage, create, and update tickets without human relay.
- `github/github-pr-workflow` + `github/github-code-review` + `github/github-issues` + `github/github-repo-management` — Hermes reading and writing `Amplified-Partners/hermes` (spine) requires these as baseline. Any Cove/coding workflow leans on them.
- `official/security/1password` — Beast has 36+ Docker containers; secrets management via `op` is clearly lower-risk than plaintext `.env`. The MAESTRO doctrine makes this a baseline, not optional.
- `official/devops/docker-management` — Beast runs Docker; Hermes will inevitably need to inspect containers, logs, and Compose stacks during incident response.
- `devops/webhook-subscriptions` — event-driven automation rather than cron-only is consistent with deterministic-first 90/10; webhooks from CI/CD, GitHub, Beast health checks all wire into this.
- `note-taking/obsidian` — PUDDING Vault ingestion, breakthrough-rule surfacing, and taxonomy maintenance all require a note-management skill. Obsidian is the documented vault system.
- `productivity/google-workspace` — Amplified Partners operates in GSuite; calendar, Gmail, Drive are operational necessities.

**Opinion (70% confidence):**

- Spine-write discipline as first custom SKILL.md — not a hub skill, but a custom `Amplified-Partners/hermes/skills/spine-write.md` that operationalises the breakthrough rule. Without this, the spine degrades into a static document.
- Uptime monitoring cron template (manual setup, no separate skill) — Beast at £XXX/month with 36+ containers benefits from Hermes running `check-uptime.py` every 30 minutes.

### Load if/when needed (conditional load)

**Opinion (65% confidence):**

- `optional/productivity/telephony` — only worth loading when a client-facing voice automation use case exists. Jesmond Plumbing pilot (trades context) is a plausible trigger: appointment confirmation calls, callback queues.
- `optional/email/agentmail` — worth loading when Hermes needs an autonomous email address distinct from Ewan's. Not needed until Hermes has delegated client communication authority.
- `productivity/notion` — load only if a client uses Notion. Don't load speculatively.
- `social-media/xurl` — load when X/Twitter outreach becomes active. Currently no evidence it's in the Amplified Partners workflow.
- `media/youtube-content` — useful for research and competitive analysis; load when that workflow is live.
- `optional/research/qmd` — load when the Vault grows large enough that FTS5 alone misses relevant documents. Not Day 1.
- `optional/research/scrapling` — load when a specific web extraction task requires Cloudflare bypass or spider crawling. Not a standing load.
- `optional/mlops/chroma` or `qdrant-vector-search` — load when a RAG use case is explicitly designed. Beast has FalkorDB; the graph DB already handles some knowledge retrieval.
- `optional/health/fitness-nutrition` — personal-use load; irrelevant to commercial operation. Load only if Ewan wants it.

### Probably bloat (avoid for now)

**Opinion (60% confidence):**

- The full MLOps cluster (`axolotl`, `trl`, `unsloth`, `vllm`, `pytorch-fsdp`, `torchtitan`, etc.) — Amplified Partners is not a model training operation. Nous Research built Hermes partly to consume their own MLOps toolchain; that's not Amplified Partners' situation.
- `optional/mlops/hermes-atropos-environments` / RL training — same reason. Not a fine-tuning pipeline context.
- `optional/health/neuroskill-bci` — requires dedicated BCI hardware. Niche even within Hermes's user base.
- `gaming/*` (Minecraft, Pokémon) — clearly out of scope.
- `red-teaming/godmode` — jailbreak skills carry IBAC risk in a shared-gateway context. If loaded, must be allowlisted to a specific user only.
- `optional/blockchain/*` (Base, Solana, Chainlink) — load only if a client use case requires on-chain data.
- `media/spotify`, `smart-home/openhue` — personal assistant loads; not commercial. Decide separately.
- `creative/baoyu-comic`, `creative/ascii-video`, `creative/pixel-art`, `creative/touchdesigner-mcp`, `creative/manim-video` — creative/media capabilities with no current Amplified Partners application. Low bloat risk individually; collectively they expand the system prompt surface for no current return.
- `yuanbao` — China-specific platform; not relevant to UK SMB context.

### A note on the spine and capability selection

**Opinion (75% confidence):** The spine architecture changes the load calculus. Because `Amplified-Partners/hermes` is git-backed, permanently accessible to other agents, and loaded at session start, it is the right place to encode which skills are canonical for this deployment. A `skills-manifest.md` in the spine — listing the currently loaded skills and the rationale for each — gives Cassian and Mirror observability into Hermes's capability state without requiring Hermes to be alive. This is the Radical Transparency principle applied operationally. The catalogue above gives Ewan the full inventory; the spine makes the choices visible and auditable.

---

*Cassian-research-subagent — 2026-05-05*

**Sources:**
- [Hermes Agent Bundled Skills Catalog](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog)
- [Hermes Agent Optional Skills Catalog](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog)
- [Hermes Skills Hub](https://hermes-agent.nousresearch.com/docs/skills)
- [Hermes Skills System docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)
- [Hermes Tools & Toolsets](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools)
- [Hermes Security docs](https://hermes-agent.nousresearch.com/docs/user-guide/security)
- [Hermes ACP Editor Integration](https://hermes-agent.nousresearch.com/docs/user-guide/features/acp)
- [Hermes WhatsApp docs](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/whatsapp)
- [Hermes Automation Templates](https://hermes-agent.nousresearch.com/docs/guides/automation-templates)
- [Hermes 1Password skill](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/security/security-1password)
- [Hermes Docker Management skill](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management)
- [Hermes Telephony skill](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/productivity/productivity-telephony)
- [agentskills.io specification](https://agentskills.io/specification)
- [0xNyk/awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)
- [Ken Huang Substack — Chapter 11: Cron/Webhook](https://kenhuangus.substack.com/p/chapter-11-hook-event-driven-automation)
- [Ken Huang Substack — Chapter 13: MCP Integration](https://kenhuangus.substack.com/p/chapter-13-mcp-integration-connecting)
- [Ken Huang Substack — Chapter 9: Observability](https://kenhuangus.substack.com/p/chapter-9-observability-and-debugging)
- [Repello AI — Hermes Agent Security](https://repello.ai/blog/hermes-agent-security)
- [DEV Community — 5-Layer Security Model](https://dev.to/thedailyagent/the-5-layer-security-model-every-ai-agent-needs-in-production-36l3)
- [1Password — Agent Skills Security Benchmark](https://1password.com/blog/ai-agent-security-benchmark)
- [Bruce on AI Engineering — Hermes v0.9.0 guide](https://www.heyuan110.com/posts/ai/2026-04-14-hermes-agent-guide/)
- [Hostinger — Hermes use cases](https://www.hostinger.com/tutorials/hermes-agent-use-cases)
- [Julian Goldie — Hermes OMI Obsidian](https://juliangoldie.com/hermes-omi-obsidian/)
- [strapi.io — What are Agent Skills](https://strapi.io/blog/what-are-agent-skills-and-how-to-use-them)
