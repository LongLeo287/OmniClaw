# 🏛️ OER & Core Daemons — OmniClaw Ecosystem Governance

> **Authority:** CEO (LongLeo) | **Version:** 2.2 | **Date:** 2026-04-05
> **Status:** ACTIVE — This document supersedes all previous ecosystem authority definitions.

[**🇻🇳 Bản Tiếng Việt**](CORE_DAEMONS_AND_OER-vn.md) | [**Back to Docs**](../README.md)

This document defines the **6 Core Daemons** of OmniClaw OS and the **5-Gate Automated Pipeline** that governs how every Skill, Plugin, Agent, and Workflow enters the ecosystem.

---

## 1. The 6 Core Daemons

To prevent scope overreach and Zero-Trust violations, ecosystem authority is strictly distributed across 6 specialized daemons with absolute zero overlap:

| Daemon | Full Name | General Role | Primary Duty |
|---|---|---|---|
| **OIW** | OmniClaw Intake Worker | Harvester | Pulls raw external Code/Data and deposits it blindly into quarantine. |
| **OSF** | OmniClaw Sandbox Firewall | Border Firewall | Guards the gates. Uses analytical threat-skills (some provided by OHD) to inspect incoming payloads before they penetrate the internal system. |
| **OHD** | OmniClaw Health Daemon | System Doctor | Internal physician. Sanitizes logs, performs deep supply-chain virus scans, clears caches, and develops health-skills shared with OSF. |
| **OA** | OmniClaw Academy | Parliament / Research Lab | The Supreme Auditor and Judge. Analyzes CIV Repos, enforces the 8 Pillars of Security & Licensing. When a repo is approved, OA initiates the profiling process to forge new Agents and Skills. |
| **Dept 1** | Backend Architect Agent | Engineer | Not a daemon, but tightly coupled. Triggered by OA to actually write the code, `SKILL.md` profiles, and unit tests for the approved assets. |
| **OER** | OmniClaw Ecosystem Registry | Warehouse Manager (Registrar) | The sole entity authorized to issue IDs (SKILL-xxxx, PLG-xxxx), assign directories, and update `SKILL_REGISTRY.json`. |
| **OMA** | Omni Management Architect | Infrastructure Manager | Manages structural file layouts, dynamically links ingested knowledge `distilled_core` nodes to the massive `LIBRARY_GRAPH.json`, and drives the robotic garbage collection process. |

---

## 2. Authority Matrix (Who Does What)

| Function | OIW | OSF | OHD | OA | OER | OMA |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Git Clone / Harvest | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Quarantine Check / Block | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Deep Internal Clean / IOC Scan | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
| Audit 8 Pillars (Parliament) | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
| Write Agent/Skill Logic (Dept 1) | ❌ | ❌ | ❌ | ⚒️ | ❌ | ❌ |
| Update `SKILL_REGISTRY.json` | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Map to `LIBRARY_GRAPH.json` | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Issue Asset IDs (SKILL-xxxx) | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Manage File Infrastructure | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |

> [!IMPORTANT]
> **Strict Compartmentalization**: OIW strips inputs. OA actively researches and audits. OER registers. OMA links infrastructure. If any daemon steps outside this matrix, the ecosystem halts.

---

## 3. The 5-Gate Automated Pipeline

```
   ┌─────────────────────────────────────────────────────────────────┐
   │                    OMNICLAW ECOSYSTEM 5-GATE PIPELINE           │
   └─────────────────────────────────────────────────────────────────┘

 [GATE 0: OER Duplicate Check]  -----> REJECT if exists
        |
 [PHASE 1: OIW — HARVEST]
   - Clone repo to vault/quarantine/
        |
 [PHASE 2: OSF & OHD — BORDER SANITIZE]
   - OSF Firewall blocks obvious outer threats.
   - OHD Doctor runs deep supply_chain_scan and cache clearing.
        |        \___FAIL__> OHD destroys payload.
 [PHASE 3: OA — RESEARCH & AUDIT]
   - OmniClaw Academy (Dept 9, Dept 12) reviews Repo structure.
   - Enforces 8 Pillars. Scores security and logic.
        |        \___FAIL__> OA Faculty Report + Block
 [PHASE 4: Dept 1 (Engineering) — FORGE CAPABILITIES]
   - Instructed by OA, the engineering tool array:
   - Writes `SKILL.md` capability profiles.
   - Defines new Agents, Departments, and MCPs.
        |
 [PHASE 5: OER — REGISTRAR & WAREHOUSE INTAKE]
     (Also OMA Infrastructure Linking)
   - OER issues unique IDs.
   - OER writes to `SKILL_REGISTRY.json`.
   - OER moves assets into appropriate ecosystem/ directories.
   - OMA updates LIBRARY_GRAPH.json and purges the volatile tmp dirs.
```

---

*OER & Core Daemons v2.2 — OmniClaw Corp — 2026-04*
