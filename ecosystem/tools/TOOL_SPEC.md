# OmniClaw TOOL_SPEC (v5.0)

This document defines the strict constraints for adding physical utility scripts, MCP servers, and executable API wrappers to the `ecosystem/tools` registry.

Unlike `skills` (which are prompts), `tools` are physical code. 

## Mandatory Structure

Every tool housed in `ecosystem/tools/` MUST be a subdirectory containing exactly:
1. `TOOL.md` - Context, execution flags, and LLM guidelines.
2. `schema.json` - Interoperability map for the Core Daemons.

### 1. The `TOOL.md` Frontmatter
The `TOOL.md` must lead with valid YAML frontmatter dictating access rules.

```yaml
---
id: mcp_notion
name: Notion MCP Connector
status: active
integration_type: mcp_server # or "python_script", "native_binary"
accessible_by:
  - Orchestrator
tags: [productivity, api]
---
```

### 2. The `schema.json` Map
The Tool Loader script (`core/scripts/tool_loader.py`) parses this JSON file to assemble the `TOOL_REGISTRY.json`, which gives AI Agents context of what commands they are legally allowed to execute.

```json
{
    "id": "mcp_notion",
    "name": "Notion MCP Connector",
    "integration_type": "mcp_server",
    "accessible_by": ["Orchestrator"],
    "exposed_functions": [
        {
            "name": "search_pages",
            "description": "Searches for Notion pages by keyword."
        }
    ]
}
```

## Security Execution Context
Tools inside this registry **CANNOT** run themselves as background daemon tasks unless explicitly invoked by the Core OS via a `launch_*.py` bridge or a direct `subprocess.call` from an approved Agent context.
