---
id: kaida-palooza-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:56.985422
---

# KNOWLEDGE EXTRACT: kaida-palooza
> **Extracted on:** 2026-03-30 17:38:14
> **Source:** kaida-palooza

---

## File: `ccpoke.md`
```markdown
# kaida-palooza/ccpoke [PENDING/APPROVE]
https://github.com/kaida-palooza/ccpoke
https://kaida-palooza.github.io/ccpoke/

## Meta
- **Stars:** 95 | **Forks:** 40
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-23
- **Status in AI OS:** PENDING/APPROVE

## Description:
Bridge between AI coding agents and your phone — notifications, 2-way chat, permissions

## README (excerpt)
```
# ccpoke — AI Agent Notification Bridge

[English](../../../core/security/QUARANTINE/vetted/repos/tookie_osint/docs/readmelang/README.en.md) · [Chinese](./README.zh.md)

> 2-way interaction with Claude Code, Codex CLI, Cursor CLI and many other AI agents via Telegram — program anytime, anywhere.

---

## Problem: Solved

You're using Claude Code, Codex CLI or Cursor CLI on your computer. You go outside with your phone but don't know if the AI agent is done, want to send more requests without opening your laptop.

**ccpoke** is a 2-way bridge between AI agent and Telegram — receive notifications, send requests, answer questions, manage multiple sessions — all from your phone.

```
AI agent completes response
        ↓
  Stop Hook triggers
        ↓
  ccpoke receives event
        ↓
  Telegram notification
```

## Supported Agents

| | Claude Code | Codex CLI | Cursor CLI |
|---|---|---|---|
| Telegram notification | macOS · Linux · Windows | macOS · Linux · Windows | macOS · Linux · Windows |
| 2-way chat (Telegram ↔ Agent) | macOS · Linux | macOS · Linux | macOS · Linux |

Add new agents via Architecture plugin — contributions welcome!

## Features

- **Push notifications** — AI agent done → Telegram receives instantly, no need to check continuously, no delay
- **2-way interaction** — chat with AI agent from Telegram, view sessions, send requests, answer questions, approve permissions
- **Multi-session** — manage multiple AI agent sessions simultaneously, switch quickly, monitor in parallel

## Requirements

- **Node.js** ≥ 20
- **tmux** — needed for 2-way interaction (auto-installed on first run)
- **Telegram Bot Token** — create from [@BotFather](https://t.me/BotFather)

## Getting Started

### Method 1: npx (no installation needed)

```bash
npx -y ccpoke
```

First run → auto setup → start bot. Single command.

### Method 2: Global installation (recommended — faster startup)

```bash
npm i -g ccpoke
ccpoke
```

Installation wizard will guide you step by step:

```
┌  ccpoke setup
│
◇  Language
│  English
│
◇  Telegram Bot Token
│  your-bot-token
│
◇  Bot: @your_bot
│
◇  Scan QR or open link to connect:
│  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
│  █ ▄▄▄▄▄ █▄▄████▀ ▄██▄▄█ ▄▄▄▄▄ █
│  █ █   █ █ ▀█ ▄▄▄▄▀▀▄▀ █ █   █ █
│  █ █▄▄▄█ █▄ ▄▄▀▄▀██▄  ▄█ █▄▄▄█ █
│  █▄▄▄▄▄▄▄█▄▀▄▀▄▀ █▄▀▄█▄█▄▄▄▄▄▄▄█
│  ...
│  █▄▄▄▄▄▄▄█▄███▄█▄███▄▄▄▄███▄█▄██
│  https://t.me/your_bot?start=setup
│
◇  Waiting for you to send /start to the bot...
│
◆  Connected! User ID: 123456789
│
◇  Select AI agents (press space to select)
│  Claude Code, Codex CLI, Cursor CLI
│
◆  Config saved
◆  Hook installed for Claude Code
◆  Hook installed for Codex CLI
◆  Hook installed for Cursor CLI
◆  Chat ID registered
│
└  Setup complete!
```


## Usage

### Start bot

```bash
# npx (no installation)
npx -y ccpoke

# Or global installation
ccpoke

```

Bot running → use Claude Code / Codex CLI / Cursor CLI normally → notifications arrive at Telegram automatically.

### View multi-agent sessions

When running multiple agents in parallel, ccpoke creates tmux sessions to manage. To view:

```bash
# Regular terminal window
tmux attach

# iTerm2 (native integration)
tmux 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```