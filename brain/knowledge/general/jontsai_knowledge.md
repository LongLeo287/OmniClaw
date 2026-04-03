---
id: jontsai-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:56.229264
---

# KNOWLEDGE EXTRACT: jontsai
> **Extracted on:** 2026-03-30 17:38:12
> **Source:** jontsai

---

## File: `openclaw-command-center.md`
```markdown
# 📦 jontsai/openclaw-command-center [🔖 PENDING/APPROVE]
🔗 https://github.com/jontsai/openclaw-command-center
🌐 https://clawhub.ai/jontsai/command-center

## Meta
- **Stars:** ⭐ 179 | **Forks:** 🍴 33
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
🤖 AI assistant command and control dashboard — Spawn more Overlords!

## README (trích đầu)
```
# 🦞 OpenClaw Command Center

English | [简体中文](README.zh-CN.md)

<div align="center">

**Mission control for your AI agents**

[![CI](https://github.com/jontsai/openclaw-command-center/actions/workflows/ci.yml/badge.svg)](https://github.com/jontsai/openclaw-command-center/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Node](https://img.shields.io/badge/node-%3E%3D18-brightgreen)](https://nodejs.org)
[![ClawHub](https://img.shields.io/badge/ClawHub-command--center-blue)](https://www.clawhub.ai/jontsai/command-center)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/jontsai/openclaw-command-center/pulls)

[Features](#features) • [Quick Start](#quick-start) • [Security](#-security) • [Configuration](#configuration)

</div>

---

## Why Command Center?

Your AI agents are running 24/7. You need to know what they're doing.

Command Center gives you **real-time visibility** into your OpenClaw deployment — sessions, costs, system health, scheduled tasks — all in one secure dashboard.

### ⚡ Fast

- **Single API call** — unified state endpoint, not 16+ separate requests
- **2-second updates** — real-time SSE push, not polling
- **5-second cache** — backend stays responsive under load
- **Instant startup** — no build step, no compilation

### 🪶 Lightweight

- **Zero dependencies** for users — just Node.js
- **~200KB total** — dashboard + server
- **No webpack/vite/bundler** — runs directly
- **No React/Vue/Angular** — vanilla JS, works everywhere

### 📱 Responsive

- **Desktop & mobile** — works on any screen size
- **Dark mode** — easy on the eyes, Starcraft-inspired
- **Live updates** — no manual refresh needed
- **Offline-friendly** — graceful degradation

### 🔧 Modern

- **ES Modules** — clean component architecture
- **SSE streaming** — efficient real-time updates
- **REST API** — integrate with your tools
- **TypeScript-ready** — JSDoc types included

### 🔒 Security (Most Important)

Command Center takes security seriously:

| Feature                  | Description                                         |
| ------------------------ | --------------------------------------------------- |
| **Auth Modes**           | Token, Tailscale, Cloudflare Access, IP allowlist   |
| **No external calls**    | Dashboard runs 100% locally — no telemetry, no CDNs |
| **Localhost default**    | Binds to `127.0.0.1` by default                     |
| **Read-only by default** | View your agents without exposing control           |
| **No secrets in UI**     | API keys, tokens never displayed                    |
| **Audit logging**        | Know who accessed what, when                        |

```bash
# Secure deployment example (Tailscale)
DASHBOARD_AUTH_MODE=tailscale node lib/server.js
# Only users on your Tailscale network can access
```

---

## Features

| Feature                    | Description                                 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

