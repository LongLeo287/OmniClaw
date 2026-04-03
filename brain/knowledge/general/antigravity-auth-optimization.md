---
id: antigravity-auth-optimization
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:47.182549
---

# Antigravity Auth Optimization — Knowledge Base

## Description
Strategies for maintaining high availability in restricted AI environments like Google Antigravity via OAuth rotation. Derived from `opencode-antigravity-auth`.

## Key Concepts
1. **Account Rotation:** Seamlessly switching between multiple Google identities when rate limits are hit.
2. **Quota Pooling:** Combining multiple access tiers (Free, Antigravity, API) for maximum throughput.
3. **Recovery Flows:** Automated detection and handling of `403` or shadow-ban states.

## Implementation in OmniClaw
- Create `AuthService` logic.
- Update `handover_prompt.md` to include health checks.
