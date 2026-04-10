# Changelog

All notable changes to ContribAI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.4.1] - 2026-03-26

### Fixed
- `summarize_findings()` used `Finding.contribution_type` instead of `Finding.type` — caused `AttributeError` during hunt mode
- SECURITY.md referenced non-existent email domain — now uses GitHub Issues

### Added
- 86 new unit tests for v2.4.0 modules (middleware, skills, registry, protocol) — 333 total
- `docs/ARCHITECTURE.md` — detailed architecture documentation
- `AGENTS.md` — AI agent guide for Copilot, Claude, Coderabbit
- `.github/copilot-instructions.md` — GitHub Copilot context

### Changed
- Updated all .md files for v2.4.0 architecture (README, CONTRIBUTING, SECURITY, PR template, dev workflow)
- Coverage restored to 53% (was 45% due to untested new modules)

## [2.4.0] - 2026-03-25

### Added
- **Middleware chain** (`contribai/core/middleware.py`): Pipeline processing with 5 built-in middlewares — RateLimit, Validation, Retry, DCO, QualityGate
- **Progressive skill loading** (`contribai/analysis/skills.py`): 17 analysis skills loaded on-demand by language/framework instead of all at once — saves tokens and improves quality
- **Framework detection**: Auto-detect Django, Flask, FastAPI, React, Express, Spring, Rails, etc. from file tree
- **Outcome learning** (`memory.py`): New `pr_outcomes` + `repo_preferences` tables — tracks PR merge/rejection to learn which contribution types work per repo
- **Context summarization** (`analyzer.py`): `summarize_findings()` compresses analysis results for downstream LLM prompts
- **Sub-agent registry** (`contribai/agents/registry.py`): 4 agent stubs (Analyzer, Generator, Patrol, Compliance) with parallel execution (max 3 concurrent)
- **Tool protocol** (`contribai/tools/protocol.py`): MCP-inspired tool system with ToolRegistry, GitHubTool, and LLMTool wrappers
- **DCO auto-signoff**: All commits via GitHub API auto-append `Signed-off-by` trailer

### Changed
- Architecture inspired by ByteDance DeerFlow 2.0 super agent harness
- README updated with PR Patrol section, v2.4.0 badges

## [2.3.0] - 2026-03-24

### Added
- **Bot review context**: When maintainer replies to a bot review (Coderabbit, etc.), patrol reads the bot's original analysis and includes it as context for LLM-based code fix generation
- **Assigned issue monitoring**: Patrol scans repos for issues assigned to our user and reports them
- **34 new unit tests** for patrol engine covering feedback collection, bot context linking, classification parsing, and assigned issue detection

### Fixed
- `generate()` → `complete()` in `_handle_code_fix` (LLM method mismatch)
- Bot comment filtering for 11 review bot logins + `[bot]` suffix detection
- Exponential backoff retry (5s → 10s → 20s) for rate limit errors during LLM calls
- Orphaned `except` block parse error in `_classify_feedback`

## [2.2.0] - 2026-03-23

### Added
- **PR Patrol** (`contribai patrol`): Monitor open PRs for review feedback and auto-respond
  - Reads maintainer review comments (issue comments + inline code reviews)
  - LLM-based feedback classification: CODE_CHANGE, QUESTION, STYLE_FIX, APPROVE, REJECT, ALREADY_HANDLED
  - Generates code fixes from review feedback and pushes to PR branch
  - Answers maintainer questions with context-aware LLM responses
  - Re-signs CLA after pushing new commits
  - `--dry-run` to preview actions, `--pr N` to filter specific PR
- **GitHub API methods**: `get_pr_reviews()`, `get_pr_review_comments()`, `create_pr_review_comment_reply()`, `get_pr_diff()`
- **Patrol models**: `FeedbackAction` enum, `FeedbackItem`, `PatrolResult`

## [2.1.0] - 2026-03-22

