# ContribAI Codebase Summary

**Version:** 5.2.0 | **Language:** Rust | **Total LOC:** ~22,000 | **Files:** 63 .rs | **Tests:** 335

---

## Quick Navigation

```
crates/contribai-rs/src/
├── core/              # Config, models, middleware, events, errors, quotas (9 files)
├── llm/               # Multi-provider LLM routing, context, formatter (7 files)
├── github/            # GitHub REST+GraphQL client, discovery, guidelines (4 files)
├── analysis/          # Analyzers, skills, triage, AST intel, repo map (8 files)
├── generator/         # Code fix generation, scorer, self-review, validation (6 files)
├── orchestrator/      # Pipeline, memory (SQLite), review gate (4 files)
├── pr/                # PR lifecycle, patrol monitoring (3 files)
├── issues/            # Issue-driven contributions (2 files)
├── agents/            # Sub-agent registry (2 files)
├── tools/             # Tool protocol (1 file)
├── mcp/               # MCP server (21 tools) + client (3 files)
├── web/               # Axum dashboard, API key auth, webhooks (1 file)
├── cli/               # Clap CLI with 22 commands + ratatui TUI (3 files)
├── scheduler/         # Tokio cron scheduler (1 file)
├── plugins/           # Trait-based plugin system (1 file)
├── templates/         # Contribution templates (1 file)
├── notifications/     # Slack/Discord/Telegram (1 file)
├── sandbox/           # Code validation (1 file)
├── lib.rs             # Crate root (public modules)
└── main.rs            # Binary entry point
```

---

## Module Responsibilities

| Module | Purpose | Key Types/Functions | Files |
|--------|---------|---------------------|-------|
| **core** | Config, models, middleware, events, errors, quotas, profiles, retry | `ContribAIConfig`, `Repository`, `Finding`, `Contribution`, `Middleware`, `EventBus` | 9 |
| **llm** | Multi-provider routing, token budgeting, formatting | `LlmProvider`, `TaskRouter`, `ContextManager`, `Formatter` | 7 |
| **github** | Async GitHub client (REST+GraphQL), repo discovery, guideline parsing | `GitHubClient`, `RepoDiscovery`, `GuidelineParser` | 4 |
| **analysis** | Multi-strategy analysis, progressive skills, triage, AST intel, repo map | `CodeAnalyzer`, `AnalysisSkill`, `TriageEngine`, `AstIntel`, `RepoMap` | 8 |
| **generator** | LLM-powered fix generation, self-review, quality scoring, validation | `ContributionGenerator`, `QualityScorer`, `SelfReview` | 6 |
| **orchestrator** | Pipeline coordination, SQLite memory, review gate | `Pipeline`, `Memory`, `ReviewGate` | 4 |
| **pr** | PR creation, patrol monitoring | `PRManager`, `PRPatrol` | 3 |
| **issues** | Issue discovery and solving | `IssueSolver` | 2 |
| **agents** | Sub-agent registry with parallel execution | `SubAgentRegistry` | 2 |
| **tools** | Tool protocol (MCP-inspired) | `Tool`, `ToolResult` | 1 |
| **mcp** | MCP stdio server (21 tools) + client | `McpServer`, `StdioMcpClient` | 3 |
| **web** | Axum REST API, API key auth, webhook receiver, dashboard | `run_server`, `AppState`, `verify_webhook_signature` | 1 |
| **cli** | Clap-based CLI with 22 commands + ratatui TUI | `Cli`, `Commands`, `run_interactive_tui` | 3 |
| **scheduler** | Tokio-based cron automation | `ContribScheduler` | 1 |
| **plugins** | Trait-based plugin system | `AnalyzerPlugin`, `GeneratorPlugin` | 1 |
| **templates** | Contribution templates | `TemplateRegistry` | 1 |
| **notifications** | Slack/Discord/Telegram integrations | `Notifier` | 1 |
| **sandbox** | Code validation | `Sandbox` | 1 |

---

## Dependency Graph

