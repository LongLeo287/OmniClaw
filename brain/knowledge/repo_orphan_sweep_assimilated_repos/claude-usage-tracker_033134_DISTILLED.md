---
id: claude-usage-tracker
type: knowledge
owner: OA_Triage
---
# claude-usage-tracker
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# 🧾 Claude Usage Tracker

> Track and visualize Claude AI usage costs across all your local development tools.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-macOS-lightgrey.svg)
![Node](https://img.shields.io/badge/node-%3E%3D16-green.svg)

## Overview

**Claude Usage Tracker** is a local-first tool that automatically discovers and aggregates your Claude AI usage across **9+ development tools**, including:

- **OpenClaw / Clawdbot** — AI agent framework
- **Claude Code CLI** — Anthropic's official CLI
- **Claude Desktop** — Anthropic's desktop app (local agent mode)
- **Cursor** — AI-powered code editor
- **Windsurf** — Codeium's AI IDE
- **Cline** — VS Code Claude extension
- **Roo Code** — VS Code AI assistant
- **Aider** — AI pair programming (litellm)
- **Continue.dev** — Open-source AI code assistant

It scans known data directories, parses JSONL/log files, calculates costs using model-specific pricing, and presents everything in a beautiful **dark-themed interactive dashboard** powered by Chart.js.

No cloud. No telemetry. Everything stays on your machine.

---

## ✨ Features

| Category | Details |
|----------|---------|
| **Multi-Source Tracking** | Auto-detects 9+ Claude-integrated tools and merges usage data |
| **Beautiful Dashboard** | Dark-themed UI with Chart.js visualizations |
| **Cost Breakdown** | Daily, weekly, monthly, and all-time cost tracking |
| **Model Analytics** | Per-model cost breakdown across Opus, Sonnet, and Haiku families |

| **Heatmaps** | Two views — Peak Hours (day × hour grid) and Peak Days (GitHub-style calendar) |
| **Session Log** | Expandable day-by-day session details with color-coded source cards |
| **Projects View** | Group sessions by working directory to see per-project cost breakdown |
| **Filtering** | Multi-criteria filtering (source, model, date range, min cost) with visual chips |
| **Monthly Projections** | Projected monthly cost based on current spending pace |
| **Yesterday Delta** | Compare today's spending vs yesterday at a glance |
| **Most Expensive Session** | Callout highlighting the priciest session of the day |
| **Keyboard Shortcuts** | `Shift+E` to expand/collapse all session rows |
| **macOS App** | Build a standalone `.app` bundle for double-click launching |
| **Animated Counters** | Smooth easing animations on stat cards |
| **Responsive Design** | Adapts to different screen sizes |

---

## 📸 Screenshots

<p align="center">
  <img src="screenshots/dashboard-overview.png" alt="Dashboard Overview" width="800" />
</p>
<p align="center"><em>Dashboard — stats, daily spend chart, source & model breakdowns</em></p>

<p align="center">
  <img src="screenshots/heatmap.png" alt="Peak Hours Heatmap" width="800" />
</p>
<p align="center"><em>Peak Hours heatmap & most expensive session callout</em></p>

<p align="center">
  <img src="screenshots/session-log.png" alt="Session Log" width="800" />
</p>
<p align="center"><em>Session log with filters, expandable day rows, and per-session costs</em></p>

<p align="center">
  <img src="screenshots/projects-view.png" alt="Projects View" width="800" />
</p>
<p align="center"><em>Projects view — see cost breakdown grouped by working directory</em></p>

<p align="center">
  <img src="screenshots/session-detail.png" alt="Session Detail" width="500" />
</p>
<p align="center"><em>Session detail panel — token breakdown, conversation history, resume command</em></p>

---

## 🚀 Quick Start

### Download (Recommended)

**Latest Release: v2.1.0**

| Platform | Download |
|----------|----------|
| macOS (Apple Silicon) | [GitHub](https://github.com/658jjh/claude-usage-tracker/releases/download/v2.1.0/Claude-Usage-Tracker-macOS-AppleSilicon.zip) |
| macOS (Intel) | [GitHub](https://github.com/658jjh/claude-usage-tracker/releases/download/v2.1.0/Claude-Usage-Tracker-macOS-Intel.zip) |

> Requires **Node.js** (v16+) and **macOS 12.0+**

Unzip, drag **Claude Usage Dashboard.app** to Applications, and double-click to launch.

[View all releases →](https://github.com/658jjh/claude-usage-tracker/releases)

### Build from Source

```bash
git clone https://github.com/658jjh/claude-usage-tracker.git
cd claude-usage-tracker
./build-app.sh
```

Then double-click **Claude Usage Dashboard.app** — it collects fresh data and renders everything in a native window.

### Browser Mode (Any OS)

```bash
node collect-usage.js
python3 -m http.server 8765
open http://localhost:8765/dashboard.html
```

---

## 📊 Supported Tools

| Tool | Data Location | Format |
|------|---------------|--------|
| **OpenClaw / Clawdbot** | `~/.openclaw/agents/main/sessions/` or `~/.clawdbot/...` | JSONL |
| **Claude Code CLI** | `~/.claude/projects/` | JSONL |
| **Claude Desktop** | `~/Library/Application Support/Claude/local-agent-mode-sessions/` | JSONL |
| **Cursor** | `~/.cursor/projects/` or `~/Library/Application Support/Cursor/` | JSONL |
| **Windsurf** | `~/.windsurf/` or `~/Library/Application Support/Windsurf/` | JSONL |
| **Cline** | `~/.cline/` or VS Code extension storage | JSONL |
| **Roo Code** | `~/.roo-code/` or VS Code extension storage | JSONL |
| **Aider** | `~/.aider/` | JSONL (litellm) |
| **Continue.dev** | `~/.continue/sessions/` | JSON |

> **Note:** Tool detection is automatic. If a tool isn't installed or has no data, it's silently skipped.

---

## 💰 Pricing Models

Costs are calculated using Anthropic's per-million-token pricing. The tracker supports all current and upcoming model families:

### Current Models

| Model | Input ($/MTok) | Output ($/MTok) | Cache Write ($/MTok) | Cache Read ($/MTok) |
|-------|:--------------:|:---------------:|:--------------------:|:-------------------:|
| **Opus 4.5 / 4.6** | $5.00 | $25.00 | $6.25 | $0.50 |
| **Opus 4.0 / 4.1** | $15.00 | $75.00 | $18.75 | $1.50 |
| **Sonnet 3.5 / 3.7 / 4.0 / 4.5 / 4.6** | $3.00 | $15.00 | $3.75 | $0.30 |
| **Haiku 4.0 / 4.5** | $1.00 | $5.00 | $1.25 | $0.10 |
| **Haiku 3.0 / 3.5** | $0.25 | $1.25 | $0.30 | $0.03 |

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feat/my-feature`
3. **Commit** your changes: `git commit -m "feat: add my feature"`
4. **Push** to your fork: `git push origin feat/my-feature`
5. **Open** a Pull Request

Please follow the existing code style and commit message conventions (`feat:`, `fix:`, `docs:`, `chore:`).

### Ideas for Contributions

- Add support for additional AI tools
- Improve mobile responsiveness
- Add data export (CSV, JSON)
- Add cost alerts / budget thresholds
- Linux / Windows path support
- Electron or Tauri desktop app

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

Built with ❤️ for the Claude community

</div>

```

### File: build-app.sh
```sh
#!/bin/bash
# Build a standalone macOS .app for Claude Usage Dashboard
# Double-click to collect fresh data + view dashboard in a native window.

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
APP_NAME="Claude Usage Dashboard"
APP_DIR="$SCRIPT_DIR/$APP_NAME.app"
CONTENTS="$APP_DIR/Contents"
MACOS="$CONTENTS/MacOS"
RESOURCES="$CONTENTS/Resources"

echo "🔨 Building $APP_NAME.app ..."

# Clean previous build
rm -rf "$APP_DIR"

# Create .app bundle structure
mkdir -p "$MACOS" "$RESOURCES/data"

# ─── Compile native Swift app ─────────────────────────────
echo "⚙️  Compiling native app ..."
swiftc -O \
    -o "$MACOS/ClaudeUsageDashboard" \
    "$SCRIPT_DIR/App.swift" \
    -framework Cocoa \
    -framework WebKit \
    -target "$(uname -m)-apple-macos12.0"
echo "  ✅ Binary compiled"

# Copy the core files into Resources
cp "$SCRIPT_DIR/collect-usage.js" "$RESOURCES/"
cp "$SCRIPT_DIR/dashboard.html" "$RESOURCES/"

# Copy the modular CSS and JS directories
cp -r "$SCRIPT_DIR/css" "$RESOURCES/"
cp -r "$SCRIPT_DIR/js" "$RESOURCES/"

# Create Info.plist
cat > "$CONTENTS/Info.plist" << 'PLIST'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>ClaudeUsageDashboard</string>
    <key>CFBundleName</key>
    <string>Claude Usage Dashboard</string>
    <key>CFBundleDisplayName</key>
    <string>Claude Usage Dashboard</string>
    <key>CFBundleIdentifier</key>
    <string>com.openclaw.usage-dashboard</string>
    <key>CFBundleVersion</key>
    <string>2.0</string>
    <key>CFBundleShortVersionString</key>
    <string>2.0</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleIconFile</key>
    <string>AppIcon</string>
    <key>LSMinimumSystemVersion</key>
    <string>12.0</string>
    <key>NSHighResolutionCapable</key>
    <true/>
</dict>
</plist>
PLIST

# ─── Generate app icon from logo.svg ─────────────────────
SVG="$SCRIPT_DIR/logo.svg"
if [ -f "$SVG" ]; then
    echo "🎨 Generating app icon from logo.svg ..."
    ICONSET="$RESOURCES/AppIcon.iconset"
    mkdir -p "$ICONSET"

    # Render SVG at each required size using Swift (preserves transparency)
    swift - "$SVG" "$ICONSET" << 'SWIFT'
    import Cocoa
    let args = CommandLine.arguments
    let svgPath = args[1]
    let outDir = args[2]
    let sizes = [16, 32, 64, 128, 256, 512, 1024]
    let svgData = try! Data(contentsOf: URL(fileURLWithPath: svgPath))
    let svgImage = NSImage(data: svgData)!
    for size in sizes {
        let s = CGFloat(size)
        let rep = NSBitmapImageRep(
            bitmapDataPlanes: nil, pixelsWide: size, pixelsHigh: size,
            bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true,
            isPlanar: false, colorSpaceName: .deviceRGB,
            bytesPerRow: 0, bitsPerPixel: 0)!
        rep.size = NSSize(width: s, height: s)
        NSGraphicsContext.saveGraphicsState()
        NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: rep)
        svgImage.draw(in: NSRect(x: 0, y: 0, width: s, height: s))
        NSGraphicsContext.restoreGraphicsState()
        let png = rep.representation(using: .png, properties: [:])!
        let outURL = URL(fileURLWithPath: outDir).appendingPathComponent("icon_\(size)x\(size).png")
        try! png.write(to: outURL)
    }
SWIFT

    # Map to Apple's expected @2x naming
    cd "$ICONSET"
    cp icon_32x32.png   icon_16x16@2x.png   2>/dev/null
    cp icon_64x64.png   icon_32x32@2x.png   2>/dev/null
    cp icon_256x256.png icon_128x128@2x.png 2>/dev/null
    cp icon_512x512.png icon_256x256@2x.png 2>/dev/null
    cp icon_1024x1024.png icon_512x512@2x.png 2>/dev/null
    rm -f icon_64x64.png icon_1024x1024.png
    cd "$SCRIPT_DIR"

    # Convert iconset → icns
    if command -v iconutil &>/dev/null; then
        iconutil -c icns "$ICONSET" -o "$RESOURCES/AppIcon.icns" 2>/dev/null \
            && echo "  ✅ AppIcon.icns created" \
            || echo "  ⚠️  iconutil failed — app will use default icon"
    fi
    rm -rf "$ICONSET"
else
    echo "  ⚠️  logo.svg not found — app will use default icon"
fi

# ─── Done ─────────────────────────────────────────────────
echo ""
echo "✅ Built: $APP_DIR"
echo ""
echo "You can now:"
echo "  • Double-click '$APP_NAME.app' in Finder"
echo "  • Drag it to /Applications or your Desktop"
echo "  • It opens as a native app — no browser or Python needed"

```

### File: collect-usage.js
```js
#!/usr/bin/env node
/**
 * Claude Usage Collector v4
 * 
 * Tracks usage across ALL local Claude tools:
 *   ✅ OpenClaw / Clawdbot      (~/.openclaw/ , ~/.clawdbot/)
 *   ✅ Claude Code CLI           (~/.claude/projects/)
 *   ✅ Claude Desktop (Agent)    (~/Library/Application Support/Claude/local-agent-mode-sessions/)
 *   ✅ Cursor                    (~/.cursor/ or ~/Library/Application Support/Cursor/)
 *   ✅ Windsurf                  (~/.windsurf/ or ~/Library/Application Support/Windsurf/)
 *   ✅ Cline (VS Code ext)       (~/.cline/ or VS Code extension storage)
 *   ✅ Roo Code (VS Code ext)    (~/.roo-code/ or VS Code extension storage)
 *   ✅ Continue.dev              (~/.continue/)
 *   ✅ Aider                     (~/.aider/)
 * 
 * Auto-detects which tools are installed and parses their JSONL/log files.
 * Attributes costs to actual dates from timestamps (not file mod dates).
 */

const fs = require('fs');
const path = require('path');
const os = require('os');

const OUTPUT_DIR = path.join(__dirname, 'data');
if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });
const CACHE_FILE = path.join(OUTPUT_DIR, 'sessions-cache.json');

const HOME = os.homedir();
const TZ_OFFSET = -new Date().getTimezoneOffset() / 60;

// ─── Helpers ─────────────────────────────────────────────

function toLocalDate(timestampMs) {
  if (!timestampMs) return null;
  const d = new Date(timestampMs + TZ_OFFSET * 3600000);
  return d.toISOString().split('T')[0];
}

function toLocalTime(timestampMs) {
  if (!timestampMs) return null;
  const d = new Date(timestampMs + TZ_OFFSET * 3600000);
  return d.toISOString().split('T')[1].substring(0, 5);
}

function parseTimestamp(ts) {
  if (!ts) return null;
  if (typeof ts === 'number') return ts;
  if (typeof ts === 'string') {
    const d = new Date(ts);
    return isNaN(d.getTime()) ? null : d.getTime();
  }
  return null;
}

function getPricing(model) {
  if (!model) return { input: 3, output: 15, cacheWrite: 3.75, cacheRead: 0.30 };
  const m = model.toLowerCase();
  if (m.includes('opus-4-6') || m.includes('opus-4.6') || m.includes('opus-4-5') || m.includes('opus-4.5'))
    return { input: 5, output: 25, cacheWrite: 6.25, cacheRead: 0.50 };
  if (m.includes('opus-4-1') || m.includes('opus-4.1'))
    return { input: 15, output: 75, cacheWrite: 18.75, cacheRead: 1.50 };
  if (m.includes('opus'))
    return { input: 15, output: 75, cacheWrite: 18.75, cacheRead: 1.50 };
  if (m.includes('sonnet'))
    return { input: 3, output: 15, cacheWrite: 3.75, cacheRead: 0.30 };
  if (m.includes('haiku-4-5') || m.includes('haiku-4.5'))
    return { input: 1, output: 5, cacheWrite: 1.25, cacheRead: 0.10 };
  if (m.includes('haiku'))
    return { input: 0.25, output: 1.25, cacheWrite: 0.30, cacheRead: 0.03 };
  return { input: 3, output: 15, cacheWrite: 3.75, cacheRead: 0.30 };
}

// Recursively find JSONL files
function findJsonl(dir, maxDepth = 10) {
  const results = [];
  if (maxDepth <= 0) return results;
  try {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const fullPath = path.join(dir, entry.name);
      if (entry.isDirectory() && !entry.name.startsWith('.git')) {
        results.push(...findJsonl(fullPath, maxDepth - 1));
      } else if (entry.name.endsWith('.jsonl') && !entry.name.includes('audit')) {
        results.push(fullPath);
      }
    }
  } catch {}
  return results;
}

function makeDayEntry() {
  return { cost: 0, input_tokens: 0, output_tokens: 0, cache_read: 0, cache_write: 0, models: new Set(), times: [] };
}

/**
 * Clean raw message text: strip XML tags, system markers, cron prefixes.
 */
function cleanMessageText(text) {
  text = text.replace(/<[^>]+>[\s\S]*?<\/[^>]+>/g, '').trim();
  text = text.replace(/<[^>]+>/g, '').trim();
  text = text.replace(/^\[SUGGESTION MODE:[^\]]*\]\s*/i, '').trim();
  const cronMatch = text.match(/^\[cron:[a-f0-9-]+\s+([^\]]*)\]\s*(.*)/i);
  if (cronMatch) {
    text = cronMatch[1].trim() + (cronMatch[2] ? ' — ' + cronMatch[2].trim() : '');
  }
  return text;
}

/**
 * Extract text content from a JSONL message entry's content field.
 */
function extractText(msg) {
  if (!msg || typeof msg !== 'object') return '';
  const content = msg.content;
  if (typeof content === 'string') return content;
  if (Array.isArray(content)) {
    // Check if this is a tool_result (skip it)
    if (content.some(b => b.type === 'tool_result')) return '';
    const textBlock = content.find(c => c.type === 'text' && c.text && c.text.trim());
    return textBlock ? textBlock.text : '';
  }
  return '';
}

/**
 * Extract session metadata + conversation history from a JSONL file.
 * Returns: { title, sessionId, cwd, history: [{role, text}] }
 */
function extractSessionMeta(filePath) {
  const meta = { title: '', sessionId: '', cwd: '', history: [] };
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    const lines = content.split('\n').filter(l => l.trim());
    let foundTitle = false;

    for (const line of lines) {
      let entry;
      try { entry = JSON.parse(line); } catch { continue; }

      // Extract sessionId and cwd from any entry that has them
      if (!meta.sessionId && entry.sessionId) meta.sessionId = entry.sessionId;
      if (!meta.cwd && entry.cwd) meta.cwd = entry.cwd;

      // Skip non-conversation entries
      const msg = entry.message;
      if (!msg || typeof msg !== 'object') continue;
      const role = msg.role;
      if (role !== 'user' && role !== 'assistant') continue;

      const rawText = extractText(msg);
      if (!rawText) continue;
      const text = cleanMessageText(rawText);
      if (!text) continue;

      // Set title from first user message
      if (!foundTitle && role === 'user') {
        meta.title = text.length > 80 ? text.substring(0, 77) + '...' : text;
        foundTitle = true;
      }

      // Add to history (max 15 turns, 120 chars each)
      if (meta.history.length < 15) {
        meta.history.push({
          role: role === 'user' ? 'user' : 'ai',
          text: text.length > 120 ? text.substring(0, 117) + '...' : text
        });
      }
    }
  } catch {}
  // Fallback: derive sessionId from filename
  if (!meta.sessionId) {
    const base = path.basename(filePath, '.jsonl');
    if (/^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/.test(base)) {
      meta.sessionId = base;
    }
  }
  return meta;
}

function pushSessions(sessions, dayData, source, fileName, meta) {
  meta = meta || {};
  for (const [date, data] of Object.entries(dayData)) {
    if (data.cost < 0.0001) continue;
    const models = [...data.models];
    const time = data.times.length > 0 ? data.times.sort()[0] : '00:00';
    const entry = {
      date,
      time,
      source,
      file: fileName,
      cost: parseFloat(data.cost.toFixed(4)),
      input_tokens: data.input_tokens,
      output_tokens: data.output_tokens,
      cache_read: data.cache_read,
      cache_write: data.cache_write,
      model: models[models.length - 1] || ''
    };
    if (meta.title) entry.title = meta.title;
    if (meta.sessionId) entry.sessionId = meta.sessionId;
    if (meta.cwd) entry.cwd = meta.cwd;
    if (meta.history && meta.history.length > 0) entry.history = meta.history;
    sessions.push(entry);
  }
}

// ─── Cache helpers ───────────────────────────────────────

function loadCache() {
  try {
    if (!fs.existsSync(CACHE_FILE)) return [];
    const raw = fs.readFileSync(CACHE_FILE, 'utf-8');
    const data = JSON.parse(raw);
    if (!Array.isArray(data)) {
      console.warn('⚠️  Cache file has unexpected format, ignoring.');
      return [];
    }
    // Per-entry validation: keep only entries with required fields
    const valid = data.filter(s =>
      s && typeof s.source === 'string' && typeof s.file === 'string' &&
      typeof s.date === 'string' && typeof s.cost === 'number'
    );
    if (valid.length < data.length) {
      console.warn(`⚠️  Filtered out ${data.length - valid.length} malformed cache entries`);
    }
    return valid;
  } catch (e) {
    if (e.code !== 'ENOENT') {
      console.warn(`⚠️  Could not load cache: ${e.message}`);
    }
    return [];
  }
}

function saveCache(sessions) {
  try {
    const tmpFile = CACHE_FILE + '.tmp';
    fs.writeFileSync(tmpFile, JSON.stringify(sessions));
    fs.renameSync(tmpFile, CACHE_FILE);
  } catch (e) {
    console.warn(`⚠️  Could not save cache: ${e.message}`);
  }
}

function mergeSessions(freshSessions, cachedSessions) {
  const freshKeys = new Set();
  for (const s of freshSessions) {
    freshKeys.add(`${s.source}|${s.file}|${s.date}`);
  }
  const merged = [...freshSessions];
  for (const s of cachedSessions) {
    const key = `${s.source}|${s.file}|${s.date}`;
    if (!freshKeys.has(key)) {
      merged.push(s);
    }
  }
  return merged;
}

// ─── Parser: OpenClaw / Clawdbot format ──────────────────
// usage fields: usage.input, usage.output, usage.cacheRead, usage.cacheWrite
// OR pre-computed usage.cost.total
function parseOpenClawFormat(filePath) {
  const content = fs.readFileSync(filePath, 'utf-8');
  const lines = content.split('\n').filter(l => l.trim());
  const dayData = {};
  let fallbackDate = null;
  try { fallbackDate = toLocalDate(fs.statSync(filePath).mtimeMs); } catch {}

  for (const line of lines) {
    let entry;
    try { entry = JSON.parse(line); } catch { continue; }
    const msg = entry.message;
    const usage = (msg && msg.usage) || entry.usage;
    if (!usage) continue;
    if (!usage.cost && !usage.input && !usage.output) continue;

    let tsMs = parseTimestamp(entry.timestamp) || parseTimestamp(msg && msg.timestamp);
    let date = tsMs ? toLocalDate(tsMs) : fallbackDate;
    let time = tsMs ? toLocalTime(tsMs) : '00:00';
    if (!date) continue;

    if (!dayData[date]) dayData[date] = makeDayEntry();
    const dd = dayData[date];
    if (time) dd.times.push(time);

    const model = (msg && msg.model) || entry.model || '';
    if (model && model.startsWith('claude')) dd.models.add(model);

    if (usage.cost && usage.cost.total) {
      dd.cost += usage.cost.total;
    } else {
      const pricing = getPricing(model);
      const inp = usage.input || 0;
      const out = usage.output || 0;
      const cr = usage.cacheRead || 0;
      const cw = usage.cacheWrite || 0;
      dd.cost += (inp * pricing.input + out * pricing.output + cw * pricing.cacheWrite + cr * pricing.cacheRead) / 1000000;
    }
    dd.input_tokens += (usage.input || 0);
    dd.output_tokens += (usage.output || 0);
    dd.cache_read += (usage.cacheRead || 0);
    dd.cache_write += (usage.cacheWrite || 0);
  }
  return dayData;
}

// ─── Parser: Claude Code / Desktop / Cursor / Windsurf format ────
// usage fields: usage.input_tokens, usage.output_tokens,
//               usage.cache_creation_input_tokens, usage.cache_read_input_tokens
function parseClaudeCodeFormat(filePath) {
  const content = fs.readFileSync(filePath, 'utf-8');
  const lines = content.split('\n').filter(l => l.trim());
  const dayData = {};
  let fallbackDate = null;
  try { fallbackDate = toLocalDate(fs.statSync(filePath).mtimeMs); } catch {}

  for (const line of lines) {
    let entry;
    try { entry = JSON.parse(line); } catch { continue; }
    const msg = entry.message;
    const usage = (msg && msg.usage) || entry.usage;
    if (!usage) continue;

    const inputTok = usage.input_tokens || 0;
    const outputTok = usage.output_tokens || 0;
    const cacheWrite = usage.cache_creation_input_tokens || 0;
    const cacheRead = usage.cache_read_input_tokens || 0;
    if (inputTok === 0 && outputTok === 0 && cacheRead === 0 && cacheWrite === 0) continue;

    let tsMs = parseTimestamp(entry.timestamp) || parseTimestamp(msg && msg.timestamp);
    let date = tsMs ? toLocalDate(tsMs) : fallbackDate;
    let time = tsMs ? toLocalTime(tsMs) : '00:00';
    if (!date) continue;

    if (!dayData[date]) dayData[date] = makeDayEntry();
    const dd = dayData[date];
    if (time) dd.times.push(time);

    const model = (msg && msg.model) || entry.model || '';
    if (model && model.startsWith('claude')) dd.models.add(model);

    dd.input_tokens += inputTok;
    dd.output_tokens += outputTok;
    dd.cache_read += cacheRead;
    dd.cache_write += cacheWrite;

    const pricing = getPricing(model);
    dd.cost += (inputTok * pricing.input + outputTok * pricing.output + cacheWrite * pricing.cacheWrite + cacheRead * pricing.cacheRead) / 1000000;
  }
  return dayData;
}

// ─── Parser: Aider format ────────────────────────────────
// Aider uses a different log format — .aider.input.history and .aider.chat.history
// It also can write JSONL with litellm format
function parseAiderFormat(filePath) {
  const content = fs.readFileSync(filePath, 'utf-8');
  const lines = content.split('\n').filter(l => l.trim());
  const dayData = {};
  let fallbackDate = null;
  try { fallbackDate = toLocalDate(fs.statSync(filePath).mtimeMs); } catch {}

  for (const line of lines) {
    let entry;
    try { entry = JSON.parse(line); } catch { continue; }

    // Aider litellm JSONL: { model, usage: { prompt_tokens, completion_tokens, total_tokens }, ... }
    const usage = entry.usage || entry.response?.usage;
    if (!usage) continue;

    const inputTok = usage.prompt_tokens || usage.input_tokens || 0;
    const outputTok = usage.completion_tokens || usage.output_tokens || 0;
    const cacheRead = usage.cache_read_input_tokens || 0;
    const cacheWrite = usage.cache_creation_input_tokens || 0;
    if (inputTok === 0 && outputTok === 0) continue;

    let tsMs = parseTimestamp(entry.timestamp) || parseTimestamp(entry.created);
    // Aider sometimes uses Unix epoch seconds
    if (entry.created && typeof entry.created === 'number' && entry.created < 2000000000) {
      tsMs = entry.created * 1000;
    }
    let date = tsMs ? toLocalDate(tsMs) : fallbackDate;
    let time = tsMs ? toLocalTime(tsMs) : '00:00';
    if (!date) continue;

    if (!dayData[date]) dayData[date] = makeDayEntry();
    const dd = dayData[date];
    if (time) dd.times.push(time);

    const model = entry.model || '';
    if (model && model.includes('claude')) dd.models.add(model);

    dd.input_tokens += inputTok;
    dd.output_tokens += outputTok;
    dd.cache_read += cacheRead;
    dd.cache_write += cacheWrite;

    const pricing = getPricing(model);
    dd.cost += (inputTok * pricing.input + outputTok * pricing.output + cacheWrite * pricing.cacheWrite + cacheRead * pricing.cacheRead) / 1000000;
  }
  return dayData;
}

// ─── Parser: Continue.dev format ─────────────────────────
// Continue stores in ~/.continue/sessions/ as JSON with completions
function parseContinueFormat(filePath) {
  const dayData = {};
  try {
    const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
    const steps = data.steps || data.history || [];
    for (const step of steps) {
      const usage = step.usage || step.promptTokens ? { input_tokens: step.promptTokens || 0, output_tokens: step.co
... [TRUNCATED]
```

### File: dashboard.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Claude Usage Dashboard</title>
    <script src="data/data.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700&family=Outfit:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">

    <!-- Base styles -->
    <link rel="stylesheet" href="css/base.css">
    <link rel="stylesheet" href="css/layout.css">

    <!-- Component styles -->
    <link rel="stylesheet" href="css/components/header.css">
    <link rel="stylesheet" href="css/components/stat-cards.css">
    <link rel="stylesheet" href="css/components/charts.css">
    <link rel="stylesheet" href="css/components/filter-bar.css">
    <link rel="stylesheet" href="css/components/sessions-table.css">
    <link rel="stylesheet" href="css/components/table-rows.css">
    <link rel="stylesheet" href="css/components/detail-panel.css">
    <link rel="stylesheet" href="css/components/badges.css">
    <link rel="stylesheet" href="css/components/heatmap.css">
    <link rel="stylesheet" href="css/components/projects-table.css">
    <link rel="stylesheet" href="css/components/expensive-callout.css">
    <link rel="stylesheet" href="css/components/footer.css">
    <link rel="stylesheet" href="css/components/reload-fab.css">
    <link rel="stylesheet" href="css/components/data-transfer.css">

    <!-- Utilities -->
    <link rel="stylesheet" href="css/utilities.css">
</head>
<body>
    <div class="ambient-blob"></div>
    <div class="container">
        <header>
            <div class="header-left">
                <div class="logo-mark"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="none"><defs><linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#22d3ee"/><stop offset="100%" stop-color="#a78bfa"/></linearGradient><linearGradient id="glowGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#34d399" stop-opacity="0.25"/><stop offset="50%" stop-color="#22d3ee" stop-opacity="0.08"/><stop offset="100%" stop-color="#a78bfa" stop-opacity="0.25"/></linearGradient><linearGradient id="bar1" x1="0" y1="1" x2="0" y2="0"><stop offset="0%" stop-color="#22d3ee"/><stop offset="100%" stop-color="#34d399"/></linearGradient><linearGradient id="bar2" x1="0" y1="1" x2="0" y2="0"><stop offset="0%" stop-color="#60a5fa"/><stop offset="100%" stop-color="#22d3ee"/></linearGradient><linearGradient id="bar3" x1="0" y1="1" x2="0" y2="0"><stop offset="0%" stop-color="#a78bfa"/><stop offset="100%" stop-color="#60a5fa"/></linearGradient><linearGradient id="bar4" x1="0" y1="1" x2="0" y2="0"><stop offset="0%" stop-color="#fb7185"/><stop offset="100%" stop-color="#a78bfa"/></linearGradient><linearGradient id="lineGrad" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#fbbf24"/><stop offset="100%" stop-color="#fb7185"/></linearGradient><linearGradient id="areaFill" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fbbf24" stop-opacity="0.15"/><stop offset="100%" stop-color="#fb7185" stop-opacity="0.02"/></linearGradient></defs><rect width="512" height="512" rx="108" ry="108" fill="#0f1629"/><rect width="512" height="512" rx="108" ry="108" fill="url(#glowGrad)" opacity="0.5"/><rect x="3" y="3" width="506" height="506" rx="105" ry="105" fill="none" stroke="url(#bgGrad)" stroke-width="1.5" opacity="0.4"/><rect x="80" y="100" width="352" height="312" rx="20" ry="20" fill="#131b2e" opacity="0.6"/><line x1="110" y1="370" x2="402" y2="370" stroke="#253147" stroke-width="1.5" opacity="0.6"/><line x1="110" y1="296" x2="402" y2="296" stroke="#1e293b" stroke-width="0.75" stroke-dasharray="3,5" opacity="0.4"/><line x1="110" y1="222" x2="402" y2="222" stroke="#1e293b" stroke-width="0.75" stroke-dasharray="3,5" opacity="0.4"/><rect x="122" y="238" width="50" height="132" rx="8" ry="8" fill="url(#bar1)" opacity="0.92"/><rect x="192" y="168" width="50" height="202" rx="8" ry="8" fill="url(#bar2)" opacity="0.92"/><rect x="262" y="206" width="50" height="164" rx="8" ry="8" fill="url(#bar3)" opacity="0.92"/><rect x="332" y="128" width="50" height="242" rx="8" ry="8" fill="url(#bar4)" opacity="0.92"/><polygon points="147,226 217,156 287,192 357,122 357,370 147,370" fill="url(#areaFill)" opacity="0.6"/><polyline points="147,226 217,156 287,192 357,122" fill="none" stroke="url(#lineGrad)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" opacity="0.95"/><circle cx="147" cy="226" r="4.5" fill="#fbbf24"/><circle cx="217" cy="156" r="4.5" fill="#f59e0b"/><circle cx="287" cy="192" r="4.5" fill="#e879a0"/><circle cx="357" cy="122" r="4.5" fill="#fb7185"/></svg></div>
                <div>
                    <h1><span>Claude</span> Usage Tracker</h1>
                </div>
            </div>
            <div class="header-meta">
                <span class="updated"><span class="status-dot"></span>Last sync: <span id="last-updated">—</span></span>
                <div class="dt-actions">
                    <button class="dt-btn dt-btn-export" id="dt-export-btn" type="button" title="Export data as JSON">
                        <svg viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
                        Export
                    </button>
                    <button class="dt-btn dt-btn-import" id="dt-import-btn" type="button" title="Import data from another device">
                        <svg viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
                        Import
                    </button>
                </div>
            </div>
        </header>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="label">Today</div>
                <div class="value" id="today-cost">$0.00</div>
                <div class="yesterday-delta" id="yesterday-delta"></div>
                <div class="subtext" id="today-date">—</div>
            </div>
            <div class="stat-card">
                <div class="label">This Week</div>
                <div class="value" id="week-cost">$0.00</div>
                <div class="subtext" id="week-range">&mdash;</div>
            </div>
            <div class="stat-card">
                <div class="label">This Month</div>
                <div class="value" id="month-cost">$0.00</div>
                <div class="subtext" id="month-name">—</div>
                <div class="projection-line" id="month-projection" style="display:none;"></div>
            </div>
            <div class="stat-card">
                <div class="label">All Time</div>
                <div class="value" id="total-cost">$0.00</div>
                <div class="subtext">Since tracking began</div>
            </div>
            <div class="stat-card">
                <div class="label">Sessions</div>
                <div class="value" id="session-count">0</div>
                <div class="subtext">Across all sources</div>
            </div>
        </div>

        <div class="chart-card chart-card-full">
            <h3>Daily Spend by Source <span class="chart-hint">click bar to filter</span></h3>
            <div class="chart-canvas-wrap">
                <canvas id="dailyChart"></canvas>
            </div>
        </div>

        <div id="day-filter-bar" style="display:none">
            <span class="day-filter-label">Filtered: <strong id="day-filter-date"></strong></span>
            <button class="day-filter-clear" onclick="clearDayFilter()">&#x2715; clear</button>
        </div>

        <div class="charts-grid-half">
            <div class="chart-card">
                <h3>By Source</h3>
                <div class="chart-canvas-wrap">
                    <canvas id="sourceChart"></canvas>
                </div>
            </div>
            <div class="chart-card">
                <h3>Spend by Model</h3>
                <div class="chart-canvas-wrap">
                    <canvas id="modelChart"></canvas>
                </div>
            </div>
        </div>

        <div class="heatmap-section">
            <div class="heatmap-header">
                <h3 id="heatmap-title">Peak Hours</h3>
                <div class="heatmap-toggle" id="heatmap-toggle">
                    <div class="heatmap-toggle-slider" id="heatmap-toggle-slider"></div>
                    <button class="heatmap-toggle-btn active" data-view="hours" id="toggle-hours-btn">Hours</button>
                    <button class="heatmap-toggle-btn" data-view="days" id="toggle-days-btn">Days</button>
                </div>
            </div>

            <!-- Hours View — actual dates × 24 hour columns -->
            <div class="heatmap-view heatmap-view-active" id="heatmap-hours-view">
                <div class="heatmap-hours-grid" id="heatmap-hours-grid"></div>
            </div>

            <!-- Days View (new) -->
            <div class="heatmap-view" id="heatmap-days-view">
                <div class="heatmap-days-container">
                    <div class="heatmap-days-day-labels" id="heatmap-days-day-labels"></div>
                    <div class="heatmap-days-grid-wrapper">
                        <div class="heatmap-days-month-labels" id="heatmap-days-month-labels"></div>
                        <div class="heatmap-days-grid" id="heatmap-days-grid"></div>
                    </div>
                </div>
            </div>

            <div class="heatmap-legend">
                <span class="heatmap-legend-label">Less</span>
                <div class="heatmap-legend-cell" style="background: rgba(30, 41, 59, 0.25); border: 1px solid rgba(30, 41, 59, 0.15);"></div>
                <div class="heatmap-legend-cell" style="background: linear-gradient(135deg, rgba(34, 211, 238, 0.15), rgba(34, 211, 238, 0.25));"></div>
                <div class="heatmap-legend-cell" style="background: linear-gradient(135deg, rgba(34, 211, 238, 0.4), rgba(96, 165, 250, 0.55));"></div>
                <div class="heatmap-legend-cell" style="background: linear-gradient(135deg, rgba(251, 191, 36, 0.55), rgba(249, 158, 11, 0.7));"></div>
                <div class="heatmap-legend-cell" style="background: linear-gradient(135deg, rgba(251, 113, 133, 0.7), rgba(244, 63, 94, 0.85));"></div>
                <span class="heatmap-legend-label">More</span>
            </div>
        </div>
        <div class="heatmap-tooltip" id="heatmap-tooltip">
            <div class="tip-day"></div>
            <div class="tip-hour"></div>
            <div class="tip-stats">
                <div class="tip-stat"><span class="tip-label">Sessions</span><span class="tip-value tip-count"></span></div>
                <div class="tip-stat"><span class="tip-label">Cost</span><span class="tip-value tip-cost"></span></div>
            </div>
        </div>

        <!-- Most Expensive Session Callout -->
        <div class="expensive-callout" id="expensive-session-callout" style="display: none;">
            <div class="expensive-callout-icon">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2z"/>
                    <path d="M12 8v4"/>
                    <path d="M12 16h.01"/>
                </svg>
            </div>
            <div class="expensive-callout-content">
                <div class="expensive-callout-title">Most Expensive Session Today</div>
                <div class="expensive-callout-details">
                    <span class="expensive-detail" id="exp-source"></span>
                    <span class="expensive-detail" id="exp-model"></span>
                    <span class="expensive-detail expensive-detail-time" id="exp-time"></span>
                    <span class="expensive-detail expensive-detail-cost" id="exp-cost"></span>
                </div>
                <div class="expensive-callout-tokens" id="exp-tokens"></div>
            </div>
        </div>

        <div class="sessions-section">
            <div class="sessions-header">
                <h3>Session Log</h3>
                <div class="view-toggle" id="sessions-view-toggle">
                    <div class="view-toggle-slider"></div>
                    <button class="view-toggle-btn active" data-view="timeline">Timeline</button>
                    <button class="view-toggle-btn" data-view="projects">Projects</button>
                </div>
                <div class="sessions-header-right">
                    <span class="hint">click a row to expand</span>
                    <button class="toggle-all-btn" id="toggle-all-btn" onclick="toggleAllDays()" title="Expand or collapse all date rows (Shift+E)">
                        Expand All<span class="arrow">&#9660;</span><span class="kbd-hint">Shift+E</span>
                    </button>
                </div>
            </div>
            <div class="filter-bar" id="filter-bar">
                <div class="filter-controls">
                    <!-- Source multi-select -->
                    <div class="filter-group" id="source-filter-group">
                        <button class="filter-btn" id="source-filter-btn" type="button">
                            Source <span class="chevron-down">&#9662;</span>
                        </button>
                        <div class="filter-dropdown" id="source-dropdown">
                            <!-- Populated dynamically -->
                        </div>
                    </div>

                    <!-- Model multi-select -->
                    <div class="filter-group" id="model-filter-group">
                        <button class="filter-btn" id="model-filter-btn" type="button">
                            Model <span class="chevron-down">&#9662;</span>
                        </button>
                        <div class="filter-dropdown" id="model-dropdown">
                            <!-- Populated dynamically -->
                        </div>
                    </div>

                    <!-- Date range -->
                    <span class="filter-label">From</span>
                    <input type="date" class="filter-date" id="filter-date-from" />
                    <span class="filter-label">To</span>
                    <input type="date" class="filter-date" id="filter-date-to" />

                    <!-- Min cost -->
                    <div class="filter-cost-wrapper">
                        <span class="dollar-s
... [TRUNCATED]
```

### File: css\base.css
```css
:root {
    --bg-primary: #0a0e17;
    --bg-secondary: #111827;
    --bg-card: #151d2e;
    --bg-card-hover: #1a2540;
    --bg-elevated: #1e293b;
    --border: #1e293b;
    --border-light: #253147;
    --text-primary: #e2e8f0;
    --text-secondary: #94a3b8;
    --text-muted: #64748b;
    --accent-cyan: #22d3ee;
    --accent-cyan-dim: rgba(34, 211, 238, 0.15);
    --accent-amber: #fbbf24;
    --accent-amber-dim: rgba(251, 191, 36, 0.12);
    --accent-emerald: #34d399;
    --accent-emerald-dim: rgba(52, 211, 153, 0.12);
    --accent-rose: #fb7185;
    --accent-rose-dim: rgba(251, 113, 133, 0.12);
    --accent-violet: #a78bfa;
    --accent-violet-dim: rgba(167, 139, 250, 0.12);
    --accent-blue: #60a5fa;
    --accent-blue-dim: rgba(96, 165, 250, 0.12);
    --glow-cyan: 0 0 20px rgba(34, 211, 238, 0.15);
    --radius: 12px;
    --radius-sm: 8px;
    --radius-pill: 20px;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: 'Outfit', sans-serif;
    background: var(--bg-primary);
    color: var(--text-primary);
    min-height: 100vh;
    overflow-x: hidden;
}

/* Ambient glow blobs — static, no filters */
body::after {
    content: '';
    position: fixed;
    top: -20%;
    right: -10%;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(34, 211, 238, 0.06) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
    will-change: auto;
}

.ambient-blob {
    position: fixed;
    bottom: -15%;
    left: -5%;
    width: 500px;
    height: 500px;
    background: radial-gradient(circle, rgba(251, 191, 36, 0.04) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
}

```

### File: css\layout.css
```css
.container {
    max-width: 1440px;
    margin: 0 auto;
    padding: 32px 40px;
    position: relative;
    z-index: 1;
}

/* Stats Grid */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 16px;
    margin-bottom: 32px;
}

/* Charts */
.charts-grid {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 16px;
    margin-bottom: 32px;
}

.charts-grid-half {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-bottom: 32px;
}

/* Responsive */
@media (max-width: 1280px) {
    .stats-grid { grid-template-columns: repeat(3, 1fr); }
}

@media (max-width: 1024px) {
    .stats-grid { grid-template-columns: repeat(2, 1fr); }
    .charts-grid { grid-template-columns: 1fr; }
    .charts-grid-half { grid-template-columns: 1fr; }
    .container { padding: 20px; }
    .filter-controls { gap: 8px; }
}

@media (max-width: 640px) {
    .stats-grid { grid-template-columns: 1fr; }
    header { flex-direction: column; align-items: flex-start; gap: 12px; }
    .header-meta { align-items: flex-start; }
    header h1 { font-size: 1.3rem; }

    .expensive-callout {
        flex-direction: column;
        gap: 10px;
    }

    .expensive-callout-details {
        flex-direction: column;
        align-items: flex-start;
        gap: 6px;
    }

    .filter-controls {
        flex-direction: column;
        align-items: stretch;
    }
    .filter-status { margin-left: 0; justify-content: space-between; }
    .filter-date { width: 100%; }
    .filter-cost { width: 100%; }
}

```

### File: css\utilities.css
```css
/* Scrollbar */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--border-light); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--text-muted); }

/* Global Animations */
@keyframes fadeSlideUp {
    from { opacity: 0; transform: translateY(16px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Reduced motion support */
@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}

/* Selection styling */
::selection {
    background: rgba(34, 211, 238, 0.2);
    color: var(--text-primary);
}

```

### File: js\main.js
```js
/**
 * main.js
 *
 * Main orchestrator for the Usage Tracker Dashboard.
 * Coordinates data loading and component initialization.
 */

// === Imports ===

// Config
import { sourceColors, defaultColors, modelColorMap } from './config/constants.js';
import { initChartDefaults } from './config/chart-config.js';

// Utils
import { formatNumber } from './utils/formatters.js';
import { getWeekStart, getWeekEnd, formatWeekLabel } from './utils/date-utils.js';
import { sourceClass } from './utils/class-utils.js';
import { getModelInfo } from './utils/model-utils.js';

// Components
import { initCounterAnimations } from './components/animations.js';

import { initCharts, clearDayFilter } from './components/charts.js';
import {
    initFilterDropdowns,
    applyFilters,
    updateFilterCount,
    setupFilterListeners
} from './components/filters.js';
import { initHeatmap } from './components/heatmap.js';
import { renderMonthlyProjection, updateYesterdayDelta } from './components/projections.js';
import {
    renderSessionTable,
    setMostExpensive,
    toggleDay,
    toggleAllDays,
    initKeyboardShortcuts
} from './components/sessions-table.js';
import {
    renderProjectsTable,
    toggleAllProjects
} from './components/projects-table.js';
import {
    exportData,
    importData,
    mergeSessions,
    recalcSummary
} from './components/data-transfer.js';

// === Global State ===

let allSessionsData = [];
let totalSessionCount = 0;
let currentSessionView = 'timeline';

// === Expose Functions to Window (for onclick handlers) ===

// toggleDay and filter removal functions are already exposed by their respective modules
// We just need to expose toggleAllDays and set up the filter callback
window.toggleAllDays = toggleAllDays;
window.toggleAllProjects = toggleAllProjects;
window.clearDayFilter = clearDayFilter;

function getCurrentRenderer() {
    return currentSessionView === 'projects' ? renderProjectsTable : renderSessionTable;
}

function applyCurrentFilters() {
    applyFilters(allSessionsData, totalSessionCount, getCurrentRenderer());
}

function toggleAllForCurrentView() {
    if (currentSessionView === 'projects') {
        toggleAllProjects();
    } else {
        toggleAllDays();
    }
}

function updateTableHeader(view) {
    const thead = document.getElementById('sessions-thead');
    if (!thead) return;
    const cells = thead.querySelectorAll('th');
    if (cells.length < 2) return;
    cells[0].textContent = view === 'projects' ? 'Project' : 'Date';
    cells[1].textContent = view === 'projects' ? 'Sources' : 'Sessions';
}

// === Main Data Loading Function ===

/**
 * Load data from window globals and initialize all dashboard components.
 * This is the main entry point after the page loads.
 */
async function loadData() {
    try {
        // Load data from window globals
        const summary = window.__SUMMARY__;
        const openclawSessions = window.__OPENCLAW_SESSIONS__ || window.__CLAWDBOT_SESSIONS__ || [];
        const claudeSessions = window.__CLAUDE_SESSIONS__ || [];

        // Check if data is available
        if (!summary) {
            document.getElementById('sessions-body').innerHTML =
                '<tr><td colspan="8" class="no-data">No data found. Run collect-usage.sh then reload.</td></tr>';
            return;
        }

        // === Static Text Values ===
        document.getElementById('today-date').textContent = summary.today;
        document.getElementById('month-name').textContent = new Date(summary.today + 'T00:00:00').toLocaleDateString('en-US', { month: 'long', year: 'numeric' });
        document.getElementById('last-updated').textContent = new Date(summary.generated_at).toLocaleString();

        // === Monthly Projection ===
        renderMonthlyProjection(summary);

        // === Prepare Animated Counter Elements ===
        // Store target values as data attributes, set initial display to zero
        const todayCostEl = document.getElementById('today-cost');
        todayCostEl.dataset.target = summary.today_cost;
        todayCostEl.dataset.prefix = '$';
        todayCostEl.dataset.decimals = '2';
        todayCostEl.textContent = '$0.00';

        const monthCostEl = document.getElementById('month-cost');
        monthCostEl.dataset.target = summary.month_cost;
        monthCostEl.dataset.prefix = '$';
        monthCostEl.dataset.decimals = '2';
        monthCostEl.textContent = '$0.00';

        const totalCostEl = document.getElementById('total-cost');
        totalCostEl.dataset.target = summary.totals.grand_total;
        totalCostEl.dataset.prefix = '$';
        totalCostEl.dataset.decimals = '2';
        totalCostEl.textContent = '$0.00';

        const sessionCountEl = document.getElementById('session-count');
        sessionCountEl.dataset.target = summary.session_counts.total;
        sessionCountEl.dataset.prefix = '';
        sessionCountEl.dataset.decimals = '0';
        sessionCountEl.textContent = '0';

        // === Combine All Sessions ===
        const allSessions = [...openclawSessions, ...claudeSessions];

        // === Calculate This Week Cost ===
        const thisWeekStart = getWeekStart(summary.today);
        const thisWeekEnd = getWeekEnd(thisWeekStart);
        const weekCost = allSessions
            .filter(s => s.date >= thisWeekStart && s.date <= thisWeekEnd)
            .reduce((sum, s) => sum + s.cost, 0);

        const weekCostEl = document.getElementById('week-cost');
        weekCostEl.dataset.target = weekCost;
        weekCostEl.dataset.prefix = '$';
        weekCostEl.dataset.decimals = '2';
        weekCostEl.textContent = '$0.00';
        document.getElementById('week-range').textContent = formatWeekLabel(thisWeekStart);

        // === Yesterday Delta ===
        updateYesterdayDelta(summary, allSessions);

        // === Find Most Expensive Session ===
        const todaySessions = allSessions.filter(s => s.date === summary.today);
        let mostExpensiveSession = null;
        let mostExpensiveFile = null;
        let mostExpensiveDate = null;

        if (todaySessions.length > 0) {
            mostExpensiveSession = todaySessions.reduce(
                (max, s) => s.cost > max.cost ? s : max,
                todaySessions[0]
            );
            mostExpensiveFile = mostExpensiveSession.file;
            mostExpensiveDate = mostExpensiveSession.date;
        }

        // Populate the expensive session callout banner
        const callout = document.getElementById('expensive-session-callout');
        if (mostExpensiveSession && mostExpensiveSession.cost > 0) {
            const ms = mostExpensiveSession;
            const sc = sourceClass(ms.source);
            const mi = getModelInfo(ms.model);

            document.getElementById('exp-source').innerHTML =
                `<span class="source-badge source-${sc}">${ms.source}</span>`;
            document.getElementById('exp-model').innerHTML =
                `<span class="model-badge ${mi.cls}">${mi.name}</span>`;
            document.getElementById('exp-time').textContent = ms.time || '---';
            document.getElementById('exp-cost').textContent = `$${ms.cost.toFixed(2)}`;
            document.getElementById('exp-tokens').innerHTML =
                `<span><span class="token-label">In:</span> <span class="token-value">${formatNumber(ms.input_tokens || 0)}</span></span>` +
                `<span><span class="token-label">Out:</span> <span class="token-value">${formatNumber(ms.output_tokens || 0)}</span></span>` +
                `<span><span class="token-label">Cache Read:</span> <span class="token-value">${formatNumber(ms.cache_read || 0)}</span></span>` +
                `<span><span class="token-label">Cache Write:</span> <span class="token-value">${formatNumber(ms.cache_write || 0)}</span></span>`;

            callout.style.display = 'flex';
        } else {
            callout.style.display = 'none';
        }

        // Pass most expensive session info to sessions-table module
        setMostExpensive(mostExpensiveFile, mostExpensiveDate);

        // === Store Global State ===
        allSessionsData = allSessions;
        totalSessionCount = allSessions.length;

        // === Initialize Filter Dropdowns ===
        initFilterDropdowns(allSessions);

        // === Render Session Table ===
        renderSessionTable(allSessions);
        updateFilterCount(allSessions.length, totalSessionCount);

        // === Initialize Chart.js Defaults ===
        initChartDefaults();

        // === Initialize Charts ===
        initCharts(allSessions);

        // === Initialize Heatmap ===
        initHeatmap(allSessions);

        // === Initialize Animated Counters ===
        initCounterAnimations();

        // === Setup Filter Listeners ===
        window._applyFiltersCallback = applyCurrentFilters;
        setupFilterListeners(applyCurrentFilters);

        // === Initialize Keyboard Shortcuts ===
        initKeyboardShortcuts(toggleAllForCurrentView);

        // === Setup Session View Toggle ===
        setupSessionViewToggle();

    } catch (error) {
        console.error('Error loading data:', error);
        document.getElementById('sessions-body').innerHTML =
            '<tr><td colspan="8" class="no-data">Error loading data. Run collect-usage.sh first.</td></tr>';
    }
}

// === Reload FAB Handler ===

function initReloadButton() {
    const fab = document.getElementById('reload-fab');
    if (!fab) return;

    fab.addEventListener('click', () => {
        fab.classList.add('is-reloading');
        // Fade out then trigger reload
        document.body.style.transition = 'opacity 0.25s ease-out';
        document.body.style.opacity = '0';
        setTimeout(() => {
            try {
                window.webkit.messageHandlers.reload.postMessage('');
            } catch (_) {
                location.reload();
            }
        }, 250);
    });
}

// === Export / Import Handlers ===

function initDataTransfer() {
    const exportBtn = document.getElementById('dt-export-btn');
    const importBtn = document.getElementById('dt-import-btn');
    if (!exportBtn || !importBtn) return;

    exportBtn.addEventListener('click', () => {
        const summary = window.__SUMMARY__;
        if (!summary || allSessionsData.length === 0) return;
        exportData(summary, allSessionsData);
    });

    importBtn.addEventListener('click', async () => {
        const result = await importData();
        if (!result) return;

        // Merge imported sessions with current data
        const merged = mergeSessions(allSessionsData, result.sessions);
        const newSummary = recalcSummary(merged);

        // Update global state
        allSessionsData = merged;
        totalSessionCount = merged.length;

        // Show import banner
        showImportBanner(result.sessions.length, merged.length);

        // Re-render with merged data
        reRenderDashboard(newSummary, merged);
    });
}

function showImportBanner(importedCount, totalCount) {
    // Remove existing banner
    const old = document.getElementById('dt-import-banner');
    if (old) old.remove();

    const banner = document.createElement('div');
    banner.id = 'dt-import-banner';
    banner.className = 'dt-import-banner';
    banner.innerHTML = `
        <span class="dt-import-banner-text">
            Viewing merged data — <strong>${totalCount}</strong> total sessions (imported ${importedCount})
        </span>
        <button class="dt-import-dismiss" onclick="location.reload()">Dismiss &amp; Reload</button>
    `;

    const container = document.querySelector('.container');
    const statsGrid = document.querySelector('.stats-grid');
    container.insertBefore(banner, statsGrid);
}

function reRenderDashboard(summary, sessions) {
    // Update stat card targets
    document.getElementById('today-cost').textContent = '$' + summary.today_cost.toFixed(2);
    document.getElementById('month-cost').textContent = '$' + summary.month_cost.toFixed(2);
    document.getElementById('total-cost').textContent = '$' + summary.totals.grand_total.toFixed(2);
    document.getElementById('session-count').textContent = sessions.length.toString();

    // Recalc week cost
    const thisWeekStart = getWeekStart(summary.today);
    const thisWeekEnd = getWeekEnd(thisWeekStart);
    const weekCost = sessions
        .filter(s => s.date >= thisWeekStart && s.date <= thisWeekEnd)
        .reduce((sum, s) => sum + s.cost, 0);
    document.getElementById('week-cost').textContent = '$' + weekCost.toFixed(2);

    // Re-render components
    initFilterDropdowns(sessions);
    getCurrentRenderer()(sessions);
    updateFilterCount(sessions.length, totalSessionCount);
    initCharts(sessions);
    initHeatmap(sessions);

    // Re-bind filter callback
    window._applyFiltersCallback = applyCurrentFilters;
    setupFilterListeners(applyCurrentFilters);
}

// === Session View Toggle ===

function setupSessionViewToggle() {
    const toggle = document.getElementById('sessions-view-toggle');
    if (!toggle) return;

    const buttons = toggle.querySelectorAll('.view-toggle-btn');
    const slider = toggle.querySelector('.view-toggle-slider');
    const toggleAllBtn = document.getElementById('toggle-all-btn');

    buttons.forEach(btn => {
        btn.addEventListener('click', () => {
            const view = btn.dataset.view;
            if (view === currentSessionView) return;

            // Update active button
            buttons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            // Slide the slider
            if (view === 'projects') {
                slider.style.transform = 'translateX(100%)';
            } else {
                slider.style.transform = 'translateX(0)';
            }

            // Update state
            currentSessionView = view;

            // Update table header
            updateTableHeader(view);

            // Update Expand All button onclick
            if (toggleAllBtn) {
                toggleAllBtn.onclick = view === 'projects' ? toggleAllProjects : toggleAllDays;
            }

            applyCurrentFilters();
        });
    });
}

// === Initialize on DOM Ready ===

function init() {
    loadData();
    initReloadButton();
    initDataTransfer();
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
