---
id: lobsterboard-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:05.776227
---

# KNOWLEDGE EXTRACT: LobsterBoard
> **Extracted on:** 2026-03-30 17:42:02
> **Source:** LobsterBoard

---

## File: `.gitignore`
```
/config.json
/todos.json
/notes.json
data/
*.log
node_modules/
.env

# Security - never commit
auth.json
secrets.json
```

## File: `app.html`
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
            <span class="widget-icon">📧</span>
            <span class="widget-name">Unread Emails</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="pomodoro">
            <span class="widget-icon">🎯</span>
            <span class="widget-name">Pomodoro</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="notes">
            <span class="widget-icon">📝</span>
            <span class="widget-name">Notes</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="github-stats">
            <span class="widget-icon">🐙</span>
            <span class="widget-name">GitHub Stats</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
        </div>
      </div>

      <!-- Finance -->
      <div class="widget-section">
        <h4>💵 Finance</h4>
        <div class="widget-list">
          <div class="widget-item" draggable="true" data-widget="stock-ticker">
            <span class="widget-icon">📈</span>
            <span class="widget-name">Stock Ticker</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="crypto-price">
            <span class="widget-icon">₿</span>
            <span class="widget-name">Crypto Price</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
        </div>
      </div>

      <!-- Smart Home section removed: requires IoT integrations, too niche -->

      <!-- Entertainment -->
      <div class="widget-section">
        <h4>🎵 Entertainment</h4>
        <div class="widget-list">
          <!-- Now Playing removed: requires Spotify OAuth, too much friction -->
          <div class="widget-item" draggable="true" data-widget="quote-of-day">
            <span class="widget-icon">💭</span>
            <span class="widget-name">Quote of Day</span>
          </div>
        </div>
      </div>

      <!-- Content -->
      <div class="widget-section">
        <h4>🔗 Content</h4>
        <div class="widget-list">
          <div class="widget-item" draggable="true" data-widget="pages-menu">
            <span class="widget-icon">📄</span>
            <span class="widget-name">Pages Menu</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="quick-links">
            <span class="widget-icon">🔗</span>
            <span class="widget-name">Quick Links</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="image-local">
            <span class="widget-icon">🖼️</span>
            <span class="widget-name">Image</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="image-embed">
            <span class="widget-icon">🌐</span>
            <span class="widget-name">Web Image</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="image-random">
            <span class="widget-icon">🎲</span>
            <span class="widget-name">Random Image</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="image-latest">
            <span class="widget-icon">🆕</span>
            <span class="widget-name">Latest Image</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="iframe-embed">
            <span class="widget-icon">🌐</span>
            <span class="widget-name">Iframe Embed</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
        </div>
      </div>

      <!-- Layout -->
      <div class="widget-section">
        <h4>📐 Layout</h4>
        <div class="widget-list">
          <div class="widget-item" draggable="true" data-widget="text-header">
            <span class="widget-icon">🔤</span>
            <span class="widget-name">Header / Text</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="horizontal-line">
            <span class="widget-icon">➖</span>
            <span class="widget-name">Horizontal Line</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
          <div class="widget-item" draggable="true" data-widget="vertical-line">
            <span class="widget-icon">│</span>
            <span class="widget-name">Vertical Line</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
        </div>
      </div>

      <!-- Bars -->
      <div class="widget-section">
        <h4>📊 Bars</h4>
        <div class="widget-list">
          <div class="widget-item" draggable="true" data-widget="rss-ticker">
            <span class="widget-icon">📡</span>
            <span class="widget-name">RSS Ticker</span>
            <span class="widget-verified" title="Tested & Verified">✓</span>
          </div>
        </div>
      </div>
      </div><!-- end widget-sections -->
    </aside>

    <!-- Canvas Area -->
    <main class="canvas-area">
      <div class="canvas-wrapper" id="canvas-wrapper">
        <div class="canvas" id="canvas" data-width="1920" data-height="1080" style="width:1920px;height:1080px;">
          <div class="canvas-grid"></div>
          <div class="drop-hint">Drag widgets here</div>
        </div>
      </div>
      <div class="canvas-info">
        <span id="canvas-dimensions">1920 × 1080</span>
        <span id="widget-count">0 widgets</span>
        <div class="zoom-controls" style="display:flex;align-items:center;gap:6px;">
          <button onclick="zoomOut()" style="background:none;border:none;color:#8b949e;font-size:16px;cursor:pointer;padding:4px 8px;" title="Zoom Out">-</button>
          <span id="zoom-level" style="color:#8b949e;font-size:12px;min-width:40px;text-align:center;">50%</span>
          <button onclick="zoomIn()" style="background:none;border:none;color:#8b949e;font-size:16px;cursor:pointer;padding:4px 8px;" title="Zoom In">+</button>
          <button onclick="zoomFit()" style="background:none;border:none;color:#8b949e;font-size:14px;cursor:pointer;padding:4px 8px;" title="Fit to Screen">⊡</button>
          <button onclick="zoom100()" style="background:none;border:none;color:#8b949e;font-size:11px;cursor:pointer;padding:4px 8px;" title="100%">1:1</button>
        </div>
      </div>
    </main>

    <!-- Properties Panel -->
    <aside class="properties-panel" id="properties-panel">
      <h3>⚙️ Properties</h3>
      <div class="no-selection">
        <p>Select a widget to edit its properties</p>
      </div>
      <div class="properties-form" id="properties-form" style="display:none;">
        <div class="prop-group">
          <label>Widget Type</label>
          <input type="text" id="prop-type" readonly>
        </div>
        <div class="prop-group" id="prop-title-group">
          <label id="prop-title-label">Title</label>
          <div style="display:flex;align-items:center;gap:8px;">
            <input type="text" id="prop-title" placeholder="Widget title" style="flex:1;">
            <input type="checkbox" id="prop-show-header" checked style="width:auto;">
            <label for="prop-show-header" style="margin:0;cursor:pointer;white-space:nowrap;font-size:11px;">Show</label>
          </div>
          <small id="prop-title-hint" style="display:none;"></small>
        </div>
        <div class="prop-group">
          <label>Position</label>
          <div class="prop-row">
            <input type="number" id="prop-x" placeholder="X">
            <input type="number" id="prop-y" placeholder="Y">
          </div>
        </div>
        <div class="prop-group">
          <label>Size</label>
          <div class="prop-row">
            <input type="number" id="prop-width" placeholder="W">
            <input type="number" id="prop-height" placeholder="H">
          </div>
        </div>
        <div class="prop-group" id="prop-location-group" style="display:none;">
          <label>Location</label>
          <input type="text" id="prop-location" placeholder="City name or City, Country">
          <small>e.g. Atlanta or Paris, FR</small>
        </div>
        <div class="prop-group" id="prop-locations-group" style="display:none;">
          <label>Locations</label>
          <input type="text" id="prop-locations" placeholder="New York; London; Tokyo">
          <small>Semicolon-separated. Use "City, Country" for duplicates</small>
        </div>
        <div class="prop-group" id="prop-units-group" style="display:none;">
          <label>Units</label>
          <select id="prop-units">
            <option value="F">Fahrenheit (°F)</option>
            <option value="C">Celsius (°C)</option>
          </select>
        </div>
        <div class="prop-group" id="prop-timeformat-group" style="display:none;">
          <label>Time Format</label>
          <select id="prop-timeformat">
            <option value="12h">12 Hour (3:45 PM)</option>
            <option value="24h">24 Hour (15:45)</option>
          </select>
        </div>
        <div class="prop-group" id="prop-targetdate-group" style="display:none;">
          <label>Target Date</label>
          <input type="date" id="prop-targetdate">
        </div>
        <div class="prop-group" id="prop-countdown-options-group" style="display:none;">
          <label>Display Options</label>
          <div style="display:flex;flex-direction:column;gap:6px;">
            <div style="display:flex;align-items:center;gap:8px;">
              <input type="checkbox" id="prop-show-hours" style="width:auto;">
              <label for="prop-show-hours" style="margin:0;cursor:pointer;font-size:12px;">Show Hours</label>
            </div>
            <div style="display:flex;align-items:center;gap:8px;">
              <input type="checkbox" id="prop-show-minutes" style="width:auto;">
              <label for="prop-show-minutes" style="margin:0;cursor:pointer;font-size:12px;">Show Minutes</label>
            </div>
          </div>
        </div>
        <div class="prop-group" id="prop-fontsize-group" style="display:none;">
          <label>Font Size (px)</label>
          <input type="number" id="prop-fontsize" min="8" max="120" placeholder="24">
        </div>
        <div class="prop-group" id="prop-fontcolor-group" style="display:none;">
          <label>Font Color</label>
          <input type="color" id="prop-fontcolor" value="#e6edf3" style="width:100%;height:32px;border:none;cursor:pointer;">
        </div>
        <div class="prop-group" id="prop-textalign-group" style="display:none;">
          <label>Alignment</label>
          <select id="prop-textalign">
            <option value="left">Left</option>
            <option value="center">Center</option>
            <option value="right">Right</option>
          </select>
        </div>
        <div class="prop-group" id="prop-fontweight-group" style="display:none;">
          <label>Font Weight</label>
          <select id="prop-fontweight">
            <option value="normal">Normal</option>
            <option value="bold">Bold</option>
            <option value="lighter">Light</option>
          </select>
        </div>
        <div class="prop-group" id="prop-showborder-group" style="display:none;">
          <label>Border</label>
          <div style="display:flex;align-items:center;gap:8px;">
            <input type="checkbox" id="prop-showborder" style="width:auto;">
            <label for="prop-showborder" style="margin:0;cursor:pointer;font-size:12px;">Show Border</label>
          </div>
        </div>
        <div class="prop-group" id="prop-linecolor-group" style="display:none;">
          <label>Line Color</label>
          <input type="color" id="prop-linecolor" value="#30363d" style="width:100%;height:32px;border:none;cursor:pointer;">
        </div>
        <div class="prop-group" id="prop-linethickness-group" style="display:none;">
          <label>Line Thickness (px)</label>
          <input type="number" id="prop-linethickness" min="1" max="20" placeholder="2">
        </div>
        <div class="prop-group" id="prop-feedurl-group" style="display:none;">
          <label>Feed URL</label>
          <input type="text" id="prop-feedurl" placeholder="https://example.com/feed.xml" style="width:100%;padding:6px 8px;background:var(--bg-secondary,#0d1117);border:1px solid var(--border,#30363d);border-radius:4px;color:var(--text,#e6edf3);font-size:12px;">
        </div>
        <div class="prop-group" id="prop-columns-group" style="display:none;">
          <label>Columns</label>
          <select id="prop-columns">
            <option value="1">1 Column</option>
            <option value="2">2 Columns</option>
          </select>
        </div>
        <div class="prop-group" id="prop-pomodoro-group" style="display:none;">
          <label>Timer Settings</label>
          <div style="display:flex;gap:8px;align-items:center;">
            <div style="flex:1;">
              <small style="display:block;margin-bottom:2px;">Work (min)</small>
              <input type="number" id="prop-work-minutes" min="1" max="120" style="width:100%;">
            </div>
            <div style="flex:1;">
              <small style="display:block;margin-bottom:2px;">Break (min)</small>
              <input type="number" id="prop-break-minutes" min="1" max="60" style="width:100%;">
            </div>
          </div>
        </div>
        <div class="prop-group" id="prop-imagepath-group" style="display:none;">
          <label>Image</label>
          <input type="file" id="prop-imagefile" accept="image/*" style="margin-bottom:8px;">
          <input type="text" id="prop-imagepath" placeholder="Or enter path: images/photo.jpg">
          <small>Browse to embed, or enter relative path</small>
        </div>
        <div class="prop-group" id="prop-imageurl-group" style="display:none;">
          <label>Image URL</label>
          <input type="text" id="prop-imageurl" placeholder="https://example.com/image.jpg">
        </div>
        <div class="prop-group" id="prop-imagelist-group" style="display:none;">
          <label>Images</label>
          <input type="file" id="prop-imagelist-file" accept="image/*" multiple style="margin-bottom:8px;">
          <small>Select images to add to the rotation</small>
          <div id="prop-imagelist-items" style="margin-top:8px;max-height:150px;overflow-y:auto;"></div>
        </div>
        <div class="prop-group" id="prop-quicklinks-group" style="display:none;">
          <label>Links</label>
          <div style="display:flex;gap:4px;margin-bottom:8px;">
            <input type="text" id="prop-link-name" placeholder="Name" style="flex:1;">
            <input type="text" id="prop-link-url" placeholder="https://..." style="flex:2;">
            <button type="button" id="prop-link-add" style="padding:4px 8px;cursor:pointer;">+</button>
          </div>
          <div id="prop-quicklinks-items" style="max-height:150px;overflow-y:auto;"></div>
        </div>
        <div class="prop-group" id="prop-layout-group" style="display:none;">
          <label>Menu Direction</label>
          <select id="prop-layout">
            <option value="vertical">Vertical</option>
            <option value="horizontal">Horizontal</option>
          </select>
        </div>
        <!-- showBorder handled by existing prop-showborder checkbox -->
        <div class="prop-group" id="prop-embedurl-group" style="display:none;">
          <label>Embed URL</label>
          <input type="text" id="prop-embedurl" placeholder="https://example.com">
          <small>URL to embed in iframe</small>
        </div>
        <div class="prop-group" id="prop-release-group" style="display:none;">
          <label>GitHub Repo</label>
          <input type="text" id="prop-repo" placeholder="owner/repo">
          <small style="margin-bottom:8px;display:block;">e.g. openclaw/openclaw</small>
          <label>Your Version</label>
          <input type="text" id="prop-currentversion" placeholder="v1.0.0">
          <small>Leave blank to just show latest</small>
        </div>
        <div class="prop-group" id="prop-github-group" style="display:none;">
          <label>GitHub Username / Org</label>
          <input type="text" id="prop-gh-username" placeholder="openclaw">
          <label style="margin-top:8px;">Repository</label>
          <input type="text" id="prop-gh-repo" placeholder="openclaw">
          <label style="margin-top:8px;">API Token <span style="color:var(--text-muted);font-weight:normal;">(optional)</span></label>
          <input type="password" id="prop-gh-apikey" placeholder="ghp_...">
          <small style="color:var(--text-muted);margin-top:4px;display:block;line-height:1.4;">Without a token: 60 requests/hr.<br>With a token: 5,000 requests/hr.<br>Create one at github.com → Settings → Developer Settings → Personal Access Tokens (no scopes needed for public repos).</small>
        </div>
        <div class="prop-group" id="prop-openclawurl-group" style="display:none;">
          <label>OpenClaw URL</label>
          <input type="text" id="prop-openclawurl" placeholder="http://localhost:18789">
          <small>Full URL to your OpenClaw gateway</small>
          <div style="margin-top:8px;padding:8px;background:var(--bg-tertiary);border-radius:4px;font-size:11px;color:var(--text-secondary);">
            ⚠️ Preview will show error (CORS).<br>
            Works when exported and run with <code>node server.js</code>
          </div>
        </div>
        <div class="prop-group" id="prop-api-group" style="display:none;">
          <label>API Key Variable</label>
          <input type="text" id="prop-api-key" readonly style="color:#8b949e;cursor:default;">
          <label style="margin-top:8px;">API Key</label>
          <input type="password" id="prop-api-key-value" placeholder="Paste your API key here" style="font-size:12px;">
          <small id="prop-api-note" style="display:none;color:#8b949e;margin-top:4px;line-height:1.4;font-style:italic;">
          </small>
        </div>
        <div class="prop-group" id="prop-endpoint-group" style="display:none;">
          <label>API Endpoint</label>
          <input type="text" id="prop-endpoint" placeholder="https://api.example.com">
        </div>
        <div class="prop-group" id="prop-directorypath-group" style="display:none;">
          <label>Directory Path</label>
          <div style="display:flex;gap:4px;">
            <input type="text" id="prop-directorypath" placeholder="~/images" style="flex:1;">
            <button type="button" id="btn-browse-dir" style="padding:4px 10px;background:var(--bg-tertiary);border:1px solid var(--border-color);border-radius:6px;color:var(--text-primary);cursor:pointer;white-space:nowrap;" title="Browse directories">📁 Browse</button>
          </div>
          <div id="dir-browser" style="display:none;margin-top:8px;max-height:200px;overflow-y:auto;background:var(--bg-tertiary);border:1px solid var(--border-color);border-radius:6px;padding:8px;font-size:12px;">
          </div>
        </div>
        <div class="prop-group" id="prop-server-group" style="display:none;">
          <label>Server</label>
          <select id="prop-server">
            <option value="local">Local</option>
            <!-- Remote servers populated dynamically -->
          </select>
          <small style="color:#8b949e;margin-top:4px;display:block;">Select data source for this widget</small>
        </div>
        <div class="prop-group">
          <label>Refresh Interval (sec)</label>
          <input type="number" id="prop-refresh" placeholder="60" min="0">
        </div>
        <div class="prop-group" id="prop-widgetfontscale-group">
          <label>Content Font Adjust</label>
          <select id="prop-widgetfontscale">
            <option value="0">Default (global)</option>
            <option value="-25">−25%</option>
            <option value="-20">−20%</option>
            <option value="-15">−15%</option>
            <option value="-10">−10%</option>
            <option value="-5">−5%</option>
            <option value="5">+5%</option>
            <option value="10">+10%</option>
            <option value="15">+15%</option>
            <option value="20">+20%</option>
            <option value="25">+25%</option>
          </select>
        </div>
        <div id="prop-extra-container"></div>
        <div class="prop-group" id="prop-description-group">
          <div id="prop-description" style="font-size:11px;color:#8b949e;padding:8px;background:#161b22;border-radius:6px;line-height:1.4;"></div>
        </div>
        <hr>
        <button class="btn btn-danger btn-sm" id="btn-delete-widget" onclick="if(state.selectedWidget) deleteWidget(state.selectedWidget.id)">🗑️ Delete Widget</button>
      </div>

      <!-- Mascot at bottom of sidebar -->
      <div class="sidebar-mascot">
        <img src="lobsterboard-mascot-clean.png" alt="LobsterBoard">
      </div>
    </aside>
  </div>

  <!-- Preview Modal -->
  <div class="modal" id="preview-modal">
    <div class="modal-content modal-fullscreen">
      <div class="modal-header">
        <h2>Preview</h2>
        <button class="modal-close" id="close-preview">&times;</button>
      </div>
      <div class="modal-body">
        <iframe id="preview-frame"></iframe>
      </div>
    </div>
  </div>

  <script src="js/widgets.js"></script>
  <script src="js/builder.js"></script>
  <script>
    // Load page links into nav
    fetch('/api/pages').then(r => r.json()).then(pages => {
      const nav = document.getElementById('header-nav');
      if (!nav || !pages.length) return;
      const sep = document.createElement('span');
      sep.className = 'page-separator';
      sep.style.cssText = 'width:1px;height:16px;background:#30363d;margin:0 4px';
      nav.insertBefore(sep, nav.firstChild);
      pages.reverse().forEach(p => {
        const a = document.createElement('a');
        a.href = '/pages/' + p.id;
        a.className = 'nav-link page-link';
        a.textContent = p.icon + ' ' + p.title;
        nav.insertBefore(a, nav.firstChild);
      });
    }).catch(() => {});

    // Theme Switcher System
    (function() {
      const THEME_KEY = 'lobsterboard-theme';
      const themeSelect = document.getElementById('theme-select');
      
      // Get saved theme from localStorage or dashboard config
      function getSavedTheme() {
        // First check localStorage
        const stored = localStorage.getItem(THEME_KEY);
        if (stored) return stored;
        
        // Fallback to dashboard config if available
        try {
          const dashConfig = localStorage.getItem('lobsterboard-dashboard');
          if (dashConfig) {
            const config = JSON.parse(dashConfig);
            if (config.theme) return config.theme;
          }
        } catch (e) {}
        
        return 'default';
      }
      
      // Apply theme to body
      function applyTheme(theme) {
        // Remove all theme classes
        document.body.classList.remove('theme-feminine', 'theme-feminine-dark', 'theme-terminal', 'theme-paper');
        
        // Apply new theme class if not default
        if (theme && theme !== 'default') {
          document.body.classList.add('theme-' + theme);
        }
      }
      
      // Save theme to localStorage and dashboard config
      function saveTheme(theme) {
        localStorage.setItem(THEME_KEY, theme);
        
        // Also update dashboard config for persistence
        try {
          const dashConfig = localStorage.getItem('lobsterboard-dashboard');
          if (dashConfig) {
            const config = JSON.parse(dashConfig);
            config.theme = theme;
            localStorage.setItem('lobsterboard-dashboard', JSON.stringify(config));
          }
        } catch (e) {}
      }
      
      // Initialize theme on page load
      const savedTheme = getSavedTheme();
      applyTheme(savedTheme);
      if (themeSelect) {
        themeSelect.value = savedTheme;
      }
      
      // Handle theme changes
      if (themeSelect) {
        themeSelect.addEventListener('change', function() {
          const theme = this.value;
          applyTheme(theme);
          saveTheme(theme);
        });
      }
      
      // Expose theme API globally for other scripts
      window.LobsterBoard = window.LobsterBoard || {};
      window.LobsterBoard.theme = {
        get: getSavedTheme,
        set: function(theme) {
          applyTheme(theme);
          saveTheme(theme);
          if (themeSelect) themeSelect.value = theme;
        },
        apply: applyTheme
      };
    })();
  </script>

  <!-- Template Gallery Modal -->
  <div id="template-gallery-modal" class="tpl-modal-overlay" style="display:none;">
    <div class="tpl-modal">
      <div class="tpl-modal-header">
        <h2>📋 Template Gallery</h2>
        <input type="text" id="tpl-search" placeholder="Search templates..." class="tpl-search">
        <button class="tpl-close-btn" id="tpl-close">&times;</button>
      </div>
      <div class="tpl-modal-body" id="tpl-grid">
        <div class="tpl-empty">No templates yet. Export your dashboard to create the first one!</div>
      </div>
      <!-- Detail view (hidden by default) -->
      <div class="tpl-detail" id="tpl-detail" style="display:none;">
        <button class="tpl-back-btn" id="tpl-back">← Back</button>
        <div class="tpl-detail-content">
          <img id="tpl-detail-img" class="tpl-detail-img" src="" alt="" style="cursor:zoom-in;" title="Click to enlarge">
          <div class="tpl-detail-info">
            <h2 id="tpl-detail-name"></h2>
            <p id="tpl-detail-desc"></p>
            <div id="tpl-detail-meta"></div>
            <div id="tpl-detail-tags"></div>
            <div class="tpl-detail-actions">
              <div style="position:relative;display:inline-block;">
                <button class="btn btn-primary" id="tpl-import-replace">Replace Current Dashboard</button>
                <div class="tpl-tooltip" style="display:none;position:absolute;bottom:calc(100% + 8px);left:50%;transform:translateX(-50%);background:#30363d;color:#e6edf3;padding:8px 12px;border-radius:6px;font-size:12px;width:220px;text-align:center;box-shadow:0 4px 12px rgba(0,0,0,0.4);z-index:10;pointer-events:none;">
                  Removes your entire current layout and replaces it with this template.
                  <div style="position:absolute;top:100%;left:50%;transform:translateX(-50%);border:6px solid transparent;border-top-color:#30363d;"></div>
                </div>
              </div>
              <div style="position:relative;display:inline-block;">
                <button class="btn btn-secondary" id="tpl-import-merge">Merge Into Current</button>
                <div class="tpl-tooltip" style="display:none;position:absolute;bottom:calc(100% + 8px);left:50%;transform:translateX(-50%);background:#30363d;color:#e6edf3;padding:8px 12px;border-radius:6px;font-size:12px;width:240px;text-align:center;box-shadow:0 4px 12px rgba(0,0,0,0.4);z-index:10;pointer-events:none;">
                  Adds this template's widgets below your existing dashboard. Your current widgets stay untouched.
                  <div style="position:absolute;top:100%;left:50%;transform:translateX(-50%);border:6px solid transparent;border-top-color:#30363d;"></div>
                </div>
              </div>
              <div style="position:relative;display:inline-block;">
                <button class="btn btn-danger" id="tpl-delete" style="background:#da3633;border-color:#da3633;">🗑️ Delete Template</button>
              </div>
            </div>
            <style>
              .tpl-detail-actions > div:hover .tpl-tooltip { display:block !important; }
            </style>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Screenshot Lightbox -->
  <div id="tpl-lightbox" style="display:none;position:fixed;inset:0;z-index:10000;background:rgba(0,0,0,0.85);cursor:default;justify-content:center;align-items:center;" onclick="this.style.display='none'">
    <div style="position:relative;display:inline-block;" onclick="event.stopPropagation()">
      <img id="tpl-lightbox-img" style="max-width:90vw;max-height:90vh;border-radius:8px;box-shadow:0 20px 60px rgba(0,0,0,0.5);">
      <button onclick="document.getElementById('tpl-lightbox').style.display='none'" style="position:absolute;top:-12px;right:-12px;background:#30363d;border:2px solid #555;color:#fff;font-size:18px;width:32px;height:32px;border-radius:50%;cursor:pointer;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,0.5);" onmouseover="this.style.background='#da3633'" onmouseout="this.style.background='#30363d'">&times;</button>
    </div>
  </div>

  <!-- Export Template Modal -->
  <div id="template-export-modal" class="tpl-modal-overlay" style="display:none;">
    <div class="tpl-modal tpl-modal-sm">
      <div class="tpl-modal-header">
        <h2>📦 Export as Template</h2>
        <button class="tpl-close-btn" id="tpl-export-close">&times;</button>
      </div>
      <div class="tpl-modal-body">
        <div class="tpl-form">
          <label>Name *</label>
          <input type="text" id="tpl-export-name" placeholder="My Dashboard Template" class="tpl-input">
          <label>Description</label>
          <textarea id="tpl-export-desc" placeholder="What this dashboard is for..." class="tpl-input" rows="3"></textarea>
          <label>Author</label>
          <input type="text" id="tpl-export-author" placeholder="your-name" class="tpl-input">
          <label>Tags (comma-separated)</label>
          <input type="text" id="tpl-export-tags" placeholder="monitoring, homelab, docker" class="tpl-input">
          <label>Screenshot</label>
          <input type="file" id="tpl-export-screenshot" accept="image/*" class="tpl-input" style="padding:6px;">
          <small style="color:#8b949e;display:block;margin-top:2px;">Optional — if left empty, a screenshot is captured automatically</small>
          <div id="tpl-widget-list" style="margin-top:12px;padding:8px;background:var(--bg-tertiary);border-radius:6px;font-size:12px;"></div>
          <button class="btn btn-primary" id="tpl-export-submit" style="margin-top:16px;width:100%;">Export Template</button>
          <div id="tpl-export-result" class="tpl-export-result" style="display:none;"></div>
        </div>
      </div>
    </div>
  </div>

  <!-- PIN Modal -->
  <div id="pin-modal" class="pin-modal-overlay" style="display:none;">
    <div class="pin-modal">
      <h3 id="pin-modal-title">🔒 Enter PIN</h3>
      <div id="pin-current-group" class="pin-group" style="display:none;">
        <label>Current PIN</label>
        <input type="password" id="pin-input-current" maxlength="6" placeholder="••••" inputmode="numeric" pattern="[0-9]*" class="pin-input">
      </div>
      <div class="pin-group">
        <label>PIN (4-6 digits)</label>
        <input type="password" id="pin-input" maxlength="6" placeholder="••••" inputmode="numeric" pattern="[0-9]*" class="pin-input">
      </div>
      <div id="pin-confirm-group" class="pin-group" style="display:none;">
        <label>Confirm PIN</label>
        <input type="password" id="pin-input-confirm" maxlength="6" placeholder="••••" inputmode="numeric" pattern="[0-9]*" class="pin-input">
      </div>
      <div id="pin-error" class="pin-error"></div>
      <div class="pin-actions">
        <button class="btn btn-primary" id="pin-submit">Submit</button>
        <button class="btn btn-secondary" id="pin-cancel">Cancel</button>
      </div>
    </div>
  </div>

  <!-- Security Settings Modal -->
  <div id="security-modal" class="pin-modal-overlay" style="display:none;">
    <div class="pin-modal" style="max-width:400px;">
      <h3>🔒 Security Settings</h3>
      <div class="security-option">
        <div class="security-option-header">
          <strong>Edit PIN</strong>
          <span id="pin-status" class="security-badge">Not Set</span>
        </div>
        <p style="color:#8b949e;font-size:12px;margin:4px 0 8px;">Require a PIN to enter edit mode</p>
        <div class="security-buttons">
          <button class="btn btn-secondary btn-sm" id="sec-set-pin">Set PIN</button>
          <button class="btn btn-secondary btn-sm" id="sec-change-pin" style="display:none;">Change PIN</button>
          <button class="btn btn-danger btn-sm" id="sec-remove-pin" style="display:none;">Remove PIN</button>
        </div>
      </div>
      <div class="security-option" style="margin-top:16px;">
        <div class="security-option-header">
          <strong>Public Mode</strong>
          <label class="toggle-switch">
            <input type="checkbox" id="public-mode-toggle">
            <span class="toggle-slider"></span>
          </label>
        </div>
        <p style="color:#8b949e;font-size:12px;margin:4px 0 0;">Hide edit button and block config APIs. Ideal for publicly-exposed dashboards.</p>
      </div>
      <div style="margin-top:20px;text-align:right;">
        <button class="btn btn-secondary" id="sec-close">Close</button>
      </div>
    </div>
  </div>

  <!-- Servers Settings Modal -->
  <div id="servers-modal" class="pin-modal-overlay" style="display:none;">
    <div class="pin-modal" style="max-width:500px;">
      <h3>🖥️ Remote Servers</h3>
      <p style="color:#8b949e;font-size:12px;margin:0 0 16px;">
        Connect to remote servers running <a href="https://www.npmjs.com/package/lobsterboard-agent" target="_blank" style="color:#58a6ff;">lobsterboard-agent</a>
      </p>
      <div id="servers-list" style="margin-bottom:16px;">
        <!-- Server list will be populated here -->
      </div>
      <div class="server-add-form" style="background:var(--bg-tertiary);padding:12px;border-radius:6px;">
        <h4 style="margin:0 0 12px;font-size:14px;">➕ Add Server</h4>
        <div style="display:flex;flex-direction:column;gap:8px;">
          <input type="text" id="server-name" placeholder="Server Name (e.g., Production VPS)" class="tpl-input" style="font-size:13px;">
          <input type="text" id="server-url" placeholder="URL (e.g., http://192.168.1.100:9090)" class="tpl-input" style="font-size:13px;">
          <input type="password" id="server-apikey" placeholder="API Key (from lobsterboard-agent show-key)" class="tpl-input" style="font-size:13px;">
          <div style="display:flex;gap:8px;margin-top:4px;">
            <button class="btn btn-primary btn-sm" id="server-add-btn">Add Server</button>
            <button class="btn btn-secondary btn-sm" id="server-test-btn">Test Connection</button>
          </div>
          <div id="server-add-result" style="font-size:12px;margin-top:4px;"></div>
        </div>
      </div>
      <div style="margin-top:16px;text-align:right;">
        <button class="btn btn-secondary" id="servers-close">Close</button>
      </div>
    </div>
  </div>

  <script src="js/templates.js"></script>
</body>
</html>
```

## File: `changelog.html`
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
            <span class="change-category">15+ screen size presets, custom dimensions, zoom controls (+/-, Fit, 1:1), keyboard shortcuts</span>
          </li>
          <li>
            <strong>Preview & Export</strong>
            <span class="change-category">Live preview modal with inlined styles, export to standalone ZIP (HTML/CSS/JS)</span>
          </li>
          <li>
            <strong>40+ Widgets</strong>
            <div class="widget-grid">
              <span class="widget-tag">🤖 Claude Usage</span>
              <span class="widget-tag">🤖 GPT Usage</span>
              <span class="widget-tag">🤖 Gemini Usage</span>
              <span class="widget-tag">🤖 AI Usage (All)</span>
              <span class="widget-tag">💰 Cost Tracker</span>
              <span class="widget-tag">🔄 API Status</span>
              <span class="widget-tag">🌡️ Local Weather</span>
              <span class="widget-tag">🌍 World Weather</span>
              <span class="widget-tag">🕐 Clock</span>
              <span class="widget-tag">🌍 World Clock</span>
              <span class="widget-tag">⏳ Countdown</span>
              <span class="widget-tag">📊 Stat Card</span>
              <span class="widget-tag">💻 CPU/Memory</span>
              <span class="widget-tag">💾 Disk Usage</span>
              <span class="widget-tag">🌐 Network Speed</span>
              <span class="widget-tag">🐳 Docker</span>
              <span class="widget-tag">📡 Uptime Monitor</span>
              <span class="widget-tag">✅ Todo List</span>
              <span class="widget-tag">📅 Calendar</span>
              <span class="widget-tag">📧 Email Count</span>
              <span class="widget-tag">🎯 Pomodoro</span>
              <span class="widget-tag">📈 Stock Ticker</span>
              <span class="widget-tag">₿ Crypto Price</span>
              <span class="widget-tag">🏠 Indoor Climate</span>
              <span class="widget-tag">📷 Camera Feed</span>
              <span class="widget-tag">🎵 Now Playing</span>
              <span class="widget-tag">💭 Quote of Day</span>
              <span class="widget-tag">🔗 Quick Links</span>
              <span class="widget-tag">📡 RSS Feed</span>
              <span class="widget-tag">📰 News Ticker</span>
              <span class="widget-tag">...and more</span>
            </div>
          </li>
          <li>
            <strong>Branding</strong>
            <span class="change-category">LobsterBoard name and mascot 🦞, logo wordmark, favicon, Apple touch icon</span>
          </li>
          <li>
            <strong>Dark Theme</strong>
            <span class="change-category">Consistent dash-card styling, matches OpenClaw aesthetic</span>
          </li>
        </ul>
      </section>
    </article>

    <!-- Upcoming -->
    <div class="upcoming">
      <h2>🚀 Upcoming</h2>
      <ul>
        <li>More themes (submit your own!)</li>
        <li>Widget templates and presets</li>
        <li>Dashboard sharing &amp; cloud sync</li>
        <li>Mobile-responsive layouts</li>
        <li>Plugin system for custom widgets</li>
      </ul>
    </div>
  </main>

  <footer>
    <p>LobsterBoard is open source. <a href="https://github.com/curbob/LobsterBoard">View on GitHub</a></p>
  </footer>

  <img src="lobsterboard-mascot-clean.png" alt="" class="mascot">
</body>
</html>
```

## File: `CHANGELOG.md`
```markdown
# Changelog

## [0.8.0] - 2026-03-24

### Added
- **Claude Usage widget** — Real-time Claude Code subscription monitoring with 5-hour session, 7-day weekly, Opus/Sonnet limits, and extra usage tracking — thanks @JamesTsetsekas!
- **Claude Usage standalone page** — Full-page dashboard for detailed usage analysis at `/pages/claude-usage/`

### Fixed
- **OpenClaw version detection** — Widget now correctly parses `openclaw --version` output to fix false "Update available" notifications — thanks @JamesTsetsekas!

### Technical
- Auto-refreshes expired Claude OAuth tokens via CLI
- Reads from standard `~/.claude/.credentials.json` location
- Comprehensive error handling for rate limits and authentication issues

## [0.7.0] - 2026-03-17

### Added
- **Enhanced Gemini CLI integration** — auto-detect all available Gemini CLI quota buckets (including new 3.x models) instead of hardcoded 2.x allowlist — thanks @mastash3ff!
- **Auto-refresh OAuth tokens** — Gemini CLI tokens now automatically refresh to survive multi-machine rotation, preventing authentication failures — thanks @mastash3ff!

### Changed
- **Future-proof model support** — Gemini CLI collector now automatically surfaces new quota windows when Google adds them

## [0.3.1] - 2026-02-28

### Fixed
- **Edit mode header clutter** — page navigation links now hide when entering edit mode to reduce header crowding

## [0.3.0] - 2026-02-28

### Added
- **Theme switcher** — 5 themes: Default (dark), Feminine (pastel pink/lavender), Feminine Dark, Terminal (green CRT), Paper (cream/sepia)
- **Phosphor icon system** — themed widgets use Phosphor icons; Default theme keeps emoji
- **Theme selector dropdown** in edit mode header
- Theme persists to localStorage and dashboard config
- **Themes showcase** on website and README with lightbox gallery

## [0.2.6] - 2026-02-23

### Fixed
- **Version suffix comparison** — versions like `2026.2.22-2` (npm post-release patches) now correctly match GitHub tags like `v2026.2.22`, fixing false "Update available" indicators — thanks @JamesTsetsekas!

## [0.2.5] - 2026-02-19

### Fixed
- **iCal timezone parsing** — calendar events now display at correct times regardless of timezone (TZID parameter support) — thanks @jlgrimes!

### Added
- **Clickable URLs in calendar** — Zoom/Teams links in event summaries and locations are now hyperlinks — thanks @jlgrimes!

## [0.2.4] - 2026-02-17

### Fixed
- SSRF vulnerability in RSS feed proxy (thanks @jlgrimes for the security report!)

## [0.2.3] - 2026-02-16

### Added
- **PIN-locked edit mode** — set a 4-6 digit PIN to prevent unauthorized editing (SHA-256 hashed, server-side only)
- **Server-side secrets store** — API keys, calendar URLs, and tokens stored in `secrets.json`, never sent to browser
- **Public Mode** — hides edit button and blocks config APIs; subtle 🔒 unlock button for admin access
- **Privacy warnings** on sensitive widgets (System Log, Activity List, Cron Jobs, Calendar, Todo List) — ⚠️ badge in widget panel + orange warning in properties panel
- **Community Widgets** — contribution guide, templates, and PR checklist for community widget submissions

### Fixed
- Private calendar URLs (Google Calendar, iCloud CalDAV) no longer leak in template exports
- Template export `stripSensitive()` now detects URLs with auth tokens
- Public mode toggle uses masked PIN modal instead of plain-text `prompt()`
- `closePinModal()` no longer kills pending callbacks

### Security
- `auth.json` and `secrets.json` added to `.gitignore`
- Pre-commit hook blocks private data patterns in template files

## [0.2.2] - 2026-02-16

### Fixed
- Removed private Google Calendar URL accidentally included in template config
- Fixed `stripSensitive()` to detect and blank URLs with embedded auth tokens

## [0.2.1] - 2026-02-15

### Fixed
- Minor bug fixes and stability improvements

## [0.2.0] - 2026-02-15

### Added
- **Template Gallery** — export, import, and share dashboard layouts with auto-screenshot previews
  - `js/templates.js` — new template gallery UI and export system
  - Templates API: list, get, preview, import (merge/replace), export, delete
  - `templates/` directory with bundled starter templates
  - Template modal with search, preview lightbox, and import options
- **Notes widget** — persistent rich-text notes with auto-save via `/api/notes`
- **Browse button** for directory selection in image widgets (Image, Random Image, Latest Image)
- **GitHub Stats widget rework** — profile contributions, stars, and activity with property bindings
- **LobsterBoard Release widget** — version update checker via `/api/lb-release`
- **SSE streaming** for system stats (`/api/stats/stream`)
- **Browse directories API** (`/api/browse-dirs`) for server-side directory picker
- Sidebar reorder, verified checkmarks, delete button, tooltips in editor
- html2canvas-based dashboard screenshot export
- Scrollable canvas mode

### Changed
- Stock Ticker widget — fixed `hasApiKey` check
- Builder — contenteditable keyboard fix, null-checks throughout
- License changed from MIT to BSL-1.1
- Widget count: 47 → 50

### Removed
- GPT Usage widget (standalone) — use AI Cost Tracker or Claude Usage instead

## [0.1.6] - 2025-02-14

- Initial public npm release
- 47 widgets, drag-and-drop editor, custom pages system
- SSRF protection for proxy endpoints
```

## File: `CNAME`
```
lobsterboard.com
```

## File: `config.example.json`
```json
{
  "canvas": {
    "width": 1920,
    "height": 1080
  },
  "fontScale": 1.25,
  "widgets": [
    {
      "id": "widget-1",
      "type": "weather",
      "x": 600,
      "y": 120,
      "width": 200,
      "height": 140,
      "properties": {
        "title": "Local Weather",
        "location": "Atlanta",
        "units": "F",
        "refreshInterval": 600,
        "showHeader": true
      }
    },
    {
      "id": "widget-2",
      "type": "weather-multi",
      "x": 600,
      "y": 280,
      "width": 340,
      "height": 220,
      "properties": {
        "title": "World Weather",
        "locations": "New York; London; Tokyo",
        "units": "F",
        "refreshInterval": 600
      }
    },
    {
      "id": "widget-3",
      "type": "clock",
      "x": 20,
      "y": 120,
      "width": 200,
      "height": 140,
      "properties": {
        "title": "Clock",
        "timezone": "local",
        "format24h": false
      }
    },
    {
      "id": "widget-4",
      "type": "world-clock",
      "x": 240,
      "y": 120,
      "width": 340,
      "height": 200,
      "properties": {
        "title": "World Clock",
        "locations": "New York; London; Tokyo",
        "format24h": false,
        "refreshInterval": 60
      }
    },
    {
      "id": "widget-5",
      "type": "countdown",
      "x": 240,
      "y": 340,
      "width": 340,
      "height": 160,
      "properties": {
        "title": "Countdown",
        "targetDate": "2026-02-27",
        "showHours": true,
        "showMinutes": true
      }
    },
    {
      "id": "widget-6",
      "type": "cpu-memory",
      "x": 20,
      "y": 280,
      "width": 200,
      "height": 160,
      "properties": {
        "title": "System",
        "endpoint": "/api/system",
        "refreshInterval": 5
      }
    },
    {
      "id": "widget-7",
      "type": "disk-usage",
      "x": 20,
      "y": 460,
      "width": 200,
      "height": 120,
      "properties": {
        "title": "Disk",
        "path": "/",
        "endpoint": "/api/disk",
        "refreshInterval": 60
      }
    },
    {
      "id": "widget-8",
      "type": "network-speed",
      "x": 20,
      "y": 600,
      "width": 200,
      "height": 140,
      "properties": {
        "title": "Network",
        "endpoint": "/api/network",
        "refreshInterval": 2
      }
    },
    {
      "id": "widget-9",
      "type": "docker-containers",
      "x": 600,
      "y": 520,
      "width": 340,
      "height": 200,
      "properties": {
        "title": "Containers",
        "endpoint": "/api/docker",
        "refreshInterval": 10
      }
    },
    {
      "id": "widget-10",
      "type": "uptime-monitor",
      "x": 240,
      "y": 520,
      "width": 340,
      "height": 200,
      "properties": {
        "title": "Uptime",
        "services": "Website,API,Database",
        "refreshInterval": 30
      }
    },
    {
      "id": "widget-12",
      "type": "text-header",
      "x": 20,
      "y": 20,
      "width": 400,
      "height": 50,
      "properties": {
        "title": "Lobster Board",
        "showHeader": false,
        "fontSize": 24,
        "fontColor": "#e6edf3",
        "textAlign": "left",
        "fontWeight": "bold"
      }
    },
    {
      "id": "widget-13",
      "type": "horizontal-line",
      "x": 20,
      "y": 40,
      "width": 1880,
      "height": 60,
      "properties": {
        "title": "",
        "showHeader": false,
        "lineColor": "#30363d",
        "lineThickness": 2
      }
    },
    {
      "id": "widget-14",
      "type": "text-header",
      "x": 20,
      "y": 20,
      "width": 400,
      "height": 50,
      "properties": {
        "title": "Lobster Board",
        "showHeader": false,
        "fontSize": 24,
        "fontColor": "#e6edf3",
        "textAlign": "left",
        "fontWeight": "bold"
      }
    },
    {
      "id": "widget-15",
      "type": "horizontal-line",
      "x": 20,
      "y": 40,
      "width": 1880,
      "height": 60,
      "properties": {
        "title": "",
        "showHeader": false,
        "lineColor": "#30363d",
        "lineThickness": 2
      }
    },
    {
      "id": "widget-16",
      "type": "text-header",
      "x": 20,
      "y": 20,
      "width": 400,
      "height": 50,
      "properties": {
        "title": "Lobster Board",
        "showHeader": false,
        "showBorder": false,
        "fontSize": 24,
        "fontColor": "#e6edf3",
        "textAlign": "left",
        "fontWeight": "bold"
      }
    },
    {
      "id": "widget-18",
      "type": "horizontal-line",
      "x": 20,
      "y": 40,
      "width": 1860,
      "height": 60,
      "properties": {
        "title": "",
        "showHeader": false,
        "lineColor": "#30363d",
        "lineThickness": 2
      }
    },
    {
      "id": "widget-22",
      "type": "auth-status",
      "x": 1080,
      "y": 100,
      "width": 240,
      "height": 140,
      "properties": {
        "title": "Auth Type",
        "endpoint": "/api/status",
        "refreshInterval": 30,
        "showHeader": true
      }
    },
    {
      "id": "widget-23",
      "type": "openclaw-release",
      "x": 1340,
      "y": 100,
      "width": 240,
      "height": 140,
      "properties": {
        "title": "OpenClaw Release",
        "openclawUrl": "",
        "refreshInterval": 3600,
        "showHeader": true,
        "widgetFontScale": 1.25
      }
    },
    {
      "id": "widget-24",
      "type": "release",
      "x": 1600,
      "y": 100,
      "width": 260,
      "height": 140,
      "properties": {
        "title": "Code Pilot Release",
        "repo": "op7418/CodePilot",
        "currentVersion": ".0.6",
        "refreshInterval": 3600,
        "showHeader": true
      }
    },
    {
      "id": "widget-30",
      "type": "rss-ticker",
      "x": 0,
      "y": 1040,
      "width": 1920,
      "height": 40,
      "properties": {
        "title": "RSS",
        "feedUrl": "https://magazine.sebastianraschka.com/feed",
        "maxItems": 10,
        "refreshInterval": 600
      }
    },
    {
      "id": "widget-31",
      "type": "todo-list",
      "x": 1080,
      "y": 260,
      "width": 350,
      "height": 300,
      "properties": {
        "title": "Todo",
        "items": "Finish LobsterBoard, Check all the widgets, see the world"
      }
    },
    {
      "id": "widget-32",
      "type": "calendar",
      "x": 1460,
      "y": 260,
      "width": 400,
      "height": 300,
      "properties": {
        "title": "Calendar",
        "calendarId": "primary",
        "maxEvents": 5,
        "refreshInterval": 300
      }
    },
    {
      "id": "widget-33",
      "type": "quick-links",
      "x": 1080,
      "y": 580,
      "width": 360,
      "height": 140,
      "properties": {
        "title": "Quick Links",
        "columns": 2,
        "links": [
          {
            "name": "reddit",
            "url": "https://reddit.com"
          },
          {
            "name": "OpenClaw",
            "url": "https://openclaw.ai/"
          }
        ]
      }
    },
    {
      "id": "widget-34",
      "type": "quick-links",
      "x": 1460,
      "y": 580,
      "width": 400,
      "height": 140,
      "properties": {
        "title": "Quick Links",
        "columns": 1,
        "links": [
          {
            "name": "LobsterBoard",
            "url": "https://github.com/Curbob/LobsterBoard"
          }
        ]
      }
    },
    {
      "id": "widget-35",
      "type": "ai-usage-claude",
      "x": 40,
      "y": 780,
      "width": 320,
      "height": 220,
      "properties": {
        "title": "Claude",
        "refreshInterval": 300,
        "apiKey": ""
      }
    },
    {
      "id": "widget-37",
      "type": "pages-menu",
      "x": 260,
      "y": 0,
      "width": 660,
      "height": 100,
      "properties": {
        "title": "Pages",
        "layout": "horizontal",
        "refreshInterval": 60,
        "showHeader": false,
        "showBorder": false
      }
    }
  ]
}
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing to LobsterBoard

Thanks for your interest in contributing! This guide covers everything you need to create and submit a community widget.

## Getting Started

1. **Fork** the repo on GitHub and clone locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/LobsterBoard.git
   cd LobsterBoard
   npm install
   ```

2. **Run the dev server:**
   ```bash
   node server.cjs
   ```
   Open http://localhost:8080 — press **Ctrl+E** to enter edit mode.

3. **Explore the widget format:** Open `js/widgets.js` to see how all 50+ built-in widgets are defined. Each widget is an object in the `WIDGETS` map with a consistent structure.

---

## Widget Development Guide

### Step 1: Copy the Template

```bash
cp -r community-widgets/_template community-widgets/my-widget-name
```

### Step 2: Understand the Widget Object

Every widget is a plain JavaScript object with these fields:

```js
{
  name: 'My Widget',            // Display name in the widget picker
  icon: '🎯',                   // Emoji icon
  category: 'small',            // 'small' | 'large' | 'bar'
  description: 'What it does.', // Shown in the picker tooltip
  defaultWidth: 200,            // Default width in pixels
  defaultHeight: 120,           // Default height in pixels
  hasApiKey: false,              // true if an API key is needed
  properties: { ... },          // User-configurable settings
  preview: `<div>...</div>`,    // Static HTML for the picker thumbnail
  generateHtml: (props) => `...`, // Returns the widget's HTML
  generateJs: (props) => `...`,   // Returns the widget's runtime JS
}
```

### Categories

| Category | Use For | Typical Size |
|----------|---------|-------------|
| `small` | KPI cards, single values, gauges | 180–250 × 100–150 |
| `large` | Lists, logs, tables, multi-row content | 300–500 × 200–400 |
| `bar` | Full-width status bars, tickers | 800+ × 60–100 |

### Properties

Properties appear as editable fields in the right-hand panel. Types are inferred from the default value:

```js
properties: {
  title: 'My Widget',       // string → text input
  count: 10,                // number → number input
  refreshInterval: 60,      // seconds between auto-refreshes
  API_KEY='[REDACTED_API_KEY]',
}
```

### `generateHtml(props)`

Returns an HTML string. This is the widget's visual structure.

**Rules:**
- Prefix ALL element IDs with `props.id` — users can add multiple instances of the same widget, so IDs must be unique.
- Use the built-in CSS classes: `dash-card`, `dash-card-head`, `dash-card-title`, `dash-card-body`, `kpi-value`, `kpi-label`.
- Use CSS variables for theming (see [Theme Variables](#theme-variables) below).

```js
generateHtml: (props) => `
  <div class="dash-card" id="widget-${props.id}" style="height:100%;">
    <div class="dash-card-head">
      <span class="dash-card-title">🎯 ${props.title || 'My Widget'}</span>
    </div>
    <div class="dash-card-body" style="display:flex;align-items:center;justify-content:center;">
      <div class="kpi-value blue" id="${props.id}-value">—</div>
    </div>
  </div>`
```

### `generateJs(props)`

Returns a JavaScript string that runs in the browser via `new Function()`. This is where you fetch data, update the DOM, and set up refresh intervals.

**Rules:**
- Use unique function names: `update_${props.id.replace(/-/g, '_')}()`
- Reference elements by the IDs from `generateHtml`
- Handle errors gracefully — show `"—"` or `"Error"`, never let it crash
- Set up auto-refresh with `setInterval`

```js
generateJs: (props) => `
  async function update_${props.id.replace(/-/g, '_')}() {
    const el = document.getElementById('${props.id}-value');
    try {
      const res = await fetch('https://api.example.com/data?key=${props.apiKey}');
      if (!res.ok) throw new Error('HTTP ' + res.status);
      const data = await res.json();
      el.textContent = data.value;
    } catch (e) {
      console.error('Widget error:', e);
      if (el) el.textContent = '—';
    }
  }
  update_${props.id.replace(/-/g, '_')}();
  setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 60) * 1000});
`
```

### Refresh Intervals

The `refreshInterval` property (in seconds) controls how often the widget re-fetches data. Convert to milliseconds when calling `setInterval`:

```js
setInterval(myFunction, ${(props.refreshInterval || 60) * 1000});
```

Reasonable defaults: weather → 600s, stocks → 30s, system stats → 5s.

### Theme Variables

LobsterBoard uses a dark theme. Use these CSS variables so your widget fits in:

| Variable | Usage |
|----------|-------|
| `--bg-primary` | Main background |
| `--bg-secondary` | Card/panel background |
| `--bg-tertiary` | Hover/active states |
| `--text-primary` | Primary text color |
| `--text-secondary` | Muted/label text |
| `--border-color` | Borders and dividers |
| `--accent-blue` | Primary accent |
| `--accent-green` | Success/positive |
| `--accent-red` | Error/negative |
| `--accent-yellow` | Warning |
| `--accent-purple` | Purple accent |

---

## Best Practices

1. **Always use `props.id` prefix** for element IDs — multiple instances must coexist.
2. **Escape user content** to prevent XSS. Never use `innerHTML` with raw user strings.
3. **Handle fetch failures gracefully** — show `"—"` or an error state, don't leave "Loading..." forever.
4. **Keep widgets self-contained** — no external CSS frameworks, no heavy libraries.
5. **Use CSS variables** from the theme so your widget matches the dark theme.
6. **Test with multiple instances** of the same widget on the canvas.
7. **Keep it lightweight** — no large dependencies or bundled libraries.
8. **Support the dark theme** — it's the only theme. Don't hardcode white backgrounds.

---

## Security Rules

These are strictly enforced during review:

- ❌ **NEVER** include real API keys, tokens, or private URLs
- ✅ Use `YOUR_API_KEY_HERE` as the placeholder value
- ❌ **NEVER** fetch from private/local IPs (`10.x`, `192.168.x`, `localhost`, `127.0.0.1`)
- ❌ **No** `eval()`, `new Function()` on user input, or dynamic script injection
- ✅ Sanitize any user-provided content before inserting into the DOM
- ✅ Use `textContent` instead of `innerHTML` when displaying user data

---

## Submission Process

1. **Copy the template:**
   ```bash
   cp -r community-widgets/_template community-widgets/your-widget-name
   ```

2. **Build your widget** — edit `widget.js` with your widget object.

3. **Add documentation** — update the `README.md` with a screenshot, description, and property table.

4. **Test locally** — add your widget to `js/widgets.js` temporarily, run the server, and verify:
   - Widget renders correctly
   - Data fetches work (or gracefully fail)
   - Multiple instances work side-by-side
   - No console errors

5. **Submit a PR** with the title format: `[Widget] Widget Name`

6. **Maintainer review** — we check for security, code quality, and functionality.

7. **Merge** — once approved, your widget gets included in the next release! 🎉

### PR Checklist

Your PR will be reviewed against this checklist:

- [ ] No hardcoded API keys, tokens, or private URLs
- [ ] Tested locally with `node server.cjs`
- [ ] README.md included with description and property table
- [ ] Preview image/screenshot included
- [ ] Follows naming conventions (`community-widgets/kebab-case-name/`)
- [ ] Works with multiple instances on the same canvas
- [ ] Uses `props.id` prefix for all element IDs
- [ ] Handles errors gracefully (no unhandled exceptions)
- [ ] No external CSS frameworks or heavy dependencies
- [ ] Uses theme CSS variables (not hardcoded colors)

---

## Questions?

Open an issue on GitHub or start a discussion. We're happy to help!
```

## File: `CONTRIBUTORS.md`
```markdown
# Contributors

Thank you to everyone who has contributed to LobsterBoard! 🦞

## Code Contributors

- **[@dougjerum](https://github.com/dougjerum)** — Server improvements and configuration ([PR #4](https://github.com/Curbob/LobsterBoard/pull/4))
- **[@mastash3ff](https://github.com/mastash3ff)** — Gemini CLI improvements: auto-detect quota buckets & OAuth token refresh ([PR #16](https://github.com/Curbob/LobsterBoard/pull/16), [PR #17](https://github.com/Curbob/LobsterBoard/pull/17))
- **[@JamesTsetsekas](https://github.com/JamesTsetsekas)** — Claude Usage widget & OpenClaw version parsing fix ([PR #18](https://github.com/Curbob/LobsterBoard/pull/18), [PR #19](https://github.com/Curbob/LobsterBoard/pull/19))

## Design Contributors

- **[@Supadoopa](https://github.com/Supadoopa)** — Feminine theme color palettes and design inspiration ([PR #7](https://github.com/Curbob/LobsterBoard/pull/7))

---

Want to contribute? Check out our [GitHub Issues](https://github.com/Curbob/LobsterBoard/issues) or submit a PR!
```

## File: `export-server.js`
```javascript
/**
 * LobsterBoard Dashboard Server
 * 
 * A minimal server that:
 * - Serves your dashboard static files
 * - Proxies allowed OpenClaw API endpoints
 * 
 * Usage: node server.js
 * 
 * Environment variables:
 *   PORT          - Server port (default: 8080)
 *   HOST          - Bind address (default: 127.0.0.1 for security)
 *   OPENCLAW_URL  - OpenClaw gateway URL (default: http://localhost:18789)
 * 
 * Security: By default binds to localhost only. To expose on network:
 *   HOST=0.0.0.0 node server.js
 *   ⚠️  Only do this on trusted networks!
 */

const http = require('http');
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

// ─────────────────────────────────────────────
// CONFIGURATION
// ─────────────────────────────────────────────

const PORT = process.env.PORT || 8080;
const HOST = process.env.HOST || '127.0.0.1';
const OPENCLAW_URL = (process.env.OPENCLAW_URL || 'http://localhost:18789').replace(/\/$/, '');

// Restrict CORS to the dashboard's own origin (no wildcard)
const ALLOWED_ORIGIN = `http://${HOST}:${PORT}`;

// Allowed API endpoints (whitelist for security)
const ALLOWED_API_PATHS = [
  '/api/status',
  '/api/health',
  '/api/activity',
  '/api/cron',
  '/api/logs',
  '/api/sessions',
  '/api/usage/tokens'
];

// MIME types for static files
const MIME_TYPES = {
  '.html': 'text/html',
  '.css': 'text/css',
  '.js': 'application/javascript',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon'
};

// ─────────────────────────────────────────────
// LOGGING
// ─────────────────────────────────────────────

const LOG_FILE = path.join(__dirname, 'export-server.log');

function log(level, message, data = null) {
  const entry = `[${new Date().toISOString()}] [${level}] ${message}${data ? ' ' + JSON.stringify(data) : ''}\n`;
  console.log(entry.trim());
  try {
    fs.appendFileSync(LOG_FILE, entry);
  } catch (e) {
    // If we can't write to log file, just continue
  }
}

// Generate request ID for tracing
function generateRequestId() {
  return crypto.randomBytes(4).toString('hex');
}

// ─────────────────────────────────────────────
// RESPONSE HELPERS
// ─────────────────────────────────────────────

function sendError(res, message, statusCode = 500, requestId = null) {
  res.writeHead(statusCode, { 
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': ALLOWED_ORIGIN,
    ...(requestId && { 'X-Request-Id': requestId })
  });
  res.end(JSON.stringify({ status: 'error', message }));
}

// ─────────────────────────────────────────────
// PROXY
// ─────────────────────────────────────────────

async function proxyToOpenClaw(reqPath, res, requestId) {
  const url = OPENCLAW_URL + reqPath;
  const startTime = Date.now();
  
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 10000);
  
  try {
    const response = await fetch(url, { signal: controller.signal });
    clearTimeout(timeout);
    const data = await response.text();
    
    log('INFO', `PROXY ${reqPath}`, { 
      requestId, 
      targetUrl: url,
      status: response.status,
      responseTime: Date.now() - startTime 
    });
    
    res.writeHead(response.status, {
      'Content-Type': response.headers.get('content-type') || 'application/json',
      'Access-Control-Allow-Origin': ALLOWED_ORIGIN,
      'X-Request-Id': requestId
    });
    res.end(data);
  } catch (error) {
    clearTimeout(timeout);
    
    // Log detailed error server-side
    log('ERROR', `Proxy failed: ${reqPath}`, { 
      requestId, 
      targetUrl: url, 
      error: error.message,
      responseTime: Date.now() - startTime
    });
    
    // Return generic message to client (don't leak internal details)
    sendError(res, 'Failed to reach backend service', 502, requestId);
  }
}

// ─────────────────────────────────────────────
// STATIC FILES
// ─────────────────────────────────────────────

function serveStatic(filePath, res, requestId) {
  // Default to index.html
  if (filePath === '/') filePath = '/index.html';
  
  const fullPath = path.resolve(__dirname, '.' + filePath);
  
  // Prevent path traversal attacks
  if (!fullPath.startsWith(path.resolve(__dirname))) {
    log('WARN', 'Path traversal attempt blocked', { requestId, path: filePath });
    sendError(res, 'Forbidden', 403, requestId);
    return;
  }
  
  const ext = path.extname(fullPath).toLowerCase();
  const contentType = MIME_TYPES[ext] || 'application/octet-stream';
  
  fs.readFile(fullPath, (err, data) => {
    if (err) {
      if (err.code === 'ENOENT') {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('Not Found');
      } else {
        log('ERROR', 'Static file read error', { requestId, path: filePath, error: err.message });
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end('Server Error');
      }
      return;
    }
    
    res.writeHead(200, { 'Content-Type': contentType });
    res.end(data);
  });
}

// ─────────────────────────────────────────────
// SERVER
// ─────────────────────────────────────────────

const server = http.createServer(async (req, res) => {
  const requestId = generateRequestId();
  const url = new URL(req.url, `http://${req.headers.host}`);
  const pathname = url.pathname;
  
  // Handle CORS preflight
  if (req.method === 'OPTIONS') {
    res.writeHead(204, {
      'Access-Control-Allow-Origin': ALLOWED_ORIGIN,
      'Access-Control-Allow-Methods': 'GET, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
      'X-Request-Id': requestId
    });
    res.end();
    return;
  }
  
  try {
    // Check if this is an allowed API proxy request
    if (pathname.startsWith('/api/')) {
      if (ALLOWED_API_PATHS.includes(pathname)) {
        await proxyToOpenClaw(pathname, res, requestId);
      } else {
        log('WARN', 'Blocked API path', { requestId, path: pathname });
        sendError(res, 'API endpoint not allowed', 403, requestId);
      }
      return;
    }
    
    // Serve static files
    serveStatic(pathname, res, requestId);
  } catch (e) {
    log('ERROR', 'Request handler error', { requestId, path: pathname, error: e.message, stack: e.stack });
    sendError(res, 'Internal server error', 500, requestId);
  }
});

// Handle server errors
server.on('error', (err) => {
  log('ERROR', 'Server error', { error: err.message, stack: err.stack });
});

// Graceful shutdown
process.on('SIGTERM', () => {
  log('INFO', 'Received SIGTERM, shutting down...');
  server.close(() => {
    log('INFO', 'Server closed');
    process.exit(0);
  });
});

process.on('SIGINT', () => {
  log('INFO', 'Received SIGINT, shutting down...');
  server.close(() => {
    log('INFO', 'Server closed');
    process.exit(0);
  });
});

// Start server
server.listen(PORT, HOST, () => {
  log('INFO', 'Server started', { host: HOST, port: PORT, openclawUrl: OPENCLAW_URL });
  console.log(`
🦞 LobsterBoard Dashboard Server

   Local:   http://${HOST}:${PORT}
   OpenClaw: ${OPENCLAW_URL}
   
   Proxied endpoints: ${ALLOWED_API_PATHS.join(', ')}
   
${HOST === '127.0.0.1' ? '   ✓ Bound to localhost (secure)\n' : '   ⚠️  Exposed to network - use on trusted networks only!\n'}
   Press Ctrl+C to stop
`);
});
```

## File: `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LobsterBoard — Self-Hosted Dashboard Builder</title>
  <meta name="description" content="A self-hosted, drag-and-drop dashboard builder with live system monitoring, dark theme, and 45 widgets. No cloud dependencies.">
  <link rel="icon" type="image/png" href="site-assets/favicon.png">
  <link rel="apple-touch-icon" href="site-assets/apple-touch-icon.png">
  <link rel="stylesheet" href="site-style.css">
</head>
<body>
  <!-- Nav -->
  <nav class="nav">
    <div class="nav-inner">
      <a href="#" class="nav-logo">
        <img src="site-assets/lobsterboard-logo-final.png" alt="LobsterBoard" height="44">
      </a>
      <div class="nav-links">
        <a href="#features">Features</a>
        <a href="#themes">Themes</a>
        <a href="#widgets">Widgets</a>
        <a href="#quickstart">Quick Start</a>
        <a href="https://github.com/curbob/LobsterBoard" target="_blank" class="btn btn-sm">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
          GitHub
        </a>
      </div>
      <button class="nav-toggle" aria-label="Menu" onclick="document.querySelector('.nav-links').classList.toggle('open')">☰</button>
    </div>
  </nav>

  <!-- Hero -->
  <section class="hero">
    <div class="hero-bg"></div>
    <div class="container hero-content">
      <img src="site-assets/lobsterboard-logo-hero.png" alt="LobsterBoard Logo" class="hero-logo fade-in">
      <h1 class="fade-in d1">Your Dashboard. Your Server. Your Rules.</h1>
      <p class="hero-sub fade-in d2">A self-hosted, drag-and-drop dashboard builder with live system monitoring, dark theme, and <strong>45 widgets</strong>. No cloud. No accounts. No nonsense.</p>
      <div class="hero-actions fade-in d3">
        <a href="#quickstart" class="btn btn-primary btn-lg">Get Started</a>
        <a href="https://github.com/curbob/LobsterBoard" target="_blank" class="btn btn-outline btn-lg">View on GitHub</a>
      </div>
      <div class="hero-badges fade-in d4">
        <img src="https://img.shields.io/npm/v/lobsterboard?style=flat-square&color=e74c3c&label=npm" alt="npm version">
        <img src="https://img.shields.io/github/license/curbob/LobsterBoard?style=flat-square&color=555" alt="MIT License">
        <img src="https://img.shields.io/badge/widgets-45-e74c3c?style=flat-square" alt="45 Widgets">
        <img src="https://img.shields.io/badge/node-%E2%89%A516-333?style=flat-square&logo=node.js" alt="Node 16+">
      </div>
    </div>
  </section>

  <!-- Features -->
  <section id="features" class="section">
    <div class="container">
      <h2 class="section-title">Why LobsterBoard?</h2>
      <p class="section-sub">Everything you need to build a personal command center — nothing you don't.</p>
      <div class="features-grid">
        <div class="feature-card">
          <div class="feature-icon">🎨</div>
          <h3>Drag & Drop Builder</h3>
          <p>Visual editor with snap grid, resize handles, and a widget sidebar. Press Ctrl+E and start building.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">📡</div>
          <h3>Live System Monitoring</h3>
          <p>CPU, memory, disk, network, and Docker stats stream in real-time via Server-Sent Events.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">🔒</div>
          <h3>Fully Self-Hosted</h3>
          <p>Single Node.js server. No cloud accounts, no telemetry, no external dependencies. Your data stays home.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">⚡</div>
          <h3>Zero Build Step</h3>
          <p>Vanilla JS, vanilla CSS. No React, no Webpack, no transpilation. Clone, install, run. That's it.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">🌙</div>
          <h3>Dark Theme Native</h3>
          <p>Built dark from the ground up with CSS custom properties. Easy on the eyes, beautiful on any screen.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">📦</div>
          <h3>50+ Widgets</h3>
          <p>System stats, weather, stocks, crypto, calendars, todos, cameras, Docker, AI usage, and much more.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">📑</div>
          <h3>Custom Pages</h3>
          <p>Built-in pages system for notes, calendars, boards, and more. Each page has its own API and storage — extend your dashboard beyond widgets.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">🔐</div>
          <h3>PIN & Public Mode</h3>
          <p>Lock editing with a PIN, store API keys server-side, and toggle Public Mode to safely share your dashboard with visitors.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">👥</div>
          <h3>Community Widgets</h3>
          <p>Build and share your own widgets. Copy the template, follow the <a href="https://github.com/curbob/LobsterBoard/blob/main/CONTRIBUTING.md" style="color:var(--accent);">contribution guide</a>, and submit a PR.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Themes -->
  <section id="themes" class="section section-dark">
    <div class="container">
      <h2 class="section-title">5 Built-in Themes</h2>
      <p class="section-sub">Switch themes from the dropdown in edit mode. Your choice persists across sessions.</p>
      <div class="themes-grid">
        <div class="theme-card" onclick="openLightbox(this)">
          <img src="site-assets/themes/theme-default.png" alt="Default Theme" loading="lazy">
          <h4>🌙 Default</h4>
          <p>Dark theme with emoji icons — the classic look</p>
        </div>
        <div class="theme-card" onclick="openLightbox(this)">
          <img src="site-assets/themes/theme-terminal.png" alt="Terminal Theme" loading="lazy">
          <h4>💻 Terminal</h4>
          <p>Green CRT aesthetic with scanlines and Phosphor icons</p>
        </div>
        <div class="theme-card" onclick="openLightbox(this)">
          <img src="site-assets/themes/theme-paper.png" alt="Paper Theme" loading="lazy">
          <h4>📜 Paper</h4>
          <p>Warm cream/sepia tones with a vintage feel</p>
        </div>
        <div class="theme-card" onclick="openLightbox(this)">
          <img src="site-assets/themes/theme-feminine.png" alt="Feminine Theme" loading="lazy">
          <h4>🌸 Feminine</h4>
          <p>Soft pink and lavender pastels with subtle glows</p>
        </div>
        <div class="theme-card" onclick="openLightbox(this)">
          <img src="site-assets/themes/theme-feminine-dark.png" alt="Feminine Dark Theme" loading="lazy">
          <h4>💜 Feminine Dark</h4>
          <p>Pink and purple accents on a dark background</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Lightbox -->
  <div id="lightbox" class="lightbox" onclick="closeLightbox()">
    <span class="lightbox-close">&times;</span>
    <img id="lightbox-img" src="" alt="">
  </div>

  <!-- Screenshot -->
  <section id="screenshot" class="section">
    <div class="container">
      <h2 class="section-title">See It In Action</h2>
      <p class="section-sub">A real dashboard built with LobsterBoard. Drag, drop, save, done.</p>
      <div class="screenshot-wrap">
        <img src="site-assets/screenshot.jpg" alt="LobsterBoard Dashboard Screenshot" class="screenshot" loading="lazy">
      </div>
    </div>
  </section>

  <!-- Widgets -->
  <section id="widgets" class="section">
    <div class="container">
      <h2 class="section-title">50+ Widgets & Counting</h2>
      <p class="section-sub">From system monitoring to smart home — there's a widget for that.</p>
      <div class="widget-categories">
        <div class="widget-cat">
          <h3>🖥️ System Monitoring</h3>
          <ul>
            <li>CPU / Memory</li>
            <li>Disk Usage</li>
            <li>Network Speed</li>
            <li>Uptime Monitor</li>
            <li>Docker Containers</li>
          </ul>
        </div>
        <div class="widget-cat">
          <h3>🤖 AI / LLM Tracking</h3>
          <ul>
            <li>Claude Usage</li>
            <li>GPT Usage</li>
            <li>Gemini Usage</li>
            <li>Combined AI View</li>
            <li>AI Cost Tracker</li>
          </ul>
        </div>
        <div class="widget-cat">
          <h3>⏰ Time & Productivity</h3>
          <ul>
            <li>Clock & World Clock</li>
            <li>Countdown Timer</li>
            <li>Pomodoro Timer</li>
            <li>Todo List</li>
            <li>Calendar (iCal)</li>
            <li>Notes</li>
          </ul>
        </div>
        <div class="widget-cat">
          <h3>💰 Finance & Weather</h3>
          <ul>
            <li>Stock Ticker</li>
            <li>Crypto Prices</li>
            <li>Local Weather</li>
            <li>World Weather</li>
          </ul>
        </div>
        <div class="widget-cat">
          <h3>🏠 Smart Home & Media</h3>
          <ul>
            <li>Indoor Climate</li>
            <li>Camera Feed</li>
            <li>Power Usage</li>
            <li>RSS Ticker</li>
            <li>Now Playing</li>
            <li>Unread Emails</li>
          </ul>
        </div>
        <div class="widget-cat">
          <h3>🔗 Embeds & Utilities</h3>
          <ul>
            <li>Image & Random Image</li>
            <li>Quick Links</li>
            <li>Iframe Embed</li>
            <li>Release Tracker</li>
            <li>API Status</li>
            <li>GitHub Stats</li>
            <li>Headers & Dividers</li>
          </ul>
        </div>
        <div class="widget-cat">
          <h3>🦞 OpenClaw Integration</h3>
          <ul>
            <li>Auth Status</li>
            <li>Release Checker</li>
            <li>Activity List</li>
            <li>Cron Jobs</li>
            <li>System Log</li>
            <li>Active Sessions</li>
            <li>Token Gauge</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- Quick Start -->
  <section id="quickstart" class="section section-dark">
    <div class="container">
      <h2 class="section-title">Up & Running in 30 Seconds</h2>
      <div class="quickstart-grid">
        <div class="quickstart-option">
          <h3>Option A: npm</h3>
          <pre><code><span class="prompt">$</span> npm install lobsterboard
<span class="prompt">$</span> cd node_modules/lobsterboard
<span class="prompt">$</span> node server.cjs</code></pre>
        </div>
        <div class="quickstart-option">
          <h3>Option B: Clone</h3>
          <pre><code><span class="prompt">$</span> git clone https://github.com/curbob/LobsterBoard.git
<span class="prompt">$</span> cd LobsterBoard
<span class="prompt">$</span> npm install
<span class="prompt">$</span> node server.cjs</code></pre>
        </div>
      </div>
      <p class="quickstart-after">Then open <code>http://localhost:8080</code> → press <kbd>Ctrl+E</kbd> → drag widgets → click 💾 Save.</p>
    </div>
  </section>

  <!-- Mascot / CTA -->
  <section class="section cta-section">
    <div class="container cta-inner">
      <img src="site-assets/lobsterboard-mascot-clean.png" alt="LobsterBoard Mascot" class="mascot">
      <div>
        <h2>Ready to build your dashboard?</h2>
        <p>Open source and built for tinkerers. Star us on GitHub and get started today.</p>
        <div class="hero-actions">
          <a href="https://github.com/curbob/LobsterBoard" target="_blank" class="btn btn-primary btn-lg">⭐ Star on GitHub</a>
          <a href="https://www.npmjs.com/package/lobsterboard" target="_blank" class="btn btn-outline btn-lg">View on npm</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer">
    <div class="container footer-inner">
      <div class="footer-left">
        <img src="site-assets/lobsterboard-logo-white.png" alt="LobsterBoard" height="24">
        <span>BSL-1.1 License · Made with 🦞 by <a href="https://github.com/curbob">curbob</a></span>
      </div>
      <div class="footer-links">
        <a href="https://github.com/curbob/LobsterBoard">GitHub</a>
        <a href="https://www.npmjs.com/package/lobsterboard">npm</a>
        <a href="https://github.com/curbob/LobsterBoard/issues">Issues</a>
      </div>
    </div>
  </footer>

  <script src="site-script.js"></script>
</body>
</html>
```

## File: `LICENSE`
```
# Business Source License 1.1

**Licensor:** Rich Curry (Curbob)

**Licensed Work:** LobsterBoard
The Licensed Work is (c) 2025-2026 Rich Curry.

**Additional Use Grant:** You may use the Licensed Work for any non-commercial purpose, including personal use, educational use, internal company use (not offered as a commercial product or service), and contributions back to the project.

**Change Date:** February 15, 2030

**Change License:** MIT License

---

## Terms

The Licensor hereby grants you the right to copy, modify, create derivative works, redistribute, and make non-commercial use of the Licensed Work.

**Commercial Use** means any use of the Licensed Work that is primarily intended for or directed toward commercial advantage or monetary compensation. This includes, but is not limited to:

- Selling the Licensed Work or derivative works
- Offering the Licensed Work as part of a paid product or service
- Using the Licensed Work to provide a commercial hosted service

If you wish to use the Licensed Work commercially, you must obtain a separate commercial license from the Licensor. Contact: **curbob@gmail.com**

Effective on the Change Date, or the fourth anniversary of the first publicly available distribution of a specific version of the Licensed Work under this License, whichever comes first, the Licensor hereby grants you rights under the terms of the Change License, and the rights granted under the Business Source License for that version terminate.

If your use of the Licensed Work does not comply with the requirements currently in effect as described in this License, you must purchase a commercial license from the Licensor, its affiliated entities, or authorized resellers, or you must refrain from using the Licensed Work.

All copies of the original and modified Licensed Work, and derivative works of the Licensed Work, are subject to this License. This License applies separately for each version of the Licensed Work.

**NOTICE:** This License does not grant you any right in any trademark or logo of the Licensor or its affiliates.

---

THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `login.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LobsterBoard — Sign In</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: #0d1117;
      color: #e6edf3;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
    }
    .card {
      background: #161b22;
      border: 1px solid #30363d;
      border-radius: 12px;
      padding: 40px 36px;
      width: 100%;
      max-width: 360px;
      box-shadow: 0 8px 32px rgba(0,0,0,0.5);
    }
    .header {
      text-align: center;
      margin-bottom: 28px;
    }
    .header .icon {
      font-size: 52px;
      line-height: 1;
      display: block;
      margin-bottom: 12px;
    }
    .header h1 {
      font-size: 22px;
      font-weight: 600;
      color: #e6edf3;
      letter-spacing: -0.3px;
    }
    .header p {
      margin-top: 6px;
      font-size: 13px;
      color: #8b949e;
    }
    .field {
      margin-bottom: 16px;
    }
    label {
      display: block;
      font-size: 13px;
      font-weight: 500;
      color: #8b949e;
      margin-bottom: 6px;
    }
    input[type="password"] {
      width: 100%;
      padding: 9px 13px;
      background: #0d1117;
      border: 1px solid #30363d;
      border-radius: 6px;
      color: #e6edf3;
      font-size: 14px;
      outline: none;
      transition: border-color 0.15s;
    }
    input[type="password"]:focus {
      border-color: #388bfd;
      box-shadow: 0 0 0 3px rgba(56,139,253,0.12);
    }
    button[type="submit"] {
      width: 100%;
      padding: 9px;
      background: #238636;
      border: 1px solid rgba(240,246,252,0.1);
      border-radius: 6px;
      color: #fff;
      font-size: 14px;
      font-weight: 500;
      cursor: pointer;
      transition: background 0.15s, opacity 0.15s;
      margin-top: 4px;
    }
    button[type="submit"]:hover:not(:disabled) { background: #2ea043; }
    button[type="submit"]:disabled { opacity: 0.55; cursor: not-allowed; }
    .error {
      display: none;
      margin-top: 14px;
      padding: 10px 13px;
      background: rgba(248,81,73,0.08);
      border: 1px solid rgba(248,81,73,0.35);
      border-radius: 6px;
      color: #f85149;
      font-size: 13px;
      line-height: 1.4;
    }
    .error.visible { display: block; }
  </style>
</head>
<body>
  <div class="card">
    <div class="header">
      <span class="icon">&#x1F99E;</span>
      <h1>LobsterBoard</h1>
      <p>Enter your password to access the dashboard</p>
    </div>
    <form id="form" autocomplete="on" onsubmit="return false;">
      <div class="field">
        <label for="password">Password</label>
        <input type="password" id="password" name="password" placeholder="Dashboard password" autocomplete="current-password" autofocus>
      </div>
      <button type="submit" id="btn">Sign in</button>
      <div class="error" id="error-msg"></div>
    </form>
  </div>

  <script>
    document.getElementById('form').addEventListener('submit', login);
    document.getElementById('btn').addEventListener('click', login);

    async function login() {
      const password = document.getElementById('password').value;
      const btn = document.getElementById('btn');
      const errEl = document.getElementById('error-msg');

      if (!password) {
        showError('Please enter your password.');
        return;
      }

      btn.disabled = true;
      btn.textContent = 'Signing in...';
      errEl.classList.remove('visible');

      try {
        const res = await fetch('/api/auth/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ password })
        });
        const data = await res.json();

        if (res.ok && data.status === 'ok') {
          window.location.href = data.redirect || '/';
        } else {
          showError(data.error || 'Incorrect password. Please try again.');
          btn.disabled = false;
          btn.textContent = 'Sign in';
          document.getElementById('password').select();
        }
      } catch (e) {
        showError('Connection error. Please try again.');
        btn.disabled = false;
        btn.textContent = 'Sign in';
      }
    }

    function showError(msg) {
      const el = document.getElementById('error-msg');
      el.textContent = msg;
      el.classList.add('visible');
    }
  </script>
</body>
</html>
```

## File: `package.json`
```json
{
  "name": "lobsterboard",
  "version": "0.8.0",
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
    "prepublishOnly": "npm run build"
  },
  "devDependencies": {
    "@rollup/plugin-terser": "^0.4.4",
    "rollup": "^4.9.6",
    "rollup-plugin-copy": "^3.5.0"
  },
  "engines": {
    "node": ">=16.0.0"
  },
  "dependencies": {
    "systeminformation": "^5.30.7"
  }
}
```

## File: `pages.json`
```json
{
  "pages": {
    "notes": { "enabled": true, "order": 10 },
    "board": { "enabled": true, "order": 20 },
    "calendar": { "enabled": true, "order": 30 }
  }
}
```

## File: `pre-commit`
```
#!/bin/bash
# Pre-commit hook: block private data in template configs
# Install: cp pre-commit .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit

PATTERNS=(
  'private-[a-f0-9]{6}'
  'caldav\.icloud\.com'
  'calendar\.google\.com/calendar/ical/.*private'
  '@gmail\.com'
  '@allinialglobal\.com'
  'sk-ant-'
)

FAILED=0
for f in $(git diff --cached --name-only -- 'templates/' 2>/dev/null); do
  [ -f "$f" ] || continue
  for pat in "${PATTERNS[@]}"; do
    if git show ":$f" 2>/dev/null | grep -qiE "$pat"; then
      echo "❌ Private data detected in $f (pattern: $pat)"
      FAILED=1
    fi
  done
done

if [ $FAILED -ne 0 ]; then
  echo ""
  echo "⚠️  Commit blocked: template files contain private data."
  echo "   Strip sensitive URLs/emails before committing."
  exit 1
fi
```

## File: `Procfile`
```
web: node server.cjs
```

## File: `README.md`
```markdown
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

👉 **Full guide with examples:** [`pages/README.md`](../../../README.md)

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

## File: `rollup.config.js`
```javascript
/**
 * LobsterBoard Rollup Configuration
 * 
 * Outputs:
 * - dist/lobsterboard.umd.js     (UMD, unminified)
 * - dist/lobsterboard.umd.min.js (UMD, minified)
 * - dist/lobsterboard.esm.js     (ES Module, unminified)
 * - dist/lobsterboard.esm.min.js (ES Module, minified)
 * - dist/lobsterboard.css        (Styles)
 */

import terser from '@rollup/plugin-terser';
import copy from 'rollup-plugin-copy';
import { readFileSync, writeFileSync, mkdirSync } from 'fs';
import { dirname } from 'path';

// Read package version
const pkg = JSON.parse(readFileSync('./package.json', 'utf8'));
const banner = `/*!
 * LobsterBoard v${pkg.version}
 * Dashboard builder with customizable widgets
 * https://github.com/curbob/LobsterBoard
 * @license MIT
 */`;

// Custom plugin to generate CSS from builder.js
function generateCss() {
  return {
    name: 'generate-css',
    writeBundle() {
      // Import the generateDashboardCss function and write the CSS
      import('./src/builder.js').then(({ generateDashboardCss }) => {
        const css = generateDashboardCss();
        const cssPath = './dist/lobsterboard.css';
        try {
          mkdirSync(dirname(cssPath), { recursive: true });
        } catch (e) {}
        writeFileSync(cssPath, `/* LobsterBoard v${pkg.version} - Dashboard Styles */\n${css}`);
        console.log('Generated dist/lobsterboard.css');
      }).catch(err => {
        console.warn('Could not generate CSS:', err.message);
      });
    }
  };
}

// Shared output options
const outputDefaults = {
  banner,
  sourcemap: true
};

export default [
  // UMD build (for browsers via script tag)
  {
    input: 'src/index.js',
    output: [
      {
        ...outputDefaults,
        file: 'dist/lobsterboard.umd.js',
        format: 'umd',
        name: 'LobsterBoard',
        exports: 'named'
      },
      {
        ...outputDefaults,
        file: 'dist/lobsterboard.umd.min.js',
        format: 'umd',
        name: 'LobsterBoard',
        exports: 'named',
        plugins: [terser({
          format: {
            comments: /^!/  // Keep banner comment
          }
        })]
      }
    ],
    plugins: [
      generateCss()
    ]
  },
  // ESM build (for modern bundlers and Node.js)
  {
    input: 'src/index.js',
    output: [
      {
        ...outputDefaults,
        file: 'dist/lobsterboard.esm.js',
        format: 'es'
      },
      {
        ...outputDefaults,
        file: 'dist/lobsterboard.esm.min.js',
        format: 'es',
        plugins: [terser({
          format: {
            comments: /^!/
          }
        })]
      }
    ]
  }
];
```

## File: `server.cjs`
```
/**
 * LobsterBoard Builder Server
 * 
 * A simple server to:
 * - Serve builder static files
 * - Handle loading and saving of config.json for the builder
 */

const http = require('http');
const fs = require('fs');
const path = require('path');
const os = require('os');
const si = require('systeminformation');
const crypto = require('crypto');

// ─────────────────────────────────────────────
// ECDH Crypto utilities for encrypted agent communication
// ─────────────────────────────────────────────
const ECDH_CURVE = 'prime256v1';
const AES_ALGORITHM = 'aes-256-gcm';
const IV_LENGTH = 12;
const AUTH_TAG_LENGTH = 16;

function generateEcdhKeyPair() {
  const ecdh = crypto.createECDH(ECDH_CURVE);
  ecdh.generateKeys();
  return {
    publicKey: ecdh.getPublicKey('base64'),
    privateKey: ecdh.getPrivateKey('base64'),
  };
}

function deriveSharedSecret(privateKeyBase64, theirPublicKeyBase64) {
  const ecdh = crypto.createECDH(ECDH_CURVE);
  ecdh.setPrivateKey(Buffer.from(privateKeyBase64, 'base64'));
  const sharedPoint = ecdh.computeSecret(Buffer.from(theirPublicKeyBase64, 'base64'));
  return crypto.createHash('sha256').update(sharedPoint).digest();
}

function decryptPayload(encryptedBase64, keyBuffer) {
  const packed = Buffer.from(encryptedBase64, 'base64');
  const iv = packed.subarray(0, IV_LENGTH);
  const authTag = packed.subarray(IV_LENGTH, IV_LENGTH + AUTH_TAG_LENGTH);
  const ciphertext = packed.subarray(IV_LENGTH + AUTH_TAG_LENGTH);
  
  const decipher = crypto.createDecipheriv(AES_ALGORITHM, keyBuffer, iv, { authTagLength: AUTH_TAG_LENGTH });
  decipher.setAuthTag(authTag);
  
  const decrypted = Buffer.concat([
    decipher.update(ciphertext),
    decipher.final(),
  ]);
  return JSON.parse(decrypted.toString('utf8'));
}

const PORT = process.env.PORT || 8080;
const HOST = process.env.HOST || '127.0.0.1';

// ─────────────────────────────────────────────
// Pages System — auto-discovery and mounting
// ─────────────────────────────────────────────
// Load from both package pages AND user's working directory pages (user overrides package)
const CWD = process.cwd();
// When run via npx/bin, LOBSTERBOARD_PKG_DIR tells us where the package is
const PKG_DIR = process.env.LOBSTERBOARD_PKG_DIR || __dirname;
const USER_PAGES_DIR = path.join(CWD, 'pages');
const PKG_PAGES_DIR = path.join(PKG_DIR, 'pages');
const PAGES_DIRS = [PKG_PAGES_DIR]; // Package pages first
if (CWD !== PKG_DIR && fs.existsSync(USER_PAGES_DIR)) {
  PAGES_DIRS.push(USER_PAGES_DIR); // User pages override
}
// For backwards compat, PAGES_DIR points to first available (used for _shared)
const PAGES_DIR = fs.existsSync(USER_PAGES_DIR) ? USER_PAGES_DIR : PKG_PAGES_DIR;
const USER_PAGES_JSON = path.join(CWD, 'pages.json');
const PKG_PAGES_JSON = path.join(__dirname, 'pages.json');
const PAGES_JSON = fs.existsSync(USER_PAGES_JSON) ? USER_PAGES_JSON : PKG_PAGES_JSON;
// Data always in working directory (user's data)
const DATA_DIR = path.join(CWD, 'data');

let loadedPages = []; // { id, title, icon, description, order, routes: { 'METHOD /path': handler } }

function loadPages() {
  const pages = [];
  const seenIds = new Set();
  let overrides = { pages: {} };
  try { overrides = JSON.parse(fs.readFileSync(PAGES_JSON, 'utf8')); } catch (_) {}

  // Scan all page directories (user pages loaded last to override package pages)
  for (const pagesDir of PAGES_DIRS) {
    let dirs;
    try { dirs = fs.readdirSync(pagesDir); } catch (_) { continue; }

    for (const dir of dirs) {
      if (dir.startsWith('_')) continue;
      const metaPath = path.join(pagesDir, dir, 'page.json');
      if (!fs.existsSync(metaPath)) continue;

      let meta;
      try { meta = JSON.parse(fs.readFileSync(metaPath, 'utf8')); } catch (_) { continue; }

      const override = overrides.pages[meta.id] || {};
      meta.enabled = override.enabled ?? meta.enabled ?? true;
      meta.order = override.order ?? meta.order ?? 99;

      if (!meta.enabled) continue;

      // If we've seen this ID before (from package), remove it so user page wins
      if (seenIds.has(meta.id)) {
        const idx = pages.findIndex(p => p.id === meta.id);
        if (idx !== -1) pages.splice(idx, 1);
      }
      seenIds.add(meta.id);

      // Store which directory this page came from
      meta._pagesDir = pagesDir;

      // Ensure data dir
      const dataDir = path.join(DATA_DIR, meta.id);
      fs.mkdirSync(dataDir, { recursive: true });

      // Load API routes if api.cjs (or api.js) exists
      let apiPath = path.join(pagesDir, dir, 'api.cjs');
      if (!fs.existsSync(apiPath)) apiPath = path.join(pagesDir, dir, 'api.js');
      let routes = {};
      if (fs.existsSync(apiPath)) {
        try {
          const ctx = {
            dataDir,
            readData: (filename) => JSON.parse(fs.readFileSync(path.join(dataDir, filename), 'utf8')),
            writeData: (filename, obj) => {
              fs.mkdirSync(dataDir, { recursive: true });
              fs.writeFileSync(path.join(dataDir, filename), JSON.stringify(obj, null, 2));
            }
          };
          const pageModule = require(apiPath)(ctx);
          routes = pageModule.routes || {};
        } catch (e) {
          console.error(`Error loading page API for ${meta.id}:`, e.message);
        }
      }

      pages.push({
        id: meta.id,
        title: meta.title,
        icon: meta.icon,
        description: meta.description,
        order: meta.order,
        nav: meta.nav !== false,
        _pagesDir: pagesDir,
        routes
      });
    }
  }

  return pages.sort((a, b) => a.order - b.order);
}

// Parse a route pattern like 'GET /items/:id' into a regex + param names
function compileRoute(pattern) {
  const [method, ...pathParts] = pattern.split(' ');
  const routePath = pathParts.join(' ');
  const paramNames = [];

  // Handle wildcard * segments
  let regexStr = routePath.replace(/\*/g, '(.+)').replace(/:([^/]+)/g, (_, name) => {
    paramNames.push(name);
    return '([^/]+)';
  });

  // Track if wildcard was used
  const hasWildcard = routePath.includes('*');
  if (hasWildcard && !paramNames.includes('*')) {
    // Insert wildcard param name at the position it appears
    const parts = routePath.split('/');
    let wildcardIdx = 0;
    for (let i = 0; i < parts.length; i++) {
      if (parts[i] === '*') {
        paramNames.splice(wildcardIdx, 0, '*');
        break;
      }
      if (parts[i].startsWith(':')) wildcardIdx++;
      if (parts[i] === '*') break;
    }
  }

  return { method: method.toUpperCase(), regex: new RegExp('^' + regexStr + '$'), paramNames };
}

// Try to match a request against page routes
function matchPageRoute(pages, method, pathname, parsedUrl) {
  // Check /api/pages listing endpoint
  if (method === 'GET' && pathname === '/api/pages') {
    return { type: 'list' };
  }

  // Check /pages/<id> for static file serving
  const pagesMatch = pathname.match(/^\/pages\/([^/]+)(\/.*)?$/);
  if (pagesMatch) {
    const pageId = pagesMatch[1];
    if (pageId === '_shared') {
      return { type: 'static', filePath: path.join(PAGES_DIR, '_shared', (pagesMatch[2] || '/').slice(1)) };
    }
    const page = pages.find(p => p.id === pageId);
    if (page) {
      const subPath = pagesMatch[2] || '';
      // Redirect /pages/id to /pages/id/ (trailing slash) for proper relative path resolution
      if (!subPath) {
        return { type: 'redirect', location: `/pages/${pageId}/` };
      }
      const pageDir = page._pagesDir || PAGES_DIR;
      if (subPath === '/') {
        return { type: 'static', filePath: path.join(pageDir, pageId, 'index.html') };
      }
      return { type: 'static', filePath: path.join(pageDir, pageId, subPath.slice(1)) };
    }
  }

  // Check /api/pages/<id>/* for API routes
  const apiMatch = pathname.match(/^\/api\/pages\/([^/]+)(\/.*)?$/);
  if (apiMatch) {
    const pageId = apiMatch[1];
    const page = pages.find(p => p.id === pageId);
    if (!page) return null;

    const subPath = apiMatch[2] || '/';
    const routeEntries = Object.entries(page.routes);

    // Sort routes: specific before wildcard, longer before shorter
    routeEntries.sort((a, b) => {
      const aHasWild = a[0].includes('*');
      const bHasWild = b[0].includes('*');
      if (aHasWild !== bHasWild) return aHasWild ? 1 : -1;
      return b[0].length - a[0].length;
    });

    for (const [pattern, handler] of routeEntries) {
      const compiled = compileRoute(pattern);
      if (compiled.method !== method) continue;
      const match = subPath.match(compiled.regex);
      if (match) {
        const params = {};
        compiled.paramNames.forEach((name, i) => {
          params[name] = decodeURIComponent(match[i + 1]);
        });
        const query = {};
        parsedUrl.searchParams.forEach((v, k) => { query[k] = v; });
        return { type: 'api', handler, params, query, pageId };
      }
    }
  }

  return null;
}

// Initialize pages
loadedPages = loadPages();
console.log(`📄 Loaded ${loadedPages.length} page(s): ${loadedPages.map(p => p.icon + ' ' + p.title).join(', ') || 'none'}`);

// ─────────────────────────────────────────────
// System Stats Collection (cached, tiered intervals)
// ─────────────────────────────────────────────
const cachedStats = {
  cpu: null,
  memory: null,
  disk: null,
  network: null,
  docker: null,
  uptime: null,
  timestamp: null
};

const sseClients = new Set();

function broadcastStats() {
  const payload = `data: ${JSON.stringify(cachedStats)}\n\n`;
  for (const res of sseClients) {
    try { res.write(payload); } catch (_) { sseClients.delete(res); }
  }
}

// Guard against overlapping async calls when si.* is slow
let _cpuNetRunning = false;
let _memRunning = false;
let _diskRunning = false;
let _dockerRunning = false;

// CPU + Network: every 2s
setInterval(async () => {
  if (_cpuNetRunning) return;
  _cpuNetRunning = true;
  try {
    const [cpu, net] = await Promise.all([
      si.currentLoad(),
      si.networkStats()
    ]);
    cachedStats.cpu = { currentLoad: cpu.currentLoad, cpus: cpu.cpus.map(c => c.load) };
    cachedStats.network = net.map(n => ({
      iface: n.iface, rx_sec: n.rx_sec, tx_sec: n.tx_sec,
      rx_bytes: n.rx_bytes, tx_bytes: n.tx_bytes
    }));
    cachedStats.timestamp = Date.now();
    broadcastStats();
  } catch (e) { console.error('Stats error (cpu/net):', e.message); }
  _cpuNetRunning = false;
}, 2000);

// Memory: every 5s
setInterval(async () => {
  if (_memRunning) return;
  _memRunning = true;
  try {
    const mem = await si.mem();
    cachedStats.memory = { total: mem.total, used: mem.used, free: mem.free, active: mem.active };
  } catch (e) { console.error('Stats error (mem):', e.message); }
  _memRunning = false;
}, 5000);

// Disk: every 30s
setInterval(async () => {
  if (_diskRunning) return;
  _diskRunning = true;
  try {
    const disk = await si.fsSize();
    cachedStats.disk = disk.map(d => ({
      fs: d.fs, mount: d.mount, size: d.size, used: d.used, available: d.available, use: d.use
    }));
  } catch (e) { console.error('Stats error (disk):', e.message); }
  _diskRunning = false;
}, 30000);

// Docker: every 5s (graceful fail)
setInterval(async () => {
  if (_dockerRunning) return;
  _dockerRunning = true;
  try {
    cachedStats.docker = await si.dockerContainers();
  } catch (_) { cachedStats.docker = []; }
  _dockerRunning = false;
}, 5000);

// Uptime: every 60s
setInterval(async () => {
  try {
    cachedStats.uptime = si.time().uptime;
  } catch (e) { console.error('Stats error (uptime):', e.message); }
}, 60000);

// Initial fetch
(async () => {
  try {
    const [cpu, mem, disk, net] = await Promise.all([
      si.currentLoad(), si.mem(), si.fsSize(), si.networkStats()
    ]);
    cachedStats.cpu = { currentLoad: cpu.currentLoad, cpus: cpu.cpus.map(c => c.load) };
    cachedStats.memory = { total: mem.total, used: mem.used, free: mem.free, active: mem.active };
    cachedStats.disk = disk.map(d => ({ fs: d.fs, mount: d.mount, size: d.size, used: d.used, available: d.available, use: d.use }));
    cachedStats.network = net.map(n => ({ iface: n.iface, rx_sec: n.rx_sec, tx_sec: n.tx_sec, rx_bytes: n.rx_bytes, tx_bytes: n.tx_bytes }));
    cachedStats.uptime = si.time().uptime;
    cachedStats.timestamp = Date.now();
    try { cachedStats.docker = await si.dockerContainers(); } catch (_) { cachedStats.docker = []; }
  } catch (e) { console.error('Initial stats fetch error:', e.message); }
})();

const MIME_TYPES = {
  '.html': 'text/html', '.css': 'text/css', '.js': 'application/javascript',
  '.json': 'application/json', '.png': 'image/png', '.jpg': 'image/jpeg',
  '.gif': 'image/gif', '.svg': 'image/svg+xml', '.ico': 'image/x-icon',
  '.map': 'application/json' // For sourcemaps
};

// User config files — stored in working directory (survives npm updates)
const CONFIG_FILE = path.join(CWD, 'config.json');
const AUTH_FILE = path.join(CWD, 'auth.json');
const SECRETS_FILE = path.join(CWD, 'secrets.json');

// ─────────────────────────────────────────────
// Migration: copy data from package dir to user dir (v0.6.2+)
// ─────────────────────────────────────────────
function migrateUserData() {
  const filesToMigrate = ['config.json', 'auth.json', 'secrets.json', 'todos.json', 'notes.json'];
  const dirsToMigrate = ['data'];
  let migrated = [];

  for (const file of filesToMigrate) {
    const userPath = path.join(CWD, file);
    const pkgPath = path.join(PKG_DIR, file);
    if (!fs.existsSync(userPath) && fs.existsSync(pkgPath)) {
      try {
        fs.copyFileSync(pkgPath, userPath);
        migrated.push(file);
      } catch (e) { /* ignore */ }
    }
  }

  for (const dir of dirsToMigrate) {
    const userDir = path.join(CWD, dir);
    const pkgDir = path.join(PKG_DIR, dir);
    if (!fs.existsSync(userDir) && fs.existsSync(pkgDir)) {
      try {
        fs.cpSync(pkgDir, userDir, { recursive: true });
        migrated.push(dir + '/');
      } catch (e) { /* ignore */ }
    }
  }

  if (migrated.length > 0) {
    console.log(`📦 Migrated data to working directory: ${migrated.join(', ')}`);
  }
}

// Run migration on startup
if (CWD !== PKG_DIR) {
  migrateUserData();
}

// ─────────────────────────────────────────────
// Server-side Session Authentication
// ─────────────────────────────────────────────

const DASHBOARD_PASSWORD = process.env.DASHBOARD_PASSWORD || null;
const SESSION_TTL_MS = (parseInt(process.env.SESSION_TTL_HOURS) || 24) * 60 * 60 * 1000;

// In-memory session store: token -> expiresAt timestamp
const sessions = new Map();

// Rate limit store: ip -> { count, resetAt }
const loginAttempts = new Map();
const MAX_LOGIN_ATTEMPTS = 5;
const LOCKOUT_MS = 15 * 60 * 1000;

function generateSessionToken() {
  return crypto.randomBytes(32).toString('hex'); // 64-char hex
}

function createSession() {
  const token = generateSessionToken();
  sessions.set(token, Date.now() + SESSION_TTL_MS);
  return token;
}

function isValidSession(token) {
  if (!token || !/^[a-f0-9]{64}$/.test(token)) return false;
  const exp = sessions.get(token);
  if (!exp) return false;
  if (Date.now() > exp) { sessions.delete(token); return false; }
  return true;
}

function getSessionCookie(req) {
  const cookie = req.headers.cookie || '';
  const match = cookie.match(/(?:^|;\s*)lb_session=([a-f0-9]{64})/);
  return match ? match[1] : null;
}

function checkPassword(input) {
  if (!DASHBOARD_PASSWORD || !input) return false;
  // HMAC both inputs so timingSafeEqual always compares equal-length buffers
  const inputHash = crypto.createHmac('sha256', 'lb-session-auth').update(String(input)).digest();
  const correctHash = crypto.createHmac('sha256', 'lb-session-auth').update(DASHBOARD_PASSWORD).digest();
  return crypto.timingSafeEqual(inputHash, correctHash);
}

function isRateLimited(ip) {
  const entry = loginAttempts.get(ip);
  if (!entry) return false;
  if (Date.now() > entry.resetAt) { loginAttempts.delete(ip); return false; }
  return entry.count >= MAX_LOGIN_ATTEMPTS;
}

function recordFailedAttempt(ip) {
  const entry = loginAttempts.get(ip) || { count: 0, resetAt: Date.now() + LOCKOUT_MS };
  entry.count++;
  loginAttempts.set(ip, entry);
}

// Clean expired sessions every hour
setInterval(() => {
  const now = Date.now();
  for (const [token, exp] of sessions) {
    if (now > exp) sessions.delete(token);
  }
}, 60 * 60 * 1000);

// ─────────────────────────────────────────────
// Security helpers
// ─────────────────────────────────────────────

function hashPin(pin) {
  return crypto.createHash('sha256').update(pin).digest('hex');
}

function readJsonFile(filepath, fallback) {
  try { return JSON.parse(fs.readFileSync(filepath, 'utf8')); } catch (_) { return fallback; }
}

function writeJsonFile(filepath, data) {
  fs.writeFileSync(filepath, JSON.stringify(data, null, 2));
}

function getAuth() { return readJsonFile(AUTH_FILE, {}); }
function getSecrets() { return readJsonFile(SECRETS_FILE, {}); }

const SENSITIVE_KEYS = ['apiKey', 'api_key', 'token', 'secret', 'password', 'icalUrl'];

function isSensitiveKey(key) {
  return SENSITIVE_KEYS.includes(key);
}

function isPublicMode() {
  const auth = getAuth();
  return auth.publicMode === true;
}

/** Mask sensitive fields in config before sending to browser */
function maskConfig(config) {
  const secrets = getSecrets();
  const masked = JSON.parse(JSON.stringify(config));
  if (masked.widgets) {
    masked.widgets.forEach(w => {
      if (!w.properties) return;
      const widgetSecrets = secrets[w.id] || {};
      for (const key of Object.keys(w.properties)) {
        if (isSensitiveKey(key) && (w.properties[key] === '__SECRET__' || widgetSecrets[key])) {
          w.properties[key] = '••••••••';
        }
      }
    });
  }
  return masked;
}

/** On save: extract sensitive values into secrets.json, replace with __SECRET__ in config */
function extractSecrets(config) {
  const secrets = getSecrets();
  if (config.widgets) {
    config.widgets.forEach(w => {
      if (!w.properties) return;
      for (const key of Object.keys(w.properties)) {
        if (isSensitiveKey(key)) {
          const val = w.properties[key];
          if (val && val !== '__SECRET__' && val !== '••••••••') {
            if (!secrets[w.id]) secrets[w.id] = {};
            secrets[w.id][key] = val;
            w.properties[key] = '__SECRET__';
          } else if (val === '••••••••') {
            // User didn't change it — keep existing secret, restore placeholder
            w.properties[key] = '__SECRET__';
          }
        }
      }
    });
  }
  writeJsonFile(SECRETS_FILE, secrets);
  return config;
}

// Scan templates directory for meta.json files
function scanTemplates(templatesDir) {
  const templates = [];
  try {
    const dirs = fs.readdirSync(templatesDir);
    for (const dir of dirs) {
      if (dir === 'templates.json' || dir === 'README.md' || dir.startsWith('.')) continue;
      const metaPath = path.join(templatesDir, dir, 'meta.json');
      if (fs.existsSync(metaPath)) {
        try {
          const meta = JSON.parse(fs.readFileSync(metaPath, 'utf8'));
          templates.push(meta);
        } catch (_) {}
      }
    }
  } catch (_) {}
  return templates;
}

// Release check cache (1 hour TTL)
let _releaseCache = null;
let _releaseCacheTime = 0;
let _lbReleaseCache = null;
let _lbReleaseCacheTime = 0;

function sendResponse(res, statusCode, contentType, data, extraHeaders = {}) {
  res.writeHead(statusCode, { 'Content-Type': contentType, ...extraHeaders });
  res.end(data);
}

function sendJson(res, statusCode, data) {
  sendResponse(res, statusCode, 'application/json', JSON.stringify(data), { 'Access-Control-Allow-Origin': '*' });
}

function sendError(res, message, statusCode = 500) {
  sendJson(res, statusCode, { status: 'error', message });
}

// Parse iCal (.ics) text into sorted upcoming events
function parseIcal(text, maxEvents) {
  const now = new Date();
  const events = [];
  // Unfold continuation lines (RFC 5545: lines starting with space/tab are continuations)
  const unfolded = text.replace(/\r?\n[ \t]/g, '');
  const blocks = unfolded.split('BEGIN:VEVENT');
  for (let i = 1; i < blocks.length; i++) {
    const block = blocks[i].split('END:VEVENT')[0];
    if (!block) continue;
    const get = (key) => { const m = block.match(new RegExp('^' + key + '(?:;[^:]*)?:(.*)$', 'm')); return m ? m[1].trim() : ''; };
    const getWithParams = (key) => { const m = block.match(new RegExp('^' + key + '((?:;[^:]*)?):(.*)$', 'm')); return m ? { params: m[1], value: m[2].trim() } : { params: '', value: '' }; };
    const summary = get('SUMMARY').replace(/\\,/g, ',').replace(/\\n/g, ' ');
    const location = get('LOCATION').replace(/\\,/g, ',').replace(/\\n/g, ' ');
    const dtstart = get('DTSTART');
    const dtstartFull = getWithParams('DTSTART');
    const dtendFull = getWithParams('DTEND');
    if (!dtstart) continue;
    // Parse iCal date: 20260210T150000Z or 20260210 (all-day)
    const allDay = dtstart.length === 8;
    // Map Windows/iCal TZID names to UTC offset (hours). Covers common zones.
    const tzOffsets = {
      'eastern standard time': -5, 'eastern daylight time': -4, 'us/eastern': -5, 'america/new_york': -5,
      'central standard time': -6, 'central daylight time': -5, 'us/central': -6, 'america/chicago': -6,
      'central america standard time': -6,
      'mountain standard time': -7, 'mountain daylight time': -6, 'us/mountain': -7, 'america/denver': -7,
      'pacific standard time': -8, 'pacific daylight time': -7, 'us/pacific': -8, 'america/los_angeles': -8,
      'pacific standard time (mexico)': -8,
      'india standard time': 5.5, 'asia/kolkata': 5.5,
      'sri lanka standard time': 5.5,
      'singapore standard time': 8, 'asia/singapore': 8,
      'china standard time': 8, 'asia/shanghai': 8,
      'tokyo standard time': 9, 'asia/tokyo': 9,
      'e. africa standard time': 3,
      'romance standard time': 1,
      'gmt standard time': 0, 'utc': 0, 'gmt': 0,
      'w. europe standard time': 1, 'europe/berlin': 1, 'europe/paris': 1,
    };
    const parseIcalDate = (s, params) => {
      if (!s) return null;
      if (s.length === 8) return new Date(s.slice(0,4) + '-' + s.slice(4,6) + '-' + s.slice(6,8) + 'T00:00:00');
      // 20260210T150000Z or 20260210T150000
      const d = s.replace(/Z$/, '');
      const iso = d.slice(0,4) + '-' + d.slice(4,6) + '-' + d.slice(6,8) + 'T' + d.slice(9,11) + ':' + d.slice(11,13) + ':' + d.slice(13,15);
      if (s.endsWith('Z')) return new Date(iso + 'Z');
      // Check for TZID parameter
      const tzMatch = (params || '').match(/TZID=([^;:]+)/i);
      if (tzMatch) {
        const tzName = tzMatch[1].trim().toLowerCase();
        const offsetHours = tzOffsets[tzName];
        if (offsetHours !== undefined) {
          // Convert from source timezone to UTC by appending the UTC offset
          const sign = offsetHours >= 0 ? '+' : '-';
          const absH = Math.floor(Math.abs(offsetHours));
          const absM = Math.round((Math.abs(offsetHours) - absH) * 60);
          const offsetStr = sign + String(absH).padStart(2, '0') + ':' + String(absM).padStart(2, '0');
          return new Date(iso + offsetStr);
        }
      }
      // No timezone info — treat as local
      return new Date(iso);
    };
    const start = parseIcalDate(dtstart, dtstartFull.params);
    const end = parseIcalDate(dtendFull.value, dtendFull.params);
    if (!start || isNaN(start.getTime())) continue;
    // Only future events (for all-day, include today)
    const cutoff = allDay ? new Date(now.getFullYear(), now.getMonth(), now.getDate()) : now;
    if (start < cutoff && (!end || end < cutoff)) continue;
    events.push({ summary: summary || 'Untitled', start: start.toISOString(), end: end ? end.toISOString() : null, location: location || null, allDay });
  }
  events.sort((a, b) => new Date(a.start) - new Date(b.start));
  return events.slice(0, maxEvents);
}

// ─────────────────────────────────────────────
// AI Usage Providers - Read local credentials and fetch usage
// ─────────────────────────────────────────────

const AI_PROVIDERS = {
  claude: {
    name: 'Claude Code',
    icon: '🟣',
    credPaths: [
      path.join(os.homedir(), '.claude', '.credentials.json'),
    ],
    keychainService: 'Claude Code-credentials',
  },
  codex: {
    name: 'Codex CLI',
    icon: '🟢',
    credPaths: [
      process.env.CODEX_HOME ? path.join(process.env.CODEX_HOME, 'auth.json') : null,
      path.join(os.homedir(), '.config', 'codex', 'auth.json'),
      path.join(os.homedir(), '.codex', 'auth.json'),
    ].filter(Boolean),
    keychainService: 'Codex Auth',
  },
  copilot: {
    name: 'GitHub Copilot',
    icon: '⚫',
    keychainService: 'gh:github.com',
  },
  cursor: {
    name: 'Cursor',
    icon: '🔵',
    sqlitePath: path.join(os.homedir(), 'Library', 'Application Support', 'Cursor', 'User', 'globalStorage', 'state.vscdb'),
  },
  gemini: {
    name: 'Gemini',
    icon: '🔷',
    credPaths: [
      path.join(os.homedir(), '.gemini', 'oauth_creds.json'),
    ],
    settingsPath: path.join(os.homedir(), '.gemini', 'settings.json'),
  },
  amp: {
    name: 'Amp',
    icon: '⚡',
    credPaths: [
      path.join(os.homedir(), '.local', 'share', 'amp', 'secrets.json'),
    ],
  },
  factory: {
    name: 'Factory',
    icon: '🏭',
    credPaths: [
      path.join(os.homedir(), '.factory', 'auth.json'),
    ],
  },
  kimi: {
    name: 'Kimi Code',
    icon: '🌙',
    credPaths: [
      path.join(os.homedir(), '.kimi', 'credentials', 'kimi-code.json'),
    ],
  },
  jetbrains: {
    name: 'JetBrains AI',
    icon: '🧠',
    configDirs: [
      path.join(os.homedir(), 'Library', 'Application Support', 'JetBrains'),
    ],
  },
  minimax: {
    name: 'MiniMax',
    icon: '🔶',
    envKeys: ['MINIMAX_API_KEY', 'MINIMAX_CN_API_KEY', 'MINIMAX_API_TOKEN'],
  },
  zai: {
    name: 'Z.ai',
    icon: '🇿',
    envKeys: ['ZAI_API_KEY', 'GLM_API_KEY'],
  },
  antigravity: {
    name: 'Antigravity',
    icon: '🪐',
    configPath: path.join(os.homedir(), 'Library', 'Application Support', 'antigravity-usage', 'config.json'),
    accountsDir: path.join(os.homedir(), 'Library', 'Application Support', 'antigravity-usage', 'accounts'),
    // OAuth credentials from env vars (get from antigravity-usage or Google Cloud Console)
    tokenUrl: 'https://oauth2.googleapis.com/token',
    apiUrl: 'https://cloudcode-pa.googleapis.com/v1internal:fetchAvailableModels',
  },
};

// Try to read credentials from file paths, then keychain (macOS)
function readCredentials(provider) {
  const config = AI_PROVIDERS[provider];
  if (!config) return null;
  
  // Try file paths first
  for (const credPath of config.credPaths) {
    try {
      if (fs.existsSync(credPath)) {
        const content = fs.readFileSync(credPath, 'utf8');
        return { source: 'file', path: credPath, data: JSON.parse(content) };
      }
    } catch (e) {
      // Continue to next path
    }
  }
  
  // Try macOS keychain (may have multiple entries with different accounts)
  if (process.platform === 'darwin' && config.keychainService) {
    const { execSync } = require('child_process');
    const accounts = [process.env.USER, os.userInfo().username, 'Claude Code', ''].filter(Boolean);
    
    for (const account of accounts) {
      try {
        const accountArg = account ? `-a "${account}"` : '';
        const keychainData = execSync(
          `security find-generic-password -s "${config.keychainService}" ${accountArg} -w 2>/dev/null`,
          { encoding: 'utf8', timeout: 5000 }
        ).trim();
        if (keychainData) {
          const parsed = JSON.parse(keychainData);
          // Check if this token is valid (not expired)
          const oauth = parsed.claudeAiOauth || parsed;
          if (oauth.expiresAt && oauth.expiresAt > Date.now()) {
            return { source: 'keychain', service: config.keychainService, account, data: parsed };
          }
          // If no expiry or expired, keep looking but save as fallback
          if (!config._fallbackCreds) {
            config._fallbackCreds = { source: 'keychain', service: config.keychainService, account, data: parsed };
          }
        }
      } catch (e) {
        // Try next account
      }
    }
    // Return fallback if we found expired creds but nothing valid
    if (config._fallbackCreds) {
      const result = config._fallbackCreds;
      delete config._fallbackCreds;
      return result;
    }
  }
  
  return null;
}

// Fetch Claude usage
async function fetchClaudeUsage() {
  const baseInfo = {
    provider: 'claude',
    name: AI_PROVIDERS.claude.name,
    icon: AI_PROVIDERS.claude.icon,
  };
  
  const creds = readCredentials('claude');
  if (!creds) return { ...baseInfo, error: 'Not logged in. Run `claude` to authenticate.' };
  
  const oauthData = creds.data.claudeAiOauth;
  if (!oauthData?.accessToken) return { ...baseInfo, error: 'No access token found.' };
  
  let accessToken = oauthData.accessToken;
  
  // Helper to make the API request
  async function makeRequest(token) {
    const resp = await fetch('https://api.anthropic.com/api/oauth/usage', {
      headers: {
        'Authorization': `Bearer ${token}`,
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'anthropic-beta': 'oauth-2025-04-20',
        'User-Agent': 'claude-code/1.0.0',
        'X-Client-Name': 'claude-code',
      },
    });
    return resp;
  }
  
  // Try with current token first
  let resp = await makeRequest(accessToken);
  
  // If unauthorized, try to refresh
  if (resp.status === 401 || resp.status === 403) {
    if (!oauthData.refreshToken) {
      return { ...baseInfo, error: 'Session expired. Run `claude` to re-authenticate.' };
    }
    try {
      const refreshed = await refreshClaudeToken(oauthData.refreshToken, creds.source === 'file' ? creds.path : null);
      if (refreshed.error) {
        return { ...baseInfo, error: 'Session expired. Run `claude` to re-authenticate.' };
      }
      accessToken = refreshed.accessToken;
      resp = await makeRequest(accessToken);
    } catch (e) {
      return { ...baseInfo, error: 'Session expired. Run `claude` to re-authenticate.' };
    }
  }
  
  try {
    if (!resp.ok) {
      if (resp.status === 429) {
        return { ...baseInfo, error: '429 rate limited - using cache' };
      }
      return { ...baseInfo, error: `API error (HTTP ${resp.status})` };
    }
    
    const data = await resp.json();
    
    // Normalize response
    const metrics = [];
    
    if (data.five_hour) {
      metrics.push({
        label: 'Session (5h)',
        used: data.five_hour.utilization,
        limit: 100,
        format: 'percent',
        resetsAt: data.five_hour.resets_at,
      });
    }
    
    if (data.seven_day) {
      metrics.push({
        label: 'Weekly',
        used: data.seven_day.utilization,
        limit: 100,
        format: 'percent',
        resetsAt: data.seven_day.resets_at,
      });
    }
    
    if (data.seven_day_opus) {
      metrics.push({
        label: 'Opus Weekly',
        used: data.seven_day_opus.utilization,
        limit: 100,
        format: 'percent',
        resetsAt: data.seven_day_opus.resets_at,
      });
    }
    
    if (data.extra_usage?.is_enabled) {
      metrics.push({
        label: 'Extra Credits',
        used: data.extra_usage.used_credits / 100,
        limit: data.extra_usage.monthly_limit ? data.extra_usage.monthly_limit / 100 : null,
        format: 'dollars',
      });
    }
    
    return {
      provider: 'claude',
      name: AI_PROVIDERS.claude.name,
      icon: AI_PROVIDERS.claude.icon,
      plan: oauthData.subscriptionType || 'unknown',
      metrics,
    };
  } catch (e) {
    return { ...baseInfo, error: 'Network error: ' + e.message };
  }
}

// Refresh Claude token
async function refreshClaudeToken(refreshToken, credPath) {
  try {
    const resp = await fetch('https://platform.claude.com/v1/oauth/token', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        grant_type: 'refresh_token',
        refresh_token: refreshToken,
        client_id: '9d1c250a-e61b-44d9-88ed-5944d1962f5e',
        scope: 'user:profile user:inference user:sessions:claude_code user:mcp_servers',
      }),
    });
    
    if (!resp.ok) return { error: 'Refresh failed (HTTP ' + resp.status + ')' };
    
    const data = await resp.json();
    
    // Update credentials file
    if (credPath && fs.existsSync(credPath)) {
      try {
        const existing = JSON.parse(fs.readFileSync(credPath, 'utf8'));
        existing.claudeAiOauth.accessToken = data.access_token;
        if (data.refresh_token) existing.claudeAiOauth.refreshToken = data.refresh_token;
        existing.claudeAiOauth.expiresAt = Date.now() + (data.expires_in * 1000);
        fs.writeFileSync(credPath, JSON.stringify(existing, null, 2));
      } catch (e) {
        // Non-fatal: token still works for this request
      }
    }
    
    return { accessToken: data.access_token };
  } catch (e) {
    return { error: e.message };
  }
}

// Fetch Codex usage
async function fetchCodexUsage() {
  const baseInfo = {
    provider: 'codex',
    name: AI_PROVIDERS.codex.name,
    icon: AI_PROVIDERS.codex.icon,
  };
  
  const creds = readCredentials('codex');
  if (!creds) return { ...baseInfo, error: 'Not logged in. Run `codex auth` to authenticate.' };
  
  const tokens = creds.data.tokens;
  if (!tokens?.access_token) return { ...baseInfo, error: 'No access token found.' };
  
  try {
    const headers = {
      'Authorization': `Bearer ${tokens.access_token}`,
      'Accept': 'application/json',
    };
    if (tokens.account_id) {
      headers['ChatGPT-Account-Id'] = tokens.account_id;
    }
    
    const resp = await fetch('https://chatgpt.com/backend-api/wham/usage', { headers });
    
    if (!resp.ok) {
      if (resp.status === 401 || resp.status === 403) {
        return { ...baseInfo, error: 'Session expired. Run `codex auth` to re-authenticate.' };
      }
      return { ...baseInfo, error: `API error (HTTP ${resp.status})` };
    }
    
    const data = await resp.json();
    
    // Normalize response
    const metrics = [];
    
    if (data.rate_limit?.primary_window) {
      const pw = data.rate_limit.primary_window;
      metrics.push({
        label: 'Session (5h)',
        used: pw.used_percent,
        limit: 100,
        format: 'percent',
        resetsAt: pw.reset_at ? new Date(pw.reset_at * 1000).toISOString() : null,
      });
    }
    
    if (data.rate_limit?.secondary_window) {
      const sw = data.rate_limit.secondary_window;
      metrics.push({
        label: 'Weekly',
        used: sw.used_percent,
        limit: 100,
        format: 'percent',
        resetsAt: sw.reset_at ? new Date(sw.reset_at * 1000).toISOString() : null,
      });
    }
    
    if (data.code_review_rate_limit?.primary_window) {
      const cr = data.code_review_rate_limit.primary_window;
      metrics.push({
        label: 'Code Reviews',
        used: cr.used_percent,
        limit: 100,
        format: 'percent',
        resetsAt: cr.reset_at ? new Date(cr.reset_at * 1000).toISOString() : null,
      });
    }
    
    if (data.credits?.has_credits) {
      metrics.push({
        label: 'Credits',
        used: null,
        remaining: data.credits.balance,
        format: 'dollars',
        unlimited: data.credits.unlimited,
      });
    }
    
    return {
      provider: 'codex',
      name: AI_PROVIDERS.codex.name,
      icon: AI_PROVIDERS.codex.icon,
      plan: data.plan_type || 'unknown',
      metrics,
    };
  } catch (e) {
    return { ...baseInfo, error: 'Network error: ' + e.message };
  }
}

// Fetch GitHub Copilot usage
async function fetchCopilotUsage() {
  const baseInfo = {
    provider: 'copilot',
    name: AI_PROVIDERS.copilot.name,
    icon: AI_PROVIDERS.copilot.icon,
  };
  
  // Try to get token from gh CLI keychain
  let token = null;
  if (process.platform === 'darwin') {
    try {
      const { execSync } = require('child_process');
      token = execSync('security find-generic-password -s "gh:github.com" -w 2>/dev/null', 
        { encoding: 'utf8', timeout: 5000 }).trim();
    } catch (e) {}
  }
  
  if (!token) {
    return { ...baseInfo, error: 'Not logged in. Run `gh auth login` first.' };
  }
  
  try {
    const resp = await fetch('https://api.github.com/copilot_internal/user', {
      headers: {
        'Authorization': `token ${token}`,
        'Accept': 'application/json',
        'Editor-Version': 'vscode/1.96.2',
        'Editor-Plugin-Version': 'copilot-chat/0.26.7',
        'User-Agent': 'GitHubCopilotChat/0.26.7',
        'X-Github-Api-Version': '2025-04-01',
      },
    });
    
    if (!resp.ok) {
      if (resp.status === 401 || resp.status === 403) {
        return { ...baseInfo, error: 'Token invalid. Run `gh auth login` to re-auth.' };
      }
      return { ...baseInfo, error: `API error (HTTP ${resp.status})` };
    }
    
    const data = await resp.json();
    const metrics = [];
    
    // Paid tier
    if (data.quota_snapshots) {
      if (data.quota_snapshots.premium_interactions) {
        const p = data.quota_snapshots.premium_interactions;
        metrics.push({
          label: 'Premium',
          used: 100 - p.percent_remaining,
          limit: 100,
          format: 'percent',
          resetsAt: data.quota_reset_date,
        });
      }
      if (data.quota_snapshots.chat) {
        const c = data.quota_snapshots.chat;
        metrics.push({
          label: 'Chat',
          used: 100 - c.percent_remaining,
          limit: 100,
          format: 'percent',
          resetsAt: data.quota_reset_date,
        });
      }
    }
    
    // Free tier
    if (data.limited_user_quotas && data.monthly_quotas) {
      const chatUsed = data.monthly_quotas.chat - data.limited_user_quotas.chat;
      const compUsed = data.monthly_quotas.completions - data.limited_user_quotas.completions;
      metrics.push({
        label: 'Chat',
        used: (chatUsed / data.monthly_quotas.chat) * 100,
        limit: 100,
        format: 'percent',
        resetsAt: data.limited_user_reset_date,
      });
      metrics.push({
        label: 'Completions',
        used: (compUsed / data.monthly_quotas.completions) * 100,
        limit: 100,
        format: 'percent',
        resetsAt: data.limited_user_reset_date,
      });
    }
    
    return {
      ...baseInfo,
      plan: data.copilot_plan || 'unknown',
      metrics,
    };
  } catch (e) {
    return { ...baseInfo, error: 'Network error: ' + e.message };
  }
}

// Fetch Cursor usage
async function fetchCursorUsage() {
  const baseInfo = {
    provider: 'cursor',
    name: AI_PROVIDERS.cursor.name,
    icon: AI_PROVIDERS.cursor.icon,
  };
  
  const dbPath = AI_PROVIDERS.cursor.sqlitePath;
  if (!fs.existsSync(dbPath)) {
    return { ...baseInfo, error: 'Cursor not installed.' };
  }
  
  // Read token from SQLite
  let accessToken = null;
  let membershipType = null;
  try {
    const { execSync } = require('child_process');
    accessToken = execSync(`sqlite3 "${dbPath}" "SELECT value FROM ItemTable WHERE key = 'cursorAuth/accessToken'" 2>/dev/null`,
      { encoding: 'utf8', timeout: 5000 }).trim();
    membershipType = execSync(`sqlite3 "${dbPath}" "SELECT value FROM ItemTable WHERE key = 'cursorAuth/stripeMembershipType'" 2>/dev/null`,
      { encoding: 'utf8', timeout: 5000 }).trim();
  } catch (e) {}
  
  if (!accessToken) {
    return { ...baseInfo, error: 'Not logged in. Sign in to Cursor.' };
  }
  
  try {
    const resp = await fetch('https://api2.cursor.sh/aiserver.v1.DashboardService/GetCurrentPeriodUsage', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${accessToken}`,
        'Content-Type': 'application/json',
        'Connect-Protocol-Version': '1',
      },
      body: '{}',
    });
    
    if (!resp.ok) {
      if (resp.status === 401 || resp.status === 403) {
        return { ...baseInfo, error: 'Session expired. Re-sign in to Cursor.' };
      }
      return { ...baseInfo, error: `API error (HTTP ${resp.status})` };
    }
    
    const data = await resp.json();
    const metrics = [];
    
    if (data.planUsage) {
      const pu = data.planUsage;
      if (typeof pu.totalPercentUsed === 'number' && isFinite(pu.totalPercentUsed)) {
        metrics.push({
          label: 'Total Usage',
          used: pu.totalPercentUsed,
          limit: 100,
          format: 'percent',
        });
      }
      if (typeof pu.autoPercentUsed === 'number' && isFinite(pu.autoPercentUsed)) {
        metrics.push({
          label: 'Auto',
          used: pu.autoPercentUsed,
          limit: 100,
          format: 'percent',
        });
      }
      if (typeof pu.apiPercentUsed === 'number' && isFinite(pu.apiPercentUsed)) {
        metrics.push({
          label: 'API',
          used: pu.apiPercentUsed,
          limit: 100,
          format: 'percent',
        });
      }
    }
    
    return {
      ...baseInfo,
      plan: membershipType || 'unknown',
      metrics,
    };
  } catch (e) {
    return { ...baseInfo, error: 'Network error: ' + e.message };
  }
}

// Refresh Gemini CLI OAuth token.
// These client credentials are intentionally public — gemini-cli is an installed
// application and Google's own guidance permits embedding them in the source:
// https://github.com/google-gemini/gemini-cli/blob/main/packages/core/src/code_assist/oauth2.ts
const GEMINI_CLIENT_ID = '681255809395-oo8ft2oprdrnp9e3aqf6av3hmdib135j.apps.googleusercontent.com';
const GEMINI_CLIENT_SECRET = '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';

async function refreshGeminiToken(credsPath, creds) {
  if (!creds.refresh_token) return { error: 'No refresh token available.' };
  try {
    const resp = await fetch('https://oauth2.googleapis.com/token', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({
        grant_type: 'refresh_token',
        refresh_token: creds.refresh_token,
        client_id: GEMINI_CLIENT_ID,
        client_secret: GEMINI_CLIENT_SECRET,
      }),
    });
    if (!resp.ok) return { error: 'Refresh failed (HTTP ' + resp.status + ')' };
    const data = await resp.json();
    const updated = {
      ...creds,
      access_token: data.access_token,
      expiry_date: Date.now() + (data.expires_in * 1000),
    };
    if (data.refresh_token) updated.refresh_token = data.refresh_token;
    if (data.id_token) updated.id_token = data.id_token;
    try { fs.writeFileSync(credsPath, JSON.stringify(updated, null, 2)); } catch (_) {}
    return { accessToken: data.access_token, creds: updated };
  } catch (e) {
    return { error: e.message };
  }
}

// Fetch Gemini usage
async function fetchGeminiUsage() {
  const baseInfo = {
    provider: 'gemini',
    name: AI_PROVIDERS.gemini.name,
    icon: AI_PROVIDERS.gemini.icon,
  };

  const credsPath = AI_PROVIDERS.gemini.credPaths[0];
  if (!fs.existsSync(credsPath)) {
    return { ...baseInfo, error: 'Not logged in. Run `gemini auth` first.' };
  }

  let creds;
  try {
    creds = JSON.parse(fs.readFileSync(credsPath, 'utf8'));
  } catch (e) {
    return { ...baseInfo, error: 'Invalid credentials file.' };
  }

  if (!creds.access_token && !creds.refresh_token) {
    return { ...baseInfo, error: 'No access token found.' };
  }

  // Proactively refresh if the token is expired or expires within 5 minutes.
  // This handles the case where gemini-cli on another machine has rotated the
  // shared OAuth token, leaving the stored access_token stale.
  const FIVE_MINUTES = 5 * 60 * 1000;
  if (!creds.access_token || (creds.expiry_date && Date.now() >= creds.expiry_date - FIVE_MINUTES)) {
    const refreshed = await refreshGeminiToken(credsPath, creds);
    if (refreshed.error) return { ...baseInfo, error: 'Session expired. Run `gemini auth` to re-auth.' };
    creds = refreshed.creds;
  }

  const callQuotaApi = (token) => fetch('https://cloudcode-pa.googleapis.com/v1internal:retrieveUserQuota', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json',
    },
    body: '{}',
  });

  try {
    let resp = await callQuotaApi(creds.access_token);

    // On auth failure, attempt a token refresh and retry once before giving up.
    if (resp.status === 401 || resp.status === 403) {
      const refreshed = await refreshGeminiToken(credsPath, creds);
      if (refreshed.error) return { ...baseInfo, error: 'Session expired. Run `gemini auth` to re-auth.' };
      creds = refreshed.creds;
      resp = await callQuotaApi(creds.access_token);
    }

    if (!resp.ok) {
      if (resp.status === 401 || resp.status === 403) {
        return { ...baseInfo, error: 'Session expired. Run `gemini auth` to re-auth.' };
      }
      return { ...baseInfo, error: `API error (HTTP ${resp.status})` };
    }
    
    const data = await resp.json();
    const metrics = [];
    
    // Parse quota buckets (API returns 'buckets' with 'remainingFraction')
    const buckets = data.buckets || data.quotaBuckets || [];
    
    // Track all non-Vertex Gemini request buckets instead of a hardcoded
    // 2.x allowlist so new Gemini CLI quota windows surface automatically.
    const seen = new Set();
    
    for (const bucket of buckets) {
      if (bucket.tokenType !== 'REQUESTS') continue;
      // Skip vertex variants
      if (bucket.modelId?.includes('_vertex')) continue;
      // Only show Gemini model buckets
      if (!bucket.modelId?.startsWith('gemini-')) continue;
      // Dedupe
      if (seen.has(bucket.modelId)) continue;
      seen.add(bucket.modelId);
      
      const remaining = bucket.remainingFraction ?? 1;
      metrics.push({
        label: bucket.modelId || 'Quota',
        used: Math.round((1 - remaining) * 100),
        limit: 100,
        format: 'percent',
        resetTime: bucket.resetTime,
      });
    }
    
    metrics.sort((a, b) => String(a.label || '').localeCompare(String(b.label || '')));

    return {
      ...baseInfo,
      plan: 'Gemini CLI',
      metrics,
    };
  } catch (e) {
    return { ...baseInfo, error: 'Network error: ' + e.message };
  }
}

// Fetch Amp usage
async function fetchAmpUsage() {
  const baseInfo = {
    provider: 'amp',
    name: AI_PROVIDERS.amp.name,
    icon: AI_PROVIDERS.amp.icon,
  };
  
  const secretsPath = AI_PROVIDERS.amp.credPaths[0];
  if (!fs.existsSync(secretsPath)) {
    return { ...baseInfo, error: 'Amp not installed. Install Amp Code to get started.' };
  }
  
  let secrets;
  try {
    secrets = JSON.parse(fs.readFileSync(secretsPath, 'utf8'));
  } catch (e) {
    return { ...baseInfo, error: 'Invalid secrets file.' };
  }
  
  const apiKey = secrets['apiKey@https://ampcode.com/'];
  if (!apiKey) {
    return { ...baseInfo, error: 'Not logged in. Sign in to Amp Code.' };
  }
  
  try {
    const resp = await fetch('https://ampcode.com/api/internal', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ method: 'userDisplayBalanceInfo', params: {} }),
    });
    
    if (!resp.ok) {
      if (resp.status === 401 || resp.status === 403) {
        return { ...baseInfo, error: 'Session expired. Re-authenticate in Amp Code.' };
      }
      return { ...baseInfo, error: `API error (HTTP ${resp.status})` };
    }
    
    const data = await resp.json();
    const metrics = [];
    
    // Parse displayText for usage info
    const displayText = data.result?.displayText || data.displayText || '';
    
    // Free tier: "$X/$Y remaining"
    const freeMatch = displayText.match(/\$(\d+(?:\.\d+)?)\s*\/\s*\$(\d+(?:\.\d+)?)\s+remaining/i);
    if (freeMatch) {
      const remaining = parseFloat(freeMatch[1]);
      const total = parseFloat(freeMatch[2]);
      const used = total - remaining;
      metrics.push({
        label: 'Free',
        used: (used / total) * 100,
        limit: 100,
        format: 'percent',
      });
    }
    
    // Credits: "Individual credits: $X remaining"
    const creditsMatch = displayText.match(/Individual credits:\s*\$(\d+(?:\.\d+)?)/i);
    if (creditsMatch) {
      metrics.push({
        label: 'Credits',
        used: null,
        remaining: parseFloat(creditsMatch[1]),
        format: 'dollars',
      });
    }
    
    return {
      ...baseInfo,
      plan: freeMatch ? 'Free' : (creditsMatch ? 'Credits' : 'unknown'),
      metrics,
    };
  } catch (e) {
    return { ...baseInfo, error: 'Network error: ' + e.message };
  }
}

// Fetch Factory (Droid) usage
async function fetchFactoryUsage() {
  const baseInfo = { provider: 'factory', name: AI_PROVIDERS.factory.name, icon: AI_PROVIDERS.factory.icon };
  const authPath = AI_PROVIDERS.factory.credPaths[0];
  
  if (!fs.existsSync(authPath)) {
    return { ...baseInfo, error: 'Not logged in. Run `droid` to authenticate.' };
  }
  
  let auth;
  try { auth = JSON.parse(fs.readFileSync(authPath, 'utf8')); } 
  catch (e) { return { ...baseInfo, error: 'Invalid auth file.' }; }
  
  if (!auth.access_token) return { ...baseInfo, error: 'No access token found.' };
  
  try {
    const resp = await fetch('https://api.factory.ai/api/organization/subscription/usage', {
      method: 'POST',
      headers: { 'Authorization': `Bearer ${auth.access_token}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({ useCache: true }),
    });
    
    if (!resp.ok) {
      if (resp.status === 401 || resp.status === 403) return { ...baseInfo, error: 'Session expired. Run `droid` to re-auth.' };
      return { ...baseInfo, error: `API error (HTTP ${resp.status})` };
    }
    
    const data = await resp.json();
    const metrics = [];
    
    if (data.usage?.standard) {
      const s = data.usage.standard;
      metrics.push({ label: 'Standard', used: (s.usedRatio || 0) * 100, limit: 100, format: 'percent' });
    }
    if (data.usage?.premium?.totalAllowance > 0) {
      const p = data.usage.premium;
      metrics.push({ label: 'Premium', used: (p.usedRatio || 0) * 100, limit: 100, format: 'percent' });
    }
    
    const allowance = data.usage?.standard?.totalAllowance || 0;
    const plan = allowance >= 200000000 ? 'Max' : allowance >= 20000000 ? 'Pro' : 'Basic';
    
    return { ...baseInfo, plan, metrics };
  } catch (e) { return { ...baseInfo, error: 'Network error: ' + e.message }; }
}

// Fetch Kimi Code usage
async function fetchKimiUsage() {
  const baseInfo = { provider: 'kimi', name: AI_PROVIDERS.kimi.name, icon: AI_PROVIDERS.kimi.icon };
  const credPath = AI_PROVIDERS.kimi.credPaths[0];
  
  if (!fs.existsSync(credPath)) {
    return { ...baseInfo, error: 'Not logged in. Run `kimi login` first.' };
  }
  
  let creds;
  try { creds = JSON.parse(fs.readFileSync(credPath, 'utf8')); }
  catch (e) { return { ...baseInfo, error: 'Invalid credentials file.' }; }
  
  if (!creds.access_token) return { ...baseInfo, error: 'No access token found.' };
  
  try {
    const resp = await fetch('https://api.kimi.com/coding/v1/usages', {
      headers: { 'Authorization': `Bearer ${creds.access_token}`, 'Accept': 'application/json' },
    });
    
    if (!resp.ok) {
      if (resp.status === 401 || resp.status === 403) return { ...baseInfo, error: 'Session expired. Run `kimi login` to re-auth.' };
      return { ...baseInfo, error: `API error (HTTP ${resp.status})` };
    }
    
    const data = await resp.json();
    const metrics = [];
    
    if (data.usage) {
      const used = parseInt(data.usage.limit) - parseInt(data.usage.remaining);
      const total = parseInt(data.usage.limit);
      metrics.push({ label: 'Session', used: (used / total) * 100, limit: 100, format: 'percent', resetsAt: data.usage.resetTime });
    }
    
    const plan = data.user?.membership?.level?.replace('LEVEL_', '') || 'unknown';
    return { ...baseInfo, plan, metrics };
  } catch (e) { return { ...baseInfo, error: 'Network error: ' + e.message }; }
}

// Fetch JetBrains AI usage
async function fetchJetbrainsUsage() {
  const baseInfo = { provider: 'jetbrains', name: AI_PROVIDERS.jetbrains.name, icon: AI_PROVIDERS.jetbrains.icon };
  const configDir = AI_PROVIDERS.jetbrains.configDirs[0];
  
  if (!fs.existsSync(configDir)) {
    return { ...baseInfo, error: 'JetBrains IDE not detected.' };
  }
  
  // Find latest IDE config with quota file
  let quotaData = null;
  try {
    const dirs = fs.readdirSync(configDir).filter(d => !d.startsWith('.'));
    for (const dir of dirs.sort().reverse()) {
      const quotaPath = path.join(configDir, dir, 'options', 'AIAssistantQuotaManager2.xml');
      if (fs.existsSync(quotaPath)) {
        const content = fs.readFileSync(quotaPath, 'utf8');
        // Simple XML parsing for quota values
        const currentMatch = content.match(/<option name="current" value="(\d+)"/);
        const maxMatch = content.match(/<option name="maximum" value="(\d+)"/);
        if (currentMatch && maxMatch) {
          quotaData = { current: parseInt(currentMatch[1]), maximum: parseInt(maxMatch[1]) };
          break;
        }
      }
    }
  } catch (e) { /* ignore */ }
  
  if (!quotaData) {
    return { ...baseInfo, error: 'JetBrains AI quota not found. Open AI Assistant in IDE.' };
  }
  
  const used = (quotaData.current / quotaData.maximum) * 100;
  return { ...baseInfo, plan: 'AI Assistant', metrics: [{ label: 'Quota', used, limit: 100, format: 'percent' }] };
}

// Fetch MiniMax usage
async function fetchMinimaxUsage() {
  const baseInfo = { provider: 'minimax', name: AI_PROVIDERS.minimax.name, icon: AI_PROVIDERS.minimax.icon };
  
  const apiKey = process.env.MINIMAX_API_KEY || process.env.MINIMAX_CN_API_KEY || process.env.MINIMAX_API_TOKEN;
  if (!apiKey) {
    return { ...baseInfo, error: 'Set MINIMAX_API_KEY environment variable.' };
  }
  
  try {
    const resp = await fetch('https://api.minimax.io/v1/api/openplatform/coding_plan/remains', {
      headers: { 'Authorization': `Bearer ${apiKey}`, 'Accept': 'application/json' },
    });
    
    if (!resp.ok) {
      if (resp.status === 401 || resp.status === 403) return { ...baseInfo, error: 'Invalid API key.' };
      return { ...baseInfo, error: `API error (HTTP ${resp.status})` };
    }
    
    const data = await resp.json();
    if (data.base_resp?.status_code !== 0) {
      return { ...baseInfo, error: data.base_resp?.status_msg || 'API error' };
    }
    
    const metrics = [];
    const model = data.model_remains?.[0];
    if (model) {
      const total = model.current_interval_total_count || 100;
      const remaining = model.current_interval_usage_count || model.current_interval_remaining_count || 0;
      const used = ((total - remaining) / total) * 100;
      metrics.push({ label: 'Session', used, limit: 100, format: 'percent' });
    }
    
    return { ...baseInfo, plan: data.current_subscribe_title || 'MiniMax', metrics };
  } catch (e) { return { ...baseInfo, error: 'Network error: ' + e.message }; }
}

// Fetch Z.ai usage
async function fetchZaiUsage() {
  const baseInfo = { provider: 'zai', name: AI_PROVIDERS.zai.name, icon: AI_PROVIDERS.zai.icon };
  
  const apiKey = process.env.ZAI_API_KEY || process.env.GLM_API_KEY;
  if (!apiKey) {
    return { ...baseInfo, error: 'Set ZAI_API_KEY environment variable.' };
  }
  
  try {
    const resp = await fetch('https://api.z.ai/api/monitor/usage/quota/limit', {
      headers: { 'Authorization': `Bearer ${apiKey}`, 'Accept': 'application/json' },
    });
    
    if (!resp.ok) {
      if (resp.status === 401 || resp.status === 403) return { ...baseInfo, error: 'Invalid API key.' };
      return { ...baseInfo, error: `API error (HTTP ${resp.status})` };
    }
    
    const data = await resp.json();
    if (data.code !== 200) {
      return { ...baseInfo, error: data.message || 'API error' };
    }
    
    const metrics = [];
    for (const limit of (data.data?.limits || [])) {
      if (limit.type === 'TOKENS_LIMIT') {
        metrics.push({ label: 'Session', used: limit.percentage || 0, limit: 100, format: 'percent' });
      } else if (limit.type === 'TIME_LIMIT') {
        metrics.push({ label: 'Weekly', used: limit.percentage || 0, limit: 100, format: 'percent' });
      }
    }
    
    return { ...baseInfo, plan: 'GLM Coding', metrics };
  } catch (e) { return { ...baseInfo, error: 'Network error: ' + e.message }; }
}

async function fetchAntigravityUsage() {
  const baseInfo = { provider: 'antigravity', name: AI_PROVIDERS.antigravity.name, icon: AI_PROVIDERS.antigravity.icon };
  const config = AI_PROVIDERS.antigravity;
  
  // Read config to get active account
  let activeAccount;
  try {
    const configData = JSON.parse(fs.readFileSync(config.configPath, 'utf8'));
    activeAccount = configData.activeAccount;
  } catch (_) {
    return { ...baseInfo, error: 'Run: antigravity-usage login' };
  }
  
  if (!activeAccount) {
    return { ...baseInfo, error: 'No active account configured.' };
  }
  
  // Read tokens for active account
  const tokensPath = path.join(config.accountsDir, activeAccount, 'tokens.json');
  let tokens;
  try {
    tokens = JSON.parse(fs.readFileSync(tokensPath, 'utf8'));
  } catch (_) {
    return { ...baseInfo, error: 'Token file not found for ' + activeAccount };
  }
  
  // Refresh token if expired
  let accessToken = tokens.accessToken;
  if (tokens.expiresAt && Date.now() > tokens.expiresAt - 60000) {
    // Need OAuth credentials from env vars for token refresh
    const clientId = process.env.ANTIGRAVITY_CLIENT_ID;
    const clientSecret = process.env.ANTIGRAVITY_CLIENT_SECRET;
    
    if (!clientId || !clientSecret) {
      return { ...baseInfo, error: 'Token expired. Run `antigravity-usage` to refresh, or set ANTIGRAVITY_CLIENT_ID/SECRET env vars.' };
    }
    
    try {
      const refreshResp = await fetch(config.tokenUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({
          client_id: clientId,
          client_secret: clientSecret,
          refresh_token: tokens.refreshToken,
          grant_type: 'refresh_token',
        }),
      });
      if (!refreshResp.ok) {
        return { ...baseInfo, error: 'Token refresh failed (HTTP ' + refreshResp.status + ')' };
      }
      const refreshData = await refreshResp.json();
      accessToken = refreshData.access_token;
      // Update stored tokens
      tokens.accessToken = accessToken;
      tokens.expiresAt = Date.now() + (refreshData.expires_in * 1000);
      try { fs.writeFileSync(tokensPath, JSON.stringify(tokens, null, 2)); } catch (_) {}
    } catch (e) {
      return { ...baseInfo, error: 'Token refresh error: ' + e.message };
    }
  }
  
  // Fetch available models with quota info
  try {
    const resp = await fetch(config.apiUrl, {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer ' + accessToken,
        'Content-Type': 'application/json',
        'User-Agent': 'antigravity',
      },
      body: JSON.stringify({ project: tokens.projectId }),
    });
    
    if (!resp.ok) {
      if (resp.status === 401 || resp.status === 403) return { ...baseInfo, error: 'Auth failed. Re-run: antigravity-usage login' };
      if (resp.status === 429) return { ...baseInfo, error: 'Rate limited. Try again later.' };
      return { ...baseInfo, error: 'API error (HTTP ' + resp.status + ')' };
    }
    
    const data = await resp.json();
    const models = data.models || {};
    
    // Build metrics from model quotas
    const metrics = [];
    const interestingModels = ['gemini-3-pro-high', 'gemini-3-pro-low', 'claude-sonnet-4-6', 'claude-opus-4-6-thinking'];
    
    for (const modelId of interestingModels) {
      const model = models[modelId];
      if (model && model.quotaInfo) {
        const remaining = model.quotaInfo.remainingFraction ?? 1;
        metrics.push({
          label: model.displayName || modelId,
          used: Math.round((1 - remaining) * 100),
          limit: 100,
          format: 'percent',
          resetTime: model.quotaInfo.resetTime,
        });
      }
    }
    
    // If no interesting models found, show first few available
    if (metrics.length === 0) {
      for (const [modelId, model] of Object.entries(models).slice(0, 4)) {
        if (model.quotaInfo) {
          const remaining = model.quotaInfo.remainingFraction ?? 1;
          metrics.push({
            label: model.displayName || modelId,
            used: Math.round((1 - remaining) * 100),
            limit: 100,
            format: 'percent',
          });
        }
      }
    }
    
    return { ...baseInfo, plan: activeAccount, metrics };
  } catch (e) {
    return { ...baseInfo, error: 'Network error: ' + e.message };
  }
}

// Cache for AI usage data (avoid 429 rate limits)
// In-memory cache
const aiUsageCache = {
  claude: { data: null, timestamp: 0 },
  codex: { data: null, timestamp: 0 },
  copilot: { data: null, timestamp: 0 },
  cursor: { data: null, timestamp: 0 },
  gemini: { data: null, timestamp: 0 },
  factory: { data: null, timestamp: 0 },
  kimi: { data: null, timestamp: 0 },
  jetbrains: { data: null, timestamp: 0 },
  minimax: { data: null, timestamp: 0 },
  zai: { data: null, timestamp: 0 },
  amp: { data: null, timestamp: 0 },
  antigravity: { data: null, timestamp: 0 },
};
const AI_CACHE_TTL_MS = 300000; // 5 minutes cache

// Persistent file cache (survives restarts)
const AI_CACHE_FILE = path.join(CWD, 'data', 'ai-usage-cache.json');

function loadPersistentCache() {
  try {
    if (fs.existsSync(AI_CACHE_FILE)) {
      const data = JSON.parse(fs.readFileSync(AI_CACHE_FILE, 'utf8'));
      for (const [provider, entry] of Object.entries(data)) {
        if (aiUsageCache[provider] && entry.data) {
          aiUsageCache[provider] = entry;
        }
      }
      console.log('[AI Cache] Loaded persistent cache');
    }
  } catch (e) { /* ignore */ }
}

function savePersistentCache() {
  try {
    fs.mkdirSync(path.dirname(AI_CACHE_FILE), { recursive: true });
    fs.writeFileSync(AI_CACHE_FILE, JSON.stringify(aiUsageCache, null, 2));
  } catch (e) { /* ignore */ }
}

// Load cache on startup
loadPersistentCache();

// Cached fetch wrapper
async function fetchWithCache(provider, fetchFn) {
  const cache = aiUsageCache[provider];
  const now = Date.now();
  
  // Return cached data if fresh
  if (cache.data && (now - cache.timestamp) < AI_CACHE_TTL_MS) {
    return { ...cache.data, cached: true };
  }
  
  // Fetch fresh data
  const result = await fetchFn();
  
  // Only cache successful results (not errors)
  if (!result.error) {
    cache.data = result;
    cache.timestamp = now;
    savePersistentCache(); // Persist to disk
  } else if (result.error.includes('429') || result.error.includes('rate')) {
    // On rate limit, return stale cache if available
    if (cache.data) {
      return { ...cache.data, cached: true, stale: true, rateLimited: true };
    }
  }
  
  return result;
}

// Get all AI usage data
async function getAllAiUsage(options = {}) {
  const results = await Promise.all([
    fetchWithCache('claude', fetchClaudeUsage),
    fetchWithCache('codex', fetchCodexUsage),
    fetchWithCache('copilot', fetchCopilotUsage),
    fetchWithCache('cursor', fetchCursorUsage),
    fetchWithCache('gemini', fetchGeminiUsage),
    fetchWithCache('amp', fetchAmpUsage),
    fetchWithCache('factory', fetchFactoryUsage),
    fetchWithCache('kimi', fetchKimiUsage),
    fetchWithCache('jetbrains', fetchJetbrainsUsage),
    fetchWithCache('minimax', fetchMinimaxUsage),
    fetchWithCache('zai', fetchZaiUsage),
    fetchWithCache('antigravity', fetchAntigravityUsage),
  ]);
  
  return {
    providers: results,
    timestamp: new Date().toISOString(),
  };
}

// GET /api/latest-image?dir=<path> - newest image from a directory
function latestImageHandler(parsedUrl, res) {
  const dir = parsedUrl.searchParams.get('dir');
  if (!dir) return sendResponse(res, 200, 'application/json', JSON.stringify({ status: 'error', message: 'Missing dir parameter' }));
  const resolved = path.resolve(dir.replace(/^~/, os.homedir()));
  const home = os.homedir();
  if (!resolved.startsWith(home + path.sep) && resolved !== home) {
    return sendResponse(res, 200, 'application/json', JSON.stringify({ status: 'error', message: 'Directory must be under home' }));
  }
  try {
    const imageExts = ['.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp', '.svg'];
    const files = fs.readdirSync(resolved)
      .filter(f => imageExts.includes(path.extname(f).toLowerCase()))
      .map(f => ({ name: f, mtime: fs.statSync(path.join(resolved, f)).mtimeMs }))
      .sort((a, b) => b.mtime - a.mtime);
    if (files.length === 0) return sendResponse(res, 200, 'application/json', JSON.stringify({ status: 'ok', image: null, message: 'No images found' }));
    const latest = files[0];
    const ext = path.extname(latest.name).toLowerCase().replace('.', '');
    const mime = ext === 'svg' ? 'image/svg+xml' : ext === 'jpg' ? 'image/jpeg' : `image/${ext}`;
    const data = fs.readFileSync(path.join(resolved, latest.name));
    const b64 = data.toString('base64');
    return sendResponse(res, 200, 'application/json', JSON.stringify({ status: 'ok', image: { name: latest.name, mtime: latest.mtime, dataUrl: `data:${mime};base64,${b64}` }, total: files.length }));
  } catch (error) { 
    return sendResponse(res, 200, 'application/json', JSON.stringify({ status: 'error', message: error.message })); 
  }
}

const server = http.createServer(async (req, res) => {
  const parsedUrl = new URL(req.url, `http://${req.headers.host}`);
  const pathname = parsedUrl.pathname;

  // ── Auth: serve login page (always accessible) ──
  if (req.method === 'GET' && pathname === '/login') {
    const loginPath = path.join(__dirname, 'login.html');
    fs.readFile(loginPath, (err, data) => {
      if (err) { sendResponse(res, 404, 'text/plain', 'Login page not found'); return; }
      sendResponse(res, 200, 'text/html', data);
    });
    return;
  }

  // ── Auth: login action ──
  if (req.method === 'POST' && pathname === '/api/auth/login') {
    if (!DASHBOARD_PASSWORD) {
      sendJson(res, 200, { status: 'ok', redirect: '/' });
      return;
    }
    const ip = req.socket.remoteAddress || 'unknown';
    if (isRateLimited(ip)) {
      sendJson(res, 429, { error: 'Too many failed attempts. Try again in 15 minutes.' });
      return;
    }
    let body = '';
    req.on('data', c => { body += c; if (body.length > 4096) req.destroy(); });
    req.on('end', () => {
      try {
        const { password } = JSON.parse(body);
        if (checkPassword(password)) {
          const token = createSession();
          const cookieOpts = `Path=/; HttpOnly; SameSite=Strict; Max-Age=${SESSION_TTL_MS / 1000}`;
          res.writeHead(200, {
            'Content-Type': 'application/json',
            'Set-Cookie': `lb_session=${token}; ${cookieOpts}`
          });
          res.end(JSON.stringify({ status: 'ok', redirect: '/' }));
        } else {
          recordFailedAttempt(ip);
          sendJson(res, 401, { error: 'Invalid password' });
        }
      } catch (e) {
        sendJson(res, 400, { error: 'Invalid request' });
      }
    });
    return;
  }

  // ── Auth: logout ──
  if (req.method === 'POST' && pathname === '/api/auth/logout') {
    const token = getSessionCookie(req);
    if (token) sessions.delete(token);
    res.writeHead(302, {
      'Set-Cookie': 'lb_session=; Path=/; HttpOnly; SameSite=Strict; Max-Age=0',
      'Location': '/login'
    });
    res.end();
    return;
  }

  // ── Auth: enforce session for all other routes ──
  if (DASHBOARD_PASSWORD) {
    const token = getSessionCookie(req);
    if (!isValidSession(token)) {
      if (pathname.startsWith('/api/')) {
        sendJson(res, 401, { status: 'error', message: 'Not authenticated' });
      } else {
        res.writeHead(302, { 'Location': '/login' });
        res.end();
      }
      return;
    }
  }

  // CORS preflight for /config
  if (req.method === 'OPTIONS' && pathname === '/config') {
    res.writeHead(204, {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type'
    });
    res.end();
    return;
  }

  // ─────────────────────────────────────────────
  // Server Profiles API (for remote LobsterBoard Agent connections)
  // ─────────────────────────────────────────────
  const SERVERS_FILE = path.join(CWD, 'data', 'servers.json');
  
  function loadServers() {
    try {
      if (fs.existsSync(SERVERS_FILE)) {
        return JSON.parse(fs.readFileSync(SERVERS_FILE, 'utf8'));
      }
    } catch (e) { /* ignore */ }
    return [{ id: 'local', name: 'Local', type: 'local' }];
  }
  
  function saveServers(servers) {
    fs.mkdirSync(path.dirname(SERVERS_FILE), { recursive: true });
    fs.writeFileSync(SERVERS_FILE, JSON.stringify(servers, null, 2));
  }

  // GET /api/servers - List all servers
  if (req.method === 'GET' && pathname === '/api/servers') {
    const servers = loadServers();
    // Mask API keys and secrets for security
    const masked = servers.map(s => ({
      ...s,
      apiKey: s.apiKey ? s.apiKey.slice(0, 10) + '...' : undefined,
      sharedSecret: s.sharedSecret ? '🔐' : undefined, // Just indicate presence
    }));
    sendJson(res, 200, { servers: masked });
    return;
  }

  // POST /api/servers - Add a server
  if (req.method === 'POST' && pathname === '/api/servers') {
    let body = '';
    req.on('data', c => body += c);
    req.on('end', async () => {
      try {
        const { name, url, apiKey } = JSON.parse(body);
        if (!name || !url || !apiKey) {
          return sendJson(res, 400, { error: 'name, url, and apiKey required' });
        }
        const servers = loadServers();
        const id = name.toLowerCase().replace(/[^a-z0-9]+/g, '-');
        if (servers.find(s => s.id === id)) {
          return sendJson(res, 400, { error: 'Server with this name already exists' });
        }
        
        // Generate ECDH key pair for encrypted communication
        const keyPair = generateEcdhKeyPair();
        
        // Perform handshake with agent
        let sharedSecret = null;
        let encrypted = false;
        try {
          const handshakeRes = await fetch(url + '/handshake', {
            method: 'POST',
            headers: { 
              'X-API-Key': apiKey,
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 
              clientId: id, 
              publicKey: keyPair.publicKey,
            }),
            signal: AbortSignal.timeout(10000),
          });
          
          if (handshakeRes.ok) {
            const handshakeData = await handshakeRes.json();
            if (handshakeData.publicKey) {
              sharedSecret = deriveSharedSecret(keyPair.privateKey, handshakeData.publicKey);
              encrypted = true;
              console.log(`🔐 Encrypted connection established with server: ${name}`);
            }
          }
        } catch (e) {
          // Handshake failed - agent may not support encryption, continue without it
          console.log(`⚠️ Handshake failed for ${name}, using unencrypted: ${e.message}`);
        }
        
        const serverEntry = { 
          id, 
          name, 
          url, 
          apiKey, 
          type: 'remote',
          encrypted,
        };
        
        // Store shared secret (base64 encoded) if encryption is enabled
        if (sharedSecret) {
          serverEntry.sharedSecret = sharedSecret.toString('base64');
          serverEntry.clientId = id;
        }
        
        servers.push(serverEntry);
        saveServers(servers);
        sendJson(res, 200, { status: 'success', id, encrypted });
      } catch (e) {
        sendJson(res, 400, { error: e.message });
      }
    });
    return;
  }

  // PUT /api/servers/:id - Update a server
  if (req.method === 'PUT' && pathname.startsWith('/api/servers/')) {
    const id = pathname.split('/')[3];
    let body = '';
    req.on('data', c => body += c);
    req.on('end', () => {
      try {
        const updates = JSON.parse(body);
        const servers = loadServers();
        const idx = servers.findIndex(s => s.id === id);
        if (idx === -1) return sendJson(res, 404, { error: 'Server not found' });
        if (id === 'local') return sendJson(res, 400, { error: 'Cannot modify local server' });
        servers[idx] = { ...servers[idx], ...updates, id }; // Don't allow id change
        saveServers(servers);
        sendJson(res, 200, { status: 'success' });
      } catch (e) {
        sendJson(res, 400, { error: e.message });
      }
    });
    return;
  }

  // DELETE /api/servers/:id - Delete a server
  if (req.method === 'DELETE' && pathname.startsWith('/api/servers/')) {
    const id = pathname.split('/')[3];
    if (id === 'local') return sendJson(res, 400, { error: 'Cannot delete local server' });
    const servers = loadServers();
    const filtered = servers.filter(s => s.id !== id);
    if (filtered.length === servers.length) {
      return sendJson(res, 404, { error: 'Server not found' });
    }
    saveServers(filtered);
    sendJson(res, 200, { status: 'success' });
    return;
  }

  // POST /api/servers/:id/test - Test connection to a server
  if (req.method === 'POST' && pathname.match(/^\/api\/servers\/[^/]+\/test$/)) {
    const id = pathname.split('/')[3];
    const servers = loadServers();
    const server = servers.find(s => s.id === id);
    if (!server) return sendJson(res, 404, { error: 'Server not found' });
    if (server.type === 'local') {
      return sendJson(res, 200, { status: 'ok', message: 'Local server' });
    }
    // Test remote connection
    fetch(server.url + '/health', {
      headers: { 'X-API-Key': server.apiKey },
      signal: AbortSignal.timeout(5000),
    })
      .then(r => r.json())
      .then(data => sendJson(res, 200, { 
        status: 'ok', 
        serverName: data.serverName,
        agentEncryption: data.encrypted || false,
        localEncryption: server.encrypted || false,
      }))
      .catch(e => sendJson(res, 200, { status: 'error', message: e.message }));
    return;
  }

  // POST /api/servers/:id/handshake - Re-establish encryption with a server
  if (req.method === 'POST' && pathname.match(/^\/api\/servers\/[^/]+\/handshake$/)) {
    const id = pathname.split('/')[3];
    const servers = loadServers();
    const serverIdx = servers.findIndex(s => s.id === id);
    if (serverIdx === -1) return sendJson(res, 404, { error: 'Server not found' });
    const server = servers[serverIdx];
    if (server.type === 'local') {
      return sendJson(res, 400, { error: 'Local server does not need handshake' });
    }

    (async () => {
      try {
        // Generate new key pair
        const keyPair = generateEcdhKeyPair();
        
        const handshakeRes = await fetch(server.url + '/handshake', {
          method: 'POST',
          headers: { 
            'X-API-Key': server.apiKey,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ 
            clientId: id, 
            publicKey: keyPair.publicKey,
          }),
          signal: AbortSignal.timeout(10000),
        });
        
        if (!handshakeRes.ok) {
          const err = await handshakeRes.json().catch(() => ({ error: 'HTTP ' + handshakeRes.status }));
          return sendJson(res, 500, { error: err.error || 'Handshake failed' });
        }
        
        const handshakeData = await handshakeRes.json();
        if (!handshakeData.publicKey) {
          return sendJson(res, 500, { error: 'Agent did not return public key' });
        }
        
        const sharedSecret = deriveSharedSecret(keyPair.privateKey, handshakeData.publicKey);
        
        // Update server config
        servers[serverIdx].encrypted = true;
        servers[serverIdx].sharedSecret = sharedSecret.toString('base64');
        servers[serverIdx].clientId = id;
        saveServers(servers);
        
        console.log(`🔐 Re-established encrypted connection with server: ${server.name}`);
        sendJson(res, 200, { status: 'ok', encrypted: true });
      } catch (e) {
        sendJson(res, 500, { error: e.message });
      }
    })();
    return;
  }

  // GET /api/servers/:id/stats - Fetch stats from a remote server
  if (req.method === 'GET' && pathname.match(/^\/api\/servers\/[^/]+\/stats$/)) {
    const id = pathname.split('/')[3];
    const servers = loadServers();
    const server = servers.find(s => s.id === id);
    if (!server) return sendJson(res, 404, { error: 'Server not found' });
    if (server.type === 'local') {
      return sendJson(res, 400, { error: 'Use /api/stats/stream for local' });
    }
    
    // Build headers - include client ID if we have encryption set up
    const headers = { 'X-API-Key': server.apiKey };
    if (server.encrypted && server.clientId) {
      headers['X-Client-ID'] = server.clientId;
    }
    
    // Fetch from remote agent
    fetch(server.url + '/stats', {
      headers,
      signal: AbortSignal.timeout(10000),
    })
      .then(r => {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        return r.json();
      })
      .then(data => {
        // Decrypt if response is encrypted
        if (data.encrypted && server.sharedSecret) {
          try {
            const keyBuffer = Buffer.from(server.sharedSecret, 'base64');
            const decrypted = decryptPayload(data.encrypted, keyBuffer);
            decrypted._remote = true;
            decrypted._encrypted = true;
            return sendJson(res, 200, decrypted);
          } catch (e) {
            console.error('Decryption failed:', e.message);
            return sendJson(res, 500, { error: 'Decryption failed: ' + e.message });
          }
        }
        // Plain response (backward compatible)
        data._remote = true;
        sendJson(res, 200, data);
      })
      .catch(e => sendJson(res, 500, { error: e.message }));
    return;
  }

  // GET /config - Load dashboard configuration
  if (req.method === 'GET' && pathname === '/config') {
    fs.readFile(CONFIG_FILE, 'utf8', (err, data) => {
      if (err) {
        if (err.code === 'ENOENT') {
          // If config.json doesn't exist, return empty config
          sendJson(res, 200, { canvas: { width: 1920, height: 1080 }, widgets: [] });
        } else {
          sendError(res, `Failed to read config file: ${err.message}`);
        }
        return;
      }
      try {
        const config = JSON.parse(data);
        sendJson(res, 200, maskConfig(config));
      } catch (parseErr) {
        sendError(res, `Failed to parse config file: ${parseErr.message}`);
      }
    });
    return;
  }

  // POST /config - Save dashboard configuration
  if (req.method === 'POST' && pathname === '/config') {
    const MAX_BODY = 1024 * 1024; // 1 MB limit
    let body = '';
    let overflow = false;
    req.on('data', chunk => {
      body += chunk.toString();
      if (body.length > MAX_BODY) { overflow = true; req.destroy(); }
    });
    req.on('end', () => {
      if (overflow) { sendError(res, 'Request body too large', 413); return; }
      try {
        let config = JSON.parse(body);
        config = extractSecrets(config);
        fs.writeFile(CONFIG_FILE, JSON.stringify(config, null, 2), 'utf8', (err) => {
          if (err) {
            sendError(res, `Failed to write config file: ${err.message}`);
            return;
          }
          sendJson(res, 200, { status: 'success', message: 'Config saved' });
        });
      } catch (parseErr) {
        sendError(res, `Invalid JSON in request body: ${parseErr.message}`, 400);
      }
    });
    return;
  }

  // CORS preflight for /api/*
  if (req.method === 'OPTIONS' && (pathname.startsWith('/api/') || pathname === '/api/pages')) {
    res.writeHead(204, {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PATCH, DELETE, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type'
    });
    res.end();
    return;
  }

  // ── Security: PIN auth endpoints ──
  if (req.method === 'GET' && pathname === '/api/auth/status') {
    const auth = getAuth();
    sendJson(res, 200, { hasPin: !!auth.pinHash, publicMode: !!auth.publicMode });
    return;
  }

  if (req.method === 'POST' && pathname === '/api/auth/set-pin') {
    let body = '';
    req.on('data', c => body += c);
    req.on('end', () => {
      try {
        const { pin, currentPin } = JSON.parse(body);
        if (!pin || pin.length < 4 || pin.length > 6 || !/^\d+$/.test(pin)) {
          sendJson(res, 400, { error: 'PIN must be 4-6 digits' }); return;
        }
        const auth = getAuth();
        // If PIN already set, require current PIN
        if (auth.pinHash && (!currentPin || hashPin(currentPin) !== auth.pinHash)) {
          sendJson(res, 403, { error: 'Current PIN is incorrect' }); return;
        }
        auth.pinHash = hashPin(pin);
        writeJsonFile(AUTH_FILE, auth);
        sendJson(res, 200, { status: 'ok' });
      } catch (e) { sendError(res, e.message, 400); }
    });
    return;
  }

  if (req.method === 'POST' && pathname === '/api/auth/verify-pin') {
    let body = '';
    req.on('data', c => body += c);
    req.on('end', () => {
      try {
        const { pin } = JSON.parse(body);
        const auth = getAuth();
        if (!auth.pinHash) { sendJson(res, 200, { valid: true }); return; }
        const valid = hashPin(pin) === auth.pinHash;
        sendJson(res, 200, { valid });
      } catch (e) { sendError(res, e.message, 400); }
    });
    return;
  }

  if (req.method === 'POST' && pathname === '/api/auth/remove-pin') {
    let body = '';
    req.on('data', c => body += c);
    req.on('end', () => {
      try {
        const { pin } = JSON.parse(body);
        const auth = getAuth();
        if (auth.pinHash && hashPin(pin) !== auth.pinHash) {
          sendJson(res, 403, { error: 'PIN is incorrect' }); return;
        }
        delete auth.pinHash;
        writeJsonFile(AUTH_FILE, auth);
        sendJson(res, 200, { status: 'ok' });
      } catch (e) { sendError(res, e.message, 400); }
    });
    return;
  }

  // ── Security: Public mode ──
  if (req.method === 'GET' && pathname === '/api/mode') {
    const auth = getAuth();
    sendJson(res, 200, { publicMode: !!auth.publicMode });
    return;
  }

  if (req.method === 'POST' && pathname === '/api/mode') {
    let body = '';
    req.on('data', c => body += c);
    req.on('end', () => {
      try {
        const { publicMode, pin } = JSON.parse(body);
        const auth = getAuth();
        // Require PIN to toggle mode if PIN is set
        if (auth.pinHash && (!pin || hashPin(pin) !== auth.pinHash)) {
          sendJson(res, 403, { error: 'PIN required' }); return;
        }
        auth.publicMode = !!publicMode;
        writeJsonFile(AUTH_FILE, auth);
        sendJson(res, 200, { status: 'ok', publicMode: auth.publicMode });
      } catch (e) { sendError(res, e.message, 400); }
    });
    return;
  }

  // ── Security: Secrets management ──
  if (req.method === 'POST' && pathname.match(/^\/api\/secrets\/[^/]+$/)) {
    if (isPublicMode()) { sendJson(res, 403, { error: 'Forbidden in public mode' }); return; }
    const widgetId = pathname.split('/')[3];
    let body = '';
    req.on('data', c => body += c);
    req.on('end', () => {
      try {
        const updates = JSON.parse(body);
        const secrets = getSecrets();
        if (!secrets[widgetId]) secrets[widgetId] = {};
        Object.assign(secrets[widgetId], updates);
        writeJsonFile(SECRETS_FILE, secrets);
        sendJson(res, 200, { status: 'ok' });
      } catch (e) { sendError(res, e.message, 400); }
    });
    return;
  }

  if (req.method === 'DELETE' && pathname.match(/^\/api\/secrets\/[^/]+\/[^/]+$/)) {
    if (isPublicMode()) { sendJson(res, 403, { error: 'Forbidden in public mode' }); return; }
    const parts = pathname.split('/');
    const widgetId = parts[3];
    const key = parts[4];
    const secrets = getSecrets();
    if (secrets[widgetId]) {
      delete secrets[widgetId][key];
      if (Object.keys(secrets[widgetId]).length === 0) delete secrets[widgetId];
      writeJsonFile(SECRETS_FILE, secrets);
    }
    sendJson(res, 200, { status: 'ok' });
    return;
  }

  // ── Public mode guard: block edit-related APIs ──
  if (isPublicMode()) {
    const editPaths = ['/config'];
    const isEditApi = (req.method === 'POST' && editPaths.includes(pathname)) ||
                      (req.method === 'POST' && pathname.startsWith('/api/templates/')) ||
                      (req.method === 'DELETE' && pathname.startsWith('/api/templates/'));
    if (isEditApi) {
      sendJson(res, 403, { error: 'Dashboard is in public mode. Editing is disabled.' });
      return;
    }
  }

  // ── Pages system routing ──
  const pageMatch = matchPageRoute(loadedPages, req.method, pathname, parsedUrl);
  if (pageMatch) {
    if (pageMatch.type === 'list') {
      sendJson(res, 200, loadedPages.filter(p => p.nav !== false).map(p => ({ id: p.id, title: p.title, icon: p.icon, description: p.description, order: p.order })));
      return;
    }
    if (pageMatch.type === 'redirect') {
      res.writeHead(302, { Location: pageMatch.location });
      res.end();
      return;
    }
    if (pageMatch.type === 'static') {
      const resolved = path.resolve(pageMatch.filePath);
      // Security: ensure path is within one of the allowed page directories
      const isAllowed = PAGES_DIRS.some(dir => resolved.startsWith(path.resolve(dir)));
      if (!isAllowed) {
        sendResponse(res, 403, 'text/plain', 'Forbidden');
        return;
      }
      const ext = path.extname(resolved).toLowerCase();
      const contentType = MIME_TYPES[ext] || 'application/octet-stream';
      fs.readFile(resolved, (err, data) => {
        if (err) { sendResponse(res, 404, 'text/plain', 'Not Found'); return; }
        sendResponse(res, 200, contentType, data);
      });
      return;
    }
    if (pageMatch.type === 'api') {
      // Parse body for non-GET requests
      if (req.method === 'GET') {
        try {
          const result = await pageMatch.handler(req, res, { query: pageMatch.query, body: {}, params: pageMatch.params });
          if (result !== undefined && !res.writableEnded) sendJson(res, res.statusCode || 200, result);
        } catch (e) { sendError(res, e.message); }
        return;
      }
      // Parse JSON body
      const MAX_BODY = 1024 * 1024;
      let body = '';
      let overflow = false;
      req.on('data', chunk => { body += chunk.toString(); if (body.length > MAX_BODY) { overflow = true; req.destroy(); } });
      req.on('end', async () => {
        if (overflow) { sendError(res, 'Request body too large', 413); return; }
        let parsed = {};
        try { if (body) parsed = JSON.parse(body); } catch (_) {}
        try {
          const result = await pageMatch.handler(req, res, { query: pageMatch.query, body: parsed, params: pageMatch.params });
          if (result !== undefined && !res.writableEnded) sendJson(res, res.statusCode || 200, result);
        } catch (e) { sendError(res, e.message); }
      });
      return;
    }
  }

  // GET/POST /api/todos - Read/write todo list
  if (pathname === '/api/todos') {
    const todosFile = path.join(CWD, 'todos.json');
    if (req.method === 'GET') {
      fs.readFile(todosFile, 'utf8', (err, data) => {
        if (err) {
          if (err.code === 'ENOENT') return sendJson(res, 200, []);
          return sendError(res, err.message);
        }
        try { sendJson(res, 200, JSON.parse(data)); }
        catch (e) { sendJson(res, 200, []); }
      });
      return;
    }
    if (req.method === 'POST') {
      const MAX_TODO_BODY = 256 * 1024; // 256 KB limit
      let body = '';
      let overflow = false;
      req.on('data', chunk => {
        body += chunk.toString();
        if (body.length > MAX_TODO_BODY) { overflow = true; req.destroy(); }
      });
      req.on('end', () => {
        if (overflow) { sendError(res, 'Request body too large', 413); return; }
        try {
          const todos = JSON.parse(body);
          fs.writeFile(todosFile, JSON.stringify(todos, null, 2), 'utf8', (err) => {
            if (err) return sendError(res, err.message);
            sendJson(res, 200, { status: 'ok' });
          });
        } catch (e) { sendError(res, 'Invalid JSON', 400); }
      });
      return;
    }
  }

  // GET/POST /api/notes - Read/write notes content
  if (pathname === '/api/notes') {
    const notesFile = path.join(CWD, 'notes.json');
    if (req.method === 'GET') {
      fs.readFile(notesFile, 'utf8', (err, data) => {
        if (err) {
          if (err.code === 'ENOENT') return sendJson(res, 200, {});
          return sendError(res, err.message);
        }
        try { sendJson(res, 200, JSON.parse(data)); }
        catch (e) { sendJson(res, 200, {}); }
      });
      return;
    }
    if (req.method === 'POST') {
      const MAX_NOTES_BODY = 512 * 1024;
      let body = '';
      let overflow = false;
      req.on('data', chunk => {
        body += chunk.toString();
        if (body.length > MAX_NOTES_BODY) { overflow = true; req.destroy(); }
      });
      req.on('end', () => {
        if (overflow) { sendError(res, 'Request body too large', 413); return; }
        try {
          const notes = JSON.parse(body);
          fs.writeFile(notesFile, JSON.stringify(notes, null, 2), 'utf8', (err) => {
            if (err) return sendError(res, err.message);
            sendJson(res, 200, { status: 'ok' });
          });
        } catch (e) { sendError(res, 'Invalid JSON', 400); }
      });
      return;
    }
  }

  // GET /api/ai-usage - Fetch usage from all configured AI providers
  if (req.method === 'GET' && pathname === '/api/ai-usage') {
    try {
      const data = await getAllAiUsage();
      sendJson(res, 200, { status: 'ok', ...data });
    } catch (e) {
      sendError(res, e.message);
    }
    return;
  }

  // GET /api/ai-usage/:provider - Fetch usage from a specific provider
  const aiUsageMatch = pathname.match(/^\/api\/ai-usage\/(\w+)$/);
  if (req.method === 'GET' && aiUsageMatch) {
    const provider = aiUsageMatch[1];
    try {
      let data;
      switch (provider) {
        case 'claude':
          data = await fetchWithCache('claude', fetchClaudeUsage);
          break;
        case 'codex':
          data = await fetchWithCache('codex', fetchCodexUsage);
          break;
        case 'copilot':
          data = await fetchWithCache('copilot', fetchCopilotUsage);
          break;
        case 'cursor':
          data = await fetchWithCache('cursor', fetchCursorUsage);
          break;
        case 'gemini':
          data = await fetchWithCache('gemini', fetchGeminiUsage);
          break;
        case 'amp':
          data = await fetchWithCache('amp', fetchAmpUsage);
          break;
        case 'factory':
          data = await fetchWithCache('factory', fetchFactoryUsage);
          break;
        case 'kimi':
          data = await fetchWithCache('kimi', fetchKimiUsage);
          break;
        case 'jetbrains':
          data = await fetchWithCache('jetbrains', fetchJetbrainsUsage);
          break;
        case 'minimax':
          data = await fetchWithCache('minimax', fetchMinimaxUsage);
          break;
        case 'zai':
          data = await fetchWithCache('zai', fetchZaiUsage);
          break;
        case 'antigravity':
          data = await fetchWithCache('antigravity', fetchAntigravityUsage);
          break;
        default:
          return sendJson(res, 404, { status: 'error', message: `Unknown provider: ${provider}` });
      }
      sendJson(res, 200, { status: 'ok', ...data });
    } catch (e) {
      sendError(res, e.message);
    }
    return;
  }

  // GET /api/cron - Read cron jobs from OpenClaw cron store
  if (req.method === 'GET' && pathname === '/api/cron') {
    const cronFile = path.join(os.homedir(), '.openclaw', 'cron', 'jobs.json');
    fs.readFile(cronFile, 'utf8', (err, data) => {
      if (err) {
        if (err.code === 'ENOENT') return sendJson(res, 200, { jobs: [] });
        return sendError(res, err.message);
      }
      try {
        const parsed = JSON.parse(data);
        const jobs = (parsed.jobs || []).map(j => ({
          name: j.name,
          schedule: j.schedule?.expr || '—',
          tz: j.schedule?.tz || '',
          enabled: j.enabled,
          lastRun: j.state?.lastRunAtMs ? new Date(j.state.lastRunAtMs).toISOString() : null,
          lastStatus: j.state?.lastStatus || null
        }));
        sendJson(res, 200, { jobs });
      } catch (e) { sendError(res, e.message); }
    });
    return;
  }

  // GET /api/system-log - Structured system log entries
  if (req.method === 'GET' && pathname === '/api/system-log') {
    try {
      const logPath = path.join(os.homedir(), '.openclaw', 'logs', 'gateway.log');
      if (!fs.existsSync(logPath)) {
        sendJson(res, 200, { status: 'ok', entries: [] });
        return;
      }
      const content = fs.readFileSync(logPath, 'utf8');
      const maxLines = Math.min(Math.max(parseInt(parsedUrl.searchParams.get('max')) || 50, 1), 200);
      const lines = content.split('\n').filter(l => l.trim());
      const entries = lines.slice(-maxLines).reverse().map(line => {
        let level = 'INFO';
        let category = 'system';
        if (/\b(error|fatal)\b/i.test(line)) level = 'ERROR';
        else if (/\bwarn/i.test(line)) level = 'WARN';
        else if (/\b(ok|success|ready|started|connected)\b/i.test(line)) level = 'OK';
        const tsMatch = line.match(/(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z?)/);
        const time = tsMatch ? tsMatch[1] : new Date().toISOString();
        if (/\b(cron|schedule)\b/i.test(line)) category = 'cron';
        else if (/\b(auth|login|token)\b/i.test(line)) category = 'auth';
        else if (/\b(session|agent)\b/i.test(line)) category = 'session';
        else if (/\b(exec|command)\b/i.test(line)) category = 'exec';
        else if (/\b(file|read|write)\b/i.test(line)) category = 'file';
        else if (/\b(restart|gateway|start)\b/i.test(line)) category = 'gateway';
        let message = line.replace(/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z?\s*/, '').trim();
        return { time, level, category, message };
      });
      sendJson(res, 200, { status: 'ok', entries });
    } catch (e) {
      sendJson(res, 200, { status: 'ok', entries: [{ time: new Date().toISOString(), level: 'ERROR', category: 'system', message: 'Error reading log: ' + e.message }] });
    }
    return;
  }

  // GET /api/logs - Read last 50 lines from gateway log
  if (req.method === 'GET' && pathname === '/api/logs') {
    const logFile = path.join(os.homedir(), '.openclaw', 'logs', 'gateway.log');
    fs.readFile(logFile, 'utf8', (err, data) => {
      if (err) {
        if (err.code === 'ENOENT') return sendJson(res, 200, { lines: [] });
        return sendError(res, err.message);
      }
      const allLines = data.split('\n').filter(l => l.trim());
      const lines = allLines.slice(-50);
      sendJson(res, 200, { lines });
    });
    return;
  }

  // GET /api/auth - OpenClaw auth status
  if (req.method === 'GET' && pathname === '/api/auth') {
    try {
      const home = os.homedir();
      const configPath = path.join(home, '.openclaw', 'openclaw.json');
      const authProfilesPath = path.join(home, '.openclaw', 'agents', 'main', 'agent', 'auth-profiles.json');
      const config = JSON.parse(fs.readFileSync(configPath, 'utf8'));
      const authProfiles = JSON.parse(fs.readFileSync(authProfilesPath, 'utf8'));

      // Get primary anthropic profile
      const anthropicOrder = config.auth?.order?.anthropic || [];
      const primaryId = anthropicOrder[0] || 'anthropic:default';
      const profileKey = primaryId.includes(':') ? primaryId : `anthropic:${primaryId}`;
      const profileType = authProfiles.profiles?.[profileKey]?.type;
      const mode = profileType === 'token' ? 'Monthly' : 'API';

      sendJson(res, 200, { status: 'ok', mode, primary: profileKey });
    } catch (e) {
      sendError(res, `Auth status error: ${e.message}`);
    }
    return;
  }

  // GET /api/releases - OpenClaw release info (cached 1hr)
  if (req.method === 'GET' && pathname === '/api/releases') {
    const now = Date.now();
    if (_releaseCache && (now - _releaseCacheTime) < 3600000) {
      sendJson(res, 200, _releaseCache);
      return;
    }
    (async () => {
      try {
        let currentVersion = 'unknown';
        try {
          // Run openclaw --version to get the actual running version
          const { execSync } = require('child_process');
          const cliOutput = execSync('openclaw --version 2>/dev/null', { encoding: 'utf8', timeout: 5000 }).trim();
          // Output format: "OpenClaw 2026.3.23-2 (hash)" — extract just the version
          const vMatch = cliOutput.match(/(\d{4}\.\d+\.\d+(?:-\d+)?)/);
          currentVersion = vMatch ? vMatch[1] : cliOutput;
        } catch (_) {
          // Fallback: try reading from package.json
          try {
            const nodeDir = path.dirname(path.dirname(process.execPath));
            const candidates = [
              path.join(nodeDir, 'lib/node_modules/openclaw/package.json'),
              path.join(os.homedir(), '.nvm/versions/node', process.version, 'lib/node_modules/openclaw/package.json'),
              '/usr/local/lib/node_modules/openclaw/package.json'
            ];
            for (const cand of candidates) {
              try {
                currentVersion = JSON.parse(fs.readFileSync(cand, 'utf8')).version;
                break;
              } catch (_) {}
            }
          } catch (_) {}
        }

        const ghRes = await fetch('https://api.github.com/repos/openclaw/openclaw/releases/latest');
        const ghData = await ghRes.json();
        const result = {
          status: 'ok',
          current: currentVersion,
          latest: ghData.tag_name,
          latestUrl: ghData.html_url,
          publishedAt: ghData.published_at
        };
        _releaseCache = result;
        _releaseCacheTime = now;
        sendJson(res, 200, result);
      } catch (e) {
        sendError(res, `Release check error: ${e.message}`);
      }
    })();
    return;
  }

  // GET /api/lb-release - LobsterBoard version check
  if (req.method === 'GET' && pathname === '/api/lb-release') {
    const now = Date.now();
    if (_lbReleaseCache && (now - _lbReleaseCacheTime) < 3600000) {
      sendJson(res, 200, _lbReleaseCache);
      return;
    }
    (async () => {
      try {
        let currentVersion = 'unknown';
        try {
          const pkgPath = path.join(__dirname, 'package.json');
          currentVersion = JSON.parse(fs.readFileSync(pkgPath, 'utf8')).version;
        } catch (_) {}

        const ghRes = await fetch('https://api.github.com/repos/lobsterboard/lobsterboard/releases/latest');
        const ghData = await ghRes.json();
        const result = {
          status: 'ok',
          current: currentVersion,
          latest: ghData.tag_name || currentVersion,
          latestUrl: ghData.html_url || '',
          publishedAt: ghData.published_at || null
        };
        _lbReleaseCache = result;
        _lbReleaseCacheTime = now;
        sendJson(res, 200, result);
      } catch (e) {
        sendError(res, `LB Release check error: ${e.message}`);
      }
    })();
    return;
  }

  // GET /api/today - Today's activity summary (port 3000 style)
  if (req.method === 'GET' && pathname === '/api/today') {
    try {
      const { execSync } = require('child_process');
      const now = new Date();
      const dateStr = [now.getFullYear(), String(now.getMonth()+1).padStart(2,'0'), String(now.getDate()).padStart(2,'0')].join('-');
      const activities = [];

      // 1. Today's memory file headers
      const memoryDir = path.join(os.homedir(), 'clawd', 'memory');
      const todayFile = path.join(memoryDir, `${dateStr}.md`);
      if (fs.existsSync(todayFile)) {
        const content = fs.readFileSync(todayFile, 'utf8');
        content.split('\n').forEach(line => {
          if (line.startsWith('#')) {
            const text = line.replace(/^#+\s*/, '').trim();
            if (text && !/session notes/i.test(text)) {
              activities.push({ type: 'note', icon: '📝', text, source: 'memory' });
            }
          }
        });
      }

      // 2. Git commits from today
      try {
        const commits = execSync(
          `cd ~/clawd && git log --since="today 00:00" --pretty=format:"%s" 2>/dev/null`,
          { encoding: 'utf8', timeout: 5000 }
        ).trim();
        if (commits) {
          commits.split('\n').slice(0, 10).forEach(msg => {
            if (msg.trim()) {
              activities.push({ type: 'commit', icon: '💾', text: msg.trim(), source: 'git' });
            }
          });
        }
      } catch (_) {}

      // 3. Cron job runs from today
      const cronFile = path.join(os.homedir(), '.openclaw', 'cron', 'jobs.json');
      if (fs.existsSync(cronFile)) {
        try {
          const cronData = JSON.parse(fs.readFileSync(cronFile, 'utf8'));
          (cronData.jobs || []).forEach(job => {
            const lastMs = job.state && job.state.lastRunAtMs;
            if (lastMs) {
              const runDate = new Date(lastMs);
              const runDateStr = [runDate.getFullYear(), String(runDate.getMonth()+1).padStart(2,'0'), String(runDate.getDate()).padStart(2,'0')].join('-');
              if (runDateStr === dateStr) {
                activities.push({ type: 'cron', icon: '⏰', text: `${job.name} ran`, source: 'cron', status: job.state.lastStatus || 'ok' });
              }
            }
          });
        } catch (_) {}
      }

      // Dedupe
      const seen = new Set();
      const unique = activities.filter(a => {
        const key = a.text.toLowerCase();
        if (seen.has(key)) return false;
        seen.add(key);
        return true;
      });

      sendJson(res, 200, { date: dateStr, activities: unique.slice(0, 15), count: unique.length });
    } catch (e) {
      const now = new Date();
      const dateStr = [now.getFullYear(), String(now.getMonth()+1).padStart(2,'0'), String(now.getDate()).padStart(2,'0')].join('-');
      sendJson(res, 200, { date: dateStr, activities: [], count: 0, error: e.message });
    }
    return;
  }

  // GET /api/activity - Recent activity from today's memory file
  if (req.method === 'GET' && pathname === '/api/activity') {
    try {
      const now = new Date();
      // Use local date (EST), not UTC
      const dateStr = [now.getFullYear(), String(now.getMonth()+1).padStart(2,'0'), String(now.getDate()).padStart(2,'0')].join('-');
      const memoryDir = path.join(__dirname, '..', 'memory');
      const todayFile = path.join(memoryDir, `${dateStr}.md`);
      const items = [];
      if (fs.existsSync(todayFile)) {
        const content = fs.readFileSync(todayFile, 'utf8');
        const lines = content.split('\n');
        for (const line of lines) {
          const trimmed = line.trim();
          // Extract bullet points and headings as activity items
          if (trimmed.startsWith('- ') && trimmed.length > 4) {
            items.push({ text: trimmed.slice(2), time: dateStr });
          } else if (trimmed.startsWith('## ') && trimmed.length > 4) {
            items.push({ text: '📌 ' + trimmed.slice(3), time: dateStr });
          }
        }
      }
      // If no memory file, show a placeholder
      if (items.length === 0) {
        items.push({ text: 'No activity logged yet today.' });
      }
      sendJson(res, 200, { items: items.slice(-20).reverse() });
    } catch (e) {
      sendJson(res, 200, { items: [{ text: 'Error loading activity: ' + e.message }] });
    }
    return;
  }

  // GET /api/rss?url=<feedUrl>&widgetId=<id>&secretKey=<key> - Server-side RSS proxy
  if (req.method === 'GET' && pathname === '/api/rss') {
    let feedUrl = parsedUrl.searchParams.get('url');
    const rssWidgetId = parsedUrl.searchParams.get('widgetId');
    const rssSecretKey = parsedUrl.searchParams.get('secretKey') || 'feedUrl';
    if ((!feedUrl || feedUrl === '••••••••' || feedUrl === '__SECRET__') && rssWidgetId) {
      const secrets = getSecrets();
      feedUrl = secrets[rssWidgetId]?.[rssSecretKey] || null;
    }
    if (!feedUrl) { sendError(res, 'Missing url parameter', 400); return; }

    // Validate URL: only http/https, block private/internal IPs (SSRF protection)
    function isPrivateHost(hostname) {
      const patterns = [
        /^127\./, /^10\./, /^172\.(1[6-9]|2\d|3[01])\./, /^192\.168\./,
        /^169\.254\./, /^0\./, /^localhost$/i, /^\[?::1\]?$/, /^\[?fc/i, /^\[?fd/i
      ];
      return patterns.some(p => p.test(hostname));
    }
    try {
      const parsed = new URL(feedUrl);
      if (parsed.protocol !== 'http:' && parsed.protocol !== 'https:') {
        sendError(res, 'Only http and https URLs are allowed', 400); return;
      }
      if (isPrivateHost(parsed.hostname)) {
        sendError(res, 'URLs pointing to private/internal addresses are not allowed', 400); return;
      }
    } catch (urlErr) {
      sendError(res, 'Invalid URL', 400); return;
    }

    try {
      const https = require('https');
      const http2 = require('http');
      function fetchFeed(url, redirects) {
        if (redirects > 3) { sendError(res, 'Too many redirects'); return; }
        // Validate each URL (including redirects) against SSRF
        try {
          const rp = new URL(url);
          if (rp.protocol !== 'http:' && rp.protocol !== 'https:') { sendError(res, 'Redirect to disallowed scheme', 400); return; }
          if (isPrivateHost(rp.hostname)) { sendError(res, 'Redirect to private address blocked', 400); return; }
        } catch (_) { sendError(res, 'Invalid redirect URL', 400); return; }
        const mod = url.startsWith('https') ? https : http2;
        const req2 = mod.get(url, { headers: { 'User-Agent': 'LobsterBoard/1.0' }, timeout: 15000 }, (proxyRes) => {
          if ([301, 302, 307, 308].includes(proxyRes.statusCode) && proxyRes.headers.location) {
            proxyRes.resume();
            fetchFeed(proxyRes.headers.location, redirects + 1);
            return;
          }
          let body = '';
          proxyRes.on('data', c => { body += c; if (body.length > 5000000) proxyRes.destroy(); });
          proxyRes.on('end', () => { sendResponse(res, 200, 'application/xml', body, { 'Access-Control-Allow-Origin': '*' }); });
        });
        req2.on('error', e => sendError(res, e.message));
        req2.on('timeout', () => { req2.destroy(); sendError(res, 'Feed request timed out'); });
      }
      fetchFeed(feedUrl, 0);
    } catch (e) { sendError(res, e.message); }
    return;
  }

  // GET /api/calendar?url=<icalUrl>&max=<maxEvents>&widgetId=<id>&secretKey=<key> - iCal feed proxy + parser
  if (req.method === 'GET' && pathname === '/api/calendar') {
    let icalUrl = parsedUrl.searchParams.get('url');
    const maxEvents = Math.min(parseInt(parsedUrl.searchParams.get('max')) || 10, 50);
    const widgetId = parsedUrl.searchParams.get('widgetId');
    const secretKey = parsedUrl.searchParams.get('secretKey') || 'icalUrl';
    // If url is masked/placeholder, resolve from secrets
    if ((!icalUrl || icalUrl === '••••••••' || icalUrl === '__SECRET__') && widgetId) {
      const secrets = getSecrets();
      icalUrl = secrets[widgetId]?.[secretKey] || null;
    }
    if (!icalUrl) { sendError(res, 'Missing url parameter', 400); return; }

    // Validate URL: only http/https, block private/internal IPs
    function isPrivateHost(hostname) {
      const patterns = [
        /^127\./, /^10\./, /^172\.(1[6-9]|2\d|3[01])\./, /^192\.168\./,
        /^169\.254\./, /^0\./, /^localhost$/i, /^\[?::1\]?$/, /^\[?fc/i, /^\[?fd/i
      ];
      return patterns.some(p => p.test(hostname));
    }
    try {
      const parsed = new URL(icalUrl);
      if (parsed.protocol !== 'http:' && parsed.protocol !== 'https:') {
        sendError(res, 'Only http and https URLs are allowed', 400); return;
      }
      if (isPrivateHost(parsed.hostname)) {
        sendError(res, 'URLs pointing to private/internal addresses are not allowed', 400); return;
      }
    } catch (urlErr) {
      sendError(res, 'Invalid URL', 400); return;
    }

    // 5-minute cache keyed by url+max
    if (!global._calendarCache) global._calendarCache = {};
    const cacheKey = icalUrl + '|' + maxEvents;
    const cached = global._calendarCache[cacheKey];
    if (cached && Date.now() - cached.ts < 300000) {
      sendJson(res, 200, cached.data);
      return;
    }

    try {
      const https = require('https');
      const http2 = require('http');
      function fetchIcal(url, redirects) {
        if (redirects > 3) { sendError(res, 'Too many redirects'); return; }
        // Validate each URL (including redirects) against SSRF
        try {
          const rp = new URL(url);
          if (rp.protocol !== 'http:' && rp.protocol !== 'https:') { sendError(res, 'Redirect to disallowed scheme', 400); return; }
          if (isPrivateHost(rp.hostname)) { sendError(res, 'Redirect to private address blocked', 400); return; }
        } catch (_) { sendError(res, 'Invalid redirect URL', 400); return; }
        const mod = url.startsWith('https') ? https : http2;
        const req2 = mod.get(url, { headers: { 'User-Agent': 'LobsterBoard/1.0' }, timeout: 15000 }, (proxyRes) => {
          if ([301, 302, 307, 308].includes(proxyRes.statusCode) && proxyRes.headers.location) {
            proxyRes.resume();
            fetchIcal(proxyRes.headers.location, redirects + 1);
            return;
          }
          let body = '';
          proxyRes.on('data', c => { body += c; if (body.length > 5000000) proxyRes.destroy(); });
          proxyRes.on('end', () => {
            try {
              const events = parseIcal(body, maxEvents);
              global._calendarCache[cacheKey] = { ts: Date.now(), data: events };
              sendJson(res, 200, events);
            } catch (e) { sendError(res, 'Failed to parse iCal: ' + e.message); }
          });
        });
        req2.on('error', e => sendError(res, e.message));
        req2.on('timeout', () => { req2.destroy(); sendError(res, 'Request timed out'); });
      }
      fetchIcal(icalUrl, 0);
    } catch (e) { sendError(res, e.message); }
    return;
  }

  // GET /api/usage/claude - Anthropic Claude usage proxy
  if (req.method === 'GET' && pathname === '/api/usage/claude') {
    let apiKey = process.env.ANTHROPIC_ADMIN_KEY;
    if (!apiKey) {
      try {
        const cfg = JSON.parse(fs.readFileSync(CONFIG_FILE, 'utf8'));
        const w = (cfg.widgets || []).find(w => w.type === 'ai-usage-claude');
        if (w && w.properties && w.properties.apiKey && w.properties.apiKey !== '__SECRET__') {
          apiKey = w.properties.apiKey;
        } else if (w) {
          // Check secrets store
          const secrets = getSecrets();
          apiKey = secrets[w.id]?.apiKey || null;
        }
      } catch(e) {}
    }
    if (!apiKey) { sendJson(res, 200, { error: 'No API key configured. Add your Anthropic Admin key in the widget properties.', tokens: 0, cost: 0, models: [] }); return; }
    (async () => {
      try {
        const now = new Date();
        const today = now.toISOString().slice(0, 10);
        const tomorrow = new Date(now.getTime() + 86400000).toISOString().slice(0, 10);
        // Week: Monday of current week
        const dayOfWeek = now.getDay();
        const mondayOffset = dayOfWeek === 0 ? 6 : dayOfWeek - 1;
        const weekStart = new Date(now.getTime() - mondayOffset * 86400000).toISOString().slice(0, 10);
        // Month: 1st of current month
        const monthStart = today.slice(0, 8) + '01';
        const headers = { 'anthropic-version': '2023-06-01', 'x-api-key': apiKey };
        const base = 'https://api.anthropic.com/v1/organizations/usage_report/messages';

        function aggregateBuckets(data) {
          let totalTokens = 0, totalCost = 0;
          const modelMap = {};
          for (const bucket of (data.data || [])) {
            const input = bucket.input_tokens || 0;
            const output = bucket.output_tokens || 0;
            const tokens = input + output;
            const cost = (bucket.input_cost || 0) + (bucket.output_cost || 0);
            totalTokens += tokens;
            totalCost += cost;
            const model = bucket.model || 'unknown';
            if (!modelMap[model]) modelMap[model] = { name: model, tokens: 0, cost: 0 };
            modelMap[model].tokens += tokens;
            modelMap[model].cost += cost;
          }
          return { tokens: totalTokens, cost: totalCost, models: Object.values(modelMap) };
        }

        const [todayResp, weekResp, monthResp] = await Promise.all([
          fetch(`${base}?starting_at=${today}T00:00:00Z&ending_at=${tomorrow}T00:00:00Z&bucket_width=1d&group_by[]=model`, { headers }),
          fetch(`${base}?starting_at=${weekStart}T00:00:00Z&ending_at=${tomorrow}T00:00:00Z&bucket_width=1d&group_by[]=model`, { headers }),
          fetch(`${base}?starting_at=${monthStart}T00:00:00Z&ending_at=${tomorrow}T00:00:00Z&bucket_width=1d&group_by[]=model`, { headers })
        ]);

        const todayData = await todayResp.json();
        if (!todayResp.ok) { sendJson(res, 200, { error: todayData.error?.message || 'API error', tokens: 0, cost: 0, models: [] }); return; }
        const weekData = await weekResp.json();
        const monthData = await monthResp.json();

        const todayAgg = aggregateBuckets(todayData);
        const weekAgg = aggregateBuckets(weekData);
        const monthAgg = aggregateBuckets(monthData);

        sendJson(res, 200, {
          tokens: todayAgg.tokens, cost: todayAgg.cost, models: todayAgg.models,
          week: { tokens: weekAgg.tokens, cost: weekAgg.cost },
          month: { tokens: monthAgg.tokens, cost: monthAgg.cost }
        });
      } catch (e) {
        sendJson(res, 200, { error: e.message, tokens: 0, cost: 0, models: [] });
      }
    })();
    return;
  }

  // GET /api/usage/openai - OpenAI usage proxy
  if (req.method === 'GET' && pathname === '/api/usage/openai') {
    let apiKey = process.env.OPENAI_API_KEY;
    if (!apiKey) {
      try {
        const cfg = JSON.parse(fs.readFileSync(CONFIG_FILE, 'utf8'));
        const w = (cfg.widgets || []).find(w => w.type === 'ai-usage-openai');
        if (w && w.properties && w.properties.apiKey && w.properties.apiKey !== '__SECRET__') {
          apiKey = w.properties.apiKey;
        } else if (w) {
          const secrets = getSecrets();
          apiKey = secrets[w.id]?.apiKey || null;
        }
      } catch(e) {}
    }
    if (!apiKey) { sendJson(res, 200, { error: 'No API key configured. Add your OpenAI key in the widget properties.', tokens: 0, cost: 0, models: [] }); return; }
    (async () => {
      try {
        const now = new Date();
        const todayUnix = Math.floor(new Date(now.toISOString().slice(0, 10) + 'T00:00:00Z').getTime() / 1000);
        const dayOfWeek = now.getDay();
        const mondayOffset = dayOfWeek === 0 ? 6 : dayOfWeek - 1;
        const weekStartUnix = todayUnix - mondayOffset * 86400;
        const monthStartUnix = Math.floor(new Date(now.toISOString().slice(0, 8) + '01T00:00:00Z').getTime() / 1000);
        const headers = { 'Authorization': `Bearer ${apiKey}` };
        const base = 'https://api.openai.com/v1/organization/costs';

        function aggregateOpenAI(data) {
          let totalCost = 0;
          const modelMap = {};
          for (const bucket of (data.data || [])) {
            for (const lineItem of (bucket.results || [])) {
              const cost = (lineItem.amount?.value || 0);
              totalCost += cost;
              const model = lineItem.line_item || 'unknown';
              if (!modelMap[model]) modelMap[model] = { name: model, tokens: 0, cost: 0 };
              modelMap[model].cost += cost;
            }
          }
          return { cost: totalCost / 100, models: Object.values(modelMap).map(m => ({ ...m, cost: m.cost / 100 })) };
        }

        const [todayResp, weekResp, monthResp] = await Promise.all([
          fetch(`${base}?start_time=${todayUnix}&bucket_width=1d`, { headers }),
          fetch(`${base}?start_time=${weekStartUnix}&bucket_width=1d`, { headers }),
          fetch(`${base}?start_time=${monthStartUnix}&bucket_width=1d`, { headers })
        ]);

        const todayData = await todayResp.json();
        if (!todayResp.ok) {
          const errMsg = todayData.error?.message || todayData.error || 'API error';
          const hint = typeof errMsg === 'string' && errMsg.includes('scope') ? ' Enable "Usage: Read" scope on your API key.' : '';
          sendJson(res, 200, { error: errMsg + hint, tokens: 0, cost: 0, models: [] }); return;
        }
        const weekData = await weekResp.json();
        const monthData = await monthResp.json();

        const todayAgg = aggregateOpenAI(todayData);
        const weekAgg = aggregateOpenAI(weekData);
        const monthAgg = aggregateOpenAI(monthData);

        sendJson(res, 200, {
          tokens: 0, cost: todayAgg.cost, models: todayAgg.models,
          week: { tokens: 0, cost: weekAgg.cost },
          month: { tokens: 0, cost: monthAgg.cost }
        });
      } catch (e) {
        sendJson(res, 200, { error: e.message, tokens: 0, cost: 0, models: [] });
      }
    })();
    return;
  }

  // GET /api/stats - Return cached system stats
  if (req.method === 'GET' && pathname === '/api/stats') {
    sendJson(res, 200, cachedStats);
    return;
  }

  // GET /api/stats/stream - SSE endpoint for live stats
  if (req.method === 'GET' && pathname === '/api/stats/stream') {
    if (sseClients.size >= 10) {
      sendError(res, 'Too many SSE connections', 429);
      return;
    }
    res.writeHead(200, {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive',
      'Access-Control-Allow-Origin': '*'
    });
    res.write(`data: ${JSON.stringify(cachedStats)}\n\n`);
    sseClients.add(res);
    req.on('close', () => sseClients.delete(res));
    return;
  }

  // ── Templates API ──
  const TEMPLATES_DIR = path.join(__dirname, 'templates');

  // GET /api/templates — list all templates
  if (req.method === 'GET' && pathname === '/api/templates') {
    try {
      const templates = scanTemplates(TEMPLATES_DIR);
      sendJson(res, 200, templates);
    } catch (e) {
      sendError(res, `Failed to list templates: ${e.message}`);
    }
    return;
  }

  // GET /api/templates/:id — get a template's config.json
  if (req.method === 'GET' && pathname.match(/^\/api\/templates\/([^/]+)$/) && !pathname.endsWith('/preview')) {
    const id = pathname.split('/')[3];
    const configPath = path.join(TEMPLATES_DIR, id, 'config.json');
    if (!fs.existsSync(configPath)) { sendJson(res, 404, { error: 'Template not found' }); return; }
    try {
      const config = JSON.parse(fs.readFileSync(configPath, 'utf8'));
      sendJson(res, 200, config);
    } catch (e) { sendError(res, e.message); }
    return;
  }

  // GET /api/templates/:id/preview — serve preview image
  if (req.method === 'GET' && pathname.match(/^\/api\/templates\/([^/]+)\/preview$/)) {
    const id = pathname.split('/')[3];
    const metaPath = path.join(TEMPLATES_DIR, id, 'meta.json');
    let previewFile = 'preview.png';
    try { previewFile = JSON.parse(fs.readFileSync(metaPath, 'utf8')).preview || 'preview.png'; } catch (_) {}
    const previewPath = path.join(TEMPLATES_DIR, id, previewFile);
    if (!fs.existsSync(previewPath)) { sendResponse(res, 404, 'text/plain', 'No preview'); return; }
    const ext = path.extname(previewPath).toLowerCase();
    const ct = MIME_TYPES[ext] || 'application/octet-stream';
    fs.readFile(previewPath, (err, data) => {
      if (err) { sendResponse(res, 404, 'text/plain', 'Not found'); return; }
      sendResponse(res, 200, ct, data);
    });
    return;
  }

  // POST /api/templates/import — import a template
  if (req.method === 'POST' && pathname === '/api/templates/import') {
    let body = '';
    req.on('data', c => body += c);
    req.on('end', () => {
      try {
        const { id, mode } = JSON.parse(body);
        if (!id) { sendJson(res, 400, { error: 'Missing template id' }); return; }
        if (!mode) { sendJson(res, 400, { error: 'Missing import mode' }); return; }
        
        const tplConfigPath = path.join(TEMPLATES_DIR, id, 'config.json');
        if (!fs.existsSync(tplConfigPath)) { sendJson(res, 404, { error: `Template "${id}" not found` }); return; }
        
        let tplConfig;
        try {
          tplConfig = JSON.parse(fs.readFileSync(tplConfigPath, 'utf8'));
        } catch (parseErr) {
          sendJson(res, 500, { error: `Template config is invalid JSON: ${parseErr.message}` }); return;
        }

        if (mode === 'replace') {
          try {
            fs.writeFileSync(CONFIG_FILE, JSON.stringify(tplConfig, null, 2));
          } catch (writeErr) {
            sendJson(res, 500, { error: `Failed to write config: ${writeErr.message}` }); return;
          }
          sendJson(res, 200, { status: 'success', message: 'Template imported (replace)' });
        } else if (mode === 'merge') {
          let currentConfig = { canvas: { width: 1920, height: 1080 }, widgets: [] };
          try { currentConfig = JSON.parse(fs.readFileSync(CONFIG_FILE, 'utf8')); } catch (_) {}
          // Find max Y of existing widgets
          let maxY = 0;
          for (const w of (currentConfig.widgets || [])) {
            const bottom = (w.y || 0) + (w.height || 100);
            if (bottom > maxY) maxY = bottom;
          }
          const offset = maxY + 100;
          const newWidgets = (tplConfig.widgets || []).map(w => ({
            ...w,
            id: w.id + '-tpl-' + Date.now(),
            y: (w.y || 0) + offset
          }));
          currentConfig.widgets = [...(currentConfig.widgets || []), ...newWidgets];
          try {
            fs.writeFileSync(CONFIG_FILE, JSON.stringify(currentConfig, null, 2));
          } catch (writeErr) {
            sendJson(res, 500, { error: `Failed to write config: ${writeErr.message}` }); return;
          }
          sendJson(res, 200, { status: 'success', message: `Merged ${newWidgets.length} widgets` });
        } else {
          sendJson(res, 400, { error: 'Invalid mode. Use "replace" or "merge"' });
        }
      } catch (e) { sendJson(res, 500, { error: `Import error: ${e.message}` }); }
    });
    return;
  }

  // POST /api/templates/export — export current config as template
  // GET /api/quote - proxy for zenquotes.io (CORS blocked in browser)
  if (req.method === 'GET' && pathname === '/api/quote') {
    const https = require('https');
    https.get('https://zenquotes.io/api/random', { headers: { 'User-Agent': 'LobsterBoard/1.0' }, timeout: 5000 }, (proxyRes) => {
      let body = '';
      proxyRes.on('data', c => body += c);
      proxyRes.on('end', () => {
        res.setHeader('Access-Control-Allow-Origin', '*');
        sendResponse(res, 200, 'application/json', body);
      });
    }).on('error', (e) => {
      sendResponse(res, 200, 'application/json', JSON.stringify([{ q: 'Stay hungry, stay foolish.', a: 'Steve Jobs' }]));
    });
    return;
  }

  if (req.method === 'GET' && pathname === '/api/latest-image') {
    return latestImageHandler(parsedUrl, res);
  }

  // GET /api/browse-dirs?dir=<path> - list subdirectories for folder picker
  if (req.method === 'GET' && pathname === '/api/browse-dirs') {
    const dir = parsedUrl.searchParams.get('dir') || os.homedir();
    const resolved = path.resolve(dir.replace(/^~/, os.homedir()));
    const home = os.homedir();
    if (!resolved.startsWith(home + path.sep) && resolved !== home) {
      return sendResponse(res, 200, 'application/json', JSON.stringify({ status: 'error', message: 'Must be under home directory' }));
    }
    try {
      const entries = fs.readdirSync(resolved, { withFileTypes: true })
        .filter(e => e.isDirectory() && !e.name.startsWith('.'))
        .map(e => e.name)
        .sort((a, b) => a.localeCompare(b));
      const imageExts = ['.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp', '.svg'];
      const imageCount = fs.readdirSync(resolved).filter(f => imageExts.includes(path.extname(f).toLowerCase())).length;
      return sendResponse(res, 200, 'application/json', JSON.stringify({ status: 'ok', path: resolved, dirs: entries, imageCount }));
    } catch (error) { 
      return sendResponse(res, 200, 'application/json', JSON.stringify({ status: 'error', message: error.message })); 
    }
  }

  if (req.method === 'POST' && pathname === '/api/templates/export') {
    let body = '';
    req.on('data', c => body += c);
    req.on('end', () => {
      try {
        const { name, description, author, tags, widgetTypes } = JSON.parse(body);
        if (!name) { sendJson(res, 400, { error: 'Name is required' }); return; }
        const id = name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
        const tplDir = path.join(TEMPLATES_DIR, id);
        fs.mkdirSync(tplDir, { recursive: true });

        // Read current config and strip sensitive data
        let config = { canvas: { width: 1920, height: 1080 }, widgets: [] };
        try { config = JSON.parse(fs.readFileSync(CONFIG_FILE, 'utf8')); } catch (_) {}

        const sensitiveKeys = ['apiKey', 'api_key', 'token', 'secret', 'password'];
        const privateIpRegex = /^https?:\/\/(10\.\d+\.\d+\.\d+|192\.168\.\d+\.\d+|localhost|127\.0\.0\.1)/i;
        // URLs that may contain private auth tokens — strip them in templates
        const privateUrlKeys = ['icalUrl'];
        const privateUrlPatterns = [/[?&/]private[-_]?[a-f0-9]/i, /caldav\.icloud\.com/i, /\/private\//i];

        function stripSensitive(props) {
          if (!props || typeof props !== 'object') return props;
          let stripped = false;
          const result = Array.isArray(props) ? [...props] : { ...props };
          for (const key of Object.keys(result)) {
            if (sensitiveKeys.includes(key)) {
              result[key] = 'YOUR_API_KEY_HERE';
              stripped = true;
            } else if ((key === 'url' || key === 'endpoint') && typeof result[key] === 'string' && privateIpRegex.test(result[key])) {
              result[key] = 'http://your-server:port/path';
              stripped = true;
            } else if (privateUrlKeys.includes(key) && typeof result[key] === 'string') {
              // Always strip private calendar/feed URLs — they contain auth tokens
              if (result[key] && (result[key].length > 0)) {
                const hasPrivateToken = privateUrlPatterns.some(p => p.test(result[key]));
                if (hasPrivateToken) {
                  result[key] = '';
                  stripped = true;
                }
              }
            } else if (typeof result[key] === 'object' && result[key] !== null) {
              const inner = stripSensitive(result[key]);
              result[key] = inner.result;
              if (inner.stripped) stripped = true;
            }
          }
          return { result, stripped };
        }

        const cleanWidgets = (config.widgets || []).map(w => {
          const cleaned = { ...w };
          if (cleaned.properties) {
            const { result, stripped } = stripSensitive(cleaned.properties);
            cleaned.properties = result;
            if (stripped) cleaned._templateNote = '⚠️ Configure this widget\'s settings after import';
          }
          return cleaned;
        });

        const cleanConfig = { canvas: config.canvas, widgets: cleanWidgets };
        fs.writeFileSync(path.join(tplDir, 'config.json'), JSON.stringify(cleanConfig, null, 2));

        const canvasSize = config.canvas ? `${config.canvas.width}x${config.canvas.height}` : '1920x1080';
        const meta = {
          id,
          name,
          description: description || '',
          author: author || 'anonymous',
          tags: tags || [],
          canvasSize,
          widgetCount: cleanWidgets.length,
          widgetTypes: widgetTypes || [],
          requiresSetup: [],
          preview: 'preview.png'
        };
        fs.writeFileSync(path.join(tplDir, 'meta.json'), JSON.stringify(meta, null, 2));

        // Rebuild templates.json
        const templates = scanTemplates(TEMPLATES_DIR);
        fs.writeFileSync(path.join(TEMPLATES_DIR, 'templates.json'), JSON.stringify(templates, null, 2));

        sendJson(res, 200, { status: 'success', id, message: `Template "${name}" exported` });
      } catch (e) { sendError(res, e.message); }
    });
    return;
  }

  // POST /api/templates/:id/screenshot — upload preview image
  if (req.method === 'POST' && pathname.match(/^\/api\/templates\/[^/]+\/screenshot$/)) {
    const tplId = pathname.split('/')[3];
    const tplDir = path.join(TEMPLATES_DIR, tplId);
    if (!fs.existsSync(tplDir)) { sendJson(res, 404, { error: 'Template not found' }); return; }
    let body = '';
    req.on('data', c => body += c);
    req.on('end', () => {
      try {
        const { data } = JSON.parse(body);
        const match = data.match(/^data:image\/(\w+);base64,(.+)$/);
        if (!match) { sendJson(res, 400, { error: 'Invalid image data' }); return; }
        const buf = Buffer.from(match[2], 'base64');
        fs.writeFileSync(path.join(tplDir, 'preview.png'), buf);
        sendJson(res, 200, { status: 'ok' });
      } catch (e) { sendError(res, e.message); }
    });
    return;
  }

  // DELETE /api/templates/:id — delete a template
  if (req.method === 'DELETE' && pathname.match(/^\/api\/templates\/[^/]+$/)) {
    const tplId = pathname.split('/')[3];
    const tplDir = path.join(TEMPLATES_DIR, tplId);
    if (!fs.existsSync(tplDir)) { sendJson(res, 404, { error: 'Template not found' }); return; }
    try {
      fs.rmSync(tplDir, { recursive: true, force: true });
      sendJson(res, 200, { status: 'success', message: `Template "${tplId}" deleted` });
    } catch (e) { sendError(res, e.message); }
    return;
  }

  // Serve static files
  // Check working directory's public/ folder first (for user assets like recap images)
  const publicPath = path.join(CWD, 'public', pathname);
  const publicResolved = path.resolve(publicPath);
  if (publicResolved.startsWith(path.join(CWD, 'public') + path.sep) && fs.existsSync(publicPath)) {
    const ext = path.extname(publicPath).toLowerCase();
    const contentType = MIME_TYPES[ext] || 'application/octet-stream';
    fs.readFile(publicPath, (err, data) => {
      if (err) { sendError(res, err.message); return; }
      sendResponse(res, 200, contentType, data);
    });
    return;
  }

  let filePath = path.join(__dirname, pathname);
  if (pathname === '/') {
    filePath = path.join(__dirname, 'app.html');
  }

  // Prevent path traversal — ensure resolved path stays within __dirname
  const resolved = path.resolve(filePath);
  if (!resolved.startsWith(__dirname + path.sep) && resolved !== __dirname) {
    sendResponse(res, 403, 'text/plain', 'Forbidden');
    return;
  }

  const ext = path.extname(filePath).toLowerCase();
  const contentType = MIME_TYPES[ext] || 'application/octet-stream';

  fs.readFile(filePath, (err, data) => {
    if (err) {
      if (err.code === 'ENOENT') {
        sendResponse(res, 404, 'text/plain', 'Not Found');
      } else {
        sendError(res, `Server error: ${err.message}`);
      }
      return;
    }
    sendResponse(res, 200, contentType, data);
  });
});

// Graceful shutdown
process.on('SIGTERM', () => server.close(() => process.exit(0)));
process.on('SIGINT', () => server.close(() => process.exit(0)));

server.listen(PORT, HOST, () => {
  const authStatus = DASHBOARD_PASSWORD
    ? '   Password auth: ENABLED (DASHBOARD_PASSWORD is set)'
    : '   Password auth: DISABLED — set DASHBOARD_PASSWORD=yourpassword to enable';
  console.log(`
LobsterBoard Builder Server running at http://${HOST}:${PORT}

${authStatus}

   Press Ctrl+C to stop
`);
});
```

## File: `site-script.js`
```javascript
// Scroll-triggered fade-in for sections
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      observer.unobserve(e.target);
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.feature-card, .widget-cat, .quickstart-option, .screenshot-wrap').forEach(el => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(20px)';
  el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
  observer.observe(el);
});

// Add visible class styles
const style = document.createElement('style');
style.textContent = '.visible { opacity: 1 !important; transform: translateY(0) !important; }';
document.head.appendChild(style);

// Close mobile nav on link click
document.querySelectorAll('.nav-links a').forEach(a => {
  a.addEventListener('click', () => {
    document.querySelector('.nav-links').classList.remove('open');
  });
});

// Lightbox for theme screenshots
function openLightbox(card) {
  const img = card.querySelector('img');
  const lightbox = document.getElementById('lightbox');
  const lightboxImg = document.getElementById('lightbox-img');
  lightboxImg.src = img.src;
  lightboxImg.alt = img.alt;
  lightbox.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeLightbox() {
  document.getElementById('lightbox').classList.remove('open');
  document.body.style.overflow = '';
}

// Close lightbox with Escape key
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeLightbox();
});
```

## File: `site-style.css`
```css
/* LobsterBoard Landing Page */
:root {
  --bg: #0d1117;
  --bg-alt: #161b22;
  --bg-card: #1c2128;
  --border: #30363d;
  --text: #e6edf3;
  --text-dim: #8b949e;
  --red: #e74c3c;
  --red-glow: rgba(231, 76, 60, 0.3);
  --red-dark: #c0392b;
  --radius: 12px;
  --radius-sm: 8px;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html { scroll-behavior: smooth; }

body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

a { color: var(--red); text-decoration: none; }
a:hover { color: #ff6b5a; }

.container { max-width: 1100px; margin: 0 auto; padding: 0 24px; }

/* Nav */
.nav {
  position: fixed; top: 0; left: 0; right: 0; z-index: 100;
  background: rgba(13, 17, 23, 0.85);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border);
}
.nav-inner {
  max-width: 1100px; margin: 0 auto; padding: 0 24px;
  display: flex; align-items: center; justify-content: space-between; height: 60px;
}
.nav-logo img { display: block; }
.nav-links { display: flex; align-items: center; gap: 24px; }
.nav-links a { color: var(--text-dim); font-size: 0.9rem; font-weight: 500; transition: color 0.2s; }
.nav-links a:hover { color: var(--text); }
.nav-toggle { display: none; background: none; border: none; color: var(--text); font-size: 1.4rem; cursor: pointer; }

/* Buttons */
.btn {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 8px 16px; border-radius: var(--radius-sm); font-weight: 600; font-size: 0.875rem;
  border: 1px solid var(--border); color: var(--text); background: var(--bg-card);
  transition: all 0.2s; cursor: pointer; text-decoration: none;
}
.btn:hover { border-color: var(--text-dim); color: var(--text); }
.btn-primary { background: var(--red); border-color: var(--red); color: #fff; }
.btn-primary:hover { background: var(--red-dark); border-color: var(--red-dark); color: #fff; }
.btn-outline { background: transparent; border-color: var(--border); }
.btn-outline:hover { border-color: var(--red); color: var(--red); }
.btn-lg { padding: 12px 28px; font-size: 1rem; border-radius: var(--radius); }
.btn-sm { padding: 6px 12px; font-size: 0.8rem; }

/* Hero */
.hero {
  position: relative; padding: 160px 0 100px; text-align: center; overflow: hidden;
}
.hero-bg {
  position: absolute; inset: 0;
  background: radial-gradient(ellipse at 50% 0%, var(--red-glow) 0%, transparent 60%);
  pointer-events: none;
}
.hero-content { position: relative; }
.hero-logo { width: 320px; margin: 0 auto 32px; display: block; }
.hero h1 { font-size: clamp(2rem, 5vw, 3.2rem); font-weight: 800; letter-spacing: -0.02em; margin-bottom: 16px; }
.hero-sub { font-size: 1.15rem; color: var(--text-dim); max-width: 600px; margin: 0 auto 32px; }
.hero-sub strong { color: var(--text); }
.hero-actions { display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; margin-bottom: 32px; }
.hero-badges { display: flex; gap: 8px; justify-content: center; flex-wrap: wrap; }
.hero-badges img { height: 22px; }

/* Sections */
.section { padding: 100px 0; }
.section-dark { background: var(--bg-alt); }
.section-title {
  font-size: 2rem; font-weight: 800; text-align: center; margin-bottom: 12px;
  letter-spacing: -0.01em;
}
.section-sub {
  text-align: center; color: var(--text-dim); max-width: 550px; margin: 0 auto 48px;
  font-size: 1.05rem;
}

/* Features Grid */
.features-grid {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}
.feature-card {
  background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius);
  padding: 28px; transition: border-color 0.3s, transform 0.3s;
}
.feature-card:hover { border-color: var(--red); transform: translateY(-2px); }
.feature-icon { font-size: 1.8rem; margin-bottom: 12px; }
.feature-card h3 { font-size: 1.1rem; margin-bottom: 8px; }
.feature-card p { color: var(--text-dim); font-size: 0.92rem; line-height: 1.5; }

/* Screenshot */
.screenshot-wrap {
  border-radius: var(--radius); overflow: hidden; border: 1px solid var(--border);
  box-shadow: 0 20px 60px rgba(0,0,0,0.5);
}
.screenshot { width: 100%; display: block; }

/* Widgets */
.widget-categories {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 20px;
}
.widget-cat {
  background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius);
  padding: 24px;
}
.widget-cat h3 { font-size: 1rem; margin-bottom: 12px; color: var(--text); }
.widget-cat ul { list-style: none; }
.widget-cat li {
  padding: 4px 0; color: var(--text-dim); font-size: 0.88rem;
  border-bottom: 1px solid rgba(48,54,61,0.5);
}
.widget-cat li:last-child { border: none; }

/* Quick Start */
.quickstart-grid {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
  gap: 24px; margin-bottom: 32px;
}
.quickstart-option {
  background: var(--bg); border: 1px solid var(--border); border-radius: var(--radius);
  padding: 24px;
}
.quickstart-option h3 { font-size: 1rem; margin-bottom: 16px; color: var(--red); }
pre {
  background: #0a0e14; border-radius: var(--radius-sm); padding: 16px; overflow-x: hidden;
  font-size: 0.85rem; line-height: 1.7; word-break: break-all; white-space: pre-wrap;
}
code { font-family: "SF Mono", "Fira Code", "Cascadia Code", monospace; }
.prompt { color: var(--red); user-select: none; }
.quickstart-after { text-align: center; color: var(--text-dim); font-size: 0.95rem; }
.quickstart-after code { background: var(--bg-card); padding: 2px 8px; border-radius: 4px; font-size: 0.85rem; }
kbd {
  background: var(--bg-card); border: 1px solid var(--border); border-radius: 4px;
  padding: 1px 6px; font-size: 0.82rem; font-family: inherit;
}

/* CTA */
.cta-section { background: var(--bg-alt); }
.cta-inner {
  display: flex; align-items: center; gap: 48px;
}
.mascot { width: 200px; flex-shrink: 0; animation: float 3s ease-in-out infinite; }
.cta-inner h2 { font-size: 1.8rem; margin-bottom: 12px; }
.cta-inner p { color: var(--text-dim); margin-bottom: 24px; }

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

/* Footer */
.footer {
  border-top: 1px solid var(--border); padding: 24px 0;
}
.footer-inner {
  display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px;
}
.footer-left { display: flex; align-items: center; gap: 12px; font-size: 0.85rem; color: var(--text-dim); }
.footer-links { display: flex; gap: 20px; }
.footer-links a { color: var(--text-dim); font-size: 0.85rem; }
.footer-links a:hover { color: var(--text); }

/* Fade-in animations */
.fade-in {
  opacity: 0; transform: translateY(20px);
  animation: fadeIn 0.6s ease forwards;
}
.d1 { animation-delay: 0.15s; }
.d2 { animation-delay: 0.3s; }
.d3 { animation-delay: 0.45s; }
.d4 { animation-delay: 0.6s; }

@keyframes fadeIn {
  to { opacity: 1; transform: translateY(0); }
}

/* Themes Grid */
.themes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
  margin-top: 32px;
}
.theme-card {
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 12px;
  overflow: hidden;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}
.theme-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(0,0,0,0.4);
}
.theme-card img {
  width: 100%;
  height: 180px;
  object-fit: cover;
  object-position: top left;
  border-bottom: 1px solid var(--border);
}
.theme-card h4 {
  margin: 12px 16px 4px;
  font-size: 1.1rem;
}
.theme-card p {
  margin: 0 16px 16px;
  font-size: 0.85rem;
  color: var(--text-dim);
}

/* Lightbox */
.lightbox {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.92);
  z-index: 9999;
  justify-content: center;
  align-items: center;
  cursor: zoom-out;
}
.lightbox.open { display: flex; }
.lightbox img {
  max-width: 95vw;
  max-height: 95vh;
  border-radius: 8px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.6);
}
.lightbox-close {
  position: absolute;
  top: 20px;
  right: 30px;
  font-size: 40px;
  color: #fff;
  cursor: pointer;
  opacity: 0.7;
  transition: opacity 0.2s;
}
.lightbox-close:hover { opacity: 1; }

/* Responsive */
@media (max-width: 768px) {
  .nav-links { display: none; position: absolute; top: 60px; left: 0; right: 0; background: var(--bg); border-bottom: 1px solid var(--border); flex-direction: column; padding: 16px 24px; gap: 12px; }
  .nav-links.open { display: flex; }
  .nav-toggle { display: block; }
  .hero { padding: 120px 0 60px; }
  .hero-logo { width: 220px; }
  .cta-inner { flex-direction: column; text-align: center; }
  .mascot { width: 140px; }
  .quickstart-grid { grid-template-columns: 1fr; }
  .themes-grid { grid-template-columns: 1fr; }
}
```

## File: `TODO.md`
```markdown
# LobsterBoard TODO

## 🏗️ Architecture Ideas

### Head Widgets
Full-width widgets that span across the top of the page, above the main grid.
- Good for: market tickers, search bars, notification banners
- Implementation: separate render zone above main canvas
- Source: Glance dashboard

### Group Widget (Tabs)
Combine multiple widgets into a single tabbed container.
- Switch between widgets without taking more space
- Example: Reddit + HN + Lobsters in one widget with tabs
- Source: Glance dashboard

---

## 📊 Widget Ideas (from Glance)

### High Priority

- [ ] **Markets Widget**
  Stock/crypto ticker. Shows symbol, price, up/down with colors.
  Could be a head widget spanning full width.
  API: Yahoo Finance, Finnhub, or similar

- [ ] **Search Widget with Bangs**
  Search box with DuckDuckGo-style shortcuts.
  `!yt` → YouTube, `!gh` → GitHub, `!r` → Reddit
  Keyboard: `S` to focus, `↑` for last query
  Pure frontend, no API needed

- [ ] **Custom API Widget**
  Generic widget that fetches any JSON API and renders via template.
  User provides URL + template string.
  Unlocks infinite possibilities without new widget code.

- [ ] **DNS Stats (Pi-hole/AdGuard)**
  Blocked queries, total queries, % blocked, top blocked domains.
  API: Pi-hole Admin API or AdGuard Home API

- [ ] **Docker Containers**
  List running containers with status indicators (running/stopped/error).
  API: Docker socket or Portainer API

- [ ] **ChangeDetection.io**
  Shows tracked websites and recent changes.
  API: ChangeDetection.io REST API

### Medium Priority

- [ ] **Repository Widget**
  GitHub repo stats: stars, forks, open issues, last release, last commit.
  API: GitHub REST API (public, optional token for rate limits)

- [ ] **Twitch Channels**
  Live status, viewer counts for followed channels.
  API: Twitch Helix API (requires client ID)

- [ ] **Twitch Top Games**
  Current top games by viewership.
  API: Twitch Helix API

- [ ] **Videos Widget (YouTube)**
  Latest videos from subscribed channels.
  Supports custom frontend URLs (Invidious).
  API: YouTube RSS feeds (no API key needed) or Data API

- [ ] **Calendar Widget**
  Visual calendar with upcoming events.
  API: iCal feeds (Google, iCloud, Outlook)
  Note: Already have calendar access via OpenClaw, needs visual widget

- [ ] **RSS Feed Widget**
  Multiple display styles: vertical list, horizontal cards, detailed list.
  Aggregates multiple feeds.
  Needs CORS proxy (server already has one)

---

## 🎨 Rainmeter Ideas (NEEDS RE-RESEARCH)

Previous research from 2026-02-14 documented 25 widget ideas from Rainmeter skins.
File was lost (`lobsterboard-dev/WIDGET-IDEAS.md`).

**TODO:** Re-research popular Rainmeter skins and extract widget ideas:
- [ ] Browse DeviantArt Rainmeter section
- [ ] Check r/Rainmeter top posts
- [ ] Look at: Honeycomb, SUSPENDED, Elegance2, Mond, Fountain of Colors
- [ ] Focus on: visualizers, system monitors, launchers, info displays

---

## 🔧 Existing Widget Improvements

See `WIDGETS-STATUS.md` for current widget status and pending backends.

---

## 📝 Notes

- Skip Split Column layout — LobsterBoard already has flexible widget sizing/placement
- Icon libraries to consider: Simple Icons (`si:`), Material Design (`mdi:`), Dashboard Icons (`di:`)
- Glance source: https://github.com/glanceapp/glance/blob/main/docs/configuration.md
```

## File: `WIDGETS-STATUS.md`
```markdown
# LobsterBoard Widget Status

## ✅ Works Out of Box (no API needed)
- [x] weather - wttr.in (free, no key) - **VERIFIED**
- [x] weather-multi - wttr.in (free, no key) - **VERIFIED**
- [x] clock - pure JS - **VERIFIED**
- [x] world-clock - uses wttr.in for timezone - **VERIFIED**
- [x] countdown - date picker, hours/minutes options - **VERIFIED**
- [x] pomodoro - work/break times, sound notification - **VERIFIED**
- [x] image-local - file picker, embedded base64 - **VERIFIED**
- [x] image-embed - web URL input - **VERIFIED** (renamed to "Web Image")
- [x] image-random - multi-file picker, visual list, delete - **VERIFIED**
- [x] quick-links - add/delete interface, auto-favicons - **VERIFIED**
- [x] iframe-embed - URL field in properties - **VERIFIED**
- [x] release - GitHub public API, repo + version fields - **VERIFIED**

## ❤️ Health
- [ ] sleep-ring (Sleep Score) - health data API (Garmin, etc.)

## 🔑 User Provides API Key
- [ ] news-ticker - NewsAPI
- [ ] stock-ticker - Finnhub
- [ ] crypto-price - various free APIs
- [ ] github-stats - optional token for rate limits

## 🦞 OpenClaw Widgets (⚠️ Needs Custom API Backend)
- [ ] openclaw-release - fetches running version from /api/status + GitHub
- [ ] auth-status - /api/status
- [ ] activity-list - /api/activity
- [ ] cron-jobs - /api/cron
- [ ] system-log - /api/logs
- [ ] session-count - /api/sessions
- [ ] token-gauge - /api/usage/tokens
- [ ] api-status - checks OpenClaw + external

**⚠️ Note:** OpenClaw doesn't expose REST API endpoints. These widgets require a custom backend bridge that translates OpenClaw's WebSocket/CLI data to REST JSON. The `server.js` proxy alone is not enough.

## ⚠️ Needs Backend (Custom Setup Required)
- [x] ai-usage-claude - ✅ Server proxy + widget implemented (ANTHROPIC_ADMIN_KEY)
- [ ] ai-usage-openai - DROPPED (requires Admin API key, not available on all plans)
- ~~ai-usage-gemini~~ - ❌ DROPPED (no public usage API)
- ~~ai-usage-multi~~ - ❌ DROPPED (removed with gemini)
- [ ] ai-cost-tracker - aggregate costs endpoint
- [ ] cpu-memory - /api/system (system stats)
- [ ] disk-usage - /api/system (system stats)
- [ ] network-speed - system stats
- [ ] uptime-monitor - needs monitoring backend
- [ ] docker-containers - Docker API proxy
- [ ] todo-list - needs storage backend
- [ ] notes - needs storage backend
- [ ] email-count - email API proxy
- [ ] calendar - calendar API
- [ ] indoor-climate - smart home API
- [ ] power-usage - smart home API
- [ ] camera-feed - camera stream URL
- [ ] now-playing - music service API
- [ ] rss-ticker - may need CORS proxy
- [ ] rss-feed - may need CORS proxy
- [x] stat-card - REMOVED (static only, not useful)
- [ ] topbar - depends on configuration

---

## Notes
- Checkmarks in widget library indicate **VERIFIED** (tested and working)
- "Works Out of Box" = no backend needed, runs entirely in browser
- "User Provides API Key" = works if user adds their own API key
- "Needs OpenClaw" = requires OpenClaw gateway running locally
- "Needs Backend" = requires custom API endpoints to be built/configured
```

## File: `community-widgets/README.md`
```markdown
# 🦞 Community Widgets

Community widgets are user-contributed widgets for LobsterBoard. They follow the same format as built-in widgets but are developed and maintained by the community.

## How to Contribute

See [CONTRIBUTING.md](../bmad_repo/CONTRIBUTING.md) for full instructions on creating and submitting widgets.

**Quick start:** Copy the `_template/` folder, build your widget, and submit a PR.

## Available Community Widgets

| Widget | Description | Author |
|--------|-------------|--------|
| *(none yet — be the first!)* | | |

<!-- 
To add your widget to this list, submit a PR with the format:
| [Widget Name](./your-widget-name/) | Short description | [@yourname](https://github.com/yourname) |
-->
```

## File: `community-widgets/_template/README.md`
```markdown
# Widget Name

> Short one-line description of what the widget does.

## Screenshot

<!-- Replace with an actual screenshot of your widget on a LobsterBoard canvas -->
![Widget Preview](preview.png)

## Description

A longer explanation of your widget — what it shows, why it's useful, and any context a user needs.

## Configuration Options

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `title` | string | `"Widget Name"` | Display title |
| `refreshInterval` | number | `60` | Seconds between data refreshes |
| `apiKey` | string | `YOUR_API_KEY_HERE` | API key for the service (if needed) |

## API Requirements

<!-- Remove this section if your widget doesn't need an API key -->

This widget requires an API key from [Service Name](https://example.com).

1. Sign up at https://example.com
2. Generate an API key
3. Paste it into the widget's property panel

**Free tier:** Describe rate limits or free tier details.

## Example Usage

Describe a typical use case. For example:

> Add this widget to your dashboard to track X. Set the `location` property to your city and it will auto-update every 10 minutes.

## Author

- **Your Name** — [@yourname](https://github.com/yourname)

## License

This widget is contributed under the same license as LobsterBoard (BSL-1.1).
```

## File: `community-widgets/_template/widget.js`
```javascript
/**
 * Community Widget Template — LobsterBoard
 * 
 * Copy this file into your widget folder and modify it.
 * Your widget object must follow the exact same format as widgets in js/widgets.js.
 * 
 * This example creates a "Custom Counter" widget that counts up every second.
 */

const myWidget = {
  // ── Required metadata ──────────────────────────────────────────

  // Display name shown in the widget picker sidebar
  name: 'Custom Counter',

  // Emoji icon shown next to the name
  icon: '🔢',

  // Category determines default sizing behavior:
  //   'small' — KPI cards (compact, single-value display)
  //   'large' — Lists, logs, multi-row content
  //   'bar'   — Full-width horizontal bars
  category: 'small',

  // Short description shown in the widget picker
  description: 'A simple counter that increments every second. Use as a starting point for your own widget.',

  // Default dimensions in pixels (user can resize)
  defaultWidth: 200,
  defaultHeight: 120,

  // Set to true if your widget requires an API key.
  // When true, the property panel will show a key input field.
  hasApiKey: false,
  // apiKeyName: 'MY_SERVICE_API',  // Uncomment if hasApiKey is true

  // ── Properties ─────────────────────────────────────────────────
  // These become editable fields in the property panel (right sidebar).
  // Users can change these values per widget instance.
  // Use descriptive defaults. Types are inferred from the default value:
  //   string → text input
  //   number → number input
  //   boolean → checkbox (not commonly used)
  properties: {
    title: 'Custom Counter',         // Widget title
    startValue: 0,                   // Starting count
    refreshInterval: 1,              // Seconds between updates
    // API_KEY='[REDACTED_API_KEY]',  // Uncomment if your widget needs an API key
  },

  // ── Preview ────────────────────────────────────────────────────
  // Static HTML snippet shown in the widget picker sidebar.
  // Keep it small; this is just a visual hint, not a live widget.
  preview: `<div style="text-align:center;padding:8px;">
    <div style="font-size:24px;">42</div>
    <div style="font-size:11px;color:#8b949e;">Custom Counter</div>
  </div>`,

  // ── generateHtml(props) ────────────────────────────────────────
  // Returns an HTML string that is injected into the widget container.
  //
  // IMPORTANT:
  //   • Use props.id as a prefix for ALL element IDs.
  //     Multiple instances of the same widget can exist on the canvas,
  //     so IDs must be unique. Pattern: id="${props.id}-myElement"
  //   • Use CSS classes from the theme (dash-card, dash-card-head, etc.)
  //   • Use CSS variables for colors: var(--bg-primary), var(--text-primary),
  //     var(--accent-blue), var(--accent-green), var(--border-color), etc.
  generateHtml: (props) => `
    <div class="dash-card" id="widget-${props.id}" style="height:100%;">
      <div class="dash-card-head">
        <span class="dash-card-title">🔢 ${props.title || 'Custom Counter'}</span>
      </div>
      <div class="dash-card-body" style="display:flex;align-items:center;justify-content:center;">
        <div>
          <div class="kpi-value blue" id="${props.id}-value">${props.startValue || 0}</div>
          <div class="kpi-label" id="${props.id}-label">counting...</div>
        </div>
      </div>
    </div>`,

  // ── generateJs(props) ──────────────────────────────────────────
  // Returns a JavaScript string that executes in the browser (via new Function).
  //
  // This is where you:
  //   • Fetch data from APIs
  //   • Update DOM elements created by generateHtml
  //   • Set up refresh intervals
  //
  // IMPORTANT:
  //   • The JS runs in global scope — use unique function names.
  //     Pattern: functionName_${props.id.replace(/-/g, '_')}
  //   • Reference elements by the IDs you created in generateHtml.
  //   • Handle errors gracefully — show "—" or a friendly message, never crash.
  //   • For API keys: reference them via props (e.g., props.apiKey).
  //     NEVER hardcode real keys in your widget file.
  generateJs: (props) => `
    // Counter Widget: ${props.id}
    (function() {
      let count = ${props.startValue || 0};
      const valEl = document.getElementById('${props.id}-value');
      const labelEl = document.getElementById('${props.id}-label');

      function update_${props.id.replace(/-/g, '_')}() {
        count++;
        if (valEl) valEl.textContent = count;
        if (labelEl) labelEl.textContent = 'counting...';
      }

      // Initial display is already set by generateHtml.
      // Set up the refresh interval (in seconds → milliseconds).
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 1) * 1000});
    })();
  `
};

// ── How this gets used ───────────────────────────────────────────
// When your widget is accepted, a maintainer will add it to the WIDGETS
// object in js/widgets.js with a unique key, like:
//
//   'community-custom-counter': { ...myWidget }
//
// You don't need to do this yourself — just provide the widget object.

export default myWidget;
```

## File: `css/builder.css`
```css
/* OpenClaw Dashboard Builder - Styles */

:root {
  --bg-primary: #0d1117;
  --bg-secondary: #161b22;
  --bg-tertiary: #21262d;
  --bg-hover: #30363d;
  --border: #30363d;
  --text-primary: #e6edf3;
  --text-secondary: #8b949e;
  --text-muted: #6e7681;
  --accent-blue: #58a6ff;
  --accent-green: #3fb950;
  --accent-orange: #d29922;
  --accent-red: #f85149;
  --accent-purple: #a371f7;
  --font-scale: 1;
}

.canvas {
  font-size: calc(14px * var(--font-scale));
}

.canvas .placed-widget {
  font-size: calc(1em);
}

.canvas .kpi-value {
  font-size: calc(24px * var(--font-scale)) !important;
}

.canvas .kpi-label {
  font-size: calc(11px * var(--font-scale)) !important;
}

.canvas .dash-card-title {
  font-size: calc(12px * var(--font-scale)) !important;
}

.canvas .dash-card-badge {
  font-size: calc(11px * var(--font-scale)) !important;
}

.canvas .dash-card-body {
  font-size: calc(13px * var(--font-scale)) !important;
}

.canvas .uptime-row,
.canvas .docker-row,
.canvas .sys-row {
  font-size: calc(12px * var(--font-scale));
}

.canvas .weather-row,
.canvas .tz-row,
.canvas .net-row {
  font-size: calc(13px * var(--font-scale));
}

.canvas .widget-icon,
.canvas .weather-icon {
  font-size: calc(1em * var(--font-scale));
}

/* Disk ring and network values */
.canvas .kpi-ring-label {
  font-size: calc(11px * var(--font-scale)) !important;
}

.canvas .kpi-data .kpi-label {
  font-size: calc(11px * var(--font-scale)) !important;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: var(--bg-primary);
  color: var(--text-primary);
  height: 100vh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

/* Header */
.builder-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 20px;
  background: var(--bg-secondary);
  border-bottom: 1px solid var(--border);
  gap: 20px;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 24px;
}

.header-left .logo-img {
  height: 40px;
  width: auto;
}

.header-nav {
  display: flex;
  gap: 16px;
}

.header-nav .nav-link {
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 13px;
  transition: color 0.2s;
}

.header-nav .nav-link:hover {
  color: var(--text-primary);
}

.header-center {
  display: flex;
  align-items: center;
  gap: 10px;
}

.header-center label {
  color: var(--text-secondary);
  font-size: 13px;
}

.header-center select,
.header-center input {
  background: var(--bg-tertiary);
  border: 1px solid var(--border);
  color: var(--text-primary);
  padding: 6px 10px;
  border-radius: 6px;
  font-size: 13px;
}

.header-right {
  display: flex;
  gap: 10px;
}

/* Buttons */
.btn {
  padding: 8px 16px;
  border: none;
  border-radius: 6px;
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.15s ease;
}

.btn-primary {
  background: var(--accent-green);
  color: #000;
}

.btn-primary:hover {
  background: #46c05a;
}

.btn-secondary {
  background: var(--bg-tertiary);
  color: var(--text-primary);
  border: 1px solid var(--border);
}

.btn-secondary:hover {
  background: var(--bg-hover);
}

.btn-danger {
  background: var(--accent-red);
  color: #fff;
}

.btn-danger:hover {
  background: #ff6b61;
}

.btn-sm {
  padding: 6px 12px;
  font-size: 12px;
  width: 100%;
}

.btn-done {
  background: var(--accent-blue);
  color: #fff;
  font-weight: 600;
}

.btn-done:hover {
  background: #6cb3fa;
}

/* Main Layout */
.builder-main {
  display: flex;
  flex: 1;
  overflow: hidden;
}

/* Widget Panel */
.widget-panel {
  width: 260px;
  min-width: 260px;
  background: var(--bg-secondary);
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  max-height: calc(100vh - 60px);
}

.widget-panel > h3 {
  padding: 16px 16px 12px 16px;
  margin: 0;
  flex-shrink: 0;
}

.widget-sections {
  flex: 1;
  overflow-y: auto;
  padding: 0 16px 16px 16px;
  min-height: 0;
}

.widget-panel h3 {
  font-size: 14px;
  color: var(--text-secondary);
  margin-bottom: 16px;
}

.widget-section {
  margin-bottom: 20px;
}

.widget-section h4 {
  font-size: 11px;
  text-transform: uppercase;
  color: var(--text-muted);
  margin-bottom: 10px;
  letter-spacing: 0.5px;
}

.widget-list {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.widget-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  background: var(--bg-tertiary);
  border: 1px solid var(--border);
  border-radius: 8px;
  cursor: grab;
  transition: all 0.15s ease;
}

.widget-item:hover {
  background: var(--bg-hover);
  border-color: var(--accent-blue);
}

.widget-item:active {
  cursor: grabbing;
}

.widget-item.dragging {
  opacity: 0.5;
}

.widget-icon {
  font-size: 18px;
}

.widget-name {
  font-size: 13px;
  color: var(--text-primary);
}

.widget-verified {
  margin-left: auto;
  font-size: 12px;
  color: var(--accent-green);
  background: rgba(63, 185, 80, 0.15);
  padding: 2px 6px;
  border-radius: 4px;
  font-weight: 600;
}

/* Canvas Area */
.canvas-area {
  flex: 1;
  display: flex;
  flex-direction: column;
  background: var(--bg-primary);
  overflow: hidden;
}

.canvas-wrapper {
  flex: 1;
  display: block;
  padding: 40px;
  overflow: auto;
  background: 
    radial-gradient(circle at center, var(--bg-secondary) 0%, var(--bg-primary) 100%);
  min-width: 0;
  min-height: 0;
}

.canvas {
  position: relative;
  background: var(--bg-primary);
  border: 2px solid var(--border);
  border-radius: 8px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.5);
  transform-origin: top left;
  transition: transform 0.2s ease;
  margin: auto;
}

.canvas-grid {
  position: absolute;
  inset: 0;
  background-image: 
    linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
  background-size: 20px 20px;
  pointer-events: none;
  border-radius: 6px;
}

.drop-hint {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-muted);
  font-size: 18px;
  pointer-events: none;
  opacity: 0.5;
}

.canvas.has-widgets .drop-hint {
  display: none;
}

.canvas.drag-over {
  border-color: var(--accent-blue);
  box-shadow: 0 0 0 4px rgba(88, 166, 255, 0.2);
}

.canvas-info {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 30px;
  padding: 10px;
  background: var(--bg-secondary);
  border-top: 1px solid var(--border);
  font-size: 12px;
  color: var(--text-secondary);
}

.zoom-controls {
  display: flex;
  align-items: center;
  gap: 4px;
}

.zoom-btn {
  width: 24px;
  height: 24px;
  background: transparent;
  border: none;
  border-radius: 4px;
  color: var(--text-secondary);
  font-size: 14px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.15s ease;
}

.zoom-btn:hover {
  background: var(--bg-tertiary);
  color: var(--text-primary);
}

#zoom-level {
  min-width: 40px;
  text-align: center;
  color: var(--text-secondary);
  font-size: 12px;
}

/* Placed Widgets on Canvas */
.placed-widget {
  position: absolute;
  background: #1c2230;
  border: 1px solid #3a4150;
  border-radius: 8px;
  cursor: move;
  overflow: hidden;
  transition: box-shadow 0.15s ease;
  box-shadow: 0 2px 8px rgba(0,0,0,0.4);
}

.placed-widget:hover {
  box-shadow: 0 0 0 2px var(--accent-blue);
}

.placed-widget.selected {
  box-shadow: 0 0 0 2px var(--accent-green);
}

.placed-widget .widget-render {
  width: 100%;
  height: 100%;
  pointer-events: none;
}

.placed-widget .resize-handle {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 16px;
  height: 16px;
  cursor: se-resize;
  background: linear-gradient(135deg, transparent 50%, var(--accent-blue) 50%);
  border-radius: 0 0 6px 0;
  opacity: 0;
  transition: opacity 0.15s;
  z-index: 10;
}

.placed-widget:hover .resize-handle,
.placed-widget.selected .resize-handle {
  opacity: 1;
}

/* Widget Styles for Canvas Preview */
.placed-widget .kpi-card {
  background: var(--bg-secondary);
  border: none;
  border-radius: 8px;
  padding: 12px;
  display: flex;
  align-items: center;
  gap: 12px;
  height: 100%;
}

.placed-widget .kpi-sm {
  padding: 10px;
}

.placed-widget .kpi-icon {
  font-size: 24px;
}

.placed-widget .kpi-data {
  flex: 1;
}

.placed-widget .kpi-value {
  font-size: 20px;
  font-weight: 600;
  color: var(--text-primary);
}

.placed-widget .kpi-value.blue { color: var(--accent-blue); }
.placed-widget .kpi-value.green { color: var(--accent-green); }
.placed-widget .kpi-value.orange { color: var(--accent-orange); }
.placed-widget .kpi-value.red { color: var(--accent-red); }

.placed-widget .kpi-label {
  font-size: 11px;
  color: var(--text-secondary);
  margin-top: 2px;
}

.placed-widget .kpi-indicator {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--text-muted);
}

.placed-widget .kpi-indicator.green { background: var(--accent-green); }
.placed-widget .kpi-indicator.yellow { background: var(--accent-orange); }
.placed-widget .kpi-indicator.red { background: var(--accent-red); }

/* Ring */
.placed-widget .kpi-ring-wrap {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.placed-widget .kpi-ring-sm {
  width: 48px;
  height: 48px;
}

.placed-widget .kpi-ring {
  width: 100%;
  height: 100%;
}

.placed-widget .kpi-ring-label {
  position: absolute;
  font-size: 12px;
  font-weight: 600;
  color: var(--text-primary);
}

/* Dash Cards */
.placed-widget .dash-card {
  background: var(--bg-secondary);
  border: none;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  height: 100%;
  overflow: hidden;
}

.placed-widget .dash-card-head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 14px;
  border-bottom: 1px solid var(--border);
  background: var(--bg-tertiary);
}

.placed-widget .dash-card-title {
  font-size: 12px;
  font-weight: 600;
  color: var(--text-primary);
}

.placed-widget .dash-card-badge {
  font-size: 10px;
  color: var(--text-secondary);
  background: var(--bg-primary);
  padding: 2px 6px;
  border-radius: 10px;
}

.placed-widget .dash-card-body {
  flex: 1;
  padding: 10px 14px;
  overflow-y: auto;
  font-size: 11px;
  color: var(--text-secondary);
}

/* Top Bar */
.placed-widget .topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 16px;
  background: var(--bg-secondary);
  height: 100%;
}

.placed-widget .topbar-left {
  display: flex;
  align-items: center;
  gap: 16px;
}

.placed-widget .topbar-brand {
  font-weight: 600;
  font-size: 13px;
  color: var(--text-primary);
}

.placed-widget .topbar-link {
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 12px;
}

.placed-widget .topbar-link.active {
  color: var(--accent-blue);
}

.placed-widget .topbar-right {
  display: flex;
  align-items: center;
  gap: 10px;
}

.placed-widget .topbar-meta {
  font-size: 11px;
  color: var(--text-muted);
}

.placed-widget .topbar-refresh {
  background: var(--bg-tertiary);
  border: 1px solid var(--border);
  color: var(--text-secondary);
  padding: 3px 6px;
  border-radius: 4px;
  font-size: 12px;
}

/* News Ticker */
/* RSS Ticker - override placed-widget styles */
.placed-widget[data-type="rss-ticker"] {
  border-radius: 4px;
  background: #0d1117;
}

.news-ticker-wrap {
  display: flex;
  align-items: center;
  background: #0d1117;
  overflow: hidden;
  height: 100%;
  padding: 0 8px;
}

.ticker-label {
  flex-shrink: 0;
  font-size: calc(14px * var(--font-scale, 1));
  margin-right: 10px;
}

.ticker-track {
  flex: 1;
  overflow: hidden;
  position: relative;
}

.ticker-content {
  display: inline-block;
  white-space: nowrap;
  padding-left: 100%;
  animation: ticker-scroll 60s linear infinite;
  font-size: calc(13px * var(--font-scale, 1));
  color: #c9d1d9;
}

@keyframes ticker-scroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-100%); }
}

.ticker-link {
  color: #c9d1d9;
  text-decoration: none;
  transition: color 0.2s;
}
.ticker-link:hover {
  color: #58a6ff;
}
.ticker-sep {
  color: #484f58;
  margin: 0 30px;
}

/* Loading */
.placed-widget .loading-sm {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 16px;
  color: var(--text-muted);
  font-size: 11px;
}

.placed-widget .spinner-sm {
  width: 16px;
  height: 16px;
  border: 2px solid var(--bg-tertiary);
  border-top-color: var(--accent-blue);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Properties Panel */
.properties-panel {
  width: 280px;
  background: var(--bg-secondary);
  border-left: 1px solid var(--border);
  padding: 16px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  position: relative;
}

.properties-panel h3 {
  font-size: 14px;
  color: var(--text-secondary);
  margin-bottom: 16px;
}

.no-selection {
  color: var(--text-muted);
  font-size: 13px;
  text-align: center;
  padding: 40px 20px;
}

.prop-group {
  margin-bottom: 16px;
}

.prop-group label {
  display: block;
  font-size: 11px;
  text-transform: uppercase;
  color: var(--text-muted);
  margin-bottom: 6px;
  letter-spacing: 0.5px;
}

.prop-group input,
.prop-group select {
  width: 100%;
  padding: 8px 10px;
  background: var(--bg-tertiary);
  border: 1px solid var(--border);
  border-radius: 6px;
  color: var(--text-primary);
  font-size: 13px;
}

.prop-group input:focus,
.prop-group select:focus {
  outline: none;
  border-color: var(--accent-blue);
}

.prop-group input[readonly] {
  color: var(--text-secondary);
  cursor: default;
}

.prop-group small {
  display: block;
  margin-top: 4px;
  font-size: 11px;
  color: var(--text-muted);
}

.prop-row {
  display: flex;
  gap: 8px;
}

.prop-row input {
  flex: 1;
}

.properties-panel hr {
  border: none;
  border-top: 1px solid var(--border);
  margin: 20px 0;
}

/* Modal */
.modal {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.8);
  z-index: 1000;
  align-items: center;
  justify-content: center;
}

.modal.active {
  display: flex;
}

.modal-content {
  background: var(--bg-secondary);
  border-radius: 12px;
  max-width: 90vw;
  max-height: 90vh;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.modal-fullscreen {
  width: 95vw;
  height: 95vh;
}

.modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 20px;
  border-bottom: 1px solid var(--border);
}

.modal-header h2 {
  font-size: 16px;
  font-weight: 600;
}

.modal-close {
  background: none;
  border: none;
  color: var(--text-secondary);
  font-size: 24px;
  cursor: pointer;
  padding: 0 8px;
}

.modal-close:hover {
  color: var(--text-primary);
}

.modal-body {
  flex: 1;
  overflow: auto;
}

.modal-body iframe {
  width: 100%;
  height: 100%;
  border: none;
  background: var(--bg-primary);
}

/* Utility */
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: var(--bg-primary);
}

::-webkit-scrollbar-thumb {
  background: var(--bg-tertiary);
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: var(--bg-hover);
}

/* Pomodoro Button */
.pomo-btn {
  background: var(--bg-tertiary);
  border: 1px solid var(--border);
  color: var(--text-primary);
  padding: 8px 20px;
  border-radius: 6px;
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.15s ease;
}

.pomo-btn:hover {
  background: var(--bg-hover);
  border-color: var(--accent-blue);
  color: var(--accent-blue);
}

.pomo-btn:active {
  background: var(--bg-secondary);
}

/* Mascot at bottom of sidebar */
.sidebar-mascot {
  flex-shrink: 0;
  padding: 20px;
  text-align: center;
  border-top: 1px solid var(--border);
  background: var(--bg-secondary);
  min-height: 180px;
  margin-top: auto;
}

.sidebar-mascot img {
  width: 85%;
  max-width: 200px;
  height: auto;
  opacity: 0.9;
}

/* ============================================
   System Widget Styles
   ============================================ */

.uptime-row, .docker-row, .sys-row, .net-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 4px 8px;
  font-size: calc(12px * var(--font-scale));
}

.uptime-row + .uptime-row,
.docker-row + .docker-row,
.sys-row + .sys-row,
.net-row + .net-row {
  border-top: 1px solid var(--border);
}

.uptime-pct, .docker-status {
  font-weight: 600;
  margin-left: 16px;
}

/* Weather rows */
.weather-row {
  display: flex;
  align-items: center;
  padding: 4px 8px;
  font-size: calc(13px * var(--font-scale));
}

.weather-row + .weather-row {
  border-top: 1px solid var(--border);
}

.weather-icon {
  margin-right: 10px;
  font-size: calc(16px * var(--font-scale));
}

.weather-loc {
  flex: 1;
  margin-right: 12px;
}

.weather-temp {
  font-weight: 600;
  white-space: nowrap;
}

/* Timezone / World Clock rows */
.tz-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 4px 8px;
  font-size: calc(13px * var(--font-scale));
}

.tz-row + .tz-row {
  border-top: 1px solid var(--border);
}

.tz-city {
  flex: 1;
  margin-right: 16px;
}

.tz-time {
  font-weight: 600;
  white-space: nowrap;
  color: var(--accent-blue);
}

/* ============================================
   Edit Mode / View Mode Overrides
   ============================================ */

body[data-mode="view"] .builder-header,
body[data-mode="view"] .widget-panel,
body[data-mode="view"] .properties-panel,
body[data-mode="view"] .canvas-info {
  display: none;
}

body[data-mode="view"] .builder-main {
  flex-direction: column;
}

body[data-mode="view"] .canvas-wrapper {
  flex: 1;
  padding: 0;
  background: var(--bg-primary);
  display: flex;
  align-items: flex-start;
  justify-content: center;
  overflow: hidden;
  width: 100vw;
  height: 100vh;
}

/* Scrollable canvas mode */
body.canvas-scrollable {
  overflow-y: auto !important;
  height: auto !important;
}

body.canvas-scrollable[data-mode="view"] .canvas-wrapper {
  overflow: visible;
  height: auto;
}

body.canvas-scrollable[data-mode="view"] .builder-main {
  overflow: visible;
}

body.canvas-scrollable[data-mode="view"] .canvas-area {
  overflow: visible;
}

body[data-mode="view"] .canvas {
  margin: 0;
  border: none;
  border-radius: 0;
  box-shadow: none;
  transform-origin: top left;
  /* Scale is set dynamically by JS */
}

body[data-mode="view"] .canvas-grid,
body[data-mode="view"] .drop-hint {
  display: none;
}

/* Empty state hint in view mode */
.view-empty-hint {
  display: none;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  color: var(--text-muted);
  pointer-events: none;
  z-index: 10;
}

.view-empty-hint .hint-icon {
  font-size: 48px;
  margin-bottom: 16px;
  opacity: 0.4;
}

.view-empty-hint .hint-text {
  font-size: 18px;
  margin-bottom: 8px;
  color: var(--text-secondary);
}

.view-empty-hint .hint-shortcut {
  font-size: 14px;
  color: var(--text-muted);
}

.view-empty-hint kbd {
  background: var(--bg-tertiary);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 2px 8px;
  font-family: inherit;
  font-size: 13px;
  color: var(--text-secondary);
}

body[data-mode="view"].empty-dashboard .view-empty-hint {
  display: block;
}

body[data-mode="view"] .placed-widget {
  border: none;
  box-shadow: none;
  cursor: default;
}

body[data-mode="view"] .placed-widget:hover {
  box-shadow: none;
}

body[data-mode="view"] .placed-widget.selected {
  box-shadow: none;
}

body[data-mode="view"] .placed-widget .resize-handle {
  display: none;
}

body[data-mode="view"] .placed-widget .widget-render {
  pointer-events: auto;
}

/* Edit Layout Button (view mode) */
.edit-layout-btn {
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 999;
  background: var(--accent-blue);
  color: #fff;
  padding: 12px 24px;
  font-size: 16px;
  font-weight: 600;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.3);
  display: none;
}

.edit-layout-btn:hover {
  background: #6cb3fa;
}

body[data-mode="view"] .edit-layout-btn {
  display: block;
}

body[data-mode="edit"] .edit-layout-btn {
  display: none;
}

/* Line widgets: transparent container, no chrome */
.placed-widget[data-type="horizontal-line"],
.placed-widget[data-type="vertical-line"] {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  border-radius: 0 !important;
  padding: 0 !important;
}

.placed-widget[data-type="horizontal-line"] .widget-render,
.placed-widget[data-type="vertical-line"] .widget-render {
  padding: 0 !important;
  margin: 0 !important;
  overflow: visible !important;
}

/* Text-header widgets: hide card chrome when showBorder is false */
.placed-widget[data-show-border="false"] {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  border-radius: 0 !important;
}

.placed-widget[data-show-border="false"] .widget-render {
  padding: 0 !important;
  margin: 0 !important;
}

.placed-widget[data-show-border="false"] .dash-card {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
}

.placed-widget[data-show-border="false"] .dash-card-head {
  display: none !important;
}

.placed-widget[data-show-border="false"] .dash-card-body {
  padding: 0 !important;
}

/* no-bg removed — using data-show-border instead */

/* ── Template Gallery ── */
.tpl-modal-overlay {
  position: fixed; inset: 0; z-index: 10000;
  background: rgba(0,0,0,0.7); backdrop-filter: blur(4px);
  display: flex; align-items: center; justify-content: center;
  animation: tplFadeIn 0.2s ease;
}
@keyframes tplFadeIn { from { opacity: 0; } to { opacity: 1; } }

.tpl-modal {
  background: #0d1117; border: 1px solid #30363d; border-radius: 12px;
  width: 90vw; max-width: 900px; max-height: 85vh;
  display: flex; flex-direction: column; overflow: hidden;
  box-shadow: 0 20px 60px rgba(0,0,0,0.5);
}
.tpl-modal-sm { max-width: 480px; }

.tpl-modal-header {
  display: flex; align-items: center; gap: 12px;
  padding: 16px 20px; border-bottom: 1px solid #30363d;
}
.tpl-modal-header h2 { margin: 0; font-size: 18px; color: #e6edf3; white-space: nowrap; }
.tpl-search {
  flex: 1; background: #161b22; border: 1px solid #30363d; border-radius: 6px;
  padding: 6px 12px; color: #e6edf3; font-size: 14px; outline: none;
}
.tpl-search:focus { border-color: #58a6ff; }
.tpl-close-btn {
  background: none; border: none; color: #8b949e; font-size: 24px;
  cursor: pointer; padding: 0 4px; line-height: 1;
}
.tpl-close-btn:hover { color: #e6edf3; }

.tpl-modal-body {
  padding: 20px; overflow-y: auto; flex: 1;
  display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 16px; align-content: start;
}

.tpl-empty {
  grid-column: 1 / -1; text-align: center; color: #8b949e;
  padding: 60px 20px; font-size: 16px;
}

.tpl-card {
  background: #161b22; border: 1px solid #30363d; border-radius: 8px;
  overflow: hidden; cursor: pointer; transition: border-color 0.2s, transform 0.2s;
}
.tpl-card:hover { border-color: #58a6ff; transform: translateY(-2px); }

.tpl-card-img {
  height: 140px; background: #0d1117; display: flex; align-items: center; justify-content: center;
  overflow: hidden;
}
.tpl-card-img img { width: 100%; height: 100%; object-fit: cover; }
.tpl-no-preview { font-size: 48px; opacity: 0.3; }

.tpl-card-body { padding: 12px; }
.tpl-card-body h3 { margin: 0 0 4px; font-size: 15px; color: #e6edf3; }
.tpl-card-body p { margin: 0 0 8px; font-size: 13px; color: #8b949e; line-height: 1.4; }

.tpl-card-meta { display: flex; gap: 12px; font-size: 12px; color: #8b949e; margin-bottom: 8px; }
.tpl-card-tags { display: flex; flex-wrap: wrap; gap: 4px; }
.tpl-tag {
  background: #1f2937; color: #58a6ff; padding: 2px 8px; border-radius: 10px;
  font-size: 11px;
}

/* Detail view */
.tpl-detail { padding: 20px; overflow-y: auto; }
.tpl-back-btn {
  background: none; border: none; color: #58a6ff; cursor: pointer;
  font-size: 14px; padding: 0; margin-bottom: 16px;
}
.tpl-back-btn:hover { text-decoration: underline; }

.tpl-detail-content { display: flex; gap: 24px; }
.tpl-detail-img {
  width: 400px; max-width: 50%; border-radius: 8px; object-fit: cover;
  background: #161b22; border: 1px solid #30363d;
}
.tpl-detail-info { flex: 1; }
.tpl-detail-info h2 { margin: 0 0 8px; color: #e6edf3; }
.tpl-detail-info p { color: #8b949e; margin: 0 0 16px; }
.tpl-detail-info div { color: #c9d1d9; font-size: 14px; margin-bottom: 4px; }

.tpl-detail-actions { margin-top: 20px; display: flex; gap: 12px; }
.tpl-detail-actions .btn { padding: 10px 20px; }

/* Export form */
.tpl-form { display: flex; flex-direction: column; gap: 8px; }
.tpl-form label { color: #8b949e; font-size: 13px; margin-top: 4px; }
.tpl-input {
  background: #161b22; border: 1px solid #30363d; border-radius: 6px;
  padding: 8px 12px; color: #e6edf3; font-size: 14px; font-family: inherit;
  outline: none; resize: vertical;
}
.tpl-input:focus { border-color: #58a6ff; }

.tpl-export-result {
  margin-top: 12px; padding: 12px; border-radius: 6px; font-size: 14px;
  line-height: 1.5;
}
.tpl-export-success { background: #0d2818; border: 1px solid #238636; color: #3fb950; }
.tpl-export-error { background: #2d1215; border: 1px solid #da3633; color: #f85149; }
.tpl-export-result code { background: #30363d; padding: 2px 6px; border-radius: 4px; }

/* ─────────────────────────────────────────────
   PIN Modal & Security Settings
   ───────────────────────────────────────────── */
.pin-modal-overlay {
  position: fixed; inset: 0; z-index: 9999;
  background: rgba(0,0,0,0.7); backdrop-filter: blur(4px);
  display: flex; align-items: center; justify-content: center;
}
.pin-modal {
  background: #161b22; border: 1px solid #30363d; border-radius: 12px;
  padding: 24px; min-width: 320px; max-width: 360px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.6);
}
.pin-modal h3 { margin: 0 0 16px; color: #e6edf3; font-size: 18px; }
.pin-group { margin-bottom: 12px; }
.pin-group label { display: block; color: #8b949e; font-size: 12px; margin-bottom: 4px; }
.pin-input {
  width: 100%; padding: 10px 12px; background: #0d1117; border: 1px solid #30363d;
  border-radius: 6px; color: #e6edf3; font-size: 20px; letter-spacing: 8px;
  text-align: center; box-sizing: border-box;
}
.pin-input:focus { border-color: #58a6ff; outline: none; }
.pin-error { color: #f85149; font-size: 12px; min-height: 18px; margin: 8px 0; }
.pin-actions { display: flex; gap: 8px; justify-content: flex-end; margin-top: 16px; }
.security-option {
  padding: 12px; background: #0d1117; border-radius: 8px; border: 1px solid #21262d;
}
.security-option-header {
  display: flex; justify-content: space-between; align-items: center;
}
.security-badge {
  font-size: 11px; padding: 2px 8px; border-radius: 10px;
  background: #21262d; color: #8b949e;
}
.security-badge.active { background: #0d2818; color: #3fb950; }
.security-buttons { display: flex; gap: 6px; }

/* Toggle switch */
.toggle-switch { position: relative; display: inline-block; width: 42px; height: 22px; }
.toggle-switch input { opacity: 0; width: 0; height: 0; }
.toggle-slider {
  position: absolute; cursor: pointer; inset: 0;
  background: #21262d; border-radius: 22px; transition: 0.3s;
}
.toggle-slider:before {
  content: ""; position: absolute; height: 16px; width: 16px;
  left: 3px; bottom: 3px; background: #8b949e;
  border-radius: 50%; transition: 0.3s;
}
.toggle-switch input:checked + .toggle-slider { background: #238636; }
.toggle-switch input:checked + .toggle-slider:before { transform: translateX(20px); background: #fff; }

/* Masked secret field in properties */
.secret-field-wrapper {
  display: flex; align-items: center; gap: 6px;
}
.secret-field-wrapper input { flex: 1; }
.secret-replace-btn {
  padding: 4px 8px; background: #21262d; border: 1px solid #30363d;
  border-radius: 4px; color: #8b949e; cursor: pointer; font-size: 11px; white-space: nowrap;
}
.secret-replace-btn:hover { background: #30363d; color: #e6edf3; }

/* Hide page links in edit mode to reduce header clutter */
body[data-mode="edit"] .page-link,
body[data-mode="edit"] .page-separator {
  display: none !important;
}
```

## File: `css/themes.css`
```css
/* LobsterBoard Theme System
   =========================
   Themes override :root CSS custom properties via body class.
   Default theme (dark GitHub-style) is defined in builder.css :root
   
   Available themes:
   - (none/default) - Dark GitHub-style
   - .theme-feminine - Pastel pink/lavender 
   - .theme-terminal - Green phosphor CRT
   - .theme-paper    - Light cream/sepia
*/

/* ============================================
   Phosphor Icons Font (for terminal theme)
   ============================================ */
@font-face {
  font-family: "Phosphor-Light";
  src: url("../fonts/Phosphor-Light.woff2") format("woff2"),
       url("../fonts/Phosphor-Light.woff") format("woff");
  font-weight: normal;
  font-style: normal;
  font-display: swap;
}

/* ============================================
   Feminine Theme - Pastel Pink & Lavender
   Extracted from PR #7
   ============================================ */
.theme-feminine {
  --bg-primary: #fdf4f8;
  --bg-secondary: #ffffff;
  --bg-tertiary: #fce8f2;
  --bg-hover: #f9d5e8;
  --border: #f0c2d8;
  --border-soft: #f5d6e8;
  --text-primary: #3b1f30;
  --text-secondary: #7a4060;
  --text-muted: #b07a95;
  --accent-blue: #7c5dc7;
  --accent-green: #10b981;
  --accent-orange: #f59e0b;
  --accent-red: #f43f6e;
  --accent-purple: #9b6cd8;
  --accent-pink: #e8478f;
  --accent-rose: #f43f6e;
  --accent-lavender: #9b6cd8;
  --glow-pink: rgba(232, 71, 143, 0.15);
  --glow-purple: rgba(155, 108, 216, 0.12);
}

/* Feminine theme-specific overrides */
.theme-feminine body,
body.theme-feminine {
  background-image:
    radial-gradient(ellipse at 15% 0%, rgba(232, 71, 143, 0.07) 0%, transparent 50%),
    radial-gradient(ellipse at 85% 100%, rgba(155, 108, 216, 0.06) 0%, transparent 50%);
}

.theme-feminine .builder-header {
  box-shadow: 0 2px 16px rgba(180, 80, 130, 0.08), 0 1px 0 rgba(232, 71, 143, 0.1);
}

.theme-feminine .header-left .logo-img {
  filter: drop-shadow(0 0 8px var(--glow-pink));
}

.theme-feminine .btn-primary {
  background: linear-gradient(135deg, var(--accent-pink), var(--accent-rose));
  color: #fff;
  box-shadow: 0 2px 12px rgba(244, 114, 182, 0.4);
}

.theme-feminine .btn-primary:hover {
  background: linear-gradient(135deg, #f584c1, #fd8a9a);
  box-shadow: 0 4px 18px rgba(244, 114, 182, 0.55);
  transform: translateY(-1px);
}

.theme-feminine .btn-done {
  background: linear-gradient(135deg, var(--accent-lavender), var(--accent-blue));
  box-shadow: 0 2px 12px rgba(192, 132, 252, 0.4);
}

.theme-feminine .btn-done:hover {
  background: linear-gradient(135deg, #d09dff, #b8a0ff);
  box-shadow: 0 4px 18px rgba(192, 132, 252, 0.55);
}

.theme-feminine .widget-item:hover {
  box-shadow: 0 0 10px var(--glow-pink);
  transform: translateX(2px);
}

.theme-feminine .canvas-wrapper {
  background:
    radial-gradient(ellipse at 30% 20%, rgba(232, 71, 143, 0.05) 0%, transparent 55%),
    radial-gradient(ellipse at 70% 80%, rgba(155, 108, 216, 0.04) 0%, transparent 55%),
    #f7ecf3;
}

.theme-feminine .canvas {
  box-shadow:
    0 4px 24px rgba(180, 80, 130, 0.1),
    0 1px 4px rgba(180, 80, 130, 0.06);
}

.theme-feminine .canvas-grid {
  background-image:
    linear-gradient(rgba(232, 71, 143, 0.06) 1px, transparent 1px),
    linear-gradient(90deg, rgba(232, 71, 143, 0.06) 1px, transparent 1px);
}

.theme-feminine .placed-widget {
  box-shadow: 0 2px 12px rgba(180, 80, 130, 0.08), 0 1px 3px rgba(180, 80, 130, 0.06);
}

.theme-feminine .placed-widget:hover {
  box-shadow: 0 0 0 2px var(--accent-pink), 0 4px 16px rgba(232, 71, 143, 0.15);
}

.theme-feminine .placed-widget.selected {
  box-shadow: 0 0 0 2px var(--accent-lavender), 0 4px 16px rgba(155, 108, 216, 0.18);
}

.theme-feminine .placed-widget .resize-handle {
  background: linear-gradient(135deg, transparent 50%, var(--accent-pink) 50%);
}

.theme-feminine .dash-card-head {
  background: linear-gradient(135deg, var(--bg-tertiary), var(--bg-hover));
}

.theme-feminine .sidebar-mascot {
  background: linear-gradient(to top, rgba(232, 71, 143, 0.06), transparent);
}

.theme-feminine .sidebar-mascot img {
  filter: drop-shadow(0 0 12px rgba(244, 114, 182, 0.3));
}

.theme-feminine .modal {
  background: rgba(180, 80, 130, 0.25);
  backdrop-filter: blur(6px);
}

.theme-feminine .modal-content {
  box-shadow: 0 8px 40px rgba(180, 80, 130, 0.15), 0 2px 8px rgba(180, 80, 130, 0.08);
}

.theme-feminine .modal-header {
  background: linear-gradient(135deg, var(--bg-tertiary), var(--bg-hover));
}

.theme-feminine .edit-layout-btn {
  background: linear-gradient(135deg, var(--accent-pink), var(--accent-rose));
  box-shadow: 0 4px 20px rgba(244, 114, 182, 0.45);
}

.theme-feminine .edit-layout-btn:hover {
  background: linear-gradient(135deg, #f584c1, #fd8a9a);
  box-shadow: 0 6px 28px rgba(244, 114, 182, 0.6);
}

.theme-feminine .tpl-modal-overlay,
.theme-feminine .pin-modal-overlay {
  background: rgba(180, 80, 130, 0.25);
  backdrop-filter: blur(8px);
}

.theme-feminine .toggle-switch input:checked + .toggle-slider {
  background: linear-gradient(135deg, var(--accent-pink), var(--accent-rose));
}

/* ============================================
   Terminal Theme - Green Phosphor CRT
   ============================================ */
.theme-terminal {
  --bg-primary: #0a0a0a;
  --bg-secondary: #0f0f0f;
  --bg-tertiary: #1a1a1a;
  --bg-hover: #252525;
  --border: #00ff0033;
  --border-soft: #00ff0022;
  --text-primary: #00ff00;
  --text-secondary: #00cc00;
  --text-muted: #009900;
  --accent-blue: #00ffff;
  --accent-green: #00ff00;
  --accent-orange: #ffaa00;
  --accent-red: #ff3333;
  --accent-purple: #ff00ff;
}

/* Terminal theme CRT effects */
body.theme-terminal {
  font-family: 'Courier New', 'Monaco', 'Consolas', monospace;
}

.theme-terminal .builder-header,
.theme-terminal .widget-panel,
.theme-terminal .properties-panel,
.theme-terminal .canvas-info {
  font-family: 'Courier New', 'Monaco', 'Consolas', monospace;
}

/* Subtle CRT scanlines */
.theme-terminal .canvas::after {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: repeating-linear-gradient(
    0deg,
    rgba(0, 0, 0, 0.1) 0px,
    rgba(0, 0, 0, 0.1) 1px,
    transparent 1px,
    transparent 2px
  );
  border-radius: inherit;
  z-index: 1000;
}

.theme-terminal .canvas-wrapper {
  background: 
    radial-gradient(ellipse at center, #0f1a0f 0%, #0a0a0a 100%);
}

.theme-terminal .canvas {
  border-color: #00ff0044;
  box-shadow: 
    0 0 20px rgba(0, 255, 0, 0.1),
    inset 0 0 60px rgba(0, 255, 0, 0.03);
}

.theme-terminal .canvas-grid {
  background-image:
    linear-gradient(rgba(0, 255, 0, 0.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0, 255, 0, 0.05) 1px, transparent 1px);
}

.theme-terminal .placed-widget {
  background: #0f0f0f;
  border-color: #00ff0033;
  box-shadow: 0 0 10px rgba(0, 255, 0, 0.1);
}

.theme-terminal .placed-widget:hover {
  box-shadow: 0 0 0 2px #00ff0088, 0 0 15px rgba(0, 255, 0, 0.2);
}

.theme-terminal .placed-widget.selected {
  box-shadow: 0 0 0 2px #00ffff88, 0 0 15px rgba(0, 255, 255, 0.2);
}

.theme-terminal .placed-widget .resize-handle {
  background: linear-gradient(135deg, transparent 50%, #00ff00 50%);
}

.theme-terminal .btn-primary {
  background: #00ff00;
  color: #0a0a0a;
  border: 1px solid #00ff00;
  box-shadow: 0 0 10px rgba(0, 255, 0, 0.3);
}

.theme-terminal .btn-primary:hover {
  background: #33ff33;
  box-shadow: 0 0 20px rgba(0, 255, 0, 0.5);
}

.theme-terminal .btn-secondary {
  border-color: #00ff0044;
}

.theme-terminal .btn-secondary:hover {
  border-color: #00ff00;
  background: #1a1a1a;
  box-shadow: 0 0 10px rgba(0, 255, 0, 0.2);
}

.theme-terminal .btn-done {
  background: #00ffff;
  color: #0a0a0a;
  box-shadow: 0 0 10px rgba(0, 255, 255, 0.3);
}

.theme-terminal .btn-done:hover {
  background: #66ffff;
  box-shadow: 0 0 20px rgba(0, 255, 255, 0.5);
}

.theme-terminal .widget-item:hover {
  border-color: #00ff00;
  box-shadow: 0 0 10px rgba(0, 255, 0, 0.2);
}

.theme-terminal .widget-verified {
  color: #00ff00;
  background: rgba(0, 255, 0, 0.15);
}

.theme-terminal .header-nav .nav-link:hover {
  color: #00ff00;
  text-shadow: 0 0 10px rgba(0, 255, 0, 0.5);
}

.theme-terminal .builder-header {
  border-bottom-color: #00ff0033;
  box-shadow: 0 1px 0 #00ff0022;
}

.theme-terminal .widget-panel {
  border-right-color: #00ff0022;
}

.theme-terminal .properties-panel {
  border-left-color: #00ff0022;
}

.theme-terminal .canvas-info {
  border-top-color: #00ff0022;
}

.theme-terminal .prop-group input:focus,
.theme-terminal .prop-group select:focus,
.theme-terminal .header-center select:focus,
.theme-terminal .header-center input:focus {
  border-color: #00ff00;
  box-shadow: 0 0 0 3px rgba(0, 255, 0, 0.15);
}

.theme-terminal .modal {
  background: rgba(0, 0, 0, 0.85);
}

.theme-terminal .modal-content {
  border-color: #00ff0044;
  box-shadow: 0 0 30px rgba(0, 255, 0, 0.15);
}

.theme-terminal .edit-layout-btn {
  background: #00ff00;
  color: #0a0a0a;
  box-shadow: 0 0 15px rgba(0, 255, 0, 0.4);
}

.theme-terminal .edit-layout-btn:hover {
  background: #33ff33;
  box-shadow: 0 0 25px rgba(0, 255, 0, 0.6);
}

.theme-terminal .dash-card-head {
  background: #1a1a1a;
  border-bottom-color: #00ff0022;
}

.theme-terminal .kpi-value.blue { color: #00ffff !important; }
.theme-terminal .kpi-value.green { color: #00ff00 !important; }
.theme-terminal .kpi-value.orange { color: #ffaa00 !important; }
.theme-terminal .kpi-value.red { color: #ff3333 !important; }

.theme-terminal .tz-time {
  color: #00ffff;
  text-shadow: 0 0 5px rgba(0, 255, 255, 0.5);
}

.theme-terminal ::-webkit-scrollbar-thumb {
  background: #00ff0044;
}

.theme-terminal ::-webkit-scrollbar-thumb:hover {
  background: #00ff0088;
}

.theme-terminal .tpl-modal-overlay,
.theme-terminal .pin-modal-overlay {
  background: rgba(0, 0, 0, 0.85);
}

.theme-terminal .tpl-modal,
.theme-terminal .pin-modal {
  border-color: #00ff0044;
  box-shadow: 0 0 30px rgba(0, 255, 0, 0.15);
}

.theme-terminal .toggle-switch input:checked + .toggle-slider {
  background: #00ff00;
}

/* ============================================
   Paper Theme - Light Cream/Sepia
   ============================================ */
.theme-paper {
  --bg-primary: #faf8f5;
  --bg-secondary: #ffffff;
  --bg-tertiary: #f5f2ed;
  --bg-hover: #ebe7e0;
  --border: #d4cfc5;
  --border-soft: #e5e1d9;
  --text-primary: #2d2a26;
  --text-secondary: #5c5650;
  --text-muted: #8a847a;
  --accent-blue: #4a7c9b;
  --accent-green: #5a8a5a;
  --accent-orange: #b8860b;
  --accent-red: #a85454;
  --accent-purple: #7a6a8a;
}

body.theme-paper {
  font-family: 'Georgia', 'Times New Roman', 'Palatino', serif;
  background: #e8e0d4;
}

.theme-paper .builder-header,
.theme-paper .widget-panel h3,
.theme-paper .properties-panel h3,
.theme-paper .widget-section h4 {
  font-family: 'Georgia', 'Times New Roman', 'Palatino', serif;
}

.theme-paper .widget-item,
.theme-paper .prop-group,
.theme-paper .canvas-info,
.theme-paper .btn {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

.theme-paper .canvas-wrapper {
  background: 
    linear-gradient(135deg, #efe9e0 0%, #e8e0d4 50%, #efe9e0 100%);
}

.theme-paper .canvas {
  background: #f5f2eb;
  border-color: #d4cfc5;
  box-shadow: 
    0 1px 3px rgba(0, 0, 0, 0.08),
    0 4px 12px rgba(0, 0, 0, 0.06);
}

.theme-paper .canvas-grid {
  background-image:
    linear-gradient(rgba(180, 170, 150, 0.1) 1px, transparent 1px),
    linear-gradient(90deg, rgba(180, 170, 150, 0.1) 1px, transparent 1px);
}

.theme-paper .placed-widget {
  background: #fffffe;
  border-color: #cdc5b8;
  box-shadow: 
    0 1px 2px rgba(0, 0, 0, 0.08),
    0 3px 8px rgba(100, 80, 60, 0.1);
}

.theme-paper .placed-widget:hover {
  box-shadow: 0 0 0 2px #4a7c9b, 0 2px 8px rgba(0, 0, 0, 0.1);
}

.theme-paper .placed-widget.selected {
  box-shadow: 0 0 0 2px #5a8a5a, 0 2px 8px rgba(0, 0, 0, 0.1);
}

.theme-paper .placed-widget .resize-handle {
  background: linear-gradient(135deg, transparent 50%, #4a7c9b 50%);
}

.theme-paper .btn-primary {
  background: #4a7c9b;
  color: #ffffff;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.theme-paper .btn-primary:hover {
  background: #5a8cab;
}

.theme-paper .btn-done {
  background: #5a8a5a;
  color: #ffffff;
}

.theme-paper .btn-done:hover {
  background: #6a9a6a;
}

.theme-paper .btn-secondary:hover {
  border-color: #4a7c9b;
}

.theme-paper .widget-item:hover {
  border-color: #4a7c9b;
}

.theme-paper .widget-verified {
  color: #5a8a5a;
  background: rgba(90, 138, 90, 0.12);
}

.theme-paper .header-nav .nav-link:hover {
  color: #4a7c9b;
}

.theme-paper .builder-header {
  background: #fffdf8;
  border-bottom: 3px solid #a89880;
  box-shadow: 0 3px 10px rgba(80, 60, 40, 0.2);
}

.theme-paper .widget-panel {
  background: #f7f3ed;
  border-right: 2px solid #d4cfc5;
}

.theme-paper .properties-panel {
  background: #f7f3ed;
  border-left: 2px solid #d4cfc5;
}

.theme-paper .prop-group input:focus,
.theme-paper .prop-group select:focus,
.theme-paper .header-center select:focus,
.theme-paper .header-center input:focus {
  border-color: #4a7c9b;
  box-shadow: 0 0 0 3px rgba(74, 124, 155, 0.15);
}

.theme-paper .dash-card-head {
  background: #ebe5d8;
  border-bottom: 2px solid #c5b8a5;
}

.theme-paper .kpi-value.blue { color: #4a7c9b !important; }
.theme-paper .kpi-value.green { color: #5a8a5a !important; }
.theme-paper .kpi-value.orange { color: #b8860b !important; }
.theme-paper .kpi-value.red { color: #a85454 !important; }

.theme-paper .tz-time {
  color: #4a7c9b;
}

.theme-paper .modal {
  background: rgba(0, 0, 0, 0.4);
}

.theme-paper .modal-content {
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
}

.theme-paper .edit-layout-btn {
  background: #4a7c9b;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

.theme-paper .edit-layout-btn:hover {
  background: #5a8cab;
}

.theme-paper ::-webkit-scrollbar-thumb {
  background: #d4cfc5;
}

.theme-paper ::-webkit-scrollbar-thumb:hover {
  background: #c4bfb5;
}

.theme-paper .tpl-tag {
  background: rgba(74, 124, 155, 0.12);
  color: #4a7c9b;
  border: 1px solid rgba(74, 124, 155, 0.2);
}

.theme-paper .toggle-switch input:checked + .toggle-slider {
  background: #5a8a5a;
}

/* ============================================
   Theme Selector Styles
   ============================================ */
.theme-selector {
  display: flex;
  align-items: center;
  gap: 8px;
}

.theme-selector label {
  color: var(--text-secondary);
  font-size: 13px;
}

.theme-selector select {
  background: var(--bg-tertiary);
  border: 1px solid var(--border);
  color: var(--text-primary);
  padding: 6px 10px;
  border-radius: 6px;
  font-size: 13px;
  cursor: pointer;
  transition: border-color 0.2s;
}

.theme-selector select:hover {
  border-color: var(--accent-blue);
}

.theme-selector select:focus {
  outline: none;
  border-color: var(--accent-blue);
  box-shadow: 0 0 0 3px rgba(88, 166, 255, 0.15);
}

/* ============================================
   Placed Widget Icon System (.lb-icon)
   Themeable icons for placed widgets on canvas
   ============================================ */

/* Base styles - shows emoji by default */
.lb-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-style: normal;
  line-height: 1;
}

/* Large icon variant (for widget body icons) */
.lb-icon-lg {
  font-size: calc(24px * var(--font-scale, 1));
}

/* ============================================
   Terminal Theme - Phosphor Icon Overrides
   Only affects .theme-terminal, default keeps emoji
   Uses Phosphor-Light font loaded from CDN
   ============================================ */

/* Hide emoji text, show icon via ::after (sidebar icons) */
.theme-terminal .widget-item .widget-icon {
  font-size: 0 !important;
  color: transparent !important;
  position: relative;
  width: 24px;
  height: 24px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.theme-terminal .widget-item .widget-icon::after {
  font-family: 'Phosphor-Light' !important;
  font-size: 20px !important;
  font-weight: normal;
  font-style: normal;
  color: #00ff00 !important;
  text-shadow: 0 0 10px rgba(0, 255, 0, 0.7);
  content: "\ed54"; /* terminal icon as default fallback */
  position: absolute;
  left: 0;
  top: 0;
}

/* ============================================
   Terminal Theme - Placed Widget Icons (.lb-icon)
   ============================================ */

/* Base styles for .lb-icon in terminal theme */
.theme-terminal .lb-icon {
  font-size: 0 !important;
  color: transparent !important;
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 18px;
  height: 18px;
  margin-right: 6px;
}

.theme-terminal .lb-icon::after {
  font-family: 'Phosphor-Light' !important;
  font-size: 14px !important;
  font-weight: normal;
  font-style: normal;
  color: #00ff00 !important;
  text-shadow: 0 0 8px rgba(0, 255, 0, 0.6);
  content: "\e900"; /* default fallback */
  position: absolute;
}

/* Large icon variant in terminal theme */
.theme-terminal .lb-icon-lg {
  width: calc(24px * var(--font-scale, 1));
  height: calc(24px * var(--font-scale, 1));
}

.theme-terminal .lb-icon-lg::after {
  font-size: calc(20px * var(--font-scale, 1)) !important;
}

/* ============================================
   .lb-icon Phosphor Mappings (Terminal Theme)
   ============================================ */

/* Weather icons */
.theme-terminal .lb-icon[data-icon="weather"]::after { content: "\ed6f"; } /* thermometer */
.theme-terminal .lb-icon[data-icon="weather-sunny"]::after { content: "\ed3a"; } /* sun */
.theme-terminal .lb-icon[data-icon="weather-cloudy"]::after { content: "\ea59"; } /* cloud-sun */
.theme-terminal .lb-icon[data-icon="weather-rainy"]::after { content: "\ea56"; } /* cloud-rain */
.theme-terminal .lb-icon[data-icon="weather-snowy"]::after { content: "\ecf5"; } /* snowflake */
.theme-terminal .lb-icon[data-icon="world-weather"]::after { content: "\eb5a"; } /* globe */

/* Time icons */
.theme-terminal .lb-icon[data-icon="clock"]::after { content: "\ea46"; } /* clock */
.theme-terminal .lb-icon[data-icon="countdown"]::after { content: "\eb95"; } /* hourglass */
.theme-terminal .lb-icon[data-icon="cron"]::after { content: "\ed7b"; } /* timer */
.theme-terminal .lb-icon[data-icon="pomodoro"]::after { content: "\ea76"; } /* crosshair */
.theme-terminal .lb-icon[data-icon="world-clock"]::after { content: "\eb5a"; } /* globe */

/* System icons */
.theme-terminal .lb-icon[data-icon="cpu"]::after { content: "\ea72"; } /* cpu */
.theme-terminal .lb-icon[data-icon="disk"]::after { content: "\eb82"; } /* hard-drive */
.theme-terminal .lb-icon[data-icon="network"]::after { content: "\edd1"; } /* wifi-high */
.theme-terminal .lb-icon[data-icon="docker"]::after { content: "\ea7b"; } /* cube */
.theme-terminal .lb-icon[data-icon="uptime"]::after { content: "\e9d6"; } /* broadcast */
.theme-terminal .lb-icon[data-icon="system-log"]::after { content: "\ede0"; } /* wrench */

/* Auth / Security icons */
.theme-terminal .lb-icon[data-icon="auth"]::after { content: "\ebc6"; } /* lock-key */
.theme-terminal .lb-icon[data-icon="sleep"]::after { content: "\ec10"; } /* moon */

/* Releases icons */
.theme-terminal .lb-icon[data-icon="lobster"]::after { content: "\ec3d"; } /* package */
.theme-terminal .lb-icon[data-icon="release"]::after { content: "\ec3d"; } /* package */

/* Lists / Activity icons */
.theme-terminal .lb-icon[data-icon="activity"]::after { content: "\ebc0"; } /* list */
.theme-terminal .lb-icon[data-icon="calendar"]::after { content: "\e9e5"; } /* calendar */
.theme-terminal .lb-icon[data-icon="notes"]::after { content: "\ec13"; } /* note */
.theme-terminal .lb-icon[data-icon="todo"]::after { content: "\ea34"; } /* check-square */
.theme-terminal .lb-icon[data-icon="pages"]::after { content: "\eb03"; } /* files */

/* AI / Monitoring icons */
.theme-terminal .lb-icon[data-icon="ai-usage"]::after { content: "\ecc6"; } /* robot */
.theme-terminal .lb-icon[data-icon="ai-claude"]::after { content: "\ea38"; } /* circle */
.theme-terminal .lb-icon[data-icon="ai-cost"]::after { content: "\ea81"; } /* currency-dollar */
.theme-terminal .lb-icon[data-icon="api-status"]::after { content: "\e96f"; } /* arrows-clockwise */
.theme-terminal .lb-icon[data-icon="sessions"]::after { content: "\ea25"; } /* chat-dots */
.theme-terminal .lb-icon[data-icon="tokens"]::after { content: "\ea18"; } /* chart-bar */

/* AI Provider icons */
.theme-terminal .lb-icon[data-icon="claude-code"]::after { content: "\ea38"; } /* circle */
.theme-terminal .lb-icon[data-icon="codex-cli"]::after { content: "\ea38"; } /* circle */
.theme-terminal .lb-icon[data-icon="github-copilot"]::after { content: "\ea38"; } /* circle */
.theme-terminal .lb-icon[data-icon="cursor"]::after { content: "\ea38"; } /* circle */
.theme-terminal .lb-icon[data-icon="gemini-cli"]::after { content: "\eaa9"; } /* diamond */
.theme-terminal .lb-icon[data-icon="amp-code"]::after { content: "\ebb3"; } /* lightning */
.theme-terminal .lb-icon[data-icon="factory"]::after { content: "\eaf4"; } /* factory */
.theme-terminal .lb-icon[data-icon="kimi-code"]::after { content: "\ec10"; } /* moon */
.theme-terminal .lb-icon[data-icon="jetbrains-ai"]::after { content: "\e9d1"; } /* brain */
.theme-terminal .lb-icon[data-icon="minimax"]::after { content: "\eaa9"; } /* diamond */
.theme-terminal .lb-icon[data-icon="zai"]::after { content: "\ecd9"; } /* sparkle */
.theme-terminal .lb-icon[data-icon="antigravity"]::after { content: "\ec42"; } /* planet */

/* Finance icons */
.theme-terminal .lb-icon[data-icon="stock"]::after { content: "\ea1c"; } /* chart-line-up */
.theme-terminal .lb-icon[data-icon="crypto"]::after { content: "\ea7d"; } /* currency-btc */

/* Productivity icons */
.theme-terminal .lb-icon[data-icon="email"]::after { content: "\eac5"; } /* envelope */
.theme-terminal .lb-icon[data-icon="github"]::after { content: "\eb4f"; } /* git-branch */

/* Smart Home icons */
.theme-terminal .lb-icon[data-icon="home"]::after { content: "\eb98"; } /* house */
.theme-terminal .lb-icon[data-icon="camera"]::after { content: "\e9eb"; } /* camera */
.theme-terminal .lb-icon[data-icon="power"]::after { content: "\ec74"; } /* plug */

/* Media icons */
.theme-terminal .lb-icon[data-icon="music"]::after { content: "\ec23"; } /* music-notes */
.theme-terminal .lb-icon[data-icon="quote"]::after { content: "\eca1"; } /* quotes */

/* Image icons */
.theme-terminal .lb-icon[data-icon="image"]::after { content: "\eba2"; } /* image */
.theme-terminal .lb-icon[data-icon="image-random"]::after { content: "\ecc0"; } /* shuffle */
.theme-terminal .lb-icon[data-icon="image-new"]::after { content: "\ecd9"; } /* sparkle */

/* Links / Embeds icons */
.theme-terminal .lb-icon[data-icon="links"]::after { content: "\ebc4"; } /* link */
.theme-terminal .lb-icon[data-icon="embed"]::after { content: "\e9d8"; } /* browser */
.theme-terminal .lb-icon[data-icon="rss"]::after { content: "\ecb8"; } /* rss */

/* Layout icons */
.theme-terminal .lb-icon[data-icon="header"]::after { content: "\ed57"; } /* text-aa */
.theme-terminal .lb-icon[data-icon="line-h"]::after { content: "\ec0e"; } /* minus */
.theme-terminal .lb-icon[data-icon="line-v"]::after { content: "\ebbc"; } /* line-vertical */

/* ============================================
   Sidebar Icon Mappings by data-widget attribute
   ============================================ */

/* Icon mappings by data-widget attribute - Phosphor Light unicode values */
.theme-terminal [data-widget="weather"] .widget-icon::after,
.theme-terminal [data-widget="weather-multi"] .widget-icon::after { content: "\ed6f"; } /* thermometer */

.theme-terminal [data-widget="clock"] .widget-icon::after,
.theme-terminal [data-widget="world-clock"] .widget-icon::after,
.theme-terminal [data-widget="pomodoro"] .widget-icon::after { content: "\ea46"; } /* clock */

.theme-terminal [data-widget="countdown"] .widget-icon::after { content: "\eb95"; } /* hourglass */

.theme-terminal [data-widget="cpu-memory"] .widget-icon::after,
.theme-terminal [data-widget="system-info"] .widget-icon::after { content: "\ea72"; } /* cpu */

.theme-terminal [data-widget="disk-usage"] .widget-icon::after { content: "\eb82"; } /* hard-drive */

.theme-terminal [data-widget="network-speed"] .widget-icon::after,
.theme-terminal [data-widget="ping-status"] .widget-icon::after { content: "\edd1"; } /* wifi-high */

.theme-terminal [data-widget="docker-status"] .widget-icon::after { content: "\ea7b"; } /* cube */

.theme-terminal [data-widget="github-stats"] .widget-icon::after,
.theme-terminal [data-widget="github-activity"] .widget-icon::after { content: "\eb4f"; } /* git-branch */

.theme-terminal [data-widget="rss-ticker"] .widget-icon::after,
.theme-terminal [data-widget="rss-feed"] .widget-icon::after { content: "\ecb8"; } /* rss */

.theme-terminal [data-widget="crypto-price"] .widget-icon::after,
.theme-terminal [data-widget="crypto-ticker"] .widget-icon::after { content: "\ea7d"; } /* currency-btc */

.theme-terminal [data-widget="stock-price"] .widget-icon::after,
.theme-terminal [data-widget="stock-chart"] .widget-icon::after { content: "\ea1b"; } /* chart-line */

.theme-terminal [data-widget="kpi-number"] .widget-icon::after,
.theme-terminal [data-widget="kpi-ring"] .widget-icon::after,
.theme-terminal [data-widget="kpi-compare"] .widget-icon::after { content: "\ea18"; } /* chart-bar */

.theme-terminal [data-widget="email-unread"] .widget-icon::after { content: "\eac5"; } /* envelope */

.theme-terminal [data-widget="calendar"] .widget-icon::after,
.theme-terminal [data-widget="calendar-agenda"] .widget-icon::after { content: "\e9e5"; } /* calendar */

.theme-terminal [data-widget="todo-list"] .widget-icon::after,
.theme-terminal [data-widget="checklist"] .widget-icon::after { content: "\ea34"; } /* check-square */

.theme-terminal [data-widget="notes"] .widget-icon::after,
.theme-terminal [data-widget="text-block"] .widget-icon::after { content: "\ec13"; } /* note */

.theme-terminal [data-widget="iframe"] .widget-icon::after,
.theme-terminal [data-widget="webview"] .widget-icon::after { content: "\e9d8"; } /* browser */

.theme-terminal [data-widget="image"] .widget-icon::after { content: "\eba2"; } /* image */

.theme-terminal [data-widget="quote"] .widget-icon::after { content: "\eca1"; } /* quotes */

.theme-terminal [data-widget="bookmark"] .widget-icon::after,
.theme-terminal [data-widget="links"] .widget-icon::after { content: "\ebc4"; } /* link */

.theme-terminal [data-widget="uptime"] .widget-icon::after { content: "\ec98"; } /* activity/pulse */

.theme-terminal [data-widget="api-status"] .widget-icon::after { content: "\e9d6"; } /* broadcast */

.theme-terminal [data-widget="random"] .widget-icon::after { content: "\ea7b"; } /* cube */

/* Globe icon for world widgets */
.theme-terminal [data-widget="world-clock"] .widget-icon::after,
.theme-terminal [data-widget="world-weather"] .widget-icon::after { content: "\eb5a"; } /* globe */

/* ============================================
   Feminine Theme - Phosphor Icon Overrides
   Pink/Lavender icons with soft glow
   ============================================ */

/* Widget panel sidebar icons */
.theme-feminine .widget-item .widget-icon {
  font-size: 0 !important;
  color: transparent !important;
  position: relative;
  width: 24px;
  height: 24px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.theme-feminine .widget-item .widget-icon::after {
  font-family: 'Phosphor-Light' !important;
  font-size: 20px !important;
  font-weight: normal;
  font-style: normal;
  color: var(--accent-pink) !important;
  text-shadow: 0 0 8px rgba(232, 71, 143, 0.4);
  content: "\eca1"; /* default fallback */
  position: absolute;
  left: 0;
  top: 0;
}

/* Placed widget icons (.lb-icon) */
.theme-feminine .lb-icon {
  font-size: 0 !important;
  color: transparent !important;
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 18px;
  height: 18px;
  margin-right: 6px;
  vertical-align: middle;
}

.theme-feminine .lb-icon::after {
  font-family: 'Phosphor-Light' !important;
  font-size: 14px;
  color: var(--accent-pink);
  text-shadow: 0 0 6px rgba(232, 71, 143, 0.3);
  content: "\eca1"; /* default */
}

.theme-feminine .lb-icon-lg {
  width: 48px;
  height: 48px;
}

.theme-feminine .lb-icon-lg::after {
  font-size: 42px;
  text-shadow: 0 0 12px rgba(232, 71, 143, 0.4);
}

/* Feminine icon mappings */
.theme-feminine .lb-icon[data-icon="weather"]::after,
.theme-feminine [data-widget="weather"] .widget-icon::after,
.theme-feminine [data-widget="weather-multi"] .widget-icon::after { content: "\ed6f"; }
.theme-feminine .lb-icon[data-icon="weather-sunny"]::after { content: "\ed1d"; }
.theme-feminine .lb-icon[data-icon="weather-cloudy"]::after { content: "\ea54"; }
.theme-feminine .lb-icon[data-icon="weather-rain"]::after { content: "\ea5a"; }
.theme-feminine .lb-icon[data-icon="weather-snow"]::after { content: "\ed11"; }
.theme-feminine .lb-icon[data-icon="weather-fog"]::after { content: "\ea5a"; }
.theme-feminine .lb-icon[data-icon="clock"]::after,
.theme-feminine [data-widget="clock"] .widget-icon::after,
.theme-feminine [data-widget="world-clock"] .widget-icon::after { content: "\ea46"; }
.theme-feminine .lb-icon[data-icon="globe"]::after { content: "\eb5a"; }
.theme-feminine .lb-icon[data-icon="countdown"]::after,
.theme-feminine [data-widget="countdown"] .widget-icon::after { content: "\eb95"; }
.theme-feminine .lb-icon[data-icon="cpu"]::after,
.theme-feminine [data-widget="cpu-memory"] .widget-icon::after { content: "\ea72"; }
.theme-feminine .lb-icon[data-icon="memory"]::after { content: "\ec9c"; }
.theme-feminine .lb-icon[data-icon="disk"]::after,
.theme-feminine [data-widget="disk-usage"] .widget-icon::after { content: "\eb82"; }
.theme-feminine .lb-icon[data-icon="network"]::after,
.theme-feminine [data-widget="network-speed"] .widget-icon::after { content: "\edd1"; }
.theme-feminine .lb-icon[data-icon="docker"]::after,
.theme-feminine [data-widget="docker-status"] .widget-icon::after { content: "\ea7b"; }
.theme-feminine .lb-icon[data-icon="uptime"]::after { content: "\ec98"; }
.theme-feminine .lb-icon[data-icon="broadcast"]::after { content: "\e9d6"; }
.theme-feminine .lb-icon[data-icon="calendar"]::after,
.theme-feminine [data-widget="calendar"] .widget-icon::after { content: "\e9e5"; }
.theme-feminine .lb-icon[data-icon="today"]::after { content: "\e9e5"; }
.theme-feminine .lb-icon[data-icon="todo"]::after,
.theme-feminine [data-widget="todo-list"] .widget-icon::after { content: "\ea34"; }
.theme-feminine .lb-icon[data-icon="notes"]::after,
.theme-feminine [data-widget="notes"] .widget-icon::after { content: "\ec13"; }
.theme-feminine .lb-icon[data-icon="text"]::after { content: "\ed57"; }
.theme-feminine .lb-icon[data-icon="chart"]::after,
.theme-feminine .lb-icon[data-icon="kpi"]::after,
.theme-feminine [data-widget="kpi-number"] .widget-icon::after { content: "\ea18"; }
.theme-feminine .lb-icon[data-icon="chart-line"]::after { content: "\ea1b"; }
.theme-feminine .lb-icon[data-icon="ring"]::after { content: "\ea1b"; }
.theme-feminine .lb-icon[data-icon="target"]::after { content: "\ed45"; }
.theme-feminine .lb-icon[data-icon="stock"]::after,
.theme-feminine [data-widget="stock-price"] .widget-icon::after { content: "\ea1b"; }
.theme-feminine .lb-icon[data-icon="crypto"]::after,
.theme-feminine [data-widget="crypto-price"] .widget-icon::after { content: "\ea7d"; }
.theme-feminine .lb-icon[data-icon="email"]::after,
.theme-feminine [data-widget="email-unread"] .widget-icon::after { content: "\eac5"; }
.theme-feminine .lb-icon[data-icon="github"]::after,
.theme-feminine [data-widget="github-stats"] .widget-icon::after { content: "\eb4f"; }
.theme-feminine .lb-icon[data-icon="home"]::after { content: "\eb98"; }
.theme-feminine .lb-icon[data-icon="camera"]::after { content: "\e9eb"; }
.theme-feminine .lb-icon[data-icon="power"]::after { content: "\ec74"; }
.theme-feminine .lb-icon[data-icon="music"]::after { content: "\ec23"; }
.theme-feminine .lb-icon[data-icon="quote"]::after { content: "\eca1"; }
.theme-feminine .lb-icon[data-icon="image"]::after,
.theme-feminine [data-widget="image"] .widget-icon::after { content: "\eba2"; }
.theme-feminine .lb-icon[data-icon="links"]::after,
.theme-feminine [data-widget="bookmark"] .widget-icon::after { content: "\ebc4"; }
.theme-feminine .lb-icon[data-icon="embed"]::after,
.theme-feminine [data-widget="iframe"] .widget-icon::after { content: "\e9d8"; }
.theme-feminine .lb-icon[data-icon="rss"]::after,
.theme-feminine [data-widget="rss-ticker"] .widget-icon::after { content: "\ecb8"; }
.theme-feminine .lb-icon[data-icon="header"]::after { content: "\ed57"; }
.theme-feminine .lb-icon[data-icon="line-h"]::after { content: "\ec0e"; }
.theme-feminine .lb-icon[data-icon="line-v"]::after { content: "\ebbc"; }
.theme-feminine .lb-icon[data-icon="lobster"]::after { content: "\ecd9"; } /* sparkle */
.theme-feminine .lb-icon[data-icon="cron"]::after,
.theme-feminine [data-widget="pomodoro"] .widget-icon::after { content: "\ea46"; }
.theme-feminine .lb-icon[data-icon="auth"]::after { content: "\ebd0"; }
.theme-feminine .lb-icon[data-icon="sleep"]::after { content: "\ec1f"; }
.theme-feminine .lb-icon[data-icon="release"]::after { content: "\ec9c"; }
.theme-feminine .lb-icon[data-icon="log"]::after { content: "\ed54"; }
.theme-feminine .lb-icon[data-icon="ai"]::after { content: "\eccc"; }

/* ============================================
   Paper Theme - Phosphor Icon Overrides
   Warm sepia icons, clean minimal style
   ============================================ */

/* Widget panel sidebar icons */
.theme-paper .widget-item .widget-icon {
  font-size: 0 !important;
  color: transparent !important;
  position: relative;
  width: 24px;
  height: 24px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.theme-paper .widget-item .widget-icon::after {
  font-family: 'Phosphor-Light' !important;
  font-size: 20px !important;
  font-weight: normal;
  font-style: normal;
  color: var(--accent-blue) !important;
  content: "\eca1"; /* default fallback */
  position: absolute;
  left: 0;
  top: 0;
}

/* Placed widget icons (.lb-icon) */
.theme-paper .lb-icon {
  font-size: 0 !important;
  color: transparent !important;
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 18px;
  height: 18px;
  margin-right: 6px;
  vertical-align: middle;
}

.theme-paper .lb-icon::after {
  font-family: 'Phosphor-Light' !important;
  font-size: 14px;
  color: #5c5650;
  content: "\eca1"; /* default */
}

.theme-paper .lb-icon-lg {
  width: 48px;
  height: 48px;
}

.theme-paper .lb-icon-lg::after {
  font-size: 42px;
  color: var(--accent-blue);
}

/* Paper icon mappings */
.theme-paper .lb-icon[data-icon="weather"]::after,
.theme-paper [data-widget="weather"] .widget-icon::after,
.theme-paper [data-widget="weather-multi"] .widget-icon::after { content: "\ed6f"; }
.theme-paper .lb-icon[data-icon="weather-sunny"]::after { content: "\ed1d"; }
.theme-paper .lb-icon[data-icon="weather-cloudy"]::after { content: "\ea54"; }
.theme-paper .lb-icon[data-icon="weather-rain"]::after { content: "\ea5a"; }
.theme-paper .lb-icon[data-icon="weather-snow"]::after { content: "\ed11"; }
.theme-paper .lb-icon[data-icon="weather-fog"]::after { content: "\ea5a"; }
.theme-paper .lb-icon[data-icon="clock"]::after,
.theme-paper [data-widget="clock"] .widget-icon::after,
.theme-paper [data-widget="world-clock"] .widget-icon::after { content: "\ea46"; }
.theme-paper .lb-icon[data-icon="globe"]::after { content: "\eb5a"; }
.theme-paper .lb-icon[data-icon="countdown"]::after,
.theme-paper [data-widget="countdown"] .widget-icon::after { content: "\eb95"; }
.theme-paper .lb-icon[data-icon="cpu"]::after,
.theme-paper [data-widget="cpu-memory"] .widget-icon::after { content: "\ea72"; }
.theme-paper .lb-icon[data-icon="memory"]::after { content: "\ec9c"; }
.theme-paper .lb-icon[data-icon="disk"]::after,
.theme-paper [data-widget="disk-usage"] .widget-icon::after { content: "\eb82"; }
.theme-paper .lb-icon[data-icon="network"]::after,
.theme-paper [data-widget="network-speed"] .widget-icon::after { content: "\edd1"; }
.theme-paper .lb-icon[data-icon="docker"]::after,
.theme-paper [data-widget="docker-status"] .widget-icon::after { content: "\ea7b"; }
.theme-paper .lb-icon[data-icon="uptime"]::after { content: "\ec98"; }
.theme-paper .lb-icon[data-icon="broadcast"]::after { content: "\e9d6"; }
.theme-paper .lb-icon[data-icon="calendar"]::after,
.theme-paper [data-widget="calendar"] .widget-icon::after { content: "\e9e5"; }
.theme-paper .lb-icon[data-icon="today"]::after { content: "\e9e5"; }
.theme-paper .lb-icon[data-icon="todo"]::after,
.theme-paper [data-widget="todo-list"] .widget-icon::after { content: "\ea34"; }
.theme-paper .lb-icon[data-icon="notes"]::after,
.theme-paper [data-widget="notes"] .widget-icon::after { content: "\ec13"; }
.theme-paper .lb-icon[data-icon="text"]::after { content: "\ed57"; }
.theme-paper .lb-icon[data-icon="chart"]::after,
.theme-paper .lb-icon[data-icon="kpi"]::after,
.theme-paper [data-widget="kpi-number"] .widget-icon::after { content: "\ea18"; }
.theme-paper .lb-icon[data-icon="chart-line"]::after { content: "\ea1b"; }
.theme-paper .lb-icon[data-icon="ring"]::after { content: "\ea1b"; }
.theme-paper .lb-icon[data-icon="target"]::after { content: "\ed45"; }
.theme-paper .lb-icon[data-icon="stock"]::after,
.theme-paper [data-widget="stock-price"] .widget-icon::after { content: "\ea1b"; }
.theme-paper .lb-icon[data-icon="crypto"]::after,
.theme-paper [data-widget="crypto-price"] .widget-icon::after { content: "\ea7d"; }
.theme-paper .lb-icon[data-icon="email"]::after,
.theme-paper [data-widget="email-unread"] .widget-icon::after { content: "\eac5"; }
.theme-paper .lb-icon[data-icon="github"]::after,
.theme-paper [data-widget="github-stats"] .widget-icon::after { content: "\eb4f"; }
.theme-paper .lb-icon[data-icon="home"]::after { content: "\eb98"; }
.theme-paper .lb-icon[data-icon="camera"]::after { content: "\e9eb"; }
.theme-paper .lb-icon[data-icon="power"]::after { content: "\ec74"; }
.theme-paper .lb-icon[data-icon="music"]::after { content: "\ec23"; }
.theme-paper .lb-icon[data-icon="quote"]::after { content: "\eca1"; }
.theme-paper .lb-icon[data-icon="image"]::after,
.theme-paper [data-widget="image"] .widget-icon::after { content: "\eba2"; }
.theme-paper .lb-icon[data-icon="links"]::after,
.theme-paper [data-widget="bookmark"] .widget-icon::after { content: "\ebc4"; }
.theme-paper .lb-icon[data-icon="embed"]::after,
.theme-paper [data-widget="iframe"] .widget-icon::after { content: "\e9d8"; }
.theme-paper .lb-icon[data-icon="rss"]::after,
.theme-paper [data-widget="rss-ticker"] .widget-icon::after { content: "\ecb8"; }
.theme-paper .lb-icon[data-icon="header"]::after { content: "\ed57"; }
.theme-paper .lb-icon[data-icon="line-h"]::after { content: "\ec0e"; }
.theme-paper .lb-icon[data-icon="line-v"]::after { content: "\ebbc"; }
.theme-paper .lb-icon[data-icon="lobster"]::after { content: "\ecd9"; }
.theme-paper .lb-icon[data-icon="cron"]::after,
.theme-paper [data-widget="pomodoro"] .widget-icon::after { content: "\ea46"; }
.theme-paper .lb-icon[data-icon="auth"]::after { content: "\ebd0"; }
.theme-paper .lb-icon[data-icon="sleep"]::after { content: "\ec1f"; }
.theme-paper .lb-icon[data-icon="release"]::after { content: "\ec9c"; }
.theme-paper .lb-icon[data-icon="log"]::after { content: "\ed54"; }
.theme-paper .lb-icon[data-icon="ai"]::after { content: "\eccc"; }

/* Memory icon additions for all themes */
.theme-terminal .lb-icon[data-icon="memory"]::after { content: "\e9d1"; } /* brain */
.theme-feminine .lb-icon[data-icon="memory"]::after { content: "\e9d1"; } /* brain */
.theme-paper .lb-icon[data-icon="memory"]::after { content: "\e9d1"; } /* brain */

/* AI Provider icons for all icon-mapped themes */
.theme-paper .lb-icon[data-icon="ai-usage"]::after,
.theme-feminine .lb-icon[data-icon="ai-usage"]::after,
.theme-feminine-dark .lb-icon[data-icon="ai-usage"]::after { content: "\ecc6"; } /* robot */

.theme-paper .lb-icon[data-icon="claude-code"]::after,
.theme-paper .lb-icon[data-icon="codex-cli"]::after,
.theme-paper .lb-icon[data-icon="github-copilot"]::after,
.theme-paper .lb-icon[data-icon="cursor"]::after,
.theme-feminine .lb-icon[data-icon="claude-code"]::after,
.theme-feminine .lb-icon[data-icon="codex-cli"]::after,
.theme-feminine .lb-icon[data-icon="github-copilot"]::after,
.theme-feminine .lb-icon[data-icon="cursor"]::after,
.theme-feminine-dark .lb-icon[data-icon="claude-code"]::after,
.theme-feminine-dark .lb-icon[data-icon="codex-cli"]::after,
.theme-feminine-dark .lb-icon[data-icon="github-copilot"]::after,
.theme-feminine-dark .lb-icon[data-icon="cursor"]::after { content: "\ea38"; } /* circle */

.theme-paper .lb-icon[data-icon="gemini-cli"]::after,
.theme-paper .lb-icon[data-icon="minimax"]::after,
.theme-feminine .lb-icon[data-icon="gemini-cli"]::after,
.theme-feminine .lb-icon[data-icon="minimax"]::after,
.theme-feminine-dark .lb-icon[data-icon="gemini-cli"]::after,
.theme-feminine-dark .lb-icon[data-icon="minimax"]::after { content: "\eaa9"; } /* diamond */

.theme-paper .lb-icon[data-icon="amp-code"]::after,
.theme-feminine .lb-icon[data-icon="amp-code"]::after,
.theme-feminine-dark .lb-icon[data-icon="amp-code"]::after { content: "\ebb3"; } /* lightning */

.theme-paper .lb-icon[data-icon="factory"]::after,
.theme-feminine .lb-icon[data-icon="factory"]::after,
.theme-feminine-dark .lb-icon[data-icon="factory"]::after { content: "\eaf4"; } /* factory */

.theme-paper .lb-icon[data-icon="kimi-code"]::after,
.theme-feminine .lb-icon[data-icon="kimi-code"]::after,
.theme-feminine-dark .lb-icon[data-icon="kimi-code"]::after { content: "\ec10"; } /* moon */

.theme-paper .lb-icon[data-icon="jetbrains-ai"]::after,
.theme-feminine .lb-icon[data-icon="jetbrains-ai"]::after,
.theme-feminine-dark .lb-icon[data-icon="jetbrains-ai"]::after { content: "\e9d1"; } /* brain */

.theme-paper .lb-icon[data-icon="zai"]::after,
.theme-feminine .lb-icon[data-icon="zai"]::after,
.theme-feminine-dark .lb-icon[data-icon="zai"]::after { content: "\ecd9"; } /* sparkle */

.theme-paper .lb-icon[data-icon="antigravity"]::after,
.theme-feminine .lb-icon[data-icon="antigravity"]::after,
.theme-feminine-dark .lb-icon[data-icon="antigravity"]::after { content: "\ec42"; } /* planet */

/* RSS Ticker overrides for light themes */
.theme-paper .news-ticker-wrap {
  background: var(--bg-tertiary);
}

.theme-paper .ticker-link {
  color: var(--text-primary);
}

.theme-paper .ticker-link:hover {
  color: var(--accent-blue);
}

.theme-paper .ticker-sep {
  color: var(--border);
}

.theme-paper .ticker-label {
  color: var(--text-secondary);
  background: var(--bg-secondary);
}

.theme-feminine .news-ticker-wrap {
  background: var(--bg-tertiary);
}

.theme-feminine .ticker-link {
  color: var(--text-primary);
}

.theme-feminine .ticker-link:hover {
  color: var(--accent-pink);
}

.theme-feminine .ticker-sep {
  color: var(--border);
}

.theme-feminine .ticker-label {
  color: var(--text-secondary);
  background: var(--bg-secondary);
}

/* Text/Header widget color overrides for light themes */
.theme-paper .placed-widget[data-type="text-header"] > div,
.theme-paper .placed-widget[data-type="text-header"] div,
.theme-paper .placed-widget[data-type="text-header"] * {
  color: #1a1815 !important;
}

.theme-feminine .placed-widget[data-type="text-header"] > div,
.theme-feminine .placed-widget[data-type="text-header"] div,
.theme-feminine .placed-widget[data-type="text-header"] * {
  color: #2a1520 !important;
}

/* ============================================
   Feminine Dark Theme - Purple/Pink on Dark
   Based on PR #7 Commit 1
   ============================================ */
.theme-feminine-dark {
  --bg-primary: #12091e;
  --bg-secondary: #1a0f28;
  --bg-tertiary: #241535;
  --bg-hover: #321f58;
  --border: #4a2d6e;
  --border-soft: #3d2560;
  --text-primary: #f0e6f6;
  --text-secondary: #c9b8d9;
  --text-muted: #9a85b0;
  --accent-blue: #9b6cd8;
  --accent-green: #10b981;
  --accent-orange: #f59e0b;
  --accent-red: #f43f6e;
  --accent-purple: #a855f7;
  --accent-pink: #ec4899;
  --accent-rose: #f472b6;
  --accent-lavender: #c084fc;
  --glow-pink: rgba(236, 72, 153, 0.25);
  --glow-purple: rgba(168, 85, 247, 0.2);
}

body.theme-feminine-dark {
  background-image:
    radial-gradient(ellipse at 15% 0%, rgba(236, 72, 153, 0.1) 0%, transparent 50%),
    radial-gradient(ellipse at 85% 100%, rgba(168, 85, 247, 0.08) 0%, transparent 50%);
}

.theme-feminine-dark .builder-header {
  box-shadow: 0 2px 16px rgba(168, 85, 247, 0.15), 0 1px 0 rgba(236, 72, 153, 0.2);
  border-bottom: 1px solid var(--border);
}

.theme-feminine-dark .header-left .logo-img {
  filter: drop-shadow(0 0 10px var(--glow-pink));
}

.theme-feminine-dark .btn-primary {
  background: linear-gradient(135deg, var(--accent-pink), var(--accent-rose));
  color: #fff;
  box-shadow: 0 2px 15px rgba(236, 72, 153, 0.5);
}

.theme-feminine-dark .btn-primary:hover {
  background: linear-gradient(135deg, #f472b6, #fb7185);
  box-shadow: 0 4px 20px rgba(236, 72, 153, 0.65);
  transform: translateY(-1px);
}

.theme-feminine-dark .btn-done {
  background: linear-gradient(135deg, var(--accent-lavender), var(--accent-purple));
  box-shadow: 0 2px 15px rgba(192, 132, 252, 0.5);
}

.theme-feminine-dark .btn-done:hover {
  background: linear-gradient(135deg, #d8b4fe, #c084fc);
  box-shadow: 0 4px 20px rgba(192, 132, 252, 0.65);
}

.theme-feminine-dark .widget-item:hover {
  box-shadow: 0 0 15px var(--glow-pink);
  border-color: var(--accent-pink);
  transform: translateX(2px);
}

.theme-feminine-dark .canvas-wrapper {
  background:
    radial-gradient(ellipse at 30% 20%, rgba(236, 72, 153, 0.08) 0%, transparent 55%),
    radial-gradient(ellipse at 70% 80%, rgba(168, 85, 247, 0.06) 0%, transparent 55%),
    #0f0818;
}

.theme-feminine-dark .canvas {
  background: var(--bg-primary);
  border-color: var(--border);
  box-shadow:
    0 0 30px rgba(168, 85, 247, 0.15),
    0 4px 24px rgba(0, 0, 0, 0.4);
}

.theme-feminine-dark .canvas-grid {
  background-image:
    linear-gradient(rgba(236, 72, 153, 0.08) 1px, transparent 1px),
    linear-gradient(90deg, rgba(236, 72, 153, 0.08) 1px, transparent 1px);
}

.theme-feminine-dark .placed-widget {
  background: var(--bg-secondary);
  border-color: var(--border-soft);
  box-shadow: 0 2px 12px rgba(168, 85, 247, 0.12), 0 1px 3px rgba(0, 0, 0, 0.3);
}

.theme-feminine-dark .placed-widget:hover {
  box-shadow: 0 0 0 2px var(--accent-pink), 0 4px 20px rgba(236, 72, 153, 0.25);
  border-color: var(--accent-pink);
}

.theme-feminine-dark .placed-widget.selected {
  box-shadow: 0 0 0 2px var(--accent-lavender), 0 4px 20px rgba(192, 132, 252, 0.25);
  border-color: var(--accent-lavender);
}

.theme-feminine-dark .placed-widget .resize-handle {
  background: linear-gradient(135deg, transparent 50%, var(--accent-pink) 50%);
}

.theme-feminine-dark .dash-card-head {
  background: linear-gradient(135deg, var(--bg-tertiary), var(--bg-hover));
  border-bottom: 1px solid var(--border);
}

.theme-feminine-dark .sidebar-mascot {
  background: linear-gradient(to top, rgba(236, 72, 153, 0.1), transparent);
}

.theme-feminine-dark .sidebar-mascot img {
  filter: drop-shadow(0 0 15px rgba(236, 72, 153, 0.4));
}

.theme-feminine-dark .modal {
  background: rgba(18, 9, 30, 0.85);
  backdrop-filter: blur(8px);
}

.theme-feminine-dark .modal-content {
  box-shadow: 0 8px 40px rgba(168, 85, 247, 0.2), 0 2px 8px rgba(0, 0, 0, 0.4);
  border: 1px solid var(--border);
}

.theme-feminine-dark .modal-header {
  background: linear-gradient(135deg, var(--bg-tertiary), var(--bg-hover));
}

.theme-feminine-dark .edit-layout-btn {
  background: linear-gradient(135deg, var(--accent-pink), var(--accent-rose));
  box-shadow: 0 4px 20px rgba(236, 72, 153, 0.5);
}

.theme-feminine-dark .edit-layout-btn:hover {
  background: linear-gradient(135deg, #f472b6, #fb7185);
  box-shadow: 0 6px 30px rgba(236, 72, 153, 0.7);
}

.theme-feminine-dark .tpl-modal-overlay,
.theme-feminine-dark .pin-modal-overlay {
  background: rgba(18, 9, 30, 0.85);
  backdrop-filter: blur(8px);
}

.theme-feminine-dark .toggle-switch input:checked + .toggle-slider {
  background: linear-gradient(135deg, var(--accent-pink), var(--accent-rose));
}

.theme-feminine-dark .widget-verified {
  color: var(--accent-pink);
  background: rgba(236, 72, 153, 0.15);
}

.theme-feminine-dark .header-nav .nav-link:hover {
  color: var(--accent-pink);
}

.theme-feminine-dark .kpi-value.blue { color: var(--accent-lavender) !important; }
.theme-feminine-dark .kpi-value.green { color: var(--accent-green) !important; }
.theme-feminine-dark .kpi-value.orange { color: var(--accent-orange) !important; }
.theme-feminine-dark .kpi-value.red { color: var(--accent-rose) !important; }

.theme-feminine-dark .tz-time {
  color: var(--accent-pink);
}

.theme-feminine-dark ::-webkit-scrollbar-thumb {
  background: var(--border-soft);
}

.theme-feminine-dark ::-webkit-scrollbar-thumb:hover {
  background: var(--accent-lavender);
}

/* Feminine Dark icon overrides */
.theme-feminine-dark .widget-item .widget-icon {
  font-size: 0 !important;
  color: transparent !important;
  position: relative;
  width: 24px;
  height: 24px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.theme-feminine-dark .widget-item .widget-icon::after {
  font-family: 'Phosphor-Light' !important;
  font-size: 20px !important;
  font-weight: normal;
  font-style: normal;
  color: var(--accent-pink) !important;
  text-shadow: 0 0 10px rgba(236, 72, 153, 0.5);
  content: "\eca1";
  position: absolute;
  left: 0;
  top: 0;
}

.theme-feminine-dark .lb-icon {
  font-size: 0 !important;
  color: transparent !important;
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 18px;
  height: 18px;
  margin-right: 6px;
  vertical-align: middle;
}

.theme-feminine-dark .lb-icon::after {
  font-family: 'Phosphor-Light' !important;
  font-size: 14px;
  color: var(--accent-pink);
  text-shadow: 0 0 8px rgba(236, 72, 153, 0.4);
  content: "\eca1";
}

.theme-feminine-dark .lb-icon-lg {
  width: 48px;
  height: 48px;
}

.theme-feminine-dark .lb-icon-lg::after {
  font-size: 42px;
  text-shadow: 0 0 15px rgba(236, 72, 153, 0.5);
}

/* Feminine Dark icon mappings */
.theme-feminine-dark .lb-icon[data-icon="weather"]::after,
.theme-feminine-dark [data-widget="weather"] .widget-icon::after { content: "\ed6f"; }
.theme-feminine-dark .lb-icon[data-icon="clock"]::after,
.theme-feminine-dark [data-widget="clock"] .widget-icon::after { content: "\ea46"; }
.theme-feminine-dark .lb-icon[data-icon="cpu"]::after,
.theme-feminine-dark [data-widget="cpu-memory"] .widget-icon::after { content: "\ea72"; }
.theme-feminine-dark .lb-icon[data-icon="memory"]::after { content: "\e9d1"; }
.theme-feminine-dark .lb-icon[data-icon="disk"]::after,
.theme-feminine-dark [data-widget="disk-usage"] .widget-icon::after { content: "\eb82"; }
.theme-feminine-dark .lb-icon[data-icon="network"]::after,
.theme-feminine-dark [data-widget="network-speed"] .widget-icon::after { content: "\edd1"; }
.theme-feminine-dark .lb-icon[data-icon="docker"]::after,
.theme-feminine-dark [data-widget="docker-status"] .widget-icon::after { content: "\ea7b"; }
.theme-feminine-dark .lb-icon[data-icon="uptime"]::after { content: "\ec98"; }
.theme-feminine-dark .lb-icon[data-icon="broadcast"]::after { content: "\e9d6"; }
.theme-feminine-dark .lb-icon[data-icon="calendar"]::after,
.theme-feminine-dark [data-widget="calendar"] .widget-icon::after { content: "\e9e5"; }
.theme-feminine-dark .lb-icon[data-icon="todo"]::after,
.theme-feminine-dark [data-widget="todo-list"] .widget-icon::after { content: "\ea34"; }
.theme-feminine-dark .lb-icon[data-icon="notes"]::after,
.theme-feminine-dark [data-widget="notes"] .widget-icon::after { content: "\ec13"; }
.theme-feminine-dark .lb-icon[data-icon="chart"]::after,
.theme-feminine-dark [data-widget="kpi-number"] .widget-icon::after { content: "\ea18"; }
.theme-feminine-dark .lb-icon[data-icon="email"]::after,
.theme-feminine-dark [data-widget="email-unread"] .widget-icon::after { content: "\eac5"; }
.theme-feminine-dark .lb-icon[data-icon="github"]::after,
.theme-feminine-dark [data-widget="github-stats"] .widget-icon::after { content: "\eb4f"; }
.theme-feminine-dark .lb-icon[data-icon="image"]::after,
.theme-feminine-dark [data-widget="image"] .widget-icon::after { content: "\eba2"; }
.theme-feminine-dark .lb-icon[data-icon="links"]::after,
.theme-feminine-dark [data-widget="bookmark"] .widget-icon::after { content: "\ebc4"; }
.theme-feminine-dark .lb-icon[data-icon="rss"]::after,
.theme-feminine-dark [data-widget="rss-ticker"] .widget-icon::after { content: "\ecb8"; }
.theme-feminine-dark .lb-icon[data-icon="globe"]::after { content: "\eb5a"; }
.theme-feminine-dark .lb-icon[data-icon="countdown"]::after { content: "\eb95"; }
.theme-feminine-dark .lb-icon[data-icon="quote"]::after { content: "\eca1"; }
.theme-feminine-dark .lb-icon[data-icon="home"]::after { content: "\eb98"; }
.theme-feminine-dark .lb-icon[data-icon="embed"]::after { content: "\e9d8"; }
```

## File: `docs/CNAME`
```
lobsterboard.com
```

## File: `docs/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LobsterBoard — Self-Hosted Dashboard Builder</title>
  <meta name="description" content="A self-hosted, drag-and-drop dashboard builder with live system monitoring, template gallery, dark theme, and 50 widgets. No cloud dependencies. Works standalone or with OpenClaw.">
  <link rel="icon" type="image/png" href="assets/favicon.png">
  <link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <!-- Nav -->
  <nav class="nav">
    <div class="nav-inner">
      <a href="#" class="nav-logo">
        <img src="assets/lobsterboard-logo-final.png" alt="LobsterBoard" height="44">
      </a>
      <div class="nav-links">
        <a href="#features">Features</a>
        <a href="#themes">Themes</a>
        <a href="#widgets">Widgets</a>
        <a href="#screenshot">Demo</a>
        <a href="#quickstart">Quick Start</a>
        <a href="https://github.com/curbob/LobsterBoard" target="_blank" class="btn btn-sm">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
          GitHub
        </a>
      </div>
      <button class="nav-toggle" aria-label="Menu" onclick="document.querySelector('.nav-links').classList.toggle('open')">☰</button>
    </div>
  </nav>

  <!-- Hero -->
  <section class="hero">
    <div class="hero-bg"></div>
    <div class="container hero-content">
      <img src="assets/lobsterboard-logo-hero.png" alt="LobsterBoard Logo" class="hero-logo fade-in">
      <h1 class="fade-in d1">Your Dashboard. Your Server. Your Rules.</h1>
      <p class="hero-sub fade-in d2">A self-hosted, drag-and-drop dashboard builder with live system monitoring, template gallery, dark theme, and <strong>50 widgets</strong>. No cloud. No accounts. No nonsense. <strong>Works standalone — no OpenClaw required.</strong></p>
      <div class="hero-actions fade-in d3">
        <a href="#quickstart" class="btn btn-primary btn-lg">Get Started</a>
        <a href="https://github.com/curbob/LobsterBoard" target="_blank" class="btn btn-outline btn-lg">View on GitHub</a>
      </div>
      <div class="hero-badges fade-in d4">
        <img src="https://img.shields.io/npm/v/lobsterboard?style=flat-square&color=e74c3c&label=npm" alt="npm version">
        <img src="https://img.shields.io/badge/license-BSL--1.1-555?style=flat-square" alt="BSL-1.1 License">
        <img src="https://img.shields.io/badge/widgets-50-e74c3c?style=flat-square" alt="50 Widgets">
        <img src="https://img.shields.io/badge/node-%E2%89%A516-333?style=flat-square&logo=node.js" alt="Node 16+">
      </div>
    </div>
  </section>

  <!-- Features -->
  <section id="features" class="section">
    <div class="container">
      <h2 class="section-title">Why LobsterBoard?</h2>
      <p class="section-sub">Everything you need to build a personal command center — nothing you don't.</p>
      <div class="features-grid">
        <div class="feature-card">
          <div class="feature-icon">🎨</div>
          <h3>Drag & Drop Builder</h3>
          <p>Visual editor with snap grid, resize handles, and a widget sidebar. Press Ctrl+E and start building.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">📡</div>
          <h3>Live System Monitoring</h3>
          <p>CPU, memory, disk, network, and Docker stats stream in real-time via Server-Sent Events.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">🔒</div>
          <h3>Fully Self-Hosted</h3>
          <p>Single Node.js server. No cloud accounts, no telemetry, no external dependencies. Your data stays home.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">⚡</div>
          <h3>Zero Build Step</h3>
          <p>Vanilla JS, vanilla CSS. No React, no Webpack, no transpilation. Clone, install, run. That's it.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">🌙</div>
          <h3>Dark Theme Native</h3>
          <p>Built dark from the ground up with CSS custom properties. Easy on the eyes, beautiful on any screen.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">📦</div>
          <h3>50 Widgets</h3>
          <p>System stats, weather, stocks, crypto, calendars, todos, cameras, Docker, AI usage, and much more.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">📋</div>
          <h3>Template Gallery</h3>
          <p>Export, import, and share dashboard layouts. Auto-captured screenshot previews, merge or replace import modes, and built-in starter templates to get going fast.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">🚀</div>
          <h3>Works Standalone</h3>
          <p>No OpenClaw required. LobsterBoard runs independently as a self-contained dashboard — just Node.js and go. OpenClaw integration is optional.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Themes -->
  <section id="themes" class="section section-dark">
    <div class="container">
      <h2 class="section-title">5 Built-in Themes</h2>
      <p class="section-sub">Switch themes from the dropdown in edit mode. Your choice persists across sessions.</p>
      <div class="themes-grid">
        <div class="theme-card" onclick="openLightbox(this)">
          <img src="assets/themes/theme-default.png" alt="Default Theme" loading="lazy">
          <h4>🌙 Default</h4>
          <p>Dark theme with emoji icons — the classic look</p>
        </div>
        <div class="theme-card" onclick="openLightbox(this)">
          <img src="assets/themes/theme-terminal.png" alt="Terminal Theme" loading="lazy">
          <h4>💻 Terminal</h4>
          <p>Green CRT aesthetic with scanlines and Phosphor icons</p>
        </div>
        <div class="theme-card" onclick="openLightbox(this)">
          <img src="assets/themes/theme-paper.png" alt="Paper Theme" loading="lazy">
          <h4>📜 Paper</h4>
          <p>Warm cream/sepia tones with a vintage feel</p>
        </div>
        <div class="theme-card" onclick="openLightbox(this)">
          <img src="assets/themes/theme-feminine.png" alt="Feminine Theme" loading="lazy">
          <h4>🌸 Feminine</h4>
          <p>Soft pink and lavender pastels with subtle glows</p>
        </div>
        <div class="theme-card" onclick="openLightbox(this)">
          <img src="assets/themes/theme-feminine-dark.png" alt="Feminine Dark Theme" loading="lazy">
          <h4>💜 Feminine Dark</h4>
          <p>Pink and purple accents on a dark background</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Lightbox -->
  <div id="lightbox" class="lightbox" onclick="closeLightbox()">
    <span class="lightbox-close">&times;</span>
    <img id="lightbox-img" src="" alt="">
  </div>

  <!-- Screenshot -->
  <section id="screenshot" class="section">
    <div class="container">
      <h2 class="section-title">See It In Action</h2>
      <p class="section-sub">A real dashboard built with LobsterBoard. Drag, drop, save, done.</p>
      <div class="screenshot-wrap">
        <img src="assets/lobsterboard-screenshot.jpg" alt="LobsterBoard Dashboard" class="screenshot" loading="lazy">
      </div>
      <div class="screenshot-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:30px;">
        <div class="screenshot-wrap">
          <p style="text-align:center;color:#8b949e;margin-bottom:10px;font-size:14px;">✏️ Edit Mode</p>
          <img src="assets/lobsterboard-editor.jpg" alt="LobsterBoard Editor" class="screenshot" loading="lazy">
        </div>
        <div class="screenshot-wrap">
          <p style="text-align:center;color:#8b949e;margin-bottom:10px;font-size:14px;">📋 Template Gallery</p>
          <img src="assets/lobsterboard-templates.jpg" alt="Template Gallery" class="screenshot" loading="lazy">
        </div>
        <div class="screenshot-wrap">
          <p style="text-align:center;color:#8b949e;margin-bottom:10px;font-size:14px;">📦 Template Import</p>
          <img src="assets/lobsterboard-template-detail.jpg" alt="Template Import" class="screenshot" loading="lazy">
        </div>
        <div class="screenshot-wrap">
          <p style="text-align:center;color:#8b949e;margin-bottom:10px;font-size:14px;">🖥️ Dashboard Example</p>
          <img src="assets/lobsterboard-dashboard-2.jpg" alt="Dashboard Example" class="screenshot" loading="lazy">
        </div>
      </div>
    </div>
  </section>

  <!-- Widgets -->
  <section id="widgets" class="section">
    <div class="container">
      <h2 class="section-title">50 Widgets & Counting</h2>
      <p class="section-sub">From system monitoring to smart home — there's a widget for that.</p>
      <div class="widget-categories">
        <div class="widget-cat">
          <h3>🖥️ System Monitoring</h3>
          <ul>
            <li>CPU / Memory</li>
            <li>Disk Usage</li>
            <li>Network Speed</li>
            <li>Uptime Monitor</li>
            <li>Docker Containers</li>
          </ul>
        </div>
        <div class="widget-cat">
          <h3>🤖 AI / LLM Tracking</h3>
          <ul>
            <li>Claude Usage</li>
            <li>GPT Usage</li>
            <li>Gemini Usage</li>
            <li>Combined AI View</li>
            <li>AI Cost Tracker</li>
          </ul>
        </div>
        <div class="widget-cat">
          <h3>⏰ Time & Productivity</h3>
          <ul>
            <li>Clock & World Clock</li>
            <li>Countdown Timer</li>
            <li>Pomodoro Timer</li>
            <li>Todo List</li>
            <li>Calendar (iCal)</li>
            <li>Notes</li>
          </ul>
        </div>
        <div class="widget-cat">
          <h3>💰 Finance & Weather</h3>
          <ul>
            <li>Stock Ticker</li>
            <li>Crypto Prices</li>
            <li>Local Weather</li>
            <li>World Weather</li>
          </ul>
        </div>
        <div class="widget-cat">
          <h3>🏠 Smart Home & Media</h3>
          <ul>
            <li>Indoor Climate</li>
            <li>Camera Feed</li>
            <li>Power Usage</li>
            <li>RSS Ticker</li>
            <li>Now Playing</li>
            <li>Unread Emails</li>
          </ul>
        </div>
        <div class="widget-cat">
          <h3>🔗 Embeds & Utilities</h3>
          <ul>
            <li>Image & Random Image</li>
            <li>Quick Links</li>
            <li>Iframe Embed</li>
            <li>Release Tracker</li>
            <li>API Status</li>
            <li>GitHub Stats</li>
            <li>Headers & Dividers</li>
          </ul>
        </div>
        <div class="widget-cat">
          <h3>🦞 OpenClaw Integration</h3>
          <ul>
            <li>Auth Status</li>
            <li>Release Checker</li>
            <li>Activity List</li>
            <li>Cron Jobs</li>
            <li>System Log</li>
            <li>Active Sessions</li>
            <li>Token Gauge</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- Quick Start -->
  <section id="quickstart" class="section section-dark">
    <div class="container">
      <h2 class="section-title">Up & Running in 30 Seconds</h2>
      <div class="quickstart-grid">
        <div class="quickstart-option">
          <h3>Option A: npm</h3>
          <pre><code><span class="prompt">$</span> npm install lobsterboard
<span class="prompt">$</span> cd node_modules/lobsterboard
<span class="prompt">$</span> node server.cjs</code></pre>
        </div>
        <div class="quickstart-option">
          <h3>Option B: Clone</h3>
          <pre><code><span class="prompt">$</span> git clone https://github.com/curbob/LobsterBoard.git
<span class="prompt">$</span> cd LobsterBoard
<span class="prompt">$</span> npm install
<span class="prompt">$</span> node server.cjs</code></pre>
        </div>
      </div>
      <p class="quickstart-after">Then open <code>http://localhost:8080</code> → press <kbd>Ctrl+E</kbd> → drag widgets → click 💾 Save.</p>
    </div>
  </section>

  <!-- Mascot / CTA -->
  <section class="section cta-section">
    <div class="container cta-inner">
      <img src="assets/lobsterboard-mascot-clean.png" alt="LobsterBoard Mascot" class="mascot">
      <div>
        <h2>Ready to build your dashboard?</h2>
        <p>Open source, BSL-1.1 licensed, and built for tinkerers. Free for non-commercial use. Star us on GitHub and get started today.</p>
        <div class="hero-actions">
          <a href="https://github.com/curbob/LobsterBoard" target="_blank" class="btn btn-primary btn-lg">⭐ Star on GitHub</a>
          <a href="https://www.npmjs.com/package/lobsterboard" target="_blank" class="btn btn-outline btn-lg">View on npm</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer">
    <div class="container footer-inner">
      <div class="footer-left">
        <img src="assets/lobsterboard-logo-white.png" alt="LobsterBoard" height="24">
        <span>BSL-1.1 License · Made with 🦞 by <a href="https://github.com/curbob">curbob</a></span>
      </div>
      <div class="footer-links">
        <a href="https://github.com/curbob/LobsterBoard">GitHub</a>
        <a href="https://www.npmjs.com/package/lobsterboard">npm</a>
        <a href="https://github.com/curbob/LobsterBoard/issues">Issues</a>
      </div>
    </div>
  </footer>

  <script src="script.js"></script>
<!-- Lightbox -->
<div id="lb-lightbox" style="display:none;position:fixed;inset:0;z-index:10000;background:rgba(0,0,0,0.9);justify-content:center;align-items:center;cursor:default;" onclick="this.style.display='none'">
  <div style="position:relative;display:inline-block;" onclick="event.stopPropagation()">
    <img id="lb-lightbox-img" style="max-width:92vw;max-height:92vh;border-radius:8px;box-shadow:0 20px 60px rgba(0,0,0,0.5);">
    <button onclick="document.getElementById('lb-lightbox').style.display='none'" style="position:absolute;top:-12px;right:-12px;background:#30363d;border:2px solid #555;color:#fff;font-size:18px;width:32px;height:32px;border-radius:50%;cursor:pointer;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,0.5);" onmouseover="this.style.background='#da3633'" onmouseout="this.style.background='#30363d'">&times;</button>
  </div>
</div>
<script>
document.querySelectorAll('.screenshot').forEach(img => {
  img.style.cursor = 'zoom-in';
  img.addEventListener('click', () => {
    document.getElementById('lb-lightbox-img').src = img.src;
    document.getElementById('lb-lightbox').style.display = 'flex';
  });
});
</script>
</body>
</html>
```

## File: `docs/script.js`
```javascript
// Scroll-triggered fade-in for sections
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      observer.unobserve(e.target);
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.feature-card, .widget-cat, .quickstart-option, .screenshot-wrap').forEach(el => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(20px)';
  el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
  observer.observe(el);
});

// Add visible class styles
const style = document.createElement('style');
style.textContent = '.visible { opacity: 1 !important; transform: translateY(0) !important; }';
document.head.appendChild(style);

// Close mobile nav on link click
document.querySelectorAll('.nav-links a').forEach(a => {
  a.addEventListener('click', () => {
    document.querySelector('.nav-links').classList.remove('open');
  });
});

// Lightbox for theme screenshots
function openLightbox(card) {
  const img = card.querySelector('img');
  const lightbox = document.getElementById('lightbox');
  const lightboxImg = document.getElementById('lightbox-img');
  lightboxImg.src = img.src;
  lightboxImg.alt = img.alt;
  lightbox.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeLightbox() {
  document.getElementById('lightbox').classList.remove('open');
  document.body.style.overflow = '';
}

// Close lightbox with Escape key
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeLightbox();
});
```

## File: `docs/style.css`
```css
/* LobsterBoard Landing Page */
:root {
  --bg: #0d1117;
  --bg-alt: #161b22;
  --bg-card: #1c2128;
  --border: #30363d;
  --text: #e6edf3;
  --text-dim: #8b949e;
  --red: #e74c3c;
  --red-glow: rgba(231, 76, 60, 0.3);
  --red-dark: #c0392b;
  --radius: 12px;
  --radius-sm: 8px;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html { scroll-behavior: smooth; }

body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

a { color: var(--red); text-decoration: none; }
a:hover { color: #ff6b5a; }

.container { max-width: 1100px; margin: 0 auto; padding: 0 24px; }

/* Nav */
.nav {
  position: fixed; top: 0; left: 0; right: 0; z-index: 100;
  background: rgba(13, 17, 23, 0.85);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border);
}
.nav-inner {
  max-width: 1100px; margin: 0 auto; padding: 0 24px;
  display: flex; align-items: center; justify-content: space-between; height: 60px;
}
.nav-logo img { display: block; }
.nav-links { display: flex; align-items: center; gap: 24px; }
.nav-links a { color: var(--text-dim); font-size: 0.9rem; font-weight: 500; transition: color 0.2s; }
.nav-links a:hover { color: var(--text); }
.nav-toggle { display: none; background: none; border: none; color: var(--text); font-size: 1.4rem; cursor: pointer; }

/* Buttons */
.btn {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 8px 16px; border-radius: var(--radius-sm); font-weight: 600; font-size: 0.875rem;
  border: 1px solid var(--border); color: var(--text); background: var(--bg-card);
  transition: all 0.2s; cursor: pointer; text-decoration: none;
}
.btn:hover { border-color: var(--text-dim); color: var(--text); }
.btn-primary { background: var(--red); border-color: var(--red); color: #fff; }
.btn-primary:hover { background: var(--red-dark); border-color: var(--red-dark); color: #fff; }
.btn-outline { background: transparent; border-color: var(--border); }
.btn-outline:hover { border-color: var(--red); color: var(--red); }
.btn-lg { padding: 12px 28px; font-size: 1rem; border-radius: var(--radius); }
.btn-sm { padding: 6px 12px; font-size: 0.8rem; }

/* Hero */
.hero {
  position: relative; padding: 160px 0 100px; text-align: center; overflow: hidden;
}
.hero-bg {
  position: absolute; inset: 0;
  background: radial-gradient(ellipse at 50% 0%, var(--red-glow) 0%, transparent 60%);
  pointer-events: none;
}
.hero-content { position: relative; }
.hero-logo { width: 320px; margin: 0 auto 32px; display: block; }
.hero h1 { font-size: clamp(2rem, 5vw, 3.2rem); font-weight: 800; letter-spacing: -0.02em; margin-bottom: 16px; }
.hero-sub { font-size: 1.15rem; color: var(--text-dim); max-width: 600px; margin: 0 auto 32px; }
.hero-sub strong { color: var(--text); }
.hero-actions { display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; margin-bottom: 32px; }
.hero-badges { display: flex; gap: 8px; justify-content: center; flex-wrap: wrap; }
.hero-badges img { height: 22px; }

/* Sections */
.section { padding: 100px 0; }
.section-dark { background: var(--bg-alt); }
.section-title {
  font-size: 2rem; font-weight: 800; text-align: center; margin-bottom: 12px;
  letter-spacing: -0.01em;
}
.section-sub {
  text-align: center; color: var(--text-dim); max-width: 550px; margin: 0 auto 48px;
  font-size: 1.05rem;
}

/* Features Grid */
.features-grid {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}
.feature-card {
  background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius);
  padding: 28px; transition: border-color 0.3s, transform 0.3s;
}
.feature-card:hover { border-color: var(--red); transform: translateY(-2px); }
.feature-icon { font-size: 1.8rem; margin-bottom: 12px; }
.feature-card h3 { font-size: 1.1rem; margin-bottom: 8px; }
.feature-card p { color: var(--text-dim); font-size: 0.92rem; line-height: 1.5; }

/* Screenshot */
.screenshot-wrap {
  border-radius: var(--radius); overflow: hidden; border: 1px solid var(--border);
  box-shadow: 0 20px 60px rgba(0,0,0,0.5);
}
.screenshot { width: 100%; display: block; }

/* Widgets */
.widget-categories {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 20px;
}
.widget-cat {
  background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius);
  padding: 24px;
}
.widget-cat h3 { font-size: 1rem; margin-bottom: 12px; color: var(--text); }
.widget-cat ul { list-style: none; }
.widget-cat li {
  padding: 4px 0; color: var(--text-dim); font-size: 0.88rem;
  border-bottom: 1px solid rgba(48,54,61,0.5);
}
.widget-cat li:last-child { border: none; }

/* Quick Start */
.quickstart-grid {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
  gap: 24px; margin-bottom: 32px;
}
.quickstart-option {
  background: var(--bg); border: 1px solid var(--border); border-radius: var(--radius);
  padding: 24px;
}
.quickstart-option h3 { font-size: 1rem; margin-bottom: 16px; color: var(--red); }
pre {
  background: #0a0e14; border-radius: var(--radius-sm); padding: 16px; overflow-x: hidden;
  font-size: 0.85rem; line-height: 1.7; word-break: break-all; white-space: pre-wrap;
}
code { font-family: "SF Mono", "Fira Code", "Cascadia Code", monospace; }
.prompt { color: var(--red); user-select: none; }
.quickstart-after { text-align: center; color: var(--text-dim); font-size: 0.95rem; }
.quickstart-after code { background: var(--bg-card); padding: 2px 8px; border-radius: 4px; font-size: 0.85rem; }
kbd {
  background: var(--bg-card); border: 1px solid var(--border); border-radius: 4px;
  padding: 1px 6px; font-size: 0.82rem; font-family: inherit;
}

/* CTA */
.cta-section { background: var(--bg-alt); }
.cta-inner {
  display: flex; align-items: center; gap: 48px;
}
.mascot { width: 200px; flex-shrink: 0; animation: float 3s ease-in-out infinite; }
.cta-inner h2 { font-size: 1.8rem; margin-bottom: 12px; }
.cta-inner p { color: var(--text-dim); margin-bottom: 24px; }

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

/* Footer */
.footer {
  border-top: 1px solid var(--border); padding: 24px 0;
}
.footer-inner {
  display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px;
}
.footer-left { display: flex; align-items: center; gap: 12px; font-size: 0.85rem; color: var(--text-dim); }
.footer-links { display: flex; gap: 20px; }
.footer-links a { color: var(--text-dim); font-size: 0.85rem; }
.footer-links a:hover { color: var(--text); }

/* Fade-in animations */
.fade-in {
  opacity: 0; transform: translateY(20px);
  animation: fadeIn 0.6s ease forwards;
}
.d1 { animation-delay: 0.15s; }
.d2 { animation-delay: 0.3s; }
.d3 { animation-delay: 0.45s; }
.d4 { animation-delay: 0.6s; }

@keyframes fadeIn {
  to { opacity: 1; transform: translateY(0); }
}

/* Themes Grid */
.themes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
  margin-top: 32px;
}
.theme-card {
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 12px;
  overflow: hidden;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}
.theme-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(0,0,0,0.4);
}
.theme-card img {
  width: 100%;
  height: 180px;
  object-fit: cover;
  object-position: top left;
  border-bottom: 1px solid var(--border);
}
.theme-card h4 {
  margin: 12px 16px 4px;
  font-size: 1.1rem;
}
.theme-card p {
  margin: 0 16px 16px;
  font-size: 0.85rem;
  color: var(--text-dim);
}

/* Lightbox */
.lightbox {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.92);
  z-index: 9999;
  justify-content: center;
  align-items: center;
  cursor: zoom-out;
}
.lightbox.open { display: flex; }
.lightbox img {
  max-width: 95vw;
  max-height: 95vh;
  border-radius: 8px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.6);
}
.lightbox-close {
  position: absolute;
  top: 20px;
  right: 30px;
  font-size: 40px;
  color: #fff;
  cursor: pointer;
  opacity: 0.7;
  transition: opacity 0.2s;
}
.lightbox-close:hover { opacity: 1; }

/* Responsive */
@media (max-width: 768px) {
  .nav-links { display: none; position: absolute; top: 60px; left: 0; right: 0; background: var(--bg); border-bottom: 1px solid var(--border); flex-direction: column; padding: 16px 24px; gap: 12px; }
  .nav-links.open { display: flex; }
  .nav-toggle { display: block; }
  .hero { padding: 120px 0 60px; }
  .hero-logo { width: 220px; }
  .cta-inner { flex-direction: column; text-align: center; }
  .mascot { width: 140px; }
  .quickstart-grid { grid-template-columns: 1fr; }
  .themes-grid { grid-template-columns: 1fr; }
}
```

## File: `js/builder.js`
```javascript
/**
 * OpenClaw Dashboard Builder - Core Logic
 * Handles drag-drop, canvas management, and export
 */

// ─────────────────────────────────────────────
// SECURITY HELPERS
// ─────────────────────────────────────────────

// Escape HTML to prevent XSS attacks
function escapeHtml(str) {
  if (!str) return '';
  const div = document.createElement('div');
  div.textContent = str;
  return div.innerHTML;
}

// ─────────────────────────────────────────────
// STATE
// ─────────────────────────────────────────────

const state = {
  canvas: { width: 1920, height: 1080 },
  zoom: 0.5,
  widgets: [],
  selectedWidget: null,
  draggedWidget: null,
  idCounter: 0,
  fontScale: 1,
  editMode: false, // New: Track edit mode state
  pinVerified: false, // Track if PIN has been verified this session
  hasPin: false, // Whether a PIN is configured
  publicMode: false // Whether public mode is enabled
};

// ─────────────────────────────────────────────
// SCROLLABLE / UNLIMITED HEIGHT HELPERS
// ─────────────────────────────────────────────

function isScrollableMode() {
  return state.canvas.height === 'auto';
}

/** Return the pixel height the canvas should actually use (based on lowest widget + padding). */
function getScrollableCanvasHeight() {
  if (!state.widgets.length) return 1080; // sensible default when empty
  let maxBottom = 0;
  state.widgets.forEach(w => {
    const bottom = w.y + w.height;
    if (bottom > maxBottom) maxBottom = bottom;
  });
  return maxBottom + 100; // 100px breathing room below lowest widget
}

// ─────────────────────────────────────────────
// EDIT MODE
// ─────────────────────────────────────────────

// ─────────────────────────────────────────────
// PIN & PUBLIC MODE
// ─────────────────────────────────────────────

function addPublicUnlockButton() {
  let unlock = document.getElementById('public-unlock');
  if (unlock) return; // already exists
  unlock = document.createElement('button');
  unlock.id = 'public-unlock';
  unlock.textContent = '🔒';
  unlock.title = 'Admin';
  unlock.style.cssText = 'position:fixed;bottom:8px;right:8px;z-index:9999;background:transparent;border:none;color:#6e7681;font-size:12px;cursor:pointer;opacity:0.3;transition:opacity .2s;padding:4px;';
  unlock.addEventListener('mouseenter', () => unlock.style.opacity = '0.8');
  unlock.addEventListener('mouseleave', () => unlock.style.opacity = '0.3');
  unlock.addEventListener('click', () => {
    if (state.hasPin) {
      showPinModal('verify');
    } else {
      openSecurityModal();
    }
  });
  document.body.appendChild(unlock);
}

async function checkAuthStatus() {
  try {
    const res = await fetch('/api/auth/status');
    const data = await res.json();
    state.hasPin = data.hasPin;
    state.publicMode = data.publicMode;
    if (state.publicMode) {
      const editBtn = document.getElementById('btn-edit-layout');
      if (editBtn) editBtn.style.display = 'none';
      addPublicUnlockButton();
    }
  } catch (e) { console.error('Auth status check failed:', e); }
}

function showPinModal(mode) {
  // mode: 'verify', 'set', 'change', 'remove'
  const modal = document.getElementById('pin-modal');
  const title = document.getElementById('pin-modal-title');
  const input = document.getElementById('pin-input');
  const input2 = document.getElementById('pin-input-confirm');
  const currentInput = document.getElementById('pin-input-current');
  const error = document.getElementById('pin-error');
  const confirmGroup = document.getElementById('pin-confirm-group');
  const currentGroup = document.getElementById('pin-current-group');

  error.textContent = '';
  input.value = '';
  input2.value = '';
  currentInput.value = '';

  if (mode === 'verify') {
    title.textContent = '🔒 Enter PIN to Edit';
    confirmGroup.style.display = 'none';
    currentGroup.style.display = 'none';
  } else if (mode === 'set') {
    title.textContent = '🔐 Set Edit PIN';
    confirmGroup.style.display = 'block';
    currentGroup.style.display = 'none';
  } else if (mode === 'change') {
    title.textContent = '🔄 Change PIN';
    confirmGroup.style.display = 'block';
    currentGroup.style.display = 'block';
  } else if (mode === 'remove') {
    title.textContent = '🗑️ Remove PIN';
    confirmGroup.style.display = 'none';
    currentGroup.style.display = 'block';
    input.parentElement.style.display = 'none';
  }

  modal.style.display = 'flex';
  modal.dataset.mode = mode;
  setTimeout(() => (mode === 'change' || mode === 'remove' ? currentInput : input).focus(), 100);
}

function closePinModal() {
  const modal = document.getElementById('pin-modal');
  modal.style.display = 'none';
  // Restore visibility of new PIN input
  document.getElementById('pin-input').parentElement.style.display = '';
  // Clear any pending public mode callback
  if (state._publicModeCallback) {
    state._publicModeCallback = null;
    const toggle = document.getElementById('public-mode-toggle');
    if (toggle) toggle.checked = state.publicMode;
  }
}

async function submitPin() {
  const modal = document.getElementById('pin-modal');
  const mode = modal.dataset.mode;
  const pin = document.getElementById('pin-input').value;
  const pin2 = document.getElementById('pin-input-confirm').value;
  const currentPin = document.getElementById('pin-input-current').value;
  const error = document.getElementById('pin-error');
  error.textContent = '';

  if (mode === 'verify') {
    const res = await fetch('/api/auth/verify-pin', {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ pin })
    });
    const data = await res.json();
    if (data.valid) {
      state.pinVerified = true;
      // If there's a pending public mode toggle, handle that instead of entering edit mode
      if (state._publicModeCallback) {
        const callback = state._publicModeCallback;
        state._publicModeCallback = null; // clear before closePinModal tries to
        closePinModal();
        await callback(pin);
        return;
      }
      // If in public mode (unlock button clicked), disable it and restore edit UI
      if (state.publicMode) {
        state.publicMode = false;
        await fetch('/api/mode', {
          method: 'POST', headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ publicMode: false, pin })
        });
        const editBtn = document.getElementById('btn-edit-layout');
        if (editBtn) editBtn.style.display = '';
        const unlock = document.getElementById('public-unlock');
        if (unlock) unlock.remove();
        const pubToggle = document.getElementById('public-mode-toggle');
        if (pubToggle) pubToggle.checked = false;
      }
      closePinModal();
      setEditMode(true);
    } else {
      error.textContent = 'Incorrect PIN';
    }
  } else if (mode === 'set') {
    if (pin !== pin2) { error.textContent = 'PINs do not match'; return; }
    if (pin.length < 4 || pin.length > 6 || !/^\d+$/.test(pin)) { error.textContent = 'PIN must be 4-6 digits'; return; }
    const res = await fetch('/api/auth/set-pin', {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ pin })
    });
    const data = await res.json();
    if (data.status === 'ok') {
      state.hasPin = true;
      state.pinVerified = true;
      closePinModal();
      setEditMode(true);
    } else { error.textContent = data.error || 'Failed to set PIN'; }
  } else if (mode === 'change') {
    if (pin !== pin2) { error.textContent = 'New PINs do not match'; return; }
    if (pin.length < 4 || pin.length > 6 || !/^\d+$/.test(pin)) { error.textContent = 'PIN must be 4-6 digits'; return; }
    const res = await fetch('/api/auth/set-pin', {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ pin, currentPin })
    });
    const data = await res.json();
    if (data.status === 'ok') {
      closePinModal();
      alert('PIN changed successfully');
    } else { error.textContent = data.error || 'Failed to change PIN'; }
  } else if (mode === 'remove') {
    const res = await fetch('/api/auth/remove-pin', {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ pin: currentPin })
    });
    const data = await res.json();
    if (data.status === 'ok') {
      state.hasPin = false;
      closePinModal();
      alert('PIN removed');
    } else { error.textContent = data.error || 'Failed to remove PIN'; }
  }
}

async function requestEditMode() {
  if (state.publicMode) { alert('Dashboard is in public mode. Editing is disabled.'); return; }
  if (state.hasPin && !state.pinVerified) {
    showPinModal('verify');
  } else if (!state.hasPin) {
    // No PIN set — offer to set one, or go straight to edit
    setEditMode(true);
  } else {
    setEditMode(true);
  }
}

function openSecurityModal() {
  const modal = document.getElementById('security-modal');
  const pinStatus = document.getElementById('pin-status');
  const setBtn = document.getElementById('sec-set-pin');
  const changeBtn = document.getElementById('sec-change-pin');
  const removeBtn = document.getElementById('sec-remove-pin');
  const publicToggle = document.getElementById('public-mode-toggle');

  if (state.hasPin) {
    pinStatus.textContent = 'Active';
    pinStatus.className = 'security-badge active';
    setBtn.style.display = 'none';
    changeBtn.style.display = '';
    removeBtn.style.display = '';
  } else {
    pinStatus.textContent = 'Not Set';
    pinStatus.className = 'security-badge';
    setBtn.style.display = '';
    changeBtn.style.display = 'none';
    removeBtn.style.display = 'none';
  }
  publicToggle.checked = state.publicMode;
  modal.style.display = 'flex';
}

function setEditMode(enable) {
  state.editMode = enable;
  document.body.dataset.mode = enable ? 'edit' : 'view';

  // Toggle button text and handler
  const editLayoutBtn = document.getElementById('btn-edit-layout');
  const saveBtn = document.getElementById('btn-save');

  if (enable) {
    stopWidgetScripts();
    editLayoutBtn.style.display = 'none';
    saveBtn.textContent = '💾 Save';
    saveBtn.removeEventListener('click', exportDashboard);
    saveBtn.addEventListener('click', saveConfig);
    // Ensure builder panels are visible in edit mode
    document.querySelector('.builder-header').style.display = 'flex';
    document.querySelector('.widget-panel').style.display = 'flex';
    document.getElementById('properties-panel').style.display = 'flex';
    document.querySelector('.canvas-info').style.display = 'flex';
    document.getElementById('canvas-wrapper').style.padding = '40px'; // Restore padding
    document.getElementById('canvas').style.border = '2px solid var(--border)'; // Restore border
    document.getElementById('canvas').style.borderRadius = '8px'; // Restore border radius
    document.getElementById('canvas').style.boxShadow = '0 10px 40px rgba(0,0,0,0.5)'; // Restore shadow
    document.querySelector('.canvas-grid').style.display = 'block'; // Show grid
    document.querySelector('.drop-hint').style.display = 'flex'; // Show drop hint
  } else {
    editLayoutBtn.style.display = state.publicMode ? 'none' : 'block';
    saveBtn.textContent = '📦 Export ZIP';
    saveBtn.removeEventListener('click', saveConfig);
    saveBtn.addEventListener('click', exportDashboard);
    // Hide builder panels in view mode
    document.querySelector('.builder-header').style.display = 'none';
    document.querySelector('.widget-panel').style.display = 'none';
    document.getElementById('properties-panel').style.display = 'none';
    document.querySelector('.canvas-info').style.display = 'none';
    document.getElementById('canvas-wrapper').style.padding = '0'; // Remove padding
    document.getElementById('canvas').style.border = 'none'; // Remove border
    document.getElementById('canvas').style.borderRadius = '0'; // Remove border radius
    document.getElementById('canvas').style.boxShadow = 'none'; // Remove shadow
    document.querySelector('.canvas-grid').style.display = 'none'; // Hide grid
    document.querySelector('.drop-hint').style.display = 'none'; // Hide drop hint
  }
  // Re-render widgets to apply new pointer-events
  state.widgets.forEach(widget => {
    const el = document.getElementById(widget.id);
    if (el) {
      el.querySelector('.widget-render').style.pointerEvents = enable ? 'none' : 'auto';
      el.querySelector('.resize-handle').style.display = enable ? 'block' : 'none';
      if (enable) {
        el.style.cursor = 'move';
        el.classList.add('builder-edit-mode'); // Add class for styling in edit mode
      } else {
        el.style.cursor = 'default';
        el.classList.remove('builder-edit-mode'); // Remove class in view mode
      }
    }
  });
  selectWidget(null); // Deselect any widget when mode changes
  updateEmptyState();
  if (!enable) {
    scaleCanvasToFit();
    if (state.widgets.length > 0) {
      executeWidgetScripts();
    }
  } else {
    // Restore edit mode zoom
    const canvas = document.getElementById('canvas');
    canvas.style.transform = `scale(${state.zoom})`;
  }
}

// Execute widget JS for live preview (view mode)
function executeWidgetScripts() {
  // Clear any existing intervals from previous executions
  if (window._widgetIntervals) {
    window._widgetIntervals.forEach(id => clearInterval(id));
  }
  window._widgetIntervals = [];

  // Override setInterval to track widget intervals
  const origSetInterval = window.setInterval;
  window.setInterval = function(fn, ms) {
    const id = origSetInterval(fn, ms);
    window._widgetIntervals.push(id);
    return id;
  };

  state.widgets.forEach(widget => {
    const template = WIDGETS[widget.type];
    if (!template || !template.generateJs) return;
    const props = sanitizeProps({ ...widget.properties, id: 'preview-' + widget.id });
    try {
      const js = template.generateJs(props);
      new Function(js)();
    } catch (e) {
      console.error(`Widget ${widget.type} script error:`, e);
    }
  });

  // Restore original setInterval
  window.setInterval = origSetInterval;
}

function stopWidgetScripts() {
  if (window._widgetIntervals) {
    window._widgetIntervals.forEach(id => clearInterval(id));
    window._widgetIntervals = [];
  }
  // Reset SSE connection so it reconnects fresh on next view
  if (_statsSource) {
    _statsSource.close();
    _statsSource = null;
    _statsCallbacks = [];
  }
}

function scaleCanvasToFit() {
  const canvas = document.getElementById('canvas');
  const vw = window.innerWidth;
  const vh = window.innerHeight;
  const cw = state.canvas.width;

  if (isScrollableMode()) {
    // Scrollable: scale width to fit viewport, height scrolls naturally
    const effectiveHeight = getScrollableCanvasHeight();
    canvas.style.height = effectiveHeight + 'px';
    const scale = vw / cw;
    canvas.style.transform = `scale(${scale})`;
    canvas.style.transformOrigin = 'top left';
    const scaledW = cw * scale;
    const offsetX = Math.max(0, (vw - scaledW) / 2);
    canvas.style.marginLeft = offsetX + 'px';
    canvas.style.marginTop = '0px';
    // Set wrapper height so page scrolls
    const wrapper = document.getElementById('canvas-wrapper');
    wrapper.style.height = (effectiveHeight * scale) + 'px';
    return;
  }

  const ch = state.canvas.height;
  const scale = Math.min(vw / cw, vh / ch);
  canvas.style.transform = `scale(${scale})`;
  canvas.style.transformOrigin = 'top left';
  // Center if there's leftover space
  const scaledW = cw * scale;
  const scaledH = ch * scale;
  const offsetX = Math.max(0, (vw - scaledW) / 2);
  const offsetY = Math.max(0, (vh - scaledH) / 2);
  canvas.style.marginLeft = offsetX + 'px';
  canvas.style.marginTop = offsetY + 'px';
}

// Re-scale on window resize in view mode
window.addEventListener('resize', () => {
  if (!state.editMode) scaleCanvasToFit();
});

function updateEmptyState() {
  if (state.widgets.length === 0) {
    document.body.classList.add('empty-dashboard');
  } else {
    document.body.classList.remove('empty-dashboard');
  }
}

// ─────────────────────────────────────────────
// CONFIG MANAGEMENT
// ─────────────────────────────────────────────

async function loadConfig() {
  try {
    const response = await fetch('/config');
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const config = await response.json();
    
    state.canvas = config.canvas || { width: 1920, height: 1080 };
    state.fontScale = config.fontScale || 1;

    // Restore canvas size dropdown to match loaded config
    const sizeSelect = document.getElementById('canvas-size');
    if (state.canvas.height === 'auto') {
      sizeSelect.value = 'scrollable';
    } else {
      const sizeKey = state.canvas.width + 'x' + state.canvas.height;
      if (sizeSelect.querySelector(`option[value="${sizeKey}"]`)) {
        sizeSelect.value = sizeKey;
      } else {
        sizeSelect.value = 'custom';
      }
    }
    state.widgets = config.widgets || [];
    document.documentElement.style.setProperty('--font-scale', state.fontScale);
    const fontScaleEl = document.getElementById('font-scale');
    if (fontScaleEl) fontScaleEl.value = String(state.fontScale);
    state.idCounter = state.widgets.reduce((maxId, w) => Math.max(maxId, parseInt(w.id.replace('widget-', ''))), 0);

    updateCanvasSize(true); // Preserve zoom on load
    state.widgets.forEach(widget => {
      try {
        renderWidget(widget);
      } catch (e) {
        console.error(`Failed to render widget ${widget.id} (type: ${widget.type}):`, e);
      }
    });
    updateCanvasInfo();
    if (state.widgets.length > 0) {
      document.getElementById('canvas').classList.add('has-widgets');
    }
    console.log('Dashboard config loaded successfully.');
    setEditMode(false); // Start in view mode
    if (state.widgets.length > 0) {
      executeWidgetScripts();
    }
  } catch (error) {
    console.error('Failed to load dashboard config:', error);
    // If config fails to load, start in edit mode with a blank canvas
    setEditMode(true);
  }
}

async function saveConfig() {
  try {
    const configToSave = {
      canvas: state.canvas,
      fontScale: state.fontScale || 1,
      widgets: state.widgets
    };
    const response = await fetch('/config', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(configToSave)
    });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const result = await response.json();
    console.log('Dashboard config saved successfully:', result);
    alert('Dashboard layout saved!');
  } catch (error) {
    console.error('Failed to save dashboard config:', error);
    alert('Failed to save dashboard layout. See console for details.');
  }
}

// ─────────────────────────────────────────────
// HELPERS
// ─────────────────────────────────────────────

// Process widget HTML to conditionally remove header
function processWidgetHtml(html, showHeader) {
  if (showHeader !== false) return html;
  // Remove the dash-card-head element (handles multi-line with newlines)
  const headerRegex = /<div\s+class="dash-card-head"[^>]*>[\s\S]*?<\/div>/i;
  return html.replace(headerRegex, '');
}

// ─────────────────────────────────────────────
// INITIALIZATION
// ─────────────────────────────────────────────

document.addEventListener('DOMContentLoaded', () => {
  initCanvas();
  initDragDrop();
  initControls();
  initProperties();
  loadConfig(); // New: Load config on startup
  // setEditMode(false) is called inside loadConfig()

  // Initialize Edit Layout button
  document.getElementById('btn-edit-layout').addEventListener('click', requestEditMode);
  document.getElementById('btn-done-editing').addEventListener('click', () => {
    saveConfig();
    setEditMode(false);
  });

  // PIN modal buttons
  document.getElementById('pin-submit').addEventListener('click', submitPin);
  document.getElementById('pin-cancel').addEventListener('click', closePinModal);
  document.getElementById('pin-input').addEventListener('keydown', (e) => { if (e.key === 'Enter') submitPin(); });
  document.getElementById('pin-input-confirm').addEventListener('keydown', (e) => { if (e.key === 'Enter') submitPin(); });
  document.getElementById('pin-input-current').addEventListener('keydown', (e) => { if (e.key === 'Enter') submitPin(); });

  // Check auth status on load
  checkAuthStatus();

  // Security modal
  document.getElementById('btn-security').addEventListener('click', openSecurityModal);
  document.getElementById('sec-close').addEventListener('click', () => {
    document.getElementById('security-modal').style.display = 'none';
  });
  document.getElementById('sec-set-pin').addEventListener('click', () => {
    document.getElementById('security-modal').style.display = 'none';
    showPinModal('set');
  });
  document.getElementById('sec-change-pin').addEventListener('click', () => {
    document.getElementById('security-modal').style.display = 'none';
    showPinModal('change');
  });
  document.getElementById('sec-remove-pin').addEventListener('click', () => {
    document.getElementById('security-modal').style.display = 'none';
    showPinModal('remove');
  });
  document.getElementById('public-mode-toggle').addEventListener('change', async (e) => {
    const enable = e.target.checked;
    if (enable && !confirm('Enable Public Mode? This will hide the Edit button and block config APIs.')) {
      e.target.checked = false; return;
    }
    if (state.hasPin) {
      // Use PIN modal instead of prompt() so input is masked
      state._pendingPublicMode = enable;
      document.getElementById('security-modal').style.display = 'none';
      showPinModal('verify');
      // Override the verify handler temporarily
      state._publicModeCallback = async (pin) => {
        const res = await fetch('/api/mode', {
          method: 'POST', headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ publicMode: enable, pin })
        });
        const data = await res.json();
        if (data.status === 'ok') {
          state.publicMode = data.publicMode;
          state._publicModeCallback = null;
          // Reload page for clean state
          location.reload();
          return;
        } else {
          e.target.checked = !enable;
          alert(data.error || 'Failed to change mode');
        }
        state._publicModeCallback = null;
      };
    } else {
      const res = await fetch('/api/mode', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ publicMode: enable })
      });
      const data = await res.json();
      if (data.status === 'ok') {
        state.publicMode = data.publicMode;
        if (data.publicMode) {
          setEditMode(false);
          document.getElementById('btn-edit-layout').style.display = 'none';
          document.getElementById('security-modal').style.display = 'none';
        } else {
          document.getElementById('btn-edit-layout').style.display = '';
        }
      } else {
        e.target.checked = !enable;
        alert(data.error || 'Failed to change mode');
      }
    }
  });

  // Servers modal
  document.getElementById('btn-servers').addEventListener('click', openServersModal);
  document.getElementById('servers-close').addEventListener('click', () => {
    document.getElementById('servers-modal').style.display = 'none';
  });
  document.getElementById('server-add-btn').addEventListener('click', addServer);
  document.getElementById('server-test-btn').addEventListener('click', testServerConnection);
});

async function openServersModal() {
  document.getElementById('servers-modal').style.display = 'flex';
  await loadServersList();
}

async function loadServersList() {
  const container = document.getElementById('servers-list');
  try {
    const res = await fetch('/api/servers');
    const data = await res.json();
    if (!data.servers || data.servers.length === 0) {
      container.innerHTML = '<p style="color:#8b949e;font-size:13px;">No servers configured. Add one below.</p>';
      return;
    }
    container.innerHTML = data.servers.map(s => `
      <div class="server-item" style="display:flex;align-items:center;justify-content:space-between;padding:8px 12px;background:var(--bg-tertiary);border-radius:6px;margin-bottom:8px;">
        <div>
          <strong style="font-size:13px;">${_escHtml(s.name)}</strong>
          ${s.type === 'local' ? '<span style="color:#8b949e;font-size:11px;margin-left:8px;">(built-in)</span>' : `<span style="color:#8b949e;font-size:11px;margin-left:8px;">${_escHtml(s.url || '')} ${s.encrypted ? '🔐' : ''}</span>`}
        </div>
        <div style="display:flex;gap:6px;">
          ${s.type !== 'local' ? `
            <button class="btn btn-sm btn-secondary" onclick="testServer('${s.id}')">Test</button>
            <button class="btn btn-sm btn-danger" onclick="deleteServer('${s.id}')">Delete</button>
          ` : '<span style="color:#3fb950;font-size:12px;">✓ Local</span>'}
        </div>
      </div>
    `).join('');
  } catch (e) {
    container.innerHTML = '<p style="color:#f85149;">Failed to load servers</p>';
  }
}

async function addServer() {
  const name = document.getElementById('server-name').value.trim();
  const url = document.getElementById('server-url').value.trim();
  const apiKey = document.getElementById('server-apikey').value.trim();
  const resultEl = document.getElementById('server-add-result');
  
  if (!name || !url || !apiKey) {
    resultEl.innerHTML = '<span style="color:#f85149;">All fields are required</span>';
    return;
  }
  
  try {
    const res = await fetch('/api/servers', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, url, apiKey })
    });
    const data = await res.json();
    if (data.status === 'success') {
      resultEl.innerHTML = '<span style="color:#3fb950;">✓ Server added</span>';
      document.getElementById('server-name').value = '';
      document.getElementById('server-url').value = '';
      document.getElementById('server-apikey').value = '';
      invalidateServerCache();
      await loadServersList();
    } else {
      resultEl.innerHTML = `<span style="color:#f85149;">${_escHtml(data.error || 'Failed to add')}</span>`;
    }
  } catch (e) {
    resultEl.innerHTML = '<span style="color:#f85149;">Network error</span>';
  }
}

async function testServerConnection() {
  const url = document.getElementById('server-url').value.trim();
  const apiKey = document.getElementById('server-apikey').value.trim();
  const resultEl = document.getElementById('server-add-result');
  
  if (!url || !apiKey) {
    resultEl.innerHTML = '<span style="color:#f85149;">URL and API Key required</span>';
    return;
  }
  
  resultEl.innerHTML = '<span style="color:#8b949e;">Testing...</span>';
  try {
    const res = await fetch(url + '/health', {
      headers: { 'X-API-Key': apiKey },
      signal: AbortSignal.timeout(5000)
    });
    if (res.ok) {
      const data = await res.json();
      const encStatus = data.encrypted ? ' 🔐' : ' ⚠️ unencrypted';
      resultEl.innerHTML = `<span style="color:#3fb950;">✓ Connected to ${_escHtml(data.serverName || 'server')}${encStatus}</span>`;
    } else {
      resultEl.innerHTML = `<span style="color:#f85149;">HTTP ${res.status}</span>`;
    }
  } catch (e) {
    resultEl.innerHTML = `<span style="color:#f85149;">Connection failed: ${_escHtml(e.message)}</span>`;
  }
}

async function testServer(id) {
  try {
    const res = await fetch(`/api/servers/${id}/test`, { method: 'POST' });
    const data = await res.json();
    if (data.status === 'ok') {
      const encStatus = data.localEncryption ? '🔐 Encrypted' : '⚠️ Not encrypted';
      alert(`✓ Connected to ${data.serverName || 'server'}\n${encStatus}`);
    } else {
      alert(`Connection failed: ${data.message || 'Unknown error'}`);
    }
  } catch (e) {
    alert('Network error');
  }
}

async function deleteServer(id) {
  if (!confirm('Delete this server?')) return;
  try {
    const res = await fetch(`/api/servers/${id}`, { method: 'DELETE' });
    const data = await res.json();
    if (data.status === 'success') {
      invalidateServerCache();
      await loadServersList();
    } else {
      alert(data.error || 'Failed to delete');
    }
  } catch (e) {
    alert('Network error');
  }
}

function _escHtml(str) {
  if (!str) return '';
  return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

// Server dropdown for system widgets
let _cachedServers = null;
async function populateServerDropdown(selectedValue) {
  const select = document.getElementById('prop-server');
  if (!select) return;
  
  // Fetch servers if not cached
  if (!_cachedServers) {
    try {
      const res = await fetch('/api/servers');
      const data = await res.json();
      _cachedServers = data.servers || [];
    } catch (e) {
      _cachedServers = [{ id: 'local', name: 'Local', type: 'local' }];
    }
  }
  
  // Populate dropdown
  select.innerHTML = _cachedServers.map(s => 
    `<option value="${_escHtml(s.id)}"${s.id === selectedValue ? ' selected' : ''}>${_escHtml(s.name)}</option>`
  ).join('');
}

// Invalidate server cache when servers are added/deleted
function invalidateServerCache() {
  _cachedServers = null;
}

function initCanvas() {
  const canvas = document.getElementById('canvas');
  updateCanvasSize();

  // Canvas click to deselect
  canvas.addEventListener('click', (e) => {
    if (e.target === canvas || e.target.classList.contains('canvas-grid')) {
      selectWidget(null);
    }
  });
}

function updateCanvasSize(preserveZoom = false) {
  const canvas = document.getElementById('canvas');
  const wrapper = document.getElementById('canvas-wrapper');
  const effectiveHeight = isScrollableMode() ? getScrollableCanvasHeight() : state.canvas.height;

  // Calculate zoom to fit (only if not preserving zoom)
  if (!preserveZoom) {
    const wrapperRect = wrapper.getBoundingClientRect();
    const maxWidth = wrapperRect.width - 80;
    const maxHeight = wrapperRect.height - 80;

    const scaleX = maxWidth / state.canvas.width;
    const scaleY = maxHeight / effectiveHeight;
    state.zoom = Math.min(scaleX, scaleY, 0.6);
  }

  canvas.style.width = state.canvas.width + 'px';
  canvas.style.height = isScrollableMode() ? effectiveHeight + 'px' : state.canvas.height + 'px';
  canvas.style.transform = `scale(${state.zoom})`;
  canvas.dataset.width = state.canvas.width;
  canvas.dataset.height = isScrollableMode() ? 'auto' : state.canvas.height;

  // Toggle scrollable class on body
  document.body.classList.toggle('canvas-scrollable', isScrollableMode());

  updateCanvasInfo();
}

function setZoom(newZoom) {
  state.zoom = Math.max(0.1, Math.min(2, newZoom)); // Clamp between 10% and 200%
  const canvas = document.getElementById('canvas');
  canvas.style.transform = `scale(${state.zoom})`;
  updateCanvasInfo();
}

function zoomIn() {
  setZoom(state.zoom + 0.1);
}

function zoomOut() {
  setZoom(state.zoom - 0.1);
}

function zoomFit() {
  updateCanvasSize(false); // Recalculate fit zoom
}

function zoom100() {
  setZoom(1);
}

// Expose functions globally for onclick handlers
window.zoomIn = zoomIn;
window.zoomOut = zoomOut;
window.zoomFit = zoomFit;
window.zoom100 = zoom100;
window.deleteWidget = deleteWidget;
window.state = state;

function updateCanvasInfo() {
  document.getElementById('canvas-dimensions').textContent =
    `${state.canvas.width} × ${isScrollableMode() ? '∞ (scrollable)' : state.canvas.height}`;
  document.getElementById('widget-count').textContent =
    `${state.widgets.length} widget${state.widgets.length !== 1 ? 's' : ''}`;
  document.getElementById('zoom-level').textContent =
    `${Math.round(state.zoom * 100)}%`;
}

// ─────────────────────────────────────────────
// DRAG & DROP
// ─────────────────────────────────────────────

function initDragDrop() {
  const canvas = document.getElementById('canvas');

  // Widget library items — add privacy badges
  document.querySelectorAll('.widget-item').forEach(item => {
    item.addEventListener('dragstart', onDragStart);
    item.addEventListener('dragend', onDragEnd);
    const widgetType = item.dataset.widget;
    const widgetDef = WIDGETS[widgetType];
    if (widgetDef && widgetDef.privacyWarning) {
      const nameEl = item.querySelector('.widget-name');
      if (nameEl && !nameEl.querySelector('.privacy-badge')) {
        const badge = document.createElement('span');
        badge.className = 'privacy-badge';
        badge.textContent = ' ⚠️';
        badge.title = 'May expose sensitive data when dashboard is public';
        badge.style.cssText = 'font-size:10px;cursor:help;';
        nameEl.appendChild(badge);
      }
    }
  });

  // Canvas drop zone
  canvas.addEventListener('dragover', onDragOver);
  canvas.addEventListener('dragleave', onDragLeave);
  canvas.addEventListener('drop', onDrop);
}

function onDragStart(e) {
  const widgetType = e.target.dataset.widget;
  e.dataTransfer.setData('widget-type', widgetType);
  e.target.classList.add('dragging');
  state.draggedWidget = widgetType;
}

function onDragEnd(e) {
  e.target.classList.remove('dragging');
  state.draggedWidget = null;
}

function onDragOver(e) {
  e.preventDefault();
  document.getElementById('canvas').classList.add('drag-over');
}

function onDragLeave(e) {
  document.getElementById('canvas').classList.remove('drag-over');
}

function onDrop(e) {
  e.preventDefault();
  const canvas = document.getElementById('canvas');
  canvas.classList.remove('drag-over');

  const widgetType = e.dataTransfer.getData('widget-type');
  if (!widgetType || !WIDGETS[widgetType]) return;

  // Calculate drop position relative to canvas
  const canvasRect = canvas.getBoundingClientRect();
  const x = (e.clientX - canvasRect.left) / state.zoom;
  const y = (e.clientY - canvasRect.top) / state.zoom;

  createWidget(widgetType, x, y);
}

// ─────────────────────────────────────────────
// WIDGET MANAGEMENT
// ─────────────────────────────────────────────

function createWidget(type, x, y) {
  const template = WIDGETS[type];
  if (!template) return;

  const id = `widget-${++state.idCounter}`;

  // Center widget on drop point
  const widget = {
    id,
    type,
    x: Math.max(0, Math.round(x - template.defaultWidth / 2)),
    y: Math.max(0, Math.round(y - template.defaultHeight / 2)),
    width: template.defaultWidth,
    height: template.defaultHeight,
    properties: JSON.parse(JSON.stringify(template.properties))
  };

  // Snap to grid (20px)
  widget.x = Math.round(widget.x / 20) * 20;
  widget.y = Math.round(widget.y / 20) * 20;

  // Keep in bounds
  widget.x = Math.min(widget.x, state.canvas.width - widget.width);
  if (!isScrollableMode()) {
    widget.y = Math.min(widget.y, state.canvas.height - widget.height);
  }

  state.widgets.push(widget);

  // In scrollable mode, grow canvas to fit new widget
  if (isScrollableMode()) {
    updateCanvasSize(true);
  }
  renderWidget(widget);
  updateEmptyState();
  selectWidget(id);
  updateCanvasInfo();

  // Show has-widgets state
  document.getElementById('canvas').classList.add('has-widgets');
}

function applyWidgetFontScale(widget) {
  const el = document.getElementById(widget.id);
  if (!el) return;
  const body = el.querySelector('.dash-card-body');
  const render = el.querySelector('.widget-render');
  const adjustment = widget.properties.widgetFontAdjust || 0; // e.g. -25, -10, 0, +10, +25
  if (adjustment !== 0) {
    // Compute effective scale: global + adjustment (additive percentage points)
    const globalScale = state.fontScale || 1;
    const effectiveScale = globalScale + (adjustment / 100);
    // Set --font-scale override on widget body content only (header stays at global)
    const target = body || render;
    if (target) {
      target.style.setProperty('--font-scale', effectiveScale);
      target.style.fontSize = (effectiveScale * 100) + '%';
    }
  } else {
    // No adjustment — inherit global
    const target = body || render;
    if (target) {
      target.style.removeProperty('--font-scale');
      target.style.removeProperty('font-size');
    }
  }
}

function renderWidget(widget) {
  const template = WIDGETS[widget.type];
  if (!template) {
    console.warn(`renderWidget: unknown widget type "${widget.type}" (${widget.id}), skipping`);
    return;
  }
  const canvas = document.getElementById('canvas');

  const el = document.createElement('div');
  el.className = 'placed-widget';
  el.dataset.type = widget.type;
  if (widget.type === 'text-header') {
    el.dataset.showBorder = widget.properties.showBorder ? 'true' : 'false';
  }
  if (widget.type === 'pages-menu' && widget.properties.showBorder === false) {
    el.dataset.showBorder = 'false';
  }
  el.id = widget.id;
  el.style.left = widget.x + 'px';
  el.style.top = widget.y + 'px';
  el.style.width = widget.width + 'px';
  el.style.height = widget.height + 'px';

  // Generate actual widget HTML for realistic preview
  const props = { ...widget.properties, id: 'preview-' + widget.id };
  const widgetContent = processWidgetHtml(template.generateHtml(props), widget.properties.showHeader);

  el.innerHTML = `
    <div class="widget-render">${widgetContent}</div>
    <div class="resize-handle"></div>
  `;

  // Apply initial edit mode styles
  if (state.editMode) {
    el.querySelector('.widget-render').style.pointerEvents = 'none';
    el.querySelector('.resize-handle').style.display = 'block';
    el.style.cursor = 'move';
    el.classList.add('builder-edit-mode');
  } else {
    el.querySelector('.widget-render').style.pointerEvents = 'auto';
    el.querySelector('.resize-handle').style.display = 'none';
    el.style.cursor = 'default';
    el.classList.remove('builder-edit-mode');
  }

  // Click to select
  el.addEventListener('click', (e) => {
    if (state.editMode) {
      e.stopPropagation();
      selectWidget(widget.id);
    }
  });

  // Drag to move
  el.addEventListener('mousedown', (e) => {
    if (state.editMode) {
      if (e.target.classList.contains('resize-handle')) return;
      startDragWidget(e, widget);
    }
  });

  // Resize handle
  el.querySelector('.resize-handle').addEventListener('mousedown', (e) => {
    if (state.editMode) {
      e.stopPropagation();
      startResizeWidget(e, widget);
    }
  });

  canvas.appendChild(el);
  applyWidgetFontScale(widget);
}

function renderWidgetPreview(widget) {
  const template = WIDGETS[widget.type];
  const el = document.getElementById(widget.id);
  if (!el) return;

  if (widget.type === 'text-header') {
    el.dataset.showBorder = widget.properties.showBorder ? 'true' : 'false';
  }

  const props = { ...widget.properties, id: 'preview-' + widget.id };
  const widgetContent = processWidgetHtml(template.generateHtml(props), widget.properties.showHeader);

  const renderDiv = el.querySelector('.widget-render');
  if (renderDiv) {
    renderDiv.innerHTML = widgetContent;
  }
}

function selectWidget(id) {
  // Deselect previous
  document.querySelectorAll('.placed-widget.selected').forEach(el => {
    el.classList.remove('selected');
  });

  state.selectedWidget = id ? state.widgets.find(w => w.id === id) : null;

  if (state.selectedWidget) {
    document.getElementById(id).classList.add('selected');
    showProperties(state.selectedWidget);
  } else {
    hideProperties();
  }
}

function deleteWidget(id) {
  const idx = state.widgets.findIndex(w => w.id === id);
  if (idx === -1) return;

  state.widgets.splice(idx, 1);
  document.getElementById(id)?.remove();
  selectWidget(null);
  updateCanvasInfo();
  updateEmptyState();

  if (state.widgets.length === 0) {
    document.getElementById('canvas').classList.remove('has-widgets');
  }
}

// ─────────────────────────────────────────────
// WIDGET DRAGGING
// ─────────────────────────────────────────────

function startDragWidget(e, widget) {
  if (e.button !== 0) return;

  const el = document.getElementById(widget.id);
  const startX = e.clientX;
  const startY = e.clientY;
  const origX = widget.x;
  const origY = widget.y;

  function onMove(e) {
    const dx = (e.clientX - startX) / state.zoom;
    const dy = (e.clientY - startY) / state.zoom;

    widget.x = Math.round((origX + dx) / 20) * 20;
    widget.y = Math.round((origY + dy) / 20) * 20;

    // Keep in bounds
    widget.x = Math.max(0, Math.min(widget.x, state.canvas.width - widget.width));
    if (isScrollableMode()) {
      widget.y = Math.max(0, widget.y);
    } else {
      widget.y = Math.max(0, Math.min(widget.y, state.canvas.height - widget.height));
    }

    el.style.left = widget.x + 'px';
    el.style.top = widget.y + 'px';

    // In scrollable mode, grow canvas to fit
    if (isScrollableMode()) {
      updateCanvasSize(true);
    }

    updatePropertyInputs();
  }

  function onUp() {
    document.removeEventListener('mousemove', onMove);
    document.removeEventListener('mouseup', onUp);
  }

  document.addEventListener('mousemove', onMove);
  document.addEventListener('mouseup', onUp);
}

function startResizeWidget(e, widget) {
  const el = document.getElementById(widget.id);
  const startX = e.clientX;
  const startY = e.clientY;
  const origW = widget.width;
  const origH = widget.height;

  function onMove(e) {
    const dw = (e.clientX - startX) / state.zoom;
    const dh = (e.clientY - startY) / state.zoom;

    widget.width = Math.round((origW + dw) / 20) * 20;
    widget.height = Math.round((origH + dh) / 20) * 20;

    // Minimum size
    widget.width = Math.max(100, widget.width);
    widget.height = Math.max(60, widget.height);

    // Keep in bounds
    widget.width = Math.min(widget.width, state.canvas.width - widget.x);
    if (!isScrollableMode()) {
      widget.height = Math.min(widget.height, state.canvas.height - widget.y);
    }

    el.style.width = widget.width + 'px';
    el.style.height = widget.height + 'px';

    // In scrollable mode, grow canvas to fit
    if (isScrollableMode()) {
      updateCanvasSize(true);
    }

    updatePropertyInputs();
  }

  function onUp() {
    document.removeEventListener('mousemove', onMove);
    document.removeEventListener('mouseup', onUp);
  }

  document.addEventListener('mousemove', onMove);
  document.addEventListener('mouseup', onUp);
}

// ─────────────────────────────────────────────
// PROPERTIES PANEL
// ─────────────────────────────────────────────

function initProperties() {
  // Position/size inputs
  ['prop-x', 'prop-y', 'prop-width', 'prop-height'].forEach(id => {
    document.getElementById(id).addEventListener('change', onPropertyChange);
  });

  // Title
  document.getElementById('prop-title').addEventListener('input', onPropertyChange);

  // Location fields
  document.getElementById('prop-location').addEventListener('input', onPropertyChange);
  document.getElementById('prop-locations').addEventListener('input', onPropertyChange);
  document.getElementById('prop-units').addEventListener('change', onPropertyChange);

  // API key and endpoint
  document.getElementById('prop-api-key').addEventListener('input', onPropertyChange);
  document.getElementById('prop-api-key-value').addEventListener('input', onPropertyChange);
  document.getElementById('prop-endpoint').addEventListener('input', onPropertyChange);
  if (document.getElementById('prop-server')) {
    document.getElementById('prop-server').addEventListener('change', onPropertyChange);
  }
  if (document.getElementById('prop-directorypath')) {
    document.getElementById('prop-directorypath').addEventListener('input', onPropertyChange);
    document.getElementById('btn-browse-dir').addEventListener('click', () => openDirBrowser());
  }
  document.getElementById('prop-refresh').addEventListener('change', onPropertyChange);
  document.getElementById('prop-widgetfontscale').addEventListener('change', onPropertyChange);
  document.getElementById('prop-timeformat').addEventListener('change', onPropertyChange);

  // Show header checkbox
  document.getElementById('prop-show-header').addEventListener('change', onPropertyChange);

  // Countdown-specific fields
  document.getElementById('prop-targetdate').addEventListener('change', onPropertyChange);
  document.getElementById('prop-show-hours').addEventListener('change', onPropertyChange);
  document.getElementById('prop-show-minutes').addEventListener('change', onPropertyChange);

  // Pomodoro-specific fields
  document.getElementById('prop-work-minutes').addEventListener('change', onPropertyChange);
  document.getElementById('prop-break-minutes').addEventListener('change', onPropertyChange);

  // Show border checkbox
  document.getElementById('prop-showborder').addEventListener('change', onPropertyChange);

  // Columns
  document.getElementById('prop-columns').addEventListener('change', onPropertyChange);

  // Feed URL
  document.getElementById('prop-feedurl').addEventListener('change', onPropertyChange);
  document.getElementById('prop-layout').addEventListener('change', onPropertyChange);

  // Text header fields
  document.getElementById('prop-fontsize').addEventListener('change', onPropertyChange);
  document.getElementById('prop-fontcolor').addEventListener('input', onPropertyChange);
  document.getElementById('prop-textalign').addEventListener('change', onPropertyChange);
  document.getElementById('prop-fontweight').addEventListener('change', onPropertyChange);

  // Line fields
  document.getElementById('prop-linecolor').addEventListener('input', onPropertyChange);
  document.getElementById('prop-linethickness').addEventListener('change', onPropertyChange);

  // Image embed fields
  document.getElementById('prop-imagepath').addEventListener('input', onPropertyChange);
  document.getElementById('prop-imagefile').addEventListener('change', onImageFileSelect);
  document.getElementById('prop-imageurl').addEventListener('input', onPropertyChange);
  document.getElementById('prop-imagelist-file').addEventListener('change', onRandomImageFilesSelect);

  // Quick links
  document.getElementById('prop-link-add').addEventListener('click', onAddQuickLink);

  // Iframe embed
  document.getElementById('prop-embedurl').addEventListener('input', onPropertyChange);

  // Release widget
  document.getElementById('prop-repo').addEventListener('input', onPropertyChange);
  document.getElementById('prop-currentversion').addEventListener('input', onPropertyChange);
  if (document.getElementById('prop-gh-username')) document.getElementById('prop-gh-username').addEventListener('input', onPropertyChange);
  if (document.getElementById('prop-gh-repo')) document.getElementById('prop-gh-repo').addEventListener('input', onPropertyChange);
  if (document.getElementById('prop-gh-apikey')) document.getElementById('prop-gh-apikey').addEventListener('input', onPropertyChange);
  document.getElementById('prop-openclawurl').addEventListener('input', onPropertyChange);

  // Delete button
  document.getElementById('btn-delete-widget').addEventListener('click', () => {
    if (state.selectedWidget) {
      deleteWidget(state.selectedWidget.id);
    }
  });
}

function showProperties(widget) {
  const template = WIDGETS[widget.type];

  document.querySelector('.no-selection').style.display = 'none';
  document.getElementById('properties-form').style.display = 'block';

  document.getElementById('prop-type').value = template.name;
  document.getElementById('prop-title').value = widget.properties.title || '';
  document.getElementById('prop-show-header').checked = widget.properties.showHeader !== false; // default true

  updatePropertyInputs();

  // Hide all optional groups first
  document.getElementById('prop-api-group').style.display = 'none';
  document.getElementById('prop-endpoint-group').style.display = 'none';
  if (document.getElementById('prop-server-group')) document.getElementById('prop-server-group').style.display = 'none';
  if (document.getElementById('prop-directorypath-group')) document.getElementById('prop-directorypath-group').style.display = 'none';
  document.getElementById('prop-location-group').style.display = 'none';
  document.getElementById('prop-locations-group').style.display = 'none';
  document.getElementById('prop-units-group').style.display = 'none';
  document.getElementById('prop-timeformat-group').style.display = 'none';
  document.getElementById('prop-targetdate-group').style.display = 'none';
  document.getElementById('prop-countdown-options-group').style.display = 'none';
  document.getElementById('prop-pomodoro-group').style.display = 'none';
  document.getElementById('prop-imagepath-group').style.display = 'none';
  document.getElementById('prop-imageurl-group').style.display = 'none';
  document.getElementById('prop-imagelist-group').style.display = 'none';
  document.getElementById('prop-quicklinks-group').style.display = 'none';
  document.getElementById('prop-embedurl-group').style.display = 'none';
  document.getElementById('prop-release-group').style.display = 'none';
  if (document.getElementById('prop-github-group')) document.getElementById('prop-github-group').style.display = 'none';
  document.getElementById('prop-openclawurl-group').style.display = 'none';
  document.getElementById('prop-title-hint').style.display = 'none';
  document.getElementById('prop-fontsize-group').style.display = 'none';
  document.getElementById('prop-fontcolor-group').style.display = 'none';
  document.getElementById('prop-textalign-group').style.display = 'none';
  document.getElementById('prop-fontweight-group').style.display = 'none';
  document.getElementById('prop-linecolor-group').style.display = 'none';
  document.getElementById('prop-linethickness-group').style.display = 'none';
  document.getElementById('prop-showborder-group').style.display = 'none';
  document.getElementById('prop-columns-group').style.display = 'none';
  document.getElementById('prop-feedurl-group').style.display = 'none';
  document.getElementById('prop-layout-group').style.display = 'none';

  // Show layout field (pages-menu)
  if (widget.properties.layout !== undefined) {
    document.getElementById('prop-layout-group').style.display = 'block';
    document.getElementById('prop-layout').value = widget.properties.layout || 'vertical';
  }

  // Show text header fields
  if (widget.properties.fontSize !== undefined) {
    document.getElementById('prop-fontsize-group').style.display = 'block';
    document.getElementById('prop-fontsize').value = widget.properties.fontSize || 24;
    document.getElementById('prop-fontcolor-group').style.display = 'block';
    document.getElementById('prop-fontcolor').value = widget.properties.fontColor || '#e6edf3';
    document.getElementById('prop-textalign-group').style.display = 'block';
    document.getElementById('prop-textalign').value = widget.properties.textAlign || 'left';
    document.getElementById('prop-fontweight-group').style.display = 'block';
    document.getElementById('prop-fontweight').value = widget.properties.fontWeight || 'bold';
  }

  // Show border toggle
  if (widget.properties.showBorder !== undefined) {
    document.getElementById('prop-showborder-group').style.display = 'block';
    document.getElementById('prop-showborder').checked = widget.properties.showBorder || false;
  }

  // Show line fields
  if (widget.properties.lineColor !== undefined) {
    document.getElementById('prop-linecolor-group').style.display = 'block';
    document.getElementById('prop-linecolor').value = widget.properties.lineColor || '#30363d';
    document.getElementById('prop-linethickness-group').style.display = 'block';
    document.getElementById('prop-linethickness').value = widget.properties.lineThickness || 2;
  }

  // Show columns field
  const tpl = WIDGETS[widget.type];
  if (widget.properties.columns !== undefined || (tpl && tpl.properties && tpl.properties.columns !== undefined)) {
    document.getElementById('prop-columns-group').style.display = 'block';
    document.getElementById('prop-columns').value = widget.properties.columns || (tpl && tpl.properties && tpl.properties.columns) || 1;
  }

  // Show feed URL field
  const tplFeed = WIDGETS[widget.type];
  if (widget.properties.feedUrl !== undefined || (tplFeed && tplFeed.properties && tplFeed.properties.feedUrl !== undefined)) {
    document.getElementById('prop-feedurl-group').style.display = 'block';
    document.getElementById('prop-feedurl').value = widget.properties.feedUrl || (tplFeed && tplFeed.properties && tplFeed.properties.feedUrl) || '';
  }

  // Show location field (single)
  if (widget.properties.location !== undefined) {
    document.getElementById('prop-location-group').style.display = 'block';
    document.getElementById('prop-location').value = widget.properties.location || '';
  }

  // Show locations field (multi)
  if (widget.properties.locations !== undefined) {
    document.getElementById('prop-locations-group').style.display = 'block';
    document.getElementById('prop-locations').value = widget.properties.locations || '';
  }

  // Show units field
  if (widget.properties.units !== undefined) {
    document.getElementById('prop-units-group').style.display = 'block';
    document.getElementById('prop-units').value = widget.properties.units || 'F';
  }

  // Show time format field
  if (widget.properties.format24h !== undefined) {
    document.getElementById('prop-timeformat-group').style.display = 'block';
    document.getElementById('prop-timeformat').value = widget.properties.format24h ? '24h' : '12h';
  }

  // Show countdown-specific fields
  if (widget.properties.targetDate !== undefined) {
    document.getElementById('prop-targetdate-group').style.display = 'block';
    document.getElementById('prop-targetdate').value = widget.properties.targetDate || '';
    document.getElementById('prop-countdown-options-group').style.display = 'block';
    document.getElementById('prop-show-hours').checked = widget.properties.showHours || false;
    document.getElementById('prop-show-minutes').checked = widget.properties.showMinutes || false;
    // Show title hint for countdown
    document.getElementById('prop-title-hint').textContent = 'Name what you\'re counting down to';
    document.getElementById('prop-title-hint').style.display = 'block';
  }

  // Show pomodoro-specific fields
  if (widget.properties.workMinutes !== undefined) {
    document.getElementById('prop-pomodoro-group').style.display = 'block';
    document.getElementById('prop-work-minutes').value = widget.properties.workMinutes || 25;
    document.getElementById('prop-break-minutes').value = widget.properties.breakMinutes || 5;
  }

  // Show local image fields
  if (widget.properties.imagePath !== undefined) {
    document.getElementById('prop-imagepath-group').style.display = 'block';
    const pathInput = document.getElementById('prop-imagepath');
    const pathHint = document.querySelector('#prop-imagepath-group small');
    // If image is embedded (base64), hide the path input
    if (widget.properties.imagePath && widget.properties.imagePath.startsWith('data:')) {
      pathInput.style.display = 'none';
      pathHint.style.display = 'none';
    } else {
      pathInput.style.display = 'block';
      pathInput.value = widget.properties.imagePath || '';
      pathHint.style.display = 'block';
    }
  }

  // Show web image fields
  if (widget.properties.imageUrl !== undefined) {
    document.getElementById('prop-imageurl-group').style.display = 'block';
    document.getElementById('prop-imageurl').value = widget.properties.imageUrl || '';
  }

  // Show random image fields
  if (widget.properties.images !== undefined || widget.type === 'image-random') {
    document.getElementById('prop-imagelist-group').style.display = 'block';
    if (!widget.properties.images) widget.properties.images = [];
    renderRandomImageList();
  }

  // Show quick links fields
  if (widget.type === 'image-latest' && document.getElementById('prop-directorypath-group')) {
    document.getElementById('prop-directorypath-group').style.display = 'block';
    document.getElementById('prop-directorypath').value = widget.properties.directoryPath || '';
  }

  if (widget.type === 'quick-links') {
    document.getElementById('prop-quicklinks-group').style.display = 'block';
    if (!widget.properties.links) widget.properties.links = [];
    renderQuickLinksList();
  }

  // Show iframe embed fields
  if (widget.properties.embedUrl !== undefined) {
    document.getElementById('prop-embedurl-group').style.display = 'block';
    document.getElementById('prop-embedurl').value = widget.properties.embedUrl || '';
  }

  // Show release widget fields
  if (widget.properties.repo !== undefined) {
    document.getElementById('prop-release-group').style.display = 'block';
    document.getElementById('prop-repo').value = widget.properties.repo || '';
    document.getElementById('prop-currentversion').value = widget.properties.currentVersion || '';
  }

  // Show GitHub stats fields
  if (widget.type === 'github-stats') {
    document.getElementById('prop-github-group').style.display = 'block';
    document.getElementById('prop-gh-username').value = widget.properties.username || '';
    document.getElementById('prop-gh-repo').value = widget.properties.repo || '';
    document.getElementById('prop-gh-apikey').value = widget.properties.apiKey || '';
  }

  // Show OpenClaw URL field
  if (widget.properties.openclawUrl !== undefined) {
    document.getElementById('prop-openclawurl-group').style.display = 'block';
    document.getElementById('prop-openclawurl').value = widget.properties.openclawUrl || '';
  }

  // Show API fields
  if (template.hasApiKey) {
    document.getElementById('prop-api-group').style.display = 'block';
    const apiKeyVarEl = document.getElementById('prop-api-key');
    const apiKeyVarLabel = apiKeyVarEl.previousElementSibling;
    if (template.hideApiKeyVar) {
      apiKeyVarEl.style.display = 'none';
      if (apiKeyVarLabel) apiKeyVarLabel.style.display = 'none';
    } else {
      apiKeyVarEl.style.display = '';
      if (apiKeyVarLabel) apiKeyVarLabel.style.display = '';
      apiKeyVarEl.value = template.apiKeyName || '';
    }
    document.getElementById('prop-api-key-value').value = widget.properties.apiKey || '';
    const noteEl = document.getElementById('prop-api-note');
    if (noteEl) {
      noteEl.textContent = template.properties?.apiKeyNote || '';
      noteEl.style.display = template.properties?.apiKeyNote ? 'block' : 'none';
    }
  }

  // Show endpoint field
  if (widget.properties.endpoint !== undefined) {
    document.getElementById('prop-endpoint-group').style.display = 'block';
    document.getElementById('prop-endpoint').value = widget.properties.endpoint || '';
  }

  // Show server dropdown for system/remote widgets
  const systemWidgets = ['uptime-monitor', 'docker-containers', 'disk-usage', 'network-speed', 'cpu-memory', 'ai-usage', 'openclaw-release', 'auth-status', 'cron-jobs', 'system-log', 'session-count', 'activity-list'];
  const serverGroup = document.getElementById('prop-server-group');
  if (serverGroup && systemWidgets.includes(widget.type)) {
    serverGroup.style.display = 'block';
    populateServerDropdown(widget.properties.server || 'local');
  } else if (serverGroup) {
    serverGroup.style.display = 'none';
  }

  document.getElementById('prop-refresh').value = widget.properties.refreshInterval || 60;

  // Widget font scale (per-widget override)
  document.getElementById('prop-widgetfontscale').value = widget.properties.widgetFontAdjust || '0';

  // Render dynamic extra properties for fields not handled by hardcoded groups
  renderExtraProperties(widget, template);

  // Show widget description
  const descEl = document.getElementById('prop-description');
  if (template.description) {
    descEl.textContent = template.description;
    document.getElementById('prop-description-group').style.display = 'block';
  } else {
    document.getElementById('prop-description-group').style.display = 'none';
  }

  // Show privacy warning for sensitive widgets
  let privWarn = document.getElementById('prop-privacy-warning');
  if (!privWarn) {
    privWarn = document.createElement('div');
    privWarn.id = 'prop-privacy-warning';
    privWarn.style.cssText = 'background:#2d1b00;border:1px solid #d29922;border-radius:6px;padding:8px 10px;margin:8px 0;font-size:11px;color:#d29922;display:none;line-height:1.4;';
    const descGroup = document.getElementById('prop-description-group');
    descGroup.parentNode.insertBefore(privWarn, descGroup.nextSibling);
  }
  if (template.privacyWarning) {
    privWarn.innerHTML = '⚠️ <strong>Privacy Warning:</strong> This widget may display sensitive data (API keys, credentials, personal info) to anyone viewing your dashboard. Public Mode and PIN protection only prevent editing — they do <strong>not</strong> hide widget content.';
    privWarn.style.display = 'block';
  } else {
    privWarn.style.display = 'none';
  }
}

// Properties already handled by hardcoded UI groups
const HANDLED_PROPS = new Set([
  'title', 'showHeader', 'refreshInterval', 'endpoint', 'server', 'path',
  'fontSize', 'fontColor', 'textAlign', 'fontWeight',
  'showBorder', 'lineColor', 'lineThickness', 'columns', 'feedUrl', 'layout',
  'location', 'locations', 'units', 'format24h',
  'targetDate', 'showHours', 'showMinutes',
  'workMinutes', 'breakMinutes',
  'imagePath', 'imageUrl', 'images', 'links',
  'embedUrl', 'repo', 'currentVersion', 'openclawUrl',
  'apiKey', 'apiKeyNote', 'username',
  'widgetFontScale', 'widgetFontAdjust', 'symbols',
  'directoryPath'
]);

// Known select/dropdown options for specific properties
const PROP_OPTIONS = {
  period: ['today', 'week', 'month', 'year'],
  units: ['F', 'C'],
  maxLength: ['0', '50', '100', '150', '200', '300'],
};

const PROP_LABELS = {
  maxLength: { '0': 'No limit', '50': '50 chars', '100': '100 chars', '150': '150 chars', '200': '200 chars', '300': '300 chars' },
};

function renderExtraProperties(widget, template) {
  const container = document.getElementById('prop-extra-container');
  container.innerHTML = '';

  const templateProps = template.properties || {};
  // Merge: show any property in templateProps or widget.properties not in HANDLED_PROPS
  const allKeys = new Set([...Object.keys(templateProps), ...Object.keys(widget.properties)]);

  for (const key of allKeys) {
    if (HANDLED_PROPS.has(key)) continue;

    const defaultVal = templateProps[key];
    const currentVal = widget.properties[key] !== undefined ? widget.properties[key] : defaultVal;
    if (currentVal === undefined) continue;

    const group = document.createElement('div');
    group.className = 'prop-group';

    const label = document.createElement('label');
    // Convert camelCase to readable label
    label.textContent = key.replace(/([A-Z])/g, ' $1').replace(/^./, s => s.toUpperCase());

    let input;

    if (PROP_OPTIONS[key]) {
      // Dropdown
      input = document.createElement('select');
      PROP_OPTIONS[key].forEach(opt => {
        const option = document.createElement('option');
        option.value = opt;
        option.textContent = (PROP_LABELS[key] && PROP_LABELS[key][opt]) || opt.charAt(0).toUpperCase() + opt.slice(1);
        if (String(currentVal) === String(opt)) option.selected = true;
        input.appendChild(option);
      });
    } else if (typeof currentVal === 'boolean' || typeof defaultVal === 'boolean') {
      // Checkbox
      input = document.createElement('input');
      input.type = 'checkbox';
      input.checked = !!currentVal;
      // Style: put checkbox inline with label
      label.style.display = 'inline';
      label.style.marginLeft = '6px';
      group.appendChild(input);
      group.appendChild(label);
      input.dataset.extraProp = key;
      input.dataset.extraType = 'boolean';
      input.addEventListener('change', onExtraPropertyChange);
      container.appendChild(group);
      continue;
    } else if (typeof currentVal === 'number' || typeof defaultVal === 'number') {
      // Number input
      input = document.createElement('input');
      input.type = 'number';
      input.value = currentVal;
    } else if (typeof currentVal === 'string') {
      // Text input
      input = document.createElement('input');
      input.type = 'text';
      input.value = currentVal;
    } else {
      continue; // Skip objects/arrays
    }

    input.dataset.extraProp = key;
    input.dataset.extraType = typeof (defaultVal !== undefined ? defaultVal : currentVal);
    input.addEventListener('change', onExtraPropertyChange);
    input.addEventListener('input', onExtraPropertyChange);

    group.appendChild(label);
    group.appendChild(input);
    container.appendChild(group);
  }
}

function onExtraPropertyChange(e) {
  if (!state.selectedWidget) return;
  const key = e.target.dataset.extraProp;
  const type = e.target.dataset.extraType;

  if (type === 'boolean') {
    state.selectedWidget.properties[key] = e.target.checked;
  } else if (type === 'number') {
    state.selectedWidget.properties[key] = parseFloat(e.target.value) || 0;
  } else {
    state.selectedWidget.properties[key] = e.target.value;
  }
  renderWidgetPreview(state.selectedWidget);
}

function hideProperties() {
  document.querySelector('.no-selection').style.display = 'block';
  document.getElementById('properties-form').style.display = 'none';
}

function updatePropertyInputs() {
  if (!state.selectedWidget) return;

  document.getElementById('prop-x').value = state.selectedWidget.x;
  document.getElementById('prop-y').value = state.selectedWidget.y;
  document.getElementById('prop-width').value = state.selectedWidget.width;
  document.getElementById('prop-height').value = state.selectedWidget.height;
}

function onImageFileSelect(e) {
  if (!state.selectedWidget) return;
  const file = e.target.files[0];
  if (!file) return;
  
  const reader = new FileReader();
  reader.onload = function(event) {
    state.selectedWidget.properties.imagePath = event.target.result;
    // Hide the path input after file is selected
    document.getElementById('prop-imagepath').style.display = 'none';
    document.querySelector('#prop-imagepath-group small').style.display = 'none';
    renderWidgetPreview(state.selectedWidget);
  };
  reader.readAsDataURL(file);
}

function onRandomImageFilesSelect(e) {
  if (!state.selectedWidget) return;
  const files = Array.from(e.target.files);
  if (!files.length) return;
  
  // Initialize images array if needed
  if (!state.selectedWidget.properties.images) {
    state.selectedWidget.properties.images = [];
  }
  
  let loaded = 0;
  files.forEach(file => {
    const reader = new FileReader();
    reader.onload = function(event) {
      state.selectedWidget.properties.images.push({
        name: file.name,
        data: event.target.result
      });
      loaded++;
      if (loaded === files.length) {
        renderRandomImageList();
        // Clear file input
        document.getElementById('prop-imagelist-file').value = '';
      }
    };
    reader.readAsDataURL(file);
  });
}

function renderRandomImageList() {
  if (!state.selectedWidget) return;
  const container = document.getElementById('prop-imagelist-items');
  const images = state.selectedWidget.properties.images || [];
  
  if (images.length === 0) {
    container.innerHTML = '<div style="color:var(--text-muted);font-size:11px;padding:8px 0;">No images added yet</div>';
    return;
  }
  
  container.innerHTML = images.map((img, i) => `
    <div style="display:flex;align-items:center;gap:8px;padding:4px 0;border-bottom:1px solid var(--border);">
      <img src="${escapeHtml(img.data)}" style="width:32px;height:32px;object-fit:cover;border-radius:4px;">
      <span style="flex:1;font-size:11px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">${escapeHtml(img.name)}</span>
      <button onclick="removeRandomImage(${i})" style="background:none;border:none;color:var(--accent-red);cursor:pointer;font-size:14px;" title="Remove">×</button>
    </div>
  `).join('');
}

window.removeRandomImage = function(index) {
  if (!state.selectedWidget || !state.selectedWidget.properties.images) return;
  state.selectedWidget.properties.images.splice(index, 1);
  renderRandomImageList();
};

function onAddQuickLink() {
  if (!state.selectedWidget) return;
  const nameInput = document.getElementById('prop-link-name');
  const urlInput = document.getElementById('prop-link-url');
  
  const name = nameInput.value.trim();
  let url = urlInput.value.trim();
  
  if (!name || !url) return;
  
  // Add https:// if missing
  if (!url.startsWith('http://') && !url.startsWith('https://')) {
    url = 'https://' + url;
  }
  
  if (!state.selectedWidget.properties.links) {
    state.selectedWidget.properties.links = [];
  }
  
  state.selectedWidget.properties.links.push({ name, url });
  renderQuickLinksList();
  renderWidgetPreview(state.selectedWidget);
  
  // Clear inputs
  nameInput.value = '';
  urlInput.value = '';
  nameInput.focus();
}

function renderQuickLinksList() {
  if (!state.selectedWidget) return;
  const container = document.getElementById('prop-quicklinks-items');
  const links = state.selectedWidget.properties.links || [];
  
  if (links.length === 0) {
    container.innerHTML = '<div style="color:var(--text-muted);font-size:11px;padding:8px 0;">No links added yet</div>';
    return;
  }
  
  container.innerHTML = links.map((link, i) => {
    let domain = '';
    try { domain = new URL(link.url).hostname; } catch(e) {}
    const favicon = domain ? 'https://www.google.com/s2/favicons?sz=16&domain=' + encodeURIComponent(domain) : '';
    return `
    <div style="display:flex;align-items:center;gap:8px;padding:4px 0;border-bottom:1px solid var(--border);">
      ${favicon ? `<img src="${escapeHtml(favicon)}" style="width:16px;height:16px;">` : ''}
      <span style="flex:1;font-size:11px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">${escapeHtml(link.name)}</span>
      <button onclick="removeQuickLink(${i})" style="background:none;border:none;color:var(--accent-red);cursor:pointer;font-size:14px;" title="Remove">×</button>
    </div>
  `;
  }).join('');
}

window.removeQuickLink = function(index) {
  if (!state.selectedWidget || !state.selectedWidget.properties.links) return;
  state.selectedWidget.properties.links.splice(index, 1);
  renderQuickLinksList();
  renderWidgetPreview(state.selectedWidget);
};

function onPropertyChange(e) {
  if (!state.selectedWidget) return;

  const widget = state.selectedWidget;
  const el = document.getElementById(widget.id);

  switch (e.target.id) {
    case 'prop-x':
      widget.x = parseInt(e.target.value) || 0;
      el.style.left = widget.x + 'px';
      break;
    case 'prop-y':
      widget.y = parseInt(e.target.value) || 0;
      el.style.top = widget.y + 'px';
      break;
    case 'prop-width':
      widget.width = parseInt(e.target.value) || 100;
      el.style.width = widget.width + 'px';
      break;
    case 'prop-height':
      widget.height = parseInt(e.target.value) || 60;
      el.style.height = widget.height + 'px';
      break;
    case 'prop-title':
      widget.properties.title = e.target.value;
      renderWidgetPreview(widget);
      break;
    case 'prop-show-header':
      widget.properties.showHeader = e.target.checked;
      renderWidgetPreview(widget);
      break;
    case 'prop-showborder':
      widget.properties.showBorder = e.target.checked;
      const el = document.getElementById(widget.id);
      if (el) el.dataset.showBorder = e.target.checked ? 'true' : 'false';
      renderWidgetPreview(widget);
      break;
    case 'prop-layout':
      widget.properties.layout = e.target.value;
      renderWidgetPreview(widget);
      break;
    case 'prop-location':
      widget.properties.location = e.target.value;
      break;
    case 'prop-locations':
      widget.properties.locations = e.target.value;
      break;
    case 'prop-units':
      widget.properties.units = e.target.value;
      break;
    case 'prop-timeformat':
      widget.properties.format24h = e.target.value === '24h';
      break;
    case 'prop-targetdate':
      widget.properties.targetDate = e.target.value;
      renderWidgetPreview(widget);
      break;
    case 'prop-show-hours':
      widget.properties.showHours = e.target.checked;
      break;
    case 'prop-show-minutes':
      widget.properties.showMinutes = e.target.checked;
      break;
    case 'prop-work-minutes':
      widget.properties.workMinutes = parseInt(e.target.value) || 25;
      renderWidgetPreview(widget);
      break;
    case 'prop-break-minutes':
      widget.properties.breakMinutes = parseInt(e.target.value) || 5;
      break;
    case 'prop-imagepath':
      widget.properties.imagePath = e.target.value;
      renderWidgetPreview(widget);
      break;
    case 'prop-imageurl':
      widget.properties.imageUrl = e.target.value;
      renderWidgetPreview(widget);
      break;
    case 'prop-embedurl':
      widget.properties.embedUrl = e.target.value;
      renderWidgetPreview(widget);
      break;
    case 'prop-repo':
      widget.properties.repo = e.target.value;
      break;
    case 'prop-currentversion':
      widget.properties.currentVersion = e.target.value;
      break;
    case 'prop-gh-username':
      widget.properties.username = e.target.value;
      break;
    case 'prop-gh-repo':
      widget.properties.repo = e.target.value;
      break;
    case 'prop-gh-apikey':
      widget.properties.apiKey = e.target.value;
      break;
    case 'prop-openclawurl':
      widget.properties.openclawUrl = e.target.value;
      break;
    case 'prop-api-key-value':
      widget.properties.apiKey = e.target.value;
      break;
    case 'prop-endpoint':
      widget.properties.endpoint = e.target.value;
      break;
    case 'prop-server':
      widget.properties.server = e.target.value;
      break;
    case 'prop-directorypath':
      widget.properties.directoryPath = e.target.value;
      break;
    case 'prop-refresh':
      widget.properties.refreshInterval = parseInt(e.target.value) || 60;
      break;
    case 'prop-widgetfontscale':
      const adj = parseInt(e.target.value) || 0;
      if (adj !== 0) {
        widget.properties.widgetFontAdjust = adj;
      } else {
        delete widget.properties.widgetFontAdjust;
      }
      // Clean up old property if present
      delete widget.properties.widgetFontScale;
      applyWidgetFontScale(widget);
      break;
    case 'prop-fontsize':
      widget.properties.fontSize = parseInt(e.target.value) || 24;
      renderWidgetPreview(widget);
      break;
    case 'prop-fontcolor':
      widget.properties.fontColor = e.target.value;
      renderWidgetPreview(widget);
      break;
    case 'prop-textalign':
      widget.properties.textAlign = e.target.value;
      renderWidgetPreview(widget);
      break;
    case 'prop-fontweight':
      widget.properties.fontWeight = e.target.value;
      renderWidgetPreview(widget);
      break;
    case 'prop-linecolor':
      widget.properties.lineColor = e.target.value;
      renderWidgetPreview(widget);
      break;
    case 'prop-linethickness':
      widget.properties.lineThickness = parseInt(e.target.value) || 2;
      renderWidgetPreview(widget);
      break;
    case 'prop-columns':
      widget.properties.columns = parseInt(e.target.value) || 1;
      renderWidgetPreview(widget);
      break;
    case 'prop-feedurl':
      widget.properties.feedUrl = e.target.value;
      break;
  }
}

// ─────────────────────────────────────────────
// CONTROLS
// ─────────────────────────────────────────────

function initControls() {
  // Canvas size selector
  document.getElementById('canvas-size').addEventListener('change', (e) => {
    if (e.target.value === 'custom') {
      document.getElementById('custom-width').style.display = 'inline-block';
      document.getElementById('custom-x').style.display = 'inline-block';
      document.getElementById('custom-height').style.display = 'inline-block';
    } else if (e.target.value === 'scrollable') {
      document.getElementById('custom-width').style.display = 'none';
      document.getElementById('custom-x').style.display = 'none';
      document.getElementById('custom-height').style.display = 'none';

      state.canvas.width = 1920;
      state.canvas.height = 'auto';
      updateCanvasSize();
    } else {
      document.getElementById('custom-width').style.display = 'none';
      document.getElementById('custom-x').style.display = 'none';
      document.getElementById('custom-height').style.display = 'none';

      const [w, h] = e.target.value.split('x').map(Number);
      state.canvas.width = w;
      state.canvas.height = h;
      updateCanvasSize();
    }
  });

  // Custom size inputs
  ['custom-width', 'custom-height'].forEach(id => {
    document.getElementById(id).addEventListener('change', () => {
      state.canvas.width = parseInt(document.getElementById('custom-width').value) || 1920;
      state.canvas.height = parseInt(document.getElementById('custom-height').value) || 1080;
      updateCanvasSize();
    });
  });

  // Font scale selector
  document.getElementById('font-scale').addEventListener('change', (e) => {
    const scale = parseFloat(e.target.value) || 1;
    state.fontScale = scale;
    document.documentElement.style.setProperty('--font-scale', scale);
    // Reapply per-widget adjustments since they're relative to global
    state.widgets.forEach(w => applyWidgetFontScale(w));
  });

  // Clear button
  document.getElementById('btn-clear').addEventListener('click', () => {
    if (confirm('Clear all widgets?')) {
      state.widgets.forEach(w => document.getElementById(w.id)?.remove());
      state.widgets = [];
      selectWidget(null);
      updateCanvasInfo();
      updateEmptyState();
      document.getElementById('canvas').classList.remove('has-widgets');
    }
  });

  // Preview button
  document.getElementById('btn-preview').addEventListener('click', showPreview);

  // Export button (now Save button)
  document.getElementById('btn-save').addEventListener('click', saveConfig);

  // Close preview
  document.getElementById('close-preview').addEventListener('click', () => {
    document.getElementById('preview-modal').classList.remove('active');
  });

  // Edit layout button
  document.getElementById('btn-edit-layout').addEventListener('click', requestEditMode);

  // Zoom controls - handled via inline onclick in HTML

  // Keyboard shortcuts for zoom and edit mode
  document.addEventListener('keydown', (e) => {
    // Check if not typing in an input/editable element
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.tagName === 'SELECT' || e.target.isContentEditable) return;

    if (e.ctrlKey && e.key === 'e') { // Ctrl+E to toggle edit mode
      e.preventDefault();
      if (state.editMode) setEditMode(false); else requestEditMode();
    } else if (e.key === '=' || e.key === '+') {
      e.preventDefault();
      zoomIn();
    } else if (e.key === '-' || e.key === '_') {
      e.preventDefault();
      zoomOut();
    } else if (e.key === '0') {
      e.preventDefault();
      zoom100();
    } else if (e.key === 'f' || e.key === 'F') {
      e.preventDefault();
      zoomFit();
    } else if (e.key === 'Delete' || e.key === 'Backspace') {
      if (state.selectedWidget && state.editMode) {
        e.preventDefault();
        deleteWidget(state.selectedWidget.id);
      }
    }
  });

  // Mouse wheel zoom (with Ctrl/Cmd)
  document.getElementById('canvas-wrapper').addEventListener('wheel', (e) => {
    if (e.ctrlKey || e.metaKey) {
      e.preventDefault();
      if (e.deltaY < 0) {
        zoomIn();
      } else {
        zoomOut();
      }
    }
  }, { passive: false });
}

// ─────────────────────────────────────────────
// PREVIEW
// ─────────────────────────────────────────────

function showPreview() {
  const css = generateDashboardCss();
  const js = generateDashboardJs();

  const widgetHtml = state.widgets.map(widget => {
    const template = WIDGETS[widget.type];
    if (!template) return '';

    const props = { ...widget.properties, id: widget.id };
    let html = processWidgetHtml(template.generateHtml(props), widget.properties.showHeader);

    return `
      <div class="widget-container" data-widget-id="${widget.id}" style="position:absolute;left:${widget.x}px;top:${widget.y}px;width:${widget.width}px;height:${widget.height}px;">
        ${html}
      </div>`;
  }).join('\n');

  const previewHtml = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dashboard Preview</title>
  <style>${css}</style>
</head>
<body>
  <main class="dashboard" style="width:${state.canvas.width}px;height:${isScrollableMode() ? 'auto' : state.canvas.height + 'px'};min-height:${isScrollableMode() ? getScrollableCanvasHeight() + 'px' : 'auto'};position:relative;">
    ${widgetHtml}
  </main>
  <script>${js}</script>
</body>
</html>`;

  const frame = document.getElementById('preview-frame');
  frame.srcdoc = previewHtml;
  document.getElementById('preview-modal').classList.add('active');
}

// ─────────────────────────────────────────────
// EXPORT
// ─────────────────────────────────────────────

async function exportDashboard() {
  const html = generateDashboardHtml();
  const css = generateDashboardCss();
  const js = generateDashboardJs();

  // Load JSZip dynamically
  if (!window.JSZip) {
    const script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js';
    document.head.appendChild(script);
    await new Promise(resolve => script.onload = resolve);
  }

  // Load html2canvas dynamically
  if (!window.html2canvas) {
    const script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js';
    document.head.appendChild(script);
    await new Promise(resolve => script.onload = resolve);
  }

  const zip = new JSZip();
  zip.file('index.html', html);
  zip.file('css/style.css', css);
  zip.file('js/dashboard.js', js);
  zip.file('README.md', generateReadme());
  zip.file('server.js', generateServerJs());

  // Capture preview screenshot automatically
  try {
    const canvas = document.getElementById('canvas');
    const screenshot = await html2canvas(canvas, {
      backgroundColor: '#0d1117',
      scale: 1,
      useCORS: true,
      allowTaint: true
    });
    const pngBlob = await new Promise(resolve => screenshot.toBlob(resolve, 'image/png'));
    zip.file('preview.png', pngBlob);
  } catch (e) {
    console.warn('Could not generate preview screenshot:', e);
  }

  const blob = await zip.generateAsync({ type: 'blob' });

  // Download
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'openclaw-dashboard.zip';
  a.click();
  URL.revokeObjectURL(url);
}

function generateDashboardHtml() {
  const widgetHtml = state.widgets.map(widget => {
    const template = WIDGETS[widget.type];
    if (!template) return '';

    const props = { ...widget.properties, id: widget.id };
    let html = processWidgetHtml(template.generateHtml(props), widget.properties.showHeader);

    // Wrap in positioned container with data-widget-id for post-export editing
    return `
      <div class="widget-container" data-widget-id="${widget.id}" style="position:absolute;left:${widget.x}px;top:${widget.y}px;width:${widget.width}px;height:${widget.height}px;">
        ${html}
      </div>`;
  }).join('\n');

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My OpenClaw Dashboard</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <main class="dashboard" style="width:${state.canvas.width}px;height:${isScrollableMode() ? 'auto' : state.canvas.height + 'px'};min-height:${isScrollableMode() ? getScrollableCanvasHeight() + 'px' : 'auto'};position:relative;">
    ${widgetHtml}
  </main>
  <script src="js/dashboard.js"></script>
</body>
</html>`;
}

function generateDashboardCss() {
  return `/* OpenClaw Dashboard - Generated Styles */

:root {
  --bg-primary: #0d1117;
  --bg-secondary: #161b22;
  --bg-tertiary: #21262d;
  --bg-hover: #30363d;
  --border: #30363d;
  --text-primary: #e6edf3;
  --text-secondary: #8b949e;
  --text-muted: #6e7681;
  --accent-blue: #58a6ff;
  --accent-green: #3fb950;
  --accent-orange: #d29922;
  --accent-red: #f85149;
  --accent-purple: #a371f7;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: var(--bg-primary);
  color: var(--text-primary);
  min-height: 100vh;
}

.dashboard {
  margin: 0 auto;
  overflow: hidden;
}

.widget-container {
  overflow: hidden;
}

/* KPI Cards */
.kpi-card {
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 16px;
  display: flex;
  align-items: center;
  gap: 12px;
  height: 100%;
}

.kpi-sm {
  padding: 12px;
}

.kpi-icon {
  font-size: 24px;
}

.kpi-data {
  flex: 1;
}

.kpi-value {
  font-size: 20px;
  font-weight: 600;
}

.kpi-value.blue { color: var(--accent-blue); }
.kpi-value.green { color: var(--accent-green); }
.kpi-value.orange { color: var(--accent-orange); }
.kpi-value.red { color: var(--accent-red); }

.kpi-label {
  font-size: 12px;
  color: var(--text-secondary);
  margin-top: 2px;
}

.kpi-indicator {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--text-muted);
}

.kpi-indicator.green { background: var(--accent-green); }
.kpi-indicator.yellow { background: var(--accent-orange); }
.kpi-indicator.red { background: var(--accent-red); }

/* Ring */
.kpi-ring-wrap {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.kpi-ring-sm {
  width: 48px;
  height: 48px;
}

.kpi-ring {
  width: 100%;
  height: 100%;
}

.kpi-ring-label {
  position: absolute;
  font-size: 14px;
  font-weight: 600;
}

/* Dash Cards */
.dash-card {
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  height: 100%;
  overflow: hidden;
}

.dash-card-head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  border-bottom: 1px solid var(--border);
  background: var(--bg-tertiary);
}

.dash-card-title {
  font-size: calc(13px * var(--font-scale, 1));
  font-weight: 600;
}

.dash-card-badge {
  font-size: 11px;
  color: var(--text-secondary);
  background: var(--bg-primary);
  padding: 2px 8px;
  border-radius: 10px;
}

.dash-card-body {
  flex: 1;
  padding: 12px 16px;
  overflow-y: auto;
}

.compact-list {
  font-size: 12px;
}

.syslog-scroll {
  font-family: 'SF Mono', Monaco, monospace;
  font-size: 11px;
}

/* Top Bar */
.topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 20px;
  background: var(--bg-secondary);
  border-bottom: 1px solid var(--border);
  height: 100%;
}

.topbar-left {
  display: flex;
  align-items: center;
  gap: 20px;
}

.topbar-brand {
  font-weight: 600;
  font-size: 14px;
}

.topbar-link {
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 13px;
}

.topbar-link:hover,
.topbar-link.active {
  color: var(--accent-blue);
}

.topbar-right {
  display: flex;
  align-items: center;
  gap: 12px;
}

.topbar-meta {
  font-size: 12px;
  color: var(--text-muted);
}

.topbar-refresh {
  background: var(--bg-tertiary);
  border: 1px solid var(--border);
  color: var(--text-secondary);
  padding: 4px 8px;
  border-radius: 4px;
  cursor: pointer;
}

/* News Ticker */
.news-ticker-wrap {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 16px;
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow: hidden;
  height: 100%;
}

.ticker-label {
  font-size: 16px;
}

.ticker-track {
  flex: 1;
  overflow: hidden;
}

.ticker-content {
  white-space: nowrap;
  animation: ticker 30s linear infinite;
  font-size: 13px;
  color: var(--text-secondary);
}

@keyframes ticker {
  0% { transform: translateX(100%); }
  100% { transform: translateX(-100%); }
}

/* Utilities */
.loading-sm {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.spinner-sm {
  width: 20px;
  height: 20px;
  border: 2px solid var(--bg-tertiary);
  border-top-color: var(--accent-blue);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.error {
  color: var(--accent-red);
  padding: 10px;
  text-align: center;
}

.list-item {
  padding: 6px 0;
  border-bottom: 1px solid var(--border);
}

.list-item:last-child {
  border-bottom: none;
}

.cron-item {
  display: flex;
  justify-content: space-between;
  padding: 6px 0;
  border-bottom: 1px solid var(--border);
}

.cron-name {
  color: var(--text-primary);
}

.cron-next {
  color: var(--text-muted);
  font-size: 11px;
}

.log-line {
  padding: 2px 0;
  border-bottom: 1px solid rgba(48, 54, 61, 0.5);
}

.event-item {
  padding: 8px 0;
  border-bottom: 1px solid var(--border);
}

.weather-row {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 0;
  border-bottom: 1px solid var(--border);
}

.weather-row:last-child {
  border-bottom: none;
}

.weather-icon {
  font-size: 18px;
}

.weather-loc {
  flex: 1;
  color: var(--text-primary);
}

.weather-temp {
  font-weight: 600;
  color: var(--accent-blue);
}

/* World Clock */
.tz-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 0;
  border-bottom: 1px solid var(--border);
}

.tz-row:last-child {
  border-bottom: none;
}

.tz-city {
  color: var(--text-primary);
}

.tz-time {
  font-weight: 600;
  color: var(--accent-blue);
  font-variant-numeric: tabular-nums;
}

.usage-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 0;
  border-bottom: 1px solid var(--border);
}

.usage-row:last-child {
  border-bottom: none;
}

.usage-tokens {
  font-weight: 600;
  color: var(--text-primary);
}

/* Pomodoro Button */
.pomo-btn {
  background: var(--bg-tertiary);
  border: 1px solid var(--border);
  color: var(--text-primary);
  padding: 8px 20px;
  border-radius: 6px;
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.15s ease;
}

.pomo-btn:hover {
  background: var(--bg-hover);
  border-color: var(--accent-blue);
  color: var(--accent-blue);
}

.pomo-btn:active {
  background: var(--bg-secondary);
}

::-webkit-scrollbar {
  width: 6px;
}

::-webkit-scrollbar-track {
  background: var(--bg-primary);
}

::-webkit-scrollbar-thumb {
  background: var(--bg-tertiary);
  border-radius: 3px;
}

/* Post-Export Edit Mode */
.edit-mode .widget-container {
  cursor: move;
  outline: 2px dashed #3b82f6;
  outline-offset: -2px;
}

.edit-mode .widget-container:hover {
  outline-color: #60a5fa;
}

.edit-mode .widget-container.dragging {
  opacity: 0.8;
  z-index: 1000;
}

.resize-handle-edit {
  display: none;
  position: absolute;
  bottom: 0;
  right: 0;
  width: 16px;
  height: 16px;
  cursor: se-resize;
  background: #3b82f6;
  border-radius: 2px 0 0 0;
  z-index: 10;
}

.resize-handle-edit::before {
  content: '';
  position: absolute;
  right: 3px;
  bottom: 3px;
  width: 6px;
  height: 6px;
  border-right: 2px solid white;
  border-bottom: 2px solid white;
}

.edit-mode .resize-handle-edit {
  display: block;
}

#edit-toggle {
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 9999;
  padding: 8px 16px;
  background: #1e293b;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 13px;
  font-weight: 500;
  box-shadow: 0 2px 8px rgba(0,0,0,0.3);
  transition: background 0.15s, transform 0.1s;
}

#edit-toggle:hover {
  background: #334155;
}

#edit-toggle:active {
  transform: scale(0.98);
}

#edit-toggle.active {
  background: #3b82f6;
}
`;
}

function generateEditJs() {
  return `
// ─────────────────────────────────────────────
// POST-EXPORT LAYOUT EDITING
// ─────────────────────────────────────────────

(function() {
  const STORAGE_KEY = 'lobsterboard-layout';
  const GRID_SIZE = 20;
  const MIN_WIDTH = 100;
  const MIN_HEIGHT = 60;
  
  let editMode = false;
  let activeWidget = null;
  let startX, startY, origLeft, origTop, origWidth, origHeight;
  let isResizing = false;

  // Initialize on DOM ready
  document.addEventListener('DOMContentLoaded', initEditMode);

  function initEditMode() {
    // Create edit toggle button
    const btn = document.createElement('button');
    btn.id = 'edit-toggle';
    btn.textContent = '✏️ Edit Layout';
    btn.onclick = toggleEditMode;
    document.body.appendChild(btn);

    // Add resize handles and event listeners to all widgets
    document.querySelectorAll('.widget-container').forEach(initWidget);

    // Load saved positions
    loadPositions();
  }

  function initWidget(widget) {
    // Add resize handle
    const handle = document.createElement('div');
    handle.className = 'resize-handle-edit';
    widget.appendChild(handle);

    // Drag to move
    widget.addEventListener('mousedown', onWidgetMouseDown);
    
    // Resize handle
    handle.addEventListener('mousedown', onResizeMouseDown);
  }

  function toggleEditMode() {
    editMode = !editMode;
    document.body.classList.toggle('edit-mode', editMode);
    document.getElementById('edit-toggle').classList.toggle('active', editMode);
    document.getElementById('edit-toggle').textContent = editMode ? '💾 Save Layout' : '✏️ Edit Layout';
    
    if (!editMode) {
      savePositions();
    }
  }

  function onWidgetMouseDown(e) {
    if (!editMode) return;
    if (e.target.classList.contains('resize-handle-edit')) return;
    if (e.button !== 0) return;

    e.preventDefault();
    activeWidget = e.currentTarget;
    isResizing = false;
    
    startX = e.clientX;
    startY = e.clientY;
    origLeft = activeWidget.offsetLeft;
    origTop = activeWidget.offsetTop;

    activeWidget.classList.add('dragging');
    
    document.addEventListener('mousemove', onMouseMove);
    document.addEventListener('mouseup', onMouseUp);
  }

  function onResizeMouseDown(e) {
    if (!editMode) return;
    e.preventDefault();
    e.stopPropagation();
    
    activeWidget = e.target.parentElement;
    isResizing = true;
    
    startX = e.clientX;
    startY = e.clientY;
    origWidth = activeWidget.offsetWidth;
    origHeight = activeWidget.offsetHeight;

    activeWidget.classList.add('dragging');
    
    document.addEventListener('mousemove', onMouseMove);
    document.addEventListener('mouseup', onMouseUp);
  }

  function onMouseMove(e) {
    if (!activeWidget) return;

    const dx = e.clientX - startX;
    const dy = e.clientY - startY;

    if (isResizing) {
      // Resize
      const newWidth = Math.max(MIN_WIDTH, origWidth + dx);
      const newHeight = Math.max(MIN_HEIGHT, origHeight + dy);
      activeWidget.style.width = newWidth + 'px';
      activeWidget.style.height = newHeight + 'px';
    } else {
      // Move
      const newLeft = Math.max(0, origLeft + dx);
      const newTop = Math.max(0, origTop + dy);
      activeWidget.style.left = newLeft + 'px';
      activeWidget.style.top = newTop + 'px';
    }
  }

  function onMouseUp() {
    if (!activeWidget) return;

    // Snap to grid
    if (isResizing) {
      activeWidget.style.width = snapToGrid(activeWidget.offsetWidth) + 'px';
      activeWidget.style.height = snapToGrid(activeWidget.offsetHeight) + 'px';
    } else {
      activeWidget.style.left = snapToGrid(activeWidget.offsetLeft) + 'px';
      activeWidget.style.top = snapToGrid(activeWidget.offsetTop) + 'px';
    }

    activeWidget.classList.remove('dragging');
    activeWidget = null;
    isResizing = false;
    
    document.removeEventListener('mousemove', onMouseMove);
    document.removeEventListener('mouseup', onMouseUp);
  }

  function snapToGrid(value) {
    return Math.round(value / GRID_SIZE) * GRID_SIZE;
  }

  function savePositions() {
    const positions = {};
    document.querySelectorAll('.widget-container').forEach(widget => {
      const id = widget.dataset.widgetId;
      if (id) {
        positions[id] = {
          left: widget.offsetLeft,
          top: widget.offsetTop,
          width: widget.offsetWidth,
          height: widget.offsetHeight
        };
      }
    });
    
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(positions));
      console.log('Layout saved');
    } catch (e) {
      console.warn('Failed to save layout:', e);
    }
  }

  function loadPositions() {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (!saved) return;
      
      const positions = JSON.parse(saved);
      document.querySelectorAll('.widget-container').forEach(widget => {
        const id = widget.dataset.widgetId;
        const pos = positions[id];
        if (pos) {
          widget.style.left = pos.left + 'px';
          widget.style.top = pos.top + 'px';
          widget.style.width = pos.width + 'px';
          widget.style.height = pos.height + 'px';
        }
      });
      console.log('Layout restored from localStorage');
    } catch (e) {
      console.warn('Failed to load saved layout:', e);
    }
  }
})();
`;
}

function sanitizeProps(props) {
  const safe = { ...props };
  for (const key of Object.keys(safe)) {
    if (typeof safe[key] === 'string') {
      safe[key] = safe[key].replace(/[`$\\]/g, '\\$&').replace(/'/g, "\\'").replace(/"/g, '\\"');
    }
  }
  return safe;
}

function generateDashboardJs() {
  const widgetJs = state.widgets.map(widget => {
    const template = WIDGETS[widget.type];
    if (!template || !template.generateJs) return '';

    const props = sanitizeProps({ ...widget.properties, id: widget.id });
    return template.generateJs(props);
  }).join('\n\n');

  const editJs = generateEditJs();

  return `/**
 * OpenClaw Dashboard - Generated JavaScript
 * Replace YOUR_*_API_KEY placeholders with your actual API keys
 */

document.addEventListener('DOMContentLoaded', () => {
  console.log('Dashboard loaded');
});

${widgetJs}

${editJs}
`;
}

function generateServerJs() {
  return `/**
 * LobsterBoard Dashboard Server
 * 
 * A server that:
 * - Serves your dashboard static files
 * - Provides OpenClaw data via CLI commands (not HTTP proxy)
 * 
 * Usage: node server.js
 * 
 * Environment variables:
 *   PORT - Server port (default: 8080)
 *   HOST - Bind address (default: 127.0.0.1 for security)
 * 
 * Security: By default binds to localhost only. To expose on network:
 *   HOST=0.0.0.0 node server.js
 *   ⚠️  Only do this on trusted networks!
 */

const http = require('http');
const fs = require('fs');
const path = require('path');
const os = require('os');
const { execSync } = require('child_process');

const PORT = process.env.PORT || 8080;
const HOST = process.env.HOST || '127.0.0.1';

const MIME_TYPES = {
  '.html': 'text/html', '.css': 'text/css', '.js': 'application/javascript',
  '.json': 'application/json', '.png': 'image/png', '.jpg': 'image/jpeg',
  '.gif': 'image/gif', '.svg': 'image/svg+xml', '.ico': 'image/x-icon'
};

// Cache for expensive CLI operations (30 second TTL)
let statusCache = { data: null, timestamp: 0 };
let cronCache = { data: null, timestamp: 0 };
let activityCache = { data: null, timestamp: 0 };
let logsCache = { data: null, timestamp: 0 };
const CACHE_TTL = 30000;

// Run openclaw CLI command and return output
function runOpenClawCmd(args) {
  try {
    return execSync(\`openclaw \${args}\`, { 
      encoding: 'utf8',
      timeout: 10000,
      stdio: ['pipe', 'pipe', 'pipe']
    });
  } catch (e) {
    console.error(\`openclaw \${args} failed:\`, e.message);
    return null;
  }
}

// Parse openclaw status output
function parseStatus() {
  const now = Date.now();
  if (statusCache.data && (now - statusCache.timestamp) < CACHE_TTL) {
    return statusCache.data;
  }

  const output = runOpenClawCmd('status');
  if (!output) return null;

  const versionOutput = runOpenClawCmd('--version');
  const currentVersion = versionOutput ? versionOutput.trim() : 'unknown';

  const data = {
    authMode: 'unknown',
    version: currentVersion,
    sessions: 0,
    gateway: 'unknown'
  };

  // Detect auth mode from status output
  if (output.includes('oauth') || output.includes('claude-cli')) {
    data.authMode = 'oauth';
  } else if (output.includes('api-key') || output.match(/sk-ant-/)) {
    data.authMode = 'api-key';
  } else {
    data.authMode = 'oauth';
  }

  // Look for version update info
  const versionMatch = output.match(/npm update ([\\\\d.-]+)/);
  if (versionMatch) data.latestVersion = versionMatch[1];

  // Look for sessions count
  const sessionsMatch = output.match(/sessions?\\\\s+(\\\\d+)/i);
  if (sessionsMatch) data.sessions = parseInt(sessionsMatch[1]);

  // Look for gateway status
  if (output.includes('running')) data.gateway = 'running';

  statusCache = { data, timestamp: now };
  return data;
}

// Parse cron jobs via CLI
function parseCronJobs() {
  const now = Date.now();
  if (cronCache.data && (now - cronCache.timestamp) < CACHE_TTL) {
    return cronCache.data;
  }

  const output = runOpenClawCmd('cron list --json');
  let jobs = [];
  try {
    if (output) {
      const parsed = JSON.parse(output);
      // Transform jobs to widget-expected format
      jobs = (parsed.jobs || []).map(job => ({
        name: job.name || job.id || 'Unnamed',
        next: job.state?.nextRunAtMs 
          ? new Date(job.state.nextRunAtMs).toLocaleString('en-US', { 
              month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit' 
            })
          : (job.schedule?.expr || '—'),
        enabled: job.enabled !== false,
        lastStatus: job.state?.lastStatus || null
      }));
    }
  } catch (e) {
    console.error('Failed to parse cron jobs:', e.message);
  }

  const data = { jobs };
  cronCache = { data, timestamp: now };
  return data;
}

// Response helpers
function sendSuccess(res, data) {
  res.writeHead(200, { 
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*'
  });
  res.end(JSON.stringify({ status: 'ok', data }));
}

function sendError(res, message, statusCode = 500) {
  res.writeHead(statusCode, { 
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*'
  });
  res.end(JSON.stringify({ status: 'error', message }));
}

// API handlers
const API_HANDLERS = {
  '/api/status': (req, res) => {
    const data = parseStatus();
    if (!data) {
      sendError(res, 'Failed to get OpenClaw status');
      return;
    }
    sendSuccess(res, data);
  },

  '/api/cron': (req, res) => {
    const data = parseCronJobs();
    sendSuccess(res, data);
  },

  '/api/activity': (req, res) => {
    const now = Date.now();
    if (activityCache.data && (now - activityCache.timestamp) < CACHE_TTL) {
      sendSuccess(res, activityCache.data);
      return;
    }

    const cronRunsDir = path.join(os.homedir(), '.openclaw', 'cron', 'runs');
    const cronJobsFile = path.join(os.homedir(), '.openclaw', 'cron', 'jobs.json');
    
    // Build job ID to name mapping
    let jobMap = {};
    try {
      if (fs.existsSync(cronJobsFile)) {
        const jobsData = JSON.parse(fs.readFileSync(cronJobsFile, 'utf8'));
        jobMap = Object.fromEntries((jobsData.jobs || []).map(j => [j.id, j.name || j.id]));
      }
    } catch (e) { /* ignore */ }

    // Read all run files and merge entries
    let allRuns = [];
    try {
      if (fs.existsSync(cronRunsDir)) {
        const files = fs.readdirSync(cronRunsDir).filter(f => f.endsWith('.jsonl'));
        for (const file of files) {
          try {
            const content = fs.readFileSync(path.join(cronRunsDir, file), 'utf8');
            const lines = content.trim().split('\\n').filter(l => l.trim());
            for (const line of lines) {
              try {
                const entry = JSON.parse(line);
                if (entry.ts && entry.action === 'finished') {
                  allRuns.push(entry);
                }
              } catch (e) { /* skip malformed lines */ }
            }
          } catch (e) { /* skip unreadable files */ }
        }
      }
    } catch (e) { /* ignore */ }

    // Sort by timestamp descending and take last 15
    allRuns.sort((a, b) => b.ts - a.ts);
    const recentRuns = allRuns.slice(0, 15);

    const items = recentRuns.map(run => {
      const jobName = jobMap[run.jobId] || run.jobId || 'Unknown Job';
      const duration = run.durationMs ? \`(\${Math.round(run.durationMs / 1000)}s)\` : '';
      const summary = run.summary ? \`: \${run.summary.slice(0, 50)}\` : '';
      return {
        text: \`\${jobName} \${duration}\${summary}\`,
        time: new Date(run.ts).toISOString(),
        status: run.status || 'unknown'
      };
    });

    // Fallback if no runs found
    if (items.length === 0) {
      items.push({ text: 'No recent activity', time: new Date().toISOString(), status: 'info' });
    }

    const data = { items };
    activityCache = { data, timestamp: now };
    sendSuccess(res, data);
  },

  '/api/logs': (req, res) => {
    const now = Date.now();
    if (logsCache.data && (now - logsCache.timestamp) < CACHE_TTL) {
      sendSuccess(res, logsCache.data);
      return;
    }

    const logPath = path.join(os.homedir(), '.openclaw', 'logs', 'gateway.log');
    let lines = [];

    try {
      if (fs.existsSync(logPath)) {
        const content = fs.readFileSync(logPath, 'utf8');
        const rawLines = content.split('\\n').filter(l => l.trim());
        // Take last 75 lines, reverse for newest first
        const recentLines = rawLines.slice(-75).reverse();
        
        lines = recentLines.map(line => {
          // Parse format: TIMESTAMP [subsystem] message
          const match = line.match(/^(\\S+)\\s+\\[(\\w+)\\]\\s+(.*)$/);
          if (match) {
            return { time: match[1], subsystem: match[2], message: match[3] };
          }
          return { raw: line };
        });
      } else {
        lines = [{ message: 'Log file not found', subsystem: 'info' }];
      }
    } catch (e) {
      lines = [{ message: \`Error reading logs: \${e.message}\`, subsystem: 'error' }];
    }

    const data = { lines };
    logsCache = { data, timestamp: now };
    sendSuccess(res, data);
  },

  '/api/sessions': (req, res) => {
    const status = parseStatus();
    sendSuccess(res, { count: status?.sessions || 0 });
  }
};

// Static file server with path traversal protection
function serveStatic(filePath, res) {
  if (filePath === '/') filePath = '/index.html';
  const fullPath = path.resolve(__dirname, '.' + filePath);
  
  // Prevent path traversal attacks
  if (!fullPath.startsWith(path.resolve(__dirname))) {
    res.writeHead(403, { 'Content-Type': 'text/plain' });
    res.end('Forbidden');
    return;
  }
  
  const ext = path.extname(fullPath).toLowerCase();
  
  fs.readFile(fullPath, (err, data) => {
    if (err) {
      res.writeHead(err.code === 'ENOENT' ? 404 : 500);
      res.end(err.code === 'ENOENT' ? 'Not Found' : 'Server Error');
      return;
    }
    res.writeHead(200, { 'Content-Type': MIME_TYPES[ext] || 'application/octet-stream' });
    res.end(data);
  });
}

const server = http.createServer((req, res) => {
  const pathname = new URL(req.url, 'http://' + req.headers.host).pathname;
  
  // CORS preflight
  if (req.method === 'OPTIONS') {
    res.writeHead(204, {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type'
    });
    res.end();
    return;
  }
  
  // API endpoints
  if (API_HANDLERS[pathname]) {
    API_HANDLERS[pathname](req, res);
    return;
  }
  
  // Static files
  serveStatic(pathname, res);
});

// Graceful shutdown
process.on('SIGTERM', () => server.close(() => process.exit(0)));
process.on('SIGINT', () => server.close(() => process.exit(0)));

server.listen(PORT, HOST, () => {
  console.log(\`
🦞 LobsterBoard Dashboard Server

   Dashboard: http://\${HOST}:\${PORT}
   
   API Endpoints:
   • /api/status   - Auth mode & version
   • /api/cron     - Cron jobs list  
   • /api/activity - Activity feed
   • /api/logs     - System logs
   • /api/sessions - Session count
   
\${HOST === '127.0.0.1' ? '   ✓ Bound to localhost (secure)' : '   ⚠️  Exposed to network'}

   Press Ctrl+C to stop
\`);
});
`;
}

function generateReadme() {
  const apiKeys = [];
  const needsOpenClaw = state.widgets.some(w => 
    ['openclaw-release', 'auth-status', 'activity-list', 'cron-jobs', 'system-log', 'session-count', 'token-gauge'].includes(w.type)
  );
  
  state.widgets.forEach(widget => {
    const template = WIDGETS[widget.type];
    if (template?.hasApiKey && template.apiKeyName) {
      if (!apiKeys.includes(template.apiKeyName)) {
        apiKeys.push(template.apiKeyName);
      }
    }
  });

  return `# LobsterBoard Dashboard

This dashboard was generated with LobsterBoard Dashboard Builder.

## ⚠️ Security Notice

**Never blindly trust scripts from the internet.**

Before running \`server.js\`, we recommend reviewing it for security:

\`\`\`
Hey [Your AI Assistant], please review the server.js file in this folder 
and check for any security concerns, suspicious code, or potential issues.
\`\`\`

The server.js included here uses the OpenClaw CLI to query data locally
(no network proxying). It binds to localhost by default for security. 
But always verify for yourself!

---

## Quick Start

${needsOpenClaw ? `### Running with OpenClaw widgets

Your dashboard includes widgets that connect to OpenClaw. The server uses
the OpenClaw CLI to query data, so make sure OpenClaw is installed and configured.

\`\`\`bash
# Make sure OpenClaw CLI is available:
openclaw status

# Then start the dashboard:
node server.js
\`\`\`

Open http://localhost:8080 in your browser.

### Configuration

**Environment variables:**

| Variable | Default | Description |
|----------|---------|-------------|
| \`PORT\` | 8080 | Server port |
| \`HOST\` | 127.0.0.1 | Bind address (localhost = secure) |

**Examples:**
\`\`\`bash
# Custom port
PORT=3000 node server.js

# Expose to network (trusted networks only!)
HOST=0.0.0.0 node server.js
\`\`\`

### Set It and Forget It (Auto-Start)

To have your dashboard start automatically on boot:

\`\`\`bash
# Install pm2 (process manager)
npm install -g pm2

# Start the dashboard
pm2 start server.js --name my-dashboard

# Save the process list
pm2 save

# Set up auto-start on boot
pm2 startup
# (follow the instructions it prints)
\`\`\`

**Useful pm2 commands:**
- \`pm2 status\` - Check if running
- \`pm2 logs my-dashboard\` - View logs
- \`pm2 restart my-dashboard\` - Restart
- \`pm2 stop my-dashboard\` - Stop

### Without server (static only)
` : ''}
Open \`index.html\` directly, or serve with any static file server.
Note: OpenClaw widgets won't work without the server proxy.

## Files

| File | Description |
|------|-------------|
| \`index.html\` | Dashboard page |
| \`css/style.css\` | Styles |
| \`js/dashboard.js\` | Widget logic |
| \`server.js\` | Server with OpenClaw API proxy |

${apiKeys.length > 0 ? `## API Keys

Edit \`js/dashboard.js\` and replace these placeholders:
${apiKeys.map(key => `- \`YOUR_${key}\``).join('\n')}
` : ''}
## Customization

Edit CSS variables in \`style.css\`:

\`\`\`css
:root {
  --bg-primary: #0d1117;
  --accent-blue: #58a6ff;
  /* etc */
}
\`\`\`

## Links

- LobsterBoard Builder: https://github.com/curbob/LobsterBoard
- OpenClaw: https://github.com/openclaw/openclaw

---

Generated: ${new Date().toISOString()}
`;
}

// ─── Directory Browser for Latest Image widget ───
async function openDirBrowser(startDir) {
  const browser = document.getElementById('dir-browser');
  const input = document.getElementById('prop-directorypath');
  const dir = startDir || input.value || '~';
  browser.style.display = 'block';
  browser.innerHTML = '<span style="color:var(--text-muted);">Loading...</span>';
  try {
    const res = await fetch('/api/browse-dirs?dir=' + encodeURIComponent(dir));
    const data = await res.json();
    if (data.status !== 'ok') { browser.innerHTML = `<span style="color:#f85149;">${escapeHtml(data.message)}</span>`; return; }
    let html = `<div style="margin-bottom:6px;color:var(--text-secondary);font-size:11px;word-break:break-all;">${escapeHtml(data.path)}</div>`;
    if (data.imageCount > 0) {
      html += `<div style="margin-bottom:6px;padding:4px 8px;background:var(--bg-secondary);border-radius:4px;color:#3fb950;font-size:11px;">📷 ${escapeHtml(String(data.imageCount))} image${data.imageCount !== 1 ? 's' : ''} in this folder</div>`;
    }
    // Up one level
    const parent = data.path.replace(/\/[^/]+\/?$/, '') || '/';
    if (data.path !== parent) {
      html += `<div class="dir-entry" data-path="${escapeHtml(parent)}" style="cursor:pointer;padding:3px 6px;border-radius:4px;color:var(--text-primary);" onmouseover="this.style.background='var(--bg-secondary)'" onmouseout="this.style.background='none'">📁 ..</div>`;
    }
    for (const d of data.dirs) {
      const full = data.path + '/' + d;
      html += `<div class="dir-entry" data-path="${escapeHtml(full)}" style="cursor:pointer;padding:3px 6px;border-radius:4px;color:var(--text-primary);" onmouseover="this.style.background='var(--bg-secondary)'" onmouseout="this.style.background='none'">📁 ${escapeHtml(d)}</div>`;
    }
    if (data.dirs.length === 0 && data.imageCount === 0) {
      html += `<div style="color:var(--text-muted);font-size:11px;padding:4px;">Empty directory</div>`;
    }
    html += `<div style="margin-top:8px;display:flex;gap:4px;">`;
    html += `<button type="button" style="flex:1;padding:4px 8px;background:var(--accent-blue);color:#fff;border:none;border-radius:4px;cursor:pointer;font-size:11px;">✓ Select this folder</button>`;
    html += `<button type="button" onclick="document.getElementById('dir-browser').style.display='none'" style="padding:4px 8px;background:var(--bg-secondary);color:var(--text-primary);border:1px solid var(--border-color);border-radius:4px;cursor:pointer;font-size:11px;">Cancel</button>`;
    html += `</div>`;
    browser.innerHTML = html;
    // Attach select button handler safely (avoid inline onclick with path data)
    const selectBtn = browser.querySelector('button');
    if (selectBtn) selectBtn.addEventListener('click', () => selectDir(data.path));
    browser.querySelectorAll('.dir-entry').forEach(el => {
      el.addEventListener('click', () => openDirBrowser(el.dataset.path));
    });
  } catch (e) { browser.innerHTML = `<span style="color:#f85149;">Error: ${escapeHtml(e.message)}</span>`; }
}

function selectDir(dirPath) {
  const input = document.getElementById('prop-directorypath');
  input.value = dirPath;
  input.dispatchEvent(new Event('input', { bubbles: true }));
  document.getElementById('dir-browser').style.display = 'none';
}
```

## File: `js/templates.js`
```javascript
/**
 * LobsterBoard Template Gallery System
 */
(function() {
  function _esc(str) {
    if (str == null) return '';
    const div = document.createElement('div');
    div.textContent = String(str);
    return div.innerHTML;
  }

  const galleryModal = document.getElementById('template-gallery-modal');
  const exportModal = document.getElementById('template-export-modal');
  const tplGrid = document.getElementById('tpl-grid');
  const tplDetail = document.getElementById('tpl-detail');
  const tplSearch = document.getElementById('tpl-search');

  let allTemplates = [];
  let selectedTemplate = null;

  // ── Open/Close Gallery ──
  document.getElementById('btn-templates').addEventListener('click', () => {
    galleryModal.style.display = 'flex';
    tplDetail.style.display = 'none';
    tplGrid.style.display = '';
    loadTemplates();
  });

  document.getElementById('tpl-close').addEventListener('click', () => {
    galleryModal.style.display = 'none';
  });

  galleryModal.addEventListener('click', (e) => {
    if (e.target === galleryModal) galleryModal.style.display = 'none';
  });

  // ── Open/Close Export ──
  document.getElementById('btn-export-template').addEventListener('click', () => {
    exportModal.style.display = 'flex';
    document.getElementById('tpl-export-result').style.display = 'none';
    document.getElementById('tpl-export-name').value = '';
    document.getElementById('tpl-export-desc').value = '';
    document.getElementById('tpl-export-author').value = '';
    document.getElementById('tpl-export-tags').value = '';
    document.getElementById('tpl-export-screenshot').value = '';
    // Show widget list
    const widgetListEl = document.getElementById('tpl-widget-list');
    if (typeof state !== 'undefined' && state.widgets && typeof WIDGETS !== 'undefined') {
      const typeCounts = {};
      state.widgets.forEach(w => {
        const tpl = WIDGETS[w.type];
        const name = tpl ? (tpl.icon || '') + ' ' + tpl.name : w.type;
        typeCounts[name] = (typeCounts[name] || 0) + 1;
      });
      const items = Object.entries(typeCounts).sort((a,b) => b[1] - a[1]);
      widgetListEl.innerHTML = `<strong style="color:var(--text-secondary);">Widgets in this template (${state.widgets.length}):</strong><div style="margin-top:6px;">${items.map(([name, count]) => `<span style="display:inline-block;padding:2px 8px;margin:2px;background:var(--bg-secondary);border-radius:4px;font-size:11px;">${name}${count > 1 ? ' ×' + count : ''}</span>`).join('')}</div>`;
    } else {
      widgetListEl.innerHTML = '';
    }
  });

  document.getElementById('tpl-export-close').addEventListener('click', () => {
    exportModal.style.display = 'none';
  });

  exportModal.addEventListener('click', (e) => {
    if (e.target === exportModal) exportModal.style.display = 'none';
  });

  // ── Search ──
  tplSearch.addEventListener('input', () => {
    const q = tplSearch.value.toLowerCase();
    renderGrid(allTemplates.filter(t =>
      t.name.toLowerCase().includes(q) ||
      t.description.toLowerCase().includes(q) ||
      (t.tags || []).some(tag => tag.toLowerCase().includes(q))
    ));
  });

  // ── Load Templates ──
  async function loadTemplates() {
    try {
      const res = await fetch('/api/templates');
      allTemplates = await res.json();
      renderGrid(allTemplates);
    } catch (e) {
      tplGrid.innerHTML = '<div class="tpl-empty">Failed to load templates</div>';
    }
  }

  // ── Render Grid ──
  function renderGrid(templates) {
    if (!templates.length) {
      tplGrid.innerHTML = '<div class="tpl-empty">No templates found. Export your dashboard to create one!</div>';
      return;
    }
    tplGrid.innerHTML = templates.map(t => `
      <div class="tpl-card" data-id="${_esc(t.id)}">
        <div class="tpl-card-img">
          <img src="/api/templates/${_esc(t.id)}/preview" alt="${_esc(t.name)}" onerror="this.parentElement.innerHTML='<div class=\\'tpl-no-preview\\'>🦞</div>'">
        </div>
        <div class="tpl-card-body">
          <h3>${_esc(t.name)}</h3>
          <p>${_esc(t.description || '')}</p>
          <div class="tpl-card-meta">
            <span>${_esc(String(t.widgetCount || 0))} widgets</span>
            <span>${_esc(t.canvasSize || '')}</span>
          </div>
          ${(t.widgetTypes || []).length ? `<div style="margin-top:4px;font-size:10px;color:var(--text-muted);">${t.widgetTypes.slice(0,6).map(w => _esc((w.icon || '') + ' ' + w.name)).join(' · ')}${t.widgetTypes.length > 6 ? ' · +' + (t.widgetTypes.length - 6) + ' more' : ''}</div>` : ''}
          <div class="tpl-card-tags">${(t.tags || []).map(tag => `<span class="tpl-tag">${_esc(tag)}</span>`).join('')}</div>
        </div>
      </div>
    `).join('');

    tplGrid.querySelectorAll('.tpl-card').forEach(card => {
      card.addEventListener('click', () => showDetail(card.dataset.id));
    });
  }

  // ── Detail View ──
  function showDetail(id) {
    selectedTemplate = allTemplates.find(t => t.id === id);
    if (!selectedTemplate) return;

    tplGrid.style.display = 'none';
    tplDetail.style.display = 'block';

    document.getElementById('tpl-detail-img').src = `/api/templates/${id}/preview`;
    document.getElementById('tpl-detail-name').textContent = selectedTemplate.name;
    document.getElementById('tpl-detail-desc').textContent = selectedTemplate.description || '';
    document.getElementById('tpl-detail-meta').innerHTML = `
      <div><strong>Author:</strong> ${_esc(selectedTemplate.author || 'anonymous')}</div>
      <div><strong>Canvas:</strong> ${_esc(selectedTemplate.canvasSize || 'unknown')}</div>
      <div><strong>Widgets:</strong> ${_esc(String(selectedTemplate.widgetCount || 0))}</div>
      ${(selectedTemplate.requiresSetup || []).length ? `<div><strong>Requires:</strong> ${(selectedTemplate.requiresSetup || []).map(s => _esc(s)).join(', ')}</div>` : ''}
      ${(selectedTemplate.widgetTypes || []).length ? `<div style="margin-top:8px;"><strong>Widget Types:</strong><div style="margin-top:4px;">${selectedTemplate.widgetTypes.map(w => `<span style="display:inline-block;padding:2px 8px;margin:2px;background:var(--bg-tertiary);border-radius:4px;font-size:11px;">${_esc((w.icon || '') + ' ' + w.name)}${w.count > 1 ? ' ×' + _esc(String(w.count)) : ''}</span>`).join('')}</div></div>` : ''}
    `;
    document.getElementById('tpl-detail-tags').innerHTML = (selectedTemplate.tags || []).map(t => `<span class="tpl-tag">${_esc(t)}</span>`).join('');
  }

  document.getElementById('tpl-back').addEventListener('click', () => {
    tplDetail.style.display = 'none';
    tplGrid.style.display = '';
  });

  // ── Lightbox — click detail image to enlarge ──
  document.getElementById('tpl-detail-img').addEventListener('click', () => {
    const lb = document.getElementById('tpl-lightbox');
    document.getElementById('tpl-lightbox-img').src = document.getElementById('tpl-detail-img').src;
    lb.style.display = 'flex';
  });

  // ── Delete Template ──
  document.getElementById('tpl-delete').addEventListener('click', async () => {
    if (!selectedTemplate) return;
    if (!confirm(`Delete template "${selectedTemplate.name}"?\n\nThis cannot be undone!`)) return;
    try {
      const res = await fetch(`/api/templates/${selectedTemplate.id}`, { method: 'DELETE' });
      const data = await res.json();
      if (data.status === 'success') {
        tplDetail.style.display = 'none';
        tplGrid.style.display = '';
        loadTemplates();
      } else {
        alert('❌ ' + (data.error || data.message || 'Delete failed'));
      }
    } catch (e) {
      alert('❌ Delete failed: ' + e.message);
    }
  });

  // ── Import ──
  document.getElementById('tpl-import-replace').addEventListener('click', async () => {
    if (!selectedTemplate) return;
    if (!confirm(`Replace your current dashboard with "${selectedTemplate.name}"?\n\nThis will overwrite your entire layout!`)) return;
    await doImport(selectedTemplate.id, 'replace');
  });

  document.getElementById('tpl-import-merge').addEventListener('click', async () => {
    if (!selectedTemplate) return;
    await doImport(selectedTemplate.id, 'merge');
  });

  async function doImport(id, mode) {
    try {
      const res = await fetch('/api/templates/import', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id, mode })
      });
      const data = await res.json();
      if (data.status === 'success') {
        galleryModal.style.display = 'none';
        alert(`✅ ${data.message}\n\nReloading dashboard...`);
        location.reload();
      } else {
        alert('❌ ' + (data.error || data.message || 'Import failed'));
      }
    } catch (e) {
      alert('❌ Import failed: ' + e.message);
    }
  }

  // ── Export ──
  document.getElementById('tpl-export-submit').addEventListener('click', async () => {
    const name = document.getElementById('tpl-export-name').value.trim();
    if (!name) { alert('Please enter a template name'); return; }

    const description = document.getElementById('tpl-export-desc').value.trim();
    const author = document.getElementById('tpl-export-author').value.trim();
    const tagsStr = document.getElementById('tpl-export-tags').value.trim();
    const tags = tagsStr ? tagsStr.split(',').map(t => t.trim()).filter(Boolean) : [];

    // Build widget type list
    const widgetTypes = [];
    if (typeof state !== 'undefined' && state.widgets && typeof WIDGETS !== 'undefined') {
      const typeCounts = {};
      state.widgets.forEach(w => {
        const tpl = WIDGETS[w.type];
        const displayName = tpl ? tpl.name : w.type;
        typeCounts[w.type] = typeCounts[w.type] || { name: displayName, icon: tpl ? (tpl.icon || '') : '', count: 0 };
        typeCounts[w.type].count++;
      });
      Object.entries(typeCounts).forEach(([type, info]) => {
        widgetTypes.push({ type, name: info.name, icon: info.icon, count: info.count });
      });
    }

    try {
      const res = await fetch('/api/templates/export', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, description, author, tags, widgetTypes })
      });
      const data = await res.json();
      const resultEl = document.getElementById('tpl-export-result');
      if (data.status === 'success') {
        // Upload screenshot — use user file if provided, otherwise auto-capture
        const screenshotFile = document.getElementById('tpl-export-screenshot').files[0];
        let screenshotData = null;

        if (screenshotFile) {
          screenshotData = await new Promise(resolve => {
            const reader = new FileReader();
            reader.onload = () => resolve(reader.result);
            reader.readAsDataURL(screenshotFile);
          });
        } else {
          // Auto-capture the canvas with html2canvas
          try {
            if (!window.html2canvas) {
              const script = document.createElement('script');
              script.src = 'https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js';
              document.head.appendChild(script);
              await new Promise(resolve => script.onload = resolve);
            }
            const canvasEl = document.getElementById('canvas');
            const captured = await html2canvas(canvasEl, {
              backgroundColor: '#0d1117',
              scale: 1,
              useCORS: true,
              allowTaint: true
            });
            screenshotData = captured.toDataURL('image/png');
          } catch (e) {
            console.warn('Auto-capture screenshot failed:', e);
          }
        }

        if (screenshotData) {
          await fetch(`/api/templates/${data.id}/screenshot`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ data: screenshotData })
          });
        }
        resultEl.innerHTML = `✅ Template exported as <strong>${_esc(data.id)}</strong>${screenshotData ? '<br>Screenshot captured!' : '<br>⚠️ No screenshot (auto-capture failed).'}`;
        resultEl.className = 'tpl-export-result tpl-export-success';
      } else {
        resultEl.innerHTML = `❌ ${_esc(data.error || 'Export failed')}`;
        resultEl.className = 'tpl-export-result tpl-export-error';
      }
      resultEl.style.display = 'block';
    } catch (e) {
      const resultEl = document.getElementById('tpl-export-result');
      resultEl.innerHTML = `❌ Export failed: ${_esc(e.message)}`;
      resultEl.className = 'tpl-export-result tpl-export-error';
      resultEl.style.display = 'block';
    }
  });
})();
```

## File: `js/widgets.js`
```javascript
/**
 * OpenClaw Dashboard Builder - Widget Definitions
 * Each widget defines its default size, properties, and generated code
 */

// ─────────────────────────────────────────────
// Security helpers (available to generated widget scripts via window)
// ─────────────────────────────────────────────

function _escHtmlGlobal(str) {
  if (str == null) return '';
  const div = document.createElement('div');
  div.textContent = String(str);
  return div.innerHTML;
}
window._esc = _escHtmlGlobal;

function _isSafeUrl(url) {
  if (!url) return false;
  try {
    const u = new URL(url);
    return u.protocol === 'https:' || u.protocol === 'http:';
  } catch (e) {
    return false;
  }
}
window._isSafeUrl = _isSafeUrl;

// ─────────────────────────────────────────────
// Icon System - Themeable widget icons
// ─────────────────────────────────────────────
const WIDGET_ICONS = {
  // Weather
  'weather': { emoji: '🌡️', phosphor: 'thermometer' },
  'weather-sunny': { emoji: '☀️', phosphor: 'sun' },
  'weather-cloudy': { emoji: '⛅', phosphor: 'cloud-sun' },
  'weather-rainy': { emoji: '🌧️', phosphor: 'cloud-rain' },
  'weather-snowy': { emoji: '❄️', phosphor: 'snowflake' },
  'world-weather': { emoji: '🌍', phosphor: 'globe' },
  
  // Time
  'clock': { emoji: '🕐', phosphor: 'clock' },
  'countdown': { emoji: '⏳', phosphor: 'hourglass' },
  'cron': { emoji: '⏰', phosphor: 'timer' },
  'pomodoro': { emoji: '🎯', phosphor: 'crosshair' },
  'world-clock': { emoji: '🌍', phosphor: 'globe' },
  
  // System
  'cpu': { emoji: '💻', phosphor: 'cpu' },
  'memory': { emoji: '🧠', phosphor: 'brain' },
  'disk': { emoji: '💾', phosphor: 'hard-drive' },
  'network': { emoji: '🌐', phosphor: 'wifi-high' },
  'docker': { emoji: '🐳', phosphor: 'cube' },
  'uptime': { emoji: '📡', phosphor: 'broadcast' },
  'system-log': { emoji: '🔧', phosphor: 'wrench' },
  
  // Auth / Security
  'auth': { emoji: '🔐', phosphor: 'lock-key' },
  'sleep': { emoji: '😴', phosphor: 'moon' },
  
  // Releases
  'lobster': { emoji: '🦞', phosphor: 'package' },
  'release': { emoji: '📦', phosphor: 'package' },
  
  // Lists / Activity
  'activity': { emoji: '📋', phosphor: 'list' },
  'calendar': { emoji: '📅', phosphor: 'calendar' },
  'notes': { emoji: '📝', phosphor: 'note' },
  'todo': { emoji: '✅', phosphor: 'check-square' },
  'pages': { emoji: '📑', phosphor: 'files' },
  
  // AI / Monitoring
  'ai-usage': { emoji: '🤖', phosphor: 'robot' },
  'claude-code': { emoji: '🟣', phosphor: 'circle' },
  'codex-cli': { emoji: '🟢', phosphor: 'circle' },
  'github-copilot': { emoji: '⚫', phosphor: 'circle' },
  'cursor': { emoji: '🔵', phosphor: 'circle' },
  'gemini-cli': { emoji: '🔷', phosphor: 'diamond' },
  'amp-code': { emoji: '⚡', phosphor: 'lightning' },
  'factory': { emoji: '🏭', phosphor: 'factory' },
  'kimi-code': { emoji: '🌙', phosphor: 'moon' },
  'jetbrains-ai': { emoji: '🧠', phosphor: 'brain' },
  'minimax': { emoji: '🔶', phosphor: 'diamond' },
  'zai': { emoji: '🇿', phosphor: 'sparkle' },
  'antigravity': { emoji: '🪐', phosphor: 'planet' },
  'ai-claude': { emoji: '🟣', phosphor: 'circle' },
  'ai-cost': { emoji: '💰', phosphor: 'currency-dollar' },
  'api-status': { emoji: '🔄', phosphor: 'arrows-clockwise' },
  'sessions': { emoji: '💬', phosphor: 'chat-dots' },
  'tokens': { emoji: '📊', phosphor: 'chart-bar' },
  
  // Finance
  'stock': { emoji: '📈', phosphor: 'chart-line-up' },
  'crypto': { emoji: '₿', phosphor: 'currency-btc' },
  
  // Productivity
  'email': { emoji: '📧', phosphor: 'envelope' },
  'github': { emoji: '🐙', phosphor: 'git-branch' },
  
  // Smart Home
  'home': { emoji: '🏠', phosphor: 'house' },
  'camera': { emoji: '📷', phosphor: 'camera' },
  'power': { emoji: '🔌', phosphor: 'plug' },
  
  // Media
  'music': { emoji: '🎵', phosphor: 'music-notes' },
  'quote': { emoji: '💭', phosphor: 'quotes' },
  
  // Images
  'image': { emoji: '🖼️', phosphor: 'image' },
  'image-random': { emoji: '🎲', phosphor: 'shuffle' },
  'image-new': { emoji: '🆕', phosphor: 'sparkle' },
  
  // Links / Embeds
  'links': { emoji: '🔗', phosphor: 'link' },
  'embed': { emoji: '🌐', phosphor: 'browser' },
  'rss': { emoji: '📡', phosphor: 'rss' },
  
  // Layout
  'header': { emoji: '🔤', phosphor: 'text-aa' },
  'line-h': { emoji: '➖', phosphor: 'minus' },
  'line-v': { emoji: '│', phosphor: 'line-vertical' },
};

/**
 * Renders a themeable icon span
 * @param {string} iconId - Key from WIDGET_ICONS
 * @returns {string} HTML span element with data-icon attribute
 */
function renderIcon(iconId) {
  const icon = WIDGET_ICONS[iconId];
  const emoji = icon ? icon.emoji : '●';
  return `<span class="lb-icon" data-icon="${iconId}">${emoji}</span> `;
}

// Expose for external use
window.renderIcon = renderIcon;
window.WIDGET_ICONS = WIDGET_ICONS;

// ─────────────────────────────────────────────
// Shared SSE connection for system stats widgets
// ─────────────────────────────────────────────
let _statsSource = null;
let _statsCallbacks = [];
function onSystemStats(callback) {
  _statsCallbacks.push(callback);
  if (!_statsSource) {
    _statsSource = new EventSource('/api/stats/stream');
    _statsSource.onmessage = (e) => {
      try {
        const data = JSON.parse(e.data);
        _statsCallbacks.forEach(cb => cb(data));
      } catch (err) {
        console.warn('System stats: failed to parse SSE data', err);
      }
    };
    _statsSource.onerror = () => {
      // EventSource auto-reconnects; just log
      console.warn('System stats SSE connection error, reconnecting...');
    };
  }
}

// ─────────────────────────────────────────────
// Remote server polling for system stats
// ─────────────────────────────────────────────
const _remotePollers = {}; // serverId -> { interval, callbacks, lastData, errors, lastSuccess }

function onRemoteStats(serverId, callback, refreshMs = 10000) {
  if (!_remotePollers[serverId]) {
    _remotePollers[serverId] = { 
      callbacks: [], 
      interval: null, 
      lastData: null,
      errors: 0,
      lastSuccess: null,
      offline: false
    };
    
    const poll = async () => {
      const poller = _remotePollers[serverId];
      try {
        const res = await fetch(`/api/servers/${serverId}/stats`, {
          signal: AbortSignal.timeout(10000) // 10s timeout
        });
        if (res.ok) {
          const data = await res.json();
          const normalized = _normalizeRemoteStats(data);
          poller.lastData = normalized;
          poller.errors = 0;
          poller.lastSuccess = Date.now();
          poller.offline = false;
          poller.callbacks.forEach(cb => cb(normalized));
        } else {
          throw new Error(`HTTP ${res.status}`);
        }
      } catch (e) {
        poller.errors++;
        console.warn(`Remote stats error (${serverId}, attempt ${poller.errors}):`, e.message);
        
        // After 3 consecutive failures, mark as offline and notify widgets
        if (poller.errors >= 3 && !poller.offline) {
          poller.offline = true;
          const offlineData = {
            _offline: true,
            _error: e.message,
            _lastSuccess: poller.lastSuccess,
            _serverId: serverId
          };
          poller.callbacks.forEach(cb => cb(offlineData));
        }
      }
    };
    
    poll(); // Initial fetch
    _remotePollers[serverId].interval = setInterval(poll, refreshMs);
  }
  
  _remotePollers[serverId].callbacks.push(callback);
  
  // If we have cached data, call immediately
  if (_remotePollers[serverId].lastData) {
    callback(_remotePollers[serverId].lastData);
  }
}

// Normalize remote agent stats to match local SSE format
function _normalizeRemoteStats(data) {
  return {
    uptime: data.uptime,
    cpu: data.cpu ? {
      currentLoad: data.cpu.usage || 0,
      cores: data.cpu.cores || 0,
    } : null,
    memory: data.memory ? {
      total: data.memory.total || 0,
      active: data.memory.used || 0,
      available: data.memory.available || 0,
    } : null,
    disk: data.disk ? [{
      mount: data.disk.mount || '/',
      size: data.disk.total || 0,
      used: data.disk.used || 0,
    }] : null,
    network: data.network ? [{
      rx_sec: data.network.rxSec || 0,
      tx_sec: data.network.txSec || 0,
    }] : null,
    docker: data.docker,
    openclaw: data.openclaw,
    serverName: data.serverName,
    _remote: true,
  };
}

// Unified stats function: local or remote
function onStats(serverId, callback, refreshMs = 10000) {
  if (!serverId || serverId === 'local') {
    onSystemStats(callback);
  } else {
    onRemoteStats(serverId, callback, refreshMs);
  }
}

window.onStats = onStats;

function _formatBytes(bytes, decimals = 1) {
  if (bytes === 0 || bytes == null) return '0 B';
  const k = 1024;
  const sizes = ['B', 'KB', 'MB', 'GB', 'TB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return (bytes / Math.pow(k, i)).toFixed(decimals) + ' ' + sizes[i];
}

function _formatBytesPerSec(bytes) {
  if (bytes == null || bytes < 0) return '0 B/s';
  if (bytes < 1024) return bytes.toFixed(0) + ' B/s';
  if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB/s';
  return (bytes / (1024 * 1024)).toFixed(1) + ' MB/s';
}

function _formatUptime(seconds) {
  if (!seconds) return '—';
  const d = Math.floor(seconds / 86400);
  const h = Math.floor((seconds % 86400) / 3600);
  const m = Math.floor((seconds % 3600) / 60);
  if (d > 0) return d + 'd ' + h + 'h ' + m + 'm';
  if (h > 0) return h + 'h ' + m + 'm';
  return m + 'm';
}

// Expose helpers globally for executeWidgetScripts (new Function runs in global scope)
window.onSystemStats = onSystemStats;
window._formatBytes = _formatBytes;
window._formatBytesPerSec = _formatBytesPerSec;
window._formatUptime = _formatUptime;

const WIDGETS = {
  // ─────────────────────────────────────────────
  // SMALL CARDS (KPI style)
  // ─────────────────────────────────────────────
  
  'weather': {
    name: 'Local Weather',
    icon: '🌡️',
    category: 'small',
    description: 'Shows current weather for a single location using Open-Meteo (no API key needed).',
    defaultWidth: 200,
    defaultHeight: 120,
    hasApiKey: false,
    properties: {
      title: 'Local Weather',
      location: 'Atlanta',
      units: 'F',
      refreshInterval: 600
    },
    preview: `<div style="text-align:center;padding:8px;">
      <div style="font-size:24px;">72°F</div>
      <div style="font-size:11px;color:#8b949e;">Atlanta</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('weather')} ${props.title || 'Local Weather'}</span>
        </div>
        <div class="dash-card-body" style="display:flex;align-items:center;justify-content:center;gap:10px;">
          <span id="${props.id}-icon" class="lb-icon lb-icon-lg" data-icon="weather">🌡️</span>
          <div>
            <div class="kpi-value blue" id="${props.id}-value">Loading...</div>
            <div class="kpi-label" id="${props.id}-label">${props.location || 'Location'}</div>
          </div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Weather Widget: ${props.id} (uses free Open-Meteo API - no key needed)
      const WMO_DESC = {0:'Clear sky',1:'Mainly clear',2:'Partly cloudy',3:'Overcast',45:'Fog',48:'Rime fog',51:'Light drizzle',53:'Drizzle',55:'Dense drizzle',61:'Slight rain',63:'Moderate rain',65:'Heavy rain',71:'Slight snow',73:'Moderate snow',75:'Heavy snow',80:'Slight showers',81:'Moderate showers',82:'Violent showers',95:'Thunderstorm',96:'Hail thunderstorm',99:'Heavy hail'};
      function wmoIcon(code) {
        if (code <= 1) return 'weather-sunny';
        if (code <= 3) return 'weather-cloudy';
        if (code >= 51 && code <= 82) return 'weather-rainy';
        if (code >= 71 && code <= 77) return 'weather-snowy';
        if (code >= 95) return 'weather-rainy';
        return 'weather';
      }
      async function update_${props.id.replace(/-/g, '_')}() {
        const valEl = document.getElementById('${props.id}-value');
        const labelEl = document.getElementById('${props.id}-label');
        const iconEl = document.getElementById('${props.id}-icon');
        try {
          const loc = '${props.location || 'Atlanta'}';
          const geoRes = await fetch('https://geocoding-api.open-meteo.com/v1/search?name=' + encodeURIComponent(loc) + '&count=1');
          const geoData = await geoRes.json();
          if (!geoData.results || !geoData.results.length) throw new Error('City not found');
          const {latitude, longitude} = geoData.results[0];
          const tempUnit = '${props.units}' === 'C' ? 'celsius' : 'fahrenheit';
          const res = await fetch('https://api.open-meteo.com/v1/forecast?latitude=' + latitude + '&longitude=' + longitude + '&current=temperature_2m,weathercode,windspeed_10m&temperature_unit=' + tempUnit);
          const data = await res.json();
          const c = data.current;
          const unit = '${props.units}' === 'C' ? '°C' : '°F';
          valEl.textContent = Math.round(c.temperature_2m) + unit;
          labelEl.textContent = WMO_DESC[c.weathercode] || 'Unknown';
          const iconId = wmoIcon(c.weathercode);
          iconEl.setAttribute('data-icon', iconId);
          const icons = window.WIDGET_ICONS || {};
          iconEl.textContent = icons[iconId] ? icons[iconId].emoji : '🌡️';
        } catch (e) {
          console.error('Weather widget error:', e);
          if (!valEl.dataset.loaded) valEl.textContent = 'Unavailable';
        }
        valEl.dataset.loaded = '1';
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 600) * 1000});
    `
  },

  'weather-multi': {
    name: 'World Weather',
    icon: '🌍',
    category: 'large',
    description: 'Shows weather for multiple locations side-by-side. Separate cities with semicolons.',
    defaultWidth: 350,
    defaultHeight: 200,
    hasApiKey: false,
    properties: {
      title: 'World Weather',
      locations: 'New York; London; Tokyo',
      units: 'F',
      refreshInterval: 600
    },
    preview: `<div style="padding:4px;font-size:11px;">
      <div>🌡️ New York: 72°F</div>
      <div>🌡️ London: 58°F</div>
      <div>🌡️ Tokyo: 68°F</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('world-weather')} ${props.title || 'World Weather'}</span>
        </div>
        <div class="dash-card-body" id="${props.id}-list">
          <div class="weather-row"><span class="weather-icon lb-icon" data-icon="weather-sunny">☀️</span><span class="weather-loc">New York</span><span class="weather-temp">72°F</span></div>
          <div class="weather-row"><span class="weather-icon lb-icon" data-icon="weather-cloudy">⛅</span><span class="weather-loc">London</span><span class="weather-temp">58°F</span></div>
          <div class="weather-row"><span class="weather-icon lb-icon" data-icon="weather-rainy">🌧️</span><span class="weather-loc">Tokyo</span><span class="weather-temp">65°F</span></div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Multi Weather Widget: ${props.id} (uses free Open-Meteo API - no key needed)
      const WMO_DESC2 = {0:'Clear',1:'Clear',2:'Partly cloudy',3:'Overcast',45:'Fog',48:'Rime fog',51:'Drizzle',53:'Drizzle',55:'Drizzle',61:'Rain',63:'Rain',65:'Heavy rain',71:'Snow',73:'Snow',75:'Heavy snow',80:'Showers',81:'Showers',82:'Showers',95:'Storm',96:'Hail',99:'Hail'};
      function wmoIcon2(code) {
        if (code <= 1) return 'weather-sunny';
        if (code <= 3) return 'weather-cloudy';
        if (code >= 51 && code <= 82) return 'weather-rainy';
        if (code >= 71 && code <= 77) return 'weather-snowy';
        if (code >= 95) return 'weather-rainy';
        return 'weather';
      }
      async function update_${props.id.replace(/-/g, '_')}() {
        const locations = '${props.locations || 'New York; London; Tokyo'}'.split(';').map(l => l.trim());
        const container = document.getElementById('${props.id}-list');
        const tempUnit = '${props.units}' === 'C' ? 'celsius' : 'fahrenheit';
        const unitSymbol = '${props.units}' === 'C' ? '°C' : '°F';
        
        const results = await Promise.all(locations.map(async (loc) => {
          try {
            const geoRes = await fetch('https://geocoding-api.open-meteo.com/v1/search?name=' + encodeURIComponent(loc) + '&count=1');
            const geoData = await geoRes.json();
            if (!geoData.results || !geoData.results.length) return { loc, temp: 'N/A', iconId: 'weather', emoji: '❓' };
            const {latitude, longitude} = geoData.results[0];
            const res = await fetch('https://api.open-meteo.com/v1/forecast?latitude=' + latitude + '&longitude=' + longitude + '&current=temperature_2m,weathercode&temperature_unit=' + tempUnit);
            const data = await res.json();
            const c = data.current;
            const iconId = wmoIcon2(c.weathercode);
            const icons = window.WIDGET_ICONS || {};
            const emoji = icons[iconId] ? icons[iconId].emoji : '🌡️';
            return { loc, temp: Math.round(c.temperature_2m), iconId, emoji };
          } catch (e) {
            return { loc, temp: 'N/A', iconId: 'weather', emoji: '❓' };
          }
        }));
        
        container.innerHTML = results.map(r =>
          '<div class="weather-row"><span class="weather-icon lb-icon" data-icon="' + _esc(r.iconId) + '">' + _esc(r.emoji) + '</span><span class="weather-loc">' + _esc(r.loc) + '</span><span class="weather-temp">' + _esc(String(r.temp)) + _esc(unitSymbol) + '</span></div>'
        ).join('');
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 600) * 1000});
    `
  },

  'auth-status': {
    name: 'Auth Status',
    icon: '🔐',
    category: 'small',
    description: 'Shows if OpenClaw is using Anthropic Max subscription (green) or API key fallback (yellow).',
    defaultWidth: 180,
    defaultHeight: 100,
    hasApiKey: true,
    apiKeyName: 'OPENCLAW_API',
    properties: {
      title: 'Auth Type',
      server: 'local',
      endpoint: '/api/status',
      refreshInterval: 30
    },
    preview: `<div style="text-align:center;padding:8px;">
      <div style="width:10px;height:10px;background:#3fb950;border-radius:50%;margin:0 auto 4px;"></div>
      <div style="font-size:13px;">OAuth</div>
      <div style="font-size:11px;color:#8b949e;">Auth</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('auth')} ${props.title || 'Auth Type'}</span>
        </div>
        <div class="dash-card-body" style="display:flex;align-items:center;justify-content:center;gap:10px;">
          <div class="kpi-indicator" id="${props.id}-dot"></div>
          <div class="kpi-value" id="${props.id}-value">—</div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Auth Status Widget: ${props.id} — ${props.server === 'local' ? 'local' : 'remote: ' + props.server}
      async function update_${props.id.replace(/-/g, '_')}() {
        const serverId = '${props.server || 'local'}';
        const dot = document.getElementById('${props.id}-dot');
        const val = document.getElementById('${props.id}-value');
        try {
          let authData;
          if (serverId === 'local') {
            const res = await fetch('/api/auth');
            authData = await res.json();
          } else {
            const res = await fetch('/api/servers/' + serverId + '/stats');
            const data = await res.json();
            if (data.error) throw new Error(data.error);
            if (!data.openclaw?.auth) throw new Error('Auth data not available');
            authData = { status: 'ok', mode: data.openclaw.auth.mode };
          }
          if (authData.status === 'ok' || authData.mode) {
            const isMonthly = authData.mode === 'Monthly';
            val.textContent = isMonthly ? 'Max' : 'API';
            dot.className = 'kpi-indicator ' + (isMonthly ? 'green' : 'yellow');
          } else {
            val.textContent = '—';
          }
        } catch (e) {
          console.error('Auth status widget error:', e);
          val.textContent = '—';
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 30) * 1000});
    `
  },

  'sleep-ring': {
    name: 'Sleep Score',
    icon: '😴',
    category: 'small',
    description: 'Displays sleep data from a configured health API endpoint.',
    defaultWidth: 160,
    defaultHeight: 100,
    hasApiKey: true,
    apiKeyName: 'GARMIN_TOKEN',
    properties: {
      title: 'Sleep Score',
      refreshInterval: 300
    },
    preview: `<div style="text-align:center;padding:8px;">
      <div style="font-size:20px;color:#3fb950;">85</div>
      <div style="font-size:11px;color:#8b949e;">Sleep Score</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('sleep')} ${props.title || 'Sleep Score'}</span>
        </div>
        <div class="dash-card-body" style="display:flex;align-items:center;justify-content:center;gap:10px;">
          <div class="kpi-ring-wrap kpi-ring-sm">
            <svg class="kpi-ring" viewBox="0 0 48 48">
              <circle cx="24" cy="24" r="20" fill="none" stroke="var(--bg-tertiary)" stroke-width="4"/>
              <circle id="${props.id}-ring" cx="24" cy="24" r="20" fill="none" stroke="var(--accent-green)" stroke-width="4"
                stroke-dasharray="125.66" stroke-dashoffset="125.66" stroke-linecap="round"
                transform="rotate(-90 24 24)" style="transition: stroke-dashoffset 0.6s ease;"/>
            </svg>
            <div class="kpi-ring-label" id="${props.id}-value">—</div>
          </div>
          <div class="kpi-data">
            <div class="kpi-label">Sleep</div>
          </div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Sleep Ring Widget: ${props.id}
      function setSleepScore_${props.id.replace(/-/g, '_')}(score) {
        const ring = document.getElementById('${props.id}-ring');
        const label = document.getElementById('${props.id}-value');
        const circumference = 125.66;
        const offset = circumference - (score / 100) * circumference;
        ring.style.strokeDashoffset = offset;
        label.textContent = score;
      }
      // Replace with your data source
      setSleepScore_${props.id.replace(/-/g, '_')}(85);
    `
  },

  'lobsterboard-release': {
    name: 'LobsterBoard Release',
    icon: '🦞',
    category: 'small',
    description: 'Auto-detects running LobsterBoard version and compares to latest GitHub release.',
    defaultWidth: 200,
    defaultHeight: 120,
    hasApiKey: false,
    properties: {
      title: 'LobsterBoard',
      refreshInterval: 3600
    },
    preview: `<div style="text-align:center;padding:8px;">
      <div style="font-size:13px;">v0.1.5</div>
      <div style="font-size:11px;color:#3fb950;">✓ Up to date</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('lobster')} ${props.title || 'LobsterBoard'}</span>
        </div>
        <div class="dash-card-body" style="display:flex;align-items:center;gap:10px;padding:8px 12px;">
          <span class="lb-icon lb-icon-lg" data-icon="lobster">🦞</span>
          <div>
            <div id="${props.id}-versions" style="display:flex;align-items:center;gap:6px;font-size:calc(13px * var(--font-scale, 1));color:#c9d1d9;">
              <span id="${props.id}-current">—</span>
              <span id="${props.id}-arrow" style="color:#6e7681;display:none;">→</span>
              <span id="${props.id}-latest" style="display:none;"></span>
            </div>
            <div id="${props.id}-status" style="font-size:calc(11px * var(--font-scale, 1));margin-top:2px;">Checking...</div>
          </div>
        </div>
      </div>`,
    generateJs: (props) => `
      async function update_${props.id.replace(/-/g, '_')}() {
        const currentEl = document.getElementById('${props.id}-current');
        const arrowEl = document.getElementById('${props.id}-arrow');
        const latestEl = document.getElementById('${props.id}-latest');
        const statusEl = document.getElementById('${props.id}-status');
        
        try {
          const res = await fetch('/api/lb-release');
          const data = await res.json();
          if (data.status !== 'ok') throw new Error(data.message);
          
          const cur = (data.current || '').replace(/^v/, '');
          const lat = (data.latest || '').replace(/^v/, '');
          // Strip -N suffixes for comparison (e.g. 2026.2.22-2 matches 2026.2.22)
          const curBase = cur.replace(/-\d+$/, '');
          const latBase = lat.replace(/-\d+$/, '');
          const isUpToDate = cur === lat || curBase === latBase || cur.startsWith(latBase + '-');
          
          if (!cur || cur === 'unknown') {
            currentEl.textContent = 'v' + lat;
            statusEl.textContent = 'Latest release';
            statusEl.style.color = '#8b949e';
          } else if (isUpToDate) {
            currentEl.textContent = 'v' + cur;
            currentEl.style.color = '#3fb950';
            statusEl.innerHTML = '✓ Up to date';
            statusEl.style.color = '#3fb950';
          } else {
            currentEl.textContent = cur;
            currentEl.style.color = '#c9d1d9';
            arrowEl.style.display = 'inline';
            latestEl.style.display = 'inline';
            latestEl.textContent = 'v' + lat;
            latestEl.style.color = '#58a6ff';
            statusEl.innerHTML = '<span style="color:#d29922;">Update available</span>';
          }
        } catch (e) {
          currentEl.textContent = '—';
          statusEl.textContent = 'Error';
          console.error('LobsterBoard Release widget error:', e);
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 3600) * 1000});
    `
  },

  'openclaw-release': {
    name: 'OpenClaw Release',
    icon: '🦞',
    category: 'small',
    description: 'Auto-detects running OpenClaw version and compares to latest GitHub release.',
    defaultWidth: 200,
    defaultHeight: 120,
    hasApiKey: false,
    properties: {
      title: 'OpenClaw',
      server: 'local',
      openclawUrl: '',
      refreshInterval: 3600
    },
    preview: `<div style="text-align:center;padding:8px;">
      <div style="font-size:13px;">v2026.2.3</div>
      <div style="font-size:11px;color:#3fb950;">✓ Up to date</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('release')} ${props.title || 'OpenClaw'}</span>
        </div>
        <div class="dash-card-body" style="display:flex;align-items:center;gap:10px;padding:8px 12px;">
          <span class="lb-icon lb-icon-lg" data-icon="release">📦</span>
          <div>
            <div id="${props.id}-versions" style="display:flex;align-items:center;gap:6px;font-size:calc(13px * var(--font-scale, 1));color:#c9d1d9;">
              <span id="${props.id}-current">—</span>
              <span id="${props.id}-arrow" style="color:#6e7681;display:none;">→</span>
              <span id="${props.id}-latest" style="display:none;"></span>
            </div>
            <div id="${props.id}-status" style="font-size:calc(11px * var(--font-scale, 1));margin-top:2px;">Checking...</div>
          </div>
        </div>
      </div>`,
    generateJs: (props) => `
      async function update_${props.id.replace(/-/g, '_')}() {
        const serverId = '${props.server || 'local'}';
        const currentEl = document.getElementById('${props.id}-current');
        const arrowEl = document.getElementById('${props.id}-arrow');
        const latestEl = document.getElementById('${props.id}-latest');
        const statusEl = document.getElementById('${props.id}-status');
        
        try {
          let cur, lat;
          
          if (serverId === 'local') {
            // Local: fetch from /api/releases
            const res = await fetch('/api/releases');
            const data = await res.json();
            if (data.status !== 'ok') throw new Error(data.message);
            cur = (data.current || '').replace(/^v/, '');
            lat = (data.latest || '').replace(/^v/, '');
          } else {
            // Remote: fetch from server stats and get openclaw.version
            const res = await fetch('/api/servers/' + serverId + '/stats');
            const data = await res.json();
            if (data.error) throw new Error(data.error);
            if (!data.openclaw) throw new Error('OpenClaw not installed on remote');
            cur = (data.openclaw.version || '').replace(/^v/, '');
            // Fetch latest from GitHub
            const ghRes = await fetch('https://api.github.com/repos/openclaw/openclaw/releases/latest');
            const ghData = await ghRes.json();
            lat = (ghData.tag_name || '').replace(/^v/, '');
          }
          
          // Strip -N suffixes for comparison (e.g. 2026.2.22-2 matches 2026.2.22)
          const curBase = cur.replace(/-\\d+$/, '');
          const latBase = lat.replace(/-\\d+$/, '');
          const isUpToDate = cur === lat || curBase === latBase || cur.startsWith(latBase + '-');
          
          if (!cur || cur === 'unknown') {
            currentEl.textContent = 'v' + lat;
            statusEl.textContent = 'Latest release';
            statusEl.style.color = '#8b949e';
          } else if (isUpToDate) {
            currentEl.textContent = 'v' + cur;
            currentEl.style.color = '#3fb950';
            statusEl.innerHTML = '✓ Up to date';
            statusEl.style.color = '#3fb950';
          } else {
            currentEl.textContent = cur;
            currentEl.style.color = '#c9d1d9';
            arrowEl.style.display = 'inline';
            latestEl.style.display = 'inline';
            latestEl.textContent = 'v' + lat;
            latestEl.style.color = '#58a6ff';
            statusEl.innerHTML = '<span style="color:#d29922;">Update available</span>';
          }
        } catch (e) {
          currentEl.textContent = '—';
          statusEl.textContent = e.message || 'Error';
          console.error('OpenClaw Release widget error:', e);
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 3600) * 1000});
    `
  },

  'release': {
    name: 'Release',
    icon: '📦',
    category: 'small',
    description: 'Compares your current version of any software to its latest GitHub release.',
    defaultWidth: 200,
    defaultHeight: 120,
    hasApiKey: false,
    properties: {
      title: 'Release',
      repo: 'openclaw/openclaw',
      currentVersion: '',
      refreshInterval: 3600
    },
    preview: `<div style="text-align:center;padding:8px;">
      <div style="font-size:13px;">v1.2.3</div>
      <div style="font-size:11px;color:#8b949e;">Up to date</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('release')} ${props.title || 'Release'}</span>
        </div>
        <div class="dash-card-body" style="display:flex;align-items:center;gap:10px;padding:8px 12px;">
          <span class="lb-icon lb-icon-lg" data-icon="release">📦</span>
          <div>
            <div id="${props.id}-versions" style="display:flex;align-items:center;gap:6px;font-size:calc(13px * var(--font-scale, 1));color:#c9d1d9;">
              <span id="${props.id}-current">—</span>
              <span id="${props.id}-arrow" style="color:#6e7681;display:none;">→</span>
              <span id="${props.id}-latest" style="display:none;"></span>
            </div>
            <div id="${props.id}-status" style="font-size:calc(11px * var(--font-scale, 1));margin-top:2px;">Checking...</div>
          </div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Release Widget: ${props.id}
      async function update_${props.id.replace(/-/g, '_')}() {
        const currentVersion = '${props.currentVersion || ''}'.replace(/^v/, '');
        const currentEl = document.getElementById('${props.id}-current');
        const arrowEl = document.getElementById('${props.id}-arrow');
        const latestEl = document.getElementById('${props.id}-latest');
        const statusEl = document.getElementById('${props.id}-status');
        
        try {
          const res = await fetch('https://api.github.com/repos/${props.repo || 'openclaw/openclaw'}/releases/latest');
          const data = await res.json();
          const lat = (data.tag_name || '').replace(/^v/, '');
          
          if (!currentVersion) {
            currentEl.textContent = 'v' + lat;
            statusEl.textContent = 'Latest release';
            statusEl.style.color = '#8b949e';
          } else if (currentVersion === lat) {
            currentEl.textContent = 'v' + currentVersion;
            currentEl.style.color = '#3fb950';
            statusEl.innerHTML = '✓ Up to date';
            statusEl.style.color = '#3fb950';
          } else {
            currentEl.textContent = currentVersion;
            currentEl.style.color = '#c9d1d9';
            arrowEl.style.display = 'inline';
            latestEl.style.display = 'inline';
            latestEl.textContent = 'v' + lat;
            latestEl.style.color = '#58a6ff';
            statusEl.innerHTML = '<span style="color:#d29922;">Update available</span>';
          }
        } catch (e) {
          console.error('Release widget error:', e);
          currentEl.textContent = '—';
          statusEl.textContent = 'Error';
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 3600) * 1000});
    `
  },

  'clock': {
    name: 'Clock',
    icon: '🕐',
    category: 'small',
    description: 'Simple digital clock. Supports 12h or 24h format.',
    defaultWidth: 200,
    defaultHeight: 120,
    hasApiKey: false,
    properties: {
      title: 'Clock',
      timezone: 'local',
      format24h: false
    },
    preview: `<div style="text-align:center;padding:8px;">
      <div style="font-size:24px;">3:45 PM</div>
      <div style="font-size:11px;color:#8b949e;">Wed, Feb 5</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('clock')} ${props.title || 'Clock'}</span>
        </div>
        <div class="dash-card-body" style="display:flex;flex-direction:column;align-items:center;justify-content:center;">
          <div class="kpi-value" id="${props.id}-time">—</div>
          <div class="kpi-label" id="${props.id}-date">—</div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Clock Widget: ${props.id}
      function updateClock_${props.id.replace(/-/g, '_')}() {
        const now = new Date();
        const timeEl = document.getElementById('${props.id}-time');
        const dateEl = document.getElementById('${props.id}-date');
        const opts = { hour: 'numeric', minute: '2-digit', hour12: ${!props.format24h} };
        timeEl.textContent = now.toLocaleTimeString('en-US', opts);
        dateEl.textContent = now.toLocaleDateString('en-US', { weekday: 'short', month: 'short', day: 'numeric' });
      }
      updateClock_${props.id.replace(/-/g, '_')}();
      setInterval(updateClock_${props.id.replace(/-/g, '_')}, 1000);
    `
  },

  // ─────────────────────────────────────────────
  // LARGE CARDS (Content)
  // ─────────────────────────────────────────────

  'activity-list': {

    name: 'Activity List',
    icon: '📋',
    category: 'large',
    description: 'Shows recent OpenClaw activity from /api/activity endpoint.',
    defaultWidth: 400,
    defaultHeight: 300,
    hasApiKey: true,
    apiKeyName: 'OPENCLAW_API',
    properties: {
      title: 'Today',
      server: 'local',
      endpoint: '/api/today',
      maxItems: 10,
      refreshInterval: 60
    },
    preview: `<div style="padding:4px;font-size:11px;color:#8b949e;">
      <div>• Meeting at 2pm</div>
      <div>• Review PR #42</div>
      <div>• Deploy v1.2</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('activity')} ${props.title || 'Today'}</span>
          <span class="dash-card-badge" id="${props.id}-badge">—</span>
        </div>
        <div class="dash-card-body compact-list" id="${props.id}-list">
          <div class="list-item">• Team standup at 10am</div>
          <div class="list-item">• Review PR #42</div>
          <div class="list-item">• Deploy v1.2.3</div>
          <div class="list-item">• Update documentation</div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Activity List Widget: ${props.id} — ${props.server === 'local' ? 'local' : 'remote: ' + props.server}
      async function update_${props.id.replace(/-/g, '_')}() {
        const serverId = '${props.server || 'local'}';
        const list = document.getElementById('${props.id}-list');
        const badge = document.getElementById('${props.id}-badge');
        try {
          let data;
          if (serverId === 'local') {
            const res = await fetch('${props.endpoint || '/api/today'}');
            data = await res.json();
          } else {
            const res = await fetch('/api/servers/' + serverId + '/stats');
            const stats = await res.json();
            if (stats.error) throw new Error(stats.error);
            data = stats.openclaw?.today || { date: new Date().toISOString().split('T')[0], activities: [] };
          }

          if (data.date && badge) {
            const d = new Date(data.date + 'T12:00:00');
            badge.textContent = d.toLocaleDateString('en-US', { weekday: 'short', month: 'short', day: 'numeric' });
          }

          const activities = data.activities || [];
          if (!activities.length) {
            list.innerHTML = '<div style="padding:8px;color:#8b949e;font-size:calc(12px * var(--font-scale,1));">No activity yet today</div>';
            return;
          }

          const fs = 'calc(12px * var(--font-scale, 1))';
          list.innerHTML = activities.slice(0, ${props.maxItems || 10}).map(a => {
            const icon = a.status === 'ok' ? '✓' : a.status === 'error' ? '❌' : '';
            const text = _esc(a.text || '');
            const source = _esc(a.source || '');
            return '<div style="display:flex;align-items:flex-start;justify-content:space-between;padding:4px 0;border-bottom:1px solid #30363d;font-size:' + fs + ';">' +
              '<div style="flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">' + _esc(a.icon || '') + ' ' + text + '</div>' +
              '<div style="flex-shrink:0;font-size:0.85em;color:#8b949e;margin-left:8px;">' + _esc(icon) + ' ' + source + '</div>' +
            '</div>';
          }).join('');
        } catch (e) { 
          console.error('Today widget error:', e);
          list.innerHTML = '<div style="padding:8px;color:#f85149;font-size:calc(12px * var(--font-scale,1));">Error: ' + _esc(e.message) + '</div>';
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 60) * 1000});
    `
  },

  'ai-usage': {

    name: 'AI Usage',
    icon: '🤖',
    category: 'large',
    description: 'Track usage across AI coding tools. Some providers may show errors on first load — see individual provider widgets for setup instructions.',
    defaultWidth: 350,
    defaultHeight: 280,
    hasApiKey: false,
    properties: {
      title: 'AI Usage',
      server: 'local',
      providers: 'all',
      hideUnauthenticated: true,
      showPlan: true,
      compactMode: false,
      refreshInterval: 300
    },
    preview: `<div style="padding:4px;font-size:11px;color:#8b949e;">
      <div>🟣 Claude — 25% session</div>
      <div>🟢 Codex — 12% weekly</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('tokens')} ${props.title || 'AI Usage'}</span>
          <span class="dash-card-badge" id="${props.id}-badge">—</span>
        </div>
        <div class="dash-card-body" id="${props.id}-content" style="display:flex;flex-direction:column;gap:8px;overflow-y:auto;">
          <div style="color:var(--text-muted);font-size:11px;">Loading...</div>
        </div>
      </div>`,
    generateJs: (props) => `
      // AI Usage Widget: ${props.id} — ${props.server === 'local' ? 'local' : 'remote: ' + props.server}
      async function update_${props.id.replace(/-/g, '_')}() {
        const content = document.getElementById('${props.id}-content');
        const badge = document.getElementById('${props.id}-badge');
        try {
          const serverId = '${props.server || 'local'}';
          const providers = '${props.providers || 'all'}';
          let json;
          
          if (serverId === 'local') {
            // Local: fetch from /api/ai-usage
            const url = providers === 'all' ? '/api/ai-usage' : '/api/ai-usage/' + providers;
            const res = await fetch(url);
            json = await res.json();
          } else {
            // Remote: fetch from server stats endpoint
            const res = await fetch('/api/servers/' + serverId + '/stats');
            const data = await res.json();
            if (data.error) {
              json = { status: 'error', message: data.error };
            } else if (data.aiUsage && data.aiUsage.providers) {
              json = { status: 'ok', providers: data.aiUsage.providers };
            } else if (data.aiUsage === undefined) {
              json = { status: 'error', message: 'AI usage not enabled on remote agent (enableAiUsage: false)' };
            } else {
              json = { status: 'error', message: 'No AI providers found on remote server' };
            }
          }
          
          if (json.status !== 'ok') {
            content.innerHTML = '<div style="color:#f85149;font-size:12px;">' + _esc(json.message || 'Error') + '</div>';
            badge.textContent = '!';
            return;
          }
          
          let allProviders = json.providers || [json];
          const hideUnauth = ${props.hideUnauthenticated !== false};
          const providerFilter = '${props.providers || 'all'}'.split(',').map(s => s.trim()).filter(Boolean);
          
          // Filter by selected providers
          if (providerFilter.length && providerFilter[0] !== 'all') {
            allProviders = allProviders.filter(p => providerFilter.includes(p.provider));
          }
          
          // Hide unauthenticated/errored providers if option is set
          if (hideUnauth) {
            allProviders = allProviders.filter(p => !p.error);
          }
          
          const validProviders = allProviders.filter(p => !p.error);
          
          badge.textContent = validProviders.length + (allProviders.length > validProviders.length ? '/' + allProviders.length : '');
          
          let html = '';
          const compact = ${props.compactMode || false};
          const showPlan = ${props.showPlan !== false};
          
          // Map provider IDs to icon IDs for theming
          const providerIconMap = {
            claude: 'claude-code', codex: 'codex-cli', copilot: 'github-copilot',
            cursor: 'cursor', gemini: 'gemini-cli', amp: 'amp-code', factory: 'factory',
            kimi: 'kimi-code', jetbrains: 'jetbrains-ai', minimax: 'minimax', zai: 'zai',
            antigravity: 'antigravity'
          };
          
          for (const prov of allProviders) {
            const iconId = providerIconMap[prov.provider] || 'ai-usage';
            const iconEmoji = _esc(prov.icon || '⚪');
            const name = _esc(prov.name || prov.provider || 'Unknown');
            
            if (prov.error) {
              html += '<div style="padding:6px 0;border-bottom:1px solid var(--border,#30363d);">';
              html += '<div style="display:flex;align-items:center;gap:6px;margin-bottom:4px;">';
              html += '<span class="lb-icon" data-icon="' + iconId + '" style="font-size:16px;">' + iconEmoji + '</span>';
              html += '<span style="font-weight:500;font-size:13px;">' + name + '</span>';
              html += '</div>';
              html += '<div style="color:#f85149;font-size:11px;padding-left:22px;">' + _esc(prov.error) + '</div>';
              html += '</div>';
              continue;
            }
            
            html += '<div style="padding:6px 0;border-bottom:1px solid var(--border,#30363d);">';
            html += '<div style="display:flex;align-items:center;gap:6px;margin-bottom:' + (compact ? '2px' : '6px') + ';">';
            html += '<span class="lb-icon" data-icon="' + iconId + '" style="font-size:16px;">' + iconEmoji + '</span>';
            html += '<span style="font-weight:500;font-size:13px;">' + name + '</span>';
            if (showPlan && prov.plan) {
              html += '<span style="font-size:10px;color:var(--text-muted);background:var(--bg-secondary);padding:1px 6px;border-radius:4px;margin-left:auto;">' + _esc(prov.plan) + '</span>';
            }
            html += '</div>';
            
            if (prov.metrics && prov.metrics.length) {
              for (const m of prov.metrics) {
                const label = _esc(m.label);
                const pct = m.used != null ? Math.min(100, Math.max(0, m.used)) : 0;
                const color = pct > 80 ? '#f85149' : pct > 50 ? '#d29922' : '#3fb950';
                
                if (m.format === 'dollars') {
                  const val = m.remaining != null ? '$' + m.remaining.toFixed(2) : (m.used != null ? '$' + m.used.toFixed(2) + ' used' : '—');
                  html += '<div style="display:flex;justify-content:space-between;font-size:11px;padding:2px 0 2px 22px;">';
                  html += '<span style="color:var(--text-secondary);">' + label + '</span>';
                  html += '<span style="color:' + (m.remaining != null ? '#3fb950' : 'var(--text-primary)') + ';">' + _esc(val) + '</span>';
                  html += '</div>';
                } else {
                  // Percentage progress bar
                  html += '<div style="padding:2px 0 2px 22px;">';
                  if (!compact) {
                    html += '<div style="display:flex;justify-content:space-between;font-size:11px;margin-bottom:2px;">';
                    html += '<span style="color:var(--text-secondary);">' + label + '</span>';
                    html += '<span style="color:' + color + ';">' + pct.toFixed(0) + '%</span>';
                    html += '</div>';
                  }
                  html += '<div style="height:' + (compact ? '4px' : '6px') + ';background:var(--bg-tertiary,#21262d);border-radius:3px;overflow:hidden;">';
                  html += '<div style="width:' + pct + '%;height:100%;background:' + color + ';transition:width 0.3s;"></div>';
                  html += '</div>';
                  if (compact) {
                    html += '<div style="font-size:9px;color:var(--text-muted);margin-top:1px;">' + label + ' ' + pct.toFixed(0) + '%</div>';
                  }
                  html += '</div>';
                }
              }
            }
            html += '</div>';
          }
          
          content.innerHTML = html || '<div style="color:var(--text-muted);font-size:11px;">No providers configured</div>';
        } catch (e) {
          console.error('AI Usage widget error:', e);
          content.innerHTML = '<div style="color:#f85149;font-size:12px;">Error loading usage data</div>';
          badge.textContent = '!';
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 300) * 1000});
    `
  },

  'claude-code': {

    name: 'Claude Code',
    icon: '🟣',
    category: 'small',
    description: 'Track Claude Code usage (session, weekly, Opus limits). Setup: run `claude` once to authenticate. May show 429 on first load — cached after success.',
    defaultWidth: 280,
    defaultHeight: 180,
    hasApiKey: false,
    properties: {
      title: 'Claude',
      showPlan: true,
      refreshInterval: 300
    },
    preview: `<div style="padding:4px;font-size:11px;color:#8b949e;">
      <div>Session: 25%</div>
      <div>Weekly: 12%</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">🟣 ${props.title || 'Claude'}</span>
          <span class="dash-card-badge" id="${props.id}-badge">—</span>
        </div>
        <div class="dash-card-body" id="${props.id}-content" style="display:flex;flex-direction:column;gap:4px;overflow-y:auto;">
          <div style="color:var(--text-muted);font-size:11px;">Loading...</div>
        </div>
      </div>`,
    generateJs: (props) => `
      async function update_${props.id.replace(/-/g, '_')}() {
        const content = document.getElementById('${props.id}-content');
        const badge = document.getElementById('${props.id}-badge');
        try {
          const res = await fetch('/api/ai-usage/claude');
          const data = await res.json();
          if (data.error) {
            content.innerHTML = '<div style="color:#f85149;font-size:11px;">' + _esc(data.error) + '</div>';
            badge.textContent = '!';
            return;
          }
          let html = '';
          const showPlan = ${props.showPlan !== false};
          if (showPlan && data.plan) {
            badge.textContent = _esc(data.plan);
          }
          for (const m of (data.metrics || [])) {
            const pct = m.used != null ? Math.min(100, Math.max(0, m.used)) : 0;
            const color = pct > 80 ? '#f85149' : pct > 50 ? '#d29922' : '#3fb950';
            if (m.format === 'dollars') {
              const val = m.used != null ? '$' + m.used.toFixed(2) : '—';
              html += '<div style="display:flex;justify-content:space-between;font-size:11px;padding:2px 0;">';
              html += '<span>' + _esc(m.label) + '</span><span style="color:#3fb950;">' + _esc(val) + '</span></div>';
            } else {
              html += '<div style="margin-bottom:4px;">';
              html += '<div style="display:flex;justify-content:space-between;font-size:11px;margin-bottom:2px;">';
              html += '<span>' + _esc(m.label) + '</span><span style="color:' + color + ';">' + pct.toFixed(0) + '%</span></div>';
              html += '<div style="height:6px;background:var(--bg-tertiary,#21262d);border-radius:3px;overflow:hidden;">';
              html += '<div style="width:' + pct + '%;height:100%;background:' + color + ';"></div></div></div>';
            }
          }
          content.innerHTML = html || '<div style="color:var(--text-muted);font-size:11px;">No data</div>';
        } catch (e) {
          content.innerHTML = '<div style="color:#f85149;font-size:11px;">Error</div>';
          badge.textContent = '!';
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 300) * 1000});
    `
  },

  'codex-cli': {

    name: 'Codex CLI',
    icon: '🟢',
    category: 'small',
    description: 'Track Codex CLI usage (session, weekly, code reviews). Setup: run `codex` once to authenticate.',
    defaultWidth: 280,
    defaultHeight: 180,
    hasApiKey: false,
    properties: {
      title: 'Codex',
      showPlan: true,
      refreshInterval: 300
    },
    preview: `<div style="padding:4px;font-size:11px;color:#8b949e;">
      <div>Session: 5%</div>
      <div>Weekly: 10%</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">🟢 ${props.title || 'Codex'}</span>
          <span class="dash-card-badge" id="${props.id}-badge">—</span>
        </div>
        <div class="dash-card-body" id="${props.id}-content" style="display:flex;flex-direction:column;gap:4px;overflow-y:auto;">
          <div style="color:var(--text-muted);font-size:11px;">Loading...</div>
        </div>
      </div>`,
    generateJs: (props) => `
      async function update_${props.id.replace(/-/g, '_')}() {
        const content = document.getElementById('${props.id}-content');
        const badge = document.getElementById('${props.id}-badge');
        try {
          const res = await fetch('/api/ai-usage/codex');
          const data = await res.json();
          if (data.error) {
            content.innerHTML = '<div style="color:#f85149;font-size:11px;">' + _esc(data.error) + '</div>';
            badge.textContent = '!';
            return;
          }
          let html = '';
          const showPlan = ${props.showPlan !== false};
          if (showPlan && data.plan) {
            badge.textContent = _esc(data.plan);
          }
          for (const m of (data.metrics || [])) {
            const pct = m.used != null ? Math.min(100, Math.max(0, m.used)) : 0;
            const color = pct > 80 ? '#f85149' : pct > 50 ? '#d29922' : '#3fb950';
            if (m.format === 'dollars') {
              const val = m.remaining != null ? '$' + m.remaining.toFixed(2) : '—';
              html += '<div style="display:flex;justify-content:space-between;font-size:11px;padding:2px 0;">';
              html += '<span>' + _esc(m.label) + '</span><span style="color:#3fb950;">' + _esc(val) + '</span></div>';
            } else {
              html += '<div style="margin-bottom:4px;">';
              html += '<div style="display:flex;justify-content:space-between;font-size:11px;margin-bottom:2px;">';
              html += '<span>' + _esc(m.label) + '</span><span style="color:' + color + ';">' + pct.toFixed(0) + '%</span></div>';
              html += '<div style="height:6px;background:var(--bg-tertiary,#21262d);border-radius:3px;overflow:hidden;">';
              html += '<div style="width:' + pct + '%;height:100%;background:' + color + ';"></div></div></div>';
            }
          }
          content.innerHTML = html || '<div style="color:var(--text-muted);font-size:11px;">No data</div>';
        } catch (e) {
          content.innerHTML = '<div style="color:#f85149;font-size:11px;">Error</div>';
          badge.textContent = '!';
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 300) * 1000});
    `
  },

  'github-copilot': {
    name: 'GitHub Copilot',
    icon: '⚫',
    category: 'small',
    description: 'Track GitHub Copilot usage. Setup: run `gh auth login` first.',
    defaultWidth: 280,
    defaultHeight: 180,
    hasApiKey: false,
    properties: { title: 'Copilot', showPlan: true, refreshInterval: 300 },
    preview: `<div style="padding:4px;font-size:11px;color:#8b949e;"><div>Premium: 20%</div><div>Chat: 5%</div></div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head"><span class="dash-card-title">⚫ ${props.title || 'Copilot'}</span><span class="dash-card-badge" id="${props.id}-badge">—</span></div>
        <div class="dash-card-body" id="${props.id}-content" style="display:flex;flex-direction:column;gap:4px;overflow-y:auto;"><div style="color:var(--text-muted);font-size:11px;">Loading...</div></div>
      </div>`,
    generateJs: (props) => `
      async function update_${props.id.replace(/-/g, '_')}() {
        const content = document.getElementById('${props.id}-content');
        const badge = document.getElementById('${props.id}-badge');
        try {
          const res = await fetch('/api/ai-usage/copilot');
          const data = await res.json();
          if (data.error) { content.innerHTML = '<div style="color:#f85149;font-size:11px;">' + _esc(data.error) + '</div>'; badge.textContent = '!'; return; }
          let html = '';
          if (${props.showPlan !== false} && data.plan) badge.textContent = _esc(data.plan);
          for (const m of (data.metrics || [])) {
            const pct = m.used != null ? Math.min(100, Math.max(0, m.used)) : 0;
            const color = pct > 80 ? '#f85149' : pct > 50 ? '#d29922' : '#3fb950';
            html += '<div style="margin-bottom:4px;"><div style="display:flex;justify-content:space-between;font-size:11px;margin-bottom:2px;"><span>' + _esc(m.label) + '</span><span style="color:' + color + ';">' + pct.toFixed(0) + '%</span></div><div style="height:6px;background:var(--bg-tertiary,#21262d);border-radius:3px;overflow:hidden;"><div style="width:' + pct + '%;height:100%;background:' + color + ';"></div></div></div>';
          }
          content.innerHTML = html || '<div style="color:var(--text-muted);font-size:11px;">No data</div>';
        } catch (e) { content.innerHTML = '<div style="color:#f85149;font-size:11px;">Error</div>'; badge.textContent = '!'; }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 300) * 1000});
    `
  },

  'cursor': {
    name: 'Cursor',
    icon: '🔵',
    category: 'small',
    description: 'Track Cursor IDE usage. Setup: just use Cursor normally — reads from IDE database.',
    defaultWidth: 280,
    defaultHeight: 180,
    hasApiKey: false,
    properties: { title: 'Cursor', showPlan: true, refreshInterval: 300 },
    preview: `<div style="padding:4px;font-size:11px;color:#8b949e;"><div>Total: 15%</div><div>API: 46%</div></div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head"><span class="dash-card-title">🔵 ${props.title || 'Cursor'}</span><span class="dash-card-badge" id="${props.id}-badge">—</span></div>
        <div class="dash-card-body" id="${props.id}-content" style="display:flex;flex-direction:column;gap:4px;overflow-y:auto;"><div style="color:var(--text-muted);font-size:11px;">Loading...</div></div>
      </div>`,
    generateJs: (props) => `
      async function update_${props.id.replace(/-/g, '_')}() {
        const content = document.getElementById('${props.id}-content');
        const badge = document.getElementById('${props.id}-badge');
        try {
          const res = await fetch('/api/ai-usage/cursor');
          const data = await res.json();
          if (data.error) { content.innerHTML = '<div style="color:#f85149;font-size:11px;">' + _esc(data.error) + '</div>'; badge.textContent = '!'; return; }
          let html = '';
          if (${props.showPlan !== false} && data.plan) badge.textContent = _esc(data.plan);
          for (const m of (data.metrics || [])) {
            const pct = m.used != null ? Math.min(100, Math.max(0, m.used)) : 0;
            const color = pct > 80 ? '#f85149' : pct > 50 ? '#d29922' : '#3fb950';
            html += '<div style="margin-bottom:4px;"><div style="display:flex;justify-content:space-between;font-size:11px;margin-bottom:2px;"><span>' + _esc(m.label) + '</span><span style="color:' + color + ';">' + pct.toFixed(0) + '%</span></div><div style="height:6px;background:var(--bg-tertiary,#21262d);border-radius:3px;overflow:hidden;"><div style="width:' + pct + '%;height:100%;background:' + color + ';"></div></div></div>';
          }
          content.innerHTML = html || '<div style="color:var(--text-muted);font-size:11px;">No data</div>';
        } catch (e) { content.innerHTML = '<div style="color:#f85149;font-size:11px;">Error</div>'; badge.textContent = '!'; }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 300) * 1000});
    `
  },

  'gemini-cli': {
    name: 'Gemini CLI',
    icon: '🔷',
    category: 'small',
    description: 'Track Gemini CLI usage. Setup: run `gemini` once to authenticate via browser.',
    defaultWidth: 280,
    defaultHeight: 180,
    hasApiKey: false,
    properties: { title: 'Gemini', showPlan: true, refreshInterval: 300 },
    preview: `<div style="padding:4px;font-size:11px;color:#8b949e;"><div>Pro: 10%</div><div>Flash: 5%</div></div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head"><span class="dash-card-title">🔷 ${props.title || 'Gemini'}</span><span class="dash-card-badge" id="${props.id}-badge">—</span></div>
        <div class="dash-card-body" id="${props.id}-content" style="display:flex;flex-direction:column;gap:4px;overflow-y:auto;"><div style="color:var(--text-muted);font-size:11px;">Loading...</div></div>
      </div>`,
    generateJs: (props) => `
      async function update_${props.id.replace(/-/g, '_')}() {
        const content = document.getElementById('${props.id}-content');
        const badge = document.getElementById('${props.id}-badge');
        try {
          const res = await fetch('/api/ai-usage/gemini');
          const data = await res.json();
          if (data.error) { content.innerHTML = '<div style="color:#f85149;font-size:11px;">' + _esc(data.error) + '</div>'; badge.textContent = '!'; return; }
          let html = '';
          if (${props.showPlan !== false} && data.plan) badge.textContent = _esc(data.plan);
          for (const m of (data.metrics || [])) {
            const pct = m.used != null ? Math.min(100, Math.max(0, m.used)) : 0;
            const color = pct > 80 ? '#f85149' : pct > 50 ? '#d29922' : '#3fb950';
            html += '<div style="margin-bottom:4px;"><div style="display:flex;justify-content:space-between;font-size:11px;margin-bottom:2px;"><span>' + _esc(m.label) + '</span><span style="color:' + color + ';">' + pct.toFixed(0) + '%</span></div><div style="height:6px;background:var(--bg-tertiary,#21262d);border-radius:3px;overflow:hidden;"><div style="width:' + pct + '%;height:100%;background:' + color + ';"></div></div></div>';
          }
          content.innerHTML = html || '<div style="color:var(--text-muted);font-size:11px;">No data</div>';
        } catch (e) { content.innerHTML = '<div style="color:#f85149;font-size:11px;">Error</div>'; badge.textContent = '!'; }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 300) * 1000});
    `
  },

  'amp-code': {
    name: 'Amp Code',
    icon: '⚡',
    category: 'small',
    description: 'Track Amp Code usage. Setup: run `amp` once to authenticate.',
    defaultWidth: 280,
    defaultHeight: 180,
    hasApiKey: false,
    properties: { title: 'Amp', showPlan: true, refreshInterval: 300 },
    preview: `<div style="padding:4px;font-size:11px;color:#8b949e;"><div>Free: 30%</div><div>Credits: $5.00</div></div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head"><span class="dash-card-title">⚡ ${props.title || 'Amp'}</span><span class="dash-card-badge" id="${props.id}-badge">—</span></div>
        <div class="dash-card-body" id="${props.id}-content" style="display:flex;flex-direction:column;gap:4px;overflow-y:auto;"><div style="color:var(--text-muted);font-size:11px;">Loading...</div></div>
      </div>`,
    generateJs: (props) => `
      async function update_${props.id.replace(/-/g, '_')}() {
        const content = document.getElementById('${props.id}-content');
        const badge = document.getElementById('${props.id}-badge');
        try {
          const res = await fetch('/api/ai-usage/amp');
          const data = await res.json();
          if (data.error) { content.innerHTML = '<div style="color:#f85149;font-size:11px;">' + _esc(data.error) + '</div>'; badge.textContent = '!'; return; }
          let html = '';
          if (${props.showPlan !== false} && data.plan) badge.textContent = _esc(data.plan);
          for (const m of (data.metrics || [])) {
            if (m.format === 'dollars') {
              const val = m.remaining != null ? '$' + m.remaining.toFixed(2) : '—';
              html += '<div style="display:flex;justify-content:space-between;font-size:11px;padding:2px 0;"><span>' + _esc(m.label) + '</span><span style="color:#3fb950;">' + _esc(val) + '</span></div>';
            } else {
              const pct = m.used != null ? Math.min(100, Math.max(0, m.used)) : 0;
              const color = pct > 80 ? '#f85149' : pct > 50 ? '#d29922' : '#3fb950';
              html += '<div style="margin-bottom:4px;"><div style="display:flex;justify-content:space-between;font-size:11px;margin-bottom:2px;"><span>' + _esc(m.label) + '</span><span style="color:' + color + ';">' + pct.toFixed(0) + '%</span></div><div style="height:6px;background:var(--bg-tertiary,#21262d);border-radius:3px;overflow:hidden;"><div style="width:' + pct + '%;height:100%;background:' + color + ';"></div></div></div>';
            }
          }
          content.innerHTML = html || '<div style="color:var(--text-muted);font-size:11px;">No data</div>';
        } catch (e) { content.innerHTML = '<div style="color:#f85149;font-size:11px;">Error</div>'; badge.textContent = '!'; }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 300) * 1000});
    `
  },

  'factory': {
    name: 'Factory',
    icon: '🏭',
    category: 'small',
    description: 'Track Factory (Droid) usage. Setup: run `factory` once to authenticate.',
    defaultWidth: 280, defaultHeight: 180, hasApiKey: false,
    properties: { title: 'Factory', showPlan: true, refreshInterval: 300 },
    preview: `<div style="padding:4px;font-size:11px;color:#8b949e;"><div>Standard: 25%</div></div>`,
    generateHtml: (props) => `<div class="dash-card" id="widget-${props.id}" style="height:100%;"><div class="dash-card-head"><span class="dash-card-title">🏭 ${props.title || 'Factory'}</span><span class="dash-card-badge" id="${props.id}-badge">—</span></div><div class="dash-card-body" id="${props.id}-content" style="display:flex;flex-direction:column;gap:4px;overflow-y:auto;"><div style="color:var(--text-muted);font-size:11px;">Loading...</div></div></div>`,
    generateJs: (props) => `async function update_${props.id.replace(/-/g, '_')}(){const content=document.getElementById('${props.id}-content');const badge=document.getElementById('${props.id}-badge');try{const res=await fetch('/api/ai-usage/factory');const data=await res.json();if(data.error){content.innerHTML='<div style="color:#f85149;font-size:11px;">'+_esc(data.error)+'</div>';badge.textContent='!';return;}let html='';if(${props.showPlan !== false}&&data.plan)badge.textContent=_esc(data.plan);for(const m of(data.metrics||[])){const pct=m.used!=null?Math.min(100,Math.max(0,m.used)):0;const color=pct>80?'#f85149':pct>50?'#d29922':'#3fb950';html+='<div style="margin-bottom:4px;"><div style="display:flex;justify-content:space-between;font-size:11px;margin-bottom:2px;"><span>'+_esc(m.label)+'</span><span style="color:'+color+';">'+pct.toFixed(0)+'%</span></div><div style="height:6px;background:var(--bg-tertiary,#21262d);border-radius:3px;overflow:hidden;"><div style="width:'+pct+'%;height:100%;background:'+color+';"></div></div></div>';}content.innerHTML=html||'<div style="color:var(--text-muted);font-size:11px;">No data</div>';}catch(e){content.innerHTML='<div style="color:#f85149;font-size:11px;">Error</div>';badge.textContent='!';}}update_${props.id.replace(/-/g, '_')}();setInterval(update_${props.id.replace(/-/g, '_')},${(props.refreshInterval||300)*1000});`
  },

  'kimi-code': {
    name: 'Kimi Code',
    icon: '🌙',
    category: 'small',
    description: 'Track Kimi Code usage. Setup: run `kimi` once to authenticate.',
    defaultWidth: 280, defaultHeight: 180, hasApiKey: false,
    properties: { title: 'Kimi', showPlan: true, refreshInterval: 300 },
    preview: `<div style="padding:4px;font-size:11px;color:#8b949e;"><div>Session: 26%</div></div>`,
    generateHtml: (props) => `<div class="dash-card" id="widget-${props.id}" style="height:100%;"><div class="dash-card-head"><span class="dash-card-title">🌙 ${props.title || 'Kimi'}</span><span class="dash-card-badge" id="${props.id}-badge">—</span></div><div class="dash-card-body" id="${props.id}-content" style="display:flex;flex-direction:column;gap:4px;overflow-y:auto;"><div style="color:var(--text-muted);font-size:11px;">Loading...</div></div></div>`,
    generateJs: (props) => `async function update_${props.id.replace(/-/g, '_')}(){const content=document.getElementById('${props.id}-content');const badge=document.getElementById('${props.id}-badge');try{const res=await fetch('/api/ai-usage/kimi');const data=await res.json();if(data.error){content.innerHTML='<div style="color:#f85149;font-size:11px;">'+_esc(data.error)+'</div>';badge.textContent='!';return;}let html='';if(${props.showPlan !== false}&&data.plan)badge.textContent=_esc(data.plan);for(const m of(data.metrics||[])){const pct=m.used!=null?Math.min(100,Math.max(0,m.used)):0;const color=pct>80?'#f85149':pct>50?'#d29922':'#3fb950';html+='<div style="margin-bottom:4px;"><div style="display:flex;justify-content:space-between;font-size:11px;margin-bottom:2px;"><span>'+_esc(m.label)+'</span><span style="color:'+color+';">'+pct.toFixed(0)+'%</span></div><div style="height:6px;background:var(--bg-tertiary,#21262d);border-radius:3px;overflow:hidden;"><div style="width:'+pct+'%;height:100%;background:'+color+';"></div></div></div>';}content.innerHTML=html||'<div style="color:var(--text-muted);font-size:11px;">No data</div>';}catch(e){content.innerHTML='<div style="color:#f85149;font-size:11px;">Error</div>';badge.textContent='!';}}update_${props.id.replace(/-/g, '_')}();setInterval(update_${props.id.replace(/-/g, '_')},${(props.refreshInterval||300)*1000});`
  },

  'jetbrains-ai': {
    name: 'JetBrains AI',
    icon: '🧠',
    category: 'small',
    description: 'Track JetBrains AI Assistant usage. Setup: sign into AI Assistant in any JetBrains IDE.',
    defaultWidth: 280, defaultHeight: 180, hasApiKey: false,
    properties: { title: 'JetBrains', showPlan: true, refreshInterval: 300 },
    preview: `<div style="padding:4px;font-size:11px;color:#8b949e;"><div>Quota: 15%</div></div>`,
    generateHtml: (props) => `<div class="dash-card" id="widget-${props.id}" style="height:100%;"><div class="dash-card-head"><span class="dash-card-title">🧠 ${props.title || 'JetBrains'}</span><span class="dash-card-badge" id="${props.id}-badge">—</span></div><div class="dash-card-body" id="${props.id}-content" style="display:flex;flex-direction:column;gap:4px;overflow-y:auto;"><div style="color:var(--text-muted);font-size:11px;">Loading...</div></div></div>`,
    generateJs: (props) => `async function update_${props.id.replace(/-/g, '_')}(){const content=document.getElementById('${props.id}-content');const badge=document.getElementById('${props.id}-badge');try{const res=await fetch('/api/ai-usage/jetbrains');const data=await res.json();if(data.error){content.innerHTML='<div style="color:#f85149;font-size:11px;">'+_esc(data.error)+'</div>';badge.textContent='!';return;}let html='';if(${props.showPlan !== false}&&data.plan)badge.textContent=_esc(data.plan);for(const m of(data.metrics||[])){const pct=m.used!=null?Math.min(100,Math.max(0,m.used)):0;const color=pct>80?'#f85149':pct>50?'#d29922':'#3fb950';html+='<div style="margin-bottom:4px;"><div style="display:flex;justify-content:space-between;font-size:11px;margin-bottom:2px;"><span>'+_esc(m.label)+'</span><span style="color:'+color+';">'+pct.toFixed(0)+'%</span></div><div style="height:6px;background:var(--bg-tertiary,#21262d);border-radius:3px;overflow:hidden;"><div style="width:'+pct+'%;height:100%;background:'+color+';"></div></div></div>';}content.innerHTML=html||'<div style="color:var(--text-muted);font-size:11px;">No data</div>';}catch(e){content.innerHTML='<div style="color:#f85149;font-size:11px;">Error</div>';badge.textContent='!';}}update_${props.id.replace(/-/g, '_')}();setInterval(update_${props.id.replace(/-/g, '_')},${(props.refreshInterval||300)*1000});`
  },

  'minimax': {
    name: 'MiniMax',
    icon: '🔶',
    category: 'small',
    description: 'Track MiniMax Coding usage. Requires MINIMAX_API_KEY env var.',
    defaultWidth: 280, defaultHeight: 180, hasApiKey: false,
    properties: { title: 'MiniMax', showPlan: true, refreshInterval: 300 },
    preview: `<div style="padding:4px;font-size:11px;color:#8b949e;"><div>Session: 30%</div></div>`,
    generateHtml: (props) => `<div class="dash-card" id="widget-${props.id}" style="height:100%;"><div class="dash-card-head"><span class="dash-card-title">🔶 ${props.title || 'MiniMax'}</span><span class="dash-card-badge" id="${props.id}-badge">—</span></div><div class="dash-card-body" id="${props.id}-content" style="display:flex;flex-direction:column;gap:4px;overflow-y:auto;"><div style="color:var(--text-muted);font-size:11px;">Loading...</div></div></div>`,
    generateJs: (props) => `async function update_${props.id.replace(/-/g, '_')}(){const content=document.getElementById('${props.id}-content');const badge=document.getElementById('${props.id}-badge');try{const res=await fetch('/api/ai-usage/minimax');const data=await res.json();if(data.error){content.innerHTML='<div style="color:#f85149;font-size:11px;">'+_esc(data.error)+'</div>';badge.textContent='!';return;}let html='';if(${props.showPlan !== false}&&data.plan)badge.textContent=_esc(data.plan);for(const m of(data.metrics||[])){const pct=m.used!=null?Math.min(100,Math.max(0,m.used)):0;const color=pct>80?'#f85149':pct>50?'#d29922':'#3fb950';html+='<div style="margin-bottom:4px;"><div style="display:flex;justify-content:space-between;font-size:11px;margin-bottom:2px;"><span>'+_esc(m.label)+'</span><span style="color:'+color+';">'+pct.toFixed(0)+'%</span></div><div style="height:6px;background:var(--bg-tertiary,#21262d);border-radius:3px;overflow:hidden;"><div style="width:'+pct+'%;height:100%;background:'+color+';"></div></div></div>';}content.innerHTML=html||'<div style="color:var(--text-muted);font-size:11px;">No data</div>';}catch(e){content.innerHTML='<div style="color:#f85149;font-size:11px;">Error</div>';badge.textContent='!';}}update_${props.id.replace(/-/g, '_')}();setInterval(update_${props.id.replace(/-/g, '_')},${(props.refreshInterval||300)*1000});`
  },

  'zai': {
    name: 'Z.ai',
    icon: '🇿',
    category: 'small',
    description: 'Track Z.ai (GLM Coding) usage. Requires ZAI_API_KEY env var.',
    defaultWidth: 280, defaultHeight: 180, hasApiKey: false,
    properties: { title: 'Z.ai', showPlan: true, refreshInterval: 300 },
    preview: `<div style="padding:4px;font-size:11px;color:#8b949e;"><div>Session: 15%</div><div>Weekly: 45%</div></div>`,
    generateHtml: (props) => `<div class="dash-card" id="widget-${props.id}" style="height:100%;"><div class="dash-card-head"><span class="dash-card-title">🇿 ${props.title || 'Z.ai'}</span><span class="dash-card-badge" id="${props.id}-badge">—</span></div><div class="dash-card-body" id="${props.id}-content" style="display:flex;flex-direction:column;gap:4px;overflow-y:auto;"><div style="color:var(--text-muted);font-size:11px;">Loading...</div></div></div>`,
    generateJs: (props) => `async function update_${props.id.replace(/-/g, '_')}(){const content=document.getElementById('${props.id}-content');const badge=document.getElementById('${props.id}-badge');try{const res=await fetch('/api/ai-usage/zai');const data=await res.json();if(data.error){content.innerHTML='<div style="color:#f85149;font-size:11px;">'+_esc(data.error)+'</div>';badge.textContent='!';return;}let html='';if(${props.showPlan !== false}&&data.plan)badge.textContent=_esc(data.plan);for(const m of(data.metrics||[])){const pct=m.used!=null?Math.min(100,Math.max(0,m.used)):0;const color=pct>80?'#f85149':pct>50?'#d29922':'#3fb950';html+='<div style="margin-bottom:4px;"><div style="display:flex;justify-content:space-between;font-size:11px;margin-bottom:2px;"><span>'+_esc(m.label)+'</span><span style="color:'+color+';">'+pct.toFixed(0)+'%</span></div><div style="height:6px;background:var(--bg-tertiary,#21262d);border-radius:3px;overflow:hidden;"><div style="width:'+pct+'%;height:100%;background:'+color+';"></div></div></div>';}content.innerHTML=html||'<div style="color:var(--text-muted);font-size:11px;">No data</div>';}catch(e){content.innerHTML='<div style="color:#f85149;font-size:11px;">Error</div>';badge.textContent='!';}}update_${props.id.replace(/-/g, '_')}();setInterval(update_${props.id.replace(/-/g, '_')},${(props.refreshInterval||300)*1000});`
  },

  'antigravity-local': {
    name: 'Antigravity',
    icon: '🪐',
    category: 'small',
    description: 'Track Google Antigravity usage (Gemini 3, Claude via Google). Requires antigravity-usage login.',
    defaultWidth: 280, defaultHeight: 200, hasApiKey: false,
    properties: { title: 'Antigravity', showPlan: true, refreshInterval: 300 },
    preview: `<div style="padding:4px;font-size:11px;color:#8b949e;"><div>Gemini 3 Pro: 25%</div><div>Claude Sonnet: 40%</div></div>`,
    generateHtml: (props) => `<div class="dash-card" id="widget-${props.id}" style="height:100%;"><div class="dash-card-head"><span class="dash-card-title">🪐 ${props.title || 'Antigravity'}</span><span class="dash-card-badge" id="${props.id}-badge">—</span></div><div class="dash-card-body" id="${props.id}-content" style="display:flex;flex-direction:column;gap:4px;overflow-y:auto;"><div style="color:var(--text-muted);font-size:11px;">Loading...</div></div></div>`,
    generateJs: (props) => `async function update_${props.id.replace(/-/g, '_')}(){const content=document.getElementById('${props.id}-content');const badge=document.getElementById('${props.id}-badge');try{const res=await fetch('/api/ai-usage/antigravity');const data=await res.json();if(data.error){content.innerHTML='<div style="color:#f85149;font-size:11px;">'+_esc(data.error)+'</div>';badge.textContent='!';return;}let html='';if(${props.showPlan !== false}&&data.plan)badge.textContent=_esc(data.plan);for(const m of(data.metrics||[])){const pct=m.used!=null?Math.min(100,Math.max(0,m.used)):0;const color=pct>80?'#f85149':pct>50?'#d29922':'#3fb950';html+='<div style="margin-bottom:4px;"><div style="display:flex;justify-content:space-between;font-size:11px;margin-bottom:2px;"><span>'+_esc(m.label)+'</span><span style="color:'+color+';">'+pct.toFixed(0)+'%</span></div><div style="height:6px;background:var(--bg-tertiary,#21262d);border-radius:3px;overflow:hidden;"><div style="width:'+pct+'%;height:100%;background:'+color+';"></div></div></div>';}content.innerHTML=html||'<div style="color:var(--text-muted);font-size:11px;">No data</div>';}catch(e){content.innerHTML='<div style="color:#f85149;font-size:11px;">Error</div>';badge.textContent='!';}}update_${props.id.replace(/-/g, '_')}();setInterval(update_${props.id.replace(/-/g, '_')},${(props.refreshInterval||300)*1000});`
  },

  'cron-jobs': {

    name: 'Cron Jobs',
    icon: '⏰',
    category: 'large',
    description: 'Lists scheduled cron jobs from OpenClaw /api/cron endpoint.',
    defaultWidth: 400,
    defaultHeight: 250,
    hasApiKey: false,
    properties: {
      title: 'Cron',
      server: 'local',
      endpoint: '/api/cron',
      columns: 1,
      refreshInterval: 30
    },
    preview: `<div style="padding:4px;font-size:11px;color:#8b949e;">
      <div>⏰ Daily backup - 2am</div>
      <div>⏰ Sync data - */5 *</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('cron')} ${props.title || 'Cron'}</span>
          <span class="dash-card-badge" id="${props.id}-badge">—</span>
        </div>
        <div class="dash-card-body" id="${props.id}-list" style="display:grid;grid-template-columns:repeat(${props.columns || 1}, 1fr);gap:0 12px;align-content:start;">
          <div class="cron-item"><span class="cron-name">Daily backup</span><span class="cron-next">2:00 AM</span></div>
          <div class="cron-item"><span class="cron-name">Sync data</span><span class="cron-next">*/5 min</span></div>
          <div class="cron-item"><span class="cron-name">Health check</span><span class="cron-next">*/15 min</span></div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Cron Jobs Widget: ${props.id} — ${props.server === 'local' ? 'local' : 'remote: ' + props.server}
      async function update_${props.id.replace(/-/g, '_')}() {
        const serverId = '${props.server || 'local'}';
        const list = document.getElementById('${props.id}-list');
        const badge = document.getElementById('${props.id}-badge');
        try {
          let jobs;
          if (serverId === 'local') {
            const res = await fetch('${props.endpoint || '/api/cron'}');
            const json = await res.json();
            jobs = json.jobs || [];
          } else {
            const res = await fetch('/api/servers/' + serverId + '/stats');
            const data = await res.json();
            if (data.error) throw new Error(data.error);
            if (!data.openclaw?.cron) throw new Error('Cron data not available');
            jobs = data.openclaw.cron.jobs || [];
          }
          if (!jobs.length) {
            list.innerHTML = '<div class="cron-item"><span class="cron-name" style="opacity:0.5;">No cron jobs found</span></div>';
            badge.textContent = '0';
            return;
          }
          const cols = ${props.columns || 1};
          list.style.display = 'grid';
          list.style.gridTemplateColumns = 'repeat(' + cols + ', 1fr)';
          list.style.gap = '0 12px';
          list.style.alignContent = 'start';
          list.innerHTML = jobs.map(job => {
            const statusDot = job.enabled ? '🟢' : '🔴';
            const lastRun = job.lastRun ? new Date(job.lastRun).toLocaleTimeString('en-US', { month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit' }) : 'Never';
            const statusBadge = job.lastStatus ? (job.lastStatus === 'ok' ? '✓' : '✗') : '';
            return '<div class="cron-item" style="display:flex;align-items:center;gap:8px;padding:4px 0;border-bottom:1px solid var(--border,#30363d);font-size:calc(13px * var(--font-scale, 1));">' +
              '<span style="flex-shrink:0;">' + _esc(statusDot) + '</span>' +
              '<div style="flex:1;min-width:0;">' +
                '<div style="font-weight:500;">' + _esc(job.name) + '</div>' +
              '</div>' +
              '<div style="text-align:right;font-size:0.8em;opacity:0.6;flex-shrink:0;">' +
                '<div>' + _esc(statusBadge) + ' ' + _esc(lastRun) + '</div>' +
              '</div>' +
            '</div>';
          }).join('');
          badge.textContent = jobs.length + ' jobs';
        } catch (e) {
          console.error('Cron jobs widget error:', e);
          list.innerHTML = '<div class="cron-item"><span class="cron-name">Error: ' + _esc(e.message) + '</span></div>';
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 30) * 1000});
    `
  },

  'system-log': {

    name: 'System Log',
    icon: '🔧',
    category: 'large',
    description: 'Shows recent system logs from OpenClaw /api/system-log endpoint.',
    defaultWidth: 500,
    defaultHeight: 400,
    hasApiKey: false,
    properties: {
      title: 'System Log',
      server: 'local',
      endpoint: '/api/system-log',
      maxLines: 50,
      refreshInterval: 10
    },
    preview: `<div style="padding:4px;font-size:10px;font-family:monospace;color:#8b949e;">
      <div>[INFO] System started</div>
      <div>[DEBUG] Loading config</div>
      <div>[INFO] Ready</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('system-log')} ${props.title || 'System Log'}</span>
          <span class="dash-card-badge" id="${props.id}-badge">—</span>
        </div>
        <div class="dash-card-body compact-list syslog-scroll" id="${props.id}-log">
          <div class="syslog-entry info"><span class="syslog-icon">●</span><span class="syslog-time">9:00am</span><span class="syslog-msg">System started</span><span class="syslog-cat">gateway</span></div>
        </div>
      </div>`,
    generateJs: (props) => `
      function getLogIcon(level) {
        if (level === 'ERROR') return '❌';
        if (level === 'WARN') return '⚠️';
        if (level === 'OK') return '✅';
        return '●';
      }
      function getLogClass(level) {
        if (level === 'ERROR') return 'error';
        if (level === 'WARN') return 'warn';
        if (level === 'OK') return 'ok';
        return 'info';
      }
      // System Log Widget: ${props.id} — ${props.server === 'local' ? 'local' : 'remote: ' + props.server}
      async function update_${props.id.replace(/-/g, '_')}() {
        const serverId = '${props.server || 'local'}';
        try {
          let entries = [];
          if (serverId === 'local') {
            const res = await fetch('${props.endpoint || '/api/system-log'}?max=${props.maxLines || 50}');
            const json = await res.json();
            entries = json.entries || [];
            if (!entries.length && json.lines && json.lines.length) {
              entries = json.lines.map(line => {
                let level = 'INFO';
                if (/\\b(error|fatal)\\b/i.test(line)) level = 'ERROR';
                else if (/\\bwarn/i.test(line)) level = 'WARN';
                else if (/\\b(ok|success|ready|started)\\b/i.test(line)) level = 'OK';
                return { time: new Date().toISOString(), level, category: 'system', message: line };
              });
            }
          } else {
            const res = await fetch('/api/servers/' + serverId + '/stats');
            const data = await res.json();
            if (data.error) throw new Error(data.error);
            entries = data.openclaw?.systemLog?.entries || [];
          }
          const log = document.getElementById('${props.id}-log');
          const badge = document.getElementById('${props.id}-badge');
          const wasAtBottom = log.scrollTop + log.clientHeight >= log.scrollHeight - 20;
          const errorCount = entries.filter(e => e.level === 'ERROR').length;
          badge.textContent = errorCount > 0 ? errorCount + ' error' + (errorCount > 1 ? 's' : '') : entries.length + ' events';
          badge.style.color = errorCount > 0 ? '#f85149' : '';
          const fs = 'calc(11px * var(--font-scale, 1))';
          log.innerHTML = entries.slice(0, ${props.maxLines || 50}).map(entry => {
            const cls = getLogClass(entry.level);
            const icon = getLogIcon(entry.level);
            const time = entry.time ? new Date(entry.time).toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit', hour12: true }).toLowerCase() : '';
            const msg = (entry.message || '').replace(/</g, '&lt;').replace(/>/g, '&gt;');
            const cat = (entry.category || '').replace(/</g, '&lt;');
            return '<div class="syslog-entry ' + cls + '" style="display:flex;align-items:flex-start;gap:6px;padding:3px 0;border-bottom:1px solid #30363d;font-size:' + fs + ';line-height:1.3;" title="' + msg + '">' +
              '<span class="syslog-icon" style="flex-shrink:0;width:14px;text-align:center;font-size:calc(10px * var(--font-scale, 1));">' + icon + '</span>' +
              '<span class="syslog-time" style="flex-shrink:0;color:#8b949e;font-size:calc(10px * var(--font-scale, 1));font-family:monospace;min-width:55px;">' + time + '</span>' +
              '<span class="syslog-msg" style="flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:' + (cls === 'error' ? '#f85149' : cls === 'warn' ? '#d29922' : cls === 'ok' ? '#3fb950' : '#c9d1d9') + ';">' + msg + '</span>' +
              '<span class="syslog-cat" style="flex-shrink:0;font-size:calc(9px * var(--font-scale, 1));padding:1px 4px;border-radius:3px;background:#161b22;color:#8b949e;font-family:monospace;">' + cat + '</span>' +
            '</div>';
          }).join('');
          if (wasAtBottom) log.scrollTop = log.scrollHeight;
        } catch (e) {
          console.error('System log widget error:', e);
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${Math.max((props.refreshInterval || 10), 30) * 1000});
    `
  },

  'calendar': {

    name: 'Calendar',
    icon: '📅',
    category: 'large',
    description: 'Displays upcoming events from an iCal (.ics) feed URL. Works with Google Calendar, Outlook, and Apple Calendar.',
    defaultWidth: 400,
    defaultHeight: 300,
    properties: {
      title: 'Calendar',
      icalUrl: '',
      maxEvents: 5,
      refreshInterval: 300
    },
    preview: `<div style="padding:4px;font-size:11px;color:#8b949e;">
      <div>📅 Team standup - 10am</div>
      <div>📅 1:1 with Bob - 2pm</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('calendar')} ${props.title || 'Calendar'}</span>
        </div>
        <div class="dash-card-body" id="${props.id}-events" style="overflow-y:auto;">
          <div style="color:#8b949e;font-size:calc(13px * var(--font-scale, 1));">Loading events…</div>
        </div>
      </div>`,
    generateJs: (props) => `
      async function update_${props.id.replace(/-/g, '_')}() {
        const container = document.getElementById('${props.id}-events');
        const icalUrl = ${JSON.stringify(props.icalUrl || '')};
        if (!icalUrl) {
          container.innerHTML = '<div style="color:#8b949e;font-size:calc(13px * var(--font-scale, 1));">Set an iCal feed URL in widget settings</div>';
          return;
        }
        try {
          const resp = await fetch('/api/calendar?url=' + encodeURIComponent(icalUrl) + '&max=${props.maxEvents || 5}');
          if (!resp.ok) throw new Error('HTTP ' + resp.status);
          const events = await resp.json();
          if (!events.length) {
            container.innerHTML = '<div style="color:#8b949e;font-size:calc(13px * var(--font-scale, 1));">No upcoming events</div>';
            return;
          }
          function _escHtml(s) { var d = document.createElement('div'); d.textContent = s; return d.innerHTML; }
          function _linkify(s) { return _escHtml(s).replace(/(https?:\\/\\/[^\\s<]+)/g, '<a href="$1" target="_blank" rel="noopener" style="color:#58a6ff;text-decoration:underline;">$1</a>'); }
          container.innerHTML = events.map(function(ev) {
            var timeStr = ev.allDay ? 'All Day' : new Date(ev.start).toLocaleTimeString([], { hour: 'numeric', minute: '2-digit' });
            return '<div style="padding:4px 0;border-bottom:1px solid #21262d;font-size:calc(13px * var(--font-scale, 1));">' +
              '<span style="color:#58a6ff;">' + timeStr + '</span> ' +
              '<span style="color:#e6edf3;">' + _linkify(ev.summary || 'Untitled') + '</span>' +
              (ev.location ? '<div style="color:#8b949e;font-size:calc(11px * var(--font-scale, 1));margin-top:2px;">📍 ' + _linkify(ev.location) + '</div>' : '') +
              '</div>';
          }).join('');
        } catch (e) {
          console.error('Calendar widget error:', e);
          container.innerHTML = '<div style="color:#f85149;font-size:calc(13px * var(--font-scale, 1));">Failed to load calendar</div>';
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${Math.max((props.refreshInterval || 300), 60) * 1000});
    `
  },

  'notes': {
    name: 'Notes',
    icon: '📝',
    category: 'large',
    description: 'Simple note-taking widget with persistent storage.',
    defaultWidth: 350,
    defaultHeight: 300,
    hasApiKey: false,
    properties: {
      title: 'Notes'
    },
    preview: `<div style="padding:4px;font-size:11px;">
      <div>📝 Remember to check logs</div>
      <div>📝 Update docs</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('notes')} ${props.title || 'Notes'}</span>
          <span class="dash-card-badge" id="${props.id}-badge">0</span>
        </div>
        <div class="dash-card-body" style="display:flex;flex-direction:column;height:100%;overflow:hidden;">
          <div style="display:flex;gap:6px;padding:0 0 8px 0;flex-shrink:0;">
            <textarea id="${props.id}-input" placeholder="Add a note..." rows="2" style="flex:1;background:var(--bg-tertiary);border:1px solid var(--border);border-radius:4px;padding:4px 8px;color:var(--text-primary);font-size:calc(12px * var(--font-scale, 1));resize:none;font-family:inherit;"></textarea>
            <button id="${props.id}-add-btn" style="background:var(--accent-blue);color:#fff;border:none;border-radius:4px;padding:4px 10px;cursor:pointer;font-size:calc(12px * var(--font-scale, 1));align-self:flex-end;">Add</button>
          </div>
          <div id="${props.id}-list" style="flex:1;overflow-y:auto;"></div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Notes Widget: ${props.id}
      (function() {
        let notes = [];
        const container = document.getElementById('${props.id}-list');
        const input = document.getElementById('${props.id}-input');
        const addBtn = document.getElementById('${props.id}-add-btn');
        const badge = document.getElementById('${props.id}-badge');

        function esc(s) { return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/\\n/g,'<br>'); }

        function render() {
          badge.textContent = notes.length;
          container.innerHTML = notes.map((n, i) =>
            '<div style="display:flex;align-items:flex-start;gap:6px;padding:4px 0;border-bottom:1px solid var(--border);font-size:calc(13px * var(--font-scale, 1));">' +
              '<span style="flex:1;white-space:pre-wrap;word-break:break-word;">' + esc(n.text) + '</span>' +
              '<button data-del="' + i + '" style="background:none;border:none;color:var(--accent-red,#f85149);cursor:pointer;font-size:calc(14px * var(--font-scale, 1));padding:0 4px;flex-shrink:0;">✕</button>' +
            '</div>'
          ).join('');
        }

        function save() {
          fetch('/api/notes').then(r => r.json()).then(all => {
            all['${props.id}'] = notes;
            return fetch('/api/notes', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(all) });
          }).catch(() => {});
        }

        container.addEventListener('click', function(e) {
          if (e.target.dataset.del != null) {
            notes.splice(parseInt(e.target.dataset.del), 1);
            save(); render();
          }
        });

        addBtn.addEventListener('click', function() {
          const text = input.value.trim();
          if (!text) return;
          notes.push({ text: text, ts: Date.now() });
          input.value = '';
          save(); render();
        });

        input.addEventListener('keydown', function(e) {
          if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); addBtn.click(); }
        });

        fetch('/api/notes').then(r => r.json()).then(all => {
          notes = Array.isArray(all['${props.id}']) ? all['${props.id}'] : [];
          render();
        }).catch(() => render());
      })();
    `
  },

  // ─────────────────────────────────────────────
  // BARS
  // ─────────────────────────────────────────────

  'text-header': {
    name: 'Header / Text',
    icon: '🔤',
    category: 'layout',
    description: 'Custom text or heading. Adjustable font size, color, and alignment.',
    defaultWidth: 400,
    defaultHeight: 50,
    hasApiKey: false,
    properties: {
      title: 'My Dashboard',
      showHeader: false,
      showBorder: false,
      fontSize: 24,
      fontColor: '#e6edf3',
      textAlign: 'left',
      fontWeight: 'bold'
    },
    preview: `<div style="padding:8px;font-size:18px;font-weight:bold;">My Dashboard</div>`,
    generateHtml: (props) => `
      <div id="widget-${props.id}" style="height:100%;display:flex;align-items:center;padding:0 12px;
        font-size:${props.fontSize || 24}px;
        color:${props.fontColor || '#e6edf3'};
        text-align:${props.textAlign || 'left'};
        font-weight:${props.fontWeight || 'bold'};
        justify-content:${props.textAlign === 'center' ? 'center' : props.textAlign === 'right' ? 'flex-end' : 'flex-start'};${props.showBorder ? 'border:1px solid #3a4150;border-radius:8px;' : ''}">
        ${props.title || 'Header'}
      </div>`,
    generateJs: () => ''
  },

  'horizontal-line': {
    name: 'Horizontal Line',
    icon: '➖',
    category: 'layout',
    description: 'A horizontal divider line. Resize width to fit.',
    defaultWidth: 600,
    defaultHeight: 10,
    hasApiKey: false,
    properties: {
      title: '',
      showHeader: false,
      lineColor: '#30363d',
      lineThickness: 2
    },
    preview: `<div style="padding:4px 0;"><hr style="border:none;border-top:2px solid #30363d;"></div>`,
    generateHtml: (props) => `
      <div id="widget-${props.id}" style="width:100%;height:100%;display:flex;align-items:center;padding:0;">
        <hr style="width:100%;border:none;border-top:${props.lineThickness || 2}px solid ${props.lineColor || '#30363d'};margin:0;flex-shrink:0;">
      </div>`,
    generateJs: () => ''
  },

  'vertical-line': {
    name: 'Vertical Line',
    icon: '│',
    category: 'layout',
    description: 'A vertical divider line. Resize height to fit.',
    defaultWidth: 10,
    defaultHeight: 300,
    hasApiKey: false,
    properties: {
      title: '',
      showHeader: false,
      lineColor: '#30363d',
      lineThickness: 2
    },
    preview: `<div style="display:flex;justify-content:center;height:40px;"><div style="border-left:2px solid #30363d;height:100%;"></div></div>`,
    generateHtml: (props) => `
      <div id="widget-${props.id}" style="width:100%;height:100%;display:flex;justify-content:center;padding:0;">
        <div style="border-left:${props.lineThickness || 2}px solid ${props.lineColor || '#30363d'};height:100%;flex-shrink:0;"></div>
      </div>`,
    generateJs: () => ''
  },

  // ─────────────────────────────────────────────
  // AI / LLM MONITORING
  // ─────────────────────────────────────────────

  'ai-usage-claude': {
    name: 'Claude Usage',
    icon: '🟣',
    category: 'small',
    description: 'Shows Anthropic Claude API usage and costs. Requires an Admin API key.',
    defaultWidth: 220,
    defaultHeight: 160,
    hasApiKey: true,
    apiKeyName: 'ANTHROPIC_ADMIN_KEY',
    hideApiKeyVar: true,
    properties: {
      title: 'Claude',
      refreshInterval: 300,
      apiKeyNote: ''
    },
    preview: `<div style="text-align:center;padding:8px;">
      <div style="font-size:11px;color:#a371f7;">Claude</div>
      <div style="font-size:18px;">125K tokens</div>
      <div style="font-size:11px;color:#8b949e;">$4.20 today</div>
      <div style="font-size:10px;color:#6e7681;margin-top:4px;">Week $28.50 · Month $95.00</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('ai-claude')} ${props.title || 'Claude'}</span>
        </div>
        <div class="dash-card-body" style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;">
          <div class="kpi-value" id="${props.id}-tokens" style="color:#a371f7;font-size:calc(22px * var(--font-scale, 1));">—</div>
          <div class="kpi-label" id="${props.id}-cost" style="font-size:calc(12px * var(--font-scale, 1));">today</div>
          <div id="${props.id}-period" style="font-size:calc(10px * var(--font-scale, 1));color:#6e7681;margin-top:4px;text-align:center;"></div>
        </div>
      </div>`,
    generateJs: (props) => `
      async function update_${props.id.replace(/-/g, '_')}() {
        try {
          const res = await fetch('/api/usage/claude');
          const data = await res.json();
          const tokensEl = document.getElementById('${props.id}-tokens');
          const costEl = document.getElementById('${props.id}-cost');
          const periodEl = document.getElementById('${props.id}-period');
          if (data.error) {
            tokensEl.textContent = '⚠️';
            tokensEl.style.fontSize = '18px';
            costEl.textContent = data.error.includes('API key') ? 'No API Key' : data.error;
            periodEl.textContent = '';
            return;
          }
          const fmt = (n) => n >= 1000000 ? (n/1000000).toFixed(1)+'M' : n >= 1000 ? (n/1000).toFixed(1)+'K' : n.toString();
          const tokens = data.tokens || 0;
          tokensEl.textContent = fmt(tokens) + ' tokens';
          costEl.textContent = '$' + (data.cost || 0).toFixed(2) + ' today';
          const parts = [];
          if (data.week) parts.push('Week $' + data.week.cost.toFixed(2));
          if (data.month) parts.push('Month $' + data.month.cost.toFixed(2));
          periodEl.textContent = parts.join(' · ');
        } catch (e) {
          document.getElementById('${props.id}-tokens').textContent = '—';
          document.getElementById('${props.id}-cost').textContent = 'Error';
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 300) * 1000});
    `
  },

  /* DROPPED: OpenAI Usage - requires Admin API key which is not available on all plans
  'ai-usage-openai': { ... },
  */

  /* DROPPED: Gemini - no public usage API available
  'ai-usage-gemini': {
    name: 'Gemini Usage',
    icon: '🔵',
    category: 'small',
    description: 'Shows Google Gemini API usage stats. Requires usage API proxy.',
    defaultWidth: 220,
    defaultHeight: 120,
    hasApiKey: true,
    apiKeyName: 'GEMINI_API_KEY',
    properties: {
      title: 'Gemini',
      refreshInterval: 300
    },
    preview: `<div style="text-align:center;padding:8px;">
      <div style="font-size:11px;color:#58a6ff;">Gemini</div>
      <div style="font-size:20px;">45K</div>
      <div style="font-size:10px;color:#8b949e;">tokens today</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">🔵 ${props.title || 'Gemini'}</span>
        </div>
        <div class="dash-card-body" style="display:flex;flex-direction:column;align-items:center;justify-content:center;">
          <div class="kpi-value" id="${props.id}-tokens">—</div>
          <div class="kpi-label" id="${props.id}-cost">tokens today</div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Gemini Usage Widget: ${props.id}
      // Requires a backend proxy - Google API doesn't support browser CORS
      // Set up a proxy endpoint for your usage data
      async function update_${props.id.replace(/-/g, '_')}() {
        try {
          const res = await fetch('/api/usage/gemini');
          const json = await res.json();
          const data = json.data || json;
          document.getElementById('${props.id}-tokens').textContent = ((data.tokens || 0) / 1000).toFixed(1) + 'K';
          if (data.cost) {
            document.getElementById('${props.id}-cost').textContent = '$' + data.cost.toFixed(2) + ' today';
          }
        } catch (e) {
          document.getElementById('${props.id}-tokens').textContent = '—';
          document.getElementById('${props.id}-cost').textContent = 'Configure endpoint';
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 300) * 1000});
    `
  },

  'ai-usage-multi': {
    name: 'AI Usage (All)',
    icon: '🤖',
    category: 'large',
    description: 'Combined view of Claude, GPT, and Gemini usage in one widget.',
    defaultWidth: 400,
    defaultHeight: 280,
    hasApiKey: true,
    apiKeyName: 'Multiple (see below)',
    properties: {
      title: 'AI Usage',
      showClaude: true,
      showOpenAI: true,
      showGemini: true,
      refreshInterval: 300
    },
    preview: `<div style="padding:4px;font-size:11px;">
      <div style="margin:4px 0;"><span style="color:#a371f7;">🟣 Claude</span> 125K tokens</div>
      <div style="margin:4px 0;"><span style="color:#3fb950;">🟢 GPT</span> 89K tokens</div>
      <div style="margin:4px 0;"><span style="color:#58a6ff;">🔵 Gemini</span> 45K tokens</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">🤖 ${props.title || 'AI Usage'}</span>
        </div>
        <div class="dash-card-body" id="${props.id}-usage">
          <div class="usage-row"><span style="color:#a371f7">🟣 Claude</span><span class="usage-tokens">125K · $4.20</span></div>
          <div class="usage-row"><span style="color:#3fb950">🟢 GPT</span><span class="usage-tokens">89K · $2.85</span></div>
          <div class="usage-row"><span style="color:#58a6ff">🔵 Gemini</span><span class="usage-tokens">45K · $0.90</span></div>
        </div>
      </div>`,
    generateJs: (props) => `
      // AI Usage Multi Widget: ${props.id}
      // Requires backend endpoints for each service
      // API Keys needed: ANTHROPIC_API_KEY, OPENAI_API_KEY, GEMINI_API_KEY
      async function update_${props.id.replace(/-/g, '_')}() {
        const container = document.getElementById('${props.id}-usage');
        const services = [];
        ${props.showClaude !== false ? "services.push({ name: 'Claude', icon: '🟣', color: '#a371f7', endpoint: '/api/usage/claude' });" : ''}
        ${props.showOpenAI !== false ? "services.push({ name: 'GPT', icon: '🟢', color: '#3fb950', endpoint: '/api/usage/openai' });" : ''}
        ${props.showGemini !== false ? "services.push({ name: 'Gemini', icon: '🔵', color: '#58a6ff', endpoint: '/api/usage/gemini' });" : ''}
        
        const results = await Promise.all(services.map(async (svc) => {
          try {
            const res = await fetch(svc.endpoint);
            const json = await res.json();
            const data = json.data || json;
            return { ...svc, tokens: data.tokens || 0, cost: data.cost || 0 };
          } catch (e) {
            return { ...svc, tokens: 0, cost: 0, error: true };
          }
        }));
        
        container.innerHTML = results.map(r => {
          const tokensStr = r.error ? '—' : ((r.tokens / 1000).toFixed(1) + 'K');
          const costStr = r.cost ? ' · $' + r.cost.toFixed(2) : '';
          return '<div class="usage-row"><span style="color:' + r.color + '">' + r.icon + ' ' + r.name + '</span><span class="usage-tokens">' + tokensStr + costStr + '</span></div>';
        }).join('');
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 300) * 1000});
    `
  },
  END DROPPED: Gemini + Multi */

  'ai-cost-tracker': {
    name: 'AI Cost Tracker',
    icon: '💰',
    category: 'small',
    description: 'Tracks total AI API spending across providers.',
    defaultWidth: 200,
    defaultHeight: 100,
    hasApiKey: true,
    apiKeyName: 'OPENCLAW_API',
    properties: {
      title: 'AI Costs',
      period: 'today',
      endpoint: '/api/costs',
      refreshInterval: 300
    },
    preview: `<div style="text-align:center;padding:8px;">
      <div style="font-size:20px;color:#3fb950;">$4.27</div>
      <div style="font-size:11px;color:#8b949e;">Today</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('ai-cost')} ${props.title || 'AI Costs'}</span>
        </div>
        <div class="dash-card-body" style="display:flex;align-items:center;justify-content:center;gap:10px;">
          <div class="kpi-value green" id="${props.id}-cost">—</div>
          <div class="kpi-label">${props.period || 'Today'}</div>
        </div>
      </div>`,
    generateJs: (props) => `
      // AI Cost Tracker Widget: ${props.id}
      async function update_${props.id.replace(/-/g, '_')}() {
        try {
          const res = await fetch('${props.endpoint || '/api/costs'}?period=${props.period || 'today'}');
          const json = await res.json();
          const data = json.data || json;
          document.getElementById('${props.id}-cost').textContent = '$' + (data.cost || 0).toFixed(2);
        } catch (e) {
          document.getElementById('${props.id}-cost').textContent = '$—';
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 300) * 1000});
    `
  },

  'api-status': {
    name: 'API Status',
    icon: '🔄',
    category: 'large',
    description: 'Shows health status of multiple API endpoints with colored indicators.',
    defaultWidth: 350,
    defaultHeight: 200,
    hasApiKey: false,
    properties: {
      title: 'API Status',
      services: 'OpenAI,Anthropic,Google,OpenClaw',
      refreshInterval: 60
    },
    preview: `<div style="padding:4px;font-size:11px;">
      <div>🟢 OpenAI</div>
      <div>🟢 Anthropic</div>
      <div>🟡 Google</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('api-status')} ${props.title || 'API Status'}</span>
        </div>
        <div class="dash-card-body" id="${props.id}-status">
          <div class="status-row">🟢 OpenAI</div>
          <div class="status-row">🟢 Anthropic</div>
          <div class="status-row">🟢 Google</div>
        </div>
      </div>`,
    generateJs: (props) => `
      // API Status Widget: ${props.id}
      const services_${props.id.replace(/-/g, '_')} = '${props.services || 'OpenAI,Anthropic'}'.split(',');
      const endpoints_${props.id.replace(/-/g, '_')} = {
        'OpenAI': 'https://status.openai.com/api/v2/status.json',
        'Anthropic': 'https://status.anthropic.com/api/v2/status.json',
        'Google': 'https://status.cloud.google.com/',
        'OpenClaw': '/api/status'
      };
      async function update_${props.id.replace(/-/g, '_')}() {
        const container = document.getElementById('${props.id}-status');
        const results = await Promise.all(services_${props.id.replace(/-/g, '_')}.map(async (svc) => {
          const name = svc.trim();
          try {
            const endpoint = endpoints_${props.id.replace(/-/g, '_')}[name] || '/api/health/' + name.toLowerCase();
            const res = await fetch(endpoint, { mode: 'no-cors' });
            return { name, status: 'ok' };
          } catch (e) {
            return { name, status: 'unknown' };
          }
        }));
        container.innerHTML = results.map(r => {
          const icon = r.status === 'ok' ? '🟢' : r.status === 'error' ? '🔴' : '🟡';
          return '<div class="status-row">' + icon + ' ' + r.name + '</div>';
        }).join('');
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 60) * 1000});
    `
  },

  'session-count': {
    name: 'Active Sessions',
    icon: '💬',
    category: 'small',
    description: 'Shows count of active OpenClaw sessions.',
    defaultWidth: 160,
    defaultHeight: 100,
    hasApiKey: true,
    apiKeyName: 'OPENCLAW_API',
    properties: {
      title: 'Sessions',
      server: 'local',
      endpoint: '/api/sessions',
      refreshInterval: 30
    },
    preview: `<div style="text-align:center;padding:8px;">
      <div style="font-size:28px;color:#58a6ff;">3</div>
      <div style="font-size:11px;color:#8b949e;">Active</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('sessions')} ${props.title || 'Sessions'}</span>
        </div>
        <div class="dash-card-body" style="display:flex;align-items:center;justify-content:center;gap:10px;">
          <div class="kpi-value blue" id="${props.id}-count">—</div>
          <div class="kpi-label">Active</div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Session Count Widget: ${props.id} — ${props.server === 'local' ? 'local' : 'remote: ' + props.server}
      async function update_${props.id.replace(/-/g, '_')}() {
        const serverId = '${props.server || 'local'}';
        try {
          let count;
          if (serverId === 'local') {
            const res = await fetch('${props.endpoint || '/api/sessions'}');
            const json = await res.json();
            const data = json.data || json;
            count = data.active || data.length || 0;
          } else {
            const res = await fetch('/api/servers/' + serverId + '/stats');
            const data = await res.json();
            if (data.error) throw new Error(data.error);
            count = data.openclaw?.sessions?.active || data.openclaw?.sessions?.recent24h || 0;
          }
          document.getElementById('${props.id}-count').textContent = count;
        } catch (e) {
          document.getElementById('${props.id}-count').textContent = '—';
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 30) * 1000});
    `
  },

  'token-gauge': {
    name: 'Token Gauge',
    icon: '📊',
    category: 'small',
    description: 'Visual gauge showing token usage from OpenClaw.',
    defaultWidth: 180,
    defaultHeight: 120,
    hasApiKey: true,
    apiKeyName: 'OPENCLAW_API',
    properties: {
      title: 'Tokens',
      maxTokens: 1000000,
      endpoint: '/api/usage/tokens',
      refreshInterval: 60
    },
    preview: `<div style="text-align:center;padding:8px;">
      <div style="font-size:18px;">425K</div>
      <div style="height:6px;background:#21262d;border-radius:3px;margin:6px 0;"><div style="width:42%;height:100%;background:#58a6ff;border-radius:3px;"></div></div>
      <div style="font-size:10px;color:#8b949e;">of 1M limit</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('tokens')} ${props.title || 'Tokens'}</span>
        </div>
        <div class="dash-card-body" style="display:flex;flex-direction:column;align-items:center;justify-content:center;">
          <div class="kpi-value" id="${props.id}-value">—</div>
          <div class="gauge-bar"><div class="gauge-fill" id="${props.id}-fill"></div></div>
          <div class="kpi-label">of ${((props.maxTokens || 1000000) / 1000000).toFixed(1)}M limit</div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Token Gauge Widget: ${props.id}
      async function update_${props.id.replace(/-/g, '_')}() {
        try {
          const res = await fetch('${props.endpoint || '/api/usage/tokens'}');
          const json = await res.json();
          const data = json.data || json;
          const tokens = data.tokens || 0;
          const max = ${props.maxTokens || 1000000};
          const pct = Math.min(100, (tokens / max) * 100);
          document.getElementById('${props.id}-value').textContent = (tokens / 1000).toFixed(0) + 'K';
          document.getElementById('${props.id}-fill').style.width = pct + '%';
        } catch (e) {
          document.getElementById('${props.id}-value').textContent = '—';
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 60) * 1000});
    `
  },

  // ─────────────────────────────────────────────
  // SYSTEM MONITORING
  // ─────────────────────────────────────────────

  'cpu-memory': {
    name: 'CPU / Memory',
    icon: '💻',
    category: 'small',
    description: 'Shows CPU and memory usage. Supports remote servers via lobsterboard-agent.',
    defaultWidth: 200,
    defaultHeight: 120,
    hasApiKey: false,
    properties: {
      title: 'System',
      server: 'local',
      refreshInterval: 5
    },
    preview: `<div style="padding:8px;font-size:11px;">
      <div>CPU: <span style="color:#58a6ff;">23%</span></div>
      <div>MEM: <span style="color:#3fb950;">4.2GB</span></div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('cpu')} ${props.title || 'System'}</span>
        </div>
        <div class="dash-card-body">
        <div class="sys-row"><span>CPU</span><span class="blue" id="${props.id}-cpu">—</span></div>
        <div class="sys-row"><span>MEM</span><span class="green" id="${props.id}-mem">—</span></div>
        </div>
      </div>`,
    generateJs: (props) => `
      // CPU/Memory Widget: ${props.id} — ${props.server === 'local' ? 'local SSE' : 'remote: ' + props.server}
      onStats('${props.server || 'local'}', function(data) {
        // Handle offline state
        if (data._offline) {
          document.getElementById('${props.id}-cpu').textContent = '⚠️';
          document.getElementById('${props.id}-mem').textContent = 'offline';
          return;
        }
        if (data.cpu) {
          document.getElementById('${props.id}-cpu').textContent = data.cpu.currentLoad.toFixed(0) + '%';
        }
        if (data.memory) {
          const used = (data.memory.active / (1024*1024*1024)).toFixed(1);
          const total = (data.memory.total / (1024*1024*1024)).toFixed(1);
          document.getElementById('${props.id}-mem').textContent = used + ' / ' + total + ' GB';
        }
      }, ${(props.refreshInterval || 5) * 1000});
    `
  },

  'disk-usage': {
    name: 'Disk Usage',
    icon: '💾',
    category: 'small',
    description: 'Shows disk space usage. Supports remote servers via lobsterboard-agent.',
    defaultWidth: 160,
    defaultHeight: 100,
    hasApiKey: false,
    properties: {
      title: 'Disk',
      server: 'local',
      path: '/',
      refreshInterval: 60
    },
    preview: `<div style="text-align:center;padding:8px;">
      <div style="font-size:20px;color:#d29922;">68%</div>
      <div style="font-size:11px;color:#8b949e;">256GB used</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('disk')} ${props.title || 'Disk Usage'}</span>
        </div>
        <div class="dash-card-body" style="display:flex;align-items:center;justify-content:center;gap:10px;">
          <div class="kpi-ring-wrap kpi-ring-sm">
            <svg class="kpi-ring" viewBox="0 0 48 48">
              <circle cx="24" cy="24" r="20" fill="none" stroke="var(--bg-tertiary)" stroke-width="4"/>
              <circle id="${props.id}-ring" cx="24" cy="24" r="20" fill="none" stroke="var(--accent-orange)" stroke-width="4"
                stroke-dasharray="125.66" stroke-dashoffset="125.66" stroke-linecap="round"
                transform="rotate(-90 24 24)" style="transition: stroke-dashoffset 0.6s ease;"/>
            </svg>
            <div class="kpi-ring-label" id="${props.id}-pct">—</div>
          </div>
          <div class="kpi-data">
            <div class="kpi-label" id="${props.id}-size">Disk</div>
          </div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Disk Usage Widget: ${props.id} — ${props.server === 'local' ? 'local SSE' : 'remote: ' + props.server}
      onStats('${props.server || 'local'}', function(data) {
        // Handle offline state
        if (data._offline) {
          document.getElementById('${props.id}-pct').textContent = '⚠️';
          document.getElementById('${props.id}-size').textContent = 'offline';
          document.getElementById('${props.id}-ring').style.strokeDashoffset = 125.66;
          return;
        }
        
        // Handle both local (array) and remote (object) disk data
        let d;
        if (Array.isArray(data.disk)) {
          if (data.disk.length === 0) return;
          const targetMount = '${props.path || '/'}';
          d = data.disk.find(x => x.mount === targetMount) || data.disk[0];
        } else if (data.disk) {
          d = data.disk;
        } else {
          return;
        }
        const pct = d.use || d.percent || 0;
        const circumference = 125.66;
        document.getElementById('${props.id}-ring').style.strokeDashoffset = circumference - (pct / 100) * circumference;
        document.getElementById('${props.id}-pct').textContent = Math.round(pct) + '%';
        const usedGB = ((d.used || 0) / (1024*1024*1024)).toFixed(1);
        const totalGB = ((d.size || d.total || 0) / (1024*1024*1024)).toFixed(0);
        document.getElementById('${props.id}-size').textContent = usedGB + ' / ' + totalGB + ' GB';
      }, ${(props.refreshInterval || 60) * 1000});
    `
  },

  'uptime-monitor': {
    name: 'Uptime Monitor',
    icon: '📡',
    category: 'large',
    description: 'Shows system uptime, CPU, and memory. Supports remote servers via lobsterboard-agent.',
    defaultWidth: 350,
    defaultHeight: 220,
    hasApiKey: false,
    properties: {
      title: 'Uptime',
      server: 'local',
      refreshInterval: 30
    },
    preview: `<div style="padding:4px;font-size:11px;">
      <div>🟢 System — 5d 12h</div>
      <div>🟢 CPU — 12.5%</div>
      <div>🟢 Memory — 45.2%</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('uptime')} ${props.title || 'Uptime'}</span>
          ${props.server && props.server !== 'local' ? `<span class="dash-card-badge" style="font-size:10px;">🌐</span>` : ''}
        </div>
        <div class="dash-card-body" id="${props.id}-services">
          <div class="uptime-row" style="color:var(--text-muted);justify-content:center;">Loading...</div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Uptime Monitor Widget: ${props.id} — ${props.server === 'local' ? 'local SSE' : 'remote: ' + props.server}
      onStats('${props.server || 'local'}', function(data) {
        const container = document.getElementById('${props.id}-services');
        
        // Handle offline state
        if (data._offline) {
          const lastSeen = data._lastSuccess ? new Date(data._lastSuccess).toLocaleTimeString() : 'never';
          container.innerHTML = '<div class="uptime-row" style="color:#f85149;justify-content:center;">⚠️ Connection lost</div>' +
            '<div class="uptime-row" style="opacity:0.6;font-size:11px;justify-content:center;">Last: ' + lastSeen + '</div>';
          return;
        }
        
        if (data.uptime == null) return;
        const secs = data.uptime;
        const d = Math.floor(secs / 86400);
        const h = Math.floor((secs % 86400) / 3600);
        const m = Math.floor((secs % 3600) / 60);
        let uptimeStr = '';
        if (d > 0) uptimeStr = d + 'd ' + h + 'h ' + m + 'm';
        else if (h > 0) uptimeStr = h + 'h ' + m + 'm';
        else uptimeStr = m + 'm';
        var html = '<div class="uptime-row"><span>' + window.renderIcon('uptime') + ' System</span><span class="uptime-pct">' + uptimeStr + '</span></div>';
        if (data.cpu) {
          html += '<div class="uptime-row"><span>' + window.renderIcon('cpu') + ' CPU Load</span><span class="uptime-pct">' + data.cpu.currentLoad.toFixed(1) + '%</span></div>';
        }
        if (data.memory) {
          const memPct = ((data.memory.active / data.memory.total) * 100).toFixed(1);
          html += '<div class="uptime-row"><span>' + window.renderIcon('memory') + ' Memory</span><span class="uptime-pct">' + memPct + '%</span></div>';
        }
        if (data.serverName && data._remote) {
          html += '<div class="uptime-row" style="opacity:0.6;font-size:11px;"><span>📡 ' + data.serverName + '</span></div>';
        }
        container.innerHTML = html;
      }, ${(props.refreshInterval || 30) * 1000});
    `
  },

  'docker-containers': {
    name: 'Docker Containers',
    icon: '🐳',
    category: 'large',
    description: 'Lists Docker containers with status. Supports remote servers via lobsterboard-agent.',
    defaultWidth: 380,
    defaultHeight: 250,
    hasApiKey: false,
    properties: {
      title: 'Containers',
      server: 'local',
      refreshInterval: 10
    },
    preview: `<div style="padding:4px;font-size:11px;">
      <div>🟢 nginx — Up 3d</div>
      <div>🟢 postgres — Up 3d</div>
      <div>🔴 redis — Exited</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('docker')} ${props.title || 'Containers'}</span>
          <span class="dash-card-badge" id="${props.id}-badge">—</span>
        </div>
        <div class="dash-card-body compact-list" id="${props.id}-list">
          <div class="docker-row" style="color:var(--text-muted);justify-content:center;">Loading...</div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Docker Containers Widget: ${props.id} — ${props.server === 'local' ? 'local SSE' : 'remote: ' + props.server}
      onStats('${props.server || 'local'}', function(data) {
        const list = document.getElementById('${props.id}-list');
        const badge = document.getElementById('${props.id}-badge');
        
        // Handle offline state
        if (data._offline) {
          list.innerHTML = '<div class="docker-row" style="color:#f85149;">⚠️ Connection lost</div>';
          badge.textContent = '—';
          return;
        }
        
        // Handle remote docker data structure
        const dockerData = data._remote && data.docker?.containers ? data.docker.containers : data.docker;
        if (!dockerData || dockerData.length === 0) {
          const msg = data._remote && data.docker?.available === false ? 'Docker not available' : 'No containers found';
          list.innerHTML = '<div class="docker-row" style="color:var(--text-muted);">' + msg + '</div>';
          badge.textContent = data._remote && data.docker ? (data.docker.running || 0) + '/' + (data.docker.total || 0) : '0';
          return;
        }
        const containers = dockerData;
        list.innerHTML = containers.map(function(c) {
          const running = c.state === 'running' || c.running === true;
          const icon = running ? '🟢' : '🔴';
          const name = (c.name || '').replace(/^\\//, '');
          return '<div class="docker-row">' + icon + ' ' + name + '<span class="docker-status">' + (c.state || c.status || '—') + '</span></div>';
        }).join('');
        badge.textContent = data._remote && data.docker ? (data.docker.running || 0) + '/' + (data.docker.total || 0) : containers.length;
      }, ${(props.refreshInterval || 10) * 1000});
    `
  },

  'network-speed': {
    name: 'Network Speed',
    icon: '🌐',
    category: 'small',
    description: 'Shows real-time network activity. Supports remote servers via lobsterboard-agent.',
    defaultWidth: 200,
    defaultHeight: 100,
    hasApiKey: false,
    properties: {
      title: 'Network',
      server: 'local',
      refreshInterval: 5
    },
    preview: `<div style="padding:8px;font-size:11px;">
      <div>↓ <span style="color:#3fb950;">45 KB/s</span></div>
      <div>↑ <span style="color:#58a6ff;">12 KB/s</span></div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('network')} ${props.title || 'Network'}</span>
        </div>
        <div class="dash-card-body" style="display:flex;flex-direction:column;align-items:center;justify-content:center;">
          <div class="net-row">↓ <span class="green" id="${props.id}-down">—</span></div>
          <div class="net-row">↑ <span class="blue" id="${props.id}-up">—</span></div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Network Speed Widget: ${props.id} — ${props.server === 'local' ? 'local SSE' : 'remote: ' + props.server}
      function _fmtRate(bytes) {
        if (bytes == null || bytes < 0) return '0 B/s';
        if (bytes < 1024) return bytes.toFixed(0) + ' B/s';
        if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB/s';
        return (bytes / (1024 * 1024)).toFixed(1) + ' MB/s';
      }
      onStats('${props.server || 'local'}', function(data) {
        // Handle offline state
        if (data._offline) {
          document.getElementById('${props.id}-down').textContent = '⚠️';
          document.getElementById('${props.id}-up').textContent = 'offline';
          return;
        }
        
        if (!data.network || data.network.length === 0) return;
        // Handle both local (array) and remote (object) formats
        let rx = 0, tx = 0;
        if (Array.isArray(data.network)) {
          data.network.forEach(function(n) {
            if (n.iface !== 'lo' && n.iface !== 'lo0') {
              rx += (n.rx_sec || 0);
              tx += (n.tx_sec || 0);
            }
          });
        } else {
          rx = data.network.rx_sec || data.network.rxSec || 0;
          tx = data.network.tx_sec || data.network.txSec || 0;
        }
        document.getElementById('${props.id}-down').textContent = _fmtRate(rx);
        document.getElementById('${props.id}-up').textContent = _fmtRate(tx);
      }, ${(props.refreshInterval || 5) * 1000});
    `
  },

  // ─────────────────────────────────────────────
  // PRODUCTIVITY
  // ─────────────────────────────────────────────

  'todo-list': {

    name: 'Todo List',
    icon: '✅',
    category: 'large',
    description: 'Task list with checkboxes. Requires storage backend.',
    defaultWidth: 350,
    defaultHeight: 300,
    hasApiKey: false,
    properties: {
      title: 'Todo'
    },
    preview: `<div style="padding:4px;font-size:11px;">
      <div>☑️ Complete project</div>
      <div>⬜ Review PR</div>
      <div>⬜ Send email</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('todo')} ${props.title || 'Todo'}</span>
          <span class="dash-card-badge" id="${props.id}-badge">0</span>
        </div>
        <div class="dash-card-body" style="display:flex;flex-direction:column;height:100%;overflow:hidden;">
          <div style="display:flex;gap:6px;padding:0 0 8px 0;flex-shrink:0;">
            <input type="text" id="${props.id}-input" placeholder="Add a task..." style="flex:1;background:var(--bg-tertiary);border:1px solid var(--border);border-radius:4px;padding:4px 8px;color:var(--text-primary);font-size:calc(12px * var(--font-scale, 1));">
            <button id="${props.id}-add-btn" style="background:var(--accent-blue);color:#fff;border:none;border-radius:4px;padding:4px 10px;cursor:pointer;font-size:calc(12px * var(--font-scale, 1));">Add</button>
          </div>
          <div id="${props.id}-list" style="flex:1;overflow-y:auto;"></div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Todo List Widget: ${props.id}
      (function() {
        let todos = [];
        const container = document.getElementById('${props.id}-list');
        const input = document.getElementById('${props.id}-input');
        const addBtn = document.getElementById('${props.id}-add-btn');
        const badge = document.getElementById('${props.id}-badge');

        function esc(s) { return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }

        function render() {
          badge.textContent = todos.filter(t => !t.done).length + '/' + todos.length;
          container.innerHTML = todos.map((t, i) =>
            '<div class="todo-item" style="display:flex;align-items:center;gap:6px;padding:3px 0;font-size:calc(13px * var(--font-scale, 1));">' +
              '<input type="checkbox" data-idx="' + i + '"' + (t.done ? ' checked' : '') + '>' +
              '<span style="flex:1;' + (t.done ? 'text-decoration:line-through;opacity:0.5;' : '') + '">' + esc(t.text) + '</span>' +
              '<button data-del="' + i + '" style="background:none;border:none;color:var(--accent-red,#f85149);cursor:pointer;font-size:calc(14px * var(--font-scale, 1));padding:0 4px;">✕</button>' +
            '</div>'
          ).join('');
        }

        function save() {
          fetch('/api/todos', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(todos) });
        }

        container.addEventListener('change', function(e) {
          if (e.target.dataset.idx != null) {
            todos[e.target.dataset.idx].done = e.target.checked;
            save(); render();
          }
        });

        container.addEventListener('click', function(e) {
          if (e.target.dataset.del != null) {
            todos.splice(parseInt(e.target.dataset.del), 1);
            save(); render();
          }
        });

        addBtn.addEventListener('click', function() {
          const text = input.value.trim();
          if (!text) return;
          todos.push({ text: text, done: false });
          input.value = '';
          save(); render();
        });

        input.addEventListener('keydown', function(e) {
          if (e.key === 'Enter') addBtn.click();
        });

        fetch('/api/todos').then(r => r.json()).then(data => {
          todos = Array.isArray(data) ? data : [];
          render();
        }).catch(() => render());
      })();
    `
  },

  'email-count': {
    name: 'Unread Emails',
    icon: '📧',
    category: 'small',
    description: 'Shows unread email count. Requires email API proxy.',
    defaultWidth: 160,
    defaultHeight: 100,
    hasApiKey: true,
    apiKeyName: 'EMAIL_API',
    properties: {
      title: 'Email',
      endpoint: '/api/email/unread',
      refreshInterval: 120
    },
    preview: `<div style="text-align:center;padding:8px;">
      <div style="font-size:28px;color:#f85149;">12</div>
      <div style="font-size:11px;color:#8b949e;">Unread</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('email')} ${props.title || 'Email'}</span>
        </div>
        <div class="dash-card-body" style="display:flex;align-items:center;justify-content:center;gap:10px;">
          <div class="kpi-value red" id="${props.id}-count">—</div>
          <div class="kpi-label">Unread</div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Email Count Widget: ${props.id}
      async function update_${props.id.replace(/-/g, '_')}() {
        try {
          const res = await fetch('${props.endpoint || '/api/email/unread'}');
          const data = await res.json();
          const el = document.getElementById('${props.id}-count');
          el.textContent = data.count || 0;
          el.className = 'kpi-value ' + (data.count > 0 ? 'red' : 'green');
        } catch (e) {
          document.getElementById('${props.id}-count').textContent = '—';
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 300) * 1000});
    `
  },

  'pomodoro': {
    name: 'Pomodoro Timer',
    icon: '🎯',
    category: 'small',
    description: 'Focus timer with configurable work/break intervals. Plays sound when done.',
    defaultWidth: 200,
    defaultHeight: 140,
    hasApiKey: false,
    properties: {
      title: 'Focus',
      workMinutes: 25,
      breakMinutes: 5
    },
    preview: `<div style="text-align:center;padding:8px;">
      <div style="font-size:24px;">25:00</div>
      <div style="font-size:11px;color:#8b949e;">▶️ Start</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('pomodoro')} ${props.title || 'Focus'}</span>
        </div>
        <div class="dash-card-body" style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;">
          <div class="kpi-value" id="${props.id}-time">${props.workMinutes || 25}:00</div>
          <button class="pomo-btn" id="${props.id}-btn" onclick="togglePomo_${props.id.replace(/-/g, '_')}()">▶️ Start</button>
        </div>
      </div>`,
    generateJs: (props) => `
      // Pomodoro Widget: ${props.id}
      let pomoRunning_${props.id.replace(/-/g, '_')} = false;
      let pomoSeconds_${props.id.replace(/-/g, '_')} = ${(props.workMinutes || 25) * 60};
      let pomoInterval_${props.id.replace(/-/g, '_')};
      let pomoIsBreak_${props.id.replace(/-/g, '_')} = false;
      
      // Audio context created on first user interaction
      let pomoAudioCtx_${props.id.replace(/-/g, '_')} = null;
      
      function playPomoSound_${props.id.replace(/-/g, '_')}() {
        try {
          if (!pomoAudioCtx_${props.id.replace(/-/g, '_')}) {
            pomoAudioCtx_${props.id.replace(/-/g, '_')} = new (window.AudioContext || window.webkitAudioContext)();
          }
          const ctx = pomoAudioCtx_${props.id.replace(/-/g, '_')};
          if (ctx.state === 'suspended') ctx.resume();
          
          const now = ctx.currentTime;
          // Schedule 3 beeps
          [0, 0.4, 0.8].forEach((delay, i) => {
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.frequency.value = i === 2 ? 1000 : 800;
            osc.type = 'sine';
            gain.gain.setValueAtTime(0.3, now + delay);
            gain.gain.exponentialRampToValueAtTime(0.01, now + delay + 0.3);
            osc.start(now + delay);
            osc.stop(now + delay + 0.3);
          });
        } catch (e) { console.log('Audio not supported:', e); }
      }
      
      // Initialize audio context on first click
      function initPomoAudio_${props.id.replace(/-/g, '_')}() {
        if (!pomoAudioCtx_${props.id.replace(/-/g, '_')}) {
          pomoAudioCtx_${props.id.replace(/-/g, '_')} = new (window.AudioContext || window.webkitAudioContext)();
        }
      }
      
      function togglePomo_${props.id.replace(/-/g, '_')}() {
        const btn = document.getElementById('${props.id}-btn');
        const timeEl = document.getElementById('${props.id}-time');
        
        // Initialize audio on user interaction
        initPomoAudio_${props.id.replace(/-/g, '_')}();
        
        if (pomoRunning_${props.id.replace(/-/g, '_')}) {
          clearInterval(pomoInterval_${props.id.replace(/-/g, '_')});
          btn.textContent = '▶️ Start';
        } else {
          // If showing Done, reset to work time
          if (timeEl.textContent === 'Done!' || timeEl.textContent === 'Break!') {
            pomoIsBreak_${props.id.replace(/-/g, '_')} = !pomoIsBreak_${props.id.replace(/-/g, '_')};
            pomoSeconds_${props.id.replace(/-/g, '_')} = pomoIsBreak_${props.id.replace(/-/g, '_')} 
              ? ${(props.breakMinutes || 5) * 60} 
              : ${(props.workMinutes || 25) * 60};
          }
          
          pomoInterval_${props.id.replace(/-/g, '_')} = setInterval(() => {
            pomoSeconds_${props.id.replace(/-/g, '_')}--;
            if (pomoSeconds_${props.id.replace(/-/g, '_')} <= 0) {
              clearInterval(pomoInterval_${props.id.replace(/-/g, '_')});
              playPomoSound_${props.id.replace(/-/g, '_')}();
              timeEl.textContent = pomoIsBreak_${props.id.replace(/-/g, '_')} ? 'Done!' : 'Break!';
              btn.textContent = pomoIsBreak_${props.id.replace(/-/g, '_')} ? '🔄 Reset' : '☕ Break';
              pomoRunning_${props.id.replace(/-/g, '_')} = false;
              return;
            }
            const m = Math.floor(pomoSeconds_${props.id.replace(/-/g, '_')} / 60);
            const s = pomoSeconds_${props.id.replace(/-/g, '_')} % 60;
            timeEl.textContent = m + ':' + (s < 10 ? '0' : '') + s;
          }, 1000);
          btn.textContent = '⏸️ Pause';
        }
        pomoRunning_${props.id.replace(/-/g, '_')} = !pomoRunning_${props.id.replace(/-/g, '_')};
      }
    `
  },

  'github-stats': {
    name: 'GitHub Stats',
    icon: '🐙',
    category: 'large',
    description: 'Shows GitHub user/repo stats. Optional token for higher rate limits.',
    defaultWidth: 380,
    defaultHeight: 200,
    hasApiKey: false,
    properties: {
      title: 'GitHub',
      username: 'openclaw',
      repo: 'openclaw',
      apiKey: '',
      refreshInterval: 1800
    },
    preview: `<div style="padding:4px;font-size:11px;">
      <div>⭐ 142 stars · 🍴 23 forks</div>
      <div>🐛 8 open issues</div>
      <div>📅 Last push: 2h ago</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('github')} ${props.title || 'GitHub'}</span>
        </div>
        <div class="dash-card-body" id="${props.id}-stats" style="font-size:calc(13px * var(--font-scale, 1));">
          <div style="color:var(--text-muted);">Loading...</div>
        </div>
      </div>`,
    generateJs: (props) => `
      // GitHub Stats Widget: ${props.id}
      async function update_${props.id.replace(/-/g, '_')}() {
        const owner = '${props.username || 'openclaw'}';
        const repo = '${props.repo || 'openclaw'}';
        const headers = {};
        ${props.apiKey ? `headers['Authorization'] = 'token ${props.apiKey}';` : ''}
        try {
          const [repoRes, prRes] = await Promise.all([
            fetch('https://api.github.com/repos/' + owner + '/' + repo, { headers }),
            fetch('https://api.github.com/repos/' + owner + '/' + repo + '/pulls?state=open&per_page=1', { headers })
          ]);
          if (!repoRes.ok) throw new Error(repoRes.status);
          const d = await repoRes.json();
          // Get open PR count from Link header (total_count) or array length
          let openPRs = '?';
          if (prRes.ok) {
            const link = prRes.headers.get('Link') || '';
            const lastMatch = link.match(/page=(\\d+)>; rel="last"/);
            openPRs = lastMatch ? lastMatch[1] : (await prRes.json()).length;
          }
          function timeAgo(date) {
            const s = Math.floor((Date.now() - new Date(date)) / 1000);
            if (s < 60) return s + 's ago';
            if (s < 3600) return Math.floor(s/60) + 'm ago';
            if (s < 86400) return Math.floor(s/3600) + 'h ago';
            return Math.floor(s/86400) + 'd ago';
          }
          const el = document.getElementById('${props.id}-stats');
          el.innerHTML =
            '<div style="margin-bottom:6px;font-weight:600;color:var(--text-primary);">' + owner + '/' + repo + '</div>' +
            '<div style="display:grid;grid-template-columns:1fr 1fr;gap:4px;">' +
              '<div>⭐ ' + d.stargazers_count.toLocaleString() + ' stars</div>' +
              '<div>🍴 ' + d.forks_count.toLocaleString() + ' forks</div>' +
              '<div>🐛 ' + d.open_issues_count + ' open issues</div>' +
              '<div>🔀 ' + openPRs + ' open PRs</div>' +
            '</div>' +
            '<div style="margin-top:6px;color:var(--text-secondary);font-size:calc(11px * var(--font-scale, 1));">' +
              '📅 Last push: ' + timeAgo(d.pushed_at) +
            '</div>';
        } catch (e) {
          console.error('GitHub stats widget error:', e);
          document.getElementById('${props.id}-stats').innerHTML = '<div style="color:var(--accent-red,#f85149);">Failed to load repo stats</div>';
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 1800) * 1000});
    `
  },

  // ─────────────────────────────────────────────
  // FINANCE
  // ─────────────────────────────────────────────

  'stock-ticker': {
    name: 'Stock Ticker',
    icon: '📈',
    category: 'bar',
    description: 'Scrolling stock ticker with multiple symbols. Free API key required — sign up at finnhub.io/register (60 calls/min free). Enter symbols separated by commas (e.g. AAPL, MSFT, GOOGL).',
    defaultWidth: 1920,
    defaultHeight: 40,
    hasApiKey: true,
    apiKeyName: 'FINNHUB_API_KEY',
    hideApiKeyVar: true,
    properties: {
      title: 'Stocks',
      symbol: 'AAPL, MSFT, GOOGL, AMZN, TSLA',
      apiKey: '',
      apiKeyNote: 'Get a free key at finnhub.io/register',
      refreshInterval: 60
    },
    preview: `<div style="background:#161b22;padding:8px;font-size:11px;overflow:hidden;">
      📈 AAPL $185.42 <span style="color:#3fb950;">+1.2%</span> •• MSFT $420.15 <span style="color:#f85149;">-0.3%</span> •• GOOGL $175.80 <span style="color:#3fb950;">+0.8%</span>
    </div>`,
    generateHtml: (props) => `
      <section class="news-ticker-wrap" id="widget-${props.id}">
        <span class="ticker-label lb-icon" data-icon="stock">📈</span>
        <div class="ticker-track">
          <div class="ticker-content" id="${props.id}-ticker">${props.apiKey ? 'Loading stocks...' : 'Set API key in Edit Mode (Ctrl+E) — free at finnhub.io/register'}</div>
        </div>
      </section>`,
    generateJs: (props) => `
      async function update_${props.id.replace(/-/g, '_')}() {
        const el = document.getElementById('${props.id}-ticker');
        if (!el) return;
        const API_KEY='[REDACTED_API_KEY]''}';
        if (!apiKey) {
          el.innerHTML = 'Set API key in Edit Mode — <a href="https://finnhub.io/register" target="_blank" style="color:#58a6ff;">get free key →</a>';
          return;
        }
        const symbols = '${props.symbol || 'AAPL'}'.split(',').map(s => s.trim()).filter(Boolean);
        try {
          const results = await Promise.all(symbols.map(async (sym) => {
            try {
              const res = await fetch('https://finnhub.io/api/v1/quote?symbol=' + sym + '&token=' + apiKey);
              const data = await res.json();
              if (data.c === 0 && data.h === 0) return '<span class="ticker-link" style="color:#8b949e;">' + sym + ' —</span>';
              const change = ((data.c - data.pc) / data.pc * 100).toFixed(2);
              const color = change >= 0 ? '#3fb950' : '#f85149';
              const arrow = change >= 0 ? '▲' : '▼';
              return '<span class="ticker-link" style="cursor:default;">' +
                '<strong>' + sym + '</strong> $' + data.c.toFixed(2) +
                ' <span style="color:' + color + ';">' + arrow + ' ' + (change >= 0 ? '+' : '') + change + '%</span></span>';
            } catch (_) {
              return '<span class="ticker-link" style="color:#8b949e;">' + sym + ' —</span>';
            }
          }));
          el.innerHTML = results.join('<span class="ticker-sep"> \\u2022\\u2022\\u2022 </span>');
        } catch (e) {
          if (!el.dataset.loaded) el.textContent = 'Failed to load stocks';
        }
        el.dataset.loaded = '1';
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 60) * 1000});
    `
  },

  'crypto-price': {
    name: 'Crypto Price',
    icon: '₿',
    category: 'small',
    description: 'Shows cryptocurrency prices from public APIs.',
    defaultWidth: 200,
    defaultHeight: 130,
    hasApiKey: false,
    properties: {
      title: 'Crypto',
      coin: 'bitcoin',
      currency: 'usd',
      refreshInterval: 60
    },
    preview: `<div style="text-align:center;padding:8px;">
      <div style="font-size:12px;color:#f7931a;">₿ BTC</div>
      <div style="font-size:18px;">$43,521</div>
      <div style="font-size:11px;color:#f85149;">-2.4%</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('crypto')} ${props.coin?.toUpperCase() || 'BTC'}</span>
        </div>
        <div class="dash-card-body" style="display:flex;flex-direction:column;align-items:center;justify-content:center;">
          <div class="kpi-value" id="${props.id}-price" style="position:relative;">
            <span id="${props.id}-price-text">Loading...</span>
            <span id="${props.id}-spinner" style="position:absolute;top:-2px;right:-14px;font-size:10px;opacity:0.5;display:none;">↻</span>
          </div>
          <div class="kpi-label" id="${props.id}-change">&nbsp;</div>
          <div id="${props.id}-stale" style="font-size:9px;color:#d29922;margin-top:2px;display:none;">⚠ stale</div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Crypto Price Widget: ${props.id}
      async function update_${props.id.replace(/-/g, '_')}() {
        const priceText = document.getElementById('${props.id}-price-text');
        const changeEl = document.getElementById('${props.id}-change');
        const spinner = document.getElementById('${props.id}-spinner');
        const staleEl = document.getElementById('${props.id}-stale');
        const hasData = priceText.dataset.loaded;
        if (hasData) spinner.style.display = 'inline';
        try {
          const res = await fetch('https://api.coingecko.com/api/v3/simple/price?ids=${props.coin || 'bitcoin'}&vs_currencies=${props.currency || 'usd'}&include_24hr_change=true');
          const data = await res.json();
          const coin = data['${props.coin || 'bitcoin'}'];
          priceText.textContent = '$' + (coin['${props.currency || 'usd'}'] || 0).toLocaleString();
          priceText.dataset.loaded = '1';
          priceText.style.opacity = '1';
          staleEl.style.display = 'none';
          const change = coin['${props.currency || 'usd'}_24h_change']?.toFixed(2) || 0;
          changeEl.textContent = (change >= 0 ? '+' : '') + change + '%';
          changeEl.className = 'crypto-change ' + (change >= 0 ? 'green' : 'red');
        } catch (e) {
          if (!hasData) priceText.textContent = 'Unavailable';
          priceText.style.opacity = '0.5';
          staleEl.style.display = 'block';
        }
        spinner.style.display = 'none';
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 30) * 1000});
    `
  },

  // ─────────────────────────────────────────────
  // SMART HOME
  // ─────────────────────────────────────────────

  'indoor-climate': {
    name: 'Indoor Climate',
    icon: '🏠',
    category: 'small',
    description: 'Shows indoor temperature/humidity from smart home sensors.',
    defaultWidth: 200,
    defaultHeight: 100,
    hasApiKey: true,
    apiKeyName: 'HOME_API',
    properties: {
      title: 'Indoor',
      endpoint: '/api/home/climate',
      refreshInterval: 60
    },
    preview: `<div style="text-align:center;padding:8px;">
      <div style="font-size:20px;">72°F</div>
      <div style="font-size:11px;color:#8b949e;">💧 45%</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('home')} ${props.title || 'Indoor'}</span>
        </div>
        <div class="dash-card-body" style="display:flex;align-items:center;justify-content:center;gap:10px;">
          <div class="kpi-value" id="${props.id}-temp">—</div>
          <div class="kpi-label" id="${props.id}-humidity">💧 —%</div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Indoor Climate Widget: ${props.id}
      async function update_${props.id.replace(/-/g, '_')}() {
        try {
          const res = await fetch('${props.endpoint || '/api/home/climate'}');
          const data = await res.json();
          document.getElementById('${props.id}-temp').textContent = (data.temp || 72) + '°F';
          document.getElementById('${props.id}-humidity').textContent = '💧 ' + (data.humidity || 50) + '%';
        } catch (e) {
          console.error('Climate error:', e);
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 60) * 1000});
    `
  },

  'camera-feed': {
    name: 'Camera Feed',
    icon: '📷',
    category: 'large',
    description: 'Displays live camera stream from URL.',
    defaultWidth: 400,
    defaultHeight: 300,
    hasApiKey: true,
    apiKeyName: 'CAMERA_URL',
    properties: {
      title: 'Camera',
      streamUrl: 'http://your-camera/stream',
      refreshInterval: 0
    },
    preview: `<div style="background:#000;height:100%;display:flex;align-items:center;justify-content:center;color:#8b949e;font-size:11px;">
      📷 Camera Feed
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('camera')} ${props.title || 'Camera'}</span>
        </div>
        <div class="dash-card-body camera-body">
          <img id="${props.id}-feed" src="${props.streamUrl || ''}" alt="Camera feed" style="width:100%;height:100%;object-fit:cover;">
        </div>
      </div>`,
    generateJs: (props) => `
      // Camera Feed Widget: ${props.id}
      // Set your camera stream URL in the widget properties
      // For MJPEG streams, the img src will auto-update
      // For other formats, you may need additional JS
    `
  },

  'power-usage': {
    name: 'Power Usage',
    icon: '🔌',
    category: 'small',
    description: 'Shows power consumption from smart home integration.',
    defaultWidth: 180,
    defaultHeight: 100,
    hasApiKey: true,
    apiKeyName: 'POWER_API',
    properties: {
      title: 'Power',
      endpoint: '/api/home/power',
      refreshInterval: 10
    },
    preview: `<div style="text-align:center;padding:8px;">
      <div style="font-size:20px;color:#d29922;">1.2kW</div>
      <div style="font-size:11px;color:#8b949e;">Current</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('power')} ${props.title || 'Power'}</span>
        </div>
        <div class="dash-card-body" style="display:flex;align-items:center;justify-content:center;gap:10px;">
          <div class="kpi-value orange" id="${props.id}-watts">—</div>
          <div class="kpi-label">Current</div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Power Usage Widget: ${props.id}
      async function update_${props.id.replace(/-/g, '_')}() {
        try {
          const res = await fetch('${props.endpoint || '/api/home/power'}');
          const data = await res.json();
          const kw = ((data.watts || 0) / 1000).toFixed(1);
          document.getElementById('${props.id}-watts').textContent = kw + 'kW';
        } catch (e) {
          console.error('Power error:', e);
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 10) * 1000});
    `
  },

  // ─────────────────────────────────────────────
  // ENTERTAINMENT
  // ─────────────────────────────────────────────

  'now-playing': {
    name: 'Now Playing',
    icon: '🎵',
    category: 'large',
    description: 'Shows currently playing music from Spotify/music service API.',
    defaultWidth: 350,
    defaultHeight: 120,
    hasApiKey: true,
    apiKeyName: 'SPOTIFY_TOKEN',
    properties: {
      title: 'Now Playing',
      endpoint: '/api/spotify/now-playing',
      refreshInterval: 10
    },
    preview: `<div style="display:flex;gap:12px;padding:8px;align-items:center;">
      <div style="width:50px;height:50px;background:#282828;border-radius:4px;"></div>
      <div style="font-size:11px;">
        <div style="color:#fff;">Song Title</div>
        <div style="color:#8b949e;">Artist Name</div>
      </div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('music')} ${props.title || 'Now Playing'}</span>
        </div>
        <div class="dash-card-body" style="display:flex;align-items:center;gap:12px;">
          <div class="np-art" id="${props.id}-art"></div>
          <div class="np-info">
            <div class="np-title" id="${props.id}-title">Not Playing</div>
            <div class="np-artist" id="${props.id}-artist">—</div>
          </div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Now Playing Widget: ${props.id}
      async function update_${props.id.replace(/-/g, '_')}() {
        try {
          const res = await fetch('${props.endpoint || '/api/spotify/now-playing'}');
          const data = await res.json();
          if (data.is_playing) {
            document.getElementById('${props.id}-title').textContent = data.item?.name || 'Unknown';
            document.getElementById('${props.id}-artist').textContent = data.item?.artists?.map(a => a.name).join(', ') || '';
            if (data.item?.album?.images?.[0]?.url) {
              document.getElementById('${props.id}-art').style.backgroundImage = 'url(' + data.item.album.images[0].url + ')';
            }
          }
        } catch (e) {
          console.error('Spotify error:', e);
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 10) * 1000});
    `
  },

  // ─────────────────────────────────────────────
  // MISCELLANEOUS
  // ─────────────────────────────────────────────

  'quote-of-day': {
    name: 'Quote of Day',
    icon: '💭',
    category: 'large',
    description: 'Displays daily inspirational quote from public API.',
    defaultWidth: 400,
    defaultHeight: 150,
    hasApiKey: false,
    properties: {
      title: 'Quote',
      maxLength: 0,
      refreshInterval: 3600
    },
    preview: `<div style="padding:8px;font-size:12px;font-style:italic;">
      "The only way to do great work is to love what you do."
      <div style="font-size:11px;color:#8b949e;margin-top:4px;">— Steve Jobs</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('quote')} ${props.title || 'Quote'}</span>
        </div>
        <div class="dash-card-body" style="display:flex;flex-direction:column;justify-content:center;">
          <div class="quote-text" id="${props.id}-text" style="font-style:italic;">Loading quote...</div>
          <div class="quote-author" id="${props.id}-author" style="margin-top:8px;color:var(--text-muted);font-size:calc(11px * var(--font-scale, 1));">—</div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Quote of Day Widget: ${props.id}
      async function update_${props.id.replace(/-/g, '_')}() {
        const maxLen = ${props.maxLength || 0};
        const maxRetries = maxLen > 0 ? 5 : 1;
        try {
          for (let i = 0; i < maxRetries; i++) {
            const res = await fetch('/api/quote');
            const data = await res.json();
            const quote = data[0];
            if (!maxLen || quote.q.length <= maxLen) {
              document.getElementById('${props.id}-text').textContent = '\\u201c' + quote.q + '\\u201d';
              document.getElementById('${props.id}-author').textContent = '— ' + quote.a;
              return;
            }
          }
          // All retries exceeded maxLength, use last one anyway
          const res = await fetch('/api/quote');
          const data = await res.json();
          document.getElementById('${props.id}-text').textContent = '\\u201c' + data[0].q + '\\u201d';
          document.getElementById('${props.id}-author').textContent = '— ' + data[0].a;
        } catch (e) {
          document.getElementById('${props.id}-text').textContent = '\\u201cStay hungry, stay foolish.\\u201d';
          document.getElementById('${props.id}-author').textContent = '— Steve Jobs';
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 3600) * 1000});
    `
  },

  'countdown': {
    name: 'Countdown',
    icon: '⏳',
    category: 'small',
    description: 'Counts down days (and optionally hours/minutes) to a target date.',
    defaultWidth: 220,
    defaultHeight: 120,
    hasApiKey: false,
    properties: {
      title: 'Countdown',
      targetDate: '2025-12-31',
      showHours: false,
      showMinutes: false
    },
    preview: `<div style="text-align:center;padding:8px;">
      <div style="font-size:11px;color:#8b949e;">Event Name</div>
      <div style="font-size:20px;">42 days</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('countdown')} ${props.title || 'Countdown'}</span>
        </div>
        <div class="dash-card-body" style="display:flex;flex-direction:column;align-items:center;justify-content:center;">
          <div class="kpi-value" id="${props.id}-countdown">—</div>
          <div class="kpi-label" id="${props.id}-date">${props.targetDate || ''}</div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Countdown Widget: ${props.id}
      function update_${props.id.replace(/-/g, '_')}() {
        const target = new Date('${props.targetDate || '2025-12-31'}T00:00:00');
        const now = new Date();
        const diff = target - now;
        const el = document.getElementById('${props.id}-countdown');
        
        if (diff <= 0) {
          el.textContent = 'Today!';
          return;
        }
        
        const days = Math.floor(diff / (1000 * 60 * 60 * 24));
        const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
        
        let parts = [];
        parts.push(days + 'd');
        ${props.showHours ? "parts.push(hours + 'h');" : ''}
        ${props.showMinutes ? "parts.push(minutes + 'm');" : ''}
        
        el.textContent = parts.join(' ');
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${props.showMinutes ? '1000' : '60000'});
    `
  },

  'image-local': {
    name: 'Image',
    icon: '🖼️',
    category: 'large',
    description: 'Displays a local image file. Embedded as base64 for portable exports.',
    defaultWidth: 300,
    defaultHeight: 220,
    hasApiKey: false,
    properties: {
      title: 'Image',
      imagePath: ''
    },
    preview: `<div style="background:#21262d;height:100%;display:flex;align-items:center;justify-content:center;color:#8b949e;font-size:11px;">
      🖼️ Local Image
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('image')} ${props.title || 'Image'}</span>
        </div>
        <div class="dash-card-body" style="padding:0;overflow:hidden;display:flex;align-items:center;justify-content:center;background:var(--bg-tertiary);">
          ${props.imagePath 
            ? `<img src="${props.imagePath}" style="width:100%;height:100%;object-fit:contain;">`
            : `<span style="color:var(--text-muted);font-size:calc(12px * var(--font-scale, 1));">${renderIcon('image')} No image path</span>`
          }
        </div>
      </div>`,
    generateJs: (props) => `
      // Local Image Widget: ${props.id}
      // Static image - no JS needed
    `
  },

  'image-random': {
    name: 'Random Image',
    icon: '🎲',
    category: 'large',
    description: 'Rotates through multiple images. Pick files to add to rotation.',
    defaultWidth: 300,
    defaultHeight: 220,
    hasApiKey: false,
    properties: {
      title: 'Random Image',
      images: [],
      refreshInterval: 30
    },
    preview: `<div style="background:#21262d;height:100%;display:flex;align-items:center;justify-content:center;color:#8b949e;font-size:11px;">
      🎲 Random Image
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('image-random')} ${props.title || 'Random Image'}</span>
        </div>
        <div class="dash-card-body" style="padding:0;overflow:hidden;display:flex;align-items:center;justify-content:center;background:var(--bg-tertiary);">
          <img id="${props.id}-img" src="" style="width:100%;height:100%;object-fit:contain;display:none;">
          <span id="${props.id}-placeholder" style="color:var(--text-muted);font-size:calc(12px * var(--font-scale, 1));">${renderIcon('image-random')} No images added</span>
        </div>
      </div>`,
    generateJs: (props) => {
      const images = (props.images || []).map(img => img.data);
      return `
      // Random Image Widget: ${props.id}
      (function() {
        const images = ${JSON.stringify(images)};
        
        const imgEl = document.getElementById('${props.id}-img');
        const placeholder = document.getElementById('${props.id}-placeholder');
        
        function showRandomImage() {
          if (images.length === 0) return;
          const randomIndex = Math.floor(Math.random() * images.length);
          imgEl.src = images[randomIndex];
          imgEl.style.display = 'block';
          placeholder.style.display = 'none';
        }
        
        if (images.length > 0) {
          showRandomImage();
          setInterval(showRandomImage, ${(props.refreshInterval || 30) * 1000});
        }
      })();
    `;
    }
  },

  'image-latest': {
    name: 'Latest Image',
    icon: '🆕',
    category: 'large',
    description: 'Shows the newest image from a directory. Auto-refreshes.',
    defaultWidth: 300,
    defaultHeight: 220,
    hasApiKey: false,
    properties: {
      title: 'Latest Image',
      directoryPath: '',
      refreshInterval: 60
    },
    preview: `<div style="background:#21262d;height:100%;display:flex;align-items:center;justify-content:center;color:#8b949e;font-size:11px;">
      🆕 Latest Image
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('image-new')} ${props.title || 'Latest Image'}</span>
          <span id="${props.id}-filename" style="font-size:11px;color:var(--text-muted);margin-left:auto;"></span>
        </div>
        <div class="dash-card-body" style="padding:0;overflow:hidden;display:flex;align-items:center;justify-content:center;background:var(--bg-tertiary);">
          <img id="${props.id}-img" src="" style="width:100%;height:100%;object-fit:contain;display:none;">
          <span id="${props.id}-placeholder" style="color:var(--text-muted);font-size:12px;">${renderIcon('image-new')} ${props.directoryPath ? 'Loading...' : 'No directory set'}</span>
        </div>
      </div>`,
    generateJs: (props) => `
      // Latest Image Widget: ${props.id}
      (function() {
        const dir = ${JSON.stringify(props.directoryPath || '')};
        const imgEl = document.getElementById('${props.id}-img');
        const placeholder = document.getElementById('${props.id}-placeholder');
        const filenameEl = document.getElementById('${props.id}-filename');
        
        async function loadLatest() {
          if (!dir) return;
          try {
            const res = await fetch('/api/latest-image?dir=' + encodeURIComponent(dir));
            const data = await res.json();
            if (data.status === 'ok' && data.image) {
              imgEl.src = data.image.dataUrl;
              imgEl.style.display = 'block';
              placeholder.style.display = 'none';
              if (filenameEl) filenameEl.textContent = data.image.name;
            } else {
              placeholder.textContent = data.message || 'No images found';
            }
          } catch (e) {
            placeholder.textContent = 'Error loading image';
          }
        }
        
        loadLatest();
        setInterval(loadLatest, ${(props.refreshInterval || 60) * 1000});
      })();
    `
  },

  'image-embed': {
    name: 'Web Image',
    icon: '🌐',
    category: 'large',
    description: 'Displays an image from a web URL.',
    defaultWidth: 300,
    defaultHeight: 220,
    hasApiKey: false,
    properties: {
      title: 'Image',
      imageUrl: ''
    },
    preview: `<div style="background:#21262d;height:100%;display:flex;align-items:center;justify-content:center;color:#8b949e;font-size:11px;">
      🌐 Web Image
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('embed')} ${props.title || 'Image'}</span>
        </div>
        <div class="dash-card-body" style="padding:0;overflow:hidden;display:flex;align-items:center;justify-content:center;background:var(--bg-tertiary);">
          ${props.imageUrl 
            ? `<img src="${props.imageUrl}" style="width:100%;height:100%;object-fit:contain;">`
            : `<span style="color:var(--text-muted);font-size:calc(12px * var(--font-scale, 1));">${renderIcon('embed')} No image URL</span>`
          }
        </div>
      </div>`,
    generateJs: (props) => `
      // Web Image Widget: ${props.id}
      // Static image - no JS needed
    `
  },

  'quick-links': {
    name: 'Quick Links',
    icon: '🔗',
    category: 'large',
    description: 'Grid of clickable links with auto-fetched favicons.',
    defaultWidth: 300,
    defaultHeight: 200,
    hasApiKey: false,
    properties: {
      title: 'Quick Links',
      columns: 1,
      links: []
    },
    preview: `<div style="padding:4px;font-size:11px;">
      <div style="padding:4px 0;">🔗 Google</div>
      <div style="padding:4px 0;">🔗 GitHub</div>
      <div style="padding:4px 0;">🔗 Reddit</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('links')} ${props.title || 'Quick Links'}</span>
        </div>
        <div class="dash-card-body links-list" id="${props.id}-links">
          ${(props.links || []).length === 0 ? '<span style="color:var(--text-muted);font-size:calc(12px * var(--font-scale, 1));">No links added</span>' : ''}
        </div>
      </div>`,
    generateJs: (props) => {
      const links = props.links || [];
      return `
      // Quick Links Widget: ${props.id}
      (function() {
        const links = ${JSON.stringify(links)};
        const container = document.getElementById('${props.id}-links');
        
        if (links.length === 0) {
          container.innerHTML = '<span style="color:var(--text-muted);font-size:calc(12px * var(--font-scale, 1));">No links added</span>';
          return;
        }
        
        const cols = ${props.columns || 1};
        container.style.display = 'grid';
        container.style.gridTemplateColumns = 'repeat(' + cols + ', 1fr)';
        container.style.gap = '4px';
        container.innerHTML = links.filter(link => _isSafeUrl(link.url)).map(link => {
          const domain = new URL(link.url).hostname;
          const favicon = 'https://www.google.com/s2/favicons?sz=32&domain=' + _esc(domain);
          return '<a href="' + _esc(link.url) + '" class="quick-link" target="_blank" rel="noopener noreferrer" style="display:flex;align-items:center;gap:8px;padding:6px 4px;text-decoration:none;color:var(--text-primary);border-bottom:1px solid var(--border);overflow:hidden;">' +
            '<img src="' + favicon + '" style="width:16px;height:16px;flex-shrink:0;" onerror="this.style.display=\\'none\\'">' +
            '<span style="overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">' + _esc(link.name) + '</span>' +
          '</a>';
        }).join('');
      })();
    `;
    }
  },

  'iframe-embed': {
    name: 'Iframe Embed',
    icon: '🌐',
    category: 'large',
    description: 'Embeds any webpage in an iframe. Some sites may block embedding.',
    defaultWidth: 500,
    defaultHeight: 350,
    hasApiKey: false,
    properties: {
      title: 'Embed',
      embedUrl: 'https://example.com',
      allowFullscreen: true
    },
    preview: `<div style="background:#21262d;height:100%;display:flex;align-items:center;justify-content:center;color:#8b949e;font-size:11px;">
      🌐 Embedded Content
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('embed')} ${props.title || 'Embed'}</span>
        </div>
        <div class="dash-card-body" style="padding:0;overflow:hidden;">
          <iframe src="${_isSafeUrl(props.embedUrl) ? props.embedUrl : 'about:blank'}" style="width:100%;height:100%;border:none;" ${props.allowFullscreen ? 'allowfullscreen' : ''}></iframe>
        </div>
      </div>`,
    generateJs: (props) => `
      // Iframe Embed Widget: ${props.id}
      // Configure the embed URL in widget properties
    `
  },

  'rss-ticker': {
    name: 'RSS Ticker',
    icon: '📡',
    category: 'bar',
    description: 'Scrolling RSS feed headlines. Add any RSS feed URL.',
    defaultWidth: 1920,
    defaultHeight: 40,
    hasApiKey: false,
    properties: {
      title: 'RSS',
      feedUrl: 'https://example.com/feed.xml',
      maxItems: 10,
      refreshInterval: 600
    },
    preview: `<div style="background:#161b22;padding:8px;font-size:11px;overflow:hidden;">
      📡 Latest headlines scrolling by...
    </div>`,
    generateHtml: (props) => `
      <section class="news-ticker-wrap" id="widget-${props.id}">
        <span class="ticker-label lb-icon" data-icon="rss">📡</span>
        <div class="ticker-track">
          <div class="ticker-content" id="${props.id}-ticker">Loading feed...</div>
        </div>
      </section>`,
    generateJs: (props) => `
      async function update_${props.id.replace(/-/g, '_')}() {
        var el = document.getElementById('${props.id}-ticker');
        if (!el) el = document.querySelector('.ticker-content');
        if (!el) return;
        try {
          var feedUrl = '${props.feedUrl || ''}';
          if (!feedUrl || feedUrl === 'https://example.com/feed.xml') {
            el.textContent = 'Set a Feed URL in Edit Mode (Ctrl+E)';
            return;
          }
          var res = await fetch('/api/rss?url=' + encodeURIComponent(feedUrl));
          if (!res.ok) { el.textContent = 'Feed error: ' + res.status; return; }
          var xml = await res.text();
          var parser = new DOMParser();
          var doc = parser.parseFromString(xml, 'text/xml');
          var items = Array.from(doc.querySelectorAll('item')).slice(0, ${props.maxItems || 10});
          if (!items.length) { el.textContent = 'No items found in feed'; return; }
          el.innerHTML = items.map(function(item) {
            var title = (item.querySelector('title') ? item.querySelector('title').textContent : '').replace(/</g,'&lt;');
            var link = item.querySelector('link') ? item.querySelector('link').textContent : '#';
            return '<a href="' + link + '" target="_blank" class="ticker-link">' + title + '</a>';
          }).join('<span class="ticker-sep"> \\u2022\\u2022\\u2022 </span>');
        } catch (e) {
          if (el) el.textContent = 'Failed to load feed';
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 600) * 1000});
    `
  },

  'world-clock': {
    name: 'World Clock',
    icon: '🌍',
    category: 'large',
    description: 'Shows current time in multiple cities side-by-side.',
    defaultWidth: 300,
    defaultHeight: 180,
    hasApiKey: false,
    properties: {
      title: 'World Clock',
      locations: 'New York; London; Tokyo',
      format24h: false,
      refreshInterval: 60
    },
    preview: `<div style="padding:4px;font-size:11px;">
      <div>🕐 New York: 5:30 PM</div>
      <div>🕐 London: 10:30 PM</div>
      <div>🕐 Tokyo: 7:30 AM</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('world-clock')} ${props.title || 'World Clock'}</span>
        </div>
        <div class="dash-card-body" id="${props.id}-clocks">
          <div style="color:#8b949e;font-size:calc(12px * var(--font-scale, 1));">Loading times...</div>
        </div>
      </div>`,
    generateJs: (props) => `
      // World Clock Widget: ${props.id} (pure Intl.DateTimeFormat - no API needed)
      const CITY_TZ_MAP = {
        'New York': 'America/New_York', 'Los Angeles': 'America/Los_Angeles', 'Chicago': 'America/Chicago',
        'London': 'Europe/London', 'Paris': 'Europe/Paris', 'Berlin': 'Europe/Berlin',
        'Tokyo': 'Asia/Tokyo', 'Sydney': 'Australia/Sydney', 'Dubai': 'Asia/Dubai',
        'Singapore': 'Asia/Singapore', 'Hong Kong': 'Asia/Hong_Kong', 'Mumbai': 'Asia/Kolkata',
        'Shanghai': 'Asia/Shanghai', 'Seoul': 'Asia/Seoul', 'Moscow': 'Europe/Moscow',
        'Istanbul': 'Europe/Istanbul', 'Bangkok': 'Asia/Bangkok', 'Toronto': 'America/Toronto',
        'Heidenheim': 'Europe/Berlin', 'Vienna': 'Europe/Vienna', 'Zurich': 'Europe/Zurich',
        'Amsterdam': 'Europe/Amsterdam', 'Rome': 'Europe/Rome', 'Madrid': 'Europe/Madrid',
        'São Paulo': 'America/Sao_Paulo', 'Mexico City': 'America/Mexico_City',
        'Graz': 'Europe/Vienna', 'Munich': 'Europe/Berlin', 'Frankfurt': 'Europe/Berlin',
        'Santiago': 'America/Santiago', 'Lima': 'America/Lima'
      };
      const locs_${props.id.replace(/-/g, '_')} = '${props.locations || 'New York; London; Tokyo'}'.split(';').map(s => s.trim());
      const hour12_${props.id.replace(/-/g, '_')} = ${!props.format24h};
      
      function update_${props.id.replace(/-/g, '_')}() {
        const container = document.getElementById('${props.id}-clocks');
        const now = new Date();
        const results = locs_${props.id.replace(/-/g, '_')}.map(loc => {
          const tz = CITY_TZ_MAP[loc] || CITY_TZ_MAP[Object.keys(CITY_TZ_MAP).find(k => k.toLowerCase() === loc.toLowerCase())] || null;
          if (!tz) return { city: loc, time: '(unknown tz)' };
          try {
            const fmt = new Intl.DateTimeFormat('en-GB', { timeZone: tz, hour: '2-digit', minute: '2-digit', hour12: hour12_${props.id.replace(/-/g, '_')} });
            return { city: loc, time: fmt.format(now) };
          } catch(e) { return { city: loc, time: '—' }; }
        });
        container.innerHTML = results.map(r => 
          '<div class="tz-row"><span class="tz-city">' + r.city + '</span><span class="tz-time">' + r.time + '</span></div>'
        ).join('');
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 60) * 1000});
    `
  },

  'pages-menu': {
    name: 'Pages Menu',
    icon: '📑',
    category: 'small',
    description: 'Navigation links to all discovered LobsterBoard pages. Supports vertical or horizontal layout.',
    defaultWidth: 220,
    defaultHeight: 200,
    hasApiKey: false,
    properties: {
      title: 'Pages',
      layout: 'vertical',
      showBorder: true,
      refreshInterval: 60
    },
    preview: `<div style="padding:6px;font-size:11px;color:#8b949e;">
      <div>📝 Notes</div>
      <div>📋 Board</div>
      <div>📅 Calendar</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('pages')} ${props.title || 'Pages'}</span>
        </div>
        <div class="dash-card-body pages-menu ${props.layout === 'horizontal' ? 'pages-menu-horizontal' : 'pages-menu-vertical'}" id="${props.id}-list">
          <span class="pages-menu-item">Loading…</span>
        </div>
      </div>
      <style>
        .pages-menu-vertical { display:flex; flex-direction:column; gap:4px; overflow-y:auto; }
        .pages-menu-horizontal { display:flex; flex-direction:row; flex-wrap:wrap; gap:6px; align-items:center; }
        .pages-menu-item {
          display:inline-flex; align-items:center; gap:6px;
          padding:6px 10px; border-radius:6px;
          background:#21262d; color:#c9d1d9;
          text-decoration:none; font-size:calc(13px * var(--font-scale, 1));
          transition: background .15s, color .15s;
        }
        .pages-menu-item:hover { background:#30363d; color:#58a6ff; }
        .pages-menu-item .pages-menu-icon { font-size:calc(15px * var(--font-scale, 1)); }
      </style>`,
    generateJs: (props) => `
      async function update_${props.id.replace(/-/g, '_')}() {
        try {
          const res = await fetch('/api/pages');
          const pages = await res.json();
          const list = document.getElementById('${props.id}-list');
          if (!pages.length) { list.innerHTML = '<span class="pages-menu-item">No pages found</span>'; return; }
          list.innerHTML = pages.map(p =>
            '<a class="pages-menu-item" href="/pages/' + p.id + '" title="' + (p.description || p.title || p.name || '') + '">' +
            '<span class="pages-menu-icon">' + (p.icon || '📄') + '</span>' +
            '<span>' + (p.title || p.name || p.id) + '</span></a>'
          ).join('');
        } catch (e) {
          console.error('Pages menu widget error:', e);
          document.getElementById('${props.id}-list').innerHTML = '<span class="pages-menu-item">Error loading pages</span>';
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 60) * 1000});
    `
  },

  'claude-usage': {
    name: 'Claude Usage',
    icon: '🤖',
    category: 'large',
    description: 'Real-time Claude Code subscription usage (5h session, 7d weekly, Opus, Sonnet limits). Reads credentials from ~/.claude.',
    defaultWidth: 380,
    defaultHeight: 260,
    hasApiKey: false,
    properties: {
      title: 'Claude Usage',
      refreshInterval: 120
    },
    preview: `<div style="padding:8px;font-size:11px;">
      <div style="margin-bottom:6px;"><b>5h Session</b> <span style="color:#3fb950;">28%</span></div>
      <div style="margin-bottom:6px;"><b>7d Weekly</b> <span style="color:#d29922;">31%</span></div>
      <div><b>Sonnet</b> <span style="color:#3fb950;">0%</span></div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">${renderIcon('claude-usage')} ${props.title || 'Claude Usage'}</span>
          <span id="${props.id}-sub" style="font-size:calc(10px * var(--font-scale,1));color:#8b949e;margin-left:auto;"></span>
        </div>
        <div class="dash-card-body" id="${props.id}-body" style="padding:8px 12px;overflow-y:auto;">
          <div style="color:#8b949e;text-align:center;">Loading...</div>
        </div>
      </div>`,
    generateJs: (props) => `
      function barColor_${props.id.replace(/-/g, '_')}(pct) {
        if (pct >= 80) return '#f85149';
        if (pct >= 50) return '#d29922';
        return '#3fb950';
      }
      function timeLeft_${props.id.replace(/-/g, '_')}(iso) {
        if (!iso) return '';
        const ms = new Date(iso) - Date.now();
        if (ms <= 0) return 'now';
        const h = Math.floor(ms / 3600000);
        const m = Math.floor((ms % 3600000) / 60000);
        return h > 0 ? h + 'h ' + m + 'm' : m + 'm';
      }
      function usageBar_${props.id.replace(/-/g, '_')}(label, pct, resetIso) {
        const p = Math.min(100, Math.max(0, pct || 0));
        const c = barColor_${props.id.replace(/-/g, '_')}(p);
        const reset = resetIso ? '<span style="color:#8b949e;font-size:calc(10px * var(--font-scale,1));">resets ' + timeLeft_${props.id.replace(/-/g, '_')}(resetIso) + '</span>' : '';
        return '<div style="margin-bottom:10px;">' +
          '<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:3px;">' +
            '<span style="font-weight:600;font-size:calc(12px * var(--font-scale,1));">' + label + '</span>' +
            '<span style="font-size:calc(13px * var(--font-scale,1));font-weight:700;color:' + c + ';">' + p.toFixed(0) + '%</span>' +
          '</div>' +
          '<div style="background:#21262d;border-radius:4px;height:8px;overflow:hidden;">' +
            '<div style="width:' + p + '%;height:100%;background:' + c + ';border-radius:4px;transition:width .5s;"></div>' +
          '</div>' +
          (reset ? '<div style="text-align:right;margin-top:2px;">' + reset + '</div>' : '') +
        '</div>';
      }
      async function update_${props.id.replace(/-/g, '_')}() {
        const body = document.getElementById('${props.id}-body');
        const subEl = document.getElementById('${props.id}-sub');
        try {
          const res = await fetch('/api/pages/claude-usage/usage');
          const d = await res.json();
          if (d.error) { body.innerHTML = '<div style="color:#f85149;">' + d.error + '</div>'; return; }
          if (subEl) {
            const labels = { max: 'Max (5×)', pro: 'Pro', free: 'Free' };
            subEl.textContent = labels[d.subscription] || d.subscription || '';
          }
          let html = '';
          if (d.five_hour) html += usageBar_${props.id.replace(/-/g, '_')}('5h Session', d.five_hour.utilization, d.five_hour.resets_at);
          if (d.seven_day) html += usageBar_${props.id.replace(/-/g, '_')}('7d Weekly', d.seven_day.utilization, d.seven_day.resets_at);
          if (d.seven_day_opus) html += usageBar_${props.id.replace(/-/g, '_')}('Opus (7d)', d.seven_day_opus.utilization, d.seven_day_opus.resets_at);
          if (d.seven_day_sonnet && d.seven_day_sonnet.utilization > 0) html += usageBar_${props.id.replace(/-/g, '_')}('Sonnet (7d)', d.seven_day_sonnet.utilization, d.seven_day_sonnet.resets_at);
          if (d.extra_usage && d.extra_usage.is_enabled) {
            const used = (d.extra_usage.used_credits / 100).toFixed(2);
            const limit = d.extra_usage.monthly_limit > 0 ? (d.extra_usage.monthly_limit / 100).toFixed(2) : '∞';
            html += '<div style="margin-top:4px;padding-top:6px;border-top:1px solid #30363d;">' +
              '<div style="display:flex;justify-content:space-between;font-size:calc(11px * var(--font-scale,1));">' +
                '<span style="color:#8b949e;">Extra Usage</span>' +
                '<span style="font-weight:600;">$' + used + ' / $' + limit + '</span>' +
              '</div></div>';
          }
          if (!html) html = '<div style="color:#8b949e;">No usage data</div>';
          body.innerHTML = html;
        } catch (e) {
          console.error('Claude usage widget error:', e);
          body.innerHTML = '<div style="color:#f85149;">Failed to load</div>';
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 120) * 1000});
    `
  },

};

// Export for use in builder
if (typeof module !== 'undefined' && module.exports) {
  module.exports = WIDGETS;
}
```

## File: `memory/2026-03-05.md`
```markdown
# 2026-03-05 — CackalackyCon MUD Build Session

## Project: CackalackyCon 2026 MUD (GoMud)
Building a hacker con-themed starting zone for GoMud. Players start at the con, collect 4 key fragments, then portal to existing Frostfang fantasy world (800+ rooms).

### Key Decisions
- **Limes are THE motif** — 2025 badge was lime-themed, major inside joke. Integrated throughout (Lime of Learning tutorial, lime décor, lime cipher puzzle)
- **Badges = armor** — neck slot, 4 tiers: Basic (free from Base16) → Upgraded (75g) → Hardened (200g) → Legendary Lime
- **Enemy theme** — corrupted badges (2026 badges pass "viruses"), purple/magenta portal spawns vs lime green for friendlies
- **Portal gate** — must collect 4 fragments from different zones before activating The Old Server (dusty 486 from 1994)
- **Economy loop** — kill enemies → loot → sell to Kiwi → buy upgrades from Nutcrunch

### Built Today
- 26+ con rooms (all villages, social areas, hallways)
- 11 enemy mobs (Script Kiddie lvl 2 → The Fed lvl 10)
- 2 merchant NPCs (Kiwi = bar/loot buyer, Nutcrunch = badge upgrades)
- Consumables: Monster Energy, Club Mate, hotel coffee, jello shots, repair kits
- 4-fragment quest system with puzzle scripts:
  - Cipher Room: `solve lime` (ROT13 puzzle)
  - Hardware Hacking: trade circuit board to s0lray
  - SAV Lounge: `say open sesame` social puzzle
  - CTF Arena: kill script kiddie, ask Uncue

### Technical Lessons
- **GoMud filename must match mob name** inside YAML exactly
- **Clear `rooms.instances/` cache** after any room file changes
- **`login` is reserved** — don't use in NPC scripts
- **YAML escaping** — colons, quotes, special chars in strings need proper escaping (caused multiple parse errors)
- **Secret exits** — use `search` skill or interaction scripts to reveal

### Blockers
- YAML parse errors in 2050.yaml (Service Hallway) and 2051.yaml (Server Room) — need fixing
- Player guide spawn message ("shower of sparks") requires Go rebuild

### File Locations
- Server: `/Users/richardcurry/clawd/GoMud/` (`./gomud` runs on ports 33333/80/9999)
- Rooms: `_datafiles/world/default/rooms/cackalackycon/`
- Item IDs: Badges 25001-25004, Consumables 35001-35011, Loot 5001-5007, Fragments 5100-5103
- Mob IDs: NPCs 100-108, Enemies 200-213

### Next Steps
1. Fix YAML errors in 2050/2051 room files
2. Test full player flow: tutorial → badge → fragments → portal → Frostfang
3. Balance enemy difficulty and loot drops
```

## File: `pages/README.md`
```markdown
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

## File: `pages/claude-usage/api.cjs`
```
const os = require('os');
const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const CREDENTIALS_PATH = path.join(process.env.HOME || os.homedir(), '.claude', '.credentials.json');
const CACHE_TTL_MS = 120_000; // 2 minutes — Anthropic rate limits are strict

// In-memory cache: survives across requests, resets on server restart
let _cache = { data: null, ts: 0, error: null, errorTs: 0 };

function readCredentials() {
  return JSON.parse(fs.readFileSync(CREDENTIALS_PATH, 'utf-8'));
}

function isTokenExpired(creds) {
  return Date.now() > (creds.claudeAiOauth?.expiresAt || 0);
}

function refreshToken() {
  try {
    execSync('echo "hi" | claude -p "hi" 2>/dev/null', {
      timeout: 45000,
      encoding: 'utf-8',
      env: { ...process.env, HOME: process.env.HOME || os.homedir() }
    });
  } catch (_) {}
}

async function fetchUsageFresh() {
  let creds = readCredentials();

  if (isTokenExpired(creds)) {
    refreshToken();
    creds = readCredentials();
    if (isTokenExpired(creds)) {
      return { error: 'Token expired and refresh failed' };
    }
  }

  const token = creds.claudeAiOauth.accessToken;
  const tier = creds.claudeAiOauth.rateLimitTier || 'unknown';
  const sub = creds.claudeAiOauth.subscriptionType || 'unknown';

  const resp = await fetch('https://api.anthropic.com/api/oauth/usage', {
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json',
      'User-Agent': 'claude-code/2.1.42',
      'anthropic-beta': 'oauth-2025-04-20'
    }
  });

  if (resp.status === 429) {
    // Rate limited — return stale cache if available, otherwise error
    if (_cache.data) {
      return { ..._cache.data, cached: true, stale: true };
    }
    return { error: 'Rate limited (429). Try again in a few minutes.' };
  }

  if (!resp.ok) {
    return { error: `API returned ${resp.status}` };
  }

  const data = await resp.json();
  return { subscription: sub, tier, ...data };
}

async function fetchUsageCached() {
  const now = Date.now();

  // Return cached data if fresh
  if (_cache.data && (now - _cache.ts) < CACHE_TTL_MS) {
    return { ..._cache.data, cached: true };
  }

  // Fetch fresh
  const result = await fetchUsageFresh();

  // Cache successful results
  if (!result.error) {
    _cache.data = result;
    _cache.ts = now;
    _cache.error = null;
  } else if (result.error.includes('429') || result.error.includes('rate')) {
    // On rate limit, return stale cache if available
    if (_cache.data) {
      return { ..._cache.data, cached: true, stale: true };
    }
    // Cache the error briefly (30s) to avoid hammering
    _cache.error = result;
    _cache.errorTs = now;
  }

  return result;
}

module.exports = function(ctx) {
  return {
    routes: {
      'GET /usage': async (req, res) => {
        return await fetchUsageCached();
      }
    }
  };
};
```

## File: `pages/claude-usage/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LobsterBoard - Claude Usage</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #0d1117; color: #e6edf3; }
    .container { max-width: 700px; margin: 0 auto; padding: 1.5rem; }
    h1 { font-size: 1.6rem; margin-bottom: 0.3rem; }
    .sub-header { color: #8b949e; font-size: 0.85rem; margin-bottom: 1.5rem; }
    .card { background: #161b22; border: 1px solid #30363d; border-radius: 10px; padding: 1.4rem; margin-bottom: 1.2rem; }
    .card h2 { font-size: 0.95rem; color: #8b949e; margin-bottom: 1rem; display: flex; align-items: center; gap: 8px; }
    .meter { margin-bottom: 1.2rem; }
    .meter:last-child { margin-bottom: 0; }
    .meter-header { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px; }
    .meter-label { font-weight: 600; font-size: 0.95rem; }
    .meter-value { font-size: 1.3rem; font-weight: 700; }
    .meter-bar { background: #21262d; border-radius: 6px; height: 10px; overflow: hidden; }
    .meter-fill { height: 100%; border-radius: 6px; transition: width 0.6s ease; }
    .meter-sub { text-align: right; margin-top: 4px; font-size: 0.8rem; color: #8b949e; }
    .green { color: #3fb950; }
    .yellow { color: #d29922; }
    .red { color: #f85149; }
    .bg-green { background: #3fb950; }
    .bg-yellow { background: #d29922; }
    .bg-red { background: #f85149; }
    .extra-row { display: flex; justify-content: space-between; padding-top: 0.8rem; border-top: 1px solid #30363d; margin-top: 0.4rem; }
    .extra-label { color: #8b949e; font-size: 0.9rem; }
    .extra-value { font-weight: 600; font-size: 0.95rem; }
    .badge { display: inline-block; padding: 3px 10px; border-radius: 12px; font-size: 0.75rem; font-weight: 600; background: #1f6feb33; color: #58a6ff; margin-left: 8px; }
    .loading { color: #8b949e; text-align: center; padding: 2rem; font-style: italic; }
    .error { color: #f85149; text-align: center; padding: 2rem; }
    .refresh-info { color: #484f58; font-size: 0.75rem; text-align: center; margin-top: 1rem; }
  </style>
</head>
<body>
  <nav id="page-nav"></nav>
  <main class="container">
    <h1>🤖 Claude Usage</h1>
    <div class="sub-header" id="plan-info">Loading...</div>

    <div class="card" id="usage-card">
      <div class="loading">Loading usage data...</div>
    </div>

    <div class="refresh-info" id="refresh-info"></div>
  </main>

  <script src="/pages/_shared/nav.js"></script>
  <script>
    function barClass(pct) {
      if (pct >= 80) return 'red';
      if (pct >= 50) return 'yellow';
      return 'green';
    }

    function timeLeft(iso) {
      if (!iso) return '';
      const ms = new Date(iso) - Date.now();
      if (ms <= 0) return 'just now';
      const h = Math.floor(ms / 3600000);
      const m = Math.floor((ms % 3600000) / 60000);
      if (h > 24) return Math.floor(h / 24) + 'd ' + (h % 24) + 'h';
      return h > 0 ? h + 'h ' + m + 'm' : m + 'm';
    }

    function renderMeter(label, pct, resetIso) {
      const p = Math.min(100, Math.max(0, pct || 0));
      const cls = barClass(p);
      const reset = resetIso ? `<div class="meter-sub">resets in ${timeLeft(resetIso)}</div>` : '';
      return `<div class="meter">
        <div class="meter-header">
          <span class="meter-label">${label}</span>
          <span class="meter-value ${cls}">${p.toFixed(0)}%</span>
        </div>
        <div class="meter-bar"><div class="meter-fill bg-${cls}" style="width:${p}%"></div></div>
        ${reset}
      </div>`;
    }

    async function loadUsage() {
      const card = document.getElementById('usage-card');
      const planEl = document.getElementById('plan-info');
      const refreshEl = document.getElementById('refresh-info');

      try {
        const res = await fetch('/api/pages/claude-usage/usage');
        const d = await res.json();

        if (d.error) {
          card.innerHTML = `<div class="error">${d.error}</div>`;
          return;
        }

        const labels = { max: 'Max (5×)', pro: 'Pro', free: 'Free' };
        const planName = labels[d.subscription] || d.subscription || 'Unknown';
        const tierLabel = d.tier ? d.tier.replace('default_claude_', '').replace(/_/g, ' ') : '';
        planEl.innerHTML = `${planName} plan` + (tierLabel ? `<span class="badge">${tierLabel}</span>` : '');

        let html = '';
        if (d.five_hour) html += renderMeter('5-Hour Session', d.five_hour.utilization, d.five_hour.resets_at);
        if (d.seven_day) html += renderMeter('7-Day Weekly', d.seven_day.utilization, d.seven_day.resets_at);
        if (d.seven_day_opus) html += renderMeter('Opus (7-Day)', d.seven_day_opus.utilization, d.seven_day_opus.resets_at);
        if (d.seven_day_sonnet) html += renderMeter('Sonnet (7-Day)', d.seven_day_sonnet.utilization, d.seven_day_sonnet.resets_at);

        if (d.extra_usage && d.extra_usage.is_enabled) {
          const used = (d.extra_usage.used_credits / 100).toFixed(2);
          const limit = d.extra_usage.monthly_limit > 0 ? '$' + (d.extra_usage.monthly_limit / 100).toFixed(2) : 'No limit';
          html += `<div class="extra-row">
            <span class="extra-label">Extra Usage (this month)</span>
            <span class="extra-value">$${used} / ${limit}</span>
          </div>`;
        }

        card.innerHTML = html || '<div class="loading">No usage data available</div>';
        refreshEl.textContent = 'Last updated: ' + new Date().toLocaleTimeString();
      } catch (e) {
        card.innerHTML = `<div class="error">Failed to load: ${e.message}</div>`;
      }
    }

    loadUsage();
    setInterval(loadUsage, 120000);
  </script>
</body>
</html>
```

## File: `pages/claude-usage/page.json`
```json
{
  "id": "claude-usage",
  "title": "Claude Usage",
  "icon": "🤖",
  "description": "Claude Code subscription usage tracker",
  "order": 5
}
```

## File: `pages/_shared/nav.js`
```javascript
// Shared navigation for LobsterBoard pages
// Include via <script src="/pages/_shared/nav.js"></script>
// Requires <nav id="page-nav"></nav> in the page HTML

(function() {
  const navEl = document.getElementById('page-nav');
  if (!navEl) return;

  const currentPath = window.location.pathname;

  fetch('/api/pages')
    .then(r => r.json())
    .then(pages => {
      const links = [
        { href: '/', icon: '🦞', title: 'Dashboard' }
      ].concat(pages.map(p => ({
        href: '/pages/' + p.id,
        icon: p.icon,
        title: p.title
      })));

      navEl.innerHTML = `
        <div class="lb-nav">
          <div class="lb-nav-left">
            ${links.map(l => {
              const active = l.href === currentPath || (l.href !== '/' && currentPath.startsWith(l.href));
              return `<a href="${l.href}" class="lb-nav-link${active ? ' active' : ''}">${l.icon} ${l.title}</a>`;
            }).join('')}
          </div>
        </div>
      `;
    })
    .catch(() => {
      navEl.innerHTML = `<div class="lb-nav"><div class="lb-nav-left">
        <a href="/" class="lb-nav-link">🦞 Dashboard</a>
      </div></div>`;
    });

  // Inject nav styles if not already present
  if (!document.getElementById('lb-nav-styles')) {
    const style = document.createElement('style');
    style.id = 'lb-nav-styles';
    style.textContent = `
      .lb-nav {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: #161b22;
        border-bottom: 1px solid #30363d;
        padding: 0 1rem;
        height: 42px;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      }
      .lb-nav-left {
        display: flex;
        align-items: center;
        gap: 0.25rem;
      }
      .lb-nav-link {
        color: #8b949e;
        text-decoration: none;
        font-size: 13px;
        font-weight: 500;
        padding: 6px 10px;
        border-radius: 6px;
        transition: color 0.15s, background 0.15s;
      }
      .lb-nav-link:hover {
        color: #e6edf3;
        background: #21262d;
      }
      .lb-nav-link.active {
        color: #e6edf3;
        background: #30363d;
      }
    `;
    document.head.appendChild(style);
  }
})();
```

## File: `src/builder.js`
```javascript
/**
 * LobsterBoard - Dashboard Builder Core
 * Provides utilities for generating dashboard HTML, CSS, and JS
 * 
 * @module lobsterboard/builder
 */

import { WIDGETS } from './widgets.js';

// ─────────────────────────────────────────────
// SECURITY HELPERS
// ─────────────────────────────────────────────

/**
 * Escape HTML to prevent XSS attacks
 * @param {string} str - String to escape
 * @returns {string} Escaped string
 */
export function escapeHtml(str) {
  if (!str) return '';
  if (typeof document !== 'undefined') {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
  }
  // Fallback for Node.js
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

// ─────────────────────────────────────────────
// HTML PROCESSING
// ─────────────────────────────────────────────

/**
 * Process widget HTML to conditionally remove header
 * @param {string} html - Widget HTML
 * @param {boolean} showHeader - Whether to show the header
 * @returns {string} Processed HTML
 */
export function processWidgetHtml(html, showHeader) {
  if (showHeader !== false) return html;
  const headerRegex = /<div\s+class="dash-card-head"[^>]*>[\s\S]*?<\/div>/i;
  return html.replace(headerRegex, '');
}

// ─────────────────────────────────────────────
// CSS GENERATION
// ─────────────────────────────────────────────

/**
 * Generate the base dashboard CSS
 * @returns {string} CSS styles
 */
export function generateDashboardCss() {
  return `/* LobsterBoard Dashboard - Generated Styles */

:root {
  --bg-primary: #0d1117;
  --bg-secondary: #161b22;
  --bg-tertiary: #21262d;
  --bg-hover: #30363d;
  --border: #30363d;
  --text-primary: #e6edf3;
  --text-secondary: #8b949e;
  --text-muted: #6e7681;
  --accent-blue: #58a6ff;
  --accent-green: #3fb950;
  --accent-orange: #d29922;
  --accent-red: #f85149;
  --accent-purple: #a371f7;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: var(--bg-primary);
  color: var(--text-primary);
  min-height: 100vh;
}

.dashboard {
  margin: 0 auto;
  overflow: hidden;
}

.widget-container {
  overflow: hidden;
}

/* KPI Cards */
.kpi-card {
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 16px;
  display: flex;
  align-items: center;
  gap: 12px;
  height: 100%;
}

.kpi-sm {
  padding: 12px;
}

.kpi-icon {
  font-size: 24px;
}

.kpi-data {
  flex: 1;
}

.kpi-value {
  font-size: 20px;
  font-weight: 600;
}

.kpi-value.blue { color: var(--accent-blue); }
.kpi-value.green { color: var(--accent-green); }
.kpi-value.orange { color: var(--accent-orange); }
.kpi-value.red { color: var(--accent-red); }

.kpi-label {
  font-size: 12px;
  color: var(--text-secondary);
  margin-top: 2px;
}

.kpi-indicator {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--text-muted);
}

.kpi-indicator.green { background: var(--accent-green); }
.kpi-indicator.yellow { background: var(--accent-orange); }
.kpi-indicator.red { background: var(--accent-red); }

/* Dash Cards */
.dash-card {
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  height: 100%;
  overflow: hidden;
}

.dash-card-head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  border-bottom: 1px solid var(--border);
  background: var(--bg-tertiary);
}

.dash-card-title {
  font-size: 13px;
  font-weight: 600;
}

.dash-card-badge {
  font-size: 11px;
  color: var(--text-secondary);
  background: var(--bg-primary);
  padding: 2px 8px;
  border-radius: 10px;
}

.dash-card-body {
  flex: 1;
  padding: 12px 16px;
  overflow-y: auto;
}

.compact-list {
  font-size: 12px;
}

.syslog-scroll {
  font-family: 'SF Mono', Monaco, monospace;
  font-size: 11px;
}

/* Top Bar */
.topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 20px;
  background: var(--bg-secondary);
  border-bottom: 1px solid var(--border);
  height: 100%;
}

.topbar-left {
  display: flex;
  align-items: center;
  gap: 20px;
}

.topbar-brand {
  font-weight: 600;
  font-size: 14px;
}

.topbar-link {
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 13px;
}

.topbar-link:hover,
.topbar-link.active {
  color: var(--accent-blue);
}

.topbar-right {
  display: flex;
  align-items: center;
  gap: 12px;
}

.topbar-meta {
  font-size: 12px;
  color: var(--text-muted);
}

.topbar-refresh {
  background: var(--bg-tertiary);
  border: 1px solid var(--border);
  color: var(--text-secondary);
  padding: 4px 8px;
  border-radius: 4px;
  cursor: pointer;
}

/* List Items */
.list-item {
  padding: 6px 0;
  border-bottom: 1px solid var(--border);
}

.list-item:last-child {
  border-bottom: none;
}

.cron-item {
  display: flex;
  justify-content: space-between;
  padding: 6px 0;
  border-bottom: 1px solid var(--border);
}

.cron-name {
  color: var(--text-primary);
}

.cron-next {
  color: var(--text-muted);
  font-size: 11px;
}

.log-line {
  padding: 2px 0;
  border-bottom: 1px solid rgba(48, 54, 61, 0.5);
}

/* Weather */
.weather-row {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 0;
  border-bottom: 1px solid var(--border);
}

.weather-row:last-child {
  border-bottom: none;
}

.weather-icon {
  font-size: 18px;
}

.weather-loc {
  flex: 1;
  color: var(--text-primary);
}

.weather-temp {
  font-weight: 600;
  color: var(--accent-blue);
}

/* Utilities */
.loading-sm {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.spinner-sm {
  width: 20px;
  height: 20px;
  border: 2px solid var(--bg-tertiary);
  border-top-color: var(--accent-blue);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.error {
  color: var(--accent-red);
  padding: 10px;
  text-align: center;
}

::-webkit-scrollbar {
  width: 6px;
}

::-webkit-scrollbar-track {
  background: var(--bg-primary);
}

::-webkit-scrollbar-thumb {
  background: var(--bg-tertiary);
  border-radius: 3px;
}

/* Post-Export Edit Mode */
.edit-mode .widget-container {
  cursor: move;
  outline: 2px dashed #3b82f6;
  outline-offset: -2px;
}

.edit-mode .widget-container:hover {
  outline-color: #60a5fa;
}

.edit-mode .widget-container.dragging {
  opacity: 0.8;
  z-index: 1000;
}

.resize-handle-edit {
  display: none;
  position: absolute;
  bottom: 0;
  right: 0;
  width: 16px;
  height: 16px;
  cursor: se-resize;
  background: #3b82f6;
  border-radius: 2px 0 0 0;
  z-index: 10;
}

.edit-mode .resize-handle-edit {
  display: block;
}

#edit-toggle {
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 9999;
  padding: 8px 16px;
  background: #1e293b;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 13px;
  font-weight: 500;
  box-shadow: 0 2px 8px rgba(0,0,0,0.3);
}

#edit-toggle:hover {
  background: #334155;
}

#edit-toggle.active {
  background: #3b82f6;
}
`;
}

// ─────────────────────────────────────────────
// JS GENERATION
// ─────────────────────────────────────────────

/**
 * Generate the post-export edit mode JS
 * @returns {string} JavaScript code
 */
export function generateEditJs() {
  return `
// ─────────────────────────────────────────────
// POST-EXPORT LAYOUT EDITING
// ─────────────────────────────────────────────

(function() {
  const STORAGE_KEY = 'lobsterboard-layout';
  const GRID_SIZE = 20;
  const MIN_WIDTH = 100;
  const MIN_HEIGHT = 60;
  
  let editMode = false;
  let activeWidget = null;
  let startX, startY, origLeft, origTop, origWidth, origHeight;
  let isResizing = false;

  document.addEventListener('DOMContentLoaded', initEditMode);

  function initEditMode() {
    const btn = document.createElement('button');
    btn.id = 'edit-toggle';
    btn.textContent = '✏️ Edit Layout';
    btn.onclick = toggleEditMode;
    document.body.appendChild(btn);
    document.querySelectorAll('.widget-container').forEach(initWidget);
    loadPositions();
  }

  function initWidget(widget) {
    const handle = document.createElement('div');
    handle.className = 'resize-handle-edit';
    widget.appendChild(handle);
    widget.addEventListener('mousedown', onWidgetMouseDown);
    handle.addEventListener('mousedown', onResizeMouseDown);
  }

  function toggleEditMode() {
    editMode = !editMode;
    document.body.classList.toggle('edit-mode', editMode);
    document.getElementById('edit-toggle').classList.toggle('active', editMode);
    document.getElementById('edit-toggle').textContent = editMode ? '💾 Save Layout' : '✏️ Edit Layout';
    if (!editMode) savePositions();
  }

  function onWidgetMouseDown(e) {
    if (!editMode) return;
    if (e.target.classList.contains('resize-handle-edit')) return;
    if (e.button !== 0) return;
    e.preventDefault();
    activeWidget = e.currentTarget;
    isResizing = false;
    startX = e.clientX;
    startY = e.clientY;
    origLeft = activeWidget.offsetLeft;
    origTop = activeWidget.offsetTop;
    activeWidget.classList.add('dragging');
    document.addEventListener('mousemove', onMouseMove);
    document.addEventListener('mouseup', onMouseUp);
  }

  function onResizeMouseDown(e) {
    if (!editMode) return;
    e.preventDefault();
    e.stopPropagation();
    activeWidget = e.target.parentElement;
    isResizing = true;
    startX = e.clientX;
    startY = e.clientY;
    origWidth = activeWidget.offsetWidth;
    origHeight = activeWidget.offsetHeight;
    activeWidget.classList.add('dragging');
    document.addEventListener('mousemove', onMouseMove);
    document.addEventListener('mouseup', onMouseUp);
  }

  function onMouseMove(e) {
    if (!activeWidget) return;
    const dx = e.clientX - startX;
    const dy = e.clientY - startY;
    if (isResizing) {
      activeWidget.style.width = Math.max(MIN_WIDTH, origWidth + dx) + 'px';
      activeWidget.style.height = Math.max(MIN_HEIGHT, origHeight + dy) + 'px';
    } else {
      activeWidget.style.left = Math.max(0, origLeft + dx) + 'px';
      activeWidget.style.top = Math.max(0, origTop + dy) + 'px';
    }
  }

  function onMouseUp() {
    if (!activeWidget) return;
    if (isResizing) {
      activeWidget.style.width = snapToGrid(activeWidget.offsetWidth) + 'px';
      activeWidget.style.height = snapToGrid(activeWidget.offsetHeight) + 'px';
    } else {
      activeWidget.style.left = snapToGrid(activeWidget.offsetLeft) + 'px';
      activeWidget.style.top = snapToGrid(activeWidget.offsetTop) + 'px';
    }
    activeWidget.classList.remove('dragging');
    activeWidget = null;
    isResizing = false;
    document.removeEventListener('mousemove', onMouseMove);
    document.removeEventListener('mouseup', onMouseUp);
  }

  function snapToGrid(value) {
    return Math.round(value / GRID_SIZE) * GRID_SIZE;
  }

  function savePositions() {
    const positions = {};
    document.querySelectorAll('.widget-container').forEach(widget => {
      const id = widget.dataset.widgetId;
      if (id) {
        positions[id] = {
          left: widget.offsetLeft,
          top: widget.offsetTop,
          width: widget.offsetWidth,
          height: widget.offsetHeight
        };
      }
    });
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(positions));
    } catch (e) {}
  }

  function loadPositions() {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (!saved) return;
      const positions = JSON.parse(saved);
      document.querySelectorAll('.widget-container').forEach(widget => {
        const id = widget.dataset.widgetId;
        const pos = positions[id];
        if (pos) {
          widget.style.left = pos.left + 'px';
          widget.style.top = pos.top + 'px';
          widget.style.width = pos.width + 'px';
          widget.style.height = pos.height + 'px';
        }
      });
    } catch (e) {}
  }
})();
`;
}

// ─────────────────────────────────────────────
// DASHBOARD GENERATION
// ─────────────────────────────────────────────

/**
 * Generate widget HTML for a widget configuration
 * @param {Object} widget - Widget configuration
 * @returns {string} Widget HTML
 */
export function generateWidgetHtml(widget) {
  const template = WIDGETS[widget.type];
  if (!template) return '';

  const props = { ...widget.properties, id: widget.id };
  let html = processWidgetHtml(template.generateHtml(props), widget.properties.showHeader);

  return `
    <div class="widget-container" data-widget-id="${widget.id}" style="position:absolute;left:${widget.x}px;top:${widget.y}px;width:${widget.width}px;height:${widget.height}px;">
      ${html}
    </div>`;
}

/**
 * Generate widget JavaScript for a widget configuration
 * @param {Object} widget - Widget configuration
 * @returns {string} Widget JavaScript
 */
export function generateWidgetJs(widget) {
  const template = WIDGETS[widget.type];
  if (!template || !template.generateJs) return '';

  const props = { ...widget.properties, id: widget.id };
  return template.generateJs(props);
}

/**
 * Generate complete dashboard HTML
 * @param {Object} config - Dashboard configuration
 * @param {Object} config.canvas - Canvas dimensions { width, height }
 * @param {Array} config.widgets - Array of widget configurations
 * @returns {string} Complete HTML document
 */
export function generateDashboardHtml(config) {
  const { canvas, widgets } = config;
  const widgetHtml = widgets.map(generateWidgetHtml).join('\n');

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My LobsterBoard Dashboard</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <main class="dashboard" style="width:${canvas.width}px;height:${canvas.height}px;position:relative;">
    ${widgetHtml}
  </main>
  <script src="js/dashboard.js"></script>
</body>
</html>`;
}

/**
 * Generate complete dashboard JavaScript
 * @param {Array} widgets - Array of widget configurations
 * @returns {string} Complete JavaScript
 */
export function generateDashboardJs(widgets) {
  const widgetJs = widgets.map(generateWidgetJs).filter(Boolean).join('\n\n');
  const editJs = generateEditJs();

  return `/**
 * LobsterBoard Dashboard - Generated JavaScript
 * Replace YOUR_*_API_KEY placeholders with your actual API keys
 */

document.addEventListener('DOMContentLoaded', () => {
  console.log('Dashboard loaded');
});

${widgetJs}

${editJs}
`;
}

/**
 * Generate README for exported dashboard
 * @param {Array} widgets - Array of widget configurations
 * @returns {string} README markdown
 */
export function generateReadme(widgets) {
  const apiKeys = [];
  const needsOpenClaw = widgets.some(w => 
    ['openclaw-release', 'auth-status', 'activity-list', 'cron-jobs', 'system-log', 'session-count', 'token-gauge'].includes(w.type)
  );
  
  widgets.forEach(widget => {
    const template = WIDGETS[widget.type];
    if (template?.hasApiKey && template.apiKeyName) {
      if (!apiKeys.includes(template.apiKeyName)) {
        apiKeys.push(template.apiKeyName);
      }
    }
  });

  return `# LobsterBoard Dashboard

This dashboard was generated with LobsterBoard Dashboard Builder.

## Quick Start

${needsOpenClaw ? `### Running with OpenClaw widgets

Your dashboard includes widgets that connect to OpenClaw. Run the included server:

\`\`\`bash
node server.js
\`\`\`

Open http://localhost:8080 in your browser.
` : ''}
### Static mode

Open \`index.html\` directly in a browser.

## Files

| File | Description |
|------|-------------|
| \`index.html\` | Dashboard page |
| \`css/style.css\` | Styles |
| \`js/dashboard.js\` | Widget logic |
| \`server.js\` | Server with OpenClaw API proxy |

${apiKeys.length > 0 ? `## API Keys

Edit \`js/dashboard.js\` and replace these placeholders:
${apiKeys.map(key => `- \`YOUR_${key}\``).join('\n')}
` : ''}

---

Generated with LobsterBoard - https://github.com/curbob/LobsterBoard
`;
}

export default {
  escapeHtml,
  processWidgetHtml,
  generateDashboardCss,
  generateEditJs,
  generateWidgetHtml,
  generateWidgetJs,
  generateDashboardHtml,
  generateDashboardJs,
  generateReadme
};
```

## File: `src/index.js`
```javascript
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

## File: `src/widgets.js`
```javascript
/**
 * LobsterBoard - Widget Definitions
 * Each widget defines its default size, properties, and generated code
 * 
 * @module lobsterboard/widgets
 */

export const WIDGETS = {
  // ─────────────────────────────────────────────
  // SMALL CARDS (KPI style)
  // ─────────────────────────────────────────────
  
  'weather': {
    name: 'Local Weather',
    icon: '🌡️',
    category: 'small',
    description: 'Shows current weather for a single location using wttr.in (no API key needed).',
    defaultWidth: 200,
    defaultHeight: 120,
    hasApiKey: false,
    properties: {
      title: 'Local Weather',
      location: 'Atlanta',
      units: 'F',
      refreshInterval: 600
    },
    preview: `<div style="text-align:center;padding:8px;">
      <div style="font-size:24px;">72°F</div>
      <div style="font-size:11px;color:#8b949e;">Atlanta</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">🌡️ ${props.title || 'Local Weather'}</span>
        </div>
        <div class="dash-card-body" style="display:flex;align-items:center;justify-content:center;gap:10px;">
          <span id="${props.id}-icon" style="font-size:24px;">🌡️</span>
          <div>
            <div class="kpi-value blue" id="${props.id}-value">—</div>
            <div class="kpi-label" id="${props.id}-label">${props.location || 'Location'}</div>
          </div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Weather Widget: ${props.id} (uses free wttr.in API - no key needed)
      async function update_${props.id.replace(/-/g, '_')}() {
        try {
          const location = encodeURIComponent('${props.location || 'Atlanta'}');
          const res = await fetch('https://wttr.in/' + location + '?format=j1');
          const data = await res.json();
          const current = data.current_condition[0];
          const temp = '${props.units}' === 'C' ? current.temp_C : current.temp_F;
          const unit = '${props.units}' === 'C' ? '°C' : '°F';
          document.getElementById('${props.id}-value').textContent = temp + unit;
          document.getElementById('${props.id}-label').textContent = current.weatherDesc[0].value;
          const code = parseInt(current.weatherCode);
          let icon = '🌡️';
          if (code === 113) icon = '☀️';
          else if (code === 116 || code === 119) icon = '⛅';
          else if (code >= 176 && code <= 359) icon = '🌧️';
          else if (code >= 368 && code <= 395) icon = '❄️';
          document.getElementById('${props.id}-icon').textContent = icon;
        } catch (e) {
          console.error('Weather widget error:', e);
          document.getElementById('${props.id}-value').textContent = '—';
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 600) * 1000});
    `
  },

  'clock': {
    name: 'Clock',
    icon: '🕐',
    category: 'small',
    description: 'Simple digital clock. Supports 12h or 24h format.',
    defaultWidth: 200,
    defaultHeight: 120,
    hasApiKey: false,
    properties: {
      title: 'Clock',
      timezone: 'local',
      format24h: false
    },
    preview: `<div style="text-align:center;padding:8px;">
      <div style="font-size:24px;">3:45 PM</div>
      <div style="font-size:11px;color:#8b949e;">Wed, Feb 5</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">🕐 ${props.title || 'Clock'}</span>
        </div>
        <div class="dash-card-body" style="display:flex;flex-direction:column;align-items:center;justify-content:center;">
          <div class="kpi-value" id="${props.id}-time">—</div>
          <div class="kpi-label" id="${props.id}-date">—</div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Clock Widget: ${props.id}
      function updateClock_${props.id.replace(/-/g, '_')}() {
        const now = new Date();
        const timeEl = document.getElementById('${props.id}-time');
        const dateEl = document.getElementById('${props.id}-date');
        const opts = { hour: 'numeric', minute: '2-digit', hour12: ${!props.format24h} };
        timeEl.textContent = now.toLocaleTimeString('en-US', opts);
        dateEl.textContent = now.toLocaleDateString('en-US', { weekday: 'short', month: 'short', day: 'numeric' });
      }
      updateClock_${props.id.replace(/-/g, '_')}();
      setInterval(updateClock_${props.id.replace(/-/g, '_')}, 1000);
    `
  },

  'auth-status': {
    name: 'Auth Status',
    icon: '🔐',
    category: 'small',
    description: 'Shows if OpenClaw is using Anthropic Max subscription (green) or API key fallback (yellow).',
    defaultWidth: 180,
    defaultHeight: 100,
    hasApiKey: true,
    apiKeyName: 'OPENCLAW_API',
    properties: {
      title: 'Auth Type',
      endpoint: '/api/status',
      refreshInterval: 30
    },
    preview: `<div style="text-align:center;padding:8px;">
      <div style="width:10px;height:10px;background:#3fb950;border-radius:50%;margin:0 auto 4px;"></div>
      <div style="font-size:13px;">OAuth</div>
      <div style="font-size:11px;color:#8b949e;">Auth</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">🔐 ${props.title || 'Auth Type'}</span>
        </div>
        <div class="dash-card-body" style="display:flex;align-items:center;justify-content:center;gap:10px;">
          <div class="kpi-indicator" id="${props.id}-dot"></div>
          <div class="kpi-value" id="${props.id}-value">—</div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Auth Status Widget: ${props.id}
      async function update_${props.id.replace(/-/g, '_')}() {
        try {
          const res = await fetch('${props.endpoint || '/api/status'}');
          const json = await res.json();
          const data = json.data || json;
          const dot = document.getElementById('${props.id}-dot');
          const val = document.getElementById('${props.id}-value');
          val.textContent = data.authMode === 'oauth' ? 'Subscription' : 'API';
          dot.className = 'kpi-indicator ' + (data.authMode === 'oauth' ? 'green' : 'yellow');
        } catch (e) {
          console.error('Auth status widget error:', e);
          document.getElementById('${props.id}-value').textContent = '—';
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 30) * 1000});
    `
  },

  'session-count': {
    name: 'Active Sessions',
    icon: '💬',
    category: 'small',
    description: 'Shows count of active OpenClaw sessions.',
    defaultWidth: 160,
    defaultHeight: 100,
    hasApiKey: true,
    apiKeyName: 'OPENCLAW_API',
    properties: {
      title: 'Sessions',
      endpoint: '/api/sessions',
      refreshInterval: 30
    },
    preview: `<div style="text-align:center;padding:8px;">
      <div style="font-size:28px;color:#58a6ff;">3</div>
      <div style="font-size:11px;color:#8b949e;">Active</div>
    </div>`,
    generateHtml: (props) => `
      <div class="kpi-card kpi-sm" id="widget-${props.id}">
        <div class="kpi-icon">💬</div>
        <div class="kpi-data">
          <div class="kpi-value blue" id="${props.id}-count">—</div>
          <div class="kpi-label">Active</div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Session Count Widget: ${props.id}
      async function update_${props.id.replace(/-/g, '_')}() {
        try {
          const res = await fetch('${props.endpoint || '/api/sessions'}');
          const json = await res.json();
          const data = json.data || json;
          document.getElementById('${props.id}-count').textContent = data.active || data.length || 0;
        } catch (e) {
          document.getElementById('${props.id}-count').textContent = '—';
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 30) * 1000});
    `
  },

  // ─────────────────────────────────────────────
  // LARGE CARDS (Content)
  // ─────────────────────────────────────────────

  'activity-list': {
    name: 'Activity List',
    icon: '📋',
    category: 'large',
    description: 'Shows recent OpenClaw activity from /api/activity endpoint.',
    defaultWidth: 400,
    defaultHeight: 300,
    hasApiKey: true,
    apiKeyName: 'OPENCLAW_API',
    properties: {
      title: 'Today',
      endpoint: '/api/activity',
      maxItems: 10,
      refreshInterval: 60
    },
    preview: `<div style="padding:4px;font-size:11px;color:#8b949e;">
      <div>• Meeting at 2pm</div>
      <div>• Review PR #42</div>
      <div>• Deploy v1.2</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">📋 ${props.title || 'Today'}</span>
          <span class="dash-card-badge" id="${props.id}-badge">—</span>
        </div>
        <div class="dash-card-body compact-list" id="${props.id}-list">
          <div class="list-item">• Team standup at 10am</div>
          <div class="list-item">• Review PR #42</div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Activity List Widget: ${props.id}
      async function update_${props.id.replace(/-/g, '_')}() {
        try {
          const res = await fetch('${props.endpoint || '/api/activity'}');
          const json = await res.json();
          const data = json.data || json;
          const list = document.getElementById('${props.id}-list');
          const badge = document.getElementById('${props.id}-badge');
          const items = data.items || [];
          list.innerHTML = items.slice(0, ${props.maxItems || 10}).map(item => 
            '<div class="list-item">' + item.text + '</div>'
          ).join('');
          badge.textContent = items.length + ' items';
        } catch (e) {
          console.error('Activity list widget error:', e);
          document.getElementById('${props.id}-list').innerHTML = '<div class="list-item">—</div>';
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 60) * 1000});
    `
  },

  'cron-jobs': {
    name: 'Cron Jobs',
    icon: '⏰',
    category: 'large',
    description: 'Lists scheduled cron jobs from OpenClaw /api/cron endpoint.',
    defaultWidth: 400,
    defaultHeight: 250,
    hasApiKey: true,
    apiKeyName: 'OPENCLAW_API',
    properties: {
      title: 'Cron',
      endpoint: '/api/cron',
      refreshInterval: 30
    },
    preview: `<div style="padding:4px;font-size:11px;color:#8b949e;">
      <div>⏰ Daily backup - 2am</div>
      <div>⏰ Sync data - */5 *</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">⏰ ${props.title || 'Cron'}</span>
          <span class="dash-card-badge" id="${props.id}-badge">—</span>
        </div>
        <div class="dash-card-body" id="${props.id}-list">
          <div class="cron-item"><span class="cron-name">Daily backup</span><span class="cron-next">2:00 AM</span></div>
        </div>
      </div>`,
    generateJs: (props) => `
      // Cron Jobs Widget: ${props.id}
      async function update_${props.id.replace(/-/g, '_')}() {
        try {
          const res = await fetch('${props.endpoint || '/api/cron'}');
          const json = await res.json();
          const data = json.data || json;
          const list = document.getElementById('${props.id}-list');
          const badge = document.getElementById('${props.id}-badge');
          const jobs = data.jobs || [];
          list.innerHTML = jobs.map(job => 
            '<div class="cron-item"><span class="cron-name">' + job.name + '</span><span class="cron-next">' + job.next + '</span></div>'
          ).join('');
          badge.textContent = jobs.length + ' jobs';
        } catch (e) {
          console.error('Cron jobs widget error:', e);
          document.getElementById('${props.id}-list').innerHTML = '<div class="cron-item"><span class="cron-name">—</span></div>';
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 30) * 1000});
    `
  },

  'system-log': {
    name: 'System Log',
    icon: '🔧',
    category: 'large',
    description: 'Shows recent system logs from OpenClaw /api/logs endpoint.',
    defaultWidth: 500,
    defaultHeight: 400,
    hasApiKey: true,
    apiKeyName: 'OPENCLAW_API',
    properties: {
      title: 'System Log',
      endpoint: '/api/logs',
      maxLines: 50,
      refreshInterval: 10
    },
    preview: `<div style="padding:4px;font-size:10px;font-family:monospace;color:#8b949e;">
      <div>[INFO] System started</div>
      <div>[DEBUG] Loading config</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">🔧 ${props.title || 'System Log'}</span>
          <span class="dash-card-badge" id="${props.id}-badge">—</span>
        </div>
        <div class="dash-card-body compact-list syslog-scroll" id="${props.id}-log">
          <div class="log-line">[INFO] System started successfully</div>
        </div>
      </div>`,
    generateJs: (props) => `
      // System Log Widget: ${props.id}
      async function update_${props.id.replace(/-/g, '_')}() {
        try {
          const res = await fetch('${props.endpoint || '/api/logs'}');
          const json = await res.json();
          const data = json.data || json;
          const log = document.getElementById('${props.id}-log');
          const badge = document.getElementById('${props.id}-badge');
          const lines = data.lines || [];
          log.innerHTML = lines.slice(-${props.maxLines || 50}).map(line => 
            '<div class="log-line">' + line + '</div>'
          ).join('');
          badge.textContent = lines.length + ' lines';
          log.scrollTop = log.scrollHeight;
        } catch (e) {
          console.error('System log widget error:', e);
          document.getElementById('${props.id}-log').innerHTML = '<div class="log-line">—</div>';
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 10) * 1000});
    `
  },

  // ─────────────────────────────────────────────
  // BARS
  // ─────────────────────────────────────────────

  'pages-menu': {
    name: 'Pages Menu',
    icon: '📑',
    category: 'small',
    description: 'Navigation links to all discovered LobsterBoard pages. Supports vertical or horizontal layout.',
    defaultWidth: 220,
    defaultHeight: 200,
    hasApiKey: false,
    properties: {
      title: 'Pages',
      layout: 'vertical',
      refreshInterval: 60
    },
    preview: `<div style="padding:6px;font-size:11px;color:#8b949e;">
      <div>📝 Notes</div>
      <div>📋 Board</div>
      <div>📅 Calendar</div>
    </div>`,
    generateHtml: (props) => `
      <div class="dash-card" id="widget-${props.id}" style="height:100%;">
        <div class="dash-card-head">
          <span class="dash-card-title">📑 ${props.title || 'Pages'}</span>
        </div>
        <div class="dash-card-body pages-menu ${props.layout === 'horizontal' ? 'pages-menu-horizontal' : 'pages-menu-vertical'}" id="${props.id}-list">
          <span class="pages-menu-item">Loading…</span>
        </div>
      </div>
      <style>
        .pages-menu-vertical { display:flex; flex-direction:column; gap:4px; overflow-y:auto; }
        .pages-menu-horizontal { display:flex; flex-direction:row; flex-wrap:wrap; gap:6px; align-items:center; }
        .pages-menu-item {
          display:inline-flex; align-items:center; gap:6px;
          padding:6px 10px; border-radius:6px;
          background:#21262d; color:#c9d1d9;
          text-decoration:none; font-size:13px;
          transition: background .15s, color .15s;
        }
        .pages-menu-item:hover { background:#30363d; color:#58a6ff; }
        .pages-menu-item .pages-menu-icon { font-size:15px; }
      </style>`,
    generateJs: (props) => `
      // Pages Menu Widget: ${props.id}
      async function update_${props.id.replace(/-/g, '_')}() {
        try {
          const res = await fetch('/api/pages');
          const pages = await res.json();
          const list = document.getElementById('${props.id}-list');
          if (!pages.length) { list.innerHTML = '<span class="pages-menu-item">No pages found</span>'; return; }
          list.innerHTML = pages.map(p =>
            '<a class="pages-menu-item" href="/pages/' + p.id + '" title="' + (p.description || p.title || p.name || '') + '">' +
            '<span class="pages-menu-icon">' + (p.icon || '📄') + '</span>' +
            '<span>' + (p.title || p.name || p.id) + '</span></a>'
          ).join('');
        } catch (e) {
          console.error('Pages menu widget error:', e);
          document.getElementById('${props.id}-list').innerHTML = '<span class="pages-menu-item">Error loading pages</span>';
        }
      }
      update_${props.id.replace(/-/g, '_')}();
      setInterval(update_${props.id.replace(/-/g, '_')}, ${(props.refreshInterval || 60) * 1000});
    `
  },

  'topbar': {
    name: 'Top Nav Bar',
    icon: '🔝',
    category: 'bar',
    description: 'Navigation bar with clock, weather, and system stats.',
    defaultWidth: 1920,
    defaultHeight: 48,
    hasApiKey: false,
    properties: {
      title: 'OpenClaw',
      links: 'Dashboard,Activity,Settings'
    },
    preview: `<div style="background:#161b22;padding:8px;font-size:11px;display:flex;gap:12px;">
      <span>🤖 OpenClaw</span>
      <span style="color:#58a6ff;">Dashboard</span>
    </div>`,
    generateHtml: (props) => `
      <nav class="topbar" id="widget-${props.id}">
        <div class="topbar-left">
          <span class="topbar-brand">🤖 ${props.title || 'OpenClaw'}</span>
          ${(props.links || 'Dashboard').split(',').map((link, i) => 
            `<a href="#" class="topbar-link${i === 0 ? ' active' : ''}">${link.trim()}</a>`
          ).join('')}
        </div>
        <div class="topbar-right">
          <span class="topbar-meta" id="${props.id}-refresh">—</span>
          <button class="topbar-refresh" onclick="location.reload()" title="Refresh">↻</button>
        </div>
      </nav>`,
    generateJs: (props) => `
      // Top Bar Widget: ${props.id}
      document.getElementById('${props.id}-refresh').textContent = 
        new Date().toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit' });
    `
  },

  'claude-usage': {
    name: 'Claude Usage',
    icon: '🤖',
    category: 'large',
    description: 'Real-time Claude Code subscription usage (5h session, 7d weekly, Opus, Sonnet limits). Reads credentials from ~/.claude.',
    defaultWidth: 380,
    defaultHeight: 260,
    hasApiKey: false,
    properties: { title: 'Claude Usage', refreshInterval: 120 },
    preview: `<div style="padding:8px;font-size:11px;"><div><b>5h Session</b> 28%</div><div><b>7d Weekly</b> 31%</div></div>`,
    generateHtml: (props) => `<div class="dash-card" id="widget-${props.id}" style="height:100%;"><div class="dash-card-head"><span class="dash-card-title">🤖 ${props.title || 'Claude Usage'}</span><span id="${props.id}-sub" style="font-size:10px;color:#8b949e;margin-left:auto;"></span></div><div class="dash-card-body" id="${props.id}-body" style="padding:8px 12px;overflow-y:auto;"><div style="color:#8b949e;text-align:center;">Loading...</div></div></div>`,
    generateJs: (props) => `
      function barColor(pct) { return pct >= 80 ? '#f85149' : pct >= 50 ? '#d29922' : '#3fb950'; }
      function timeLeft(iso) { if (!iso) return ''; const ms = new Date(iso) - Date.now(); if (ms <= 0) return 'now'; const h = Math.floor(ms/3600000), m = Math.floor((ms%3600000)/60000); return h > 0 ? h+'h '+m+'m' : m+'m'; }
      function usageBar(label, pct, resetIso) { const p = Math.min(100,Math.max(0,pct||0)), c = barColor(p), reset = resetIso ? '<span style="color:#8b949e;font-size:10px;">resets '+timeLeft(resetIso)+'</span>' : ''; return '<div style="margin-bottom:10px;"><div style="display:flex;justify-content:space-between;margin-bottom:3px;"><span style="font-weight:600;font-size:12px;">'+label+'</span><span style="font-size:13px;font-weight:700;color:'+c+';">'+p.toFixed(0)+'%</span></div><div style="background:#21262d;border-radius:4px;height:8px;overflow:hidden;"><div style="width:'+p+'%;height:100%;background:'+c+';border-radius:4px;transition:width .5s;"></div></div>'+(reset?'<div style="text-align:right;margin-top:2px;">'+reset+'</div>':'')+'</div>'; }
      async function update_${props.id.replace(/-/g,'_')}() { const body = document.getElementById('${props.id}-body'); const subEl = document.getElementById('${props.id}-sub'); try { const res = await fetch('/api/pages/claude-usage/usage'); const d = await res.json(); if (d.error) { body.innerHTML='<div style="color:#f85149;">'+d.error+'</div>'; return; } if (subEl) { subEl.textContent = {max:'Max (5×)',pro:'Pro',free:'Free'}[d.subscription]||d.subscription||''; } let html=''; if(d.five_hour) html+=usageBar('5h Session',d.five_hour.utilization,d.five_hour.resets_at); if(d.seven_day) html+=usageBar('7d Weekly',d.seven_day.utilization,d.seven_day.resets_at); if(d.seven_day_opus) html+=usageBar('Opus (7d)',d.seven_day_opus.utilization,d.seven_day_opus.resets_at); if(d.seven_day_sonnet&&d.seven_day_sonnet.utilization>0) html+=usageBar('Sonnet (7d)',d.seven_day_sonnet.utilization,d.seven_day_sonnet.resets_at); if(d.extra_usage&&d.extra_usage.is_enabled){const used=(d.extra_usage.used_credits/100).toFixed(2),limit=d.extra_usage.monthly_limit>0?(d.extra_usage.monthly_limit/100).toFixed(2):'∞';html+='<div style="margin-top:4px;padding-top:6px;border-top:1px solid #30363d;"><div style="display:flex;justify-content:space-between;font-size:11px;"><span style="color:#8b949e;">Extra Usage</span><span style="font-weight:600;">$'+used+' / $'+limit+'</span></div></div>';} if(!html) html='<div style="color:#8b949e;">No usage data</div>'; body.innerHTML=html; } catch(e) { console.error('Claude usage error:',e); body.innerHTML='<div style="color:#f85149;">Failed to load</div>'; } }
      update_${props.id.replace(/-/g,'_')}(); setInterval(update_${props.id.replace(/-/g,'_')}, ${(props.refreshInterval||120)*1000});
    `
  }
};

// Helper to get widget categories
export function getWidgetCategories() {
  const categories = {};
  for (const [key, widget] of Object.entries(WIDGETS)) {
    const cat = widget.category || 'other';
    if (!categories[cat]) categories[cat] = [];
    categories[cat].push({ key, ...widget });
  }
  return categories;
}

// Helper to get widget by type
export function getWidget(type) {
  return WIDGETS[type] || null;
}

// Helper to list all widget types
export function getWidgetTypes() {
  return Object.keys(WIDGETS);
}

export default WIDGETS;
```

## File: `templates/README.md`
```markdown
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

## File: `templates/templates.json`
```json
[
  {
    "id": "full-screen-focus-on-openclaw-systems",
    "name": "Full screen focus on OpenClaw systems",
    "description": "A full screen template that focuses on the Openclaw system log, activity and cron jobs",
    "author": "curbob",
    "tags": [
      "OpenClaw",
      "LobsterBoard"
    ],
    "canvasSize": "1920x1080",
    "widgetCount": 23,
    "widgetTypes": [
      {
        "type": "weather",
        "name": "Local Weather",
        "icon": "🌡️",
        "count": 1
      },
      {
        "type": "clock",
        "name": "Clock",
        "icon": "🕐",
        "count": 1
      },
      {
        "type": "text-header",
        "name": "Header / Text",
        "icon": "🔤",
        "count": 3
      },
      {
        "type": "horizontal-line",
        "name": "Horizontal Line",
        "icon": "➖",
        "count": 2
      },
      {
        "type": "auth-status",
        "name": "Auth Status",
        "icon": "🔐",
        "count": 1
      },
      {
        "type": "openclaw-release",
        "name": "OpenClaw Release",
        "icon": "🦞",
        "count": 1
      },
      {
        "type": "rss-ticker",
        "name": "RSS Ticker",
        "icon": "📡",
        "count": 1
      },
      {
        "type": "lobsterboard-release",
        "name": "LobsterBoard Release",
        "icon": "🦞",
        "count": 1
      },
      {
        "type": "cron-jobs",
        "name": "Cron Jobs",
        "icon": "⏰",
        "count": 1
      },
      {
        "type": "system-log",
        "name": "System Log",
        "icon": "🔧",
        "count": 1
      },
      {
        "type": "activity-list",
        "name": "Activity List",
        "icon": "📋",
        "count": 1
      },
      {
        "type": "cpu-memory",
        "name": "CPU / Memory",
        "icon": "💻",
        "count": 1
      },
      {
        "type": "disk-usage",
        "name": "Disk Usage",
        "icon": "💾",
        "count": 1
      },
      {
        "type": "network-speed",
        "name": "Network Speed",
        "icon": "🌐",
        "count": 1
      },
      {
        "type": "uptime-monitor",
        "name": "Uptime Monitor",
        "icon": "📡",
        "count": 1
      },
      {
        "type": "calendar",
        "name": "Calendar",
        "icon": "📅",
        "count": 1
      },
      {
        "type": "todo-list",
        "name": "Todo List",
        "icon": "✅",
        "count": 1
      },
      {
        "type": "github-stats",
        "name": "GitHub Stats",
        "icon": "🐙",
        "count": 1
      },
      {
        "type": "quote-of-day",
        "name": "Quote of Day",
        "icon": "💭",
        "count": 1
      },
      {
        "type": "stock-ticker",
        "name": "Stock Ticker",
        "icon": "📈",
        "count": 1
      }
    ],
    "requiresSetup": [],
    "preview": "preview.png"
  },
  {
    "id": "minimal-layout-for-10-inch-screen",
    "name": "minimal layout for 10 inch screen",
    "description": "For a small static screen where thereisn't much space for many widgets",
    "author": "Curbob",
    "tags": [],
    "canvasSize": "1280x800",
    "widgetCount": 14,
    "widgetTypes": [
      {
        "type": "weather",
        "name": "Local Weather",
        "icon": "🌡️",
        "count": 1
      },
      {
        "type": "clock",
        "name": "Clock",
        "icon": "🕐",
        "count": 1
      },
      {
        "type": "text-header",
        "name": "Header / Text",
        "icon": "🔤",
        "count": 3
      },
      {
        "type": "horizontal-line",
        "name": "Horizontal Line",
        "icon": "➖",
        "count": 2
      },
      {
        "type": "auth-status",
        "name": "Auth Status",
        "icon": "🔐",
        "count": 1
      },
      {
        "type": "openclaw-release",
        "name": "OpenClaw Release",
        "icon": "🦞",
        "count": 1
      },
      {
        "type": "rss-ticker",
        "name": "RSS Ticker",
        "icon": "📡",
        "count": 1
      },
      {
        "type": "lobsterboard-release",
        "name": "LobsterBoard Release",
        "icon": "🦞",
        "count": 1
      },
      {
        "type": "cron-jobs",
        "name": "Cron Jobs",
        "icon": "⏰",
        "count": 1
      },
      {
        "type": "system-log",
        "name": "System Log",
        "icon": "🔧",
        "count": 1
      },
      {
        "type": "activity-list",
        "name": "Activity List",
        "icon": "📋",
        "count": 1
      }
    ],
    "requiresSetup": [],
    "preview": "preview.png"
  }
]
```

## File: `templates/full-screen-focus-on-openclaw-systems/config.json`
```json
{
  "canvas": {
    "width": 1920,
    "height": 1080
  },
  "widgets": [
    {
      "id": "widget-1",
      "type": "weather",
      "x": 240,
      "y": 120,
      "width": 200,
      "height": 140,
      "properties": {
        "title": "Local Weather",
        "location": "Atlanta",
        "units": "F",
        "refreshInterval": 600,
        "showHeader": true
      }
    },
    {
      "id": "widget-3",
      "type": "clock",
      "x": 20,
      "y": 120,
      "width": 200,
      "height": 140,
      "properties": {
        "title": "Clock",
        "timezone": "local",
        "format24h": false
      }
    },
    {
      "id": "widget-12",
      "type": "text-header",
      "x": 20,
      "y": 20,
      "width": 400,
      "height": 50,
      "properties": {
        "title": "Lobster Board",
        "showHeader": false,
        "fontSize": 24,
        "fontColor": "#e6edf3",
        "textAlign": "left",
        "fontWeight": "bold"
      }
    },
    {
      "id": "widget-14",
      "type": "text-header",
      "x": 20,
      "y": 20,
      "width": 400,
      "height": 50,
      "properties": {
        "title": "Lobster Board",
        "showHeader": false,
        "fontSize": 24,
        "fontColor": "#e6edf3",
        "textAlign": "left",
        "fontWeight": "bold"
      }
    },
    {
      "id": "widget-15",
      "type": "horizontal-line",
      "x": 20,
      "y": 40,
      "width": 1220,
      "height": 60,
      "properties": {
        "title": "",
        "showHeader": false,
        "lineColor": "#30363d",
        "lineThickness": 2
      }
    },
    {
      "id": "widget-16",
      "type": "text-header",
      "x": 20,
      "y": 20,
      "width": 400,
      "height": 50,
      "properties": {
        "title": "Lobster Board",
        "showHeader": false,
        "showBorder": false,
        "fontSize": 24,
        "fontColor": "#e6edf3",
        "textAlign": "left",
        "fontWeight": "bold"
      }
    },
    {
      "id": "widget-18",
      "type": "horizontal-line",
      "x": 20,
      "y": 40,
      "width": 1860,
      "height": 60,
      "properties": {
        "title": "",
        "showHeader": false,
        "lineColor": "#30363d",
        "lineThickness": 2
      }
    },
    {
      "id": "widget-22",
      "type": "auth-status",
      "x": 460,
      "y": 120,
      "width": 240,
      "height": 140,
      "properties": {
        "title": "Auth Type",
        "endpoint": "/api/status",
        "refreshInterval": 30,
        "showHeader": true
      }
    },
    {
      "id": "widget-23",
      "type": "openclaw-release",
      "x": 720,
      "y": 120,
      "width": 280,
      "height": 140,
      "properties": {
        "title": "OpenClaw Release",
        "openclawUrl": "",
        "refreshInterval": 3600,
        "showHeader": true,
        "widgetFontAdjust": 25
      }
    },
    {
      "id": "widget-30",
      "type": "rss-ticker",
      "x": 0,
      "y": 1000,
      "width": 1900,
      "height": 60,
      "properties": {
        "title": "RSS",
        "feedUrl": "https://magazine.sebastianraschka.com/feed",
        "maxItems": 10,
        "refreshInterval": 600
      }
    },
    {
      "id": "widget-31",
      "type": "lobsterboard-release",
      "x": 1020,
      "y": 120,
      "width": 240,
      "height": 140,
      "properties": {
        "title": "LobsterBoard",
        "refreshInterval": 3600,
        "widgetFontAdjust": 25
      }
    },
    {
      "id": "widget-38",
      "type": "cron-jobs",
      "x": 20,
      "y": 280,
      "width": 580,
      "height": 320,
      "properties": {
        "title": "Cron",
        "endpoint": "/api/cron",
        "columns": 2,
        "refreshInterval": 30
      }
    },
    {
      "id": "widget-39",
      "type": "system-log",
      "x": 620,
      "y": 280,
      "width": 640,
      "height": 720,
      "properties": {
        "title": "System Log",
        "endpoint": "/api/system-log",
        "maxLines": 50,
        "refreshInterval": 10
      }
    },
    {
      "id": "widget-40",
      "type": "activity-list",
      "x": 20,
      "y": 620,
      "width": 580,
      "height": 380,
      "properties": {
        "title": "Today",
        "endpoint": "/api/today",
        "maxItems": 10,
        "refreshInterval": 60
      }
    },
    {
      "id": "widget-41",
      "type": "cpu-memory",
      "x": 1280,
      "y": 120,
      "width": 200,
      "height": 140,
      "properties": {
        "title": "System",
        "endpoint": "/api/system",
        "refreshInterval": 5
      }
    },
    {
      "id": "widget-42",
      "type": "disk-usage",
      "x": 1500,
      "y": 120,
      "width": 200,
      "height": 140,
      "properties": {
        "title": "Disk",
        "path": "/",
        "endpoint": "/api/disk",
        "refreshInterval": 60
      }
    },
    {
      "id": "widget-43",
      "type": "network-speed",
      "x": 1720,
      "y": 120,
      "width": 180,
      "height": 140,
      "properties": {
        "title": "Network",
        "endpoint": "/api/network",
        "refreshInterval": 2
      }
    },
    {
      "id": "widget-44",
      "type": "uptime-monitor",
      "x": 1560,
      "y": 560,
      "width": 340,
      "height": 200,
      "properties": {
        "title": "Uptime",
        "services": "Website,API,Database",
        "refreshInterval": 30
      }
    },
    {
      "id": "widget-45",
      "type": "calendar",
      "x": 1280,
      "y": 560,
      "width": 260,
      "height": 200,
      "properties": {
        "title": "Calendar",
        "icalUrl": "",
        "maxEvents": 5,
        "refreshInterval": 300
      },
      "_templateNote": "\u26a0\ufe0f Configure this widget's settings after import"
    },
    {
      "id": "widget-48",
      "type": "todo-list",
      "x": 1280,
      "y": 780,
      "width": 260,
      "height": 220,
      "properties": {
        "title": "Todo"
      }
    },
    {
      "id": "widget-49",
      "type": "github-stats",
      "x": 1560,
      "y": 780,
      "width": 340,
      "height": 220,
      "properties": {
        "title": "GitHub",
        "username": "curbob",
        "refreshInterval": 300,
        "widgetFontAdjust": 25,
        "apiKey": "YOUR_API_KEY_HERE",
        "repo": "LobsterBoard"
      },
      "_templateNote": "\u26a0\ufe0f Configure this widget's settings after import"
    },
    {
      "id": "widget-50",
      "type": "quote-of-day",
      "x": 1280,
      "y": 280,
      "width": 620,
      "height": 180,
      "properties": {
        "title": "Quote",
        "maxLength": 0,
        "refreshInterval": 3600
      }
    },
    {
      "id": "widget-51",
      "type": "stock-ticker",
      "x": 1280,
      "y": 480,
      "width": 620,
      "height": 60,
      "properties": {
        "title": "Stocks",
        "symbol": "AAPL, MSFT, GOOGL, AMZN, TSLA",
        "apiKey": "YOUR_API_KEY_HERE",
        "apiKeyNote": "Get a free key at finnhub.io/register",
        "refreshInterval": 60
      },
      "_templateNote": "\u26a0\ufe0f Configure this widget's settings after import"
    }
  ]
}
```

## File: `templates/full-screen-focus-on-openclaw-systems/meta.json`
```json
{
  "id": "full-screen-focus-on-openclaw-systems",
  "name": "Full screen focus on OpenClaw systems",
  "description": "A full screen template that focuses on the Openclaw system log, activity and cron jobs",
  "author": "curbob",
  "tags": [
    "OpenClaw",
    "LobsterBoard"
  ],
  "canvasSize": "1920x1080",
  "widgetCount": 23,
  "widgetTypes": [
    {
      "type": "weather",
      "name": "Local Weather",
      "icon": "🌡️",
      "count": 1
    },
    {
      "type": "clock",
      "name": "Clock",
      "icon": "🕐",
      "count": 1
    },
    {
      "type": "text-header",
      "name": "Header / Text",
      "icon": "🔤",
      "count": 3
    },
    {
      "type": "horizontal-line",
      "name": "Horizontal Line",
      "icon": "➖",
      "count": 2
    },
    {
      "type": "auth-status",
      "name": "Auth Status",
      "icon": "🔐",
      "count": 1
    },
    {
      "type": "openclaw-release",
      "name": "OpenClaw Release",
      "icon": "🦞",
      "count": 1
    },
    {
      "type": "rss-ticker",
      "name": "RSS Ticker",
      "icon": "📡",
      "count": 1
    },
    {
      "type": "lobsterboard-release",
      "name": "LobsterBoard Release",
      "icon": "🦞",
      "count": 1
    },
    {
      "type": "cron-jobs",
      "name": "Cron Jobs",
      "icon": "⏰",
      "count": 1
    },
    {
      "type": "system-log",
      "name": "System Log",
      "icon": "🔧",
      "count": 1
    },
    {
      "type": "activity-list",
      "name": "Activity List",
      "icon": "📋",
      "count": 1
    },
    {
      "type": "cpu-memory",
      "name": "CPU / Memory",
      "icon": "💻",
      "count": 1
    },
    {
      "type": "disk-usage",
      "name": "Disk Usage",
      "icon": "💾",
      "count": 1
    },
    {
      "type": "network-speed",
      "name": "Network Speed",
      "icon": "🌐",
      "count": 1
    },
    {
      "type": "uptime-monitor",
      "name": "Uptime Monitor",
      "icon": "📡",
      "count": 1
    },
    {
      "type": "calendar",
      "name": "Calendar",
      "icon": "📅",
      "count": 1
    },
    {
      "type": "todo-list",
      "name": "Todo List",
      "icon": "✅",
      "count": 1
    },
    {
      "type": "github-stats",
      "name": "GitHub Stats",
      "icon": "🐙",
      "count": 1
    },
    {
      "type": "quote-of-day",
      "name": "Quote of Day",
      "icon": "💭",
      "count": 1
    },
    {
      "type": "stock-ticker",
      "name": "Stock Ticker",
      "icon": "📈",
      "count": 1
    }
  ],
  "requiresSetup": [],
  "preview": "preview.png"
}
```

## File: `templates/minimal-layout-for-10-inch-screen/config.json`
```json
{
  "canvas": {
    "width": 1280,
    "height": 800
  },
  "widgets": [
    {
      "id": "widget-1",
      "type": "weather",
      "x": 240,
      "y": 120,
      "width": 200,
      "height": 140,
      "properties": {
        "title": "Local Weather",
        "location": "Atlanta",
        "units": "F",
        "refreshInterval": 600,
        "showHeader": true
      }
    },
    {
      "id": "widget-3",
      "type": "clock",
      "x": 20,
      "y": 120,
      "width": 200,
      "height": 140,
      "properties": {
        "title": "Clock",
        "timezone": "local",
        "format24h": false
      }
    },
    {
      "id": "widget-12",
      "type": "text-header",
      "x": 20,
      "y": 20,
      "width": 400,
      "height": 50,
      "properties": {
        "title": "Lobster Board",
        "showHeader": false,
        "fontSize": 24,
        "fontColor": "#e6edf3",
        "textAlign": "left",
        "fontWeight": "bold"
      }
    },
    {
      "id": "widget-14",
      "type": "text-header",
      "x": 20,
      "y": 20,
      "width": 400,
      "height": 50,
      "properties": {
        "title": "Lobster Board",
        "showHeader": false,
        "fontSize": 24,
        "fontColor": "#e6edf3",
        "textAlign": "left",
        "fontWeight": "bold"
      }
    },
    {
      "id": "widget-15",
      "type": "horizontal-line",
      "x": 20,
      "y": 40,
      "width": 1220,
      "height": 60,
      "properties": {
        "title": "",
        "showHeader": false,
        "lineColor": "#30363d",
        "lineThickness": 2
      }
    },
    {
      "id": "widget-16",
      "type": "text-header",
      "x": 20,
      "y": 20,
      "width": 400,
      "height": 50,
      "properties": {
        "title": "Lobster Board",
        "showHeader": false,
        "showBorder": false,
        "fontSize": 24,
        "fontColor": "#e6edf3",
        "textAlign": "left",
        "fontWeight": "bold"
      }
    },
    {
      "id": "widget-18",
      "type": "horizontal-line",
      "x": 20,
      "y": 40,
      "width": 1240,
      "height": 60,
      "properties": {
        "title": "",
        "showHeader": false,
        "lineColor": "#30363d",
        "lineThickness": 2
      }
    },
    {
      "id": "widget-22",
      "type": "auth-status",
      "x": 460,
      "y": 120,
      "width": 240,
      "height": 140,
      "properties": {
        "title": "Auth Type",
        "endpoint": "/api/status",
        "refreshInterval": 30,
        "showHeader": true
      }
    },
    {
      "id": "widget-23",
      "type": "openclaw-release",
      "x": 720,
      "y": 120,
      "width": 280,
      "height": 140,
      "properties": {
        "title": "OpenClaw Release",
        "openclawUrl": "",
        "refreshInterval": 3600,
        "showHeader": true,
        "widgetFontAdjust": 25
      }
    },
    {
      "id": "widget-30",
      "type": "rss-ticker",
      "x": 0,
      "y": 700,
      "width": 1260,
      "height": 60,
      "properties": {
        "title": "RSS",
        "feedUrl": "https://magazine.sebastianraschka.com/feed",
        "maxItems": 10,
        "refreshInterval": 600
      }
    },
    {
      "id": "widget-31",
      "type": "lobsterboard-release",
      "x": 1020,
      "y": 120,
      "width": 240,
      "height": 140,
      "properties": {
        "title": "LobsterBoard",
        "refreshInterval": 3600,
        "widgetFontAdjust": 25
      }
    },
    {
      "id": "widget-38",
      "type": "cron-jobs",
      "x": 20,
      "y": 280,
      "width": 580,
      "height": 200,
      "properties": {
        "title": "Cron",
        "endpoint": "/api/cron",
        "columns": 2,
        "refreshInterval": 30
      }
    },
    {
      "id": "widget-39",
      "type": "system-log",
      "x": 620,
      "y": 280,
      "width": 640,
      "height": 420,
      "properties": {
        "title": "System Log",
        "endpoint": "/api/system-log",
        "maxLines": 50,
        "refreshInterval": 10
      }
    },
    {
      "id": "widget-40",
      "type": "activity-list",
      "x": 20,
      "y": 500,
      "width": 580,
      "height": 200,
      "properties": {
        "title": "Today",
        "endpoint": "/api/today",
        "maxItems": 10,
        "refreshInterval": 60
      }
    }
  ]
}
```

## File: `templates/minimal-layout-for-10-inch-screen/meta.json`
```json
{
  "id": "minimal-layout-for-10-inch-screen",
  "name": "minimal layout for 10 inch screen",
  "description": "For a small static screen where thereisn't much space for many widgets",
  "author": "Curbob",
  "tags": [],
  "canvasSize": "1280x800",
  "widgetCount": 14,
  "widgetTypes": [
    {
      "type": "weather",
      "name": "Local Weather",
      "icon": "🌡️",
      "count": 1
    },
    {
      "type": "clock",
      "name": "Clock",
      "icon": "🕐",
      "count": 1
    },
    {
      "type": "text-header",
      "name": "Header / Text",
      "icon": "🔤",
      "count": 3
    },
    {
      "type": "horizontal-line",
      "name": "Horizontal Line",
      "icon": "➖",
      "count": 2
    },
    {
      "type": "auth-status",
      "name": "Auth Status",
      "icon": "🔐",
      "count": 1
    },
    {
      "type": "openclaw-release",
      "name": "OpenClaw Release",
      "icon": "🦞",
      "count": 1
    },
    {
      "type": "rss-ticker",
      "name": "RSS Ticker",
      "icon": "📡",
      "count": 1
    },
    {
      "type": "lobsterboard-release",
      "name": "LobsterBoard Release",
      "icon": "🦞",
      "count": 1
    },
    {
      "type": "cron-jobs",
      "name": "Cron Jobs",
      "icon": "⏰",
      "count": 1
    },
    {
      "type": "system-log",
      "name": "System Log",
      "icon": "🔧",
      "count": 1
    },
    {
      "type": "activity-list",
      "name": "Activity List",
      "icon": "📋",
      "count": 1
    }
  ],
  "requiresSetup": [],
  "preview": "preview.png"
}
```

