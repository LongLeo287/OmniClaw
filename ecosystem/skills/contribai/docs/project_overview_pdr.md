# ContribAI — Project Overview & PDR

**Version:** 5.2.0 | **License:** AGPL-3.0 + Commons Clause | **Status:** Active Development

---

## Executive Summary

**ContribAI** is an autonomous AI agent written in Rust that discovers open source repositories on GitHub, analyzes them for improvement opportunities, generates high-quality code fixes, and submits Pull Requests — all without human intervention. It bridges the gap between maintainer bandwidth constraints and contributor availability by delivering production-grade contributions at scale.

**v5.2.0** is the full Rust rewrite: ~4.5 MB single binary, ~5ms startup, 22 CLI commands, interactive TUI, and real notification delivery.

---

## Product Definition

### Target Users

1. **Open Source Maintainers** — Reduce issue backlog via autonomous quality contributions
2. **Project Leaders** — Accelerate project evolution with AI-powered improvements
3. **Enterprise Operators** — Deploy in-house for internal projects or customer repos
4. **AI/ML Researchers** — Study autonomous contribution patterns, agent design, code generation quality

### Core Value Proposition

Autonomous, safe, high-quality code contributions that:
- **Reduce manual labor** — No human reviews needed for obvious improvements
- **Increase contribution velocity** — 10-15 PRs per day per instance
- **Maintain quality standards** — 7-check gate prevents low-quality submissions
- **Respect maintainer intent** — Learns from PR outcomes, avoids rejected patterns
- **Operate safely** — Rate limiting, AI policy detection, duplicate prevention
- **Single binary** — No runtime required, ~4.5 MB stripped binary

### Key Features

#### Core Pipeline
- **Smart Discovery** — GitHub Search API (REST + GraphQL), multi-language
- **Multi-Strategy Analysis** — 7 analyzers + 17 progressive skills (security, quality, docs, UI/UX, perf, refactor, framework)
- **LLM-Powered Generation** — Multi-provider with self-review and quality scoring
- **Autonomous PR Creation** — Fork, branch, commit (DCO), PR — all automated

#### Hunt Mode
- Autonomous hunting across GitHub (configurable rounds + delays)
- Cross-file pattern detection and bulk fixes
- Duplicate PR prevention via title similarity
- Post-PR CI monitoring with auto-close on failures

#### Interactive TUI (v5.2.0 NEW)
- **ratatui** 4-tab terminal browser: Dashboard / PRs / Repos / Actions
- Browse PR history, per-repo merge rates, run commands
- Keyboard navigation: Tab/1-4 switch tabs · j/k scroll · ? help · q quit

#### Resilience & Safety
- AI policy detection (respects contributor bans)
- CLA/DCO auto-signing
- Deep validation reduces false positives
- Rate limiting (max 2 findings per repo)
- API retry with exponential backoff
- Code-only modifications (skips docs/config/meta files)

#### PR Patrol
- Reviews open PRs for maintainer feedback
- Bot-aware feedback classification (11+ known bots filtered)
- Auto-generates fixes based on review feedback
- DCO auto-signoff on commits

#### Multi-LLM Support
- **Primary:** Google Gemini (Flash, Pro)
- **Alternates:** OpenAI, Anthropic, Ollama, Google Vertex AI
- Task routing (performance/balanced/economy strategies)
- Token-aware context budgeting (30k token limit)

#### Agent Architecture
- Sub-agent registry with 5 built-in agents (Analyzer, Generator, Patrol, Compliance, Issue)
- Event bus (15 typed events, JSONL logging)
- Working memory (per-repo analysis context, 72h TTL)
- Context compression (LLM-driven + 3-tier truncation)

#### Platform Features
- **Web Dashboard** — axum REST API + static dashboard (`:8787`)
- **Scheduler** — Tokio cron-based automation
- **Templates** — Built-in contribution templates (YAML-based)
- **Profiles** — Named presets (security-focused, docs-focused, full-scan, gentle)
- **Plugins** — Trait-based system for custom analyzers/generators
- **Webhooks** — GitHub webhook receiver (HMAC-SHA256 verified)
- **Docker** — Full docker-compose setup (dashboard, scheduler, runner)

#### MCP Server (21 tools)
- 21 tools exposed to Claude Desktop + Antigravity IDE via stdio JSON-RPC
- GitHub read/write, PR management, safety checks, maintenance utilities

---

## Technical Requirements

### Core Requirements

| Requirement | Details |
|------------|---------|
| **Rust** | 1.75+ (2021 edition) |
| **GitHub** | Token (PAT) with `repo` + `workflow` scopes |
| **LLM API** | Gemini / OpenAI / Anthropic / Vertex AI API key |
| **Database** | SQLite (bundled via rusqlite — no install needed) |
| **OS** | Linux, macOS, Windows |

### Core Dependencies (Rust)

