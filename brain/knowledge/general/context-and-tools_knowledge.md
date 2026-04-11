# Knowledge Dump for context-and-tools

## File: claude.md
```
# Netlify Context and Tools

This repository contains public Netlify skills — factual platform reference for AI agents working with Netlify projects.

## Repository Structure

- `context/` — Steering guides (e.g., POWER.md for Kiro deployments)
- `.claude-plugin/` — Plugin marketplace config for Claude Code installation
- `skills/` — Netlify platform skills (source of truth for all agent formats)
- `cursor/rules/` — Auto-generated Cursor `.mdc` rule files (do NOT edit directly)
- `codex/` — Auto-generated Codex skills and `AGENTS.md` router (do NOT edit directly)
- `scripts/build-cursor-rules.sh` — Converts `skills/` → `cursor/rules/`
- `scripts/build-codex-skills.sh` — Copies `skills/` → `codex/` and generates `AGENTS.md`
- `.github/workflows/build-cursor-rules.yml` — Runs the build on push to main and PRs
- `.github/workflows/build-codex-skills.yml` — Runs the Codex build on push to main and PRs

## Skills

The `skills/` directory contains skills covering Netlify platform primitives. See `skills/CLAUDE.md` for a guide on when to use each skill.

## Cursor Rules

The `cursor/rules/` directory is **auto-generated** from `skills/` and must never be edited directly. A GitHub Actions workflow rebuilds these files whenever `skills/` changes on `main`. To rebuild locally:

```bash
bash scripts/build-cursor-rules.sh
```

## Contributing

Skills should be factual and platform-focused — not opinionated about frameworks, ORMs, or workflow preferences. They help any agent work correctly with Netlify primitives.

Each skill follows the standard SKILL.md format with YAML frontmatter (`name` and `description`). Keep SKILL.md files under 500 lines. Use `references/` subdirectories for detailed content.

**Important:** Always edit files in `skills/`. Never edit files in `cursor/rules/` or `codex/` — they are overwritten by CI.

```

## File: gemini-extension.json
```
{
  "name": "netlify-skills",
  "version": "1.1.0",
  "skills": [
    "skills/netlify-functions",
    "skills/netlify-edge-functions",
    "skills/netlify-blobs",
    "skills/netlify-db",
    "skills/netlify-image-cdn",
    "skills/netlify-forms",
    "skills/netlify-frameworks",
    "skills/netlify-caching",
    "skills/netlify-config",
    "skills/netlify-cli-and-deploy",
    "skills/netlify-deploy",
    "skills/netlify-ai-gateway",
    "skills/netlify-identity"
  ]
}

```

## File: README.md
```
# Netlify Context and Tools

Public Netlify skills for AI coding agents. Each skill is a focused, factual reference for a Netlify platform primitive — designed to help agents build correctly on Netlify without needing to search docs.

## Skills

| Skill | What it covers |
|---|---|

### References

Some skills include `references/` subdirectories with deeper content:


## Installation

### Codex Desktop App

Install the Netlify plugin from the [Codex plugin directory](https://developers.openai.com/codex/plugins/) in the Codex desktop app.

The plugin lets Codex deploy to Netlify without leaving your coding workflow. You can create projects, generate preview URLs, deploy to production, validate build configuration, and inspect deploy status and logs. For full details, refer to [Deploy from Codex with the Netlify Plugin](https://www.netlify.com/changelog/2026-03-27-deploy-from-codex-netlify-plugin/).

### Codex CLI

Copy the pre-built `codex/` directory into your project root:

```bash
git clone --depth 1 https://github.com/netlify/context-and-tools.git /tmp/netlify-skills && \
  cp -r /tmp/netlify-skills/codex . && \
  rm -rf /tmp/netlify-skills
```

This gives you `codex/AGENTS.md` (the skill router) and `codex/skills/` with all Netlify skills. Codex discovers `AGENTS.md` automatically and activates skills by name using `$skill-name` syntax.

### Claude Code

Add the marketplace and install the plugin:

```
/plugin marketplace add netlify/context-and-tools
/plugin install netlify-skills@netlify-context-and-tools
```

This installs all Netlify skills into Claude Code. The included `skills/CLAUDE.md` acts as a router — it tells the agent which skill to read based on what you're building.

### Cursor

Install from the [Cursor plugin marketplace](https://cursor.com/marketplace):

1. Open Cursor Settings (`Cmd+,` / `Ctrl+,`)
2. Go to **Plugins**
3. Search for **netlify-skills**
4. Click **Install**

Or install via the command palette: `Cmd+Shift+P` → **Plugins: Install Plugin** → search **netlify-skills**.

This installs 21 `.mdc` rule files covering all Netlify platform primitives. A router rule (`netlify-skills-router.mdc`) is always active and directs the agent to the right skill for the task.

<details>
<summary>Manual installation (without the plugin marketplace)</summary>

Copy pre-built rule files directly into your project:

```bash
git clone --depth 1 https://github.com/netlify/context-and-tools.git /tmp/netlify-skills && \
  mkdir -p .cursor/rules && \
  cp /tmp/netlify-skills/cursor/rules/*.mdc .cursor/rules/ && \
  rm -rf /tmp/netlify-skills
```

This copies `.mdc` rule files into `.cursor/rules/`, where Cursor automatically discovers them.

</details>



### Other AI agents

Each `SKILL.md` file is a self-contained reference with YAML frontmatter (`name` and `description`) and markdown body. Feed them into any agent's context as needed.

## Design Principles

- **Factual, not opinionated** — platform behavior and API reference, not workflow preferences
- **Composable** — skills cover individual primitives; agents combine them as needed
- **Concise** — each SKILL.md stays under 500 lines; detailed content goes in `references/`
- **Current** — covers modern Netlify patterns (v2 functions, Vite plugin, AI Gateway)

## Contributing

Keep skills focused on Netlify platform primitives. Each skill should answer "how does this Netlify feature work?" rather than "how should I structure my project?"

Follow the existing format: YAML frontmatter with `name` and `description`, markdown body, code examples with TypeScript where applicable. Use `references/` subdirectories for content that would push a SKILL.md past 500 lines.

### Cursor rules and Codex skills are generated — do not edit them directly

The `cursor/rules/` and `codex/` directories are auto-generated from `skills/` by GitHub Actions workflows. Always edit the source files in `skills/` — the workflows rebuild on every push to `main` that changes `skills/`. To test locally:

```bash
bash scripts/build-cursor-rules.sh
bash scripts/build-codex-skills.sh
```

```

## File: renovate.json
```
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": [
    "local>netlify/renovate-config"
  ]
}

```

## File: _GIT_INGEST.md
```
# OmniClaw Repo Plow: CIV_FETCHED_context-and-tools_150409



================================================
FILE: CLAUDE.md
================================================
# Netlify Context and Tools

This repository contains public Netlify skills — factual platform reference for AI agents working with Netlify projects.

## Repository Structure

- `context/` — Steering guides (e.g., POWER.md for Kiro deployments)
- `.claude-plugin/` — Plugin marketplace config for Claude Code installation
- `skills/` — Netlify platform skills (source of truth for all agent formats)
- `cursor/rules/` — Auto-generated Cursor `.mdc` rule files (do NOT edit directly)
- `codex/` — Auto-generated Codex skills and `AGENTS.md` router (do NOT edit directly)
- `scripts/build-cursor-rules.sh` — Converts `skills/` → `cursor/rules/`
- `scripts/build-codex-skills.sh` — Copies `skills/` → `codex/` and generates `AGENTS.md`
- `.github/workflows/build-cursor-rules.yml` — Runs the build on push to main and PRs
- `.github/workflows/build-codex-skills.yml` — Runs the Codex build on push to main and PRs

## Skills

The `skills/` directory contains skills covering Netlify platform primitives. See `skills/CLAUDE.md` for a guide on when to use each skill.

## Cursor Rules

The `cursor/rules/` directory is **auto-generated** from `skills/` and must never be edited directly. A GitHub Actions workflow rebuilds these files whenever `skills/` changes on `main`. To rebuild locally:

```bash
bash scripts/build-cursor-rules.sh
```

## Contributing

Skills should be factual and platform-focused — not opinionated about frameworks, ORMs, or workflow preferences. They help any agent work correctly with Netlify primitives.

Each skill follows the standard SKILL.md format with YAML frontmatter (`name` and `description`). Keep SKILL.md files under 500 lines. Use `references/` subdirectories for detailed content.

**Important:** Always edit files in `skills/`. Never edit files in `cursor/rules/` or `codex/` — they are overwritten by CI.


================================================
FILE: gemini-extension.json
================================================
{
  "name": "netlify-skills",
  "version": "1.1.0",
  "skills": [
    "skills/netlify-functions",
    "skills/netlify-edge-functions",
    "skills/netlify-blobs",
    "skills/netlify-db",
    "skills/netlify-image-cdn",
    "skills/netlify-forms",
    "skills/netlify-frameworks",
    "skills/netlify-caching",
    "skills/netlify-config",
    "skills/netlify-cli-and-deploy",
    "skills/netlify-deploy",
    "skills/netlify-ai-gateway",
    "skills/netlify-identity"
  ]
}


================================================
FILE: README.md
================================================
# Netlify Context and Tools

Public Netlify skills for AI coding agents. Each skill is a focused, factual reference for a Netlify platform primitive — designed to help agents build correctly on Netlify without needing to search docs.

## Skills

| Skill | What it covers |
|---|---|

### References

Some skills include `references/` subdirectories with deeper content:


## Installation

### Codex Desktop App

Install the Netlify plugin from the [Codex plugin directory](https://developers.openai.com/codex/plugins/) in the Codex desktop app.

The plugin lets Codex deploy to Netlify without leaving your coding workflow. You can create projects, generate preview URLs, deploy to production, validate build configuration, and inspect deploy status and logs. For full details, refer to [Deploy from Codex with the Netlify Plugin](https://www.netlify.com/changelog/2026-03-27-deploy-from-codex-netlify-plugin/).

### Codex CLI

Copy the pre-built `codex/` directory into your project root:

```bash
git clone --depth 1 https://github.com/netlify/context-and-tools.git /tmp/netlify-skills && \
  cp -r /tmp/netlify-skills/codex . && \
  rm -rf /tmp/netlify-skills
```

This gives you `codex/AGENTS.md` (the skill router) and `codex/skills/` with all Netlify skills. Codex discovers `AGENTS.md` automatically and activates skills by name using `$skill-name` syntax.

### Claude Code

Add the marketplace and install the plugin:

```
/plugin marketplace add netlify/context-and-tools
/plugin install netlify-skills@netlify-context-and-tools
```

This installs all Netlify skills into Claude Code. The included `skills/CLAUDE.md` acts as a router — it tells the agent which skill to read based on what you're building.

### Cursor

Install from the [Cursor plugin marketplace](https://cursor.com/marketplace):

1. Open Cursor Settings (`Cmd+,` / `Ctrl+,`)
2. Go to **Plugins**
3. Search for **netlify-skills**
4. Click **Install**

Or install via the command palette: `Cmd+Shift+P` → **Plugins: Install Plugin** → search **netlify-skills**.

This installs 21 `.mdc` rule files covering all Netlify platform primitives. A router rule (`netlify-skills-router.mdc`) is always active and directs the agent to the right skill for the task.

<details>
<summary>Manual installation (without the plugin marketplace)</summary>

Copy pre-built rule files directly into your project:

```bash
git clone --depth 1 https://github.com/netlify/context-and-tools.git /tmp/netlify-skills && \
  mkdir -p .cursor/rules && \
  cp /tmp/netlify-skills/cursor/rules/*.mdc .cursor/rules/ && \
  rm -rf /tmp/netlify-skills
```

This copies `.mdc` rule files into `.cursor/rules/`, where Cu

================================================
FILE: renovate.json
================================================
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": [
    "local>netlify/renovate-config"
  ]
}


================================================
FILE: .claude-plugin\marketplace.json
================================================
{
  "name": "netlify-context-and-tools",
  "owner": {
    "name": "Netlify"
  },
  "plugins": [
    {
      "name": "netlify-skills",
      "description": "Netlify platform skills — functions, edge functions, blobs, database, identity, image CDN, forms, config, CLI, frameworks, caching, AI gateway, and deployment",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/netlify-functions",
        "./skills/netlify-edge-functions",
        "./skills/netlify-blobs",
        "./skills/netlify-db",
        "./skills/netlify-image-cdn",
        "./skills/netlify-forms",
        "./skills/netlify-frameworks",
        "./skills/netlify-caching",
        "./skills/netlify-config",
        "./skills/netlify-cli-and-deploy",
        "./skills/netlify-deploy",
        "./skills/netlify-ai-gateway",
        "./skills/netlify-identity"
      ]
    }
  ]
}


================================================
FILE: .claude-plugin\plugin.json
================================================
{
  "name": "netlify-skills",
  "version": "1.1.0",
  "description": "Netlify platform skills for Claude Code",
  "author": {
    "name": "Netlify"
  },
  "repository": "https://github.com/netlify/context-and-tools"
}


================================================
FILE: .cursor-plugin\plugin.json
================================================
{
  "name": "netlify-skills",
  "version": "1.1.0",
  "description": "Netlify platform skills — functions, edge functions, blobs, database, identity, image CDN, forms, config, CLI, frameworks, caching, AI gateway, and deployment",
  "author": {
    "name": "Netlify"
  },
  "homepage": "https://www.netlify.com",
  "repository": "https://github.com/netlify/context-and-tools",
  "keywords": [
    "netlify",
    "deployment",
    "serverless",
    "edge-functions",
    "cdn",
    "hosting",
    "jamstack",
    "functions"
  ],
  "rules": "cursor/rules"
}


================================================
FILE: codex\AGENTS.md
================================================
# Netlify Skills

This project deploys on Netlify. Use these skills for guidance on Netlify platform primitives. Each skill provides specific, factual reference for working with a Netlify feature.

## When to Use Each Skill

**Building API endpoints or server-side logic?**
Read `$netlify-functions` for modern function syntax, routing, background/scheduled functions.

**Need low-latency middleware, geo-based logic, or request manipulation?**
Read `$netlify-edge-functions` for edge compute patterns.

**Storing files, images, or simple key-value data?**
Read `$netlify-blobs` for object storage API.

**Need a relational database?**
Read `$netlify-db` for Neon Postgres setup, Drizzle ORM, and migrations. It also covers when Blobs is a better fit.

**Optimizing or transforming images?**
Read `$netlify-image-cdn` for the image transformation endpoint and clean URL patterns. For user-uploaded images, see `$netlify-image-cdn/references/user-uploads.md`.

**Adding HTML forms?**
Read `$netlify-forms` for form detection, AJAX submissions, spam filtering, and file uploads.

**Configuring netlify.toml (redirects, headers, build settings)?**
Read `$netlify-config` for the complete configuration reference.

**Deploying, managing env vars, or running local dev?**
Read `$netlify-cli-and-deploy` for CLI commands, Git vs manual deploys, and environment variable management.

**Setting up a framework (Vite, Astro, TanStack, Next.js)?**
Read `$netlify-frameworks` for adapter/plugin setup. Framework-specific details are in `$netlify-frameworks`.

**Controlling CDN caching behavior?**
Read `$netlify-caching` for cache headers, stale-while-revalidate, cache tags, and purge.

**Adding AI capabilities or choosing an AI model?**
Read `$netlify-ai-gateway` for AI Gateway setup, supported models, and provider SDKs.

**Adding user authentication, signups, logins, or access control?**
Read `$netlify-identity` for Netlify Identity setup, OAuth, role-based access, and protecting routes and functions.

**Deploying a site to Netlify?**
Read `$netlify-deploy` for the full deployment workflow — authentication, site linking, preview and production deploys.

## General Rules

- Use `Netlify.env.get("VAR")` for environment variables in functions (not `process.env`)
- Never hardcode secrets — use Netlify environment variables
- Add `.netlify` to `.gitignore`
- For framework-specific patterns, check the framework reference before writing custom Netlify Functions — the adapter may handle it


================================================
FILE: codex\skills\netlify-ai-gateway\SKILL.md
================================================
---
name: netlify-ai-gateway
description: Guide for using Netlify AI Gateway to access AI models. Use when adding AI capabilities or selecting/changing AI models. Must be read before choosing a model. Covers supported providers (OpenAI, Anthropic, Google), SDK setup, environment variables, and the list of available models.
---

# Netlify AI Gateway

> **IMPORTANT:** Only use models listed in the "Available Models" section below. AI Gateway does not support every model a provider offers. Using an unsupported model will cause runtime errors.

Netlify AI Gateway provides access to AI models from multiple providers without managing API keys directly. It is available on all Netlify sites.

## How It Works

The AI Gateway acts as a proxy — you use standard provider SDKs (OpenAI, Anthropic, Google) but point them at Netlify's gateway URL instead of the provider's API. Netlify handles authentication, rate limiting, and monitoring.

## Setup

1. Enable AI on your site in the Netlify UI
2. The environment variable `OPENAI_BASE_URL` is set automatically by Netlify
3. Install the provider SDK you want to use

No provider API keys are needed — Netlify's gateway handles authentication.

## Using OpenAI SDK

```bash
npm install openai
```

```typescript
import OpenAI from "openai";

const openai = new OpenAI();
// OPENAI_BASE_URL is auto-configured — no API key or base URL needed

const completion = await openai.chat.completions.create({
  model: "gpt-4o-mini",
  messages: [{ role: "user", content: "Hello!" }],
});
```

## Using Anthropic SDK

```bash
npm install @anthropic-ai/sdk
```

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  baseURL: Netlify.env.get("ANTHROPIC_BASE_URL"),
});

const message = await client.messages.create({
  model: "claude-sonnet-4-5-20250929",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello!" }],
});
```

## Using Google AI SDK

```bash
npm install @google/generative-ai
```

```typescript
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("placeholder");
// Configure base URL via environment variable

const model = genAI.getGenerativeModel({ model: "gemini-2.5-flash" });
const result = await model.generateContent("Hello!");
```

## In a Netlify Function

```typescript
import type { Config, Context } from "@netlify/functions";
import OpenAI from "openai";

export default async (req: Request, context: Context) => {
  const { prompt } = await req.json();
  const openai = new OpenAI();

  const completion = await openai.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [{ role: "user", content: prompt }],
  });

  return Response.json({
    response: completion.choices[0].message.content,
  });
};

export const config: Config = {
  path: "/api/ai",
  method: "POST",
};
```

## Environment Variables

| Variable | Provider | Set by |
|---|---|---|
| `OPENAI_BASE_URL` | OpenAI | Netlify (automatic) |
| `ANTHROPIC_BASE_URL` | Anthropic | Netlify (automatic) |

These are configured automatically when AI is enabled on the site. No manual setup required.

## Local Development

With `@netlify/vite-plugin` or `netlify dev`, gateway environment variables are injected automatically. The AI Gateway is accessible during local development after the site has been deployed at least once.

## Available Models

For the list of supported models, see https://docs.netlify.com/build/ai-gateway/overview/.


================================================
FILE: codex\skills\netlify-blobs\SKILL.md
================================================
---
name: netlify-blobs
description: Guide for using Netlify Blobs object storage. Use when storing files, images, documents, or simple key-value data without a full database. Covers getStore(), CRUD operations, metadata, listing, deploy-scoped vs site-scoped stores, and local development.
---

# Netlify Blobs

Netlify Blobs is zero-config object storage available from any Netlify compute (functions, edge functions, framework server routes). No provisioning required.

```bash
npm install @netlify/blobs
```

## Getting a Store

```typescript
import { getStore } from "@netlify/blobs";

const store = getStore({ name: "my-store" });

// Use "strong" consistency when you need immediate reads after writes
const store = getStore({ name: "my-store", consistency: "strong" });
```

## CRUD Operations

These are the **only** store methods. Do not invent others.

### Create / Update

```typescript
// String or binary data
await store.set("key", "value");
await store.set("key", fileBuffer);

// With metadata
await store.set("key", data, {
  metadata: { contentType: "image/png", uploadedAt: new Date().toISOString() },
});

// JSON data
await store.setJSON("key", { name: "Example", count: 42 });
```

### Read

```typescript
// Text (default)
const text = await store.get("key");                    // string | null

// Typed retrieval
const json = await store.get("key", { type: "json" });  // object | null
const stream = await store.get("key", { type: "stream" });
const blob = await store.get("key", { type: "blob" });
const buffer = await store.get("key", { type: "arrayBuffer" });

// With metadata
const result = await store.getWithMetadata("key");
// { data: any, etag: string, metadata: object } | null

// Metadata only (no data download)
const meta = await store.getMetadata("key");
// { etag: string, metadata: object } | null
```

### Delete

```typescript
await store.delete("key");
```

### List

```typescript
const { blobs } = await store.list();
// blobs: [{ etag: string, key: string }, ...]

// Filter by prefix
const { blobs } = await store.list({ prefix: "uploads/" });
```

## Store Types

- **Site-scoped** (`getStore()`): Persist across all deploys. Use for most cases.
- **Deploy-scoped** (`getDeployStore()`): Tied to a specific deploy lifecycle.

## Limits

| Limit | Value |
|---|---|
| Max object size | 5 GB |
| Store name max length | 64 bytes |
| Key max length | 600 bytes |

## Local Development

Local dev uses a sandboxed store (separate from production). For Vite-based projects, install `@netlify/vite-plugin` to enable local Blobs access. Otherwise, use `netlify dev`.

**Common error**: "The environment has not been configured to use Netlify Blobs" — install `@netlify/vite-plugin` or run via `netlify dev`.


================================================
FILE: codex\skills\netlify-caching\SKILL.md
================================================
---
name: netlify-caching
description: Guide for controlling caching on Netlify's CDN. Use when configuring cache headers, setting up stale-while-revalidate, implementing on-demand cache purge, or understanding Netlify's CDN caching behavior. Covers Cache-Control, Netlify-CDN-Cache-Control, cache tags, durable cache, and framework-specific caching patterns.
---

# Caching on Netlify

## Default Behavior

**Static assets** are cached automatically:
- CDN: cached for 1 year, invalidated on every deploy
- Browser: always revalidates (`max-age=0, must-revalidate`)
- No configuration needed

**Dynamic responses** (functions, edge functions, proxied) are **not cached by default**. Add cache headers explicitly.

## Cache-Control Headers

Three headers control caching, from most to least specific:

| Header | Who sees it | Use case |
|---|---|---|
| `Netlify-CDN-Cache-Control` | Netlify CDN only (stripped before browser) | CDN-only caching |
| `CDN-Cache-Control` | All CDN caches (stripped before browser) | Multi-CDN setups |
| `Cache-Control` | Browser and all caches | General caching |

### Common Patterns

```typescript
// Cache at CDN for 1 hour, browser always revalidates
return new Response(body, {
  headers: {
    "Netlify-CDN-Cache-Control": "public, s-maxage=3600, must-revalidate",
    "Cache-Control": "public, max-age=0, must-revalidate",
  },
});

// Stale-while-revalidate (serve stale for 2 min while refreshing)
return new Response(body, {
  headers: {
    "Netlify-CDN-Cache-Control": "public, max-age=60, stale-while-revalidate=120",
  },
});

// Durable cache (shared across edge nodes, serverless functions only)
return new Response(body, {
  headers: {
    "Netlify-CDN-Cache-Control": "public, durable, max-age=60, stale-while-revalidate=120",
  },
});
```

### Immutable Assets

For fingerprinted files (hash in filename):

```toml
# netlify.toml
[[headers]]
for = "/assets/*"
[headers.values]
Cache-Control = "public, max-age=31536000, immutable"
```

## Cache Tags and On-Demand Purge

Tag responses for selective cache invalidation:

```typescript
return new Response(body, {
  headers: {
    "Netlify-Cache-ID": "product,listing",
    "Netlify-CDN-Cache-Control": "public, s-maxage=86400",
  },
});
```

Purge by tag:

```typescript
import { purgeCache } from "@netlify/functions";

export default async () => {
  await purgeCache({ tags: ["product"] });
  return new Response("Purged", { status: 202 });
};
```

Purge entire site:

```typescript
await purgeCache();
```

Responses with `Netlify-Cache-ID` are **excluded from automatic deploy-based invalidation** — they must be purged explicitly.

## Cache Key Variation

Customize what creates separate cache entries:

```typescript
return new Response(body, {
  headers: {
    "Netlify-Vary": "cookie=ab_test|is_logged_in",
    // Other options: query=param1|param2, header=X-Custom, country=us|de, language=en|fr
  },
});
```

## Framework-Specific Caching

### Next.js
ISR uses Netlify's durable cache automatically (runtime 5.5.0+). `revalidatePath` and `revalidateTag` trigger cache purge.

### Astro / Remix
Full control over cache headers in server routes. Set `Netlify-CDN-Cache-Control` in responses for CDN caching.

### Nuxt
Default Nitro preset handles caching. ISR-style patterns use `routeRules` with `swr` or `isr` options.

### Vite SPA
Static assets are cached by default. API responses from Netlify Functions need explicit cache headers.

## Debugging

Check the `Cache-Status` response header:
- `HIT` — served from cache
- `MISS` — generated fresh
- `REVALIDATED` — stale content was revalidated

## Constraints

- Basic auth disables caching for the entire site
- Durable cache is serverless functions only (not edge functions)
- Same URL must return identical `Netlify-Vary` headers across responses
- Deploy invalidation is scoped to deploy context (production vs preview)


================================================
FILE: codex\skills\netlify-cli-and-deploy\SKILL.md
================================================
---
name: netlify-cli-and-deploy
description: Guide for using the Netlify CLI and deploying sites. Use when installing the CLI, linking sites, deploying (Git-based or manual), managing environment variables, or running local development. Covers netlify dev, netlify deploy, Git vs non-Git workflows, and environment variable management.
---

# Netlify CLI and Deployment

## Installation

```bash
npm install -g netlify-cli    # Global (for local dev)
npm install netlify-cli -D    # Local (for CI)
```

Requires Node.js 18.14.0+.

## Authentication

```bash
netlify login       # Opens browser for OAuth
netlify status      # Check auth + linked site status
```

For CI, set `NETLIFY_AUTH_TOKEN` environment variable instead.

## Linking a Site

Check if already linked with `netlify status`. If not:

```bash
# Interactive
netlify link

# By Git remote (if using Git)
netlify link --git-remote-url https://github.com/org/repo

# Create new site
netlify init           # With Git CI/CD setup
netlify init --manual  # Without Git CI/CD
```

Site ID is stored in `.netlify/state.json`. Add `.netlify` to `.gitignore`.

## Deploying

### Git-Based Deploys (Continuous Deployment)

Set up with `netlify init`. Automatic deploys trigger on push/PR:
- Push to production branch → production deploy
- Open PR → deploy preview with unique URL
- Push to other branches → branch deploy

Build runs on Netlify's servers. Configure build settings in `netlify.toml`.

### Manual / Local Deploys (No Git Required)

Build locally, then upload:

```bash
netlify deploy          # Draft deploy (preview URL)
netlify deploy --prod   # Production deploy
netlify deploy --dir=dist  # Specify output directory
```

This works without Git — useful for prototypes, local-only projects, or CI pipelines.

## Local Development

### Option 1: netlify dev

```bash
netlify dev
```

Wraps your framework's dev server and provides:
- Environment variable injection
- Functions and edge functions
- Redirects and headers processing

### Option 2: Netlify Vite Plugin (Vite-based projects)

For projects using Vite (React SPA, TanStack Start, SvelteKit, Remix), the Vite plugin provides Netlify platform primitives directly in the framework's dev server:

```bash
npm install @netlify/vite-plugin
```

```typescript
// vite.config.ts
import netlify from "@netlify/vite-plugin";
export default defineConfig({ plugins: [netlify()] });
```

Then run your normal dev command (`npm run dev`) — no `netlify dev` wrapper needed. This gives you access to Blobs, DB, Functions, and environment variables during development.

See the **netlify-frameworks** skill for framework-specific local dev guidance.

## Environment Variables

### CLI Management

```bash
# Set
netlify env:set API_KEY "value"
netlify env:set API_KEY "value" --secret              # Hidden from logs
netlify env:set API_KEY "value" --context production   # Context-specific

# Get
netlify env:get API_KEY

# List
netlify env:list
netlify env:list --plain > .env                        # Export to file

# Import from file
netlify env:import .env

# Delete
netlify env:unset API_KEY
```

### Context Scoping

Variables can be scoped to deploy contexts:

```bash
netlify env:set API_URL "https://api.prod.com" --context production
netlify env:set API_URL "https://api.staging.com" --context deploy-preview
netlify env:set DEBUG "true" --context branch:feature-x
```

### Accessing in Code

- **Server-side (Functions)**: Use `Netlify.env.get("VAR")` (preferred) or `process.env.VAR`
- **Client-side (Vite)**: Only `VITE_`-prefixed vars via `import.meta.env.VITE_VAR`
- **Client-side (Astro)**: Only `PUBLIC_`-prefixed vars via `import.meta.env.PUBLIC_VAR`

**Never use `VITE_` or `PUBLIC_` prefix for secrets** — these are exposed to the browser.

## Useful Commands

| Command | Description |
|---|---|
| `netlify status` | Auth and site link status |
| `netlify dev` | Start local dev server |
| `netlify build` | Run build locally (mimics Netlify environment) |
| `netlify deploy` | Draft deploy |
| `netlify deploy --prod` | Production deploy |
| `netlify dev:exec <cmd>` | Run command with Netlify environment loaded |
| `netlify env:list` | List environment variables |
| `netlify clone org/repo` | Clone, link, and set up in one step |


================================================
FILE: codex\skills\netlify-config\SKILL.md
================================================
---
name: netlify-config
description: Reference for netlify.toml configuration. Use when configuring build settings, redirects, rewrites, headers, deploy contexts, environment variables, or any site-level configuration. Covers the complete netlify.toml syntax including redirects with splats/conditions, headers, deploy contexts, functions config, and edge functions config.
---

# Netlify Configuration (netlify.toml)

Place `netlify.toml` at the repository root (or at the base directory for monorepos).

## Build Settings

```toml
[build]
  base = "project/"          # Base directory (default: root)
  command = "npm run build"  # Build command
  publish = "dist/"          # Output directory
```

## Redirects

```toml
# Basic redirect
[[redirects]]
from = "/old"
to = "/new"
status = 301              # 301 (default), 302, 200 (rewrite), 404

# SPA catch-all
[[redirects]]
from = "/*"
to = "/index.html"
status = 200

# Splat (wildcard)
[[redirects]]
from = "/blog/*"
to = "/news/:splat"

# Path parameters
[[redirects]]
from = "/users/:id"
to = "/api/users/:id"
status = 200

# Force (override existing files)
[[redirects]]
from = "/app/*"
to = "/index.html"
status = 200
force = true

# Proxy to external service
[[redirects]]
from = "/api/*"
to = "https://api.example.com/:splat"
status = 200
[redirects.headers]
  X-Custom = "value"

# Country/language conditions
[[redirects]]
from = "/*"
to = "/fr/:splat"
status = 200
conditions = { Country = ["FR"], Language = ["fr"] }
```

**Rule order matters** — Netlify processes the first matching rule. Place specific rules before general ones.

## Headers

```toml
[[headers]]
for = "/*"
[headers.values]
  X-Frame-Options = "DENY"
  X-Content-Type-Options = "nosniff"

[[headers]]
for = "/assets/*"
[headers.values]
  Cache-Control = "public, max-age=31536000, immutable"
```

Headers apply only to files served from Netlify's CDN (not to function or edge function responses — set those in code).

## Deploy Contexts

Override settings per deploy context:

```toml
[context.production]
command = "npm run build"
environment = { NODE_ENV = "production" }

[context.deploy-preview]
command = "npm run build:preview"

[context.branch-deploy]
command = "npm run build:staging"

[context.dev]
environment = { NODE_ENV = "development" }

# Specific branch
[context."staging"]
command = "npm run build:staging"
```

## Environment Variables

```toml
[build.environment]
NODE_VERSION = "20"

[context.production.environment]
API_URL = "https://api.prod.com"

[context.deploy-preview.environment]
API_URL = "https://api.staging.com"
```

**Do not put secrets in netlify.toml** (it's committed to source control). Use the Netlify UI or CLI for sensitive values. See the **netlify-cli-and-deploy** skill for CLI environment variable management.

## Functions Configuration

```toml
[functions]
directory = "netlify/functions"   # Default
node_bundler = "esbuild"

# Scheduled function
[functions."cleanup"]
schedule = "@daily"
```

## Edge Functions Configuration

```toml
[[edge_functions]]
path = "/admin"
function = "auth"

# Import map for Deno URL imports
[functions]
deno_import_map = "./import_map.json"
```

## Dev Server

```toml
[dev]
command = "npm start"       # Dev server command
port = 8888                 # Netlify Dev port
targetPort = 3000           # Your app's dev server port
framework = "#auto"         # "#auto", "#static", "#custom"
```

## Plugins

```toml
[[plugins]]
package = "@netlify/plugin-lighthouse"
[plugins.inputs]
  audits = ["performance", "accessibility"]
```

## Image CDN

```toml
[images]
remote_images = ["https://example\\.com/.*"]
```

See the **netlify-image-cdn** skill for full Image CDN usage.


================================================
FILE: codex\skills\netlify-db\SKILL.md
================================================
---
name: netlify-db
description: Guide for using Netlify DB (managed Neon Postgres). Use when the project needs a relational database, structured data storage, SQL queries, or data that will grow over time. Covers provisioning, raw SQL via @netlify/neon, Drizzle ORM integration, migrations, and deploy preview branching. Also covers when to use Netlify Blobs instead.
---

# Netlify DB

Netlify DB provisions a managed Neon Postgres database automatically. No Neon account required.

## When to Use DB vs Blobs

**Use Netlify DB when:**
- Storing structured, relational data
- Data will grow over time
- Need queries, filtering, joins, or aggregations

**Use Netlify Blobs instead when:**
- Storing files (images, documents, exports)
- A handful of records with no growth expectation
- Simple key-value storage with no relational needs
- Want zero dependencies beyond `@netlify/blobs`

See the **netlify-blobs** skill for Blobs usage.

## Setup

```bash
npm install @netlify/neon
netlify db init    # Provisions database and sets up Drizzle ORM
```

Prerequisites: logged into Netlify CLI and site linked (`netlify link`).

## Raw SQL via @netlify/neon

`@netlify/neon` wraps `@neondatabase/serverless`. No connection string needed — it auto-configures.

```typescript
import { neon } from "@netlify/neon";
const sql = neon();

const users = await sql("SELECT * FROM users");
await sql("INSERT INTO users (name) VALUES ($1)", ["Jane"]);
await sql("UPDATE users SET name = $1 WHERE id = $2", ["Jane", 1]);
await sql("DELETE FROM users WHERE id = $1", [1]);
```

## Drizzle ORM Integration

For most projects, use Drizzle ORM on top of Netlify DB.

### drizzle.config.ts

```typescript
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  dbCredentials: { url: process.env.NETLIFY_DATABASE_URL! },
  schema: "./db/schema.ts",
  out: "./migrations",
  migrations: { prefix: "timestamp" }, // Avoids conflicts across branches
});
```

### db/index.ts

```typescript
import { neon } from "@neondatabase/serverless";
import { drizzle } from "drizzle-orm/neon-http";
import * as schema from "./schema";

const sql = neon(process.env.NETLIFY_DATABASE_URL!);
export const db = drizzle(sql, { schema });
export * from "./schema";
```

### Schema Example

```typescript
// db/schema.ts
import { integer, pgTable, varchar, text, boolean, timestamp } from "drizzle-orm/pg-core";

export const items = pgTable("items", {
  id: integer().primaryKey().generatedAlwaysAsIdentity(),
  title: varchar({ length: 255 }).notNull(),
  description: text(),
  isActive: boolean("is_active").notNull().default(true),
  createdAt: timestamp("created_at").defaultNow(),
  updatedAt: timestamp("updated_at").defaultNow(),
});

export type Item = typeof items.$inferSelect;
export type NewItem = typeof items.$inferInsert;
```

### Query Patterns

```typescript
import { db, items } from "../db";
import { eq } from "drizzle-orm";

const all = await db.select().from(items);
const [one] = await db.select().from(items).where(eq(items.id, id)).limit(1);
const [created] = await db.insert(items).values({ title: "New" }).returning();
const [updated] = await db.update(items).set({ title: "Updated" }).where(eq(items.id, id)).returning();
await db.delete(items).where(eq(items.id, id));
```

## Migrations

```json
{
  "scripts": {
    "db:generate": "drizzle-kit generate",
    "db:migrate": "netlify dev:exec drizzle-kit migrate",
    "db:push": "netlify dev:exec drizzle-kit push",
    "db:studio": "netlify dev:exec drizzle-kit studio"
  }
}
```

Workflow: modify schema, run `db:generate`, then `db:migrate`.

## Deploy Preview Branching

Netlify DB supports branching — production branch gets the production database, all other branches and deploy previews get a separate preview branch. Develop and test migrations on preview, merge to main, then apply to production.

## Environment Variables

- `NETLIFY_DATABASE_URL` — Auto-set by Netlify when database is provisioned
- Retrieve manually: `netlify env:get NETLIFY_DATABASE_URL`

## Local Development

Run `netlify dev` or use `@netlify/vite-plugin` to get database access locally. Use `netlify dev:exec` to run migration commands with the proper environment.


================================================
FILE: codex\skills\netlify-deploy\SKILL.md
================================================
---
name: netlify-deploy
description: Deploy web projects to Netlify using the Netlify CLI (`npx netlify`). Use when the user asks to deploy, host, publish, or link a site/repo on Netlify, including preview and production deploys.
---

# Netlify Deployment Skill

Deploy web projects to Netlify using the Netlify CLI with intelligent detection of project configuration and deployment context.

## Overview

This skill automates Netlify deployments by:
- Verifying Netlify CLI authentication
- Detecting project configuration and framework
- Linking to existing sites or creating new ones
- Deploying to production or preview environments

## Prerequisites

- **Netlify CLI**: Installed via npx (no global install required)
- **Authentication**: Netlify account with active login session
- **Project**: Valid web project in current directory
- **Network access**: Deployment requires outbound network calls. If sandboxing blocks these, the agent may need to request elevated permissions or prompt the user.
- **Timeouts**: Deployments can take a few minutes. Use appropriate timeout values for CLI commands.

## Authentication Pattern

The skill uses the **pre-authenticated Netlify CLI** approach:

1. Check authentication status with `npx netlify status`
2. If not authenticated, guide user through `npx netlify login`
3. Fail gracefully if authentication cannot be established

Authentication uses either:
- **Browser-based OAuth** (primary): `netlify login` opens browser for authentication
- **API Key** (alternative): Set `NETLIFY_AUTH_TOKEN` environment variable

## Workflow

### 1. Verify Netlify CLI Authentication

Check if the user is logged into Netlify:

```bash
npx netlify status
```

**Expected output patterns**:
- ✅ Authenticated: Shows logged-in user email and site link status
- ❌ Not authenticated: "Not logged into any site" or authentication error

**If not authenticated**, guide the user:

```bash
npx netlify login
```

This opens a browser window for OAuth authentication. Wait for user to complete login, then verify with `netlify status` again.

**Alternative: API Key authentication**

If browser authentication isn't available, users can set:

```bash
export NETLIFY_AUTH_TOKEN=your_token_here
```

Tokens can be generated at: https://app.netlify.com/user/applications#personal-access-tokens

### 2. Detect Site Link Status

From `netlify status` output, determine:
- **Linked**: Site already connected to Netlify (shows site name/URL)
- **Not linked**: Need to link or create site

### 3. Link to Existing Site or Create New

**If already linked** → Skip to step 4

**If not linked**, attempt to link by Git remote:

```bash
# Check if project is Git-based
git remote show origin

# If Git-based, extract remote URL
# Format: https://github.com/username/repo or git@github.com:username/repo.git

# Try to link by Git remote
npx netlify link --git-remote-url <REMOTE_URL>
```

**If link fails** (site doesn't exist on Netlify):

```bash
# Create new site interactively
npx netlify init
```

This guides user through:
1. Choosing team/account
2. Setting site name
3. Configuring build settings
4. Creating netlify.toml if needed

### 4. Verify Dependencies

Before deploying, ensure project dependencies are installed:

```bash
# For npm projects
npm install

# For other package managers, detect and use appropriate command
# yarn install, pnpm install, etc.
```

### 5. Deploy to Netlify

Choose deployment type based on context:

**Preview/Draft Deploy** (default for existing sites):

```bash
npx netlify deploy
```

This creates a deploy preview with a unique URL for testing.

**Production Deploy** (for new sites or explicit production deployments):

```bash
npx netlify deploy --prod
```

This deploys to the live production URL.

**Deployment process**:
1. CLI detects build settings (from netlify.toml or prompts user)
2. Builds the project locally
3. Uploads built assets to Netlify
4. Returns deployment URL

### 6. Report Results

After deployment, report to user:
- **Deploy URL**: Unique URL for this deployment
- **Site URL**: Production URL (if production deploy)
- **Deploy logs**: Link to Netlify dashboard for logs
- **Next steps**: Suggest `netlify open` to view site or dashboard

## Handling netlify.toml

If a `netlify.toml` file exists, the CLI uses it automatically. If not, the CLI will prompt for:
- **Build command**: e.g., `npm run build`, `next build`
- **Publish directory**: e.g., `dist`, `build`, `.next`

Common framework defaults:
- **Next.js**: build command `npm run build`, publish `.next`
- **React (Vite)**: build command `npm run build`, publish `dist`
- **Static HTML**: no build command, publish current directory

The skill should detect framework from `package.json` if possible and suggest appropriate settings.

## Example Full Workflow

```bash
# 1. Check authentication
npx netlify status

# If not authenticated:
npx netlify login

# 2. Link site (if needed)
# Try Git-based linking first
git remote show origin
npx net

================================================
FILE: codex\skills\netlify-deploy\references\cli-commands.md
================================================
# Netlify CLI Commands Reference

Quick reference for common Netlify CLI commands used in deployments.

## Authentication

```bash
# Login via browser OAuth
npx netlify login

# Check authentication status and site link
npx netlify status

# Logout
npx netlify logout
```

## Site Management

```bash
# Link current directory to existing site
npx netlify link

# Link by Git remote URL
npx netlify link --git-remote-url <url>

# Create and link new site
npx netlify init

# Unlink from current site
npx netlify unlink

# Open site in Netlify dashboard
npx netlify open

# Open site admin panel
npx netlify open:admin

# Open site in browser
npx netlify open:site
```

## Deployment

```bash
# Deploy preview/draft (safe for testing)
npx netlify deploy

# Deploy to production
npx netlify deploy --prod

# Deploy with specific directory
npx netlify deploy --dir=dist

# Deploy with message
npx netlify deploy --message="Deploy message"

# List all deploys
npx netlify deploy:list
```

## Development

```bash
# Run local dev server with Netlify features
npx netlify dev

# Run local dev server on specific port
npx netlify dev --port 3000
```

## Site Information

```bash
# Get site info
npx netlify sites:list

# Get current site info
npx netlify api getSite --data '{"site_id": "YOUR_SITE_ID"}'
```

## Environment Variables

```bash
# List environment variables
npx netlify env:list

# Set environment variable
npx netlify env:set KEY value

# Get environment variable value
npx netlify env:get KEY

# Import env vars from file
npx netlify env:import .env
```

## Build

```bash
# Show build settings
npx netlify build --dry

# Run build locally
npx netlify build
```

## Functions (Serverless)

```bash
# List functions
npx netlify functions:list

# Invoke function locally
npx netlify functions:invoke FUNCTION_NAME

# Create new function
npx netlify functions:create FUNCTION_NAME
```

## Logs

```bash
# Stream function logs
npx netlify logs

# View logs for specific function
npx netlify logs:function FUNCTION_NAME
```

## Troubleshooting Commands

```bash
# Check CLI version
npx netlify --version

# Get help for any command
npx netlify help [command]

# Check status with verbose output
npx netlify status --verbose
```

## Exit Codes

- `0` - Success
- `1` - General error
- `2` - Authentication error
- `3` - Site not found
- `4` - Build failed

## Common Flags

- `--json` - Output as JSON
- `--silent` - Suppress output
- `--debug` - Show debug information
- `--force` - Skip confirmation prompts

## Resources

- Full CLI documentation: https://docs.netlify.com/cli/get-started/
- CLI GitHub repository: https://github.com/netlify/cli


================================================
FILE: codex\skills\netlify-deploy\references\deployment-patterns.md
================================================
# Netlify Deployment Patterns

Common deployment scenarios and best practices for the Netlify skill.

## Deployment Decision Tree

```
Is user authenticated?
├─ No → Run `netlify login`
└─ Yes → Is site linked?
    ├─ No → Is it a Git repo?
    │   ├─ Yes → Try `netlify link --git-remote-url`
    │   │   ├─ Success → Continue to deploy
    │   │   └─ Fail → Run `netlify init`
    │   └─ No → Run `netlify init`
    └─ Yes → Is this first deploy or existing site?
        ├─ First deploy/new site → `netlify deploy --prod`
        └─ Existing site → `netlify deploy` (preview)
```

## Scenario 1: First-Time Deployment (New Project)

**Context**: User has a project that has never been deployed to Netlify.

**Steps**:
1. Check authentication: `npx netlify status`
2. If not authenticated: `npx netlify login`
3. Initialize new site: `npx netlify init`
   - This guides user through setup
   - Creates netlify.toml if needed
4. Install dependencies: `npm install`
5. Deploy to production: `npx netlify deploy --prod`

**Example**:
```bash
npx netlify status
# Not linked to a site

npx netlify login
# Opens browser for authentication

npx netlify init
# Walks through site creation

npm install
npx netlify deploy --prod
```

## Scenario 2: Linking Existing Git Repository to Existing Site

**Context**: User has a site already on Netlify and wants to link their local repo.

**Steps**:
1. Check authentication: `npx netlify status`
2. Get Git remote: `git remote show origin`
3. Extract URL (e.g., `https://github.com/user/repo.git`)
4. Link by remote: `npx netlify link --git-remote-url <URL>`
5. If found, linked. If not, run `netlify init`

**Example**:
```bash
git remote show origin
# * remote origin
#   Fetch URL: https://github.com/user/my-app.git

npx netlify link --git-remote-url https://github.com/user/my-app.git
# Site linked successfully
```

## Scenario 3: Preview Deployment (Testing Changes)

**Context**: User wants to test changes before pushing to production.

**Steps**:
1. Ensure site is linked: `npx netlify status`
2. Make code changes
3. Deploy preview: `npx netlify deploy`
4. Review preview URL
5. If approved, deploy to prod: `npx netlify deploy --prod`

**Example**:
```bash
# Make changes to code

npx netlify deploy
# Draft deploy URL: https://507f1f77bcf86cd799439011-my-app.netlify.app

# Test the preview, then:
npx netlify deploy --prod
```

## Scenario 4: Framework-Specific Deployments

### Next.js

```bash
# Next.js typically uses .next as output
npx netlify deploy --prod

# netlify.toml should have:
# [build]
#   command = "npm run build"
#   publish = ".next"
```

### React (Vite)

```bash
# Vite outputs to dist by default
npm run build
npx netlify deploy --dir=dist --prod

# netlify.toml:
# [build]
#   command = "npm run build"
#   publish = "dist"
```

### Static HTML

```bash
# No build step needed
npx netlify deploy --dir=. --prod
```

## Scenario 5: Monorepo Deployment

**Context**: Project is in a subdirectory of a monorepo.

**Steps**:
1. Navigate to project subdirectory: `cd packages/frontend`
2. Or set base in netlify.toml:
   ```toml
   [build]
     base = "packages/frontend"
     command = "npm run build"
     publish = "dist"
   ```
3. Deploy normally: `npx netlify deploy --prod`

## Scenario 6: Environment Variables

**Context**: Project needs secrets or environment-specific config.

**Steps**:
1. Never commit secrets to Git
2. Set in Netlify dashboard or CLI:
   ```bash
   npx netlify env:set API_KEY "secret_value"
   npx netlify env:set NODE_ENV "production"
   ```
3. Access in code: `process.env.API_KEY`
4. Deploy: `npx netlify deploy --prod`

## Scenario 7: Custom Domain Setup

**Context**: User wants to use a custom domain.

**Steps**:
1. Deploy site first: `npx netlify deploy --prod`
2. Add domain via dashboard or CLI:
   ```bash
   npx netlify open:admin
   # Navigate to Domain settings
   ```
3. Update DNS records as instructed by Netlify
4. Wait for DNS propagation (can take up to 48 hours)

## Best Practices

### 1. Always Preview First

```bash
# Deploy preview
npx netlify deploy

# Test thoroughly
# Then deploy to production
npx netlify deploy --prod
```

### 2. Use netlify.toml for Consistency

Create a `netlify.toml` file in your repo root:

```toml
[build]
  command = "npm run build"
  publish = "dist"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

This ensures consistent builds across all deployments.

### 3. Framework Detection

Let Netlify auto-detect when possible. Only specify build settings if:
- Netlify can't detect your framework
- You need custom build commands
- Your project has a non-standard structure

### 4. Dependency Installation

Always ensure dependencies are installed before deploying:

```bash
npm install  # or yarn install, pnpm install
npx netlify deploy
```

### 5. Build Locally First

Test builds locally before deploying:

```bash
npm run build
# Check that build output exists

npx netlify deploy --dir=dist
```

### 6. Use Deploy Me

================================================
FILE: codex\skills\netlify-deploy\references\netlify-toml.md
================================================
# netlify.toml Configuration Reference

Configuration file for Netlify builds and deployments.

## Basic Structure

```toml
[build]
  command = "npm run build"
  publish = "dist"
```

## Build Settings

### Common Configuration

```toml
[build]
  # Command to build your site
  command = "npm run build"

  # Directory to publish (relative to repo root)
  publish = "dist"

  # Functions directory
  functions = "netlify/functions"

  # Base directory (if not repo root)
  base = "packages/frontend"

  # Ignore builds for specific conditions
  ignore = "git diff --quiet HEAD^ HEAD package.json"
```

## Environment Variables

```toml
[build.environment]
  NODE_VERSION = "18"
  NPM_FLAGS = "--prefix=/dev/null"

[context.production.environment]
  NODE_ENV = "production"
```

## Framework Detection

Netlify auto-detects frameworks, but you can override:

### Next.js

```toml
[build]
  command = "npm run build"
  publish = ".next"
```

### React (Vite)

```toml
[build]
  command = "npm run build"
  publish = "dist"
```

### Vue

```toml
[build]
  command = "npm run build"
  publish = "dist"
```

### Astro

```toml
[build]
  command = "npm run build"
  publish = "dist"
```

### SvelteKit

```toml
[build]
  command = "npm run build"
  publish = "build"
```

## Redirects and Rewrites

```toml
[[redirects]]
  from = "/old-path"
  to = "/new-path"
  status = 301

[[redirects]]
  from = "/api/*"
  to = "https://api.example.com/:splat"
  status = 200

# SPA fallback (for client-side routing)
[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

## Headers

```toml
[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-XSS-Protection = "1; mode=block"
    Content-Security-Policy = "default-src 'self'"

[[headers]]
  for = "/assets/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"
```

## Context-Specific Configuration

Deploy different settings per context:

```toml
# Production
[context.production]
  command = "npm run build:prod"
  [context.production.environment]
    NODE_ENV = "production"

# Deploy previews
[context.deploy-preview]
  command = "npm run build:preview"

# Branch deploys
[context.branch-deploy]
  command = "npm run build:staging"

# Specific branch
[context.staging]
  command = "npm run build:staging"
```

## Functions Configuration

```toml
[functions]
  directory = "netlify/functions"
  node_bundler = "esbuild"

[[functions]]
  path = "/api/*"
  function = "api"
```

## Build Plugins

```toml
[[plugins]]
  package = "@netlify/plugin-lighthouse"

  [plugins.inputs]
    output_path = "reports/lighthouse.html"

[[plugins]]
  package = "netlify-plugin-submit-sitemap"

  [plugins.inputs]
    baseUrl = "https://example.com"
    sitemapPath = "/sitemap.xml"
```

## Edge Functions

```toml
[[edge_functions]]
  function = "geolocation"
  path = "/api/location"
```

## Processing

```toml
[build.processing]
  skip_processing = false

[build.processing.css]
  bundle = true
  minify = true

[build.processing.js]
  bundle = true
  minify = true

[build.processing.html]
  pretty_urls = true

[build.processing.images]
  compress = true
```

## Common Patterns

### Single Page Application (SPA)

```toml
[build]
  command = "npm run build"
  publish = "dist"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

### Monorepo with Base Directory

```toml
[build]
  base = "packages/web"
  command = "npm run build"
  publish = "dist"
```

### Multiple Redirects with Country-Based Routing

```toml
[[redirects]]
  from = "/"
  to = "/uk"
  status = 302
  conditions = {Country = ["GB"]}

[[redirects]]
  from = "/"
  to = "/us"
  status = 302
  conditions = {Country = ["US"]}
```

## Validation

Validate your netlify.toml:

```bash
npx netlify build --dry
```

## Resources

- Full configuration reference: https://docs.netlify.com/configure-builds/file-based-configuration/
- Framework-specific guides: https://docs.netlify.com/frameworks/


================================================
FILE: codex\skills\netlify-edge-functions\SKILL.md
================================================
---
name: netlify-edge-functions
description: Guide for writing Netlify Edge Functions. Use when building middleware, geolocation-based logic, request/response manipulation, authentication checks, A/B testing, or any low-latency edge compute. Covers Deno runtime, context.next() middleware pattern, geolocation, and when to choose edge vs serverless.
---

# Netlify Edge Functions

Edge functions run on Netlify's globally distributed edge network (Deno runtime), providing low-latency responses close to users.

## Syntax

```typescript
import type { Config, Context } from "@netlify/edge-functions";

export default async (req: Request, context: Context) => {
  return new Response("Hello from the edge!");
};

export const config: Config = {
  path: "/hello",
};
```

Place files in `netlify/edge-functions/`. Uses `.ts`, `.js`, `.tsx`, or `.jsx` extensions.

## Config Object

```typescript
export const config: Config = {
  path: "/api/*",                    // URLPattern path(s)
  excludedPath: "/api/public/*",     // Exclusions
  method: ["GET", "POST"],           // HTTP methods
  onError: "bypass",                 // "fail" (default), "bypass", or "/error-page"
  cache: "manual",                   // Enable response caching
};
```

## Middleware Pattern

Use `context.next()` to invoke the next handler in the chain and optionally modify the response:

```typescript
export default async (req: Request, context: Context) => {
  // Before: modify request or short-circuit
  if (!isAuthenticated(req)) {
    return new Response("Unauthorized", { status: 401 });
  }

  // Continue to origin/next function
  const response = await context.next();

  // After: modify response
  response.headers.set("x-custom-header", "value");
  return response;
};
```

Return `undefined` to pass through without modification:

```typescript
export default async (req: Request, context: Context) => {
  if (!shouldHandle(req)) return; // continues to next handler
  return new Response("Handled");
};
```

## Geolocation and IP

```typescript
export default async (req: Request, context: Context) => {
  const { city, country, subdivision, timezone } = context.geo;
  const ip = context.ip;

  if (country?.code === "DE") {
    return Response.redirect(new URL("/de", req.url));
  }
};
```

Local dev with mocked geo: `netlify dev --geo=mock --country=US`

## Environment Variables

Use `Netlify.env` (not `process.env` or `Deno.env`):

```typescript
const secret = Netlify.env.get("API_SECRET");
```

## Module Support

- **Node.js builtins**: `import { randomBytes } from "node:crypto";`
- **npm packages**: Install via npm and import by name
- **Deno modules**: URL imports (e.g., `import X from "https://esm.sh/package"`)

For URL imports, use an import map:

```json
// import_map.json
{ "imports": { "html-rewriter": "https://ghuc.cc/worker-tools/html-rewriter/index.ts" } }
```

```toml
# netlify.toml
[functions]
  deno_import_map = "./import_map.json"
```

## When to Use Edge vs Serverless

| Use Edge Functions for | Use Serverless Functions for |
|---|---|
| Low-latency responses | Long-running operations (up to 15 min) |
| Request/response manipulation | Complex Node.js dependencies |
| Geolocation-based logic | Database-heavy operations |
| Auth checks and redirects | Background/scheduled tasks |
| A/B testing, personalization | Tasks needing > 512 MB memory |

## Limits

| Resource | Limit |
|---|---|
| CPU time | 50 ms per request |
| Memory | 512 MB per deployed set |
| Response header timeout | 40 seconds |
| Code size | 20 MB compressed |


================================================
FILE: codex\skills\netlify-forms\SKILL.md
================================================
---
name: netlify-forms
description: Guide for using Netlify Forms for HTML form handling. Use when adding contact forms, feedback forms, file upload forms, or any form that should be collected by Netlify. Covers the data-netlify attribute, spam filtering, AJAX submissions, file uploads, notifications, and the submissions API.
---

# Netlify Forms

Netlify Forms collects HTML form submissions without server-side code. Form detection must be enabled in the Netlify UI (Forms section).

## Basic Setup

Add `data-netlify="true"` and a unique `name` to the form:

```html
<form name="contact" method="POST" data-netlify="true">
  <label>Name: <input type="text" name="name" /></label>
  <label>Email: <input type="email" name="email" /></label>
  <label>Message: <textarea name="message"></textarea></label>
  <button type="submit">Send</button>
</form>
```

Netlify's build system detects the form and injects a hidden `form-name` input automatically. For a custom success page, add `action="/thank-you"` to the form tag. Use paths without `.html` extension — Netlify serves `thank-you.html` at `/thank-you` by default, and the `.html` path returns 404.

## JavaScript-Rendered Forms (React, Vue, SSR Frameworks)

For forms rendered by JavaScript frameworks (React, Vue, TanStack Start, Next.js, SvelteKit, Remix, Nuxt), Netlify's build parser cannot detect the form in static HTML. You MUST create a static HTML skeleton file for build-time form detection:

Create a static HTML file in `public/` (e.g. `public/__forms.html`) containing a hidden copy of each form:

```html
<!DOCTYPE html>
<html>
  <body>
    <form name="contact" data-netlify="true" netlify-honeypot="bot-field" hidden>
      <input type="hidden" name="form-name" value="contact" />
      <input type="text" name="name" />
      <input type="email" name="email" />
      <textarea name="message"></textarea>
      <input name="bot-field" />
    </form>
  </body>
</html>
```

**Rules:**
- The form `name` must exactly match the `form-name` value used in your component's fetch call
- Include every field your component submits — Netlify validates field names against the registered form
- Without this file, Netlify cannot detect the form and submissions will silently fail

Your component must also include a hidden `form-name` input:

```jsx
<form name="contact" method="POST" data-netlify="true">
  <input type="hidden" name="form-name" value="contact" />
  {/* ... fields ... */}