```
                     ┌──────────────────┐
                     │   CLI / Web      │
                     │  (clap / axum)   │
                     └────────┬─────────┘
                              │
                   ┌──────────┴──────────┐
                   ▼                     ▼
            ┌─────────────┐      ┌──────────────┐
            │ Orchestrator│      │  Scheduler   │
            │  + Pipeline │      │   (tokio)    │
            └─────┬───────┘      └──────────────┘
                  │
        ┌─────────┼─────────┬──────────┐
        ▼         ▼         ▼          ▼
    ┌────────┐┌────────┐┌────────┐┌────────┐
    │Analysis││Generator││  PR    ││ Issues │
    │+Triage ││+Scorer ││Manager ││ Solver │
    └────┬───┘└────┬───┘└────┬───┘└────┬───┘
         │         │         │         │
         └─────────┼─────────┴─────────┘
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
    ┌─────────┐         ┌──────────┐
    │   LLM   │         │  GitHub  │
    │ Routing │         │  Client  │
    └────┬────┘         └────┬─────┘
         │                   │
         └───────┬───────────┘
                 ▼
         ┌──────────────┐
         │    CORE      │
         │ (Models,     │
         │  Config,     │
         │  Middleware,  │
         │  Events)     │
         └──────────────┘
```

**Dependency Flow:** core ← github/llm ← analysis/generator ← orchestrator ← cli/web

---

## Key Entry Points

### CLI Entry Point
- **File:** `crates/contribai-rs/src/cli/mod.rs`
- **Struct:** `Cli` (clap derive)
- **22 Commands:**
  - `run` — Single full pipeline run
  - `hunt` — Autonomous multi-round hunting
  - `patrol` — Monitor open PRs
  - `target` — Analyze specific repo
  - `analyze` — Dry-run analysis
  - `solve` — Solve issues in a repo
  - `stats` — Summary statistics
  - `status` — Show PR status table
  - `leaderboard` — Merge rates by repo
  - `models` — Available LLM models
  - `templates` — Contribution templates
  - `profile` — Named config profiles
  - `cleanup` — Remove stale forks
  - `notify-test` — Real HTTP to Slack/Discord/Telegram
  - `system-status` — DB, rate limits, scheduler
  - `interactive` — **ratatui TUI browser** (NEW in v5.2.0)
  - `web-server` — Start web dashboard
  - `schedule` — Start cron scheduler
  - `mcp-server` — MCP stdio server
  - `init` — Interactive setup wizard
  - `login` — Auth status
  - `config-get/set/list` — YAML config editor

### Web Entry Point
- **File:** `crates/contribai-rs/src/web/mod.rs`
- **Framework:** Axum (tokio-based)
- **Key Routes:**
  - `GET /` — Dashboard HTML
  - `GET /api/stats` — Overall statistics
  - `GET /api/repos` — Analyzed repos list
  - `POST /api/run` — Trigger pipeline (API key required)
  - `POST /api/run/target` — Target specific repo (API key required)
  - `POST /api/webhooks/github` — GitHub webhook (HMAC-SHA256)
  - `GET /api/health` — Health check

### MCP Server Entry Point
- **File:** `crates/contribai-rs/src/mcp/server.rs`
- **Protocol:** stdio JSON-RPC (Model Context Protocol)
- **Exposed Tools:** 21 (GitHub read/write, safety, maintenance, PR management)

---

## Critical Data Structures

### Core Models (serde + struct)

| Struct | Purpose | Key Fields |
|--------|---------|-----------|
| `Repository` | GitHub repo metadata | `owner`, `name`, `full_name`, `language`, `stars`, `forks`, `topics` |
| `Finding` | Detected issue | `finding_type`, `file_path`, `line`, `description`, `severity`, `context` |
| `Contribution` | Proposed fix | `finding`, `code_change`, `explanation`, `confidence_score` |
| `PRResult` | PR outcome | `pr_number`, `url`, `status` |
| `ContribAIConfig` | Application config | `github`, `llm`, `discovery`, `analysis`, `pipeline`, `web` |

### Database Schema (SQLite via rusqlite, 7 tables)

| Table | Purpose |
|-------|---------|
| `analyzed_repos` | Track analyzed repositories |
| `submitted_prs` | All created PRs |
| `findings_cache` | Cached analysis results (72h TTL) |
| `run_log` | Pipeline execution history |
| `pr_outcomes` | PR merge/close outcomes for learning |
| `repo_preferences` | Learned repo patterns |
| `ci_monitor` | CI status tracking |

### Event Types (18 total)

