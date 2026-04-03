---
id: nghyane-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:11.850589
---

# KNOWLEDGE EXTRACT: nghyane
> **Extracted on:** 2026-03-30 17:49:11
> **Source:** nghyane

---

## File: `ampcode-connector.md`
```markdown
# 📦 nghyane/ampcode-connector [🔖 PENDING/APPROVE]
🔗 https://github.com/nghyane/ampcode-connector


## Meta
- **Stars:** ⭐ 17 | **Forks:** 🍴 5
- **Language:** TypeScript | **License:** Unknown
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Lightweight proxy that routes AmpCode requests through local OAuth credentials (Claude Code, Codex CLI, Gemini CLI, Antigravity)

## README (trích đầu)
```
# ampcode-connector

Route [AmpCode](https://ampcode.com) through your existing Claude Code, Codex CLI & Gemini CLI subscriptions.

```bash
bunx ampcode-connector setup    # point AmpCode → proxy
bunx ampcode-connector login    # authenticate providers
bunx ampcode-connector          # start
```

Requires [Bun](https://bun.sh) 1.3+. Config at `./config.yaml` or `~/.config/ampcode-connector/config.yaml` — see [`config.example.yaml`](config.example.yaml).

`setup` writes `amp.url` to Amp's canonical settings file (`~/.config/amp/settings.json`, or `AMP_SETTINGS_FILE` if set). Amp tokens are stored in `~/.local/share/amp/secrets.json`.

## License

[MIT](LICENSE)

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `llm-mux.md`
```markdown
# 📦 nghyane/llm-mux [🔖 PENDING/APPROVE]
🔗 https://github.com/nghyane/llm-mux
🌐 https://nghyane.github.io/llm-mux/

## Meta
- **Stars:** ⭐ 331 | **Forks:** 🍴 92
- **Language:** Go | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
AI Gateway: Claude Pro, Copilot, Gemini subscriptions → OpenAI/Anthropic/Gemini APIs. No API keys needed.

## README (trích đầu)
```
# llm-mux

**AI Gateway for Subscription-Based LLMs**

[![GitHub release](https://img.shields.io/github/v/release/nghyane/llm-mux)](https://github.com/nghyane/llm-mux/releases)
[![GitHub stars](https://img.shields.io/github/stars/nghyane/llm-mux)](https://github.com/nghyane/llm-mux/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docker](https://img.shields.io/docker/pulls/nghyane/llm-mux)](https://hub.docker.com/r/nghyane/llm-mux)
[![Docs](https://img.shields.io/badge/docs-online-blue)](https://nghyane.github.io/llm-mux/)
[![Discord](https://img.shields.io/discord/1326216179697410129?color=5865F2&logo=discord&logoColor=white)](https://discord.gg/86nFZUh4a9)

---

## 🎁 MiniMax Coding Plan - New Year Mega Offer!

**🔥 GET 10% OFF INSTANTLY - No voucher needed!**

Use the link below to get an immediate 10% discount when signing up for MiniMax Coding Plan:

👉 **https://platform.minimax.io/subscribe/coding-plan?code=EljrpDLxkH&source=link**

> 💡 **Why MiniMax?** Google Antigravity Claude quotas have been heavily throttled. MiniMax offers nearly identical quality at a lower cost with faster response times!

---

Turn your Claude Pro, GitHub Copilot, and Gemini subscriptions into standard LLM APIs. No API keys needed.

## Features

- **Multi-Provider** — Claude, Copilot, Gemini, Codex, Qwen, Kiro, iFlow, Cline, and more
- **Multi-Format** — OpenAI, Anthropic, Gemini, Ollama compatible endpoints
- **Multi-Account** — Load balance across accounts, auto-retry on quota limits
- **Zero Config** — OAuth login, no API keys required
- **Management API** — Usage statistics, auth management, runtime configuration
- **Extended Thinking** — Support for Claude's extended thinking mode
- **AMP CLI Compatible** — Drop-in replacement for Amp CLI with model mapping

## Quick Start

```bash
# Install
curl -fsSL https://raw.githubusercontent.com/nghyane/llm-mux/main/install.sh | bash

# Login to a provider
llm-mux login antigravity   # Google Gemini
llm-mux login claude        # Claude Pro/Max
llm-mux login copilot       # GitHub Copilot

# Start server
llm-mux

# Test
curl http://localhost:8317/v1/models
```

## Usage

```
Base URL: http://localhost:8317
API Key:  unused (or any string)
```

```bash
# OpenAI format
curl http://localhost:8317/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "gemini-2.5-pro", "messages": [{"role": "user", "content": "Hello!"}]}'
```

Works with: **Cursor, Aider, Claude Code, Cline, Continue, OpenCode, LangChain, Open WebUI**, and any OpenAI/Anthropic/Gemini compatible tool.

## Documentation

📖 **https://nghyane.github.io/llm-mux/**

- [Installation](https://nghyane.github.io/llm-mux/#/installation) — Install, update, uninstall
- [Providers](https://nghyane.github.io/llm-mux/#/providers) — All providers and login commands
- [Configuration](https://nghyane.github.io/llm-mux/#/configuration) — Config file reference
- [Integrations](https://
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