### Added
- **Smart Context Builder**: `_detect_project_profile()` auto-detects project type (library, web_app, api_server, cli_tool, data_pipeline), tech stack (Django, Flask, FastAPI, etc.), and conventions (tests, CI, type hints)
- **Style Guide Extraction**: `_build_style_guide()` analyzes source code to detect naming conventions, error handling, docstring format, import style, and logging patterns
- **Score-based File Prioritization**: `_prioritize_files()` ranks files by contribution value (entry points +40, API routes +35, auth/security +30, config +20) with penalties for tests, vendor, and deeply nested files
- **Anti-false-positive Rules**: 5 mandatory checks before reporting findings — ALREADY_HANDLED, BY_DESIGN, BOUNDED_CONTEXT, TRIVIAL_FIX, COSMETIC
- **Pre-generation Validation**: Early filter skips findings targeting non-code files (SKIP_EXTENSIONS) and protected meta files before expensive LLM code generation
- **Maintainer Acceptance Gate**: Generation prompt includes "30-second merge test" criteria

### Changed
- Analyzer system prompt upgraded from generic "expert code analyst" to "senior software engineer performing focused code review" with project profile injection
- Security prompt now focuses on real exploitability: SQL injection only for raw queries (not ORM), hardcoded secrets only outside test fixtures
- Code quality prompt focuses on bugs/crashes: unhandled None, resource leaks, race conditions, off-by-one errors
- Performance prompt requires >10% measurable impact; skips micro-optimizations
- Max 3 findings per analyzer (quality over quantity)
- Generator system prompt includes style guide injection and 8 explicit rules (no adjacent refactoring, no comments, no unrelated files)

## [2.0.0] - 2026-03-22

### Added
- **Parallel Hunt Mode**: `asyncio.gather` + semaphore for concurrent repo processing in hunt
  - New `_hunt_process_repo()` method extracted as class method
  - Honors `max_concurrent_repos` config (default: 3)
- **GitHub API retry with backoff**: `_request()` retries 3× on 502/503/504 errors (2s/4s/8s)
- **Fork cleanup command**: `contribai cleanup` — syncs PR statuses, removes stale forks via `gh repo delete`
- **Code-only file filter**: `SKIP_EXTENSIONS` (.md, .yaml, .json, .toml, .rst, .txt, .cfg, .ini, .lock) and `PROTECTED_META_FILES` (LICENSE, CONTRIBUTING.md, etc.) prevent non-code modifications
- **Hunt mode flags**: `--mode analysis|issues|both` for fine-grained control
- **EXE standalone behavior**: Defaults to `info` command when run without arguments, pauses before exit

### Changed
- `max_repos_per_run` from config is now respected in hunt mode (was hardcoded to 3)
- `star_tiers` in hunt mode now prioritizes configured `stars_range` first
- Daily PR limit default changed from 10 to 15
- Test count: 213 tests (refactored from 287)

### Fixed
- Hunt mode ignored `max_repos_per_run` config, used hardcoded `targets[:3]`
- 504 Gateway Timeout crashes when pushing files to GitHub API
- Unwanted PRs modifying non-code files (CONTRIBUTING.md, LICENSE, .yaml, .json)


## [1.0.0] - 2026-03-20

### Added
- **Stealth Mode**: PRs appear human-written — no ContribAI branding in body, branch names, or comments
- **CLA Auto-signing**: Detects CLAAssistant/EasyCLA bots and auto-signs CLA agreements
- **AI Policy Detection**: Checks `AI_POLICY.md` and `CONTRIBUTING.md` for anti-AI contribution policies, skips banned repos
- **Max 2 findings per repo**: Prevents spamming repos with too many PRs
- `create_pr_comment()` method in GitHubClient

### Changed
- Branch names: `fix/xxx` instead of `contribai/fix-xxx` (stealth)
- PR body: clean `## Problem / ## Solution / ## Changes` format
- CI auto-close message: no branding or emoji
- License: AGPL-3.0 + Commons Clause (from MIT)

### Fixed
- Updated all test assertions to v1.0.0

## [0.11.0] - 2026-03-20

### Added
- **Hunt Mode**: Autonomous multi-round repo discovery and PR creation
- `contribai hunt --rounds N --delay M` CLI command
- Configurable delay between hunt rounds
- 5 new tests (total: 287 tests)

## [0.10.0] - 2026-03-20

### Added
- **GitHub API dedup**: Prevents searching same repos twice across rounds
- **Cross-file pattern matching**: Detects same issue across multiple files and fixes all in one PR
- **Duplicate PR prevention**: Title similarity matching prevents creating duplicate PRs

## [0.9.0] - 2026-03-19

