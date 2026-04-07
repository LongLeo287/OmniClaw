---
id: goclaw
type: knowledge
owner: OA_Triage
---
# goclaw
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<p align="center">
  <img src="_statics/goclaw-logo.svg" alt="GoClaw" height="200" />
</p>

<p align="center"><strong>Multi-Tenant AI Agent Platform</strong></p>

<p align="center">
Multi-agent AI gateway built in Go. 20+ LLM providers. 7 channels. Multi-tenant PostgreSQL.<br/>
Single binary. Production-tested. Agents that orchestrate for you.
</p>

<p align="center">
  <a href="https://docs.goclaw.sh">Documentation</a> •
  <a href="https://docs.goclaw.sh/#quick-start">Quick Start</a> •
  <a href="https://x.com/nlb_io">Twitter / X</a>
</p>

<p align="center">
  <a href="https://go.dev/"><img src="https://img.shields.io/badge/Go_1.26-00ADD8?style=flat-square&logo=go&logoColor=white" alt="Go" /></a>
  <a href="https://www.postgresql.org/"><img src="https://img.shields.io/badge/PostgreSQL_18-316192?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" /></a>
  <a href="https://www.docker.com/"><img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" /></a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/API/WebSocket"><img src="https://img.shields.io/badge/WebSocket-010101?style=flat-square&logo=socket.io&logoColor=white" alt="WebSocket" /></a>
  <a href="https://opentelemetry.io/"><img src="https://img.shields.io/badge/OpenTelemetry-000000?style=flat-square&logo=opentelemetry&logoColor=white" alt="OpenTelemetry" /></a>
  <a href="https://www.anthropic.com/"><img src="https://img.shields.io/badge/Anthropic-191919?style=flat-square&logo=anthropic&logoColor=white" alt="Anthropic" /></a>
  <a href="https://openai.com/"><img src="https://img.shields.io/badge/OpenAI_Compatible-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI" /></a>
  <img src="https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey?style=flat-square" alt="License: CC BY-NC 4.0" />
</p>

