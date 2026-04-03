---
id: RULE-ARCH-02
name: "The 4-Pillar Master Blueprint"
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

### 🧠 1. `/brain/` (Memory & Knowledge Zone)
This is a Read-Only Zone (Semantic Graph Space). It contains pure data (Text, Markdown, JSON, YAML). Executable Code or Binaries are strictly forbidden here.
- 📂 **`rules/`** (Laws & Constitution). *[Sanctum Zone]*
- 📂 **`knowledge/`** (Dry Knowledge Base). Storage for documentation, READMEs, and Condensed Knowledge.
  - `[Empty Space]`: Reserved area to export Knowledge Items (KIs) when OA extracts learned insights from trash.
- 📂 **`memory/`** (Dynamic Memory).
  - `/tenants/`: Strictly separates the memory space of each Department, preventing read bleed-overs.
- 📂 **`registry/`** (Declaration Vault). Contains `FAST_INDEX.json`, `SKILL_REGISTRY.json`, and `OMA_SYSTEM_MAP.json`. The supreme write authority belongs to **OER**.

---

### ⚙️ 2. `/core/` (System Engine Zone)
This is the executing Heart of the Operating System. Contains critically important Python/Powershell Backend scripts. *[Sanctum Zone]*
- 📂 **`daemons/`** (Headquarters of the 5 Forces). Forcing the creation of any Daemon outside of OIW, OMA, OER, OHD, OA is prohibited.
- 📂 **`security/`** (Firewall & Security).
  - `/QUARANTINE_INCOMING/`: A mandatory checkpoint for all external source code scraped by OIW.
- 📂 **`bridges/`** (Multi-channel communication gateways, e.g., Telegram Bot).

---

### 🛠️ 3. `/ecosystem/` (Skills & Weapons Zone)
Where the system integrates extended functionalities for AI Agents. *[Sanctum Zone]*
- 📂 **`skills/`** (Independent, reusable scripts).
  - `[Empty Space]`: Capacity for future new Skills. OER acts as the Librarian.
- 📂 **`plugins/`** (Large 3rd-party tool packages).
- 📂 **`workflows/`** (Multi-step scaled automated behavior flows).

---

### 🗄️ 4. `/vault/` (Heavy Storage Zone)
The massive cold storage containing temporary trash files, Databases, Images, and heavy Models. LLM Agents are restricted from accessing this area unless specified.
- 📂 **`assets/`** (Images, Videos, Audio).
- 📂 **`archives/`** (Contains old Log files, Database Backups, preserved Repositories holding machine code).
- 📂 **`models/`** (Contains static LLM Weights if applicable).
- 📂 **`tmp/`** (Rogue processing zone).
  - `/quarantine/`: **Medical Isolation Camp**. OHD is stationed here.
  - `/sandbox_env/`: Raw working ground for OIW and OA (has a dedicated `/OA_workshop/`).
  - `/raw_knowledge_dumps/`: Massive blob data warehouse waiting for OA to learn.
  - `/state_queues/`: Handover mailbox between Daemons.
    - `OIW_INBOX/` — OER notifies OIW to scrape updates.
    - `OHD_TRIGGER/` — Any Daemon notifying OHD of an issue.
    - `OER_INBOX/` — Clean files waiting for OER registration.
    - `OA_DISPATCH_QUEUE/` — Complex cases waiting for OA verdict.

---

## 🚫 STRICT TABOOS:
1. It is absolutely forbidden to use the Root directory (`D:/LongLeo/...`) to store stray folders/files such as `docs/`, `asset/`, `storage/`, `logs/`. 
2. Every `[Empty Space]` has been measured and licensed by OMA on the System Map. As the system expands, OMA's exact positioning must be used. Overstepping authority will trigger prosecution by the Court (OA).
3. **Deep Localization Law:** Sub-zones belonging to `brain/knowledge/` and `ecosystem/skills/` MUST be marked by OER with a `_DIR_IDENTITY.md` sign at their root. This sign declares the directory identity to optimize context for the MLLM Agent. Fast-changing areas (like `vault/tmp/`) are absolutely forbidden from having tiny signs scattered around causing Git clutter.
4. **Forced Sandbox Constraint:** EVERY Agent, Script, or Crawler generating trash files, temp data, or raw logs MUST DEFAULT to writing into `vault/tmp/sandbox_env/`. 100% Forbidden from freely writing files into `brain/` or `core/`. Data seeking to enter the Knowledge Zone must be submitted through `vault/tmp/quarantine/` for OA & OHD registration.
5. **PROJECT FIREWALL ISOLATION RULE:** When Humans or AI Agents (Frontline Team) execute Build Tasks (App Creation, Web Coding, Dev Env Setup...), it is ABSOLUTELY PROHIBITED to place Project Folders deep inside the OmniClaw OS Ecosystem (`D:/LongLeo/AI OS CORP/AI OS/`). All junk Projects / Sub-apps must be stored in the Independent External Crafting Zone outside the OS (e.g., `D:/LongLeo/AI OS CORP/Projects/`). OmniClaw is the force-coordinating Engine; absolutely do not use the Core OS body as a dumping ground for Junk Projects.
