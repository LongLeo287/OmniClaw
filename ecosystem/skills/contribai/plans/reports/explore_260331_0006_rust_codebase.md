# Rust Codebase Exploration Report

## Architecture Overview
- 78 Rust source files organized into 12 core modules
- Monolithic crate structure with async/await (Tokio)
- Full CLI interface with subcommands (run, hunt, patrol, target, mcp-server, web-server, stats, version)

## Core Modules

### 1. CLI Module (src/cli/mod.rs)
- Commands: run, hunt, patrol, target, mcp-server, web-server, stats, version
- Flags: --language, --stars, --dry-run, --rounds, --delay, --host, --port
- Uses clap derive macros for command parsing
- Creates GitHub client, LLM provider, Memory, and EventBus

### 2. GitHub Module (src/github/)
- GitHubClient: Async HTTP client with reqwest
- Methods: search_repositories, get_repo_details, get_file_tree, get_file_content, fork_repository, create_branch, create_or_update_file, create_pull_request, get_pr_comments, get_open_issues, search_issues, graphql_query
- Rate limit handling: check_rate_limit(), ensure_rate_limit()
- Error handling: 3 retries with exponential backoff
- RepoDiscovery: Search, filter, prioritize repositories
- RepoGuidelines: Parse CONTRIBUTING.md and PR templates

### 3. Analysis Module (src/analysis/)
- CodeAnalyzer: Main orchestrator
  1. Fetch file tree
  2. Select analyzable files
  3. AST parse via tree-sitter
  4. Build import graph → PageRank
  5. Select skills
  6. LLM analyze
  7. Triage score
- AstIntel (NEW): Tree-sitter wrapper supporting Python, JS, TS, Go, Rust, Java, C, C++
- TriageEngine (NEW): 12 weighted signals for finding prioritization
- PageRank (NEW): File importance ranking
- Skills: Analysis skill registry with language/framework matching

### 4. LLM Module (src/llm/)
- LlmProvider trait: complete(), chat()
- Implementations: GeminiProvider, OpenAiProvider, AnthropicProvider, OllamaProvider
- GeminiProvider: Supports API key + Vertex AI (token cached 55min)
- TaskRouter: Cost-aware routing (Performance, Balanced, Economy)
- Models: gemini-3.1-pro, gemini-3-flash, gpt-4o, claude-3-5-sonnet, etc.

### 5. Generator Module (src/generator/)
- ContributionGenerator: Code generation pipeline
  1. Build context
  2. LLM generate (with retry)
  3. Parse structured output
  4. Validate
  5. Quality score
  6. Self-review (optional)
- QualityScorer: 7 quality checks
- Validation: Bracket balancing, no-op detection, size checks
- JSON parser: Extracts FileChange objects from markdown-wrapped JSON

### 6. Orchestrator Module (src/orchestrator/)
- ContribPipeline: Main orchestrator
  - run() → PipelineResult
  - Protected files: CONTRIBUTING.md, LICENSE, .github/CODEOWNERS
  - Skip directories: examples, docs, test, vendor, __pycache__, node_modules
- Memory (SQLite): 7 tables for persistence
  - analyzed_repos, submitted_prs, findings_cache, run_log, pr_outcomes, repo_preferences, working_memory

### 7. PR Module (src/pr/)
- PrManager: Full PR lifecycle (fork → branch → commit → PR)
- Methods: create_pr(), fork_if_needed(), human_branch_name(), build_signoff()
- PrPatrol: Monitor open PRs, respond to feedback
- Skips review bots: coderabbitai, copilot, dependabot, sonarcloud

### 8. Core Module (src/core/)
- ContribAIConfig: Config loading from YAML + env vars
- Models: Repository, Issue, FileNode, Finding, Contribution, FileChange, AnalysisResult, Symbol, DiscoveryCriteria
- Enums: ContributionType (7 types), Severity (4 levels), PrStatus, SymbolKind
- Error handling: ContribError enum
- Events: EventType (18 types), Event struct, EventBus
- Retry: async_retry(), github_retry(), llm_retry()
- Middleware: MiddlewareChain, PipelineContext

