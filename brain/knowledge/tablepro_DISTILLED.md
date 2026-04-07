---
id: tablepro
type: knowledge
owner: OA_Triage
---
# tablepro
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<p align="center">
  <img src=".github/assets/logo.png" width="128" height="128" alt="TablePro">
</p>

<h1 align="center">TablePro</h1>

<p align="center">
  A fast, native macOS database client with built-in AI assistant.
</p>

<p align="center">
  <a href="https://docs.tablepro.app">Documentation</a> ·
  <a href="https://github.com/TableProApp/TablePro/releases">Download</a> ·
  <a href="https://github.com/TableProApp/TablePro/issues">Report Bug</a>
</p>

<p align="center">
  <a href="https://www.gnu.org/licenses/agpl-3.0"><img src="https://img.shields.io/badge/License-AGPL_v3-blue.svg" alt="License: AGPL v3"></a>
</p>

<p align="center">
  <a href="README.vi.md">Tiếng Việt</a>
</p>

---

<p align="center">
  <img src=".github/assets/hero-dark.png" alt="TablePro Screenshot" width="800">
</p>

## About

TablePro is a native macOS database client. Connects to MySQL, MariaDB, PostgreSQL, SQLite, MongoDB, Redis, SQL Server, and Redshift. Includes a SQL editor with autocomplete, inline editing, and AI assistance.

## Install

```bash
brew install --cask tablepro
```

