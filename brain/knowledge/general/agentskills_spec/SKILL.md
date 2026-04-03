---
id: agentskills-spec
name: AgentSkills Specification
version: 1.0.0
tier: 1
status: active
author: OmniClaw Core Team
updated: 2026-04-02
description: Official Anthropic agentskills.io specification ingested into OmniClaw. Defines the standard interface, lifecycle, and metadata format for agent skills. Used by Skill Creator Ultra and all skill-aware agents.
department: registry_capability
category: specification
tags: [spec, agentskills, anthropic, standard, skill-lifecycle]
---

# AgentSkills Specification

**Repo:** `ecosystem/skills/agentskills-spec`
**Type:** Specification / reference document
**Source:** `https://github.com/agentskills/agentskills` (Anthropic)
**Delivered by:** `ingest-router-agent` (CIV-2026-03-17-001)
**Department:** Registry & Capability
**Tier:** 1 — foundational specification

## What it is

The authoritative **agentskills.io specification** from Anthropic, copied into OmniClaw brain. Defines:

- Standard skill YAML/Markdown metadata schema
- Skill lifecycle states: `draft → active → deprecated`
- Tool interface contracts for skill invocation
- Agent capability declaration format
- Tier classification system (1–5)

## Contents

| File | Purpose |
|------|---------|
| `CIV-DELIVERY.md` | Delivery receipt from ingest-router-agent |

## Usage by OmniClaw

All SKILL.md files in OmniClaw follow this spec:
```yaml
---
name: <skill name>
description: <1-line description>
department: <dept_id>
tier: 1-5
category: <category>
status: active|deprecated|draft
tags: [...]
---
```

## OmniClaw Integration
- **Owner:** `registry_capability` department
- **Read by:** Skill Creator Ultra, SKILL_REGISTRY.json builder, ClawTask Skills panel
- **Purpose:** Ensures all 44+ OmniClaw skills conform to the same schema
- **Used in:** `/api/omniclaw/skills` endpoint for validation
