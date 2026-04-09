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
