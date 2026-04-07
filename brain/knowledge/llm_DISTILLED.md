---
id: llm
type: knowledge
owner: OA_Triage
---
# llm
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
	"name": "llm-lean-log",
	"version": "0.2.6",
	"private": true,
	"scripts": {
		"example": "bun run --filter llm-lean-log-core example",
		"cli": "bun run packages/cli/src/index.ts",
		"web:dev": "bun run --filter l-log-vis dev",
		"mcp:dev": "bun run --filter l-log-mcp-server dev",
		"mcp:start": "bun run --filter l-log-mcp-server start",
		"fmt": "biome format --write .",
		"lint": "biome lint",
		"test": "bun test",
		"test:watch": "bun test --watch",
		"test:coverage": "bun test --coverage",
		"test:coverage:w": "bun test --coverage > coverage.txt 2>&1",
		"pub:core": "cd packages/core && bun publish",
		"pub:cli": "cd packages/cli && bun publish",
		"pub:vis": "cd packages/visualizer && bun publish",
		"pub:mcp": "cd packages/mcp && bun publish",
		"pub:mcp-server": "cd packages/mcp-server && bun publish",
		"type": "bun run --filter llm-lean-log-core type && bun run --filter llm-lean-log-cli type && bun run --filter l-log-vis type"
	},
	"description": "Logging for LLMs, but we cut the fat. A CSV-based logging format optimized for LLM token usage.",
	"repository": {
		"type": "git",
		"url": "git+https://github.com/loclv/llm-lean-log.git"
	},
	"bugs": {
		"url": "https://github.com/loclv/llm-lean-log/issues"
	},
	"homepage": "https://github.com/loclv/llm-lean-log#readme",
	"workspaces": [
		"packages/*"
	],
	"type": "module",
	"devDependencies": {
		"@biomejs/biome": "^2.3.11",
		"bun-types": "latest"
	},
	"peerDependencies": {
		"typescript": "^5.9.3"
	},
	"keywords": [
		"llm",
		"logging",
		"csv",
		"token-optimization",
		"ai"
	],
	"engines": {
		"bun": ">=1.3.9",
		"npm": "please-use-bun"
	},
	"license": "MIT"
}

```

### File: README.md
```md
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