A Go port of [OpenClaw](https://github.com/openclaw/openclaw) with enhanced security, multi-tenant PostgreSQL, and production-grade observability.

🌐 **Languages:**
[🇨🇳 简体中文](_readmes/README.zh-CN.md) ·
[🇯🇵 日本語](_readmes/README.ja.md) ·
[🇰🇷 한국어](_readmes/README.ko.md) ·
[🇻🇳 Tiếng Việt](_readmes/README.vi.md) ·
[🇵🇭 Tagalog](_readmes/README.tl.md) ·
[🇪🇸 Español](_readmes/README.es.md) ·
[🇧🇷 Português](_readmes/README.pt.md) ·
[🇮🇹 Italiano](_readmes/README.it.md) ·
[🇩🇪 Deutsch](_readmes/README.de.md) ·
[🇫🇷 Français](_readmes/README.fr.md) ·
[🇸🇦 العربية](_readmes/README.ar.md) ·
[🇮🇳 हिन्दी](_readmes/README.hi.md) ·
[🇷🇺 Русский](_readmes/README.ru.md) ·
[🇧🇩 বাংলা](_readmes/README.bn.md) ·
[🇮🇱 עברית](_readmes/README.he.md) ·
[🇵🇱 Polski](_readmes/README.pl.md) ·
[🇨🇿 Čeština](_readmes/README.cs.md) ·
[🇳🇱 Nederlands](_readmes/README.nl.md) ·
[🇹🇷 Türkçe](_readmes/README.tr.md) ·
[🇺🇦 Українська](_readmes/README.uk.md) ·
[🇮🇩 Bahasa Indonesia](_readmes/README.id.md) ·
[🇹🇭 ไทย](_readmes/README.th.md) ·
[🇵🇰 اردو](_readmes/README.ur.md) ·
[🇷🇴 Română](_readmes/README.ro.md) ·
[🇸🇪 Svenska](_readmes/README.sv.md) ·
[🇬🇷 Ελληνικά](_readmes/README.el.md) ·
[🇭🇺 Magyar](_readmes/README.hu.md) ·
[🇫🇮 Suomi](_readmes/README.fi.md) ·
[🇩🇰 Dansk](_readmes/README.da.md) ·
[🇳🇴 Norsk](_readmes/README.nb.md)

## What Makes It Different

- **Agent Teams & Orchestration** — Teams with shared task boards, inter-agent delegation (sync/async), and hybrid agent discovery
- **Multi-Tenant PostgreSQL** — Per-user workspaces, per-user context files, encrypted API keys (AES-256-GCM), isolated sessions
- **Single Binary** — ~25 MB static Go binary, no Node.js runtime, <1s startup, runs on a $5 VPS
- **Production Security** — 5-layer permission system (gateway auth → global tool policy → per-agent → per-channel → owner-only) plus rate limiting, prompt injection detection, SSRF protection, shell deny patterns, and AES-256-GCM encryption
- **20+ LLM Providers** — Anthropic (native HTTP+SSE with prompt caching), OpenAI, OpenRouter, Groq, DeepSeek, Gemini, Mistral, xAI, MiniMax, Cohere, Perplexity, DashScope, Bailian, Zai, Ollama, Ollama Cloud, Claude CLI, Codex, ACP, and any OpenAI-compatible endpoint
- **7 Messaging Channels** — Telegram, Discord, Slack, Zalo OA, Zalo Personal, Feishu/Lark, WhatsApp
- **Extended Thinking** — Per-provider thinking mode (Anthropic budget tokens, OpenAI reasoning effort, DashScope thinking budget) with streaming support
- **Heartbeat System** — Periodic agent check-ins via HEARTBEAT.md checklists with suppress-on-OK, active hours, retry logic, and channel delivery
- **Scheduling & Cron** — `at`, `every`, and cron expressions for automated agent tasks with lane-based concurrency
- **Observability** — Built-in LLM call tracing with spans and prompt cache metrics, optional OpenTelemetry OTLP export

## Claw Ecosystem

|                 | OpenClaw        | ZeroClaw | PicoClaw | **GoClaw**                              |
| --------------- | --------------- | -------- | -------- | --------------------------------------- |
| Language        | TypeScript      | Rust     | Go       | **Go**                                  |
| Binary size     | 28 MB + Node.js | 3.4 MB   | ~8 MB    | **~25 MB** (base) / **~36 MB** (+ OTel) |
| Docker image    | —               | —        | —        | **~50 MB** (Alpine)                     |
| RAM (idle)      | > 1 GB          | < 5 MB   | < 10 MB  | **~35 MB**                              |
| Startup         | > 5 s           | < 10 ms  | < 1 s    | **< 1 s**                               |
| Target hardware | $599+ Mac Mini  | $10 edge | $10 edge | **$5 VPS+**                             |

| Feature                    | OpenClaw                             | ZeroClaw                                     | PicoClaw                              | **GoClaw**                     |
| -------------------------- | ------------------------------------ | -------------------------------------------- | ------------------------------------- | ------------------------------ |
| Multi-tenant (PostgreSQL)  | —                                    | —                                            | —                                     | ✅                             |
| MCP integration            | — (uses ACP)                         | —                                            | —                                     | ✅ (stdio/SSE/streamable-http) |
| Agent teams                | —                                    | —                                            | —                                     | ✅ Task board + mailbox        |
| Security hardening         | ✅ (SSRF, path traversal, injection) | ✅ (sandbox, rate limit, injection, pairing) | Basic (workspace restrict, exec deny) | ✅ 5-layer defense             |
| OTel observability         | ✅ (opt-in extension)                | ✅ (Prometheus + OTLP)                       | —                                     | ✅ OTLP (opt-in build tag)     |
| Prompt caching             | —                                    | —                                            | —                                     | ✅ Anthropic + OpenAI-compat   |
| Knowledge graph            | —                                    | —                                            | —                                     | ✅ LLM extraction + traversal  |
| Skill system               | ✅ Embeddings/semantic               | ✅ SKILL.md + TOML                           | ✅ Basic                              | ✅ BM25 + pgvector hybrid      |
| Lane-based scheduler       | ✅                                   | Bounded concurrency                          | —                                     | ✅ (main/subagent/team/cron)   |
| Messaging channels         | 37+                                  | 15+                                          | 10+                                   | 7+                             |
| Companion apps             | macOS, iOS, Android                  | Python SDK                                   | —                                     | Web dashboard                  |
| Live Canvas / Voice        | ✅ (A2UI + TTS/STT)                  | —                                            | Voice transcription                   | TTS (4 providers)              |
| LLM providers              | 10+                                  | 8 native + 29 compat                         | 13+                                   | **20+**                        |
| Per-user workspaces        | ✅ (file-based)                      | —                                            | —                                     | ✅ (PostgreSQL)                |
| Encrypted secrets          | — (env vars only)                    | ✅ ChaCha20-Poly1305                         | — (plaintext JSON)                    | ✅ AES-256-GCM in DB           |

## Architecture

<p align="center">
  <img src="_statics/architecture.jpg" alt="GoClaw Architecture" width="800" />
</p>

<p align="center">
  <img src="_statics/goclaw_multi_tenant.png" alt="GoClaw Multi-Tenant" width="800" />
</p>

## Quick Start

**Prerequisites:** Go 1.26+, PostgreSQL 18 with pgvector, Docker (optional)

### From Source

```bash
git clone https://github.com/nextlevelbuilder/goclaw.git && cd goclaw
make build
./goclaw onboard        # Interactive setup wizard
source .env.local && ./goclaw
```

### With Docker

```bash
# Generate .env with auto-generated secrets
chmod +x prepare-env.sh && ./prepare-env.sh

# Add at least one GOCLAW_*_API_KEY to .env, then:
make up

# Web Dashboard at http://localhost:3000
# Health check: curl http://localhost:18790/health
```

`make up` creates a Docker network, embeds the correct version from git tags, builds and starts all services, and runs database migrations automatically.

**Common commands:**

```bash
make up                # Start all services (build + migrate)
make down              # Stop all services
make logs              # Tail logs (goclaw service)
make reset             # Wipe volumes and rebuild from scratch
```

**Optional services** — enable with `WITH_*` flags:

| Flag | Service | What it does |
|------|---------|-------------|
| `WITH_BROWSER=1` | Headless Chrome | Enables `browser` tool for web scraping, screenshots, automation |
| `WITH_OTEL=1` | Jaeger | OpenTelemetry tracing UI for debugging LLM calls and latency |
| `WITH_SANDBOX=1` | Docker sandbox | Isolated container for running untrusted code from agents |
| `WITH_TAILSCALE=1` | Tailscale | Expose gateway over Tailscale private network |
| `WITH_REDIS=1` | Redis | Redis-backed caching layer |

Flags can be combined and work with all commands:

```bash
# Start with browser automation and tracing
make up WITH_BROWSER=1 WITH_OTEL=1

# Stop everything including optional services
make down WITH_BROWSER=1 WITH_OTEL=1
```

When `GOCLAW_*_API_KEY` environment variables are set, the gateway auto-onboards without interactive prompts — detects provider, runs migrations, and seeds default data.

> For detailed configuration and Docker image tags, see the [Deployment Guide](https://docs.goclaw.sh/#deploy-docker-compose).

## Multi-Agent Orchestration

GoClaw supports agent teams and inter-agent delegation — each agent runs with its own identity, tools, LLM provider, and context files.

### Agent Delegation

<p align="center">
  <img src="_statics/agent-delegation.jpg" alt="Agent Delegation" width="700" />
</p>

| Mode | How it works | Best for |
|------|-------------|----------|
| **Sync** | Agent A asks Agent B and **waits** for the answer | Quick lookups, fact checks |
| **Async** | Agent A asks Agent B and **moves on**. B announces later | Long tasks, reports, deep analysis |

Agents communicate through explicit **permission links** with direction control (`outbound`, `inbound`, `bidirectional`) and concurrency limits at both per-link and per-agent levels.

### Agent Teams

<p align="center">
  <img src="_statics/agent-teams.jpg" alt="Agent Teams Workflow" width="800" />
</p>

- **Shared task board** — Create, claim, complete, search tasks with `blocked_by` dependencies
- **Team mailbox** — Direct peer-to-peer messaging and broadcasts
- **Tools**: `team_tasks` for task management, `team_message` for mailbox

> For delegation details, permission links, and concurrency control, see the [Agent Teams docs](https://docs.goclaw.sh/#teams-what-are-teams).

## Built-in Tools

| Tool               | Group         | Description                                                  |
| ------------------ | ------------- | ------------------------------------------------------------ |
| `read_file`        | fs            | Read file contents (with virtual FS routing)                 |
| `write_file`       | fs            | Write/create files                                           |
| `edit_file`        | fs            | Apply targeted edits to existing files                       |
| `list_files`       | fs            | List directory contents                                      |
| `search`           | fs            | Search file contents by pattern                              |
| `glob`             | fs            | Find files by glob pattern                                   |
| `exec`             | runtime       | Execute shell commands (with approval workflow)              |
| `web_search`       | web           | Search the web (Brave, DuckDuckGo)                           |
| `web_fetch`        | web           | Fetch and parse web content                                  |
| `memory_search`    | memory        | Search long-term memory (FTS + vector)                       |
| `memory_get`       | memory        | Retrieve memory entries                                      |
| `skill_search`     | —             | Search skills (BM25 + embedding hybrid)                      |
| `knowledge_graph_search` | memory  | Search entities and traverse knowledge graph relationships   |
| `create_image`     | media         | Image generation (DashScope, MiniMax)                        |
| `create_audio`     | media         | Audio generation (OpenAI, ElevenLabs, MiniMax, Suno)         |
| `create_video`     | media         | Video generation (MiniMax, Veo)                              |
| `read_document`    | media         | Document reading (Gemini File API, provider chain)           |
| `read_image`       | media         | Image analysis                                               |
| `read_audio`       | media         | Audio transcription and analysis                             |
| `read_video`       | media         | Video analysis                                               |
| `message`          | messaging     | Send messages to channels                                    |
| `tts`              | —             | Text-to-Speech synthesis                                     |
| `spawn`            | —             | Spawn a subagent                                             |
| `subagents`        | sessions      | Control running subagents                                    |
| `team_tasks`       | teams         
... [TRUNCATED]
```

### File: ui\web\package.json
```json
{
  "name": "goclaw-web",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "preview": "vite preview",
    "lint": "eslint ."
  },
  "dependencies": {
    "@dnd-kit/core": "^6.3.1",
    "@dnd-kit/sortable": "^10.0.0",
    "@dnd-kit/utilities": "^3.2.2",
    "@tailwindcss/typography": "^0.5.19",
    "@tanstack/react-query": "^5.90.21",
    "@tanstack/react-table": "^8.21.3",
    "@xyflow/react": "^12.10.1",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "d3-force": "^3.0.0",
    "date-fns": "^4.1.0",
    "framer-motion": "^12.34.3",
    "highlight.js": "^11.11.1",
    "i18next": "^25.8.15",
    "jszip": "^3.10.1",
    "lucide-react": "^0.468.0",
    "radix-ui": "^1.4.3",
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "react-i18next": "^16.5.6",
    "react-markdown": "^10.1.0",
    "react-router": "^7.1.0",
    "recharts": "^3.8.0",
    "rehype-highlight": "^7.0.2",
    "remark-gfm": "^4.0.1",
    "tailwind-merge": "^2.6.0",
    "zustand": "^5.0.0"
  },
  "devDependencies": {
    "@tailwindcss/vite": "^4.0.0",
    "@types/d3-force": "^3.0.10",
    "@types/react": "^19.0.0",
    "@types/react-dom": "^19.0.0",
    "@types/ws": "^8.18.1",
    "@vitejs/plugin-react": "^4.3.4",
    "tailwindcss": "^4.0.0",
    "typescript": "~5.7.0",
    "vite": "^6.0.0",
    "ws": "^8.19.0"
  },
  "packageManager": "pnpm@10.30.1+sha512.3590e550d5384caa39bd5c7c739f72270234b2f6059e13018f975c313b1eb9fefcc09714048765d4d9efe961382c312e624572c0420762bdc5d5940cdf9be73a"
}

```

### File: api_reference.md
```md
# API Reference

## HTTP Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Health check |
| GET | `/ws` | WebSocket upgrade |
| POST | `/v1/chat/completions` | OpenAI-compatible chat API |
| POST | `/v1/responses` | Responses protocol |
| POST | `/v1/tools/invoke` | Tool invocation |
| GET/POST | `/v1/agents/*` | Agent management |
| GET/POST | `/v1/skills/*` | Skills management |
| GET/POST/PUT/DELETE | `/v1/tools/custom/*` | Custom tool CRUD |
| GET/POST/PUT/DELETE | `/v1/mcp/*` | MCP server + grants management |
| GET | `/v1/traces/*` | Trace viewer |

## Custom Tools

Define shell-based tools at runtime via HTTP API — no recompile or restart needed. The LLM can invoke custom tools identically to built-in tools.

**How it works:**
1. Admin creates a tool via `POST /v1/tools/custom` with a shell command template
2. LLM generates a tool call with the custom tool name
3. GoClaw renders the command template with shell-escaped arguments, checks deny patterns, and executes with timeout

**Capabilities:**
- **Scope** — Global (all agents) or per-agent (`agent_id` field)
- **Parameters** — JSON Schema definition for LLM arguments
- **Security** — All arguments auto shell-escaped, deny pattern filtering (blocks `curl|sh`, reverse shells, etc.), configurable timeout (default 60s)
- **Encrypted env vars** — Environment variables stored with AES-256-GCM encryption in the database
- **Cache invalidation** — Mutations broadcast events for hot-reload without restart

**API:**

| Method | Path | Description |
|---|---|---|
| GET | `/v1/tools/custom` | List tools (filter by `?agent_id=`) |
| POST | `/v1/tools/custom` | Create a custom tool |
| GET | `/v1/tools/custom/{id}` | Get tool details |
| PUT | `/v1/tools/custom/{id}` | Update a tool (JSON patch) |
| DELETE | `/v1/tools/custom/{id}` | Delete a tool |

**Example — create a tool that checks DNS records:**

```json
{
  "name": "dns_lookup",
  "description": "Look up DNS records for a domain",
  "parameters": {
    "type": "object",
    "properties": {
      "domain": { "type": "string", "description": "Domain name to look up" },
      "record_type": { "type": "string", "enum": ["A", "AAAA", "MX", "CNAME", "TXT"] }
    },
    "required": ["domain"]
  },
  "command": "dig +short {{.record_type}} {{.domain}}",
  "timeout_seconds": 10,
  "enabled": true
}
```

## MCP Integration

Connect external [Model Context Protocol](https://modelcontextprotocol.io) servers to extend agent capabilities. MCP tools are registered transparently into GoClaw's tool registry and invoked like any built-in tool.

**Supported transports:** `stdio`, `sse`, `streamable-http`

**Static config** — configure in `config.json` (deprecated; use HTTP API for dynamic management):

```json
{
  "mcp": {
    "servers": {
      "filesystem": {
        "transport": "stdio",
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", "/workspace"]
      },
      "remote-tools": {
        "transport": "streamable-http",
        "url": "https://mcp.example.com/tools"
      }
    }
  }
}
```

**HTTP API** — full CRUD with per-agent and per-user access grants:

| Method | Path | Description |
|---|---|---|
| GET | `/v1/mcp/servers` | List registered MCP servers |
| POST | `/v1/mcp/servers` | Register a new MCP server |
| GET | `/v1/mcp/servers/{id}` | Get server details |
| PUT | `/v1/mcp/servers/{id}` | Update server config |
| DELETE | `/v1/mcp/servers/{id}` | Remove MCP server |
| POST | `/v1/mcp/servers/{id}/grants/agent` | Grant access to an agent |
| DELETE | `/v1/mcp/servers/{id}/grants/agent/{agentID}` | Revoke agent access |
| GET | `/v1/mcp/grants/agent/{agentID}` | List agent's MCP grants |
| POST | `/v1/mcp/servers/{id}/grants/user` | Grant access to a user |
| DELETE | `/v1/mcp/servers/{id}/grants/user/{userID}` | Revoke user access |
| POST | `/v1/mcp/requests` | Request access (user self-service) |
| GET | `/v1/mcp/requests` | List pending access requests |
| POST | `/v1/mcp/requests/{id}/review` | Approve or reject a request |

**Features:**
- **Multi-server** — Connect multiple MCP servers simultaneously
- **Tool name prefixing** — Optional `{prefix}__{toolName}` to avoid collisions
- **Per-agent grants** — Control which agents can access which MCP servers, with tool allow/deny lists
- **Per-user grants** — Fine-grained user-level access control
- **Access requests** — Users can request access; admins approve or reject

```

### File: CHANGELOG.md
```md
# Changelog

All notable changes to GoClaw are documented here. For full documentation, see [docs.goclaw.sh](https://docs.goclaw.sh).

## Project Status

### Implemented & Tested in Production

- **Agent management & configuration** — Create, update, delete agents via API and web dashboard. Agent types (`open` / `predefined`), agent routing, and lazy resolution all tested.
- **Telegram channel** — Full integration tested: message handling, streaming responses, rich formatting (HTML, tables, code blocks), reactions, media, chunked long messages.
- **Seed data & bootstrapping** — Auto-onboard, DB seeding, migration pipeline tested end-to-end.
- **User-scope & content files** — Per-user context files (`user_context_files`), agent-level context files (`agent_context_files`), virtual FS interceptors, per-user seeding (`SeedUserFiles`), and user-agent profile tracking all implemented and tested.
- **Core built-in tools** — File system tools (`read_file`, `write_file`, `edit_file`, `list_files`, `search`, `glob`), shell execution (`exec`), web tools (`web_search`, `web_fetch`), and session management tools tested in real agent loops.
- **Memory system** — Long-term memory with pgvector hybrid search (FTS + vector) implemented and tested with real conversations.
- **Agent loop** — Think-act-observe cycle, tool use, session history, auto-summarization, and subagent spawning tested in production.
- **WebSocket RPC protocol (v3)** — Connect handshake, chat streaming, event push all tested with web dashboard and integration tests.
- **Store layer (PostgreSQL)** — All PG stores (sessions, agents, providers, skills, cron, pairing, tracing, memory, teams) implemented and running.
- **Browser automation** — Rod/CDP integration for headless Chrome, tested in production agent workflows.
- **Lane-based scheduler** — Main/subagent/team/cron lane isolation with concurrent execution tested. Group chats support up to 3 concurrent agent runs per session with adaptive throttle and deferred session writes for history isolation.
- **Security hardening** — Rate limiting, prompt injection detection, CORS, shell deny patterns, SSRF protection, credential scrubbing all implemented and verified.
- **Web dashboard** — Channel management, agent management, pairing approval, traces & spans viewer, skills, MCP, cron, sessions, teams, and config pages all implemented and working.
- **Prompt caching** — Anthropic (explicit `cache_control`), OpenAI/MiniMax/OpenRouter (automatic). Cache metrics tracked in trace spans and displayed in web dashboard.
- **Agent delegation** — Inter-agent task delegation with permission links, sync/async modes, per-user restrictions, concurrency limits, and hybrid agent search. Tested in production.
- **Agent teams** — Team creation with lead/member roles, shared task board (create, claim, complete, search, blocked_by dependencies), team mailbox (send, broadcast, read). Tested in production.
- **Evaluate loop** — Generator-evaluator feedback cycles with configurable max rounds and pass criteria. Tested in production.
- **Delegation history** — Queryable audit trail of inter-agent delegations. Tested in production.
- **Skill system** — BM25 search, ZIP upload, SKILL.md parsing, and embedding hybrid search. Tested in production.
- **MCP integration** — stdio, SSE, and streamable-http transports with per-agent/per-user grants. Tested in production.
- **Cron scheduling** — `at`, `every`, and cron expression scheduling. Tested in production.
- **Docker sandbox** — Isolated code execution in containers. Tested in production.
- **Text-to-Speech** — OpenAI, ElevenLabs, Edge, MiniMax providers. Tested in production.
- **HTTP API** — `/v1/chat/completions`, `/v1/agents`, `/v1/skills`, etc. Tested in production. Interactive Swagger UI at `/docs`.
- **API key management** — Multi-key auth with RBAC scopes, SHA-256 hashed storage, show-once pattern, optional expiry, revocation. HTTP + WebSocket CRUD. Web UI for management.
- **Hooks system** — Event-driven hooks with command evaluators (shell exit code) and agent evaluators (delegate to reviewer). Blocking gates with auto-retry and recursion-safe evaluation.
- **Media tools** — `create_image` (DashScope, MiniMax), `create_audio` (OpenAI, ElevenLabs, MiniMax, Suno), `create_video` (MiniMax, Veo), `read_document` (Gemini File API), `read_image`, `read_audio`, `read_video`. Persistent media storage with lazy-loaded MediaRef.
- **Additional provider modes** — Claude CLI (Anthropic via stdio + MCP bridge), Codex (OpenAI gpt-5.3-codex via OAuth).
- **Knowledge graph** — LLM-powered entity extraction, graph traversal, force-directed visualization, and `knowledge_graph_search` agent tool.
- **Memory management** — Admin dashboard for memory documents (CRUD, semantic search, chunk/embedding details, bulk re-indexing).
- **Persistent pending messages** — Channel messages persisted to PostgreSQL with auto-compaction (LLM summarization) and monitoring dashboard.
- **Heartbeat system** — Periodic agent check-ins via HEARTBEAT.md checklists with suppress-on-OK, active hours, retry logic, and channel delivery.

### Implemented but Not Fully Tested

- **Slack** — Channel integration implemented, not yet validated with real users.
- **Other messaging channels** — Discord, Zalo OA, Zalo Personal, Feishu/Lark, WhatsApp channel adapters are implemented but have not been tested end-to-end in production. Only Telegram has been validated with real users.
- **OpenTelemetry export** — OTLP gRPC/HTTP exporter implemented (build-tag gated). In-app tracing works; external OTel export not validated in production.
- **Tailscale integration** — tsnet listener implemented (build-tag gated). Not tested in a real deployment.
- **Redis cache** — Optional distributed cache backend (build-tag gated). Not tested in production.
- **Browser pairing** — Pairing code flow implemented with CLI and web UI approval. Basic flow tested but not validated at scale.

```

### File: CLAUDE.md
```md
# GoClaw Gateway

PostgreSQL multi-tenant AI agent gateway with WebSocket RPC + HTTP API.

## Tech Stack

**Backend:** Go 1.26, Cobra CLI, gorilla/websocket, pgx/v5 (database/sql, no ORM), golang-migrate, go-rod/rod, telego (Telegram)
**Web UI:** React 19, Vite 6, TypeScript, Tailwind CSS 4, Radix UI, Zustand, React Router 7. Located in `ui/web/`. **Use `pnpm` (not npm).**
**Database:** PostgreSQL 18 with pgvector. Raw SQL with `$1, $2` positional params. Nullable columns: `*string`, `*time.Time`, etc.

## Project Structure

```
cmd/                          CLI commands, gateway startup, onboard wizard, migrations
internal/
├── agent/                    Agent loop (think→act→observe), router, resolver, input guard
├── bootstrap/                System prompt files (SOUL.md, IDENTITY.md) + seeding + per-user seed
├── bus/                      Event bus system
├── cache/                    Caching layer
├── channels/                 Channel manager: Telegram, Feishu/Lark, Zalo, Discord, WhatsApp
├── config/                   Config loading (JSON5) + env var overlay
├── crypto/                   AES-256-GCM encryption for API keys
├── cron/                     Cron scheduling (at/every/cron expr)
├── gateway/                  WS + HTTP server, client, method router
│   └── methods/              RPC handlers (chat, agents, sessions, config, skills, cron, pairing)
├── hooks/                    Hook system for extensibility
├── http/                     HTTP API (/v1/chat/completions, /v1/agents, /v1/skills, etc.)
├── i18n/                     Message catalog: T(locale, key, args...) + per-locale catalogs (en/vi/zh)
├── knowledgegraph/           Knowledge graph storage and traversal
├── mcp/                      Model Context Protocol bridge/server
├── media/                    Media handling utilities
├── memory/                   Memory system (pgvector)
├── oauth/                    OAuth authentication
├── permissions/              RBAC (admin/operator/viewer)
├── providers/                LLM providers: Anthropic (native HTTP+SSE), OpenAI-compat (HTTP+SSE), DashScope (Alibaba Qwen), Claude CLI (stdio+MCP bridge), ACP (Anthropic Console Proxy), Codex (OpenAI)
├── sandbox/                  Docker-based code sandbox
├── scheduler/                Lane-based concurrency (main/subagent/cron)
├── sessions/                 Session management
├── skills/                   SKILL.md loader + BM25 search
├── store/                    Store interfaces + pg/ (PostgreSQL) implementations
├── tasks/                    Task management
├── tools/                    Tool registry, filesystem, exec, web, memory, subagent, MCP bridge
├── tracing/                  LLM call tracing + optional OTel export (build-tag gated)
├── tts/                      Text-to-Speech (OpenAI, ElevenLabs, Edge, MiniMax)
├── upgrade/                  Database schema version tracking
pkg/protocol/                 Wire types (frames, methods, errors, events)
pkg/browser/                  Browser automation (Rod + CDP)
migrations/                   PostgreSQL migration files
ui/web/                       React SPA (pnpm, Vite, Tailwind, Radix UI)
```

## Key Patterns

- **Store layer:** Interface-based (`store.SessionStore`, `store.AgentStore`, etc.) with pg/ (PostgreSQL) implementations. Uses `database/sql` + `pgx/v5/stdlib`, raw SQL, `execMapUpdate()` helper in `pg/helpers.go`
- **Agent types:** `open` (per-user context, 7 files) vs `predefined` (shared context + USER.md per-user)
- **Context files:** `agent_context_files` (agent-level) + `user_context_files` (per-user), routed via `ContextFileInterceptor`
- **Providers:** Anthropic (native HTTP+SSE), OpenAI-compat (HTTP+SSE), DashScope (Alibaba Qwen), Claude CLI (stdio+MCP bridge), ACP (Anthropic Console Proxy), Codex (OpenAI). All use `RetryDo()` for retries. Loads from `llm_providers` table with encrypted API keys
- **Agent loop:** `RunRequest` → think→act→observe → `RunResult`. Events: `run.started`, `run.completed`, `chunk`, `tool.call`, `tool.result`. Auto-summarization at >75% context
- **Context propagation:** `store.WithAgentType(ctx)`, `store.WithUserID(ctx)`, `store.WithAgentID(ctx)`, `store.WithLocale(ctx)`
- **WebSocket protocol (v3):** Frame types `req`/`res`/`event`. First request must be `connect`
- **Config:** JSON5 at `GOCLAW_CONFIG` env. Secrets in `.env.local` or env vars, never in config.json
- **Security:** Rate limiting, input guard (detection-only), CORS, shell deny patterns, SSRF protection, path traversal prevention, AES-256-GCM encryption. All security logs: `slog.Warn("security.*")`
- **Telegram formatting:** LLM output → `SanitizeAssistantContent()` → `markdownToTelegramHTML()` → `chunkHTML()` → `sendHTML()`. Tables rendered as ASCII in `<pre>` tags
- **i18n:** Web UI uses `i18next` with namespace-split locale files in `ui/web/src/i18n/locales/{lang}/`. Backend uses `internal/i18n` message catalog with `i18n.T(locale, key, args...)`. Locale propagated via `store.WithLocale(ctx)` — WS `connect` param `locale`, HTTP `Accept-Language` header. Supported: en (default), vi, zh. New user-facing strings: add key to `internal/i18n/keys.go`, add translations to all 3 catalog files. New UI strings: add key to all 3 locale dirs. Bootstrap templates (SOUL.md, etc.) stay English-only (LLM consumption).

## Running

```bash
go build -o goclaw . && ./goclaw onboard && source .env.local && ./goclaw
./goclaw migrate up                 # DB migrations
go test -v ./tests/integration/     # Integration tests

cd ui/web && pnpm install && pnpm dev   # Web dashboard (dev)
```

## Post-Implementation Checklist

After implementing or modifying Go code, run these checks:

```bash
go fix ./...                        # Apply Go version upgrades (run before commit)
go build ./...                      # Compile check
go vet ./...                        # Static analysis
go test -race ./tests/integration/  # Integration tests with race detector
```

Go conventions to follow:
- Use `errors.Is(err, sentinel)` instead of `err == sentinel`
- Use `switch/case` instead of `if/else if` chains on the same variable
- Use `append(dst, src...)` instead of loop-based append
- Always handle errors; don't ignore return values
- **Migrations:** When adding a new SQL migration file in `migrations/`, bump `RequiredSchemaVersion` in `internal/upgrade/version.go` to match the new migration number
- **i18n strings:** When adding user-facing error messages, add key to `internal/i18n/keys.go` and translations to `catalog_en.go`, `catalog_vi.go`, `catalog_zh.go`. For UI strings, add to all locale JSON files in `ui/web/src/i18n/locales/{en,vi,zh}/`
- **SQL safety:** When implementing or modifying SQL store code (`store/pg/*.go`), always verify: (1) All user inputs use parameterized queries (`$1, $2, ...`), never string concatenation — prevents SQL injection. (2) Queries are optimized — no N+1 queries, no unnecessary full table scans. (3) WHERE clauses, JOINs, and ORDER BY columns use existing indices — check migration files for available indexes
- **DB query reuse:** Before adding a new DB query for key entities (teams, agents, sessions, users), check if the same data is already fetched earlier in the current flow/pipeline. Prefer passing resolved data through context, event payloads, or function params rather than re-querying. Duplicate queries waste DB resources and add latency
- **Solution design:** When designing a fix or feature, identify the root cause first — don't just patch symptoms. Think through production scenarios (high concurrency, multi-tenant isolation, failure cascades, long-running sessions) to ensure the solution holds up. Prefer explicit configuration over runtime heuristics. Prefer the simplest solution that addresses the root cause directly

## Mobile UI/UX Rules

When implementing or modifying web UI components, follow these rules to ensure mobile compatibility:

- **Viewport height:** Use `h-dvh` (dynamic viewport height), never `h-screen`. `h-screen` causes content to hide behind mobile browser chrome and virtual keyboards
- **Input font-size:** All `<input>`, `<textarea>`, `<select>` must use `text-base md:text-sm` (16px on mobile). Font-size < 16px triggers iOS Safari auto-zoom on focus
- **Safe areas:** Root layout must use `viewport-fit=cover` meta tag. Apply `safe-top`, `safe-bottom`, `safe-left`, `safe-right` utility classes on edge-anchored elements (app shell, sidebar, toasts, chat input) for notched devices
- **Touch targets:** Icon buttons must have ≥44px hit area on touch devices. CSS in `index.css` uses `@media (pointer: coarse)` with `::after` pseudo-elements to expand targets
- **Tables:** Always wrap `<table>` in `<div className="overflow-x-auto">` and set `min-w-[600px]` on the table for horizontal scroll on narrow screens
- **Grid layouts:** Use mobile-first responsive grids: `grid-cols-1 sm:grid-cols-2 lg:grid-cols-N`. Never use fixed `grid-cols-N` without a mobile breakpoint
- **Dialogs:** Full-screen on mobile with slide-up animation (`max-sm:inset-0`), centered with zoom on desktop (`sm:max-w-lg`). Handled in `ui/dialog.tsx`
- **Virtual keyboard:** Chat input uses `useVirtualKeyboard()` hook + `var(--keyboard-height, 0px)` CSS var to stay above the keyboard
- **Scroll behavior:** Use `overscroll-contain` on scrollable areas to prevent background scroll. Auto-scroll: smooth for incoming messages, instant on user send
- **Landscape:** Use `landscape-compact` class on top bars to reduce padding in phone landscape orientation (`max-height: 500px`)
- **Portal dropdowns in dialogs:** Custom dropdown components using `createPortal(content, document.body)` MUST add `pointer-events-auto` class to the dropdown element. Radix Dialog sets `pointer-events: none` on `document.body` — without this class, dropdowns are unclickable. Radix-native portals (Select, Popover) handle this automatically
- **Timezone:** User timezone stored in Zustand (`useUiStore`). Charts use `formatBucketTz()` from `lib/format.ts` with native `Intl.DateTimeFormat` — no date-fns-tz dependency
- **ErrorBoundary key:** `AppLayout` uses `<ErrorBoundary key={stableErrorBoundaryKey(pathname)}>` which strips dynamic segments (`/chat/session-A` → `/chat`). NEVER use `key={location.pathname}` on ErrorBoundary/Suspense wrapping `<Outlet>` — it causes full page remount on param changes. Pages with sub-navigation (chat sessions, detail pages) must share a stable key
- **Route params as source of truth:** For pages with URL params (e.g. `/chat/:sessionKey`), derive state from `useParams()` — do NOT duplicate into `useState`. Dual state causes race conditions between `setState` and `navigate()` leading to UI flash (state bounces: B→A→B). Use optional params (`/chat/:sessionKey?`) instead of two separate routes

```

### File: docker-entrypoint.sh
```sh
#!/bin/sh
set -e

# Set up writable runtime directories for agent-installed packages.
# Rootfs is read-only; /app/data is a writable Docker volume.
RUNTIME_DIR="/app/data/.runtime"
# Non-fatal: on first start with a fresh volume the directory may not be
# writable yet (volume initialisation race on some Docker runtimes).
# The app starts fine without .runtime; package installs will fail gracefully.
mkdir -p "$RUNTIME_DIR/pip" "$RUNTIME_DIR/npm-global/lib" "$RUNTIME_DIR/pip-cache" || true

# Fix .runtime ownership for split root/goclaw access.
# .runtime itself must be root-owned so pkg-helper (root) can write apk-packages.
# Subdirs pip/, npm-global/, pip-cache/ must be goclaw-owned for runtime installs.
# This also handles upgrades from older images where .runtime was fully goclaw-owned.
if [ "$(id -u)" = "0" ] && [ -d "$RUNTIME_DIR" ]; then
  chown root:goclaw "$RUNTIME_DIR" 2>/dev/null || true
  chmod 0750 "$RUNTIME_DIR" 2>/dev/null || true
  chown -R goclaw:goclaw "$RUNTIME_DIR/pip" "$RUNTIME_DIR/npm-global" "$RUNTIME_DIR/pip-cache" 2>/dev/null || true
fi

# Python: allow agent to pip install to writable target dir
export PYTHONPATH="$RUNTIME_DIR/pip:${PYTHONPATH:-}"
export PIP_TARGET="$RUNTIME_DIR/pip"
export PIP_BREAK_SYSTEM_PACKAGES=1
export PIP_CACHE_DIR="$RUNTIME_DIR/pip-cache"

# Node.js: allow agent to npm install -g to writable prefix
# NODE_PATH includes both pre-installed system globals and runtime-installed globals.
export NPM_CONFIG_PREFIX="$RUNTIME_DIR/npm-global"
export NODE_PATH="/usr/local/lib/node_modules:$RUNTIME_DIR/npm-global/lib/node_modules:${NODE_PATH:-}"
export PATH="$RUNTIME_DIR/npm-global/bin:$RUNTIME_DIR/pip/bin:$PATH"

# System packages: re-install on-demand packages persisted across recreates.
# After chown above, root owns .runtime and can create this file.
APK_LIST="$RUNTIME_DIR/apk-packages"
if [ "$(id -u)" = "0" ]; then
  touch "$APK_LIST" 2>/dev/null || true
  chown root:goclaw "$APK_LIST" 2>/dev/null || true
  chmod 0640 "$APK_LIST" 2>/dev/null || true
fi
if [ -f "$APK_LIST" ] && [ -s "$APK_LIST" ]; then
  echo "Re-installing persisted system packages..."
  VALID_PKGS=""
  while IFS= read -r pkg || [ -n "$pkg" ]; do
    pkg="$(printf '%s' "$pkg" | tr -d '[:space:]')"
    case "$pkg" in
      [a-zA-Z0-9@]*) VALID_PKGS="$VALID_PKGS $pkg" ;;
      "") ;;
      *) echo "WARNING: skipping invalid package: $pkg" ;;
    esac
  done < "$APK_LIST"
  if [ -n "$VALID_PKGS" ]; then
    # shellcheck disable=SC2086
    apk add --no-cache $VALID_PKGS 2>/dev/null || \
      echo "Warning: some packages failed to install"
  fi
fi

# Start the root-privileged package helper (listens on /tmp/pkg.sock).
# Only in Docker (running as root). Outside Docker, pkg-helper is not available.
if [ -x /app/pkg-helper ] && [ "$(id -u)" = "0" ]; then
  /app/pkg-helper &
  PKG_PID=$!
  for _i in 1 2 3 4; do
    [ -S /tmp/pkg.sock ] && break
    sleep 0.5
  done
  if ! [ -S /tmp/pkg.sock ]; then
    echo "ERROR: pkg-helper failed to start (PID $PKG_PID)"
    kill "$PKG_PID" 2>/dev/null || true
  fi
fi

# Copy Claude CLI credentials from root-owned read-only mount to goclaw-accessible location.
# /app/.claude is a symlink → /app/data/.claude (writable volume, see Dockerfile).
# Uses install(1) for atomic copy with correct ownership+permissions (no temp file needed).
if [ -f /app/.claude-host/.credentials.json ]; then
  (mkdir -p /app/data/.claude \
    && install -m 600 -o goclaw -g goclaw /app/.claude-host/.credentials.json /app/data/.claude/.credentials.json \
    && echo "Claude CLI credentials synced from host.") || echo "WARNING: Claude credentials copy failed (non-fatal)"
fi

# Run command with privilege drop (su-exec in Docker, direct otherwise).
run_as_goclaw() {
  if command -v su-exec >/dev/null 2>&1 && [ "$(id -u)" = "0" ]; then
    exec su-exec goclaw "$@"
  else
    exec "$@"
  fi
}

case "${1:-serve}" in
  serve)
    # Auto-upgrade (schema migrations + data hooks) before starting.
    if [ -n "$GOCLAW_POSTGRES_DSN" ]; then
      echo "Running database upgrade..."
      if command -v su-exec >/dev/null 2>&1 && [ "$(id -u)" = "0" ]; then
        su-exec goclaw /app/goclaw upgrade || \
          echo "Upgrade warning (may already be up-to-date)"
      else
        /app/goclaw upgrade || \
          echo "Upgrade warning (may already be up-to-date)"
      fi
    fi
    run_as_goclaw /app/goclaw
    ;;
  upgrade)
    shift
    run_as_goclaw /app/goclaw upgrade "$@"
    ;;
  migrate)
    shift
    run_as_goclaw /app/goclaw migrate "$@"
    ;;
  onboard)
    run_as_goclaw /app/goclaw onboard
    ;;
  version)
    run_as_goclaw /app/goclaw version
    ;;
  *)
    run_as_goclaw /app/goclaw "$@"
    ;;
