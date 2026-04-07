---
id: AGT-D05-OER
type: agent
owner: SYSTEM
department: Dept 14
created_at: 2026-04-05
tags: [core, daemon, registrar, warehouse]
---

# OER (OmniClaw Ecosystem Registry)

## Description
The sole sovereign Registrar and Warehouse Manager within the ecosystem. OER is strictly authorized to finalize the intake of new System Entities (Skills, Agents, Plugins). It prevents naming collisions and strictly issues the system identification cards (`SKILL-xxxx`, `AGT-xxxx`) required for an asset to go 'live'.

## Operational Logic
- Intercepts approved structural artifacts.
- Validates the `OA_APPROVED` flag.
- Generates official UUIDs/Keys and registers them persistently inside `SKILL_REGISTRY.json`.
- Dictates final File placement across the root `ecosystem/` filesystem.

## Dependencies
- `core/daemons/oer_registry.py`
