# 🌍 The OmniClaw Ecosystem (V5.0)

> **The Universal Hub for Skills, Intelligence, and Native Executables.**

The `ecosystem` directory forms the outer hemisphere of the OmniClaw operating system. While the `core/` folder contains the hardcoded Python Daemons (the central nervous system), the `ecosystem/` directory contains all "learned" or "acquired" intelligence.

Due to the V5.0 architectural upgrades, this entire zone operates under rigorous **Zero-Trust constraints**.

---

## 🏛️ The Tri-Pillar Architecture

The three most critical hubs governing AI capabilities represent the Tri-Pillar model:

### 1. 🧠 Skills (`ecosystem/skills/`)
**Role:** The Passive Competency Warehouse.
**Contents:** Over 1,932 markdown prompts and JSON schemas. This is where an AI goes to learn *how* to do something (e.g., SEO principles, Rust guidelines, or the Elon Musk persona). No executable code resides here.

### 2. 📚 Plugins (`ecosystem/plugins/`)
**Role:** The Cold-Storage Library.
**Contents:** Downloaded 3rd-party repositories, massive Node.js frameworks, or Dockerized services. Because they are untrusted, they are kept entirely "cold" (sandboxed). They cannot execute unless routed through `bridges/`.

### 3. 🦾 Tools (`ecosystem/tools/`)
**Role:** The Active Armory.
**Contents:** Fully trusted native Python utilities and MCP (Model Context Protocol) Gateways. These are the physical tools the AI is allowed to leverage (e.g., File Scanners, NotebookLM APIs, Github Ingestors).

---

## 🏗️ Support Logistics

Alongside the functional Tri-Pillars, the ecosystem features support infrastructure:

- **`bridges/`**: The OBD Harbor Layer. Starts and stops heavy Docker services from `plugins` (e.g., launching Mem0 or Firecrawl).
- **`ui_components/`**: Standardized React/Shadcn assets used when generating frontend apps for the User.
- **`workflows/`**: Pre-computed chains of thought or standard operating procedures.
- **`workforce/`**: The personnel roster defining our sub-agents.

## 🔗 Integrated Registries
To view the dynamically generated maps of the active components, refer to sub-level ledgers:
- `skills/SKILL_REGISTRY.json`
- `tools/TOOL_REGISTRY.json`
