---
trigger: always_on
---

# Codebase Overview Quick Reference

## Project Summary

This is a monorepo called `llm-lean-log` for maintaining development task history. It provides logging, CLI, web visualizer, and MCP server components.

## Package Structure

- core/ # CSV utilities, logger functions, types (pure functions)
- cli/ # Command-line interface (entry: src/index.ts)
- visualizer/ # React web interface
- mcp-server/ # MCP server for LLM memory
- mcp/ # MCP related code

## Key Files to Know

- Root config: `package.json` (workspace), `biome.json` (formatting/linting)
- Agent rules: `.agent/rules/*.md` (auto-loaded for all agents)
- Project rules: `AGENTS.md` (OpenCode configuration)
- Log path: `./logs/chat.csv`

## Essential Commands

```bash
bun i # Install dependencies
bun test # Run all tests
bun test <file> # Run specific test
bun run fmt # Format code
bun run lint # Lint code
bun run type # Type check
bun run cli # Run CLI locally
bun run web:dev # Run visualizer dev server
bun run mcp:dev # Run MCP server in dev mode
```

## Code Conventions (Must Follow)

- Functional programming: No classes, use pure functions
- TypeScript: Explicit return types, no `any`, use `unknown` or proper typing
- Naming: kebab-case files, camelCase functions, PascalCase types, UPPER_SNAKE constants
- Formatting: Tabs, double quotes, trailing commas required
- Console: Use `\n` for multi-line output

## Testing Rules

- All new functions need unit tests (`*.test.ts` in same directory)
- Use `bun:test` with `describe`, `it`, `expect`
- Test both happy path and error cases

## Common Patterns

```typescript
// Async function with proper typing
export async function loadLogs(filePath: string): Promise<LogEntry[]> {
  try {
    // implementation
  } catch (error) {
    console.error("Failed to load logs:", error);
    throw error;
  }
}

// Use Bun built-ins
import { file } from "bun";
const data = await file("path").text();
```

## Context Retrieval

Use MCP server tools:

- `search_logs(query)` - Find how problems were solved
- `get_task_history(taskName)` - See feature progression
- `recent` - Overview of recent work
- `learned` - Review past mistakes

## Work Logging

Always log your work after:

```bash
l-log add ./logs/chat.csv "<Task Name>" --tags="<tags>" --problem="<problem>" --solution="<solution>" --action="<action>" --files="<files>" --tech-stack="<tech>" --created-by-agent="<agent-name>"
```

For more details, see `AGENTS.md`.
