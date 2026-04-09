# Contributing to ContribAI

Thank you for your interest in contributing to ContribAI! 🎉

## 🚀 Quick Start

```bash
# Clone & build (Rust — primary)
git clone https://github.com/tang-vu/ContribAI.git
cd ContribAI
cargo build --release
cargo install --path crates/contribai-rs

# Verify
cargo test              # 335 tests must pass
contribai --help        # shows 22 commands
```

> **Legacy Python** is in `python/` (v4.1.0, reference only).  
> If working on Python legacy: `cd python && pip install -e ".[dev]" && pytest tests/ -v`

## 📋 Development Workflow

1. **Create a branch** from `main`:
   ```bash
   git checkout -b feat/your-feature
   ```

2. **Write Rust code** following our standards:
   - All I/O is `async fn` with tokio
   - `anyhow::Result` for app code, `thiserror` for lib errors
   - `snake_case` functions/vars, `PascalCase` structs/enums
   - `///` doc comments on all public items
   - Lines max 100 chars (clippy enforced)

3. **Write tests** co-located with source (`#[cfg(test)] mod tests`)

4. **Lint & format**:
   ```bash
   cargo fmt
   cargo clippy -- -D warnings
   ```

5. **Run tests**:
   ```bash
   cargo test              # 335 tests
   cargo test -- --nocapture   # with stdout
   ```

6. **Commit** with conventional messages:
   ```bash
   git commit -m "feat: add Django security analyzer"
   ```
   Valid prefixes: `feat`, `fix`, `refactor`, `docs`, `test`, `perf`, `chore`

7. **Push & create PR** using the PR template

## 🏗️ Project Structure (v5.1.0)

| Directory | Purpose |
|-----------|---------|
| `crates/contribai-rs/src/cli/` | 22 commands + ratatui TUI |
| `crates/contribai-rs/src/core/` | Config, models, middleware, events |
| `crates/contribai-rs/src/analysis/` | 7 analyzers + 17 progressive skills |
| `crates/contribai-rs/src/llm/` | Multi-provider LLM + 5 sub-agents |
| `crates/contribai-rs/src/github/` | GitHub REST + GraphQL client |
| `crates/contribai-rs/src/generator/` | Code generation + self-review + scorer |
| `crates/contribai-rs/src/pr/` | PR lifecycle + patrol |
| `crates/contribai-rs/src/orchestrator/` | Pipeline + SQLite memory (72h TTL) |
| `crates/contribai-rs/src/mcp/` | 21-tool MCP server (stdio JSON-RPC) |
| `crates/contribai-rs/src/web/` | axum dashboard + webhooks |
| `crates/contribai-rs/tests/` | 335 unit tests |
| `python/` | Legacy v4.1.0 (reference only) |
| `docs/` | Architecture documentation |
| `.agents/workflows/` | Development workflows |

## 🔑 Key Architecture Patterns

1. **Middleware Chain** — 5 ordered middlewares: RateLimit → Validation → Retry → DCO → QualityGate
2. **Progressive Skills** — 17 analysis skills loaded on-demand by language/framework
3. **Sub-Agent Registry** — 5 agents with parallel execution
4. **Tool Protocol** — MCP-inspired interface for GitHub/LLM tools
5. **Outcome Learning** — Tracks PR merge/rejection per repo (SQLite)
6. **Context Compression** — LLM-driven compression with 30k token budget
7. **Interactive TUI** — ratatui 4-tab browser (Dashboard/PRs/Repos/Actions)

See [AGENTS.md](AGENTS.md) for full architecture and code patterns.

## 🤖 AI Agent Guide

If you're an AI assistant scanning this repo, see [AGENTS.md](AGENTS.md) for structured context.

## ✅ PR Requirements

- All CI checks pass (clippy, tests)
- Tests for new/changed code
- Documentation updated (if user-facing)
- Follows conventional commits
- CHANGELOG.md updated (if applicable)
