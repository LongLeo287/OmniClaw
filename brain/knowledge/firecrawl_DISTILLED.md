---
id: firecrawl
type: knowledge
owner: OA_Triage
---
# firecrawl
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<h3 align="center">
  <a name="readme-top"></a>
  <img
    src="https://raw.githubusercontent.com/firecrawl/firecrawl/main/img/firecrawl_logo.png"
    height="200"
  >
</h3>

<div align="center">
  <a href="https://github.com/firecrawl/firecrawl/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/firecrawl/firecrawl" alt="License">
  </a>
  <a href="https://pepy.tech/project/firecrawl-py">
    <img src="https://static.pepy.tech/badge/firecrawl-py" alt="Downloads">
  </a>
  <a href="https://GitHub.com/firecrawl/firecrawl/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/firecrawl/firecrawl.svg" alt="GitHub Contributors">
  </a>
  <a href="https://firecrawl.dev">
    <img src="https://img.shields.io/badge/Visit-firecrawl.dev-orange" alt="Visit firecrawl.dev">
  </a>
</div>

<div>
  <p align="center">
    <a href="https://twitter.com/firecrawl">
      <img src="https://img.shields.io/badge/Follow%20on%20X-000000?style=for-the-badge&logo=x&logoColor=white" alt="Follow on X" />
    </a>
    <a href="https://www.linkedin.com/company/104100957">
      <img src="https://img.shields.io/badge/Follow%20on%20LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Follow on LinkedIn" />
    </a>
    <a href="https://discord.gg/firecrawl">
      <img src="https://img.shields.io/badge/Join%20our%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Join our Discord" />
    </a>
  </p>
</div>

---

# **🔥 Firecrawl**

**Turn websites into LLM-ready data.** 

