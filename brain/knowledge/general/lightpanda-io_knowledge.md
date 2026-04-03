---
id: lightpanda-io-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:04.191720
---

# KNOWLEDGE EXTRACT: lightpanda-io
> **Extracted on:** 2026-03-30 17:40:16
> **Source:** lightpanda-io

---

## File: `browser.md`
```markdown
# 📦 lightpanda-io/browser [🔖 PENDING/APPROVE]
🔗 https://github.com/lightpanda-io/browser
🌐 https://lightpanda.io

## Meta
- **Stars:** ⭐ 24958 | **Forks:** 🍴 1009
- **Language:** Zig | **License:** AGPL-3.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Lightpanda: the headless browser designed for AI and automation

## README (trích đầu)
```
<p align="center">
  <a href="https://lightpanda.io"><img src="https://cdn.lightpanda.io/assets/images/logo/lpd-logo.png" alt="Logo" height=170></a>
</p>
<h1 align="center">Lightpanda Browser</h1>
<p align="center">
<strong>The headless browser built from scratch for AI agents and automation.</strong><br>
Not a Chromium fork. Not a WebKit patch. A new browser, written in Zig.
</p>

</div>
<div align="center">

[![License](https://img.shields.io/github/license/lightpanda-io/browser)](https://github.com/lightpanda-io/browser/blob/main/LICENSE)
[![Twitter Follow](https://img.shields.io/twitter/follow/lightpanda_io)](https://twitter.com/lightpanda_io)
[![GitHub stars](https://img.shields.io/github/stars/lightpanda-io/browser)](https://github.com/lightpanda-io/browser)
[![Discord](https://img.shields.io/discord/1391984864894521354?style=flat-square&label=discord)](https://discord.gg/K63XeymfB5)

</div>
<div align="center">

[<img width="350px" src="https://cdn.lightpanda.io/assets/images/github/execution-time-v2.svg">
](https://github.com/lightpanda-io/demo)
&emsp;
[<img width="350px" src="https://cdn.lightpanda.io/assets/images/github/memory-frame-v2.svg">
](https://github.com/lightpanda-io/demo)
</div>

_chromedp requesting 933 real web pages over the network on a AWS EC2 m5.large instance.
See [benchmark details](https://github.com/lightpanda-io/demo/blob/main/BENCHMARKS.md#crawler-benchmark)._

Lightpanda is the open-source browser made for headless usage:

- Javascript execution
- Support of Web APIs (partial, WIP)
- Compatible with Playwright[^1], Puppeteer, chromedp through [CDP](https://chromedevtools.github.io/devtools-protocol/)

Fast web automation for AI agents, LLM training, scraping and testing:

- Ultra-low memory footprint (9x less than Chrome)
- Exceptionally fast execution (11x faster than Chrome)
- Instant startup

[^1]: **Playwright support disclaimer:**
Due to the nature of Playwright, a script that works with the current version of the browser may not function correctly with a future version. Playwright uses an intermediate JavaScript layer that selects an execution strategy based on the browser's available features. If Lightpanda adds a new [Web API](https://developer.mozilla.org/en-US/docs/Web/API), Playwright may choose to execute different code for the same script. This new code path could attempt to use features that are not yet implemented. Lightpanda makes an effort to add compatibility tests, but we can't cover all scenarios. If you encounter an issue, please create a [GitHub issue](https://github.com/lightpanda-io/browser/issues) and include the last known working version of the script.

## Quick start

### Install
**Install from the nightly builds**

You can download the last binary from the [nightly
builds](https://github.com/lightpanda-io/browser/releases/tag/nightly) for
Linux x86_64 and MacOS aarch64.

*For Linux*
```console
curl -L -o lightpanda https://github.com/lightpanda-io/browser/releases/download/nightly/lig
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

