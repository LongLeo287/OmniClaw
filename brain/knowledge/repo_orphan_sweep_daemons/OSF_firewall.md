---
id: AGT-D02-OSF
type: agent
owner: SYSTEM
department: Dept 19
created_at: 2026-04-05
tags: [core, daemon, firewall, security]
---

# OSF (OmniClaw Sandbox Firewall)

## Description
The primary Gatekeeper of the ecosystem. OSF guards the Vault's quarantine zone. It leverages deep security scans and heuristics to identify viruses, malicious payloads, indicator of compromises (IOC), or dangerous structural anomalies before an inbound data package is allowed integration.

## Operational Logic
- Constantly watches `<OMNICLAW_ROOT>\vault\quarantine`.
- Rejects and destroys malicious inputs.
- Passes clean data payload to `OER_INBOX` queues.

## Dependencies
- `core/daemons/osf_firewall.py`
