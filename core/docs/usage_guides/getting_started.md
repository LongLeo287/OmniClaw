---
id: getting-started
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:44:27.670194
---

# 🚀 Getting Started with OmniClaw

Welcome aboard! This guide will walk you through setting up OmniClaw, booting your first AI orchestrator, and linking your local workspace.

[**🇻🇳 Xem Bản Tiếng Việt**](getting_started-vn.md) | [**Return to Docs Index**](../README.md) | [**📚 Wiki Reference**](https://github.com/LongLeo287/OmniClaw/wiki)

---

## 1. Prerequisites

Before unleashing the 21-department AI framework, ensure you have the following installed:
- **Node.js (v18+)** for the MCP ecosystem and JavaScript-based tools.
- **Python (3.11+)** for the deep reasoning backends and pipeline workflows.
- **Docker** (Optional but recommended) for spinning up isolated local DBs and APIs.
- API Keys: Provide instances of `GEMINI_API_KEY` (or Anthropic keys if defaulting to Claude Code).

## 2. Installation Setup

1. Clone the repository to your local machine: `git clone <repo-url>`
2. **[CRITICAL] Pull the Heavy Vaults:** Since heavy data (like Agent Memory and massive code plugins) are not stored on GitHub due to the 100MB limit, you MUST pull the delta fragments back from HuggingFace/Drive:
   ```bash
   python system/ops/scripts/omniclaw_data_pull.py
   ```
3. Install the dependencies: `pip install -r requirements.txt`
4. Spin up the initial routers using `infra/llm/router.yaml`.

## 3. First Boot (Lighting the Core)

The AI OS starts by booting the main orchestrator memory file.
To activate the **Antigravity** central hub engine, load the `GEMINI.md` file using your agent interface in your IDE (or Claude Code for `CLAUDE.md`).

Upon first boot, the system will:
1. Read the `brain/shared-context/blackboard.json` to view current global state tasks.
2. Register all accessible capabilities from the `SKILL_REGISTRY.json`.
3. Stand by for CEO (Human) instructions.

## 4. Next Steps

- Go read the [**Agent Commands**](agent_commands.md) to understand how to interact.
- Submit a repository for processing via the [**CIV Intake**](../workflows/data_intake.md) protocol.
