---
id: brain_indices
type: systemic_database
owner: OSF_Daemon
status: standard_v5
---

# Brain Map Indices (Sharded Database)

> [!CAUTION]  
> **OSF DAEMON SECURITY WATERMARK**  
> This directory is dynamically managed by the Core Daemons. Manual editing of JSON files in this directory will trigger anti-tamper quarantines.

## 1. Overview & Competency
The `brain/indices` domain implements OmniClaw's V5.0 **Sharded Architecture**. Instead of loading a monolithic registry map into daemon memory, the registry is mathematically fractioned into specific topological categories. This provides O(1) instantaneous lookup capabilities for routing agents, validating skills, and discovering plugins without ram ballooning.

## 2. Topological Graph

```mermaid
graph TD
    classDef daemon fill:#6a0dad,stroke:#333,stroke-width:2px,color:#fff;
    classDef physical fill:#003366,stroke:#ccc,stroke-width:1px,color:#fff;
    classDef shard fill:#104E8B,stroke:#00f,stroke-width:1px,color:#fff;

    subgraph Core_Daemons
        OMA[OMA Indexer Engine]:::daemon
        OER[OER Registrar]:::daemon
    end

    subgraph V5_Physical_Assets
        ES[ecosystem/skills]:::physical
        EA[ecosystem/workforce]:::physical
        BK[brain/knowledge]:::physical
        EP[ecosystem/plugins]:::physical
    end

    subgraph Brain_Indices_Shards
        F_AG(FAST_AGENT_INDEX.json):::shard
        F_SK(FAST_SKILL_INDEX.json):::shard
        F_KN(FAST_KNOWLEDGE_INDEX.json):::shard
        F_PL(FAST_PLUGIN_INDEX.json):::shard
    end

    V5_Physical_Assets --> |"Reads & Verify"| OMA
    OMA --> |"Balkanizes & Dispatches"| Brain_Indices_Shards
    OER --> |"Incremental Appends"| Brain_Indices_Shards
```

## 3. Data Integrity Certifications
- **Ghost Entries**: 0% (Fully Purged & Synchronized with local disk).
- **Rogue Identifiers**: `.`, `unknown`, and unclassified entities strictly prohibited.
- **Encoding Status**: UTF-8 Strict Compliance (Mojibake eradicated).
