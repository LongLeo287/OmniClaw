# ☘️ llm-lean-log

<p align="center">
  <img src="docs/imgs/logo.webp" alt="llm-lean-log logo" width="200">
</p>

|Package|What is it?|Version|Downloads|NPM Page|
|---|---|---|---|---|
|llm-lean-log-cli|CLI tool to save/read chat logs|![llm-lean-log-cli npm](https://img.shields.io/npm/v/llm-lean-log-cli)|![llm-lean-log-core npm](https://img.shields.io/npm/dw/llm-lean-log-core)|[npm page](https://www.npmjs.com/package/llm-lean-log-cli)|
|llm-lean-log-core|Core library to save/read chat logs|![llm-lean-log-core npm](https://img.shields.io/npm/v/llm-lean-log-core)|![l-log-vis npm](https://img.shields.io/npm/dw/l-log-vis)|[npm page](https://www.npmjs.com/package/llm-lean-log-core)|
|bl-log|CLI tool to save/read chat logs for Bun only|![bl-log npm](https://img.shields.io/npm/v/bl-log)|![bl-log npm](https://img.shields.io/npm/dw/bl-log)|[npm page](https://www.npmjs.com/package/bl-log)|
|l-log-vis|CLI tool to view chat logs|![l-log-vis npm](https://img.shields.io/npm/v/l-log-vis)|![l-log-vis npm](https://img.shields.io/npm/dw/l-log-vis)|[npm page](https://www.npmjs.com/package/l-log-vis)|
|l-log-mcp-server|MCP Server to save/read chat logs|![l-log-mcp-server npm](https://img.shields.io/npm/v/l-log-mcp-server)|![l-log-mcp-server npm](https://img.shields.io/npm/dw/l-log-mcp-server)|[npm page](https://www.npmjs.com/package/l-log-mcp-server)|

[Vietnamese](README-vi.md) | [Japanese](README-ja.md) | [Chinese](README-zh.md)

Work with LLMs and it's agents to write and read logs:

- Antigravity
- Cursor
- Windsurf
- Claude Code
- Opencode
- or what LLM client you want

Starting from my day-to-day coding needs, I wanted a tool to log chat sessions with AI agents so I could use them as personal reference material or as project documentation. While browsing developer groups, I also noticed a growing demand for syncing chat logs across multiple machines and keeping long-term history.

That’s how `llm-lean-log-cli` was born: a tool for reading and writing chat history optimized for minimal token usage — which means fewer tokens, and therefore lower cost.

> 📝 Logging for LLMs, but we cut the fat.

`llm-lean-log` is a format for logging that is optimized for LLMs token usage, cause and effect relationships based on CSV Data.

## 🍓 Ask AI agent (LLMs) to write a log

Before you ask AI agent (LLMs) to write a log, make sure to install `llm-lean-log-cli` CLI tool globally.

```bash
bun add -g llm-lean-log-cli
```

Ask LLMs to write a log by prompt:

> use `l-log add ./logs/chat.csv "Fix bug" --tags=bug,fix --problem="Problem description" --files="file1.ts,src/file2.ts" --tech-stack="elysia,drizzle,sqlite" --causeIds="uuid1,uuid2" --created-by-agent="agent-name"` CLI tool to save last chat logs / talk above

Or simpler for user but less efficient for LLMs:

> use l-log CLI to save chat log above

Or:

> use l-log to save

## 🍓 Ask AI agent (LLMs) to read a log

Ask LLMs to read last log only by prompt (efficient for LLMs):

> run `l-log view ./logs/example.csv --last` CLI and read output

Ask LLMs to read all logs by prompt (less efficient for LLMs):

> read last chat logs from "./logs/example.csv" and tell me what should I do next

This is a efficient way to read logs for LLMs. Save time, tokens and energy. Because LLMs no need to read long CSV files before LLMs can write a log at the end of the log.

## 📚 Add rules for agent to write log

For example, you can add this rule to your LLM agent configuration file (e.g. `.agent/rules/common.md`):

```bash
# Create file
touch .agent/rules/common.md
```

Add this content to the file:

```text
---
trigger: always_on
---

# Common rules for LLM agent

Whenever you finish a task or change codes, always log your work using the l-log bash command (llm-lean-log-cli package) with the following format:

`l-log add ./logs/chat.csv "<Task Name>" --tags="<tags>" --problem="<problem>" --solution="<solution>" --action="<action>" --files="<files>" --tech-stack="<tech>" --created-by-agent="<agent-name>"`

Note: `--last-commit-short-sha` is optional and will be auto-populated by the CLI if not provided.

Before run:

- Install the l-log CLI if not already installed: `bun add -g llm-lean-log-cli`.
- If need, run CLI help command: `l-log -h` for more information.
- log path: `./logs/chat.csv`.

```

With `logs/chat.csv` file path, you can change it to any path you want.

If LLMs forget about the log or it is not known that should write the log when responding to a user, you can ask LLMs to write the log again by prompt:

> use l-log

## 🌵 MCP Memory

For MCP memory, please use `l-log-mcp-server` package. More information in [packages/mcp/README.md](packages/mcp/README.md) and [packages/mcp-server/README.md](packages/mcp-server/README.md).

## ❌ Problems

- `markdown` is not optimized for LLMs token usage, only for human readability.
- `json` is not optimized for LLMs token usage, only for machine readability.
- Best performance of LLMs token usage. This is pure tabular data, so CSV is smaller than `TOON` for flat tables. Refer to <https://github.com/toon-format/toon?tab=readme-ov-file#when-not-to-use-toon>.
- There are many best practices for system logging, but they are not optimized for LLMs token usage and missing data structure for understanding the context of the log chat.
  - For example, log level WARNING is using for system logger, but what LLMs need to know?
- Clean, predictable and simple format for LLMs to read past seasons of logs.
- When LLMs write logs, should be use by a CLI tool to save logs, so LLMs no need to edit CSV file itself and it's saving time, tokens and energy.
  - -> We need a efficient way to save logs for LLMs.
- When human read CSV logs, I want a tool to view long CSV logs in a more human-friendly way.
  - -> We need a efficient way to read logs for humans.
- A local first, full control data storage for logs, documents of project, not dependent on external services like Cursor, Windsurf, TUI client, etc.
- Very long, long and long conversation history, but LLMs can summarize it in a few words and save important information only.
  - -> Do not save all conversation history, only save important information.
- We need a reasoning-based, human-like retrieval over long documents (like <https://github.com/VectifyAI/PageIndex>).
  - Data can be Directed Acyclic Graph (<https://en.wikipedia.org/wiki/Directed_acyclic_graph>) or Directed cyclic Graph (<https://en.wikipedia.org/wiki/Directed_graph>). Cause and effect is link between nodes - chats.

## ✅ Solution

<img src="docs/imgs/graph.png" alt="Graph" width="256">

🪴 Create a simple, single, flat, CSV data format file for logs:

- 🌟 Headers are logger important fields:

  - `id`: log ID (required), UUID for unique identifier, used for Directed Graph, cause and effect.
  - `name`: main content of the log (short). (required)
  - `tags`: tags to categorize the log, comma separated, wrap with double quotes if multiple tags. Example: `"error,api,auth"`. (optional)
  - `problem`: description of the problem, context of the log. (required)
  - `solution`: description of the solution, method to fix the problem. (optional)
  - `action`: run command, action (web search, etc.) that was taken to fix the problem. (optional)

    - running command format: `text {language}`\`code-block\``

      - Example of row value:

        ```text
        run bash`bun i`; then start dev server bash`bun dev`; update constants in "src/constants.ts": ts`const MY_CONSTANT = 'new value';`
        ```

      - Language is optional, but recommended for better parsing.
      - Why?
        - Better parsing and understanding of the code.
        - Learn from Markdown code blocks format, so humans can read and understand the code.

    - Format: `text {language}`\`code-block\`` or markdown code block or text.

  - `files`: list of files that were modified, created, deleted or must be read (optional).
    - Example: `"src/index.ts,src/constants.ts"`
    - Why?
      - Better understanding of the code, context of the log.
    - Format: comma separated list of files, wrap with double quotes if multiple files.
  - `tech-stack`: list of technologies that were used (optional).
    - Example: `"elysia,drizzle,sqlite,turso"`
    - Why?
      - Better understanding of the code, context of the log.
    - Format: comma separated list of technologies, wrap with double quotes if multiple technologies.
  - `cause`: cause log of the problem (optional).

    - Example: `you choose to use X instead of Y, to do Z`
    - Why?
      - Better understanding of the log.
    - Format: text.

  - `causeIds`: cause log ID of the log (optional).

    - Example: `"UUID,UUID"`
    - Why?
      - Better understanding of the log.
    - Format: comma separated list of other log IDs, wrap with double quotes if multiple cause log IDs.

  - `effectIds`: effect log ID of the log (optional).

    - Example: `"UUID,UUID"`
    - Why?
      - Better understanding of the log.
    - Format: comma separated list of other log IDs, wrap with double quotes if multiple effect log IDs.

  - `last-commit-short-sha`: last git commit short SHA of the log (optional).
    - If not input, it will be updated automatically by `l-log` CLI tool.
    - Example: `a1b2c3d`
    - Why not updated git commit?
      - git commit is usually updated before when LLMs write logs.
    - Format: short SHA of the last commit.

  - `created-at`: when the log was created. (required).
    - Format: `YYYY-MM-DDTHH:mm:ssZ` (ISO 8601)
      - Example: `2025-10-15T12:34:56Z`
      - Readable for humans, machines and LLMs.
  - `updated-at`: when the log was updated (optional).
    - Format: `YYYY-MM-DDTHH:mm:ssZ` (ISO 8601)
      - Example: `2025-10-15T12:34:56Z`
      - Readable for humans, machines and LLMs.
  - `model`: model that was used (optional).
    - Example: `gpt-4o-mini`
  - `created-by-agent`: model that was used to create the log (optional).
    - Example: `gpt-4o-mini`

- Row:
  - Each row is a log entry.
  - No new lines, or use `\n`, just use comma - `,`, dot - `.`, semicolon - `;` to separate information.

## Another problems

Problem: CSV format is sometimes hard to read since it's not human-friendly, too long lines, no code-blocks support.

- Solution: Use `llm-lean-log-cli` CLI tool for viewing logs in a more human-friendly way.

```bash
bun add -g llm-lean-log-cli
```

User want to view `git diff` from log:

- Solution: `llm-lean-log-cli` CLI tool will auto save `git diff` to `.diff` file.
  - When LLM/ Human write logs, it will auto save `git diff` to `.diff` file.
    - use `git diff -- . ':(exclude)*.lock' ':(exclude)yarn.lock' ':(exclude)package-lock.json' > <UUID>.diff` to exclude `*.lock` files.

## 💻 Usage

`llm-lean-log-cli`'s bin name is `l-log`.

For LLMs viewing logs (no need `--human` option, output is CSV format (+ auto-hide Metadata columns if empty)):

```bash
# List all log entries, output is CSV format
l-log list ./logs/example.csv
```

Expected output is CSV format for LLMs:

```text
id,name,tags,problem,solution,action,files,tech-stack,causeIds,created-at,model
auth-error-001,API Authentication Error,"error,api,auth",Users unable to login due to JWT token expiration not being handled correctly,Added token refresh logic with exponential backoff retry mechanism,Updated auth.ts middleware and added refresh endpoint,"src/middleware/auth.ts, src/routes/auth.routes.ts","typescript, express, jwt",,2026-01-13T14:52:58.681Z,claude-3.5-sonnet
db-investigation-002,Database Connection Pool Exhausted,"error,database,performance",Application crashes during high traffic due to database connection pool being exhausted,Increased pool size from 10 to 50 and added connection timeout handling,"Modified database.config.ts: ts`pool.max = 50, pool.idleTimeoutMillis = 30_000`",src/config/database.config.ts,"typescript, postgresql, node.js",auth-error-001,2026-01-13T14:52:58.681Z,gpt-4-turbo
...
```

```bash
# Show statistics
l-log stats ./logs/example.csv

# View detailed entry at index
l-log view ./logs/example.csv 0

# View the last log entry
l-log view ./logs/example.csv --last
```

Expected output is CSV format for LLMs:

```text
id,name,tags,problem,solution,action,files,tech-stack,causeIds,created-at,model
typescript-migration-006,TypeScript Migration Complete,"refactor,typescript,milestone",Codebase was in JavaScript making it hard to catch type errors,Migrated entire codebase to TypeScript with strict mode enabled,"Converted all .js files to .ts, added type definitions, configured tsconfig.json","tsconfig.json, package.json, src/**/*","typescript, node.js","auth-error-001,memory-leak-004,image-optimization-005",2026-01-13T14:52:58.681Z,gpt-4-turbo
```

```bash
# Search logs, output is CSV format
l-log search ./logs/example.csv "Database"

# Filter by tags, output is CSV format
l-log tags ./logs/example.csv error api

# Add a new log entry (auto-saves git diff by default)
l-log add ./logs/chat.csv "Fix bug" --tags=bug,fix --problem="Problem description"

# Add a new log entry without saving git diff
l-log add ./logs/chat.csv "Fix bug" --tags=bug,fix --problem="Problem description" --no-diff

# Add a new log entry and explicitly save git diff (default behavior)
l-log add ./logs/chat.csv "Fix bug" --tags=bug,fix --problem="Problem description" --diff
```

For human users viewing logs with `--human` option:

```bash
# List all log entries
l-log list ./logs/example.csv --human
# Output: [Full beautiful table with colors and headers]

# Show statistics
l-log stats ./logs/example.csv --human

# View detailed entry at index
l-log view ./logs/example.csv 0 --human

# Search logs
l-log search ./logs/example.csv "query" --human

# Filter by tags
l-log tags ./logs/example.csv tag1 tag2 --human

# Add a new log entry, if not specify log file, it will use `./logs/example.csv` log file
l-log add ./logs/example.csv "Fix bug" --tags=bug,fix --problem="Problem description"
```

## 🐳 Visualizer for humans

Install `l-log-vis` (llm-lean-log-visualizer` package) globally:

```bash
bun add -g l-log-vis
```

Run visualizer:

```bash
l-log-vis ./logs/example.csv
# or
l-log-vis
```

## 🛠️ Development

- Added CLI tool for managing logs
- Added search and filter capabilities
- Added beautiful React-based Web Visualizer with code highlighting, view more at [Web Visualizer](./packages/visualizer/README.md).

To install dependencies:

```bash
bun i
```

### 🌈 Running the Application

🌱 Create example logs and run visualizer:

```bash
bun example
```

💻 CLI Usage:

```bash
# List all log entries
bun cli list

# List all log entries (compact view)
bun cli ls -c
```

```bash
# Show statistics
bun cli stats
```

Screenshots:

![CLI Stats](docs/imgs/bun-cli-stats.png)

```bash
# View detailed entry at index
bun cli view 0

# View the last log entry
bun cli view --last
```

Screenshots:

![CLI View](docs/imgs/bun-cli-view.png)

```bash
# Search logs by name, problem, or solution
bun cli search "memory"
```

Screenshots:

![CLI Search](docs/imgs/bun-cli-search.png)

```bash
# Filter logs by tags
bun cli tags error api
```

```bash
# Add a new log entry
bun cli add "Fix bug" --tags=bug,fix --problem="Bug description" --solution="Fixed the issue"
# expected: Log entry added successfully

# Show help
bun cli help
```

This project was created using `bun init` in bun v1.3.5. [Bun](https://bun.com) is a fast all-in-one JavaScript runtime.

## 📖 Additional information

- Publish docs: `./docs/publish.sh`
- Release docs: `./docs/release.sh`

### Documentation

- [AI Agents Integration](./docs/ai-agents.md) - Guide for configuring AI agents (Cursor, Windsurf, Claude Code, OpenCode, etc.)
- [Development Guide](./docs/development.md) - Detailed development setup, commands, and workflow
- [AGENTS.md](./AGENTS.md) - Comprehensive guide for AI agents working on this project
- [CONTRIBUTING.md](./CONTRIBUTING.md) - Contribution guidelines and code style
- [Project Structure](./docs/project-strcture.md) - Overview of project structure
- [Graph](./docs/graph.md) - Basic workflow diagram
- [Public](./docs/public.md) - How to publish packages
- [Release](./docs/release.md) - Release process and changelog format

### 💻 Use with VS Code base editor

- Install recommended extensions from `.vscode/extensions.json`, which includes:
  - `DavidAnson.vscode-markdownlint` - Markdown linting
  - `biomejs.biome` - Code formatting and linting
  - `oven-sh.bun` - Bun runtime support
  - `jeff-hykin.better-csv-syntax` - CSV syntax highlighting (with color coding)
  - `YoavBls.pretty-ts-errors` - Pretty TypeScript errors
  - `ReprEng.csv` - CSV support

![CSV Preview](./docs/imgs/screenshot-csv-preview.png)

## 📚 Coverage status

Read more at `./coverage.txt`

## TODO

- Improve visualizer web app for Directed Graph (show cause and effect).

## 📄 License

MIT
