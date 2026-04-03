---
id: longtho638-jpg-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:06.161256
---

# KNOWLEDGE EXTRACT: longtho638-jpg
> **Extracted on:** 2026-03-30 17:42:03
> **Source:** longtho638-jpg

---

## File: `openclaw-worker.md`
```markdown
# 📦 longtho638-jpg/openclaw-worker [🔖 PENDING/APPROVE]
🔗 https://github.com/longtho638-jpg/openclaw-worker


## Meta
- **Stars:** ⭐ 41 | **Forks:** 🍴 11
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
🦞 Autonomous AI Swarm Engine — Drop a file, watch 3 AI agents execute in parallel. Built on Claude Code CLI + tmux.

## README (trích đầu)
```
# 🦞 OpenClaw Worker — Autonomous AI Swarm Engine

> **Drop a file. Watch AI agents execute.** No manual intervention needed.

OpenClaw Worker turns Claude Code CLI into an autonomous swarm — 3 AI workers running in parallel, processing tasks from a simple file-drop queue. Built for developers who want AI agents that **just work**.

## ⚡ 30-Second Quick Start

```bash
# Prerequisites: Node.js 18+, tmux, Claude CLI
brew install tmux                              # macOS
# sudo apt install tmux                        # Linux

npm install -g @anthropic-ai/claude-code       # Claude CLI

# Clone & Start
git clone https://github.com/longtho638-jpg/openclaw-worker.git
cd openclaw-worker && npm install

# Launch the swarm (4 tmux panes inside your terminal)
bash restore_swarm.sh
```

You'll see 4 panes:
```
┌──────────────────┬──────────────────┐
│ P0: Mission Log  │ P1: AI Worker 1  │
│ (real-time feed) │ (Claude CLI TUI) │
├──────────────────┼──────────────────┤
│ P2: AI Worker 2  │ P3: AI Worker 3  │
│ (Claude CLI TUI) │ (Claude CLI TUI) │
└──────────────────┴──────────────────┘
```

## 🚀 How It Works

**Drop a mission file → AI workers auto-execute → Results logged.**

```bash
# Create a task (that's it!)
echo "Refactor the auth module to use JWT tokens" > tasks/mission_myapp_auto_auth_refactor.txt
```

The task-watcher daemon:
1. **Detects** new files in `tasks/` directory
2. **Dispatches** to the next available worker (round-robin)
3. **Monitors** execution (busy/idle/timeout detection)
4. **Archives** completed missions to `tasks/processed/`

## 📁 Architecture

```
openclaw-worker/
├── task-watcher.js              # 🧠 Main orchestrator
├── config.js                    # ⚙️ Configuration
├── restore_swarm.sh             # 🦞 One-command launcher
├── lib/
│   ├── brain-tmux.js            # Tmux interactive mode (default)
│   ├── brain-headless-per-mission.js  # Headless claude -p mode
│   ├── brain-vscode-terminal.js # VS Code terminal mode
│   ├── task-queue.js            # File watcher + dispatch queue
│   ├── mission-dispatcher.js    # Prompt builder + routing
│   ├── self-healer.js           # Auto-recovery + health checks
│   └── m1-cooling-daemon.js     # Thermal throttling (Apple Silicon)
└── tasks/                       # Drop mission files here
    └── processed/               # Completed missions archived here
```

## 🧠 Three Brain Modes

| Mode | File | Best For |
|------|------|----------|
| **Tmux Interactive** | `brain-tmux.js` | Visual — see ClaudeKit TUI |
| **Headless** | `brain-headless-per-mission.js` | Servers — no display needed |
| **VS Code Terminal** | `brain-vscode-terminal.js` | VS Code / Antigravity users |

Switch in `task-watcher.js` line 40:
```javascript
const { spawnBrain, killBrain, log } = require('./lib/brain-tmux');
```

## ⚙️ Configuration

Edit `config.js`:

```javascript
MODEL_NAME: 'claude-3-5-sonnet-20241022',  // AI model
MAX_CONCURRENT_MISSIONS: 3,                 // Parallel workers
MISSION_TIMEOUT_MS: 15 * 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

