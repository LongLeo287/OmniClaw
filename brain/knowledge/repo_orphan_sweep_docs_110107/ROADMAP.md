# Roadmap

## Shipped

### v1.7.0
- `install` command as primary entry point (`init` kept as alias)
- `--dry-run` flag for previewing install/init changes
- Automatic PyPI publishing via GitHub Actions on release
- README rewrite with real benchmark data from httpx, FastAPI, and Next.js

### v1.6.4
- Portable `uvx`-based MCP config — no absolute paths, works on any machine with `uv`
- Removed `_safe_path` symlink workaround (superseded by `uvx`)

### v1.6.3
- SessionStart hook: Claude Code prefers graph tools over full codebase scans automatically
- plugin.json corrected for official marketplace submission
- README cleanup

### v1.6.2
- 24 audit fixes: critical bugs, performance, parser, tests, CI, docs, accessibility
- C/C++ parser support with full node extraction
- Name extraction fixes for Kotlin, Swift, Ruby
- NetworkX caching, batch queries, subprocess timeouts, chunked search
- CI: coverage enforcement, bandit, mypy
- 40+ new tests, 7 language fixtures

### v1.5.3
- `init` auto-handles spaces in paths (macOS iCloud, OneDrive, etc.)
- Works without git — `build`, `status`, `visualize`, `watch` fall back to cwd
- Skills registered in plugin.json for Claude Code plugin discovery

### v1.5.0
- Generated files organized into `.code-review-graph/` directory (auto-gitignored, legacy migration)
- Visualization density: collapsed start, search, edge toggles, scale-aware layout
- Project cleanup: removed redundant files and directories

### v1.4.0
- `init` command for automatic `.mcp.json` setup
- Interactive D3.js graph visualization (`visualize` command)
- `serve` command to start MCP server directly
- Comprehensive documentation overhaul

### v1.3.0
- Python version check with Docker fallback
- Universal install via `pip install code-review-graph`
- CLI entry point (`code-review-graph` command)

### v1.2.0
- Logging improvements and watch debounce
- tools.py fixes and CI coverage via GitHub Actions

### v1.1.0
- Watch mode, vector embeddings, 12+ languages verified

## v2.0 (Planned)
- Surgical edit suggestions (auto-fix common patterns)
- GitHub PR bot integration
- Team sync (shared graph via git-tracked DB)
- Memgraph/Cypher support for large-scale graphs

## Ongoing
- Additional language grammars as requested
- Performance optimization for monorepos (>50k files)
- Integration with more Claude Code features as the platform evolves
