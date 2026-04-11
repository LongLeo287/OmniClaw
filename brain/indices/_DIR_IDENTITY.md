---
id: brain_indices
type: directory_identity
namespace: brain.indices
owner: OSF_Daemon
status: standard_v5
description: "High-Speed Cache Layer containing deterministic FAST JSON indices generated exclusively from OmniClaw V5.0 physical namespaces."
registered_by: OMA_AI_FORGER
tags: ["indices", "cache", "deterministic-routing", "OmniClaw-V5"]
forged_at: 2026-04-11
---

# Indices Identity ⚡

This directory is the **High-Speed Cache Layer** of the OmniClaw OS. It contains serialized JSON index tables built by parsing physical namespaces rather than metadata. It completely strips out `fake signals` and `shared-context` noise from earlier legacy system versions.

## 📍 Core Declarations:
*   **AGENT:** Strictly maps exactly 30 true agents (28 Departments + 2 Daemons).
*   **SKILL:** Maps operational payload scripts across `ecosystem/skills/`.
*   **KNOWLEDGE:** Maps heavily isolated datasets inside `vault/knowledge/`.
*   **WORKFLOW/PLUGIN/DOCUMENT:** Maps corresponding namespaces deterministically.

---

## 🗺️ Topological View

```mermaid
graph TD
  Brain("brain/") --> Indices("indices/")
  Indices --> FA["FAST_AGENT_INDEX.json"]
  Indices --> FS["FAST_SKILL_INDEX.json"]
  Indices --> FK["FAST_KNOWLEDGE_INDEX.json"]
  Indices --> FW["FAST_WORKFLOW_INDEX.json"]
  Indices --> FP["FAST_PLUGIN_INDEX.json"]
  Indices --> FD["FAST_DOCUMENT_INDEX.json"]
```

---
*OmniClaw V5.0 Blueprint | Forged by Antigravity OS Architect | brain.indices | 2026-04-11*
