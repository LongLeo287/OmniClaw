# Changelog - llm-lean-log

This project is a monorepo containing multiple packages. For detailed changes, please see the individual package changelogs:

- [`llm-lean-log-core`](./packages/core/CHANGELOG.md)
- [`llm-lean-log-cli`](./packages/cli/CHANGELOG.md)
- [`l-log-vis`](./packages/visualizer/CHANGELOG.md)
- [`l-log-mcp`](./packages/mcp-server/CHANGELOG.md)
- [`l-log-mcp-server`](./packages/mcp-server/CHANGELOG.md)

## v0.2.6 - January 19, 2026

- Enhanced `l-log-mcp-server` with developer convenience features (`--config`, `postinstall` guide)
- Improved building and type management for MCP server package
- Updated release workflows to sync GitHub Release notes with package changelogs

## v0.2.5 - January 18, 2026

- Fixed CLI build configuration to resolve __require errors
- Updated build process to use external dependencies
- Fixed package.json import issues in bundled CLI

## v0.2.4 - January 18, 2026

- Updated changelog documentation
- Minor documentation improvements
- Added cause field support across all packages

## v0.2.1 - January 14, 2026

- Version bump across all packages to 0.2.1
- Updated dependency versions for consistency
- Minor improvements and bug fixes

## Summary of Major Milestones

### Jan 14, 2026

- Core library and CLI tool reached stable 0.1.7/0.1.8 versions.
- Improved test coverage and fixed critical CSV parsing edge cases.
- Standardized project-wide field names and structures.

### Jan 13, 2026

- Major feature additions: Cause & Effect tracking, `tech-stack` tags, and `created-by-agent` metadata.
- CLI renamed to `l-log` and Visualizer renamed to `l-log-vis`.
- Enhanced CSV parser to handle multi-line fields (e.g., long code blocks or problems).

### Jan 12, 2026

- Initial public release of all core components.
- Launched the Web Visualizer for beautiful, interactive log browsing.
- Transitioned to Bun-native monorepo architecture.
- Added Terminal syntax highlighting for the CLI.
