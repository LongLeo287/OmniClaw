---
id: openclaw-worker-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:15.969159
---

# KNOWLEDGE EXTRACT: openclaw-worker
> **Extracted on:** 2026-03-30 13:17:04
> **Source:** openclaw-worker

---

## File: `.gitignore`
```
node_modules/
.claude/
.serena/
*.log
tasks/processed/*
!tasks/processed/.gitkeep
.env
.env.*
tom_hum_*.log
/tmp/
```

## File: `COMMUNITY_GUIDE_VI.md`
```markdown
# Biến Claude Code CLI thành đội quân AI tự hành — OpenClaw Worker

> *Thay vì gõ từng lệnh, drop 1 file text — 3 AI agent tự chạy song song.*

---

## Problem:

Bạn có 10 task cần làm. Mở Claude Code, gõ task 1, đợi xong, gõ task 2... Mỗi task 15 phút. 10 task = **2.5 tiếng ngồi chờ**.

## Solution: OpenClaw Worker

**Drop file vào thư mục → AI tự nhận → tự chạy → tự archive.**

Không cần ngồi canh. Không cần copy-paste prompt. 3 worker chạy song song, pipeline tự động từ A đến Z.

## Cách hoạt động

```
Bạn tạo file: tasks/mission_myapp_auto_fix_bug.txt  
  → Task Watcher detect (< 5 giây)
  → Dispatch vào Worker trống (round-robin)
  → Claude CLI thực thi với full ClaudeKit TUI
  → Xong → archive vào tasks/processed/
  → Worker sẵn sàng nhận task tiếp
```

## Setup — 3 phút

**Installation: prerequisite:**

```bash
# macOS
brew install tmux
npm install -g @anthropic-ai/claude-code

# Linux (Ubuntu/Debian)
sudo apt install tmux
npm install -g @anthropic-ai/claude-code
```

**Clone và chạy:**

```bash
git clone https://github.com/longtho638-jpg/openclaw-worker.git
cd openclaw-worker
npm install
bash restore_swarm.sh
```

Bạn sẽ thấy 4 ô tmux chia đều:

```
┌─────────────────┬─────────────────┐
│ P0: Log viewer  │ P1: AI Worker 1 │
├─────────────────┼─────────────────┤
│ P2: AI Worker 2 │ P3: AI Worker 3 │
└─────────────────┴─────────────────┘
```

- **P0**: Log real-time — xem task nào đang chạy, hoàn thành, lỗi
- **P1-P3**: Claude CLI interactive — xem AI agent đang code real-time

## Giao việc

Tạo file text trong `tasks/`:

```bash
echo "Add dark mode toggle to the header component" > tasks/mission_webapp_auto_dark_mode.txt
```

Hoặc dùng ClaudeKit command:

```bash
echo '/plan:hard "Migrate auth from session-based to JWT"' > tasks/mission_api_auto_jwt.txt
```

Đặt tên file theo format: `mission_<project>_auto_<mô-tả>.txt`

## 3 chế độ chạy

| Chế độ | Khi nào dùng |
|--------|-------------|
| **Tmux** (mặc định) | Muốn xem 4 ô, theo dõi AI agent chạy real-time |
| **Headless** | Chạy trên server, không cần màn hình |
| **VS Code Terminal** | Dùng trong VS Code / Antigravity |

Đổi chế độ — sửa 1 dòng trong `task-watcher.js`:

```javascript
// Tmux (mặc định — 4 ô đẹp)
const { spawnBrain } = require('./lib/brain-tmux');

// Headless (server)
const { spawnBrain } = require('./lib/brain-headless-per-mission');
```

## Tự phục hồi

OpenClaw không chỉ dispatch — nó **tự chữa lành**:

- Worker bị treo → timeout → kill → chuyển task sang worker khác
- Proxy mất kết nối → tự reconnect
- Model hết quota → tự chuyển model dự phòng
- MacBook nóng → throttle tự động (Apple Silicon)

## Configuration:

Mở `config.js`:

```javascript
MODEL_NAME: 'claude-3-5-sonnet-20241022',   // Model AI
MAX_CONCURRENT_MISSIONS: 3,                  // Số worker song song
MISSION_TIMEOUT_MS: 15 * 60 * 1000,         // Timeout mỗi task
```

## Tương thích

✅ macOS (M1/M2/M3/Intel)  
✅ Linux (Ubuntu, Debian, CentOS)  
✅ Windows (qua WSL2)

## Tóm gọn

| Trước | Sau |
|-------|-----|
| Gõ task thủ công | Drop file |
| 1 task 1 lúc | 3 task song song |
| Ngồi canh | Đi uống cà phê |
| Task bị treo = stuck | Tự phục hồi |

---

**GitHub**: [github.com/longtho638-jpg/openclaw-worker](https://github.com/longtho638-jpg/openclaw-worker)  
**License**: MIT — Tự do sử dụng, fork, thương mại hóa.

*OpenClaw Worker — Để AI làm việc, bạn làm chiến lược.* 🦞
```

## File: `config.js`
```javascript
const path = require('path');
const os = require('os');

const HOME = os.homedir();
const PROJECT_DIR = process.env.MEKONG_DIR || process.cwd();

module.exports = {
  MEKONG_DIR: PROJECT_DIR,
  OPENCLAW_HOME: process.env.OPENCLAW_HOME || path.join(HOME, '.openclaw'),
  WATCH_DIR: path.join(PROJECT_DIR, 'tasks'),
  PROCESSED_DIR: path.join(PROJECT_DIR, 'tasks', 'processed'),
  REJECTED_DIR: path.join(PROJECT_DIR, 'tasks', 'rejected'),
  LOG_FILE: process.env.TOM_HUM_LOG || path.join(HOME, 'tom_hum_cto.log'),
  THERMAL_LOG: process.env.TOM_HUM_THERMAL_LOG || path.join(HOME, 'tom_hum_thermal.log'),
  MISSION_FILE: '/tmp/tom_hum_next_mission.txt',
  DONE_FILE: '/tmp/tom_hum_mission_done',
  TASK_PATTERN: /^(?:CRITICAL_|HIGH_|MEDIUM_|LOW_)?mission_.*\.txt$/,
  MISSION_TIMEOUT_MS: 45 * 60 * 1000,
  TIMEOUT_SIMPLE: 15 * 60 * 1000,   // 15 min
  TIMEOUT_MEDIUM: 30 * 60 * 1000,   // 30 min
  TIMEOUT_COMPLEX: 45 * 60 * 1000,  // 45 min
  POLL_INTERVAL_MS: 200,
  COOLING_INTERVAL_MS: 90000,
  AUTO_CTO_EMPTY_THRESHOLD: 10,
  STATE_FILE: path.join(PROJECT_DIR, 'tasks', '.tom_hum_state.json'),
  PROXY_PORT: process.env.PROXY_PORT ? parseInt(process.env.PROXY_PORT) : 11434,
  CLOUD_BRAIN_URL: process.env.CLOUD_BRAIN_URL || 'http://127.0.0.1:11436',
  QWEN_PROXY_PORT: 8081,
  MODEL_NAME: process.env.MODEL_NAME || 'claude-3-5-sonnet-20241022',
  OPUS_MODEL: 'claude-opus-4-5-20250514',
  USE_GH_MODELS: false,
  FALLBACK_MODEL_NAME: process.env.FALLBACK_MODEL || 'gemini-1.5-flash',
  QWEN_MODEL_NAME: process.env.QWEN_MODEL_NAME || 'qwen3-coder-next',
  ENGINE: process.env.TOM_HUM_ENGINE || 'antigravity',
  PROJECTS: [],  // Add your project names here

  // Self-Healer
  HEALTH_CHECK_INTERVAL_MS: 30_000,
  PROXY_PING_TIMEOUT_MS: 5_000,
  MAX_RECOVERY_ATTEMPTS: 3,
  STALE_OUTPUT_THRESHOLD_MS: 3 * 60_000,
  MODEL_FALLBACK_CHAIN: ['claude-sonnet-4-5-20250514', 'gemini-3-flash', 'qwen3-coder-next'],

  // Agent Team orchestration
  MAX_CONCURRENT_MISSIONS: 3,
  AGENT_TEAM_SIZE_DEFAULT: 4,
  AGENT_TEAM_TIMEOUT_MS: 4 * 60 * 60 * 1000,

  // Complexity classification
  COMPLEXITY: {
    COMPLEX_KEYWORDS: ['refactor', 'redesign', 'migrate', 'rewrite', 'architecture', 'security audit', 'performance audit', 'tech debt'],
    MEDIUM_KEYWORDS: ['feature', 'implement', 'security', 'audit', 'integration', 'api', 'database', 'auth', 'testing'],
  },

  // Agent Team roles
  AGENT_TEAM_ROLES: {
    security_scan: ['code-reviewer', 'tester', 'debugger', 'fullstack-developer'],
    tech_debt: ['code-reviewer', 'tester', 'fullstack-developer', 'researcher'],
    perf_audit: ['code-reviewer', 'tester', 'debugger', 'fullstack-developer'],
    default: ['code-reviewer', 'tester', 'debugger', 'fullstack-developer'],
  },

  // Example autonomous tasks
  BINH_PHAP_TASKS: [
    { id: 'console_cleanup', complexity: 'simple', cmd: 'Clean all console.log and debug statements from production code' },
    { id: 'type_safety', complexity: 'medium', cmd: 'Audit TypeScript any types — fix all with proper type annotations' },
    { id: 'security_scan', complexity: 'complex', cmd: 'Security audit — check CSP headers, XSS vectors, exposed secrets, CORS config' },
    { id: 'tech_debt', complexity: 'complex', cmd: 'Full codebase review — TODO/FIXME/HACK count, dead code, circular deps' },
  ],
};
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 AgencyOS / OpenClaw

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `README.md`
```markdown
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
```

## File: `restore_swarm.sh`
```bash
#!/bin/bash
# 🦞 TÔM HÙM SWARM — 4 Panes inside Antigravity Terminal
# Run this INSIDE Antigravity's terminal (Ctrl+`)
# Gets tmux tiled layout: P0=Logs, P1-P3=CC CLI Workers

SESSION="tom_hum_brain"

# Environment
PROXY_URL="http://localhost:11436"
CLAUDE_CONFIG="$HOME/.claude_openclaw"
ENV_CMD="unset ANTHROPIC_AUTH_TOKEN; export ANTHROPIC_API_KEY='ollama' ANTHROPIC_BASE_URL='$PROXY_URL' CLAUDE_BASE_URL='$PROXY_URL' CLAUDE_CONFIG_DIR='$CLAUDE_CONFIG'"
CC_CMD="claude --model claude-3-5-sonnet-20241022 --dangerously-skip-permissions"

# Kill old session
tmux kill-session -t $SESSION 2>/dev/null
sleep 1

# Create new session with P0 = Log viewer
tmux new-session -d -s $SESSION -x 200 -y 50
tmux send-keys -t ${SESSION}:0.0 "echo '📋 P0: MISSION CONTROL' && tail -f ~/tom_hum_cto.log" Enter

# P1 = CC CLI Worker 1
tmux split-window -t ${SESSION}:0
tmux send-keys -t ${SESSION}:0.1 "$ENV_CMD && echo '🦞 P1: WORKER 1' && $CC_CMD" Enter

# P2 = CC CLI Worker 2
tmux split-window -t ${SESSION}:0
tmux send-keys -t ${SESSION}:0.2 "$ENV_CMD && echo '🦞 P2: WORKER 2' && $CC_CMD" Enter

# P3 = CC CLI Worker 3
tmux split-window -t ${SESSION}:0
tmux send-keys -t ${SESSION}:0.3 "$ENV_CMD && echo '🦞 P3: WORKER 3' && $CC_CMD" Enter

# Tiled layout (4 equal panes)
tmux select-layout -t ${SESSION}:0 tiled

echo "✅ TÔM HÙM 4-Pane Swarm ACTIVE inside Antigravity!"
echo "📋 P0: Log viewer | 🦞 P1-P3: CC CLI Workers"
echo ""
echo "Attach: tmux attach -t $SESSION"

# Auto-attach
tmux attach -t $SESSION
```

## File: `SETUP_GUIDE.md`
```markdown
# 🦞 TÔM HÙM Swarm — Setup Guide

> Hệ thống tự động giao việc cho CC CLI Workers qua file drop.

## Yêu cầu

