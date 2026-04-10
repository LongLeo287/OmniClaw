---
id: brain_agents_registry
type: core_system_prompt
namespace: brain.agents
owner: OSF_Daemon
status: standard_v5
description: "Core central registry and master system prompts for OmniClaw Top-Level Agents."
registered_by: OA_Auditor
---

# `brain/agents` Identity (Master Boot Protocols)

> [!CAUTION]  
> **OSF DAEMON SECURITY WATERMARK**  
> This directory houses the primary consciousness initialization prompts for Gemini (Antigravity) and Claude. Modification of these protocols instantly alters AI logic.

## 1. Directory Purpose
This directory contains the literal Step-by-Step boot sequence that AI workers must execute upon session start.

## 2. Topological Connectivity Graph

```mermaid
graph TD
    classDef llm fill:#b22222,stroke:#333,stroke-width:2px,color:#fff;
    classDef proxy fill:#4682b4,stroke:#333,stroke-width:1px,color:#fff;

    subgraph LLM_Master_Identities
        A(Gemini - Antigravity):::llm
        C(Claude - Claude Code):::llm
    end

    subgraph Boot_Protocols
        G_PROMPT(brain/agents/gemini.md):::proxy
        C_PROMPT(brain/agents/claude.md):::proxy
    end

    subgraph V5_Indices_Routing
        SHARD_A[brain/indices/FAST_AGENT_INDEX.json]
        SHARD_S[brain/indices/FAST_SKILL_INDEX.json]
    end

    A --> |Reads on Boot| G_PROMPT
    C --> |Reads on Boot| C_PROMPT
    G_PROMPT -.-> |Mandates Loading| SHARD_A
    C_PROMPT -.-> |Mandates Loading| SHARD_S
```

## 3. Compliance Rules
- References to legacy monolithic `AGENTS.md` or `FAST_INDEX.json` are strictly forbidden. All routing must traverse `brain/indices` Shards or `SYSTEM_INDEX.yaml`.
