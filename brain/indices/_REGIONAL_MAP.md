# 🗺️ Regional Map: brain/indices

The `brain/indices/` folder serves as the central circulatory system for memory retrieval. Daemons read these artifacts to jump instantly to resources anywhere in the repository.

## 🔗 Determistic Mapping Flow

This map visualizes how the V5 index builder scripts sweep physical namespaces to compile these 6 core registry files.

```mermaid
graph LR
    %% Ecosystem Sources
    subgraph Ecosystem ["Ecosystem Sources (Real Signals)"]
        Dept("ecosystem/workforce/departments")
        Skills("ecosystem/skills")
        Workflows("ecosystem/workflows")
        Plugins("ecosystem/plugins")
    end

    %% Vault Sources
    subgraph Vault ["Vault / Documents"]
        Know("vault/knowledge")
        Docs("core/docs")
    end

    %% Builder Script
    Builder[["core/ops/scripts/build_v5_indices.py"]]
    
    %% Target Indices
    subgraph Indices ["brain/indices/"]
        FA[FAST_AGENT_INDEX]
        FS[FAST_SKILL_INDEX]
        FW[FAST_WORKFLOW_INDEX]
        FP[FAST_PLUGIN_INDEX]
        FK[FAST_KNOWLEDGE_INDEX]
        FD[FAST_DOCUMENT_INDEX]
    end

    %% Edges
    Dept -->|crawls| Builder
    Skills -->|crawls| Builder
    Workflows -->|crawls| Builder
    Plugins -->|crawls| Builder
    Know -->|crawls| Builder
    Docs -->|crawls| Builder

    Builder -->|generates| FA
    Builder -->|generates| FS
    Builder -->|generates| FW
    Builder -->|generates| FP
    Builder -->|generates| FK
    Builder -->|generates| FD

    style Builder fill:#bf360c,color:#fff,stroke:#ff5722
    style Indices fill:#004d40,color:#fff,stroke:#00bfa5
```

---
*OmniClaw V5.0 Blueprint | Forged by Antigravity OS Architect | brain.indices | 2026-04-11*