Or download the DMG from [GitHub Releases](https://github.com/TableProApp/TablePro/releases).

## Documentation

Full documentation is available at [docs.tablepro.app](https://docs.tablepro.app).

## Support Development

TablePro is free and open source. If you find it useful, consider [purchasing a license](https://tablepro.app) to support ongoing development and get access to premium features.

## Sponsors

Thanks to these amazing people for supporting TablePro:

**[Dwarves Foundation](https://dwarves.foundation/?ref=tablepro)** · **[Nimbus](https://getnimbus.io?ref=tablepro)** · **[Visnalize](https://visnalize.com?ref=tablepro)** · **[Huy TQ](https://github.com/imhuytq)** · **[Unikorn](https://unikorn.vn?ref=tablepro)**

## Star History

<a href="https://www.star-history.com/?repos=TableProApp%2FTablePro&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=TableProApp/TablePro&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=TableProApp/TablePro&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/image?repos=TableProApp/TablePro&type=date&legend=top-left" />
 </picture>
</a>

## License

This project is licensed under the [GNU Affero General Public License v3.0 (AGPLv3)](LICENSE).

Contributions require signing a Contributor License Agreement (CLA). See [CLA.md](CLA.md) for details.

```

### File: docs\README.md
```md
# TablePro Documentation

Source files for the [TablePro documentation site](https://docs.tablepro.app), powered by [Mintlify](https://mintlify.com).

## Structure

```
docs/
├── index.mdx                # Introduction
├── quickstart.mdx           # Getting started guide
├── installation.mdx         # Installation instructions
├── changelog.mdx            # Release changelog
├── databases/               # Database connection guides
├── features/                # Feature documentation
├── customization/           # Settings and customization
├── development/             # Developer documentation
└── vi/                      # Vietnamese translation (full parity)
```

## Local Development

Install the [Mintlify CLI](https://www.npmjs.com/package/mint) and start the dev server:

```bash
npm i -g mint
mint dev
```

Preview at `http://localhost:3000`.

## Deployment

Changes pushed to the default branch are deployed automatically via the [Mintlify GitHub app](https://dashboard.mintlify.com/settings/organization/github-app).

```

### File: CHANGELOG.md
```md
# Changelog

All notable changes to TablePro will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.27.3] - 2026-04-03

### Added

- Structure tab context menu with Copy Name, Copy Definition (SQL), Duplicate, and Delete for columns, indexes, and foreign keys
- Foreign key preview: press Cmd+Enter on a FK cell to see the referenced row in a popover
- Column header: sort ascending/descending and show all hidden columns in context menu
- Data grid: preview and navigate FK references from right-click context menu
- Data grid: add row from right-click on empty space

### Fixed

- Oracle: crash when opening views caused by OracleNIO state-machine corruption from concurrent queries, LONG column types, and DBMS_METADATA errors

## [0.27.2] - 2026-04-02

### Added

- Option to group all connection tabs in one window instead of separate windows per connection

### Changed

- Separate preferred themes for Light and Dark appearance modes, with automatic switching in Auto mode

## [0.27.1] - 2026-04-01

### Fixed

- Table queries incorrectly prefixed with connection username as schema name on non-schema databases (MySQL, MariaDB, ClickHouse, Redis, etc.), causing "Table 'username.table' doesn't exist" errors when opening a second table tab

## [0.27.0] - 2026-03-31

### Added

- Option to prompt for database password on every connection instead of saving to Keychain
- Autocompletion for filter fields: column names and SQL keywords suggested as you type (Raw SQL and Value fields)
- Multi-line support for Raw SQL filter field (Option+Enter for newline)
- Visual Create Table UI with multi-database support (sidebar → "Create New Table...")
- Auto-fit column width: double-click column divider or right-click → "Size to Fit"
- Collapsible results panel (`Cmd+Opt+R`), multiple result tabs for multi-statement queries, result pinning
- Inline error banner for query errors
- JSON syntax highlighting and brace matching in Details sidebar and JSON editor popover
- Database-aware SQL functions in field menu (MySQL, PostgreSQL, SQLite, SQL Server, ClickHouse)

### Changed

- Replace GCD dispatch patterns with Swift structured concurrency
- Refactor Details sidebar into modular field editor architecture with extracted editor components

### Fixed

- PostgreSQL: Schema name lost after app restart, causing "relation does not exist" errors for non-public schemas
- Error dialog OK button not dismissing when a SwiftUI sheet is active, making the app unusable
- SQL Server: Unicode characters (Thai, CJK, etc.) in nvarchar/nchar/ntext columns displaying as question marks
- Globe+F (fn+F) fullscreen shortcut not working in SwiftUI lifecycle app

## [0.26.0] - 2026-03-29

### Added

- Global toggle to disable all AI features (Settings > AI)
- Drag to reorder columns in the Structure tab (MySQL/MariaDB)
- Nested hierarchical groups for connection list (up to 3 levels deep)
- Confirmation dialogs for deep link queries, connection imports, and pre-connect scripts
- JSON fields in Row Details sidebar now display in a scrollable monospaced text area
- Open, save, and save-as for SQL files with native macOS title bar integration (#475)
- BigQuery plugin support (Google BigQuery analytics via REST API)

### Changed

- Removed query history sync from iCloud Sync (connections, groups, settings, and SSH profiles still sync)

### Fixed

- SQL editor not auto-focused on new tab and cursor missing after tab switch
- Long lines not scrollable horizontally in the SQL editor
- Home and End keys not moving cursor in the SQL editor (#448)
- SSH profile lost after app restart when iCloud Sync enabled
- MariaDB JSON columns showing as hex dumps instead of JSON text
- MongoDB Atlas TLS certificate verification failure
- ENUM/SET dropdown chevron buttons not showing on first table open

## [0.25.0] - 2026-03-27

### Added

- Connection sharing: export/import connections as `.tablepro` files with import preview and duplicate detection (#466)
- Encrypted export with credentials, protected by AES-256-GCM passphrase (Pro)
- Linked Folders: watch a shared directory for `.tablepro` files (Pro)
- Environment variable references (`$VAR`, `${VAR}`) in connection fields (Pro)

## [0.24.2] - 2026-03-26

### Fixed

- XLSX export producing corrupted files that Excel cannot open (#464)
- Deep link cold launch missing toolbar and duplicate windows (#465)

### Added

- Enum/set picker support for PostgreSQL custom enums, ClickHouse Enum8/Enum16, and DuckDB ENUM types
- Boolean picker for MSSQL BIT columns and MySQL TINYINT(1) convention
- Correct type classification for ClickHouse Nullable()/LowCardinality() wrappers, MSSQL MONEY/IMAGE/DATETIME2, DuckDB unsigned integers, and parameterized MySQL integer types

## [0.24.1] - 2026-03-26

### Fixed

- Keyboard shortcut hints in welcome window footer overflowing and truncating when too many items are displayed

## [0.24.0] - 2026-03-26

### Added

- Multi-select connections in Welcome window (Cmd+Click, Shift+Click) with bulk delete (⌘⌫), Move to Group, and multi-connect
- Reorder connections within groups and reorder groups in Welcome window
- ClickHouse, MSSQL, Redis, XLSX Export, MQL Export, and SQL Import now ship as built-in plugins
- Large document safety caps for syntax highlighting (skip >5MB, throttle >50KB)
- Lazy-load full values for LONGTEXT/MEDIUMTEXT/CLOB columns in the detail pane sidebar

### Fixed

- SSH profile connections displaying incorrect host/username on the Welcome window home screen (#454)
- Saved connections disappearing after normal app quit (Cmd+Q) while persisting after force quit (#452)
- Crash when disconnecting an etcd connection while requests are in-flight
- Detail pane showing truncated values for LONGTEXT/MEDIUMTEXT/CLOB columns, preventing correct editing
- Redis hash/list/set/zset/stream views showing empty or misaligned rows when values contained binary, null, or integer types

## [0.23.2] - 2026-03-24

### Fixed

- MongoDB Atlas connections failing to authenticate (#438)
- MongoDB TLS certificate verification skipped for SRV connections
- Active tab data no longer refreshes when switching back to the app window
- Undo history preserved when switching between database tables
- Health monitor now detects stuck queries beyond the configured timeout
- SSH tunnel closure errors now logged instead of silently discarded
- Schema/database restore errors during reconnect now logged
- Memory not released after closing tabs
- New tabs opening as separate windows instead of joining the connection tab group
- Clicking tables in sidebar not opening table tabs

## [0.23.1] - 2026-03-24

### Added

- Test Connection button in SSH profile editor to validate SSH connectivity independently

### Changed

- Improve performance: faster sorting, lower memory usage, adaptive tab eviction

## [0.23.0] - 2026-03-22

### Added

- Redis key namespace tree view with collapse/expand grouping in sidebar (#418)
- Keyboard focus navigation (Tab, Ctrl+J/K/N/P, arrow keys) for connection list, quick switcher, and database switcher
- MongoDB `mongodb+srv://` URI support with SRV toggle, Auth Mechanism dropdown, and Replica Set field (#419)
- Show all available database types in connection form with install status badge (#418)

### Changed

- MongoDB `authSource` defaults to database name per MongoDB URI spec instead of always "admin"

### Fixed

- DuckDB: TIMESTAMPTZ, TIMETZ, and other temporal columns displaying as null (#424)
- Onboarding "Get Started" button not rendering on macOS 15 until window loses focus (#420)
- MongoDB collection loading uses `estimatedDocumentCount` and smaller schema sample for faster sidebar population

## [0.22.1] - 2026-03-22

### Added

- Show/hide row numbers column in data grid (Settings > Data Grid)
- Persist column widths and order per table across tab switches, view toggles, and app restarts

### Fixed

- Show correct version for installed registry plugins (#410)
- Dangling pointer in release builds due to incorrect withUnsafeBufferPointer usage
- AI provider connection test error handling (#407)
- Use-after-free crash in Redis plugin redisFree

## [0.22.0] - 2026-03-21

### Added

- Export query results directly to CSV, JSON, SQL, XLSX, or MQL via File menu, context menu, or toolbar
- Pro license gating for Safe Mode (Touch ID) and XLSX export
- License activation dialog

- Reusable SSH tunnel profiles: save SSH configurations once and select them across multiple connections
- Ctrl+HJKL navigation as arrow key alternative for keyboards without dedicated arrow keys
- Amazon DynamoDB database support with PartiQL queries, AWS IAM/Profile/SSO authentication, GSI/LSI browsing, table scanning, capacity display, and DynamoDB Local support

### Fixed

- High CPU usage (79%+) and energy consumption when idle (#394)
- etcd connection failing with 404 when gRPC gateway uses a different API prefix (auto-detects `/v3/`, `/v3beta/`, `/v3alpha/`)
- Data grid editing (delete rows, modify cells, add rows) not working in query tabs (#383)

## [0.21.0] - 2026-03-19

### Added

- Cloudflare D1 database support
- Match highlighting in autocomplete suggestions (matched characters shown in bold)
- Loading spinner in autocomplete popup while fetching column metadata

### Changed

- Refactored autocomplete popup to native SwiftUI (visible selection highlight, native accent color, scroll-to-selection)
- Autocomplete now suppresses noisy empty-prefix suggestions in non-browseable contexts (e.g., after SELECT, WHERE)
- Autocomplete ranking stays consistent as you type (unified fuzzy scoring between initial display and live filtering)
- Increased autocomplete suggestion limit from 20 to 40 for schema-heavy contexts (FROM, SELECT, WHERE)

## [0.20.4] - 2026-03-19

### Fixed

- SQL syntax error when editing columns with reserved keyword names (e.g., `database`, `table`, `order`) in MySQL/PostgreSQL/SQLite
- High CPU usage and memory leaks at idle
- N+1 query performance in foreign key fetching with bulk queries
- Architecture-specific update delivery using `sparkle:hardwareRequirements`

### Changed

- Improved performance for medium and low severity bottlenecks (query history, tab persistence, sidebar rendering)

## [0.20.3] - 2026-03-18

### Added

- Optional iCloud Keychain sync for connection passwords

### Fixed

- `Use ~/.pgpass` setting not persisting when saving a PostgreSQL connection

## [0.20.2] - 2026-03-18

### Fixed

- Safe mode badge not displaying for silent level
- Safe mode level reading from immutable connection state instead of live toolbar state
- `~/.pgpass` password lookup using SSH tunnel host instead of original host when connecting through SSH

## [0.20.1] - 2026-03-17

### Fixed

- Plugin registry compatibility with PluginKit version 2

## [0.20.0] - 2026-03-17

### Added

- Turkish language in Settings > General (Türkçe) with Turkish translations for UI strings
- etcd v3 plugin with prefix-tree key browsing, etcdctl syntax editor, lease management, watch, mTLS, auth, and cluster info
- Save Changes button in toolbar for committing pending data edits
- Confirmation dialog before deleting a connection
- Confirmation dialog before sort, pagination, filter, or search discards unsaved edits

### Fixed

- SSH tunnel crashes caused by concurrent libssh2 calls on the same session
- Unsaved cell edits lost when switching tabs, sorting, paginating, filtering, or switching apps
- Auto-reconnect and health monitor silently discarding unsaved changes
- SSH tunnel recovery failing after tunnel death due to stale driver state
- Health monitor ping interfering with active user queries
- Connection test not cleaning up SSH tunnel on completion
- Test connection success indicator not resetting after field changes
- SSH port field accepting invalid values
- DROP TABLE and TRUNCATE TABLE sidebar operations producing no SQL for plugin-based drivers
- Foreign key navigation arrows not appearing after switching databases with Cmd+K on MySQL
- Sidebar not refreshing after creating or dropping tables
- Dropping a table disconnecting the database when the dropped table's tab was active

## [0.19.1] - 2026-03-16

### Fixed

- SSH tunnel connections timing out due to relay deadlock
- Plugin metadata dispatch failing for externally installed plugins
- SSH public key authentication error messages now include detailed failure reason

## [0.19.0] - 2026-03-15

### Added

- iCloud Sync (Pro): sync connections, groups, tags, settings, and query history across Macs with per-category toggles, conflict resolution, and real-time status indicator
- SQL Favorites: save frequently used queries with optional keyword bindings for autocomplete expansion
- Copy selected rows as JSON from context menu and Edit menu
- Help menu and welcome screen links to website, documentation, GitHub, and sponsor page
- Display BLOB data as hex dump in detail view sidebar

### Fixed

- SSH agent connections failing when socket path contains `~` (e.g., 1Password agent)
- Keychain authorization prompt no longer appears on every table open

## [0.18.1] - 2026-03-14

### Fixed

- Plugin download counts now accumulate across all versions instead of only counting the current release

## [0.18.0] - 2026-03-14

### Added

- Theme engine: 4 built-in themes (Default Light/Dark, Dracula, Nord), custom themes with full color/font/layout customization, import/export as JSON
- Theme registry: browse, install, and update community themes from the plugin registry
- App-level appearance mode: Light, Dark, or Auto (follow system), independent of theme
- Cassandra and ScyllaDB database support (downloadable plugin)
- SSH TOTP/two-factor authentication with auto-generate and prompt modes
- SSH host key verification with fingerprint confirmation
- Keyboard Interactive SSH authentication
- Column visibility: toggle columns on/off via status bar or header context menu
- Copy as INSERT/UPDATE SQL from data grid context menu
- `~/.pgpass` support for PostgreSQL/Redshift connections
- Pre-connect script: run a shell command before each connection
- MSSQL query cancellation and lock timeout support
- Custom plugin registry URL for enterprise/private registries

### Changed

- Extracted MSSQL, MongoDB, Redis, XLSX export, MQL export, and SQL import into downloadable plugins. MySQL, PostgreSQL, SQLite, CSV, JSON, and SQL export remain built-in
- Redesigned Plugins settings with master-detail layout and download counts
- All database-specific behavior now driven by plugin metadata instead of hardcoded switches, enabling third-party database plugins
- Connection form fields, sidebar labels, and SQL dialect features are now fully plugin-driven

### Fixed

- Plugin icon rendering now supports custom asset images alongside SF Symbols

## [0.17.0] - 2026-03-11

### Added

- DuckDB database support — connect to `.duckdb` files
... [TRUNCATED]
```

### File: CLA.md
```md
# Contributor License Agreement

By submitting a contribution (pull request, patch, or other modification) to
this project, you agree to the following terms:

## 1. Grant of Rights

You grant Ngo Quoc Dat (the "Maintainer") a perpetual, worldwide,
non-exclusive, royalty-free, irrevocable license to use, reproduce, modify,
display, perform, sublicense, and distribute your contribution as part of
TablePro under any license terms the Maintainer chooses, including proprietary
licenses.

## 2. Why This Is Needed

TablePro is licensed under AGPLv3 for the open-source community. However, the
Maintainer offers premium features under a separate commercial license. This CLA
allows the Maintainer to:

- Distribute TablePro with premium features under commercial terms
- Relicense contributions if needed (e.g., linking with non-AGPL dependencies)

Without this CLA, every contributor would need to individually approve any
licensing change, making commercial licensing impractical.

## 3. Your Representations

You represent that:

- You are the original author of the contribution, or have the right to submit
  it.
- Your contribution does not violate any third-party rights (patents,
  copyrights, trade secrets, etc.).
- You are not aware of any claims or litigation regarding the contribution.

## 4. No Obligation

This CLA does not obligate the Maintainer to use, merge, or distribute your
contribution.

## 5. Agreement

By opening a pull request, you indicate your agreement to these terms. First-time
contributors will be asked to explicitly confirm via the CLA Assistant bot.

```

### File: CLAUDE.md
```md
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

TablePro is a native macOS database client (SwiftUI + AppKit) — a fast, lightweight alternative to TablePlus. macOS 14.0+, Swift 5.9, Universal Binary (arm64 + x86_64).

- **Source**: `TablePro/` — `Core/` (business logic, services), `Views/` (UI), `Models/` (data structures), `ViewModels/`, `Extensions/`, `Theme/`
- **Plugins**: `Plugins/` — `.tableplugin` bundles + `TableProPluginKit` shared framework. Built-in (bundled in app): MySQL, PostgreSQL, SQLite, ClickHouse, MSSQL, Redis, CSV, JSON, SQL export, XLSX, MQL, SQLImport. Separately distributed via plugin registry: MongoDB, Oracle, DuckDB, Cassandra, Etcd, CloudflareD1, DynamoDB, BigQuery
- **C bridges**: Each plugin contains its own C bridge module (e.g., `Plugins/MySQLDriverPlugin/CMariaDB/`, `Plugins/PostgreSQLDriverPlugin/CLibPQ/`)
- **Static libs**: `Libs/` — pre-built `libmariadb*.a`, `libpq*.a`, etc. Downloaded from GitHub Releases via `scripts/download-libs.sh` (not in git)
- **SPM deps**: CodeEditSourceEditor (`main` branch, tree-sitter editor), Sparkle (2.8.1, auto-update), OracleNIO. Managed via Xcode, no `Package.swift`.

## Build & Development Commands

```bash
# Build (development) — -skipPackagePluginValidation required for SwiftLint plugin in CodeEditSourceEditor
xcodebuild -project TablePro.xcodeproj -scheme TablePro -configuration Debug build -skipPackagePluginValidation

# Clean build
xcodebuild -project TablePro.xcodeproj -scheme TablePro clean

# Build and run
xcodebuild -project TablePro.xcodeproj -scheme TablePro -configuration Debug build -skipPackagePluginValidation && open build/Debug/TablePro.app

# Release builds
scripts/build-release.sh arm64|x86_64|both

# Lint & format
swiftlint lint                    # Check issues
swiftlint --fix                   # Auto-fix
swiftformat .                     # Format code

# Tests
xcodebuild -project TablePro.xcodeproj -scheme TablePro test -skipPackagePluginValidation
xcodebuild -project TablePro.xcodeproj -scheme TablePro test -skipPackagePluginValidation -only-testing:TableProTests/TestClassName
xcodebuild -project TablePro.xcodeproj -scheme TablePro test -skipPackagePluginValidation -only-testing:TableProTests/TestClassName/testMethodName

# DMG
scripts/create-dmg.sh

# Static libraries (first-time setup or after lib updates)
scripts/download-libs.sh          # Download from GitHub Releases (skips if already present)
scripts/download-libs.sh --force  # Re-download and overwrite
```

### Updating Static Libraries

Static libs (`Libs/*.a`) are hosted on the `libs-v1` GitHub Release (not in git). When adding or updating a library:

```bash
# 1. Update the .a files in Libs/
# 2. Regenerate checksums
shasum -a 256 Libs/*.a > Libs/checksums.sha256
# 3. Recreate and upload the archive
tar czf /tmp/tablepro-libs-v1.tar.gz -C Libs .
gh release upload libs-v1 /tmp/tablepro-libs-v1.tar.gz --clobber --repo TableProApp/TablePro
# 4. Commit the updated checksums
git add Libs/checksums.sha256 && git commit -m "build: update static library checksums"
```

## Architecture

### Plugin System

All database drivers are `.tableplugin` bundles loaded at runtime by `PluginManager` (`Core/Plugins/`):

- **TableProPluginKit** (`Plugins/TableProPluginKit/`) — shared framework with `PluginDatabaseDriver`, `DriverPlugin`, `TableProPlugin` protocols and transfer types (`PluginQueryResult`, `PluginColumnInfo`, etc.)
- **PluginDriverAdapter** (`Core/Plugins/PluginDriverAdapter.swift`) — bridges `PluginDatabaseDriver` → `DatabaseDriver` protocol
- **DatabaseDriverFactory** (`Core/Database/DatabaseDriver.swift`) — looks up plugins via `DatabaseType.pluginTypeId`
- **DatabaseManager** (`Core/Database/DatabaseManager.swift`) — connection pool, lifecycle, primary interface for views/coordinators
- **ConnectionHealthMonitor** — 30s ping, auto-reconnect with exponential backoff

Plugin bundles under `Plugins/`:

| Plugin                 | Database Types       | C Bridge             | Distribution |
| ---------------------- | -------------------- | -------------------- | ------------ |
| MySQLDriverPlugin      | MySQL, MariaDB       | CMariaDB             | Built-in     |
| PostgreSQLDriverPlugin | PostgreSQL, Redshift | CLibPQ               | Built-in     |
| SQLiteDriverPlugin     | SQLite               | (Foundation sqlite3) | Built-in     |
| ClickHouseDriverPlugin | ClickHouse           | (URLSession HTTP)    | Built-in     |
| MSSQLDriverPlugin      | SQL Server           | CFreeTDS             | Built-in     |
| RedisDriverPlugin      | Redis                | CRedis               | Built-in     |
| MongoDBDriverPlugin    | MongoDB              | CLibMongoc           | Registry     |
| DuckDBDriverPlugin     | DuckDB               | CDuckDB              | Registry     |
| OracleDriverPlugin     | Oracle               | OracleNIO (SPM)      | Registry     |
| CassandraDriverPlugin  | Cassandra, ScyllaDB  | CCassandra           | Registry     |
| EtcdDriverPlugin       | Etcd                 | (gRPC/HTTP)          | Registry     |
| CloudflareD1Plugin     | Cloudflare D1        | (URLSession HTTP)    | Registry     |
| DynamoDBDriverPlugin   | DynamoDB             | (AWS SDK)            | Registry     |
| BigQueryDriverPlugin   | BigQuery             | (URLSession REST)    | Registry     |

When adding a new driver: create a new plugin bundle under `Plugins/`, implement `DriverPlugin` + `PluginDatabaseDriver`, add target to pbxproj, add `DatabaseType` static constant, add case to `resolve_plugin_info()` in `.github/workflows/build-plugin.yml`, add row to `docs/index.mdx` supported databases table, and add CHANGELOG entry. See `docs/development/plugin-system/` for details.

When adding a new method to the driver protocol: add to `PluginDatabaseDriver` (with default implementation), then update `PluginDriverAdapter` to bridge it to `DatabaseDriver`.

**PluginKit ABI versioning**: When `DriverPlugin` or `PluginDatabaseDriver` protocol changes (new methods, changed signatures), bump `currentPluginKitVersion` in `PluginManager.swift` AND `TableProPluginKitVersion` in every plugin's `Info.plist`. Stale user-installed plugins with mismatched versions crash on load with `EXC_BAD_INSTRUCTION` (not catchable in Swift). Removing protocol methods that have default `nil` implementations does NOT require a version bump — old plugins have dead code, new plugins fall back to defaults.

### DatabaseType (String-Based Struct)

`DatabaseType` is a string-based struct (not an enum). Key rules:
- All `switch` statements on `DatabaseType` must include `default:` — the type is open
- Use static constants (`.mysql`, `.postgresql`) for known types
- Unknown types (from future plugins) are valid — they round-trip through Codable
- Use `DatabaseType.allKnownTypes` (not `allCases`) for the canonical list of built-in types

### Editor Architecture (CodeEditSourceEditor)

- **`SQLEditorTheme`** — single source of truth for editor colors/fonts
- **`TableProEditorTheme`** — adapter to CodeEdit's `EditorTheme` protocol
- **`CompletionEngine`** — framework-agnostic; **`SQLCompletionAdapter`** bridges to CodeEdit's `CodeSuggestionDelegate`
- **`EditorTabBar`** — pure SwiftUI tab bar
- Cursor model: `cursorPositions: [CursorPosition]` (multi-cursor via CodeEditSourceEditor)

### Change Tracking Flow

1. User edits cell → `DataChangeManager` records change
2. User clicks Save → `SQLStatementGenerator` produces INSERT/UPDATE/DELETE
3. `DataChangeUndoManager` provides undo/redo
4. `AnyChangeManager` abstracts over concrete manager for protocol-based usage

### Main Coordinator Pattern

`MainContentCoordinator` is the central coordinator, split across 7+ extension files in `Views/Main/Extensions/` (e.g., `+Alerts`, `+Filtering`, `+Pagination`, `+RowOperations`). When adding coordinator functionality, add a new extension file rather than growing the main file.

**Tab replacement guard**: `openTableTab` checks for active work (unsaved edits, applied filters, sorting) before replacing the current tab. Tabs with active work open a new native window tab instead. This check runs before the preview tab branch.

### Source Organization

`Core/Services/` is split into domain subdirectories:

| Subdirectory      | Contents                                                               |
| ----------------- | ---------------------------------------------------------------------- |
| `Export/`         | ExportService, ImportService, XLSXWriter                               |
| `Formatting/`     | SQLFormatterService, DateFormattingService                             |
| `Infrastructure/` | AppNotifications, DeeplinkHandler, WindowOpener, UpdaterBridge, etc.   |
| `Licensing/`      | LicenseManager, LicenseAPIClient, LicenseSignatureVerifier             |
| `Query/`          | SQLDialectProvider, TableQueryBuilder, RowParser, RowOperationsManager |

`Models/` is split into: `AI/`, `Connection/`, `Database/`, `Export/`, `Query/`, `Settings/`, `UI/`, `Schema/`, `ClickHouse/`

`Core/Utilities/` is split into: `Connection/`, `SQL/`, `File/`, `UI/`

`Core/QuerySupport/` contains MongoDB and Redis query builders/statement generators (non-driver query logic).

### Storage Patterns

| What                 | How              | Where                                       |
| -------------------- | ---------------- | ------------------------------------------- |
| Connection passwords | Keychain         | `ConnectionStorage`                         |
| User preferences     | UserDefaults     | `AppSettingsStorage` / `AppSettingsManager` |
| Query history        | SQLite FTS5      | `QueryHistoryStorage`                       |
| Tab state            | JSON persistence | `TabPersistenceService` / `TabStateStorage` |
| Filter presets       | UserDefaults     | `FilterSettingsStorage`                     |
| Per-table filters    | UserDefaults     | `FilterSettingsStorage` (saves `appliedFilters` only) |

### Logging

Use OSLog, never `print()`:

```swift
import os
private static let logger = Logger(subsystem: "com.TablePro", category: "ComponentName")
```

## Code Style

**Authoritative sources**: `.swiftlint.yml` and `.swiftformat` — check those files for the full rule set. Key points that aren't obvious from config:

- **4 spaces** indentation (never tabs except Makefile/pbxproj)
- **120 char** target line length (SwiftFormat); SwiftLint warns at 180, errors at 300
- **K&R braces**, LF line endings, no semicolons, no trailing commas
- **Imports**: system frameworks alphabetically → third-party → local, blank line after imports
- **Access control**: always explicit (`private`, `internal`, `public`). Specify on extension, not individual members.
- **No force unwrapping/casting** — use `guard let`, `if let`, `as?`
- **Acronyms as words**: `JsonEncoder` not `JSONEncoder` (except SDK types)
- **No unnecessary comments**: Don't add comments that restate what the code already says. Only comment to explain non-obvious "why" reasoning or clarify genuinely complex logic.
- **Extension access modifiers on the extension itself**:
    ```swift
    // Good
    public extension NSEvent {
        var semanticKeyCode: KeyCode? { ... }
    }
    ```

### SwiftLint Limits

| Metric                | Warning | Error |
| --------------------- | ------- | ----- |
| File length           | 1200    | 1800  |
| Type body             | 1100    | 1500  |
| Function body         | 160     | 250   |
| Cyclomatic complexity | 40      | 60    |

When approaching limits: extract into `TypeName+Category.swift` extension files in an `Extensions/` subfolder. Group by domain logic, not arbitrary line counts.

## Mandatory Rules

These are **non-negotiable** — never skip them:

1. **CHANGELOG.md**: Update under `[Unreleased]` section (Added/Fixed/Changed) for new features and notable changes. But do **not** add a "Fixed" entry for fixing something that is itself still unreleased — if a feature under `[Unreleased]` has a bug, just fix it without adding another CHANGELOG entry. "Fixed" entries are only for bugs in already-released features. Documentation-only changes (`docs/`) do **not** need a CHANGELOG entry.

2. **Localization**: Use `String(localized:)` for new user-facing strings in computed properties, AppKit code, alerts, and error descriptions. SwiftUI view literals (`Text("literal")`, `Button("literal")`) auto-localize. Do NOT localize technical terms (font names, database types, SQL keywords, encoding names). Never use `String(localized:)` with string interpolation — `String(localized: "Preview \(name)")` creates a dynamic key that never matches the strings catalog. Use static keys or `String(format: String(localized: "Preview %@"), name)`.

3. **Documentation**: Update docs in `docs/` (Mintlify-based) when adding/changing features. Key mappings:
    - New keyboard shortcuts → `docs/features/keyboard-shortcuts.mdx`
    - UI/feature changes → relevant `docs/features/*.mdx` page
    - Settings changes → `docs/customization/settings.mdx`
    - Database driver changes → `docs/databases/*.mdx`
    - Update English docs in `docs/` (no Vietnamese `docs/vi/` directory currently exists)

4. **Test-first correctness**: When tests fail, fix the **source code** — never adjust tests to match incorrect output. Tests define expected behavior.

5. **Lint after changes**: Run `swiftlint lint --strict` to verify compliance.

6. **Commit messages**: Follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/). Single line only, no description body. Examples: `docs: fix installation instructions for unsigned app`, `fix: prevent crash on empty query result`, `feat: add CSV export`.

## Agent Execution Strategy

- **Plans must include edge cases.** When creating implementation plans, identify edge cases, thread safety concerns, and boundary conditions. Include them as explicit checklist items in the plan — don't defer discovery to code review.
- **Implementation includes self-review.** Before committing, agents must check: thread safety (lock coverage, race conditions), all code paths (loops, early returns, between iterations), error handling, and flag/state reset logic. This eliminates the review→fix→review cycle.
- **Tests are part of implementation, not a separate step.** When implementing a feature, write tests in the same commit or immediately after — don't wait for a separate `/write-tests` invocation. The implementation agent should include test writing in its scope.
- **Always use team agents** for implementation work. Use the Agent tool (not subagents/tasks) to delegate coding to specialized agents (e.g., `feature-dev:feature-dev`, `feature-dev:code-architect`, `code-simplifier:code-simplifier`).
- **Always parallelize** independent tasks. Launch multiple agents in a single message.
- **Main context = orchestrator only.** Read files, launch agents, summarize results, update
... [TRUNCATED]
```

### File: CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
datlechin@gmail.com.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.

```

### File: CONTRIBUTING.md
```md
# Contributing

## Setup

You'll need macOS 14.0+, Xcode 15+, and [Git LFS](https://git-lfs.github.com/) (static libs in `Libs/` are LFS-tracked). Install [SwiftLint](https://github.com/realm/SwiftLint) and [SwiftFormat](https://github.com/nicklockwood/SwiftFormat) too.

```bash
git clone https://github.com/<your-username>/TablePro.git
cd TablePro
git lfs pull
```

Build with the `-skipPackagePluginValidation` flag (needed for the SwiftLint plugin in CodeEditSourceEditor):

```bash
xcodebuild -project TablePro.xcodeproj -scheme TablePro -configuration Debug build -skipPackagePluginValidation
```

Run tests:

```bash
xcodebuild -project TablePro.xcodeproj -scheme TablePro test -skipPackagePluginValidation
```

## Code Style

`.swiftlint.yml` and `.swiftformat` are the source of truth. The short version:

- 4-space indentation, 120-char line length target
- Explicit access control (`private`, `internal`, `public`)
- No force unwraps or force casts. Use `guard let`, `if let`, `as?`
- `String(localized:)` for user-facing strings. SwiftUI view literals auto-localize
- OSLog only, no `print()`

Run both before committing:

```bash
swiftlint lint --strict
swiftformat .
```

## Commits

[Conventional Commits](https://www.conventionalcommits.org/), single line, no body.

```
feat: add CSV export for query results
fix: prevent crash on empty query result
docs: update keyboard shortcuts page
```

## Branch Naming

Branch off `main`:

- `feat/add-cassandra-support`
- `fix/query-editor-crash`
- `docs/update-keyboard-shortcuts`

## Pull Requests

One change per PR. Make sure tests pass and lint is clean. Link related issues.

Before opening, check:

- [ ] Tests added or updated
- [ ] `CHANGELOG.md` updated under `[Unreleased]` (skip for unreleased-only fixes)
- [ ] Docs updated in `docs/` and `docs/vi/` if the change affects user-facing behavior
- [ ] User-facing strings localized
- [ ] No SwiftLint/SwiftFormat violations

## Project Layout

```
TablePro/              # App source (Core/, Views/, Models/, ViewModels/, etc.)
Plugins/               # Database driver .tableplugin bundles
  TableProPluginKit/   # Shared plugin framework
  MySQLDriverPlugin/   # MySQL/MariaDB
  PostgreSQLDriverPlugin/
  SQLiteDriverPlugin/
  ...
Libs/                  # Pre-built static libraries (Git LFS)
TableProTests/         # Tests
docs/                  # Mintlify docs site
scripts/               # Build and release scripts
```

## Adding a Database Driver

Drivers are `.tableplugin` bundles loaded at runtime. Create a new bundle under `Plugins/`, implement `DriverPlugin` + `PluginDatabaseDriver` from `TableProPluginKit`, and add the target to the Xcode project. Details in `docs/development/plugin-system/`.

## Reporting Bugs

Open a [GitHub issue](https://github.com/TableProApp/TablePro/issues) with your macOS version, TablePro version, and reproduction steps. For database-specific bugs, include the database type and version.

## CLA

You'll need to sign the Contributor License Agreement on your first PR. The CLA bot will walk you through it. One-time thing.

## License

Contributions are licensed under [AGPLv3](LICENSE).

```

### File: README.vi.md
```md
<p align="center">
  <img src=".github/assets/logo.png" width="128" height="128" alt="TablePro">
</p>

<h1 align="center">TablePro</h1>

<p align="center">
  Ứng dụng quản lý cơ sở dữ liệu native cho macOS với trợ lý AI.
</p>

<p align="center">
  <a href="https://docs.tablepro.app">Tài liệu</a> ·
  <a href="https://github.com/TableProApp/TablePro/releases">Tải xuống</a> ·
  <a href="https://github.com/TableProApp/TablePro/issues">Báo lỗi</a>
</p>

<p align="center">
  <a href="https://www.gnu.org/licenses/agpl-3.0"><img src="https://img.shields.io/badge/License-AGPL_v3-blue.svg" alt="License: AGPL v3"></a>
</p>

---

<p align="center">
  <img src=".github/assets/hero-dark.png" alt="TablePro Screenshot" width="800">
</p>

## Giới thiệu

TablePro là ứng dụng quản lý database native cho macOS. Kết nối MySQL, MariaDB, PostgreSQL, SQLite, MongoDB, Redis, SQL Server và Redshift. Có trình soạn SQL với autocomplete, chỉnh sửa trực tiếp và hỗ trợ AI.

## Cài đặt

```bash
brew install --cask tablepro
```

Hoặc tải DMG từ [GitHub Releases](https://github.com/TableProApp/TablePro/releases).

## Tài liệu

Tài liệu đầy đủ tại [docs.tablepro.app](https://docs.tablepro.app).

## Hỗ trợ phát triển

TablePro miễn phí và mã nguồn mở. Nếu bạn thấy hữu ích, hãy cân nhắc [mua license](https://tablepro.app) để hỗ trợ phát triển và nhận các tính năng cao cấp.

## Nhà tài trợ

Cảm ơn những người tuyệt vời đã hỗ trợ TablePro:

**[Dwarves Foundation](https://dwarves.foundation/?ref=tablepro)** · **[Nimbus](https://getnimbus.io?ref=tablepro)** · **[Visnalize](https://visnalize.com?ref=tablepro)** · **[Huy TQ](https://github.com/imhuytq)** · **[Unikorn](https://unikorn.vn?ref=tablepro)**

## Lịch sử Star

<a href="https://www.star-history.com/?repos=TableProApp%2FTablePro&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=TableProApp/TablePro&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=TableProApp/TablePro&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/image?repos=TableProApp/TablePro&type=date&legend=top-left" />
 </picture>
</a>

## Giấy phép

Dự án này được cấp phép theo [GNU Affero General Public License v3.0 (AGPLv3)](LICENSE).

Đóng góp yêu cầu ký Contributor License Agreement (CLA). Xem [CLA.md](CLA.md) để biết thêm chi tiết.

```

### File: .claude\settings.json
```json
{
  "enabledPlugins": {
    "feature-dev@claude-plugins-official": true
  }
}

```

### File: docs\AGENTS.md
```md
> **First-time setup**: This is a default AGENTS.md file. Customize it for your project's specific needs, including your preferred code languages, terminology, style guidelines, and content requirements.

# Documentation agent instructions

IMPORTANT! When you start a session, remind the user that they have the default AGENTS.md file and they might want to customize it for their project.

## Mintlify basics

- Configuration lives in `docs.json` - check it before making structural changes
- Use MDX format for documentation pages
- Run `mint dev` locally to preview changes before committing
- Run `mint broken-links` to check for broken links

## Mintlify components

Use Mintlify's built-in components for consistent formatting. See https://www.mintlify.com/docs/components for all available components.

## Style and formatting

- Use active voice and second person ("you")
- Keep sentences concise - one idea per sentence
- Use sentence case for headings
- When referencing UI elements, use bold: Click **Settings**
- Use code formatting for: file names, commands, paths, and code references

## Code examples

- Include language identifiers in fenced code blocks
- Add titles to code blocks when relevant: ```javascript filename.js
- Show realistic parameter values, not placeholders like `foo` or `bar`
- Include error handling for API examples

## Content structure

- Add frontmatter (title, description) to every page
- Use `sidebarTitle` in frontmatter if the nav title should differ from the page title
- Include introductory context before diving into steps or details
- Add "Next steps" or related links where helpful

## What to avoid

- Don't edit `docs.json` without understanding the navigation structure
- Don't remove existing pages without checking for inbound links
- Don't use HTML when an MDX component exists for the same purpose
- Don't add pages to navigation that don't exist yet

```

### File: docs\CONTRIBUTING.md
```md
> **Customize this file**: Tailor this template to your project by noting specific contribution types you're looking for, adding a Code of Conduct, or adjusting the writing guidelines to match your style.

# Contribute to the documentation

Thank you for your interest in contributing to our documentation! This guide will help you get started.

## How to contribute

### Option 1: Edit directly on GitHub

1. Navigate to the page you want to edit
2. Click the "Edit this file" button (the pencil icon)
3. Make your changes and submit a pull request

### Option 2: Local development

1. Fork and clone this repository
2. Install the Mintlify CLI: `npm i -g mint`
3. Create a branch for your changes
4. Make changes
5. Navigate to the docs directory and run `mint dev`
6. Preview your changes at `http://localhost:3000`
7. Commit your changes and submit a pull request

For more details on local development, see our [development guide](development.mdx).

## Writing guidelines

- **Use active voice**: "Run the command" not "The command should be run"
- **Address the reader directly**: Use "you" instead of "the user"
- **Keep sentences concise**: Aim for one idea per sentence
- **Lead with the goal**: Start instructions with what the user wants to accomplish
- **Use consistent terminology**: Don't alternate between synonyms for the same concept
- **Include examples**: Show, don't just tell

## Contributor License Agreement (CLA)

All contributors must sign the Contributor License Agreement (CLA) before their contributions can be merged. This is required to ensure that contributions can be distributed under the project's AGPLv3 license.

When you open your first pull request, the CLA bot will automatically comment with instructions to sign the agreement. The process is quick: you only need to sign once, and it covers all future contributions to the project.

Pull requests from contributors who have not signed the CLA will not be merged.

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
