---
id: PerformanceStudio
type: knowledge
owner: OA_Triage
---
# PerformanceStudio
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Performance Studio

A cross-platform SQL Server execution plan analyzer with built-in MCP server for AI-assisted analysis. Parses `.sqlplan` XML, identifies performance problems, suggests missing indexes, and provides actionable warnings — from the command line or a desktop GUI.

Built for developers and DBAs who want fast, automated plan analysis without clicking through SSMS.

## Screenshots

### Query Editor
Write queries with syntax highlighting and SQL keyword completion, connect to any SQL Server, and capture plans with one click.

![Query Editor](screenshots/Query%20Editor.png)

### Actual Execution Plan with Plan Insights
Graphical plan tree with SSMS-style operator icons, cost percentages, row counts, and warning badges. The Plan Insights panel shows runtime summary, missing indexes, parameters, and wait stats at a glance.

![Actual Execution Plan](screenshots/Actual%20Execution%20Plan.png)

### Multi-Statement Navigation
Navigate stored procedures and batches with multiple statements. Click any statement in the grid to jump to its plan. Plan Insights shows parameters with compiled vs runtime values.

![Navigate Stored Procedure Statements and Plans](screenshots/Navigate%20Stored%20Procedure%20Statements%20and%20Plans.png)

### Operator Tooltip and Properties
Hover over any operator for a detailed tooltip with costs, rows, I/O, timing, parallelism, and warnings. Click to open the full properties panel with per-thread timing, predicates, and more.

![Operator Tooltip](screenshots/Actual%20Execution%20Plan%20With%20Warning%20Tool%20Tip.png)

![Operator Properties](screenshots/Operator%20Properties.png)

### Advice for Humans
One-click text report with server context, warnings, wait stats, and expensive operators — ready to read or share.

![Advice for Humans](screenshots/Advice%20For%20Humans.png)

### Plan Comparison
Side-by-side comparison of two plans showing cost, runtime, I/O, memory, and wait stat differences.

![Plan Comparison](screenshots/Plan%20Comparison.png)

### Query Store Integration
Fetch top queries by CPU, duration, logical reads, physical reads, writes, memory, or executions from Query Store and load their plans directly into the analyzer.

![Query Store Integration](screenshots/Query%20Store%20Integration.png)

### MCP Integration
Ask Claude Code to analyze loaded plans, identify warnings, suggest indexes, and compare plans — all through the built-in MCP server.

![MCP Integration](screenshots/MCP%20Integration.png)

## What It Does

Feed it a query plan and it tells you what's wrong:

- **Large memory grants** — flags queries hoarding memory they don't use
- **Row estimate mismatches** — finds operators where estimates are 10x+ off from actuals
- **Missing indexes** — extracts SQL Server's index suggestions with ready-to-run CREATE statements
- **Hash, sort, and exchange spills** — identifies operators spilling to TempDB with severity based on volume
- **Parallel skew** — detects threads doing all the work while others sit idle
- **Scan predicates** — warns when scans filter rows with residual predicates
- **Key and RID lookups** — flags lookups back to the base table, distinguishes heaps from clustered indexes
- **Late filters** — finds Filter operators discarding rows deep in the plan
- **Nested loop concerns** — flags high-execution nested loops that might be better as hash joins
- **Parameter sniffing** — compares compiled vs runtime parameter values
- **Scalar UDFs** — warns about T-SQL and CLR scalar functions in execution paths
- **Implicit conversions** — detects type mismatches, upgrades severity when a seek plan is prevented
- **Anti-patterns** — OPTIMIZE FOR UNKNOWN, NOT IN with nullable columns, leading wildcards, function-wrapped predicates, and more

Each warning includes severity (Info, Warning, or Critical), the operator node ID, and enough context to act on immediately.

## Prerequisites

