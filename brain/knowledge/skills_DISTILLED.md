---
id: skills
type: knowledge
owner: OA_Triage
---
# skills
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "@composiohq/skills",
  "version": "1.0.6",
  "description": "Agent skills for Composio developers",
  "type": "module",
  "license": "MIT",
  "author": "Composio",
  "repository": {
    "type": "git",
    "url": "https://github.com/composiohq/skills.git"
  },
  "scripts": {
    "build:agents": "node scripts/build-agents.cjs",
    "watch:agents": "node scripts/watch-agents.cjs",
    "build": "npm run build:agents"
  }
}

```

### File: README.md
```md
# @composiohq/skills

Distributable agent skills for Composio developers. This repository contains comprehensive guides and best practices for building AI agents with Composio's Tool Router and Triggers.

## Quick Start

Add Composio skills to your AI assistant:

```bash
npx skills add composiohq/skills
```

This command installs the Composio agent skills, giving your AI assistant access to:
- **Tool Router best practices** - Session management, authentication, and framework integration
- **Triggers & Events** - Real-time webhooks and event handling
- **Production patterns** - Security, error handling, and deployment guides

Your AI assistant can now reference these skills when helping you build with Composio!

## Overview

This skills repository provides comprehensive guides and best practices for building AI agents with Composio, organized as markdown files that AI assistants can easily reference.

## Structure

```
skills/
└── composio/
    ├── SKILL.md           # Main skill overview with rule references
    ├── AGENTS.md          # Consolidated single-file version (auto-generated)
    └── rules/             # Individual rule files
        ├── tr-*.md        # Tool Router rules
        └── triggers-*.md  # Trigger rules
```

## Available Skills

### 1. Tool Router (Building Agents)
- User ID best practices for security
- Creating and managing sessions
- Session lifecycle patterns
- Native tools vs MCP integration
- Framework integration (Vercel, OpenAI Agents, LangChain, Claude, CrewAI)

### 2. Authentication
- Auto authentication in chat
- Manual authorization flows
- Connection management

### 3. Toolkits & Connection Status
- Querying toolkit availability
- Building connection UIs

### 4. Advanced Features (Triggers & Events)
- Creating triggers for real-time events
- Subscribing to events (development only)
- Webhook verification (production recommended)
- Managing trigger lifecycle

## Usage

### For AI Assistants

Read either:
- **SKILL.md** - Main file with links to individual rules (faster to navigate)
- **AGENTS.md** - Single consolidated file with all content (easier to consume)

### For Developers

#### Build AGENTS.md

Automatically generate the consolidated AGENTS.md file from all rule files:

```bash
npm run build:agents
```

This script:
- Reads SKILL.md for structure
- Extracts all rule references
- Combines individual rule files
- Generates table of contents
- Outputs AGENTS.md with proper formatting

#### Watch Mode

Auto-rebuild AGENTS.md when any file changes:

```bash
npm run watch:agents
```

This watches:
- `SKILL.md` for structure changes
- `rules/*.md` for content changes
- Auto-rebuilds on any modification

## Contributing

### Adding a New Rule

1. Create a new markdown file in `skills/composio/rules/`
2. Use the naming convention:
   - `tr-*.md` for Tool Router rules
   - `triggers-*.md` for Trigger rules
3. Include frontmatter:

```markdown
---
title: Your Rule Title
impact: CRITICAL|HIGH|MEDIUM|LOW
description: Brief description of what this rule covers
tags: [tool-router, triggers, etc]
---

# Your Rule Title

Content with ❌ Incorrect and ✅ Correct examples...
```

4. Add reference to `SKILL.md` in the appropriate section
5. Run `npm run build:agents` to regenerate AGENTS.md
6. Commit all changes (rule file, SKILL.md, and AGENTS.md)

### Rule Format

Each rule should include:
- **Frontmatter** with metadata
- **❌ Incorrect examples** showing what not to do
- **✅ Correct examples** showing best practices
- **Explanations** of why each approach is better
- **Code examples** in both TypeScript and Python (when applicable)
- **References** to official documentation

## Build Scripts

The repository includes two scripts in `scripts/`:

### build-agents.cjs

Generates the consolidated AGENTS.md file:
- Parses SKILL.md for structure
- Reads all rule files
- Combines content with proper formatting
- Generates table of contents
- Adds impact badges and descriptions

### watch-agents.cjs

Watches for file changes and auto-rebuilds:
- Monitors SKILL.md and rules/ directory
- Triggers rebuild on any .md file change
- Shows real-time build status

## File Statistics

Current repository stats:
- **14+ rules** covering Tool Router and Triggers
- **150+ KB** of consolidated documentation
- **Both TypeScript and Python** examples throughout
- **Production-ready** patterns and best practices

## Key Features

### Tool Router Coverage
- Session management and lifecycle
- User isolation patterns
- Native tools vs MCP comparison
- Framework integration guides
- Connection management
- Authentication flows

### Triggers Coverage
- Creating trigger instances
- Real-time event subscription
- Webhook verification and security
- Trigger lifecycle management
- Production deployment patterns

## License

MIT

## Links

