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

## Building a New Plugin
To build a skill or plugin for OmniClaw:
1. Create a `SKILL.md` inside `ecosystem/skills/YOUR_SKILL_NAME/`.
2. Define the schema according to the Open Standard.
3. Submit it to the system. The Orchestrator will have Dept 20 (CIV) verify it.
4. If approved, Dept 04 (Registry) updates the global cache and your tool goes live immediately across all 21 departments.
