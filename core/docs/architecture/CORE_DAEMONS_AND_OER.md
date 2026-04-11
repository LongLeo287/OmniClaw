# 🏛️ Core Daemons — OmniClaw Ecosystem Governance

> **Authority:** CEO (LongLeo) | **Version:** 5.0 | **Date:** 2026-04-11
> **Status:** ACTIVE — This document supersedes all previous ecosystem authority definitions.

[**Back to Docs**](../../../README.md)

This document defines the **8 Core Daemons** of OmniClaw OS and the **Zero-Trust Automated Pipeline** that governs how every Skill, Plugin, Agent, and Workflow enters the ecosystem.

---

## 1. The 8 Pillars of Governance (Master Hierarchy)

To prevent scope overreach and Zero-Trust violations, ecosystem authority is strictly distributed across 8 specialized Agents (Daemons) housed strictly within 3 distinct architectural departments (`system_daemons`, `system_health`, `system_security`):

| Node ID | Designation | General Role | Department |
| :--- | :--- | :--- | :--- |
| **`oma_architect`**| OmniClaw Map Architect | Infrastructure Config | `system_daemons` |
| **`oap_pipeline`** | Omnibus Assimilation | Pipeline Sorter | `system_daemons` |
| **`oer_registry`**| OmniClaw Ecosystem Registry | Registrar | `system_daemons` |
| **`oiw_intake`** | OmniClaw Intake Worker | Harvester | `system_daemons` |
| **`osf_warden`** | OmniClaw Sandbox Firewall | Border Firewall | `system_security` |
| **`ohd_healer`** | OmniClaw Health Daemon | System Doctor | `system_health` |
| **`oa_academy`** | OmniClaw Academy | Execution Auditor | `system_daemons` |
| **`obd_harbor`** | OmniClaw Bridge Daemon | Harbor Master / Port Firewall | `system_security` |

---

## 2. Authority Matrix (Who Does What)

| Function | OMA | OAP | OER | OIW | OSF | OHD | OA | OBD |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Map Node Paths & Identities | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Route Triage Matrix | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Update `REGISTRY.json` | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Git Clone / Harvest | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Quarantine Check (Border) | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
| Fix Files (Lint/Auto-Heal) | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
| Audit Logic & Recruit Agents | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Open Localhost Ports & Bridges | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |

> [!CAUTION]
> **Zero-Trust Compartmentalization**: All 8 Daemons are fully registered agent nodes with restricted skill boundaries. If any daemon attempts to execute a script outside its mandate, the Orchestrator will instantly terminate the instance.

---

## 3. OBD Harbor – The Strict Perimeter

As of Version 5.0, **OBD (OmniClaw Bridge Daemon)** is elevated to handle absolute networking and perimeter defense:
* **No Auto-Connections:** Third-party skills and web servers CANNOT bind to ports unmanaged by OBD.
* **127.0.0.1 Enforcement:** Opening `0.0.0.0` is strictly illegal unless explicit API Gateway authorization is granted. 
* **MCP Integration:** Claude/Cursor MCP modules running natively via `stdio` are tracked directly inside the OBD Dashboard to ensure full visibility of AI-managed bypasses.

For exact bridge protocol documentation, refer to `ecosystem/bridges/README.md`.

---

## 4. The Autonomous OAP Hierarchy

```mermaid
graph TD
    classDef sys fill:#1e1e2f,stroke:#4a4a6a,stroke-width:2px,color:#fff;
    classDef hlth fill:#1a2e26,stroke:#34a853,stroke-width:2px,color:#fff;
    classDef sec fill:#2b1919,stroke:#ea4335,stroke-width:2px,color:#fff;
    
    subgraph system_security[🏢 system_security / Boundary Defense]
        OSF["🛡️ OSF Firewall (osf_warden)"]:::sec
        OBD["🌉 OBD Harbor (obd_harbor)"]:::sec
    end
    
    subgraph system_health[🏥 system_health / Clinical Operations]
        OHD["⚕️ OHD Healer (ohd_healer)"]:::hlth
    end

    subgraph system_daemons[⚙️ system_daemons / Core Infrastructure]
        OMA["🗺️ OMA Architect (oma_architect)"]:::sys
        OAP["🔀 OAP Pipeline (oap_pipeline)"]:::sys
        OA["👑 OA Academy (oa_academy)"]:::sys
        OIW["📥 OIW Intake (oiw_intake)"]:::sys
        OER["📜 OER Registry (oer_registry)"]:::sys
    end

    OMA -->|"Maps & Routes"| OAP
    OAP -->|"Triage"| OIW
    OIW -->|"Pulls Code"| OSF
    OSF -->|"Quarantines"| OHD
    OHD -->|"Healed Files"| OER
    OER -->|"Stamps ID"| OA
    OBD -->|"Bridge APIs"| OSF
```

---

*Core Daemons v5.0 — OmniClaw Corp — 2026-04-11*
