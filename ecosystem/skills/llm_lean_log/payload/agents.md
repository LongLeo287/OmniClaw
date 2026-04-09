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