### Added
- **Deep finding validation**: LLM re-validates findings against full file context to filter false positives
- **Post-PR CI monitoring**: Polls CI check runs and auto-closes PRs that fail
- **Fuzzy search/replace matching**: Fallback matching when exact search strings don't match

## [0.8.0] - 2026-03-19

### Added
- **Performance analyzer**: Detects blocking calls, string allocation, N+1 queries
- **Refactor analyzer**: Finds unused imports, non-null assertions, encoding issues
- **Testing analyzer**: Identifies missing test coverage opportunities

### Fixed
- CI test failures and lint formatting errors

## [0.7.1] - 2026-03-19

### Fixed
- Auto-check PR template checkboxes for repos with required checklists
- Use search/replace blocks instead of full-file replacement to preserve existing code

## [0.7.0] - 2026-03-19

### Added
- **Multi-Model Agent System**: Task-based routing to different LLM models
- **Model Tiers**: Fast models for triage, powerful models for code generation
- **Vertex AI**: Google Cloud Vertex AI provider support
- **Env var fallback**: Token/API key resolution from environment variables
- **Auto-create issue**: Creates GitHub issue alongside PR for traceability
- **Post-PR compliance loop**: Monitors PR feedback and auto-fixes
- **Repo guidelines compliance**: Reads CONTRIBUTING.md and adapts PR format
- 287 tests total

## [0.6.0] - 2026-03-18

### Added
- **Interactive TUI**: Rich-based CLI interactive mode for browsing, selecting, and approving contributions
- **Contribution Leaderboard**: PR merge/close rate tracking with repo rankings and type-based stats
- **Multi-language Analyzers**: 19 analysis rules for JavaScript/TypeScript (7), Go (6), Rust (6)
- **Notification System**: Slack webhook, Discord embeds, Telegram Bot API integration
- 3 new CLI commands: `interactive`, `leaderboard`, `notify-test`
- `NotificationConfig` in config with per-channel and event-type toggles
- `httpx` dependency for notification HTTP clients

## [0.5.0] - 2026-03-18

### Added
- **Plugin System**: Entry-point based `AnalyzerPlugin` / `GeneratorPlugin` with auto-discovery
- **Webhooks**: GitHub webhook receiver (issues.opened, issues.labeled, push) with HMAC-SHA256
- **Usage Quotas**: Daily tracking for GitHub API calls, LLM calls, and token usage
- **API Key Auth**: `X-API-Key` header auth for dashboard mutation endpoints
- **Docker Compose**: 3-service setup (dashboard, scheduler, runner) with shared volumes

## [0.4.0] - 2026-03-18

### Added
- **Web Dashboard**: FastAPI REST API + static HTML dashboard with stats, PRs, repos, run history
- **Scheduler**: APScheduler-based cron scheduling for automated pipeline runs
- **Parallel Processing**: `asyncio.gather` + Semaphore for concurrent repo processing (default 3)
- **Contribution Templates**: 5 built-in YAML templates
- **Community Profiles**: 4 named presets (security-focused, docs-focused, full-scan, gentle)

## [0.3.0] - 2026-03-18

### Added
- **Issue Solver**: Classify GitHub issues by labels/keywords, filter by solvability, LLM-powered solving
- **Framework Strategies**: Auto-detect Django, Flask, FastAPI, React/Next.js, Express
- **Quality Scorer**: 7-check quality gate before PR submission

## [0.2.0] - 2026-03-18

### Added
- **Retry Utilities**: `async_retry` decorator with exponential backoff + jitter
- **LRU Cache**: Response caching for GitHub API and LLM calls
- **Test Suite**: 128 tests across all modules

## [0.1.0] - 2026-03-17

### Added
- **Core Pipeline**: Full discover → analyze → generate → PR workflow
- **Multi-LLM Support**: Gemini (primary), OpenAI, Anthropic, Ollama providers
- **GitHub Integration**: Async API client with rate limiting, repo discovery
- **Code Analysis**: Security, code quality, documentation, and UI/UX analyzers
- **Contribution Generator**: LLM-powered code generation with self-review
- **PR Manager**: Automated fork → branch → commit → PR workflow
- **Memory System**: SQLite-backed persistent tracking of repos and PRs
- **Rich CLI**: Commands: `run`, `target`, `analyze`, `status`, `stats`, `config`