| Tool | Installation: |
|------|---------|
| Node.js 18+ | [nodejs.org](https://nodejs.org) |
| tmux | `brew install tmux` (macOS) / `sudo apt install tmux` (Linux) |
| Claude CLI | `npm install -g @anthropic-ai/claude-code` |
| Antigravity Proxy | Đã có trong `scripts/anthropic-adapter.js` |

## Khởi động nhanh

```bash
# 1. Clone repo
git clone <repo-url> mekong-cli && cd mekong-cli

# 2. Cài dependencies
npm install

# 3. Khởi động Proxy (terminal riêng)
node scripts/anthropic-adapter.js 11436

# 4. Khởi động 4-pane Swarm
bash restore_swarm.sh
```

Xong! Sẽ thấy 4 ô tmux:
```
┌──────────────┬──────────────┐
│ P0: Log      │ P1: CC CLI   │
│ (tail -f)    │ Worker 1     │
├──────────────┼──────────────┤
│ P2: CC CLI   │ P3: CC CLI   │
│ Worker 2     │ Worker 3     │
└──────────────┴──────────────┘
```

## Giao việc

Drop file vào thư mục `tasks/`:
```bash
echo 'Description: task ở đây' > tasks/mission_project_auto_tên-task.txt
```

Task-watcher tự detect → dispatch vào P1-P3 → xong thì archive.

## Giám sát

```bash
# Xem log real-time
tail -f ~/tom_hum_cto.log

# Attach lại tmux (nếu bị disconnect)
tmux attach -t tom_hum_brain

# Dừng swarm
tmux kill-session -t tom_hum_brain
```

## Tương thích

| OS | Status: |
|----|-----------|
| macOS (M1/M2/Intel) | ✅ Đã test |
| Linux (Ubuntu/Debian) | ✅ Hỗ trợ |
| Windows | ✅ Qua WSL2 |

## Configuration:

Sửa trong `apps/openclaw-worker/config.js`:
- `MODEL_NAME` — Model CC CLI sử dụng
- `MAX_CONCURRENT_MISSIONS` — Số task chạy song song (mặc định: 3)
- `CLOUD_BRAIN_URL` — URL proxy (mặc định: `http://localhost:11436`)
```

## File: `task-watcher.js`
```javascript
#!/usr/bin/env node
/**
 * TOM HUM (OpenClaw) Task Watcher — v2026.2.13 TMUX INTERACTIVE
 *
 * Thin orchestrator: imports modules, wires lifecycle, handles shutdown.
 * Runs FOREVER as a daemon — never exits after queue empties.
 * Self-healing: any exception → log + sleep 30s + continue.
 *
 * v2026.2.13 changes (upstream sync):
 *   - Write-ahead delivery queue: missions survive restarts (#15636)
 *   - Stale state cleanup: clear command-queue on restart (#15195)
 *   - SIGUSR1 in-process restart: clear zombie state (#15195)
 *   - Heartbeat race fix: scheduler no longer dies silently (#15108)
 *   - Session archival: /new /reset clean stale transcripts (#14869)
 *
 * Modules:
 *   config.js                    — All constants, paths, env vars
 *   lib/brain-tmux.js            — Tmux brain (CC CLI interactive session)
 *   lib/mission-dispatcher.js    — Prompt building, project routing
 *   lib/task-queue.js            — File watching, queuing, archiving
 *   lib/auto-cto-pilot.js        — Binh Phap auto-task generation
 *   lib/m1-cooling-daemon.js     — M1 thermal management + thermal gate
 */

const fs = require('fs');
const path = require('path');
const config = require('./config');

// --- Unhandled error protection FIRST: log but do NOT crash the daemon ---
process.on('uncaughtException', (err) => {
  const msg = `[${new Date().toISOString().slice(11, 19)}] [tom-hum] UNCAUGHT EXCEPTION (daemon stays alive): ${err.stack || err.message}\n`;
  try { fs.appendFileSync(config.LOG_FILE, msg); } catch (e) { }
});
process.on('unhandledRejection', (reason) => {
  const msg = `[${new Date().toISOString().slice(11, 19)}] [tom-hum] UNHANDLED REJECTION (daemon stays alive): ${reason}\n`;
  try { fs.appendFileSync(config.LOG_FILE, msg); } catch (e) { }
});

// --- Import modules ---
const { spawnBrain, killBrain, log } = require('./lib/brain-vscode-terminal');
const { startWatching, stopWatching } = require('./lib/task-queue');
const { startAutoCTO, stopAutoCTO } = require('./lib/auto-cto-pilot');
const { startCooling, stopCooling } = require('./lib/m1-cooling-daemon');
const { startMonitor: startHealer, stopMonitor: stopHealer } = require('./lib/self-healer');

// --- v2026.2.13: Write-ahead queue for crash recovery (#15636) ---
const WAL_FILE = path.join(config.WATCH_DIR, '.wal.json');

function clearStaleState() {
  // v2026.2.13: Clear stale command-queue and heartbeat state after restart (#15195)
  try {
    if (fs.existsSync(WAL_FILE)) {
      const wal = JSON.parse(fs.readFileSync(WAL_FILE, 'utf8'));
      if (wal.inFlight && wal.inFlight.length > 0) {
        log(`WAL RECOVERY: Found ${wal.inFlight.length} in-flight mission(s) — re-queuing`);
        for (const mission of wal.inFlight) {
          const dest = path.join(config.WATCH_DIR, mission.filename);
          if (!fs.existsSync(dest)) {
            fs.writeFileSync(dest, mission.prompt);
            log(`WAL RECOVERY: Re-queued ${mission.filename}`);
          }
        }
      }
      fs.unlinkSync(WAL_FILE);
      log('WAL: Cleared stale write-ahead log');
    }
  } catch (e) {
    log(`WAL: Could not recover — ${e.message}`);
  }

  // v2026.2.13: Archive stale session transcripts (#14869)
  try {
    const gateResults = path.join(__dirname, '.gate-results.json');
    if (fs.existsSync(gateResults)) {
      const stats = fs.statSync(gateResults);
      const ageHours = (Date.now() - stats.mtimeMs) / (1000 * 60 * 60);
      if (ageHours > 24) {
        fs.unlinkSync(gateResults);
        log('CLEANUP: Archived stale gate results (>24h)');
      }
    }
  } catch (e) { /* non-critical */ }
}

// --- Self-healing boot: retry each module independently ---
function safeBoot(name, fn) {
  try {
    fn();
    log(`BOOT OK: ${name}`);
  } catch (e) {
    log(`BOOT ERROR (${name}): ${e.message} — will retry in 30s`);
    setTimeout(() => {
      try { fn(); log(`BOOT RETRY OK: ${name}`); }
      catch (e2) { log(`BOOT RETRY FAILED (${name}): ${e2.message}`); }
    }, 30000);
  }
}

// --- Ensure required directories exist ---
try {
  if (!fs.existsSync(config.WATCH_DIR)) fs.mkdirSync(config.WATCH_DIR, { recursive: true });
  if (!fs.existsSync(config.PROCESSED_DIR)) fs.mkdirSync(config.PROCESSED_DIR, { recursive: true });
  if (!fs.existsSync(config.REJECTED_DIR)) fs.mkdirSync(config.REJECTED_DIR, { recursive: true });
} catch (e) {
  log(`WARN: Could not create task dirs: ${e.message}`);
}

// --- v2026.2.13: Clear stale state before boot ---
clearStaleState();

// --- Boot ---
log('--- MISSION CONTROL v2026.2.13 ONLINE (Tmux Interactive) ---');

safeBoot('spawnBrain', spawnBrain);
safeBoot('startWatching', startWatching);
// 🎯 FOCUSED DELIVERY MODE — Auto-CTO DISABLED to prevent non-priority mission flooding (Feb 14 2026)
// safeBoot('startAutoCTO', startAutoCTO);
safeBoot('startCooling', startCooling);
safeBoot('startHealer', startHealer);

log('Tmux Brain + File Watcher + M1 Cooling + Self-Healer ACTIVE');

// --- Keepalive: prevent Node from exiting when event loop is idle ---
const keepalive = setInterval(() => { }, 60000);

// --- Graceful Shutdown ---
let shuttingDown = false;

function shutdown(sig) {
  if (shuttingDown) return;
  shuttingDown = true;
  log(`Received ${sig} — shutting down gracefully`);
  clearInterval(keepalive);
  try { stopWatching(); } catch (e) { log(`Shutdown error (stopWatching): ${e.message}`); }
  try { stopAutoCTO(); } catch (e) { log(`Shutdown error (stopAutoCTO): ${e.message}`); }
  try { stopCooling(); } catch (e) { log(`Shutdown error (stopCooling): ${e.message}`); }
  try { stopHealer(); } catch (e) { log(`Shutdown error (stopHealer): ${e.message}`); }
  try { killBrain(); } catch (e) { log(`Shutdown error (killBrain): ${e.message}`); }
  log('All modules stopped. Goodbye.');
  process.exit(0);
}

// --- v2026.2.13: SIGUSR1 in-process restart — clear zombie state (#15195) ---
process.on('SIGUSR1', () => {
  log('Received SIGUSR1 — in-process restart (clearing stale state)');
  try { stopWatching(); } catch (e) { }
  try { stopCooling(); } catch (e) { }
  try { stopHealer(); } catch (e) { }
  clearStaleState();
  safeBoot('spawnBrain', spawnBrain);
  safeBoot('startWatching', startWatching);
  safeBoot('startCooling', startCooling);
  safeBoot('startHealer', startHealer);
  log('SIGUSR1 restart complete — all modules re-initialized');
});

process.on('SIGTERM', () => shutdown('SIGTERM'));
process.on('SIGINT', () => shutdown('SIGINT'));

```

## File: `lib/brain-headless-per-mission.js`
```javascript
/**
 * Brain Headless — Spawns claude -p per mission as isolated child process
 *
 * Each mission = one short-lived `claude -p` process.
 * Crash in one mission does NOT affect the daemon.
 * stdin MUST be 'ignore' — piped stdin causes infinite hang.
 *
 * Exports: spawnBrain, killBrain, isBrainAlive, runMission, log
 */

const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');
const config = require('../config');
const { diagnoseFailure, truncatePrompt } = require('./mission-recovery');

let missionCount = 0;
let activeMission = null; // Track current child process

// --- Logging ---

function log(msg) {
  const timestamp = new Date().toISOString().slice(11, 19);
  const formatted = `[${timestamp}] [tom-hum] ${msg}\n`;
  process.stderr.write(formatted);
  try { fs.appendFileSync(config.LOG_FILE, formatted); } catch (e) { }
}

// --- Brain lifecycle (headless = no persistent brain) ---

function spawnBrain() {
  log('BRAIN MODE: headless — each mission spawns claude -p. No persistent brain.');
}

function killBrain() {
  if (activeMission) {
    try { activeMission.kill('SIGTERM'); } catch (e) { }
    activeMission = null;
  }
  log('BRAIN MODE: headless — active mission killed (if any).');
}

function isBrainAlive() {
  // Headless mode: brain is always "alive" — we spawn on demand
  return true;
}

// --- Core: run one mission via claude -p ---

/**
 * Spawn claude -p with prompt, wait for exit, return result.
 * @param {string} prompt - Full mission prompt
 * @param {string} projectDir - Working directory for the mission
 * @param {number} timeoutMs - Max runtime before kill
 * @param {object} [opts] - Options: { model, isRetry }
 * @returns {Promise<{success: boolean, result: string, elapsed: number}>}
 */
function spawnMission(prompt, projectDir, timeoutMs, opts = {}) {
  const model = opts.model || config.MODEL_NAME;
  const isRetry = opts.isRetry || false;

  return new Promise((resolve) => {
    const startTime = Date.now();
    const num = missionCount;
    let resolved = false;
    let stdout = '';
    let stderr = '';

    const args = [
      '-p', prompt,
      '--model', model,
      '--dangerously-skip-permissions',
    ];

    log(`SPAWN #${num}${isRetry ? ' (RETRY)' : ''}: claude -p [model=${model}] [cwd=${projectDir}] [timeout=${Math.round(timeoutMs / 60000)}min]`);

    const child = spawn('claude', args, {
      cwd: projectDir,
      stdio: ['ignore', 'pipe', 'pipe'], // stdin MUST be ignore
      env: {
        ...process.env,
        ANTHROPIC_API_KEY: 'ollama',
        ANTHROPIC_BASE_URL: config.CLOUD_BRAIN_URL,
        CLAUDE_BASE_URL: config.CLOUD_BRAIN_URL,
      },
      timeout: timeoutMs,
    });

    activeMission = child;

    // Stream stdout to log
    child.stdout.on('data', (chunk) => {
      stdout += chunk.toString();
      // Log last meaningful line for visibility
      const lines = chunk.toString().trim().split('\n');
      const last = lines[lines.length - 1];
      if (last && last.length > 5) {
        const truncated = last.length > 200 ? last.slice(0, 200) + '...' : last;
        try { fs.appendFileSync(config.LOG_FILE, `[${new Date().toISOString().slice(11, 19)}] [mission-${num}] ${truncated}\n`); } catch (e) { }
      }
    });

    child.stderr.on('data', (chunk) => {
      stderr += chunk.toString();
    });

    // Timeout kill
    const timer = setTimeout(() => {
      if (resolved) return;
      resolved = true;
      activeMission = null;
      try { child.kill('SIGTERM'); } catch (e) { }
      const elapsed = Math.round((Date.now() - startTime) / 1000);
      log(`TIMEOUT: Mission #${num} exceeded ${Math.round(timeoutMs / 1000)}s — killed`);
      resolve({ success: false, result: 'timeout', elapsed });
    }, timeoutMs);

    child.on('close', (code) => {
      clearTimeout(timer);
      if (resolved) return;
      resolved = true;
      activeMission = null;
      const elapsed = Math.round((Date.now() - startTime) / 1000);
      const success = code === 0;
      log(`${success ? 'COMPLETE' : 'FAILED'}: Mission #${num} (exit=${code}, ${elapsed}s)`);
      resolve({ success, result: success ? 'done' : `exit_${code}`, elapsed, stderr });
    });

    child.on('error', (err) => {
      clearTimeout(timer);
      if (resolved) return;
      resolved = true;
      activeMission = null;
      const elapsed = Math.round((Date.now() - startTime) / 1000);
      log(`ERROR: Mission #${num} spawn failed: ${err.message}`);
      resolve({ success: false, result: 'spawn_error', elapsed, stderr: err.message });
    });
  });
}

/**
 * Run a mission with automatic recovery (model failover + context truncation).
 * @param {string} prompt - Mission prompt
 * @param {string} projectDir - Working directory
 * @param {number} timeoutMs - Timeout in ms
 * @returns {Promise<{success: boolean, result: string, elapsed: number}>}
 */
async function runMission(prompt, projectDir, timeoutMs) {
  missionCount++;
  const num = missionCount;
  log(`MISSION #${num}: ${prompt.slice(0, 150)}...`);
  log(`PROJECT: ${projectDir} | MODE: headless`);

  // First attempt
  const result = await spawnMission(prompt, projectDir, timeoutMs);

  if (result.success) return result;

  // Recovery: check if failure is recoverable
  const diagnosis = diagnoseFailure(result.stderr || '');

  if (diagnosis.action === 'model_failover') {
    log(`RECOVERY: Model failover → ${diagnosis.model}`);
    return spawnMission(prompt, projectDir, timeoutMs, { model: diagnosis.model, isRetry: true });
  }

  if (diagnosis.action === 'context_truncate') {
    log(`RECOVERY: Context overflow → truncating prompt`);
    const truncated = truncatePrompt(prompt);
    return spawnMission(truncated, projectDir, timeoutMs, { isRetry: true });
  }

  return result;
}

module.exports = { spawnBrain, killBrain, isBrainAlive, runMission, log };
```

## File: `lib/brain-terminal-app.js`
```javascript
/**
 * Brain Terminal.app — CC CLI interactive in macOS Terminal tabs
 *
 * Uses AppleScript to control Terminal.app (no tmux needed):
 *   - spawnBrain()  → Opens Terminal.app tab with CC CLI interactive
 *   - runMission()  → Pastes prompt into Terminal tab + monitors output
 *   - Full ClaudeKit TUI visible in native Terminal.app
 *
 * Why Terminal.app > tmux:
 *   - Native macOS, way more stable than tmux
 *   - Full TUI rendering (colors, unicode, ClaudeKit agents visible)
 *   - No tmux buffer/paste issues
 *   - User can see everything real-time
 *
 * Exports: spawnBrain, killBrain, isBrainAlive, runMission, log
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const config = require('../config');

let missionCount = 0;
const PROMPT_FILE = '/tmp/tom_hum_terminal_prompt.txt';
const OUTPUT_FILE = '/tmp/tom_hum_terminal_output.log';

// --- Logging ---
function log(msg) {
    const timestamp = new Date().toISOString().slice(11, 19);
    const formatted = `[${timestamp}] [tom-hum] ${msg}\n`;
    process.stderr.write(formatted);
    try { fs.appendFileSync(config.LOG_FILE, formatted); } catch (e) { }
}

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

// --- AppleScript helpers ---

/**
 * Run AppleScript command
 */
function runAppleScript(script) {
    try {
        return execSync(`osascript -e '${script.replace(/'/g, "'\\''")}'`, {
            encoding: 'utf-8',
            timeout: 10000,
        }).trim();
    } catch (e) {
        log(`APPLESCRIPT ERROR: ${e.message}`);
        return '';
    }
}

/**
 * Run multi-line AppleScript
 */
function runAppleScriptFile(script) {
    const tmpFile = '/tmp/tom_hum_applescript.scpt';
    fs.writeFileSync(tmpFile, script);
    try {
        return execSync(`osascript ${tmpFile}`, { encoding: 'utf-8', timeout: 15000 }).trim();
    } catch (e) {
        log(`APPLESCRIPT ERROR: ${e.message}`);
        return '';
    } finally {
        try { fs.unlinkSync(tmpFile); } catch (e) { }
    }
}

// --- Brain lifecycle ---

/**
 * Open Terminal.app with CC CLI interactive in a new tab
 */
function spawnBrain() {
    log('BRAIN MODE: Terminal.app — CC CLI interactive in native macOS Terminal');

    const proxyUrl = config.CLOUD_BRAIN_URL || 'http://127.0.0.1:11436';
    const proxyPort = new URL(proxyUrl).port || '11436';
    const configDir = `${HOME}/.claude_antigravity_${proxyPort}`;

    // Build the CC CLI command
    const envSetup = [
        `export ANTHROPIC_API_KEY="ollama"`,
        `export ANTHROPIC_BASE_URL="${proxyUrl}"`,
        `export CLAUDE_BASE_URL="${proxyUrl}"`,
        `export CLAUDE_CONFIG_DIR="${configDir}"`,
        `unset ANTHROPIC_AUTH_TOKEN`,
    ].join(' && ');

    const claudeCmd = `claude --model ${config.MODEL_NAME} --dangerously-skip-permissions`;
    const fullCmd = `${envSetup} && ${claudeCmd}`;

    // AppleScript to open Terminal.app with CC CLI
    const script = `
tell application "Terminal"
  activate
  set newTab to do script "${fullCmd.replace(/"/g, '\\"')}"
  set custom title of newTab to "🦞 TÔM HÙM Worker"
end tell
`;

    runAppleScriptFile(script);
    log('BRAIN: Terminal.app tab opened with CC CLI interactive');
}

function killBrain() {
    log('BRAIN: Sending Ctrl+C to Terminal.app CC CLI...');
    const script = `
tell application "Terminal"
  set targetTab to null
  repeat with w in windows
    repeat with t in tabs of w
      if custom title of t contains "TÔM HÙM" then
        set targetTab to t
      end if
    end repeat
  end repeat
  if targetTab is not null then
    do script "exit" in targetTab
  end if
end tell
`;
    runAppleScriptFile(script);
}

function isBrainAlive() {
    try {
        execSync('pgrep -f "claude.*dangerously-skip-permissions"', { timeout: 3000 });
        return true;
    } catch (e) { return false; }
}

// --- Type text into Terminal.app CC CLI tab ---

function typeInTerminal(text) {
    // Write prompt to temp file
    const tmpFile = '/tmp/tom_hum_paste.txt';
    fs.writeFileSync(tmpFile, text);

    // Use Terminal.app's `do script` to send text directly — NO System Events needed
    // Escape for AppleScript string
    const escapedFile = tmpFile.replace(/\\/g, '\\\\').replace(/"/g, '\\"');

    const script = `
set promptText to (read POSIX file "${escapedFile}")

tell application "Terminal"
  -- Find TÔM HÙM worker tab
  set targetTab to null
  repeat with w in windows
    repeat with t in tabs of w
      try
        if custom title of t contains "TÔM HÙM" then
          set targetTab to t
        end if
      end try
    end repeat
  end repeat
  
  -- If found, send prompt directly
  if targetTab is not null then
    do script promptText in targetTab
  else
    -- No worker tab found, create one
    set targetTab to do script promptText
    set custom title of targetTab to "🦞 TÔM HÙM Worker"
  end if
  
  activate
end tell
`;
    runAppleScriptFile(script);
}

// --- Core: Run mission in Terminal.app CC CLI ---

async function runMission(prompt, projectDir, timeoutMs) {
    missionCount++;
    const num = missionCount;
    const startTime = Date.now();

    log(`MISSION #${num}: ${prompt.slice(0, 150)}...`);
    log(`PROJECT: ${projectDir} | MODE: Terminal.app`);

    // Check CC CLI is running
    if (!isBrainAlive()) {
        log('BRAIN NOT RUNNING — spawning new Terminal.app tab...');
        spawnBrain();
        await sleep(10000); // Wait for CC CLI to boot
        if (!isBrainAlive()) {
            return { success: false, result: 'brain_spawn_failed', elapsed: 0 };
        }
    }

    // Build full prompt with context
    let fullPrompt = prompt;
    if (projectDir && projectDir !== config.MEKONG_DIR) {
        fullPrompt = `CONTEXT: Target Project is inside '${projectDir}'. You are at ROOT.\n${prompt}`;
    }

    // Type prompt into Terminal.app
    typeInTerminal(fullPrompt);
    log(`DISPATCHED: Mission #${num} typed into Terminal.app`);

    // ═══════════════════════════════════════════════════════════
    // MONITOR: Poll for CC CLI completion via process state
    //
    // Since we can't reliably scrape Terminal.app buffer,
    // we monitor the CC CLI process state:
    //   - pgrep shows claude running = BUSY
    //   - claude exits or shows prompt = DONE
    //   - Timeout = KILL
    // ═══════════════════════════════════════════════════════════

    const deadline = Date.now() + timeoutMs;
    let wasBusy = false;
    let idleCount = 0;

    // Initial wait for CC CLI to start processing
    await sleep(8000);

    while (Date.now() < deadline) {
        // Check if CC CLI process is alive
        const alive = isBrainAlive();
        const elapsedSec = Math.round((Date.now() - startTime) / 1000);

        if (!alive && wasBusy) {
            // CC CLI was busy but now process gone — likely completed + exited
            log(`COMPLETE: Mission #${num} — CC CLI process ended (${elapsedSec}s)`);
            return { success: true, result: 'done', elapsed: elapsedSec };
        }

        if (alive) {
            // Check CPU usage of claude process to determine busy vs idle
            try {
                const cpuInfo = execSync(
                    'ps -p $(pgrep -f "claude.*dangerously-skip-permissions" | head -1) -o %cpu= 2>/dev/null',
                    { encoding: 'utf-8', timeout: 3000 }
                ).trim();
                const cpuUsage = parseFloat(cpuInfo) || 0;

                if (cpuUsage > 5) {
                    wasBusy = true;
                    idleCount = 0;
                    if (elapsedSec % 30 === 0) {
                        log(`BUSY: Mission #${num} — CC CLI active (CPU: ${cpuUsage}%, ${elapsedSec}s)`);
                    }
                } else if (wasBusy) {
                    idleCount++;
                    if (idleCount >= 6) {  // 6 × 5s = 30s idle after being busy = done
                        log(`COMPLETE: Mission #${num} — CC CLI idle after processing (${elapsedSec}s)`);
                        return { success: true, result: 'done', elapsed: elapsedSec };
                    }
                }
            } catch (e) {
                // Process check failed — might have just exited
                if (wasBusy) {
                    log(`COMPLETE: Mission #${num} — CC CLI process ended (${elapsedSec}s)`);
                    return { success: true, result: 'done', elapsed: elapsedSec };
                }
            }
        }

        await sleep(5000);
    }

    // Timeout
    const elapsed = Math.round((Date.now() - startTime) / 1000);
    log(`TIMEOUT: Mission #${num} exceeded ${Math.round(timeoutMs / 1000)}s — leaving CC CLI running`);
    return { success: false, result: 'timeout', elapsed };
}

module.exports = { spawnBrain, killBrain, isBrainAlive, runMission, log };
```

## File: `lib/brain-tmux.js`
```javascript
/**
 * Brain Tmux — CC CLI interactive mode via tmux session
 *
 * Architecture:
 *   spawnBrain()  → tmux new-session + launch CC CLI interactive
 *   runMission()  → paste prompt + state-machine polling (DISPATCHED→BUSY→DONE)
 *   killBrain()   → tmux kill-session
 *
 * CRITICAL FIX (v29): CC CLI TUI always renders ❯ even when busy.
 * hasPrompt() alone is UNRELIABLE for completion detection.
 * runMission() uses state machine: require BUSY→IDLE transition or completion pattern.
 *
 * State machine for mission completion:
 *   DISPATCHED → BUSY → DONE
 *   Completion requires:
 *     (a) Completion pattern (Cooked/Sautéed/Churned for Xm Ys), OR
 *     (b) Was BUSY then became IDLE for 3 consecutive polls, OR
 *     (c) Never detected BUSY but elapsed > 45s and IDLE for 3 consecutive polls
 *
 * Context management: /clear every 3 missions, /compact every 5 missions
 * Crash recovery: auto-respawn with --continue, rate-limited 5/hr
 *
 * Exports: spawnBrain, killBrain, isBrainAlive, runMission, log
 */

const { execSync } = require('child_process');
const fs = require('fs');
const config = require('../config');

const TMUX_SESSION = 'tom_hum_brain';
const COMPACT_EVERY_N = 10; // Relaxed: Compact every 10 missions
const CLEAR_EVERY_N = 5;    // Relaxed: Clear every 5 missions
const MAX_RESPAWNS_PER_HOUR = 5;
const RESPAWN_COOLDOWN_MS = 5 * 60 * 1000;
const PROMPT_FILE = '/tmp/tom_hum_prompt.txt';
const MIN_MISSION_SECONDS = 15;   // SPEED BOOST: Reduced from 45s for faster local inference
const IDLE_CONFIRM_POLLS = 3;     // Consecutive idle polls required for completion

// --- DETECTION PATTERNS ---

// CC CLI activity indicators (present continuous = actively processing)
const BUSY_PATTERNS = [
  /Photosynthesizing/i, /Crunching/i, /Saut[eé]ing/i,
  /Crunching/i, /Saut[eé]ing/i,
  /Marinating/i, /Fermenting/i, /Braising/i,
  /Reducing/i, /Blanching/i, /Thinking/i,
  /Churning/i, /Cooking/i, /Toasting/i,
  /Simmering/i, /Steaming/i, /Grilling/i, /Roasting/i,
  /Hatching/i, /Envisioning/i, /Brewing/i, // v2.0 New States
  /Working/i, /Planning/i, /Executing/i,
  /Smooshing/i, /Mulling/i, /Concocting/i, /Billowing/i, /Germinating/i, // v2.1 Creative States
  /Sifting/i, /Smelting/i, /Pondering/i, /Deciphering/i,
  /⏺\s+planner/i, /⏺\s+Bash/i, /⏺\s+Left/i, // Tool execution
  /Vibing/i,                           // ClaudeKit status
  /[✻✽✶✴]\s+\w+ing/,                   // General: Star variants + any gerund verb
  // FIXED: Detect BOTH Up (Upload) and Down (Download) arrows
  /\d+[ms]\s+\d+[ms]\s*·\s*[↑↓]/,      // Timer + arrow: "4m 27s · ↑"
  /[↑↓]\s*[\d.]+k?\s*tokens/i,         // Counter: "↑ 0 tokens" or "↓ 4.5k tokens"
  /queued messages/i,
  /Press up to edit queued/i,
  /Cost:\s*\$[\d.]+/,                  // Cost display usually means busy calculating
];

// CC CLI completion indicators (past tense = finished cooking)
const COMPLETION_PATTERNS = [
  /(?:Cooked|Churned|Saut[eé]ed|Braised|Blanched|Reduced|Fermented|Marinated|Toasted|Simmered|Steamed|Grilled|Roasted)\s+for\s+\d+/i,
  /✻\s+\w+(?:ed|t)\s+for\s+\d+/i,     // General: ✻ + past tense + "for N"
];

// CC CLI asking for approval/confirmation
const APPROVE_PATTERNS = [
  /Do you want to run this command\?/,
  /Do you want to proceed\?/,
  /Do you want to execute this code\?/,
  /terraform apply/,
  /npm install/,
  /Allow this/i,
  /Enter your API key/, // Legacy prompt
  /Do you want to use this API key\?/, // <--- NEW: Custom Key Confirmation
  /\(y\/n\)/i, /\[y\/n\]/i, /\[Y\/n\]/i,
  /Do you want to continue/i,
  /Approve\?/i, /Confirm\?/i,
  /Press Enter/i, /waiting for input/i,
  /Would you like to/i, /Should I /i,
  /Use arrow keys to select/i, // More specific for menus
  /Press up to edit queued messages/i, // NEW: CC CLI v2.1.x
  /By proceeding, you accept all responsibility/i, // NEW: Bypass prompt
  /Yes, I accept/i,
  /Select an option/i,
  /Approve this code change/i, /2\.\s+No\s+\(recommended\)/i, // Catch the menu state directly
];

// CC CLI context exhaustion
const CONTEXT_LIMIT_PATTERNS = [
  /Context limit reached/i,
  /\/compact or \/clear/i,
  /context is full/i,
  /out of context/i,
];

// 🦴 GỠ XƯƠNG: CC CLI stuck in TUI menus (NOT a question, needs Escape to exit)
const STUCK_PATTERNS = [
  /Clarification/i,                     // CC CLI asking for clarification
  /What does.*mean.*Please clarify/i,    // "What does X mean?"
  /Enter to select.*navigate.*Esc/i,     // TUI selection menu
  /↑\/↓ to navigate.*Esc to cancel/i,    // Arrow key navigation menu
  /Pick a model/i,                       // Model selection menu
  /MCP server failed/i,                  // MCP server error
  /There's an issue with the selected model/i, // Model not available
  /Run \/model to pick a different model/i,    // Model fallback prompt
  /Always run.*Exit code/i,              // Exit/run menu
  /Checked command status/i,             // Stuck checking status
  /Rewind/i,                             // 🦴 Rewind screen (stale session)
  /Restore the code.*conversation/i,     // 🦴 Restore prompt
  /Enter to continue.*Esc to exit/i,     // 🦴 Rewind selection menu
  /Model.*not found/i,                   // 🦴 Model validation failure
  /No code changes/i,                    // 🦴 Rewind "No code changes" option
  /Interrupted · What should Claude do instead/i, // 🦴 Caught in a loop
];

// 🦴 GỠ XƯƠNG: Nuclear patterns — need full CC CLI respawn, not just Escape
// NOTE: "Interrupted" is handled by STUCK_PATTERNS + isInterrupted (soft Enter).
// Do NOT put it here — tmux scrollback retains the text after clear-history,
// causing an infinite respawn loop.
const NUCLEAR_PATTERNS = [
  /There's an issue with the selected model/i,
  /Model.*not found/i,
  /Run \/model to pick a different model/i,
];

let missionCount = 0;
let respawnTimestamps = [];
let stuckRetryCount = {};  // Per-pane stuck retry counter
const activePaneLocks = new Set(); // v2026.2.14: Tracks panes currently executing a mission

// --- Logging ---

function log(msg) {
  const timestamp = new Date().toISOString().slice(11, 19);
  const formatted = `[${timestamp}] [tom-hum] ${msg}\n`;
  try { process.stderr.write(formatted); } catch (e) { /* EPIPE safe */ }
  try { fs.appendFileSync(config.LOG_FILE, formatted); } catch (e) { }
}

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

/** Strip ANSI escape codes + control characters from captured tmux text */
function stripAnsi(text) {
  return text
    .replace(/\x1B\[[0-9;?]*[A-Za-z]/g, '')         // CSI sequences (colors, cursor)
    .replace(/\x1B\][^\x07\x1B]*(?:\x07|\x1B\\)/g, '') // OSC sequences (BEL or ST)
    .replace(/\x1B[()][A-Za-z0-9]/g, '')              // Character set selection
    .replace(/\x1B[A-Za-z]/g, '')                      // Simple ESC sequences
    .replace(/[\x00-\x08\x0E-\x1F\x7F]/g, '');        // Control chars (keep \t \n \r)
}

// --- Tmux helpers ---

function tmuxExec(cmd) {
  try {
    return execSync(cmd, { encoding: 'utf-8', timeout: 10000 }).trim();
  } catch (e) { return ''; }
}

function isSessionAlive() {
  try {
    execSync(`tmux has-session -t ${TMUX_SESSION} 2>/dev/null`, { timeout: 5000 });
    return true;
  } catch (e) { return false; }
}

function capturePane(paneIdx) {
  const p = (paneIdx !== undefined) ? paneIdx : currentWorkerIdx;
  const target = `${TMUX_SESSION}:0.${p}`;
  return tmuxExec(`tmux capture-pane -t ${target} -p -S -50`);
}

/** Get clean last N lines from captured tmux output */
function getCleanTail(output, n) {
  return stripAnsi(output).split('\n').slice(-n);
}

// --- State detection functions ---

/** CC CLI is ACTIVELY PROCESSING (Photosynthesizing, Crunching, etc.) */
function isBusy(output) {
  const tail = getCleanTail(output, 25).join('\n');
  return BUSY_PATTERNS.some(p => p.test(tail));
}

/** Mission completion pattern found (Cooked for Xm Ys, Sautéed for Xm Ys) */
function hasCompletionPattern(output) {
  const tail = getCleanTail(output, 25).join('\n');
  return COMPLETION_PATTERNS.some(p => p.test(tail));
}

/** CC CLI prompt visible — ONLY meaningful when NOT busy.
 *  WARNING: CC CLI TUI always renders ❯ even when processing.
 *  This function gates on !isBusy() but callers should still treat
 *  this as a weak signal and require additional confirmation. */
function hasPrompt(output) {
  if (isBusy(output)) return false;
  for (const line of getCleanTail(output, 10)) {
    const t = line.trim();
    if (!t) continue;
    if (t.includes('❯')) return true;
    if (/^>\s*$/.test(t)) return true;
  }
  return false;
}

function hasApproveQuestion(output) {
  const tail = getCleanTail(output, 10).join('\n');
  return APPROVE_PATTERNS.some(p => p.test(tail));
}

function hasContextLimit(output) {
  const tail = getCleanTail(output, 15).join('\n');
  return CONTEXT_LIMIT_PATTERNS.some(p => p.test(tail));
}

/** 🦴 GỠ XƯƠNG: CC CLI stuck in TUI menu (Clarification, model select, etc.) */
function isStuck(output) {
  const tail = getCleanTail(output, 10).join('\n');
  return STUCK_PATTERNS.some(p => p.test(tail));
}

/** Check if the pane is sitting at a raw shell prompt (zsh/bash) instead of Claude */
function isShellPrompt(output) {
  const tail = getCleanTail(output, 5).join('\n');
  // Matches typical shell prompts: "user@host dir %", "bash-3.2$", etc.
  // CRITICAL: Claude's prompt is "❯" or ">". Shell is "%" or "$".
  if (tail.includes('❯')) return false; // Claude is active
  if (tail.includes('Choose a capability:')) return false; // Claude menu
  if (/^>\s*$/.test(tail.trim())) return false; // Simple interactive prompt

  if (/%[\s]*$/.test(tail)) return true; // zsh
  if (/\$ \s*$/.test(tail)) return true; // bash
  if (/# \s*$/.test(tail)) return true; // root
  return false;
}

/** Unified state detection from tmux output.
 *  Returns: 'busy' | 'complete' | 'context_limit' | 'stuck' | 'question' | 'idle' | 'unknown'
 *  CRITICAL: BUSY checked BEFORE completion — prevents stale "Cooked for"
 *  in scrollback from overriding active processing indicators. */
function detectState(output) {
  if (hasContextLimit(output)) return 'context_limit';
  // 九變 FIX: Check BUSY first — prevents stale "Interrupted" text from
  // overriding active processing. If CLI is actively working (Metamorphosing,
  // Searching, etc.), it is NOT stuck — even if old stuck text is in scrollback.
  if (isBusy(output)) return 'busy';
  // Then check stuck (menus, Interrupted, model errors)
  if (isStuck(output)) return 'stuck';
  // Questions (approve prompts) — need Enter/y
  if (hasApproveQuestion(output)) return 'question';
  if (hasCompletionPattern(output)) return 'complete';
  if (hasPrompt(output)) return 'idle';
  return 'unknown';
}

// --- Text dispatch ---

function pasteText(text, paneIdx) {
  const p = (paneIdx !== undefined) ? paneIdx : currentWorkerIdx;
  const bufferName = `buf_${p}`;
  // Use unique prompt files for parallel execution to avoid collisions
  const tempPromptFile = `/tmp/tom_hum_prompt_${p}.txt`;
  fs.writeFileSync(tempPromptFile, text);

  // v2026.2.14: Use NAMED BUFFERS to avoid global buffer race conditions
  tmuxExec(`tmux load-buffer -b ${bufferName} ${tempPromptFile}`);
  const target = `${TMUX_SESSION}:0.${p}`;
  tmuxExec(`tmux paste-buffer -b ${bufferName} -t ${target}`);

  try { fs.unlinkSync(tempPromptFile); } catch (e) { }
}

function sendEnter(paneIdx) {
  const p = (paneIdx !== undefined) ? paneIdx : currentWorkerIdx;
  const target = `${TMUX_SESSION}:0.${p}`;
  // ⚡ WARP SPEED: Instant Enter (No Sleep)
  tmuxExec(`tmux send-keys -t ${target} Enter`);
  tmuxExec(`tmux send-keys -t ${target} Enter`); // Double tap just in case (queue screen)
}

function sendCtrlC(paneIdx) {
  const p = (paneIdx !== undefined) ? paneIdx : currentWorkerIdx;
  const target = `${TMUX_SESSION}:0.${p}`;
  tmuxExec(`tmux send-keys -t ${target} C-c`);
}

/** Poll until prompt appears (used by spawnBrain/respawn/context management) */
async function waitForPrompt(timeoutMs = 120000, paneIdx) {
  const deadline = Date.now() + timeoutMs;
  while (Date.now() < deadline) {
    if (hasPrompt(capturePane(paneIdx))) return true;
    await sleep(200); // ⚡ WARP SPEED: 200ms check (was 3000ms)
  }
  return false;
}

// --- Respawn rate limiting ---

function canRespawn() {
  // USER DEMAND: "vòng lặp vô tận cấm off" (Infinite Loop, Never Off)
  // We disable the rate limiter entirely.
  // const cutoff = Date.now() - 3600000;
  // respawnTimestamps = respawnTimestamps.filter(ts => ts > cutoff);
  // return respawnTimestamps.length < MAX_RESPAWNS_PER_HOUR;
  return true;
}

function buildClaudeCmd() {
  // 🦴 PERMANENT FIX: Always use CLOUD_BRAIN_URL (port 11436) — PROXY_PORT (11434) is WRONG
  const baseUrl = config.CLOUD_BRAIN_URL || `http://127.0.0.1:11436`;
  const proxyPort = new URL(baseUrl).port || '11436';
  const model = config.MODEL_NAME;
  const claudeConfigDir = `${HOME}/.claude_antigravity_${proxyPort}`;
  // FIX: Set ALL env vars (match spawnBrain) — unset AUTH_TOKEN to prevent conflict
  const envVars = `unset ANTHROPIC_AUTH_TOKEN && export ANTHROPIC_API_KEY="ollama" && export ANTHROPIC_BASE_URL="${baseUrl}" && export CLAUDE_BASE_URL="${baseUrl}" && export CLAUDE_CONFIG_DIR="${claudeConfigDir}"`;
  return `${envVars} && claude --model ${model} --mcp-config "${claudeConfigDir}/mcp.json" --dangerously-skip-permissions`;
}

// --- Brain lifecycle ---

// Brain State
let currentWorkerIdx = 1; // Start at P1 (P0 is Monitor), unless Full CLI

function spawnBrain() {
  const teamSize = config.AGENT_TEAM_SIZE_DEFAULT || 4; // Default 4 (P0-P3)

  if (isSessionAlive()) {
    try {
      const paneCount = parseInt(execSync(`tmux list-panes -t ${TMUX_SESSION} | wc -l`, { encoding: 'utf-8' }).trim());
      if (paneCount >= teamSize) {
        log(`BRAIN: tmux session exists (Panes: ${paneCount}/${teamSize}) — reusing`);
        return;
      }
      log(`BRAIN: Session exists but has ${paneCount}/${teamSize} panes. REPAIRING...`);

      // FIXED: Use Cloud Brain URL (Serveo/Ollama)
      const proxyUrl = config.CLOUD_BRAIN_URL;

      // FIX: Standardize all env vars to 'ollama' bridge protocol
      // 🦴 PERMANENT FIX: Use port from CLOUD_BRAIN_URL (11436), NOT config.PROXY_PORT (11434)
      const proxyPortNum = new URL(proxyUrl).port || '11436';
      const claudeConfigDir = `${HOME}/.claude_antigravity_${proxyPortNum}`;
      // FIX: Standardize all env vars to 'ollama' bridge protocol
      // REMOVED ANTHROPIC_AUTH_TOKEN to avoid conflict (502/Auth Warning)
      const envVars = `export ANTHROPIC_API_KEY="ollama" && export ANTHROPIC_BASE_URL="${proxyUrl}" && export CLAUDE_BASE_URL="${proxyUrl}" && export CLAUDE_CONFIG_DIR="${claudeConfigDir}"`;
      const geminiCmd = `${envVars} && claude --model ${config.MODEL_NAME} --mcp-config "${claudeConfigDir}/mcp.json" --dangerously-skip-permissions`;

      // Repair Loop: Add missing panes
      for (let i = paneCount; i < teamSize; i++) {
        log(`BRAIN: Spawning missing Worker P${i}...`);
        tmuxExec(`tmux split-window -t ${TMUX_SESSION}:0`);
        tmuxExec(`tmux select-layout -t ${TMUX_SESSION}:0 tiled`);
        execSync('sleep 1');
        tmuxExec(`tmux send-keys -t ${TMUX_SESSION}:0.${i} '${geminiCmd}' Enter`);
        // AUTO-ACCEPT Bypass Permissions for repaired panes
        execSync('sleep 5');
        tmuxExec(`tmux send-keys -t ${TMUX_SESSION}:0.${i} Down Enter`);
        execSync('sleep 2');
        tmuxExec(`tmux send-keys -t ${TMUX_SESSION}:0.${i} Down Enter`); // Double Down just in case
        tmuxExec(`tmux send-keys -t ${TMUX_SESSION}:0.${i} Enter`);
      }
      return; // Repair done
    } catch (e) {
      log(`BRAIN: Error checking/repairing session: ${e.message}`);
    }
  }

  log(`BRAIN: Creating tmux session with CC CLI interactive (Team Size: ${teamSize})...`);
  if (config.FULL_CLI_MODE) log('BRAIN: ⚡️ ANTIGRAVITY GOD MODE ACTIVE: P0 IS A WORKER ⚡️');

  // FORCE correct proxy URL — ignore shell env to prevent ECONNREFUSED
  const proxyUrl = config.CLOUD_BRAIN_URL || `http://127.0.0.1:${config.PROXY_PORT}`;
  log(`BRAIN: Connecting to Brain URL: ${proxyUrl}`);

  // Create explicit config with CLAUDEKIT INJECTION 💉
  // 🦴 PERMANENT FIX: Use port from CLOUD_BRAIN_URL (11436), NOT config.PROXY_PORT (11434)
  const proxyPortNum = new URL(proxyUrl).port || '11436';
  const claudeConfigDir = `${HOME}/.claude_antigravity_${proxyPortNum}`;
  const fs = require('fs');
  if (!fs.existsSync(claudeConfigDir)) fs.mkdirSync(claudeConfigDir, { recursive: true });

  // 🦴 SEED .claude.json: Prevent CC CLI first-run prompts (OAuth login, effort level, security notes)
  const claudeJsonPath = `${claudeConfigDir}/.claude.json`;
  const sourceDir = '${HOME}/.claude_antigravity_11434';
  if (!fs.existsSync(claudeJsonPath) || fs.statSync(claudeJsonPath).size < 2000) {
    // Try copy from working _11434 dir first
    if (fs.existsSync(`${sourceDir}/.claude.json`)) {
      try {
        fs.copyFileSync(`${sourceDir}/.claude.json`, claudeJsonPath);
        log('BRAIN: Seeded .claude.json from _11434 (full auth + history)');
      } catch (e) { log(`BRAIN: Copy .claude.json failed: ${e.message}`); }
    } else {
      // Fallback: create minimal .claude.json with required fields
      const minClaudeJson = {
        numStartups: 999,
        installMethod: 'global',
        customApiKeyResponses: { approved: ['ollama', 'ollama', 'ollama'], rejected: [] },
        hasCompletedOnboarding: true,
        hasAcknowledgedDisclaimer: true,
      };
      fs.writeFileSync(claudeJsonPath, JSON.stringify(minClaudeJson, null, 2));
      log('BRAIN: Seeded minimal .claude.json (no source dir)');
    }
  }
  // Seed settings.json
  const settingsPath = `${claudeConfigDir}/settings.json`;
  if (!fs.existsSync(settingsPath)) {
    fs.writeFileSync(settingsPath, JSON.stringify({
      model: config.MODEL_NAME,
      skipDangerousModePermissionPrompt: true,
      effortLevel: 'medium',
    }, null, 2));
    log('BRAIN: Seeded settings.json');
  }

  // MCP INJECTION: ClaudeKit + Filesystem + Google Suite (gogcli)
  const mcpConfig = {
    "mcpServers": {
      "claudekit": {
        "command": "/opt/homebrew/bin/ck",
        "args": ["mcp"]
      },
      "filesystem": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", "process.cwd()"]
      },
      "google": {
        "command": "/opt/homebrew/bin/gog",
        "args": ["mcp"],
        "env": {
          "GOG_ACCOUNT": ""
        }
      }
    }
  };

  const configContent = {
    "completedProjectSetup": true,
    "lastUpdateCheck": Date.now(),
    "primaryColor": "#D97757", // Tôm Hùm Orange
    "theme": "dark",
    "verbose": true,
    "dangerouslySkipPermissions": true,
    "agreedToBypassPermissions": true,
    "bypassPermissions": true,
    // "mcp": mcpConfig.mcpServers // Native CLI might ignore this in main config
  };

  // Inject API Key if present to avoid prompts
  // Inject API Key to avoid prompts (Standard Ollama protocol)
  configContent.anthropicApiKey = "ollama";
  configContent.anthropicAuthToken = "ollama"; // Bypass Login via Ollama protocol
  configContent.agreedToBypassPermissions = true;
  configContent.bypassPermissions = true;

  fs.writeFileSync(`${claudeConfigDir}/config.json`, JSON.stringify(configContent, null, 2));

  // Write dedicated MCP config file for --mcp-config flag
  fs.writeFileSync(`${claudeConfigDir}/mcp.json`, JSON.stringify(mcpConfig, null, 2));

  // FORCE API URL via wrapper env function
  // We use config.MODEL_NAME to bypass CLI validation (Opus masquerade)
  const apiKeyExport = process.env.ANTHROPIC_API_KEY ? `export ANTHROPIC_API_KEY="${process.env.ANTHROPIC_API_KEY}" && ` : '';
  // FIX: Unset AUTH_TOKEN to prevent auth conflict
  const envVars = `unset ANTHROPIC_AUTH_TOKEN && export ANTHROPIC_API_KEY="ollama" && export ANTHROPIC_BASE_URL="${proxyUrl}" && export CLAUDE_BASE_URL="${proxyUrl}" && export CLAUDE_CONFIG_DIR="${claudeConfigDir}"`;

  // FIX: Run 'claude' directly to avoid wrapper logic overhead
  const geminiCmd = `${envVars} && claude --model ${config.MODEL_NAME} --mcp-config "${claudeConfigDir}/mcp.json" --dangerously-skip-permissions`;

  // Create session (Pane 0) - MONITOR (Standard) OR WORKER (God Mode)
  let p0Cmd = `tail -f ${config.LOG_FILE}`;
  let p0Title = "P0: SUPERVISOR (Auto-CTO)";

  if (config.FULL_CLI_MODE) {
    p0Cmd = geminiCmd;
    p0Title = "P0: GOD MODE WORKER (Antigravity)";
  }

  tmuxExec(`tmux new-session -d -s ${TMUX_SESSION} -n brain -x 200 -y 50`);
  tmuxExec(`tmux send-keys -t ${TMUX_SESSION}:0.0 '${p0Cmd}' Enter`);
  tmuxExec(`tmux select-pane -t ${TMUX_SESSION}:0.0 -T "${p0Title}"`);

  // Create additional panes - WORKERS (Gemini 3 Pro High)
  for (let i = 1; i < teamSize; i++) {
    tmuxExec(`tmux split-window -t ${TMUX_SESSION}:0`);
    tmuxExec(`tmux select-layout -t ${TMUX_SESSION}:0 tiled`);
    execSync('sleep 1'); // Stagger boot to prevent API rate spikes
    tmuxExec(`tmux send-keys -t ${TMUX_SESSION}:0.${i} '${geminiCmd}' Enter`);
  }

  // AUTO-ACCEPT Bypass Permissions for all Workers
  log('BRAIN: Auto-accepting Bypass Permissions for all panes...');
  execSync('sleep 8');
  for (let i = 0; i < teamSize; i++) {
    // Only workers (and P0 if God Mode)
    if (i === 0 && !config.FULL_CLI_MODE) continue;
    // FIXv34: User request "cứ đẩy lệnh luôn" — Remove "y", just use Enter
    tmuxExec(`tmux send-keys -t ${TMUX_SESSION}:0.${i} Enter`);
    execSync('sleep 0.1');
    tmuxExec(`tmux send-keys -t ${TMUX_SESSION}:0.${i} Enter`);
  }

  // Clear history for all active panes to remove stale boot errors
  for (let i = 0; i < teamSize; i++) {
    tmuxExec(`tmux clear-history -t ${TMUX_SESSION}:0.${i}`);
  }

  // Set initial focus to P0 (if God Mode) or P1
  const startPane = config.FULL_CLI_MODE ? 0 : 1;
  tmuxExec(`tmux select-pane -t ${TMUX_SESSION}:0.${startPane}`);

  log(`BRAIN: Spawned [session=${TMUX_SESSION}] [panes=${teamSize}]`);
  log(`BRAIN: P0=${config.FULL_CLI_MODE ? 'WORKER' : 'MONITOR'}, P1-${teamSize - 1}=WORKERS`);
}

/**
 * 虛實 (Xu Shi) — 1 chạy 2 nghỉ Strategy
 * Round-robin P1→P2→P3: daemon bay vào pane để chạy
 * task-queue isProcessing mutex = chỉ 1 active tại 1 thời điểm
 * Pane nghỉ = idle ở prompt, visible nhưng không tốn proxy
 */
function rotateWorker() {
  const teamSize = config.AGENT_TEAM_SIZE_DEFAULT || 4;
  const minIdx = config.FULL_CLI_MODE ? 0 : 1;
  const maxIdx = teamSize - 1;

  // 🚀 FIXED: Find first IDLE pane that isn't locked
  // This prevents multiple parallel missions from hitting the same pane
  for (let i = 0; i < teamSize; i++) {
    // Round-robin starting from currentWorkerIdx
    const candidate = ((currentWorkerIdx + i) % teamSize);
    if (candidate < minIdx) continue;

    if (!activePaneLocks.has(candidate)) {
      currentWorkerIdx = candidate;
      log(`DISPATCH: Selected IDLE Worker P${currentWorkerIdx}`);
      tmuxExec(`tmux select-pane -t ${TMUX_SESSION}:0.${currentWorkerIdx}`);
      return currentWorkerIdx;
    }
  }

  // Fallback: This shouldn't happen if MAX_CONCURRENT_MISSIONS <= workers
  log(`WARNING: All worker panes busy! Forcing rotation to next...`);
  currentWorkerIdx++;
  if (currentWorkerIdx >= teamSize) currentWorkerIdx = minIdx;
  return currentWorkerIdx;
}

function killBrain() {
  if (isSessionAlive()) {
    tmuxExec(`tmux kill-session -t ${TMUX_SESSION}`);
    log('BRAIN: tmux session killed');
  }
}

function isBrainAlive() {
  if (!isSessionAlive()) return false;
  try {
    execSync('pgrep -f "claude"', { timeout: 3000 });
    return true;
  } catch (e) { return false; }
}

// --- Context management ---
// NOTE: 🔋 XX% via Antigravity Proxy is FAKE (tracks Anthropic limits but routes
// through Gemini). Use mission count instead.

function parseContextUsage(output) {
  const match = output.match(/🔋\s*(\d+)%/);
  return match ? parseInt(match[1]) : -1;
}

async function manageContext(paneIdx) {
  if (missionCount > 0 && missionCount % CLEAR_EVERY_N === 0) {
    log(`CONTEXT: /clear (mission #${missionCount}) on P${paneIdx}`);
    pasteText('/clear', paneIdx);
    await sleep(1000);
    sendEnter(paneIdx);
    await sleep(5000);
    await waitForPrompt(30000, paneIdx);
    return true;
  }
  return false;
}

async function compactIfNeeded(paneIdx) {
  if (missionCount > 0 && missionCount % COMPACT_EVERY_N === 0) {
    log(`CONTEXT: /compact (mission #${missionCount}) on P${paneIdx}`);
    pasteText('/compact', paneIdx);
    await sleep(1000);
    sendEnter(paneIdx);
    await sleep(10000);
    await waitForPrompt(60000, paneIdx);
  }
}

// --- Crash recovery ---

async function respawnBrain(useContinue = true) {
  if (!canRespawn()) {
    log(`RESPAWN: Rate limit (${MAX_RESPAWNS_PER_HOUR}/hr) — cooldown ${RESPAWN_COOLDOWN_MS / 1000}s`);
    await sleep(RESPAWN_COOLDOWN_MS);
    respawnTimestamps = [];
  }
  respawnTimestamps.push(Date.now());
  killBrain();
  await sleep(5000); // Wait for cleanup

  // REUSE spawnBrain() logic to ensure P0=Monitor, P1..=Workers layout
  spawnBrain();

  // Clear history of all panes after respawn to remove stale errors
  for (let i = 0; i < (config.AGENT_TEAM_SIZE_DEFAULT || 4); i++) {
    tmuxExec(`tmux clear-history -t ${TMUX_SESSION}:0.${i}`);
  }

  log(`RESPAWN: Session rebuilt via spawnBrain()`);
  return waitForPrompt(120000);
}

// --- Core: run mission via tmux (state machine) ---

async function runMission(prompt, projectDir, timeoutMs, modelOverride) {
  missionCount++;
  const num = missionCount;
  const startTime = Date.now();

  log(`MISSION #${num}: ${prompt.slice(0, 150)}...`);
  log(`PROJECT: ${projectDir} | MODE: tmux-interactive${modelOverride ? ` | MODEL: ${modelOverride} 🔥` : ''}`);

  // Rotate to next worker pane (Round Robin P1..N)
  // 🚀 FIXED: Capture paneIdx LOCALLY and LOCK it to avoid race conditions
  const paneIdx = rotateWorker();
  activePaneLocks.add(paneIdx);
  const paneKey = `P${paneIdx}`;

  try {
    // Thermal gate
    const { waitForSafeTemperature } = require('./m1-cooling-daemon');
    await waitForSafeTemperature();

    // Context management (pane-aware)
    await manageContext(paneIdx);
    await compactIfNeeded(paneIdx);

    // 虛實 Model Switch: DISABLED — CC CLI /model command validates against internal list, NOT proxy
    // Proxy handles model routing based on prompt complexity. Startup --model flag is sufficient.
    if (modelOverride) {
      log(`🔥 MODEL INTENT: ${modelOverride} (Binh Phap) — proxy routes automatically, /model DISABLED`);
      // DO NOT send /model command — CC CLI rejects it → Rewind loop → stuck
    }

    // Build full prompt
    let fullPrompt = prompt;
    if (projectDir && projectDir !== config.MEKONG_DIR) {
      // 🧠 SMART CONTEXT: Don't force CD, just provide context to avoid ENOWORKSPACES
      fullPrompt = `CONTEXT: Target Project is inside '${projectDir}'. You are at ROOT. Detect package.json/workspaces before running npm install. \n${prompt}`;
    }

    // CC CLI activity indicators (present continuous = actively processing)
    const BUSY_PATTERNS = [
      /Photosynthesizing/i, /Crunching/i, /Saut[eé]ing/i,
      /Marinating/i, /Fermenting/i, /Braising/i,
      /Reducing/i, /Blanching/i, /Thinking/i,
      /Churning/i, /Cooking/i, /Toasting/i,
      /Simmering/i, /Steaming/i, /Grilling/i, /Roasting/i,
      /Vibing/i,                           // ClaudeKit status
      /✻\s+\w+ing/,                        // General: ✻ + any gerund verb
      /\d+[ms]\s+\d+[ms]\s*·\s*↓/,         // Timer + download: "4m 27s · ↓"
      /↓\s*[\d.]+k?\s*tokens/i,            // Download counter: "↓ 4.5k tokens"
      /queued messages/i,
      /Press up to edit queued/i,
    ];

    // ... (patterns remain)

    function sendEnter() {
      tmuxExec(`tmux send-keys -t ${TMUX_SESSION} Enter`);
    }

    // ... (helpers remain)

    // SAFETY CHECK: Ensure Claude is actually running before dispatching
    // If we paste into a raw ZSH shell, we get "Command not found" errors.
    const checkOutput = capturePane();
    if (!isBrainAlive() || isShellPrompt(checkOutput)) {
      log(`CRITICAL: Brain died or dropped to shell! check=${!isBrainAlive()} shell=${isShellPrompt(checkOutput)}`);
      // Attempt rapid recovery
      const respawnSuccess = await respawnBrain(true);
      if (!respawnSuccess) {
        return { success: false, result: 'brain_died_fatal', elapsed: 0 };
      }
      // Give post-respawn some time to settle
      await sleep(5000);
    }

    // Dispatch via paste-buffer (reliable for long text + special chars)
    pasteText(fullPrompt, paneIdx);
    await sleep(3000); // FIXED: Increased from 1000ms to allow TUI to render large pastes
    sendEnter(paneIdx);
    log(`DISPATCHED: Mission #${num} sent to tmux (Pane P${paneIdx})`);

    // ═══════════════════════════════════════════════════════════════
    // STATE MACHINE: DISPATCHED → BUSY → DONE
    //
    // CC CLI TUI always renders ❯ even when busy — hasPrompt() alone
    // is NOT reliable. We track wasBusy and require either:
    //   (a) Completion pattern found (Cooked/Sautéed for Xm Ys)
    //   (b) Was BUSY → 3x consecutive IDLE polls
    //   (c) Never saw BUSY but elapsed > 45s → 3x consecutive IDLE
    // ═══════════════════════════════════════════════════════════════

    let wasBusy = false;
    let idleConfirmCount = 0;
    const deadline = Date.now() + timeoutMs;
    let lastLogTime = Date.now();
    let kickStartCount = 0;

    // Give CC CLI time to parse prompt and begin processing
    await sleep(5000); // Reduced initial sleep to check for early failures

    while (Date.now() < deadline) {
      if (!isSessionAlive()) {
        const elapsed = Math.round((Date.now() - startTime) / 1000);
        log(`BRAIN DIED: Mission #${num} (${elapsed}s)`);
        await respawnBrain(true);
        return { success: false, result: 'brain_died', elapsed };
      }

      const output = capturePane(paneIdx);
      const state = detectState(output);
      const elapsedSec = Math.round((Date.now() - startTime) / 1000);

      /* KICK-START DISABLED: User reported it causes phantom inputs (wasted tokens)
      // KICK-START: If idle and never busy in first 30s, press Enter again
      if (state === 'idle' && !wasBusy && elapsedSec < 30 && kickStartCount < 2) {
        log(`KICK-START: Idle detected early (${elapsedSec}s) — sending Enter again...`);
        sendEnter(paneIdx);
        kickStartCount++;
        await sleep(2000);
        continue;
      }
      */

      // STUCK INTERVENTION (Parallel Cooling): Kill stuck task if Hot & Long
      if (checkStuckIntervention(elapsedSec, num, paneIdx)) {
        return { success: false, result: 'killed_stuck', elapsed: elapsedSec };
      }

      switch (state) {
        case 'complete': {
          // Guard against stale completion from previous mission still in scrollback
          if (!wasBusy && elapsedSec < MIN_MISSION_SECONDS) {
            break; // Likely stale — wait for BUSY or more elapsed time
          }
          const usage = parseContextUsage(output);
          log(`COMPLETE: Mission #${num} (${elapsedSec}s) [cooked-pattern]${usage >= 0 ? ` [ctx=${usage}%]` : ''}`);
          return { success: true, result: 'done', elapsed: elapsedSec };
        }

        case 'busy':
          if (!wasBusy) log(`BUSY: Mission #${num} — CC CLI started processing (Pane P${paneIdx})`);
          wasBusy = true;
          idleConfirmCount = 0;
          break;

        case 'question':
          log(`QUESTION: Mission #${num} — auto-approving (Pane P${paneIdx})`);
          const targetPane = `${TMUX_SESSION}:0.${paneIdx}`;

          // SPECIAL CASE: Queued messages (v2.1.x)
          if (/Press up to edit queued messages/i.test(output)) {
            log(`QUESTION: Queued messages detected — sending DOUBLE ENTER to submit`);
            tmuxExec(`tmux send-keys -t ${targetPane} Enter Enter`);
          }
          // SPECIAL CASE: API Key Confirmation (Needs "1" + Enter for "Yes")
          else if (/2\.\s+No\s+\(recommended\)/i.test(output)) {
            log(`QUESTION: API Key detected in P${paneIdx} — selecting '1. Yes'`);
            tmuxExec(`tmux send-keys -t ${targetPane} 1 Enter`);
          }
          // SPECIAL CASE: Kick-Start waiting for Enter (bypass permissions)
          else if (/By proceeding, you accept all responsibility/i.test(output) || /Yes, I accept/i.test(output)) {
            log(`QUESTION: Bypass Permissions prompt — ACCEPTING with Enter (No 'y')`);
            tmuxExec(`tmux send-keys -t ${targetPane} Enter`);
          } else {
            // Default: Just send Enter (safer than 'y')
            log(`QUESTION: Generic question detected — sending Enter`);
            tmuxExec(`tmux send-keys -t ${targetPane} Enter`);
          }
          await sleep(3000);
          idleConfirmCount = 0;
          continue; // Re-check immediately

        case 'stuck': {
          // 🦴 九變 Recovery State Machine v3: Ctrl+C → Clear → Re-dispatch
          const stuckPane = `${TMUX_SESSION}:0.${paneIdx}`;
          const paneKey = `P${paneIdx}`;

          // 九變 GUARD: Don't fire stuck recovery in the first 15s — CC CLI
          // needs time for tool calls (search, read). Early recovery sends
          // Escape/Ctrl+C that INTERRUPTS active processing.
          const MIN_STUCK_SECONDS = 15;
          if (elapsedSec < MIN_STUCK_SECONDS) {
            log(`🦴 九變: P${paneIdx} stuck detected at ${elapsedSec}s — SKIPPING (< ${MIN_STUCK_SECONDS}s guard)`);
            break;
          }

          stuckRetryCount[paneKey] = (stuckRetryCount[paneKey] || 0) + 1;
          const retries = stuckRetryCount[paneKey];

          // Check specific stuck sub-states
          const currentOutput = capturePane(paneIdx);
          const isNuclear = NUCLEAR_PATTERNS.some(p => p.test(currentOutput));
          const isRewind = /Rewind|Restore the code|Enter to continue.*Esc to exit/i.test(currentOutput);
          const isInterrupted = /Interrupted\s+·\s+What\s+should\s+Claude\s+do\s+instead/i.test(currentOutput);

          if (isNuclear || retries >= 5) {
            // 🦴 NUCLEAR RESPAWN + RE-DISPATCH (九變 Biến 4)
            log(`🦴 九變 NUCLEAR: P${paneIdx} — ${isNuclear ? 'model error' : `stuck ${retries}x`} — full respawn + re-dispatch`);
            tmuxExec(`tmux send-keys -t ${stuckPane} C-c C-c`);
            await sleep(1000);
            tmuxExec(`tmux send-keys -t ${stuckPane} '/exit' Enter`);
            await sleep(3000);
            // Clear BOTH visible buffer AND scrollback BEFORE relaunch
            tmuxExec(`tmux send-keys -t ${stuckPane} C-l`);
            tmuxExec(`tmux clear-history -t ${stuckPane}`);
            await sleep(500);
            // Respawn with correct model
            const cmd = buildClaudeCmd();
            log(`🦴 九變: Respawning P${paneIdx} with fresh CC CLI`);
            tmuxExec(`tmux send-keys -t ${stuckPane} '${cmd}' Enter`);
            stuckRetryCount[paneKey] = 0;
            // Auto-accept bypass permissions prompt (Down → Enter × 2)
            await sleep(5000);
            tmuxExec(`tmux send-keys -t ${stuckPane} Down Enter`);
            await sleep(2000);
            tmuxExec(`tmux send-keys -t ${stuckPane} Down Enter`);
            tmuxExec(`tmux send-keys -t ${stuckPane} Enter`);
            // Wait for CLI to boot + re-dispatch the original mission
            const respawnReady = await waitForPrompt(45000, paneIdx);
            if (respawnReady) {
              log(`🦴 九變: P${paneIdx} respawned — RE-DISPATCHING mission #${num}`);
              pasteText(fullPrompt, paneIdx);
              await sleep(2000);
              sendEnter(paneIdx);
              wasBusy = false;
              idleConfirmCount = 0;
            } else {
              log(`🦴 九變: P${paneIdx} respawn TIMEOUT — returning failure`);
              activePaneLocks.delete(paneIdx);
              return { success: false, result: 'respawn_failed', elapsed: elapsedSec };
            }
          } else if (isInterrupted) {
            // 🦴 九變 Biến 2: Ctrl+C abort → clear scrollback → re-dispatch mission
            log(`🦴 九變: P${paneIdx} Interrupted — Ctrl+C abort + re-dispatch (retry ${retries}/5)`);
            tmuxExec(`tmux send-keys -t ${stuckPane} C-c`);
            await sleep(2000);
            // Clear stale "Interrupted" text from scrollback
            tmuxExec(`tmux send-keys -t ${stuckPane} C-l`);
            tmuxExec(`tmux clear-history -t ${stuckPane}`);
            await sleep(1000);
            const postCtrlC = capturePane(paneIdx);
            if (hasPrompt(postCtrlC)) {
              log(`🦴 九變: P${paneIdx} back to prompt — RE-DISPATCHING mission #${num}`);
              pasteText(fullPrompt, paneIdx);
              await sleep(2000);
              sendEnter(paneIdx);
              wasBusy = false;
              idleConfirmCount = 0;
              stuckRetryCount[paneKey] = 0;
            }
          } else if (isRewind) {
            // 🦴 GỠ XƯƠNG: Rewind screen — press Enter to accept current state
            log(`🦴 GỠ XƯƠNG: P${paneIdx} stuck on Rewind — pressing Enter`);
            tmuxExec(`tmux send-keys -t ${stuckPane} Enter`);
            await sleep(3000);
          } else {
            // Standard: Escape out of TUI menu
            log(`🦴 GỠ XƯƠNG: Mission #${num} — P${paneIdx} stuck in TUI menu (retry ${retries}/5) — sending Escape`);
            tmuxExec(`tmux send-keys -t ${stuckPane} Escape Escape`);
            await sleep(1000);
            const postEsc = capturePane(paneIdx);
            if (hasPrompt(postEsc)) {
              log(`🦴 GỠ XƯƠNG: P${paneIdx} back to prompt — re-entering mission`);
              stuckRetryCount[paneKey] = 0;
              sendEnter(paneIdx);
            }
          }
          await sleep(2000);
          idleConfirmCount = 0;
          continue;
        }

        case 'context_limit':
          log(`CONTEXT LIMIT: Mission #${num} — sending /clear`);
          tmuxExec(`tmux send-keys -t ${TMUX_SESSION}:0.${paneIdx} '/clear' Enter`);
          await sleep(5000);
          continue;

        case 'idle':
          if (wasBusy) {
            // 九變 CHECK: Is there "Interrupted" text visible? If so, this is a FAILED
            // mission that looks idle because ❯ prompt appeared after Interrupted.
            // Re-dispatch instead of completing.
            const idleOutput = capturePane(paneIdx);
            const wasInterrupted = /Interrupted\s+·\s+What\s+should\s+Claude\s+do\s+instead/i.test(idleOutput);
            if (wasInterrupted && elapsedSec < 120) {
              log(`🦴 九變: P${paneIdx} IDLE but has Interrupted text — Ctrl+C + RE-DISPATCH (#${num})`);
              const idlePane = `${TMUX_SESSION}:0.${paneIdx}`;
              tmuxExec(`tmux send-keys -t ${idlePane} C-c`);
              await sleep(1000);
              tmuxExec(`tmux send-keys -t ${idlePane} C-l`);
              tmuxExec(`tmux clear-history -t ${idlePane}`);
              await sleep(1000);
              pasteText(fullPrompt, paneIdx);
              await sleep(2000);
              sendEnter(paneIdx);
              wasBusy = false;
              idleConfirmCount = 0;
              continue;
            }

            // Was processing, now idle — confirm over multiple polls
            idleConfirmCount++;
            if (idleConfirmCount >= IDLE_CONFIRM_POLLS) {
              const elapsed = Math.round((Date.now() - startTime) / 1000);

              // REQUIRE > 60s for "auto-complete" if it was just idle
              if (elapsed < 60 && !/successfully implemented/i.test(output)) {
                log(`FINISH: Mission #${num} — IGNORED (Possible failure at ${elapsed}s)`);
                return { success: false, result: 'fast_failure', elapsed };
              }

              log(`COMPLETE: Mission #${num} (${elapsed}s) [idle-confirm]`);
              return { success: true, result: 'done', elapsed };
            }
          } else if (elapsedSec > 30) { // Reduced from MIN_MISSION_SECONDS to catch fast-start idle
            // Never saw BUSY — might be very fast or isBusy missed it
            idleConfirmCount++;
            if (idleConfirmCount >= IDLE_CONFIRM_POLLS) {
              log(`COMPLETE: Mission #${num} (${elapsedSec}s) [idle-no-busy]`);
              return { success: true, result: 'done', elapsed: elapsedSec };
            }
          }
          break;

        default: // 'unknown' — can't classify, reset idle counter
          idleConfirmCount = 0;
          break;
      }

      // Progress logging every 60s
      if (Date.now() - lastLogTime > 60000) {
        log(`Mission #${num} [${state}] — ${elapsedSec}s${wasBusy ? ' (was-busy)' : ''}`);
        lastLogTime = Date.now();
      }

      // PROJECT FLASH: Ultra Speed Polling (1s)
      await sleep(1000);
    }
    return { success: false, result: 'timeout', elapsed: Math.round(timeoutMs / 1000) };
  } finally {
    // 🔓 RELEASE LOCK
    activePaneLocks.delete(paneIdx);
    log(`RELEASE: Pane P${paneIdx} is available (Active: ${activePaneLocks.size})`);
  }
}

// --- SYSTEM MONITORING (User Request: "Giám sát nhiệt độ & API") ---

function getSystemMetrics() {
  try {
    // macOS Load Average
    const loadString = execSync('sysctl -n vm.loadavg').toString().trim();
    // Format: "{ 2.15 2.05 1.98 }" -> remove braces -> split
    const parts = loadString.replace(/[{}]/g, '').trim().split(/\s+/);
    const load1min = parseFloat(parts[0]);

    // Memory Usage (Approximate RSS)
    const mem = process.memoryUsage().rss / 1024 / 1024;

    return { load: load1min, mem: Math.round(mem) };
  } catch (e) {
    return { load: 0, mem: 0 };
  }
}

function isOverheating() {
  const metrics = getSystemMetrics();
  // THRESHOLD: Load > 4.0 is "Overheating" (Intervention Zone)
  if (metrics.load > 4.0) {
    // ACTIVE INTERVENTION: Monitor & Support
    const coolingTime = 10000; // 10s Cooling Nap
    appendFileSync(config.THERMAL_LOG, `[${new Date().toISOString()}] 🔥 HIGH LOAD (${metrics.load}). Intervening... Sleeping ${coolingTime / 1000}s\n`);

    // We intentionally block here to force the system to slow down.
    // This supports the machine as requested ("can thiệp hỗ trợ").
    execSync(`sleep ${coolingTime / 1000}`);

    return true;
  }
  return false;
}

// STUCK INTERVENTION: If task > 5min AND Load > 4.0, assume stuck model -> Ctrl+C
function checkStuckIntervention(elapsedSec, num, paneIdx) {
  const metrics = getSystemMetrics();
  // 300s = 5 minutes
  if (elapsedSec > 300 && metrics.load > 4.0) {
    log(`INTERVENTION: Mission #${num} stuck (${elapsedSec}s) & Hot (${metrics.load}) on P${paneIdx} — Sending Ctrl+C to unblock.`);
    sendCtrlC(paneIdx);
    return true;
  }
  return false;
}

module.exports = { spawnBrain, killBrain, isBrainAlive, runMission, log, isOverheating, getSystemMetrics, checkStuckIntervention };
```

## File: `lib/brain-vscode-terminal.js`
```javascript
/**
 * Brain VS Code Terminal — CC CLI visible in Terminal.app alongside Antigravity
 *
 * Architecture:
 *   - CC CLI runs in Terminal.app with full TUI (drag tab into Antigravity)
 *   - Prompts dispatched via Terminal.app `do script` (no Accessibility needed)
 *   - Task-watcher runs in background, monitors CC CLI process state
 *   - Falls back to headless `claude -p` if Terminal.app unavailable
 *
 * Why this approach:
 *   - NO System Events keystroke (no Accessibility permission)
 *   - NO tmux (crashes)
 *   - Full ClaudeKit TUI visible
 *   - Terminal.app `do script` is bulletproof
 *
 * Exports: spawnBrain, killBrain, isBrainAlive, runMission, log
 */

const { execSync, spawn } = require('child_process');
const fs = require('fs');
const config = require('../config');

let missionCount = 0;

// --- Logging ---
function log(msg) {
    const timestamp = new Date().toISOString().slice(11, 19);
    const formatted = `[${timestamp}] [tom-hum] ${msg}\n`;
    process.stderr.write(formatted);
    try { fs.appendFileSync(config.LOG_FILE, formatted); } catch (e) { }
}

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

// --- AppleScript helper ---
function runAppleScriptFile(script) {
    const tmpFile = '/tmp/tom_hum_applescript.scpt';
    fs.writeFileSync(tmpFile, script);
    try {
        return execSync(`osascript ${tmpFile}`, { encoding: 'utf-8', timeout: 15000 }).trim();
    } catch (e) {
        log(`APPLESCRIPT ERROR: ${e.message}`);
        return '';
    } finally {
        try { fs.unlinkSync(tmpFile); } catch (e) { }
    }
}

// --- CC CLI config ---
function getProxyConfig() {
    const proxyUrl = config.CLOUD_BRAIN_URL || 'http://127.0.0.1:11436';
    const proxyPort = new URL(proxyUrl).port || '11436';
    return {
        proxyUrl,
        configDir: `${HOME}/.claude_antigravity_${proxyPort}`,
    };
}

// --- Brain lifecycle ---

function spawnBrain() {
    log('BRAIN MODE: Antigravity Terminal — CC CLI in Terminal.app');

    const { proxyUrl, configDir } = getProxyConfig();

    // Create launcher script
    const launcher = '/tmp/tom_hum_cc_launcher.sh';
    fs.writeFileSync(launcher, [
        '#!/bin/bash',
        `export ANTHROPIC_API_KEY="ollama"`,
        `export ANTHROPIC_BASE_URL="${proxyUrl}"`,
        `export CLAUDE_BASE_URL="${proxyUrl}"`,
        `export CLAUDE_CONFIG_DIR="${configDir}"`,
        'unset ANTHROPIC_AUTH_TOKEN',
        `cd "${config.MEKONG_DIR}"`,
        'echo "🦞 TÔM HÙM Worker — CC CLI Interactive"',
        'echo "================================"',
        `claude --model ${config.MODEL_NAME} --dangerously-skip-permissions`,
    ].join('\n'), { mode: 0o755 });

    // Open in Terminal.app via AppleScript (no Accessibility needed)
    runAppleScriptFile(`
tell application "Terminal"
  activate
  do script "/tmp/tom_hum_cc_launcher.sh"
end tell
`);

    log('BRAIN: CC CLI launched in Terminal.app');
    log('TIP: Drag Terminal tab into Antigravity for integrated view');
}

function killBrain() {
    log('BRAIN: Killing CC CLI...');
    try {
        const pid = execSync('pgrep -f "claude.*dangerously-skip-permissions" | head -1', {
            encoding: 'utf-8', timeout: 3000
        }).trim();
        if (pid) execSync(`kill ${pid}`, { timeout: 3000 });
    } catch (e) { }
}

function isBrainAlive() {
    try {
        execSync('pgrep -f "claude.*dangerously-skip-permissions"', { timeout: 3000 });
        return true;
    } catch (e) { return false; }
}

// --- Send prompt to CC CLI via Terminal.app `do script` ---
function typeInTerminal(text) {
    fs.writeFileSync('/tmp/tom_hum_paste.txt', text);

    // Terminal.app `do script` — reliable, no permissions needed
    const result = runAppleScriptFile(`
set promptText to (read POSIX file "/tmp/tom_hum_paste.txt")

tell application "Terminal"
  set targetTab to null
  repeat with w in windows
    repeat with t in tabs of w
      try
        set tabContent to contents of t
        if tabContent contains "TÔM HÙM Worker" then
          set targetTab to t
        end if
      end try
    end repeat
  end repeat
  
  if targetTab is not null then
    do script promptText in targetTab
  else
    set targetTab to do script "/tmp/tom_hum_cc_launcher.sh"
    delay 5
    do script promptText in targetTab
  end if
  activate
end tell
`);
    return true;
}

// --- Headless fallback ---
function runHeadlessFallback(prompt, projectDir, timeoutMs) {
    return new Promise((resolve) => {
        const startTime = Date.now();
        let resolved = false;
        const { proxyUrl } = getProxyConfig();

        const args = ['-p', prompt, '--model', config.MODEL_NAME, '--dangerously-skip-permissions'];
        log(`FALLBACK HEADLESS: claude -p [cwd=${projectDir}] [timeout=${Math.round(timeoutMs / 60000)}min]`);

        const child = spawn('claude', args, {
            cwd: projectDir,
            stdio: ['ignore', 'pipe', 'pipe'],
            env: {
                ...process.env,
                ANTHROPIC_API_KEY: 'ollama',
                ANTHROPIC_BASE_URL: proxyUrl,
                CLAUDE_BASE_URL: proxyUrl,
            },
            timeout: timeoutMs,
        });

        child.stdout.on('data', (chunk) => {
            const last = chunk.toString().trim().split('\n').pop();
            if (last && last.length > 5) {
                const line = last.length > 200 ? last.slice(0, 200) + '...' : last;
                try { fs.appendFileSync(config.LOG_FILE, `[${new Date().toISOString().slice(11, 19)}] [headless] ${line}\n`); } catch (e) { }
            }
        });

        const timer = setTimeout(() => {
            if (resolved) return;
            resolved = true;
            try { child.kill('SIGTERM'); } catch (e) { }
            resolve({ success: false, result: 'timeout', elapsed: Math.round((Date.now() - startTime) / 1000) });
        }, timeoutMs);

        child.on('close', (code) => {
            clearTimeout(timer);
            if (resolved) return;
            resolved = true;
            const elapsed = Math.round((Date.now() - startTime) / 1000);
            resolve({ success: code === 0, result: code === 0 ? 'done' : `exit_${code}`, elapsed });
        });

        child.on('error', () => {
            clearTimeout(timer);
            if (resolved) return;
            resolved = true;
            resolve({ success: false, result: 'spawn_error', elapsed: 0 });
        });
    });
}

// --- Core: Run mission ---
async function runMission(prompt, projectDir, timeoutMs) {
    missionCount++;
    const num = missionCount;
    const startTime = Date.now();

    log(`MISSION #${num}: ${prompt.slice(0, 150)}...`);
    log(`PROJECT: ${projectDir} | MODE: Antigravity Terminal`);

    // If CC CLI not running, spawn it
    if (!isBrainAlive()) {
        log('CC CLI not running — spawning...');
        spawnBrain();
        await sleep(12000);
        if (!isBrainAlive()) {
            log('CC CLI failed to start — headless fallback');
            return runHeadlessFallback(prompt, projectDir, timeoutMs);
        }
    }

    // Build prompt with context
    let fullPrompt = prompt;
    if (projectDir && projectDir !== config.MEKONG_DIR) {
        fullPrompt = `CONTEXT: Target Project inside '${projectDir}'. At ROOT.\n${prompt}`;
    }

    // Dispatch to Terminal.app
    typeInTerminal(fullPrompt);
    log(`DISPATCHED: Mission #${num} sent to Antigravity terminal`);

    // Monitor CC CLI process state
    const deadline = Date.now() + timeoutMs;
    let wasBusy = false;
    let idleCount = 0;
    await sleep(8000);

    while (Date.now() < deadline) {
        const alive = isBrainAlive();
        const elapsedSec = Math.round((Date.now() - startTime) / 1000);

        if (!alive && wasBusy) {
            log(`COMPLETE: Mission #${num} — CC CLI ended (${elapsedSec}s)`);
            return { success: true, result: 'done', elapsed: elapsedSec };
        }

        if (alive) {
            try {
                const cpu = parseFloat(execSync(
                    'ps -p $(pgrep -f "claude.*dangerously-skip-permissions" | head -1) -o %cpu= 2>/dev/null',
                    { encoding: 'utf-8', timeout: 3000 }
                ).trim()) || 0;

                if (cpu > 5) {
                    wasBusy = true;
                    idleCount = 0;
                    if (elapsedSec % 30 === 0) log(`BUSY: Mission #${num} (CPU:${cpu}%, ${elapsedSec}s)`);
                } else if (wasBusy) {
                    idleCount++;
                    if (idleCount >= 6) {
                        log(`COMPLETE: Mission #${num} — idle after processing (${elapsedSec}s)`);
                        return { success: true, result: 'done', elapsed: elapsedSec };
                    }
                }
            } catch (e) {
                if (wasBusy) {
                    log(`COMPLETE: Mission #${num} — process ended (${elapsedSec}s)`);
                    return { success: true, result: 'done', elapsed: elapsedSec };
                }
            }
        }

        await sleep(5000);
    }

    const elapsed = Math.round((Date.now() - startTime) / 1000);
    log(`TIMEOUT: Mission #${num} (${Math.round(timeoutMs / 1000)}s)`);
    return { success: false, result: 'timeout', elapsed };
}

module.exports = { spawnBrain, killBrain, isBrainAlive, runMission, log };
```

## File: `lib/m1-cooling-daemon.js`
```javascript
/**
 * M1 Cooling Daemon — Thermal protection + dispatch pause gate
 *
 * Monitors load average and free RAM every COOLING_INTERVAL_MS (90s).
 * When overheating: sets pause flag, kills resource hogs, purges caches.
 * Task queue and auto-CTO check isOverheating() before dispatching.
 *
 * Pre-dispatch gate (waitForSafeTemperature):
 *   Blocks until load < 7 AND free RAM > 300MB.
 *   Logs thermal status every 30s to ~/tom_hum_thermal.log.
 *
 * Thresholds:
 *   OVERHEAT: load > 7 OR free RAM < 50MB → pause dispatch
 *   SAFE:     load < 5 AND free RAM > 100MB → resume dispatch
 *   NOTE: macOS aggressively caches files in RAM, so Pages free is typically
 *         50-200MB even when healthy. Only trigger on truly critical levels.
 */

const { execSync } = require('child_process');
const fs = require('fs');
const config = require('../config');
// Import log lazily to avoid circular dependency
let _log;
function log(msg) {
  if (!_log) _log = require('./brain-tmux').log;
  _log(msg);
}

const THERMAL_LOG = config.THERMAL_LOG || 'path.join(os.homedir(), 'tom_hum_thermal.log')';
const OVERHEAT_LOAD = 10;
const OVERHEAT_RAM_MB = 20;   // Even lower threshold for M1 Max
const SAFE_LOAD = 8;
const SAFE_RAM_MB = 50;      // Resume when free RAM > 50MB

let coolingCycle = 0;
let intervalRef = null;
let thermalLogRef = null;
let overheating = false;

// --- System metrics ---

function getLoadAverage() {
  try {
    const raw = execSync('sysctl -n vm.loadavg 2>/dev/null', { encoding: 'utf-8', timeout: 5000 }).trim();
    const match = raw.match(/([\d.]+)\s+([\d.]+)\s+([\d.]+)/);
    return match ? parseFloat(match[1]) : 0;
  } catch (e) { return 0; }
}

function getFreeRAM() {
  try {
    const raw = execSync('vm_stat 2>/dev/null | head -5', { encoding: 'utf-8', timeout: 5000 });
    const match = raw.match(/Pages free:\s+(\d+)/);
    return match ? Math.round((parseInt(match[1]) * 16384) / 1024 / 1024) : -1;
  } catch (e) { return -1; }
}

function hasThermalWarning() {
  try {
    const raw = execSync('pmset -g therm 2>/dev/null', { encoding: 'utf-8', timeout: 5000 });
    return raw.includes('CPU_Scheduler_Limit') || raw.includes('Speed_Limit');
  } catch (e) { return false; }
}

// --- Thermal logging (every 30s) ---

function logThermalStatus() {
  const load1 = getLoadAverage();
  const freeMB = getFreeRAM();
  const thermal = hasThermalWarning();
  const emoji = overheating ? '🔴' : load1 > OVERHEAT_LOAD ? '🟡' : '🟢';
  const line = `[${new Date().toISOString()}] ${emoji} load=${load1} ram=${freeMB}MB thermal=${thermal} paused=${overheating}\n`;
  try { fs.appendFileSync(THERMAL_LOG, line); } catch (e) { }
}

// --- Resource cleanup ---

const RESOURCE_HOGS = ['pyrefly', 'pyright', 'eslint_d', 'prettierd'];

function killResourceHogs() {
  for (const proc of RESOURCE_HOGS) {
    try {
      const pids = execSync(`pgrep -f "${proc}" 2>/dev/null`, { encoding: 'utf-8' }).trim();
      if (pids) {
        execSync(`pkill -f "${proc}" 2>/dev/null`);
        log(`KILLED ${proc}`);
      }
    } catch (e) { }
  }
}

function purgeSystemCaches() {
  const cachePaths = [
    '~/Library/Caches/com.apple.dt.*',
    '~/Library/Caches/node*',
    '~/Library/Caches/typescript',
  ];
  try {
    execSync(`rm -rf ${cachePaths.join(' ')} 2>/dev/null`, { timeout: 10000 });
  } catch (e) { }
  try {
    execSync('purge 2>/dev/null', { timeout: 10000 });
    log('RAM purge executed');
  } catch (e) { }
}

// --- Overheat detection ---

function checkOverheatStatus() {
  const load1 = getLoadAverage();
  const freeMB = getFreeRAM();
  const thermal = hasThermalWarning();

  const isOverheated = load1 > OVERHEAT_LOAD || (freeMB >= 0 && freeMB < OVERHEAT_RAM_MB) || thermal;
  const isSafe = load1 < SAFE_LOAD && (freeMB < 0 || freeMB > SAFE_RAM_MB);

  // Hysteresis: only change state at clear thresholds
  if (isOverheated && !overheating) {
    overheating = true;
    log(`OVERHEAT DETECTED — Load: ${load1} | RAM: ${freeMB}MB | Thermal: ${thermal} — PAUSING DISPATCH`);
    killResourceHogs();
    purgeSystemCaches();
  } else if (isSafe && overheating) {
    overheating = false;
    log(`COOLED DOWN — Load: ${load1} | RAM: ${freeMB}MB — RESUMING DISPATCH`);
  }

  return { load1, freeMB, thermal, overheating };
}

// --- Public API ---

/** Returns true if system is overheating and dispatch should be paused */
function isOverheating() { return overheating; }

/**
 * Pre-dispatch gate: blocks until load < 7 AND free RAM > 300MB.
 * Called before spawning each claude -p mission.
 * @returns {Promise<void>}
 */
async function waitForSafeTemperature() {
  let load1 = getLoadAverage();
  // Maintenance: Kill hogs even if not blocking
  if (load1 >= OVERHEAT_LOAD) killResourceHogs();
  // NEVER BLOCK: AGI must be immortal
  return;
}

/**
 * Legacy gate for backward compatibility with task-queue.js
 * @returns {Promise<void>}
 */
async function pauseIfOverheating() {
  if (!overheating) return;
  log('THERMAL PAUSE — waiting for system to cool down...');
  while (overheating) {
    await new Promise(r => setTimeout(r, 60000));
    checkOverheatStatus();
    if (overheating) {
      const load1 = getLoadAverage();
      const freeMB = getFreeRAM();
      log(`Still hot — Load: ${load1} | RAM: ${freeMB}MB — waiting 60s more`);
      killResourceHogs();
    }
  }
  log('THERMAL PAUSE LIFTED — dispatch resuming');
}

function startCooling() {
  // Main cooling cycle (every 90s)
  intervalRef = setInterval(() => {
    coolingCycle++;
    const { load1, freeMB } = checkOverheatStatus();
    const emoji = load1 > OVERHEAT_LOAD ? '🔴' : load1 > SAFE_LOAD ? '🟡' : '🟢';
    log(`COOLING #${coolingCycle} ${emoji} Load: ${load1} | RAM: ${freeMB}MB${overheating ? ' | PAUSED' : ''}`);
  }, config.COOLING_INTERVAL_MS);

  // Thermal log (every 30s)
  thermalLogRef = setInterval(logThermalStatus, 30000);
  logThermalStatus(); // Log immediately on start
}

function stopCooling() {
  if (intervalRef) { clearInterval(intervalRef); intervalRef = null; }
  if (thermalLogRef) { clearInterval(thermalLogRef); thermalLogRef = null; }
}

module.exports = { startCooling, stopCooling, isOverheating, pauseIfOverheating, waitForSafeTemperature };
```

## File: `lib/mission-complexity-classifier.js`
```javascript
/**
 * Mission Complexity Classifier — Routes missions to appropriate execution format
 *
 * ALL levels use /cook ClaudeKit command to ensure proper workflow activation.
 *
 * SIMPLE  → /cook "task"                        (single agent, 15 phút)
 * MEDIUM  → /cook "task" --auto                  (sub-agents, 30 phút)
 * COMPLEX → /cook with Agent Team instructions   (4+ parallel Task subagents, 45 phút)
 */

const config = require('../config');

const VI_PREFIX = 'Trả lời bằng TIẾNG VIỆT. ';
const FILE_LIMIT = 'Chỉ sửa TỐI ĐA 5 file mỗi mission. Nếu cần sửa nhiều hơn, báo cáo danh sách còn lại.';
const NO_GIT = 'CRITICAL: DO NOT run git commit, git push, or /check-and-commit. The CI/CD gate handles git operations.';

/**
 * Classify mission complexity based on task metadata and keyword analysis.
 * @param {object} task - Task object from BINH_PHAP_TASKS ({id, cmd, complexity?})
 * @param {string} project - Project name for scope context
 * @returns {'simple'|'medium'|'complex'}
 */
function classifyComplexity(task, project) {
  if (task.complexity) return task.complexity;
  const text = `${task.cmd} ${task.id}`.toLowerCase();
  if (config.COMPLEXITY.COMPLEX_KEYWORDS.some(kw => text.includes(kw))) return 'complex';
  if (config.COMPLEXITY.MEDIUM_KEYWORDS.some(kw => text.includes(kw))) return 'medium';
  return 'simple';
}

/**
 * Get timeout for a given complexity level.
 * @param {'simple'|'medium'|'complex'} complexity
 * @returns {number} Timeout in milliseconds
 */
function getTimeoutForComplexity(complexity) {
  if (complexity === 'complex') return config.TIMEOUT_COMPLEX;
  if (complexity === 'medium') return config.TIMEOUT_MEDIUM;
  return config.TIMEOUT_SIMPLE;
}

/**
 * Classify raw mission text and return appropriate timeout.
 * Used by task-queue for dynamic timeout on any mission content.
 * @param {string} text - Raw mission file content
 * @returns {{ complexity: string, timeout: number }}
 */
function classifyContentTimeout(text) {
  const lower = text.toLowerCase();
  if (config.COMPLEXITY.COMPLEX_KEYWORDS.some(kw => lower.includes(kw))) {
    return { complexity: 'complex', timeout: config.TIMEOUT_COMPLEX };
  }
  if (config.COMPLEXITY.MEDIUM_KEYWORDS.some(kw => lower.includes(kw))) {
    return { complexity: 'medium', timeout: config.TIMEOUT_MEDIUM };
  }
  return { complexity: 'simple', timeout: config.TIMEOUT_SIMPLE };
}

/**
 * Build Agent Team instruction block for complex missions.
 * Tells CC CLI to spawn parallel Task subagents via the native Task tool.
 * @param {string} taskId - Task identifier for role lookup
 * @returns {string} Agent Team instruction text
 */
function buildAgentTeamBlock(taskId) {
  const roles = config.AGENT_TEAM_ROLES[taskId] || config.AGENT_TEAM_ROLES.default;
  const roleList = roles.map((r, i) => `(${i + 1}) ${r}`).join(', ');
  return [
    'AGENT TEAM: Activate Agent Teams.',
    `Spawn ${roles.length} parallel subagents: ${roleList}.`,
    'Launch them in parallel.',
    'Wait for all to complete, then consolidate findings.',
    'IMPORTANT: DO NOT use XML tags like <invoke>. Use natural language or slash commands only.',
  ].join(' ');
}

/**
 * Generate the mission prompt with Phong Lâm Hỏa Sơn (風林火山) token optimization.
 *
 * 🌪️ GIÓ (SIMPLE):  --fast --no-test  → 30% tokens, speed run
 * 🌲 RỪNG (MEDIUM): --auto            → 60% tokens, standard quality
 * 🔥 LỬA (COMPLEX): --parallel teams  → 100% tokens, maximum power
 * ⛰️ NÚI (IDLE):    queue scan        → 0 tokens
 *
 * @param {object} task - Task object ({id, cmd, complexity?})
 * @param {string} project - Target project name
 * @param {'simple'|'medium'|'complex'} complexity - Classified complexity
 * @returns {{ prompt: string, timeout: number, mode: string }} Formatted mission prompt + timeout + binh phap mode
 */
function generateMissionPrompt(task, project, complexity) {
  const mission = `${VI_PREFIX}${task.cmd} in ${project}. ${FILE_LIMIT} ${NO_GIT}`;
  const timeout = getTimeoutForComplexity(complexity);

  // 🔥 LỬA mode — Complex: Agent Teams parallel, max token burn, max output
  if (complexity === 'complex') {
    const teamBlock = buildAgentTeamBlock(task.id);
    return { prompt: `/cook "${mission} ${teamBlock}" --auto`, timeout, mode: '🔥LỬA' };
  }

  // 🌲 RỪNG mode — Medium: standard /cook with auto, balanced
  if (complexity === 'medium') {
    return { prompt: `/cook "${mission}" --auto`, timeout, mode: '🌲RỪNG' };
  }

  // 🌪️ GIÓ mode — Simple: fast + no-test, minimum token burn, maximum speed
  return { prompt: `/cook "${mission}" --fast --no-test --auto`, timeout, mode: '🌪️GIÓ' };
}

/**
 * Check if a mission prompt is a team/complex mission (for timeout decisions).
 * @param {string} prompt - The full mission prompt text
 * @returns {boolean}
 */
function isTeamMission(prompt) {
  const lower = prompt.toLowerCase();
  return lower.includes('agent team') ||
    lower.includes('parallel task subagents') ||
    lower.includes('scope: thorough') ||
    lower.includes('teammates');
}

module.exports = { classifyComplexity, generateMissionPrompt, isTeamMission, buildAgentTeamBlock, classifyContentTimeout, getTimeoutForComplexity };
```

## File: `lib/mission-dispatcher.js`
```javascript
/**
 * 🚀 Mission Dispatcher v3 — Agent Team aware prompt building
 *
 * Routes tasks to project directories, builds prompts, and executes
 * missions via brain-process-manager's runMission().
 *
 * v1: Wrote mission to /tmp file → expect brain read it → file IPC polling
 * v2: Calls runMission() directly → Node.js child_process → exit code
 * v3: Complex missions get Agent Team prompts → parallel Task subagents
 */

const path = require('path');
const config = require('../config');
const { log, runMission } = require('./brain-vscode-terminal');
const { isTeamMission, buildAgentTeamBlock } = require('./mission-complexity-classifier');

const VI_PREFIX = 'Trả lời bằng TIẾNG VIỆT. ';
const FILE_LIMIT = 'Chỉ sửa TỐI ĐA 5 file mỗi mission. Nếu cần sửa nhiều hơn, báo cáo danh sách còn lại.';

// Project routing: detect project from task content keywords
function detectProjectDir(taskContent) {
  const lower = taskContent.toLowerCase();
  const routes = {
    '84tea': 'apps/84tea',
    apex: 'apps/apex-os',
    anima: 'apps/anima119',
    sophia: 'apps/sophia-ai-factory',
    well: 'apps/well',
    agency: 'apps/agencyos-web',
    'sa-dec': 'apps/sa-dec-flower-hunt',
    'flower': 'apps/sa-dec-flower-hunt',
    mekong: '.',
  };
  for (const [keyword, dir] of Object.entries(routes)) {
    if (lower.includes(keyword)) return path.join(config.MEKONG_DIR, dir);
  }
  return config.MEKONG_DIR;
}

/**
 * Check if raw task text is complex based on config keywords.
 * @param {string} text - Sanitized task text (lowercase)
 * @returns {boolean}
 */
function isComplexRawMission(text) {
  return config.COMPLEXITY.COMPLEX_KEYWORDS.some(kw => text.includes(kw));
}

/**
 * Build prompt from raw task content.
 * - If task already has /binh-phap or /cook → pass through unchanged
 * - If task matches complex keywords → wrap with Agent Team instructions
 * - Otherwise → standard /binh-phap + /cook wrapper
 */
const MONOREPO_RULE = 'CẤM chạy `npm install/test/build` bên trong folder con. PHẢI chạy từ ROOT dùng flag `--workspace` (VD: `npm install -w apps/84tea`). ';

function buildPrompt(taskContent) {
  let clean = taskContent.replace(/\\!/g, '!').replace(/\\"/g, '"').trim();
  // Strip project routing prefix (e.g. "sophia: " at start)
  clean = clean.replace(/^[a-z0-9_-]+:\s*/i, '');
  const safe = clean.replace(/[()$`\\!]/g, ' ').replace(/\s+/g, ' ').trim();

  // Don't double-wrap if already has /binh-phap or /cook
  if (safe.includes('/binh-phap') || safe.includes('/cook')) return `${MONOREPO_RULE}${safe}`;

  // Complex raw missions → Agent Team prompt
  const lower = safe.toLowerCase();
  if (isComplexRawMission(lower)) {
    const teamBlock = buildAgentTeamBlock('default');
    return `/cook "${VI_PREFIX}${MONOREPO_RULE}${safe}. ${FILE_LIMIT} ${teamBlock}" --auto`;
  }

  return `/cook "${VI_PREFIX}${MONOREPO_RULE}${safe}. ${FILE_LIMIT}" --auto`;
}

/**
 * Full dispatch flow: detect project → build prompt → run via brain
 *
 * @param {string} taskContent - Raw task file content
 * @param {string} taskFile - Task filename (for logging)
 * @param {number} [timeoutMs] - Override timeout from classifier (optional)
 * @returns {Promise<{success: boolean, result: string, elapsed: number}>}
 */
async function executeTask(taskContent, taskFile, timeoutMs, complexity) {
  const projectDir = detectProjectDir(taskContent);
  const prompt = buildPrompt(taskContent);
  const finalTimeout = timeoutMs || (isTeamMission(prompt) ? config.AGENT_TEAM_TIMEOUT_MS : config.MISSION_TIMEOUT_MS);
  const mode = isTeamMission(prompt) ? 'AGENT_TEAM' : 'SINGLE';

  // 虛實 Model Routing: Opus only for complex, qwen3 for rest
  let modelOverride = null;
  if (complexity === 'complex') {
    modelOverride = config.OPUS_MODEL;
    log(`🔥 OPUS ACTIVATED: ${modelOverride} — Complex mission requires Ultra power`);
  }

  log(`PROMPT [${mode}]: ${prompt.slice(0, 150)}... [timeout=${Math.round(finalTimeout / 60000)}min] [model=${modelOverride || config.MODEL_NAME}]`);

  const result = await runMission(prompt, projectDir, finalTimeout, modelOverride);

  // 虛實: Switch back to default model after Opus mission
  if (modelOverride) {
    log(`🔥→🌲 Opus mission done — switching back to ${config.MODEL_NAME}`);
    // Model switch back happens at next runMission start (no explicit /model needed)
  }

  return result;
}

module.exports = { executeTask, buildPrompt, detectProjectDir };
```

## File: `lib/self-healer.js`
```javascript
/**
 * 🩺 Self-Healer v1.0 — Autonomous CC CLI + Proxy Recovery
 *
 * 4 subsystems:
 *   1. CC CLI Health Monitor — detect stuck/crash → auto-restart tmux
 *   2. Proxy Health Gate    — check proxy alive before dispatch
 *   3. Model Fallback       — if model rejected → try backup chain
 *   4. Telegram Escalation  — alert when self-heal fails
 *
 * v2026.2.13 upstream sync: crash recovery, zombie cleanup
 */

const { execSync } = require('child_process');
const http = require('http');
const config = require('../config');
const { sendTelegram } = require('./telegram-client');

// Lazy imports to avoid circular deps
let brainTmux = null;
function getBrain() {
    if (!brainTmux) brainTmux = require('./brain-tmux');
    return brainTmux;
}

// ═══════════════════════════════════════
// CONFIG
// ═══════════════════════════════════════

const HEALTH_CHECK_INTERVAL_MS = 30_000;      // Check CC CLI every 30s
const PROXY_TIMEOUT_MS = 5_000;               // Proxy ping timeout
const MAX_RECOVERY_ATTEMPTS = 3;              // Before escalating
const STALE_OUTPUT_THRESHOLD_MS = 3 * 60_000; // 3 min no new output → stuck
const MODEL_FALLBACK_CHAIN = [
    config.MODEL_NAME,                          // claude-sonnet-4-5
    config.FALLBACK_MODEL_NAME,                 // gemini-3-flash
    config.QWEN_MODEL_NAME,                     // qwen3-coder-next
];

// ═══════════════════════════════════════
// STATE
// ═══════════════════════════════════════

let monitorRef = null;
let lastOutputHash = '';
let lastOutputTime = Date.now();
let consecutiveFailures = 0;
let currentModelIdx = 0;

function log(msg) {
    getBrain().log(`[HEALER] ${msg}`);
}

// ═══════════════════════════════════════
// 1. CC CLI HEALTH MONITOR
// ═══════════════════════════════════════

function checkCCCLIHealth() {
    try {
        const { isBrainAlive, capturePane, isShellPrompt, isStuck } = getBrain();

        // Check tmux session alive
        if (!isBrainAlive || (typeof isBrainAlive === 'function' && !isBrainAlive())) {
            log('❌ CC CLI tmux session DEAD');
            return { healthy: false, reason: 'session_dead' };
        }

        const output = capturePane();
        if (!output || output.trim().length === 0) {
            log('⚠️ CC CLI output empty');
            return { healthy: false, reason: 'no_output' };
        }

        // Check if dropped to shell
        if (isShellPrompt(output)) {
            log('❌ CC CLI dropped to shell prompt');
            return { healthy: false, reason: 'shell_prompt' };
        }

        // Check if stuck in TUI menu
        if (isStuck(output)) {
            log('⚠️ CC CLI stuck in TUI menu');
            return { healthy: false, reason: 'stuck_tui' };
        }

        // Check for stale output (no change for 3 min)
        const outputHash = simpleHash(output.slice(-500));
        if (outputHash === lastOutputHash) {
            const staleDuration = Date.now() - lastOutputTime;
            if (staleDuration > STALE_OUTPUT_THRESHOLD_MS) {
                log(`⚠️ CC CLI stale output for ${Math.round(staleDuration / 1000)}s`);
                return { healthy: false, reason: 'stale_output' };
            }
        } else {
            lastOutputHash = outputHash;
            lastOutputTime = Date.now();
        }

        // Check for model rejection
        const modelRejected = /Model.*not found|not supported|issue with.*selected model/i.test(output);
        if (modelRejected) {
            log('⚠️ CC CLI model rejected');
            return { healthy: false, reason: 'model_rejected' };
        }

        return { healthy: true };
    } catch (e) {
        log(`Health check error: ${e.message}`);
        return { healthy: false, reason: 'check_error' };
    }
}

function simpleHash(str) {
    let h = 0;
    for (let i = 0; i < str.length; i++) {
        h = ((h << 5) - h + str.charCodeAt(i)) | 0;
    }
    return h.toString(36);
}

// ═══════════════════════════════════════
// 2. PROXY HEALTH GATE
// ═══════════════════════════════════════

function checkProxyHealth() {
    return new Promise((resolve) => {
        const url = new URL('/v1/models', config.CLOUD_BRAIN_URL);
        const req = http.get(url, { timeout: PROXY_TIMEOUT_MS }, (res) => {
            let data = '';
            res.on('data', (chunk) => data += chunk);
            res.on('end', () => {
                if (res.statusCode === 200) {
                    resolve({ healthy: true, models: data });
                } else {
                    resolve({ healthy: false, reason: `status_${res.statusCode}` });
                }
            });
        });
        req.on('error', (e) => resolve({ healthy: false, reason: e.message }));
        req.on('timeout', () => {
            req.destroy();
            resolve({ healthy: false, reason: 'timeout' });
        });
    });
}

async function restartProxy() {
    log('🔄 Attempting proxy restart...');
    try {
        // Find and kill existing proxy process
        try {
            execSync('pkill -f "anthropic-adapter" 2>/dev/null', { timeout: 5000 });
        } catch (e) { /* may not be running */ }

        await new Promise(r => setTimeout(r, 3000));

        // Restart proxy
        const proxyScript = `${config.MEKONG_DIR}/scripts/anthropic-adapter.js`;
        execSync(`node ${proxyScript} &`, {
            cwd: config.MEKONG_DIR,
            timeout: 10000,
            stdio: 'ignore',
            detached: true,
        });

        await new Promise(r => setTimeout(r, 5000));

        const recheck = await checkProxyHealth();
        if (recheck.healthy) {
            log('✅ Proxy restarted successfully');
            return true;
        }
        log('❌ Proxy still down after restart');
        return false;
    } catch (e) {
        log(`Proxy restart failed: ${e.message}`);
        return false;
    }
}

// ═══════════════════════════════════════
// 3. MODEL FALLBACK
// ═══════════════════════════════════════

function getNextModel() {
    currentModelIdx = (currentModelIdx + 1) % MODEL_FALLBACK_CHAIN.length;
    return MODEL_FALLBACK_CHAIN[currentModelIdx];
}

function getCurrentModel() {
    return MODEL_FALLBACK_CHAIN[currentModelIdx];
}

function resetModelChain() {
    currentModelIdx = 0;
}

// ═══════════════════════════════════════
// 4. TELEGRAM ESCALATION
// ═══════════════════════════════════════

function escalate(errorType, details) {
    const msg = `🚨 *TÔM HÙM ALERT*\n\n` +
        `Error: \`${errorType}\`\n` +
        `Retries: ${consecutiveFailures}/${MAX_RECOVERY_ATTEMPTS}\n` +
        `Details: ${details.slice(0, 200)}\n` +
        `Time: ${new Date().toISOString().slice(11, 19)}`;

    sendTelegram(msg);
    log(`📱 Telegram alert sent: ${errorType}`);
}

// ═══════════════════════════════════════
// RECOVERY ENGINE
// ═══════════════════════════════════════

async function recover(reason) {
    consecutiveFailures++;
    log(`🔧 Recovery attempt ${consecutiveFailures}/${MAX_RECOVERY_ATTEMPTS} — reason: ${reason}`);

    if (consecutiveFailures > MAX_RECOVERY_ATTEMPTS) {
        escalate(reason, `Failed ${consecutiveFailures} times. Manual intervention needed.`);
        consecutiveFailures = 0; // Reset to try again later
        return false;
    }

    switch (reason) {
        case 'session_dead':
        case 'shell_prompt':
        case 'no_output': {
            log('🔄 Respawning CC CLI brain...');
            try {
                const { respawnBrain } = getBrain();
                if (typeof respawnBrain === 'function') {
                    await respawnBrain(true);
                    log('✅ Brain respawned');
                    consecutiveFailures = 0;
                    return true;
                }
            } catch (e) {
                log(`Brain respawn failed: ${e.message}`);
            }
            return false;
        }

        case 'stuck_tui': {
            log('🔄 Sending Escape + Ctrl-C to unstick TUI...');
            try {
                const { sendCtrlC } = getBrain();
                sendCtrlC();
                await new Promise(r => setTimeout(r, 2000));
                sendCtrlC();
                await new Promise(r => setTimeout(r, 2000));
                consecutiveFailures = 0;
                return true;
            } catch (e) {
                log(`Unstick failed: ${e.message}`);
            }
            return false;
        }

        case 'stale_output': {
            // Maybe just slow — send Enter to kick
            log('🔄 Kicking stale session with Enter...');
            try {
                const { sendEnter } = getBrain();
                if (typeof sendEnter === 'function') sendEnter();
                lastOutputTime = Date.now(); // Reset timer
                return true;
            } catch (e) {
                log(`Kick failed: ${e.message}`);
            }
            return false;
        }

        case 'model_rejected': {
            const nextModel = getNextModel();
            log(`🔄 Model fallback: trying ${nextModel}`);
            try {
                const { respawnBrain } = getBrain();
                // Update MODEL_NAME in config for next spawn
                config.MODEL_NAME = nextModel;
                if (typeof respawnBrain === 'function') {
                    await respawnBrain(false);
                    log(`✅ Switched to model: ${nextModel}`);
                    consecutiveFailures = 0;
                    return true;
                }
            } catch (e) {
                log(`Model switch failed: ${e.message}`);
            }
            return false;
        }

        case 'proxy_down': {
            const restarted = await restartProxy();
            if (restarted) {
                consecutiveFailures = 0;
                return true;
            }
            return false;
        }

        default:
            log(`Unknown recovery reason: ${reason}`);
            return false;
    }
}

// ═══════════════════════════════════════
// PUBLIC API
// ═══════════════════════════════════════

/**
 * Pre-flight check: call before every mission dispatch.
 * Checks proxy + CC CLI health. Auto-recovers if possible.
 * @returns {Promise<boolean>} true = safe to dispatch
 */
async function preFlightCheck() {
    // 1. Check proxy only (CC CLI health check disabled — uses unexported brain-tmux internals)
    const proxyHealth = await checkProxyHealth();
    if (!proxyHealth.healthy) {
        log(`PRE-FLIGHT: Proxy unhealthy — ${proxyHealth.reason}`);
        const recovered = await recover('proxy_down');
        if (!recovered) return false;
    }

    return true;
}

/**
 * Report a mission failure for tracking.
 * Triggers recovery if pattern detected.
 */
async function reportFailure(taskFile, error) {
    const msg = error?.message || String(error);
    log(`FAILURE REPORT: ${taskFile} — ${msg.slice(0, 150)}`);

    // Detect specific failure patterns
    if (/brain_died|respawn/i.test(msg)) {
        await recover('session_dead');
    } else if (/timeout/i.test(msg)) {
        await recover('stale_output');
    } else if (/model/i.test(msg)) {
        await recover('model_rejected');
    }
}

/**
 * Background health monitor — runs every 30s.
 */
function startMonitor() {
    log('🩺 Health Monitor started (proxy-only mode)');
    // CC CLI health monitor disabled — uses unexported brain-tmux internals
    // Only proxy health is checked via preFlightCheck before each dispatch
}

function stopMonitor() {
    if (monitorRef) {
        clearInterval(monitorRef);
        monitorRef = null;
        log('🩺 Health Monitor stopped');
    }
}

module.exports = {
    preFlightCheck,
    reportFailure,
    startMonitor,
    stopMonitor,
    checkProxyHealth,
    checkCCCLIHealth,
    getCurrentModel,
    resetModelChain,
    escalate,
};
```

## File: `lib/task-queue.js`
```javascript
const fs = require('fs');
const path = require('path');
const config = require('../config');
const { log } = require('./brain-tmux');
const { checkSafety } = require('./safety-guard');
const { executeTask, detectProjectDir } = require('./mission-dispatcher');
const { classifyContentTimeout } = require('./mission-complexity-classifier');
const { pauseIfOverheating, waitForSafeTemperature } = require('./m1-cooling-daemon');
const { runFullGate } = require('./post-mission-gate');
const { preFlightCheck, reportFailure } = require('./self-healer');
const { sendTelegram } = require('./telegram-client');

let isProcessing = false; // Legacy lock (unused but kept for safety reference)
let activeMissions = 0;   // 🚀 WARP SPEED: Track active parallel missions
let currentTaskFile = null; // Only tracks the *latest* dispatched task (for logging)
const queue = [];
const processingFiles = new Set(); // 🚀 FIX: Track files in-flight to prevent re-queueing
let pollIntervalRef = null;
let watcher = null;

async function processQueue() {
  // 🚀 WARP SPEED: Loop until we hit concurrency limit or queue empty
  while (queue.length > 0 && activeMissions < (config.MAX_CONCURRENT_MISSIONS || 3)) {

    // Thermal gate: block NEW missions if system is overheating
    // (Existing running missions continue)
    const isHot = await pauseIfOverheating();
    if (isHot) {
      await waitForSafeTemperature();
    }

    // v2026.2.13: Pre-flight health check (proxy + CC CLI)
    // We check once per dispatch to ensure we don't spawn into a dead system
    const healthy = await preFlightCheck();
    if (!healthy) {
      log(`PRE-FLIGHT FAILED: ${queue[0] || 'unknown'} — halting dispatch for 30s`);
      setTimeout(processQueue, 30000); // Retry later
      return;
    }

    const taskFile = queue.shift();
    if (processingFiles.has(taskFile)) {
      log(`SKIPPED DUPLICATE: ${taskFile} is already running`);
      continue;
    }

    processingFiles.add(taskFile); // Mark as processing
    currentTaskFile = taskFile; // For logging purpose
    const filePath = path.join(config.WATCH_DIR, taskFile);

    // Increment counter *before* async work start
    activeMissions++;
    log(`🚀 DISPATCHING: ${taskFile} (Active: ${activeMissions}/${config.MAX_CONCURRENT_MISSIONS || 3})`);

    // ASYNC EXECUTION (Do NOT await here, or we block the loop)
    // We launch the mission and attach a .finally() handler to decrement counter
    (async () => {
      try {
        if (!fs.existsSync(filePath)) {
          log(`Ghost file ignored: ${taskFile}`);
          return;
        }
        const content = fs.readFileSync(filePath, 'utf-8').trim();

        // --- 🛡️ SAFETY GATE (Phase 1) ---
        const safety = await checkSafety(content);
        if (!safety.safe) {
           log(`🛑 SAFETY BLOCK: ${taskFile} rejected. Reason: ${safety.reason}`);
           sendTelegram(`🛑 *SAFETY BLOCK*: \`${taskFile}\`\nReason: ${safety.reason}`);

           // Ensure rejected dir exists (double check)
           if (!fs.existsSync(config.REJECTED_DIR)) {
              fs.mkdirSync(config.REJECTED_DIR, { recursive: true });
           }
           fs.renameSync(filePath, path.join(config.REJECTED_DIR, taskFile));
           return;
        }
        // --------------------------------

        const { complexity, timeout } = classifyContentTimeout(content);
        log(`EXECUTING [${complexity.toUpperCase()}/${Math.round(timeout / 60000)}min]: ${taskFile}`);
        sendTelegram(`🦞 *STARTED* [${complexity.toUpperCase()}]: \`${taskFile}\`\n⏳ Timeout: ${Math.round(timeout / 60000)}m\n🚀 Active: ${activeMissions}`);

        const result = await executeTask(content, taskFile, timeout, complexity);

        // === 軍形 CI/CD GATE ===
        let gateStatus = "Skipped";
        if (result && result.success) {
          const projectMatch = taskFile.match(/^(?:HIGH_|MEDIUM_|LOW_)?mission_([a-z0-9_-]+?)_(?:auto_)?/i);
          // Alias map: project names that share a codebase with another project
          const PROJECT_ALIASES = { 'wellnexus': 'anima119' };
          const rawProject = projectMatch ? projectMatch[1].replace(/_/g, '-') : null;
          const project = rawProject ? (PROJECT_ALIASES[rawProject] || rawProject) : null;
          const missionId = taskFile.replace(/^.*?_auto_/, '').replace('.txt', '');

          if (project) {
            log(`GATE: 軍形 verify for ${project}/${missionId}...`);
            const gate = runFullGate(project, missionId);
            if (gate.build) {
              const pushMsg = gate.pushed ? 'PUSHED' : 'no changes';
              log(`GATE: ✅ GREEN — ${pushMsg}`);
              gateStatus = `✅ GREEN (${pushMsg})`;
            } else {
              log(`GATE: ❌ RED — build failed, NOT pushing`);
              gateStatus = "❌ RED (Build Failed)";
            }
          }
        }

        if (fs.existsSync(filePath)) {
          // v2026.2.14: Fast-failure (quota) protection — do NOT archive, keep for retry
          if (result && result.result === 'fast_failure') {
            log(`RETRY: ${taskFile} — fast failure (quota), keeping in queue`);
            return;
          }
          fs.renameSync(filePath, path.join(config.PROCESSED_DIR, taskFile));
          log(`Archived: ${taskFile}`);
        }

        // Telegram Notification
        if (result && result.success) {
          sendTelegram(`✅ *COMPLETED*: \`${taskFile}\`\nGate: ${gateStatus}\n📉 Active: ${activeMissions - 1}`);
        } else {
          sendTelegram(`⚠️ *COMPLETED (With Issues)*: \`${taskFile}\`\nResult: ${JSON.stringify(result)}\n📉 Active: ${activeMissions - 1}`);
        }
      } catch (error) {
        log(`Error processing ${taskFile}: ${error.message}`);
        sendTelegram(`❌ *FAILED*: \`${taskFile}\`\nError: ${error.message}`);
        reportFailure(taskFile, error).catch(() => { });
      } finally {
        activeMissions--;
        processingFiles.delete(taskFile); // Release lock
        log(`🏁 FINISHED: ${taskFile} (Active: ${activeMissions})`);

        // Trigger next dispatch immediately if queue has items
        if (queue.length > 0) {
          processQueue();
        }
      }
    })();

    // Slight delay between parallel launches to prevent TMUX race conditions
    await new Promise(r => setTimeout(r, 2000));
  }
}

function enqueue(filename) {
  if (filename && config.TASK_PATTERN.test(filename)) {
    const filePath = path.join(config.WATCH_DIR, filename);
    // 🚀 FIX: Check processingFiles to avoid double-queueing active tasks
    if (fs.existsSync(filePath) && !queue.includes(filename) && filename !== currentTaskFile && !processingFiles.has(filename)) {
      log(`DETECTED: ${filename}`);
      queue.push(filename);
      // Trigger processing if idle
      processQueue();
    }
  }
}

function startWatching() {
  // Ensure processed dir exists
  if (!fs.existsSync(config.PROCESSED_DIR)) {
    fs.mkdirSync(config.PROCESSED_DIR, { recursive: true });
  }

  // fs.watch for instant detection
  if (fs.existsSync(config.WATCH_DIR)) {
    watcher = fs.watch(config.WATCH_DIR, (eventType, filename) => enqueue(filename));
  }

  // Periodic poll as backup (every 5s) — only log genuinely new tasks
  pollIntervalRef = setInterval(() => {
    try {
      const files = fs.readdirSync(config.WATCH_DIR);
      const tasks = files.filter(f => config.TASK_PATTERN.test(f));
      const newTasks = tasks.filter(f => !queue.includes(f) && f !== currentTaskFile && !processingFiles.has(f));
      if (newTasks.length > 0) {
        log(`Poll found new: ${newTasks.join(', ')}`);
      }
      tasks.forEach(enqueue);
    } catch (e) { }
  }, config.POLL_INTERVAL_MS); // PROJECT FLASH: 200ms Backup Poll
}

function stopWatching() {
  if (pollIntervalRef) {
    clearInterval(pollIntervalRef);
    pollIntervalRef = null;
  }
  if (watcher) {
    watcher.close();
    watcher = null;
  }
}

function isQueueEmpty() { return queue.length === 0 && !isProcessing; }

module.exports = { startWatching, stopWatching, isQueueEmpty, enqueue };
```