```rust
RepositoryDiscovered | RepositoryAnalyzed | FindingDetected |
ContributionGenerated | PRCreated | PRMerged | PRClosed |
PRPatrolStarted | ReviewFound | CodeChangeGenerated |
ConfigLoaded | PipelineStarted | PipelineCompleted |
ErrorOccurred | RateLimitExceeded | IssueFound |
SchedulerStarted | WebhookReceived
```

---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| **Language** | Rust 2021 edition |
| **Async Runtime** | Tokio (multi-threaded) |
| **Web** | Axum, tower, hyper |
| **HTTP Client** | reqwest (async) |
| **GitHub** | reqwest + REST/GraphQL APIs |
| **LLM** | reqwest (Gemini, OpenAI, Anthropic, Ollama) |
| **Serialization** | serde, serde_json, serde_yaml |
| **Database** | rusqlite (sync, wrapped in tokio::task::spawn_blocking) |
| **CLI** | clap (derive macros) |
| **Logging** | tracing, tracing-subscriber |
| **Code Parsing** | tree-sitter (8 language grammars) |
| **Crypto** | hmac, sha2, hex (webhook verification) |
| **Testing** | cargo test (built-in), 335 tests |
| **Linting** | clippy |
| **Formatting** | rustfmt |

---

## Rust-Only Features (Not in Python)

| Feature | Module | Description |
|---------|--------|-------------|
| **Tree-sitter AST** | `analysis/ast_intel.rs` | Parse 8 languages (Rust, Python, JS, TS, Go, Java, C, C++) |
| **PageRank file ranking** | `analysis/repo_map.rs` | Rank file importance via import graph analysis |
| **12-signal triage** | `analysis/triage.rs` | Score issues by recency, complexity, maintainer activity, etc. |
| **3-tier context compression** | `analysis/compressor.rs` | Language-aware signature extraction for 5 languages |
| **Language rules** | `analysis/language_rules.rs` | Per-language analysis rules and patterns |
| **Leaderboard** | `core/leaderboard.rs` | Contribution tracking and ranking |

---

## Common Code Patterns

### Pattern 1: Async with Tokio

```rust
pub async fn process_repo(&self, repo: &Repository) -> Result<PipelineResult> {
    let findings = self.analyzer.analyze(repo).await?;
    let contributions = self.generator.generate_fixes(&findings).await?;
    let prs = self.pr_manager.create_prs(repo, &contributions).await?;
    Ok(PipelineResult { repo: repo.clone(), prs })
}
```

### Pattern 2: Serde Models

```rust
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Finding {
    pub finding_type: String,
    pub file_path: String,
    pub line: usize,
    pub description: String,
    pub severity: Severity,
}
```

### Pattern 3: Trait-Based Providers

```rust
pub trait LlmProvider: Send + Sync {
    async fn complete(&self, prompt: &str) -> Result<String>;
    fn name(&self) -> &str;
}
```

### Pattern 4: Middleware Chain

```rust
pub struct MiddlewareChain {
    middlewares: Vec<Box<dyn Middleware>>,
}
// RateLimit → Validation → Retry → DCO → QualityGate
```

### Pattern 5: Event Bus

```rust
event_bus.emit(Event::PRCreated {
    repo: repo.full_name.clone(),
    pr_number,
    url: pr_url.clone(),
    timestamp: Utc::now(),
});
```

---

## Testing Structure

Tests are co-located in each source file using `#[cfg(test)] mod tests`:

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_feature() {
        // Arrange, Act, Assert
    }

    #[tokio::test]
    async fn test_async_feature() {
        // Async test with tokio runtime
    }
}
```

**Test Coverage:** 335 tests across 63 source files
**Test Command:** `cargo test` (all tests), `cargo test <module>` (specific)

---

## Configuration

- **Source:** `crates/contribai-rs/src/core/config.rs`
- **Format:** YAML (`config.yaml`) + environment variables (`CONTRIBAI_*`)
- **Load Order:** CLI flags → Env vars → YAML → Defaults
- **Key Structs:** `ContribAIConfig`, `GitHubConfig`, `LlmConfig`, `DiscoveryConfig`, `WebConfig`

---

## Document Metadata

- **Created:** 2026-03-28
- **Last Updated:** 2026-04-01
- **Version:** 5.2.0 (Interactive TUI, real notify-test, full CLI parity)