[**Firecrawl**](https://firecrawl.dev/?ref=github) is an API that scrapes, crawls, and extracts structured data from any website, powering AI agents and apps with real-time context from the web.

Looking for our MCP? Check out the repo [here](https://github.com/firecrawl/firecrawl-mcp-server).

*This repository is in development, and we're still integrating custom modules into the mono repo. It's not fully ready for self-hosted deployment yet, but you can run it locally.*

_Pst. Hey, you, join our stargazers :)_

<a href="https://github.com/firecrawl/firecrawl">
  <img src="https://img.shields.io/github/stars/firecrawl/firecrawl.svg?style=social&label=Star&maxAge=2592000" alt="GitHub stars">
</a>

---

## Why Firecrawl?

- **LLM-ready output**: Clean markdown, structured JSON, screenshots, HTML, and more
- **Industry-leading reliability**: >80% coverage on [benchmark evaluations](https://www.firecrawl.dev/blog/the-worlds-best-web-data-api-v25), outperforming every other provider tested
- **Handles the hard stuff**: Proxies, JavaScript rendering, and dynamic content that breaks other scrapers
- **Customization**: Exclude tags, crawl behind auth walls, max depth, and more
- **Media parsing**: Automatic text extraction from PDFs, DOCX, and images
- **Actions**: Click, scroll, input, wait, and more before extracting
- **Batch processing**: Scrape thousands of URLs asynchronously
- **Change tracking**: Monitor website content changes over time

---

## Quick Start

Sign up at [firecrawl.dev](https://firecrawl.dev) to get your API key and start extracting data in seconds. Try the [playground](https://firecrawl.dev/playground) to test it out.

### Make Your First API Request
```bash
curl -X POST 'https://api.firecrawl.dev/v2/scrape' \
  -H 'Authorization: Bearer fc-YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{"url": "https://example.com"}'
```

Response:
```json
{
  "success": true,
  "data": {
    "markdown": "# Example Domain\n\nThis domain is for use in illustrative examples...",
    "metadata": {
      "title": "Example Domain",
      "sourceURL": "https://example.com"
    }
  }
}
```

### Install the Firecrawl Skill & CLI

The Firecrawl Skill is an easy way for AI agents such as [Claude Code](https://claude.ai/code), [Antigravity](https://antigravity.google) and [OpenCode](https://opencode.ai) to use Firecrawl through the CLI.

Install and configure the skill for all detected AI coding agents:
```bash
npx -y firecrawl-cli@latest init --all --browser
```

After installing, restart your agent for it to discover the new skill.

You can also install the CLI globally:
```bash
npm install -g firecrawl-cli
```

Authenticate with your API key:
```bash
# Interactive login (opens browser)
firecrawl login --browser

# Or login with API key directly
firecrawl login --api-key fc-YOUR_API_KEY

# Or set via environment variable
export FIRECRAWL_API_KEY=fc-YOUR_API_KEY
```

Try a quick scrape:
```bash
firecrawl https://example.com --only-main-content
```

See the full [Skill + CLI documentation](https://docs.firecrawl.dev/sdks/cli) for all available commands including search, map, crawl, agent, and browser automation.

---

## Feature Overview

| Feature | Description |
|---------|-------------|
| [**Scrape**](#scraping) | Convert any URL to markdown, HTML, screenshots, or structured JSON |
| [**Search**](#search) | Search the web and get full page content from results |
| [**Browse**](#browse) | Let agents safely interact with the web |
| [**Map**](#map) | Discover all URLs on a website instantly |
| [**Crawl**](#crawling) | Scrape all URLs of a website with a single request |
| [**Agent**](#agent) | Automated data gathering, just describe what you need |
---

## Scrape

Convert any URL to clean markdown, HTML, or structured data.
```bash
curl -X POST 'https://api.firecrawl.dev/v2/scrape' \
  -H 'Authorization: Bearer fc-YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://docs.firecrawl.dev",
    "formats": ["markdown", "html"]
  }'
```

Response:
```json
{
  "success": true,
  "data": {
    "markdown": "# Firecrawl Docs\n\nTurn websites into LLM-ready data...",
    "html": "<!DOCTYPE html><html>...",
    "metadata": {
      "title": "Quickstart | Firecrawl",
      "description": "Firecrawl allows you to turn entire websites into LLM-ready markdown",
      "sourceURL": "https://docs.firecrawl.dev",
      "statusCode": 200
    }
  }
}
```

### Extract Structured Data (JSON Mode)

Extract structured data using a schema:
```python
from firecrawl import Firecrawl
from pydantic import BaseModel

app = Firecrawl(API_KEY='[REDACTED_API_KEY]')

class CompanyInfo(BaseModel):
    company_mission: str
    is_open_source: bool
    is_in_yc: bool

result = app.scrape(
    'https://firecrawl.dev',
    formats=[{"type": "json", "schema": CompanyInfo.model_json_schema()}]
)

print(result.json)
```
```json
{"company_mission": "Turn websites into LLM-ready data", "is_open_source": true, "is_in_yc": true}
```

Or extract with just a prompt (no schema):
```python
result = app.scrape(
    'https://firecrawl.dev',
    formats=[{"type": "json", "prompt": "Extract the company mission"}]
)
```

### Scrape Formats

Available formats: `markdown`, `html`, `rawHtml`, `screenshot`, `links`, `json`, `branding`

**Get a screenshot**
```python
doc = app.scrape("https://firecrawl.dev", formats=["screenshot"])
print(doc.screenshot)  # Base64 encoded image
```

**Extract brand identity (colors, fonts, typography)**
```python
doc = app.scrape("https://firecrawl.dev", formats=["branding"])
print(doc.branding)  # {"colors": {...}, "fonts": [...], "typography": {...}}
```

### Actions (Interact Before Scraping)

Click, type, scroll, and more before extracting:
```python
doc = app.scrape(
    url="https://example.com/login",
    formats=["markdown"],
    actions=[
        {"type": "write", "text": "user@example.com"},
        {"type": "press", "key": "Tab"},
        {"type": "write", "text": "password"},
        {"type": "click", "selector": 'button[type="submit"]'},
        {"type": "wait", "milliseconds": 2000},
        {"type": "screenshot"}
    ]
)
```

---

## Search

Search the web and optionally scrape the results.
```bash
curl -X POST 'https://api.firecrawl.dev/v2/search' \
  -H 'Authorization: Bearer fc-YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "firecrawl web scraping",
    "limit": 5
  }'
```

Response:
```json
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://www.firecrawl.dev/",
        "title": "Firecrawl - The Web Data API for AI",
        "description": "The web crawling, scraping, and search API for AI.",
        "position": 1
      }
    ],
    "images": [...],
    "news": [...]
  }
}
```

### Search with Content Scraping

Get the full content of search results:
```python
from firecrawl import Firecrawl

firecrawl = Firecrawl(API_KEY='[REDACTED_API_KEY]')

results = firecrawl.search(
    "firecrawl web scraping",
    limit=3,
    scrape_options={
        "formats": ["markdown", "links"]
    }
)
```

---

## Browse

Give your agents a secure browser environment. Let them run code safely to gather data and take action on the web.
```bash
curl -X POST 'https://api.firecrawl.dev/v2/browser' \
  -H 'Authorization: Bearer fc-YOUR_API_KEY' \
  -H 'Content-Type: application/json'
```

Response:
```json
{
  "success": true,
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "cdpUrl": "wss://cdp-proxy.firecrawl.dev/cdp/550e8400-e29b-41d4-a716-446655440000",
  "liveViewUrl": "https://liveview.firecrawl.dev/550e8400-e29b-41d4-a716-446655440000"
}
```

### Execute Code in the Browser

Run Playwright code, Python, or bash commands remotely:
```javascript
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ API_KEY='[REDACTED_API_KEY]' });

// 1. Launch a session
const session = await firecrawl.browser();

// 2. Execute code
const result = await firecrawl.browserExecute(session.id, {
  code: `
    await page.goto("https://news.ycombinator.com");
    const title = await page.title();
    console.log(title);
  `,
  language: "node",
});
console.log(result.result); // "Hacker News"

// 3. Close
await firecrawl.deleteBrowser(session.id);
```

### Persistent Sessions

Save and reuse browser state (cookies, localStorage) across sessions:
```javascript
const session = await firecrawl.browser({
  ttl: 600,
  profile: {
    name: "my-profile",
    saveChanges: true,
  },
});
```

### agent-browser (Bash Mode)

Instead of writing Playwright code, agents can send simple bash commands via [agent-browser](https://github.com/vercel-labs/agent-browser):
```bash
firecrawl browser "open https://example.com"
firecrawl browser "snapshot"
firecrawl browser "click @e5"
```

---

## Agent

**The easiest way to get data from the web.** Describe what you need, and our AI agent searches, navigates, and extracts it. No URLs required.

Agent is the evolution of our `/extract` endpoint: faster, more reliable, and doesn't require you to know the URLs upfront.
```bash
curl -X POST 'https://api.firecrawl.dev/v2/agent' \
  -H 'Authorization: Bearer fc-YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "prompt": "Find the pricing plans for Notion"
  }'
```

Response:
```json
{
  "success": true,
  "data": {
    "result": "Notion offers the following pricing plans:\n\n1. Free - $0/month...\n2. Plus - $10/seat/month...\n3. Business - $18/seat/month...",
    "sources": ["https://www.notion.so/pricing"]
  }
}
```

### Agent with Structured Output

Use a schema to get structured data:
```python
from firecrawl import Firecrawl
from pydantic import BaseModel, Field
from typing import List, Optional

app = Firecrawl(API_KEY='[REDACTED_API_KEY]')

class Founder(BaseModel):
    name: str = Field(description="Full name of the founder")
    role: Optional[str] = Field(None, description="Role or position")

class FoundersSchema(BaseModel):
    founders: List[Founder] = Field(description="List of founders")

result = app.agent(
    prompt="Find the founders of Firecrawl",
    schema=FoundersSchema
)

print(result.data)
```
```json
{
  "founders": [
    {"name": "Eric Ciarla", "role": "Co-founder"},
    {"name": "Nicolas Camara", "role": "Co-founder"},
    {"name": "Caleb Peffer", "role": "Co-founder"}
  ]
}
```

### Agent with URLs (Optional)

Focus the agent on specific pages:
```python
result = app.agent(
    urls=["https://docs.firecrawl.dev", "https://firecrawl.dev/pricing"],
    prompt="Compare the features and pricing information"
)
```

### Model Selection

Choose between two models based on your needs:

| Model | Cost | Best For |
|-------|------|----------|
| `spark-1-mini` (default) | 60% cheaper | Most tasks |
| `spark-1-pro` | Standard | Complex research, critical extraction |
```python
result = app.agent(
    prompt="Compare enterprise features across Firecrawl, Apify, and ScrapingBee",
    model="spark-1-pro"
)
```

**When to use Pro:**
- Comparing data across multiple websites
- Extracting from sites with complex navigation or auth
- Research tasks where the agent needs to explore multiple paths
- Critical data where accuracy is paramount

Learn more about Spark models in our [Agent documentation](https://docs.firecrawl.dev/features/agent).

### Using Firecrawl with AI agents

Install the Firecrawl skill to let AI agents like Claude Code, Codex, and OpenCode use Firecrawl automatically:
```bash
npx skills add firecrawl/cli
```

Restart your agent after installing. See the [Skill + CLI docs](https://docs.firecrawl.dev/sdks/cli) for full setup.

---

## Crawling

Crawl an entire website and get content from all pages.
```bash
curl -X POST 'https://api.firecrawl.dev/v2/crawl' \
  -H 'Authorization: Bearer fc-YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://docs.firecrawl.dev",
    "limit": 100,
    "scrapeOptions": {
      "formats": ["markdown"]
    }
  }'
```

Returns a job ID:
```json
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/crawl/123-456-789"
}
```

### Check Crawl Status
```bash
curl -X GET 'https://api.firecrawl.dev/v2/crawl/123-456-789' \
  -H 'Authorization: Bearer fc-YOUR_API_KEY'
```
```json
{
  "status": "completed",
  "total": 50,
  "completed": 50,
  "creditsUsed": 50,
  "data": [
    {
      "markdown": "# Page Title\n\nContent...",
      "metadata": {"title": "Page Title", "sourceURL": "https://..."}
    }
  ]
}
```

**Note:** The [SDKs](#sdks) handle polling automatically for a better developer experience.

---

## Map

Discover all URLs on a website instantly.
```bash
curl -X POST 'https://api.firecrawl.dev/v2/map' \
  -H 'Authorization: Bearer fc-YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{"url": "https://firecrawl.dev"}'
```

Response:
```json
{
  "success": true,
  "links": [
    {"url": "https://firecrawl.dev", "title": "Firecrawl", "description": "Turn websites into LLM-ready data"},
    {"url": "https://firecrawl.dev/pricing", "title": "Pricing", "description": "Firecrawl pricing plans"},
    {"url": "https://firecrawl.dev/blog", "title": "Blog", "description": "Firecrawl blog"}
  ]
}
```

### Map with Search

Find specific URLs within a site:
```python
from firecrawl import Firecrawl

app = Firecrawl(API_KEY='[REDACTED_API_KEY]')

result = app.map("https://firecrawl.dev", search="pricing")
# Returns URLs ord
... [TRUNCATED]
```

### File: .github\scripts\requirements.txt
```txt
requests
packaging
toml
```

### File: apps\api\package.json
```json
{
  "name": "firecrawl-scraper-js",
  "version": "1.0.0",
  "description": "",
  "main": "src/index.ts",
  "scripts": {
    "start": "tsc && node dist/src/harness.js --start-built",
    "dev": "tsx src/harness.ts --start",
    "server": "tsc-watch --onSuccess \"node dist/src/index.js\"",
    "server:production": "tsc && node dist/src/index.js",
    "server:production:nobuild": "node dist/src/index.js",
    "format": "prettier --write \"src/**/*.(js|ts)\"",
    "flyio": "node dist/src/index.js",
    "start:dev": "tsc-watch --onSuccess \"node dist/src/index.js\"",
    "build": "tsc",
    "branding:print": "node src/scraper/scrapeURL/engines/fire-engine/branding-script/print-script.js",
    "build:nosentry": "tsc",
    "test": "jest --testPathIgnorePatterns=\"src/__tests__/e2e_noAuth/*\"",
    "test:local-no-auth": "jest --testPathIgnorePatterns=\"src/__tests__/e2e_withAuth/*\"",
    "test:full": "jest --testPathIgnorePatterns=\"(src/__tests__/e2e_noAuth|src/__tests__/e2e_withAuth)\"",
    "test:prod": "jest --testPathIgnorePatterns=\"(src/__tests__/e2e_noAuth|src/__tests__/e2e_full_withAuth|src/scraper/scrapeURL)\"",
    "test:snips": "jest \"src/__tests__/snips/v[12]/.+\\.test\\.ts\"",
    "harness": "tsx src/harness.ts",
    "workers": "tsc-watch --onSuccess \"node dist/src/services/queue-worker.js\"",
    "worker:production": "node dist/src/services/queue-worker.js",
    "nuq-worker": "tsc-watch --onSuccess \"node dist/src/services/worker/nuq-worker.js\"",
    "nuq-worker:production": "node dist/src/services/worker/nuq-worker.js",
    "nuq-prefetch-worker": "tsc-watch --onSuccess \"node dist/src/services/worker/nuq-prefetch-worker.js\"",
    "nuq-prefetch-worker:production": "node dist/src/services/worker/nuq-prefetch-worker.js",
    "nuq-reconciler-worker": "tsc-watch --onSuccess \"node dist/src/services/worker/nuq-reconciler-worker.js\"",
    "nuq-reconciler-worker:production": "node dist/src/services/worker/nuq-reconciler-worker.js",
    "extract-worker": "tsc-watch --onSuccess \"node dist/src/services/extract-worker.js\"",
    "extract-worker:production": "node dist/src/services/extract-worker.js",
    "index-worker": "tsc-watch --onSuccess \"node dist/src/services/indexing/index-worker.js\"",
    "index-worker:production": "node dist/src/services/indexing/index-worker.js",
    "mongo-docker": "docker run -d -p 2717:27017 -v ./mongo-data:/data/db --name mongodb mongo:latest",
    "mongo-docker-console": "docker exec -it mongodb mongosh",
    "sentry:sourcemaps": "sentry-cli sourcemaps inject --org caleb-peffer --project firecrawl-scraper-js ./dist && sentry-cli sourcemaps upload --org caleb-peffer --project firecrawl-scraper-js ./dist",
    "prepare": "cd ../.. && husky ./apps/api/.husky",
    "knip": "knip"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "@jest/globals": "^30.2.0",
    "@sentry/core": "^10.28.0",
    "@types/amqplib": "^0.10.7",
    "@types/body-parser": "^1.19.2",
    "@types/cors": "^2.8.13",
    "@types/culori": "^4.0.1",
    "@types/escape-html": "^1.0.4",
    "@types/express": "^4.17.21",
    "@types/express-ws": "^3.0.5",
    "@types/jest": "^30.0.0",
    "@types/lodash": "^4.17.14",
    "@types/node": "^22.19.1",
    "@types/pdf-parse": "^1.1.4",
    "@types/pg": "^8.15.5",
    "@types/qs": "^6.14.0",
    "@types/supertest": "^6.0.2",
    "@types/tough-cookie": "^4.0.5",
    "husky": "^9.1.7",
    "jest": "^30.2.0",
    "jest-junit": "^16.0.0",
    "knip": "^5.70.1",
    "lint-staged": "^16.1.6",
    "supertest": "^6.3.3",
    "ts-jest": "^29.4.5",
    "tsc-watch": "^7.1.1",
    "tsx": "^4.20.3",
    "typescript": "^5.8.3",
    "undici-types": "^7.16.0"
  },
  "dependencies": {
    "@ai-sdk/anthropic": "^2.0.41",
    "@ai-sdk/deepinfra": "^1.0.27",
    "@ai-sdk/fireworks": "^1.0.27",
    "@ai-sdk/google": "^3.0.29",
    "@ai-sdk/google-vertex": "^3.0.86",
    "@ai-sdk/groq": "^2.0.28",
    "@ai-sdk/openai": "2.0.64",
    "@apidevtools/json-schema-ref-parser": "^15.1.2",
    "@bull-board/api": "^6.14.0",
    "@bull-board/express": "^6.14.0",
    "@dqbd/tiktoken": "^1.0.22",
    "@google-cloud/storage": "^7.19.0",
    "@mendable/firecrawl-rs": "workspace:*",
    "@openrouter/ai-sdk-provider": "^0.4.5",
    "@sentry/cli": "^2.58.2",
    "@sentry/node": "^10.27.0",
    "@supabase/supabase-js": "^2.52.0",
    "@types/ws": "^8.5.12",
    "@x402/core": "^2.4.0",
    "@x402/evm": "^2.4.0",
    "@x402/express": "^2.4.0",
    "ai": "6.0.86",
    "ajv": "^8.18.0",
    "ajv-formats": "^3.0.1",
    "amqplib": "^0.10.9",
    "async-mutex": "^0.5.0",
    "autumn-js": "1.1.6",
    "axios": "^1.13.5",
    "body-parser": "^1.20.3",
    "bullmq": "^5.56.7",
    "cacheable-lookup": "^6.1.0",
    "cheerio": "^1.0.0-rc.12",
    "cors": "^2.8.5",
    "culori": "^4.0.2",
    "dotenv": "^16.3.1",
    "esbuild": "^0.27.2",
    "escape-html": "^1.0.3",
    "express": "4.22.0",
    "express-ws": "^5.0.2",
    "geoip-country": "^5.0.202510312342",
    "git-diff": "^2.0.6",
    "http-cookie-agent": "^7.0.1",
    "ioredis": "^5.6.1",
    "ipaddr.js": "^2.2.0",
    "joplin-turndown-plugin-gfm": "^1.0.12",
    "jsdom": "^26.0.0",
    "koffi": "^2.9.0",
    "lodash": "^4.18.0",
    "marked": "^14.1.2",
    "ollama-ai-provider": "^1.2.0",
    "openai": "^5.20.2",
    "parse-diff": "^0.11.1",
    "pdf-parse": "^1.1.1",
    "pg": "^8.16.3",
    "prettier": "^3.6.2",
    "prom-client": "^15.1.3",
    "psl": "^1.15.0",
    "qs": "^6.15.0",
    "rate-limiter-flexible": "2.4.2",
    "redlock": "5.0.0-beta.2",
    "resend": "^3.5.0",
    "response-time": "^2.3.4",
    "robots-parser": "^3.0.1",
    "stripe": "^16.1.0",
    "systeminformation": "^5.31.0",
    "tldts": "^6.1.75",
    "tough-cookie": "^4.1.4",
    "turndown": "^7.1.3",
    "undici": "7.24.1",
    "uuid": "^13.0.0",
    "winston": "^3.14.2",
    "ws": "^8.18.0",
    "xml2js": "^0.6.2",
    "zod": "4.1.12"
  },
  "nodemonConfig": {
    "ignore": [
      "*.docx",
      "*.json",
      "temp"
    ]
  },
  "pnpm": {
    "allowScripts": {
      "oxc-resolver": true
    },
    "onlyBuiltDependencies": [
      "@mendable/firecrawl-rs",
      "@sentry-internal/node-cpu-profiler",
      "@sentry/cli",
      "bigint-buffer",
      "bufferutil",
      "four-flap-bigint-buffer",
      "esbuild",
      "keccak",
      "koffi",
      "libpq",
      "msgpackr-extract",
      "oxc-resolver",
      "protobufjs",
      "supabase",
      "utf-8-validate",
      "wordpos"
    ],
    "overrides": {
      "bigint-buffer": "npm:four-flap-bigint-buffer@1.1.6",
      "diff": "^8.0.3",
      "ajv": "^8.18.0",
      "fast-xml-parser": "^5.5.7",
      "glob@>=10.2.0 <10.5.0": ">=10.5.0",
      "js-yaml@<3.14.2": ">=3.14.2",
      "qs@<6.14.2": ">=6.14.2",
      "minimatch@<10.2.3": ">=10.2.3",
      "bn.js@<5.2.3": ">=5.2.3",
      "@tootallnate/once@<3.0.1": ">=3.0.1",
      "yauzl": "^3.2.1",
      "undici": "7.24.1",
      "picomatch@<4.0.4": ">=4.0.4",
      "yaml@<2.8.3": ">=2.8.3",
      "smol-toml@<1.6.1": ">=1.6.1",
      "handlebars": ">=4.7.9",
      "path-to-regexp@~0.1.12": "0.1.13",
      "brace-expansion": ">=5.0.5"
    }
  },
  "lint-staged": {
    "*.{js,jsx,ts,tsx,json,css,md}": "prettier --write"
  },
  "packageManager": "pnpm@10.16.1"
}

```

### File: CLAUDE.md
```md
Firecrawl is a web scraper API. The directory you have access to is a monorepo:
 - `apps/api` has the actual API and worker code
 - `apps/js-sdk`, `apps/python-sdk`, `apps/rust-sdk` and `apps/java-sdk` are various SDKs

When making changes to the API, here are the general steps you should take:
1. Write some end-to-end tests that assert your win conditions, if they don't already exist
  - 1 happy path (more is encouraged if there are multiple happy paths with significantly different code paths taken)
  - 1+ failure path(s)
  - Generally, E2E (called `snips` in the API) is always preferred over unit testing.
  - In the API, always use `scrapeTimeout` from `./lib` to set the timeout you use for scrapes.
  - These tests will be ran on a variety of configurations. You should gate tests in the following manner:
    - If it requires fire-engine: `!process.env.TEST_SUITE_SELF_HOSTED`
    - If it requires AI: `!process.env.TEST_SUITE_SELF_HOSTED || process.env.OPENAI_API_KEY || process.env.OLLAMA_BASE_URL`
2. Write code to achieve your win conditions
3. Run your tests using `pnpm harness jest ...`
  - `pnpm harness` is a command that gets the API server and workers up for you to run the tests. Don't try to `pnpm start` manually.
  - The full test suite takes a long time to run, so you should try to only execute the relevant tests locally, and let CI run the full test suite.
4. Push to a branch, open a PR, and let CI run to verify your win condition.
Keep these steps in mind while building your TODO list.
```

### File: CONTRIBUTING.md
```md
# Contributors guide:

Welcome to [Firecrawl](https://firecrawl.dev) 🔥! Here are some instructions on how to get the project locally, so you can run it on your own (and contribute)

If you're contributing, note that the process is similar to other open source repos i.e. (fork firecrawl, make changes, run tests, PR). If you have any questions, and would like help getting on board, reach out to help@firecrawl.com for more or submit an issue!

## Running the project locally

First, start by installing dependencies:

1. node.js [instructions](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)
2. rust [instructions](https://www.rust-lang.org/tools/install)
3. pnpm [instructions](https://pnpm.io/installation)
4. redis [instructions](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/)
5. postgresql
6. Docker (optional) (for running postgres)

You need to set up the PostgreSQL database by running the SQL file at `apps/nuq-postgres/nuq.sql`. Easiest way is to use the docker image inside `apps/nuq-postgres`. With Docker running, build the image:

```bash
docker build -t nuq-postgres .
```

and then run:

```bash
docker run --name nuqdb \          
  -e POSTGRES_PASSWORD=postgres \
  -p 5433:5432 \
  -v nuq-data:/var/lib/postgresql/data \
  -d nuq-postgres
```

Set environment variables in a .env in the /apps/api/ directory you can copy over the template in .env.example.

To start, we won't set up authentication, or any optional sub services (pdf parsing, JS blocking support, AI features)

.env:

```
# ===== Required ENVS ======
NUM_WORKERS_PER_QUEUE=8
PORT=3002
HOST=0.0.0.0
REDIS_URL=redis://localhost:6379
REDIS_RATE_LIMIT_URL=redis://localhost:6379

## To turn on DB authentication, you need to set up supabase.
USE_DB_AUTHENTICATION=false

## Using the PostgreSQL for queuing -- change if credentials, host, or DB is different
NUQ_DATABASE_URL=postgres://postgres:postgres@localhost:5433/postgres

# ===== Optional ENVS ======

# Supabase Setup (used to support DB authentication, advanced logging, etc.)
SUPABASE_ANON_TOKEN=
SUPABASE_URL=
SUPABASE_SERVICE_TOKEN=

# Other Optionals
TEST_API_KEY= # use if you've set up authentication and want to test with a real API key
OPENAI_API_KEY= # add for LLM dependent features (image alt generation, etc.)
BULL_AUTH_KEY= @
PLAYWRIGHT_MICROSERVICE_URL=  # set if you'd like to run a playwright fallback
LLAMAPARSE_API_KEY= #Set if you have a llamaparse key you'd like to use to parse pdfs
SLACK_WEBHOOK_URL= # set if you'd like to send slack server health status messages


```

### Installing dependencies

First, install the dependencies using pnpm.

```bash
# cd apps/api # to make sure you're in the right folder
pnpm install # make sure you have pnpm version 9+!
```

### Running the project

You're going to need to open 3 terminals.

### Terminal 1 - setting up redis

Run the command anywhere within your project

```bash
redis-server
```

### Terminal 2 - setting up the service

Now, navigate to the apps/api/ directory and run:

```bash
pnpm start
# if you are going to use the [llm-extract feature](https://github.com/firecrawl/firecrawl/pull/586/), you should also export OPENAI_API_KEY=sk-______
```

This will start the workers who are responsible for processing crawl jobs.

### Terminal 3 - sending our first request.

Alright: now let’s send our first request.

```curl
curl -X GET http://localhost:3002/test
```

This should return the response Hello, world!

If you’d like to test the crawl endpoint, you can run this

```curl
curl -X POST http://localhost:3002/v1/crawl \
    -H 'Content-Type: application/json' \
    -d '{
      "url": "https://mendable.ai"
    }'
```

### Alternative: Using Docker Compose

For a simpler setup, you can use Docker Compose to run all services:

1. Prerequisites: Make sure you have Docker and Docker Compose installed
2. Copy the `.env.example` file to `.env` in the `/apps/api/` directory and configure as needed
3. From the root directory, run:

```bash
docker compose up
```

This will start Redis, the API server, and workers automatically in the correct configuration.

## Tests:

The best way to do this is run the test with `npm run test:snips`.

```

### File: docker-compose.yaml
```yaml
name: firecrawl

x-common-service: &common-service
  # NOTE: If you don't want to build the service locally,
  # comment out the build: statement and uncomment the image: statement
  # image: ghcr.io/firecrawl/firecrawl
  build: apps/api

  ulimits:
    nofile:
      soft: 65535
      hard: 65535
  networks:
    - backend
  extra_hosts:
    - "host.docker.internal:host-gateway"
  logging:
    driver: "json-file"
    options:
      max-size: "10m"
      max-file: "3"
      compress: "true"

x-common-env: &common-env
  REDIS_URL: ${REDIS_URL:-redis://redis:6379}
  REDIS_RATE_LIMIT_URL: ${REDIS_URL:-redis://redis:6379}
  PLAYWRIGHT_MICROSERVICE_URL: ${PLAYWRIGHT_MICROSERVICE_URL:-http://playwright-service:3000/scrape}
  POSTGRES_USER: ${POSTGRES_USER:-postgres}
  POSTGRES_PASSWORD: "${POSTGRES_PASSWORD:-postgres}"
  POSTGRES_DB: ${POSTGRES_DB:-postgres}
  POSTGRES_HOST: ${POSTGRES_HOST:-nuq-postgres}
  POSTGRES_PORT: ${POSTGRES_PORT:-5432}
  USE_DB_AUTHENTICATION: ${USE_DB_AUTHENTICATION:-false}
  NUM_WORKERS_PER_QUEUE: ${NUM_WORKERS_PER_QUEUE:-8}
  CRAWL_CONCURRENT_REQUESTS: ${CRAWL_CONCURRENT_REQUESTS:-10}
  MAX_CONCURRENT_JOBS: ${MAX_CONCURRENT_JOBS:-5}
  BROWSER_POOL_SIZE: ${BROWSER_POOL_SIZE:-5}
  OPENAI_API_KEY: ${OPENAI_API_KEY}
  OPENAI_BASE_URL: ${OPENAI_BASE_URL}
  MODEL_NAME: ${MODEL_NAME}
  MODEL_EMBEDDING_NAME: ${MODEL_EMBEDDING_NAME} 
  OLLAMA_BASE_URL: ${OLLAMA_BASE_URL} 
  AUTUMN_SECRET_KEY: ${AUTUMN_SECRET_KEY}
  SLACK_WEBHOOK_URL: ${SLACK_WEBHOOK_URL}
  BULL_AUTH_KEY: ${BULL_AUTH_KEY}
  TEST_API_KEY: ${TEST_API_KEY}
  SUPABASE_ANON_TOKEN: ${SUPABASE_ANON_TOKEN}
  SUPABASE_URL: ${SUPABASE_URL}
  SUPABASE_SERVICE_TOKEN: ${SUPABASE_SERVICE_TOKEN}
  SELF_HOSTED_WEBHOOK_URL: ${SELF_HOSTED_WEBHOOK_URL}
  LOGGING_LEVEL: ${LOGGING_LEVEL}
  PROXY_SERVER: ${PROXY_SERVER}
  PROXY_USERNAME: ${PROXY_USERNAME}
  PROXY_PASSWORD: ${PROXY_PASSWORD}
  SEARXNG_ENDPOINT: ${SEARXNG_ENDPOINT}
  SEARXNG_ENGINES: ${SEARXNG_ENGINES}
  SEARXNG_CATEGORIES: ${SEARXNG_CATEGORIES}

services:
  playwright-service:
    # NOTE: If you don't want to build the service locally,
    # comment out the build: statement and uncomment the image: statement
    # image: ghcr.io/firecrawl/playwright-service:latest
    build: apps/playwright-service-ts
    environment:
      PORT: 3000
      PROXY_SERVER: ${PROXY_SERVER}
      PROXY_USERNAME: ${PROXY_USERNAME}
      PROXY_PASSWORD: ${PROXY_PASSWORD}
      ALLOW_LOCAL_WEBHOOKS: ${ALLOW_LOCAL_WEBHOOKS}
      BLOCK_MEDIA: ${BLOCK_MEDIA}
      # Configure maximum concurrent pages for Playwright browser instances
      MAX_CONCURRENT_PAGES: ${CRAWL_CONCURRENT_REQUESTS:-10}
    networks:
      - backend
    # Resource limits for Docker Compose (not Swarm)
    cpus: 2.0
    mem_limit: 4G
    memswap_limit: 4G
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
        compress: "true"
    tmpfs:
      - /tmp/.cache:noexec,nosuid,size=1g

  api:
    <<: *common-service
    environment:
      <<: *common-env
      HOST: "0.0.0.0"
      PORT: ${INTERNAL_PORT:-3002}
      EXTRACT_WORKER_PORT: ${EXTRACT_WORKER_PORT:-3004}
      WORKER_PORT: ${WORKER_PORT:-3005}
      NUQ_RABBITMQ_URL: amqp://rabbitmq:5672
      ENV: local
    depends_on:
      redis:
        condition: service_started
      playwright-service:
        condition: service_started
      rabbitmq:
        condition: service_healthy
    ports:
      - "${PORT:-3002}:${INTERNAL_PORT:-3002}"
    command: node dist/src/harness.js --start-docker
    # Resource limits for Docker Compose (not Swarm)
    # Increase if you have more CPU cores/RAM available
    cpus: 4.0
    mem_limit: 8G
    memswap_limit: 8G

  redis:
    # NOTE: If you want to use Valkey (open source) instead of Redis (source available),
    # uncomment the Valkey statement and comment out the Redis statement.
    # Using Valkey with Firecrawl is untested and not guaranteed to work. Use with caution.
    image: redis:alpine
    # image: valkey/valkey:alpine

    networks:
      - backend
    command: redis-server --bind 0.0.0.0
    logging:
      driver: "json-file"
      options:
        max-size: "5m"
        max-file: "2"
        compress: "true"
    
  rabbitmq:
    image: rabbitmq:3-management
    networks:
      - backend
    command: rabbitmq-server
    healthcheck:
      test: ["CMD", "rabbitmq-diagnostics", "-q", "check_running"]
      interval: 5s
      timeout: 5s
      retries: 3
      start_period: 5s
    logging:
      driver: "json-file"
      options:
        max-size: "5m"
        max-file: "2"
        compress: "true"
  
  nuq-postgres:
    # NOTE: If you don't want to build the image locally,
    # comment out the build: statement and uncomment the image: statement
    # image: ghcr.io/firecrawl/nuq-postgres:latest
    build: apps/nuq-postgres
    environment:
      POSTGRES_USER: ${POSTGRES_USER:-postgres}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-postgres}
      POSTGRES_DB: ${POSTGRES_DB:-postgres}
    networks:
      - backend
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
        compress: "true"

networks:
  backend:
    driver: bridge

```

### File: docker_compose.yaml
```yaml
name: firecrawl

x-common-service: &common-service
  # NOTE: If you don't want to build the service locally,
  # comment out the build: statement and uncomment the image: statement
  # image: ghcr.io/firecrawl/firecrawl
  build: apps/api

  ulimits:
    nofile:
      soft: 65535
      hard: 65535
  networks:
    - backend
  extra_hosts:
    - "host.docker.internal:host-gateway"
  logging:
    driver: "json-file"
    options:
      max-size: "10m"
      max-file: "3"
      compress: "true"

x-common-env: &common-env
  REDIS_URL: ${REDIS_URL:-redis://redis:6379}
  REDIS_RATE_LIMIT_URL: ${REDIS_URL:-redis://redis:6379}
  PLAYWRIGHT_MICROSERVICE_URL: ${PLAYWRIGHT_MICROSERVICE_URL:-http://playwright-service:3000/scrape}
  POSTGRES_USER: ${POSTGRES_USER:-postgres}
  POSTGRES_PASSWORD='[REDACTED_PASSWORD]'
  POSTGRES_DB: ${POSTGRES_DB:-postgres}
  POSTGRES_HOST: ${POSTGRES_HOST:-nuq-postgres}
  POSTGRES_PORT: ${POSTGRES_PORT:-5432}
  USE_DB_AUTHENTICATION: ${USE_DB_AUTHENTICATION:-false}
  NUM_WORKERS_PER_QUEUE: ${NUM_WORKERS_PER_QUEUE:-8}
  CRAWL_CONCURRENT_REQUESTS: ${CRAWL_CONCURRENT_REQUESTS:-10}
  MAX_CONCURRENT_JOBS: ${MAX_CONCURRENT_JOBS:-5}
  BROWSER_POOL_SIZE: ${BROWSER_POOL_SIZE:-5}
  OPENAI_API_KEY: ${OPENAI_API_KEY}
  OPENAI_BASE_URL: ${OPENAI_BASE_URL}
  MODEL_NAME: ${MODEL_NAME}
  MODEL_EMBEDDING_NAME: ${MODEL_EMBEDDING_NAME} 
  OLLAMA_BASE_URL: ${OLLAMA_BASE_URL} 
  AUTUMN_SECRET_KEY: ${AUTUMN_SECRET_KEY}
  SLACK_WEBHOOK_URL: ${SLACK_WEBHOOK_URL}
  BULL_AUTH_KEY: ${BULL_AUTH_KEY}
  TEST_API_KEY: ${TEST_API_KEY}
  SUPABASE_ANON_TOKEN: ${SUPABASE_ANON_TOKEN}
  SUPABASE_URL: ${SUPABASE_URL}
  SUPABASE_SERVICE_TOKEN: ${SUPABASE_SERVICE_TOKEN}
  SELF_HOSTED_WEBHOOK_URL: ${SELF_HOSTED_WEBHOOK_URL}
  LOGGING_LEVEL: ${LOGGING_LEVEL}
  PROXY_SERVER: ${PROXY_SERVER}
  PROXY_USERNAME: ${PROXY_USERNAME}
  PROXY_PASSWORD: ${PROXY_PASSWORD}
  SEARXNG_ENDPOINT: ${SEARXNG_ENDPOINT}
  SEARXNG_ENGINES: ${SEARXNG_ENGINES}
  SEARXNG_CATEGORIES: ${SEARXNG_CATEGORIES}

services:
  playwright-service:
    # NOTE: If you don't want to build the service locally,
    # comment out the build: statement and uncomment the image: statement
    # image: ghcr.io/firecrawl/playwright-service:latest
    build: apps/playwright-service-ts
    environment:
      PORT: 3000
      PROXY_SERVER: ${PROXY_SERVER}
      PROXY_USERNAME: ${PROXY_USERNAME}
      PROXY_PASSWORD: ${PROXY_PASSWORD}
      ALLOW_LOCAL_WEBHOOKS: ${ALLOW_LOCAL_WEBHOOKS}
      BLOCK_MEDIA: ${BLOCK_MEDIA}
      # Configure maximum concurrent pages for Playwright browser instances
      MAX_CONCURRENT_PAGES: ${CRAWL_CONCURRENT_REQUESTS:-10}
    networks:
      - backend
    # Resource limits for Docker Compose (not Swarm)
    cpus: 2.0
    mem_limit: 4G
    memswap_limit: 4G
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
        compress: "true"
    tmpfs:
      - /tmp/.cache:noexec,nosuid,size=1g

  api:
    <<: *common-service
    environment:
      <<: *common-env
      HOST: "0.0.0.0"
      PORT: ${INTERNAL_PORT:-3002}
      EXTRACT_WORKER_PORT: ${EXTRACT_WORKER_PORT:-3004}
      WORKER_PORT: ${WORKER_PORT:-3005}
      NUQ_RABBITMQ_URL: amqp://rabbitmq:5672
      ENV: local
    depends_on:
      redis:
        condition: service_started
      playwright-service:
        condition: service_started
      rabbitmq:
        condition: service_healthy
    ports:
      - "${PORT:-3002}:${INTERNAL_PORT:-3002}"
    command: node dist/src/harness.js --start-docker
    # Resource limits for Docker Compose (not Swarm)
    # Increase if you have more CPU cores/RAM available
    cpus: 4.0
    mem_limit: 8G
    memswap_limit: 8G

  redis:
    # NOTE: If you want to use Valkey (open source) instead of Redis (source available),
    # uncomment the Valkey statement and comment out the Redis statement.
    # Using Valkey with Firecrawl is untested and not guaranteed to work. Use with caution.
    image: redis:alpine
    # image: valkey/valkey:alpine

    networks:
      - backend
    command: redis-server --bind 0.0.0.0
    logging:
      driver: "json-file"
      options:
        max-size: "5m"
        max-file: "2"
        compress: "true"
    
  rabbitmq:
    image: rabbitmq:3-management
    networks:
      - backend
    command: rabbitmq-server
    healthcheck:
      test: ["CMD", "rabbitmq-diagnostics", "-q", "check_running"]
      interval: 5s
      timeout: 5s
      retries: 3
      start_period: 5s
    logging:
      driver: "json-file"
      options:
        max-size: "5m"
        max-file: "2"
        compress: "true"
  
  nuq-postgres:
    build: apps/nuq-postgres
    environment:
      POSTGRES_USER: ${POSTGRES_USER:-postgres}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-postgres}
      POSTGRES_DB: ${POSTGRES_DB:-postgres}
    networks:
      - backend
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
        compress: "true"

networks:
  backend:
    driver: bridge

```

### File: SELF_HOST.md
```md
# Self-hosting Firecrawl

#### Contributor?

Welcome to [Firecrawl](https://firecrawl.dev) 🔥! Here are some instructions on how to get the project locally so you can run it on your own and contribute.

If you're contributing, note that the process is similar to other open-source repos, i.e., fork Firecrawl, make changes, run tests, PR.

If you have any questions or would like help getting on board, join our Discord community [here](https://discord.gg/firecrawl) for more information or submit an issue on Github [here](https://github.com/firecrawl/firecrawl/issues/new/choose)!

## Why?

Self-hosting Firecrawl is particularly beneficial for organizations with stringent security policies that require data to remain within controlled environments. Here are some key reasons to consider self-hosting:

- **Enhanced Security and Compliance:** By self-hosting, you ensure that all data handling and processing complies with internal and external regulations, keeping sensitive information within your secure infrastructure. Note that Firecrawl is a Mendable product and relies on SOC2 Type2 certification, which means that the platform adheres to high industry standards for managing data security.
- **Customizable Services:** Self-hosting allows you to tailor the services, such as the Playwright service, to meet specific needs or handle particular use cases that may not be supported by the standard cloud offering.
- **Learning and Community Contribution:** By setting up and maintaining your own instance, you gain a deeper understanding of how Firecrawl works, which can also lead to more meaningful contributions to the project.

### Considerations

However, there are some limitations and additional responsibilities to be aware of:

1. **Limited Access to Fire-engine:** Currently, self-hosted instances of Firecrawl do not have access to Fire-engine, which includes advanced features for handling IP blocks, robot detection mechanisms, and more. This means that while you can manage basic scraping tasks, more complex scenarios might require additional configuration or might not be supported.
2. **Manual Configuration Required:** If you need to use scraping methods beyond the basic fetch and Playwright options, you will need to manually configure these in the `.env` file. This requires a deeper understanding of the technologies and might involve more setup time.

Self-hosting Firecrawl is ideal for those who need full control over their scraping and data processing environments but comes with the trade-off of additional maintenance and configuration efforts.

## Steps

1. First, start by installing the dependencies

- Docker [instructions](https://docs.docker.com/get-docker/)


2. Set environment variables

Create an `.env` in the root directory using the template below.

`.env:`
```
# ===== Required ENVS ======
PORT=3002
HOST=0.0.0.0

# Note: PORT is used by both the main API server and worker liveness check endpoint

# To turn on DB authentication, you need to set up Supabase.
USE_DB_AUTHENTICATION=false

# ===== Optional ENVS ======

## === AI features (JSON format on scrape, /extract API) ===
# Provide your OpenAI API key here to enable AI features
# OPENAI_API_KEY=

# Experimental: Use Ollama
# OLLAMA_BASE_URL=http://localhost:11434/api
# MODEL_NAME=deepseek-r1:7b
# MODEL_EMBEDDING_NAME=nomic-embed-text

# Experimental: Use any OpenAI-compatible API
# OPENAI_BASE_URL=https://example.com/v1
# OPENAI_API_KEY=

## === Proxy ===
# PROXY_SERVER can be a full URL (e.g. http://0.1.2.3:1234) or just an IP and port combo (e.g. 0.1.2.3:1234)
# Do not uncomment PROXY_USERNAME and PROXY_PASSWORD if your proxy is unauthenticated
# PROXY_SERVER=
# PROXY_USERNAME=
# PROXY_PASSWORD=

## === /search API ===
# By default, the /search API will use Google search.

# You can specify a SearXNG server with the JSON format enabled, if you'd like to use that instead of direct Google.
# You can also customize the engines and categories parameters, but the defaults should also work just fine.
# SEARXNG_ENDPOINT=http://your.searxng.server
# SEARXNG_ENGINES=
# SEARXNG_CATEGORIES=

## === Other ===

# Supabase Setup (used to support DB authentication, advanced logging, etc.)
# SUPABASE_ANON_TOKEN=
# SUPABASE_URL=
# SUPABASE_SERVICE_TOKEN=

# Use if you've set up authentication and want to test with a real API key
# TEST_API_KEY=

# This key lets you access the queue admin panel. Change this if your deployment is publicly accessible.
BULL_AUTH_KEY=CHANGEME

# This is now autoconfigured by the docker-compose.yaml. You shouldn't need to set it.
# PLAYWRIGHT_MICROSERVICE_URL=http://playwright-service:3000/scrape
# REDIS_URL=redis://redis:6379
# REDIS_RATE_LIMIT_URL=redis://redis:6379

## === PostgreSQL Database Configuration ===
# Configure PostgreSQL credentials. These should match the credentials used by the nuq-postgres container.
# If you change these, ensure all three are set consistently.
# POSTGRES_USER=firecrawl
# POSTGRES_PASSWORD=firecrawl_password
# POSTGRES_DB=firecrawl

# Set if you have a llamaparse key you'd like to use to parse pdfs
# LLAMAPARSE_API_KEY=

# Set if you'd like to send server health status messages to Slack
# SLACK_WEBHOOK_URL=

## === System Resource Configuration ===
# Maximum CPU usage threshold (0.0-1.0). Worker will reject new jobs when CPU usage exceeds this value.
# Default: 0.8 (80%)
# MAX_CPU=0.8

# Maximum RAM usage threshold (0.0-1.0). Worker will reject new jobs when memory usage exceeds this value.
# Default: 0.8 (80%)
# MAX_RAM=0.8

# Set if you'd like to allow local webhooks to be sent to your self-hosted instance
# ALLOW_LOCAL_WEBHOOKS=true
```

### Security considerations

- **Use strong PostgreSQL credentials.** The defaults in the `.env` template are for local development only. When deploying to a server, set `POSTGRES_USER`, `POSTGRES_PASSWORD`, and `POSTGRES_DB` to secure values and ensure they match the database service configuration.
- **Keep the database port internal.** The provided `docker-compose.yaml` does not expose PostgreSQL to the host or the internet. Avoid adding a `ports` mapping for `nuq-postgres` unless you are restricting access with a firewall. To access the database for maintenance, prefer using `docker compose exec nuq-postgres psql` or a temporary, firewalled tunnel.
- **Protect the admin UI.** Set `BULL_AUTH_KEY` to a strong secret, especially on any deployment reachable from untrusted networks.

3.  Build and run the Docker containers:

    ```bash
    docker compose build
    docker compose up
    ```

    If you encounter an error, make sure you're using `docker compose` and not `docker-compose`.
    
    This will run a local instance of Firecrawl which can be accessed at `http://localhost:3002`.
    
    You should be able to see the Bull Queue Manager UI on `http://localhost:3002/admin/CHANGEME/queues`.

5. *(Optional)* Test the API

If you’d like to test the crawl endpoint, you can run this:

  ```bash
  curl -X POST http://localhost:3002/v1/crawl \
      -H 'Content-Type: application/json' \
      -d '{
        "url": "https://firecrawl.dev"
      }'
  ```   

## Troubleshooting

This section provides solutions to common issues you might encounter while setting up or running your self-hosted instance of Firecrawl.

### API Keys for SDK Usage

**Note:** When using Firecrawl SDKs with a self-hosted instance, API keys are optional. API keys are only required when connecting to the cloud service (api.firecrawl.dev).

### Supabase client is not configured

**Symptom:**
```bash
[YYYY-MM-DDTHH:MM:SS.SSSz]ERROR - Attempted to access Supabase client when it's not configured.
[YYYY-MM-DDTHH:MM:SS.SSSz]ERROR - Error inserting scrape event: Error: Supabase client is not configured.
```

**Explanation:**
This error occurs because the Supabase client setup is not completed. You should be able to scrape and crawl with no problems. Right now it's not possible to configure Supabase in self-hosted instances.

### You're bypassing authentication

**Symptom:**
```bash
[YYYY-MM-DDTHH:MM:SS.SSSz]WARN - You're bypassing authentication
```

**Explanation:**
This error occurs because the Supabase client setup is not completed. You should be able to scrape and crawl with no problems. Right now it's not possible to configure Supabase in self-hosted instances.

### Docker containers fail to start

**Symptom:**
Docker containers exit unexpectedly or fail to start.

**Solution:**
Check the Docker logs for any error messages using the command:
```bash
docker logs [container_name]
```

- Ensure all required environment variables are set correctly in the .env file.
- Verify that all Docker services defined in docker-compose.yml are correctly configured and the necessary images are available.

### Connection issues with Redis

**Symptom:**
Errors related to connecting to Redis, such as timeouts or "Connection refused".

**Solution:**
- Ensure that the Redis service is up and running in your Docker environment.
- Verify that the REDIS_URL and REDIS_RATE_LIMIT_URL in your .env file point to the correct Redis instance, ensure that it points to the same URL in the `docker-compose.yaml` file (`redis://redis:6379`)
- Check network settings and firewall rules that may block the connection to the Redis port.

### API endpoint does not respond

**Symptom:**
API requests to the Firecrawl instance timeout or return no response.

**Solution:**
- Ensure that the Firecrawl service is running by checking the Docker container status.
- Verify that the PORT and HOST settings in your .env file are correct and that no other service is using the same port.
- Check the network configuration to ensure that the host is accessible from the client making the API request.

By addressing these common issues, you can ensure a smoother setup and operation of your self-hosted Firecrawl instance.

## Install Firecrawl on a Kubernetes Cluster (Simple Version)

Read the [examples/kubernetes/cluster-install/README.md](https://github.com/firecrawl/firecrawl/blob/main/examples/kubernetes/cluster-install/README.md) for instructions on how to install Firecrawl on a Kubernetes Cluster.

## Install Firecrawl on a Kubernetes Cluster with Helm

Read the [examples/kubernetes/firecrawl-helm/README.md](https://github.com/firecrawl/firecrawl/blob/main/examples/kubernetes/firecrawl-helm/README.md) for instructions on how to install Firecrawl on a Kubernetes Cluster with Helm.

```

### File: examples\attributes-extraction-js-sdk.js
```js
/**
 * Example: Using Firecrawl JS SDK v2 to extract attributes from HTML elements
 */

import FirecrawlApp from '@mendable/firecrawl-js';

const app = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

async function main() {
  console.log('🎯 Extracting attributes from Hacker News...');

  try {
    // Extract story IDs from Hacker News
    const result = await app.scrapeUrl('https://news.ycombinator.com', {
      formats: [
        { type: 'markdown' },
        {
          type: 'attributes',
          selectors: [
            { selector: '.athing', attribute: 'id' }
          ]
        }
      ]
    });

    console.log('✅ Success! Extracted data:');
    console.log('Story IDs:', result.data.attributes[0].values.slice(0, 5));
    console.log('Total stories found:', result.data.attributes[0].values.length);

    // Example with GitHub - multiple attributes
    console.log('\n🎯 Extracting multiple attributes from GitHub...');

    const githubResult = await app.scrapeUrl('https://github.com/microsoft/vscode', {
      formats: [
        {
          type: 'attributes',
          selectors: [
            { selector: '[data-testid]', attribute: 'data-testid' },
            { selector: '[data-view-component]', attribute: 'data-view-component' }
          ]
        }
      ]
    });

    console.log('✅ GitHub extraction success!');
    console.log('Test IDs found:', githubResult.data.attributes[0].values.length);
    console.log('Components found:', githubResult.data.attributes[1].values.length);

  } catch (error) {
    console.error('❌ Error:', error.message);
  }
}

main();
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
