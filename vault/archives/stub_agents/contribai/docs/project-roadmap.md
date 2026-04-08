# Project Roadmap

**Current Version:** 5.2.0 | **Release Date:** 2026-04-01 | **Status:** Active Development

---

## Executive Summary

ContribAI is a mature autonomous AI contribution system. Originally built in Python (v0.x–v4.0), it was rewritten in Rust (v5.0.0) for performance, safety, and new capabilities like tree-sitter AST parsing and PageRank file ranking. v5.2.0 adds an interactive TUI, real notification delivery, and full 22-command CLI parity. The roadmap focuses on leveraging Rust's advantages for production maturity and ecosystem expansion.

---

## Release Timeline

### v0.x Series (2026-03-17 to 2026-03-20) — Foundation Building (Python)

| Version | Date | Milestone | Status |
|---------|------|-----------|--------|
| **v0.1** | 2026-03-17 | Core pipeline (discovery → analysis → generation → PR) | ✓ Complete |
| **v0.4** | 2026-03-18 | Web dashboard + REST API | ✓ Complete |
| **v0.5** | 2026-03-18 | Scheduler + cron automation | ✓ Complete |
| **v0.7** | 2026-03-19 | Multi-LLM support (Gemini, OpenAI, Anthropic, Ollama) | ✓ Complete |
| **v0.11** | 2026-03-20 | Hunt Mode (autonomous multi-round hunting) | ✓ Complete |

---

### v1.x Series (2026-03-20) — Quality & Safety (Python)

| Version | Date | Milestone | Status |
|---------|------|-----------|--------|
| **v1.0** | 2026-03-20 | Official release; quality improvements | ✓ Complete |
| **v1.5** | 2026-03-20 | CLA/DCO handling; compliance automation | ✓ Complete |
| **v1.8** | 2026-03-20 | Cross-file pattern detection + bulk fixes | ✓ Complete |

---

### v2.x Series (2026-03-22 to 2026-03-26) — Learning & Resilience (Python)

| Version | Date | Milestone | Status |
|---------|------|-----------|--------|
| **v2.0** | 2026-03-22 | Safety gates (quality scorer, duplicate prevention) | ✓ Complete |
| **v2.2** | 2026-03-23 | PR Patrol (auto-monitor + auto-fix feedback) | ✓ Complete |
| **v2.4** | 2026-03-25 | Outcome memory (learns from PR results) | ✓ Complete |
| **v2.6** | 2026-03-26 | MCP server (14 tools for Claude Desktop) | ✓ Complete |
| **v2.7** | 2026-03-26 | Event bus (15 typed events) + working memory | ✓ Complete |
| **v2.8** | 2026-03-26 | Context compression + progressive skills | ✓ Complete |

---

### v3.x–v4.x Series (2026-03-26 to 2026-03-28) — Production Hardening (Python)

| Version | Date | Milestone | Status |
|---------|------|-----------|--------|
| **v3.0.0** | 2026-03-26 | EventBus system, Formatter, MCP Client, CLI flags | ✓ Complete |
| **v3.0.4** | 2026-03-28 | Security hardening (constant-time API keys, webhook validation) | ✓ Complete |
| **v3.0.6** | 2026-03-28 | SKIP_DIRECTORIES filter, auto-close linked issues | ✓ Complete |
| **v4.0.0** | 2026-03-28 | Repo Intelligence, Smart Dedup, Issue-First Strategy | ✓ Complete |

---

### v5.0.0 (2026-03-28 to 2026-03-31) — Rust Rewrite ✓

| Sprint | Date | Milestone | Status |
|--------|------|-----------|--------|
| **S1** | 2026-03-28 | Core architecture: config, models, middleware, events, errors | ✓ Complete |
| **S2** | 2026-03-29 | CI Monitor, Outcome Learning, Vertex AI, token cache | ✓ Complete |
| **S3** | 2026-03-30 | Web dashboard (axum), web-server CLI command | ✓ Complete |
| **S4** | 2026-03-30 | GraphQL GitHub, JSONL event log, template+plugin system | ✓ Complete |
| **Parity** | 2026-03-31 | Full Python→Rust feature parity audit + gap implementation | ✓ Complete |

**Key Achievements (v5.0.0):**
- ✓ Complete Python→Rust rewrite: 62 .rs files, ~21,400 LOC, 323 tests
- ✓ Tokio async runtime (replacing Python asyncio)
- ✓ Axum web framework (replacing Python FastAPI)
- ✓ Clap CLI with 21 commands (replacing Python Click)
- ✓ rusqlite for SQLite (replacing Python aiosqlite)
- ✓ serde for serialization (replacing Python Pydantic)
- ✓ MCP server expanded: 21 tools (was 14)
- ✓ API key auth with constant-time comparison
- ✓ HMAC-SHA256 webhook verification
- ✓ 17 analysis skills (5 new vs Python)

