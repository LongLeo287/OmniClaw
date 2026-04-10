---
id: core_ops_integrators
type: module
owner: OIW
supervising_daemon: OIW
managing_agent: civ-agent
department: 19 Content Intake/CIV
description: Core repository intake routers and tracking integrators from AI OS V3.1. Handled by OIW and CIV pipeline to register and sync telemetry and capabilities.
tags: ["integration", "telemetry", "legacy", "intake", "civ"]
---

# Integrators & Intake Logistics

Assimilation of legacy AI OS remote integration scripts.

Utilized by `civ-agent` during Content Intake (Pipeline: CIV -> OIW -> OA) for continuous monitoring, repository pulling, batch cloning operations via external interfaces (Github/Telegram) and pushing updates to `SKILL_REGISTRY.md` via `registry-manager-agent`.
