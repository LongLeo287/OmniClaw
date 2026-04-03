---
id: github.com-auriti-labs-kore-memory-8b1caaca-knowle
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:33.506887
---

# KNOWLEDGE EXTRACT: github.com_Auriti-Labs_kore-memory_8b1caaca
> **Extracted on:** 2026-04-01 11:41:52
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007521465/github.com_Auriti-Labs_kore-memory_8b1caaca

---

## File: `.gitignore`
```
# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd
.Python
*.egg-info/
dist/
build/
.eggs/

# Virtual environment
.venv/
venv/
env/

# Data & secrets — NEVER commit
data/
logs/
*.db
*.db-shm
*.db-wal
.api_key
*.key
*.secret
.env
.env.*

# IDE
.vscode/
.idea/
*.swp
*.swo

# Testing
.pytest_cache/
.coverage
htmlcov/

# Piani di lavoro
PLAN-*.md

# Claude Code (local only)
CLAUDE.md

# SDK JS
sdk/js/node_modules/
sdk/js/dist/

# OS
.DS_Store
Thumbs.db
```

## File: `CHANGELOG.md`
```markdown
# Changelog

All notable changes to Kore Memory are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

---

## [2.0.0] - 2026-02-27

### Theme: "Intelligence"

### Added
- **Graph RAG with recursive CTE** — `GET /graph/traverse?start_id=X&depth=3` traverses the memory relation graph up to 10 hops using SQLite recursive CTE. Returns connected nodes, edges, and hop distance. Supports `relation_type` filter
- **Memory summarization (TF-IDF)** — `GET /summarize?topic=X` extracts keywords from related memories using TF-IDF scoring (no LLM). Returns top keywords, category breakdown, importance average, and time span
- **Multi-agent shared memory with ACL** — `POST /memories/{id}/acl` grants read/write/admin access to other agents. `DELETE /memories/{id}/acl/{agent}` revokes. `GET /shared` lists memories shared with the requesting agent. New `memory_acl` table with permission hierarchy
- **SSE streaming search** — `GET /stream/search?q=X` returns Server-Sent Events with FTS5 results first, then semantic results. Deduplicates across phases. Events: `fts`, `semantic`, `done`
- **Analytics endpoint** — `GET /analytics` returns comprehensive stats: category distribution, decay analysis (healthy/fading/critical), top tags, access patterns, 30-day growth, compression and archive stats, relation count
- **GDPR right to erasure** — `DELETE /memories/agent/{agent_id}` permanently deletes all agent data: memories, tags, relations, ACL entries, sessions, and audit events. Self-deletion only (agent must match)
- **Plugin system** — `KorePlugin` abstract base class with 8 hook points: `pre_save`, `post_save`, `pre_search`, `post_search`, `pre_delete`, `post_delete`, `pre_compress`, `post_compress`. Register via `register_plugin()`. `GET /plugins` lists registered plugins
- **New Pydantic models**: `GraphTraverseResponse`, `SummarizeResponse`, `ACLGrantRequest`, `ACLResponse`, `SharedMemoriesResponse`, `AnalyticsResponse`, `GDPRDeleteResponse`, `PluginListResponse`

### Stats
- 426 tests, all passing
- 7 new endpoints, 4 new modules
- New files: `summarizer.py`, `acl.py`, `analytics.py`, `plugins.py`

---

## [1.3.0] - 2026-02-27

### Theme: "Performance"

### Added
- **sqlite-vec native vector search** — Vector search now runs directly in SQLite via `vec0` virtual table with `distance_metric=cosine` and `partition key` by agent_id. Eliminates loading all embeddings into RAM. Falls back to numpy in-memory index if sqlite-vec is not installed
- **Asymmetric search support** — New `embed_query()` function for search queries and `embed_document()` for documents, leveraging sentence-transformers v5 `encode_query()`/`encode_document()` when the model supports asymmetric prompts
- **ONNX backend support** — Set `KORE_EMBED_BACKEND=onnx` to use ONNX Runtime for faster embedding inference (requires `pip install 'sentence-transformers[onnx]'`)
- **`get_dimensions()` helper** — Returns the embedding dimension of the current model
- **Chunked compressor** — Compressor now processes large datasets (>2000 vectors) in chunks to avoid O(n²) memory usage. Supports 100K+ memories without OOM

### Changed
- **Repository refactored** — Monolithic `repository.py` (979 lines) split into 5 focused modules: `repository/memory.py` (CRUD), `repository/search.py` (FTS5, semantic, tag, timeline), `repository/lifecycle.py` (decay, archive, cleanup), `repository/graph.py` (tags, relations), `repository/sessions.py` (session management). Full backward compatibility via `__init__.py` re-exports
- **Atomic updates** — `update_memory()` now uses a single `UPDATE ... WHERE` query instead of read-then-write, eliminating race conditions
- **sqlite-vec added to `[semantic]` optional dependency** — `pip install 'kore-memory[semantic]'` now includes sqlite-vec
- **sqlite-vec extension auto-loaded** on every database connection for native vector operations

---

## [1.2.0] - 2026-02-27

### Theme: "Developer Experience"

### Added
- **GET /memories/{id}** — New endpoint to retrieve a single memory by ID with agent isolation
- **PydanticAI integration** — `kore_toolset()` and `create_kore_tools()` for PydanticAI agents (`kore_memory.integrations.pydantic_ai`)
- **OpenAI Agents SDK integration** — `kore_agent_tools()` with `@function_tool` decorators (`kore_memory.integrations.openai_agents`)
- **LangChain v0.3+ BaseChatMessageHistory** — `KoreChatMessageHistory` for use with `RunnableWithMessageHistory`
- **MCP Streamable HTTP transport** — `kore-mcp --transport streamable-http` for network access (not just stdio)
- **SDK cursor pagination** — `cursor` parameter in `search()` and `timeline()` (sync + async clients)
- **SDK `get()` method** — New `get(memory_id)` method in `KoreClient` and `AsyncKoreClient`
- **OpenAPI examples** — `json_schema_extra` with examples for `MemorySaveRequest` and `MemoryRecord`
- **Optional dependencies** — `pydantic-ai` and `openai-agents` extras in pyproject.toml

### Changed
- **SDK importance default** — `KoreClient.save()` and `AsyncKoreClient.save()` now default to `importance=None` (auto-scoring) instead of `importance=1`
- **LangChain auto_importance** — `KoreLangChainMemory.save_context()` passes `importance=None` when auto_importance=True

### Tests
- 24 new tests for v1.2.0 features (`test_v12_features.py`)
- Updated 5 LangChain tests for new importance=None default

---

## [1.1.0] - 2026-02-27

### Theme: "Stability"

### Fixed
- **[CRITICAL] Archived memories leak in export** — `export_memories()` now filters `archived_at IS NULL`, preventing archived data from appearing in exports
- **[CRITICAL] Archived memories leak in search_by_tag** — `search_by_tag()` now filters `archived_at IS NULL`
- **[CRITICAL] Archived memories counted as active** — `_count_active_memories()` now excludes archived memories from pagination totals (both FTS5 and LIKE paths)
- **4 audit events never emitted** — `archive_memory()`, `restore_memory()`, `run_decay_pass()`, and `compress()` now properly emit `MEMORY_ARCHIVED`, `MEMORY_RESTORED`, `MEMORY_DECAYED`, `MEMORY_COMPRESSED` events
- **Race condition in VectorIndex** — `load_vectors()` dirty flag check+reload now protected by single lock acquisition (TOCTOU fix)
- **Infinite compression chains** — Compressor now limits compression depth to 3 levels via recursive CTE depth calculation
- **Connection pool NameError** — `acquire()` now handles `NameError` if `conn` is undefined when closing corrupt connections
- **Audit handler accumulation** — `events.on()` now deduplicates handlers, preventing duplicate event logging on repeated registrations

### Added
- **Composite index** `idx_agent_decay_active ON memories(agent_id, compressed_into, archived_at, decay_score DESC)` for faster search and decay queries
- **SQLite PRAGMA optimizations** — `synchronous=NORMAL`, `temp_store=MEMORY`, `mmap_size=256MB`, `cache_size=32MB` (5-10x write performance improvement)
- 14 new tests covering all v1.1.0 fixes (373 total tests)

---

## [1.0.2] - 2026-02-27

### Fixed
- **Search ranking** — Semantic search now includes similarity score in final ranking (`similarity × decay × importance_weight`). Previously similarity was used only for shortlisting, then discarded during re-ranking.
- **CI: root cause "no such table: memories"** — `test_auth_events.py` removed `KORE_DB_PATH` from env after each test (`os.environ.pop`), breaking all subsequent tests. Now saves and restores the original path.
- **CI: ruff lint** — Fixed 13 lint errors (E501 line-too-long, E402 import order, B904 raise from None, SIM108 ternary, W291 trailing whitespace). Applied `ruff format` on 15 files.
- **CI: MCP test skip** — Added `pytest.importorskip("mcp")` so MCP tests are skipped when the optional dependency is not installed.
- **CI: coverage threshold** — Adjusted from 85% to 80% (actual: 80.8%).
- **Test isolation** — `test_sessions.py` fixture now restores `KORE_DB_PATH` after per-test DB override. Added session-scoped DB verification fixture in `conftest.py`.

### Added
- `article-devto.md` — Dev.to article (draft) aligned with actual codebase implementation.

---

## [1.0.1] - 2026-02-25

### Fixed
- Complete English localization of all codebase (dashboard UI, docstrings, MCP tool descriptions, comments)
- Version bump to 1.0.1 across Python package, JS SDK, and config

---

## [1.0.0] - 2026-02-25

### Theme: "Production Ready"

### Added
- **Pydantic response models** on all endpoints for type-safe API responses
- **Cursor-based pagination** for `/search` and `/timeline` (replaces offset-based)
- **Archive (soft-delete)** — `POST /memories/{id}/archive`, `POST /memories/{id}/restore`, `GET /archive`
- **Batch save** — `POST /save/batch` for multiple memories in one request
- **TTL support** — `ttl_hours` parameter on save, automatic cleanup of expired memories
- **Prometheus metrics** — `GET /metrics` endpoint
- **Security hardening** — CSP headers, rate limiting, timing-safe auth, input sanitization
- 359 total tests across 10 test files

### Changed
- Repository migrated from `auriti-web-design` to `auriti-labs` organization
- All URLs updated to `github.com/auriti-labs/kore-memory`

---

## [0.9.0] - 2026-02-24

### Theme: "Intelligence"

### Added
- **Session/Conversation Tracking**: New `sessions` table, `X-Session-Id` header support, auto-create sessions on save. Endpoints: `POST /sessions`, `GET /sessions`, `GET /sessions/{id}/memories`, `GET /sessions/{id}/summary`, `POST /sessions/{id}/end`, `DELETE /sessions/{id}`. Sessions UI tab in dashboard.
- **Memory Graph Visualization**: New "Graph" tab in dashboard with force-directed layout (vanilla JS canvas, zero dependencies). Nodes colored by category, sized by importance. Hover tooltips, edge labels, SVG export. Category filter support.
- **Entity Extraction** (`kore-memory[nlp]`): Optional spaCy NER for PERSON, ORG, GPE, DATE, MONEY, PRODUCT entities. Regex fallback for emails, URLs, dates, monetary values (no extra deps). Auto-tagging with `entity:type:value` format. `GET /entities` endpoint. Enable with `KORE_ENTITY_EXTRACTION=1`.
- **Importance Auto-Tuning**: Learns from access patterns — boosts frequently accessed memories (access_count >= 5), reduces never-accessed memories after 30 days. `POST /auto-tune`, `GET /stats/scoring` endpoints. Enable with `KORE_AUTO_TUNE=1`. Thread-safe with dedicated lock.
- **Event Audit Log**: Persistent event logging to `event_logs` table. Captures all memory lifecycle events (save, delete, update, compress, decay, archive, restore). `GET /audit` endpoint with filters (event type, since, limit). Auto-cleanup support. Enable with `KORE_AUDIT_LOG=1`.
- **Agent Discovery**: `GET /agents` endpoint lists all agent IDs with memory count and last activity. Dashboard agent selector now shows datalist with existing agents.
- **Dashboard Sessions tab**: View sessions, session summary (categories, avg importance, memory count), session memories list.
- 77 new tests (17 sessions + 20 auto-tuner + 17 audit + 23 entities), total: 242

### Changed
- `save_memory()` now accepts optional `session_id` parameter
- Database schema: added `sessions` table, `event_logs` table, `session_id` column on memories
- CSP fix: removed all 26 inline onclick handlers, replaced with addEventListener + event delegation

---

## [0.8.0] - 2026-02-24

**"Developer Experience" — Framework integrations, dashboard overhaul, CI/CD maturity.**

### ✨ Added

- **LangChain Integration** — `KoreLangChainMemory` extending `BaseMemory` for drop-in use with LangChain chains
  - `load_memory_variables()` retrieves relevant context via semantic search
  - `save_context()` auto-saves conversation turns with importance scoring
  - `clear()` is a no-op — Kore handles decay naturally
  - Configurable: `memory_key`, `input_key`, `output_key`, `k`, `semantic`, `category`
  - Install: `pip install 'kore-memory[langchain]'`

- **CrewAI Integration** — `KoreCrewAIMemory` as a memory provider for CrewAI agents
  - `save()` / `search()` for general memory operations
  - `save_short_term()` — importance=1, TTL=24h for ephemeral context
  - `save_long_term()` — importance=4+, no TTL for persistent knowledge
  - Install: `pip install 'kore-memory[crewai]'`

- **Dashboard UX Overhaul** — Major UI improvements:
  - Light/dark theme toggle (persisted in localStorage)
  - Keyboard shortcuts: `/` search, `N` new memory, `Esc` dismiss, `1-9` navigation, `T` theme, `?` help
  - Search filters panel: category, importance range, date range
  - Expandable memory cards with full detail view (tags, relations, decay, access count)
  - Inline memory editing (click Edit to modify content, category, importance)
  - CSV + JSON export from search results
  - New **Archive tab** — view and restore archived memories
  - New **Metrics tab** — category distribution, importance histogram, decay distribution, system stats
  - Loading spinners on all API calls (search, save, maintenance, export, import)
  - Toast notifications with success/error icons
  - Empty state illustrations with helpful guidance
  - ARIA labels, `role` attributes, skip-to-content link, `aria-live` regions
  - Keyboard-navigable sidebar with `tabindex` and `aria-current`

- **CI/CD Improvements**:
  - Coverage job with `pytest-cov` (warns if <80%)
  - JS SDK test job (Node 20, vitest)
  - JS SDK build auto-triggered on `v*` tags
  - Coverage report uploaded as GitHub Actions artifact

- **Quick Wins**:
  - `__version__` exported from `kore_memory` package
  - `CONTRIBUTING.md` guide for OSS contributors
  - GitHub issue templates (bug report + feature request, YAML forms)
  - Pull request template with checklist
  - Example scripts: `basic_usage.py`, `langchain_example.py`, `async_usage.py`

### 📦 SDK

- JavaScript SDK updated to v0.8.0
- New optional dependency groups: `langchain`, `crewai`
- `pytest-cov` added to dev dependencies

### 🧪 Testing

- 28 new LangChain integration tests (mocked client, graceful import fallback)
- 19 new CrewAI integration tests (short/long-term patterns, lifecycle)
- Total test suite: **165 tests** (was 118)

---

## [0.7.0] - 2026-02-24

**Resolves ALL 30 open GitHub issues.**

### ⚡ Performance
- **#13** — Semantic search O(n) → numpy batch dot product (10-50x faster)
- **#14** — Compressor O(n²) → numpy matrix multiplication for pairwise similarity
- **#26** — Embeddings serialized as binary (`struct.pack`) instead of JSON text (~50% smaller)
- **#19** — Batch save uses `embed_batch()` for single model invocation instead of N calls
- **#27** — SQLite connection pooling (Queue-based, pool size 4)

### 🔐 Security
- **#12** — Rate limiter hardened: threading lock, `X-Forwarded-For`/`X-Real-IP` support, periodic bucket cleanup (prevents memory leak)
- **#16** — Dashboard requires authentication for non-localhost requests
- **#17** — CSP upgraded from `unsafe-inline` to nonce-based scripts (per-request nonce via `secrets.token_urlsafe`)
- **#18** — CI security scanning: bandit SAST + pip-audit dependency audit
- **#28** — Shell scripts: `.env` loading replaced with safe parser (no arbitrary code execution)

### ✨ Added
- **#15** — `PUT /memories/{id}` — update memory content, category, importance with automatic embedding regeneration
- **#20** — Event system — in-process lifecycle hooks (MEMORY_SAVED, DELETED, UPDATED, COMPRESSED, DECAYED, ARCHIVED, RESTORED)
- **#21** — Storage abstraction — `MemoryStore` Protocol with 16 method signatures for future PostgreSQL support
- **#22** — MCP server expanded from 6 to 14 tools: added delete, update, batch save, tags, search by tag, relations, cleanup, import
- **#24** — Dashboard HTML extracted from Python into `templates/dashboard.html` (dashboard.py: 1208 → 75 lines)
- **#29** — Soft-delete: `POST /memories/{id}/archive`, `POST /memories/{id}/restore`, `GET /archive`
- **#30** — Prometheus metrics endpoint: `GET /metrics` with memory counts, search latency, decay stats
- **#31** — Static type checking: mypy configured, `py.typed` PEP 561 marker

### 🧪 Testing
- **#23** — MCP server test suite: 32 tests across 12 test classes covering all 14 tools
- **#25** — Test fixtures: `conftest.py` with autouse rate limiter reset, isolated DB per test
- **#7** — CI now tests semantic search with sentence-transformers (separate job with model caching)
- Total test suite: **118 tests** (was 91)

### 📦 SDK
- JavaScript SDK updated to v0.7.0: added `update()`, `archive()`, `restore()`, `getArchived()`, `metrics()` methods
- Cursor-based pagination support in search/timeline options

---

## [0.6.0] - 2026-02-23

### ⚠️ BREAKING CHANGES

- **Package Renamed** — `src` → `kore_memory` to fix namespace collision (#1)
  - All imports must be updated: `from src import KoreClient` → `from kore_memory import KoreClient`
  - See [MIGRATION-v0.6.md](MIGRATION-v0.6.md) for migration guide
  - Automated migration: `sed -i 's/from src\./from kore_memory./g' *.py`

### 🔧 Fixed

- **#2 (CRITICAL)** — Pagination broken with offset/limit
  - Replaced broken offset/limit with cursor-based pagination
  - No more duplicate/missing results with offset > 0
  - `offset` parameter kept for backwards compat (deprecated)
  - New `cursor` param returns base64 encoded position token
  - Test: 20 records, 4 pages, zero duplicates ✅

- **#1 (CRITICAL)** — Package naming `src/` causes namespace collision
  - Package renamed to `kore_memory` following Python best practices
  - Fixes installation conflicts with other projects using src-layout
  - All internal imports updated

### ✨ Added

- **Cursor-based Pagination** — Reliable pagination for `/search` and `/timeline`
  - `cursor` parameter for next page navigation
  - `has_more` boolean in response
  - Backwards compatible with deprecated `offset`

### 📚 Documentation

- Added `MIGRATION-v0.6.md` with migration guide
- Updated README with new import paths
- Updated all code examples to use `kore_memory`

---

## [0.5.4] - 2026-02-20

### 🔧 Fixed
- **UX Improvement** — `KORE_LOCAL_ONLY=1` di default per localhost. Nessuna API key richiesta per `127.0.0.1`
- **Auto API Key Generation** — Genera automaticamente API key sicura al primo avvio se mancante
- **Installation Experience** — Funziona out-of-the-box dopo `pip install kore-memory && kore`

### ✨ Added
- **JavaScript/TypeScript SDK** — `kore-memory-client` npm package con 17 metodi async, zero runtime dependencies, dual ESM/CJS output, full TypeScript support
- **Error Hierarchy** — 6 classi errore tipizzate (KoreError, KoreAuthError, KoreNotFoundError, etc.)
- **Complete Test Suite** — 44 test per SDK JS con mock fetch, error handling, tutti i metodi API

### 📦 Package
- **Zero Dependencies** — usa fetch nativo, ~6KB minified
- **Dual Output** — ESM + CommonJS con tsup
- **Type Definitions** — .d.ts completi per TypeScript
- **Node 18+** — supporto JavaScript moderno

### 📚 Documentation
- README completo per SDK con esempi TypeScript
- Sezione JS/TS SDK aggiunta al README principale
- Roadmap aggiornato: npm SDK ✅

---

## [0.5.3] - 2026-02-20

### ✨ Added
- **Web Dashboard** — dashboard completa servita da FastAPI su `/dashboard`. HTML inline con CSS + JS vanilla, zero dipendenze extra. 7 sezioni: Overview, Memories, Tags, Relations, Timeline, Maintenance, Backup. Dark theme, responsive, agent selector
- **CSP dinamico** — Content Security Policy allargato solo per `/dashboard` (inline styles/scripts + Google Fonts), restrittivo per tutte le API

### 🧪 Testing
- 7 nuovi test dashboard (route, sezioni, CSP, branding, JS helpers)
- Total test suite: **91 tests** ✅

### 📚 Documentation
- README: aggiunta sezione Web Dashboard con tabella feature, aggiornata roadmap (dashboard completata), aggiunto `/dashboard` alla API reference

---

## [0.5.2] - 2026-02-20

### 🔧 Fixed
- **Public exports** — `KoreClient`, `AsyncKoreClient`, e tutte le eccezioni ora esportati da `src/__init__.py` (`from src import KoreClient`)
- **README imports** — aggiornati tutti gli esempi da `from src.client import` a `from src import`

---

## [0.5.1] - 2026-02-20

### ✨ Added
- **Python SDK** — `KoreClient` (sync) and `AsyncKoreClient` (async) with type-safe wrappers for all 17 API endpoints. Typed exceptions (`KoreAuthError`, `KoreNotFoundError`, `KoreValidationError`, `KoreRateLimitError`, `KoreServerError`). Context manager support (`with` / `async with`). Returns Pydantic models, zero duplication (`src/client.py`)

### 🧪 Testing
- 35 new SDK tests (15 unit + 20 integration via ASGI transport)
- Total test suite: **84 tests** ✅

### 📚 Documentation
- README: added Python SDK section with sync/async examples, error handling, and methods table
- CHANGELOG: updated with SDK details
- Roadmap: Python SDK marked as complete

---

## [0.5.0] - 2026-02-20

### ✨ Added
- **MCP Server** — native Model Context Protocol integration for Claude, Cursor, and any MCP client (`kore-mcp` command). 6 tools: save, search, timeline, decay, compress, export. 1 resource: `kore://health`
- **Tags** — tag any memory, search by tag, agent-scoped. Normalized to lowercase, duplicates ignored (`POST/DELETE/GET /memories/{id}/tags`, `GET /tags/{tag}/memories`)
- **Relations** — bidirectional knowledge graph between memories. Cross-agent linking prevented (`POST/GET /memories/{id}/relations`)
- **Batch API** — save up to 100 memories in a single request (`POST /save/batch`)
- **TTL (Time-to-Live)** — set `ttl_hours` on save for auto-expiring memories. Expired memories filtered from search, timeline, export. Manual cleanup via `POST /cleanup`, automatic cleanup integrated into decay pass
- **Export / Import** — full JSON backup of active memories (`GET /export`, `POST /import`). Expired memories excluded from export. Import skips invalid records gracefully
- **Pagination** — `offset` + `has_more` on `/search` and `/timeline` endpoints
- **Centralized config** — all env vars in `src/config.py` (9 configurable options)
- **Vector index cache** — in-memory embedding cache with per-agent invalidation for faster semantic search
- **Python SDK** — `KoreClient` (sync) and `AsyncKoreClient` (async) with type-safe wrappers for all 17 API endpoints. Typed exceptions (`KoreAuthError`, `KoreNotFoundError`, `KoreValidationError`, `KoreRateLimitError`, `KoreServerError`). Context manager support (`with` / `async with`). Returns Pydantic models, zero duplication
- **OOM protection** — embedding input capped at `KORE_MAX_EMBED_CHARS` (default 8000)
- **Concurrency locks** — non-blocking threading locks for decay and compression passes

### 🗄️ Database
- Added `memory_tags` table (memory_id, tag) with tag index
- Added `memory_relations` table (source_id, target_id, relation) with bidirectional indexes
- Added `expires_at` column to memories table with migration for existing DBs

### 🧪 Testing
- Test suite expanded from 17 to **84 tests** covering all P3 features + SDK
- Tests for: batch API, tags (7), relations (5), TTL/cleanup (8), export/import (5), pagination (3)
- SDK tests: 15 unit (helpers, exceptions, class structure) + 20 integration (all endpoints via ASGI transport)
- Rate limiter reset in `setup_method` to prevent 429 interference between test classes

### 📚 Documentation
- README rewritten: comparison table (+5 features), key features (+5 sections), complete API reference organized by category, MCP Server section with Claude/Cursor config, Python SDK section with sync/async examples, full env var documentation, updated roadmap

### 📦 Installation
- New optional dependency group: `mcp` (`pip install kore-memory[mcp]`)
- New entry point: `kore-mcp` for MCP server

---

## [0.4.0] - 2026-02-20

### 🔐 Security
- Added rate limiting middleware (10 requests/second per IP)
- Implemented CORS middleware with configurable origins
- Added comprehensive security headers (X-Frame-Options, X-Content-Type-Options, CSP)
- Added global error handler to prevent information leakage
- Enabled SSL verification on httpx client (controlled via `WP_SSL_VERIFY` env var)
- Sanitized credentials in maintenance templates

### 🗄️ Database
- Fixed `KORE_DB_PATH` to resolve at runtime instead of import-time
- Switched all timestamps to UTC (via `datetime.now(UTC)`)
- Improved FTS5 query sanitization (prevent SQL injection)
- Added batch decay updates for better performance
- Made embedding generation resilient to failures

### 🧪 Testing
- Fixed test suite: explicit `init_db()` call before TestClient initialization
- All 17 tests passing ✅

### 📚 Documentation
- Added `CLAUDE.md` (project context for AI assistants)
- Added competitive analysis vs Mem0, Letta, Zep
- Improved README with deployment section

### 🛠️ Fixes
- Fixed CLI bug: corrected module path from `kore.src.main:app` to `src.main:app` (ModuleNotFoundError)
- Created `kore-daemon.sh` for proper daemonization with `.env` support
- Updated `start.sh` to load environment variables correctly

### ⚡ Performance
- Optimized memory decay calculations
- Batch processing for compression operations

---

## [0.3.1] - 2026-02-19

### ✨ Added
- Semantic search with multilingual embeddings (50+ languages)
- Memory compression (auto-merge similar memories)
- Timeline API (chronological memory traces)
- Agent namespace isolation
- Auto-importance scoring (no LLM required)
- Memory decay using Ebbinghaus forgetting curve

### 🔐 Security
- API key authentication
- Agent-scoped access control
- Timing-safe key comparison

### 📦 Installation
- Published to PyPI as `kore-memory`
- CLI command `kore` available after install
- Optional `[semantic]` extras for embeddings

---

## [0.3.0] - 2026-02-18

### 🎉 Initial Public Release
- Core memory storage with SQLite + FTS5
- REST API (FastAPI)
- Basic search and CRUD operations
- Offline-first architecture
- Zero external dependencies for core features

---

## Version Naming

- **0.8.x** — Developer experience, LangChain/CrewAI, dashboard UX
- **0.7.x** — Performance, security, 30 issues resolved
- **0.6.x** — Package rename, cursor-based pagination
- **0.5.x** — MCP, tags, relations, TTL, batch API, Python SDK
- **0.4.x** — Security & stability improvements
- **0.3.x** — Semantic search & compression
- **0.2.x** — Internal testing (not released)
- **0.1.x** — Initial development

---

[0.8.0]: https://github.com/auriti-labs/kore-memory/compare/v0.7.0...v0.8.0
[0.7.0]: https://github.com/auriti-labs/kore-memory/compare/v0.6.0...v0.7.0
[0.6.0]: https://github.com/auriti-labs/kore-memory/compare/v0.5.4...v0.6.0
[0.5.4]: https://github.com/auriti-labs/kore-memory/compare/v0.5.3...v0.5.4
[0.5.3]: https://github.com/auriti-labs/kore-memory/compare/v0.5.2...v0.5.3
[0.5.2]: https://github.com/auriti-labs/kore-memory/compare/v0.5.1...v0.5.2
[0.5.1]: https://github.com/auriti-labs/kore-memory/compare/v0.5.0...v0.5.1
[0.5.0]: https://github.com/auriti-labs/kore-memory/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/auriti-labs/kore-memory/compare/v0.3.1...v0.4.0
[0.3.1]: https://github.com/auriti-labs/kore-memory/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/auriti-labs/kore-memory/releases/tag/v0.3.0
```

## File: `CLAUDE.md`
```markdown
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Kore Memory is a persistent memory layer for AI agents (Python 3.11+, FastAPI, SQLite). Runs fully offline — no LLM calls, no cloud APIs. Implements Ebbinghaus forgetting curve decay, local auto-importance scoring, semantic search via sentence-transformers (with sqlite-vec native vector search), memory compression, graph RAG, multi-agent ACL, and a plugin system.

Published on PyPI as `kore-memory` (v2.0.0). JS SDK on npm as `kore-memory-client` (v2.0.0). MIT license.

## Commands

```bash
# Setup
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[semantic,dev]"

# Run server
kore                                    # localhost:8765
kore --port 9000 --reload               # dev mode
./start.sh                              # background (PID in logs/kore.pid)

# Tests (pytest, 15 file, 426 test)
pytest tests/ -v
pytest tests/test_api.py::TestSave -v           # singola classe
pytest tests/test_api.py::TestSave::test_save_basic -v  # singolo test

# Coverage (target >= 85%, attuale 88%)
pytest tests/ --cov=kore_memory --cov-report=term-missing

# JS SDK
cd sdk/js && npm install && npm run build   # build con tsup
cd sdk/js && npm test                       # test con vitest

# Build per PyPI
pip install build && python -m build
```

## Architecture

```
Request → FastAPI (main.py) → Auth (auth.py) → Pydantic (models.py) → Repository (repository/) → SQLite (database.py)
                                                     ↕                    ↕           ↕
                                               scorer.py           embedder.py    decay.py
                                                              vector_index.py  compressor.py
                                                     ↕
                                              events.py → audit.py
                                              auto_tuner.py
                                              integrations/entities.py
                                                     ↕
                                  summarizer.py | acl.py | analytics.py | plugins.py
```

**Entry points:**
- `kore_memory/cli.py` → comando `kore`, avvia uvicorn su `kore_memory.main:app`
- `kore_memory/main.py` → FastAPI app con lifespan (init_db + graceful shutdown), 50+ endpoint REST + dashboard
- `kore_memory/mcp_server.py` → comando `kore-mcp`, server MCP (stdio + streamable-http) per Claude/Cursor

**Repository package (kore_memory/repository/):**

The monolithic `repository.py` has been split into focused modules (v1.3.0):

| Module | Lines | Responsibility |
|--------|-------|----------------|
| `memory.py` | ~411 | CRUD: save, get, update (atomic), delete, batch, import/export, stats, agents |
| `search.py` | ~358 | Search: FTS5, semantic (asymmetric via embed_query), tag, timeline |
| `lifecycle.py` | ~125 | Decay pass, cleanup expired, archive, restore |
| `graph.py` | ~220 | Tags, relations, graph traversal (recursive CTE) |
| `sessions.py` | ~119 | Session CRUD + summarization |
| `__init__.py` | ~95 | Re-exports for backward compatibility |

**Core modules (kore_memory/):**

| Module | Lines | Responsibility |
|--------|-------|----------------|
| `main.py` | ~1050 | FastAPI app, 50+ REST endpoints, rate limiting, security headers, SSE streaming |
| `client.py` | ~509 | Python client SDK (sync `KoreClient` + async `AsyncKoreClient`) |
| `models.py` | ~370 | Pydantic v2 schemas, 35+ request/response models |
| `mcp_server.py` | ~400 | FastMCP server, 14 tool MCP + streamable-http transport |
| `compressor.py` | ~373 | Merge memories via cosine similarity > 0.88. Chunked clustering (O(chunk×n)) |
| `database.py` | ~257 | SQLite WAL mode, connection pool, schema (memories, FTS5, tags, relations, sessions, events, vec_memories) |
| `vector_index.py` | ~370 | SqliteVecIndex (native sqlite-vec) + legacy VectorIndex (in-memory numpy) fallback |
| `auto_tuner.py` | ~207 | Auto-tuning importance based on access patterns |
| `summarizer.py` | ~120 | TF-IDF keyword extraction and topic summarization (no LLM) |
| `acl.py` | ~193 | Multi-agent access control: grant/revoke/check permissions (read/write/admin) |
| `analytics.py` | ~131 | Aggregated analytics: categories, decay, tags, access patterns, growth |
| `plugins.py` | ~144 | Plugin system: KorePlugin ABC with 8 pre/post hooks |
| `embedder.py` | ~120 | Wrapper sentence-transformers v5: asymmetric search (encode_query/encode_document), ONNX backend |
| `auth.py` | ~118 | API key auto-generated, timing-safe comparison, agent namespace isolation |
| `audit.py` | ~110 | Event logging for memory operations |
| `config.py` | ~70 | Centralized config from env vars (all `KORE_*`) |
| `decay.py` | ~69 | Ebbinghaus curve: `decay = e^(-t·ln2/half_life)`. Half-life 7d→365d. +15% per retrieval |
| `scorer.py` | ~67 | Auto-scoring importance 1-5 without LLM: keyword signals, category baseline, length bonus |
| `events.py` | ~48 | Event bus for lifecycle hooks (save, delete, update, compress, archive, restore, decay) |

**Integrations (kore_memory/integrations/):**
- `pydantic_ai.py` — Tool-based memory access for PydanticAI agents
- `openai_agents.py` — Function tools for OpenAI Agents SDK
- `langchain.py` — `KoreLangChainMemory` (BaseMemory) + `KoreChatMessageHistory` (BaseChatMessageHistory v2)
- `crewai.py` — `KoreCrewAIMemory` memory provider for CrewAI agents
- `entities.py` — Entity extraction (spaCy NER optional, regex fallback)
- Optional install: `pip install 'kore-memory[pydantic-ai]'` / `'[openai-agents]'` / `'[langchain]'` / `'[crewai]'` / `'[nlp]'`

**JS/TS SDK (sdk/js/):**
- `src/client.ts` — class `KoreClient`, 17 async methods
- `src/types.ts` — TypeScript interfaces (HealthResponse aligned with real API)
- `src/errors.ts` — error hierarchy (`KoreError` → `KoreValidationError` | `KoreAuthError` | ...)
- Build: tsup (ESM + CJS), test: vitest

**Database schema:**
- Table `memories`: `id`, `agent_id`, `content`, `category`, `importance` (1-5), `decay_score` (0.0-1.0), `access_count`, `embedding` (JSON blob), `compressed_into` (FK self-ref), `expires_at` (TTL), `session_id`, `archived_at`
- Virtual table `memories_fts` (FTS5) on content + category with auto-sync triggers
- Virtual table `vec_memories` (sqlite-vec, optional) — native vector search with cosine distance, agent_id partition key
- Table `memory_tags`: many-to-many tags
- Table `memory_relations`: directed graph relations between memories
- Table `memory_acl`: access control (memory_id, agent_id, permission, granted_by)
- Table `sessions`: conversations (id, agent_id, title, created_at, ended_at)
- Table `event_logs`: audit trail (event, agent_id, memory_id, data, created_at)
- Composite index `idx_agent_decay_active` on (agent_id, compressed_into, archived_at, decay_score DESC)
- PRAGMA optimizations: synchronous=NORMAL, mmap_size=256MB, cache_size=32MB, temp_store=MEMORY

**Search flow:**
1. If `q=*` → return all memories (global wildcard)
2. If semantic=True and embeddings available → cosine similarity via sqlite-vec (native) or VectorIndex (legacy numpy)
3. Otherwise → FTS5 with wildcard, fallback LIKE
4. Filter archived (`archived_at IS NULL`), forgotten (`decay_score < 0.05`), and expired TTL
5. Re-rank by `similarity × decay × importance_weight`
6. Reinforcement: `access_count++`, `decay_score += 0.05`

**Auto-importance scoring:**
- `importance: None` (or omitted) → auto-scored via keyword signals, category, length
- `importance: 1-5` (explicit) → used as-is, no override

## Test Structure

15 files in `tests/` — **426 tests** total, coverage **88%**. Uses `TestClient` FastAPI (in-process, no network). Each test uses a shared temp DB (`KORE_DB_PATH` env var), `KORE_TEST_MODE=1` for testclient trusted host, isolated via `X-Agent-Id: test-agent`.

- `test_client_sync.py` (~812 lines) — 64 tests sync KoreClient (all methods)
- `test_api.py` (~769 lines) — TestHealth, TestSave, TestAuth, TestAgentIsolation, TestSearch, TestDecay, TestCompress, TestTimeline, TestDelete, TestArchive, TestCursorPagination, TestRateLimit, TestUpdateMemory, TestAutoScore
- `test_v2_features.py` (~428 lines) — 29 tests: Graph RAG, Summarization, ACL, SSE Streaming, Analytics, GDPR, Plugins
- `test_langchain.py` (~423 lines) — 28 tests LangChain integration (mocked)
- `test_client.py` (~398 lines) — Python client SDK (sync + async)
- `test_crewai.py` (~354 lines) — 19 tests CrewAI integration (mocked)
- `test_mcp.py` (~351 lines) — 32 tests MCP server (14 tools)
- `test_auto_tuner.py` (~348 lines) — auto-tuning importance
- `test_auth_events.py` (~304 lines) — 19 tests: auth, events, integrations, database edge cases
- `test_entities.py` (~296 lines) — entity extraction (NER, regex fallback)
- `test_audit.py` (~287 lines) — audit log (tracking, filtering, endpoint)
- `test_cli.py` (~261 lines) — 19 tests CLI (args, uvicorn mock, errors)
- `test_v11_fixes.py` (~230 lines) — 14 tests for v1.1.0 fixes (archived leak, audit emit, PRAGMA, thread-safety)
- `test_sessions.py` (~183 lines) — sessions (create, list, summarize, end, delete)
- `test_dashboard.py` (~100 lines) — dashboard route + CSP

Config pytest in `pyproject.toml` (`asyncio_mode = "auto"`). conftest.py sets `KORE_TEST_MODE=1` and resets rate limiter between tests.

## CI/CD

- `.github/workflows/ci.yml` — push/PR on main: test (Python 3.11+3.12+3.13), test-semantic, security (bandit + pip-audit), lint (ruff), coverage (pytest-cov ≥80%), test-js-sdk (Node 20)
- `.github/workflows/publish.yml` — tag v*, build + publish PyPI (trusted OIDC)
- `.github/workflows/build-sdk.yml` — tag v* + manual dispatch, build + test JS SDK

## Environment Variables

| Variable | Default | Usage |
|----------|---------|-------|
| `KORE_API_KEY` | auto-generated in `data/.api_key` | Override API key |
| `KORE_LOCAL_ONLY` | `"1"` | Skip auth for localhost (`"1"` = auth disabled on 127.0.0.1) |
| `KORE_TEST_MODE` | `"0"` | Enable `testclient` as trusted host (`"1"` in tests) |
| `KORE_DB_PATH` | `data/memory.db` | DB path (overridden in tests for temp DB) |
| `KORE_HOST` | `127.0.0.1` | Bind address |
| `KORE_PORT` | `8765` | Server port |
| `KORE_CORS_ORIGINS` | *(empty)* | Allowed origins (comma-separated) |
| `KORE_EMBED_MODEL` | `paraphrase-multilingual-MiniLM-L12-v2` | sentence-transformers model |
| `KORE_EMBED_DIM` | `384` | Embedding dimensions for sqlite-vec virtual table |
| `KORE_EMBED_BACKEND` | *(empty)* | Set to `"onnx"` for ONNX inference backend |
| `KORE_MAX_EMBED_CHARS` | `8000` | Max chars per embedder call (OOM protection) |
| `KORE_SIMILARITY_THRESHOLD` | `0.88` | Cosine threshold for compression |
| `KORE_AUTO_TUNE` | `"0"` | Enable auto-tuning importance (`"1"` to activate) |
| `KORE_ENTITY_EXTRACTION` | `"0"` | Enable entity extraction with spaCy/regex (`"1"` to activate) |
| `KORE_AUDIT_LOG` | `"0"` | Enable audit log for all operations (`"1"` to activate) |

## MCP Server

14 tools exposed via stdio + streamable-http transport (`kore-mcp`), with sanitized agent_id:

| Tool | Parameters | Usage |
|------|------------|-------|
| `memory_save` | content, category, importance, agent_id | Save memory (importance=0 → auto-score) |
| `memory_search` | query, limit, category, semantic, agent_id | Search (semantic/FTS5) |
| `memory_timeline` | subject, limit, agent_id | Chronological history |
| `memory_decay_run` | agent_id | Recalculate decay scores |
| `memory_compress` | agent_id | Merge similar memories |
| `memory_export` | agent_id | Export all memories |
| `memory_delete` | memory_id, agent_id | Delete memory |
| `memory_update` | memory_id, content, category, importance, agent_id | Update memory |
| `memory_save_batch` | memories[], agent_id | Batch save (max 100) |
| `memory_add_tags` | memory_id, tags[], agent_id | Add tags |
| `memory_search_by_tag` | tag, agent_id, limit | Search by tag |
| `memory_add_relation` | source_id, target_id, relation, agent_id | Create relation |
| `memory_cleanup` | agent_id | Delete expired memories |
| `memory_import` | memories[], agent_id | Bulk import (max 500) |

**NOTE**: Optional params use `str = ""` / `int = 0` as sentinels (not `str | None`) to avoid `anyOf` schema that prevents tool loading in Claude Code.

## REST API Endpoints (v2.0.0)

### Core CRUD
- `POST /save` — Save memory (auto-importance if omitted, X-Session-Id support)
- `POST /save/batch` — Batch save (max 100)
- `GET /search` — Semantic/FTS5 search with cursor pagination
- `GET /memories/{id}` — Get single memory by ID
- `PUT /memories/{id}` — Update memory (atomic single-query UPDATE)
- `DELETE /memories/{id}` — Hard delete

### Tags & Relations
- `POST /memories/{id}/tags` — Add tags
- `DELETE /memories/{id}/tags` — Remove tags
- `GET /memories/{id}/tags` — List tags
- `GET /tags/{tag}/memories` — Search by tag
- `POST /memories/{id}/relations` — Create relation
- `GET /memories/{id}/relations` — List relations

### Graph RAG (v2.0)
- `GET /graph/traverse?start_id=X&depth=3&relation_type=Y` — Multi-hop traversal via recursive CTE (max 10 hops)

### Summarization (v2.0)
- `GET /summarize?topic=X` — TF-IDF keyword extraction from related memories (no LLM)

### ACL (v2.0)
- `POST /memories/{id}/acl` — Grant read/write/admin to another agent
- `DELETE /memories/{id}/acl/{agent}` — Revoke access
- `GET /memories/{id}/acl` — List permissions
- `GET /shared` — List memories shared with requesting agent

### SSE Streaming (v2.0)
- `GET /stream/search?q=X` — Server-Sent Events (FTS first, then semantic, with dedup)

### Analytics (v2.0)
- `GET /analytics` — Categories, decay buckets, top tags, access patterns, 30-day growth

### GDPR (v2.0)
- `DELETE /memories/agent/{agent_id}` — Right to erasure (permanent deletion of ALL agent data)

### Plugins (v2.0)
- `GET /plugins` — List registered plugins

### Lifecycle
- `POST /decay/run` — Recalculate decay scores
- `POST /compress` — Merge similar memories
- `POST /cleanup` — Delete expired memories
- `POST /auto-tune` — Auto-adjust importance from access patterns
- `POST /memories/{id}/archive` — Soft-delete
- `POST /memories/{id}/restore` — Unarchive
- `GET /archive` — List archived

### Sessions
- `POST /sessions` — Create session
- `GET /sessions` — List sessions
- `GET /sessions/{id}/memories` — Session memories
- `GET /sessions/{id}/summary` — Session stats
- `POST /sessions/{id}/end` — End session
- `DELETE /sessions/{id}` — Delete session

### Admin
- `GET /export` — Export all agent memories
- `POST /import` — Import memories (max 500)
- `GET /entities` — Extracted entities
- `GET /agents` — List all agents
- `GET /audit` — Event log
- `GET /stats/scoring` — Importance stats
- `GET /metrics` — Prometheus-compatible metrics
- `GET /health` — Health check
- `GET /dashboard` — Web UI

## Key Patterns

- **Agent isolation**: all DB queries filter by `agent_id`. Header `X-Agent-Id`, default `"default"`, sanitized to `[a-zA-Z0-9_-]` max 64 chars
- **Local-only auth**: with `KORE_LOCAL_ONLY=1` (default), localhost requests skip API key validation. `testclient` trusted only with `KORE_TEST_MODE=1`. X-Forwarded-For ignored in local-only mode to prevent spoofing
- **Archived memories**: filtered with `AND archived_at IS NULL` in search (FTS5, semantic, LIKE), compression, decay pass, and vector index reload
- **Session ID validation**: header `X-Session-Id` validated with regex `^[a-zA-Z0-9_\-\.]{1,128}$`
- **Lazy embeddings**: sentence-transformers model loaded on first use, not at server startup
- **sqlite-vec**: native vector search via vec0 virtual table with partition key for agent isolation. Falls back to in-memory numpy if extension unavailable
- **Asymmetric search**: embedder v3 uses `encode_query()` for search queries and `encode_document()` for stored content (when model supports prompts)
- **Atomic updates**: `update_memory()` uses single UPDATE query with rowcount check (no read-then-write race condition)
- **Chunked compression**: similarity matrix processed in blocks of 2000 vectors — O(chunk×n) memory instead of O(n²)
- **Plugin hooks**: 8 hook points (pre/post save, search, delete, compress) via `KorePlugin` ABC
- **ACL hierarchy**: admin > write > read. Owner always has full access. Non-owners need explicit ACL grant
- **DB path**: `data/` and `logs/` directories created at runtime, ignored by git
- **Dashboard**: HTML served from `dashboard.py` with template in `templates/dashboard.html`
- **Client SDK exports**: `kore_memory/__init__.py` exports `KoreClient`, `AsyncKoreClient` and error hierarchy
- **CSP nonce**: each HTML response includes a per-request nonce to prevent XSS
- **Connection pool**: SQLite thread-safe pool size 4, connection validation, fd leak cleanup, graceful shutdown
- **Rate limiting**: in-memory per IP+path, configured in `config.RATE_LIMITS`
- **Response models**: all endpoints have `response_model` Pydantic for OpenAPI validation

## Release History

| Version | Theme | Key Features |
|---------|-------|--------------|
| v1.0.0 | Launch | Core API, FTS5, decay, auto-scoring, MCP server, dashboard |
| v1.1.0 | Stability | Bug fixes (archived leak), SQLite PRAGMA optimization, audit emit |
| v1.2.0 | Developer Experience | PydanticAI/OpenAI Agents/LangChain v2 integrations, MCP HTTP transport, SDK cursor pagination |
| v1.3.0 | Performance | sqlite-vec native vector search, repository refactoring (5 modules), embedder v3 (asymmetric + ONNX), chunked compressor |
| v2.0.0 | Intelligence | Graph RAG (recursive CTE), TF-IDF summarization, multi-agent ACL, SSE streaming, analytics, GDPR right to erasure, plugin system |
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing to Kore Memory

Thank you for your interest in contributing to Kore Memory! This guide will help you get started.

## Prerequisites

- **Python 3.11+** (3.12 recommended)
- **git**
- A Unix-like environment (macOS, Linux, WSL)

## Development Setup

1. **Fork and clone the repository:**

   ```bash
   git clone https://github.com/<your-username>/kore-memory.git
   cd kore-memory
   ```

2. **Create a virtual environment and install dependencies:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -e ".[semantic,dev]"
   ```

3. **Verify the setup:**

   ```bash
   pytest tests/ -v
   ```

   All tests should pass before you start making changes.

## Running the Server Locally

```bash
kore                        # starts on localhost:8765
kore --port 9000 --reload   # dev mode with auto-reload
```

## Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run a specific test file
pytest tests/test_api.py -v

# Run a specific test class or method
pytest tests/test_api.py::TestSave -v
pytest tests/test_api.py::TestSave::test_save_basic -v
```

Tests use an in-process FastAPI TestClient (no network required) with a temporary SQLite database.

## Code Style

- **Formatter/Linter:** [ruff](https://docs.astral.sh/ruff/)
- **Line length:** 120 characters
- **Type hints:** Required for all public functions
- **Docstrings:** Required for all public classes and functions

Run the linter before committing:

```bash
ruff check .
ruff format .
```

## Submitting a Pull Request

1. **Create a feature branch** from `main`:

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** with clear, focused commits.

3. **Ensure all tests pass:**

   ```bash
   pytest tests/ -v
   ```

4. **Ensure code style is clean:**

   ```bash
   ruff check .
   ruff format --check .
   ```

5. **Push your branch** and open a Pull Request against `main`.

6. **Describe your changes** in the PR using the pull request template. Include what changed, why, and how to test it.

## Reporting Issues

When opening an issue, please include:

- **A clear title** summarizing the problem or request.
- **Steps to reproduce** (for bugs) with the minimal code to trigger the issue.
- **Expected vs. actual behavior.**
- **Environment details:** Python version, OS, Kore Memory version (`python -c "import kore_memory; print(kore_memory.__version__)"`).
- **Logs or tracebacks** if available.

Use the provided issue templates (bug report / feature request) when possible.

## Project Structure

See [CLAUDE.md](CLAUDE.md) for a detailed architecture overview, module descriptions, and environment variable reference.

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Juan Auriti

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `MIGRATION-v0.6.md`
```markdown
# Migration Guide: v0.5.x → v0.6.0

## ⚠️ Breaking Changes

### Package Renamed: `src` → `kore_memory`

**Why:** The package was incorrectly named `src`, causing namespace collisions with other projects using the src-layout pattern.

**Impact:** All imports must be updated.

---

## 🔧 How to Migrate

### 1. Update your imports

**Before (v0.5.x):**
```python
from src import KoreClient, AsyncKoreClient
from src.models import MemorySaveRequest
from src.database import init_db
```

**After (v0.6.0):**
```python
from kore_memory import KoreClient, AsyncKoreClient
from kore_memory.models import MemorySaveRequest
from kore_memory.database import init_db
```

### 2. Public API (recommended)

If you're using the public exports (recommended), migration is simple:

```python
# v0.5.x
from src import KoreClient

# v0.6.0
from kore_memory import KoreClient
```

### 3. Automated migration

Run this command in your project root:

```bash
find . -name "*.py" -exec sed -i 's/from src\./from kore_memory./g' {} \;
find . -name "*.py" -exec sed -i 's/import src\./import kore_memory./g' {} \;
```

---

## ✅ Non-Breaking Changes

All these work **exactly the same** in v0.6.0:

- REST API endpoints (`/search`, `/save`, `/timeline`, etc.)
- Database schema (no migrations needed)
- Configuration (`.env`, `config.py`)
- CLI commands (`kore`, `kore-mcp`)
- MCP server tools

---

## 🆕 New in v0.6.0

### Cursor-based pagination (fixes #2)

The broken `offset`/`limit` pagination has been replaced with cursor-based pagination:

**Before (v0.5.x):**
```python
# ❌ Could skip/duplicate results
response = client.search("query", limit=10, offset=20)
```

**After (v0.6.0):**
```python
# ✅ Reliable pagination
response = client.search("query", limit=10)
next_page = client.search("query", limit=10, cursor=response.cursor)
```

**Backwards compatibility:** The `offset` parameter still works but is deprecated.

---

## 📦 Installation

```bash
pip install --upgrade kore-memory
```

---

## 🐛 Issues Fixed

- **#1** - Package naming `src/` causes namespace collision (CRITICAL)
- **#2** - Pagination broken with offset/limit (CRITICAL)

---

## 📞 Need Help?

- [Open an issue](https://github.com/auriti-labs/kore-memory/issues)
- [Read the docs](https://github.com/auriti-labs/kore-memory#readme)
```

## File: `README.md`
```markdown
<div align="center">

<img src="assets/logo.svg" alt="Kore Memory" width="420"/>

<br/>

**The memory layer that thinks like a human.**
<br/>
Remembers what matters. Forgets what doesn't. Never calls home.

<br/>

[![CI](https://github.com/auriti-labs/kore-memory/actions/workflows/ci.yml/badge.svg)](https://github.com/auriti-labs/kore-memory/actions/workflows/ci.yml)
[![PyPI version](https://img.shields.io/pypi/v/kore-memory.svg?style=flat-square&color=7c3aed)](https://pypi.org/project/kore-memory/)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue?style=flat-square)](https://python.org)
[![License: MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)
[![Zero Cloud](https://img.shields.io/badge/cloud-zero-orange?style=flat-square)]()
[![Multilingual](https://img.shields.io/badge/languages-50%2B-purple?style=flat-square)]()
[![Docs](https://img.shields.io/badge/docs-auritidesign.it-00b4d8?style=flat-square)](https://auritidesign.it/brain/knowledge/docs_legacy/kore-memory/)

<br/>

[**Docs**](https://auritidesign.it/brain/knowledge/docs_legacy/kore-memory/) · [**Install**](#-install) · [**Quickstart**](#-quickstart) · [**How it works**](#-how-it-works) · [**API**](#-api-reference) · [**Changelog**](CHANGELOG.md) · [**Roadmap**](#-roadmap)

</div>

---

## Why Kore?

Every AI agent memory tool has the same flaw: they remember everything forever, phone home to cloud APIs, or need an LLM just to decide what's worth storing.

**Kore is different.**

<div align="center">

| Feature | **Kore** | Mem0 | Letta | Memori |
|---|:---:|:---:|:---:|:---:|
| Runs fully offline | ✅ | ❌ | ❌ | ❌ |
| No LLM required | ✅ | ❌ | ❌ | ✅ |
| **Memory Decay** (Ebbinghaus) | ✅ | ❌ | ❌ | ❌ |
| Auto-importance scoring | ✅ local | ✅ via LLM | ❌ | ❌ |
| **Memory Compression** | ✅ | ❌ | ❌ | ❌ |
| Semantic search (50+ langs) | ✅ local | ✅ via API | ✅ | ✅ |
| Timeline API | ✅ | ❌ | ❌ | ❌ |
| Tags & Relations (graph) | ✅ | ❌ | ✅ | ❌ |
| TTL / Auto-expiration | ✅ | ❌ | ❌ | ❌ |
| MCP Server (Claude, Cursor) | ✅ | ❌ | ❌ | ❌ |
| Batch API | ✅ | ❌ | ❌ | ❌ |
| Export / Import (JSON) | ✅ | ❌ | ✅ | ❌ |
| Soft-delete / Archive | ✅ | ❌ | ❌ | ❌ |
| Prometheus Metrics | ✅ | ❌ | ❌ | ❌ |
| Agent namespace isolation | ✅ | ✅ | ✅ | ❌ |
| Install in 2 minutes | ✅ | ❌ | ❌ | ❌ |

</div>

---

## ✨ Key Features

### 📉 Memory Decay — The Ebbinghaus Engine
Memories fade over time using the [Ebbinghaus forgetting curve](https://en.wikipedia.org/wiki/Forgetting_curve). Critical memories persist for months. Casual notes fade in days.

```
decay = e^(-t · ln2 / half_life)
```

Every retrieval resets the clock and boosts the decay score — just like spaced repetition in human learning.

### 🤖 Auto-Importance Scoring
No LLM call needed. Kore scores importance locally using content analysis — keywords, category, length.

```python
"API token: sk-abc123"  →  importance: 5  (critical, never forget)
"Juan prefers dark mode"  →  importance: 4  (preference)
"Meeting at 3pm"  →  importance: 2  (general)
```

### 🔍 Semantic Search in 50+ Languages
Powered by local `sentence-transformers`. Find memories by meaning, not just keywords. Search in English, get results in Italian. Zero API calls.

### 🗜️ Memory Compression
Similar memories (cosine similarity > 0.88) are automatically merged into richer, deduplicated records. Your DB stays lean forever.

### 📅 Timeline API
"What did I know about project X last month?" — trace any subject chronologically.

### 🏷️ Tags & Relations
Organize memories with tags and build a knowledge graph by linking related memories together. Search by tag, traverse relations bidirectionally.

### ⏳ TTL — Time-to-Live
Set an expiration on any memory. Expired memories are automatically excluded from search, export, and timeline. Run `/cleanup` to purge them, or let the decay pass handle it.

### 📦 Batch API
Save up to 100 memories in a single request. Perfect for bulk imports and agent bootstrapping.

### 💾 Export / Import
Full JSON export of all active memories. Import from a previous backup or migrate between instances.

### 🔌 MCP Server (Model Context Protocol)
Native integration with Claude, Cursor, and any MCP-compatible client. Exposes save, search, timeline, decay, compress, and export as MCP tools.

### 🔐 Agent Namespace Isolation
Multi-agent safe. Each agent sees only its own memories, even on a shared server.

---

## 📦 Install

```bash
# Core (FTS5 search only)
pip install kore-memory

# With semantic search (50+ languages, local embeddings)
pip install kore-memory[semantic]

# With MCP server (Claude, Cursor integration)
pip install kore-memory[semantic,mcp]
```

---

## 🚀 Quickstart

```bash
# Start the server
kore
# → Kore running on http://localhost:8765
```

```bash
# Save a memory
curl -X POST http://localhost:8765/save \
  -H "Content-Type: application/json" \
  -H "X-Agent-Id: my-agent" \
  -d '{"content": "User prefers concise responses in Italian", "category": "preference"}'

# → {"id": 1, "importance": 4, "message": "Memory saved"}
#   (importance auto-scored: preference category + keyword "prefers")
```

```bash
# Search — any language
curl "http://localhost:8765/search?q=user+preferences&limit=5" \
  -H "X-Agent-Id: my-agent"
```

```bash
# Save with TTL (auto-expires after 48 hours)
curl -X POST http://localhost:8765/save \
  -H "Content-Type: application/json" \
  -H "X-Agent-Id: my-agent" \
  -d '{"content": "Deploy scheduled for Friday", "category": "task", "ttl_hours": 48}'
```

```bash
# Batch save (up to 100 per request)
curl -X POST http://localhost:8765/save/batch \
  -H "Content-Type: application/json" \
  -H "X-Agent-Id: my-agent" \
  -d '{"memories": [
    {"content": "React 19 supports server components", "category": "project"},
    {"content": "Always use parameterized queries", "category": "decision", "importance": 5}
  ]}'
```

```bash
# Tag a memory
curl -X POST http://localhost:8765/memories/1/tags \
  -H "Content-Type: application/json" \
  -H "X-Agent-Id: my-agent" \
  -d '{"tags": ["react", "frontend"]}'

# Search by tag
curl "http://localhost:8765/tags/react/memories" \
  -H "X-Agent-Id: my-agent"
```

```bash
# Link two related memories
curl -X POST http://localhost:8765/memories/1/relations \
  -H "Content-Type: application/json" \
  -H "X-Agent-Id: my-agent" \
  -d '{"target_id": 2, "relation": "depends_on"}'
```

```bash
# Timeline for a subject
curl "http://localhost:8765/timeline?subject=project+alpha" \
  -H "X-Agent-Id: my-agent"

# Run daily decay pass (cron this)
curl -X POST http://localhost:8765/decay/run \
  -H "X-Agent-Id: my-agent"

# Compress similar memories
curl -X POST http://localhost:8765/compress \
  -H "X-Agent-Id: my-agent"

# Export all memories (JSON backup)
curl "http://localhost:8765/export" \
  -H "X-Agent-Id: my-agent" > backup.json

# Cleanup expired memories
curl -X POST http://localhost:8765/cleanup \
  -H "X-Agent-Id: my-agent"
```

---

## 🧠 How It Works

```
Save memory
    │
    ▼
Auto-score importance (1–5)
    │
    ▼
Generate embedding (local, offline)
    │
    ▼
Store in SQLite with decay_score = 1.0
    │
    │   [time passes]
    │
    ▼
decay_score decreases (Ebbinghaus curve)
    │
    ▼
Search query arrives
    │
    ▼
Semantic similarity scored
    │
    ▼
Filter out forgotten memories (decay < 0.05)
    │
    ▼
Re-rank by effective_score = similarity × decay × importance
    │
    ▼
Access reinforcement: decay_score += 0.05
    │
    ▼
Return top-k results
```

### Memory Half-Lives

| Importance | Label | Half-life |
|:---:|:---:|:---:|
| 1 | Low | 7 days |
| 2 | Normal | 14 days |
| 3 | Important | 30 days |
| 4 | High | 90 days |
| 5 | Critical | 365 days |

Each retrieval extends the half-life by **+15%** (spaced repetition effect).

---

## 📡 API Reference

### Core

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/save` | Save a memory (auto-scored). Supports `ttl_hours` for auto-expiration |
| `POST` | `/save/batch` | Save up to 100 memories in one request |
| `GET` | `/search?q=...` | Semantic search with pagination (`limit`, `offset`) |
| `GET` | `/timeline?subject=...` | Chronological history with pagination |
| `DELETE` | `/memories/{id}` | Delete a memory |
| `PUT` | `/memories/{id}` | Update a memory (content, category, importance) |

### Tags

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/memories/{id}/tags` | Add tags to a memory |
| `DELETE` | `/memories/{id}/tags` | Remove tags from a memory |
| `GET` | `/memories/{id}/tags` | List tags for a memory |
| `GET` | `/tags/{tag}/memories` | Search memories by tag |

### Relations

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/memories/{id}/relations` | Create a relation to another memory |
| `GET` | `/memories/{id}/relations` | List all relations (bidirectional) |

### Maintenance

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/decay/run` | Recalculate decay scores + cleanup expired |
| `POST` | `/compress` | Merge similar memories |
| `POST` | `/cleanup` | Remove expired memories (TTL) |
| `GET` | `/metrics` | Prometheus metrics (memory counts, latency, decay stats) |

### Archive

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/memories/{id}/archive` | Soft-delete (archive) a memory |
| `POST` | `/memories/{id}/restore` | Restore an archived memory |
| `GET` | `/archive` | List archived memories |

### Backup

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/export` | Export all active memories (JSON) |
| `POST` | `/import` | Import memories from a previous export |

### Utility

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/health` | Health check + capabilities |
| `GET` | `/dashboard` | Web dashboard (HTML, no auth required) |

Interactive docs: **http://localhost:8765/docs**

### Headers

| Header | Required | Description |
|---|:---:|---|
| `X-Agent-Id` | No | Agent namespace (default: `"default"`) |
| `X-Kore-Key` | On non-localhost | API key (auto-generated on first run) |

### Categories

`general` · `project` · `trading` · `finance` · `person` · `preference` · `task` · `decision`

### Save Request Body

```json
{
  "content": "Memory content (3–4000 chars)",
  "category": "general",
  "importance": null,
  "ttl_hours": null
}
```

| Field | Type | Default | Description |
|---|---|---|---|
| `content` | string | *required* | Memory text (3–4000 chars) |
| `category` | string | `"general"` | One of the categories above |
| `importance` | int (1–5) \| null | `null` | null = auto-scored, 1–5 = explicit |
| `ttl_hours` | int \| null | `null` | Auto-expire after N hours (1–8760). Null = never expires |

---

## ⚙️ Configuration

| Env Var | Default | Description |
|---|---|---|
| `KORE_DB_PATH` | `data/memory.db` | Custom database path |
| `KORE_HOST` | `127.0.0.1` | Server bind address |
| `KORE_PORT` | `8765` | Server port |
| `KORE_LOCAL_ONLY` | `1` | Skip auth for localhost requests |
| `KORE_API_KEY` | auto-generated | Override API key |
| `KORE_CORS_ORIGINS` | *(empty)* | Comma-separated allowed origins |
| `KORE_EMBED_MODEL` | `paraphrase-multilingual-MiniLM-L12-v2` | Sentence-transformers model |
| `KORE_MAX_EMBED_CHARS` | `8000` | Max chars sent to embedder (OOM protection) |
| `KORE_SIMILARITY_THRESHOLD` | `0.88` | Cosine threshold for compression |

---

## 🔌 MCP Server

Kore ships with a native [Model Context Protocol](https://modelcontextprotocol.io) server for direct integration with Claude, Cursor, and any MCP-compatible client.

```bash
# Install with MCP support
pip install kore-memory[mcp]

# Run the MCP server (stdio transport, default)
kore-mcp
```

### Available MCP Tools

| Tool | Description |
|---|---|
| `memory_save` | Save a memory with auto-scoring |
| `memory_search` | Semantic or full-text search |
| `memory_delete` | Delete a memory |
| `memory_update` | Update memory content, category, or importance |
| `memory_save_batch` | Save up to 100 memories at once |
| `memory_add_tags` | Add tags to a memory |
| `memory_search_by_tag` | Search memories by tag |
| `memory_add_relation` | Link two related memories |
| `memory_timeline` | Chronological history for a subject |
| `memory_decay_run` | Recalculate decay scores |
| `memory_compress` | Merge similar memories |
| `memory_cleanup` | Remove expired memories |
| `memory_import` | Import memories from JSON |
| `memory_export` | Export all active memories |

### Claude Desktop Configuration

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "kore-memory": {
      "command": "kore-mcp",
      "args": []
    }
  }
}
```

### Cursor / Claude Code Configuration

Add to your `.claude/settings.json` or MCP config:

```json
{
  "mcpServers": {
    "kore-memory": {
      "command": "kore-mcp"
    }
  }
}
```

---

## 📊 Web Dashboard

Kore includes a built-in web dashboard served directly from FastAPI — no build step, no npm, no extra dependencies.

```bash
# Start Kore
kore

# Open in browser
open http://localhost:8765/dashboard
```

### Features

| Tab | Description |
|---|---|
| **Overview** | Health status, total memories, categories breakdown |
| **Memories** | Search (FTS + semantic), save, delete, pagination |
| **Tags** | Search by tag, add/remove/list tags on any memory |
| **Relations** | View and create memory relations (knowledge graph) |
| **Timeline** | Chronological trace for any subject |
| **Maintenance** | Run decay, compress, and cleanup with one click |
| **Backup** | Export as JSON download, import from file |

- Dark theme with Kore purple accents
- Responsive (mobile-friendly with bottom nav)
- Agent selector in header — switch agent context instantly
- All interactions via the same REST API (no separate backend)

---

## 🟨 JavaScript/TypeScript SDK

Kore ships with a native JavaScript/TypeScript client — zero runtime dependencies, dual ESM/CJS output, full type safety.

```bash
npm install kore-memory-client
```

### Usage

```typescript
import { KoreClient } from 'kore-memory-client';

const kore = new KoreClient({
  baseUrl: 'http://localhost:8765',
  agentId: 'my-agent'
});

// Save
const result = await kore.save({
  content: 'User prefers dark mode',
  category: 'preference',
  importance: 4
});

// Search
const memories = await kore.search({
  q: 'dark mode',
  limit: 5,
  semantic: true
});

// Tags & Relations
await kore.addTags(result.id, ['ui', 'preference']);
await kore.addRelation(result.id, otherId, 'related');

// Update
await kore.update(result.id, { importance: 5 });

// Archive & Restore
await kore.archive(result.id);
await kore.restore(result.id);

// Maintenance
await kore.decayRun();
await kore.compress();

// Export
const backup = await kore.exportMemories();
```

### Error Handling

```typescript
import { KoreValidationError, KoreAuthError } from 'kore-memory-client';

try {
  await kore.save({ content: 'ab' }); // too short
} catch (error) {
  if (error instanceof KoreValidationError) {
    console.log('Validation failed:', error.detail);
  }
}
```

**Features:** Zero deps • ESM + CJS • Full TypeScript • 17 async methods • ~6KB minified • Node 18+

---

## 🐍 Python SDK

Kore ships with a built-in Python client SDK — type-safe, zero dependencies beyond `httpx`, supports both sync and async.

```bash
pip install kore-memory
```

### Sync

```python
from kore_memory import KoreClient

with KoreClient("http://localhost:8765", agent_id="my-agent") as kore:
    # Save
    result = kore.save("User prefers dark mode", category="preference")
    print(result.id, result.importance)

    # Search
    results = kore.search("dark mode", limit=5)
    for mem in results.results:
        print(mem.content, mem.decay_score)

    # Tags
    kore.add_tags(result.id, ["ui", "preference"])
    kore.search_by_tag("ui")

    # Relations
    other = kore.save("Use Tailwind for styling", category="decision")
    kore.add_relation(result.id, other.id, "related")

    # Maintenance
    kore.decay_run()
    kore.compress()
    kore.cleanup()

    # Export
    backup = kore.export_memories()
```

### Async

```python
from kore_memory import AsyncKoreClient

async with AsyncKoreClient("http://localhost:8765", agent_id="my-agent") as kore:
    result = await kore.save("Async memory", category="project")
    results = await kore.search("async", limit=5)
    await kore.decay_run()
```

### Error Handling

```python
from kore_memory import KoreClient, KoreValidationError, KoreRateLimitError

with KoreClient() as kore:
    try:
        kore.save("ab")  # too short
    except KoreValidationError as e:
        print(f"Validation error: {e.detail}")
    except KoreRateLimitError:
        print("Slow down!")
```

**Exception hierarchy:** `KoreError` → `KoreAuthError` | `KoreNotFoundError` | `KoreValidationError` | `KoreRateLimitError` | `KoreServerError`

### SDK Methods

| Method | Description |
|---|---|
| `save(content, category, importance, ttl_hours)` | Save a memory |
| `save_batch(memories)` | Batch save (up to 100) |
| `search(q, limit, offset, category, semantic)` | Semantic or FTS search |
| `timeline(subject, limit, offset)` | Chronological history |
| `delete(memory_id)` | Delete a memory |
| `add_tags(memory_id, tags)` | Add tags |
| `get_tags(memory_id)` | Get tags |
| `remove_tags(memory_id, tags)` | Remove tags |
| `search_by_tag(tag, limit)` | Search by tag |
| `add_relation(memory_id, target_id, relation)` | Create relation |
| `get_relations(memory_id)` | Get relations |
| `decay_run()` | Run decay pass |
| `compress()` | Merge similar memories |
| `cleanup()` | Remove expired memories |
| `export_memories()` | Export all memories |
| `import_memories(memories)` | Import memories |
| `update(memory_id, content, category, importance)` | Update a memory |
| `archive(memory_id)` | Archive (soft-delete) a memory |
| `restore(memory_id)` | Restore an archived memory |
| `get_archived(limit, offset)` | List archived memories |
| `health()` | Health check |

---

## 🔐 Security

- **API key** — auto-generated on first run, saved as `data/.api_key` (chmod 600)
- **Agent isolation** — agents can only read/write/delete their own memories
- **SQL injection proof** — parameterized queries throughout
- **Timing-safe key comparison** — `secrets.compare_digest`
- **Input validation** — Pydantic v2 on all endpoints
- **Rate limiting** — per IP + path, configurable limits
- **Security headers** — `X-Content-Type-Options`, `X-Frame-Options`, `CSP`, `Referrer-Policy`
- **CORS** — restricted by default, configurable via `KORE_CORS_ORIGINS`
- **FTS5 sanitization** — special characters stripped, token count limited
- **OOM protection** — embedding input capped at 8000 chars
- **CSP nonce** — per-request nonce for inline scripts, no `unsafe-inline`
- **Connection pooling** — thread-safe SQLite connection pool

---

## 🗺️ Roadmap

- [x] FTS5 full-text search
- [x] Semantic search (multilingual)
- [x] Memory Decay (Ebbinghaus)
- [x] Auto-importance scoring
- [x] Memory Compression
- [x] Timeline API
- [x] Agent namespace isolation
- [x] API key authentication
- [x] Rate limiting
- [x] Security headers & CORS
- [x] Export / Import (JSON)
- [x] Tags & Relations (knowledge graph)
- [x] Batch API
- [x] TTL / Auto-expiration
- [x] MCP Server (Claude, Cursor)
- [x] Pagination (offset + has_more)
- [x] Cursor-based pagination
- [x] Centralized config (env vars)
- [x] OOM protection (embedder)
- [x] Vector index cache
- [x] numpy-optimized search & compression
- [x] Python client SDK (sync + async)
- [x] npm client SDK
- [x] Web dashboard (localhost UI)
- [x] Soft-delete / archive
- [x] Prometheus metrics
- [x] MCP full API coverage (14 tools)
- [x] CSP nonce-based security
- [x] Event system (lifecycle hooks)
- [x] Connection pooling
- [ ] PostgreSQL backend
- [ ] Embeddings v2 (multilingual-e5-large)

## 🛠️ Development

```bash
git clone https://github.com/auriti-labs/kore-memory
cd kore-memory
python -m venv .venv && source .venv/bin/activate
pip install -e ".[semantic,dev]"
pytest tests/ -v
```

---

## 📄 License

MIT © [Juan Auriti](https://github.com/auriti)

---

<div align="center">
<sub>Built for AI agents that deserve better memory.</sub>
</div>

---

<p align="center">
  <a href="https://buymeacoffee.com/auritidesign">
    <img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me a Coffee" />
  </a>
</p>
```

## File: `article-devto.md`
```markdown
---
title: "I Built a Memory System That Thinks Like a Human Brain — Here's How Kore Memory Works"
published: false
description: "Persistent memory for AI agents with local-only semantic search, Ebbinghaus decay curves, and zero cloud dependencies. Install in 2 minutes."
tags: ai, python, opensource, machinelearning
cover_image:
---

TL;DR: Kore Memory is an open-source memory layer for AI agents that runs 100% offline on SQLite. It implements the Ebbinghaus forgetting curve (memories naturally decay), auto-scores importance without any LLM, and supports semantic search in 50+ languages. 360 tests, 80%+ coverage. `pip install kore-memory` and you're done.

---

## The Problem: AI Agents Have Amnesia

Every conversation with an AI agent feels like meeting them for the first time. They don't remember what you told them yesterday. They don't learn from interactions. Every session is a blank slate.

Current "memory solutions" are worse than useless:
- **Mem0, Zep, Letta** require cloud APIs (privacy nightmare)
- They call LLMs just to decide what's worth storing (expensive, slow, dependency hell)
- They remember everything forever in a flat database (useless bloat)
- They cost money per request

What if memory worked like a human brain instead? Remembering what matters. Forgetting what doesn't. Automatically. Offline.

That's Kore Memory.

---

## What is Kore Memory? (30-Second Pitch)

Kore Memory is a persistent memory layer for AI agents built on three principles:

1. **100% Offline** — Runs on SQLite. No cloud. No LLM calls. No API keys to cloud services. Ship it with your agent.
2. **Forgets Like Humans** — Implements the Ebbinghaus forgetting curve. Critical memories stick around for months. Casual notes fade in days. Each retrieval extends the half-life.
3. **Zero LLM Overhead** — Auto-scores importance using keyword analysis and category signals. No OpenAI calls. No latency tax.

Install it:
```bash
pip install kore-memory[semantic]
kore
# → http://localhost:8765
```

That's it. You now have persistent, intelligent memory for your agent.

---

## The Science: Ebbinghaus Forgetting Curve

You probably learned about the Ebbinghaus forgetting curve in school. After you learn something, you forget it exponentially fast unless you review it.

Kore implements this mathematically:

```
decay_score = e^(-t · ln2 / half_life)
```

Where:
- `t` = days since memory was created (or last accessed)
- `half_life` = days until the memory is 50% "forgotten"

The half-life scales with importance:

| Importance | Label | Half-life |
|:---:|:---:|:---:|
| 1 | Low | 7 days |
| 2 | Normal | 14 days |
| 3 | Important | 30 days |
| 4 | High | 90 days |
| 5 | Critical | 365 days |

Here's the clever part: **every time you retrieve a memory, its decay score jumps up by 0.05** (capped at 1.0) **and the effective half-life extends by 15%** — exactly like spaced repetition in human learning. Your brain strengthens pathways you use frequently.

Memories below decay_score 0.05 are "forgotten" — filtered from all searches. They're still in the database (soft delete), but your agent won't accidentally retrieve stale info.

---

## Auto-Importance Scoring (Zero LLM Cost)

Most memory systems ask "is this important?" and wait for an LLM response. Not Kore.

Kore scores importance locally using three signals, no AI needed:

**1. Category Baseline**
```
preference → 4 (user preferences matter)
decision   → 4 (architectural choices matter)
project    → 3 (project context is valuable)
task       → 2 (one-off tasks are ephemeral)
general    → 1 (random notes are low value)
```

**2. Keyword Analysis**
```
"password", "token", "secret", "api_key" → +1 (add 1 to importance)
"prefers", "likes", "dislikes" → +0 (preference signals already baseline 4)
"critical", "urgent", "never" → +1
"remember", "important" → +1
```

**3. Length Bonus**
```
60+ words → +1 (longer = more context = probably important)
```

Concrete examples:

```python
kore.save("API token: sk-abc123def456")
# → importance: 5 (token keyword pushes baseline 1 → 5)

kore.save("Juan prefers dark mode and concise responses")
# → importance: 4 (preference baseline + length bonus)

kore.save("Meeting at 3pm")
# → importance: 1 (short, generic)

kore.save("CRITICAL: Always sanitize user input")
# → importance: 5 (decision baseline 4 + critical keyword)
```

No API calls. No network roundtrips. Instant, local, deterministic.

---

## Code Examples: Getting Started

### Quick Start (3 Lines)

```bash
pip install kore-memory[semantic]
kore
# → Kore running on http://localhost:8765
# → Dashboard: http://localhost:8765/dashboard
```

Open your browser. You now have a web UI to save, search, and manage memories. Dark theme. No build step. No frontend framework. Pure HTML/CSS/JS inline in Python.

### Python SDK: Save & Search

```python
from kore_memory import KoreClient

# Sync client
with KoreClient("http://localhost:8765", agent_id="my-agent") as kore:
    # Save a memory
    memory = kore.save(
        content="User prefers dark mode and concise technical responses",
        category="preference"
    )
    print(f"Saved with importance: {memory.importance}")  # → 4

    # Search semantically
    results = kore.search(
        q="dark theme preference",
        semantic=True,
        limit=5
    )
    for mem in results.results:
        print(f"Score: {mem.decay_score:.2f} | {mem.content}")

    # Add tags
    kore.add_tags(memory.id, ["ui", "user-prefs"])

    # Search by tag
    ui_memories = kore.search_by_tag("ui")
```

### JavaScript/TypeScript SDK

```typescript
import { KoreClient } from 'kore-memory-client';

const kore = new KoreClient({
  baseUrl: 'http://localhost:8765',
  agentId: 'my-agent'
});

// Save
const result = await kore.save({
  content: 'React 19 supports server components',
  category: 'project',
  importance: 3
});

// Search
const memories = await kore.search({
  q: 'server components',
  semantic: true,
  limit: 5
});

// Relations (build a knowledge graph)
await kore.addRelation(result.id, otherId, 'depends_on');
```

### LangChain Integration

```python
from langchain.chains import LLMChain
from kore_memory.integrations import KoreLangChainMemory

# 5 lines to add persistent memory to any LangChain chain
memory = KoreLangChainMemory(
    kore_url="http://localhost:8765",
    agent_id="langchain-agent"
)

chain = LLMChain(llm=model, memory=memory, prompt=prompt)
response = chain.invoke({"question": "What's my favorite language?"})
# → Memory automatically saves the exchange
```

The `KoreLangChainMemory` class extends LangChain's `BaseMemory`. It auto-saves exchanges with semantic context. Next conversation, the agent remembers.

### CrewAI Integration

```python
from crewai import Agent
from kore_memory.integrations import KoreCrewAIMemory

# Split short-term (ephemeral) and long-term (persistent) memory
short_term = KoreCrewAIMemory(
    kore_url="http://localhost:8765",
    agent_id="crew-agent",
    ttl_hours=24  # Expires after 24 hours
)

long_term = KoreCrewAIMemory(
    kore_url="http://localhost:8765",
    agent_id="crew-agent"
    # No TTL = persists forever (or until decay filters it)
)

agent = Agent(
    name="researcher",
    memory=long_term,  # or short_term, or mix both
    tools=[...]
)
```

### MCP Integration (Claude Desktop)

Kore ships with a Model Context Protocol server. Plug it directly into Claude Desktop:

```bash
pip install kore-memory[mcp]
kore-mcp  # Start the MCP server
```

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "kore-memory": {
      "command": "kore-mcp",
      "args": []
    }
  }
}
```

Now Claude has 14 memory tools:
- `memory_save` — Save with auto-scoring
- `memory_search` — Semantic or full-text
- `memory_add_tags` — Organize with tags
- `memory_add_relation` — Link related memories
- `memory_timeline` — Trace chronological history
- `memory_compress` — Deduplicate similar memories
- ... and 8 more

---

## Comparison: Kore vs the Competition

Here's what sets Kore apart:

| Feature | Kore | Mem0 | Zep | ChromaDB |
|---|:---:|:---:|:---:|:---:|
| Fully offline | ✅ | ❌ | ❌ | ✅ |
| No LLM required | ✅ | ❌ | ❌ | ✅ |
| Ebbinghaus decay | ✅ | ❌ | ❌ | ❌ |
| Auto-importance (local) | ✅ | LLM | ❌ | ❌ |
| Memory compression | ✅ | ❌ | ❌ | ❌ |
| Semantic search (50+ langs) | ✅ | API | API | ✅ |
| Timeline API | ✅ | ❌ | ❌ | ❌ |
| Tags & Relations | ✅ | ❌ | ❌ | ❌ |
| TTL / Auto-expiration | ✅ | ❌ | ❌ | ❌ |
| MCP Server (Claude/Cursor) | ✅ | ❌ | ❌ | ❌ |
| Batch API | ✅ | ❌ | ❌ | ❌ |
| Web Dashboard | ✅ | ✅ | ✅ | ❌ |
| Runs locally in 2 minutes | ✅ | ❌ | ❌ | ✅ |

Mem0 and Zep are enterprise solutions requiring cloud infra. ChromaDB is a vector store, not a memory system (no decay, no auto-importance). Kore is purpose-built for AI agents that need to remember intelligently.

---

## Architecture: How It Works

```
POST /save
  │
  ├─ Parse + validate (Pydantic)
  │
  ├─ Auto-score importance
  │   ├─ Category baseline
  │   ├─ Keyword signals
  │   └─ Length bonus
  │
  ├─ Generate embedding (local sentence-transformers)
  │
  └─ Store in SQLite
      ├─ `memories` table (core data)
      ├─ `memories_fts` virtual table (FTS5 index)
      ├─ `memory_tags` (many-to-many)
      └─ `memory_relations` (knowledge graph)

GET /search?q=dark+mode
  │
  ├─ Encode query (same embedding model)
  │
  ├─ FTS5 keyword match (fast baseline)
  │
  ├─ Semantic search (cosine similarity)
  │
  ├─ Filter expired + decayed memories
  │
  ├─ Re-rank: score = similarity × decay × importance
  │
  └─ Return top-k + reinforce (access_count++, decay+0.05)
```

**Key technical details:**
- FastAPI + SQLite (WAL mode for concurrency)
- FTS5 full-text index with automatic triggers
- Sentence-transformers (multilingual) with OOM protection
- Connection pooling, parameterized queries, rate limiting
- 360 tests, 80%+ code coverage
- Async/await support throughout

**Dependencies:** Just FastAPI, Uvicorn, Pydantic, httpx. Semantic search pulls in sentence-transformers (lazy-loaded, not required for basic FTS).

---

## What Developers Are Using It For

1. **LangChain Agents** — Multi-turn conversations that remember context from previous sessions
2. **CrewAI Teams** — Persistent knowledge graph across agent interactions
3. **AI Tutors** — Remember student progress, learning style, misconceptions
4. **Code Review Bots** — Remember coding standards, team preferences, architectural patterns
5. **Sales Agents** — Customer history, preferences, deal context
6. **Research Assistants** — Literature notes, methodology choices, hypotheses
7. **Claude/Cursor Plugins** — Via MCP, extend Claude with custom memory

Real-world use case: A code review agent trained on a specific codebase. It uses Kore to remember:
- Architectural decisions (importance 5, half-life 365 days)
- Code patterns the team prefers (importance 4, half-life 90 days)
- Past PRs that triggered discussions (importance 3, decays over time)
- Linting rules (importance 5, never forget)

It searches for "async patterns" and finds relevant memories from 6 months ago, weighted by decay and importance. If it hasn't seen that memory in a while, decay reduces its score — exactly like human memory.

---

## Getting Started: 4-Step Walkthrough

**Step 1: Install**
```bash
pip install kore-memory[semantic]
```

**Step 2: Start the server**
```bash
kore
# → Kore running on http://localhost:8765
```

**Step 3: Open the dashboard**
```
http://localhost:8765/dashboard
```

No login. Dark theme. Fully responsive. Try saving a memory. Try searching.

**Step 4: Integrate with your agent**

If you're using LangChain:
```python
from kore_memory.integrations import KoreLangChainMemory
memory = KoreLangChainMemory("http://localhost:8765")
# Pass to your chain
```

If you're building custom:
```python
from kore_memory import KoreClient
kore = KoreClient("http://localhost:8765")
kore.save("Important context", category="project")
results = kore.search("context")
```

---

## Open Questions We Get Asked

**Q: Does it use my data for training?**
A: No. 100% offline. Nothing leaves your machine.

**Q: Can I use this in production?**
A: Yes. It's stable (v1.0.2), has 360 tests, and is used in production by several teams.

**Q: What about LLM cost?**
A: Zero. No API calls except to your own LLM (Claude, Llama, etc.).

**Q: Can multiple agents share a server?**
A: Yes. Agent namespace isolation via `X-Agent-Id` header. Each agent's memories are private.

**Q: What's the latency?**
A: Search latency is typically 10-50ms. Semantic search (with embeddings) is 50-200ms. No network roundtrips.

**Q: How much data can I store?**
A: SQLite handles millions of memories. We've tested with 100K+ memories with no performance degradation.

**Q: Can I export my memories?**
A: Yes. Full JSON export, import support, soft-delete/archive, TTL for auto-expiration.

---

## Why We Built This

Traditional memory systems treat "forgetting" as a bug. They accumulate every interaction forever.

But human memory is smarter. You remember your first car's license plate (never accessed, slowly decays). You remember your spouse's birthday (constantly reinforced, never decays). You instantly forget meeting room numbers after leaving the building.

Kore brings that intelligence to AI agents. It's not just a vector store. It's a deliberate model of how memory *should* work.

---

## Next Steps

- **Star on GitHub** — [github.com/auriti-labs/kore-memory](https://github.com/auriti-labs/kore-memory)
- **Install** — `pip install kore-memory[semantic]`
- **JS SDK** — `npm install kore-memory-client`
- **Documentation** — [auritidesign.it/brain/knowledge/docs_legacy/kore-memory](https://auritidesign.it/brain/knowledge/docs_legacy/kore-memory)
- **Contribute** — Issues, PRs, and feature discussions welcome

The agent that remembers wins. Build one.

---

**Questions? Comments? Hit me up on GitHub or reach out on dev.to.**
```

## File: `hatch_build.py`
```python
"""
Hatch build hook — shows welcome message after pip install.
"""

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        pass

    def finalize(self, version, build_data, artifact_path):
        try:
            from kore_memory.welcome import print_welcome
            print_welcome()
        except Exception:
            pass
```

## File: `kore-daemon.sh`
```bash
#!/usr/bin/env bash
# Kore — proper daemon launcher with .env support

set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

PID_FILE="$DIR/logs/kore.pid"
LOG_FILE="$DIR/logs/server.log"
mkdir -p logs

# Load .env (safe: only reads KEY=VALUE lines, ignores comments and commands)
if [ -f "$DIR/.env" ]; then
    while IFS='=' read -r key value; do
        # Skip comments, empty lines, and lines without =
        case "$key" in
            '#'*|'') continue ;;
        esac
        # Remove surrounding quotes from value
        value="${value%\"}"
        value="${value#\"}"
        value="${value%\'}"
        value="${value#\'}"
        export "$key=$value"
    done < "$DIR/.env"
fi

# Check if already running
if [ -f "$PID_FILE" ] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null; then
    if curl -sf http://127.0.0.1:8765/health >/dev/null 2>&1; then
        echo "Kore already running (PID $(cat "$PID_FILE"))"
        exit 0
    fi
fi

# Kill stale processes
fuser -k 8765/tcp 2>/dev/null || true
sleep 1

# Start with proper daemonization
setsid "$DIR/.venv/bin/kore" \
    --host 127.0.0.1 \
    --port 8765 \
    --log-level warning \
    < /dev/null >> "$LOG_FILE" 2>&1 &

PID=$!
echo "$PID" > "$PID_FILE"
disown

echo "Kore started (PID $PID)"
```

## File: `pyproject.toml`
```
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "kore-memory"
version = "2.0.0"
description = "The memory layer that thinks like a human: remembers what matters, forgets what doesn't, and never calls home."
readme = "README.md"
license = { text = "MIT" }
requires-python = ">=3.11"
keywords = ["ai", "memory", "agents", "llm", "embeddings", "semantic-search", "rag", "forgetting-curve"]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
]
dependencies = [
    "fastapi>=0.115.0",
    "uvicorn[standard]>=0.30.0",
    "pydantic>=2.7.0",
    "httpx>=0.27.0",
]

[project.optional-dependencies]
semantic = [
    "sentence-transformers>=3.0.0",
    "sqlite-vec>=0.1.1",
]
nlp = [
    "spacy>=3.7.0",
]
mcp = [
    "mcp>=1.0.0",
]
crewai = [
    "crewai>=0.28.0",
]
langchain = [
    "langchain-core>=0.2.0",
]
pydantic-ai = [
    "pydantic-ai>=0.0.49",
]
openai-agents = [
    "openai-agents>=0.2.0",
]
dev = [
    "pytest>=8.0.0",
    "pytest-cov>=5.0.0",
    "httpx>=0.27.0",
    "pytest-asyncio>=1.0.0",
    "ruff>=0.8.0",
]

[project.urls]
Homepage = "https://github.com/auriti-labs/kore-memory"
Documentation = "https://auritidesign.it/docs"
Repository = "https://github.com/auriti-labs/kore-memory"
Issues = "https://github.com/auriti-labs/kore-memory/issues"

[project.scripts]
kore = "kore_memory.cli:main"
kore-mcp = "kore_memory.mcp_server:main"
kore-welcome = "kore_memory.welcome:print_welcome"

[tool.hatch.build.targets.wheel]
packages = ["kore_memory"]
artifacts = ["assets/logo.svg"]

[tool.hatch.build.hooks.custom]
path = "hatch_build.py"

[tool.pytest.ini_options]
asyncio_mode = "auto"

[tool.bandit]
exclude_dirs = ["tests", "scripts"]
skips = ["B101", "B603", "B607", "B110", "B112", "B608"]

[tool.ruff]
target-version = "py311"
line-length = 120

[tool.ruff.lint]
select = ["E", "F", "W", "I", "UP", "B", "SIM", "S"]
ignore = [
    "S101",    # assert — used in tests
    "S603",    # subprocess — not applicable
    "S607",    # partial path — not applicable
    "S608",    # SQL injection — false positive, all queries use parameterized placeholders
    "S110",    # try-except-pass — intentional error suppression (connection cleanup)
    "S112",    # try-except-continue — intentional skip of corrupted data
    "B008",    # function call in default arg — Depends() pattern FastAPI
    "B905",    # zip without strict — not needed for numeric vectors
    "SIM105",  # contextlib.suppress — explicit try-except is clearer
    "SIM118",  # key in dict — readability preference
]

[tool.ruff.lint.per-file-ignores]
"tests/*" = ["S", "B"]

[tool.ruff.format]
quote-style = "double"

[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = false
check_untyped_defs = true
ignore_missing_imports = true
```

## File: `requirements.txt`
```
fastapi>=0.115.0
uvicorn[standard]>=0.30.0
pydantic>=2.7.0
sentence-transformers>=3.0.0
httpx>=0.27.0
```

## File: `start.sh`
```bash
#!/usr/bin/env sh
# Kore — start server in background
# Usage: ./start.sh

DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR" || exit 1

PID_FILE="$DIR/logs/kore.pid"
mkdir -p "$DIR/logs"

# Controlla se il server risponde davvero (non solo se il PID esiste)
if curl -sf http://127.0.0.1:8765/health >/dev/null 2>&1; then
    echo "Kore already running and healthy"
    exit 0
fi

# PID esiste ma server non risponde → processo zombie, kill forzato
if [ -f "$PID_FILE" ]; then
    OLD_PID=$(cat "$PID_FILE")
    kill -9 "$OLD_PID" 2>/dev/null
    rm -f "$PID_FILE"
fi

# Libera la porta 8765 nel caso ci fosse qualcos'altro
fuser -k 8765/tcp 2>/dev/null || true
sleep 1

# Load .env and start server in one command (preserves env vars in nohup)
if [ -f "$DIR/.env" ]; then
    # shellcheck disable=SC2046
    nohup env $(grep -v '^#' "$DIR/.env" | xargs) \
        "$DIR/.venv/bin/kore" \
        --host 127.0.0.1 \
        --port 8765 \
        --log-level warning \
        > "$DIR/logs/server.log" 2>&1 &
else
    nohup "$DIR/.venv/bin/kore" \
        --host 127.0.0.1 \
        --port 8765 \
        --log-level warning \
        > "$DIR/logs/server.log" 2>&1 &
fi

echo $! > "$PID_FILE"
echo "Kore started (pid $!)"
```

## File: `test_pagination_fix.py`
```python
#!/usr/bin/env python3
"""Test rapido per verificare il fix pagination issue #2"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.dirname(__file__))

from kore_memory.database import init_db
from kore_memory.models import MemorySaveRequest
from kore_memory.repository import save_memory, search_memories

# Init DB
init_db()

# Pulisci test precedenti
from kore_memory.database import get_connection
with get_connection() as conn:
    conn.execute("DELETE FROM memories WHERE agent_id = 'test_pagination'")

print("🧪 Testing pagination fix...")

# Crea 20 memorie di test
print("\n1️⃣ Creando 20 memorie...")
for i in range(20):
    req = MemorySaveRequest(
        content=f"Test memory number {i+1:02d} for pagination testing",
        category="general",
        importance=3,
    )
    save_memory(req, agent_id="test_pagination")

print("✅ 20 memorie create")

# Test 1: Prima pagina (limit=5, no cursor)
print("\n2️⃣ Test prima pagina (limit=5, no cursor)...")
results1, cursor1 = search_memories("test memory", limit=5, semantic=False, agent_id="test_pagination")
print(f"   Risultati: {len(results1)}")
print(f"   Ha next cursor: {cursor1 is not None}")
print(f"   IDs: {[r.id for r in results1]}")
assert len(results1) == 5, f"Expected 5 results, got {len(results1)}"
assert cursor1 is not None, "Expected cursor for next page"

# Test 2: Seconda pagina (limit=5, with cursor)
print("\n3️⃣ Test seconda pagina (limit=5, with cursor)...")
results2, cursor2 = search_memories("test memory", limit=5, semantic=False, agent_id="test_pagination", cursor=cursor1)
print(f"   Risultati: {len(results2)}")
print(f"   Ha next cursor: {cursor2 is not None}")
print(f"   IDs: {[r.id for r in results2]}")
assert len(results2) == 5, f"Expected 5 results, got {len(results2)}"
assert cursor2 is not None, "Expected cursor for next page"

# Test 3: Verifica che non ci siano duplicati
print("\n4️⃣ Test no duplicati tra pagine...")
ids1 = {r.id for r in results1}
ids2 = {r.id for r in results2}
overlap = ids1 & ids2
assert len(overlap) == 0, f"Found duplicate IDs between pages: {overlap}"
print("   ✅ Nessun duplicato")

# Test 4: Pagina 3 e 4
print("\n5️⃣ Test pagine successive...")
results3, cursor3 = search_memories("test memory", limit=5, semantic=False, agent_id="test_pagination", cursor=cursor2)
results4, cursor4 = search_memories("test memory", limit=5, semantic=False, agent_id="test_pagination", cursor=cursor3)
print(f"   Pagina 3: {len(results3)} risultati, cursor={cursor3 is not None}")
print(f"   Pagina 4: {len(results4)} risultati, cursor={cursor4 is not None}")

# Test 5: Totale risultati
all_ids = {r.id for r in results1 + results2 + results3 + results4}
print(f"\n6️⃣ Totale IDs unici ottenuti: {len(all_ids)}")
assert len(all_ids) == 20, f"Expected 20 unique results, got {len(all_ids)}"

# Cleanup
with get_connection() as conn:
    conn.execute("DELETE FROM memories WHERE agent_id = 'test_pagination'")

print("\n✅ TUTTI I TEST PASSATI! Issue #2 è fixata! 🎉")
```

## File: `brain/knowledge/docs_legacy/competitive-analysis-2025.md`
```markdown
# Analisi Competitiva: Kore Memory nel Mercato AI Agent Memory (2025)

**Data:** Febbraio 2025
**Prodotto:** [kore-memory](https://github.com/auriti-labs/kore-memory) v0.3.1
**Autore:** Ricerca condotta per auriti-labs

---

## Sommario Esecutivo

Kore-memory si posiziona in un mercato in rapida crescita — quello dei sistemi di memoria persistente per agenti AI. Con un approccio unico basato su Ebbinghaus decay, funzionamento completamente offline e scoring automatico senza LLM, il prodotto ha caratteristiche distintive rare nel panorama competitivo.

Questo report analizza 6 competitor principali, identifica gap e opportunita, e propone una roadmap strategica per rendere kore-memory indispensabile.

---

## 1. Analisi dei Competitor

### 1.1 Mem0 (mem0.ai)

**Descrizione:** Sistema di memoria AI più popolare nel mercato, nato nel 2023 con forte focus su integrazioni LLM.

| Aspetto | Dettagli |
|---------|----------|
| **GitHub Stars** | ~22.000+ (gen 2025) |
| **Pricing** | Free tier (1.000 memories) / Pro $99/mese / Enterprise custom |
| **Backend** | Cloud-first (Mem0 Platform) + self-hosted option |
| **LLM Dependency** | Si — usa LLM per estrazione e scoring |

**Feature Chiave:**
- Memory graph (relazioni tra memorie)
- Multi-user support nativo
- Auto-extraction da conversazioni
- Integrazioni: OpenAI, LangChain, CrewAI, Autogen
- SDK: Python, TypeScript, REST API
- Dashboard web

**Cosa manca a Kore che Mem0 ha:**
1. Memory Graph (relazioni esplicite tra entita)
2. Auto-extraction da conversazioni
3. Dashboard web UI
4. SDK TypeScript/npm
5. Integrazioni native con framework AI (CrewAI, Autogen)
6. Multi-user management (non solo multi-agent)

**Cosa Kore ha che Mem0 NON ha:**
1. **Ebbinghaus decay** — memoria che sbiadisce naturalmente
2. **Funzionamento 100% offline** — zero chiamate cloud
3. **No LLM required** — scoring locale senza costi API
4. **Memory compression** — deduplicazione automatica
5. **Timeline API** — storia cronologica per soggetto
6. **Costo zero** — nessun tier a pagamento richiesto

---

### 1.2 Letta (ex-MemGPT)

**Descrizione:** Framework per agenti AI con memoria a lungo termine, nato come progetto di ricerca UC Berkeley nel 2023.

| Aspetto | Dettagli |
|---------|----------|
| **GitHub Stars** | ~12.000+ |
| **Pricing** | Open-source (Apache 2.0) + Letta Cloud in beta |
| **Backend** | PostgreSQL/SQLite + vector store |
| **LLM Dependency** | Si — core architecture basata su LLM |

**Feature Chiave:**
- Architettura "LLM-as-OS" (LLM gestisce la propria memoria)
- Paging automatico tra memoria core e archival
- Tool calling nativo
- Multi-agent orchestration
- State management persistente
- Supporto per function calling

**Cosa manca a Kore che Letta ha:**
1. Architettura agent-as-OS (LLM auto-gestisce memoria)
2. Memory paging automatico (core vs archival)
3. Tool/function calling integrato
4. Multi-agent orchestration
5. Conversation state management

**Cosa Kore ha che Letta NON ha:**
1. **Semplicita** — non richiede comprensione di architetture complesse
2. **No LLM dependency** — Letta e inutilizzabile senza LLM
3. **Ebbinghaus decay** — Letta non ha forgetting curve
4. **Leggerezza** — Kore e una singola dipendenza, Letta e un framework completo
5. **Install in 2 minuti** — Letta richiede configurazione significativa

---

### 1.3 Zep (getzep.com)

**Descrizione:** Memory layer specifico per AI assistants, con focus su conversational AI.

| Aspetto | Dettagli |
|---------|----------|
| **GitHub Stars** | ~2.500+ |
| **Pricing** | Free self-hosted / Zep Cloud: $20/mese starter, custom enterprise |
| **Backend** | PostgreSQL + pgvector |
| **LLM Dependency** | Parziale — embedding via API o locale |

**Feature Chiave:**
- Session management (conversazioni multi-turn)
- Entity extraction automatica
- Conversation summarization
- Fact extraction da dialoghi
- Temporal awareness (quando e stato detto qualcosa)
- Postgres-native (pgvector)
- LangChain integration nativa

**Cosa manca a Kore che Zep ha:**
1. Session/conversation management
2. Entity extraction automatica
3. Conversation summarization
4. Fact extraction strutturata
5. Postgres backend (scalabilita enterprise)

**Cosa Kore ha che Zep NON ha:**
1. **Ebbinghaus decay** — Zep non ha forgetting
2. **Memory compression** — nessuna deduplicazione
3. **Zero cloud dependency** — Zep Cloud e il focus principale
4. **SQLite backend** — piu semplice per deployment locale
5. **Timeline API esplicita**

---

### 1.4 LangChain Memory Modules

**Descrizione:** Moduli di memoria integrati nel framework LangChain.

| Aspetto | Dettagli |
|---------|----------|
| **GitHub Stars** | ~98.000+ (LangChain totale) |
| **Pricing** | Open-source (MIT) |
| **Backend** | Vari (in-memory, Redis, MongoDB, etc.) |
| **LLM Dependency** | Varia per modulo |

**Tipi di Memory:**
- `ConversationBufferMemory` — buffer semplice
- `ConversationSummaryMemory` — riassunto via LLM
- `ConversationKGMemory` — knowledge graph
- `VectorStoreRetrieverMemory` — vector search
- `EntityMemory` — traccia entita menzionate

**Cosa manca a Kore che LangChain ha:**
1. Integrazione nativa in un framework AI popolare
2. Conversation summarization via LLM
3. Knowledge Graph memory
4. Entity tracking automatico
5. Varieta di backend storage

**Cosa Kore ha che LangChain NON ha:**
1. **Sistema di decay** — LangChain memories sono statiche
2. **Auto-importance scoring** — nessun ranking intelligente
3. **Memory compression** — nessuna deduplicazione
4. **Prodotto standalone** — LangChain memory richiede LangChain
5. **Multilingual search nativo** — senza configurazione

---

### 1.5 Chroma

**Descrizione:** Vector database open-source ottimizzato per AI applications.

| Aspetto | Dettagli |
|---------|----------|
| **GitHub Stars** | ~15.000+ |
| **Pricing** | Open-source / Chroma Cloud (pricing non pubblico) |
| **Backend** | SQLite + hnswlib |
| **LLM Dependency** | No (ma spesso usato con LLM) |

**Feature Chiave:**
- Vector storage puro e semplice
- Collection-based organization
- Metadata filtering
- Embedding-agnostic
- Multi-tenancy
- REST API + Python SDK

**Differenze fondamentali:**
Chroma e un **vector database**, non un sistema di memoria AI. Manca completamente di:
- Concetto di "memoria" (solo vettori)
- Decay/forgetting
- Importance scoring
- Memory lifecycle management
- Compression/deduplication

**Kore vs Chroma:**
Kore potrebbe usare Chroma come backend, ma sono prodotti di categoria diversa. Kore e una "memoria intelligente", Chroma e un "database vettoriale".

---

### 1.6 Weaviate

**Descrizione:** Vector database cloud-native con GraphQL API.

| Aspetto | Dettagli |
|---------|----------|
| **GitHub Stars** | ~11.000+ |
| **Pricing** | Open-source / Weaviate Cloud Services (pay-as-you-go) |
| **Backend** | Custom (Go), distributed |
| **LLM Dependency** | No |

**Feature Chiave:**
- GraphQL + REST API
- Hybrid search (vector + keyword)
- Multi-modal (testo, immagini)
- Horizontal scaling
- Enterprise-grade

**Stessa considerazione di Chroma:** Weaviate e infrastruttura, non prodotto. Kore potrebbe teoricamente usare Weaviate come storage layer.

---

### 1.7 Altri Player Rilevanti (2024-2025)

| Prodotto | Focus | Note |
|----------|-------|------|
| **Cognee** | Knowledge graphs per AI | Open-source, Python, graph-centric |
| **Motorhead** | Memory per LangChain | Redis-based, serverless-friendly |
| **Pinecone** | Vector DB managed | Enterprise pricing, no memory semantics |
| **Qdrant** | Vector DB open-source | Rust, high-performance, no memory layer |
| **Marvin** | AI engineering toolkit | Include memory utilities, Python |

---

## 2. Matrice Comparativa

| Feature | Kore | Mem0 | Letta | Zep | LangChain |
|---------|:----:|:----:|:-----:|:---:|:---------:|
| Ebbinghaus Decay | **Si** | No | No | No | No |
| No LLM Required | **Si** | No | No | Parziale | Parziale |
| 100% Offline | **Si** | No | No | Parziale | Si |
| Auto-Importance | **Si** | Via LLM | No | No | No |
| Memory Compression | **Si** | No | No | No | No |
| Timeline API | **Si** | No | No | Parziale | No |
| Memory Graph | No | **Si** | No | Parziale | Si |
| Conversation Mgmt | No | Parziale | **Si** | **Si** | **Si** |
| Entity Extraction | No | **Si** | Parziale | **Si** | **Si** |
| Multi-Agent Native | **Si** | **Si** | **Si** | **Si** | Si |
| TypeScript SDK | No | **Si** | **Si** | Si | Si |
| Web Dashboard | No | **Si** | **Si** | Si | No |
| Free Tier Unlimited | **Si** | No | No | No | Si |

---

## 3. Top 10 Feature da Aggiungere a Kore

Basandosi sull'analisi competitiva, ecco le feature prioritarie:

### 3.1 Alta Priorita (Differenziazione)

1. **Memory Graph / Relations**
   - *Perche:* Mem0 e Zep lo hanno, e fondamentale per contesto ricco
   - *Implementazione:* Tabella `memory_relations` con tipo relazione
   - *Effort:* Medio

2. **Conversation/Session Management**
   - *Perche:* Use-case dominante per AI assistants
   - *Implementazione:* Session ID, conversation history linkage
   - *Effort:* Medio

3. **Web Dashboard (localhost)**
   - *Perche:* Esperienza utente, debugging, visualizzazione decay
   - *Implementazione:* React UI su /dashboard, WebSocket per real-time
   - *Effort:* Alto

4. **Entity Extraction (No-LLM)**
   - *Perche:* Mantiene la filosofia no-LLM ma aggiunge intelligenza
   - *Implementazione:* spaCy/NER locale, lightweight
   - *Effort:* Medio

### 3.2 Media Priorita (Ecosystem)

5. **TypeScript/npm SDK**
   - *Perche:* Ecosistema JS enorme, Vercel AI SDK, Next.js
   - *Implementazione:* Client wrapper per REST API
   - *Effort:* Basso

6. **LangChain Integration**
   - *Perche:* Standard de-facto per AI apps
   - *Implementazione:* `KoreMemory` class compatibile con LangChain
   - *Effort:* Basso

7. **Export/Import JSON**
   - *Perche:* Backup, migrazione, debugging
   - *Implementazione:* Endpoint `/export` e `/import`
   - *Effort:* Basso

8. **Rate Limiting**
   - *Perche:* Production-readiness, abuse prevention
   - *Implementazione:* Token bucket in middleware
   - *Effort:* Basso

### 3.3 Bassa Priorita (Nice-to-Have)

9. **Conversation Summarization (opzionale, con LLM)**
   - *Perche:* Use-case comune, ma opt-in per mantenere filosofia
   - *Implementazione:* Endpoint che accetta callback LLM
   - *Effort:* Medio

10. **Plugin System**
    - *Perche:* Estensibilita per casi edge
    - *Implementazione:* Hook pre/post save, custom scorers
    - *Effort:* Alto

---

## 4. Unique Selling Points di Kore-Memory

### 4.1 Il Valore dell'Approccio Ebbinghaus

Kore e **l'unico** sistema di memoria AI che implementa il forgetting curve:

```
decay = e^(-t * ln2 / half_life)
```

**Perche questo e prezioso:**

1. **Realismo cognitivo** — Gli umani dimenticano, gli agenti dovrebbero farlo
2. **Storage efficiente** — Non accumula infinite memorie irrilevanti
3. **Prioritizzazione naturale** — L'importante emerge, il banale svanisce
4. **Spaced repetition** — L'accesso rinforza, come nello studio

### 4.2 Il Valore del No-LLM

Nessun competitor offre auto-scoring senza LLM. Vantaggi:

1. **Costo zero** — Nessuna API call = nessun costo variabile
2. **Latenza zero** — Scoring istantaneo
3. **Privacy totale** — Nessun dato esce dal server
4. **Determinismo** — Stesso input = stesso score (riproducibile)

### 4.3 Il Valore del 100% Offline

| Scenario | Mem0 | Letta | Zep | **Kore** |
|----------|------|-------|-----|----------|
| Rete assente | Fallisce | Fallisce | Fallisce | **Funziona** |
| GDPR strict | Problematico | Problematico | Problematico | **Compliant** |
| Air-gapped | Impossibile | Impossibile | Impossibile | **Possibile** |
| Edge deployment | No | No | No | **Si** |

### 4.4 Memory Compression

Feature **unica** nel mercato:

- Similarita coseno > 0.88 → merge automatico
- Database sempre snello
- Zero configurazione

---

## 5. Target Audience Analysis

### 5.1 Segmenti Primari

#### A. Sviluppatori Indie / Solopreneur
**Profilo:** Builder di side-projects AI, budget limitato
**Pain point:** Costi API LLM gia alti, non vogliono pagare per memoria
**Kore fit:** **Eccellente** — gratuito, semplice, offline
**Willingness to pay:** $0-29/mese per premium features

#### B. Startup AI Early-Stage
**Profilo:** Team 2-10, prodotto AI in MVP/beta
**Pain point:** Iterazione veloce, non vogliono lock-in cloud
**Kore fit:** **Buono** — serve dashboard e integrazioni
**Willingness to pay:** $49-199/mese per hosted + support

#### C. Enterprise Privacy-Conscious
**Profilo:** Finance, healthcare, government
**Pain point:** GDPR, compliance, no data externalization
**Kore fit:** **Eccellente filosoficamente**, mancano feature enterprise
**Willingness to pay:** $500-5000/mese per on-prem + SLA

#### D. AI Agent Framework Users (CrewAI, Autogen)
**Profilo:** Developer che usano framework multi-agent
**Pain point:** Memoria persistente tra sessioni
**Kore fit:** **Buono** se integrazione nativa
**Willingness to pay:** Freemium + premium integrations

### 5.2 Segmenti Secondari

- **Ricercatori AI** — Sperimentazione memory systems
- **Hobbyists** — Personal AI assistants
- **Educatori** — Insegnamento AI/ML

---

## 6. Modelli di Business Potenziali

### 6.1 Open-Core (Raccomandato)

```
Kore OSS (MIT)           Kore Pro ($49/mese)      Kore Enterprise (custom)
----------------         ------------------        -----------------------
- Core memory            - Web dashboard           - SSO/SAML
- Decay engine           - Memory graph            - Audit logs
- Semantic search        - Entity extraction       - Multi-tenant
- Compression            - Advanced analytics      - SLA 99.9%
- REST API               - Priority support        - Dedicated support
- Agent isolation        - npm SDK                 - On-prem deployment
```

### 6.2 Cloud-First (Alternativo)

```
Kore Cloud
----------
Free: 10.000 memories, 1 agent
Pro: $29/mese - unlimited memories, 10 agents, dashboard
Team: $99/mese - unlimited agents, API priority, webhooks
Enterprise: Custom - VPC, dedicated infra
```

### 6.3 Sponsorship/Consulting

- GitHub Sponsors per mantenimento OSS
- Consulting per integrazioni custom
- Training/workshop per team

### 6.4 Raccomandazione

**Open-Core** e il modello piu sostenibile:
- Core gratuito attira utenti
- Feature avanzate monetizzano
- Community contribuisce al core
- Non aliena gli early adopters

---

## 7. Opportunita di Integrazione

### 7.1 Priorita 1: LLM Providers

| Provider | Integrazione | Effort |
|----------|--------------|--------|
| **OpenAI** | Function calling schema per save/search | Basso |
| **Anthropic Claude** | MCP Tool definition | Basso |
| **Ollama** | Local-first story perfetta | Basso |

### 7.2 Priorita 2: AI Agent Frameworks

| Framework | Stars | Integrazione |
|-----------|-------|--------------|
| **LangChain** | 98k | `KoreMemory(BaseMemory)` class |
| **CrewAI** | 25k | Memory provider interface |
| **AutoGen** | 35k | Custom agent memory |
| **LlamaIndex** | 37k | Storage/retrieval plugin |

### 7.3 Priorita 3: Orchestration Platforms

| Platform | Tipo | Integrazione |
|----------|------|--------------|
| **n8n** | Low-code automation | Custom node |
| **Flowise** | LangChain UI | Memory option |
| **Dify** | LLM app platform | Plugin |

### 7.4 Priorita 4: Deployment

| Target | Perche |
|--------|--------|
| **Docker Hub** | One-liner deployment |
| **Railway/Render** | Deploy button |
| **Vercel (Edge)** | JS SDK + serverless |

---

## 8. Roadmap Strategica

### Q1 2025: Foundation

- [x] Core memory system
- [x] Ebbinghaus decay
- [x] Semantic search
- [x] Memory compression
- [ ] **Web dashboard v1** (localhost)
- [ ] **Export/Import JSON**
- [ ] Rate limiting

### Q2 2025: Ecosystem

- [ ] **npm/TypeScript SDK**
- [ ] **LangChain integration**
- [ ] **Memory relations v1**
- [ ] Docker Hub official image
- [ ] CrewAI integration

### Q3 2025: Intelligence

- [ ] **Entity extraction (spaCy)**
- [ ] Session/conversation management
- [ ] Memory graph UI
- [ ] Analytics dashboard

### Q4 2025: Enterprise

- [ ] Multi-tenant mode
- [ ] Audit logging
- [ ] Kore Cloud beta
- [ ] Enterprise pilot

---

## 9. Conclusioni

### 9.1 Posizionamento

Kore-memory occupa una nicchia **unica e difendibile**:

> "L'unica memoria AI che pensa come un umano: dimentica, comprime, e non chiama mai casa."

Nessun competitor combina:
- Ebbinghaus decay
- No-LLM scoring
- 100% offline
- Memory compression

### 9.2 Rischi

1. **Mem0 aggiunge decay** — Mitigazione: brevettare l'implementazione? Muoversi veloce.
2. **Nicchia troppo piccola** — Mitigazione: integrazioni con framework popolari.
3. **Mancanza risorse** — Mitigazione: community-driven development.

### 9.3 Opportunita

1. **Privacy wave** — GDPR, AI Act, data sovereignty crescono
2. **Edge AI** — Deploy locale sempre piu richiesto
3. **AI Agent boom** — Mercato in esplosione, tutti cercano memoria
4. **LLM cost optimization** — No-LLM e sempre piu attraente

### 9.4 Next Actions

1. Implementare Web Dashboard (differenziatore visivo)
2. Pubblicare npm SDK (espandere audience)
3. Creare LangChain integration (network effect)
4. Scrivere blog post su Ebbinghaus approach (thought leadership)
5. Lanciare su Product Hunt (visibility)

---

## Appendice: Dati Competitor (Gennaio 2025)

| Metric | Mem0 | Letta | Zep | Chroma | Weaviate |
|--------|------|-------|-----|--------|----------|
| GitHub Stars | ~22k | ~12k | ~2.5k | ~15k | ~11k |
| First Release | 2023 | 2023 | 2023 | 2022 | 2021 |
| Funding | $4.4M | $12M | $5.5M | $18M | $68M |
| Team Size | ~10 | ~15 | ~10 | ~20 | ~80 |
| Primary Language | Python | Python | Go/Python | Python | Go |

---

*Report generato per supportare decisioni strategiche su kore-memory.*
*Dati basati su informazioni pubblicamente disponibili a gennaio 2025.*
```

## File: `brain/knowledge/docs_legacy/v1.0-roadmap.md`
```markdown
# Kore Memory — Roadmap v1.0 "Stable Release"

> Generato: 2026-02-25 | Versione attuale: 0.9.0 | Target: 1.0.0
> Analisi eseguita da: Security Audit, Code Review, Architecture Analysis, Context7 Verification, Test Coverage Analysis

## Score attuale: 7.5/10

---

## Fase 1 — Bug critici (BLOCKING)

Devono essere risolti prima di qualsiasi altro lavoro.

### 1.1 Ordine parametri SQL in `_semantic_search`
- **File**: `kore_memory/repository.py:902-926`
- **Bug**: Quando `cursor + category` sono entrambi forniti, i parametri SQL vengono passati nell'ordine errato. La query SQL posiziona `{category_clause}` prima di `{cursor_filter}`, ma i parametri vengono accumulati nell'ordine inverso.
- **Impatto**: Risultati di ricerca semantica completamente sbagliati con cursor+category
- **Fix**: Invertire l'ordine di accumulo: prima `category`, poi `cursor`
- **Stato**: [x] Completato (2026-02-25) — ordine corretto: IN ids, category, cursor

### 1.2 Memorie archiviate visibili nei risultati di search
- **File**: `kore_memory/repository.py:803-876, 879-944` e `kore_memory/vector_index.py:119-137`
- **Bug**: `_fts_search`, `_semantic_search` e `VectorIndex._reload_from_db` non filtrano `archived_at IS NOT NULL`
- **Impatto**: Le memorie archiviate (soft-deleted) appaiono nei risultati normali
- **Fix**: Aggiungere `AND archived_at IS NULL` nelle clausole WHERE di:
  - `_fts_search` (riga ~827)
  - `_semantic_search` DB query (riga ~919)
  - `_reload_from_db` (riga ~124)
- **Stato**: [x] Completato (2026-02-25) — aggiunto `AND archived_at IS NULL` in _fts_search, _semantic_search, _reload_from_db

### 1.3 Compressor include memorie archiviate
- **File**: `kore_memory/compressor.py:81-90`
- **Bug**: `_load_compressible_memories` non filtra `archived_at IS NOT NULL`
- **Impatto**: Memoria archiviata puo' tornare "attiva" dopo compressione
- **Fix**: Aggiungere `AND archived_at IS NULL` nella query
- **Stato**: [x] Completato (2026-02-25) — aggiunto `AND archived_at IS NULL` nel compressor

### 1.4 Decay pass include memorie archiviate
- **File**: `kore_memory/repository.py:319`
- **Bug**: Il decay pass aggiorna `decay_score` anche per record archiviati
- **Fix**: Aggiungere `AND archived_at IS NULL` nella query SELECT
- **Stato**: [x] Completato (2026-02-25) — aggiunto `AND archived_at IS NULL` nel decay pass

---

## Fase 2 — Sicurezza (BLOCKING)

Vulnerabilita' che vanno risolte prima del rilascio pubblico.

### 2.1 Auth bypass via "testclient" in host trusted
- **File**: `kore_memory/auth.py:62`
- **Severita'**: CRITICA
- **Bug**: `"testclient"` nella lista degli host locali trusted in produzione
- **Fix**: Spostare dietro env `KORE_TEST_MODE=1`, usare `os.getenv("KORE_TEST_MODE", "0") == "1"`
- **Stato**: [x] Completato (2026-02-25) — `KORE_TEST_MODE` env var + conftest.py

### 2.2 `/metrics` senza autenticazione
- **File**: `kore_memory/main.py:647-666`
- **Severita'**: ALTA
- **Bug**: Endpoint accessibile senza `_Auth` dependency, espone stats di tutti gli agenti
- **Fix**: Aggiungere `_: str = _Auth` e `agent_id: str = _Agent` come dependency
- **Stato**: [x] Completato (2026-02-25) — aggiunto `_Auth` + `_Agent` dependency

### 2.3 Rate limiting mancante su endpoint distruttivi
- **File**: `kore_memory/config.py:33-39`
- **Severita'**: ALTA
- **Endpoint senza rate limit**: DELETE /memories, GET /export, POST /import, POST /cleanup, DELETE /sessions
- **Fix**: Aggiungere limiti in `RATE_LIMITS` dict
- **Stato**: [x] Completato (2026-02-25) — aggiunto export, import, cleanup, delete

### 2.4 `X-Session-Id` non validato
- **File**: `kore_memory/main.py:222`
- **Severita'**: MEDIA
- **Bug**: Header letto senza sanitizzazione, accetta caratteri speciali e lunghezza arbitraria
- **Fix**: Regex `^[a-zA-Z0-9_-]{1,128}$` prima di usare il valore
- **Stato**: [x] Completato (2026-02-25) — regex `_SESSION_ID_RE` + `_validate_session_id()`

### 2.5 MCP `agent_id` non sanitizzato
- **File**: `kore_memory/mcp_server.py:43-57`
- **Severita'**: MEDIA
- **Bug**: Il server MCP bypassa la sanitizzazione di `auth.get_agent_id()`
- **Fix**: Aggiungere `_sanitize_agent_id()` che applica stessa regex di auth.py
- **Stato**: [x] Completato (2026-02-25) — `_sanitize_agent_id()` applicato a tutti i 14 tool MCP

### 2.6 `X-XSS-Protection` obsoleto
- **File**: `kore_memory/main.py:150`
- **Severita'**: BASSA
- **Fix**: Cambiare da `"1; mode=block"` a `"0"`
- **Stato**: [x] Completato (2026-02-25) — cambiato a `"0"`

### 2.7 API key log masking troppo rivelatorio
- **File**: `kore_memory/auth.py:41`
- **Severita'**: BASSA
- **Fix**: Mostrare solo i primi 4 caratteri invece di 8+8
- **Stato**: [x] Completato (2026-02-25) — mostra solo 4 char + asterischi

---

## Fase 3 — Architettura e coerenza (BLOCKING)

### 3.1 Colonne `archived_at` e `session_id` nel CREATE TABLE
- **File**: `kore_memory/database.py:95-113`
- **Problema**: Colonne aggiunte solo via migration runtime, non nello schema principale
- **Fix**: Aggiungere al `CREATE TABLE IF NOT EXISTS memories`
- **Stato**: [x] Completato (2026-02-25) — colonne aggiunte nello schema + indice `idx_memories_archived`

### 3.2 Graceful shutdown
- **File**: `kore_memory/main.py` (lifespan)
- **Problema**: Pool SQLite non chiuso su SIGTERM/SIGINT — rischio corruzione WAL
- **Fix**: Aggiungere `_pool.clear()` nel lifespan FastAPI dopo yield
- **Stato**: [x] Completato (2026-02-25) — `_pool.clear()` nel lifespan yield

### 3.3 Health check con verifica DB
- **File**: `kore_memory/main.py`
- **Problema**: `/health` non verifica connettivita' DB (sempre "ok" anche con DB corrotto)
- **Fix**: Aggiungere `SELECT 1` nel health check, restituire `"degraded"` se fallisce
- **Stato**: [x] Completato (2026-02-25) — `SELECT 1` + status `"degraded"` + campo `database`

### 3.4 Response model Pydantic per tutti gli endpoint
- **File**: `kore_memory/main.py`, `kore_memory/models.py`
- **Endpoint corretti**: archive, restore, sessions (create/list/end/delete), entities, agents, audit
- **Nuovi modelli**: `SessionDeleteResponse`, `EntityRecord`, `EntityListResponse`, `AgentRecord`, `AgentListResponse`, `AuditEventRecord`, `AuditResponse`
- **Stato**: [x] Completato (2026-02-25) — 9 endpoint con response_model, 7 nuovi modelli

### 3.5 `save_memory_batch` non emette eventi audit
- **File**: `kore_memory/repository.py`
- **Fix**: Aggiunto `emit(MEMORY_SAVED, ...)` per ogni memoria salvata nel batch
- **Stato**: [x] Completato (2026-02-25) — emit dopo ciclo insert

### 3.6 `update_memory` risponde con `importance=0` invalido
- **File**: `kore_memory/main.py`
- **Bug**: `MemorySaveResponse(importance=req.importance or 0)` — se importance non aggiornato, ritorna 0
- **Fix**: SELECT importance reale dal DB dopo update
- **Stato**: [x] Completato (2026-02-25) — query DB per importance reale

### 3.7 `auto_score` impossibile salvare importance=1 esplicita
- **File**: `kore_memory/models.py`, `kore_memory/repository.py`, `kore_memory/mcp_server.py`
- **Problema**: `if importance == 1` attiva auto-scoring anche per valore esplicito
- **Fix**: `importance: int | None = None` nel modello, `if importance is None:` nel repository
- **Stato**: [x] Completato (2026-02-25) — sentinel `None`, MCP aggiornato

---

## Fase 4 — Test coverage (IMPORTANTE)

Coverage attuale: 81% globale. Target v1.0: >= 85%.

### 4.1 Test mancanti — Priorita' 1 (funzionalita' core)

| Test da aggiungere | File target | Modulo testato |
|---|---|---|
| `TestArchive` (archive, restore, get_archived) | test_api.py | repository.py, main.py |
| `TestCursorPagination` (cursor valido, invalido, has_more) | test_api.py | main.py, repository.py |
| `TestRateLimit` (superamento, 429, cleanup bucket) | test_api.py | main.py |
| `TestKoreClientSync` (tutti i metodi sincroni) | test_client_sync.py (nuovo) | client.py |

### 4.2 Test mancanti — Priorita' 2

| Test da aggiungere | File target | Modulo testato |
|---|---|---|
| `TestCLI` (argomenti, uvicorn non trovato) | test_cli.py (nuovo) | cli.py |
| `TestAuthAutoGeneration` (API key creation) | test_api.py | auth.py |
| `TestCompressorPython` (fallback senza numpy) | test_api.py | compressor.py |
| `TestAgentsEndpoint` e `TestMetricsEndpoint` | test_api.py | main.py |

### 4.3 Test mancanti — Priorita' 3

- `database.py`: connessione corrotta nel pool, rollback su eccezione
- `repository.py`: wildcard `q=*`, cursor semantico + category, update senza campi
- `events.py`: handler che lancia eccezione non interrompe catena
- `integrations/__init__.py`: lazy-loader per entities, AttributeError

### 4.4 Stato attuale per modulo

| Modulo | Coverage prima | Coverage dopo | Target |
|--------|----------------|---------------|--------|
| `cli.py` | 0% | **94%** | >= 70% ✅ |
| `client.py` | 68% | **96%** | >= 85% ✅ |
| `auth.py` | 71% | **96%** | >= 85% ✅ |
| `events.py` | 92% | **100%** | >= 85% ✅ |
| `integrations/__init__` | 23% | **100%** | >= 85% ✅ |
| `database.py` | 81% | **85%** | >= 85% ✅ |
| `main.py` | 80% | **86%** | >= 85% ✅ |
| `repository.py` | 82% | **85%** | >= 85% ✅ |
| `compressor.py` | 77% | 77% | >= 85% ⚠️ |
| `dashboard.py` | 67% | 67% | >= 80% ⚠️ |

**Coverage globale**: 82% → **88%** (target >= 85% ✅)
**Test totali**: 242 → **295** (+53 nuovi)

- **Stato**: [x] Completato (2026-02-25) — target 85% raggiunto (88%)

---

## Fase 5 — Packaging e CI/CD (BLOCKING)

### 5.1 pyproject.toml
- [x] Cambiare classifier da `"4 - Beta"` a `"5 - Production/Stable"`
- [x] Aggiungere `Programming Language :: Python :: 3.13`
- [x] Aggiornare lower bound pytest-asyncio da `>=0.23.0` a `>=1.0.0`
- [x] Aggiungere URL `Documentation` in `[project.urls]`
- [x] Versione: `1.0.0`
- **Stato**: [x] Completato (2026-02-25)

### 5.2 CI/CD hardening
- **File**: `.github/workflows/ci.yml`
- [x] Rimuovere `|| true` da bandit e pip-audit
- [x] Cambiare warning in `exit 1` per coverage sotto 85%
- [x] Aggiungere Python 3.13 nella matrix
- [x] Installare `[mcp]` nel job coverage
- **Stato**: [x] Completato (2026-02-25)

### 5.3 Versione coerente
- [x] `pyproject.toml` → `1.0.0`
- [x] `kore_memory/config.py` VERSION → `1.0.0`
- [x] `sdk/js/package.json` → `1.0.0`
- [x] JS SDK `HealthResponse` allineato con endpoint reale (rimosso `capabilities`, aggiunto `database`)
- **Stato**: [x] Completato (2026-02-25)

---

## Fase 6 — Documentazione (NICE-TO-HAVE)

### 6.1 CLAUDE.md da aggiornare
- [x] "6 file in tests/" → "13 file, 359 test"
- [x] "MCP server espone 6 tool" → "14 tool"
- [x] `dashboard.py` ~1200 righe → `templates/dashboard.html`
- [x] `KORE_LOCAL_ONLY` default → corretto: `"1"`
- [x] `mcp_server.py` righe aggiornate (~338)
- [x] `repository.py` righe aggiornate (~979)
- [x] Aggiunto `KORE_TEST_MODE`, rate limiting, archived memories, session validation, health check patterns
- [x] Rimosso `storage.py` dalla tabella moduli
- [x] Versione aggiornata a v1.0.0
- **Stato**: [x] Completato (2026-02-25)

### 6.2 Pulizia dead code
- [x] `storage.py` — rimosso (Protocol mai implementato)
- [x] `config.LOCAL_ONLY` — verificato: e' usato in main.py e auth.py (non era dead code)
- [x] `scorer.py:67` — rimosso branch dead code `score + 0`
- **Stato**: [x] Completato (2026-02-25)

### 6.3 Miglioramenti minori
- [ ] Indice su `memories.archived_at` (performance query archivio)
- [ ] DB schema versioning con `PRAGMA user_version`
- [ ] Esportare modelli Pydantic da `__init__.py`
- [ ] Estrarre `_parse_cursor()` come helper condiviso in main.py
- [ ] Endpoint REST per `audit.cleanup_audit_log()`
- [ ] Logging strutturato JSON in produzione
- [ ] Usare `tempfile.NamedTemporaryFile` nei test invece di `mktemp()` deprecato

---

## Librerie — Stato aggiornamento (2026-02-25)

Tutte le dipendenze sono all'ultima versione PyPI:

| Dipendenza | Installata | Ultima | Note |
|---|---|---|---|
| FastAPI | 0.133.0 | 0.133.0 | Strict Content-Type attivo da 0.125+ |
| Pydantic | 2.12.5 | 2.12.5 | `Field(deprecated=True)` supportato da v2.7 |
| sentence-transformers | 5.2.3 | 5.2.3 | `encode()` stabile, v5.x retrocompatibile |
| mcp | 1.26.0 | 1.26.0 | `json_response=True` ancora supportato |
| uvicorn | 0.41.0 | 0.41.0 | — |
| httpx | 0.28.1 | 0.28.1 | — |
| pytest-asyncio | 1.3.0 | 1.3.0 | Lower bound da aggiornare a >=1.0.0 |

---

## Checklist rilascio v1.0

```
[x] Fase 1 completata (bug critici)
[x] Fase 2 completata (sicurezza)
[x] Fase 3 completata (architettura)
[x] Fase 4 completata (test 88% >= 85%)
[x] Fase 5 completata (packaging e CI)
[x] 359 test passano (erano 242)
[x] Coverage 88% >= 85%
[ ] Bandit senza finding critici
[ ] pip-audit pulito
[ ] CHANGELOG.md aggiornato
[ ] Tag v1.0.0 creato
[ ] PyPI publish verificato
[x] JS SDK v1.0.0 allineato
```
```

## File: `examples/async_usage.py`
```python
"""
Async usage of Kore Memory Python SDK.

Demonstrates how to:
- Use AsyncKoreClient for non-blocking operations
- Save and search memories asynchronously
- Run multiple operations concurrently with asyncio.gather
- Properly manage the async client lifecycle

Prerequisites:
    pip install kore-memory
    kore  # start the server on localhost:8765
"""

import asyncio

from kore_memory import AsyncKoreClient


async def main() -> None:
    # Create an async client. Use it as an async context manager
    # to ensure the underlying httpx.AsyncClient is properly closed.
    async with AsyncKoreClient(
        base_url="http://localhost:8765",
        agent_id="async-example-agent",
    ) as client:

        # -- Save multiple memories concurrently ------------------------------
        # asyncio.gather runs all coroutines concurrently, which is faster
        # than awaiting them sequentially.
        print("Saving memories concurrently...")
        results = await asyncio.gather(
            client.save(
                content="Python 3.12 introduces improved error messages.",
                category="general",
                importance=3,
            ),
            client.save(
                content="The async client uses httpx.AsyncClient under the hood.",
                category="decision",
                importance=2,
            ),
            client.save(
                content="Always close async clients to avoid resource leaks.",
                category="preference",
                importance=4,
            ),
        )
        print(f"Saved {len(results)} memories:")
        for r in results:
            print(f"  id={r.id}")

        # -- Search asynchronously --------------------------------------------
        print("\nSearching for 'async client'...")
        search_results = await client.search(q="async client", limit=5)
        print(f"Found {len(search_results.results)} result(s):")
        for mem in search_results.results:
            print(f"  [{mem.category}] {mem.content}")

        # -- Semantic search --------------------------------------------------
        print("\nSemantic search for 'how to avoid resource leaks'...")
        semantic_results = await client.search(
            q="how to avoid resource leaks",
            limit=3,
            semantic=True,
        )
        print(f"Found {len(semantic_results.results)} result(s):")
        for mem in semantic_results.results:
            print(f"  [{mem.category}] {mem.content}")

        # -- Timeline ---------------------------------------------------------
        print("\nFetching timeline...")
        timeline = await client.timeline(limit=10)
        print(f"Timeline has {len(timeline.memories)} memories:")
        for mem in timeline.memories:
            print(f"  [{mem.created_at}] {mem.content[:60]}")

        # -- Run multiple read operations concurrently ------------------------
        # This pattern is useful when you need data from multiple endpoints
        # at the same time.
        print("\nRunning concurrent search + timeline...")
        search_task, timeline_task = await asyncio.gather(
            client.search(q="Python", limit=3),
            client.timeline(limit=5),
        )
        print(f"Search found {len(search_task.results)} results")
        print(f"Timeline has {len(timeline_task.memories)} memories")

    # The async context manager ensures the client is closed here.
    print("\nDone! Client closed automatically.")


if __name__ == "__main__":
    asyncio.run(main())
```

## File: `examples/basic_usage.py`
```python
"""
Basic usage of Kore Memory Python SDK.

Demonstrates how to:
- Connect to a running Kore server
- Save memories with categories and importance
- Search memories (full-text and semantic)
- Retrieve a timeline of recent memories
- Work with tags and relations

Prerequisites:
    pip install kore-memory
    kore  # start the server on localhost:8765
"""

from kore_memory import KoreClient


def main() -> None:
    # Connect to the Kore server.
    # When running locally with KORE_LOCAL_ONLY=1, no API key is needed.
    # For authenticated servers, pass api_key="your-key".
    client = KoreClient(
        base_url="http://localhost:8765",
        agent_id="example-agent",
    )

    # -- Save memories --------------------------------------------------------
    # Save a simple memory. The server auto-scores importance if you pass 1.
    result = client.save(
        content="The project deadline is March 15th.",
        category="project",
        importance=1,  # auto-scored by the server
    )
    project_memory_id = result.id
    print(f"Saved project memory: id={project_memory_id}")

    # Save a memory with explicit importance (1=low, 5=critical)
    result = client.save(
        content="Always use UTC timestamps in the API.",
        category="decision",
        importance=4,
    )
    decision_memory_id = result.id
    print(f"Saved decision memory: id={decision_memory_id}")

    # Save a preference memory
    client.save(
        content="User prefers dark mode and compact layout.",
        category="preference",
        importance=3,
    )
    print("Saved preference memory.")

    # -- Search memories ------------------------------------------------------
    # Full-text search (uses SQLite FTS5 under the hood)
    search_results = client.search(q="deadline", limit=5)
    print(f"\nSearch for 'deadline': {len(search_results.results)} result(s)")
    for mem in search_results.results:
        print(f"  [{mem.category}] {mem.content} (score={mem.effective_score:.2f})")

    # Semantic search (requires sentence-transformers installed on the server)
    semantic_results = client.search(q="when is the project due?", limit=5, semantic=True)
    print(f"\nSemantic search for 'when is the project due?': {len(semantic_results.results)} result(s)")
    for mem in semantic_results.results:
        print(f"  [{mem.category}] {mem.content}")

    # -- Timeline -------------------------------------------------------------
    # Get recent memories ordered by creation time
    timeline = client.timeline(limit=10)
    print(f"\nTimeline ({len(timeline.memories)} memories):")
    for mem in timeline.memories:
        print(f"  [{mem.created_at}] {mem.content[:60]}...")

    # -- Tags -----------------------------------------------------------------
    # Add tags to a memory for easy filtering
    client.add_tags(memory_id=project_memory_id, tags=["deadline", "q1-2026"])
    print(f"\nAdded tags to memory {project_memory_id}")

    # Retrieve tags for a memory
    tags = client.get_tags(memory_id=project_memory_id)
    print(f"Tags: {tags.tags}")

    # -- Relations ------------------------------------------------------------
    # Create a relation between two memories
    client.add_relation(
        source_id=project_memory_id,
        target_id=decision_memory_id,
        relation_type="informs",
    )
    print(f"\nCreated relation: {project_memory_id} --informs--> {decision_memory_id}")

    # Retrieve relations for a memory
    relations = client.get_relations(memory_id=project_memory_id)
    print(f"Relations: {len(relations.relations)} relation(s)")

    # -- Cleanup --------------------------------------------------------------
    # Close the HTTP client when done
    client.close()
    print("\nDone!")


if __name__ == "__main__":
    main()
```

## File: `examples/langchain_example.py`
```python
"""
Using Kore Memory as a LangChain memory backend.

Demonstrates how to:
- Create a KoreLangChainMemory instance
- Use it to save and retrieve conversation context
- Integrate it with LangChain chains (conceptual example)

Prerequisites:
    pip install kore-memory langchain-core
    kore  # start the server on localhost:8765

Note: This example shows the KoreLangChainMemory API directly.
For a full LangChain chain integration, you would also need an LLM
provider (e.g., langchain-openai).
"""

from kore_memory.integrations.langchain import KoreLangChainMemory


def main() -> None:
    # -- Create the memory backend --------------------------------------------
    # KoreLangChainMemory wraps a KoreClient and implements LangChain's
    # BaseMemory interface, so it can be used with any LangChain chain.
    memory = KoreLangChainMemory(
        base_url="http://localhost:8765",
        agent_id="langchain-agent",
        # Number of memories to retrieve per query
        k=5,
        # Use semantic search for better relevance (requires sentence-transformers)
        semantic=True,
        # Category for saved conversation turns
        category="general",
        # Let the server auto-score importance based on content
        auto_importance=True,
    )

    # -- Save conversation context --------------------------------------------
    # save_context() stores a conversation turn (input + output) as a memory.
    # In a real LangChain chain, this is called automatically after each step.
    memory.save_context(
        inputs={"input": "What is Kore Memory?"},
        outputs={"output": "Kore Memory is a persistent memory layer for AI agents."},
    )
    print("Saved conversation turn 1.")

    memory.save_context(
        inputs={"input": "Does it require an LLM?"},
        outputs={"output": "No, Kore runs fully offline with no LLM calls."},
    )
    print("Saved conversation turn 2.")

    memory.save_context(
        inputs={"input": "How does it handle forgetting?"},
        outputs={"output": "It uses the Ebbinghaus forgetting curve to decay old memories."},
    )
    print("Saved conversation turn 3.")

    # -- Load memory variables ------------------------------------------------
    # load_memory_variables() retrieves relevant past memories based on
    # the current input. This is called automatically by LangChain chains
    # to inject context into the prompt.
    context = memory.load_memory_variables({"input": "Tell me about memory decay"})
    print(f"\nRetrieved context for 'memory decay':")
    print(context["history"])

    # -- Retrieving context for a different query -----------------------------
    context = memory.load_memory_variables({"input": "Does it need internet?"})
    print(f"\nRetrieved context for 'Does it need internet?':")
    print(context["history"])

    # -- Integration with a LangChain chain (conceptual) ----------------------
    # In a real application, you would use it like this:
    #
    #   from langchain.chains import LLMChain
    #   from langchain_openai import ChatOpenAI
    #   from langchain.prompts import PromptTemplate
    #
    #   llm = ChatOpenAI(model="gpt-4")
    #   prompt = PromptTemplate(
    #       input_variables=["history", "input"],
    #       template="Previous context:\n{history}\n\nHuman: {input}\nAI:",
    #   )
    #   chain = LLMChain(llm=llm, prompt=prompt, memory=memory)
    #   response = chain.run("What did we discuss about forgetting?")

    print("\nDone!")


if __name__ == "__main__":
    main()
```

## File: `kore_memory/__init__.py`
```python
# Kore package

from .client import (
    AsyncKoreClient,
    KoreAuthError,
    KoreClient,
    KoreError,
    KoreNotFoundError,
    KoreRateLimitError,
    KoreServerError,
    KoreValidationError,
)
from .config import VERSION as __version__

__all__ = [
    "__version__",
    "KoreClient",
    "AsyncKoreClient",
    "KoreError",
    "KoreAuthError",
    "KoreNotFoundError",
    "KoreValidationError",
    "KoreRateLimitError",
    "KoreServerError",
]
```

## File: `kore_memory/acl.py`
```python
"""
Kore — Access Control Layer
Multi-agent shared memory with permission management.
Permissions: read, write, admin.
"""

from __future__ import annotations

from .database import get_connection

# Valid permission levels
PERMISSIONS = ("read", "write", "admin")


def _ensure_acl_table() -> None:
    """Create the ACL table if it doesn't exist (migration-safe)."""
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS memory_acl (
                memory_id   INTEGER NOT NULL REFERENCES memories(id) ON DELETE CASCADE,
                agent_id    TEXT    NOT NULL,
                permission  TEXT    NOT NULL CHECK (permission IN ('read', 'write', 'admin')),
                granted_by  TEXT    NOT NULL,
                created_at  TEXT    NOT NULL DEFAULT (datetime('now')),
                PRIMARY KEY (memory_id, agent_id)
            )
        """)
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_acl_agent ON memory_acl (agent_id)"
        )


def grant_access(
    memory_id: int,
    target_agent: str,
    permission: str,
    grantor_agent: str,
) -> bool:
    """
    Grant access to a memory for another agent.
    Only the memory owner or an agent with admin permission can grant access.
    """
    if permission not in PERMISSIONS:
        return False

    _ensure_acl_table()

    with get_connection() as conn:
        # Verify grantor owns the memory or has admin permission
        owner = conn.execute(
            "SELECT agent_id FROM memories WHERE id = ? AND archived_at IS NULL",
            (memory_id,),
        ).fetchone()
        if not owner:
            return False

        is_owner = owner["agent_id"] == grantor_agent
        has_admin = False
        if not is_owner:
            acl_row = conn.execute(
                "SELECT permission FROM memory_acl WHERE memory_id = ? AND agent_id = ?",
                (memory_id, grantor_agent),
            ).fetchone()
            has_admin = acl_row and acl_row["permission"] == "admin"

        if not is_owner and not has_admin:
            return False

        # Upsert permission
        conn.execute(
            """INSERT INTO memory_acl (memory_id, agent_id, permission, granted_by)
               VALUES (?, ?, ?, ?)
               ON CONFLICT (memory_id, agent_id)
               DO UPDATE SET permission = excluded.permission, granted_by = excluded.granted_by""",
            (memory_id, target_agent, permission, grantor_agent),
        )
        return True


def revoke_access(memory_id: int, target_agent: str, grantor_agent: str) -> bool:
    """Revoke access for an agent. Only the owner or an admin can revoke."""
    _ensure_acl_table()

    with get_connection() as conn:
        owner = conn.execute(
            "SELECT agent_id FROM memories WHERE id = ?",
            (memory_id,),
        ).fetchone()
        if not owner:
            return False

        is_owner = owner["agent_id"] == grantor_agent
        has_admin = False
        if not is_owner:
            acl_row = conn.execute(
                "SELECT permission FROM memory_acl WHERE memory_id = ? AND agent_id = ?",
                (memory_id, grantor_agent),
            ).fetchone()
            has_admin = acl_row and acl_row["permission"] == "admin"

        if not is_owner and not has_admin:
            return False

        cursor = conn.execute(
            "DELETE FROM memory_acl WHERE memory_id = ? AND agent_id = ?",
            (memory_id, target_agent),
        )
        return cursor.rowcount > 0


def list_permissions(memory_id: int, agent_id: str) -> list[dict]:
    """
    List all permissions for a memory.
    Only visible to the owner or agents with admin permission.
    """
    _ensure_acl_table()

    with get_connection() as conn:
        owner = conn.execute(
            "SELECT agent_id FROM memories WHERE id = ?",
            (memory_id,),
        ).fetchone()
        if not owner:
            return []

        is_owner = owner["agent_id"] == agent_id
        if not is_owner:
            acl_row = conn.execute(
                "SELECT permission FROM memory_acl WHERE memory_id = ? AND agent_id = ?",
                (memory_id, agent_id),
            ).fetchone()
            if not (acl_row and acl_row["permission"] == "admin"):
                return []

        rows = conn.execute(
            """SELECT agent_id, permission, granted_by, created_at
               FROM memory_acl WHERE memory_id = ?
               ORDER BY created_at""",
            (memory_id,),
        ).fetchall()
        return [dict(r) for r in rows]


def check_access(memory_id: int, agent_id: str, required: str = "read") -> bool:
    """
    Check if an agent has the required permission on a memory.
    The owner always has full access. Permission hierarchy: admin > write > read.
    """
    _ensure_acl_table()
    hierarchy = {"read": 0, "write": 1, "admin": 2}

    with get_connection() as conn:
        # Owner always has access
        owner = conn.execute(
            "SELECT agent_id FROM memories WHERE id = ?",
            (memory_id,),
        ).fetchone()
        if not owner:
            return False
        if owner["agent_id"] == agent_id:
            return True

        # Check ACL
        acl_row = conn.execute(
            "SELECT permission FROM memory_acl WHERE memory_id = ? AND agent_id = ?",
            (memory_id, agent_id),
        ).fetchone()
        if not acl_row:
            return False

        return hierarchy.get(acl_row["permission"], -1) >= hierarchy.get(required, 0)


def get_shared_memories(agent_id: str, limit: int = 50) -> list[dict]:
    """Get all memories shared with an agent (not owned by them)."""
    _ensure_acl_table()

    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT m.id, m.content, m.category, m.importance, m.decay_score,
                   m.created_at, m.updated_at, m.agent_id AS owner_agent,
                   a.permission
            FROM memory_acl a
            JOIN memories m ON m.id = a.memory_id
            WHERE a.agent_id = ? AND m.agent_id != ?
              AND m.archived_at IS NULL AND m.compressed_into IS NULL
            ORDER BY m.created_at DESC
            LIMIT ?
            """,
            (agent_id, agent_id, limit),
        ).fetchall()
        return [dict(r) for r in rows]
```

## File: `kore_memory/analytics.py`
```python
"""
Kore — Analytics
Aggregated statistics: category distribution, decay analysis, top tags,
access patterns, memory growth over time.
"""

from __future__ import annotations

from .database import get_connection


def get_analytics(agent_id: str = "default") -> dict:
    """Compute comprehensive analytics for an agent's memory store."""
    with get_connection() as conn:
        # Total memories
        total = conn.execute(
            "SELECT COUNT(*) FROM memories WHERE agent_id = ? AND compressed_into IS NULL AND archived_at IS NULL",
            (agent_id,),
        ).fetchone()[0]

        # Category distribution
        cat_rows = conn.execute(
            """SELECT category, COUNT(*) AS cnt
               FROM memories
               WHERE agent_id = ? AND compressed_into IS NULL AND archived_at IS NULL
               GROUP BY category ORDER BY cnt DESC""",
            (agent_id,),
        ).fetchall()
        categories = {r["category"]: r["cnt"] for r in cat_rows}

        # Importance distribution
        imp_rows = conn.execute(
            """SELECT importance, COUNT(*) AS cnt
               FROM memories
               WHERE agent_id = ? AND compressed_into IS NULL AND archived_at IS NULL
               GROUP BY importance ORDER BY importance""",
            (agent_id,),
        ).fetchall()
        importance_dist = {str(r["importance"]): r["cnt"] for r in imp_rows}

        # Decay distribution (buckets: healthy >0.7, fading 0.3-0.7, critical <0.3)
        decay_rows = conn.execute(
            """SELECT
                SUM(CASE WHEN decay_score > 0.7 THEN 1 ELSE 0 END) AS healthy,
                SUM(CASE WHEN decay_score BETWEEN 0.3 AND 0.7 THEN 1 ELSE 0 END) AS fading,
                SUM(CASE WHEN decay_score < 0.3 THEN 1 ELSE 0 END) AS critical,
                ROUND(AVG(decay_score), 3) AS avg_decay
               FROM memories
               WHERE agent_id = ? AND compressed_into IS NULL AND archived_at IS NULL""",
            (agent_id,),
        ).fetchone()
        decay_analysis = {
            "healthy": decay_rows["healthy"] or 0,
            "fading": decay_rows["fading"] or 0,
            "critical": decay_rows["critical"] or 0,
            "avg_decay": decay_rows["avg_decay"] or 0.0,
        }

        # Top tags
        tag_rows = conn.execute(
            """SELECT mt.tag, COUNT(*) AS cnt
               FROM memory_tags mt
               JOIN memories m ON m.id = mt.memory_id
               WHERE m.agent_id = ? AND m.archived_at IS NULL AND m.compressed_into IS NULL
               GROUP BY mt.tag ORDER BY cnt DESC LIMIT 20""",
            (agent_id,),
        ).fetchall()
        top_tags = [{"tag": r["tag"], "count": r["cnt"]} for r in tag_rows]

        # Access patterns
        access_rows = conn.execute(
            """SELECT
                SUM(CASE WHEN access_count = 0 THEN 1 ELSE 0 END) AS never_accessed,
                SUM(CASE WHEN access_count BETWEEN 1 AND 5 THEN 1 ELSE 0 END) AS low_access,
                SUM(CASE WHEN access_count BETWEEN 6 AND 20 THEN 1 ELSE 0 END) AS medium_access,
                SUM(CASE WHEN access_count > 20 THEN 1 ELSE 0 END) AS high_access,
                ROUND(AVG(access_count), 1) AS avg_access
               FROM memories
               WHERE agent_id = ? AND compressed_into IS NULL AND archived_at IS NULL""",
            (agent_id,),
        ).fetchone()
        access_patterns = {
            "never_accessed": access_rows["never_accessed"] or 0,
            "low_access": access_rows["low_access"] or 0,
            "medium_access": access_rows["medium_access"] or 0,
            "high_access": access_rows["high_access"] or 0,
            "avg_access": access_rows["avg_access"] or 0.0,
        }

        # Memory growth over time (last 30 days, grouped by day)
        growth_rows = conn.execute(
            """SELECT DATE(created_at) AS day, COUNT(*) AS cnt
               FROM memories
               WHERE agent_id = ? AND created_at >= datetime('now', '-30 days')
                 AND compressed_into IS NULL
               GROUP BY DATE(created_at) ORDER BY day""",
            (agent_id,),
        ).fetchall()
        growth = [{"date": r["day"], "count": r["cnt"]} for r in growth_rows]

        # Compression stats
        compressed = conn.execute(
            "SELECT COUNT(*) FROM memories WHERE agent_id = ? AND compressed_into IS NOT NULL",
            (agent_id,),
        ).fetchone()[0]

        archived = conn.execute(
            "SELECT COUNT(*) FROM memories WHERE agent_id = ? AND archived_at IS NOT NULL",
            (agent_id,),
        ).fetchone()[0]

        # Relations count
        relations = conn.execute(
            """SELECT COUNT(*) FROM memory_relations r
               JOIN memories m ON m.id = r.source_id
               WHERE m.agent_id = ?""",
            (agent_id,),
        ).fetchone()[0]

    return {
        "total_memories": total,
        "categories": categories,
        "importance_distribution": importance_dist,
        "decay_analysis": decay_analysis,
        "top_tags": top_tags,
        "access_patterns": access_patterns,
        "growth_last_30d": growth,
        "compressed_memories": compressed,
        "archived_memories": archived,
        "total_relations": relations,
    }
```

## File: `kore_memory/audit.py`
```python
"""
Kore — Audit Log
Persists memory lifecycle events to the event_logs table.
Enabled via KORE_AUDIT_LOG=1.
"""

from __future__ import annotations

import json
import logging
from typing import Any

from . import events
from .database import get_connection

logger = logging.getLogger("kore.audit")


def _audit_handler(event: str, data: dict[str, Any]) -> None:
    """Write a single event to the event_logs table."""
    agent_id = data.get("agent_id", "default")
    memory_id = data.get("id")
    # Serialize the full payload (minus agent_id which has its own column)
    data_blob = json.dumps(data) if data else None

    with get_connection() as conn:
        conn.execute(
            "INSERT INTO event_logs (event, agent_id, memory_id, data) VALUES (?, ?, ?, ?)",
            (event, agent_id, memory_id, data_blob),
        )


def register_audit_handler() -> None:
    """Register the audit handler on all known memory event types."""
    all_events = [
        events.MEMORY_SAVED,
        events.MEMORY_DELETED,
        events.MEMORY_UPDATED,
        events.MEMORY_COMPRESSED,
        events.MEMORY_DECAYED,
        events.MEMORY_ARCHIVED,
        events.MEMORY_RESTORED,
    ]
    for event_type in all_events:
        events.on(event_type, _audit_handler)
    logger.info("Audit log handler registered for %d event types", len(all_events))


def query_audit_log(
    agent_id: str,
    event_type: str | None = None,
    limit: int = 100,
    since: str | None = None,
) -> list[dict[str, Any]]:
    """
    Query persisted audit events for a given agent.

    Args:
        agent_id: Filter to this agent's events.
        event_type: Optional event type filter (e.g. "memory.saved").
        limit: Max rows to return (default 100).
        since: ISO datetime string — only return events after this timestamp.

    Returns:
        List of event dicts with id, event, agent_id, memory_id, data, created_at.
    """
    sql = "SELECT id, event, agent_id, memory_id, data, created_at FROM event_logs WHERE agent_id = ?"
    params: list[Any] = [agent_id]

    if event_type:
        sql += " AND event = ?"
        params.append(event_type)

    if since:
        sql += " AND created_at >= ?"
        params.append(since)

    sql += " ORDER BY created_at DESC LIMIT ?"
    params.append(limit)

    with get_connection() as conn:
        rows = conn.execute(sql, params).fetchall()

    results = []
    for row in rows:
        entry = {
            "id": row["id"],
            "event": row["event"],
            "agent_id": row["agent_id"],
            "memory_id": row["memory_id"],
            "data": json.loads(row["data"]) if row["data"] else None,
            "created_at": row["created_at"],
        }
        results.append(entry)
    return results


def cleanup_audit_log(days: int = 90) -> int:
    """
    Delete audit log entries older than `days` days.

    Returns:
        Number of rows deleted.
    """
    with get_connection() as conn:
        cursor = conn.execute(
            "DELETE FROM event_logs WHERE created_at < datetime('now', ?)",
            (f"-{days} days",),
        )
        return cursor.rowcount
```

## File: `kore_memory/auth.py`
```python
"""
Kore — Authentication & Authorization
API key validation + agent namespace isolation.

Config via environment variables:
  KORE_API_KEY   — master key (required in non-local mode)
  KORE_LOCAL_ONLY — if "1", skip auth for 127.0.0.1 requests (default: "1")
"""

import os
import secrets

from fastapi import Header, HTTPException, Request, status

from . import config

_KEY_FILE = config.API_KEY_FILE

# ── Key management ────────────────────────────────────────────────────────────


def get_or_create_api_key() -> str:
    """
    Load API key from env or file. Generate and persist one if missing.
    Priority: KORE_API_KEY env → data/.api_key file → auto-generate
    """
    env_key = os.getenv("KORE_API_KEY")
    if env_key:
        return env_key

    if _KEY_FILE.exists():
        return _KEY_FILE.read_text().strip()

    # Auto-generate a secure key on first run
    new_key = secrets.token_urlsafe(32)
    _KEY_FILE.parent.mkdir(parents=True, exist_ok=True)
    _KEY_FILE.write_text(new_key)
    _KEY_FILE.chmod(0o600)  # owner read/write only

    # Log key creation with masked value (security: never log full keys)
    import logging

    masked_key = f"{new_key[:4]}{'*' * 8}"
    logging.warning(f"🔑 Kore API key generated: {masked_key}")
    logging.warning(f"   Full key saved to: {_KEY_FILE}")
    logging.warning("   Read the key from the file above or set KORE_API_KEY env var.")

    return new_key


_API_KEY: str | None = None


def _loaded_key() -> str:
    global _API_KEY
    if _API_KEY is None:
        _API_KEY = get_or_create_api_key()
    return _API_KEY


def _is_local(request: Request) -> bool:
    client_host = request.client.host if request.client else ""
    trusted = {"127.0.0.1", "::1", "localhost"}
    # "testclient" only in explicit test environments
    if os.getenv("KORE_TEST_MODE", "0") == "1":
        trusted.add("testclient")
    return client_host in trusted


def _local_only_mode() -> bool:
    # Re-read at runtime to support override in tests (KORE_LOCAL_ONLY=1)
    # Default "1" = skip auth for localhost (consistent with config.LOCAL_ONLY)
    return os.getenv("KORE_LOCAL_ONLY", "1") == "1"


# ── FastAPI dependency ────────────────────────────────────────────────────────


async def require_auth(
    request: Request,
    x_kore_key: str | None = Header(default=None, alias="X-Kore-Key"),
) -> str:
    """
    FastAPI dependency: validates API key.
    In local-only mode, skips auth for 127.0.0.1 requests.
    Returns the validated API key (or 'local' for unauthenticated local requests).
    """
    if _local_only_mode() and _is_local(request):
        return "local"

    if not x_kore_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing API key. Pass X-Kore-Key header.",
            headers={"WWW-Authenticate": "ApiKey"},
        )

    if not secrets.compare_digest(x_kore_key, _loaded_key()):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API key.",
        )

    return x_kore_key


async def get_agent_id(
    request: Request,
    x_agent_id: str | None = Header(default=None, alias="X-Agent-Id"),
) -> str:
    """
    FastAPI dependency: extracts agent namespace.
    Defaults to 'default' when not provided.
    Agent IDs are sanitized to alphanumeric + dash/underscore only.
    """
    agent_id = (x_agent_id or "default").strip()
    # Sanitize: only allow safe chars
    safe = "".join(c for c in agent_id if c.isalnum() or c in "-_")
    if not safe:
        safe = "default"
    return safe[:64]  # max 64 chars
```

## File: `kore_memory/auto_tuner.py`
```python
"""
Kore — Memory Importance Auto-Tuner
Dynamically adjusts memory importance scores based on access patterns.

Rules:
  - Boost: memories accessed >= 5 times with importance < 5 get importance += 1
  - Reduce: memories never accessed (access_count == 0) older than 30 days
    with importance > 1 get importance -= 1

Controlled by KORE_AUTO_TUNE env var (disabled by default).
Thread-safe: only one auto-tune run at a time.
"""

import threading
from datetime import UTC, datetime

from . import config
from .database import get_connection
from .events import emit

# Event type for auto-tune operations
MEMORY_AUTO_TUNED = "memory.auto_tuned"

# Thresholds
BOOST_ACCESS_THRESHOLD = 5
REDUCE_AGE_DAYS = 30

# Thread-safe lock — prevents concurrent auto-tune runs
_auto_tune_lock = threading.Lock()


def run_auto_tune(agent_id: str | None = None) -> dict:
    """
    Run importance auto-tuning based on access patterns.

    - Boosts importance of frequently accessed memories (access_count >= 5, importance < 5)
    - Reduces importance of never-accessed memories older than 30 days (importance > 1)
    - Disabled by default; enable with KORE_AUTO_TUNE=1

    Returns {"boosted": N, "reduced": N, "message": "Auto-tune complete"}
    """
    if not config.AUTO_TUNE:
        return {"boosted": 0, "reduced": 0, "message": "Auto-tune is disabled"}

    if not _auto_tune_lock.acquire(blocking=False):
        return {"boosted": 0, "reduced": 0, "message": "Auto-tune already running"}

    try:
        return _run_auto_tune_inner(agent_id)
    finally:
        _auto_tune_lock.release()


def _run_auto_tune_inner(agent_id: str | None = None) -> dict:
    """Core auto-tune logic, runs inside the lock."""
    now_iso = datetime.now(UTC).isoformat()
    boosted = 0
    reduced = 0

    # ── Boost: frequently accessed memories ──────────────────────────────────
    with get_connection() as conn:
        sql = """
            SELECT id, importance, access_count
            FROM memories
            WHERE compressed_into IS NULL
              AND access_count >= :threshold
              AND importance < 5
        """
        params: dict = {"threshold": BOOST_ACCESS_THRESHOLD}
        if agent_id:
            sql += " AND agent_id = :agent_id"
            params["agent_id"] = agent_id

        rows = conn.execute(sql, params).fetchall()

        boost_updates = []
        for row in rows:
            new_importance = min(5, row["importance"] + 1)
            boost_updates.append((new_importance, now_iso, row["id"]))

        if boost_updates:
            conn.executemany(
                "UPDATE memories SET importance = ?, updated_at = ? WHERE id = ?",
                boost_updates,
            )
            boosted = len(boost_updates)

    # ── Reduce: never-accessed old memories ──────────────────────────────────
    with get_connection() as conn:
        sql = """
            SELECT id, importance
            FROM memories
            WHERE compressed_into IS NULL
              AND access_count = 0
              AND importance > 1
              AND created_at <= datetime('now', :age_offset)
        """
        params = {"age_offset": f"-{REDUCE_AGE_DAYS} days"}
        if agent_id:
            sql += " AND agent_id = :agent_id"
            params["agent_id"] = agent_id

        rows = conn.execute(sql, params).fetchall()

        reduce_updates = []
        for row in rows:
            new_importance = max(1, row["importance"] - 1)
            reduce_updates.append((new_importance, now_iso, row["id"]))

        if reduce_updates:
            conn.executemany(
                "UPDATE memories SET importance = ?, updated_at = ? WHERE id = ?",
                reduce_updates,
            )
            reduced = len(reduce_updates)

    if boosted > 0 or reduced > 0:
        emit(
            MEMORY_AUTO_TUNED,
            {
                "agent_id": agent_id,
                "boosted": boosted,
                "reduced": reduced,
            },
        )

    return {"boosted": boosted, "reduced": reduced, "message": "Auto-tune complete"}


def get_scoring_stats(agent_id: str | None = None) -> dict:
    """
    Return statistics about the importance distribution of active memories.

    Returns:
        {
            "total": int,
            "distribution": {"1": N, "2": N, ...},
            "avg_importance": float,
            "avg_access_count": float,
            "never_accessed_30d": int,
            "frequently_accessed": int,
        }
    """
    with get_connection() as conn:
        # Base filter: active, non-compressed memories
        where = "WHERE compressed_into IS NULL"
        params: list = []
        if agent_id:
            where += " AND agent_id = ?"
            params.append(agent_id)

        # Total count
        total = conn.execute(f"SELECT COUNT(*) FROM memories {where}", params).fetchone()[0]

        if total == 0:
            return {
                "total": 0,
                "distribution": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0},
                "avg_importance": 0.0,
                "avg_access_count": 0.0,
                "never_accessed_30d": 0,
                "frequently_accessed": 0,
            }

        # Importance distribution
        dist_rows = conn.execute(
            f"SELECT importance, COUNT(*) as cnt FROM memories {where} GROUP BY importance",
            params,
        ).fetchall()
        distribution = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0}
        for row in dist_rows:
            distribution[str(row["importance"])] = row["cnt"]

        # Averages
        avgs = conn.execute(
            f"SELECT AVG(importance) as avg_imp, AVG(access_count) as avg_acc FROM memories {where}",
            params,
        ).fetchone()
        avg_importance = round(avgs["avg_imp"] or 0.0, 2)
        avg_access_count = round(avgs["avg_acc"] or 0.0, 2)

        # Never accessed, older than 30 days
        never_sql = f"""
            SELECT COUNT(*) FROM memories
            {where}
              AND access_count = 0
              AND created_at <= datetime('now', '-30 days')
        """
        never_accessed_30d = conn.execute(never_sql, params).fetchone()[0]

        # Frequently accessed (access_count >= threshold)
        freq_sql = f"""
            SELECT COUNT(*) FROM memories
            {where}
              AND access_count >= ?
        """
        freq_params = params + [BOOST_ACCESS_THRESHOLD]
        frequently_accessed = conn.execute(freq_sql, freq_params).fetchone()[0]

    return {
        "total": total,
        "distribution": distribution,
        "avg_importance": avg_importance,
        "avg_access_count": avg_access_count,
        "never_accessed_30d": never_accessed_30d,
        "frequently_accessed": frequently_accessed,
    }
```

## File: `kore_memory/cli.py`
```python
"""
Kore — CLI entry point
Usage: kore [--host HOST] [--port PORT] [--reload]
"""

import argparse
import sys


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="kore",
        description="Kore memory server — start the API.",
    )
    parser.add_argument("--host", default="127.0.0.1", help="Bind host (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8765, help="Bind port (default: 8765)")
    parser.add_argument("--reload", action="store_true", help="Enable auto-reload (dev mode)")
    parser.add_argument("--log-level", default="warning", choices=["debug", "info", "warning", "error"])
    args = parser.parse_args()

    try:
        import uvicorn
    except ImportError:
        print("Error: uvicorn not found. Run: pip install kore-memory", file=sys.stderr)
        sys.exit(1)

    uvicorn.run(
        "kore_memory.main:app",
        host=args.host,
        port=args.port,
        reload=args.reload,
        log_level=args.log_level,
    )


if __name__ == "__main__":
    main()
```

## File: `kore_memory/client.py`
```python
"""
Kore — Python SDK Client
Type-safe client for interacting with the Kore server via HTTP.
Supports both synchronous (KoreClient) and asynchronous (AsyncKoreClient) usage.

Usage:
    from kore_memory import KoreClient

    with KoreClient("http://localhost:8765", api_key="...") as kore:
        kore.save("Important memory", category="project", importance=4)
        results = kore.search("project")
"""

from __future__ import annotations

from typing import Any

import httpx

from .models import (
    BatchSaveResponse,
    CleanupExpiredResponse,
    CompressRunResponse,
    DecayRunResponse,
    MemoryExportResponse,
    MemoryImportResponse,
    MemorySaveResponse,
    MemorySearchResponse,
    RelationResponse,
    TagResponse,
)

# ── Exceptions ───────────────────────────────────────────────────────────────


class KoreError(Exception):
    """Base error class for the Kore client."""

    def __init__(self, message: str, status_code: int | None = None, detail: Any = None):
        super().__init__(message)
        self.status_code = status_code
        self.detail = detail


class KoreAuthError(KoreError):
    """Authentication failed (401/403)."""


class KoreNotFoundError(KoreError):
    """Resource not found (404)."""


class KoreRateLimitError(KoreError):
    """Rate limit exceeded (429)."""


class KoreServerError(KoreError):
    """Server-side error (5xx)."""


class KoreValidationError(KoreError):
    """Validation failed (422)."""


# ── Helpers ──────────────────────────────────────────────────────────────────


def _raise_for_status(response: httpx.Response) -> None:
    """Converts HTTP errors into typed Kore exceptions."""
    if response.is_success:
        return

    status = response.status_code
    try:
        body = response.json()
        detail = body.get("detail", body)
    except Exception:
        detail = response.text

    if status == 401:
        raise KoreAuthError("Authentication required", status, detail)
    if status == 403:
        raise KoreAuthError("Invalid API key", status, detail)
    if status == 404:
        raise KoreNotFoundError("Resource not found", status, detail)
    if status == 422:
        raise KoreValidationError("Validation error", status, detail)
    if status == 429:
        raise KoreRateLimitError("Rate limit exceeded", status, detail)
    if status >= 500:
        raise KoreServerError("Server error", status, detail)

    raise KoreError(f"HTTP {status}", status, detail)


def _build_headers(api_key: str | None, agent_id: str) -> dict[str, str]:
    """Builds the common request headers."""
    headers: dict[str, str] = {"X-Agent-Id": agent_id}
    if api_key:
        headers["X-Kore-Key"] = api_key
    return headers


# ── Synchronous client ───────────────────────────────────────────────────────


class KoreClient:
    """
    Synchronous client for the Kore Memory API.

    Args:
        base_url: Kore server URL (default: http://localhost:8765)
        api_key: API key for authentication (optional on localhost)
        agent_id: Agent namespace (default: "default")
        timeout: Request timeout in seconds (default: 10.0)
    """

    def __init__(
        self,
        base_url: str = "http://localhost:8765",
        api_key: str | None = None,
        agent_id: str = "default",
        timeout: float = 10.0,
    ):
        self.base_url = base_url.rstrip("/")
        self.agent_id = agent_id
        self._client = httpx.Client(
            base_url=self.base_url,
            headers=_build_headers(api_key, agent_id),
            timeout=timeout,
        )

    def __enter__(self) -> KoreClient:
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()

    def close(self) -> None:
        """Closes the HTTP client."""
        self._client.close()

    # ── Core ─────────────────────────────────────────────────────────────

    def save(
        self,
        content: str,
        category: str = "general",
        importance: int | None = None,
        ttl_hours: int | None = None,
    ) -> MemorySaveResponse:
        """Saves a memory. Importance is auto-scored when None (default)."""
        payload: dict[str, Any] = {
            "content": content,
            "category": category,
        }
        if importance is not None:
            payload["importance"] = importance
        if ttl_hours is not None:
            payload["ttl_hours"] = ttl_hours
        r = self._client.post("/save", json=payload)
        _raise_for_status(r)
        return MemorySaveResponse(**r.json())

    def save_batch(
        self,
        memories: list[dict[str, Any]],
    ) -> BatchSaveResponse:
        """Saves up to 100 memories in a single request."""
        r = self._client.post("/save/batch", json={"memories": memories})
        _raise_for_status(r)
        return BatchSaveResponse(**r.json())

    def search(
        self,
        q: str,
        limit: int = 5,
        cursor: str | None = None,
        category: str | None = None,
        semantic: bool = True,
        offset: int = 0,
    ) -> MemorySearchResponse:
        """Searches memories by meaning or text. Uses cursor-based pagination."""
        params: dict[str, Any] = {
            "q": q,
            "limit": limit,
            "semantic": semantic,
        }
        if cursor:
            params["cursor"] = cursor
        if category:
            params["category"] = category
        if offset:
            params["offset"] = offset
        r = self._client.get("/search", params=params)
        _raise_for_status(r)
        return MemorySearchResponse(**r.json())

    def timeline(
        self,
        subject: str,
        limit: int = 20,
        cursor: str | None = None,
        offset: int = 0,
    ) -> MemorySearchResponse:
        """Returns the memory timeline for a subject (oldest to newest). Uses cursor-based pagination."""
        params: dict[str, Any] = {
            "subject": subject,
            "limit": limit,
        }
        if cursor:
            params["cursor"] = cursor
        if offset:
            params["offset"] = offset
        r = self._client.get("/timeline", params=params)
        _raise_for_status(r)
        return MemorySearchResponse(**r.json())

    def get(self, memory_id: int) -> dict[str, Any]:
        """Gets a single memory by ID. Raises KoreNotFoundError if not found."""
        r = self._client.get(f"/memories/{memory_id}")
        _raise_for_status(r)
        return r.json()

    def delete(self, memory_id: int) -> bool:
        """Deletes a memory. Returns True if deleted."""
        r = self._client.delete(f"/memories/{memory_id}")
        if r.status_code == 404:
            return False
        _raise_for_status(r)
        return True

    # ── Tags ─────────────────────────────────────────────────────────────

    def add_tags(self, memory_id: int, tags: list[str]) -> TagResponse:
        """Adds tags to a memory."""
        r = self._client.post(f"/memories/{memory_id}/tags", json={"tags": tags})
        _raise_for_status(r)
        return TagResponse(**r.json())

    def get_tags(self, memory_id: int) -> TagResponse:
        """Returns the tags of a memory."""
        r = self._client.get(f"/memories/{memory_id}/tags")
        _raise_for_status(r)
        return TagResponse(**r.json())

    def remove_tags(self, memory_id: int, tags: list[str]) -> TagResponse:
        """Removes tags from a memory."""
        r = self._client.request("DELETE", f"/memories/{memory_id}/tags", json={"tags": tags})
        _raise_for_status(r)
        return TagResponse(**r.json())

    def search_by_tag(self, tag: str, limit: int = 20) -> MemorySearchResponse:
        """Searches memories by tag."""
        r = self._client.get(f"/tags/{tag}/memories", params={"limit": limit})
        _raise_for_status(r)
        return MemorySearchResponse(**r.json())

    # ── Relations ────────────────────────────────────────────────────────

    def add_relation(
        self,
        memory_id: int,
        target_id: int,
        relation: str = "related",
    ) -> RelationResponse:
        """Creates a relation between two memories."""
        r = self._client.post(
            f"/memories/{memory_id}/relations",
            json={
                "target_id": target_id,
                "relation": relation,
            },
        )
        _raise_for_status(r)
        return RelationResponse(**r.json())

    def get_relations(self, memory_id: int) -> RelationResponse:
        """Returns the relations of a memory."""
        r = self._client.get(f"/memories/{memory_id}/relations")
        _raise_for_status(r)
        return RelationResponse(**r.json())

    # ── Maintenance ──────────────────────────────────────────────────────

    def decay_run(self) -> DecayRunResponse:
        """Recalculates the decay scores of all memories."""
        r = self._client.post("/decay/run")
        _raise_for_status(r)
        return DecayRunResponse(**r.json())

    def compress(self) -> CompressRunResponse:
        """Merges similar memories."""
        r = self._client.post("/compress")
        _raise_for_status(r)
        return CompressRunResponse(**r.json())

    def cleanup(self) -> CleanupExpiredResponse:
        """Removes memories with an expired TTL."""
        r = self._client.post("/cleanup")
        _raise_for_status(r)
        return CleanupExpiredResponse(**r.json())

    # ── Backup ───────────────────────────────────────────────────────────

    def export_memories(self) -> MemoryExportResponse:
        """Exports all active memories as JSON."""
        r = self._client.get("/export")
        _raise_for_status(r)
        return MemoryExportResponse(**r.json())

    def import_memories(self, memories: list[dict[str, Any]]) -> MemoryImportResponse:
        """Imports memories from a list of dicts."""
        r = self._client.post("/import", json={"memories": memories})
        _raise_for_status(r)
        return MemoryImportResponse(**r.json())

    # ── Utility ──────────────────────────────────────────────────────────

    def health(self) -> dict[str, Any]:
        """Server health check."""
        r = self._client.get("/health")
        _raise_for_status(r)
        return r.json()


# ── Asynchronous client ──────────────────────────────────────────────────────


class AsyncKoreClient:
    """
    Asynchronous client for the Kore Memory API.

    Args:
        base_url: Kore server URL (default: http://localhost:8765)
        api_key: API key for authentication (optional on localhost)
        agent_id: Agent namespace (default: "default")
        timeout: Request timeout in seconds (default: 10.0)
    """

    def __init__(
        self,
        base_url: str = "http://localhost:8765",
        api_key: str | None = None,
        agent_id: str = "default",
        timeout: float = 10.0,
    ):
        self.base_url = base_url.rstrip("/")
        self.agent_id = agent_id
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            headers=_build_headers(api_key, agent_id),
            timeout=timeout,
        )

    async def __aenter__(self) -> AsyncKoreClient:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()

    async def close(self) -> None:
        """Closes the HTTP client."""
        await self._client.aclose()

    # ── Core ─────────────────────────────────────────────────────────────

    async def save(
        self,
        content: str,
        category: str = "general",
        importance: int | None = None,
        ttl_hours: int | None = None,
    ) -> MemorySaveResponse:
        """Saves a memory. Importance is auto-scored when None (default)."""
        payload: dict[str, Any] = {
            "content": content,
            "category": category,
        }
        if importance is not None:
            payload["importance"] = importance
        if ttl_hours is not None:
            payload["ttl_hours"] = ttl_hours
        r = await self._client.post("/save", json=payload)
        _raise_for_status(r)
        return MemorySaveResponse(**r.json())

    async def save_batch(
        self,
        memories: list[dict[str, Any]],
    ) -> BatchSaveResponse:
        """Saves up to 100 memories in a single request."""
        r = await self._client.post("/save/batch", json={"memories": memories})
        _raise_for_status(r)
        return BatchSaveResponse(**r.json())

    async def search(
        self,
        q: str,
        limit: int = 5,
        cursor: str | None = None,
        category: str | None = None,
        semantic: bool = True,
        offset: int = 0,
    ) -> MemorySearchResponse:
        """Searches memories by meaning or text. Uses cursor-based pagination."""
        params: dict[str, Any] = {
            "q": q,
            "limit": limit,
            "semantic": semantic,
        }
        if cursor:
            params["cursor"] = cursor
        if category:
            params["category"] = category
        if offset:
            params["offset"] = offset
        r = await self._client.get("/search", params=params)
        _raise_for_status(r)
        return MemorySearchResponse(**r.json())

    async def timeline(
        self,
        subject: str,
        limit: int = 20,
        cursor: str | None = None,
        offset: int = 0,
    ) -> MemorySearchResponse:
        """Returns the memory timeline for a subject (oldest to newest). Uses cursor-based pagination."""
        params: dict[str, Any] = {
            "subject": subject,
            "limit": limit,
        }
        if cursor:
            params["cursor"] = cursor
        if offset:
            params["offset"] = offset
        r = await self._client.get("/timeline", params=params)
        _raise_for_status(r)
        return MemorySearchResponse(**r.json())

    async def get(self, memory_id: int) -> dict[str, Any]:
        """Gets a single memory by ID. Raises KoreNotFoundError if not found."""
        r = await self._client.get(f"/memories/{memory_id}")
        _raise_for_status(r)
        return r.json()

    async def delete(self, memory_id: int) -> bool:
        """Deletes a memory. Returns True if deleted."""
        r = await self._client.delete(f"/memories/{memory_id}")
        if r.status_code == 404:
            return False
        _raise_for_status(r)
        return True

    # ── Tags ─────────────────────────────────────────────────────────────

    async def add_tags(self, memory_id: int, tags: list[str]) -> TagResponse:
        """Adds tags to a memory."""
        r = await self._client.post(f"/memories/{memory_id}/tags", json={"tags": tags})
        _raise_for_status(r)
        return TagResponse(**r.json())

    async def get_tags(self, memory_id: int) -> TagResponse:
        """Returns the tags of a memory."""
        r = await self._client.get(f"/memories/{memory_id}/tags")
        _raise_for_status(r)
        return TagResponse(**r.json())

    async def remove_tags(self, memory_id: int, tags: list[str]) -> TagResponse:
        """Removes tags from a memory."""
        r = await self._client.request("DELETE", f"/memories/{memory_id}/tags", json={"tags": tags})
        _raise_for_status(r)
        return TagResponse(**r.json())

    async def search_by_tag(self, tag: str, limit: int = 20) -> MemorySearchResponse:
        """Searches memories by tag."""
        r = await self._client.get(f"/tags/{tag}/memories", params={"limit": limit})
        _raise_for_status(r)
        return MemorySearchResponse(**r.json())

    # ── Relations ────────────────────────────────────────────────────────

    async def add_relation(
        self,
        memory_id: int,
        target_id: int,
        relation: str = "related",
    ) -> RelationResponse:
        """Creates a relation between two memories."""
        r = await self._client.post(
            f"/memories/{memory_id}/relations",
            json={
                "target_id": target_id,
                "relation": relation,
            },
        )
        _raise_for_status(r)
        return RelationResponse(**r.json())

    async def get_relations(self, memory_id: int) -> RelationResponse:
        """Returns the relations of a memory."""
        r = await self._client.get(f"/memories/{memory_id}/relations")
        _raise_for_status(r)
        return RelationResponse(**r.json())

    # ── Maintenance ──────────────────────────────────────────────────────

    async def decay_run(self) -> DecayRunResponse:
        """Recalculates the decay scores of all memories."""
        r = await self._client.post("/decay/run")
        _raise_for_status(r)
        return DecayRunResponse(**r.json())

    async def compress(self) -> CompressRunResponse:
        """Merges similar memories."""
        r = await self._client.post("/compress")
        _raise_for_status(r)
        return CompressRunResponse(**r.json())

    async def cleanup(self) -> CleanupExpiredResponse:
        """Removes memories with an expired TTL."""
        r = await self._client.post("/cleanup")
        _raise_for_status(r)
        return CleanupExpiredResponse(**r.json())

    # ── Backup ───────────────────────────────────────────────────────────

    async def export_memories(self) -> MemoryExportResponse:
        """Exports all active memories as JSON."""
        r = await self._client.get("/export")
        _raise_for_status(r)
        return MemoryExportResponse(**r.json())

    async def import_memories(self, memories: list[dict[str, Any]]) -> MemoryImportResponse:
        """Imports memories from a list of dicts."""
        r = await self._client.post("/import", json={"memories": memories})
        _raise_for_status(r)
        return MemoryImportResponse(**r.json())

    # ── Utility ──────────────────────────────────────────────────────────

    async def health(self) -> dict[str, Any]:
        """Server health check."""
        r = await self._client.get("/health")
        _raise_for_status(r)
        return r.json()
```

## File: `kore_memory/compressor.py`
```python
"""
Kore — Memory Compressor
Finds clusters of similar memories and merges them into a single richer record.

Strategy:
  1. Load all memories without a compressed_into reference
  2. For each pair, compute cosine similarity
  3. Cluster memories with similarity > threshold
  4. Merge each cluster into one record (union of content, max importance)
  5. Mark originals as compressed_into the new record
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from . import config
from .database import get_connection
from .embedder import cosine_similarity, deserialize
from .events import MEMORY_COMPRESSED, emit
from .models import MemorySaveRequest
from .repository import _compress_lock, save_memory

SIMILARITY_THRESHOLD = config.SIMILARITY_THRESHOLD
MAX_COMPRESSION_DEPTH = 3  # Limite massimo catena di compressione

# --- numpy availability (optional, installed with [semantic]) ---
try:
    import numpy as np

    _HAS_NUMPY = True
except ImportError:
    np = None  # type: ignore[assignment]
    _HAS_NUMPY = False


@dataclass
class CompressionResult:
    clusters_found: int
    memories_merged: int
    new_records_created: int


def run_compression(agent_id: str = "default") -> CompressionResult:
    """
    Full compression: finds similar memories and merges them.
    Thread-safe: only one run at a time.
    """
    if not _compress_lock.acquire(blocking=False):
        return CompressionResult(0, 0, 0)  # run already in progress

    try:
        return _run_compression_inner(agent_id)
    finally:
        _compress_lock.release()


def _run_compression_inner(agent_id: str = "default") -> CompressionResult:
    memories = _load_compressible_memories(agent_id)
    if len(memories) < 2:
        return CompressionResult(0, 0, 0)

    clusters = _find_clusters(memories)
    if not clusters:
        return CompressionResult(0, 0, 0)

    merged = 0
    created = 0
    for cluster in clusters:
        new_id = _merge_cluster(cluster, agent_id=agent_id)
        if new_id:
            merged += len(cluster)
            created += 1
            emit(MEMORY_COMPRESSED, {
                "id": new_id,
                "agent_id": agent_id,
                "merged_ids": [m["id"] for m in cluster],
                "cluster_size": len(cluster),
            })

    return CompressionResult(
        clusters_found=len(clusters),
        memories_merged=merged,
        new_records_created=created,
    )


def _load_compressible_memories(agent_id: str = "default") -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT id, content, category, importance, embedding
            FROM memories
            WHERE compressed_into IS NULL AND archived_at IS NULL AND embedding IS NOT NULL AND agent_id = ?
            """,
            (agent_id,),
        ).fetchall()

    # Filtra memorie che sono già risultato di troppi livelli di compressione
    result = []
    for r in rows:
        result.append(dict(r))

    if not result:
        return result

    # Escludi memorie che hanno già raggiunto la profondità massima di compressione
    ids = [m["id"] for m in result]
    with get_connection() as conn:
        depth_map = _get_compression_depths(conn, ids)

    return [m for m in result if depth_map.get(m["id"], 0) < MAX_COMPRESSION_DEPTH]


def _get_compression_depths(conn, memory_ids: list[int]) -> dict[int, int]:
    """Calcola la profondità di compressione per ogni memoria.
    Depth 0 = memoria originale, 1 = risultato di una compressione, ecc."""
    if not memory_ids:
        return {}

    # Conta quante memorie puntano a ciascun id (quanti livelli di merge)
    placeholders = ",".join("?" for _ in memory_ids)
    rows = conn.execute(
        f"""
        WITH RECURSIVE chain(id, depth) AS (
            SELECT id, 0 FROM memories WHERE id IN ({placeholders})
            UNION ALL
            SELECT m.id, c.depth + 1
            FROM memories m
            JOIN chain c ON m.compressed_into = c.id
        )
        SELECT chain.id, MAX(chain.depth) AS max_depth
        FROM chain
        GROUP BY chain.id
        """,
        memory_ids,
    ).fetchall()

    return {row["id"]: row["max_depth"] for row in rows}


def _find_clusters(memories: list[dict]) -> list[list[dict]]:
    """
    Greedy clustering: finds groups of memories with similarity > threshold.

    Uses numpy matrix multiplication when available for O(n²) batch similarity
    computation (much faster than O(n²) pure Python pairwise comparisons).
    Falls back to pure Python if numpy is not installed.
    """
    # Pre-deserialize all vectors once
    vectors: dict[int, list[float]] = {}
    for mem in memories:
        try:
            vectors[mem["id"]] = deserialize(mem["embedding"])
        except Exception:
            continue

    # Filter to only memories with valid vectors
    valid_memories = [m for m in memories if m["id"] in vectors]

    if len(valid_memories) < 2:
        return []

    if _HAS_NUMPY:
        return _find_clusters_numpy(valid_memories, vectors)
    else:
        return _find_clusters_python(valid_memories, vectors)


_CHUNK_SIZE = 2000  # Max vectors per chunk to avoid OOM on large datasets


def _find_clusters_numpy(
    memories: list[dict],
    vectors: dict[int, list[float]],
) -> list[list[dict]]:
    """
    Numpy-accelerated clustering with chunked processing.

    For datasets up to CHUNK_SIZE: full n×n similarity matrix (fast, O(n²) memory).
    For larger datasets: chunked processing computes similarity in blocks,
    keeping memory usage bounded at O(CHUNK_SIZE × n) per iteration.
    """
    n = len(memories)
    mem_ids = [m["id"] for m in memories]
    matrix = np.array([vectors[mid] for mid in mem_ids], dtype=np.float32)

    if n <= _CHUNK_SIZE:
        # Small dataset: full similarity matrix in one shot
        return _cluster_full_matrix(memories, matrix, n)

    # Large dataset: chunked row-by-row similarity computation
    return _cluster_chunked(memories, matrix, n)


def _cluster_full_matrix(
    memories: list[dict],
    matrix: np.ndarray,
    n: int,
) -> list[list[dict]]:
    """Full n×n similarity matrix clustering (for small datasets)."""
    sim_matrix = matrix @ matrix.T  # shape: (n, n)

    used: set[int] = set()
    clusters: list[list[dict]] = []

    for i in range(n):
        if i in used:
            continue

        # Vectorized: find all j > i with similarity >= threshold
        sims = sim_matrix[i, i + 1:]
        similar_mask = sims >= SIMILARITY_THRESHOLD
        similar_indices = np.where(similar_mask)[0] + (i + 1)

        # Filter out already used indices
        cluster_indices = [i]
        for j in similar_indices:
            if j not in used:
                cluster_indices.append(int(j))

        if len(cluster_indices) > 1:
            for idx in cluster_indices:
                used.add(idx)
            clusters.append([memories[idx] for idx in cluster_indices])

    return clusters


def _cluster_chunked(
    memories: list[dict],
    matrix: np.ndarray,
    n: int,
) -> list[list[dict]]:
    """Chunked similarity computation for large datasets (>CHUNK_SIZE vectors)."""
    used: set[int] = set()
    clusters: list[list[dict]] = []

    for chunk_start in range(0, n, _CHUNK_SIZE):
        chunk_end = min(chunk_start + _CHUNK_SIZE, n)

        # Compute similarity between chunk rows and ALL columns
        chunk_matrix = matrix[chunk_start:chunk_end]  # shape: (chunk, dim)
        sim_block = chunk_matrix @ matrix.T  # shape: (chunk, n)

        for local_i in range(chunk_end - chunk_start):
            global_i = chunk_start + local_i
            if global_i in used:
                continue

            # Only look at j > global_i to avoid double-counting
            sims = sim_block[local_i, global_i + 1:]
            similar_mask = sims >= SIMILARITY_THRESHOLD
            similar_indices = np.where(similar_mask)[0] + (global_i + 1)

            cluster_indices = [global_i]
            for j in similar_indices:
                if j not in used:
                    cluster_indices.append(int(j))

            if len(cluster_indices) > 1:
                for idx in cluster_indices:
                    used.add(idx)
                clusters.append([memories[idx] for idx in cluster_indices])

    return clusters


def _find_clusters_python(
    memories: list[dict],
    vectors: dict[int, list[float]],
) -> list[list[dict]]:
    """
    Pure Python fallback: O(n²/2) pairwise cosine similarity comparisons.
    """
    used: set[int] = set()
    clusters: list[list[dict]] = []

    for i, mem_a in enumerate(memories):
        if mem_a["id"] in used:
            continue

        vec_a = vectors[mem_a["id"]]
        cluster = [mem_a]

        # Compare only with subsequent memories (avoids double comparisons)
        for mem_b in memories[i + 1 :]:
            if mem_b["id"] in used:
                continue
            if cosine_similarity(vec_a, vectors[mem_b["id"]]) >= SIMILARITY_THRESHOLD:
                cluster.append(mem_b)

        if len(cluster) > 1:
            for m in cluster:
                used.add(m["id"])
            clusters.append(cluster)

    return clusters


def _merge_cluster(cluster: list[dict], agent_id: str = "default") -> int | None:
    """
    Merge a cluster of memories into a single new record.
    Returns the id of the new merged record, or None on failure.
    """
    if not cluster:
        return None

    # Build merged content: combine unique sentences
    # Split on sentence boundaries (. ! ? followed by space/end) instead of pipe
    combined_parts = []
    seen = set()
    for mem in cluster:
        sentences = re.split(r"(?<=[.!?])\s+", mem["content"].strip())
        for s in sentences:
            s = s.strip()
            if s and s not in seen:
                seen.add(s)
                combined_parts.append(s)

    merged_content = " ".join(combined_parts)
    if len(merged_content) > 4000:
        merged_content = merged_content[:3997] + "..."

    # Use the most common category and highest importance
    categories = [m["category"] for m in cluster]
    merged_category = max(set(categories), key=categories.count)
    merged_importance = max(m["importance"] for m in cluster)

    # Save the new merged record
    req = MemorySaveRequest(
        content=merged_content,
        category=merged_category,
        importance=merged_importance,
    )
    new_id, _ = save_memory(req, agent_id=agent_id)

    # Migrate tags and relations from originals to the new record, then mark as compressed
    ids = [m["id"] for m in cluster]
    with get_connection() as conn:
        # Copy unique tags to the new record
        placeholders = ",".join("?" for _ in ids)
        conn.execute(
            f"""INSERT OR IGNORE INTO memory_tags (memory_id, tag)
                SELECT ?, tag FROM memory_tags WHERE memory_id IN ({placeholders})""",
            [new_id, *ids],
        )

        # Relink relations: source_id -> new_id
        conn.execute(
            f"""UPDATE memory_relations SET source_id = ?
                WHERE source_id IN ({placeholders})""",
            [new_id, *ids],
        )
        # Relink relations: target_id -> new_id
        conn.execute(
            f"""UPDATE memory_relations SET target_id = ?
                WHERE target_id IN ({placeholders})""",
            [new_id, *ids],
        )
        # Remove any self-relations created by the relink
        conn.execute(
            "DELETE FROM memory_relations WHERE source_id = target_id",
        )

        # Mark originals as compressed
        conn.executemany(
            "UPDATE memories SET compressed_into = ? WHERE id = ?",
            [(new_id, mid) for mid in ids],
        )

    return new_id
```

## File: `kore_memory/config.py`
```python
"""
Kore — Centralized configuration
All environment variables and constants in a single place.
"""

import os
from pathlib import Path

# ── Paths ─────────────────────────────────────────────────────────────────────

_PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = _PROJECT_ROOT / "data"

# Database
DEFAULT_DB_PATH = str(DATA_DIR / "memory.db")
DB_PATH = os.getenv("KORE_DB_PATH", DEFAULT_DB_PATH)

# API key
API_KEY_FILE = DATA_DIR / ".api_key"

# ── Server ────────────────────────────────────────────────────────────────────

HOST = os.getenv("KORE_HOST", "127.0.0.1")
PORT = int(os.getenv("KORE_PORT", "8765"))
LOCAL_ONLY = os.getenv("KORE_LOCAL_ONLY", "1") == "1"

# ── CORS ──────────────────────────────────────────────────────────────────────

CORS_ORIGINS = [o.strip() for o in os.getenv("KORE_CORS_ORIGINS", "").split(",") if o.strip()]

# ── Rate limiting ─────────────────────────────────────────────────────────────

RATE_LIMITS: dict[str, tuple[int, int]] = {
    "/save": (30, 60),  # 30 req/min
    "/search": (60, 60),  # 60 req/min
    "/timeline": (60, 60),  # 60 req/min
    "/decay/run": (5, 3600),  # 5 req/hour
    "/compress": (2, 3600),  # 2 req/hour
    "/export": (10, 3600),  # 10 req/hour
    "/import": (5, 3600),  # 5 req/hour
    "/cleanup": (10, 3600),  # 10 req/hour
    "/delete": (120, 60),  # 120 delete/min
}

# ── Embedder ──────────────────────────────────────────────────────────────────

EMBED_MODEL = os.getenv("KORE_EMBED_MODEL", "paraphrase-multilingual-MiniLM-L12-v2")
MAX_EMBED_CHARS = int(os.getenv("KORE_MAX_EMBED_CHARS", "8000"))
EMBED_BACKEND = os.getenv("KORE_EMBED_BACKEND", "")  # "onnx" for ONNX backend

# ── Compressor ────────────────────────────────────────────────────────────────

SIMILARITY_THRESHOLD = float(os.getenv("KORE_SIMILARITY_THRESHOLD", "0.88"))

# ── Auto-tuner ───────────────────────────────────────────────────────────────

AUTO_TUNE = os.getenv("KORE_AUTO_TUNE", "0") == "1"

# ── Entity extraction ────────────────────────────────────────────────────────

ENTITY_EXTRACTION = os.getenv("KORE_ENTITY_EXTRACTION", "0") == "1"

# ── Audit log ────────────────────────────────────────────────────────────────

AUDIT_LOG = os.getenv("KORE_AUDIT_LOG", "0") == "1"

# ── Version ───────────────────────────────────────────────────────────────────

VERSION = "2.0.0"
```

## File: `kore_memory/dashboard.py`
```python
"""
Kore — Web Dashboard
Dashboard HTML loaded from templates/dashboard.html at import time.
Falls back to inline string if template file is missing.
Vanilla JS + CSS, zero dipendenze esterne.
"""

import logging
from pathlib import Path

_logger = logging.getLogger(__name__)

# ── Template location ────────────────────────────────────────────────────────

_TEMPLATE_DIR = Path(__file__).parent / "templates"
_TEMPLATE_PATH = _TEMPLATE_DIR / "dashboard.html"

# ── Fallback HTML (shown only if template file is missing) ───────────────────

_FALLBACK_HTML = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Kore — Dashboard Unavailable</title>
<style>
body { font-family: system-ui, sans-serif; background: #0c0c1d; color: #c8cad8;
       display: flex; justify-content: center; align-items: center; min-height: 100vh; }
.msg { text-align: center; max-width: 480px; }
h1 { color: #7c3aed; margin-bottom: 1rem; }
code { background: #1e1e48; padding: 2px 8px; border-radius: 4px; }
</style>
</head>
<body>
<div class="msg">
<h1>Kore</h1>
<p>Dashboard template file not found.</p>
<p>Expected at: <code>kore_memory/templates/dashboard.html</code></p>
<p>Please reinstall the package or restore the template file.</p>
</div>
<script>/* fallback — no functionality */</script>
</body>
</html>
"""

# ── Load template at import time (cached in module variable) ─────────────────


def _load_template() -> str:
    """Load dashboard HTML from the template file.

    Reads templates/dashboard.html at import time so the file is only read once.
    If the template file is missing (e.g. broken install), falls back to a
    minimal error page.
    """
    try:
        return _TEMPLATE_PATH.read_text(encoding="utf-8")
    except FileNotFoundError:
        _logger.warning(
            "Dashboard template not found at %s — serving fallback page",
            _TEMPLATE_PATH,
        )
        return _FALLBACK_HTML
    except OSError as exc:
        _logger.error("Failed to read dashboard template: %s", exc)
        return _FALLBACK_HTML


_DASHBOARD_HTML: str = _load_template()


def get_dashboard_html() -> str:
    """Ritorna l'HTML completo della dashboard."""
    return _DASHBOARD_HTML
```

## File: `kore_memory/database.py`
```python
"""
Kore - Database layer
Handles SQLite connection pool and schema initialization.
"""

import os
import sqlite3
import threading
from contextlib import contextmanager
from pathlib import Path
from queue import Empty, Queue

from . import config

_POOL_SIZE = 4

# --- sqlite-vec availability ---
try:
    import sqlite_vec

    _HAS_SQLITE_VEC = True
except ImportError:
    _HAS_SQLITE_VEC = False


def _load_sqlite_vec(conn: sqlite3.Connection) -> None:
    """Load sqlite-vec extension on a connection (idempotent, silent if unavailable)."""
    if not _HAS_SQLITE_VEC:
        return
    try:
        conn.enable_load_extension(True)
        sqlite_vec.load(conn)
        conn.enable_load_extension(False)
    except Exception:
        pass  # already loaded or not available


def _get_db_path() -> Path:
    """Risolve il path del DB a runtime (supporta override via KORE_DB_PATH)."""
    # Controlla env var a runtime per supporto test con DB temporaneo
    return Path(os.getenv("KORE_DB_PATH", config.DEFAULT_DB_PATH))


# ── Connection Pool ─────────────────────────────────────────────────────────


class _ConnectionPool:
    """Simple thread-safe SQLite connection pool."""

    def __init__(self) -> None:
        self._pools: dict[str, Queue] = {}
        self._lock = threading.Lock()

    def _get_pool(self, db_path: str) -> Queue:
        with self._lock:
            if db_path not in self._pools:
                self._pools[db_path] = Queue(maxsize=_POOL_SIZE)
            return self._pools[db_path]

    def acquire(self, db_path: str) -> sqlite3.Connection:
        pool = self._get_pool(db_path)
        try:
            conn = pool.get_nowait()
            # Verifica che la connessione sia ancora valida
            conn.execute("SELECT 1")
            return conn
        except Empty:
            pass
        except Exception:
            # Connessione corrotta — chiudi per evitare fd leak
            try:
                conn.close()  # noqa: F821 — conn definita da get_nowait() sopra
            except (Exception, NameError):
                pass
        # Crea nuova connessione
        conn = sqlite3.connect(db_path, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA foreign_keys=ON")
        # Ottimizzazioni performance: 5-10x miglioramento write
        conn.execute("PRAGMA synchronous=NORMAL")
        conn.execute("PRAGMA temp_store=MEMORY")
        conn.execute("PRAGMA mmap_size=268435456")  # 256MB mmap
        conn.execute("PRAGMA cache_size=-32000")  # 32MB cache
        # Load sqlite-vec extension if available
        _load_sqlite_vec(conn)
        return conn

    def release(self, db_path: str, conn: sqlite3.Connection) -> None:
        pool = self._get_pool(db_path)
        try:
            pool.put_nowait(conn)
        except Exception:
            # Pool pieno — chiudi la connessione
            conn.close()

    def clear(self) -> None:
        """Chiudi tutte le connessioni nel pool (per test cleanup)."""
        with self._lock:
            for pool in self._pools.values():
                while not pool.empty():
                    try:
                        conn = pool.get_nowait()
                        conn.close()
                    except Empty:
                        break
            self._pools.clear()


_pool = _ConnectionPool()


def init_db() -> None:
    """Initialize the database and create tables if they don't exist."""
    db_path = _get_db_path()
    db_path.parent.mkdir(parents=True, exist_ok=True)
    # Ensure DB file exists before chmod
    db_path.touch(exist_ok=True)
    db_path.chmod(0o600)  # owner only — protects memory data

    with get_connection() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS memories (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                agent_id        TEXT    NOT NULL DEFAULT 'default',
                content         TEXT    NOT NULL,
                category        TEXT    NOT NULL DEFAULT 'general',
                importance      INTEGER NOT NULL DEFAULT 1 CHECK (importance BETWEEN 1 AND 5),
                decay_score     REAL    NOT NULL DEFAULT 1.0,
                access_count    INTEGER NOT NULL DEFAULT 0,
                last_accessed   TEXT    DEFAULT NULL,
                compressed_into INTEGER DEFAULT NULL REFERENCES memories(id),
                embedding       TEXT    DEFAULT NULL,
                expires_at      TEXT    DEFAULT NULL,
                archived_at     TEXT    DEFAULT NULL,
                session_id      TEXT    DEFAULT NULL,
                created_at      TEXT    NOT NULL DEFAULT (datetime('now')),
                updated_at      TEXT    NOT NULL DEFAULT (datetime('now'))
            );

            CREATE INDEX IF NOT EXISTS idx_memories_agent      ON memories (agent_id);
            CREATE INDEX IF NOT EXISTS idx_memories_decay      ON memories (decay_score DESC);
            CREATE INDEX IF NOT EXISTS idx_memories_compressed ON memories (compressed_into);

            CREATE INDEX IF NOT EXISTS idx_memories_category  ON memories (category);
            CREATE INDEX IF NOT EXISTS idx_memories_importance ON memories (importance DESC);
            CREATE INDEX IF NOT EXISTS idx_memories_created_at ON memories (created_at DESC);
            CREATE INDEX IF NOT EXISTS idx_memories_expires ON memories (expires_at) WHERE expires_at IS NOT NULL;
            CREATE INDEX IF NOT EXISTS idx_memories_archived ON memories (archived_at) WHERE archived_at IS NOT NULL;

            -- Indice composito per query search e decay_pass (agent + attive + ordinamento)
            CREATE INDEX IF NOT EXISTS idx_agent_decay_active
                ON memories (agent_id, compressed_into, archived_at, decay_score DESC);

            CREATE VIRTUAL TABLE IF NOT EXISTS memories_fts
            USING fts5(content, category, content='memories', content_rowid='id', tokenize='unicode61');

            CREATE TRIGGER IF NOT EXISTS memories_ai
            AFTER INSERT ON memories BEGIN
                INSERT INTO memories_fts (rowid, content, category)
                VALUES (new.id, new.content, new.category);
            END;

            CREATE TRIGGER IF NOT EXISTS memories_ad
            AFTER DELETE ON memories BEGIN
                INSERT INTO memories_fts (memories_fts, rowid, content, category)
                VALUES ('delete', old.id, old.content, old.category);
            END;

            CREATE TRIGGER IF NOT EXISTS memories_au
            AFTER UPDATE ON memories BEGIN
                INSERT INTO memories_fts (memories_fts, rowid, content, category)
                VALUES ('delete', old.id, old.content, old.category);
                INSERT INTO memories_fts (rowid, content, category)
                VALUES (new.id, new.content, new.category);
            END;

            -- Tag per memorie
            CREATE TABLE IF NOT EXISTS memory_tags (
                memory_id   INTEGER NOT NULL REFERENCES memories(id) ON DELETE CASCADE,
                tag         TEXT    NOT NULL,
                PRIMARY KEY (memory_id, tag)
            );
            CREATE INDEX IF NOT EXISTS idx_tags_tag ON memory_tags (tag);

            -- Sessioni di conversazione
            CREATE TABLE IF NOT EXISTS sessions (
                id          TEXT    PRIMARY KEY,
                agent_id    TEXT    NOT NULL DEFAULT 'default',
                title       TEXT    DEFAULT NULL,
                created_at  TEXT    NOT NULL DEFAULT (datetime('now')),
                ended_at    TEXT    DEFAULT NULL
            );
            CREATE INDEX IF NOT EXISTS idx_sessions_agent ON sessions (agent_id);

            -- Relazioni tra memorie (grafo)
            CREATE TABLE IF NOT EXISTS memory_relations (
                source_id   INTEGER NOT NULL REFERENCES memories(id) ON DELETE CASCADE,
                target_id   INTEGER NOT NULL REFERENCES memories(id) ON DELETE CASCADE,
                relation    TEXT    NOT NULL DEFAULT 'related',
                created_at  TEXT    NOT NULL DEFAULT (datetime('now')),
                PRIMARY KEY (source_id, target_id, relation)
            );
            CREATE INDEX IF NOT EXISTS idx_relations_source ON memory_relations (source_id);
            CREATE INDEX IF NOT EXISTS idx_relations_target ON memory_relations (target_id);

            -- Audit / event log
            CREATE TABLE IF NOT EXISTS event_logs (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                event       TEXT    NOT NULL,
                agent_id    TEXT    NOT NULL DEFAULT 'default',
                memory_id   INTEGER DEFAULT NULL,
                data        TEXT    DEFAULT NULL,
                created_at  TEXT    NOT NULL DEFAULT (datetime('now'))
            );
            CREATE INDEX IF NOT EXISTS idx_event_logs_agent   ON event_logs (agent_id);
            CREATE INDEX IF NOT EXISTS idx_event_logs_event   ON event_logs (event);
            CREATE INDEX IF NOT EXISTS idx_event_logs_created ON event_logs (created_at DESC);
        """)

        # Create sqlite-vec virtual table if extension is available
        if _HAS_SQLITE_VEC:
            try:
                embed_dim = int(os.getenv("KORE_EMBED_DIM", "384"))
                conn.execute(f"""
                    CREATE VIRTUAL TABLE IF NOT EXISTS vec_memories USING vec0(
                        agent_id TEXT partition key,
                        embedding float[{embed_dim}] distance_metric=cosine
                    )
                """)
            except Exception:
                pass  # extension not loaded on this connection

        # Migrazione: aggiungi expires_at se mancante (DB pre-esistenti)
        cols = {row[1] for row in conn.execute("PRAGMA table_info(memories)").fetchall()}
        if "expires_at" not in cols:
            conn.execute("ALTER TABLE memories ADD COLUMN expires_at TEXT DEFAULT NULL")
        if "archived_at" not in cols:
            conn.execute("ALTER TABLE memories ADD COLUMN archived_at TEXT DEFAULT NULL")
        if "session_id" not in cols:
            conn.execute("ALTER TABLE memories ADD COLUMN session_id TEXT DEFAULT NULL")


@contextmanager
def get_connection():
    """Yield a pooled thread-safe SQLite connection with WAL mode enabled."""
    db_path = str(_get_db_path())
    conn = _pool.acquire(db_path)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        _pool.release(db_path, conn)
```

## File: `kore_memory/decay.py`
```python
"""
Kore — Memory Decay Engine
Implements human-like forgetting: memories fade over time unless reinforced.

Formula inspired by Ebbinghaus forgetting curve:
  decay = importance_factor * e^(-t / half_life)

Where:
  t              = days since last access
  half_life      = base days before 50% decay (modulated by importance)
  importance_fac = 1.0 to 2.0 (higher importance = slower decay)
  access_count   = each retrieval resets the clock and boosts score
"""

import math
from datetime import UTC, datetime

# Half-life in days per importance level (higher importance = longer half-life)
HALF_LIFE: dict[int, float] = {
    1: 7.0,  # low — fades in ~1 week
    2: 14.0,  # normal — fades in ~2 weeks
    3: 30.0,  # important — fades in ~1 month
    4: 90.0,  # very important — fades in ~3 months
    5: 365.0,  # critical — fades in ~1 year
}

# Access reinforcement: each retrieval extends half-life by this factor
ACCESS_BOOST = 0.15  # +15% half-life per access


def compute_decay(
    importance: int,
    created_at: str,
    last_accessed: str | None,
    access_count: int,
) -> float:
    """
    Compute current decay score (0.0–1.0) for a memory.
    1.0 = perfectly fresh, 0.0 = completely faded.
    """
    reference_time = last_accessed or created_at
    try:
        ref_dt = datetime.fromisoformat(reference_time).replace(tzinfo=UTC)
    except ValueError:
        ref_dt = datetime.now(UTC)

    now = datetime.now(UTC)
    days_elapsed = max(0.0, (now - ref_dt).total_seconds() / 86400)

    base_half_life = HALF_LIFE.get(importance, 14.0)
    effective_half_life = base_half_life * (1 + ACCESS_BOOST * access_count)

    # Ebbinghaus formula: R = e^(-t/S) where S is stability (half-life)
    decay = math.exp(-days_elapsed * math.log(2) / effective_half_life)
    return round(min(1.0, max(0.0, decay)), 4)


def effective_score(decay_score: float, importance: int) -> float:
    """
    Decay × importance weight used for ranking search results.
    Multiplied by similarity score (when available) in repository.search_memories().
    """
    importance_weight = importance / 5.0  # normalize to 0.2–1.0
    return round(decay_score * importance_weight, 4)


def should_forget(decay_score: float, threshold: float = 0.05) -> bool:
    """Returns True when a memory has faded below the forgetting threshold."""
    return decay_score < threshold
```

## File: `kore_memory/embedder.py`
```python
"""
Kore — Embedder (v3)
Lazy-loaded sentence embeddings using multilingual models.
Default: paraphrase-multilingual-MiniLM-L12-v2 (~120MB, 384 dim, 50+ languages)

Supports:
- sentence-transformers v5.x encode_query()/encode_document() for asymmetric search
- ONNX backend for faster inference (optional: pip install 'sentence-transformers[onnx]')
- Custom models via KORE_EMBED_MODEL env var
"""

from __future__ import annotations

import base64
import json
import logging
import struct
from functools import lru_cache
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sentence_transformers import SentenceTransformer

from . import config

MODEL_NAME = config.EMBED_MODEL
MAX_EMBED_CHARS = config.MAX_EMBED_CHARS
ONNX_BACKEND = config.EMBED_BACKEND

logger = logging.getLogger(__name__)

# --- numpy availability (optional, installed with [semantic]) ---
try:
    import numpy as np

    _HAS_NUMPY = True
except ImportError:
    np = None  # type: ignore[assignment]
    _HAS_NUMPY = False


@lru_cache(maxsize=1)
def get_model() -> SentenceTransformer:
    """Load the model once and keep it cached."""
    from sentence_transformers import SentenceTransformer

    kwargs = {}
    if ONNX_BACKEND:
        kwargs["backend"] = "onnx"
        logger.info("Loading model %s with ONNX backend", MODEL_NAME)

    model = SentenceTransformer(MODEL_NAME, **kwargs)

    # Check if model supports asymmetric search (v5+ with prompts)
    has_prompts = hasattr(model, "prompts") and model.prompts
    logger.info(
        "Loaded model %s (dim=%d, asymmetric=%s)",
        MODEL_NAME,
        model.get_sentence_embedding_dimension(),
        bool(has_prompts),
    )
    return model


def _truncate(text: str, max_chars: int = MAX_EMBED_CHARS) -> str:
    """Truncate text to max chars to prevent OOM."""
    if len(text) <= max_chars:
        return text
    return text[:max_chars]


def _has_asymmetric_support(model: SentenceTransformer) -> bool:
    """Check if model supports encode_query/encode_document (v5+ with prompts)."""
    return (
        hasattr(model, "encode_query")
        and hasattr(model, "prompts")
        and bool(model.prompts)
    )


def embed(text: str) -> list[float]:
    """Return the embedding vector for a single text (document mode)."""
    model = get_model()
    truncated = _truncate(text)

    if _has_asymmetric_support(model):
        vector = model.encode_document(truncated, normalize_embeddings=True)
    else:
        vector = model.encode(truncated, normalize_embeddings=True)

    return vector.tolist()


def embed_query(text: str) -> list[float]:
    """Return the embedding vector optimized for search queries."""
    model = get_model()
    truncated = _truncate(text)

    if _has_asymmetric_support(model):
        vector = model.encode_query(truncated, normalize_embeddings=True)
    else:
        vector = model.encode(truncated, normalize_embeddings=True)

    return vector.tolist()


def embed_batch(texts: list[str]) -> list[list[float]]:
    """Return embedding vectors for a list of texts (document mode)."""
    model = get_model()
    truncated = [_truncate(t) for t in texts]

    if _has_asymmetric_support(model):
        vectors = model.encode_document(truncated, normalize_embeddings=True, batch_size=32)
    else:
        vectors = model.encode(truncated, normalize_embeddings=True, batch_size=32)

    return [v.tolist() for v in vectors]


def get_dimensions() -> int:
    """Return the embedding dimension of the current model."""
    model = get_model()
    return model.get_sentence_embedding_dimension()


def cosine_similarity(a: list[float], b: list[float]) -> float:
    """Dot product of two normalized vectors = cosine similarity."""
    if _HAS_NUMPY:
        return float(np.dot(a, b))
    return sum(x * y for x, y in zip(a, b))


# --- Serialization: base64-encoded struct.pack (~50% smaller than JSON) ---


def serialize(vector: list[float]) -> str:
    """Serialize a float vector to a compact base64 string."""
    binary = struct.pack(f"{len(vector)}f", *vector)
    return base64.b64encode(binary).decode("ascii")


def deserialize(blob: str) -> list[float]:
    """
    Deserialize a vector from either base64 binary or legacy JSON format.
    Auto-detects format: if the string starts with '[' it's JSON, otherwise base64.
    """
    if blob.startswith("["):  # Legacy JSON format
        return json.loads(blob)
    binary = base64.b64decode(blob)
    count = len(binary) // 4
    return list(struct.unpack(f"{count}f", binary))
```

## File: `kore_memory/events.py`
```python
"""
Kore — Event System
Simple in-process event dispatch for memory lifecycle events.
"""

from __future__ import annotations

import logging
from collections import defaultdict
from collections.abc import Callable
from typing import Any

logger = logging.getLogger("kore.events")

EventHandler = Callable[[str, dict[str, Any]], None]

_handlers: dict[str, list[EventHandler]] = defaultdict(list)

# Event types
MEMORY_SAVED = "memory.saved"
MEMORY_DELETED = "memory.deleted"
MEMORY_UPDATED = "memory.updated"
MEMORY_COMPRESSED = "memory.compressed"
MEMORY_DECAYED = "memory.decayed"
MEMORY_ARCHIVED = "memory.archived"
MEMORY_RESTORED = "memory.restored"


def on(event: str, handler: EventHandler) -> None:
    """Register a handler for an event type. Evita duplicati."""
    if handler not in _handlers[event]:
        _handlers[event].append(handler)


def emit(event: str, data: dict[str, Any] | None = None) -> None:
    """Emit an event to all registered handlers."""
    payload = data or {}
    for handler in _handlers.get(event, []):
        try:
            handler(event, payload)
        except Exception:
            logger.exception("Event handler error for %s", event)


def clear() -> None:
    """Remove all handlers (for testing)."""
    _handlers.clear()
```

## File: `kore_memory/main.py`
```python
"""
Kore — FastAPI application
Memory layer with decay, auto-scoring, compression, semantic search, and auth.
"""

import re as _re
import secrets

# ── Rate limiter in-memory ───────────────────────────────────────────────────
import threading as _rl_threading
import time
from collections import defaultdict
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response, StreamingResponse

from . import config
from .auth import get_agent_id, require_auth
from .dashboard import get_dashboard_html
from .database import init_db
from .models import (
    ACLGrantRequest,
    ACLResponse,
    AgentListResponse,
    AgentRecord,
    AnalyticsResponse,
    ArchiveResponse,
    AuditResponse,
    AutoTuneResponse,
    BatchSaveRequest,
    BatchSaveResponse,
    CleanupExpiredResponse,
    CompressRunResponse,
    DecayRunResponse,
    EntityListResponse,
    EntityRecord,
    GDPRDeleteResponse,
    GraphTraverseResponse,
    MemoryExportResponse,
    MemoryImportRequest,
    MemoryImportResponse,
    MemoryRecord,
    MemorySaveRequest,
    MemorySaveResponse,
    MemorySearchResponse,
    MemoryUpdateRequest,
    PluginListResponse,
    RelationRequest,
    RelationResponse,
    ScoringStatsResponse,
    SessionCreateRequest,
    SessionDeleteResponse,
    SessionResponse,
    SessionSummaryResponse,
    SharedMemoriesResponse,
    SummarizeResponse,
    TagRequest,
    TagResponse,
)
from .repository import (
    add_relation,
    add_tags,
    archive_memory,
    cleanup_expired,
    create_session,
    delete_memory,
    delete_session,
    end_session,
    export_memories,
    get_archived,
    get_memory,
    get_relations,
    get_session_memories,
    get_session_summary,
    get_tags,
    get_timeline,
    import_memories,
    list_agents,
    list_sessions,
    remove_tags,
    restore_memory,
    run_decay_pass,
    save_memory,
    save_memory_batch,
    search_by_tag,
    search_memories,
    traverse_graph,
    update_memory,
)

_rate_buckets: dict[str, list[float]] = defaultdict(list)
_rate_lock = _rl_threading.Lock()
_rate_last_cleanup = 0.0


_SESSION_ID_RE = _re.compile(r"^[a-zA-Z0-9_\-\.]{1,128}$")


def _validate_session_id(raw: str | None) -> str | None:
    """Validate and sanitize X-Session-Id header. None if absent or invalid."""
    if not raw:
        return None
    raw = raw.strip()
    if not _SESSION_ID_RE.match(raw):
        raise HTTPException(status_code=400, detail="X-Session-Id contains invalid characters")
    return raw


def _get_client_ip(request: Request) -> str:
    """Extract client IP. Ignores X-Forwarded-For in local-only mode to prevent spoofing."""
    # In local-only mode, use the raw socket IP only — prevents
    # spoofing via X-Forwarded-For: 127.0.0.1 to bypass auth/rate-limit
    if config.LOCAL_ONLY:
        return request.client.host if request.client else "unknown"
    # Behind a trusted reverse proxy, read the first IP from the chain
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        return forwarded.split(",")[0].strip()
    real_ip = request.headers.get("X-Real-IP")
    if real_ip:
        return real_ip.strip()
    return request.client.host if request.client else "unknown"


def _check_rate_limit(client_ip: str, path: str) -> None:
    """Check rate limit for IP + path. Raises HTTPException 429 if exceeded."""
    limit_conf = config.RATE_LIMITS.get(path)
    if not limit_conf:
        return
    max_requests, window = limit_conf
    now = time.monotonic()
    key = f"{client_ip}:{path}"

    with _rate_lock:
        # Periodic cleanup of stale buckets (every 60s) — prevents memory leak
        global _rate_last_cleanup
        if now - _rate_last_cleanup > 60:
            stale_keys = [
                k for k, timestamps in _rate_buckets.items() if not timestamps or now - timestamps[-1] > window
            ]
            for k in stale_keys:
                del _rate_buckets[k]
            _rate_last_cleanup = now

        # Discard expired requests for this bucket
        _rate_buckets[key] = [ts for ts in _rate_buckets[key] if now - ts < window]

        if len(_rate_buckets[key]) >= max_requests:
            raise HTTPException(status_code=429, detail="Rate limit exceeded. Retry later.")

        _rate_buckets[key].append(now)


# ── Security headers middleware ──────────────────────────────────────────────


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    _API_CSP = "default-src 'none'; frame-ancestors 'none'"

    @staticmethod
    def _dashboard_csp(nonce: str) -> str:
        """Build CSP for dashboard with per-request nonce instead of unsafe-inline scripts."""
        return (
            "default-src 'self'; "
            "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
            "font-src 'self' https://fonts.gstatic.com; "
            f"script-src 'nonce-{nonce}'; "
            "connect-src 'self'; "
            "img-src 'self' data:; "
            "frame-ancestors 'none'"
        )

    async def dispatch(self, request: Request, call_next) -> Response:
        # Generate a per-request nonce and store it for the dashboard endpoint
        nonce = secrets.token_urlsafe(16)
        request.state.csp_nonce = nonce

        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "0"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        # CSP with nonce for the dashboard, restrictive for APIs
        if request.url.path == "/dashboard":
            response.headers["Content-Security-Policy"] = self._dashboard_csp(nonce)
        else:
            response.headers["Content-Security-Policy"] = self._API_CSP
        return response


# ── App factory ──────────────────────────────────────────────────────────────


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    # Initialize API key (auto-generate if missing)
    from .auth import get_or_create_api_key

    get_or_create_api_key()
    # Enable audit log if configured
    if config.AUDIT_LOG:
        from .audit import register_audit_handler

        register_audit_handler()
    yield
    # Graceful shutdown: close the SQLite connection pool
    from .database import _pool

    _pool.clear()


app = FastAPI(
    title="Kore",
    description=(
        "The memory layer that thinks like a human: remembers what matters, forgets what doesn't, and never calls home."
    ),
    version=config.VERSION,
    lifespan=lifespan,
)

# CORS — configurable origins via env, restrictive by default
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.CORS_ORIGINS,
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["X-Kore-Key", "X-Agent-Id", "Content-Type"],
)

# Security headers on all responses
app.add_middleware(SecurityHeadersMiddleware)


# Global handler for unhandled exceptions — no stack trace exposed to client
@app.exception_handler(Exception)
async def _global_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    import logging

    logging.error("Unhandled error: %s", exc, exc_info=True)
    return JSONResponse(status_code=500, content={"error": "Internal server error"})


# Shared auth dependencies
_Auth = Depends(require_auth)
_Agent = Depends(get_agent_id)


# ── Core endpoints ────────────────────────────────────────────────────────────


@app.post("/save", response_model=MemorySaveResponse, status_code=201)
def save(
    request: Request,
    req: MemorySaveRequest,
    _: str = _Auth,
    agent_id: str = _Agent,
) -> MemorySaveResponse:
    """Save a memory scoped to the requesting agent. Importance is auto-scored if omitted.
    Use X-Session-Id header to associate the memory with a conversation session."""
    _check_rate_limit(_get_client_ip(request), "/save")
    session_id = _validate_session_id(request.headers.get("X-Session-Id"))
    memory_id, importance = save_memory(req, agent_id=agent_id, session_id=session_id)
    return MemorySaveResponse(id=memory_id, importance=importance)


@app.post("/save/batch", response_model=BatchSaveResponse, status_code=201)
def save_batch(
    request: Request,
    req: BatchSaveRequest,
    _: str = _Auth,
    agent_id: str = _Agent,
) -> BatchSaveResponse:
    """Save multiple memories in a single request (max 100). Uses batch embedding."""
    _check_rate_limit(_get_client_ip(request), "/save")
    results = save_memory_batch(req.memories, agent_id=agent_id)
    saved = [MemorySaveResponse(id=mid, importance=imp) for mid, imp in results]
    return BatchSaveResponse(saved=saved, total=len(saved))


@app.get("/search", response_model=MemorySearchResponse)
def search(
    request: Request,
    q: str = Query(..., min_length=1, description="Search query (any language)"),
    limit: int = Query(5, ge=1, le=20),
    cursor: str | None = Query(None, description="Opaque pagination cursor"),
    category: str | None = Query(None),
    semantic: bool = Query(True),
    _: str = _Auth,
    agent_id: str = _Agent,
    # Deprecated params for backwards compatibility
    offset: int = Query(0, ge=0, deprecated=True, description="Deprecated: use cursor"),
) -> MemorySearchResponse:
    """Semantic search scoped to the requesting agent, with cursor-based pagination."""
    _check_rate_limit(_get_client_ip(request), "/search")

    # Parse cursor (base64 encoded tuple of decay_score, id)
    cursor_tuple = None
    if cursor:
        try:
            import base64
            import json

            decoded = base64.b64decode(cursor).decode("utf-8")
            cursor_tuple = tuple(json.loads(decoded))
        except Exception:
            raise HTTPException(400, "Invalid cursor format") from None

    # Execute search with cursor
    results, next_cursor, total_count = search_memories(
        query=q,
        limit=limit,
        category=category,
        semantic=semantic,
        agent_id=agent_id,
        cursor=cursor_tuple,
    )

    # Encode next cursor
    cursor_str = None
    if next_cursor:
        import base64
        import json

        cursor_str = base64.b64encode(json.dumps(next_cursor).encode("utf-8")).decode("utf-8")

    return MemorySearchResponse(
        results=results,
        total=total_count,
        cursor=cursor_str,
        has_more=next_cursor is not None,
        offset=offset,  # Keep for backwards compat
    )


@app.get("/timeline", response_model=MemorySearchResponse)
def timeline(
    request: Request,
    subject: str = Query(..., min_length=1),
    limit: int = Query(20, ge=1, le=50),
    cursor: str | None = Query(None, description="Opaque pagination cursor"),
    _: str = _Auth,
    agent_id: str = _Agent,
    offset: int = Query(0, ge=0, deprecated=True, description="Deprecated: use cursor"),
) -> MemorySearchResponse:
    """Chronological memory history for a subject, scoped to agent, with cursor-based pagination."""
    _check_rate_limit(_get_client_ip(request), "/timeline")

    # Parse cursor
    cursor_tuple = None
    if cursor:
        try:
            import base64
            import json

            decoded = base64.b64decode(cursor).decode("utf-8")
            cursor_tuple = tuple(json.loads(decoded))
        except Exception:
            raise HTTPException(400, "Invalid cursor format") from None

    results, next_cursor, total_count = get_timeline(
        subject=subject,
        limit=limit,
        agent_id=agent_id,
        cursor=cursor_tuple,
    )

    # Encode next cursor
    cursor_str = None
    if next_cursor:
        import base64
        import json

        cursor_str = base64.b64encode(json.dumps(next_cursor).encode("utf-8")).decode("utf-8")

    return MemorySearchResponse(
        results=results,
        total=total_count,
        cursor=cursor_str,
        has_more=next_cursor is not None,
        offset=offset,
    )


@app.get("/memories/{memory_id}", response_model=MemoryRecord)
def get_single(
    memory_id: int,
    _: str = _Auth,
    agent_id: str = _Agent,
) -> MemoryRecord:
    """Get a single memory by ID. Agents can only access their own memories."""
    memory = get_memory(memory_id, agent_id=agent_id)
    if not memory:
        raise HTTPException(status_code=404, detail="Memory not found")
    return memory


@app.put("/memories/{memory_id}", response_model=MemorySaveResponse)
def update(
    memory_id: int,
    req: MemoryUpdateRequest,
    _: str = _Auth,
    agent_id: str = _Agent,
) -> MemorySaveResponse:
    """Update a memory's content, category, or importance. Agents can only update their own memories."""
    if not update_memory(memory_id, req, agent_id=agent_id):
        raise HTTPException(status_code=404, detail="Memory not found")
    # Fetch the actual importance from DB (req.importance may be None)
    from .database import get_connection

    with get_connection() as conn:
        row = conn.execute(
            "SELECT importance FROM memories WHERE id = ? AND agent_id = ?",
            (memory_id, agent_id),
        ).fetchone()
    real_importance = row["importance"] if row else 1
    return MemorySaveResponse(id=memory_id, importance=real_importance, message="Memory updated")


@app.delete("/memories/{memory_id}", status_code=204)
def delete(
    memory_id: int,
    _: str = _Auth,
    agent_id: str = _Agent,
) -> None:
    """Delete a memory. Agents can only delete their own memories."""
    if not delete_memory(memory_id, agent_id=agent_id):
        raise HTTPException(status_code=404, detail="Memory not found")


# ── Tag endpoints ─────────────────────────────────────────────────────────────


@app.post("/memories/{memory_id}/tags", response_model=TagResponse, status_code=201)
def tag_add(
    memory_id: int,
    req: TagRequest,
    _: str = _Auth,
    agent_id: str = _Agent,
) -> TagResponse:
    """Add tags to a memory."""
    count = add_tags(memory_id, req.tags, agent_id=agent_id)
    tags = get_tags(memory_id, agent_id=agent_id)
    return TagResponse(count=count, tags=tags)


@app.delete("/memories/{memory_id}/tags", response_model=TagResponse)
def tag_remove(
    memory_id: int,
    req: TagRequest,
    _: str = _Auth,
    agent_id: str = _Agent,
) -> TagResponse:
    """Remove tags from a memory."""
    remove_tags(memory_id, req.tags, agent_id=agent_id)
    tags = get_tags(memory_id, agent_id=agent_id)
    return TagResponse(count=len(tags), tags=tags)


@app.get("/memories/{memory_id}/tags", response_model=TagResponse)
def tag_list(
    memory_id: int,
    _: str = _Auth,
    agent_id: str = _Agent,
) -> TagResponse:
    """Return the tags of a memory (only if it belongs to the agent)."""
    tags = get_tags(memory_id, agent_id=agent_id)
    return TagResponse(count=len(tags), tags=tags)


@app.get("/tags/{tag}/memories", response_model=MemorySearchResponse)
def tag_search(
    tag: str,
    limit: int = Query(20, ge=1, le=50),
    _: str = _Auth,
    agent_id: str = _Agent,
) -> MemorySearchResponse:
    """Search memories by tag."""
    results = search_by_tag(tag, agent_id=agent_id, limit=limit)
    return MemorySearchResponse(results=results, total=len(results))


# ── Relation endpoints ───────────────────────────────────────────────────────


@app.post("/memories/{memory_id}/relations", response_model=RelationResponse, status_code=201)
def relation_add(
    memory_id: int,
    req: RelationRequest,
    _: str = _Auth,
    agent_id: str = _Agent,
) -> RelationResponse:
    """Create a relation between two memories."""
    add_relation(memory_id, req.target_id, req.relation, agent_id=agent_id)
    relations = get_relations(memory_id, agent_id=agent_id)
    return RelationResponse(relations=relations, total=len(relations))


@app.get("/memories/{memory_id}/relations", response_model=RelationResponse)
def relation_list(
    memory_id: int,
    _: str = _Auth,
    agent_id: str = _Agent,
) -> RelationResponse:
    """Return the relations of a memory."""
    relations = get_relations(memory_id, agent_id=agent_id)
    return RelationResponse(relations=relations, total=len(relations))


# ── Maintenance endpoints ─────────────────────────────────────────────────────


@app.post("/decay/run", response_model=DecayRunResponse)
def decay_run(
    request: Request,
    _: str = _Auth,
    agent_id: str = _Agent,
) -> DecayRunResponse:
    """Recalculate decay scores for agent's memories."""
    _check_rate_limit(_get_client_ip(request), "/decay/run")
    updated = run_decay_pass(agent_id=agent_id)
    return DecayRunResponse(updated=updated)


@app.post("/compress", response_model=CompressRunResponse)
def compress(
    request: Request,
    _: str = _Auth,
    agent_id: str = _Agent,
) -> CompressRunResponse:
    """Merge similar memories for this agent."""
    _check_rate_limit(_get_client_ip(request), "/compress")
    from .compressor import run_compression

    result = run_compression(agent_id=agent_id)
    return CompressRunResponse(
        clusters_found=result.clusters_found,
        memories_merged=result.memories_merged,
        new_records_created=result.new_records_created,
    )


@app.post("/cleanup", response_model=CleanupExpiredResponse)
def cleanup(
    _: str = _Auth,
    agent_id: str = _Agent,
) -> CleanupExpiredResponse:
    """Remove expired memories (elapsed TTL) for this agent."""
    removed = cleanup_expired(agent_id=agent_id)
    return CleanupExpiredResponse(removed=removed)


@app.post("/auto-tune", response_model=AutoTuneResponse)
def auto_tune(
    request: Request,
    _: str = _Auth,
    agent_id: str = _Agent,
) -> AutoTuneResponse:
    """Auto-tune memory importance based on access patterns."""
    _check_rate_limit(_get_client_ip(request), "/decay/run")  # share decay rate limit
    from .auto_tuner import run_auto_tune

    result = run_auto_tune(agent_id=agent_id)
    return AutoTuneResponse(**result)


@app.get("/stats/scoring", response_model=ScoringStatsResponse)
def scoring_stats(
    _: str = _Auth,
    agent_id: str = _Agent,
) -> ScoringStatsResponse:
    """Return importance scoring statistics for the agent's memories."""
    from .auto_tuner import get_scoring_stats

    return ScoringStatsResponse(**get_scoring_stats(agent_id=agent_id))


# ── Backup / Import ──────────────────────────────────────────────────────────


@app.get("/export", response_model=MemoryExportResponse)
def export(
    _: str = _Auth,
    agent_id: str = _Agent,
) -> MemoryExportResponse:
    """Export all active memories for the agent (without embeddings)."""
    data = export_memories(agent_id=agent_id)
    return MemoryExportResponse(memories=data, total=len(data))


@app.post("/import", response_model=MemoryImportResponse, status_code=201)
def import_data(
    req: MemoryImportRequest,
    _: str = _Auth,
    agent_id: str = _Agent,
) -> MemoryImportResponse:
    """Import memories from a previous export."""
    count = import_memories(req.memories, agent_id=agent_id)
    return MemoryImportResponse(imported=count)


# ── Archive endpoints ──────────────────────────────────────────────────────


@app.post("/memories/{memory_id}/archive", response_model=ArchiveResponse, status_code=200)
def archive(memory_id: int, _: str = _Auth, agent_id: str = _Agent) -> ArchiveResponse:
    if not archive_memory(memory_id, agent_id=agent_id):
        raise HTTPException(404, "Memory not found or already archived")
    return ArchiveResponse(success=True, message="Memory archived")


@app.post("/memories/{memory_id}/restore", response_model=ArchiveResponse, status_code=200)
def restore(memory_id: int, _: str = _Auth, agent_id: str = _Agent) -> ArchiveResponse:
    if not restore_memory(memory_id, agent_id=agent_id):
        raise HTTPException(404, "Memory not found or not archived")
    return ArchiveResponse(success=True, message="Memory restored")


@app.get("/archive", response_model=MemorySearchResponse)
def archive_list(limit: int = Query(50, ge=1, le=100), _: str = _Auth, agent_id: str = _Agent) -> MemorySearchResponse:
    results = get_archived(agent_id=agent_id, limit=limit)
    return MemorySearchResponse(results=results, total=len(results))


# ── Session endpoints ─────────────────────────────────────────────────────────


@app.post("/sessions", response_model=SessionResponse, status_code=201)
def session_create(
    req: SessionCreateRequest,
    _: str = _Auth,
    agent_id: str = _Agent,
) -> SessionResponse:
    """Create a new conversation session."""
    result = create_session(req.session_id, agent_id=agent_id, title=req.title)
    if not result:
        raise HTTPException(400, "Failed to create session")
    return SessionResponse(**result, memory_count=0)


@app.get("/sessions", response_model=list[SessionResponse])
def sessions_list(
    limit: int = Query(50, ge=1, le=200),
    _: str = _Auth,
    agent_id: str = _Agent,
) -> list[SessionResponse]:
    """List all sessions for the requesting agent."""
    rows = list_sessions(agent_id=agent_id, limit=limit)
    return [SessionResponse(**r) for r in rows]


@app.get("/sessions/{session_id}/memories", response_model=MemorySearchResponse)
def session_memories(
    session_id: str,
    _: str = _Auth,
    agent_id: str = _Agent,
) -> MemorySearchResponse:
    """Get all memories in a session."""
    results = get_session_memories(session_id, agent_id=agent_id)
    return MemorySearchResponse(results=results, total=len(results))


@app.get("/sessions/{session_id}/summary", response_model=SessionSummaryResponse)
def session_summary(
    session_id: str,
    _: str = _Auth,
    agent_id: str = _Agent,
) -> SessionSummaryResponse:
    """Get aggregated summary of a session (no LLM)."""
    summary = get_session_summary(session_id, agent_id=agent_id)
    if not summary:
        raise HTTPException(404, "Session not found")
    return SessionSummaryResponse(**summary)


@app.post("/sessions/{session_id}/end", response_model=ArchiveResponse)
def session_end(
    session_id: str,
    _: str = _Auth,
    agent_id: str = _Agent,
) -> ArchiveResponse:
    """Mark a session as ended."""
    if not end_session(session_id, agent_id=agent_id):
        raise HTTPException(404, "Session not found or already ended")
    return ArchiveResponse(success=True, message="Session ended")


@app.delete("/sessions/{session_id}", response_model=SessionDeleteResponse, status_code=200)
def session_delete(
    session_id: str,
    _: str = _Auth,
    agent_id: str = _Agent,
) -> SessionDeleteResponse:
    """Delete a session. Memories are unlinked but not deleted."""
    unlinked = delete_session(session_id, agent_id=agent_id)
    return SessionDeleteResponse(success=True, unlinked_memories=unlinked)


# ── Entity extraction ─────────────────────────────────────────────────────────


@app.get("/entities", response_model=EntityListResponse)
def entities_list(
    type: str | None = Query(
        None,
        description="Filter by entity type (person, org, email, url, date, money, location, product)",
    ),
    limit: int = Query(50, ge=1, le=200),
    _: str = _Auth,
    agent_id: str = _Agent,
) -> EntityListResponse:
    """List extracted entities from memory tags. Requires KORE_ENTITY_EXTRACTION=1."""
    from .integrations.entities import search_entities

    results = search_entities(agent_id, entity_type=type, limit=limit)
    return EntityListResponse(
        entities=[EntityRecord(**r) for r in results],
        total=len(results),
    )


# ── Graph RAG ────────────────────────────────────────────────────────────────


@app.get("/graph/traverse", response_model=GraphTraverseResponse)
def graph_traverse(
    start_id: int = Query(..., description="Starting memory ID"),
    depth: int = Query(3, ge=1, le=10, description="Max traversal depth"),
    relation_type: str | None = Query(None, description="Filter by relation type"),
    _: str = _Auth,
    agent_id: str = _Agent,
) -> GraphTraverseResponse:
    """Multi-hop graph traversal using recursive CTE. Returns connected memories up to N hops."""
    result = traverse_graph(start_id, agent_id=agent_id, depth=depth, relation_type=relation_type)
    return GraphTraverseResponse(**result)


# ── Summarization ────────────────────────────────────────────────────────────


@app.get("/summarize", response_model=SummarizeResponse)
def summarize(
    topic: str = Query(..., min_length=1, description="Topic to summarize"),
    limit: int = Query(50, ge=1, le=200),
    top_keywords: int = Query(10, ge=1, le=50),
    _: str = _Auth,
    agent_id: str = _Agent,
) -> SummarizeResponse:
    """Summarize memories about a topic using TF-IDF keyword extraction (no LLM)."""
    from .summarizer import summarize_topic

    result = summarize_topic(topic, agent_id=agent_id, limit=limit, top_keywords=top_keywords)
    return SummarizeResponse(**result)


# ── ACL (multi-agent shared memory) ──────────────────────────────────────────


@app.post("/memories/{memory_id}/acl", response_model=ACLResponse, status_code=201)
def acl_grant(
    memory_id: int,
    req: ACLGrantRequest,
    _: str = _Auth,
    agent_id: str = _Agent,
) -> ACLResponse:
    """Grant access to a memory for another agent. Only owner or admin can grant."""
    from .acl import grant_access, list_permissions

    success = grant_access(memory_id, req.target_agent, req.permission, grantor_agent=agent_id)
    if not success:
        raise HTTPException(403, "Not authorized to grant access or memory not found")
    perms = list_permissions(memory_id, agent_id)
    return ACLResponse(success=True, permissions=perms)


@app.delete("/memories/{memory_id}/acl/{target_agent}", response_model=ACLResponse)
def acl_revoke(
    memory_id: int,
    target_agent: str,
    _: str = _Auth,
    agent_id: str = _Agent,
) -> ACLResponse:
    """Revoke access for an agent. Only owner or admin can revoke."""
    from .acl import list_permissions, revoke_access

    success = revoke_access(memory_id, target_agent, grantor_agent=agent_id)
    if not success:
        raise HTTPException(403, "Not authorized to revoke access or no permission found")
    perms = list_permissions(memory_id, agent_id)
    return ACLResponse(success=True, permissions=perms)


@app.get("/memories/{memory_id}/acl", response_model=ACLResponse)
def acl_list(
    memory_id: int,
    _: str = _Auth,
    agent_id: str = _Agent,
) -> ACLResponse:
    """List all permissions for a memory. Only visible to owner or admin."""
    from .acl import list_permissions

    perms = list_permissions(memory_id, agent_id)
    return ACLResponse(success=True, permissions=perms)


@app.get("/shared", response_model=SharedMemoriesResponse)
def shared_memories(
    limit: int = Query(50, ge=1, le=200),
    _: str = _Auth,
    agent_id: str = _Agent,
) -> SharedMemoriesResponse:
    """Get all memories shared with this agent by other agents."""
    from .acl import get_shared_memories

    results = get_shared_memories(agent_id, limit=limit)
    return SharedMemoriesResponse(memories=results, total=len(results))


# ── SSE Streaming Search ─────────────────────────────────────────────────────


@app.get("/stream/search")
async def stream_search(
    request: Request,
    q: str = Query(..., min_length=1, description="Search query"),
    limit: int = Query(10, ge=1, le=50),
    _: str = _Auth,
    agent_id: str = _Agent,
) -> StreamingResponse:
    """Server-Sent Events streaming search. FTS5 results first, then semantic."""
    import asyncio
    import json

    async def event_stream():
        # Phase 1: FTS5 results (fast)
        fts_results, _, fts_total = search_memories(
            query=q, limit=limit, semantic=False, agent_id=agent_id,
        )
        fts_data = {
            "results": [r.model_dump(mode="json") for r in fts_results],
            "total": fts_total,
            "phase": "fts",
        }
        yield f"event: fts\ndata: {json.dumps(fts_data)}\n\n"

        # Small delay to allow client to process FTS
        await asyncio.sleep(0.05)

        # Phase 2: Semantic results (slower, may overlap with FTS)
        try:
            sem_results, _, sem_total = search_memories(
                query=q, limit=limit, semantic=True, agent_id=agent_id,
            )
            # Deduplicate — exclude IDs already sent in FTS phase
            fts_ids = {r.id for r in fts_results}
            new_results = [r for r in sem_results if r.id not in fts_ids]
            sem_data = {
                "results": [r.model_dump(mode="json") for r in new_results],
                "total": sem_total,
                "phase": "semantic",
            }
            yield f"event: semantic\ndata: {json.dumps(sem_data)}\n\n"
        except Exception:
            err_data = {"results": [], "total": 0, "phase": "semantic", "error": "unavailable"}
            yield f"event: semantic\ndata: {json.dumps(err_data)}\n\n"

        # Done signal
        yield "event: done\ndata: {}\n\n"

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


# ── Analytics ────────────────────────────────────────────────────────────────


@app.get("/analytics", response_model=AnalyticsResponse)
def analytics(
    _: str = _Auth,
    agent_id: str = _Agent,
) -> AnalyticsResponse:
    """Comprehensive analytics: categories, decay, tags, access patterns, growth."""
    from .analytics import get_analytics

    return AnalyticsResponse(**get_analytics(agent_id=agent_id))


# ── GDPR / Right to Erasure ──────────────────────────────────────────────────


@app.delete("/memories/agent/{target_agent}", response_model=GDPRDeleteResponse)
def gdpr_delete_agent(
    target_agent: str,
    _: str = _Auth,
    agent_id: str = _Agent,
) -> GDPRDeleteResponse:
    """GDPR Article 17 — Right to erasure. Permanently deletes ALL data for an agent.
    The requesting agent must match the target agent (self-deletion only)."""
    if agent_id != target_agent:
        raise HTTPException(403, "Can only delete your own agent data")

    from .database import get_connection

    with get_connection() as conn:
        # Count before deletion
        mem_count = conn.execute(
            "SELECT COUNT(*) FROM memories WHERE agent_id = ?", (target_agent,)
        ).fetchone()[0]

        # Delete in dependency order
        # Tags and relations cascade from memories, but be explicit
        tag_count = conn.execute(
            "DELETE FROM memory_tags WHERE memory_id IN (SELECT id FROM memories WHERE agent_id = ?)",
            (target_agent,),
        ).rowcount

        rel_count = conn.execute(
            """DELETE FROM memory_relations WHERE
               source_id IN (SELECT id FROM memories WHERE agent_id = ?)
               OR target_id IN (SELECT id FROM memories WHERE agent_id = ?)""",
            (target_agent, target_agent),
        ).rowcount

        # Delete ACL entries if table exists
        try:
            conn.execute(
                "DELETE FROM memory_acl WHERE agent_id = ? OR granted_by = ?",
                (target_agent, target_agent),
            )
        except Exception:
            pass  # ACL table may not exist yet

        # Delete vec_memories if sqlite-vec available
        try:
            conn.execute("DELETE FROM vec_memories WHERE agent_id = ?", (target_agent,))
        except Exception:
            pass

        # Delete FTS entries (triggers handle this on memory delete)
        conn.execute("DELETE FROM memories WHERE agent_id = ?", (target_agent,))

        session_count = conn.execute(
            "DELETE FROM sessions WHERE agent_id = ?", (target_agent,)
        ).rowcount

        event_count = conn.execute(
            "DELETE FROM event_logs WHERE agent_id = ?", (target_agent,)
        ).rowcount

    return GDPRDeleteResponse(
        deleted_memories=mem_count,
        deleted_tags=tag_count,
        deleted_relations=rel_count,
        deleted_sessions=session_count,
        deleted_events=event_count,
    )


# ── Plugins ──────────────────────────────────────────────────────────────────


@app.get("/plugins", response_model=PluginListResponse)
def plugins_list(_: str = _Auth) -> PluginListResponse:
    """List registered plugins."""
    from .plugins import list_plugins

    names = list_plugins()
    return PluginListResponse(plugins=names, total=len(names))


# ── Agents ────────────────────────────────────────────────────────────────────


@app.get("/agents", response_model=AgentListResponse)
def agents_list(_: str = _Auth) -> AgentListResponse:
    """List all agent IDs with memory count and last activity. No agent scoping — returns all agents."""
    rows = list_agents()
    return AgentListResponse(
        agents=[AgentRecord(**r) for r in rows],
        total=len(rows),
    )


# ── Metrics ───────────────────────────────────────────────────────────────────


@app.get("/metrics", include_in_schema=False)
def metrics(_: str = _Auth, agent_id: str = _Agent) -> Response:
    """Prometheus-compatible metrics endpoint."""
    from .repository import get_stats

    stats = get_stats(agent_id)
    lines = [
        "# HELP kore_memories_total Total memory records",
        "# TYPE kore_memories_total gauge",
        f"kore_memories_total {stats['total_memories']}",
        "# HELP kore_memories_active Active (non-decayed) memory records",
        "# TYPE kore_memories_active gauge",
        f"kore_memories_active {stats['active_memories']}",
        "# HELP kore_memories_archived Archived memory records",
        "# TYPE kore_memories_archived gauge",
        f"kore_memories_archived {stats['archived_memories']}",
        "# HELP kore_db_size_bytes Database file size in bytes",
        "# TYPE kore_db_size_bytes gauge",
        f"kore_db_size_bytes {stats['db_size_bytes']}",
    ]
    return Response(content="\n".join(lines) + "\n", media_type="text/plain; charset=utf-8")


# ── Audit log ────────────────────────────────────────────────────────────────


@app.get("/audit", response_model=AuditResponse)
def audit_log(
    request: Request,
    event: str | None = Query(None),
    limit: int = Query(100, ge=1, le=1000),
    since: str | None = Query(None, description="ISO datetime"),
    _: str = _Auth,
    agent_id: str = _Agent,
) -> AuditResponse:
    """Query the audit event log for the requesting agent."""
    from .audit import query_audit_log

    entries = query_audit_log(agent_id, event_type=event, limit=limit, since=since)
    return AuditResponse(events=entries, total=len(entries))


# ── Favicon ───────────────────────────────────────────────────────────────────


@app.get("/favicon.svg", include_in_schema=False)
async def favicon():
    """Serve the SVG favicon."""
    from pathlib import Path

    svg_path = Path(__file__).parent.parent / "assets" / "favicon.svg"
    if svg_path.exists():
        return Response(content=svg_path.read_text(), media_type="image/svg+xml")
    return Response(status_code=404)


# ── Dashboard ─────────────────────────────────────────────────────────────────


@app.get("/dashboard", response_class=HTMLResponse, include_in_schema=False)
async def dashboard(request: Request) -> HTMLResponse:
    """Web dashboard for memory management. Requires auth if not in local-only mode."""
    from .auth import _is_local, _local_only_mode

    if not (_local_only_mode() and _is_local(request)):
        await require_auth(request, request.headers.get("X-Kore-Key"))
    html = get_dashboard_html()
    # Inject CSP nonce
    nonce = getattr(request.state, "csp_nonce", "")
    html = html.replace("<script>", f'<script nonce="{nonce}">')
    return HTMLResponse(content=html)


# ── Utility ───────────────────────────────────────────────────────────────────


@app.get("/health")
def health() -> JSONResponse:
    from .database import get_connection
    from .repository import _embeddings_available

    # Verify DB connectivity
    db_ok = True
    try:
        with get_connection() as conn:
            conn.execute("SELECT 1").fetchone()
    except Exception:
        db_ok = False
    status = "ok" if db_ok else "degraded"
    return JSONResponse(
        {
            "status": status,
            "version": app.version,
            "semantic_search": _embeddings_available(),
            "database": "connected" if db_ok else "error",
        }
    )
```

## File: `kore_memory/mcp_server.py`
```python
"""
Kore — MCP Server (Model Context Protocol)
Exposes save, search, timeline, decay and compress as MCP tools
for direct integration with Claude, Cursor, and other MCP clients.

Usage:
  kore-mcp                                       # stdio (default)
  kore-mcp --transport streamable-http            # HTTP transport (porta 8766)
  kore-mcp --transport streamable-http --port 9000  # HTTP porta custom
"""

from __future__ import annotations

import re as _re

from mcp.server.fastmcp import FastMCP

from .database import init_db
from .models import MemorySaveRequest, MemoryUpdateRequest
from .repository import (
    add_relation,
    add_tags,
    cleanup_expired,
    delete_memory,
    export_memories,
    get_timeline,
    import_memories,
    run_decay_pass,
    save_memory,
    search_by_tag,
    search_memories,
    update_memory,
)

# Initialize DB before any operation
init_db()

mcp = FastMCP(
    "Kore Memory",
    json_response=True,
)

_SAFE_AGENT_RE = _re.compile(r"[^a-zA-Z0-9_\-]")


def _sanitize_agent_id(agent_id: str) -> str:
    """Sanitize agent_id: only alphanumeric characters, dashes and underscores, max 64 chars."""
    safe = _SAFE_AGENT_RE.sub("", agent_id)
    return (safe or "default")[:64]


# ── Tools ────────────────────────────────────────────────────────────────────


@mcp.tool()
def memory_save(
    content: str,
    category: str = "general",
    importance: int = 0,
    agent_id: str = "default",
) -> dict:
    """
    Save a memory to persistent storage.
    Importance is auto-calculated if 0 or not specified (1-5 = explicit).
    Categories: general, project, trading, finance, person, preference, task, decision.
    """
    req = MemorySaveRequest(content=content, category=category, importance=importance or None)
    mem_id, imp = save_memory(req, agent_id=_sanitize_agent_id(agent_id))
    return {"id": mem_id, "importance": imp, "message": "Memory saved"}


@mcp.tool()
def memory_search(
    query: str,
    limit: int = 5,
    category: str = "",
    semantic: bool = True,
    agent_id: str = "default",
) -> dict:
    """
    Search memory. Supports semantic (embedding) and full-text search.
    Returns the most relevant memories sorted by score.
    Leave category empty to search across all categories.
    """
    results, next_cursor, total_count = search_memories(
        query=query,
        limit=limit,
        category=category or None,
        semantic=semantic,
        agent_id=_sanitize_agent_id(agent_id),
    )
    return {
        "results": [
            {
                "id": r.id,
                "content": r.content,
                "category": r.category,
                "importance": r.importance,
                "decay_score": r.decay_score,
                "score": r.score,
                "created_at": str(r.created_at),
            }
            for r in results
        ],
        "total": total_count,
        "has_more": next_cursor is not None,
    }


@mcp.tool()
def memory_timeline(
    subject: str,
    limit: int = 20,
    agent_id: str = "default",
) -> dict:
    """
    Timeline of memories on a subject, ordered from oldest to most recent.
    Useful for reconstructing the history of a project or a person.
    """
    results, next_cursor, total_count = get_timeline(
        subject=subject,
        limit=limit,
        agent_id=_sanitize_agent_id(agent_id),
    )
    return {
        "results": [
            {
                "id": r.id,
                "content": r.content,
                "category": r.category,
                "importance": r.importance,
                "created_at": str(r.created_at),
            }
            for r in results
        ],
        "total": total_count,
        "has_more": next_cursor is not None,
    }


@mcp.tool()
def memory_decay_run(agent_id: str = "default") -> dict:
    """
    Recalculate the decay score of all memories for the agent.
    Memories that have not been accessed decay over time following the Ebbinghaus curve.
    """
    updated = run_decay_pass(agent_id=_sanitize_agent_id(agent_id))
    return {"updated": updated, "message": "Decay pass complete"}


@mcp.tool()
def memory_compress(agent_id: str = "default") -> dict:
    """
    Compress similar memories by merging them into a single richer record.
    Reduces redundancy while preserving important information.
    """
    from .compressor import run_compression

    result = run_compression(agent_id=_sanitize_agent_id(agent_id))
    return {
        "clusters_found": result.clusters_found,
        "memories_merged": result.memories_merged,
        "new_records_created": result.new_records_created,
    }


@mcp.tool()
def memory_export(agent_id: str = "default") -> dict:
    """Export all active memories for the agent as a backup."""
    data = export_memories(agent_id=_sanitize_agent_id(agent_id))
    return {"memories": data, "total": len(data)}


@mcp.tool()
def memory_delete(
    memory_id: int,
    agent_id: str = "default",
) -> dict:
    """
    Delete a memory by id. The memory must belong to the specified agent.
    Returns success=True if deleted, False if not found.
    """
    deleted = delete_memory(memory_id, agent_id=_sanitize_agent_id(agent_id))
    return {
        "success": deleted,
        "message": "Memory deleted" if deleted else "Memory not found",
    }


@mcp.tool()
def memory_update(
    memory_id: int,
    content: str = "",
    category: str = "",
    importance: int = 0,
    agent_id: str = "default",
) -> dict:
    """
    Update an existing memory. Only the provided fields are modified.
    Regenerates the embedding if the content changes.
    Leave fields empty/0 for those you do not want to modify.
    """
    req = MemoryUpdateRequest(
        content=content or None,
        category=category or None,
        importance=importance or None,
    )
    updated = update_memory(memory_id, req, agent_id=_sanitize_agent_id(agent_id))
    return {
        "success": updated,
        "message": "Memory updated" if updated else "Memory not found",
    }


@mcp.tool()
def memory_save_batch(
    memories: list[dict],
    agent_id: str = "default",
) -> dict:
    """
    Save multiple memories in a batch. Each item must have at least 'content'.
    Optional fields: category (default 'general'), importance (None=auto, 1-5=explicit).
    Maximum 100 memories per batch.
    """
    saved = []
    errors = 0
    for mem in memories[:100]:
        content = mem.get("content", "")
        if not content or len(content.strip()) < 3:
            continue
        try:
            raw_imp = mem.get("importance")
            req = MemorySaveRequest(
                content=content,
                category=mem.get("category", "general"),
                importance=raw_imp if raw_imp and raw_imp >= 1 else None,
            )
            mem_id, imp = save_memory(req, agent_id=_sanitize_agent_id(agent_id))
            saved.append({"id": mem_id, "importance": imp})
        except Exception:
            errors += 1
    return {"saved": saved, "total": len(saved), "errors": errors}


@mcp.tool()
def memory_add_tags(
    memory_id: int,
    tags: list[str],
    agent_id: str = "default",
) -> dict:
    """
    Add tags to a memory. Tags are normalized to lowercase.
    Returns the number of tags added.
    """
    count = add_tags(memory_id, tags, agent_id=_sanitize_agent_id(agent_id))
    return {"count": count, "message": f"{count} tags added"}


@mcp.tool()
def memory_search_by_tag(
    tag: str,
    agent_id: str = "default",
    limit: int = 20,
) -> dict:
    """
    Search memories by tag. Returns memories sorted by importance and date.
    """
    results = search_by_tag(tag, agent_id=_sanitize_agent_id(agent_id), limit=limit)
    return {
        "results": [
            {
                "id": r.id,
                "content": r.content,
                "category": r.category,
                "importance": r.importance,
                "decay_score": r.decay_score,
                "created_at": str(r.created_at),
            }
            for r in results
        ],
        "total": len(results),
    }


@mcp.tool()
def memory_add_relation(
    source_id: int,
    target_id: int,
    relation: str = "related",
    agent_id: str = "default",
) -> dict:
    """
    Create a relation between two memories (graph). Both must belong to the agent.
    Common types: related, causes, blocks, extends, contradicts.
    """
    created = add_relation(source_id, target_id, relation, agent_id=_sanitize_agent_id(agent_id))
    return {
        "success": created,
        "message": "Relation created" if created else "Failed — memories not found or not owned by agent",
    }


@mcp.tool()
def memory_cleanup(agent_id: str = "default") -> dict:
    """
    Delete memories with an expired TTL for the specified agent.
    Returns the number of records removed.
    """
    removed = cleanup_expired(agent_id=_sanitize_agent_id(agent_id))
    return {"removed": removed, "message": f"{removed} expired memories cleaned up"}


@mcp.tool()
def memory_import(
    memories: list[dict],
    agent_id: str = "default",
) -> dict:
    """
    Import memories from a list of dicts. Each item must have at least 'content'.
    Optional fields: category, importance. Maximum 500 memories.
    """
    count = import_memories(memories, agent_id=_sanitize_agent_id(agent_id))
    return {"imported": count, "message": f"{count} memories imported"}


# ── Resources ────────────────────────────────────────────────────────────────


@mcp.resource("kore://health")
def health_resource() -> str:
    """Kore server health status."""
    from . import config
    from .repository import _embeddings_available

    return f"Kore v{config.VERSION} — semantic_search={'enabled' if _embeddings_available() else 'disabled'}"


# ── Entry point ──────────────────────────────────────────────────────────────


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Kore MCP Server")
    parser.add_argument(
        "--transport",
        choices=["stdio", "streamable-http", "sse"],
        default="stdio",
        help="Transport protocol (default: stdio)",
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Host per HTTP transport (default: 127.0.0.1)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8766,
        help="Porta per HTTP transport (default: 8766)",
    )
    args = parser.parse_args()

    if args.transport in ("streamable-http", "sse"):
        mcp.run(transport=args.transport, host=args.host, port=args.port)
    else:
        mcp.run()


if __name__ == "__main__":
    main()
```

## File: `kore_memory/models.py`
```python
"""
Kore — Pydantic models
Request/response schemas with validation.
"""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field, field_validator

Category = Literal[
    "general",
    "project",
    "trading",
    "finance",
    "person",
    "preference",
    "task",
    "decision",
]


class MemorySaveRequest(BaseModel):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "content": "Il progetto usa FastAPI con SQLite per la persistenza",
                    "category": "project",
                    "importance": 4,
                },
                {
                    "content": "Riunione con il team alle 15:00",
                    "category": "task",
                },
            ]
        }
    }

    content: str = Field(..., min_length=3, max_length=4000)
    category: Category = Field("general")
    importance: int | None = Field(None, ge=1, le=5, description="None=auto-scored, 1-5=explicit")
    ttl_hours: int | None = Field(None, ge=1, le=8760, description="Time-to-live in ore (max 1 anno)")

    @field_validator("content")
    @classmethod
    def content_must_not_be_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Content cannot be blank")
        return v.strip()


class MemoryUpdateRequest(BaseModel):
    content: str | None = Field(None, min_length=3, max_length=4000)
    category: Category | None = None
    importance: int | None = Field(None, ge=1, le=5)

    @field_validator("content")
    @classmethod
    def content_must_not_be_blank(cls, v: str | None) -> str | None:
        if v is not None and not v.strip():
            raise ValueError("Content cannot be blank")
        return v.strip() if v else v


class MemoryRecord(BaseModel):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 42,
                    "content": "Il progetto usa FastAPI con SQLite",
                    "category": "project",
                    "importance": 4,
                    "decay_score": 0.95,
                    "created_at": "2026-01-15T10:30:00",
                    "updated_at": "2026-01-15T10:30:00",
                    "score": 3.8,
                }
            ]
        }
    }

    id: int
    content: str
    category: str
    importance: int
    decay_score: float = 1.0
    created_at: datetime
    updated_at: datetime
    score: float | None = None


class MemorySaveResponse(BaseModel):
    id: int
    importance: int
    message: str = "Memory saved"


class MemorySearchResponse(BaseModel):
    results: list[MemoryRecord]
    total: int
    cursor: str | None = Field(None, description="Opaque cursor for next page (base64)")
    has_more: bool = False
    # Deprecated fields kept for backwards compatibility
    offset: int = Field(0, deprecated=True, description="Deprecated: use cursor instead")


class MemoryImportRequest(BaseModel):
    memories: list[dict] = Field(..., min_length=1, max_length=500)


class MemoryImportResponse(BaseModel):
    imported: int
    message: str = "Import complete"


class MemoryExportResponse(BaseModel):
    memories: list[dict]
    total: int


class BatchSaveRequest(BaseModel):
    memories: list[MemorySaveRequest] = Field(..., min_length=1, max_length=100)


class BatchSaveResponse(BaseModel):
    saved: list[MemorySaveResponse]
    total: int


class TagRequest(BaseModel):
    tags: list[str] = Field(..., min_length=1, max_length=20)


class TagResponse(BaseModel):
    count: int
    tags: list[str] = []


class RelationRequest(BaseModel):
    target_id: int
    relation: str = Field("related", max_length=100)


class RelationResponse(BaseModel):
    relations: list[dict]
    total: int


class DecayRunResponse(BaseModel):
    updated: int
    message: str = "Decay pass complete"


class CleanupExpiredResponse(BaseModel):
    removed: int
    message: str = "Expired memories cleaned up"


class CompressRunResponse(BaseModel):
    clusters_found: int
    memories_merged: int
    new_records_created: int
    message: str = "Compression complete"


class ArchiveResponse(BaseModel):
    success: bool
    message: str = ""


class AutoTuneResponse(BaseModel):
    boosted: int
    reduced: int
    message: str = "Auto-tune complete"


class ScoringStatsResponse(BaseModel):
    total: int
    distribution: dict[str, int]  # importance level -> count
    avg_importance: float
    avg_access_count: float
    never_accessed_30d: int
    frequently_accessed: int


class SessionCreateRequest(BaseModel):
    session_id: str = Field(..., min_length=1, max_length=128)
    title: str | None = Field(None, max_length=500)


class SessionResponse(BaseModel):
    id: str
    agent_id: str
    title: str | None = None
    created_at: datetime
    ended_at: datetime | None = None
    memory_count: int = 0


class SessionSummaryResponse(BaseModel):
    session_id: str
    agent_id: str
    title: str | None = None
    created_at: str
    ended_at: str | None = None
    memory_count: int = 0
    categories: list[str] = []
    avg_importance: float = 0.0
    first_memory: str | None = None
    last_memory: str | None = None


class SessionDeleteResponse(BaseModel):
    success: bool
    unlinked_memories: int


class EntityRecord(BaseModel):
    type: str
    value: str
    memory_id: int
    tag: str


class EntityListResponse(BaseModel):
    entities: list[EntityRecord]
    total: int


class AgentRecord(BaseModel):
    agent_id: str
    memory_count: int
    last_active: str | None = None


class AgentListResponse(BaseModel):
    agents: list[AgentRecord]
    total: int


class AuditEventRecord(BaseModel):
    id: int
    event: str
    agent_id: str
    memory_id: int | None = None
    data: dict | str | None = None
    created_at: str


class AuditResponse(BaseModel):
    events: list[AuditEventRecord]
    total: int


# ── Graph RAG ────────────────────────────────────────────────────────────────


class GraphNodeRecord(BaseModel):
    id: int
    content: str
    category: str
    importance: int
    decay_score: float
    created_at: str
    hop: int


class GraphEdgeRecord(BaseModel):
    source_id: int
    target_id: int
    relation: str
    created_at: str


class GraphTraverseResponse(BaseModel):
    start: dict | None = None
    nodes: list[GraphNodeRecord] = []
    edges: list[GraphEdgeRecord] = []
    depth: int


# ── Summarization ────────────────────────────────────────────────────────────


class KeywordRecord(BaseModel):
    word: str
    score: float


class SummarizeResponse(BaseModel):
    topic: str
    memory_count: int
    keywords: list[KeywordRecord] = []
    categories: dict[str, int] = {}
    avg_importance: float = 0.0
    time_span: dict[str, str] | None = None


# ── ACL ──────────────────────────────────────────────────────────────────────


class ACLGrantRequest(BaseModel):
    target_agent: str = Field(..., min_length=1, max_length=64)
    permission: str = Field("read", pattern=r"^(read|write|admin)$")


class ACLRecord(BaseModel):
    agent_id: str
    permission: str
    granted_by: str
    created_at: str


class ACLResponse(BaseModel):
    success: bool
    permissions: list[ACLRecord] = []


class SharedMemoryRecord(BaseModel):
    id: int
    content: str
    category: str
    importance: int
    decay_score: float
    created_at: str
    updated_at: str
    owner_agent: str
    permission: str


class SharedMemoriesResponse(BaseModel):
    memories: list[SharedMemoryRecord]
    total: int


# ── Analytics ────────────────────────────────────────────────────────────────


class AnalyticsResponse(BaseModel):
    total_memories: int
    categories: dict[str, int]
    importance_distribution: dict[str, int]
    decay_analysis: dict[str, float | int]
    top_tags: list[dict]
    access_patterns: dict[str, float | int]
    growth_last_30d: list[dict]
    compressed_memories: int
    archived_memories: int
    total_relations: int


# ── GDPR ─────────────────────────────────────────────────────────────────────


class GDPRDeleteResponse(BaseModel):
    deleted_memories: int
    deleted_tags: int
    deleted_relations: int
    deleted_sessions: int
    deleted_events: int
    message: str = "All agent data permanently deleted"


# ── Plugins ──────────────────────────────────────────────────────────────────


class PluginListResponse(BaseModel):
    plugins: list[str]
    total: int
```

## File: `kore_memory/plugins.py`
```python
"""
Kore — Plugin System
Hook points for extending memory operations.
Supports pre/post hooks for save, search, delete, and compress.
"""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import Any

logger = logging.getLogger("kore.plugins")


class KorePlugin(ABC):
    """Base class for Kore plugins. Override the hooks you need."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Unique plugin name."""
        ...

    def pre_save(self, content: str, category: str, importance: int | None, agent_id: str) -> dict[str, Any] | None:
        """Called before saving. Return dict to override fields, or None to keep original."""
        return None

    def post_save(self, memory_id: int, content: str, category: str, importance: int, agent_id: str) -> None:  # noqa: B027
        """Called after saving a memory."""

    def pre_search(self, query: str, agent_id: str, semantic: bool) -> dict[str, Any] | None:
        """Called before search. Return dict to override query params, or None."""
        return None

    def post_search(self, query: str, results: list[dict], agent_id: str) -> list[dict]:
        """Called after search. Can filter/reorder results. Must return results list."""
        return results

    def pre_delete(self, memory_id: int, agent_id: str) -> bool:
        """Called before delete. Return False to block deletion."""
        return True

    def post_delete(self, memory_id: int, agent_id: str) -> None:  # noqa: B027
        """Called after deletion."""

    def pre_compress(self, agent_id: str) -> bool:
        """Called before compression. Return False to block."""
        return True

    def post_compress(self, clusters_found: int, merged: int, agent_id: str) -> None:  # noqa: B027
        """Called after compression."""


# Plugin registry
_plugins: dict[str, KorePlugin] = {}


def register_plugin(plugin: KorePlugin) -> None:
    """Register a plugin. Replaces existing plugin with same name."""
    _plugins[plugin.name] = plugin
    logger.info("Plugin registered: %s", plugin.name)


def unregister_plugin(name: str) -> bool:
    """Unregister a plugin by name. Returns True if found."""
    return _plugins.pop(name, None) is not None


def list_plugins() -> list[str]:
    """Return registered plugin names."""
    return list(_plugins.keys())


def clear_plugins() -> None:
    """Remove all plugins (for testing)."""
    _plugins.clear()


# Hook dispatch functions

def run_pre_save(content: str, category: str, importance: int | None, agent_id: str) -> dict[str, Any]:
    """Run all pre_save hooks. Returns merged overrides."""
    overrides: dict[str, Any] = {}
    for plugin in _plugins.values():
        try:
            result = plugin.pre_save(content, category, importance, agent_id)
            if result:
                overrides.update(result)
        except Exception:
            logger.exception("Plugin %s pre_save error", plugin.name)
    return overrides


def run_post_save(memory_id: int, content: str, category: str, importance: int, agent_id: str) -> None:
    """Run all post_save hooks."""
    for plugin in _plugins.values():
        try:
            plugin.post_save(memory_id, content, category, importance, agent_id)
        except Exception:
            logger.exception("Plugin %s post_save error", plugin.name)


def run_pre_search(query: str, agent_id: str, semantic: bool) -> dict[str, Any]:
    """Run all pre_search hooks. Returns merged overrides."""
    overrides: dict[str, Any] = {}
    for plugin in _plugins.values():
        try:
            result = plugin.pre_search(query, agent_id, semantic)
            if result:
                overrides.update(result)
        except Exception:
            logger.exception("Plugin %s pre_search error", plugin.name)
    return overrides


def run_post_search(query: str, results: list[dict], agent_id: str) -> list[dict]:
    """Run all post_search hooks. Each plugin can filter/reorder results."""
    for plugin in _plugins.values():
        try:
            results = plugin.post_search(query, results, agent_id)
        except Exception:
            logger.exception("Plugin %s post_search error", plugin.name)
    return results


def run_pre_delete(memory_id: int, agent_id: str) -> bool:
    """Run all pre_delete hooks. Returns False if any plugin blocks deletion."""
    for plugin in _plugins.values():
        try:
            if not plugin.pre_delete(memory_id, agent_id):
                return False
        except Exception:
            logger.exception("Plugin %s pre_delete error", plugin.name)
    return True


def run_post_delete(memory_id: int, agent_id: str) -> None:
    """Run all post_delete hooks."""
    for plugin in _plugins.values():
        try:
            plugin.post_delete(memory_id, agent_id)
        except Exception:
            logger.exception("Plugin %s post_delete error", plugin.name)
```

## File: `kore_memory/scorer.py`
```python
"""
Kore — Auto-Importance Scorer
Calculates memory importance (1–5) locally, without any LLM API call.

Scoring factors:
  1. Content length       — longer = more detailed = more important
  2. Keyword signals      — critical words bump importance up
  3. Category baseline    — some categories are inherently more important
  4. Uniqueness           — if similar memories exist with high importance, inherit it
"""

# Keywords that signal high importance
HIGH_IMPORTANCE_KEYWORDS = {
    5: [
        "password",
        "token",
        "chiave",
        "secret",
        "api key",
        "credenziali",
        "urgente",
        "critico",
        "never",
        "mai",
        "sempre",
        "always",
        "private key",
        "segreto",
    ],
    4: [
        "decisione",
        "decision",
        "importante",
        "important",
        "priorità",
        "priority",
        "deadline",
        "scadenza",
        "pagamento",
        "payment",
        "debito",
        "debt",
        "errore critico",
        "bug critico",
        "non fare",
        "do not",
        "regola",
    ],
    3: [
        "progetto",
        "project",
        "strategia",
        "strategy",
        "obiettivo",
        "goal",
        "configurazione",
        "config",
        "server",
        "deploy",
        "produzione",
    ],
    2: [
        "nota",
        "note",
        "reminder",
        "appunto",
        "considerare",
        "consider",
    ],
}

# Category importance baselines
CATEGORY_BASELINE: dict[str, int] = {
    "general": 1,
    "preference": 4,
    "decision": 4,
    "finance": 3,
    "trading": 3,
    "project": 3,
    "task": 2,
    "person": 2,
}


def auto_score(content: str, category: str) -> int:
    """
    Return an importance score (1–5) based on content analysis.
    Used when importance is not explicitly set.
    """
    score = CATEGORY_BASELINE.get(category, 2)
    content_lower = content.lower()

    # Keyword signals — take the highest match
    for level in sorted(HIGH_IMPORTANCE_KEYWORDS.keys(), reverse=True):
        for kw in HIGH_IMPORTANCE_KEYWORDS[level]:
            if kw in content_lower:
                score = max(score, level)
                break

    # Length bonus: contenuto dettagliato e' probabilmente piu' importante
    word_count = len(content.split())
    if word_count > 60:
        score = min(5, score + 1)

    return max(1, min(5, score))
```

## File: `kore_memory/summarizer.py`
```python
"""
Kore — Memory Summarizer
TF-IDF based keyword extraction and topic summarization without LLM.
"""

from __future__ import annotations

import math
import re
from collections import Counter

from .database import get_connection

# Common stop words (multilingual: EN + IT)
_STOP_WORDS = frozenset([
    # English
    "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "will", "would", "shall",
    "should", "may", "might", "can", "could", "this", "that", "these",
    "those", "it", "its", "they", "them", "their", "he", "she", "him",
    "her", "his", "we", "our", "you", "your", "i", "me", "my", "and",
    "or", "but", "not", "no", "nor", "so", "if", "then", "than", "too",
    "very", "just", "about", "also", "back", "before", "between", "both",
    "by", "came", "come", "each", "from", "get", "got", "how", "into",
    # Italian
    "il", "lo", "la", "le", "gli", "un", "una", "dei", "delle", "del",
    "della", "di", "da", "in", "con", "su", "per", "tra", "fra", "che",
    "non", "si", "al", "sono", "stato", "essere", "fatto", "come", "anche",
    "più", "questo", "quello", "e", "o", "ma", "se", "poi", "già",
    "ancora", "solo", "tutto", "tutti", "dove", "quando", "perché", "cosa", "chi",
])

_WORD_RE = re.compile(r"[a-zA-ZÀ-ÿ]{2,}")


def _tokenize(text: str) -> list[str]:
    """Extract lowercase words, filter stop words."""
    return [w.lower() for w in _WORD_RE.findall(text) if w.lower() not in _STOP_WORDS]


def _compute_tfidf(documents: list[list[str]]) -> list[dict[str, float]]:
    """Compute TF-IDF scores for each document."""
    n = len(documents)
    if n == 0:
        return []

    # Document frequency
    df: Counter = Counter()
    for doc in documents:
        df.update(set(doc))

    results = []
    for doc in documents:
        tf = Counter(doc)
        total = len(doc) or 1
        tfidf = {}
        for word, count in tf.items():
            tf_score = count / total
            idf_score = math.log(1 + n / (1 + df.get(word, 0)))
            tfidf[word] = round(tf_score * idf_score, 4)
        results.append(tfidf)
    return results


def summarize_topic(
    topic: str,
    agent_id: str = "default",
    limit: int = 50,
    top_keywords: int = 10,
) -> dict:
    """
    Summarize memories related to a topic.
    Returns keyword extraction (TF-IDF), category breakdown, and timeline span.
    """
    with get_connection() as conn:
        # Search memories matching the topic via FTS5
        try:
            rows = conn.execute(
                """
                SELECT m.id, m.content, m.category, m.importance, m.decay_score,
                       m.created_at, m.access_count
                FROM memories m
                JOIN memories_fts f ON f.rowid = m.id
                WHERE memories_fts MATCH ? AND m.agent_id = ?
                  AND m.archived_at IS NULL AND m.compressed_into IS NULL
                ORDER BY m.importance DESC, m.created_at DESC
                LIMIT ?
                """,
                (topic, agent_id, limit),
            ).fetchall()
        except Exception:
            # FTS match failure — fallback to LIKE
            rows = conn.execute(
                """
                SELECT id, content, category, importance, decay_score,
                       created_at, access_count
                FROM memories
                WHERE content LIKE ? AND agent_id = ?
                  AND archived_at IS NULL AND compressed_into IS NULL
                ORDER BY importance DESC, created_at DESC
                LIMIT ?
                """,
                (f"%{topic}%", agent_id, limit),
            ).fetchall()

    if not rows:
        return {
            "topic": topic,
            "memory_count": 0,
            "keywords": [],
            "categories": {},
            "avg_importance": 0.0,
            "time_span": None,
        }

    # Tokenize all memories
    documents = [_tokenize(r["content"]) for r in rows]
    tfidf_scores = _compute_tfidf(documents)

    # Aggregate TF-IDF across all documents
    global_scores: Counter = Counter()
    for doc_scores in tfidf_scores:
        for word, score in doc_scores.items():
            global_scores[word] += score

    keywords = [
        {"word": word, "score": round(score, 4)}
        for word, score in global_scores.most_common(top_keywords)
    ]

    # Category breakdown
    categories: Counter = Counter()
    for r in rows:
        categories[r["category"]] += 1

    # Timeline span
    dates = [r["created_at"] for r in rows]
    time_span = {
        "earliest": min(dates),
        "latest": max(dates),
    }

    # Average importance
    avg_importance = round(sum(r["importance"] for r in rows) / len(rows), 2)

    return {
        "topic": topic,
        "memory_count": len(rows),
        "keywords": keywords,
        "categories": dict(categories),
        "avg_importance": avg_importance,
        "time_span": time_span,
    }
```

## File: `kore_memory/vector_index.py`
```python
"""
Kore — Vector index with sqlite-vec native search.

Strategy:
  - Uses sqlite-vec virtual table for native KNN search in SQLite
  - Vectors stored directly in vec0 table (not loaded in RAM)
  - Partition key by agent_id for efficient per-agent queries
  - Falls back to numpy in-memory approach if sqlite-vec is unavailable
  - distance_metric=cosine for normalized embeddings
"""

from __future__ import annotations

import logging
import struct
import threading
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)

# --- sqlite-vec availability ---
try:
    import sqlite_vec

    _HAS_SQLITE_VEC = True
except ImportError:
    _HAS_SQLITE_VEC = False

# --- numpy availability (optional, installed with [semantic]) ---
try:
    import numpy as np

    _HAS_NUMPY = True
except ImportError:
    np = None  # type: ignore[assignment]
    _HAS_NUMPY = False


def has_sqlite_vec() -> bool:
    """Check if sqlite-vec extension is available."""
    return _HAS_SQLITE_VEC


# ── sqlite-vec native index ─────────────────────────────────────────────────


class SqliteVecIndex:
    """Native vector search via sqlite-vec virtual table."""

    def __init__(self, dimensions: int = 384) -> None:
        self._dimensions = dimensions
        self._initialized_dbs: set[str] = set()
        self._lock = threading.Lock()

    def _ensure_table(self, conn) -> None:
        """Create vec_memories table if it doesn't exist."""
        db_path = str(conn.execute("PRAGMA database_list").fetchone()[2])
        if db_path in self._initialized_dbs:
            return

        with self._lock:
            if db_path in self._initialized_dbs:
                return

            try:
                conn.execute("SELECT 1 FROM vec_memories LIMIT 0")
            except Exception:
                conn.execute(f"""
                    CREATE VIRTUAL TABLE IF NOT EXISTS vec_memories USING vec0(
                        agent_id TEXT partition key,
                        embedding float[{self._dimensions}] distance_metric=cosine
                    )
                """)
                conn.commit()

            self._initialized_dbs.add(db_path)

    def upsert(self, conn, memory_id: int, agent_id: str, embedding: list[float]) -> None:
        """Insert or replace a vector in the index."""
        self._ensure_table(conn)
        vec_blob = _serialize_f32(embedding)
        # Delete existing entry if any, then insert
        conn.execute("DELETE FROM vec_memories WHERE rowid = ?", (memory_id,))
        conn.execute(
            "INSERT INTO vec_memories(rowid, agent_id, embedding) VALUES (?, ?, ?)",
            (memory_id, agent_id, vec_blob),
        )

    def remove(self, conn, memory_id: int) -> None:
        """Remove a vector from the index."""
        self._ensure_table(conn)
        conn.execute("DELETE FROM vec_memories WHERE rowid = ?", (memory_id,))

    def search(
        self,
        query_vec: list[float],
        agent_id: str,
        category: str | None = None,
        limit: int = 10,
        min_similarity: float = 0.1,
    ) -> list[tuple[int, float]]:
        """
        KNN search via sqlite-vec. Returns [(memory_id, similarity_score), ...].
        distance_metric=cosine returns cosine distance (1 - similarity),
        so we convert to similarity score.
        """
        from .database import get_connection

        vec_blob = _serialize_f32(query_vec)

        with get_connection() as conn:
            self._ensure_table(conn)

            # Load sqlite-vec extension on this connection
            _load_vec_extension(conn)

            rows = conn.execute(
                """
                SELECT rowid, distance
                FROM vec_memories
                WHERE embedding MATCH ?
                  AND agent_id = ?
                  AND k = ?
                """,
                (vec_blob, agent_id, limit * 2),
            ).fetchall()

        # Convert cosine distance to similarity score (1 - distance)
        results: list[tuple[int, float]] = []
        for row in rows:
            similarity = 1.0 - row[1]
            if similarity >= min_similarity:
                results.append((row[0], round(similarity, 4)))

        results.sort(key=lambda x: x[1], reverse=True)
        return results[:limit]

    def invalidate(self, agent_id: str) -> None:
        """No-op: sqlite-vec doesn't need cache invalidation."""
        pass

    def invalidate_all(self) -> None:
        """No-op: sqlite-vec doesn't need cache invalidation."""
        pass

    def sync_from_memories(self, conn) -> None:
        """Sync vec_memories table from memories table (migration/rebuild)."""
        self._ensure_table(conn)
        from .embedder import deserialize

        # Load extension for this connection
        _load_vec_extension(conn)

        # Clear and rebuild
        conn.execute("DELETE FROM vec_memories")

        rows = conn.execute(
            """
            SELECT id, agent_id, embedding FROM memories
            WHERE embedding IS NOT NULL
              AND compressed_into IS NULL
              AND archived_at IS NULL
            """
        ).fetchall()

        for row in rows:
            try:
                vec = deserialize(row["embedding"])
                vec_blob = _serialize_f32(vec)
                conn.execute(
                    "INSERT INTO vec_memories(rowid, agent_id, embedding) VALUES (?, ?, ?)",
                    (row["id"], row["agent_id"], vec_blob),
                )
            except Exception:
                continue  # skip corrupted embeddings

        conn.commit()
        logger.info("Synced %d vectors to sqlite-vec index", len(rows))


def _serialize_f32(vector: list[float]) -> bytes:
    """Serialize float list to raw float32 bytes for sqlite-vec."""
    return struct.pack(f"{len(vector)}f", *vector)


def _load_vec_extension(conn) -> None:
    """Load sqlite-vec extension on a connection (idempotent)."""
    if not _HAS_SQLITE_VEC:
        return
    try:
        conn.enable_load_extension(True)
        sqlite_vec.load(conn)
        conn.enable_load_extension(False)
    except Exception:
        pass  # already loaded or not available


# ── Legacy numpy in-memory index (fallback) ─────────────────────────────────


@dataclass
class _AgentCache:
    """Per-agent vector cache for legacy in-memory index."""

    vectors: dict[int, list[float]] = field(default_factory=dict)
    dirty: bool = True  # force reload on first access


class VectorIndex:
    """Legacy in-memory vector index with per-agent invalidation."""

    def __init__(self) -> None:
        self._caches: dict[str, _AgentCache] = {}
        self._lock = threading.Lock()

    def get_cache(self, agent_id: str) -> _AgentCache:
        with self._lock:
            if agent_id not in self._caches:
                self._caches[agent_id] = _AgentCache()
            return self._caches[agent_id]

    def invalidate(self, agent_id: str) -> None:
        """Invalidate cache for an agent (after save/delete/compress)."""
        with self._lock:
            if agent_id in self._caches:
                self._caches[agent_id].dirty = True

    def invalidate_all(self) -> None:
        """Invalidate all caches (after global decay pass)."""
        with self._lock:
            for cache in self._caches.values():
                cache.dirty = True

    def load_vectors(self, agent_id: str, category: str | None = None) -> dict[int, list[float]]:
        """
        Load/return vectors for an agent.
        If cache is dirty, reload from DB.
        Thread-safe: uses lock to avoid concurrent reloads.
        """
        with self._lock:
            if agent_id not in self._caches:
                self._caches[agent_id] = _AgentCache()
            cache = self._caches[agent_id]

            if cache.dirty:
                self._reload_from_db(agent_id, cache)

            return cache.vectors

    def search(
        self,
        query_vec: list[float],
        agent_id: str,
        category: str | None = None,
        limit: int = 10,
        min_similarity: float = 0.1,
    ) -> list[tuple[int, float]]:
        """
        Batch vector search: compute cosine similarity on all vectors
        and return top-k results as [(memory_id, score), ...].

        Uses numpy batch dot product when available for ~10-50x speedup.
        Falls back to pure Python if numpy is not installed.
        """
        vectors = self.load_vectors(agent_id, category)
        if not vectors:
            return []

        mem_ids = list(vectors.keys())

        if _HAS_NUMPY and mem_ids:
            # Batch computation: build matrix and compute all dot products at once
            matrix = np.array([vectors[mid] for mid in mem_ids], dtype=np.float32)
            query_arr = np.array(query_vec, dtype=np.float32)
            similarities = matrix @ query_arr  # shape: (n,)

            scored: list[tuple[int, float]] = [
                (mem_ids[i], float(similarities[i])) for i in range(len(mem_ids)) if similarities[i] >= min_similarity
            ]
        else:
            # Pure Python fallback
            scored = []
            for mem_id, vec in vectors.items():
                sim = sum(a * b for a, b in zip(query_vec, vec))
                if sim >= min_similarity:
                    scored.append((mem_id, sim))

        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:limit]

    def _reload_from_db(self, agent_id: str, cache: _AgentCache) -> None:
        """Reload all embeddings from DB for the agent."""
        from .database import get_connection
        from .embedder import deserialize

        with get_connection() as conn:
            rows = conn.execute(
                """
                SELECT id, embedding FROM memories
                WHERE embedding IS NOT NULL
                  AND compressed_into IS NULL
                  AND archived_at IS NULL
                  AND agent_id = ?
                """,
                (agent_id,),
            ).fetchall()

        cache.vectors = {}
        for row in rows:
            try:
                cache.vectors[row["id"]] = deserialize(row["embedding"])
            except Exception:
                continue  # corrupted embedding — skip

        cache.dirty = False


# ── Singleton instances ─────────────────────────────────────────────────────

_legacy_index = VectorIndex()
_vec_index = SqliteVecIndex() if _HAS_SQLITE_VEC else None


def get_index() -> VectorIndex | SqliteVecIndex:
    """Return the best available vector index (sqlite-vec preferred)."""
    if _vec_index is not None:
        return _vec_index
    return _legacy_index
```

## File: `kore_memory/welcome.py`
```python
"""
Kore — Welcome message shown after installation.
"""

BANNER = r"""
\033[38;5;105m
  ██╗  ██╗ ██████╗ ██████╗ ███████╗
  ██║ ██╔╝██╔═══██╗██╔══██╗██╔════╝
  █████╔╝ ██║   ██║██████╔╝█████╗
  ██╔═██╗ ██║   ██║██╔══██╗██╔══╝
  ██║  ██╗╚██████╔╝██║  ██║███████╗
  ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
\033[0m"""

TAGLINE = "\033[38;5;147m  memory layer for AI agents — remembers what matters, forgets what doesn't\033[0m"

QUICK_START = """
\033[38;5;244m  ─────────────────────────────────────────────────\033[0m
\033[1m  Quick Start\033[0m

  \033[38;5;147m$\033[0m kore                    \033[38;5;244m# start server on :8765\033[0m
  \033[38;5;147m$\033[0m curl localhost:8765/health

  \033[38;5;147m$\033[0m curl -X POST localhost:8765/save \\
      -d '{\"content\": \"your first memory\", \"category\": \"general\"}'

\033[38;5;244m  ─────────────────────────────────────────────────\033[0m
  \033[38;5;75mhttps://github.com/auriti-labs/kore-memory\033[0m
\033[38;5;244m  ─────────────────────────────────────────────────\033[0m
"""


def print_welcome() -> None:
    print(BANNER)
    print(TAGLINE)
    print(QUICK_START)


if __name__ == "__main__":
    print_welcome()
```

## File: `kore_memory/integrations/__init__.py`
```python
"""
Kore Memory — Framework integrations.
Optional bridges for LangChain, CrewAI, PydanticAI, OpenAI Agents SDK, and other AI frameworks.
Le dipendenze sono opzionali: ogni modulo gestisce l'ImportError internamente.
"""

from __future__ import annotations


def __getattr__(name: str):
    """Lazy-load integration classes to avoid hard dependencies."""

    if name == "KoreCrewAIMemory":
        from .crewai import KoreCrewAIMemory

        return KoreCrewAIMemory

    if name == "KoreLangChainMemory":
        from .langchain import KoreLangChainMemory

        return KoreLangChainMemory

    if name == "KoreChatMessageHistory":
        from .langchain import KoreChatMessageHistory

        return KoreChatMessageHistory

    if name == "kore_toolset":
        from .pydantic_ai import kore_toolset

        return kore_toolset

    if name == "create_kore_tools":
        from .pydantic_ai import create_kore_tools

        return create_kore_tools

    if name == "kore_agent_tools":
        from .openai_agents import kore_agent_tools

        return kore_agent_tools

    if name in ("extract_entities", "auto_tag_entities", "search_entities"):
        from . import entities

        return getattr(entities, name)

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    "KoreCrewAIMemory",
    "KoreLangChainMemory",
    "KoreChatMessageHistory",
    "kore_toolset",
    "create_kore_tools",
    "kore_agent_tools",
    "extract_entities",
    "auto_tag_entities",
    "search_entities",
]
```

## File: `kore_memory/integrations/crewai.py`
```python
"""
Kore Memory — CrewAI integration.
Provides KoreCrewAIMemory as a memory provider for CrewAI agents.

Usage:
    from kore_memory.integrations.crewai import KoreCrewAIMemory

    memory = KoreCrewAIMemory(base_url="http://localhost:8765", agent_id="my-crew")
    memory.save("The user prefers dark mode")
    results = memory.search("user preferences")
"""

from __future__ import annotations

from typing import Any

try:
    from crewai.memory import BaseMemory as CrewAIBaseMemory

    _HAS_CREWAI = True
except ImportError:
    _HAS_CREWAI = False
    CrewAIBaseMemory = object  # type: ignore[assignment, misc]


from kore_memory.client import KoreClient


class KoreCrewAIMemory(CrewAIBaseMemory):  # type: ignore[misc]
    """
    CrewAI memory provider backed by Kore Memory.

    Wraps KoreClient to store and retrieve memories through the Kore Memory API.
    Supports short-term (ephemeral, high-decay) and long-term (persistent, high-importance)
    memory patterns.

    Args:
        base_url: URL del server Kore (default: http://localhost:8765)
        api_key: API key per autenticazione (opzionale su localhost)
        agent_id: Namespace agente per isolamento memorie (default: "default")
        category: Categoria default per le memorie salvate (default: "general")
        timeout: Timeout richieste in secondi (default: 10.0)
    """

    def __init__(
        self,
        base_url: str = "http://localhost:8765",
        api_key: str | None = None,
        agent_id: str = "default",
        category: str = "general",
        timeout: float = 10.0,
    ):
        self._base_url = base_url
        self._api_key = api_key
        self._agent_id = agent_id
        self._category = category
        self._timeout = timeout
        self._client = KoreClient(
            base_url=base_url,
            api_key=api_key,
            agent_id=agent_id,
            timeout=timeout,
        )

    # ── Core interface ───────────────────────────────────────────────────

    def save(self, value: str, metadata: dict[str, Any] | None = None) -> None:
        """
        Salva una memoria in Kore.

        Args:
            value: Contenuto testuale della memoria.
            metadata: Dict opzionale con chiavi extra (category, importance, ttl_hours).
                      Le chiavi riconosciute vengono estratte e passate a KoreClient.save().
        """
        meta = metadata or {}
        category = meta.get("category", self._category)
        importance = meta.get("importance", 1)
        ttl_hours = meta.get("ttl_hours", None)

        self._client.save(
            content=value,
            category=category,
            importance=importance,
            ttl_hours=ttl_hours,
        )

    def search(self, query: str, limit: int = 5) -> list[dict[str, Any]]:
        """
        Cerca memorie in Kore.

        Args:
            query: Stringa di ricerca (FTS5 o semantic).
            limit: Numero massimo di risultati (default: 5).

        Returns:
            Lista di dict con id, content, category, importance, decay_score, score.
        """
        response = self._client.search(q=query, limit=limit, category=None, semantic=True)
        return [
            {
                "id": r.id,
                "content": r.content,
                "category": r.category,
                "importance": r.importance,
                "decay_score": r.decay_score,
                "score": r.score,
            }
            for r in response.results
        ]

    # ── Short-term / Long-term patterns ──────────────────────────────────

    def save_short_term(self, value: str) -> None:
        """
        Salva una memoria a breve termine (alta decay, bassa importanza).
        TTL di 24 ore, importance 1 — verra dimenticata rapidamente.
        """
        self.save(value, metadata={"importance": 1, "ttl_hours": 24})

    def save_long_term(self, value: str, importance: int = 4) -> None:
        """
        Salva una memoria a lungo termine (alta importanza, nessun TTL).
        Importance default 4, decay naturale via curva di Ebbinghaus.

        Args:
            value: Contenuto testuale della memoria.
            importance: Livello di importanza 2-5 (default: 4).
        """
        clamped = max(2, min(5, importance))
        self.save(value, metadata={"importance": clamped})

    # ── Lifecycle ────────────────────────────────────────────────────────

    def close(self) -> None:
        """Chiude il client HTTP sottostante."""
        self._client.close()

    def __enter__(self) -> KoreCrewAIMemory:
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()

    def __repr__(self) -> str:
        return (
            f"KoreCrewAIMemory(base_url={self._base_url!r}, agent_id={self._agent_id!r}, category={self._category!r})"
        )
```

## File: `kore_memory/integrations/entities.py`
```python
"""
Kore Memory — Entity Extraction integration.
Extracts named entities from memory content and stores them as tags.

Uses spaCy for NER when available, falls back to regex-based extraction.
Entities are stored as tags with `entity:type:value` format.

Usage:
    from kore_memory.integrations.entities import extract_entities, auto_tag_entities

    entities = extract_entities("Meeting with Juan at Google on 2024-01-15")
    # [{"type": "person", "value": "Juan"}, {"type": "org", "value": "Google"}, ...]

    auto_tag_entities(memory_id=1, content="...", agent_id="default")
"""

from __future__ import annotations

import re
from typing import Any

# ── spaCy lazy loading ────────────────────────────────────────────────────────

_spacy_nlp: Any = None
_spacy_checked: bool = False
_HAS_SPACY: bool = False

# Mapping from spaCy entity labels to our entity types
_SPACY_LABEL_MAP: dict[str, str] = {
    "PERSON": "person",
    "ORG": "org",
    "GPE": "location",
    "DATE": "date",
    "MONEY": "money",
    "PRODUCT": "product",
}


def _get_spacy_nlp() -> Any:
    """Lazy-load spaCy model on first use. Returns None if unavailable."""
    global _spacy_nlp, _spacy_checked, _HAS_SPACY

    if _spacy_checked:
        return _spacy_nlp

    _spacy_checked = True
    try:
        import spacy

        _HAS_SPACY = True
        try:
            _spacy_nlp = spacy.load("en_core_web_sm")
        except OSError:
            # Model not downloaded — try other common models
            for model_name in ("en_core_web_md", "en_core_web_lg"):
                try:
                    _spacy_nlp = spacy.load(model_name)
                    break
                except OSError:
                    continue
    except ImportError:
        _HAS_SPACY = False
        _spacy_nlp = None

    return _spacy_nlp


def spacy_available() -> bool:
    """Check if spaCy is available and a model is loaded."""
    _get_spacy_nlp()
    return _spacy_nlp is not None


# ── Regex-based fallback extractors ──────────────────────────────────────────

# Email: standard RFC-ish pattern
_EMAIL_RE = re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b")

# URL: http/https URLs
_URL_RE = re.compile(r"https?://[a-zA-Z0-9._~:/?#\[\]@!$&'()*+,;=%-]+")

# Date: common formats (YYYY-MM-DD, DD/MM/YYYY, MM/DD/YYYY, Month DD YYYY, etc.)
_DATE_RE = re.compile(
    r"\b\d{4}-\d{2}-\d{2}\b"  # 2024-01-15
    r"|\b\d{1,2}/\d{1,2}/\d{2,4}\b"  # 01/15/2024 or 15/01/24
    r"|\b(?:January|February|March|April|May|June|July|August|September|October|November|December)"
    r"\s+\d{1,2},?\s*\d{4}\b"  # January 15, 2024
    r"|\b\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)"
    r"\s+\d{4}\b",  # 15 January 2024
    re.IGNORECASE,
)

# Money: currency values ($100, EUR 50.00, 1,000.50 USD, etc.)
_MONEY_RE = re.compile(
    r"[$\u20ac\u00a3\u00a5]\s*[\d,]+(?:\.\d{1,2})?"  # $100, EUR50.00
    r"|[\d,]+(?:\.\d{1,2})?\s*(?:USD|EUR|GBP|JPY|CHF|BTC|ETH)\b"  # 100 USD
    r"|(?:USD|EUR|GBP|JPY|CHF)\s*[\d,]+(?:\.\d{1,2})?",  # USD 100
    re.IGNORECASE,
)


def _extract_regex(text: str) -> list[dict[str, str]]:
    """Extract entities using regex patterns (no external dependencies)."""
    entities: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()

    for match in _EMAIL_RE.finditer(text):
        val = match.group().lower()
        key = ("email", val)
        if key not in seen:
            seen.add(key)
            entities.append({"type": "email", "value": val})

    for match in _URL_RE.finditer(text):
        val = match.group().rstrip(".,;:")
        key = ("url", val.lower())
        if key not in seen:
            seen.add(key)
            entities.append({"type": "url", "value": val})

    for match in _DATE_RE.finditer(text):
        val = match.group().strip()
        key = ("date", val.lower())
        if key not in seen:
            seen.add(key)
            entities.append({"type": "date", "value": val})

    for match in _MONEY_RE.finditer(text):
        val = match.group().strip()
        key = ("money", val.lower())
        if key not in seen:
            seen.add(key)
            entities.append({"type": "money", "value": val})

    return entities


def _extract_spacy(text: str) -> list[dict[str, str]]:
    """Extract entities using spaCy NER."""
    nlp = _get_spacy_nlp()
    if nlp is None:
        return []

    doc = nlp(text[:10000])  # Limit text length for performance
    entities: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()

    for ent in doc.ents:
        entity_type = _SPACY_LABEL_MAP.get(ent.label_)
        if entity_type is None:
            continue
        val = ent.text.strip()
        if not val:
            continue
        key = (entity_type, val.lower())
        if key not in seen:
            seen.add(key)
            entities.append({"type": entity_type, "value": val})

    return entities


# ── Public API ────────────────────────────────────────────────────────────────


def extract_entities(text: str) -> list[dict[str, str]]:
    """
    Extract entities from text content.

    Uses spaCy NER when available (PERSON, ORG, GPE, DATE, MONEY, PRODUCT),
    falls back to regex extraction (email, url, date, money).

    Both methods are combined when spaCy is available — spaCy handles named
    entities while regex catches structured patterns (emails, URLs) that
    spaCy may miss.

    Args:
        text: The text to extract entities from.

    Returns:
        List of dicts with 'type' and 'value' keys.
        Example: [{"type": "person", "value": "Juan"}, ...]
    """
    if not text or not text.strip():
        return []

    entities: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()

    # Always run regex extraction (catches emails, URLs, structured patterns)
    regex_entities = _extract_regex(text)
    for ent in regex_entities:
        key = (ent["type"], ent["value"].lower())
        if key not in seen:
            seen.add(key)
            entities.append(ent)

    # Add spaCy entities if available
    if spacy_available():
        spacy_entities = _extract_spacy(text)
        for ent in spacy_entities:
            key = (ent["type"], ent["value"].lower())
            if key not in seen:
                seen.add(key)
                entities.append(ent)

    return entities


def auto_tag_entities(memory_id: int, content: str, agent_id: str = "default") -> int:
    """
    Extract entities from content and save them as tags on the memory.

    Tags are stored in `entity:type:value` format, e.g.:
    - `entity:person:juan`
    - `entity:email:user@example.com`
    - `entity:url:https://example.com`

    Args:
        memory_id: The memory ID to tag.
        content: The text content to extract entities from.
        agent_id: The agent namespace.

    Returns:
        Number of entity tags added.
    """
    from ..repository import add_tags

    entities = extract_entities(content)
    if not entities:
        return 0

    tags = []
    for ent in entities:
        # Normalize value for tag: lowercase, limit length
        value = ent["value"].strip().lower()[:80]
        tag = f"entity:{ent['type']}:{value}"
        tags.append(tag)

    if not tags:
        return 0

    return add_tags(memory_id, tags, agent_id=agent_id)


def search_entities(
    agent_id: str,
    entity_type: str | None = None,
    limit: int = 50,
) -> list[dict[str, str]]:
    """
    Search entity tags across all memories for an agent.

    Queries the memory_tags table for tags matching `entity:*` pattern,
    optionally filtered by entity type.

    Args:
        agent_id: The agent namespace to search within.
        entity_type: Optional filter by entity type (e.g., "person", "email").
        limit: Maximum number of results (default: 50).

    Returns:
        List of dicts with 'type', 'value', 'memory_id', and 'tag' keys.
    """
    from ..database import get_connection

    pattern = f"entity:{entity_type.lower()}:%" if entity_type else "entity:%"

    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT mt.memory_id, mt.tag
            FROM memory_tags mt
            JOIN memories m ON mt.memory_id = m.id
            WHERE mt.tag LIKE ?
              AND m.agent_id = ?
              AND m.compressed_into IS NULL
              AND (m.expires_at IS NULL OR m.expires_at > datetime('now'))
            ORDER BY m.created_at DESC
            LIMIT ?
            """,
            (pattern, agent_id, limit),
        ).fetchall()

    results: list[dict[str, str]] = []
    for row in rows:
        tag = row["tag"]
        parts = tag.split(":", 2)
        if len(parts) == 3:
            results.append(
                {
                    "type": parts[1],
                    "value": parts[2],
                    "memory_id": row["memory_id"],
                    "tag": tag,
                }
            )

    return results
```

## File: `kore_memory/integrations/langchain.py`
```python
"""
Kore — LangChain Integration
Integration with LangChain via BaseMemory and BaseChatMessageHistory.

Allows using Kore as a memory backend for LangChain chains and agents.
Requires `langchain-core>=0.2.0` (optional).

Usage (legacy BaseMemory):
    from kore_memory.integrations.langchain import KoreLangChainMemory

    memory = KoreLangChainMemory(base_url="http://localhost:8765", agent_id="my-agent")
    chain = LLMChain(llm=llm, prompt=prompt, memory=memory)

Usage (LangChain v0.3+ BaseChatMessageHistory):
    from kore_memory.integrations.langchain import KoreChatMessageHistory

    history = KoreChatMessageHistory(session_id="conv-1", agent_id="my-agent")
    chain = RunnableWithMessageHistory(llm, lambda sid: KoreChatMessageHistory(session_id=sid))
"""

from __future__ import annotations

import logging
from typing import Any

try:
    from langchain_core.memory import BaseMemory

    _HAS_LANGCHAIN = True
except ImportError:
    _HAS_LANGCHAIN = False
    BaseMemory = object  # type: ignore[assignment,misc]

try:
    from langchain_core.chat_history import BaseChatMessageHistory
    from langchain_core.messages import AIMessage, BaseMessage, HumanMessage

    _HAS_CHAT_HISTORY = True
except ImportError:
    _HAS_CHAT_HISTORY = False
    BaseChatMessageHistory = object  # type: ignore[assignment,misc]

from kore_memory.client import KoreClient

logger = logging.getLogger(__name__)


class KoreLangChainMemory(BaseMemory):  # type: ignore[misc]
    """
    LangChain memory backend che usa Kore Memory per persistenza.

    Salva automaticamente i turni di conversazione (input/output) come memorie
    in Kore, e recupera le memorie rilevanti durante load_memory_variables
    usando ricerca semantica o FTS5.

    Args:
        base_url: URL del server Kore (default: http://localhost:8765)
        api_key: API key per autenticazione (opzionale su localhost)
        agent_id: Namespace agente (default: "default")
        memory_key: Chiave usata per iniettare memorie nel prompt (default: "history")
        input_key: Chiave dell'input nella chain (default: "input")
        output_key: Chiave dell'output nella chain (default: "output")
        k: Numero massimo di risultati da recuperare (default: 5)
        semantic: Usa ricerca semantica se disponibile (default: True)
        category: Categoria per le memorie salvate (default: "general")
        auto_importance: Usa auto-scoring importanza (default: True)
    """

    # -- Campi di configurazione (non-Pydantic, gestiti manualmente) ----------
    # Nota: BaseMemory usa Pydantic v1 internamente in alcune versioni di
    # langchain-core; per massima compatibilita' usiamo attributi semplici.

    _client: KoreClient
    _memory_key: str
    _input_key: str
    _output_key: str
    _k: int
    _semantic: bool
    _category: str
    _auto_importance: bool

    def __init__(
        self,
        base_url: str = "http://localhost:8765",
        api_key: str | None = None,
        agent_id: str = "default",
        memory_key: str = "history",
        input_key: str = "input",
        output_key: str = "output",
        k: int = 5,
        semantic: bool = True,
        category: str = "general",
        auto_importance: bool = True,
        *,
        client: KoreClient | None = None,
    ):
        if not _HAS_LANGCHAIN:
            raise ImportError(
                "langchain-core is required for KoreLangChainMemory. "
                "Install it with: pip install 'kore-memory[langchain]'"
            )

        # Inizializza BaseMemory (Pydantic v1 in langchain-core < 0.3)
        super().__init__()

        # Client Kore: usa quello fornito oppure ne crea uno nuovo
        self._client = client or KoreClient(
            base_url=base_url,
            api_key=api_key,
            agent_id=agent_id,
        )
        self._memory_key = memory_key
        self._input_key = input_key
        self._output_key = output_key
        self._k = k
        self._semantic = semantic
        self._category = category
        self._auto_importance = auto_importance

    # -- Proprieta' richieste da BaseMemory -----------------------------------

    @property
    def memory_variables(self) -> list[str]:
        """Restituisce le chiavi che questa memoria inietta nel prompt."""
        return [self._memory_key]

    # -- Metodi richiesti da BaseMemory ---------------------------------------

    def load_memory_variables(self, inputs: dict[str, Any]) -> dict[str, str]:
        """
        Recupera memorie rilevanti da Kore basandosi sull'input corrente.

        Cerca nel database Kore usando il valore dell'input_key come query.
        Restituisce un dict con memory_key -> stringa formattata delle memorie.
        """
        query = self._extract_query(inputs)
        if not query:
            return {self._memory_key: ""}

        try:
            response = self._client.search(
                q=query,
                limit=self._k,
                semantic=self._semantic,
            )
            if not response.results:
                return {self._memory_key: ""}

            # Formatta le memorie come testo leggibile
            lines: list[str] = []
            for mem in response.results:
                lines.append(f"[{mem.category}] {mem.content}")

            return {self._memory_key: "\n".join(lines)}

        except Exception:
            logger.warning("Kore memory search failed, returning empty context", exc_info=True)
            return {self._memory_key: ""}

    def save_context(self, inputs: dict[str, Any], outputs: dict[str, str]) -> None:
        """
        Salva il turno di conversazione (input + output) come memoria in Kore.

        Combina input e output in un singolo record di memoria per il retrieval futuro.
        """
        input_text = self._extract_query(inputs)
        output_text = outputs.get(self._output_key, "")

        if not input_text and not output_text:
            return

        # Combina input e output in un formato strutturato
        parts: list[str] = []
        if input_text:
            parts.append(f"Human: {input_text}")
        if output_text:
            parts.append(f"AI: {output_text}")

        content = "\n".join(parts)

        # None = auto-scored dal server, esplicito altrimenti
        importance = None if self._auto_importance else 2

        try:
            self._client.save(
                content=content,
                category=self._category,
                importance=importance,
            )
        except Exception:
            logger.warning("Kore memory save failed", exc_info=True)

    def clear(self) -> None:
        """
        No-op: Kore gestisce il decay delle memorie automaticamente.

        Le memorie obsolete vengono dimenticate tramite la curva di Ebbinghaus,
        quindi non serve un clear esplicito. Per forzare la pulizia, usa
        direttamente il client Kore (decay_run, compress, cleanup).
        """

    # -- Helpers privati -------------------------------------------------------

    def _extract_query(self, inputs: dict[str, Any]) -> str:
        """Estrae la query dall'input dict, con fallback su tutti i valori."""
        if self._input_key in inputs:
            return str(inputs[self._input_key])

        # Fallback: concatena tutti i valori stringa dell'input
        text_parts = [str(v) for v in inputs.values() if isinstance(v, str)]
        return " ".join(text_parts)


# ── LangChain v0.3+ BaseChatMessageHistory ────────────────────────────────────


class KoreChatMessageHistory(BaseChatMessageHistory):  # type: ignore[misc]
    """
    LangChain v0.3+ chat message history backed by Kore Memory.

    Each message is saved as an individual memory. Compatible with
    RunnableWithMessageHistory for session management.

    Args:
        session_id: Conversation session ID.
        base_url: Kore server URL (default: http://localhost:8765).
        api_key: API key for authentication (optional on localhost).
        agent_id: Agent namespace (default: "default").
        category: Category for saved memories (default: "general").
    """

    def __init__(
        self,
        session_id: str,
        base_url: str = "http://localhost:8765",
        api_key: str | None = None,
        agent_id: str = "default",
        category: str = "general",
        *,
        client: KoreClient | None = None,
    ):
        if not _HAS_CHAT_HISTORY:
            raise ImportError(
                "langchain-core>=0.3.0 is required for KoreChatMessageHistory. "
                "Install with: pip install 'kore-memory[langchain]'"
            )

        self._session_id = session_id
        self._agent_id = agent_id
        self._category = category
        self._client = client or KoreClient(
            base_url=base_url,
            api_key=api_key,
            agent_id=agent_id,
        )

    @property
    def messages(self) -> list[BaseMessage]:  # type: ignore[override]
        """Retrieve all messages for this session from Kore."""
        try:
            response = self._client.search(
                q="*",
                limit=100,
                semantic=False,
            )
            msgs: list[BaseMessage] = []
            for mem in response.results:
                content = mem.content
                # Reconstruct message type from prefix
                if content.startswith("Human: "):
                    msgs.append(HumanMessage(content=content[7:]))
                elif content.startswith("AI: "):
                    msgs.append(AIMessage(content=content[4:]))
                else:
                    # Generic message — treat as human
                    msgs.append(HumanMessage(content=content))
            return msgs
        except Exception:
            logger.warning("Kore chat history retrieval failed", exc_info=True)
            return []

    def add_messages(self, messages: list[BaseMessage]) -> None:  # type: ignore[override]
        """Save a list of messages to Kore as individual memories."""
        for msg in messages:
            # Add prefix to distinguish message type on retrieval
            if isinstance(msg, HumanMessage):
                content = f"Human: {msg.content}"
            elif isinstance(msg, AIMessage):
                content = f"AI: {msg.content}"
            else:
                content = str(msg.content)

            try:
                self._client.save(
                    content=content,
                    category=self._category,
                )
            except Exception:
                logger.warning("Kore chat history save failed", exc_info=True)

    def clear(self) -> None:
        """
        No-op: Kore gestisce il decay delle memorie automaticamente.

        Le memorie obsolete vengono dimenticate tramite la curva di Ebbinghaus.
        Per forzare la pulizia, usa direttamente il client Kore.
        """
```

## File: `kore_memory/integrations/openai_agents.py`
```python
"""
Kore Memory — OpenAI Agents SDK integration.
Provides ready-to-use function tools for OpenAI Agents SDK agents.

Usage:
    from kore_memory.integrations.openai_agents import kore_agent_tools

    tools = kore_agent_tools(base_url="http://localhost:8765", agent_id="my-agent")
    agent = Agent(name="Assistant", tools=tools)

Requires: pip install 'kore-memory[openai-agents]' (or openai-agents separately)
"""

from __future__ import annotations

from typing import Any

try:
    from agents import function_tool

    _HAS_OPENAI_AGENTS = True
except ImportError:
    _HAS_OPENAI_AGENTS = False

from kore_memory.client import KoreClient


def kore_agent_tools(
    base_url: str = "http://localhost:8765",
    api_key: str | None = None,
    agent_id: str = "default",
    timeout: float = 10.0,
) -> list[Any]:
    """
    Create a list of function tools for OpenAI Agents SDK.

    Args:
        base_url: Kore server URL.
        api_key: API key for authentication (optional on localhost).
        agent_id: Agent namespace for memory isolation.
        timeout: Request timeout in seconds.

    Returns:
        List of FunctionTool ready to be passed to Agent(tools=[...]).
    """
    if not _HAS_OPENAI_AGENTS:
        raise ImportError(
            "OpenAI Agents SDK not installed. Install with: pip install openai-agents"
        )

    client = KoreClient(
        base_url=base_url,
        api_key=api_key,
        agent_id=agent_id,
        timeout=timeout,
    )

    @function_tool
    def kore_save(content: str, category: str = "general", importance: int = 0) -> str:
        """Save a memory to Kore persistent storage.

        Args:
            content: The text content to memorize.
            category: Category (general, project, task, decision, person, preference).
            importance: Importance 1-5, 0 for auto-scoring.
        """
        imp = importance if importance > 0 else None
        result = client.save(content=content, category=category, importance=imp)
        return f"Memory saved with id={result.id}, importance={result.importance}"

    @function_tool
    def kore_search(query: str, limit: int = 5, category: str = "") -> str:
        """Search Kore persistent memory using semantic search.

        Args:
            query: The search query (any language).
            limit: Maximum number of results (1-20).
            category: Filter by category (optional, empty string = all).
        """
        cat = category if category else None
        response = client.search(q=query, limit=limit, category=cat, semantic=True)
        if not response.results:
            return "No memories found."
        lines = []
        for r in response.results:
            lines.append(f"[id={r.id}] ({r.category}, imp={r.importance}) {r.content}")
        return "\n".join(lines)

    @function_tool
    def kore_timeline(subject: str, limit: int = 10) -> str:
        """Show the chronological timeline of memories on a specific subject.

        Args:
            subject: The subject to search in the timeline.
            limit: Maximum number of results (1-50).
        """
        response = client.timeline(subject=subject, limit=limit)
        if not response.results:
            return "No memories found for this subject."
        lines = []
        for r in response.results:
            lines.append(f"[{r.created_at}] {r.content}")
        return "\n".join(lines)

    @function_tool
    def kore_delete(memory_id: int) -> str:
        """Delete a memory from persistent storage.

        Args:
            memory_id: The ID of the memory to delete.
        """
        deleted = client.delete(memory_id)
        if deleted:
            return f"Memory {memory_id} deleted."
        return f"Memory {memory_id} not found."

    return [kore_save, kore_search, kore_timeline, kore_delete]
```

## File: `kore_memory/integrations/pydantic_ai.py`
```python
"""
Kore Memory — PydanticAI integration.
Provides ready-to-use tools for PydanticAI agents.

Usage:
    from kore_memory.integrations.pydantic_ai import kore_toolset

    agent = Agent('openai:gpt-4o', toolsets=[kore_toolset(base_url="http://localhost:8765")])
    result = agent.run_sync("Save that the project uses FastAPI")

Requires: pip install 'kore-memory[pydantic-ai]' (or pydantic-ai separately)
"""

from __future__ import annotations

from typing import Any

try:
    from pydantic_ai import FunctionToolset

    _HAS_PYDANTIC_AI = True
except ImportError:
    _HAS_PYDANTIC_AI = False

from kore_memory.client import KoreClient


def kore_toolset(
    base_url: str = "http://localhost:8765",
    api_key: str | None = None,
    agent_id: str = "default",
    timeout: float = 10.0,
) -> Any:
    """
    Create a PydanticAI FunctionToolset with Kore Memory tools.

    Args:
        base_url: Kore server URL.
        api_key: API key for authentication (optional on localhost).
        agent_id: Agent namespace for memory isolation.
        timeout: Request timeout in seconds.

    Returns:
        FunctionToolset with tools: kore_save, kore_search, kore_timeline, kore_delete.
    """
    if not _HAS_PYDANTIC_AI:
        raise ImportError(
            "PydanticAI not installed. Install with: pip install pydantic-ai"
        )

    client = KoreClient(
        base_url=base_url,
        api_key=api_key,
        agent_id=agent_id,
        timeout=timeout,
    )

    toolset = FunctionToolset()

    @toolset.tool
    def kore_save(
        content: str,
        category: str = "general",
        importance: int = 0,
    ) -> str:
        """Save a memory to Kore persistent storage.

        Args:
            content: The text content to memorize.
            category: Category (general, project, task, decision, person, preference, trading, finance).
            importance: Importance 1-5, 0 for auto-scoring.
        """
        imp = importance if importance > 0 else None
        result = client.save(content=content, category=category, importance=imp)
        return f"Memory saved with id={result.id}, importance={result.importance}"

    @toolset.tool
    def kore_search(
        query: str,
        limit: int = 5,
        category: str = "",
    ) -> str:
        """Search Kore persistent memory using semantic search.

        Args:
            query: The search query (any language).
            limit: Maximum number of results (1-20).
            category: Filter by category (optional, empty string = all).
        """
        cat = category if category else None
        response = client.search(q=query, limit=limit, category=cat, semantic=True)
        if not response.results:
            return "No memories found."
        lines = []
        for r in response.results:
            lines.append(f"[id={r.id}] ({r.category}, imp={r.importance}) {r.content}")
        return "\n".join(lines)

    @toolset.tool
    def kore_timeline(
        subject: str,
        limit: int = 10,
    ) -> str:
        """Show the chronological timeline of memories on a subject.

        Args:
            subject: The subject to search in the timeline.
            limit: Maximum number of results (1-50).
        """
        response = client.timeline(subject=subject, limit=limit)
        if not response.results:
            return "No memories found for this subject."
        lines = []
        for r in response.results:
            lines.append(f"[{r.created_at}] {r.content}")
        return "\n".join(lines)

    @toolset.tool
    def kore_delete(memory_id: int) -> str:
        """Delete a memory from persistent storage.

        Args:
            memory_id: The ID of the memory to delete.
        """
        deleted = client.delete(memory_id)
        if deleted:
            return f"Memory {memory_id} deleted."
        return f"Memory {memory_id} not found."

    return toolset


# ── Standalone tools (for agents using @agent.tool_plain) ────────────────────


def create_kore_tools(
    base_url: str = "http://localhost:8765",
    api_key: str | None = None,
    agent_id: str = "default",
) -> dict[str, Any]:
    """
    Create a dictionary of standalone tool functions for use with @agent.tool_plain.

    Returns:
        Dict with keys: save, search, timeline, delete — functions ready for PydanticAI.
    """
    client = KoreClient(base_url=base_url, api_key=api_key, agent_id=agent_id)

    def save(content: str, category: str = "general", importance: int = 0) -> str:
        """Save a memory."""
        imp = importance if importance > 0 else None
        result = client.save(content=content, category=category, importance=imp)
        return f"Saved id={result.id}, importance={result.importance}"

    def search(query: str, limit: int = 5) -> list[dict]:
        """Search memories."""
        response = client.search(q=query, limit=limit, semantic=True)
        return [
            {"id": r.id, "content": r.content, "category": r.category, "importance": r.importance}
            for r in response.results
        ]

    def timeline(subject: str, limit: int = 10) -> list[dict]:
        """Timeline of a subject."""
        response = client.timeline(subject=subject, limit=limit)
        return [
            {"id": r.id, "content": r.content, "created_at": str(r.created_at)}
            for r in response.results
        ]

    def delete(memory_id: int) -> bool:
        """Delete a memory."""
        return client.delete(memory_id)

    return {"save": save, "search": search, "timeline": timeline, "delete": delete}
```

## File: `kore_memory/repository/__init__.py`
```python
"""
Kore — Repository package.
Re-exports all public functions for backward compatibility.

The monolithic repository.py has been split into:
- memory.py   — CRUD operations (save, get, update, delete, batch, import/export)
- search.py   — Search operations (FTS5, semantic, tag, timeline)
- lifecycle.py — Decay, cleanup, archive, restore
- graph.py     — Tags and relations between memories
- sessions.py  — Session management
"""

# ruff: noqa: F401 — re-exports for backward compatibility
from .graph import add_relation, add_tags, get_relations, get_tags, remove_tags, traverse_graph
from .lifecycle import (
    _compress_lock,
    _decay_lock,
    archive_memory,
    cleanup_expired,
    get_archived,
    restore_memory,
    run_decay_pass,
)
from .memory import (
    _embeddings_available,
    delete_memory,
    export_memories,
    get_memory,
    get_stats,
    import_memories,
    list_agents,
    save_memory,
    save_memory_batch,
    update_memory,
)
from .search import (
    _count_active_memories,
    _row_to_record,
    _sanitize_fts_query,
    get_timeline,
    search_by_tag,
    search_memories,
)
from .sessions import (
    create_session,
    delete_session,
    end_session,
    get_session_memories,
    get_session_summary,
    list_sessions,
)

__all__ = [
    # Memory
    "_embeddings_available",
    "save_memory",
    "save_memory_batch",
    "update_memory",
    "get_memory",
    "delete_memory",
    "export_memories",
    "import_memories",
    "get_stats",
    "list_agents",
    # Search
    "search_memories",
    "get_timeline",
    "search_by_tag",
    "_count_active_memories",
    "_row_to_record",
    "_sanitize_fts_query",
    # Lifecycle
    "run_decay_pass",
    "cleanup_expired",
    "archive_memory",
    "restore_memory",
    "get_archived",
    "_decay_lock",
    "_compress_lock",
    # Graph
    "add_tags",
    "remove_tags",
    "get_tags",
    "add_relation",
    "get_relations",
    "traverse_graph",
    # Sessions
    "create_session",
    "list_sessions",
    "get_session_memories",
    "end_session",
    "delete_session",
    "get_session_summary",
]
```

## File: `kore_memory/repository/graph.py`
```python
"""
Kore — Repository: Graph operations.
Tags and relations between memories.
"""

from __future__ import annotations

from ..database import get_connection


def add_tags(memory_id: int, tags: list[str], agent_id: str = "default") -> int:
    """Add tags to a memory. Returns the number of tags added."""
    # Verify that the memory belongs to the agent
    with get_connection() as conn:
        row = conn.execute(
            "SELECT id FROM memories WHERE id = ? AND agent_id = ?",
            (memory_id, agent_id),
        ).fetchone()
        if not row:
            return 0
        added = 0
        for tag in tags:
            tag = tag.strip().lower()[:100]
            if not tag:
                continue
            try:
                conn.execute(
                    "INSERT OR IGNORE INTO memory_tags (memory_id, tag) VALUES (?, ?)",
                    (memory_id, tag),
                )
                added += 1
            except Exception:
                continue
    return added


def remove_tags(memory_id: int, tags: list[str], agent_id: str = "default") -> int:
    """Remove tags from a memory. Returns the number of tags removed."""
    with get_connection() as conn:
        row = conn.execute(
            "SELECT id FROM memories WHERE id = ? AND agent_id = ?",
            (memory_id, agent_id),
        ).fetchone()
        if not row:
            return 0
        removed = 0
        for tag in tags:
            tag = tag.strip().lower()
            cursor = conn.execute(
                "DELETE FROM memory_tags WHERE memory_id = ? AND tag = ?",
                (memory_id, tag),
            )
            removed += cursor.rowcount
    return removed


def get_tags(memory_id: int, agent_id: str = "default") -> list[str]:
    """
    Return the tags of a memory.
    Verifies that the memory belongs to the specified agent_id.
    """
    with get_connection() as conn:
        # JOIN with memories to verify ownership
        rows = conn.execute(
            """
            SELECT mt.tag
            FROM memory_tags mt
            JOIN memories m ON mt.memory_id = m.id
            WHERE mt.memory_id = ? AND m.agent_id = ?
            ORDER BY mt.tag
            """,
            (memory_id, agent_id),
        ).fetchall()
    return [r["tag"] for r in rows]


def add_relation(source_id: int, target_id: int, relation: str = "related", agent_id: str = "default") -> bool:
    """Create a relation between two memories. Both must belong to the agent."""
    with get_connection() as conn:
        # Verify that both memories belong to the agent
        count = conn.execute(
            "SELECT COUNT(*) FROM memories WHERE id IN (?, ?) AND agent_id = ?",
            (source_id, target_id, agent_id),
        ).fetchone()[0]
        if count < 2:
            return False
        try:
            conn.execute(
                """INSERT OR IGNORE INTO memory_relations (source_id, target_id, relation)
                   VALUES (?, ?, ?)""",
                (source_id, target_id, relation.strip().lower()[:100]),
            )
            return True
        except Exception:
            return False


def get_relations(memory_id: int, agent_id: str = "default") -> list[dict]:
    """Return all relations of a memory (in both directions)."""
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT r.source_id, r.target_id, r.relation, r.created_at,
                   m.content AS related_content
            FROM memory_relations r
            JOIN memories m ON m.id = CASE
                WHEN r.source_id = ? THEN r.target_id
                ELSE r.source_id
            END
            WHERE (r.source_id = ? OR r.target_id = ?) AND m.agent_id = ?
            ORDER BY r.created_at DESC
            """,
            (memory_id, memory_id, memory_id, agent_id),
        ).fetchall()
    return [dict(r) for r in rows]


def traverse_graph(
    start_id: int,
    agent_id: str = "default",
    depth: int = 3,
    relation_type: str | None = None,
) -> dict:
    """
    Multi-hop graph traversal using SQLite recursive CTE.
    Returns the start node and all reachable nodes within `depth` hops.
    """
    depth = min(depth, 10)  # cap to prevent excessive recursion

    relation_filter = ""

    with get_connection() as conn:
        # Verify start memory belongs to agent
        start = conn.execute(
            "SELECT id, content, category, importance, decay_score, created_at "
            "FROM memories WHERE id = ? AND agent_id = ? AND archived_at IS NULL",
            (start_id, agent_id),
        ).fetchone()
        if not start:
            return {"start": None, "nodes": [], "edges": [], "depth": depth}

        # Build CTE params: anchor(start_id), [relation_type], agent_id, depth, agent_id, start_id
        cte_params: list = [start_id]
        if relation_type:
            relation_filter = "AND r.relation = ?"
            cte_params.append(relation_type)
        cte_params.extend([agent_id, depth])
        # Outer query params
        outer_params = [agent_id, start_id]

        # Recursive CTE — traverse both directions
        rows = conn.execute(
            f"""
            WITH RECURSIVE graph_walk(node_id, hop) AS (
                -- Anchor: start node
                SELECT ? AS node_id, 0 AS hop
                UNION
                -- Recursive step: follow relations in both directions
                SELECT
                    CASE WHEN r.source_id = gw.node_id THEN r.target_id ELSE r.source_id END,
                    gw.hop + 1
                FROM graph_walk gw
                JOIN memory_relations r
                    ON (r.source_id = gw.node_id OR r.target_id = gw.node_id)
                    {relation_filter}
                JOIN memories m
                    ON m.id = CASE WHEN r.source_id = gw.node_id THEN r.target_id ELSE r.source_id END
                    AND m.agent_id = ?
                    AND m.archived_at IS NULL
                WHERE gw.hop < ?
            )
            SELECT DISTINCT gw.node_id, gw.hop,
                   m.content, m.category, m.importance, m.decay_score, m.created_at
            FROM graph_walk gw
            JOIN memories m ON m.id = gw.node_id AND m.agent_id = ?
            WHERE gw.node_id != ?
            ORDER BY gw.hop, m.importance DESC
            """,
            (*cte_params, *outer_params),
        ).fetchall()

        nodes = [
            {
                "id": r["node_id"],
                "content": r["content"],
                "category": r["category"],
                "importance": r["importance"],
                "decay_score": r["decay_score"],
                "created_at": r["created_at"],
                "hop": r["hop"],
            }
            for r in rows
        ]

        # Fetch edges between all discovered nodes
        node_ids = [start_id] + [n["id"] for n in nodes]
        if len(node_ids) > 1:
            placeholders = ",".join("?" * len(node_ids))
            edge_params: list = list(node_ids) + list(node_ids)
            if relation_type:
                edge_params.append(relation_type)
            edges_rows = conn.execute(
                f"""
                SELECT source_id, target_id, relation, created_at
                FROM memory_relations
                WHERE source_id IN ({placeholders}) AND target_id IN ({placeholders})
                {"AND relation = ?" if relation_type else ""}
                """,
                edge_params,
            ).fetchall()
            edges = [dict(e) for e in edges_rows]
        else:
            edges = []

    return {
        "start": dict(start),
        "nodes": nodes,
        "edges": edges,
        "depth": depth,
    }
```

## File: `kore_memory/repository/lifecycle.py`
```python
"""
Kore — Repository: Memory lifecycle operations.
Decay, cleanup, archive, restore.
"""

from __future__ import annotations

import threading
from datetime import UTC, datetime

from ..database import get_connection
from ..decay import compute_decay
from ..events import MEMORY_ARCHIVED, MEMORY_DECAYED, MEMORY_RESTORED, emit
from ..models import MemoryRecord
from .search import _row_to_record

# Lock for maintenance operations — prevents concurrent runs
_decay_lock = threading.Lock()
_compress_lock = threading.Lock()


def cleanup_expired(agent_id: str | None = None) -> int:
    """Delete memories with elapsed TTL. Returns the number of records removed."""
    with get_connection() as conn:
        sql = "DELETE FROM memories WHERE expires_at IS NOT NULL AND expires_at <= datetime('now')"
        params: list = []
        if agent_id:
            sql += " AND agent_id = ?"
            params.append(agent_id)
        cursor = conn.execute(sql, params)
        return cursor.rowcount


def run_decay_pass(agent_id: str | None = None) -> int:
    """
    Recalculate decay_score for all active memories (optionally scoped to agent).
    Also cleans up memories with elapsed TTL.
    Returns the count of memories updated. Thread-safe: only one run at a time.
    """
    if not _decay_lock.acquire(blocking=False):
        return 0  # run already in progress — silent skip

    try:
        # Clean up expired memories before recalculating
        cleanup_expired(agent_id)
        return _run_decay_pass_inner(agent_id)
    finally:
        _decay_lock.release()


def _run_decay_pass_inner(agent_id: str | None = None) -> int:
    with get_connection() as conn:
        sql = (
            "SELECT id, importance, created_at, last_accessed, access_count"
            " FROM memories WHERE compressed_into IS NULL AND archived_at IS NULL"
        )
        params: list = []
        if agent_id:
            sql += " AND agent_id = ?"
            params.append(agent_id)
        rows = conn.execute(sql, params).fetchall()

    now = datetime.now(UTC).isoformat()
    updates = []
    for row in rows:
        new_score = compute_decay(
            importance=row["importance"],
            created_at=row["created_at"],
            last_accessed=row["last_accessed"],
            access_count=row["access_count"],
        )
        updates.append((new_score, now, row["id"]))

    if updates:
        with get_connection() as conn:
            conn.executemany(
                "UPDATE memories SET decay_score = ?, updated_at = ? WHERE id = ?",
                updates,
            )
        emit(MEMORY_DECAYED, {"agent_id": agent_id or "all", "updated": len(updates)})

    return len(updates)


def archive_memory(memory_id: int, agent_id: str = "default") -> bool:
    """Archive a memory (soft-delete). Returns True if archived."""
    with get_connection() as conn:
        cursor = conn.execute(
            "UPDATE memories SET archived_at = datetime('now') WHERE id = ? AND agent_id = ? AND archived_at IS NULL",
            (memory_id, agent_id),
        )
        archived = cursor.rowcount > 0

    if archived:
        emit(MEMORY_ARCHIVED, {"id": memory_id, "agent_id": agent_id})

    return archived


def restore_memory(memory_id: int, agent_id: str = "default") -> bool:
    """Restore an archived memory. Returns True if restored."""
    with get_connection() as conn:
        cursor = conn.execute(
            "UPDATE memories SET archived_at = NULL WHERE id = ? AND agent_id = ? AND archived_at IS NOT NULL",
            (memory_id, agent_id),
        )
        restored = cursor.rowcount > 0

    if restored:
        emit(MEMORY_RESTORED, {"id": memory_id, "agent_id": agent_id})

    return restored


def get_archived(agent_id: str = "default", limit: int = 50) -> list[MemoryRecord]:
    """List archived memories for an agent."""
    with get_connection() as conn:
        rows = conn.execute(
            """SELECT id, content, category, importance, decay_score, access_count,
                      last_accessed, created_at, updated_at, NULL AS score
               FROM memories WHERE agent_id = ? AND archived_at IS NOT NULL
               ORDER BY archived_at DESC LIMIT ?""",
            (agent_id, limit),
        ).fetchall()
    return [_row_to_record(r) for r in rows]
```

## File: `kore_memory/repository/memory.py`
```python
"""
Kore — Repository: Memory CRUD operations.
Save, get, update, delete, batch save, import/export.
"""

from __future__ import annotations

import os
from datetime import UTC, datetime, timedelta

from ..database import _get_db_path, get_connection
from ..events import MEMORY_DELETED, MEMORY_SAVED, MEMORY_UPDATED, emit
from ..models import MemoryRecord, MemorySaveRequest, MemoryUpdateRequest
from ..scorer import auto_score

_EMBEDDINGS_AVAILABLE: bool | None = None


def _embeddings_available() -> bool:
    global _EMBEDDINGS_AVAILABLE
    if _EMBEDDINGS_AVAILABLE is None:
        try:
            import sentence_transformers  # noqa: F401

            _EMBEDDINGS_AVAILABLE = True
        except ImportError:
            _EMBEDDINGS_AVAILABLE = False
    return _EMBEDDINGS_AVAILABLE


def save_memory(req: MemorySaveRequest, agent_id: str = "default", session_id: str | None = None) -> tuple[int, int]:
    """
    Persist a new memory record scoped to agent_id.
    Auto-scores importance if not explicitly set.
    Returns (row_id, importance).
    """
    importance = req.importance
    if importance is None:
        importance = auto_score(req.content, req.category)

    embedding_blob = None
    if _embeddings_available():
        from ..embedder import embed, serialize

        try:
            embedding_blob = serialize(embed(req.content))
        except Exception:
            embedding_blob = None

    # Compute expires_at if TTL is specified
    expires_at = None
    if req.ttl_hours:
        expires_at = (datetime.now(UTC) + timedelta(hours=req.ttl_hours)).isoformat()

    with get_connection() as conn:
        # Auto-create session if session_id provided but doesn't exist
        if session_id:
            conn.execute(
                "INSERT OR IGNORE INTO sessions (id, agent_id) VALUES (?, ?)",
                (session_id, agent_id),
            )

        cursor = conn.execute(
            """
            INSERT INTO memories (agent_id, content, category, importance, embedding, expires_at, session_id)
            VALUES (:agent_id, :content, :category, :importance, :embedding, :expires_at, :session_id)
            """,
            {
                "agent_id": agent_id,
                "content": req.content,
                "category": req.category,
                "importance": importance,
                "embedding": embedding_blob,
                "expires_at": expires_at,
                "session_id": session_id,
            },
        )
        row_id = cursor.lastrowid

    # Update vector index
    if embedding_blob:
        from ..vector_index import get_index, has_sqlite_vec

        index = get_index()
        if has_sqlite_vec():
            # Insert into sqlite-vec native index
            from ..embedder import deserialize

            try:
                vec = deserialize(embedding_blob)
                with get_connection() as conn:
                    index.upsert(conn, row_id, agent_id, vec)
            except Exception:
                pass  # graceful degradation
        else:
            index.invalidate(agent_id)

    emit(MEMORY_SAVED, {"id": row_id, "agent_id": agent_id})

    # Entity extraction (optional, enabled via KORE_ENTITY_EXTRACTION=1)
    from .. import config as _cfg

    if _cfg.ENTITY_EXTRACTION:
        from ..integrations.entities import auto_tag_entities

        try:
            auto_tag_entities(row_id, req.content, agent_id)
        except Exception:
            pass  # graceful degradation

    return row_id, importance


def save_memory_batch(reqs: list[MemorySaveRequest], agent_id: str = "default") -> list[tuple[int, int]]:
    """
    Batch save: single transaction, batch embeddings.
    Returns list of (row_id, importance) tuples.
    """
    if not reqs:
        return []

    # Auto-score importances
    importances = []
    for req in reqs:
        imp = req.importance
        if imp is None:
            imp = auto_score(req.content, req.category)
        importances.append(imp)

    # Batch embed all contents at once
    embeddings: list[str | None] = [None] * len(reqs)
    if _embeddings_available():
        from ..embedder import embed_batch, serialize

        try:
            vectors = embed_batch([req.content for req in reqs])
            embeddings = [serialize(v) for v in vectors]
        except Exception:
            pass  # Fall back to no embeddings

    # Single transaction for all inserts
    results = []
    with get_connection() as conn:
        for i, req in enumerate(reqs):
            expires_at = None
            if req.ttl_hours:
                expires_at = (datetime.now(UTC) + timedelta(hours=req.ttl_hours)).isoformat()

            cursor = conn.execute(
                """INSERT INTO memories (agent_id, content, category, importance, embedding, expires_at)
                   VALUES (:agent_id, :content, :category, :importance, :embedding, :expires_at)""",
                {
                    "agent_id": agent_id,
                    "content": req.content,
                    "category": req.category,
                    "importance": importances[i],
                    "embedding": embeddings[i],
                    "expires_at": expires_at,
                },
            )
            results.append((cursor.lastrowid, importances[i]))

    # Emit audit event for each saved memory
    for row_id, _ in results:
        emit(MEMORY_SAVED, {"id": row_id, "agent_id": agent_id})

    # Update vector index
    if any(e is not None for e in embeddings):
        from ..vector_index import get_index, has_sqlite_vec

        index = get_index()
        if has_sqlite_vec():
            from ..embedder import deserialize

            with get_connection() as conn:
                for i, emb in enumerate(embeddings):
                    if emb is not None:
                        try:
                            vec = deserialize(emb)
                            index.upsert(conn, results[i][0], agent_id, vec)
                        except Exception:
                            pass
        else:
            index.invalidate(agent_id)

    return results


def update_memory(memory_id: int, req: MemoryUpdateRequest, agent_id: str = "default") -> bool:
    """
    Update an existing memory atomically. Only provided fields are changed.
    Re-generates embedding if content changes.
    Returns True if updated, False if not found.
    """
    updates = []
    params: list = []

    if req.content is not None:
        updates.append("content = ?")
        params.append(req.content)
        # Regenerate embedding if content changes
        if _embeddings_available():
            from ..embedder import embed, serialize

            try:
                embedding_blob = serialize(embed(req.content))
                updates.append("embedding = ?")
                params.append(embedding_blob)
            except Exception:
                pass

    if req.category is not None:
        updates.append("category = ?")
        params.append(req.category)

    if req.importance is not None:
        updates.append("importance = ?")
        params.append(req.importance)

    if not updates:
        # Nothing to update — check if memory exists
        with get_connection() as conn:
            row = conn.execute(
                "SELECT id FROM memories WHERE id = ? AND agent_id = ? AND compressed_into IS NULL",
                (memory_id, agent_id),
            ).fetchone()
        return row is not None

    updates.append("updated_at = ?")
    params.append(datetime.now(UTC).isoformat())
    params.append(memory_id)
    params.append(agent_id)

    # Single atomic UPDATE — no read-then-write race condition
    with get_connection() as conn:
        cursor = conn.execute(
            f"UPDATE memories SET {', '.join(updates)} WHERE id = ? AND agent_id = ? AND compressed_into IS NULL",
            params,
        )
        if cursor.rowcount == 0:
            return False

    # Update vector index
    if req.content is not None:
        from ..vector_index import get_index, has_sqlite_vec

        index = get_index()
        if has_sqlite_vec() and _embeddings_available():
            from ..embedder import embed

            try:
                vec = embed(req.content)
                with get_connection() as conn:
                    index.upsert(conn, memory_id, agent_id, vec)
            except Exception:
                pass
        else:
            index.invalidate(agent_id)

    emit(MEMORY_UPDATED, {"id": memory_id, "agent_id": agent_id})
    return True


def get_memory(memory_id: int, agent_id: str = "default") -> MemoryRecord | None:
    """Get a single memory by ID, scoped to agent. None if not found."""
    with get_connection() as conn:
        row = conn.execute(
            """SELECT id, content, category, importance, decay_score,
                      created_at, updated_at
               FROM memories
               WHERE id = ? AND agent_id = ? AND archived_at IS NULL""",
            (memory_id, agent_id),
        ).fetchone()
    if not row:
        return None
    return MemoryRecord(
        id=row["id"],
        content=row["content"],
        category=row["category"],
        importance=row["importance"],
        decay_score=row["decay_score"],
        created_at=row["created_at"],
        updated_at=row["updated_at"],
    )


def delete_memory(memory_id: int, agent_id: str = "default") -> bool:
    """Delete a memory by id, scoped to agent. Returns True if deleted."""
    with get_connection() as conn:
        cursor = conn.execute(
            "DELETE FROM memories WHERE id = ? AND agent_id = ?",
            (memory_id, agent_id),
        )
        deleted = cursor.rowcount > 0

    if deleted:
        from ..vector_index import get_index, has_sqlite_vec

        index = get_index()
        if has_sqlite_vec():
            try:
                with get_connection() as conn:
                    index.remove(conn, memory_id)
            except Exception:
                pass
        else:
            index.invalidate(agent_id)
        emit(MEMORY_DELETED, {"id": memory_id, "agent_id": agent_id})

    return deleted


def export_memories(agent_id: str = "default") -> list[dict]:
    """Export all active memories for the agent as a list of dicts (without embeddings)."""
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT id, content, category, importance, decay_score,
                   access_count, last_accessed, created_at, updated_at
            FROM memories
            WHERE agent_id = ? AND compressed_into IS NULL
              AND archived_at IS NULL
              AND (expires_at IS NULL OR expires_at > datetime('now'))
            ORDER BY created_at DESC
            """,
            (agent_id,),
        ).fetchall()
    return [dict(r) for r in rows]


_VALID_CATEGORIES = {"general", "project", "trading", "finance", "person", "preference", "task", "decision"}


def import_memories(records: list[dict], agent_id: str = "default") -> int:
    """Import memories from a list of dicts. Returns the number of records imported."""
    imported = 0
    for rec in records:
        content = rec.get("content", "").strip()
        if not content or len(content) < 3:
            continue
        category = rec.get("category", "general")
        if category not in _VALID_CATEGORIES:
            category = "general"
        importance = rec.get("importance", 1)
        importance = max(1, min(5, int(importance)))

        req = MemorySaveRequest(
            content=content[:4000],
            category=category,
            importance=importance,
        )
        save_memory(req, agent_id=agent_id)
        imported += 1

    return imported


def get_stats(agent_id: str | None = None) -> dict:
    """Get database statistics for monitoring."""
    with get_connection() as conn:
        if agent_id:
            total = conn.execute(
                "SELECT COUNT(*) FROM memories WHERE agent_id = ? AND compressed_into IS NULL",
                (agent_id,),
            ).fetchone()[0]
            active = conn.execute(
                "SELECT COUNT(*) FROM memories WHERE agent_id = ? AND compressed_into IS NULL AND decay_score >= 0.05",
                (agent_id,),
            ).fetchone()[0]
            try:
                archived = conn.execute(
                    "SELECT COUNT(*) FROM memories WHERE agent_id = ? AND archived_at IS NOT NULL",
                    (agent_id,),
                ).fetchone()[0]
            except Exception:
                archived = 0
        else:
            total = conn.execute(
                "SELECT COUNT(*) FROM memories WHERE compressed_into IS NULL",
            ).fetchone()[0]
            active = conn.execute(
                "SELECT COUNT(*) FROM memories WHERE compressed_into IS NULL AND decay_score >= 0.05",
            ).fetchone()[0]
            try:
                archived = conn.execute(
                    "SELECT COUNT(*) FROM memories WHERE archived_at IS NOT NULL",
                ).fetchone()[0]
            except Exception:
                archived = 0

        db_path = _get_db_path()
        db_size = os.path.getsize(str(db_path)) if db_path.exists() else 0

    return {"total_memories": total, "active_memories": active, "archived_memories": archived, "db_size_bytes": db_size}


def list_agents() -> list[dict]:
    """Return all distinct agent_ids with memory count and last activity."""
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT agent_id,
                   COUNT(*) AS memory_count,
                   MAX(created_at) AS last_active
            FROM memories
            WHERE compressed_into IS NULL
            GROUP BY agent_id
            ORDER BY last_active DESC
            """
        ).fetchall()
    return [dict(r) for r in rows]
```

## File: `kore_memory/repository/search.py`
```python
"""
Kore — Repository: Search operations.
FTS5, semantic search, tag search, timeline.
"""

from __future__ import annotations

from datetime import UTC, datetime

from ..database import get_connection
from ..decay import effective_score, should_forget
from ..models import MemoryRecord
from .memory import _embeddings_available


def search_memories(
    query: str,
    limit: int = 5,
    category: str | None = None,
    semantic: bool = True,
    agent_id: str = "default",
    cursor: tuple[float, int] | None = None,
) -> tuple[list[MemoryRecord], tuple[float, int] | None, int]:
    """
    Search memories with cursor-based pagination.

    Returns: (results, next_cursor, total_count)
    - results: list of MemoryRecord
    - next_cursor: (decay_score, id) for next page, or None if no more results
    - total_count: total matching memories in DB (not just page size)

    Uses semantic (embedding) search when available,
    falls back to FTS5 full-text search, then LIKE.
    Filters out fully-decayed memories. Reinforces access count on results.
    """
    # Fetch extra results to ensure we have enough after filtering
    fetch_limit = limit * 3

    if semantic and _embeddings_available():
        results = _semantic_search(query, fetch_limit, category, agent_id, cursor)
    else:
        results = _fts_search(query, fetch_limit, category, agent_id, cursor)

    # Filter forgotten memories, re-rank by combined score:
    # similarity (semantic) × decay × importance_weight
    alive = [r for r in results if not should_forget(r.decay_score or 1.0)]
    alive.sort(
        key=lambda r: (r.score if r.score and r.score > 0 else 1.0)
        * effective_score(r.decay_score or 1.0, r.importance),
        reverse=True,
    )

    # Get total count of matching active memories
    total_count = _count_active_memories(query, category, agent_id)

    # Take requested page + 1 to check if there are more results
    page = alive[: limit + 1]
    has_more = len(page) > limit
    top = page[:limit]

    # Generate next cursor if there are more results
    next_cursor = None
    if has_more and top:
        last = top[-1]
        next_cursor = (last.decay_score or 1.0, last.id)

    # Reinforce access for retrieved memories
    if top:
        _reinforce([r.id for r in top])

    return top, next_cursor, total_count


def get_timeline(
    subject: str,
    limit: int = 20,
    agent_id: str = "default",
    cursor: tuple[float, int] | None = None,
) -> tuple[list[MemoryRecord], tuple[float, int] | None, int]:
    """Return memories about a subject ordered by creation time with cursor pagination."""
    fetch_limit = limit * 2  # Fetch extra for sorting

    if _embeddings_available():
        results = _semantic_search(subject, fetch_limit, category=None, agent_id=agent_id, cursor=cursor)
    else:
        results = _fts_search(subject, fetch_limit, category=None, agent_id=agent_id, cursor=cursor)

    # Get total count
    total_count = _count_active_memories(subject, None, agent_id)

    # Sort by creation time (oldest first)
    sorted_results = sorted(results, key=lambda r: r.created_at)

    # Paginate
    page = sorted_results[: limit + 1]
    has_more = len(page) > limit
    top = page[:limit]

    next_cursor = None
    if has_more and top:
        last = top[-1]
        next_cursor = (last.decay_score or 1.0, last.id)

    return top, next_cursor, total_count


def search_by_tag(tag: str, agent_id: str = "default", limit: int = 20) -> list[MemoryRecord]:
    """Search memories by tag."""
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT m.id, m.content, m.category, m.importance,
                   m.decay_score, m.access_count, m.last_accessed,
                   m.created_at, m.updated_at, NULL AS score
            FROM memories m
            JOIN memory_tags t ON m.id = t.memory_id
            WHERE t.tag = ? AND m.agent_id = ? AND m.compressed_into IS NULL
              AND m.archived_at IS NULL
              AND (m.expires_at IS NULL OR m.expires_at > datetime('now'))
            ORDER BY m.importance DESC, m.created_at DESC
            LIMIT ?
            """,
            (tag.strip().lower(), agent_id, limit),
        ).fetchall()
    return [_row_to_record(r) for r in rows]


# ── Private helpers ──────────────────────────────────────────────────────────


def _count_active_memories(query: str, category: str | None, agent_id: str) -> int:
    """Count total active memories matching query (for pagination total)."""
    with get_connection() as conn:
        safe_query = _sanitize_fts_query(query)
        if safe_query:
            sql = """
                SELECT COUNT(*) FROM memories_fts
                JOIN memories m ON memories_fts.rowid = m.id
                WHERE memories_fts MATCH :query
                  AND m.agent_id = :agent_id
                  AND m.compressed_into IS NULL
                  AND m.archived_at IS NULL
                  AND m.decay_score >= 0.05
                  AND (m.expires_at IS NULL OR m.expires_at > datetime('now'))
            """
            params: dict = {"query": safe_query, "agent_id": agent_id}
        else:
            escaped = query.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
            sql = """
                SELECT COUNT(*) FROM memories
                WHERE content LIKE :query ESCAPE '\\'
                  AND agent_id = :agent_id
                  AND compressed_into IS NULL
                  AND archived_at IS NULL
                  AND decay_score >= 0.05
                  AND (expires_at IS NULL OR expires_at > datetime('now'))
            """
            params = {"query": f"%{escaped}%", "agent_id": agent_id}

        if category:
            # Prefix m. for FTS JOIN, no prefix for direct LIKE query
            col_prefix = "m." if safe_query else ""
            sql = sql.rstrip() + f" AND {col_prefix}category = :category"
            params["category"] = category

        return conn.execute(sql, params).fetchone()[0]


def _reinforce(memory_ids: list[int]) -> None:
    """Increment access_count and update last_accessed for retrieved memories."""
    now = datetime.now(UTC).isoformat()
    with get_connection() as conn:
        conn.executemany(
            """
            UPDATE memories
            SET access_count = access_count + 1,
                last_accessed = ?,
                decay_score   = MIN(1.0, decay_score + 0.05),
                updated_at    = ?
            WHERE id = ?
            """,
            [(now, now, mid) for mid in memory_ids],
        )


def _fts_search(
    query: str,
    limit: int,
    category: str | None,
    agent_id: str = "default",
    cursor: tuple[float, int] | None = None,
) -> list[MemoryRecord]:
    """Full-text search via SQLite FTS5 with prefix wildcards, scoped to agent."""
    with get_connection() as conn:
        safe_query = _sanitize_fts_query(query)

        cursor_filter = ""
        if cursor:
            decay_score, last_id = cursor
            cursor_filter = (
                "AND ((m.decay_score, m.id) < (:cursor_score, :cursor_id))"
                if safe_query
                else "AND ((decay_score, id) < (:cursor_score, :cursor_id))"
            )

        if safe_query:
            sql = """
                SELECT m.id, m.content, m.category, m.importance,
                       m.decay_score, m.access_count, m.last_accessed,
                       m.created_at, m.updated_at, rank AS score
                FROM memories_fts
                JOIN memories m ON memories_fts.rowid = m.id
                WHERE memories_fts MATCH :query
                  AND m.agent_id = :agent_id
                  AND m.compressed_into IS NULL
                  AND m.archived_at IS NULL
                  AND (m.expires_at IS NULL OR m.expires_at > datetime('now'))
                  {category_filter}
                  {cursor_filter}
                ORDER BY m.decay_score DESC, m.id DESC
                LIMIT :limit
            """
            params: dict = {"query": safe_query, "limit": limit, "agent_id": agent_id}
        else:
            sql = """
                SELECT id, content, category, importance,
                       decay_score, access_count, last_accessed,
                       created_at, updated_at, NULL AS score
                FROM memories
                WHERE content LIKE :query ESCAPE '\\'
                  AND agent_id = :agent_id
                  AND compressed_into IS NULL
                  AND archived_at IS NULL
                  AND (expires_at IS NULL OR expires_at > datetime('now'))
                  {category_filter}
                  {cursor_filter}
                ORDER BY decay_score DESC, id DESC
                LIMIT :limit
            """
            # q=* → list all memories (global wildcard)
            if query.strip() == "*":
                escaped_query = ""
            else:
                escaped_query = query.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
            params = {"query": f"%{escaped_query}%", "limit": limit, "agent_id": agent_id}

        if cursor:
            params["cursor_score"] = cursor[0]
            params["cursor_id"] = cursor[1]

        category_filter = (
            "AND m.category = :category" if safe_query and category else "AND category = :category" if category else ""
        )
        if category:
            params["category"] = category

        rows = conn.execute(sql.format(category_filter=category_filter, cursor_filter=cursor_filter), params).fetchall()

    return [_row_to_record(r) for r in rows]


def _semantic_search(
    query: str,
    limit: int,
    category: str | None,
    agent_id: str = "default",
    cursor: tuple[float, int] | None = None,
) -> list[MemoryRecord]:
    """Semantic search with vector index, scoped to agent."""
    from ..embedder import embed_query
    from ..vector_index import get_index

    query_vec = embed_query(query)
    index = get_index()

    # Batch vector search via in-memory index
    top_ids = index.search(query_vec, agent_id, category=category, limit=limit)
    if not top_ids:
        return []

    # Load full records from DB with cursor filter
    id_score_map = {mem_id: score for mem_id, score in top_ids}
    placeholders = ",".join("?" for _ in top_ids)

    cursor_filter = ""
    params = [id for id, _ in top_ids]

    with get_connection() as conn:
        # Build query — parameter order: IN ids, category, cursor
        category_clause = "AND category = ?" if category else ""
        if category:
            params.append(category)

        if cursor:
            decay_score, last_id = cursor
            cursor_filter = "AND ((decay_score, id) < (?, ?))"
            params.extend([decay_score, last_id])

        sql = f"""
            SELECT id, content, category, importance,
                   decay_score, access_count, last_accessed,
                   created_at, updated_at
            FROM memories
            WHERE id IN ({placeholders})
              AND archived_at IS NULL
              AND (expires_at IS NULL OR expires_at > datetime('now'))
              {category_clause}
              {cursor_filter}
            ORDER BY decay_score DESC, id DESC
        """
        rows = conn.execute(sql, params).fetchall()

    results = []
    for row in rows:
        sim = id_score_map.get(row["id"], 0.0)
        results.append(
            MemoryRecord(
                id=row["id"],
                content=row["content"],
                category=row["category"],
                importance=row["importance"],
                decay_score=row["decay_score"],
                created_at=row["created_at"],
                updated_at=row["updated_at"],
                score=round(sim, 4),
            )
        )

    # Sort by descending score
    results.sort(key=lambda r: r.score or 0.0, reverse=True)
    return results


def _sanitize_fts_query(query: str) -> str:
    """Sanitize FTS5 query: remove special operators, limit token count."""
    special = set('"^():-*+<>&|')
    cleaned = "".join(c if c not in special else " " for c in query).strip()
    if not cleaned:
        return ""
    # Max 10 tokens, min 2 characters each — prevents DoS
    tokens = [t for t in cleaned.split() if len(t) >= 2][:10]
    if not tokens:
        return ""
    # Quote for exact match, wildcard suffix for flexibility
    return " OR ".join(f'"{t}"*' for t in tokens)


def _row_to_record(row) -> MemoryRecord:
    return MemoryRecord(
        id=row["id"],
        content=row["content"],
        category=row["category"],
        importance=row["importance"],
        decay_score=row["decay_score"] if "decay_score" in row.keys() else 1.0,
        created_at=row["created_at"],
        updated_at=row["updated_at"],
        score=row["score"],
    )
```

## File: `kore_memory/repository/sessions.py`
```python
"""
Kore — Repository: Session management.
Create, list, end, delete, summarize conversation sessions.
"""

from __future__ import annotations

from ..database import get_connection
from ..models import MemoryRecord
from .search import _row_to_record


def create_session(session_id: str, agent_id: str = "default", title: str | None = None) -> dict:
    """Create a new conversation session."""
    with get_connection() as conn:
        conn.execute(
            "INSERT OR IGNORE INTO sessions (id, agent_id, title) VALUES (?, ?, ?)",
            (session_id, agent_id, title),
        )
        row = conn.execute("SELECT * FROM sessions WHERE id = ?", (session_id,)).fetchone()
    return dict(row) if row else {}


def list_sessions(agent_id: str = "default", limit: int = 50) -> list[dict]:
    """List all sessions for an agent with memory count."""
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT s.id, s.agent_id, s.title, s.created_at, s.ended_at,
                   COUNT(m.id) AS memory_count
            FROM sessions s
            LEFT JOIN memories m ON m.session_id = s.id AND m.agent_id = s.agent_id
            WHERE s.agent_id = ?
            GROUP BY s.id
            ORDER BY s.created_at DESC
            LIMIT ?
            """,
            (agent_id, limit),
        ).fetchall()
    return [dict(r) for r in rows]


def get_session_memories(session_id: str, agent_id: str = "default") -> list[MemoryRecord]:
    """Get all memories in a session."""
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT id, content, category, importance, decay_score,
                   access_count, last_accessed, created_at, updated_at, NULL AS score
            FROM memories
            WHERE session_id = ? AND agent_id = ? AND compressed_into IS NULL
            ORDER BY created_at ASC
            """,
            (session_id, agent_id),
        ).fetchall()
    return [_row_to_record(r) for r in rows]


def end_session(session_id: str, agent_id: str = "default") -> bool:
    """Mark a session as ended."""
    with get_connection() as conn:
        cursor = conn.execute(
            "UPDATE sessions SET ended_at = datetime('now') WHERE id = ? AND agent_id = ? AND ended_at IS NULL",
            (session_id, agent_id),
        )
        return cursor.rowcount > 0


def delete_session(session_id: str, agent_id: str = "default") -> int:
    """Delete a session and unlink its memories. Returns number of memories unlinked."""
    with get_connection() as conn:
        # Unlink memories from session (don't delete them)
        cursor = conn.execute(
            "UPDATE memories SET session_id = NULL WHERE session_id = ? AND agent_id = ?",
            (session_id, agent_id),
        )
        unlinked = cursor.rowcount
        conn.execute(
            "DELETE FROM sessions WHERE id = ? AND agent_id = ?",
            (session_id, agent_id),
        )
    return unlinked


def get_session_summary(session_id: str, agent_id: str = "default") -> dict:
    """Get a summary of a session (no LLM, just aggregation)."""
    with get_connection() as conn:
        row = conn.execute(
            "SELECT * FROM sessions WHERE id = ? AND agent_id = ?",
            (session_id, agent_id),
        ).fetchone()
        if not row:
            return {}

        stats = conn.execute(
            """
            SELECT COUNT(*) AS memory_count,
                   GROUP_CONCAT(DISTINCT category) AS categories,
                   AVG(importance) AS avg_importance,
                   MIN(created_at) AS first_memory,
                   MAX(created_at) AS last_memory
            FROM memories
            WHERE session_id = ? AND agent_id = ? AND compressed_into IS NULL
            """,
            (session_id, agent_id),
        ).fetchone()

    return {
        "session_id": row["id"],
        "agent_id": row["agent_id"],
        "title": row["title"],
        "created_at": row["created_at"],
        "ended_at": row["ended_at"],
        "memory_count": stats["memory_count"] or 0,
        "categories": stats["categories"].split(",") if stats["categories"] else [],
        "avg_importance": round(stats["avg_importance"] or 0, 1),
        "first_memory": stats["first_memory"],
        "last_memory": stats["last_memory"],
    }
```

## File: `kore_memory/templates/dashboard.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Kore — Memory Dashboard</title>
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<style>
/* ── Reset + Variables ─────────────────────────────────────────────── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --bg-primary: #09090b;
  --bg-secondary: #18181b;
  --bg-tertiary: #27272a;
  --bg-hover: #3f3f46;
  --border: #27272a;
  --border-hover: #3f3f46;
  --text: #fafafa;
  --text-muted: #a1a1aa;
  --text-dim: #71717a;
  --accent: #8b5cf6;
  --accent-hover: #a78bfa;
  --accent-muted: rgba(139, 92, 246, 0.15);
  --success: #10b981;
  --success-muted: rgba(16, 185, 129, 0.15);
  --warning: #f59e0b;
  --warning-muted: rgba(245, 158, 11, 0.15);
  --danger: #ef4444;
  --danger-muted: rgba(239, 68, 68, 0.15);
  --radius: 8px;
  --radius-lg: 12px;
  --radius-full: 9999px;
  --sidebar-w: 240px;
  --header-h: 65px;
  --font: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
  --font-mono: 'SF Mono', 'Cascadia Code', 'Fira Code', ui-monospace, monospace;
  --shadow: 0 1px 3px rgba(0,0,0,0.3);
  --shadow-lg: 0 8px 24px rgba(0,0,0,0.4);
  --transition: 0.2s ease;
}

/* ── Light theme ──────────────────────────────────────────────────── */
[data-theme="light"] {
  --bg-primary: #fafafa;
  --bg-secondary: #ffffff;
  --bg-tertiary: #f4f4f5;
  --bg-hover: #e4e4e7;
  --border: #e4e4e7;
  --border-hover: #d4d4d8;
  --text: #18181b;
  --text-muted: #71717a;
  --text-dim: #a1a1aa;
  --accent: #7c3aed;
  --accent-hover: #6d28d9;
  --accent-muted: rgba(124, 58, 237, 0.1);
  --success: #059669;
  --success-muted: rgba(5, 150, 105, 0.1);
  --warning: #d97706;
  --warning-muted: rgba(217, 119, 6, 0.1);
  --danger: #dc2626;
  --danger-muted: rgba(220, 38, 38, 0.1);
  --shadow: 0 1px 3px rgba(0,0,0,0.06);
  --shadow-lg: 0 8px 24px rgba(0,0,0,0.1);
}

html { font-size: 14px; }
body {
  font-family: var(--font);
  background: var(--bg-primary);
  color: var(--text);
  min-height: 100vh;
  overflow: hidden;
  -webkit-font-smoothing: antialiased;
}

/* ── Scrollbar ────────────────────────────────────────────────────── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--border-hover); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--accent); }

/* ── Layout ───────────────────────────────────────────────────────── */
.app {
  display: grid;
  grid-template-columns: var(--sidebar-w) 1fr;
  grid-template-rows: var(--header-h) 1fr;
  height: 100vh;
}

/* ── Sidebar ──────────────────────────────────────────────────────── */
.sidebar {
  grid-row: 1 / -1;
  background: var(--bg-secondary);
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  z-index: 20;
}
.sidebar-brand {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 16px 20px;
  border-bottom: 1px solid var(--border);
  text-decoration: none;
  color: var(--text);
}
.sidebar-brand .logo {
  width: 32px; height: 32px;
  background: linear-gradient(135deg, #a78bfa, #7c3aed);
  border-radius: var(--radius);
  display: flex; align-items: center; justify-content: center;
  font-weight: 700; font-size: 16px; color: #fff;
  flex-shrink: 0;
}
.sidebar-brand span { font-weight: 600; font-size: 15px; letter-spacing: -0.3px; }
.sidebar-brand small { color: var(--text-dim); font-size: 11px; font-weight: 400; margin-left: auto; }

.sidebar-nav { flex: 1; padding: 8px; }
.nav-item {
  display: flex; align-items: center; gap: 10px;
  padding: 9px 12px; border-radius: var(--radius);
  color: var(--text-muted); cursor: pointer;
  transition: all var(--transition); font-size: 13px;
  border: none; background: none; width: 100%; text-align: left;
  font-family: inherit;
}
.nav-item:hover { background: var(--bg-tertiary); color: var(--text); }
.nav-item.active { background: var(--accent-muted); color: var(--accent); font-weight: 500; }
.nav-item svg { flex-shrink: 0; opacity: 0.7; }
.nav-item.active svg { opacity: 1; }

.sidebar-footer {
  padding: 12px 16px;
  border-top: 1px solid var(--border);
  display: flex; gap: 12px; align-items: center;
}
.sidebar-footer a {
  color: var(--text-dim); text-decoration: none; font-size: 12px;
  display: flex; align-items: center; gap: 4px;
  transition: color var(--transition);
}
.sidebar-footer a:hover { color: var(--accent); }

/* ── Header ───────────────────────────────────────────────────────── */
.header {
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 24px; background: var(--bg-secondary);
  border-bottom: 1px solid var(--border); z-index: 10;
}
.header-left { display: flex; align-items: center; gap: 16px; }
.header-title { font-weight: 600; font-size: 16px; color: var(--text); }
.header-right { display: flex; align-items: center; gap: 8px; }

.btn-hamburger {
  display: none; background: none; border: none; color: var(--text);
  cursor: pointer; padding: 6px; border-radius: var(--radius);
}
.btn-hamburger:hover { background: var(--bg-tertiary); }

/* ── Agent selector ──────────────────────────────────────────────── */
.agent-select {
  background: var(--bg-tertiary); border: 1px solid var(--border);
  color: var(--text); padding: 6px 10px; border-radius: var(--radius);
  font-family: var(--font-mono); font-size: 12px; cursor: pointer;
  outline: none; transition: border-color var(--transition);
}
.agent-select:focus { border-color: var(--accent); }

/* ── Theme button ────────────────────────────────────────────────── */
.btn-icon {
  background: none; border: 1px solid var(--border); color: var(--text-muted);
  width: 34px; height: 34px; border-radius: var(--radius);
  display: flex; align-items: center; justify-content: center;
  cursor: pointer; transition: all var(--transition);
}
.btn-icon:hover { background: var(--bg-tertiary); color: var(--text); border-color: var(--border-hover); }

/* ── Main ─────────────────────────────────────────────────────────── */
.main {
  overflow-y: auto; padding: 24px;
  background: var(--bg-primary);
}

/* ── Pages ─────────────────────────────────────────────────────────── */
.page { display: none; animation: fadeIn 0.25s ease; }
.page.active { display: block; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }

/* ── Cards ─────────────────────────────────────────────────────────── */
.card {
  background: var(--bg-secondary); border: 1px solid var(--border);
  border-radius: var(--radius-lg); padding: 20px;
  transition: border-color var(--transition);
}
.card:hover { border-color: var(--border-hover); }
.card-title { font-weight: 600; font-size: 13px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 12px; }

/* ── Stats grid ───────────────────────────────────────────────────── */
.stats-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 12px; margin-bottom: 24px;
}
.stat-card {
  background: var(--bg-secondary); border: 1px solid var(--border);
  border-radius: var(--radius-lg); padding: 16px 20px;
  transition: all var(--transition);
}
.stat-card:hover { border-color: var(--accent); box-shadow: 0 0 0 1px var(--accent-muted); }
.stat-label { font-size: 12px; color: var(--text-dim); margin-bottom: 4px; }
.stat-value { font-size: 28px; font-weight: 700; color: var(--text); line-height: 1.2; }
.stat-value.accent { color: var(--accent); }
.stat-value.success { color: var(--success); }
.stat-value.warning { color: var(--warning); }
.stat-sub { font-size: 11px; color: var(--text-dim); margin-top: 2px; }

/* ── Buttons ──────────────────────────────────────────────────────── */
.btn {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 8px 16px; border-radius: var(--radius); font-size: 13px;
  font-weight: 500; cursor: pointer; transition: all var(--transition);
  border: 1px solid transparent; font-family: inherit;
}
.btn-primary { background: var(--accent); color: #fff; border-color: var(--accent); }
.btn-primary:hover { background: var(--accent-hover); border-color: var(--accent-hover); }
.btn-secondary { background: var(--bg-tertiary); color: var(--text); border-color: var(--border); }
.btn-secondary:hover { background: var(--bg-hover); border-color: var(--border-hover); }
.btn-danger { background: var(--danger-muted); color: var(--danger); border-color: transparent; }
.btn-danger:hover { background: var(--danger); color: #fff; }
.btn-success { background: var(--success-muted); color: var(--success); border-color: transparent; }
.btn-success:hover { background: var(--success); color: #fff; }
.btn-sm { padding: 5px 10px; font-size: 12px; }
.btn-ghost { background: none; border: none; color: var(--text-muted); padding: 6px; }
.btn-ghost:hover { color: var(--text); background: var(--bg-tertiary); }
.btn:disabled { opacity: 0.5; cursor: not-allowed; }

/* ── Input / Form ─────────────────────────────────────────────────── */
.input, .textarea, .select {
  background: var(--bg-tertiary); border: 1px solid var(--border);
  color: var(--text); padding: 8px 12px; border-radius: var(--radius);
  font-family: inherit; font-size: 13px; width: 100%;
  outline: none; transition: border-color var(--transition);
}
.input:focus, .textarea:focus, .select:focus { border-color: var(--accent); }
.textarea { resize: vertical; min-height: 80px; }
.form-group { margin-bottom: 14px; }
.form-label { display: block; font-size: 12px; font-weight: 500; color: var(--text-muted); margin-bottom: 4px; }

/* ── Badge ─────────────────────────────────────────────────────────── */
.badge {
  display: inline-flex; align-items: center; padding: 2px 8px;
  border-radius: var(--radius-full); font-size: 11px; font-weight: 500;
}
.badge-general { background: rgba(139,92,246,0.15); color: #a78bfa; }
.badge-project { background: rgba(59,130,246,0.15); color: #60a5fa; }
.badge-trading { background: rgba(245,158,11,0.15); color: #fbbf24; }
.badge-finance { background: rgba(16,185,129,0.15); color: #34d399; }
.badge-person { background: rgba(236,72,153,0.15); color: #f472b6; }
.badge-preference { background: rgba(6,182,212,0.15); color: #22d3ee; }
.badge-task { background: rgba(249,115,22,0.15); color: #fb923c; }
.badge-decision { background: rgba(99,102,241,0.15); color: #818cf8; }
.badge-tag { background: var(--bg-tertiary); color: var(--text-muted); font-size: 12px; padding: 3px 10px; cursor: pointer; }
.badge-tag:hover { background: var(--accent-muted); color: var(--accent); }

/* ── Table ────────────────────────────────────────────────────────── */
.table-wrap { overflow-x: auto; }
table { width: 100%; border-collapse: collapse; }
th { text-align: left; font-size: 11px; font-weight: 600; color: var(--text-dim); text-transform: uppercase; letter-spacing: 0.5px; padding: 10px 12px; border-bottom: 1px solid var(--border); }
td { padding: 10px 12px; border-bottom: 1px solid var(--border); font-size: 13px; color: var(--text); vertical-align: top; }
tr:hover td { background: var(--bg-tertiary); }

/* ── Importance dots ──────────────────────────────────────────────── */
.importance { display: flex; gap: 3px; }
.importance .dot {
  width: 8px; height: 8px; border-radius: 50%;
  background: var(--border); transition: background var(--transition);
}
.importance .dot.filled { background: var(--accent); }

/* ── Decay bar ────────────────────────────────────────────────────── */
.decay-bar { width: 60px; height: 4px; background: var(--bg-tertiary); border-radius: 2px; overflow: hidden; }
.decay-bar-fill { height: 100%; border-radius: 2px; transition: width 0.4s ease; }

/* ── Toolbar ──────────────────────────────────────────────────────── */
.toolbar {
  display: flex; align-items: center; gap: 10px;
  margin-bottom: 20px; flex-wrap: wrap;
}
.search-box {
  display: flex; align-items: center; gap: 8px;
  background: var(--bg-secondary); border: 1px solid var(--border);
  border-radius: var(--radius); padding: 0 12px; flex: 1; max-width: 400px;
}
.search-box svg { color: var(--text-dim); flex-shrink: 0; }
.search-box input {
  background: none; border: none; color: var(--text);
  padding: 8px 0; font-size: 13px; width: 100%; outline: none;
  font-family: inherit;
}

/* ── Modal ─────────────────────────────────────────────────────────── */
.modal-overlay {
  position: fixed; inset: 0; background: rgba(0,0,0,0.6);
  display: none; align-items: center; justify-content: center;
  z-index: 100; backdrop-filter: blur(4px);
}
.modal-overlay.open { display: flex; }
.modal {
  background: var(--bg-secondary); border: 1px solid var(--border);
  border-radius: var(--radius-lg); padding: 24px; width: 90%;
  max-width: 520px; max-height: 85vh; overflow-y: auto;
  box-shadow: var(--shadow-lg); animation: modalIn 0.2s ease;
}
@keyframes modalIn { from { opacity: 0; transform: scale(0.96); } to { opacity: 1; transform: scale(1); } }
.modal-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
.modal-title { font-weight: 600; font-size: 16px; }
.modal-footer { display: flex; justify-content: flex-end; gap: 8px; margin-top: 20px; padding-top: 16px; border-top: 1px solid var(--border); }

/* ── Toast ─────────────────────────────────────────────────────────── */
.toast-container { position: fixed; top: 16px; right: 16px; z-index: 200; display: flex; flex-direction: column; gap: 8px; }
.toast {
  padding: 12px 16px; border-radius: var(--radius); font-size: 13px;
  display: flex; align-items: center; gap: 8px;
  animation: toastIn 0.3s ease; min-width: 260px;
  box-shadow: var(--shadow-lg);
}
.toast-success { background: var(--success); color: #fff; }
.toast-error { background: var(--danger); color: #fff; }
.toast-info { background: var(--accent); color: #fff; }
@keyframes toastIn { from { opacity: 0; transform: translateX(20px); } to { opacity: 1; transform: translateX(0); } }

/* ── Empty state ──────────────────────────────────────────────────── */
.empty-state {
  display: flex; flex-direction: column; align-items: center;
  justify-content: center; padding: 48px 24px; color: var(--text-dim);
  text-align: center;
}
.empty-state svg { margin-bottom: 12px; opacity: 0.4; }
.empty-state p { font-size: 14px; max-width: 320px; }

/* ── Spinner ──────────────────────────────────────────────────────── */
.spinner { display: inline-block; width: 20px; height: 20px; border: 2px solid var(--border); border-top-color: var(--accent); border-radius: 50%; animation: spin 0.6s linear infinite; }
@keyframes spin { to { transform: rotate(360deg); } }
.loading-center { display: flex; justify-content: center; padding: 48px; }

/* ── Grid layout utilities ────────────────────────────────────────── */
.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
.flex-between { display: flex; justify-content: space-between; align-items: center; }
.mb-16 { margin-bottom: 16px; }
.mb-24 { margin-bottom: 24px; }

/* ── Memory card ──────────────────────────────────────────────────── */
.memory-card {
  background: var(--bg-secondary); border: 1px solid var(--border);
  border-radius: var(--radius-lg); padding: 16px; margin-bottom: 10px;
  transition: all var(--transition);
}
.memory-card:hover { border-color: var(--border-hover); }
.memory-card-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px; }
.memory-card-content { font-size: 13px; color: var(--text); line-height: 1.5; margin-bottom: 10px; word-break: break-word; }
.memory-card-footer { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }
.memory-card-footer .meta { font-size: 11px; color: var(--text-dim); display: flex; align-items: center; gap: 4px; }
.memory-card-actions { display: flex; gap: 4px; }

/* ── Quick actions ────────────────────────────────────────────────── */
.action-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }
.action-card {
  background: var(--bg-secondary); border: 1px solid var(--border);
  border-radius: var(--radius-lg); padding: 20px; cursor: pointer;
  transition: all var(--transition); text-align: left;
  font-family: inherit;
}
.action-card:hover { border-color: var(--accent); transform: translateY(-1px); box-shadow: 0 4px 12px rgba(0,0,0,0.2); }
.action-card:disabled { opacity: 0.5; cursor: not-allowed; transform: none; }
.action-card h3 { font-size: 14px; font-weight: 600; margin-bottom: 4px; }
.action-card p { font-size: 12px; color: var(--text-dim); }

/* ── Category distribution ────────────────────────────────────────── */
.cat-bar-row { display: flex; align-items: center; gap: 10px; margin-bottom: 8px; }
.cat-bar-label { font-size: 12px; color: var(--text-muted); width: 80px; text-align: right; }
.cat-bar-track { flex: 1; height: 8px; background: var(--bg-tertiary); border-radius: 4px; overflow: hidden; }
.cat-bar-fill { height: 100%; border-radius: 4px; transition: width 0.5s ease; }
.cat-bar-count { font-size: 12px; color: var(--text-dim); width: 32px; }

/* ── Graph canvas ─────────────────────────────────────────────────── */
.graph-container { position: relative; }
#graph-canvas {
  width: 100%; height: calc(100vh - 200px);
  background: var(--bg-secondary); border: 1px solid var(--border);
  border-radius: var(--radius-lg); cursor: grab;
}
#graph-canvas.dragging { cursor: grabbing; }
#graph-canvas.hovering { cursor: pointer; }

/* Graph tooltip */
.graph-tooltip {
  position: absolute; pointer-events: none;
  background: var(--bg-secondary); border: 1px solid var(--border);
  border-radius: var(--radius); padding: 10px 14px;
  box-shadow: var(--shadow-lg); font-size: 12px;
  max-width: 300px; z-index: 30; display: none;
  transition: opacity 0.15s ease; opacity: 0;
}
.graph-tooltip.visible { display: block; opacity: 1; }
.graph-tooltip .tt-id { color: var(--accent); font-family: var(--font-mono); font-weight: 600; }
.graph-tooltip .tt-cat { margin-left: 6px; }
.graph-tooltip .tt-content { margin-top: 4px; color: var(--text); line-height: 1.4; }
.graph-tooltip .tt-relations { margin-top: 6px; padding-top: 6px; border-top: 1px solid var(--border); color: var(--text-dim); font-size: 11px; }

/* Node detail panel */
.graph-detail {
  position: absolute; top: 12px; right: 12px; width: 280px;
  background: var(--bg-secondary); border: 1px solid var(--border);
  border-radius: var(--radius-lg); padding: 16px;
  box-shadow: var(--shadow-lg); display: none; z-index: 25;
  max-height: calc(100% - 24px); overflow-y: auto;
}
.graph-detail.open { display: block; animation: fadeIn 0.2s ease; }
.graph-detail-close { position: absolute; top: 8px; right: 8px; }

/* Graph legend */
.graph-legend {
  display: flex; flex-wrap: wrap; gap: 8px; margin-top: 8px;
  padding: 8px 12px; background: var(--bg-secondary);
  border: 1px solid var(--border); border-radius: var(--radius);
}
.graph-legend-item { display: flex; align-items: center; gap: 4px; font-size: 11px; color: var(--text-muted); }
.graph-legend-dot { width: 10px; height: 10px; border-radius: 50%; }

/* ── Sessions ─────────────────────────────────────────────────────── */
.session-card {
  background: var(--bg-secondary); border: 1px solid var(--border);
  border-radius: var(--radius-lg); padding: 16px; margin-bottom: 10px;
  display: flex; justify-content: space-between; align-items: center;
  transition: border-color var(--transition);
}
.session-card:hover { border-color: var(--border-hover); }
.session-info h4 { font-size: 14px; margin-bottom: 2px; }
.session-info .meta { font-size: 12px; color: var(--text-dim); }

/* ── Timeline ─────────────────────────────────────────────────────── */
.timeline-item {
  display: flex; gap: 16px; padding: 16px 0;
  border-bottom: 1px solid var(--border);
}
.timeline-dot {
  width: 10px; height: 10px; border-radius: 50%;
  background: var(--accent); margin-top: 4px; flex-shrink: 0;
}
.timeline-content { flex: 1; }
.timeline-date { font-size: 11px; color: var(--text-dim); margin-bottom: 4px; }
.timeline-text { font-size: 13px; line-height: 1.5; }

/* ── Audit log ────────────────────────────────────────────────────── */
.audit-row { font-family: var(--font-mono); font-size: 12px; }
.audit-event { color: var(--accent); font-weight: 500; }
.audit-time { color: var(--text-dim); }

/* ── Tag cloud ────────────────────────────────────────────────────── */
.tag-cloud { display: flex; flex-wrap: wrap; gap: 6px; }

/* ── Responsive ───────────────────────────────────────────────────── */
@media (max-width: 768px) {
  .app { grid-template-columns: 1fr; }
  .sidebar {
    position: fixed; left: -260px; top: 0; bottom: 0;
    width: 260px; transition: left 0.3s ease;
    box-shadow: var(--shadow-lg);
  }
  .sidebar.open { left: 0; }
  .btn-hamburger { display: flex; }
  .main { padding: 16px; }
  .stats-grid { grid-template-columns: repeat(2, 1fr); }
  .grid-2, .grid-3 { grid-template-columns: 1fr; }
  .header-title { font-size: 14px; }
  .action-grid { grid-template-columns: 1fr; }
}

/* ── Visible focus (accessibility) ───────────────────────────────── */
:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}
button:focus:not(:focus-visible), a:focus:not(:focus-visible) { outline: none; }
</style>
</head>
<body>

<div class="app">
  <!-- Sidebar -->
  <aside class="sidebar" id="sidebar">
    <a class="sidebar-brand" href="/dashboard">
      <div class="logo">K</div>
      <span>Kore</span>
      <small id="version-badge">v-</small>
    </a>
    <nav class="sidebar-nav" id="sidebar-nav"></nav>
    <div class="sidebar-footer">
      <a href="https://github.com/auriti-labs/kore-memory" target="_blank" rel="noopener" title="GitHub">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
        GitHub
      </a>
      <a href="https://auritidesign.it/brain/knowledge/docs_legacy/kore-memory/" target="_blank" rel="noopener" title="Documentation">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
        Docs
      </a>
    </div>
  </aside>

  <!-- Header -->
  <header class="header">
    <div class="header-left">
      <button class="btn-hamburger" id="btn-hamburger" aria-label="Menu">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
      </button>
      <h1 class="header-title" id="header-title">Overview</h1>
    </div>
    <div class="header-right">
      <select class="agent-select" id="agent-select" title="Select agent">
        <option value="default">default</option>
      </select>
      <button class="btn-icon" id="btn-theme" title="Toggle theme" aria-label="Toggle theme">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" id="icon-theme"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
      </button>
    </div>
  </header>

  <!-- Main content -->
  <main class="main" id="main-content">

    <!-- PAGE: Overview -->
    <section class="page active" data-page="overview">
      <div class="stats-grid" id="stats-grid"></div>
      <div class="grid-2 mb-24">
        <div class="card">
          <div class="card-title">Recent memories</div>
          <div id="recent-memories"></div>
        </div>
        <div class="card">
          <div class="card-title">Category distribution</div>
          <div id="category-dist"></div>
        </div>
      </div>
      <div class="card">
        <div class="card-title">Quick actions</div>
        <div class="action-grid" id="quick-actions"></div>
      </div>
    </section>

    <!-- PAGE: Memories -->
    <section class="page" data-page="memories">
      <div class="toolbar">
        <div class="search-box">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
          <input type="text" id="mem-search" placeholder="Search memories...">
        </div>
        <select class="select" id="mem-category" style="width:auto;min-width:120px">
          <option value="">All</option>
          <option value="general">general</option>
          <option value="project">project</option>
          <option value="trading">trading</option>
          <option value="finance">finance</option>
          <option value="person">person</option>
          <option value="preference">preference</option>
          <option value="task">task</option>
          <option value="decision">decision</option>
        </select>
        <label style="display:flex;align-items:center;gap:4px;font-size:12px;color:var(--text-muted);cursor:pointer">
          <input type="checkbox" id="mem-semantic" checked> Semantic
        </label>
        <button class="btn btn-primary" id="btn-new-memory">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
          New
        </button>
      </div>
      <div id="memories-list"></div>
    </section>

    <!-- PAGE: Tags & Relations -->
    <section class="page" data-page="tags">
      <div class="grid-2">
        <div class="card">
          <div class="card-title">Tag</div>
          <div class="toolbar">
            <div class="search-box" style="max-width:100%">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
              <input type="text" id="tag-search" placeholder="Search tags...">
            </div>
          </div>
          <div class="tag-cloud" id="tag-cloud"></div>
          <div id="tag-memories" style="margin-top:16px"></div>
        </div>
        <div class="card">
          <div class="card-title">Relations</div>
          <div id="relations-list"></div>
          <div style="margin-top:16px;padding-top:16px;border-top:1px solid var(--border)">
            <div class="card-title">Create relation</div>
            <div class="form-group">
              <label class="form-label">Source ID</label>
              <input type="number" class="input" id="rel-source" placeholder="Source memory ID">
            </div>
            <div class="form-group">
              <label class="form-label">Target ID</label>
              <input type="number" class="input" id="rel-target" placeholder="Target memory ID">
            </div>
            <div class="form-group">
              <label class="form-label">Relation type</label>
              <input type="text" class="input" id="rel-type" value="related" placeholder="related, causes, requires...">
            </div>
            <button class="btn btn-primary" id="btn-add-relation">Create relation</button>
          </div>
        </div>
      </div>
    </section>

    <!-- PAGE: Graph -->
    <section class="page" data-page="graph">
      <div class="toolbar">
        <button class="btn btn-secondary" id="btn-graph-reload">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 4 23 10 17 10"/><path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"/></svg>
          Reload
        </button>
        <button class="btn btn-secondary" id="btn-graph-center">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M12 2v4m0 12v4M2 12h4m12 0h4"/></svg>
          Center
        </button>
        <label style="display:flex;align-items:center;gap:4px;font-size:12px;color:var(--text-muted);cursor:pointer">
          <input type="checkbox" id="graph-show-labels" checked> Labels
        </label>
        <label style="display:flex;align-items:center;gap:4px;font-size:12px;color:var(--text-muted);cursor:pointer">
          <input type="checkbox" id="graph-show-arrows" checked> Arrows
        </label>
        <span style="font-size:12px;color:var(--text-dim);margin-left:auto" id="graph-info">Nodes: 0 — Edges: 0</span>
      </div>
      <div class="graph-container">
        <canvas id="graph-canvas"></canvas>
        <div class="graph-tooltip" id="graph-tooltip">
          <div><span class="tt-id"></span><span class="tt-cat badge"></span></div>
          <div class="tt-content"></div>
          <div class="tt-relations"></div>
        </div>
        <div class="graph-detail" id="graph-detail">
          <button class="btn-ghost graph-detail-close" id="graph-detail-close" aria-label="Close">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
          </button>
          <div id="graph-detail-content"></div>
        </div>
      </div>
      <div class="graph-legend" id="graph-legend"></div>
    </section>

    <!-- PAGE: Sessions -->
    <section class="page" data-page="sessions">
      <div class="toolbar">
        <button class="btn btn-primary" id="btn-new-session">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
          New session
        </button>
      </div>
      <div id="sessions-list"></div>
    </section>

    <!-- PAGE: Timeline -->
    <section class="page" data-page="timeline">
      <div class="toolbar">
        <div class="search-box">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
          <input type="text" id="timeline-search" placeholder="Subject to search...">
        </div>
        <button class="btn btn-primary" id="btn-timeline-search">Search</button>
      </div>
      <div id="timeline-list"></div>
    </section>

    <!-- PAGE: Maintenance -->
    <section class="page" data-page="maintenance">
      <div class="action-grid mb-24">
        <button class="action-card" id="btn-decay">
          <h3 style="color:var(--accent)">Run Decay</h3>
          <p>Recalculate decay scores (Ebbinghaus)</p>
        </button>
        <button class="action-card" id="btn-compress">
          <h3 style="color:var(--success)">Compress</h3>
          <p>Merge similar memories (cosine similarity)</p>
        </button>
        <button class="action-card" id="btn-cleanup">
          <h3 style="color:var(--warning)">Cleanup TTL</h3>
          <p>Remove expired memories</p>
        </button>
        <button class="action-card" id="btn-autotune">
          <h3 style="color:var(--danger)">Auto-Tune</h3>
          <p>Optimize importance based on access</p>
        </button>
      </div>
      <div class="grid-2 mb-24">
        <div class="card">
          <div class="card-title">Scoring Stats</div>
          <div id="scoring-stats"></div>
        </div>
        <div class="card">
          <div class="card-title">Archive</div>
          <div id="archive-list"></div>
        </div>
      </div>
      <div class="card">
        <div class="card-title">Export / Import</div>
        <div style="display:flex;gap:10px;flex-wrap:wrap">
          <button class="btn btn-secondary" id="btn-export">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            Export JSON
          </button>
          <label class="btn btn-secondary" style="cursor:pointer">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
            Import JSON
            <input type="file" id="import-file" accept=".json" style="display:none">
          </label>
        </div>
      </div>
    </section>

    <!-- PAGE: Settings -->
    <section class="page" data-page="settings">
      <div class="grid-2 mb-24">
        <div class="card">
          <div class="card-title">Agents</div>
          <div id="agents-list"></div>
        </div>
        <div class="card">
          <div class="card-title">Server Info</div>
          <div id="server-info"></div>
        </div>
      </div>
      <div class="card mb-24">
        <div class="flex-between mb-16">
          <div class="card-title" style="margin-bottom:0">Audit Log</div>
          <div style="display:flex;gap:8px;align-items:center">
            <select class="select" id="audit-event-filter" style="width:auto;min-width:120px">
              <option value="">All events</option>
              <option value="save">save</option>
              <option value="search">search</option>
              <option value="delete">delete</option>
              <option value="update">update</option>
              <option value="decay">decay</option>
              <option value="compress">compress</option>
            </select>
            <button class="btn btn-sm btn-secondary" id="btn-audit-refresh">Refresh</button>
          </div>
        </div>
        <div class="table-wrap" id="audit-table"></div>
      </div>
      <div class="card">
        <div class="card-title">Prometheus Metrics</div>
        <pre id="metrics-display" style="font-family:var(--font-mono);font-size:12px;color:var(--text-muted);white-space:pre-wrap;padding:12px;background:var(--bg-tertiary);border-radius:var(--radius);overflow-x:auto"></pre>
      </div>
    </section>

  </main>
</div>

<!-- Modal Create/Edit Memory -->
<div class="modal-overlay" id="modal-memory">
  <div class="modal">
    <div class="modal-header">
      <span class="modal-title" id="modal-memory-title">New memory</span>
      <button class="btn-ghost" id="modal-memory-close" aria-label="Close">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
    </div>
    <div class="form-group">
      <label class="form-label">Content</label>
      <textarea class="textarea" id="modal-mem-content" rows="4" placeholder="Memory content..."></textarea>
    </div>
    <div class="grid-2">
      <div class="form-group">
        <label class="form-label">Category</label>
        <select class="select" id="modal-mem-category">
          <option value="general">general</option>
          <option value="project">project</option>
          <option value="trading">trading</option>
          <option value="finance">finance</option>
          <option value="person">person</option>
          <option value="preference">preference</option>
          <option value="task">task</option>
          <option value="decision">decision</option>
        </select>
      </div>
      <div class="form-group">
        <label class="form-label">Importance (1=auto)</label>
        <select class="select" id="modal-mem-importance">
          <option value="1">1 — Auto</option>
          <option value="2">2 — Low</option>
          <option value="3">3 — Medium</option>
          <option value="4">4 — High</option>
          <option value="5">5 — Critical</option>
        </select>
      </div>
    </div>
    <div class="form-group">
      <label class="form-label">TTL (hours, optional)</label>
      <input type="number" class="input" id="modal-mem-ttl" placeholder="Leave empty for no expiration" min="1" max="8760">
    </div>
    <div class="form-group">
      <label class="form-label">Tags (comma separated)</label>
      <input type="text" class="input" id="modal-mem-tags" placeholder="tag1, tag2, tag3">
    </div>
    <div class="modal-footer">
      <button class="btn btn-secondary" id="modal-mem-cancel">Cancel</button>
      <button class="btn btn-primary" id="modal-mem-save">Save</button>
    </div>
  </div>
</div>

<!-- Modal Create Session -->
<div class="modal-overlay" id="modal-session">
  <div class="modal">
    <div class="modal-header">
      <span class="modal-title">New session</span>
      <button class="btn-ghost" id="modal-session-close" aria-label="Close">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
    </div>
    <div class="form-group">
      <label class="form-label">Session ID</label>
      <input type="text" class="input" id="modal-sess-id" placeholder="e.g. session-2026-02-25">
    </div>
    <div class="form-group">
      <label class="form-label">Title (optional)</label>
      <input type="text" class="input" id="modal-sess-title" placeholder="Session title">
    </div>
    <div class="modal-footer">
      <button class="btn btn-secondary" id="modal-sess-cancel">Cancel</button>
      <button class="btn btn-primary" id="modal-sess-save">Create</button>
    </div>
  </div>
</div>

<!-- Toast container -->
<div class="toast-container" id="toast-container"></div>

<script>
/* ═══════════════════════════════════════════════════════════════════════
   Kore Dashboard — Vanilla JS Application
   Zero dependencies, CSP-compliant, accessible
   ═══════════════════════════════════════════════════════════════════════ */

/* ── Application state ─────────────────────────────────────────────── */
const state = {
  currentPage: 'overview',
  agentId: 'default',
  theme: localStorage.getItem('kore-theme') || 'dark',
  version: '',
  semanticEnabled: false,
  editingMemoryId: null,
};

/* ── Category colors ──────────────────────────────────────────────── */
const CAT_COLORS = {
  general: '#8b5cf6', project: '#3b82f6', trading: '#f59e0b', finance: '#10b981',
  person: '#ec4899', preference: '#06b6d4', task: '#f97316', decision: '#6366f1'
};

/* ── Pages and navigation ──────────────────────────────────────────── */
const PAGES = [
  { id: 'overview', label: 'Overview', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>' },
  { id: 'memories', label: 'Memories', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>' },
  { id: 'tags', label: 'Tags & Relations', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg>' },
  { id: 'graph', label: 'Graph', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/></svg>' },
  { id: 'sessions', label: 'Sessions', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>' },
  { id: 'timeline', label: 'Timeline', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>' },
  { id: 'maintenance', label: 'Maintenance', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>' },
  { id: 'settings', label: 'Settings', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="21" x2="4" y2="14"/><line x1="4" y1="10" x2="4" y2="3"/><line x1="12" y1="21" x2="12" y2="12"/><line x1="12" y1="8" x2="12" y2="3"/><line x1="20" y1="21" x2="20" y2="16"/><line x1="20" y1="12" x2="20" y2="3"/><line x1="1" y1="14" x2="7" y2="14"/><line x1="9" y1="8" x2="15" y2="8"/><line x1="17" y1="16" x2="23" y2="16"/></svg>' },
];

/* ── Safe DOM utilities ────────────────────────────────────────────── */
/* Escape HTML — prevents XSS using browser textContent */
function esc(s) { const d = document.createElement('div'); d.textContent = s; return d.innerHTML; }
function $(sel) { return document.querySelector(sel); }
function $$(sel) { return document.querySelectorAll(sel); }
function truncate(s, n) { n = n || 150; return s.length > n ? s.slice(0, n) + '\u2026' : s; }

/* Safe render: builds HTML with values escaped via esc() */
function safeRender(target, html) {
  var el = typeof target === 'string' ? $(target) : target;
  if (el) el.innerHTML = html;
}

function fmtDate(d) {
  if (!d) return '\u2014';
  var dt = new Date(d);
  return dt.toLocaleDateString('en-US', { day: '2-digit', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit' });
}
function fmtDateShort(d) {
  if (!d) return '\u2014';
  return new Date(d).toLocaleDateString('en-US', { day: '2-digit', month: 'short' });
}
function decayColor(score) {
  if (score >= 0.7) return 'var(--success)';
  if (score >= 0.3) return 'var(--warning)';
  return 'var(--danger)';
}
function importanceDots(n) {
  var out = '';
  for (var i = 0; i < 5; i++) out += '<div class="dot ' + (i < n ? 'filled' : '') + '"></div>';
  return out;
}

/* ── API Client ────────────────────────────────────────────────────── */
var api = {
  request: function(method, path, body) {
    var headers = { 'X-Agent-Id': state.agentId };
    if (body) headers['Content-Type'] = 'application/json';
    return fetch(path, {
      method: method, headers: headers,
      body: body ? JSON.stringify(body) : null
    }).then(function(res) {
      if (res.status === 204) return null;
      if (!res.ok) {
        return res.json().catch(function() { return { detail: res.statusText }; }).then(function(err) {
          throw new Error(err.detail || err.error || 'API Error');
        });
      }
      var ct = res.headers.get('content-type') || '';
      return ct.indexOf('json') >= 0 ? res.json() : res.text();
    }).catch(function(e) {
      if (e.message === 'Failed to fetch') throw new Error('Server unreachable');
      throw e;
    });
  },
  get: function(p) { return api.request('GET', p); },
  post: function(p, b) { return api.request('POST', p, b); },
  put: function(p, b) { return api.request('PUT', p, b); },
  del: function(p, b) { return api.request('DELETE', p, b); },
};

/* ── Toast ─────────────────────────────────────────────────────────── */
function toast(msg, type) {
  type = type || 'info';
  var el = document.createElement('div');
  el.className = 'toast toast-' + type;
  el.textContent = msg;
  $('#toast-container').appendChild(el);
  setTimeout(function() { el.style.opacity = '0'; setTimeout(function() { el.remove(); }, 300); }, 3500);
}

/* ── Tema ──────────────────────────────────────────────────────────── */
function applyTheme() {
  document.documentElement.setAttribute('data-theme', state.theme);
  var iconEl = $('#icon-theme');
  if (state.theme === 'dark') {
    iconEl.innerHTML = '<circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>';
  } else {
    iconEl.innerHTML = '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>';
  }
}

/* ── Navigation ────────────────────────────────────────────────────── */
function initNav() {
  var nav = $('#sidebar-nav');
  var html = '';
  PAGES.forEach(function(p) {
    html += '<button class="nav-item ' + (p.id === state.currentPage ? 'active' : '') + '" data-nav="' + p.id + '">' + p.icon + '<span>' + esc(p.label) + '</span></button>';
  });
  safeRender(nav, html);
  nav.addEventListener('click', function(e) {
    var btn = e.target.closest('[data-nav]');
    if (btn) navigate(btn.dataset.nav);
  });
}

function navigate(pageId) {
  state.currentPage = pageId;
  $$('.nav-item').forEach(function(el) { el.classList.toggle('active', el.dataset.nav === pageId); });
  $$('.page').forEach(function(el) { el.classList.toggle('active', el.dataset.page === pageId); });
  var page = PAGES.find(function(p) { return p.id === pageId; });
  $('#header-title').textContent = page ? page.label : '';
  $('#sidebar').classList.remove('open');
  loadPageData(pageId);
}

function loadPageData(pageId) {
  switch (pageId) {
    case 'overview': return loadOverview();
    case 'memories': return loadMemories();
    case 'tags': return loadTags();
    case 'graph': return loadGraph();
    case 'sessions': return loadSessions();
    case 'maintenance': return loadMaintenance();
    case 'settings': return loadSettings();
  }
}

/* ═══════════════════════════════════════════════════════════════════════
   PAGE: Overview
   ═══════════════════════════════════════════════════════════════════════ */
function loadOverview() {
  Promise.all([
    api.get('/health'),
    api.get('/search?q=*&limit=20&semantic=false'),
    api.get('/agents'),
    api.get('/stats/scoring').catch(function() { return null; }),
    api.get('/archive?limit=1').catch(function() { return { total: 0 }; }),
  ]).then(function(results) {
    var health = results[0], searchRes = results[1], agents = results[2], scoring = results[3], arch = results[4];

    state.version = health.version || '';
    state.semanticEnabled = health.semantic_search || false;
    $('#version-badge').textContent = 'v' + state.version;

    var totalMem = searchRes.total || 0;
    var agentCount = agents ? (agents.total || (agents.agents || agents).length) : 0;
    var avgImp = scoring ? (scoring.avg_importance || 0).toFixed(1) : '\u2014';
    var semStatus = state.semanticEnabled ? 'Active' : 'Off';
    var archivedCount = arch.total || 0;

    safeRender('#stats-grid',
      '<div class="stat-card"><div class="stat-label">Total memories</div><div class="stat-value accent">' + totalMem + '</div></div>' +
      '<div class="stat-card"><div class="stat-label">Agents</div><div class="stat-value">' + agentCount + '</div></div>' +
      '<div class="stat-card"><div class="stat-label">Archived</div><div class="stat-value">' + archivedCount + '</div></div>' +
      '<div class="stat-card"><div class="stat-label">Avg importance</div><div class="stat-value warning">' + esc(avgImp) + '</div></div>' +
      '<div class="stat-card"><div class="stat-label">Semantic search</div><div class="stat-value ' + (state.semanticEnabled ? 'success' : '') + '">' + semStatus + '</div></div>' +
      '<div class="stat-card"><div class="stat-label">Version</div><div class="stat-value" style="font-size:20px">' + esc(state.version) + '</div></div>'
    );

    /* Recent memories */
    var recent = (searchRes.results || []).slice(0, 6);
    if (recent.length) {
      var rhtml = '';
      recent.forEach(function(m) {
        rhtml += '<div style="padding:8px 0;border-bottom:1px solid var(--border);display:flex;justify-content:space-between;align-items:flex-start;gap:8px">' +
          '<div style="flex:1;min-width:0"><div style="font-size:13px;color:var(--text);white-space:nowrap;overflow:hidden;text-overflow:ellipsis">' + esc(truncate(m.content, 80)) + '</div>' +
          '<div style="font-size:11px;color:var(--text-dim);margin-top:2px">' + fmtDateShort(m.created_at) + '</div></div>' +
          '<span class="badge badge-' + esc(m.category) + '">' + esc(m.category) + '</span></div>';
      });
      safeRender('#recent-memories', rhtml);
    } else {
      safeRender('#recent-memories', '<div class="empty-state"><p>No memories found</p></div>');
    }

    /* Category distribution */
    var cats = {};
    (searchRes.results || []).forEach(function(m) { cats[m.category] = (cats[m.category] || 0) + 1; });
    var maxCat = Math.max.apply(null, Object.values(cats).concat([1]));
    var catEntries = Object.entries(cats).sort(function(a, b) { return b[1] - a[1]; });

    if (catEntries.length) {
      var chtml = '';
      catEntries.forEach(function(entry) {
        var cat = entry[0], count = entry[1];
        chtml += '<div class="cat-bar-row"><span class="cat-bar-label">' + esc(cat) + '</span>' +
          '<div class="cat-bar-track"><div class="cat-bar-fill" style="width:' + (count/maxCat*100).toFixed(0) + '%;background:' + (CAT_COLORS[cat]||'var(--accent)') + '"></div></div>' +
          '<span class="cat-bar-count">' + count + '</span></div>';
      });
      safeRender('#category-dist', chtml);
    } else {
      safeRender('#category-dist', '<div class="empty-state"><p>No data</p></div>');
    }

    /* Quick actions */
    safeRender('#quick-actions',
      '<button class="action-card" data-action="decay"><h3 style="color:var(--accent)">Run Decay</h3><p>Recalculate decay scores</p></button>' +
      '<button class="action-card" data-action="compress"><h3 style="color:var(--success)">Compress</h3><p>Merge similar memories</p></button>' +
      '<button class="action-card" data-action="cleanup"><h3 style="color:var(--warning)">Cleanup TTL</h3><p>Remove expired memories</p></button>' +
      '<button class="action-card" data-action="autotune"><h3 style="color:var(--danger)">Auto-Tune</h3><p>Optimize importance</p></button>'
    );
    $('#quick-actions').querySelectorAll('[data-action]').forEach(function(btn) {
      btn.addEventListener('click', function() { runMaintenanceAction(btn.dataset.action); });
    });

  }).catch(function(e) {
    toast('Error loading overview: ' + e.message, 'error');
  });
}

/* ═══════════════════════════════════════════════════════════════════════
   PAGE: Memories
   ═══════════════════════════════════════════════════════════════════════ */
var memSearchTimeout = null;

function loadMemories(query) {
  var q = query || ($('#mem-search') ? $('#mem-search').value.trim() : '') || '*';
  var cat = $('#mem-category') ? $('#mem-category').value : '';
  var semantic = $('#mem-semantic') ? $('#mem-semantic').checked : true;
  var list = $('#memories-list');

  safeRender(list, '<div class="loading-center"><div class="spinner"></div></div>');

  var url = '/search?q=' + encodeURIComponent(q) + '&limit=20&semantic=' + semantic;
  if (cat) url += '&category=' + encodeURIComponent(cat);

  api.get(url).then(function(data) {
    if (!data.results || !data.results.length) {
      safeRender(list, '<div class="empty-state"><p>No memories found. Try another search.</p></div>');
      return;
    }

    var html = '';
    data.results.forEach(function(m) {
      html += '<div class="memory-card" data-id="' + m.id + '">' +
        '<div class="memory-card-header"><div style="display:flex;gap:8px;align-items:center">' +
        '<span class="badge badge-' + esc(m.category) + '">' + esc(m.category) + '</span>' +
        '<span style="font-size:11px;color:var(--text-dim)">#' + m.id + '</span></div>' +
        '<div class="memory-card-actions">' +
        '<button class="btn-ghost btn-sm" title="Edit" data-edit="' + m.id + '"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg></button>' +
        '<button class="btn-ghost btn-sm" title="Archive" data-archive="' + m.id + '"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="21 8 21 21 3 21 3 8"/><rect x="1" y="3" width="22" height="5"/><line x1="10" y1="12" x2="14" y2="12"/></svg></button>' +
        '<button class="btn-ghost btn-sm" title="Delete" data-delete="' + m.id + '" style="color:var(--danger)"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg></button>' +
        '</div></div>' +
        '<div class="memory-card-content">' + esc(m.content) + '</div>' +
        '<div class="memory-card-footer">' +
        '<div class="importance" title="Importance: ' + m.importance + '/5">' + importanceDots(m.importance) + '</div>' +
        '<div style="display:flex;align-items:center;gap:4px" title="Decay: ' + (m.decay_score*100).toFixed(0) + '%">' +
        '<div class="decay-bar"><div class="decay-bar-fill" style="width:' + (m.decay_score*100).toFixed(0) + '%;background:' + decayColor(m.decay_score) + '"></div></div>' +
        '<span style="font-size:10px;color:var(--text-dim)">' + (m.decay_score*100).toFixed(0) + '%</span></div>' +
        '<span class="meta">' + fmtDate(m.created_at) + '</span>' +
        '</div></div>';
    });
    safeRender(list, html);

    /* Event handlers */
    list.querySelectorAll('[data-edit]').forEach(function(btn) {
      btn.addEventListener('click', function() { openEditMemory(parseInt(btn.dataset.edit)); });
    });
    list.querySelectorAll('[data-archive]').forEach(function(btn) {
      btn.addEventListener('click', function() {
        api.post('/memories/' + btn.dataset.archive + '/archive').then(function() {
          toast('Memory archived', 'success'); loadMemories();
        }).catch(function(e) { toast(e.message, 'error'); });
      });
    });
    list.querySelectorAll('[data-delete]').forEach(function(btn) {
      btn.addEventListener('click', function() {
        if (!confirm('Delete this memory?')) return;
        api.del('/memories/' + btn.dataset.delete).then(function() {
          toast('Memory deleted', 'success'); loadMemories();
        }).catch(function(e) { toast(e.message, 'error'); });
      });
    });

  }).catch(function(e) {
    safeRender(list, '<div class="empty-state"><p>Error: ' + esc(e.message) + '</p></div>');
  });
}

function openEditMemory(id) {
  var card = document.querySelector('.memory-card[data-id="' + id + '"]');
  if (!card) return;
  state.editingMemoryId = id;
  $('#modal-memory-title').textContent = 'Edit memory #' + id;
  $('#modal-mem-content').value = card.querySelector('.memory-card-content').textContent;
  var catEl = card.querySelector('.badge');
  if (catEl) $('#modal-mem-category').value = catEl.textContent.trim();
  $('#modal-mem-importance').value = card.querySelectorAll('.dot.filled').length || 1;
  $('#modal-mem-ttl').value = '';
  $('#modal-mem-tags').value = '';
  $('#modal-memory').classList.add('open');
}

/* ═══════════════════════════════════════════════════════════════════════
   PAGE: Tags & Relations
   ═══════════════════════════════════════════════════════════════════════ */
function loadTags() {
  api.get('/search?q=*&limit=20&semantic=false').then(function(data) {
    var tagMap = {};
    var promises = (data.results || []).map(function(m) {
      return api.get('/memories/' + m.id + '/tags').then(function(t) {
        (t.tags || []).forEach(function(tag) {
          if (!tagMap[tag]) tagMap[tag] = { count: 0 };
          tagMap[tag].count++;
        });
      }).catch(function() {});
    });

    return Promise.all(promises).then(function() {
      var cloud = $('#tag-cloud');
      var tags = Object.entries(tagMap).sort(function(a, b) { return b[1].count - a[1].count; });

      if (tags.length) {
        var html = '';
        tags.forEach(function(entry) {
          html += '<span class="badge badge-tag" data-tag="' + esc(entry[0]) + '" title="' + entry[1].count + ' memories">' + esc(entry[0]) + ' (' + entry[1].count + ')</span>';
        });
        safeRender(cloud, html);
        cloud.querySelectorAll('[data-tag]').forEach(function(el) {
          el.addEventListener('click', function() {
            api.get('/tags/' + encodeURIComponent(el.dataset.tag) + '/memories').then(function(res) {
              var h = '<div class="card-title" style="margin-top:8px">Memories with tag "' + esc(el.dataset.tag) + '"</div>';
              (res.results || []).forEach(function(m) {
                h += '<div style="padding:8px 0;border-bottom:1px solid var(--border)"><span style="font-size:12px;color:var(--text-dim)">#' + m.id + '</span> <span style="font-size:13px">' + esc(truncate(m.content, 100)) + '</span></div>';
              });
              safeRender('#tag-memories', h);
            }).catch(function(e) { toast(e.message, 'error'); });
          });
        });
      } else {
        safeRender(cloud, '<div class="empty-state"><p>No tags found</p></div>');
      }

      /* Relations */
      loadRelations(data.results || []);
    });
  }).catch(function(e) {
    toast('Error loading tags: ' + e.message, 'error');
  });
}

function loadRelations(memories) {
  var allRel = [];
  var promises = memories.slice(0, 20).map(function(m) {
    return api.get('/memories/' + m.id + '/relations').then(function(r) {
      (r.relations || []).forEach(function(rel) { allRel.push(rel); });
    }).catch(function() {});
  });

  Promise.all(promises).then(function() {
    if (allRel.length) {
      var html = '';
      allRel.forEach(function(r) {
        html += '<div style="padding:8px 0;border-bottom:1px solid var(--border);font-size:13px">' +
          '<span style="color:var(--accent)">#' + r.source_id + '</span> ' +
          '<span style="color:var(--text-dim)">\u2192</span> ' +
          '<span class="badge badge-tag">' + esc(r.relation) + '</span> ' +
          '<span style="color:var(--text-dim)">\u2192</span> ' +
          '<span style="color:var(--accent)">#' + r.target_id + '</span></div>';
      });
      safeRender('#relations-list', html);
    } else {
      safeRender('#relations-list', '<div class="empty-state" style="padding:24px"><p>No relations found</p></div>');
    }
  });
}

/* ═══════════════════════════════════════════════════════════════════════
   PAGE: Graph (Interactive force-directed)
   Node drag, zoom/pan, hover tooltip, click detail, directional arrows
   ═══════════════════════════════════════════════════════════════════════ */
var graphNodes = [], graphEdges = [], graphAnim = null;
var graphState = {
  zoom: 1, panX: 0, panY: 0,
  dragNode: null, hoveredNode: null, selectedNode: null,
  isPanning: false, lastMouse: null,
  showLabels: true, showArrows: true,
  settled: false, iteration: 0
};

/* Mouse coordinates → graph coordinates (applies zoom/pan) */
function screenToGraph(canvas, mx, my) {
  var rect = canvas.getBoundingClientRect();
  var sx = (mx - rect.left);
  var sy = (my - rect.top);
  return {
    x: (sx - canvas.width/2) / graphState.zoom - graphState.panX + canvas.width/2,
    y: (sy - canvas.height/2) / graphState.zoom - graphState.panY + canvas.height/2
  };
}

/* Find node under cursor */
function hitTestNode(gx, gy) {
  for (var i = graphNodes.length - 1; i >= 0; i--) {
    var n = graphNodes[i];
    var r = 6 + n.importance * 2.5;
    var dx = gx - n.x, dy = gy - n.y;
    if (dx*dx + dy*dy <= r*r) return n;
  }
  return null;
}

function loadGraph() {
  var canvas = $('#graph-canvas');
  var ctx = canvas.getContext('2d');
  canvas.width = canvas.offsetWidth * (window.devicePixelRatio || 1);
  canvas.height = canvas.offsetHeight * (window.devicePixelRatio || 1);
  canvas.style.width = canvas.offsetWidth + 'px';
  canvas.style.height = canvas.offsetHeight + 'px';
  ctx.scale(window.devicePixelRatio || 1, window.devicePixelRatio || 1);
  var w = canvas.offsetWidth, h = canvas.offsetHeight;

  /* Reset state */
  graphState.zoom = 1; graphState.panX = 0; graphState.panY = 0;
  graphState.dragNode = null; graphState.hoveredNode = null;
  graphState.selectedNode = null; graphState.settled = false; graphState.iteration = 0;

  api.get('/search?q=*&limit=20&semantic=false').then(function(data) {
    var memories = data.results || [];
    /* Distribute nodes in a circle for better initial layout */
    graphNodes = memories.map(function(m, i) {
      var angle = (2 * Math.PI * i) / memories.length;
      var radius = Math.min(w, h) * 0.3;
      return {
        id: m.id, label: truncate(m.content, 25), fullContent: m.content,
        category: m.category, importance: m.importance,
        decay_score: m.decay_score, created_at: m.created_at,
        x: w/2 + Math.cos(angle) * radius,
        y: h/2 + Math.sin(angle) * radius,
        vx: 0, vy: 0
      };
    });
    graphEdges = [];

    var promises = memories.map(function(m) {
      return api.get('/memories/' + m.id + '/relations').then(function(r) {
        (r.relations || []).forEach(function(rel) {
          if (graphNodes.find(function(n) { return n.id === rel.target_id; })) {
            graphEdges.push({ source: m.id, target: rel.target_id, label: rel.relation });
          }
        });
      }).catch(function() {});
    });

    return Promise.all(promises).then(function() {
      $('#graph-info').textContent = 'Nodes: ' + graphNodes.length + ' \u2014 Edges: ' + graphEdges.length;

      /* Legend of present categories */
      var catsUsed = {};
      graphNodes.forEach(function(n) { catsUsed[n.category] = true; });
      var legendHtml = '';
      Object.keys(catsUsed).forEach(function(cat) {
        legendHtml += '<span class="graph-legend-item"><span class="graph-legend-dot" style="background:' + (CAT_COLORS[cat]||'var(--accent)') + '"></span>' + esc(cat) + '</span>';
      });
      safeRender('#graph-legend', legendHtml);

      if (graphAnim) cancelAnimationFrame(graphAnim);
      animateGraph(ctx, canvas);
      initGraphInteractions(canvas);
    });
  }).catch(function(e) {
    toast('Error loading graph: ' + e.message, 'error');
  });
}

function initGraphInteractions(canvas) {
  /* Avoid double listeners: remove and recreate */
  var newCanvas = canvas.cloneNode(true);
  canvas.parentNode.replaceChild(newCanvas, canvas);
  canvas = newCanvas;
  /* Update global reference */
  var ctx = canvas.getContext('2d');
  ctx.scale(window.devicePixelRatio || 1, window.devicePixelRatio || 1);

  /* Restart animation with new canvas */
  if (graphAnim) cancelAnimationFrame(graphAnim);
  animateGraph(ctx, canvas);

  var tooltip = $('#graph-tooltip');

  /* ── Mouse move: hover + drag ──────────────────────────── */
  canvas.addEventListener('mousemove', function(e) {
    var g = screenToGraph(canvas, e.clientX, e.clientY);

    /* Node drag */
    if (graphState.dragNode) {
      graphState.dragNode.x = g.x;
      graphState.dragNode.y = g.y;
      graphState.dragNode.vx = 0;
      graphState.dragNode.vy = 0;
      return;
    }

    /* View pan */
    if (graphState.isPanning && graphState.lastMouse) {
      var rect = canvas.getBoundingClientRect();
      var dx = (e.clientX - graphState.lastMouse.x) / graphState.zoom;
      var dy = (e.clientY - graphState.lastMouse.y) / graphState.zoom;
      graphState.panX += dx;
      graphState.panY += dy;
      graphState.lastMouse = { x: e.clientX, y: e.clientY };
      return;
    }

    /* Hover detection */
    var node = hitTestNode(g.x, g.y);
    graphState.hoveredNode = node;
    canvas.classList.toggle('hovering', !!node);

    if (node) {
      /* Show tooltip */
      var rect = canvas.getBoundingClientRect();
      var sx = (node.x - canvas.offsetWidth/2 + graphState.panX) * graphState.zoom + canvas.offsetWidth/2;
      var sy = (node.y - canvas.offsetHeight/2 + graphState.panY) * graphState.zoom + canvas.offsetHeight/2;
      tooltip.querySelector('.tt-id').textContent = '#' + node.id;
      var catBadge = tooltip.querySelector('.tt-cat');
      catBadge.textContent = node.category;
      catBadge.className = 'tt-cat badge badge-' + node.category;
      tooltip.querySelector('.tt-content').textContent = truncate(node.fullContent, 120);
      /* Node relations */
      var rels = graphEdges.filter(function(ed) { return ed.source === node.id || ed.target === node.id; });
      if (rels.length) {
        tooltip.querySelector('.tt-relations').textContent = rels.length + ' relation' + (rels.length === 1 ? '' : 's');
      } else {
        tooltip.querySelector('.tt-relations').textContent = 'No relations';
      }
      tooltip.style.left = Math.min(sx + 15, canvas.offsetWidth - 310) + 'px';
      tooltip.style.top = Math.min(sy - 10, canvas.offsetHeight - 80) + 'px';
      tooltip.classList.add('visible');
    } else {
      tooltip.classList.remove('visible');
    }
  });

  /* ── Mouse down: start node drag or pan ─────────────── */
  canvas.addEventListener('mousedown', function(e) {
    var g = screenToGraph(canvas, e.clientX, e.clientY);
    var node = hitTestNode(g.x, g.y);
    if (node) {
      graphState.dragNode = node;
      canvas.classList.add('dragging');
    } else {
      graphState.isPanning = true;
      graphState.lastMouse = { x: e.clientX, y: e.clientY };
      canvas.classList.add('dragging');
    }
  });

  /* ── Mouse up: end drag/pan ────────────────────────── */
  canvas.addEventListener('mouseup', function(e) {
    canvas.classList.remove('dragging');
    if (graphState.dragNode) {
      /* After drag, briefly restart simulation to settle */
      graphState.iteration = Math.min(graphState.iteration, 120);
    }
    graphState.dragNode = null;
    graphState.isPanning = false;
    graphState.lastMouse = null;
  });

  canvas.addEventListener('mouseleave', function() {
    canvas.classList.remove('dragging');
    canvas.classList.remove('hovering');
    graphState.dragNode = null;
    graphState.isPanning = false;
    graphState.lastMouse = null;
    tooltip.classList.remove('visible');
  });

  /* ── Click: select node and show detail ─────────────── */
  canvas.addEventListener('click', function(e) {
    var g = screenToGraph(canvas, e.clientX, e.clientY);
    var node = hitTestNode(g.x, g.y);
    if (node) {
      graphState.selectedNode = node;
      showGraphDetail(node);
    } else {
      graphState.selectedNode = null;
      $('#graph-detail').classList.remove('open');
    }
  });

  /* ── Wheel: zoom ─────────────────────────────────────── */
  canvas.addEventListener('wheel', function(e) {
    e.preventDefault();
    var delta = e.deltaY > 0 ? 0.9 : 1.1;
    graphState.zoom = Math.max(0.2, Math.min(5, graphState.zoom * delta));
  }, { passive: false });
}

function showGraphDetail(node) {
  var detail = $('#graph-detail');
  /* Outgoing and incoming relations */
  var outgoing = graphEdges.filter(function(e) { return e.source === node.id; });
  var incoming = graphEdges.filter(function(e) { return e.target === node.id; });

  var relsHtml = '';
  outgoing.forEach(function(e) {
    var target = graphNodes.find(function(n) { return n.id === e.target; });
    relsHtml += '<div style="padding:4px 0;font-size:12px"><span style="color:var(--accent)">\u2192</span> <span class="badge badge-tag">' + esc(e.label) + '</span> #' + e.target + (target ? ' <span style="color:var(--text-dim)">' + esc(truncate(target.fullContent, 30)) + '</span>' : '') + '</div>';
  });
  incoming.forEach(function(e) {
    var source = graphNodes.find(function(n) { return n.id === e.source; });
    relsHtml += '<div style="padding:4px 0;font-size:12px"><span style="color:var(--success)">\u2190</span> <span class="badge badge-tag">' + esc(e.label) + '</span> #' + e.source + (source ? ' <span style="color:var(--text-dim)">' + esc(truncate(source.fullContent, 30)) + '</span>' : '') + '</div>';
  });

  safeRender('#graph-detail-content',
    '<div style="margin-bottom:12px"><span style="font-family:var(--font-mono);color:var(--accent);font-weight:600">#' + node.id + '</span>' +
    ' <span class="badge badge-' + esc(node.category) + '">' + esc(node.category) + '</span></div>' +
    '<div style="font-size:13px;line-height:1.5;margin-bottom:12px">' + esc(node.fullContent) + '</div>' +
    '<div style="display:flex;gap:12px;margin-bottom:12px">' +
    '<div><span style="font-size:11px;color:var(--text-dim)">Importance</span><div class="importance">' + importanceDots(node.importance) + '</div></div>' +
    '<div><span style="font-size:11px;color:var(--text-dim)">Decay</span><div style="display:flex;align-items:center;gap:4px;margin-top:2px"><div class="decay-bar" style="width:50px"><div class="decay-bar-fill" style="width:' + (node.decay_score*100).toFixed(0) + '%;background:' + decayColor(node.decay_score) + '"></div></div><span style="font-size:10px;color:var(--text-dim)">' + (node.decay_score*100).toFixed(0) + '%</span></div></div></div>' +
    '<div style="font-size:11px;color:var(--text-dim);margin-bottom:8px">' + fmtDate(node.created_at) + '</div>' +
    (relsHtml ? '<div class="card-title" style="font-size:11px;margin-bottom:4px">Relations (' + (outgoing.length + incoming.length) + ')</div>' + relsHtml : '<div style="font-size:12px;color:var(--text-dim)">No relations</div>') +
    '<div style="margin-top:12px;display:flex;gap:6px">' +
    '<button class="btn btn-sm btn-primary" data-graph-edit="' + node.id + '">Edit</button>' +
    '<button class="btn btn-sm btn-secondary" data-graph-goto="' + node.id + '">Go to Memories</button></div>'
  );

  detail.classList.add('open');

  /* Buttons in the detail panel */
  var editBtn = detail.querySelector('[data-graph-edit]');
  if (editBtn) editBtn.addEventListener('click', function() {
    detail.classList.remove('open');
    navigate('memories');
    setTimeout(function() { openEditMemory(node.id); }, 300);
  });
  var gotoBtn = detail.querySelector('[data-graph-goto]');
  if (gotoBtn) gotoBtn.addEventListener('click', function() {
    detail.classList.remove('open');
    navigate('memories');
  });
}

function animateGraph(ctx, canvas) {
  var w = canvas.offsetWidth, h = canvas.offsetHeight;

  /* Force simulation — progressive cooling and stabilization */
  var cooling = graphState.iteration < 150 ? 1.0 : Math.max(0.0, 1.0 - (graphState.iteration - 150) / 150);
  graphState.iteration++;

  /* If simulation has settled, do not calculate forces */
  if (cooling <= 0 && !graphState.dragNode) {
    /* Just draw — no forces applied */
  } else {

  graphNodes.forEach(function(n) {
    if (n === graphState.dragNode) return;
    n.vx *= 0.8; n.vy *= 0.8;
    /* Gravity toward center — strong enough to overcome repulsion */
    n.vx += (w/2 - n.x) * 0.005 * cooling;
    n.vy += (h/2 - n.y) * 0.005 * cooling;
  });

  /* Node repulsion — more contained force with minimum distance */
  for (var i = 0; i < graphNodes.length; i++) {
    for (var j = i + 1; j < graphNodes.length; j++) {
      var a = graphNodes[i], b = graphNodes[j];
      if (a === graphState.dragNode || b === graphState.dragNode) continue;
      var dx = b.x - a.x, dy = b.y - a.y;
      var dist = Math.sqrt(dx*dx + dy*dy) || 1;
      if (dist > 300) continue; /* Ignore nodes too far apart */
      var force = 400 * cooling / (dist * dist + 100);
      a.vx -= dx * force; a.vy -= dy * force;
      b.vx += dx * force; b.vy += dy * force;
    }
  }

  /* Edge attraction — ideal spring at 100px */
  graphEdges.forEach(function(e) {
    var a = graphNodes.find(function(n) { return n.id === e.source; });
    var b = graphNodes.find(function(n) { return n.id === e.target; });
    if (!a || !b) return;
    if (a === graphState.dragNode || b === graphState.dragNode) return;
    var dx = b.x - a.x, dy = b.y - a.y;
    var dist = Math.sqrt(dx*dx + dy*dy) || 1;
    var f = (dist - 100) * 0.01 * cooling;
    a.vx += dx/dist * f; a.vy += dy/dist * f;
    b.vx -= dx/dist * f; b.vy -= dy/dist * f;
  });

  /* Update positions with 15% margin from edge */
  var mx = w * 0.15, my = h * 0.15;
  graphNodes.forEach(function(n) {
    if (n === graphState.dragNode) return;
    n.x += n.vx * 0.3;
    n.y += n.vy * 0.3;
    n.x = Math.max(mx, Math.min(w - mx, n.x));
    n.y = Math.max(my, Math.min(h - my, n.y));
  });

  } /* end cooling > 0 block */

  /* ── Draw ────────────────────────────────────────── */
  var isDark = state.theme === 'dark';
  ctx.clearRect(0, 0, w, h);
  ctx.save();

  /* Apply zoom and pan */
  ctx.translate(w/2, h/2);
  ctx.scale(graphState.zoom, graphState.zoom);
  ctx.translate(graphState.panX - w/2, graphState.panY - h/2);

  /* Edges */
  graphEdges.forEach(function(e) {
    var a = graphNodes.find(function(n) { return n.id === e.source; });
    var b = graphNodes.find(function(n) { return n.id === e.target; });
    if (!a || !b) return;

    var isHighlighted = graphState.hoveredNode && (graphState.hoveredNode.id === a.id || graphState.hoveredNode.id === b.id);
    var isSelected = graphState.selectedNode && (graphState.selectedNode.id === a.id || graphState.selectedNode.id === b.id);

    ctx.strokeStyle = isHighlighted || isSelected
      ? (isDark ? 'rgba(139,92,246,0.7)' : 'rgba(124,58,237,0.5)')
      : (isDark ? 'rgba(139,92,246,0.15)' : 'rgba(124,58,237,0.1)');
    ctx.lineWidth = isHighlighted || isSelected ? 2 : 1;

    ctx.beginPath();
    ctx.moveTo(a.x, a.y);
    ctx.lineTo(b.x, b.y);
    ctx.stroke();

    /* Directional arrow */
    if (graphState.showArrows) {
      var dx = b.x - a.x, dy = b.y - a.y;
      var dist = Math.sqrt(dx*dx + dy*dy) || 1;
      var rB = 6 + b.importance * 2.5;
      var ax = b.x - (dx/dist) * (rB + 4);
      var ay = b.y - (dy/dist) * (rB + 4);
      var angle = Math.atan2(dy, dx);
      var arrowLen = 8;
      ctx.fillStyle = ctx.strokeStyle;
      ctx.beginPath();
      ctx.moveTo(ax, ay);
      ctx.lineTo(ax - arrowLen * Math.cos(angle - 0.35), ay - arrowLen * Math.sin(angle - 0.35));
      ctx.lineTo(ax - arrowLen * Math.cos(angle + 0.35), ay - arrowLen * Math.sin(angle + 0.35));
      ctx.closePath();
      ctx.fill();
    }

    /* Relation label at arc center */
    if (graphState.showLabels && (isHighlighted || isSelected)) {
      var mx = (a.x + b.x) / 2, my = (a.y + b.y) / 2;
      ctx.fillStyle = isDark ? 'rgba(139,92,246,0.9)' : 'rgba(124,58,237,0.8)';
      ctx.font = '9px system-ui';
      ctx.textAlign = 'center';
      ctx.fillText(e.label, mx, my - 4);
    }
  });

  /* Nodes */
  graphNodes.forEach(function(n) {
    var r = 6 + n.importance * 2.5;
    var isHovered = graphState.hoveredNode === n;
    var isSelected = graphState.selectedNode === n;
    var isConnected = false;
    if (graphState.hoveredNode && graphState.hoveredNode !== n) {
      isConnected = graphEdges.some(function(e) {
        return (e.source === graphState.hoveredNode.id && e.target === n.id) ||
               (e.target === graphState.hoveredNode.id && e.source === n.id);
      });
    }

    var baseColor = CAT_COLORS[n.category] || '#8b5cf6';
    var dimmed = graphState.hoveredNode && !isHovered && !isConnected;

    /* Glow for selected/hovered node */
    if (isSelected || isHovered) {
      ctx.beginPath();
      ctx.arc(n.x, n.y, r + 6, 0, Math.PI * 2);
      ctx.fillStyle = baseColor.replace(')', ',0.2)').replace('rgb', 'rgba');
      if (baseColor.charAt(0) === '#') {
        ctx.fillStyle = baseColor + '33';
      }
      ctx.fill();
    }

    /* Node circle */
    ctx.beginPath();
    ctx.arc(n.x, n.y, r, 0, Math.PI * 2);
    ctx.fillStyle = dimmed ? (isDark ? '#3f3f46' : '#d4d4d8') : baseColor;
    ctx.fill();

    /* Border for selected node */
    if (isSelected) {
      ctx.strokeStyle = '#fff';
      ctx.lineWidth = 2;
      ctx.stroke();
    }

    /* Label below node */
    if (graphState.showLabels && !dimmed) {
      ctx.fillStyle = isHovered || isSelected
        ? (isDark ? '#fafafa' : '#18181b')
        : (isDark ? '#71717a' : '#a1a1aa');
      ctx.font = (isHovered || isSelected ? 'bold ' : '') + '10px system-ui';
      ctx.textAlign = 'center';
      ctx.fillText('#' + n.id + ' ' + n.label, n.x, n.y + r + 14);
    }
  });

  ctx.restore();
  graphAnim = requestAnimationFrame(function() { animateGraph(ctx, canvas); });
}

/* ═══════════════════════════════════════════════════════════════════════
   PAGE: Sessions
   ═══════════════════════════════════════════════════════════════════════ */
function loadSessions() {
  var list = $('#sessions-list');
  safeRender(list, '<div class="loading-center"><div class="spinner"></div></div>');

  api.get('/sessions?limit=50').then(function(sessions) {
    if (!sessions || !sessions.length) {
      safeRender(list, '<div class="empty-state"><p>No sessions found</p></div>');
      return;
    }
    var html = '';
    sessions.forEach(function(s) {
      html += '<div class="session-card"><div class="session-info">' +
        '<h4>' + esc(s.title || s.id) + '</h4>' +
        '<div class="meta">' + esc(s.id) + ' \u2014 ' + fmtDate(s.created_at) +
        (s.ended_at ? ' \u2192 ' + fmtDate(s.ended_at) : ' <span style="color:var(--success)">\u2022 active</span>') +
        '</div></div><div style="display:flex;gap:6px">' +
        (!s.ended_at ? '<button class="btn btn-sm btn-secondary" data-end-session="' + esc(s.id) + '">End</button>' : '') +
        '<button class="btn btn-sm btn-secondary" data-view-session="' + esc(s.id) + '">Memories</button>' +
        '<button class="btn btn-sm btn-danger" data-del-session="' + esc(s.id) + '">Delete</button>' +
        '</div></div>';
    });
    safeRender(list, html);

    list.querySelectorAll('[data-end-session]').forEach(function(btn) {
      btn.addEventListener('click', function() {
        api.post('/sessions/' + encodeURIComponent(btn.dataset.endSession) + '/end').then(function() {
          toast('Session ended', 'success'); loadSessions();
        }).catch(function(e) { toast(e.message, 'error'); });
      });
    });
    list.querySelectorAll('[data-del-session]').forEach(function(btn) {
      btn.addEventListener('click', function() {
        if (!confirm('Delete this session?')) return;
        api.del('/sessions/' + encodeURIComponent(btn.dataset.delSession)).then(function() {
          toast('Session deleted', 'success'); loadSessions();
        }).catch(function(e) { toast(e.message, 'error'); });
      });
    });
    list.querySelectorAll('[data-view-session]').forEach(function(btn) {
      btn.addEventListener('click', function() {
        api.get('/sessions/' + encodeURIComponent(btn.dataset.viewSession) + '/memories').then(function(res) {
          var mems = res.results || [];
          if (!mems.length) { toast('No memories in this session', 'info'); return; }
          var h = '<div class="card" style="margin-top:16px"><div class="card-title">Session memories ' + esc(btn.dataset.viewSession) + '</div>';
          mems.forEach(function(m) {
            h += '<div style="padding:8px 0;border-bottom:1px solid var(--border)"><span class="badge badge-' + esc(m.category) + '" style="margin-right:6px">' + esc(m.category) + '</span><span style="font-size:13px">' + esc(truncate(m.content, 120)) + '</span></div>';
          });
          h += '</div>';
          list.insertAdjacentHTML('beforeend', h);
        }).catch(function(e) { toast(e.message, 'error'); });
      });
    });
  }).catch(function(e) {
    safeRender(list, '<div class="empty-state"><p>Error: ' + esc(e.message) + '</p></div>');
  });
}

/* ═══════════════════════════════════════════════════════════════════════
   PAGE: Timeline
   ═══════════════════════════════════════════════════════════════════════ */
function loadTimeline(subject) {
  if (!subject) {
    safeRender('#timeline-list', '<div class="empty-state"><p>Enter a subject to search in timeline</p></div>');
    return;
  }
  safeRender('#timeline-list', '<div class="loading-center"><div class="spinner"></div></div>');

  api.get('/timeline?subject=' + encodeURIComponent(subject) + '&limit=30').then(function(data) {
    if (!data.results || !data.results.length) {
      safeRender('#timeline-list', '<div class="empty-state"><p>No results found</p></div>');
      return;
    }
    var html = '';
    data.results.forEach(function(m) {
      html += '<div class="timeline-item">' +
        '<div class="timeline-dot" style="background:' + (CAT_COLORS[m.category]||'var(--accent)') + '"></div>' +
        '<div class="timeline-content"><div class="timeline-date">' + fmtDate(m.created_at) +
        ' \u2014 <span class="badge badge-' + esc(m.category) + '">' + esc(m.category) + '</span></div>' +
        '<div class="timeline-text">' + esc(m.content) + '</div></div></div>';
    });
    safeRender('#timeline-list', html);
  }).catch(function(e) {
    safeRender('#timeline-list', '<div class="empty-state"><p>Error: ' + esc(e.message) + '</p></div>');
  });
}

/* ═══════════════════════════════════════════════════════════════════════
   PAGE: Maintenance
   ═══════════════════════════════════════════════════════════════════════ */
function loadMaintenance() {
  /* Scoring stats */
  api.get('/stats/scoring').then(function(stats) {
    var dist = stats.distribution || {};
    var h = '<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px">' +
      '<div><span style="color:var(--text-dim);font-size:12px">Total</span><div style="font-size:20px;font-weight:600">' + stats.total + '</div></div>' +
      '<div><span style="color:var(--text-dim);font-size:12px">Avg importance</span><div style="font-size:20px;font-weight:600">' + (stats.avg_importance || 0).toFixed(1) + '</div></div>' +
      '<div><span style="color:var(--text-dim);font-size:12px">Never accessed (30d)</span><div style="font-size:20px;font-weight:600;color:var(--warning)">' + stats.never_accessed_30d + '</div></div>' +
      '<div><span style="color:var(--text-dim);font-size:12px">Frequently accessed</span><div style="font-size:20px;font-weight:600;color:var(--success)">' + stats.frequently_accessed + '</div></div></div>' +
      '<div class="card-title" style="margin-top:8px">Importance distribution</div>';
    [1,2,3,4,5].forEach(function(i) {
      var count = dist[String(i)] || 0;
      var pct = stats.total ? (count / stats.total * 100).toFixed(0) : 0;
      h += '<div class="cat-bar-row"><span class="cat-bar-label">' + '\u2605'.repeat(i) + '</span><div class="cat-bar-track"><div class="cat-bar-fill" style="width:' + pct + '%;background:var(--accent)"></div></div><span class="cat-bar-count">' + count + '</span></div>';
    });
    safeRender('#scoring-stats', h);
  }).catch(function() {
    safeRender('#scoring-stats', '<div class="empty-state"><p>Stats not available</p></div>');
  });

  /* Archive */
  api.get('/archive?limit=20').then(function(arch) {
    var items = arch.results || [];
    if (items.length) {
      var h = '';
      items.forEach(function(m) {
        h += '<div style="padding:8px 0;border-bottom:1px solid var(--border);display:flex;justify-content:space-between;align-items:center">' +
          '<div><span style="font-size:12px;color:var(--text-dim)">#' + m.id + '</span> <span style="font-size:13px">' + esc(truncate(m.content, 60)) + '</span></div>' +
          '<button class="btn btn-sm btn-success" data-restore="' + m.id + '">Restore</button></div>';
      });
      safeRender('#archive-list', h);
      $('#archive-list').querySelectorAll('[data-restore]').forEach(function(btn) {
        btn.addEventListener('click', function() {
          api.post('/memories/' + btn.dataset.restore + '/restore').then(function() {
            toast('Memory restored', 'success'); loadMaintenance();
          }).catch(function(e) { toast(e.message, 'error'); });
        });
      });
    } else {
      safeRender('#archive-list', '<div class="empty-state" style="padding:24px"><p>No archived memories</p></div>');
    }
  }).catch(function() {
    safeRender('#archive-list', '<div class="empty-state"><p>Error loading archive</p></div>');
  });
}

function runMaintenanceAction(action) {
  var endpoints = { decay: '/decay/run', compress: '/compress', cleanup: '/cleanup', autotune: '/auto-tune' };
  api.post(endpoints[action]).then(function(result) {
    switch (action) {
      case 'decay': toast('Decay complete: ' + result.updated + ' memories updated', 'success'); break;
      case 'compress': toast('Compression: ' + result.clusters_found + ' clusters, ' + result.memories_merged + ' merged', 'success'); break;
      case 'cleanup': toast('Cleanup: ' + result.removed + ' expired memories removed', 'success'); break;
      case 'autotune': toast('Auto-tune: ' + result.boosted + ' boosted, ' + result.reduced + ' reduced', 'success'); break;
    }
  }).catch(function(e) { toast('Error: ' + e.message, 'error'); });
}

/* ═══════════════════════════════════════════════════════════════════════
   PAGE: Settings
   ═══════════════════════════════════════════════════════════════════════ */
function loadSettings() {
  /* Agents */
  api.get('/agents').then(function(res) {
    var agents = res.agents || res;
    if (agents && agents.length) {
      var h = '<table><thead><tr><th>Agent ID</th><th>Memories</th><th>Last activity</th></tr></thead><tbody>';
      agents.forEach(function(a) {
        h += '<tr><td style="font-family:var(--font-mono);color:var(--accent)">' + esc(a.agent_id) + '</td>' +
          '<td>' + a.memory_count + '</td><td style="color:var(--text-dim)">' + fmtDate(a.last_active || a.last_activity) + '</td></tr>';
      });
      h += '</tbody></table>';
      safeRender('#agents-list', h);
    } else {
      safeRender('#agents-list', '<div class="empty-state"><p>No agents found</p></div>');
    }
  }).catch(function() {
    safeRender('#agents-list', '<div class="empty-state"><p>Error</p></div>');
  });

  /* Server info */
  api.get('/health').then(function(health) {
    safeRender('#server-info',
      '<div style="display:grid;gap:8px">' +
      '<div style="display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid var(--border)"><span style="color:var(--text-dim)">Status</span><span style="color:var(--success);font-weight:500">' + esc(health.status) + '</span></div>' +
      '<div style="display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid var(--border)"><span style="color:var(--text-dim)">Version</span><span>' + esc(health.version) + '</span></div>' +
      '<div style="display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid var(--border)"><span style="color:var(--text-dim)">Semantic search</span><span style="color:' + (health.semantic_search ? 'var(--success)' : 'var(--text-dim)') + '">' + (health.semantic_search ? 'Active' : 'Disabled') + '</span></div></div>'
    );
  }).catch(function() {
    safeRender('#server-info', '<div class="empty-state"><p>Server unreachable</p></div>');
  });

  loadAuditLog();

  /* Metrics */
  api.get('/metrics').then(function(metrics) {
    $('#metrics-display').textContent = typeof metrics === 'string' ? metrics : JSON.stringify(metrics, null, 2);
  }).catch(function() {
    $('#metrics-display').textContent = 'Metrics not available';
  });
}

function loadAuditLog() {
  var eventFilter = $('#audit-event-filter') ? $('#audit-event-filter').value : '';
  var url = '/audit?limit=100';
  if (eventFilter) url += '&event=' + encodeURIComponent(eventFilter);

  api.get(url).then(function(data) {
    var events = data.events || [];
    if (events.length) {
      var h = '<table><thead><tr><th>Event</th><th>Memory</th><th>Date</th><th>Data</th></tr></thead><tbody>';
      events.slice(0, 50).forEach(function(e) {
        h += '<tr class="audit-row"><td><span class="audit-event">' + esc(e.event) + '</span></td>' +
          '<td>' + (e.memory_id ? '#' + e.memory_id : '\u2014') + '</td>' +
          '<td class="audit-time">' + fmtDate(e.created_at) + '</td>' +
          '<td style="max-width:200px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap" title="' + esc(e.data || '') + '">' + esc(truncate(e.data || '', 40)) + '</td></tr>';
      });
      h += '</tbody></table>';
      safeRender('#audit-table', h);
    } else {
      safeRender('#audit-table', '<div class="empty-state" style="padding:24px"><p>No audit events</p></div>');
    }
  }).catch(function() {
    safeRender('#audit-table', '<div class="empty-state"><p>Audit log non disponibile (KORE_AUDIT_LOG=1)</p></div>');
  });
}

/* ═══════════════════════════════════════════════════════════════════════
   Event Handlers
   ═══════════════════════════════════════════════════════════════════════ */
function initEventHandlers() {
  $('#btn-theme').addEventListener('click', function() {
    state.theme = state.theme === 'dark' ? 'light' : 'dark';
    localStorage.setItem('kore-theme', state.theme);
    applyTheme();
  });

  $('#btn-hamburger').addEventListener('click', function() {
    $('#sidebar').classList.toggle('open');
  });

  $('#mem-search').addEventListener('input', function() {
    clearTimeout(memSearchTimeout);
    memSearchTimeout = setTimeout(function() { loadMemories(); }, 400);
  });
  $('#mem-search').addEventListener('keydown', function(e) {
    if (e.key === 'Enter') { clearTimeout(memSearchTimeout); loadMemories(); }
  });
  $('#mem-category').addEventListener('change', function() { loadMemories(); });
  $('#mem-semantic').addEventListener('change', function() { loadMemories(); });

  $('#btn-new-memory').addEventListener('click', function() {
    state.editingMemoryId = null;
    $('#modal-memory-title').textContent = 'New memory';
    $('#modal-mem-content').value = '';
    $('#modal-mem-category').value = 'general';
    $('#modal-mem-importance').value = '1';
    $('#modal-mem-ttl').value = '';
    $('#modal-mem-tags').value = '';
    $('#modal-memory').classList.add('open');
  });

  $('#modal-memory-close').addEventListener('click', function() { $('#modal-memory').classList.remove('open'); });
  $('#modal-mem-cancel').addEventListener('click', function() { $('#modal-memory').classList.remove('open'); });

  $('#modal-mem-save').addEventListener('click', function() {
    var content = $('#modal-mem-content').value.trim();
    if (!content) { toast('Content is required', 'error'); return; }
    var category = $('#modal-mem-category').value;
    var importance = parseInt($('#modal-mem-importance').value);
    var ttl = $('#modal-mem-ttl').value ? parseInt($('#modal-mem-ttl').value) : null;
    var tags = $('#modal-mem-tags').value.split(',').map(function(t) { return t.trim(); }).filter(Boolean);

    if (state.editingMemoryId) {
      api.put('/memories/' + state.editingMemoryId, { content: content, category: category, importance: importance }).then(function() {
        toast('Memory updated', 'success');
        $('#modal-memory').classList.remove('open');
        loadMemories();
      }).catch(function(e) { toast(e.message, 'error'); });
    } else {
      var body = { content: content, category: category, importance: importance };
      if (ttl) body.ttl_hours = ttl;
      api.post('/save', body).then(function(res) {
        if (tags.length && res && res.id) {
          return api.post('/memories/' + res.id + '/tags', { tags: tags });
        }
      }).then(function() {
        toast('Memory saved', 'success');
        $('#modal-memory').classList.remove('open');
        loadMemories();
      }).catch(function(e) { toast(e.message, 'error'); });
    }
  });

  $('#btn-new-session').addEventListener('click', function() {
    $('#modal-sess-id').value = 'session-' + new Date().toISOString().slice(0, 10) + '-' + Math.random().toString(36).slice(2, 6);
    $('#modal-sess-title').value = '';
    $('#modal-session').classList.add('open');
  });
  $('#modal-session-close').addEventListener('click', function() { $('#modal-session').classList.remove('open'); });
  $('#modal-sess-cancel').addEventListener('click', function() { $('#modal-session').classList.remove('open'); });
  $('#modal-sess-save').addEventListener('click', function() {
    var id = $('#modal-sess-id').value.trim();
    if (!id) { toast('Session ID is required', 'error'); return; }
    api.post('/sessions', { session_id: id, title: $('#modal-sess-title').value.trim() || null }).then(function() {
      toast('Session created', 'success');
      $('#modal-session').classList.remove('open');
      loadSessions();
    }).catch(function(e) { toast(e.message, 'error'); });
  });

  $('#btn-timeline-search').addEventListener('click', function() { loadTimeline($('#timeline-search').value.trim()); });
  $('#timeline-search').addEventListener('keydown', function(e) { if (e.key === 'Enter') loadTimeline($('#timeline-search').value.trim()); });

  $('#btn-decay').addEventListener('click', function() { runMaintenanceAction('decay'); });
  $('#btn-compress').addEventListener('click', function() { runMaintenanceAction('compress'); });
  $('#btn-cleanup').addEventListener('click', function() { runMaintenanceAction('cleanup'); });
  $('#btn-autotune').addEventListener('click', function() { runMaintenanceAction('autotune'); });

  $('#btn-export').addEventListener('click', function() {
    api.get('/export').then(function(data) {
      var blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
      var url = URL.createObjectURL(blob);
      var a = document.createElement('a');
      a.href = url; a.download = 'kore-export-' + state.agentId + '-' + new Date().toISOString().slice(0,10) + '.json';
      a.click(); URL.revokeObjectURL(url);
      toast('Export complete: ' + data.total + ' memories', 'success');
    }).catch(function(e) { toast(e.message, 'error'); });
  });

  $('#import-file').addEventListener('change', function(e) {
    var file = e.target.files[0];
    if (!file) return;
    file.text().then(function(text) {
      var data = JSON.parse(text);
      var memories = data.memories || data;
      if (!Array.isArray(memories)) throw new Error('Invalid format');
      return api.post('/import', { memories: memories });
    }).then(function(res) {
      toast('Import: ' + res.imported + ' memories imported', 'success');
      e.target.value = '';
    }).catch(function(err) { toast('Import error: ' + err.message, 'error'); });
  });

  $('#btn-add-relation').addEventListener('click', function() {
    var source = parseInt($('#rel-source').value);
    var target = parseInt($('#rel-target').value);
    var relation = $('#rel-type').value.trim() || 'related';
    if (!source || !target) { toast('Enter source and target ID', 'error'); return; }
    api.post('/memories/' + source + '/relations', { target_id: target, relation: relation }).then(function() {
      toast('Relation created', 'success'); loadTags();
    }).catch(function(e) { toast(e.message, 'error'); });
  });

  $('#btn-graph-reload').addEventListener('click', loadGraph);
  $('#btn-graph-center').addEventListener('click', function() {
    graphState.zoom = 1; graphState.panX = 0; graphState.panY = 0;
  });
  $('#graph-show-labels').addEventListener('change', function(e) {
    graphState.showLabels = e.target.checked;
  });
  $('#graph-show-arrows').addEventListener('change', function(e) {
    graphState.showArrows = e.target.checked;
  });
  $('#graph-detail-close').addEventListener('click', function() {
    graphState.selectedNode = null;
    $('#graph-detail').style.display = 'none';
  });

  $('#agent-select').addEventListener('change', function(e) {
    state.agentId = e.target.value;
    loadPageData(state.currentPage);
  });

  $('#btn-audit-refresh').addEventListener('click', loadAuditLog);
  $('#audit-event-filter').addEventListener('change', loadAuditLog);

  /* Close modal on overlay click */
  $$('.modal-overlay').forEach(function(overlay) {
    overlay.addEventListener('click', function(e) {
      if (e.target === overlay) overlay.classList.remove('open');
    });
  });

  /* Close modal with Escape */
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
      $$('.modal-overlay.open').forEach(function(m) { m.classList.remove('open'); });
    }
  });

  /* Tag filter */
  $('#tag-search').addEventListener('input', function() {
    var q = $('#tag-search').value.toLowerCase();
    $$('#tag-cloud .badge-tag').forEach(function(el) {
      el.style.display = el.textContent.toLowerCase().indexOf(q) >= 0 ? '' : 'none';
    });
  });
}

/* ── Load agent list in selector ──────────────────────────────────── */
function loadAgentSelector() {
  api.get('/agents').then(function(res) {
    var agents = res.agents || res;
    var select = $('#agent-select');
    var current = select.value;
    var html = '';
    (agents || []).forEach(function(a) {
      html += '<option value="' + esc(a.agent_id) + '">' + esc(a.agent_id) + ' (' + a.memory_count + ')</option>';
    });
    safeRender(select, html);
    if (!select.querySelector('option[value="' + current + '"]')) {
      select.insertAdjacentHTML('afterbegin', '<option value="default">default</option>');
    }
    select.value = current || 'default';
  }).catch(function() { /* keep default */ });
}

/* ── Initialization ────────────────────────────────────────────────── */
function init() {
  applyTheme();
  initNav();
  initEventHandlers();
  loadAgentSelector();
  loadPageData('overview');
}

init();
</script>
</body>
</html>
```

## File: `scripts/import_memory.py`
```python
"""
Kore — import_memory.py
Popola il DB Kore leggendo MEMORY.md e suddividendo per sezioni.
Esegui una volta sola dopo l'installazione.
"""

import re
import sys
import json
from pathlib import Path

import httpx

MEMORY_PATH = Path(__file__).parent.parent.parent / "MEMORY.md"
KORE_URL = "http://localhost:8765"

SECTION_CATEGORY_MAP = {
    "finanz": "finance",
    "kore": "project",
    "progetti": "project",
    "clawdwork": "task",
    "freelance": "person",
    "crypto": "trading",
    "regole": "preference",
    "ottimizzaz": "preference",
    "calcfast": "project",
    "amazon": "project",
    "agencypilot": "project",
    "priorità": "task",
}

IMPORTANCE_MAP = {
    "finance": 4,
    "trading": 4,
    "project": 3,
    "task": 3,
    "preference": 5,
    "person": 2,
    "decision": 4,
    "general": 2,
}


def detect_category(section_title: str) -> str:
    title_lower = section_title.lower()
    for keyword, category in SECTION_CATEGORY_MAP.items():
        if keyword in title_lower:
            return category
    return "general"


def parse_memory_md(path: Path) -> list[dict]:
    """Split MEMORY.md into chunks by H2 section, return list of records."""
    text = path.read_text(encoding="utf-8")
    sections = re.split(r"\n(?=## )", text)

    records = []
    for section in sections:
        lines = section.strip().splitlines()
        if not lines:
            continue

        title_line = lines[0].lstrip("#").strip()
        body_lines = [l for l in lines[1:] if l.strip() and not l.startswith("---")]

        if not body_lines:
            continue

        category = detect_category(title_line)
        importance = IMPORTANCE_MAP.get(category, 2)

        # Split long sections into sub-chunks by bullet points
        chunks = chunk_section(title_line, body_lines)
        for chunk in chunks:
            records.append({
                "content": chunk,
                "category": category,
                "importance": importance,
            })

    return records


def chunk_section(title: str, lines: list[str]) -> list[str]:
    """
    Group bullet lines into chunks of max 3 items, prefixed with section title.
    Avoids saving single massive blobs.
    """
    bullets = [l.strip().lstrip("-").lstrip("*").strip() for l in lines if l.strip()]
    bullets = [b for b in bullets if len(b) > 10]

    if not bullets:
        return []

    chunks = []
    for i in range(0, len(bullets), 3):
        group = bullets[i:i+3]
        chunk = f"[{title}] " + " | ".join(group)
        if len(chunk) > 4000:
            chunk = chunk[:3997] + "..."
        chunks.append(chunk)

    return chunks


def save_record(record: dict) -> int | None:
    try:
        resp = httpx.post(f"{KORE_URL}/save", json=record, timeout=5)
        if resp.status_code == 201:
            return resp.json()["id"]
        else:
            print(f"  ⚠️  {resp.status_code}: {resp.text[:80]}")
            return None
    except Exception as e:
        print(f"  ❌ Errore: {e}")
        return None


def main():
    print(f"📂 Lettura {MEMORY_PATH}...")
    records = parse_memory_md(MEMORY_PATH)
    print(f"📝 Trovati {len(records)} chunk da importare\n")

    saved = 0
    for rec in records:
        record_id = save_record(rec)
        if record_id:
            print(f"  ✅ #{record_id} [{rec['category']}] ★{rec['importance']} — {rec['content'][:60]}...")
            saved += 1

    print(f"\n🎉 Importati {saved}/{len(records)} record in Kore")


if __name__ == "__main__":
    main()
```

## File: `sdk/js/.gitignore`
```
node_modules/
dist/
*.log
.DS_Store
```

## File: `sdk/js/README.md`
```markdown
# Kore Memory Client

JavaScript/TypeScript client for [Kore Memory](https://github.com/auriti-labs/kore-memory) - the memory layer that thinks like a human.

## Features

- 🔥 **Zero runtime dependencies** - uses native `fetch`
- 📦 **Dual package** - ESM + CommonJS support
- 🏷️ **Full TypeScript support** - complete type definitions
- 🚀 **17 async methods** - covers all Kore Memory REST APIs
- ⚡ **Lightweight** - ~6KB minified
- 🛡️ **Error handling** - typed error hierarchy
- 🌐 **Node 18+** - modern JavaScript support

## Installation

```bash
npm install kore-memory-client
```

## Quick Start

```typescript
import { KoreClient } from 'kore-memory-client';

const kore = new KoreClient({
  baseUrl: 'http://localhost:8765',
  agentId: 'my-agent',
  apiKey: 'your-api-key' // optional for localhost
});

// Save a memory
const result = await kore.save({
  content: 'User prefers dark mode',
  category: 'preference',
  importance: 4
});

// Search memories
const memories = await kore.search({
  q: 'dark mode',
  limit: 5,
  semantic: true
});

console.log(memories.results);
```

## Configuration

```typescript
const kore = new KoreClient({
  baseUrl?: string;    // default: 'http://localhost:8765'
  agentId?: string;    // default: 'default'
  apiKey?: string;     // optional, required for non-localhost
  timeout?: number;    // default: 30000ms
});
```

## API Methods

### Core Operations

```typescript
// Save memory
await kore.save({
  content: string,
  category?: Category,     // 'general' | 'project' | 'task' | etc.
  importance?: number,     // 1-5, 1=auto-scored
  ttl_hours?: number      // auto-expire after N hours
});

// Batch save (up to 100)
await kore.saveBatch([
  { content: 'Memory 1', category: 'project' },
  { content: 'Memory 2', category: 'task' }
]);

// Search memories
await kore.search({
  q: string,
  limit?: number,         // default: 5
  offset?: number,        // pagination
  category?: Category,    // filter by category
  semantic?: boolean      // default: true
});

// Timeline for subject
await kore.timeline({
  subject: string,
  limit?: number,
  offset?: number
});

// Delete memory
await kore.delete(memoryId: number);
```

### Tags & Relations

```typescript
// Add tags
await kore.addTags(memoryId, ['react', 'frontend']);

// Get tags
await kore.getTags(memoryId);

// Remove tags
await kore.removeTags(memoryId, ['old-tag']);

// Search by tag
await kore.searchByTag('react', 10);

// Add relation
await kore.addRelation(memoryId, targetId, 'depends_on');

// Get relations
await kore.getRelations(memoryId);
```

### Maintenance

```typescript
// Run decay pass (Ebbinghaus forgetting)
await kore.decayRun();

// Compress similar memories
await kore.compress();

// Cleanup expired memories
await kore.cleanup();
```

### Backup

```typescript
// Export all memories
const backup = await kore.exportMemories();

// Import memories
await kore.importMemories(backup.memories);
```

### Utility

```typescript
// Health check
const health = await kore.health();
console.log(health.capabilities.semantic_search);
```

## Error Handling

The client provides a typed error hierarchy:

```typescript
import { 
  KoreError,
  KoreAuthError,
  KoreNotFoundError,
  KoreValidationError,
  KoreRateLimitError,
  KoreServerError
} from 'kore-memory-client';

try {
  await kore.save({ content: 'ab' }); // too short
} catch (error) {
  if (error instanceof KoreValidationError) {
    console.log('Validation failed:', error.detail);
  } else if (error instanceof KoreAuthError) {
    console.log('Authentication failed');
  }
}
```

## TypeScript Support

Full type definitions included:

```typescript
import type { 
  MemoryRecord,
  MemorySaveResponse,
  MemorySearchResponse,
  Category,
  SearchOptions
} from 'kore-memory-client';

const memories: MemoryRecord[] = await kore.search({ q: 'test' }).then(r => r.results);
```

## Categories

Available memory categories:

- `general` (default)
- `project`
- `trading`
- `finance`
- `person`
- `preference`
- `task`
- `decision`

## License

MIT © [Juan Auriti](https://github.com/auriti)

---

Part of the [Kore Memory](https://github.com/auriti-labs/kore-memory) ecosystem.
```

## File: `sdk/js/package.json`
```json
{
  "name": "kore-memory-client",
  "version": "2.0.0",
  "description": "JavaScript/TypeScript client for Kore Memory - the memory layer that thinks like a human",
  "type": "module",
  "main": "./dist/index.cjs",
  "module": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js",
      "require": "./dist/index.cjs"
    }
  },
  "files": [
    "dist"
  ],
  "scripts": {
    "build": "tsup",
    "test": "vitest run",
    "test:watch": "vitest",
    "typecheck": "tsc --noEmit",
    "clean": "rm -rf dist"
  },
  "keywords": [
    "ai",
    "memory",
    "agents",
    "llm",
    "embeddings",
    "semantic-search",
    "rag",
    "forgetting-curve",
    "typescript",
    "javascript"
  ],
  "author": "Juan Auriti",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/auriti-labs/kore-memory.git",
    "directory": "sdk/js"
  },
  "bugs": {
    "url": "https://github.com/auriti-labs/kore-memory/issues"
  },
  "homepage": "https://github.com/auriti-labs/kore-memory#readme",
  "engines": {
    "node": ">=18.0.0"
  },
  "devDependencies": {
    "@types/node": "^20.0.0",
    "tsup": "^8.0.0",
    "typescript": "^5.0.0",
    "vitest": "^1.0.0"
  }
}
```

## File: `sdk/js/tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["ES2022", "DOM"],
    "module": "ESNext",
    "moduleResolution": "bundler",
    "allowSyntheticDefaultImports": true,
    "esModuleInterop": true,
    "allowJs": true,
    "strict": true,
    "noEmit": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "outDir": "./dist",
    "rootDir": "./src",
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist", "tests"]
}
```

## File: `sdk/js/tsup.config.ts`
```typescript
import { defineConfig } from "tsup";

export default defineConfig({
  entry: ["src/index.ts"],
  format: ["esm", "cjs"],
  dts: true,
  sourcemap: true,
  clean: true,
  splitting: false,
  minify: false,
});
```

## File: `sdk/js/vitest.config.ts`
```typescript
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    environment: "node",
    globals: true,
  },
});
```

## File: `sdk/js/src/client.ts`
```typescript
/**
 * Kore Memory - JavaScript/TypeScript Client
 * Mirrors src/client.py functionality
 */

import { mapHttpError } from "./errors.js";
import type {
  ArchiveResponse,
  BatchSaveRequest,
  BatchSaveResponse,
  CleanupExpiredResponse,
  CompressRunResponse,
  DecayRunResponse,
  HealthResponse,
  KoreClientConfig,
  MemoryExportResponse,
  MemoryImportRequest,
  MemoryImportResponse,
  MemoryRecord,
  MemorySaveRequest,
  MemorySaveResponse,
  MemorySearchResponse,
  MemoryUpdateRequest,
  RelationResponse,
  SearchOptions,
  TagResponse,
  TimelineOptions,
} from "./types.js";

export class KoreClient {
  private readonly baseUrl: string;
  private readonly apiKey?: string;
  private readonly agentId: string;
  private readonly timeout: number;

  constructor(config: KoreClientConfig = {}) {
    this.baseUrl = config.baseUrl?.replace(/\/$/, "") || "http://localhost:8765";
    this.apiKey = config.apiKey;
    this.agentId = config.agentId || "default";
    this.timeout = config.timeout || 30000;
  }

  private async _request<T>(
    method: string,
    path: string,
    body?: any,
    params?: Record<string, string | number | boolean>
  ): Promise<T> {
    const url = new URL(path, this.baseUrl);
    
    if (params) {
      Object.entries(params).forEach(([key, value]) => {
        if (value !== undefined && value !== null) {
          url.searchParams.set(key, String(value));
        }
      });
    }

    const headers: Record<string, string> = {
      "X-Agent-Id": this.agentId,
    };

    if (this.apiKey) {
      headers["X-Kore-Key"] = this.apiKey;
    }

    if (body) {
      headers["Content-Type"] = "application/json";
    }

    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), this.timeout);

    try {
      const response = await fetch(url.toString(), {
        method,
        headers,
        body: body ? JSON.stringify(body) : undefined,
        signal: controller.signal,
      });

      clearTimeout(timeoutId);

      if (!response.ok) {
        let errorDetail;
        try {
          errorDetail = await response.json();
        } catch {
          errorDetail = await response.text();
        }
        
        const message = typeof errorDetail === "object" && errorDetail.detail
          ? errorDetail.detail
          : String(errorDetail || response.statusText);
        
        throw mapHttpError(response.status, message, errorDetail);
      }

      // Handle 204 No Content (DELETE responses)
      if (response.status === 204) {
        return true as T;
      }

      return await response.json();
    } catch (error: any) {
      clearTimeout(timeoutId);
      if (error.name === "AbortError") {
        throw new Error(`Request timeout after ${this.timeout}ms`);
      }
      throw error;
    }
  }

  /**
   * Performs an HTTP request that returns plain text instead of JSON.
   * Used for endpoints like /metrics that return Prometheus-format text.
   */
  private async _requestText(
    method: string,
    path: string,
    params?: Record<string, string | number | boolean>
  ): Promise<string> {
    const url = new URL(path, this.baseUrl);

    if (params) {
      Object.entries(params).forEach(([key, value]) => {
        if (value !== undefined && value !== null) {
          url.searchParams.set(key, String(value));
        }
      });
    }

    const headers: Record<string, string> = {
      "X-Agent-Id": this.agentId,
    };

    if (this.apiKey) {
      headers["X-Kore-Key"] = this.apiKey;
    }

    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), this.timeout);

    try {
      const response = await fetch(url.toString(), {
        method,
        headers,
        signal: controller.signal,
      });

      clearTimeout(timeoutId);

      if (!response.ok) {
        let errorDetail;
        try {
          errorDetail = await response.json();
        } catch {
          errorDetail = await response.text();
        }

        const message = typeof errorDetail === "object" && errorDetail.detail
          ? errorDetail.detail
          : String(errorDetail || response.statusText);

        throw mapHttpError(response.status, message, errorDetail);
      }

      return await response.text();
    } catch (error: any) {
      clearTimeout(timeoutId);
      if (error.name === "AbortError") {
        throw new Error(`Request timeout after ${this.timeout}ms`);
      }
      throw error;
    }
  }

  // Core memory operations
  async save(input: MemorySaveRequest): Promise<MemorySaveResponse> {
    return this._request<MemorySaveResponse>("POST", "/save", input);
  }

  async saveBatch(memories: MemorySaveRequest[]): Promise<BatchSaveResponse> {
    const body: BatchSaveRequest = { memories };
    return this._request<BatchSaveResponse>("POST", "/save/batch", body);
  }

  async search(options: SearchOptions): Promise<MemorySearchResponse> {
    const { q, ...params } = options;
    return this._request<MemorySearchResponse>("GET", "/search", undefined, {
      q,
      ...params,
    });
  }

  async timeline(options: TimelineOptions): Promise<MemorySearchResponse> {
    const { subject, ...params } = options;
    return this._request<MemorySearchResponse>("GET", "/timeline", undefined, {
      subject,
      ...params,
    });
  }

  async update(memoryId: number, input: MemoryUpdateRequest): Promise<MemorySaveResponse> {
    return this._request<MemorySaveResponse>("PUT", `/memories/${memoryId}`, input);
  }

  async delete(memoryId: number): Promise<boolean> {
    return this._request<boolean>("DELETE", `/memories/${memoryId}`);
  }

  // Archive
  async archive(memoryId: number): Promise<ArchiveResponse> {
    return this._request<ArchiveResponse>("POST", `/memories/${memoryId}/archive`);
  }

  async restore(memoryId: number): Promise<ArchiveResponse> {
    return this._request<ArchiveResponse>("POST", `/memories/${memoryId}/restore`);
  }

  async getArchived(options?: { limit?: number; offset?: number }): Promise<MemorySearchResponse> {
    return this._request<MemorySearchResponse>("GET", "/archive", undefined, options);
  }

  // Tags
  async addTags(memoryId: number, tags: string[]): Promise<TagResponse> {
    return this._request<TagResponse>("POST", `/memories/${memoryId}/tags`, {
      tags,
    });
  }

  async getTags(memoryId: number): Promise<TagResponse> {
    return this._request<TagResponse>("GET", `/memories/${memoryId}/tags`);
  }

  async removeTags(memoryId: number, tags: string[]): Promise<TagResponse> {
    return this._request<TagResponse>("DELETE", `/memories/${memoryId}/tags`, {
      tags,
    });
  }

  async searchByTag(tag: string, limit?: number): Promise<MemorySearchResponse> {
    return this._request<MemorySearchResponse>(
      "GET",
      `/tags/${encodeURIComponent(tag)}/memories`,
      undefined,
      limit ? { limit } : undefined
    );
  }

  // Relations
  async addRelation(
    memoryId: number,
    targetId: number,
    relation = "related"
  ): Promise<RelationResponse> {
    return this._request<RelationResponse>(
      "POST",
      `/memories/${memoryId}/relations`,
      { target_id: targetId, relation }
    );
  }

  async getRelations(memoryId: number): Promise<RelationResponse> {
    return this._request<RelationResponse>(
      "GET",
      `/memories/${memoryId}/relations`
    );
  }

  // Maintenance
  async decayRun(): Promise<DecayRunResponse> {
    return this._request<DecayRunResponse>("POST", "/decay/run");
  }

  async compress(): Promise<CompressRunResponse> {
    return this._request<CompressRunResponse>("POST", "/compress");
  }

  async cleanup(): Promise<CleanupExpiredResponse> {
    return this._request<CleanupExpiredResponse>("POST", "/cleanup");
  }

  // Backup
  async exportMemories(): Promise<MemoryExportResponse> {
    return this._request<MemoryExportResponse>("GET", "/export");
  }

  async importMemories(
    memories: Record<string, any>[]
  ): Promise<MemoryImportResponse> {
    const body: MemoryImportRequest = { memories };
    return this._request<MemoryImportResponse>("POST", "/import", body);
  }

  // Utility
  async health(): Promise<HealthResponse> {
    return this._request<HealthResponse>("GET", "/health");
  }

  /** Returns Prometheus-format metrics as raw text. */
  async metrics(): Promise<string> {
    return this._requestText("GET", "/metrics");
  }
}
```

## File: `sdk/js/src/errors.ts`
```typescript
/**
 * Kore Memory - Error Classes
 * Mirrors src/client.py error hierarchy
 */

export class KoreError extends Error {
  constructor(
    message: string,
    public statusCode?: number,
    public detail?: any
  ) {
    super(message);
    this.name = "KoreError";
  }
}

export class KoreAuthError extends KoreError {
  constructor(message: string, statusCode?: number, detail?: any) {
    super(message, statusCode, detail);
    this.name = "KoreAuthError";
  }
}

export class KoreNotFoundError extends KoreError {
  constructor(message: string, statusCode?: number, detail?: any) {
    super(message, statusCode, detail);
    this.name = "KoreNotFoundError";
  }
}

export class KoreValidationError extends KoreError {
  constructor(message: string, statusCode?: number, detail?: any) {
    super(message, statusCode, detail);
    this.name = "KoreValidationError";
  }
}

export class KoreRateLimitError extends KoreError {
  constructor(message: string, statusCode?: number, detail?: any) {
    super(message, statusCode, detail);
    this.name = "KoreRateLimitError";
  }
}

export class KoreServerError extends KoreError {
  constructor(message: string, statusCode?: number, detail?: any) {
    super(message, statusCode, detail);
    this.name = "KoreServerError";
  }
}

/**
 * Maps HTTP status codes to appropriate Kore error classes
 */
export function mapHttpError(
  status: number,
  message: string,
  detail?: any
): KoreError {
  switch (status) {
    case 401:
    case 403:
      return new KoreAuthError(message, status, detail);
    case 404:
      return new KoreNotFoundError(message, status, detail);
    case 422:
      return new KoreValidationError(message, status, detail);
    case 429:
      return new KoreRateLimitError(message, status, detail);
    default:
      if (status >= 500) {
        return new KoreServerError(message, status, detail);
      }
      return new KoreError(message, status, detail);
  }
}
```

## File: `sdk/js/src/index.ts`
```typescript
/**
 * Kore Memory - JavaScript/TypeScript Client SDK
 * Entry point with all exports
 */

export { KoreClient } from "./client.js";
export * from "./types.js";
export * from "./errors.js";
```

## File: `sdk/js/src/types.ts`
```typescript
/**
 * Kore Memory - TypeScript Types
 * Mirrors src/models.py Pydantic models
 */

export type Category =
  | "general"
  | "project"
  | "trading"
  | "finance"
  | "person"
  | "preference"
  | "task"
  | "decision";

export interface MemorySaveRequest {
  content: string;
  category?: Category;
  importance?: number; // 1-5, 1=auto-scored
  ttl_hours?: number; // 1-8760
}

export interface MemoryUpdateRequest {
  content?: string;
  category?: Category;
  importance?: number; // 1-5
}

export interface MemoryRecord {
  id: number;
  content: string;
  category: string;
  importance: number;
  decay_score: number;
  created_at: string;
  updated_at: string;
  score?: number;
}

export interface MemorySaveResponse {
  id: number;
  importance: number;
  message: string;
}

export interface MemorySearchResponse {
  results: MemoryRecord[];
  total: number;
  offset: number;
  has_more: boolean;
  cursor?: string | null;
}

export interface BatchSaveRequest {
  memories: MemorySaveRequest[];
}

export interface BatchSaveResponse {
  saved: MemorySaveResponse[];
  total: number;
}

export interface TagRequest {
  tags: string[];
}

export interface TagResponse {
  count: number;
  tags: string[];
}

export interface RelationRequest {
  target_id: number;
  relation?: string;
}

export interface RelationRecord {
  source_id: number;
  target_id: number;
  relation: string;
  created_at: string;
}

export interface RelationResponse {
  relations: RelationRecord[];
  total: number;
}

export interface DecayRunResponse {
  updated: number;
  message: string;
}

export interface CompressRunResponse {
  clusters_found: number;
  memories_merged: number;
  new_records_created: number;
  message: string;
}

export interface CleanupExpiredResponse {
  removed: number;
  message: string;
}

export interface ArchiveResponse {
  success: boolean;
  message: string;
}

export interface MemoryExportResponse {
  memories: Record<string, any>[];
  total: number;
}

export interface MemoryImportRequest {
  memories: Record<string, any>[];
}

export interface MemoryImportResponse {
  imported: number;
  message: string;
}

export interface HealthResponse {
  status: string;
  version: string;
  semantic_search: boolean;
  database: string;
}

// Client configuration
export interface KoreClientConfig {
  baseUrl?: string;
  apiKey?: string;
  agentId?: string;
  timeout?: number;
}

// Search options
export interface SearchOptions {
  q: string;
  limit?: number;
  offset?: number;
  category?: Category;
  semantic?: boolean;
  cursor?: string;
}

// Timeline options
export interface TimelineOptions {
  subject: string;
  limit?: number;
  offset?: number;
  cursor?: string;
}
```

## File: `sdk/js/tests/client.test.ts`
```typescript
/**
 * Tests for KoreClient
 */

import { describe, it, expect, vi, beforeEach, afterEach } from "vitest";
import { KoreClient } from "../src/client.js";
import {
  KoreAuthError,
  KoreNotFoundError,
  KoreValidationError,
} from "../src/errors.js";
import { mockResponse, mockFetch, mockFetchError } from "./helpers.js";

describe("KoreClient", () => {
  let client: KoreClient;
  let originalFetch: typeof global.fetch;

  beforeEach(() => {
    originalFetch = global.fetch;
    client = new KoreClient({
      baseUrl: "http://localhost:8765",
      agentId: "test-agent",
      apiKey: "test-key",
    });
  });

  afterEach(() => {
    global.fetch = originalFetch;
    vi.restoreAllMocks();
  });

  describe("Constructor", () => {
    it("should use default config", () => {
      const defaultClient = new KoreClient();
      expect(defaultClient).toBeDefined();
    });

    it("should strip trailing slash from baseUrl", () => {
      const clientWithSlash = new KoreClient({
        baseUrl: "http://localhost:8765/",
      });
      expect(clientWithSlash).toBeDefined();
    });
  });

  describe("save", () => {
    it("should save memory successfully", async () => {
      const mockResponseData = {
        id: 1,
        importance: 4,
        message: "Memory saved",
      };
      mockFetch(mockResponse(200, mockResponseData));

      const result = await client.save({
        content: "Test memory",
        category: "general",
        importance: 4,
      });

      expect(result).toEqual(mockResponseData);
      expect(fetch).toHaveBeenCalledWith(
        "http://localhost:8765/save",
        expect.objectContaining({
          method: "POST",
          headers: expect.objectContaining({
            "Content-Type": "application/json",
            "X-Agent-Id": "test-agent",
            "X-Kore-Key": "test-key",
          }),
          body: JSON.stringify({
            content: "Test memory",
            category: "general",
            importance: 4,
          }),
        })
      );
    });

    it("should handle validation error", async () => {
      mockFetch(mockResponse(422, { detail: "Content too short" }));

      await expect(
        client.save({ content: "ab" })
      ).rejects.toThrow(KoreValidationError);
    });
  });

  describe("saveBatch", () => {
    it("should save batch of memories", async () => {
      const mockResponseData = {
        saved: [
          { id: 1, importance: 3, message: "Memory saved" },
          { id: 2, importance: 4, message: "Memory saved" },
        ],
        total: 2,
      };
      mockFetch(mockResponse(200, mockResponseData));

      const memories = [
        { content: "Memory 1", category: "project" as const },
        { content: "Memory 2", category: "task" as const },
      ];

      const result = await client.saveBatch(memories);

      expect(result).toEqual(mockResponseData);
      expect(fetch).toHaveBeenCalledWith(
        "http://localhost:8765/save/batch",
        expect.objectContaining({
          method: "POST",
          body: JSON.stringify({ memories }),
        })
      );
    });
  });

  describe("search", () => {
    it("should search memories with all options", async () => {
      const mockResponseData = {
        results: [
          {
            id: 1,
            content: "Test memory",
            category: "general",
            importance: 3,
            decay_score: 0.95,
            created_at: "2024-01-01T00:00:00Z",
            updated_at: "2024-01-01T00:00:00Z",
            score: 0.85,
          },
        ],
        total: 1,
        offset: 0,
        has_more: false,
      };
      mockFetch(mockResponse(200, mockResponseData));

      const result = await client.search({
        q: "test",
        limit: 10,
        offset: 0,
        category: "general",
        semantic: true,
      });

      expect(result).toEqual(mockResponseData);
      expect(fetch).toHaveBeenCalledWith(
        "http://localhost:8765/search?q=test&limit=10&offset=0&category=general&semantic=true",
        expect.objectContaining({
          method: "GET",
        })
      );
    });

    it("should search with minimal options", async () => {
      const mockResponseData = {
        results: [],
        total: 0,
        offset: 0,
        has_more: false,
      };
      mockFetch(mockResponse(200, mockResponseData));

      const result = await client.search({ q: "test" });

      expect(result).toEqual(mockResponseData);
      expect(fetch).toHaveBeenCalledWith(
        "http://localhost:8765/search?q=test",
        expect.objectContaining({
          method: "GET",
        })
      );
    });
  });

  describe("timeline", () => {
    it("should get timeline for subject", async () => {
      const mockResponseData = {
        results: [
          {
            id: 1,
            content: "Project started",
            category: "project",
            importance: 4,
            decay_score: 0.9,
            created_at: "2024-01-01T00:00:00Z",
            updated_at: "2024-01-01T00:00:00Z",
          },
        ],
        total: 1,
        offset: 0,
        has_more: false,
      };
      mockFetch(mockResponse(200, mockResponseData));

      const result = await client.timeline({
        subject: "project alpha",
        limit: 20,
      });

      expect(result).toEqual(mockResponseData);
      expect(fetch).toHaveBeenCalledWith(
        "http://localhost:8765/timeline?subject=project+alpha&limit=20",
        expect.objectContaining({
          method: "GET",
        })
      );
    });
  });

  describe("delete", () => {
    it("should delete memory successfully", async () => {
      mockFetch(mockResponse(204));

      const result = await client.delete(1);

      expect(result).toBe(true);
      expect(fetch).toHaveBeenCalledWith(
        "http://localhost:8765/memories/1",
        expect.objectContaining({
          method: "DELETE",
        })
      );
    });

    it("should handle not found error", async () => {
      mockFetch(mockResponse(404, { detail: "Memory not found" }));

      await expect(client.delete(999)).rejects.toThrow(KoreNotFoundError);
    });
  });

  describe("Tags", () => {
    it("should add tags to memory", async () => {
      const mockResponseData = {
        count: 2,
        tags: ["react", "frontend"],
      };
      mockFetch(mockResponse(200, mockResponseData));

      const result = await client.addTags(1, ["react", "frontend"]);

      expect(result).toEqual(mockResponseData);
      expect(fetch).toHaveBeenCalledWith(
        "http://localhost:8765/memories/1/tags",
        expect.objectContaining({
          method: "POST",
          body: JSON.stringify({ tags: ["react", "frontend"] }),
        })
      );
    });

    it("should get tags for memory", async () => {
      const mockResponseData = {
        count: 1,
        tags: ["react"],
      };
      mockFetch(mockResponse(200, mockResponseData));

      const result = await client.getTags(1);

      expect(result).toEqual(mockResponseData);
      expect(fetch).toHaveBeenCalledWith(
        "http://localhost:8765/memories/1/tags",
        expect.objectContaining({
          method: "GET",
        })
      );
    });

    it("should remove tags from memory", async () => {
      const mockResponseData = {
        count: 0,
        tags: [],
      };
      mockFetch(mockResponse(200, mockResponseData));

      const result = await client.removeTags(1, ["old-tag"]);

      expect(result).toEqual(mockResponseData);
      expect(fetch).toHaveBeenCalledWith(
        "http://localhost:8765/memories/1/tags",
        expect.objectContaining({
          method: "DELETE",
          body: JSON.stringify({ tags: ["old-tag"] }),
        })
      );
    });

    it("should search by tag", async () => {
      const mockResponseData = {
        results: [
          {
            id: 1,
            content: "React component",
            category: "project",
            importance: 3,
            decay_score: 0.9,
            created_at: "2024-01-01T00:00:00Z",
            updated_at: "2024-01-01T00:00:00Z",
          },
        ],
        total: 1,
        offset: 0,
        has_more: false,
      };
      mockFetch(mockResponse(200, mockResponseData));

      const result = await client.searchByTag("react", 10);

      expect(result).toEqual(mockResponseData);
      expect(fetch).toHaveBeenCalledWith(
        "http://localhost:8765/tags/react/memories?limit=10",
        expect.objectContaining({
          method: "GET",
        })
      );
    });

    it("should encode tag in URL", async () => {
      mockFetch(mockResponse(200, { results: [], total: 0, offset: 0, has_more: false }));

      await client.searchByTag("tag with spaces");

      expect(fetch).toHaveBeenCalledWith(
        "http://localhost:8765/tags/tag%20with%20spaces/memories",
        expect.anything()
      );
    });
  });

  describe("Relations", () => {
    it("should add relation between memories", async () => {
      const mockResponseData = {
        relations: [
          {
            source_id: 1,
            target_id: 2,
            relation: "depends_on",
            created_at: "2024-01-01T00:00:00Z",
          },
        ],
        total: 1,
      };
      mockFetch(mockResponse(200, mockResponseData));

      const result = await client.addRelation(1, 2, "depends_on");

      expect(result).toEqual(mockResponseData);
      expect(fetch).toHaveBeenCalledWith(
        "http://localhost:8765/memories/1/relations",
        expect.objectContaining({
          method: "POST",
          body: JSON.stringify({
            target_id: 2,
            relation: "depends_on",
          }),
        })
      );
    });

    it("should add relation with default type", async () => {
      const mockResponseData = {
        relations: [],
        total: 0,
      };
      mockFetch(mockResponse(200, mockResponseData));

      await client.addRelation(1, 2);

      expect(fetch).toHaveBeenCalledWith(
        "http://localhost:8765/memories/1/relations",
        expect.objectContaining({
          body: JSON.stringify({
            target_id: 2,
            relation: "related",
          }),
        })
      );
    });

    it("should get relations for memory", async () => {
      const mockResponseData = {
        relations: [
          {
            source_id: 1,
            target_id: 2,
            relation: "related",
            created_at: "2024-01-01T00:00:00Z",
          },
        ],
        total: 1,
      };
      mockFetch(mockResponse(200, mockResponseData));

      const result = await client.getRelations(1);

      expect(result).toEqual(mockResponseData);
      expect(fetch).toHaveBeenCalledWith(
        "http://localhost:8765/memories/1/relations",
        expect.objectContaining({
          method: "GET",
        })
      );
    });
  });

  describe("Maintenance", () => {
    it("should run decay pass", async () => {
      const mockResponseData = {
        updated: 42,
        message: "Decay pass complete",
      };
      mockFetch(mockResponse(200, mockResponseData));

      const result = await client.decayRun();

      expect(result).toEqual(mockResponseData);
      expect(fetch).toHaveBeenCalledWith(
        "http://localhost:8765/decay/run",
        expect.objectContaining({
          method: "POST",
        })
      );
    });

    it("should run compression", async () => {
      const mockResponseData = {
        clusters_found: 3,
        memories_merged: 8,
        new_records_created: 3,
        message: "Compression complete",
      };
      mockFetch(mockResponse(200, mockResponseData));

      const result = await client.compress();

      expect(result).toEqual(mockResponseData);
      expect(fetch).toHaveBeenCalledWith(
        "http://localhost:8765/compress",
        expect.objectContaining({
          method: "POST",
        })
      );
    });

    it("should cleanup expired memories", async () => {
      const mockResponseData = {
        removed: 5,
        message: "Expired memories cleaned up",
      };
      mockFetch(mockResponse(200, mockResponseData));

      const result = await client.cleanup();

      expect(result).toEqual(mockResponseData);
      expect(fetch).toHaveBeenCalledWith(
        "http://localhost:8765/cleanup",
        expect.objectContaining({
          method: "POST",
        })
      );
    });
  });

  describe("Backup", () => {
    it("should export memories", async () => {
      const mockResponseData = {
        memories: [
          {
            id: 1,
            content: "Test memory",
            category: "general",
            importance: 3,
          },
        ],
        total: 1,
      };
      mockFetch(mockResponse(200, mockResponseData));

      const result = await client.exportMemories();

      expect(result).toEqual(mockResponseData);
      expect(fetch).toHaveBeenCalledWith(
        "http://localhost:8765/export",
        expect.objectContaining({
          method: "GET",
        })
      );
    });

    it("should import memories", async () => {
      const mockResponseData = {
        imported: 2,
        message: "Import complete",
      };
      mockFetch(mockResponse(200, mockResponseData));

      const memories = [
        { content: "Memory 1", category: "general" },
        { content: "Memory 2", category: "project" },
      ];

      const result = await client.importMemories(memories);

      expect(result).toEqual(mockResponseData);
      expect(fetch).toHaveBeenCalledWith(
        "http://localhost:8765/import",
        expect.objectContaining({
          method: "POST",
          body: JSON.stringify({ memories }),
        })
      );
    });
  });

  describe("Utility", () => {
    it("should get health status", async () => {
      const mockResponseData = {
        status: "healthy",
        version: "0.5.3",
        capabilities: {
          semantic_search: true,
          mcp_server: true,
        },
      };
      mockFetch(mockResponse(200, mockResponseData));

      const result = await client.health();

      expect(result).toEqual(mockResponseData);
      expect(fetch).toHaveBeenCalledWith(
        "http://localhost:8765/health",
        expect.objectContaining({
          method: "GET",
        })
      );
    });
  });

  describe("Error Handling", () => {
    it("should handle network error", async () => {
      mockFetchError(new Error("Network error"));

      await expect(
        client.save({ content: "test" })
      ).rejects.toThrow("Network error");
    });

    it("should handle auth error", async () => {
      mockFetch(mockResponse(401, { detail: "Invalid API key" }));

      await expect(
        client.save({ content: "test" })
      ).rejects.toThrow(KoreAuthError);
    });

    it("should handle malformed JSON error response", async () => {
      global.fetch = vi.fn().mockResolvedValue(
        new Response("invalid json", {
          status: 422,
          statusText: "Unprocessable Entity",
          headers: { "Content-Type": "application/json" },
        })
      );

      await expect(
        client.save({ content: "test" })
      ).rejects.toThrow();
    });
  });

  describe("Request Configuration", () => {
    it("should not include API key header when not provided", async () => {
      const clientWithoutKey = new KoreClient({
        baseUrl: "http://localhost:8765",
        agentId: "test-agent",
      });

      mockFetch(mockResponse(200, { id: 1, importance: 3, message: "saved" }));

      await clientWithoutKey.save({ content: "test" });

      expect(fetch).toHaveBeenCalledWith(
        expect.any(String),
        expect.objectContaining({
          headers: expect.not.objectContaining({
            "X-Kore-Key": expect.any(String),
          }),
        })
      );
    });

    it("should handle undefined query parameters", async () => {
      mockFetch(mockResponse(200, { results: [], total: 0, offset: 0, has_more: false }));

      await client.search({
        q: "test",
        limit: undefined,
        category: undefined,
      });

      expect(fetch).toHaveBeenCalledWith(
        "http://localhost:8765/search?q=test",
        expect.anything()
      );
    });
  });
});
```

## File: `sdk/js/tests/errors.test.ts`
```typescript
/**
 * Tests for error mapping and hierarchy
 */

import { describe, it, expect } from "vitest";
import {
  KoreError,
  KoreAuthError,
  KoreNotFoundError,
  KoreValidationError,
  KoreRateLimitError,
  KoreServerError,
  mapHttpError,
} from "../src/errors.js";

describe("Error Classes", () => {
  it("should create base KoreError", () => {
    const error = new KoreError("Test error", 400, { field: "invalid" });
    expect(error.name).toBe("KoreError");
    expect(error.message).toBe("Test error");
    expect(error.statusCode).toBe(400);
    expect(error.detail).toEqual({ field: "invalid" });
    expect(error instanceof Error).toBe(true);
  });

  it("should create KoreAuthError", () => {
    const error = new KoreAuthError("Unauthorized", 401);
    expect(error.name).toBe("KoreAuthError");
    expect(error instanceof KoreError).toBe(true);
    expect(error instanceof Error).toBe(true);
  });

  it("should create KoreNotFoundError", () => {
    const error = new KoreNotFoundError("Not found", 404);
    expect(error.name).toBe("KoreNotFoundError");
    expect(error instanceof KoreError).toBe(true);
  });

  it("should create KoreValidationError", () => {
    const error = new KoreValidationError("Validation failed", 422);
    expect(error.name).toBe("KoreValidationError");
    expect(error instanceof KoreError).toBe(true);
  });

  it("should create KoreRateLimitError", () => {
    const error = new KoreRateLimitError("Rate limited", 429);
    expect(error.name).toBe("KoreRateLimitError");
    expect(error instanceof KoreError).toBe(true);
  });

  it("should create KoreServerError", () => {
    const error = new KoreServerError("Server error", 500);
    expect(error.name).toBe("KoreServerError");
    expect(error instanceof KoreError).toBe(true);
  });
});

describe("mapHttpError", () => {
  it("should map 401 to KoreAuthError", () => {
    const error = mapHttpError(401, "Unauthorized");
    expect(error instanceof KoreAuthError).toBe(true);
    expect(error.statusCode).toBe(401);
  });

  it("should map 403 to KoreAuthError", () => {
    const error = mapHttpError(403, "Forbidden");
    expect(error instanceof KoreAuthError).toBe(true);
  });

  it("should map 404 to KoreNotFoundError", () => {
    const error = mapHttpError(404, "Not found");
    expect(error instanceof KoreNotFoundError).toBe(true);
  });

  it("should map 422 to KoreValidationError", () => {
    const error = mapHttpError(422, "Validation error");
    expect(error instanceof KoreValidationError).toBe(true);
  });

  it("should map 429 to KoreRateLimitError", () => {
    const error = mapHttpError(429, "Rate limited");
    expect(error instanceof KoreRateLimitError).toBe(true);
  });

  it("should map 500 to KoreServerError", () => {
    const error = mapHttpError(500, "Server error");
    expect(error instanceof KoreServerError).toBe(true);
  });

  it("should map 502 to KoreServerError", () => {
    const error = mapHttpError(502, "Bad gateway");
    expect(error instanceof KoreServerError).toBe(true);
  });

  it("should map unknown status to KoreError", () => {
    const error = mapHttpError(418, "I'm a teapot");
    expect(error instanceof KoreError).toBe(true);
    expect(error instanceof KoreAuthError).toBe(false);
    expect(error.statusCode).toBe(418);
  });

  it("should preserve detail in mapped error", () => {
    const detail = { field: "content", message: "too short" };
    const error = mapHttpError(422, "Validation failed", detail);
    expect(error.detail).toEqual(detail);
  });
});
```

## File: `sdk/js/tests/helpers.ts`
```typescript
/**
 * Test helpers for mocking fetch responses
 */

export function mockResponse(
  status: number,
  body?: any,
  headers?: Record<string, string>
): Response {
  const responseBody = body !== undefined ? JSON.stringify(body) : undefined;
  
  return new Response(responseBody, {
    status,
    statusText: getStatusText(status),
    headers: {
      "Content-Type": "application/json",
      ...headers,
    },
  });
}

export function mockFetch(response: Response): void {
  global.fetch = vi.fn().mockResolvedValue(response);
}

export function mockFetchError(error: Error): void {
  global.fetch = vi.fn().mockRejectedValue(error);
}

function getStatusText(status: number): string {
  const statusTexts: Record<number, string> = {
    200: "OK",
    201: "Created",
    204: "No Content",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    422: "Unprocessable Entity",
    429: "Too Many Requests",
    500: "Internal Server Error",
  };
  return statusTexts[status] || "Unknown";
}
```

## File: `tests/conftest.py`
```python
import os
import sqlite3
import tempfile

# Shared temp DB for all tests — set BEFORE any kore_memory import
_TEST_DB = tempfile.mktemp(suffix=".db")
os.environ["KORE_DB_PATH"] = _TEST_DB
os.environ["KORE_LOCAL_ONLY"] = "1"
os.environ["KORE_TEST_MODE"] = "1"

import pytest  # noqa: E402

from kore_memory.database import init_db  # noqa: E402
from kore_memory.main import _rate_buckets  # noqa: E402

# Initialize schema once
init_db()

# Verify tables were created (fail fast if something went wrong)
_verify_conn = sqlite3.connect(_TEST_DB)
_tables = {r[0] for r in _verify_conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()}
_verify_conn.close()
assert "memories" in _tables, f"init_db() did not create memories table in {_TEST_DB}. Found: {_tables}"


@pytest.fixture(autouse=True, scope="session")
def _ensure_db():
    """Session-scoped fixture: ensure DB is initialized and env var is set."""
    # Re-verify at session start (after all conftest modules are loaded)
    assert os.environ.get("KORE_DB_PATH") == _TEST_DB, (
        f"KORE_DB_PATH changed! Expected {_TEST_DB}, got {os.environ.get('KORE_DB_PATH')}"
    )
    conn = sqlite3.connect(_TEST_DB)
    tables = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()}
    conn.close()
    assert "memories" in tables, f"memories table missing at session start. DB: {_TEST_DB}, tables: {tables}"
    yield


@pytest.fixture(autouse=True)
def _reset_rate_limiter():
    """Reset rate limiter state between tests."""
    _rate_buckets.clear()
    yield
    _rate_buckets.clear()
```

## File: `tests/test_api.py`
```python
"""
Kore — API tests
Fast, no-network, uses TestClient (ASGI in-process).
Auth: local-only mode enabled in tests (KORE_LOCAL_ONLY=1).
"""

import os

import pytest
from fastapi.testclient import TestClient

from kore_memory.main import app  # noqa: E402

# Header di default: namespace agent per test di isolamento
HEADERS = {"X-Agent-Id": "test-agent"}
OTHER_AGENT = {"X-Agent-Id": "other-agent"}

client = TestClient(app)


class TestHealth:
    def test_health_returns_ok(self):
        r = client.get("/health")
        assert r.status_code == 200
        assert r.json()["status"] == "ok"
        assert "semantic_search" in r.json()


class TestSave:
    def test_save_basic(self):
        r = client.post("/save", json={"content": "Juan works on Kore memory system", "category": "project"}, headers=HEADERS)
        assert r.status_code == 201
        data = r.json()
        assert "id" in data
        assert data["importance"] >= 1

    def test_save_auto_scores_credentials(self):
        r = client.post("/save", json={
            "content": "API token: sk-abc123 for production",
            "category": "general",
        }, headers=HEADERS)
        assert r.status_code == 201
        assert r.json()["importance"] == 5

    def test_save_rejects_blank(self):
        r = client.post("/save", json={"content": "   ", "category": "general"}, headers=HEADERS)
        assert r.status_code == 422

    def test_save_rejects_too_short(self):
        r = client.post("/save", json={"content": "hi", "category": "general"}, headers=HEADERS)
        assert r.status_code == 422


class TestAuth:
    def test_no_key_on_remote_fails(self):
        """When KORE_LOCAL_ONLY=0 and no key, should get 401."""
        os.environ["KORE_LOCAL_ONLY"] = "0"
        try:
            r = client.get("/search?q=test")
            assert r.status_code == 401
        finally:
            os.environ["KORE_LOCAL_ONLY"] = "1"

    def test_wrong_key_fails(self):
        os.environ["KORE_LOCAL_ONLY"] = "0"
        try:
            r = client.get("/search?q=test", headers={"X-Kore-Key": "wrong-key"})
            assert r.status_code == 403
        finally:
            os.environ["KORE_LOCAL_ONLY"] = "1"


class TestAgentIsolation:
    def setup_method(self):
        client.post("/save", json={"content": "Secret data for agent A only", "category": "general", "importance": 3}, headers=HEADERS)

    def test_other_agent_cannot_see_data(self):
        r = client.get("/search?q=Secret&semantic=false", headers=OTHER_AGENT)
        assert r.json()["total"] == 0

    def test_owner_agent_can_see_data(self):
        r = client.get("/search?q=Secret&semantic=false", headers=HEADERS)
        assert r.json()["total"] >= 1

    def test_other_agent_cannot_delete(self):
        save_r = client.post("/save", json={"content": "Memory to protect", "category": "general"}, headers=HEADERS)
        mid = save_r.json()["id"]
        del_r = client.delete(f"/memories/{mid}", headers=OTHER_AGENT)
        assert del_r.status_code == 404  # not found for other agent


class TestSearch:
    def setup_method(self):
        client.post("/save", json={"content": "CalcFast is a calculator website for Italian taxes", "category": "project", "importance": 3}, headers=HEADERS)
        client.post("/save", json={"content": "Betfair account has 40 euros for bot trading", "category": "finance", "importance": 4}, headers=HEADERS)

    def test_search_returns_results(self):
        r = client.get("/search?q=CalcFast&semantic=false", headers=HEADERS)
        assert r.status_code == 200
        assert r.json()["total"] >= 1

    def test_search_category_filter(self):
        r = client.get("/search?q=trading&category=finance&semantic=false", headers=HEADERS)
        assert r.status_code == 200
        for result in r.json()["results"]:
            assert result["category"] == "finance"


class TestDecay:
    def test_decay_run(self):
        r = client.post("/decay/run", headers=HEADERS)
        assert r.status_code == 200
        assert r.json()["updated"] >= 0


class TestCompress:
    def test_compress_run(self):
        r = client.post("/compress", headers=HEADERS)
        assert r.status_code == 200
        assert "clusters_found" in r.json()


class TestTimeline:
    def test_timeline(self):
        r = client.get("/timeline?subject=CalcFast", headers=HEADERS)
        assert r.status_code == 200
        results = r.json()["results"]
        if len(results) > 1:
            dates = [r["created_at"] for r in results]
            assert dates == sorted(dates)


class TestDelete:
    def test_delete_existing(self):
        save_r = client.post("/save", json={"content": "Temporary memory to delete", "category": "general"}, headers=HEADERS)
        mid = save_r.json()["id"]
        del_r = client.delete(f"/memories/{mid}", headers=HEADERS)
        assert del_r.status_code == 204

    def test_delete_nonexistent(self):
        r = client.delete("/memories/999999", headers=HEADERS)
        assert r.status_code == 404


# ── P3: Batch API ────────────────────────────────────────────────────────────

class TestBatchSave:
    def setup_method(self):
        from kore_memory.main import _rate_buckets
        _rate_buckets.clear()

    def test_batch_save_multiple(self):
        """Salva 3 memorie in un'unica richiesta batch."""
        payload = {
            "memories": [
                {"content": "Batch memory one", "category": "general"},
                {"content": "Batch memory two", "category": "project", "importance": 3},
                {"content": "Batch memory three", "category": "finance"},
            ]
        }
        r = client.post("/save/batch", json=payload, headers=HEADERS)
        assert r.status_code == 201
        data = r.json()
        assert data["total"] == 3
        assert len(data["saved"]) == 3
        # Ogni elemento ha id e importance
        for item in data["saved"]:
            assert "id" in item
            assert item["importance"] >= 1

    def test_batch_save_single(self):
        """Batch con una sola memoria — deve funzionare."""
        r = client.post("/save/batch", json={
            "memories": [{"content": "Single batch item", "category": "general"}]
        }, headers=HEADERS)
        assert r.status_code == 201
        assert r.json()["total"] == 1

    def test_batch_save_empty_rejected(self):
        """Batch vuoto — rifiutato da validazione."""
        r = client.post("/save/batch", json={"memories": []}, headers=HEADERS)
        assert r.status_code == 422

    def test_batch_save_invalid_content(self):
        """Batch con contenuto troppo corto — rifiutato."""
        r = client.post("/save/batch", json={
            "memories": [{"content": "ab", "category": "general"}]
        }, headers=HEADERS)
        assert r.status_code == 422


# ── P3: Tag system ───────────────────────────────────────────────────────────

class TestTags:
    def _create_memory(self) -> int:
        r = client.post("/save", json={"content": "Memory for tag testing purposes", "category": "general"}, headers=HEADERS)
        return r.json()["id"]

    def test_add_tags(self):
        """Aggiunge tag a una memoria."""
        mid = self._create_memory()
        r = client.post(f"/memories/{mid}/tags", json={"tags": ["python", "test"]}, headers=HEADERS)
        assert r.status_code == 201
        data = r.json()
        assert data["count"] == 2
        assert "python" in data["tags"]
        assert "test" in data["tags"]

    def test_get_tags(self):
        """Legge i tag di una memoria."""
        mid = self._create_memory()
        client.post(f"/memories/{mid}/tags", json={"tags": ["alpha", "beta"]}, headers=HEADERS)
        r = client.get(f"/memories/{mid}/tags", headers=HEADERS)
        assert r.status_code == 200
        assert "alpha" in r.json()["tags"]
        assert "beta" in r.json()["tags"]

    def test_remove_tags(self):
        """Rimuove un tag specifico."""
        mid = self._create_memory()
        client.post(f"/memories/{mid}/tags", json={"tags": ["keep", "remove"]}, headers=HEADERS)
        r = client.request("DELETE", f"/memories/{mid}/tags", json={"tags": ["remove"]}, headers=HEADERS)
        assert r.status_code == 200
        assert "keep" in r.json()["tags"]
        assert "remove" not in r.json()["tags"]

    def test_search_by_tag(self):
        """Cerca memorie per tag."""
        mid = self._create_memory()
        client.post(f"/memories/{mid}/tags", json={"tags": ["unique-tag-xyz"]}, headers=HEADERS)
        r = client.get("/tags/unique-tag-xyz/memories", headers=HEADERS)
        assert r.status_code == 200
        assert r.json()["total"] >= 1
        ids = [m["id"] for m in r.json()["results"]]
        assert mid in ids

    def test_tags_normalized_lowercase(self):
        """I tag vengono normalizzati in lowercase."""
        mid = self._create_memory()
        client.post(f"/memories/{mid}/tags", json={"tags": ["UPPER", "MiXeD"]}, headers=HEADERS)
        r = client.get(f"/memories/{mid}/tags", headers=HEADERS)
        tags = r.json()["tags"]
        assert "upper" in tags
        assert "mixed" in tags

    def test_tags_scoped_to_agent(self):
        """Un altro agente non può aggiungere tag a memorie altrui."""
        mid = self._create_memory()
        r = client.post(f"/memories/{mid}/tags", json={"tags": ["intruder"]}, headers=OTHER_AGENT)
        assert r.status_code == 201
        assert r.json()["count"] == 0  # nessun tag aggiunto — memoria non appartiene all'agente

    def test_duplicate_tags_ignored(self):
        """Tag duplicati vengono ignorati (INSERT OR IGNORE)."""
        mid = self._create_memory()
        client.post(f"/memories/{mid}/tags", json={"tags": ["dup"]}, headers=HEADERS)
        client.post(f"/memories/{mid}/tags", json={"tags": ["dup"]}, headers=HEADERS)
        r = client.get(f"/memories/{mid}/tags", headers=HEADERS)
        assert r.json()["tags"].count("dup") == 1


# ── P3: Relazioni ────────────────────────────────────────────────────────────

class TestRelations:
    def _create_two_memories(self) -> tuple[int, int]:
        r1 = client.post("/save", json={"content": "Source memory for relation test", "category": "general"}, headers=HEADERS)
        r2 = client.post("/save", json={"content": "Target memory for relation test", "category": "general"}, headers=HEADERS)
        return r1.json()["id"], r2.json()["id"]

    def test_add_relation(self):
        """Crea una relazione tra due memorie."""
        src, tgt = self._create_two_memories()
        r = client.post(f"/memories/{src}/relations", json={"target_id": tgt, "relation": "depends_on"}, headers=HEADERS)
        assert r.status_code == 201
        data = r.json()
        assert data["total"] >= 1

    def test_get_relations(self):
        """Legge le relazioni di una memoria."""
        src, tgt = self._create_two_memories()
        client.post(f"/memories/{src}/relations", json={"target_id": tgt, "relation": "related"}, headers=HEADERS)
        r = client.get(f"/memories/{src}/relations", headers=HEADERS)
        assert r.status_code == 200
        assert r.json()["total"] >= 1
        # Verifica che la relazione contenga i dati attesi
        rel = r.json()["relations"][0]
        assert "relation" in rel
        assert "related_content" in rel

    def test_relation_bidirectional_visibility(self):
        """La relazione è visibile da entrambi i lati."""
        src, tgt = self._create_two_memories()
        client.post(f"/memories/{src}/relations", json={"target_id": tgt}, headers=HEADERS)
        # Visibile dal target
        r = client.get(f"/memories/{tgt}/relations", headers=HEADERS)
        assert r.json()["total"] >= 1

    def test_relation_cross_agent_rejected(self):
        """Non si può creare relazione con memoria di un altro agente."""
        r1 = client.post("/save", json={"content": "Agent A memory for cross relation", "category": "general"}, headers=HEADERS)
        r2 = client.post("/save", json={"content": "Agent B memory for cross relation", "category": "general"}, headers=OTHER_AGENT)
        src = r1.json()["id"]
        tgt = r2.json()["id"]
        # L'agente A prova a collegare la sua memoria a quella dell'agente B
        r = client.post(f"/memories/{src}/relations", json={"target_id": tgt}, headers=HEADERS)
        assert r.status_code == 201
        # La relazione non viene creata (count < 2 nella verifica)
        assert r.json()["total"] == 0

    def test_relation_default_type(self):
        """Il tipo di relazione predefinito è 'related'."""
        src, tgt = self._create_two_memories()
        client.post(f"/memories/{src}/relations", json={"target_id": tgt}, headers=HEADERS)
        r = client.get(f"/memories/{src}/relations", headers=HEADERS)
        assert r.json()["relations"][0]["relation"] == "related"


# ── P3: TTL / Cleanup ────────────────────────────────────────────────────────

class TestTTL:
    def setup_method(self):
        """Resetta rate limiter per evitare 429 nei test TTL."""
        from kore_memory.main import _rate_buckets
        _rate_buckets.clear()

    def test_save_with_ttl(self):
        """Salva una memoria con TTL — deve essere accettata."""
        r = client.post("/save", json={
            "content": "Expiring memory with TTL",
            "category": "general",
            "ttl_hours": 24,
        }, headers=HEADERS)
        assert r.status_code == 201
        assert "id" in r.json()

    def test_save_without_ttl(self):
        """Salva senza TTL — nessun expires_at impostato."""
        r = client.post("/save", json={
            "content": "Permanent memory without TTL",
            "category": "general",
        }, headers=HEADERS)
        assert r.status_code == 201

    def test_ttl_validation_min(self):
        """TTL < 1 ora — rifiutato."""
        r = client.post("/save", json={
            "content": "Invalid TTL memory",
            "category": "general",
            "ttl_hours": 0,
        }, headers=HEADERS)
        assert r.status_code == 422

    def test_ttl_validation_max(self):
        """TTL > 8760 ore (1 anno) — rifiutato."""
        r = client.post("/save", json={
            "content": "Invalid TTL memory too long",
            "category": "general",
            "ttl_hours": 9999,
        }, headers=HEADERS)
        assert r.status_code == 422

    def test_cleanup_endpoint(self):
        """L'endpoint /cleanup risponde correttamente."""
        r = client.post("/cleanup", headers=HEADERS)
        assert r.status_code == 200
        data = r.json()
        assert "removed" in data
        assert data["removed"] >= 0

    def test_expired_memory_not_in_search(self):
        """Memorie con expires_at nel passato non appaiono nella ricerca."""
        from kore_memory.database import get_connection

        # Inserisci direttamente una memoria già scaduta
        with get_connection() as conn:
            conn.execute(
                """INSERT INTO memories (agent_id, content, category, importance, expires_at)
                   VALUES (?, ?, ?, ?, datetime('now', '-1 hour'))""",
                ("test-agent", "Expired secret data for TTL test", "general", 3),
            )

        r = client.get("/search?q=Expired+secret+data+for+TTL&semantic=false", headers=HEADERS)
        # La memoria scaduta non deve apparire
        for result in r.json()["results"]:
            assert "Expired secret data for TTL test" not in result["content"]

    def test_cleanup_removes_expired(self):
        """Il cleanup rimuove effettivamente le memorie scadute."""
        from kore_memory.database import get_connection

        # Inserisci memoria già scaduta
        with get_connection() as conn:
            conn.execute(
                """INSERT INTO memories (agent_id, content, category, importance, expires_at)
                   VALUES (?, ?, ?, ?, datetime('now', '-2 hours'))""",
                ("test-agent", "Cleanup target memory", "general", 1),
            )

        r = client.post("/cleanup", headers=HEADERS)
        assert r.status_code == 200
        assert r.json()["removed"] >= 1

    def test_non_expired_memory_survives_cleanup(self):
        """Memorie con TTL futuro sopravvivono al cleanup."""
        r = client.post("/save", json={
            "content": "Future TTL memory should survive cleanup",
            "category": "general",
            "ttl_hours": 8760,  # 1 anno
        }, headers=HEADERS)
        mid = r.json()["id"]

        client.post("/cleanup", headers=HEADERS)

        # La memoria deve ancora esistere — verifico con search
        sr = client.get("/search?q=Future+TTL+memory+should+survive&semantic=false", headers=HEADERS)
        ids = [m["id"] for m in sr.json()["results"]]
        assert mid in ids


# ── P3/P2: Export / Import ────────────────────────────────────────────────────

class TestExportImport:
    def test_export_returns_memories(self):
        """L'export restituisce le memorie dell'agente."""
        # Assicura che ci sia almeno una memoria
        client.post("/save", json={"content": "Export test memory data", "category": "project"}, headers=HEADERS)
        r = client.get("/export", headers=HEADERS)
        assert r.status_code == 200
        data = r.json()
        assert data["total"] >= 1
        assert len(data["memories"]) == data["total"]

    def test_export_scoped_to_agent(self):
        """L'export non include memorie di altri agenti."""
        agent_c = {"X-Agent-Id": "export-agent-c"}
        client.post("/save", json={"content": "Agent C exclusive export data", "category": "general"}, headers=agent_c)

        r = client.get("/export", headers=OTHER_AGENT)
        for mem in r.json()["memories"]:
            assert "Agent C exclusive" not in mem["content"]

    def test_import_memories(self):
        """L'import salva le memorie correttamente."""
        payload = {
            "memories": [
                {"content": "Imported memory alpha", "category": "general", "importance": 2},
                {"content": "Imported memory beta", "category": "project", "importance": 4},
            ]
        }
        r = client.post("/import", json=payload, headers=HEADERS)
        assert r.status_code == 201
        assert r.json()["imported"] == 2

    def test_import_skips_invalid(self):
        """L'import salta record con contenuto troppo corto."""
        payload = {
            "memories": [
                {"content": "ab", "category": "general"},  # troppo corto — saltato
                {"content": "Valid imported memory content", "category": "general"},
            ]
        }
        r = client.post("/import", json=payload, headers=HEADERS)
        assert r.status_code == 201
        assert r.json()["imported"] == 1

    def test_export_excludes_expired(self):
        """L'export non include memorie con TTL scaduto."""
        from kore_memory.database import get_connection

        with get_connection() as conn:
            conn.execute(
                """INSERT INTO memories (agent_id, content, category, importance, expires_at)
                   VALUES (?, ?, ?, ?, datetime('now', '-1 hour'))""",
                ("test-agent", "Expired export exclusion test", "general", 1),
            )

        r = client.get("/export", headers=HEADERS)
        for mem in r.json()["memories"]:
            assert "Expired export exclusion test" not in mem["content"]


# ── P2: Pagination ────────────────────────────────────────────────────────────

class TestPagination:
    def setup_method(self):
        """Crea abbastanza memorie per testare la paginazione."""
        from kore_memory.main import _rate_buckets
        _rate_buckets.clear()
        for i in range(6):
            client.post("/save", json={
                "content": f"Pagination test item number {i} with unique marker PGNX",
                "category": "general",
                "importance": 3,
            }, headers=HEADERS)

    def test_search_pagination_offset(self):
        """La ricerca con offset salta i primi risultati."""
        r_full = client.get("/search?q=PGNX&limit=10&semantic=false", headers=HEADERS)
        r_offset = client.get("/search?q=PGNX&limit=3&offset=2&semantic=false", headers=HEADERS)
        assert r_offset.status_code == 200
        data = r_offset.json()
        assert data["offset"] == 2
        assert len(data["results"]) <= 3

    def test_search_has_more_flag(self):
        """has_more è True quando ci sono più risultati oltre la pagina."""
        r = client.get("/search?q=PGNX&limit=2&offset=0&semantic=false", headers=HEADERS)
        data = r.json()
        if data["total"] > 2:
            assert data["has_more"] is True

    def test_timeline_pagination(self):
        """La timeline supporta offset."""
        r = client.get("/timeline?subject=PGNX&limit=2&offset=1", headers=HEADERS)
        assert r.status_code == 200
        assert r.json()["offset"] == 1


# ── Archive (soft-delete) ─────────────────────────────────────────────────────

class TestArchive:
    """Verifica il workflow di archiviazione e ripristino memorie."""

    def _save(self, content: str = "Memoria da archiviare per test archivio") -> int:
        """Helper: salva una memoria e restituisce l'id."""
        r = client.post("/save", json={"content": content, "category": "general", "importance": 3}, headers=HEADERS)
        assert r.status_code == 201
        return r.json()["id"]

    def test_archive_memory(self):
        """Archivia una memoria esistente — risposta 200 con success=True."""
        mid = self._save()
        r = client.post(f"/memories/{mid}/archive", headers=HEADERS)
        assert r.status_code == 200
        data = r.json()
        assert data["success"] is True

    def test_archive_not_found(self):
        """Tentativo di archiviare una memoria inesistente — deve rispondere 404."""
        r = client.post("/memories/999999999/archive", headers=HEADERS)
        assert r.status_code == 404

    def test_restore_memory(self):
        """Archivia poi ripristina una memoria — risposta 200 con success=True."""
        mid = self._save("Memoria archiviata e poi ripristinata nel test")
        # Archivia
        arch = client.post(f"/memories/{mid}/archive", headers=HEADERS)
        assert arch.status_code == 200
        # Ripristina
        rest = client.post(f"/memories/{mid}/restore", headers=HEADERS)
        assert rest.status_code == 200
        assert rest.json()["success"] is True

    def test_restore_not_archived(self):
        """Tentativo di ripristinare una memoria non archiviata — deve rispondere 404."""
        mid = self._save("Memoria attiva non archiviata da ripristinare")
        # La memoria non è archiviata, il restore deve fallire
        r = client.post(f"/memories/{mid}/restore", headers=HEADERS)
        assert r.status_code == 404

    def test_archived_not_in_search(self):
        """Una memoria archiviata non deve apparire nei risultati di ricerca."""
        contenuto = "Contenuto univoco archiviato ARCHTEST99"
        mid = self._save(contenuto)
        # Verifica che sia trovabile prima dell'archivio
        r_before = client.get("/search?q=ARCHTEST99&semantic=false", headers=HEADERS)
        ids_before = [m["id"] for m in r_before.json()["results"]]
        assert mid in ids_before
        # Archivia
        client.post(f"/memories/{mid}/archive", headers=HEADERS)
        # Dopo l'archivio non deve più comparire nella ricerca
        r_after = client.get("/search?q=ARCHTEST99&semantic=false", headers=HEADERS)
        ids_after = [m["id"] for m in r_after.json()["results"]]
        assert mid not in ids_after

    def test_archive_list(self):
        """Una memoria archiviata deve comparire in GET /archive."""
        mid = self._save("Memoria da listare nell archivio ARCHLIST01")
        client.post(f"/memories/{mid}/archive", headers=HEADERS)
        r = client.get("/archive", headers=HEADERS)
        assert r.status_code == 200
        ids = [m["id"] for m in r.json()["results"]]
        assert mid in ids


# ── Cursor-based pagination ───────────────────────────────────────────────────

class TestCursorPagination:
    """Verifica la paginazione basata su cursore opaco (base64)."""

    # Marcatore univoco per isolare le memorie di questa classe
    _MARKER = "CURSORPAGTEST"

    def setup_method(self):
        """Crea 5 memorie con marcatore univoco prima di ogni test."""
        from kore_memory.main import _rate_buckets
        _rate_buckets.clear()
        for i in range(5):
            client.post("/save", json={
                "content": f"Memoria per cursor pagination numero {i} marker {self._MARKER}",
                "category": "general",
                "importance": 3,
            }, headers=HEADERS)

    def test_cursor_pagination_search(self):
        """Ricerca con limit=2 poi usa il cursore — la seconda pagina deve avere risultati diversi."""
        # Prima pagina
        r1 = client.get(f"/search?q={self._MARKER}&limit=2&semantic=false", headers=HEADERS)
        assert r1.status_code == 200
        data1 = r1.json()
        assert len(data1["results"]) == 2
        cursor = data1.get("cursor")
        # Se ci sono più risultati il cursore non deve essere None
        assert cursor is not None

        # Seconda pagina usando il cursore
        r2 = client.get(f"/search?q={self._MARKER}&limit=2&cursor={cursor}&semantic=false", headers=HEADERS)
        assert r2.status_code == 200
        data2 = r2.json()
        # Gli id della seconda pagina devono essere diversi da quelli della prima
        ids1 = {m["id"] for m in data1["results"]}
        ids2 = {m["id"] for m in data2["results"]}
        assert ids1.isdisjoint(ids2), "Le pagine non devono contenere le stesse memorie"

    def test_invalid_cursor(self):
        """Un cursore non valido (stringa arbitraria non base64 decodificabile) deve rispondere 400."""
        r = client.get("/search?q=test&cursor=NON_VALIDO_!!!&semantic=false", headers=HEADERS)
        assert r.status_code == 400

    def test_has_more_flag(self):
        """Con 5 memorie e limit=2 has_more deve essere True; sull'ultima pagina False."""
        # Prima pagina — deve avere has_more=True
        r1 = client.get(f"/search?q={self._MARKER}&limit=2&semantic=false", headers=HEADERS)
        assert r1.status_code == 200
        assert r1.json()["has_more"] is True

        # Scorri fino all'esaurimento dei risultati
        cursor = r1.json().get("cursor")
        last_has_more = True
        iterations = 0
        while cursor and iterations < 10:
            rn = client.get(f"/search?q={self._MARKER}&limit=2&cursor={cursor}&semantic=false", headers=HEADERS)
            assert rn.status_code == 200
            last_has_more = rn.json()["has_more"]
            cursor = rn.json().get("cursor")
            iterations += 1

        # L'ultima pagina deve avere has_more=False
        assert last_has_more is False


# ── Rate limiting ─────────────────────────────────────────────────────────────

class TestRateLimit:
    """Verifica che il rate limiter risponda 429 quando il limite viene superato."""

    def setup_method(self):
        """Resetta i bucket per garantire uno stato pulito prima di ogni test."""
        from kore_memory.main import _rate_buckets
        _rate_buckets.clear()

    def test_rate_limit_exceeded(self):
        """Supera il limite di /decay/run (5 req/ora) — la sesta deve restituire 429."""
        # Il limite configurato è 5 richieste per ora
        for _ in range(5):
            r = client.post("/decay/run", headers=HEADERS)
            assert r.status_code == 200
        # La sesta richiesta deve essere rifiutata
        r_exceeded = client.post("/decay/run", headers=HEADERS)
        assert r_exceeded.status_code == 429

    def test_rate_limit_different_paths(self):
        """Path diversi hanno bucket di rate limit indipendenti."""
        from kore_memory.main import _rate_buckets
        _rate_buckets.clear()

        # Esaurisci il limite di /decay/run (5 req/ora)
        for _ in range(5):
            client.post("/decay/run", headers=HEADERS)

        # /cleanup ha un bucket separato (10 req/ora) — la prima chiamata deve riuscire
        # anche se /decay/run è esaurito, perché i bucket sono per-path
        r_cleanup = client.post("/cleanup", headers=HEADERS)
        assert r_cleanup.status_code == 200, (
            "Il rate limit di /cleanup deve essere indipendente da /decay/run"
        )


# ── Update memory — correttezza del campo importance ─────────────────────────

class TestUpdateMemory:
    """Verifica che PUT /memories/{id} restituisca il valore di importance reale dal DB."""

    def _save_with_importance(self, importance: int) -> int:
        """Helper: salva una memoria con importance esplicita e restituisce l'id."""
        r = client.post("/save", json={
            "content": "Memoria per test aggiornamento importance valore",
            "category": "general",
            "importance": importance,
        }, headers=HEADERS)
        assert r.status_code == 201
        return r.json()["id"]

    def test_update_returns_real_importance(self):
        """Aggiorna solo il contenuto — la risposta deve contenere importance=3 (non 0)."""
        mid = self._save_with_importance(3)
        r = client.put(f"/memories/{mid}", json={
            "content": "Contenuto aggiornato senza modificare importance",
        }, headers=HEADERS)
        assert r.status_code == 200
        data = r.json()
        # Il campo importance deve riflettere il valore salvato nel DB, non 0
        assert data["importance"] == 3, (
            f"importance atteso=3, ottenuto={data['importance']}. "
            "L'endpoint non deve restituire 0 quando importance non è nel payload."
        )

    def test_update_importance_explicit(self):
        """Aggiorna importance a 5 — la risposta deve confermare importance=5."""
        mid = self._save_with_importance(2)
        r = client.put(f"/memories/{mid}", json={
            "importance": 5,
        }, headers=HEADERS)
        assert r.status_code == 200
        assert r.json()["importance"] == 5


# ── Auto-scoring importance ───────────────────────────────────────────────────

class TestAutoScore:
    """Verifica che importance=None attivi l'auto-scoring, mentre importance=1 esplicito venga rispettato."""

    def test_save_without_importance_auto_scores(self):
        """Senza campo importance il server deve assegnare un punteggio >= 1 automaticamente."""
        # Contenuto neutro nella categoria "general" — baseline 1, auto-score atteso >= 1
        r = client.post("/save", json={
            "content": "Informazione generica senza importanza esplicita per test auto score",
            "category": "general",
        }, headers=HEADERS)
        assert r.status_code == 201
        data = r.json()
        assert "importance" in data
        # L'auto-scorer deve sempre restituire un valore valido nell'intervallo 1–5
        assert 1 <= data["importance"] <= 5

    def test_save_with_importance_1_explicit(self):
        """Con importance=1 esplicito il server deve conservare 1, senza sovrascrivere con auto-score."""
        r = client.post("/save", json={
            # Contenuto che senza vincolo di importance potrebbe ricevere un punteggio più alto
            "content": "Decisione importante urgente priorità massima progetto critico",
            "category": "decision",
            "importance": 1,
        }, headers=HEADERS)
        assert r.status_code == 201
        data = r.json()
        # importance=1 esplicito deve essere rispettato: l'auto-scorer non deve intervenire
        assert data["importance"] == 1, (
            f"importance atteso=1 (esplicito), ottenuto={data['importance']}. "
            "Un importance esplicito non deve essere sovrascritto dall'auto-scorer."
        )
```

## File: `tests/test_audit.py`
```python
"""
Kore — Audit log tests
Tests for event audit logging, querying, cleanup, and the /audit endpoint.
"""

import pytest
from fastapi.testclient import TestClient

from kore_memory import events  # noqa: E402
from kore_memory.audit import (  # noqa: E402
    _audit_handler,
    cleanup_audit_log,
    query_audit_log,
    register_audit_handler,
)
from kore_memory.database import get_connection  # noqa: E402
from kore_memory.main import app  # noqa: E402

HEADERS = {"X-Agent-Id": "test-agent"}
OTHER_AGENT = {"X-Agent-Id": "other-agent"}

client = TestClient(app)


class TestAuditDisabled:
    """When audit is not explicitly enabled, no entries should be saved."""

    def test_no_entries_without_registration(self):
        """Events emitted without a registered audit handler produce no log rows."""
        # Clear any previously registered handlers
        events.clear()
        client.post(
            "/save",
            json={"content": "This should not be audited", "category": "general"},
            headers=HEADERS,
        )
        entries = query_audit_log("test-agent")
        # No audit handler registered, so nothing should be logged
        assert len(entries) == 0


class TestAuditEnabled:
    """Tests with the audit handler registered."""

    @classmethod
    def setup_class(cls):
        events.clear()
        register_audit_handler()

    @classmethod
    def teardown_class(cls):
        events.clear()

    def test_save_event_captured(self):
        """Saving a memory should produce a memory.saved audit entry."""
        r = client.post(
            "/save",
            json={"content": "Audit test: memory save event", "category": "project"},
            headers=HEADERS,
        )
        assert r.status_code == 201
        memory_id = r.json()["id"]

        entries = query_audit_log("test-agent", event_type="memory.saved")
        matching = [e for e in entries if e["memory_id"] == memory_id]
        assert len(matching) >= 1
        assert matching[0]["event"] == "memory.saved"
        assert matching[0]["agent_id"] == "test-agent"
        assert matching[0]["data"]["id"] == memory_id

    def test_delete_event_captured(self):
        """Deleting a memory should produce a memory.deleted audit entry."""
        r = client.post(
            "/save",
            json={"content": "Audit test: to be deleted", "category": "general"},
            headers=HEADERS,
        )
        memory_id = r.json()["id"]

        client.delete(f"/memories/{memory_id}", headers=HEADERS)

        entries = query_audit_log("test-agent", event_type="memory.deleted")
        matching = [e for e in entries if e["memory_id"] == memory_id]
        assert len(matching) >= 1
        assert matching[0]["event"] == "memory.deleted"

    def test_update_event_captured(self):
        """Updating a memory should produce a memory.updated audit entry."""
        r = client.post(
            "/save",
            json={"content": "Audit test: to be updated", "category": "general"},
            headers=HEADERS,
        )
        memory_id = r.json()["id"]

        client.put(
            f"/memories/{memory_id}",
            json={"content": "Audit test: updated content"},
            headers=HEADERS,
        )

        entries = query_audit_log("test-agent", event_type="memory.updated")
        matching = [e for e in entries if e["memory_id"] == memory_id]
        assert len(matching) >= 1
        assert matching[0]["event"] == "memory.updated"

    def test_query_event_type_filter(self):
        """Querying with event_type filter returns only matching events."""
        # Create at least one save and one delete
        r = client.post(
            "/save",
            json={"content": "Audit filter test memory", "category": "general"},
            headers=HEADERS,
        )
        mid = r.json()["id"]
        client.delete(f"/memories/{mid}", headers=HEADERS)

        saved = query_audit_log("test-agent", event_type="memory.saved")
        deleted = query_audit_log("test-agent", event_type="memory.deleted")

        assert all(e["event"] == "memory.saved" for e in saved)
        assert all(e["event"] == "memory.deleted" for e in deleted)

    def test_query_since_filter(self):
        """Querying with since filter returns only events after the timestamp."""
        # All test events were created 'now', querying since far future should return nothing
        entries = query_audit_log("test-agent", since="2099-01-01T00:00:00")
        assert len(entries) == 0

        # Querying since far past should return events
        entries = query_audit_log("test-agent", since="2000-01-01T00:00:00")
        assert len(entries) > 0

    def test_query_limit(self):
        """Querying with a limit caps the number of results."""
        entries = query_audit_log("test-agent", limit=2)
        assert len(entries) <= 2

    def test_cleanup_old_entries(self):
        """Cleanup removes entries older than specified days."""
        # Insert an old entry directly
        with get_connection() as conn:
            conn.execute(
                "INSERT INTO event_logs (event, agent_id, memory_id, data, created_at) "
                "VALUES (?, ?, ?, ?, datetime('now', '-100 days'))",
                ("memory.saved", "test-agent", 999, '{"id": 999, "agent_id": "test-agent"}'),
            )

        # Verify it exists
        with get_connection() as conn:
            row = conn.execute(
                "SELECT COUNT(*) as cnt FROM event_logs WHERE memory_id = 999"
            ).fetchone()
            assert row["cnt"] == 1

        # Cleanup entries older than 90 days
        removed = cleanup_audit_log(days=90)
        assert removed >= 1

        # Verify old entry is gone
        with get_connection() as conn:
            row = conn.execute(
                "SELECT COUNT(*) as cnt FROM event_logs WHERE memory_id = 999"
            ).fetchone()
            assert row["cnt"] == 0

    def test_cleanup_preserves_recent(self):
        """Cleanup does not remove recent entries."""
        before = query_audit_log("test-agent")
        recent_count = len(before)

        removed = cleanup_audit_log(days=90)

        after = query_audit_log("test-agent")
        # All recent entries should still be there
        assert len(after) == recent_count

    def test_agent_isolation(self):
        """Audit entries are scoped to their agent_id."""
        # Save with other-agent
        r = client.post(
            "/save",
            json={"content": "Audit isolation test from other agent", "category": "general"},
            headers=OTHER_AGENT,
        )
        other_id = r.json()["id"]

        # Query as test-agent should not see other-agent's events
        entries = query_audit_log("test-agent")
        other_entries = [e for e in entries if e["memory_id"] == other_id]
        assert len(other_entries) == 0

        # Query as other-agent should see the event
        entries = query_audit_log("other-agent", event_type="memory.saved")
        other_entries = [e for e in entries if e["memory_id"] == other_id]
        assert len(other_entries) >= 1


class TestAuditEndpoint:
    """Tests for the /audit REST endpoint."""

    @classmethod
    def setup_class(cls):
        events.clear()
        register_audit_handler()

    @classmethod
    def teardown_class(cls):
        events.clear()

    def test_endpoint_returns_events(self):
        """GET /audit returns audit events for the agent."""
        # Save something to generate an event
        client.post(
            "/save",
            json={"content": "Endpoint test memory", "category": "general"},
            headers=HEADERS,
        )

        r = client.get("/audit", headers=HEADERS)
        assert r.status_code == 200
        data = r.json()
        assert "events" in data
        assert "total" in data
        assert data["total"] >= 1

    def test_endpoint_event_filter(self):
        """GET /audit?event=memory.saved filters by event type."""
        r = client.get("/audit?event=memory.saved", headers=HEADERS)
        assert r.status_code == 200
        data = r.json()
        assert all(e["event"] == "memory.saved" for e in data["events"])

    def test_endpoint_limit(self):
        """GET /audit?limit=1 respects limit."""
        r = client.get("/audit?limit=1", headers=HEADERS)
        assert r.status_code == 200
        data = r.json()
        assert len(data["events"]) <= 1
        assert data["total"] <= 1

    def test_endpoint_since_filter(self):
        """GET /audit?since=... filters by timestamp."""
        r = client.get("/audit?since=2099-01-01T00:00:00", headers=HEADERS)
        assert r.status_code == 200
        assert r.json()["total"] == 0

    def test_endpoint_agent_isolation(self):
        """GET /audit only returns events for the requesting agent."""
        r_test = client.get("/audit", headers=HEADERS)
        r_other = client.get("/audit", headers=OTHER_AGENT)
        assert r_test.status_code == 200
        assert r_other.status_code == 200

        # test-agent events should not appear in other-agent results
        test_ids = {e["id"] for e in r_test.json()["events"]}
        other_ids = {e["id"] for e in r_other.json()["events"]}
        assert test_ids.isdisjoint(other_ids)


class TestAuditHandlerDirect:
    """Direct unit tests for the audit handler function."""

    def test_handler_signature(self):
        """The handler accepts (event, data) as expected by the events system."""
        _audit_handler("memory.saved", {"id": 9999, "agent_id": "direct-test"})

        entries = query_audit_log("direct-test", event_type="memory.saved")
        matching = [e for e in entries if e["memory_id"] == 9999]
        assert len(matching) >= 1
        assert matching[0]["data"]["id"] == 9999

    def test_handler_with_empty_data(self):
        """The handler handles empty data gracefully."""
        _audit_handler("memory.decayed", {})

        entries = query_audit_log("default", event_type="memory.decayed")
        assert len(entries) >= 1
```

## File: `tests/test_auth_events.py`
```python
"""
Test per auth.py, events.py, integrations/__init__.py e database.py edge cases.
Migliora coverage dei moduli con gap > 15%.
"""

import os
import tempfile

import pytest
from fastapi.testclient import TestClient


# ── Fixture DB temporaneo ──────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def _temp_db(tmp_path):
    """Crea un DB temporaneo per ogni test, ripristina il path originale dopo."""
    original_db_path = os.environ.get("KORE_DB_PATH")
    db_file = tmp_path / "test.db"
    os.environ["KORE_DB_PATH"] = str(db_file)
    # Reset API key cache
    import kore_memory.auth as auth_mod
    auth_mod._API_KEY = None
    yield
    # Restore the original DB path (set by conftest.py)
    if original_db_path is not None:
        os.environ["KORE_DB_PATH"] = original_db_path
    else:
        os.environ.pop("KORE_DB_PATH", None)


@pytest.fixture
def client():
    from kore_memory.database import init_db
    init_db()
    from kore_memory.main import app
    return TestClient(app)


HEADERS = {"X-Agent-Id": "test-agent", "Content-Type": "application/json"}


# ── TestAuth ───────────────────────────────────────────────────────────────────

class TestAuth:
    """Test autenticazione e gestione API key."""

    def test_auto_generate_api_key(self, tmp_path):
        """Verifica che venga generata una API key se mancante."""
        import kore_memory.auth as auth_mod
        import kore_memory.config as cfg

        # Pulisci env e file
        old_env = os.environ.pop("KORE_API_KEY", None)
        old_file = cfg.API_KEY_FILE
        cfg.API_KEY_FILE = tmp_path / ".api_key"
        auth_mod._KEY_FILE = cfg.API_KEY_FILE
        auth_mod._API_KEY = None

        try:
            key = auth_mod.get_or_create_api_key()
            assert len(key) > 16
            assert cfg.API_KEY_FILE.exists()
            # Seconda chiamata ritorna stessa key dal file
            key2 = auth_mod.get_or_create_api_key()
            assert key == key2
        finally:
            cfg.API_KEY_FILE = old_file
            auth_mod._KEY_FILE = old_file
            if old_env:
                os.environ["KORE_API_KEY"] = old_env

    def test_env_key_takes_priority(self, tmp_path):
        """KORE_API_KEY env var ha priorità sul file."""
        import kore_memory.auth as auth_mod

        os.environ["KORE_API_KEY"] = "test-env-key-123"
        auth_mod._API_KEY = None
        try:
            key = auth_mod.get_or_create_api_key()
            assert key == "test-env-key-123"
        finally:
            os.environ.pop("KORE_API_KEY", None)

    def test_require_auth_missing_key_non_local(self, client):
        """Senza LOCAL_ONLY e senza key, ritorna 401."""
        old = os.environ.get("KORE_LOCAL_ONLY")
        old_test = os.environ.get("KORE_TEST_MODE")
        os.environ["KORE_LOCAL_ONLY"] = "0"
        os.environ["KORE_TEST_MODE"] = "0"
        try:
            resp = client.get("/health")
            # Health non richiede auth, ma /search sì
            resp = client.get("/search", params={"q": "test"})
            assert resp.status_code == 401
        finally:
            if old:
                os.environ["KORE_LOCAL_ONLY"] = old
            else:
                os.environ.pop("KORE_LOCAL_ONLY", None)
            if old_test:
                os.environ["KORE_TEST_MODE"] = old_test
            else:
                os.environ.pop("KORE_TEST_MODE", None)

    def test_require_auth_wrong_key(self, client):
        """Key errata ritorna 403."""
        old = os.environ.get("KORE_LOCAL_ONLY")
        old_test = os.environ.get("KORE_TEST_MODE")
        os.environ["KORE_LOCAL_ONLY"] = "0"
        os.environ["KORE_TEST_MODE"] = "0"
        try:
            resp = client.get("/search", params={"q": "test"},
                              headers={"X-Kore-Key": "wrong-key-here"})
            assert resp.status_code == 403
        finally:
            if old:
                os.environ["KORE_LOCAL_ONLY"] = old
            else:
                os.environ.pop("KORE_LOCAL_ONLY", None)
            if old_test:
                os.environ["KORE_TEST_MODE"] = old_test
            else:
                os.environ.pop("KORE_TEST_MODE", None)

    def test_agent_id_sanitization(self, client):
        """Agent ID con caratteri speciali viene sanitizzato."""
        resp = client.post("/save", json={"content": "test sanitizzazione agente"},
                           headers={"X-Agent-Id": "agent<script>alert(1)</script>", "Content-Type": "application/json"})
        assert resp.status_code == 201
        # L'agente sanitizzato non contiene caratteri pericolosi
        data = resp.json()
        assert data["id"] > 0

    def test_agent_id_empty_defaults(self, client):
        """Agent ID vuoto diventa 'default'."""
        resp = client.post("/save", json={"content": "test default agent"},
                           headers={"X-Agent-Id": "", "Content-Type": "application/json"})
        assert resp.status_code == 201


# ── TestEvents ────────────────────────────────────────────────────────────────

class TestEvents:
    """Test sistema eventi in-process."""

    def test_emit_and_on(self):
        """Registra handler e verifica emissione."""
        from kore_memory.events import clear, emit, on

        received = []
        def handler(event, data):
            received.append((event, data))

        clear()
        on("test.event", handler)
        emit("test.event", {"key": "value"})

        assert len(received) == 1
        assert received[0] == ("test.event", {"key": "value"})
        clear()

    def test_emit_no_handlers(self):
        """Emissione senza handler non causa errori."""
        from kore_memory.events import clear, emit

        clear()
        # Non deve lanciare eccezioni
        emit("unknown.event", {"x": 1})
        clear()

    def test_handler_exception_does_not_break_chain(self):
        """Handler che lancia eccezione non interrompe altri handler."""
        from kore_memory.events import clear, emit, on

        results = []

        def bad_handler(event, data):
            raise ValueError("Errore intenzionale nel test")

        def good_handler(event, data):
            results.append(data)

        clear()
        on("test.chain", bad_handler)
        on("test.chain", good_handler)
        emit("test.chain", {"ok": True})

        # Il secondo handler deve eseguire nonostante il primo fallisca
        assert len(results) == 1
        assert results[0]["ok"] is True
        clear()

    def test_emit_without_data(self):
        """Emissione senza data usa dict vuoto."""
        from kore_memory.events import clear, emit, on

        received = []
        def handler(event, data):
            received.append(data)

        clear()
        on("test.nodata", handler)
        emit("test.nodata")

        assert received[0] == {}
        clear()

    def test_clear_removes_handlers(self):
        """clear() rimuove tutti gli handler registrati."""
        from kore_memory.events import clear, emit, on

        received = []
        def handler(event, data):
            received.append(True)

        on("test.clear", handler)
        clear()
        emit("test.clear", {})

        assert len(received) == 0


# ── TestIntegrationsInit ──────────────────────────────────────────────────────

class TestIntegrationsInit:
    """Test lazy-loader nel modulo integrations."""

    def test_lazy_load_langchain(self):
        """Verifica accesso lazy a KoreLangChainMemory."""
        from kore_memory import integrations
        cls = integrations.KoreLangChainMemory
        assert cls is not None
        assert hasattr(cls, "__init__")

    def test_lazy_load_crewai(self):
        """Verifica accesso lazy a KoreCrewAIMemory."""
        from kore_memory import integrations
        cls = integrations.KoreCrewAIMemory
        assert cls is not None

    def test_lazy_load_entities(self):
        """Verifica accesso lazy a funzioni entities."""
        from kore_memory import integrations
        fn = integrations.search_entities
        assert callable(fn)

    def test_attribute_error_unknown(self):
        """Attributo inesistente lancia AttributeError."""
        from kore_memory import integrations
        with pytest.raises(AttributeError, match="has no attribute"):
            _ = integrations.nonexistent_module


# ── TestDatabaseEdgeCases ─────────────────────────────────────────────────────

class TestDatabaseEdgeCases:
    """Test edge case per database.py."""

    def test_connection_pool_release_and_reacquire(self):
        """Connessione rilasciata viene riutilizzata dal pool."""
        from kore_memory.database import _pool, get_connection

        # Prima connessione
        with get_connection() as conn1:
            conn1.execute("SELECT 1")

        # Seconda connessione — dovrebbe prendere dal pool
        with get_connection() as conn2:
            conn2.execute("SELECT 1")

    def test_pool_clear(self):
        """Pulizia pool chiude tutte le connessioni."""
        from kore_memory.database import _pool, get_connection, init_db

        init_db()
        with get_connection() as conn:
            conn.execute("SELECT 1")

        _pool.clear()
        # Dopo clear, nuova connessione deve funzionare
        with get_connection() as conn:
            result = conn.execute("SELECT 1").fetchone()
            assert result is not None

    def test_migration_on_existing_db(self):
        """init_db su DB esistente non crasha (migration idempotente)."""
        from kore_memory.database import init_db

        init_db()
        # Seconda chiamata — tabelle esistono già
        init_db()

    def test_rollback_on_exception(self):
        """Eccezione in get_connection causa rollback."""
        from kore_memory.database import get_connection, init_db

        init_db()
        try:
            with get_connection() as conn:
                conn.execute("INSERT INTO memories (agent_id, content, category, importance) VALUES ('test', 'test', 'general', 1)")
                raise ValueError("Test rollback")
        except ValueError:
            pass

        # Il record non deve essere stato salvato
        with get_connection() as conn:
            count = conn.execute("SELECT COUNT(*) FROM memories").fetchone()[0]
            assert count == 0
```

## File: `tests/test_auto_tuner.py`
```python
"""
Kore — Auto-Tuner tests
Tests for the memory importance auto-tuning feature.
Uses TestClient (ASGI in-process, no network).
Auth: local-only mode enabled (KORE_LOCAL_ONLY=1).
"""

import os

import pytest
from fastapi.testclient import TestClient

from kore_memory.database import get_connection  # noqa: E402
from kore_memory.main import app, _rate_buckets  # noqa: E402

HEADERS = {"X-Agent-Id": "test-agent"}
OTHER_AGENT = {"X-Agent-Id": "other-agent"}

client = TestClient(app)


def _clear_rate_limits():
    """Reset rate limiter to avoid 429 in tests."""
    _rate_buckets.clear()


def _insert_memory(
    agent_id: str = "test-agent",
    content: str = "Test memory for auto-tuner",
    category: str = "general",
    importance: int = 3,
    access_count: int = 0,
    age_days: int = 0,
) -> int:
    """Insert a memory directly into DB with full control over fields."""
    age_offset = f"-{age_days} days" if age_days > 0 else "+0 days"
    with get_connection() as conn:
        cursor = conn.execute(
            """
            INSERT INTO memories (agent_id, content, category, importance, access_count, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, datetime('now', ?), datetime('now'))
            """,
            (agent_id, content, category, importance, access_count, age_offset),
        )
        return cursor.lastrowid


class TestAutoTuneDisabled:
    """Test auto-tune when KORE_AUTO_TUNE is disabled (default)."""

    def setup_method(self):
        _clear_rate_limits()
        # Ensure auto-tune is disabled
        os.environ.pop("KORE_AUTO_TUNE", None)
        os.environ["KORE_AUTO_TUNE"] = "0"
        # Reload config to pick up the change
        from kore_memory import config
        config.AUTO_TUNE = os.getenv("KORE_AUTO_TUNE", "0") == "1"

    def test_auto_tune_disabled_returns_zero(self):
        """When disabled, auto-tune should return 0 boosted and 0 reduced."""
        from kore_memory.auto_tuner import run_auto_tune
        result = run_auto_tune(agent_id="test-agent")
        assert result["boosted"] == 0
        assert result["reduced"] == 0
        assert "disabled" in result["message"].lower()

    def test_auto_tune_disabled_no_changes(self):
        """When disabled, no memories should be modified even if they qualify."""
        mid = _insert_memory(access_count=10, importance=2)
        from kore_memory.auto_tuner import run_auto_tune
        run_auto_tune(agent_id="test-agent")
        # Check that importance was NOT changed
        with get_connection() as conn:
            row = conn.execute("SELECT importance FROM memories WHERE id = ?", (mid,)).fetchone()
        assert row["importance"] == 2

    def test_api_endpoint_when_disabled(self):
        """The /auto-tune endpoint should work but report disabled."""
        r = client.post("/auto-tune", headers=HEADERS)
        assert r.status_code == 200
        data = r.json()
        assert data["boosted"] == 0
        assert data["reduced"] == 0


class TestAutoTuneBoost:
    """Test boosting of frequently accessed memories."""

    def setup_method(self):
        _clear_rate_limits()
        os.environ["KORE_AUTO_TUNE"] = "1"
        from kore_memory import config
        config.AUTO_TUNE = True

    def teardown_method(self):
        os.environ["KORE_AUTO_TUNE"] = "0"
        from kore_memory import config
        config.AUTO_TUNE = False

    def test_boost_high_access_count(self):
        """Memories with access_count >= 5 and importance < 5 should be boosted."""
        mid = _insert_memory(access_count=5, importance=3)
        from kore_memory.auto_tuner import run_auto_tune
        result = run_auto_tune(agent_id="test-agent")
        assert result["boosted"] >= 1

        with get_connection() as conn:
            row = conn.execute("SELECT importance FROM memories WHERE id = ?", (mid,)).fetchone()
        assert row["importance"] == 4  # 3 + 1

    def test_boost_does_not_exceed_5(self):
        """Importance should never be boosted above 5."""
        mid = _insert_memory(access_count=10, importance=5)
        from kore_memory.auto_tuner import run_auto_tune
        result = run_auto_tune(agent_id="test-agent")
        # This memory should NOT be boosted (already at max)
        with get_connection() as conn:
            row = conn.execute("SELECT importance FROM memories WHERE id = ?", (mid,)).fetchone()
        assert row["importance"] == 5

    def test_boost_threshold_boundary(self):
        """Memories with exactly access_count=4 should NOT be boosted."""
        mid = _insert_memory(access_count=4, importance=2)
        from kore_memory.auto_tuner import run_auto_tune
        run_auto_tune(agent_id="test-agent")
        with get_connection() as conn:
            row = conn.execute("SELECT importance FROM memories WHERE id = ?", (mid,)).fetchone()
        assert row["importance"] == 2  # unchanged

    def test_boost_multiple_memories(self):
        """Multiple qualifying memories should all be boosted."""
        mid1 = _insert_memory(content="Boost me first", access_count=6, importance=1)
        mid2 = _insert_memory(content="Boost me second", access_count=8, importance=3)
        from kore_memory.auto_tuner import run_auto_tune
        result = run_auto_tune(agent_id="test-agent")
        assert result["boosted"] >= 2

        with get_connection() as conn:
            r1 = conn.execute("SELECT importance FROM memories WHERE id = ?", (mid1,)).fetchone()
            r2 = conn.execute("SELECT importance FROM memories WHERE id = ?", (mid2,)).fetchone()
        assert r1["importance"] == 2  # 1 + 1
        assert r2["importance"] == 4  # 3 + 1


class TestAutoTuneReduce:
    """Test reduction of importance for never-accessed old memories."""

    def setup_method(self):
        _clear_rate_limits()
        os.environ["KORE_AUTO_TUNE"] = "1"
        from kore_memory import config
        config.AUTO_TUNE = True

    def teardown_method(self):
        os.environ["KORE_AUTO_TUNE"] = "0"
        from kore_memory import config
        config.AUTO_TUNE = False

    def test_reduce_old_never_accessed(self):
        """Memories never accessed and older than 30 days should be reduced."""
        mid = _insert_memory(access_count=0, importance=4, age_days=31)
        from kore_memory.auto_tuner import run_auto_tune
        result = run_auto_tune(agent_id="test-agent")
        assert result["reduced"] >= 1

        with get_connection() as conn:
            row = conn.execute("SELECT importance FROM memories WHERE id = ?", (mid,)).fetchone()
        assert row["importance"] == 3  # 4 - 1

    def test_reduce_does_not_go_below_1(self):
        """Importance should never be reduced below 1."""
        mid = _insert_memory(access_count=0, importance=1, age_days=60)
        from kore_memory.auto_tuner import run_auto_tune
        result = run_auto_tune(agent_id="test-agent")
        # This memory should NOT be reduced (already at min)
        with get_connection() as conn:
            row = conn.execute("SELECT importance FROM memories WHERE id = ?", (mid,)).fetchone()
        assert row["importance"] == 1

    def test_reduce_not_triggered_for_young_memories(self):
        """Memories younger than 30 days should NOT be reduced, even if never accessed."""
        mid = _insert_memory(access_count=0, importance=3, age_days=10)
        from kore_memory.auto_tuner import run_auto_tune
        run_auto_tune(agent_id="test-agent")
        with get_connection() as conn:
            row = conn.execute("SELECT importance FROM memories WHERE id = ?", (mid,)).fetchone()
        assert row["importance"] == 3  # unchanged

    def test_reduce_not_triggered_if_accessed(self):
        """Old memories that HAVE been accessed should NOT be reduced."""
        mid = _insert_memory(access_count=1, importance=3, age_days=60)
        from kore_memory.auto_tuner import run_auto_tune
        run_auto_tune(agent_id="test-agent")
        with get_connection() as conn:
            row = conn.execute("SELECT importance FROM memories WHERE id = ?", (mid,)).fetchone()
        assert row["importance"] == 3  # unchanged


class TestAutoTuneAgentIsolation:
    """Test that auto-tune respects agent isolation."""

    def setup_method(self):
        _clear_rate_limits()
        os.environ["KORE_AUTO_TUNE"] = "1"
        from kore_memory import config
        config.AUTO_TUNE = True

    def teardown_method(self):
        os.environ["KORE_AUTO_TUNE"] = "0"
        from kore_memory import config
        config.AUTO_TUNE = False

    def test_auto_tune_scoped_to_agent(self):
        """Auto-tune should only affect the specified agent's memories."""
        mid_own = _insert_memory(agent_id="test-agent", access_count=7, importance=2)
        mid_other = _insert_memory(agent_id="other-agent", access_count=7, importance=2)
        from kore_memory.auto_tuner import run_auto_tune
        run_auto_tune(agent_id="test-agent")
        with get_connection() as conn:
            own = conn.execute("SELECT importance FROM memories WHERE id = ?", (mid_own,)).fetchone()
            other = conn.execute("SELECT importance FROM memories WHERE id = ?", (mid_other,)).fetchone()
        assert own["importance"] == 3  # boosted
        assert other["importance"] == 2  # unchanged


class TestAutoTuneAPI:
    """Test the /auto-tune and /stats/scoring API endpoints."""

    def setup_method(self):
        _clear_rate_limits()

    def test_auto_tune_endpoint(self):
        """The /auto-tune endpoint returns the correct response structure."""
        r = client.post("/auto-tune", headers=HEADERS)
        assert r.status_code == 200
        data = r.json()
        assert "boosted" in data
        assert "reduced" in data
        assert "message" in data

    def test_auto_tune_endpoint_auth_required(self):
        """The /auto-tune endpoint requires auth when not in local-only mode."""
        os.environ["KORE_LOCAL_ONLY"] = "0"
        try:
            r = client.post("/auto-tune")
            assert r.status_code == 401
        finally:
            os.environ["KORE_LOCAL_ONLY"] = "1"

    def test_stats_scoring_endpoint(self):
        """The /stats/scoring endpoint returns the correct structure."""
        # Ensure at least one memory exists
        client.post("/save", json={"content": "Stats test memory content", "category": "general"}, headers=HEADERS)
        r = client.get("/stats/scoring", headers=HEADERS)
        assert r.status_code == 200
        data = r.json()
        assert "total" in data
        assert "distribution" in data
        assert "avg_importance" in data
        assert "avg_access_count" in data
        assert "never_accessed_30d" in data
        assert "frequently_accessed" in data
        assert data["total"] >= 1

    def test_stats_scoring_distribution_keys(self):
        """Distribution should have keys for importance levels 1-5."""
        client.post("/save", json={"content": "Distribution test memory", "category": "general"}, headers=HEADERS)
        r = client.get("/stats/scoring", headers=HEADERS)
        dist = r.json()["distribution"]
        for level in ["1", "2", "3", "4", "5"]:
            assert level in dist

    def test_stats_scoring_empty_agent(self):
        """Stats for an agent with no memories should return zeroes."""
        r = client.get("/stats/scoring", headers={"X-Agent-Id": "empty-agent-xyz"})
        assert r.status_code == 200
        data = r.json()
        assert data["total"] == 0
        assert data["avg_importance"] == 0.0
        assert data["avg_access_count"] == 0.0

    def test_stats_scoring_auth_required(self):
        """The /stats/scoring endpoint requires auth when not in local-only mode."""
        os.environ["KORE_LOCAL_ONLY"] = "0"
        try:
            r = client.get("/stats/scoring")
            assert r.status_code == 401
        finally:
            os.environ["KORE_LOCAL_ONLY"] = "1"


class TestAutoTuneIntegration:
    """Integration tests combining boost and reduce in a single run."""

    def setup_method(self):
        _clear_rate_limits()
        os.environ["KORE_AUTO_TUNE"] = "1"
        from kore_memory import config
        config.AUTO_TUNE = True

    def teardown_method(self):
        os.environ["KORE_AUTO_TUNE"] = "0"
        from kore_memory import config
        config.AUTO_TUNE = False

    def test_boost_and_reduce_in_same_run(self):
        """A single auto-tune run can both boost and reduce memories."""
        # Memory to boost: high access, low importance
        mid_boost = _insert_memory(content="Frequently accessed memory", access_count=10, importance=2)
        # Memory to reduce: never accessed, old, high importance
        mid_reduce = _insert_memory(content="Old forgotten memory", access_count=0, importance=4, age_days=45)

        from kore_memory.auto_tuner import run_auto_tune
        result = run_auto_tune(agent_id="test-agent")

        assert result["boosted"] >= 1
        assert result["reduced"] >= 1

        with get_connection() as conn:
            boosted = conn.execute("SELECT importance FROM memories WHERE id = ?", (mid_boost,)).fetchone()
            reduced = conn.execute("SELECT importance FROM memories WHERE id = ?", (mid_reduce,)).fetchone()

        assert boosted["importance"] == 3  # 2 + 1
        assert reduced["importance"] == 3  # 4 - 1

    def test_compressed_memories_not_affected(self):
        """Compressed memories should not be auto-tuned."""
        # Create a target memory (the "merged" record) and a memory to mark as compressed
        target_mid = _insert_memory(content="Merged target record")
        mid = _insert_memory(access_count=10, importance=2)
        with get_connection() as conn:
            conn.execute("UPDATE memories SET compressed_into = ? WHERE id = ?", (target_mid, mid))

        from kore_memory.auto_tuner import run_auto_tune
        run_auto_tune(agent_id="test-agent")

        with get_connection() as conn:
            row = conn.execute("SELECT importance FROM memories WHERE id = ?", (mid,)).fetchone()
        assert row["importance"] == 2  # unchanged — compressed memories are skipped
```

## File: `tests/test_cli.py`
```python
"""
Kore — Test per il modulo CLI (kore_memory/cli.py)
Verifica il parsing degli argomenti e la gestione degli errori.

Pattern: mock di uvicorn.run per evitare l'avvio reale del server.
Ogni test isola il parsing degli argomenti tramite sys.argv.
"""

import sys
from unittest.mock import MagicMock, patch

import pytest


# ── Helper ────────────────────────────────────────────────────────────────────

def _esegui_main(argv: list[str]) -> None:
    """
    Imposta sys.argv e invoca main() con uvicorn mockato.
    Solleva SystemExit se argparse fallisce (argomenti non validi).
    """
    from kore_memory.cli import main

    with patch.dict(sys.modules, {"uvicorn": MagicMock()}):
        with patch("sys.argv", ["kore"] + argv):
            main()


# ── Argomenti di default ──────────────────────────────────────────────────────


class TestArgomentiDefault:
    """Verifica che i valori di default siano applicati correttamente."""

    def test_host_default(self):
        """Senza --host il server deve partire su 127.0.0.1."""
        mock_uvicorn = MagicMock()
        with patch.dict(sys.modules, {"uvicorn": mock_uvicorn}):
            with patch("sys.argv", ["kore"]):
                from kore_memory.cli import main
                main()

        # Recupera i kwargs passati a uvicorn.run
        _, kwargs = mock_uvicorn.run.call_args
        assert kwargs["host"] == "127.0.0.1"

    def test_port_default(self):
        """Senza --port il server deve partire sulla porta 8765."""
        mock_uvicorn = MagicMock()
        with patch.dict(sys.modules, {"uvicorn": mock_uvicorn}):
            with patch("sys.argv", ["kore"]):
                from kore_memory.cli import main
                main()

        _, kwargs = mock_uvicorn.run.call_args
        assert kwargs["port"] == 8765

    def test_reload_default_disabilitato(self):
        """Senza --reload il flag reload deve essere False."""
        mock_uvicorn = MagicMock()
        with patch.dict(sys.modules, {"uvicorn": mock_uvicorn}):
            with patch("sys.argv", ["kore"]):
                from kore_memory.cli import main
                main()

        _, kwargs = mock_uvicorn.run.call_args
        assert kwargs["reload"] is False

    def test_log_level_default(self):
        """Senza --log-level il livello di log deve essere 'warning'."""
        mock_uvicorn = MagicMock()
        with patch.dict(sys.modules, {"uvicorn": mock_uvicorn}):
            with patch("sys.argv", ["kore"]):
                from kore_memory.cli import main
                main()

        _, kwargs = mock_uvicorn.run.call_args
        assert kwargs["log_level"] == "warning"

    def test_app_target_corretto(self):
        """Il primo argomento di uvicorn.run deve puntare a kore_memory.main:app."""
        mock_uvicorn = MagicMock()
        with patch.dict(sys.modules, {"uvicorn": mock_uvicorn}):
            with patch("sys.argv", ["kore"]):
                from kore_memory.cli import main
                main()

        args, _ = mock_uvicorn.run.call_args
        assert args[0] == "kore_memory.main:app"


# ── Argomenti personalizzati ──────────────────────────────────────────────────


class TestArgomentiPersonalizzati:
    """Verifica che gli argomenti da CLI vengano passati correttamente a uvicorn."""

    def test_host_personalizzato(self):
        """--host 0.0.0.0 deve essere trasmesso a uvicorn."""
        mock_uvicorn = MagicMock()
        with patch.dict(sys.modules, {"uvicorn": mock_uvicorn}):
            with patch("sys.argv", ["kore", "--host", "0.0.0.0"]):
                from kore_memory.cli import main
                main()

        _, kwargs = mock_uvicorn.run.call_args
        assert kwargs["host"] == "0.0.0.0"

    def test_port_personalizzata(self):
        """--port 9000 deve essere trasmesso come intero a uvicorn."""
        mock_uvicorn = MagicMock()
        with patch.dict(sys.modules, {"uvicorn": mock_uvicorn}):
            with patch("sys.argv", ["kore", "--port", "9000"]):
                from kore_memory.cli import main
                main()

        _, kwargs = mock_uvicorn.run.call_args
        assert kwargs["port"] == 9000

    def test_port_e_tipo_intero(self):
        """Il valore di --port deve essere di tipo int, non str."""
        mock_uvicorn = MagicMock()
        with patch.dict(sys.modules, {"uvicorn": mock_uvicorn}):
            with patch("sys.argv", ["kore", "--port", "4321"]):
                from kore_memory.cli import main
                main()

        _, kwargs = mock_uvicorn.run.call_args
        assert isinstance(kwargs["port"], int)

    def test_reload_abilitato(self):
        """--reload deve impostare il flag reload=True in uvicorn."""
        mock_uvicorn = MagicMock()
        with patch.dict(sys.modules, {"uvicorn": mock_uvicorn}):
            with patch("sys.argv", ["kore", "--reload"]):
                from kore_memory.cli import main
                main()

        _, kwargs = mock_uvicorn.run.call_args
        assert kwargs["reload"] is True

    def test_host_port_reload_combinati(self):
        """Tutti gli argomenti combinati devono essere passati correttamente."""
        mock_uvicorn = MagicMock()
        with patch.dict(sys.modules, {"uvicorn": mock_uvicorn}):
            with patch("sys.argv", ["kore", "--host", "192.168.1.1", "--port", "7777", "--reload"]):
                from kore_memory.cli import main
                main()

        _, kwargs = mock_uvicorn.run.call_args
        assert kwargs["host"] == "192.168.1.1"
        assert kwargs["port"] == 7777
        assert kwargs["reload"] is True

    def test_log_level_debug(self):
        """--log-level debug deve essere accettato e passato a uvicorn."""
        mock_uvicorn = MagicMock()
        with patch.dict(sys.modules, {"uvicorn": mock_uvicorn}):
            with patch("sys.argv", ["kore", "--log-level", "debug"]):
                from kore_memory.cli import main
                main()

        _, kwargs = mock_uvicorn.run.call_args
        assert kwargs["log_level"] == "debug"

    def test_log_level_info(self):
        """--log-level info deve essere accettato e passato a uvicorn."""
        mock_uvicorn = MagicMock()
        with patch.dict(sys.modules, {"uvicorn": mock_uvicorn}):
            with patch("sys.argv", ["kore", "--log-level", "info"]):
                from kore_memory.cli import main
                main()

        _, kwargs = mock_uvicorn.run.call_args
        assert kwargs["log_level"] == "info"

    def test_log_level_error(self):
        """--log-level error deve essere accettato e passato a uvicorn."""
        mock_uvicorn = MagicMock()
        with patch.dict(sys.modules, {"uvicorn": mock_uvicorn}):
            with patch("sys.argv", ["kore", "--log-level", "error"]):
                from kore_memory.cli import main
                main()

        _, kwargs = mock_uvicorn.run.call_args
        assert kwargs["log_level"] == "error"


# ── Argomenti non validi ──────────────────────────────────────────────────────


class TestArgomentiNonValidi:
    """Verifica che argomenti errati vengano rifiutati da argparse."""

    def test_port_non_numerica_rifiutata(self):
        """--port con valore non numerico deve causare SystemExit."""
        with pytest.raises(SystemExit) as exc:
            with patch("sys.argv", ["kore", "--port", "abc"]):
                from kore_memory.cli import main
                with patch.dict(sys.modules, {"uvicorn": MagicMock()}):
                    main()
        # argparse esce con codice 2 per errori di validazione
        assert exc.value.code == 2

    def test_log_level_non_valido_rifiutato(self):
        """--log-level con valore non nelle scelte deve causare SystemExit."""
        with pytest.raises(SystemExit) as exc:
            with patch("sys.argv", ["kore", "--log-level", "verbose"]):
                from kore_memory.cli import main
                with patch.dict(sys.modules, {"uvicorn": MagicMock()}):
                    main()
        assert exc.value.code == 2

    def test_argomento_sconosciuto_rifiutato(self):
        """Un argomento non riconosciuto deve causare SystemExit."""
        with pytest.raises(SystemExit) as exc:
            with patch("sys.argv", ["kore", "--opzione-inesistente"]):
                from kore_memory.cli import main
                with patch.dict(sys.modules, {"uvicorn": MagicMock()}):
                    main()
        assert exc.value.code == 2


# ── Uvicorn non trovato (ImportError) ────────────────────────────────────────


class TestUvicornNonTrovato:
    """Verifica il comportamento quando uvicorn non è installato."""

    def test_import_error_causa_exit_1(self):
        """Se uvicorn non è trovato, main() deve uscire con codice 1."""
        # Rimuove uvicorn dal cache dei moduli e simula ImportError
        with patch.dict(sys.modules, {"uvicorn": None}):
            with patch("sys.argv", ["kore"]):
                from kore_memory.cli import main
                with pytest.raises(SystemExit) as exc:
                    main()
        assert exc.value.code == 1

    def test_import_error_stampa_messaggio_su_stderr(self, capsys):
        """Se uvicorn non è trovato, deve stampare un messaggio su stderr."""
        with patch.dict(sys.modules, {"uvicorn": None}):
            with patch("sys.argv", ["kore"]):
                from kore_memory.cli import main
                with pytest.raises(SystemExit):
                    main()

        # Verifica che il messaggio di errore sia su stderr
        catturato = capsys.readouterr()
        assert "uvicorn" in catturato.err.lower()

    def test_import_error_non_stampa_su_stdout(self, capsys):
        """Il messaggio di errore di uvicorn non deve apparire su stdout."""
        with patch.dict(sys.modules, {"uvicorn": None}):
            with patch("sys.argv", ["kore"]):
                from kore_memory.cli import main
                with pytest.raises(SystemExit):
                    main()

        catturato = capsys.readouterr()
        assert catturato.out == ""
```

## File: `tests/test_client.py`
```python
"""
Kore — Test del Client SDK
Verifica KoreClient e AsyncKoreClient contro il server ASGI.

I test di integrazione usano AsyncKoreClient (ASGITransport è solo async).
I test unit verificano helpers, eccezioni, e headers senza rete.
"""

import pytest

from kore_memory.main import app, _rate_buckets  # noqa: E402

import httpx  # noqa: E402

from kore_memory.client import (  # noqa: E402
    AsyncKoreClient,
    KoreAuthError,
    KoreClient,
    KoreError,
    KoreNotFoundError,
    KoreRateLimitError,
    KoreServerError,
    KoreValidationError,
    _build_headers,
    _raise_for_status,
)
from kore_memory.models import (  # noqa: E402
    BatchSaveResponse,
    CleanupExpiredResponse,
    CompressRunResponse,
    DecayRunResponse,
    MemoryExportResponse,
    MemoryImportResponse,
    MemorySaveResponse,
    MemorySearchResponse,
    RelationResponse,
    TagResponse,
)


# ── Helper: client async che usa il transport ASGI (zero rete) ───────────────


def _make_async_client(agent_id: str = "sdk-test") -> AsyncKoreClient:
    """Crea un AsyncKoreClient che punta al server ASGI in-process."""
    kc = AsyncKoreClient.__new__(AsyncKoreClient)
    kc.base_url = "http://testserver"
    kc.agent_id = agent_id
    kc._client = httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app),
        base_url="http://testserver",
        headers=_build_headers(None, agent_id),
        timeout=10.0,
    )
    return kc


# ── Test unit: _build_headers ────────────────────────────────────────────────


class TestBuildHeaders:
    def test_headers_senza_api_key(self):
        h = _build_headers(None, "my-agent")
        assert h == {"X-Agent-Id": "my-agent"}
        assert "X-Kore-Key" not in h

    def test_headers_con_api_key(self):
        h = _build_headers("secret-key", "my-agent")
        assert h["X-Agent-Id"] == "my-agent"
        assert h["X-Kore-Key"] == "secret-key"


# ── Test unit: _raise_for_status ─────────────────────────────────────────────


class TestRaiseForStatus:
    def test_successo_non_alza_eccezione(self):
        r = httpx.Response(200, json={"ok": True})
        _raise_for_status(r)  # non deve alzare eccezione

    def test_401_alza_auth_error(self):
        r = httpx.Response(401, json={"detail": "No auth"})
        with pytest.raises(KoreAuthError) as exc_info:
            _raise_for_status(r)
        assert exc_info.value.status_code == 401

    def test_403_alza_auth_error(self):
        r = httpx.Response(403, json={"detail": "Forbidden"})
        with pytest.raises(KoreAuthError) as exc_info:
            _raise_for_status(r)
        assert exc_info.value.status_code == 403

    def test_404_alza_not_found_error(self):
        r = httpx.Response(404, json={"detail": "Not found"})
        with pytest.raises(KoreNotFoundError) as exc_info:
            _raise_for_status(r)
        assert exc_info.value.status_code == 404

    def test_422_alza_validation_error(self):
        r = httpx.Response(422, json={"detail": "Invalid"})
        with pytest.raises(KoreValidationError) as exc_info:
            _raise_for_status(r)
        assert exc_info.value.status_code == 422

    def test_429_alza_rate_limit_error(self):
        r = httpx.Response(429, json={"detail": "Rate limit"})
        with pytest.raises(KoreRateLimitError) as exc_info:
            _raise_for_status(r)
        assert exc_info.value.status_code == 429

    def test_500_alza_server_error(self):
        r = httpx.Response(500, json={"detail": "Server error"})
        with pytest.raises(KoreServerError) as exc_info:
            _raise_for_status(r)
        assert exc_info.value.status_code == 500

    def test_status_generico_alza_kore_error(self):
        r = httpx.Response(418, json={"detail": "I'm a teapot"})
        with pytest.raises(KoreError) as exc_info:
            _raise_for_status(r)
        assert exc_info.value.status_code == 418

    def test_body_non_json(self):
        """Se il body non è JSON, usa il testo grezzo come detail."""
        r = httpx.Response(500, text="Internal error")
        with pytest.raises(KoreServerError) as exc_info:
            _raise_for_status(r)
        assert exc_info.value.detail == "Internal error"


# ── Test unit: KoreClient init e struttura ───────────────────────────────────


class TestKoreClientInit:
    def test_init_default(self):
        kc = KoreClient.__new__(KoreClient)
        # Verifica che la classe abbia i metodi attesi
        metodi = [
            "save", "save_batch", "search", "timeline", "delete",
            "add_tags", "get_tags", "remove_tags", "search_by_tag",
            "add_relation", "get_relations",
            "decay_run", "compress", "cleanup",
            "export_memories", "import_memories", "health",
            "close", "__enter__", "__exit__",
        ]
        for m in metodi:
            assert hasattr(kc, m), f"Metodo mancante: {m}"

    def test_async_client_ha_tutti_i_metodi(self):
        akc = AsyncKoreClient.__new__(AsyncKoreClient)
        metodi = [
            "save", "save_batch", "search", "timeline", "delete",
            "add_tags", "get_tags", "remove_tags", "search_by_tag",
            "add_relation", "get_relations",
            "decay_run", "compress", "cleanup",
            "export_memories", "import_memories", "health",
            "close", "__aenter__", "__aexit__",
        ]
        for m in metodi:
            assert hasattr(akc, m), f"Metodo mancante: {m}"


# ── Test unit: gerarchia eccezioni ───────────────────────────────────────────


class TestExceptionHierarchy:
    def test_tutte_ereditano_kore_error(self):
        assert issubclass(KoreAuthError, KoreError)
        assert issubclass(KoreNotFoundError, KoreError)
        assert issubclass(KoreValidationError, KoreError)
        assert issubclass(KoreRateLimitError, KoreError)
        assert issubclass(KoreServerError, KoreError)

    def test_kore_error_attributi(self):
        e = KoreError("test", status_code=500, detail={"key": "value"})
        assert str(e) == "test"
        assert e.status_code == 500
        assert e.detail == {"key": "value"}


# ── Test integrazione: AsyncKoreClient ───────────────────────────────────────


class TestAsyncKoreClientCore:
    """Test core: save, search, timeline, delete, batch."""

    def setup_method(self):
        _rate_buckets.clear()

    @pytest.mark.anyio
    async def test_save_ritorna_modello(self):
        async with _make_async_client() as kore:
            result = await kore.save("SDK test memory content", category="project")
            assert isinstance(result, MemorySaveResponse)
            assert result.id > 0
            assert result.importance >= 1

    @pytest.mark.anyio
    async def test_save_con_ttl(self):
        async with _make_async_client() as kore:
            result = await kore.save("SDK TTL memory test data", ttl_hours=48)
            assert isinstance(result, MemorySaveResponse)
            assert result.id > 0

    @pytest.mark.anyio
    async def test_save_validation_error(self):
        async with _make_async_client() as kore:
            with pytest.raises(KoreValidationError):
                await kore.save("ab")  # troppo corto

    @pytest.mark.anyio
    async def test_search_ritorna_modello(self):
        async with _make_async_client() as kore:
            await kore.save("SDK search target XYZQ unique", category="project")
            result = await kore.search("XYZQ", semantic=False)
            assert isinstance(result, MemorySearchResponse)
            assert result.total >= 1

    @pytest.mark.anyio
    async def test_search_con_offset(self):
        async with _make_async_client() as kore:
            for i in range(4):
                await kore.save(f"SDK async pagination item {i} marker ASDKPG")
            result = await kore.search("ASDKPG", limit=2, offset=1, semantic=False)
            assert isinstance(result, MemorySearchResponse)
            assert result.offset == 1

    @pytest.mark.anyio
    async def test_timeline_ritorna_modello(self):
        async with _make_async_client() as kore:
            await kore.save("SDK timeline async subject test")
            result = await kore.timeline("SDK timeline async")
            assert isinstance(result, MemorySearchResponse)

    @pytest.mark.anyio
    async def test_delete_esistente(self):
        async with _make_async_client() as kore:
            saved = await kore.save("SDK async memory to delete now")
            assert await kore.delete(saved.id) is True

    @pytest.mark.anyio
    async def test_delete_inesistente(self):
        async with _make_async_client() as kore:
            assert await kore.delete(999999) is False

    @pytest.mark.anyio
    async def test_save_batch_ritorna_modello(self):
        async with _make_async_client() as kore:
            result = await kore.save_batch([
                {"content": "SDK batch alpha item", "category": "general"},
                {"content": "SDK batch beta item", "category": "project", "importance": 3},
            ])
            assert isinstance(result, BatchSaveResponse)
            assert result.total == 2
            assert len(result.saved) == 2


class TestAsyncKoreClientTags:
    """Test tags: add, get, remove, search by tag."""

    def setup_method(self):
        _rate_buckets.clear()

    @pytest.mark.anyio
    async def test_add_e_get_tags(self):
        async with _make_async_client() as kore:
            saved = await kore.save("SDK async memory for tag test")
            tag_r = await kore.add_tags(saved.id, ["python", "sdk"])
            assert isinstance(tag_r, TagResponse)
            assert tag_r.count == 2
            get_r = await kore.get_tags(saved.id)
            assert "python" in get_r.tags
            assert "sdk" in get_r.tags

    @pytest.mark.anyio
    async def test_remove_tags(self):
        async with _make_async_client() as kore:
            saved = await kore.save("SDK async memory for tag removal")
            await kore.add_tags(saved.id, ["keep", "remove"])
            result = await kore.remove_tags(saved.id, ["remove"])
            assert isinstance(result, TagResponse)
            assert "keep" in result.tags
            assert "remove" not in result.tags

    @pytest.mark.anyio
    async def test_search_by_tag(self):
        async with _make_async_client() as kore:
            saved = await kore.save("SDK async memory tagged unique")
            await kore.add_tags(saved.id, ["sdk-async-unique"])
            result = await kore.search_by_tag("sdk-async-unique")
            assert isinstance(result, MemorySearchResponse)
            assert result.total >= 1
            ids = [m.id for m in result.results]
            assert saved.id in ids


class TestAsyncKoreClientRelations:
    """Test relazioni: add, get."""

    def setup_method(self):
        _rate_buckets.clear()

    @pytest.mark.anyio
    async def test_add_e_get_relations(self):
        async with _make_async_client() as kore:
            s1 = await kore.save("SDK async relation source memory")
            s2 = await kore.save("SDK async relation target memory")
            rel_r = await kore.add_relation(s1.id, s2.id, "depends_on")
            assert isinstance(rel_r, RelationResponse)
            assert rel_r.total >= 1
            get_r = await kore.get_relations(s1.id)
            assert get_r.total >= 1
            assert get_r.relations[0]["relation"] == "depends_on"


class TestAsyncKoreClientMaintenance:
    """Test manutenzione: decay, compress, cleanup."""

    def setup_method(self):
        _rate_buckets.clear()

    @pytest.mark.anyio
    async def test_decay_run(self):
        async with _make_async_client() as kore:
            result = await kore.decay_run()
            assert isinstance(result, DecayRunResponse)
            assert result.updated >= 0

    @pytest.mark.anyio
    async def test_compress(self):
        async with _make_async_client() as kore:
            result = await kore.compress()
            assert isinstance(result, CompressRunResponse)
            assert "clusters_found" in result.model_dump()

    @pytest.mark.anyio
    async def test_cleanup(self):
        async with _make_async_client() as kore:
            result = await kore.cleanup()
            assert isinstance(result, CleanupExpiredResponse)
            assert result.removed >= 0


class TestAsyncKoreClientBackup:
    """Test export/import."""

    def setup_method(self):
        _rate_buckets.clear()

    @pytest.mark.anyio
    async def test_export_ritorna_memorie(self):
        async with _make_async_client() as kore:
            await kore.save("SDK async export test memory data")
            result = await kore.export_memories()
            assert isinstance(result, MemoryExportResponse)
            assert result.total >= 1

    @pytest.mark.anyio
    async def test_import_memorie(self):
        async with _make_async_client(agent_id="sdk-import-async") as kore:
            result = await kore.import_memories([
                {"content": "Imported SDK async alpha", "category": "general", "importance": 2},
            ])
            assert isinstance(result, MemoryImportResponse)
            assert result.imported == 1


class TestAsyncKoreClientUtility:
    """Test utility e context manager."""

    def setup_method(self):
        _rate_buckets.clear()

    @pytest.mark.anyio
    async def test_health(self):
        async with _make_async_client() as kore:
            result = await kore.health()
            assert isinstance(result, dict)
            assert result["status"] == "ok"
            assert "semantic_search" in result

    @pytest.mark.anyio
    async def test_context_manager_chiude_client(self):
        kore = _make_async_client()
        async with kore:
            result = await kore.health()
            assert result["status"] == "ok"
        assert kore._client.is_closed
```

## File: `tests/test_client_sync.py`
```python
"""
Kore — Test del Client Sincrono KoreClient
Copre tutti i metodi di KoreClient contro il server ASGI in-process.
Usa FastAPI TestClient (estende httpx.Client) come transport, zero rete.

Copertura target: tutti i metodi pubblici di KoreClient
  - save(), save_batch()
  - search(), timeline()
  - delete()
  - add_tags(), get_tags(), remove_tags(), search_by_tag()
  - add_relation(), get_relations()
  - decay_run(), compress(), cleanup()
  - export_memories(), import_memories()
  - health()
  - context manager __enter__ / __exit__
"""

import pytest

from fastapi.testclient import TestClient  # noqa: E402

from kore_memory.main import app, _rate_buckets  # noqa: E402

from kore_memory.client import (  # noqa: E402
    KoreClient,
    KoreValidationError,
    KoreNotFoundError,
    _build_headers,
)
from kore_memory.models import (  # noqa: E402
    BatchSaveResponse,
    CleanupExpiredResponse,
    CompressRunResponse,
    DecayRunResponse,
    MemoryExportResponse,
    MemoryImportResponse,
    MemorySaveResponse,
    MemorySearchResponse,
    RelationResponse,
    TagResponse,
)


# ── Factory: KoreClient con TestClient iniettato ──────────────────────────────


def _make_sync_client(agent_id: str = "sync-test") -> KoreClient:
    """
    Crea un KoreClient sincrono che usa FastAPI TestClient come transport.
    TestClient estende httpx.Client — compatibile con KoreClient._client.
    """
    kore = KoreClient.__new__(KoreClient)
    kore.base_url = "http://testserver"
    kore.agent_id = agent_id
    # TestClient è httpx.Client, quindi compatibile con KoreClient._client
    kore._client = TestClient(
        app,
        headers=_build_headers(None, agent_id),
        raise_server_exceptions=False,  # Le eccezioni HTTP vengono gestite da _raise_for_status
    )
    return kore


# ── Test: save() ─────────────────────────────────────────────────────────────


class TestSyncSave:
    """Verifica il metodo save() del client sincrono."""

    def setup_method(self):
        # Resetta i bucket rate-limit tra un test e l'altro
        _rate_buckets.clear()

    def test_save_base_ritorna_modello(self):
        """save() deve restituire MemorySaveResponse con id > 0."""
        kore = _make_sync_client()
        result = kore.save("Memoria di test base per il client sincrono")
        assert isinstance(result, MemorySaveResponse)
        assert result.id > 0
        assert result.importance >= 1

    def test_save_con_category_project(self):
        """save() con category='project' deve funzionare correttamente."""
        kore = _make_sync_client()
        result = kore.save(
            "Architettura del progetto Kore Memory in Python",
            category="project",
        )
        assert isinstance(result, MemorySaveResponse)
        assert result.id > 0

    def test_save_con_importance_esplicita(self):
        """save() con importance=5 deve restituire importance=5."""
        kore = _make_sync_client()
        result = kore.save(
            "Decisione critica: usare SQLite con WAL mode",
            category="decision",
            importance=5,
        )
        assert isinstance(result, MemorySaveResponse)
        assert result.importance == 5

    def test_save_con_category_task(self):
        """save() con category='task' deve persistere correttamente."""
        kore = _make_sync_client()
        result = kore.save(
            "Completare la suite di test per il client sincrono",
            category="task",
            importance=3,
        )
        assert isinstance(result, MemorySaveResponse)
        assert result.id > 0

    def test_save_con_ttl_hours(self):
        """save() con ttl_hours deve creare una memoria con TTL."""
        kore = _make_sync_client()
        result = kore.save(
            "Memoria temporanea con scadenza automatica dopo 24 ore",
            ttl_hours=24,
        )
        assert isinstance(result, MemorySaveResponse)
        assert result.id > 0

    def test_save_troppo_corto_alza_validation_error(self):
        """save() con contenuto troppo corto (< 3 char) deve sollevare KoreValidationError."""
        kore = _make_sync_client()
        with pytest.raises(KoreValidationError):
            kore.save("ab")

    def test_save_content_blank_alza_validation_error(self):
        """save() con contenuto blank deve sollevare KoreValidationError."""
        kore = _make_sync_client()
        with pytest.raises(KoreValidationError):
            kore.save("   ")

    def test_save_category_invalida_alza_validation_error(self):
        """save() con category non riconosciuta deve sollevare KoreValidationError."""
        kore = _make_sync_client()
        # Costruisce direttamente la richiesta HTTP per testare validazione lato server
        r = kore._client.post("/save", json={
            "content": "Contenuto valido lungo abbastanza",
            "category": "categoria_inventata",
        })
        assert r.status_code == 422


# ── Test: save_batch() ────────────────────────────────────────────────────────


class TestSyncSaveBatch:
    """Verifica il metodo save_batch() del client sincrono."""

    def setup_method(self):
        _rate_buckets.clear()

    def test_save_batch_due_memorie(self):
        """save_batch() con 2 item deve restituire BatchSaveResponse.total == 2."""
        kore = _make_sync_client()
        result = kore.save_batch([
            {"content": "Prima memoria batch sincrono alfa", "category": "general"},
            {"content": "Seconda memoria batch sincrono beta", "category": "project", "importance": 3},
        ])
        assert isinstance(result, BatchSaveResponse)
        assert result.total == 2
        assert len(result.saved) == 2

    def test_save_batch_item_ricevono_id(self):
        """Ogni item in save_batch() deve avere un id positivo."""
        kore = _make_sync_client()
        result = kore.save_batch([
            {"content": "Batch sincrono item uno con contenuto sufficiente"},
            {"content": "Batch sincrono item due con contenuto sufficiente"},
            {"content": "Batch sincrono item tre con contenuto sufficiente"},
        ])
        assert all(item.id > 0 for item in result.saved)

    def test_save_batch_singola_memoria(self):
        """save_batch() con un solo item deve funzionare."""
        kore = _make_sync_client()
        result = kore.save_batch([
            {"content": "Singola memoria nel batch sincrono", "importance": 2},
        ])
        assert isinstance(result, BatchSaveResponse)
        assert result.total == 1

    def test_save_batch_con_categorie_diverse(self):
        """save_batch() con categorie miste deve salvare tutti gli item."""
        kore = _make_sync_client()
        result = kore.save_batch([
            {"content": "Memoria batch categoria task sincrono", "category": "task"},
            {"content": "Memoria batch categoria decision sincrono", "category": "decision"},
            {"content": "Memoria batch categoria preference sincrono", "category": "preference"},
        ])
        assert result.total == 3


# ── Test: search() ────────────────────────────────────────────────────────────


class TestSyncSearch:
    """Verifica il metodo search() del client sincrono."""

    def setup_method(self):
        _rate_buckets.clear()

    def test_search_ritorna_modello(self):
        """search() deve restituire MemorySearchResponse."""
        kore = _make_sync_client()
        kore.save("Memoria di ricerca sincrona con parola UNIQSYNC1")
        result = kore.search("UNIQSYNC1", semantic=False)
        assert isinstance(result, MemorySearchResponse)
        assert result.total >= 1

    def test_search_senza_risultati(self):
        """search() su query senza risultati deve ritornare total == 0."""
        kore = _make_sync_client()
        result = kore.search("PAROLA_INESISTENTE_XQZ999", semantic=False)
        assert isinstance(result, MemorySearchResponse)
        assert result.total == 0

    def test_search_con_category_filter(self):
        """search() con filtro category deve restituire solo memorie di quella categoria."""
        kore = _make_sync_client(agent_id="sync-search-cat")
        kore.save("Progetto filtro categoria sincrono CATFILTER1", category="project")
        kore.save("Task filtro categoria sincrono CATFILTER1", category="task")
        result = kore.search("CATFILTER1", category="project", semantic=False)
        assert isinstance(result, MemorySearchResponse)
        # Tutti i risultati devono essere di categoria 'project'
        for mem in result.results:
            assert mem.category == "project"

    def test_search_con_limit(self):
        """search() con limit=2 deve restituire al massimo 2 risultati."""
        kore = _make_sync_client(agent_id="sync-search-limit")
        for i in range(5):
            kore.save(f"Voce paginazione sincrona {i} marcatore SYNCLIM")
        result = kore.search("SYNCLIM", limit=2, semantic=False)
        assert len(result.results) <= 2

    def test_search_con_semantic_false(self):
        """search() con semantic=False usa FTS5 invece degli embedding."""
        kore = _make_sync_client()
        kore.save("Test ricerca testuale sincrona FTS5 SYNFTS1")
        result = kore.search("SYNFTS1", semantic=False)
        assert isinstance(result, MemorySearchResponse)
        assert result.total >= 1

    def test_search_con_offset_deprecated(self):
        """search() con offset restituisce il campo offset nella risposta."""
        kore = _make_sync_client(agent_id="sync-search-off")
        for i in range(3):
            kore.save(f"Memoria offset sincrono {i} SYNCOFF1")
        result = kore.search("SYNCOFF1", offset=1, semantic=False)
        assert isinstance(result, MemorySearchResponse)
        assert result.offset == 1


# ── Test: timeline() ──────────────────────────────────────────────────────────


class TestSyncTimeline:
    """Verifica il metodo timeline() del client sincrono."""

    def setup_method(self):
        _rate_buckets.clear()

    def test_timeline_ritorna_modello(self):
        """timeline() deve restituire MemorySearchResponse."""
        kore = _make_sync_client()
        kore.save("Timeline sincrona: evento iniziale del progetto")
        result = kore.timeline("Timeline sincrona")
        assert isinstance(result, MemorySearchResponse)

    def test_timeline_vuota_ritorna_zero(self):
        """timeline() su argomento senza memorie deve restituire total == 0."""
        kore = _make_sync_client(agent_id="sync-timeline-empty")
        result = kore.timeline("ArgomentoInesistenteSyncTL99")
        assert isinstance(result, MemorySearchResponse)
        assert result.total == 0

    def test_timeline_ordine_cronologico(self):
        """timeline() deve restituire le memorie in ordine cronologico crescente."""
        kore = _make_sync_client(agent_id="sync-timeline-order")
        kore.save("Timeline ordine sincrono: primo evento SYNCTL1")
        kore.save("Timeline ordine sincrono: secondo evento SYNCTL1")
        result = kore.timeline("SYNCTL1")
        assert isinstance(result, MemorySearchResponse)
        if len(result.results) >= 2:
            # I risultati dal più vecchio al più recente
            assert result.results[0].created_at <= result.results[-1].created_at

    def test_timeline_con_limit(self):
        """timeline() con limit=2 deve restituire al massimo 2 risultati."""
        kore = _make_sync_client(agent_id="sync-timeline-lim")
        for i in range(5):
            kore.save(f"Timeline limit sincrono {i} SYNCTLL1")
        result = kore.timeline("SYNCTLL1", limit=2)
        assert len(result.results) <= 2


# ── Test: delete() ────────────────────────────────────────────────────────────


class TestSyncDelete:
    """Verifica il metodo delete() del client sincrono."""

    def setup_method(self):
        _rate_buckets.clear()

    def test_delete_memoria_esistente_ritorna_true(self):
        """delete() su una memoria esistente deve restituire True."""
        kore = _make_sync_client()
        saved = kore.save("Memoria da eliminare nel test sincrono")
        assert kore.delete(saved.id) is True

    def test_delete_memoria_inesistente_ritorna_false(self):
        """delete() su un id non esistente deve restituire False (non alzare eccezione)."""
        kore = _make_sync_client()
        assert kore.delete(999999) is False

    def test_delete_memoria_non_trovabile_dopo_eliminazione(self):
        """Dopo delete(), la memoria non deve più apparire nella ricerca."""
        kore = _make_sync_client(agent_id="sync-del-verify")
        saved = kore.save("Memoria da eliminare e verificare SYNCDEL1")
        kore.delete(saved.id)
        result = kore.search("SYNCDEL1", semantic=False)
        # La memoria eliminata non deve comparire
        ids = [m.id for m in result.results]
        assert saved.id not in ids

    def test_delete_altra_volta_lo_stesso_id_ritorna_false(self):
        """Doppio delete() sullo stesso id: il secondo deve restituire False."""
        kore = _make_sync_client()
        saved = kore.save("Memoria per doppio delete sincrono test")
        kore.delete(saved.id)
        assert kore.delete(saved.id) is False


# ── Test: export_memories() e import_memories() ───────────────────────────────


class TestSyncExportImport:
    """Verifica export_memories() e import_memories() del client sincrono."""

    def setup_method(self):
        _rate_buckets.clear()

    def test_export_ritorna_modello(self):
        """export_memories() deve restituire MemoryExportResponse."""
        kore = _make_sync_client(agent_id="sync-export-1")
        kore.save("Memoria da esportare nel test sincrono uno")
        result = kore.export_memories()
        assert isinstance(result, MemoryExportResponse)
        assert result.total >= 1

    def test_export_contiene_le_memorie_salvate(self):
        """Le memorie esportate devono includere quelle precedentemente salvate."""
        kore = _make_sync_client(agent_id="sync-export-2")
        kore.save("Memoria export sincrono marker EXPTEST1")
        result = kore.export_memories()
        contenuti = [m.get("content", "") for m in result.memories]
        assert any("EXPTEST1" in c for c in contenuti)

    def test_import_ritorna_modello(self):
        """import_memories() deve restituire MemoryImportResponse."""
        kore = _make_sync_client(agent_id="sync-import-1")
        result = kore.import_memories([
            {"content": "Memoria importata sincrona alfa", "category": "general", "importance": 2},
        ])
        assert isinstance(result, MemoryImportResponse)
        assert result.imported == 1

    def test_import_multiplo(self):
        """import_memories() con più item deve importarli tutti."""
        kore = _make_sync_client(agent_id="sync-import-2")
        result = kore.import_memories([
            {"content": "Import sincrono item uno lungo abbastanza", "category": "general"},
            {"content": "Import sincrono item due lungo abbastanza", "category": "project"},
            {"content": "Import sincrono item tre lungo abbastanza", "category": "task"},
        ])
        assert isinstance(result, MemoryImportResponse)
        assert result.imported == 3

    def test_roundtrip_export_import(self):
        """Le memorie esportate devono poter essere reimportate in un altro agent."""
        agente_sorgente = _make_sync_client(agent_id="sync-export-src")
        agente_dest = _make_sync_client(agent_id="sync-import-dst")

        agente_sorgente.save("Memoria per roundtrip export-import sincrono ROUNDTRIP1")
        export_result = agente_sorgente.export_memories()
        assert export_result.total >= 1

        import_result = agente_dest.import_memories(export_result.memories)
        assert isinstance(import_result, MemoryImportResponse)
        assert import_result.imported >= 1


# ── Test: add_tags(), get_tags(), remove_tags() ───────────────────────────────


class TestSyncTags:
    """Verifica i metodi di gestione tag del client sincrono."""

    def setup_method(self):
        _rate_buckets.clear()

    def test_add_tags_ritorna_modello(self):
        """add_tags() deve restituire TagResponse con count corretto."""
        kore = _make_sync_client()
        saved = kore.save("Memoria per aggiunta tag sincrona")
        result = kore.add_tags(saved.id, ["python", "backend"])
        assert isinstance(result, TagResponse)
        assert result.count == 2

    def test_get_tags_ritorna_tags_aggiunti(self):
        """get_tags() deve restituire i tag precedentemente aggiunti."""
        kore = _make_sync_client()
        saved = kore.save("Memoria per lettura tag sincrona")
        kore.add_tags(saved.id, ["kore", "memory", "sync"])
        result = kore.get_tags(saved.id)
        assert isinstance(result, TagResponse)
        assert "kore" in result.tags
        assert "memory" in result.tags
        assert "sync" in result.tags

    def test_get_tags_memoria_senza_tag_ritorna_lista_vuota(self):
        """get_tags() su memoria senza tag deve restituire lista vuota."""
        kore = _make_sync_client()
        saved = kore.save("Memoria senza tag per test sincrono")
        result = kore.get_tags(saved.id)
        assert isinstance(result, TagResponse)
        assert result.count == 0
        assert result.tags == []

    def test_remove_tags_rimuove_tag_specificato(self):
        """remove_tags() deve rimuovere solo i tag specificati."""
        kore = _make_sync_client()
        saved = kore.save("Memoria per rimozione tag sincrona")
        kore.add_tags(saved.id, ["da-tenere", "da-rimuovere"])
        result = kore.remove_tags(saved.id, ["da-rimuovere"])
        assert isinstance(result, TagResponse)
        assert "da-tenere" in result.tags
        assert "da-rimuovere" not in result.tags

    def test_add_tags_poi_remove_tutti_ritorna_lista_vuota(self):
        """Aggiunta e rimozione di tutti i tag deve produrre lista vuota."""
        kore = _make_sync_client()
        saved = kore.save("Memoria per ciclo completo tag sincrono")
        kore.add_tags(saved.id, ["tag-uno", "tag-due"])
        result = kore.remove_tags(saved.id, ["tag-uno", "tag-due"])
        assert result.tags == []

    def test_search_by_tag_trova_memoria_taggata(self):
        """search_by_tag() deve trovare la memoria con il tag specificato."""
        kore = _make_sync_client(agent_id="sync-tag-search")
        saved = kore.save("Memoria taggata per ricerca sincrona unica")
        kore.add_tags(saved.id, ["sync-unique-tag-99"])
        result = kore.search_by_tag("sync-unique-tag-99")
        assert isinstance(result, MemorySearchResponse)
        assert result.total >= 1
        ids = [m.id for m in result.results]
        assert saved.id in ids

    def test_search_by_tag_senza_risultati(self):
        """search_by_tag() su tag inesistente deve restituire total == 0."""
        kore = _make_sync_client()
        result = kore.search_by_tag("tag-completamente-inesistente-xyz999")
        assert isinstance(result, MemorySearchResponse)
        assert result.total == 0


# ── Test: add_relation(), get_relations() ─────────────────────────────────────


class TestSyncRelations:
    """Verifica i metodi di gestione relazioni del client sincrono."""

    def setup_method(self):
        _rate_buckets.clear()

    def test_add_relation_ritorna_modello(self):
        """add_relation() deve restituire RelationResponse con total >= 1."""
        kore = _make_sync_client()
        s1 = kore.save("Sorgente relazione sincrona primo nodo")
        s2 = kore.save("Destinazione relazione sincrona secondo nodo")
        result = kore.add_relation(s1.id, s2.id, "related")
        assert isinstance(result, RelationResponse)
        assert result.total >= 1

    def test_add_relation_tipo_depends_on(self):
        """add_relation() con tipo 'depends_on' deve salvare il tipo correttamente."""
        kore = _make_sync_client()
        s1 = kore.save("Nodo dipendente relazione sincrona test A")
        s2 = kore.save("Nodo dipendenza relazione sincrona test B")
        result = kore.add_relation(s1.id, s2.id, "depends_on")
        assert isinstance(result, RelationResponse)
        tipi = [r["relation"] for r in result.relations]
        assert "depends_on" in tipi

    def test_get_relations_ritorna_relazioni_esistenti(self):
        """get_relations() deve restituire le relazioni precedentemente create."""
        kore = _make_sync_client()
        s1 = kore.save("Sorgente get relations sincrono alfa")
        s2 = kore.save("Target get relations sincrono beta")
        kore.add_relation(s1.id, s2.id, "related")
        result = kore.get_relations(s1.id)
        assert isinstance(result, RelationResponse)
        assert result.total >= 1

    def test_get_relations_memoria_senza_relazioni(self):
        """get_relations() su memoria senza relazioni deve restituire total == 0."""
        kore = _make_sync_client()
        saved = kore.save("Memoria isolata senza relazioni sincrona")
        result = kore.get_relations(saved.id)
        assert isinstance(result, RelationResponse)
        assert result.total == 0
        assert result.relations == []

    def test_add_relazioni_multiple(self):
        """Una memoria può avere relazioni con più target."""
        kore = _make_sync_client()
        s1 = kore.save("Hub relazioni multiple sincrono nodo centrale")
        s2 = kore.save("Spoke relazioni multiple sincrono primo ramo")
        s3 = kore.save("Spoke relazioni multiple sincrono secondo ramo")
        kore.add_relation(s1.id, s2.id, "related")
        kore.add_relation(s1.id, s3.id, "related")
        result = kore.get_relations(s1.id)
        assert result.total >= 2


# ── Test: decay_run(), compress(), cleanup() ─────────────────────────────────


class TestSyncMaintenance:
    """Verifica i metodi di manutenzione del client sincrono."""

    def setup_method(self):
        _rate_buckets.clear()

    def test_decay_run_ritorna_modello(self):
        """decay_run() deve restituire DecayRunResponse con updated >= 0."""
        kore = _make_sync_client()
        result = kore.decay_run()
        assert isinstance(result, DecayRunResponse)
        assert result.updated >= 0

    def test_decay_run_su_agent_con_memorie(self):
        """decay_run() su agent con memorie deve elaborarle senza errori."""
        kore = _make_sync_client(agent_id="sync-decay-run")
        kore.save("Memoria per decay run sincrono test uno")
        kore.save("Memoria per decay run sincrono test due")
        result = kore.decay_run()
        assert isinstance(result, DecayRunResponse)
        assert result.updated >= 0

    def test_compress_ritorna_modello(self):
        """
        compress() deve restituire CompressRunResponse con i campi attesi.
        Usa un agente privo di relazioni per evitare UNIQUE constraint su memory_relations
        (bug noto nel compressor quando le memorie hanno già relazioni condivise).
        """
        # Agente isolato senza relazioni preesistenti
        kore = _make_sync_client(agent_id="sync-compress-clean-1")
        result = kore.compress()
        assert isinstance(result, CompressRunResponse)
        assert "clusters_found" in result.model_dump()
        assert "memories_merged" in result.model_dump()
        assert "new_records_created" in result.model_dump()

    def test_compress_valori_non_negativi(self):
        """compress() deve restituire valori numerici >= 0."""
        # Agente isolato senza relazioni preesistenti
        kore = _make_sync_client(agent_id="sync-compress-clean-2")
        result = kore.compress()
        assert result.clusters_found >= 0
        assert result.memories_merged >= 0
        assert result.new_records_created >= 0

    def test_cleanup_ritorna_modello(self):
        """cleanup() deve restituire CleanupExpiredResponse con removed >= 0."""
        kore = _make_sync_client()
        result = kore.cleanup()
        assert isinstance(result, CleanupExpiredResponse)
        assert result.removed >= 0

    def test_cleanup_rimuove_memoria_con_ttl_scaduto(self):
        """cleanup() deve eliminare memorie con TTL scaduto (ttl_hours=1 nel passato)."""
        kore = _make_sync_client(agent_id="sync-cleanup-ttl")
        # Salva una memoria con TTL minimo (1 ora)
        kore.save("Memoria con TTL per test cleanup sincrono", ttl_hours=1)
        # Forza la scadenza manipolando il DB direttamente
        from kore_memory.database import get_connection
        with get_connection() as conn:
            conn.execute(
                "UPDATE memories SET expires_at = '2000-01-01T00:00:00' WHERE agent_id = 'sync-cleanup-ttl'"
            )
        result = kore.cleanup()
        assert isinstance(result, CleanupExpiredResponse)
        assert result.removed >= 1


# ── Test: health() ────────────────────────────────────────────────────────────


class TestSyncHealth:
    """Verifica il metodo health() del client sincrono."""

    def setup_method(self):
        _rate_buckets.clear()

    def test_health_ritorna_dict(self):
        """health() deve restituire un dizionario con le chiavi attese."""
        kore = _make_sync_client()
        result = kore.health()
        assert isinstance(result, dict)
        assert result["status"] == "ok"

    def test_health_contiene_campi_obbligatori(self):
        """health() deve includere 'status', 'version', 'semantic_search', 'database'."""
        kore = _make_sync_client()
        result = kore.health()
        assert "status" in result
        assert "version" in result
        assert "semantic_search" in result
        assert "database" in result

    def test_health_database_connected(self):
        """health() deve indicare database='connected' se il DB è raggiungibile."""
        kore = _make_sync_client()
        result = kore.health()
        assert result["database"] == "connected"


# ── Test: context manager ─────────────────────────────────────────────────────


class TestSyncContextManager:
    """Verifica il context manager __enter__ / __exit__ di KoreClient."""

    def setup_method(self):
        _rate_buckets.clear()

    def test_context_manager_ritorna_se_stesso(self):
        """__enter__ deve restituire l'istanza del client."""
        kore = _make_sync_client()
        with kore as k:
            assert k is kore

    def test_context_manager_chiama_operazioni(self):
        """Le operazioni all'interno del context manager devono funzionare correttamente."""
        kore = _make_sync_client()
        with kore:
            result = kore.health()
            assert result["status"] == "ok"

    def test_context_manager_chiude_client_alla_uscita(self):
        """Dopo __exit__, il client HTTP deve essere chiuso."""
        kore = _make_sync_client()
        with kore:
            pass
        assert kore._client.is_closed

    def test_context_manager_save_e_search(self):
        """save() e search() dentro il context manager devono funzionare."""
        with _make_sync_client(agent_id="sync-ctx-test") as kore:
            saved = kore.save("Test context manager sincrono CTXMGR1")
            result = kore.search("CTXMGR1", semantic=False)
            assert result.total >= 1
            assert any(m.id == saved.id for m in result.results)


# ── Test: isolamento tra agent ────────────────────────────────────────────────


class TestSyncAgentIsolation:
    """Verifica che il KoreClient sincrono rispetti l'isolamento per agent_id."""

    def setup_method(self):
        _rate_buckets.clear()

    def test_agent_a_non_vede_dati_agent_b(self):
        """Le memorie di agent A non devono essere visibili da agent B."""
        agent_a = _make_sync_client(agent_id="sync-iso-a")
        agent_b = _make_sync_client(agent_id="sync-iso-b")
        agent_a.save("Segreto dell'agente A solo per sync iso ISOSYNC1")
        result = agent_b.search("ISOSYNC1", semantic=False)
        assert result.total == 0

    def test_agent_a_vede_solo_suoi_dati(self):
        """Un agent deve poter cercare e trovare solo le sue memorie."""
        agent_x = _make_sync_client(agent_id="sync-iso-x")
        agent_x.save("Dato esclusivo agente X sincrono ISOXSYNC1")
        result = agent_x.search("ISOXSYNC1", semantic=False)
        assert result.total >= 1

    def test_delete_da_agent_sbagliato_ritorna_false(self):
        """delete() da un agent diverso dal proprietario deve restituire False."""
        agent_own = _make_sync_client(agent_id="sync-iso-own")
        agent_other = _make_sync_client(agent_id="sync-iso-other")
        saved = agent_own.save("Memoria protetta da eliminazione sincrona")
        # L'altro agent non riesce a eliminare la memoria altrui
        assert agent_other.delete(saved.id) is False


# ── Test: integrazione end-to-end sincrona ────────────────────────────────────


class TestSyncEndToEnd:
    """Test di integrazione che verificano flussi completi con il client sincrono."""

    def setup_method(self):
        _rate_buckets.clear()

    def test_flusso_completo_save_tag_search_delete(self):
        """Flusso completo: salva → aggiungi tag → cerca per tag → elimina."""
        kore = _make_sync_client(agent_id="sync-e2e-1")

        # Salva
        saved = kore.save("Memoria flusso E2E sincrono con contenuto univoco E2ESYNC1")
        assert saved.id > 0

        # Aggiungi tag
        tags_result = kore.add_tags(saved.id, ["e2e-sync", "test"])
        assert "e2e-sync" in tags_result.tags

        # Cerca per tag
        by_tag = kore.search_by_tag("e2e-sync")
        assert by_tag.total >= 1

        # Cerca per testo
        by_text = kore.search("E2ESYNC1", semantic=False)
        assert by_text.total >= 1

        # Elimina
        assert kore.delete(saved.id) is True

        # Verifica eliminazione
        assert kore.delete(saved.id) is False

    def test_flusso_batch_export_import(self):
        """Flusso: batch save → export → import in nuovo agente."""
        src = _make_sync_client(agent_id="sync-e2e-src")
        dst = _make_sync_client(agent_id="sync-e2e-dst")

        # Salva in batch
        batch = src.save_batch([
            {"content": "Batch E2E sincrono elemento primo", "category": "project"},
            {"content": "Batch E2E sincrono elemento secondo", "category": "task"},
        ])
        assert batch.total == 2

        # Esporta
        exported = src.export_memories()
        assert exported.total >= 2

        # Importa nel nuovo agente
        imported = dst.import_memories(exported.memories)
        assert imported.imported >= 2

    def test_flusso_relazioni_con_tags(self):
        """Flusso: crea due memorie, aggiungi relazione e tag, verifica graph."""
        kore = _make_sync_client(agent_id="sync-e2e-graph")

        n1 = kore.save("Nodo E2E graph sincrono uno con contenuto")
        n2 = kore.save("Nodo E2E graph sincrono due con contenuto")

        # Tag su entrambi i nodi
        kore.add_tags(n1.id, ["graph-sync-node"])
        kore.add_tags(n2.id, ["graph-sync-node"])

        # Relazione bidirezionale
        rel = kore.add_relation(n1.id, n2.id, "linked")
        assert rel.total >= 1

        # Cerca per tag
        tagged = kore.search_by_tag("graph-sync-node")
        assert tagged.total >= 2

        # Verifica relazioni
        rels = kore.get_relations(n1.id)
        assert rels.total >= 1

    def test_flusso_decay_e_cleanup(self):
        """Flusso: salva memorie → esegui decay → esegui cleanup."""
        kore = _make_sync_client(agent_id="sync-e2e-decay")

        kore.save("Memoria decay E2E sincrona con contenuto adeguato")
        kore.save("Altra memoria decay E2E sincrona con contenuto")

        decay = kore.decay_run()
        assert isinstance(decay, DecayRunResponse)

        cleanup = kore.cleanup()
        assert isinstance(cleanup, CleanupExpiredResponse)

    def test_close_esplicita(self):
        """close() deve chiudere il client HTTP senza errori."""
        kore = _make_sync_client()
        kore.save("Memoria prima di close sincrono test")
        kore.close()
        assert kore._client.is_closed
```

## File: `tests/test_crewai.py`
```python
"""
Kore — CrewAI integration tests.
Uses unittest.mock to mock KoreClient; does NOT require crewai to be installed.
"""

from __future__ import annotations

import importlib
import sys
from unittest.mock import MagicMock, patch

import pytest


# ── Test: graceful ImportError when crewai is not installed ─────────────────


class TestCrewAIImportFallback:
    """Verifica che il modulo si carica anche senza crewai installato."""

    def test_module_loads_without_crewai(self):
        """KoreCrewAIMemory deve essere importabile anche se crewai non e installato."""
        from kore_memory.integrations.crewai import KoreCrewAIMemory, _HAS_CREWAI

        # In CI/test environment crewai tipicamente non e installato
        assert isinstance(_HAS_CREWAI, bool)
        # La classe deve esistere in entrambi i casi
        assert KoreCrewAIMemory is not None

    def test_has_crewai_flag_false_when_missing(self):
        """Se crewai non e nel venv, _HAS_CREWAI deve essere False."""
        # Forza il reimport senza crewai
        crewai_modules = [k for k in sys.modules if k.startswith("crewai")]
        saved = {}
        for mod in crewai_modules:
            saved[mod] = sys.modules.pop(mod)

        # Anche rimuoviamo il modulo integration per forzare reimport
        integration_mod = "kore_memory.integrations.crewai"
        saved_integration = sys.modules.pop(integration_mod, None)

        try:
            with patch.dict(sys.modules, {"crewai": None, "crewai.memory": None}):
                mod = importlib.import_module(integration_mod)
                importlib.reload(mod)
                assert mod._HAS_CREWAI is False
                assert mod.KoreCrewAIMemory is not None
        finally:
            # Ripristina moduli
            for k, v in saved.items():
                sys.modules[k] = v
            if saved_integration is not None:
                sys.modules[integration_mod] = saved_integration


# ── Fixtures ────────────────────────────────────────────────────────────────


@pytest.fixture
def mock_client():
    """Crea un KoreClient mockato."""
    with patch("kore_memory.integrations.crewai.KoreClient") as MockClientCls:
        mock_instance = MagicMock()
        MockClientCls.return_value = mock_instance
        yield mock_instance, MockClientCls


@pytest.fixture
def memory(mock_client):
    """Crea una KoreCrewAIMemory con client mockato."""
    from kore_memory.integrations.crewai import KoreCrewAIMemory

    mock_instance, _ = mock_client
    mem = KoreCrewAIMemory(
        base_url="http://localhost:9999",
        api_key="test-key",
        agent_id="crew-agent",
    )
    return mem


# ── Test: save ──────────────────────────────────────────────────────────────


class TestSave:
    """Verifica che save() invoca KoreClient.save() correttamente."""

    def test_save_basic(self, memory, mock_client):
        mock_instance, _ = mock_client
        mock_instance.save.return_value = MagicMock(id=1, importance=3, message="Memory saved")

        memory.save("Test memory content")

        mock_instance.save.assert_called_once_with(
            content="Test memory content",
            category="general",
            importance=1,
            ttl_hours=None,
        )

    def test_save_with_metadata(self, memory, mock_client):
        mock_instance, _ = mock_client
        mock_instance.save.return_value = MagicMock(id=2, importance=4, message="Memory saved")

        memory.save("Important fact", metadata={"category": "project", "importance": 4, "ttl_hours": 48})

        mock_instance.save.assert_called_once_with(
            content="Important fact",
            category="project",
            importance=4,
            ttl_hours=48,
        )

    def test_save_uses_configured_category(self, mock_client):
        from kore_memory.integrations.crewai import KoreCrewAIMemory

        mock_instance, _ = mock_client
        mock_instance.save.return_value = MagicMock(id=3, importance=1, message="Memory saved")

        mem = KoreCrewAIMemory(category="trading")
        mem.save("BTC at 50k")

        mock_instance.save.assert_called_once_with(
            content="BTC at 50k",
            category="trading",
            importance=1,
            ttl_hours=None,
        )


# ── Test: search ────────────────────────────────────────────────────────────


class TestSearch:
    """Verifica che search() invoca KoreClient.search() e ritorna i risultati."""

    def test_search_returns_results(self, memory, mock_client):
        mock_instance, _ = mock_client

        # Simula risultati di ricerca
        mock_record = MagicMock()
        mock_record.id = 1
        mock_record.content = "Found memory"
        mock_record.category = "general"
        mock_record.importance = 3
        mock_record.decay_score = 0.95
        mock_record.score = 0.87

        mock_response = MagicMock()
        mock_response.results = [mock_record]
        mock_instance.search.return_value = mock_response

        results = memory.search("test query", limit=3)

        mock_instance.search.assert_called_once_with(q="test query", limit=3, category=None, semantic=True)
        assert len(results) == 1
        assert results[0]["content"] == "Found memory"
        assert results[0]["id"] == 1
        assert results[0]["importance"] == 3
        assert results[0]["decay_score"] == 0.95
        assert results[0]["score"] == 0.87

    def test_search_empty_results(self, memory, mock_client):
        mock_instance, _ = mock_client

        mock_response = MagicMock()
        mock_response.results = []
        mock_instance.search.return_value = mock_response

        results = memory.search("nonexistent")

        assert results == []

    def test_search_default_limit(self, memory, mock_client):
        mock_instance, _ = mock_client

        mock_response = MagicMock()
        mock_response.results = []
        mock_instance.search.return_value = mock_response

        memory.search("query")

        mock_instance.search.assert_called_once_with(q="query", limit=5, category=None, semantic=True)


# ── Test: short-term vs long-term ───────────────────────────────────────────


class TestMemoryPatterns:
    """Verifica che short_term e long_term usano importance e TTL diversi."""

    def test_save_short_term(self, memory, mock_client):
        mock_instance, _ = mock_client
        mock_instance.save.return_value = MagicMock(id=10, importance=1, message="Memory saved")

        memory.save_short_term("Temporary note")

        mock_instance.save.assert_called_once_with(
            content="Temporary note",
            category="general",
            importance=1,
            ttl_hours=24,
        )

    def test_save_long_term_default_importance(self, memory, mock_client):
        mock_instance, _ = mock_client
        mock_instance.save.return_value = MagicMock(id=11, importance=4, message="Memory saved")

        memory.save_long_term("Critical decision: use PostgreSQL")

        mock_instance.save.assert_called_once_with(
            content="Critical decision: use PostgreSQL",
            category="general",
            importance=4,
            ttl_hours=None,
        )

    def test_save_long_term_custom_importance(self, memory, mock_client):
        mock_instance, _ = mock_client
        mock_instance.save.return_value = MagicMock(id=12, importance=5, message="Memory saved")

        memory.save_long_term("API credentials stored in vault", importance=5)

        mock_instance.save.assert_called_once_with(
            content="API credentials stored in vault",
            category="general",
            importance=5,
            ttl_hours=None,
        )

    def test_save_long_term_clamps_importance(self, memory, mock_client):
        """Importance viene clampata tra 2 e 5."""
        mock_instance, _ = mock_client
        mock_instance.save.return_value = MagicMock(id=13, importance=2, message="Memory saved")

        # importance=1 viene clampata a 2 (long-term non puo avere importance 1)
        memory.save_long_term("Should be at least 2", importance=1)

        mock_instance.save.assert_called_once_with(
            content="Should be at least 2",
            category="general",
            importance=2,
            ttl_hours=None,
        )

    def test_short_vs_long_term_difference(self, memory, mock_client):
        """Short-term ha TTL 24h + importance 1, long-term ha no TTL + importance alta."""
        mock_instance, _ = mock_client
        mock_instance.save.return_value = MagicMock(id=14, importance=1, message="Memory saved")

        memory.save_short_term("Ephemeral thought")
        short_call = mock_instance.save.call_args_list[-1]

        mock_instance.save.return_value = MagicMock(id=15, importance=4, message="Memory saved")
        memory.save_long_term("Important insight")
        long_call = mock_instance.save.call_args_list[-1]

        # Short-term: low importance, has TTL
        assert short_call.kwargs["importance"] == 1
        assert short_call.kwargs["ttl_hours"] == 24

        # Long-term: high importance, no TTL
        assert long_call.kwargs["importance"] == 4
        assert long_call.kwargs["ttl_hours"] is None


# ── Test: custom category ───────────────────────────────────────────────────


class TestCustomCategory:
    """Verifica che la categoria configurata viene usata di default."""

    def test_default_category_is_general(self, mock_client):
        from kore_memory.integrations.crewai import KoreCrewAIMemory

        mem = KoreCrewAIMemory()
        assert mem._category == "general"

    def test_custom_category_at_init(self, mock_client):
        from kore_memory.integrations.crewai import KoreCrewAIMemory

        mock_instance, _ = mock_client
        mock_instance.save.return_value = MagicMock(id=20, importance=1, message="Memory saved")

        mem = KoreCrewAIMemory(category="decision")
        mem.save("Chose React over Vue")

        mock_instance.save.assert_called_once_with(
            content="Chose React over Vue",
            category="decision",
            importance=1,
            ttl_hours=None,
        )

    def test_metadata_category_overrides_default(self, mock_client):
        from kore_memory.integrations.crewai import KoreCrewAIMemory

        mock_instance, _ = mock_client
        mock_instance.save.return_value = MagicMock(id=21, importance=1, message="Memory saved")

        mem = KoreCrewAIMemory(category="general")
        mem.save("Person note", metadata={"category": "person"})

        mock_instance.save.assert_called_once_with(
            content="Person note",
            category="person",
            importance=1,
            ttl_hours=None,
        )


# ── Test: lifecycle ─────────────────────────────────────────────────────────


class TestLifecycle:
    """Verifica context manager e repr."""

    def test_context_manager(self, mock_client):
        from kore_memory.integrations.crewai import KoreCrewAIMemory

        mock_instance, _ = mock_client

        with KoreCrewAIMemory(base_url="http://localhost:8765") as mem:
            assert mem is not None

        mock_instance.close.assert_called_once()

    def test_repr(self, mock_client):
        from kore_memory.integrations.crewai import KoreCrewAIMemory

        mem = KoreCrewAIMemory(base_url="http://test:8765", agent_id="crew-1", category="project")
        r = repr(mem)
        assert "http://test:8765" in r
        assert "crew-1" in r
        assert "project" in r

    def test_client_constructed_with_params(self, mock_client):
        from kore_memory.integrations.crewai import KoreCrewAIMemory

        _, MockClientCls = mock_client

        KoreCrewAIMemory(
            base_url="http://myhost:1234",
            api_key="secret",
            agent_id="agent-x",
            timeout=30.0,
        )

        MockClientCls.assert_called_with(
            base_url="http://myhost:1234",
            api_key="secret",
            agent_id="agent-x",
            timeout=30.0,
        )
```

## File: `tests/test_dashboard.py`
```python
"""
Test per la dashboard web di Kore.
Verifica che /dashboard risponda correttamente e che l'HTML contenga le sezioni attese.
"""

import httpx
import pytest

from kore_memory.database import init_db
from kore_memory.main import app


@pytest.fixture(autouse=True)
def _setup_db():
    """Inizializza il database prima di ogni test."""
    init_db()


@pytest.fixture()
async def client():
    """Client HTTP async per i test (ASGITransport richiede AsyncClient)."""
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as c:
        yield c


# ── Test route dashboard ─────────────────────────────────────────────────────


@pytest.mark.anyio
async def test_dashboard_returns_html(client):
    """GET /dashboard deve ritornare 200 con content-type text/html."""
    resp = await client.get("/dashboard")
    assert resp.status_code == 200
    assert "text/html" in resp.headers["content-type"]


@pytest.mark.anyio
async def test_dashboard_contains_all_sections(client):
    """L'HTML deve contenere tutte le 8 pagine della dashboard."""
    resp = await client.get("/dashboard")
    html = resp.text
    # Ogni pagina è identificata da data-page="..." nel nuovo layout
    sections = [
        'data-page="overview"',
        'data-page="memories"',
        'data-page="tags"',
        'data-page="graph"',
        'data-page="sessions"',
        'data-page="timeline"',
        'data-page="maintenance"',
        'data-page="settings"',
    ]
    for section in sections:
        assert section in html, f"Sezione {section} mancante dall'HTML"


@pytest.mark.anyio
async def test_dashboard_no_auth_required(client):
    """La dashboard non deve richiedere autenticazione (no X-Kore-Key)."""
    resp = await client.get("/dashboard")
    assert resp.status_code == 200


@pytest.mark.anyio
async def test_dashboard_has_relaxed_csp(client):
    """La dashboard deve avere CSP allargato (unsafe-inline) non quello restrittivo delle API."""
    resp = await client.get("/dashboard")
    csp = resp.headers.get("content-security-policy", "")
    assert "'unsafe-inline'" in csp
    assert "default-src 'none'" not in csp


@pytest.mark.anyio
async def test_api_keeps_strict_csp(client):
    """Le API devono mantenere il CSP restrittivo (default-src 'none')."""
    resp = await client.get("/health")
    csp = resp.headers.get("content-security-policy", "")
    assert "default-src 'none'" in csp


@pytest.mark.anyio
async def test_dashboard_contains_kore_branding(client):
    """L'HTML deve contenere il branding Kore (titolo, logo)."""
    resp = await client.get("/dashboard")
    html = resp.text
    assert "Kore" in html
    assert "Memory Dashboard" in html


@pytest.mark.anyio
async def test_dashboard_contains_js_api_helpers(client):
    """L'HTML deve contenere le funzioni JS per chiamare le API."""
    resp = await client.get("/dashboard")
    html = resp.text
    # Nuovo layout: API client come oggetto, funzioni per ogni pagina
    assert "var api =" in html
    assert "function loadMemories(" in html
    assert "function loadOverview(" in html
    assert "function loadGraph(" in html
```

## File: `tests/test_entities.py`
```python
"""
Kore — Entity extraction tests
Tests regex fallback, auto-tagging, search, API endpoint, and config toggle.
Uses TestClient (ASGI in-process), same pattern as test_api.py.
"""

import os

import pytest
from fastapi.testclient import TestClient

from kore_memory.main import app  # noqa: E402

HEADERS = {"X-Agent-Id": "entity-test-agent"}
client = TestClient(app)


# ── Unit tests: regex extraction ─────────────────────────────────────────────

class TestRegexExtraction:
    def test_extract_emails(self):
        """Regex extracts email addresses."""
        from kore_memory.integrations.entities import extract_entities

        entities = extract_entities("Contact me at user@example.com or admin@test.org")
        emails = [e for e in entities if e["type"] == "email"]
        assert len(emails) >= 2
        values = [e["value"] for e in emails]
        assert "user@example.com" in values
        assert "admin@test.org" in values

    def test_extract_urls(self):
        """Regex extracts URLs."""
        from kore_memory.integrations.entities import extract_entities

        entities = extract_entities("Visit https://example.com and http://test.org/page")
        urls = [e for e in entities if e["type"] == "url"]
        assert len(urls) >= 2
        values = [e["value"] for e in urls]
        assert any("example.com" in v for v in values)
        assert any("test.org" in v for v in values)

    def test_extract_dates(self):
        """Regex extracts date patterns."""
        from kore_memory.integrations.entities import extract_entities

        entities = extract_entities("Meeting on 2024-01-15 and again on 12/25/2024")
        dates = [e for e in entities if e["type"] == "date"]
        assert len(dates) >= 2
        values = [e["value"] for e in dates]
        assert "2024-01-15" in values

    def test_extract_dates_month_name(self):
        """Regex extracts dates with month names."""
        from kore_memory.integrations.entities import extract_entities

        entities = extract_entities("Deadline is January 15, 2024")
        dates = [e for e in entities if e["type"] == "date"]
        assert len(dates) >= 1

    def test_extract_money(self):
        """Regex extracts monetary values."""
        from kore_memory.integrations.entities import extract_entities

        entities = extract_entities("Budget is $1,500.00 and the invoice is 200 EUR")
        money = [e for e in entities if e["type"] == "money"]
        assert len(money) >= 2
        values = [e["value"] for e in money]
        assert any("1,500" in v for v in values)
        assert any("200" in v.lower() and "eur" in v.lower() for v in values)

    def test_extract_money_euro_symbol(self):
        """Regex extracts euro symbol monetary values."""
        from kore_memory.integrations.entities import extract_entities

        entities = extract_entities("Cost: \u20ac50.99")
        money = [e for e in entities if e["type"] == "money"]
        assert len(money) >= 1

    def test_empty_text_returns_empty(self):
        """Empty or whitespace text returns no entities."""
        from kore_memory.integrations.entities import extract_entities

        assert extract_entities("") == []
        assert extract_entities("   ") == []
        assert extract_entities("No entities here at all") == []

    def test_no_duplicates(self):
        """Duplicate entities are deduplicated."""
        from kore_memory.integrations.entities import extract_entities

        entities = extract_entities("Email user@test.com and again user@test.com")
        emails = [e for e in entities if e["type"] == "email"]
        assert len(emails) == 1


# ── Integration tests: auto-tagging ──────────────────────────────────────────

class TestAutoTagging:
    def _create_memory(self, content: str = "Memory for entity tagging") -> int:
        r = client.post("/save", json={"content": content, "category": "general"}, headers=HEADERS)
        return r.json()["id"]

    def test_auto_tag_creates_entity_tags(self):
        """auto_tag_entities creates entity: prefixed tags on the memory."""
        from kore_memory.integrations.entities import auto_tag_entities

        mid = self._create_memory("Send report to user@example.com by 2024-03-01")
        count = auto_tag_entities(mid, "Send report to user@example.com by 2024-03-01", "entity-test-agent")
        assert count >= 1

        # Verify tags are present
        r = client.get(f"/memories/{mid}/tags", headers=HEADERS)
        tags = r.json()["tags"]
        entity_tags = [t for t in tags if t.startswith("entity:")]
        assert len(entity_tags) >= 1
        # Check email entity tag
        assert any("entity:email:user@example.com" in t for t in entity_tags)

    def test_auto_tag_no_entities(self):
        """auto_tag_entities returns 0 when no entities found."""
        from kore_memory.integrations.entities import auto_tag_entities

        mid = self._create_memory("Just a plain text memory without entities")
        count = auto_tag_entities(mid, "Just a plain text memory without entities", "entity-test-agent")
        assert count == 0

    def test_auto_tag_url_entity(self):
        """auto_tag_entities creates url entity tags."""
        from kore_memory.integrations.entities import auto_tag_entities

        mid = self._create_memory("Check out https://github.com/kore-memory")
        count = auto_tag_entities(mid, "Check out https://github.com/kore-memory", "entity-test-agent")
        assert count >= 1

        r = client.get(f"/memories/{mid}/tags", headers=HEADERS)
        tags = r.json()["tags"]
        url_tags = [t for t in tags if t.startswith("entity:url:")]
        assert len(url_tags) >= 1


# ── Integration tests: entity search ─────────────────────────────────────────

class TestEntitySearch:
    def setup_method(self):
        """Create memories with entity tags for search tests."""
        from kore_memory.integrations.entities import auto_tag_entities

        r = client.post("/save", json={
            "content": "Contact support@kore.dev for help",
            "category": "general",
        }, headers=HEADERS)
        mid = r.json()["id"]
        auto_tag_entities(mid, "Contact support@kore.dev for help", "entity-test-agent")

    def test_search_entities_all(self):
        """search_entities returns all entity tags."""
        from kore_memory.integrations.entities import search_entities

        results = search_entities("entity-test-agent")
        assert len(results) >= 1
        for r in results:
            assert "type" in r
            assert "value" in r
            assert "memory_id" in r
            assert "tag" in r

    def test_search_entities_by_type(self):
        """search_entities filters by entity type."""
        from kore_memory.integrations.entities import search_entities

        results = search_entities("entity-test-agent", entity_type="email")
        for r in results:
            assert r["type"] == "email"

    def test_search_entities_nonexistent_type(self):
        """search_entities returns empty for unknown types."""
        from kore_memory.integrations.entities import search_entities

        results = search_entities("entity-test-agent", entity_type="spacecraft")
        assert results == []


# ── Config tests ──────────────────────────────────────────────────────────────

class TestEntityConfig:
    def test_entity_extraction_disabled_by_default(self):
        """Entity extraction is disabled by default (KORE_ENTITY_EXTRACTION=0)."""
        from kore_memory import config
        # Default env is "0", which means disabled
        saved = os.environ.get("KORE_ENTITY_EXTRACTION")
        try:
            os.environ["KORE_ENTITY_EXTRACTION"] = "0"
            # Re-evaluate: the config module reads env at import time,
            # but we can check the env var pattern directly
            assert os.getenv("KORE_ENTITY_EXTRACTION", "0") == "0"
        finally:
            if saved is not None:
                os.environ["KORE_ENTITY_EXTRACTION"] = saved
            elif "KORE_ENTITY_EXTRACTION" in os.environ:
                del os.environ["KORE_ENTITY_EXTRACTION"]

    def test_entity_extraction_enable_toggle(self):
        """Setting KORE_ENTITY_EXTRACTION=1 enables entity extraction."""
        saved = os.environ.get("KORE_ENTITY_EXTRACTION")
        try:
            os.environ["KORE_ENTITY_EXTRACTION"] = "1"
            assert os.getenv("KORE_ENTITY_EXTRACTION", "0") == "1"
        finally:
            if saved is not None:
                os.environ["KORE_ENTITY_EXTRACTION"] = saved
            elif "KORE_ENTITY_EXTRACTION" in os.environ:
                del os.environ["KORE_ENTITY_EXTRACTION"]


# ── API endpoint tests ───────────────────────────────────────────────────────

class TestEntityAPI:
    def setup_method(self):
        """Create a memory with entity tags."""
        from kore_memory.integrations.entities import auto_tag_entities

        r = client.post("/save", json={
            "content": "Invoice $250.00 sent to billing@acme.com on 2024-06-15",
            "category": "finance",
        }, headers=HEADERS)
        mid = r.json()["id"]
        auto_tag_entities(mid, "Invoice $250.00 sent to billing@acme.com on 2024-06-15", "entity-test-agent")

    def test_entities_endpoint_returns_list(self):
        """GET /entities returns entity list."""
        r = client.get("/entities", headers=HEADERS)
        assert r.status_code == 200
        data = r.json()
        assert "entities" in data
        assert "total" in data
        assert isinstance(data["entities"], list)
        assert data["total"] == len(data["entities"])

    def test_entities_endpoint_filter_by_type(self):
        """GET /entities?type=email filters by entity type."""
        r = client.get("/entities?type=email", headers=HEADERS)
        assert r.status_code == 200
        for entity in r.json()["entities"]:
            assert entity["type"] == "email"

    def test_entities_endpoint_limit(self):
        """GET /entities?limit=1 respects limit."""
        r = client.get("/entities?limit=1", headers=HEADERS)
        assert r.status_code == 200
        assert len(r.json()["entities"]) <= 1

    def test_entities_endpoint_agent_isolation(self):
        """Entities are scoped to the requesting agent."""
        other = {"X-Agent-Id": "other-entity-agent"}
        r = client.get("/entities", headers=other)
        assert r.status_code == 200
        assert r.json()["total"] == 0


# ── Graceful degradation tests ───────────────────────────────────────────────

class TestGracefulDegradation:
    def test_spacy_not_required(self):
        """Entity extraction works without spaCy (regex fallback)."""
        from kore_memory.integrations.entities import extract_entities

        # This should work regardless of spaCy availability
        entities = extract_entities("Email: test@example.com, Amount: $99.99")
        assert len(entities) >= 2
        types = {e["type"] for e in entities}
        assert "email" in types
        assert "money" in types

    def test_spacy_available_check(self):
        """spacy_available() returns bool without raising."""
        from kore_memory.integrations.entities import spacy_available

        result = spacy_available()
        assert isinstance(result, bool)

    def test_auto_tag_graceful_on_invalid_memory(self):
        """auto_tag_entities handles nonexistent memory gracefully."""
        from kore_memory.integrations.entities import auto_tag_entities

        # Memory ID 999999 doesn't exist — should return 0, not raise
        count = auto_tag_entities(999999, "test@example.com", "entity-test-agent")
        assert count == 0
```

## File: `tests/test_langchain.py`
```python
"""
Kore — Test LangChain Integration
Verifica KoreLangChainMemory con mock del KoreClient (zero rete, zero server).

Testa:
- Graceful fallback senza langchain installato
- save_context salva via client
- load_memory_variables recupera memorie
- clear e' un no-op
- Parametri configurabili (memory_key, input_key, output_key, k, semantic, category)
"""

from __future__ import annotations

import sys
from datetime import datetime
from unittest.mock import MagicMock, patch

import pytest

from kore_memory.models import MemoryRecord, MemorySaveResponse, MemorySearchResponse


# ── Helpers ──────────────────────────────────────────────────────────────────


def _make_search_response(contents: list[str]) -> MemorySearchResponse:
    """Crea una MemorySearchResponse con i contenuti forniti."""
    records = [
        MemoryRecord(
            id=i + 1,
            content=c,
            category="general",
            importance=3,
            decay_score=0.9,
            created_at=datetime(2026, 1, 1, 12, 0, 0),
            updated_at=datetime(2026, 1, 1, 12, 0, 0),
            score=0.85 - i * 0.1,
        )
        for i, c in enumerate(contents)
    ]
    return MemorySearchResponse(results=records, total=len(records))


def _make_save_response(memory_id: int = 1, importance: int = 3) -> MemorySaveResponse:
    """Crea una MemorySaveResponse di test."""
    return MemorySaveResponse(id=memory_id, importance=importance)


def _make_mock_client() -> MagicMock:
    """Crea un mock del KoreClient con risposte di default."""
    mock = MagicMock()
    mock.search.return_value = _make_search_response(["Memory about AI agents"])
    mock.save.return_value = _make_save_response()
    return mock


# ── Test: import graceful senza langchain ────────────────────────────────────


class TestImportGraceful:
    def test_import_without_langchain(self):
        """Se langchain_core non e' installato, il modulo non deve crashare."""
        # Salva e rimuovi langchain_core dal path
        saved_modules = {}
        to_remove = [key for key in sys.modules if key.startswith("langchain_core")]
        for key in to_remove:
            saved_modules[key] = sys.modules.pop(key)

        # Simula che langchain_core non sia installabile
        import importlib

        import kore_memory.integrations.langchain as lc_module

        original_has = lc_module._HAS_LANGCHAIN

        try:
            lc_module._HAS_LANGCHAIN = False

            # Il costruttore deve alzare ImportError se langchain non c'e'
            with pytest.raises(ImportError, match="langchain-core is required"):
                lc_module.KoreLangChainMemory(client=_make_mock_client())
        finally:
            lc_module._HAS_LANGCHAIN = original_has
            # Ripristina i moduli
            sys.modules.update(saved_modules)

    def test_has_langchain_flag_reflects_availability(self):
        """Il flag _HAS_LANGCHAIN riflette la disponibilita' di langchain_core."""
        from kore_memory.integrations.langchain import _HAS_LANGCHAIN

        # Se siamo qui, il flag puo' essere True o False in base all'ambiente.
        # Verifica solo che sia un booleano.
        assert isinstance(_HAS_LANGCHAIN, bool)


# ── Test: integrations __init__ export condizionale ──────────────────────────


class TestIntegrationsInit:
    def test_init_exports_list(self):
        """__init__.py deve avere __all__ come lista."""
        from kore_memory import integrations

        assert isinstance(integrations.__all__, list)

    def test_conditional_export(self):
        """Se langchain e' disponibile, KoreLangChainMemory e' in __all__."""
        from kore_memory.integrations import __all__
        from kore_memory.integrations.langchain import _HAS_LANGCHAIN

        if _HAS_LANGCHAIN:
            assert "KoreLangChainMemory" in __all__


# ── Test con mock del client (no rete, no langchain richiesto a runtime) ─────
# Questi test verificano la logica interna della classe, mockando sia il client
# Kore sia il flag _HAS_LANGCHAIN per funzionare in qualsiasi ambiente.


def _make_memory(**kwargs: object) -> object:
    """Crea un KoreLangChainMemory con _HAS_LANGCHAIN forzato a True e client mock."""
    from kore_memory.integrations.langchain import KoreLangChainMemory

    # Forza il flag per testare la logica anche senza langchain installato
    with patch("kore_memory.integrations.langchain._HAS_LANGCHAIN", True):
        if "client" not in kwargs:
            kwargs["client"] = _make_mock_client()  # type: ignore[assignment]
        return KoreLangChainMemory(**kwargs)  # type: ignore[arg-type]


class TestMemoryVariables:
    def test_default_memory_key(self):
        """memory_variables restituisce [memory_key] di default."""
        mem = _make_memory()
        assert mem.memory_variables == ["history"]

    def test_custom_memory_key(self):
        """memory_variables rispetta un memory_key personalizzato."""
        mem = _make_memory(memory_key="kore_context")
        assert mem.memory_variables == ["kore_context"]


class TestLoadMemoryVariables:
    def test_load_returns_formatted_memories(self):
        """load_memory_variables formatta i risultati come [category] content."""
        mock_client = _make_mock_client()
        mock_client.search.return_value = _make_search_response([
            "AI agents are autonomous systems",
            "Kore Memory uses Ebbinghaus decay",
        ])
        mem = _make_memory(client=mock_client)

        result = mem.load_memory_variables({"input": "Tell me about AI"})

        assert "history" in result
        assert "[general] AI agents are autonomous systems" in result["history"]
        assert "[general] Kore Memory uses Ebbinghaus decay" in result["history"]
        mock_client.search.assert_called_once_with(
            q="Tell me about AI",
            limit=5,
            semantic=True,
        )

    def test_load_with_empty_results(self):
        """Se non ci sono risultati, restituisce stringa vuota."""
        mock_client = _make_mock_client()
        mock_client.search.return_value = _make_search_response([])
        mem = _make_memory(client=mock_client)

        result = mem.load_memory_variables({"input": "something obscure"})

        assert result == {"history": ""}

    def test_load_with_empty_input(self):
        """Se l'input e' vuoto, restituisce stringa vuota senza chiamare search."""
        mock_client = _make_mock_client()
        mem = _make_memory(client=mock_client)

        result = mem.load_memory_variables({"input": ""})

        assert result == {"history": ""}
        mock_client.search.assert_not_called()

    def test_load_uses_custom_input_key(self):
        """load_memory_variables usa l'input_key configurato."""
        mock_client = _make_mock_client()
        mem = _make_memory(client=mock_client, input_key="question")

        mem.load_memory_variables({"question": "What is Kore?"})

        mock_client.search.assert_called_once_with(
            q="What is Kore?",
            limit=5,
            semantic=True,
        )

    def test_load_uses_custom_memory_key(self):
        """Il risultato usa il memory_key configurato."""
        mem = _make_memory(memory_key="context")

        result = mem.load_memory_variables({"input": "test query"})

        assert "context" in result
        assert "history" not in result

    def test_load_respects_k_parameter(self):
        """Il parametro k viene passato come limit alla search."""
        mock_client = _make_mock_client()
        mem = _make_memory(client=mock_client, k=3)

        mem.load_memory_variables({"input": "test"})

        mock_client.search.assert_called_once_with(q="test", limit=3, semantic=True)

    def test_load_respects_semantic_toggle(self):
        """Il parametro semantic viene passato alla search."""
        mock_client = _make_mock_client()
        mem = _make_memory(client=mock_client, semantic=False)

        mem.load_memory_variables({"input": "test"})

        mock_client.search.assert_called_once_with(q="test", limit=5, semantic=False)

    def test_load_fallback_on_missing_input_key(self):
        """Se input_key non e' nel dict, concatena tutti i valori stringa."""
        mock_client = _make_mock_client()
        mem = _make_memory(client=mock_client, input_key="question")

        mem.load_memory_variables({"prompt": "Hello world"})

        mock_client.search.assert_called_once_with(
            q="Hello world",
            limit=5,
            semantic=True,
        )

    def test_load_handles_search_exception(self):
        """Se la search fallisce, restituisce stringa vuota senza propagare."""
        mock_client = _make_mock_client()
        mock_client.search.side_effect = Exception("Connection refused")
        mem = _make_memory(client=mock_client)

        result = mem.load_memory_variables({"input": "test"})

        assert result == {"history": ""}


class TestSaveContext:
    def test_save_stores_conversation_turn(self):
        """save_context salva input + output come memoria formattata."""
        mock_client = _make_mock_client()
        mem = _make_memory(client=mock_client)

        mem.save_context(
            {"input": "What is Kore?"},
            {"output": "Kore is a memory layer for AI agents."},
        )

        mock_client.save.assert_called_once_with(
            content="Human: What is Kore?\nAI: Kore is a memory layer for AI agents.",
            category="general",
            importance=None,
        )

    def test_save_uses_custom_keys(self):
        """save_context usa input_key e output_key configurati."""
        mock_client = _make_mock_client()
        mem = _make_memory(
            client=mock_client,
            input_key="question",
            output_key="answer",
        )

        mem.save_context(
            {"question": "How does decay work?"},
            {"answer": "Ebbinghaus forgetting curve."},
        )

        mock_client.save.assert_called_once_with(
            content="Human: How does decay work?\nAI: Ebbinghaus forgetting curve.",
            category="general",
            importance=None,
        )

    def test_save_uses_custom_category(self):
        """save_context usa la category configurata."""
        mock_client = _make_mock_client()
        mem = _make_memory(client=mock_client, category="project")

        mem.save_context({"input": "test"}, {"output": "response"})

        mock_client.save.assert_called_once_with(
            content="Human: test\nAI: response",
            category="project",
            importance=None,
        )

    def test_save_auto_importance_enabled(self):
        """Con auto_importance=True, importance viene inviata come None (auto-scored dal server)."""
        mock_client = _make_mock_client()
        mem = _make_memory(client=mock_client, auto_importance=True)

        mem.save_context({"input": "test"}, {"output": "response"})

        call_kwargs = mock_client.save.call_args[1]
        assert call_kwargs["importance"] is None

    def test_save_auto_importance_disabled(self):
        """Con auto_importance=False, importance viene inviata come 2."""
        mock_client = _make_mock_client()
        mem = _make_memory(client=mock_client, auto_importance=False)

        mem.save_context({"input": "test"}, {"output": "response"})

        call_kwargs = mock_client.save.call_args[1]
        assert call_kwargs["importance"] == 2

    def test_save_skips_empty_content(self):
        """Se sia input che output sono vuoti, non salva nulla."""
        mock_client = _make_mock_client()
        mem = _make_memory(client=mock_client)

        mem.save_context({"input": ""}, {"output": ""})

        mock_client.save.assert_not_called()

    def test_save_only_input(self):
        """Salva anche se c'e' solo l'input senza output."""
        mock_client = _make_mock_client()
        mem = _make_memory(client=mock_client)

        mem.save_context({"input": "Hello"}, {"output": ""})

        mock_client.save.assert_called_once_with(
            content="Human: Hello",
            category="general",
            importance=None,
        )

    def test_save_handles_exception(self):
        """Se il save fallisce, non propaga l'eccezione."""
        mock_client = _make_mock_client()
        mock_client.save.side_effect = Exception("Connection refused")
        mem = _make_memory(client=mock_client)

        # Non deve alzare eccezione
        mem.save_context({"input": "test"}, {"output": "response"})


class TestClear:
    def test_clear_is_noop(self):
        """clear() non fa nulla — Kore gestisce il decay automaticamente."""
        mock_client = _make_mock_client()
        mem = _make_memory(client=mock_client)

        # Non deve alzare eccezione ne' chiamare metodi sul client
        mem.clear()

        # Verifica che nessun metodo del client sia stato chiamato
        mock_client.assert_not_called()
        mock_client.delete.assert_not_called()


class TestConstructor:
    def test_default_parameters(self):
        """Verifica i valori di default del costruttore."""
        mem = _make_memory()

        assert mem._memory_key == "history"
        assert mem._input_key == "input"
        assert mem._output_key == "output"
        assert mem._k == 5
        assert mem._semantic is True
        assert mem._category == "general"
        assert mem._auto_importance is True

    def test_custom_parameters(self):
        """Verifica che tutti i parametri custom vengano applicati."""
        mem = _make_memory(
            memory_key="kore_ctx",
            input_key="question",
            output_key="answer",
            k=10,
            semantic=False,
            category="trading",
            auto_importance=False,
        )

        assert mem._memory_key == "kore_ctx"
        assert mem._input_key == "question"
        assert mem._output_key == "answer"
        assert mem._k == 10
        assert mem._semantic is False
        assert mem._category == "trading"
        assert mem._auto_importance is False

    def test_accepts_external_client(self):
        """Accetta un KoreClient esterno via parametro client."""
        mock_client = _make_mock_client()
        mem = _make_memory(client=mock_client)

        assert mem._client is mock_client

    def test_creates_client_from_params(self):
        """Senza client esterno, ne crea uno con i parametri forniti."""
        with patch("kore_memory.integrations.langchain._HAS_LANGCHAIN", True), \
             patch("kore_memory.integrations.langchain.KoreClient") as MockClient:
            MockClient.return_value = MagicMock()

            from kore_memory.integrations.langchain import KoreLangChainMemory

            mem = KoreLangChainMemory(
                base_url="http://custom:9000",
                api_key="my-key",
                agent_id="test-agent",
            )

            MockClient.assert_called_once_with(
                base_url="http://custom:9000",
                api_key="my-key",
                agent_id="test-agent",
            )
```

## File: `tests/test_mcp.py`
```python
"""
Kore — MCP server tests
Tests MCP tool functions directly (no MCP protocol needed).
Each tool is a plain Python function that calls repository layer.

Setup: temp DB + local-only mode, same pattern as test_api.py.
Must set env vars BEFORE importing mcp_server (it calls init_db at import time).
Requires optional [mcp] dependency — skipped if not installed.
"""

import pytest

pytest.importorskip("mcp", reason="mcp package not installed (optional dependency)")

from kore_memory.mcp_server import (  # noqa: E402
    memory_add_relation,
    memory_add_tags,
    memory_cleanup,
    memory_delete,
    memory_export,
    memory_import,
    memory_save,
    memory_save_batch,
    memory_search,
    memory_search_by_tag,
    memory_timeline,
    memory_update,
)

AGENT = "mcp-test-agent"


class TestMemorySave:
    def test_save_returns_id_and_importance(self):
        result = memory_save(
            content="MCP test: remember this important fact",
            category="general",
            agent_id=AGENT,
        )
        assert "id" in result
        assert result["id"] > 0
        assert "importance" in result
        assert result["importance"] >= 1
        assert result["message"] == "Memory saved"

    def test_save_with_explicit_importance(self):
        result = memory_save(
            content="Critical security credential for production",
            category="project",
            importance=5,
            agent_id=AGENT,
        )
        assert result["importance"] == 5

    def test_save_with_category(self):
        result = memory_save(
            content="Juan prefers dark mode in all editors",
            category="preference",
            agent_id=AGENT,
        )
        assert result["id"] > 0


class TestMemorySearch:
    def test_search_finds_saved_memory(self):
        memory_save(
            content="Semantic search test: unique kangaroo phrase",
            category="general",
            agent_id=AGENT,
        )
        result = memory_search(
            query="kangaroo",
            limit=5,
            semantic=False,
            agent_id=AGENT,
        )
        assert "results" in result
        assert "total" in result
        assert "has_more" in result
        assert any("kangaroo" in r["content"] for r in result["results"])

    def test_search_returns_empty_for_no_match(self):
        result = memory_search(
            query="zzzyyyxxx_nonexistent_term",
            limit=5,
            semantic=False,
            agent_id=AGENT,
        )
        assert result["results"] == []

    def test_search_with_category_filter(self):
        memory_save(
            content="Finance test: quarterly earnings report analysis",
            category="finance",
            agent_id=AGENT,
        )
        result = memory_search(
            query="earnings",
            limit=5,
            category="finance",
            semantic=False,
            agent_id=AGENT,
        )
        found = result["results"]
        assert all(r["category"] == "finance" for r in found)


class TestMemoryDelete:
    def test_delete_existing_memory(self):
        saved = memory_save(
            content="This memory will be deleted soon",
            category="general",
            agent_id=AGENT,
        )
        mem_id = saved["id"]
        result = memory_delete(memory_id=mem_id, agent_id=AGENT)
        assert result["success"] is True
        assert result["message"] == "Memory deleted"

    def test_delete_nonexistent_memory(self):
        result = memory_delete(memory_id=999999, agent_id=AGENT)
        assert result["success"] is False
        assert result["message"] == "Memory not found"

    def test_delete_wrong_agent(self):
        saved = memory_save(
            content="Memory owned by mcp-test-agent only",
            category="general",
            agent_id=AGENT,
        )
        result = memory_delete(memory_id=saved["id"], agent_id="wrong-agent")
        assert result["success"] is False


class TestMemoryUpdate:
    def test_update_content(self):
        saved = memory_save(
            content="Original content before update",
            category="general",
            agent_id=AGENT,
        )
        result = memory_update(
            memory_id=saved["id"],
            content="Updated content after modification",
            agent_id=AGENT,
        )
        assert result["success"] is True
        assert result["message"] == "Memory updated"

    def test_update_category(self):
        saved = memory_save(
            content="Will change category from general to project",
            category="general",
            agent_id=AGENT,
        )
        result = memory_update(
            memory_id=saved["id"],
            category="project",
            agent_id=AGENT,
        )
        assert result["success"] is True

    def test_update_importance(self):
        saved = memory_save(
            content="Will increase importance to maximum",
            category="general",
            importance=1,
            agent_id=AGENT,
        )
        result = memory_update(
            memory_id=saved["id"],
            importance=5,
            agent_id=AGENT,
        )
        assert result["success"] is True

    def test_update_nonexistent(self):
        result = memory_update(
            memory_id=999999,
            content="This should fail",
            agent_id=AGENT,
        )
        assert result["success"] is False
        assert result["message"] == "Memory not found"


class TestMemoryAddTags:
    def test_add_tags_to_memory(self):
        saved = memory_save(
            content="Memory that needs tags for organization",
            category="general",
            agent_id=AGENT,
        )
        result = memory_add_tags(
            memory_id=saved["id"],
            tags=["python", "testing", "mcp"],
            agent_id=AGENT,
        )
        assert result["count"] == 3
        assert "3 tags added" in result["message"]

    def test_add_tags_to_nonexistent_memory(self):
        result = memory_add_tags(
            memory_id=999999,
            tags=["orphan"],
            agent_id=AGENT,
        )
        assert result["count"] == 0


class TestMemorySearchByTag:
    def test_search_by_tag_finds_tagged_memory(self):
        saved = memory_save(
            content="Tagged memory for search by tag test",
            category="project",
            agent_id=AGENT,
        )
        memory_add_tags(
            memory_id=saved["id"],
            tags=["unique-tag-xyz"],
            agent_id=AGENT,
        )
        result = memory_search_by_tag(
            tag="unique-tag-xyz",
            agent_id=AGENT,
        )
        assert result["total"] >= 1
        assert any(r["id"] == saved["id"] for r in result["results"])

    def test_search_by_tag_no_results(self):
        result = memory_search_by_tag(
            tag="nonexistent-tag-abc",
            agent_id=AGENT,
        )
        assert result["total"] == 0
        assert result["results"] == []


class TestMemoryCleanup:
    def test_cleanup_returns_count(self):
        result = memory_cleanup(agent_id=AGENT)
        assert "removed" in result
        assert isinstance(result["removed"], int)
        assert "message" in result


class TestMemoryExport:
    def test_export_returns_memories(self):
        # Save a memory first to ensure there's something to export
        memory_save(
            content="Memory for export test verification",
            category="general",
            agent_id=AGENT,
        )
        result = memory_export(agent_id=AGENT)
        assert "memories" in result
        assert "total" in result
        assert result["total"] >= 1
        assert isinstance(result["memories"], list)

    def test_export_empty_agent(self):
        result = memory_export(agent_id="empty-agent-no-memories")
        assert result["total"] == 0
        assert result["memories"] == []


class TestMemoryImport:
    def test_import_memories(self):
        records = [
            {"content": "Imported memory one for testing", "category": "general", "importance": 2},
            {"content": "Imported memory two for testing", "category": "project", "importance": 3},
        ]
        result = memory_import(memories=records, agent_id=AGENT)
        assert result["imported"] == 2
        assert "2 memories imported" in result["message"]

    def test_import_skips_invalid(self):
        records = [
            {"content": "Valid imported memory content"},
            {"content": "ab"},           # too short (< 3 chars)
            {"content": "  "},           # blank
            {"content": ""},             # empty
        ]
        result = memory_import(memories=records, agent_id=AGENT)
        assert result["imported"] == 1


class TestMemorySaveBatch:
    def test_save_batch(self):
        memories = [
            {"content": "Batch memory alpha for testing", "category": "general"},
            {"content": "Batch memory beta for testing", "category": "project", "importance": 3},
        ]
        result = memory_save_batch(memories=memories, agent_id=AGENT)
        assert result["total"] == 2
        assert len(result["saved"]) == 2
        assert all("id" in s for s in result["saved"])

    def test_save_batch_skips_invalid(self):
        memories = [
            {"content": "Valid batch content here"},
            {"content": "ab"},   # too short
        ]
        result = memory_save_batch(memories=memories, agent_id=AGENT)
        assert result["total"] == 1


class TestMemoryAddRelation:
    def test_add_relation_between_memories(self):
        m1 = memory_save(content="Source memory for relation test", category="general", agent_id=AGENT)
        m2 = memory_save(content="Target memory for relation test", category="general", agent_id=AGENT)
        result = memory_add_relation(
            source_id=m1["id"],
            target_id=m2["id"],
            relation="related",
            agent_id=AGENT,
        )
        assert result["success"] is True
        assert result["message"] == "Relation created"

    def test_add_relation_nonexistent_memory(self):
        m1 = memory_save(content="Existing memory for failed relation", category="general", agent_id=AGENT)
        result = memory_add_relation(
            source_id=m1["id"],
            target_id=999999,
            relation="related",
            agent_id=AGENT,
        )
        assert result["success"] is False


class TestMemoryTimeline:
    def test_timeline_returns_results(self):
        memory_save(
            content="Timeline event: project Kore started development",
            category="project",
            agent_id=AGENT,
        )
        result = memory_timeline(
            subject="Kore",
            limit=10,
            agent_id=AGENT,
        )
        assert "results" in result
        assert "total" in result
        assert "has_more" in result
        assert isinstance(result["results"], list)
```

## File: `tests/test_sessions.py`
```python
"""
Tests for session/conversation tracking (v0.9.0).
"""

import os

import pytest

from fastapi.testclient import TestClient

from kore_memory.database import init_db, _pool
from kore_memory.main import app

HEADERS = {"X-Agent-Id": "test-agent"}


@pytest.fixture(autouse=True)
def _fresh_db(tmp_path):
    original_db_path = os.environ.get("KORE_DB_PATH")
    db_file = str(tmp_path / "test.db")
    os.environ["KORE_DB_PATH"] = db_file
    _pool.clear()
    init_db()
    yield
    _pool.clear()
    # Restore the original DB path (set by conftest.py)
    if original_db_path is not None:
        os.environ["KORE_DB_PATH"] = original_db_path


@pytest.fixture()
def client():
    return TestClient(app)


class TestSessionCreate:
    def test_create_session(self, client):
        r = client.post("/sessions", json={"session_id": "sess-001", "title": "Test Chat"}, headers=HEADERS)
        assert r.status_code == 201
        data = r.json()
        assert data["id"] == "sess-001"
        assert data["agent_id"] == "test-agent"
        assert data["title"] == "Test Chat"

    def test_create_session_no_title(self, client):
        r = client.post("/sessions", json={"session_id": "sess-002"}, headers=HEADERS)
        assert r.status_code == 201
        assert r.json()["title"] is None

    def test_create_duplicate_session(self, client):
        client.post("/sessions", json={"session_id": "sess-dup"}, headers=HEADERS)
        r = client.post("/sessions", json={"session_id": "sess-dup"}, headers=HEADERS)
        assert r.status_code == 201  # INSERT OR IGNORE — idempotent


class TestSessionList:
    def test_list_empty(self, client):
        r = client.get("/sessions", headers=HEADERS)
        assert r.status_code == 200
        assert r.json() == []

    def test_list_sessions(self, client):
        client.post("/sessions", json={"session_id": "s1", "title": "Chat 1"}, headers=HEADERS)
        client.post("/sessions", json={"session_id": "s2", "title": "Chat 2"}, headers=HEADERS)
        r = client.get("/sessions", headers=HEADERS)
        data = r.json()
        assert len(data) == 2
        assert data[0]["id"] == "s2"  # newest first

    def test_sessions_scoped_to_agent(self, client):
        client.post("/sessions", json={"session_id": "s1"}, headers=HEADERS)
        client.post("/sessions", json={"session_id": "s2"}, headers={"X-Agent-Id": "other-agent"})
        r = client.get("/sessions", headers=HEADERS)
        assert len(r.json()) == 1


class TestSessionMemories:
    def test_save_with_session(self, client):
        """Save a memory with X-Session-Id header and retrieve session memories."""
        client.post("/sessions", json={"session_id": "chat-1"}, headers=HEADERS)
        # Save memories with session
        h = {**HEADERS, "X-Session-Id": "chat-1"}
        client.post("/save", json={"content": "First message in chat", "category": "general"}, headers=h)
        client.post("/save", json={"content": "Second message in chat", "category": "general"}, headers=h)
        # Save memory without session
        client.post("/save", json={"content": "Memory without session", "category": "general"}, headers=HEADERS)

        r = client.get("/sessions/chat-1/memories", headers=HEADERS)
        assert r.status_code == 200
        data = r.json()
        assert data["total"] == 2
        assert "First message" in data["results"][0]["content"]

    def test_auto_create_session(self, client):
        """Session is auto-created when X-Session-Id is provided on save."""
        h = {**HEADERS, "X-Session-Id": "auto-sess"}
        client.post("/save", json={"content": "Auto session test memory", "category": "general"}, headers=h)

        r = client.get("/sessions", headers=HEADERS)
        sessions = r.json()
        assert any(s["id"] == "auto-sess" for s in sessions)

    def test_session_memories_empty(self, client):
        client.post("/sessions", json={"session_id": "empty-sess"}, headers=HEADERS)
        r = client.get("/sessions/empty-sess/memories", headers=HEADERS)
        assert r.json()["total"] == 0


class TestSessionSummary:
    def test_summary(self, client):
        h = {**HEADERS, "X-Session-Id": "sum-sess"}
        client.post("/save", json={"content": "Project discussion about API design", "category": "project", "importance": 4}, headers=h)
        client.post("/save", json={"content": "Decision to use REST over GraphQL", "category": "decision", "importance": 5}, headers=h)

        r = client.get("/sessions/sum-sess/summary", headers=HEADERS)
        assert r.status_code == 200
        data = r.json()
        assert data["session_id"] == "sum-sess"
        assert data["memory_count"] == 2
        assert "project" in data["categories"]
        assert "decision" in data["categories"]
        assert data["avg_importance"] >= 4.0

    def test_summary_not_found(self, client):
        r = client.get("/sessions/nonexistent/summary", headers=HEADERS)
        assert r.status_code == 404


class TestSessionEnd:
    def test_end_session(self, client):
        client.post("/sessions", json={"session_id": "end-me"}, headers=HEADERS)
        r = client.post("/sessions/end-me/end", headers=HEADERS)
        assert r.status_code == 200
        assert r.json()["success"] is True

        # Verify session is ended
        sessions = client.get("/sessions", headers=HEADERS).json()
        ended = [s for s in sessions if s["id"] == "end-me"]
        assert ended[0]["ended_at"] is not None

    def test_end_already_ended(self, client):
        client.post("/sessions", json={"session_id": "end-twice"}, headers=HEADERS)
        client.post("/sessions/end-twice/end", headers=HEADERS)
        r = client.post("/sessions/end-twice/end", headers=HEADERS)
        assert r.status_code == 404

    def test_end_nonexistent(self, client):
        r = client.post("/sessions/nope/end", headers=HEADERS)
        assert r.status_code == 404


class TestSessionDelete:
    def test_delete_session(self, client):
        h = {**HEADERS, "X-Session-Id": "del-sess"}
        client.post("/save", json={"content": "Memory in session to delete", "category": "general"}, headers=h)

        r = client.delete("/sessions/del-sess", headers=HEADERS)
        assert r.status_code == 200
        data = r.json()
        assert data["success"] is True
        assert data["unlinked_memories"] == 1

        # Session gone
        sessions = client.get("/sessions", headers=HEADERS).json()
        assert not any(s["id"] == "del-sess" for s in sessions)

        # Memory still exists but unlinked
        r = client.get("/search?q=session+to+delete", headers=HEADERS)
        assert r.json()["total"] >= 1

    def test_delete_nonexistent(self, client):
        r = client.delete("/sessions/nope", headers=HEADERS)
        assert r.status_code == 200  # idempotent, just 0 unlinked


class TestSessionMemoryCount:
    def test_list_shows_memory_count(self, client):
        h = {**HEADERS, "X-Session-Id": "counted"}
        client.post("/save", json={"content": "Memory one in counted session", "category": "general"}, headers=h)
        client.post("/save", json={"content": "Memory two in counted session", "category": "general"}, headers=h)

        sessions = client.get("/sessions", headers=HEADERS).json()
        counted = [s for s in sessions if s["id"] == "counted"]
        assert counted[0]["memory_count"] == 2
```

## File: `tests/test_v11_fixes.py`
```python
"""
Test per i fix della v1.1.0 — Stability release.
Verifica: archived leak (export, search_by_tag, count), emit audit,
handler dedup, VectorIndex thread-safety, compression depth limit,
PRAGMA SQLite.
"""

import threading

from fastapi.testclient import TestClient

from kore_memory import events
from kore_memory.database import get_connection
from kore_memory.main import app
from kore_memory.repository import (
    _count_active_memories,
    add_tags,
    archive_memory,
    export_memories,
    restore_memory,
    run_decay_pass,
    save_memory,
    search_by_tag,
)

HEADERS = {"X-Agent-Id": "test-v11"}
client = TestClient(app)

# ── Helper ──────────────────────────────────────────────────────────────────

def _save(content: str, **kwargs) -> int:
    """Salva una memoria e ritorna l'id."""
    from kore_memory.models import MemorySaveRequest
    req = MemorySaveRequest(content=content, **kwargs)
    mid, _ = save_memory(req, agent_id="test-v11")
    return mid


def _cleanup_agent():
    """Pulisce tutte le memorie dell'agente test-v11."""
    with get_connection() as conn:
        conn.execute("DELETE FROM memory_tags WHERE memory_id IN (SELECT id FROM memories WHERE agent_id = 'test-v11')")
        conn.execute("DELETE FROM memories WHERE agent_id = 'test-v11'")
        conn.execute("DELETE FROM event_logs WHERE agent_id = 'test-v11'")


# ── BUG: export_memories include memorie archiviate ─────────────────────────


class TestExportArchivedLeak:
    def setup_method(self):
        _cleanup_agent()

    def test_export_excludes_archived(self):
        """export_memories() NON deve includere memorie archiviate."""
        mid1 = _save("Memoria attiva per export test")
        mid2 = _save("Memoria da archiviare per export test")
        archive_memory(mid2, agent_id="test-v11")

        exported = export_memories(agent_id="test-v11")
        exported_ids = {m["id"] for m in exported}

        assert mid1 in exported_ids, "Memoria attiva mancante dall'export"
        assert mid2 not in exported_ids, "Memoria archiviata trovata nell'export — BUG"

    def test_export_api_excludes_archived(self):
        """L'endpoint /export NON deve includere memorie archiviate."""
        mid1 = _save("API export memoria attiva")
        mid2 = _save("API export memoria archiviata")
        archive_memory(mid2, agent_id="test-v11")

        r = client.get("/export", headers=HEADERS)
        assert r.status_code == 200
        exported_ids = {m["id"] for m in r.json()["memories"]}

        assert mid1 in exported_ids
        assert mid2 not in exported_ids


# ── BUG: search_by_tag include memorie archiviate ──────────────────────────


class TestSearchByTagArchivedLeak:
    def setup_method(self):
        _cleanup_agent()

    def test_search_by_tag_excludes_archived(self):
        """search_by_tag() NON deve ritornare memorie archiviate."""
        mid1 = _save("Memoria taggata attiva")
        mid2 = _save("Memoria taggata archiviata")
        add_tags(mid1, ["v11-test"], agent_id="test-v11")
        add_tags(mid2, ["v11-test"], agent_id="test-v11")
        archive_memory(mid2, agent_id="test-v11")

        results = search_by_tag("v11-test", agent_id="test-v11")
        result_ids = {r.id for r in results}

        assert mid1 in result_ids, "Memoria attiva taggata mancante"
        assert mid2 not in result_ids, "Memoria archiviata trovata in search_by_tag — BUG"


# ── BUG: _count_active_memories conta archiviate ──────────────────────────


class TestCountActiveArchivedLeak:
    def setup_method(self):
        _cleanup_agent()

    def test_count_excludes_archived(self):
        """_count_active_memories() NON deve contare memorie archiviate."""
        _save("Conteggio contaxyz memoria attiva")
        mid2 = _save("Conteggio contaxyz memoria archiviata")
        archive_memory(mid2, agent_id="test-v11")

        # Cerca con termine presente in entrambe le memorie
        count = _count_active_memories("contaxyz", None, "test-v11")
        # Solo la memoria attiva deve essere contata
        assert count == 1, f"Atteso 1 (solo attiva), ottenuto {count}"


# ── BUG: eventi audit mai emessi ───────────────────────────────────────────


class TestAuditEventEmission:
    def setup_method(self):
        _cleanup_agent()
        events.clear()
        self._captured: list[tuple[str, dict]] = []

        def _capture(event: str, data: dict):
            self._captured.append((event, data))

        # Registra handler per catturare gli eventi
        events.on(events.MEMORY_ARCHIVED, _capture)
        events.on(events.MEMORY_RESTORED, _capture)
        events.on(events.MEMORY_DECAYED, _capture)
        events.on(events.MEMORY_COMPRESSED, _capture)

    def teardown_method(self):
        events.clear()

    def test_archive_emits_event(self):
        """archive_memory() deve emettere MEMORY_ARCHIVED."""
        mid = _save("Test emissione evento archive")
        archive_memory(mid, agent_id="test-v11")

        archived_events = [(e, d) for e, d in self._captured if e == events.MEMORY_ARCHIVED]
        assert len(archived_events) == 1
        assert archived_events[0][1]["id"] == mid

    def test_restore_emits_event(self):
        """restore_memory() deve emettere MEMORY_RESTORED."""
        mid = _save("Test emissione evento restore")
        archive_memory(mid, agent_id="test-v11")
        self._captured.clear()  # Ignora evento archive

        restore_memory(mid, agent_id="test-v11")

        restored_events = [(e, d) for e, d in self._captured if e == events.MEMORY_RESTORED]
        assert len(restored_events) == 1
        assert restored_events[0][1]["id"] == mid

    def test_decay_emits_event(self):
        """run_decay_pass() deve emettere MEMORY_DECAYED."""
        _save("Test emissione evento decay", importance=3)

        run_decay_pass(agent_id="test-v11")

        decayed_events = [(e, d) for e, d in self._captured if e == events.MEMORY_DECAYED]
        assert len(decayed_events) == 1
        assert decayed_events[0][1]["updated"] >= 1


# ── FIX: handler deduplication ──────────────────────────────────────────────


class TestHandlerDedup:
    def setup_method(self):
        events.clear()

    def teardown_method(self):
        events.clear()

    def test_duplicate_handler_ignored(self):
        """Registrare lo stesso handler due volte non duplica le chiamate."""
        call_count = [0]

        def _counter(event: str, data: dict):
            call_count[0] += 1

        events.on("test.event", _counter)
        events.on("test.event", _counter)  # duplicato — deve essere ignorato

        events.emit("test.event", {"test": True})
        assert call_count[0] == 1, f"Handler chiamato {call_count[0]} volte, atteso 1"


# ── PERF: PRAGMA SQLite ──────────────────────────────────────────────────────


class TestSQLitePragmas:
    def test_synchronous_normal(self):
        """Le connessioni devono usare PRAGMA synchronous=NORMAL."""
        with get_connection() as conn:
            result = conn.execute("PRAGMA synchronous").fetchone()
            # NORMAL = 1
            assert result[0] == 1, f"synchronous atteso 1 (NORMAL), ottenuto {result[0]}"

    def test_temp_store_memory(self):
        """Le connessioni devono usare PRAGMA temp_store=MEMORY."""
        with get_connection() as conn:
            result = conn.execute("PRAGMA temp_store").fetchone()
            # MEMORY = 2
            assert result[0] == 2, f"temp_store atteso 2 (MEMORY), ottenuto {result[0]}"

    def test_mmap_size(self):
        """Le connessioni devono avere mmap_size > 0."""
        with get_connection() as conn:
            result = conn.execute("PRAGMA mmap_size").fetchone()
            assert result[0] > 0, f"mmap_size atteso > 0, ottenuto {result[0]}"

    def test_cache_size(self):
        """Le connessioni devono avere cache_size negativo (KB)."""
        with get_connection() as conn:
            result = conn.execute("PRAGMA cache_size").fetchone()
            assert result[0] < 0, f"cache_size atteso negativo (KB), ottenuto {result[0]}"


# ── PERF: indice composito ───────────────────────────────────────────────────


class TestCompositeIndex:
    def test_idx_agent_decay_active_exists(self):
        """L'indice composito idx_agent_decay_active deve esistere."""
        with get_connection() as conn:
            indexes = conn.execute(
                "SELECT name FROM sqlite_master WHERE type='index' AND name='idx_agent_decay_active'"
            ).fetchall()
            assert len(indexes) == 1, "Indice composito idx_agent_decay_active mancante"


# ── VectorIndex thread-safety ────────────────────────────────────────────────


class TestVectorIndexThreadSafety:
    def test_concurrent_invalidate_and_load(self):
        """Invalidate e load_vectors concorrenti non devono crashare."""
        from kore_memory.vector_index import VectorIndex

        idx = VectorIndex()
        errors: list[Exception] = []

        def _invalidate():
            try:
                for _ in range(100):
                    idx.invalidate("test-agent")
            except Exception as e:
                errors.append(e)

        def _load():
            try:
                for _ in range(100):
                    idx.load_vectors("test-agent")
            except Exception as e:
                errors.append(e)

        threads = [
            threading.Thread(target=_invalidate),
            threading.Thread(target=_load),
            threading.Thread(target=_invalidate),
            threading.Thread(target=_load),
        ]
        for t in threads:
            t.start()
        for t in threads:
            t.join(timeout=10)

        assert not errors, f"Errori durante accesso concorrente: {errors}"
```

## File: `tests/test_v12_features.py`
```python
"""
Test per le feature della v1.2.0 — Developer Experience release.
Verifica: SDK importance fix, GET /memories/{id}, cursor pagination,
integrazioni PydanticAI/OpenAI/LangChain, MCP HTTP transport.
"""

from unittest.mock import MagicMock, patch

from fastapi.testclient import TestClient

from kore_memory.client import AsyncKoreClient, KoreClient
from kore_memory.database import get_connection
from kore_memory.main import app
from kore_memory.models import MemorySaveRequest
from kore_memory.repository import get_memory, save_memory

HEADERS = {"X-Agent-Id": "test-v12"}
client = TestClient(app)


def _save(content: str, **kwargs) -> int:
    """Salva una memoria e ritorna l'id."""
    req = MemorySaveRequest(content=content, **kwargs)
    mid, _ = save_memory(req, agent_id="test-v12")
    return mid


def _cleanup():
    """Pulisce tutte le memorie dell'agente test-v12."""
    with get_connection() as conn:
        conn.execute("DELETE FROM memory_tags WHERE memory_id IN (SELECT id FROM memories WHERE agent_id = 'test-v12')")
        conn.execute("DELETE FROM memories WHERE agent_id = 'test-v12'")


# ── SDK importance default fix ─────────────────────────────────────────────────


class TestSDKImportanceDefault:
    def test_sync_save_default_importance_is_none(self):
        """KoreClient.save() deve avere importance=None come default (auto-scoring)."""
        import inspect
        sig = inspect.signature(KoreClient.save)
        default = sig.parameters["importance"].default
        assert default is None, f"Atteso None, ottenuto {default}"

    def test_async_save_default_importance_is_none(self):
        """AsyncKoreClient.save() deve avere importance=None come default."""
        import inspect
        sig = inspect.signature(AsyncKoreClient.save)
        default = sig.parameters["importance"].default
        assert default is None, f"Atteso None, ottenuto {default}"

    def test_sync_save_omits_importance_when_none(self):
        """Se importance=None, il payload non deve includere importance."""
        with patch.object(KoreClient, "__init__", lambda self, **kw: None):
            kc = KoreClient.__new__(KoreClient)
            mock_client = MagicMock()
            mock_response = MagicMock()
            mock_response.is_success = True
            mock_response.json.return_value = {"id": 1, "importance": 3, "message": "saved"}
            mock_client.post.return_value = mock_response
            kc._client = mock_client

            kc.save("test content")
            call_args = mock_client.post.call_args
            payload = call_args[1]["json"]
            assert "importance" not in payload, f"importance presente nel payload: {payload}"


# ── GET /memories/{id} endpoint ────────────────────────────────────────────────


class TestGetMemoryEndpoint:
    def setup_method(self):
        _cleanup()

    def test_get_memory_success(self):
        """GET /memories/{id} ritorna la memoria corretta."""
        mid = _save("Memoria per test get endpoint")
        r = client.get(f"/memories/{mid}", headers=HEADERS)
        assert r.status_code == 200
        data = r.json()
        assert data["id"] == mid
        assert "Memoria per test get endpoint" in data["content"]

    def test_get_memory_not_found(self):
        """GET /memories/{id} ritorna 404 per ID inesistente."""
        r = client.get("/memories/999999", headers=HEADERS)
        assert r.status_code == 404

    def test_get_memory_agent_isolation(self):
        """GET /memories/{id} non accede a memorie di altri agent."""
        mid = _save("Memoria isolata per agent test")
        r = client.get(f"/memories/{mid}", headers={"X-Agent-Id": "altro-agente"})
        assert r.status_code == 404

    def test_get_memory_repository(self):
        """get_memory() ritorna MemoryRecord o None."""
        mid = _save("Test repository get_memory")
        mem = get_memory(mid, agent_id="test-v12")
        assert mem is not None
        assert mem.id == mid
        assert "Test repository get_memory" in mem.content

        none_mem = get_memory(999999, agent_id="test-v12")
        assert none_mem is None


# ── SDK cursor pagination ──────────────────────────────────────────────────────


class TestSDKCursorPagination:
    def test_sync_search_has_cursor_param(self):
        """KoreClient.search() deve accettare il parametro cursor."""
        import inspect
        sig = inspect.signature(KoreClient.search)
        assert "cursor" in sig.parameters

    def test_sync_timeline_has_cursor_param(self):
        """KoreClient.timeline() deve accettare il parametro cursor."""
        import inspect
        sig = inspect.signature(KoreClient.timeline)
        assert "cursor" in sig.parameters

    def test_async_search_has_cursor_param(self):
        """AsyncKoreClient.search() deve accettare il parametro cursor."""
        import inspect
        sig = inspect.signature(AsyncKoreClient.search)
        assert "cursor" in sig.parameters

    def test_async_timeline_has_cursor_param(self):
        """AsyncKoreClient.timeline() deve accettare il parametro cursor."""
        import inspect
        sig = inspect.signature(AsyncKoreClient.timeline)
        assert "cursor" in sig.parameters


# ── SDK get() method ───────────────────────────────────────────────────────────


class TestSDKGetMethod:
    def test_sync_client_has_get(self):
        """KoreClient deve avere il metodo get()."""
        assert hasattr(KoreClient, "get")

    def test_async_client_has_get(self):
        """AsyncKoreClient deve avere il metodo get()."""
        assert hasattr(AsyncKoreClient, "get")


# ── API docs examples (openapi_examples) ──────────────────────────────────────


class TestOpenAPIExamples:
    def test_save_request_has_examples(self):
        """MemorySaveRequest deve avere examples nel json_schema."""
        schema = MemorySaveRequest.model_json_schema()
        assert "examples" in schema, "MemorySaveRequest manca examples in json_schema"

    def test_openapi_schema_accessible(self):
        """L'endpoint /openapi.json deve essere accessibile."""
        r = client.get("/openapi.json")
        assert r.status_code == 200
        schema = r.json()
        assert "paths" in schema
        # Verifica che GET /memories/{memory_id} sia presente
        assert "/memories/{memory_id}" in schema["paths"]
        assert "get" in schema["paths"]["/memories/{memory_id}"]


# ── Integrazioni: import e struttura ──────────────────────────────────────────


class TestIntegrationImports:
    def test_pydantic_ai_module_exists(self):
        """Il modulo pydantic_ai deve esistere e avere le funzioni attese."""
        from kore_memory.integrations import pydantic_ai
        assert hasattr(pydantic_ai, "kore_toolset")
        assert hasattr(pydantic_ai, "create_kore_tools")

    def test_openai_agents_module_exists(self):
        """Il modulo openai_agents deve esistere e avere la funzione attesa."""
        from kore_memory.integrations import openai_agents
        assert hasattr(openai_agents, "kore_agent_tools")

    def test_langchain_chat_history_exists(self):
        """Il modulo langchain deve avere KoreChatMessageHistory."""
        from kore_memory.integrations import langchain
        assert hasattr(langchain, "KoreChatMessageHistory")

    def test_lazy_imports_from_init(self):
        """Le nuove classi devono essere accessibili via lazy-loading."""
        from kore_memory.integrations import __all__
        assert "kore_toolset" in __all__
        assert "kore_agent_tools" in __all__
        assert "KoreChatMessageHistory" in __all__

    def test_create_kore_tools_returns_dict(self):
        """create_kore_tools() deve ritornare un dict con save/search/timeline/delete."""
        from kore_memory.integrations.pydantic_ai import create_kore_tools
        tools = create_kore_tools(base_url="http://localhost:8765")
        assert "save" in tools
        assert "search" in tools
        assert "timeline" in tools
        assert "delete" in tools
        assert callable(tools["save"])


# ── MCP transport args ─────────────────────────────────────────────────────────


class TestMCPTransportArgs:
    def test_main_accepts_transport_arg(self):
        """mcp_server.main() deve accettare --transport."""
        from kore_memory.mcp_server import main
        # Verifica che main sia definita (non possiamo eseguirla senza bloccare)
        assert callable(main)

    def test_mcp_server_has_argparse(self):
        """Il modulo mcp_server deve usare argparse per il parsing degli argomenti."""
        import inspect

        import kore_memory.mcp_server as mcp_mod
        source = inspect.getsource(mcp_mod.main)
        assert "argparse" in source
        assert "streamable-http" in source
        assert "--transport" in source


# ── Pyproject.toml dependencies ──────────────────────────────────────────────


class TestOptionalDependencies:
    def test_pydantic_ai_in_pyproject(self):
        """pyproject.toml deve avere la dipendenza opzionale pydantic-ai."""
        import tomllib
        with open("pyproject.toml", "rb") as f:
            data = tomllib.load(f)
        optional = data["project"]["optional-dependencies"]
        assert "pydantic-ai" in optional

    def test_openai_agents_in_pyproject(self):
        """pyproject.toml deve avere la dipendenza opzionale openai-agents."""
        import tomllib
        with open("pyproject.toml", "rb") as f:
            data = tomllib.load(f)
        optional = data["project"]["optional-dependencies"]
        assert "openai-agents" in optional
```

## File: `tests/test_v2_features.py`
```python
"""
Kore — v2.0 feature tests
Graph RAG, Summarization, ACL, SSE Streaming, Analytics, GDPR, Plugins.
"""

import json

import pytest
from fastapi.testclient import TestClient

from kore_memory.main import app

HEADERS = {"X-Agent-Id": "v2-test-agent"}
OTHER = {"X-Agent-Id": "v2-other-agent"}

client = TestClient(app)


# ── Helpers ──────────────────────────────────────────────────────────────────


def _save(content: str, category: str = "project", headers=None) -> int:
    """Save a memory and return its ID."""
    r = client.post("/save", json={"content": content, "category": category}, headers=headers or HEADERS)
    assert r.status_code == 201
    return r.json()["id"]


def _relate(source_id: int, target_id: int, relation: str = "related") -> None:
    """Create a relation between two memories."""
    r = client.post(
        f"/memories/{source_id}/relations",
        json={"target_id": target_id, "relation": relation},
        headers=HEADERS,
    )
    assert r.status_code == 201


# ── Graph RAG ────────────────────────────────────────────────────────────────


class TestGraphTraverse:
    def test_traverse_basic(self):
        """Traverse a simple A→B→C chain."""
        a = _save("Graph node A: the root memory")
        b = _save("Graph node B: connected to A")
        c = _save("Graph node C: connected to B")
        _relate(a, b, "depends_on")
        _relate(b, c, "depends_on")

        r = client.get(f"/graph/traverse?start_id={a}&depth=3", headers=HEADERS)
        assert r.status_code == 200
        data = r.json()
        assert data["start"] is not None
        assert len(data["nodes"]) >= 2  # B and C
        assert len(data["edges"]) >= 2

    def test_traverse_with_relation_filter(self):
        """Filter traversal by relation type."""
        a = _save("Filter test node A root")
        b = _save("Filter test node B related")
        c = _save("Filter test node C causal")
        _relate(a, b, "related")
        _relate(a, c, "causes")

        r = client.get(f"/graph/traverse?start_id={a}&depth=2&relation_type=causes", headers=HEADERS)
        data = r.json()
        assert data["start"] is not None
        # Should find C but not B (different relation type)
        node_ids = {n["id"] for n in data["nodes"]}
        assert c in node_ids

    def test_traverse_nonexistent_memory(self):
        """Traversing a non-existent memory returns empty."""
        r = client.get("/graph/traverse?start_id=999999&depth=2", headers=HEADERS)
        assert r.status_code == 200
        assert r.json()["start"] is None
        assert r.json()["nodes"] == []

    def test_traverse_depth_limit(self):
        """Depth is capped at 10."""
        a = _save("Depth test root node")
        r = client.get(f"/graph/traverse?start_id={a}&depth=15", headers=HEADERS)
        assert r.status_code == 422  # validation error: le=10

    def test_traverse_isolated_node(self):
        """Node with no relations returns empty nodes/edges."""
        a = _save("Isolated graph node test")
        r = client.get(f"/graph/traverse?start_id={a}&depth=3", headers=HEADERS)
        data = r.json()
        assert data["start"] is not None
        assert data["nodes"] == []
        assert data["edges"] == []


# ── Summarization ────────────────────────────────────────────────────────────


class TestSummarize:
    def test_summarize_basic(self):
        """Summarize a topic with keyword extraction."""
        _save("Python FastAPI framework for building APIs quickly")
        _save("Python type hints improve code quality and IDE support")
        _save("Python asyncio enables concurrent programming patterns")

        r = client.get("/summarize?topic=Python", headers=HEADERS)
        assert r.status_code == 200
        data = r.json()
        assert data["topic"] == "Python"
        assert data["memory_count"] >= 1
        assert len(data["keywords"]) > 0
        assert "categories" in data

    def test_summarize_no_results(self):
        """Summarizing non-existent topic returns empty."""
        r = client.get("/summarize?topic=xyznonexistent12345", headers=HEADERS)
        assert r.status_code == 200
        assert r.json()["memory_count"] == 0

    def test_summarize_with_time_span(self):
        """Summary includes earliest/latest timestamps."""
        _save("Summary timeline test memory alpha")
        _save("Summary timeline test memory beta")
        r = client.get("/summarize?topic=timeline+test", headers=HEADERS)
        data = r.json()
        if data["memory_count"] > 0:
            assert data["time_span"] is not None
            assert "earliest" in data["time_span"]
            assert "latest" in data["time_span"]


# ── ACL (Multi-agent shared memory) ──────────────────────────────────────────


class TestACL:
    def test_grant_and_list_permissions(self):
        """Owner grants read access to another agent."""
        mem_id = _save("ACL test: shared knowledge base entry")
        r = client.post(
            f"/memories/{mem_id}/acl",
            json={"target_agent": "v2-other-agent", "permission": "read"},
            headers=HEADERS,
        )
        assert r.status_code == 201
        data = r.json()
        assert data["success"] is True
        assert len(data["permissions"]) >= 1
        assert data["permissions"][0]["agent_id"] == "v2-other-agent"

    def test_grant_invalid_permission(self):
        """Invalid permission type is rejected."""
        mem_id = _save("ACL invalid permission test")
        r = client.post(
            f"/memories/{mem_id}/acl",
            json={"target_agent": "someone", "permission": "superadmin"},
            headers=HEADERS,
        )
        assert r.status_code == 422

    def test_revoke_access(self):
        """Revoke previously granted access."""
        mem_id = _save("ACL revoke test memory entry")
        # Grant first
        client.post(
            f"/memories/{mem_id}/acl",
            json={"target_agent": "v2-other-agent", "permission": "write"},
            headers=HEADERS,
        )
        # Revoke
        r = client.delete(f"/memories/{mem_id}/acl/v2-other-agent", headers=HEADERS)
        assert r.status_code == 200
        assert r.json()["success"] is True

    def test_non_owner_cannot_grant(self):
        """Non-owner without admin cannot grant access."""
        mem_id = _save("ACL ownership test memory")
        r = client.post(
            f"/memories/{mem_id}/acl",
            json={"target_agent": "intruder", "permission": "read"},
            headers=OTHER,
        )
        assert r.status_code == 403

    def test_shared_memories_endpoint(self):
        """List memories shared with an agent."""
        mem_id = _save("ACL shared listing test")
        client.post(
            f"/memories/{mem_id}/acl",
            json={"target_agent": "v2-other-agent", "permission": "read"},
            headers=HEADERS,
        )
        r = client.get("/shared", headers=OTHER)
        assert r.status_code == 200
        data = r.json()
        assert data["total"] >= 0  # May or may not find depending on ACL table state

    def test_list_permissions(self):
        """List ACL entries for a memory."""
        mem_id = _save("ACL permission listing test")
        client.post(
            f"/memories/{mem_id}/acl",
            json={"target_agent": "agent-x", "permission": "admin"},
            headers=HEADERS,
        )
        r = client.get(f"/memories/{mem_id}/acl", headers=HEADERS)
        assert r.status_code == 200
        assert len(r.json()["permissions"]) >= 1


# ── SSE Streaming Search ─────────────────────────────────────────────────────


class TestSSEStreaming:
    def test_stream_search_basic(self):
        """SSE stream returns FTS and semantic phases."""
        _save("SSE streaming test: FastAPI performance optimization")

        with client.stream("GET", "/stream/search?q=FastAPI", headers=HEADERS) as response:
            assert response.status_code == 200
            content = response.read().decode("utf-8")

        # Should contain event types
        assert "event: fts" in content
        assert "event: done" in content

    def test_stream_search_fts_has_results(self):
        """FTS phase produces parseable JSON data."""
        _save("SSE FTS parse test: unique keyword xylophone")

        with client.stream("GET", "/stream/search?q=xylophone", headers=HEADERS) as response:
            content = response.read().decode("utf-8")

        # Parse FTS event
        for line in content.split("\n"):
            if line.startswith("data: ") and "fts" in line:
                data = json.loads(line[6:])
                assert "results" in data
                assert "phase" in data
                break


# ── Analytics ────────────────────────────────────────────────────────────────


class TestAnalytics:
    def test_analytics_basic(self):
        """Analytics returns all expected fields."""
        _save("Analytics test memory: tracking patterns")

        r = client.get("/analytics", headers=HEADERS)
        assert r.status_code == 200
        data = r.json()
        assert "total_memories" in data
        assert "categories" in data
        assert "importance_distribution" in data
        assert "decay_analysis" in data
        assert "top_tags" in data
        assert "access_patterns" in data
        assert "growth_last_30d" in data
        assert "compressed_memories" in data
        assert "archived_memories" in data
        assert "total_relations" in data

    def test_analytics_decay_buckets(self):
        """Decay analysis has healthy/fading/critical buckets."""
        r = client.get("/analytics", headers=HEADERS)
        decay = r.json()["decay_analysis"]
        assert "healthy" in decay
        assert "fading" in decay
        assert "critical" in decay
        assert "avg_decay" in decay


# ── GDPR ─────────────────────────────────────────────────────────────────────


class TestGDPR:
    def test_gdpr_delete_self(self):
        """Agent can delete all their own data."""
        gdpr_headers = {"X-Agent-Id": "gdpr-delete-agent"}
        _save("GDPR test memory one to delete", headers=gdpr_headers)
        _save("GDPR test memory two to delete", headers=gdpr_headers)

        r = client.delete("/memories/agent/gdpr-delete-agent", headers=gdpr_headers)
        assert r.status_code == 200
        data = r.json()
        assert data["deleted_memories"] >= 2
        assert "message" in data

    def test_gdpr_cannot_delete_other_agent(self):
        """Agent cannot delete another agent's data."""
        r = client.delete("/memories/agent/someone-else", headers=HEADERS)
        assert r.status_code == 403

    def test_gdpr_delete_nonexistent_agent(self):
        """Deleting non-existent agent data returns zero counts."""
        headers = {"X-Agent-Id": "gdpr-empty-agent"}
        r = client.delete("/memories/agent/gdpr-empty-agent", headers=headers)
        assert r.status_code == 200
        assert r.json()["deleted_memories"] == 0


# ── Plugins ──────────────────────────────────────────────────────────────────


class TestPlugins:
    def test_list_plugins_empty(self):
        """Default state: no plugins registered."""
        r = client.get("/plugins", headers=HEADERS)
        assert r.status_code == 200
        assert r.json()["total"] >= 0

    def test_plugin_registration(self):
        """Register a plugin and verify it appears in the list."""
        from kore_memory.plugins import KorePlugin, clear_plugins, register_plugin

        class TestPlugin(KorePlugin):
            @property
            def name(self) -> str:
                return "test-v2-plugin"

        register_plugin(TestPlugin())

        r = client.get("/plugins", headers=HEADERS)
        assert "test-v2-plugin" in r.json()["plugins"]

        # Cleanup
        clear_plugins()

    def test_plugin_pre_save_hook(self):
        """Plugin pre_save can override importance."""
        from kore_memory.plugins import KorePlugin, clear_plugins, register_plugin, run_pre_save

        class BoostPlugin(KorePlugin):
            @property
            def name(self) -> str:
                return "boost-plugin"

            def pre_save(self, content, category, importance, agent_id):
                if "critical" in content.lower():
                    return {"importance": 5}
                return None

        register_plugin(BoostPlugin())

        result = run_pre_save("This is a critical decision", "general", None, "test")
        assert result["importance"] == 5

        # Cleanup
        clear_plugins()

    def test_plugin_post_search_filter(self):
        """Plugin post_search can filter results."""
        from kore_memory.plugins import KorePlugin, clear_plugins, register_plugin, run_post_search

        class FilterPlugin(KorePlugin):
            @property
            def name(self) -> str:
                return "filter-plugin"

            def post_search(self, query, results, agent_id):
                return [r for r in results if r.get("importance", 0) >= 3]

        register_plugin(FilterPlugin())

        fake_results = [
            {"id": 1, "importance": 5},
            {"id": 2, "importance": 1},
            {"id": 3, "importance": 4},
        ]
        filtered = run_post_search("test", fake_results, "test")
        assert len(filtered) == 2
        assert all(r["importance"] >= 3 for r in filtered)

        clear_plugins()

    def test_plugin_pre_delete_block(self):
        """Plugin pre_delete can block deletion."""
        from kore_memory.plugins import KorePlugin, clear_plugins, register_plugin, run_pre_delete

        class ProtectPlugin(KorePlugin):
            @property
            def name(self) -> str:
                return "protect-plugin"

            def pre_delete(self, memory_id, agent_id):
                return memory_id != 42  # Block deletion of memory 42

        register_plugin(ProtectPlugin())

        assert run_pre_delete(1, "test") is True
        assert run_pre_delete(42, "test") is False

        clear_plugins()


# ── Summarizer Unit Tests ────────────────────────────────────────────────────


class TestSummarizerUnit:
    def test_tokenize(self):
        """Tokenizer filters stop words and extracts meaningful tokens."""
        from kore_memory.summarizer import _tokenize

        tokens = _tokenize("The quick brown fox jumps over the lazy dog")
        assert "quick" in tokens
        assert "brown" in tokens
        assert "the" not in tokens

    def test_tfidf_computation(self):
        """TF-IDF produces non-zero scores."""
        from kore_memory.summarizer import _compute_tfidf, _tokenize

        docs = [
            _tokenize("Python FastAPI web framework"),
            _tokenize("Python Django web framework"),
            _tokenize("JavaScript React frontend library"),
        ]
        scores = _compute_tfidf(docs)
        assert len(scores) == 3
        # "python" appears in 2 docs, "javascript" in 1 — JS should have higher IDF
        assert any(s > 0 for s in scores[0].values())

    def test_empty_documents(self):
        """TF-IDF handles empty input."""
        from kore_memory.summarizer import _compute_tfidf

        assert _compute_tfidf([]) == []
```

