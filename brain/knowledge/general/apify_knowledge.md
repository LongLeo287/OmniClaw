---
id: apify-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:49.776346
---

# KNOWLEDGE EXTRACT: apify
> **Extracted on:** 2026-03-30 17:29:10
> **Source:** apify

---

## File: `agent-skills.md`
```markdown
# 📦 apify/agent-skills [🔖 PENDING/APPROVE]
🔗 https://github.com/apify/agent-skills


## Meta
- **Stars:** ⭐ 1751 | **Forks:** 🍴 183
- **Language:** JavaScript | **License:** Unknown
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Collection of Apify Agent Skills

## README (trích đầu)
```
# Apify Agent Skills

A collection of AI agent skills for web scraping, data extraction, and Actor development on the Apify platform.

> Looking for more specialized skills? Check out [apify/awesome-skills](https://github.com/apify/awesome-skills) — a community collection of domain-specific skills for lead generation, brand monitoring, competitor intelligence, and more.

## Skills

### Scraping

- **[Ultimate scraper](skills/apify-ultimate-scraper/)** (`apify-ultimate-scraper`) — AI-powered web scraper for 55+ platforms including Instagram, Facebook, TikTok, YouTube, Google Maps, Amazon, Walmart, eBay, Booking.com, TripAdvisor, and more. Can also search the [Apify Store](https://apify.com/store) to find the right Actor for any platform not listed here.

### Development

- **[Actor development](skills/apify-actor-development/)** (`apify-actor-development`) — create, debug, and deploy Apify Actors from scratch in JavaScript, TypeScript, or Python.
- **[Actorization](skills/apify-actorization/)** (`apify-actorization`) — convert existing projects into Apify Actors. Supports JS/TS (SDK), Python (async context manager), and any language (CLI wrapper).
- **[Generate output schema](skills/apify-generate-output-schema/)** (`apify-generate-output-schema`) — generate output schemas (`dataset_schema.json`, `output_schema.json`, `key_value_store_schema.json`) for an Apify Actor by analyzing its source code.

## Installation

```bash
npx skills add apify/agent-skills
```

### Claude Code

```bash
# Add the marketplace
/plugin marketplace add https://github.com/apify/agent-skills

# Install a skill
/plugin install apify-ultimate-scraper@apify-agent-skills
```

### Cursor / Windsurf

Add to your project's `.cursor/settings.json` or use the same Claude Code plugin format.

### Codex / Gemini CLI

Point your agent to the `agents/AGENTS.md` file which contains skill descriptions and paths:

```bash
# Gemini CLI uses gemini-extension.json automatically
# For Codex, reference agents/AGENTS.md in your configuration
```

### Other AI tools

Any AI tool that supports Markdown context can use the skills by pointing to:
- `agents/AGENTS.md` - auto-generated skill index
- `skills/*/SKILL.md` - individual skill documentation

## Prerequisites

1. **Apify account** — [apify.com](https://apify.com)
2. **API token** — get from [Apify Console](https://console.apify.com/account/integrations), add `APIFY_TOKEN=your_token` to `.env`
3. **Node.js 20.6+** (for the scraper skill)

## Pricing

Apify Actors use pay-per-result pricing. Check individual Actor pricing on the [Apify platform](https://apify.com).

## Support

- [Apify Documentation](https://docs.apify.com)
- [Apify Discord](https://discord.gg/jyEM2PRvMU)

## License

[Apache-2.0](LICENSE)

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `crawlee.md`
```markdown
# 📦 apify/crawlee [🔖 PENDING/APPROVE]
🔗 https://github.com/apify/crawlee
🌐 https://crawlee.dev

## Meta
- **Stars:** ⭐ 22515 | **Forks:** 🍴 1287
- **Language:** TypeScript | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Crawlee—A web scraping and browser automation library for Node.js to build reliable crawlers. In JavaScript and TypeScript. Extract data for AI, LLMs, RAG, or GPTs. Download HTML, PDF, JPG, PNG, and other files from websites. Works with Puppeteer, Playwright, Cheerio, JSDOM, and raw HTTP. Both headful and headless mode. With proxy rotation.

## README (trích đầu)
```
<h1 align="center">
    <a href="https://crawlee.dev">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/apify/crawlee/master/website/static/img/crawlee-dark.svg?sanitize=true">
          <img alt="Crawlee" src="https://raw.githubusercontent.com/apify/crawlee/master/website/static/img/crawlee-light.svg?sanitize=true" width="500">
        </picture>
    </a>
    <br>
    <small>A web scraping and browser automation library</small>
</h1>

<p align=center>
    <a href="https://trendshift.io/repositories/5179" target="_blank"><img src="https://trendshift.io/api/badge/repositories/5179" alt="apify%2Fcrawlee | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>

<p align=center>
    <a href="https://www.npmjs.com/package/@crawlee/core" rel="nofollow"><img src="https://img.shields.io/npm/v/@crawlee/core.svg" alt="NPM latest version" data-canonical-src="https://img.shields.io/npm/v/@crawlee/core/next.svg" style="max-width: 100%;"></a>
    <a href="https://www.npmjs.com/package/@crawlee/core" rel="nofollow"><img src="https://img.shields.io/npm/dm/@crawlee/core.svg" alt="Downloads" data-canonical-src="https://img.shields.io/npm/dm/@crawlee/core.svg" style="max-width: 100%;"></a>
    <a href="https://discord.gg/jyEM2PRvMU" rel="nofollow"><img src="https://img.shields.io/discord/801163717915574323?label=discord" alt="Chat on discord" data-canonical-src="https://img.shields.io/discord/801163717915574323?label=discord" style="max-width: 100%;"></a>
    <a href="https://github.com/apify/crawlee/actions/workflows/test-ci.yml"><img src="https://github.com/apify/crawlee/actions/workflows/test-ci.yml/badge.svg?branch=master" alt="Build Status" style="max-width: 100%;"></a>
</p>

Crawlee covers your crawling and scraping end-to-end and **helps you build reliable scrapers. Fast.**

Your crawlers will appear human-like and fly under the radar of modern bot protections even with the default configuration. Crawlee gives you the tools to crawl the web for links, scrape data, and store it to disk or cloud while staying configurable to suit your project's needs.

Crawlee is available as the [`crawlee`](https://www.npmjs.com/package/crawlee) NPM package.

> 👉 **View full documentation, guides and examples on the [Crawlee project website](https://crawlee.dev)** 👈

> Do you prefer 🐍 Python instead of JavaScript? [👉 Checkout Crawlee for Python 👈](https://github.com/apify/crawlee-python).

## Installation

We recommend visiting the [Introduction tutorial](https://crawlee.dev/js/brain/knowledge/docs_legacy/introduction) in Crawlee documentation for more information.

> Crawlee requires **Node.js 16 or higher**.

### With Crawlee CLI

The fastest way to try Crawlee out is to use the **Crawlee CLI** and choose the **Getting started example**. The CLI will install all the necessary dependencies and add boilerplate code for you to play with.

```bash
npx crawlee create my-crawler
```

```bash
cd my-crawler
npm 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