</form>
```

## AJAX Submissions

### Vanilla JavaScript

```javascript
const form = document.querySelector("form");
form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const formData = new FormData(form);
  await fetch("/", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams(formData).toString(),
  });
});
```

> **SSR frameworks (TanStack Start, Next.js, SvelteKit, Remix, Nuxt):** The `fetch` URL must target the static skeleton
> file path (e.g. `"/__forms.html"`), **not** `"/"`. In SSR apps, `fetch("/")` is intercepted by the SSR catch-all
> function and never reaches Netlify's form processing middleware. See the React example and troubleshooting section below.

### React Example

```tsx
function ContactForm() {
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);
    // For SSR apps, use the skeleton file path instead of "/" (e.g. "/__forms.html")
    const response = await fetch("/__forms.html", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams(formData as any).toString(),
    });
    if (response.ok) {
      // Show success feedback
    }
  };

  return (
    <form name="contact" method="POST" data-netlify="true" onSubmit={handleSubmit}>
      <input type="hidden" name="form-name" value="contact" />
      <input type="text" name="name" placeholder="Name" />
      <input type="email" name="email" placeholder="Email" />
      <textarea name="message" placeholder="Message" />
      <button type="submit">Send</button>
    </form>
  );
}
```

> **SSR troubleshooting:** If form submissions appear to succeed (200 response) but nothing shows in the Netlify Forms
> UI, the POST is likely being intercepted by the SSR function. Ensure `fetch` targets the skeleton file path (e.g.
> `"/__forms.html"`), not `"/"`. The skeleton file path routes through the CDN origin where Netlify's form handler runs.

## Spam Filtering

Netlify uses Akismet automatically. Add a honeypot field for extra protection:

```html
<form name="contact" method="POST" netlify-honeypot="bot-field" data-netlify="true">
  <p style="display:none">
    <label>Don't fill this out: <input name="bot-field" /></label>
  </p>
  <!-- visible fields -->
</form>
```

For reCAPTCHA, add `data-netlify-recaptcha="true"` to the form and include `<div data-netlify-recaptcha="true"></div>` where t

================================================
FILE: codex\skills\netlify-frameworks\SKILL.md
================================================
---
name: netlify-frameworks
description: Guide for deploying web frameworks on Netlify. Use when setting up a framework project (Vite/React, Astro, TanStack Start, Next.js, Nuxt, SvelteKit, Remix) for Netlify deployment, configuring adapters or plugins, or troubleshooting framework-specific Netlify integration. Covers what Netlify needs from each framework and how adapters handle server-side rendering.
---

# Frameworks on Netlify

Netlify supports any framework that produces static output. For frameworks with server-side capabilities (SSR, API routes, middleware), an adapter or plugin translates the framework's server-side code into Netlify Functions and Edge Functions automatically.

## How It Works

During build, the framework adapter writes files to `.netlify/v1/` — functions, edge functions, redirects, and configuration. Netlify reads these to deploy the site. You do not need to write Netlify Functions manually when using a framework adapter for server-side features.

## Detecting Your Framework

Check these files to determine the framework:

| File | Framework |
|---|---|
| `astro.config.*` | Astro |
| `next.config.*` | Next.js |
| `nuxt.config.*` | Nuxt |
| `vite.config.*` + `react-router` | Vite + React (SPA or Remix) |
| `app.config.*` + `@tanstack/react-start` | TanStack Start |
| `svelte.config.*` | SvelteKit |

## Framework Reference Guides

Each framework has specific adapter/plugin requirements and local dev patterns:


## General Patterns

### Client-Side Routing (SPA)

For single-page apps with client-side routing, add a catch-all redirect:

```toml
# netlify.toml
[[redirects]]
from = "/*"
to = "/index.html"
status = 200
```

### Custom 404 Pages

- **Static sites**: Create a `404.html` in your publish directory. Netlify serves it automatically for unmatched routes.
- **SSR frameworks**: Handle 404s in the framework's routing (the adapter maps this to Netlify's function routing).

### Environment Variables in Frameworks

Each framework exposes environment variables to client-side code differently:

| Framework | Client prefix | Access pattern |
|---|---|---|
| Vite / React | `VITE_` | `import.meta.env.VITE_VAR` |
| Astro | `PUBLIC_` | `import.meta.env.PUBLIC_VAR` |
| Next.js | `NEXT_PUBLIC_` | `process.env.NEXT_PUBLIC_VAR` |
| Nuxt | `NUXT_PUBLIC_` | `useRuntimeConfig().public.var` |

Server-side code in all frameworks can access variables via `process.env.VAR` or `Netlify.env.get("VAR")`.


================================================
FILE: codex\skills\netlify-frameworks\references\astro.md
================================================
# Astro on Netlify

## Setup

Install the Netlify adapter:

```bash
npx astro add netlify
```

This installs `@astrojs/netlify` and updates `astro.config.*` automatically.

### Manual Setup

```bash
npm install @astrojs/netlify
```

```typescript
// astro.config.mjs
import { defineConfig } from "astro/config";
import netlify from "@astrojs/netlify";

export default defineConfig({
  output: "server",  // or "hybrid" for mixed static/SSR
  adapter: netlify(),
});
```

## Output Modes

| Mode | Behavior |
|---|---|
| `"static"` | Fully pre-rendered at build time (no adapter needed) |
| `"server"` | All pages rendered on request (SSR) |
| `"hybrid"` | Static by default, opt-in to SSR per page with `export const prerender = false` |

## What the Adapter Does

- Converts Astro server routes into Netlify Functions
- Handles SSR, API routes, and middleware
- Maps Astro's routing to Netlify's function routing
- You do **not** write raw Netlify Functions for Astro's server routes

## API Routes

Astro API routes (in `src/pages/api/`) are handled by the adapter:

```typescript
// src/pages/api/items.ts
import type { APIRoute } from "astro";

export const GET: APIRoute = async () => {
  return new Response(JSON.stringify({ items: [] }), {
    headers: { "Content-Type": "application/json" },
  });
};

export const POST: APIRoute = async ({ request }) => {
  const data = await request.json();
  return new Response(JSON.stringify({ created: data }), { status: 201 });
};
```

## Forms (HTML Pattern)

Astro renders HTML server-side, so Netlify can detect forms directly:

```astro
---
// src/pages/contact.astro
---
<form name="contact" method="POST" data-netlify="true">
  <label>Name: <input type="text" name="name" /></label>
  <label>Email: <input type="email" name="email" /></label>
  <label>Message: <textarea name="message"></textarea></label>
  <button type="submit">Send</button>
</form>
```

For form submissions that should redirect back with feedback, handle the POST in an API route and redirect:

```typescript
// src/pages/api/contact.ts
export const POST: APIRoute = async ({ request, redirect }) => {
  const formData = await request.formData();
  // Process form...
  return redirect("/contact?success=true");
};
```

## Custom 404

Create `src/pages/404.astro`. Astro handles this automatically.

## Local Development

**Option A: Astro dev server** (simpler, but no Netlify primitives):

```bash
npm run dev    # astro dev
```

**Option B: netlify dev** (full Netlify environment including functions, env vars):

```bash
netlify dev
```

The Astro adapter's local dev experience with `netlify dev` varies — for Blobs and DB access, `netlify dev` is recommended. If using `@netlify/vite-plugin` alongside Astro, local platform primitives may also be available via the standard dev server, but this integration is less mature than with pure Vite projects.

## Build and Deploy

```toml
# netlify.toml
[build]
command = "astro build"
publish = "dist"
```

The adapter configures the publish directory and function routing automatically.


================================================
FILE: codex\skills\netlify-frameworks\references\nextjs.md
================================================
# Next.js on Netlify

## Setup

Next.js on Netlify uses the `@netlify/next` runtime, which is installed automatically. No manual adapter installation is required — Netlify detects Next.js and configures the build automatically.

```toml
# netlify.toml
[build]
command = "next build"
publish = ".next"
```

## What the Runtime Does

- Converts Next.js server-side features (SSR, API routes, middleware, ISR) into Netlify Functions and Edge Functions
- Handles image optimization via Netlify Image CDN
- Maps Next.js routing to Netlify's infrastructure
- Supports App Router and Pages Router

## Key Configuration

### next.config.js

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [
      { protocol: "https", hostname: "example.com" },
    ],
  },
};

module.exports = nextConfig;
```

