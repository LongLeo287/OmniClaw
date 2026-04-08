---
id: RULE-ARCH-01
name: "The 5 Core Daemons Framework"
tags: [core, architecture, daemons, governance]
owner: OA
type: system_rule
registered: true
---

# RULE-ARCH-01: THE 6 CORE DAEMONS MATRIX

> [!IMPORTANT]
> **Authority:** CEO & OmniClaw Academy (OA)
> **Severity:** ABSOLUTE (All agents and system logic must route through this matrix).

The OmniClaw system (v5.0) operates upon the functional decentralization platform of the **6 Core Daemons** (including OSF). Any violation of this data routing principle will result in prosecution by OA.

---

## 1. Identity Map (The 5 Pillars)

### 📥 1. OIW (OmniClaw Intake Workflow) - The Customs Force
* **Role:** Harvester. 
* **Mandate:** OIW stands outside the System. It pulls GitHub repositories, web content, and extracts them into Markdown. OIW MUST NEVER inject files directly into `brain/`. OIW must place data at the front gate (or Quarantine).

### 🗺️ 2. OMA (OmniClaw Master Architect) - The Chief Architect
* **Role:** Keeper of the Omniscient Map. Closely linked with all core daemons.
* **IRON RULE:** Manage planning with **"Move Only, Absolute Ban on Delete Commands"**. OMA must absolutely never use destruction commands (Delete/Remove). All trash must be moved to the Quarantine zone. Permanent destruction is the exclusive final authority of the OA Court and the OHD Incinerator.
* **Mandate:** Continuously patrol the 4 Architectural Tiers (`brain/`, `core/`, `ecosystem/`, `vault/`).
* Holds the responsibility of issuing `OMA_SYSTEM_MAP.json`. If it detects stray garbage files outside the root directory, or `.md` files LACKING `id/tags` YAML, OMA will forcibly detain that file into `vault/tmp/quarantine/`.
* **Deepscan Privilege:** Possesses the all-seeing eye across every corner of the system. For any room/tier/void that is unfilled or redundant, OMA will note these "Empty Spaces" on the Map to signal capacity to other Daemons.
* *Note: OMA patrols and documents, but does not arbitrarily modify file contents. Untagged trash is thrown to OHD and OA to handle.*

### 🏥 3. OHD (OmniClaw Health Daemon) - Hospital & Environment
* **Role:** Healer & Janitor.
* **Mandate:** Permanently stationed at the Quarantine area. 
* **(Healing):** For files stripped of ID/Tags brought in by OMA, OHD will perform an examination, inject the YAML Tags, restore the correct format structure, and release the healthy file back into the system.
* **(Garbage Collection):** Cleans up the environment. Bloated log files and foul tmp trash will be completely incinerated by OHD to keep the OS permanently Healthy.

### 🛂 4. OER (OmniClaw Ecosystem Registrar) - Chief Registrar & Librarian
* **Role:** Ecosystem Manager & Registrar. The Royal Guard defending the Core Zone.
* **Mandate:** Acts as the librarian and mends the "brain" map of the entire OmniClaw system. 
* After OHD successfully processes a file, OER is the sole entity with exclusive rights to register and load that new file/entity into federated shards via `brain/indices/FAST_{TYPE}_INDEX.json` and `SKILL_REGISTRY.json`.
* **The Sanctums (Inviolable Zones):** OER is the Sole Keeper of the 3 Absolute Core Zones:
  1. `core/` (Pump engine & Daemons)
  2. `brain/rules/` (Constitutional laws)
  3. `ecosystem/` (Weapons & Skills)
  All Agents/Sub-agents are 100% prohibited from arbitrarily creating or modifying files in these 3 zones. All changes must pass through the OER gateway. Any file that fails to pass OER is considered non-existent (invisible).

### 🏛️ 5. OA (OmniClaw Academy) - The Academy, Analysis Institute & Court
* **Role:** Supreme Court, Research Institute.
* **Mandate:** The pinnacle of system knowledge. OA performs analysis, learning, research, and Self-upgrade for the entire AI OS.
* **Authority:** Any case showing signs of "overstepping authority" or falling outside the understanding of OIW, OMA, OHD, and OER must be escalated to seek the jurisdiction of OA.
* **Trash Processing (Alchemy):** OA will occasionally dig through system trash (files in quarantine/trash) to distill the essence, analyzing and summarizing knowledge before complete disposal. OA teaches and passes down standard doctrines to the Agents.

### 🛡️ 6. OSF (OmniClaw Sandbox Firewall) - Border Control
* **Role:** Security Sentinel.
* **Mandate:** Acts as the impenetrable layer verifying all raw data from OIW against malicious signatures, hardcoded API keys, and vulnerabilities BEFORE deeper components access them.

---

> [!NOTE]
> **To view the exact routing pipeline sequence, refer exclusively to `RULE_OAP_PIPELINE.md` (The 6-Gate Golden Pipeline). Do not recreate conflicting routing sequences here.**