---

### v5.2.0 (2026-04-01) — Interactive Login, Rust CI, 4-platform Binaries ✓

**Key Achievements (v5.2.0):**
- ✓ Interactive `contribai login` — switch LLM providers, update tokens, launch wizard
- ✓ One-line install scripts (`install.sh` + `install.ps1`) — auto-detect OS/arch
- ✓ 4-platform release binaries: Linux x86_64, Windows x86_64, macOS Intel, macOS ARM64
- ✓ Rust-first CI pipeline: fmt + clippy -D warnings + 335 tests + cargo audit
- ✓ Python legacy tests only trigger with `[python]` commit label
- ✓ Resolved 24+ clippy warnings, zero-warning strict lint
- ✓ Cross-compilation support for macOS aarch64

---

### v5.1.0 (2026-04-01) — Interactive TUI & Full CLI Parity ✓

**Key Achievements (v5.1.0):**
- ✓ Interactive TUI: ratatui 4-tab browser (Dashboard/PRs/Repos/Actions)
- ✓ Real `notify-test`: live HTTP to Slack, Discord, Telegram
- ✓ Full 22-command CLI (init, login, leaderboard, models, templates, profile, config-get/set/list, system-status, notify-test)
- ✓ Setup wizard (`contribai init`)
- ✓ Config editor (`config-get`, `config-set`, `config-list`)
- ✓ 63 .rs files, ~22,000 LOC, **335 tests**
- ✓ Python moved to `python/` (v4.1.0 legacy, preserved for reference)
- ✓ Root `Cargo.toml` workspace — `cargo build` from project root

---

## Feature Status Matrix (v5.2.0)

### Core Pipeline

| Feature | Status | Details |
|---------|--------|---------|
| Repository discovery | ✓ Complete | GitHub Search API (REST + GraphQL) |
| Multi-strategy analysis | ✓ Complete | 7 analyzers, 17 skills, framework detection |
| Tree-sitter AST parsing | ✓ Complete | 8 language grammars (Rust-only) |
| PageRank file ranking | ✓ Complete | Import graph analysis (Rust-only) |
| 12-signal triage | ✓ Complete | Multi-factor issue scoring (Rust-only) |
| LLM-powered generation | ✓ Complete | Multi-provider routing, self-review, quality scoring |
| Autonomous PR creation | ✓ Complete | Fork, branch, commit, PR, CLA/DCO handling |
| Hunt mode (multi-round) | ✓ Complete | Configurable rounds, delays, deduplication |
| Cross-file fixes | ✓ Complete | Bulk fix for pattern repetition |
| Issue-driven solving | ✓ Complete | Fetch + solve open GitHub issues |

### Safety & Compliance

| Feature | Status | Details |
|---------|--------|---------|
| Rate limiting | ✓ Complete | Daily PR limit + API rate respect |
| Quality gate | ✓ Complete | 7-check scorer, 0.6 min threshold |
| Duplicate prevention | ✓ Complete | Fuzzy title matching (>90% = duplicate) |
| AI policy detection | ✓ Complete | Parse CONTRIBUTING.md for AI bans |
| CLA auto-signing | ✓ Complete | CLA-Assistant, EasyCLA |
| DCO signoff | ✓ Complete | Auto-append to all commits |
| Deep validation | ✓ Complete | LLM validates findings vs. file context |
| Webhook verification | ✓ Complete | HMAC-SHA256 signature validation |
| API key auth | ✓ Complete | Constant-time comparison (timing attack safe) |

### Platform Features

| Feature | Status | Details |
|---------|--------|---------|
| Web dashboard | ✓ Complete | Axum REST API + static UI at `:8787` |
| Scheduler | ✓ Complete | Tokio-based cron automation |
| Webhooks | ✓ Complete | GitHub webhook receiver with HMAC verification |
| Profiles | ✓ Complete | Named presets (security-focused, docs-focused, etc.) |
| Templates | ✓ Complete | Built-in contribution templates |
| Plugins | ✓ Complete | Trait-based plugin system |
| Notifications | ✓ Complete | Slack, Discord, Telegram |
| MCP server | ✓ Complete | 21 tools for Claude Desktop |
| MCP client | ✓ Complete | StdioMcpClient for external MCP servers |

### Architecture & Internals

| Feature | Status | Details |
|---------|--------|---------|
| Event bus | ✓ Complete | 18 typed events, JSONL file logging |
| Sub-agent registry | ✓ Complete | 5 agents (Analyzer, Generator, Patrol, Compliance, Issue) |
| Context compression | ✓ Complete | 3-tier with language-aware signature extraction |
| Working memory | ✓ Complete | Per-repo cache with 72h TTL |
| Outcome learning | ✓ Complete | PR outcome tracking + repo preferences |
| Error handling | ✓ Complete | thiserror enum hierarchy + graceful recovery |
| Async-first design | ✓ Complete | All I/O via Tokio async |

