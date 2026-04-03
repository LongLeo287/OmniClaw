---
id: tirth8205-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:22.457186
---

# KNOWLEDGE EXTRACT: tirth8205
> **Extracted on:** 2026-03-30 17:54:18
> **Source:** tirth8205

---

## File: `code-review-graph.md`
```markdown
# 📦 tirth8205/code-review-graph [🔖 PENDING/APPROVE]
🔗 https://github.com/tirth8205/code-review-graph


## Meta
- **Stars:** ⭐ 3648 | **Forks:** 🍴 323
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Local knowledge graph for Claude Code. Builds a persistent map of your codebase so Claude reads only what matters — 6.8× fewer tokens on reviews and up to 49× on daily coding tasks.

## README (trích đầu)
```
<h1 align="center">code-review-graph</h1>

<p align="center">
  <strong>Stop burning tokens. Start reviewing smarter.</strong>
</p>

<p align="center">
  <a href="https://github.com/tirth8205/code-review-graph/stargazers"><img src="https://img.shields.io/github/stars/tirth8205/code-review-graph?style=flat-square" alt="Stars"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="MIT Licence"></a>
  <a href="https://github.com/tirth8205/code-review-graph/actions/workflows/ci.yml"><img src="https://github.com/tirth8205/code-review-graph/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.10%2B-blue.svg?style=flat-square" alt="Python 3.10+"></a>
  <a href="https://modelcontextprotocol.io/"><img src="https://img.shields.io/badge/MCP-compatible-green.svg?style=flat-square" alt="MCP"></a>
  <a href="#"><img src="https://img.shields.io/badge/version-2.0.0-purple.svg?style=flat-square" alt="v2.0.0"></a>
</p>

<br>

Claude Code re-reads your entire codebase on every task. `code-review-graph` fixes that. It builds a structural map of your code with [Tree-sitter](https://tree-sitter.github.io/tree-sitter/), tracks changes incrementally, and gives Claude precise context so it reads only what matters.

<p align="center">
  <img src="diagrams/diagram1_before_vs_after.png" alt="The Token Problem: 8.2x average token reduction across 6 real repositories" width="85%" />
</p>

---

## Quick Start

```bash
pip install code-review-graph
code-review-graph install          # auto-detects and configures all supported platforms
code-review-graph build            # parse your codebase
```

One command sets up everything. `install` detects which AI coding tools you have and writes the correct MCP configuration for each one. Restart your editor/tool after installing.

To target a specific platform:

```bash
code-review-graph install --platform cursor      # configure only Cursor
code-review-graph install --platform claude-code  # configure only Claude Code
```

Requires Python 3.10+ and [uv](https://docs.astral.sh/uv/).

### Supported Platforms

| Platform | Config file | Auto-detected |
|----------|-------------|:---:|
| **Claude Code** | `.mcp.json` | Yes |
| **Cursor** | `.cursor/mcp.json` | Yes |
| **Windsurf** | `.windsurf/mcp.json` | Yes |
| **Zed** | `.zed/settings.json` | Yes |
| **Continue** | `.continue/config.json` | Yes |
| **OpenCode** | `.opencode/config.json` | Yes |

Then open your project and ask your AI assistant:

```
Build the code review graph for this project
```

The initial build takes ~10 seconds for a 500-file project. After that, the graph updates automatically on every file edit and git commit.

---

## How It Works

Your repository is parsed into an AST with Tree-sitter, stored as a graph of nodes (functions, classes, imports) and edges (calls, inheritance, test coverage), then quer
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

