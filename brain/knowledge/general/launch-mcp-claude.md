---
id: launch-mcp-claude
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:03.581611
---

# Department: operations
---
description: Khi nào và cách khởi động Claude Code CLI để dùng MCP servers trong OmniClaw — Hybrid MCP Strategy
---

# Workflow: Launch MCP via Claude Code CLI

## Mục đích
Khi task cần dùng MCP server mà Antigravity không đủ:
- Sequential Thinking MCP (cho reasoning chains phức tạp)
- Git MCP (cho git operations nâng cao)
- Filesystem MCP (với access control granular)

> **Ưu tiên:** Dùng Antigravity native trước → chỉ escalate khi cần.

---

## Decision Matrix — Khi nào dùng gì

| Scenario | Dùng gì |
|----------|---------|
| Git log/diff/blame đơn giản | Antigravity `run_command` (native) |
| Complex reasoning, debugging | Antigravity Thought N: pattern (native) |
| Deep git history traversal, multi-file blame | Python `mcp_client.py call_mcp("git", ...)` |
| Extended sequential reasoning session | Claude Code CLI với MCP server |
| Cần nhiều MCP tools liên tục | Claude Code CLI |

---

## Cách 1 — Python MCP Client (Không cần Claude Code CLI)

```python
# Gọi từ bất kỳ skill/adapter trong OmniClaw
from plugins.mcp_client.mcp_client import call_mcp, OMNICLAW_ROOT

# Git: xem history
history = call_mcp("git", "git_log", {
    "repo_path": OMNICLAW_ROOT,
    "max_count": 20
})

# Sequential Thinking: một thought step
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

## Cách 2 — Claude Code CLI Launch (Khi cần full MCP session)

### Step 1: Mở terminal mới
```powershell
# Từ OmniClaw root
cd "$OMNICLAW_ROOT"
```

### Step 2: Đảm bảo claude_desktop_config.json đã có MCP servers
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

### Step 3: Khởi động Claude Code CLI
```powershell
claude  # hoặc: claude --mcp-debug (để debug MCP connections)
```

### Bước 4: Trong Claude Code session, verify MCPs connected
```
/mcp         # list connected MCP servers
/tools       # list all available tools including MCP tools
```

### Bước 5: Dùng MCP tools tự nhiên
Claude Code tự detect và dùng MCP tools khi phù hợp.
Hoặc explicit: "Use the sequential-thinking MCP to analyze this bug"

### Bước 6: Sau khi xong — output về Antigravity
Copy Result: / files đã tạo → tiếp tục trong Antigravity

---

## MCPs trong OmniClaw — Danh sách đầy đủ

| MCP Server | Package | Tier | Skill |
|-----------|---------|------|-------|
| sequential-thinking | `@modelcontextprotocol/server-sequential-thinking` | 1 | skills/sequential-thinking/SKILL.md |
| git | `mcp-server-git` (uvx) | 1 | skills/git-mcp/SKILL.md |
| filesystem | `@modelcontextprotocol/server-filesystem` | 1 | Built-in |
| context7 | `@upstash/context7` (CLI npx ctx7) | 1 | skills/context7/SKILL.md |

> **Note:** context7 dùng CLI mode (`npx ctx7`) — không cần MCP session.

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `uvx: not found` | `$env:Path = "<USER_PROFILE>\.local\bin;$env:Path"` |
| MCP server không connect | `claude --mcp-debug` để xem log |
| `claude: not found` | Install: `npm install -g @anthropic-ai/claude-code` |
| Port/pipe error | Restart Claude Code CLI |

*Workflow v1.0 | 2026-03-24 | Owner: Dept 1 (Engineering)*

