# OmniClaw Brain Agents 🧠

**Path:** `brain/agents/`
**Namespace:** `brain.agents`
**Status:** V5.0 (Standardized)

This directory serves as the **Initialization sequence & Routing core** for OmniClaw Agents. It acts as the bridge connecting the LLMs (Claude, Gemini), the System Daemons, and the vast 28-Department Workforce.

---

## 📂 Core Architecture

Unlike standard runtime environments, this directory does **not** contain executable Python or Node code. It holds declarative metadata, prompts, and JSON routers that dictact how AI nodes boot up and behave.

### 1. Boot Protocols (The "Souls")
The master prompts that define the core agents' initial context and sequence.
*   **[`gemini.md`](./gemini.md)**: Boot sequence and hyper-focus protocol for Antigravity (Gemini). Dictates the 8-step mandatory boot, ensuring it loads all indices and governance rules before taking action.
*   **[`claude.md`](./claude.md)**: Boot sequence for the Claude Code CLI. Operates as the Tier 2 executor that actively reads the blackboard for tasks when the CEO opens the terminal.

### 2. System Intelligence (The "Neurology")
*   **[`system_router.json`](./system_router.json)**: The static map of all 28 workforce departments. When the OmniClaw Orchestrator (or an LLM reading this file) needs to find the proper agent for a task, it refers to this file to match department names `<->` agent names.
*   **[`activation_status.json`](./activation_status.json)**: The live-state ledger of system health. Modified dynamically by OmniClaw daemons (`ohd_health`, `omniclaw_orchestrator`) to mark which agents are `ONLINE` or `OFFLINE`.

### 3. Structural Integrity 
*   **[`_DIR_IDENTITY.md`](./_DIR_IDENTITY.md)**: OmniClaw V5.0 OMA (OmniClaw Map Architect) tag. Definitively identifies the folder for daemons, stopping accidental deletions and allowing map aggregations.

---

## 🚦 System Interaction Flow
1. CEO triggers terminal (`aos` / `claude`).
2. AI reads its respective Boot Protocol (`gemini.md` or `claude.md`).
3. CLI or Orchestrator daemon reads `<activation_status.json>` to check who is awake.
4. Payload intent is mapped using `<system_router.json>` to the corresponding department in `ecosystem/workforce/departments/`.

> **Note to Developers:** Do **not** place `.py` or `.js` execution logic here. Logic scripts belong in `core/ops/` or `core/daemons/`. This folder is strictly intended for JSON state and Markdown LLM prompts.
