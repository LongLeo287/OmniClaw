---
id: unique_slug
type: directory_identity
namespace: brain.example.path
owner: OSF_Daemon
status: standard_v5
description: "The 'indices' directory contains essential files for managing various types of indices used in OmniClaw v5.0, including agent, knowledge, plugin, skill, and workflow indices."
registered_by: OMA_AI_FORGER
tags: ["indices", "OmniClaw_v5.0"]
---

# Indices Identity

The 'indices' directory contains essential files for managing various types of indices used in OmniClaw v5.0, including agent, knowledge, plugin, skill, and workflow indices.

## Topological View

```mermaid
graph TD
  Parent("brain") --> Node("indices")
  Node --> Sub1("FAST_AGENT_INDEX.json")
  Node --> Sub2("FAST_KNOWLEDGE_INDEX.json")
  Node --> Sub3("FAST_PLUGIN_INDEX.json")
  Node --> Sub4("FAST_SKILL_INDEX.json")
  Node --> Sub5("FAST_WORKFLOW_INDEX.json")
```

---
*OmniClaw V5.0 | Forged by AI Architect | Evaluated dynamically*
