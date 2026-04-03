---
id: letta-ai-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:03.952097
---

# KNOWLEDGE EXTRACT: letta-ai
> **Extracted on:** 2026-03-30 17:40:16
> **Source:** letta-ai

---

## File: `claude-subconscious.md`
```markdown
# 📦 letta-ai/claude-subconscious [🔖 PENDING/APPROVE]
🔗 https://github.com/letta-ai/claude-subconscious


## Meta
- **Stars:** ⭐ 1743 | **Forks:** 🍴 127
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Give Claude Code a subconscious

## README (trích đầu)
```
# Claude Subconscious

A background agent that whispers to Claude Code. A [Letta](https://letta.com) agent that watches your sessions, reads your files, builds up memory over time, and whispers guidance back.

> [!IMPORTANT]
> Claude Subconscious is an experimental way to extend Claude Code (a closed source / black box agent) with the power of Letta's memory system, tool access, and context engineering.
>
> If you're looking for a coding agent that's memory-first, model agnostic, and fully open source, we recommend using [**Letta Code**](https://github.com/letta-ai/letta-code).

![evil claude](assets/evil-claude.jpeg)

## What Is This?

Claude Code forgets everything between sessions. Claude Subconscious is a second agent running underneath — watching, learning, and whispering back:

- **Watches** every Claude Code session transcript
- **Reads your codebase** — explores files with Read, Grep, and Glob while processing transcripts
- **Remembers** across sessions, projects, and time
- **Whispers guidance** — surfaces context, patterns, and reminders before each prompt
- **Never blocks** — runs in the background via the [Letta Code SDK](https://docs.letta.com/letta-code/sdk/)

Not just a memory layer — a background agent with real tool access that gets smarter the more you use it.

Using Letta's [Conversations](https://docs.letta.com/guides/agents/conversations/) feature, a single agent can serve multiple Claude Code sessions in parallel with shared memory across all of them.

## How It Works

After each response, the transcript is sent to a Letta agent via the Letta Code SDK. The agent reads files, searches the web, updates its memory — then whispers back before the next prompt. Nothing is written to CLAUDE.md.

```
┌─────────────┐          ┌──────────────────────────┐
│ Claude Code │◄────────►│ Letta Agent (background)  │
└─────────────┘          │                          │
       │                 │  Tools: Read, Grep, Glob │
       │                 │  Memory: persistent       │
       │                 │  Web: search, fetch       │
       │                 └──────────────────────────┘
       │                        │
       │   Session Start        │
       ├───────────────────────►│ New session notification
       │                        │
       │   Before each prompt   │
       │◄───────────────────────┤ Whispers guidance → stdout
       │                        │
       │   Before each tool use │
       │◄───────────────────────┤ Mid-workflow updates → stdout
       │                        │
       │   After each response  │
       ├───────────────────────►│ Transcript → SDK session (async)
       │                        │  ↳ Reads files, updates memory
```

## Installation

Install from GitHub:

```
/plugin marketplace add letta-ai/claude-subconscious
/plugin install claude-subconscious@claude-subconscious
```

### Updating

```
/plugin marketplace update
/plugin update claude-subconscious@claude-subconscious
```

### Install from Sou
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