Remote image patterns in `next.config.js` are automatically mapped to Netlify Image CDN's `remote_images` configuration.

## API Routes

Next.js API routes work automatically — they are deployed as Netlify Functions:

```typescript
// app/api/items/route.ts (App Router)
export async function GET() {
  return Response.json({ items: [] });
}

export async function POST(request: Request) {
  const data = await request.json();
  return Response.json({ created: data }, { status: 201 });
}
```

## Middleware

Next.js middleware is deployed as a Netlify Edge Function:

```typescript
// middleware.ts
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

export function middleware(request: NextRequest) {
  // Runs at the edge on Netlify
  return NextResponse.next();
}
```

## ISR (Incremental Static Regeneration)

ISR works on Netlify. Pages with `revalidate` are cached and revalidated using Netlify's CDN cache with `stale-while-revalidate`. On-demand revalidation via `revalidatePath` and `revalidateTag` triggers Netlify cache purge.

## Local Development

```bash
npm run dev    # next dev — standard Next.js dev server
```

For Netlify-specific features (environment variables, edge middleware testing), use:

```bash
netlify dev
```

## Known Patterns

- **Static export** (`output: "export"`): Works without the runtime — produces a fully static site
- **Standalone mode** is not required; the Netlify runtime handles deployment automatically
- Environment variables use the `NEXT_PUBLIC_` prefix for client-side access


================================================
FILE: codex\skills\netlify-frameworks\references\tanstack.md
================================================
# TanStack Start on Netlify

## Setup

TanStack Start uses the Netlify Vite plugin for deployment.

```bash
npm install @netlify/vite-plugin
```

```typescript
// app.config.ts
import { defineConfig } from "@tanstack/react-start/config";
import netlify from "@netlify/vite-plugin";

export default defineConfig({
  vite: {
    plugins: [netlify()],
  },
});
```

## What the Plugin Does

- Handles SSR output for Netlify Functions
- Enables Netlify platform primitives (Blobs, DB, env vars) in local dev
- Maps TanStack Start's file-based routing to Netlify's infrastructure

## Server Functions

TanStack Start uses `createServerFn` for server-side logic. These are automatically handled by the Netlify Vite plugin — no raw Netlify Functions needed:

```typescript
import { createServerFn } from "@tanstack/react-start";

const getItems = createServerFn({ method: "GET" }).handler(async () => {
  // Server-side code — runs as Netlify Function in production
  const items = await db.select().from(itemsTable);
  return items;
});
```

## Local Development

```bash
npm run dev    # Uses Vite plugin — Netlify primitives available
```

The Vite plugin provides Functions, Blobs, DB, and environment variables during local dev without needing `netlify dev`.

## Build and Deploy

```toml
# netlify.toml
[build]
command = "npm run build"
publish = ".output/public"
```

The Vite plugin configures the output structure for Netlify automatically.


================================================
FILE: codex\skills\netlify-frameworks\references\vite.md
================================================
# Vite + React on Netlify

## Setup

Install the Netlify Vite plugin:

```bash
npm install @netlify/vite-plugin
```

```typescript
// vite.config.ts
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import netlify from "@netlify/vite-plugin";

export default defineConfig({
  plugins: [react(), netlify()],
});
```

## What the Plugin Does

- Enables Netlify Functions, Blobs, DB, and environment variables in local dev
- Handles build output for Netlify deployment
- No need for `netlify dev` — run `npm run dev` directly

## SPA Routing

For client-side routing (React Router, etc.), add the catch-all redirect:

```toml
# netlify.toml
[[redirects]]
from = "/*"
to = "/index.html"
status = 200
```

## Netlify Functions

Write functions in `netlify/functions/` as usual. The Vite plugin makes them available during local dev at their configured paths.

```typescript
// netlify/functions/api.ts
import type { Config, Context } from "@netlify/functions";

export default async (req: Request, context: Context) => {
  return Response.json({ message: "Hello from API" });
};

export const config: Config = { path: "/api/hello" };
```

## Forms (AJAX Pattern)

Since Vite + React renders forms client-side, include a hidden HTML form for Netlify to detect, and submit via AJAX:

```tsx
// In your React component
function ContactForm() {
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);
    await fetch("/", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams(formData as any).toString(),
    });
  };

  return (
    <form name="contact" method="POST" data-netlify="true" onSubmit={handleSubmit}>
      <input type="hidden" name="form-name" value="contact" />
      {/* fields */}
    </form>
  );
}
```

Also add a hidden form in `index.html`:

```html
<form name="contact" netlify hidden>
  <input type="text" name="name" />
  <input type="email" name="email" />
  <textarea name="message"></textarea>
</form>
```

## Local Dev

```bash
npm run dev   # Uses Vite plugin — Netlify primitives available
```

No `netlify dev` wrapper needed. Functions, Blobs, DB, and environment variables all work.

## Build and Deploy

```toml
# netlify.toml
[build]
command = "npm run build"
publish = "dist"
```


================================================
FILE: codex\skills\netlify-functions\SKILL.md
================================================
---
name: netlify-functions
description: Guide for writing Netlify serverless functions. Use when creating API endpoints, background processing, scheduled tasks, or any server-side logic using Netlify Functions. Covers modern syntax (default export + Config), TypeScript, path routing, background functions, scheduled functions, streaming, and method routing.
---

# Netlify Functions

## Modern Syntax

Always use the modern default export + Config pattern. Never use the legacy `exports.handler` or named `handler` export.

```typescript
import type { Context, Config } from "@netlify/functions";

export default async (req: Request, context: Context) => {
  return new Response("Hello, world!");
};

export const config: Config = {
  path: "/api/hello",
};
```

The handler receives a standard Web API `Request` and returns a `Response`. The second argument is a Netlify `Context` object.

## File Structure

Place functions in `netlify/functions/`:

```
netlify/functions/
  _shared/           # Non-function shared code (underscore prefix)
    auth.ts
    db.ts
  items.ts           # -> /.netlify/functions/items (or custom path via config)
  users/index.ts     # -> /.netlify/functions/users
```

Use `.ts` or `.mts` extensions. If both `.ts` and `.js` exist with the same name, the `.js` file takes precedence.

## Path Routing

Define custom paths via the `config` export:

```typescript
export const config: Config = {
  path: "/api/items",                    // Static path
  // path: "/api/items/:id",            // Path parameter
  // path: ["/api/items", "/api/items/:id"], // Multiple paths
  // excludedPath: "/api/items/special", // Excluded paths
  // preferStatic: true,                // Don't override static files
};
```

Without a `path` config, functions are available at `/.netlify/functions/{name}`. Setting a `path` makes the function available **only** at that path.

Access path parameters via `context.params`:

```typescript
// config: { path: "/api/items/:id" }
export default async (req: Request, context: Context) => {
  const { id } = context.params;
  // ...
};
```

## Method Routing

```typescript
export default async (req: Request, context: Context) => {
  switch (req.method) {
    case "GET":    return handleGet(context.params.id);
    case "POST":   return handlePost(await req.json());
    case "DELETE": return handleDelete(context.params.id);
    default:       return new Response("Method not allowed", { status: 405 });
  }
};

export const config: Config = {
  path: "/api/items/:id",
  method: ["GET", "POST", "DELETE"],
};
```

## Background Functions

For long-running tasks (up to 15 minutes). The client receives an immediate `202` response; return values are ignored.

Name the file with a `-background` suffix:

```
netlify/functions/process-background.ts
```

Store results externally (Netlify Blobs, database) for later retrieval.

## Scheduled Functions

Run on a cron schedule (UTC timezone):

```typescript
export default async (req: Request) => {
  const { next_run } = await req.json();
  console.log("Next invocation at:", next_run);
};

export const config: Config = {
  schedule: "@hourly", // or cron: "0 * * * *"
};
```

Shortcuts: `@yearly`, `@monthly`, `@weekly`, `@daily`, `@hourly`. Scheduled functions have a **30-second timeout** and only run on published deploys.

## Streaming Responses

Return a `ReadableStream` body for streamed responses (up to 20 MB):

```typescript
export default async (req: Request) => {
  const stream = new ReadableStream({ /* ... */ });
  return new Response(stream, {
    headers: { "Content-Type": "text/event-stream" },
  });
};
```

## Context Object

| Property | Description |
|---|---|
| `context.params` | Path parameters from config |
| `context.geo` | `{ city, country: {code, name}, latitude, longitude, subdivision, timezone, postalCode }` |
| `context.ip` | Client IP address |
| `context.cookies` | `.get()`, `.set()`, `.delete()` |
| `context.deploy` | `{ context, id, published }` |
| `context.site` | `{ id, name, url }` |
| `context.account.id` | Team account ID |
| `context.requestId` | Unique request ID |
| `context.waitUntil(promise)` | Extend execution after response is sent |

## Environment Variables

Use `Netlify.env` (not `process.env`) inside functions:

```typescript
const apiKey = Netlify.env.get("API_KEY");
```

## Resource Limits

| Resource | Limit |
|---|---|
| Synchronous timeout | 60 seconds |
| Background timeout | 15 minutes |
| Scheduled timeout | 30 seconds |
| Memory | 1024 MB |
| Buffered payload | 6 MB |
| Streamed payload | 20 MB |

## Framework Considerations

Frameworks with server-side capabilities (Astro, Next.js, Nuxt, SvelteKit, TanStack Start) typically generate their own serverless functions via adapters. You usually do not write raw Netlify Functions in these projects — the framework adapter handles server-side rendering and API routes. Write Netlify Functions directly when:

