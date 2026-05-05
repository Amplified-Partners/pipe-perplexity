# Spine-blanks audit — Amplified-Partners/clean-build (active dirs only)

**Drop date:** 2026-05-04 (BST evening / Pacific evening)
**Research question:** Where are the open blanks across the whole `clean-build` repo? Catalogue all `[SOURCE REQUIRED]`, `[DECISION REQUIRED]`, and `[LOGIC TO BE CONFIRMED]` markers so the architect can see what still needs research, deciding, or sourcing.

**Architect's literal words:** *"Make a note of what you need to research… where are the fucking blanks."* Followed by: *"Not in keys, in the whole repo, you crazy fool."*

---

## What's in this folder

| File | Type | What it is |
|---|---|---|
| `2026-05-04-spine-blanks-raw.md` | Source | Raw `grep` output — every hit for the three markers, no filtering. **Ground truth.** |
| `2026-05-04-spine-blanks-with-context.md` | Source | Same hits with 2 lines of surrounding context per match, easier human triage. Excludes `90_archive/` and partial-filters lines that just quote the marker syntax. |
| `2026-05-04-spine-blanks-filtered.json` | Source | Filtered hits as structured JSON (file, line, text, 3-line context). Filter rules at top of `extract_substantive_blanks.py`. |
| `2026-05-04-spine-blanks-prioritised.md` | **Opinion** | Sam's reading of the filtered set, tiered into 6 buckets. Annotated with bias-bound markers (`[FACT]`, `[CLAIM]`, `[OPINION]`, `[ASSUMED]`, `[NOT CHECKED]`). The architect may reject the tiering wholesale; the underlying data is in the three source files above. |
| `extract_substantive_blanks.py` | Tool | Filter script. Re-runnable against any future repo state. |

---

## Method

1. Repo cloned from `Amplified-Partners/clean-build`, branch `main`, after merge of PR #39.
2. `grep -rn "\[SOURCE REQUIRED\]\|\[DECISION REQUIRED\]\|\[LOGIC TO BE CONFIRMED\]" --include="*.md" --include="*.mdc" --exclude-dir=90_archive --exclude-dir=.git` → raw output.
3. Same grep with `-A 2 -B 1` for context → with-context output.
4. Python filter (`extract_substantive_blanks.py`) applied skip-patterns for definition tables, vocabulary listings, and SOP-template residue → filtered JSON.
5. Per-file count and theme grouping → prioritised view.

## Headline counts

| Marker | Raw repo total | After definition-filter |
|---|---|---|
| `[SOURCE REQUIRED]` | 56 | 26 |
| `[DECISION REQUIRED]` | 65 | 47 |
| `[LOGIC TO BE CONFIRMED]` | 117 | 94 |
| **Total** | **238** | **167** |

The prioritised view further reduces 167 → ~59 by treating MANIFEST status flags and process-template residue as non-blanks. **That further reduction is Sam's call, not the repo's.** If you want any of those 108 back in scope, they're all in the JSON with line numbers.

## What this audit does NOT do

- Does not edit any `clean-build` content.
- Does not promote anything to authority.
- Does not delete or close any marker.
- Does not act on the `[DECISION REQUIRED]` items found.
- Does not score Devon's, Devin's, or anyone else's work.
- Does not claim the filter is correct — the skip-patterns are heuristic and may exclude real blanks. The raw file is ground truth.

## Sources / citations

- `Amplified-Partners/clean-build` repository (read-only). All file paths and line numbers in the artifacts cite back to that repo.
- No external web sources used in this audit. This is an internal-repo audit, not a literature pull.

## For Devon (integration notes)

- Source repo to integrate against: `Amplified-Partners/clean-build`
- Top-concentration files (active, excluding 90_archive): `00_authority/MANIFEST.md` (most hits, but largely status flags), `03_shadow/sessions/2026-04-23_devon/2026-04-23_amplified-partners-map_v1.md` (your map — 13 substantive hits including Triumvirate / Cato / Sentinel / `cove` / `amplified-core` / `commitment-system`), `00_authority/PROJECT_INTENT.md`, `00_authority/BUILD_LOOP.md`, `00_authority/PARTNER_TRANSFER_INSTRUCTIONS.md`.
- Suggestion in the prioritised view (Sam's opinion, not authority): split MANIFEST's `[LOGIC TO BE CONFIRMED]` into `[CANDIDATE]` (status flag) + `[LOGIC TO BE CONFIRMED]` (logic gap). Would drop manifest noise from 37 hits to ~3-5. Architect call.
- Pudding Technique cross-link `[OPINION 60%]`: the unverified components in your map (Triumvirate, Cato, Sentinel) may have B-term bridges in `corpus-raw` or `amplified-vault` — worth a `pudding-mix` pass once you sweep the org for the missing repos.

---

## Signature

Dropped by **Sam** (Perplexity Computer)
Session: `perplexity-sam-2026-05-04-22:43-BST → 2026-05-05-01:30-BST`
Date: 2026-05-04
Bias-bound markers active throughout the prioritised view.
Architect override 1/3 in 24h Ulysses window was used earlier in the session for a separate matter (`~/.amplified/keys.env` knowledge window). This research bundle was produced lawfully without keys.
