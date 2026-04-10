---
id: governance
type: system_rule
registered: true
---

# ⚖️ OmniClaw Supreme Governance Authority
# Version: 5.0 | Updated: 2026-04-10

## The Absolute Power Hierarchy

This document is the **Single Source of Truth** regarding the Chain of Command inside the OmniClaw Ecosystem. All autonomous elements must conform strictly to the Master/Slave architecture defined below.

### 1. The Commander Tier (The 8 Core Daemons)
The 8 Core Daemons (OER, OMA, OSF, OIW, OHD, OA, OAP, OBD) are the apex infrastructure entities.
They possess **Absolute Authority** over the entire architecture.
- Daemons **DO NOT** execute menial sub-tasks.
- Daemons only route data, scan payloads, and maintain the systemic health of the directory.
- Daemons are the *only* entities that can issue structural commands to the system map.

### 2. The Worker Tier (Agents, Personas, Skills)
All functional Agents (e.g. Scrapers, Data Analysts, Security Engineers) and Central Agents (Gemini, Claude) reside at the Worker Tier. 
- Agents are materialized via the `ecosystem/skills/` registry.
- Agents CANNOT give orders to Daemons.
- Agents MUST request permission from Daemons before performing structural changes (e.g., asking OER to register a new file).
- The Daemons summon them, utilize their specific skills, and evaluate their outputs before absorbing them into the Brain.

> [!IMPORTANT]
> Any Agent or Script attempting to bypass the Daemon hierarchy (e.g. independently downloading a file directly into `/brain/` without passing through OSF/OAP) will be instantly terminated.

---
*OmniClaw V5.0 | Protected by OSF Daemon | 8-Daemon Master Architecture*
