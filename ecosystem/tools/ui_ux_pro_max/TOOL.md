---
id: ui_ux_pro_max
name: UI/UX Pro Max Toolkit
status: active
integration_type: python_script
accessible_by:
  - Orchestrator
  - Frontend Agents
tags: [ui, ux, design-system, pattern-extraction, python, data-driven]
---

# UI/UX Pro Max Pattern Engine

## Overview
Advanced UI/UX tool native python engine. Contains offline logic scripts for systematic UI pattern extraction, design system generation, and component search.

## Instructions
Execute via terminal mapping:
```bash
# Search for UI pattern
python $OMNICLAW_ROOT/ecosystem/tools/ui_ux_pro_max/scripts/search.py "navigation sidebar with icons"

# Generate component spec
python $OMNICLAW_ROOT/ecosystem/tools/ui_ux_pro_max/scripts/core.py generate "glassmorphism card"

# Extract patterns from URL
python $OMNICLAW_ROOT/ecosystem/tools/ui_ux_pro_max/scripts/core.py extract "https://example.com"
```
