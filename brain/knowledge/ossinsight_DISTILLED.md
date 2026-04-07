---
id: ossinsight
type: knowledge
owner: OA_Triage
---
# ossinsight
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "ossinsight-monorepo",
  "private": true,
  "scripts": {
    "build": "turbo run build",
    "dev": "pnpm --filter web dev",
    "dev:web": "pnpm --filter web dev",
    "dev:all": "turbo run dev --filter=web --filter=docs",
    "dev:docs": "turbo run dev --filter=docs",
    "start": "pnpm --filter web start",
    "start:web": "pnpm --filter web start",
    "start:all": "turbo run start --filter=web --filter=docs",
    "start:docs": "turbo run start --filter=docs",
    "lint": "turbo run lint",
    "check-types": "turbo run check-types"
  },
  "devDependencies": {
    "turbo": "^2.7.1",
    "typescript": "^5.2.2"
  },
  "packageManager": "pnpm@10.29.3",
  "engines": {
    "node": ">=20.9.0"
  },
  "pnpm": {
    "overrides": {
      "@tanstack/react-query": "^5.90.21"
    }
  }
}

```

### File: README.md
```md
<h1 align="center">OSSInsight</h1>

<p align="center">
  <b>The analytics engine for the AI-native open source ecosystem.</b><br/>
  Analyze 10+ billion GitHub events. Track AI agents, coding tools, and the repos shaping the future.
</p>

<div align="center">
<a href="https://ossinsight.io">
  <img src="https://raw.githubusercontent.com/pingcap/ossinsight/main/apps/docs/public/img/screenshots/homepage.gif"
</a>
</div>

<h4 align="center">
  <b><a href="https://ossinsight.io/explore/">Data Explorer</a></b>
  •
  <b><a href="https://ossinsight.io/collections/ai-agent-frameworks">AI Agent Rankings</a></b>
  •
  <b><a href="https://ossinsight.io/trending">Trending</a></b>
  •
  <a href="https://ossinsight.io/analyze/karpathy/autoresearch">Repo Analytics</a>
  •
  <a href="https://ossinsight.io/analyze-user/torvalds">Developer Analytics</a>
  •
  <a href="https://ossinsight.io/collections/open-source-database">Collections</a>
  •
  <a href="https://ossinsight.io/blog">Blog</a>
  •
  <a href="https://twitter.com/OSSInsight">Twitter</a>
</h4>

## What is OSSInsight?

OSSInsight analyzes **10+ billion rows of GitHub event data** to surface insights about the open source ecosystem — from individual developers to entire technical fields.

In 2026, that means tracking the explosion of **AI agents, coding assistants, research automation, and the infrastructure being built around them**. OSSInsight is how you see what's actually happening in open source, measured in commits, stars, forks, and contributors — not hype.

### For AI builders

