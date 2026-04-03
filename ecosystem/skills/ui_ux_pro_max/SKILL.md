---
id: ui-ux-pro-max
name: UI-UX Pro Max
version: 1.0.0
tier: 2
status: active
author: OmniClaw Core Team
updated: 2026-04-02
description: Advanced UI/UX analysis and generation skills with data-driven patterns. Python scripts (core.py, search.py) for systematic UI pattern extraction, design system generation, and component search from curated data sources.
department: engineering, rd
category: design
tags: [ui, ux, design-system, pattern-extraction, python, data-driven]
---

# UI-UX Pro Max

**Repo:** `ecosystem/skills/ui-ux-pro-max`
**Type:** Python skill scripts + data
**Department:** Engineering / R&D
**Tier:** 2 — runnable scripts

## What it does

Advanced UI/UX toolkit with Python-powered analysis:

### Scripts

#### `scripts/core.py`
Core UI pattern engine:
- Extract design patterns from reference UIs
- Generate component specifications from descriptions
- Produce Tailwind/CSS class recommendations
- Output structured design tokens

#### `scripts/search.py`
UI/UX pattern search engine:
- Search curated `data/` directory for UI patterns
- Similarity matching for design requests
- Returns top-N matching component patterns

### Data (`data/`)
Curated UI/UX pattern library and reference data used by the scripts.

## Usage

```bash
# Search for UI pattern
python ecosystem/skills/ui-ux-pro-max/scripts/search.py "navigation sidebar with icons"

# Generate component spec
python ecosystem/skills/ui-ux-pro-max/scripts/core.py generate "glassmorphism card"

# Extract patterns from URL
python ecosystem/skills/ui-ux-pro-max/scripts/core.py extract "https://example.com"
```

## OmniClaw Integration
- **Used by:** Frontend agent, Engineering agent for UI generation
- **ClawTask:** Terminal panel → run scripts via `/api/tool-run`
- **Output:** Component specs fed to `ui/dashboard/`, `ui/viewer/`
- **Pairs with:** `plugins/lenis` (animations), `ecosystem/skills/domains/frontend/`

## Agent Invocation
```json
{
  "cmd": "python ecosystem/skills/ui-ux-pro-max/scripts/search.py",
  "args": ["glassmorphism dashboard card"],
  "cwd": "$OMNICLAW_ROOT"
}
```
