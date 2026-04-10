---
id: registry_domain
name: Registry Core
path: brain/registry
type: directory_identity
registered_daemons: [OER, OMA]
---

# ==========================================
# OmniClaw V5.0 | Protected by OSF Daemon
# ==========================================

# 🗃️ The Registry Core (OER & OMA Domain)

> [!CAUTION]
> This directory is the **Authoritative Fast Index** of the OmniClaw System. It is strictly maintained by the **OER (Entity Registrar)** and **OMA (System Architect)** Daemons.
> - **Execution Agents:** DO NOT attempt to write or modify JSON/YAML files in this directory. 
> - If an Agent wants to register a new skill or dataset, it MUST submit a formal request to the `OAP Pipeline`. Only OER has the authority to append to `SKILL_REGISTRY.json` or `FAST_INDEX.json`.

## 🗺️ Registry Topology (V5.0)
The absolute routing hierarchy executed by the core daemons.

```mermaid
graph TD
    classDef daemon fill:#e91e63,stroke:#fff,stroke-width:2px,color:#fff
    classDef index fill:#2196f3,stroke:#fff,stroke-width:2px,color:#fff
    classDef agent fill:#ff9800,stroke:#fff,stroke-width:2px,color:#fff

    subgraph "brain/registry/"
        FAST[FAST_INDEX.json]:::index
        SYS[SYSTEM_INDEX.yaml]:::index
        SKILL[SKILL_REGISTRY.json]:::index
        EXT[EXTERNAL_SKILL_SOURCES.yaml]:::index
        ROUTER[SKILL_ROUTER.yaml]:::index
    end

    OMA(OMA System Architect):::daemon
    OER(OER Entity Registrar):::daemon
    OAP(OAP Pipeline):::daemon
    
    AGENTS(Execution Agents):::agent

    %% OMA Architect controls structural indexes
    OMA -->|Compiles Map| FAST
    OMA -->|Indexes Content| SYS

    %% OER Registrar controls skills
    OER -->|Validates Tools| SKILL
    OER -->|Fetches Repos| EXT

    %% OAP controls Agents
    OAP -->|Directs logic| ROUTER

    %% Execution Agents reading the indexes
    AGENTS -.->|Read Only| FAST
    AGENTS -.->|Read Only| SKILL
    
    %% Instruction Flow
    ROUTER -.->|Forces task| AGENTS
    
    %% Strict protection
    OSF(OSF Warden):::daemon -->|Protects All Indexes| FAST
```

## Core Mechanisms
- **FAST INDEX:** The hyper-optimized map utilized by OMA to route systemic signals.
- **SKILL REGISTRY:** The exhaustive record of all approved scripts, tools, and actions permitted to run.
- **NO HUMAN LOGS:** This directory is not a log-dump. System transaction logs are strictly banished.
