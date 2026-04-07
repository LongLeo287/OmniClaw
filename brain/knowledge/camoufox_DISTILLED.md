---
id: camoufox
type: knowledge
owner: OA_Triage
---
# camoufox
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<img src="https://i.imgur.com/enUBkXt.png" align="center">

<h1 align="center">Camoufox</h1>

<h4 align="center">A stealthy, minimalistic, custom build of Firefox for web scraping 🦊</h4>

<p align="center">                                      
Camoufox is an open source anti-detect browser for robust fingerprint injection & anti-bot evasion.
</p>

<p align="center">
  <a href="https://trendshift.io/repositories/12224" target="_blank">
  <img src="https://trendshift.io/api/badge/repositories/12224" alt="daijro%2Fcamoufox | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a><br>
</p>

---

> [!NOTE]
> **All of the latest documentation is avaliable at [camoufox.com](https://camoufox.com).**

> [!NOTE]
> Browser development is active at [github.com/CloverLabsAI/camoufox](https://github.com/CloverLabsAI/camoufox). ([See activity](https://github.com/CloverLabsAI/camoufox/activity))<br>

> [!NOTE] 
> To make use of the alpha Camoufox releases, use the [`cloverlabs-camoufox`](https://pypi.org/project/cloverlabs-camoufox/) pip package. 

<hr width=50>

---

# Sponsors

<details open>
<summary>View</summary>
<table>
  <tr>
    <td width="30%" align="center" valign="middle">
      <a href="https://scrapfly.io/?utm_source=github&utm_medium=sponsoring&utm_campaign=camoufox" target="_blank">
        <img src="https://raw.githubusercontent.com/daijro/camoufox/main/assets/scrapfly.png" alt="Scrapfly.io" width="200">
      </a>
    </td>
    <td valign="middle">
      <a href="https://scrapfly.io/?utm_source=github&utm_medium=sponsoring&utm_campaign=camoufox">Scrapfly</a> is an enterprise-grade solution providing Web Scraping API that aims to simplify the scraping process by managing everything: real browser rendering, rotating proxies, and fingerprints (TLS, HTTP, browser) to bypass all major anti-bots. Scrapfly also unlocks the observability by providing an analytical dashboard and measuring the success rate/block rate in detail.
    </td>
  </tr>
  <tr>
    <td width="30%" align="center" valign="middle">
      <a href="https://cloverlabs.ai/?utm_source=github&utm_medium=sponsoring&utm_campaign=camoufox" target="_blank">
        <img src="https://i.imgur.com/I3oe7xG.jpeg" alt="cloverlabs.ai" width="300">
      </a>
    </td>
    <td valign="middle">
      <a href="https://cloverlabs.ai/?utm_source=github&utm_medium=sponsoring&utm_campaign=camoufox">Clover Labs</a> is a Toronto based venture studio building AI agents for growth and distribution.
    </td>
  </tr>
  <tr>
    <td width="30%" align="center" valign="middle" height="100">
      <a href="https://serpapi.com/use-cases/web-search-api?utm_source=camoufox" target="_blank">
        <img width="350" alt="color horizontal" src="https://github.com/user-attachments/assets/cdf90178-869e-4f85-8288-3fe32da319d9"/>
      </a>
    </td>
    <td valign="middle">
      <a href="https://serpapi.com/use-cases/web-search-api?utm_source=camoufox">SerpApi, a web search API</a> to scrape Google and other search engines with a simple API.
    </td>
  </tr>
  <tr>
    <td width="30%" align="center" valign="middle">
      <a href="https://www.thordata.com/?ls=github&lk=camoufox" target="_blank">
        <img alt="thordata" src="https://github.com/user-attachments/assets/fa79fe26-633b-44a4-a2a8-bce570f180ca" width="350"/>
      </a>
    </td>
    <td valign="middle">
      <a href="https://www.thordata.com/?ls=github&lk=camoufox">Thordata</a> - Your First Plan is on Us! 💰 Get 100% of your first residential proxy purchase back as wallet balance, up to $900.<br><br>
      <b>⚡ Why Thordata?</b><br><br>
      🌍 190+ real residential & ISP IP locations<br>
      🔐 Fully encrypted, ultra-secure connections<br>
      🚀 Optimized for web scraping, ad verification & automation workflows<br><br>
      🔥 Don't wait - this is your <b>best time to start</b> with <a href="https://www.thordata.com/?ls=github&lk=camoufox">Thordata</a> and experience the safest, fastest proxy network.
    </td>
  </tr>
  <tr>
    <td width="30%" align="center" valign="middle">
      <a href="https://proxyempire.io/?ref=camoufox&utm_source=camoufox" target="_blank">
        <img width="380" alt="proxyempire" src="https://github.com/user-attachments/assets/d1c5f849-5cb0-4aff-b48c-530bda2ee03f"/>
      </a>
    </td>
    <td valign="middle">
      <b>🚀 Camoufox × ProxyEmpire</b><br><br>
      Running Camoufox? Your proxy layer decides whether you scale — or get blocked.<br><br>
      <a href="https://proxyempire.io/?ref=camoufox&utm_source=camoufox">ProxyEmpire</a> delivers:<br>
      🌍 30M+ Residential IPs (170+ countries)<br>
      📱 4G/5G Mobile Proxies<br>
      🔄 Rotating & Sticky Sessions<br>
      ⚡ Unlimited Concurrent Sessions<br>
      🎯 Precise geo-targeting<br>
      HTTP, HTTPS & SOCKS5 Support<br><br>
      Built for scraping, automation, and high-stealth workflows.<br><br>
      <b>🔥 Exclusive Offer</b><br>
      Use code <b>Camoufox30</b><br>
      Get <b>30% recurring discount</b> (not just first month).<br>
      Upgrade your proxies. Reduce bans. Scale properly
    </td>
  </tr>
  <tr>
    <td width="30%" align="center" valign="middle">
      <a href="https://birdproxies.com/t/camoufox" target="_blank">
        <img width="380" alt="birdproxies" src="https://github.com/user-attachments/assets/e146836d-eb92-4b05-8bd9-120fd95dca10"/>
      </a>
    </td>
    <td valign="middle">
      Hey, we built BirdProxies because proxies shouldn't be complicated or overpriced. Fast residential and ISP proxies in 195+ locations, fair pricing, and real support.<br>
      Try our FlappyBird game on the landing page for free data!<br>
      <a href="https://birdproxies.com/t/camoufox">Try Now</a> | <a href="https://discord.com/invite/birdproxies">Discord</a>
    </td>
  </tr>
</table>
</details>

---

# Introduction

Camoufox is a modern & effective open source solution for avoiding bot detection and intelligent fingerprint rotation.

## Highlights

- **Invisible to anti-bot systems** 🎭
  - Page agent is hidden from JavaScript inspection. See the [stealth page](https://camoufox.com/stealth) for more details.

* **Fingerprint injection & rotation (without JS injection!)**
  - All navigator properties (device, OS, hardware, browser, etc.) ✅
  - Screen size, resolution, window, & viewport properties ✅
  - Geolocation, timezone, locale, & Intl spoofing ✅
  - WebRTC IP spoofing at the protocol level ✅
  - Voices, speech playback rate, etc. ✅
  - And much, much more!

- **Anti Graphical fingerprinting**
  - WebGL parameters, supported extensions, context attributes, & shader precision formats ✅
  - Font spoofing & anti-fingerprinting ✅

* **Quality of life features**
  - Human-like mouse movement 🖱️
  - Blocks & circumvents ads 🛡️
  - No CSS animations 💨

- Debloated & optimized for memory efficiency ⚡
- [PyPi package](https://pypi.org/project/camoufox/) for updates & auto fingerprint injection 📦
- Stays up to date with the latest Firefox version 🕓

---

## Fingerprint Injection

In Camoufox, data is intercepted at the C++ implementation level, making the changes undetectable through JavaScript inspection.

To spoof individual fingerprint properties, pass a JSON containing properties to spoof to the [Python interface](https://github.com/daijro/camoufox/tree/main/pythonlib#camoufox-python-interface):

```py
>>> with Camoufox(config={"property": "value"}) as browser:
```

Config data not set by the user will be automatically populated using [BrowserForge](https://github.com/daijro/browserforge) fingerprints, which mimic the statistical distribution of device characteristics in real-world traffic.

[[See implemented properties](https://camoufox.com/fingerprint/)]

---

## Python Usage

Camoufox is compatible with your existing Playwright code. You only have to change your browser initialization.

**Sync API**

```python
from camoufox.sync_api import Camoufox

with Camoufox() as browser:
    page = browser.new_page()
    page.goto("https://example.com")
```

**Async API**

```python
from camoufox.async_api import AsyncCamoufox

async with AsyncCamoufox() as browser:
    page = await browser.new_page()
    await page.goto("https://example.com")
```

[[Installation & usage](https://camoufox.com/python/)]

### Making Full use of Hardware Spoofing

For stable releases, you should always use the main [`camoufox`](https://pypi.org/project/camoufox/) pip package. However, if you want to make use of per-context fingerprints and hardware spoofing, use the [`cloverlabs-camoufox`](https://pypi.org/project/cloverlabs-camoufox/) package. This package is updated with each releases, whereas the official package is released on delay.

Make sure you are using a virtual env to avoid conflicts between the two packages.

**Installation**

```bash
pip install cloverlabs-camoufox
```

**Fetch the latest prerelease browser** (recommended for newest patches)

```bash
python -m camoufox sync
python -m camoufox set official/prerelease
python -m camoufox fetch
```

**Usage** — the API is identical to the upstream package:

```python
from camoufox.sync_api import Camoufox

with Camoufox() as browser:
    page = browser.new_page()
    page.goto("https://example.com")
```

---

## Capabilities

Below is a list of patches and features implemented in Camoufox.

### Fingerprint spoofing

- Navigator properties spoofing (device, browser, locale, etc.)
- Support for emulating screen size, resolution, etc.
- Spoof WebGL parameters, supported extensions, context attributes, and shader precision formats.
- Spoof inner and outer window viewport sizes
- Spoof AudioContext sample rate, output latency, and max channel count
- Spoof device voices & playback rates
- Spoof the amount of microphones, webcams, and speakers available.
- Network headers (Accept-Languages and User-Agent) are spoofed to match the navigator properties
- WebRTC IP spoofing at the protocol level
- Geolocation, timezone, and locale spoofing
- Battery API spoofing
- etc.

### Stealth patches

- Avoids main world execution leaks. All page agent javascript is sandboxed
- Avoids frame execution context leaks
- Fixes `navigator.webdriver` detection
- Fixes Firefox headless detection via pointer type ([#26](https://github.com/daijro/camoufox/issues/26))
- Removed potentially leaking anti-zoom/meta viewport handling patches
- Uses non-default screen & window sizes
- Re-enable fission content isolations
- Re-enable PDF.js
- Other leaking config properties changed
- Human-like cursor movement

### Anti font fingerprinting

- Automatically uses the correct system fonts for your User Agent
- Bundled with Windows, Mac, and Linux system fonts
- Prevents font metrics fingerprinting by randomly offsetting letter spacing

### Playwright support

- Custom implementation of Playwright for the latest Firefox
- Various config patches to evade bot detection

### Debloat/Optimizations

- Stripped out/disabled _many, many_ Mozilla services. Runs faster than the original Mozilla Firefox, and uses less memory (200mb)
- Patches from LibreWolf & Ghostery to help remove telemetry & bloat
- Debloat config from PeskyFox, LibreWolf, and others
- Speed & network optimizations from FastFox
- Removed all CSS animations
- Minimalistic theming
- etc.

### Addons

- Load Firefox addons without a debug server by passing a list of paths to the `addons` property
- Added uBlock Origin with custom privacy filters
- Addons are not allowed to open tabs
- Addons are automatically enabled in Private Browsing mode
- Addons are automatically pinned to the toolbar
- Fixes DNS leaks with uBO prefetching

### Python Interface

- Automatically generates & injects unique device characteristics into Camoufox based on their real-world distribution
- WebGL fingerprint injection & rotation
- Uses the correct system fonts and subpixel antialiasing & hinting based on your target OS
- Avoid proxy detection by calculating your target geolocation, timezone, & locale from your proxy's target region
- Calculate and spoof the browser's language based on the distribution of language speakers in the proxy's target region
- Remote server hosting to use Camoufox with other languages that support Playwright
- Built-in virtual display buffer to run Camoufox headfully on a headless server
- Toggle image loading, WebRTC, and WebGL
- etc.

> [!NOTE]
> Camoufox does **not** fully support injecting Chromium fingerprints. Some WAFs (such as [Interstitial](https://nopecha.com/demo/cloudflare)) test for Spidermonkey engine behavior, which is impossible to spoof.

---

# Stealth Overview

## How Camoufox hides its automation library

> [!WARNING]
> **Current status as of 2026**:
> There has been a year gap in maintenance due to a personal situation. Camoufox has gone down in performance due to the base Firefox version and newly discovered fingerprint inconsistencies. **Camoufox is currently under active development.**

In Camoufox, all of Playwright's internal Page Agent's code is sandboxed and isolated. This makes it impossible for a page to detect the presence of Playwright through Javascript inspection.

Normally, Playwright injects some JavaScript into the page such as `window.__playwright__binding__` and to perform actions like querying elements, evaluating javascript, or running init scripts, which can be detected by websites. In Camoufox, these actions are handled in an isolated scope outside of the page. In other words, websites can no longer "see" any JavaScript that Playwright would typically inject. This prevents traces of Playwright altogether.

However, even with hiding its automation library, Camoufox is not immune to inconsistencies in fingerprint rotation. This still requires maintenance to spot and fix.

### Page Interactions

Anti-bot systems also run client-side scripts to monitor your behavior. For example, they look for patterns in mouse movements, clicks, scrolling, and the timing between actions.

<video src="https://github.com/user-attachments/assets/6d33d6af-3537-4603-bf24-6bd3f4f8f455" width="200px" autoplay loop muted></video>

Camoufox tries its best with its human-like mouse movement algorithm. The natural motion algorithm was originally from [riflosnake's HumanCursor](https://github.com/riflosnake/HumanCursor) and has been rewritten in C++ and modified for more distance-aware trajectories.

However, this isn't perfect. It may still be detected with sophisticated enough analysis. (WIP for the future)

---

## How Camoufox rotates identities

In addition to hiding the automation library, your identity must be randomized in each instance as well to avoid rate limiting and detection. Rotating your IP address means nothing if it's obviously you each time. There are thousands of things that create a unique **fingerprint** of you. Right now, any website you visit can see you are using Chrome on Linux, running on NVIDIA GeForce RTX 4090.

### Market Share Distribution

Even if you are rotating your IP for each running bot instance, web 
... [TRUNCATED]
```

### File: tests\README.md
```md
# Camoufox Tests

Ensures that Playwright functionality is not broken.

---

This directory is based on the original Playwright-Python [tests](https://github.com/microsoft/playwright-python/tree/main/tests).

It has been modified to skip tests that use the following features:

- Injecting JavaScript into the page or writing to DOM. Camoufox's `page.evaluate` only supports reading values, not executing within the page context.
- Overriding the User-Agent.
- Any tests specific to Chromium or Webkit.

---

# Usage

### Setting up the environment

Cd to this directory and run the following command to setup the venv and install the dependencies:

```bash
bash setup-venv.sh
```

### Running the tests

Run via the shell script:

```bash
bash run-tests.sh --headful --executable-path /path/to/camoufox-bin
```

Or through the Makefile:

```bash
make tests headful=true
```

---
```

### File: assets_DISTILLED.md
```md
---
id: assets
type: distilled_knowledge
---
# assets

## SWALLOW ENGINE DISTILLATION

### File: search-config.json
```json
{"data": [], "timestamp": 1654094046000}

```

### File: uBOAssets.json
```json
{
  "assets.json": {
    "content": "internal",
    "updateAfter": 13,
    "contentURL": "https://gitlab.com/librewolf-community/browser/source/-/raw/main/assets/uBOAssets.json"
  },
  "public_suffix_list.dat": {
    "content": "internal",
    "updateAfter": 19,
    "contentURL": [
      "https://publicsuffix.org/list/public_suffix_list.dat",
      "assets/thirdparties/publicsuffix.org/list/effective_tld_names.dat"
    ]
  },
  "ublock-badlists": {
    "content": "internal",
    "updateAfter": 29,
    "contentURL": [
      "https://ublockorigin.github.io/uAssets/filters/badlists.txt",
      "assets/ublock/badlists.txt"
    ],
    "cdnURLs": [
      "https://ublockorigin.github.io/uAssetsCDN/filters/badlists.txt",
      "https://ublockorigin.pages.dev/filters/badlists.txt",
      "https://cdn.jsdelivr.net/gh/uBlockOrigin/uAssetsCDN@main/filters/badlists.txt",
      "https://cdn.statically.io/gh/uBlockOrigin/uAssetsCDN/main/filters/badlists.txt"
    ]
  },
  "ublock-filters": {
    "content": "filters",
    "group": "default",
    "parent": "uBlock filters",
    "title": "uBlock filters – Ads",
    "tags": "ads",
    "contentURL": [
      "https://ublockorigin.github.io/uAssets/filters/filters.txt",
      "assets/ublock/filters.min.txt",
      "assets/ublock/filters.txt"
    ],
    "cdnURLs": [
      "https://ublockorigin.github.io/uAssetsCDN/filters/filters.min.txt",
      "https://ublockorigin.pages.dev/filters/filters.min.txt",
      "https://cdn.jsdelivr.net/gh/uBlockOrigin/uAssetsCDN@main/filters/filters.min.txt",
      "https://cdn.statically.io/gh/uBlockOrigin/uAssetsCDN/main/filters/filters.min.txt"
    ],
    "supportURL": "https://github.com/uBlockOrigin/uAssets"
  },
  "ublock-privacy": {
    "content": "filters",
    "group": "default",
    "parent": "uBlock filters",
    "title": "uBlock filters – Privacy",
    "tags": "privacy",
    "contentURL": [
      "https://ublockorigin.github.io/uAssets/filters/privacy.txt",
      "assets/ublock/privacy.min.txt",
      "assets/ublock/privacy.txt"
    ],
    "cdnURLs": [
      "https://ublockorigin.github.io/uAssetsCDN/filters/privacy.min.txt",
      "https://ublockorigin.pages.dev/filters/privacy.min.txt",
      "https://cdn.jsdelivr.net/gh/uBlockOrigin/uAssetsCDN@main/filters/privacy.min.txt",
      "https://cdn.statically.io/gh/uBlockOrigin/uAssetsCDN/main/filters/privacy.min.txt"
    ],
    "supportURL": "https://github.com/uBlockOrigin/uAssets"
  },
  "ublock-unbreak": {
    "content": "filters",
    "group": "default",
    "parent": "uBlock filters",
    "title": "uBlock filters – Unbreak",
    "contentURL": [
      "https://ublockorigin.github.io/uAssets/filters/unbreak.txt",
      "assets/ublock/unbreak.min.txt",
      "assets/ublock/unbreak.txt"
    ],
    "cdnURLs": [
      "https://ublockorigin.github.io/uAssetsCDN/filters/unbreak.min.txt",
      "https://ublockorigin.pages.dev/filters/unbreak.min.txt",
      "https://cdn.jsdelivr.net/gh/uBlockOrigin/uAssetsCDN@main/filters/unbreak.min.txt",
      "https://cdn.statically.io/gh/uBlockOrigin/uAssetsCDN/main/filters/unbreak.min.txt"
    ],
    "supportURL": "https://github.com/uBlockOrigin/uAssets"
  },
  "ublock-quick-fixes": {
    "content": "filters",
    "group": "default",
    "parent": "uBlock filters",
    "title": "uBlock filters – Quick fixes",
    "contentURL": [
      "https://ublockorigin.github.io/uAssets/filters/quick-fixes.txt",
      "assets/ublock/quick-fixes.min.txt",
      "assets/ublock/quick-fixes.txt"
    ],
    "cdnURLs": [
      "https://ublockorigin.github.io/uAssetsCDN/filters/quick-fixes.min.txt",
      "https://ublockorigin.pages.dev/filters/quick-fixes.min.txt",
      "https://cdn.jsdelivr.net/gh/uBlockOrigin/uAssetsCDN@main/filters/quick-fixes.min.txt",
      "https://cdn.statically.io/gh/uBlockOrigin/uAssetsCDN/main/filters/quick-fixes.min.txt"
    ],
    "supportURL": "https://github.com/uBlockOrigin/uAssets"
  },
  "adguard-generic": {
    "content": "filters",
    "group": "ads",
    "off": true,
    "title": "AdGuard – Ads",
    "tags": "ads",
    "contentURL": "https://filters.adtidy.org/extension/ublock/filters/2_without_easylist.txt",
    "supportURL": "https://github.com/AdguardTeam/AdguardFilters#adguard-filters",
    "instructionURL": "https://adguard.com/kb/general/ad-filtering/adguard-filters/"
  },
  "adguard-mobile": {
    "content": "filters",
    "group": "ads",
    "off": true,
    "title": "AdGuard – Mobile Ads",
    "tags": "ads mobile",
    "ua": "mobile",
    "contentURL": "https://filters.adtidy.org/extension/ublock/filters/11.txt",
    "supportURL": "https://github.com/AdguardTeam/AdguardFilters#adguard-filters",
    "instructionURL": "https://adguard.com/kb/general/ad-filtering/adguard-filters/"
  },
  "easylist": {
    "content": "filters",
    "group": "ads",
    "title": "EasyList",
    "tags": "ads",
    "preferred": true,
    "contentURL": [
      "https://ublockorigin.github.io/uAssets/thirdparties/easylist.txt",
      "assets/thirdparties/easylist/easylist.txt"
    ],
    "cdnURLs": [
      "https://cdn.jsdelivr.net/gh/uBlockOrigin/uAssetsCDN@main/thirdparties/easylist.txt",
      "https://cdn.statically.io/gh/uBlockOrigin/uAssetsCDN/main/thirdparties/easylist.txt",
      "https://ublockorigin.pages.dev/thirdparties/easylist.txt"
    ],
    "supportURL": "https://easylist.to/"
  },
  "adguard-spyware-url": {
    "content": "filters",
    "group": "privacy",
    "title": "AdGuard URL Tracking Protection",
    "tags": "privacy",
    "contentURL": "https://filters.adtidy.org/extension/ublock/filters/17.txt",
    "supportURL": "https://github.com/AdguardTeam/AdguardFilters#adguard-filters",
    "instructionURL": "https://adguard.com/kb/general/ad-filtering/adguard-filters/"
  },
  "adguard-spyware": {
    "content": "filters",
    "group": "privacy",
    "off": true,
    "title": "AdGuard Tracking Protection",
    "contentURL": "https://filters.adtidy.org/extension/ublock/filters/3.txt",
    "supportURL": "https://github.com/AdguardTeam/AdguardFilters#adguard-filters",
    "instructionURL": "https://adguard.com/kb/general/ad-filtering/adguard-filters/"
  },
  "block-lan": {
    "content": "filters",
    "group": "privacy",
    "off": true,
    "title": "Block Outsider Intrusion into LAN",
    "tags": "privacy security",
    "contentURL": "https://ublockorigin.github.io/uAssets/filters/lan-block.txt",
    "cdnURLs": [
      "https://ublockorigin.github.io/uAssetsCDN/filters/lan-block.txt",
      "https://ublockorigin.pages.dev/filters/lan-block.txt",
      "https://cdn.jsdelivr.net/gh/uBlockOrigin/uAssetsCDN@main/filters/lan-block.txt",
      "https://cdn.statically.io/gh/uBlockOrigin/uAssetsCDN/main/filters/lan-block.txt"
    ],
    "supportURL": "https://github.com/uBlockOrigin/uAssets"
  },
  "easyprivacy": {
    "content": "filters",
    "group": "privacy",
    "title": "EasyPrivacy",
    "tags": "privacy",
    "preferred": true,
    "contentURL": [
      "https://ublockorigin.github.io/uAssets/thirdparties/easyprivacy.txt",
      "assets/thirdparties/easylist/easyprivacy.txt"
    ],
    "cdnURLs": [
      "https://cdn.jsdelivr.net/gh/uBlockOrigin/uAssetsCDN@main/thirdparties/easyprivacy.txt",
      "https://cdn.statically.io/gh/uBlockOrigin/uAssetsCDN/main/thirdparties/easyprivacy.txt",
      "https://ublockorigin.pages.dev/thirdparties/easyprivacy.txt"
    ],
    "supportURL": "https://easylist.to/"
  },
  "adguard-cookies": {
    "content": "filters",
    "group": "annoyances",
    "group2": "cookies",
    "parent": "AdGuard/uBO – Cookie Notices",
    "off": true,
    "title": "AdGuard – Cookie Notices",
    "tags": "annoyances cookies",
    "contentURL": "https://filters.adtidy.org/extension/ublock/filters/18.txt",
    "supportURL": "https://github.com/AdguardTeam/AdguardFilters#adguard-filters",
    "instructionURL": "https://adguard.com/kb/general/ad-filtering/adguard-filters/"
  },
  "ublock-cookies-adguard": {
    "content": "filters",
    "group": "annoyances",
    "group2": "cookies",
    "parent": "AdGuard/uBO – Cookie Notices",
    "off": true,
    "title": "uBlock filters – Cookie Notices",
    "tags": "annoyances cookies",
    "contentURL": "https://ublockorigin.github.io/uAssets/filters/annoyances-cookies.txt",
    "cdnURLs": [
      "https://ublockorigin.github.io/uAssetsCDN/filters/annoyances-cookies.txt",
      "https://ublockorigin.pages.dev/filters/annoyances-cookies.txt",
      "https://cdn.jsdelivr.net/gh/uBlockOrigin/uAssetsCDN@main/filters/annoyances-cookies.txt",
      "https://cdn.statically.io/gh/uBlockOrigin/uAssetsCDN/main/filters/annoyances-cookies.txt"
    ],
    "supportURL": "https://github.com/uBlockOrigin/uAssets"
  },
  "fanboy-cookiemonster": {
    "content": "filters",
    "group": "annoyances",
    "group2": "cookies",
    "parent": "EasyList/uBO – Cookie Notices",
    "off": true,
    "title": "EasyList – Cookie Notices",
    "tags": "annoyances cookies",
    "preferred": true,
    "contentURL": [
      "https://ublockorigin.github.io/uAssets/thirdparties/easylist-cookies.txt",
      "https://secure.fanboy.co.nz/fanboy-cookiemonster_ubo.txt"
    ],
    "cdnURLs": [
      "https://ublockorigin.github.io/uAssetsCDN/thirdparties/easylist-cookies.txt",
      "https://ublockorigin.pages.dev/thirdparties/easylist-cookies.txt",
      "https://cdn.jsdelivr.net/gh/uBlockOrigin/uAssetsCDN@main/thirdparties/easylist-cookies.txt",
      "https://cdn.statically.io/gh/uBlockOrigin/uAssetsCDN/main/thirdparties/easylist-cookies.txt",
      "https://secure.fanboy.co.nz/fanboy-cookiemonster_ubo.txt"
    ],
    "supportURL": "https://github.com/easylist/easylist#fanboy-lists"
  },
  "ublock-cookies-easylist": {
    "content": "filters",
    "group": "annoyances",
    "group2": "cookies",
    "parent": "EasyList/uBO – Cookie Notices",
    "off": true,
    "title": "uBlock filters – Cookie Notices",
    "tags": "annoyances cookies",
    "preferred": true,
    "contentURL": "https://ublockorigin.github.io/uAssets/filters/annoyances-cookies.txt",
    "cdnURLs": [
      "https://ublockorigin.github.io/uAssetsCDN/filters/annoyances-cookies.txt",
      "https://ublockorigin.pages.dev/filters/annoyances-cookies.txt",
      "https://cdn.jsdelivr.net/gh/uBlockOrigin/uAssetsCDN@main/filters/annoyances-cookies.txt",
      "https://cdn.statically.io/gh/uBlockOrigin/uAssetsCDN/main/filters/annoyances-cookies.txt"
    ],
    "supportURL": "https://github.com/uBlockOrigin/uAssets"
  },
  "adguard-social": {
    "content": "filters",
    "group": "annoyances",
    "group2": "social",
    "parent": null,
    "off": true,
    "title": "AdGuard – Social Widgets",
    "tags": "annoyances social",
    "contentURL": "https://filters.adtidy.org/extension/ublock/filters/4.txt",
    "supportURL": "https://github.com/AdguardTeam/AdguardFilters#adguard-filters",
    "instructionURL": "https://adguard.com/kb/general/ad-filtering/adguard-filters/"
  },
  "fanboy-social": {
    "content": "filters",
    "group": "annoyances",
    "group2": "social",
    "parent": null,
    "off": true,
    "title": "EasyList – Social Widgets",
    "tags": "annoyances social",
    "preferred": true,
    "contentURL": [
      "https://ublockorigin.github.io/uAssets/thirdparties/easylist-social.txt",
      "https://secure.fanboy.co.nz/fanboy-social_ubo.txt"
    ],
    "cdnURLs": [
      "https://ublockorigin.github.io/uAssetsCDN/thirdparties/easylist-social.txt",
      "https://ublockorigin.pages.dev/thirdparties/easylist-social.txt",
      "https://cdn.jsdelivr.net/gh/uBlockOrigin/uAssetsCDN@main/thirdparties/easylist-social.txt",
      "https://cdn.statically.io/gh/uBlockOrigin/uAssetsCDN/main/thirdparties/easylist-social.txt",
      "https://secure.fanboy.co.nz/fanboy-social_ubo.txt"
    ],
    "supportURL": "https://easylist.to/"
  },
  "fanboy-thirdparty_social": {
    "content": "filters",
    "group": "annoyances",
    "group2": "social",
    "off": true,
    "title": "Fanboy – Anti-Facebook",
    "tags": "privacy",
    "contentURL": "https://secure.fanboy.co.nz/fanboy-antifacebook.txt",
    "supportURL": "https://github.com/ryanbr/fanboy-adblock/issues"
  },
  "adguard-popup-overlays": {
    "content": "filters",
    "group": "annoyances",
    "parent": "AdGuard – Annoyances",
    "off": true,
    "title": "AdGuard – Popup Overlays",
    "tags": "annoyances",
    "contentURL": "https://filters.adtidy.org/extension/ublock/filters/19.txt",
    "supportURL": "https://github.com/AdguardTeam/AdguardFilters#adguard-filters",
    "instructionURL": "https://adguard.com/kb/general/ad-filtering/adguard-filters/"
  },
  "adguard-mobile-app-banners": {
    "content": "filters",
    "group": "annoyances",
    "parent": "AdGuard – Annoyances",
    "off": true,
    "title": "AdGuard – Mobile App Banners",
    "tags": "annoyances mobile",
    "contentURL": "https://filters.adtidy.org/extension/ublock/filters/20.txt",
    "supportURL": "https://github.com/AdguardTeam/AdguardFilters#adguard-filters",
    "instructionURL": "https://adguard.com/kb/general/ad-filtering/adguard-filters/"
  },
  "adguard-other-annoyances": {
    "content": "filters",
    "group": "annoyances",
    "parent": "AdGuard – Annoyances",
    "off": true,
    "title": "AdGuard – Other Annoyances",
    "tags": "annoyances",
    "contentURL": "https://filters.adtidy.org/extension/ublock/filters/21.txt",
    "supportURL": "https://github.com/AdguardTeam/AdguardFilters#adguard-filters",
    "instructionURL": "https://adguard.com/kb/general/ad-filtering/adguard-filters/"
  },
  "adguard-widgets": {
    "content": "filters",
    "group": "annoyances",
    "parent": "AdGuard – Annoyances",
    "off": true,
    "title": "AdGuard – Widgets",
    "tags": "annoyances",
    "contentURL": "https://filters.adtidy.org/extension/ublock/filters/22.txt",
    "supportURL": "https://github.com/AdguardTeam/AdguardFilters#adguard-filters",
    "instructionURL": "https://adguard.com/kb/general/ad-filtering/adguard-filters/"
  },
  "easylist-annoyances": {
    "content": "filters",
    "group": "annoyances",
    "parent": "EasyList – Annoyances",
    "off": true,
    "title": "EasyList – Other Annoyances",
    "tags": "annoyances",
    "preferred": true,
    "contentURL": "https://ublockorigin.github.io/uAssets/thirdparties/easylist-annoyances.txt",
    "cdnURLs": [
      "https://ublockorigin.github.io/uAssetsCDN/thirdparties/easylist-annoyances.txt",
      "https://ublockorigin.pages.dev/thirdparties/easylist-annoyances.txt",
      "https://cdn.jsdelivr.net/gh/uBlockOrigin/uAssetsCDN@main/thirdparties/easylist-annoyances.txt",
      "https://cdn.statically.io/gh/uBlockOrigin/uAssetsCDN/main/thirdparties/easylist-annoyances.txt"
    ],
    "supportURL": "https://github.com/easylist/easylist#fanboy-lists"
  },
  "easylist-chat": {
   
... [TRUNCATED]
```

### File: CONTRIBUTING.md
```md
# Contributing to Camoufox

Thanks for your interest in contributing! Here's how to get started.

## Ways to Contribute

- **Bug reports** — Open an issue with steps to reproduce, expected behavior, and actual behavior.
- **Feature requests** — Open an issue describing the use case and why it's useful.
- **Code contributions** — Fork the repo, make your changes, and open a pull request.
- **Documentation** — Fixes and improvements to docs are always welcome.

## Development Setup
See README.md

## Pull Request Rules

1. Each pull request must be associated with a Github issue
2. Follow the pull request template
3. Keep commits focused — one logical change per commit.
4. Open a PR with a clear description of what you changed and why.
5. All pull requests must pass both the **build-tester** and **service_tests** test suites before merging.

## Testing Requirements

**Both test suites are required for every PR.** They test different layers of the stack and catch different classes of bugs — passing one does not substitute for the other.

### build-tester

Tests the **raw binary** in isolation, bypassing the Python package entirely. Fingerprints are injected manually via `generate_context_fingerprint` + `addInitScript` (per-context mode) and via the `CAMOU_CONFIG` environment variable (global mode). It also validates that injected values actually appear in the page via match result checks.

**Run this when you change:** browser patches, Firefox source modifications, WebGL/canvas/audio spoofing, WebRTC IP handling, or anything in the C++/JS browser layer.

```bash
cd build-tester
npm install          # first time only
pip install -r requirements.txt
python scripts/run_tests.py /path/to/camoufox-binary
```

See [`build-tester/README.md`](build-tester/README.md) for full details.

---

### service_tests

Tests the **full stack** — the binary and the Python package together — using only the public `AsyncNewContext` API. Fingerprints are generated entirely by camoufox/browserforge with no manual injection. Real proxies are required; the WebRTC IP and timezone are auto-derived from each proxy's exit IP. This is a black-box trust test: if it fails, the fix belongs in the Python package, not in the test.

**Run this when you change:** `pythonlib/` (fingerprint generation, `AsyncNewContext`, `NewContext`), proxy handling, or any behaviour that affects how the Python package interacts with the binary.

```bash
cd service_tests
# Add proxies (one per line, format: user:pass@domain:port)
cp proxies.txt.example proxies.txt   # or create manually
./run_tests.sh
```

See [`service_tests/README.md`](service_tests/README.md) for full details.

---

### Key differences

| | build-tester | service_tests |
|---|---|---|
| Entry point | Raw binary path | `pip install camoufox` |
| Fingerprint injection | Manual | Via `AsyncNewContext` API |
| Global mode (`CAMOU_CONFIG`) | ✓ | ✗ |
| Match result validation | ✓ | ✗ |
| Proxy required | ✗ | ✓ |
| Profiles | 8 (6 per-context + 2 global) | 6 (per-context) |
| Fix target on failure | Browser source | Python package |

## Reporting Issues

Please search existing issues before opening a new one. Include:
- Camoufox version
- OS and Python version
- A minimal reproducible example

## Questions

For usage questions, check the [documentation](https://camoufox.com) first. For anything else, open an issue.

```

### File: docs_DISTILLED.md
```md
---
id: docs
type: distilled_knowledge
---
# docs

## SWALLOW ENGINE DISTILLATION

### File: beta-testing-ff146.md
```md
# Testing Firefox 146 Beta

This guide explains how to test the experimental Firefox 146 build of Camoufox.

> **Note:** The FF146 build is experimental and may contain bugs. For a stable production version, use branch `releases/135`.

## Build from Source

1. Clone the repository:
```bash
git clone --depth 1 https://github.com/daijro/camoufox
cd camoufox
```

2. Set up the build environment:
```bash
make dir
make bootstrap   # only needed once
```

3. Build for your target platform:
```bash
python3 multibuild.py --target <os> --arch <arch>
```

| Parameter | Options |
|-----------|---------|
| `--target` | `linux`, `windows`, `macos` |
| `--arch` | `x86_64`, `arm64`, `i686` |

Build artifacts will appear in the `dist/` folder.

### Default Install Directories

When using the Python library (`camoufox fetch`), the default install directory is:

| OS | Install Directory |
|------|-------------------|
| **Linux** | `~/.cache/camoufox/` |
| **macOS** | `~/Library/Caches/camoufox/` |
| **Windows** | `C:\Users\<user>\AppData\Local\camoufox\camoufox\Cache\` |

## Replacing the Binary

To test FF146 with an existing Camoufox installation:

1. Build from source using the instructions above
2. Extract the built zip from `dist/`
3. Replace the binary at the corresponding path for your OS:

**Linux:**
```bash
cp /path/to/built/camoufox-bin ~/.cache/camoufox/camoufox-bin
```

**macOS:**
```bash
cp /path/to/built/Camoufox.app ~/Library/Caches/camoufox/Camoufox.app
```

**Windows:**
```powershell
copy C:\path\to\built\camoufox.exe C:\Users\<user>\AppData\Local\camoufox\camoufox\Cache\camoufox.exe
```

```

### File: patch-upgrading-guide.md
```md
# Firefox Patch Upgrading Guide for LLMs

This guide provides step-by-step instructions for updating Camoufox patches when upgrading Firefox versions. Patches frequently break due to Firefox API changes, file reorganizations, and line number shifts.

**All patches are located in the `patches/` directory.** There are no separate context patches to merge—per-context functionality is already built into the patches.

## Table of Contents

1. [Understanding the Patch System](#understanding-the-patch-system)
2. [Preparation](#preparation)
3. [General Workflow](#general-workflow)
4. [Fixing Common Reject Types](#fixing-common-reject-types)
5. [Context Patch Merging](#context-patch-merging) *(Historical - skip for future updates)*
6. [Testing and Validation](#testing-and-validation)
7. [Best Practices](#best-practices)

---

## Understanding the Patch System

### Patch Categories

All Camoufox patches are in the `patches/` directory:

- **Core Patches**: `0-playwright.patch`, `1-leak-fixes.patch`, etc.
- **Feature Patches**: `webrtc-ip-spoofing.patch`, `anti-font-fingerprinting.patch`, etc.
- All patches now include per-user-context (per-Playwright-context) support built-in

**Historical Note**: Context patches (e.g., `font-fingerprinting.context.patch`, `webrtc.context.patch`) were previously separate but have been merged into their base patches as of Firefox 146. You will not find `.context.patch` files in the repository.

### Key Infrastructure Files

- **RoverfoxStorageManager.cpp/h**: Thread-safe key-value storage for per-context data
- **Manager Classes**: FontSpacingSeedManager, WebRTCIPManager, etc.
- **Window.webidl**: Exposes JavaScript APIs to Playwright

---

## Preparation

### 1. Reset to Clean State

**IMPORTANT**: Always use `make clean` to reset to fresh Firefox source:

```bash
make clean
```

**DO NOT** use `git reset` or `git clean` commands directly in the Firefox source directory - these can delete untracked files needed for the build.

### 2. Identify Patches to Update

Check which patches exist:

```bash
ls patches/*.patch
```

### 3. Understand Patch Dependencies

Some patches depend on others being applied first:
- `1-leak-fixes.patch` requires `0-playwright.patch`
- Check the Makefile or patch comments for dependency chains

---

## General Workflow

### Step 1: Apply Base Patch and Identify Rejects

```bash
cd camoufox-<version>
patch -p1 < ../patches/patch-name.patch
```

Find reject files:

```bash
find . -name '*.rej' -type f
```

### Step 2: Analyze Each Reject File

Read the reject file to understand what failed:

```bash
cat path/to/file.cpp.rej
```

Reject files show:
- `@@` lines: Line numbers where patch expected to apply
- `-` lines: What the patch expected to find (old code)
- `+` lines: What the patch wanted to add (new code)

### Step 3: Locate the Correct Position in Firefox Code

The line numbers in rejects are usually wrong for the new Firefox version. You need to:

1. **Search for unique context** around the reject
2. **Understand what the patch is doing**
3. **Find equivalent location** in new Firefox code

### Step 4: Apply Changes Manually

Use the Edit tool to apply the rejected changes to the correct location.

### Step 5: Remove Reject Files

After fixing all rejects:

```bash
rm -f path/to/file.cpp.rej
find . -name '*.rej' -type f  # Verify all removed
```

### Step 6: Generate Updated Patch

```bash
# Add any new files first
git add new/file.cpp new/file.h

# Generate patch with both staged and unstaged changes
git diff --cached --binary > /tmp/patch-name.patch
git diff --binary >> /tmp/patch-name.patch

# Copy to patches directory
cp /tmp/patch-name.patch ../patches/patch-name.patch
```

### Step 7: Verify Patch Applies Cleanly

```bash
cd ..
make clean
cd camoufox-<version>
patch -p1 < ../patches/patch-name.patch
find . -name '*.rej' -type f  # Should return nothing
```

---

## Fixing Common Reject Types

### Type 1: Include Directive Rejects

**Symptom**: Reject shows failed `#include` additions

**Example Reject**:
```
@@ -325,6 +325,7 @@
 #include "xpcpublic.h"

+#include "WebRTCIPManager.h"
 #include "nsDocShell.h"
```

**How to Fix**:

1. Read the actual file to find the includes section
2. Search for nearby includes (e.g., `xpcpublic.h`)
3. Add the new include in the appropriate location
4. Firefox include order: system headers, then Mozilla headers, alphabetically within groups

**Example**:

```cpp
// Find this in the actual file:
#include "xpcpublic.h"

// Add the missing includes after it:
#include "xpcpublic.h"

#include "WebRTCIPManager.h"
#include "nsDocShell.h"
#include "mozilla/OriginAttributes.h"
```

### Type 2: Function Signature Changes

**Symptom**: Reject shows function call with changed parameters

**Example Reject**:
```
-  mouseOrPointerEvent.mButton = aButton;
+  mouseOrPointerEvent.mJugglerEventId = aMouseEventData.mJugglerEventId;
```

**Common Causes**:
- Firefox refactored the API
- Parameters moved from individual args to struct/data object
- Parameter order changed

**How to Fix**:

1. Search for the function definition in Firefox source
2. Understand the new API structure
3. Port the patch logic to the new API

**Example - Firefox 146 Mouse Event Refactoring**:

Old Firefox 144 API (individual parameters):
```cpp
void SynthesizeMouseEvent(int x, int y, int button, ...)
```

New Firefox 146 API (structured data):
```cpp
void SynthesizeMouseEvent(SynthesizeMouseEventData& aData,
                         SynthesizeMouseEventOptions& aOptions)
```

Port the patch:
```cpp
// Old patch code:
mouseEvent.mButton = aButton;
mouseEvent.jugglerEventId = aJugglerEventId;

// New patch code for Firefox 146:
mouseOrPointerEvent.mButton = aMouseEventData.mButton;
mouseOrPointerEvent.mJugglerEventId = aMouseEventData.mJugglerEventId;
mouseOrPointerEvent.convertToPointer = aOptions.mConvertToPointer;
```

### Type 3: Missing Context - Code Moved

**Symptom**: Reject shows context that doesn't exist in the file

**How to Fix**:

1. Use grep to search for unique function names or variables in the reject
2. Find where Firefox moved the code
3. Apply the patch to the new location

```bash
# Search across the codebase
grep -r "FunctionName" camoufox-<version>/ --include="*.cpp"
```

### Type 4: New Parameter Added to Function Calls

**Symptom**: Reject shows function call, but Firefox added/removed parameters

**Example - MakeTextRun userContextId**:

Old call:
```cpp
MakeTextRun(text, len, drawTarget, appUnitsPerDevPixel, flags, recorder);
```

New Firefox expects:
```cpp
MakeTextRun(text, len, drawTarget, appUnitsPerDevPixel, flags, recorder, userContextId);
```

**How to Fix**:

1. Extract userContextId from available context (Document, PresContext, etc.)
2. Add proper extraction code before the call
3. Pass userContextId as the last parameter

**Standard userContextId Extraction Pattern**:

```cpp
uint32_t userContextId = 0;
if (mozilla::dom::Document* doc = presContext->Document()) {
  if (nsIPrincipal* principal = doc->NodePrincipal()) {
    auto* bp = mozilla::BasePrincipal::Cast(principal);
    if (bp) {
      userContextId = bp->OriginAttributesRef().mUserContextId;
    }
  }
}

// Now pass userContextId to the function
MakeTextRun(..., userContextId);
```

### Type 5: Line Number Shifts (No Code Changes)

**Symptom**: Reject shows patch tried to apply at wrong line number, but code is identical

**How to Fix**:

Simply apply the patch manually at the correct line number. The code hasn't changed, just the location.

---

## Context Patch Merging (Historical - Not Applicable for Future Updates)

**NOTE**: As of Firefox 146, all context patches have been merged into their base patches. This section is kept for historical reference and understanding how the patches evolved. Future Firefox updates will only need to update patches in the `patches/` directory.

---

**Historical Context**: Context patches previously added per-user-context functionality to base patches. The workflow was different from simple patch updates.

### Historical Goal

Merge all changes from `*.context.patch` into the corresponding base patch so there's only one comprehensive patch file.

### Historical Example: font-fingerprinting.context.patch → anti-font-fingerprinting.patch

### Workflow

1. **Reset to clean Firefox**:
   ```bash
   make clean
   ```

2. **Apply base patch first**:
   ```bash
   cd camoufox-<version>
   patch -p1 < ../patches/anti-font-fingerprinting.patch
   ```

3. **Apply context patch on top**:
   ```bash
   patch -p1 < ../font-fingerprinting.context.patch
   ```

4. **Fix any rejects** (usually include conflicts since base patch may have some overlapping changes)

5. **Generate combined patch**:
   ```bash
   # Add new files (e.g., FontSpacingSeedManager.cpp/h)
   git add dom/base/FontSpacingSeedManager.cpp
   git add dom/base/FontSpacingSeedManager.h
   git add dom/base/RoverfoxStorageManager.cpp
   git add dom/base/RoverfoxStorageManager.h

   # Generate combined patch
   git diff --cached --binary > /tmp/anti-font-fingerprinting.patch
   git diff --binary >> /tmp/anti-font-fingerprinting.patch

   # Replace base patch
   cp /tmp/anti-font-fingerprinting.patch ../patches/anti-font-fingerprinting.patch
   ```

6. **Verify combined patch**:
   ```bash
   cd ..
   make clean
   cd camoufox-<version>
   patch -p1 < ../patches/anti-font-fingerprinting.patch
   find . -name '*.rej' -type f  # Should be empty
   ```

### What Context Patches Add

Context patches typically add:

1. **Manager classes** (e.g., FontSpacingSeedManager, WebRTCIPManager):
   - Store per-context settings using RoverfoxStorageManager
   - Provide WebIDL-compatible enable/disable checks
   - Handle self-destructing functions

2. **Window.webidl functions**:
   - JavaScript APIs exposed to Playwright
   - Examples: `setFontSpacingSeed()`, `setWebRTCIPv4()`

3. **nsGlobalWindowInner.cpp implementations**:
   - Extract userContextId from window/document/docshell
   - Call manager classes
   - Self-destruct logic (remove function after first use)

4. **Core logic changes**:
   - Replace global config (MaskConfig) with per-context manager
   - Pass userContextId through call chains
   - Query manager for per-context values

---

## Testing and Validation

### Minimal Verification

After updating a patch, always verify:

1. **Patch applies cleanly**:
   ```bash
   make clean
   cd camoufox-<version>
   patch -p1 < ../patches/patch-name.patch
   find . -name '*.rej' -type f
   ```

2. **No reject files remain**

3. **Build compiles** (if feasible):
   ```bash
   cd ..
   make build
   ```

### Full Testing

For critical patches, test with actual Playwright scenarios after building.

---

## Best Practices

### DO:

1. ✅ **Always use `make clean`** to reset Firefox source
2. ✅ **Read and understand** what the patch is trying to do before fixing rejects
3. ✅ **Search for API changes** in Firefox release notes when functions have changed
4. ✅ **Use grep/search** extensively to find where code moved
5. ✅ **Extract userContextId properly** using the standard pattern
6. ✅ **Test patches apply cleanly** before considering them done
7. ✅ **Keep commits atomic** - one patch fix per session
8. ✅ **Document major API changes** you discover

### DON'T:

1. ❌ **Don't use `git reset` or `git clean`** on Firefox source directory
2. ❌ **Don't leave TODO comments** - fix things properly as you go
3. ❌ **Don't guess parameter values** - extract them properly or investigate
4. ❌ **Don't skip verification** - always test the patch applies cleanly
5. ❌ **Don't batch multiple patch updates** - do them one at a time
6. ❌ **Don't assume line numbers are correct** in reject files
7. ❌ **Don't ignore warnings** during patch application

### Common Pitfalls

1. **Assuming reject line numbers are accurate**: They're usually wrong in new Firefox versions
2. **Not understanding API changes**: Firefox refactors often - read the new code
3. **Forgetting to add new files**: Use `git add` before generating patch
4. **Not testing on clean source**: Always verify with `make clean`
5. **Leaving reject files**: Remove all `.rej` files after fixing

---

## Example: Complete Patch Update Session

Here's a complete example of updating `0-playwright.patch` from Firefox 144 to Firefox 146:

### 1. Reset and Apply

```bash
make clean
cd camoufox-146.0.1-beta.25
patch -p1 < ../patches/0-playwright.patch
```

### 2. Find Rejects

```bash
find . -name '*.rej' -type f
```

Output shows 20 reject files.

### 3. Analyze First Reject

```bash
cat dom/base/Navigator.cpp.rej
```

Shows parameter order changed in `GetAcceptLanguages`.

### 4. Fix the Reject

Search for the function in the actual file, understand the new signature, apply changes manually.

### 5. Repeat for All Rejects

Work through each reject systematically.

### 6. Discover API Change

Firefox 146 refactored mouse events from individual parameters to `SynthesizeMouseEventData` and `SynthesizeMouseEventOptions`. Port all mouse event logic to new API.

### 7. Remove Rejects

```bash
rm -f dom/base/Navigator.cpp.rej dom/base/Element.cpp.rej ...
find . -name '*.rej' -type f  # Verify empty
```

### 8. Generate New Patch

```bash

... [TRUNCATED]
```

### File: multibuild.py
```py
"""
Easy build CLI for Camoufox

options:
  -h, --help            show this help message and exit
  --target {linux,windows,macos} [{linux,windows,macos} ...]
                        Target platforms to build
  --arch {x86_64,arm64,i686} [{x86_64,arm64,i686} ...]
                        Target architectures to build for each platform
  --bootstrap           Bootstrap the build system
  --clean               Clean the build directory before starting

Example:
$ python3 multibuild.py --target linux windows macos --arch x86_64 arm64

Since Camoufox is NOT meant to be used as a daily driver, no installers are provided.
"""

import argparse
import glob
import os
from pathlib import Path
import sys
from dataclasses import dataclass
from typing import List
import shutil

# Constants
AVAILABLE_TARGETS = ["linux", "windows", "macos"]
AVAILABLE_ARCHS = ["x86_64", "arm64", "i686"]


def setup_linux_sysroots():
    """
    Set up symlinks required for Linux cross-compilation.
    The sysroots may be missing the libsqlite3.so symlink needed for linking.
    """
    mozbuild = Path.home() / '.mozbuild'
    sysroots = [
        ('sysroot-aarch64-linux-gnu', 'aarch64-linux-gnu'),
        ('sysroot-x86_64-linux-gnu', 'x86_64-linux-gnu'),
        ('sysroot-i686-linux-gnu', 'i686-linux-gnu'),
    ]

    for sysroot_name, lib_arch in sysroots:
        sysroot_lib = mozbuild / sysroot_name / 'usr' / 'lib' / lib_arch
        sqlite_so = sysroot_lib / 'libsqlite3.so'
        sqlite_so_0 = sysroot_lib / 'libsqlite3.so.0'

        if sysroot_lib.exists() and sqlite_so_0.exists() and not sqlite_so.exists():
            print(f"Creating libsqlite3.so symlink in {sysroot_lib}")
            sqlite_so.symlink_to('libsqlite3.so.0')


def run(cmd, exit_on_fail=True):
    print(f'\n------------\n{cmd}\n------------\n')
    retval = os.system(cmd)
    if retval != 0 and exit_on_fail:
        print(f"fatal error: command '{cmd}' failed")
        sys.exit(1)
    return retval


@dataclass
class BSYS:
    target: str
    arch: str

    @staticmethod
    def bootstrap():
        """Bootstrap the build system"""
        run('make bootstrap')

    @staticmethod
    def generate_assets_car():
        """Generate Assets.car for macOS builds"""
        run('make generate-assets-car')

    def build(self):
        """Build the Camoufox source code"""
        os.environ['BUILD_TARGET'] = f'{self.target},{self.arch}'
        run('make build')

    def package(self):
        """Package the Camoufox source code"""
        run(f'make package-{self.target} arch={self.arch}')

    def update_target(self):
        """Change the build target"""
        os.environ['BUILD_TARGET'] = f'{self.target},{self.arch}'
        run('make set-target')

    @property
    def assets(self) -> List[str]:
        """Get the list of assets"""
        package_pattern = f'camoufox-*-{self.target[:3]}.{self.arch}.zip'
        return glob.glob(package_pattern)

    @staticmethod
    def clean():
        """Clean the Camoufox directory"""
        run('make clean')


def run_build(target, arch):
    """
    Run the build for the given target and architecture
    """
    builder = BSYS(target, arch)
    builder.update_target()
    # Run build
    builder.build()
    # Run package
    builder.package()
    # Move assets to dist
    print('Assets:', ', '.join(builder.assets))
    for asset in builder.assets:
        shutil.move(asset, f'dist/{asset}')


def main():
    parser = argparse.ArgumentParser(description="Easy build CLI for Camoufox")
    parser.add_argument(
        "--target",
        choices=AVAILABLE_TARGETS,
        nargs='+',
        required=True,
        help="Target platform for the build",
    )
    parser.add_argument(
        "--arch",
        choices=AVAILABLE_ARCHS,
        nargs='+',
        required=True,
        help="Target architecture for the build",
    )
    parser.add_argument("--bootstrap", action="store_true", help="Bootstrap the build system")
    parser.add_argument(
        "--clean", action="store_true", help="Clean the build directory before starting"
    )

    args = parser.parse_args()

    # Run bootstrap if requested
    if args.bootstrap:
        BSYS.bootstrap()
    # Clean if requested
    if args.clean:
        BSYS.clean()
    # Generate Assets.car if building for macOS
    if 'macos' in args.target:
        BSYS.generate_assets_car()

    # Ensure dist directory exists
    os.makedirs('dist', exist_ok=True)

    # Set up Linux sysroot symlinks if needed
    if 'linux' in args.target:
        setup_linux_sysroots()

    # Run build
    for target in args.target:
        for arch in args.arch:
            if (target, arch) in [("windows", "arm64"), ("macos", "i686")]:
                print(f"Skipping {target} {arch}: Unsupported architecture.")
                continue
            run_build(target, arch)


if __name__ == "__main__":
    main()

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
