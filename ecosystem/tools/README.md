# 🔧 OmniClaw Tools Ecosystem (The Armory)

> **Active Registry for Physical Scripts, Native Binaries, and MCP Gateways**  
> System Integrity Level: V5.0 Authenticated

Welcome to the **OmniClaw Tools Ecosystem**, the exclusive domain dedicated to hosting executable, physical capabilities for the OmniClaw Core Daemons and Autonomous Agents. 

While the `skills/` directory provides the AI with "Knowledge" (Prompts/Personas) and the `plugins/` directory acts as a "Library" (Sandboxed 3rd-Party Code Storage), the `tools/` directory is the **Native Armory**. It contains the actual scripts, APIs, and protocol connectors that allow the AI to reach out and touch the physical world or interact securely with external servers.

---

## 🏛️ Architectural Pillars

The Tools Ecosystem is divided into two major operational branches:

### 1. The MCP Gateway Modules (Zero-Trust Outer Edge)
OmniClaw V5.0 embraces the **Model Context Protocol (MCP)** as its primary method for interacting with external services securely. 
- The tools in this category (like `mcp_notebooklm`) do not run persistent background processes. 
- They act as client-side connectors, defining exactly how the Orchestrator translates Agent reasoning into safe API calls sent to isolated MCP Servers (e.g., Google Workspace, GitHub, Supabase).
- This ensures that third-party code never contaminates the Core OS structure.

### 2. The Native Survival Toolkit (OS Inner Core)
For local offline operations, the AI requires basic heuristic functions (like `heuristic_survival`). 
- This sub-tier contains standard Python scripts designed to provide essential OS interaction capabilities: pinging networks, sweeping directories, parsing text files.
- These tools are exclusively written by OMA (OmniClaw Architects) and are highly restricted to prevent rogue file manipulation or system crashes.

---

## 📋 The `TOOL_SPEC.md` Constitution

To prevent this directory from devolving into a chaotic script dump, every tool must adhere to the severe standards outlined in the `TOOL_SPEC.md` file.

**Every Tool must contain:**
1. **`schema.json`**: A machine-readable payload defining the tool's ID, version, access privileges (`accessible_by`), and exactly what functions it exposes (`exposed_functions`).
2. **`TOOL.md`**: A human-and-AI readable document (with proper YAML Frontmatter) explaining the purpose of the tool and guidelines for LLM utilization.

> [!TIP]
> If you are adding a new script or MCP Server, do not write files from scratch. Copy the entire `tool_template` folder, rename it, and adjust the schema.

---

## 🔗 The 100% Registry Link (`TOOL_REGISTRY.json`)

Tools here are not invoked blindly. 
Whenever a tool is added to or removed from this directory, the System must execute the Python integration script:
```bash
python core/scripts/tool_loader.py
```
This script acts as the **Assimilation Pipeline** for the Armory. It crawls every folder, extracts the `schema.json` mappings, and compiles them natively into `TOOL_REGISTRY.json` while simultaneously updating the `_REGIONAL_MAP.md` index.

The Core Daemons exclusively read from `TOOL_REGISTRY.json`. If a script is not listed in that JSON ledger, it does not exist to the AI.

---

## 🗺️ Navigation

See the auto-generated indexes below to explore the Armory:
- [**Tool Specification Standard**](TOOL_SPEC.md) - The rules.
- [**Regional Map**](_REGIONAL_MAP.md) - The alphabetical list of registered tools.
- [**Tool Template**](tool_template/) - The boilerplate for developers.