- **[AI Agent Frameworks](https://ossinsight.io/collections/ai-agent-frameworks)** — Rankings and trends across LangChain, CrewAI, AutoGen, and 50+ agent frameworks
- **[Coding Agents](https://ossinsight.io/collections/ai-coding-assistant)** — Track Claude Code, Copilot, Cursor, Aider, and the autonomous coding wave
- **[Research Agents](https://ossinsight.io/analyze/karpathy/autoresearch)** — Analyze repos like autoresearch (54K stars in 19 days) that are turning research into search
- **[MCP & Tool Infrastructure](https://ossinsight.io/collections/model-context-protocol)** — The standardizing integration layer for AI agents

### For developers

- **[Developer Analytics](https://ossinsight.io/analyze-user/torvalds)** — Contribution patterns, code review cadence, collaboration networks
- **[Repository Analytics](https://ossinsight.io/analyze/pingcap/tidb)** — Stars, forks, contributor growth, geographic distribution, company breakdown
- **[Compare Projects](https://ossinsight.io/analyze/pytorch/pytorch?vs=tensorflow/tensorflow)** — Side-by-side comparison on any metric
- **[Trending](https://ossinsight.io/trending)** — What's gaining velocity right now

### For researchers & analysts

- **[Data Explorer](https://ossinsight.io/explore/)** — Ask questions about GitHub data in natural language, get SQL + visualizations
- **[60+ Curated Collections](https://ossinsight.io/collections/open-source-database)** — From databases to Web3, from DevOps to AI safety
- **[Blog](https://ossinsight.io/blog)** — Data-driven analysis of open source trends

## LLM-Friendly

OSSInsight is built for the AI era:

- **[`/llms.txt`](https://ossinsight.io/llms.txt)** — Structured site description for LLMs
- **[`/llms-full.txt`](https://ossinsight.io/llms-full.txt)** — Full documentation in LLM-friendly format
- **[OpenSearch](https://ossinsight.io/opensearch.xml)** — Machine-readable search integration
- **Schema.org structured data** on every page — TechArticle, CollectionPage, BreadcrumbList, FAQPage, and more

## Featured Analysis

| Topic | What we found |
|-------|--------------|
| [autoresearch: 54K Stars in 19 Days](https://ossinsight.io/blog/autoresearch-overnight-ai-scientist) | Research is becoming search. karpathy/autoresearch has a 1,085:1 fork-to-contributor ratio — people fork to run private experiments, not to contribute back. |
| [The Coding Agent Wars](https://ossinsight.io/blog/coding-agent-wars-2026) | Claude Code, Codex, OpenCode — the autonomous coding landscape mapped by the data. |
| [Agent Skills: Not the Endgame](https://ossinsight.io/blog/agent-skills-not-endgame) | 57K AGENTS.md repos, 21K CLAUDE.md — skills are a transitional layer, not the final form. |

## Features

### **Data Explorer**
  
Ask questions about GitHub data in natural language — Data Explorer generates SQL, queries the data, and presents results visually.

Examples:
* [Projects similar to @facebook/react](https://ossinsight.io/explore?id=ba186a53-b2ab-4cad-a46f-e2c36566cacd)
* [Where are @kubernetes/kubernetes contributors from?](https://ossinsight.io/explore?id=754a681e-913f-4333-b55d-dbd8598bd84d)
* [More popular questions](https://ossinsight.io/explore/)

### **Collections & Rankings**

Find insights about monthly or historical rankings and trends in technical fields with curated repository lists.

<div align="center">
    <img src="https://raw.githubusercontent.com/pingcap/ossinsight/main/apps/docs/public/img/screenshots/homepage-collection.png" alt="GitHub Collections Analytics" height="500" />
</div>

**Examples**:
* [Collection: AI Agent Frameworks](https://ossinsight.io/collections/ai-agent-frameworks)
* [Collection: Open Source Database](https://ossinsight.io/collections/open-source-database)
* [Collection: Web Framework](https://ossinsight.io/collections/web-framework)
* [More](https://ossinsight.io/collections/open-source-database) ...

### **Developer Analytics**

Insights about **developer productivity**, **work cadence**, and **collaboration** from contribution behavior.

* Contribution time distribution, stars, languages, and trends
* Code (commits, pull requests, code line changes), code reviews, and issues

<div align="center">
    <img src="https://raw.githubusercontent.com/pingcap/ossinsight/main/apps/docs/public/img/screenshots/homepage-developer.png" alt="Developer Analytics" height="500" />
</div>

### **Repository Analytics**

Insights about **code update frequency & popularity** from repository status.

* Stars, forks, issues, commits, pull requests, contributors, languages, and lines of code
* Geographical and company distribution of stargazers, issue creators, and PR creators

<div align="center">
    <img src="https://raw.githubusercontent.com/pingcap/ossinsight/main/apps/docs/public/img/screenshots/homepage-repository.png" alt="Repository Analytics" height="500" />
</div>

**Examples**:
* [React](https://ossinsight.io/analyze/facebook/react)
* [TiDB](https://ossinsight.io/analyze/pingcap/tidb)
* [PyTorch](https://ossinsight.io/analyze/pytorch/pytorch)

### **Compare Projects**

Compare two projects side-by-side on any metric.

**Examples**:
* [Compare Vue and React](https://ossinsight.io/analyze/vuejs/vue?vs=facebook/react)
* [Compare PyTorch and TensorFlow](https://ossinsight.io/analyze/pytorch/pytorch?vs=tensorflow/tensorflow)

## Collections

Curated lists of repos in technical fields, ranked by GitHub metrics. Perfect for tracking ecosystems.

**Add a collection** by submitting a PR to [`etl/meta/collections/`](https://github.com/pingcap/ossinsight/tree/main/etl/meta/collections):

```yml
id: <collection_id>
name: <collection_name>
items:
  - owner/repo-1
  - owner/repo-2
```

**Popular collections:**
[AI Agent Frameworks](https://ossinsight.io/collections/ai-agent-frameworks) •
[Open Source Database](https://ossinsight.io/collections/open-source-database) •
[Web Framework](https://ossinsight.io/collections/web-framework) •
[JavaScript ORM](https://ossinsight.io/collections/javascript-orm) •
[More...](https://ossinsight.io/collections/open-source-database)

## Development

```bash
pnpm install
pnpm dev        # Start web app (port 3001)
pnpm dev:docs   # Start docs site (port 3002)
pnpm dev:all    # Start both
```

## Contributing

- [GitHub Discussions](https://github.com/pingcap/ossinsight/discussions) — Questions, ideas, best practices
- [GitHub Issues](https://github.com/pingcap/ossinsight/issues) — Bugs, features, collection suggestions
- [GitHub PRs](https://github.com/pingcap/ossinsight/pulls) — Code, fixes, blog posts, new collections

## Contact

- [@OSSInsight](https://twitter.com/OSSInsight) on Twitter
- [GitHub Discussions](https://github.com/pingcap/ossinsight/discussions)
- [ossinsight@pingcap.com](mailto:ossinsight@pingcap.com)

<div align="center">
  <sub>Powered by</sub><br/>
  <a href="https://en.pingcap.com/tidb-cloud/?utm_source=ossinsight&utm_medium=referral">
    <img src="https://raw.githubusercontent.com/pingcap/ossinsight/main/apps/docs/public/img/tidb-cloud-logo-w.png" height=50 />
  </a>
</div>

```

### File: apps\docs\package.json
```json
{
  "name": "docs",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "sh -c 'PORT=\"${PORT:-3002}\"; rm -rf .next/dev; exec next dev -p \"$PORT\"'",
    "build": "next build",
    "start": "sh -c 'PORT=\"${PORT:-3002}\"; exec next start -p \"$PORT\"'",
    "lint": "next lint",
    "check-types": "tsc --noEmit"
  },
  "dependencies": {
    "@radix-ui/react-menubar": "^1.1.6",
    "@repo/site-shell": "workspace:*",
    "@tanstack/react-query": "^5.80.7",
    "clsx": "^2.0.0",
    "fumadocs-core": "^16.6.16",
    "fumadocs-mdx": "^14.2.9",
    "fumadocs-ui": "^16.6.16",
    "gray-matter": "^4.0.3",
    "lucide-react": "^0.577.0",
    "next": "16.1.6",
    "next-themes": "^0.4.6",
    "react": "^19.2.0",
    "react-dom": "^19.2.0",
    "react-markdown": "^10.1.0",
    "reading-time": "^1.5.0",
    "rehype-autolink-headings": "^7.1.0",
    "rehype-pretty-code": "^0.14.3",
    "rehype-raw": "^7.0.0",
    "rehype-slug": "^6.0.0",
    "remark-gfm": "^4.0.1",
    "shiki": "^4.0.2",
    "tailwindcss": "^4.2.1",
    "yaml": "^2.8.1"
  },
  "devDependencies": {
    "@repo/typescript-config": "workspace:*",
    "@tailwindcss/postcss": "^4.2.1",
    "@types/mdx": "^2.0.7",
    "@types/node": "20.4.2",
    "@types/react": "^19.2.2",
    "@types/react-dom": "^19.2.2",
    "autoprefixer": "10.4.14",
    "eslint": "^9.0.0",
    "eslint-config-next": "16.1.6",
    "postcss": "8.4.26",
    "typescript": "^5.2.2"
  }
}

```

### File: apps\web\package.json
```json
{
  "name": "web",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "sh -c 'PORT=\"${PORT:-3001}\"; exec next dev --webpack -p \"$PORT\"'",
    "build": "next build",
    "start": "sh -c 'PORT=\"${PORT:-3001}\"; exec next start -p \"$PORT\"'",
    "lint": "next lint",
    "check-types": "tsc --noEmit"
  },
  "dependencies": {
    "@ai-sdk/openai": "^3.0.41",
    "@ai-sdk/react": "^3.0.118",
    "@geo-maps/countries-land-10km": "^0.6.0",
    "@mdx-js/loader": "^2.3.0",
    "@mdx-js/react": "^2.3.0",
    "@napi-rs/canvas": "^0.1.44",
    "@next/mdx": "16.1.6",
    "@primer/octicons-react": "^19.7.0",
    "@radix-ui/react-avatar": "^1.1.11",
    "@radix-ui/react-dialog": "^1.1.15",
    "@radix-ui/react-menubar": "^1.1.16",
    "@radix-ui/react-popover": "^1.1.15",
    "@radix-ui/react-select": "^2.2.6",
    "@radix-ui/react-switch": "^1.2.6",
    "@radix-ui/react-tabs": "^1.1.13",
    "@radix-ui/react-tooltip": "^1.2.8",
    "@radix-ui/react-use-controllable-state": "^1.2.2",
    "@repo/site-shell": "workspace:*",
    "@rive-app/react-webgl2": "^4.27.1",
    "@streamdown/cjk": "^1.0.2",
    "@streamdown/code": "^1.1.0",
    "@streamdown/math": "^1.0.2",
    "@streamdown/mermaid": "^1.0.2",
    "@tanstack/react-query": "^5.90.21",
    "@tidbcloud/serverless": "^0.0.6",
    "@upstash/ratelimit": "^2.0.8",
    "@upstash/redis": "^1.37.0",
    "@vercel/related-projects": "^1.0.1",
    "@xyflow/react": "^12.10.1",
    "ai": "^6.0.116",
    "ansi-to-react": "^6.2.6",
    "autoprefixer": "10.4.14",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.0.0",
    "cmdk": "^1.1.1",
    "d3-cloud": "^1.2.9",
    "d3-hierarchy": "^3.1.2",
    "deepmerge": "^4.3.1",
    "echarts": "^5.4.3",
    "echarts-for-react": "^3.0.6",
    "embla-carousel-react": "^8.6.0",
    "human-format": "^1.2.0",
    "jsonpath": "^1.1.1",
    "liquidjs": "^10.9.2",
    "lodash": "^4.17.21",
    "lucide-react": "^0.577.0",
    "luxon": "^3.4.3",
    "media-chrome": "^4.18.0",
    "merge-refs": "^1.2.1",
    "motion": "^12.35.2",
    "nanoid": "^5.1.6",
    "next": "16.1.6",
    "next-plugin-svgr": "^1.1.8",
    "postcss": "8.4.26",
    "pretty-ms": "^8.0.0",
    "radix-ui": "^1.4.3",
    "react": "18.2.0",
    "react-dom": "18.2.0",
    "react-jsx-parser": "^2.4.1",
    "react-transition-state": "^2.1.1",
    "react-window": "^1.8.9",
    "rehype-react": "^7.2.0",
    "remark-parse": "^10.0.2",
    "remark-rehype": "^10.1.0",
    "shadcn": "^4.0.5",
    "shiki": "^4.0.2",
    "streamdown": "^2.4.0",
    "tailwindcss": "3.3.3",
    "tokenlens": "^1.3.1",
    "tw-animate-css": "^1.4.0",
    "unified": "^10.1.2",
    "url-template": "^3.1.0",
    "use-stick-to-bottom": "^1.1.3",
    "zod": "^4.3.6"
  },
  "devDependencies": {
    "@repo/typescript-config": "workspace:*",
    "@svgr/webpack": "^8.1.0",
    "@tailwindcss/typography": "^0.5.10",
    "@types/lodash": "^4.14.199",
    "@types/luxon": "^3.3.2",
    "@types/mdast": "^4.0.0",
    "@types/mdx": "^2.0.7",
    "@types/node": "20.4.2",
    "@types/react": "18.2.15",
    "@types/react-dom": "18.2.7",
    "@types/react-window": "^1.8.5",
    "bootstrap-icons": "^1.11.1",
    "eslint": "^9.0.0",
    "eslint-config-next": "16.1.6",
    "playwright": "^1.58.2",
    "raw-loader": "^4.0.2",
    "tailwind-merge": "^1.14.0",
    "typescript": "^5.2.2"
  }
}

```

### File: packages\pipeline\package.json
```json
{
  "name": "@ossinsight/pipeline",
  "version": "0.0.1",
  "description": "The data pipelines for OSSInsight",
  "license": "Apache-2.0",
  "author": "Mini256",
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "directories": {
    "test": "__tests__"
  },
  "scripts": {
    "build": "tsc",
    "build:watch": "tsc -w",
    "dev": "NODE_ENV=development fastify start -p ${PIPELINE_SERVER_PORT:-30003} -P --ignore-watch=.ts$ -L dist/logger.js -l info -w dist/app.js",
    "start": "fastify start -a 0.0.0.0 -p ${PIPELINE_SERVER_PORT:-30003} -L dist/logger.js -l info dist/app.js"
  },
  "dependencies": {
    "@fastify/autoload": "^5.0.0",
    "@fastify/env": "^4.1.0",
    "@fastify/mysql": "^4.1.0",
    "@fastify/schedule": "^4.1.1",
    "croner": "^6.0.7",
    "fastify": "^4.0.0",
    "fastify-cli": "^5.5.1",
    "fastify-metrics": "^10.0.0",
    "fastify-plugin": "^4.3.0",
    "luxon": "^3.3.0",
    "mysql2": "^3.11.5",
    "node-schedule": "^2.1.1",
    "pino": "^8.7.0",
    "pino-pretty": "^9.1.1",
    "toad-scheduler": "^3.0.0"
  },
  "devDependencies": {
    "@fastify/type-provider-json-schema-to-ts": "^2.1.1",
    "@types/luxon": "^3.3.1",
    "@types/node": "^18.0.0",
    "@types/node-schedule": "^2.1.0",
    "fastify-tsconfig": "^1.0.1",
    "typescript": "^4.5.4"
  }
}

```

### File: packages\pipeline\README.md
```md
# OSSInsight Pipeline




```

### File: packages\types\package.json
```json
{
  "name": "@ossinsight/types",
  "version": "1.0.0",
  "description": "The type definitions for OSS Insight",
  "license": "Apache-2.0",
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "directories": {
    "test": "__tests__"
  },
  "scripts": {
    "gen:d.ts": "json2ts ./schema/query.schema.json ./src/query.schema.d.ts",
    "validate:query": "ajv -s ./schema/query.schema.json -r ./schema/openapi-2021-09-28.schema.json -c ajv-formats -d \"../../configs/queries/*/params.json\"",
    "build": "tsc"
  },
  "dependencies": {

  },
  "devDependencies": {
    "@types/node": "^18.0.0",
    "ajv-cli": "^5.0.0",
    "ajv-formats": "^2.1.1",
    "fastify-tsconfig": "^1.0.1",
    "json-schema-to-ts": "^2.6.0",
    "json-schema-to-typescript": "^11.0.2",
    "typescript": "^4.5.4"
  }
}

```

### File: packages\types\README.md
```md
# Types of OSSInsight


```

### File: NOTE.md
```md
# Notes

## Current audit

- Main web routes currently smoke-test clean locally: `/`, `/explore`, `/collections`, `/analyze/pingcap/ossinsight`, `/analyze/pingcap`, `/collections/api`, `/gh/repo/pingcap/ossinsight`, and `/api/q/events-total` all return `200`.
- Multi-repo compare mode still has a real runtime chart error. `http://127.0.0.1:3001/analyze/pingcap/ossinsight?vs=vercel/next.js` returns `200`, but the browser console still reports `Error: yAxis "vs" not found`, which means at least one compare chart is still misconfigured.
- Org analyze still has confirmed broken data dependencies. `http://127.0.0.1:3001/analyze/pingcap` returns `200`, but `/api/q/orgs/repos/active/ranking` and `/api/q/orgs/repos/active/total` both return `404`, and the page console still reports `TypeError: object is not iterable` from `apps/web/components/ui/components/GHRepoSelector/utils.ts` / `GHOrgRepoSelector.tsx`.
- `docs` and `API` pages had several `fumadocs` card surfaces that did not match the flatter content structure of `ossinsight.io`. These were reduced in the current pass, but the shared docs header and some generated widgets still need more source-level alignment.
- The docs app still depends on `fumadocs` interaction patterns for sidebar, tabs, and page chrome. That keeps behavior stable, but it is not a perfect structural match for the original Docusaurus-based site.
- Some migrated blog posts still degrade legacy interactive content to archive placeholders instead of restoring the original embedded experience. This is visible in `apps/docs/src/components/CommonChart.tsx` and `apps/docs/src/components/ContributorsCharts.tsx`.
- `Data Explorer` is visually much closer to the original homepage and result layout, but the backend still uses the newer one-turn flow. The original site exposed a more staged lifecycle while SQL was being generated.
- The current `Data Explorer` page still emits image warnings in dev for legacy preview assets. That is not user-visible breakage, but it is a cleanup item.
- The `Data Explorer` duplicate-key warning in the popular-question list has been fixed in the current pass, so it is no longer an outstanding runtime issue.
- The homepage hero currently renders `SELECT insights FROM 0 GitHub events` on first load in local runtime, even though the old site treated that total as a core live credibility signal. The data-refresh logic exists in `apps/web/app/home-content.tsx`, but the rendered value still does not reliably match the legacy experience.
- The docs/API header is still a custom Next implementation, not a direct structural port of the old site header. It now matches the site colors, but spacing, dropdown behavior, and active-state treatment still differ from the original implementation.
- The docs/API experience still shows two layers of chrome on API pages: the shared site header plus the internal `fumadocs` banner/search/sidebar shell. That is functional, but structurally further from the original OSS Insight site than a single integrated header would be.
- Blog article pages now have top-and-bottom share buttons again, matching the old site behavior more closely, but blog list/detail pages still do not fully recreate the old Docusaurus footer/paginator structure.
- API detail pages are functional, but they still lean heavily on `fumadocs` primitives such as `DynamicCodeBlock`, `Tabs`, `TypeTable`, and `DocsPage`. That keeps them usable, but the result is still visually more framework-shaped than the original OSS Insight API/docs pages.
- `next build` for `apps/web` still finishes with the long-standing `/collections` dynamic-usage notice around `searchParams`. It is not a user-facing outage, but it remains an architectural mismatch with a fully static-friendly setup.
- Homepage, Explore, collection detail, and collection trends pages currently run without browser-console errors in the sampled local pass. The remaining confirmed runtime breakages are concentrated in compare analyze, org analyze, and some migrated docs/blog embeds rather than the whole site shell.

## Old-site issues not worth copying 1:1

- The original docs/blog stack inherited a lot of default Docusaurus chrome. It was functional, but some screens felt more like framework defaults than OSS Insight-specific design.
- The old API docs leaned on generated documentation widgets heavily. They exposed the data well, but the visual density and method-color palette were not always consistent with the rest of the site.
- Several old blog/doc pages mixed content with embedded legacy widgets in ways that created uneven spacing and inconsistent visual weight.
- The old sidebar collapse affordance was easy to miss once layered under a custom site header. That behavior is not something to preserve.
- The original `Data Explorer` loading lifecycle had more visible intermediate steps, but it also made the interaction model more complex and brittle. Preserving the visual rhythm is useful; preserving the full old control flow is not automatically a quality win.
- The original blog/article chrome relied on framework-provided pagination and footer conventions that were familiar, but not especially distinctive. Reintroducing the useful navigation affordances makes sense; copying every piece of Docusaurus chrome does not.
- Some old embedded chart blocks inside blog posts were tightly coupled to legacy widget bundles and page runtime assumptions. Recreating the insight is useful; preserving those brittle embedding mechanics exactly is not.

## Follow-up replication targets

- Fix org analyze first: restore `/api/q/orgs/repos/active/ranking` and `/api/q/orgs/repos/active/total`, then resolve the `GHOrgRepoSelector` iterable error so the org page is functionally complete again.
- Fix the compare-page `yAxis "vs" not found` ECharts error before doing more cosmetic compare-page polish.
- Restore the homepage total-events hero count so it no longer idles at `0` during normal local runtime.
- Continue flattening docs/API detail screens so the page body reads like content first and framework shell second.
- Collapse the docs/API double-header setup into a single integrated chrome layer if the goal is closer source-level parity with `ossinsight.io`.
- Audit the shared docs header against the main web header at the spacing and hover-state level.
- Inspect generated tables, tabs, and API examples to decide which third-party styles should be overridden for closer OSS Insight parity.
- Decide whether the archived blog chart placeholders should be rebuilt with lightweight static chart renders or remain as explicit migration gaps.
- Review `Data Explorer` result-state details against the legacy execution flow, especially loading copy, share affordances, and SQL/result spacing.
- Audit analyze pages section-by-section against `ossinsight-next` for remaining spacing and typography drift after the major layout work.

```

### File: pnpm_workspace.yaml
```yaml
packages:
  - apps/*
  - packages/*

```

### File: turbo.json
```json
{
  "$schema": "https://turbo.build/schema.json",
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "inputs": ["$TURBO_DEFAULT$", ".env*"],
      "outputs": [".next/**", "!.next/cache/**"]
    },
    "dev": {
      "cache": false,
      "persistent": true
    },
    "lint": {
      "dependsOn": ["^lint"]
    },
    "check-types": {
      "dependsOn": ["^check-types"]
    },
    "start": {
      "cache": false,
      "persistent": true
    }
  }
}

```

### File: configs\allowed_origins.yaml
```yaml
private_origins:
  # Develop.
  - ^http://localhost:\d+$
  # Preview.
  - ^https://pingcap-ossinsight-preview-pr-.+\.surge\.sh$
  - ^https*://.+\.preview\.app\.github\.dev/*$
  # Production.
  - ^https://ossinsight\.io$
  - ^https://next\.ossinsight\.io$
  - ^https://live\.ossinsight\.io$
  # Next
  - ^https://ossinsight-next\.vercel\.app$
  - ^https://ossinsight-next-.+-pingcap\.vercel\.app$
  - ^https://ossinsight-next-ui\.vercel\.app$
public_origins:
  # External Users.
  - ^https://github1s\.com$
  - ^https://github\.com$

```

### File: configs\params_preset.json
```json
{
  "repo_subset": [
    "db_repos",
    "js_framework_repos",
    "nocode_repos",
    "programming_language_repos",
    "web_framework_repos"
  ],
  "years": ["1", "2", "5", "10"],
  "n": ["10", "20", "50"],
  "event": [
    "WatchEvent",
    "PullRequestEvent",
    "ForkEvent"
  ]
}
```

### File: memory\competitive_analysis_2026_03_20.md
```md
# OSSInsight 竞品差异化分析报告

## 执行摘要

**分析日期**: 2026-03-20  
**分析角度**: 竞品差异化 (Competitive Differentiation)  
**使用模型**: 千问 qwen3.5-plus

---

## 一、竞品地图

### 1.1 直接竞品（GitHub 数据分析）

| 竞品 | 核心功能 | 优势 | 劣势 |
|------|---------|------|------|
| **Star History** | Star 趋势可视化 | 简洁、专注、嵌入方便 | 单一维度，无深度分析 |
| **GitHub Trends** | 官方 Trending 页面 | 官方数据、权威性 | 无历史数据、无分析功能 |
| **LibHunt** | 开源项目发现与比较 | 分类完善、有社区评分 | 数据更新慢、无开发者分析 |
| **GitHut 2.0** | 编程语言流行度 | 独特的语言维度 | 仅语言层面，无 repo 分析 |
| **Open Source Insights** (deps.dev) | 依赖关系分析 | Google 背书、依赖图谱 | 侧重安全/依赖，非社区分析 |
| **RepoStats** 类工具 | 基础 repo 统计 | 轻量快速 | 功能单一、无 AI 能力 |

### 1.2 间接竞品（开发者工具/洞察）

| 竞品 | 定位 | 与 OSSInsight 的关系 |
|------|------|---------------------|
| **Sourcegraph** | 代码搜索与分析 | 代码层面 vs 社区层面 |
| **StackOverflow Trends** | 技术趋势 | 问答数据 vs 代码贡献数据 |
| **NPM Trends / PyPI Stats** | 包使用统计 | 单一生态 vs 跨生态 |
| **State of JS / State of Open Source** | 年度调研 | 调研数据 vs 实时行为数据 |

---

## 二、OSSInsight 核心优势

### 2.1 数据优势（护城河）

1. **10+ billion rows GitHub events** - 市场上最大的公开 GitHub 事件数据集
2. **历史数据完整** - 可追溯多年历史趋势
3. **实时性** - 数据持续更新
4. **跨维度关联** - repo、developer、organization、language、topic 多维关联

### 2.2 技术优势

1. **AI 驱动的 Data Explorer** - Chat2Query 自然语言查询
2. **TiDB Cloud 后端** - 处理大规模数据分析
3. **程序化分析页面** - 每个 repo/developer 自动生成深度报告

### 2.3 产品优势

1. **Collections** -  curated 技术分类（数据库、Web 框架、AI 等）
2. **Compare 功能** - repo vs repo 对比分析
3. **Developer Analytics** - 开发者生产力分析
4. **免费开放** - 无付费墙

---

## 三、竞品有而 OSSInsight 没有的功能

### 3.1 缺失功能清单

| 功能 | 竞品 | 重要性 | 实施难度 |
|------|------|--------|----------|
| **浏览器扩展** | Sourcegraph | 中 | 中等 |
| **CLI 工具** | 多个竞品 | 中 | 简单 |
| **API 开发者门户** | deps.dev | 高 | 中等 |
| **依赖关系图谱** | deps.dev | 中 | 复杂 |
| **安全漏洞集成** | deps.dev | 中 | 中等 |
| **技术雷达/象限图** | ThoughtWorks | 低 | 简单 |
| **Slack/Discord 集成** | 多个 SaaS | 中 | 简单 |
| **RSS 订阅** | 传统博客 | 低 | 简单 |
| **Webhook 通知** | GitHub Apps | 中 | 中等 |
| **导出为 PDF/图片** | Star History | 高 | 简单 |

### 3.2 高优先级缺失功能详解

#### 🔴 功能 1: 导出/分享增强
**现状**: 已有分享按钮，但缺少结构化导出  
**竞品做法**: Star History 可导出 PNG/SVG，State of JS 可下载报告  
**机会**: 
- 一键导出 repo 分析报告为 PDF
- 生成可嵌入的图片卡片（多尺寸）
- 导出原始数据为 CSV/JSON

#### 🔴 功能 2: API 开发者生态
**现状**: 有 API 文档，但开发者生态弱  
**竞品做法**: deps.dev 有完整 API 文档、SDK、示例  
**机会**:
- 创建官方 SDK（Python/JavaScript/Go）
- 增加 API 使用示例库
- 建立 API 使用案例展示
- 提供 API 沙箱环境

#### 🟡 功能 3: CLI 工具
**现状**: 无 CLI  
**竞品做法**: 多个开发者工具有 CLI  
**机会**:
```bash
$ ossinsight analyze pingcap/tidb
$ ossinsight compare vuejs/vue facebook/react
$ ossinsight trending --category database --period weekly
```

#### 🟡 功能 4: 依赖关系分析
**现状**: 无依赖分析  
**竞品做法**: deps.dev 专注依赖图谱和安全  
**机会**:
- 展示 repo 的依赖树
- 分析依赖健康度（活跃度、维护状态）
- 识别"危险依赖"（低活跃度、少维护者）

---

## 四、未被满足的用户需求

### 4.1 基于社区反馈的洞察

| 需求 | 用户群体 | 现有方案痛点 | OSSInsight 机会 |
|------|---------|-------------|----------------|
| **"这个技术还在活跃维护吗？"** | 技术选型者 | 需手动查看 commit 频率 | 提供"健康度评分" |
| **"哪个竞品更活跃？"** | 架构师 | 需打开多个页面比较 | 增强 compare 功能 |
| **"这个 repo 背后有哪些公司？"** | 开发者 | 需手动查看 contributor | 公司维度分析 |
| **"最近有什么新技术冒头？"** | 技术爱好者 | 依赖 Twitter/新闻 | trending 发现功能 |
| **"我的贡献在团队中如何？"** | 开发者 | 无量化参考 | 团队对比功能 |

### 4.2 高价值需求优先级

**🔴 P0 - 技术健康度评分**
- 综合 commit 频率、issue 响应、PR 合并、贡献者增长
- 输出 0-100 分数 + 等级（活跃/维护/停滞/废弃）
- 用于技术选型决策

**🟡 P1 - 公司/组织维度分析**
- 哪些公司在贡献这个生态
- 公司员工贡献排名
- 公司开源投入对比

**🟡 P1 - Trending 发现**
- 新兴 repo 发现（基于增长率而非绝对值）
- " rising stars" 榜单
- 按技术分类的 trending

**🟢 P2 - 团队贡献分析**
- 公司/团队内部贡献者对比
- 个人在团队中的贡献位置
- 需要 OAuth 登录

---

## 五、差异化战略建议

### 5.1 核心定位

> **"GitHub 生态的 Google Analytics"**

不是简单的统计工具，而是**开源生态洞察平台**。

### 5.2 差异化支柱

| 支柱 | 具体策略 | 竞品难以复制的原因 |
|------|---------|-------------------|
| **数据规模** | 持续扩大事件数据覆盖 | 需要长期积累和存储成本 |
| **AI 查询** | 强化 Data Explorer 的 NL2SQL | 需要训练数据和工程投入 |
| ** curated 内容** | 扩展 Collections 覆盖 | 需要人工维护和领域知识 |
| **开发者视角** | 深化 Developer Analytics | 多数竞品只关注 repo |
| **开放免费** | 保持核心功能免费 | 多数 SaaS 快速付费化 |

### 5.3 避免的陷阱

❌ **不要做**: 
- 与 deps.dev 竞争依赖安全分析（非核心）
- 做代码搜索（Sourcegraph 已主导）
- 过度付费化（破坏增长飞轮）

✅ **应该做**:
- 强化"发现"和"洞察"能力
- 建立开源生态的"权威数据源"地位
- 通过 API 和嵌入扩大影响力

---

## 六、具体增长机会

### 6.1 高优先级（立即行动）

| 机会 | 影响 | 难度 | 优先级 |
|------|------|------|--------|
| **技术健康度评分** | 高 | 中等 | P0 |
| **导出为图片/PDF** | 高 | 简单 | P0 |
| **API SDK 和示例** | 高 | 中等 | P0 |
| **"Rising Stars" 榜单** | 高 | 简单 | P0 |

### 6.2 中优先级（本季度）

| 机会 | 影响 | 难度 | 优先级 |
|------|------|------|--------|
| **CLI 工具** | 中 | 简单 | P1 |
| **公司维度分析** | 中 | 中等 | P1 |
| **Webhook 通知** | 中 | 中等 | P1 |
| **Slack/Discord 集成** | 中 | 简单 | P1 |

### 6.3 低优先级（探索）

| 机会 | 影响 | 难度 | 优先级 |
|------|------|------|--------|
| **浏览器扩展** | 低 | 中等 | P2 |
| **依赖图谱** | 中 | 复杂 | P2 |
| **技术雷达** | 低 | 简单 | P2 |

---

## 七、建议创建的 Issue

基于以上分析，建议创建以下 Issue：

### Issue 1: 技术健康度评分
```
Title: [Growth] Add "Project Health Score" for repos
Body: 
- Composite score (0-100) based on:
  - Commit frequency
  - Issue response time
  - PR merge rate
  - Contributor growth
  - Release cadence
- Display on repo analyze page
- Use for sorting/filtering in collections
- Help users make tech adoption decisions
```

### Issue 2: 导出功能增强
```
Title: [Growth] Add export options for reports (PNG/PDF/CSV)
Body:
- Export repo analysis as PNG/SVG image
- Export full report as PDF
- Export raw data as CSV/JSON
- Multiple size presets for social sharing
- Include OSSInsight branding for virality
```

### Issue 3: Rising Stars 榜单
```
Title: [Growth] Create "Rising Stars" trending page
Body:
- Rank repos by growth rate (not absolute stars)
- Filter by category/language/time period
- Weekly/monthly/quarterly views
- Highlight emerging technologies
- Similar to "trending" but data-driven
```

### Issue 4: API Developer Experience
```
Title: [Growth] Improve API DX with SDKs and examples
Body:
- Create official SDKs (Python, JavaScript, Go)
- Add interactive API playground
- Build example gallery with use cases
- Add API usage documentation
- Consider API key system for rate limiting
```

---

## 八、总结

OSSInsight 在**数据规模**和**AI 查询能力**上具有明显优势，但在**开发者工具生态**和**导出分享**方面存在差距。

**核心建议**:
1. 快速实现导出功能（高影响、低难度）
2. 建立技术健康度评分（差异化功能）
3. 投资 API 开发者生态（长期护城河）
4. 创建 Rising Stars 榜单（内容营销素材）

**避免**: 过度扩展至依赖分析、代码搜索等非核心领域。

---

*分析完成时间: 2026-03-20 10:47 AM (Asia/Shanghai)*
*使用模型: 千问 qwen3.5-plus*

```

### File: memory\growth_analysis.json
```json
{
  "lastRound": 15,
  "rounds": [
    {
      "round": 1,
      "date": "2025-01-10",
      "focus": "SEO 基础优化",
      "issues": [1801, 1802, 1803]
    },
    {
      "round": 2,
      "date": "2025-01-11",
      "focus": "Programmatic SEO - 语言页面",
      "issues": [1804, 1805]
    },
    {
      "round": 3,
      "date": "2025-01-12",
      "focus": "社交分享优化",
      "issues": [1806, 1807]
    },
    {
      "round": 4,
      "date": "2025-01-13",
      "focus": "用户留存 - OAuth 登录",
      "issues": [1808]
    },
    {
      "round": 5,
      "date": "2025-01-14",
      "focus": "Programmatic SEO - Trending 页面",
      "issues": [1809]
    },
    {
      "round": 6,
      "date": "2025-01-15",
      "focus": "产品体验 - 性能优化",
      "issues": [1810]
    },
    {
      "round": 7,
      "date": "2025-01-16",
      "focus": "竞品差异化 - 健康评分",
      "issues": [1811]
    },
    {
      "round": 8,
      "date": "2025-01-17",
      "focus": "用户留存 - Dashboard",
      "issues": [1812]
    },
    {
      "round": 9,
      "date": "2025-01-18",
      "focus": "GitHub 生态集成",
      "issues": [1813, 1814]
    },
    {
      "round": 10,
      "date": "2025-01-19",
      "focus": "内容营销策略",
      "issues": [1815]
    },
    {
      "round": 11,
      "date": "2025-01-20",
      "focus": "Programmatic SEO - 对比页面",
      "issues": [1816]
    },
    {
      "round": 12,
      "date": "2025-01-21",
      "focus": "用户留存 - 邮件订阅",
      "issues": [1817]
    },
    {
      "round": 13,
      "date": "2025-01-22",
      "focus": "Schema.org 结构化数据",
      "issues": [1818]
    },
    {
      "round": 14,
      "date": "2026-03-20",
      "focus": "Onboarding & First-time User Experience",
      "issues": [2033],
      "analysis": {
        "findings": [
          "首页价值主张清晰，但缺少新用户引导流程",
          "Explore 页面有 Popular questions 示例，但缺少交互式教程",
          "没有进度/成就系统激励用户探索",
          "缺少社交证明指标（查询次数、活跃用户数）",
          "对比竞品 star-history.com，他们的 CTA 更简洁直接"
        ],
        "opportunities": [
          "添加 30 秒快速上手引导（交互式教程）",
          "创建模板库页面，按场景分类（竞品分析、趋势发现、开发者画像）",
          "添加查询成就系统（首次查询、探索 5 个 repo 等）",
          "在首页展示社交证明（累计查询次数、覆盖 repo 数量）",
          "优化空状态引导，提供 contextual help"
        ]
      }
    },
    {
      "round": 15,
      "date": "2026-03-20",
      "focus": "Analytics & A/B Testing Infrastructure",
      "issues": [2034],
      "analysis": {
        "findings": [
          "当前只有 Google Analytics 基础 pageview 追踪，无自定义事件",
          "关键交互缺失追踪：搜索、分享、反馈、导出、Collections",
          "无法构建用户漏斗，不知道转化率",
          "没有 A/B 测试基础设施，无法数据驱动优化",
          "无法区分新用户 vs 回访用户行为"
        ],
        "opportunities": [
          "创建统一 analytics.ts 追踪库，集成 PostHog（开源可自托管）",
          "追踪 5 大类事件：搜索发现、分析流程、分享传播、反馈质量、Collections 留存",
          "实现 useAnalytics hook 供 React 组件调用",
          "添加 A/B 测试框架和 feature flags",
          "建立增长仪表盘，追踪核心指标（搜索转化率、分享率、k-factor）"
        ],
        "impact": "这是所有增长工作的基础设施 - 没有数据就无法优化。预计 2-3 周完成，完成后可以：1) 识别转化漏斗流失点 2) 运行 A/B 测试优化关键页面 3) 追踪病毒传播系数 4) 数据驱动决策而非猜测"
      }
    }
  ],
  "nextFocus": "Viral Loops & Referral Mechanisms"
}

```

### File: memory\growth_analysis_round_10.md
```md
# Growth Analysis Round 10 - Developer Experience (DX): API SDK + CLI Tools

**Date:** 2026-03-20
**Focus:** Developer Experience - API SDK, CLI Tools, and Developer Resources
**Model:** qwen3.5-plus

## Current State Analysis

### ✅ Strengths
- **OpenAPI Spec:** Complete specification at `configs/public_api/openapi.yaml`
- **API Documentation:** Well-structured docs using fumadocs (`apps/docs/app/docs/api/`)
- **No Auth Required:** Beta version is open (600 req/hour/IP, 1000 req/minute global)
- **Showcase Page:** Displays third-party integrations (Raycast extension, ChatGH, etc.)
- **API Routes:** Comprehensive v1 endpoints for repos, collections, trends

### ❌ Gaps (Growth Opportunities)
1. **No Official SDK** - No JavaScript/TypeScript/Python/Go SDKs
2. **No CLI Tool** - No command-line interface for quick data access
3. **No Interactive Playground** - No in-browser API testing UI
4. **No Cookbook/Recipes** - No code examples for common use cases
5. **No Postman Collection** - No ready-to-import API collection

## Competitive Analysis

| Platform | SDK | CLI | Playground | Docs |
|----------|-----|-----|------------|------|
| OSSInsight | ❌ | ❌ | ❌ | ✅ |
| Libraries.io | ✅ (Ruby/JS) | ❌ | ❌ | ✅ |
| GitHub API | ✅ (Octokit - multi-lang) | ✅ (gh) | ✅ | ✅ |
| npm trends | ❌ | ❌ | ❌ | ⚠️ |
| Star History | ❌ | ❌ | ❌ | ⚠️ |

## Growth Opportunities (Prioritized)

### 1. Official TypeScript/JavaScript SDK (HIGH PRIORITY)
**Why:** Most API consumers are frontend/Node.js developers
**Impact:** 
- Reduces integration friction
- Type safety improves developer experience
- Increases API adoption rate

**Implementation:**
```
packages/sdk-ts/
├── src/
│   ├── client.ts
│   ├── endpoints/
│   │   ├── repos.ts
│   │   ├── collections.ts
│   │   └── trends.ts
│   └── types.ts
├── package.json
└── README.md
```

**Example API:**
```typescript
import { OSSInsight } from '@ossinsight/sdk';

const client = new OSSInsight();
const stargazers = await client.repos('pingcap/tidb').stargazers.countries();
const trending = await client.trends.repos({ period: '7d' });
```

### 2. CLI Tool (HIGH PRIORITY)
**Why:** Developers love CLI tools for automation and quick queries
**Impact:**
- Viral potential in developer communities
- Integrates into CI/CD workflows
- Generates social proof (terminal screenshots)

**Implementation:**
```bash
# Installation
npm install -g ossinsight

# Usage examples
ossinsight repo pingcap/tidb stargazers --format json
ossinsight trending --period 7d --limit 10
ossinsight collection awesome-db ranking
```

### 3. API Playground (MEDIUM PRIORITY)
**Why:** Interactive testing reduces learning curve
**Impact:**
- Increases API exploration time
- Reduces support questions
- Better first-time experience

**Features:**
- Pre-populated examples
- Live response preview
- Copy-as-cURL/JavaScript/Python
- Authentication (if needed in future)

### 4. Cookbook / Recipes (MEDIUM PRIORITY)
**Why:** Developers learn by example
**Impact:**
- Faster time-to-integration
- More diverse use cases discovered
- SEO content for developer queries

**Example Recipes:**
- "Get top 10 trending repos this week"
- "Compare stargazers between two repos"
- "Build a repo health dashboard"
- "Export collection data to CSV"

### 5. Postman Collection (LOW PRIORITY)
**Why:** Some developers prefer Postman for API testing
**Impact:**
- Easier API exploration for Postman users
- Shareable collections
- Auto-generated documentation

## Expected Outcomes

| Initiative | Effort | Impact | Timeline |
|------------|--------|--------|----------|
| TypeScript SDK | Medium | High | 2-3 weeks |
| CLI Tool | Medium | High | 2-3 weeks |
| API Playground | High | Medium | 3-4 weeks |
| Cookbook | Low | Medium | 1-2 weeks |
| Postman Collection | Low | Low | 1 week |

## Recommended Next Steps

1. **Start with TypeScript SDK** - Highest impact for developer adoption
2. **Build CLI tool in parallel** - Uses same SDK internally
3. **Create initial cookbook** - 5-10 common recipes
4. **Add API Playground** - After SDK is stable
5. **Promote in developer communities** - Hacker News, Reddit, Twitter

## Related Files
- `configs/public_api/openapi.yaml` - OpenAPI spec
- `apps/docs/app/docs/api/` - API documentation
- `packages/api-server/src/routes/v1/` - API route implementations

```

### File: memory\growth_analysis_round_6.json
```json
{
  "round": 6,
  "date": "2026-03-20",
  "angle": "📈 用户获取（Acquisition）- 程序化内容页面 (Programmatic SEO)",
  "analysis": {
    "current_state": {
      "sitemap_coverage": "仅包含 1000 个 top repos + collections，覆盖率极低",
      "indexed_pages": "约 1000-2000 页",
      "programmatic_pages": "仅有 /analyze/[owner]/[repo] 动态页面",
      "missing_dimensions": [
        "编程语言 landing pages (/languages/JavaScript, /languages/Rust 等)",
        "Topic landing pages (/topics/ai, /topics/machine-learning 等)",
        "组织/公司 pages (/orgs/microsoft, /orgs/google 等) - 已有但未优化",
        "开发者用户 pages (/users/torvalds 等) - 已有但未优化",
        "趋势榜单 pages (/trending/daily, /trending/weekly 等)",
        "对比结果 pages (/compare/react/vue 等)"
      ]
    },
    "opportunities": [
      {
        "id": "prog-seo-1",
        "title": "编程语言 Landing Pages",
        "description": "为每个主流编程语言创建独立的聚合分析页面，展示该语言下最活跃的 repos、趋势、明星项目等",
        "target_keywords": [
          "JavaScript GitHub stats",
          "Rust repositories trending",
          "Python open source projects",
          "TypeScript GitHub analytics",
          "Go language projects"
        ],
        "estimated_pages": "~50 个主流语言 × 1 page = 50 pages",
        "long_tail_potential": "每个语言页面可链接到该语言下 top 1000 repos，形成内部链接网络",
        "implementation": {
          "route": "/languages/[language]",
          "data_needed": "按语言聚合的 repo 统计数据",
          "content_sections": [
            "语言概述（总项目数、总 stars、活跃开发者数）",
            "Top 20 trending repos this week",
            "Fastest growing repos",
            "Most starred new repos",
            "Key contributors in this language",
            "Related languages"
          ]
        },
        "impact": "高",
        "difficulty": "中等",
        "priority": "P0"
      },
      {
        "id": "prog-seo-2",
        "title": "GitHub Topics Landing Pages",
        "description": "为每个热门 GitHub Topic 创建聚合页面，捕获按主题搜索的长尾流量",
        "target_keywords": [
          "best AI GitHub repositories",
          "machine learning open source projects",
          "web development frameworks GitHub",
          "blockchain projects GitHub",
          "devops tools open source"
        ],
        "estimated_pages": "~500 个热门 topics × 1 page = 500 pages",
        "long_tail_potential": "Topic 搜索是开发者发现项目的主要方式之一",
        "implementation": {
          "route": "/topics/[topic]",
          "data_needed": "GitHub topics API 或内部 tags 数据",
          "content_sections": [
            "Topic 概述",
            "Top repos in this topic",
            "Related topics",
            "Trending repos this week",
            "New repos added recently"
          ]
        },
        "impact": "高",
        "difficulty": "中等",
        "priority": "P0"
      },
      {
        "id": "prog-seo-3",
        "title": "组织/公司 Hub Pages",
        "description": "为公司/组织创建更丰富的聚合页面，展示其开源影响力",
        "target_keywords": [
          "Microsoft open source projects",
          "Google GitHub repositories",
          "Meta open source",
          "Amazon open source projects"
        ],
        "estimated_pages": "~1000 个活跃组织",
        "implementation": {
          "route": "/orgs/[org]",
          "enhancement": "当前已有 /analyze/(org)/[owner] 页面，但需要增强内容深度和 SEO",
          "content_sections": [
            "组织概况（总 repos、总 stars、成员数）",
            "Top repos by stars",
            "Most active repos this month",
            "Contribution activity heatmap",
            "Top contributors",
            "Compare with similar orgs"
          ]
        },
        "impact": "中",
        "difficulty": "简单",
        "priority": "P1"
      },
      {
        "id": "prog-seo-4",
        "title": "趋势榜单 Pages (Trending Lists)",
        "description": "创建多种维度的趋势榜单页面，捕获'trending'相关搜索",
        "target_keywords": [
          "trending GitHub repos today",
          "most starred repos this week",
          "fastest growing open source projects",
          "hot GitHub projects"
        ],
        "estimated_pages": "~20 个榜单变体",
        "implementation": {
          "routes": [
            "/trending/daily",
            "/trending/weekly",
            "/trending/monthly",
            "/trending/[language]",
            "/rising/daily",
            "/rising/weekly",
            "/new/notable"
          ],
          "content_sections": [
            "榜单列表（可交互表格）",
            "趋势图表",
            "历史对比",
            "订阅此榜单 CTA"
          ]
        },
        "impact": "高",
        "difficulty": "简单",
        "priority": "P0"
      },
      {
        "id": "prog-seo-5",
        "title": "对比结果 Pages (SEO-friendly)",
        "description": "将 repo 对比结果生成为可索引的静态页面，捕获对比类搜索",
        "target_keywords": [
          "React vs Vue GitHub stats",
          "Next.js vs Gatsby comparison",
          "TensorFlow vs PyTorch stars"
        ],
        "estimated_pages": "理论上无限，可限制为 top 10000 repos 的组合",
        "implementation": {
          "route": "/compare/[repo1]/[repo2]",
          "seo_note": "需要生成独特的 meta description 和 title，避免重复内容问题",
          "content_sections": [
            "侧边对比图表",
            "关键指标对比表",
            "增长曲线对比",
            "Verdict/Summary（AI 生成）"
          ]
        },
        "impact": "中",
        "difficulty": "中等",
        "priority": "P1"
      },
      {
        "id": "prog-seo-6",
        "title": "扩展 Sitemap 覆盖",
        "description": "将 sitemap 从 1000 个 repos 扩展到 10 万 +，覆盖更多长尾 repos",
        "implementation": {
          "current": "1000 repos",
          "target": "100,000+ repos",
          "strategy": [
            "分片 sitemap (sitemap-0.xml, sitemap-1.xml, ...)",
            "按 stars 阈值分层：top 10k (priority 0.8), top 100k (priority 0.5)",
            "使用 Next.js incremental static regeneration 预渲染热门 pages"
          ]
        },
        "impact": "高",
        "difficulty": "简单",
        "priority": "P0"
      }
    ],
    "technical_recommendations": {
      "sitemap_scaling": {
        "issue": "当前 sitemap.ts 只生成 ~1000 条 URLs",
        "solution": "实现分页 sitemap，使用 sitemap-index.xml 管理多个子 sitemap",
        "code_example": "创建 /app/sitemap/[page]/route.ts 处理分页"
      },
      "isg_strategy": {
        "recommendation": "对 top 10k repos 使用 ISR (revalidate: 3600)，对长尾 repos 使用 SSR",
        "benefit": "平衡 SEO 覆盖和服务器负载"
      },
      "internal_linking": {
        "recommendation": "在每个 repo 页面添加'Related repos'模块，链接到同语言/同 topic 的其他 repos",
        "benefit": "提升爬虫抓取深度，传递 PageRank"
      },
      "structured_data": {
        "current": "已有 SoftwareSourceCode schema",
        "enhancement": "添加 ItemList schema 用于榜单页面，BreadcrumbList 用于导航"
      }
    },
    "traffic_projection": {
      "current_estimated_organic": "50,000-100,000 monthly visits (估算)",
      "potential_after_implementation": "300,000-500,000 monthly visits (6-12 个月)",
      "breakdown": {
        "language_pages": "50 pages × 200 visits/page/month = 10,000",
        "topic_pages": "500 pages × 100 visits/page/month = 50,000",
        "expanded_repos": "100k repos × 0.5 visits/repo/month = 50,000",
        "trending_pages": "20 pages × 5000 visits/page/month = 100,000",
        "brand_search_lift": "SEO 可见度提升带来的品牌搜索增长 = 50,000+"
      }
    }
  },
  "issues_to_create": [
    {
      "title": "[Growth] Programmatic SEO: Language & Topic landing pages",
      "body": "## 机会\n\n当前 OSSInsight 仅有 ~1000 个 repo 页面被 sitemap 收录，但 GitHub 有数亿个 repositories。通过程序化 SEO 策略，可以低成本创建大量高质量 landing pages，捕获长尾搜索流量。\n\n## 建议实现\n\n### P0 - 高优先级\n\n1. **编程语言 Landing Pages** (`/languages/[language]`)\n   - 展示该语言下 trending repos、增长最快的项目、明星贡献者\n   - 目标关键词：\"JavaScript GitHub stats\", \"Rust repositories trending\" 等\n   - 预计 ~50 个页面\n\n2. **Topic Landing Pages** (`/topics/[topic]`)\n   - 为 AI、ML、Web 开发等热门主题创建聚合页\n   - 目标关键词：\"best AI GitHub repositories\", \"machine learning open source\"\n   - 预计 ~500 个页面\n\n3. **趋势榜单 Pages** (`/trending/daily`, `/trending/weekly`, `/trending/[language]`)\n   - 捕获 \"trending GitHub repos\" 相关搜索\n   - 可订阅的榜单，促进用户留存\n\n4. **扩展 Sitemap** - 从 1000 扩展到 10 万 + repos\n   - 使用分页 sitemap (sitemap-index.xml)\n   - 按 stars 分层设置 priority\n\n### P1 - 中优先级\n\n5. **组织 Hub Pages 增强** - 优化现有 `/orgs/[org]` 页面的 SEO\n6. **对比结果 Pages** - `/compare/[repo1]/[repo2]` 生成可索引页面\n\n## 技术建议\n\n- 对 top 10k repos 使用 ISR (revalidate: 3600)\n- 添加 ItemList schema 用于榜单页面\n- 在每个 repo 页面添加 \"Related repos\" 内部链接模块\n\n## 预期影响\n\n- 当前自然搜索流量：~50k-100k monthly visits (估算)\n- 实施后 6-12 个月：~300k-500k monthly visits\n- 主要增长来源：长尾关键词覆盖、榜单页面病毒传播\n\n## 竞品参考\n\n- GitHub Trends: https://github.com/trending\n- Star History: https://star-history.com/\n- LibHunt: https://www.libhunt.com/\n\n---\n\n**Labels:** enhancement, growth, seo\n**Priority:** High",
      "labels": ["enhancement", "growth", "seo"]
    }
  ],
  "message_content": "📊 **OSSInsight 增长分析 - 第 6 轮**\n\n**使用模型：** 千问 qwen3.5-plus\n**本轮角度：** 📈 用户获取（Acquisition）- 程序化内容页面 (Programmatic SEO)\n\n---\n\n## 🔍 核心发现\n\n当前 sitemap 仅覆盖 **~1000 个 repos**，但 GitHub 有数亿个项目。通过程序化 SEO 策略，可低成本创建大量高质量 landing pages，捕获长尾搜索流量。\n\n---\n\n## 🎯 具体机会（按优先级）\n\n### P0 - 高优先级\n\n1. **编程语言 Landing Pages** (`/languages/[language]`)\n   - 展示该语言下 trending repos、增长最快项目、明星贡献者\n   - 目标关键词：\"JavaScript GitHub stats\", \"Rust repositories trending\"\n   - 预计 ~50 个页面\n\n2. **Topic Landing Pages** (`/topics/[topic]`)\n   - 为 AI、ML、Web 开发等热门主题创建聚合页\n   - 预计 ~500 个页面\n\n3. **趋势榜单 Pages** (`/trending/daily|weekly|[language]`)\n   - 捕获 \"trending GitHub repos\" 相关搜索\n   - 可订阅榜单，促进留存\n\n4. **扩展 Sitemap** - 从 1000 → 10 万 + repos\n   - 使用分页 sitemap (sitemap-index.xml)\n   - 按 stars 分层设置 priority\n\n### P1 - 中优先级\n\n5. **组织 Hub Pages 增强** - 优化现有 `/orgs/[org]` 页面\n6. **对比结果 Pages** - `/compare/[repo1]/[repo2]` 可索引化\n\n---\n\n## 📈 流量预估\n\n| 指标 | 当前 | 目标 (6-12 个月) |\n|------|------|------------------|\n| 收录页面 | ~1,000 | ~100,000+ |\n| 月自然搜索流量 | ~50k-100k | ~300k-500k |\n| 长尾关键词覆盖 | 低 | 高 |\n\n---\n\n## 🎯 影响评估\n\n- **预估影响：** 🔥 高 (可能带来 3-5x 自然搜索流量增长)\n- **实施难度：** ⚙️ 中等 (需要数据聚合 + 新路由开发)\n- **优先级建议：** P0 - 建议立即启动\n\n---\n\n## 📝 后续动作\n\n即将创建 GitHub issue：\n- `[Growth] Programmatic SEO: Language & Topic landing pages`\n\n这是目前 ROI 最高的增长杠杆，建议优先实施。",
  "issues_created": [],
  "next_round_angle": "🛠️ 产品改进 - 性能优化与 Core Web Vitals"
}

```

### File: memory\issue_2015.md
```md
## 竞品分析

通过对标 Libraries.io、Open Source Insights (Google)、RepoRater 等竞品，发现 OSSInsight 缺少**项目健康度评分**功能。

### 竞品现状

| 竞品 | 健康度指标 | 维护者分析 |
|------|-----------|-----------|
| Libraries.io | 依赖树健康度 | 维护者数量追踪 |
| Open Source Insights | 依赖图分析 | ❌ |
| RepoRater | 综合评分系统 | ❌ |
| **OSSInsight** | ❌ | ❌ |

## 建议功能

### 1. 项目健康度评分 (Project Health Score)

综合以下维度计算 0-100 分：

- **活跃度** (30%): 近 3 个月 commit 频率、issue/PR 处理速度
- **社区参与** (25%): 贡献者数量变化、PR review 响应时间
- **代码质量** (20%): PR 合并率、issue 关闭率、平均 PR 大小
- **增长趋势** (15%): Star 增长率、Fork 增长率
- **维护可持续性** (10%): 核心维护者数量、Bus Factor 评估

### 2. 维护者可持续性指标

- **Bus Factor**: 多少核心贡献者离开会导致项目停滞
- **贡献集中度**: Top 5 贡献者占比（过高表示风险）
- **响应 SLA**: issue/PR 平均响应时间、关闭时间
- **维护者 burnout 预警**: 单个维护者负载过高时提醒

### 3. 差异化价值

✅ **数据优势**: 基于 10 亿 + GitHub 事件数据，比竞品更准确
✅ **AI 驱动**: 可用 Chat2Query 自定义健康度公式
✅ **可视化**: 历史趋势图 + 同行对比

## 实施建议

### Phase 1 (MVP - 2 周)
- [ ] 定义健康度评分算法
- [ ] 在 Repo Analytics 页面增加 Health Score 展示
- [ ] 添加 Collection 健康度排行榜

### Phase 2 (4 周)
- [ ] 维护者可持续性分析
- [ ] Bus Factor 计算
- [ ] 健康度预警通知（配合 #2007 邮件订阅）

### Phase 3 (6 周)
- [ ] API 开放健康度数据
- [ ] Badge 支持
- [ ] 企业版：私有 repo 健康度监控

## 预期影响

- 📈 **用户获取**: 健康度 Badge 可嵌入 README，带来自然流量
- 🔄 **用户留存**: 项目维护者会定期查看健康度变化
- 🦠 **病毒传播**: 健康度评分易于在社交媒体传播讨论

## 技术实现

健康度评分可基于现有 GitHub Events 数据计算，无需额外数据源。

## 参考

- CHAOSS Metrics - 开源社区健康度标准
- Maintainer Survey - 维护者调研数据

```

### File: memory\issue_2016.md
```md
## 竞品分析

Libraries.io 和 Google Open Source Insights 的核心功能是**依赖关系分析**，OSSInsight 目前缺少此功能。

### 用户场景

1. **安全审计**: 我的项目依赖了哪些有安全漏洞的库？
2. **影响分析**: 某个底层库更新会影响哪些上游项目？
3. **生态洞察**: 某个技术栈的依赖关系图谱
4. **维护者视角**: 有多少项目依赖我的库？

## 建议功能

### 1. 依赖关系图谱 (Dependency Graph)

- 基于 GitHub package.json, Cargo.toml, go.mod 等文件解析依赖
- 可视化展示直接依赖和传递依赖
- 支持钻取：点击依赖项查看其详情

### 2. 反向依赖追踪 (Reverse Dependencies)

- 显示有多少项目依赖当前 repo
- 按影响力排序（依赖者的 star 数、下载量）
- 变更影响预警：你更新可能影响的项目列表

### 3. 依赖健康度分析

- 依赖项的更新频率
- 依赖项的健康度评分（联动 #2015）
- 过期依赖预警
- 安全漏洞关联（集成 GitHub Advisory Database）

### 4. 生态位分析

- 在依赖图谱中的位置（核心库 vs 边缘库）
- 同类替代品对比
- 技术栈演变趋势

## 差异化价值

| 功能 | Libraries.io | OSSInsight (建议) |
|------|-------------|------------------|
| 依赖图谱 | ✅ | ✅ |
| 反向依赖 | ✅ | ✅ + 影响力排序 |
| 健康度评分 | ❌ | ✅ (联动 #2015) |
| 趋势分析 | 基础 | ✅ AI 驱动深度分析 |
| 数据覆盖 | 多包管理器 | GitHub 全量事件 |

## 实施建议

### Phase 1 (MVP - 4 周)
- [ ] ETL: 解析 repo 根目录的包管理文件
- [ ] 存储依赖关系到 ClickHouse/TiDB
- [ ] 基础依赖列表页面

### Phase 2 (6 周)
- [ ] 反向依赖查询
- [ ] 依赖关系可视化图谱
- [ ] 依赖健康度指标

### Phase 3 (8 周)
- [ ] 安全漏洞集成
- [ ] 变更影响分析
- [ ] API 开放

## 技术挑战

1. **数据量**: 需要解析百万 + repo 的包管理文件
2. **更新频率**: 依赖关系变化频繁，需要增量更新
3. **多语言支持**: npm, pip, cargo, go, maven 等

## 预期影响

- 📈 **用户获取**: 依赖分析是开发者高频需求
- 🔄 **用户留存**: 项目维护者定期检查依赖健康度
- 💰 **商业化**: 企业版可提供私有依赖扫描

## 参考

- [Libraries.io](https://libraries.io/)
- [Google Open Source Insights](https://deps.dev/)
- [GitHub Dependency Graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph)

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
