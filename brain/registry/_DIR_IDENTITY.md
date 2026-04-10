---
id: brain_registry
type: core_system_prompt
namespace: brain.registry
owner: OSF_Daemon
status: standard_v5
description: "The brain/registry directory manages the core components of the OmniClaw v5.0 AI operating system, including skill sources, indexations, and routing configurations that ensure seamless integration and execution across all agents."
registered_by: OA_Auditor
tags: ["core", "orchestration", "AI OS", "skill management"]
---

# Registry Identity

The brain/registry directory manages the core components of the OmniClaw v5.0 AI operating system, including skill sources, indexations, and routing configurations that ensure seamless integration and execution across all agents.

## Topological View

```mermaid
graph TD
 Root("brain/registry")
 SKILL_REGISTRY(("SKILL_REGISTRY.json"))
 FAST_INDEX(("FAST_INDEX.json"))
 SYSTEM_INDEX(("SYSTEM_INDEX.yaml"))
 EXTERNAL_SKILL_SOURCES(("EXTERNAL_SKILL_SOURCES.yaml"))
 SKILL_ROUTER(("SKILL_ROUTER.yaml"))
 Root --> SKILL_REGISTRY
 Root --> FAST_INDEX
 Root --> SYSTEM_INDEX
 Root --> EXTERNAL_SKILL_SOURCES
 Root --> SKILL_ROUTER
```

---
*OmniClaw V5.0 | Forged by AI Architect | Evaluated dynamically*