- Using a client-side-only framework (Vite + React

================================================
FILE: codex\skills\netlify-identity\SKILL.md
================================================
---
name: netlify-identity
description: Use when the task involves authentication, user signups, logins, password recovery, OAuth providers, role-based access control, or protecting routes and functions. Always use `@netlify/identity`. Never use `netlify-identity-widget` or `gotrue-js` — they are deprecated.
---

# Netlify Identity

Netlify Identity is a user management service for signups, logins, password recovery, user metadata, and role-based access control. It is built on [GoTrue](https://github.com/netlify/gotrue) and issues JSON Web Tokens (JWTs).

**Always use `@netlify/identity`.** Never use `netlify-identity-widget` or `gotrue-js` — they are deprecated. `@netlify/identity` provides a unified, headless TypeScript API that works in both browser and server contexts (Netlify Functions, Edge Functions, SSR frameworks).

## Setup

```bash
npm install @netlify/identity
```

Identity is automatically enabled when a deploy created by a Netlify Agent Runner session includes Identity code. Otherwise, it must be manually enabled in the UI. These are the default settings:

- **Registration** — Open (anyone can sign up). Change to Invite only in **Project configuration > Identity** if needed.
- **Autoconfirm** — Off (new signups require email confirmation). Enable in **Project configuration > Identity** to skip confirmation during development.

### Local Development

Identity does **not** currently work with `netlify dev`. You must deploy to Netlify to test Identity features. Use `npx netlify deploy` for preview deploys during development. This limitation may be resolved in a future release.

## Quick Start

Log in from the browser:

```typescript
import { login, getUser } from '@netlify/identity'

const user = await login('user@example.com', '<password>')
console.log(`Hello, ${user.name}`)

// Later, check auth state
const currentUser = await getUser()
```

Protect a Netlify Function:

```typescript
// netlify/functions/protected.mts
import { getUser } from '@netlify/identity'
import type { Context } from '@netlify/functions'

export default async (req: Request, context: Context) => {
  const user = await getUser()
  if (!user) return new Response('Unauthorized', { status: 401 })
  return Response.json({ id: user.id, email: user.email })
}
```

## Core API

Import and use headless functions directly:

```typescript
import {
  getUser,
  handleAuthCallback,
  login,
  logout,
  signup,
  oauthLogin,
  onAuthChange,
  getSettings,
} from '@netlify/identity'
```

### Login

```typescript
import { login, AuthError } from '@netlify/identity'

async function handleLogin(email: string, password: string) {
  try {
    const user = await login(email, password)
    showSuccess(`Welcome back, ${user.name ?? user.email}`)
  } catch (error) {
    if (error instanceof AuthError) {
      showError(error.status === 401 ? 'Invalid email or password.' : error.message)
    }
  }
}
```

### Signup

After signup, check `user.emailVerified` to determine if the user was auto-confirmed or needs to confirm their email.

```typescript
import { signup, AuthError } from '@netlify/identity'

async function handleSignup(email: string, password: string, name: string) {
  try {
    const user = await signup(email, password, { full_name: name })
    if (user.emailVerified) {
      // Autoconfirm ON — user is logged in immediately
      showSuccess('Account created. You are now logged in.')
    } else {
      // Autoconfirm OFF — confirmation email sent
      showSuccess('Check your email to confirm your account.')
    }
  } catch (error) {
    if (error instanceof AuthError) {
      showError(error.status === 403 ? 'Signups are not allowed.' : error.message)
    }
  }
}
```

### Logout

```typescript
import { logout } from '@netlify/identity'

await logout()
```

### OAuth

OAuth is a two-step flow: `oauthLogin(provider)` redirects away from the site, then `handleAuthCallback()` processes the redirect when the user returns.

```typescript
import { oauthLogin } from '@netlify/identity'

// Step 1: Redirect to provider (navigates away — never returns)
function handleOAuthClick(provider: 'google' | 'github' | 'gitlab' | 'bitbucket') {
  oauthLogin(provider)
}
```

Enable providers in **Project configuration > Identity > External providers** before using OAuth.

### Handling Callbacks

Always call `handleAuthCallback()` on page load in any app that uses OAuth, password recovery, invites, or email confirmation. It processes all callback types via the URL hash.

```typescript
import { handleAuthCallback, AuthError } from '@netlify/identity'

async function processCallback() {
  try {
    const result = await handleAuthCallback()
    if (!result) return // No callback hash — normal page load

    switch (result.type) {
      case 'oauth':
        showSuccess(`Logged in as ${result.user?.email}`)
        break
      case 'confirmation':
        showSuccess('Email confirmed. You are now logged in.')
        break
      case 'recovery':
        // User

================================================
FILE: codex\skills\netlify-identity\references\advanced-patterns.md
================================================
# Advanced Identity Patterns

## Password Recovery

Three-step flow: request recovery email, handle the callback, then set a new password.

```typescript
import { requestPasswordRecovery, handleAuthCallback, updateUser, AuthError } from '@netlify/identity'

// Step 1: Send recovery email
async function handleForgotPassword(email: string) {
  try {
    await requestPasswordRecovery(email)
    showSuccess('Check your email for a password reset link.')
  } catch (error) {
    if (error instanceof AuthError) showError(error.message)
  }
}

// Step 2: handleAuthCallback() returns { type: 'recovery', user } — show password reset form
// (See the handleAuthCallback switch in SKILL.md)

// Step 3: Set new password
async function handlePasswordReset(newPassword: string) {
  try {
    await updateUser({ password: newPassword })
    showSuccess('Password updated.')
  } catch (error) {
    if (error instanceof AuthError) showError(error.message)
  }
}
```

The recovery callback fires a `'recovery'` auth event, not `'login'`. The user is authenticated but should be prompted to set a new password before navigating away.

## Invite Acceptance

When a user clicks an invite link, `handleAuthCallback()` returns `{ type: 'invite', user: null, token }`. Use the token to accept the invite and set a password.

```typescript
import { acceptInvite, AuthError } from '@netlify/identity'

async function handleAcceptInvite(token: string, password: string) {
  try {
    const user = await acceptInvite(token, password)
    showSuccess(`Welcome, ${user.email}! Your account is ready.`)
  } catch (error) {
    if (error instanceof AuthError) showError(error.message)
  }
}
```

## Email Change

When a user verifies an email change, `handleAuthCallback()` returns `{ type: 'email_change', user }`. The user must be logged in when clicking the verification link.

```typescript
import { verifyEmailChange, AuthError } from '@netlify/identity'

async function handleEmailChangeVerification(token: string) {
  try {
    const user = await verifyEmailChange(token)
    showSuccess(`Email updated to ${user.email}`)
  } catch (error) {
    if (error instanceof AuthError) showError(error.message)
  }
}
```

## Session Hydration

`hydrateSession()` bridges server-set cookies to the browser session. Call it on page load when using server-side login (e.g., login inside a Netlify Function followed by a redirect).

```typescript
import { hydrateSession } from '@netlify/identity'

const user = await hydrateSession()
if (user) {
  // Browser session is now in sync with server-set cookies
}
```

`getUser()` auto-hydrates from the `nf_jwt` cookie if no browser session exists, so explicit `hydrateSession()` is only needed when you want to restore the full session (including token refresh timers) after a server-side login.

## SSR Integration Patterns

For SSR frameworks, the recommended pattern is:

- **Browser-side** for auth mutations: `login()`, `signup()`, `logout()`, `oauthLogin()`
- **Server-side** for reading auth state: `getUser()`, `getSettings()`, `getIdentityConfig()`

Browser-side auth mutations set the `nf_jwt` cookie and localStorage, and emit `onAuthChange` events. The server reads the cookie on the next request.

The library also supports server-side mutations (`login()`, `signup()`, `logout()` inside Netlify Functions), but these require the Netlify Functions runtime to set cookies. After a server-side mutation, use a full page navigation so the browser sends the new cookie.

Always use `window.location.href` (not framework router navigation) after server-side auth mutations in Next.js, TanStack Start, and SvelteKit. Remix `redirect()` is safe because Remix actions return real HTTP responses.

## Full API Reference

For the complete API reference — all function signatures, type definitions, OAuth helpers, admin operations, session management, auth events, and framework-specific examples — read the package README:

```
node_modules/@netlify/identity/README.md
```

The README is shipped with the npm package and is always in sync with the installed version.


================================================
FILE: codex\skills\netlify-image-cdn\SKILL.md
================================================
---
name: netlify-image-cdn
description: Guide for using Netlify Image CDN for image optimization and transformation. Use when serving optimized images, creating responsive image markup, setting up user-uploaded image pipelines, or configuring image transformations. Covers the /.netlify/images endpoint, query parameters, remote image allowlisting, clean URL rewrites, and composing uploads with Functions + Blobs.
---

# Netlify Image CDN

Every Netlify site has a built-in `/.netlify/images` endpoint for on-the-fly image transformation. No configuration required for local images.

## Basic Usage

```html
<img src="/.netlify/images?url=/photo.jpg&w=800&h=600&fit=cover&q=80" />
```

## Query Parameters

| Param | Description | Values |
|---|---|---|
| `url` | Source image path (required) | Relative path or absolute URL |
| `w` | Width in pixels | Any positive integer |
| `h` | Height in pixels | Any positive integer |
| `fit` | Resize behavior | `contain` (default), `cover`, `fill` |
| `position` | Crop alignment (with `cover`) | `center` (default), `top`, `bottom`, `left`, `right` |
| `fm` | Output format | `avif`, `webp`, `jpg`, `png`, `gif`, `blurhash` |
| `q` | Quality (lossy formats) | 1-100 (default: 75) |

When `fm` is omitted, Netlify auto-negotiates the best format based on browser support (preferring `webp`, then `avif`).

## Remote Image Allowlisting

External images must be explicitly allowed in `netlify.toml`:

```toml
[images]
remote_images = ["https://example\\.com/.*", "https://cdn\\.images\\.com/.*"]
```

Values are regex patterns.

## Clean URL Rewrites

Create user-friendly image URLs with redirects:

```toml
# Basic optimization
[[redirects]]
from = "/img/*"
to = "/.netlify/images?url=/:splat"
status = 200

# Preset: thumbnail
[[redirects]]
from = "/img/thumb/:key"
to = "/.netlify/images?url=/uploads/:key&w=150&h=150&fit=cover"
status = 200

# Preset: hero
[[redirects]]
from = "/img/hero/:key"
to = "/.netlify/images?url=/uploads/:key&w=1200&h=675&fit=cover"
status = 200
```

## Caching

- Transformed images are cached at the CDN edge automatically
- Cache invalidates on new deploys
- Set cache headers on source images to control caching:

```toml
[[headers]]
for = "/uploads/*"
[headers.values]
Cache-Control = "public, max-age=31536000, immutable"
```

## User-Uploaded Images

Combine **Netlify Functions** (upload handler) + **Netlify Blobs** (storage) + **Image CDN** (serving/transforming) to build a complete user-uploaded image pipeline. See references/user-uploads.md for the full pattern.


================================================
FILE: codex\skills\netlify-image-cdn\references\user-uploads.md
================================================
# User-Uploaded Images Pipeline

Compose Netlify Functions (upload handler) + Netlify Blobs (storage) + Image CDN (serving/transforming) to build a complete user-uploaded image pipeline.

## Architecture

1. **Upload** — A Netlify Function receives multipart form data, validates, and stores in Blobs
2. **Storage** — Netlify Blobs stores the binary image with metadata
3. **Serve** — A Netlify Function retrieves the blob and serves it at `/uploads/:key`
4. **Transform** — A redirect maps `/img/:key` to `/.netlify/images?url=/uploads/:key` for CDN optimization

## Dependencies

```bash
npm install @netlify/blobs
```

## Upload Handler

```typescript
// netlify/functions/upload.ts
import type { Context, Config } from "@netlify/functions";
import { getStore } from "@netlify/blobs";
import { randomUUID } from "crypto";

const ALLOWED_TYPES = ["image/jpeg", "image/png", "image/gif", "image/webp"];
const MAX_SIZE = 4 * 1024 * 1024; // 4 MB

export default async (req: Request, context: Context) => {
  if (req.method !== "POST") {
    return new Response("Method not allowed", { status: 405 });
  }

  const formData = await req.formData();
  const image = formData.get("image") as File;

  if (!image) return Response.json({ error: "No image provided" }, { status: 400 });
  if (!ALLOWED_TYPES.includes(image.type)) return Response.json({ error: "Invalid type" }, { status: 400 });
  if (image.size > MAX_SIZE) return Response.json({ error: "File too large" }, { status: 400 });

  const extension = image.name.split(".").pop() || "jpg";
  const key = `${randomUUID()}.${extension}`;
  const store = getStore({ name: "images", consistency: "strong" });

  await store.set(key, image, {
    metadata: {
      contentType: image.type,
      originalFilename: image.name,
      uploadedAt: new Date().toISOString(),
    },
  });

  return Response.json({ success: true, key, url: `/img/${key}` });
};

export const config: Config = { path: "/api/upload", method: "POST" };
```

## Serve Handler

```typescript
// netlify/functions/serve-image.ts
import type { Context, Config } from "@netlify/functions";
import { getStore } from "@netlify/blobs";

export default async (req: Request, context: Context) => {
  const key = context.params.key;
  const store = getStore({ name: "images", consistency: "strong" });

  const result = await store.getWithMetadata(key, { type: "stream" });
  if (!result) return new Response("Not found", { status: 404 });

  return new Response(result.data, {
    headers: {
      "Content-Type": result.metadata?.contentType || "image/jpeg",
      "Cache-Control": "public, max-age=31536000, immutable",
    },
  });
};

export const config: Config = { path: "/uploads/:key" };
```

## CDN Redirect

```toml
# netlify.toml

# Basic optimized URL
[[redirects]]
from = "/img/:key"
to = "/.netlify/images?url=/uploads/:key"
status = 200

# Thumbnail preset
[[redirects]]
from = "/img/thumb/:key"
to = "/.netlify/images?url=/uploads/:key&w=150&h=150&fit=cover"
status = 200

# Hero preset
[[redirects]]
from = "/img/hero/:key"
to = "/.netlify/images?url=/uploads/:key&w=1200&h=675&fit=cover"
status = 200
```

## Client-Side Upload (React Example)

```tsx
function ImageUpload({ onUpload }: { onUpload: (url: string) => void }) {
  const handleChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("image", file);

    const res = await fetch("/api/upload", { method: "POST", body: formData });
    const { url } = await res.json();
    onUpload(url);
  };

  return <input type="file" accept="image/*" onChange={handleChange} />;
}
```

## Astro Upload (API Route)

```typescript
// src/pages/api/upload.ts
import type { APIRoute } from "astro";
import { getStore } from "@netlify/blobs";
import { randomUUID } from "crypto";

export const POST: APIRoute = async ({ request, redirect }) => {
  const formData = await request.formData();
  const image = formData.get("image") as File;
  if (!image) return new Response("No image", { status: 400 });

  const key = `${randomUUID()}.${image.name.split(".").pop() || "jpg"}`;
  const store = getStore({ name: "images", consistency: "strong" });
  await store.set(key, image, {
    metadata: { contentType: image.type, originalFilename: image.name },
  });

  return redirect(`/gallery?uploaded=${key}`);
};
```

## Key Points

- Always validate file type and size on the server (client validation can be bypassed)
- Use `strong` consistency on Blobs for immediate reads after writes
- The serve handler's `Cache-Control: immutable` means the CDN caches the raw image permanently — Image CDN transformations layer on top
- Without `fm` parameter, Netlify auto-serves AVIF or WebP based on browser support


================================================
FILE: context\steering\netlify-deployment-power\POWER.md
================================================
---
name: "netlify-deployment"
displayName: "Netlify Deployment"
description: "Deploy and manage websites on Netlify using CLI-first workflow with netlify.toml configuration"
keywords: ["netlify", "deploy", "hosting", "cli", "deployment", "web", "static-site"]
author: "Netlify"
---

Netlify Deployment (CLI-First)
==============================

> Use this file whenever you are asked to deploy or update a site on Netlify. **Default behavior:** prefer the Netlify CLI

1\. Defaults & Principles
-------------------------

*   Prefer **Netlify CLI** as the primary deployment method.
*   Use a netlify.toml file for consistent build and publish configuration.
*   Never hardcode secrets; always use **Netlify environment variables**.
*   For framework-specific details, reference official Netlify docs (via llms.txt) rather than inventing new patterns.

2\. netlify.toml Basics
-----------------------

```
[build]
  command = "BUILD_COMMAND"
  publish = "PUBLISH_DIRECTORY"
```

*   Adjust publish to match the actual output directory.
*   Use SPA redirect only for client-side routed apps.
*   Do not include secrets.
    

3\. Deploy with Netlify CLI (Preferred)
---------------------------------------

### Install & Authenticate

```
npm install -g netlify-cli

# will tell you linked status and user status
netlify status

#only if the user is not logged in
netlify login 
```

### Link or Create a Site

Determine if the site is linked to an existing Netlify account with `netlify status`

Skip this step if it is already linked.

If not already linked:
1. determine if it is git based
   1.a. if it is git based, use `git remote show origin` to find the git remote url like "https://github.com/orgname/reponame"
   1.b. see if the site already exists on their account with `netlify link --git-remote-url REMOTE_URL`
   1.c. if the site is not found then we must create it.
2. if site is unknown, create a new site use `netlify init` and let the user walk through the steps


### Dependencies

Confirm that all dependencies have been installed. (e.g. `npm install`)

### Deploy

If the user created a new site, then do a production deploy. If this is linking an existing site, we must create a preview/non-production deploy unless the user expclitly asked for this.

non-production deploy:
`netlify deploy`

production deploy:
`netlify deploy --prod`

    
4\. Troubleshooting Basics
--------------------------

*   Check Netlify build logs for errors.
*   Confirm correct build command and publish directory.
*   Verify required environment variables exist.


================================================
FILE: skills\CLAUDE.md
================================================
# Netlify Skills

This project deploys on Netlify. Use these skills for guidance on Netlify platform primitives. Each skill provides specific, factual reference for working with a Netlify feature.

## When to Use Each Skill

**Building API endpoints or server-side logic?**
Read `netlify-functions/SKILL.md` for modern function syntax, routing, background/scheduled functions.

**Need low-latency middleware, geo-based logic, or request manipulation?**
Read `netlify-edge-functions/SKILL.md` for edge compute patterns.

**Storing files, images, or simple key-value data?**
Read `netlify-blobs/SKILL.md` for object storage API.

**Need a relational database?**
Read `netlify-db/SKILL.md` for Neon Postgres setup, Drizzle ORM, and migrations. It also covers when Blobs is a better fit.

**Optimizing or transforming images?**
Read `netlify-image-cdn/SKILL.md` for the image transformation endpoint and clean URL patterns. For user-uploaded images, see `netlify-image-cdn/references/user-uploads.md`.

**Adding HTML forms?**
Read `netlify-forms/SKILL.md` for form detection, AJAX submissions, spam filtering, and file uploads.

**Configuring netlify.toml (redirects, headers, build settings)?**
Read `netlify-config/SKILL.md` for the complete configuration reference.

**Deploying, managing env vars, or running local dev?**
Read `netlify-cli-and-deploy/SKILL.md` for CLI commands, Git vs manual deploys, and environment variable management.

**Setting up a framework (Vite, Astro, TanStack, Next.js)?**
Read `netlify-frameworks/SKILL.md` for adapter/plugin setup. Framework-specific details are in `netlify-frameworks/references/`.

**Controlling CDN caching behavior?**
Read `netlify-caching/SKILL.md` for cache headers, stale-while-revalidate, cache tags, and purge.

**Adding AI capabilities or choosing an AI model?**
Read `netlify-ai-gateway/SKILL.md` for AI Gateway setup, supported models, and provider SDKs.

**Adding user authentication, signups, logins, or access control?**
Read `netlify-identity/SKILL.md` for Netlify Identity setup, OAuth, role-based access, and protecting routes and functions.

**Deploying a site to Netlify?**
Read `netlify-deploy/SKILL.md` for the full deployment workflow — authentication, site linking, preview and production deploys.

## General Rules

- Use `Netlify.env.get("VAR")` for environment variables in functions (not `process.env`)
- Never hardcode secrets — use Netlify environment variables
- Add `.netlify` to `.gitignore`
- For framework-specific patterns, check the framework reference before writing custom Netlify Functions — the adapter may handle it


================================================
FILE: skills\netlify-ai-gateway\SKILL.md
================================================
---
name: netlify-ai-gateway
description: Guide for using Netlify AI Gateway to access AI models. Use when adding AI capabilities or selecting/changing AI models. Must be read before choosing a model. Covers supported providers (OpenAI, Anthropic, Google), SDK setup, environment variables, and the list of available models.
---

# Netlify AI Gateway

> **IMPORTANT:** Only use models listed in the "Available Models" section below. AI Gateway does not support every model a provider offers. Using an unsupported model will cause runtime errors.

Netlify AI Gateway provides access to AI models from multiple providers without managing API keys directly. It is available on all Netlify sites.

## How It Works

The AI Gateway acts as a proxy — you use standard provider SDKs (OpenAI, Anthropic, Google) but point them at Netlify's gateway URL instead of the provider's API. Netlify handles authentication, rate limiting, and monitoring.

## Setup

1. Enable AI on your site in the Netlify UI
2. The environment variable `OPENAI_BASE_URL` is set automatically by Netlify
3. Install the provider SDK you want to use

No provider API keys are needed — Netlify's gateway handles authentication.

## Using OpenAI SDK

```bash
npm install openai
```

```typescript
import OpenAI from "openai";

const openai = new OpenAI();
// OPENAI_BASE_URL is auto-configured — no API key or base URL needed

const completion = await openai.chat.completions.create({
  model: "gpt-4o-mini",
  messages: [{ role: "user", content: "Hello!" }],
});
```

## Using Anthropic SDK

```bash
npm install @anthropic-ai/sdk
```

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  baseURL: Netlify.env.get("ANTHROPIC_BASE_URL"),
});

const message = await client.messages.create({
  model: "claude-sonnet-4-5-20250929",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello!" }],
});
```

## Using Google AI SDK

```bash
npm install @google/generative-ai
```

```typescript
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("placeholder");
// Configure base URL via environment variable

const model = genAI.getGenerativeModel({ model: "gemini-2.5-flash" });
const result = await model.generateContent("Hello!");
```

## In a Netlify Function

```typescript
import type { Config, Context } from "@netlify/functions";
import OpenAI from "openai";

export default async (req: Request, context: Context) => {
  const { prompt } = await req.json();
  const openai = new OpenAI();

  const completion = await openai.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [{ role: "user", content: prompt }],
  });

  return Response.json({
    response: completion.choices[0].message.content,
  });
};

export const config: Config = {
  path: "/api/ai",
  method: "POST",
};
```

## Environment Variables

| Variable | Provider | Set by |
|---|---|---|
| `OPENAI_BASE_URL` | OpenAI | Netlify (automatic) |
| `ANTHROPIC_BASE_URL` | Anthropic | Netlify (automatic) |

These are configured automatically when AI is enabled on the site. No manual setup required.

## Local Development

With `@netlify/vite-plugin` or `netlify dev`, gateway environment variables are injected automatically. The AI Gateway is accessible during local development after the site has been deployed at least once.

## Available Models

For the list of supported models, see https://docs.netlify.com/build/ai-gateway/overview/.


================================================
FILE: skills\netlify-blobs\SKILL.md
================================================
---
name: netlify-blobs
description: Guide for using Netlify Blobs object storage. Use when storing files, images, documents, or simple key-value data without a full database. Covers getStore(), CRUD operations, metadata, listing, deploy-scoped vs site-scoped stores, and local development.
---

# Netlify Blobs

Netlify Blobs is zero-config object storage available from any Netlify compute (functions, edge functions, framework server routes). No provisioning required.

```bash
npm install @netlify/blobs
```

## Getting a Store

```typescript
import { getStore } from "@netlify/blobs";

const store = getStore({ name: "my-store" });

// Use "strong" consistency when you need immediate reads after writes
const store = getStore({ name: "my-store", consistency: "strong" });
```

## CRUD Operations

These are the **only** store methods. Do not invent others.

### Create / Update

```typescript
// String or binary data
await store.set("key", "value");
await store.set("key", fileBuffer);

// With metadata
await store.set("key", data, {
  metadata: { contentType: "image/png", uploadedAt: new Date().toISOString() },
});

// JSON data
await store.setJSON("key", { name: "Example", count: 42 });
```

### Read

```typescript
// Text (default)
const text = await store.get("key");                    // string | null

// Typed retrieval
const json = await store.get("key", { type: "json" });  // object | null
const stream = await store.get("key", { type: "stream" });
const blob = await store.get("key", { type: "blob" });
const buffer = await store.get("key", { type: "arrayBuffer" });

// With metadata
const result = await store.getWithMetadata("key");
// { data: any, etag: string, metadata: object } | null

// Metadata only (no data download)
const meta = await store.getMetadata("key");
// { etag: string, metadata: object } | null
```

### Delete

```typescript
await store.delete("key");
```

### List

```typescript
const { blobs } = await store.list();
// blobs: [{ etag: string, key: string }, ...]

// Filter by prefix
const { blobs } = await store.list({ prefix: "uploads/" });
```

## Store Types

- **Site-scoped** (`getStore()`): Persist across all deploys. Use for most cases.
- **Deploy-scoped** (`getDeployStore()`): Tied to a specific deploy lifecycle.

## Limits

| Limit | Value |
|---|---|
| Max object size | 5 GB |
| Store name max length | 64 bytes |
| Key max length | 600 bytes |

## Local Development

Local dev uses a sandboxed store (separate from production). For Vite-based projects, install `@netlify/vite-plugin` to enable local Blobs access. Otherwise, use `netlify dev`.

**Common error**: "The environment has not been configured to use Netlify Blobs" — install `@netlify/vite-plugin` or run via `netlify dev`.


================================================
FILE: skills\netlify-caching\SKILL.md
================================================
---
name: netlify-caching
description: Guide for controlling caching on Netlify's CDN. Use when configuring cache headers, setting up stale-while-revalidate, implementing on-demand cache purge, or understanding Netlify's CDN caching behavior. Covers Cache-Control, Netlify-CDN-Cache-Control, cache tags, durable cache, and framework-specific caching patterns.
---

# Caching on Netlify

## Default Behavior

**Static assets** are cached automatically:
- CDN: cached for 1 year, invalidated on every deploy
- Browser: always revalidates (`max-age=0, must-revalidate`)
- No configuration needed

**Dynamic responses** (functions, edge functions, proxied) are **not cached by default**. Add cache headers explicitly.

## Cache-Control Headers

Three headers control caching, from most to least specific:

| Header | Who sees it | Use case |
|---|---|---|
| `Netlify-CDN-Cache-Control` | Netlify CDN only (stripped before browser) | CDN-only caching |
| `CDN-Cache-Control` | All CDN caches (stripped before browser) | Multi-CDN setups |
| `Cache-Control` | Browser and all caches | General caching |

### Common Patterns

```typescript
// Cache at CDN for 1 hour, browser always revalidates
return new Response(body, {
  headers: {
    "Netlify-CDN-Cache-Control": "public, s-maxage=3600, must-revalidate",
    "Cache-Control": "public, max-age=0, must-revalidate",
  },
});

// Stale-while-revalidate (serve stale for 2 min while refreshing)
return new Response(body, {
  headers: {
    "Netlify-CDN-Cache-Control": "public, max-age=60, stale-while-revalidate=120",
  },
});

// Durable cache (shared across edge nodes, serverless functions only)
return new Response(body, {
  headers: {
    "Netlify-CDN-Cache-Control": "public, durable, max-age=60, stale-while-revalidate=120",
  },
});
```

### Immutable Assets

For fingerprinted files (hash in filename):

```toml
# netlify.toml
[[headers]]
for = "/assets/*"
[headers.values]
Cache-Control = "public, max-age=31536000, immutable"
```

## Cache Tags and On-Demand Purge

Tag responses for selective cache invalidation:

```typescript
return new Response(body, {
  headers: {
    "Netlify-Cache-ID": "product,listing",
    "Netlify-CDN-Cache-Control": "public, s-maxage=86400",
  },
});
```

Purge by tag:

```typescript
import { purgeCache } from "@netlify/functions";

export default async () => {
  await purgeCache({ tags: ["product"] });
  return new Response("Purged", { status: 202 });
};
```

Purge entire site:

```typescript
await purgeCache();
```

Responses with `Netlify-Cache-ID` are **excluded from automatic deploy-based invalidation** — they must be purged explicitly.

## Cache Key Variation

Customize what creates separate cache entries:

```typescript
return new Response(body, {
  headers: {
    "Netlify-Vary": "cookie=ab_test|is_logged_in",
    // Other options: query=param1|param2, header=X-Custom, country=us|de, language=en|fr
  },
});
```

## Framework-Specific Caching

### Next.js
ISR uses Netlify's durable cache automatically (runtime 5.5.0+). `revalidatePath` and `revalidateTag` trigger cache purge.

### Astro / Remix
Full control over cache headers in server routes. Set `Netlify-CDN-Cache-Control` in responses for CDN caching.

### Nuxt
Default Nitro preset handles caching. ISR-style patterns use `routeRules` with `swr` or `isr` options.

### Vite SPA
Static assets are cached by default. API responses from Netlify Functions need explicit cache headers.

## Debugging

Check the `Cache-Status` response header:
- `HIT` — served from cache
- `MISS` — generated fresh
- `REVALIDATED` — stale content was revalidated

## Constraints

- Basic auth disables caching for the entire site
- Durable cache is serverless functions only (not edge functions)
- Same URL must return identical `Netlify-Vary` headers across responses
- Deploy invalidation is scoped to deploy context (production vs preview)


================================================
FILE: skills\netlify-cli-and-deploy\SKILL.md
================================================
---
name: netlify-cli-and-deploy
description: Guide for using the Netlify CLI and deploying sites. Use when installing the CLI, linking sites, deploying (Git-based or manual), managing environment variables, or running local development. Covers netlify dev, netlify deploy, Git vs non-Git workflows, and environment variable management.
---

# Netlify CLI and Deployment

## Installation

```bash
npm install -g netlify-cli    # Global (for local dev)
npm install netlify-cli -D    # Local (for CI)
```

Requires Node.js 18.14.0+.

## Authentication

```bash
netlify login       # Opens browser for OAuth
netlify status      # Check auth + linked site status
```

For CI, set `NETLIFY_AUTH_TOKEN` environment variable instead.

## Linking a Site

Check if already linked with `netlify status`. If not:

```bash
# Interactive
netlify link

# By Git remote (if using Git)
netlify link --git-remote-url https://github.com/org/repo

# Create new site
netlify init           # With Git CI/CD setup
netlify init --manual  # Without Git CI/CD
```

Site ID is stored in `.netlify/state.json`. Add `.netlify` to `.gitignore`.

## Deploying

### Git-Based Deploys (Continuous Deployment)

Set up with `netlify init`. Automatic deploys trigger on push/PR:
- Push to production branch → production deploy
- Open PR → deploy preview with unique URL
- Push to other branches → branch deploy

Build runs on Netlify's servers. Configure build settings in `netlify.toml`.

### Manual / Local Deploys (No Git Required)

Build locally, then upload:

```bash
netlify deploy          # Draft deploy (preview URL)
netlify deploy --prod   # Production deploy
netlify deploy --dir=dist  # Specify output directory
```

This works without Git — useful for prototypes, local-only projects, or CI pipelines.

## Local Development

### Option 1: netlify dev

```bash
netlify dev
```

Wraps your framework's dev server and provides:
- Environment variable injection
- Functions and edge functions
- Redirects and headers processing

### Option 2: Netlify Vite Plugin (Vite-based projects)

For projects using Vite (React SPA, TanStack Start, SvelteKit, Remix), the Vite plugin provides Netlify platform primitives directly in the framework's dev server:

```bash
npm install @netlify/vite-plugin
```

```typescript
// vite.config.ts
import netlify from "@netlify/vite-plugin";
export default defineConfig({ plugins: [netlify()] });
```

Then run your normal dev command (`npm run dev`) — no `netlify dev` wrapper needed. This gives you access to Blobs, DB, Functions, and environment variables during development.

See the **netlify-frameworks** skill for framework-specific local dev guidance.

## Environment Variables

### CLI Management

```bash
# Set
netlify env:set API_KEY "value"
netlify env:set API_KEY "value" --secret              # Hidden from logs
netlify env:set API_KEY "value" --context production   # Context-specific

# Get
netlify env:get API_KEY

# List
netlify env:list
netlify env:list --plain > .env                        # Export to file

# Import from file
netlify env:import .env

# Delete
netlify env:unset API_KEY
```

### Context Scoping

Variables can be scoped to deploy contexts:

```bash
netlify env:set API_URL "https://api.prod.com" --context production
netlify env:set API_URL "https://api.staging.com" --context deploy-preview
netlify env:set DEBUG "true" --context branch:feature-x
```

### Accessing in Code

- **Server-side (Functions)**: Use `Netlify.env.get("VAR")` (preferred) or `process.env.VAR`
- **Client-side (Vite)**: Only `VITE_`-prefixed vars via `import.meta.env.VITE_VAR`
- **Client-side (Astro)**: Only `PUBLIC_`-prefixed vars via `import.meta.env.PUBLIC_VAR`

**Never use `VITE_` or `PUBLIC_` prefix for secrets** — these are exposed to the browser.

## Useful Commands

| Command | Description |
|---|---|
| `netlify status` | Auth and site link status |
| `netlify dev` | Start local dev server |
| `netlify build` | Run build locally (mimics Netlify environment) |
| `netlify deploy` | Draft deploy |
| `netlify deploy --prod` | Production deploy |
| `netlify dev:exec <cmd>` | Run command with Netlify environment loaded |
| `netlify env:list` | List environment variables |
| `netlify clone org/repo` | Clone, link, and set up in one step |


================================================
FILE: skills\netlify-config\SKILL.md
================================================
---
name: netlify-config
description: Reference for netlify.toml configuration. Use when configuring build settings, redirects, rewrites, headers, deploy contexts, environment variables, or any site-level configuration. Covers the complete netlify.toml syntax including redirects with splats/conditions, headers, deploy contexts, functions config, and edge functions config.
---

# Netlify Configuration (netlify.toml)

Place `netlify.toml` at the repository root (or at the base directory for monorepos).

## Build Settings

```toml
[build]
  base = "project/"          # Base directory (default: root)
  command = "npm run build"  # Build command
  publish = "dist/"          # Output directory
```

## Redirects

```toml
# Basic redirect
[[redirects]]
from = "/old"
to = "/new"
status = 301              # 301 (default), 302, 200 (rewrite), 404

# SPA catch-all
[[redirects]]
from = "/*"
to = "/index.html"
status = 200

# Splat (wildcard)
[[redirects]]
from = "/blog/*"
to = "/news/:splat"

# Path parameters
[[redirects]]
from = "/users/:id"
to = "/api/users/:id"
status = 200

# Force (override existing files)
[[redirects]]
from = "/app/*"
to = "/index.html"
status = 200
force = true

# Proxy to external service
[[redirects]]
from = "/api/*"
to = "https://api.example.com/:splat"
status = 200
[redirects.headers]
  X-Custom = "value"

# Country/language conditions
[[redirects]]
from = "/*"
to = "/fr/:splat"
status = 200
conditions = { Country = ["FR"], Language = ["fr"] }
```

**Rule order matters** — Netlify processes the first matching rule. Place specific rules before general ones.

## Headers

```toml
[[headers]]
for = "/*"
[headers.values]
  X-Frame-Options = "DENY"
  X-Content-Type-Options = "nosniff"

[[headers]]
for = "/assets/*"
[headers.values]
  Cache-Control = "public, max-age=31536000, immutable"
```

Headers apply only to files served from Netlify's CDN (not to function or edge function responses — set those in code).

## Deploy Contexts

Override settings per deploy context:

```toml
[context.production]
command = "npm run build"
environment = { NODE_ENV = "production" }

[context.deploy-preview]
command = "npm run build:preview"

[context.branch-deploy]
command = "npm run build:staging"

[context.dev]
environment = { NODE_ENV = "development" }

# Specific branch
[context."staging"]
command = "npm run build:staging"
```

## Environment Variables

```toml
[build.environment]
NODE_VERSION = "20"

[context.production.environment]
API_URL = "https://api.prod.com"

[context.deploy-preview.environment]
API_URL = "https://api.staging.com"
```

**Do not put secrets in netlify.toml** (it's committed to source control). Use the Netlify UI or CLI for sensitive values. See the **netlify-cli-and-deploy** skill for CLI environment variable management.

## Functions Configuration

```toml
[functions]
directory = "netlify/functions"   # Default
node_bundler = "esbuild"

# Scheduled function
[functions."cleanup"]
schedule = "@daily"
```

## Edge Functions Configuration

```toml
[[edge_functions]]
path = "/admin"
function = "auth"

# Import map for Deno URL imports
[functions]
deno_import_map = "./import_map.json"
```

## Dev Server

```toml
[dev]
command = "npm start"       # Dev server command
port = 8888                 # Netlify Dev port
targetPort = 3000           # Your app's dev server port
framework = "#auto"         # "#auto", "#static", "#custom"
```

## Plugins

```toml
[[plugins]]
package = "@netlify/plugin-lighthouse"
[plugins.inputs]
  audits = ["performance", "accessibility"]
```

## Image CDN

```toml
[images]
remote_images = ["https://example\\.com/.*"]
```

See the **netlify-image-cdn** skill for full Image CDN usage.


================================================
FILE: skills\netlify-db\SKILL.md
================================================
---
name: netlify-db
description: Guide for using Netlify DB (managed Neon Postgres). Use when the project needs a relational database, structured data storage, SQL queries, or data that will grow over time. Covers provisioning, raw SQL via @netlify/neon, Drizzle ORM integration, migrations, and deploy preview branching. Also covers when to use Netlify Blobs instead.
---

# Netlify DB

Netlify DB provisions a managed Neon Postgres database automatically. No Neon account required.

## When to Use DB vs Blobs

**Use Netlify DB when:**
- Storing structured, relational data
- Data will grow over time
- Need queries, filtering, joins, or aggregations

**Use Netlify Blobs instead when:**
- Storing files (images, documents, exports)
- A handful of records with no growth expectation
- Simple key-value storage with no relational needs
- Want zero dependencies beyond `@netlify/blobs`

See the **netlify-blobs** skill for Blobs usage.

## Setup

```bash
npm install @netlify/neon
netlify db init    # Provisions database and sets up Drizzle ORM
```

Prerequisites: logged into Netlify CLI and site linked (`netlify link`).

## Raw SQL via @netlify/neon

`@netlify/neon` wraps `@neondatabase/serverless`. No connection string needed — it auto-configures.

```typescript
import { neon } from "@netlify/neon";
const sql = neon();

const users = await sql("SELECT * FROM users");
await sql("INSERT INTO users (name) VALUES ($1)", ["Jane"]);
await sql("UPDATE users SET name = $1 WHERE id = $2", ["Jane", 1]);
await sql("DELETE FROM users WHERE id = $1", [1]);
```

## Drizzle ORM Integration

For most projects, use Drizzle ORM on top of Netlify DB.

### drizzle.config.ts

```typescript
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  dbCredentials: { url: process.env.NETLIFY_DATABASE_URL! },
  schema: "./db/schema.ts",
  out: "./migrations",
  migrations: { prefix: "timestamp" }, // Avoids conflicts across branches
});
```

### db/index.ts

```typescript
import { neon } from "@neondatabase/serverless";
import { drizzle } from "drizzle-orm/neon-http";
import * as schema from "./schema";

const sql = neon(process.env.NETLIFY_DATABASE_URL!);
export const db = drizzle(sql, { schema });
export * from "./schema";
```

### Schema Example

```typescript
// db/schema.ts
import { integer, pgTable, varchar, text, boolean, timestamp } from "drizzle-orm/pg-core";

export const items = pgTable("items", {
  id: integer().primaryKey().generatedAlwaysAsIdentity(),
  title: varchar({ length: 255 }).notNull(),
  description: text(),
  isActive: boolean("is_active").notNull().default(true),
  createdAt: timestamp("created_at").defaultNow(),
  updatedAt: timestamp("updated_at").defaultNow(),
});

export type Item = typeof items.$inferSelect;
export type NewItem = typeof items.$inferInsert;
```

### Query Patterns

```typescript
import { db, items } from "../db";
import { eq } from "drizzle-orm";

const all = await db.select().from(items);
const [one] = await db.select().from(items).where(eq(items.id, id)).limit(1);
const [created] = await db.insert(items).values({ title: "New" }).returning();
const [updated] = await db.update(items).set({ title: "Updated" }).where(eq(items.id, id)).returning();
await db.delete(items).where(eq(items.id, id));
```

## Migrations

```json
{
  "scripts": {
    "db:generate": "drizzle-kit generate",
    "db:migrate": "netlify dev:exec drizzle-kit migrate",
    "db:push": "netlify dev:exec drizzle-kit push",
    "db:studio": "netlify dev:exec drizzle-kit studio"
  }
}
```

Workflow: modify schema, run `db:generate`, then `db:migrate`.

## Deploy Preview Branching

Netlify DB supports branching — production branch gets the production database, all other branches and deploy previews get a separate preview branch. Develop and test migrations on preview, merge to main, then apply to production.

## Environment Variables

- `NETLIFY_DATABASE_URL` — Auto-set by Netlify when database is provisioned
- Retrieve manually: `netlify env:get NETLIFY_DATABASE_URL`

## Local Development

Run `netlify dev` or use `@netlify/vite-plugin` to get database access locally. Use `netlify dev:exec` to run migration commands with the proper environment.


================================================
FILE: skills\netlify-deploy\SKILL.md
================================================
---
name: netlify-deploy
description: Deploy web projects to Netlify using the Netlify CLI (`npx netlify`). Use when the user asks to deploy, host, publish, or link a site/repo on Netlify, including preview and production deploys.
---

# Netlify Deployment Skill

Deploy web projects to Netlify using the Netlify CLI with intelligent detection of project configuration and deployment context.

## Overview

This skill automates Netlify deployments by:
- Verifying Netlify CLI authentication
- Detecting project configuration and framework
- Linking to existing sites or creating new ones
- Deploying to production or preview environments

## Prerequisites

- **Netlify CLI**: Installed via npx (no global install required)
- **Authentication**: Netlify account with active login session
- **Project**: Valid web project in current directory
- **Network access**: Deployment requires outbound network calls. If sandboxing blocks these, the agent may need to request elevated permissions or prompt the user.
- **Timeouts**: Deployments can take a few minutes. Use appropriate timeout values for CLI commands.

## Authentication Pattern

The skill uses the **pre-authenticated Netlify CLI** approach:

1. Check authentication status with `npx netlify status`
2. If not authenticated, guide user through `npx netlify login`
3. Fail gracefully if authentication cannot be established

Authentication uses either:
- **Browser-based OAuth** (primary): `netlify login` opens browser for authentication
- **API Key** (alternative): Set `NETLIFY_AUTH_TOKEN` environment variable

## Workflow

### 1. Verify Netlify CLI Authentication

Check if the user is logged into Netlify:

```bash
npx netlify status
```

**Expected output patterns**:
- ✅ Authenticated: Shows logged-in user email and site link status
- ❌ Not authenticated: "Not logged into any site" or authentication error

**If not authenticated**, guide the user:

```bash
npx netlify login
```

This opens a browser window for OAuth authentication. Wait for user to complete login, then verify with `netlify status` again.

**Alternative: API Key authentication**

If browser authentication isn't available, users can set:

```bash
export NETLIFY_AUTH_TOKEN=your_token_here
```

Tokens can be generated at: https://app.netlify.com/user/applications#personal-access-tokens

### 2. Detect Site Link Status

From `netlify status` output, determine:
- **Linked**: Site already connected to Netlify (shows site name/URL)
- **Not linked**: Need to link or create site

### 3. Link to Existing Site or Create New

**If already linked** → Skip to step 4

**If not linked**, attempt to link by Git remote:

```bash
# Check if project is Git-based
git remote show origin

# If Git-based, extract remote URL
# Format: https://github.com/username/repo or git@github.com:username/repo.git

# Try to link by Git remote
npx netlify link --git-remote-url <REMOTE_URL>
```

**If link fails** (site doesn't exist on Netlify):

```bash
# Create new site interactively
npx netlify init
```

This guides user through:
1. Choosing team/account
2. Setting site name
3. Configuring build settings
4. Creating netlify.toml if needed

### 4. Verify Dependencies

Before deploying, ensure project dependencies are installed:

```bash
# For npm projects
npm install

# For other package managers, detect and use appropriate command
# yarn install, pnpm install, etc.
```

### 5. Deploy to Netlify

Choose deployment type based on context:

**Preview/Draft Deploy** (default for existing sites):

```bash
npx netlify deploy
```

This creates a deploy preview with a unique URL for testing.

**Production Deploy** (for new sites or explicit production deployments):

```bash
npx netlify deploy --prod
```

This deploys to the live production URL.

**Deployment process**:
1. CLI detects build settings (from netlify.toml or prompts user)
2. Builds the project locally
3. Uploads built assets to Netlify
4. Returns deployment URL

### 6. Report Results

After deployment, report to user:
- **Deploy URL**: Unique URL for this deployment
- **Site URL**: Production URL (if production deploy)
- **Deploy logs**: Link to Netlify dashboard for logs
- **Next steps**: Suggest `netlify open` to view site or dashboard

## Handling netlify.toml

If a `netlify.toml` file exists, the CLI uses it automatically. If not, the CLI will prompt for:
- **Build command**: e.g., `npm run build`, `next build`
- **Publish directory**: e.g., `dist`, `build`, `.next`

Common framework defaults:
- **Next.js**: build command `npm run build`, publish `.next`
- **React (Vite)**: build command `npm run build`, publish `dist`
- **Static HTML**: no build command, publish current directory

The skill should detect framework from `package.json` if possible and suggest appropriate settings.

## Example Full Workflow

```bash
# 1. Check authentication
npx netlify status

# If not authenticated:
npx netlify login

# 2. Link site (if needed)
# Try Git-based linking first
git remote show origin
npx net

================================================
FILE: skills\netlify-deploy\references\cli-commands.md
================================================
# Netlify CLI Commands Reference

Quick reference for common Netlify CLI commands used in deployments.

## Authentication

```bash
# Login via browser OAuth
npx netlify login

# Check authentication status and site link
npx netlify status

# Logout
npx netlify logout
```

## Site Management

```bash
# Link current directory to existing site
npx netlify link

# Link by Git remote URL
npx netlify link --git-remote-url <url>

# Create and link new site
npx netlify init

# Unlink from current site
npx netlify unlink

# Open site in Netlify dashboard
npx netlify open

# Open site admin panel
npx netlify open:admin

# Open site in browser
npx netlify open:site
```

## Deployment

```bash
# Deploy preview/draft (safe for testing)
npx netlify deploy

# Deploy to production
npx netlify deploy --prod

# Deploy with specific directory
npx netlify deploy --dir=dist

# Deploy with message
npx netlify deploy --message="Deploy message"

# List all deploys
npx netlify deploy:list
```

## Development

```bash
# Run local dev server with Netlify features
npx netlify dev

# Run local dev server on specific port
npx netlify dev --port 3000
```

## Site Information

```bash
# Get site info
npx netlify sites:list

# Get current site info
npx netlify api getSite --data '{"site_id": "YOUR_SITE_ID"}'
```

## Environment Variables

```bash
# List environment variables
npx netlify env:list

# Set environment variable
npx netlify env:set KEY value

# Get environment variable value
npx netlify env:get KEY

# Import env vars from file
npx netlify env:import .env
```

## Build

```bash
# Show build settings
npx netlify build --dry

# Run build locally
npx netlify build
```

## Functions (Serverless)

```bash
# List functions
npx netlify functions:list

# Invoke function locally
npx netlify functions:invoke FUNCTION_NAME

# Create new function
npx netlify functions:create FUNCTION_NAME
```

## Logs

```bash
# Stream function logs
npx netlify logs

# View logs for specific function
npx netlify logs:function FUNCTION_NAME
```

## Troubleshooting Commands

```bash
# Check CLI version
npx netlify --version

# Get help for any command
npx netlify help [command]

# Check status with verbose output
npx netlify status --verbose
```

## Exit Codes

- `0` - Success
- `1` - General error
- `2` - Authentication error
- `3` - Site not found
- `4` - Build failed

## Common Flags

- `--json` - Output as JSON
- `--silent` - Suppress output
- `--debug` - Show debug information
- `--force` - Skip confirmation prompts

## Resources

- Full CLI documentation: https://docs.netlify.com/cli/get-started/
- CLI GitHub repository: https://github.com/netlify/cli


================================================
FILE: skills\netlify-deploy\references\deployment-patterns.md
================================================
# Netlify Deployment Patterns

Common deployment scenarios and best practices for the Netlify skill.

## Deployment Decision Tree

```
Is user authenticated?
├─ No → Run `netlify login`
└─ Yes → Is site linked?
    ├─ No → Is it a Git repo?
    │   ├─ Yes → Try `netlify link --git-remote-url`
    │   │   ├─ Success → Continue to deploy
    │   │   └─ Fail → Run `netlify init`
    │   └─ No → Run `netlify init`
    └─ Yes → Is this first deploy or existing site?
        ├─ First deploy/new site → `netlify deploy --prod`
        └─ Existing site → `netlify deploy` (preview)
```

## Scenario 1: First-Time Deployment (New Project)

**Context**: User has a project that has never been deployed to Netlify.

**Steps**:
1. Check authentication: `npx netlify status`
2. If not authenticated: `npx netlify login`
3. Initialize new site: `npx netlify init`
   - This guides user through setup
   - Creates netlify.toml if needed
4. Install dependencies: `npm install`
5. Deploy to production: `npx netlify deploy --prod`

**Example**:
```bash
npx netlify status
# Not linked to a site

npx netlify login
# Opens browser for authentication

npx netlify init
# Walks through site creation

npm install
npx netlify deploy --prod
```

## Scenario 2: Linking Existing Git Repository to Existing Site

**Context**: User has a site already on Netlify and wants to link their local repo.

**Steps**:
1. Check authentication: `npx netlify status`
2. Get Git remote: `git remote show origin`
3. Extract URL (e.g., `https://github.com/user/repo.git`)
4. Link by remote: `npx netlify link --git-remote-url <URL>`
5. If found, linked. If not, run `netlify init`

**Example**:
```bash
git remote show origin
# * remote origin
#   Fetch URL: https://github.com/user/my-app.git

npx netlify link --git-remote-url https://github.com/user/my-app.git
# Site linked successfully
```

## Scenario 3: Preview Deployment (Testing Changes)

**Context**: User wants to test changes before pushing to production.

**Steps**:
1. Ensure site is linked: `npx netlify status`
2. Make code changes
3. Deploy preview: `npx netlify deploy`
4. Review preview URL
5. If approved, deploy to prod: `npx netlify deploy --prod`

**Example**:
```bash
# Make changes to code

npx netlify deploy
# Draft deploy URL: https://507f1f77bcf86cd799439011-my-app.netlify.app

# Test the preview, then:
npx netlify deploy --prod
```

## Scenario 4: Framework-Specific Deployments

### Next.js

```bash
# Next.js typically uses .next as output
npx netlify deploy --prod

# netlify.toml should have:
# [build]
#   command = "npm run build"
#   publish = ".next"
```

### React (Vite)

```bash
# Vite outputs to dist by default
npm run build
npx netlify deploy --dir=dist --prod

# netlify.toml:
# [build]
#   command = "npm run build"
#   publish = "dist"
```

### Static HTML

```bash
# No build step needed
npx netlify deploy --dir=. --prod
```

## Scenario 5: Monorepo Deployment

**Context**: Project is in a subdirectory of a monorepo.

**Steps**:
1. Navigate to project subdirectory: `cd packages/frontend`
2. Or set base in netlify.toml:
   ```toml
   [build]
     base = "packages/frontend"
     command = "npm run build"
     publish = "dist"
   ```
3. Deploy normally: `npx netlify deploy --prod`

## Scenario 6: Environment Variables

**Context**: Project needs secrets or environment-specific config.

**Steps**:
1. Never commit secrets to Git
2. Set in Netlify dashboard or CLI:
   ```bash
   npx netlify env:set API_KEY "secret_value"
   npx netlify env:set NODE_ENV "production"
   ```
3. Access in code: `process.env.API_KEY`
4. Deploy: `npx netlify deploy --prod`

## Scenario 7: Custom Domain Setup

**Context**: User wants to use a custom domain.

**Steps**:
1. Deploy site first: `npx netlify deploy --prod`
2. Add domain via dashboard or CLI:
   ```bash
   npx netlify open:admin
   # Navigate to Domain settings
   ```
3. Update DNS records as instructed by Netlify
4. Wait for DNS propagation (can take up to 48 hours)

## Best Practices

### 1. Always Preview First

```bash
# Deploy preview
npx netlify deploy

# Test thoroughly
# Then deploy to production
npx netlify deploy --prod
```

### 2. Use netlify.toml for Consistency

Create a `netlify.toml` file in your repo root:

```toml
[build]
  command = "npm run build"
  publish = "dist"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

This ensures consistent builds across all deployments.

### 3. Framework Detection

Let Netlify auto-detect when possible. Only specify build settings if:
- Netlify can't detect your framework
- You need custom build commands
- Your project has a non-standard structure

### 4. Dependency Installation

Always ensure dependencies are installed before deploying:

```bash
npm install  # or yarn install, pnpm install
npx netlify deploy
```

### 5. Build Locally First

Test builds locally before deploying:

```bash
npm run build
# Check that build output exists

npx netlify deploy --dir=dist
```

### 6. Use Deploy Me

================================================
FILE: skills\netlify-deploy\references\netlify-toml.md
================================================
# netlify.toml Configuration Reference

Configuration file for Netlify builds and deployments.

## Basic Structure

```toml
[build]
  command = "npm run build"
  publish = "dist"
```

## Build Settings

### Common Configuration

```toml
[build]
  # Command to build your site
  command = "npm run build"

  # Directory to publish (relative to repo root)
  publish = "dist"

  # Functions directory
  functions = "netlify/functions"

  # Base directory (if not repo root)
  base = "packages/frontend"

  # Ignore builds for specific conditions
  ignore = "git diff --quiet HEAD^ HEAD package.json"
```

## Environment Variables

```toml
[build.environment]
  NODE_VERSION = "18"
  NPM_FLAGS = "--prefix=/dev/null"

[context.production.environment]
  NODE_ENV = "production"
```

## Framework Detection

Netlify auto-detects frameworks, but you can override:

### Next.js

```toml
[build]
  command = "npm run build"
  publish = ".next"
```

### React (Vite)

```toml
[build]
  command = "npm run build"
  publish = "dist"
```

### Vue

```toml
[build]
  command = "npm run build"
  publish = "dist"
```

### Astro

```toml
[build]
  command = "npm run build"
  publish = "dist"
```

### SvelteKit

```toml
[build]
  command = "npm run build"
  publish = "build"
```

## Redirects and Rewrites

```toml
[[redirects]]
  from = "/old-path"
  to = "/new-path"
  status = 301

[[redirects]]
  from = "/api/*"
  to = "https://api.example.com/:splat"
  status = 200

# SPA fallback (for client-side routing)
[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

## Headers

```toml
[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-XSS-Protection = "1; mode=block"
    Content-Security-Policy = "default-src 'self'"

[[headers]]
  for = "/assets/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"
```

## Context-Specific Configuration

Deploy different settings per context:

```toml
# Production
[context.production]
  command = "npm run build:prod"
  [context.production.environment]
    NODE_ENV = "production"

# Deploy previews
[context.deploy-preview]
  command = "npm run build:preview"

# Branch deploys
[context.branch-deploy]
  command = "npm run build:staging"

# Specific branch
[context.staging]
  command = "npm run build:staging"
```

## Functions Configuration

```toml
[functions]
  directory = "netlify/functions"
  node_bundler = "esbuild"

[[functions]]
  path = "/api/*"
  function = "api"
```

## Build Plugins

```toml
[[plugins]]
  package = "@netlify/plugin-lighthouse"

  [plugins.inputs]
    output_path = "reports/lighthouse.html"

[[plugins]]
  package = "netlify-plugin-submit-sitemap"

  [plugins.inputs]
    baseUrl = "https://example.com"
    sitemapPath = "/sitemap.xml"
```

## Edge Functions

```toml
[[edge_functions]]
  function = "geolocation"
  path = "/api/location"
```

## Processing

```toml
[build.processing]
  skip_processing = false

[build.processing.css]
  bundle = true
  minify = true

[build.processing.js]
  bundle = true
  minify = true

[build.processing.html]
  pretty_urls = true

[build.processing.images]
  compress = true
```

## Common Patterns

### Single Page Application (SPA)

```toml
[build]
  command = "npm run build"
  publish = "dist"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

### Monorepo with Base Directory

```toml
[build]
  base = "packages/web"
  command = "npm run build"
  publish = "dist"
```

### Multiple Redirects with Country-Based Routing

```toml
[[redirects]]
  from = "/"
  to = "/uk"
  status = 302
  conditions = {Country = ["GB"]}

[[redirects]]
  from = "/"
  to = "/us"
  status = 302
  conditions = {Country = ["US"]}
```

## Validation

Validate your netlify.toml:

```bash
npx netlify build --dry
```

## Resources

- Full configuration reference: https://docs.netlify.com/configure-builds/file-based-configuration/
- Framework-specific guides: https://docs.netlify.com/frameworks/


================================================
FILE: skills\netlify-edge-functions\SKILL.md
================================================
---
name: netlify-edge-functions
description: Guide for writing Netlify Edge Functions. Use when building middleware, geolocation-based logic, request/response manipulation, authentication checks, A/B testing, or any low-latency edge compute. Covers Deno runtime, context.next() middleware pattern, geolocation, and when to choose edge vs serverless.
---

# Netlify Edge Functions

Edge functions run on Netlify's globally distributed edge network (Deno runtime), providing low-latency responses close to users.

## Syntax

```typescript
import type { Config, Context } from "@netlify/edge-functions";

export default async (req: Request, context: Context) => {
  return new Response("Hello from the edge!");
};

export const config: Config = {
  path: "/hello",
};
```

Place files in `netlify/edge-functions/`. Uses `.ts`, `.js`, `.tsx`, or `.jsx` extensions.

## Config Object

```typescript
export const config: Config = {
  path: "/api/*",                    // URLPattern path(s)
  excludedPath: "/api/public/*",     // Exclusions
  method: ["GET", "POST"],           // HTTP methods
  onError: "bypass",                 // "fail" (default), "bypass", or "/error-page"
  cache: "manual",                   // Enable response caching
};
```

## Middleware Pattern

Use `context.next()` to invoke the next handler in the chain and optionally modify the response:

```typescript
export default async (req: Request, context: Context) => {
  // Before: modify request or short-circuit
  if (!isAuthenticated(req)) {
    return new Response("Unauthorized", { status: 401 });
  }

  // Continue to origin/next function
  const response = await context.next();

  // After: modify response
  response.headers.set("x-custom-header", "value");
  return response;
};
```

Return `undefined` to pass through without modification:

```typescript
export default async (req: Request, context: Context) => {
  if (!shouldHandle(req)) return; // continues to next handler
  return new Response("Handled");
};
```

## Geolocation and IP

```typescript
export default async (req: Request, context: Context) => {
  const { city, country, subdivision, timezone } = context.geo;
  const ip = context.ip;

  if (country?.code === "DE") {
    return Response.redirect(new URL("/de", req.url));
  }
};
```

Local dev with mocked geo: `netlify dev --geo=mock --country=US`

## Environment Variables

Use `Netlify.env` (not `process.env` or `Deno.env`):

```typescript
const secret = Netlify.env.get("API_SECRET");
```

## Module Support

- **Node.js builtins**: `import { randomBytes } from "node:crypto";`
- **npm packages**: Install via npm and import by name
- **Deno modules**: URL imports (e.g., `import X from "https://esm.sh/package"`)

For URL imports, use an import map:

```json
// import_map.json
{ "imports": { "html-rewriter": "https://ghuc.cc/worker-tools/html-rewriter/index.ts" } }
```

```toml
# netlify.toml
[functions]
  deno_import_map = "./import_map.json"
```

## When to Use Edge vs Serverless

| Use Edge Functions for | Use Serverless Functions for |
|---|---|
| Low-latency responses | Long-running operations (up to 15 min) |
| Request/response manipulation | Complex Node.js dependencies |
| Geolocation-based logic | Database-heavy operations |
| Auth checks and redirects | Background/scheduled tasks |
| A/B testing, personalization | Tasks needing > 512 MB memory |

## Limits

| Resource | Limit |
|---|---|
| CPU time | 50 ms per request |
| Memory | 512 MB per deployed set |
| Response header timeout | 40 seconds |
| Code size | 20 MB compressed |


================================================
FILE: skills\netlify-forms\SKILL.md
================================================
---
name: netlify-forms
description: Guide for using Netlify Forms for HTML form handling. Use when adding contact forms, feedback forms, file upload forms, or any form that should be collected by Netlify. Covers the data-netlify attribute, spam filtering, AJAX submissions, file uploads, notifications, and the submissions API.
---

# Netlify Forms

Netlify Forms collects HTML form submissions without server-side code. Form detection must be enabled in the Netlify UI (Forms section).

## Basic Setup

Add `data-netlify="true"` and a unique `name` to the form:

```html
<form name="contact" method="POST" data-netlify="true">
  <label>Name: <input type="text" name="name" /></label>
  <label>Email: <input type="email" name="email" /></label>
  <label>Message: <textarea name="message"></textarea></label>
  <button type="submit">Send</button>
</form>
```

Netlify's build system detects the form and injects a hidden `form-name` input automatically. For a custom success page, add `action="/thank-you"` to the form tag. Use paths without `.html` extension — Netlify serves `thank-you.html` at `/thank-you` by default, and the `.html` path returns 404.

## JavaScript-Rendered Forms (React, Vue, SSR Frameworks)

For forms rendered by JavaScript frameworks (React, Vue, TanStack Start, Next.js, SvelteKit, Remix, Nuxt), Netlify's build parser cannot detect the form in static HTML. You MUST create a static HTML skeleton file for build-time form detection:

Create a static HTML file in `public/` (e.g. `public/__forms.html`) containing a hidden copy of each form:

```html
<!DOCTYPE html>
<html>
  <body>
    <form name="contact" data-netlify="true" netlify-honeypot="bot-field" hidden>
      <input type="hidden" name="form-name" value="contact" />
      <input type="text" name="name" />
      <input type="email" name="email" />
      <textarea name="message"></textarea>
      <input name="bot-field" />
    </form>
  </body>
</html>
```

**Rules:**
- The form `name` must exactly match the `form-name` value used in your component's fetch call
- Include every field your component submits — Netlify validates field names against the registered form
- Without this file, Netlify cannot detect the form and submissions will silently fail

Your component must also include a hidden `form-name` input:

```jsx
<form name="contact" method="POST" data-netlify="true">
  <input type="hidden" name="form-name" value="contact" />
  {/* ... fields ... */}
</form>
```

## AJAX Submissions

### Vanilla JavaScript

```javascript
const form = document.querySelector("form");
form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const formData = new FormData(form);
  await fetch("/", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams(formData).toString(),
  });
});
```

> **SSR frameworks (TanStack Start, Next.js, SvelteKit, Remix, Nuxt):** The `fetch` URL must target the static skeleton
> file path (e.g. `"/__forms.html"`), **not** `"/"`. In SSR apps, `fetch("/")` is intercepted by the SSR catch-all
> function and never reaches Netlify's form processing middleware. See the React example and troubleshooting section below.

### React Example

```tsx
function ContactForm() {
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);
    // For SSR apps, use the skeleton file path instead of "/" (e.g. "/__forms.html")
    const response = await fetch("/__forms.html", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams(formData as any).toString(),
    });
    if (response.ok) {
      // Show success feedback
    }
  };

  return (
    <form name="contact" method="POST" data-netlify="true" onSubmit={handleSubmit}>
      <input type="hidden" name="form-name" value="contact" />
      <input type="text" name="name" placeholder="Name" />
      <input type="email" name="email" placeholder="Email" />
      <textarea name="message" placeholder="Message" />
      <button type="submit">Send</button>
    </form>
  );
}
```

> **SSR troubleshooting:** If form submissions appear to succeed (200 response) but nothing shows in the Netlify Forms
> UI, the POST is likely being intercepted by the SSR function. Ensure `fetch` targets the skeleton file path (e.g.
> `"/__forms.html"`), not `"/"`. The skeleton file path routes through the CDN origin where Netlify's form handler runs.

## Spam Filtering

Netlify uses Akismet automatically. Add a honeypot field for extra protection:

```html
<form name="contact" method="POST" netlify-honeypot="bot-field" data-netlify="true">
  <p style="display:none">
    <label>Don't fill this out: <input name="bot-field" /></label>
  </p>
  <!-- visible fields -->
