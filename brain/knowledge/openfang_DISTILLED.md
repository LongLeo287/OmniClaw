---
id: openfang
type: knowledge
owner: OA_Triage
---
# openfang
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<p align="center">
  <img src="public/assets/openfang-logo.png" width="160" alt="OpenFang Logo" />
</p>

<h1 align="center">OpenFang</h1>
<h3 align="center">The Agent Operating System</h3>

<p align="center">
  Open-source Agent OS built in Rust. 137K LOC. 14 crates. 1,767+ tests. Zero clippy warnings.<br/>
  <strong>One binary. Battle-tested. Agents that actually work for you.</strong>
</p>

<p align="center">
  <a href="https://openfang.sh/docs">Documentation</a> &bull;
  <a href="https://openfang.sh/docs/getting-started">Quick Start</a> &bull;
  <a href="https://x.com/openfangg">Twitter / X</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/language-Rust-orange?style=flat-square" alt="Rust" />
  <img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="MIT" />
  <img src="https://img.shields.io/badge/version-0.3.30-green?style=flat-square" alt="v0.3.30" />
  <img src="https://img.shields.io/badge/tests-1,767%2B%20passing-brightgreen?style=flat-square" alt="Tests" />
  <img src="https://img.shields.io/badge/clippy-0%20warnings-brightgreen?style=flat-square" alt="Clippy" />
  <a href="https://www.buymeacoffee.com/openfang" target="_blank"><img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-FFDD00?style=flat-square&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me A Coffee" /></a>
</p>

---

