---
id: loclv-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:06.101317
---

# KNOWLEDGE EXTRACT: loclv
> **Extracted on:** 2026-03-30 17:42:03
> **Source:** loclv

---

## File: `llm-lean-log.md`
```markdown
# 📦 loclv/llm-lean-log [🔖 PENDING/APPROVE]
🔗 https://github.com/loclv/llm-lean-log


## Meta
- **Stars:** ⭐ 5 | **Forks:** 🍴 1
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Logging for LLMs, but we cut the fat. A CSV-based logging format optimized for LLM token usage.

## README (trích đầu)
```
# ☘️ llm-lean-log

<p align="center">
  <img src="docs/imgs/logo.webp" alt="llm-lean-log logo" width="200">
</p>

|Package|What is it?|Version|Downloads|NPM Page|
|---|---|---|---|---|
|llm-lean-log-cli|CLI tool to save/read chat logs|![llm-lean-log-cli npm](https://img.shields.io/npm/v/llm-lean-log-cli)|![llm-lean-log-core npm](https://img.shields.io/npm/dw/llm-lean-log-core)|[npm page](https://www.npmjs.com/package/llm-lean-log-cli)|
|llm-lean-log-core|Core library to save/read chat logs|![llm-lean-log-core npm](https://img.shields.io/npm/v/llm-lean-log-core)|![l-log-vis npm](https://img.shields.io/npm/dw/l-log-vis)|[npm page](https://www.npmjs.com/package/llm-lean-log-core)|
|bl-log|CLI tool to save/read chat logs for Bun only|![bl-log npm](https://img.shields.io/npm/v/bl-log)|![bl-log npm](https://img.shields.io/npm/dw/bl-log)|[npm page](https://www.npmjs.com/package/bl-log)|
|l-log-vis|CLI tool to view chat logs|![l-log-vis npm](https://img.shields.io/npm/v/l-log-vis)|![l-log-vis npm](https://img.shields.io/npm/dw/l-log-vis)|[npm page](https://www.npmjs.com/package/l-log-vis)|
|l-log-mcp-server|MCP Server to save/read chat logs|![l-log-mcp-server npm](https://img.shields.io/npm/v/l-log-mcp-server)|![l-log-mcp-server npm](https://img.shields.io/npm/dw/l-log-mcp-server)|[npm page](https://www.npmjs.com/package/l-log-mcp-server)|

[Vietnamese](README-vi.md) | [Japanese](../../../vault/archives/archive_legacy/bat/doc/README-ja.md) | [Chinese](README-zh.md)

Work with LLMs and it's agents to write and read logs:

- Antigravity
- Cursor
- Windsurf
- Claude Code
- Opencode
- or what LLM client you want

Starting from my day-to-day coding needs, I wanted a tool to log chat sessions with AI agents so I could use them as personal reference material or as project documentation. While browsing developer groups, I also noticed a growing demand for syncing chat logs across multiple machines and keeping long-term history.

That’s how `llm-lean-log-cli` was born: a tool for reading and writing chat history optimized for minimal token usage — which means fewer tokens, and therefore lower cost.

> 📝 Logging for LLMs, but we cut the fat.

`llm-lean-log` is a format for logging that is optimized for LLMs token usage, cause and effect relationships based on CSV Data.

## 🍓 Ask AI agent (LLMs) to write a log

Before you ask AI agent (LLMs) to write a log, make sure to install `llm-lean-log-cli` CLI tool globally.

```bash
bun add -g llm-lean-log-cli
```

Ask LLMs to write a log by prompt:

> use `l-log add ./logs/chat.csv "Fix bug" --tags=bug,fix --problem="Problem description" --files="file1.ts,src/file2.ts" --tech-stack="elysia,drizzle,sqlite" --causeIds="uuid1,uuid2" --created-by-agent="agent-name"` CLI tool to save last chat logs / talk above

Or simpler for user but less efficient for LLMs:

> use l-log CLI to save chat log above

Or:

> use l-log to save

## 🍓 Ask AI agent (LLMs) to read a log

Ask LLMs to read last log only by prompt (efficient for LLMs):

> run `l-log view ./logs/example.csv --last` C
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