</form>
```

For reCAPTCHA, add `data-netlify-recaptcha="true"` to the form and include `<div data-netlify-recaptcha="true"></div>` where t

================================================
FILE: skills\netlify-frameworks\SKILL.md
================================================
---
name: netlify-frameworks
description: Guide for deploying web frameworks on Netlify. Use when setting up a framework project (Vite/React, Astro, TanStack Start, Next.js, Nuxt, SvelteKit, Remix) for Netlify deployment, configuring adapters or plugins, or troubleshooting framework-specific Netlify integration. Covers what Netlify needs from each framework and how adapters handle server-side rendering.
---

# Frameworks on Netlify

Netlify supports any framework that produces static output. For frameworks with server-side capabilities (SSR, API routes, middleware), an adapter or plugin translates the framework's server-side code into Netlify Functions and Edge Functions automatically.

## How It Works

During build, the framework adapter writes files to `.netlify/v1/` — functions, edge functions, redirects, and configuration. Netlify reads these to deploy the site. You do not need to write Netlify Functions manually when using a framework adapter for server-side features.

## Detecting Your Framework

Check these files to determine the framework:

| File | Framework |
|---|---|
| `astro.config.*` | Astro |
| `next.config.*` | Next.js |
| `nuxt.config.*` | Nuxt |
| `vite.config.*` + `react-router` | Vite + React (SPA or Remix) |
| `app.config.*` + `@tanstack/react-start` | TanStack Start |
| `svelte.config.*` | SvelteKit |

## Framework Reference Guides

Each framework has specific adapter/plugin requirements and local dev patterns:


## General Patterns

### Client-Side Routing (SPA)

For single-page apps with client-side routing, add a catch-all redirect:

```toml
# netlify.toml
[[redirects]]
from = "/*"
to = "/index.html"
status = 200
```

### Custom 404 Pages

- **Static sites**: Create a `404.html` in your publish directory. Netlify serves it automatically for unmatched routes.
- **SSR frameworks**: Handle 404s in the framework's routing (the adapter maps this to Netlify's function routing).

### Environment Variables in Frameworks

Each framework exposes environment variables to client-side code differently:

| Framework | Client prefix | Access pattern |
|---|---|---|
| Vite / React | `VITE_` | `import.meta.env.VITE_VAR` |
| Astro | `PUBLIC_` | `import.meta.env.PUBLIC_VAR` |
| Next.js | `NEXT_PUBLIC_` | `process.env.NEXT_PUBLIC_VAR` |
| Nuxt | `NUXT_PUBLIC_` | `useRuntimeConfig().public.var` |

Server-side code in all frameworks can access variables via `process.env.VAR` or `Netlify.env.get("VAR")`.


================================================
FILE: skills\netlify-frameworks\references\astro.md
================================================
# Astro on Netlify

## Setup

Install the Netlify adapter:

```bash
npx astro add netlify
```

This installs `@astrojs/netlify` and updates `astro.config.*` automatically.

### Manual Setup

```bash
npm install @astrojs/netlify
```

```typescript
// astro.config.mjs
import { defineConfig } from "astro/config";
import netlify from "@astrojs/netlify";

export default defineConfig({
  output: "server",  // or "hybrid" for mixed static/SSR
  adapter: netlify(),
});
```

## Output Modes

| Mode | Behavior |
|---|---|
| `"static"` | Fully pre-rendered at build time (no adapter needed) |
| `"server"` | All pages rendered on request (SSR) |
| `"hybrid"` | Static by default, opt-in to SSR per page with `export const prerender = false` |

## What the Adapter Does

- Converts Astro server routes into Netlify Functions
- Handles SSR, API routes, and middleware
- Maps Astro's routing to Netlify's function routing
- You do **not** write raw Netlify Functions for Astro's server routes

## API Routes

Astro API routes (in `src/pages/api/`) are handled by the adapter:

```typescript
// src/pages/api/items.ts
import type { APIRoute } from "astro";

export const GET: APIRoute = async () => {
  return new Response(JSON.stringify({ items: [] }), {
    headers: { "Content-Type": "application/json" },
  });
};

export const POST: APIRoute = async ({ request }) => {
  const data = await request.json();
  return new Response(JSON.stringify({ created: data }), { status: 201 });
};
```

## Forms (HTML Pattern)

Astro renders HTML server-side, so Netlify can detect forms directly:

```astro
---
// src/pages/contact.astro
---
<form name="contact" method="POST" data-netlify="true">
  <label>Name: <input type="text" name="name" /></label>
  <label>Email: <input type="email" name="email" /></label>
  <label>Message: <textarea name="message"></textarea></label>
  <button type="submit">Send</button>
</form>
```

For form submissions that should redirect back with feedback, handle the POST in an API route and redirect:

```typescript
// src/pages/api/contact.ts
export const POST: APIRoute = async ({ request, redirect }) => {
  const formData = await request.formData();
  // Process form...
  return redirect("/contact?success=true");
};
```

## Custom 404

Create `src/pages/404.astro`. Astro handles this automatically.

## Local Development

**Option A: Astro dev server** (simpler, but no Netlify primitives):

```bash
npm run dev    # astro dev
```

**Option B: netlify dev** (full Netlify environment including functions, env vars):

```bash
netlify dev
```

The Astro adapter's local dev experience with `netlify dev` varies — for Blobs and DB access, `netlify dev` is recommended. If using `@netlify/vite-plugin` alongside Astro, local platform primitives may also be available via the standard dev server, but this integration is less mature than with pure Vite projects.

## Build and Deploy

```toml
# netlify.toml
[build]
command = "astro build"
publish = "dist"
```

The adapter configures the publish directory and function routing automatically.


================================================
FILE: skills\netlify-frameworks\references\nextjs.md
================================================
# Next.js on Netlify

## Setup

Next.js on Netlify uses the `@netlify/next` runtime, which is installed automatically. No manual adapter installation is required — Netlify detects Next.js and configures the build automatically.

```toml
# netlify.toml
[build]
command = "next build"
publish = ".next"
```

## What the Runtime Does

- Converts Next.js server-side features (SSR, API routes, middleware, ISR) into Netlify Functions and Edge Functions
- Handles image optimization via Netlify Image CDN
- Maps Next.js routing to Netlify's infrastructure
- Supports App Router and Pages Router

## Key Configuration

### next.config.js

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [
      { protocol: "https", hostname: "example.com" },
    ],
  },
};

module.exports = nextConfig;
```

Remote image patterns in `next.config.js` are automatically mapped to Netlify Image CDN's `remote_images` configuration.

## API Routes

Next.js API routes work automatically — they are deployed as Netlify Functions:

```typescript
// app/api/items/route.ts (App Router)
export async function GET() {
  return Response.json({ items: [] });
}

export async function POST(request: Request) {
  const data = await request.json();
  return Response.json({ created: data }, { status: 201 });
}
```

## Middleware

Next.js middleware is deployed as a Netlify Edge Function:

```typescript
// middleware.ts
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

export function middleware(request: NextRequest) {
  // Runs at the edge on Netlify
  return NextResponse.next();
}
```

## ISR (Incremental Static Regeneration)

ISR works on Netlify. Pages with `revalidate` are cached and revalidated using Netlify's CDN cache with `stale-while-revalidate`. On-demand revalidation via `revalidatePath` and `revalidateTag` triggers Netlify cache purge.

## Local Development

```bash
npm run dev    # next dev — standard Next.js dev server
```

For Netlify-specific features (environment variables, edge middleware testing), use:

```bash
netlify dev
```

## Known Patterns

- **Static export** (`output: "export"`): Works without the runtime — produces a fully static site
- **Standalone mode** is not required; the Netlify runtime handles deployment automatically
- Environment variables use the `NEXT_PUBLIC_` prefix for client-side access


================================================
FILE: skills\netlify-frameworks\references\tanstack.md
================================================
# TanStack Start on Netlify

## Setup

TanStack Start uses the Netlify Vite plugin for deployment.

```bash
npm install @netlify/vite-plugin
```

```typescript
// app.config.ts
import { defineConfig } from "@tanstack/react-start/config";
import netlify from "@netlify/vite-plugin";

export default defineConfig({
  vite: {
    plugins: [netlify()],
  },
});
```

## What the Plugin Does

- Handles SSR output for Netlify Functions
- Enables Netlify platform primitives (Blobs, DB, env vars) in local dev
- Maps TanStack Start's file-based routing to Netlify's infrastructure

## Server Functions

TanStack Start uses `createServerFn` for server-side logic. These are automatically handled by the Netlify Vite plugin — no raw Netlify Functions needed:

```typescript
import { createServerFn } from "@tanstack/react-start";

const getItems = createServerFn({ method: "GET" }).handler(async () => {
  // Server-side code — runs as Netlify Function in production
  const items = await db.select().from(itemsTable);
  return items;
});
```

## Local Development

```bash
npm run dev    # Uses Vite plugin — Netlify primitives available
```

The Vite plugin provides Functions, Blobs, DB, and environment variables during local dev without needing `netlify dev`.

## Build and Deploy

```toml
# netlify.toml
[build]
command = "npm run build"
publish = ".output/public"
```

The Vite plugin configures the output structure for Netlify automatically.


================================================
FILE: skills\netlify-frameworks\references\vite.md
================================================
# Vite + React on Netlify

## Setup

Install the Netlify Vite plugin:

```bash
npm install @netlify/vite-plugin
```

```typescript
// vite.config.ts
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import netlify from "@netlify/vite-plugin";

export default defineConfig({
  plugins: [react(), netlify()],
});
```

## What the Plugin Does

- Enables Netlify Functions, Blobs, DB, and environment variables in local dev
- Handles build output for Netlify deployment
- No need for `netlify dev` — run `npm run dev` directly

## SPA Routing

For client-side routing (React Router, etc.), add the catch-all redirect:

```toml
# netlify.toml
[[redirects]]
from = "/*"
to = "/index.html"
status = 200
```

## Netlify Functions

Write functions in `netlify/functions/` as usual. The Vite plugin makes them available during local dev at their configured paths.

```typescript
// netlify/functions/api.ts
import type { Config, Context } from "@netlify/functions";

export default async (req: Request, context: Context) => {
  return Response.json({ message: "Hello from API" });
};

export const config: Config = { path: "/api/hello" };
```

## Forms (AJAX Pattern)

Since Vite + React renders forms client-side, include a hidden HTML form for Netlify to detect, and submit via AJAX:

```tsx
// In your React component
function ContactForm() {
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);
    await fetch("/", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams(formData as any).toString(),
    });
  };

  return (
    <form name="contact" method="POST" data-netlify="true" onSubmit={handleSubmit}>
      <input type="hidden" name="form-name" value="contact" />
      {/* fields */}
    </form>
  );
}
```

Also add a hidden form in `index.html`:

```html
<form name="contact" netlify hidden>
  <input type="text" name="name" />
  <input type="email" name="email" />
  <textarea name="message"></textarea>
</form>
```

## Local Dev

```bash
npm run dev   # Uses Vite plugin — Netlify primitives available
```

No `netlify dev` wrapper needed. Functions, Blobs, DB, and environment variables all work.

## Build and Deploy

```toml
# netlify.toml
[build]
command = "npm run build"
publish = "dist"
```


================================================
FILE: skills\netlify-functions\SKILL.md
================================================
---
name: netlify-functions
description: Guide for writing Netlify serverless functions. Use when creating API endpoints, background processing, scheduled tasks, or any server-side logic using Netlify Functions. Covers modern syntax (default export + Config), TypeScript, path routing, background functions, scheduled functions, streaming, and method routing.
---

# Netlify Functions

## Modern Syntax

Always use the modern default export + Config pattern. Never use the legacy `exports.handler` or named `handler` export.

```typescript
import type { Context, Config } from "@netlify/functions";

export default async (req: Request, context: Context) => {
  return new Response("Hello, world!");
};

export const config: Config = {
  path: "/api/hello",
};
```

The handler receives a standard Web API `Request` and returns a `Response`. The second argument is a Netlify `Context` object.

## File Structure

Place functions in `netlify/functions/`:

```
netlify/functions/
  _shared/           # Non-function shared code (underscore prefix)
    auth.ts
    db.ts
  items.ts           # -> /.netlify/functions/items (or custom path via config)
  users/index.ts     # -> /.netlify/functions/users
```

Use `.ts` or `.mts` extensions. If both `.ts` and `.js` exist with the same name, the `.js` file takes precedence.

## Path Routing

Define custom paths via the `config` export:

```typescript
export const config: Config = {
  path: "/api/items",                    // Static path
  // path: "/api/items/:id",            // Path parameter
  // path: ["/api/items", "/api/items/:id"], // Multiple paths
  // excludedPath: "/api/items/special", // Excluded paths
  // preferStatic: true,                // Don't override static files
};
```

Without a `path` config, functions are available at `/.netlify/functions/{name}`. Setting a `path` makes the function available **only** at that path.

Access path parameters via `context.params`:

```typescript
// config: { path: "/api/items/:id" }
export default async (req: Request, context: Context) => {
  const { id } = context.params;
  // ...
};
```

## Method Routing

```typescript
export default async (req: Request, context: Context) => {
  switch (req.method) {
    case "GET":    return handleGet(context.params.id);
    case "POST":   return handlePost(await req.json());
    case "DELETE": return handleDelete(context.params.id);
    default:       return new Response("Method not allowed", { status: 405 });
  }
};

export const config: Config = {
  path: "/api/items/:id",
  method: ["GET", "POST", "DELETE"],
};
```

## Background Functions

For long-running tasks (up to 15 minutes). The client receives an immediate `202` response; return values are ignored.

Name the file with a `-background` suffix:

```
netlify/functions/process-background.ts
```

Store results externally (Netlify Blobs, database) for later retrieval.

## Scheduled Functions

Run on a cron schedule (UTC timezone):

```typescript
export default async (req: Request) => {
  const { next_run } = await req.json();
  console.log("Next invocation at:", next_run);
};

export const config: Config = {
  schedule: "@hourly", // or cron: "0 * * * *"
};
```

Shortcuts: `@yearly`, `@monthly`, `@weekly`, `@daily`, `@hourly`. Scheduled functions have a **30-second timeout** and only run on published deploys.

## Streaming Responses

Return a `ReadableStream` body for streamed responses (up to 20 MB):

```typescript
export default async (req: Request) => {
  const stream = new ReadableStream({ /* ... */ });
  return new Response(stream, {
    headers: { "Content-Type": "text/event-stream" },
  });
};
```

## Context Object

| Property | Description |
|---|---|
| `context.params` | Path parameters from config |
| `context.geo` | `{ city, country: {code, name}, latitude, longitude, subdivision, timezone, postalCode }` |
| `context.ip` | Client IP address |
| `context.cookies` | `.get()`, `.set()`, `.delete()` |
| `context.deploy` | `{ context, id, published }` |
| `context.site` | `{ id, name, url }` |
| `context.account.id` | Team account ID |
| `context.requestId` | Unique request ID |
| `context.waitUntil(promise)` | Extend execution after response is sent |

## Environment Variables

Use `Netlify.env` (not `process.env`) inside functions:

```typescript
const apiKey = Netlify.env.get("API_KEY");
```

## Resource Limits

| Resource | Limit |
|---|---|
| Synchronous timeout | 60 seconds |
| Background timeout | 15 minutes |
| Scheduled timeout | 30 seconds |
| Memory | 1024 MB |
| Buffered payload | 6 MB |
| Streamed payload | 20 MB |

## Framework Considerations

Frameworks with server-side capabilities (Astro, Next.js, Nuxt, SvelteKit, TanStack Start) typically generate their own serverless functions via adapters. You usually do not write raw Netlify Functions in these projects — the framework adapter handles server-side rendering and API routes. Write Netlify Functions directly when:

