---
id: repo-fetched-chrome-auto-pip-124700
type: knowledge
owner: OA
registered_at: 2026-04-05T04:12:20.345129
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_chrome-auto-pip_124700

## Assimilation Report
Auto-cloned repository: FETCHED_chrome-auto-pip_124700

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "auto-pip-extension-tests",
  "private": true,
  "version": "1.0.0",
  "devDependencies": {
    "@playwright/test": "^1.42.1"
  },
  "scripts": {
    "test:e2e": "playwright test",
    "test:e2e:ui": "playwright test --ui"
  }
}

```

### File: README.md
```md
# Chrome Automatic Picture-in-Picture (PiP)

[Chrome Web Store](https://chromewebstore.google.com/detail/automatic-picture-in-pict/dmjccoaplbldlhhljlcldhaciadfhkcj)

Free and open source.

Changelog: [CHANGELOG.md](CHANGELOG.md)

Automatically enables Picture-in-Picture when switching tabs like Arc or Firefox or Zen.

Also enables Picture-in-Picture when switching windows or applications.

Includes one click activation of Picture-in-Picture through plugin icon.
<br><br>
Enjoying the extension?

[![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=000000)](https://buymeacoffee.com/apotenza)

## Installation

1. **Enable the browser flag (REQUIRED)**

   1. Go to `about://flags` and search for `auto-picture-in-picture-for-video-playback`
   2. Set the flag to **Enabled**
   3. Restart your browser

2. **Install the extension** 

   **Option A: Chrome Web Store (Recommended)**
   
   [Chrome Web Store](https://chromewebstore.google.com/detail/automatic-picture-in-pict/dmjccoaplbldlhhljlcldhaciadfhkcj)
   
   **Option B: Manual Installation (GitHub Release ZIP)**

   1. Download the latest release ZIP from: https://github.com/apotenza92/chrome-auto-pip/releases
   2. Extract/unzip the downloaded file to a folder on your computer
   3. Open Chrome and go to `chrome://extensions` (or `brave://extensions` / `edge://extensions`)
   4. Enable **Developer mode** (toggle in the top right)
   5. Click **Load unpacked**
   6. Select the extracted folder (the one that contains `manifest.json`)
   7. The extension should now appear in your extensions list and toolbar

## Usage

### Default Automatic Behavior (Fresh Install)
- `Auto PiP on Tab Switch`: **On**
- `Auto PiP on Window Switch`: **Off**
- `Auto PiP on App Switch`: **Off**

With default settings, switching tabs away from a playing video will automatically enter PiP.

### Manual PiP
Click the extension icon to immediately activate PiP on the current video

### Open Extension Options
1. Right-click the extension icon in the Chrome toolbar and click **Options**
2. Or open `chrome://extensions`, open this extension's **Details**, and click **Extension options**

Chrome docs reference: [Options page](https://developer.chrome.com/docs/extensions/develop/ui/options-page)

### Window/App Switch Modes
- If you enable **Auto PiP on Window Switch** or **Auto PiP on App Switch**, the extension will create temporary `about:blank` helper tabs by design.
- This is required for how the current focus-change detection works when handling aggressive window/app switching behavior.
- It can trigger in undesirable circumstances (for example, opening other extension popups) because Chrome reports browser focus loss as `WINDOW_ID_NONE` and does not reliably expose whether that focus change came from a popup/overlay.

#### Why The Extension Works This Way
- Tab switching is straightforward because Chrome gives direct tab activation events.
- App/window switching is harder: extensions only get high-level focus changes from `chrome.windows.onFocusChanged`.
- For app switches, Chrome can report `WINDOW_ID_NONE`, which means "Chrome lost focus", but it does not say *what* got focus instead.
- To keep PiP behavior consistent in those modes, the extension creates a temporary `about:blank` helper tab to force a reliable focus transition path that Chrome can observe.

#### Chrome Extension Limitations
- There is no reliable API signal that says "this focus loss came from another extension popup/overlay."
- Because of that, some interactions that are not true app switching can still look like app/window switching to the extension.
- This is a platform-level limitation of the currently available extension focus APIs, not a site-specific bug.

References:
- [Chrome windows API](https://developer.chrome.com/docs/extensions/reference/api/windows)
- [Auto PiP MediaSession behavior](https://developer.chrome.com/blog/automatic-picture-in-picture-media-playback)

### Disabled Sites
Auto-PiP is disabled on specific domains. You can add or remove domains in the Options page. Use a `*.` prefix to include subdomains (e.g. `*.zoom.us`).

Default disabled sites:
- `meet.google.com`
- `*.zoom.us`
- `zoom.com`
- `teams.microsoft.com`
- `teams.live.com`
- `*.slack.com`
- `*.discord.com`

## How It Works

This extension uses Chrome's [MediaSession API](https://developer.chrome.com/blog/automatic-picture-in-picture-media-playback) to register an `enterpictureinpicture` handler and sets the `autopictureinpicture` attribute on videos. When you switch tabs away from a playing video, Chrome's built-in auto-PiP feature (enabled via the flag) automatically triggers PiP.

## Site Compatibility

### Sites That Work Seamlessly
Most video sites work automatically, including:
- YouTube
- Netflix
- Vimeo
- And many others where the video is in the main page frame

### Sites Requiring User Interaction

**Twitch** and similar sites that embed video players in iframes may require a click or keyboard input on the page before auto-PiP will activate when switching tabs.

**Why?** Chrome's auto-PiP has a security requirement that [media must be in the top frame](https://developer.chrome.com/blog/automatic-picture-in-picture-media-playback). When the video is in an iframe (like Twitch's player), Chrome requires a recent user gesture to allow PiP.

**Workaround:** Simply click anywhere on the Twitch page before switching tabs. After that initial interaction, auto-PiP should work. If you return to the tab and want to switch away again, another click may be needed.

> **Note:** Firefox's built-in auto-PiP feature doesn't have this limitation because it's implemented at the browser level with elevated privileges, not as an extension subject to web security policies.

## Requirements

- Chrome 134+ or compatible Chromium browser
- The `auto-picture-in-picture-for-video-playback` flag must be enabled

## Store Description Copy

Use this updated text for the Chrome Web Store long description:

Automatically enables Picture-in-Picture when switching tabs, with one-click manual PiP from the toolbar icon.

Default behavior for new installs:
- Auto PiP on Tab Switch: On
- Auto PiP on Window Switch: Off
- Auto PiP on App Switch: Off

Window Switch and App Switch modes are available in Extension Options as opt-in aggressive modes.

Important: when Window Switch or App Switch is enabled, the extension will create temporary `about:blank` helper tabs by design. This is required so focus transitions can be detected reliably for those modes.

In some undesirable circumstances (for example opening other extension popups), this behavior can still trigger because Chrome reports browser focus loss as `WINDOW_ID_NONE` and does not reliably identify popup sources to extensions.

```

### File: AGENTS.md
```md
# AGENTS

This repo is a Chrome (MV3) extension. This file documents common project workflows for maintainers and automation/agents.

## Development

- Main extension code: `main.js`
- Options UI: `options.html`, `options.js`
- Content scripts: `scripts/`
- Manifest: `manifest.json`

## Tests

End-to-end tests use Playwright.

```bash
npm install
npm run test:e2e
```

## Releases (GitHub Release ZIPs)

This project publishes a downloadable ZIP asset on GitHub Releases so users can install manually via **Load unpacked**.

### How it works

- Workflow: `.github/workflows/release.yml`
- Trigger: pushing a tag that matches `v*.*.*` (example: `v1.6.3`)
- The workflow:
  1. Derives the version from the tag.
  2. Verifies `manifest.json` `version` matches the tag version.
  3. Extracts the matching section from `CHANGELOG.md` and uses it as the GitHub Release notes.
  4. Builds `chrome-auto-pip-<version>.zip` containing the extension runtime files.
  5. Creates/updates the GitHub Release and uploads the ZIP as a release asset.

### Publish a release

1. Update `manifest.json` version (and `CHANGELOG.md`).
2. Commit and push to `main`.
3. Create and push a tag:

```bash
git tag v<version>
git push origin v<version>
```

Example:

```bash
git tag v1.6.3
git push origin v1.6.3
```

After the workflow finishes, the release page will contain `chrome-auto-pip-<version>.zip`.

### Backfill/update existing GitHub Releases

If older versions don't have GitHub Releases (or the release body needs to be updated to match `CHANGELOG.md`), run the workflow:

- Actions → **Backfill GitHub Releases** → Run workflow
- Optional input: `versions` as a comma-separated list (e.g. `1.6.2,1.6.1`). Leave blank to process all versions in `CHANGELOG.md`.

This will create/update releases and upload the matching ZIP assets.

```

### File: CHANGELOG.md
```md
# Changelog

## [1.6.3] - 2026-02-14

### Fixed
- Reduced false positives for **Auto PiP on App Switch** by debouncing transient `chrome.windows.WINDOW_ID_NONE` focus events.
- Reduced "ghost" helper tabs by:
  - Creating helper tabs as `about:blank#chrome-auto-pip-helper` (so they are identifiable).
  - Best-effort cleanup of orphaned helper tabs when a window regains focus (covers MV3 service worker restarts that lose in-memory state).
- Improved helper-tab cleanup robustness by retrying `chrome.tabs.remove()` more times when Chrome reports the tab is temporarily busy.

### Changed
- Helper tab URL is now `about:blank#chrome-auto-pip-helper` (instead of plain `about:blank`).

### Tests
- Made e2e tests self-contained by serving a local MP4 fixture with proper Range support.

## [1.6.2] - 2026-02-12

### Changed
- Safer defaults and clearer UX copy around aggressive modes:
  - **Auto PiP on Tab Switch**: On
  - **Auto PiP on Window Switch**: Off
  - **Auto PiP on App Switch**: Off
- Refined Chrome Web Store description/summary copy.

## [1.6.1] - 2026-02-06

### Changed
- Removed the unused `webNavigation` permission.

### Internal
- Adjusted Chrome Web Store release workflows (removed CI release workflow; added manual workflow).

## [1.6.0] - 2026-02-04

### Removed
- Removed Document PiP support.

### Added
- Added per-site auto-PiP exclusions (blocklist) to avoid conferencing/app conflicts.

### Fixed
- Improved fallback cleanup reliability and default PiP sizing.

### Docs
- Updated README and store description to clarify window/app switch behavior and limitations.

## [1.5.0] - 2026-01-28

### Added
- Added Document PiP sizing support.

### Fixed
- Added/improved window-blur fallback cleanup.

## [1.4.0] - 2026-01-08

### Fixed
- Fixed Auto-PiP option not being respected in already-open tabs.

## [1.3.0] - 2025-12-08

### Changed
- Refactored and consolidated shared utilities to improve auto-PiP reliability.

### Fixed
- Improved Twitch support.
- Fixed settings changes not being applied to currently open tabs.

### Added
- Added support for swapping workspaces in browsers like Vivaldi.

## [1.2.0] - 2025-10-15

### Fixed
- Fixed `check-video` logic and improved multi-frame/all-frames handling.
- Improved PiP reliability by force-enabling PiP in cases where pages temporarily disable it.

### Changed
- Updated icons/assets.

## [1.1.0] - 2025-08-24

### Fixed
- Fixed detection of videos in new windows and autoplaying scenarios.
- Fixed manual PiP activation to respect the user option.

## [1.0.0] - 2025-07-17

### Fixed
- Fixed user disabling Auto PiP not being applied to currently open tabs.

### Docs
- General documentation updates and privacy policy added.

## [0.1.0] - 2025-06-13

### Added
- Initial release.
- Auto PiP on tab switch via MediaSession/auto-PiP registration.
- Manual PiP trigger from the toolbar action.
- Options page and basic settings persistence.
- Early error-handling and restricted-URL safeguards.

```

### File: main.js
```js
var currentTab = 0;
var prevTab = null;
var targetTab = null;
var targetWindowId = null;

// Track last focus-change events.
// Note: Chrome may report WINDOW_ID_NONE for transient focus changes (e.g. extension UI)
// so we also keep a "best known" normal window id.
var lastFocusedWindowId = null;
var lastFocusedNormalWindowId = null;

// about:blank helper tab management (used for window/app switch modes)
const FALLBACK_HELPER_URL = 'about:blank#chrome-auto-pip-helper';
const APP_SWITCH_DEBOUNCE_MS = 250;
var pendingAppSwitchTimer = null;
var pendingAppSwitchFromWindowId = null;

var blurFallbackWindowId = null;
var blurFallbackOriginalTabId = null;
var blurFallbackTempTabId = null;
var pipActiveTab = null; // Track which tab has active PiP
var autoPipOnTabSwitch = true; // Default to enabled
var autoPipOnWindowSwitch = false; // Default to disabled
var autoPipOnAppSwitch = false; // Default to disabled
const DEFAULT_BLOCKED_SITES = [
  'meet.google.com',
  '*.zoom.us',
  'zoom.com',
  'teams.microsoft.com',
  'teams.live.com',
  '*.slack.com',
  '*.discord.com'
];
var autoPipSiteBlocklist = DEFAULT_BLOCKED_SITES.slice();
var log = []
var settingsLoaded = false;
var settingsReady = null;

function removeTabWithRetry(tabId, context, attempt = 0) {
  if (tabId == null) return;

  chrome.tabs.remove(tabId, () => {
    if (chrome.runtime.lastError) {
      const message = chrome.runtime.lastError.message || '';

      const isBusy = message.includes('Tabs cannot be edited right now');
      if (isBusy && attempt < 12) {
        setTimeout(() => {
          removeTabWithRetry(tabId, context, attempt + 1);
        }, 150 * (attempt + 1));
      }
      return;
    }
  });
}


// Helper function to check if a URL is restricted (chrome://, chrome-extension://, etc.)
function isRestrictedUrl(url) {
  if (!url) return true;
  const restrictedProtocols = ['chrome:', 'chrome-extension:', 'chrome-search:', 'chrome-devtools:', 'moz-extension:', 'edge:', 'about:'];
  return restrictedProtocols.some(protocol => url.startsWith(protocol));
}

function normalizeHostEntry(value) {
  if (typeof value !== 'string') return null;
  let input = value.trim().toLowerCase();
  if (!input) return null;

  let wildcard = false;
  if (input.startsWith('*.')) {
    wildcard = true;
    input = input.slice(2);
  }

  let hostname = '';
  try {
    const url = input.includes('://') ? new URL(input) : new URL(`https://${input}`);
    hostname = url.hostname.toLowerCase();
  } catch (_) {
    hostname = input.split('/')[0].split('?')[0].split('#')[0];
  }

  hostname = hostname.split(':')[0].replace(/^\.+|\.+$/g, '');
  if (!hostname) return null;
  return wildcard ? `*.${hostname}` : hostname;
}

function normalizeBlocklist(entries) {
  if (!Array.isArray(entries)) return null;
  const normalized = [];
  entries.forEach((entry) => {
    const value = normalizeHostEntry(entry);
    if (!value) return;
    if (!normalized.includes(value)) {
      normalized.push(value);
    }
  });
  return normalized;
}

function getHostnameFromUrl(url) {
  if (!url || isRestrictedUrl(url)) return null;
  try {
    return new URL(url).hostname.toLowerCase();
  } catch (_) {
    return null;
  }
}

function isHostBlocked(hostname) {
  if (!hostname) return false;
  const patterns = Array.isArray(autoPipSiteBlocklist) ? autoPipSiteBlocklist : [];
  for (let i = 0; i < patterns.length; i++) {
    const pattern = patterns[i];
    if (!pattern || typeof pattern !== 'string') continue;
    if (pattern.startsWith('*.')) {
      const suffix = pattern.slice(2);
      if (!suffix) continue;
      if (hostname === suffix || hostname.endsWith(`.${suffix}`)) return true;
    } else {
      if (hostname === pattern) return true;
      if (hostname === `www.${pattern}`) return true;
    }
  }
  return false;
}

function isAutoPipAllowedUrl(url) {
  const hostname = getHostnameFromUrl(url);
  if (!hostname) return false;
  return !isHostBlocked(hostname);
}

function isAutoPipAllowedTab(tab) {
  if (!tab || !tab.url) return false;
  return isAutoPipAllowedUrl(tab.url);
}

// Small helpers to reduce repetition
function isValidTab(tab) {
  return !!(tab && tab.url && !isRestrictedUrl(tab.url));
}

function hasAnyFrameTrue(results) {
  return Array.isArray(results) && results.some(frameResult => frameResult && frameResult.result);
}

function isAnyAutoPipEnabled() {
  return autoPipOnTabSwitch || autoPipOnWindowSwitch || autoPipOnAppSwitch;
}

function updateTargetWindow(tabId) {
  if (tabId == null) {
    targetWindowId = null;
    return;
  }
  chrome.tabs.get(tabId, (tab) => {
    if (chrome.runtime.lastError || !tab) return;
    targetWindowId = tab.windowId;
  });
}

function setTargetTab(tabId) {
  targetTab = tabId;
  updateTargetWindow(tabId);
}

function clearBlurFallback() {
  blurFallbackWindowId = null;
  blurFallbackOriginalTabId = null;
  blurFallbackTempTabId = null;
}

function cancelPendingAppSwitch() {
  if (pendingAppSwitchTimer != null) {
    clearTimeout(pendingAppSwitchTimer);
  }
  pendingAppSwitchTimer = null;
  pendingAppSwitchFromWindowId = null;
}

function cleanupFocusedHelperTab(windowId) {
  if (windowId == null) return;
  const isNone = chrome.windows && chrome.windows.WINDOW_ID_NONE;
  if (windowId === isNone) return;

  chrome.tabs.query({ active: true, windowId }, (tabs) => {
    const activeTab = tabs && tabs.length > 0 ? tabs[0] : null;
    if (!activeTab || !activeTab.id) return;
    if (activeTab.url !== FALLBACK_HELPER_URL) return;
    removeTabWithRetry(activeTab.id, 'helperTabCleanup');
  });
}

function scheduleDebouncedAppSwitch(fromWindowId, handler) {
  if (fromWindowId == null) return;
  const isNone = chrome.windows.WINDOW_ID_NONE;
  if (fromWindowId === isNone) return;

  // Debounce to avoid false positives when Chrome briefly reports WINDOW_ID_NONE
  // (e.g. some extension popups/overlays, omnibox UI transitions, etc.).
  cancelPendingAppSwitch();
  pendingAppSwitchFromWindowId = fromWindowId;

  pendingAppSwitchTimer = setTimeout(() => {
    pendingAppSwitchTimer = null;

    const stillNone = lastFocusedWindowId === chrome.windows.WINDOW_ID_NONE;
    const effectiveFromWindowId = pendingAppSwitchFromWindowId;
    pendingAppSwitchFromWindowId = null;

    if (!stillNone) return;
    handler(effectiveFromWindowId);
  }, APP_SWITCH_DEBOUNCE_MS);
}

function activateFallbackTab(windowId, originalTabId) {
  if (windowId == null || originalTabId == null) return;

  blurFallbackWindowId = windowId;
  blurFallbackOriginalTabId = originalTabId;

  const createBlankTab = (index) => {
    if (blurFallbackTempTabId != null) {
      removeTabWithRetry(blurFallbackTempTabId, 'activateFallbackTab');
      blurFallbackTempTabId = null;
    }

    const createOptions = { windowId, url: FALLBACK_HELPER_URL, active: true };
    if (typeof index === 'number') {
      createOptions.index = index;
    }

    chrome.tabs.create(createOptions, (tab) => {
      if (chrome.runtime.lastError || !tab) return;
      blurFallbackTempTabId = tab.id;
    });
  };

  chrome.tabs.get(originalTabId, (tab) => {
    if (chrome.runtime.lastError || !tab) {
      createBlankTab();
      return;
    }

    const nextIndex = typeof tab.index === 'number' ? tab.index + 1 : undefined;
    createBlankTab(nextIndex);
  });
}

// Script injection helpers - always inject utils.js first for shared functionality
function injectWithUtils(tabId, scripts, callback) {
  safeExecuteScript(tabId, ['./scripts/utils.js', './scripts/site-fixes.js', ...scripts], callback);
}

function injectTriggerAutoPiP(tabId, callback) {
  injectWithUtils(tabId, ['./scripts/trigger-auto-pip.js'], callback);
}

function injectCheckVideoScript(tabId, callback) {
  injectWithUtils(tabId, ['./scripts/check-video.js'], callback);
}

function injectCheckPlayingScript(tabId, callback) {
  injectWithUtils(tabId, ['./scripts/check-playing.js'], callback);
}

function injectExitPiPScript(tabId, callback) {
  injectWithUtils(tabId, ['./scripts/exit-pip.js'], callback);
}

function injectImmediatePiPScript(tabId, callback) {
  safeExecuteScript(tabId, ['./scripts/utils.js', './scripts/site-fixes.js', './scripts/immediate-pip.js'], callback, { allowBlocked: true });
}

function injectClearAutoPiPScript(tabId, callback) {
  safeExecuteScript(tabId, ['./scripts/clear-auto-pip.js'], callback);
}

function injectDisableAutoPiPScript(tabId, callback) {
  safeExecuteScript(tabId, ['./scripts/disable-auto-pip.js'], callback, { allowBlocked: true });
}

function registerAutoPipOnAllTabs() {
  chrome.tabs.query({}, (tabs) => {
    if (!tabs) return;
    tabs.forEach(tab => {
      if (!isValidTab(tab)) return;
      if (!isAutoPipAllowedTab(tab)) return;
      injectTriggerAutoPiP(tab.id, () => { });
    });
  });
}

function clearAutoPipOnAllTabs() {
  chrome.tabs.query({}, (tabs) => {
    if (!tabs) return;
    tabs.forEach(tab => {
      if (isRestrictedUrl(tab.url)) return;
      injectClearAutoPiPScript(tab.id, () => { });
    });
  });
}

function applyBlocklistToAllTabs() {
  chrome.tabs.query({}, (tabs) => {
    if (!tabs) return;
    tabs.forEach(tab => {
      if (!isValidTab(tab)) return;
      const allowed = isAutoPipAllowedTab(tab);
      if (!allowed) {
        injectDisableAutoPiPScript(tab.id, () => { });
        if (targetTab === tab.id) {
          setTargetTab(null);
        }
        if (pipActiveTab === tab.id) {
          pipActiveTab = null;
        }
        return;
      }
      if (isAnyAutoPipEnabled()) {
        injectTriggerAutoPiP(tab.id, () => { });
      }
    });
  });
}

async function migrateAutoPipSettings(syncData) {
  const hasOldSetting = typeof syncData.autoPipEnabled === 'boolean';
  const hasNewSettings =
    typeof syncData.autoPipOnTabSwitch === 'boolean' ||
    typeof syncData.autoPipOnWindowSwitch === 'boolean' ||
    typeof syncData.autoPipOnAppSwitch === 'boolean';

  if (hasOldSetting && !hasNewSettings) {
    const migrated = {
      autoPipOnTabSwitch: syncData.autoPipEnabled,
      autoPipOnWindowSwitch: syncData.autoPipEnabled,
      autoPipOnAppSwitch: syncData.autoPipEnabled
    };

    try { await chrome.storage.sync.set(migrated); } catch (_) { }
    try { await chrome.storage.local.set(migrated); } catch (_) { }
    return migrated;
  }

  return null;
}

// Helper function to load settings (local cache first, then sync authoritative)
async function loadSettings() {
  try {
    // Fast path: local cache for immediate availability
    try {
      const local = await chrome.storage.local.get([
        'autoPipOnTabSwitch',
        'autoPipOnWindowSwitch',
        'autoPipOnAppSwitch',
        'autoPipEnabled',
        'autoPipSiteBlocklist'
      ]);

      const hasLocalNew =
        typeof local.autoPipOnTabSwitch === 'boolean' ||
        typeof local.autoPipOnWindowSwitch === 'boolean' ||
        typeof local.autoPipOnAppSwitch === 'boolean';

      const localBlocklist = normalizeBlocklist(local.autoPipSiteBlocklist);
      if (localBlocklist) {
        autoPipSiteBlocklist = localBlocklist;
      }

      if (hasLocalNew) {
        if (typeof local.autoPipOnTabSwitch === 'boolean') {
          autoPipOnTabSwitch = local.autoPipOnTabSwitch;
        }
        if (typeof local.autoPipOnWindowSwitch === 'boolean') {
          autoPipOnWindowSwitch = local.autoPipOnWindowSwitch;
        }
        if (typeof local.autoPipOnAppSwitch === 'boolean') {
          autoPipOnAppSwitch = local.autoPipOnAppSwitch;
        }
      } else if (typeof local.autoPipEnabled === 'boolean') {
        autoPipOnTabSwitch = local.autoPipEnabled;
        autoPipOnWindowSwitch = local.autoPipEnabled;
        autoPipOnAppSwitch = local.autoPipEnabled;
      }
    } catch (e) {
    }

    // Authoritative: sync storage
      const result = await chrome.storage.sync.get([
        'autoPipOnTabSwitch',
        'autoPipOnWindowSwitch',
        'autoPipOnAppSwitch',
        'autoPipEnabled',
        'autoPipSiteBlocklist'
      ]);

    const migrated = await migrateAutoPipSettings(result);
    const effective = migrated || result;

    autoPipOnTabSwitch = typeof effective.autoPipOnTabSwitch === 'boolean'
        ? effective.autoPipOnTabSwitch
        : true;
    autoPipOnWindowSwitch = typeof effective.autoPipOnWindowSwitch === 'boolean'
      ? effective.autoPipOnWindowSwitch
      : false;
      autoPipOnAppSwitch = typeof effective.autoPipOnAppSwitch === 'boolean'
        ? effective.autoPipOnAppSwitch
        : false;

      const syncBlocklist = normalizeBlocklist(effective.autoPipSiteBlocklist);
      const localBlocklist = normalizeBlocklist(autoPipSiteBlocklist);
      const effectiveBlocklist = syncBlocklist || localBlocklist || DEFAULT_BLOCKED_SITES.slice();
      autoPipSiteBlocklist = effectiveBlocklist;

      if (!syncBlocklist) {
        try { await chrome.storage.sync.set({ autoPipSiteBlocklist: effectiveBlocklist }); } catch (_) { }
      }

    // Mirror to local cache (best-effort)
      try {
        await chrome.storage.local.set({
          autoPipOnTabSwitch,
          autoPipOnWindowSwitch,
          autoPipOnAppSwitch,
          autoPipSiteBlocklist
        });
      } catch (_) { }
  } catch (error) {
    // If sync is unavailable, ensure we have a sensible default and cache it
    autoPipOnTabSwitch = true;
    autoPipOnWindowSwitch = false;
    autoPipOnAppSwitch = false;
    autoPipSiteBlocklist = DEFAULT_BLOCKED_SITES.slice();
    try {
      await chrome.storage.local.set({
        autoPipOnTabSwitch,
        autoPipOnWindowSwitch,
        autoPipOnAppSwitch,
        autoPipSiteBlocklist
      });
    } catch (_) { }
  } finally {
    settingsLoaded = true;
    applyBlocklistToAllTabs();
  }
}

// Load settings on startup
settingsReady = loadSettings();

// Also refresh settings when the service worker wakes up with browser startup
if (chrome.runtime && chrome.runtime.onStartup) {
  chrome.runtime.onStartup.addListener(() => {
    loadSettings();
    // If tab switching is enabled, re-register handlers on all tabs at startup
    setTimeout(() => {
      if (!autoPipOnTabSwitch) return;
      registerAutoPipOnAllTabs();
    }, 300);
  });
}

// Set default settings on first install
chrome.runtime.onInstalled.addListener(async (details) => {
  if (details.reason === 'install') {
    try {
      await chrome.storage.sync.clear();
      await chrome.storage.local.clear();
      await chrome.storage.sync.set({
        autoPipOnTabSwitch: true,
        autoPipOnWindowSwitch: false,
        autoPipOnAppSwitch: false,
        autoPipSiteBlocklist: DEFAULT_BLOCKED_SITES.slice()
      });
      autoPipOnTabSwitch = true;
      autoPipOnWindowSwitch = false;
      autoPipOnAppSwitch = false;
      autoPipSiteBlocklist = DEFAULT_BLOCKED_SITES.slice();
    } catch (error) { }
    return;
  }

  if (details.reason === 'update') {
    try {
      await chrome.storage.sync.remove(['pipSize', 'pipSizeCustom', 'displayInfo']);
    } catch (_) { }
    try {
      await chrome.sto
... [TRUNCATED]
```

### File: manifest.json
```json
{
  "name": "Automatic Picture-in-Picture (PiP)",
  "description": "Auto Picture-in-Picture when you switch tabs like Arc and Firefox. Includes one-click PiP and optional window/app switch modes.",
  "version": "1.6.3",
  "manifest_version": 3,
  "icons": {
    "128": "assets/icon.png"
  },
  "background": {
    "service_worker": "main.js"
  },
  "action": {
    "default_title": "Picture-in-Picture",
    "default_icon": "assets/icon.png"
  },
  "options_ui": {
    "page": "options.html",
    "open_in_tab": false
  },
  "permissions": [
    "scripting",
    "storage",
    "tabs",
    "activeTab",
    "windows"
  ],
  "host_permissions": ["<all_urls>"],
  "web_accessible_resources": [
    {
      "resources": ["assets/*"],
      "matches": ["<all_urls>"]
    }
  ],
  "minimum_chrome_version": "134",
  "author": "Alex Potenza",
  "homepage_url": "https://github.com/apotenza92/chrome-auto-pip"
}

```

### File: options.html
```html
<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Settings</title>
        <style>
            body {
                font-family:
                    -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
                    sans-serif;
                margin: 0;
                padding: 20px;
                background: #f8f9fa;
                min-width: 400px;
            }

            .container {
                background: white;
                padding: 24px;
                border-radius: 8px;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            }

            h1 {
                margin: 0 0 24px 0;
                color: #1a1a1a;
                font-size: 24px;
                font-weight: 600;
            }

            .setting {
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 16px 0;
                border-bottom: 1px solid #e5e7eb;
            }

            .setting:last-child {
                border-bottom: none;
            }

            .setting.setting-vertical {
                flex-direction: column;
                align-items: flex-start;
                gap: 12px;
            }

            .setting-info {
                flex: 1;
            }

            .setting-title {
                font-size: 16px;
                font-weight: 500;
                color: #1a1a1a;
                margin: 0 0 4px 0;
            }

            .setting-description {
                font-size: 14px;
                color: #6b7280;
                margin: 0;
            }

            .setting-note {
                font-size: 14px;
                color: #6b7280;
                margin-top: 4px;
            }

            .setting-control {
                margin-left: 16px;
                align-self: center;
            }

            .toggle {
                position: relative;
                display: inline-block;
                width: 48px;
                height: 24px;
            }

            .toggle input {
                opacity: 0;
                width: 0;
                height: 0;
            }

            .slider {
                position: absolute;
                cursor: pointer;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background-color: #d1d5db;
                transition: 0.3s;
                border-radius: 24px;
            }

            .slider:before {
                position: absolute;
                content: "";
                height: 18px;
                width: 18px;
                left: 3px;
                bottom: 3px;
                background-color: white;
                transition: 0.3s;
                border-radius: 50%;
            }

            input:checked + .slider {
                background-color: #3b82f6;
            }

            input:checked + .slider:before {
                transform: translateX(24px);
            }

            select {
                padding: 8px 12px;
                border: 1px solid #d1d5db;
                border-radius: 6px;
                background: white;
                font-size: 14px;
                color: #1a1a1a;
                cursor: pointer;
                min-width: 80px;
            }

            select:focus {
                outline: none;
                border-color: #3b82f6;
                box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
            }

            .setting-controls {
                width: 100%;
                display: flex;
                flex-direction: column;
                gap: 12px;
            }

            .site-row {
                display: grid;
                grid-template-columns: 140px minmax(0, 220px) auto;
                align-items: center;
                gap: 8px;
                width: 100%;
                justify-content: start;
            }

            .site-row.site-row-manual {
                grid-template-columns: 140px minmax(0, 180px) auto;
            }

            #manualSiteInput {
                max-width: 119px;
                justify-self: start;
            }

            .site-row label {
                font-size: 14px;
                color: #374151;
            }

            .site-row input,
            .site-row select {
                width: 100%;
                min-width: 0;
            }

            .site-row input {
                padding: 8px 12px;
                border: 1px solid #d1d5db;
                border-radius: 6px;
                font-size: 14px;
                color: #1a1a1a;
            }

            .site-row input:focus {
                outline: none;
                border-color: #3b82f6;
                box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
            }

            .button {
                padding: 8px 12px;
                border: 1px solid #d1d5db;
                border-radius: 6px;
                background: #f9fafb;
                color: #111827;
                font-size: 14px;
                cursor: pointer;
                white-space: nowrap;
            }

            .button:hover {
                background: #f3f4f6;
            }

            .button:disabled {
                opacity: 0.6;
                cursor: not-allowed;
            }

            .button.button-small {
                padding: 6px 10px;
                font-size: 13px;
            }

            .site-list {
                width: 100%;
                display: flex;
                flex-direction: column;
                gap: 8px;
            }

            .site-item {
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 8px 12px;
                border: 1px solid #e5e7eb;
                border-radius: 6px;
                background: #f9fafb;
                font-size: 14px;
            }

            .site-item span {
                color: #111827;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>Options</h1>

            <div class="setting">
                <div class="setting-info">
                    <div class="setting-title">Auto PiP on Tab Switch</div>
                    <div class="setting-description">
                        Automatically activate PiP when switching to a different
                        tab in the same window.
                    </div>
                </div>
                <label class="toggle">
                    <input type="checkbox" id="autoPipOnTabSwitch" />
                    <span class="slider"></span>
                </label>
            </div>

            <div class="setting">
                <div class="setting-info">
                    <div class="setting-title">Auto PiP on Window Switch</div>
                    <div class="setting-description">
                        Automatically activate PiP when switching to a different
                        browser window.
                    </div>
                    <div class="setting-description">
                        <br />
                        This mode creates temporary <code>about:blank</code>
                        helper tabs.
                        <br />
                        <br />
                        This mode is aggressive and can trigger in undesired
                        circumstances.
                    </div>
                </div>
                <label class="toggle">
                    <input type="checkbox" id="autoPipOnWindowSwitch" />
                    <span class="slider"></span>
                </label>
            </div>

            <div class="setting">
                <div class="setting-info">
                    <div class="setting-title">Auto PiP on App Switch</div>
                    <div class="setting-description">
                        Automatically activate PiP when switching to a different
                        application.
                    </div>
                    <div class="setting-description">
                        <br />
                        This mode creates temporary <code>about:blank</code>
                        helper tabs.
                        <br />
                        <br />
                        This mode is aggressive and can trigger in undesired
                        circumstances.
                    </div>
                </div>
                <label class="toggle">
                    <input type="checkbox" id="autoPipOnAppSwitch" />
                    <span class="slider"></span>
                </label>
            </div>

            <div class="setting setting-vertical" id="blockedSitesSetting">
                <div class="setting-info">
                    <div class="setting-title">Disabled Sites</div>
                    <div class="setting-description">
                        Auto PiP will not run on these domains. Use a
                        <code>*.</code> prefix to include subdomains (e.g.
                        <code>*.zoom.us</code>).
                    </div>
                </div>
                <div class="setting-controls">
                    <div class="site-row">
                        <label for="currentSiteSelect">Add an open site</label>
                        <select id="currentSiteSelect">
                            <option value="">Select a site</option>
                        </select>
                        <button class="button" id="addCurrentSite">Add</button>
                    </div>
                    <div class="site-row site-row-manual">
                        <label for="manualSiteInput">Add manually</label>
                        <input id="manualSiteInput" type="text" />
                        <button class="button" id="addManualSite">Add</button>
                    </div>
                </div>
                <div class="site-list" id="blockedSitesList"></div>
            </div>
        </div>

        <script src="options.js"></script>
    </body>
</html>

```

### File: options.js
```js
// Options page JavaScript
document.addEventListener('DOMContentLoaded', async () => {
    const autoPipOnTabSwitchToggle = document.getElementById('autoPipOnTabSwitch');
    const autoPipOnWindowSwitchToggle = document.getElementById('autoPipOnWindowSwitch');
    const autoPipOnAppSwitchToggle = document.getElementById('autoPipOnAppSwitch');
    const currentSiteSelect = document.getElementById('currentSiteSelect');
    const addCurrentSiteButton = document.getElementById('addCurrentSite');
    const manualSiteInput = document.getElementById('manualSiteInput');
    const addManualSiteButton = document.getElementById('addManualSite');
    const blockedSitesList = document.getElementById('blockedSitesList');

    // Prevent user interaction until we load
    autoPipOnTabSwitchToggle.disabled = true;
    autoPipOnWindowSwitchToggle.disabled = true;
    autoPipOnAppSwitchToggle.disabled = true;
    currentSiteSelect.disabled = true;
    addCurrentSiteButton.disabled = true;
    manualSiteInput.disabled = true;
    addManualSiteButton.disabled = true;

    const DEFAULT_BLOCKED_SITES = [
        'meet.google.com',
        '*.zoom.us',
        'zoom.com',
        'teams.microsoft.com',
        'teams.live.com',
        '*.slack.com',
        '*.discord.com'
    ];
    let blockedSites = DEFAULT_BLOCKED_SITES.slice();

    function normalizeHostEntry(value) {
        if (typeof value !== 'string') return null;
        let input = value.trim().toLowerCase();
        if (!input) return null;

        let wildcard = false;
        if (input.startsWith('*.')) {
            wildcard = true;
            input = input.slice(2);
        }

        let hostname = '';
        try {
            const url = input.includes('://') ? new URL(input) : new URL(`https://${input}`);
            hostname = url.hostname.toLowerCase();
        } catch (_) {
            hostname = input.split('/')[0].split('?')[0].split('#')[0];
        }

        hostname = hostname.split(':')[0].replace(/^\.+|\.+$/g, '');
        if (!hostname) return null;
        return wildcard ? `*.${hostname}` : hostname;
    }

    function normalizeBlocklist(entries) {
        if (!Array.isArray(entries)) return null;
        const normalized = [];
        entries.forEach((entry) => {
            const value = normalizeHostEntry(entry);
            if (!value) return;
            if (!normalized.includes(value)) {
                normalized.push(value);
            }
        });
        return normalized;
    }

    function sortBlocklist(entries) {
        return entries.slice().sort((a, b) => a.localeCompare(b));
    }

    function setBlocklistControlsDisabled(disabled) {
        currentSiteSelect.disabled = disabled;
        addCurrentSiteButton.disabled = disabled;
        manualSiteInput.disabled = disabled;
        addManualSiteButton.disabled = disabled;
    }

    function renderBlockedSites() {
        blockedSitesList.innerHTML = '';

        if (!blockedSites.length) {
            const empty = document.createElement('div');
            empty.className = 'site-item';
            const label = document.createElement('span');
            label.textContent = 'No sites disabled';
            empty.appendChild(label);
            blockedSitesList.appendChild(empty);
            return;
        }

        const sorted = sortBlocklist(blockedSites);
        sorted.forEach((site) => {
            const row = document.createElement('div');
            row.className = 'site-item';

            const label = document.createElement('span');
            label.textContent = site;

            const removeButton = document.createElement('button');
            removeButton.className = 'button button-small';
            removeButton.textContent = 'Remove';
            removeButton.addEventListener('click', () => {
                const next = blockedSites.filter((entry) => entry !== site);
                saveBlocklist(next);
            });

            row.appendChild(label);
            row.appendChild(removeButton);
            blockedSitesList.appendChild(row);
        });
    }

    function isRestrictedUrl(url) {
        if (!url) return true;
        const restrictedProtocols = ['chrome:', 'chrome-extension:', 'chrome-search:', 'chrome-devtools:', 'moz-extension:', 'edge:', 'about:'];
        return restrictedProtocols.some(protocol => url.startsWith(protocol));
    }

    async function refreshCurrentSiteOptions() {
        try {
            const tabs = await new Promise(resolve => {
                chrome.tabs.query({}, resolve);
            });

            const hosts = new Set();
            (tabs || []).forEach((tab) => {
                if (!tab || !tab.url || isRestrictedUrl(tab.url)) return;
                try {
                    const host = new URL(tab.url).hostname.toLowerCase();
                    if (host) hosts.add(host);
                } catch (_) { }
            });

            const sortedHosts = Array.from(hosts).sort((a, b) => a.localeCompare(b));
            currentSiteSelect.innerHTML = '<option value="">Select a site</option>';
            sortedHosts.forEach((host) => {
                const option = document.createElement('option');
                option.value = host;
                option.textContent = host;
                currentSiteSelect.appendChild(option);
            });
        } catch (_) {
        }
    }

    async function saveBlocklist(next) {
        blockedSites = next;
        renderBlockedSites();
        setBlocklistControlsDisabled(true);
        try {
            await chrome.storage.sync.set({ autoPipSiteBlocklist: blockedSites });
            try { await chrome.storage.local.set({ autoPipSiteBlocklist: blockedSites }); } catch (_) { }
            try { chrome.runtime.sendMessage({ type: 'auto_pip_blocklist_updated', blocklist: blockedSites }); } catch (_) { }
        } catch (_) {
        } finally {
            setBlocklistControlsDisabled(false);
        }
    }

    async function migrateOldSettings(syncData, localData) {
        // Check if old autoPipEnabled exists and new settings don't
        const hasOldSetting = typeof syncData.autoPipEnabled === 'boolean';
        const hasNewSettings = 
            typeof syncData.autoPipOnTabSwitch === 'boolean' ||
            typeof syncData.autoPipOnWindowSwitch === 'boolean' ||
            typeof syncData.autoPipOnAppSwitch === 'boolean';

        if (hasOldSetting && !hasNewSettings) {
            // Migrate old setting to all three new settings
            const oldValue = syncData.autoPipEnabled;
            const migration = {
                autoPipOnTabSwitch: oldValue,
                autoPipOnWindowSwitch: oldValue,
                autoPipOnAppSwitch: oldValue
            };
            
            try {
                await chrome.storage.sync.set(migration);
                await chrome.storage.local.set(migration);
                console.log('[Auto PiP] Migrated old autoPipEnabled setting to new separate settings');
                return migration;
            } catch (e) {
                console.error('[Auto PiP] Failed to migrate settings:', e);
            }
        }
        return null;
    }

    async function loadSettingsWithFallback() {
        // Try fast local cache first
        try {
            const local = await chrome.storage.local.get([
                'autoPipOnTabSwitch', 'autoPipOnWindowSwitch', 'autoPipOnAppSwitch',
                'autoPipEnabled', 'autoPipSiteBlocklist'
            ]);
            
            // Try to migrate if needed
            const sync = await chrome.storage.sync.get([
                'autoPipEnabled',
                'autoPipOnTabSwitch',
                'autoPipOnWindowSwitch',
                'autoPipOnAppSwitch',
                'autoPipSiteBlocklist'
            ]);
            const migrated = await migrateOldSettings(sync, local);
            
            if (migrated) {
                autoPipOnTabSwitchToggle.checked = migrated.autoPipOnTabSwitch;
                autoPipOnWindowSwitchToggle.checked = migrated.autoPipOnWindowSwitch;
                autoPipOnAppSwitchToggle.checked = migrated.autoPipOnAppSwitch;
            } else {
                // Defaults for fresh installs: tab switch on, window/app switch off
                autoPipOnTabSwitchToggle.checked = typeof sync.autoPipOnTabSwitch === 'boolean' ? sync.autoPipOnTabSwitch : true;
                autoPipOnWindowSwitchToggle.checked = typeof sync.autoPipOnWindowSwitch === 'boolean' ? sync.autoPipOnWindowSwitch : false;
                autoPipOnAppSwitchToggle.checked = typeof sync.autoPipOnAppSwitch === 'boolean' ? sync.autoPipOnAppSwitch : false;
            }
            
            const localBlocklist = normalizeBlocklist(local.autoPipSiteBlocklist);
            if (localBlocklist) {
                blockedSites = localBlocklist;
                renderBlockedSites();
            }
        } catch (_) {
            // ignore
        }

        // Then authoritative sync storage
        try {
            const result = await chrome.storage.sync.get([
                'autoPipOnTabSwitch', 'autoPipOnWindowSwitch', 'autoPipOnAppSwitch',
                'autoPipEnabled', 'autoPipSiteBlocklist'
            ]);
            
            // Try migration again if needed
            const migrated = await migrateOldSettings(result, {});
            
            if (migrated) {
                autoPipOnTabSwitchToggle.checked = migrated.autoPipOnTabSwitch;
                autoPipOnWindowSwitchToggle.checked = migrated.autoPipOnWindowSwitch;
                autoPipOnAppSwitchToggle.checked = migrated.autoPipOnAppSwitch;
            } else {
                // Defaults for fresh installs: tab switch on, window/app switch off
                autoPipOnTabSwitchToggle.checked = typeof result.autoPipOnTabSwitch === 'boolean' ? result.autoPipOnTabSwitch : true;
                autoPipOnWindowSwitchToggle.checked = typeof result.autoPipOnWindowSwitch === 'boolean' ? result.autoPipOnWindowSwitch : false;
                autoPipOnAppSwitchToggle.checked = typeof result.autoPipOnAppSwitch === 'boolean' ? result.autoPipOnAppSwitch : false;
            }
            
            const syncBlocklist = normalizeBlocklist(result.autoPipSiteBlocklist);
            const localBlocklist = normalizeBlocklist(blockedSites);
            const effectiveBlocklist = syncBlocklist || localBlocklist || DEFAULT_BLOCKED_SITES.slice();
            blockedSites = effectiveBlocklist;
            renderBlockedSites();

            if (!syncBlocklist) {
                try {
                    await chrome.storage.sync.set({ autoPipSiteBlocklist: effectiveBlocklist });
                } catch (_) { }
            }

            // Keep local cache in sync for fast startup
            try { 
                await chrome.storage.local.set({ 
                    autoPipOnTabSwitch: autoPipOnTabSwitchToggle.checked,
                    autoPipOnWindowSwitch: autoPipOnWindowSwitchToggle.checked,
                    autoPipOnAppSwitch: autoPipOnAppSwitchToggle.checked,
                    autoPipSiteBlocklist: blockedSites
                }); 
            } catch (_) { }
        } catch (_) {
            // If sync is unavailable, ensure we have sensible defaults
            if (autoPipOnTabSwitchToggle.checked !== true && autoPipOnTabSwitchToggle.checked !== false) {
                autoPipOnTabSwitchToggle.checked = true;
            }
            if (autoPipOnWindowSwitchToggle.checked !== true && autoPipOnWindowSwitchToggle.checked !== false) {
                autoPipOnWindowSwitchToggle.checked = false;
            }
            if (autoPipOnAppSwitchToggle.checked !== true && autoPipOnAppSwitchToggle.checked !== false) {
                autoPipOnAppSwitchToggle.checked = false;
            }
            if (!blockedSites.length) {
                blockedSites = DEFAULT_BLOCKED_SITES.slice();
                renderBlockedSites();
            }
        }

        renderBlockedSites();
        await refreshCurrentSiteOptions();
    }

    await loadSettingsWithFallback();
    autoPipOnTabSwitchToggle.disabled = false;
    autoPipOnWindowSwitchToggle.disabled = false;
    autoPipOnAppSwitchToggle.disabled = false;
    setBlocklistControlsDisabled(false);

    async function saveSettings() {
        const tabSwitchEnabled = autoPipOnTabSwitchToggle.checked;
        const windowSwitchEnabled = autoPipOnWindowSwitchToggle.checked;
        const appSwitchEnabled = autoPipOnAppSwitchToggle.checked;

        // Disable controls while saving
        autoPipOnTabSwitchToggle.disabled = true;
        autoPipOnWindowSwitchToggle.disabled = true;
        autoPipOnAppSwitchToggle.disabled = true;

        try {
            // Write to sync (authoritative)
            await chrome.storage.sync.set({ 
                autoPipOnTabSwitch: tabSwitchEnabled,
                autoPipOnWindowSwitch: windowSwitchEnabled,
                autoPipOnAppSwitch: appSwitchEnabled
            });
            // Mirror to local cache (best-effort)
            try { 
                await chrome.storage.local.set({ 
                    autoPipOnTabSwitch: tabSwitchEnabled,
                    autoPipOnWindowSwitch: windowSwitchEnabled,
                    autoPipOnAppSwitch: appSwitchEnabled
                }); 
            } catch (_) { }

        } catch (error) {
        } finally {
            autoPipOnTabSwitchToggle.disabled = false;
            autoPipOnWindowSwitchToggle.disabled = false;
            autoPipOnAppSwitchToggle.disabled = false;
        }
    }

    // Save settings when changed
    autoPipOnTabSwitchToggle.addEventListener('change', saveSettings);
    autoPipOnWindowSwitchToggle.addEventListener('change', saveSettings);
    autoPipOnAppSwitchToggle.addEventListener('change', saveSettings);

    addCurrentSiteButton.addEventListener('click', () => {
        const selected = currentSiteSelect.value;
        const normalized = normalizeHostEntry(selected);
        if (!normalized) return;
        if (blockedSites.includes(normalized)) return;
        saveBlocklist([...blockedSites, normalized]);
        currentSiteSelect.value = '';
    });

    addManualSiteButton.addEventListener('click', () => {
        const normalized = normalizeHostEntry(manualSiteInput.value);
        if (!normalized) return;
        if (blockedSites.includes(normalized)) return;
        saveBlocklist([...blockedSites, normalized]);
        manualSiteInput.value = '';
    });

    manualSiteInput.addEventListener('keydown', (event) => {
        if (event.key !== 'Enter') return;
        event.preventDefault();
        addManualSiteButton.click();
    });

    chrome.storage.onChanged.addListener((changes, namespace) => {
        if (namespace !== 'sync') return;
        
        const tabSwitchChange = changes.autoPipOnTabSwitch ? changes.autoPipOnTabSwitch.newValue : undefined;
        const windowSwitchC
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
