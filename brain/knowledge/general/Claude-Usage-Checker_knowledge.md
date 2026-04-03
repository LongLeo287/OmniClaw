---
id: claude-usage-checker-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:05.541308
---

# KNOWLEDGE EXTRACT: claude-usage-checker
> **Extracted on:** 2026-03-30 17:33:12
> **Source:** claude-usage-checker

---

## File: `content.js`
```javascript
/* Claude Usage Checker - Minimal UI */
'use strict';

// Simple logging
function Log(...args) {
    console.log('[Claude Usage Checker]', ...args);
}

// Sleep helper
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Floating Popup UI Manager with Real Usage API
class UsagePopup {
    constructor() {
        this.container = null;
        this.isMinimized = false;
        this.orgId = null;
    }

    async initialize() {
        // Get org ID from cookie
        this.orgId = this.getOrgIdFromCookie();
        if (!this.orgId) {
            Log('Could not find org ID');
            return;
        }

        // Create popup
        this.container = document.createElement('div');
        this.container.className = 'ut-floating-popup';
        this.container.id = 'ut-usage-popup';
        this.container.innerHTML = this.buildPopupHTML();
        document.body.appendChild(this.container);

        // Setup event listeners
        this.setupEventListeners();

        // Load saved state
        this.loadState();

        // Fetch usage data
        await this.fetchUsageData();

        // Auto refresh every 60 seconds
        setInterval(() => this.fetchUsageData(), 60000);

        Log('Popup initialized');
    }

    getOrgIdFromCookie() {
        const match = document.cookie.match(/lastActiveOrg=([^;]+)/);
        return match ? match[1] : null;
    }

    buildPopupHTML() {
        return `
			<div class="ut-popup-header">
				<div class="ut-popup-title">
					<span class="ut-popup-title-icon">
						<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
							<path d="M3 3v18h18"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/>
						</svg>
					</span>
					<span>Usage</span>
				</div>
				<div class="ut-popup-controls">
					<button class="ut-popup-btn ut-refresh-btn" title="Refresh">
						<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
							<path d="M23 4v6h-6M1 20v-6h6"/>
							<path d="M3.51 9a9 9 0 0114.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0020.49 15"/>
						</svg>
					</button>
					<button class="ut-popup-btn ut-minimize-btn" title="Minimize">−</button>
				</div>
			</div>
			<div class="ut-popup-content">
				<div class="ut-popup-section">
					<div class="ut-popup-usage-row">
						<span class="ut-popup-label">SESSION</span>
						<span class="ut-popup-percentage" id="ut-session-pct">--%</span>
					</div>
					<div class="ut-popup-progress-container">
						<div class="ut-popup-progress-bar" id="ut-session-bar" style="width: 0%"></div>
					</div>
					<div class="ut-popup-reset-row">
						<span class="ut-popup-reset-label">
							<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
								<circle cx="12" cy="12" r="10"/><polyline points="12,6 12,12 16,14"/>
							</svg>
							Resets in
						</span>
						<span class="ut-popup-reset-value" id="ut-session-reset">Loading...</span>
					</div>
				</div>
				<div class="ut-popup-section">
					<div class="ut-popup-usage-row">
						<span class="ut-popup-label">WEEKLY</span>
						<span class="ut-popup-percentage" id="ut-weekly-pct">--%</span>
					</div>
					<div class="ut-popup-progress-container">
						<div class="ut-popup-progress-bar" id="ut-weekly-bar" style="width: 0%"></div>
					</div>
					<div class="ut-popup-reset-row">
						<span class="ut-popup-reset-label">
							<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
								<circle cx="12" cy="12" r="10"/><polyline points="12,6 12,12 16,14"/>
							</svg>
							Resets in
						</span>
						<span class="ut-popup-reset-value" id="ut-weekly-reset">Loading...</span>
					</div>
				</div>
				<div class="ut-popup-footer">
					<span>From Brian Le</span>
				</div>
			</div>
		`;
    }

    setupEventListeners() {
        // Minimize button
        this.container.querySelector('.ut-minimize-btn').addEventListener('click', () => {
            this.toggleMinimize();
        });

        // Refresh button
        this.container.querySelector('.ut-refresh-btn').addEventListener('click', () => {
            this.fetchUsageData();
        });
    }

    toggleMinimize() {
        this.isMinimized = !this.isMinimized;
        this.container.classList.toggle('ut-minimized', this.isMinimized);
        this.container.querySelector('.ut-minimize-btn').textContent = this.isMinimized ? '+' : '−';
        this.saveState();
    }

    saveState() {
        localStorage.setItem('ut-popup-minimized', this.isMinimized ? '1' : '0');
    }

    loadState() {
        if (localStorage.getItem('ut-popup-minimized') === '1') {
            this.toggleMinimize();
        }
    }

    async fetchUsageData() {
        try {
            const response = await fetch(`https://claude.ai/api/organizations/${this.orgId}/usage`, {
                credentials: 'include'
            });

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }

            const data = await response.json();
            this.updateDisplay(data);
        } catch (error) {
            Log('Error fetching usage:', error);
        }
    }

    updateDisplay(data) {
        // Session (5-hour)
        if (data.five_hour) {
            const sessionPct = Math.round(data.five_hour.utilization || 0);
            const sessionPctEl = document.getElementById('ut-session-pct');
            const sessionBarEl = document.getElementById('ut-session-bar');

            sessionPctEl.textContent = `${sessionPct}%`;
            sessionBarEl.style.width = `${sessionPct}%`;
            document.getElementById('ut-session-reset').textContent = this.formatResetTime(data.five_hour.resets_at);

            // Add warning class if usage is high
            if (sessionPct >= 80) {
                sessionPctEl.classList.add('warning');
                sessionBarEl.classList.add('warning');
            } else {
                sessionPctEl.classList.remove('warning');
                sessionBarEl.classList.remove('warning');
            }
        }

        // Weekly (7-day)
        if (data.seven_day) {
            const weeklyPct = Math.round(data.seven_day.utilization || 0);
            const weeklyPctEl = document.getElementById('ut-weekly-pct');
            const weeklyBarEl = document.getElementById('ut-weekly-bar');

            weeklyPctEl.textContent = `${weeklyPct}%`;
            weeklyBarEl.style.width = `${weeklyPct}%`;
            document.getElementById('ut-weekly-reset').textContent = this.formatResetTime(data.seven_day.resets_at);

            // Add warning class if usage is high
            if (weeklyPct >= 80) {
                weeklyPctEl.classList.add('warning');
                weeklyBarEl.classList.add('warning');
            } else {
                weeklyPctEl.classList.remove('warning');
                weeklyBarEl.classList.remove('warning');
            }
        }
    }

    formatResetTime(isoString) {
        if (!isoString) return 'Unknown';

        const resetDate = new Date(isoString);
        const now = new Date();
        const diffMs = resetDate - now;

        if (diffMs <= 0) return 'Now';

        const diffHours = Math.floor(diffMs / (1000 * 60 * 60));
        const diffMins = Math.floor((diffMs % (1000 * 60 * 60)) / (1000 * 60));

        if (diffHours >= 24) {
            const days = Math.floor(diffHours / 24);
            return `${days}d ${diffHours % 24}h`;
        }
        return `${diffHours}h ${diffMins}m`;
    }
}