- Using a client-side-only framework (Vite + React

================================================
FILE: skills\netlify-identity\SKILL.md
================================================
---
name: netlify-identity
description: Use when the task involves authentication, user signups, logins, password recovery, OAuth providers, role-based access control, or protecting routes and functions. Always use `@netlify/identity`. Never use `netlify-identity-widget` or `gotrue-js` — they are deprecated.
---

# Netlify Identity

Netlify Identity is a user management service for signups, logins, password recovery, user metadata, and role-based access control. It is built on [GoTrue](https://github.com/netlify/gotrue) and issues JSON Web Tokens (JWTs).

**Always use `@netlify/identity`.** Never use `netlify-identity-widget` or `gotrue-js` — they are deprecated. `@netlify/identity` provides a unified, headless TypeScript API that works in both browser and server contexts (Netlify Functions, Edge Functions, SSR frameworks).

## Setup

```bash
npm install @netlify/identity
```

Identity is automatically enabled when a deploy created by a Netlify Agent Runner session includes Identity code. Otherwise, it must be manually enabled in the UI. These are the default settings:

- **Registration** — Open (anyone can sign up). Change to Invite only in **Project configuration > Identity** if needed.
- **Autoconfirm** — Off (new signups require email confirmation). Enable in **Project configuration > Identity** to skip confirmation during development.

### Local Development

Identity does **not** currently work with `netlify dev`. You must deploy to Netlify to test Identity features. Use `npx netlify deploy` for preview deploys during development. This limitation may be resolved in a future release.

## Quick Start

Log in from the browser:

```typescript
import { login, getUser } from '@netlify/identity'

const user = await login('user@example.com', '<password>')
console.log(`Hello, ${user.name}`)

// Later, check auth state
const currentUser = await getUser()
```

Protect a Netlify Function:

```typescript
// netlify/functions/protected.mts
import { getUser } from '@netlify/identity'
import type { Context } from '@netlify/functions'

export default async (req: Request, context: Context) => {
  const user = await getUser()
  if (!user) return new Response('Unauthorized', { status: 401 })
  return Response.json({ id: user.id, email: user.email })
}
```

## Core API

Import and use headless functions directly:

```typescript
import {
  getUser,
  handleAuthCallback,
  login,
  logout,
  signup,
  oauthLogin,
  onAuthChange,
  getSettings,
} from '@netlify/identity'
```

### Login

```typescript
import { login, AuthError } from '@netlify/identity'

async function handleLogin(email: string, password: string) {
  try {
    const user = await login(email, password)
    showSuccess(`Welcome back, ${user.name ?? user.email}`)
  } catch (error) {
    if (error instanceof AuthError) {
      showError(error.status === 401 ? 'Invalid email or password.' : error.message)
    }
  }
}
```

### Signup

After signup, check `user.emailVerified` to determine if the user was auto-confirmed or needs to confirm their email.

```typescript
import { signup, AuthError } from '@netlify/identity'

async function handleSignup(email: string, password: string, name: string) {
  try {
    const user = await signup(email, password, { full_name: name })
    if (user.emailVerified) {
      // Autoconfirm ON — user is logged in immediately
      showSuccess('Account created. You are now logged in.')
    } else {
      // Autoconfirm OFF — confirmation email sent
      showSuccess('Check your email to confirm your account.')
    }
  } catch (error) {
    if (error instanceof AuthError) {
      showError(error.status === 403 ? 'Signups are not allowed.' : error.message)
    }
  }
}
```

### Logout

```typescript
import { logout } from '@netlify/identity'

await logout()
```

### OAuth

OAuth is a two-step flow: `oauthLogin(provider)` redirects away from the site, then `handleAuthCallback()` processes the redirect when the user returns.

```typescript
import { oauthLogin } from '@netlify/identity'

// Step 1: Redirect to provider (navigates away — never returns)
function handleOAuthClick(provider: 'google' | 'github' | 'gitlab' | 'bitbucket') {
  oauthLogin(provider)
}
```

Enable providers in **Project configuration > Identity > External providers** before using OAuth.

### Handling Callbacks

Always call `handleAuthCallback()` on page load in any app that uses OAuth, password recovery, invites, or email confirmation. It processes all callback types via the URL hash.

```typescript
import { handleAuthCallback, AuthError } from '@netlify/identity'

async function processCallback() {
  try {
    const result = await handleAuthCallback()
    if (!result) return // No callback hash — normal page load

    switch (result.type) {
      case 'oauth':
        showSuccess(`Logged in as ${result.user?.email}`)
        break
      case 'confirmation':
        showSuccess('Email confirmed. You are now logged in.')
        break
      case 'recovery':
        // User

================================================
FILE: skills\netlify-identity\references\advanced-patterns.md
================================================
# Advanced Identity Patterns

## Password Recovery

Three-step flow: request recovery email, handle the callback, then set a new password.

```typescript
import { requestPasswordRecovery, handleAuthCallback, updateUser, AuthError } from '@netlify/identity'

// Step 1: Send recovery email
async function handleForgotPassword(email: string) {
  try {
    await requestPasswordRecovery(email)
    showSuccess('Check your email for a password reset link.')
  } catch (error) {
    if (error instanceof AuthError) showError(error.message)
  }
}

// Step 2: handleAuthCallback() returns { type: 'recovery', user } — show password reset form
// (See the handleAuthCallback switch in SKILL.md)

// Step 3: Set new password
async function handlePasswordReset(newPassword: string) {
  try {
    await updateUser({ password: newPassword })
    showSuccess('Password updated.')
  } catch (error) {
    if (error instanceof AuthError) showError(error.message)
  }
}
```

The recovery callback fires a `'recovery'` auth event, not `'login'`. The user is authenticated but should be prompted to set a new password before navigating away.

## Invite Acceptance

When a user clicks an invite link, `handleAuthCallback()` returns `{ type: 'invite', user: null, token }`. Use the token to accept the invite and set a password.

```typescript
import { acceptInvite, AuthError } from '@netlify/identity'

async function handleAcceptInvite(token: string, password: string) {
  try {
    const user = await acceptInvite(token, password)
    showSuccess(`Welcome, ${user.email}! Your account is ready.`)
  } catch (error) {
    if (error instanceof AuthError) showError(error.message)
  }
}
```

## Email Change

When a user verifies an email change, `handleAuthCallback()` returns `{ type: 'email_change', user }`. The user must be logged in when clicking the verification link.

```typescript
import { verifyEmailChange, AuthError } from '@netlify/identity'

async function handleEmailChangeVerification(token: string) {
  try {
    const user = await verifyEmailChange(token)
    showSuccess(`Email updated to ${user.email}`)
  } catch (error) {
    if (error instanceof AuthError) showError(error.message)
  }
}
```

## Session Hydration

`hydrateSession()` bridges server-set cookies to the browser session. Call it on page load when using server-side login (e.g., login inside a Netlify Function followed by a redirect).

```typescript
import { hydrateSession } from '@netlify/identity'

const user = await hydrateSession()
if (user) {
  // Browser session is now in sync with server-set cookies
}
```

`getUser()` auto-hydrates from the `nf_jwt` cookie if no browser session exists, so explicit `hydrateSession()` is only needed when you want to restore the full session (including token refresh timers) after a server-side login.

## SSR Integration Patterns

For SSR frameworks, the recommended pattern is:

- **Browser-side** for auth mutations: `login()`, `signup()`, `logout()`, `oauthLogin()`
- **Server-side** for reading auth state: `getUser()`, `getSettings()`, `getIdentityConfig()`

Browser-side auth mutations set the `nf_jwt` cookie and localStorage, and emit `onAuthChange` events. The server reads the cookie on the next request.

The library also supports server-side mutations (`login()`, `signup()`, `logout()` inside Netlify Functions), but these require the Netlify Functions runtime to set cookies. After a server-side mutation, use a full page navigation so the browser sends the new cookie.

Always use `window.location.href` (not framework router navigation) after server-side auth mutations in Next.js, TanStack Start, and SvelteKit. Remix `redirect()` is safe because Remix actions return real HTTP responses.

## Full API Reference

For the complete API reference — all function signatures, type definitions, OAuth helpers, admin operations, session management, auth events, and framework-specific examples — read the package README:

```
node_modules/@netlify/identity/README.md
```

The README is shipped with the npm package and is always in sync with the installed version.


================================================
FILE: skills\netlify-image-cdn\SKILL.md
================================================
---
name: netlify-image-cdn
description: Guide for using Netlify Image CDN for image optimization and transformation. Use when serving optimized images, creating responsive image markup, setting up user-uploaded image pipelines, or configuring image transformations. Covers the /.netlify/images endpoint, query parameters, remote image allowlisting, clean URL rewrites, and composing uploads with Functions + Blobs.
---

# Netlify Image CDN

Every Netlify site has a built-in `/.netlify/images` endpoint for on-the-fly image transformation. No configuration required for local images.

## Basic Usage

```html
<img src="/.netlify/images?url=/photo.jpg&w=800&h=600&fit=cover&q=80" />
```

## Query Parameters

| Param | Description | Values |
|---|---|---|
| `url` | Source image path (required) | Relative path or absolute URL |
| `w` | Width in pixels | Any positive integer |
| `h` | Height in pixels | Any positive integer |
| `fit` | Resize behavior | `contain` (default), `cover`, `fill` |
| `position` | Crop alignment (with `cover`) | `center` (default), `top`, `bottom`, `left`, `right` |
| `fm` | Output format | `avif`, `webp`, `jpg`, `png`, `gif`, `blurhash` |
| `q` | Quality (lossy formats) | 1-100 (default: 75) |

When `fm` is omitted, Netlify auto-negotiates the best format based on browser support (preferring `webp`, then `avif`).

## Remote Image Allowlisting

External images must be explicitly allowed in `netlify.toml`:

```toml
[images]
remote_images = ["https://example\\.com/.*", "https://cdn\\.images\\.com/.*"]
```

Values are regex patterns.

## Clean URL Rewrites

Create user-friendly image URLs with redirects:

```toml
# Basic optimization
[[redirects]]
from = "/img/*"
to = "/.netlify/images?url=/:splat"
status = 200

# Preset: thumbnail
[[redirects]]
from = "/img/thumb/:key"
to = "/.netlify/images?url=/uploads/:key&w=150&h=150&fit=cover"
status = 200

# Preset: hero
[[redirects]]
from = "/img/hero/:key"
to = "/.netlify/images?url=/uploads/:key&w=1200&h=675&fit=cover"
status = 200
```

## Caching

- Transformed images are cached at the CDN edge automatically
- Cache invalidates on new deploys
- Set cache headers on source images to control caching:

```toml
[[headers]]
for = "/uploads/*"
[headers.values]
Cache-Control = "public, max-age=31536000, immutable"
```

## User-Uploaded Images

Combine **Netlify Functions** (upload handler) + **Netlify Blobs** (storage) + **Image CDN** (serving/transforming) to build a complete user-uploaded image pipeline. See references/user-uploads.md for the full pattern.


================================================
FILE: skills\netlify-image-cdn\references\user-uploads.md
================================================
# User-Uploaded Images Pipeline

Compose Netlify Functions (upload handler) + Netlify Blobs (storage) + Image CDN (serving/transforming) to build a complete user-uploaded image pipeline.

## Architecture

1. **Upload** — A Netlify Function receives multipart form data, validates, and stores in Blobs
2. **Storage** — Netlify Blobs stores the binary image with metadata
3. **Serve** — A Netlify Function retrieves the blob and serves it at `/uploads/:key`
4. **Transform** — A redirect maps `/img/:key` to `/.netlify/images?url=/uploads/:key` for CDN optimization

## Dependencies

```bash
npm install @netlify/blobs
```

## Upload Handler

```typescript
// netlify/functions/upload.ts
import type { Context, Config } from "@netlify/functions";
import { getStore } from "@netlify/blobs";
import { randomUUID } from "crypto";

const ALLOWED_TYPES = ["image/jpeg", "image/png", "image/gif", "image/webp"];
const MAX_SIZE = 4 * 1024 * 1024; // 4 MB

export default async (req: Request, context: Context) => {
  if (req.method !== "POST") {
    return new Response("Method not allowed", { status: 405 });
  }

  const formData = await req.formData();
  const image = formData.get("image") as File;

  if (!image) return Response.json({ error: "No image provided" }, { status: 400 });
  if (!ALLOWED_TYPES.includes(image.type)) return Response.json({ error: "Invalid type" }, { status: 400 });
  if (image.size > MAX_SIZE) return Response.json({ error: "File too large" }, { status: 400 });

  const extension = image.name.split(".").pop() || "jpg";
  const key = `${randomUUID()}.${extension}`;
  const store = getStore({ name: "images", consistency: "strong" });

  await store.set(key, image, {
    metadata: {
      contentType: image.type,
      originalFilename: image.name,
      uploadedAt: new Date().toISOString(),
    },
  });

  return Response.json({ success: true, key, url: `/img/${key}` });
};

export const config: Config = { path: "/api/upload", method: "POST" };
```

## Serve Handler

```typescript
// netlify/functions/serve-image.ts
import type { Context, Config } from "@netlify/functions";
import { getStore } from "@netlify/blobs";

export default async (req: Request, context: Context) => {
  const key = context.params.key;
  const store = getStore({ name: "images", consistency: "strong" });

  const result = await store.getWithMetadata(key, { type: "stream" });
  if (!result) return new Response("Not found", { status: 404 });

  return new Response(result.data, {
    headers: {
      "Content-Type": result.metadata?.contentType || "image/jpeg",
      "Cache-Control": "public, max-age=31536000, immutable",
    },
  });
};

export const config: Config = { path: "/uploads/:key" };
```

## CDN Redirect

```toml
# netlify.toml

# Basic optimized URL
[[redirects]]
from = "/img/:key"
to = "/.netlify/images?url=/uploads/:key"
status = 200

# Thumbnail preset
[[redirects]]
from = "/img/thumb/:key"
to = "/.netlify/images?url=/uploads/:key&w=150&h=150&fit=cover"
status = 200

# Hero preset
[[redirects]]
from = "/img/hero/:key"
to = "/.netlify/images?url=/uploads/:key&w=1200&h=675&fit=cover"
status = 200
```

## Client-Side Upload (React Example)

```tsx
function ImageUpload({ onUpload }: { onUpload: (url: string) => void }) {
  const handleChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("image", file);

    const res = await fetch("/api/upload", { method: "POST", body: formData });
    const { url } = await res.json();
    onUpload(url);
  };

  return <input type="file" accept="image/*" onChange={handleChange} />;
}
```

## Astro Upload (API Route)

```typescript
// src/pages/api/upload.ts
import type { APIRoute } from "astro";
import { getStore } from "@netlify/blobs";
import { randomUUID } from "crypto";

export const POST: APIRoute = async ({ request, redirect }) => {
  const formData = await request.formData();
  const image = formData.get("image") as File;
  if (!image) return new Response("No image", { status: 400 });

  const key = `${randomUUID()}.${image.name.split(".").pop() || "jpg"}`;
  const store = getStore({ name: "images", consistency: "strong" });
  await store.set(key, image, {
    metadata: { contentType: image.type, originalFilename: image.name },
  });

  return redirect(`/gallery?uploaded=${key}`);
};
```

## Key Points

- Always validate file type and size on the server (client validation can be bypassed)
- Use `strong` consistency on Blobs for immediate reads after writes
- The serve handler's `Cache-Control: immutable` means the CDN caches the raw image permanently — Image CDN transformations layer on top
- Without `fm` parameter, Netlify auto-serves AVIF or WebP based on browser support

```

## File: .claude-plugin\marketplace.json
```
{
  "name": "netlify-context-and-tools",
  "owner": {
    "name": "Netlify"
  },
  "plugins": [
    {
      "name": "netlify-skills",
      "description": "Netlify platform skills — functions, edge functions, blobs, database, identity, image CDN, forms, config, CLI, frameworks, caching, AI gateway, and deployment",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/netlify-functions",
        "./skills/netlify-edge-functions",
        "./skills/netlify-blobs",
        "./skills/netlify-db",
        "./skills/netlify-image-cdn",
        "./skills/netlify-forms",
        "./skills/netlify-frameworks",
        "./skills/netlify-caching",
        "./skills/netlify-config",
        "./skills/netlify-cli-and-deploy",
        "./skills/netlify-deploy",
        "./skills/netlify-ai-gateway",
        "./skills/netlify-identity"
      ]
    }
  ]
}

```

## File: .claude-plugin\plugin.json
```
{
  "name": "netlify-skills",
  "version": "1.1.0",
  "description": "Netlify platform skills for Claude Code",
  "author": {
    "name": "Netlify"
  },
  "repository": "https://github.com/netlify/context-and-tools"
}

```

## File: .cursor-plugin\plugin.json
```
{
  "name": "netlify-skills",
  "version": "1.1.0",
  "description": "Netlify platform skills — functions, edge functions, blobs, database, identity, image CDN, forms, config, CLI, frameworks, caching, AI gateway, and deployment",
  "author": {
    "name": "Netlify"
  },
  "homepage": "https://www.netlify.com",
  "repository": "https://github.com/netlify/context-and-tools",
  "keywords": [
    "netlify",
    "deployment",
    "serverless",
    "edge-functions",
    "cdn",
    "hosting",
    "jamstack",
    "functions"
  ],
  "rules": "cursor/rules"
}

```

## File: .github\workflows\build-codex-skills.yml
```
name: Build Codex skills

on:
  push:
    branches: [main]
    paths:
      - "skills/**"
      - "scripts/build-codex-skills.sh"
  pull_request:
    paths:
      - "skills/**"
      - "scripts/build-codex-skills.sh"

permissions:
  contents: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          ref: ${{ github.head_ref || github.ref }}

      - name: Build Codex skills from source
        run: bash scripts/build-codex-skills.sh

      - name: Commit updated Codex skills
        if: github.event_name == 'push' && github.ref == 'refs/heads/main'
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add codex/
          if git diff --cached --quiet; then
            echo "No changes to Codex skills"
          else
            git commit -m "chore: Rebuild Codex skills from source [skip ci]"
            git push
          fi

```

## File: .github\workflows\build-cursor-rules.yml
```
name: Build Cursor rules

on:
  push:
    branches: [main]
    paths:
      - "skills/**"
      - "scripts/build-cursor-rules.sh"
  pull_request:
    paths:
      - "skills/**"
      - "scripts/build-cursor-rules.sh"

permissions:
  contents: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          ref: ${{ github.head_ref || github.ref }}

      - name: Build Cursor rules from skills
        run: bash scripts/build-cursor-rules.sh

      - name: Commit updated Cursor rules
        if: github.event_name == 'push' || github.event_name == 'pull_request'
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add cursor/rules/
          if git diff --cached --quiet; then
            echo "No changes to Cursor rules"
          else
            git commit -m "chore: Rebuild Cursor rules from skills [skip ci]"
            git push
          fi

```

## File: .github\workflows\validate-skills.yml
```
name: Validate Skills
on:
  pull_request:
    paths:
      - "skills/**"

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install skill-validator
        run: |
          brew install agent-ecosystem/tap/skill-validator

      - name: Validate skills
        run: |
          skill-validator check --strict --emit-annotations skills/
          skill-validator check --strict -o markdown skills/ >> "$GITHUB_STEP_SUMMARY"

```

## File: codex\agents.md
```
# Netlify Skills

This project deploys on Netlify. Use these skills for guidance on Netlify platform primitives. Each skill provides specific, factual reference for working with a Netlify feature.

## When to Use Each Skill

**Building API endpoints or server-side logic?**
Read `$netlify-functions` for modern function syntax, routing, background/scheduled functions.

**Need low-latency middleware, geo-based logic, or request manipulation?**
Read `$netlify-edge-functions` for edge compute patterns.

**Storing files, images, or simple key-value data?**
Read `$netlify-blobs` for object storage API.

**Need a relational database?**
Read `$netlify-db` for Neon Postgres setup, Drizzle ORM, and migrations. It also covers when Blobs is a better fit.

**Optimizing or transforming images?**
Read `$netlify-image-cdn` for the image transformation endpoint and clean URL patterns. For user-uploaded images, see `$netlify-image-cdn/references/user-uploads.md`.

**Adding HTML forms?**
Read `$netlify-forms` for form detection, AJAX submissions, spam filtering, and file uploads.

**Configuring netlify.toml (redirects, headers, build settings)?**
Read `$netlify-config` for the complete configuration reference.

**Deploying, managing env vars, or running local dev?**
Read `$netlify-cli-and-deploy` for CLI commands, Git vs manual deploys, and environment variable management.

**Setting up a framework (Vite, Astro, TanStack, Next.js)?**
Read `$netlify-frameworks` for adapter/plugin setup. Framework-specific details are in `$netlify-frameworks`.

**Controlling CDN caching behavior?**
Read `$netlify-caching` for cache headers, stale-while-revalidate, cache tags, and purge.

**Adding AI capabilities or choosing an AI model?**
Read `$netlify-ai-gateway` for AI Gateway setup, supported models, and provider SDKs.

**Adding user authentication, signups, logins, or access control?**
Read `$netlify-identity` for Netlify Identity setup, OAuth, role-based access, and protecting routes and functions.

**Deploying a site to Netlify?**
Read `$netlify-deploy` for the full deployment workflow — authentication, site linking, preview and production deploys.

## General Rules

- Use `Netlify.env.get("VAR")` for environment variables in functions (not `process.env`)
- Never hardcode secrets — use Netlify environment variables
- Add `.netlify` to `.gitignore`
- For framework-specific patterns, check the framework reference before writing custom Netlify Functions — the adapter may handle it

```

## File: context\steering\netlify-deployment-power\power.md
```
---
name: "netlify-deployment"
displayName: "Netlify Deployment"
description: "Deploy and manage websites on Netlify using CLI-first workflow with netlify.toml configuration"
keywords: ["netlify", "deploy", "hosting", "cli", "deployment", "web", "static-site"]
author: "Netlify"
---

Netlify Deployment (CLI-First)
==============================

> Use this file whenever you are asked to deploy or update a site on Netlify. **Default behavior:** prefer the Netlify CLI

1\. Defaults & Principles
-------------------------

*   Prefer **Netlify CLI** as the primary deployment method.
*   Use a netlify.toml file for consistent build and publish configuration.
*   Never hardcode secrets; always use **Netlify environment variables**.
*   For framework-specific details, reference official Netlify docs (via llms.txt) rather than inventing new patterns.

2\. netlify.toml Basics
-----------------------

```
[build]
  command = "BUILD_COMMAND"
  publish = "PUBLISH_DIRECTORY"
```

*   Adjust publish to match the actual output directory.
*   Use SPA redirect only for client-side routed apps.
*   Do not include secrets.
    

3\. Deploy with Netlify CLI (Preferred)
---------------------------------------

### Install & Authenticate

```
npm install -g netlify-cli

# will tell you linked status and user status
netlify status

#only if the user is not logged in
netlify login 
```

### Link or Create a Site

Determine if the site is linked to an existing Netlify account with `netlify status`

Skip this step if it is already linked.

If not already linked:
1. determine if it is git based
   1.a. if it is git based, use `git remote show origin` to find the git remote url like "https://github.com/orgname/reponame"
   1.b. see if the site already exists on their account with `netlify link --git-remote-url REMOTE_URL`
   1.c. if the site is not found then we must create it.
2. if site is unknown, create a new site use `netlify init` and let the user walk through the steps


### Dependencies

Confirm that all dependencies have been installed. (e.g. `npm install`)

### Deploy

If the user created a new site, then do a production deploy. If this is linking an existing site, we must create a preview/non-production deploy unless the user expclitly asked for this.

non-production deploy:
`netlify deploy`

production deploy:
`netlify deploy --prod`

    
4\. Troubleshooting Basics
--------------------------

*   Check Netlify build logs for errors.
*   Confirm correct build command and publish directory.
*   Verify required environment variables exist.

```

## File: skills\claude.md
```
# Netlify Skills

This project deploys on Netlify. Use these skills for guidance on Netlify platform primitives. Each skill provides specific, factual reference for working with a Netlify feature.

## When to Use Each Skill

**Building API endpoints or server-side logic?**
Read `netlify-functions/SKILL.md` for modern function syntax, routing, background/scheduled functions.

**Need low-latency middleware, geo-based logic, or request manipulation?**
Read `netlify-edge-functions/SKILL.md` for edge compute patterns.

**Storing files, images, or simple key-value data?**
Read `netlify-blobs/SKILL.md` for object storage API.

**Need a relational database?**
Read `netlify-db/SKILL.md` for Neon Postgres setup, Drizzle ORM, and migrations. It also covers when Blobs is a better fit.

**Optimizing or transforming images?**
Read `netlify-image-cdn/SKILL.md` for the image transformation endpoint and clean URL patterns. For user-uploaded images, see `netlify-image-cdn/references/user-uploads.md`.

**Adding HTML forms?**
Read `netlify-forms/SKILL.md` for form detection, AJAX submissions, spam filtering, and file uploads.

**Configuring netlify.toml (redirects, headers, build settings)?**
Read `netlify-config/SKILL.md` for the complete configuration reference.

**Deploying, managing env vars, or running local dev?**
Read `netlify-cli-and-deploy/SKILL.md` for CLI commands, Git vs manual deploys, and environment variable management.

**Setting up a framework (Vite, Astro, TanStack, Next.js)?**
Read `netlify-frameworks/SKILL.md` for adapter/plugin setup. Framework-specific details are in `netlify-frameworks/references/`.

**Controlling CDN caching behavior?**
Read `netlify-caching/SKILL.md` for cache headers, stale-while-revalidate, cache tags, and purge.

**Adding AI capabilities or choosing an AI model?**
Read `netlify-ai-gateway/SKILL.md` for AI Gateway setup, supported models, and provider SDKs.

**Adding user authentication, signups, logins, or access control?**
Read `netlify-identity/SKILL.md` for Netlify Identity setup, OAuth, role-based access, and protecting routes and functions.

**Deploying a site to Netlify?**
Read `netlify-deploy/SKILL.md` for the full deployment workflow — authentication, site linking, preview and production deploys.

## General Rules

- Use `Netlify.env.get("VAR")` for environment variables in functions (not `process.env`)
- Never hardcode secrets — use Netlify environment variables
- Add `.netlify` to `.gitignore`
- For framework-specific patterns, check the framework reference before writing custom Netlify Functions — the adapter may handle it

```

## File: skills\netlify-ai-gateway\SKILL.md
```
---
name: netlify-ai-gateway
description: Guide for using Netlify AI Gateway to access AI models. Use when adding AI capabilities or selecting/changing AI models. Must be read before choosing a model. Covers supported providers (OpenAI, Anthropic, Google), SDK setup, environment variables, and the list of available models.
---

# Netlify AI Gateway

> **IMPORTANT:** Only use models listed in the "Available Models" section below. AI Gateway does not support every model a provider offers. Using an unsupported model will cause runtime errors.

Netlify AI Gateway provides access to AI models from multiple providers without managing API keys directly. It is available on all Netlify sites.

## How It Works

The AI Gateway acts as a proxy — you use standard provider SDKs (OpenAI, Anthropic, Google) but point them at Netlify's gateway URL instead of the provider's API. Netlify handles authentication, rate limiting, and monitoring.

## Setup

1. Enable AI on your site in the Netlify UI
2. The environment variable `OPENAI_BASE_URL` is set automatically by Netlify
3. Install the provider SDK you want to use

No provider API keys are needed — Netlify's gateway handles authentication.

## Using OpenAI SDK

```bash
npm install openai
```

```typescript
import OpenAI from "openai";

const openai = new OpenAI();
// OPENAI_BASE_URL is auto-configured — no API key or base URL needed

const completion = await openai.chat.completions.create({
  model: "gpt-4o-mini",
  messages: [{ role: "user", content: "Hello!" }],
});
```

## Using Anthropic SDK

```bash
npm install @anthropic-ai/sdk
```

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  baseURL: Netlify.env.get("ANTHROPIC_BASE_URL"),
});

const message = await client.messages.create({
  model: "claude-sonnet-4-5-20250929",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello!" }],
});
```

## Using Google AI SDK

```bash
npm install @google/generative-ai
```

```typescript
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("placeholder");
// Configure base URL via environment variable

const model = genAI.getGenerativeModel({ model: "gemini-2.5-flash" });
const result = await model.generateContent("Hello!");
```

## In a Netlify Function

```typescript
import type { Config, Context } from "@netlify/functions";
import OpenAI from "openai";

export default async (req: Request, context: Context) => {
  const { prompt } = await req.json();
  const openai = new OpenAI();

  const completion = await openai.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [{ role: "user", content: prompt }],
  });

  return Response.json({
    response: completion.choices[0].message.content,
  });
};

export const config: Config = {
  path: "/api/ai",
  method: "POST",
};
```

## Environment Variables

| Variable | Provider | Set by |
|---|---|---|
| `OPENAI_BASE_URL` | OpenAI | Netlify (automatic) |
| `ANTHROPIC_BASE_URL` | Anthropic | Netlify (automatic) |

These are configured automatically when AI is enabled on the site. No manual setup required.

## Local Development

With `@netlify/vite-plugin` or `netlify dev`, gateway environment variables are injected automatically. The AI Gateway is accessible during local development after the site has been deployed at least once.

## Available Models

For the list of supported models, see https://docs.netlify.com/build/ai-gateway/overview/.

```

## File: skills\netlify-blobs\SKILL.md
```
---
name: netlify-blobs
description: Guide for using Netlify Blobs object storage. Use when storing files, images, documents, or simple key-value data without a full database. Covers getStore(), CRUD operations, metadata, listing, deploy-scoped vs site-scoped stores, and local development.
---

# Netlify Blobs

Netlify Blobs is zero-config object storage available from any Netlify compute (functions, edge functions, framework server routes). No provisioning required.

```bash
npm install @netlify/blobs
```

## Getting a Store

```typescript
import { getStore } from "@netlify/blobs";

const store = getStore({ name: "my-store" });

// Use "strong" consistency when you need immediate reads after writes
const store = getStore({ name: "my-store", consistency: "strong" });
```

## CRUD Operations

These are the **only** store methods. Do not invent others.

### Create / Update

```typescript
// String or binary data
await store.set("key", "value");
await store.set("key", fileBuffer);

// With metadata
await store.set("key", data, {
  metadata: { contentType: "image/png", uploadedAt: new Date().toISOString() },
});

// JSON data
await store.setJSON("key", { name: "Example", count: 42 });
```

### Read

```typescript
// Text (default)
const text = await store.get("key");                    // string | null

// Typed retrieval
const json = await store.get("key", { type: "json" });  // object | null
const stream = await store.get("key", { type: "stream" });
const blob = await store.get("key", { type: "blob" });
const buffer = await store.get("key", { type: "arrayBuffer" });

// With metadata
const result = await store.getWithMetadata("key");
// { data: any, etag: string, metadata: object } | null

// Metadata only (no data download)
const meta = await store.getMetadata("key");
// { etag: string, metadata: object } | null
```

### Delete

```typescript
await store.delete("key");
```

### List

```typescript
const { blobs } = await store.list();
// blobs: [{ etag: string, key: string }, ...]

// Filter by prefix
const { blobs } = await store.list({ prefix: "uploads/" });
```

## Store Types

- **Site-scoped** (`getStore()`): Persist across all deploys. Use for most cases.
- **Deploy-scoped** (`getDeployStore()`): Tied to a specific deploy lifecycle.

## Limits

| Limit | Value |
|---|---|
| Max object size | 5 GB |
| Store name max length | 64 bytes |
| Key max length | 600 bytes |

## Local Development

Local dev uses a sandboxed store (separate from production). For Vite-based projects, install `@netlify/vite-plugin` to enable local Blobs access. Otherwise, use `netlify dev`.

**Common error**: "The environment has not been configured to use Netlify Blobs" — install `@netlify/vite-plugin` or run via `netlify dev`.

```

## File: skills\netlify-caching\SKILL.md
```
---
name: netlify-caching
description: Guide for controlling caching on Netlify's CDN. Use when configuring cache headers, setting up stale-while-revalidate, implementing on-demand cache purge, or understanding Netlify's CDN caching behavior. Covers Cache-Control, Netlify-CDN-Cache-Control, cache tags, durable cache, and framework-specific caching patterns.
---

# Caching on Netlify

## Default Behavior

**Static assets** are cached automatically:
- CDN: cached for 1 year, invalidated on every deploy
- Browser: always revalidates (`max-age=0, must-revalidate`)
- No configuration needed

**Dynamic responses** (functions, edge functions, proxied) are **not cached by default**. Add cache headers explicitly.

## Cache-Control Headers

Three headers control caching, from most to least specific:

| Header | Who sees it | Use case |
|---|---|---|
| `Netlify-CDN-Cache-Control` | Netlify CDN only (stripped before browser) | CDN-only caching |
| `CDN-Cache-Control` | All CDN caches (stripped before browser) | Multi-CDN setups |
| `Cache-Control` | Browser and all caches | General caching |

### Common Patterns

```typescript
// Cache at CDN for 1 hour, browser always revalidates
return new Response(body, {
  headers: {
    "Netlify-CDN-Cache-Control": "public, s-maxage=3600, must-revalidate",
    "Cache-Control": "public, max-age=0, must-revalidate",
  },
});

// Stale-while-revalidate (serve stale for 2 min while refreshing)
return new Response(body, {
  headers: {
    "Netlify-CDN-Cache-Control": "public, max-age=60, stale-while-revalidate=120",
  },
});

// Durable cache (shared across edge nodes, serverless functions only)
return new Response(body, {
  headers: {
    "Netlify-CDN-Cache-Control": "public, durable, max-age=60, stale-while-revalidate=120",
  },
});
```

### Immutable Assets

For fingerprinted files (hash in filename):

```toml
# netlify.toml
[[headers]]
for = "/assets/*"
[headers.values]
Cache-Control = "public, max-age=31536000, immutable"
```

## Cache Tags and On-Demand Purge

Tag responses for selective cache invalidation:

```typescript
return new Response(body, {
  headers: {
    "Netlify-Cache-ID": "product,listing",
    "Netlify-CDN-Cache-Control": "public, s-maxage=86400",
  },
});
```

Purge by tag:

```typescript
import { purgeCache } from "@netlify/functions";

export default async () => {
  await purgeCache({ tags: ["product"] });
  return new Response("Purged", { status: 202 });
};
```

Purge entire site:

```typescript
await purgeCache();
```

Responses with `Netlify-Cache-ID` are **excluded from automatic deploy-based invalidation** — they must be purged explicitly.

## Cache Key Variation

Customize what creates separate cache entries:

```typescript
return new Response(body, {
  headers: {
    "Netlify-Vary": "cookie=ab_test|is_logged_in",
    // Other options: query=param1|param2, header=X-Custom, country=us|de, language=en|fr
  },
});
```

## Framework-Specific Caching

### Next.js
ISR uses Netlify's durable cache automatically (runtime 5.5.0+). `revalidatePath` and `revalidateTag` trigger cache purge.

### Astro / Remix
Full control over cache headers in server routes. Set `Netlify-CDN-Cache-Control` in responses for CDN caching.

### Nuxt
Default Nitro preset handles caching. ISR-style patterns use `routeRules` with `swr` or `isr` options.

### Vite SPA
Static assets are cached by default. API responses from Netlify Functions need explicit cache headers.

## Debugging

Check the `Cache-Status` response header:
- `HIT` — served from cache
- `MISS` — generated fresh
- `REVALIDATED` — stale content was revalidated

## Constraints

- Basic auth disables caching for the entire site
- Durable cache is serverless functions only (not edge functions)
- Same URL must return identical `Netlify-Vary` headers across responses
- Deploy invalidation is scoped to deploy context (production vs preview)

```

## File: skills\netlify-cli-and-deploy\SKILL.md
```
---
name: netlify-cli-and-deploy
description: Guide for using the Netlify CLI and deploying sites. Use when installing the CLI, linking sites, deploying (Git-based or manual), managing environment variables, or running local development. Covers netlify dev, netlify deploy, Git vs non-Git workflows, and environment variable management.
---

# Netlify CLI and Deployment

## Installation

```bash
npm install -g netlify-cli    # Global (for local dev)
npm install netlify-cli -D    # Local (for CI)
```

Requires Node.js 18.14.0+.

## Authentication

```bash
netlify login       # Opens browser for OAuth
netlify status      # Check auth + linked site status
```

For CI, set `NETLIFY_AUTH_TOKEN` environment variable instead.

## Linking a Site

Check if already linked with `netlify status`. If not:

```bash
# Interactive
netlify link

# By Git remote (if using Git)
netlify link --git-remote-url https://github.com/org/repo

# Create new site
netlify init           # With Git CI/CD setup
netlify init --manual  # Without Git CI/CD
```

Site ID is stored in `.netlify/state.json`. Add `.netlify` to `.gitignore`.

## Deploying

### Git-Based Deploys (Continuous Deployment)

Set up with `netlify init`. Automatic deploys trigger on push/PR:
- Push to production branch → production deploy
- Open PR → deploy preview with unique URL
- Push to other branches → branch deploy

Build runs on Netlify's servers. Configure build settings in `netlify.toml`.

### Manual / Local Deploys (No Git Required)

Build locally, then upload:

```bash
netlify deploy          # Draft deploy (preview URL)
netlify deploy --prod   # Production deploy
netlify deploy --dir=dist  # Specify output directory
```

This works without Git — useful for prototypes, local-only projects, or CI pipelines.

## Local Development

### Option 1: netlify dev

```bash
netlify dev
```

Wraps your framework's dev server and provides:
- Environment variable injection
- Functions and edge functions
- Redirects and headers processing

### Option 2: Netlify Vite Plugin (Vite-based projects)

For projects using Vite (React SPA, TanStack Start, SvelteKit, Remix), the Vite plugin provides Netlify platform primitives directly in the framework's dev server:

```bash
npm install @netlify/vite-plugin
```

```typescript
// vite.config.ts
import netlify from "@netlify/vite-plugin";
export default defineConfig({ plugins: [netlify()] });
```

Then run your normal dev command (`npm run dev`) — no `netlify dev` wrapper needed. This gives you access to Blobs, DB, Functions, and environment variables during development.

See the **netlify-frameworks** skill for framework-specific local dev guidance.

## Environment Variables

### CLI Management

```bash
# Set
netlify env:set API_KEY "value"
netlify env:set API_KEY "value" --secret              # Hidden from logs
netlify env:set API_KEY "value" --context production   # Context-specific

# Get
netlify env:get API_KEY

# List
netlify env:list
netlify env:list --plain > .env                        # Export to file

# Import from file
netlify env:import .env

# Delete
netlify env:unset API_KEY
```

### Context Scoping

Variables can be scoped to deploy contexts:

```bash
netlify env:set API_URL "https://api.prod.com" --context production
netlify env:set API_URL "https://api.staging.com" --context deploy-preview
netlify env:set DEBUG "true" --context branch:feature-x
```

### Accessing in Code

- **Server-side (Functions)**: Use `Netlify.env.get("VAR")` (preferred) or `process.env.VAR`
- **Client-side (Vite)**: Only `VITE_`-prefixed vars via `import.meta.env.VITE_VAR`
- **Client-side (Astro)**: Only `PUBLIC_`-prefixed vars via `import.meta.env.PUBLIC_VAR`

**Never use `VITE_` or `PUBLIC_` prefix for secrets** — these are exposed to the browser.

## Useful Commands

| Command | Description |
|---|---|
| `netlify status` | Auth and site link status |
| `netlify dev` | Start local dev server |
| `netlify build` | Run build locally (mimics Netlify environment) |
| `netlify deploy` | Draft deploy |
| `netlify deploy --prod` | Production deploy |
| `netlify dev:exec <cmd>` | Run command with Netlify environment loaded |
| `netlify env:list` | List environment variables |
| `netlify clone org/repo` | Clone, link, and set up in one step |

```

## File: skills\netlify-config\SKILL.md
```
---
name: netlify-config
description: Reference for netlify.toml configuration. Use when configuring build settings, redirects, rewrites, headers, deploy contexts, environment variables, or any site-level configuration. Covers the complete netlify.toml syntax including redirects with splats/conditions, headers, deploy contexts, functions config, and edge functions config.
---

# Netlify Configuration (netlify.toml)

Place `netlify.toml` at the repository root (or at the base directory for monorepos).

## Build Settings

```toml
[build]
  base = "project/"          # Base directory (default: root)
  command = "npm run build"  # Build command
  publish = "dist/"          # Output directory
```

## Redirects

```toml
# Basic redirect
[[redirects]]
from = "/old"
to = "/new"
status = 301              # 301 (default), 302, 200 (rewrite), 404

# SPA catch-all
[[redirects]]
from = "/*"
to = "/index.html"
status = 200

# Splat (wildcard)
[[redirects]]
from = "/blog/*"
to = "/news/:splat"

# Path parameters
[[redirects]]
from = "/users/:id"
to = "/api/users/:id"
status = 200

# Force (override existing files)
[[redirects]]
from = "/app/*"
to = "/index.html"
status = 200
force = true

# Proxy to external service
[[redirects]]
from = "/api/*"
to = "https://api.example.com/:splat"
status = 200
[redirects.headers]
  X-Custom = "value"

# Country/language conditions
[[redirects]]
from = "/*"
to = "/fr/:splat"
status = 200
conditions = { Country = ["FR"], Language = ["fr"] }
```

**Rule order matters** — Netlify processes the first matching rule. Place specific rules before general ones.

## Headers

```toml
[[headers]]
for = "/*"
[headers.values]
  X-Frame-Options = "DENY"
  X-Content-Type-Options = "nosniff"

[[headers]]
for = "/assets/*"
[headers.values]
  Cache-Control = "public, max-age=31536000, immutable"
```

Headers apply only to files served from Netlify's CDN (not to function or edge function responses — set those in code).

## Deploy Contexts

Override settings per deploy context:

```toml
[context.production]
command = "npm run build"
environment = { NODE_ENV = "production" }

[context.deploy-preview]
command = "npm run build:preview"

[context.branch-deploy]
command = "npm run build:staging"

[context.dev]
environment = { NODE_ENV = "development" }

# Specific branch
[context."staging"]
command = "npm run build:staging"
```

## Environment Variables

```toml
[build.environment]
NODE_VERSION = "20"

[context.production.environment]
API_URL = "https://api.prod.com"

[context.deploy-preview.environment]
API_URL = "https://api.staging.com"
```

**Do not put secrets in netlify.toml** (it's committed to source control). Use the Netlify UI or CLI for sensitive values. See the **netlify-cli-and-deploy** skill for CLI environment variable management.

## Functions Configuration

```toml
[functions]
directory = "netlify/functions"   # Default
node_bundler = "esbuild"

# Scheduled function
[functions."cleanup"]
schedule = "@daily"
```

## Edge Functions Configuration

```toml
[[edge_functions]]
path = "/admin"
function = "auth"

# Import map for Deno URL imports
[functions]
deno_import_map = "./import_map.json"
```

## Dev Server

```toml
[dev]
command = "npm start"       # Dev server command
port = 8888                 # Netlify Dev port
targetPort = 3000           # Your app's dev server port
framework = "#auto"         # "#auto", "#static", "#custom"
```

## Plugins

```toml
[[plugins]]
package = "@netlify/plugin-lighthouse"
[plugins.inputs]
  audits = ["performance", "accessibility"]
```

## Image CDN

```toml
[images]
remote_images = ["https://example\\.com/.*"]
```

See the **netlify-image-cdn** skill for full Image CDN usage.

```

## File: skills\netlify-db\SKILL.md
```
---
name: netlify-db
description: Guide for using Netlify DB (managed Neon Postgres). Use when the project needs a relational database, structured data storage, SQL queries, or data that will grow over time. Covers provisioning, raw SQL via @netlify/neon, Drizzle ORM integration, migrations, and deploy preview branching. Also covers when to use Netlify Blobs instead.
---

# Netlify DB

Netlify DB provisions a managed Neon Postgres database automatically. No Neon account required.

## When to Use DB vs Blobs

**Use Netlify DB when:**
- Storing structured, relational data
- Data will grow over time
- Need queries, filtering, joins, or aggregations

**Use Netlify Blobs instead when:**
- Storing files (images, documents, exports)
- A handful of records with no growth expectation
- Simple key-value storage with no relational needs
- Want zero dependencies beyond `@netlify/blobs`

See the **netlify-blobs** skill for Blobs usage.

## Setup

```bash
npm install @netlify/neon
netlify db init    # Provisions database and sets up Drizzle ORM
```

Prerequisites: logged into Netlify CLI and site linked (`netlify link`).

## Raw SQL via @netlify/neon

`@netlify/neon` wraps `@neondatabase/serverless`. No connection string needed — it auto-configures.

```typescript
import { neon } from "@netlify/neon";
const sql = neon();

const users = await sql("SELECT * FROM users");
await sql("INSERT INTO users (name) VALUES ($1)", ["Jane"]);
await sql("UPDATE users SET name = $1 WHERE id = $2", ["Jane", 1]);
await sql("DELETE FROM users WHERE id = $1", [1]);
```

## Drizzle ORM Integration

For most projects, use Drizzle ORM on top of Netlify DB.

### drizzle.config.ts

```typescript
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  dbCredentials: { url: process.env.NETLIFY_DATABASE_URL! },
  schema: "./db/schema.ts",
  out: "./migrations",
  migrations: { prefix: "timestamp" }, // Avoids conflicts across branches
});
```

### db/index.ts

```typescript
import { neon } from "@neondatabase/serverless";
import { drizzle } from "drizzle-orm/neon-http";
import * as schema from "./schema";

const sql = neon(process.env.NETLIFY_DATABASE_URL!);
export const db = drizzle(sql, { schema });
export * from "./schema";
```

### Schema Example

```typescript
// db/schema.ts
import { integer, pgTable, varchar, text, boolean, timestamp } from "drizzle-orm/pg-core";

export const items = pgTable("items", {
  id: integer().primaryKey().generatedAlwaysAsIdentity(),
  title: varchar({ length: 255 }).notNull(),
  description: text(),
  isActive: boolean("is_active").notNull().default(true),
  createdAt: timestamp("created_at").defaultNow(),
  updatedAt: timestamp("updated_at").defaultNow(),
});

export type Item = typeof items.$inferSelect;
export type NewItem = typeof items.$inferInsert;
```

### Query Patterns

```typescript
import { db, items } from "../db";
import { eq } from "drizzle-orm";

const all = await db.select().from(items);
const [one] = await db.select().from(items).where(eq(items.id, id)).limit(1);
const [created] = await db.insert(items).values({ title: "New" }).returning();
const [updated] = await db.update(items).set({ title: "Updated" }).where(eq(items.id, id)).returning();
await db.delete(items).where(eq(items.id, id));
```

## Migrations

```json
{
  "scripts": {
    "db:generate": "drizzle-kit generate",
    "db:migrate": "netlify dev:exec drizzle-kit migrate",
    "db:push": "netlify dev:exec drizzle-kit push",
    "db:studio": "netlify dev:exec drizzle-kit studio"
  }
}
```

Workflow: modify schema, run `db:generate`, then `db:migrate`.

## Deploy Preview Branching

Netlify DB supports branching — production branch gets the production database, all other branches and deploy previews get a separate preview branch. Develop and test migrations on preview, merge to main, then apply to production.

## Environment Variables

- `NETLIFY_DATABASE_URL` — Auto-set by Netlify when database is provisioned
- Retrieve manually: `netlify env:get NETLIFY_DATABASE_URL`

## Local Development

Run `netlify dev` or use `@netlify/vite-plugin` to get database access locally. Use `netlify dev:exec` to run migration commands with the proper environment.

```

## File: skills\netlify-deploy\SKILL.md
```
---
name: netlify-deploy
description: Deploy web projects to Netlify using the Netlify CLI (`npx netlify`). Use when the user asks to deploy, host, publish, or link a site/repo on Netlify, including preview and production deploys.
---

# Netlify Deployment Skill

Deploy web projects to Netlify using the Netlify CLI with intelligent detection of project configuration and deployment context.

## Overview

This skill automates Netlify deployments by:
- Verifying Netlify CLI authentication
- Detecting project configuration and framework
- Linking to existing sites or creating new ones
- Deploying to production or preview environments

## Prerequisites

- **Netlify CLI**: Installed via npx (no global install required)
- **Authentication**: Netlify account with active login session
- **Project**: Valid web project in current directory
- **Network access**: Deployment requires outbound network calls. If sandboxing blocks these, the agent may need to request elevated permissions or prompt the user.
- **Timeouts**: Deployments can take a few minutes. Use appropriate timeout values for CLI commands.

## Authentication Pattern

The skill uses the **pre-authenticated Netlify CLI** approach:

1. Check authentication status with `npx netlify status`
2. If not authenticated, guide user through `npx netlify login`
3. Fail gracefully if authentication cannot be established

Authentication uses either:
- **Browser-based OAuth** (primary): `netlify login` opens browser for authentication
- **API Key** (alternative): Set `NETLIFY_AUTH_TOKEN` environment variable

## Workflow

### 1. Verify Netlify CLI Authentication

Check if the user is logged into Netlify:

```bash
npx netlify status
```

**Expected output patterns**:
- ✅ Authenticated: Shows logged-in user email and site link status
- ❌ Not authenticated: "Not logged into any site" or authentication error

**If not authenticated**, guide the user:

```bash
npx netlify login
```

This opens a browser window for OAuth authentication. Wait for user to complete login, then verify with `netlify status` again.

**Alternative: API Key authentication**

If browser authentication isn't available, users can set:

```bash
export NETLIFY_AUTH_TOKEN=your_token_here
```

Tokens can be generated at: https://app.netlify.com/user/applications#personal-access-tokens

### 2. Detect Site Link Status

From `netlify status` output, determine:
- **Linked**: Site already connected to Netlify (shows site name/URL)
- **Not linked**: Need to link or create site

### 3. Link to Existing Site or Create New

**If already linked** → Skip to step 4

**If not linked**, attempt to link by Git remote:

```bash
# Check if project is Git-based
git remote show origin

# If Git-based, extract remote URL
# Format: https://github.com/username/repo or git@github.com:username/repo.git

# Try to link by Git remote
npx netlify link --git-remote-url <REMOTE_URL>
```

**If link fails** (site doesn't exist on Netlify):

```bash
# Create new site interactively
npx netlify init
```

This guides user through:
1. Choosing team/account
2. Setting site name
3. Configuring build settings
4. Creating netlify.toml if needed

### 4. Verify Dependencies

Before deploying, ensure project dependencies are installed:

```bash
# For npm projects
npm install

# For other package managers, detect and use appropriate command
# yarn install, pnpm install, etc.
```

### 5. Deploy to Netlify

Choose deployment type based on context:

**Preview/Draft Deploy** (default for existing sites):

```bash
npx netlify deploy
```

This creates a deploy preview with a unique URL for testing.

**Production Deploy** (for new sites or explicit production deployments):

```bash
npx netlify deploy --prod
```

This deploys to the live production URL.

**Deployment process**:
1. CLI detects build settings (from netlify.toml or prompts user)
2. Builds the project locally
3. Uploads built assets to Netlify
4. Returns deployment URL

### 6. Report Results

After deployment, report to user:
- **Deploy URL**: Unique URL for this deployment
- **Site URL**: Production URL (if production deploy)
- **Deploy logs**: Link to Netlify dashboard for logs
- **Next steps**: Suggest `netlify open` to view site or dashboard

## Handling netlify.toml

If a `netlify.toml` file exists, the CLI uses it automatically. If not, the CLI will prompt for:
- **Build command**: e.g., `npm run build`, `next build`
- **Publish directory**: e.g., `dist`, `build`, `.next`

Common framework defaults:
- **Next.js**: build command `npm run build`, publish `.next`
- **React (Vite)**: build command `npm run build`, publish `dist`
- **Static HTML**: no build command, publish current directory

The skill should detect framework from `package.json` if possible and suggest appropriate settings.

## Example Full Workflow

```bash
# 1. Check authentication
npx netlify status

# If not authenticated:
npx netlify login

# 2. Link site (if needed)
# Try Git-based linking first
git remote show origin
npx netlify link --git-remote-url https://github.com/user/repo

# If no site exists, create new one:
npx netlify init

# 3. Install dependencies
npm install

# 4. Deploy (preview for testing)
npx netlify deploy

# 5. Deploy to production (when ready)
npx netlify deploy --prod
```

## Error Handling

Common issues and solutions:

**"Not logged in"**
→ Run `npx netlify login`

**"No site linked"**
→ Run `npx netlify link` or `npx netlify init`

**"Build failed"**
→ Check build command and publish directory in netlify.toml or CLI prompts
→ Verify dependencies are installed
→ Review build logs for specific errors

**"Publish directory not found"**
→ Verify build command ran successfully
→ Check publish directory path is correct

## Environment Variables

For secrets and configuration:

1. Never commit secrets to Git
2. Set in Netlify dashboard: Site Settings → Environment Variables
3. Access in builds via `process.env.VARIABLE_NAME`

## Tips

- Use `netlify deploy` (no `--prod`) first to test before production
- Run `netlify open` to view site in Netlify dashboard
- Run `netlify logs` to view function logs (if using Netlify Functions)
- Use `netlify dev` for local development with Netlify Functions

## Reference

- Netlify CLI Docs: https://docs.netlify.com/cli/get-started/
- netlify.toml Reference: https://docs.netlify.com/configure-builds/file-based-configuration/

## References


```

## File: skills\netlify-deploy\references\cli_commands.md
```
# Netlify CLI Commands Reference

Quick reference for common Netlify CLI commands used in deployments.

## Authentication

```bash
# Login via browser OAuth
npx netlify login

# Check authentication status and site link
npx netlify status

# Logout
npx netlify logout
```

## Site Management

```bash
# Link current directory to existing site
npx netlify link

# Link by Git remote URL
npx netlify link --git-remote-url <url>

# Create and link new site
npx netlify init

# Unlink from current site
npx netlify unlink

# Open site in Netlify dashboard
npx netlify open

# Open site admin panel
npx netlify open:admin

# Open site in browser
npx netlify open:site
```

## Deployment

```bash
# Deploy preview/draft (safe for testing)
npx netlify deploy

# Deploy to production
npx netlify deploy --prod

# Deploy with specific directory
npx netlify deploy --dir=dist

# Deploy with message
npx netlify deploy --message="Deploy message"

# List all deploys
npx netlify deploy:list
```

## Development

```bash
# Run local dev server with Netlify features
npx netlify dev

# Run local dev server on specific port
npx netlify dev --port 3000
```

## Site Information

```bash
# Get site info
npx netlify sites:list

# Get current site info
npx netlify api getSite --data '{"site_id": "YOUR_SITE_ID"}'
```

## Environment Variables

```bash
# List environment variables
npx netlify env:list

# Set environment variable
npx netlify env:set KEY value

# Get environment variable value
npx netlify env:get KEY

# Import env vars from file
npx netlify env:import .env
```

## Build

```bash
# Show build settings
npx netlify build --dry

# Run build locally
npx netlify build
```

## Functions (Serverless)

```bash
# List functions
npx netlify functions:list

# Invoke function locally
npx netlify functions:invoke FUNCTION_NAME

# Create new function
npx netlify functions:create FUNCTION_NAME
```

## Logs

```bash
# Stream function logs
npx netlify logs

# View logs for specific function
npx netlify logs:function FUNCTION_NAME
```

## Troubleshooting Commands

```bash
# Check CLI version
npx netlify --version

# Get help for any command
npx netlify help [command]

# Check status with verbose output
npx netlify status --verbose
```

## Exit Codes

- `0` - Success
- `1` - General error
- `2` - Authentication error
- `3` - Site not found
- `4` - Build failed

## Common Flags

- `--json` - Output as JSON
- `--silent` - Suppress output
- `--debug` - Show debug information
- `--force` - Skip confirmation prompts

## Resources

- Full CLI documentation: https://docs.netlify.com/cli/get-started/
- CLI GitHub repository: https://github.com/netlify/cli

```

## File: skills\netlify-deploy\references\deployment_patterns.md
```
# Netlify Deployment Patterns

Common deployment scenarios and best practices for the Netlify skill.

## Deployment Decision Tree

```
Is user authenticated?
├─ No → Run `netlify login`
└─ Yes → Is site linked?
    ├─ No → Is it a Git repo?
    │   ├─ Yes → Try `netlify link --git-remote-url`
    │   │   ├─ Success → Continue to deploy
    │   │   └─ Fail → Run `netlify init`
    │   └─ No → Run `netlify init`
    └─ Yes → Is this first deploy or existing site?
        ├─ First deploy/new site → `netlify deploy --prod`
        └─ Existing site → `netlify deploy` (preview)
```

## Scenario 1: First-Time Deployment (New Project)

**Context**: User has a project that has never been deployed to Netlify.

**Steps**:
1. Check authentication: `npx netlify status`
2. If not authenticated: `npx netlify login`
3. Initialize new site: `npx netlify init`
   - This guides user through setup
   - Creates netlify.toml if needed
4. Install dependencies: `npm install`
5. Deploy to production: `npx netlify deploy --prod`

**Example**:
```bash
npx netlify status
# Not linked to a site

npx netlify login
# Opens browser for authentication

npx netlify init
# Walks through site creation

npm install
npx netlify deploy --prod
```

## Scenario 2: Linking Existing Git Repository to Existing Site

**Context**: User has a site already on Netlify and wants to link their local repo.

**Steps**:
1. Check authentication: `npx netlify status`
2. Get Git remote: `git remote show origin`
3. Extract URL (e.g., `https://github.com/user/repo.git`)
4. Link by remote: `npx netlify link --git-remote-url <URL>`
5. If found, linked. If not, run `netlify init`

**Example**:
```bash
git remote show origin
# * remote origin
#   Fetch URL: https://github.com/user/my-app.git

npx netlify link --git-remote-url https://github.com/user/my-app.git
# Site linked successfully
```

## Scenario 3: Preview Deployment (Testing Changes)

**Context**: User wants to test changes before pushing to production.

**Steps**:
1. Ensure site is linked: `npx netlify status`
2. Make code changes
3. Deploy preview: `npx netlify deploy`
4. Review preview URL
5. If approved, deploy to prod: `npx netlify deploy --prod`

**Example**:
```bash
# Make changes to code

npx netlify deploy
# Draft deploy URL: https://507f1f77bcf86cd799439011-my-app.netlify.app

# Test the preview, then:
npx netlify deploy --prod
```

## Scenario 4: Framework-Specific Deployments

### Next.js

```bash
# Next.js typically uses .next as output
npx netlify deploy --prod

# netlify.toml should have:
# [build]
#   command = "npm run build"
#   publish = ".next"
```

### React (Vite)

```bash
# Vite outputs to dist by default
npm run build
npx netlify deploy --dir=dist --prod

# netlify.toml:
# [build]
#   command = "npm run build"
#   publish = "dist"
```

### Static HTML

```bash
# No build step needed
npx netlify deploy --dir=. --prod
```

## Scenario 5: Monorepo Deployment

**Context**: Project is in a subdirectory of a monorepo.

**Steps**:
1. Navigate to project subdirectory: `cd packages/frontend`
2. Or set base in netlify.toml:
   ```toml
   [build]
     base = "packages/frontend"
     command = "npm run build"
     publish = "dist"
   ```
3. Deploy normally: `npx netlify deploy --prod`

## Scenario 6: Environment Variables

**Context**: Project needs secrets or environment-specific config.

**Steps**:
1. Never commit secrets to Git
2. Set in Netlify dashboard or CLI:
   ```bash
   npx netlify env:set API_KEY "secret_value"
   npx netlify env:set NODE_ENV "production"
   ```
3. Access in code: `process.env.API_KEY`
4. Deploy: `npx netlify deploy --prod`

## Scenario 7: Custom Domain Setup

**Context**: User wants to use a custom domain.

**Steps**:
1. Deploy site first: `npx netlify deploy --prod`
2. Add domain via dashboard or CLI:
   ```bash
   npx netlify open:admin
   # Navigate to Domain settings
   ```
3. Update DNS records as instructed by Netlify
4. Wait for DNS propagation (can take up to 48 hours)

## Best Practices

### 1. Always Preview First

```bash
# Deploy preview
npx netlify deploy

# Test thoroughly
# Then deploy to production
npx netlify deploy --prod
```

### 2. Use netlify.toml for Consistency

Create a `netlify.toml` file in your repo root:

```toml
[build]
  command = "npm run build"
  publish = "dist"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

This ensures consistent builds across all deployments.

### 3. Framework Detection

Let Netlify auto-detect when possible. Only specify build settings if:
- Netlify can't detect your framework
- You need custom build commands
- Your project has a non-standard structure

### 4. Dependency Installation

Always ensure dependencies are installed before deploying:

```bash
npm install  # or yarn install, pnpm install
npx netlify deploy
```

### 5. Build Locally First

Test builds locally before deploying:

```bash
npm run build
# Check that build output exists

npx netlify deploy --dir=dist
```

### 6. Use Deploy Messages

Add context to deployments:

```bash
npx netlify deploy --prod --message="Fix login bug"
```

## Error Recovery Patterns

### "Publish directory not found"

**Cause**: Build command didn't create expected output directory.

**Fix**:
1. Run build locally: `npm run build`
2. Check output directory name
3. Update netlify.toml or CLI prompts with correct path

### "Command failed with exit code 1"

**Cause**: Build command failed.

**Fix**:
1. Check build logs for specific error
2. Run build locally to reproduce: `npm run build`
3. Fix the build error
4. Deploy again

### "Not logged in"

**Cause**: Authentication token expired or missing.

**Fix**:
```bash
npx netlify logout
npx netlify login
```

### "No site linked"

**Cause**: Project not connected to a Netlify site.

**Fix**:
```bash
# Try linking to existing site
npx netlify link

# Or create new site
npx netlify init
```

## Performance Tips

1. **Enable processing** in netlify.toml for auto-optimization:
   ```toml
   [build.processing.css]
     bundle = true
     minify = true
   ```

2. **Use caching headers** for static assets:
   ```toml
   [[headers]]
     for = "/assets/*"
     [headers.values]
       Cache-Control = "public, max-age=31536000, immutable"
   ```

3. **Optimize images** before deploying or use Netlify Image CDN

4. **Use Netlify Functions** for serverless backend (avoid external API calls when possible)

## Resources

- Netlify CLI Documentation: https://docs.netlify.com/cli/get-started/
- Framework Integration Guides: https://docs.netlify.com/frameworks/
- Build Configuration: https://docs.netlify.com/configure-builds/

```

## File: skills\netlify-deploy\references\netlify_toml.md
```
# netlify.toml Configuration Reference

Configuration file for Netlify builds and deployments.

## Basic Structure

```toml
[build]
  command = "npm run build"
  publish = "dist"
```

## Build Settings

### Common Configuration

```toml
[build]
  # Command to build your site
  command = "npm run build"

  # Directory to publish (relative to repo root)
  publish = "dist"

  # Functions directory
  functions = "netlify/functions"

  # Base directory (if not repo root)
  base = "packages/frontend"

  # Ignore builds for specific conditions
  ignore = "git diff --quiet HEAD^ HEAD package.json"
```

## Environment Variables

```toml
[build.environment]
  NODE_VERSION = "18"
  NPM_FLAGS = "--prefix=/dev/null"

[context.production.environment]
  NODE_ENV = "production"
```

## Framework Detection

Netlify auto-detects frameworks, but you can override:

### Next.js

```toml
[build]
  command = "npm run build"
  publish = ".next"
```

### React (Vite)

```toml
[build]
  command = "npm run build"
  publish = "dist"
```

### Vue

```toml
[build]
  command = "npm run build"
  publish = "dist"
```

### Astro

```toml
[build]
  command = "npm run build"
  publish = "dist"
```

### SvelteKit

```toml
[build]
  command = "npm run build"
  publish = "build"
```

## Redirects and Rewrites

```toml
[[redirects]]
  from = "/old-path"
  to = "/new-path"
  status = 301

[[redirects]]
  from = "/api/*"
  to = "https://api.example.com/:splat"
  status = 200

# SPA fallback (for client-side routing)
[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

## Headers

```toml
[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-XSS-Protection = "1; mode=block"
    Content-Security-Policy = "default-src 'self'"

[[headers]]
  for = "/assets/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"
```

## Context-Specific Configuration

Deploy different settings per context:

```toml
# Production
[context.production]
  command = "npm run build:prod"
  [context.production.environment]
    NODE_ENV = "production"

# Deploy previews
[context.deploy-preview]
  command = "npm run build:preview"

# Branch deploys
[context.branch-deploy]
  command = "npm run build:staging"

# Specific branch
[context.staging]
  command = "npm run build:staging"
```

## Functions Configuration

```toml
[functions]
  directory = "netlify/functions"
  node_bundler = "esbuild"

[[functions]]
  path = "/api/*"
  function = "api"
```

## Build Plugins

```toml
[[plugins]]
  package = "@netlify/plugin-lighthouse"

  [plugins.inputs]
    output_path = "reports/lighthouse.html"

[[plugins]]
  package = "netlify-plugin-submit-sitemap"

  [plugins.inputs]
    baseUrl = "https://example.com"
    sitemapPath = "/sitemap.xml"
```

## Edge Functions

```toml
[[edge_functions]]
  function = "geolocation"
  path = "/api/location"
```

## Processing

```toml
[build.processing]
  skip_processing = false

[build.processing.css]
  bundle = true
  minify = true

[build.processing.js]
  bundle = true
  minify = true

[build.processing.html]
  pretty_urls = true

[build.processing.images]
  compress = true
```

## Common Patterns

### Single Page Application (SPA)

```toml
[build]
  command = "npm run build"
  publish = "dist"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

### Monorepo with Base Directory

```toml
[build]
  base = "packages/web"
  command = "npm run build"
  publish = "dist"
```

### Multiple Redirects with Country-Based Routing

```toml
[[redirects]]
  from = "/"
  to = "/uk"
  status = 302
  conditions = {Country = ["GB"]}

[[redirects]]
  from = "/"
  to = "/us"
  status = 302
  conditions = {Country = ["US"]}
```

## Validation

Validate your netlify.toml:

```bash
npx netlify build --dry
```

## Resources

- Full configuration reference: https://docs.netlify.com/configure-builds/file-based-configuration/
- Framework-specific guides: https://docs.netlify.com/frameworks/

```

## File: skills\netlify-edge-functions\SKILL.md
```
---
name: netlify-edge-functions
description: Guide for writing Netlify Edge Functions. Use when building middleware, geolocation-based logic, request/response manipulation, authentication checks, A/B testing, or any low-latency edge compute. Covers Deno runtime, context.next() middleware pattern, geolocation, and when to choose edge vs serverless.
---

# Netlify Edge Functions

Edge functions run on Netlify's globally distributed edge network (Deno runtime), providing low-latency responses close to users.

## Syntax

```typescript
import type { Config, Context } from "@netlify/edge-functions";

export default async (req: Request, context: Context) => {
  return new Response("Hello from the edge!");
};

export const config: Config = {
  path: "/hello",
};
```

Place files in `netlify/edge-functions/`. Uses `.ts`, `.js`, `.tsx`, or `.jsx` extensions.

## Config Object

```typescript
export const config: Config = {
  path: "/api/*",                    // URLPattern path(s)
  excludedPath: "/api/public/*",     // Exclusions
  method: ["GET", "POST"],           // HTTP methods
  onError: "bypass",                 // "fail" (default), "bypass", or "/error-page"
  cache: "manual",                   // Enable response caching
};
```

## Middleware Pattern

Use `context.next()` to invoke the next handler in the chain and optionally modify the response:

```typescript
export default async (req: Request, context: Context) => {
  // Before: modify request or short-circuit
  if (!isAuthenticated(req)) {
    return new Response("Unauthorized", { status: 401 });
  }

  // Continue to origin/next function
  const response = await context.next();

  // After: modify response
  response.headers.set("x-custom-header", "value");
  return response;
};
```

Return `undefined` to pass through without modification:

```typescript
export default async (req: Request, context: Context) => {
  if (!shouldHandle(req)) return; // continues to next handler
  return new Response("Handled");
};
```

## Geolocation and IP

```typescript
export default async (req: Request, context: Context) => {
  const { city, country, subdivision, timezone } = context.geo;
  const ip = context.ip;

  if (country?.code === "DE") {
    return Response.redirect(new URL("/de", req.url));
  }
};
```

Local dev with mocked geo: `netlify dev --geo=mock --country=US`

## Environment Variables

Use `Netlify.env` (not `process.env` or `Deno.env`):

```typescript
const secret = Netlify.env.get("API_SECRET");
```

## Module Support

- **Node.js builtins**: `import { randomBytes } from "node:crypto";`
- **npm packages**: Install via npm and import by name
- **Deno modules**: URL imports (e.g., `import X from "https://esm.sh/package"`)

For URL imports, use an import map:

```json
// import_map.json
{ "imports": { "html-rewriter": "https://ghuc.cc/worker-tools/html-rewriter/index.ts" } }
```

```toml
# netlify.toml
[functions]
  deno_import_map = "./import_map.json"
```

## When to Use Edge vs Serverless

| Use Edge Functions for | Use Serverless Functions for |
|---|---|
| Low-latency responses | Long-running operations (up to 15 min) |
| Request/response manipulation | Complex Node.js dependencies |
| Geolocation-based logic | Database-heavy operations |
| Auth checks and redirects | Background/scheduled tasks |
| A/B testing, personalization | Tasks needing > 512 MB memory |

## Limits

| Resource | Limit |
|---|---|
| CPU time | 50 ms per request |
| Memory | 512 MB per deployed set |
| Response header timeout | 40 seconds |
| Code size | 20 MB compressed |

```

## File: skills\netlify-forms\SKILL.md
```
---
name: netlify-forms
description: Guide for using Netlify Forms for HTML form handling. Use when adding contact forms, feedback forms, file upload forms, or any form that should be collected by Netlify. Covers the data-netlify attribute, spam filtering, AJAX submissions, file uploads, notifications, and the submissions API.
---

# Netlify Forms

Netlify Forms collects HTML form submissions without server-side code. Form detection must be enabled in the Netlify UI (Forms section).

## Basic Setup

Add `data-netlify="true"` and a unique `name` to the form:

```html
<form name="contact" method="POST" data-netlify="true">
  <label>Name: <input type="text" name="name" /></label>
  <label>Email: <input type="email" name="email" /></label>
  <label>Message: <textarea name="message"></textarea></label>
  <button type="submit">Send</button>
</form>
```

Netlify's build system detects the form and injects a hidden `form-name` input automatically. For a custom success page, add `action="/thank-you"` to the form tag. Use paths without `.html` extension — Netlify serves `thank-you.html` at `/thank-you` by default, and the `.html` path returns 404.

## JavaScript-Rendered Forms (React, Vue, SSR Frameworks)

For forms rendered by JavaScript frameworks (React, Vue, TanStack Start, Next.js, SvelteKit, Remix, Nuxt), Netlify's build parser cannot detect the form in static HTML. You MUST create a static HTML skeleton file for build-time form detection:

Create a static HTML file in `public/` (e.g. `public/__forms.html`) containing a hidden copy of each form:

```html
<!DOCTYPE html>
<html>
  <body>
    <form name="contact" data-netlify="true" netlify-honeypot="bot-field" hidden>
      <input type="hidden" name="form-name" value="contact" />
      <input type="text" name="name" />
      <input type="email" name="email" />
      <textarea name="message"></textarea>
      <input name="bot-field" />
    </form>
  </body>
</html>
```

**Rules:**
- The form `name` must exactly match the `form-name` value used in your component's fetch call
- Include every field your component submits — Netlify validates field names against the registered form
- Without this file, Netlify cannot detect the form and submissions will silently fail

Your component must also include a hidden `form-name` input:

```jsx
<form name="contact" method="POST" data-netlify="true">
  <input type="hidden" name="form-name" value="contact" />
  {/* ... fields ... */}
</form>
```

## AJAX Submissions

### Vanilla JavaScript

```javascript
const form = document.querySelector("form");
form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const formData = new FormData(form);
  await fetch("/", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams(formData).toString(),
  });
});
```

> **SSR frameworks (TanStack Start, Next.js, SvelteKit, Remix, Nuxt):** The `fetch` URL must target the static skeleton
> file path (e.g. `"/__forms.html"`), **not** `"/"`. In SSR apps, `fetch("/")` is intercepted by the SSR catch-all
> function and never reaches Netlify's form processing middleware. See the React example and troubleshooting section below.

### React Example

```tsx
function ContactForm() {
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);
    // For SSR apps, use the skeleton file path instead of "/" (e.g. "/__forms.html")
    const response = await fetch("/__forms.html", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams(formData as any).toString(),
    });
    if (response.ok) {
      // Show success feedback
    }
  };

  return (
    <form name="contact" method="POST" data-netlify="true" onSubmit={handleSubmit}>
      <input type="hidden" name="form-name" value="contact" />
      <input type="text" name="name" placeholder="Name" />
      <input type="email" name="email" placeholder="Email" />
      <textarea name="message" placeholder="Message" />
      <button type="submit">Send</button>
    </form>
  );
}
```

> **SSR troubleshooting:** If form submissions appear to succeed (200 response) but nothing shows in the Netlify Forms
> UI, the POST is likely being intercepted by the SSR function. Ensure `fetch` targets the skeleton file path (e.g.
> `"/__forms.html"`), not `"/"`. The skeleton file path routes through the CDN origin where Netlify's form handler runs.

## Spam Filtering

Netlify uses Akismet automatically. Add a honeypot field for extra protection:

```html
<form name="contact" method="POST" netlify-honeypot="bot-field" data-netlify="true">
  <p style="display:none">
    <label>Don't fill this out: <input name="bot-field" /></label>
  </p>
  <!-- visible fields -->