| Crate | Purpose |
|-------|---------|
| `tokio` | Async runtime (full features) |
| `reqwest` | HTTP client (async, rustls) |
| `axum` | Web framework + dashboard |
| `rusqlite` | SQLite (bundled) |
| `clap` | CLI (derive macros, 22 commands) |
| `ratatui` + `crossterm` | Interactive TUI |
| `serde` / `serde_json` / `serde_yaml` | Serialization |
| `tracing` | Structured logging |
| `anyhow` / `thiserror` | Error handling |
| `tree-sitter` | AST parsing (8 languages) |
| `hmac` + `sha2` | Webhook HMAC verification |

### Optional

- **Docker** — For sandbox code validation (`sandbox.enabled = true`)
- **Redis** — For distributed rate limiting (future)
- **PostgreSQL** — For multi-instance deployments (future)

---

## Functional Requirements

### Discovery (FR-D)

| ID | Requirement | Implementation |
|----|-------------|---------------|
| FR-D.1 | Search GitHub by language + star range | GitHub Search API (REST + GraphQL) |
| FR-D.2 | Filter inactive repos | Skip if last commit > 6 months ago |
| FR-D.3 | Detect contribution bans | Parse CONTRIBUTING.md for AI policy |
| FR-D.4 | Prevent duplicate analysis | SQLite `analyzed_repos` table |
| FR-D.5 | Support multiple languages | Language detection via file extensions |
| FR-D.6 | Issue-driven discovery | Fetch + solve open GitHub issues |

### Analysis (FR-A)

| ID | Requirement | Implementation |
|----|-------------|---------------|
| FR-A.1 | Detect security issues | Security analyzer + 17 skills |
| FR-A.2 | Detect code quality issues | Code quality analyzer + rules |
| FR-A.3 | Detect documentation gaps | Doc analyzer |
| FR-A.4 | Detect UI/UX issues | UI/UX analyzer |
| FR-A.5 | Detect performance problems | Performance analyzer |
| FR-A.6 | Framework-specific detection | Auto-detect Django/Flask/FastAPI/React/etc. |
| FR-A.7 | Progressive skill loading | 17 skills on-demand by language |
| FR-A.8 | Deep validation | LLM validates findings against file context |
| FR-A.9 | AST parsing | tree-sitter (8 languages) |
| FR-A.10 | File importance ranking | PageRank via import graph |

### Generation (FR-G)

| ID | Requirement | Implementation |
|----|-------------|---------------|
| FR-G.1 | Generate code fixes | LLM-powered generation with retry |
| FR-G.2 | Self-review generated code | LLM reviews own fixes before submission |
| FR-G.3 | Quality scoring | 7-check gate (min 0.6/1.0 score) |
| FR-G.4 | Syntax validation | Balanced brackets, no-op detection |
| FR-G.5 | Multi-language generation | Python, JS, Go, Rust, Java, etc. |
| FR-G.6 | Cross-file fixes | Detect same pattern across files, fix all |

### PR Management (FR-PR)

| ID | Requirement | Implementation |
|----|-------------|---------------|
| FR-PR.1 | Auto-fork repo | GitHub API fork operation |
| FR-PR.2 | Create feature branch | Git branch creation |
| FR-PR.3 | Commit with DCO signoff | Auto-append `Signed-off-by` |
| FR-PR.4 | Create PR with context | PR title + detailed body |
| FR-PR.5 | Auto-sign CLAs | Detect CLA service, auto-sign |
| FR-PR.6 | Monitor CI | Check PR status, auto-close if CI fails |
| FR-PR.7 | Monitor reviews | Track maintainer feedback, auto-fix |
| FR-PR.8 | Duplicate prevention | Title similarity matching (>90% = duplicate) |

### Interactive CLI (FR-I) — v5.2.0

| ID | Requirement | Implementation |
|----|-------------|---------------|
| FR-I.1 | 22-command CLI | clap derive + dialoguer menu |
| FR-I.2 | Interactive TUI | ratatui 4-tab browser |
| FR-I.3 | Setup wizard | `contribai init` with dialoguer |
| FR-I.4 | Config editor | `config-get/set/list` YAML editor |
| FR-I.5 | Auth status | `contribai login` — check all providers |
| FR-I.6 | Notification test | `contribai notify-test` — real HTTP |

### Configuration (FR-C)

| ID | Requirement | Implementation |
|----|-------------|---------------|
| FR-C.1 | Load from YAML | `config.yaml` with serde_yaml |
| FR-C.2 | Environment overrides | Env vars override YAML values |
| FR-C.3 | Profile presets | Named configs (security-focused, etc.) |
| FR-C.4 | CLI config editor | `config-get/set/list` commands |

---

## Non-Functional Requirements

### Performance (NFR-P)

| Requirement | Python v4 | Rust v5.1 Target |
|---|---|---|
| Startup time | ~800ms | ~5ms |
| Single repo analysis | < 2 min | < 30s |
| Memory footprint | ~120 MB | ~8 MB |
| Dashboard API latency | < 500ms (p95) | < 50ms (p95) |
| Binary size | needs runtime | ~4.5 MB stripped |

