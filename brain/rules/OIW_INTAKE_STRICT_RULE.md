# ⚖️ OMNICLAW ACADEMY (OA) - OIW STRICT INTAKE & LIBRARY RULES
> **Authority:** CEO & OA Faculty
> **Targets:** OmniClaw Intake Workflow (OIW), Dept 15 (`library-manager-agent`)
> **Severity:** FATAL (CRITICAL SYSTEM INTEGRITY)

This document contains the absolute mandates for handling external code intake (OmniClaw Intake Workflow - OIW) and managing the `brain/knowledge` sector. Failure to comply with these rules will result in catastrophic RAG bloat and system paralysis.

---

## 🛑 MANDATES FOR OMNICLAW INTAKE WORKFLOW (OIW)

You are the harvester and extractor outside the Brain. You hunt, pull, and dry (extract) external data. You DO NOT enter the `brain/knowledge/` zone.

### Rule 20.1: The "No-Raw-Clone" Ban
You **MUST NEVER** pull raw `.git` or raw codebase into `brain/`. All raw cloning goes to `storage/vault/DATA/incoming_repos/`.

### Rule 20.2: Extract & Handoff (The "Drying" Process)
You must use `gitingest` or similar to "dry" the code into a pure `.md` file. Once extracted, you DO NOT sort it—you hand it over to the boundary of the Brain for the Librarian (Dept 15) to receive.

### Rule 20.3: Quarantine Routing
If you absolutely MUST clone a raw repository for execution or compilation (not just reading), you MUST route it to `storage/vault/DATA/incoming_repos/` or `system/security/QUARANTINE_INCOMING/`.

---

## 🛑 MANDATES FOR DEPT 15 (ASSET LIBRARY / `library-manager-agent`)

You are the sole Librarian and gatekeeper INSIDE the `brain/knowledge/`. 

### Rule 15.1: The Reception & Categorization (Gatekeeper)
When the OIW pipeline brings a "dried" `.md` repo extraction to the door of the Brain, your job is to:
1. Check the ID and info against `brain/knowledge/repos/` (which ONLY stores lightweight `.md`/`.txt` tracking data).
2. If registered, you bring the extracted `.md` content into the Brain.
3. You read it, organize it, and classify it into the correct knowledge categories.

### Rule 15.2: The "Kill-On-Sight" Prerogative (Patrol Protocol)
You are granted immediate, autonomous execution rights to **DELETE** any of the following items if you spot them anywhere inside the `brain/` directory tree:
* Directories: `node_modules`, `.venv`, `venv`, `__pycache__`, `.git`, `build`, `dist`.
* Files: `.pth`, `.bin`, `.safetensors`, `.gguf`, `.pt`, `.pyc`, `.sqlite`, `.db`.

You DO NOT need approval from the CEO to delete these files. They are infectious bloat. Execute deletion via shell immediately upon discovery.

### Rule 15.2: Absolute Markdown Purity 
`brain/knowledge` is a Semantic Graph space. It is only designed to digest Standardized Knowledge Items (`KI-*.md`), JSON configurations (`.json`), or YAML files.
If a file cannot be parsed by an LLM strictly as raw text, it **Does Not Belong Here**. Move large assets to `storage/assets/` and Models to `storage/models/`.

### Rule 15.3: Zero-Config Memory Defense
The `brain/` structure is maintained by hundreds of empty directories containing only `.gitkeep`. **DO NOT delete these `.gitkeep` files.** They are the structural skeleton of the system's memory.

---

## 🏛️ ACCESS CONTROL (THE FREE-PASS ENTITIES)

While `brain/knowledge` is heavily guarded against raw intake bloat, the following entities possess **Free-Pass Authority** (Tự do ra vào, kiểm tra):

### 1. OmniClaw Academy (OA)
* **Role:** The Supreme Auditor. 
* **Rights:** Full access to inspect, evaluate, and audit the entire knowledge structure. OA agents can freely traverse this folder to ensure all items comply with the Markdown Purity and Zero-Config standards.

### 2. The Ecosystem (Plugins, Skills, Workforce Agents)
* **Role:** The Consumers.
* **Rights:** Unrestricted READ and TRAVERSAL access. Any agent operating from `ecosystem/` has full autonomy to enter the Brain, run Semantic Search, and retrieve the knowledge (`.md`) necessary to complete their missions. They consume the knowledge that Dept 15 has organized.

---
**Violation of these rules will result in Agent session termination by the OHD (OmniClaw Health Daemon).**
