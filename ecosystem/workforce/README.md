# 🏢 OmniClaw Workforce — The Autonomous Agent Army

> **The Corporate Brain of OmniClaw.**
> Defines WHO does WHAT, under WHOSE command, with WHICH rules.
> System Integrity Level: V5.0 Consolidated

---

## What Is This?

The Workforce is OmniClaw's **Organizational Chart** — a fully declarative governance layer that maps out every AI Agent, Subagent, Department, and Daemon identity in the system. It contains **zero executable code**. All runtime logic lives in [`core/daemons/`](../../core/daemons/) and [`ecosystem/workflows/`](../workflows/).

Think of it as the HR manual for an AI corporation:
- **Departments** define command chains and capability inventories.
- **Prompts** define how each Agent behaves when activated.
- **Rules** define what each Agent is allowed and forbidden to do.

---

## Directory Structure

```
workforce/
├── departments/                    # 28 functional business domains
│   ├── engineering/                # Software engineering corps
│   │   ├── department.md           # Agent roster + capabilities
│   │   ├── manager_prompt.md       # System prompt for dept manager
│   │   ├── worker_prompt.md        # System prompt for dept workers
│   │   ├── rules.md                # Department governance rules
│   │   └── _DIR_IDENTITY.md        # Identity tag
│   ├── security_grc/               # Security & compliance
│   ├── rd/                         # Research & development
│   ├── ... (25 more departments)
│   └── _REGIONAL_MAP.md            # Full department index
│
├── system/                         # Declarative system config
│   ├── corp_prompts/               # Global prompt templates
│   │   ├── master_prompt.md        # Tier-1 Orchestrator identity
│   │   ├── ceo_prompt.md           # CEO interaction rules
│   │   ├── csuite_prompt.md        # C-Suite behavioral guidelines
│   │   ├── manager_prompt.md       # Generic manager template
│   │   ├── worker_prompt.md        # Generic worker template
│   │   └── qa_prompt.md            # QA auditor template
│   ├── daemons/                    # Daemon metadata (YAML, NOT code)
│   │   ├── oa_daemon.yaml          # OA Academy identity
│   │   ├── oer_daemon.yaml         # OER Registry identity
│   │   ├── ohd_daemon.yaml         # OHD Health identity
│   │   └── oiw_daemon.yaml         # OIW Intake identity
│   └── system_protocol.md          # "No Code Allowed" governance
│
├── subagent_operating_guide.md     # Ops manual for Dev/QA/Researcher roles
├── _DIR_IDENTITY.md                # Root identity card
└── _REGIONAL_MAP.md                # Zone geography
```

---

## The 28 Departments

| Category | Departments |
|----------|-------------|
| **Core Tech** | `engineering`, `rd`, `qa_testing`, `it_infra` |
| **Operations** | `operations`, `orchestration`, `planning_pmo`, `facility` |
| **Content** | `content_intake`, `content_review`, `asset_library` |
| **Corporate** | `hr_people`, `finance`, `legal`, `marketing`, `strategy` |
| **Security** | `security_grc`, `system_security`, `system_integrity` |
| **System** | `system_daemons`, `system_health`, `registry_capability` |
| **Customer** | `client_reception`, `ux_design`, `support` |
| **Knowledge** | `od_learning`, `archivist`, `monitoring_inspection` |

Each department folder contains a standardized set of governance files defining its agent roster, behavioral prompts, and operational rules.

---

## How Agents Are Organized

Agents and Subagents are **nested within their departments**. Each `department.md` file contains the complete workforce roster:

```markdown
## Workforce Roster
- **backend-architect-agent** (active): Worker for engineering
- **frontend-agent** (active): Worker for engineering
- **sre-agent** (active): Worker for engineering
```

There are no separate `agents/` or `subagents/` directories. The Department IS the organizational unit.

---

## Key Governance Documents

| Document | Location | Purpose |
|----------|----------|---------|
| **Subagent Operating Guide** | `subagent_operating_guide.md` | Defines DEVELOPER/QA/RESEARCHER workflow patterns, MQ Protocol, Receipt Schema |
| **System Protocol** | `system/system_protocol.md` | Enforces "No Code Execution" rule for the system/ quadrant |
| **Master Prompt** | `system/corp_prompts/master_prompt.md` | Full OmniClaw identity block for bootstrapping AI sessions |

---

> ⚠️ **Zero-Trust Rule**: This entire directory is DECLARATIVE ONLY. Any `.py`, `.bat`, or `.ps1` files found here are in violation and must be relocated to `core/` or `ecosystem/tools/`.
