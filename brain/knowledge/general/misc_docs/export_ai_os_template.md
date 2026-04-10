---
id: export-ai-os-template
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:23.209596
---

# Department: operations
---
description: Automated protocol for exporting a clean, project-agnostic version of the OmniClaw Headquarters for use in new projects.
---

# ðŸ“¦ OmniClaw Boilerplate Export Protocol

## Objective
To safely copy the OmniClaw "Engine" to a new project directory WITHOUT carrying over the specific context, history, or knowledge of the current project. This prevents "AI Hallucination" where the AI thinks the new project is still the old project.

## The Strategy: Engine vs Cargo
When cloning the OmniClaw, we only keep the Universal structural files (The Engine) and we wipe the specific data files (The Cargo).

### ðŸŸ¢ KEEP (The Universal Engine)
These folders contain universal logic and rules that apply to ANY project:
- `rules/` (AGENTS.md, agent_behavior.md, WORKFLOW.md)
- `workflows/` (DELEGATION_SOP, automated_cli_handoff, etc.)
- `skills/` (The actual sub-agent scripts/instructions like Archivist)
- `CLAUDE.md` / `SOUL.md` (If placed at root)

### ðŸ”´ WIPE (The Project Cargo)
These folders contain context specific to the OLD project and MUST be emptied (keep the folder structure, but delete the contents):
- `knowledge/` (Delete all architectural deep dives of the old project)
- `plans/` & `tasks/` (Delete old roadmaps, implementation plans, and task.md)
- `archive/` (Delete old brainstorms and master legacy logs)
- `brain/memory/` (Reset blackboard.json and state files)

## Export Command (Automated Script)
Run this command to create a clean `.agents-template` folder that you can copy to any new project.

```powershell
# Set source to the current OmniClaw root, dest to your target location
$source = $env:OMNICLAW_ROOT                         # or: "path\to\your\.agents" folder
$dest   = Join-Path (Split-Path $source -Parent) "OmniClaw-Template"

# Clone full structure
Copy-Item -Path $source -Destination $dest -Recurse -Force

# Wipe project-specific cargo
Remove-Item -Path "$dest\knowledge\*" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "$dest\plans\*" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "$dest\tasks\*" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "$dest\archive\*" -Recurse -Force -ErrorAction SilentlyContinue

# Create empty anchor files for the new project
New-Item -ItemType File -Path "$dest\tasks\task.md" -Value "# Task Decomposition`n`n## Objective`n[Define your new project goal here]" -Force
New-Item -ItemType File -Path "$dest\knowledge\knowledge_index.md" -Value "# Knowledge Index`n`n## Governance Core`n- [AGENTS.md](../../../.claude/skills/supabase-postgres-best-practices/AGENTS.md)`n`n## Technical Library`n[Add new project docs here]" -Force
```

