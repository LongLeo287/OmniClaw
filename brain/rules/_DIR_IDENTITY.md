---
id: rules
type: directory_identity
namespace: brain.rules
owner: OSF_Daemon
status: standard_v5
description: "The 'rules' directory within OmniClaw v5.0 houses the governance and security policies, as well as architectural guidelines for agents and systems interacting with the brain module."
registered_by: OMA_AI_FORGER
tags: ["governance", "security", "architecture"]
forged_at: 2026-04-10
---

# Rules Identity

The 'rules' directory within OmniClaw v5.0 houses the governance and security policies, as well as architectural guidelines for agents and systems interacting with the brain module.

---

## Topological View

```mermaid
graph TD
 Parent("brain") --> Node("rules")
 Node --> S1("agents")
 Node --> S2("architecture")
 Node --> S3("governance")
 Node --> S4("security")
 Node --> S5("sops")
```

---
*OmniClaw V5.0 | Forged by OMA AI Architect | brain.rules | 2026-04-10*
