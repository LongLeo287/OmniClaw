# BLUEPRINT: OER Assimilation Pipeline (OAP)
# Architecture Framework: V2.1
# Governance: Omni Management Architect (OMA) & Security Firewall (OSF)

## 1. Executive Summary

The **OER Assimilation Pipeline (OAP)** is the central metabolic engine of the OmniClaw OS. It standardizes the procedure for ingesting external data (repositories, knowledge drops, external code) and converting it into highly distilled, secure, and searchable "Assimilated Nodes" inside the Brain cortex. 

Any daemon or script attempting to inject data into OmniClaw MUST adhere to these 5 rigorous stages. Deviations are hostile system actions.

---

## 2. The 5-Stage Protocol (Pipeline Topology)

### 🟢 Stage 1: INTAKE (The Cloner/Acquisition)
- **Actor:** `civ_intake_processor.py` / `sandbox_intake_pipeline.py`
- **Location:** Network ➔ `vault/quarantine`
- **Rules:**
  - Raw data is fetched blindly from the internet.
  - MUST be placed directly into quarantine or a sandbox_env.
  - No direct code execution is permitted during this phase.

### 🟡 Stage 2: VALIDATION (The Gatekeeper / X-Ray)
- **Actor:** `osf_malware_censor.py` (Governed by OSF Quarantine Guard)
- **Location:** `vault/quarantine`
- **Rules:**
  - OSF scans all incoming scripts using rules generated dynamically from `OSF_THREAT_INTELLIGENCE.json`.
  - Checks for Base64 encodings, destructive shell commands, and malicious payloads.
  - **Verdict:**
    - `0` (Sạch/Pass): Move to Stage 3.
    - `1` (Độc/Fail): Halt Pipeline. Send to OHD for Vaporization.

### 🟠 Stage 3: TRIAGE (The Sorter & Deduplicator)
- **Actor:** `oa_inbox_triage.py` (Governed by Omni Agent - OA)
- **Location:** `vault/tmp/state_queues/OER_INBOX`
- **Rules:**
  - Safe data is cleared to enter the actual INBOX.
  - OA generates deep structural hashing of folders.
  - Deduplication occurs automatically to prevent logic poisoning.

### 🔴 Stage 4: DISTILLATION (The Digester)
- **Actor:** `oa_swallow_engine.py` (The Swallow Algorithm)
- **Location:** `vault/tmp/state_queues/OER_INBOX`
- **Rules:**
  - Raw trees are recursively scraped, parsed, and compressed.
  - Irrelevant boilerplate (like `node_modules` or `.git`) is discarded.
  - Converts data into high-density Markdown cards: `*_DISTILLED.md`.
  - Original raw directories are flushed out by OMA Robo Purger.

### 🟣 Stage 5: INTEGRATION (The Mapper & Coder)
- **Actor:** `oma_knowledge_mapper.py` & `skill_loader.ps1`
- **Location:** `brain/knowledge/assimilated_repos/` & `ecosystem/skills/`
- **Rules:**
  - Distilled knowledge cards are moved to their permanent cerebral locations.
  - `_DIR_IDENTITY.md` graphs are updated to register the child nodes.
  - Global `SKILL_REGISTRY.json` and `LIBRARY_GRAPH.json` are refreshed dynamically.

---

## 3. Enforcement Policy (The OSF Promise)
The OAP Pipeline ensures that OmniClaw remains clean, hyper-optimized, and impossible to infect. Any attempt to bypass the **Validation Stage (Stage 2)** will result in the Orchestrator suspending the Daemon thread responsible for the bypass.

> All scripts inside `core/ops/scripts` that fetch Git repositories must invoke OSF before parsing. Failure to do so breaks the Island Sandbox Protocol.

---

## 4. File Morphology (The Artifact Taxonomy)

To prevent scattered waste ("file pollution") and guarantee a closed Ouroboros loop, Daemons are strictly prohibited from generating arbitrary file extensions outside of these explicit artifact typings:

### 🧟 The Raw Zone (`vault/quarantine` & `vault/tmp`)
- **Allowed:** Unrestricted unstructured files (`*.py`, `*.js`, `*.cpp`, `*.ts`, `package.json`, etc.) from external cloned inputs.
- **Rules:** Cannot be executed (Sandbox lock). Automatically Garbage Collected via `oma_robo_purger.py` at the end of the cycle. 

### 🧠 The Distillation Zone (`brain/knowledge/assimilated_repos`)
- **Allowed:** 
  1. `[RepoName]_DISTILLED.md`: The pure extracted logic/memory of the code. Code files must be compiled into this flat markdown surface.
  2. `_DIR_IDENTITY.md`: Graph Identity Card.
- **Rules:** RAW code files (`.py, .js`) are **BANNED** from existence inside the Brain zone.

### 🌐 The Logic Zone (`ecosystem/plugins` & `brain/memory`)
- **Allowed:**
  1. `SKILL.md`: Actionable executable markdown plugins.
  2. `*.json` (Registries): `SKILL_REGISTRY.json`, `LIBRARY_GRAPH.json`, `OSF_THREAT_INTELLIGENCE.json`.
- **Rules:** These JSON and MD files are read-heavy graph nodes. They represent the living awareness of OmniClaw. 

*If a file is not in this Taxonomy, it does not legally belong in the OAP Lifecycle. It is an orphan and will be vaporized.*
