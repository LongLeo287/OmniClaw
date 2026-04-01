# OER_CHARTER.md - OmniClaw Ecosystem Registry

**Authority:** CEO (LongLeo) | **Daemon Class:** Core Daemon #4
**Operated by:** Dept 14 (`registry-manager-agent`)
**Effective:** 2026-04-02

[**Vietnamese Version**](OER_CHARTER-vn.md) | [**Back to Docs**](../README.md)

---

## What is OER?

OER (OmniClaw Ecosystem Registry) is the **Fourth Core Daemon** of OmniClaw OS.
Where OIW harvests, OHD heals, and OA judges — **OER is the Registrar**.

OER is the sole entity authorized to:
- Issue unique IDs to all Skills, Plugins, Agents, and Workflows.
- Write and maintain `SKILL_REGISTRY.json` (the ecosystem manifest).
- Move approved artifacts into `ecosystem/` directories.
- Hold the Free-Pass traversal key to `brain/knowledge/` for capability coordination.

No other agent, daemon, or officer may perform these actions. This is not a suggestion.

---

## Core Responsibilities

### 1. The Registry (Sổ Cái Sinh Thái)
OER owns and operates the single source of truth: `brain/registry/SKILL_REGISTRY.json`.
Every Skill, Plugin, Agent, Workflow registered in OmniClaw must have an OER-issued ID before it can be used by the Orchestrator.

**ID Formats:**
| Asset Type | ID Format | Example |
|---|---|---|
| Skill | `SKILL-xxxx` | `SKILL-0104` |
| Plugin | `PLG-xxxx` | `PLG-0021` |
| Agent | `AGT-xxxx` | `AGT-0015` |
| Workflow | `WRK-xxxx` | `WRK-0008` |
| Department | `DEPT-xx` | `DEPT-22` |

### 2. Gate 0 — Duplicate Check
Before any pipeline begins, OER must confirm the asset does not already exist
in `SKILL_REGISTRY.json`. If a duplicate is detected, OER rejects the request
and returns the existing asset ID to the requestor.

### 3. Final Intake — PHASE 5
OER only acts **after** the following conditions are ALL met:
- `OHD_CLEAN` stamp present (supply chain verified, zero IOC)
- `OA_APPROVED` stamp present (score >= 70, all 8 Pillars reviewed)
- `SKILL.md` or equivalent manifest written by Dept 1 (Engineering)
- Source in `storage/vault/quarantine/` awaiting final transfer

OER then:
1. Generates a unique ID for the asset.
2. Copies the artifact from `quarantine/` to the correct `ecosystem/` tier.
3. Updates `SKILL_REGISTRY.json` with full metadata.
4. Writes a receipt to `telemetry/qa_receipts/gate_oer/`.
5. Notifies Orchestrator with a structured summary.

---

## The 5-Gate Automated Pipeline

```
[TRIGGER: CEO / Orchestrator / Dept Lead]
        |
 [GATE 0: OER Duplicate Check]  -----> REJECT if exists
        |
 [PHASE 1: OIW — Harvest & Gitingest]
   - Clone repo to storage/vault/quarantine/
   - Compress to .md via gitingest
        |
 [PHASE 2: OHD — Sanitize & Supply Chain Scan]
   - Run: system/security/supply_chain_scan.ps1
   - Run: npm audit (if JS), pip-audit (if Python)
   - Stamp: OHD_CLEAN | Timestamp
        |        \___FAIL__> OA Blacklist + Alert
 [PHASE 3: OA — Audit & Compliance]
   - Dept 9 (Strix): Security score >= 70
   - Dept 12 (Legal): License check
   - 8 Pillars review
   - Stamp: OA_APPROVED | Score
        |        \___FAIL__> OA Faculty Report + Block
 [PHASE 4: Dept 1 (Engineering) — Forge]
   - Write: SKILL.md / plugin manifest
   - Write: unit tests
   - Stage in: quarantine/ (polished, ready)
        |
 [PHASE 5: OER — Register]
   - Issue unique ID
   - Move to ecosystem/[tier]/
   - Update: SKILL_REGISTRY.json
   - Write: telemetry receipt
   - Notify: Orchestrator "REGISTERED"
```

---

## Access Control

| Entity | Read `ecosystem/` | Write `ecosystem/` | Update Registry |
|---|---|---|---|
| **OER (Dept 14)** | YES | **YES (ONLY)** | **YES (ONLY)** |
| OA | YES (audit) | NO | NO |
| OHD | NO | NO | NO |
| OIW | NO | NO | NO |
| Orchestrator | YES | NO | NO |
| CTO / C-Suite | YES | NO | NO |
| All other agents | NO | NO | NO |

---

## Relationship to Other Core Daemons

| Daemon | Role | Hands OER | Receives from OER |
|---|---|---|---|
| OIW | Harvester | Raw quarantined source | Confirmation slot is open |
| OHD | Doctor | `OHD_CLEAN` stamp | Scheduled scan requests |
| OA | Judge | `OA_APPROVED` stamp | Blacklist updates to enforce |

---

*OER Charter v1.0 — OmniClaw Corp — 2026-04-02*
