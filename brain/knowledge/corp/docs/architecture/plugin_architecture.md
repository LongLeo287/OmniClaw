---
id: plugin-architecture
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:44:27.665225
---

# 🧩 Plugin Architecture (3-Tier System)

OmniClaw uses a strict 3-Tier Plugin Architecture to safely extend its capabilities. All code that interacts with the internet, touches sensitive files, or runs unvetted scripts goes through these tiers.

[**🇻🇳 Xem Bản Tiếng Việt**](plugin_architecture-vn.md) | [**Return to Docs Index**](../README.md) | [**📚 Wiki Reference**](https://github.com/LongLeo287/OmniClaw/wiki)

---

## The 3 Tiers of Trust

### 1. Tier 1: Core OS Tools (Highest Trust)
These are hardcoded deep inside the `system/ops/` architecture. They are tools the AI fundamentally needs to "breathe", such as reading its own Local Memory, spawning subagents, or reading `blackboard.json`.

### 2. Tier 2: Vetted Plugins (Sandbox)
Found inside the `ecosystem/plugins/` folder. These are community or third-party tools that have passed the rigorous **CIV (Content Intake)** pipeline and have been merged into the `SKILL_REGISTRY.json`.
- **Examples:** Open-Source Git scrapers, RAG vector injectors, Terminal shell tools.
- **Rule:** Before any Tier 2 plugin is run, Dept 10 (Strix Security) analyzes its payload for malicious commands.

### 3. Tier 3: External / MCP Servers (Zero Trust)
These are out-of-process servers using the **Model Context Protocol (MCP)**.
- OmniClaw acts as an MCP Host and can connect to off-site tools (e.g., Supabase MCP, Google Drive MCP).
- Because they run on the OS machine but are written by outside parties, they are kept entirely sandboxed. The AI can only invoke the schema they expose.

## Building a New Plugin (The Strict Handoff)
To build a skill or plugin for OmniClaw, a strict 3-step Isolation Handoff must be observed to prevent overlapping authority:
1. **Quarantine:** The raw plugin code (created by R&D or OIW) must be placed in `storage/vault/quarantine/`.
2. **Security Gate (Dept 10):** The Security Agent (`strix-agent`) inspects the code. If clean, it stamps the approval.
3. **Registration (Dept 14):** Only the Registry Manager (`registry-manager-agent`) has the file-level authority to move the approved code into `ecosystem/skills/`, define the Open Standard schema, and update the global `SKILL_REGISTRY.json`. No other agents (including CTO or Orchestrator) may write directly to the `ecosystem/` folder.

---

## 📖 Dept 14 Free-Pass to Brain (`brain/knowledge`)

While the creation and ingestion of knowledge sets are tightly guarded by the OmniClaw Intake Workflow (OIW) and Dept 15, the sole administrator of the ecosystem, **Dept 14 (`registry-manager-agent`), holds "Free-Pass" Authority.**
* **What this means:** Dept 14 can freely Read, Traverse, and Semantically Search the entire `brain/knowledge/` directory structure on behalf of the plugins it manages. **Standard executing agents, CTO, Orchestrator, and individual plugins DO NOT have this right.**
* **Protection Equivalence:** The `ecosystem/` directory and the `brain/knowledge/` directory share the exact same security posture: they are **Read-Only Vaults**. Tools and algorithms can view them, but no unauthorized modification is permitted.