esac

```

### File: main.go
```go
package main

import (
	_ "time/tzdata" // embed IANA timezone database for containers without tzdata

	"github.com/nextlevelbuilder/goclaw/cmd"
)

func main() {
	cmd.Execute()
}

```

### File: prepare-env.sh
```sh
#!/usr/bin/env bash
# prepare-env.sh — Create or update .env with auto-generated secrets.
# Safe to run multiple times: only fills in missing values, never overwrites existing ones.
#
# Usage:  ./prepare-env.sh

set -euo pipefail

ENV_FILE=".env"

# --- helpers ---

gen_hex() { openssl rand -hex "$1" 2>/dev/null || head -c "$1" /dev/urandom | xxd -p | tr -d '\n'; }

# Read current value from .env (KEY=VALUE format, no export prefix).
get_env_val() {
  local key="$1"
  if [ -f "$ENV_FILE" ]; then
    grep -E "^${key}=" "$ENV_FILE" 2>/dev/null | tail -1 | cut -d'=' -f2-
  fi
}

# Set a key in .env. Appends if missing, replaces if empty.
set_env_val() {
  local key="$1" val="$2"
  if [ ! -f "$ENV_FILE" ]; then
    echo "${key}=${val}" >> "$ENV_FILE"
  elif grep -qE "^${key}=" "$ENV_FILE" 2>/dev/null; then
    # Key exists — only replace if current value is empty
    local current
    current="$(get_env_val "$key")"
    if [ -z "$current" ]; then
      if [[ "$OSTYPE" == "darwin"* ]]; then
        sed -i '' "s|^${key}=.*|${key}=${val}|" "$ENV_FILE"
      else
        sed -i "s|^${key}=.*|${key}=${val}|" "$ENV_FILE"
      fi
    fi
  else
    echo "${key}=${val}" >> "$ENV_FILE"
  fi
}