---

## Completed Milestones

### Milestone 1: MVP (v0.1–v0.11, Python) ✓
- ✓ Pipeline: discovery → analysis → generation → PR
- ✓ 7 multi-strategy analyzers, multi-LLM, hunt mode, web dashboard

### Milestone 2: Safety & Learning (v1.0–v2.8, Python) ✓
- ✓ Quality scoring, CLA/DCO, PR patrol, outcome memory, event bus

### Milestone 3: Production Hardening (v3.0–v4.0, Python) ✓
- ✓ MCP server, enhanced code gen, security hardening, comprehensive docs

### Milestone 4: Rust Rewrite (v5.0.0) ✓
- ✓ Full feature parity with Python (99%+)
- ✓ New Rust-only capabilities (tree-sitter, PageRank, triage, compression)
- ✓ 62 files, ~21,400 LOC, 323 tests, single static binary

### Milestone 5: Full CLI Parity + TUI (v5.2.0) ✓
- ✓ 22 CLI commands (was 21)
- ✓ Interactive ratatui TUI browser
- ✓ Real notification testing (Slack, Discord, Telegram)
- ✓ Setup wizard + config editor commands
- ✓ Python moved to `python/` legacy, root Cargo workspace
- ✓ 335 tests

---

## Planned Features (v5.2+)

### v5.2.0 — Enterprise Scalability (Q2 2026)

- [ ] PostgreSQL migration layer (drop-in SQLite replacement)
- [ ] Redis-based distributed rate limiting
- [ ] Prometheus metrics export
- [ ] OpenTelemetry distributed tracing
- [ ] Kubernetes Helm charts
- [ ] Multi-region deployment patterns

### v5.2.0 — Advanced Analysis (Q3 2026)

- [ ] Semantic code chunking (not truncation)
- [ ] Code2Vec embeddings for similarity
- [ ] Multi-turn LLM conversations for complex reasoning
- [ ] Enhanced tree-sitter analysis (cross-file reference resolution)
- [ ] Type-aware code generation

### v5.3.0 — Plugin Ecosystem (Q4 2026)

- [ ] Central plugin registry (GitHub-based)
- [ ] Plugin package format (dynamic Rust libraries / WASM)
- [ ] Pre-built plugins: Django, React, async patterns
- [ ] Plugin security scanning

### v6.0.0 — Full Agent Autonomy (2027 H1)

- [ ] Agent-to-agent communication protocol
- [ ] Self-evaluation + automatic improvement loops
- [ ] Multi-agent coordination (spec → design → implement → test)
- [ ] GitLab/Gitea/Gitee support (pluggable VCS)

---

## Technical Debt

### Resolved by Rust Rewrite

| Item | Status |
|------|--------|
| Refactor analysis pipeline (composition over inheritance) | ✓ Done (traits) |
| Add structured logging (JSON format) | ✓ Done (tracing) |
| AST analysis for structural patterns | ✓ Done (tree-sitter) |
| Type safety throughout codebase | ✓ Done (Rust type system) |

### Remaining

| Item | Effort | Priority |
|------|--------|----------|
| Add database indexes for performance | Small | High |
| Implement integration test suite | Medium | High |
| Add structured OpenTelemetry spans | Medium | Medium |

---

## Dependency & Risk Assessment

### Key Dependencies

| Dependency | Risk Level | Mitigation |
|-----------|-----------|-----------|
| **Google Gemini API** | Medium | OpenAI/Anthropic/Ollama fallbacks |
| **GitHub API** | Low | Rate limiting, retry, GraphQL fallback |
| **Rust ecosystem** | Low | Stable, growing, excellent tooling |
| **Tokio runtime** | Low | Industry standard async runtime |
| **tree-sitter** | Low | Maintained by GitHub, widely used |

---

## Success Metrics

| Metric | v4.0 (Python) | v5.0 (Rust) | Target (v5.1) |
|--------|---------------|-------------|----------------|
| **LOC** | ~5,500 | ~21,400 | ~22,000 |
| **Test count** | ~298 | 323 | **335** |
| **Binary size** | N/A (interpreted) | ~15MB static | ~4.5MB stripped |
| **Startup time** | ~2s | <100ms | ~5ms |
| **Memory usage** | ~80MB | ~20MB | ~8MB |
| **MCP tools** | 14 | 21 | 21 |
| **CLI commands** | 8 | 21 | **22** |
| **Analysis skills** | 12 | 17 | 17 |
| **AST languages** | 0 | 8 | 8 |

---

## Document Metadata

- **Created:** 2026-03-28
- **Last Updated:** 2026-04-01
- **Version:** 5.2.0 (TUI + full CLI parity)
- **Next Review:** 2026-06-30 (Q2 end)
