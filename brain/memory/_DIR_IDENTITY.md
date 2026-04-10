---
id: brain_memory_core
type: active_memory_state
namespace: brain.memory
owner: OSF_Daemon
status: standard_v5
description: "Live State, Short-Term Memory, and Blackboard coordination for OmniClaw."
registered_by: OA_Auditor
---

# `brain/memory` Identity (Active Memory State)

> [!CAUTION]  
> **OSF DAEMON SECURITY WATERMARK**  
> This directory contains live operational data, including the global Blackboard, system status, and agent task queues. 

## 1. Directory Purpose
Serves as the volatile and semi-persistent Short-Term Memory (STM) core of the OmniClaw system. All agents read, write, and synchronize their current work cycles against the states stored here.

## 2. Structural Topology

```mermaid
graph TD
    classDef memory fill:#2b5e2b,stroke:#333,stroke-width:2px,color:#fff;
    classDef queue fill:#8b4513,stroke:#333,stroke-width:1px,color:#fff;
    classDef root fill:#003366,stroke:#ccc,stroke-width:1px,color:#fff;

    M(brain/memory):::root

    BB[blackboard.json <br> Global State]:::memory
    RM[roadmap.md <br> Milestones]:::memory
    C_MEM(corp_memory/ <br> Org Archives):::queue
    A_MEM(agents/ <br> Task Queues):::queue
    SYS(core/ <br> STATUS.json):::queue

    M --> BB
    M --> RM
    M --> C_MEM
    M --> A_MEM
    M --> SYS
```

## 3. Compliance Rules
- This zone is highly dynamic. Data here changes frequently and is read continuously by AI boot protocols (e.g. `gemini.md`, `claude.md`).
- Legacy metadata identifying this folder as "Empty Shell (v2.1)" is permanently purged.