# --- main ---

echo ""
echo "=== GoClaw Environment Preparation ==="
echo ""

# 1. Create .env from .env.example if it doesn't exist
if [ ! -f "$ENV_FILE" ]; then
  if [ -f ".env.example" ]; then
    # Strip 'export ' prefix for Docker Compose compatibility
    sed 's/^export //' .env.example > "$ENV_FILE"
    echo "  [created]   .env from .env.example"
  else
    touch "$ENV_FILE"
    echo "  [created]   .env (empty)"
  fi
else
  echo "  [exists]    .env"
fi

# 2. Auto-generate GOCLAW_ENCRYPTION_KEY if missing
current_enc="$(get_env_val GOCLAW_ENCRYPTION_KEY)"
if [ -z "$current_enc" ]; then
  new_key="$(gen_hex 32)"
  set_env_val "GOCLAW_ENCRYPTION_KEY" "$new_key"
  echo "  [generated] GOCLAW_ENCRYPTION_KEY"
else
  echo "  [exists]    GOCLAW_ENCRYPTION_KEY"
fi

# 3. Auto-generate GOCLAW_GATEWAY_TOKEN if missing
current_tok="$(get_env_val GOCLAW_GATEWAY_TOKEN)"
if [ -z "$current_tok" ]; then
  new_tok="$(gen_hex 16)"
  set_env_val "GOCLAW_GATEWAY_TOKEN" "$new_tok"
  echo "  [generated] GOCLAW_GATEWAY_TOKEN"