- [.NET 8 SDK](https://dotnet.microsoft.com/download/dotnet/8.0) (required to build and run)
- SQL Server instance (optional — only needed for live plan capture; file analysis works without one)
- Docker (optional — macOS/Linux users can run SQL Server locally via Docker)

## Download

Pre-built binaries are available on the [Releases](https://github.com/erikdarlingdata/PerformanceStudio/releases/latest) page:

| Platform | Download |
|----------|----------|
| Windows (x64) | [PerformanceStudio-win-x64.zip](https://github.com/erikdarlingdata/PerformanceStudio/releases/latest/download/PerformanceStudio-win-x64.zip) |
| macOS (Apple Silicon) | [PerformanceStudio-osx-arm64.zip](https://github.com/erikdarlingdata/PerformanceStudio/releases/latest/download/PerformanceStudio-osx-arm64.zip) |
| macOS (Intel) | [PerformanceStudio-osx-x64.zip](https://github.com/erikdarlingdata/PerformanceStudio/releases/latest/download/PerformanceStudio-osx-x64.zip) |
| Linux (x64) | [PerformanceStudio-linux-x64.zip](https://github.com/erikdarlingdata/PerformanceStudio/releases/latest/download/PerformanceStudio-linux-x64.zip) |

These are self-contained — no .NET SDK required. Extract the zip and run.

**macOS note:** macOS may block the app because it isn't signed with an Apple Developer certificate. If you see a warning that the app "can't be opened," run this after extracting:

```bash
xattr -cr PerformanceStudio.app
```

Then open the app normally.

## Build from Source

Clone and build:

```bash
git clone https://github.com/erikdarlingdata/PerformanceStudio.git
cd PerformanceStudio
dotnet build
```

To verify the build:

```bash
dotnet test tests/PlanViewer.Core.Tests    # 37 tests should pass
dotnet run --project src/PlanViewer.Cli -- analyze --help
```

## Quick Start

### Analyze an existing .sqlplan file

If you already have a `.sqlplan` file (saved from SSMS, Azure Data Studio, or another tool):

```bash
# JSON output (default) — full operator tree, suitable for automation
planview analyze my_query.sqlplan

# Human-readable text output
planview analyze my_query.sqlplan --output text

# Text output, warnings and missing indexes only (skip operator tree)
planview analyze my_query.sqlplan --output text --warnings-only
```

### Capture and analyze plans from a live server

Connect to a SQL Server instance, run queries, and capture their execution plans automatically.

**Quickest way** — pass credentials directly:

```bash
# Capture an actual execution plan (the query WILL run)
planview analyze --server sql2022 --database AdventureWorks \
    --login sa --password YourPassword \
    --query "SELECT * FROM Sales.SalesOrderHeader WHERE OrderDate > '2024-01-01'" \
    --trust-cert --output-dir ./results/

# Capture an estimated plan (safe for production — query is NOT executed)
planview analyze --server sql2022 --database AdventureWorks \
    --login sa --password YourPassword \
    --query "SELECT * FROM Sales.SalesOrderHeader" \
    --estimated --trust-cert --output-dir ./results/
```

**Using a .env file** — drop a `.env` in your working directory to avoid repeating connection details:

```bash
# .env
PLANVIEW_SERVER=sql2022
PLANVIEW_DATABASE=AdventureWorks
PLANVIEW_LOGIN=sa
PLANVIEW_PASSWORD=YourPassword
PLANVIEW_TRUST_CERT=true
```

Then just run:

```bash
planview analyze --query "SELECT * FROM Sales.SalesOrderHeader"
planview analyze ./queries/ --output-dir ./results/
```

CLI arguments override `.env` values when both are provided.

**Using the credential store** — for longer-term use, store credentials in your OS keychain:

```bash
# Store credentials (once per server)
planview credential add sql2022 --user sa
# You'll be prompted for the password — it's stored in your OS credential store

# Now connect without --login/--password
planview analyze --server sql2022 --database AdventureWorks \
    --query "SELECT * FROM Sales.SalesOrderHeader" \
    --trust-cert --output-dir ./results/
```

**Batch processing** a folder of .sql files:

```bash
planview analyze ./queries/ --server sql2022 --database StackOverflow2013 \
    --login sa --password YourPassword \
    --trust-cert --output-dir ./results/
```

Batch mode produces three files per query:
- `query_name.sqlplan` — the raw execution plan XML (openable in SSMS or the Performance Studio GUI)
- `query_name.analysis.json` — structured analysis with warnings, missing indexes, and operator tree
- `query_name.analysis.txt` — human-readable text report

### Manage credentials

```bash
planview credential add my-server --user sa        # prompts for password
planview credential add my-server --user sa -p pwd  # non-interactive
planview credential list                            # show stored credentials
planview credential remove my-server                # delete credential
```

Credentials are stored in the OS credential store — Windows Credential Manager on Windows, Apple Keychain on macOS. Nothing is written to disk in plaintext.

## Example Output

These examples were generated against StackOverflow2013 on SQL Server 2022. Source queries are in [`examples/queries/`](examples/queries/), plans and analysis in [`examples/output/`](examples/output/).

### Text output (`--output text`)

```
Plan: 04_comment_heavy_posts.sqlplan
SQL Server: 1.564 (build 16.0.4222.2)
Statements: 1

--- Statement 1: SELECT ---
  Query: SELECT p.Id, p.Title, p.Score, COUNT(c.Id) AS CommentCount
         FROM dbo.Posts AS p JOIN dbo.Comments AS c ON c.PostId = p.Id
         WHERE p.PostTypeId = 1 GROUP BY p.Id, p.Title, p.Score
         HAVING COUNT(c.Id) > 20 ORDER BY CommentCount DESC
  Estimated cost: 4069.8700
  DOP: 8
  Runtime: 4551ms elapsed, 15049ms CPU
  Memory grant: 8,022,664 KB granted, 2,514,944 KB used

  Warnings:
    [Critical] Large Memory Grant: Query granted 7835 MB of memory.

  Operator warnings:
    [Critical] Parallelism (Node 0): Estimated 1 rows, actual 2,889 (2889x underestimated).
    [Critical] Sort (Node 1): Estimated 1 rows, actual 2,889 (2889x underestimated).
    [Warning] Sort (Node 1): Thread 1 processed 100% of rows. Work is heavily skewed.
    [Warning] Filter (Node 2): Filter discards rows late in the plan.

  Missing indexes:
    StackOverflow2013.dbo.Posts (impact: 74%)
      CREATE NONCLUSTERED INDEX [IX_Posts_PostTypeId]
      ON dbo.Posts (PostTypeId) INCLUDE (Score, Title)
    StackOverflow2013.dbo.Comments (impact: 19%)
      CREATE NONCLUSTERED INDEX [IX_Comments_PostId]
      ON dbo.Comments (PostId)

=== Summary ===
  Warnings: 8 (4 critical)
  Missing indexes: 2
  Actual stats: yes
  Warning types: Filter Operator, Large Memory Grant, Parallel Skew,
                 Row Estimate Mismatch, Scan With Predicate
```

### JSON output (default)

The default JSON output includes the full operator tree, making it suitable for CI pipelines, LLM consumption, or further processing. See [`examples/output/`](examples/output/) for complete examples.

### Batch processing

```
$ planview analyze ./examples/queries/ --server sql2022 \
    --database StackOverflow2013 --trust-cert --output-dir ./results/

Capturing actual plans from sql2022/StackOverflow2013

[1/5] 01_top_users_by_posts ... OK (1.8s)
[2/5] 02_recent_questions ... OK (0.8s)
[3/5] 03_unanswered_high_score ... OK (0.7s)
[4/5] 04_comment_heavy_posts ... OK (4.7s)
[5/5] 05_user_vote_summary ... OK (4.3s)

Processed 5 files: 5 succeeded, 0 failed
Output: ./results/
```

## Desktop GUI

The Avalonia-based GUI renders execution plans visually with the same operator icons as SSMS. Open `.sqlplan` files via File > Open or drag-and-drop.

Features:
- Graphical plan tree with cost percentages and row counts
- Warning badge on root node showing total warning count
- Plan Insights panel — three-column view with runtime summary, missing indexes, and wait stats visualization
- Zoom and pan (mouse wheel + middle-click drag)
- Click any operator to see full properties (30 sections)
- Statement grid with sortable columns (cost, rows, DOP, warnings)
- Tooltips on hover with key operator metrics
- **Advice for Humans** — one-click text analysis report you can read or share
- **Advice for Robots** — one-click JSON export designed for LLMs and automation
- **Plan Comparison** — compare two plans side-by-side (cost, runtime, I/O, memory, wait stats)
- **Copy Repro Script** — extracts parameters, SET options, and query text into a runnable `sp_executesql` script
- **Get Actual Plan** — connect to a server and re-execute the query to capture runtime stats
- **Query Store Analysis** — connect to a server and analyze top queries by CPU, duration, or reads
- **MCP Server** — built-in Model Context Protocol server for AI-assisted plan analysis (opt-in)
- Dark theme

```bash
dotnet run --project src/PlanViewer.App
```

## SSMS Extension

A VSIX extension that adds **"Open in Performance Studio"** to the execution plan right-click context menu in SSMS 18-22.

### How it works

1. Right-click on any execution plan in SSMS
2. Click "Open in Performance Studio"
3. The extension extracts the plan XML via reflection and saves it to a temp file
4. Performance Studio opens with the plan loaded

### Installation

1. Download `PlanViewer.Ssms.vsix` and `InstallSsmsExtension.exe` from the [v0.7.0 release](https://github.com/erikdarlingdata/PerformanceStudio/releases/tag/v0.7.0) (SSMS extension is not yet included in automated builds)
2. Place them in the same folder
3. Double-click `InstallSsmsExtension.exe` and approve the UAC prompt
4. The installer auto-detects SSMS 21 and/or SSMS 22 and installs into both
5. Restart SSMS to activate the extension

### First run

On first use, if Performance Studio isn't found automatically, the extension will prompt you to locate `PlanViewer.App.exe`. The path is saved to the registry (`HKCU\SOFTWARE\DarlingData\SQLPerformanceStudio\InstallPath`) so you only need to do this once.

The extension searches for the app in this order:
1. Registry key (set automatically after first browse)
2. System PATH
3. Common install locations (`%LOCALAPPDATA%\Programs\SQLPerformanceStudio\`, `Program Files`, etc.)

## MCP Server (LLM Integration)

The desktop GUI includes an embedded [Model Context Protocol](https://modelcontextprotocol.io) server that exposes loaded execution plans and Query Store data to LLM clients like Claude Code and Cursor.

### Setup

1. Enable the MCP server in `~/.planview/settings.json`:

```json
{
  "mcp_enabled": true,
  "mcp_port": 5152
}
```

2. Register with Claude Code:

```
claude mcp add --transport http --scope user performance-studio http://localhost:5152/
```

3. Open a new Claude Code session and ask questions like:
   - "What plans are loaded in the application?"
   - "Analyze the execution plan and tell me what's wrong"
   - "Are there any missing index suggestions?"
   - "Compare these two plans — which is better?"
   - "Fetch the top 10 queries by CPU from Query Store"

### Available Tools

13 tools for plan analysis and Query Store data:

| Category | Tools |
|---|---|
| Discovery | `list_plans`, `get_connections` |
| Plan Analysis | `analyze_plan`, `get_
... [TRUNCATED]
```

### File: CONTRIBUTING.md
```md
# Contributing to Performance Studio

Thank you for your interest in contributing to Performance Studio! This guide will help you get started.

## Reporting Issues

- Use [GitHub Issues](https://github.com/erikdarlingdata/PerformanceStudio/issues) for bugs and feature requests
- Include the `.sqlplan` file (or a minimal reproduction) when reporting parser or analysis bugs
- Specify your OS and .NET version

## Development Setup

### Prerequisites

- [.NET 8 SDK](https://dotnet.microsoft.com/download/dotnet/8.0)
- Git

### Build and Test

```bash
git clone https://github.com/erikdarlingdata/PerformanceStudio.git
cd PerformanceStudio
dotnet build
dotnet test tests/PlanViewer.Core.Tests
```

### Run the GUI

```bash
dotnet run --project src/PlanViewer.App
```

### Run the CLI

```bash
dotnet run --project src/PlanViewer.Cli -- analyze --help
```

## Project Structure

```
PerformanceStudio/
├── src/
│   ├── PlanViewer.Core/       # Analysis engine (parser, rules, layout)
│   ├── PlanViewer.App/        # Avalonia desktop GUI
│   └── PlanViewer.Cli/        # CLI tool (planview command)
└── tests/
    └── PlanViewer.Core.Tests/ # xUnit tests with real .sqlplan fixtures
```

## Architecture

- **PlanViewer.Core** is the shared library. It contains the XML parser (`ShowPlanParser`), analysis rules (`PlanAnalyzer`), plan layout engine, text/JSON formatters, and all models. Both the GUI and CLI depend on it.
- **PlanViewer.App** is an Avalonia 11 desktop app using code-behind (no MVVM framework). It renders plan trees on a Canvas with the same operator icons as SSMS.
- **PlanViewer.Cli** is a System.CommandLine-based CLI tool that wraps Core for command-line use.

## Code Style

- File-scoped namespaces (`namespace Foo;`)
- Nullable enabled across all projects
- Code-behind pattern for UI (no MVVM, no ReactiveUI)
- No unnecessary abstractions — keep it simple and direct
- Tests use real `.sqlplan` XML fixtures, not mocks

## Adding Analysis Rules

Rules live in `PlanAnalyzer.cs`. Each rule:

1. Inspects `PlanNode` properties (statement-level rules) or individual operator nodes
2. Adds a `PlanWarning` with `WarningType`, `Message`, and `Severity` (Info, Warning, or Critical)
3. Has a corresponding test in `PlanAnalyzerTests.cs` with a minimal `.sqlplan` fixture

When adding a rule:
- Add the rule logic to `AnalyzeStatement()` or `AnalyzeNode()` in `PlanAnalyzer.cs`
- Create a minimal `.sqlplan` test fixture in `tests/PlanViewer.Core.Tests/Plans/`
- Add a test method in `PlanAnalyzerTests.cs`
- Ensure all existing tests still pass

## Pull Requests

1. Fork the repo and create a feature branch
2. Make your changes
3. Run `dotnet test` — all tests must pass
4. Run `dotnet build` — no warnings or errors
5. Open a PR with a clear description of what changed and why

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

```

### File: llms.txt
```txt
# SQL Server Performance Studio

> Free, open-source SQL Server execution plan analyzer by Erik Darling (Darling Data, LLC). Cross-platform desktop GUI (Avalonia) and CLI tool with 30 analysis rules that identify memory grants, row estimate mismatches, missing indexes, spills, parallel skew, parameter sniffing, implicit conversions, and more. Built-in MCP server for AI-assisted plan analysis. SSMS extension for one-click plan transfer. Runs on Windows, macOS, and Linux. MIT licensed.

- Analyzes .sqlplan XML files or captures plans live from SQL Server
- 30 rules covering memory, estimates, indexes, parallelism, joins, filters, functions, parameters, patterns, compilation, objects, and operators
- Query Store browser with search by identifier, multi-plan history charting, and in-line bar charts
- CLI supports batch processing of .sql file directories with JSON and text output
- Built-in MCP server with 13 tools for plan analysis and Query Store data
- SSMS 18-22 extension adds "Open in Performance Studio" context menu

## Documentation

- [README](https://github.com/erikdarlingdata/PerformanceStudio/blob/main/README.md): Complete documentation including quick start, CLI reference, analysis rules, MCP server setup, and platform support
- [Releases](https://github.com/erikdarlingdata/PerformanceStudio/releases): Download pre-built binaries for Windows, macOS, and Linux
- [Examples](https://github.com/erikdarlingdata/PerformanceStudio/tree/main/examples): Sample queries, plans, and analysis output

## Optional

- [License](https://github.com/erikdarlingdata/PerformanceStudio/blob/main/LICENSE): MIT License
- [Third-party notices](https://github.com/erikdarlingdata/PerformanceStudio/blob/main/THIRD_PARTY_NOTICES.md): License information for bundled components

```

### File: SECURITY.md
```md
# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in Performance Studio, please report it responsibly.

**Do not open a public GitHub issue for security vulnerabilities.**

Instead, please email **erik@erikdarling.com** with:

- A description of the vulnerability
- Steps to reproduce the issue
- The potential impact
- Any suggested fixes (optional)

You should receive a response within 72 hours. We will work with you to understand the issue and coordinate a fix before any public disclosure.

## Scope

This policy applies to:

- Desktop application (PlanViewer.App)
- Core analysis library (PlanViewer.Core)
- CLI tool (PlanViewer.Cli)
- SSMS extension (PlanViewer.Ssms)

## Security Best Practices

When using Performance Studio:

- Use Windows Authentication where possible when connecting to SQL Server
- Use dedicated accounts with minimal required permissions
- Enable encryption for SQL Server connections
- Keep your SQL Server instances patched and up to date

```

### File: THIRD_PARTY_NOTICES.md
```md
# Third-Party Notices

Performance Studio includes the following third-party open-source components. Each component is subject to the license terms specified below.

---

## vscode-mssql (Execution Plan Icons)

**Author**: Microsoft Corporation
**Repository**: https://github.com/microsoft/vscode-mssql
**License**: MIT License

Execution plan operator icons (PNG) from the vscode-mssql extension are used to render graphical execution plans. Icons are located in `src/PlanViewer.Core/Resources/PlanIcons/`.

### License Text

MIT License

Copyright (c) Microsoft Corporation

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

Full license: https://github.com/microsoft/vscode-mssql/blob/main/LICENSE

---

## Acknowledgments

Performance Studio uses execution plan operator icons from **Microsoft's vscode-mssql extension**, which provides SQL Server tooling for Visual Studio Code. We are grateful for their commitment to open-source software.

---

*Last Updated: March 5, 2026*

```

### File: .github\PULL_REQUEST_TEMPLATE.md
```md
## What does this PR do?

A clear description of the change and why it's being made.

## Which component(s) does this affect?

- [ ] Desktop App (PlanViewer.App)
- [ ] Core Library (PlanViewer.Core)
- [ ] CLI Tool (PlanViewer.Cli)
- [ ] SSMS Extension (PlanViewer.Ssms)
- [ ] Tests
- [ ] Documentation

## How was this tested?

Describe the testing you've done. Include:
- Plan files tested (estimated, actual, Query Store, etc.)
- Platforms tested (Windows, macOS, Linux)

## Checklist

- [ ] I have read the [contributing guide](https://github.com/erikdarlingdata/PerformanceStudio/blob/main/CONTRIBUTING.md)
- [ ] My code builds with zero warnings (`dotnet build -c Debug`)
- [ ] All tests pass (`dotnet test`)
- [ ] I have not introduced any hardcoded credentials or server names

```

