---
id: lobsterboard
type: knowledge
owner: OA_Triage
---
# lobsterboard
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "lobsterboard",
  "version": "0.8.3",
  "description": "Self-hosted drag-and-drop dashboard builder with 50 widgets, template gallery, and custom pages. Works standalone or with OpenClaw.",
  "keywords": [
    "dashboard",
    "widgets",
    "monitoring",
    "kpi",
    "builder",
    "homelab",
    "self-hosted",
    "openclaw"
  ],
  "author": "curbob",
  "license": "BSL-1.1",
  "homepage": "https://github.com/curbob/LobsterBoard#readme",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/curbob/LobsterBoard.git"
  },
  "bugs": {
    "url": "https://github.com/curbob/LobsterBoard/issues"
  },
  "type": "module",
  "main": "dist/lobsterboard.umd.js",
  "module": "dist/lobsterboard.esm.js",
  "unpkg": "dist/lobsterboard.umd.min.js",
  "jsdelivr": "dist/lobsterboard.umd.min.js",
  "browser": "dist/lobsterboard.umd.min.js",
  "exports": {
    ".": {
      "import": "./dist/lobsterboard.esm.js",
      "require": "./dist/lobsterboard.umd.js",
      "browser": "./dist/lobsterboard.umd.min.js"
    },
    "./css": "./dist/lobsterboard.css",
    "./widgets": {
      "import": "./src/widgets.js"
    },
    "./builder": {
      "import": "./src/builder.js"
    }
  },
  "bin": {
    "lobsterboard": "./bin/lobsterboard.mjs"
  },
  "files": [
    "server.cjs",
    "app.html",
    "js/",
    "css/",
    "dist",
    "src",
    "bin/",
    "templates/",
    "js/templates.js",
    "README.md",
    "CHANGELOG.md",
    "LICENSE"
  ],
  "scripts": {
    "build": "rollup -c",
    "build:watch": "rollup -c -w",
    "prebuild": "rm -rf dist",
    "start": "node server.cjs",
    "dev": "node server.cjs",
    "test": "vitest run",
    "test:watch": "vitest",
    "test:coverage": "vitest run --coverage",
    "prepublishOnly": "npm run build"
  },
  "devDependencies": {
    "@rollup/plugin-terser": "^0.4.4",
    "@vitest/coverage-v8": "^4.1.2",
    "jsdom": "^29.0.1",
    "rollup": "^4.9.6",
    "rollup-plugin-copy": "^3.5.0",
    "vitest": "^4.1.2"
  },
  "engines": {
    "node": ">=16.0.0"
  },
  "dependencies": {
    "systeminformation": "^5.30.7"
  }
}

```

### File: README.md
```md
# 🦞 LobsterBoard

A self-hosted, drag-and-drop dashboard builder with 60+ widgets, a template gallery, custom pages, and zero cloud dependencies. One Node.js server, no frameworks, no build step needed.