else
  echo "  [exists]    GOCLAW_GATEWAY_TOKEN"
fi

echo ""
echo "=== Done ==="
echo ""
echo "  Run: docker compose -f docker-compose.yml -f docker-compose.postgres.yml -f docker-compose.selfservice.yml up -d --build"
echo ""

```

### File: websocket_protocol.md
```md
# WebSocket Protocol (v3)

Frame types: `req` (client request), `res` (server response), `event` (server push).

## Authentication

The first request must be a `connect` handshake. Authentication supports three paths:

```json
// Path 1: Token-based (admin role)
{"type": "req", "id": 1, "method": "connect", "params": {"token": "your-gateway-token", "user_id": "alice"}}

// Path 2: Browser pairing reconnect (operator role)
{"type": "req", "id": 1, "method": "connect", "params": {"sender_id": "previously-paired-id", "user_id": "alice"}}

// Path 3: No token — initiates browser pairing flow (returns pairing code)
{"type": "req", "id": 1, "method": "connect", "params": {"user_id": "alice"}}
```

## Methods

| Method | Description |
|--------|-------------|
| `connect` | Authentication handshake (must be first request) |
| `health` | Server health check |
| `status` | Server status and metadata |
| `chat.send` | Send a message to an agent |
| `chat.history` | Retrieve session history |
| `chat.abort` | Abort a running agent request |
| `agent` | Get agent info |
| `sessions.list` | List active sessions |
| `sessions.delete` | Delete a session |
| `sessions.label` | Label a session |
| `skills.list` | List available skills |
| `cron.list` | List scheduled jobs |
| `cron.create` | Create a cron job |
| `cron.delete` | Delete a cron job |
| `cron.toggle` | Enable/disable a cron job |
| `models.list` | List available AI models |
| `browser.pairing.status` | Poll pairing approval status |
| `device.pair.request` | Request device pairing |
| `device.pair.approve` | Approve a pairing code |
| `device.pair.list` | List pending and approved pairings |
| `device.pair.revoke` | Revoke a pairing |