// Inject styles
function injectStyles() {
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = chrome.runtime.getURL('tracker-styles.css');
    document.head.appendChild(link);
}

// Initialize
(async () => {
    try {
        await sleep(1000);
        injectStyles();
        const popup = new UsagePopup();
        await popup.initialize();
    } catch (error) {
        console.error('[Claude Usage Checker] Failed to initialize:', error);
    }
})();
```

## File: `manifest.json`
```json
{
	"manifest_version": 3,
	"name": "Claude Usage Checker",
	"version": "1.0.0",
	"description": "Track your Claude.ai usage with a beautiful floating popup.",
	"content_scripts": [
		{
			"matches": [
				"https://claude.ai/*"
			],
			"js": [
				"content.js"
			],
			"css": [
				"tracker-styles.css"
			]
		}
	],
	"permissions": [
		"storage"
	],
	"host_permissions": [
		"*://claude.ai/*"
	],
	"web_accessible_resources": [
		{
			"resources": [
				"tracker-styles.css"
			],
			"matches": [
				"<all_urls>"
			]
		}
	],
	"icons": {
		"128": "icon128.png",
		"512": "icon512.png"
	},
	"action": {
		"default_icon": "icon128.png",
		"default_title": "Claude Usage Checker"
	}
}
```

## File: `README.md`
```markdown
# Claude Usage Checker

<div align="center">
  <img src="icon128.png" alt="Claude Usage Checker" width="128" height="128">
  
  **Track your Claude.ai usage with a beautiful floating popup**
</div>

---

## ✨ Features

- 📊 **Real-time Usage** - Displays actual usage from Claude's API
- ⏱️ **Session & Weekly Limits** - Shows 5-hour and 7-day quotas
- 🎨 **Dark Theme** - Clean, modern glassmorphism design
- 🔒 **Privacy Focused** - No data collection, all local
- 🔄 **Auto Refresh** - Updates every 60 seconds

## 📸 Screenshot

<div align="center">
  <img src="Screenshot.png" alt="Screenshot" width="600">
</div>

## 🚀 Installation