</form>
```

For reCAPTCHA, add `data-netlify-recaptcha="true"` to the form and include `<div data-netlify-recaptcha="true"></div>` where the widget should appear.

## File Uploads

```html
<form name="upload" enctype="multipart/form-data" data-netlify="true">
  <input type="text" name="name" />
  <input type="file" name="attachment" />
  <button type="submit">Upload</button>
</form>
```

For AJAX file uploads, use `FormData` directly — do **not** set `Content-Type` (the browser sets it with the correct boundary):

```javascript
await fetch("/", { method: "POST", body: new FormData(form) });
```

**Limits:** 8 MB max request size, 30-second timeout, one file per input field.

## Notifications

Configure in the Netlify UI under **Project configuration > Notifications**:

- **Email**: Auto-sends on submission. Add `<input type="hidden" name="subject" value="Contact form" />` for custom subject lines.
- **Slack**: Via Netlify App for Slack.
- **Webhooks**: Trigger external services on submission.

## Submissions API

Access submissions programmatically:

```
GET /api/v1/forms/{form_id}/submissions
Authorization: Bearer <PERSONAL_ACCESS_TOKEN>
```

Key endpoints:

| Action | Method | Path |
|---|---|---|
| List forms | GET | `/api/v1/sites/{site_id}/forms` |
| Get submissions | GET | `/api/v1/forms/{form_id}/submissions` |
| Get spam | GET | `/api/v1/forms/{form_id}/submissions?state=spam` |
| Delete submission | DELETE | `/api/v1/submissions/{id}` |

```

## File: skills\netlify-frameworks\SKILL.md
```
---
name: netlify-frameworks
description: Guide for deploying web frameworks on Netlify. Use when setting up a framework project (Vite/React, Astro, TanStack Start, Next.js, Nuxt, SvelteKit, Remix) for Netlify deployment, configuring adapters or plugins, or troubleshooting framework-specific Netlify integration. Covers what Netlify needs from each framework and how adapters handle server-side rendering.
---

# Frameworks on Netlify

Netlify supports any framework that produces static output. For frameworks with server-side capabilities (SSR, API routes, middleware), an adapter or plugin translates the framework's server-side code into Netlify Functions and Edge Functions automatically.

## How It Works

During build, the framework adapter writes files to `.netlify/v1/` — functions, edge functions, redirects, and configuration. Netlify reads these to deploy the site. You do not need to write Netlify Functions manually when using a framework adapter for server-side features.

## Detecting Your Framework

Check these files to determine the framework:

| File | Framework |
|---|---|
| `astro.config.*` | Astro |
| `next.config.*` | Next.js |
| `nuxt.config.*` | Nuxt |
| `vite.config.*` + `react-router` | Vite + React (SPA or Remix) |
| `app.config.*` + `@tanstack/react-start` | TanStack Start |
| `svelte.config.*` | SvelteKit |

## Framework Reference Guides

Each framework has specific adapter/plugin requirements and local dev patterns:


## General Patterns

### Client-Side Routing (SPA)

For single-page apps with client-side routing, add a catch-all redirect:

```toml
# netlify.toml
[[redirects]]
from = "/*"
to = "/index.html"
status = 200
```

### Custom 404 Pages

- **Static sites**: Create a `404.html` in your publish directory. Netlify serves it automatically for unmatched routes.
- **SSR frameworks**: Handle 404s in the framework's routing (the adapter maps this to Netlify's function routing).

### Environment Variables in Frameworks

Each framework exposes environment variables to client-side code differently:

| Framework | Client prefix | Access pattern |
|---|---|---|
| Vite / React | `VITE_` | `import.meta.env.VITE_VAR` |
| Astro | `PUBLIC_` | `import.meta.env.PUBLIC_VAR` |
| Next.js | `NEXT_PUBLIC_` | `process.env.NEXT_PUBLIC_VAR` |
| Nuxt | `NUXT_PUBLIC_` | `useRuntimeConfig().public.var` |

Server-side code in all frameworks can access variables via `process.env.VAR` or `Netlify.env.get("VAR")`.

```

