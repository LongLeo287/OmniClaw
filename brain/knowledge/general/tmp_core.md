---
id: tmp-core
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-07T10:06:02.600597
---

﻿---
id: core-daemons-and-oer
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:44:27.660828
---

# ­ƒÅø´©Å OER & Core Daemons ÔÇö OmniClaw Ecosystem Governance

> **Authority:** CEO (LongLeo) | **Version:** 1.0 | **Date:** 2026-04-02
> **Status:** ACTIVE ÔÇö This document supersedes all previous ecosystem authority definitions.

**­ƒç╗­ƒç│ Bß║ún Tiß║┐ng Viß╗çt** | [**Back to Docs**](../README.md)

This document defines the **4 Core Daemons** of OmniClaw OS and the **5-Gate Automated Pipeline** that governs how every Skill, Plugin, Agent, and Workflow enters the ecosystem.

---

## Why This Exists

Before OER was established, ecosystem authority was fragmented:

| Problem | Entity | Issue |
|---|---|---|
| OIW harvested data but also registered new Agents | OIW | **Scope overreach** |
| Dept 14 held the Registry but had no formal identity | Dept 14 | **Invisible in Prompt context** |
| OA judged architecture but OEA (proposed, then dropped) also judged | OEA | **Redundant authority** |
| Orchestrator/CTO wrote files directly into `ecosystem/` | C-Suite | **Zero-Trust violation** |

**Solution:** Establish **OER (OmniClaw Ecosystem Registry)** as Core Daemon #4, formally distributing all responsibilities across 4 specialized daemons with zero overlap.

---

## The 4 Core Daemons

| Daemon | Full Name | Operated By | Primary Role |
|---|---|---|---|
| **OIW** | OmniClaw Intake Workflow | Dept 20 (`intake-chief-agent`) | Harvester ÔÇö pulls & dries external data |
| **OHD** | OmniClaw Health Daemon | Dept 19 (`health-chief-agent`) | Doctor ÔÇö sanitizes & maintains system health |
| **OA** | OmniClaw Academy | OA Faculty + Dept 9/12 | Judge ÔÇö enforces 8 Pillars, audits compliance |
| **OER** | OmniClaw Ecosystem Registry | Dept 14 (`registry-manager-agent`) | Registrar ÔÇö sole authority over ecosystem intake |

---

## Authority Matrix (Who Does What)

| Function | OIW | OHD | OA | OER |
|---|---|---|---|---|
| Harvest Repo, Gitingest | Ô£à | ÔØî | ÔØî | ÔØî |
| Place Repo in Quarantine | Ô£à | ÔØî | ÔØî | ÔØî |
| **Register new Agent/Dept** | ÔØî | ÔØî | ÔØî | Ô£à |
| Scan for Virus/IOC Supply Chain | ÔØî | Ô£à | ÔØî | ÔØî |
| Clean npm cache, `__pycache__` | ÔØî | Ô£à | ÔØî | ÔØî |
| Periodic health reporting | ÔØî | Ô£à | ÔØî | ÔØî |
| Judge architecture violations | ÔØî | ÔØî | Ô£à | ÔØî |
| Audit Ecosystem plugins | ÔØî | ÔØî | Ô£à | ÔØî |
| **Write to `ecosystem/`** | ÔØî | ÔØî | ÔØî | Ô£à |
| **Update `SKILL_REGISTRY.json`** | ÔØî | ÔØî | ÔØî | Ô£à |
| **Issue IDs for Tools/Plugins** | ÔØî | ÔØî | ÔØî | Ô£à |
| **Free-Pass into `brain/knowledge`** | ÔØî | ÔØî | ÔØî | Ô£à |
| Write OA laws, 8 Pillars | ÔØî | ÔØî | Ô£à | ÔØî |

> [!IMPORTANT]
> **Core change:** OIW loses all registration rights. All registration authority (Agent, Dept, Skill, Plugin, Workflow) transfers to OER. No other entity may write to `ecosystem/` or modify `SKILL_REGISTRY.json`.

