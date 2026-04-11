# 🗺️ Regional Map: brain/knowledge

This graph demonstrates the internal topological structure of the curated Knowledge Library and its strict one-way extraction relationship with the massive, untracked `vault/knowledge/`.

```mermaid
graph TD
    %% Isolation Firewall
    subgraph Cold Storage [Untracked Vault]
      V1("vault/knowledge/global_codebases/")
      V2("vault/knowledge/archived_fetches/")
    end

    %% Intake & Refinement
    subgraph OmniClaw Daemons
      C1((Cognitive Reflector))
      C2((Knowledge Intake))
    end

    %% Curated Namespace
    subgraph Brain Knowledge [brain/knowledge/ (Tracked & Curated)]
      Node("knowledge/")
      
      subgraph Core Architecture
        S1("agent_architecture/")
        S4("architecture/")
        M1("ai_os_system_map.md")
        M2("capability_map.md")
      end

      subgraph Domains
        S2("ai_ml/")
        S11("cybersecurity/")
        S25("devops/")
        S36("system_health/")
      end

      subgraph Operational Pointers
        R1("retrieval_protocol.md")
        L1("LIBRARY_GRAPH.json")
        O1("OS_CODE_RULES.md")
      end

      Node --> Core Architecture
      Node --> Domains
      Node --> Operational Pointers
    end

    %% Extraction Flow
    Cold Storage -->|Raw Data| OmniClaw Daemons
    OmniClaw Daemons -->|Distils & Refines| Brain Knowledge

    style Cold Storage fill:#ffebee,stroke:#c62828,stroke-width:2px,stroke-dasharray: 5 5
    style Brain Knowledge fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style OmniClaw Daemons fill:#fff3e0,stroke:#e65100
```

---
*OmniClaw V5.0 Blueprint | Forged by Antigravity OS Architect | brain.knowledge | 2026-04-11*
