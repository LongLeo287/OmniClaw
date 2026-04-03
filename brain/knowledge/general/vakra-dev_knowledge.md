---
id: vakra-dev-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:40.261327
---

# KNOWLEDGE EXTRACT: vakra-dev
> **Extracted on:** 2026-03-30 17:58:06
> **Source:** vakra-dev

---

## File: `reader.md`
```markdown
# 📦 vakra-dev/reader [🔖 PENDING/APPROVE]
🔗 https://github.com/vakra-dev/reader
🌐 https://reader.dev

## Meta
- **Stars:** ⭐ 481 | **Forks:** 🍴 33
- **Language:** TypeScript | **License:** Apache-2.0
- **Last updated:** 2026-03-23
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Open-source, production-grade web scraping engine built for LLMs. Scrape and crawl the entire web, clean markdown, ready for your agents.

## README (trích đầu)
```
<p align="center">
  <img src="docs/assets/logo.png" alt="Reader Logo" width="200" />
</p>

<h1 align="center">Reader</h1>

<p align="center">
  <strong>Open-source, production-grade web scraping engine built for LLMs.</strong>
</p>

<p align="center">
  Scrape and crawl the entire web, clean markdown, ready for your agents.
</p>

<p align="center">
  <a href="https://opensource.org/licenses/Apache-2.0"><img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="License: Apache 2.0"></a>
  <a href="https://www.npmjs.com/package/@vakra-dev/reader"><img src="https://img.shields.io/npm/v/@vakra-dev/reader.svg" alt="npm version"></a>
  <a href="https://github.com/vakra-dev/reader/stargazers"><img src="https://img.shields.io/github/stars/vakra-dev/reader.svg?style=social" alt="GitHub stars"></a>
</p>

<p align="center">
  <a href="https://docs.reader.dev">Docs</a> · <a href="https://docs.reader.dev/home/examples">Examples</a> · <a href="https://discord.gg/6tjkq7J5WV">Discord</a>
</p>

<p align="center">
  <img src="./docs/assets/demo.gif" alt="Reader demo — scrape any URL to clean markdown" width="700" />
</p>

## The Problem

Building agents that need web access is frustrating. You piece together Puppeteer, add stealth plugins, fight Cloudflare, manage proxies and it still breaks in production.

Because production grade web scraping isn't about rendering a page and converting HTML to markdown. It's about everything underneath:

| Layer                    | What it actually takes                                              |
| ------------------------ | ------------------------------------------------------------------- |
| **Browser architecture** | Managing browser instances at scale, not one-off scripts            |
| **Anti-bot bypass**      | Cloudflare, Turnstile, JS challenges, they all block naive scrapers |
| **TLS fingerprinting**   | Real browsers have fingerprints. Puppeteer doesn't. Sites know.     |
| **Proxy infrastructure** | Datacenter vs residential, rotation strategies, sticky sessions     |
| **Resource management**  | Browser pooling, memory limits, graceful recycling                  |
| **Reliability**          | Rate limiting, retries, timeouts, caching, graceful degradation     |

I built **Reader**, a production-grade web scraping engine on top of [Ulixee Hero](https://ulixee.org/), a headless browser designed for exactly this.

## The Solution

Two primitives. That's it.

```typescript
import { ReaderClient } from "@vakra-dev/reader";

const reader = new ReaderClient();

// Scrape URLs → clean markdown
const result = await reader.scrape({ urls: ["https://example.com"] });
console.log(result.data[0].markdown);

// Crawl a site → discover + scrape pages
const pages = await reader.crawl({
  url: "https://example.com",
  depth: 2,
  scrape: true,
});
console.log(`Found ${pages.urls.length} pages`);
```

All the hard stuff, browser pooling, challenge detection, proxy rotation, retries, happens under the hood. You ge
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

