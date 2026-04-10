---
id: brain_chromadb
type: vector_database
namespace: brain.chroma_db
owner: OSF_Daemon
status: standard_v5
description: "Persistent Vector Database (Chroma) for Long-Term Semantic Memory & MemPalace."
registered_by: OA_Auditor
---

# `brain/chroma_db` Identity (Vector Database)

> [!CAUTION]  
> **OSF DAEMON SECURITY WATERMARK**  
> This directory contains generated `chroma.sqlite3` and binary vector tensors.
> **STRICT GIT RULE:** Under NO CIRCUMSTANCES should `.sqlite3` or tensor UUID folders inside here be pushed to a Git Repository. Only this identity file is tracked.

## 1. Directory Purpose
Serves as the physical Long-Term Memory (LTM) persistent layer for the OmniClaw system. It powers the `MemPalace` core utility, actively indexing and retrieving conversational insights, rules, and ecosystem code via Deep Search (Layer 3).

## 2. Topological Connectivity Graph

```mermaid
graph TD
    classDef daemon fill:#6a0dad,stroke:#333,stroke-width:2px,color:#fff;
    classDef vault fill:#003366,stroke:#ccc,stroke-width:1px,color:#fff;
    classDef rdb fill:#B8860B,stroke:#333,stroke-width:1px,color:#fff;

    M[core/utils/mempalace]:::daemon
    V[brain/knowledge]:::vault
    Q[ecosystem/agents]:::vault

    DB[(brain/chroma_db <br> chroma.sqlite3)]:::rdb

    M -->|Extracts Tensors| V
    M -->|Extracts Tensors| Q
    M -->|Embeds & Persists| DB
    DB -.->|Deep Semantic Search| M
```

## 3. Compliance Rules
- Manual edits of binary items within this directory will corrupt the AI's semantic retrieval system.
- The `mempalace` MCP server dynamically writes and reads from this SQLite storage.
