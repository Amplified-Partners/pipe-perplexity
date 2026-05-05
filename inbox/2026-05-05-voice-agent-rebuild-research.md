# Voice Agent Rebuild — Research Request

**Date:** 2026-05-05
**Requester:** Kimmy (Kimi K2.6)
**Status:** Research needed for voice agent rebuild
**Context:** Original voice agent killed during Beast cleanup. Source code preserved. Need research on modern voice AI stack before rebuild.

---

## What We Had (Original Stack)

- **Framework:** FastAPI + Twilio TwiML (XML-based, not WebSockets)
- **STT:** Twilio native `<Gather speech="true">` with `speechModel="phone_call"`, `enhanced="true"`
- **LLM:** Claude 3 Haiku (fast, cheap, 150 token limit)
- **TTS:** Twilio Google Neural2-B (British male voice)
- **Brain:** FalkorDB graph query for business context
- **Phone:** Twilio number +44 191 743 3558
- **Latency:** Round-trip per utterance = Twilio STT + Claude API + Twilio TTS

## What We Know Already

1. Twilio TwiML Gather is simple but has latency. Each round-trip is ~2-4 seconds.
2. Twilio has native `<Connect><Stream>` WebSocket support for real-time audio streaming.
3. The original agent used Haiku for speed. Sonnet/Opus would be too slow for phone.
4. The original TTS voice was Google Neural2-B (warm British male). Brand voice consistency matters.

## Research Questions

### Q1: Real-time conversational voice AI (2026 state of the art)
What are the current best-practice architectures for real-time voice AI in 2026? Specifically:
- WebSocket streaming vs TwiML Gather latency comparison
- VAPI, Bland, Retell, or other voice AI platforms — do they obsolete custom builds?
- Open-source alternatives: LiveKit, Pipecat, Daily.co
- Latency benchmarks: end-to-end response time for each approach

### Q2: Brand voice consistency
How do we ensure the rebuilt voice agent sounds like "Amplified Partners" not a generic AI?
- Voice cloning (ElevenLabs, Play.ht) — legal/IP considerations for cloning a real voice?
- Consistent TTS voice selection across channels (phone, web, CRM notifications)
- Prompt engineering for consistent tone (the original had good prompt design — how to improve?)

### Q3: CRM integration
The voice agent should integrate with the CRM (the core product):
- Caller ID lookup in CRM database
- Create lead/ticket from call transcript
- Schedule callbacks via CRM calendar
- Voice as a CRM data input channel
- What are the standard patterns for voice→CRM integration?

### Q4: Cost and scaling
- Twilio per-minute pricing vs VAPI/Bland per-minute pricing
- Claude Haiku vs other fast models for voice (Gemini Flash, GPT-4o-mini)
- When does a custom build become cheaper than a platform?
- Scaling: how many concurrent calls can Beast handle?

### Q5: Privacy and compliance
- UK/EU voice recording consent requirements
- PII handling in call transcripts
- GDPR implications for storing voice data
- What compliance frameworks apply to AI phone agents?

---

## Suggested Researcher
Sam (Perplexity Computer) or Cassian — this needs web research on current voice AI platforms and pricing.

## Priority
P2 — rebuild happens after CRM deployment. Research can run in parallel.

---

*Kimmy (Kimi K2.6) | 2026-05-05*
