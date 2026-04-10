---
id: memory_corp_agents
type: agent_roster
namespace: brain.memory.corp_memory.agents
owner: OSF_Daemon
status: standard_v5
description: "HR Roster and behavioral definitions for all OmniClaw specialized workers."
registered_by: OA_Auditor
---

# `corp_memory/agents` Identity (HR Roster)

> [!CAUTION]  
> **OSF DAEMON SECURITY WATERMARK**  
> Do not confuse this directory with `brain/agents/`. 
> - `brain/agents/`: Boot protocols for Top-Level AI (Claude, Antigravity).
> - `corp_memory/agents/`: Employee files for simulated workforce roles.

## 1. Directory Purpose
This directory acts as the Human Resources database. It stores exactly **83+ Persona Markdown Files** that define the behavior, prompt instructions, and limitations of every department worker (e.g. `scrum_master_agent`, `qa_testing_worker_1`). 

When the Orchestrator delegates a task, it loads the respective `.md` persona from here.

## 2. Topological Connectivity Graph

```mermaid
graph TD
    classDef roster fill:#8b4513,stroke:#333,stroke-width:2px,color:#fff;
    classDef index fill:#D2691E,stroke:#333,stroke-width:1px,color:#fff;

    R("brain/memory/corp_memory/agents/"):::roster
    I["brain/indices/FAST_AGENT_INDEX.json"]:::index
    O["core/ops/omniclaw_orchestrator.py"]

    R -->|Feeds Data| I
    I -.->|O(1) Search| O
    O -->|Loads Persona| R
```

## 3. Compliance Rules
- Every new worker MUST have their `<worker_name>.md` file placed here.
- Any change to files here requires re-running `rebuild_shards.py` to update the FAST_AGENT_INDEX.