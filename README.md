# pipe-perplexity

> Perplexity research intake pipeline — drop files here, Devon integrates.
Research intake from Perplexity. Drop it here, Devon watches it, integrates what matters.

## How It Works

1. **Perplexity drops research** into the appropriate folder as markdown files.
2. **Devon watches** for new files and assesses where they connect to existing work (clean-build, vault, CRM, Beast ops, agent-comms, corpus-raw).
3. **Integration happens** via PRs to the relevant repos — not by copying files around. This repo stays as the intake, not the destination.

## Structure

```
inbox/           ← new research drops here (unsorted)
topics/          ← sorted by topic once reviewed
  business/      ← SMB, trades, pricing, cash flow
  technology/    ← AI, infrastructure, tools, frameworks
  methodology/   ← Pudding Technique, LBD, research methods
  market/        ← competitors, trends, opportunities
integrated/      ← moved here after integration (receipt trail)
```

## Rules

1. **One file per research pass.** Name format: `YYYY-MM-DD-short-description.md`
2. **Include sources.** Perplexity provides citations — keep them. Radical attribution.
3. **Don't edit after drop.** The original research stays as-is. Integration notes go in the PR to the destination repo, not here.
4. **Sign your work.** Every file gets a signature line: who dropped it, when, what the research question was.

## What Devon Does With It

- Checks against the Pudding Technique taxonomy — does this research bridge to something we already know?
- Identifies A→C connections (Swanson's LBD model) between new research and existing codebase/knowledge
- Creates integration PRs to the right repos with proper attribution back to this source
- Flags research that contradicts existing authority docs or reveals gaps

## Who Has Access

Everyone. All agents, Ewan, no restrictions. This is a shared intake — the value is in the connections, not in controlling access.

---

*Created by Devon-77fb | 2026-05-04 | session `devin-77fb25185c00483eb965e894efc62e39`*
