---
id: core-daemons-and-oer
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:44:27.660828
---

# 🏛️ OER & Core Daemons — OmniClaw Ecosystem Governance

> **Authority:** CEO (LongLeo) | **Version:** 1.0 | **Date:** 2026-04-02
> **Status:** ACTIVE — This document supersedes all previous ecosystem authority definitions.

[**🇻🇳 Bản Tiếng Việt**](CORE_DAEMONS_AND_OER-vn.md) | [**Back to Docs**](../README.md)

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
| **OIW** | OmniClaw Intake Workflow | Dept 20 (`intake-chief-agent`) | Harvester — pulls & dries external data |
| **OHD** | OmniClaw Health Daemon | Dept 19 (`health-chief-agent`) | Doctor — sanitizes & maintains system health |
| **OA** | OmniClaw Academy | OA Faculty + Dept 9/12 | Judge — enforces 8 Pillars, audits compliance |
| **OER** | OmniClaw Ecosystem Registry | Dept 14 (`registry-manager-agent`) | Registrar — sole authority over ecosystem intake |

---

## Authority Matrix (Who Does What)

| Function | OIW | OHD | OA | OER |
|---|---|---|---|---|
| Harvest Repo, Gitingest | ✅ | ❌ | ❌ | ❌ |
| Place Repo in Quarantine | ✅ | ❌ | ❌ | ❌ |
| **Register new Agent/Dept** | ❌ | ❌ | ❌ | ✅ |
| Scan for Virus/IOC Supply Chain | ❌ | ✅ | ❌ | ❌ |
| Clean npm cache, `__pycache__` | ❌ | ✅ | ❌ | ❌ |
| Periodic health reporting | ❌ | ✅ | ❌ | ❌ |
| Judge architecture violations | ❌ | ❌ | ✅ | ❌ |
| Audit Ecosystem plugins | ❌ | ❌ | ✅ | ❌ |
| **Write to `ecosystem/`** | ❌ | ❌ | ❌ | ✅ |
| **Update `SKILL_REGISTRY.json`** | ❌ | ❌ | ❌ | ✅ |
| **Issue IDs for Tools/Plugins** | ❌ | ❌ | ❌ | ✅ |
| **Free-Pass into `brain/knowledge`** | ❌ | ❌ | ❌ | ✅ |
| Write OA laws, 8 Pillars | ❌ | ❌ | ✅ | ❌ |

> [!IMPORTANT]
> **Core change:** OIW loses all registration rights. All registration authority (Agent, Dept, Skill, Plugin, Workflow) transfers to OER. No other entity may write to `ecosystem/` or modify `SKILL_REGISTRY.json`.

---

## 5-Gate Automated Pipeline

```
   ┌─────────────────────────────────────────────────────────────────────────┐
   │                    OMNICLAW ECOSYSTEM INGEST PIPELINE                   │
   └─────────────────────────────────────────────────────────────────────────┘

[TRIGGER]
CEO / Orchestrator / Dept Lead requests:
  "Need a new Skill / Plugin / Agent"
         │
         ▼
  ┌─────────────┐
  │ GATE 0      │  Check: Already in SKILL_REGISTRY.json?
  │ OER Check   │  → Yes: Reject, return existing ID
  └──────┬──────┘  → No: Continue
         │
         ▼
  ┌─────────────┐
  │ PHASE 1     │  OIW (Dept 20) pulls source code
  │ HARVEST     │  gitingest → compress to .md / .txt
  │             │  Deposit to: storage/vault/quarantine/
  └──────┬──────┘
         │
         ▼
  ┌─────────────┐
  │ PHASE 2     │  OHD (Dept 19) runs supply_chain_scan.ps1
  │ SANITIZE    │  Checks IOC, virus, .map leak, C2 connection
  │             │  → FAIL: Send verdict to OA, add to BLACKLIST
  └──────┬──────┘  → PASS: Stamp "OHD_CLEAN" + timestamp
         │
         ▼
  ┌─────────────┐
  │ PHASE 3     │  OA (Academy) reviews 8 Pillars
  │ AUDIT       │  Dept 9 (Strix): Security score >= 70
  │             │  Dept 12 (Legal): License check
  │             │  → FAIL: Block + OA Faculty Report
  └──────┬──────┘  → PASS: Stamp "OA_APPROVED" + score
         │
         ▼
  ┌─────────────┐
  │ PHASE 4     │  Dept 1 (Engineering): Build & Integration test
  │ FORGE       │  Write SKILL.md to schema standard
  │             │  Write basic unit tests
  └──────┬──────┘  → FAIL: Return to Dept 1 to fix
         │
         ▼
  ┌─────────────┐
  │ PHASE 5     │  OER (Dept 14 - registry-manager-agent) accepts
  │ REGISTER    │  Issues unique ID (SKILL-xxxx / PLG-xxxx / AGT-xxxx)
  │             │  Writes to SKILL_REGISTRY.json
  │             │  Moves to ecosystem/ correct tier
  └──────┬──────┘  Reports back to Orchestrator/CEO: "REGISTERED"
         │
         ▼
  ┌─────────────┐
  │ TELEMETRY   │  Receipt written to telemetry/qa_receipts/gate_oer/
  │ LOG         │  + Update brain/knowledge/repos/ (if new repo)
  └─────────────┘
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
| **OER (Dept 14)** | **Final authority** — issues ID, stores in ecosystem | `registry-manager-agent` |

---

## Related Files

| File | Purpose |
|---|---|
| [`OER_CHARTER.md`](OER_CHARTER.md) | Full OER charter (English) |
| [`OER_CHARTER-vn.md`](OER_CHARTER-vn.md) | Full OER charter (Vietnamese) |
| [`MASTER_SYSTEM_MAP-vn.md`](MASTER_SYSTEM_MAP-vn.md) | Full system map with 4 Daemon matrix |
| [`OA_CHARTER.md`](OA_CHARTER.md) | OA's 8 Pillars of integrity |
| [`../brain/rules/OIW_INTAKE_STRICT_RULE.md`](../../../../rules/OIW_INTAKE_STRICT_RULE.md) | OIW rules (incl. Rule 20.4: Zero Registration Rights) |
| [`../brain/rules/GLOBAL_BLACKLIST.md`](../../../../rules/GLOBAL_BLACKLIST.md) | Active IOC blacklist (OHD enforcement) |
| [`../system/ops/scripts/oer_register.py`](../system/ops/scripts/oer_register.py) | Phase 5 automation script |
| [`../system/security/supply_chain_scan.ps1`](../system/security/supply_chain_scan.ps1) | Phase 2 OHD scan script |
| [`../system/security/strix_policy.yaml`](../system/security/strix_policy.yaml) | Phase 3 OA scoring policy |

---

*OmniClaw Core Daemons & OER — v1.0 — 2026-04-02*