## Events (server push)

| Event | Description |
|-------|-------------|
| `chunk` | Streaming token from LLM (payload: `{content}`) |
| `tool.call` | Agent invoking a tool (payload: `{name, id}`) |
| `tool.result` | Tool execution result |
| `run.started` | Agent started processing |
| `run.completed` | Agent finished processing |
| `shutdown` | Server shutting down |

## Frame Format

### Request (client to server)
```json
{
  "type": "req",
  "id": "unique-request-id",
  "method": "chat.send",
  "params": { ... }
}
```

### Response (server to client)
```json
{
  "type": "res",
  "id": "matching-request-id",
  "ok": true,
  "payload": { ... }
}
```

### Error Response
```json
{
  "type": "res",
  "id": "matching-request-id",
  "ok": false,
  "error": {
    "code": "error_code",
    "message": "Human-readable error message"
  }
}
```

### Event (server push)
```json
{
  "type": "event",
  "event": "chunk",
  "payload": { "content": "streaming text..." }
}
```

```

### File: cmd\agent.go
```go
package cmd

import (
	"encoding/json"
	"fmt"
	"os"
	"sort"
	"text/tabwriter"

	"github.com/spf13/cobra"

	"github.com/nextlevelbuilder/goclaw/internal/config"
)

func agentCmd() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "agent",
		Short: "Manage agents — add, list, delete",
	}
	cmd.AddCommand(agentListCmd())
	cmd.AddCommand(agentAddCmd())
	cmd.AddCommand(agentDeleteCmd())
	cmd.AddCommand(agentChatCmd())
	return cmd
}

