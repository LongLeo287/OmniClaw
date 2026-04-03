---
id: tanviet12-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:21.070011
---

# KNOWLEDGE EXTRACT: tanviet12
> **Extracted on:** 2026-03-30 17:54:15
> **Source:** tanviet12

---

## File: `chat-quality-agent.md`
```markdown
# 📦 tanviet12/chat-quality-agent [🔖 PENDING/APPROVE]
🔗 https://github.com/tanviet12/chat-quality-agent
🌐 https://tanviet12.github.io/chat-quality-agent/

## Meta
- **Stars:** ⭐ 222 | **Forks:** 🍴 211
- **Language:** Go | **License:** MIT
- **Last updated:** 2026-03-26
- **Status in AI OS:** 🔖 PENDING/APPROVE

## Description:
Chat Quality Agent - An agent for analyzing customer service quality using AI

## README (excerpt)
'''
# Chat Quality Agent (CQA)

[![Docker Hub](https://img.shields.io/docker/v/buitanviet/chat-quality-agent?label=Docker%20Hub&sort=semver)](https://hub.docker.com/r/buitanviet/chat-quality-agent)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An AI-powered system for analyzing customer service quality. It automatically syncs messages from Zalo OA and Facebook Messenger, uses AI (Claude/Gemini) to evaluate customer service quality, and sends alerts via Telegram/Email.

📖 **Detailed User Guide: [https://tanviet12.github.io/chat-quality-agent/](https://tanviet12.github.io/chat-quality-agent/)**

![Dashboard](https://raw.githubusercontent.com/tanviet12/chat-quality-agent/main/docs/public/screenshots/dashboard.png)

## Features

- **Sync messages** from Zalo OA and Facebook Messenger
- **Evaluate customer service quality** using AI (Claude or Gemini) — Pass/Fail, score 0-100, detailed feedback
- **Classify chats** by custom topics (complaints, suggestions, price inquiries...)
- **Automatic alerts** via Telegram and Email
- **Batch AI mode** — group multiple chats per AI call to save costs
- **Dashboard** with charts, statistics, and recent alerts
- **Multi-tenant** — multiple companies on one system, with Owner > Admin > Member roles
- **MCP integration** for Claude Web/Desktop
- **Automatic SSL** via Let's Encrypt (optional)

## Quick Installation

### Method 1: Automatic Installation (recommended)

'''bash
curl -s https://raw.githubusercontent.com/tanviet12/chat-quality-agent/main/install.sh | sudo bash
'''

The script automatically installs Docker, generates random secrets, pulls images, and starts the services.

### Method 2: Build from source

'''bash
git clone https://github.com/tanviet12/chat-quality-agent.git
cd chat-quality-agent
cp .env.example .env
# Edit .env
docker compose up -d --build
'''

Access: **http://your-server-ip** (or `http://localhost` if installed locally) — The first time, a Setup page will appear to create an admin account.

### Enable SSL (optional)

Add to the `.env` file:
'''
LEGO_DOMAIN=cqa.yourdomain.com
LEGO_EMAIL=admin@yourdomain.com
'''

Point the DNS A record to the server IP, then restart:
'''bash
docker compose restart nginx
'''

SSL will be automatically generated and renewed via Let's Encrypt.

## Technology

| Component | Technology |
|-----------|-----------|
| Backend | Go 1.25+ / Gin |
| Frontend | Vue 3 + Vuetify 4 + Vite |
| Database | MySQL 8.0 |
| AI | Claude (Anthropic) / Gemini (Google) |
| Reverse Proxy | Nginx + Let's Encrypt (Lego) |
| Deploy | Docker Compose |

## Architecture

'''
                    ┌──────────────┐
  Internet ────────>│    Nginx     │ Port 80/443
                    │  (SSL + RP)  │
                    └──────┬───────┘
                           │
                    ┌──────┴───────┐
                    │   CQA App    │ Port 8080 (internal)
                    │ Go + Vue SPA │
                    └──────┬───────┘
                           │
                    ┌──────┴───────┐
                    │   MySQL 8.0  │ Port 3306 (internal)
                    └──────────────┘
'''

## Project Structure
'''
---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
'''
