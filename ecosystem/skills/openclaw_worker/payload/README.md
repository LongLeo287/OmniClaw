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
MISSION_TIMEOUT_MS: 15 * 60 * 1000,        // 15min per task
CLOUD_BRAIN_URL: 'http://localhost:11436',  // Proxy URL
```

## 📋 Mission File Format

Filename: `mission_<project>_auto_<description>.txt`

```
mission_myapp_auto_add_dark_mode.txt
mission_webapp_auto_fix_login_bug.txt
mission_api_auto_add_rate_limiting.txt
```

Content = plain text task description. ClaudeKit `/commands` supported:
```
/plan:hard "Migrate database from MySQL to PostgreSQL"
```

## 🔧 Commands

```bash
# Start swarm
bash restore_swarm.sh

# Attach to running swarm
tmux attach -t tom_hum_brain

# Monitor logs
tail -f ~/tom_hum_cto.log

# Stop swarm
tmux kill-session -t tom_hum_brain

# Drop a task
echo "your task" > tasks/mission_project_auto_name.txt
```

## 🌍 Platform Support

| Platform | Status | Notes |
|----------|--------|-------|
| macOS (Apple Silicon) | ✅ Tested | M1/M2/M3, thermal management included |
| macOS (Intel) | ✅ Supported | |
| Linux (Ubuntu/Debian) | ✅ Supported | Server or desktop |
| Windows | ✅ Via WSL2 | Install tmux in WSL |

## 🛡️ Self-Healing

Built-in resilience:
- **Proxy health monitoring** — auto-restart if proxy goes down
- **Model failover** — switches models on quota exhaustion
- **Thermal management** — throttles on Apple Silicon overheating
- **Timeout recovery** — kills stuck missions, moves to next task

## 📜 License

MIT — Use it, fork it, build empires with it. 🦞