1. Clone: `git clone https://github.com/0xAstroAlpha/Claude-Usage-Checker.git`
2. Go to `chrome://extensions/`
3. Enable **Developer mode**
4. Click **Load unpacked** → select the folder
5. Visit [claude.ai](https://claude.ai)

## 📁 Files

```
├── manifest.json       # Extension config
├── content.js          # Main script
├── tracker-styles.css  # Popup styling
├── icon128.png         # Icon
└── icon512.png         # Large icon
```

## 🔒 Privacy

- ✅ No external data collection
- ✅ No background scripts
- ✅ Only reads from Claude's API

---

<div align="center">
  Made by <b>Brian Le</b>
</div>
```

## File: `tracker-styles.css`
```css
/* ui-styles.css */

/* Base Components */
.ut-card {
    position: fixed;
    border-radius: 8px;
    padding: 12px;
    font-size: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    z-index: 99999;
    user-select: none;
}

.ut-header {
    padding: 8px;
    margin: -12px -12px 8px -12px;
    cursor: move;
}

.ut-container {
    display: flex;
    flex-direction: column;
    margin-bottom: 8px;
}

.ut-row {
    display: flex;
    align-items: center;
    gap: 8px;
}

.ut-section {
    margin-bottom: 12px;
}

/* All inputs get the same treatment */
.ut-input {
    padding: 6px;
    border-radius: 4px;
    margin-bottom: 12px;
}

/* All buttons get the same treatment */
.ut-button {
    border: none;
    border-radius: 4px;
    cursor: pointer;
    padding: 6px 12px;
    transition: all 300ms cubic-bezier(0.165, 0.85, 0.45, 1);
}

.ut-button:active {
    transform: scale(0.95);
}

.ut-button-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    height: 32px;
    width: 32px;
    border-radius: 6px;
    padding: 0;
}

/* Close button is just positioned */
.ut-close {
    position: absolute;
    top: 0px;
    right: 8px;
}

/* Progress bars always the same */
.ut-progress {
    height: 6px;
    border-radius: 3px;
    overflow: hidden;
    width: 100%;
    user-select: none;
}

.ut-progress-bar {
    width: 0%;
    height: 100%;
    transition: width 0.3s ease, background-color 0.3s ease;
}


.ut-text-lg {
    font-size: 14px;
}

/* Common utilities */
.ut-label {
    display: block;
    margin-bottom: 8px;
}

.ut-link {
    text-decoration: underline;
    cursor: pointer;
}

.ut-tooltip {
    position: fixed;
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 12px;
    opacity: 0;
    transition: opacity 0.2s;
    pointer-events: none;
    white-space: nowrap;
    z-index: 9999;
    user-select: none;
}

.ut-tooltip-trigger {
    -webkit-touch-callout: none;
    /* Disable callout on long press */
    -webkit-user-select: none;
    /* Disable text selection */
    user-select: none;
}

.ut-content-box {
    padding: 8px;
    border-radius: 4px;
    overflow-y: auto;
}

/* Spacing utilities */
.ut-mb-0 {
    margin-bottom: 0;
}

.ut-mb-1 {
    margin-bottom: 4px;
}

.ut-mb-2 {
    margin-bottom: 8px;
}

.ut-mb-3 {
    margin-bottom: 12px;
}

/* Width utilities */
.ut-w-full {
    width: 100%;
}

.ut-w-auto {
    width: auto;
}

/* Flex utilities */
.ut-flex-1 {
    flex: 1;
}

.ut-flex-grow {
    flex-grow: 1;
}

.ut-justify-between {
    justify-content: space-between;
}

.ut-justify-center {
    justify-content: center;
}

.ut-items-center {
    align-items: center;
}

/* Text alignment */
.ut-text-left {
    text-align: left;
}

.ut-text-center {
    text-align: center;
}

.ut-text-right {
    text-align: right;
}

/* Display utilities */
.ut-block {
    display: block;
}

.ut-hidden {
    display: none;
}

/* Position utilities */
.ut-sticky {
    position: sticky;
    top: 0;
}

.ut-relative {
    position: relative;
}

/* Selection */
.ut-select-none {
    user-select: none;
}

.ut-select-text {
    user-select: text;
}

.ut-desktop-footer {
    font-size: 0.75rem;
    color: var(--text-400);
    border-top: 1px solid var(--border-400);
    text-align: center;
}

.ut-desktop-footer.ut-sidebar-footer {
    text-align: left;
    /*padding: 0 0.5rem 0.5rem 0.5rem;*/
}

/* ========================================
   GLASSMORPHISM FLOATING POPUP
   ======================================== */

