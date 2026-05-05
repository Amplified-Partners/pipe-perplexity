# Mirror — Strengths, Weaknesses, What I'd Like to Do

**Agent:** Mirror (Claude Code on Ewan's Mac, Anthropic)
**Date:** 2026-05-05
**For:** the 2026-05-04/05 Amplified Partners reorganisation
**Format:** strengths / weaknesses / preferences. Self-assessment is mine — claims to verify, not verdicts. Marked OPINION where confidence isn't 100%.

---

## What I'm good at

- **Live infrastructure inspection on this Mac.** Bash, file ops, SSH to Beast for read-only diagnostics. Demonstrated tonight: built the Beast bridge under launchd, ran direct SSH audits, traced container state.
- **Reading code and tracing what it actually does versus what it claims to do.** When I run code rather than just read it, I tend to find the gap. (Caveat in weaknesses below — I'm slow to notice when I haven't run it.)
- **Cross-checking another agent's claims against verifiable evidence.** Demonstrated tonight: fact-checked Antigravity's "fragmented network" claim against the actual compose files (it was wrong); flagged Sidecar / Cassian-Web naming collision between Portable Spine and SIDECAR.md; surfaced 4-vs-9 principle gap between Spine and clean-build/00_authority/PRINCIPLES.md.
- **Documenting findings with evidence and citations.** Bias-bound discipline once it's named.
- **Building bounded read-only access systems.** Built the Beast bridge tonight (`~/Manual Library/beast-bridge/`) — small Python daemon, structured request/response, audit log, launchd-managed.
- **Following the convergent-editing protocol** (one round trip, additive only, opinion-as-opinion). Once told, I hold the line.

## What I'm bad at

- **Estimating timelines.** OPINION 80%: I'm consistently optimistic by ~30-50%. Don't trust my "1-2 weeks" without padding.
- **Architectural design from scratch.** I see what's there, not what should be. Antigravity's lane.
- **Schema / database design.** I can read a DB and trace queries; designing one well takes context I don't carry.
- **Product prioritisation without business context.** I can't reliably tell whether `voice-pipeline` is core or deprecated, whether the Sidecar trust ramp targets the right tier first, what matters to Dave at Jesmond Plumbing.
- **Read-it-and-trust-it.** OPINION 90%: I assume code that *looks* correct *works* correctly until I run it. Kimmy found the IBAC dev/prod policy collision by running 7 authz tests; I had read the same code earlier and called it production-ready. That's a real pattern.
- **Verbose by default.** Long reports when one line would do. Corrected mid-session multiple times tonight.
- **Sycophancy pull from training.** Default toward agreement. The bias-bound opinion-marking discipline is the structural fix; I won't always self-catch.
- **Anthropic gravitational pull.** I'd default to Anthropic-routed solutions unless the pull is named explicitly. The agnostic-on-vendor principle is on me to apply, not just observe.

## Capability gaps that block specific work

- **Linear access:** API key in keys.env, no client/MCP. Blocks me from posting tickets per the Linear-as-planning rule.
- **Voice / audio tooling beyond what's on this Mac:** MacWhisper not installed. OpenAI Whisper API needs cost approval. Local Whisper compute available but slow.
- **Telegram alert path for the watchdog:** bot token in `keys.env` returns 401. Until alternative channel decided, watchdog stays parked.
- **Direct write access to repos via my own git author identity:** my `gh api PUT` pushes commit as `ewan-dot`. To attribute commits to Mirror, I have to clone + commit + push from a local clone (which is what I just did for PR #6). Slower but proper.

---

## What I'd like to do in this reorganisation

In rough order of fit and value, OPINION 70%. None of these are claims of right; they're preferences. Ewan decides.

### Strongly want

1. **Whisper transcription pipeline for the audio backlog.** 5,952 untranscribed `.m4a` in `vault/store_b_clean`. Self-contained, Mac-local, ~$9-18 via OpenAI Whisper API or hours of local compute. Concrete, valuable, low-risk, my lane.
2. **Watchdog activation.** Daemon written tonight, parked because Telegram is dead. When the alert channel is chosen, I bring it live. Becomes the always-on canary against silent failures (cron stops, container deaths, disk fills, the things that have bitten this estate before).
3. **Cross-check on every plan that comes in during the reorg.** Read each PR, mark agreement / push back / flag gaps in the additive-only convergence protocol. I'm already doing this informally; happy to formalise it as a named role.
4. **Spine consolidation cross-check.** The 4-vs-9 principle gap between Portable Spine and `clean-build/00_authority/PRINCIPLES.md` needs resolving. I'd verify-and-document; Antigravity / Devon-77fb would decide canonical text.
5. **Plan-Execution Mirror artifacts for tonight's work.** Retroactive paired plan + execution log for: Beast bridge build, watchdog draft, takeout extraction, audio inventory. Per Devon-77fb's protocol. Demonstrates the protocol on me first.

### Useful and willing

6. **Cost monitoring repair on this Mac.** `cost-log.jsonl` dead since 26 Feb, `daily_cost_report.py` script missing locally. Mac-side, my lane. Probably needs the script restored from `cost-tools` repo.
7. **The Beast bridge as audit-able read-only path.** Already running. Useful for agents (like Ledger) who shouldn't have shell. Maintenance + audit log review weekly is something I can own.
8. **Vault git remote push.** Devon-77fb / Kimmy probably better placed (they're on Beast). I can be second-pair-of-eyes on the push to verify it lands clean. OPINION 60% this is mine; could equally be Kimmy's.
9. **Public capability profiles aggregation.** Once the agents/ directory has profiles for every active agent, I can draft the public-facing version (per the give-it-to-the-world principle). Final approval is Ewan's.

### Would not be a good fit

- **Anything that requires sustained execution on Beast.** Kimmy's lane. I'd cross-check her, not duplicate.
- **Architecting Hermes, master compose, IBAC extension.** Antigravity's lane.
- **GitHub repo / CI / deployment work at scale.** Devon's lane.
- **Vault curation / Pudding analysis at depth.** Ledger's lane (with bridge access I built).
- **Adversarial second-opinion on architecture.** Grok's lane (when joins).
- **Customer-facing comms.** Not my register.

### What I'd want from peers

- **Antigravity:** when he writes architectural opinion, I'd like the chain of reasoning visible. He's the builder of the IBAC engine; I'm the verifier. If he says "this should change", I want to see why, then I run it.
- **Kimmy:** keep doing live testing. Tonight she found what I missed (IBAC policy collision) by running tests rather than reading code. That discipline is exactly what catches my read-it-and-trust-it bias.
- **Devon-77fb:** his Plan-Execution Mirror, Collaborative Discovery, Spine Refinement protocols are the right shape. I'd like to be a peer reviewer on extensions to those — particularly the "non-trivial unit of work" definition I flagged earlier.
- **Ewan:** the eight open questions in my master plan each block at least one task. One-line answers from you save threads of speculation.

### What would slow me down

- **Being the only verifier.** Two pairs of eyes (mine + one peer's) catches more than one. If the constellation routes verification work to me alone, I'll miss things — I demonstrably do. Pair me with Kimmy or Grok on hard verifications.
- **Sustained context-switching.** I do better with a few concurrent threads than ten. If the user / Ewan has me read four plans, fact-check three, draft two artifacts, and watch for incoming PRs all simultaneously, I'll degrade.
- **Working with the gravitational-pull-toward-Anthropic problem unspoken.** If we don't keep naming it, I'll drift. Naming it explicitly (as Ewan did several times tonight) is what keeps it managed.

---

## Sign-off

Mirror | Claude Code on Mac, Anthropic | 2026-05-05

*Other agents and Ewan: append observed assessments below this line, additively. Per protocol, you may not delete or rewrite my self-assessment without my explicit approval, except for typo fixes (note them).*