### 9. Issues Module (src/issues/)
- IssueSolver: Classify and solve GitHub issues
- IssueCategory: Bug, Feature, Docs, Security, Performance, UiUx, GoodFirstIssue

### 10. MCP Module (src/mcp/)
- run_stdio_server(): JSON-RPC 2.0 over stdio
- Exposed tools: search_repos, get_repo_info, get_file_tree, get_file_content, get_open_issues, fork_repo, create_branch, push_file_change, create_pr, close_pr, check_duplicate_pr, check_ai_policy, get_stats, patrol_prs, cleanup_forks

### 11. Web Module (src/web/)
- run_server(): Axum HTTP server
- Routes: GET /, /api/health, /api/stats, /api/repos, /api/prs, /api/runs; POST /api/run, /api/target
- CORS enabled, pagination support

### 12. Supporting Modules
- agents: Agent registry (stub)
- notifications: Webhooks (stub)
- plugins: Plugin system (stub)
- sandbox: Sandboxed execution (stub)
- scheduler: Task scheduling (stub)
- templates: PR/commit templates (stub)
- tools: Utilities (stub)

## Key Data Models

### Enums
- ContributionType: SecurityFix, FeatureAdd, DocsImprove, UiUxFix, PerformanceOpt, Refactor, CodeQuality
- Severity: Low (1.0), Medium (2.0), High (3.0), Critical (4.0)
- PrStatus: Pending, Open, Merged, Closed, ReviewRequested
- SymbolKind: Function, Class, Method, Interface, Struct, Enum, Constant, Variable, Import
- FixComplexity: Trivial, Simple, Moderate, Complex

### Structs
- Repository: owner, name, full_name, language, stars, default_branch, topics, last_push_at
- Finding: id, finding_type, severity, title, description, file_path, line_start/end, suggestion, confidence
- FileChange: path, original_content, new_content, is_new_file, is_deleted
- Contribution: finding, contribution_type, title, description, changes[], commit_message, tests_added[]
- AnalysisResult: repo, findings[], analyzed_files, analysis_duration_sec
- Symbol: name, kind, file_path, line_start, line_end
- RemediationSpec: finding, fix_complexity, priority_score, signals[]
- PrResult: pr_url, pr_number, repo, status, created_at

## Configuration

**config.yaml structure:**
- github: token, max_prs_per_day, rate_limit_buffer
- llm: provider, model, api_key, temperature, max_tokens, vertex_project
- analysis: max_context_tokens
- discovery: languages, stars_min, stars_max, max_results
- pipeline: min_quality_score, max_retries
- storage: db_path
- contribution, quotas, notifications, sandbox, scheduler, multi_model

**Env vars (priority over config):**
- GITHUB_TOKEN (fallback: gh auth token)
- GEMINI_API_KEY, OPENAI_API_KEY, ANTHROPIC_API_KEY
- GOOGLE_CLOUD_PROJECT (for Vertex AI)

## Key Features

### NEW in Rust
1. Tree-sitter AST parsing (8 languages)
2. PageRank file importance
3. Weighted triage (12 signals)
4. Async/await (Tokio)
5. Static binary
6. MCP protocol
7. Axum web server

### Ported from Python
1. Multi-provider LLM
2. Smart model routing
3. 7 contribution types
4. Repository discovery
5. PR patrol
6. SQLite memory
7. Middleware chain
8. YAML + env config

## Statistics
- 78 .rs files
- ~15,000+ lines of code
- 46 test modules
- 8 supported languages (AST)
- 4 LLM providers
- 22 MCP tools
- 7 contribution types
- 12 triage signals
- 7 quality checks
- 7 database tables

## Dependencies
**Runtime:** tokio, reqwest, tree-sitter (8 lang), serde/json/yaml, rusqlite, clap, tracing, axum/tower-http, chrono, regex, uuid, colored, indicatif
**Dev:** mockall, tempfile, wiremock, tokio-test
**Build:** Release profile with size optimization (opt-level=z), LTO, single codegen unit, stripped

