---
id: memory_core_domain
type: directory_identity
namespace: brain.memory.core
owner: OBD_Daemon
status: standard_v5
description: "High-speed volatile datastore for Orchestrator Telemetry and HUD Dashboard integration."
registered_by: OA_Auditor
---

# `brain/memory/core` / [OBD_Telemetry_Vault]

> **[CLASSIFIED] █ █ █ █ █ █ █ █ █ █**
> **WATERMARK:** `// OMNICLAW_OS_V5.0 // CORE_TELEMETRY // OBD_BRIDGE //`
> **ACCESS LEVEL:** TIER-2 (DAEMONS ONLY)

This partition acts as the **Headless System A/B Bridge**. It holds rapidly changing JSON data stores (such as `STATUS.json`) written by the Orchestrator and retrieved exclusively via the `OBD_Daemon` (Bridge Protocol) for external UI consumption.

## 📡 Telemetry Topology (V5.0)

```mermaid
graph LR
    classDef daemon fill:#1E293B,stroke:#F59E0B,stroke-width:2px,color:#fff;
    classDef ltm fill:#0F172A,stroke:#6366F1,stroke-width:2px,color:#fff;
    classDef api fill:#064E3B,stroke:#10B981,stroke-width:2px,color:#fff;
    classDef ext fill:#8B5CF6,stroke:#4C1D95,stroke-width:2px,color:#fff;

    subgraph INTRANET [Local Backend]
        ORCH("omniclaw_orchestrator.py<br/>[Data Writer]"):::daemon
        START("omniclaw_startup.py<br/>[Data Writer]"):::daemon
        
        subgraph MEMORY_CORE [brain/memory/core]
            STAT[("STATUS.json<br/>Headless API Payload")]:::ltm
        end

        OBD("OBD_Daemon<br/>[Bridge Protocol]"):::daemon
        PORT(("Port 7474<br/>clawtask_api")):::api
        TEL(("Telegram Bot<br/>Dispatcher")):::api
    end

    subgraph EXTRANET [Client Tier]
        UI(["OmniClaw UI<br/>React/Tailwind"]):::ext
        REM(["OmniClaw Remote<br/>Mobile/Web"]):::ext
        CEO(["CEO / Admin"]):::ext
    end

    START -->|Inject Boot Status| STAT
    ORCH -->|Inject Cycle Digest| STAT
    
    STAT -.->|Read| OBD
    OBD -->|Serve Endpoint| PORT
    OBD -->|Push Digest| TEL
    
    PORT <==>|HTTP GET /status| UI
    PORT <==>|HTTP GET /status| REM
    TEL ===>|Push Notifications| CEO
```

## Declarations
- **Strictly No Logic**: This directory MUST NOT contain `.py`, `.js`, or executable files.
- **V5 Constraint**: JSON keys must reflect physical paths (e.g., `"vault"` instead of legacy `"kho"`).
