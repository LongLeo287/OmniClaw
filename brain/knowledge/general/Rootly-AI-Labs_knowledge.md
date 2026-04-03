---
id: rootly-ai-labs-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:09.868072
---

# KNOWLEDGE EXTRACT: Rootly-AI-Labs
> **Extracted on:** 2026-03-30 17:53:01
> **Source:** Rootly-AI-Labs

---

## File: `rootly-mcp-server.md`
```markdown
# 📦 Rootly-AI-Labs/rootly-mcp-server [🔖 PENDING/APPROVE]
🔗 https://github.com/Rootly-AI-Labs/rootly-mcp-server
🌐 https://rootly.com/ai-labs

## Meta
- **Stars:** ⭐ 40 | **Forks:** 🍴 17
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Rootly MCP server

## README (trích đầu)
```
<!-- mcp-name: com.rootly/mcp-server -->
# Rootly MCP Server

[![PyPI version](https://badge.fury.io/py/rootly-mcp-server.svg)](https://pypi.org/project/rootly-mcp-server/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/rootly-mcp-server)](https://pypi.org/project/rootly-mcp-server/)
[![Python Version](https://img.shields.io/pypi/pyversions/rootly-mcp-server.svg)](https://pypi.org/project/rootly-mcp-server/)
[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=rootly&config=eyJ1cmwiOiJodHRwczovL21jcC5yb290bHkuY29tL3NzZSIsImhlYWRlcnMiOnsiQXV0aG9yaXphdGlvbiI6IkJlYXJlciA8WU9VUl9ST09UTFlfQVBJX1RPS0VOPiJ9fQ==)

An MCP server for the [Rootly API](https://docs.rootly.com/api-reference/overview) for Cursor, Windsurf, Claude, and other MCP clients.

![Demo GIF](https://raw.githubusercontent.com/Rootly-AI-Labs/Rootly-MCP-server/refs/heads/main/rootly-mcp-server-demo.gif)

## Quick Start

Use the hosted MCP server. No local installation required.

### Hosted Transport Options

- **Streamable HTTP (recommended):** `https://mcp.rootly.com/mcp`
- **SSE (fallback):** `https://mcp.rootly.com/sse`
- **Code Mode:** `https://mcp.rootly.com/mcp-codemode`

### General Remote Setup

Default remote config (HTTP streamable):

```json
{
  "mcpServers": {
    "rootly": {
      "url": "https://mcp.rootly.com/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_ROOTLY_API_TOKEN"
      }
    }
  }
}
```

SSE fallback:

```json
{
  "mcpServers": {
    "rootly": {
      "url": "https://mcp.rootly.com/sse",
      "headers": {
        "Authorization": "Bearer YOUR_ROOTLY_API_TOKEN"
      }
    }
  }
}
```

Code Mode:

```json
{
  "mcpServers": {
    "rootly": {
      "url": "https://mcp.rootly.com/mcp-codemode",
      "headers": {
        "Authorization": "Bearer YOUR_ROOTLY_API_TOKEN"
      }
    }
  }
}
```

### Agent Setup

<details>
<summary><strong>Claude Code</strong></summary>

<br>

**Streamable HTTP**

```bash
claude mcp add --transport http rootly https://mcp.rootly.com/mcp \
  --header "Authorization: Bearer YOUR_ROOTLY_API_TOKEN"
```

Code Mode:

```bash
claude mcp add rootly-codemode --transport http https://mcp.rootly.com/mcp-codemode \
  --header "Authorization: Bearer YOUR_ROOTLY_API_TOKEN"
```

SSE fallback:

```bash
claude mcp add --transport sse rootly-sse https://mcp.rootly.com/sse \
  --header "Authorization: Bearer YOUR_ROOTLY_API_TOKEN"
```

**Manual Configuration**

Create `.mcp.json` in your project root:

```json
{
  "mcpServers": {
    "rootly": {
      "type": "sse",
      "url": "https://mcp.rootly.com/sse",
      "headers": {
        "Authorization": "Bearer YOUR_ROOTLY_API_TOKEN"
      }
    }
  }
}
```

Restart Claude Code after updating the config.

</details>

<details>
<summary><strong>Gemini CLI</strong></summary>

<br>

Install the extension:

```bash
gemini extensions install https://github.com/Rootly-AI-Labs/Rootly-MCP-server
```

Or configure manually in `~/.gemini/set
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