![CLI Search](docs/imgs/bun-cli-search
... [TRUNCATED]
```

### File: packages\cli\package.json
```json
{
	"name": "llm-lean-log-cli",
	"version": "0.2.9",
	"description": "CLI tool for llm-lean-log",
	"scripts": {
		"cli": "bun run src/index.ts",
		"build": "bun build src/index.ts --outfile dist/index.js --target node && tsc --emitDeclarationOnly",
		"compile": "bun build src/index.bun.ts --compile --outfile dist/l-log-bun --target bun",
		"compile:mac": "bun build src/index.bun.ts --compile --target bun-darwin-arm64 --outfile dist/l-log-mac",
		"compile:win": "bun build src/index.bun.ts --compile --target bun-windows-x64 --outfile dist/l-log-win.exe",
		"compile:linux": "bun build src/index.bun.ts --compile --target bun-linux-x64 --outfile dist/l-log-linux",
		"prepublishOnly": "bun run build",
		"type": "tsc --noEmit"
	},
	"repository": {
		"type": "git",
		"url": "git+https://github.com/loclv/llm-lean-log.git",
		"directory": "packages/cli"
	},
	"bugs": {
		"url": "https://github.com/loclv/llm-lean-log/issues"
	},
	"homepage": "https://github.com/loclv/llm-lean-log/tree/main/packages/cli#readme",
	"main": "dist/index.js",
	"module": "dist/index.js",
	"type": "module",
	"bin": {
		"l-log": "dist/index.js"
	},
	"files": [
		"dist",
		"README.md",
		"LICENSE"
	],
	"publishConfig": {
		"access": "public"
	},
	"dependencies": {
		"cli-highlight": "^2.1.11"
	},
	"devDependencies": {
		"@types/bun": "latest",
		"llm-lean-log-core": "workspace:*",
		"typescript": "^5.9.3"
	},
	"keywords": [
		"llm",
		"logging",
		"cli",
		"csv",
		"token-optimization"
	],
	"license": "MIT"
}

```

### File: packages\cli\README.md
```md
# llm-lean-log-cli

> 💻 CLI tool for llm-lean-log - Logging for LLMs, but we cut the fat.

`llm-lean-log` is a format for logging that is optimized for LLM token usage, using a simple CSV-based structure.

For more information, see the [main repository](https://github.com/loclv/llm-lean-log).

## 🚀 Installation

```bash
bun add -g llm-lean-log-cli
```

## 💻 Usage

For LLMs viewing logs (default output is structured CSV):

```bash
# List all log entries (returns CSV, omits empty columns)
l-log list ./logs/example.csv

# Show statistics
l-log stats ./logs/example.csv

# View detailed entry at index (returns minimal CSV)
l-log view ./logs/example.csv 0

# View the last log entry
l-log view ./logs/example.csv --last

# Search logs (returns CSV)
l-log search ./logs/example.csv "query"

# Filter by tags (returns CSV)
l-log tags ./logs/example.csv tag1 tag2

# Add a new log entry
l-log add ./logs/example.csv "Fix bug" --tags=bug,fix --problem="Problem description"
```

For human users viewing logs:

```bash
# List all log entries
l-log list ./logs/example.csv --human

# Show statistics
l-log stats ./logs/example.csv --human

# View detailed entry at index
l-log view ./logs/example.csv 0 --human

# Search logs
l-log search ./logs/example.csv "query" --human

# Filter by tags
l-log tags ./logs/example.csv tag1 tag2 --human

# Add a new log entry
l-log add ./logs/example.csv "Fix bug" --tags=bug,fix --problem="Problem description"
```

## 🤖 Ask AI agent (LLMs) to write a log

> use l-log CLI to save chat log above

## Ask AI agent (LLMs) to read a log

> read last chat logs from "./logs/example.csv" and tell me what should I do next

Example LLMs's response:

```text
Based on the last entry in ./logs/example.csv and the current state of your repository, here is what you should do next:

### Current Status

The last task completed was "Make llm-lean-log packages public". This involved:

- Updating package.json for both llm-lean-log-core and llm-lean-log-cli with repository info, files, and publishConfig.
- Adding LICENSE and README.md files.
- Configuring the CLI as an executable.
- Creating the guide at docs/public.md.

### Recommended Next Steps

1. Perform a Dry Run
Before pushing to NPM, ensure that the files being packaged are correct. Run this from the root:

...
```

## 📖 Additional information

This project was created using `bun init` in bun v1.3.5. [Bun](https://bun.com) is a fast all-in-one JavaScript runtime.

### 💻 Use with VS Code base editor

- Install recommended extensions from `.vscode/extensions.json`, which includes:
  - `DavidAnson.vscode-markdownlint` - Markdown linting
  - `biomejs.biome` - Code formatting and linting
  - `oven-sh.bun` - Bun runtime support
  - `jeff-hykin.better-csv-syntax` - CSV syntax highlighting (with color coding)
  - `YoavBls.pretty-ts-errors` - Pretty TypeScript errors

## 📄 License

MIT

```

### File: packages\core\package.json
```json
{
	"name": "llm-lean-log-core",
	"version": "0.2.5",
	"scripts": {
		"build": "bun build src/index.ts --outdir dist --target node --splitting && tsc --emitDeclarationOnly",
		"prepublishOnly": "bun run build",
		"test": "bun test",
		"example": "bun run example.ts",
		"type": "tsc --noEmit"
	},
	"description": "Core library for llm-lean-log",
	"repository": {
		"type": "git",
		"url": "git+https://github.com/loclv/llm-lean-log.git",
		"directory": "packages/core"
	},
	"bugs": {
		"url": "https://github.com/loclv/llm-lean-log/issues"
	},
	"homepage": "https://github.com/loclv/llm-lean-log/tree/main/packages/core#readme",
	"main": "dist/index.js",
	"module": "dist/index.js",
	"types": "dist/index.d.ts",
	"type": "module",
	"files": [
		"dist",
		"README.md",
		"LICENSE"
	],
	"publishConfig": {
		"access": "public"
	},
	"devDependencies": {
		"@types/bun": "latest"
	},
	"peerDependencies": {
		"typescript": "^5.9.3"
	},
	"keywords": [
		"llm",
		"logging",
		"core",
		"csv",
		"token-optimization"
	],
	"license": "MIT"
}

```

### File: packages\core\README.md
```md
# llm-lean-log-core

> 📦 Core library for llm-lean-log - Logging for LLMs, but we cut the fat.

`llm-lean-log` is a format for logging that is optimized for LLM token usage, using a simple CSV-based structure.

For more information, see the [main repository](https://github.com/loclv/llm-lean-log).

This package contains the core logic for parsing, saving, and visualizing logs in the `llm-lean-log` format.

## 🚀 Installation

```bash
bun add llm-lean-log-core
```

## 📦 Usage

### Managing Logs

```typescript
import { loadLogs, addLogEntry, saveLogs } from "llm-lean-log-core";

// Load logs
let entries = await loadLogs("logs.csv");

// Add an entry
entries = addLogEntry(entries, {
  name: "My Log",
  problem: "Something happened",
  tags: "tag1,tag2"
});

// Save logs
await saveLogs("logs.csv", entries);
```

### Visualizing Logs

```typescript
import { visualizeTable, visualizeEntry } from "llm-lean-log-core";

// Get LLM-optimized CSV output (omits empty columns)
const llmTable = visualizeTable(entries, { llm: true });

// Get Human-friendly formatted output (with colors and boxes)
const humanEntry = visualizeEntry(entries[0], { colors: true });
```

### Advanced CSV Export

```typescript
import { logEntriesToCSVMinimal } from "llm-lean-log-core";

// Export entries to CSV, automatically removing columns that are empty for all rows
const minimalCsv = logEntriesToCSVMinimal(entries);
```

## 📄 License

MIT

```

### File: packages\mcp\package.json
```json
{
	"name": "l-log-mcp",
	"version": "0.1.2",
	"type": "module",
	"main": "dist/index.js",
	"module": "dist/index.js",
	"types": "dist/index.d.ts",
	"scripts": {
		"start": "bun src/main.ts",
		"build": "bun build src/index.ts --outdir dist --target node --format esm && tsc --emitDeclarationOnly",
		"prepublishOnly": "bun run build",
		"test": "bun test"
	},
	"dependencies": {
		"@modelcontextprotocol/sdk": "^1.25.2",
		"llm-lean-log-core": "workspace:*",
		"zod": "^4.3.5"
	},
	"devDependencies": {
		"@types/bun": "latest"
	},
	"peerDependencies": {
		"typescript": "^5.9.3"
	}
}

```

### File: packages\mcp\README.md
```md
# l-log-mcp

An MCP server that exposes your `llm-lean-log` history as a queryable memory for LLMs.

## Installation

This package is part of the `llm-lean-log` monorepo.

To run the standalone server locally:

```bash
cd packages/mcp-server
bun i
bun run src/index.ts
```

### Quick Test

To verify your setup, run the server with a test log file:

```bash
LLM_LOG_PATH="/path/to/your/chat.csv" bun run src/index.ts
```

The server should start without errors and show available resources and tools.

## Configuration for Claude Desktop

Important: The MCP server requires the `LLM_LOG_PATH` environment variable to point to your chat log file.

Add this to your `claude_config.json`:

```json
{
  "mcpServers": {
    "llm-memory": {
      "command": "bun",
      "args": [
        "/absolute/path/to/llm-lean-log/packages/mcp-server/src/index.ts"
      ],
      "env": {
        "LLM_LOG_PATH": "/absolute/path/to/your/logs/chat.csv"
      }
    }
  }
}
```

## Configuration for OpenCode

Important: The MCP server requires the `LLM_LOG_PATH` environment variable to point to your chat log file.

Add this to your `opencode.json` or `.opencode.json` (usually located at `~/.opencode.json` or in your project root):

```json
{
  "mcp": {
    "llm-memory": {
      "type": "local",
      "command": [
        "bun",
        "/absolute/path/to/llm-lean-log/packages/mcp-server/src/index.ts"
      ],
      "environment": {
        "LLM_LOG_PATH": "/absolute/path/to/your/logs/chat.csv"
      }
    }
  }
}
```

### Setup Steps for OpenCode

1. Open your OpenCode configuration file (e.g., `~/.opencode.json`).
2. Add the `llm-memory` configuration inside the `mcp` object.
3. Modify the absolute paths to point to your local installation:
   - Command path: `/absolute/path/to/llm-lean-log/packages/mcp-server/src/index.ts`
   - Log path: `/absolute/path/to/your/logs/chat.csv`
4. Restart your OpenCode session.
5. Create or update `AGENTS.md` in your project root to provide instructions to the AI agent on how to use these tools (see the [AGENTS.md](../../AGENTS.md) file for an example):

```text
# Project Rules for OpenCode

This project uses `llm-lean-log` to maintain a history of development tasks. As an AI agent working on this project, you must follow these rules:

## Work Logging

Whenever you finish a task or modify code, you must log your work using the `l-log` CLI.

Command Format: `l-log add ./logs/chat.csv "<Task Name>" --tags="<tags>" --problem="<problem>" --solution="<solution>" --action="<action>" --files="<files>" --tech-stack="<tech>" --cause="<cause>" --created-by-agent="OpenCode"`

Ensure log path: `./logs/chat.csv`

## Context Retrieval (MCP)

This project has an MCP server `llm-memory` configured. Use it to retrieve context from previous tasks:

- Use `search_logs(query)` to find how previous problems were solved.
- Use `get_task_history(taskName)` to see the progression of a specific feature.
- Use the `recent_work` prompt to get an overview of what has been done recently.
- Use the `learned` prompt to review past mistakes and lessons learned to avoid repeating them.
- Use the `up` prompt to get an overview of what has been done recently.

```

## Features

### Resources

- `memory://recent`: View the last 8 log entries.
- `memory://last`: View the very last log entry with full details.
- `memory://stats`: View statistics about your logs.

### Tools

- `search_logs(query)`: Search for specific topics or errors in your history.
- `get_task_history(taskName)`: Get all logs related to a specific task.

### Prompts

- `recent_work`: A prompt template to summarize recent activities.
- `learned`: Review past mistakes and lessons learned to avoid repeating them.

## Test the MCP server

```bash
LLM_LOG_PATH="/absolute/path/to/your/logs/chat.csv" bun run src/index.ts
```

Test the MCP server by trying to run it with a simple JSON-RPC request:

```bash
 echo '{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "test", "version": "1.0"}}}' | bun src/index.ts
```

Expected response:

```txt
Starting MCP server with log path: ./logs/chat.csv
MCP Server is running on stdio
{"result":{"protocolVersion":"2024-11-05","capabilities":{"resources":{"listChanged":true},"tools":{"listChanged":true},"prompts":{"listChanged":true}},"serverInfo":{"name":"l-log-mcp-server","version":"0.1.0"}},"jsonrpc":"2.0","id":1}
```

Test the tools/list endpoint:

```bash
echo '{"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}}' | bun src/index.ts
```

Expected response:

```txt
Starting MCP server with log path: ./logs/chat.csv
MCP Server is running on stdio
{"result":{"tools":[{"name":"search_logs","description":"Search the log history for past problems, solutions, or topics.","inputSchema":{"$schema":"http://json-schema.org/draft-07/schema#","type":"object","properties":{"query":{"type":"string","description":"The search query (e.g. 'build error', 'database migration')"}},"required":["query"]},"execution":{"taskSupport":"forbidden"}},{"name":"get_task_history","description":"Get all log entries related to a specific task name.","inputSchema":{"$schema":"http://json-schema.org/draft-07/schema#","type":"object","properties":{"taskName":{"type":"string","description":"The exact or partial task name to filter by."}},"required":["taskName"]},"execution":{"taskSupport":"forbidden"}}]},"jsonrpc":"2.0","id":2}
```

Ask `search_logs "CSV parsing"`:

Expected response:

```text
I'll search the logs for "CSV parsing" to find relevant entries.

Found 2 log entries containing "CSV parsing":
1. Implement Memory MCP (2026-01-17T16:28:57.632Z)
- Tags: mcp, implementation, feature
- Problem: Need to implement the Memory MCP server as per the roadmap
- Solution: Created packages/memory-mcp, implemented basic server with Resources (recent, stats), Tools (search_logs, get_task_history), and Prompts (recent_work). Used llm-lean-log-core for CSV parsing
- Files: packages/memory-mcp/package.json, packages/memory-mcp/src/index.ts, packages/memory-mcp/src/data-access.ts, packages/memory-mcp/README.md
- Tech Stack: bun, typescript, mcp-sdk
- Agent: Antigravity
2. Verify CSV Column Order (2026-01-17T16:25:58.250Z)
- Tags: test, core, typescript
- Problem: Need to ensure CSV parsing handles arbitrary column orders and gracefully handles schema changes (missing/extra columns)
- Solution: Added order-of-col.test.ts with tests for scrambled headers, missing columns, and extra columns
- Files: packages/core/src/order-of-col.test.ts
- Tech Stack: typescript, bun-test
- Agent: Antigravity
The CSV parsing functionality is primarily implemented in the llm-lean-log-core package and used by the Memory MCP server for data access.
```

## Troubleshooting

### Common Issues

Server fails to start:

- Ensure `LLM_LOG_PATH` is set and points to a valid CSV file
- Check that the file path is absolute, not relative

Path not found errors:

- Use absolute paths in configuration files
- On macOS/Linux, paths start with `/Users/...` or `/home/...`
- On Windows, use forward slashes or escaped backslashes

Permission denied:

- Ensure the log file is readable by the user running the MCP server
- Check directory permissions for the log file location

No resources/tools available:

- Verify the server started successfully (check console output)
- Ensure the MCP client is properly configured to connect to the server

```

### File: packages\mcp_server\package.json
```json
{
	"name": "l-log-mcp-server",
	"version": "0.1.11",
	"type": "module",
	"main": "dist/index.js",
	"module": "dist/index.js",
	"types": "dist/index.d.ts",
	"bin": {
		"l-log-mcp-server": "dist/index.js"
	},
	"scripts": {
		"start": "bun dist/index.js",
		"dev": "bun --watch src/index.ts",
		"build": "bun build src/index.ts --outdir dist --target node --format esm --external @modelcontextprotocol/sdk --banner='#!/usr/bin/env node' && chmod +x dist/index.js && tsc --emitDeclarationOnly",
		"prepublishOnly": "bun run build",
		"test": "bun test",
		"postinstall": "node scripts/postinstall.js"
	},
	"files": [
		"dist",
		"scripts",
		"README.md"
	],
	"publishConfig": {
		"access": "public"
	},
	"repository": {
		"type": "git",
		"url": "git+https://github.com/loclv/llm-lean-log.git",
		"directory": "packages/mcp-server"
	},
	"dependencies": {
		"@modelcontextprotocol/sdk": "^1.25.2"
	},
	"devDependencies": {
		"@types/bun": "latest",
		"l-log-mcp": "workspace:*",
		"typescript": "^5.9.3"
	}
}

```

### File: packages\mcp_server\README.md
```md
# l-log-mcp-server

The standalone MCP (Model Context Protocol) server for `llm-lean-log`. It allows AI agents to search and access your coding task history.

## MCP server with llm-lean-log

The pairing looks like:

```text
LLM runtime
-[use CLI to write log]->
llm-lean-log (token-cheap, structured CSV)
->
mcp-server
<-[use MCP to read log]->
LLM runtime
```

`llm-lean-log` become MCP memory, which gives you:

- auditability (what did the model think last week?)
- debugging (why did it choose X?)
- analytics (token burn, drift, behavior change)
- training data for fine-tuning or evals

## How to use?

1. Install globally: `bun i -g l-log-mcp-server`.
2. Add the configuration to your AI client's config file.
3. Restart your AI client to pick up the new configuration.

## Quick Start Configuration

After installing globally, you can get the configuration snippets for your favorite AI client by running:

```bash
l-log-mcp-server --config
```

### OpenCode Configuration

Add this to your `~/.opencode.json`:

```json
{
  "mcp": {
    "llm-memory": {
      "type": "local",
      "command": ["l-log-mcp-server"],
      "environment": {
        "LLM_LOG_PATH": "/absolute/path/to/your/logs/chat.csv"
      }
    }
  }
}
```

Read more at: [docs/config-for-opencode.md](docs/config-for-opencode.md)

### Claude Desktop / Claude Code Configuration

Add this to your `claude_config.json` (Desktop) or `.claude/settings.json` (Code):

```json
{
  "mcpServers": {
    "llm-memory": {
      "command": "l-log-mcp-server",
      "env": {
        "LLM_LOG_PATH": "/absolute/path/to/your/logs/chat.csv"
      }
    }
  }
}
```

## Features / usesage

### Resources

- `memory://recent`: View the last 50 log entries from the project history.
- `memory://stats`: View statistics about your logs (total entries, last entry date, unique tags).
- `memory://last`: View the very last log entry from the project history.

Example User Prompts:

- "Show me the last 50 log entries to see what I've been working on recently"
- "What are my project statistics? How many entries do I have and what tags have I used?"
- "What was the very last thing I worked on?"

### Tools

- `search_logs(query)`: Search the log history for past problems, solutions, or topics.
- `get_task_history(taskName)`: Get all log entries related to a specific task name.

Example User Prompts:

- "Search my logs for 'database migration' using llm-memory MCP to see how I handled similar issues before"
- "Find all entries related to 'authentication system' using llm-memory MCP to understand the development history"
- "Look up any past 'build errors' using llm-memory MCP to see common solutions"
- "Look up how I solved 'TypeScript compilation errors' using llm-memory MCP in the past"

### Prompts

- `up`: A prompt for daily standup meetings - "What did I do last time and what's next?"
- `recent_work`: A prompt template to summarize recent activities based on logs.
- `learned`: Review past mistakes and lessons learned to avoid repeating them.

Example User Prompts:

- "up from llm-memory mcp"
- "recent_work from llm-memory"
- "learned from llm-memory"
- "Help me with my daily standup - what did I do last time and what's next?"
- "Summarize what I've been working on recently"
- "Based on my past mistakes, what should I be careful about in this project?"

### Postinstall

The package includes a `postinstall` script to streamline the setup process for new users.

Why it's needed: Setting up an MCP server requires specific configuration (like environment variables and command paths) that can be easily overlooked. The postinstall script provides an immediate, copy-paste-able configuration snippet tailored for your client (like OpenCode) right after installation.

How it runs: This script is triggered automatically by your package manager (`bun`, `npm`, or `yarn`) immediately after the global or local installation of `l-log-mcp-server` finishes.

Example output during installation:

```text
✨ l-log-mcp-server summary:
To use this with OpenCode, add the following to your ~/.opencode.json:
{
  "mcp": {
    "llm-memory": {
      "type": "local",
      "command": [
        "l-log-mcp-server"
      ],
      "environment": {
        "LLM_LOG_PATH": "/absolute/path/to/your/logs/chat.csv"
      }
    }
  }
}

Note: Replace /absolute/path/to/your/logs/chat.csv with the actual path to your chat.csv file.
You can also get this config anytime by running: l-log-mcp-server --config
```

### CLI Usage

```bash
l-log-mcp-server --help
```

### Install from source

```bash
cd packages/mcp-server
bun i
bun run build
```

---

For more details about the core logic, see [mcp/README.md](../mcp/README.md).

```

### File: .markdownlint.json
```json
{
	"MD013": false,
	"MD024": false,
	"MD029": false,
	"no-inline-html": false,
	"table-column-style": false
}

```

### File: AGENTS.md
```md
# Project Rules for OpenCode

This project uses `llm-lean-log` to maintain a history of development tasks. As an AI agent working on this project, you must follow these rules:

## Build & Development Commands

### Project Structure

This is a monorepo with packages in `packages/*`. Use workspace commands:

```bash
# Install dependencies
bun i

# Run all tests
bun test

# Run specific test file
bun test packages/core/src/logger.test.ts

# Run tests with coverage
bun run test:coverage

# Run tests in watch mode
bun run test:watch

# Format code
bun run fmt

# Lint code
bun run lint

# Type checking
bun run type
```

### Package-specific Commands

```bash
# Run CLI locally
bun run cli

# Run visualizer dev server
bun run web:dev

# Run MCP server in development
bun run mcp:dev

# Start MCP server
bun run mcp:start

# Run core package example
bun run example
```

## Work Logging (Required)

Whenever you finish a task or modify code, you must log your work using the `l-log` CLI:

`l-log add ./logs/chat.csv "<Task Name>" --tags="<tags>" --problem="<problem>" --solution="<solution>" --action="<action>" --files="<files>" --tech-stack="<tech>" --cause="<cause>" --created-by-agent="OpenCode"`

Ensure log path: `./logs/chat.csv`

## Context Retrieval (MCP)

This project has an MCP server `llm-memory` configured:

- `search_logs(query)` - Find how problems were solved
- `get_task_history(taskName)` - See feature progression
- `recent_work` - Overview of recent work
- `up` - Daily standup context
- `learned` - Review past mistakes

## Code Style Guidelines

### Imports & Dependencies

- Use `node:` prefix for Node.js built-ins: `import { readFile } from "node:fs/promises"`
- Prefer Bun's built-in APIs over external packages
- `Bun.file()` instead of `node:fs`
- `bun:sqlite` instead of `better-sqlite3`
- `Bun.serve()` instead of `express`
- `Bun.redis` for Redis, `Bun.sql` for Postgres
- Use `bunx <package>` instead of `npx <package>`

### Formatting

- **Indentation**: Use tabs (configured in biome.json)
- **Quotes**: Use double quotes for strings
- **Line endings**: Use LF
- **Semicolons**: Required
- **Trailing commas**: Required in multi-line structures
- Run `bun run fmt` and `bun run lint` to ensure compliance

### TypeScript Conventions

- Always provide explicit return types for functions
- Use optional chaining (`?.`) for potentially undefined properties
- Never use `any` - use `unknown` or proper typing
- Use try-catch with `console.error()` for async operations

### Naming Conventions

- **Files**: kebab-case (`csv-utils.ts`, `logger.test.ts`)
- **Functions**: camelCase (`loadLogs`, `createLogEntry`)
- **Constants**: UPPER_SNAKE_CASE for exports (`CSV_HEADERS`)
- **Types**: PascalCase (`LogEntry`, `CsvRow`)
- **Variables**: camelCase

### Function Documentation

Every function must have a JSDoc comment:

```typescript
/**
 * Load existing logs from file
 * @param filePath - Path to the CSV file containing logs
 * @returns Promise resolving to array of log entries
 */
export async function loadLogs(filePath: string): Promise<LogEntry[]> {
  // implementation
}
```

### Testing

Write unit tests for ALL new functions and bug fixes:

- Test files: `*.test.ts` in same directory as source
- Use `bun:test` with `describe`, `test`/`it`, `expect`
- Test both happy path and error cases
- Update tests when modifying source code

```typescript
import { describe, expect, it } from "bun:test";

describe("functionName", () => {
  it("should handle normal case", () => {
    // test
  });

  it("should handle errors", () => {
    // error test
  });
});
```

## Architecture Principles

- Functional programming: No classes or OOP patterns
- Pure functions preferred over methods with side effects
- Immutable data structures where possible
- Composition over inheritance
- Avoid mutation of function parameters

## Package Management

- Monorepo using Bun workspaces
- All dependencies in root `package.json` unless package-specific
- Use `devDependencies` for build tools and testing frameworks
- For CLI packages: move core dependencies to `devDependencies` and bundle

## Package-Specific Notes

### Core Package (`packages/core`)

- CSV utilities and logger functions
- All functions must be pure and testable
- TypeScript types exported for other packages

### CLI Package (`packages/cli`)

- Entry point: `src/index.ts`
- Bundle with Bun, include all dependencies

### Visualizer Package (`packages/visualizer`)

- React-based web interface
- Import LogEntry type from core package

### MCP Server Package (`packages/mcp-server`)

- Standalone MCP server for LLM memory
- Uses `llm-lean-log-core` for data access
- Configure via `LLM_LOG_PATH` environment variable

## Git Workflow

- Main branch: `main`
- Use conventional commit messages when possible
- Always include git short SHA in log entries
- Run tests and lint before committing changes

## Console Output

Use `\n` to separate multiple lines in console.log/console.warn/console.error

Remember: This file is your guide. When in doubt, check existing code for patterns and follow the established conventions.

## When change code

When change code, always update unit tests and run type check before commit.
Use `bun test` to run unit tests.
Use `bun tsc --noEmit` to run type check.

```

### File: biome.json
```json
{
	"$schema": "https://biomejs.dev/schemas/2.3.11/schema.json",
	"vcs": {
		"enabled": true,
		"clientKind": "git",
		"useIgnoreFile": true
	},
	"files": {
		"ignoreUnknown": false
	},
	"formatter": {
		"enabled": true,
		"indentStyle": "tab"
	},
	"linter": {
		"enabled": true,
		"rules": {
			"recommended": true,
			"suspicious": {
				"noArrayIndexKey": "off"
			},
			"complexity": {
				"noImportantStyles": "off"
			}
		}
	},
	"javascript": {
		"formatter": {
			"quoteStyle": "double"
		}
	},
	"assist": {
		"enabled": true,
		"actions": {
			"source": {
				"organizeImports": "on"
			}
		}
	}
}

```

### File: CHANGELOG.md
```md
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

```

### File: CONTRIBUTING.md
```md
# Contributing to llm-lean-log

Thank you for your interest in contributing to llm-lean-log. This guide will help you get started.

## Prerequisites

- Bun 1.3.5 or higher
- Git

## Getting Started

### Installation

1. Fork the repository
2. Clone your fork:

```bash
git clone https://github.com/YOUR_USERNAME/llm-lean-log.git
cd llm-lean-log
```

3. Install dependencies:

```bash
bun i
```

### Development Workflow

1. Create a new branch for your feature or bugfix:

```bash
git checkout -b feat/your-feature-name
# or
git checkout -b fix/your-bugfix-name
```

2. Make your changes

3. Run tests:

```bash
# Run all tests
bun test

# Run specific test file
bun test packages/core/src/logger.test.ts

# Run tests in watch mode
bun run test:watch

# Run tests with coverage
bun run test:coverage
```

4. Format code:

```bash
bun run fmt
```

5. Lint code:

```bash
bun run lint
```

6. Type checking:

```bash
bun run type
```

7. Commit your changes

8. Push to your fork and create a pull request

## Project Structure

```text
llm-lean-log/
├── packages/
│   ├── core/          # Core library (CSV utilities, logging)
│   ├── cli/           # CLI application
│   ├── visualizer/    # React-based web visualizer
│   ├── mcp/           # MCP server core logic
│   └── mcp-server/    # Standalone MCP server
├── docs/              # Documentation
├── AGENTS.md          # Guide for AI agents
└── package.json       # Root package.json
```

## Code Style Guidelines

### General Principles

- Use functional programming approach (no classes or OOP patterns)
- Pure functions preferred over methods with side effects
- Immutable data structures where possible
- Composition over inheritance
- Avoid mutation of function parameters

### TypeScript

- Always provide explicit return types for functions
- Use optional chaining (`?.`) for potentially undefined properties
- Never use `any` - use `unknown` or proper typing
- Use try-catch with `console.error()` for async operations

### Naming Conventions

- **Files**: kebab-case (`csv-utils.ts`, `logger.test.ts`)
- **Functions**: camelCase (`loadLogs`, `createLogEntry`)
- **Constants**: UPPER_SNAKE_CASE for exports (`CSV_HEADERS`)
- **Types**: PascalCase (`LogEntry`, `CsvRow`)
- **Variables**: camelCase

### Formatting

- **Indentation**: Use tabs (configured in biome.json)
- **Quotes**: Use double quotes for strings
- **Line endings**: Use LF
- **Semicolons**: Required
- **Trailing commas**: Required in multi-line structures

Run `bun run fmt` to format code automatically.

### Comments

Every function must have a JSDoc comment:

```typescript
/**
 * Load existing logs from file
 * @param filePath - Path to the CSV file containing logs
 * @returns Promise resolving to array of log entries
 */
export async function loadLogs(filePath: string): Promise<LogEntry[]> {
  // implementation
}
```

### Bun Usage

- Use `bun run <file>` instead of `node <file>` or `ts-node <file>`
- Use `bun i` instead of `npm install` or `yarn install` or `pnpm install`
- Use `bun run <script>` instead of `npm run <script>` or `yarn run <script>` or `pnpm run <script>`
- Use `bunx <package>` instead of `npx <package>`
- Bun automatically loads `.env` files - no dotenv needed

### Bun APIs

- `Bun.file()` instead of `node:fs` for file operations
- `bun:sqlite` instead of `better-sqlite3`
- `Bun.serve()` instead of `express`
- `Bun.redis` for Redis
- `Bun.sql` for Postgres
- `WebSocket` is built-in - don't use `ws`

## Testing

### Writing Tests

Write unit tests for ALL new functions and bug fixes:

- Test files: `*.test.ts` in same directory as source
- Use `bun:test` with `describe`, `test`/`it`, `expect`
- Test both happy path and error cases
- Update tests when modifying source code

Example:

```typescript
import { describe, expect, it } from "bun:test";

describe("functionName", () => {
  it("should handle normal case", () => {
    // test implementation
  });

  it("should handle errors", () => {
    // error test implementation
  });
});
```

### Running Tests

```bash
# Run all tests
bun test

# Run specific test file
bun test packages/core/src/logger.test.ts

# Run tests in watch mode
bun run test:watch

# Run tests with coverage
bun run test:coverage
```

## Package-Specific Guidelines

### Core Package

- Contains CSV utilities and logger functions
- All functions must be pure and testable
- TypeScript types exported for other packages

### CLI Package

- Entry point: `src/index.ts`
- Bundle with Bun, include all dependencies
- Test CLI commands with integration tests

### Visualizer Package

- React-based web interface
- Import LogEntry type from core package
- Use Vite for development builds

### MCP Server Package

- Standalone MCP server for LLM memory
- Uses `llm-lean-log-core` for data access
- Configure via `LLM_LOG_PATH` environment variable

## Git Workflow

### Commit Messages

Use conventional commit messages when possible:

- `feat: add new feature`
- `fix: fix bug`
- `docs: update documentation`
- `style: format code`
- `refactor: refactor code`
- `test: add tests`
- `chore: update dependencies`

### Branch Naming

- `feature/feature-name`
- `fix/bug-fix-name`
- `docs/documentation-update`
- `refactor/refactoring-description`

### Pull Request Process

1. Ensure your code passes all tests: `bun test`
2. Format your code: `bun run fmt`
3. Lint your code: `bun run lint`
4. Type check: `bun run type`
5. Update documentation if needed
6. Submit a pull request with a clear description of your changes

## LLM Token Optimization

This project is optimized for LLM token usage. When making changes:

- CSV format should remain simple and predictable for LLMs
- Avoid unnecessary complexity in log entries
- Consider token overhead when adding new features
- Maintain backward compatibility with existing CSV files

## Logging Your Work

If you're an AI agent contributing to this project, you must log your work using the `l-log` CLI:

```bash
l-log add ./logs/chat.csv "<Task Name>" --tags="<tags>" --problem="<problem>" --solution="<solution>" --action="<action>" --files="<files>" --tech-stack="<tech>" --created-by-agent="<agent-name>"
```

Ensure log path: `./logs/chat.csv`

## Questions?

Feel free to open an issue if you have questions or need clarification.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