## File: skills\netlify-frameworks\references\astro.md
```
# Astro on Netlify

## Setup

Install the Netlify adapter:

```bash
npx astro add netlify
```

This installs `@astrojs/netlify` and updates `astro.config.*` automatically.

### Manual Setup

```bash
npm install @astrojs/netlify
```

```typescript
// astro.config.mjs
import { defineConfig } from "astro/config";
import netlify from "@astrojs/netlify";

export default defineConfig({
  output: "server",  // or "hybrid" for mixed static/SSR
  adapter: netlify(),
});
```

## Output Modes

| Mode | Behavior |
|---|---|
| `"static"` | Fully pre-rendered at build time (no adapter needed) |
| `"server"` | All pages rendered on request (SSR) |
| `"hybrid"` | Static by default, opt-in to SSR per page with `export const prerender = false` |

## What the Adapter Does

- Converts Astro server routes into Netlify Functions
- Handles SSR, API routes, and middleware
- Maps Astro's routing to Netlify's function routing
- You do **not** write raw Netlify Functions for Astro's server routes

## API Routes

Astro API routes (in `src/pages/api/`) are handled by the adapter:

```typescript
// src/pages/api/items.ts
import type { APIRoute } from "astro";

export const GET: APIRoute = async () => {
  return new Response(JSON.stringify({ items: [] }), {
    headers: { "Content-Type": "application/json" },
  });
};

export const POST: APIRoute = async ({ request }) => {
  const data = await request.json();
  return new Response(JSON.stringify({ created: data }), { status: 201 });
};
```

## Forms (HTML Pattern)

Astro renders HTML server-side, so Netlify can detect forms directly:

```astro
---
// src/pages/contact.astro
---
<form name="contact" method="POST" data-netlify="true">
  <label>Name: <input type="text" name="name" /></label>
  <label>Email: <input type="email" name="email" /></label>
  <label>Message: <textarea name="message"></textarea></label>
  <button type="submit">Send</button>
</form>
```

For form submissions that should redirect back with feedback, handle the POST in an API route and redirect:

```typescript
// src/pages/api/contact.ts
export const POST: APIRoute = async ({ request, redirect }) => {
  const formData = await request.formData();
  // Process form...
  return redirect("/contact?success=true");
};
```

## Custom 404

Create `src/pages/404.astro`. Astro handles this automatically.

## Local Development

**Option A: Astro dev server** (simpler, but no Netlify primitives):

```bash
npm run dev    # astro dev
```

**Option B: netlify dev** (full Netlify environment including functions, env vars):

```bash
netlify dev
```

The Astro adapter's local dev experience with `netlify dev` varies — for Blobs and DB access, `netlify dev` is recommended. If using `@netlify/vite-plugin` alongside Astro, local platform primitives may also be available via the standard dev server, but this integration is less mature than with pure Vite projects.

## Build and Deploy

```toml
# netlify.toml
[build]
command = "astro build"
publish = "dist"
```

The adapter configures the publish directory and function routing automatically.

```

## File: skills\netlify-frameworks\references\nextjs.md
```
# Next.js on Netlify

## Setup

Next.js on Netlify uses the `@netlify/next` runtime, which is installed automatically. No manual adapter installation is required — Netlify detects Next.js and configures the build automatically.

```toml
# netlify.toml
[build]
command = "next build"
publish = ".next"
```

## What the Runtime Does

- Converts Next.js server-side features (SSR, API routes, middleware, ISR) into Netlify Functions and Edge Functions
- Handles image optimization via Netlify Image CDN
- Maps Next.js routing to Netlify's infrastructure
- Supports App Router and Pages Router

## Key Configuration

### next.config.js

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [
      { protocol: "https", hostname: "example.com" },
    ],
  },
};

module.exports = nextConfig;
```

Remote image patterns in `next.config.js` are automatically mapped to Netlify Image CDN's `remote_images` configuration.

## API Routes

Next.js API routes work automatically — they are deployed as Netlify Functions:

```typescript
// app/api/items/route.ts (App Router)
export async function GET() {
  return Response.json({ items: [] });
}

export async function POST(request: Request) {
  const data = await request.json();
  return Response.json({ created: data }, { status: 201 });
}
```

## Middleware

Next.js middleware is deployed as a Netlify Edge Function:

```typescript
// middleware.ts
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

export function middleware(request: NextRequest) {
  // Runs at the edge on Netlify
  return NextResponse.next();
}
```

## ISR (Incremental Static Regeneration)

ISR works on Netlify. Pages with `revalidate` are cached and revalidated using Netlify's CDN cache with `stale-while-revalidate`. On-demand revalidation via `revalidatePath` and `revalidateTag` triggers Netlify cache purge.

## Local Development

```bash
npm run dev    # next dev — standard Next.js dev server
```

For Netlify-specific features (environment variables, edge middleware testing), use:

```bash
netlify dev
```

## Known Patterns

- **Static export** (`output: "export"`): Works without the runtime — produces a fully static site
- **Standalone mode** is not required; the Netlify runtime handles deployment automatically
- Environment variables use the `NEXT_PUBLIC_` prefix for client-side access

```

## File: skills\netlify-frameworks\references\tanstack.md
```
# TanStack Start on Netlify

## Setup

TanStack Start uses the Netlify Vite plugin for deployment.

```bash
npm install @netlify/vite-plugin
```

```typescript
// app.config.ts
import { defineConfig } from "@tanstack/react-start/config";
import netlify from "@netlify/vite-plugin";

export default defineConfig({
  vite: {
    plugins: [netlify()],
  },
});
```

## What the Plugin Does

- Handles SSR output for Netlify Functions
- Enables Netlify platform primitives (Blobs, DB, env vars) in local dev
- Maps TanStack Start's file-based routing to Netlify's infrastructure

## Server Functions

TanStack Start uses `createServerFn` for server-side logic. These are automatically handled by the Netlify Vite plugin — no raw Netlify Functions needed:

```typescript
import { createServerFn } from "@tanstack/react-start";

const getItems = createServerFn({ method: "GET" }).handler(async () => {
  // Server-side code — runs as Netlify Function in production
  const items = await db.select().from(itemsTable);
  return items;
});
```

## Local Development

```bash
npm run dev    # Uses Vite plugin — Netlify primitives available
```

The Vite plugin provides Functions, Blobs, DB, and environment variables during local dev without needing `netlify dev`.

## Build and Deploy

```toml
# netlify.toml
[build]
command = "npm run build"
publish = ".output/public"
```

The Vite plugin configures the output structure for Netlify automatically.

```

## File: skills\netlify-frameworks\references\vite.md
```
# Vite + React on Netlify

## Setup

Install the Netlify Vite plugin:

```bash
npm install @netlify/vite-plugin
```

```typescript
// vite.config.ts
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import netlify from "@netlify/vite-plugin";

export default defineConfig({
  plugins: [react(), netlify()],
});
```

## What the Plugin Does

- Enables Netlify Functions, Blobs, DB, and environment variables in local dev
- Handles build output for Netlify deployment
- No need for `netlify dev` — run `npm run dev` directly

## SPA Routing

For client-side routing (React Router, etc.), add the catch-all redirect:

```toml
# netlify.toml
[[redirects]]
from = "/*"
to = "/index.html"
status = 200
```

## Netlify Functions

Write functions in `netlify/functions/` as usual. The Vite plugin makes them available during local dev at their configured paths.

```typescript
// netlify/functions/api.ts
import type { Config, Context } from "@netlify/functions";

export default async (req: Request, context: Context) => {
  return Response.json({ message: "Hello from API" });
};

export const config: Config = { path: "/api/hello" };
```

## Forms (AJAX Pattern)

Since Vite + React renders forms client-side, include a hidden HTML form for Netlify to detect, and submit via AJAX:

```tsx
// In your React component
function ContactForm() {
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);
    await fetch("/", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams(formData as any).toString(),
    });
  };

  return (
    <form name="contact" method="POST" data-netlify="true" onSubmit={handleSubmit}>
      <input type="hidden" name="form-name" value="contact" />
      {/* fields */}
    </form>
  );
}
```

Also add a hidden form in `index.html`:

```html
<form name="contact" netlify hidden>
  <input type="text" name="name" />
  <input type="email" name="email" />
  <textarea name="message"></textarea>
</form>
```

## Local Dev

```bash
npm run dev   # Uses Vite plugin — Netlify primitives available
```

No `netlify dev` wrapper needed. Functions, Blobs, DB, and environment variables all work.

## Build and Deploy

```toml
# netlify.toml
[build]
command = "npm run build"
publish = "dist"
```

```

## File: skills\netlify-functions\SKILL.md
```
---
name: netlify-functions
description: Guide for writing Netlify serverless functions. Use when creating API endpoints, background processing, scheduled tasks, or any server-side logic using Netlify Functions. Covers modern syntax (default export + Config), TypeScript, path routing, background functions, scheduled functions, streaming, and method routing.
---

# Netlify Functions

## Modern Syntax

Always use the modern default export + Config pattern. Never use the legacy `exports.handler` or named `handler` export.

```typescript
import type { Context, Config } from "@netlify/functions";

export default async (req: Request, context: Context) => {
  return new Response("Hello, world!");
};

export const config: Config = {
  path: "/api/hello",
};
```

The handler receives a standard Web API `Request` and returns a `Response`. The second argument is a Netlify `Context` object.

## File Structure

Place functions in `netlify/functions/`:

```
netlify/functions/
  _shared/           # Non-function shared code (underscore prefix)
    auth.ts
    db.ts
  items.ts           # -> /.netlify/functions/items (or custom path via config)
  users/index.ts     # -> /.netlify/functions/users
```

Use `.ts` or `.mts` extensions. If both `.ts` and `.js` exist with the same name, the `.js` file takes precedence.

## Path Routing

Define custom paths via the `config` export:

```typescript
export const config: Config = {
  path: "/api/items",                    // Static path
  // path: "/api/items/:id",            // Path parameter
  // path: ["/api/items", "/api/items/:id"], // Multiple paths
  // excludedPath: "/api/items/special", // Excluded paths
  // preferStatic: true,                // Don't override static files
};
```

Without a `path` config, functions are available at `/.netlify/functions/{name}`. Setting a `path` makes the function available **only** at that path.

Access path parameters via `context.params`:

```typescript
// config: { path: "/api/items/:id" }
export default async (req: Request, context: Context) => {
  const { id } = context.params;
  // ...
};
```

## Method Routing

```typescript
export default async (req: Request, context: Context) => {
  switch (req.method) {
    case "GET":    return handleGet(context.params.id);
    case "POST":   return handlePost(await req.json());
    case "DELETE": return handleDelete(context.params.id);
    default:       return new Response("Method not allowed", { status: 405 });
  }
};

export const config: Config = {
  path: "/api/items/:id",
  method: ["GET", "POST", "DELETE"],
};
```

## Background Functions

For long-running tasks (up to 15 minutes). The client receives an immediate `202` response; return values are ignored.

Name the file with a `-background` suffix:

```
netlify/functions/process-background.ts
```

Store results externally (Netlify Blobs, database) for later retrieval.

## Scheduled Functions

Run on a cron schedule (UTC timezone):

```typescript
export default async (req: Request) => {
  const { next_run } = await req.json();
  console.log("Next invocation at:", next_run);
};

export const config: Config = {
  schedule: "@hourly", // or cron: "0 * * * *"
};
```

Shortcuts: `@yearly`, `@monthly`, `@weekly`, `@daily`, `@hourly`. Scheduled functions have a **30-second timeout** and only run on published deploys.

## Streaming Responses

Return a `ReadableStream` body for streamed responses (up to 20 MB):

```typescript
export default async (req: Request) => {
  const stream = new ReadableStream({ /* ... */ });
  return new Response(stream, {
    headers: { "Content-Type": "text/event-stream" },
  });
};
```

## Context Object

| Property | Description |
|---|---|
| `context.params` | Path parameters from config |
| `context.geo` | `{ city, country: {code, name}, latitude, longitude, subdivision, timezone, postalCode }` |
| `context.ip` | Client IP address |
| `context.cookies` | `.get()`, `.set()`, `.delete()` |
| `context.deploy` | `{ context, id, published }` |
| `context.site` | `{ id, name, url }` |
| `context.account.id` | Team account ID |
| `context.requestId` | Unique request ID |
| `context.waitUntil(promise)` | Extend execution after response is sent |

## Environment Variables

Use `Netlify.env` (not `process.env`) inside functions:

```typescript
const apiKey = Netlify.env.get("API_KEY");
```

## Resource Limits

| Resource | Limit |
|---|---|
| Synchronous timeout | 60 seconds |
| Background timeout | 15 minutes |
| Scheduled timeout | 30 seconds |
| Memory | 1024 MB |
| Buffered payload | 6 MB |
| Streamed payload | 20 MB |

## Framework Considerations

Frameworks with server-side capabilities (Astro, Next.js, Nuxt, SvelteKit, TanStack Start) typically generate their own serverless functions via adapters. You usually do not write raw Netlify Functions in these projects — the framework adapter handles server-side rendering and API routes. Write Netlify Functions directly when:

- Using a client-side-only framework (Vite + React SPA, vanilla JS)
- Adding background or scheduled tasks to any project
- Building standalone API endpoints outside the framework's routing

See the **netlify-frameworks** skill for adapter setup.

```

## File: skills\netlify-identity\SKILL.md
```
---
name: netlify-identity
description: Use when the task involves authentication, user signups, logins, password recovery, OAuth providers, role-based access control, or protecting routes and functions. Always use `@netlify/identity`. Never use `netlify-identity-widget` or `gotrue-js` — they are deprecated.
---

# Netlify Identity

Netlify Identity is a user management service for signups, logins, password recovery, user metadata, and role-based access control. It is built on [GoTrue](https://github.com/netlify/gotrue) and issues JSON Web Tokens (JWTs).

**Always use `@netlify/identity`.** Never use `netlify-identity-widget` or `gotrue-js` — they are deprecated. `@netlify/identity` provides a unified, headless TypeScript API that works in both browser and server contexts (Netlify Functions, Edge Functions, SSR frameworks).

## Setup

```bash
npm install @netlify/identity
```

Identity is automatically enabled when a deploy created by a Netlify Agent Runner session includes Identity code. Otherwise, it must be manually enabled in the UI. These are the default settings:

- **Registration** — Open (anyone can sign up). Change to Invite only in **Project configuration > Identity** if needed.
- **Autoconfirm** — Off (new signups require email confirmation). Enable in **Project configuration > Identity** to skip confirmation during development.

### Local Development

Identity does **not** currently work with `netlify dev`. You must deploy to Netlify to test Identity features. Use `npx netlify deploy` for preview deploys during development. This limitation may be resolved in a future release.

## Quick Start

Log in from the browser:

```typescript
import { login, getUser } from '@netlify/identity'

const user = await login('user@example.com', '<password>')
console.log(`Hello, ${user.name}`)

// Later, check auth state
const currentUser = await getUser()
```

Protect a Netlify Function:

```typescript
// netlify/functions/protected.mts
import { getUser } from '@netlify/identity'
import type { Context } from '@netlify/functions'

export default async (req: Request, context: Context) => {
  const user = await getUser()
  if (!user) return new Response('Unauthorized', { status: 401 })
  return Response.json({ id: user.id, email: user.email })
}
```

## Core API

Import and use headless functions directly:

```typescript
import {
  getUser,
  handleAuthCallback,
  login,
  logout,
  signup,
  oauthLogin,
  onAuthChange,
  getSettings,
} from '@netlify/identity'
```

### Login

```typescript
import { login, AuthError } from '@netlify/identity'

async function handleLogin(email: string, password: string) {
  try {
    const user = await login(email, password)
    showSuccess(`Welcome back, ${user.name ?? user.email}`)
  } catch (error) {
    if (error instanceof AuthError) {
      showError(error.status === 401 ? 'Invalid email or password.' : error.message)
    }
  }
}
```

### Signup

After signup, check `user.emailVerified` to determine if the user was auto-confirmed or needs to confirm their email.

```typescript
import { signup, AuthError } from '@netlify/identity'

async function handleSignup(email: string, password: string, name: string) {
  try {
    const user = await signup(email, password, { full_name: name })
    if (user.emailVerified) {
      // Autoconfirm ON — user is logged in immediately
      showSuccess('Account created. You are now logged in.')
    } else {
      // Autoconfirm OFF — confirmation email sent
      showSuccess('Check your email to confirm your account.')
    }
  } catch (error) {
    if (error instanceof AuthError) {
      showError(error.status === 403 ? 'Signups are not allowed.' : error.message)
    }
  }
}
```

### Logout

```typescript
import { logout } from '@netlify/identity'

await logout()
```

### OAuth

OAuth is a two-step flow: `oauthLogin(provider)` redirects away from the site, then `handleAuthCallback()` processes the redirect when the user returns.

```typescript
import { oauthLogin } from '@netlify/identity'

// Step 1: Redirect to provider (navigates away — never returns)
function handleOAuthClick(provider: 'google' | 'github' | 'gitlab' | 'bitbucket') {
  oauthLogin(provider)
}
```

Enable providers in **Project configuration > Identity > External providers** before using OAuth.

### Handling Callbacks

Always call `handleAuthCallback()` on page load in any app that uses OAuth, password recovery, invites, or email confirmation. It processes all callback types via the URL hash.

```typescript
import { handleAuthCallback, AuthError } from '@netlify/identity'

async function processCallback() {
  try {
    const result = await handleAuthCallback()
    if (!result) return // No callback hash — normal page load

    switch (result.type) {
      case 'oauth':
        showSuccess(`Logged in as ${result.user?.email}`)
        break
      case 'confirmation':
        showSuccess('Email confirmed. You are now logged in.')
        break
      case 'recovery':
        // User is authenticated but must set a new password
        showPasswordResetForm(result.user)
        break
      case 'invite':
        // User must set a password to accept the invite
        showInviteAcceptForm(result.token)
        break
      case 'email_change':
        showSuccess('Email address updated.')
        break
    }
  } catch (error) {
    if (error instanceof AuthError) showError(error.message)
  }
}
```

### Auth State

```typescript
import { getUser, onAuthChange, AUTH_EVENTS } from '@netlify/identity'

// Check current user (never throws — returns null if not authenticated)
const user = await getUser()

// Subscribe to auth state changes (returns unsubscribe function)
const unsubscribe = onAuthChange((event, user) => {
  switch (event) {
    case AUTH_EVENTS.LOGIN:
      console.log('Logged in:', user?.email)
      break
    case AUTH_EVENTS.LOGOUT:
      console.log('Logged out')
      break
    case AUTH_EVENTS.TOKEN_REFRESH:
      break
    case AUTH_EVENTS.USER_UPDATED:
      console.log('Profile updated:', user?.email)
      break
    case AUTH_EVENTS.RECOVERY:
      console.log('Password recovery initiated')
      break
  }
})
```

### Settings-Driven UI

Fetch the project's Identity settings to conditionally render signup forms and OAuth buttons.

```typescript
import { getSettings } from '@netlify/identity'

const settings = await getSettings()
// settings.autoconfirm — boolean
// settings.disableSignup — boolean
// settings.providers — Record<AuthProvider, boolean>

if (!settings.disableSignup) showSignupForm()

for (const [provider, enabled] of Object.entries(settings.providers)) {
  if (enabled) showOAuthButton(provider)
}
```

## Minimal React Example

```tsx
import { useEffect, useState } from 'react'
import {
  getUser,
  handleAuthCallback,
  login,
  logout,
  oauthLogin,
  onAuthChange,
} from '@netlify/identity'

function App() {
  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    ;(async () => {
      await handleAuthCallback()
      setUser(await getUser())
      setLoading(false)
    })()
    return onAuthChange((_event, currentUser) => setUser(currentUser))
  }, [])

  const handleLogin = async (email, password) => {
    const currentUser = await login(email, password)
    setUser(currentUser)
  }

  const handleGoogleLogin = () => oauthLogin('google')

  const handleSignOut = async () => {
    await logout()
    setUser(null)
  }

  if (loading) return <p>Loading...</p>
  // Render login form or user details based on `user` state
}
```

## Error Handling

`@netlify/identity` throws two error classes:

- **`AuthError`** — Thrown by auth operations. Has `message`, optional `status` (HTTP status code), and optional `cause`.
- **`MissingIdentityError`** — Thrown when Identity is not configured in the current environment.

`getUser()` and `isAuthenticated()` never throw — they return `null` and `false` respectively on failure.

| Status | Meaning |
|--------|---------|
| 401 | Invalid credentials or expired token |
| 403 | Action not allowed (e.g., signups disabled) |
| 422 | Validation error (e.g., weak password, malformed email) |
| 404 | User or resource not found |

## Identity Event Functions

Special serverless functions that trigger on Identity lifecycle events. These use the **legacy named `handler` export** (not the modern default export).

**Event names:** `identity-validate`, `identity-signup`, `identity-login`

```typescript
// netlify/functions/identity-signup.mts
import type { Handler, HandlerEvent, HandlerContext } from '@netlify/functions'

const handler: Handler = async (event: HandlerEvent, context: HandlerContext) => {
  const { user } = JSON.parse(event.body || '{}')

  return {
    statusCode: 200,
    body: JSON.stringify({
      app_metadata: {
        ...user.app_metadata,
        roles: ['member'],
      },
    }),
  }
}

export { handler }
```

The response body replaces `app_metadata` and/or `user_metadata` on the user record — include all fields you want to keep.

## Roles and Authorization

- **`app_metadata.roles`** — Server-controlled. Only settable via the Netlify UI, admin API, or Identity event functions. Never let users set their own roles.
- **`user_metadata`** — User-controlled. Users can update via `updateUser({ data: { ... } })`.

### Role-Based Redirects

```toml
# netlify.toml
[[redirects]]
  from = "/admin/*"
  to = "/admin/:splat"
  status = 200
  conditions = { Role = ["admin"] }

[[redirects]]
  from = "/admin/*"
  to = "/"
  status = 302
```

Rules are evaluated top-to-bottom. The `nf_jwt` cookie is read by the CDN to evaluate role conditions.

## References


```

## File: skills\netlify-identity\references\advanced_patterns.md
```
# Advanced Identity Patterns

## Password Recovery

Three-step flow: request recovery email, handle the callback, then set a new password.

```typescript
import { requestPasswordRecovery, handleAuthCallback, updateUser, AuthError } from '@netlify/identity'

// Step 1: Send recovery email
async function handleForgotPassword(email: string) {
  try {
    await requestPasswordRecovery(email)
    showSuccess('Check your email for a password reset link.')
  } catch (error) {
    if (error instanceof AuthError) showError(error.message)
  }
}

// Step 2: handleAuthCallback() returns { type: 'recovery', user } — show password reset form
// (See the handleAuthCallback switch in SKILL.md)

// Step 3: Set new password
async function handlePasswordReset(newPassword: string) {
  try {
    await updateUser({ password: newPassword })
    showSuccess('Password updated.')
  } catch (error) {
    if (error instanceof AuthError) showError(error.message)
  }
}
```

The recovery callback fires a `'recovery'` auth event, not `'login'`. The user is authenticated but should be prompted to set a new password before navigating away.

## Invite Acceptance

When a user clicks an invite link, `handleAuthCallback()` returns `{ type: 'invite', user: null, token }`. Use the token to accept the invite and set a password.

```typescript
import { acceptInvite, AuthError } from '@netlify/identity'

async function handleAcceptInvite(token: string, password: string) {
  try {
    const user = await acceptInvite(token, password)
    showSuccess(`Welcome, ${user.email}! Your account is ready.`)
  } catch (error) {
    if (error instanceof AuthError) showError(error.message)
  }
}
```

## Email Change

When a user verifies an email change, `handleAuthCallback()` returns `{ type: 'email_change', user }`. The user must be logged in when clicking the verification link.

```typescript
import { verifyEmailChange, AuthError } from '@netlify/identity'

async function handleEmailChangeVerification(token: string) {
  try {
    const user = await verifyEmailChange(token)
    showSuccess(`Email updated to ${user.email}`)
  } catch (error) {
    if (error instanceof AuthError) showError(error.message)
  }
}
```

## Session Hydration

`hydrateSession()` bridges server-set cookies to the browser session. Call it on page load when using server-side login (e.g., login inside a Netlify Function followed by a redirect).

```typescript
import { hydrateSession } from '@netlify/identity'

const user = await hydrateSession()
if (user) {
  // Browser session is now in sync with server-set cookies
}
```

`getUser()` auto-hydrates from the `nf_jwt` cookie if no browser session exists, so explicit `hydrateSession()` is only needed when you want to restore the full session (including token refresh timers) after a server-side login.

## SSR Integration Patterns

For SSR frameworks, the recommended pattern is:

- **Browser-side** for auth mutations: `login()`, `signup()`, `logout()`, `oauthLogin()`
- **Server-side** for reading auth state: `getUser()`, `getSettings()`, `getIdentityConfig()`

Browser-side auth mutations set the `nf_jwt` cookie and localStorage, and emit `onAuthChange` events. The server reads the cookie on the next request.

The library also supports server-side mutations (`login()`, `signup()`, `logout()` inside Netlify Functions), but these require the Netlify Functions runtime to set cookies. After a server-side mutation, use a full page navigation so the browser sends the new cookie.

Always use `window.location.href` (not framework router navigation) after server-side auth mutations in Next.js, TanStack Start, and SvelteKit. Remix `redirect()` is safe because Remix actions return real HTTP responses.

## Full API Reference

For the complete API reference — all function signatures, type definitions, OAuth helpers, admin operations, session management, auth events, and framework-specific examples — read the package README:

```
node_modules/@netlify/identity/README.md
```

The README is shipped with the npm package and is always in sync with the installed version.

```

## File: skills\netlify-image-cdn\SKILL.md
```
---
name: netlify-image-cdn
description: Guide for using Netlify Image CDN for image optimization and transformation. Use when serving optimized images, creating responsive image markup, setting up user-uploaded image pipelines, or configuring image transformations. Covers the /.netlify/images endpoint, query parameters, remote image allowlisting, clean URL rewrites, and composing uploads with Functions + Blobs.
---

# Netlify Image CDN

Every Netlify site has a built-in `/.netlify/images` endpoint for on-the-fly image transformation. No configuration required for local images.

## Basic Usage

```html
<img src="/.netlify/images?url=/photo.jpg&w=800&h=600&fit=cover&q=80" />
```

## Query Parameters

| Param | Description | Values |
|---|---|---|
| `url` | Source image path (required) | Relative path or absolute URL |
| `w` | Width in pixels | Any positive integer |
| `h` | Height in pixels | Any positive integer |
| `fit` | Resize behavior | `contain` (default), `cover`, `fill` |
| `position` | Crop alignment (with `cover`) | `center` (default), `top`, `bottom`, `left`, `right` |
| `fm` | Output format | `avif`, `webp`, `jpg`, `png`, `gif`, `blurhash` |
| `q` | Quality (lossy formats) | 1-100 (default: 75) |

When `fm` is omitted, Netlify auto-negotiates the best format based on browser support (preferring `webp`, then `avif`).

## Remote Image Allowlisting

External images must be explicitly allowed in `netlify.toml`:

```toml
[images]
remote_images = ["https://example\\.com/.*", "https://cdn\\.images\\.com/.*"]
```

Values are regex patterns.

## Clean URL Rewrites

Create user-friendly image URLs with redirects:

```toml
# Basic optimization
[[redirects]]
from = "/img/*"
to = "/.netlify/images?url=/:splat"
status = 200

# Preset: thumbnail
[[redirects]]
from = "/img/thumb/:key"
to = "/.netlify/images?url=/uploads/:key&w=150&h=150&fit=cover"
status = 200

# Preset: hero
[[redirects]]
from = "/img/hero/:key"
to = "/.netlify/images?url=/uploads/:key&w=1200&h=675&fit=cover"
status = 200
```

## Caching

- Transformed images are cached at the CDN edge automatically
- Cache invalidates on new deploys
- Set cache headers on source images to control caching:

```toml
[[headers]]
for = "/uploads/*"
[headers.values]
Cache-Control = "public, max-age=31536000, immutable"
```

## User-Uploaded Images

Combine **Netlify Functions** (upload handler) + **Netlify Blobs** (storage) + **Image CDN** (serving/transforming) to build a complete user-uploaded image pipeline. See references/user-uploads.md for the full pattern.

```

## File: skills\netlify-image-cdn\references\user_uploads.md
```
# User-Uploaded Images Pipeline

Compose Netlify Functions (upload handler) + Netlify Blobs (storage) + Image CDN (serving/transforming) to build a complete user-uploaded image pipeline.

## Architecture

1. **Upload** — A Netlify Function receives multipart form data, validates, and stores in Blobs
2. **Storage** — Netlify Blobs stores the binary image with metadata
3. **Serve** — A Netlify Function retrieves the blob and serves it at `/uploads/:key`
4. **Transform** — A redirect maps `/img/:key` to `/.netlify/images?url=/uploads/:key` for CDN optimization

## Dependencies

```bash
npm install @netlify/blobs
```

## Upload Handler

```typescript
// netlify/functions/upload.ts
import type { Context, Config } from "@netlify/functions";
import { getStore } from "@netlify/blobs";
import { randomUUID } from "crypto";

const ALLOWED_TYPES = ["image/jpeg", "image/png", "image/gif", "image/webp"];
const MAX_SIZE = 4 * 1024 * 1024; // 4 MB

export default async (req: Request, context: Context) => {
  if (req.method !== "POST") {
    return new Response("Method not allowed", { status: 405 });
  }

  const formData = await req.formData();
  const image = formData.get("image") as File;

  if (!image) return Response.json({ error: "No image provided" }, { status: 400 });
  if (!ALLOWED_TYPES.includes(image.type)) return Response.json({ error: "Invalid type" }, { status: 400 });
  if (image.size > MAX_SIZE) return Response.json({ error: "File too large" }, { status: 400 });

  const extension = image.name.split(".").pop() || "jpg";
  const key = `${randomUUID()}.${extension}`;
  const store = getStore({ name: "images", consistency: "strong" });

  await store.set(key, image, {
    metadata: {
      contentType: image.type,
      originalFilename: image.name,
      uploadedAt: new Date().toISOString(),
    },
  });

  return Response.json({ success: true, key, url: `/img/${key}` });
};

export const config: Config = { path: "/api/upload", method: "POST" };
```

## Serve Handler

```typescript
// netlify/functions/serve-image.ts
import type { Context, Config } from "@netlify/functions";
import { getStore } from "@netlify/blobs";

export default async (req: Request, context: Context) => {
  const key = context.params.key;
  const store = getStore({ name: "images", consistency: "strong" });

  const result = await store.getWithMetadata(key, { type: "stream" });
  if (!result) return new Response("Not found", { status: 404 });

  return new Response(result.data, {
    headers: {
      "Content-Type": result.metadata?.contentType || "image/jpeg",
      "Cache-Control": "public, max-age=31536000, immutable",
    },
  });
};

export const config: Config = { path: "/uploads/:key" };
```

## CDN Redirect

```toml
# netlify.toml

# Basic optimized URL
[[redirects]]
from = "/img/:key"
to = "/.netlify/images?url=/uploads/:key"
status = 200

# Thumbnail preset
[[redirects]]
from = "/img/thumb/:key"
to = "/.netlify/images?url=/uploads/:key&w=150&h=150&fit=cover"
status = 200

# Hero preset
[[redirects]]
from = "/img/hero/:key"
to = "/.netlify/images?url=/uploads/:key&w=1200&h=675&fit=cover"
status = 200
```

## Client-Side Upload (React Example)

```tsx
function ImageUpload({ onUpload }: { onUpload: (url: string) => void }) {
  const handleChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("image", file);

    const res = await fetch("/api/upload", { method: "POST", body: formData });
    const { url } = await res.json();
    onUpload(url);
  };

  return <input type="file" accept="image/*" onChange={handleChange} />;
}
```

## Astro Upload (API Route)

```typescript
// src/pages/api/upload.ts
import type { APIRoute } from "astro";
import { getStore } from "@netlify/blobs";
import { randomUUID } from "crypto";

export const POST: APIRoute = async ({ request, redirect }) => {
  const formData = await request.formData();
  const image = formData.get("image") as File;
  if (!image) return new Response("No image", { status: 400 });

  const key = `${randomUUID()}.${image.name.split(".").pop() || "jpg"}`;
  const store = getStore({ name: "images", consistency: "strong" });
  await store.set(key, image, {
    metadata: { contentType: image.type, originalFilename: image.name },
  });

  return redirect(`/gallery?uploaded=${key}`);
};
```

## Key Points

- Always validate file type and size on the server (client validation can be bypassed)
- Use `strong` consistency on Blobs for immediate reads after writes
- The serve handler's `Cache-Control: immutable` means the CDN caches the raw image permanently — Image CDN transformations layer on top
- Without `fm` parameter, Netlify auto-serves AVIF or WebP based on browser support

```