**Works standalone or with [OpenClaw](https://github.com/openclaw/openclaw).** LobsterBoard is a general-purpose dashboard — use it to monitor your homelab, track stocks, display weather, manage todos, or anything else. OpenClaw users get bonus widgets (auth status, cron jobs, activity logs), but they're completely optional.

![LobsterBoard](lobsterboard-logo-final.png)

![LobsterBoard Dashboard](lobsterboard-screenshot.jpg)

## Quick Start

```bash
npm install lobsterboard
cd node_modules/lobsterboard
node server.cjs
```

Or clone it:

```bash
git clone https://github.com/Curbob/LobsterBoard.git
cd LobsterBoard
npm install
node server.cjs
```

Open **http://localhost:8080** → press **Ctrl+E** to enter edit mode → drag widgets from the sidebar → click **💾 Save**.

![Edit Mode](lobsterboard-editor.jpg)

## Features

- **Drag-and-drop editor** — visual layout with 20px snap grid, resize handles, property panel
- **60+ widgets** — system monitoring, weather, calendars, RSS, smart home, finance, AI/LLM tracking, notes, and more
- **Template Gallery** — export, import, and share dashboard layouts with auto-screenshot previews; import as merge or full replace
- **Custom pages** — extend your dashboard with full custom pages (notes, kanban boards, anything)
- **Canvas sizes** — preset resolutions (1920×1080, 2560×1440, etc.) or custom sizes
- **Live data** — system stats stream via Server-Sent Events, widgets auto-refresh
- **5 themes** — Default (dark), Terminal (CRT green), Feminine (pastel pink), Feminine Dark, Paper (sepia)
- **No cloud** — everything runs locally, your data stays yours

## Themes

LobsterBoard ships with 5 built-in themes. Switch themes from the dropdown in edit mode — your choice persists across sessions.

| Default | Terminal | Paper |
|---------|----------|-------|
| ![Default](site-assets/themes/theme-default.png) | ![Terminal](site-assets/themes/theme-terminal.png) | ![Paper](site-assets/themes/theme-paper.png) |

| Feminine | Feminine Dark |
|----------|---------------|
| ![Feminine](site-assets/themes/theme-feminine.png) | ![Feminine Dark](site-assets/themes/theme-feminine-dark.png) |

- **Default** — dark theme with emoji icons (the classic look)
- **Terminal** — green CRT aesthetic with scanlines and Phosphor icons
- **Paper** — warm cream/sepia tones, serif fonts, vintage feel
- **Feminine** — soft pink and lavender pastels with subtle glows
- **Feminine Dark** — pink/purple accents on a dark background

## Remote Server Monitoring

Monitor multiple servers from a single dashboard using [lobsterboard-agent](https://www.npmjs.com/package/lobsterboard-agent).

### Setup Remote Server

On your VPS/remote server:

```bash
npm install -g lobsterboard-agent
lobsterboard-agent init     # Generates API key - save it!
lobsterboard-agent serve    # Starts on port 9090
```

### Add to LobsterBoard

1. Click **🖥️ Servers** in the header
2. Enter server name, URL (`http://your-server-ip:9090`), and API key
3. Click **Test Connection** to verify
4. Add widgets (Uptime Monitor, Docker, CPU/Memory, etc.)
5. Select your remote server from the **Server** dropdown in widget properties

### Supported Widgets

These widgets support remote server data:

| Widget | What It Shows |
|--------|---------------|
| **Uptime Monitor** | System uptime, CPU, memory |
| **CPU / Memory** | CPU usage + RAM usage |
| **Disk Usage** | Disk space with ring chart |
| **Network Speed** | Upload/download throughput |
| **Docker Containers** | Container list and status |

### Multi-Server Dashboard

Add multiple widgets and select different servers for each — monitor your entire infrastructure from one dashboard.

## Configuration

```bash
PORT=3000 node server.cjs              # Custom port
HOST=0.0.0.0 node server.cjs           # Expose to network
```

Widget settings are edited in the right-hand panel during edit mode. All configuration saves to `config.json`.

## Template Gallery

![Template Gallery](lobsterboard-templates.jpg)

LobsterBoard includes a built-in template system for sharing and reusing dashboard layouts.

![Template Import](lobsterboard-template-detail.jpg)

- **Export** your current dashboard as a template (auto-captures a screenshot preview)
- **Browse** the template gallery to discover pre-built layouts
- **Import** templates in two modes:
  - **Replace** — swap your entire dashboard for the template
  - **Merge** — append the template's widgets below your existing layout
- Templates are stored in the `templates/` directory and can be shared as folders

![Dashboard Example](lobsterboard-dashboard-2.jpg)

## Widgets

### 🖥️ System Monitoring
| Widget | Description |
|--------|-------------|
| CPU / Memory | Real-time CPU load and memory usage |
| Disk Usage | Disk space with ring gauge |
| Network Speed | Upload/download throughput |
| Uptime Monitor | System uptime, CPU load, memory summary |
| Docker Containers | Container list with status |

### 🌤️ Weather
| Widget | Description |
|--------|-------------|
| Local Weather | Current conditions for your city |
| World Weather | Multi-city weather overview |

### ⏰ Time & Productivity
| Widget | Description |
|--------|-------------|
| Clock | Analog/digital clock |
| World Clock | Multiple time zones |
| Countdown | Timer to a target date |
| Todo List | Persistent task list |
| Pomodoro Timer | Work/break timer |
| Notes | Persistent rich-text notes with auto-save |

### 📰 Media & Content
| Widget | Description |
|--------|-------------|
| RSS Ticker | Scrolling feed from any RSS/Atom URL |
| Calendar | iCal feed display (Google, Apple, Outlook) |
| Now Playing | Currently playing media |
| Quote of Day | Random inspirational quotes |
| Quick Links | Bookmark grid |

### 🤖 AI / LLM Monitoring

Track your AI coding subscriptions in real-time. Inspired by [OpenUsage](https://github.com/robinebers/openusage) by Robin Ebers.

| Widget | Description | Setup |
|--------|-------------|-------|
| AI Usage | Combined view of all providers | — |
| Claude Code | Session, weekly, Opus limits | Run `claude` once |
| Codex CLI | Session, weekly, code reviews | Run `codex` once |
| GitHub Copilot | Premium, chat, completions | Run `gh auth login` |
| Cursor | Credits, usage breakdown | Just use Cursor IDE |
| Gemini CLI | All available Gemini CLI quota buckets | Run `gemini` once |
| Amp | Free tier, credits | Run `amp` once |
| Factory / Droid | Standard, premium tokens | Run `factory` once |
| Kimi Code | Session, weekly | Run `kimi` once |
| JetBrains AI | Quota tracking | Sign in via IDE |
| Antigravity | Gemini 3, Claude via Google | Run `antigravity-usage login` |
| MiniMax | Coding plan session | Set `MINIMAX_API_KEY` |
| Z.ai | Session, weekly | Set `ZAI_API_KEY` |
| AI Cost Tracker | Monthly cost breakdown | — |
| API Status | Provider availability | — |
| Active Sessions | OpenClaw session monitor | — |
| Token Gauge | Context window usage | — |

### 💰 Finance
| Widget | Description |
|--------|-------------|
| Stock Ticker | Live stock prices (requires API key) |
| Crypto Price | Cryptocurrency tracker |

### 🏠 Smart Home
| Widget | Description |
|--------|-------------|
| Indoor Climate | Temperature/humidity sensors |
| Camera Feed | IP camera stream |
| Power Usage | Energy monitoring |

### 🔗 Embeds & Media
| Widget | Description |
|--------|-------------|
| Image / Random Image / Web Image / Latest Image | Static, rotating, remote, or latest images (with browse button for directory selection) |
| Iframe Embed | Embed any webpage |

### 🔧 Utility
| Widget | Description |
|--------|-------------|
| Auth Status | Authentication status display |
| Sleep Score | Garmin sleep score widget |
| GitHub Stats | Repository stats — stars, forks, open issues, open PRs |
| Unread Emails | Email inbox counter |
| System Log | Recent system log entries |
| Activity List | Activity timeline |
| Cron Jobs | Cron job status monitor |
| LobsterBoard Release | Version update checker |
| OpenClaw Release | OpenClaw version checker |
| Release | Generic release tracker |

### 🎨 Layout
| Widget | Description |
|--------|-------------|
| Header / Text | Custom text with formatting |
| Horizontal Line | Divider |
| Vertical Line | Vertical divider |
| Pages Menu | Navigation for custom pages |

## Custom Pages

LobsterBoard includes a pages system for adding full custom pages beyond the widget dashboard. Pages get their own route, nav entry, and optional server-side API.

```
pages/
└── my-page/
    ├── page.json       # Metadata (title, icon, order)
    ├── index.html      # Page UI
    └── api.cjs         # Optional: server-side API routes
```

Pages are auto-discovered on startup. Drop a folder in `pages/`, restart the server, and it appears in the nav.

👉 **Full guide with examples:** [`pages/README.md`](pages/README.md)

## Run on Boot

### macOS (launchd)

```bash
cat > ~/Library/LaunchAgents/com.lobsterboard.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>Label</key><string>com.lobsterboard</string>
    <key>RunAtLoad</key><true/>
    <key>KeepAlive</key><true/>
    <key>ProgramArguments</key>
    <array>
      <string>/usr/local/bin/node</string>
      <string>/path/to/lobsterboard/server.cjs</string>
    </array>
    <key>WorkingDirectory</key><string>/path/to/lobsterboard</string>
    <key>EnvironmentVariables</key>
    <dict>
      <key>PORT</key><string>8080</string>
      <key>HOST</key><string>0.0.0.0</string>
    </dict>
  </dict>
</plist>
EOF

launchctl load ~/Library/LaunchAgents/com.lobsterboard.plist
```

Update the paths to match your install location and Node.js binary (`which node`).

### Linux (systemd)

```bash
sudo cat > /etc/systemd/system/lobsterboard.service << 'EOF'
[Unit]
Description=LobsterBoard Dashboard
After=network.target

[Service]
Type=simple
User=your-user
WorkingDirectory=/path/to/lobsterboard
ExecStart=/usr/bin/node server.cjs
Environment=PORT=8080 HOST=0.0.0.0
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl enable lobsterboard
sudo systemctl start lobsterboard
```

### pm2 (any OS)

```bash
npm install -g pm2
cd /path/to/lobsterboard
PORT=8080 HOST=0.0.0.0 pm2 start server.cjs --name lobsterboard
pm2 save
pm2 startup
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/config` | GET/POST | Load/save dashboard layout |
| `/api/stats/stream` | GET | Live system stats (SSE) |
| `/api/pages` | GET | List custom pages |
| `/api/todos` | GET/POST | Todo list data |
| `/api/notes` | GET/POST | Notes widget data |
| `/api/templates` | GET | List available templates |
| `/api/templates/:id` | GET | Get template config |
| `/api/templates/:id/preview` | GET | Template preview image |
| `/api/templates/import` | POST | Import a template (merge/replace) |
| `/api/templates/export` | POST | Export current dashboard as template |
| `/api/calendar?url=` | GET | Proxy iCal feed |
| `/api/rss?url=` | GET | Proxy RSS/Atom feed |
| `/api/lb-release` | GET | LobsterBoard version check |

## File Structure

```
lobsterboard/
├── server.cjs          # Node.js server
├── app.html            # Dashboard builder
├── config.json         # Your saved layout
├── js/
│   ├── builder.js      # Editor: drag-drop, zoom, config I/O
│   ├── widgets.js      # All 50 widget definitions
│   └── templates.js    # Template gallery & export system
├── css/
│   └── builder.css     # Dark theme styles
├── templates/          # Dashboard templates
│   ├── templates.json  # Template index
│   └── */              # Individual template folders
├── pages/              # Custom pages (auto-discovered)
│   └── README.md       # Page creation guide
└── package.json
```

## Community Widgets

Community contributions are welcome! Build your own widget and share it with the LobsterBoard community.

- 📖 **[Contributing Guide](CONTRIBUTING.md)** — how to create and submit a widget
- 📁 **[Community Widgets](community-widgets/)** — browse contributed widgets and the starter template

## License

This project is licensed under the **Business Source License 1.1 (BSL-1.1)**.

You are free to use, modify, and self-host LobsterBoard for **non-commercial purposes**. Commercial use requires a separate license. See [LICENSE](LICENSE) for full terms.

## Commercial Licensing

For commercial use, OEM licensing, or enterprise deployments, contact:

📧 **curbob** on GitHub — [github.com/Curbob](https://github.com/Curbob)

---

Made with 🦞 by [Curbob](https://github.com/Curbob)

```

### File: pages\README.md
```md
# Creating Custom Pages

## Quick Start

Tell your OpenClaw agent:

> "Create a new LobsterBoard page called [name] that [description]"

Your agent will create the page folder in `pages/` with the required files.

## Where to Put Pages

Create a `pages/` folder **in the directory where you run LobsterBoard**:

```
your-project/
├── pages/              # Your custom pages go here
│   └── my-page/
├── data/               # Auto-created for page data
├── public/             # Optional: static assets (images, etc.)
├── node_modules/
└── package.json
```

If installed via npm, run from your project folder:
```bash
cd your-project
npm start
```

LobsterBoard loads pages from your directory first, then falls back to built-in pages.

## Manual Setup

### File Structure

```
pages/
└── my-page/
    ├── page.json       # Required: metadata
    ├── index.html      # Required: page HTML
    ├── api.cjs         # Optional: server-side API routes (use .cjs extension)
    └── style.css       # Optional: additional styles
```

### page.json Schema

```json
{
  "id": "my-page",           // URL slug, must match folder name
  "title": "My Page",        // Display name in nav
  "icon": "🔖",              // Emoji icon for nav
  "description": "What this page does",
  "order": 50,               // Sort position (lower = first)
  "enabled": true,           // Whether page is active
  "nav": true,               // Show in navigation bar (default: true)
  "standalone": true          // true = works without OpenClaw
}
```

### API Format (api.cjs)

> **Note:** Use `.cjs` extension since LobsterBoard's package.json has `"type": "module"`.

```js
module.exports = function(ctx) {
  // ctx.dataDir — absolute path to data/<page-id>/
  // ctx.readData(filename) — read and parse JSON file from data dir
  // ctx.writeData(filename, obj) — write JSON object to data dir

  return {
    routes: {
      'GET /': (req, res, { query, body, params }) => {
        // Return value is sent as JSON automatically
        return { items: [] };
      },

      'POST /': (req, res, { body }) => {
        // body is the parsed JSON request body
        const item = { id: Date.now().toString(), ...body };
        res.statusCode = 201;
        return item;
      },

      'GET /:id': (req, res, { params }) => {
        // :id params are extracted automatically
        return { id: params.id };
      },

      'PATCH /:id': (req, res, { body, params }) => {
        // Set res.statusCode for non-200 responses
        res.statusCode = 404;
        return { error: 'Not found' };
      },

      'DELETE /:id': (req, res, { params }) => {
        return { ok: true };
      },

      // Wildcard routes (match multiple path segments)
      'GET /*': (req, res, { params }) => {
        // params['*'] contains the matched path
        return { path: params['*'] };
      }
    }
  };
};
```

Handlers receive `(req, res, { query, body, params })`:
- **query** — parsed URL query parameters
- **body** — parsed JSON request body (POST/PATCH/DELETE)
- **params** — URL path parameters (`:id`, `*`)
- **Return value** — automatically JSON-serialized and sent

### Using the Shared Nav

Include in your `index.html`:

```html
<nav id="page-nav"></nav>
<!-- ... your page content ... -->
<script src="/pages/_shared/nav.js"></script>
```

The nav bar fetches `/api/pages` and renders links for all enabled pages, highlighting the current one.

### Important: Use Absolute Paths

Always use **absolute paths** for scripts and stylesheets in your `index.html`:

```html
<!-- ✅ Correct: absolute paths -->
<script src="/pages/my-page/script.js"></script>
<link rel="stylesheet" href="/pages/my-page/style.css">

<!-- ❌ Wrong: relative paths may break -->
<script src="script.js"></script>
```

This ensures assets load correctly regardless of how the URL is accessed.

### Storing Data

Data lives in `data/<page-id>/`. Use the `ctx` helpers:

```js
// Read
const data = ctx.readData('items.json');

// Write
ctx.writeData('items.json', { items: [...] });
```

Initialize your data file in `data/<page-id>/` with default content.

### Enable/Disable Pages

Edit `pages.json` in the LobsterBoard root:

```json
{
  "pages": {
    "my-page": { "enabled": true, "order": 50 },
    "other-page": { "enabled": false }
  }
}
```

Or set `"enabled": false` in the page's own `page.json`. The `pages.json` overrides take priority.

Restart the server after changes.

## Full Example: Bookmarks Page

### pages/bookmarks/page.json

```json
{
  "id": "bookmarks",
  "title": "Bookmarks",
  "icon": "🔖",
  "description": "Save and organize bookmarks",
  "order": 40,
  "enabled": true,
  "standalone": true
}
```

### data/bookmarks/bookmarks.json

```json
{ "bookmarks": [] }
```

### pages/bookmarks/api.cjs

```js
const crypto = require('crypto');

module.exports = function(ctx) {
  function read() {
    try { return ctx.readData('bookmarks.json'); }
    catch { return { bookmarks: [] }; }
  }
  function write(data) { ctx.writeData('bookmarks.json', data); }

  return {
    routes: {
      'GET /': (req, res, { query }) => {
        const data = read();
        let items = data.bookmarks;
        if (query.q) {
          const q = query.q.toLowerCase();
          items = items.filter(b => b.title.toLowerCase().includes(q) || b.url.toLowerCase().includes(q));
        }
        return items;
      },

      'POST /': (req, res, { body }) => {
        const data = read();
        const bookmark = {
          id: crypto.randomUUID(),
          title: body.title || 'Untitled',
          url: body.url || '',
          tags: body.tags || [],
          createdAt: new Date().toISOString()
        };
        data.bookmarks.push(bookmark);
        write(data);
        res.statusCode = 201;
        return bookmark;
      },

      'DELETE /:id': (req, res, { params }) => {
        const data = read();
        const idx = data.bookmarks.findIndex(b => b.id === params.id);
        if (idx === -1) { res.statusCode = 404; return { error: 'Not found' }; }
        data.bookmarks.splice(idx, 1);
        write(data);
        return { ok: true };
      }
    }
  };
};
```

### pages/bookmarks/index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LobsterBoard - Bookmarks</title>
  <style>
    body { font-family: -apple-system, sans-serif; background: #0d1117; color: #e6edf3; }
    .container { max-width: 800px; margin: 0 auto; padding: 1.5rem; }
    /* ... your styles ... */
  </style>
</head>
<body>
  <nav id="page-nav"></nav>
  <main class="container">
    <h1>🔖 Bookmarks</h1>
    <!-- your page content -->
  </main>
  <script src="/pages/_shared/nav.js"></script>
  <script>
    const API = '/api/pages/bookmarks';
    // ... your page logic, fetch from API ...
  </script>
</body>
</html>
```

### pages.json (add entry)

```json
{
  "pages": {
    "bookmarks": { "enabled": true, "order": 40 }
  }
}
```

Restart the server and visit `/pages/bookmarks`.

```

### File: src\index.js
```js
/**
 * LobsterBoard - Dashboard Builder Library
 * 
 * A library for building and generating dashboard configurations
 * with customizable widgets.
 * 
 * @module lobsterboard
 * @example
 * // ESM
 * import { WIDGETS, generateDashboardHtml, generateDashboardCss } from 'lobsterboard';
 * 
 * // CommonJS
 * const { WIDGETS, generateDashboardHtml } = require('lobsterboard');
 * 
 * // Browser (UMD)
 * <script src="https://unpkg.com/lobsterboard"></script>
 * const { WIDGETS } = LobsterBoard;
 */

// Widget definitions
export { 
  WIDGETS, 
  getWidgetCategories, 
  getWidget, 
  getWidgetTypes 
} from './widgets.js';

// Builder utilities
export {
  escapeHtml,
  processWidgetHtml,
  generateDashboardCss,
  generateEditJs,
  generateWidgetHtml,
  generateWidgetJs,
  generateDashboardHtml,
  generateDashboardJs,
  generateReadme
} from './builder.js';

// Re-export defaults for convenience
import { WIDGETS } from './widgets.js';
import builder from './builder.js';

// Version (will be replaced during build)
export const VERSION = '0.1.0';

// Default export for convenience
export default {
  VERSION,
  WIDGETS,
  ...builder
};

```

### File: templates\README.md
```md
# LobsterBoard Templates

Templates are pre-built dashboard layouts that can be browsed, previewed, and imported into your LobsterBoard instance.

## Creating a Template

### The Easy Way (Export)

1. Build your dashboard in LobsterBoard's edit mode
2. Click **"📦 Export Template"** in the toolbar
3. Fill in the name, description, author, and tags
4. Your template is saved automatically with sensitive data stripped

### Manual Creation

Create a folder inside `templates/` with a unique slug name:

```
templates/
└── my-template/
    ├── meta.json       # Template metadata
    ├── config.json     # Dashboard configuration
    └── preview.png     # Preview screenshot (optional, recommended)
```

#### meta.json

```json
{
  "id": "my-template",
  "name": "My Template",
  "description": "A brief description of what this dashboard does",
  "author": "your-name",
  "tags": ["monitoring", "homelab"],
  "canvasSize": "1920x1080",
  "widgetCount": 8,
  "requiresSetup": ["docker"],
  "preview": "preview.png"
}
```

#### config.json

This is a standard LobsterBoard config file with `canvas` and `widgets` array. Sensitive values (API keys, private URLs) should use placeholders:

- `"YOUR_API_KEY_HERE"` for API keys, tokens, secrets
- `"http://your-server:port/path"` for private/local URLs

Any widget with stripped data should include:
```json
"_templateNote": "⚠️ Configure this widget's settings after import"
```

#### preview.png

A screenshot of the dashboard. Recommended size: 800×450px or similar 16:9 ratio.

## Template Registry

The `templates.json` file in this directory is auto-generated. It contains an array of all `meta.json` contents. The server rebuilds it by scanning template directories on startup and when templates are added.

## Importing Templates

- **Replace**: Overwrites your entire current dashboard with the template
- **Merge**: Adds template widgets below your existing widgets (positions are offset automatically)

## Sharing Templates

To share a template, just share the template folder (the directory with `meta.json`, `config.json`, and optionally `preview.png`). Drop it into another LobsterBoard's `templates/` directory.

```

### File: js\editor\index.js
```js
/**
 * OpenClaw Dashboard Builder - Widget Index
 *
 * In the browser, this file should be loaded AFTER the shared modules
 * and BEFORE the category modules. It initializes the global WIDGETS object.
 *
 * The category modules (weather.js, system.js, etc.) add their widgets
 * to window.WIDGETS via their IIFE wrappers.
 *
 * After all category modules are loaded, window.WIDGETS contains all widget
 * definitions, and the WIDGETS variable below also references it.
 */

// Initialize the global WIDGETS object (browser)
if (typeof window !== 'undefined') {
  window.WIDGETS = window.WIDGETS || {};
}

// Make WIDGETS available as a local const for any code that expects it
const WIDGETS = (typeof window !== 'undefined') ? window.WIDGETS : {};

```

### File: js\widgets\index.js
```js
/**
 * OpenClaw Dashboard Builder - Widget Registry Initialization
 * 
 * Initializes the global WIDGETS object that other widget modules will populate.
 * This must be loaded before any widget category modules.
 */

(function() {
  'use strict';
  
  // Initialize the global widgets registry
  if (typeof window !== 'undefined') {
    window.WIDGETS = {};
  }
  
  // For Node.js environments (testing, etc.)
  if (typeof global !== 'undefined' && typeof module !== 'undefined') {
    global.WIDGETS = {};
    module.exports = global.WIDGETS;
  }
})();
```

### File: app.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LobsterBoard - Dashboard Builder</title>
  <link rel="icon" type="image/png" href="favicon.png">
  <link rel="apple-touch-icon" href="apple-touch-icon.png">
  <link rel="stylesheet" href="css/builder.css">
  <link rel="stylesheet" href="css/themes.css">
</head>
<body data-mode="view">
  <!-- Header -->
  <header class="builder-header">
    <div class="header-left">
      <img src="lobsterboard-logo-final.png" alt="LobsterBoard" class="logo-img">
      <nav class="header-nav" id="header-nav">
        <a href="changelog.html" class="nav-link">Changelog</a>
        <a href="https://github.com/curbob/LobsterBoard" target="_blank" class="nav-link">GitHub</a>
      </nav>
    </div>
    <div class="header-center">
      <div class="theme-selector">
        <label>Theme:</label>
        <select id="theme-select">
          <option value="default">🌙 Default (Dark)</option>
          <option value="feminine">🌸 Feminine</option>
          <option value="feminine-dark">💜 Feminine Dark</option>
          <option value="terminal">💻 Terminal</option>
          <option value="paper">📜 Paper</option>
        </select>
      </div>
      <label>Font Scale:</label>
      <select id="font-scale">
        <option value="0.8">80%</option>
        <option value="1" selected>100%</option>
        <option value="1.25">125%</option>
        <option value="1.5">150%</option>
        <option value="1.75">175%</option>
        <option value="2">200%</option>
      </select>
      <label>Canvas Size:</label>
      <select id="canvas-size">
        <optgroup label="Standard Displays">
          <option value="1920x1080" selected>1920×1080 (1080p)</option>
          <option value="2560x1440">2560×1440 (1440p)</option>
          <option value="3840x2160">3840×2160 (4K)</option>
          <option value="1280x720">1280×720 (720p)</option>
        </optgroup>
        <optgroup label="Laptops">
          <option value="1366x768">1366×768 (Common Laptop)</option>
          <option value="1536x864">1536×864 (Laptop)</option>
          <option value="1440x900">1440×900 (MacBook)</option>
        </optgroup>
        <optgroup label="Tablets & Small">
          <option value="1280x800">1280×800 (10" Tablet)</option>
          <option value="1024x768">1024×768 (iPad/Small)</option>
          <option value="1024x600">1024×600 (10" Netbook)</option>
          <option value="800x480">800×480 (7" Display)</option>
        </optgroup>
        <optgroup label="Ultrawide">
          <option value="2560x1080">2560×1080 (Ultrawide)</option>
          <option value="3440x1440">3440×1440 (Ultrawide QHD)</option>
        </optgroup>
        <optgroup label="Portrait Mode">
          <option value="1080x1920">1080×1920 (Portrait 1080p)</option>
          <option value="768x1024">768×1024 (Portrait Tablet)</option>
        </optgroup>
        <option value="custom">Custom...</option>
        <optgroup label="Special">
          <option value="scrollable">Full Page (Scrollable)</option>
        </optgroup>
      </select>
      <input type="number" id="custom-width" placeholder="Width" style="display:none; width:80px;">
      <span id="custom-x" style="display:none;">×</span>
      <input type="number" id="custom-height" placeholder="Height" style="display:none; width:80px;">
    </div>
    <div class="header-right">
      <button class="btn btn-secondary" id="btn-servers">🖥️ Servers</button>
      <button class="btn btn-secondary" id="btn-security">🔒 Security</button>
      <button class="btn btn-secondary" id="btn-templates">📋 Templates</button>
      <button class="btn btn-secondary" id="btn-export-template">📦 Export Template</button>
      <button class="btn btn-secondary" id="btn-clear">Clear All</button>
      <button class="btn btn-secondary" id="btn-preview">Preview</button>
      <button class="btn btn-primary" id="btn-save">💾 Save</button>
      <button class="btn btn-done" id="btn-done-editing">✓ Done</button>
    </div>
  </header>

  <!-- Edit button for view mode (fixed position) -->
  <button id="btn-edit-layout" class="btn btn-primary edit-layout-btn">Edit Layout</button>

  <!-- Empty dashboard hint (view mode only) -->
  <div class="view-empty-hint">
    <div class="hint-icon">🦞</div>
    <div class="hint-text">Your dashboard is empty</div>
    <div class="hint-shortcut">Press <kbd>Ctrl</kbd> + <kbd>E</kbd> to add widgets</div>
  </div>

  <div class="builder-main">
    <!-- Widget Library Panel -->
    <aside class="widget-panel">
      <h3>📦 Widgets</h3>

      <div class="widget-sections">
      <!-- Basics -->
      <div class="widget-section">
        <h4>📌 Basics</h4>
        <div class="widget-list">
          <div class="widget-item" draggable="true" data-widget="weather">
            <span class="widget-icon">🌡️</span>
            <span class="widget-name">Local Weather</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="weather-multi">
            <span class="widget-icon">🌍</span>
            <span class="widget-name">World Weather</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="clock">
            <span class="widget-icon">🕐</span>
            <span class="widget-name">Clock</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="world-clock">
            <span class="widget-icon">🌍</span>
            <span class="widget-name">World Clock</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="countdown">
            <span class="widget-icon">⏳</span>
            <span class="widget-name">Countdown</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
        </div>
      </div>

      <!-- System Monitoring -->
      <div class="widget-section">
        <h4>💻 System</h4>
        <div class="widget-list">
          <div class="widget-item" draggable="true" data-widget="cpu-memory">
            <span class="widget-icon">💻</span>
            <span class="widget-name">CPU / Memory</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="disk-usage">
            <span class="widget-icon">💾</span>
            <span class="widget-name">Disk Usage</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="network-speed">
            <span class="widget-icon">🌐</span>
            <span class="widget-name">Network Speed</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="docker-containers">
            <span class="widget-icon">🐳</span>
            <span class="widget-name">Docker</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="uptime-monitor">
            <span class="widget-icon">📡</span>
            <span class="widget-name">Uptime Monitor</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="system-graphical">
            <span class="widget-icon">💻</span>
            <span class="widget-name">System (Graphical)</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
        </div>
      </div>

      <!-- Health -->
      <div class="widget-section">
        <h4>❤️ Health</h4>
        <div class="widget-list">
          <div class="widget-item" draggable="true" data-widget="sleep-ring">
            <span class="widget-icon">😴</span>
            <span class="widget-name">Sleep Score</span>
          </div>
        </div>
      </div>

      <!-- OpenClaw -->
      <div class="widget-section">
        <h4>🐾 OpenClaw</h4>
        <div class="widget-list">
          <div class="widget-item" draggable="true" data-widget="auth-status">
            <span class="widget-icon">🔐</span>
            <span class="widget-name">Auth Status</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="lobsterboard-release">
            <span class="widget-icon">🦞</span>
            <span class="widget-name">LobsterBoard Release</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="openclaw-release">
            <span class="widget-icon">🦞</span>
            <span class="widget-name">OpenClaw Release</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="release">
            <span class="widget-icon">📦</span>
            <span class="widget-name">Release</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="activity-list">
            <span class="widget-icon">📋</span>
            <span class="widget-name">Activity List</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="cron-jobs">
            <span class="widget-icon">⏰</span>
            <span class="widget-name">Cron Jobs</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="system-log">
            <span class="widget-icon">🔧</span>
            <span class="widget-name">System Log</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
        </div>
      </div>

      <!-- AI / LLM -->
      <div class="widget-section">
        <h4>🤖 AI / LLM</h4>
        <div class="widget-list">
          <div class="widget-item" draggable="true" data-widget="ai-usage">
            <span class="widget-icon">🤖</span>
            <span class="widget-name">AI Usage</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="claude-code">
            <span class="widget-icon">🟣</span>
            <span class="widget-name">Claude Code</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="codex-cli">
            <span class="widget-icon">🟢</span>
            <span class="widget-name">Codex CLI</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="github-copilot">
            <span class="widget-icon">⚫</span>
            <span class="widget-name">GitHub Copilot</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="cursor">
            <span class="widget-icon">🔵</span>
            <span class="widget-name">Cursor</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="gemini-cli">
            <span class="widget-icon">🔷</span>
            <span class="widget-name">Gemini CLI</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="amp-code">
            <span class="widget-icon">⚡</span>
            <span class="widget-name">Amp Code</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="factory">
            <span class="widget-icon">🏭</span>
            <span class="widget-name">Factory</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="kimi-code">
            <span class="widget-icon">🌙</span>
            <span class="widget-name">Kimi Code</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="jetbrains-ai">
            <span class="widget-icon">🧠</span>
            <span class="widget-name">JetBrains AI</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="minimax">
            <span class="widget-icon">🔶</span>
            <span class="widget-name">MiniMax</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="zai">
            <span class="widget-icon">🇿</span>
            <span class="widget-name">Z.ai</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="antigravity-local">
            <span class="widget-icon">🪐</span>
            <span class="widget-name">Antigravity</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="ai-cost-tracker">
            <span class="widget-icon">💰</span>
            <span class="widget-name">Cost Tracker</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="api-status">
            <span class="widget-icon">🔄</span>
            <span class="widget-name">API Status</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="session-count">
            <span class="widget-icon">💬</span>
            <span class="widget-name">Active Sessions</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="token-gauge">
            <span class="widget-icon">📊</span>
            <span class="widget-name">Token Gauge</span>
          </div>
        </div>
      </div>

      <!-- Productivity -->
      <div class="widget-section">
        <h4>📋 Productivity</h4>
        <div class="widget-list">
          <div class="widget-item" draggable="true" data-widget="todo-list">
            <span class="widget-icon">✅</span>
            <span class="widget-name">Todo List</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="calendar">
            <span class="widget-icon">📅</span>
            <span class="widget-name">Calendar</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="email-count">
          
... [TRUNCATED]
```

### File: changelog.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Changelog - LobsterBoard</title>
  <link rel="icon" type="image/png" href="favicon.png">
  <link rel="apple-touch-icon" href="apple-touch-icon.png">
  <style>
    :root {
      --bg-primary: #0d1117;
      --bg-secondary: #161b22;
      --bg-tertiary: #21262d;
      --text-primary: #e6edf3;
      --text-secondary: #8b949e;
      --text-muted: #6e7681;
      --border: #30363d;
      --accent: #58a6ff;
      --accent-green: #3fb950;
      --accent-purple: #a371f7;
      --accent-orange: #d29922;
    }

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
      background: var(--bg-primary);
      color: var(--text-primary);
      line-height: 1.6;
      min-height: 100vh;
    }

    header {
      background: var(--bg-secondary);
      border-bottom: 1px solid var(--border);
      padding: 16px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .logo {
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: var(--text-primary);
    }

    .logo img {
      height: 36px;
    }

    .nav-links {
      display: flex;
      gap: 24px;
    }

    .nav-links a {
      color: var(--text-secondary);
      text-decoration: none;
      font-size: 14px;
      transition: color 0.2s;
    }

    .nav-links a:hover {
      color: var(--text-primary);
    }

    .nav-links a.active {
      color: var(--accent);
    }

    main {
      max-width: 800px;
      margin: 0 auto;
      padding: 48px 24px;
    }

    h1 {
      font-size: 32px;
      margin-bottom: 8px;
    }

    .subtitle {
      color: var(--text-secondary);
      margin-bottom: 48px;
    }

    .version {
      margin-bottom: 48px;
    }

    .version-header {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 24px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--border);
    }

    .version-number {
      font-size: 24px;
      font-weight: 600;
      color: var(--accent);
    }

    .version-date {
      color: var(--text-muted);
      font-size: 14px;
    }

    .version-tag {
      background: var(--accent-green);
      color: var(--bg-primary);
      padding: 2px 8px;
      border-radius: 12px;
      font-size: 12px;
      font-weight: 600;
    }

    .version-tag.initial {
      background: var(--accent-purple);
    }

    .change-section {
      margin-bottom: 24px;
    }

    .change-section h3 {
      font-size: 16px;
      color: var(--text-secondary);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .change-section h3::before {
      font-size: 18px;
    }

    .change-section.added h3::before { content: '✨'; }
    .change-section.changed h3::before { content: '🔄'; }
    .change-section.fixed h3::before { content: '🐛'; }
    .change-section.removed h3::before { content: '🗑️'; }

    .change-section ul {
      list-style: none;
      padding-left: 0;
    }

    .change-section li {
      padding: 8px 0;
      padding-left: 24px;
      position: relative;
      border-bottom: 1px solid var(--bg-tertiary);
    }

    .change-section li:last-child {
      border-bottom: none;
    }

    .change-section li::before {
      content: '•';
      position: absolute;
      left: 8px;
      color: var(--text-muted);
    }

    .change-category {
      display: block;
      font-size: 13px;
      color: var(--text-muted);
      margin-top: 4px;
    }

    .widget-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 8px;
      margin-top: 12px;
    }

    .widget-tag {
      background: var(--bg-tertiary);
      padding: 6px 10px;
      border-radius: 6px;
      font-size: 13px;
      color: var(--text-secondary);
    }

    .upcoming {
      background: var(--bg-secondary);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 24px;
      margin-top: 48px;
    }

    .upcoming h2 {
      font-size: 18px;
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .upcoming ul {
      list-style: none;
      padding: 0;
    }

    .upcoming li {
      padding: 8px 0;
      color: var(--text-secondary);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .upcoming li::before {
      content: '○';
      color: var(--text-muted);
    }

    footer {
      text-align: center;
      padding: 48px 24px;
      color: var(--text-muted);
      font-size: 14px;
    }

    footer a {
      color: var(--accent);
      text-decoration: none;
    }

    footer a:hover {
      text-decoration: underline;
    }

    .mascot {
      position: fixed;
      bottom: 20px;
      right: 20px;
      width: 80px;
      opacity: 0.6;
      transition: opacity 0.2s;
    }

    .mascot:hover {
      opacity: 1;
    }

    @media (max-width: 600px) {
      .nav-links {
        gap: 16px;
      }
      
      .version-header {
        flex-wrap: wrap;
      }

      .widget-grid {
        grid-template-columns: 1fr 1fr;
      }

      .mascot {
        display: none;
      }
    }
  </style>
</head>
<body>
  <header>
    <a href="app.html" class="logo">
      <img src="lobsterboard-logo-final.png" alt="LobsterBoard">
    </a>
    <nav class="nav-links">
      <a href="app.html">Dashboard</a>
      <a href="changelog.html" class="active">Changelog</a>
      <a href="https://github.com/curbob/LobsterBoard" target="_blank">GitHub</a>
    </nav>
  </header>

  <main>
    <h1>Changelog</h1>
    <p class="subtitle">All notable changes to LobsterBoard will be documented here.</p>

    <!-- Version 0.3.1 -->
    <article class="version">
      <div class="version-header">
        <span class="version-number">v0.3.1</span>
        <span class="version-date">February 28, 2026</span>
      </div>
      <div class="version-body">
        <section class="change-section fixed">
          <h3>Fixed</h3>
          <ul>
            <li><strong>Edit mode header clutter</strong> — page navigation links now hide when entering edit mode to reduce header crowding</li>
          </ul>
        </section>
      </div>
    </article>

    <!-- Version 0.3.0 -->
    <article class="version">
      <div class="version-header">
        <span class="version-number">v0.3.0</span>
        <span class="version-date">February 28, 2026</span>
        <span class="version-tag">Major</span>
      </div>
      <div class="version-body">
        <section class="change-section added">
          <h3>Added</h3>
          <ul>
            <li><strong>Theme switcher</strong> — 5 beautiful themes: Default (dark), Feminine (pastel pink/lavender), Feminine Dark, Terminal (green CRT), Paper (cream/sepia)</li>
            <li><strong>Phosphor icon system</strong> — themed widgets use Phosphor icons; Default theme keeps emoji</li>
            <li><strong>Theme selector dropdown</strong> in edit mode header</li>
            <li>Theme persists to localStorage and dashboard config</li>
            <li><strong>Themes showcase</strong> on website and README with lightbox gallery</li>
          </ul>
        </section>
      </div>
    </article>

    <!-- Version 0.2.6 -->
    <article class="version">
      <div class="version-header">
        <span class="version-number">v0.2.6</span>
        <span class="version-date">February 23, 2026</span>
      </div>
      <div class="version-body">
        <section class="change-section fixed">
          <h3>Fixed</h3>
          <ul>
            <li><strong>Version suffix comparison</strong> — versions like <code>2026.2.22-2</code> (npm post-release patches) now correctly match GitHub tags like <code>v2026.2.22</code>, fixing false "Update available" indicators — thanks @JamesTsetsekas!</li>
          </ul>
        </section>
      </div>
    </article>

    <!-- Version 0.2.5 -->
    <article class="version">
      <div class="version-header">
        <span class="version-number">v0.2.5</span>
        <span class="version-date">February 19, 2026</span>
        <span class="version-tag">Community</span>
      </div>
      <div class="version-body">
        <section class="change-section fixed">
          <h3>Fixed</h3>
          <ul>
            <li><strong>iCal timezone parsing</strong> — calendar events now display at correct times regardless of timezone (TZID parameter support) — thanks @jlgrimes!</li>
          </ul>
        </section>
        <section class="change-section added">
          <h3>Added</h3>
          <ul>
            <li><strong>Clickable URLs in calendar</strong> — Zoom/Teams links in event summaries and locations are now hyperlinks — thanks @jlgrimes!</li>
          </ul>
        </section>
      </div>
    </article>

    <!-- Version 0.2.4 -->
    <article class="version">
      <div class="version-header">
        <span class="version-number">v0.2.4</span>
        <span class="version-date">February 17, 2026</span>
        <span class="version-tag">Security</span>
      </div>
      <div class="version-body">
        <section class="change-section fixed">
          <h3>Fixed</h3>
          <ul>
            <li><strong>SSRF vulnerability</strong> in RSS feed proxy — thanks @jlgrimes for the security report!</li>
          </ul>
        </section>
      </div>
    </article>

    <!-- Version 0.2.3 -->
    <article class="version">
      <div class="version-header">
        <span class="version-number">v0.2.3</span>
        <span class="version-date">February 16, 2026</span>
        <span class="version-tag">Security</span>
      </div>
      <div class="version-body">
        <h3>🔐 Security & Privacy</h3>
        <ul>
          <li><strong>PIN-locked edit mode</strong> — set a 4-6 digit PIN to prevent unauthorized editing (SHA-256 hashed, server-side only)</li>
          <li><strong>Server-side secrets store</strong> — API keys, calendar URLs, and tokens stored securely, never sent to browser</li>
          <li><strong>Public Mode</strong> — hides edit button and blocks config APIs; subtle 🔒 unlock button for admin access</li>
          <li><strong>Privacy warnings</strong> on sensitive widgets (System Log, Activity List, Cron Jobs, Calendar, Todo List)</li>
          <li>Template export now strips private calendar URLs with auth tokens</li>
          <li>Pre-commit hook blocks private data in template files</li>
        </ul>
        <h3>👥 Community</h3>
        <ul>
          <li><strong>Community Widgets</strong> — contribution guide, widget templates, and PR checklist for submissions</li>
        </ul>
      </div>
    </article>

    <!-- Version 0.2.2 -->
    <article class="version">
      <div class="version-header">
        <span class="version-number">v0.2.2</span>
        <span class="version-date">February 16, 2026</span>
      </div>
      <div class="version-body">
        <h3>🐛 Fixes</h3>
        <ul>
          <li>Removed private calendar URL accidentally included in template config</li>
          <li>Fixed template export sanitization for URLs with embedded auth tokens</li>
        </ul>
      </div>
    </article>

    <!-- Version 0.2.1 -->
    <article class="version">
      <div class="version-header">
        <span class="version-number">v0.2.1</span>
        <span class="version-date">February 15, 2026</span>
      </div>
      <div class="version-body">
        <h3>🐛 Fixes</h3>
        <ul>
          <li>Minor bug fixes and stability improvements</li>
        </ul>
      </div>
    </article>

    <!-- Version 0.2.0 -->
    <article class="version">
      <div class="version-header">
        <span class="version-number">v0.2.0</span>
        <span class="version-date">February 15, 2026</span>
        <span class="version-tag">Major</span>
      </div>
      <div class="version-body">
        <h3>✨ New Features</h3>
        <ul>
          <li><strong>Template Gallery</strong> — export, import, and share dashboard layouts with auto-screenshot previews</li>
          <li><strong>Notes widget</strong> — persistent rich-text notes with auto-save</li>
          <li><strong>GitHub Stats widget</strong> — profile contributions, stars, and activity</li>
          <li><strong>LobsterBoard Release widget</strong> — version update checker</li>
          <li><strong>SSE streaming</strong> for real-time system stats</li>
          <li><strong>Directory browser</strong> for image widgets</li>
          <li>Scrollable canvas mode</li>
          <li>html2canvas dashboard screenshot export</li>
          <li>Widget count: 47 → 50</li>
        </ul>
        <h3>🔄 Changed</h3>
        <ul>
          <li>License changed from MIT to BSL-1.1</li>
          <li>Stock Ticker widget — fixed hasApiKey check</li>
          <li>Builder — contenteditable keyboard fix, null-checks throughout</li>
        </ul>
      </div>
    </article>

    <!-- Version 0.1.6 -->
    <article class="version">
      <div class="version-header">
        <span class="version-number">v0.1.6</span>
        <span class="version-date">February 14, 2026</span>
      </div>
      <div class="version-body">
        <h3>🚀 Initial npm Release</h3>
        <ul>
          <li>47 widgets, drag-and-drop editor, custom pages system</li>
          <li>SSRF protection for proxy endpoints</li>
        </ul>
      </div>
    </article>

    <!-- Version 0.1.1 -->
    <article class="version">
      <div class="version-header">
        <span class="version-number">v0.1.1</span>
        <span class="version-date">February 6, 2026</span>
      </div>

      <section class="change-section changed">
        <h3>Changed</h3>
        <ul>
          <li>Moved mascot from left sidebar to right (properties panel)</li>
          <li>Mascot now pinned to bottom of panel (doesn't float up with content)</li>
        </ul>
      </section>

      <section class="change-section fixed">
        <h3>Fixed</h3>
        <ul>
          <li>Mascot positioning using flexbox margin-top: auto</li>
        </ul>
      </section>
    </article>

    <!-- Version 0.1.0 -->
    <article class="version">
      <div class="version-header">
        <span class="version-number">v0.1.0</span>
        <span class="version-date">February 5, 2026</span>
        <span class="version-tag initial">Initial Release</span>
      </div>

      <section class="change-section added">
        <h3>Added</h3>
        <ul>
          <li>
            <strong>Core Builder</strong>
            <span class="change-category">Drag-and-drop widget placement, grid snapping (20px), resize handles, properties panel</span>
          </li>
          <li>
            <strong>Canvas Controls</strong>
            <span class="change-category">15+ screen size pre
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
