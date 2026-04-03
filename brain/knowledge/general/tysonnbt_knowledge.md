---
id: tysonnbt-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:24.313401
---

# KNOWLEDGE EXTRACT: tysonnbt
> **Extracted on:** 2026-03-30 17:56:43
> **Source:** tysonnbt

---

## File: `Antigravity-Deck.md`
```markdown
# 📦 tysonnbt/Antigravity-Deck [🔖 PENDING/APPROVE]
🔗 https://github.com/tysonnbt/Antigravity-Deck


## Meta
- **Stars:** ⭐ 95 | **Forks:** 🍴 33
- **Language:** TypeScript | **License:** Unknown
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Remote control for Antigravity — manage AI conversations, workspaces, and agents from any device. One command to set up, one URL to access.

## README (trích đầu)
```
# 🔮 Antigravity Deck

Full-featured workspace dashboard for [Antigravity](https://codeium.com/antigravity). View, send, and manage AI conversations across multiple workspaces — with resource monitoring, source control, headless IDE, agent bridge, and remote access.

---

## 📸 Screenshots

| Dashboard | Workspace Conversations |
|:-:|:-:|
| ![Dashboard](docs/images/dashboard-desktop.png) | ![Workspace](docs/images/workspace-conversations.png) |

| Conversation View | Mobile |
|:-:|:-:|
| ![Conversation](docs/images/conversation-desktop.png) | ![Mobile](docs/images/conversation-mobile.png) |

---

## ✨ Feature Highlights

### 💬 Chat & Conversations
- **Full conversation history** — Bypasses the 598-step JSON API limit via hybrid JSON + binary protobuf fetching
- **Real-time updates** — WebSocket-powered polling with adaptive rates (1s active → 5s idle)
- **Send messages** — Compose and send directly to Antigravity cascades from the web UI
- **Image upload** — Attach images via paste or file picker for multimodal AI interactions
- **Model selection** — Choose from available AI models (fetched live from LS API)
- **Create & delete conversations** — Full CRUD for cascade conversations
- **All step types** — User input, agent responses, tool calls, code actions, commands, browser subagent, generated images, and 17+ more
- **Smart rendering** — Markdown with syntax highlighting, collapsible thinking blocks, step type tags
- **Workflow autocomplete** — Suggests available workflow commands while typing

### 🖥️ Multi-Workspace Management
- **Auto-detection** — Discovers all running LS processes, ports, and CSRF tokens automatically (Windows/macOS/Linux)
- **Workspace switching** — Switch between multiple Antigravity workspaces seamlessly
- **Workspace creation** — Launch new Antigravity IDE instances with auto-binding
- **Workspace folders** — Configure a default root directory; existing subfolders appear as available workspaces
- **Open mode dialog** — Click any available workspace to choose: **Open with IDE** or **Open Headless**
- **Auto-rescan** — Detects new LS instances every 10 seconds

### 🧠 Headless Language Server
Run Antigravity LS instances **without the IDE UI** — directly from the Deck.

- **Full lifecycle management** — Launch, kill, and list headless instances
- **Auto-auth** — Reuses extension server (port + CSRF) from a running IDE for cloud API access
- **HL badge** — Visual indicators (Terminal icon + green "HL" badge) in sidebar and resource monitor
- **Kill from dashboard** — Terminate headless instances via styled AlertDialog in Resource Monitor
- **Workspace binding** — Proper `AddTrackedWorkspace` + `GetWorkspaceInfos` for correct routing
- **Mock parent pipe** — Keeps LS alive and allows port binding
- **Protobuf metadata** — Binary encoding for LS stdin handshake

### 📊 Resource Monitor
Real-time system and per-workspace resource dashboard.

- **System overview** — CPU, RAM, Disk in animated donut charts with tooltips
- **Per-wor
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