- [Composio Documentation](https://docs.composio.dev)
- [Tool Router API](https://docs.composio.dev/sdk/typescript/api/tool-router)
- [Triggers API](https://docs.composio.dev/sdk/typescript/api/triggers)
- [GitHub Repository](https://github.com/composiohq/skills)

```

### File: skills\README.md
```md
# skills/

该目录用于存放所有技能定义，每个技能一个子目录。  
This directory stores all skill definitions, one subdirectory per skill.

## 目录约定 / Directory Convention

- `skills/<skill-name>/SKILL.md`
- `<skill-name>` 使用小写短横线（kebab-case） / Use kebab-case for `<skill-name>`

## 示例 / Examples

- `skills/characteristic-voice/SKILL.md`：情绪化/人格化语音能力示例 / Expressive voice capability example
- `skills/tts/SKILL.md`：语音生成流程示例 / Voice generation workflow example
- `skills/template-skill/SKILL.md`：可复制模板 / Reusable template

```

### File: skills\cloudflare\references\api\README.md
```md
# Cloudflare API Integration

Guide for working with Cloudflare's REST API - authentication, SDK usage, common patterns, and troubleshooting.

## Quick Decision Tree

```
How are you calling the Cloudflare API?
├─ From Workers runtime → Use bindings, not REST API (see ../bindings/)
├─ Server-side (Node/Python/Go) → Official SDK (see api.md)
├─ CLI/scripts → Wrangler or curl (see configuration.md)
├─ Infrastructure-as-code → See ../pulumi/ or ../terraform/
└─ One-off requests → curl examples (see api.md)
```

## SDK Selection

| Language | Package | Best For | Default Retries |
|----------|---------|----------|-----------------|
| TypeScript | `cloudflare` | Node.js, Bun, Next.js, Workers | 2 |
| Python | `cloudflare` | FastAPI, Django, scripts | 2 |
| Go | `cloudflare-go/v4` | CLI tools, microservices | 10 |

All SDKs are Stainless-generated from OpenAPI spec (consistent APIs).

## Authentication Methods

| Method | Security | Use Case | Scope |
|--------|----------|----------|-------|
| **API Token** ✓ | Scoped, rotatable | Production | Per-zone or account |
| API Key + Email | Full account access | Legacy only | Everything |
| User Service Key | Limited | Origin CA certs only | Origin CA |

**Always use API tokens** for new projects.

## Rate Limits

| Limit | Value |
|-------|-------|
| Per user/token | 1200 requests / 5 minutes |
| Per IP | 200 requests / second |
| GraphQL | 320 / 5 minutes (cost-based) |

## Reading Order

| Task | Files to Read |
|------|---------------|
| Initialize SDK client | api.md |
| Configure auth/timeout/retry | configuration.md |
| Find usage patterns | patterns.md |
| Debug errors/rate limits | gotchas.md |
| Product-specific APIs | ../workers/, ../r2/, ../kv/, etc. |

## In This Reference

- **[api.md](api.md)** - SDK client initialization, pagination, error handling, examples
- **[configuration.md](configuration.md)** - Environment variables, SDK config, Wrangler setup
- **[patterns.md](patterns.md)** - Real-world patterns, batch operations, workflows
- **[gotchas.md](gotchas.md)** - Rate limits, SDK-specific issues, troubleshooting

## See Also

- [Cloudflare API Docs](https://developers.cloudflare.com/api/)
- [Bindings Reference](../bindings/) - Workers runtime bindings (preferred over REST API)
- [Wrangler Reference](../wrangler/) - CLI tool for Cloudflare development
- [GraphQL Analytics API Reference](../graphql-api/) - Analytics data via GraphQL (separate endpoint from REST API)

```

### File: skills\cloudflare\references\containers\README.md
```md
# Cloudflare Containers Skill Reference

**APPLIES TO: Cloudflare Containers ONLY - NOT general Cloudflare Workers**

Use when working with Cloudflare Containers: deploying containerized apps on Workers platform, configuring container-enabled Durable Objects, managing container lifecycle, or implementing stateful/stateless container patterns.

## Beta Status

⚠️ Containers is currently in **beta**. API may change without notice. No SLA guarantees. Custom instance types added Jan 2026.

## Core Concepts

**Container as Durable Object:** Each container is a Durable Object with persistent identity. Accessed via `getByName(id)` or `getRandom()`.

**Image deployment:** Images pre-fetched globally. Deployments use rolling strategy (not instant like Workers).

**Lifecycle:** cold start (2-3s) → running → `sleepAfter` timeout → stopped. No autoscaling - manual load balancing via `getRandom()`.

**Persistent identity, ephemeral disk:** Container ID persists, but disk resets on stop. Use Durable Object storage for persistence.

## Quick Start

```typescript
import { Container } from "@cloudflare/containers";

export class MyContainer extends Container {
  defaultPort = 8080;
  sleepAfter = "30m";
}

export default {
  async fetch(request: Request, env: Env) {
    const container = env.MY_CONTAINER.getByName("instance-1");
    await container.startAndWaitForPorts();
    return container.fetch(request);
  }
};
```

## Reading Order

| Task | Files |
|------|-------|
| Setup new container project | README → configuration.md |
| Implement container logic | README → api.md → patterns.md |
| Choose routing pattern | patterns.md (routing section) |
| Debug issues | gotchas.md |
| Production hardening | gotchas.md → patterns.md (lifecycle) |

## Routing Decision Tree

**How should requests reach containers?**

- **Same user/session → same container:** Use `getByName(sessionId)` for session affinity
- **Stateless, spread load:** Use `getRandom()` for load balancing
- **Job per container:** Use `getByName(jobId)` + explicit lifecycle management
- **Single global instance:** Use `getByName("singleton")`

## When to Use Containers vs Workers

**Use Containers when:**
- Need stateful, long-lived processes (sessions, WebSockets, games)
- Running existing containerized apps (Node.js, Python, custom binaries)
- Need filesystem access or specific system dependencies
- Per-user/session isolation with dedicated compute

**Use Workers when:**
- Stateless HTTP handlers
- Sub-millisecond cold starts required
- Auto-scaling to zero critical
- Simple request/response patterns

## In This Reference

- **[configuration.md](configuration.md)** - Wrangler config, instance types, Container class properties, environment variables, account limits
- **[api.md](api.md)** - Container class API, startup methods, communication (HTTP/TCP/WebSocket), routing helpers, lifecycle hooks, scheduling, state inspection
- **[patterns.md](patterns.md)** - Routing patterns (session affinity, load balancing, singleton), WebSocket forwarding, graceful shutdown, Workflow/Queue integration
- **[gotchas.md](gotchas.md)** - Critical gotchas (WebSocket, startup methods), common errors with solutions, specific limits, beta caveats

## See Also

- [Durable Objects](../durable-objects/) - Containers extend Durable Objects
- [Workflows](../workflows/) - Orchestrate container operations
- [Queues](../queues/) - Trigger containers from queue messages
- [Cloudflare Docs](https://developers.cloudflare.com/containers/)

```

### File: skills\cloudflare\references\images\README.md
```md
# Cloudflare Images Skill Reference

**Cloudflare Images** is an end-to-end image management solution providing storage, transformation, optimization, and delivery at scale via Cloudflare's global network.

## Quick Decision Tree

**Need to:**
- **Transform in Worker?** → [api.md](api.md#workers-binding-api-2026-primary-method) (Workers Binding API)
- **Upload from Worker?** → [api.md](api.md#upload-from-worker) (REST API)
- **Upload from client?** → [patterns.md](patterns.md#upload-from-client-direct-creator-upload) (Direct Creator Upload)
- **Set up variants?** → [configuration.md](configuration.md#variants-configuration)
- **Serve responsive images?** → [patterns.md](patterns.md#responsive-images)
- **Add watermarks?** → [patterns.md](patterns.md#watermarking)
- **Fix errors?** → [gotchas.md](gotchas.md#common-errors)

## Reading Order

**For building image upload/transform feature:**
1. [configuration.md](configuration.md) - Setup Workers binding
2. [api.md](api.md#workers-binding-api-2026-primary-method) - Learn transform API
3. [patterns.md](patterns.md#upload-from-client-direct-creator-upload) - Direct upload pattern
4. [gotchas.md](gotchas.md) - Check limits and errors

**For URL-based transforms:**
1. [configuration.md](configuration.md#variants-configuration) - Create variants
2. [api.md](api.md#url-transform-api) - URL syntax
3. [patterns.md](patterns.md#responsive-images) - Responsive patterns

**For troubleshooting:**
1. [gotchas.md](gotchas.md#common-errors) - Error messages
2. [gotchas.md](gotchas.md#limits) - Size/format limits

## Core Methods

| Method | Use Case | Location |
|--------|----------|----------|
| `env.IMAGES.input().transform()` | Transform in Worker | [api.md:11](api.md) |
| REST API `/images/v1` | Upload images | [api.md:57](api.md) |
| Direct Creator Upload | Client-side upload | [api.md:127](api.md) |
| URL transforms | Static image delivery | [api.md:112](api.md) |

## In This Reference

- **[api.md](api.md)** - Complete API: Workers binding, REST endpoints, URL transforms
- **[configuration.md](configuration.md)** - Setup: wrangler.toml, variants, auth, signed URLs
- **[patterns.md](patterns.md)** - Patterns: responsive images, watermarks, format negotiation, caching
- **[gotchas.md](gotchas.md)** - Troubleshooting: limits, errors, best practices

## Key Features

- **Automatic Optimization** - AVIF/WebP format negotiation
- **On-the-fly Transforms** - Resize, crop, blur, sharpen via URL or API
- **Workers Binding** - Transform images in Workers (2026 primary method)
- **Direct Upload** - Secure client-side uploads without backend proxy
- **Global Delivery** - Cached at 300+ Cloudflare data centers
- **Watermarking** - Overlay images programmatically

## See Also

- [Official Docs](https://developers.cloudflare.com/images/)
- [Workers Examples](https://developers.cloudflare.com/images/tutorials/)

```

### File: skills\cloudflare\references\observability\README.md
```md
# Cloudflare Observability Skill Reference

**Purpose**: Comprehensive guidance for implementing observability in Cloudflare Workers, covering traces, logs, metrics, and analytics.

**Scope**: Cloudflare Observability features ONLY - Workers Logs, Traces, Analytics Engine, Logpush, Metrics & Analytics, and OpenTelemetry exports.

---

## Decision Tree: Which File to Load?

Use this to route to the correct file without loading all content:

```
├─ "How do I enable/configure X?"           → configuration.md
├─ "What's the API/method/binding for X?"   → api.md
├─ "How do I implement X pattern?"          → patterns.md
│   ├─ Usage tracking/billing               → patterns.md
│   ├─ Error tracking                       → patterns.md
│   ├─ Performance monitoring               → patterns.md
│   ├─ Multi-tenant tracking                → patterns.md
│   ├─ Tail Worker filtering                → patterns.md
│   └─ OpenTelemetry export                 → patterns.md
└─ "Why isn't X working?" / "Limits?"       → gotchas.md
```

## Reading Order

Load files in this order based on task:

| Task Type | Load Order | Reason |
|-----------|------------|--------|
| **Initial setup** | configuration.md → gotchas.md | Setup first, avoid pitfalls |
| **Implement feature** | patterns.md → api.md → gotchas.md | Pattern → API details → edge cases |
| **Debug issue** | gotchas.md → configuration.md | Common issues first |
| **Query data** | api.md → patterns.md | API syntax → query examples |

## Product Overview

### Workers Logs
- **What:** Console output from Workers (console.log/warn/error)
- **Access:** Dashboard (Real-time Logs), Logpush, Tail Workers
- **Cost:** Free (included with all Workers)
- **Retention:** Real-time only (no historical storage in dashboard)

### Workers Traces
- **What:** Execution traces with timing, CPU usage, outcome
- **Access:** Dashboard (Workers Analytics → Traces), Logpush
- **Cost:** $0.10/1M spans (GA pricing starts March 1, 2026), 10M free/month
- **Retention:** 14 days included

### Analytics Engine
- **What:** High-cardinality event storage and SQL queries
- **Access:** SQL API, Dashboard (Analytics → Analytics Engine)
- **Cost:** $0.25/1M writes beyond 10M free/month
- **Retention:** 90 days (configurable up to 1 year)

### Tail Workers
- **What:** Workers that receive logs/traces from other Workers
- **Use Cases:** Log filtering, transformation, external export
- **Cost:** Standard Workers pricing

### Logpush
- **What:** Stream logs to external storage (S3, R2, Datadog, etc.)
- **Access:** Dashboard, API
- **Cost:** Requires Business/Enterprise plan

## Pricing Summary (2026)

| Feature | Free Tier | Cost Beyond Free Tier | Plan Requirement |
|---------|-----------|----------------------|------------------|
| Workers Logs | Unlimited | Free | Any |
| Workers Traces | 10M spans/month | $0.10/1M spans | Paid Workers (GA: March 1, 2026) |
| Analytics Engine | 10M writes/month | $0.25/1M writes | Paid Workers |
| Logpush | N/A | Included in plan | Business/Enterprise |

## In This Reference

- **[configuration.md](configuration.md)** - Setup, deployment, configuration (Logs, Traces, Analytics Engine, Tail Workers, Logpush)
- **[api.md](api.md)** - API endpoints, methods, interfaces (GraphQL, SQL, bindings, types)
- **[patterns.md](patterns.md)** - Common patterns, use cases, examples (billing, monitoring, error tracking, exports)
- **[gotchas.md](gotchas.md)** - Troubleshooting, best practices, limitations (common errors, performance gotchas, pricing)

## See Also

- [Cloudflare Workers Docs](https://developers.cloudflare.com/workers/)
- [Analytics Engine Docs](https://developers.cloudflare.com/analytics/analytics-engine/)
- [Workers Traces Docs](https://developers.cloudflare.com/workers/observability/traces/)
- [GraphQL Analytics API Reference](../graphql-api/) - Query Workers metrics, HTTP analytics, and 70+ other datasets via GraphQL

```

### File: skills\cloudflare\references\pages\README.md
```md
# Cloudflare Pages

JAMstack platform for full-stack apps on Cloudflare's global network.

## Key Features

- **Git-based deploys**: Auto-deploy from GitHub/GitLab
- **Preview deployments**: Unique URL per branch/PR
- **Pages Functions**: File-based serverless routing (Workers runtime)
- **Static + dynamic**: Smart asset caching + edge compute
- **Smart Placement**: Automatic function optimization based on traffic patterns
- **Framework optimized**: SvelteKit, Astro, Nuxt, Qwik, Solid Start

## Deployment Methods

### 1. Git Integration (Production)
Dashboard → Workers & Pages → Create → Connect to Git → Configure build

### 2. Direct Upload
```bash
npx wrangler pages deploy ./dist --project-name=my-project
npx wrangler pages deploy ./dist --project-name=my-project --branch=staging
```

### 3. C3 CLI
```bash
npm create cloudflare@latest my-app
# Select framework → auto-setup + deploy
```

## vs Workers

- **Pages**: Static sites, JAMstack, frameworks, git workflow, file-based routing
- **Workers**: Pure APIs, complex routing, WebSockets, scheduled tasks, email handlers
- **Combine**: Pages Functions use Workers runtime, can bind to Workers

## Quick Start

```bash
# Create
npm create cloudflare@latest

# Local dev
npx wrangler pages dev ./dist

# Deploy
npx wrangler pages deploy ./dist --project-name=my-project

# Types
npx wrangler types --path='./functions/types.d.ts'

# Secrets
echo "value" | npx wrangler pages secret put KEY --project-name=my-project

# Logs
npx wrangler pages deployment tail --project-name=my-project
```

## Resources

- [Pages Docs](https://developers.cloudflare.com/pages/)
- [Functions API](https://developers.cloudflare.com/pages/functions/api-reference/)
- [Framework Guides](https://developers.cloudflare.com/pages/framework-guides/)
- [Discord #functions](https://discord.com/channels/595317990191398933/910978223968518144)

## Reading Order

**New to Pages?** Start here:
1. README.md (you are here) - Overview & quick start
2. [configuration.md](./configuration.md) - Project setup, wrangler.jsonc, bindings
3. [api.md](./api.md) - Functions API, routing, context
4. [patterns.md](./patterns.md) - Common implementations
5. [gotchas.md](./gotchas.md) - Troubleshooting & pitfalls

**Quick reference?** Jump to relevant file above.

## In This Reference

- [configuration.md](./configuration.md) - wrangler.jsonc, build, env vars, Smart Placement
- [api.md](./api.md) - Functions API, bindings, context, advanced mode
- [patterns.md](./patterns.md) - Full-stack patterns, framework integration
- [gotchas.md](./gotchas.md) - Build issues, limits, debugging, framework warnings

## See Also

- [pages-functions](../pages-functions/) - File-based routing, middleware
- [d1](../d1/) - SQL database for Pages Functions
- [kv](../kv/) - Key-value storage for caching/state

```

### File: skills\cloudflare\references\sandbox\README.md
```md
# Cloudflare Sandbox SDK

Secure isolated code execution in containers on Cloudflare's edge. Run untrusted code, manage files, expose services, integrate with AI agents.

**Use cases**: AI code execution, interactive dev environments, data analysis, CI/CD, code interpreters, multi-tenant execution.

## Architecture

- Each sandbox = Durable Object + Container
- Persistent across requests (same ID = same sandbox)
- Isolated filesystem/processes/network
- Configurable sleep/wake for cost optimization

## Quick Start

```typescript
import { getSandbox, proxyToSandbox, type Sandbox } from '@cloudflare/sandbox';
export { Sandbox } from '@cloudflare/sandbox';

type Env = { Sandbox: DurableObjectNamespace<Sandbox>; };

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    // CRITICAL: proxyToSandbox MUST be called first for preview URLs
    const proxyResponse = await proxyToSandbox(request, env);
    if (proxyResponse) return proxyResponse;

    const sandbox = getSandbox(env.Sandbox, 'my-sandbox');
    const result = await sandbox.exec('python3 -c "print(2 + 2)"');
    return Response.json({ output: result.stdout });
  }
};
```

**wrangler.jsonc**:
```jsonc
{
  "name": "my-sandbox-worker",
  "main": "src/index.ts",
  "compatibility_date": "2025-01-01", // Use current date for new projects
  
  "containers": [{
    "class_name": "Sandbox",
    "image": "./Dockerfile",
    "instance_type": "lite",        // lite | standard | heavy
    "max_instances": 5
  }],
  
  "durable_objects": {
    "bindings": [{ "class_name": "Sandbox", "name": "Sandbox" }]
  },
  
  "migrations": [{
    "tag": "v1",
    "new_sqlite_classes": ["Sandbox"]
  }]
}
```

**Dockerfile**:
```dockerfile
FROM docker.io/cloudflare/sandbox:0.7.0
RUN pip3 install --no-cache-dir pandas numpy matplotlib
EXPOSE 8080 3000  # Required for wrangler dev
```

## Core APIs

- `getSandbox(namespace, id, options?)` → Get/create sandbox
- `sandbox.exec(command, options?)` → Execute command
- `sandbox.readFile(path)` / `writeFile(path, content)` → File ops
- `sandbox.startProcess(command, options)` → Background process
- `sandbox.exposePort(port, options)` → Get preview URL
- `sandbox.createSession(options)` → Isolated session
- `sandbox.wsConnect(request, port)` → WebSocket proxy
- `sandbox.destroy()` → Terminate container
- `sandbox.mountBucket(bucket, path, options)` → Mount S3 storage

## Critical Rules

- ALWAYS call `proxyToSandbox()` first
- Same ID = reuse sandbox
- Use `/workspace` for persistent files
- `normalizeId: true` for preview URLs
- Retry on `CONTAINER_NOT_READY`

## In This Reference
- [configuration.md](./configuration.md) - Config, CLI, environment setup
- [api.md](./api.md) - Programmatic API, testing patterns
- [patterns.md](./patterns.md) - Common workflows, CI/CD integration
- [gotchas.md](./gotchas.md) - Issues, limits, best practices

## See Also
- [durable-objects](../durable-objects/) - Sandbox runs on DO infrastructure
- [containers](../containers/) - Container runtime fundamentals
- [workers](../workers/) - Entry point for sandbox requests

```

### File: skills\cloudflare\references\snippets\README.md
```md
# Cloudflare Snippets Skill Reference

## Description
Expert guidance for **Cloudflare Snippets ONLY** - a lightweight JavaScript-based edge logic platform for modifying HTTP requests and responses. Snippets run as part of the Ruleset Engine and are included at no additional cost on paid plans (Pro, Business, Enterprise).

## What Are Snippets?
Snippets are JavaScript functions executed at the edge as part of Cloudflare's Ruleset Engine. Key characteristics:
- **Execution time**: 5ms CPU limit per request
- **Size limit**: 32KB per snippet
- **Runtime**: V8 isolate (subset of Workers APIs)
- **Subrequests**: 2-5 fetch calls depending on plan
- **Cost**: Included with Pro/Business/Enterprise plans

## Snippets vs Workers Decision Matrix

| Factor | Choose Snippets If... | Choose Workers If... |
|--------|----------------------|---------------------|
| **Complexity** | Simple request/response modifications | Complex business logic, routing, middleware |
| **Execution time** | <5ms sufficient | Need >5ms or variable time |
| **Subrequests** | 2-5 fetch calls sufficient | Need >5 subrequests or complex orchestration |
| **Code size** | <32KB sufficient | Need >32KB or npm dependencies |
| **Cost** | Want zero additional cost | Can afford $5/mo + usage |
| **APIs** | Need basic fetch, headers, URL | Need KV, D1, R2, Durable Objects, cron triggers |
| **Deployment** | Need rule-based triggers | Want custom routing logic |

**Rule of thumb**: Use Snippets for modifications, Workers for applications.

## Execution Model
1. Request arrives at Cloudflare edge
2. Ruleset Engine evaluates snippet rules (filter expressions)
3. If rule matches, snippet executes within 5ms limit
4. Modified request/response continues through pipeline
5. Response returned to client

Snippets execute synchronously in the request path - performance is critical.

## Reading Order
1. **[configuration.md](configuration.md)** - Start here: setup, deployment methods (Dashboard/API/Terraform)
2. **[api.md](api.md)** - Core APIs: Request, Response, headers, `request.cf` properties
3. **[patterns.md](patterns.md)** - Real-world examples: geo-routing, A/B tests, security headers
4. **[gotchas.md](gotchas.md)** - Troubleshooting: common errors, performance tips, API limitations

## In This Reference

- **[configuration.md](configuration.md)** - Setup, deployment, configuration
- **[api.md](api.md)** - API endpoints, methods, interfaces
- **[patterns.md](patterns.md)** - Common patterns, use cases, examples
- **[gotchas.md](gotchas.md)** - Troubleshooting, best practices, limitations

## Quick Start
```javascript
// Snippet: Add security headers
export default {
  async fetch(request) {
    const response = await fetch(request);
    const newResponse = new Response(response.body, response);
    newResponse.headers.set("X-Frame-Options", "DENY");
    newResponse.headers.set("X-Content-Type-Options", "nosniff");
    return newResponse;
  }
}
```

Deploy via Dashboard (Rules → Snippets) or API/Terraform. See configuration.md for details.

## See Also

- [Cloudflare Docs](https://developers.cloudflare.com/rules/snippets/)

```

### File: skills\cloudflare\references\stream\README.md
```md
# Cloudflare Stream

Serverless live and on-demand video streaming platform with one API.

## Overview

Cloudflare Stream provides video upload, storage, encoding, and delivery without managing infrastructure. Runs on Cloudflare's global network.

### Key Features
- **On-demand video**: Upload, encode, store, deliver
- **Live streaming**: RTMPS/SRT ingestion with ABR
- **Direct creator uploads**: End users upload without API keys
- **Signed URLs**: Token-based access control
- **Analytics**: Server-side metrics via GraphQL
- **Webhooks**: Processing notifications
- **Captions**: Upload or AI-generate subtitles
- **Watermarks**: Apply branding to videos
- **Downloads**: Enable MP4 offline viewing

## Core Concepts

### Video Upload Methods
1. **API Upload (TUS protocol)**: Direct server upload
2. **Upload from URL**: Import from external source
3. **Direct Creator Uploads**: User-generated content (recommended)

### Playback Options
1. **Stream Player (iframe)**: Built-in, optimized player
2. **Custom Player (HLS/DASH)**: Video.js, HLS.js integration
3. **Thumbnails**: Static or animated previews

### Access Control
- **Public**: No restrictions
- **requireSignedURLs**: Token-based access
- **allowedOrigins**: Domain restrictions
- **Access Rules**: Geo/IP restrictions in tokens

### Live Streaming
- RTMPS/SRT ingest from OBS, FFmpeg
- Automatic recording to on-demand
- Simulcast to YouTube, Twitch, etc.
- WebRTC support for browser streaming

## Quick Start

**Upload video via API**
```bash
curl -X POST \
  "https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/copy" \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/video.mp4"}'
```

**Embed player**
```html
<iframe
  src="https://customer-<CODE>.cloudflarestream.com/<VIDEO_ID>/iframe"
  style="border: none;"
  height="720" width="1280"
  allow="accelerometer; gyroscope; autoplay; encrypted-media; picture-in-picture;"
  allowfullscreen="true"
></iframe>
```

**Create live input**
```bash
curl -X POST \
  "https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/live_inputs" \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"recording": {"mode": "automatic"}}'
```

## Limits

- Max file size: 30 GB
- Max frame rate: 60 fps (recommended)
- Supported formats: MP4, MKV, MOV, AVI, FLV, MPEG-2 TS/PS, MXF, LXF, GXF, 3GP, WebM, MPG, QuickTime

## Pricing

- $5/1000 min stored
- $1/1000 min delivered

## Resources

- Dashboard: https://dash.cloudflare.com/?to=/:account/stream
- API Docs: https://developers.cloudflare.com/api/resources/stream/
- Stream Docs: https://developers.cloudflare.com/stream/

## Reading Order

| Order | File | Purpose | When to Use |
|-------|------|---------|-------------|
| 1 | [configuration.md](./configuration.md) | Setup SDKs, env vars, signing keys | Starting new project |
| 2 | [api.md](./api.md) | On-demand video APIs | Implementing uploads/playback |
| 3 | [api-live.md](./api-live.md) | Live streaming APIs | Building live streaming |
| 4 | [patterns.md](./patterns.md) | Full-stack flows, TUS, JWT signing | Implementing workflows |
| 5 | [gotchas.md](./gotchas.md) | Errors, limits, troubleshooting | Debugging issues |

## In This Reference

- [configuration.md](./configuration.md) - Setup, environment variables, wrangler config
- [api.md](./api.md) - On-demand video upload, playback, management APIs
- [api-live.md](./api-live.md) - Live streaming (RTMPS/SRT/WebRTC), simulcast
- [patterns.md](./patterns.md) - Full-stack flows, state management, best practices
- [gotchas.md](./gotchas.md) - Error codes, troubleshooting, limits

## See Also

- [workers](../workers/) - Deploy Stream APIs in Workers
- [pages](../pages/) - Integrate Stream with Pages
- [workers-ai](../workers-ai/) - AI-generate captions

```

### File: skills\cloudflare\references\workflows\README.md
```md
# Cloudflare Workflows

Durable multi-step applications with automatic retries, state persistence, and long-running execution.

## What It Does

- Chain steps with automatic retry logic
- Persist state between steps (minutes → weeks)
- Handle failures without losing progress
- Wait for external events/approvals
- Sleep without consuming resources

**Available:** Free & Paid Workers plans

## Core Concepts

**Workflow**: Class extending `WorkflowEntrypoint` with `run` method
**Instance**: Single execution with unique ID & independent state
**Steps**: Independently retriable units via `step.do()` - API calls, DB queries, AI invocations
**State**: Persisted from step returns; step name = cache key

## Quick Start

```typescript
import { WorkflowEntrypoint, WorkflowStep, WorkflowEvent } from 'cloudflare:workers';

type Env = { MY_WORKFLOW: Workflow; DB: D1Database };
type Params = { userId: string };

export class MyWorkflow extends WorkflowEntrypoint<Env, Params> {
  async run(event: WorkflowEvent<Params>, step: WorkflowStep) {
    const user = await step.do('fetch user', async () => {
      return await this.env.DB.prepare('SELECT * FROM users WHERE id = ?')
        .bind(event.payload.userId).first();
    });
    
    await step.sleep('wait 7 days', '7 days');
    
    await step.do('send reminder', async () => {
      await sendEmail(user.email, 'Reminder!');
    });
  }
}
```

## Key Features

- **Durability**: Failed steps don't re-run successful ones
- **Retries**: Configurable backoff (constant/linear/exponential)
- **Events**: `waitForEvent()` for webhooks/approvals (timeout: 1h → 365d)
- **Sleep**: `sleep()` / `sleepUntil()` for scheduling (max 365d)
- **Parallel**: `Promise.all()` for concurrent steps
- **Idempotency**: Check-then-execute patterns

## Reading Order

**Getting Started:** configuration.md → api.md → patterns.md  
**Troubleshooting:** gotchas.md

## In This Reference
- [configuration.md](./configuration.md) - wrangler.jsonc setup, step config, bindings
- [api.md](./api.md) - Step APIs, instance management, sleep/parameters
- [patterns.md](./patterns.md) - Common workflows, testing, orchestration
- [gotchas.md](./gotchas.md) - Timeouts, limits, debugging strategies

## See Also
- [durable-objects](../durable-objects/) - Alternative stateful approach
- [queues](../queues/) - Message-driven workflows
- [workers](../workers/) - Entry point for workflow instances

```

### File: .mcp.json
```json
{
  "mcpServers": {
    "cloudflare-api": {
      "type": "http",
      "url": "https://mcp.cloudflare.com/mcp"
    },
    "cloudflare-docs": {
      "type": "http",
      "url": "https://docs.mcp.cloudflare.com/mcp"
    },
    "cloudflare-bindings": {
      "type": "http",
      "url": "https://bindings.mcp.cloudflare.com/mcp"
    },
    "cloudflare-builds": {
      "type": "http",
      "url": "https://builds.mcp.cloudflare.com/mcp"
    },
    "cloudflare-observability": {
      "type": "http",
      "url": "https://observability.mcp.cloudflare.com/mcp"
    }
  }
}

```

### File: AGENTS.md
```md
# Skills Generator

Generate [Agent Skills](https://agentskills.io/home) from project documentation.

PLEASE STRICTLY FOLLOW THE BEST PRACTICES FOR SKILL: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices

- Focus on agents capabilities and practical usage patterns.
- Ignore user-facing guides, introductions, get-started, install guides, etc.
- Ignore content that LLM agents already confident about in their training data.
- Make the skill as concise as possible, avoid creating too many references.

## Skill Source Types

There are two types of skill sources. The project lists are defined in `meta.ts`:

### Type 1: Generated Skills (`sources/`)

For OSS projects **without existing skills**. We clone the repo as a submodule and generate skills from their documentation.

- **Projects:** Vue, Nuxt, Vite, UnoCSS
- **Workflow:** Read docs → Understand → Generate skills
- **Source:** `sources/{project}/docs/`

### Type 2: Synced Skills (`vendor/`)

For projects that **already maintain their own skills**. We clone their repo as a submodule and sync specified skills to ours.

- **Projects:** Slidev, VueUse
- **Workflow:** Pull updates → Copy specified skills (with optional renaming)
- **Source:** `vendor/{project}/skills/{skill-name}/`
- **Config:** Each vendor specifies which skills to sync and their output names in `meta.ts`

### Type 3: Hand-written Skills

For skills that are written by Anthony Fu with his preferences, experience, tastes and best practices.

You don't need to do anything about them unless being asked.

## Repository Structure

```
.
├── meta.ts                     # Project metadata (repos & URLs)
├── instructions/               # Instructions for generating skills
│   └── {project}.md            # Instructions for generating skills for {project}
│
├── sources/                    # Type 1: OSS repos (generate from docs)
│   └── {project}/
│       └── docs/               # Read documentation from here
│
├── vendor/                     # Type 2: Projects with existing skills (sync only)
│   └── {project}/
│       └── skills/
│           └── {skill-name}/   # Individual skills to sync
│
└── skills/                     # Output directory (generated or synced)
    └── {output-name}/
        ├── SKILL.md           # Index of all skills
        ├── GENERATION.md       # Tracking metadata (for generated skills)
        ├── SYNC.md             # Tracking metadata (for synced skills)
        └── references/
            └── *.md            # Individual skill files
```

**Important:** For Type 1 (generated), the `skills/{project}/` name must match `sources/{project}/`. For Type 2 (synced), the output name is configured in `meta.ts` and may differ from the source skill name.

## Workflows

### For Generated Skills (Type 1)

#### Adding a New Project

1. **Add entry to `meta.ts`** in the `submodules` object:
   ```ts
   export const submodules = {
     // ... existing entries
     'new-project': 'https://github.com/org/repo',
   }
   ```

2. **Run sync script** to clone the submodule:
   ```bash
   nr start init -y
   ```
   This will clone the repository to `sources/{project}/`

3. **Follow the generation guide** below to create the skills

#### General Instructions for Generation

- Focus on agents capabilities and practical usage patterns. For user-facing guides, introductions, get-started, or common knowledge that LLM agents already know, you can skip those content.
- Categorize each references into `core`, `features`, `best-practices`, `advanced`, etc categories, and prefix the reference file name with the category. For each feature field, feel free to create more categories if needed to better organize the content.

#### Creating New Skills

- **Read** source docs from `sources/{project}/docs/`
- **Read** the instructions in `instructions/{project}.md` for specific generation instructions if exists
- **Understand** the documentation thoroughly
- **Create** skill files in `skills/{project}/references/`
- **Create** `SKILL.md` index listing all skills
- **Create** `GENERATION.md` with the source git SHA

#### Updating Generated Skills

1. **Check** git diff since the SHA recorded in `GENERATION.md`:
   ```bash
   cd sources/{project}
   git diff {old-sha}..HEAD -- docs/
   ```
2. **Update** affected skill files based on changes
3. **Update** `SKILL.md` with the new version of the tool/project and skills table.
4. **Update** `GENERATION.md` with new SHA

### For Synced Skills (Type 2)

#### Initial Sync

1. **Copy** specified skills from `vendor/{project}/skills/{skill-name}/` to `skills/{output-name}/`
2. **Create** `SYNC.md` with the vendor git SHA

#### Updating Synced Skills

1. **Check** git diff since the SHA recorded in `SYNC.md`:
   ```bash
   cd vendor/{project}
   git diff {old-sha}..HEAD -- skills/{skill-name}/
   ```
2. **Copy** changed files from `vendor/{project}/skills/{skill-name}/` to `skills/{output-name}/`
3. **Update** `SYNC.md` with new SHA

**Note:** Do NOT modify synced skills manually. Changes should be contributed upstream to the vendor project.

## File Formats

### `SKILL.md`

Index file listing all skills with brief descriptions. Name should be in `kebab-case`.

The version should be the date of the last sync.

Also record the version of the tool/project when the skills were generated.

```markdown
---
name: {name}
description: {description}
metadata:
  author: Anthony Fu
  version: "2026.1.1"
  source: Generated from {source-url}, scripts located at https://github.com/antfu/skills
---

> The skill is based on {project} v{version}, generated at {date}.

// Some concise summary/context/introduction of the project

## Core References

| Topic | Description | Reference |
|-------|-------------|-----------|
| Markdown Syntax | Slide separators, frontmatter, notes, code blocks | [core-syntax](references/core-syntax.md) |
| Animations | v-click, v-clicks, motion, transitions | [core-animations](references/core-animations.md) |
| Headmatter | Deck-wide configuration options | [core-headmatter](references/core-headmatter.md) |

## Features

### Feature a

| Topic | Description | Reference |
|-------|-------------|-----------|
| Feature A Editor | Description of feature a | [feature-a](references/feature-a-foo.md) |
| Feature A Preview | Description of feature b | [feature-b](references/feature-a-bar.md) |

### Feature b

| Topic | Description | Reference |
|-------|-------------|-----------|
| Feature B | Description of feature b | [feature-b](references/feature-b-bar.md) |

// ...
```

### `GENERATION.md`

Tracking metadata for generated skills (Type 1):

```markdown
# Generation Info

- **Source:** `sources/{project}`
- **Git SHA:** `abc123def456...`
- **Generated:** 2024-01-15
```

### `SYNC.md`

Tracking metadata for synced skills (Type 2):

```markdown
# Sync Info

- **Source:** `vendor/{project}/skills/{skill-name}`
- **Git SHA:** `abc123def456...`
- **Synced:** 2024-01-15
```

### `references/*.md`

Individual skill files. One concept per file.

At the end of the file, include the reference links to the source documentation.

```markdown
---
name: {name}
description: {description}
---

# {Concept Name}

Brief description of what this skill covers.

## Usage

Code examples and practical patterns.

## Key Points

- Important detail 1
- Important detail 2

<!--
Source references:
- {source-url}
- {source-url}
- {source-url}
-->
```

## Writing Guidelines

When generating skills (Type 1 only):

1. **Rewrite for agents** - Don't copy docs verbatim; synthesize for LLM consumption
2. **Be practical** - Focus on usage patterns and code examples
3. **Be concise** - Remove fluff, keep essential information
4. **One concept per file** - Split large topics into separate skill files
5. **Include code** - Always provide working code examples
6. **Explain why** - Not just how to use, but when and why

## Supported Projects

See `meta.ts` for the canonical list of projects and their repository URLs.

```

### File: CLAUDE.md
```md
# Expo Skills Repository

This repository contains Claude Code plugins for building Expo apps. It serves as a marketplace for distributing skills to the Expo community.

## Repository Structure

```
.claude-plugin/
  marketplace.json          # Marketplace catalog - lists all plugins
plugins/
  expo-app-design/          # Plugin for building Expo apps
    .claude-plugin/
      plugin.json           # Plugin manifest
    skills/
      building-ui/
        SKILL.md            # Main skill file
        references/         # Supporting documentation
      deployment/
        SKILL.md
        reference/
      ...
    README.md
  upgrading-expo/           # Plugin for SDK upgrades
  expo-cicd-workflows/      # Plugin for EAS workflows
README.md                   # User-facing installation instructions
```

## Creating Claude Code Plugins

### Plugin Directory Structure

Each plugin follows this structure:

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json         # Required: Plugin manifest (only file in this dir)
├── skills/                 # Skill directories
│   └── skill-name/
│       ├── SKILL.md        # Required: Main skill file
│       ├── references/     # Optional: Supporting docs
│       └── scripts/        # Optional: Utility scripts
└── README.md               # Optional: Plugin documentation
```

### Plugin Manifest (`plugin.json`)

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "Brief description of the plugin",
  "author": {
    "name": "Your Name",
    "email": "you@example.com"
  }
}
```

Required fields:
- `name`: Unique identifier in kebab-case

Optional fields:
- `version`: Semantic versioning (e.g., `"1.0.0"`)
- `description`: Brief explanation shown in plugin manager
- `author`: Object with `name` and optionally `email`

### Skill Files (`SKILL.md`)

Skills teach Claude how to perform specific tasks. Each skill has a `SKILL.md` file with YAML frontmatter:

```markdown
---
name: skill-name
description: What the skill does and when to use it. Claude uses this for auto-discovery.
---

# Skill Title

Skill content goes here...
```

**Frontmatter fields:**

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Skill identifier (lowercase, hyphens, max 64 chars) |
| `description` | Yes | When to use this skill (max 1024 chars) - crucial for auto-discovery |
| `allowed-tools` | No | Tools Claude can use without permission (e.g., `"Read, Grep, Bash(node:*)"`) |
| `version` | No | Skill version |
| `license` | No | License identifier |

**Best practices:**
- Keep `SKILL.md` under 500 lines
- Use `references/` subdirectory for detailed documentation
- Write descriptions that match what users naturally say
- Include keywords users would search for

### Supporting Files

Skills can include supporting files:

```
skills/my-skill/
├── SKILL.md                 # Main skill (required)
├── references/              # Detailed documentation
│   ├── setup.md
│   └── examples.md
└── scripts/                 # Utility scripts
    ├── fetch.js
    └── validate.js
```

Reference these in your SKILL.md:
```markdown
## References

Consult these resources as needed:
- ./references/setup.md -- Setup and configuration guide
- ./references/examples.md -- Usage examples
```

## Marketplace Configuration

The `.claude-plugin/marketplace.json` file catalogs all plugins:

```json
{
  "name": "marketplace-name",
  "owner": {
    "name": "Owner Name",
    "email": "owner@example.com"
  },
  "metadata": {
    "description": "Marketplace description"
  },
  "plugins": [
    {
      "name": "plugin-name",
      "source": "./plugins/plugin-name",
      "description": "What the plugin does."
    }
  ]
}
```

**Plugin entry fields:**
- `name` (required): Plugin identifier in kebab-case
- `source` (required): Relative path to plugin directory
- `description`: Brief description for the plugin list

## Adding a New Plugin

1. Create the plugin directory structure:
   ```bash
   mkdir -p plugins/my-plugin/.claude-plugin
   mkdir -p plugins/my-plugin/skills/my-skill
   ```

2. Create `plugins/my-plugin/.claude-plugin/plugin.json`:
   ```json
   {
     "name": "my-plugin",
     "version": "1.0.0",
     "description": "What the plugin does",
     "author": {
       "name": "Your Name",
       "email": "you@example.com"
     }
   }
   ```

3. Create `plugins/my-plugin/skills/my-skill/SKILL.md`:
   ```markdown
   ---
   name: my-skill
   description: When to use this skill and what it does.
   ---

   # My Skill

   Content...
   ```

4. Create `plugins/my-plugin/README.md`:
   ```markdown
   # My Plugin

   Brief description.

   ## License

   MIT
   ```

5. Add to `.claude-plugin/marketplace.json`:
   ```json
   {
     "name": "my-plugin",
     "source": "./plugins/my-plugin",
     "description": "What the plugin does."
   }
   ```

6. Add to `README.md` installation examples:
   ```
   /plugin install my-plugin
   ```

## Testing Plugins

Test plugins locally before publishing:

```bash
# Load plugin for testing
claude --plugin-dir ./plugins/my-plugin

# Validate plugin structure
claude plugin validate ./plugins/my-plugin
```

## User Installation

Users install plugins from this marketplace:

```bash
# Add the marketplace
/plugin marketplace add expo/skills

# Install a plugin
/plugin install expo-app-design
/plugin install upgrading-expo
/plugin install expo-cicd-workflows
```

## Conventions in This Repo

- **Plugin names**: Use kebab-case (e.g., `expo-app-design`)
- **Skill names**: Use kebab-case (e.g., `building-ui`, `cicd-workflows`)
- **File names**: Use kebab-case for all files
- **Author emails**: Use `@expo.io` or `@expo.dev` domain
- **License**: MIT for all plugins
- **README.md**: Include in each plugin with brief description and license

```

### File: CONTRIBUTING.md
```md
# Contributing to Composio Skills

Thanks for contributing! This is kept intentionally simple.

## Adding a Rule

1. Create a new `.md` file in `skills/composio/rules/`
2. Follow the naming: `{prefix}-{descriptive-name}.md`
3. Use the structure below

## Rule Template

```markdown
---
title: Clear, Action-Oriented Title
impact: CRITICAL | HIGH | MEDIUM | LOW
description: One sentence describing the impact
tags: [relevant, tags]
---

# Rule Title

1-2 sentences explaining why this matters.

## ❌ Incorrect

\`\`\`typescript
// Show the wrong way with explanatory comments
const bad = 'example';
\`\`\`

\`\`\`python
# Show the wrong way with explanatory comments
bad = "example"
\`\`\`

## ✅ Correct

\`\`\`typescript
// Show the right way with explanatory comments
const good = 'example';
\`\`\`

\`\`\`python
# Show the right way with explanatory comments
good = "example"
\`\`\`

## Reference

- [Relevant docs](https://docs.composio.dev)
```

## Guidelines

- **One rule per file**: Keep it focused
- **Real examples**: Use actual code, not pseudocode
- **Both languages**: Include TypeScript and Python examples
- **Explain why**: Use comments to explain reasoning
- **Be actionable**: Developers should know exactly what to do

## Impact Levels

- **CRITICAL**: Security, data loss, breaking bugs
- **HIGH**: Major performance or UX issues
- **MEDIUM**: Maintainability, code quality
- **LOW**: Style, minor optimizations

## Prefixes

- `auth-` - Authentication & Security
- `exec-` - Tool Execution
- `conn-` - Connected Accounts
- `custom-` - Custom Tools
- `provider-` - Provider Integration
- `error-` - Error Handling
- `perf-` - Performance
- `dev-` - Development

That's it! Keep it simple.

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