// --- agent list ---

func agentListCmd() *cobra.Command {
	var jsonOutput bool
	cmd := &cobra.Command{
		Use:   "list",
		Short: "List all configured agents",
		Run: func(cmd *cobra.Command, args []string) {
			runAgentList(jsonOutput)
		},
	}
	cmd.Flags().BoolVar(&jsonOutput, "json", false, "output as JSON")
	return cmd
}

type agentListEntry struct {
	ID          string `json:"id"`
	DisplayName string `json:"displayName"`
	Provider    string `json:"provider"`
	Model       string `json:"model"`
	Workspace   string `json:"workspace,omitempty"`
	IsDefault   bool   `json:"isDefault"`
}

func runAgentList(jsonOutput bool) {
	cfgPath := resolveConfigPath()
	cfg, err := config.Load(cfgPath)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error loading config: %v\n", err)
		os.Exit(1)
	}

	var entries []agentListEntry

	// Default agent (always present)
	d := cfg.Agents.Defaults
	defaultID := cfg.ResolveDefaultAgentID()
	entries = append(entries, agentListEntry{
		ID:          config.DefaultAgentID,
		DisplayName: cfg.ResolveDisplayName(config.DefaultAgentID),
		Provider:    d.Provider,
		Model:       d.Model,
		Workspace:   d.Workspace,
		IsDefault:   defaultID == config.DefaultAgentID,
	})

	// Agents from list
	ids := make([]string, 0, len(cfg.Agents.List))
	for id := range cfg.Agents.List {
		if id == config.DefaultAgentID {
			continue
		}
		ids = append(ids, id)
	}
	sort.Strings(ids)

	for _, id := range ids {
		resolved := cfg.ResolveAgent(id)
		spec := cfg.Agents.List[id]
		name := spec.DisplayName
		if name == "" {
			name = id
		}
		entries = append(entries, agentListEntry{
			ID:          id,
			DisplayName: name,
			Provider:    resolved.Provider,
			Model:       resolved.Model,
			Workspace:   resolved.Workspace,
			IsDefault:   id == defaultID,
		})
	}

	if jsonOutput {
		data, _ := json.MarshalIndent(entries, "", "  ")
		fmt.Println(string(data))
		return
	}

	if len(entries) == 0 {
		fmt.Println("No agents configured.")
		return
	}

	w := tabwriter.NewWriter(os.Stdout, 0, 4, 2, ' ', 0)
	fmt.Fprintln(w, "ID\tDISPLAY NAME\tPROVIDER\tMODEL\tDEFAULT")
	for _, e := range entries {
		def := ""
		if e.IsDefault {
			def = "*"
		}
		fmt.Fprintf(w, "%s\t%s\t%s\t%s\t%s\n", e.ID, e.DisplayName, e.Provider, e.Model, def)
	}
	w.Flush()
}

// --- agent add ---