### Reliability (NFR-R)

| Requirement | Target |
|---|---|
| Uptime (dashboard) | 99.5% (self-hosted) |
| CI pass rate (tests) | 100% (cargo test: 335 tests) |
| Recovery time (crash) | < 5 minutes (auto-restart) |

### Security (NFR-S)

| Requirement | Implementation |
|---|---|
| API key handling | Never log, use env vars only |
| Code execution | Docker sandbox or local fallback |
| Webhook verification | HMAC-SHA256 (`X-Hub-Signature-256`) |
| API auth | Constant-time key comparison (timing-safe) |
| Payload size limit | 10 MB max on webhook endpoint |
| Dependency audits | `cargo audit` in CI |

### Scalability (NFR-Sc)

| Requirement | Implementation |
|---|---|
| Multi-instance deployment | Docker + shared SQLite → future PostgreSQL |
| Parallel repo processing | Tokio + Semaphore(3) |
| Async-first | All I/O via tokio async |
| Token budgeting | 30k token limit per analysis |

---

## Success Metrics

### Operational Metrics

| Metric | Target | Measurement |
|---|---|---|
| **Repos analyzed per day** | 50+ | `run_log` table |
| **PRs created per day** | 10-15 | `submitted_prs` table |
| **PR success rate** | > 80% | merged/total |
| **Avg time-to-merge** | < 7 days | `time_to_close_hours` |
| **False positive rate** | < 5% | Manual audit |

### Quality Metrics

| Metric | Target | Measurement |
|---|---|---|
| **Code review comments** | < 2 per PR | GitHub API |
| **Rejection rate** | < 20% | PR close reason |
| **Quality score avg** | > 0.75/1.0 | Scorer output |
| **Test coverage (Rust)** | 335+ tests | `cargo test` |

---

## Constraints & Assumptions

### Constraints

1. **GitHub API Rate Limits** — 5,000 requests/hour (authenticated)
2. **LLM API Costs** — Pay-as-you-go; configurable daily budget
3. **Code Size** — Skips files > 50 KB
4. **License** — AGPL-3.0 + Commons Clause (open source, non-commercial)
5. **Rust MSRV** — 1.75+ required

### Assumptions

1. Users have valid GitHub + LLM API credentials
2. Target repos have standard structure (README, src dir, tests)
3. Maintainers read PRs within 7 days
4. AI-generated contributions are acceptable in target community
5. Network connectivity is stable (retries handle transient failures)

---

## Roadmap Alignment

### Recent Releases

- **v5.0.0** (2026-03-31) — Full Rust rewrite, 21 CLI commands, 323 tests
- **v5.2.0** (2026-04-01) — Interactive TUI, real notifications, 22 commands, 335 tests
- **v4.1.0** (2026-03-28) — Python legacy: Antigravity MCP, clean PR titles _(archived)_

### Planned (v5.2.0+)

- PostgreSQL migration layer
- Redis distributed rate limiting
- Prometheus + OpenTelemetry
- Kubernetes Helm charts
- Multi-turn LLM conversations for complex reasoning

---

## Dependencies & Integrations

### External Services

- **GitHub API** — Repo discovery, file access, PR creation (REST + GraphQL)
- **LLM APIs** — Gemini, OpenAI, Anthropic, Vertex AI
- **Slack/Discord/Telegram** — Real HTTP notifications
- **CLA Services** — CLA-Assistant, EasyCLA (auto-sign)

### Internal Integrations

- **Event Bus** — 15 typed events, JSONL logging
- **Memory System** — SQLite (7 tables), 72h TTL working memory
- **MCP Server** — 21 tools for Claude Desktop
- **Web Dashboard** — axum REST API

---

## Glossary

| Term | Definition |
|------|-----------|
| **Hunt** | Autonomous multi-round repo search + contribution cycle |
| **Contribution** | A proposed code change (generated fix for a finding) |
| **Finding** | An issue detected by an analyzer (security bug, missing docstring, etc.) |
| **Skill** | Reusable knowledge module loaded on-demand (e.g., Django security patterns) |
| **Middleware** | Cross-cutting concern handler (rate limiting, validation, retry, DCO, quality gate) |
| **Sub-Agent** | Specialized executor (Analyzer, Generator, Patrol, Compliance, Issue) |
| **Profile** | Named preset configuration (security-focused, docs-focused, etc.) |
| **PR Patrol** | Automated monitoring + fixing of open PRs based on feedback |
| **TUI** | ratatui terminal UI — interactive 4-tab browser |
| **CLA** | Contributor License Agreement (auto-signed) |
| **DCO** | Developer Certificate of Origin (auto-appended) |

---

## Document Metadata

- **Created:** 2026-03-28
- **Last Updated:** 2026-04-01
- **Version:** 5.2.0 (Rust — Interactive TUI + full CLI parity)
- **Related:** README.md, AGENTS.md, docs/ARCHITECTURE.md, docs/system-architecture.md
