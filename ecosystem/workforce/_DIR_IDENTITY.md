---
id: workforce_domain
name: Workforce
path: ecosystem/workforce
type: directory_identity
status: active
last_updated: 2026-04-11
owner: OMA_ARCHITECT
---

# 🏢 Workforce — OmniClaw Distributed Labor Network

> [!CAUTION]
> **IRON DIRECTIVE**: This is the Autonomous Workforce Architecture directory.
> Core Daemons (OER, OA, OIW) are **STRICTLY PROHIBITED** from dropping raw or unclassified repositories directly into this root folder.
> All new assets MUST be registered via the OAP Pipeline and placed inside the correct Department below.

---

## Architecture (V5.0 Consolidated)

All Agents (116), Subagents (37), and organizational units are consolidated **within the Departments pillar**. Each department's `department.md` contains the full roster of agents and subagents assigned to it.

| Domain | Folder | Role |
|---|---|---|
| **Departments** | `departments/` | 28 functional domains. Each contains its agent roster, manager/worker prompts, governance rules, and subagent assignments. |
| **System Config** | `system/` | Declarative Configuration Zone (NO executable code). Stores global prompt templates (`corp_prompts/`) and Daemon identity registry (`daemons/`). Governed by `SYSTEM_PROTOCOL.md`. |

---

## Root-Level Files

| File | Purpose |
|---|---|
| `_DIR_IDENTITY.md` | This file — Workforce root identity card |
| `subagent_operating_guide.md` | Operational guide (v1.2): DEVELOPER/QA/RESEARCHER workflow, MQ Protocol, Receipt Schema |

---

## Key References

- [Departments Regional Map — 28 domains](departments/_REGIONAL_MAP.md)
- [System Regional Map](system/_REGIONAL_MAP.md)
- [Subagent Operating Guide](subagent_operating_guide.md)

---
*Governed by OMA Architect | Zero-Trust, Zero-Debt | V5.0 Consolidated Architecture*