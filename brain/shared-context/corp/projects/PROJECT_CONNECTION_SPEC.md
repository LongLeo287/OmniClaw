# Project Connection Protocol — OmniClaw v3.0
# Authority: Tier 0 (Constitution)
# Updated: 2026-03-16

> **Purpose:** Defines the standard protocol for any external project to connect to and leverage OmniClaw capabilities (skills, channels, knowledge, agents).

---

## Core Concept

```
┌─────────────────────────────────────────────┐
│              EXTERNAL PROJECT               │
│  (React app, GAS backend, CLI tool, etc.)   │
│                                             │
│  [.agent/CLAUDE.md]  ← reads OmniClaw skills  │
│  [.clauderules]      ← workspace rules      │
│  [.claudeignore]     ← scope limits         │
└────────────────┬────────────────────────────┘
                 │ registers via
                 ▼
┌─────────────────────────────────────────────┐
│              OmniClaw CORE                     │
│  registry.json  ← project catalog          │
│  skills/        ← shared capabilities      │
│  knowledge/     ← shared intelligence      │
│  channels/      ← remote bridge (optional) │
└─────────────────────────────────────────────┘
```

---

## Connection Steps (for a new project)

### Step 1: Register in `registry.json`

Add entry to `$OMNICLAW_ROOT\registry.json`:

```json
"PRJ-XXX": {
  "name": "Project Display Name",
  "path": "D:\\path\\to\\project",
  "description": "One-line description",
  "status": "active",
  "skills_used": ["skill-name-1", "skill-name-2"],
  "channels_enabled": false,
  "data_sources": ["google-sheets", "local-sqlite"],
  "contact_agent": "claude_code",
  "config_path": "$OMNICLAW_ROOT\\projects\\PRJ-XXX\\CLAUDE.md",
  "workflows_path": "$OMNICLAW_ROOT\\projects\\PRJ-XXX\\workflows\\"
}
```

Use `scripts/register_project.ps1 -Id PRJ-XXX -Name "..." -Path "..."` to automate.

---

### Step 2: Create Project Config in `projects/PRJ-XXX/`

```
projects/PRJ-XXX/
├── CLAUDE.md          ← Project-scoped identity (load OmniClaw skills)
└── workflows/         ← Project-specific workflows
    ├── deploy.md
    └── debug.md
```

The `CLAUDE.md` must start with:
```markdown
# Project: [Name] — OmniClaw Connected
# PRJ-ID: PRJ-XXX
# reads-from: $OMNICLAW_ROOT\CLAUDE.md

## Skills Loaded
- [ui-ux-pro-max](../../skills/domains/frontend/ui-ux-pro-max/SKILL.md)
- [pos-event-sourcing](../../skills/domains/pos/pos-event-sourcing/SKILL.md)
```

---

### Step 3: Configure Project Workspace

In the project directory, create `.clauderules` (or `.agent/CLAUDE.md`):

```markdown
# Workspace Rules — [Project Name]
# Connected to OmniClaw: $OMNICLAW_ROOT

## Identity
This workspace is a satellite project of OmniClaw.
When coding here, Antigravity has full authority per OmniClaw hierarchy.

## Skills Available
See: $OMNICLAW_ROOT\shared-context\SKILL_REGISTRY.json

## Handoff
For complex tasks: follow $OMNICLAW_ROOT\workflows\claude_code_handoff.md
```

---

### Step 4: Run Gatekeeper (first access)

```powershell
# From OmniClaw root
.\gatekeeper.ps1 -ProjectId PRJ-XXX
```

If GRANT → project is active in OmniClaw ecosystem.

---

## Project Status Lifecycle

```
DRAFT → ACTIVE → MAINTENANCE → ARCHIVED
```

| Status | Meaning |
|--------|---------|
| `draft` | Being set up, not yet registered |
| `active` | Fully connected, regular work happening |
| `maintenance` | Minimal activity, skills still loaded |
| `archived` | No longer active, knowledge preserved |

---

## What OmniClaw Provides to Connected Projects

| Resource | Location | How to Use |
|----------|----------|------------|
| Skills | `skills/` + `skills/domains/` | Reference in project CLAUDE.md |
| Knowledge | `knowledge/` | Read via knowledge_navigator skill |
| Channel Bridge | `channels/` | Set `channels_enabled: true` in registry |
| Shared Agents | `agents/` | Invoke via blackboard.json |
| Orchestrator | `blackboard.json` | Write task payload → OmniClaw picks up |

---

## Quick Reference: Auto-Register Script

```powershell
# Tạo project mới và register tự động:
.\scripts\register_project.ps1 `
  -Id "PRJ-005" `
  -Name "My New Project" `
  -Path "D:\MyProject" `
  -Description "Brief description" `
  -Skills @("ui-ux-pro-max") `
  -Channels $false
```

---

*"Every project is a satellite. OmniClaw is the operating system they orbit."*

