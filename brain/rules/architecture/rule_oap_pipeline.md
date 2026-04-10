---
id: rule-oap-pipeline
name: Omnibus Assimilation Pipeline (OAP)
version: 5.0
enforced_by: OMA
scope: core_daemons
tags: [architecture, pipeline, core, oap]
---

# OmniClaw Assimilation Pipeline (OAP)

The following pipeline is the highest law of data and repository assimilation within OmniClaw. It guarantees 100% full-stack autonomous execution without human intervention. Core Daemons MUST run asynchronously via their respective command panels or background Watchdogs.

## The 6-Daemon Golden Pipeline

### 1. Gate 1: OIW (Intake Harvester)
- **Role:** The Plow & Harvester.
- **Rules:** OIW listens to Neural Bus events (e.g. `URL_SUBMITTED`). It uses advanced context compression (like `gitingest`) to crush full repositories into minimal text blocks.
- **Destination:** Raw data is shoved into `vault/tmp/sandbox`.

### 2. Gate 2: OSF (Sandbox Firewall)
- **Role:** The Guard.
- **Rules:** OSF scans every single byte in `vault/tmp/sandbox`. If `package.json` contains blacklisted packages listed in `global_blacklist.md`, OSF terminates the asset. 

### 3. Gate 3: OHD (Healer/Cleaner)
- **Role:** The Sanitizer.
- **Rules:** Unzips and unpacks data. Purges redundant files, minifies `.json`, deletes massive cache folders (`node_modules`) BEFORE they pollute the ecosystem.

### 4. Gate 4: OAP & OA Triage Matrix (Value Assessment)
- **Role:** The Sorter & Assessor.
- **Rules:** Because human intervention (CIV Reports) is abolished, OAP delegates an automated Value Assessment to the Academy Daemon (OA). OA scans the repository for systemic value:
  - 🌟 **[Grade A - Evolutionary]:** Repo contains high-value AI Logic, new agentic frameworks, or novel toolsets. OAP completely reroutes this Data into `vault/tmp/OA_workshop/`. Here, OA is authorized to dissect the code to auto-spawn **new Skills, Plugins, or Sub-Daemons**.
  - 📘 **[Grade B - Standard Knowledge]:** Repo is standard reference material. OAP executes the **MemPalace Logic**: Code goes verbatim to Layer 1 (Drawers) in `brain/knowledge/`; Chat/Docs invoke `mempalace_agent` into Layer 2 (AAAK Closets).
  - 🗑️ **[Grade C - Junk]:** Low value. Ignored or compressed blindly into `vault/archives/`.

### 5. Gate 5: OER (Registrar)
- **Role:** The Indexer.
- **Rules:** Writes entry into `SKILL_REGISTRY.json` or `FAST_KNOWLEDGE_INDEX.json` and announces to Neural Bus that the entity is live.

### 6. Gate 6: OA (Evolution & Graduation)
- **Role:** The Analyst.
- **Rules:** Reads the final output from the Bus and derives new System Rules or OS upgrades if needed.


---
*OmniClaw V5.0 | Protected by OSF Daemon | 8-Daemon Master Architecture*
