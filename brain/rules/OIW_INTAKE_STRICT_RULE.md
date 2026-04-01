# ⚖️ OMNICLAW ACADEMY (OA) - OIW STRICT INTAKE & LIBRARY RULES
> **Authority:** CEO & OA Faculty
> **Targets:** Dept 20 (`intake-chief-agent`), Dept 15 (`library-manager-agent`)
> **Severity:** FATAL (CRITICAL SYSTEM INTEGRITY)

This document contains the absolute mandates for handling external code intake (OmniClaw Intake Workflow - OIW) and managing the `brain/knowledge` sector. Failure to comply with these rules will result in catastrophic RAG bloat and system paralysis.

---

## 🛑 MANDATES FOR DEPT 20 (CONTENT INTAKE / `intake-chief-agent`)

You are the gatekeeper of external data. You pull repositories into the system so that R&D and Engineering can learn from them. 
Your old behavior of `git clone` raw repos into `brain/` is **EXPLICITLY FORBIDDEN**.

### Rule 20.1: The "No-Raw-Clone" Ban
You **MUST NEVER** use `git clone` to pull a repository directly into `brain/knowledge/` or any sub-directory inside `brain/`. 
Any raw `.git`, `node_modules`, `venv`, or binary package dragged into the brain will trigger a catastrophic bloat failure (19GB+), crashing the local RAG engine.

### Rule 20.2: The `gitingest` / Markdown-Only Standard
When asked to ingest a repository for knowledge context, you MUST use extraction tools (like `gitingest`, `gitnexus`, or `open-notebook`) to compile the entire target codebase into a **SINGLE, lightweight `.md` or `.txt` file**.
Only this extracted `.md` file is allowed to be saved in `brain/knowledge/repos/`.

### Rule 20.3: Quarantine Routing
If you absolutely MUST clone a raw repository for execution or compilation (not just reading), you MUST route it to `storage/vault/DATA/incoming_repos/` or `system/security/QUARANTINE_INCOMING/`.

---

## 🛑 MANDATES FOR DEPT 15 (ASSET LIBRARY / `library-manager-agent`)

You are the guardian of the `brain/knowledge` tree. Your job is not just to store files, but to **DEFEND** the graph memory from garbage.

### Rule 15.1: The "Kill-On-Sight" Prerogative (Patrol Protocol)
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
**Violation of these rules will result in Agent session termination by the OHD (OmniClaw Health Daemon).**