> **v0.3.30 — Security Hardening Release (March 2026)**
>
> OpenFang is feature-complete but still pre-1.0. You may encounter rough edges or breaking changes between minor versions. We ship fast and fix fast. Pin to a specific commit for production use until v1.0. [Report issues here.](https://github.com/RightNow-AI/openfang/issues)

---

## What is OpenFang?

OpenFang is an **open-source Agent Operating System** — not a chatbot framework, not a Python wrapper around an LLM, not a "multi-agent orchestrator." It is a full operating system for autonomous agents, built from scratch in Rust.

Traditional agent frameworks wait for you to type something. OpenFang runs **autonomous agents that work for you** — on schedules, 24/7, building knowledge graphs, monitoring targets, generating leads, managing your social media, and reporting results to your dashboard.

The entire system compiles to a **single ~32MB binary**. One install, one command, your agents are live.

```bash
curl -fsSL https://openfang.sh/install | sh
openfang init
openfang start
# Dashboard live at http://localhost:4200
```

<details>
<summary><strong>Windows</strong></summary>

```powershell
irm https://openfang.sh/install.ps1 | iex
openfang init
openfang start
```

</details>

---

## Hands: Agents That Actually Do Things

<p align="center"><em>"Traditional agents wait for you to type. Hands work <strong>for</strong> you."</em></p>

**Hands** are OpenFang's core innovation — pre-built autonomous capability packages that run independently, on schedules, without you having to prompt them. This is not a chatbot. This is an agent that wakes up at 6 AM, researches your competitors, builds a knowledge graph, scores the findings, and delivers a report to your Telegram before you've had coffee.

Each Hand bundles:
- **HAND.toml** — Manifest declaring tools, settings, requirements, and dashboard metrics
- **System Prompt** — Multi-phase operational playbook (not a one-liner — these are 500+ word expert procedures)
- **SKILL.md** — Domain expertise reference injected into context at runtime
- **Guardrails** — Approval gates for sensitive actions (e.g. Browser Hand requires approval before any purchase)

All compiled into the binary. No downloading, no pip install, no Docker pull.

### The 7 Bundled Hands

| Hand | What It Actually Does |
|------|----------------------|
| **Clip** | Takes a YouTube URL, downloads it, identifies the best moments, cuts them into vertical shorts with captions and thumbnails, optionally adds AI voice-over, and publishes to Telegram and WhatsApp. 8-phase pipeline. FFmpeg + yt-dlp + 5 STT backends. |
| **Lead** | Runs daily. Discovers prospects matching your ICP, enriches them with web research, scores 0-100, deduplicates against your existing database, and delivers qualified leads in CSV/JSON/Markdown. Builds ICP profiles over time. |
| **Collector** | OSINT-grade intelligence. You give it a target (company, person, topic). It monitors continuously — change detection, sentiment tracking, knowledge graph construction, and critical alerts when something important shifts. |
| **Predictor** | Superforecasting engine. Collects signals from multiple sources, builds calibrated reasoning chains, makes predictions with confidence intervals, and tracks its own accuracy using Brier scores. Has a contrarian mode that deliberately argues against consensus. |
| **Researcher** | Deep autonomous researcher. Cross-references multiple sources, evaluates credibility using CRAAP criteria (Currency, Relevance, Authority, Accuracy, Purpose), generates cited reports with APA formatting, supports multiple languages. |
| **Twitter** | Autonomous Twitter/X account manager. Creates content in 7 rotating formats, schedules posts for optimal engagement, responds to mentions, tracks performance metrics. Has an approval queue — nothing posts without your OK. |
| **Browser** | Web automation agent. Navigates sites, fills forms, clicks buttons, handles multi-step workflows. Uses Playwright bridge with session persistence. **Mandatory purchase approval gate** — it will never spend your money without explicit confirmation. |

```bash
# Activate the Researcher Hand — it starts working immediately
openfang hand activate researcher

# Check its progress anytime
openfang hand status researcher

# Activate lead generation on a daily schedule
openfang hand activate lead

# Pause without losing state
openfang hand pause lead

# See all available Hands
openfang hand list
```

**Build your own.** Define a `HAND.toml` with tools, settings, and a system prompt. Publish to FangHub.

---

## OpenFang vs The Landscape

<p align="center">
  <img src="public/assets/openfang-vs-claws.png" width="600" alt="OpenFang vs OpenClaw vs ZeroClaw" />
</p>

### Benchmarks: Measured, Not Marketed

All data from official documentation and public repositories — February 2026.

#### Cold Start Time (lower is better)

```
ZeroClaw   ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   10 ms
OpenFang   ██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  180 ms    ★
LangGraph  █████████████████░░░░░░░░░░░░░░░░░░░░░░░░░  2.5 sec
CrewAI     ████████████████████░░░░░░░░░░░░░░░░░░░░░░  3.0 sec
AutoGen    ██████████████████████████░░░░░░░░░░░░░░░░░  4.0 sec
OpenClaw   █████████████████████████████████████████░░  5.98 sec
```

#### Idle Memory Usage (lower is better)

```
ZeroClaw   █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    5 MB
OpenFang   ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   40 MB    ★
LangGraph  ██████████████████░░░░░░░░░░░░░░░░░░░░░░░░░  180 MB
CrewAI     ████████████████████░░░░░░░░░░░░░░░░░░░░░░░  200 MB
AutoGen    █████████████████████████░░░░░░░░░░░░░░░░░░  250 MB
OpenClaw   ████████████████████████████████████████░░░░  394 MB
```

#### Install Size (lower is better)

```
ZeroClaw   █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  8.8 MB
OpenFang   ███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   32 MB    ★
CrewAI     ████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  100 MB
LangGraph  ████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  150 MB
AutoGen    ████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░  200 MB
OpenClaw   ████████████████████████████████████████░░░░  500 MB
```

#### Security Systems (higher is better)

```
OpenFang   ████████████████████████████████████████████   16      ★
ZeroClaw   ███████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░    6
OpenClaw   ████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    3
AutoGen    █████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    2
LangGraph  █████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    2
CrewAI     ███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    1
```

#### Channel Adapters (higher is better)

```
OpenFang   ████████████████████████████████████████████   40      ★
ZeroClaw   ███████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░   15
OpenClaw   █████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   13
CrewAI     ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    0
AutoGen    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    0
LangGraph  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    0
```

#### LLM Providers (higher is better)

```
ZeroClaw   ████████████████████████████████████████████   28
OpenFang   ██████████████████████████████████████████░░   27      ★
LangGraph  ██████████████████████░░░░░░░░░░░░░░░░░░░░░   15
CrewAI     ██████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   10
OpenClaw   ██████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   10
AutoGen    ███████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    8
```

### Feature-by-Feature Comparison

| Feature | OpenFang | OpenClaw | ZeroClaw | CrewAI | AutoGen | LangGraph |
|---------|----------|----------|----------|--------|---------|-----------|
| **Language** | **Rust** | TypeScript | **Rust** | Python | Python | Python |
| **Autonomous Hands** | **7 built-in** | None | None | None | None | None |
| **Security Layers** | **16 discrete** | 3 basic | 6 layers | 1 basic | Docker | AES enc. |
| **Agent Sandbox** | **WASM dual-metered** | None | Allowlists | None | Docker | None |
| **Channel Adapters** | **40** | 13 | 15 | 0 | 0 | 0 |
| **Built-in Tools** | **53 + MCP + A2A** | 50+ | 12 | Plugins | MCP | LC tools |
| **Memory** | **SQLite + vector** | File-based | SQLite FTS5 | 4-layer | External | Checkpoints |
| **Desktop App** | **Tauri 2.0** | None | None | None | Studio | None |
| **Audit Trail** | **Merkle hash-chain** | Logs | Logs | Tracing | Logs | Checkpoints |
| **Cold Start** | **<200ms** | ~6s | ~10ms | ~3s | ~4s | ~2.5s |
| **Install Size** | **~32 MB** | ~500 MB | ~8.8 MB | ~100 MB | ~200 MB | ~150 MB |
| **License** | MIT | MIT | MIT | MIT | Apache 2.0 | MIT |

---

## 16 Security Systems — Defense in Depth

OpenFang doesn't bolt security on after the fact. Every layer is independently testable and operates without a single point of failure.

| # | System | What It Does |
|---|--------|-------------|
| 1 | **WASM Dual-Metered Sandbox** | Tool code runs in WebAssembly with fuel metering + epoch interruption. A watchdog thread kills runaway code. |
| 2 | **Merkle Hash-Chain Audit Trail** | Every action is cryptographically linked to the previous one. Tamper with one entry and the entire chain breaks. |
| 3 | **Information Flow Taint Tracking** | Labels propagate through execution — secrets are tracked from source to sink. |
| 4 | **Ed25519 Signed Agent Manifests** | Every agent identity and capability set is cryptographically signed. |
| 5 | **SSRF Protection** | Blocks private IPs, cloud metadata endpoints, and DNS rebinding attacks. |
| 6 | **Secret Zeroization** | `Zeroizing<String>` auto-wipes API keys from memory the instant they're no longer needed. |
| 7 | **OFP Mutual Authentication** | HMAC-SHA256 nonce-based, constant-time verification for P2P networking. |
| 8 | **Capability Gates** | Role-based access control — agents declare required tools, the kernel enforces it. |
| 9 | **Security Headers** | CSP, X-Frame-Options, HSTS, X-Content-Type-Options on every response. |
| 10 | **Health Endpoint Redaction** | Public health check returns minimal info. Full diagnostics require authentication. |
| 11 | **Subprocess Sandbox** | `env_clear()` + selective variable passthrough. Process tree isolation with cross-platform kill. |
| 12 | **Prompt Injection Scanner** | Detects override attempts, data exfiltration patterns, and shell reference injection in skills. |
| 13 | **Loop Guard** | SHA256-based tool call loop detection with circuit breaker. Handles ping-pong patterns. |
| 14 | **Session Repair** | 7-phase message history validation and automatic recovery from corruption. |
| 15 | **Path Traversal Prevention** | Canonicalization with symlink escape prevention. `../` doesn't work here. |
| 16 | **GCRA Rate Limiter** | Cost-aware token bucket rate limiting with per-IP tracking and stale cleanup. |

---

## Architecture

14 Rust crates. 137,728 lines of code. Modular kernel design.

```
openfang-kernel      Orchestration, workflows, metering, RBAC, scheduler, budget tracking
openfang-runtime     Agent loop, 3 LLM drivers, 53 tools, WASM sandbox, MCP, A2A
openfang-api         140+ REST/WS/SSE endpoints, OpenAI-compatible API, dashboard
openfang-channels    40 messaging adapters with rate limiting, DM/group policies
openfang-memory      SQLite persistence, vector embeddings, canonical sessions, compaction
openfang-types       Core types, taint tracking, Ed25519 manifest signing, model catalog
openfang-skills      60 bundled skills, SKILL.md parser, FangHub marketplace
openfang-hands       7 autonomous Hands, HAND.toml parser, lifecycle management
openfang-extensions  25 MCP templates, AES-256-GCM credential vault, OAuth2 PKCE
openfang-wire        OFP P2P protocol with HMAC-SHA256 mutual authentication
openfang-cli         CLI with daemon management, TUI dashboard, MCP server mode
openfang-desktop     Tauri 2.0 native app (system tray, notifications, global shortcuts)
openfang-migrate     OpenClaw, LangChain, AutoGPT migration engine
xtask                Build automation
```

---

## 40 Channel Adapters

Connect your agents to every platform your users are on.

**Core:** Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Email (IMAP/SMTP)
**Enterprise:** Microsoft Teams, Mattermost, Google Chat, Webex, Feishu/Lark, Zulip
**Social:** LINE, Viber, Facebook Messenger, Mastodon, Bluesky, Reddit, LinkedIn, Twitch
**Community:** IRC, XMPP, Guilded, Revolt, Keybase, Discourse, Gitter
**Privacy:** Threema, Nostr, Mumble, Nextcloud Talk, Rocket.Chat, Ntfy, Gotify
**Workplace:** Pumble, Flock, Twist, DingTalk, Zalo, Webhooks

Each adapter supports per-channel model overrides, DM/group policies, rate limiting, and output formatting.

---

## WhatsApp Web Gateway (QR Code)

Connect your personal WhatsApp account to OpenFang via QR code — just like WhatsApp Web. No Meta Business account required.

### Prerequisites

- **Node.js >= 18** installed ([download](https://nodejs.org/))
- OpenFang installed and initialized

### Setup

**1. Install the gateway dependencies:**

```bash
cd packages/whatsapp-gateway
npm install
```

**2. Configure `config.toml`:**

```toml
[channels.whatsapp]
mode = "web"
default_agent = "assistant"
```

**3. Set the gateway URL (choose one):**

Add to your shell profile for persistence:

```bash
# macOS / Linux
echo 'export WHATSAPP_WEB_GATEWAY_URL="http://127.0.0.1:3009"' >> ~/.zshrc
source ~/.zshrc
```

Or set it inline when starting the gateway:

```bash
export WHATSAPP_WEB_GATEWAY_URL="http://127.0.0.1:3009"
```

**4. Start the gateway:**

```bash
node packages/whatsapp-gateway/index.js
```

The gateway listens on port `3009` by default. Override with `WHATSAPP_GATEWAY_PORT`.

**5. Start OpenFang:**

```bash
openfang start
# Dashboar
... [TRUNCATED]
```

### File: docs\README.md
```md
# OpenFang Documentation

Welcome to the OpenFang documentation. OpenFang is the open-source Agent Operating System -- 14 Rust crates, 40 channels, 60 skills, 20 LLM providers, 76 API endpoints, and 16 security systems in a single binary.

---

## Getting Started

| Guide | Description |
|-------|-------------|
| [Getting Started](getting-started.md) | Installation, first agent, first chat session |
| [Configuration](configuration.md) | Complete `config.toml` reference with every field |
| [CLI Reference](cli-reference.md) | Every command and subcommand with examples |
| [Troubleshooting](troubleshooting.md) | Common issues, FAQ, diagnostics |

## Core Concepts

| Guide | Description |
|-------|-------------|
| [Architecture](architecture.md) | 12-crate structure, kernel boot, agent lifecycle, memory substrate |
| [Agent Templates](agent-templates.md) | 30 pre-built agents across 4 performance tiers |
| [Workflows](workflows.md) | Multi-agent pipelines with branching, fan-out, loops, and triggers |
| [Security](security.md) | 16 defense-in-depth security systems |

## Integrations

| Guide | Description |
|-------|-------------|
| [Channel Adapters](channel-adapters.md) | 40 messaging channels -- setup, configuration, custom adapters |
| [LLM Providers](providers.md) | 20 providers, 51 models, 23 aliases -- setup and model routing |
| [Skills](skill-development.md) | 60 bundled skills, custom skill development, FangHub marketplace |
| [MCP & A2A](mcp-a2a.md) | Model Context Protocol and Agent-to-Agent protocol integration |

## Reference

| Guide | Description |
|-------|-------------|
| [API Reference](api-reference.md) | All 76 REST/WS/SSE endpoints with request/response examples |
| [Desktop App](desktop.md) | Tauri 2.0 native app -- build, features, architecture |

## Release & Operations

| Guide | Description |
|-------|-------------|
| [Production Checklist](production-checklist.md) | Every step before tagging v0.1.0 -- signing keys, secrets, verification |

## Additional Resources

| Resource | Description |
|----------|-------------|
| [CONTRIBUTING.md](../CONTRIBUTING.md) | Development setup, code style, PR guidelines |
| [MIGRATION.md](../MIGRATION.md) | Migrating from OpenClaw, LangChain, or AutoGPT |
| [SECURITY.md](../SECURITY.md) | Security policy and vulnerability reporting |
| [CHANGELOG.md](../CHANGELOG.md) | Release notes and version history |

---

## Quick Reference

### Start in 30 Seconds

```bash
export GROQ_API_KEY="your-key"
openfang init && openfang start
# Open http://127.0.0.1:4200
```

### Key Numbers

| Metric | Count |
|--------|-------|
| Crates | 14 |
| Agent templates | 30 |
| Messaging channels | 40 |
| Bundled skills | 60 |
| Built-in tools | 38 |
| LLM providers | 20 |
| Models in catalog | 51 |
| Model aliases | 23 |
| API endpoints | 76 |
| Security systems | 16 |
| Tests | 967 |

### Important Paths

| Path | Description |
|------|-------------|
| `~/.openfang/config.toml` | Main configuration file |
| `~/.openfang/data/openfang.db` | SQLite database |
| `~/.openfang/skills/` | Installed skills |
| `~/.openfang/daemon.json` | Daemon PID and port info |
| `agents/` | Agent template manifests |

### Key Environment Variables

| Variable | Provider |
|----------|----------|
| `ANTHROPIC_API_KEY` | Anthropic (Claude) |
| `OPENAI_API_KEY` | OpenAI (GPT-4o) |
| `GEMINI_API_KEY` | Google Gemini |
| `GROQ_API_KEY` | Groq (fast Llama/Mixtral) |
| `DEEPSEEK_API_KEY` | DeepSeek |
| `XAI_API_KEY` | xAI (Grok) |

Only one provider key is needed to get started. Groq offers a free tier.

```

### File: sdk\javascript\index.js
```js
/**
 * @openfang/sdk — Official JavaScript client for the OpenFang Agent OS REST API.
 *
 * Usage:
 *   const { OpenFang } = require("@openfang/sdk");
 *   const client = new OpenFang("http://localhost:3000");
 *
 *   const agent = await client.agents.create({ template: "assistant" });
 *   const reply = await client.agents.message(agent.id, "Hello!");
 *   console.log(reply);
 *
 *   // Streaming:
 *   for await (const event of client.agents.stream(agent.id, "Tell me a joke")) {
 *     process.stdout.write(event.delta || "");
 *   }
 */

"use strict";

class OpenFangError extends Error {
  constructor(message, status, body) {
    super(message);
    this.name = "OpenFangError";
    this.status = status;
    this.body = body;
  }
}

class OpenFang {
  /**
   * @param {string} baseUrl - OpenFang server URL (e.g. "http://localhost:3000")
   * @param {object} [opts]
   * @param {Record<string, string>} [opts.headers] - Extra headers for every request
   */
  constructor(baseUrl, opts) {
    this.baseUrl = baseUrl.replace(/\/+$/, "");
    this._headers = Object.assign({ "Content-Type": "application/json" }, (opts && opts.headers) || {});
    this.agents = new AgentResource(this);
    this.sessions = new SessionResource(this);
    this.workflows = new WorkflowResource(this);
    this.skills = new SkillResource(this);
    this.channels = new ChannelResource(this);
    this.tools = new ToolResource(this);
    this.models = new ModelResource(this);
    this.providers = new ProviderResource(this);
    this.memory = new MemoryResource(this);
    this.triggers = new TriggerResource(this);
    this.schedules = new ScheduleResource(this);
  }

  /** Low-level fetch wrapper. */
  async _request(method, path, body) {
    var url = this.baseUrl + path;
    var init = { method: method, headers: Object.assign({}, this._headers) };
    if (body !== undefined) {
      init.body = JSON.stringify(body);
    }
    var res = await fetch(url, init);
    if (!res.ok) {
      var text = await res.text().catch(function () { return ""; });
      throw new OpenFangError("HTTP " + res.status + ": " + text, res.status, text);
    }
    var ct = res.headers.get("content-type") || "";
    if (ct.includes("application/json")) {
      return res.json();
    }
    return res.text();
  }

  /** Low-level SSE streaming. Returns an async iterator of parsed events. */
  async *_stream(method, path, body) {
    var url = this.baseUrl + path;
    var headers = Object.assign({}, this._headers, { Accept: "text/event-stream" });
    var init = { method: method, headers: headers };
    if (body !== undefined) {
      init.body = JSON.stringify(body);
    }
    var res = await fetch(url, init);
    if (!res.ok) {
      var text = await res.text().catch(function () { return ""; });
      throw new OpenFangError("HTTP " + res.status + ": " + text, res.status, text);
    }
    var reader = res.body.getReader();
    var decoder = new TextDecoder();
    var buffer = "";
    while (true) {
      var result = await reader.read();
      if (result.done) break;
      buffer += decoder.decode(result.value, { stream: true });
      var lines = buffer.split("\n");
      buffer = lines.pop() || "";
      for (var i = 0; i < lines.length; i++) {
        var line = lines[i].trim();
        if (line.startsWith("data: ")) {
          var data = line.slice(6);
          if (data === "[DONE]") return;
          try {
            yield JSON.parse(data);
          } catch (_) {
            yield { raw: data };
          }
        }
      }
    }
  }

  /** Health check. */
  async health() {
    return this._request("GET", "/api/health");
  }

  /** Detailed health. */
  async healthDetail() {
    return this._request("GET", "/api/health/detail");
  }

  /** Server status. */
  async status() {
    return this._request("GET", "/api/status");
  }

  /** Server version. */
  async version() {
    return this._request("GET", "/api/version");
  }

  /** Prometheus metrics (text). */
  async metrics() {
    return this._request("GET", "/api/metrics");
  }

  /** Usage statistics. */
  async usage() {
    return this._request("GET", "/api/usage");
  }

  /** Config. */
  async config() {
    return this._request("GET", "/api/config");
  }
}

// ── Agent Resource ──────────────────────────────────────────────

class AgentResource {
  constructor(client) { this._c = client; }

  /** List all agents. */
  async list() {
    return this._c._request("GET", "/api/agents");
  }

  /** Get agent by ID. */
  async get(id) {
    return this._c._request("GET", "/api/agents/" + id);
  }

  /** Create (spawn) a new agent.
   * @param {object} opts - e.g. { template: "assistant", name: "My Agent" }
   */
  async create(opts) {
    return this._c._request("POST", "/api/agents", opts);
  }

  /** Delete (kill) an agent. */
  async delete(id) {
    return this._c._request("DELETE", "/api/agents/" + id);
  }

  /** Stop an agent. */
  async stop(id) {
    return this._c._request("POST", "/api/agents/" + id + "/stop");
  }

  /** Clone an agent. */
  async clone(id) {
    return this._c._request("POST", "/api/agents/" + id + "/clone");
  }

  /** Update agent. */
  async update(id, data) {
    return this._c._request("PUT", "/api/agents/" + id + "/update", data);
  }

  /** Set agent mode. */
  async setMode(id, mode) {
    return this._c._request("PUT", "/api/agents/" + id + "/mode", { mode: mode });
  }

  /** Set agent model. */
  async setModel(id, model) {
    return this._c._request("PUT", "/api/agents/" + id + "/model", { model: model });
  }

  /** Send a message and get the full response. */
  async message(id, text, opts) {
    var body = Object.assign({ message: text }, opts || {});
    return this._c._request("POST", "/api/agents/" + id + "/message", body);
  }

  /** Send a message and stream the response (async iterator of SSE events).
   * @example
   *   for await (const evt of client.agents.stream(id, "Hello")) {
   *     if (evt.type === "text_delta") process.stdout.write(evt.delta);
   *   }
   */
  async *stream(id, text, opts) {
    var body = Object.assign({ message: text }, opts || {});
    yield* this._c._stream("POST", "/api/agents/" + id + "/message/stream", body);
  }

  /** Get agent session. */
  async session(id) {
    return this._c._request("GET", "/api/agents/" + id + "/session");
  }

  /** Reset agent session. */
  async resetSession(id) {
    return this._c._request("POST", "/api/agents/" + id + "/session/reset");
  }

  /** Compact session. */
  async compactSession(id) {
    return this._c._request("POST", "/api/agents/" + id + "/session/compact");
  }

  /** List sessions for an agent. */
  async listSessions(id) {
    return this._c._request("GET", "/api/agents/" + id + "/sessions");
  }

  /** Create a new session. */
  async createSession(id, label) {
    return this._c._request("POST", "/api/agents/" + id + "/sessions", { label: label });
  }

  /** Switch to a session. */
  async switchSession(id, sessionId) {
    return this._c._request("POST", "/api/agents/" + id + "/sessions/" + sessionId + "/switch");
  }

  /** Get agent skills. */
  async getSkills(id) {
    return this._c._request("GET", "/api/agents/" + id + "/skills");
  }

  /** Set agent skills. */
  async setSkills(id, skills) {
    return this._c._request("PUT", "/api/agents/" + id + "/skills", skills);
  }

  /** Upload a file to agent. */
  async upload(id, file, filename) {
    var url = this._c.baseUrl + "/api/agents/" + id + "/upload";
    var form = new FormData();
    form.append("file", file, filename);
    var res = await fetch(url, { method: "POST", body: form });
    if (!res.ok) throw new OpenFangError("Upload failed: " + res.status, res.status);
    return res.json();
  }

  /** Update agent identity. */
  async setIdentity(id, identity) {
    return this._c._request("PATCH", "/api/agents/" + id + "/identity", identity);
  }

  /** Patch agent config. */
  async patchConfig(id, config) {
    return this._c._request("PATCH", "/api/agents/" + id + "/config", config);
  }
}

// ── Session Resource ────────────────────────────────────────────

class SessionResource {
  constructor(client) { this._c = client; }

  async list() {
    return this._c._request("GET", "/api/sessions");
  }

  async delete(id) {
    return this._c._request("DELETE", "/api/sessions/" + id);
  }

  async setLabel(id, label) {
    return this._c._request("PUT", "/api/sessions/" + id + "/label", { label: label });
  }
}

// ── Workflow Resource ───────────────────────────────────────────

class WorkflowResource {
  constructor(client) { this._c = client; }

  async list() {
    return this._c._request("GET", "/api/workflows");
  }

  async create(workflow) {
    return this._c._request("POST", "/api/workflows", workflow);
  }

  async run(id, input) {
    return this._c._request("POST", "/api/workflows/" + id + "/run", input);
  }

  async runs(id) {
    return this._c._request("GET", "/api/workflows/" + id + "/runs");
  }
}

// ── Skill Resource ──────────────────────────────────────────────

class SkillResource {
  constructor(client) { this._c = client; }

  async list() {
    return this._c._request("GET", "/api/skills");
  }

  async install(skill) {
    return this._c._request("POST", "/api/skills/install", skill);
  }

  async uninstall(skill) {
    return this._c._request("POST", "/api/skills/uninstall", skill);
  }

  async search(query) {
    return this._c._request("GET", "/api/marketplace/search?q=" + encodeURIComponent(query));
  }
}

// ── Channel Resource ────────────────────────────────────────────

class ChannelResource {
  constructor(client) { this._c = client; }

  async list() {
    return this._c._request("GET", "/api/channels");
  }

  async configure(name, config) {
    return this._c._request("POST", "/api/channels/" + name + "/configure", config);
  }

  async remove(name) {
    return this._c._request("DELETE", "/api/channels/" + name + "/configure");
  }

  async test(name) {
    return this._c._request("POST", "/api/channels/" + name + "/test");
  }
}

// ── Tool Resource ───────────────────────────────────────────────

class ToolResource {
  constructor(client) { this._c = client; }

  async list() {
    return this._c._request("GET", "/api/tools");
  }
}

// ── Model Resource ──────────────────────────────────────────────

class ModelResource {
  constructor(client) { this._c = client; }

  async list() {
    return this._c._request("GET", "/api/models");
  }

  async get(id) {
    return this._c._request("GET", "/api/models/" + id);
  }

  async aliases() {
    return this._c._request("GET", "/api/models/aliases");
  }
}

// ── Provider Resource ───────────────────────────────────────────

class ProviderResource {
  constructor(client) { this._c = client; }

  async list() {
    return this._c._request("GET", "/api/providers");
  }

  async setKey(name, key) {
    return this._c._request("POST", "/api/providers/" + name + "/key", { key: key });
  }

  async deleteKey(name) {
    return this._c._request("DELETE", "/api/providers/" + name + "/key");
  }

  async test(name) {
    return this._c._request("POST", "/api/providers/" + name + "/test");
  }
}

// ── Memory Resource ─────────────────────────────────────────────

class MemoryResource {
  constructor(client) { this._c = client; }

  async getAll(agentId) {
    return this._c._request("GET", "/api/memory/agents/" + agentId + "/kv");
  }

  async get(agentId, key) {
    return this._c._request("GET", "/api/memory/agents/" + agentId + "/kv/" + key);
  }

  async set(agentId, key, value) {
    return this._c._request("PUT", "/api/memory/agents/" + agentId + "/kv/" + key, { value: value });
  }

  async delete(agentId, key) {
    return this._c._request("DELETE", "/api/memory/agents/" + agentId + "/kv/" + key);
  }
}

// ── Trigger Resource ────────────────────────────────────────────

class TriggerResource {
  constructor(client) { this._c = client; }

  async list() {
    return this._c._request("GET", "/api/triggers");
  }

  async create(trigger) {
    return this._c._request("POST", "/api/triggers", trigger);
  }

  async update(id, trigger) {
    return this._c._request("PUT", "/api/triggers/" + id, trigger);
  }

  async delete(id) {
    return this._c._request("DELETE", "/api/triggers/" + id);
  }
}

// ── Schedule Resource ───────────────────────────────────────────

class ScheduleResource {
  constructor(client) { this._c = client; }

  async list() {
    return this._c._request("GET", "/api/schedules");
  }

  async create(schedule) {
    return this._c._request("POST", "/api/schedules", schedule);
  }

  async update(id, schedule) {
    return this._c._request("PUT", "/api/schedules/" + id, schedule);
  }

  async delete(id) {
    return this._c._request("DELETE", "/api/schedules/" + id);
  }

  async run(id) {
    return this._c._request("POST", "/api/schedules/" + id + "/run");
  }
}

// ── Exports ─────────────────────────────────────────────────────

module.exports = { OpenFang: OpenFang, OpenFangError: OpenFangError };

```

### File: sdk\javascript\package.json
```json
{
  "name": "@openfang/sdk",
  "version": "0.1.0",
  "description": "Official JavaScript/TypeScript client for the OpenFang Agent OS REST API",
  "main": "index.js",
  "types": "index.d.ts",
  "keywords": ["openfang", "agent", "ai", "llm", "sdk"],
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/openfang/openfang"
  },
  "engines": {
    "node": ">=18.0.0"
  },
  "files": ["index.js", "index.d.ts"]
}

```

### File: sdk\python\setup.py
```py
from setuptools import setup

setup(
    name="openfang",
    version="0.1.0",
    description="Official Python client for the OpenFang Agent OS REST API",
    py_modules=["openfang_sdk", "openfang_client"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

```

### File: buildopenfang.sh
```sh
#!/bin/sh

TAG=rc05_01

set -e

CPW=$(pwd)

DIR=_build
[ -d $DIR ] || { printf '%s does not exist!\n' "$DIR"; mkdir $DIR; }

date=$(date +"%Y-%m-%d %H:%M")
#ID="($(git rev-parse HEAD)) $date"
ID="$(git describe --tags)"
SHORTID=$(git rev-parse --short HEAD)

echo "$ID" > fs/opt/version

cp fs $DIR/ -r;

sed -i "s/VERSION=.*/VERSION=\"$date\"/g" $DIR/fs/opt/autoupdate.sh
sed -i "s/TAG=.*/TAG=\"$TAG\"/g" $DIR/fs/opt/autoupdate.sh
sed -i "s/ID=.*/ID=\"$SHORTID\"/g" $DIR/fs/opt/autoupdate.sh

[ "$1" = "stamp" ] && { exit 0; }

cd $DIR

BUILDROOT_VERSION=2016.02

[ -d "buildroot-$BUILDROOT_VERSION" ] || {
wget https://buildroot.org/downloads/buildroot-$BUILDROOT_VERSION.tar.gz;
tar xvf buildroot-$BUILDROOT_VERSION.tar.gz;
rm buildroot-$BUILDROOT_VERSION.tar.gz;
cd buildroot-$BUILDROOT_VERSION
patch -p1 < "$CPW"/patches/add_fp_no_fused_madd.patch
cd ..
}

cd buildroot-$BUILDROOT_VERSION

# update config files
cp "$CPW"/config/buildroot.config ./.config
cp "$CPW"/config/busybox.config ./package/busybox
cp "$CPW"/config/uClibc-ng.config ./package/uclibc

[ -d "dl" ] || { mkdir dl; }

cp ../../kernel-3.10.14.tar.xz dl/
cp ../../uboot-v2013.07.tar.xz dl/

WDIR=$CPW/$DIR/buildroot-$BUILDROOT_VERSION

# Patch buildroot if gcc >= 5
#
GCCVER=$(gcc -dumpversion | cut -d'.' -f1)
echo "GCC version: $GCCVER"
if [ "$GCCVER" -ge "5" ]; then
  cp "$CPW"/patches/automake.in.patch "$WDIR"/package/automake
  cp "$CPW"/patches/python/python2.7_gcc8__fix.patch "$WDIR"/package/python
  cp "$CPW"/patches/lzop-gcc6.patch "$WDIR"/package/lzop
fi

# copy python patches to address host-python build failing
# when host has openssl 1.1.0 headers installed
cp -f "$CPW"/patches/python/111-optional-ssl.patch "$WDIR"/package/python
cp "$CPW"/patches/python/019-force-internal-hash-if-ssl-disabled.patch "$WDIR"/package/python

# copy custom openfang packages to buildroot directory
rm -r "$WDIR"/package/ffmpeg # use updated package version instead
rm -r "$WDIR"/package/libtirpc # use updated package version instead
#rm -r "$WDIR"/package/python # use updated package version instead
#rm -r "$WDIR"/package/uclibc # use updated package version instead
cp "$CPW"/buildroot/* . -rf

make

#
# compile different versions of uboot
#
[ -f "output/images/u-boot-lzo-with-spl.bin" ] && mv output/images/u-boot-lzo-with-spl.bin output/images/u-boot-lzo-with-spl_t20_128M.bin

# change uboot configuration
sed -i "s/BR2_TARGET_UBOOT_BOARDNAME=.*/BR2_TARGET_UBOOT_BOARDNAME=\"isvp_t20_sfcnor\"/g" .config

make uboot-dirclean
make uboot

[ -f "output/images/u-boot-lzo-with-spl.bin" ] && mv output/images/u-boot-lzo-with-spl.bin output/images/u-boot-lzo-with-spl_t20_64M.bin

# end uboot compilation


# constructs release with git hash label
echo "Compressing toolchain..."
tar -c -C "$WDIR"/output/host --transform s/./mipsel-ingenic-linux-uclibc/ --checkpoint=.1000 .  | xz --best > "$CPW"/toolchain-$SHORTID.tar.xz
echo "Compressing rootfs images..."
tar -c -C "$WDIR"/output/images --transform s/./openfang-images/ --checkpoint=.1000 . | xz --best > "$CPW"/images-$SHORTID.tar.xz
echo "Build completed successfully."



```

### File: CHANGELOG.md
```md
# Changelog

All notable changes to OpenFang will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- **BREAKING:** Dashboard password hashing switched from SHA256 to Argon2id. Existing `password_hash` values in `config.toml` must be regenerated with `openfang auth hash-password`. Only affects users with `[auth] enabled = true`.

### Fixed

- Dashboard passwords were hashed with plain SHA256 (no salt), making them vulnerable to rainbow table and GPU-accelerated brute force attacks. Now uses Argon2id with random salts.

## [0.1.0] - 2026-02-24

### Added

#### Core Platform
- 15-crate Rust workspace: types, memory, runtime, kernel, api, channels, wire, cli, migrate, skills, hands, extensions, desktop, xtask
- Agent lifecycle management: spawn, list, kill, clone, mode switching (Full/Assist/Observe)
- SQLite-backed memory substrate with structured KV, semantic recall, vector embeddings
- 41 built-in tools (filesystem, web, shell, browser, scheduling, collaboration, image analysis, inter-agent, TTS, media)
- WASM sandbox with dual metering (fuel + epoch interruption with watchdog thread)
- Workflow engine with pipelines, fan-out parallelism, conditional steps, loops, and variable expansion
- Visual workflow builder with drag-and-drop node graph, 7 node types, and TOML export
- Trigger system with event pattern matching, content filters, and fire limits
- Event bus with publish/subscribe and correlation IDs
- 7 Hands packages for autonomous agent actions

#### LLM Support
- 3 native LLM drivers: Anthropic, Google Gemini, OpenAI-compatible
- 27 providers: Anthropic, Gemini, OpenAI, Groq, OpenRouter, DeepSeek, Together, Mistral, Fireworks, Cohere, Perplexity, xAI, AI21, Cerebras, SambaNova, Hugging Face, Replicate, Ollama, vLLM, LM Studio, and more
- Model catalog with 130+ built-in models, 23 aliases, tier classification
- Intelligent model routing with task complexity scoring
- Fallback driver for automatic failover between providers
- Cost estimation and metering engine with per-model pricing
- Streaming support (SSE) across all drivers

#### Token Management & Context
- Token-aware session compaction (chars/4 heuristic, triggers at 70% context capacity)
- In-loop emergency trimming at 70%/90% thresholds with summary injection
- Tool profile filtering (cuts default 41 tools to 4-10 for chat agents, saving 15-20K tokens)
- Context budget allocation for system prompt, tools, history, and response
- MAX_TOOL_RESULT_CHARS reduced from 50K to 15K to prevent tool result bloat
- Default token quota raised from 100K to 1M per hour

#### Security
- Capability-based access control with privilege escalation prevention
- Path traversal protection in all file tools
- SSRF protection blocking private IPs and cloud metadata endpoints
- Ed25519 signed agent manifests
- Merkle hash chain audit trail with tamper detection
- Information flow taint tracking
- HMAC-SHA256 mutual authentication for peer wire protocol
- API key authentication with Bearer token
- GCRA rate limiter with cost-aware token buckets
- Security headers middleware (CSP, X-Frame-Options, HSTS)
- Secret zeroization on all API key fields
- Subprocess environment isolation
- Health endpoint redaction (public minimal, auth full)
- Loop guard with SHA256-based detection and circuit breaker thresholds
- Session repair (validates and fixes orphaned tool results, empty messages)

#### Channels
- 40 channel adapters: Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Email, Teams, Mattermost, Google Chat, Webex, Feishu/Lark, LINE, Viber, Facebook Messenger, Mastodon, Bluesky, Reddit, LinkedIn, Twitch, IRC, XMPP, and 18 more
- Unified bridge with agent routing, command handling, message splitting
- Per-channel user filtering and RBAC enforcement
- Graceful shutdown, exponential backoff, secret zeroization on all adapters

#### API
- 100+ REST/WS/SSE API endpoints (axum 0.8)
- WebSocket real-time streaming with per-agent connections
- OpenAI-compatible `/v1/chat/completions` API (streaming SSE + non-streaming)
- OpenAI-compatible `/v1/models` endpoint
- WebChat embedded UI with Alpine.js
- Google A2A protocol support (agent card, task send/get/cancel)
- Prometheus text-format `/api/metrics` endpoint for monitoring
- Multi-session management: list, create, switch, label sessions per agent
- Usage analytics: summary, by-model, daily breakdown
- Config hot-reload via polling (30-second interval, no restart required)

#### Web UI
- Chat message search with Ctrl+F, real-time filtering, text highlighting
- Voice input with hold-to-record mic button (WebM/Opus codec)
- TTS audio playback inline in tool cards
- Browser screenshot rendering in chat (inline images)
- Canvas rendering with iframe sandbox and CSP support
- Session switcher dropdown in chat header
- 6-step first-run setup wizard with provider API key help (12 providers)
- Skill marketplace with 4 tabs (Installed, ClawHub, MCP Servers, Quick Start)
- Copy-to-clipboard on messages, message timestamps
- Visual workflow builder with drag-and-drop canvas

#### Client SDKs
- JavaScript SDK (`@openfang/sdk`): full REST API client with streaming, TypeScript declarations
- Python client SDK (`openfang_client`): zero-dependency stdlib client with SSE streaming
- Python agent SDK (`openfang_sdk`): decorator-based framework for writing Python agents
- Usage examples for both languages (basic + streaming)

#### CLI
- 14+ subcommands: init, start, agent, workflow, trigger, migrate, skill, channel, config, chat, status, doctor, dashboard, mcp
- Daemon auto-detection via PID file
- Shell completion generation (bash, zsh, fish, PowerShell)
- MCP server mode for IDE integration

#### Skills Ecosystem
- 60 bundled skills across 14 categories
- Skill registry with TOML manifests
- 4 runtimes: Python, Node.js, WASM, PromptOnly
- FangHub marketplace with search/install
- ClawHub client for OpenClaw skill compatibility
- SKILL.md parser with auto-conversion
- SHA256 checksum verification
- Prompt injection scanning on skill content

#### Desktop App
- Tauri 2.0 native desktop app
- System tray with status and quick actions
- Single-instance enforcement
- Hide-to-tray on close
- Updated CSP for media, frame, and blob sources

#### Session Management
- LLM-based session compaction with token-aware triggers
- Multi-session per agent with named labels
- Session switching via API and UI
- Cross-channel canonical sessions
- Extended chat commands: `/new`, `/compact`, `/model`, `/stop`, `/usage`, `/think`

#### Image Support
- `ContentBlock::Image` with base64 inline data
- Media type validation (png, jpeg, gif, webp only)
- 5MB size limit enforcement
- Mapped to all 3 native LLM drivers

#### Usage Tracking
- Per-response cost estimation with model-aware pricing
- Usage footer in WebSocket responses and WebChat UI
- Usage events persisted to SQLite
- Quota enforcement with hourly windows

#### Interoperability
- OpenClaw migration engine (YAML/JSON5 to TOML)
- MCP client (JSON-RPC 2.0 over stdio/SSE, tool namespacing)
- MCP server (exposes OpenFang tools via MCP protocol)
- A2A protocol client and server
- Tool name compatibility mappings (21 OpenClaw tool names)

#### Infrastructure
- Multi-stage Dockerfile (debian:bookworm-slim runtime)
- docker-compose.yml with volume persistence
- GitHub Actions CI (check, test, clippy, format)
- GitHub Actions release (multi-platform, GHCR push, SHA256 checksums)
- Cross-platform install script (curl/irm one-liner)
- systemd service file for Linux deployment

#### Multi-User
- RBAC with Owner/Admin/User/Viewer roles
- Channel identity resolution
- Per-user authorization checks
- Device pairing and approval system

#### Production Readiness
- 1731+ tests across 15 crates, 0 failures
- Cross-platform support (Linux, macOS, Windows)
- Graceful shutdown with signal handling (SIGINT/SIGTERM on Unix, Ctrl+C on Windows)
- Daemon PID file with stale process detection
- Release profile with LTO, single codegen unit, symbol stripping
- Prometheus metrics for monitoring
- Config hot-reload without restart

[0.1.0]: https://github.com/RightNow-AI/openfang/releases/tag/v0.1.0

```

### File: CLAUDE.md
```md
# OpenFang — Agent Instructions

## Project Overview
OpenFang is an open-source Agent Operating System written in Rust (14 crates).
- Config: `~/.openfang/config.toml`
- Default API: `http://127.0.0.1:4200`
- CLI binary: `target/release/openfang.exe` (or `target/debug/openfang.exe`)

## Build & Verify Workflow
After every feature implementation, run ALL THREE checks:
```bash
cargo build --workspace --lib          # Must compile (use --lib if exe is locked)
cargo test --workspace                 # All tests must pass (currently 1744+)
cargo clippy --workspace --all-targets -- -D warnings  # Zero warnings
```

## MANDATORY: Live Integration Testing
**After implementing any new endpoint, feature, or wiring change, you MUST run live integration tests.** Unit tests alone are not enough — they can pass while the feature is actually dead code. Live tests catch:
- Missing route registrations in server.rs
- Config fields not being deserialized from TOML
- Type mismatches between kernel and API layers
- Endpoints that compile but return wrong/empty data

### How to Run Live Integration Tests

#### Step 1: Stop any running daemon
```bash
tasklist | grep -i openfang
taskkill //PID <pid> //F
# Wait 2-3 seconds for port to release
sleep 3
```

#### Step 2: Build fresh release binary
```bash
cargo build --release -p openfang-cli
```

#### Step 3: Start daemon with required API keys
```bash
GROQ_API_KEY=<key> target/release/openfang.exe start &
sleep 6  # Wait for full boot
curl -s http://127.0.0.1:4200/api/health  # Verify it's up
```
The daemon command is `start` (not `daemon`).

#### Step 4: Test every new endpoint
```bash
# GET endpoints — verify they return real data, not empty/null
curl -s http://127.0.0.1:4200/api/<new-endpoint>

# POST/PUT endpoints — send real payloads
curl -s -X POST http://127.0.0.1:4200/api/<endpoint> \
  -H "Content-Type: application/json" \
  -d '{"field": "value"}'

# Verify write endpoints persist — read back after writing
curl -s -X PUT http://127.0.0.1:4200/api/<endpoint> -d '...'
curl -s http://127.0.0.1:4200/api/<endpoint>  # Should reflect the update
```

#### Step 5: Test real LLM integration
```bash
# Get an agent ID
curl -s http://127.0.0.1:4200/api/agents | python3 -c "import sys,json; print(json.load(sys.stdin)[0]['id'])"

# Send a real message (triggers actual LLM call to Groq/OpenAI)
curl -s -X POST "http://127.0.0.1:4200/api/agents/<id>/message" \
  -H "Content-Type: application/json" \
  -d '{"message": "Say hello in 5 words."}'
```

#### Step 6: Verify side effects
After an LLM call, verify that any metering/cost/usage tracking updated:
```bash
curl -s http://127.0.0.1:4200/api/budget       # Cost should have increased
curl -s http://127.0.0.1:4200/api/budget/agents  # Per-agent spend should show
```

#### Step 7: Verify dashboard HTML
```bash
# Check that new UI components exist in the served HTML
curl -s http://127.0.0.1:4200/ | grep -c "newComponentName"
# Should return > 0
```

#### Step 8: Cleanup
```bash
tasklist | grep -i openfang
taskkill //PID <pid> //F
```

### Key API Endpoints for Testing
| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/health` | GET | Basic health check |
| `/api/agents` | GET | List all agents |
| `/api/agents/{id}/message` | POST | Send message (triggers LLM) |
| `/api/budget` | GET/PUT | Global budget status/update |
| `/api/budget/agents` | GET | Per-agent cost ranking |
| `/api/budget/agents/{id}` | GET | Single agent budget detail |
| `/api/network/status` | GET | OFP network status |
| `/api/peers` | GET | Connected OFP peers |
| `/api/a2a/agents` | GET | External A2A agents |
| `/api/a2a/discover` | POST | Discover A2A agent at URL |
| `/api/a2a/send` | POST | Send task to external A2A agent |
| `/api/a2a/tasks/{id}/status` | GET | Check external A2A task status |

## Architecture Notes
- **Don't touch `openfang-cli`** — user is actively building the interactive CLI
- `KernelHandle` trait avoids circular deps between runtime and kernel
- `AppState` in `server.rs` bridges kernel to API routes
- New routes must be registered in `server.rs` router AND implemented in `routes.rs`
- Dashboard is Alpine.js SPA in `static/index_body.html` — new tabs need both HTML and JS data/methods
- Config fields need: struct field + `#[serde(default)]` + Default impl entry + Serialize/Deserialize derives

## Common Gotchas
- `openfang.exe` may be locked if daemon is running — use `--lib` flag or kill daemon first
- `PeerRegistry` is `Option<PeerRegistry>` on kernel but `Option<Arc<PeerRegistry>>` on `AppState` — wrap with `.as_ref().map(|r| Arc::new(r.clone()))`
- Config fields added to `KernelConfig` struct MUST also be added to the `Default` impl or build fails
- `AgentLoopResult` field is `.response` not `.response_text`
- CLI command to start daemon is `start` not `daemon`
- On Windows: use `taskkill //PID <pid> //F` (double slashes in MSYS2/Git Bash)

```

### File: CONTRIBUTING.md
```md
# Contributing to OpenFang

Thank you for your interest in contributing to OpenFang. This guide covers everything you need to get started, from setting up your development environment to submitting pull requests.

## Table of Contents

- [Development Environment](#development-environment)
- [Building and Testing](#building-and-testing)
- [Code Style](#code-style)
- [Architecture Overview](#architecture-overview)
- [How to Add a New Agent Template](#how-to-add-a-new-agent-template)
- [How to Add a New Channel Adapter](#how-to-add-a-new-channel-adapter)
- [How to Add a New Tool](#how-to-add-a-new-tool)
- [Pull Request Process](#pull-request-process)
- [Code of Conduct](#code-of-conduct)

---

## Development Environment

### Prerequisites

- **Rust 1.75+** (install via [rustup](https://rustup.rs/))
- **Git**
- **Python 3.8+** (optional, for Python runtime and skills)
- A supported LLM API key (Anthropic, OpenAI, Groq, etc.) for end-to-end testing

### Clone and Build

```bash
git clone https://github.com/RightNow-AI/openfang.git
cd openfang
cargo build
```

The first build takes a few minutes because it compiles SQLite (bundled) and Wasmtime. Subsequent builds are incremental.

### Environment Variables

For running integration tests that hit a real LLM, set at least one provider key:

```bash
export GROQ_API_KEY=gsk_...          # Recommended for fast, free-tier testing
export ANTHROPIC_API_KEY=sk-ant-...  # For Anthropic-specific tests
```

Tests that require a real LLM key will skip gracefully if the env var is absent.

---

## Building and Testing

### Build the Entire Workspace

```bash
cargo build --workspace
```

### Fast Release Build (for development)

The default `--release` profile uses full LTO and single-codegen-unit, which produces the smallest/fastest binary but is slow to compile. For iterating locally, use the `release-fast` profile instead:

```bash
cargo build --profile release-fast -p openfang-cli
```

This cuts link time significantly (thin LTO, 8 codegen units, `opt-level=2`) while still producing a binary fast enough to run integration tests against. Use `--release` only for final binaries or CI.

### Run All Tests

```bash
cargo test --workspace
```

The test suite is currently 1,744+ tests. All must pass before merging.

### Run Tests for a Single Crate

```bash
cargo test -p openfang-kernel
cargo test -p openfang-runtime
cargo test -p openfang-memory
```

### Check for Clippy Warnings

```bash
cargo clippy --workspace --all-targets -- -D warnings
```

The CI pipeline enforces zero clippy warnings.

### Format Code

```bash
cargo fmt --all
```

Always run `cargo fmt` before committing. CI will reject unformatted code.

### Run the Doctor Check

After building, verify your local setup:

```bash
cargo run -- doctor
```

---

## Code Style

- **Formatting**: Use `rustfmt` with default settings. Run `cargo fmt --all` before every commit.
- **Linting**: `cargo clippy --workspace -- -D warnings` must pass with zero warnings.
- **Documentation**: All public types and functions must have doc comments (`///`).
- **Error Handling**: Use `thiserror` for error types. Avoid `unwrap()` in library code; prefer `?` propagation.
- **Naming**:
  - Types: `PascalCase` (e.g., `OpenFangKernel`, `AgentManifest`)
  - Functions/methods: `snake_case`
  - Constants: `SCREAMING_SNAKE_CASE`
  - Crate names: `openfang-{name}` (kebab-case)
- **Dependencies**: Workspace dependencies are declared in the root `Cargo.toml`. Prefer reusing workspace deps over adding new ones. If you need a new dependency, justify it in the PR.
- **Testing**: Every new feature must include tests. Use `tempfile::TempDir` for filesystem isolation and random port binding for network tests.
- **Serde**: All config structs use `#[serde(default)]` for forward compatibility with partial TOML.

---

## Architecture Overview

OpenFang is organized as a Cargo workspace with 14 crates:

| Crate | Role |
|-------|------|
| `openfang-types` | Shared type definitions, taint tracking, manifest signing (Ed25519), model catalog, MCP/A2A config types |
| `openfang-memory` | SQLite-backed memory substrate with vector embeddings, usage tracking, canonical sessions, JSONL mirroring |
| `openfang-runtime` | Agent loop, 3 LLM drivers (Anthropic/Gemini/OpenAI-compat), 38 built-in tools, WASM sandbox, MCP client/server, A2A protocol |
| `openfang-hands` | Hands system (curated autonomous capability packages), 7 bundled hands |
| `openfang-extensions` | Integration registry (25 bundled MCP templates), AES-256-GCM credential vault, OAuth2 PKCE |
| `openfang-kernel` | Assembles all subsystems: workflow engine, RBAC auth, heartbeat monitor, cron scheduler, config hot-reload |
| `openfang-api` | REST/WS/SSE API (Axum 0.8), 76 endpoints, 14-page SPA dashboard, OpenAI-compatible `/v1/chat/completions` |
| `openfang-channels` | 40 channel adapters (Telegram, Discord, Slack, WhatsApp, and 36 more), formatter, rate limiter |
| `openfang-wire` | OFP (OpenFang Protocol): TCP P2P networking with HMAC-SHA256 mutual authentication |
| `openfang-cli` | Clap CLI with daemon auto-detect (HTTP mode vs. in-process fallback), MCP server |
| `openfang-migrate` | Migration engine for importing from OpenClaw (and future frameworks) |
| `openfang-skills` | Skill system: 60 bundled skills, FangHub marketplace, OpenClaw compatibility, prompt injection scanning |
| `openfang-desktop` | Tauri 2.0 native desktop app (WebView + system tray + single-instance + notifications) |
| `xtask` | Build automation tasks |

### Key Architectural Patterns

- **`KernelHandle` trait**: Defined in `openfang-runtime`, implemented on `OpenFangKernel` in `openfang-kernel`. This avoids circular crate dependencies while enabling inter-agent tools.
- **Shared memory**: A fixed UUID (`AgentId(Uuid::from_bytes([0..0, 0x01]))`) provides a cross-agent KV namespace.
- **Daemon detection**: The CLI checks `~/.openfang/daemon.json` and pings the health endpoint. If a daemon is running, commands use HTTP; otherwise, they boot an in-process kernel.
- **Capability-based security**: Every agent operation is checked against the agent's granted capabilities before execution.

---

## How to Add a New Agent Template

Agent templates live in the `agents/` directory. Each template is a folder containing an `agent.toml` manifest.

### Steps

1. Create a new directory under `agents/`:

```
agents/my-agent/agent.toml
```

2. Write the manifest:

```toml
name = "my-agent"
version = "0.1.0"
description = "A brief description of what this agent does."
author = "openfang"
module = "builtin:chat"
tags = ["category"]

[model]
provider = "groq"
model = "llama-3.3-70b-versatile"

[resources]
max_llm_tokens_per_hour = 100000

[capabilities]
tools = ["file_read", "file_list", "web_fetch"]
memory_read = ["*"]
memory_write = ["self.*"]
agent_spawn = false
```

3. Include a system prompt if needed by adding it to the `[model]` section:

```toml
[model]
provider = "anthropic"
model = "claude-sonnet-4-20250514"
system_prompt = """
You are a specialized agent that...
"""
```

4. Test by spawning:

```bash
openfang agent spawn agents/my-agent/agent.toml
```

5. Submit a PR with the new template.

---

## How to Add a New Channel Adapter

Channel adapters live in `crates/openfang-channels/src/`. Each adapter implements the `ChannelAdapter` trait.

### Steps

1. Create a new file: `crates/openfang-channels/src/myplatform.rs`

2. Implement the `ChannelAdapter` trait (defined in `types.rs`):

```rust
use crate::types::{ChannelAdapter, ChannelMessage, ChannelType};
use async_trait::async_trait;

pub struct MyPlatformAdapter {
    // token, client, config fields
}

#[async_trait]
impl ChannelAdapter for MyPlatformAdapter {
    fn channel_type(&self) -> ChannelType {
        ChannelType::Custom("myplatform".to_string())
    }

    async fn start(&mut self) -> Result<(), Box<dyn std::error::Error>> {
        // Start polling/listening for messages
        Ok(())
    }

    async fn send(&self, channel_id: &str, content: &str) -> Result<(), Box<dyn std::error::Error>> {
        // Send a message back to the platform
        Ok(())
    }

    async fn stop(&mut self) {
        // Clean shutdown
    }
}
```

3. Register the module in `crates/openfang-channels/src/lib.rs`:

```rust
pub mod myplatform;
```

4. Wire it up in the channel bridge (`crates/openfang-api/src/channel_bridge.rs`) so the daemon starts it alongside other adapters.

5. Add configuration support in `openfang-types` config structs (add a `[channels.myplatform]` section).

6. Add CLI setup wizard instructions in `crates/openfang-cli/src/main.rs` under `cmd_channel_setup`.

7. Write tests and submit a PR.

---

## How to Add a New Tool

Built-in tools are defined in `crates/openfang-runtime/src/tool_runner.rs`.

### Steps

1. Add the tool implementation function:

```rust
async fn tool_my_tool(input: &serde_json::Value) -> Result<String, String> {
    let param = input["param"]
        .as_str()
        .ok_or("Missing 'param' field")?;

    // Tool logic here
    Ok(format!("Result: {param}"))
}
```

2. Register it in the `execute_tool` match block:

```rust
"my_tool" => tool_my_tool(input).await,
```

3. Add the tool definition to `builtin_tool_definitions()`:

```rust
ToolDefinition {
    name: "my_tool".to_string(),
    description: "Description shown to the LLM.".to_string(),
    input_schema: serde_json::json!({
        "type": "object",
        "properties": {
            "param": {
                "type": "string",
                "description": "The parameter description"
            }
        },
        "required": ["param"]
    }),
},
```

4. Agents that need the tool must list it in their manifest:

```toml
[capabilities]
tools = ["my_tool"]
```

5. Write tests for the tool function.

6. If the tool requires kernel access (e.g., inter-agent communication), accept `Option<&Arc<dyn KernelHandle>>` and handle the `None` case gracefully.

---

## Pull Request Process

1. **Fork and branch**: Create a feature branch from `main`. Use descriptive names like `feat/add-matrix-adapter` or `fix/session-restore-crash`.

2. **Make your changes**: Follow the code style guidelines above.

3. **Test thoroughly**:
   - `cargo test --workspace` must pass (all 1,744+ tests).
   - `cargo clippy --workspace --all-targets -- -D warnings` must produce zero warnings.
   - `cargo fmt --all --check` must produce no diff.

4. **Write a clear PR description**: Explain what changed and why. Include before/after examples if applicable.

5. **One concern per PR**: Keep PRs focused. A single PR should address one feature, one bug fix, or one refactor -- not all three.

6. **Review process**: At least one maintainer must approve before merge. Address review feedback promptly.

7. **CI must pass**: All automated checks must be green before merge.

### Commit Messages

Use clear, imperative-mood messages:

```
Add Matrix channel adapter with E2EE support
Fix session restore crash on kernel reboot
Refactor capability manager to use DashMap
```

---

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). By participating, you agree to uphold a welcoming, inclusive, and harassment-free environment for everyone.

Please report unacceptable behavior to the maintainers.

---

## Questions?

- Open a [GitHub Discussion](https://github.com/RightNow-AI/openfang/discussions) for questions.
- Open a [GitHub Issue](https://github.com/RightNow-AI/openfang/issues) for bugs or feature requests.
- Check the [docs/](docs/) directory for detailed guides on specific topics.

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
