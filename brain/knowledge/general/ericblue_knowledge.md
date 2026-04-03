---
id: ericblue-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:21.933321
---

# KNOWLEDGE EXTRACT: ericblue
> **Extracted on:** 2026-03-30 17:36:11
> **Source:** ericblue

---

## File: `claude-openclaw-bridge.md`
```markdown
# 📦 ericblue/claude-openclaw-bridge [🔖 PENDING/APPROVE]
🔗 https://github.com/ericblue/claude-openclaw-bridge


## Meta
- **Stars:** ⭐ 7 | **Forks:** 🍴 3
- **Language:** Makefile | **License:** Unknown
- **Last updated:** 2026-03-15
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Claude Code skill for relaying questions and tasks to an OpenClaw agent — supports one-shot queries and persistent relay mode

## README (trích đầu)
```
# claude-openclaw-bridge

A Claude Code skill that bridges to an OpenClaw agent via its OpenAI-compatible API.

## What it does

Relays user requests to a remote OpenClaw instance and returns responses verbatim. Any capabilities, skills, or tools available on the OpenClaw agent become accessible from within Claude Code.

## Triggers

- "Ask OpenClaw ..."
- "OpenClaw mode on" / "OpenClaw mode off" (relay mode toggle)
- `/openclaw-bridge`

## Environment Variables

| Variable | Required | Example |
|----------|----------|---------|
| `OPENCLAW_BASE_URL` | yes | `http://127.0.0.1:18789/v1` |
| `OPENCLAW_MODEL` | yes | `openclaw:main` |
| `OPENCLAW_API_KEY` | yes | `sk-your-key` |
| `OPENCLAW_ASSISTANT_NAME` | no | `YOUR_ASSISTANT_NAME` (defaults to `OpenClaw`) |

Set these in your shell profile or `.env` before launching Claude Code.

## Installation

```bash
make install
```

This copies `SKILL.md` to `~/.claude/skills/openclaw-bridge/`.

To remove:

```bash
make uninstall
```

## Relay Mode

Say "OpenClaw mode on" to enter relay mode -- all subsequent messages are forwarded to the OpenClaw agent automatically. Say "OpenClaw mode off" to return to normal Claude Code behavior. This is session-scoped and does not persist.

## Enabling OpenAI-Compatible Endpoints

The bridge communicates with OpenClaw using the **OpenAI Chat Completions API** format. Any OpenClaw instance that exposes an OpenAI-compatible `/v1/chat/completions` endpoint will work.

### What the bridge expects

- **POST** `${OPENCLAW_BASE_URL}/chat/completions`
- Standard request body: `{ "model": "<model>", "messages": [{ "role": "user", "content": "..." }] }`
- Bearer token authentication via `Authorization: Bearer ${OPENCLAW_API_KEY}`
- Standard response: `{ "choices": [{ "message": { "content": "..." } }] }`

### Configuring your OpenClaw instance

1. **Enable the OpenAI-compatible server** in your OpenClaw configuration. The exact steps depend on your OpenClaw version, but generally you need to start the API server with an OpenAI-compatible endpoint enabled (commonly on a local port like `18789`).
2. **Set a model identifier** that your OpenClaw instance recognizes (e.g. `openclaw:main`).
3. **Generate or configure an API key** for authentication. Even for local-only access, an API key is recommended.
4. **Verify the endpoint** is reachable:

```bash
curl -s "${OPENCLAW_BASE_URL}/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${OPENCLAW_API_KEY}" \
  -d '{"model": "'"${OPENCLAW_MODEL}"'", "messages": [{"role": "user", "content": "hello"}]}' \
  | jq .choices[0].message.content
```

If you get a response, the bridge is ready to use.

## Security Considerations

OpenClaw is often sandboxed and isolated from your main environment, and may have access to sensitive or personal data that you would not normally expose to Claude Code. The bridge creates a path between these two worlds, so it is important to be deliberate about when and how it is ac
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `memspan.md`
```markdown
# 📦 ericblue/memspan [🔖 PENDING/APPROVE]
🔗 https://github.com/ericblue/memspan


## Meta
- **Stars:** ⭐ 11 | **Forks:** 🍴 3
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-15
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A persistent span of identity, memory, and conversation for LLMs and agents

## README (trích đầu)
```
# Memspan.ai

<div align="center">
  <img src="brain/knowledge/docs_legacy/images/memspan_logo.png" alt="memspan logo" width="600">
</div>


> A persistent span of identity, memory, and conversation for LLMs and agents

**Website:** [https://memspan.ai](https://memspan.ai)

**memspan** is a file-system based memory archive system that helps you extract, organize, and load your personal identity, saved memories, and conversation history into Claude Code and other LLM interfaces. It provides a portable, tool-agnostic approach to maintaining continuity across AI assistant sessions.

## Overview

Memspan addresses a fundamental challenge: **LLMs don't remember across sessions**. While platforms like ChatGPT offer memory features, they're platform-locked and don't easily transfer to other tools like Claude Code. memspan bridges this gap by:

- **Extracting** your identity, memories, and conversation history from platforms like OpenAI ChatGPT
- **Organizing** this data into a structured, portable format
- **Loading** it dynamically into Claude Code sessions when needed

The system is designed to be:
- **File-based**: No databases, no servers—just files you control
- **Portable**: Works across different LLM tools and platforms
- **Selective**: Load only what you need for each session
- **Independent**: Doesn't interfere with Claude Code's own memory system

## Current State

### What Works Today

memspan currently provides:

1. **Identity Extraction**: Scripts and prompts to extract your personal identity from ChatGPT conversations
2. **Memory Export**: Tools to export and structure ChatGPT saved memories
3. **Project Conversations**: Scripts to correlate ChatGPT Projects with conversation history (the default export doesn't include project metadata)
4. **Context Loading**: A wrapper script (`cc-memspan`) to dynamically load identity, memories, and project context into Claude Code sessions

### Architecture

The project follows a three-tier memory model:

1. **Core Identity** (~2-4KB): Always-available personal context
2. **Project/Framework Memory** (~10-50KB per domain): Session-selectable deep context
3. **Historical Archive**: Indexed, retrieved on-demand

### Memory Architecture

```mermaid
graph TB
    subgraph ChatGPT["ChatGPT Platform"]
        CH_ID[Identity Data]
        CH_MEM[Saved Memories]
        CH_CONV[Conversations & Projects]
    end
    
    subgraph Export["Export Process"]
        EXP_ID[Identity Extraction<br/>Manual Prompt]
        EXP_MEM[Memory Export<br/>Settings UI or Prompt]
        EXP_CONV[Conversation Export<br/>Python Scripts]
    end
    
    subgraph Memspan["memspan File System"]
        FS_ID[memory/identity/<br/>core-identity.json]
        FS_MEM[memory/chatgpt/<br/>memories_export.md]
        FS_PROJ[memory/projects/<br/>projects.json<br/>context.md]
        FS_CLAUDE[memory/claude/<br/>index.json<br/>entries/*.md]
    end
    
    subgraph CC["cc-memspan Script"]
        CC_LOAD[Load Context Files]
        CC_COMBINE[Combine into<br/>Sy
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

