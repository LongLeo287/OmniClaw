# MEMORY_SPEC.md — OmniClaw Unified Memory Architecture

# Version: 5.0 | Updated: 2026-04-10
# Authority: Tier 4 (Data & Memory)

## 🧠 Long-Term Episodic Engine (System B - V5.0)

OmniClaw currently utilizes the **Unified Memory Framework V5.0**:
- **Short-term Memory (System A)**: `brain/memory/` designated for ultra-fast, real-time IO (`blackboard.json`).
- **Long-term Memory (System B)**: `brain/memory/corp_memory/` designated for permanent, narrative, and log-based storage in Markdown format for RAG ingestion and Orchestrator Automated Workflows.

This specification outlines the operational rules for **Long-term Memory (System B)** based on the 8-Daemon Architecture modernization.

```mermaid
graph TD
    classDef sys fill:#1E293B,stroke:#3B82F6,stroke-width:2px,color:#fff;
    classDef inbox fill:#8B5CF6,stroke:#3B82F6,stroke-width:2px,color:#fff;
    classDef gap fill:#EF4444,stroke:#DC2626,stroke-width:2px,color:#fff;
    classDef orch fill:#10B981,stroke:#047857,stroke-width:3px,color:#fff;
    classDef global fill:#F59E0B,stroke:#B45309,stroke-width:2px,color:#fff;

    O[OmniClaw Orchestrator]:::orch
    
    subgraph SYSTEM_B[Long-Term Corp Memory]
        D(departments/):::sys
        A(agents/):::sys
        B(brainstorms/):::sys
        
        G(global/):::global
        P(patterns/):::global
        
        GA(gaps/):::gap
        PR(proposals/):::inbox
    end

    A -->|Agent History| O
    D -->|Department Patterns| O
    
    O -.->|Task Dispatch| G
    G -->|Overriding CEO Ledger| O
    O -.->|Task Dispatch| P
    P -->|Heuristics Patch Overlay| O
    
    GA -->|Gap Ingestion| O
    PR -->|Proposal Ingestion| O
```

### 1. The Autonomous Tiers
| Directory | Owner | Workflow Hook |
| --------- | ----- | ------------- |
| `global/` | CEO | Unconditional Supreme Context (Top-down) |
| `patterns/` | Agents | Dynamic Adaptive Overlays (System-wide heuristics patch) |
| `gaps/` | Agents | Orchestrator self-healing ingestion (Promotes `Refactoring` tasks) |
| `proposals/` | CEO | Orchestrator inbox ingestion (Promotes `Setup` tasks upon `[x] APPROVE`) |

### 2. The Organizational Tiers
| Directory | Owner | Purpose |
| --------- | ----- | ------- |
| `departments/` | Dept Heads | High-level 30-day institutional memory. Aggregates overarching rules mapping to entire teams. |
| `agents/` | Native Agents | Granular task history. 7-day auto-purged individual alignment files. |
| `brainstorms/` | Cross-Functional | Volatile idea dumping grounds. |

---