---

## 5-Gate Automated Pipeline

```
   ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
   Ôöé                    OMNICLAW ECOSYSTEM INGEST PIPELINE                   Ôöé
   ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ

[TRIGGER]
CEO / Orchestrator / Dept Lead requests:
  "Need a new Skill / Plugin / Agent"
         Ôöé
         Ôû╝
  ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
  Ôöé GATE 0      Ôöé  Check: Already in SKILL_REGISTRY.json?
  Ôöé OER Check   Ôöé  ÔåÆ Yes: Reject, return existing ID
  ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ  ÔåÆ No: Continue
         Ôöé
         Ôû╝
  ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
  Ôöé PHASE 1     Ôöé  OIW (Dept 20) pulls source code
  Ôöé HARVEST     Ôöé  gitingest ÔåÆ compress to .md / .txt
  Ôöé             Ôöé  Deposit to: storage/vault/quarantine/
  ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
         Ôöé
         Ôû╝
  ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
  Ôöé PHASE 2     Ôöé  OHD (Dept 19) runs supply_chain_scan.ps1
  Ôöé SANITIZE    Ôöé  Checks IOC, virus, .map leak, C2 connection
  Ôöé             Ôöé  ÔåÆ FAIL: Send verdict to OA, add to BLACKLIST
  ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ  ÔåÆ PASS: Stamp "OHD_CLEAN" + timestamp
         Ôöé
         Ôû╝
  ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
  Ôöé PHASE 3     Ôöé  OA (Academy) reviews 8 Pillars
  Ôöé AUDIT       Ôöé  Dept 9 (Strix): Security score >= 70
  Ôöé             Ôöé  Dept 12 (Legal): License check
  Ôöé             Ôöé  ÔåÆ FAIL: Block + OA Faculty Report
  ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ  ÔåÆ PASS: Stamp "OA_APPROVED" + score
         Ôöé
         Ôû╝
  ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
  Ôöé PHASE 4     Ôöé  Dept 1 (Engineering): Build & Integration test
  Ôöé FORGE       Ôöé  Write SKILL.md to schema standard
  Ôöé             Ôöé  Write basic unit tests
  ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ  ÔåÆ FAIL: Return to Dept 1 to fix
         Ôöé
         Ôû╝
  ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
  Ôöé PHASE 5     Ôöé  OER (Dept 14 - registry-manager-agent) accepts
  Ôöé REGISTER    Ôöé  Issues unique ID (SKILL-xxxx / PLG-xxxx / AGT-xxxx)
  Ôöé             Ôöé  Writes to SKILL_REGISTRY.json
  Ôöé             Ôöé  Moves to ecosystem/ correct tier
  ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ  Reports back to Orchestrator/CEO: "REGISTERED"
         Ôöé
         Ôû╝
  ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
  Ôöé TELEMETRY   Ôöé  Receipt written to telemetry/qa_receipts/gate_oer/
  Ôöé LOG         Ôöé  + Update brain/knowledge/repos/ (if new repo)
  ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
```

---

## Departments Contributing to OER Pipeline

| Daemon / Dept | Contribution | Lead Agent |
|---|---|---|
| **OIW** | Supplies raw quarantined source material | `intake-chief-agent` (Dept 20) |
| **OHD** | Issues "Clean" certificate | `health-chief-agent` (Dept 19) |
| **OA** | Issues "Constitutional" approval stamp | `strix-agent` + `legal-agent` (Dept 9, 12) |
| **Dept 1** | Forges code into standard SKILL.md | `backend-architect-agent` |
| **Dept 13** | Proposes required new skills (R&D) | `rd-lead-agent` |
| **Dept 15** | Opens `brain/knowledge` when OER needs to read | `library-manager-agent` |
| **OER (Dept 14)** | **Final authority** ÔÇö issues ID, stores in ecosystem | `registry-manager-agent` |

---

## Related Files

| File | Purpose |
|---|---|

---

*OmniClaw Core Daemons & OER ÔÇö v1.0 ÔÇö 2026-04-02*
