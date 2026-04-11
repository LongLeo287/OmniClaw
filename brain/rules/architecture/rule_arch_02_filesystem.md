---
id: RULE-ARCH-02
name: -The 4-Pillar Master Blueprint-
tags: [core, architecture, filesystem, topology]
owner: OMA
type: system_rule
registered: true
---

# RULE-ARCH-02: THE 4-PILLAR SANCTUMS (FILESYSTEM BLUEPRINT)

> [!IMPORTANT]
> **Authority:** OMA (OmniClaw Master Architect)
> **Severity:** ABSOLUTE. Strictly forbids any action of creating Files/Folders outside the boundaries of this map. Violating entities will be isolated by OMA and handed over to OHD for Cleanup/Healing or sent to OA for Sentencing.

---

## OVERVIEW
The OmniClaw v5.0 system eliminates clutter by strictly organizing all data into **4 Core Zones (The 4 Pillars)**. OMA operates a Deepscan loop periodically to monitor this model.

---

### ðŸ§  1. `/brain/` (Memory & Knowledge Zone)
This is the Semantic Graph Space. The system strictly governs this space via the **MemPalace 3-Layer Spatial Architecture (RULE-ARCH-06)** to prevent malicious code execution:
- ðŸ“‚ **`rules/`** (Laws & Constitution). *[Sanctum Zone]*
- ðŸ“‚ **`knowledge/`** (The 3-Layer Ecosystem).
  - **Layer 1 (Executable Core):** `plugins/` and `frameworks/`. Validated tools and scripts that AI Agents are explicitly permitted to Execute directly.
  - **Layer 2 (Dry Reading):** `repos/` and `general/`. Read-Only reference repositories and documentation. **Execute permission is fiercely forbidden** here.
  - **Layer 3 (Remote Runtimes):** `REMOTE/claws/`. Highly isolated remote or containerized agentic environments.
- ðŸ“‚ **`memory/`** (Dynamic Memory).
  - `/tenants/`: Strictly separates the memory space of each Department, preventing read bleed-overs.
  - `/agents/`: Holds highly volatile queue files like `activation_status.json` and task queues.
- ðŸ“‚ **`registry/`** (Declaration Vault). Contains mappings and logs. The supreme write authority belongs to **OER**.
- ðŸ“‚ **`agents/`** (Core Personas & Boot). Contains solely the lightweight Boot Protocols (`gemini.md`, `claude.md`) for Central OmniClaw Agents.
- ðŸ“‚ **`brain/memory/`** (Blackboard). System routing tables and blackboards connecting Agents together.
- ðŸ“‚ **`indices/`** & ðŸ“‚ **`chroma_db/`** (Graphs & Vector Data). Managed exclusively by OER/Retrieval nodes.

---

This is the executing Heart of the Operating System. Contains critically important Python/Powershell Backend scripts. *[Sanctum Zone]*
- ðŸ“‚ **`daemons/`** (Headquarters of the 5 Forces). Forcing the creation of any Daemon outside of OIW, OMA, OER, OHD, OA is prohibited.
- ðŸ“‚ **`security/`** (Firewall & Security).
  - `/QUARANTINE_INCOMING/`: A mandatory checkpoint for all external source code scraped by OIW.
- ðŸ“‚ **`bridges/`** (Multi-channel communication gateways, e.g., Telegram Bot).

---

### ðŸ› ï¸ 3. `/ecosystem/` (Skills & Weapons Zone)
Where the system integrates extended functionalities for AI Agents. *[Sanctum Zone]*
- ðŸ“‚ **`skills/`** (Independent, reusable scripts).
  - `[Empty Space]`: Capacity for future new Skills. OER acts as the Librarian.
- ðŸ“‚ **`plugins/`** (Large 3rd-party tool packages).
- ðŸ“‚ **`workflows/`** (Multi-step scaled automated behavior flows).

---

### ðŸ—„ï¸ 4. `/vault/` (Heavy Storage Zone)
The massive cold storage containing temporary trash files, Databases, Images, and heavy Models. LLM Agents are restricted from accessing this area unless specified.
- ðŸ“‚ **`assets/`** (Images, Videos, Audio).
- ðŸ“‚ **`archives/`** (Contains old Log files, Database Backups, preserved Repositories holding machine code).
- ðŸ“‚ **`models/`** (Contains static LLM Weights if applicable).
- ðŸ“‚ **`tmp/`** (Rogue processing zone).
  - `/quarantine/`: **Medical Isolation Camp**. OHD is stationed here.
  - `/sandbox_env/`: Raw working ground for OIW and OA (has a dedicated `/OA_workshop/`).
  - `/raw_knowledge_dumps/`: Massive blob data warehouse waiting for OA to learn.
  - `/state_queues/`: **[OBSOLETE]** Handover mailboxes between Daemons have been replaced by the **Neural Bus** architecture. Daemons now listen to live events instead of polling physical file queues.

---

## ðŸš« STRICT TABOOS:
1. It is absolutely forbidden to use the Root directory (`D:/OmniClaw/...`) to store stray folders/files such as `docs/`, `asset/`, `storage/`, `logs/`. 
2. Every `[Empty Space]` has been measured and licensed by OMA on the System Map. As the system expands, OMA->s exact positioning must be used. Overstepping authority will trigger prosecution by the Court (OA).
3. **Deep Localization Law:** Sub-zones belonging to `brain/knowledge/` and `ecosystem/skills/` MUST be marked by OER with a `_DIR_IDENTITY.md` sign at their root. This sign declares the directory identity to optimize context for the MLLM Agent. Fast-changing areas (like `vault/tmp/`) are absolutely forbidden from having tiny signs scattered around causing Git clutter.
4. **Forced Sandbox Constraint:** EVERY Agent, Script, or Crawler generating trash files, temp data, or raw logs MUST DEFAULT to writing into `vault/tmp/sandbox_env/`. 100% Forbidden from freely writing files into `brain/` or `core/`. Data seeking to enter the Knowledge Zone must be submitted through `vault/tmp/quarantine/` for OA & OHD registration.
5. **PROJECT FIREWALL ISOLATION RULE:** When Humans or AI Agents (Frontline Team) execute Build Tasks (App Creation, Web Coding, Dev Env Setup...), it is ABSOLUTELY PROHIBITED to place Project Folders deep inside the OmniClaw OS Ecosystem (`D:/OmniClaw/OmniClaw Ecosystem/OmniClaw/`). All junk Projects / Sub-apps must be stored in the Independent External Crafting Zone outside the OS (e.g., `D:/OmniClaw/OmniClaw Ecosystem/Projects/`). OmniClaw is the force-coordinating Engine; absolutely do not use the Core OS body as a dumping ground for Junk Projects.



---
*OmniClaw V5.0 | Protected by OSF Daemon | 8-Daemon Master Architecture*

