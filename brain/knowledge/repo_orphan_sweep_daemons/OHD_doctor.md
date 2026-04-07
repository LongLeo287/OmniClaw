---
id: AGT-D03-OHD
type: agent
owner: SYSTEM
department: Dept 19
created_at: 2026-04-05
tags: [core, daemon, doctor, health]
---

# OHD (OmniClaw Health Daemon)

## Description
The interior physician of the OmniClaw system. OHD traverses the internal directories mapping for structural fragmentation, caching bloat, and hidden dependencies. It generates security updates and diagnostic routines, which are explicitly shared with the OSF Firewall.

## Operational Logic
- Operates primarily out of `core/daemons/ohd_health.py`.
- Purges `__pycache__`, `node_modules` and orphan `.git` states post-assimilation.
- Audits active system logs to flag deteriorating modules.

## Dependencies
- `core/daemons/ohd_health.py`
