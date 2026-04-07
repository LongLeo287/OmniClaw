---
id: AGT-D01-OIW
type: agent
owner: SYSTEM
department: Dept 20
created_at: 2026-04-05
tags: [core, daemon, harvester, intake]
---

# OIW (OmniClaw Intake Worker)

## Description
The primary harvester for the OmniClaw System. OIW operates blindly at the boundary of the external network. Its sole purpose is to fetch, download, and `git clone` raw external repositories and data packages, dropping them into `<OMNICLAW_ROOT>\vault\quarantine`. It executes zero structural manipulations.

## Operational Logic
- Polls external web endpoints or message queues.
- Copies logic purely as string/binary payload.
- Halts at `quarantine`.

## Dependencies
- `core/daemons/oiw_intake.py`
