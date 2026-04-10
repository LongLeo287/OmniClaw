---
id: launch-mcp-claude
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:03.581611
---

# Department: operations
---
description: When and how to start Claude Code CLI to use MCP servers in OmniClaw — Hybrid MCP Strategy
---

# Workflow: Launch MCP via Claude Code CLI

## Purpose
When a task requires an MCP server that Antigravity cannot provide:
- Sequential Thinking MCP (for complex reasoning chains)
- Git MCP (for advanced git operations)
- Filesystem MCP (with granular access control)

> **Priority:** Use Antigravity native first → only escalate when needed.

---

## Decision Matrix — When to Use What

| Scenario | Use What |
|----------|---------|
| Simple Git log/diff/blame | Antigravity `run_command` (native) |
| Complex reasoning, debugging | Antigravity Thought N: pattern (native) |
| Deep git history traversal, multi-file blame | Python `mcp_client.py call_mcp("git", ...)` |
| Extended sequential reasoning session | Claude Code CLI with MCP server |
| Need many MCP tools continuously | Claude Code CLI |

---

## Method 1 — Python MCP Client (No Claude Code CLI Needed)

```python
# Call from any skill/adapter in OmniClaw
from plugins.mcp_client.mcp_client import call_mcp, OMNICLAW_ROOT

# Git: view history
history = call_mcp("git", "git_log", {
    "repo_path": OMNICLAW_ROOT,
    "max_count": 20
})

# Sequential Thinking: one thought step
thought = call_mcp("sequential-thinking", "sequentialthinking", {
    "thought": "Analyzing the root cause of this bug...",
    "thoughtNumber": 1,
    "totalThoughts": 4,
    "nextThoughtNeeded": True
})

# Filesystem: list directory
files = call_mcp("filesystem", "list_directory", {
    "path": f"{OMNICLAW_ROOT}/skills"
})
```

```bash
# CLI mode
python plugins/mcp-client/mcp_client.py git git_log '{"repo_path": "$OMNICLAW_ROOT", "max_count": 10}'
```

---

## Method 2 — Claude Code CLI Launch (When Full MCP Session Needed)

### Step 1: Open new terminal
```powershell
# From OmniClaw root
cd "$OMNICLAW_ROOT"
```

### Step 2: Ensure claude_desktop_config.json has MCP servers
File: `<USER_PROFILE>\AppData\Roaming\Claude\claude_desktop_config.json`
```json
{
  "mcpServers": {
    "sequential-thinking": { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"] },
    "git": { "command": "uvx", "args": ["mcp-server-git", "--repository", "$OMNICLAW_ROOT"] },
    "filesystem": { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", "d:\\OmniClaw Corp"] }
  }
}
```

### Step 3: Start Claude Code CLI
```powershell
claude  # or: claude --mcp-debug (to debug MCP connections)
```

### Step 4: In Claude Code session, verify MCPs connected
```
/mcp         # list connected MCP servers
/tools       # list all available tools including MCP tools
```

### Step 5: Use MCP tools naturally
Claude Code automatically detects and uses MCP tools when appropriate.
Or explicit: "Use the sequential-thinking MCP to analyze this bug"

### Step 6: When done — output back to Antigravity
Copy Result: / files created → continue in Antigravity

---

## MCPs in OmniClaw — Complete List

| MCP Server | Package | Tier | Skill |
|-----------|---------|------|-------|
| sequential-thinking | `@modelcontextprotocol/server-sequential-thinking` | 1 | skills/sequential-thinking/SKILL.md |
| git | `mcp-server-git` (uvx) | 1 | skills/git-mcp/SKILL.md |
| filesystem | `@modelcontextprotocol/server-filesystem` | 1 | Built-in |
| context7 | `@upstash/context7` (CLI npx ctx7) | 1 | skills/context7/SKILL.md |

> **Note:** context7 uses CLI mode (`npx ctx7`) — no MCP session needed.

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `uvx: not found` | `$env:Path = "<USER_PROFILE>\.local\bin;$env:Path"` |
| MCP server not connecting | `claude --mcp-debug` to see logs |
| `claude: not found` | Install: `npm install -g @anthropic-ai/claude-code` |
| Port/pipe error | Restart Claude Code CLI |

*Workflow v1.0 | 2026-03-24 | Owner: Dept 1 (Engineering)*