/* Main Container */
.ut-floating-popup {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 280px;
    background: rgba(20, 20, 25, 0.95);
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 16px;
    box-shadow:
        0 8px 32px rgba(0, 0, 0, 0.4),
        0 0 0 1px rgba(255, 255, 255, 0.05) inset;
    z-index: 99999;
    overflow: hidden;
    font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    animation: ut-glass-appear 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

@keyframes ut-glass-appear {
    from {
        opacity: 0;
        transform: translateY(30px) scale(0.95);
    }

    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

/* Minimized State - collapses content smoothly */
.ut-floating-popup.ut-minimized {
    width: auto;
    min-width: 100px;
    border-radius: 12px;
}

.ut-floating-popup.ut-minimized .ut-popup-content {
    max-height: 0;
    padding: 0 16px;
    opacity: 0;
    overflow: hidden;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.ut-floating-popup .ut-popup-content {
    max-height: 500px;
    opacity: 1;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.ut-floating-popup.ut-minimized .ut-popup-header {
    border-bottom: none;
    padding: 10px 12px;
}

/* Header */
.ut-popup-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 14px 16px;
    background: rgba(255, 255, 255, 0.05);
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    user-select: none;
}

.ut-popup-title {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 14px;
    font-weight: 600;
    color: rgba(255, 255, 255, 0.95);
    letter-spacing: -0.01em;
}

.ut-popup-title-icon {
    width: 28px;
    height: 28px;
    background: linear-gradient(135deg, #8b5cf6 0%, #a78bfa 50%, #c4b5fd 100%);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    box-shadow: 0 4px 12px rgba(139, 92, 246, 0.4);
}

.ut-popup-controls {
    display: flex;
    gap: 6px;
}

.ut-popup-btn {
    width: 28px;
    height: 28px;
    border: none;
    background: rgba(255, 255, 255, 0.08);
    border-radius: 8px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    color: rgba(255, 255, 255, 0.6);
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    backdrop-filter: blur(4px);
}

.ut-popup-btn:hover {
    background: rgba(255, 255, 255, 0.15);
    color: rgba(255, 255, 255, 0.95);
    transform: scale(1.05);
}

.ut-popup-btn:active {
    transform: scale(0.95);
}

/* Content Area */
.ut-popup-content {
    padding: 16px;
}

/* Usage Sections */
.ut-popup-section {
    position: relative;
    margin-bottom: 14px;
    padding: 12px;
    background: rgba(255, 255, 255, 0.03);
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.06);
    transition: all 0.2s ease;
}

.ut-popup-section:last-child {
    margin-bottom: 0;
}

.ut-popup-section:hover {
    background: rgba(255, 255, 255, 0.06);
    border-color: rgba(255, 255, 255, 0.12);
}

/* Usage Row */
.ut-popup-usage-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 10px;
}

.ut-popup-label {
    font-size: 10px;
    font-weight: 600;
    color: rgba(255, 255, 255, 0.5);
    text-transform: uppercase;
    letter-spacing: 1.2px;
}

.ut-popup-percentage {
    font-size: 24px;
    font-weight: 700;
    background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: -0.03em;
}

.ut-popup-percentage.warning {
    background: linear-gradient(135deg, #f87171 0%, #fb923c 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* Progress Bar */
.ut-popup-progress-container {
    height: 6px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 3px;
    overflow: hidden;
    margin-bottom: 10px;
}

.ut-popup-progress-bar {
    height: 100%;
    background: linear-gradient(90deg, #60a5fa 0%, #a78bfa 100%);
    border-radius: 3px;
    transition: width 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 0 12px rgba(96, 165, 250, 0.5);
}

.ut-popup-progress-bar.warning {
    background: linear-gradient(90deg, #f87171 0%, #fb923c 100%);
    box-shadow: 0 0 12px rgba(248, 113, 113, 0.5);
}

/* Reset Time Row */
.ut-popup-reset-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 11px;
}

.ut-popup-reset-label {
    color: rgba(255, 255, 255, 0.4);
    display: flex;
    align-items: center;
    gap: 4px;
}

.ut-popup-reset-value {
    color: rgba(255, 255, 255, 0.8);
    font-weight: 500;
    font-variant-numeric: tabular-nums;
}

/* Footer - Credit */
.ut-popup-footer {
    text-align: center;
    padding-top: 12px;
    margin-top: 8px;
    border-top: 1px solid rgba(255, 255, 255, 0.06);
    font-size: 10px;
    color: rgba(255, 255, 255, 0.3);
}

/* Hover glow effect */
.ut-floating-popup::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg,
            transparent 0%,
            rgba(139, 92, 246, 0.5) 50%,
            transparent 100%);
    opacity: 0;
    transition: opacity 0.3s ease;
}

.ut-floating-popup:hover::before {
    opacity: 1;
}
```

