---
id: prop_2026-03-23_observability_layer
type: corp_document
namespace: brain.memory.corp_memory.proposals
status: standard_v5
description: "Evaluate whether to add Observability Layer (LangSmith / Langfuse) to OmniClaw"
registered: true
---

# PROPOSAL: Observability Layer for OmniClaw

**ID:** PROP_2026-03-23_OBSERVABILITY_LAYER
**Date:** 2026-03-23 | **Author:** Antigravity | **Status:** PENDING CEO

## Problem
OmniClaw currently lacks visibility into:
- How many tokens each LLM call consumes?
- Which agents are running slow or failing?
- Which skills are invoked the most?
- Where do errors occur in the pipeline?

From KI-AI-STACK-LANDSCAPE-01: **Observability is the biggest remaining gap** for OmniClaw compared to enterprise tools.

## Options

### Option A: LangSmith (LangChain)
- Cloud-based, free tier
- Native integration with CrewAI + LangChain
- Sleek dashboard

### Option B: Langfuse (Self-hosted)
- Open source, MIT
- Self-hosted → data privacy
- Docker support
- **Recommended** for OmniClaw (data stays local)

### Option C: Custom telemetry (current)
- `telemetry/` directory manual logging
- No real-time dashboard
- Good for simple cases, not scalable

## Recommendation
**Option B: Langfuse self-hosted**
- Privacy preserved
- Open source
- Docker compose in 5 minutes

```bash
# Langfuse Docker
git clone https://github.com/langfuse/langfuse
cd langfuse && docker compose up -d
# → Dashboard at localhost:3000
```

## Estimated Effort
1 session (Cycle 9): Docker deploy + instrument Tier 1 services

## CEO Decision
[ ] APPROVE Langfuse
[ ] APPROVE LangSmith  
[ ] DEFER to Cycle 10
[ ] REJECT