func agentAddCmd() *cobra.Command {
	return &cobra.Command{
		Use:   "add",
		Short: "Add a new agent (interactive wizard)",
		Run: func(cmd *cobra.Command, args []string) {
			runAgentAdd()
		},
	}
}

func runAgentAdd() {
	cfgPath := resolveConfigPath()
	cfg, err := config.Load(cfgPath)
	if err != nil {
		// Start with default config if no file exists
		if _, statErr := os.Stat(cfgPath); os.IsNotExist(statErr) {
			cfg = config.Default()
		} else {
			fmt.Fprintf(os.Stderr, "Error loading config: %v\n", err)
			os.Exit(1)
		}
	}

	fmt.Println("── Add New Agent ──")
	fmt.Println()

	// Step 1: Agent name (with validation loop)
	var name string
	for {
		name, err = promptString("Agent name", "e.g. coder, researcher, assistant", "")
		if err != nil {
			fmt.Println("Cancelled.")
			return
		}
		if name == "" {
			fmt.Println("  Name is required.")
			continue
		}
		id := config.NormalizeAgentID(name)
		if id == config.DefaultAgentID {
			fmt.Printf("  %q is reserved.\n", config.DefaultAgentID)
			continue
		}
		if _, exists := cfg.Agents.List[id]; exists {
			fmt.Printf("  Agent %q already exists.\n", id)
			continue
		}
		break
	}

	agentID := config.NormalizeAgentID(name)
	if name != agentID {
		fmt.Printf("  Normalized ID: %s\n", agentID)
	}

	// Step 2: Display name
	displayName, err := promptString("Display name", "", name)
	if err != nil {
		fmt.Println("Cancelled.")
		return
	}

	// Step 3: Provider (optional override)
	providerOptions := []SelectOption[string]{
		{fmt.Sprintf("Inherit from defaults (%s)", cfg.Agents.Defaults.Provider), ""},
		{"OpenRouter", "openrouter"},
		{"Anthropic", "anthropic"},
		{"OpenAI", "openai"},
		{"Groq", "groq"},
		{"DeepSeek", "deepseek"},
		{"Gemini", "gemini"},
		{"Mistral", "mistral"},
	}

	providerChoice, err := promptSelect("Provider", providerOptions, 0)
	if err != nil {
		fmt.Println("Cancelled.")
		return
	}

	// Step 4: Model (optional override)
	modelPlaceholder := fmt.Sprintf("(inherit: %s)", cfg.Agents.Defaults.Model)
	model, err := promptString("Model (empty = inherit from defaults)", modelPlaceholder, "")
	if err != nil {
		fmt.Println("Cancelled.")
		return
	}

	// Step 5: Workspace
	defaultWS := fmt.Sprintf("%s/%s", cfg.Agents.Defaults.Workspace, agentID)
	workspace, err := promptString("Workspace directory", "", defaultWS)
	if err != nil {
		fmt.Println("Cancelled.")
		return
	}

	// Build AgentSpec
	spec := config.AgentSpec{
		DisplayName: displayName,
		Provider:    providerChoice,
		Model:       model,
		Workspace:   workspace,
	}

	// Add to config
	if cfg.Agents.List == nil {
		cfg.Agents.List = make(map[string]config.AgentSpec)
	}
	cfg.Agents.List[agentID] = spec

	// Create workspace directory
	expandedWS := config.ExpandHome(workspace)
	if err := os.MkdirAll(expandedWS, 0755); err != nil {
		fmt.Printf("Warning: could not create workspace: %v\n", err)
	}

	// Save config (strip secrets like onboard does)
	savedProviders := cfg.Providers
	savedGwToken := cfg.Gateway.Token
	savedTgToken := cfg.Channels.Telegram.Token
	cfg.Providers = config.ProvidersConfig{}
	cfg.Gateway.Token = ""
	cfg.Channels.Telegram.Token = ""

	saveErr := config.Save(cfgPath, cfg)

	cfg.Providers = savedProviders
	cfg.Gateway.Token = savedGwToken
	cfg.Channels.Telegram.Token = savedTgToken

	if saveErr != nil {
		fmt.Fprintf(os.Stderr, "Error saving config: %v\n", saveErr)
		os.Exit(1)
	}

	fmt.Println()
	fmt.Printf("Agent %q created successfully.\n", agentID)
	fmt.Printf("  Display name: %s\n", displayName)
	if providerChoice != "" {
		fmt.Printf("  Provider:     %s\n", providerChoice)
	} else {
		fmt.Printf("  Provider:     (inherit: %s)\n", cfg.Agents.Defaults.Provider)
	}
	if model != "" {
		fmt.Printf("  Model:        %s\n", model)
	} else {
		fmt.Printf("  Model:        (inherit: %s)\n", cfg.Agents.Defaults.Model)
	}
	fmt.Printf("  Workspace:    %s\n", workspace)
	fmt.Println()
	fmt.Println("Restart the gateway to activate this agent.")
}

// --- agent delete ---

func agentDeleteCmd() *cobra.Command {
	var force bool
	cmd := &cobra.Command{
		Use:   "delete <agent-id>",
		Short: "Delete an agent",
		Args:  cobra.ExactArgs(1),
		Run: func(cmd *cobra.Command, args []string) {
			runAgentDelete(args[0], force)
		},
	}
	cmd.Flags().BoolVar(&force, "force", false, "skip confirmation")
	return cmd
}

func runAgentDelete(rawID string, force bool) {
	agentID := config.NormalizeAgentID(rawID)

	if agentID == config.DefaultAgentID {
		fmt.Fprintf(os.Stderr, "Error: %q cannot be deleted (reserved).\n", config.DefaultAgentID)
		os.Exit(1)
	}

	cfgPath := resolveConfigPath()
	cfg, err := config.Load(cfgPath)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error loading config: %v\n", err)
		os.Exit(1)
	}

	if _, exists := cfg.Agents.List[agentID]; !exists {
		fmt.Fprintf(os.Stderr, "Error: agent %q not found.\n", agentID)
		os.Exit(1)
	}

	if !force {
		confirmed, err := promptConfirm(fmt.Sprintf("Delete agent %q?", agentID), false)
		if err != nil || !confirmed {
			fmt.Println("Cancelled.")
			return
		}
	}

	// Remove agent
	delete(cfg.Agents.List, agentID)

	// Remove bindings that reference this agent
	removedBindings := 0
	if len(cfg.Bindings) > 0 {
		filtered := make([]config.AgentBinding, 0, len(cfg.Bindings))
		for _, b := range cfg.Bindings {
			if config.NormalizeAgentID(b.AgentID) == agentID {
				removedBindings++
				continue
			}
			filtered = append(filtered, b)
		}
		cfg.Bindings = filtered
		if len(cfg.Bindings) == 0 {
			cfg.Bindings = nil
		}
	}

	// Save config (strip secrets)
	savedProviders := cfg.Providers
	savedGwToken := cfg.Gateway.Token
	savedTgToken := cfg.Channels.Telegram.Token
	cfg.Providers = config.ProvidersConfig{}
	cfg.Gateway.Token = ""
	cfg.Channels.Telegram.Token = ""

	saveErr := config.Save(cfgPath, cfg)

	cfg.Providers = savedProviders
	cfg.Gateway.Token = savedGwToken
	cfg.Channels.Telegram.Token = savedTgToken

	if saveErr != nil {
		fmt.Fprintf(os.Stderr, "Error saving config: %v\n", saveErr)
		os.Exit(1)
	}

	fmt.Printf("Agent %q deleted.\n", agentID)
	if removedBindings > 0 {
		fmt.Printf("Removed %d binding(s) that referenced this agent.\n", removedBindings)
	}
	fmt.Println("Restart the gateway to apply changes.")
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
