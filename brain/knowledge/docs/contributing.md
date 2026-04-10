---
id: contributing
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:44:27.715252
---

# CONTRIBUTING.md â€” How to Add Repos, Skills & Agents to OmniClaw
# Version: 1.0 | Created: 2026-03-16

---

## ðŸŽ¯ Overview

This guide explains how to extend OmniClaw with new repositories, skills, and agents.
Following these steps ensures security, discoverability, and proper governance.

---

## ðŸ“¦ Adding a New Repository

### Option A: Clone into plugins/ (agent-executable)
Use when: it has SKILL.md, manifest.json, or can be called by agents
```powershell
# 1. Security check (MANDATORY)
# â†’ Run: agents/security_agent â†’ scan_repo("<url>")
# â†’ Minimum score: 60

# 2. Clone
git clone --depth=1 <url> "$OMNICLAW_ROOT\plugins\<name>"

# 3. Create manifest
# â†’ plugins/<name>/manifest.json (see PLUGIN_SPEC.md)

# 4. Register in SKILL_REGISTRY.json
# â†’ brain/registry/SKILL_REGISTRY.json â†’ add entry with source="plugin"

# 5. Update knowledge index
# â†’ knowledge/knowledge_index.md â†’ add one-line reference
```

### Option B: Clone into knowledge/repos/ (reference only)
Use when: it's a learning resource, not directly callable
```powershell
git clone --depth=1 <url> "$OMNICLAW_ROOT\knowledge\repos\<name>"
# Register with source="knowledge_ref" in SKILL_REGISTRY.json
```

### Option C: Clone into REMOTE/claws/ (Claw variants)
Use when: it's a Claude/AI runtime variant
```powershell
git clone --depth=1 <url> "$OMNICLAW_ROOT\REMOTE\claws\<name>"
# Register with category="claw_variant" in SKILL_REGISTRY.json
```

### Option D: Web Analysis (can't clone â€” private/deleted)
```
1. Fetch: https://raw.githubusercontent.com/<owner>/<repo>/main/README.md
2. Create: knowledge/<name>_analysis.md
3. Register: SKILL_REGISTRY.json with source="knowledge_web"
4. Reference: knowledge/knowledge_index.md
```

---

## ðŸ”§ Creating a New Skill

Skills live in `skills/` and expose functions to all agents.

### Structure
```
skills/<skill_name>/
â”œâ”€â”€ SKILL.md        â† Required: manifest + function docs
â”œâ”€â”€ __init__.py     â† Optional: Python module
â””â”€â”€ README.md       â† Optional: user-facing docs
```

### SKILL.md Template
```yaml
---
name: my_skill
version: 1.0
tier: 3
category: <category>
description: One-sentence description
exposed_functions:
  - function_name
dependencies:
  - other_skill_id
---

# My Skill

## Purpose
...

## Exposed Functions

### function_name(arg: type) â†’ return_type
...
```

### Registration
Add to `brain/registry/SKILL_REGISTRY.json`:
```json
{
  "id": "my_skill",
  "name": "My Skill",
  "version": "1.0",
  "tier": 3,
  "status": "active",
  "source": "skill",
  "path": "skills/my_skill/SKILL.md",
  "description": "...",
  "category": "...",
  "domain": "internal",
  "cost_tier": "free"
}
```

---

## ðŸ¤– Creating a New Agent

Agents live in `agents/` (primary) or `subagents/` (support roles).

### Structure
```
agents/<agent_name>/
â””â”€â”€ SKILL.md        â† Required: role + capabilities + governance
```

### SKILL.md Template
```yaml
---
name: my_agent
version: 1.0
tier: <1|2|3>
description: Role description
---

# My Agent

## Role
...

## Tier
...

## Capabilities
### function_name() â†’ type
...

## Activation
Triggered by: ...

## Dependencies
- skill_name

## Governance
...
```

### Registration
1. Add to `brain/memory/AGENTS.md` agent roster table
2. Add to `CLAUDE.md` agent roster table
3. Add to SKILL_REGISTRY.json with source="agent"

---

## ðŸ” Security Requirements

ALL additions must pass:
1. Security Agent scan (minimum score: 60)
2. Review of SKILL.md for dangerous patterns
3. No hardcoded tokens or paths
4. Declared license

---

## ðŸ“ Checklist Before Submitting

```
[ ] Security scan passed (score â‰¥ 60)
[ ] SKILL.md / manifest.json created
[ ] SKILL_REGISTRY.json updated
[ ] knowledge_index.md updated
[ ] AGENTS.md updated (for agents)
[ ] CLAUDE.md directory map updated (if new directory)
[ ] version.json updated
```

---

*"A well-documented addition is a gift to future agents."*

