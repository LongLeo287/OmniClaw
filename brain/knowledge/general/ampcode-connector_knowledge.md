# Knowledge Dump for ampcode-connector

## File: agents.md
```
# AGENTS.md — ampcode-connector

## Build & Run
- Install: `bun install` | Start: `bun start` | Dev: `bun run dev` (with --watch)
- Format: `bun run format` | Check: `bun run check` | E2E: `bun run test:e2e`
- **Always `bun run format` before `bun run check`.**

## Architecture
TypeScript + Bun runtime, ESM-only, strict TS. Proxy intercepts Amp CLI requests at `/api/provider/{provider}/v1/...`, routes to local OAuth providers (anthropic, codex, gemini, antigravity) or falls back to Amp upstream. Non-provider routes forwarded to ampcode.com as-is. SSE streaming passthrough with model name rewriting. Config in `config.yaml` (YAML loaded via Bun.YAML). Entry point: `src/index.ts`. Key dirs: `src/auth/` (OAuth PKCE + token refresh), `src/providers/` (per-provider handlers), `src/routing/` (route decision + affinity + cooldown), `src/proxy/` (upstream proxy + SSE rewriter), `src/server/` (Bun.serve HTTP server), `src/config/`, `src/utils/`, `src/cli/`. Tests in `tests/`.

## Code Style (enforced by Biome + tsc)
- 2-space indent, double quotes, semicolons always, trailing commas, 120 char line width
- Biome linter: `recommended` rules enabled. Disabled: `noForEach`, `noExplicitAny`, `noNonNullAssertion`, `useNodejsImportProtocol`
- tsc strict mode with `noUnusedLocals` and `noUnusedParameters` enabled — no unused code allowed
- Imports: use `type` keyword for type-only imports (`import { type Foo, bar }`), include `.ts` extensions. Biome enforces alphabetical import sorting
- Prefer `const` over `let`. Prefix intentionally unused params with `_`
- Use `async/await`, not callbacks. Functions return `Promise<void>` or explicit types
- Each provider implements the `Provider` interface from `src/providers/base.ts`
- Log routing decisions: `LOCAL_CLAUDE`, `LOCAL_CODEX`, `LOCAL_GEMINI`, `LOCAL_ANTIGRAVITY`, `AMP_UPSTREAM`
- No external frameworks — uses Bun built-ins (Bun.serve, Bun.YAML, fetch)

## Design Principles
- **Strict type safety** — Never bypass type errors; no implicit `any`. Fix types, don't cast around them
- **Clear boundaries** — Respect layer separation (CLI → server → routing → providers → auth). Do not call across layers directly
- **Environment-agnostic** — Utilities and core logic must not depend on specific runtime details; isolate platform-specific code at the edges

## Analysis Rules
- **Verify before flagging** — Do not report a problem (circular deps, dead code, missing coverage) without tool evidence (`Grep` tool, `bun run check`, test runs). If one check can disprove the claim, run it first.
- **Actionable only** — Every issue raised must have a concrete fix with clear scope. "Needs more tests" is not actionable; "forward.ts lacks retry exhaustion test" is.

## Important
- **Do NOT modify `references/`** — read-only reference code from external projects (oh-my-pi-ai proxy + CLIProxyAPI patterns used as architectural reference)
- Dependencies: `@google/genai`, `exa-js`, `@kreuzberg/html-to-markdown`. Prefer Bun built-ins over npm packages

```

## File: biome.json
```
{
  "$schema": "https://biomejs.dev/schemas/2.4.0/schema.json",
  "files": {
    "includes": ["src/**", "tests/**", "*.json", "*.toml"]
  },
  "formatter": {
    "enabled": true,
    "indentStyle": "space",
    "indentWidth": 2,
    "lineWidth": 120
  },
  "linter": {
    "enabled": true,
    "rules": {
      "recommended": true,
      "complexity": {
        "noForEach": "off"
      },
      "suspicious": {
        "noExplicitAny": "off"
      },
      "style": {
        "noNonNullAssertion": "off",
        "useNodejsImportProtocol": "off"
      }
    }
  },
  "javascript": {
    "formatter": {
      "quoteStyle": "double",
      "semicolons": "always",
      "trailingCommas": "all"
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

## File: config.example.yaml
```
# ampcode-connector configuration
# Copy to ./config.yaml or ~/.config/ampcode-connector/config.yaml
# Amp CLI settings are managed at ~/.config/amp/settings.json (or AMP_SETTINGS_FILE)

port: 8765
logLevel: info

# ampUpstreamUrl: https://ampcode.com
# ampApiKey: ...          # optional override; normally read from ~/.local/share/amp/secrets.json
# exaApiKey: ...          # or EXA_API_KEY env (for web_search)

providers:
  anthropic: true
  codex: true
  google: true

```

## File: docker-compose.yml
```
services:
  ampcode-connector:
    build: .
    ports:
      - "7860:7860"
    volumes:
      - ./config.yaml:/app/config.yaml:ro
      - credentials:/root/.ampcode-connector
    restart: unless-stopped

volumes:
  credentials:

```

## File: package.json
```
{
  "name": "ampcode-connector",
  "version": "0.1.21",
  "description": "Proxy AmpCode through local OAuth subscriptions (Claude Code, Codex, Gemini CLI, Antigravity)",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/nghyane/ampcode-connector"
  },
  "keywords": [
    "amp",
    "ampcode",
    "proxy",
    "claude",
    "openai",
    "gemini",
    "oauth"
  ],
  "module": "src/index.ts",
  "type": "module",
  "files": [
    "src/**/*.ts",
    "config.yaml",
    "tsconfig.json"
  ],
  "publishConfig": {
    "access": "public"
  },
  "bin": {
    "ampcode-connector": "src/index.ts"
  },
  "scripts": {
    "start": "bun run src/index.ts",
    "dev": "bun run --watch src/index.ts",
    "setup": "bun run src/index.ts setup",
    "login": "bun run src/index.ts login",
    "test": "bun test tests/router.test.ts tests/middleware.test.ts tests/rewriter.test.ts tests/forward.test.ts",
    "test:e2e": "bun test tests/code-assist.test.ts",
    "check": "biome check src/ tests/ && tsc --noEmit && bun run test",
    "format": "biome check --write src/ tests/"
  },
  "devDependencies": {
    "@biomejs/biome": "^2.4.2",
    "@google/genai": "^1.42.0",
    "@types/bun": "^1.3.9",
    "@types/turndown": "^5.0.6"
  },
  "peerDependencies": {
    "typescript": "^5.9.3"
  },
  "dependencies": {
    "@anthropic-ai/sdk": "0.74.0",
    "exa-js": "^2.4.0",
    "turndown": "^7.2.2",
    "turndown-plugin-gfm": "^1.0.2"
  }
}

```

## File: README.md
```
# ampcode-connector

Route [AmpCode](https://ampcode.com) through your existing Claude Code, Codex CLI & Gemini CLI subscriptions.

```bash
bunx ampcode-connector setup    # point AmpCode → proxy
bunx ampcode-connector login    # authenticate providers
bunx ampcode-connector          # start
```

Requires [Bun](https://bun.sh) 1.3+. Config at `./config.yaml` or `~/.config/ampcode-connector/config.yaml` — see `config.example.yaml`.

`setup` writes `amp.url` to Amp's canonical settings file (`~/.config/amp/settings.json`, or `AMP_SETTINGS_FILE` if set). Amp tokens are stored in `~/.local/share/amp/secrets.json`.

## License

MIT

```

## File: tsconfig.json
```
{
  "compilerOptions": {
    // Environment setup & latest features
    "lib": ["ESNext"],
    "target": "ESNext",
    "module": "Preserve",
    "moduleDetection": "force",
    "jsx": "react-jsx",
    "allowJs": true,

    // Bundler mode
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "verbatimModuleSyntax": false,
    "noEmit": true,

    // Best practices
    "strict": true,
    "skipLibCheck": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,

    // Some stricter flags (disabled by default)
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noPropertyAccessFromIndexSignature": false
  },
  "exclude": ["references"]
}

```

## File: _GIT_INGEST.md
```
# OmniClaw Repo Plow: CIV_FETCHED_ampcode-connector_150454



================================================
FILE: AGENTS.md
================================================
# AGENTS.md — ampcode-connector

## Build & Run
- Install: `bun install` | Start: `bun start` | Dev: `bun run dev` (with --watch)
- Format: `bun run format` | Check: `bun run check` | E2E: `bun run test:e2e`
- **Always `bun run format` before `bun run check`.**

## Architecture
TypeScript + Bun runtime, ESM-only, strict TS. Proxy intercepts Amp CLI requests at `/api/provider/{provider}/v1/...`, routes to local OAuth providers (anthropic, codex, gemini, antigravity) or falls back to Amp upstream. Non-provider routes forwarded to ampcode.com as-is. SSE streaming passthrough with model name rewriting. Config in `config.yaml` (YAML loaded via Bun.YAML). Entry point: `src/index.ts`. Key dirs: `src/auth/` (OAuth PKCE + token refresh), `src/providers/` (per-provider handlers), `src/routing/` (route decision + affinity + cooldown), `src/proxy/` (upstream proxy + SSE rewriter), `src/server/` (Bun.serve HTTP server), `src/config/`, `src/utils/`, `src/cli/`. Tests in `tests/`.

## Code Style (enforced by Biome + tsc)
- 2-space indent, double quotes, semicolons always, trailing commas, 120 char line width
- Biome linter: `recommended` rules enabled. Disabled: `noForEach`, `noExplicitAny`, `noNonNullAssertion`, `useNodejsImportProtocol`
- tsc strict mode with `noUnusedLocals` and `noUnusedParameters` enabled — no unused code allowed
- Imports: use `type` keyword for type-only imports (`import { type Foo, bar }`), include `.ts` extensions. Biome enforces alphabetical import sorting
- Prefer `const` over `let`. Prefix intentionally unused params with `_`
- Use `async/await`, not callbacks. Functions return `Promise<void>` or explicit types
- Each provider implements the `Provider` interface from `src/providers/base.ts`
- Log routing decisions: `LOCAL_CLAUDE`, `LOCAL_CODEX`, `LOCAL_GEMINI`, `LOCAL_ANTIGRAVITY`, `AMP_UPSTREAM`
- No external frameworks — uses Bun built-ins (Bun.serve, Bun.YAML, fetch)

## Design Principles
- **Strict type safety** — Never bypass type errors; no implicit `any`. Fix types, don't cast around them
- **Clear boundaries** — Respect layer separation (CLI → server → routing → providers → auth). Do not call across layers directly
- **Environment-agnostic** — Utilities and core logic must not depend on specific runtime details; isolate platform-specific code at the edges

## Analysis Rules
- **Verify before flagging** — Do not report a problem (circular deps, dead code, missing coverage) without tool evidence (`Grep` tool, `bun run check`, test runs). If one check can disprove the claim, run it first.
- **Actionable only** — Every issue raised must have a concrete fix with clear scope. "Needs more tests" is not actionable; "forward.ts lacks retry exhaustion test" is.

## Important
- **Do NOT modify `references/`** — read-only reference code from external projects (oh-my-pi-ai proxy + CLIProxyAPI patterns used as architectural reference)
- Dependencies: `@google/genai`, `exa-js`, `@kreuzberg/html-to-markdown`. Prefer Bun built-ins over npm packages


================================================
FILE: biome.json
================================================
{
  "$schema": "https://biomejs.dev/schemas/2.4.0/schema.json",
  "files": {
    "includes": ["src/**", "tests/**", "*.json", "*.toml"]
  },
  "formatter": {
    "enabled": true,
    "indentStyle": "space",
    "indentWidth": 2,
    "lineWidth": 120
  },
  "linter": {
    "enabled": true,
    "rules": {
      "recommended": true,
      "complexity": {
        "noForEach": "off"
      },
      "suspicious": {
        "noExplicitAny": "off"
      },
      "style": {
        "noNonNullAssertion": "off",
        "useNodejsImportProtocol": "off"
      }
    }
  },
  "javascript": {
    "formatter": {
      "quoteStyle": "double",
      "semicolons": "always",
      "trailingCommas": "all"
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


================================================
FILE: package.json
================================================
{
  "name": "ampcode-connector",
  "version": "0.1.21",
  "description": "Proxy AmpCode through local OAuth subscriptions (Claude Code, Codex, Gemini CLI, Antigravity)",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/nghyane/ampcode-connector"
  },
  "keywords": [
    "amp",
    "ampcode",
    "proxy",
    "claude",
    "openai",
    "gemini",
    "oauth"
  ],
  "module": "src/index.ts",
  "type": "module",
  "files": [
    "src/**/*.ts",
    "config.yaml",
    "tsconfig.json"
  ],
  "publishConfig": {
    "access": "public"
  },
  "bin": {
    "ampcode-connector": "src/index.ts"
  },
  "scripts": {
    "start": "bun run src/index.ts",
    "dev": "bun run --watch src/index.ts",
    "setup": "bun run src/index.ts setup",
    "login": "bun run src/index.ts login",
    "test": "bun test tests/router.test.ts tests/middleware.test.ts tests/rewriter.test.ts tests/forward.test.ts",
    "test:e2e": "bun test tests/code-assist.test.ts",
    "check": "biome check src/ tests/ && tsc --noEmit && bun run test",
    "format": "biome check --write src/ tests/"
  },
  "devDependencies": {
    "@biomejs/biome": "^2.4.2",
    "@google/genai": "^1.42.0",
    "@types/bun": "^1.3.9",
    "@types/turndown": "^5.0.6"
  },
  "peerDependencies": {
    "typescript": "^5.9.3"
  },
  "dependencies": {
    "@anthropic-ai/sdk": "0.74.0",
    "exa-js": "^2.4.0",
    "turndown": "^7.2.2",
    "turndown-plugin-gfm": "^1.0.2"
  }
}


================================================
FILE: README.md
================================================
# ampcode-connector

Route [AmpCode](https://ampcode.com) through your existing Claude Code, Codex CLI & Gemini CLI subscriptions.

```bash
bunx ampcode-connector setup    # point AmpCode → proxy
bunx ampcode-connector login    # authenticate providers
bunx ampcode-connector          # start
```

Requires [Bun](https://bun.sh) 1.3+. Config at `./config.yaml` or `~/.config/ampcode-connector/config.yaml` — see `config.example.yaml`.

`setup` writes `amp.url` to Amp's canonical settings file (`~/.config/amp/settings.json`, or `AMP_SETTINGS_FILE` if set). Amp tokens are stored in `~/.local/share/amp/secrets.json`.

## License

MIT


================================================
FILE: tsconfig.json
================================================
{
  "compilerOptions": {
    // Environment setup & latest features
    "lib": ["ESNext"],
    "target": "ESNext",
    "module": "Preserve",
    "moduleDetection": "force",
    "jsx": "react-jsx",
    "allowJs": true,

    // Bundler mode
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "verbatimModuleSyntax": false,
    "noEmit": true,

    // Best practices
    "strict": true,
    "skipLibCheck": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,

    // Some stricter flags (disabled by default)
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noPropertyAccessFromIndexSignature": false
  },
  "exclude": ["references"]
}


================================================
FILE: amp-extractions-latest\README.md
================================================
# Amp CLI Extractions (Latest Local Binary)

This directory is a refreshed extraction snapshot built from the latest local Amp CLI binary.

## Source

- **Binary:** `~/.amp/bin/amp`
- **Version detected:** `0.0.1773129970-gb3ab74`
- **Generated:** 2026-03-10

## Files

- `config/settings.md` — settings registry from help + internal `UE0` object (public + hidden keys)
- `config/endpoints.md` — endpoint and service URL candidates from binary strings scan
- `agents/agent-tools.md` — full tool descriptions and schemas from `amp tools show`
- `agents/agent-architecture.md` — mode tool matrix + mode/subagent model mapping

## Notes

- This folder is separate from `references/` to avoid modifying read-only reference content.
- Endpoint extraction is static/best-effort; verify runtime traffic if you need exact invocation behavior.


================================================
FILE: amp-extractions-latest\agents\agent-architecture.md
================================================
# AMP CLI Agent Architecture Notes (Latest Binary)

- **Source binary:** `~/.amp/bin/amp`
- **Version:** `0.0.1773129970-gb3ab74 (released 2026-03-10T08:11:50.960Z, 2h ago)`
- **Extraction date:** 2026-03-10T11:07:32.130Z
- **Method:** `amp tools list --json --mode <mode>` + binary strings extraction (objects `Xy` and `Wt`).

## Tool Availability By Mode

| Mode | Tool Count | Tools |
|---|---:|---|
| `smart` | 23 | `Bash`, `chart`, `create_file`, `edit_file`, `find_thread`, `finder`, `glob`, `Grep`, `handoff`, `librarian`, `look_at`, `mermaid`, `oracle`, `painter`, `Read`, `read_mcp_resource`, `read_thread`, `read_web_page`, `skill`, `Task`, `task_list`, `undo_edit`, `web_search` |
| `deep` | 13 | `apply_patch`, `chart`, `find_thread`, `finder`, `handoff`, `librarian`, `oracle`, `painter`, `read_thread`, `read_web_page`, `shell_command`, `skill`, `web_search` |
| `rush` | 23 | `Bash`, `chart`, `create_file`, `edit_file`, `find_thread`, `finder`, `glob`, `Grep`, `handoff`, `librarian`, `look_at`, `mermaid`, `oracle`, `painter`, `Read`, `read_mcp_resource`, `read_thread`, `read_web_page`, `skill`, `Task`, `task_list`, `undo_edit`, `web_search` |
| `free` | 15 | `Bash`, `chart`, `create_file`, `edit_file`, `find_thread`, `finder`, `glob`, `Grep`, `mermaid`, `Read`, `read_thread`, `read_web_page`, `skill`, `task_list`, `web_search` |

## Primary Model By Agent Mode

| Mode | Primary Model Constant |
|---|---|
| `smart` | `CLAUDE_OPUS_4_6` |
| `free` | `CLAUDE_HAIKU_4_5` |
| `rush` | `CLAUDE_HAIKU_4_5` |
| `agg-man` | `CLAUDE_OPUS_4_6` |
| `large` | `CLAUDE_SONNET_4_6` |
| `deep` | `GPT_5_3_CODEX` |
| `internal` | `GPT_5_4` |

## Subagent Model Mapping

| Subagent | Model Constant |
|---|---|
| `finder` | `CLAUDE_HAIKU_4_5` |
| `oracle` | `GPT_5_4` |
| `librarian` | `CLAUDE_SONNET_4_6` |
| `task-subagent` | `(dynamic/default)` |
| `code-review` | `CLAUDE_SONNET_4_5` |
| `code-tour` | `CLAUDE_OPUS_4_6` |
| `codereview-check` | `CLAUDE_HAIKU_4_5` |

## Notes

- Full assembled system prompts are not publicly retrievable in this environment (`amp tools list --inspect` returns permission denied).
- This file complements `agents/agent-tools.md` with mode/subagent model mapping inferred from binary internals.


================================================
FILE: amp-extractions-latest\agents\agent-tools.md
================================================
# AMP CLI Agent Tools (Latest Binary)

- **Source binary:** `~/.amp/bin/amp`
- **Version:** `0.0.1773129970-gb3ab74 (released 2026-03-10T08:11:50.960Z, 2h ago)`
- **Extraction date:** 2026-03-10T11:05:25.332Z
- **Method:** `amp tools list` + `amp tools show <tool>`.

## Active Tools List

```text
23 tools available

Built-in
  Bash               Executes the given shell command using bash (or sh on systems without bash)
  chart              Render a chart visualization by running a command that produces JSON data
  create_file        Create or overwrite a file in the workspace
  edit_file          Make edits to a text file
  find_thread        Find Amp threads (conversation threads with the agent) using a query DSL
  finder             Intelligently search your codebase
  glob               Fast file pattern matching tool that works with any codebase size
  Grep               Search for exact text patterns in files using ripgrep, a fast keyword search tool
  handoff            Hand off work to a new thread that runs in the background
  librarian          The Librarian - a specialized codebase understanding agent that helps answer questions about large, complex codebases
  look_at            Extract specific information from a local file (including PDFs, images, and other media)
  mermaid            Renders a Mermaid diagram from the provided code
  oracle             Consult the oracle - an AI advisor powered by OpenAI's GPT-5
  painter            Generate an image using an AI model
  Read               Read a file or list a directory from the file system
  read_mcp_resource  Read a resource from an MCP (Model Context Protocol) server
  read_thread        Read and extract relevant content from another Amp thread by its ID
  read_web_page      Read the contents of a web page at a given URL
  skill              Load a specialized skill that provides domain-specific instructions and workflows
  Task               Perform a task (a sub-task of the user's overall task) using a sub-agent that has access to the following tools
  task_list          Plan and track tasks
  undo_edit          Undo the last edit made to a file
  web_search         Search the web for information relevant to a research objective
```

## Tool Definitions (Full Dump)

```text
===== TOOL: Bash =====
# Bash (built-in)

Executes the given shell command using bash (or sh on systems without bash).

- Do NOT chain commands with `;` or `&&` or use `&` for background processes; make separate tool calls instead
- Do NOT use interactive commands (REPLs, editors, password prompts)
- Output is truncated to the last 50000 characters
- Environment variables and `cd` do not persist between commands; use the `cwd` parameter instead
- Commands run in the workspace root by default; only use `cwd` when you need a different directory (never use `cd dir && cmd`)
- Only the last 50000 characters of the output will be returned to you along with how many lines got truncated, if any; rerun with a grep or head/tail filter if needed
- On Windows, use PowerShell commands and `\` path separators
- ALWAYS quote file paths: `cat "path with spaces/file.txt"`
- Use finder/Grep instead of find/grep, Read instead of cat, edit_file instead of sed
- Only run `git commit` and `git push` if explicitly instructed by the user.


# Schema

- cmd (string): The shell command to execute
- cwd (string): Absolute path to a directory where the command will be executed (must be absolute, not relative)


===== TOOL: chart =====
# chart (built-in)

Render a chart visualization by running a command that produces JSON data. The chart is displayed inline to the user.

Use this tool to visualize data as bar charts, line charts, or area charts. You provide a shell command that outputs JSON, and specify which columns map to the X and Y axes, the chart type, and display options.

# Parameters

- **cmd**: A shell command to execute that must produce JSON output (a JSON array of objects). The command is run via the Bash tool internally. Pipe through `jq -c .` if needed to produce compact JSON.
- **chartType**: "bar", "line", or "area"
- **xColumn**: The column name to use for the X axis (labels)
- **yColumns**: Array of column names for the Y axis. Multiple columns create multiple series (e.g., overlay revenue and expenses on the same chart).
- **title**: Chart title displayed above the chart
- **stacked**: When true with multiple yColumns, stack the series instead of overlaying them. Works with bar and area charts.
- **horizontal**: When true with bar chartType, renders horizontal bars (good for categorical data with long labels).
- **hoverColumns**: Extra column names to show in the hover tooltip but not plotted on the Y axis.
- **groupColumn**: A column whose unique values become separate series. Use with a single yColumn to pivot unpivoted data — e.g., rows with a "type" column become one series per type. Commonly used with stacked charts.

# When to use this tool

- When the user explicitly as

================================================
FILE: amp-extractions-latest\config\endpoints.md
================================================
# AMP CLI Endpoints Reference (Latest Binary)

- **Source binary:** `~/.amp/bin/amp`
- **Version:** `0.0.1773129970-gb3ab74 (released 2026-03-10T08:11:50.960Z, 2h ago)`
- **Extraction date:** 2026-03-10T11:04:35.859Z
- **Method:** static strings scan from binary (best-effort).

## Provider Proxy Paths

- `/api/provider/anthropic`
- `/api/provider/baseten/v1`
- `/api/provider/cerebras`
- `/api/provider/fireworks/v1`
- `/api/provider/google`
- `/api/provider/groq`
- `/api/provider/kimi`
- `/api/provider/openai/v1`
- `/api/provider/xai/v1`

## Other API Path Candidates

- `/api/1.0/projects/`
- `/api/1.0/repos`
- `/api/durable-thread-workers`
- `/api/events`
- `/api/hello`
- `/api/hello/:name`
- `/api/http`
- `/api/internal`
- `/api/internal/bitbucket-instance-url`
- `/api/internal/github-auth-status`
- `/api/internal/github-proxy/`
- `/api/session`
- `/api/sessions`
- `/api/telemetry`
- `/api/threads`
- `/api/threads/`
- `/api/threads/find`
- `/api/threads/sync`
- `/api/users/:id`
- `/api/v1`
- `/api/v2/`
- `/api/v2/spans`

## Related Service URLs Found

- `http://localhost:4318/`
- `http://localhost:9411/api/v2/spans`
- `https://aiplatform.googleapis.com/`
- `https://ampcode.com`
- `https://ampcode.com/`
- `https://ampcode.com/manual`
- `https://ampcode.com/manual/appendix`
- `https://ampcode.com/models`
- `https://ampcode.com/news/stick-a-fork-in-it`
- `https://ampcode.com/settings`
- `https://ampcode.com/threads/`
- `https://ampcode.com/threads/T-3f1beb2b-bded-4fda-96cc-1af7192f24b6`
- `https://ampcode.com/threads/T-5928a90d-d53b-488f-a829-4e36442142ee`
- `https://ampcode.com/threads/T-95e73a95-f4fe-4f22-8d5c-6297467c97a5`
- `https://ampcode.com/threads/T-f916b832-c070-4853-8ab3-5e7596953bec`
- `https://ampcode.com/threads/T-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`
- `https://api.anthropic.com`
- `https://api.anthropic.com/`
- `https://api.cerebras.ai`
- `https://api.openai.com/v1`
- `https://generativelanguage.googleapis.com`
- `https://generativelanguage.googleapis.com/`
- `https://openrouter.ai/api/v1`
- `https://storage.googleapis.com/amp-public-assets-prod-0/cli`
- `https://storage.googleapis.com/amp-public-assets-prod-0/cli/cli-version.txt`
- `https://storage.googleapis.com/amp-public-assets-prod-0/jetbrains/latest.json`
- `https://storage.googleapis.com/amp-public-assets-prod-0/ripgrep/ripgrep-binaries/`

## Notes

- Static string extraction can include dead code or SDK/internal paths.
- Use runtime logging/proxy capture to verify which endpoints are actually invoked in your environment.


================================================
FILE: amp-extractions-latest\config\settings.md
================================================
# AMP CLI Settings Reference (Latest Binary)

- **Source binary:** `~/.amp/bin/amp`
- **Version:** `0.0.1773129970-gb3ab74 (released 2026-03-10T08:11:50.960Z, 2h ago)`
- **Extraction date:** 2026-03-10T11:04:01.398Z
- **Method:** `amp --help` + binary strings extraction of internal settings registry object `UE0`.

## Summary

- **Total registry settings:** 42
- **Visible/public settings:** 23
- **Internal/hidden settings:** 19

## Public Settings

| Key | Default | Description |
|---|---|---|
| `amp.agent.deepReasoningEffort` | `high` | Default GPT-5.3 Codex reasoning effort for new deep-mode threads (medium, high, xhigh). |
| `amp.bitbucketToken` | `undefined` | Personal access token for Bitbucket Enterprise. Used with a workspace-level Bitbucket connection configured by an admin. |
| `amp.dangerouslyAllowAll` | `false` | Disable all command confirmation prompts (agent will execute all commands without asking) |
| `amp.defaultVisibility` | `{"github.com/sourcegraph/amp":"workspace"}` | Define default thread visibility per repository origin using mappings like "github.com/org/repo": "workspace". Values: private, public, workspace, group. |
| `amp.experimental.modes` | `[]` | Enable experimental agent modes by name. Available modes: deep |
| `amp.fuzzy.alwaysIncludePaths` | `[]` | Glob patterns for paths that should always be included in fuzzy file search, even if gitignored |
| `amp.git.commit.ampThread.enabled` | `true` | Enable adding Amp-Thread trailer in git commits |
| `amp.git.commit.coauthor.enabled` | `true` | Enable adding Amp as co-author in git commits |
| `amp.guardedFiles.allowlist` | `[]` | Array of file glob patterns that are allowed to be accessed without confirmation. Takes precedence over the built-in denylist. |
| `amp.mcpServers` | `{"filesystem":{"command":"npx","args":["@modelcontextprotocol/server-filesystem","/path/to/allowed/dir"]}}` | Model Context Protocol servers to connect to for additional tools |
| `amp.network.timeout` | `30` | How many seconds to wait for network requests to the Amp server before timing out |
| `amp.notifications.enabled` | `true` | Enable system sound notifications when agent completes tasks |
| `amp.notifications.system.enabled` | `true` | Enable system notifications when terminal is not focused |
| `amp.permissions` | `[{"tool":"Bash","action":"ask","matches":{"cmd":["git push*","git commit*","git branch -D*","git checkout HEAD*"]}}]` | Permission rules for tool calls. See amp permissions --help |
| `amp.proxy` | `undefined` | Proxy URL used for both HTTP and HTTPS requests to the Amp server |
| `amp.showCosts` | `true` | Set to false to hide costs while working on a thread |
| `amp.skills.path` | `undefined` | Path to additional directories containing skills. Supports colon-separated paths (semicolon on Windows). Use ~ for home directory. |
| `amp.terminal.animation` | `true` | Set to false to disable terminal animations (or use the equivalent NO_ANIMATION=1 env var) |
| `amp.terminal.theme` | `terminal` | Color theme for the CLI. Built-in: terminal, dark, light, catppuccin-mocha, solarized-dark, solarized-light, gruvbox-dark-hard, nord. Custom themes: ~/.config/amp/themes/<name>/colors.toml |
| `amp.toolbox.path` | `undefined` | Path to the directory containing toolbox scripts. Supports colon-separated paths. |
| `amp.tools.disable` | `["browser_navigate","builtin:edit_file"]` | Array of tool names to disable. Use 'builtin:toolname' to disable only the builtin tool with that name (allowing an MCP server to provide a tool by that name). |
| `amp.tools.enable` | `undefined` | Array of tool name patterns to enable. Supports glob patterns (e.g., 'mcp__metabase__*'). If not set, all tools are enabled. If set, only matching tools are enabled. |
| `amp.updates.mode` | `auto` | Control update checking behavior: "warn" shows update notifications, "disabled" turns off checking, "auto" automatically runs update. |

## Internal/Hidden Settings

| Key | Default | Description |
|---|---|---|
| `amp.agent.skipTitleGenerationIfMessageContains` | `[]` | List of strings that, if present in a message, will skip title generation |
| `amp.anthropic.effort` | `high` | Effort level for Anthropic models that support auto-thinking (low, medium, high, max). Higher effort means more thinking and better performance. |
| `amp.anthropic.interleavedThinking.enabled` | `false` | Enable interleaved thinking for Claude 4 models (allows reasoning between tool calls) |
| `amp.anthropic.provider` | `anthropic` | Which provider to use for Anthropic Claude inference: "anthropic" or "vertex" |
| `amp.anthropic.speed` | `undefined` | Speed mode for Anthropic models (standard or fast) |
| `amp.anthropic.temperature` | `1` | Temperature setting for Anthropic models (0.0 = deterministic, 1.0 = creative). Note: Only takes effect when thinking is disabled. Internal use only. |
| `amp.anthropic.thinking.enabled` | `false` | Enable Claude thinking process output for debugging |
| `amp.debugLogs` | `f

================================================
FILE: scripts\debug-openai.ts
================================================
/**
 * Mini diagnostic flow for OpenAI (Codex) provider.
 *
 * Step 1: Read token from credential store
 * Step 2: Refresh token if expired
 * Step 3: Call OpenAI API directly (bypass proxy)
 * Step 4: Call through the local proxy
 *
 * Usage: bun run scripts/debug-openai.ts [port]
 */

import { Database } from "bun:sqlite";
import { homedir } from "node:os";
import { join } from "node:path";

const port = process.argv[2] ?? "7860";
const CODEX_BASE_URL = "https://chatgpt.com/backend-api";
const OPENAI_TOKEN_URL = "https://auth.openai.com/oauth/token";
const CLIENT_ID = "app_EMoamEEZ73f0CkXaXp7hrann";
const JWT_CLAIM_PATH = "https://api.openai.com/auth";

const BODY = {
  model: "gpt-5.2",
  stream: true,
  store: false,
  instructions: "",
  input: [{ role: "user", content: "Say hello in one word." }],
};

// ── Helpers ──────────────────────────────────────────────────────────────────

function header(title: string) {
  console.log(`\n${"═".repeat(60)}`);
  console.log(`  ${title}`);
  console.log(`${"═".repeat(60)}`);
}

async function printResponse(label: string, response: Response) {
  console.log(`\n[${label}] Status: ${response.status} ${response.statusText}`);
  console.log(`[${label}] Headers:`);
  for (const [k, v] of response.headers.entries()) {
    if (["content-type", "x-request-id", "retry-after", "x-ratelimit-remaining-tokens"].includes(k)) {
      console.log(`  ${k}: ${v}`);
    }
  }
  const text = await response.text();
  console.log(`[${label}] Body (${text.length} bytes):`);
  try {
    console.log(JSON.stringify(JSON.parse(text), null, 2));
  } catch {
    console.log(text.slice(0, 500));
  }
  return text;
}

// ── Step 1: Read credentials from SQLite ─────────────────────────────────────

header("Step 1: Read Codex credentials from store");

const dbPath = join(homedir(), ".ampcode-connector", "credentials.db");
let db: Database;
try {
  db = new Database(dbPath, { readonly: true, strict: true });
} catch (err) {
  console.error(`✗ Cannot open credential DB at ${dbPath}: ${err}`);
  process.exit(1);
}

const rows = db.prepare<{ account: number; data: string }, [string]>(
  "SELECT account, data FROM credentials WHERE provider = ? ORDER BY account",
).all("codex");

if (rows.length === 0) {
  console.error("✗ No Codex credentials found. Run the login flow first.");
  process.exit(1);
}

for (const row of rows) {
  const creds = JSON.parse(row.data);
  const expiresIn = Math.round((creds.expiresAt - Date.now()) / 1000);
  const fresh = Date.now() < creds.expiresAt;
  console.log(`  account=${row.account}  fresh=${fresh}  expiresIn=${expiresIn}s  hasRefresh=${!!creds.refreshToken}`);
  console.log(`  accessToken=${creds.accessToken.slice(0, 20)}...`);
}

// ── Step 2: Refresh token if expired ─────────────────────────────────────────

header("Step 2: Ensure fresh access token");

const creds = JSON.parse(rows[0]!.data);
let accessToken: string = creds.accessToken;

if (Date.now() >= creds.expiresAt) {
  console.log("  Token expired, attempting refresh...");

  if (!creds.refreshToken) {
    console.error("  ✗ No refresh token available. Re-login required.");
    process.exit(1);
  }

  const refreshRes = await fetch(OPENAI_TOKEN_URL, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      grant_type: "refresh_token",
      refresh_token: creds.refreshToken,
      client_id: CLIENT_ID,
    }).toString(),
  });

  if (!refreshRes.ok) {
    const text = await refreshRes.text();
    console.error(`  ✗ Refresh failed (${refreshRes.status}): ${text}`);
    process.exit(1);
  }

  const refreshData = (await refreshRes.json()) as Record<string, unknown>;
  accessToken = refreshData.access_token as string;
  console.log(`  ✓ Refreshed! New token: ${accessToken.slice(0, 20)}...`);
  console.log(`  expires_in: ${refreshData.expires_in}s`);
} else {
  console.log(`  ✓ Token still fresh (${Math.round((creds.expiresAt - Date.now()) / 1000)}s remaining)`);
}

// ── Step 2b: Extract account ID from JWT ─────────────────────────────────────

let accountId: string | undefined;
try {
  const parts = accessToken.split(".");
  const payload = JSON.parse(Buffer.from(parts[1]!, "base64url").toString("utf-8"));
  accountId = payload[JWT_CLAIM_PATH]?.chatgpt_account_id;
  console.log(`  accountId: ${accountId ?? "(not found)"}`);
} catch {
  console.log("  ⚠ Could not decode JWT for account ID");
}

// ── Step 3: Call ChatGPT Codex backend directly (bypass proxy) ───────────────

header("Step 3: Call ChatGPT Codex backend directly (bypass proxy)");

const directUrl = `${CODEX_BASE_URL}/codex/responses`;
console.log(`  URL: ${directUrl}`);

const directRes = await fetch(directUrl, {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer ${accessToken}`,
    Accept: "text/event-stream",
    "OpenAI-Beta": "responses=experimental",
    "originator": "codex_cli_rs",
    "User-Agent": "codex_cli_rs/0

================================================
FILE: scripts\debug-oracle.ts
================================================
/**
 * Debug script: sends a mock oracle (OpenAI /responses) request to the local proxy
 * and prints raw status, headers, and body to diagnose "Out of Credits" errors.
 *
 * Usage: bun run scripts/debug-oracle.ts [port]
 */

const port = process.argv[2] ?? "7860";
const url = `http://localhost:${port}/api/provider/openai/v1/responses`;

const body = {
  model: "gpt-5.2",
  stream: false,
  input: [{ role: "user", content: "Say hello in one word." }],
};

console.log(`\n>>> POST ${url}`);
console.log(`>>> Body: ${JSON.stringify(body, null, 2)}\n`);

const start = Date.now();
const response = await fetch(url, {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
  body: JSON.stringify(body),
});
const elapsed = Date.now() - start;

console.log(`<<< Status: ${response.status} ${response.statusText}`);
console.log(`<<< Duration: ${elapsed}ms`);
console.log(`<<< Headers:`);
for (const [key, value] of response.headers.entries()) {
  console.log(`<<<   ${key}: ${value}`);
}

const text = await response.text();
console.log(`\n<<< Body (${text.length} bytes):`);
try {
  console.log(JSON.stringify(JSON.parse(text), null, 2));
} catch {
  console.log(text);
}


================================================
FILE: src\constants.ts
================================================
/** Single source of truth — no magic strings scattered across files. */

export const CODE_ASSIST_ENDPOINT = "https://cloudcode-pa.googleapis.com";
export const ANTIGRAVITY_DAILY_ENDPOINT = "https://daily-cloudcode-pa.googleapis.com";
export const ANTIGRAVITY_DAILY_SANDBOX_ENDPOINT = "https://daily-cloudcode-pa.sandbox.googleapis.com";
export const AUTOPUSH_ENDPOINT = "https://autopush-cloudcode-pa.sandbox.googleapis.com";
export const DEFAULT_ANTIGRAVITY_PROJECT = "rising-fact-p41fc";

export const ANTHROPIC_API_URL = "https://api.anthropic.com";
export const CODEX_BASE_URL = "https://chatgpt.com/backend-api";

/** Codex-specific headers required by the ChatGPT backend. */
export const codexHeaders = {
  BETA: "OpenAI-Beta",
  ACCOUNT_ID: "chatgpt-account-id",
  ORIGINATOR: "originator",
  SESSION_ID: "session_id",
  CONVERSATION_ID: "conversation_id",
} as const;

export const CODEX_CLI_VERSION = "0.101.0";

export const codexHeaderValues = {
  BETA_RESPONSES: "responses=experimental",
  ORIGINATOR: "codex_cli_rs",
  VERSION: CODEX_CLI_VERSION,
  USER_AGENT: `codex_cli_rs/${CODEX_CLI_VERSION} (${process.platform} ${process.arch})`,
} as const;

/** Map Amp CLI paths → ChatGPT backend paths.
 *  Both /v1/responses and /v1/chat/completions route to /codex/responses. */
export const codexPathMap: Record<string, string> = {
  "/v1/responses": "/codex/responses",
  "/v1/chat/completions": "/codex/responses",
} as const;
export const DEFAULT_AMP_UPSTREAM_URL = "https://ampcode.com";

export const ANTHROPIC_TOKEN_URL = "https://platform.claude.com/v1/oauth/token";
export const OPENAI_TOKEN_URL = "https://auth.openai.com/oauth/token";
export const GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token";

export const TOKEN_EXPIRY_BUFFER_MS = 5 * 60 * 1000;
export const CLAUDE_CODE_VERSION = "2.1.77";

export const claudeCodeBetas = [
  "claude-code-20250219",
  "oauth-2025-04-20",
  "interleaved-thinking-2025-05-14",
  "context-management-2025-06-27",
  "prompt-caching-scope-2026-01-05",
] as const;

export const filteredBetaFeatures = ["fast-mode-2026-02-01"] as const;

export const modelFieldPaths = [
  "model",
  "message.model",
  "modelVersion",
  "response.model",
  "response.modelVersion",
] as const;

export const passthroughPrefixes = [
  "/api/internal",
  "/api/user",
  "/api/auth",
  "/api/meta",
  "/api/ads",
  "/api/telemetry",
  "/api/threads",
  "/api/otel",
  "/api/tab",
  "/api/durable-thread-workers",
] as const;

/** Browser routes — redirect to ampcode.com (auth cookies need correct domain). */
export const browserPrefixes = ["/auth", "/threads", "/docs", "/settings"] as const;

export const passthroughExact = ["/threads.rss", "/news.rss"] as const;


================================================
FILE: src\index.ts
================================================
#!/usr/bin/env bun
/** ampcode-connector entry point. */

import { startAutoRefresh } from "./auth/auto-refresh.ts";
import * as configs from "./auth/configs.ts";
import type { OAuthConfig } from "./auth/oauth.ts";
import * as oauth from "./auth/oauth.ts";
import { bannerAd } from "./cli/ads.ts";
import { line, s } from "./cli/ansi.ts";
import { setup } from "./cli/setup.ts";
import * as status from "./cli/status.ts";
import { dashboard } from "./cli/tui.ts";
import { loadConfig, type ProxyConfig } from "./config/config.ts";
import { startServer } from "./server/server.ts";
import { logger, setLogLevel } from "./utils/logger.ts";

const providers: Record<string, OAuthConfig> = {
  anthropic: configs.anthropic,
  codex: configs.codex,
  google: configs.google,
};

async function main(): Promise<void> {
  const [command, arg] = process.argv.slice(2);

  if (command === "setup") return setup();

  if (command === "login") {
    if (!arg) return dashboard();

    const config = providers[arg];
    if (!config) {
      logger.error(`Unknown provider: ${arg}. Available: ${Object.keys(providers).join(", ")}`);
      process.exit(1);
    }
    await oauth.login(config);
    return;
  }

  if (command === "help" || command === "--help" || command === "-h") {
    usage();
    return;
  }

  const config = await loadConfig();
  setLogLevel(config.logLevel);
  startServer(config);
  startAutoRefresh();
  banner(config);

  // Non-blocking update check — runs in background after server starts
  const { checkForUpdates } = await import("./utils/update-check.ts");
  checkForUpdates();
}

function banner(config: ProxyConfig): void {
  const providers = status.all();
  const upstream = config.ampUpstreamUrl.replace(/^https?:\/\//, "");

  line();
  line(`  ${s.bold}ampcode-connector${s.reset}`);
  line(`  ${s.dim}http://${config.hostname}:${config.port}${s.reset}`);
  line();

  for (const p of providers) {
    const count = p.accounts.length;
    const label = p.label.padEnd(16);
    const countStr = count > 0 ? `${count} account${count > 1 ? "s" : ""}` : "--";
    const dot = count > 0 ? `${s.green}●${s.reset}` : `${s.dim}○${s.reset}`;
    line(`  ${label}  ${countStr.padEnd(12)}${dot}`);
  }

  line();
  line(`  ${s.dim}upstream → ${upstream}${s.reset}`);
  line();
  bannerAd();
  line();
}

function usage(): void {
  line();
  line(`${s.bold}ampcode-connector${s.reset} ${s.dim}— proxy Amp CLI through local OAuth subscriptions${s.reset}`);
  line();
  line(`${s.bold}USAGE${s.reset}`);
  line(`  ${s.cyan}bun start${s.reset}              Start the proxy server`);
  line(`  ${s.cyan}bun run setup${s.reset}          Configure Amp CLI to use this proxy`);
  line(`  ${s.cyan}bun run login${s.reset}          Interactive login dashboard`);
  line(`  ${s.cyan}bun run login <p>${s.reset}      Login to a specific provider`);
  line();
  line(`${s.bold}PROVIDERS${s.reset}`);
  line(`  anthropic     Claude Code ${s.dim}(Anthropic models)${s.reset}`);
  line(`  codex         OpenAI Codex ${s.dim}(GPT/o3 models)${s.reset}`);
  line(`  google        Google ${s.dim}(Gemini CLI + Antigravity, dual quota)${s.reset}`);
  line();
  line(`${s.bold}CONFIG${s.reset}`);
  line(`  Edit ${s.cyan}config.yaml${s.reset} to customize port, providers, and log level.`);
  line();
}

main().catch((err) => {
  logger.error("Fatal", { error: String(err) });
  process.exit(1);
});


================================================
FILE: src\auth\auto-refresh.ts
================================================
import { TOKEN_EXPIRY_BUFFER_MS } from "../constants.ts";
import { logger } from "../utils/logger.ts";
import * as configs from "./configs.ts";
import type { OAuthConfig } from "./oauth.ts";
import * as oauth from "./oauth.ts";
import { getAll, type ProviderName } from "./store.ts";

const REFRESH_INTERVAL_MS = 60_000;

const providerConfigs: Record<ProviderName, OAuthConfig> = {
  anthropic: configs.anthropic,
  codex: configs.codex,
  google: configs.google,
};

let timer: Timer | null = null;

async function refreshAll(): Promise<void> {
  const now = Date.now();

  for (const [provider, config] of Object.entries(providerConfigs) as [ProviderName, OAuthConfig][]) {
    for (const { account, credentials } of getAll(provider)) {
      if (credentials.expiresAt - now > TOKEN_EXPIRY_BUFFER_MS) continue;

      try {
        logger.debug("Auto-refreshing token", { provider, account });
        await oauth.token(config, account);
      } catch (err) {
        logger.error("Auto-refresh failed", { provider, account, error: String(err) });
      }
    }
  }
}

export function startAutoRefresh(): void {
  if (timer) return;
  timer = setInterval(refreshAll, REFRESH_INTERVAL_MS);
}

export function stopAutoRefresh(): void {
  if (!timer) return;
  clearInterval(timer);
  timer = null;
}


================================================
FILE: src\auth\callback-server.ts
================================================
/** Temporary localhost HTTP server to receive OAuth callbacks. */

import { logger } from "../utils/logger.ts";

interface CallbackResult {
  code: string;
  state: string;
}

const DEFAULT_TIMEOUT = 120_000;

export async function waitForCallback(
  preferredPort: number,
  callbackPath: string,
  expectedState: string,
  timeout: number = DEFAULT_TIMEOUT,
): Promise<CallbackResult> {
  return new Promise((resolve, reject) => {
    let server: ReturnType<typeof Bun.serve> | null = null;
    let timeoutId: Timer | null = null;

    const cleanup = () => {
      if (timeoutId) clearTimeout(timeoutId);
      if (server) {
        server.stop(true);
        server = null;
      }
    };

    timeoutId = setTimeout(() => {
      cleanup();
      reject(new Error(`OAuth callback timed out after ${timeout}ms`));
    }, timeout);

    try {
      server = Bun.serve({
        port: preferredPort,
        hostname: "localhost",
        fetch(req) {
          const url = new URL(req.url);
          if (url.pathname !== callbackPath) return new Response("Not found", { status: 404 });

          const code = url.searchParams.get("code");
          const state = url.searchParams.get("state");
          const error = url.searchParams.get("error");
          const errorDescription = url.searchParams.get("error_description");

          if (error) {
            cleanup();
            reject(new Error(`OAuth error: ${error} - ${errorDescription ?? "unknown"}`));
            return htmlPage("Authentication Failed", `Error: ${error}. ${errorDescription ?? ""}`);
          }

          if (!code || !state) {
            cleanup();
            reject(new Error("Missing code or state in OAuth callback"));
            return htmlPage("Authentication Failed", "Missing authorization code.");
          }

          if (state !== expectedState) {
            cleanup();
            reject(new Error("State mismatch in OAuth callback (possible CSRF)"));
            return htmlPage("Authentication Failed", "State validation failed.");
          }

          cleanup();
          resolve({ code, state });
          return htmlPage("Authentication Successful", "You can close this window and return to the terminal.");
        },
      });

      logger.debug("Callback server started", { provider: `port:${preferredPort}` });
    } catch (err) {
      cleanup();
      reject(new Error(`Failed to start callback server on port ${preferredPort}: ${err}`));
    }
  });
}

function htmlPage(title: string, message: string): Response {
  const body = `<!DOCTYPE html>
<html>
<head><title>${title}</title></head>
<body style="font-family: system-ui; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0;">
  <div style="text-align: center;">
    <h1>${title}</h1>
    <p>${message}</p>
  </div>
</body>
</html>`;
  return new Response(body, { headers: { "Content-Type": "text/html" } });
}


================================================
FILE: src\auth\configs.ts
================================================
import { ANTHROPIC_TOKEN_URL, GOOGLE_TOKEN_URL, OPENAI_TOKEN_URL } from "../constants.ts";
import { discoverAnthropic, discoverCodex, discoverGoogle } from "./discovery.ts";
import type { OAuthConfig } from "./oauth.ts";

export const anthropic: OAuthConfig = {
  providerName: "anthropic",
  clientId: "9d1c250a-e61b-44d9-88ed-5944d1962f5e",
  authorizeUrl: "https://claude.ai/oauth/authorize",
  tokenUrl: ANTHROPIC_TOKEN_URL,
  callbackPort: 54545,
  callbackPath: "/callback",
  scopes: "org:create_api_key user:profile user:inference user:sessions:claude_code user:mcp_servers user:file_upload",
  bodyFormat: "json",
  expiryBuffer: true,
  sendStateInExchange: true,
  authorizeExtra: { code: "true" },
  extractIdentity: discoverAnthropic,
};

export const codex: OAuthConfig = {
  providerName: "codex",
  clientId: "app_EMoamEEZ73f0CkXaXp7hrann",
  authorizeUrl: "https://auth.openai.com/oauth/authorize",
  tokenUrl: OPENAI_TOKEN_URL,
  callbackPort: 1455,
  callbackPath: "/auth/callback",
  scopes: "openid profile email offline_access",
  bodyFormat: "form",
  expiryBuffer: true,
  authorizeExtra: {
    id_token_add_organizations: "true",
    codex_cli_simplified_flow: "true",
    originator: "opencode",
  },
  extractIdentity: discoverCodex,
};

export const google: OAuthConfig = {
  providerName: "google",
  clientId: "1071006060591-tmhssin2h21lcre235vtolojh4g403ep.apps.googleusercontent.com",
  clientSecret: "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",
  authorizeUrl: "https://accounts.google.com/o/oauth2/v2/auth",
  tokenUrl: GOOGLE_TOKEN_URL,
  callbackPort: 51121,
  callbackPath: "/oauth-callback",
  scopes: [
    "https://www.googleapis.com/auth/cloud-platform",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "https://www.googleapis.com/auth/cclog",
    "https://www.googleapis.com/auth/experimentsandconfigs",
  ].join(" "),
  bodyFormat: "form",
  expiryBuffer: true,
  authorizeExtra: { access_type: "offline", prompt: "consent" },
  extractIdentity: discoverGoogle,
};


================================================
FILE: src\auth\discovery.ts
================================================
import {
  ANTIGRAVITY_DAILY_ENDPOINT,
  AUTOPUSH_ENDPOINT,
  CODE_ASSIST_ENDPOINT,
  DEFAULT_ANTIGRAVITY_PROJECT,
} from "../constants.ts";
import { fromBase64url } from "../utils/encoding.ts";
import { logger } from "../utils/logger.ts";
import type { Credentials } from "./store.ts";

type Raw = Record<string, unknown>;

export async function discoverAnthropic(raw: Raw): Promise<Partial<Credentials>> {
  const account = raw.account as { uuid?: string; email_address?: string } | undefined;
  return {
    ...(account?.email_address ? { email: account.email_address } : {}),
    ...(account?.uuid ? { accountId: account.uuid } : {}),
  };
}

export async function discoverCodex(raw: Raw): Promise<Partial<Credentials>> {
  const accessToken = raw.access_token as string;
  const accountId = accountIdFromJWT(accessToken);
  const email = await fetchEmail("https://api.openai.com/v1/me", accessToken);
  return {
    ...(accountId ? { accountId } : {}),
    ...(email ? { email } : {}),
  };
}

export async function discoverGoogle(raw: Raw): Promise<Partial<Credentials>> {
  const accessToken = raw.access_token as string;
  const email = await fetchEmail("https://www.googleapis.com/oauth2/v1/userinfo?alt=json", accessToken);
  const projectId = await findProject(accessToken);
  return { ...(email ? { email } : {}), ...(projectId ? { projectId } : {}) };
}

function accountIdFromJWT(token: string): string | null {
  try {
    const parts = token.split(".");
    if (parts.length < 2 || !parts[1]) return null;
    const payload = JSON.parse(new TextDecoder().decode(fromBase64url(parts[1]))) as Raw;
    const auth = payload["https://api.openai.com/auth"] as Raw | undefined;
    return (auth?.chatgpt_account_id as string) ?? null;
  } catch {
    return null;
  }
}

async function fetchEmail(url: string, accessToken: string): Promise<string | undefined> {
  try {
    const res = await fetch(url, { headers: { Authorization: `Bearer ${accessToken}` } });
    if (!res.ok) return undefined;
    return ((await res.json()) as { email?: string }).email;
  } catch {
    return undefined;
  }
}

const CCA_HEADERS = {
  "Content-Type": "application/json",
  "User-Agent": "google-api-nodejs-client/9.15.1",
  "X-Goog-Api-Client": "google-cloud-sdk vscode_cloudshelleditor/0.1",
  "Client-Metadata": JSON.stringify({
    ideType: "IDE_UNSPECIFIED",
    platform: "PLATFORM_UNSPECIFIED",
    pluginType: "GEMINI",
  }),
} as const;

const CCA_BODY = JSON.stringify({
  metadata: { ideType: "IDE_UNSPECIFIED", platform: "PLATFORM_UNSPECIFIED", pluginType: "GEMINI" },
});

async function findProject(accessToken: string): Promise<string | undefined> {
  for (const endpoint of [CODE_ASSIST_ENDPOINT, ANTIGRAVITY_DAILY_ENDPOINT, AUTOPUSH_ENDPOINT]) {
    try {
      const res = await fetch(`${endpoint}/v1internal:loadCodeAssist`, {
        method: "POST",
        headers: { ...CCA_HEADERS, Authorization: `Bearer ${accessToken}` },
        body: CCA_BODY,
      });

      if (!res.ok) {
        logger.debug(`loadCodeAssist ${res.status} at ${endpoint}`);
        continue;
      }

      const body = (await res.json()) as { cloudaicompanionProject?: string | { id?: string } };
      const proj = body.cloudaicompanionProject;
      const id = typeof proj === "string" ? proj : proj?.id;
      if (id) return id;
    } catch (err) {
      logger.debug(`loadCodeAssist error at ${endpoint}`, { error: String(err) });
    }
  }

  logger.warn(`Project discovery failed, using fallback: ${DEFAULT_ANTIGRAVITY_PROJECT}`);
  return DEFAULT_ANTIGRAVITY_PROJECT;
}


================================================
FILE: src\auth\oauth.ts
================================================
import { TOKEN_EXPIRY_BUFFER_MS } from "../constants.ts";
import * as browser from "../utils/browser.ts";
import { logger } from "../utils/logger.ts";
import { waitForCallback } from "./callback-server.ts";
import { generatePKCE, generateState } from "./pkce.ts";
import type { Credentials, ProviderName } from "./store.ts";
import * as store from "./store.ts";

export interface OAuthConfig {
  providerName: ProviderName;
  clientId: string;
  clientSecret?: string;
  authorizeUrl: string;
  tokenUrl: string;
  callbackPort: number;
  callbackPath: string;
  scopes: string;
  bodyFormat: "json" | "form";
  authorizeExtra?: Record<string, string>;
  expiryBuffer?: boolean;
  sendStateInExchange?: boolean;
  extractIdentity?: (raw: Record<string, unknown>) => Promise<Partial<Credentials>>;
}

export async function token(config: OAuthConfig, account = 0): Promise<string | null> {
  const creds = store.get(config.providerName, account);

  if (!creds) {
    try {
      return (await serialize(config)).accessToken;
    } catch (err) {
      logger.error(`Auto-login failed for ${config.providerName}`, { error: String(err) });
      return null;
    }
  }

  if (store.fresh(creds)) return creds.accessToken;

  const refreshed = await refreshWithRetry(config, creds.refreshToken, account);
  return refreshed?.accessToken ?? null;
}

export async function tokenFromAny(config: OAuthConfig): Promise<{ accessToken: string; account: number } | null> {
  for (const { account, credentials: c } of store.getAll(config.providerName)) {
    if (store.fresh(c)) return { accessToken: c.accessToken, account };
  }

  for (const { account, credentials: c } of store.getAll(config.providerName)) {
    if (!c.refreshToken) continue;
    try {
      const refreshed = await refresh(config, c.refreshToken, account);
      return { accessToken: refreshed.accessToken, account };
    } catch (err) {
      handleRefreshFailure(config, account, err);
      logger.debug(`${config.providerName}:${account} refresh failed in tokenFromAny`, { error: String(err) });
    }
  }

  return null;
}

export function ready(config: OAuthConfig): boolean {
  return store.exists(config.providerName);
}

export function accountCount(config: OAuthConfig): number {
  return store.count(config.providerName);
}

export async function login(config: OAuthConfig): Promise<Credentials> {
  const { verifier, challenge } = await generatePKCE();
  const state = generateState();
  const redirectUri = `http://localhost:${config.callbackPort}${config.callbackPath}`;

  const authUrl = new URL(config.authorizeUrl);
  const q = authUrl.searchParams;
  q.set("client_id", config.clientId);
  q.set("response_type", "code");
  q.set("redirect_uri", redirectUri);
  q.set("scope", config.scopes);
  q.set("code_challenge", challenge);
  q.set("code_challenge_method", "S256");
  q.set("state", state);
  if (config.authorizeExtra) {
    for (const [k, v] of Object.entries(config.authorizeExtra)) q.set(k, v);
  }

  logger.info(`Opening browser for ${config.providerName} OAuth...`);
  if (!(await browser.open(authUrl.toString()))) {
    logger.warn("Could not open browser. Please open this URL manually:");
    logger.info(authUrl.toString());
  }

  const callback = await waitForCallback(config.callbackPort, config.callbackPath, state);

  const exchangeParams: Record<string, string> = {
    grant_type: "authorization_code",
    code: callback.code,
    redirect_uri: redirectUri,
    code_verifier: verifier,
  };
  if (config.sendStateInExchange) exchangeParams.state = callback.state;

  const raw = await exchange(config, exchangeParams);
  let credentials = parseTokenFields(raw, config);

  if (config.extractIdentity) {
    try {
      credentials = { ...credentials, ...(await config.extractIdentity(raw)) };
    } catch (err) {
      logger.error(`${config.providerName} identity extraction failed`, { error: String(err) });
    }
  }

  const existing = store.findByIdentity(config.providerName, credentials);
  const account = existing ?? store.nextAccount(config.providerName);

  if (!credentials.refreshToken) {
    credentials.refreshToken = store.get(config.providerName, account)?.refreshToken ?? "";
  }
  if (!credentials.refreshToken) {
    throw new Error(`No refresh token for ${config.providerName}. Revoke app access and try again.`);
  }

  store.save(config.providerName, credentials, account);
  logger.info(`${config.providerName}:${account} ${existing !== null ? "updated" : "added"}`);
  return credentials;
}

const loginLocks = new Map<ProviderName, Promise<Credentials>>();

function serialize(config: OAuthConfig): Promise<Credentials> {
  const pending = loginLocks.get(config.providerName);
  if (pending) return pending;

  const promise = login(config).finally(() => loginLocks.delete(config.providerName));
  loginLocks.set(config.providerName, promise);
  return promise;
}

async function refresh(config: OAuthConfig, refreshToken: string, account = 0): Promise<Credentials> 

================================================
FILE: src\auth\pkce.ts
================================================
/** PKCE (Proof Key for Code Exchange) — S256 challenge for all OAuth flows. */

import { toBase64url } from "../utils/encoding.ts";

export async function generatePKCE(): Promise<{ verifier: string; challenge: string }> {
  const verifierBytes = new Uint8Array(96);
  crypto.getRandomValues(verifierBytes);
  const verifier = toBase64url(verifierBytes);

  const hashBuffer = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(verifier));
  const challenge = toBase64url(new Uint8Array(hashBuffer));

  return { verifier, challenge };
}

export function generateState(): string {
  const bytes = new Uint8Array(16);
  crypto.getRandomValues(bytes);
  return Array.from(bytes)
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");
}


================================================
FILE: src\auth\store.ts
================================================
/** SQLite credential storage at ~/.ampcode-connector/credentials.db
 *  Multi-account: composite key (provider, account).
 *  Sync API via bun:sqlite — no cache needed at 0.4µs/read. */

import { Database, type Statement } from "bun:sqlite";
import { mkdirSync } from "node:fs";
import { homedir } from "node:os";
import { join } from "node:path";
import { logger } from "../utils/logger.ts";

export interface Credentials {
  accessToken: string;
  refreshToken: string;
  expiresAt: number;
  projectId?: string;
  email?: string;
  accountId?: string;
}

export type ProviderName = "anthropic" | "codex" | "google";

const DEFAULT_DIR = join(homedir(), ".ampcode-connector");
const DEFAULT_DB_PATH = join(DEFAULT_DIR, "credentials.db");

interface DataRow {
  data: string;
}
interface AccountDataRow {
  account: number;
  data: string;
}
interface MaxAccountRow {
  max_account: number | null;
}
interface CountRow {
  cnt: number;
}

interface Statements {
  get: Statement<DataRow, [string, number]>;
  getAll: Statement<AccountDataRow, [string]>;
  set: Statement<void, [string, number, string]>;
  delOne: Statement<void, [string, number]>;
  delAll: Statement<void, [string]>;
  maxAccount: Statement<MaxAccountRow, [string]>;
  count: Statement<CountRow, [string]>;
}

let _db: Database | null = null;
let _stmts: Statements | null = null;
const _dbPath = DEFAULT_DB_PATH;
function init() {
  if (_stmts) return _stmts;

  const dir = _dbPath.replace(/\/[^/]+$/, "");
  mkdirSync(dir, { recursive: true, mode: 0o700 });
  _db = new Database(_dbPath, { strict: true });
  _db.exec("PRAGMA journal_mode=WAL");
  _db.exec("PRAGMA busy_timeout=5000");
  _db.exec(`
    CREATE TABLE IF NOT EXISTS credentials (
      provider TEXT NOT NULL,
      account  INTEGER NOT NULL DEFAULT 0,
      data     TEXT NOT NULL,
      PRIMARY KEY (provider, account)
    )
  `);

  _stmts = {
    get: _db.prepare<DataRow, [string, number]>("SELECT data FROM credentials WHERE provider = ? AND account = ?"),
    getAll: _db.prepare<AccountDataRow, [string]>(
      "SELECT account, data FROM credentials WHERE provider = ? ORDER BY account",
    ),
    set: _db.prepare<void, [string, number, string]>(
      "INSERT OR REPLACE INTO credentials (provider, account, data) VALUES (?, ?, ?)",
    ),
    delOne: _db.prepare<void, [string, number]>("DELETE FROM credentials WHERE provider = ? AND account = ?"),
    delAll: _db.prepare<void, [string]>("DELETE FROM credentials WHERE provider = ?"),
    maxAccount: _db.prepare<MaxAccountRow, [string]>(
      "SELECT MAX(account) as max_account FROM credentials WHERE provider = ?",
    ),
    count: _db.prepare<CountRow, [string]>("SELECT COUNT(*) as cnt FROM credentials WHERE provider = ?"),
  };
  return _stmts;
}

export function get(provider: ProviderName, account = 0): Credentials | undefined {
  const row = init().get.get(provider, account);
  if (!row) return undefined;
  try {
    return JSON.parse(row.data) as Credentials;
  } catch (err) {
    logger.warn(`Corrupt credentials for ${provider}:${account}, removing`, { error: String(err) });
    init().delOne.run(provider, account);
    return undefined;
  }
}

export function getAll(provider: ProviderName): { account: number; credentials: Credentials }[] {
  const results: { account: number; credentials: Credentials }[] = [];
  for (const row of init().getAll.all(provider)) {
    try {
      results.push({ account: row.account, credentials: JSON.parse(row.data) as Credentials });
    } catch (err) {
      logger.warn(`Corrupt credentials for ${provider}:${row.account}, removing`, { error: String(err) });
      init().delOne.run(provider, row.account);
    }
  }
  return results;
}

export function save(provider: ProviderName, credentials: Credentials, account = 0): void {
  init().set.run(provider, account, JSON.stringify(credentials));
}

export function remove(provider: ProviderName, account?: number): void {
  if (account !== undefined) {
    init().delOne.run(provider, account);
  } else {
    init().delAll.run(provider);
  }
}

export function nextAccount(provider: ProviderName): number {
  const row = init().maxAccount.get(provider);
  return (row?.max_account ?? -1) + 1;
}

export function count(provider: ProviderName): number {
  return init().count.get(provider)?.cnt ?? 0;
}

/** Find existing account by email or accountId match. */
export function findByIdentity(provider: ProviderName, credentials: Credentials): number | null {
  const all = getAll(provider);
  for (const entry of all) {
    if (credentials.email && entry.credentials.email === credentials.email) return entry.account;
    if (credentials.accountId && entry.credentials.accountId === credentials.accountId) return entry.account;
  }
  return null;
}

export function exists(provider: ProviderName): boolean {
  const all = getAll(provider);
  return all.some((e) => !!e.credentials.refreshToken);
}

export function fresh(credentials: Credentials): boolean {
  return Date.now() < credent

================================================
FILE: src\cli\ads.ts
================================================
/** Periodic GitHub star reminder — non-intrusive, shows in server logs. */

import { line, s } from "../cli/ansi.ts";

const REPO_URL = "https://github.com/nghyane/ampcode-connector";
const REQUEST_INTERVAL = 50;

let requestCount = 0;
let shown = false;

const messages = [
  `${s.yellow}⭐${s.reset} Enjoying ampcode-connector? Star us on GitHub → ${s.cyan}${REPO_URL}${s.reset}`,
  `${s.yellow}⭐${s.reset} Help others discover this tool — star on GitHub → ${s.cyan}${REPO_URL}${s.reset}`,
  `${s.yellow}⭐${s.reset} ${s.dim}Your star helps keep this project alive!${s.reset} → ${s.cyan}${REPO_URL}${s.reset}`,
];

function pick(): string {
  return messages[Math.floor(Math.random() * messages.length)]!;
}

/** Show star prompt in the startup banner (once). */
export function bannerAd(): void {
  line(`  ${s.dim}⭐ Star us → ${REPO_URL}${s.reset}`);
}

/** Call after each proxied request. Shows a reminder every N requests. */
export function maybeShowAd(): void {
  requestCount++;
  if (requestCount % REQUEST_INTERVAL !== 0) return;

  // Only show once per interval, don't spam
  if (shown && requestCount < REQUEST_INTERVAL * 3) return;
  shown = true;

  line();
  line(`  ${pick()}`);
  line();
}


================================================
FILE: src\cli\ansi.ts
================================================
/** Raw ANSI escape helpers — no dependencies. */

const ESC = "\x1b[";

export const cursor = {
  hide: () => out(`${ESC}?25l`),
  show: () => out(`${ESC}?25h`),
  home: () => out(`${ESC}H`),
};

export const screen = {
  clear: () => out(`${ESC}2J${ESC}H`),
};

/** Erase from cursor to end of line. */
const eol = `${ESC}K`;

export const s = {
  reset: `${ESC}0m`,
  bold: `${ESC}1m`,
  dim: `${ESC}2m`,
  inverse: `${ESC}7m`,
  green: `${ESC}32m`,
  red: `${ESC}31m`,
  yellow: `${ESC}33m`,
  gray: `${ESC}90m`,
  cyan: `${ESC}36m`,
  white: `${ESC}37m`,
};

export function out(text: string): void {
  process.stdout.write(text);
}

export function line(text = ""): void {
  process.stdout.write(`${text}${eol}\n`);
}


================================================
FILE: src\cli\setup.ts
================================================
/** Auto-configure Amp CLI to route through ampcode-connector. */

import { existsSync, lstatSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { homedir } from "node:os";
import { dirname, join } from "node:path";
import { loadConfig } from "../config/config.ts";
import { line, out, s } from "./ansi.ts";
import * as status from "./status.ts";

const AMP_SECRETS_DIR = join(homedir(), ".local", "share", "amp");
const AMP_SECRETS_PATH = join(AMP_SECRETS_DIR, "secrets.json");

const AMP_SETTINGS_PATH = join(homedir(), ".config", "amp", "settings.json");
const AMP_LEGACY_SETTINGS_PATH = join(homedir(), ".amp", "settings.json");

function ampSettingsPath(): string {
  const envPath = process.env.AMP_SETTINGS_FILE;
  return envPath || AMP_SETTINGS_PATH;
}

function warnLegacySettingsFile(): void {
  if (process.env.AMP_SETTINGS_FILE || !existsSync(AMP_LEGACY_SETTINGS_PATH)) return;
  try {
    if (lstatSync(AMP_LEGACY_SETTINGS_PATH).isSymbolicLink()) return;
  } catch {
    return;
  }

  line(
    `${s.yellow}!${s.reset} Legacy settings file detected at ${s.dim}${AMP_LEGACY_SETTINGS_PATH}${s.reset}. ` +
      `Prefer a single source of truth at ${s.dim}${AMP_SETTINGS_PATH}${s.reset}.`,
  );
}

function readJson(path: string): Record<string, unknown> {
  if (!existsSync(path)) return {};
  try {
    return JSON.parse(readFileSync(path, "utf-8")) as Record<string, unknown>;
  } catch {
    return {};
  }
}

function writeJson(path: string, data: Record<string, unknown>): void {
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, `${JSON.stringify(data, null, 2)}\n`, "utf-8");
}

function findAmpApiKey(proxyUrl: string): string | undefined {
  if (process.env.AMP_API_KEY) return process.env.AMP_API_KEY;

  const secrets = readJson(AMP_SECRETS_PATH);
  const exact = secrets[`apiKey@${proxyUrl}`];
  if (typeof exact === "string" && exact.length > 0) return exact;

  for (const value of Object.values(secrets)) {
    if (typeof value === "string" && value.startsWith("sgamp_")) return value;
  }
  return undefined;
}

/** Save key under proxy URL and migrate stale entries to keep secrets.json clean. */
function saveAmpApiKey(token: string, proxyUrl: string): void {
  const secrets = readJson(AMP_SECRETS_PATH);
  for (const key of Object.keys(secrets)) {
    if (key.startsWith("apiKey")) delete secrets[key];
  }
  secrets[`apiKey@${proxyUrl}`] = token;
  mkdirSync(AMP_SECRETS_DIR, { recursive: true, mode: 0o700 });
  writeJson(AMP_SECRETS_PATH, secrets);
}

function prompt(question: string): Promise<string> {
  return new Promise((resolve) => {
    out(question);
    const chunks: string[] = [];

    const onData = (data: Buffer) => {
      const str = data.toString();
      if (str.includes("\n") || str.includes("\r")) {
        process.stdin.removeListener("data", onData);
        process.stdin.pause();
        resolve(chunks.join("").trim());
        return;
      }
      chunks.push(str);
    };

    process.stdin.resume();
    process.stdin.setEncoding("utf-8");
    process.stdin.on("data", onData);
  });
}

export async function setup(): Promise<void> {
  const config = await loadConfig();
  const proxyUrl = `http://localhost:${config.port}`;

  line();
  line(`${s.bold}ampcode-connector setup${s.reset}`);
  line();

  // Step 1: Configure amp.url in canonical settings file
  const settingsPath = ampSettingsPath();
  const settings = readJson(settingsPath);
  if (settings["amp.url"] !== proxyUrl) {
    settings["amp.url"] = proxyUrl;
    writeJson(settingsPath, settings);
  }
  line(`${s.green}ok${s.reset} amp.url = ${s.cyan}${proxyUrl}${s.reset}  ${s.dim}${settingsPath}${s.reset}`);
  warnLegacySettingsFile();

  // Step 2: Amp API key
  const existingKey = findAmpApiKey(proxyUrl);

  if (existingKey) {
    saveAmpApiKey(existingKey, proxyUrl);
    const preview = `${existingKey.slice(0, 10)}...`;
    line(`${s.green}ok${s.reset} Amp token found  ${s.dim}${preview}${s.reset}`);
  } else {
    line();
    line(`${s.yellow}!${s.reset}  No Amp token found.`);
    line(`   Get one from ${s.cyan}https://ampcode.com/settings${s.reset}`);
    line(`   Or run ${s.cyan}amp login${s.reset} after starting the proxy.`);
    line();

    const token = await prompt(`   Paste token (or press Enter to skip): `);
    line();

    if (token) {
      saveAmpApiKey(token, proxyUrl);
      line(`${s.green}ok${s.reset} Token saved  ${s.dim}${AMP_SECRETS_PATH}${s.reset}`);
    } else {
      line(`${s.dim}-- skipped${s.reset}`);
    }
  }

  // Step 3: Provider status
  line();
  line(`${s.bold}Providers${s.reset}`);

  const providers = status.all();
  let hasAny = false;

  for (const p of providers) {
    const connected = p.accounts.filter((a) => a.status === "connected");
    const disabled = p.accounts.filter((a) => a.status === "disabled");
    const total = p.accounts.filter((a) => a.status !== "disconnected");

    if (connected.length > 0) {
      hasAny = true;
      const emails = connec

================================================
FILE: src\cli\status.ts
================================================
import type { Credentials, ProviderName } from "../auth/store.ts";
import * as store from "../auth/store.ts";
import { cooldown, type QuotaPool } from "../routing/cooldown.ts";

export type ConnectionStatus = "connected" | "expired" | "disabled" | "disconnected";

export interface AccountStatus {
  account: number;
  status: ConnectionStatus;
  email?: string;
  expiresAt?: number;
}

export interface ProviderStatus {
  name: ProviderName;
  label: string;
  sublabel?: string;
  accounts: AccountStatus[];
}

const PROVIDERS: { name: ProviderName; label: string; sublabel?: string }[] = [
  { name: "anthropic", label: "Claude Code" },
  { name: "codex", label: "OpenAI Codex" },
  { name: "google", label: "Google" },
];

const POOL_MAP: Record<ProviderName, QuotaPool[]> = {
  anthropic: ["anthropic"],
  codex: ["codex"],
  google: ["google"],
};

function connectionOf(name: ProviderName, account: number, creds: Credentials): ConnectionStatus {
  if (!creds.refreshToken) return "disconnected";
  const pools = POOL_MAP[name];
  if (pools.some((p) => cooldown.isExhausted(p, account))) return "disabled";
  return store.fresh(creds) ? "connected" : "expired";
}

export function all(): ProviderStatus[] {
  return PROVIDERS.map(({ name, label, sublabel }) => ({
    name,
    label,
    sublabel,
    accounts: store.getAll(name).map((e) => ({
      account: e.account,
      status: connectionOf(name, e.account, e.credentials),
      email: e.credentials.email,
      expiresAt: e.credentials.expiresAt,
    })),
  }));
}

export function remaining(expiresAt: number): string {
  const diff = expiresAt - Date.now();
  if (diff <= 0) return "expired";
  const mins = Math.floor(diff / 60_000);
  const hrs = Math.floor(mins / 60);
  if (hrs > 0) return `${hrs}h ${mins % 60}m`;
  return `${mins}m`;
}


================================================
FILE: src\cli\tui.ts
================================================
import * as configs from "../auth/configs.ts";
import type { OAuthConfig } from "../auth/oauth.ts";
import * as oauth from "../auth/oauth.ts";
import type { ProviderName } from "../auth/store.ts";
import * as store from "../auth/store.ts";
import { cursor, line, s, screen } from "./ansi.ts";
import type { AccountStatus, ConnectionStatus, ProviderStatus } from "./status.ts";
import * as status from "./status.ts";

const oauthConfigs: Record<ProviderName, OAuthConfig> = {
  anthropic: configs.anthropic,
  codex: configs.codex,
  google: configs.google,
};

const ICON: Record<ConnectionStatus, string> = {
  connected: `${s.green}●${s.reset}`,
  expired: `${s.yellow}●${s.reset}`,
  disabled: `${s.red}●${s.reset}`,
  disconnected: `${s.dim}○${s.reset}`,
};

type Item =
  | { type: "provider"; provider: ProviderStatus }
  | { type: "account"; provider: ProviderStatus; account: AccountStatus };

let selected = 0;
let items: Item[] = [];
let message = "";
let busy = false;
let timer: Timer | null = null;

export function dashboard(): void {
  if (!process.stdin.isTTY) throw new Error("Interactive dashboard requires a TTY.");

  rebuild();
  process.stdin.setRawMode(true);
  process.stdin.resume();
  process.stdin.setEncoding("utf8");
  cursor.hide();
  screen.clear();
  render();
  timer = setInterval(render, 1_000);
  process.stdin.on("data", onKey);
  process.on("exit", cleanup);
  process.on("SIGINT", () => process.exit());
  process.on("SIGTERM", () => process.exit());
}

function rebuild(): void {
  items = [];
  for (const p of status.all()) {
    items.push({ type: "provider", provider: p });
    for (const a of p.accounts) items.push({ type: "account", provider: p, account: a });
  }
  if (selected >= items.length) selected = Math.max(0, items.length - 1);
}

function cleanup(): void {
  if (timer) clearInterval(timer);
  cursor.show();
  screen.clear();
}

function render(): void {
  cursor.home();
  line(`${s.bold} ampcode-connector${s.reset}`);
  line(`${s.dim} ↑↓ navigate · enter login/add · d disconnect · q quit${s.reset}`);
  line();

  for (let i = 0; i < items.length; i++) {
    const item = items[i]!;
    const sel = i === selected;

    if (item.type === "provider") {
      renderProvider(item.provider, sel);
    } else {
      renderAccount(item.account, sel);
    }
  }

  line();
  if (busy) line(`${s.cyan}   ⟳ waiting for browser…${s.reset}`);
  else if (message) line(`   ${message}`);
  else line();
}

function renderProvider(p: ProviderStatus, sel: boolean): void {
  const n = p.accounts.length;
  const connected = p.accounts.filter((a) => a.status === "connected").length;
  const suffix = n > 0 ? ` ${s.dim}(${connected}/${n})${s.reset}` : "";
  const label = p.label.padEnd(16);

  if (sel) line(`${s.inverse} › ${s.bold}${label}${s.reset}${s.inverse}${suffix} ${s.reset}`);
  else line(`   ${s.bold}${label}${s.reset}${suffix}`);

  if (p.sublabel) line(`     ${s.dim}${p.sublabel}${s.reset}`);
}

function renderAccount(a: AccountStatus, sel: boolean): void {
  const ic = ICON[a.status];
  const tag = `#${a.account}`.padEnd(4);
  const info = formatInfo(a);

  if (sel) line(`${s.inverse}     ${ic} ${tag} ${info} ${s.reset}`);
  else line(`     ${ic} ${s.dim}${tag}${s.reset} ${info}`);
}

function formatInfo(a: AccountStatus): string {
  if (a.status === "disconnected") return `${s.dim}—${s.reset}`;

  const parts: string[] = [];
  if (a.status === "connected") parts.push(`${s.green}connected${s.reset}`);
  else if (a.status === "disabled") parts.push(`${s.red}disabled${s.reset}`);
  else parts.push(`${s.yellow}expired${s.reset}`);
  if (a.expiresAt && a.status === "connected") parts.push(`${s.dim}${status.remaining(a.expiresAt)}${s.reset}`);
  if (a.email) parts.push(`${s.dim}${a.email}${s.reset}`);
  return parts.join(`${s.dim} · ${s.reset}`);
}

async function onKey(data: string): Promise<void> {
  if (busy) return;

  if (data === "\x03" || data === "q") return void process.exit();
  if (data === "\x1b[A") {
    selected = Math.max(0, selected - 1);
    render();
    return;
  }
  if (data === "\x1b[B") {
    selected = Math.min(items.length - 1, selected + 1);
    render();
    return;
  }

  if (data === "\r" || data === "\n") {
    const item = items[selected]!;
    await doLogin(item.provider);
    return;
  }

  if (data === "d" || data === "D") {
    const item = items[selected]!;
    if (item.type === "account") doDisconnect(item.provider, item.account.account);
    else doDisconnectAll(item.provider);
    return;
  }
}

async function doLogin(p: ProviderStatus): Promise<void> {
  busy = true;
  message = "";
  render();

  try {
    const creds = await oauth.login(oauthConfigs[p.name]);
    message = `${s.green}✓ ${p.label} ${creds.email ?? "account"} logged in${s.reset}`;
  } catch (err) {
    message = `${s.red}✗ ${err instanceof Error ? err.message : String(err)}${s.reset}`;
  }

  rebuild();
  busy = false;
  render();
}

function doDisconnect(p: ProviderStatus, account: number): 

================================================
FILE: src\config\config.ts
================================================
/** YAML config loader with env/file fallback for API key. */

import { homedir } from "node:os";
import { join } from "node:path";
import { DEFAULT_AMP_UPSTREAM_URL } from "../constants.ts";
import type { LogLevel } from "../utils/logger.ts";
import { logger } from "../utils/logger.ts";

export interface ProxyConfig {
  hostname: string;
  port: number;
  ampUpstreamUrl: string;
  ampApiKey?: string;
  exaApiKey?: string;
  logLevel: LogLevel;
  providers: {
    anthropic: boolean;
    codex: boolean;
    google: boolean;
  };
}

const DEFAULTS: ProxyConfig = {
  hostname: "localhost",
  port: 8765,
  ampUpstreamUrl: DEFAULT_AMP_UPSTREAM_URL,
  logLevel: "info",
  providers: { anthropic: true, codex: true, google: true },
};

/** Config search order: cwd → ~/.config/ampcode-connector */
const CONFIG_PATHS = [
  join(process.cwd(), "config.yaml"),
  join(homedir(), ".config", "ampcode-connector", "config.yaml"),
];
const SECRETS_PATH = join(homedir(), ".local", "share", "amp", "secrets.json");

export async function loadConfig(): Promise<ProxyConfig> {
  const file = await readConfigFile();
  const apiKey = await resolveApiKey(file);
  const providers = asRecord(file?.providers);

  const port = asNumber(file?.port) ?? DEFAULTS.port;
  if (port < 1 || port > 65535) {
    throw new Error(`Invalid port ${port}: must be between 1 and 65535`);
  }

  return {
    hostname: asString(file?.hostname) ?? process.env.HOST ?? DEFAULTS.hostname,
    port,
    ampUpstreamUrl: asString(file?.ampUpstreamUrl) ?? DEFAULTS.ampUpstreamUrl,
    ampApiKey: apiKey,
    exaApiKey: asString(file?.exaApiKey) ?? process.env.EXA_API_KEY,
    logLevel: asLogLevel(file?.logLevel) ?? DEFAULTS.logLevel,
    providers: {
      anthropic: asBool(providers?.anthropic) ?? DEFAULTS.providers.anthropic,
      codex: asBool(providers?.codex) ?? DEFAULTS.providers.codex,
      google: asBool(providers?.google) ?? DEFAULTS.providers.google,
    },
  };
}

async function readConfigFile(): Promise<Record<string, unknown> | null> {
  for (const configPath of CONFIG_PATHS) {
    const file = Bun.file(configPath);
    if (await file.exists()) {
      try {
        const text = await file.text();
        logger.info(`Loaded config from ${configPath}`);
        return Bun.YAML.parse(text) as Record<string, unknown>;
      } catch (err) {
        throw new Error(`Invalid config at ${configPath}: ${err}`);
      }
    }
  }
  return null;
}

/** Amp API key resolution: config file → AMP_API_KEY env → secrets.json */
async function resolveApiKey(file: Record<string, unknown> | null): Promise<string | undefined> {
  const fromFile = asString(file?.ampApiKey);
  if (fromFile) return fromFile;

  const fromEnv = process.env.AMP_API_KEY;
  if (fromEnv) return fromEnv;

  return readSecretsFile();
}

async function readSecretsFile(): Promise<string | undefined> {
  const file = Bun.file(SECRETS_PATH);
  if (!(await file.exists())) return undefined;
  try {
    const secrets = (await file.json()) as Record<string, unknown>;
    const canonical = asString(secrets[`apiKey@${DEFAULT_AMP_UPSTREAM_URL}/`]);
    if (canonical) return canonical;
    for (const value of Object.values(secrets)) {
      if (typeof value === "string" && value.startsWith("sgamp_")) return value;
    }
    return undefined;
  } catch (err) {
    logger.warn("Failed to read secrets.json", { error: String(err) });
    return undefined;
  }
}

function asRecord(v: unknown): Record<string, unknown> | undefined {
  return v != null && typeof v === "object" && !Array.isArray(v) ? (v as Record<string, unknown>) : undefined;
}

function asNumber(v: unknown): number | undefined {
  return typeof v === "number" && !Number.isNaN(v) ? v : undefined;
}

function asString(v: unknown): string | undefined {
  return typeof v === "string" && v.length > 0 ? v : undefined;
}

function asBool(v: unknown): boolean | undefined {
  return typeof v === "boolean" ? v : undefined;
}

const VALID_LOG_LEVELS = new Set<string>(["debug", "info", "warn", "error"]);

function asLogLevel(v: unknown): LogLevel | undefined {
  return typeof v === "string" && VALID_LOG_LEVELS.has(v) ? (v as LogLevel) : undefined;
}


================================================
FILE: src\providers\anthropic.ts
================================================
/** Forwards requests to api.anthropic.com with Claude Code stealth headers. */

import { createHash } from "node:crypto";
import { anthropic as config } from "../auth/configs.ts";
import * as oauth from "../auth/oauth.ts";
import * as store from "../auth/store.ts";
import { ANTHROPIC_API_URL, CLAUDE_CODE_VERSION, claudeCodeBetas, filteredBetaFeatures } from "../constants.ts";
import type { ParsedBody } from "../server/body.ts";
import type { Provider } from "./base.ts";
import { denied, forward } from "./forward.ts";

/** Headers to drop from client request (replaced by connector or irrelevant). */
const DROP_HEADERS = new Set(["host", "content-length", "connection", "x-api-key", "authorization", "anthropic-beta"]);

/** Extract X-Stainless-* and other passthrough headers from the client request. */
function passthroughHeaders(originalHeaders: Headers): Record<string, string> {
  const out: Record<string, string> = {};
  for (const [k, v] of originalHeaders.entries()) {
    if (DROP_HEADERS.has(k)) continue;
    // Drop amp-specific headers
    if (k.startsWith("x-amp-")) continue;
    out[k] = v;
  }
  return out;
}

export const provider: Provider = {
  name: "Anthropic",
  routeDecision: "LOCAL_CLAUDE",

  isAvailable: (account?: number) =>
    account !== undefined ? !!store.get("anthropic", account)?.refreshToken : oauth.ready(config),

  accountCount: () => oauth.accountCount(config),

  async forward(sub, body, originalHeaders, rewrite, account = 0) {
    const accessToken = await oauth.token(config, account);
    if (!accessToken) return denied("Anthropic");

    const fwdBody = prepareBody(body);
    const betaHdr = betaHeader(originalHeaders.get("anthropic-beta"));
    const clientHeaders = passthroughHeaders(originalHeaders);

    return forward({
      url: `${ANTHROPIC_API_URL}${sub}`,
      body: fwdBody,
      streaming: body.stream,
      providerName: "Anthropic",
      rewrite,
      email: store.get("anthropic", account)?.email,
      headers: {
        // Client headers first (stainless, accept, content-type, anthropic-version, etc.)
        ...clientHeaders,
        // Override auth + identity
        "Anthropic-Dangerous-Direct-Browser-Access": "true",
        "Anthropic-Beta": betaHdr,
        "User-Agent": `claude-cli/${CLAUDE_CODE_VERSION} (external, cli)`,
        "X-App": "cli",
        Authorization: `Bearer ${accessToken}`,
      },
    });
  },
};

const BILLING_SALT = "59cf53e54c78";

/** Compute the cch checksum from the first user message text and version. */
function computeCch(firstUserText: string, version: string): string {
  const chars = [4, 7, 20].map((i) => firstUserText[i] || "0").join("");
  return createHash("sha256").update(`${BILLING_SALT}${chars}${version}`).digest("hex").slice(0, 5);
}

/** Extract text from the first user message in the body. */
function firstUserText(parsed: Record<string, unknown>): string {
  const messages = parsed.messages as Array<{ role?: string; content?: unknown }> | undefined;
  if (!Array.isArray(messages)) return "";
  const userMsg = messages.find((m) => m.role === "user");
  if (!userMsg) return "";
  if (typeof userMsg.content === "string") return userMsg.content;
  if (Array.isArray(userMsg.content)) {
    const textBlock = userMsg.content.find((b: { type?: string }) => b.type === "text") as
      | { text?: string }
      | undefined;
    return textBlock?.text ?? "";
  }
  return "";
}

/** Prepare body: inject billing header + strip speed field.
 *  Always re-injects billing header because cch depends on per-request message content.
 *  Shallow-copies parsed to avoid mutating the shared ParsedBody.parsed reference. */
function prepareBody(body: ParsedBody): string {
  const raw = body.forwardBody;

  try {
    const original = body.parsed;
    if (!original) return raw;

    const text = firstUserText(original);
    const cch = computeCch(text, CLAUDE_CODE_VERSION);
    const billingLine = `x-anthropic-billing-header: cc_version=${CLAUDE_CODE_VERSION}; cc_entrypoint=cli; cch=${cch};`;

    const { speed: _, system: existingSystem, ...rest } = original;

    return JSON.stringify({
      ...rest,
      system: injectBillingHeader(existingSystem, billingLine),
    });
  } catch {
    return raw;
  }
}

/** Prepend the billing header into the system prompt, handling both array and string formats. */
function injectBillingHeader(system: unknown, billingLine: string): unknown {
  if (Array.isArray(system)) {
    const filtered = system.filter(
      (s: { text?: string }) => !(typeof s.text === "string" && s.text.includes("x-anthropic-billing-header")),
    );
    return [{ type: "text", text: billingLine }, ...filtered];
  }
  if (typeof system === "string") {
    return `${billingLine}\n${system.replace(/x-anthropic-billing-header:[^\n]*\n?/, "")}`;
  }
  return [{ type: "text", text: billingLine }];
}

function betaHeader(original: string | null): string {
  const features = new Set<string>(claudeCodeBetas);

  if (original)

================================================
FILE: src\providers\base.ts
================================================
/** Provider interface — the contract every provider must implement. */

import type { ParsedBody } from "../server/body.ts";
import type { RouteDecision } from "../utils/logger.ts";

export interface Provider {
  readonly name: string;
  readonly routeDecision: RouteDecision;
  isAvailable(account?: number): boolean;
  accountCount(): number;
  forward(
    path: string,
    body: ParsedBody,
    headers: Headers,
    rewrite?: (data: string) => string,
    account?: number,
  ): Promise<Response>;
}


================================================
FILE: src\providers\codex-sse.ts
================================================
/** Transforms Responses API SSE events → Chat Completions SSE chunks.
 *
 *  Codex backend returns Responses API format (response.output_text.delta, etc.)
 *  but Amp CLI expects Chat Completions format (chat.completion.chunk). */

import * as sse from "../utils/streaming.ts";

interface CompletionChunk {
  id: string;
  object: "chat.completion.chunk";
  created: number;
  model: string;
  choices: Choice[];
  usage?: Usage | null;
}

interface Choice {
  index: number;
  delta: Delta;
  finish_reason: string | null;
}

interface Delta {
  role?: string;
  content?: string;
  reasoning_content?: string;
  tool_calls?: ToolCallDelta[];
}

interface ToolCallDelta {
  index: number;
  id?: string;
  type?: string;
  function?: { name?: string; arguments?: string };
}

interface Usage {
  prompt_tokens: number;
  completion_tokens: number;
  total_tokens: number;
  prompt_tokens_details?: { cached_tokens: number };
  completion_tokens_details?: { reasoning_tokens: number };
}

interface TransformState {
  responseId: string;
  model: string;
  created: number;
  toolCallIndex: number;
  /** Track active tool call IDs to assign sequential indices. */
  toolCallIds: Map<string, number>;
}

/** Resolve tool call index from item_id or call_id, falling back to 0. */
function lookupToolIndex(state: TransformState, itemId?: string, callId?: string): number {
  if (itemId) {
    const idx = state.toolCallIds.get(itemId);
    if (idx !== undefined) return idx;
  }
  if (callId) {
    const idx = state.toolCallIds.get(callId);
    if (idx !== undefined) return idx;
  }
  return 0;
}

/** Create a stateful SSE transformer: Responses API → Chat Completions. */
function createResponseTransformer(ampModel: string): (data: string) => string {
  const state: TransformState = {
    responseId: "",
    model: ampModel,
    created: Math.floor(Date.now() / 1000),
    toolCallIndex: 0,
    toolCallIds: new Map(),
  };

  return (data: string): string => {
    if (data === "[DONE]") return "";

    let parsed: Record<string, unknown>;
    try {
      parsed = JSON.parse(data) as Record<string, unknown>;
    } catch {
      return data;
    }

    const eventType = parsed.type as string | undefined;
    if (!eventType) return data;

    // Extract response metadata on creation
    if (eventType === "response.created") {
      const resp = parsed.response as Record<string, unknown>;
      state.responseId = (resp?.id as string) ?? state.responseId;
      state.model = ampModel;
      state.created = (resp?.created_at as number) ?? state.created;
      // Don't emit a chunk for response.created
      return "";
    }

    switch (eventType) {
      // Assistant message started — emit role
      case "response.output_item.added": {
        const item = parsed.item as Record<string, unknown>;
        if (item?.type === "message" && item.role === "assistant") {
          return serialize(state, { role: "assistant", content: "" });
        }
        if (item?.type === "function_call") {
          const callId = item.call_id as string;
          const itemId = item.id as string | undefined;
          const name = item.name as string;
          const idx = state.toolCallIndex++;
          state.toolCallIds.set(callId, idx);
          if (itemId) state.toolCallIds.set(itemId, idx);
          return serialize(state, {
            tool_calls: [{ index: idx, id: callId, type: "function", function: { name, arguments: "" } }],
          });
        }
        return "";
      }

      // Text content delta
      case "response.output_text.delta": {
        const delta = parsed.delta as string;
        if (delta) return serialize(state, { content: delta });
        return "";
      }

      // Function call arguments delta
      case "response.function_call_arguments.delta": {
        const delta = parsed.delta as string;
        const itemId = parsed.item_id as string | undefined;
        const callId = parsed.call_id as string | undefined;
        if (delta) {
          const idx = lookupToolIndex(state, itemId, callId);
          return serialize(state, { tool_calls: [{ index: idx, function: { arguments: delta } }] });
        }
        return "";
      }

      // Response completed — emit finish_reason + usage
      case "response.completed": {
        const resp = parsed.response as Record<string, unknown>;
        const usage = extractUsage(resp?.usage as Record<string, unknown> | undefined);
        const hasToolCalls = state.toolCallIndex > 0;
        const finishReason = hasToolCalls ? "tool_calls" : "stop";
        return serializeFinish(state, finishReason, usage);
      }

      // Response incomplete — inspect reason to determine finish_reason
      case "response.incomplete": {
        const resp = parsed.response as Record<string, unknown>;
        const usage = extractUsage(resp?.usage as Record<string, unknown> | undefined);
        const finishReason = incompleteReason(resp);
        return serializeFinish(state, finishReason, 

================================================
FILE: src\providers\codex-state.ts
================================================
/** In-memory conversation state for Responses API previous_response_id support.
 *
 *  Each response is stored with its expanded input + output. When a follow-up
 *  request references previous_response_id, the stored input and output are
 *  prepended to build the full conversation context. Because we store the
 *  already-expanded input, recursive chains resolve in O(1) — no traversal. */

import * as sse from "../utils/streaming.ts";

const MAX_ENTRIES = 500;
const TTL_MS = 30 * 60 * 1000; // 30 minutes

interface StoredResponse {
  input: unknown[];
  output: unknown[];
  instructions: string | null;
  createdAt: number;
}

const responses = new Map<string, StoredResponse>();

// ---------------------------------------------------------------------------
// Public API
// ---------------------------------------------------------------------------

/** Store a completed response for future previous_response_id lookups. */
export function store(id: string, input: unknown[], output: unknown[], instructions: string | null): void {
  if (responses.size >= MAX_ENTRIES) evict();
  responses.set(id, { input, output, instructions, createdAt: Date.now() });
}

/** Expand previous_response_id: prepend stored context to current input.
 *  Returns null if the referenced response is not found (expired or invalid). */
export function expand(
  previousResponseId: string,
  currentInput: unknown[],
  currentInstructions: string | null,
): { input: unknown[]; instructions: string | null } | null {
  const stored = responses.get(previousResponseId);
  if (!stored) return null;
  if (Date.now() - stored.createdAt > TTL_MS) {
    responses.delete(previousResponseId);
    return null;
  }

  return {
    input: [...stored.input, ...stored.output, ...currentInput],
    instructions: currentInstructions ?? stored.instructions,
  };
}

// ---------------------------------------------------------------------------
// SSE response capture — extract id + output from Codex SSE stream
// ---------------------------------------------------------------------------

/** Extract the full response object from a Codex SSE stream (for non-streaming / buffer path).
 *  Returns the parsed response from `response.completed` or `response.failed`. */
export async function bufferResponseJson(response: Response): Promise<Record<string, unknown> | null> {
  if (!response.body) return null;

  const decoder = new TextDecoder();
  let sseBuffer = "";
  let fullResponse: Record<string, unknown> | null = null;

  const reader = response.body.getReader();
  for (;;) {
    const { done, value } = await reader.read();
    if (done) break;

    sseBuffer += decoder.decode(value, { stream: true }).replaceAll("\r\n", "\n");
    const boundary = sseBuffer.lastIndexOf("\n\n");
    if (boundary === -1) continue;

    const complete = sseBuffer.slice(0, boundary + 2);
    sseBuffer = sseBuffer.slice(boundary + 2);
    fullResponse = extractCompleted(complete) ?? fullResponse;
  }

  if (sseBuffer.trim()) {
    fullResponse = extractCompleted(sseBuffer) ?? fullResponse;
  }

  return fullResponse;
}

/** Wrap a SSE stream to capture response state while passing all data through unchanged.
 *  Zero latency — chunks are forwarded immediately, state is captured as a side-effect
 *  when `response.completed` or `response.failed` passes through. */
export function withStateCapture(
  stream: ReadableStream<Uint8Array>,
  expandedInput: unknown[],
  instructions: string | null,
): ReadableStream<Uint8Array> {
  const decoder = new TextDecoder();
  let buffer = "";

  return stream.pipeThrough(
    new TransformStream<Uint8Array, Uint8Array>({
      transform(raw, controller) {
        controller.enqueue(raw);

        buffer += decoder.decode(raw, { stream: true }).replaceAll("\r\n", "\n");
        const boundary = buffer.lastIndexOf("\n\n");
        if (boundary === -1) return;

        const complete = buffer.slice(0, boundary + 2);
        buffer = buffer.slice(boundary + 2);
        captureFromChunk(complete, expandedInput, instructions);
      },
      flush() {
        if (buffer.trim()) {
          captureFromChunk(buffer, expandedInput, instructions);
        }
      },
    }),
  );
}

// ---------------------------------------------------------------------------
// Internals
// ---------------------------------------------------------------------------

function captureFromChunk(raw: string, expandedInput: unknown[], instructions: string | null): void {
  for (const chunk of sse.parse(raw)) {
    if (chunk.data === "[DONE]") continue;
    try {
      const parsed = JSON.parse(chunk.data) as Record<string, unknown>;
      const type = parsed.type as string | undefined;
      if (type === "response.completed" || type === "response.failed") {
        const resp = parsed.response as Record<string, unknown> | undefined;
        if (resp?.id) {
          const output = Array.isArray(resp.output) ? (resp.output as unknown[]) : [];
          store(resp.id as string,

================================================
FILE: src\providers\codex.ts
================================================
/** Forwards requests to chatgpt.com/backend-api/codex with Codex CLI OAuth token.
 *
 *  The ChatGPT backend only accepts the Responses API format (input[] + instructions),
 *  but Amp CLI sends Chat Completions format (messages[]). This module transforms
 *  the request body before forwarding.
 *
 *  Forward flow (5 steps):
 *    1. AUTH    — acquire OAuth access token
 *    2. EXPAND  — resolve previous_response_id → full input (codex-state)
 *    3. PREPARE — transform body for Codex backend
 *    4. FORWARD — send to Codex backend
 *    5. PROCESS — format response + capture state for future turns */

import { codex as config } from "../auth/configs.ts";
import * as oauth from "../auth/oauth.ts";
import * as store from "../auth/store.ts";
import { CODEX_BASE_URL, codexHeaders, codexHeaderValues, codexPathMap } from "../constants.ts";
import { fromBase64url } from "../utils/encoding.ts";
import { logger } from "../utils/logger.ts";
import { apiError } from "../utils/responses.ts";
import type { Provider } from "./base.ts";
import { bufferCodexResponse, transformCodexResponse } from "./codex-sse.ts";
import * as state from "./codex-state.ts";
import { denied, forward } from "./forward.ts";

const DEFAULT_INSTRUCTIONS = "You are an expert coding assistant.";

export const provider: Provider = {
  name: "OpenAI Codex",
  routeDecision: "LOCAL_CODEX",

  isAvailable: (account?: number) =>
    account !== undefined ? !!store.get("codex", account)?.refreshToken : oauth.ready(config),

  accountCount: () => oauth.accountCount(config),

  async forward(sub, body, originalHeaders, rewrite, account = 0) {
    // 1. AUTH
    const accessToken = await oauth.token(config, account);
    if (!accessToken) return denied("OpenAI Codex");

    const accountId = getAccountId(accessToken, account);
    const codexPath = codexPathMap[sub] ?? sub;
    const promptCacheKey = originalHeaders.get("x-amp-thread-id") ?? originalHeaders.get("x-session-id") ?? undefined;

    // 2. EXPAND — resolve previous_response_id before body transform
    const expandedBody = expandPreviousResponse(body.forwardBody);
    if (expandedBody === null) {
      return apiError(400, "previous_response_id references an unknown or expired response");
    }

    // 3. PREPARE — transform body for Codex backend
    const {
      body: codexBody,
      needsResponseTransform,
      expandedInput,
      instructions,
    } = transformForCodex(expandedBody, promptCacheKey);
    const ampModel = body.ampModel ?? "gpt-5.2";

    // 4. FORWARD
    const response = await forward({
      url: `${CODEX_BASE_URL}${codexPath}`,
      body: codexBody,
      streaming: body.stream,
      providerName: "OpenAI Codex",
      rewrite: needsResponseTransform ? undefined : rewrite,
      email: store.get("codex", account)?.email,
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${accessToken}`,
        Accept: body.stream ? "text/event-stream" : "application/json",
        Connection: "Keep-Alive",
        [codexHeaders.BETA]: codexHeaderValues.BETA_RESPONSES,
        [codexHeaders.ORIGINATOR]: codexHeaderValues.ORIGINATOR,
        "User-Agent": codexHeaderValues.USER_AGENT,
        Version: codexHeaderValues.VERSION,
        ...(accountId ? { [codexHeaders.ACCOUNT_ID]: accountId } : {}),
        ...(promptCacheKey
          ? { [codexHeaders.SESSION_ID]: promptCacheKey, [codexHeaders.CONVERSATION_ID]: promptCacheKey }
          : {}),
      },
    });

    // 5. PROCESS — format response + capture state
    if (!response.ok) return response;

    // Chat Completions path — transform only, no state capture
    if (needsResponseTransform) {
      return body.stream ? transformCodexResponse(response, ampModel) : bufferCodexResponse(response, ampModel);
    }

    // Responses API path — capture state + format
    return body.stream
      ? processStreamingResponse(response, expandedInput, instructions)
      : processBufferedResponse(response, expandedInput, instructions);
  },
};

// ---------------------------------------------------------------------------
// Step 2: Expand previous_response_id
// ---------------------------------------------------------------------------

/** Resolve previous_response_id into expanded input. Returns the (possibly modified) body string,
 *  or null if the referenced response was not found. */
function expandPreviousResponse(rawBody: string): string | null {
  if (!rawBody) return rawBody;

  let parsed: Record<string, unknown>;
  try {
    parsed = JSON.parse(rawBody) as Record<string, unknown>;
  } catch {
    return rawBody;
  }

  const prevId = parsed.previous_response_id as string | undefined;
  if (!prevId) return rawBody;

  const currentInput = Array.isArray(parsed.input) ? (parsed.input as unknown[]) : [];
  const currentInstructions = (parsed.instructions as string) ?? null;
  const expanded = state.expand(prevId, currentInput, currentInstructions);
  if (!expanded) {
    logger.warn(

================================================
FILE: src\providers\forward.ts
================================================
/** HTTP forwarding with transport-level retry, SSE proxying, and response rewriting. */

import { logger } from "../utils/logger.ts";
import { apiError } from "../utils/responses.ts";
import * as sse from "../utils/streaming.ts";

export interface ForwardOptions {
  url: string;
  body: string;
  streaming: boolean;
  headers: Record<string, string>;
  providerName: string;
  rewrite?: (data: string) => string;
  email?: string;
}

const RETRYABLE_STATUS = new Set([408, 500, 502, 503, 504]);
const MAX_RETRIES = 3;
const RETRY_DELAY_MS = 500;

const PASSTHROUGH_HEADERS = [
  "content-type",
  "retry-after",
  "x-request-id",
  "x-ratelimit-limit-requests",
  "x-ratelimit-remaining-requests",
  "x-ratelimit-reset-requests",
];

function copyHeaders(source: Headers): Headers {
  const dest = new Headers();
  for (const name of PASSTHROUGH_HEADERS) {
    const value = source.get(name);
    if (value !== null) dest.set(name, value);
  }
  return dest;
}

export async function forward(opts: ForwardOptions): Promise<Response> {
  for (let attempt = 0; attempt <= MAX_RETRIES; attempt++) {
    let response: Response;
    try {
      response = await fetch(opts.url, {
        method: "POST",
        headers: opts.headers,
        body: opts.body,
      });
    } catch (err) {
      if (attempt < MAX_RETRIES) {
        logger.debug(`${opts.providerName} fetch error, retry ${attempt + 1}/${MAX_RETRIES}`, {
          error: String(err),
        });
        await Bun.sleep(RETRY_DELAY_MS * (attempt + 1));
        continue;
      }
      return transportErrorResponse(opts.providerName, err);
    }

    // Retry on server errors (429 handled at routing layer)
    if (RETRYABLE_STATUS.has(response.status) && attempt < MAX_RETRIES) {
      await response.text(); // consume body
      logger.debug(`${opts.providerName} returned ${response.status}, retry ${attempt + 1}/${MAX_RETRIES}`);
      await Bun.sleep(RETRY_DELAY_MS * (attempt + 1));
      continue;
    }

    const contentType = response.headers.get("Content-Type") ?? "application/json";

    if (!response.ok) {
      const text = await response.text();
      const ctx = opts.email ? ` account=${opts.email}` : "";
      logger.error(`${opts.providerName} API error (${response.status})${ctx}`, { error: text.slice(0, 200) });

      // Normalize non-standard error responses (e.g. {"detail":"..."}) to OpenAI format
      // so Amp CLI can deserialize them (it expects {"error": {...}})
      let errorBody = text;
      try {
        const parsed = JSON.parse(text) as Record<string, unknown>;
        if (!parsed.error) {
          const message = (parsed.detail as string) ?? (parsed.message as string) ?? text;
          errorBody = JSON.stringify({
            error: { message, type: "api_error", code: String(response.status) },
          });
        }
      } catch {
        // Not JSON — wrap raw text
        errorBody = JSON.stringify({
          error: { message: text, type: "api_error", code: String(response.status) },
        });
      }

      const headers = copyHeaders(response.headers);
      headers.set("Content-Type", "application/json");
      return new Response(errorBody, {
        status: response.status,
        headers,
      });
    }

    const isSSE = contentType.includes("text/event-stream") || opts.streaming;
    if (isSSE) return sse.proxy(response, opts.rewrite);

    const headers = copyHeaders(response.headers);

    if (opts.rewrite) {
      const text = await response.text();
      return new Response(opts.rewrite(text), { status: response.status, headers });
    }

    return new Response(response.body, { status: response.status, headers });
  }

  // Unreachable, but TypeScript needs it
  throw new Error(`${opts.providerName}: all retries exhausted`);
}

export function denied(providerName: string): Response {
  return apiError(401, `No ${providerName} OAuth token available. Run login first.`);
}

function transportErrorResponse(providerName: string, err: unknown): Response {
  const message = transportErrorMessage(providerName, err);
  logger.error(`${providerName} transport error after retries exhausted`, { error: String(err) });
  return apiError(502, message, "connection_error");
}

function transportErrorMessage(providerName: string, err: unknown): string {
  const base = `${providerName} connection error after retries were exhausted.`;
  const details = String(err);

  if (providerName !== "Anthropic") {
    return `${base} ${details}`;
  }

  const looksLikeReset =
    details.includes("ECONNRESET") ||
    details.includes("socket connection was closed unexpectedly") ||
    details.includes("tls") ||
    details.includes("network");

  if (!looksLikeReset) {
    return `${base} ${details}`;
  }

  return `${base} ${details} This is often a local network issue rather than an OAuth bug: check Wi-Fi MTU (1492 is a common fix), hotspot stability, and iPhone dual-SIM Cellular Data Switching if you are tethering.`;
}


================================================
FILE: src\providers\google.ts
================================================
/** Unified Google provider — merges Gemini CLI and Antigravity strategies
 *  with internal fallback. Tries preferred strategy first, then falls back. */

import { google as config } from "../auth/configs.ts";
import * as oauth from "../auth/oauth.ts";
import * as store from "../auth/store.ts";
import { ANTIGRAVITY_DAILY_ENDPOINT, ANTIGRAVITY_DAILY_SANDBOX_ENDPOINT, CODE_ASSIST_ENDPOINT } from "../constants.ts";
import { buildUrl, maybeWrap, withUnwrap } from "../utils/code-assist.ts";
import { logger } from "../utils/logger.ts";
import * as path from "../utils/path.ts";
import { apiError } from "../utils/responses.ts";
import type { Provider } from "./base.ts";
import { denied, forward } from "./forward.ts";

const GOOGLE_CLIENT_METADATA = JSON.stringify({
  ideType: "IDE_UNSPECIFIED",
  platform: "PLATFORM_UNSPECIFIED",
  pluginType: "GEMINI",
});

interface GoogleStrategy {
  name: string;
  headers: Readonly<Record<string, string>>;
  endpoints: readonly string[];
  modelMapper?: (model: string) => string;
  wrapOpts: {
    userAgent: "antigravity" | "pi-coding-agent";
    requestIdPrefix: "agent" | "pi";
    requestType?: "agent" | "image_gen";
  };
}

const geminiStrategy: GoogleStrategy = {
  name: "gemini",
  headers: {
    "User-Agent": "google-cloud-sdk vscode_cloudshelleditor/0.1",
    "X-Goog-Api-Client": "gl-node/22.17.0",
    "Client-Metadata": GOOGLE_CLIENT_METADATA,
  },
  endpoints: [CODE_ASSIST_ENDPOINT],
  wrapOpts: {
    userAgent: "pi-coding-agent",
    requestIdPrefix: "pi",
  },
};

/** Antigravity uses different model names than what Amp CLI sends. */
const antigravityModelMap: Record<string, string> = {
  "gemini-3-flash-preview": "gemini-3-flash",
  "gemini-3-pro-preview": "gemini-3-pro-high",
  "gemini-3-pro-image-preview": "gemini-3.1-flash-image",
  "gemini-3.1-flash-image-preview": "gemini-3.1-flash-image",
};

const antigravityStrategy: GoogleStrategy = {
  name: "antigravity",
  headers: {
    "User-Agent": "antigravity/1.104.0 darwin/arm64",
    "X-Goog-Api-Client": "google-cloud-sdk vscode_cloudshelleditor/0.1",
    "Client-Metadata": GOOGLE_CLIENT_METADATA,
  },
  endpoints: [ANTIGRAVITY_DAILY_ENDPOINT, ANTIGRAVITY_DAILY_SANDBOX_ENDPOINT, CODE_ASSIST_ENDPOINT],
  modelMapper: (model: string) => antigravityModelMap[model] ?? model,
  wrapOpts: {
    userAgent: "antigravity",
    requestIdPrefix: "agent",
    requestType: "agent",
  },
};

const strategies: readonly GoogleStrategy[] = [geminiStrategy, antigravityStrategy];

/** Models that only work on the antigravity strategy. */
const ANTIGRAVITY_ONLY_MODELS = new Set(["gemini-3-pro-image-preview", "gemini-3.1-flash-image-preview"]);

const COOLDOWN_MS = 60_000;

interface StrategyPreference {
  strategy: GoogleStrategy;
  until: number;
}

// Per-account strategy preference: after success, prefer that strategy;
// after failure, skip it for COOLDOWN_MS.
const preferredStrategy = new Map<number, StrategyPreference>();
const cooldowns = new Map<string, number>(); // key: `${account}:${strategy.name}`

function cooldownKey(account: number, strategy: GoogleStrategy): string {
  return `${account}:${strategy.name}`;
}

function getOrderedStrategies(account: number, model?: string): GoogleStrategy[] {
  const now = Date.now();

  // Some models only work on antigravity — skip other strategies entirely
  if (model && ANTIGRAVITY_ONLY_MODELS.has(model)) {
    const cd = cooldowns.get(cooldownKey(account, antigravityStrategy));
    if (cd && cd > now) return [];
    return [antigravityStrategy];
  }

  const pref = preferredStrategy.get(account);
  const ordered =
    pref && pref.until > now ? [pref.strategy, ...strategies.filter((s) => s !== pref.strategy)] : [...strategies];

  return ordered.filter((s) => {
    const cd = cooldowns.get(cooldownKey(account, s));
    return !cd || cd <= now;
  });
}

function markSuccess(account: number, strategy: GoogleStrategy): void {
  preferredStrategy.set(account, { strategy, until: Date.now() + COOLDOWN_MS * 10 });
  cooldowns.delete(cooldownKey(account, strategy));
}

function markFailure(account: number, strategy: GoogleStrategy): void {
  cooldowns.set(cooldownKey(account, strategy), Date.now() + COOLDOWN_MS);
  const pref = preferredStrategy.get(account);
  if (pref?.strategy === strategy) {
    preferredStrategy.delete(account);
  }
}

/** Buffer an SSE response and merge all chunks into a single JSON response.
 *  Used when we force streamGenerateContent but the client expects non-streaming JSON.
 *  Accumulates all candidate parts across chunks (image inlineData may be in earlier chunks). */
async function bufferSSEToJSON(response: Response): Promise<Response | null> {
  const text = await response.text();
  const chunks: Record<string, unknown>[] = [];

  for (const line of text.split("\n")) {
    if (!line.startsWith("data: ")) continue;
    const data = line.slice(6).trim();
    if (!data || data === "[DONE]") continue;
    try {
      chunks.push(JSON.parse(data) as Record<str

================================================
FILE: src\proxy\rewriter.ts
================================================
/**
 * SSE response rewriting: model name substitution + thinking block suppression.
 *
 * Thinking blocks are filtered when tool_use is present because the Amp client
 * struggles with both simultaneously (ref: CLIProxyAPI response_rewriter.go:72-94).
 */

import { modelFieldPaths } from "../constants.ts";

/** Pre-split field paths — avoids .split(".") on every SSE chunk. */
const MODEL_FIELD_PARTS = modelFieldPaths.map((p) => p.split("."));

export function rewrite(originalModel: string): (data: string) => string {
  return (data: string) => {
    if (data === "[DONE]") return data;

    try {
      const parsed = JSON.parse(data) as Record<string, unknown>;
      let modified = false;

      for (const parts of MODEL_FIELD_PARTS) {
        const current = getField(parsed, parts);
        if (current !== undefined && current !== originalModel) {
          setField(parsed, parts, originalModel);
          modified = true;
        }
      }

      if (suppressThinking(parsed)) modified = true;

      return modified ? JSON.stringify(parsed) : data;
    } catch {
      return data;
    }
  };
}

function getField(obj: Record<string, unknown>, parts: string[]): unknown {
  let current: unknown = obj;
  for (const part of parts) {
    if (current == null || typeof current !== "object") return undefined;
    current = (current as Record<string, unknown>)[part];
  }
  return current;
}

function setField(obj: Record<string, unknown>, parts: string[], value: unknown): void {
  let current: unknown = obj;
  for (let i = 0; i < parts.length - 1; i++) {
    if (current == null || typeof current !== "object") return;
    current = (current as Record<string, unknown>)[parts[i]!];
  }
  if (current != null && typeof current === "object") {
    (current as Record<string, unknown>)[parts[parts.length - 1]!] = value;
  }
}

function suppressThinking(data: Record<string, unknown>): boolean {
  const content = data.content;
  if (!Array.isArray(content)) return false;

  const hasToolUse = content.some((b: Record<string, unknown>) => b.type === "tool_use");
  if (!hasToolUse) return false;

  const hasThinking = content.some((b: Record<string, unknown>) => b.type === "thinking");
  if (!hasThinking) return false;

  data.content = content.filter((b: Record<string, unknown>) => b.type !== "thinking");
  return true;
}


================================================
FILE: src\proxy\upstream.ts
================================================
/** Reverse proxy to ampcode.com for non-intercepted routes and fallback. */

import { logger } from "../utils/logger.ts";

export async function forward(request: Request, ampUpstreamUrl: string, ampApiKey?: string): Promise<Response> {
  const url = new URL(request.url);
  const upstreamUrl = new URL(url.pathname + url.search, ampUpstreamUrl);

  const upstreamHost = new URL(ampUpstreamUrl).host;
  const headers = new Headers(request.headers);
  if (ampApiKey) headers.set("Authorization", `Bearer ${ampApiKey}`);
  headers.set("Host", upstreamHost);

  logger.debug("Forwarding to Amp upstream", { provider: "amp" });

  try {
    const response = await fetch(upstreamUrl.toString(), {
      method: request.method,
      headers,
      redirect: "manual",
      body: request.method !== "GET" && request.method !== "HEAD" ? request.body : undefined,
      duplex: "half" as const,
    });

    const responseHeaders = new Headers(response.headers);
    responseHeaders.delete("Content-Encoding");
    responseHeaders.delete("Content-Length");

    return new Response(response.body, {
      status: response.status,
      statusText: response.statusText,
      headers: responseHeaders,
    });
  } catch (err) {
    logger.error("Upstream proxy error", { error: String(err) });
    return Response.json({ error: "Failed to connect to Amp upstream", details: String(err) }, { status: 502 });
  }
}


================================================
FILE: src\routing\affinity.ts
================================================
/** Thread+provider → (quotaPool, account) affinity map.
 *  Ensures a thread sticks to the same account per provider for session consistency.
 *  Key is composite (threadId, ampProvider) so a single thread can hold
 *  independent affinities for different providers (e.g. anthropic AND google). */

import type { QuotaPool } from "./cooldown.ts";

interface AffinityEntry {
  pool: QuotaPool;
  account: number;
  lastUsedAt: number;
}

/** Affinity expires after 2 hours of inactivity. */
const TTL_MS = 2 * 3600_000;
/** Cleanup stale entries every 10 minutes. */
const CLEANUP_INTERVAL_MS = 10 * 60_000;

class AffinityStore {
  private map = new Map<string, AffinityEntry>();
  private counts = new Map<string, number>();
  private cleanupTimer: Timer | null = null;

  private key(threadId: string, ampProvider: string): string {
    return `${threadId}\0${ampProvider}`;
  }

  private countKey(pool: QuotaPool, account: number): string {
    return `${pool}:${account}`;
  }

  private incCount(pool: QuotaPool, account: number): void {
    const k = this.countKey(pool, account);
    this.counts.set(k, (this.counts.get(k) ?? 0) + 1);
  }

  private decCount(pool: QuotaPool, account: number): void {
    const k = this.countKey(pool, account);
    const v = (this.counts.get(k) ?? 0) - 1;
    if (v <= 0) this.counts.delete(k);
    else this.counts.set(k, v);
  }

  private removeExpired(k: string, entry: AffinityEntry): void {
    this.map.delete(k);
    this.decCount(entry.pool, entry.account);
  }

  /** Read affinity without side effects. Returns undefined if expired or missing. */
  peek(threadId: string, ampProvider: string): AffinityEntry | undefined {
    const k = this.key(threadId, ampProvider);
    const entry = this.map.get(k);
    if (!entry) return undefined;
    if (Date.now() - entry.lastUsedAt > TTL_MS) {
      this.removeExpired(k, entry);
      return undefined;
    }
    return entry;
  }

  /** Read affinity and touch (extend TTL). */
  get(threadId: string, ampProvider: string): AffinityEntry | undefined {
    const entry = this.peek(threadId, ampProvider);
    if (entry) entry.lastUsedAt = Date.now();
    return entry;
  }

  set(threadId: string, ampProvider: string, pool: QuotaPool, account: number): void {
    const k = this.key(threadId, ampProvider);
    const existing = this.map.get(k);
    if (existing) {
      if (existing.pool !== pool || existing.account !== account) {
        this.decCount(existing.pool, existing.account);
        this.incCount(pool, account);
      }
    } else {
      this.incCount(pool, account);
    }
    this.map.set(k, { pool, account, lastUsedAt: Date.now() });
  }

  /** Break affinity when account is exhausted — allow re-routing. */
  clear(threadId: string, ampProvider: string): void {
    const k = this.key(threadId, ampProvider);
    const existing = this.map.get(k);
    if (existing) {
      this.decCount(existing.pool, existing.account);
      this.map.delete(k);
    }
  }

  /** Count active threads pinned to a specific (pool, account). */
  activeCount(pool: QuotaPool, account: number): number {
    return this.counts.get(this.countKey(pool, account)) ?? 0;
  }

  /** Start periodic cleanup of expired entries. Call once at server startup. */
  startCleanup(): void {
    if (this.cleanupTimer) return;
    this.cleanupTimer = setInterval(() => {
      const now = Date.now();
      for (const [k, entry] of this.map) {
        if (now - entry.lastUsedAt > TTL_MS) {
          this.removeExpired(k, entry);
        }
      }
    }, CLEANUP_INTERVAL_MS);
  }

  reset(): void {
    this.map.clear();
    this.counts.clear();
    if (this.cleanupTimer) {
      clearInterval(this.cleanupTimer);
      this.cleanupTimer = null;
    }
  }
}

/** Singleton instance for production use. */
export const affinity = new AffinityStore();


================================================
FILE: src\routing\cooldown.ts
================================================
/** Per-(quotaPool, account) cooldown tracking.
 *  Distinguishes short burst 429s from quota exhaustion. */

import { logger } from "../utils/logger.ts";

export type QuotaPool = "anthropic" | "codex" | "google";

interface CooldownEntry {
  until: number;
  exhausted: boolean;
  consecutive429: number;
}

/** When detected as exhausted, cooldown for this long. */
/** 403 = account disabled/revoked — long cooldown. */
const FORBIDDEN_COOLDOWN_MS = 24 * 3600_000;
const EXHAUSTED_COOLDOWN_MS = 2 * 3600_000;
/** Retry-After threshold (seconds) above which we consider quota exhausted. */
const EXHAUSTED_THRESHOLD_S = 300;
/** Consecutive 429 count to trigger exhaustion detection. */
const EXHAUSTED_CONSECUTIVE = 3;
/** Default burst cooldown when no Retry-After header. */
const DEFAULT_BURST_S = 30;

class CooldownTracker {
  private entries = new Map<string, CooldownEntry>();

  private key(pool: QuotaPool, account: number): string {
    return `${pool}:${account}`;
  }

  private getEntry(pool: QuotaPool, account: number): CooldownEntry | undefined {
    const k = this.key(pool, account);
    const entry = this.entries.get(k);
    if (!entry) return undefined;
    if (Date.now() >= entry.until) {
      this.entries.delete(k);
      return undefined;
    }
    return entry;
  }

  isCoolingDown(pool: QuotaPool, account: number): boolean {
    return this.getEntry(pool, account) !== undefined;
  }

  isExhausted(pool: QuotaPool, account: number): boolean {
    return this.getEntry(pool, account)?.exhausted ?? false;
  }

  record429(pool: QuotaPool, account: number, retryAfterSeconds?: number): void {
    const k = this.key(pool, account);
    const entry = this.entries.get(k) ?? { until: 0, exhausted: false, consecutive429: 0 };

    entry.consecutive429++;
    const retryAfter = retryAfterSeconds ?? DEFAULT_BURST_S;

    if (retryAfter > EXHAUSTED_THRESHOLD_S || entry.consecutive429 >= EXHAUSTED_CONSECUTIVE) {
      entry.exhausted = true;
      entry.until = Date.now() + EXHAUSTED_COOLDOWN_MS;
      logger.warn(`Quota exhausted: ${k}`, { cooldownMinutes: EXHAUSTED_COOLDOWN_MS / 60_000 });
    } else {
      entry.until = Date.now() + retryAfter * 1000;
      logger.debug(`Burst cooldown: ${k}`, { retryAfterSeconds: retryAfter });
    }

    this.entries.set(k, entry);
  }

  /** 403 = account forbidden/revoked. Immediately disable for 24h. */
  record403(pool: QuotaPool, account: number): void {
    const k = this.key(pool, account);
    this.entries.set(k, { until: Date.now() + FORBIDDEN_COOLDOWN_MS, exhausted: true, consecutive429: 0 });
    logger.warn(`Account disabled (403): ${k}`, { cooldownHours: FORBIDDEN_COOLDOWN_MS / 3600_000 });
  }

  /** Return shortest remaining wait (ms) among non-exhausted entries for the given candidates.
   *  Returns undefined if no candidates are cooling down or all are exhausted. */
  shortestBurstWait(candidates: { pool: QuotaPool; account: number }[]): number | undefined {
    let shortest: number | undefined;
    const now = Date.now();
    for (const c of candidates) {
      const entry = this.entries.get(this.key(c.pool, c.account));
      if (!entry || entry.exhausted) continue;
      const remaining = entry.until - now;
      if (remaining > 0 && (shortest === undefined || remaining < shortest)) {
        shortest = remaining;
      }
    }
    return shortest;
  }

  recordSuccess(pool: QuotaPool, account: number): void {
    this.entries.delete(this.key(pool, account));
  }

  reset(): void {
    this.entries.clear();
  }
}

/** Singleton instance for production use. */
export const cooldown = new CooldownTracker();

/** Parse Retry-After header (seconds or HTTP-date). */
export function parseRetryAfter(header: string | null): number | undefined {
  if (!header) return undefined;
  const seconds = Number(header);
  if (!Number.isNaN(seconds)) return seconds;
  const date = Date.parse(header);
  if (!Number.isNaN(date)) return Math.max(0, Math.ceil((date - Date.now()) / 1000));
  return undefined;
}


================================================
FILE: src\routing\retry.ts
================================================
/** Retry logic: cache-preserving wait + reroute after retryable failures (429/403). */

import type { ProxyConfig } from "../config/config.ts";
import type { ParsedBody } from "../server/body.ts";
import { logger } from "../utils/logger.ts";
import { cooldown, parseRetryAfter, type QuotaPool } from "./cooldown.ts";
import { buildCandidates, type RouteResult, recordSuccess, reroute } from "./router.ts";

/** Max reroute attempts before falling back to upstream. */
const MAX_REROUTE_ATTEMPTS = 4;
/** Max seconds to wait-and-retry on the same account (preserves prompt cache). */
const CACHE_PRESERVE_WAIT_MAX_S = 10;
/** Max ms to wait when all candidates are burst-cooling before giving up. */
const BURST_WAIT_MAX_MS = 30_000;

/** Status codes that trigger rerouting to a different account/pool. */
const REROUTABLE_STATUSES = new Set([429, 403]);

interface RerouteContext {
  providerName: string;
  ampModel: string | null;
  config: ProxyConfig;
  sub: string;
  body: ParsedBody;
  headers: Headers;
  rewrite: ((data: string) => string) | undefined;
  threadId?: string;
}

/** Wait briefly and retry on the same account to preserve prompt cache (429 only). */
export async function tryWithCachePreserve(
  route: RouteResult,
  sub: string,
  body: ParsedBody,
  headers: Headers,
  rewrite: ((data: string) => string) | undefined,
  initialResponse: Response,
): Promise<Response | null> {
  const retryAfter = parseRetryAfter(initialResponse.headers.get("retry-after"));
  if (retryAfter === undefined || retryAfter > CACHE_PRESERVE_WAIT_MAX_S) return null;

  logger.debug(`Waiting ${retryAfter}s to preserve prompt cache on account=${route.account}`);
  await Bun.sleep(retryAfter * 1000);
  const response = await route.handler!.forward(sub, body, headers, rewrite, route.account);

  if (response.status !== 429 && response.status !== 403 && response.status !== 401) {
    recordSuccess(route.pool!, route.account);
    return response;
  }
  if (response.status === 429) {
    const nextRetryAfter = parseRetryAfter(response.headers.get("retry-after"));
    cooldown.record429(route.pool!, route.account, nextRetryAfter);
  }
  if (response.status === 403) {
    cooldown.record403(route.pool!, route.account);
  }
  return null;
}

/** Reroute to different accounts/pools after a retryable failure (429/403). */
export async function tryReroute(
  ctx: RerouteContext,
  initialRoute: RouteResult,
  status: number,
): Promise<Response | null> {
  recordFailure(initialRoute.pool!, initialRoute.account, status);

  let currentPool = initialRoute.pool!;
  let currentAccount = initialRoute.account;

  for (let attempt = 0; attempt < MAX_REROUTE_ATTEMPTS; attempt++) {
    let next = reroute(ctx.providerName, ctx.ampModel, ctx.config, currentPool, currentAccount, ctx.threadId);

    // All candidates cooling down — wait for shortest burst then retry
    if (!next?.handler) {
      const candidates = buildCandidates(ctx.providerName, ctx.config);
      const waitMs = cooldown.shortestBurstWait(candidates);
      if (waitMs && waitMs <= BURST_WAIT_MAX_MS) {
        logger.info(`All accounts cooling, waiting ${Math.ceil(waitMs / 1000)}s for burst cooldown`);
        await Bun.sleep(waitMs + 100); // small buffer
        next = reroute(ctx.providerName, ctx.ampModel, ctx.config, currentPool, currentAccount, ctx.threadId);
      }
    }

    if (!next?.handler) break;

    logger.info(`REROUTE (${status}) -> ${next.decision} account=${next.account}`);
    const response = await next.handler.forward(ctx.sub, ctx.body, ctx.headers, ctx.rewrite, next.account);

    if (REROUTABLE_STATUSES.has(response.status) && next.pool) {
      recordFailure(next.pool, next.account, response.status);
      currentPool = next.pool;
      currentAccount = next.account;
      continue;
    }

    if (response.status !== 401) {
      if (next.pool) recordSuccess(next.pool, next.account);
      return response;
    }
    break;
  }

  return null;
}

/** Record the appropriate cooldown based on status code. */
function recordFailure(pool: QuotaPool, account: number, status: number): void {
  if (status === 403) {
    cooldown.record403(pool, account);
  } else {
    cooldown.record429(pool, account);
  }
}


================================================
FILE: src\routing\router.ts
================================================
/**
 * Route decision: local provider (free) or Amp upstream (paid).
 *
 * Multi-account aware:
 * - Thread affinity: same thread sticks to same account
 * - Cooldown: skip 429'd accounts, detect quota exhaustion
 * - Least-connections: prefer accounts with fewer active threads
 * - Google: single pool with internal strategy fallback (gemini/antigravity)
 */

import type { ProviderName } from "../auth/store.ts";
import * as store from "../auth/store.ts";
import type { ProxyConfig } from "../config/config.ts";
import { provider as anthropic } from "../providers/anthropic.ts";
import type { Provider } from "../providers/base.ts";
import { provider as codex } from "../providers/codex.ts";
import { provider as google } from "../providers/google.ts";
import { logger, type RouteDecision } from "../utils/logger.ts";
import { affinity } from "./affinity.ts";
import { cooldown, type QuotaPool } from "./cooldown.ts";

interface ProviderEntry {
  provider: Provider;
  pool: QuotaPool;
  credentialName: ProviderName;
}

/** Maps ampProvider name → list of provider entries (checked against config at lookup time). */
const PROVIDER_REGISTRY = new Map<string, { configKey: keyof ProxyConfig["providers"]; entries: ProviderEntry[] }>([
  [
    "anthropic",
    {
      configKey: "anthropic",
      entries: [{ provider: anthropic, pool: "anthropic", credentialName: "anthropic" }],
    },
  ],
  [
    "openai",
    {
      configKey: "codex",
      entries: [{ provider: codex, pool: "codex", credentialName: "codex" }],
    },
  ],
  [
    "google",
    {
      configKey: "google",
      entries: [{ provider: google, pool: "google", credentialName: "google" }],
    },
  ],
]);

/** Reverse map: QuotaPool → Provider (built once at module init). */
const POOL_TO_PROVIDER = new Map<QuotaPool, Provider>();
for (const [, { entries }] of PROVIDER_REGISTRY) {
  for (const entry of entries) {
    POOL_TO_PROVIDER.set(entry.pool, entry.provider);
  }
}

export interface RouteResult {
  decision: RouteDecision;
  provider: string;
  model: string;
  handler: Provider | null;
  account: number;
  pool: QuotaPool | null;
}

interface Candidate {
  provider: Provider;
  pool: QuotaPool;
  account: number;
}

export function routeRequest(
  ampProvider: string,
  model: string | null,
  config: ProxyConfig,
  threadId?: string,
): RouteResult {
  const modelStr = model ?? "unknown";

  // Early exit if provider is disabled in config
  const reg = PROVIDER_REGISTRY.get(ampProvider);
  if (!reg || !config.providers[reg.configKey]) {
    logger.route("AMP_UPSTREAM", ampProvider, modelStr);
    return result(null, ampProvider, modelStr, 0, null);
  }

  // Check thread affinity (keyed by threadId + ampProvider)
  if (threadId) {
    const pinned = affinity.get(threadId, ampProvider);
    if (pinned && !cooldown.isExhausted(pinned.pool, pinned.account)) {
      const handler = providerForPool(pinned.pool);
      if (handler?.isAvailable(pinned.account)) {
        if (!cooldown.isCoolingDown(pinned.pool, pinned.account)) {
          logger.route(handler.routeDecision, ampProvider, modelStr);
          return result(handler, ampProvider, modelStr, pinned.account, pinned.pool);
        }
        // Burst cooldown — still pinned but cooling, let it fall through to find alternative
      }
    }
    // Affinity broken (exhausted / unavailable) — clear and re-route
    if (pinned) affinity.clear(threadId, ampProvider);
  }

  // Build candidate list
  const candidates = buildCandidates(ampProvider, config);
  if (candidates.length === 0) {
    logger.route("AMP_UPSTREAM", ampProvider, modelStr);
    return result(null, ampProvider, modelStr, 0, null);
  }

  // Pick best candidate: not cooling down, least active threads
  const picked = pickCandidate(candidates);
  if (!picked) {
    logger.route("AMP_UPSTREAM", ampProvider, modelStr);
    return result(null, ampProvider, modelStr, 0, null);
  }

  // Pin thread affinity
  if (threadId) affinity.set(threadId, ampProvider, picked.pool, picked.account);

  logger.route(picked.provider.routeDecision, ampProvider, modelStr);
  return result(picked.provider, ampProvider, modelStr, picked.account, picked.pool);
}

/** Record a failure on the current account and pick the next candidate.
 *  Caller is responsible for recording the failure (429/403) on cooldown before calling. */
export function reroute(
  ampProvider: string,
  model: string | null,
  config: ProxyConfig,
  failedPool: QuotaPool,
  failedAccount: number,
  threadId?: string,
): RouteResult | null {
  if (threadId && cooldown.isExhausted(failedPool, failedAccount)) {
    affinity.clear(threadId, ampProvider);
  }

  const modelStr = model ?? "unknown";
  const candidates = buildCandidates(ampProvider, config);
  const picked = pickCandidate(candidates);

  if (!picked) return null;

  if (threadId) affinity.set(threadId, ampProvider, picked.pool, picked.account);
  logger.route(picked.provider.routeDecision, ampProvider, modelStr);
  return res

================================================
FILE: src\server\body.ts
================================================
/** Request body — lazy parsing with regex fast path.
 *  Fast path: regex extracts model + stream flag without JSON.parse.
 *  Slow path: full JSON.parse only when .parsed or .forwardBody is accessed
 *  (e.g. Google CCA wrapping, model rewrite). */

import { resolveModel, rewriteBodyModel } from "../utils/models.ts";
import * as path from "../utils/path.ts";

export interface ParsedBody {
  /** Original raw body string (for upstream fallback). */
  readonly raw: string;
  /** Amp model name from body.model (before mapping). */
  readonly ampModel: string | null;
  /** Whether body.stream === true. */
  readonly stream: boolean;
  /** Body string to send to provider (re-serialized only if model was remapped). */
  readonly forwardBody: string;
  /** Parsed JSON object — lazy, only materialized when accessed (Google CCA wrapping). */
  readonly parsed: Record<string, unknown> | null;
}

/** Fast-path regex to extract "model" and "stream" without JSON.parse. */
const MODEL_RE = /"model"\s*:\s*"([^"]+)"/;
const STREAM_RE = /"stream"\s*:\s*true\b/;

export function parseBody(raw: string, sub: string): ParsedBody {
  const fallbackModel = path.modelFromUrl(sub);
  if (!raw) return { raw, parsed: null, ampModel: fallbackModel, stream: false, forwardBody: raw };

  const ampModel = raw.match(MODEL_RE)?.[1] ?? fallbackModel;
  const stream = STREAM_RE.test(raw);
  const providerModel = ampModel ? resolveModel(ampModel) : null;
  const needsRewrite = !!(ampModel && providerModel && providerModel !== ampModel);

  let _parsed: Record<string, unknown> | null | undefined;
  function ensureParsed(): Record<string, unknown> | null {
    if (_parsed === undefined) {
      try {
        _parsed = JSON.parse(raw) as Record<string, unknown>;
      } catch {
        _parsed = null;
      }
    }
    return _parsed;
  }

  let _forwardBody: string | undefined;
  function ensureForwardBody(): string {
    if (_forwardBody === undefined) {
      if (needsRewrite) {
        const p = ensureParsed();
        _forwardBody = p ? rewriteBodyModel(p, providerModel!) : raw;
      } else {
        _forwardBody = raw;
      }
    }
    return _forwardBody;
  }

  return {
    raw,
    ampModel,
    stream,
    get parsed() {
      return ensureParsed();
    },
    get forwardBody() {
      return ensureForwardBody();
    },
  };
}


================================================
FILE: src\server\server.ts
================================================
/** HTTP server — routes provider requests through local OAuth or Amp upstream. */

import { maybeShowAd } from "../cli/ads.ts";
import type { ProxyConfig } from "../config/config.ts";
import * as rewriter from "../proxy/rewriter.ts";
import * as upstream from "../proxy/upstream.ts";
import { affinity } from "../routing/affinity.ts";
import { tryReroute, tryWithCachePreserve } from "../routing/retry.ts";
import { recordSuccess, routeRequest } from "../routing/router.ts";
import { handleInternal, isLocalMethod } from "../tools/internal.ts";
import { logger } from "../utils/logger.ts";
import * as path from "../utils/path.ts";
import { apiError } from "../utils/responses.ts";
import { stats } from "../utils/stats.ts";
import { type ParsedBody, parseBody } from "./body.ts";

export function startServer(config: ProxyConfig): ReturnType<typeof Bun.serve> {
  const server = Bun.serve({
    port: config.port,
    hostname: config.hostname,
    idleTimeout: 255, // seconds — LLM streaming responses can take minutes

    async fetch(req) {
      const startTime = Date.now();
      const url = new URL(req.url);
      let status = 500;
      try {
        const response = await handle(req, url, config);
        status = response.status;
        return response;
      } catch (err) {
        logger.error("Unhandled server error", { error: String(err) });
        return apiError(status, "Internal proxy error");
      } finally {
        logger.info(`${req.method} ${url.pathname}${url.search} ${status}`, { duration: Date.now() - startTime });
      }
    },
  });

  affinity.startCleanup();
  logger.info(`ampcode-connector listening on http://${config.hostname}:${config.port}`);

  const shutdown = () => {
    logger.info("Shutting down...");
    server.stop();
    process.exit(0);
  };

  process.on("SIGTERM", shutdown);
  process.on("SIGINT", shutdown);

  return server;
}

async function handle(req: Request, url: URL, config: ProxyConfig): Promise<Response> {
  const { pathname, search } = url;

  if ((pathname === "/" || pathname === "/status") && req.method === "GET") {
    return healthCheck(config);
  }

  if (path.browser(pathname)) {
    const target = new URL(pathname + search, config.ampUpstreamUrl);
    return Response.redirect(target.toString(), 302);
  }

  if (path.passthrough(pathname)) {
    if (pathname.startsWith("/api/internal") && isLocalMethod(search)) {
      return handleInternal(req, search, config);
    }
    return upstream.forward(req, config.ampUpstreamUrl, config.ampApiKey);
  }

  const providerName = path.provider(pathname);
  if (providerName) return handleProvider(req, providerName, pathname, config);

  return upstream.forward(req, config.ampUpstreamUrl, config.ampApiKey);
}

async function handleProvider(
  req: Request,
  providerName: string,
  pathname: string,
  config: ProxyConfig,
): Promise<Response> {
  const startTime = Date.now();
  const sub = path.subpath(pathname);
  const threadId = req.headers.get("x-amp-thread-id") ?? req.headers.get("x-session-id") ?? undefined;

  const rawBody = req.method === "POST" ? await req.text() : "";
  const body = parseBody(rawBody, sub);
  const ampModel = body.ampModel;
  const route = routeRequest(providerName, ampModel, config, threadId);

  logger.info(
    `ROUTE ${route.decision} provider=${providerName} model=${ampModel ?? "?"} account=${route.account} sub=${sub}`,
  );

  let response: Response;

  if (route.handler) {
    const rewrite = ampModel ? rewriter.rewrite(ampModel) : undefined;
    const handlerResponse = await route.handler.forward(sub, body, req.headers, rewrite, route.account);

    if (
      (handlerResponse.status === 429 || handlerResponse.status === 403 || handlerResponse.status === 404) &&
      route.pool
    ) {
      const ctx = { providerName, ampModel, config, sub, body, headers: req.headers, rewrite, threadId };
      // 429: try short wait to preserve prompt cache first
      const cached =
        handlerResponse.status === 429
          ? await tryWithCachePreserve(route, sub, body, req.headers, rewrite, handlerResponse)
          : null;
      if (cached) {
        response = cached;
      } else {
        const rerouted = await tryReroute(ctx, route, handlerResponse.status);
        response = rerouted ?? (await fallbackUpstream(req, body, config));
      }
    } else if (handlerResponse.status === 401) {
      logger.debug("Local provider denied, falling back to upstream");
      response = await fallbackUpstream(req, body, config);
    } else {
      if (route.pool) recordSuccess(route.pool, route.account);
      response = handlerResponse;
    }
  } else {
    response = await fallbackUpstream(req, body, config);
  }

  stats.record({
    timestamp: new Date().toISOString(),
    route: route.decision,
    provider: providerName,
    model: ampModel ?? "unknown",
    statusCode: response.status,
    durationMs: Date.now() - startTime,
  });

  maybeShowAd();

  return response;
}

/** Fall back to Am

================================================
FILE: src\tools\internal.ts
================================================
/** Dispatcher for /api/internal?{method} — routes to local handlers or upstream. */

import type { ProxyConfig } from "../config/config.ts";
import * as upstream from "../proxy/upstream.ts";
import { logger } from "../utils/logger.ts";
import { handleWebRead } from "./web-read.ts";
import { handleSearch } from "./web-search.ts";

interface HandlerContext {
  params: Record<string, unknown>;
  config: ProxyConfig;
  forward: () => Promise<Response>;
}

type Handler = (ctx: HandlerContext) => Promise<Response>;

const handlers: Record<string, Handler> = {
  extractWebPageContent: async ({ params }) => {
    const url = str(params, "url");
    if (!url) return error("invalid-params", "missing 'url'");
    return json(
      await handleWebRead({ url, objective: str(params, "objective"), forceRefetch: bool(params, "forceRefetch") }),
    );
  },

  webSearch2: async ({ params, config, forward }) => {
    if (!config.exaApiKey) {
      logger.warn("webSearch2: no exaApiKey configured, forwarding upstream");
      return forward();
    }
    const objective = str(params, "objective");
    if (!objective) return error("invalid-params", "missing 'objective'");
    return handleSearch(
      { objective, searchQueries: strArray(params, "searchQueries"), maxResults: num(params, "maxResults") },
      config.exaApiKey,
    ).then(json, (err) => {
      logger.warn("webSearch2 local failed, falling back to upstream", { error: String(err) });
      return forward();
    });
  },
};

export function isLocalMethod(search: string): boolean {
  return search.replace("?", "") in handlers;
}

export async function handleInternal(req: Request, search: string, config: ProxyConfig): Promise<Response> {
  const method = search.replace("?", "");
  const body = req.method === "POST" ? await req.text() : "";

  let params: Record<string, unknown>;
  try {
    params = JSON.parse(body).params ?? {};
  } catch {
    return error("invalid-body", "Invalid JSON body");
  }

  logger.info(`[INTERNAL] ${method} params=${JSON.stringify(params).slice(0, 200)}`);

  const forward = () => {
    const rebuilt = new Request(req.url, { method: req.method, headers: req.headers, body: body || undefined });
    return upstream.forward(rebuilt, config.ampUpstreamUrl, config.ampApiKey);
  };

  const handler = handlers[method];
  return handler ? handler({ params, config, forward }) : forward();
}

function str(p: Record<string, unknown>, k: string): string | undefined {
  const v = p[k];
  return typeof v === "string" ? v : undefined;
}

function num(p: Record<string, unknown>, k: string): number | undefined {
  const v = p[k];
  return typeof v === "number" ? v : undefined;
}

function bool(p: Record<string, unknown>, k: string): boolean | undefined {
  const v = p[k];
  return typeof v === "boolean" ? v : undefined;
}

function strArray(p: Record<string, unknown>, k: string): string[] | undefined {
  const v = p[k];
  return Array.isArray(v) && v.every((i: unknown) => typeof i === "string") ? (v as string[]) : undefined;
}

function json(data: unknown): Response {
  return Response.json(data);
}

function error(code: string, message: string): Response {
  return Response.json({ ok: false, error: { code, message } });
}


================================================
FILE: src\tools\web-read.ts
================================================
/** Local handler for extractWebPageContent — fetches a URL, converts to Markdown, ranks by objective. */

import TurndownService from "turndown";
import { gfm } from "turndown-plugin-gfm";
import { logger } from "../utils/logger.ts";

interface WebReadParams {
  url: string;
  objective?: string;
  forceRefetch?: boolean;
}

type WebReadResult =
  | { ok: true; result: { excerpts: string[] } | { fullContent: string } }
  | { ok: false; error: { code: string; message: string } };

interface Section {
  heading: string;
  text: string;
  index: number;
}

interface ScoredSection {
  text: string;
  score: number;
  index: number;
}

type FetchOk = { ok: true; body: string; contentType: string };
type FetchErr = WebReadResult & { ok: false };

const FETCH = {
  TIMEOUT_MS: 30_000,
  USER_AGENT: "Mozilla/5.0 (compatible; AmpBot/1.0)",
} as const;

const CACHE = {
  MAX_ENTRIES: 50,
  TTL_MS: 5 * 60 * 1000,
} as const;

const RANKING = {
  MAX_SECTIONS: 10,
  MAX_SECTION_WORDS: 500,
  MIN_KEYWORD_LEN: 3,
  HEADING_BOOST: 2,
  BIGRAM_BOOST: 1.5,
  POSITION_DECAY: 0.1,
  BM25_K1: 1.5,
  BM25_B: 0.75,
} as const;

const CLIPPING = {
  MAX_BYTES: 262_144, // 256 KB — CLI truncation limit
  MIN_TAIL_BYTES: 100,
  EXCERPT_SEP_BYTES: 2, // "\n\n" separator
} as const;

const turndown = new TurndownService({ headingStyle: "atx", codeBlockStyle: "fenced" });
turndown.use(gfm);
turndown.remove(["script", "style", "img"]);

// biome-ignore format: compact
const STOP_WORDS = new Set(
  ("the and for are but not you all can her was one our out " +
  "has have had been from this that with they which their will " +
  "each make like just over such than them very some what about " +
  "into more other then these when where how does also after " +
  "should would could being there before between those through while using").split(" "),
);

const encoder = new TextEncoder();
const decoder = new TextDecoder("utf-8", { fatal: false });

const cache = new Map<string, { markdown: string; createdAt: number }>();

function getCached(url: string): string | undefined {
  const entry = cache.get(url);
  if (!entry) return undefined;

  if (Date.now() - entry.createdAt > CACHE.TTL_MS) {
    cache.delete(url);
    return undefined;
  }

  // Re-insert to promote as most-recent (LRU)
  cache.delete(url);
  cache.set(url, entry);
  return entry.markdown;
}

function setCache(url: string, markdown: string): void {
  if (cache.size >= CACHE.MAX_ENTRIES) {
    const oldest = cache.keys().next().value!;
    cache.delete(oldest);
  }
  cache.set(url, { markdown, createdAt: Date.now() });
}

export async function handleWebRead({ url, objective, forceRefetch }: WebReadParams): Promise<WebReadResult> {
  let markdown = forceRefetch ? undefined : getCached(url);

  if (!markdown) {
    const page = await fetchPage(url);
    if (!page.ok) return page;
    markdown = convertToMarkdown(page.body, page.contentType);
    setCache(url, markdown);
  }

  if (objective) {
    return { ok: true, result: { excerpts: rankExcerpts(markdown, objective) } };
  }
  return { ok: true, result: { fullContent: clipText(markdown) } };
}

async function fetchPage(url: string): Promise<FetchOk | FetchErr> {
  let response: Response;
  try {
    response = await fetch(url, {
      signal: AbortSignal.timeout(FETCH.TIMEOUT_MS),
      redirect: "follow",
      headers: { "User-Agent": FETCH.USER_AGENT },
    });
  } catch (error) {
    logger.warn("web-read fetch failed", { url, error: String(error) });
    return fetchError(`Failed to fetch ${url}: ${String(error)}`);
  }

  if (!response.ok) {
    return fetchError(`HTTP ${response.status} from ${url}`);
  }

  const body = await response.text();
  const contentType = response.headers.get("content-type") ?? "";
  return { ok: true, body, contentType };
}

function fetchError(message: string): FetchErr {
  return { ok: false, error: { code: "fetch-error", message } };
}

function convertToMarkdown(raw: string, contentType: string): string {
  if (contentType.includes("text/html") || contentType.includes("application/xhtml")) {
    return turndown.turndown(raw);
  }

  if (contentType.includes("application/json")) {
    try {
      return `\`\`\`json\n${JSON.stringify(JSON.parse(raw), null, 2)}\n\`\`\``;
    } catch {
      return raw;
    }
  }

  return raw;
}

function rankExcerpts(markdown: string, objective: string): string[] {
  const sections = splitSections(markdown);
  if (!sections.length) return [clipText(markdown)];
  const { unigrams, bigrams } = parseTerms(objective);
  if (!unigrams.length) return [clipText(markdown)];
  const unigramPatterns = unigrams.map((w) => new RegExp(`\\b${RegExp.escape(w)}\\b`, "g"));
  const idfWeights = computeIdf(sections, unigramPatterns);
  const avgDocLen = sections.reduce((sum, s) => sum + (s.text.split(/\s+/).length || 1), 0) / sections.length;
  const totalSections = sections.length;
  const scored = sections.map((section) =>
    scoreSection(section, unigramPatterns, bigrams,

================================================
FILE: src\tools\web-search.ts
================================================
/** Local handler for webSearch2 — searches via Exa API. */

import Exa from "exa-js";
import { logger } from "../utils/logger.ts";

let _exa: InstanceType<typeof Exa> | null = null;
let _exaKey: string | null = null;

function getExa(apiKey: string): InstanceType<typeof Exa> {
  if (!_exa || _exaKey !== apiKey) {
    _exa = new Exa(apiKey);
    _exaKey = apiKey;
  }
  return _exa;
}

interface SearchParams {
  objective: string;
  searchQueries?: string[];
  maxResults?: number;
}

interface SearchResultItem {
  title: string;
  url: string;
  excerpts: string[];
}

interface SearchResponse {
  ok: true;
  result: { results: SearchResultItem[]; showParallelAttribution: boolean };
}

export async function handleSearch(params: SearchParams, exaApiKey: string): Promise<SearchResponse> {
  const { objective, searchQueries, maxResults = 5 } = params;
  const query = searchQueries?.length ? searchQueries.join(" ") : objective;

  const exa = getExa(exaApiKey);
  const response = await exa.search(query, {
    numResults: maxResults,
    type: "auto",
    contents: {
      highlights: { query: objective },
    },
  });

  const results: SearchResultItem[] = response.results.map((r) => ({
    title: r.title ?? "",
    url: r.url,
    excerpts: r.highlights?.length ? r.highlights : [],
  }));

  logger.info(`[SEARCH] Exa returned ${results.length} results for "${query.slice(0, 80)}"`);
  return { ok: true, result: { results, showParallelAttribution: false } };
}


================================================
FILE: src\types\turndown-plugin-gfm.d.ts
================================================
declare module "turndown-plugin-gfm" {
  import type TurndownService from "turndown";
  export function gfm(service: TurndownService): void;
  export function tables(service: TurndownService): void;
  export function strikethrough(service: TurndownService): void;
  export function taskListItems(service: TurndownService): void;
  export function highlightedCodeBlock(service: TurndownService): void;
}


================================================
FILE: src\utils\browser.ts
================================================
/** Cross-platform: macOS (open), Linux (xdg-open), Windows (start). */
export async function open(url: string): Promise<boolean> {
  const commands: Record<string, string[]> = {
    darwin: ["open", url],
    linux: ["xdg-open", url],
    win32: ["cmd", "/c", "start", url],
  };

  const cmd = commands[process.platform];
  if (!cmd) return false;

  try {
    const proc = Bun.spawn(cmd);
    await proc.exited;
    return true;
  } catch {
    return false;
  }
}


================================================
FILE: src\utils\code-assist.ts
================================================
/** Cloud Code Assist request/URL helpers shared by Gemini CLI and Antigravity. */

interface WrapOptions {
  projectId: string;
  model: string;
  body: Record<string, unknown>;
  userAgent: "antigravity" | "pi-coding-agent";
  requestIdPrefix: "agent" | "pi";
  requestType?: "agent" | "image_gen";
}

/** Wrap a raw request body in the Cloud Code Assist envelope. */
function wrapRequest(opts: WrapOptions): string {
  const isImageGen = opts.requestType === "image_gen";
  const requestId = isImageGen
    ? `image_gen/${Date.now()}/${crypto.randomUUID()}/12`
    : `${opts.requestIdPrefix}-${Date.now()}-${crypto.randomUUID().slice(0, 8)}`;

  return JSON.stringify({
    project: opts.projectId,
    model: opts.model,
    request: opts.body,
    ...(opts.requestType && { requestType: opts.requestType }),
    userAgent: opts.userAgent,
    requestId,
  });
}

/** Build the Cloud Code Assist URL for a given action. Preserves the original action
 *  (generateContent vs streamGenerateContent). Only adds ?alt=sse for streaming actions. */
export function buildUrl(endpoint: string, action: string): string {
  const streaming = action.toLowerCase().includes("stream");
  return `${endpoint}/v1internal:${action}${streaming ? "?alt=sse" : ""}`;
}

/** Unwrap Cloud Code Assist SSE envelope: {"response":{...},"traceId":"..."} → inner response.
 *  Returns empty string for [DONE] sentinel (Google SDK doesn't expect it). */
export function unwrap(data: string): string {
  if (data === "[DONE]") return "";
  try {
    const parsed = JSON.parse(data) as { response?: unknown };
    if (parsed.response !== undefined) return JSON.stringify(parsed.response);
    return data;
  } catch {
    return data;
  }
}

/** Chain CCA unwrap with an optional rewrite function. */
export function withUnwrap(rewrite?: (d: string) => string): (d: string) => string {
  return rewrite ? (d: string) => rewrite(unwrap(d)) : unwrap;
}

/** Ensure every function_response part has a non-empty name.
 *  Gemini API rejects requests where function_response.name is empty.
 *  Uses two strategies:
 *  1. Positional: a model turn with N functionCall parts is followed by a user turn
 *     with N functionResponse parts in the same order — match by index.
 *  2. ID-based fallback: match function_response.id → function_call.id.
 *  Handles both camelCase (functionCall) and snake_case (function_call) keys. */
function fixFunctionResponseNames(body: Record<string, unknown>): void {
  const contents = body.contents;
  if (!Array.isArray(contents)) return;

  type Part = Record<string, unknown>;
  type Content = { role?: string; parts?: Part[] };
  const getFc = (p: Part) => (p.functionCall ?? p.function_call) as Record<string, unknown> | undefined;
  const getFr = (p: Part) => (p.functionResponse ?? p.function_response) as Record<string, unknown> | undefined;

  // Pass 1: positional matching — pair consecutive model/user turns
  for (let i = 0; i < contents.length - 1; i++) {
    const modelTurn = contents[i] as Content;
    const userTurn = contents[i + 1] as Content;
    if (modelTurn.role !== "model" || userTurn.role !== "user") continue;
    if (!Array.isArray(modelTurn.parts) || !Array.isArray(userTurn.parts)) continue;

    const fcParts = modelTurn.parts.filter((p) => getFc(p as Part));
    const frParts = userTurn.parts.filter((p) => getFr(p as Part));
    if (fcParts.length === 0 || fcParts.length !== frParts.length) continue;

    for (let j = 0; j < frParts.length; j++) {
      const fr = getFr(frParts[j] as Part)!;
      if (typeof fr.name === "string" && fr.name) continue;
      const fc = getFc(fcParts[j] as Part)!;
      if (typeof fc.name === "string") {
        fr.name = fc.name;
      }
    }
  }

  // Pass 2: ID-based fallback for any remaining empty names
  const nameById = new Map<string, string>();
  for (const content of contents) {
    const parts = (content as Content)?.parts;
    if (!Array.isArray(parts)) continue;
    for (const part of parts) {
      const fc = getFc(part as Part);
      if (fc && typeof fc.name === "string" && typeof fc.id === "string") {
        nameById.set(fc.id, fc.name);
      }
    }
  }

  if (nameById.size === 0) return;

  for (const content of contents) {
    const parts = (content as Content)?.parts;
    if (!Array.isArray(parts)) continue;
    for (const part of parts) {
      const fr = getFr(part as Part);
      if (!fr || (typeof fr.name === "string" && fr.name)) continue;
      const resolved = typeof fr.id === "string" ? nameById.get(fr.id) : undefined;
      if (resolved) {
        fr.name = resolved;
      }
    }
  }
}

/** Wrap body in CCA envelope if not already wrapped. */
export function maybeWrap(
  parsed: Record<string, unknown> | null,
  raw: string,
  projectId: string,
  model: string,
  opts: {
    userAgent: "antigravity" | "pi-coding-agent";
    requestIdPrefix: "agent" | "pi";
    requestType?: "agent" | "image_gen";
  },
): string {
  if (!parsed) return raw;
  if (parsed.project) 

================================================
FILE: src\utils\encoding.ts
================================================
/** Encode bytes to base64url (no padding). */
export function toBase64url(buffer: Uint8Array): string {
  return Buffer.from(buffer).toString("base64url");
}

/** Decode base64url string to bytes. Handles both base64url and standard base64. */
export function fromBase64url(input: string): Uint8Array {
  return new Uint8Array(Buffer.from(input, "base64url"));
}


================================================
FILE: src\utils\logger.ts
================================================
/** Structured logging with route decision tracking. */

export type RouteDecision = "LOCAL_CLAUDE" | "LOCAL_CODEX" | "LOCAL_GOOGLE" | "AMP_UPSTREAM";

export type LogLevel = "debug" | "info" | "warn" | "error";

interface LogEntry {
  timestamp: string;
  level: LogLevel;
  message: string;
  route?: RouteDecision;
  provider?: string;
  model?: string;
  duration?: number;
  error?: string;
  [key: string]: unknown;
}

const LOG_LEVELS: Record<LogLevel, number> = {
  debug: 0,
  info: 1,
  warn: 2,
  error: 3,
};

const isTTY = !!process.stdout.isTTY;

const RESET = "\x1b[0m";
const DIM = "\x1b[2m";
const GREEN = "\x1b[32m";
const YELLOW = "\x1b[33m";
const RED = "\x1b[31m";

const LEVEL_COLORS: Record<LogLevel, string> = {
  debug: DIM,
  info: "",
  warn: YELLOW,
  error: RED,
};

const ROUTE_COLORS: Record<RouteDecision, string> = {
  LOCAL_CLAUDE: GREEN,
  LOCAL_CODEX: GREEN,
  LOCAL_GOOGLE: GREEN,
  AMP_UPSTREAM: YELLOW,
};

function colorize(text: string, color: string): string {
  if (!isTTY || !color) return text;
  return `${color}${text}${RESET}`;
}

let currentLevel: LogLevel = "info";

export function setLogLevel(level: LogLevel): void {
  currentLevel = level;
}

function shouldLog(level: LogLevel): boolean {
  return LOG_LEVELS[level] >= LOG_LEVELS[currentLevel];
}

function format(entry: LogEntry): string {
  const { timestamp, level, message, route, provider, model, duration, error } = entry;

  const tag = colorize(`[${level.toUpperCase().padEnd(5)}]`, LEVEL_COLORS[level]);
  let line = `${timestamp} ${tag} ${message}`;
  if (route) line += ` route=${colorize(route, ROUTE_COLORS[route])}`;
  if (provider) line += ` provider=${provider}`;
  if (model) line += ` model=${model}`;
  if (duration !== undefined) line += ` duration=${duration}ms`;
  if (error) line += ` error=${error}`;

  return line;
}

type Meta = Partial<Omit<LogEntry, "timestamp" | "level" | "message">>;

function log(level: LogLevel, message: string, meta?: Meta): void {
  if (!shouldLog(level)) return;

  const entry: LogEntry = {
    timestamp: new Date().toISOString(),
    level,
    message,
    ...meta,
  };

  const line = format(entry);

  if (level === "error") {
    console.error(line);
  } else if (level === "warn") {
    console.warn(line);
  } else {
    console.log(line);
  }
}

export const logger = {
  debug: (message: string, meta?: Meta) => log("debug", message, meta),
  info: (message: string, meta?: Meta) => log("info", message, meta),
  warn: (message: string, meta?: Meta) => log("warn", message, meta),
  error: (message: string, meta?: Meta) => log("error", message, meta),

  route(decision: RouteDecision, provider: string, model: string): void {
    log("info", "Route decision", { route: decision, provider, model });
  },
};


================================================
FILE: src\utils\models.ts
================================================
/** Centralized model name mapping: Amp CLI model → provider API model.
 *  Amp's proxy may use aliased model names that differ from the provider's API.
 *  This module resolves the correct model name and provides the serialized body. */

/** Suffix patterns stripped when forwarding to the real provider API. */
const STRIP_SUFFIXES = ["-api-preview"] as const;

/** Resolve the model name the provider API expects.
 *  Returns the original if no mapping applies. */
export function resolveModel(ampModel: string): string {
  for (const suffix of STRIP_SUFFIXES) {
    if (ampModel.endsWith(suffix)) return ampModel.slice(0, -suffix.length);
  }
  return ampModel;
}

/** Return body string with provider model name substituted.
 *  Shallow-copies parsed to avoid mutating the shared ParsedBody.parsed reference. */
export function rewriteBodyModel(parsed: Record<string, unknown>, providerModel: string): string {
  return JSON.stringify({ ...parsed, model: providerModel });
}


================================================
FILE: src\utils\path.ts
================================================
/** URL path parsing for Amp CLI provider routes. */

import { browserPrefixes, passthroughExact, passthroughPrefixes } from "../constants.ts";

const PROVIDER_RE = /^\/api\/provider\/([^/]+)/;
const SUBPATH_RE = /^\/api\/provider\/[^/]+(\/.*)/;
const MODEL_RE = /models\/([^/:]+)/;
const GOOGLE_MODEL_RE = /models\/([^/:]+):(\w+)/;

export function passthrough(pathname: string): boolean {
  if ((passthroughExact as readonly string[]).includes(pathname)) return true;
  return passthroughPrefixes.some((prefix) => pathname.startsWith(prefix));
}

export function browser(pathname: string): boolean {
  return browserPrefixes.some((prefix) => pathname === prefix || pathname.startsWith(`${prefix}/`));
}

export function provider(pathname: string): string | null {
  const match = pathname.match(PROVIDER_RE);
  return match?.[1] ?? null;
}

export function subpath(pathname: string): string {
  const match = pathname.match(SUBPATH_RE);
  return match?.[1] ?? pathname;
}

export function modelFromUrl(url: string): string | null {
  const match = url.match(MODEL_RE);
  return match?.[1] ?? null;
}

export function googleModel(url: string): { model: string; action: string } | null {
  const match = url.match(GOOGLE_MODEL_RE);
  if (!match) return null;
  return { model: match[1]!, action: match[2]! };
}


================================================
FILE: src\utils\responses.ts
================================================
export function apiError(status: number, message: string, type = "api_error"): Response {
  return Response.json({ error: { message, type, code: String(status) } }, { status });
}


================================================
FILE: src\utils\stats.ts
================================================
/** Request statistics tracking with ring buffer. */

import type { RouteDecision } from "../utils/logger.ts";

export interface RequestEntry {
  timestamp: string;
  route: RouteDecision;
  provider: string;
  model: string;
  statusCode: number;
  durationMs: number;
}

export interface StatsSnapshot {
  totalRequests: number;
  requestsByRoute: Partial<Record<RouteDecision, number>>;
  count429: number;
  averageDurationMs: number;
  uptimeMs: number;
}

export class StatsRecorder {
  private readonly maxEntries: number;
  private buffer: RequestEntry[] = [];
  private writeIndex = 0;
  private totalCount = 0;
  private readonly startedAt = Date.now();

  constructor(maxEntries = 1000) {
    this.maxEntries = maxEntries;
  }

  record(entry: RequestEntry): void {
    if (this.buffer.length < this.maxEntries) {
      this.buffer.push(entry);
    } else {
      this.buffer[this.writeIndex] = entry;
    }
    this.writeIndex = (this.writeIndex + 1) % this.maxEntries;
    this.totalCount++;
  }

  snapshot(): StatsSnapshot {
    const requestsByRoute: Partial<Record<RouteDecision, number>> = {};
    let count429 = 0;
    let totalDuration = 0;

    for (const entry of this.buffer) {
      requestsByRoute[entry.route] = (requestsByRoute[entry.route] ?? 0) + 1;
      if (entry.statusCode === 429) count429++;
      totalDuration += entry.durationMs;
    }

    return {
      totalRequests: this.totalCount,
      requestsByRoute,
      count429,
      averageDurationMs: this.buffer.length > 0 ? totalDuration / this.buffer.length : 0,
      uptimeMs: Date.now() - this.startedAt,
    };
  }

  recentRequests(n: number): RequestEntry[] {
    const count = Math.min(n, this.buffer.length);
    if (count === 0) return [];

    const result: RequestEntry[] = [];
    let idx = (this.writeIndex - count + this.buffer.length) % this.buffer.length;
    for (let i = 0; i < count; i++) {
      result.push(this.buffer[idx]!);
      idx = (idx + 1) % this.buffer.length;
    }
    return result;
  }

  reset(): void {
    this.buffer = [];
    this.writeIndex = 0;
    this.totalCount = 0;
  }
}

/** Singleton instance for production use. */
export const stats = new StatsRecorder();


================================================
FILE: src\utils\streaming.ts
================================================
/** SSE (Server-Sent Events) stream parsing, encoding, and transformation. */

export interface Chunk {
  event?: string;
  data: string;
  id?: string;
  retry?: number;
}

export function parse(raw: string): Chunk[] {
  const chunks: Chunk[] = [];

  for (const block of raw.split("\n\n")) {
    if (!block.trim()) continue;

    const chunk: Partial<Chunk> = {};
    for (const line of block.split("\n")) {
      if (line.startsWith("event:")) {
        chunk.event = line.slice(6).trim();
      } else if (line.startsWith("data:")) {
        const value = line.slice(5).trimStart();
        chunk.data = chunk.data ? `${chunk.data}\n${value}` : value;
      } else if (line.startsWith("id:")) {
        chunk.id = line.slice(3).trim();
      } else if (line.startsWith("retry:")) {
        const val = parseInt(line.slice(6).trim(), 10);
        if (!Number.isNaN(val)) chunk.retry = val;
      }
    }

    if (chunk.data !== undefined) chunks.push(chunk as Chunk);
  }

  return chunks;
}

export function encode(chunk: Chunk): string {
  let result = "";
  if (chunk.event) result += `event: ${chunk.event}\n`;
  if (chunk.id) result += `id: ${chunk.id}\n`;
  if (chunk.retry !== undefined) result += `retry: ${chunk.retry}\n`;

  for (const line of chunk.data.split("\n")) {
    result += `data: ${line}\n`;
  }

  result += "\n";
  return result;
}

const decoder = new TextDecoder();
const encoder = new TextEncoder();

function transform(source: ReadableStream<Uint8Array>, fn: (data: string) => string): ReadableStream<Uint8Array> {
  let buffer = "";

  const stream = new TransformStream<Uint8Array, Uint8Array>({
    transform(raw, controller) {
      buffer += decoder.decode(raw, { stream: true }).replaceAll("\r\n", "\n");

      const boundary = buffer.lastIndexOf("\n\n");
      if (boundary === -1) return;

      const complete = buffer.slice(0, boundary + 2);
      buffer = buffer.slice(boundary + 2);

      for (const chunk of parse(complete)) {
        chunk.data = fn(chunk.data);
        if (chunk.data) controller.enqueue(encoder.encode(encode(chunk)));
      }
    },

    flush(controller) {
      if (buffer.trim()) {
        for (const chunk of parse(buffer)) {
          chunk.data = fn(chunk.data);
          if (chunk.data) controller.enqueue(encoder.encode(encode(chunk)));
        }
      }
      buffer = "";
    },
  });

  return source.pipeThrough(stream);
}

const SSE_HEADERS: Readonly<Record<string, string>> = {
  "Content-Type": "text/event-stream",
  "Cache-Control": "no-cache",
  Connection: "keep-alive",
};

const forwardedHeaders = [
  "x-request-id",
  "request-id",
  "anthropic-ratelimit-requests-limit",
  "anthropic-ratelimit-requests-remaining",
  "anthropic-ratelimit-tokens-limit",
  "anthropic-ratelimit-tokens-remaining",
  "x-ratelimit-limit-requests",
  "x-ratelimit-remaining-requests",
  "x-ratelimit-limit-tokens",
  "x-ratelimit-remaining-tokens",
] as const;

export function proxy(upstream: Response, rewrite?: (data: string) => string): Response {
  if (!upstream.body) {
    return new Response("No response body", { status: 502 });
  }

  const body = rewrite ? transform(upstream.body, rewrite) : upstream.body;

  const h: Record<string, string> = { ...SSE_HEADERS };
  for (const name of forwardedHeaders) {
    const value = upstream.headers.get(name);
    if (value) h[name] = value;
  }

  return new Response(body, { status: upstream.status, headers: h });
}


================================================
FILE: src\utils\update-check.ts
================================================
/** Check npm registry for newer versions on startup. */

import { line, s } from "../cli/ansi.ts";

const PACKAGE_NAME = "ampcode-connector";
const REGISTRY_URL = `https://registry.npmjs.org/${PACKAGE_NAME}/latest`;
const TIMEOUT_MS = 3_000;

function currentVersion(): string {
  // Read from package.json at import time
  const pkg = require("../../package.json");
  return pkg.version;
}

async function fetchLatestVersion(): Promise<string | null> {
  try {
    const res = await fetch(REGISTRY_URL, {
      signal: AbortSignal.timeout(TIMEOUT_MS),
    });
    if (!res.ok) return null;
    const data = (await res.json()) as { version: string };
    return data.version;
  } catch {
    return null;
  }
}

function isNewer(latest: string, current: string): boolean {
  const parse = (v: string) => v.split(".").map(Number);
  const [la = 0, lb = 0, lc = 0] = parse(latest);
  const [ca = 0, cb = 0, cc = 0] = parse(current);
  return la > ca || (la === ca && lb > cb) || (la === ca && lb === cb && lc > cc);
}

/** Non-blocking update check — logs a notice if a newer version exists. */
export async function checkForUpdates(): Promise<void> {
  const current = currentVersion();
  const latest = await fetchLatestVersion();

  if (!latest || !isNewer(latest, current)) return;

  line();
  line(`${s.yellow}⬆ Update available${s.reset}  ${s.dim}${current}${s.reset} → ${s.green}${latest}${s.reset}`);
  line(`  Run ${s.cyan}bunx ampcode-connector@latest${s.reset} to update`);
  line();
}


================================================
FILE: tests\code-assist.test.ts
================================================
/** Integration test: @google/genai SDK → proxy → Google CCA → response.
 *
 *  Proves the proxy correctly translates between Amp CLI's Vertex AI format
 *  and Cloud Code Assist's /v1internal envelope — using the real SDK and real endpoint. */

import { afterAll, beforeAll, describe, expect, test } from "bun:test";
import { GoogleGenAI } from "@google/genai";
import { google } from "../src/auth/configs.ts";
import * as oauth from "../src/auth/oauth.ts";
import * as store from "../src/auth/store.ts";
import { provider as googleProvider } from "../src/providers/google.ts";
import * as rewriter from "../src/proxy/rewriter.ts";
import type { ParsedBody } from "../src/server/body.ts";
import * as path from "../src/utils/path.ts";

let creds: ReturnType<typeof store.get>;

beforeAll(async () => {
  creds = store.get("google");
  if (!creds) throw new Error("No google credentials — run `bun run login` first");
  const freshToken = await oauth.token(google);
  if (!freshToken) throw new Error("Failed to refresh google token");
});

/** Minimal proxy that uses the unified Google provider. */
function proxyServer() {
  return Bun.serve({
    port: 0,
    async fetch(req) {
      const { pathname } = new URL(req.url);
      const sub = path.subpath(pathname);
      const raw = req.method === "POST" ? await req.text() : "";
      const parsed = raw ? (JSON.parse(raw) as Record<string, unknown>) : null;
      const model = (parsed && typeof parsed.model === "string" ? parsed.model : null) ?? path.modelFromUrl(sub);
      const body: ParsedBody = {
        raw,
        parsed,
        ampModel: model,
        stream: parsed?.stream === true,
        forwardBody: raw,
      };
      const rewrite = model ? rewriter.rewrite(model) : undefined;
      return googleProvider.forward(sub, body, req.headers, rewrite);
    },
  });
}

describe("google provider via @google/genai SDK", () => {
  let server: ReturnType<typeof Bun.serve>;
  let client: InstanceType<typeof GoogleGenAI>;

  beforeAll(() => {
    server = proxyServer();
    client = new GoogleGenAI({
      apiKey: "placeholder",
      vertexai: true,
      httpOptions: {
        baseUrl: `http://localhost:${server.port}/api/provider/google`,
        headers: { Authorization: "Bearer test" },
      },
    });
  });

  afterAll(() => server?.stop());

  test("non-streaming generateContent", async () => {
    const result = await client.models.generateContent({
      model: "gemini-3-flash",
      contents: [{ role: "user", parts: [{ text: "Say hi in one word" }] }],
      config: { maxOutputTokens: 500, temperature: 0.1 },
    });

    expect(result.candidates).toBeDefined();
    expect(result.candidates!.length).toBeGreaterThan(0);
    expect(result.text).toBeTruthy();
    expect(result.modelVersion).toContain("gemini");
  });

  test("streaming generateContentStream", async () => {
    const stream = await client.models.generateContentStream({
      model: "gemini-3-flash",
      contents: [{ role: "user", parts: [{ text: "Say hello in one word" }] }],
      config: { maxOutputTokens: 500, temperature: 0.1 },
    });

    let chunks = 0;
    let gotContent = false;
    for await (const chunk of stream) {
      chunks++;
      if (chunk.text) gotContent = true;
    }

    expect(chunks).toBeGreaterThan(0);
    expect(gotContent).toBe(true);
  });
});

describe("direct SDK to CCA rejects Vertex paths", () => {
  test("returns 404 (proves proxy translation is required)", async () => {
    const direct = new GoogleGenAI({
      apiKey: "placeholder",
      vertexai: true,
      httpOptions: {
        baseUrl: "https://cloudcode-pa.googleapis.com",
        headers: { Authorization: `Bearer ${creds!.accessToken}` },
      },
    });

    try {
      await direct.models.generateContent({
        model: "gemini-3-flash",
        contents: [{ role: "user", parts: [{ text: "hi" }] }],
        config: { maxOutputTokens: 10 },
      });
      throw new Error("Should have thrown");
    } catch (e: unknown) {
      expect((e as { status: number }).status).toBe(404);
    }
  });
});


================================================
FILE: tests\forward.test.ts
================================================
import { afterAll, beforeAll, describe, expect, test } from "bun:test";
import { denied, type ForwardOptions, forward } from "../src/providers/forward.ts";

/** Minimal HTTP server that simulates provider responses. */
const baseUrl = "http://mock.local";
const originalFetch = globalThis.fetch;

// Track requests for assertions
const requests: { url: string; body: string; headers: Record<string, string> }[] = [];

// Configurable response behavior
const nextResponses: Array<{ status: number; body: string; headers?: Record<string, string> } | { error: Error }> = [];

function enqueue(status: number, body: string, headers?: Record<string, string>): void {
  nextResponses.push({ status, body, headers });
}

function enqueueError(error: Error): void {
  nextResponses.push({ error });
}

beforeAll(() => {
  globalThis.fetch = (async (input, init) => {
    const req = input instanceof Request ? input : new Request(String(input), init);
    const body = await req.text();
    const hdrs: Record<string, string> = {};
    req.headers.forEach((v, k) => {
      hdrs[k] = v;
    });
    requests.push({ url: req.url, body, headers: hdrs });

    const next = nextResponses.shift();
    if (!next) return new Response("no mock configured", { status: 500 });
    if ("error" in next) throw next.error;

    return new Response(next.body, {
      status: next.status,
      headers: { "Content-Type": "application/json", ...next.headers },
    });
  }) as typeof fetch;
});

afterAll(() => {
  globalThis.fetch = originalFetch;
});

function opts(overrides?: Partial<ForwardOptions>): ForwardOptions {
  return {
    url: `${baseUrl}/test`,
    body: '{"prompt":"hello"}',
    streaming: false,
    headers: { "Content-Type": "application/json" },
    providerName: "TestProvider",
    ...overrides,
  };
}

function clearRequests(): void {
  requests.length = 0;
  nextResponses.length = 0;
}

describe("forward", () => {
  test("returns successful JSON response", async () => {
    clearRequests();
    enqueue(200, '{"result":"ok"}');

    const res = await forward(opts());
    expect(res.status).toBe(200);
    expect(await res.json()).toEqual({ result: "ok" });
    expect(requests).toHaveLength(1);
    expect(requests[0]!.body).toBe('{"prompt":"hello"}');
  });

  test("retries on 500 and eventually succeeds", async () => {
    clearRequests();
    enqueue(500, "server error");
    enqueue(500, "server error");
    enqueue(200, '{"result":"recovered"}');

    const res = await forward(opts());
    expect(res.status).toBe(200);
    expect(await res.json()).toEqual({ result: "recovered" });
    expect(requests).toHaveLength(3);
  });

  test("retries on fetch error and eventually succeeds", async () => {
    clearRequests();
    enqueueError(new Error("ECONNRESET"));
    enqueue(200, '{"ok":true}');

    const res = await forward(opts());
    expect(res.status).toBe(200);
    expect(requests).toHaveLength(2);
  });

  test("returns error response on non-retryable 4xx", async () => {
    clearRequests();
    enqueue(422, '{"error":"validation"}');

    const res = await forward(opts());
    expect(res.status).toBe(422);
    expect(await res.text()).toBe('{"error":"validation"}');
    expect(requests).toHaveLength(1);
  });

  test("returns 429 without retry (handled at routing layer)", async () => {
    clearRequests();
    enqueue(429, '{"error":"rate limited"}');

    const res = await forward(opts());
    expect(res.status).toBe(429);
    expect(requests).toHaveLength(1);
  });

  test("applies rewrite to non-streaming response", async () => {
    clearRequests();
    enqueue(200, '{"model":"real-model"}');

    const rewrite = (data: string) => data.replace("real-model", "fake-model");
    const res = await forward(opts({ rewrite }));
    expect(res.status).toBe(200);
    expect(await res.text()).toBe('{"model":"fake-model"}');
  });

  test("logs email context on error", async () => {
    clearRequests();
    enqueue(403, '{"error":"forbidden"}');

    const res = await forward(opts({ email: "user@test.com" }));
    expect(res.status).toBe(403);
  });

  test("exhausts retries on persistent 500", async () => {
    clearRequests();
    enqueue(500, "fail");
    enqueue(500, "fail");
    enqueue(500, "fail");
    enqueue(500, "fail"); // attempt 0,1,2,3

    const res = await forward(opts());
    // After MAX_RETRIES (3), the 4th 500 is returned as-is
    expect(res.status).toBe(500);
    expect(requests).toHaveLength(4);
  });

  test("returns actionable Anthropic transport diagnostics after fetch retries are exhausted", async () => {
    clearRequests();
    enqueueError(new Error("ECONNRESET"));
    enqueueError(new Error("ECONNRESET"));
    enqueueError(new Error("ECONNRESET"));
    enqueueError(new Error("ECONNRESET"));

    const res = await forward(
      opts({
        providerName: "Anthropic",
      }),
    );

    expect(res.status).toBe(502);
    const body = (await res.json()) as { error: { message: string; type: string } };

================================================
FILE: tests\middleware.test.ts
================================================
import { describe, expect, test } from "bun:test";
import * as path from "../src/utils/path.ts";

describe("path.passthrough", () => {
  test("identifies management routes", () => {
    expect(path.passthrough("/api/internal")).toBe(true);
    expect(path.passthrough("/api/internal/config")).toBe(true);
    expect(path.passthrough("/api/user")).toBe(true);
    expect(path.passthrough("/api/user/profile")).toBe(true);
    expect(path.passthrough("/api/auth")).toBe(true);
    expect(path.passthrough("/api/auth/login")).toBe(true);
    expect(path.passthrough("/api/meta")).toBe(true);
    expect(path.passthrough("/api/telemetry")).toBe(true);
    expect(path.passthrough("/api/threads")).toBe(true);
    expect(path.passthrough("/api/threads/123")).toBe(true);
    expect(path.passthrough("/api/otel")).toBe(true);
    expect(path.passthrough("/api/tab")).toBe(true);
    expect(path.passthrough("/api/durable-thread-workers")).toBe(true);
  });

  test("rejects browser routes (handled separately)", () => {
    expect(path.passthrough("/threads")).toBe(false);
    expect(path.passthrough("/docs")).toBe(false);
    expect(path.passthrough("/settings")).toBe(false);
    expect(path.passthrough("/auth")).toBe(false);
  });

  test("identifies exact match routes", () => {
    expect(path.passthrough("/threads.rss")).toBe(true);
    expect(path.passthrough("/news.rss")).toBe(true);
    expect(path.browser("/threads.rss")).toBe(false);
    expect(path.browser("/news.rss")).toBe(false);
  });

  test("rejects provider routes", () => {
    expect(path.passthrough("/api/provider/anthropic/v1/messages")).toBe(false);
    expect(path.passthrough("/api/provider/openai/v1/chat/completions")).toBe(false);
    expect(path.passthrough("/api/provider/google/v1beta/models")).toBe(false);
  });

  test("rejects root path", () => {
    expect(path.passthrough("/")).toBe(false);
  });
});

describe("path.browser", () => {
  test("identifies auth routes", () => {
    expect(path.browser("/auth")).toBe(true);
    expect(path.browser("/auth/cli-login")).toBe(true);
    expect(path.browser("/auth/sign-in")).toBe(true);
    expect(path.browser("/auth/callback")).toBe(true);
  });

  test("identifies other browser routes", () => {
    expect(path.browser("/threads")).toBe(true);
    expect(path.browser("/threads/abc")).toBe(true);
    expect(path.browser("/docs")).toBe(true);
    expect(path.browser("/docs/api")).toBe(true);
    expect(path.browser("/settings")).toBe(true);
  });

  test("rejects API routes", () => {
    expect(path.browser("/api/internal")).toBe(false);
    expect(path.browser("/api/provider/anthropic/v1/messages")).toBe(false);
  });
});

describe("path.provider", () => {
  test("extracts anthropic", () => {
    expect(path.provider("/api/provider/anthropic/v1/messages")).toBe("anthropic");
  });

  test("extracts openai", () => {
    expect(path.provider("/api/provider/openai/v1/chat/completions")).toBe("openai");
  });

  test("extracts google", () => {
    expect(path.provider("/api/provider/google/v1beta/models/gemini-pro:generateContent")).toBe("google");
  });

  test("extracts other Amp providers (passthrough to upstream)", () => {
    expect(path.provider("/api/provider/xai/v1/chat/completions")).toBe("xai");
    expect(path.provider("/api/provider/cerebras/v1/chat/completions")).toBe("cerebras");
    expect(path.provider("/api/provider/fireworks/v1/chat/completions")).toBe("fireworks");
    expect(path.provider("/api/provider/groq/v1/chat/completions")).toBe("groq");
    expect(path.provider("/api/provider/baseten/v1/chat/completions")).toBe("baseten");
    expect(path.provider("/api/provider/kimi/v1/chat/completions")).toBe("kimi");
  });

  test("returns null for non-provider paths", () => {
    expect(path.provider("/api/internal")).toBeNull();
    expect(path.provider("/")).toBeNull();
    expect(path.provider("/api/user")).toBeNull();
  });
});

describe("path.subpath", () => {
  test("extracts sub-path for anthropic", () => {
    expect(path.subpath("/api/provider/anthropic/v1/messages")).toBe("/v1/messages");
  });

  test("extracts sub-path for openai", () => {
    expect(path.subpath("/api/provider/openai/v1/chat/completions")).toBe("/v1/chat/completions");
  });

  test("extracts sub-path for google", () => {
    expect(path.subpath("/api/provider/google/v1beta/models/gemini-pro:generateContent")).toBe(
      "/v1beta/models/gemini-pro:generateContent",
    );
  });

  test("returns original path if no match", () => {
    expect(path.subpath("/api/internal")).toBe("/api/internal");
  });
});


================================================
FILE: tests\rewriter.test.ts
================================================
import { describe, expect, test } from "bun:test";
import * as rewriter from "../src/proxy/rewriter.ts";
import * as sse from "../src/utils/streaming.ts";

describe("rewriter.rewrite", () => {
  const rewrite = rewriter.rewrite("claude-opus-4-6");

  test("rewrites model field in JSON data", () => {
    const data = JSON.stringify({ model: "claude-sonnet-4-20250514", content: "hello" });
    const result = rewrite(data);
    const parsed = JSON.parse(result);
    expect(parsed.model).toBe("claude-opus-4-6");
  });

  test("rewrites nested model fields", () => {
    const data = JSON.stringify({
      message: { model: "claude-sonnet-4-20250514", role: "assistant" },
    });
    const result = rewrite(data);
    const parsed = JSON.parse(result);
    expect(parsed.message.model).toBe("claude-opus-4-6");
  });

  test("passes through [DONE] marker", () => {
    expect(rewrite("[DONE]")).toBe("[DONE]");
  });

  test("passes through non-JSON data unchanged", () => {
    expect(rewrite("not json")).toBe("not json");
  });

  test("does not add model field if not present", () => {
    const data = JSON.stringify({ content: "hello", role: "assistant" });
    const result = rewrite(data);
    const parsed = JSON.parse(result);
    expect(parsed.model).toBeUndefined();
  });

  test("suppresses thinking blocks when tool_use is present", () => {
    const data = JSON.stringify({
      content: [
        { type: "thinking", text: "Let me think..." },
        { type: "tool_use", name: "read_file", input: {} },
        { type: "text", text: "Here is the result" },
      ],
    });
    const result = rewrite(data);
    const parsed = JSON.parse(result);
    expect(parsed.content).toHaveLength(2);
    expect(parsed.content[0].type).toBe("tool_use");
    expect(parsed.content[1].type).toBe("text");
  });

  test("keeps thinking blocks when no tool_use", () => {
    const data = JSON.stringify({
      content: [
        { type: "thinking", text: "Let me think..." },
        { type: "text", text: "Here is the result" },
      ],
    });
    const result = rewrite(data);
    const parsed = JSON.parse(result);
    expect(parsed.content).toHaveLength(2);
    expect(parsed.content[0].type).toBe("thinking");
  });
});

describe("sse.parse", () => {
  test("parses single event", () => {
    const chunk = 'data: {"model":"claude"}\n\n';
    const events = sse.parse(chunk);
    expect(events).toHaveLength(1);
    expect(events[0]!.data).toBe('{"model":"claude"}');
  });

  test("parses multiple events", () => {
    const chunk = 'data: {"chunk":1}\n\ndata: {"chunk":2}\n\n';
    const events = sse.parse(chunk);
    expect(events).toHaveLength(2);
  });

  test("parses event with event type", () => {
    const chunk = 'event: message\ndata: {"text":"hi"}\n\n';
    const events = sse.parse(chunk);
    expect(events).toHaveLength(1);
    expect(events[0]!.event).toBe("message");
    expect(events[0]!.data).toBe('{"text":"hi"}');
  });

  test("handles [DONE] marker", () => {
    const chunk = "data: [DONE]\n\n";
    const events = sse.parse(chunk);
    expect(events).toHaveLength(1);
    expect(events[0]!.data).toBe("[DONE]");
  });

  test("ignores empty chunks", () => {
    expect(sse.parse("")).toHaveLength(0);
    expect(sse.parse("\n\n")).toHaveLength(0);
  });
});

describe("sse.encode", () => {
  test("encodes basic data event", () => {
    const encoded = sse.encode({ data: '{"model":"claude"}' });
    expect(encoded).toBe('data: {"model":"claude"}\n\n');
  });

  test("encodes event with type", () => {
    const encoded = sse.encode({ event: "message", data: "hello" });
    expect(encoded).toBe("event: message\ndata: hello\n\n");
  });

  test("encodes multi-line data", () => {
    const encoded = sse.encode({ data: "line1\nline2" });
    expect(encoded).toBe("data: line1\ndata: line2\n\n");
  });
});


================================================
FILE: tests\router.test.ts
================================================
import { describe, expect, test } from "bun:test";
import { parseBody } from "../src/server/body.ts";
import { resolveModel, rewriteBodyModel } from "../src/utils/models.ts";
import * as path from "../src/utils/path.ts";

describe("path.modelFromUrl", () => {
  test("extracts model from Gemini-style path", () => {
    expect(path.modelFromUrl("/v1beta/models/gemini-pro:generateContent")).toBe("gemini-pro");
  });

  test("extracts model from streaming path", () => {
    expect(path.modelFromUrl("/v1beta/models/gemini-3-flash-preview:streamGenerateContent")).toBe(
      "gemini-3-flash-preview",
    );
  });

  test("returns null for non-matching path", () => {
    expect(path.modelFromUrl("/v1/messages")).toBeNull();
  });

  test("returns null for empty path", () => {
    expect(path.modelFromUrl("")).toBeNull();
  });

  test("extracts from nested model path", () => {
    expect(path.modelFromUrl("/api/v1beta/models/gemini-pro:generateContent")).toBe("gemini-pro");
  });
});

describe("resolveModel", () => {
  test("strips -api-preview suffix", () => {
    expect(resolveModel("gpt-5.3-codex-api-preview")).toBe("gpt-5.3-codex");
  });

  test("leaves normal models unchanged", () => {
    expect(resolveModel("gpt-5.2-codex")).toBe("gpt-5.2-codex");
    expect(resolveModel("claude-opus-4-6")).toBe("claude-opus-4-6");
    expect(resolveModel("gemini-3-pro-preview")).toBe("gemini-3-pro-preview");
  });
});

describe("rewriteBodyModel", () => {
  test("replaces model in body string", () => {
    const parsed = { model: "gpt-5.3-codex-api-preview", stream: true };
    const result = rewriteBodyModel(parsed, "gpt-5.3-codex");
    expect(JSON.parse(result).model).toBe("gpt-5.3-codex");
  });

  test("preserves other fields", () => {
    const parsed = { model: "gpt-5.3-codex-api-preview", messages: [{ role: "user" }], stream: true };
    const result = rewriteBodyModel(parsed, "gpt-5.3-codex");
    const out = JSON.parse(result);
    expect(out.model).toBe("gpt-5.3-codex");
    expect(out.messages).toEqual([{ role: "user" }]);
    expect(out.stream).toBe(true);
  });

  test("does not mutate original parsed object", () => {
    const parsed = { model: "gpt-5.3-codex-api-preview", stream: true };
    rewriteBodyModel(parsed, "gpt-5.3-codex");
    expect(parsed.model).toBe("gpt-5.3-codex-api-preview");
  });
});

describe("parseBody", () => {
  test("extracts model from JSON body", () => {
    const body = parseBody(JSON.stringify({ model: "claude-opus-4-6", stream: true }), "/v1/messages");
    expect(body.ampModel).toBe("claude-opus-4-6");
    expect(body.stream).toBe(true);
    expect(body.forwardBody).toBe(body.raw);
  });

  test("falls back to URL model when body has no model field", () => {
    const body = parseBody(JSON.stringify({ stream: true }), "/v1beta/models/gemini-pro:generateContent");
    expect(body.ampModel).toBe("gemini-pro");
  });

  test("returns null model for empty body", () => {
    const body = parseBody("", "/v1/messages");
    expect(body.ampModel).toBeNull();
    expect(body.stream).toBe(false);
  });

  test("rewrites -api-preview model in forwardBody", () => {
    const raw = JSON.stringify({ model: "gpt-5.3-codex-api-preview", stream: true });
    const body = parseBody(raw, "/v1/chat/completions");
    expect(body.ampModel).toBe("gpt-5.3-codex-api-preview");
    expect(JSON.parse(body.forwardBody).model).toBe("gpt-5.3-codex");
    expect(body.raw).toBe(raw);
  });

  test("handles invalid JSON gracefully", () => {
    const body = parseBody("not json", "/v1/messages");
    expect(body.parsed).toBeNull();
    expect(body.forwardBody).toBe("not json");
  });
});

```

## File: .github\FUNDING.yml
```
# These are supported funding model platforms

github: [nghyane]
patreon: # Replace with a single Patreon username
open_collective: # Replace with a single Open Collective username
ko_fi: # Replace with a single Ko-fi username
tidelift: # Replace with a single Tidelift platform-name/package-name e.g., npm/babel
community_bridge: # Replace with a single Community Bridge project-name e.g., cloud-foundry
liberapay: # Replace with a single Liberapay username
issuehunt: # Replace with a single IssueHunt username
lfx_crowdfunding: # Replace with a single LFX Crowdfunding project-name e.g., cloud-foundry
polar: # Replace with a single Polar username
buy_me_a_coffee: # Replace with a single Buy Me a Coffee username
thanks_dev: # Replace with a single thanks.dev username
custom: # Replace with up to 4 custom sponsorship URLs e.g., ['link1', 'link2']

```

## File: amp-extractions-latest\README.md
```
# Amp CLI Extractions (Latest Local Binary)

This directory is a refreshed extraction snapshot built from the latest local Amp CLI binary.

## Source

- **Binary:** `~/.amp/bin/amp`
- **Version detected:** `0.0.1773129970-gb3ab74`
- **Generated:** 2026-03-10

## Files

- `config/settings.md` — settings registry from help + internal `UE0` object (public + hidden keys)
- `config/endpoints.md` — endpoint and service URL candidates from binary strings scan
- `agents/agent-tools.md` — full tool descriptions and schemas from `amp tools show`
- `agents/agent-architecture.md` — mode tool matrix + mode/subagent model mapping

## Notes

- This folder is separate from `references/` to avoid modifying read-only reference content.
- Endpoint extraction is static/best-effort; verify runtime traffic if you need exact invocation behavior.

```

## File: amp-extractions-latest\agents\agent_architecture.md
```
# AMP CLI Agent Architecture Notes (Latest Binary)

- **Source binary:** `~/.amp/bin/amp`
- **Version:** `0.0.1773129970-gb3ab74 (released 2026-03-10T08:11:50.960Z, 2h ago)`
- **Extraction date:** 2026-03-10T11:07:32.130Z
- **Method:** `amp tools list --json --mode <mode>` + binary strings extraction (objects `Xy` and `Wt`).

## Tool Availability By Mode

| Mode | Tool Count | Tools |
|---|---:|---|
| `smart` | 23 | `Bash`, `chart`, `create_file`, `edit_file`, `find_thread`, `finder`, `glob`, `Grep`, `handoff`, `librarian`, `look_at`, `mermaid`, `oracle`, `painter`, `Read`, `read_mcp_resource`, `read_thread`, `read_web_page`, `skill`, `Task`, `task_list`, `undo_edit`, `web_search` |
| `deep` | 13 | `apply_patch`, `chart`, `find_thread`, `finder`, `handoff`, `librarian`, `oracle`, `painter`, `read_thread`, `read_web_page`, `shell_command`, `skill`, `web_search` |
| `rush` | 23 | `Bash`, `chart`, `create_file`, `edit_file`, `find_thread`, `finder`, `glob`, `Grep`, `handoff`, `librarian`, `look_at`, `mermaid`, `oracle`, `painter`, `Read`, `read_mcp_resource`, `read_thread`, `read_web_page`, `skill`, `Task`, `task_list`, `undo_edit`, `web_search` |
| `free` | 15 | `Bash`, `chart`, `create_file`, `edit_file`, `find_thread`, `finder`, `glob`, `Grep`, `mermaid`, `Read`, `read_thread`, `read_web_page`, `skill`, `task_list`, `web_search` |

## Primary Model By Agent Mode

| Mode | Primary Model Constant |
|---|---|
| `smart` | `CLAUDE_OPUS_4_6` |
| `free` | `CLAUDE_HAIKU_4_5` |
| `rush` | `CLAUDE_HAIKU_4_5` |
| `agg-man` | `CLAUDE_OPUS_4_6` |
| `large` | `CLAUDE_SONNET_4_6` |
| `deep` | `GPT_5_3_CODEX` |
| `internal` | `GPT_5_4` |

## Subagent Model Mapping

| Subagent | Model Constant |
|---|---|
| `finder` | `CLAUDE_HAIKU_4_5` |
| `oracle` | `GPT_5_4` |
| `librarian` | `CLAUDE_SONNET_4_6` |
| `task-subagent` | `(dynamic/default)` |
| `code-review` | `CLAUDE_SONNET_4_5` |
| `code-tour` | `CLAUDE_OPUS_4_6` |
| `codereview-check` | `CLAUDE_HAIKU_4_5` |

## Notes

- Full assembled system prompts are not publicly retrievable in this environment (`amp tools list --inspect` returns permission denied).
- This file complements `agents/agent-tools.md` with mode/subagent model mapping inferred from binary internals.

```

## File: amp-extractions-latest\agents\agent_tools.md
```
# AMP CLI Agent Tools (Latest Binary)

- **Source binary:** `~/.amp/bin/amp`
- **Version:** `0.0.1773129970-gb3ab74 (released 2026-03-10T08:11:50.960Z, 2h ago)`
- **Extraction date:** 2026-03-10T11:05:25.332Z
- **Method:** `amp tools list` + `amp tools show <tool>`.

## Active Tools List

```text
23 tools available

Built-in
  Bash               Executes the given shell command using bash (or sh on systems without bash)
  chart              Render a chart visualization by running a command that produces JSON data
  create_file        Create or overwrite a file in the workspace
  edit_file          Make edits to a text file
  find_thread        Find Amp threads (conversation threads with the agent) using a query DSL
  finder             Intelligently search your codebase
  glob               Fast file pattern matching tool that works with any codebase size
  Grep               Search for exact text patterns in files using ripgrep, a fast keyword search tool
  handoff            Hand off work to a new thread that runs in the background
  librarian          The Librarian - a specialized codebase understanding agent that helps answer questions about large, complex codebases
  look_at            Extract specific information from a local file (including PDFs, images, and other media)
  mermaid            Renders a Mermaid diagram from the provided code
  oracle             Consult the oracle - an AI advisor powered by OpenAI's GPT-5
  painter            Generate an image using an AI model
  Read               Read a file or list a directory from the file system
  read_mcp_resource  Read a resource from an MCP (Model Context Protocol) server
  read_thread        Read and extract relevant content from another Amp thread by its ID
  read_web_page      Read the contents of a web page at a given URL
  skill              Load a specialized skill that provides domain-specific instructions and workflows
  Task               Perform a task (a sub-task of the user's overall task) using a sub-agent that has access to the following tools
  task_list          Plan and track tasks
  undo_edit          Undo the last edit made to a file
  web_search         Search the web for information relevant to a research objective
```

## Tool Definitions (Full Dump)

```text
===== TOOL: Bash =====
# Bash (built-in)

Executes the given shell command using bash (or sh on systems without bash).

- Do NOT chain commands with `;` or `&&` or use `&` for background processes; make separate tool calls instead
- Do NOT use interactive commands (REPLs, editors, password prompts)
- Output is truncated to the last 50000 characters
- Environment variables and `cd` do not persist between commands; use the `cwd` parameter instead
- Commands run in the workspace root by default; only use `cwd` when you need a different directory (never use `cd dir && cmd`)
- Only the last 50000 characters of the output will be returned to you along with how many lines got truncated, if any; rerun with a grep or head/tail filter if needed
- On Windows, use PowerShell commands and `\` path separators
- ALWAYS quote file paths: `cat "path with spaces/file.txt"`
- Use finder/Grep instead of find/grep, Read instead of cat, edit_file instead of sed
- Only run `git commit` and `git push` if explicitly instructed by the user.


# Schema

- cmd (string): The shell command to execute
- cwd (string): Absolute path to a directory where the command will be executed (must be absolute, not relative)


===== TOOL: chart =====
# chart (built-in)

Render a chart visualization by running a command that produces JSON data. The chart is displayed inline to the user.

Use this tool to visualize data as bar charts, line charts, or area charts. You provide a shell command that outputs JSON, and specify which columns map to the X and Y axes, the chart type, and display options.

# Parameters

- **cmd**: A shell command to execute that must produce JSON output (a JSON array of objects). The command is run via the Bash tool internally. Pipe through `jq -c .` if needed to produce compact JSON.
- **chartType**: "bar", "line", or "area"
- **xColumn**: The column name to use for the X axis (labels)
- **yColumns**: Array of column names for the Y axis. Multiple columns create multiple series (e.g., overlay revenue and expenses on the same chart).
- **title**: Chart title displayed above the chart
- **stacked**: When true with multiple yColumns, stack the series instead of overlaying them. Works with bar and area charts.
- **horizontal**: When true with bar chartType, renders horizontal bars (good for categorical data with long labels).
- **hoverColumns**: Extra column names to show in the hover tooltip but not plotted on the Y axis.
- **groupColumn**: A column whose unique values become separate series. Use with a single yColumn to pivot unpivoted data — e.g., rows with a "type" column become one series per type. Commonly used with stacked charts.

# When to use this tool

- When the user explicitly asks to "chart", "graph", "plot", or "visualize" data
- When the user explicitly requests a visual representation of data
- Do NOT use this tool proactively for tabular data unless the user asks for a visualization

# Examples

Bar chart from a BigQuery query:
{"cmd":"bq query --format=json --nouse_legacy_sql 'SELECT name, score FROM dataset.table LIMIT 10'","chartType":"bar","xColumn":"name","yColumns":["score"],"title":"Test Scores"}

Multi-series comparison:
{"cmd":"cat data.json","chartType":"bar","xColumn":"month","yColumns":["revenue","expenses"],"title":"Revenue vs Expenses"}

Horizontal bar chart:
{"cmd":"echo '[{\"tool\":\"Bash\",\"count\":42},{\"tool\":\"Read\",\"count\":31}]'","chartType":"bar","xColumn":"tool","yColumns":["count"],"title":"Tool Usage","horizontal":true}

Stacked area chart:
{"cmd":"cat commits.json","chartType":"area","xColumn":"date","yColumns":["frontend","backend"],"title":"Commits by Team","stacked":true}

Stacked area chart with groupColumn (auto-pivots rows by credit_type):
{"cmd":"bq query --format=json --nouse_legacy_sql 'SELECT hour, credits, credit_type FROM dataset.usage'","chartType":"area","xColumn":"hour","yColumns":["credits"],"groupColumn":"credit_type","title":"Credits by Type","stacked":true}

# Best practices

- Pipe through `jq -c .` if the command might produce non-JSON text (headers, warnings) or pretty-printed output that could break parsing.
- The chart renders at most 100 points per series (extra rows are silently dropped). Use aggregation (GROUP BY) or LIMIT so the JSON output stays under this threshold.
- Use `groupColumn` to pivot flat rows into multiple series instead of running separate queries or reshaping data manually.
- ISO-date xColumn values (YYYY-MM-DD…) are automatically sorted ascending; categorical labels preserve source order.
- Include a `link` key in JSON rows to make tooltip values clickable hyperlinks.
- Use `hoverColumns` to surface extra context (IDs, descriptions) in tooltips without adding chart clutter.
- Choose `horizontal: true` for bar charts when labels are long (e.g. file paths, URLs).

# Schema

- cmd (string): A shell command to execute that produces JSON output (a JSON array of objects).
- chartType (string): The type of chart to render.
- xColumn (string): Column name to use for the X axis (labels).
- yColumns (array of string): Column name(s) for the Y axis. Multiple columns create multiple series.
- title (string): Chart title.
- subtitle (string): Optional subtitle shown below the title.
- xAxisLabel (string): Label for the X axis. Defaults to the xColumn name.
- yAxisLabel (string): Label for the Y axis. Defaults to the first yColumn name.
- stacked (boolean): Stack multiple series instead of overlaying. Works with bar and area charts.
- horizontal (boolean): Render bars horizontally. Only applies to bar chartType.
- hoverColumns (array of string): Extra columns to display in hover tooltips but not plotted on the Y axis.
- groupColumn (string): Column whose unique values become separate series. Pivots unpivoted data — e.g., a "type" column creates one series per type. Use with a single yColumn.


===== TOOL: create_file =====
# create_file (built-in)

Create or overwrite a file in the workspace.

Use this tool to create a **new file** that does not yet exist.

For **existing files**, prefer `edit_file` instead—even for extensive changes. Only use `create_file` to overwrite an existing file when you are replacing nearly all of its content AND the file is small (under ~250 lines).


# Schema

- path (string): The absolute path of the file to be created (must be absolute, not relative). If the file exists, it will be overwritten. ALWAYS generate this argument first.
- content (string): The content for the file.


===== TOOL: edit_file =====
# edit_file (built-in)

Make edits to a text file.

Replaces `old_str` with `new_str` in the given file.

Returns a git-style diff showing the changes made as formatted markdown, along with the line range ([startLine, endLine]) of the changed content. The diff is also shown to the user.

The file specified by `path` MUST exist, and it MUST be an absolute path. If you need to create a new file, use `create_file` instead.

`old_str` MUST exist in the file. Use tools like `Read` to understand the files you are editing before changing them.

`old_str` and `new_str` MUST be different from each other.

Set `replace_all` to true to replace all occurrences of `old_str` in the file. Else, `old_str` MUST be unique within the file or the edit will fail. Additional lines of context can be added to make the string more unique.

If you need to replace the entire contents of a file, use `create_file` instead, since it requires less tokens for the same action (since you won't have to repeat the contents before replacing)


# Schema

- path (string): The absolute path to the file (MUST be absolute, not relative). File must exist. ALWAYS generate this argument first.
- old_str (string): Text to search for. Must match exactly.
- new_str (string): Text to replace old_str with.
- replace_all (boolean): Set to true to replace all matches of old_str. Else, old_str must be an unique match.


===== TOOL: find_thread =====
# find_thread (built-in)

Find Amp threads (conversation threads with the agent) using a query DSL.

## What this tool finds

This tool searches **Amp threads** (conversations with the agent), NOT git commits. Use this when the user asks about threads, conversations, or Amp history.

## Query syntax

- **Keywords**: Bare words or quoted phrases for text search: `auth` or `"race condition"`
- **File filter**: `file:path` to find threads that touched a file: `file:src/auth/login.ts`
- **Repo filter**: `repo:url` to scope to a repository: `repo:github.com/owner/repo` or `repo:owner/repo`
- **Author filter**: `author:name` to find threads by a user: `author:alice` or `author:me` for your own threads
- **Date filters**: `after:date` and `before:date` to filter by date: `after:2024-01-15`, `after:7d`, `before:2w`
- **Task filter**: `task:id` to find threads that worked on a task: `task:142`. Use `task:142+` to include threads that worked on the task's dependencies, `task:142^` to include dependents (tasks that depend on this task), or `task:142+^` for both.
- **Cluster filter**: `cluster_of:id` to find threads in the same cluster as a thread: `cluster_of:T-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`
- **Combine filters**: Use implicit AND: `auth file:src/foo.ts repo:amp after:7d`

All matching is case-insensitive. File paths use partial matching. Date formats: ISO dates (`2024-01-15`), relative days (`7d`), or weeks (`2w`).

## When to use this tool

- "which thread touched this file" / "which thread modified this file"
- "what thread last changed X" / "find the thread that edited X"
- "find threads about X" / "search threads mentioning Y"
- Any question about Amp thread history or previous Amp conversations
- When the user says "thread" and is referring to Amp work, not git commits

## When NOT to use this tool

- If the user asks about git commits, git history, or git blame → use git commands instead
- If the user wants to know WHO (a person) made changes → use git log

# Examples

User asks: "Find threads where we discussed the monorepo migration"
```json
{"query":"monorepo migration","limit":10}
```

User asks: "Show me threads that modified src/server/index.ts"
```json
{"query":"file:src/server/index.ts","limit":5}
```

User asks: "What threads have touched this file?" (for current file in github.com/sourcegraph/amp)
```json
{"query":"file:core/src/tools/tool-service.ts repo:sourcegraph/amp"}
```

User asks: "Find auth-related threads in the amp repo"
```json
{"query":"auth repo:sourcegraph/amp"}
```

User asks: "Show me my recent threads"
```json
{"query":"author:me","limit":10}
```

User asks: "Find threads from the last week about authentication"
```json
{"query":"auth after:7d","limit":10}
```

User asks: "Which threads worked on task 142 and its dependencies?"
```json
{"query":"task:142+"}
```

User asks: "Show me all threads related to task 50 and tasks that depend on it"
```json
{"query":"task:50^"}
```


# Schema

- query (string): Search query using DSL syntax. Supports keywords, file:path, repo:url, author:name, after:date, before:date, task:id, and cluster_of:id filters.
- limit (number): Maximum number of threads to return. Defaults to 20.


===== TOOL: finder =====
# finder (built-in)

Intelligently search your codebase: Use it for complex, multi-step search tasks where you need to find code based on functionality or concepts rather than exact matches. Anytime you want to chain multiple grep calls you should use this tool.

WHEN TO USE THIS TOOL:
- You must locate code by behavior or concept
- You need to run multiple greps in sequence
- You must correlate or look for connection between several areas of the codebase.
- You must filter broad terms ("config", "logger", "cache") by context.
- You need answers to questions such as "Where do we validate JWT authentication headers?" or "Which module handles file-watcher retry logic"

WHEN NOT TO USE THIS TOOL:
- When you know the exact file path - use Read directly
- When looking for specific symbols or exact strings - use glob or Grep
- When you need to create, modify files, or run terminal commands

USAGE GUIDELINES:
1. Always spawn multiple search agents in parallel to maximise speed.
2. Formulate your query as a precise engineering request.
   ✓ "Find every place we build an HTTP error response."
   ✗ "error handling search"
3. Name concrete artifacts, patterns, or APIs to narrow scope (e.g., "Express middleware", "fs.watch debounce").
4. State explicit success criteria so the agent knows when to stop (e.g., "Return file paths and line numbers for all JWT verification calls").
5. Never issue vague or exploratory commands - be definitive and goal-oriented.


# Schema

- query (string): The search query describing to the agent what it should. Be specific and include technical terms, file types, or expected code patterns to help the agent find relevant code. Formulate the query in a way that makes it clear to the agent when it has found the right thing.


===== TOOL: glob =====
# glob (built-in)

Fast file pattern matching tool that works with any codebase size

Use this tool to find files by name patterns across your codebase. Results are returned in ripgrep's traversal order, not by modification time.

## File pattern syntax

- `**/*.js` - All JavaScript files in any directory
- `src/**/*.ts` - All TypeScript files under the src directory (searches only in src)
- `*.json` - All JSON files in the current directory
- `**/*test*` - All files with "test" in their name
- `web/src/**/*` - All files under the web/src directory
- `**/*.{js,ts}` - All JavaScript and TypeScript files (alternative patterns)
- `src/[a-z]*/*.ts` - TypeScript files in src subdirectories that start with lowercase letters

# Examples

Find all typescript files in the codebase
```json
{"filePattern":"**/*.ts"}
```

Find all test files under a specific directory
```json
{"filePattern":"src/**/*test*.ts"}
```

Search for svelte component files in the web/src directory
```json
{"filePattern":"web/src/**/*.svelte"}
```

Find up to 10 JSON files
```json
{"filePattern":"**/*.json","limit":10}
```


# Schema

- filePattern (string): Glob pattern like "**/*.js" or "src/**/*.ts" to match files
- limit (number): Maximum number of results to return (default: 200, max: 1000)
- offset (number): Number of results to skip (for pagination)


===== TOOL: Grep =====
# Grep (built-in)

Search for exact text patterns in files using ripgrep, a fast keyword search tool.

# When to use this tool
- Finding exact text matches (variable names, function calls, specific strings)
- Use finder for semantic/conceptual searches

# Strategy
- Use 'path' or 'glob' to narrow searches; run multiple focused calls rather than one broad search
- Uses Rust-style regex (escape `{` and `}`); use `literal: true` for literal text search

# Constraints
- Results are limited to 100 matches (up to 10 per file)
- Lines are truncated at 200 characters

# Examples

Find a specific function name across the codebase
```json
{"pattern":"registerTool","path":"core/src"}
```

Search for interface definitions in a specific directory
```json
{"pattern":"interface ToolDefinition","path":"core/src/tools"}
```

Use a case-sensitive search to find the exact string `ERROR:`
```json
{"pattern":"ERROR:","caseSensitive":true}
```

Find TODO comments in frontend code
```json
{"pattern":"TODO:","path":"web/src"}
```

Find a specific function name in test files
```json
{"pattern":"restoreThreads","glob":"**/*.test.ts"}
```

Find all REST API endpoint definitions
```json
{"pattern":"app\\.(get|post|put|delete)\\([\"']","path":"server"}
```

Locate CSS class definition in stylesheets
```json
{"pattern":"\\.container\\s*\\{","path":"web/src/styles"}
```

# Complementary to finder
- Use finder first to locate relevant code concepts
- Then use Grep to find specific implementations or all occurrences
- For complex tasks, iterate between both tools to refine your understanding


# Schema

- pattern (string): The pattern to search for (regex)
- path (string): The file or directory path to search in. Cannot be used with glob.
- glob (string): The glob pattern to search for. Cannot be used with path.
- caseSensitive (boolean): Whether to search case-sensitively
- literal (boolean): Whether to treat the pattern as a literal string instead of a regex


===== TOOL: handoff =====
# handoff (built-in)

Hand off work to a new thread that runs in the background. Use this tool when you need to continue work in a fresh context because:
- The current thread is getting too long and context is degrading
- You want to start a new focused task while preserving context from the current thread
- The current thread's context window is near capacity

When you call this tool:
1. A new thread will be created with relevant context from this thread
2. The new thread will start running in the background
3. The current thread continues to run - you can finish up any remaining work

When the user message tells you to continue the work or to handoff to only one new thread, you should follow to the new thread by setting follow to true.

The goal parameter should describe what work should continue in the new thread. Keep it short—a single sentence or at most one paragraph. Focus on what needs to be done next, not what was already completed.

Use the mode parameter when the user explicitly requests a different agent mode (e.g., "deep", "smart", "rush") for the new thread.

# Schema

- goal (string): A short description of the next task to accomplish in the new thread. Should be a single sentence or at most one paragraph. Focus on what needs to be done next, not what was already completed.
- follow (boolean): If true, navigate to the new thread after creation. Use this when the current thread is stopping and work should continue in the new thread.
- mode (string): The agent mode for the new thread. Defaults to the current thread's agent mode if not specified.


===== TOOL: librarian =====
# librarian (built-in)

The Librarian - a specialized codebase understanding agent that helps answer questions about large, complex codebases.
The Librarian works by reading from GitHub - it can see the private repositories the user approved access to in addition to all public repositories on GitHub.
The Librarian also supports Bitbucket Enterprise (self-hosted) repositories when the user has connected their Bitbucket Enterprise instance.

The Librarian acts as your personal multi-repository codebase expert, providing thorough analysis and comprehensive explanations across repositories.

It's ideal for complex, multi-step analysis tasks where you need to understand code architecture, functionality, and patterns across multiple repositories.

WHEN TO USE THE LIBRARIAN:
- Understanding complex multi-repository codebases and how they work
- Exploring relationships between different repositories
- Analyzing architectural patterns across large open-source projects
- Finding specific implementations across multiple codebases
- Understanding code evolution and commit history
- Getting comprehensive explanations of how major features work
- Exploring how systems are designed end-to-end across repositories

WHEN NOT TO USE THE LIBRARIAN:
- Simple local file reading (use Read directly)  
- Local codebase searches (use finder)
- Code modifications or implementations (use other tools)
- Questions not related to understanding existing repositories

USAGE GUIDELINES:
1. Be specific about what repositories or projects you want to understand
2. Provide context about what you're trying to achieve
3. The Librarian will explore thoroughly across repositories before providing comprehensive answers
4. Expect detailed, documentation-quality responses suitable for sharing
5. When getting an answer from the Librarian, show it to the user in full, do not summarize it.

EXAMPLES:
- "How does authentication work in the Kubernetes codebase?"
- "Explain the architecture of the React rendering system"
- "Find how database migrations are handled in Rails"
- "Understand the plugin system in the VSCode codebase"
- "Compare how different web frameworks handle routing"
- "What changed in commit abc123 in my private repository?"
- "Show me the diff for commit fb492e2 in github.com/mycompany/private-repo"
- "Read the README from the main API repo on our Bitbucket Enterprise instance"


# Schema

- query (string): Your question about the codebase. Be specific about what you want to understand or explore.
- context (string): Optional context about what you're trying to achieve or background information.


===== TOOL: look_at =====
# look_at (built-in)

Extract specific information from a local file (including PDFs, images, and other media).

Use this tool when you need to extract or summarize information from a file without getting the literal contents. Always provide a clear objective describing what you want to learn or extract.

Pass reference files when you need to compare two or more things.

## When to use this tool

- Analyzing PDFs, images, or media files that the Read tool cannot interpret
- Extracting specific information or summaries from documents
- Describing visual content in images or diagrams
- When you only need analyzed/extracted data, not raw file contents

## When NOT to use this tool

- For source code or plain text files where you need exact contents—use Read instead
- When you need to edit the file afterward (you need the literal content from Read)
- For simple file reading where no interpretation is needed

# Examples

Summarize a local PDF document with a specific goal
```json
{"path":"docs/specs/system-design.pdf","objective":"Summarize main architectural decisions.","context":"We are evaluating this system design for a new project we are building."}
```

Describe what is shown in an image file
```json
{"path":"assets/mockups/homepage.png","objective":"Describe the layout and main UI elements.","context":"We are creating a UI component library and need to understand the visual structure."}
```

Compare two screenshots to identify visual differences
```json
{"path":"screenshots/before.png","objective":"Identify all visual differences between the two screenshots.","context":"We are reviewing UI changes for a feature update and need to document all differences.","referenceFiles":["screenshots/after.png"]}
```


# Schema

- path (string): Absolute path to the file to analyze.
- objective (string): Natural-language description of the analysis goal (e.g., summarize, extract data, describe image).
- context (string): The broader goal and context for the analysis. Include relevant background information about what you are trying to achieve and why this analysis is needed.
- referenceFiles (array of string): Optional list of absolute paths to reference files for comparison (e.g., to compare two screenshots or documents).


===== TOOL: mermaid =====
# mermaid (built-in)

Renders a Mermaid diagram from the provided code.

PROACTIVELY USE DIAGRAMS when they would better convey information than prose alone. The diagrams produced by this tool are shown to the user.

You should create diagrams WITHOUT being explicitly asked in these scenarios:
- When explaining system architecture or component relationships
- When describing workflows, data flows, or user journeys
- When explaining algorithms or complex processes
- When illustrating class hierarchies or entity relationships
- When showing state transitions or event sequences

Diagrams are especially valuable for visualizing:
- Application architecture and dependencies
- API interactions and data flow
- Component hierarchies and relationships
- State machines and transitions
- Sequence and timing of operations
- Decision trees and conditional logic

# Citations
- **Always include `citations` to as many nodes and edges as possible to make diagram elements clickable, linking to code locations.**
- Do not add wrong citation and if needed read the file again to validate the code links.
- Keys: node IDs (e.g., `"api"`) or edge labels (e.g., `"authenticate(token)"`)
- Values: file:// URIs with optional line range (e.g., `file:///src/api.ts#L10-L50`)

<examples>

Flowchart with clickable nodes
<example>
{"code":"flowchart LR\n    api[API Layer] --> svc[Service Layer]\n    svc --> db[(Database)]","citations":{"api":"file:///src/api/routes.ts#L1-L100","svc":"file:///src/services/index.ts#L10-L50","db":"file:///src/models/schema.ts"}}
</example>

Sequence diagram with clickable actors AND messages
<example>
{"code":"sequenceDiagram\n    Client->>Server: authenticate(token)\n    Server->>DB: validate_token()","citations":{"Client":"file:///src/client/index.ts","Server":"file:///src/server/handler.ts","authenticate(token)":"file:///src/server/auth.ts#L25-L40","validate_token()":"file:///src/db/tokens.ts#L10-L30"}}
</example>

</examples>

# Styling
- When defining custom classDefs, always define fill color, stroke color, and text color ("fill", "stroke", "color") explicitly
- IMPORTANT!!! Use DARK fill colors (close to #000) with light stroke and text colors (close to #fff)

# Schema

- code (string): The Mermaid diagram code to render (DO NOT override with custom colors or other styles, DO NOT use HTML tags in node labels)
- citations (object): REQUIRED: Map of citation keys to file:// URIs for clickable code navigation. Keys can be node IDs (e.g., "api") or edge labels (e.g., "run_rollout(request)"). Use {} if no code references apply.


===== TOOL: oracle =====
# oracle (built-in)

Consult the oracle - an AI advisor powered by OpenAI's GPT-5.4 reasoning model that can plan, review, and provide expert guidance.

The oracle has access to the following tools:
- Read
- Grep
- glob
- web_search
- read_web_page
- read_thread
- find_thread.

You should consult the oracle for:
- Code reviews and architecture feedback
- Finding difficult bugs in codepaths that flow across many files
- Planning complex implementations or refactors
- Answering complex technical questions that require deep technical reasoning
- Providing an alternative point of view when you are struggling to solve a problem

You should NOT consult the oracle for:
- File reads or simple keyword searches (use Read or Grep directly)
- Codebase searches (use finder)
- Web browsing and searching (use read_web_page or web_search)
- Basic code modifications and when you need to execute code changes (do it yourself or use Task)

Usage guidelines:
- Be specific about what you want the oracle to review, plan, or debug
- Provide relevant context about what you're trying to achieve. If you know that 3 files are involved, list them and they will be attached.

# Examples

Review the authentication system architecture and suggest improvements
```json
{"task":"Review the authentication architecture and suggest improvements","files":["src/auth/index.ts","src/auth/jwt.ts"]}
```

Plan the implementation of real-time collaboration features
```json
{"task":"Plan the implementation of real-time collaboration feature"}
```

Analyze the performance bottlenecks in the data processing pipeline
```json
{"task":"Analyze performance bottlenecks","context":"Users report slow response times when processing large datasets"}
```

Review this API design and suggest better patterns
```json
{"task":"Review API design","context":"This is a REST API for user management","files":["src/api/users.ts"]}
```

Debug failing tests after refactor
```json
{"task":"Help debug why tests are failing","context":"Tests fail with \"undefined is not a function\" after refactoring the auth module","files":["src/auth/auth.test.ts"]}
```


# Schema

- task (string): The task or question you want the oracle to help with. Be specific about what kind of guidance, review, or planning you need.
- context (string): Optional context about the current situation, what you've tried, or background information that would help the oracle provide better guidance.
- files (array of string): Optional list of specific file paths (text files, images) that the oracle should examine as part of its analysis. These files will be attached to the oracle input.


===== TOOL: painter =====
# painter (built-in)

Generate an image using an AI model.

IMPORTANT: Only invoke this tool when the user explicitly asks to use the "painter" tool. Do not use this tool automatically or proactively.

- When using this tool, request a single image at a time. Multiple input reference images are OK.
- Use savePath to specify the output file path only if the user explicitly asks for it.

## When to use this tool

- When the user explicitly asks to use the "painter" tool
- When the user explicitly requests image generation using this tool

## When NOT to use this tool

- Do NOT use automatically for UI mockups, diagrams, or icons—only unless explicitly requested by user
- For code-linked diagrams—use the "mermaid" tool instead
- For analyzing existing images—use the "look_at" tool instead

## Example Scenarios

- **Generate a image from user description**: Provide only a prompt with detailed visual instructions. No inputImagePaths needed.
- **Create with reference**: Provide one or more reference images provided by the user for style/content inspiration. The model will use these as guidance to create a new image matching your prompt. Your prompt should describe how to use each reference (e.g., "match the color palette from the first image", "use the icon style from the second").
- **Edit/composite images**: Provide the image to edit and optionally another image with elements to incorporate. The prompt should describe what to change or how to combine them.

# Examples

Generate an app icon for a CLI tool
```json
{"prompt":"1024x1024 app icon. Dark background #1a1a2e. Glowing terminal cursor symbol in cyan #00d9ff. Minimal, modern style for macOS dock."}
```

Generate a hero image using existing brand assets as reference
```json
{"prompt":"Hero image for documentation landing page. Match the color palette from the first image and icon style from the second. Abstract flowing code symbols. 1920x600 dimensions.","inputImagePaths":["/Users/alice/project/docs/assets/brand-colors.png","/Users/alice/project/docs/assets/icon-style.png"]}
```

Redact sensitive data from a terminal screenshot
```json
{"prompt":"Blur or redact any visible API keys, tokens, passwords, or email addresses in this terminal screenshot. Keep command output readable. Preserve dimensions.","inputImagePaths":["/Users/alice/project/docs/screenshots/terminal-output.png"]}
```

Generate an image and save to the Documents folder (Windows)
```json
{"prompt":"A modern company logo with blue and white colors. Clean, minimalist design.","savePath":"C:\\Users\\alice\\Documents\\logo.png"}
```


# Schema

- prompt (string): Detailed instructions for image generation based on user requirements. Include specifics about design, layout, style, colors, composition, and any other visual details the user mentioned.
- inputImagePaths (array of string): Optional image paths provided by the user for editing or style guidance. Maximum 3 images allowed. Each image path should be same as the `sourcePath` provided by the user.
- savePath (string): Optional absolute path to save the generated image (e.g., C:/Users/name/Documents/image.png on Windows, /home/user/Documents/image.png on Linux/Mac). Only valid when a single image is generated.


===== TOOL: Read =====
# Read (built-in)

Read a file or list a directory from the file system. If the path is a directory, it returns a line-numbered list of entries. If the file or directory doesn't exist, an error is returned.

- The path parameter MUST be an absolute path.
- By default, this tool returns the first 500 lines. To read more, call it multiple times with different read_ranges.
- Use the Grep tool to find specific content in large files or files with long lines.
- If you are unsure of the correct file path, use the glob tool to look up filenames by glob pattern.
- The contents are returned with each line prefixed by its line number. For example, if a file has contents "abc\
", you will receive "1: abc\
". For directories, entries are returned one per line (without line numbers) with a trailing "/" for subdirectories.
- This tool can read images (such as PNG, JPEG, and GIF files) and present them to the model visually.
- When possible, call this tool in parallel for all files you will want to read.
      - Avoid tiny repeated slices (e.g., 50\u2011line chunks). If you need more context from the same file, read a larger range or the full default window instead.

# Schema

- path (string): The absolute path to the file or directory (MUST be absolute, not relative).
- read_range (array of number): An array of two integers specifying the start and end line numbers to view. Line numbers are 1-indexed. If not provided, defaults to [1, 1000]. Examples: [500, 700], [700, 1400]


===== TOOL: read_mcp_resource =====
# read_mcp_resource (built-in)

Read a resource from an MCP (Model Context Protocol) server.

Use when the user references an MCP resource, e.g. "read @filesystem-server:file:///path/to/document.txt"

# Examples

Read a file from an MCP file server
```json
{"server":"filesystem-server","uri":"file:///path/to/document.txt"}
```

Read a database record from an MCP database server
```json
{"server":"database-server","uri":"db://users/123"}
```


# Schema

- server (string): The name or identifier of the MCP server to read from
- uri (string): The URI of the resource to read


===== TOOL: read_thread =====
# read_thread (built-in)

Read and extract relevant content from another Amp thread by its ID.

This tool fetches a thread (locally or from the server if synced), renders it as markdown, and uses AI to extract only the information relevant to your specific goal. This keeps context concise while preserving important details.

## When to use this tool

- When the user pastes or references an Amp thread URL (format: https://ampcode.com/threads/T-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx) in their message
- When the user references a thread ID (format: T-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx or @T-abc123)
- When the user asks to "apply the same approach from [thread URL]"
- When the user says "do what we did in [thread URL]"
- When the user says "implement the plan we devised in [thread URL]"
- When you need to extract specific information from a referenced thread

## When NOT to use this tool

- When no thread ID is mentioned
- When working within the current thread (context is already available)

## Parameters

- **threadID**: The thread identifier in format T-{uuid} (e.g., "T-a38f981d-52da-47b1-818c-fbaa9ab56e0c")
- **goal**: A clear description of what information you're looking for in that thread. Be specific about what you need to extract.

# Examples

User asks "Implement the plan we devised in https://ampcode.com/threads/T-3f1beb2b-bded-4fda-96cc-1af7192f24b6"
```json
{"threadID":"T-3f1beb2b-bded-4fda-96cc-1af7192f24b6","goal":"Extract the implementation plan, design decisions, architecture approach, and any code patterns or examples discussed"}
```

User asks: "Do what we did in https://ampcode.com/threads/T-f916b832-c070-4853-8ab3-5e7596953bec, but for the Oracle tool"
```json
{"threadID":"T-f916b832-c070-4853-8ab3-5e7596953bec","goal":"Extract the implementation approach, code patterns, techniques used, and any relevant code examples that can be adapted for the Oracle tool"}
```

User asks: "Take the SQL queries from https://ampcode.com/threads/T-95e73a95-f4fe-4f22-8d5c-6297467c97a5 and turn it into a reusable script"
```json
{"threadID":"T-95e73a95-f4fe-4f22-8d5c-6297467c97a5","goal":"Extract all SQL queries, their purpose, parameters, and any context needed to understand how to make them reusable"}
```

User asks: "Apply the same fix from @T-def456 to this issue"
```json
{"threadID":"T-def456","goal":"Extract the bug description, root cause, the fix/solution, and relevant code changes"}
```


# Schema

- threadID (string): The thread ID in format T-{uuid} (e.g., "T-a38f981d-52da-47b1-818c-fbaa9ab56e0c")
- goal (string): A clear description of what information you need from the thread. Be specific about what to extract.


===== TOOL: read_web_page =====
# read_web_page (built-in)

Read the contents of a web page at a given URL.

When only the url parameter is set, it returns the contents of the webpage converted to Markdown.

When an objective is provided, it returns excerpts relevant to that objective.

If the user asks for the latest or recent contents, pass `forceRefetch: true` to ensure the latest content is fetched.

Do NOT use for access to localhost or any other local or non-Internet-accessible URLs; use `curl` via the Bash instead.

# Examples

Summarize recent changes for a library. Force refresh because freshness is important.
```json
{"url":"https://example.com/changelog","objective":"Summarize the API changes in this software library.","forceRefetch":true}
```

Extract all text content from a web page
```json
{"url":"https://example.com/docs/getting-started"}
```


# Schema

- url (string): The URL of the web page to read
- objective (string): A natural-language description of the research goal. If set, only relevant excerpts will be returned. If not set, the full content of the web page will be returned. 
- forceRefetch (boolean): Force a live fetch of the URL (default: use a cached version that may be a few days old)


===== TOOL: skill =====
# skill (built-in)

Load a specialized skill that provides domain-specific instructions and workflows.

When you recognize that a task matches one of the available skills listed below, use this tool to load the full skill instructions.

The skill will inject detailed instructions, workflows, and access to bundled resources (scripts, references, templates) into the conversation context.

Parameters:
- name: The name of the skill to load (must match one of the skills listed below)

Example: To use the web-browser skill for interacting with web pages, call this tool with name: "web-browser"

# Available Skills

{{AVAILABLE_SKILLS}}

# Schema

- name (string): The name of the skill to load
- arguments (string): Optional arguments to pass to the skill


===== TOOL: Task =====
# Task (built-in)

Perform a task (a sub-task of the user's overall task) using a sub-agent that has access to the following tools: Grep, glob, Read, Bash, edit_file, create_file, read_web_page, get_diagnostics, web_search, finder, skill, task_list.


When to use the Task tool:
- When you need to perform complex multi-step tasks
- When you need to run an operation that will produce a lot of output (tokens) that is not needed after the sub-agent's task completes
- When you are making changes across many layers of an application (frontend, backend, API layer, etc.), after you have first planned and spec'd out the changes so they can be implemented independently by multiple sub-agents
- When the user asks you to launch an "agent" or "subagent", because the user assumes that the agent will do a good job

When NOT to use the Task tool:
- When you are performing a single logical task, such as adding a new feature to a single part of an application.
- When you're reading a single file (use Read), performing a text search (use Grep), editing a single file (use edit_file)
- When you're not sure what changes you want to make. Use all tools available to you to determine the changes to make.

How to use the Task tool:
- Run multiple sub-agents concurrently if the tasks may be performed independently (e.g., if they do not involve editing the same parts of the same file), by including multiple tool uses in a single assistant message.
- You will not see the individual steps of the sub-agent's execution, and you can't communicate with it until it finishes, at which point you will receive a summary of its work.
- Include all necessary context from the user's message and prior assistant steps, as well as a detailed plan for the task, in the task description. Be specific about what the sub-agent should return when finished to summarize its work.
- Tell the sub-agent how to verify its work if possible (e.g., by mentioning the relevant test commands to run).
- When the agent is done, it will return a single message back to you. The result returned by the agent is not visible to the user. To show the user the result, you should send a text message back to the user with a concise summary of the result.


# Schema

- prompt (string): The task for the agent to perform. Be specific about what needs to be done and include any relevant context.
- description (string): A very short description of the task that can be displayed to the user.


===== TOOL: task_list =====
# task_list (built-in)

Plan and track tasks. Use this tool for ALL task planning - breaking down work into steps, tracking progress, and managing what needs to be done.

Actions:
- create: Create a new task with title (required), description, repoURL, status, dependsOn, parentID
- list: List tasks with optional filters (repoURL, status, limit, ready). Completed tasks are excluded by default; use status filter to include them.
- get: Get a single task by taskID
- update: Update a task by taskID with new values
- delete: Soft delete a task by taskID

Use dependsOn to specify task dependencies - an array of task IDs that block this task. If B dependsOn A, then A blocks B (A must complete before B can start). Use `ready: true` with the list action to find tasks where all blockers are completed. Use parentID to establish parent-child relationships between tasks (for hierarchical task breakdown). Tasks persist across sessions and the creating thread ID is automatically recorded.

Write task descriptions with enough context that a future thread can pick up the work without needing the original conversation. Include relevant file paths, function names, error messages, or acceptance criteria.

# Examples

Run the build and fix any type errors:
```
create "Run the build" → gets id "build"
create "Fix type errors", dependsOn: ["build"]
[run build, find 3 errors]
create task for each error, each dependsOn: ["build"]
update "build" → completed
[fix first error]
update that task → completed
[continue...]
```

Build a new API feature (mixed sequential and parallel):
```
create "Design API schema" → gets id "design"
create "Set up database tables", dependsOn: ["design"] → gets id "db"
create "Implement API endpoints", dependsOn: ["design"] → gets id "api"
create "Write backend tests", dependsOn: ["api"] → gets id "backend-tests"
create "Build frontend components", dependsOn: ["api"] → gets id "frontend"
create "Integration tests", dependsOn: ["backend-tests", "frontend"] → gets id "integration"
create "Deploy to staging", dependsOn: ["integration"]
```
- db and api are parallel (both blocked by design)
- backend-tests chains after api
- frontend chains after api
- integration waits for BOTH backend-tests and frontend
- deploy is the final step

# Schema

- action (string): The action to perform
- taskID (string): Task ID (required for get, update, delete)
- title (string): Task title (required for create, optional for update)
- description (string): Task description
- repoURL (string): Repository URL to associate with the task
- status (string): Task status
- dependsOn (array of string): Array of task IDs this task depends on - should be done after these tasks
- parentID (string): Parent task ID for hierarchical task breakdown
- limit (number): Maximum number of tasks to return (for list action)
- ready (boolean): Filter to only return tasks that are ready to work on (all dependencies completed)


===== TOOL: undo_edit =====
# undo_edit (built-in)

Undo the last edit made to a file.

This command reverts the most recent edit made to the specified file.
It will restore the file to its state before the last edit was made.

Returns a git-style diff showing the changes that were undone as formatted markdown.


# Schema

- path (string): The absolute path to the file whose last edit should be undone (must be absolute, not relative)


===== TOOL: web_search =====
# web_search (built-in)

Search the web for information relevant to a research objective.

Use when you need up-to-date or precise documentation. Use `read_web_page` to fetch full content from a specific URL.

# Examples

Get API documentation for a specific provider
```json
{"objective":"I want to know the request fields for the Stripe billing create customer API. Prefer Stripe's docs site."}
```

See usage documentation for newly released library features
```json
{"objective":"I want to know how to use SvelteKit remote functions, which is a new feature shipped in the last month.","search_queries":["sveltekit","remote function"]}
```


# Schema

- objective (string): A natural-language description of the broader task or research goal, including any source or freshness guidance
- search_queries (array of string): Optional keyword queries to ensure matches for specific terms are prioritized (recommended for best results)
- max_results (number): The maximum number of results to return (default: 5)
```

```

## File: amp-extractions-latest\config\endpoints.md
```
# AMP CLI Endpoints Reference (Latest Binary)

- **Source binary:** `~/.amp/bin/amp`
- **Version:** `0.0.1773129970-gb3ab74 (released 2026-03-10T08:11:50.960Z, 2h ago)`
- **Extraction date:** 2026-03-10T11:04:35.859Z
- **Method:** static strings scan from binary (best-effort).

## Provider Proxy Paths

- `/api/provider/anthropic`
- `/api/provider/baseten/v1`
- `/api/provider/cerebras`
- `/api/provider/fireworks/v1`
- `/api/provider/google`
- `/api/provider/groq`
- `/api/provider/kimi`
- `/api/provider/openai/v1`
- `/api/provider/xai/v1`

## Other API Path Candidates

- `/api/1.0/projects/`
- `/api/1.0/repos`
- `/api/durable-thread-workers`
- `/api/events`
- `/api/hello`
- `/api/hello/:name`
- `/api/http`
- `/api/internal`
- `/api/internal/bitbucket-instance-url`
- `/api/internal/github-auth-status`
- `/api/internal/github-proxy/`
- `/api/session`
- `/api/sessions`
- `/api/telemetry`
- `/api/threads`
- `/api/threads/`
- `/api/threads/find`
- `/api/threads/sync`
- `/api/users/:id`
- `/api/v1`
- `/api/v2/`
- `/api/v2/spans`

## Related Service URLs Found

- `http://localhost:4318/`
- `http://localhost:9411/api/v2/spans`
- `https://aiplatform.googleapis.com/`
- `https://ampcode.com`
- `https://ampcode.com/`
- `https://ampcode.com/manual`
- `https://ampcode.com/manual/appendix`
- `https://ampcode.com/models`
- `https://ampcode.com/news/stick-a-fork-in-it`
- `https://ampcode.com/settings`
- `https://ampcode.com/threads/`
- `https://ampcode.com/threads/T-3f1beb2b-bded-4fda-96cc-1af7192f24b6`
- `https://ampcode.com/threads/T-5928a90d-d53b-488f-a829-4e36442142ee`
- `https://ampcode.com/threads/T-95e73a95-f4fe-4f22-8d5c-6297467c97a5`
- `https://ampcode.com/threads/T-f916b832-c070-4853-8ab3-5e7596953bec`
- `https://ampcode.com/threads/T-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`
- `https://api.anthropic.com`
- `https://api.anthropic.com/`
- `https://api.cerebras.ai`
- `https://api.openai.com/v1`
- `https://generativelanguage.googleapis.com`
- `https://generativelanguage.googleapis.com/`
- `https://openrouter.ai/api/v1`
- `https://storage.googleapis.com/amp-public-assets-prod-0/cli`
- `https://storage.googleapis.com/amp-public-assets-prod-0/cli/cli-version.txt`
- `https://storage.googleapis.com/amp-public-assets-prod-0/jetbrains/latest.json`
- `https://storage.googleapis.com/amp-public-assets-prod-0/ripgrep/ripgrep-binaries/`

## Notes

- Static string extraction can include dead code or SDK/internal paths.
- Use runtime logging/proxy capture to verify which endpoints are actually invoked in your environment.

```

## File: amp-extractions-latest\config\settings.md
```
# AMP CLI Settings Reference (Latest Binary)

- **Source binary:** `~/.amp/bin/amp`
- **Version:** `0.0.1773129970-gb3ab74 (released 2026-03-10T08:11:50.960Z, 2h ago)`
- **Extraction date:** 2026-03-10T11:04:01.398Z
- **Method:** `amp --help` + binary strings extraction of internal settings registry object `UE0`.

## Summary

- **Total registry settings:** 42
- **Visible/public settings:** 23
- **Internal/hidden settings:** 19

## Public Settings

| Key | Default | Description |
|---|---|---|
| `amp.agent.deepReasoningEffort` | `high` | Default GPT-5.3 Codex reasoning effort for new deep-mode threads (medium, high, xhigh). |
| `amp.bitbucketToken` | `undefined` | Personal access token for Bitbucket Enterprise. Used with a workspace-level Bitbucket connection configured by an admin. |
| `amp.dangerouslyAllowAll` | `false` | Disable all command confirmation prompts (agent will execute all commands without asking) |
| `amp.defaultVisibility` | `{"github.com/sourcegraph/amp":"workspace"}` | Define default thread visibility per repository origin using mappings like "github.com/org/repo": "workspace". Values: private, public, workspace, group. |
| `amp.experimental.modes` | `[]` | Enable experimental agent modes by name. Available modes: deep |
| `amp.fuzzy.alwaysIncludePaths` | `[]` | Glob patterns for paths that should always be included in fuzzy file search, even if gitignored |
| `amp.git.commit.ampThread.enabled` | `true` | Enable adding Amp-Thread trailer in git commits |
| `amp.git.commit.coauthor.enabled` | `true` | Enable adding Amp as co-author in git commits |
| `amp.guardedFiles.allowlist` | `[]` | Array of file glob patterns that are allowed to be accessed without confirmation. Takes precedence over the built-in denylist. |
| `amp.mcpServers` | `{"filesystem":{"command":"npx","args":["@modelcontextprotocol/server-filesystem","/path/to/allowed/dir"]}}` | Model Context Protocol servers to connect to for additional tools |
| `amp.network.timeout` | `30` | How many seconds to wait for network requests to the Amp server before timing out |
| `amp.notifications.enabled` | `true` | Enable system sound notifications when agent completes tasks |
| `amp.notifications.system.enabled` | `true` | Enable system notifications when terminal is not focused |
| `amp.permissions` | `[{"tool":"Bash","action":"ask","matches":{"cmd":["git push*","git commit*","git branch -D*","git checkout HEAD*"]}}]` | Permission rules for tool calls. See amp permissions --help |
| `amp.proxy` | `undefined` | Proxy URL used for both HTTP and HTTPS requests to the Amp server |
| `amp.showCosts` | `true` | Set to false to hide costs while working on a thread |
| `amp.skills.path` | `undefined` | Path to additional directories containing skills. Supports colon-separated paths (semicolon on Windows). Use ~ for home directory. |
| `amp.terminal.animation` | `true` | Set to false to disable terminal animations (or use the equivalent NO_ANIMATION=1 env var) |
| `amp.terminal.theme` | `terminal` | Color theme for the CLI. Built-in: terminal, dark, light, catppuccin-mocha, solarized-dark, solarized-light, gruvbox-dark-hard, nord. Custom themes: ~/.config/amp/themes/<name>/colors.toml |
| `amp.toolbox.path` | `undefined` | Path to the directory containing toolbox scripts. Supports colon-separated paths. |
| `amp.tools.disable` | `["browser_navigate","builtin:edit_file"]` | Array of tool names to disable. Use 'builtin:toolname' to disable only the builtin tool with that name (allowing an MCP server to provide a tool by that name). |
| `amp.tools.enable` | `undefined` | Array of tool name patterns to enable. Supports glob patterns (e.g., 'mcp__metabase__*'). If not set, all tools are enabled. If set, only matching tools are enabled. |
| `amp.updates.mode` | `auto` | Control update checking behavior: "warn" shows update notifications, "disabled" turns off checking, "auto" automatically runs update. |

## Internal/Hidden Settings

| Key | Default | Description |
|---|---|---|
| `amp.agent.skipTitleGenerationIfMessageContains` | `[]` | List of strings that, if present in a message, will skip title generation |
| `amp.anthropic.effort` | `high` | Effort level for Anthropic models that support auto-thinking (low, medium, high, max). Higher effort means more thinking and better performance. |
| `amp.anthropic.interleavedThinking.enabled` | `false` | Enable interleaved thinking for Claude 4 models (allows reasoning between tool calls) |
| `amp.anthropic.provider` | `anthropic` | Which provider to use for Anthropic Claude inference: "anthropic" or "vertex" |
| `amp.anthropic.speed` | `undefined` | Speed mode for Anthropic models (standard or fast) |
| `amp.anthropic.temperature` | `1` | Temperature setting for Anthropic models (0.0 = deterministic, 1.0 = creative). Note: Only takes effect when thinking is disabled. Internal use only. |
| `amp.anthropic.thinking.enabled` | `false` | Enable Claude thinking process output for debugging |
| `amp.debugLogs` | `false` | Enable debug logging output |
| `amp.experimental.cli.nativeSecretsStorage.enabled` | `false` | Use native secret storage instead of the plain-text secrets configuration file |
| `amp.experimental.tools` | `[]` | Enable experimental tools by name |
| `amp.gemini.thinkingLevel` | `undefined` | Thinking level for Gemini models (minimal, low, medium, high, or undefined) |
| `amp.hooks` | `[]` | Custom hooks for extending Amp functionality |
| `amp.jetbrains.skipInstall` | `false` | Skip JetBrains plugin installation |
| `amp.submitOnEnter` | `true` | Whether to submit messages on Enter (true) or require Ctrl+Enter (false) |
| `amp.systemPrompt` | `undefined` | Custom system prompt text to append (SDK use only) |
| `amp.terminal.commands.nodeSpawn.loadProfile` | `daily` | How often to load shell profile in node-spawn mode (always, daily, never) |
| `amp.tools.inactivityTimeout` | `300` | How many seconds of no output to wait before canceling bash commands |
| `amp.tools.stopTimeout` | `300` | Timeout for stopping tools |
| `amp.url` | `https://ampcode.com` | The Amp server URL to connect to |

## Raw Public Help Block

```text
amp.agent.deepReasoningEffort
      Default GPT-5.3 Codex reasoning effort for new deep-mode threads (medium, high, xhigh).
  amp.bitbucketToken
      Personal access token for Bitbucket Enterprise. Used with a workspace-level Bitbucket connection configured by an
      admin.
  amp.dangerouslyAllowAll
      Disable all command confirmation prompts (agent will execute all commands without asking)
  amp.defaultVisibility
      Define default thread visibility per repository origin using mappings like "github.com/org/repo": "workspace".
      Values: private, public, workspace, group.
  amp.experimental.modes
      Enable experimental agent modes by name. Available modes: deep
  amp.fuzzy.alwaysIncludePaths
      Glob patterns for paths that should always be included in fuzzy file search, even if gitignored
  amp.git.commit.ampThread.enabled
      Enable adding Amp-Thread trailer in git commits
  amp.git.commit.coauthor.enabled
      Enable adding Amp as co-author in git commits
  amp.guardedFiles.allowlist
      Array of file glob patterns that are allowed to be accessed without confirmation. Takes precedence over the
      built-in denylist.
  amp.mcpServers
      Model Context Protocol servers to connect to for additional tools
  amp.network.timeout
      How many seconds to wait for network requests to the Amp server before timing out
  amp.notifications.enabled
      Enable system sound notifications when agent completes tasks
  amp.notifications.system.enabled
      Enable system notifications when terminal is not focused
  amp.permissions
      Permission rules for tool calls. See amp permissions --help
  amp.proxy
      Proxy URL used for both HTTP and HTTPS requests to the Amp server
  amp.showCosts
      Set to false to hide costs while working on a thread
  amp.skills.path
      Path to additional directories containing skills. Supports colon-separated paths (semicolon on Windows). Use ~ for
      home directory.
  amp.terminal.animation
      Set to false to disable terminal animations (or use the equivalent NO_ANIMATION=1 env var)
  amp.terminal.theme
      Color theme for the CLI. Built-in: terminal, dark, light, catppuccin-mocha, solarized-dark, solarized-light,
      gruvbox-dark-hard, nord. Custom themes: ~/.config/amp/themes/<name>/colors.toml
  amp.toolbox.path
      Path to the directory containing toolbox scripts. Supports colon-separated paths.
  amp.tools.disable
      Array of tool names to disable. Use 'builtin:toolname' to disable only the builtin tool with that name (allowing
      an MCP server to provide a tool by that name).
  amp.tools.enable
      Array of tool name patterns to enable. Supports glob patterns (e.g., 'mcp__metabase__*'). If not set, all tools
      are enabled. If set, only matching tools are enabled.
  amp.updates.mode
      Control update checking behavior: "warn" shows update notifications, "disabled" turns off checking, "auto"
      automatically runs update.
```

```

## File: scripts\debug-openai.ts
```
/**
 * Mini diagnostic flow for OpenAI (Codex) provider.
 *
 * Step 1: Read token from credential store
 * Step 2: Refresh token if expired
 * Step 3: Call OpenAI API directly (bypass proxy)
 * Step 4: Call through the local proxy
 *
 * Usage: bun run scripts/debug-openai.ts [port]
 */

import { Database } from "bun:sqlite";
import { homedir } from "node:os";
import { join } from "node:path";

const port = process.argv[2] ?? "7860";
const CODEX_BASE_URL = "https://chatgpt.com/backend-api";
const OPENAI_TOKEN_URL = "https://auth.openai.com/oauth/token";
const CLIENT_ID = "app_EMoamEEZ73f0CkXaXp7hrann";
const JWT_CLAIM_PATH = "https://api.openai.com/auth";

const BODY = {
  model: "gpt-5.2",
  stream: true,
  store: false,
  instructions: "",
  input: [{ role: "user", content: "Say hello in one word." }],
};

// ── Helpers ──────────────────────────────────────────────────────────────────

function header(title: string) {
  console.log(`\n${"═".repeat(60)}`);
  console.log(`  ${title}`);
  console.log(`${"═".repeat(60)}`);
}

async function printResponse(label: string, response: Response) {
  console.log(`\n[${label}] Status: ${response.status} ${response.statusText}`);
  console.log(`[${label}] Headers:`);
  for (const [k, v] of response.headers.entries()) {
    if (["content-type", "x-request-id", "retry-after", "x-ratelimit-remaining-tokens"].includes(k)) {
      console.log(`  ${k}: ${v}`);
    }
  }
  const text = await response.text();
  console.log(`[${label}] Body (${text.length} bytes):`);
  try {
    console.log(JSON.stringify(JSON.parse(text), null, 2));
  } catch {
    console.log(text.slice(0, 500));
  }
  return text;
}

// ── Step 1: Read credentials from SQLite ─────────────────────────────────────

header("Step 1: Read Codex credentials from store");

const dbPath = join(homedir(), ".ampcode-connector", "credentials.db");
let db: Database;
try {
  db = new Database(dbPath, { readonly: true, strict: true });
} catch (err) {
  console.error(`✗ Cannot open credential DB at ${dbPath}: ${err}`);
  process.exit(1);
}

const rows = db.prepare<{ account: number; data: string }, [string]>(
  "SELECT account, data FROM credentials WHERE provider = ? ORDER BY account",
).all("codex");

if (rows.length === 0) {
  console.error("✗ No Codex credentials found. Run the login flow first.");
  process.exit(1);
}

for (const row of rows) {
  const creds = JSON.parse(row.data);
  const expiresIn = Math.round((creds.expiresAt - Date.now()) / 1000);
  const fresh = Date.now() < creds.expiresAt;
  console.log(`  account=${row.account}  fresh=${fresh}  expiresIn=${expiresIn}s  hasRefresh=${!!creds.refreshToken}`);
  console.log(`  accessToken=${creds.accessToken.slice(0, 20)}...`);
}

// ── Step 2: Refresh token if expired ─────────────────────────────────────────

header("Step 2: Ensure fresh access token");

const creds = JSON.parse(rows[0]!.data);
let accessToken: string = creds.accessToken;

if (Date.now() >= creds.expiresAt) {
  console.log("  Token expired, attempting refresh...");

  if (!creds.refreshToken) {
    console.error("  ✗ No refresh token available. Re-login required.");
    process.exit(1);
  }

  const refreshRes = await fetch(OPENAI_TOKEN_URL, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      grant_type: "refresh_token",
      refresh_token: creds.refreshToken,
      client_id: CLIENT_ID,
    }).toString(),
  });

  if (!refreshRes.ok) {
    const text = await refreshRes.text();
    console.error(`  ✗ Refresh failed (${refreshRes.status}): ${text}`);
    process.exit(1);
  }

  const refreshData = (await refreshRes.json()) as Record<string, unknown>;
  accessToken = refreshData.access_token as string;
  console.log(`  ✓ Refreshed! New token: ${accessToken.slice(0, 20)}...`);
  console.log(`  expires_in: ${refreshData.expires_in}s`);
} else {
  console.log(`  ✓ Token still fresh (${Math.round((creds.expiresAt - Date.now()) / 1000)}s remaining)`);
}

// ── Step 2b: Extract account ID from JWT ─────────────────────────────────────

let accountId: string | undefined;
try {
  const parts = accessToken.split(".");
  const payload = JSON.parse(Buffer.from(parts[1]!, "base64url").toString("utf-8"));
  accountId = payload[JWT_CLAIM_PATH]?.chatgpt_account_id;
  console.log(`  accountId: ${accountId ?? "(not found)"}`);
} catch {
  console.log("  ⚠ Could not decode JWT for account ID");
}

// ── Step 3: Call ChatGPT Codex backend directly (bypass proxy) ───────────────

header("Step 3: Call ChatGPT Codex backend directly (bypass proxy)");

const directUrl = `${CODEX_BASE_URL}/codex/responses`;
console.log(`  URL: ${directUrl}`);

const directRes = await fetch(directUrl, {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer ${accessToken}`,
    Accept: "text/event-stream",
    "OpenAI-Beta": "responses=experimental",
    "originator": "codex_cli_rs",
    "User-Agent": "codex_cli_rs/0.101.0 (debug-script)",
    "Version": "0.101.0",
    ...(accountId ? { "chatgpt-account-id": accountId } : {}),
  },
  body: JSON.stringify(BODY),
});

await printResponse("DIRECT", directRes);

// ── Step 4: Call through local proxy ─────────────────────────────────────────

header("Step 4: Call through local proxy");

const proxyUrl = `http://localhost:${port}/api/provider/openai/v1/responses`;

try {
  const proxyRes = await fetch(proxyUrl, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
    body: JSON.stringify(BODY),
  });

  await printResponse("PROXY", proxyRes);

  // ── Comparison ─────────────────────────────────────────────────────────────

  header("Diagnosis");

  if (directRes.ok && !proxyRes.ok) {
    console.log("  ⚠ Direct call succeeded but proxy failed.");
    console.log("  → The proxy is likely falling back to Amp upstream (token issue in proxy).");
    console.log("  → Check if the proxy refreshed the token or used an expired one.");
  } else if (directRes.ok && proxyRes.ok) {
    console.log("  ✓ Both direct and proxy calls succeeded. Everything works!");
  } else if (!directRes.ok && !proxyRes.ok) {
    console.log("  ✗ Both calls failed. OpenAI token or account may be invalid.");
  } else {
    console.log("  ? Unexpected: direct failed but proxy succeeded.");
  }
} catch (err) {
  console.error(`  ✗ Cannot reach proxy at ${proxyUrl}: ${err}`);
  console.log("  → Is the proxy running? Start with: bun start");
}

db.close();

```

## File: scripts\debug-oracle.ts
```
/**
 * Debug script: sends a mock oracle (OpenAI /responses) request to the local proxy
 * and prints raw status, headers, and body to diagnose "Out of Credits" errors.
 *
 * Usage: bun run scripts/debug-oracle.ts [port]
 */

const port = process.argv[2] ?? "7860";
const url = `http://localhost:${port}/api/provider/openai/v1/responses`;

const body = {
  model: "gpt-5.2",
  stream: false,
  input: [{ role: "user", content: "Say hello in one word." }],
};

console.log(`\n>>> POST ${url}`);
console.log(`>>> Body: ${JSON.stringify(body, null, 2)}\n`);

const start = Date.now();
const response = await fetch(url, {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
  body: JSON.stringify(body),
});
const elapsed = Date.now() - start;

console.log(`<<< Status: ${response.status} ${response.statusText}`);
console.log(`<<< Duration: ${elapsed}ms`);
console.log(`<<< Headers:`);
for (const [key, value] of response.headers.entries()) {
  console.log(`<<<   ${key}: ${value}`);
}

const text = await response.text();
console.log(`\n<<< Body (${text.length} bytes):`);
try {
  console.log(JSON.stringify(JSON.parse(text), null, 2));
} catch {
  console.log(text);
}

```

## File: src\constants.ts
```
/** Single source of truth — no magic strings scattered across files. */

export const CODE_ASSIST_ENDPOINT = "https://cloudcode-pa.googleapis.com";
export const ANTIGRAVITY_DAILY_ENDPOINT = "https://daily-cloudcode-pa.googleapis.com";
export const ANTIGRAVITY_DAILY_SANDBOX_ENDPOINT = "https://daily-cloudcode-pa.sandbox.googleapis.com";
export const AUTOPUSH_ENDPOINT = "https://autopush-cloudcode-pa.sandbox.googleapis.com";
export const DEFAULT_ANTIGRAVITY_PROJECT = "rising-fact-p41fc";

export const ANTHROPIC_API_URL = "https://api.anthropic.com";
export const CODEX_BASE_URL = "https://chatgpt.com/backend-api";

/** Codex-specific headers required by the ChatGPT backend. */
export const codexHeaders = {
  BETA: "OpenAI-Beta",
  ACCOUNT_ID: "chatgpt-account-id",
  ORIGINATOR: "originator",
  SESSION_ID: "session_id",
  CONVERSATION_ID: "conversation_id",
} as const;

export const CODEX_CLI_VERSION = "0.101.0";

export const codexHeaderValues = {
  BETA_RESPONSES: "responses=experimental",
  ORIGINATOR: "codex_cli_rs",
  VERSION: CODEX_CLI_VERSION,
  USER_AGENT: `codex_cli_rs/${CODEX_CLI_VERSION} (${process.platform} ${process.arch})`,
} as const;

/** Map Amp CLI paths → ChatGPT backend paths.
 *  Both /v1/responses and /v1/chat/completions route to /codex/responses. */
export const codexPathMap: Record<string, string> = {
  "/v1/responses": "/codex/responses",
  "/v1/chat/completions": "/codex/responses",
} as const;
export const DEFAULT_AMP_UPSTREAM_URL = "https://ampcode.com";

export const ANTHROPIC_TOKEN_URL = "https://platform.claude.com/v1/oauth/token";
export const OPENAI_TOKEN_URL = "https://auth.openai.com/oauth/token";
export const GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token";

export const TOKEN_EXPIRY_BUFFER_MS = 5 * 60 * 1000;
export const CLAUDE_CODE_VERSION = "2.1.77";

export const claudeCodeBetas = [
  "claude-code-20250219",
  "oauth-2025-04-20",
  "interleaved-thinking-2025-05-14",
  "context-management-2025-06-27",
  "prompt-caching-scope-2026-01-05",
] as const;

export const filteredBetaFeatures = ["fast-mode-2026-02-01"] as const;

export const modelFieldPaths = [
  "model",
  "message.model",
  "modelVersion",
  "response.model",
  "response.modelVersion",
] as const;

export const passthroughPrefixes = [
  "/api/internal",
  "/api/user",
  "/api/auth",
  "/api/meta",
  "/api/ads",
  "/api/telemetry",
  "/api/threads",
  "/api/otel",
  "/api/tab",
  "/api/durable-thread-workers",
] as const;

/** Browser routes — redirect to ampcode.com (auth cookies need correct domain). */
export const browserPrefixes = ["/auth", "/threads", "/docs", "/settings"] as const;

export const passthroughExact = ["/threads.rss", "/news.rss"] as const;

```

## File: src\index.ts
```
#!/usr/bin/env bun
/** ampcode-connector entry point. */

import { startAutoRefresh } from "./auth/auto-refresh.ts";
import * as configs from "./auth/configs.ts";
import type { OAuthConfig } from "./auth/oauth.ts";
import * as oauth from "./auth/oauth.ts";
import { bannerAd } from "./cli/ads.ts";
import { line, s } from "./cli/ansi.ts";
import { setup } from "./cli/setup.ts";
import * as status from "./cli/status.ts";
import { dashboard } from "./cli/tui.ts";
import { loadConfig, type ProxyConfig } from "./config/config.ts";
import { startServer } from "./server/server.ts";
import { logger, setLogLevel } from "./utils/logger.ts";

const providers: Record<string, OAuthConfig> = {
  anthropic: configs.anthropic,
  codex: configs.codex,
  google: configs.google,
};

async function main(): Promise<void> {
  const [command, arg] = process.argv.slice(2);

  if (command === "setup") return setup();

  if (command === "login") {
    if (!arg) return dashboard();

    const config = providers[arg];
    if (!config) {
      logger.error(`Unknown provider: ${arg}. Available: ${Object.keys(providers).join(", ")}`);
      process.exit(1);
    }
    await oauth.login(config);
    return;
  }

  if (command === "help" || command === "--help" || command === "-h") {
    usage();
    return;
  }

  const config = await loadConfig();
  setLogLevel(config.logLevel);
  startServer(config);
  startAutoRefresh();
  banner(config);

  // Non-blocking update check — runs in background after server starts
  const { checkForUpdates } = await import("./utils/update-check.ts");
  checkForUpdates();
}

function banner(config: ProxyConfig): void {
  const providers = status.all();
  const upstream = config.ampUpstreamUrl.replace(/^https?:\/\//, "");

  line();
  line(`  ${s.bold}ampcode-connector${s.reset}`);
  line(`  ${s.dim}http://${config.hostname}:${config.port}${s.reset}`);
  line();

  for (const p of providers) {
    const count = p.accounts.length;
    const label = p.label.padEnd(16);
    const countStr = count > 0 ? `${count} account${count > 1 ? "s" : ""}` : "--";
    const dot = count > 0 ? `${s.green}●${s.reset}` : `${s.dim}○${s.reset}`;
    line(`  ${label}  ${countStr.padEnd(12)}${dot}`);
  }

  line();
  line(`  ${s.dim}upstream → ${upstream}${s.reset}`);
  line();
  bannerAd();
  line();
}

function usage(): void {
  line();
  line(`${s.bold}ampcode-connector${s.reset} ${s.dim}— proxy Amp CLI through local OAuth subscriptions${s.reset}`);
  line();
  line(`${s.bold}USAGE${s.reset}`);
  line(`  ${s.cyan}bun start${s.reset}              Start the proxy server`);
  line(`  ${s.cyan}bun run setup${s.reset}          Configure Amp CLI to use this proxy`);
  line(`  ${s.cyan}bun run login${s.reset}          Interactive login dashboard`);
  line(`  ${s.cyan}bun run login <p>${s.reset}      Login to a specific provider`);
  line();
  line(`${s.bold}PROVIDERS${s.reset}`);
  line(`  anthropic     Claude Code ${s.dim}(Anthropic models)${s.reset}`);
  line(`  codex         OpenAI Codex ${s.dim}(GPT/o3 models)${s.reset}`);
  line(`  google        Google ${s.dim}(Gemini CLI + Antigravity, dual quota)${s.reset}`);
  line();
  line(`${s.bold}CONFIG${s.reset}`);
  line(`  Edit ${s.cyan}config.yaml${s.reset} to customize port, providers, and log level.`);
  line();
}

main().catch((err) => {
  logger.error("Fatal", { error: String(err) });
  process.exit(1);
});

```

## File: src\auth\auto-refresh.ts
```
import { TOKEN_EXPIRY_BUFFER_MS } from "../constants.ts";
import { logger } from "../utils/logger.ts";
import * as configs from "./configs.ts";
import type { OAuthConfig } from "./oauth.ts";
import * as oauth from "./oauth.ts";
import { getAll, type ProviderName } from "./store.ts";

const REFRESH_INTERVAL_MS = 60_000;

const providerConfigs: Record<ProviderName, OAuthConfig> = {
  anthropic: configs.anthropic,
  codex: configs.codex,
  google: configs.google,
};

let timer: Timer | null = null;

async function refreshAll(): Promise<void> {
  const now = Date.now();

  for (const [provider, config] of Object.entries(providerConfigs) as [ProviderName, OAuthConfig][]) {
    for (const { account, credentials } of getAll(provider)) {
      if (credentials.expiresAt - now > TOKEN_EXPIRY_BUFFER_MS) continue;

      try {
        logger.debug("Auto-refreshing token", { provider, account });
        await oauth.token(config, account);
      } catch (err) {
        logger.error("Auto-refresh failed", { provider, account, error: String(err) });
      }
    }
  }
}

export function startAutoRefresh(): void {
  if (timer) return;
  timer = setInterval(refreshAll, REFRESH_INTERVAL_MS);
}

export function stopAutoRefresh(): void {
  if (!timer) return;
  clearInterval(timer);
  timer = null;
}

```

## File: src\auth\callback-server.ts
```
/** Temporary localhost HTTP server to receive OAuth callbacks. */

import { logger } from "../utils/logger.ts";

interface CallbackResult {
  code: string;
  state: string;
}

const DEFAULT_TIMEOUT = 120_000;

export async function waitForCallback(
  preferredPort: number,
  callbackPath: string,
  expectedState: string,
  timeout: number = DEFAULT_TIMEOUT,
): Promise<CallbackResult> {
  return new Promise((resolve, reject) => {
    let server: ReturnType<typeof Bun.serve> | null = null;
    let timeoutId: Timer | null = null;

    const cleanup = () => {
      if (timeoutId) clearTimeout(timeoutId);
      if (server) {
        server.stop(true);
        server = null;
      }
    };

    timeoutId = setTimeout(() => {
      cleanup();
      reject(new Error(`OAuth callback timed out after ${timeout}ms`));
    }, timeout);

    try {
      server = Bun.serve({
        port: preferredPort,
        hostname: "localhost",
        fetch(req) {
          const url = new URL(req.url);
          if (url.pathname !== callbackPath) return new Response("Not found", { status: 404 });

          const code = url.searchParams.get("code");
          const state = url.searchParams.get("state");
          const error = url.searchParams.get("error");
          const errorDescription = url.searchParams.get("error_description");

          if (error) {
            cleanup();
            reject(new Error(`OAuth error: ${error} - ${errorDescription ?? "unknown"}`));
            return htmlPage("Authentication Failed", `Error: ${error}. ${errorDescription ?? ""}`);
          }

          if (!code || !state) {
            cleanup();
            reject(new Error("Missing code or state in OAuth callback"));
            return htmlPage("Authentication Failed", "Missing authorization code.");
          }

          if (state !== expectedState) {
            cleanup();
            reject(new Error("State mismatch in OAuth callback (possible CSRF)"));
            return htmlPage("Authentication Failed", "State validation failed.");
          }

          cleanup();
          resolve({ code, state });
          return htmlPage("Authentication Successful", "You can close this window and return to the terminal.");
        },
      });

      logger.debug("Callback server started", { provider: `port:${preferredPort}` });
    } catch (err) {
      cleanup();
      reject(new Error(`Failed to start callback server on port ${preferredPort}: ${err}`));
    }
  });
}

function htmlPage(title: string, message: string): Response {
  const body = `<!DOCTYPE html>
<html>
<head><title>${title}</title></head>
<body style="font-family: system-ui; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0;">
  <div style="text-align: center;">
    <h1>${title}</h1>
    <p>${message}</p>
  </div>
</body>
</html>`;
  return new Response(body, { headers: { "Content-Type": "text/html" } });
}

```

## File: src\auth\configs.ts
```
import { ANTHROPIC_TOKEN_URL, GOOGLE_TOKEN_URL, OPENAI_TOKEN_URL } from "../constants.ts";
import { discoverAnthropic, discoverCodex, discoverGoogle } from "./discovery.ts";
import type { OAuthConfig } from "./oauth.ts";

export const anthropic: OAuthConfig = {
  providerName: "anthropic",
  clientId: "9d1c250a-e61b-44d9-88ed-5944d1962f5e",
  authorizeUrl: "https://claude.ai/oauth/authorize",
  tokenUrl: ANTHROPIC_TOKEN_URL,
  callbackPort: 54545,
  callbackPath: "/callback",
  scopes: "org:create_api_key user:profile user:inference user:sessions:claude_code user:mcp_servers user:file_upload",
  bodyFormat: "json",
  expiryBuffer: true,
  sendStateInExchange: true,
  authorizeExtra: { code: "true" },
  extractIdentity: discoverAnthropic,
};

export const codex: OAuthConfig = {
  providerName: "codex",
  clientId: "app_EMoamEEZ73f0CkXaXp7hrann",
  authorizeUrl: "https://auth.openai.com/oauth/authorize",
  tokenUrl: OPENAI_TOKEN_URL,
  callbackPort: 1455,
  callbackPath: "/auth/callback",
  scopes: "openid profile email offline_access",
  bodyFormat: "form",
  expiryBuffer: true,
  authorizeExtra: {
    id_token_add_organizations: "true",
    codex_cli_simplified_flow: "true",
    originator: "opencode",
  },
  extractIdentity: discoverCodex,
};

export const google: OAuthConfig = {
  providerName: "google",
  clientId: "1071006060591-tmhssin2h21lcre235vtolojh4g403ep.apps.googleusercontent.com",
  clientSecret: "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",
  authorizeUrl: "https://accounts.google.com/o/oauth2/v2/auth",
  tokenUrl: GOOGLE_TOKEN_URL,
  callbackPort: 51121,
  callbackPath: "/oauth-callback",
  scopes: [
    "https://www.googleapis.com/auth/cloud-platform",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "https://www.googleapis.com/auth/cclog",
    "https://www.googleapis.com/auth/experimentsandconfigs",
  ].join(" "),
  bodyFormat: "form",
  expiryBuffer: true,
  authorizeExtra: { access_type: "offline", prompt: "consent" },
  extractIdentity: discoverGoogle,
};

```

## File: src\auth\discovery.ts
```
import {
  ANTIGRAVITY_DAILY_ENDPOINT,
  AUTOPUSH_ENDPOINT,
  CODE_ASSIST_ENDPOINT,
  DEFAULT_ANTIGRAVITY_PROJECT,
} from "../constants.ts";
import { fromBase64url } from "../utils/encoding.ts";
import { logger } from "../utils/logger.ts";
import type { Credentials } from "./store.ts";

type Raw = Record<string, unknown>;

export async function discoverAnthropic(raw: Raw): Promise<Partial<Credentials>> {
  const account = raw.account as { uuid?: string; email_address?: string } | undefined;
  return {
    ...(account?.email_address ? { email: account.email_address } : {}),
    ...(account?.uuid ? { accountId: account.uuid } : {}),
  };
}

export async function discoverCodex(raw: Raw): Promise<Partial<Credentials>> {
  const accessToken = raw.access_token as string;
  const accountId = accountIdFromJWT(accessToken);
  const email = await fetchEmail("https://api.openai.com/v1/me", accessToken);
  return {
    ...(accountId ? { accountId } : {}),
    ...(email ? { email } : {}),
  };
}

export async function discoverGoogle(raw: Raw): Promise<Partial<Credentials>> {
  const accessToken = raw.access_token as string;
  const email = await fetchEmail("https://www.googleapis.com/oauth2/v1/userinfo?alt=json", accessToken);
  const projectId = await findProject(accessToken);
  return { ...(email ? { email } : {}), ...(projectId ? { projectId } : {}) };
}

function accountIdFromJWT(token: string): string | null {
  try {
    const parts = token.split(".");
    if (parts.length < 2 || !parts[1]) return null;
    const payload = JSON.parse(new TextDecoder().decode(fromBase64url(parts[1]))) as Raw;
    const auth = payload["https://api.openai.com/auth"] as Raw | undefined;
    return (auth?.chatgpt_account_id as string) ?? null;
  } catch {
    return null;
  }
}

async function fetchEmail(url: string, accessToken: string): Promise<string | undefined> {
  try {
    const res = await fetch(url, { headers: { Authorization: `Bearer ${accessToken}` } });
    if (!res.ok) return undefined;
    return ((await res.json()) as { email?: string }).email;
  } catch {
    return undefined;
  }
}

const CCA_HEADERS = {
  "Content-Type": "application/json",
  "User-Agent": "google-api-nodejs-client/9.15.1",
  "X-Goog-Api-Client": "google-cloud-sdk vscode_cloudshelleditor/0.1",
  "Client-Metadata": JSON.stringify({
    ideType: "IDE_UNSPECIFIED",
    platform: "PLATFORM_UNSPECIFIED",
    pluginType: "GEMINI",
  }),
} as const;

const CCA_BODY = JSON.stringify({
  metadata: { ideType: "IDE_UNSPECIFIED", platform: "PLATFORM_UNSPECIFIED", pluginType: "GEMINI" },
});

async function findProject(accessToken: string): Promise<string | undefined> {
  for (const endpoint of [CODE_ASSIST_ENDPOINT, ANTIGRAVITY_DAILY_ENDPOINT, AUTOPUSH_ENDPOINT]) {
    try {
      const res = await fetch(`${endpoint}/v1internal:loadCodeAssist`, {
        method: "POST",
        headers: { ...CCA_HEADERS, Authorization: `Bearer ${accessToken}` },
        body: CCA_BODY,
      });

      if (!res.ok) {
        logger.debug(`loadCodeAssist ${res.status} at ${endpoint}`);
        continue;
      }

      const body = (await res.json()) as { cloudaicompanionProject?: string | { id?: string } };
      const proj = body.cloudaicompanionProject;
      const id = typeof proj === "string" ? proj : proj?.id;
      if (id) return id;
    } catch (err) {
      logger.debug(`loadCodeAssist error at ${endpoint}`, { error: String(err) });
    }
  }

  logger.warn(`Project discovery failed, using fallback: ${DEFAULT_ANTIGRAVITY_PROJECT}`);
  return DEFAULT_ANTIGRAVITY_PROJECT;
}

```

## File: src\auth\oauth.ts
```
import { TOKEN_EXPIRY_BUFFER_MS } from "../constants.ts";
import * as browser from "../utils/browser.ts";
import { logger } from "../utils/logger.ts";
import { waitForCallback } from "./callback-server.ts";
import { generatePKCE, generateState } from "./pkce.ts";
import type { Credentials, ProviderName } from "./store.ts";
import * as store from "./store.ts";

export interface OAuthConfig {
  providerName: ProviderName;
  clientId: string;
  clientSecret?: string;
  authorizeUrl: string;
  tokenUrl: string;
  callbackPort: number;
  callbackPath: string;
  scopes: string;
  bodyFormat: "json" | "form";
  authorizeExtra?: Record<string, string>;
  expiryBuffer?: boolean;
  sendStateInExchange?: boolean;
  extractIdentity?: (raw: Record<string, unknown>) => Promise<Partial<Credentials>>;
}

export async function token(config: OAuthConfig, account = 0): Promise<string | null> {
  const creds = store.get(config.providerName, account);

  if (!creds) {
    try {
      return (await serialize(config)).accessToken;
    } catch (err) {
      logger.error(`Auto-login failed for ${config.providerName}`, { error: String(err) });
      return null;
    }
  }

  if (store.fresh(creds)) return creds.accessToken;

  const refreshed = await refreshWithRetry(config, creds.refreshToken, account);
  return refreshed?.accessToken ?? null;
}

export async function tokenFromAny(config: OAuthConfig): Promise<{ accessToken: string; account: number } | null> {
  for (const { account, credentials: c } of store.getAll(config.providerName)) {
    if (store.fresh(c)) return { accessToken: c.accessToken, account };
  }

  for (const { account, credentials: c } of store.getAll(config.providerName)) {
    if (!c.refreshToken) continue;
    try {
      const refreshed = await refresh(config, c.refreshToken, account);
      return { accessToken: refreshed.accessToken, account };
    } catch (err) {
      handleRefreshFailure(config, account, err);
      logger.debug(`${config.providerName}:${account} refresh failed in tokenFromAny`, { error: String(err) });
    }
  }

  return null;
}

export function ready(config: OAuthConfig): boolean {
  return store.exists(config.providerName);
}

export function accountCount(config: OAuthConfig): number {
  return store.count(config.providerName);
}

export async function login(config: OAuthConfig): Promise<Credentials> {
  const { verifier, challenge } = await generatePKCE();
  const state = generateState();
  const redirectUri = `http://localhost:${config.callbackPort}${config.callbackPath}`;

  const authUrl = new URL(config.authorizeUrl);
  const q = authUrl.searchParams;
  q.set("client_id", config.clientId);
  q.set("response_type", "code");
  q.set("redirect_uri", redirectUri);
  q.set("scope", config.scopes);
  q.set("code_challenge", challenge);
  q.set("code_challenge_method", "S256");
  q.set("state", state);
  if (config.authorizeExtra) {
    for (const [k, v] of Object.entries(config.authorizeExtra)) q.set(k, v);
  }

  logger.info(`Opening browser for ${config.providerName} OAuth...`);
  if (!(await browser.open(authUrl.toString()))) {
    logger.warn("Could not open browser. Please open this URL manually:");
    logger.info(authUrl.toString());
  }

  const callback = await waitForCallback(config.callbackPort, config.callbackPath, state);

  const exchangeParams: Record<string, string> = {
    grant_type: "authorization_code",
    code: callback.code,
    redirect_uri: redirectUri,
    code_verifier: verifier,
  };
  if (config.sendStateInExchange) exchangeParams.state = callback.state;

  const raw = await exchange(config, exchangeParams);
  let credentials = parseTokenFields(raw, config);

  if (config.extractIdentity) {
    try {
      credentials = { ...credentials, ...(await config.extractIdentity(raw)) };
    } catch (err) {
      logger.error(`${config.providerName} identity extraction failed`, { error: String(err) });
    }
  }

  const existing = store.findByIdentity(config.providerName, credentials);
  const account = existing ?? store.nextAccount(config.providerName);

  if (!credentials.refreshToken) {
    credentials.refreshToken = store.get(config.providerName, account)?.refreshToken ?? "";
  }
  if (!credentials.refreshToken) {
    throw new Error(`No refresh token for ${config.providerName}. Revoke app access and try again.`);
  }

  store.save(config.providerName, credentials, account);
  logger.info(`${config.providerName}:${account} ${existing !== null ? "updated" : "added"}`);
  return credentials;
}

const loginLocks = new Map<ProviderName, Promise<Credentials>>();

function serialize(config: OAuthConfig): Promise<Credentials> {
  const pending = loginLocks.get(config.providerName);
  if (pending) return pending;

  const promise = login(config).finally(() => loginLocks.delete(config.providerName));
  loginLocks.set(config.providerName, promise);
  return promise;
}

async function refresh(config: OAuthConfig, refreshToken: string, account = 0): Promise<Credentials> {
  const raw = await exchange(config, { grant_type: "refresh_token", refresh_token: refreshToken });

  const credentials: Credentials = {
    ...store.get(config.providerName, account),
    ...parseTokenFields(raw, config),
    refreshToken: (raw.refresh_token as string) ?? refreshToken,
  };

  store.save(config.providerName, credentials, account);
  return credentials;
}

async function refreshWithRetry(
  config: OAuthConfig,
  refreshToken: string,
  account: number,
): Promise<Credentials | null> {
  try {
    return await refresh(config, refreshToken, account);
  } catch (err) {
    if (handleRefreshFailure(config, account, err)) return null;

    logger.warn(`Token refresh failed for ${config.providerName}:${account}, retrying...`, { error: String(err) });

    try {
      await Bun.sleep(1000);
      return await refresh(config, refreshToken, account);
    } catch (retryErr) {
      handleRefreshFailure(config, account, retryErr);
      logger.error(`Token refresh retry failed for ${config.providerName}:${account}`, { error: String(retryErr) });
      return null;
    }
  }
}

async function exchange(config: OAuthConfig, params: Record<string, string>): Promise<Record<string, unknown>> {
  const all: Record<string, string> = { client_id: config.clientId, ...params };
  if (config.clientSecret) all.client_secret = config.clientSecret;

  const isJson = config.bodyFormat === "json";
  const res = await fetch(config.tokenUrl, {
    method: "POST",
    headers: { "Content-Type": isJson ? "application/json" : "application/x-www-form-urlencoded" },
    body: isJson ? JSON.stringify(all) : new URLSearchParams(all).toString(),
  });

  if (!res.ok) {
    const text = await res.text();
    const oauthError = parseOAuthError(text);
    throw new TokenExchangeError(config.providerName, res.status, text, oauthError.code, oauthError.description);
  }

  return (await res.json()) as Record<string, unknown>;
}

class TokenExchangeError extends Error {
  readonly status: number;
  readonly responseBody: string;
  readonly errorCode: string | null;
  readonly errorDescription: string | null;

  constructor(
    providerName: string,
    status: number,
    responseBody: string,
    errorCode: string | null,
    errorDescription: string | null,
  ) {
    super(`${providerName} token exchange failed (${status}): ${responseBody}`);
    this.name = "TokenExchangeError";
    this.status = status;
    this.responseBody = responseBody;
    this.errorCode = errorCode;
    this.errorDescription = errorDescription;
  }
}

function parseOAuthError(responseBody: string): { code: string | null; description: string | null } {
  try {
    const parsed = JSON.parse(responseBody) as { error?: unknown; error_description?: unknown };
    const code = typeof parsed.error === "string" ? parsed.error : null;
    const description = typeof parsed.error_description === "string" ? parsed.error_description : null;
    return { code, description };
  } catch {
    return { code: null, description: null };
  }
}

/** Handles terminal refresh failures and returns true when retry should stop. */
function handleRefreshFailure(config: OAuthConfig, account: number, err: unknown): boolean {
  if (!isInvalidRefreshTokenError(err)) return false;
  if (!store.get(config.providerName, account)) return false;

  store.remove(config.providerName, account);
  logger.warn(`Removed invalid refresh token for ${config.providerName}:${account}; re-login required.`, {
    error: String(err),
  });
  return true;
}

function isInvalidRefreshTokenError(err: unknown): boolean {
  if (!(err instanceof TokenExchangeError)) return false;
  if (err.status !== 400 && err.status !== 401) return false;

  if (err.errorCode === "invalid_grant") return true;

  const description = err.errorDescription?.toLowerCase() ?? "";
  const hasRefreshTokenContext = description.includes("refresh token");
  const indicatesInvalidState =
    description.includes("invalid") ||
    description.includes("not found") ||
    description.includes("expired") ||
    description.includes("revoked");

  if (hasRefreshTokenContext && indicatesInvalidState) return true;

  const body = err.responseBody.toLowerCase();
  return (
    body.includes("invalid_grant") ||
    body.includes("invalid refresh token") ||
    body.includes("refresh token not found") ||
    body.includes("refresh token is invalid")
  );
}

function parseTokenFields(raw: Record<string, unknown>, config: OAuthConfig): Credentials {
  if (typeof raw.access_token !== "string" || !raw.access_token) {
    throw new Error(`${config.providerName} token response missing access_token`);
  }
  if (typeof raw.expires_in !== "number" || Number.isNaN(raw.expires_in)) {
    throw new Error(`${config.providerName} token response missing or invalid expires_in`);
  }
  const buffer = config.expiryBuffer !== false ? TOKEN_EXPIRY_BUFFER_MS : 0;
  return {
    accessToken: raw.access_token,
    refreshToken: (raw.refresh_token as string) ?? "",
    expiresAt: Date.now() + raw.expires_in * 1000 - buffer,
  };
}

```

## File: src\auth\pkce.ts
```
/** PKCE (Proof Key for Code Exchange) — S256 challenge for all OAuth flows. */

import { toBase64url } from "../utils/encoding.ts";

export async function generatePKCE(): Promise<{ verifier: string; challenge: string }> {
  const verifierBytes = new Uint8Array(96);
  crypto.getRandomValues(verifierBytes);
  const verifier = toBase64url(verifierBytes);

  const hashBuffer = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(verifier));
  const challenge = toBase64url(new Uint8Array(hashBuffer));

  return { verifier, challenge };
}

export function generateState(): string {
  const bytes = new Uint8Array(16);
  crypto.getRandomValues(bytes);
  return Array.from(bytes)
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");
}

```

## File: src\auth\store.ts
```
/** SQLite credential storage at ~/.ampcode-connector/credentials.db
 *  Multi-account: composite key (provider, account).
 *  Sync API via bun:sqlite — no cache needed at 0.4µs/read. */

import { Database, type Statement } from "bun:sqlite";
import { mkdirSync } from "node:fs";
import { homedir } from "node:os";
import { join } from "node:path";
import { logger } from "../utils/logger.ts";

export interface Credentials {
  accessToken: string;
  refreshToken: string;
  expiresAt: number;
  projectId?: string;
  email?: string;
  accountId?: string;
}

export type ProviderName = "anthropic" | "codex" | "google";

const DEFAULT_DIR = join(homedir(), ".ampcode-connector");
const DEFAULT_DB_PATH = join(DEFAULT_DIR, "credentials.db");

interface DataRow {
  data: string;
}
interface AccountDataRow {
  account: number;
  data: string;
}
interface MaxAccountRow {
  max_account: number | null;
}
interface CountRow {
  cnt: number;
}

interface Statements {
  get: Statement<DataRow, [string, number]>;
  getAll: Statement<AccountDataRow, [string]>;
  set: Statement<void, [string, number, string]>;
  delOne: Statement<void, [string, number]>;
  delAll: Statement<void, [string]>;
  maxAccount: Statement<MaxAccountRow, [string]>;
  count: Statement<CountRow, [string]>;
}

let _db: Database | null = null;
let _stmts: Statements | null = null;
const _dbPath = DEFAULT_DB_PATH;
function init() {
  if (_stmts) return _stmts;

  const dir = _dbPath.replace(/\/[^/]+$/, "");
  mkdirSync(dir, { recursive: true, mode: 0o700 });
  _db = new Database(_dbPath, { strict: true });
  _db.exec("PRAGMA journal_mode=WAL");
  _db.exec("PRAGMA busy_timeout=5000");
  _db.exec(`
    CREATE TABLE IF NOT EXISTS credentials (
      provider TEXT NOT NULL,
      account  INTEGER NOT NULL DEFAULT 0,
      data     TEXT NOT NULL,
      PRIMARY KEY (provider, account)
    )
  `);

  _stmts = {
    get: _db.prepare<DataRow, [string, number]>("SELECT data FROM credentials WHERE provider = ? AND account = ?"),
    getAll: _db.prepare<AccountDataRow, [string]>(
      "SELECT account, data FROM credentials WHERE provider = ? ORDER BY account",
    ),
    set: _db.prepare<void, [string, number, string]>(
      "INSERT OR REPLACE INTO credentials (provider, account, data) VALUES (?, ?, ?)",
    ),
    delOne: _db.prepare<void, [string, number]>("DELETE FROM credentials WHERE provider = ? AND account = ?"),
    delAll: _db.prepare<void, [string]>("DELETE FROM credentials WHERE provider = ?"),
    maxAccount: _db.prepare<MaxAccountRow, [string]>(
      "SELECT MAX(account) as max_account FROM credentials WHERE provider = ?",
    ),
    count: _db.prepare<CountRow, [string]>("SELECT COUNT(*) as cnt FROM credentials WHERE provider = ?"),
  };
  return _stmts;
}

export function get(provider: ProviderName, account = 0): Credentials | undefined {
  const row = init().get.get(provider, account);
  if (!row) return undefined;
  try {
    return JSON.parse(row.data) as Credentials;
  } catch (err) {
    logger.warn(`Corrupt credentials for ${provider}:${account}, removing`, { error: String(err) });
    init().delOne.run(provider, account);
    return undefined;
  }
}

export function getAll(provider: ProviderName): { account: number; credentials: Credentials }[] {
  const results: { account: number; credentials: Credentials }[] = [];
  for (const row of init().getAll.all(provider)) {
    try {
      results.push({ account: row.account, credentials: JSON.parse(row.data) as Credentials });
    } catch (err) {
      logger.warn(`Corrupt credentials for ${provider}:${row.account}, removing`, { error: String(err) });
      init().delOne.run(provider, row.account);
    }
  }
  return results;
}

export function save(provider: ProviderName, credentials: Credentials, account = 0): void {
  init().set.run(provider, account, JSON.stringify(credentials));
}

export function remove(provider: ProviderName, account?: number): void {
  if (account !== undefined) {
    init().delOne.run(provider, account);
  } else {
    init().delAll.run(provider);
  }
}

export function nextAccount(provider: ProviderName): number {
  const row = init().maxAccount.get(provider);
  return (row?.max_account ?? -1) + 1;
}

export function count(provider: ProviderName): number {
  return init().count.get(provider)?.cnt ?? 0;
}

/** Find existing account by email or accountId match. */
export function findByIdentity(provider: ProviderName, credentials: Credentials): number | null {
  const all = getAll(provider);
  for (const entry of all) {
    if (credentials.email && entry.credentials.email === credentials.email) return entry.account;
    if (credentials.accountId && entry.credentials.accountId === credentials.accountId) return entry.account;
  }
  return null;
}

export function exists(provider: ProviderName): boolean {
  const all = getAll(provider);
  return all.some((e) => !!e.credentials.refreshToken);
}

export function fresh(credentials: Credentials): boolean {
  return Date.now() < credentials.expiresAt;
}

```

## File: src\cli\ads.ts
```
/** Periodic GitHub star reminder — non-intrusive, shows in server logs. */

import { line, s } from "../cli/ansi.ts";

const REPO_URL = "https://github.com/nghyane/ampcode-connector";
const REQUEST_INTERVAL = 50;

let requestCount = 0;
let shown = false;

const messages = [
  `${s.yellow}⭐${s.reset} Enjoying ampcode-connector? Star us on GitHub → ${s.cyan}${REPO_URL}${s.reset}`,
  `${s.yellow}⭐${s.reset} Help others discover this tool — star on GitHub → ${s.cyan}${REPO_URL}${s.reset}`,
  `${s.yellow}⭐${s.reset} ${s.dim}Your star helps keep this project alive!${s.reset} → ${s.cyan}${REPO_URL}${s.reset}`,
];

function pick(): string {
  return messages[Math.floor(Math.random() * messages.length)]!;
}

/** Show star prompt in the startup banner (once). */
export function bannerAd(): void {
  line(`  ${s.dim}⭐ Star us → ${REPO_URL}${s.reset}`);
}

/** Call after each proxied request. Shows a reminder every N requests. */
export function maybeShowAd(): void {
  requestCount++;
  if (requestCount % REQUEST_INTERVAL !== 0) return;

  // Only show once per interval, don't spam
  if (shown && requestCount < REQUEST_INTERVAL * 3) return;
  shown = true;

  line();
  line(`  ${pick()}`);
  line();
}

```

## File: src\cli\ansi.ts
```
/** Raw ANSI escape helpers — no dependencies. */

const ESC = "\x1b[";

export const cursor = {
  hide: () => out(`${ESC}?25l`),
  show: () => out(`${ESC}?25h`),
  home: () => out(`${ESC}H`),
};

export const screen = {
  clear: () => out(`${ESC}2J${ESC}H`),
};

/** Erase from cursor to end of line. */
const eol = `${ESC}K`;

export const s = {
  reset: `${ESC}0m`,
  bold: `${ESC}1m`,
  dim: `${ESC}2m`,
  inverse: `${ESC}7m`,
  green: `${ESC}32m`,
  red: `${ESC}31m`,
  yellow: `${ESC}33m`,
  gray: `${ESC}90m`,
  cyan: `${ESC}36m`,
  white: `${ESC}37m`,
};

export function out(text: string): void {
  process.stdout.write(text);
}

export function line(text = ""): void {
  process.stdout.write(`${text}${eol}\n`);
}

```

## File: src\cli\setup.ts
```
/** Auto-configure Amp CLI to route through ampcode-connector. */

import { existsSync, lstatSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { homedir } from "node:os";
import { dirname, join } from "node:path";
import { loadConfig } from "../config/config.ts";
import { line, out, s } from "./ansi.ts";
import * as status from "./status.ts";

const AMP_SECRETS_DIR = join(homedir(), ".local", "share", "amp");
const AMP_SECRETS_PATH = join(AMP_SECRETS_DIR, "secrets.json");

const AMP_SETTINGS_PATH = join(homedir(), ".config", "amp", "settings.json");
const AMP_LEGACY_SETTINGS_PATH = join(homedir(), ".amp", "settings.json");

function ampSettingsPath(): string {
  const envPath = process.env.AMP_SETTINGS_FILE;
  return envPath || AMP_SETTINGS_PATH;
}

function warnLegacySettingsFile(): void {
  if (process.env.AMP_SETTINGS_FILE || !existsSync(AMP_LEGACY_SETTINGS_PATH)) return;
  try {
    if (lstatSync(AMP_LEGACY_SETTINGS_PATH).isSymbolicLink()) return;
  } catch {
    return;
  }

  line(
    `${s.yellow}!${s.reset} Legacy settings file detected at ${s.dim}${AMP_LEGACY_SETTINGS_PATH}${s.reset}. ` +
      `Prefer a single source of truth at ${s.dim}${AMP_SETTINGS_PATH}${s.reset}.`,
  );
}

function readJson(path: string): Record<string, unknown> {
  if (!existsSync(path)) return {};
  try {
    return JSON.parse(readFileSync(path, "utf-8")) as Record<string, unknown>;
  } catch {
    return {};
  }
}

function writeJson(path: string, data: Record<string, unknown>): void {
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, `${JSON.stringify(data, null, 2)}\n`, "utf-8");
}

function findAmpApiKey(proxyUrl: string): string | undefined {
  if (process.env.AMP_API_KEY) return process.env.AMP_API_KEY;

  const secrets = readJson(AMP_SECRETS_PATH);
  const exact = secrets[`apiKey@${proxyUrl}`];
  if (typeof exact === "string" && exact.length > 0) return exact;

  for (const value of Object.values(secrets)) {
    if (typeof value === "string" && value.startsWith("sgamp_")) return value;
  }
  return undefined;
}

/** Save key under proxy URL and migrate stale entries to keep secrets.json clean. */
function saveAmpApiKey(token: string, proxyUrl: string): void {
  const secrets = readJson(AMP_SECRETS_PATH);
  for (const key of Object.keys(secrets)) {
    if (key.startsWith("apiKey")) delete secrets[key];
  }
  secrets[`apiKey@${proxyUrl}`] = token;
  mkdirSync(AMP_SECRETS_DIR, { recursive: true, mode: 0o700 });
  writeJson(AMP_SECRETS_PATH, secrets);
}

function prompt(question: string): Promise<string> {
  return new Promise((resolve) => {
    out(question);
    const chunks: string[] = [];

    const onData = (data: Buffer) => {
      const str = data.toString();
      if (str.includes("\n") || str.includes("\r")) {
        process.stdin.removeListener("data", onData);
        process.stdin.pause();
        resolve(chunks.join("").trim());
        return;
      }
      chunks.push(str);
    };

    process.stdin.resume();
    process.stdin.setEncoding("utf-8");
    process.stdin.on("data", onData);
  });
}

export async function setup(): Promise<void> {
  const config = await loadConfig();
  const proxyUrl = `http://localhost:${config.port}`;

  line();
  line(`${s.bold}ampcode-connector setup${s.reset}`);
  line();

  // Step 1: Configure amp.url in canonical settings file
  const settingsPath = ampSettingsPath();
  const settings = readJson(settingsPath);
  if (settings["amp.url"] !== proxyUrl) {
    settings["amp.url"] = proxyUrl;
    writeJson(settingsPath, settings);
  }
  line(`${s.green}ok${s.reset} amp.url = ${s.cyan}${proxyUrl}${s.reset}  ${s.dim}${settingsPath}${s.reset}`);
  warnLegacySettingsFile();

  // Step 2: Amp API key
  const existingKey = findAmpApiKey(proxyUrl);

  if (existingKey) {
    saveAmpApiKey(existingKey, proxyUrl);
    const preview = `${existingKey.slice(0, 10)}...`;
    line(`${s.green}ok${s.reset} Amp token found  ${s.dim}${preview}${s.reset}`);
  } else {
    line();
    line(`${s.yellow}!${s.reset}  No Amp token found.`);
    line(`   Get one from ${s.cyan}https://ampcode.com/settings${s.reset}`);
    line(`   Or run ${s.cyan}amp login${s.reset} after starting the proxy.`);
    line();

    const token = await prompt(`   Paste token (or press Enter to skip): `);
    line();

    if (token) {
      saveAmpApiKey(token, proxyUrl);
      line(`${s.green}ok${s.reset} Token saved  ${s.dim}${AMP_SECRETS_PATH}${s.reset}`);
    } else {
      line(`${s.dim}-- skipped${s.reset}`);
    }
  }

  // Step 3: Provider status
  line();
  line(`${s.bold}Providers${s.reset}`);

  const providers = status.all();
  let hasAny = false;

  for (const p of providers) {
    const connected = p.accounts.filter((a) => a.status === "connected");
    const disabled = p.accounts.filter((a) => a.status === "disabled");
    const total = p.accounts.filter((a) => a.status !== "disconnected");

    if (connected.length > 0) {
      hasAny = true;
      const emails = connected
        .map((a) => a.email)
        .filter(Boolean)
        .join(", ");
      const info = emails ? `  ${s.dim}${emails}${s.reset}` : "";
      const disabledInfo = disabled.length > 0 ? `  ${s.red}${disabled.length} disabled${s.reset}` : "";
      line(`  ${p.label.padEnd(16)} ${s.green}${connected.length} account(s)${s.reset}${info}${disabledInfo}`);
    } else if (disabled.length > 0) {
      line(`  ${p.label.padEnd(16)} ${s.red}${disabled.length} disabled${s.reset}`);
    } else if (total.length > 0) {
      line(`  ${p.label.padEnd(16)} ${s.yellow}${total.length} expired${s.reset}`);
    } else {
      line(`  ${p.label.padEnd(16)} ${s.dim}--${s.reset}`);
    }
  }

  if (!hasAny) {
    line();
    line(`  Run ${s.cyan}bun run login${s.reset} to authenticate providers.`);
  }

  // Summary
  line();
  line(`${s.bold}Next${s.reset}`);
  line(`  ${s.cyan}bun start${s.reset}       Start proxy`);
  if (!existingKey) {
    line(`  ${s.cyan}amp login${s.reset}       Authenticate with ampcode.com (proxy must be running)`);
  }
  line(`  ${s.cyan}amp "hello"${s.reset}     Test`);
  line();
}

```

## File: src\cli\status.ts
```
import type { Credentials, ProviderName } from "../auth/store.ts";
import * as store from "../auth/store.ts";
import { cooldown, type QuotaPool } from "../routing/cooldown.ts";

export type ConnectionStatus = "connected" | "expired" | "disabled" | "disconnected";

export interface AccountStatus {
  account: number;
  status: ConnectionStatus;
  email?: string;
  expiresAt?: number;
}

export interface ProviderStatus {
  name: ProviderName;
  label: string;
  sublabel?: string;
  accounts: AccountStatus[];
}

const PROVIDERS: { name: ProviderName; label: string; sublabel?: string }[] = [
  { name: "anthropic", label: "Claude Code" },
  { name: "codex", label: "OpenAI Codex" },
  { name: "google", label: "Google" },
];

const POOL_MAP: Record<ProviderName, QuotaPool[]> = {
  anthropic: ["anthropic"],
  codex: ["codex"],
  google: ["google"],
};

function connectionOf(name: ProviderName, account: number, creds: Credentials): ConnectionStatus {
  if (!creds.refreshToken) return "disconnected";
  const pools = POOL_MAP[name];
  if (pools.some((p) => cooldown.isExhausted(p, account))) return "disabled";
  return store.fresh(creds) ? "connected" : "expired";
}

export function all(): ProviderStatus[] {
  return PROVIDERS.map(({ name, label, sublabel }) => ({
    name,
    label,
    sublabel,
    accounts: store.getAll(name).map((e) => ({
      account: e.account,
      status: connectionOf(name, e.account, e.credentials),
      email: e.credentials.email,
      expiresAt: e.credentials.expiresAt,
    })),
  }));
}

export function remaining(expiresAt: number): string {
  const diff = expiresAt - Date.now();
  if (diff <= 0) return "expired";
  const mins = Math.floor(diff / 60_000);
  const hrs = Math.floor(mins / 60);
  if (hrs > 0) return `${hrs}h ${mins % 60}m`;
  return `${mins}m`;
}

```

## File: src\cli\tui.ts
```
import * as configs from "../auth/configs.ts";
import type { OAuthConfig } from "../auth/oauth.ts";
import * as oauth from "../auth/oauth.ts";
import type { ProviderName } from "../auth/store.ts";
import * as store from "../auth/store.ts";
import { cursor, line, s, screen } from "./ansi.ts";
import type { AccountStatus, ConnectionStatus, ProviderStatus } from "./status.ts";
import * as status from "./status.ts";

const oauthConfigs: Record<ProviderName, OAuthConfig> = {
  anthropic: configs.anthropic,
  codex: configs.codex,
  google: configs.google,
};

const ICON: Record<ConnectionStatus, string> = {
  connected: `${s.green}●${s.reset}`,
  expired: `${s.yellow}●${s.reset}`,
  disabled: `${s.red}●${s.reset}`,
  disconnected: `${s.dim}○${s.reset}`,
};

type Item =
  | { type: "provider"; provider: ProviderStatus }
  | { type: "account"; provider: ProviderStatus; account: AccountStatus };

let selected = 0;
let items: Item[] = [];
let message = "";
let busy = false;
let timer: Timer | null = null;

export function dashboard(): void {
  if (!process.stdin.isTTY) throw new Error("Interactive dashboard requires a TTY.");

  rebuild();
  process.stdin.setRawMode(true);
  process.stdin.resume();
  process.stdin.setEncoding("utf8");
  cursor.hide();
  screen.clear();
  render();
  timer = setInterval(render, 1_000);
  process.stdin.on("data", onKey);
  process.on("exit", cleanup);
  process.on("SIGINT", () => process.exit());
  process.on("SIGTERM", () => process.exit());
}

function rebuild(): void {
  items = [];
  for (const p of status.all()) {
    items.push({ type: "provider", provider: p });
    for (const a of p.accounts) items.push({ type: "account", provider: p, account: a });
  }
  if (selected >= items.length) selected = Math.max(0, items.length - 1);
}

function cleanup(): void {
  if (timer) clearInterval(timer);
  cursor.show();
  screen.clear();
}

function render(): void {
  cursor.home();
  line(`${s.bold} ampcode-connector${s.reset}`);
  line(`${s.dim} ↑↓ navigate · enter login/add · d disconnect · q quit${s.reset}`);
  line();

  for (let i = 0; i < items.length; i++) {
    const item = items[i]!;
    const sel = i === selected;

    if (item.type === "provider") {
      renderProvider(item.provider, sel);
    } else {
      renderAccount(item.account, sel);
    }
  }

  line();
  if (busy) line(`${s.cyan}   ⟳ waiting for browser…${s.reset}`);
  else if (message) line(`   ${message}`);
  else line();
}

function renderProvider(p: ProviderStatus, sel: boolean): void {
  const n = p.accounts.length;
  const connected = p.accounts.filter((a) => a.status === "connected").length;
  const suffix = n > 0 ? ` ${s.dim}(${connected}/${n})${s.reset}` : "";
  const label = p.label.padEnd(16);

  if (sel) line(`${s.inverse} › ${s.bold}${label}${s.reset}${s.inverse}${suffix} ${s.reset}`);
  else line(`   ${s.bold}${label}${s.reset}${suffix}`);

  if (p.sublabel) line(`     ${s.dim}${p.sublabel}${s.reset}`);
}

function renderAccount(a: AccountStatus, sel: boolean): void {
  const ic = ICON[a.status];
  const tag = `#${a.account}`.padEnd(4);
  const info = formatInfo(a);

  if (sel) line(`${s.inverse}     ${ic} ${tag} ${info} ${s.reset}`);
  else line(`     ${ic} ${s.dim}${tag}${s.reset} ${info}`);
}

function formatInfo(a: AccountStatus): string {
  if (a.status === "disconnected") return `${s.dim}—${s.reset}`;

  const parts: string[] = [];
  if (a.status === "connected") parts.push(`${s.green}connected${s.reset}`);
  else if (a.status === "disabled") parts.push(`${s.red}disabled${s.reset}`);
  else parts.push(`${s.yellow}expired${s.reset}`);
  if (a.expiresAt && a.status === "connected") parts.push(`${s.dim}${status.remaining(a.expiresAt)}${s.reset}`);
  if (a.email) parts.push(`${s.dim}${a.email}${s.reset}`);
  return parts.join(`${s.dim} · ${s.reset}`);
}

async function onKey(data: string): Promise<void> {
  if (busy) return;

  if (data === "\x03" || data === "q") return void process.exit();
  if (data === "\x1b[A") {
    selected = Math.max(0, selected - 1);
    render();
    return;
  }
  if (data === "\x1b[B") {
    selected = Math.min(items.length - 1, selected + 1);
    render();
    return;
  }

  if (data === "\r" || data === "\n") {
    const item = items[selected]!;
    await doLogin(item.provider);
    return;
  }

  if (data === "d" || data === "D") {
    const item = items[selected]!;
    if (item.type === "account") doDisconnect(item.provider, item.account.account);
    else doDisconnectAll(item.provider);
    return;
  }
}

async function doLogin(p: ProviderStatus): Promise<void> {
  busy = true;
  message = "";
  render();

  try {
    const creds = await oauth.login(oauthConfigs[p.name]);
    message = `${s.green}✓ ${p.label} ${creds.email ?? "account"} logged in${s.reset}`;
  } catch (err) {
    message = `${s.red}✗ ${err instanceof Error ? err.message : String(err)}${s.reset}`;
  }

  rebuild();
  busy = false;
  render();
}

function doDisconnect(p: ProviderStatus, account: number): void {
  store.remove(p.name, account);
  message = `${s.yellow}✗ ${p.label} #${account} disconnected${s.reset}`;
  rebuild();
  render();
}

function doDisconnectAll(p: ProviderStatus): void {
  if (p.accounts.length === 0) return;
  store.remove(p.name);
  message = `${s.yellow}✗ ${p.label} all disconnected${s.reset}`;
  rebuild();
  render();
}

```

## File: src\config\config.ts
```
/** YAML config loader with env/file fallback for API key. */

import { homedir } from "node:os";
import { join } from "node:path";
import { DEFAULT_AMP_UPSTREAM_URL } from "../constants.ts";
import type { LogLevel } from "../utils/logger.ts";
import { logger } from "../utils/logger.ts";

export interface ProxyConfig {
  hostname: string;
  port: number;
  ampUpstreamUrl: string;
  ampApiKey?: string;
  exaApiKey?: string;
  logLevel: LogLevel;
  providers: {
    anthropic: boolean;
    codex: boolean;
    google: boolean;
  };
}

const DEFAULTS: ProxyConfig = {
  hostname: "localhost",
  port: 8765,
  ampUpstreamUrl: DEFAULT_AMP_UPSTREAM_URL,
  logLevel: "info",
  providers: { anthropic: true, codex: true, google: true },
};

/** Config search order: cwd → ~/.config/ampcode-connector */
const CONFIG_PATHS = [
  join(process.cwd(), "config.yaml"),
  join(homedir(), ".config", "ampcode-connector", "config.yaml"),
];
const SECRETS_PATH = join(homedir(), ".local", "share", "amp", "secrets.json");

export async function loadConfig(): Promise<ProxyConfig> {
  const file = await readConfigFile();
  const apiKey = await resolveApiKey(file);
  const providers = asRecord(file?.providers);

  const port = asNumber(file?.port) ?? DEFAULTS.port;
  if (port < 1 || port > 65535) {
    throw new Error(`Invalid port ${port}: must be between 1 and 65535`);
  }

  return {
    hostname: asString(file?.hostname) ?? process.env.HOST ?? DEFAULTS.hostname,
    port,
    ampUpstreamUrl: asString(file?.ampUpstreamUrl) ?? DEFAULTS.ampUpstreamUrl,
    ampApiKey: apiKey,
    exaApiKey: asString(file?.exaApiKey) ?? process.env.EXA_API_KEY,
    logLevel: asLogLevel(file?.logLevel) ?? DEFAULTS.logLevel,
    providers: {
      anthropic: asBool(providers?.anthropic) ?? DEFAULTS.providers.anthropic,
      codex: asBool(providers?.codex) ?? DEFAULTS.providers.codex,
      google: asBool(providers?.google) ?? DEFAULTS.providers.google,
    },
  };
}

async function readConfigFile(): Promise<Record<string, unknown> | null> {
  for (const configPath of CONFIG_PATHS) {
    const file = Bun.file(configPath);
    if (await file.exists()) {
      try {
        const text = await file.text();
        logger.info(`Loaded config from ${configPath}`);
        return Bun.YAML.parse(text) as Record<string, unknown>;
      } catch (err) {
        throw new Error(`Invalid config at ${configPath}: ${err}`);
      }
    }
  }
  return null;
}

/** Amp API key resolution: config file → AMP_API_KEY env → secrets.json */
async function resolveApiKey(file: Record<string, unknown> | null): Promise<string | undefined> {
  const fromFile = asString(file?.ampApiKey);
  if (fromFile) return fromFile;

  const fromEnv = process.env.AMP_API_KEY;
  if (fromEnv) return fromEnv;

  return readSecretsFile();
}

async function readSecretsFile(): Promise<string | undefined> {
  const file = Bun.file(SECRETS_PATH);
  if (!(await file.exists())) return undefined;
  try {
    const secrets = (await file.json()) as Record<string, unknown>;
    const canonical = asString(secrets[`apiKey@${DEFAULT_AMP_UPSTREAM_URL}/`]);
    if (canonical) return canonical;
    for (const value of Object.values(secrets)) {
      if (typeof value === "string" && value.startsWith("sgamp_")) return value;
    }
    return undefined;
  } catch (err) {
    logger.warn("Failed to read secrets.json", { error: String(err) });
    return undefined;
  }
}

function asRecord(v: unknown): Record<string, unknown> | undefined {
  return v != null && typeof v === "object" && !Array.isArray(v) ? (v as Record<string, unknown>) : undefined;
}

function asNumber(v: unknown): number | undefined {
  return typeof v === "number" && !Number.isNaN(v) ? v : undefined;
}

function asString(v: unknown): string | undefined {
  return typeof v === "string" && v.length > 0 ? v : undefined;
}

function asBool(v: unknown): boolean | undefined {
  return typeof v === "boolean" ? v : undefined;
}

const VALID_LOG_LEVELS = new Set<string>(["debug", "info", "warn", "error"]);

function asLogLevel(v: unknown): LogLevel | undefined {
  return typeof v === "string" && VALID_LOG_LEVELS.has(v) ? (v as LogLevel) : undefined;
}

```

## File: src\providers\anthropic.ts
```
/** Forwards requests to api.anthropic.com with Claude Code stealth headers. */

import { createHash } from "node:crypto";
import { anthropic as config } from "../auth/configs.ts";
import * as oauth from "../auth/oauth.ts";
import * as store from "../auth/store.ts";
import { ANTHROPIC_API_URL, CLAUDE_CODE_VERSION, claudeCodeBetas, filteredBetaFeatures } from "../constants.ts";
import type { ParsedBody } from "../server/body.ts";
import type { Provider } from "./base.ts";
import { denied, forward } from "./forward.ts";

/** Headers to drop from client request (replaced by connector or irrelevant). */
const DROP_HEADERS = new Set(["host", "content-length", "connection", "x-api-key", "authorization", "anthropic-beta"]);

/** Extract X-Stainless-* and other passthrough headers from the client request. */
function passthroughHeaders(originalHeaders: Headers): Record<string, string> {
  const out: Record<string, string> = {};
  for (const [k, v] of originalHeaders.entries()) {
    if (DROP_HEADERS.has(k)) continue;
    // Drop amp-specific headers
    if (k.startsWith("x-amp-")) continue;
    out[k] = v;
  }
  return out;
}

export const provider: Provider = {
  name: "Anthropic",
  routeDecision: "LOCAL_CLAUDE",

  isAvailable: (account?: number) =>
    account !== undefined ? !!store.get("anthropic", account)?.refreshToken : oauth.ready(config),

  accountCount: () => oauth.accountCount(config),

  async forward(sub, body, originalHeaders, rewrite, account = 0) {
    const accessToken = await oauth.token(config, account);
    if (!accessToken) return denied("Anthropic");

    const fwdBody = prepareBody(body);
    const betaHdr = betaHeader(originalHeaders.get("anthropic-beta"));
    const clientHeaders = passthroughHeaders(originalHeaders);

    return forward({
      url: `${ANTHROPIC_API_URL}${sub}`,
      body: fwdBody,
      streaming: body.stream,
      providerName: "Anthropic",
      rewrite,
      email: store.get("anthropic", account)?.email,
      headers: {
        // Client headers first (stainless, accept, content-type, anthropic-version, etc.)
        ...clientHeaders,
        // Override auth + identity
        "Anthropic-Dangerous-Direct-Browser-Access": "true",
        "Anthropic-Beta": betaHdr,
        "User-Agent": `claude-cli/${CLAUDE_CODE_VERSION} (external, cli)`,
        "X-App": "cli",
        Authorization: `Bearer ${accessToken}`,
      },
    });
  },
};

const BILLING_SALT = "59cf53e54c78";

/** Compute the cch checksum from the first user message text and version. */
function computeCch(firstUserText: string, version: string): string {
  const chars = [4, 7, 20].map((i) => firstUserText[i] || "0").join("");
  return createHash("sha256").update(`${BILLING_SALT}${chars}${version}`).digest("hex").slice(0, 5);
}

/** Extract text from the first user message in the body. */
function firstUserText(parsed: Record<string, unknown>): string {
  const messages = parsed.messages as Array<{ role?: string; content?: unknown }> | undefined;
  if (!Array.isArray(messages)) return "";
  const userMsg = messages.find((m) => m.role === "user");
  if (!userMsg) return "";
  if (typeof userMsg.content === "string") return userMsg.content;
  if (Array.isArray(userMsg.content)) {
    const textBlock = userMsg.content.find((b: { type?: string }) => b.type === "text") as
      | { text?: string }
      | undefined;
    return textBlock?.text ?? "";
  }
  return "";
}

/** Prepare body: inject billing header + strip speed field.
 *  Always re-injects billing header because cch depends on per-request message content.
 *  Shallow-copies parsed to avoid mutating the shared ParsedBody.parsed reference. */
function prepareBody(body: ParsedBody): string {
  const raw = body.forwardBody;

  try {
    const original = body.parsed;
    if (!original) return raw;

    const text = firstUserText(original);
    const cch = computeCch(text, CLAUDE_CODE_VERSION);
    const billingLine = `x-anthropic-billing-header: cc_version=${CLAUDE_CODE_VERSION}; cc_entrypoint=cli; cch=${cch};`;

    const { speed: _, system: existingSystem, ...rest } = original;

    return JSON.stringify({
      ...rest,
      system: injectBillingHeader(existingSystem, billingLine),
    });
  } catch {
    return raw;
  }
}

/** Prepend the billing header into the system prompt, handling both array and string formats. */
function injectBillingHeader(system: unknown, billingLine: string): unknown {
  if (Array.isArray(system)) {
    const filtered = system.filter(
      (s: { text?: string }) => !(typeof s.text === "string" && s.text.includes("x-anthropic-billing-header")),
    );
    return [{ type: "text", text: billingLine }, ...filtered];
  }
  if (typeof system === "string") {
    return `${billingLine}\n${system.replace(/x-anthropic-billing-header:[^\n]*\n?/, "")}`;
  }
  return [{ type: "text", text: billingLine }];
}

function betaHeader(original: string | null): string {
  const features = new Set<string>(claudeCodeBetas);

  if (original) {
    for (const raw of original.split(",")) {
      const feature = raw.trim();
      if (feature && !filteredBetaFeatures.includes(feature as (typeof filteredBetaFeatures)[number])) {
        features.add(feature);
      }
    }
  }

  return Array.from(features).join(",");
}

```

## File: src\providers\base.ts
```
/** Provider interface — the contract every provider must implement. */

import type { ParsedBody } from "../server/body.ts";
import type { RouteDecision } from "../utils/logger.ts";

export interface Provider {
  readonly name: string;
  readonly routeDecision: RouteDecision;
  isAvailable(account?: number): boolean;
  accountCount(): number;
  forward(
    path: string,
    body: ParsedBody,
    headers: Headers,
    rewrite?: (data: string) => string,
    account?: number,
  ): Promise<Response>;
}

```

## File: src\providers\codex-sse.ts
```
/** Transforms Responses API SSE events → Chat Completions SSE chunks.
 *
 *  Codex backend returns Responses API format (response.output_text.delta, etc.)
 *  but Amp CLI expects Chat Completions format (chat.completion.chunk). */

import * as sse from "../utils/streaming.ts";

interface CompletionChunk {
  id: string;
  object: "chat.completion.chunk";
  created: number;
  model: string;
  choices: Choice[];
  usage?: Usage | null;
}

interface Choice {
  index: number;
  delta: Delta;
  finish_reason: string | null;
}

interface Delta {
  role?: string;
  content?: string;
  reasoning_content?: string;
  tool_calls?: ToolCallDelta[];
}

interface ToolCallDelta {
  index: number;
  id?: string;
  type?: string;
  function?: { name?: string; arguments?: string };
}

interface Usage {
  prompt_tokens: number;
  completion_tokens: number;
  total_tokens: number;
  prompt_tokens_details?: { cached_tokens: number };
  completion_tokens_details?: { reasoning_tokens: number };
}

interface TransformState {
  responseId: string;
  model: string;
  created: number;
  toolCallIndex: number;
  /** Track active tool call IDs to assign sequential indices. */
  toolCallIds: Map<string, number>;
}

/** Resolve tool call index from item_id or call_id, falling back to 0. */
function lookupToolIndex(state: TransformState, itemId?: string, callId?: string): number {
  if (itemId) {
    const idx = state.toolCallIds.get(itemId);
    if (idx !== undefined) return idx;
  }
  if (callId) {
    const idx = state.toolCallIds.get(callId);
    if (idx !== undefined) return idx;
  }
  return 0;
}

/** Create a stateful SSE transformer: Responses API → Chat Completions. */
function createResponseTransformer(ampModel: string): (data: string) => string {
  const state: TransformState = {
    responseId: "",
    model: ampModel,
    created: Math.floor(Date.now() / 1000),
    toolCallIndex: 0,
    toolCallIds: new Map(),
  };

  return (data: string): string => {
    if (data === "[DONE]") return "";

    let parsed: Record<string, unknown>;
    try {
      parsed = JSON.parse(data) as Record<string, unknown>;
    } catch {
      return data;
    }

    const eventType = parsed.type as string | undefined;
    if (!eventType) return data;

    // Extract response metadata on creation
    if (eventType === "response.created") {
      const resp = parsed.response as Record<string, unknown>;
      state.responseId = (resp?.id as string) ?? state.responseId;
      state.model = ampModel;
      state.created = (resp?.created_at as number) ?? state.created;
      // Don't emit a chunk for response.created
      return "";
    }

    switch (eventType) {
      // Assistant message started — emit role
      case "response.output_item.added": {
        const item = parsed.item as Record<string, unknown>;
        if (item?.type === "message" && item.role === "assistant") {
          return serialize(state, { role: "assistant", content: "" });
        }
        if (item?.type === "function_call") {
          const callId = item.call_id as string;
          const itemId = item.id as string | undefined;
          const name = item.name as string;
          const idx = state.toolCallIndex++;
          state.toolCallIds.set(callId, idx);
          if (itemId) state.toolCallIds.set(itemId, idx);
          return serialize(state, {
            tool_calls: [{ index: idx, id: callId, type: "function", function: { name, arguments: "" } }],
          });
        }
        return "";
      }

      // Text content delta
      case "response.output_text.delta": {
        const delta = parsed.delta as string;
        if (delta) return serialize(state, { content: delta });
        return "";
      }

      // Function call arguments delta
      case "response.function_call_arguments.delta": {
        const delta = parsed.delta as string;
        const itemId = parsed.item_id as string | undefined;
        const callId = parsed.call_id as string | undefined;
        if (delta) {
          const idx = lookupToolIndex(state, itemId, callId);
          return serialize(state, { tool_calls: [{ index: idx, function: { arguments: delta } }] });
        }
        return "";
      }

      // Response completed — emit finish_reason + usage
      case "response.completed": {
        const resp = parsed.response as Record<string, unknown>;
        const usage = extractUsage(resp?.usage as Record<string, unknown> | undefined);
        const hasToolCalls = state.toolCallIndex > 0;
        const finishReason = hasToolCalls ? "tool_calls" : "stop";
        return serializeFinish(state, finishReason, usage);
      }

      // Response incomplete — inspect reason to determine finish_reason
      case "response.incomplete": {
        const resp = parsed.response as Record<string, unknown>;
        const usage = extractUsage(resp?.usage as Record<string, unknown> | undefined);
        const finishReason = incompleteReason(resp);
        return serializeFinish(state, finishReason, usage);
      }

      // Response failed — emit error content so the client sees the failure
      case "response.failed": {
        const resp = parsed.response as Record<string, unknown>;
        const usage = extractUsage(resp?.usage as Record<string, unknown> | undefined);
        const errorMsg = extractErrorMessage(resp);
        let chunks = "";
        if (errorMsg) {
          chunks = serialize(state, { role: "assistant", content: `[Error] ${errorMsg}` });
          chunks += "\n\n";
        }
        chunks += serializeFinish(state, "stop", usage);
        return chunks;
      }

      // Reasoning/thinking delta — emit as reasoning_content (separate from content)
      case "response.reasoning_summary_text.delta": {
        const delta = parsed.delta as string;
        if (delta) return serialize(state, { reasoning_content: delta });
        return "";
      }

      // Events we can skip
      case "response.in_progress":
      case "response.output_item.done":
      case "response.content_part.added":
      case "response.content_part.done":
      case "response.output_text.done":
      case "response.function_call_arguments.done":
      case "response.reasoning_summary_part.added":
      case "response.reasoning_summary_part.done":
        return "";

      default:
        return "";
    }
  };
}

function serialize(state: TransformState, delta: Delta): string {
  const chunk: CompletionChunk = {
    id: `chatcmpl-${state.responseId}`,
    object: "chat.completion.chunk",
    created: state.created,
    model: state.model,
    choices: [{ index: 0, delta, finish_reason: null }],
  };
  return JSON.stringify(chunk);
}

function serializeFinish(state: TransformState, finishReason: string, usage?: Usage): string {
  const chunk: CompletionChunk = {
    id: `chatcmpl-${state.responseId}`,
    object: "chat.completion.chunk",
    created: state.created,
    model: state.model,
    choices: [{ index: 0, delta: {}, finish_reason: finishReason }],
    ...(usage ? { usage } : {}),
  };
  return JSON.stringify(chunk);
}

/** Map Responses API incomplete reason → Chat Completions finish_reason. */
function incompleteReason(resp: Record<string, unknown> | undefined): string {
  if (!resp) return "length";
  const reason = resp.incomplete_details as Record<string, unknown> | undefined;
  const type = reason?.reason as string | undefined;
  if (type === "max_output_tokens" || type === "max_tokens") return "length";
  if (type === "content_filter") return "content_filter";
  return "length";
}

/** Extract a human-readable error message from a failed response. */
function extractErrorMessage(resp: Record<string, unknown> | undefined): string | null {
  if (!resp) return null;
  const error = resp.error as Record<string, unknown> | undefined;
  if (!error) return null;
  const message = error.message as string | undefined;
  const code = error.code as string | undefined;
  if (message) return code ? `${code}: ${message}` : message;
  if (code) return code;
  return null;
}

function extractUsage(raw: Record<string, unknown> | undefined): Usage | undefined {
  if (!raw) return undefined;
  const input = (raw.input_tokens as number) ?? 0;
  const output = (raw.output_tokens as number) ?? 0;
  const cached = (raw.input_tokens_details as Record<string, unknown>)?.cached_tokens as number | undefined;
  const reasoning = (raw.output_tokens_details as Record<string, unknown>)?.reasoning_tokens as number | undefined;
  return {
    prompt_tokens: input,
    completion_tokens: output,
    total_tokens: input + output,
    ...(cached !== undefined ? { prompt_tokens_details: { cached_tokens: cached } } : {}),
    ...(reasoning !== undefined ? { completion_tokens_details: { reasoning_tokens: reasoning } } : {}),
  };
}

const FORWARDED_HEADERS = [
  "x-request-id",
  "request-id",
  "x-ratelimit-limit-requests",
  "x-ratelimit-remaining-requests",
  "x-ratelimit-limit-tokens",
  "x-ratelimit-remaining-tokens",
] as const;

/** Wrap a Codex SSE response with the Responses → Chat Completions transformer.
 *  Strips Responses API event names so output looks like standard Chat Completions SSE. */
export function transformCodexResponse(response: Response, ampModel: string): Response {
  if (!response.body) return response;

  const transformer = createResponseTransformer(ampModel);
  const body = transformStream(response.body, transformer);

  const headers: Record<string, string> = {
    "Content-Type": "text/event-stream",
    "Cache-Control": "no-cache",
    Connection: "keep-alive",
  };
  for (const name of FORWARDED_HEADERS) {
    const value = response.headers.get(name);
    if (value) headers[name] = value;
  }

  return new Response(body, { status: response.status, headers });
}

/** Buffer a Codex SSE response into a single Chat Completions JSON response.
 *  Used when the client requests stream: false but the backend forces streaming. */
export async function bufferCodexResponse(response: Response, ampModel: string): Promise<Response> {
  if (!response.body) return response;

  const state: TransformState = {
    responseId: "",
    model: ampModel,
    created: Math.floor(Date.now() / 1000),
    toolCallIndex: 0,
    toolCallIds: new Map(),
  };

  let content = "";
  let reasoningContent = "";
  const toolCalls: Map<number, { id: string; type: string; function: { name: string; arguments: string } }> = new Map();
  let finishReason = "stop";
  let usage: Usage | undefined;

  const decoder = new TextDecoder();
  let sseBuffer = "";

  const reader = response.body.getReader();
  for (;;) {
    const { done, value } = await reader.read();
    if (done) break;

    sseBuffer += decoder.decode(value, { stream: true }).replaceAll("\r\n", "\n");
    const boundary = sseBuffer.lastIndexOf("\n\n");
    if (boundary === -1) continue;

    const complete = sseBuffer.slice(0, boundary + 2);
    sseBuffer = sseBuffer.slice(boundary + 2);

    for (const chunk of sse.parse(complete)) {
      if (chunk.data === "[DONE]") continue;

      let parsed: Record<string, unknown>;
      try {
        parsed = JSON.parse(chunk.data) as Record<string, unknown>;
      } catch {
        continue;
      }

      const eventType = parsed.type as string | undefined;
      if (!eventType) continue;

      if (eventType === "response.created") {
        const resp = parsed.response as Record<string, unknown>;
        state.responseId = (resp?.id as string) ?? state.responseId;
        state.created = (resp?.created_at as number) ?? state.created;
        continue;
      }

      switch (eventType) {
        case "response.output_text.delta": {
          const delta = parsed.delta as string;
          if (delta) content += delta;
          break;
        }

        case "response.reasoning_summary_text.delta": {
          const delta = parsed.delta as string;
          if (delta) reasoningContent += delta;
          break;
        }

        case "response.output_item.added": {
          const item = parsed.item as Record<string, unknown>;
          if (item?.type === "function_call") {
            const callId = item.call_id as string;
            const itemId = item.id as string | undefined;
            const name = item.name as string;
            const idx = state.toolCallIndex++;
            state.toolCallIds.set(callId, idx);
            if (itemId) state.toolCallIds.set(itemId, idx);
            toolCalls.set(idx, { id: callId, type: "function", function: { name, arguments: "" } });
          }
          break;
        }

        case "response.function_call_arguments.delta": {
          const delta = parsed.delta as string;
          const itemId = parsed.item_id as string | undefined;
          const callId = parsed.call_id as string | undefined;
          if (delta) {
            const idx = lookupToolIndex(state, itemId, callId);
            const tc = toolCalls.get(idx);
            if (tc) tc.function.arguments += delta;
          }
          break;
        }

        case "response.completed": {
          const resp = parsed.response as Record<string, unknown>;
          usage = extractUsage(resp?.usage as Record<string, unknown> | undefined);
          finishReason = state.toolCallIndex > 0 ? "tool_calls" : "stop";
          break;
        }

        case "response.incomplete": {
          const resp = parsed.response as Record<string, unknown>;
          usage = extractUsage(resp?.usage as Record<string, unknown> | undefined);
          finishReason = incompleteReason(resp);
          break;
        }

        case "response.failed": {
          const resp = parsed.response as Record<string, unknown>;
          usage = extractUsage(resp?.usage as Record<string, unknown> | undefined);
          const errorMsg = extractErrorMessage(resp);
          if (errorMsg) content += `[Error] ${errorMsg}`;
          break;
        }
      }
    }
  }

  // Process remaining buffer — reuse the same event handling as main loop
  if (sseBuffer.trim()) {
    for (const chunk of sse.parse(sseBuffer)) {
      if (chunk.data === "[DONE]") continue;

      let parsed: Record<string, unknown>;
      try {
        parsed = JSON.parse(chunk.data) as Record<string, unknown>;
      } catch {
        continue;
      }

      const eventType = parsed.type as string | undefined;
      if (!eventType) continue;

      switch (eventType) {
        case "response.output_text.delta": {
          const delta = parsed.delta as string;
          if (delta) content += delta;
          break;
        }
        case "response.reasoning_summary_text.delta": {
          const delta = parsed.delta as string;
          if (delta) reasoningContent += delta;
          break;
        }
        case "response.output_item.added": {
          const item = parsed.item as Record<string, unknown>;
          if (item?.type === "function_call") {
            const callId = item.call_id as string;
            const itemId = item.id as string | undefined;
            const name = item.name as string;
            const idx = state.toolCallIndex++;
            state.toolCallIds.set(callId, idx);
            if (itemId) state.toolCallIds.set(itemId, idx);
            toolCalls.set(idx, { id: callId, type: "function", function: { name, arguments: "" } });
          }
          break;
        }
        case "response.function_call_arguments.delta": {
          const delta = parsed.delta as string;
          const itemId = parsed.item_id as string | undefined;
          const callId = parsed.call_id as string | undefined;
          if (delta) {
            const idx = lookupToolIndex(state, itemId, callId);
            const tc = toolCalls.get(idx);
            if (tc) tc.function.arguments += delta;
          }
          break;
        }
        case "response.completed": {
          const resp = parsed.response as Record<string, unknown>;
          usage = extractUsage(resp?.usage as Record<string, unknown> | undefined);
          finishReason = state.toolCallIndex > 0 ? "tool_calls" : "stop";
          break;
        }
        case "response.incomplete": {
          const resp = parsed.response as Record<string, unknown>;
          usage = extractUsage(resp?.usage as Record<string, unknown> | undefined);
          finishReason = incompleteReason(resp);
          break;
        }
        case "response.failed": {
          const resp = parsed.response as Record<string, unknown>;
          usage = extractUsage(resp?.usage as Record<string, unknown> | undefined);
          const errorMsg = extractErrorMessage(resp);
          if (errorMsg) content += `[Error] ${errorMsg}`;
          break;
        }
      }
    }
  }

  const message: Record<string, unknown> = { role: "assistant", content: content || null };
  if (reasoningContent) {
    message.reasoning_content = reasoningContent;
  }
  if (toolCalls.size > 0) {
    message.tool_calls = Array.from(toolCalls.entries())
      .sort(([a], [b]) => a - b)
      .map(([, tc]) => tc);
  }

  const result = {
    id: `chatcmpl-${state.responseId}`,
    object: "chat.completion",
    created: state.created,
    model: state.model,
    choices: [{ index: 0, message, finish_reason: finishReason }],
    ...(usage ? { usage } : {}),
  };

  return new Response(JSON.stringify(result), {
    status: 200,
    headers: { "Content-Type": "application/json" },
  });
}

/** Custom SSE transform that strips event names (Chat Completions doesn't use them). */
function transformStream(source: ReadableStream<Uint8Array>, fn: (data: string) => string): ReadableStream<Uint8Array> {
  const decoder = new TextDecoder();
  const textEncoder = new TextEncoder();
  let buffer = "";

  return source.pipeThrough(
    new TransformStream<Uint8Array, Uint8Array>({
      transform(raw, controller) {
        buffer += decoder.decode(raw, { stream: true }).replaceAll("\r\n", "\n");
        const boundary = buffer.lastIndexOf("\n\n");
        if (boundary === -1) return;

        const complete = buffer.slice(0, boundary + 2);
        buffer = buffer.slice(boundary + 2);

        for (const chunk of sse.parse(complete)) {
          const transformed = fn(chunk.data);
          if (transformed) {
            // Emit without event name — standard Chat Completions format
            controller.enqueue(textEncoder.encode(`data: ${transformed}\n\n`));
          }
        }
      },
      flush(controller) {
        if (buffer.trim()) {
          for (const chunk of sse.parse(buffer)) {
            const transformed = fn(chunk.data);
            if (transformed) {
              controller.enqueue(textEncoder.encode(`data: ${transformed}\n\n`));
            }
          }
        }
        // Emit [DONE] marker
        controller.enqueue(textEncoder.encode("data: [DONE]\n\n"));
      },
    }),
  );
}

```

## File: src\providers\codex-state.ts
```
/** In-memory conversation state for Responses API previous_response_id support.
 *
 *  Each response is stored with its expanded input + output. When a follow-up
 *  request references previous_response_id, the stored input and output are
 *  prepended to build the full conversation context. Because we store the
 *  already-expanded input, recursive chains resolve in O(1) — no traversal. */

import * as sse from "../utils/streaming.ts";

const MAX_ENTRIES = 500;
const TTL_MS = 30 * 60 * 1000; // 30 minutes

interface StoredResponse {
  input: unknown[];
  output: unknown[];
  instructions: string | null;
  createdAt: number;
}

const responses = new Map<string, StoredResponse>();

// ---------------------------------------------------------------------------
// Public API
// ---------------------------------------------------------------------------

/** Store a completed response for future previous_response_id lookups. */
export function store(id: string, input: unknown[], output: unknown[], instructions: string | null): void {
  if (responses.size >= MAX_ENTRIES) evict();
  responses.set(id, { input, output, instructions, createdAt: Date.now() });
}

/** Expand previous_response_id: prepend stored context to current input.
 *  Returns null if the referenced response is not found (expired or invalid). */
export function expand(
  previousResponseId: string,
  currentInput: unknown[],
  currentInstructions: string | null,
): { input: unknown[]; instructions: string | null } | null {
  const stored = responses.get(previousResponseId);
  if (!stored) return null;
  if (Date.now() - stored.createdAt > TTL_MS) {
    responses.delete(previousResponseId);
    return null;
  }

  return {
    input: [...stored.input, ...stored.output, ...currentInput],
    instructions: currentInstructions ?? stored.instructions,
  };
}

// ---------------------------------------------------------------------------
// SSE response capture — extract id + output from Codex SSE stream
// ---------------------------------------------------------------------------

/** Extract the full response object from a Codex SSE stream (for non-streaming / buffer path).
 *  Returns the parsed response from `response.completed` or `response.failed`. */
export async function bufferResponseJson(response: Response): Promise<Record<string, unknown> | null> {
  if (!response.body) return null;

  const decoder = new TextDecoder();
  let sseBuffer = "";
  let fullResponse: Record<string, unknown> | null = null;

  const reader = response.body.getReader();
  for (;;) {
    const { done, value } = await reader.read();
    if (done) break;

    sseBuffer += decoder.decode(value, { stream: true }).replaceAll("\r\n", "\n");
    const boundary = sseBuffer.lastIndexOf("\n\n");
    if (boundary === -1) continue;

    const complete = sseBuffer.slice(0, boundary + 2);
    sseBuffer = sseBuffer.slice(boundary + 2);
    fullResponse = extractCompleted(complete) ?? fullResponse;
  }

  if (sseBuffer.trim()) {
    fullResponse = extractCompleted(sseBuffer) ?? fullResponse;
  }

  return fullResponse;
}

/** Wrap a SSE stream to capture response state while passing all data through unchanged.
 *  Zero latency — chunks are forwarded immediately, state is captured as a side-effect
 *  when `response.completed` or `response.failed` passes through. */
export function withStateCapture(
  stream: ReadableStream<Uint8Array>,
  expandedInput: unknown[],
  instructions: string | null,
): ReadableStream<Uint8Array> {
  const decoder = new TextDecoder();
  let buffer = "";

  return stream.pipeThrough(
    new TransformStream<Uint8Array, Uint8Array>({
      transform(raw, controller) {
        controller.enqueue(raw);

        buffer += decoder.decode(raw, { stream: true }).replaceAll("\r\n", "\n");
        const boundary = buffer.lastIndexOf("\n\n");
        if (boundary === -1) return;

        const complete = buffer.slice(0, boundary + 2);
        buffer = buffer.slice(boundary + 2);
        captureFromChunk(complete, expandedInput, instructions);
      },
      flush() {
        if (buffer.trim()) {
          captureFromChunk(buffer, expandedInput, instructions);
        }
      },
    }),
  );
}

// ---------------------------------------------------------------------------
// Internals
// ---------------------------------------------------------------------------

function captureFromChunk(raw: string, expandedInput: unknown[], instructions: string | null): void {
  for (const chunk of sse.parse(raw)) {
    if (chunk.data === "[DONE]") continue;
    try {
      const parsed = JSON.parse(chunk.data) as Record<string, unknown>;
      const type = parsed.type as string | undefined;
      if (type === "response.completed" || type === "response.failed") {
        const resp = parsed.response as Record<string, unknown> | undefined;
        if (resp?.id) {
          const output = Array.isArray(resp.output) ? (resp.output as unknown[]) : [];
          store(resp.id as string, expandedInput, output, instructions);
        }
      }
    } catch {
      // Ignore unparseable chunks
    }
  }
}

function extractCompleted(raw: string): Record<string, unknown> | null {
  for (const chunk of sse.parse(raw)) {
    if (chunk.data === "[DONE]") continue;
    try {
      const parsed = JSON.parse(chunk.data) as Record<string, unknown>;
      const type = parsed.type as string | undefined;
      if (type === "response.completed" || type === "response.failed") {
        return (parsed.response as Record<string, unknown>) ?? null;
      }
    } catch {
      // Ignore
    }
  }
  return null;
}

function evict(): void {
  const now = Date.now();
  for (const [key, value] of responses) {
    if (now - value.createdAt > TTL_MS) responses.delete(key);
  }
  // If still at capacity, remove oldest
  if (responses.size >= MAX_ENTRIES) {
    const first = responses.keys().next().value;
    if (first) responses.delete(first);
  }
}

```

## File: src\providers\codex.ts
```
/** Forwards requests to chatgpt.com/backend-api/codex with Codex CLI OAuth token.
 *
 *  The ChatGPT backend only accepts the Responses API format (input[] + instructions),
 *  but Amp CLI sends Chat Completions format (messages[]). This module transforms
 *  the request body before forwarding.
 *
 *  Forward flow (5 steps):
 *    1. AUTH    — acquire OAuth access token
 *    2. EXPAND  — resolve previous_response_id → full input (codex-state)
 *    3. PREPARE — transform body for Codex backend
 *    4. FORWARD — send to Codex backend
 *    5. PROCESS — format response + capture state for future turns */

import { codex as config } from "../auth/configs.ts";
import * as oauth from "../auth/oauth.ts";
import * as store from "../auth/store.ts";
import { CODEX_BASE_URL, codexHeaders, codexHeaderValues, codexPathMap } from "../constants.ts";
import { fromBase64url } from "../utils/encoding.ts";
import { logger } from "../utils/logger.ts";
import { apiError } from "../utils/responses.ts";
import type { Provider } from "./base.ts";
import { bufferCodexResponse, transformCodexResponse } from "./codex-sse.ts";
import * as state from "./codex-state.ts";
import { denied, forward } from "./forward.ts";

const DEFAULT_INSTRUCTIONS = "You are an expert coding assistant.";

export const provider: Provider = {
  name: "OpenAI Codex",
  routeDecision: "LOCAL_CODEX",

  isAvailable: (account?: number) =>
    account !== undefined ? !!store.get("codex", account)?.refreshToken : oauth.ready(config),

  accountCount: () => oauth.accountCount(config),

  async forward(sub, body, originalHeaders, rewrite, account = 0) {
    // 1. AUTH
    const accessToken = await oauth.token(config, account);
    if (!accessToken) return denied("OpenAI Codex");

    const accountId = getAccountId(accessToken, account);
    const codexPath = codexPathMap[sub] ?? sub;
    const promptCacheKey = originalHeaders.get("x-amp-thread-id") ?? originalHeaders.get("x-session-id") ?? undefined;

    // 2. EXPAND — resolve previous_response_id before body transform
    const expandedBody = expandPreviousResponse(body.forwardBody);
    if (expandedBody === null) {
      return apiError(400, "previous_response_id references an unknown or expired response");
    }

    // 3. PREPARE — transform body for Codex backend
    const {
      body: codexBody,
      needsResponseTransform,
      expandedInput,
      instructions,
    } = transformForCodex(expandedBody, promptCacheKey);
    const ampModel = body.ampModel ?? "gpt-5.2";

    // 4. FORWARD
    const response = await forward({
      url: `${CODEX_BASE_URL}${codexPath}`,
      body: codexBody,
      streaming: body.stream,
      providerName: "OpenAI Codex",
      rewrite: needsResponseTransform ? undefined : rewrite,
      email: store.get("codex", account)?.email,
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${accessToken}`,
        Accept: body.stream ? "text/event-stream" : "application/json",
        Connection: "Keep-Alive",
        [codexHeaders.BETA]: codexHeaderValues.BETA_RESPONSES,
        [codexHeaders.ORIGINATOR]: codexHeaderValues.ORIGINATOR,
        "User-Agent": codexHeaderValues.USER_AGENT,
        Version: codexHeaderValues.VERSION,
        ...(accountId ? { [codexHeaders.ACCOUNT_ID]: accountId } : {}),
        ...(promptCacheKey
          ? { [codexHeaders.SESSION_ID]: promptCacheKey, [codexHeaders.CONVERSATION_ID]: promptCacheKey }
          : {}),
      },
    });

    // 5. PROCESS — format response + capture state
    if (!response.ok) return response;

    // Chat Completions path — transform only, no state capture
    if (needsResponseTransform) {
      return body.stream ? transformCodexResponse(response, ampModel) : bufferCodexResponse(response, ampModel);
    }

    // Responses API path — capture state + format
    return body.stream
      ? processStreamingResponse(response, expandedInput, instructions)
      : processBufferedResponse(response, expandedInput, instructions);
  },
};

// ---------------------------------------------------------------------------
// Step 2: Expand previous_response_id
// ---------------------------------------------------------------------------

/** Resolve previous_response_id into expanded input. Returns the (possibly modified) body string,
 *  or null if the referenced response was not found. */
function expandPreviousResponse(rawBody: string): string | null {
  if (!rawBody) return rawBody;

  let parsed: Record<string, unknown>;
  try {
    parsed = JSON.parse(rawBody) as Record<string, unknown>;
  } catch {
    return rawBody;
  }

  const prevId = parsed.previous_response_id as string | undefined;
  if (!prevId) return rawBody;

  const currentInput = Array.isArray(parsed.input) ? (parsed.input as unknown[]) : [];
  const currentInstructions = (parsed.instructions as string) ?? null;
  const expanded = state.expand(prevId, currentInput, currentInstructions);
  if (!expanded) {
    logger.warn(`previous_response_id "${prevId}" not found in state store`);
    return null;
  }

  parsed.input = expanded.input;
  if (expanded.instructions) parsed.instructions = expanded.instructions;
  delete parsed.previous_response_id;

  logger.debug(`Expanded previous_response_id "${prevId}", input items: ${expanded.input.length}`);
  return JSON.stringify(parsed);
}

// ---------------------------------------------------------------------------
// Step 5: Response processing with state capture
// ---------------------------------------------------------------------------

/** Streaming Responses API: pass through SSE + capture state from response.completed. */
function processStreamingResponse(response: Response, expandedInput: unknown[], instructions: string | null): Response {
  if (!response.body) return response;

  const body = state.withStateCapture(response.body, expandedInput, instructions);
  return new Response(body, { status: response.status, headers: response.headers });
}

/** Non-streaming Responses API: buffer SSE → JSON + capture state. */
async function processBufferedResponse(
  response: Response,
  expandedInput: unknown[],
  instructions: string | null,
): Promise<Response> {
  const fullResponse = await state.bufferResponseJson(response);
  if (!fullResponse) {
    return apiError(502, "No response received from Codex backend");
  }

  // Capture state for future previous_response_id lookups
  if (fullResponse.id) {
    const output = Array.isArray(fullResponse.output) ? (fullResponse.output as unknown[]) : [];
    state.store(fullResponse.id as string, expandedInput, output, instructions);
  }

  return new Response(JSON.stringify(fullResponse), {
    status: 200,
    headers: { "Content-Type": "application/json" },
  });
}

// ---------------------------------------------------------------------------
// Body transformation: Chat Completions → Responses API
// ---------------------------------------------------------------------------

interface ChatMessage {
  role: string;
  content: unknown;
  tool_calls?: ToolCallItem[];
  tool_call_id?: string;
  name?: string;
}

interface ToolCallItem {
  id: string;
  type: string;
  function: { name: string; arguments: string };
}

function clampReasoningEffort(model: string, effort: string): string {
  const modelId = model.includes("/") ? model.split("/").pop()! : model;
  if (modelId === "gpt-5.1" && effort === "xhigh") return "high";
  if ((modelId.startsWith("gpt-5.2") || modelId.startsWith("gpt-5.3")) && effort === "minimal") return "low";
  if (modelId === "gpt-5.1-codex-mini") {
    return effort === "high" || effort === "xhigh" ? "high" : "medium";
  }
  return effort;
}

interface TransformResult {
  body: string;
  needsResponseTransform: boolean;
  /** The input[] sent to Codex — used for state capture. */
  expandedInput: unknown[];
  /** The instructions sent to Codex — used for state capture. */
  instructions: string | null;
}

function transformForCodex(rawBody: string, promptCacheKey?: string): TransformResult {
  const empty: TransformResult = {
    body: rawBody,
    needsResponseTransform: false,
    expandedInput: [],
    instructions: null,
  };
  if (!rawBody) return empty;

  let parsed: Record<string, unknown>;
  try {
    parsed = JSON.parse(rawBody) as Record<string, unknown>;
  } catch {
    return empty;
  }

  // Convert Chat Completions messages[] → Responses API input[]
  let needsResponseTransform = false;
  if (Array.isArray(parsed.messages) && !parsed.input) {
    const { instructions, input } = convertMessages(parsed.messages as ChatMessage[]);
    parsed.input = input;
    parsed.instructions = parsed.instructions ?? instructions ?? DEFAULT_INSTRUCTIONS;
    delete parsed.messages;
    needsResponseTransform = true;
  }

  // Already Responses API format — ensure instructions exists
  if (!parsed.instructions) {
    parsed.instructions = extractInstructionsFromInput(parsed) ?? DEFAULT_INSTRUCTIONS;
  }

  // Snapshot input + instructions for state capture (before Codex-specific mutations)
  const expandedInput = Array.isArray(parsed.input) ? [...(parsed.input as unknown[])] : [];
  const instructions = (parsed.instructions as string) ?? null;

  // Codex backend requirements
  parsed.store = false;
  parsed.stream = true;

  // Strip id fields from input items
  if (Array.isArray(parsed.input)) {
    stripInputIds(parsed.input as Record<string, unknown>[]);
    fixOrphanOutputs(parsed.input as Record<string, unknown>[]);
  }

  // Reasoning config — merge with caller-provided values, defaults match reference behavior
  // Chat Completions uses top-level "reasoning_effort"; Responses API uses "reasoning.effort"
  const model = (parsed.model as string) ?? "";
  const existingReasoning = (parsed.reasoning as Record<string, unknown>) ?? {};
  const topLevelEffort = parsed.reasoning_effort as string | undefined;
  parsed.reasoning = {
    effort: clampReasoningEffort(model, topLevelEffort ?? (existingReasoning.effort as string) ?? "medium"),
    summary: existingReasoning.summary ?? "auto",
  };

  const existingText = (parsed.text as Record<string, unknown>) ?? {};
  parsed.text = { ...existingText, verbosity: existingText.verbosity ?? "medium" };

  const existingInclude = Array.isArray(parsed.include) ? (parsed.include as string[]) : [];
  if (!existingInclude.includes("reasoning.encrypted_content")) {
    existingInclude.push("reasoning.encrypted_content");
  }
  parsed.include = existingInclude;

  if (promptCacheKey) {
    parsed.prompt_cache_key = promptCacheKey;
  }

  // Remove fields the Codex backend doesn't accept
  delete parsed.reasoning_effort; // Chat Completions field; already mapped to reasoning.effort above
  delete parsed.max_tokens;
  delete parsed.max_completion_tokens;
  delete parsed.max_output_tokens;
  // Chat Completions fields not in Responses API
  delete parsed.frequency_penalty;
  delete parsed.logprobs;
  delete parsed.top_logprobs;
  delete parsed.n;
  delete parsed.presence_penalty;
  delete parsed.seed;
  delete parsed.stop;
  delete parsed.logit_bias;
  delete parsed.response_format;

  // Normalize tools[] for Responses API: flatten function.{name,description,parameters,strict} to top-level
  if (Array.isArray(parsed.tools)) {
    parsed.tools = (parsed.tools as Record<string, unknown>[]).map((tool) => {
      if (tool.type === "function" && tool.function && typeof tool.function === "object") {
        const fn = tool.function as Record<string, unknown>;
        return {
          type: "function",
          name: fn.name,
          description: fn.description,
          parameters: fn.parameters,
          ...(fn.strict !== undefined ? { strict: fn.strict } : {}),
        };
      }
      return tool;
    });
  }

  // Normalize tool_choice for Responses API
  if (parsed.tool_choice !== undefined && parsed.tool_choice !== null) {
    if (typeof parsed.tool_choice === "string") {
      // "auto", "none", "required" pass through as-is
    } else if (typeof parsed.tool_choice === "object") {
      const tc = parsed.tool_choice as Record<string, unknown>;
      if (tc.type === "function" && tc.function) {
        const fn = tc.function as Record<string, unknown>;
        parsed.tool_choice = { type: "function", name: fn.name };
      } else if (tc.type === "tool" && tc.name) {
        parsed.tool_choice = { type: "function", name: tc.name };
      }
    }
  }

  return { body: JSON.stringify(parsed), needsResponseTransform, expandedInput, instructions };
}

/** Convert Chat Completions messages[] → Responses API input[] + instructions. */
function convertMessages(messages: ChatMessage[]): { instructions: string | null; input: unknown[] } {
  let instructions: string | null = null;
  const input: unknown[] = [];

  for (const msg of messages) {
    switch (msg.role) {
      case "system":
      case "developer": {
        // First system message → instructions; additional ones → developer input items
        const text = textOf(msg.content);
        if (!instructions) {
          instructions = text;
        } else if (text) {
          input.push({ role: "developer", content: [{ type: "input_text", text }] });
        }
        break;
      }

      case "user":
        input.push({ role: "user", content: convertUserContent(msg.content) });
        break;

      case "assistant": {
        // Text content → message output item
        const text = textOf(msg.content);
        if (text) {
          input.push({
            type: "message",
            role: "assistant",
            content: [{ type: "output_text", text, annotations: [] }],
            status: "completed",
          });
        }
        // Tool calls → function_call items
        if (msg.tool_calls) {
          for (const tc of msg.tool_calls) {
            input.push({
              type: "function_call",
              call_id: tc.id,
              name: tc.function.name,
              arguments: tc.function.arguments,
            });
          }
        }
        break;
      }

      case "tool":
        // Tool result → function_call_output
        input.push({
          type: "function_call_output",
          call_id: msg.tool_call_id,
          output: stringifyContent(msg.content),
        });
        break;
    }
  }

  return { instructions, input };
}

/** Convert user message content to Responses API format. */
function convertUserContent(content: unknown): unknown[] {
  if (typeof content === "string") {
    return [{ type: "input_text", text: content }];
  }
  if (Array.isArray(content)) {
    return content.map((part: Record<string, unknown>) => {
      if (part.type === "text") {
        return { type: "input_text", text: part.text };
      }
      if (part.type === "image_url") {
        const imageUrl = part.image_url as Record<string, unknown>;
        return { type: "input_image", image_url: imageUrl.url, detail: imageUrl.detail ?? "auto" };
      }
      return part;
    });
  }
  return [{ type: "input_text", text: String(content) }];
}

/** Convert content to string, with JSON fallback for non-text values. */
function stringifyContent(content: unknown): string {
  if (typeof content === "string") return content;
  const text = textOf(content);
  if (text !== null) return text;
  try {
    return JSON.stringify(content);
  } catch {
    return String(content ?? "");
  }
}

/** Extract text from content (string or array). */
function textOf(content: unknown): string | null {
  if (typeof content === "string") return content;
  if (Array.isArray(content)) {
    const texts = content
      .filter((c: Record<string, unknown>) => c.type === "text" || c.type === "input_text")
      .map((c: Record<string, unknown>) => c.text as string);
    return texts.length > 0 ? texts.join("\n") : null;
  }
  return null;
}

/** Extract instructions from system/developer messages already in input[]. */
function extractInstructionsFromInput(parsed: Record<string, unknown>): string | null {
  const input = parsed.input;
  if (!Array.isArray(input)) return null;

  for (let i = 0; i < input.length; i++) {
    const item = input[i] as Record<string, unknown>;
    if (item.role === "system" || item.role === "developer") {
      const text = textOf(item.content);
      if (text) {
        input.splice(i, 1);
        return text;
      }
    }
  }
  return null;
}

/** Strip `id` fields from input items — Codex backend rejects them. */
function stripInputIds(items: Record<string, unknown>[]): void {
  for (const item of items) {
    if ("id" in item) {
      delete item.id;
    }
  }
}

/** Convert orphan function_call_output items (no matching function_call) to assistant messages. */
function fixOrphanOutputs(items: Record<string, unknown>[]): void {
  const callIds = new Set(
    items.filter((i) => i.type === "function_call" && typeof i.call_id === "string").map((i) => i.call_id as string),
  );
  for (let i = 0; i < items.length; i++) {
    const item = items[i]!;
    if (item.type === "function_call_output" && typeof item.call_id === "string" && !callIds.has(item.call_id)) {
      const toolName = typeof item.name === "string" ? (item.name as string) : "tool";
      let text = "";
      try {
        text = typeof item.output === "string" ? (item.output as string) : JSON.stringify(item.output);
      } catch {
        text = String(item.output ?? "");
      }
      if (text.length > 16000) {
        text = `${text.slice(0, 16000)}\n...[truncated]`;
      }
      items[i] = {
        type: "message",
        role: "assistant",
        content: [
          {
            type: "output_text",
            text: `[Previous ${toolName} result; call_id=${item.call_id}]: ${text}`,
            annotations: [],
          },
        ],
        status: "completed",
      };
    }
  }
}

/** Extract chatgpt_account_id from JWT, falling back to stored credentials. */
function getAccountId(accessToken: string, account: number): string | undefined {
  const creds = store.get("codex", account);
  if (creds?.accountId) return creds.accountId;

  try {
    const parts = accessToken.split(".");
    if (parts.length < 2 || !parts[1]) return undefined;
    const payload = JSON.parse(new TextDecoder().decode(fromBase64url(parts[1]))) as Record<string, unknown>;
    const auth = payload["https://api.openai.com/auth"] as Record<string, unknown> | undefined;
    return (auth?.chatgpt_account_id as string) ?? undefined;
  } catch {
    return undefined;
  }
}

```

## File: src\providers\forward.ts
```
/** HTTP forwarding with transport-level retry, SSE proxying, and response rewriting. */

import { logger } from "../utils/logger.ts";
import { apiError } from "../utils/responses.ts";
import * as sse from "../utils/streaming.ts";

export interface ForwardOptions {
  url: string;
  body: string;
  streaming: boolean;
  headers: Record<string, string>;
  providerName: string;
  rewrite?: (data: string) => string;
  email?: string;
}

const RETRYABLE_STATUS = new Set([408, 500, 502, 503, 504]);
const MAX_RETRIES = 3;
const RETRY_DELAY_MS = 500;

const PASSTHROUGH_HEADERS = [
  "content-type",
  "retry-after",
  "x-request-id",
  "x-ratelimit-limit-requests",
  "x-ratelimit-remaining-requests",
  "x-ratelimit-reset-requests",
];

function copyHeaders(source: Headers): Headers {
  const dest = new Headers();
  for (const name of PASSTHROUGH_HEADERS) {
    const value = source.get(name);
    if (value !== null) dest.set(name, value);
  }
  return dest;
}

export async function forward(opts: ForwardOptions): Promise<Response> {
  for (let attempt = 0; attempt <= MAX_RETRIES; attempt++) {
    let response: Response;
    try {
      response = await fetch(opts.url, {
        method: "POST",
        headers: opts.headers,
        body: opts.body,
      });
    } catch (err) {
      if (attempt < MAX_RETRIES) {
        logger.debug(`${opts.providerName} fetch error, retry ${attempt + 1}/${MAX_RETRIES}`, {
          error: String(err),
        });
        await Bun.sleep(RETRY_DELAY_MS * (attempt + 1));
        continue;
      }
      return transportErrorResponse(opts.providerName, err);
    }

    // Retry on server errors (429 handled at routing layer)
    if (RETRYABLE_STATUS.has(response.status) && attempt < MAX_RETRIES) {
      await response.text(); // consume body
      logger.debug(`${opts.providerName} returned ${response.status}, retry ${attempt + 1}/${MAX_RETRIES}`);
      await Bun.sleep(RETRY_DELAY_MS * (attempt + 1));
      continue;
    }

    const contentType = response.headers.get("Content-Type") ?? "application/json";

    if (!response.ok) {
      const text = await response.text();
      const ctx = opts.email ? ` account=${opts.email}` : "";
      logger.error(`${opts.providerName} API error (${response.status})${ctx}`, { error: text.slice(0, 200) });

      // Normalize non-standard error responses (e.g. {"detail":"..."}) to OpenAI format
      // so Amp CLI can deserialize them (it expects {"error": {...}})
      let errorBody = text;
      try {
        const parsed = JSON.parse(text) as Record<string, unknown>;
        if (!parsed.error) {
          const message = (parsed.detail as string) ?? (parsed.message as string) ?? text;
          errorBody = JSON.stringify({
            error: { message, type: "api_error", code: String(response.status) },
          });
        }
      } catch {
        // Not JSON — wrap raw text
        errorBody = JSON.stringify({
          error: { message: text, type: "api_error", code: String(response.status) },
        });
      }

      const headers = copyHeaders(response.headers);
      headers.set("Content-Type", "application/json");
      return new Response(errorBody, {
        status: response.status,
        headers,
      });
    }

    const isSSE = contentType.includes("text/event-stream") || opts.streaming;
    if (isSSE) return sse.proxy(response, opts.rewrite);

    const headers = copyHeaders(response.headers);

    if (opts.rewrite) {
      const text = await response.text();
      return new Response(opts.rewrite(text), { status: response.status, headers });
    }

    return new Response(response.body, { status: response.status, headers });
  }

  // Unreachable, but TypeScript needs it
  throw new Error(`${opts.providerName}: all retries exhausted`);
}

export function denied(providerName: string): Response {
  return apiError(401, `No ${providerName} OAuth token available. Run login first.`);
}

function transportErrorResponse(providerName: string, err: unknown): Response {
  const message = transportErrorMessage(providerName, err);
  logger.error(`${providerName} transport error after retries exhausted`, { error: String(err) });
  return apiError(502, message, "connection_error");
}

function transportErrorMessage(providerName: string, err: unknown): string {
  const base = `${providerName} connection error after retries were exhausted.`;
  const details = String(err);

  if (providerName !== "Anthropic") {
    return `${base} ${details}`;
  }

  const looksLikeReset =
    details.includes("ECONNRESET") ||
    details.includes("socket connection was closed unexpectedly") ||
    details.includes("tls") ||
    details.includes("network");

  if (!looksLikeReset) {
    return `${base} ${details}`;
  }

  return `${base} ${details} This is often a local network issue rather than an OAuth bug: check Wi-Fi MTU (1492 is a common fix), hotspot stability, and iPhone dual-SIM Cellular Data Switching if you are tethering.`;
}

```

## File: src\providers\google.ts
```
/** Unified Google provider — merges Gemini CLI and Antigravity strategies
 *  with internal fallback. Tries preferred strategy first, then falls back. */

import { google as config } from "../auth/configs.ts";
import * as oauth from "../auth/oauth.ts";
import * as store from "../auth/store.ts";
import { ANTIGRAVITY_DAILY_ENDPOINT, ANTIGRAVITY_DAILY_SANDBOX_ENDPOINT, CODE_ASSIST_ENDPOINT } from "../constants.ts";
import { buildUrl, maybeWrap, withUnwrap } from "../utils/code-assist.ts";
import { logger } from "../utils/logger.ts";
import * as path from "../utils/path.ts";
import { apiError } from "../utils/responses.ts";
import type { Provider } from "./base.ts";
import { denied, forward } from "./forward.ts";

const GOOGLE_CLIENT_METADATA = JSON.stringify({
  ideType: "IDE_UNSPECIFIED",
  platform: "PLATFORM_UNSPECIFIED",
  pluginType: "GEMINI",
});

interface GoogleStrategy {
  name: string;
  headers: Readonly<Record<string, string>>;
  endpoints: readonly string[];
  modelMapper?: (model: string) => string;
  wrapOpts: {
    userAgent: "antigravity" | "pi-coding-agent";
    requestIdPrefix: "agent" | "pi";
    requestType?: "agent" | "image_gen";
  };
}

const geminiStrategy: GoogleStrategy = {
  name: "gemini",
  headers: {
    "User-Agent": "google-cloud-sdk vscode_cloudshelleditor/0.1",
    "X-Goog-Api-Client": "gl-node/22.17.0",
    "Client-Metadata": GOOGLE_CLIENT_METADATA,
  },
  endpoints: [CODE_ASSIST_ENDPOINT],
  wrapOpts: {
    userAgent: "pi-coding-agent",
    requestIdPrefix: "pi",
  },
};

/** Antigravity uses different model names than what Amp CLI sends. */
const antigravityModelMap: Record<string, string> = {
  "gemini-3-flash-preview": "gemini-3-flash",
  "gemini-3-pro-preview": "gemini-3-pro-high",
  "gemini-3-pro-image-preview": "gemini-3.1-flash-image",
  "gemini-3.1-flash-image-preview": "gemini-3.1-flash-image",
};

const antigravityStrategy: GoogleStrategy = {
  name: "antigravity",
  headers: {
    "User-Agent": "antigravity/1.104.0 darwin/arm64",
    "X-Goog-Api-Client": "google-cloud-sdk vscode_cloudshelleditor/0.1",
    "Client-Metadata": GOOGLE_CLIENT_METADATA,
  },
  endpoints: [ANTIGRAVITY_DAILY_ENDPOINT, ANTIGRAVITY_DAILY_SANDBOX_ENDPOINT, CODE_ASSIST_ENDPOINT],
  modelMapper: (model: string) => antigravityModelMap[model] ?? model,
  wrapOpts: {
    userAgent: "antigravity",
    requestIdPrefix: "agent",
    requestType: "agent",
  },
};

const strategies: readonly GoogleStrategy[] = [geminiStrategy, antigravityStrategy];

/** Models that only work on the antigravity strategy. */
const ANTIGRAVITY_ONLY_MODELS = new Set(["gemini-3-pro-image-preview", "gemini-3.1-flash-image-preview"]);

const COOLDOWN_MS = 60_000;

interface StrategyPreference {
  strategy: GoogleStrategy;
  until: number;
}

// Per-account strategy preference: after success, prefer that strategy;
// after failure, skip it for COOLDOWN_MS.
const preferredStrategy = new Map<number, StrategyPreference>();
const cooldowns = new Map<string, number>(); // key: `${account}:${strategy.name}`

function cooldownKey(account: number, strategy: GoogleStrategy): string {
  return `${account}:${strategy.name}`;
}

function getOrderedStrategies(account: number, model?: string): GoogleStrategy[] {
  const now = Date.now();

  // Some models only work on antigravity — skip other strategies entirely
  if (model && ANTIGRAVITY_ONLY_MODELS.has(model)) {
    const cd = cooldowns.get(cooldownKey(account, antigravityStrategy));
    if (cd && cd > now) return [];
    return [antigravityStrategy];
  }

  const pref = preferredStrategy.get(account);
  const ordered =
    pref && pref.until > now ? [pref.strategy, ...strategies.filter((s) => s !== pref.strategy)] : [...strategies];

  return ordered.filter((s) => {
    const cd = cooldowns.get(cooldownKey(account, s));
    return !cd || cd <= now;
  });
}

function markSuccess(account: number, strategy: GoogleStrategy): void {
  preferredStrategy.set(account, { strategy, until: Date.now() + COOLDOWN_MS * 10 });
  cooldowns.delete(cooldownKey(account, strategy));
}

function markFailure(account: number, strategy: GoogleStrategy): void {
  cooldowns.set(cooldownKey(account, strategy), Date.now() + COOLDOWN_MS);
  const pref = preferredStrategy.get(account);
  if (pref?.strategy === strategy) {
    preferredStrategy.delete(account);
  }
}

/** Buffer an SSE response and merge all chunks into a single JSON response.
 *  Used when we force streamGenerateContent but the client expects non-streaming JSON.
 *  Accumulates all candidate parts across chunks (image inlineData may be in earlier chunks). */
async function bufferSSEToJSON(response: Response): Promise<Response | null> {
  const text = await response.text();
  const chunks: Record<string, unknown>[] = [];

  for (const line of text.split("\n")) {
    if (!line.startsWith("data: ")) continue;
    const data = line.slice(6).trim();
    if (!data || data === "[DONE]") continue;
    try {
      chunks.push(JSON.parse(data) as Record<string, unknown>);
    } catch {
      // skip non-JSON
    }
  }

  if (chunks.length === 0) return null;
  if (chunks.length === 1) {
    return new Response(JSON.stringify(chunks[0]), {
      status: 200,
      headers: { "Content-Type": "application/json" },
    });
  }

  // Merge: accumulate parts from all chunks into the first candidate
  const merged = chunks[0]! as Record<string, unknown>;
  const allParts: unknown[] = [];

  for (const chunk of chunks) {
    const candidates = chunk.candidates as { content?: { parts?: unknown[] } }[] | undefined;
    if (!candidates) continue;
    for (const candidate of candidates) {
      if (candidate.content?.parts) {
        allParts.push(...candidate.content.parts);
      }
    }
  }

  // Use last chunk's metadata (finishReason, usageMetadata)
  const last = chunks[chunks.length - 1]! as Record<string, unknown>;
  const lastCandidates = last.candidates as Record<string, unknown>[] | undefined;
  const mergedCandidates = merged.candidates as Record<string, unknown>[] | undefined;

  if (mergedCandidates?.[0] && allParts.length > 0) {
    const content = (mergedCandidates[0] as Record<string, unknown>).content as Record<string, unknown> | undefined;
    if (content) content.parts = allParts;
    if (lastCandidates?.[0]) {
      (mergedCandidates[0] as Record<string, unknown>).finishReason = (
        lastCandidates[0] as Record<string, unknown>
      ).finishReason;
    }
  }
  if (last.usageMetadata) merged.usageMetadata = last.usageMetadata;

  return new Response(JSON.stringify(merged), {
    status: 200,
    headers: { "Content-Type": "application/json" },
  });
}

/** Generate a fallback project ID when none is stored (matches CLIProxyAPI behavior). */
function generateProjectId(): string {
  const adjectives = ["useful", "bright", "swift", "calm", "bold"];
  const nouns = ["fuze", "wave", "spark", "flow", "core"];
  const adj = adjectives[Math.floor(Math.random() * adjectives.length)]!;
  const noun = nouns[Math.floor(Math.random() * nouns.length)]!;
  const rand = crypto.randomUUID().slice(0, 5).toLowerCase();
  return `${adj}-${noun}-${rand}`;
}

export const provider: Provider = {
  name: "Google",
  routeDecision: "LOCAL_GOOGLE",

  isAvailable: (account?: number) =>
    account !== undefined ? !!store.get("google", account)?.refreshToken : oauth.ready(config),

  accountCount: () => oauth.accountCount(config),

  async forward(sub, body, _originalHeaders, rewrite, account = 0) {
    const accessToken = await oauth.token(config, account);
    if (!accessToken) return denied("Google");

    const creds = store.get("google", account);
    const projectId = creds?.projectId || generateProjectId();
    const email = creds?.email;

    const modelAction = path.googleModel(sub);
    if (!modelAction) {
      logger.debug(`Non-model Google path, cannot route to CCA: ${sub}`);
      return denied("Google (unsupported path)");
    }

    const unwrapThenRewrite = withUnwrap(rewrite);
    const orderedStrategies = getOrderedStrategies(account, modelAction.model);

    if (orderedStrategies.length === 0) {
      const now = Date.now();
      let minWait = COOLDOWN_MS;
      for (const s of strategies) {
        const until = cooldowns.get(cooldownKey(account, s));
        if (until) minWait = Math.min(minWait, Math.max(0, until - now));
      }
      const retryAfterS = Math.ceil(minWait / 1000);
      return new Response(
        JSON.stringify({
          error: { message: "All Google strategies cooling down", type: "rate_limit_error", code: "429" },
        }),
        { status: 429, headers: { "Content-Type": "application/json", "Retry-After": String(retryAfterS) } },
      );
    }

    let saw429 = false;
    let lastResponse: Response | null = null;

    for (const strategy of orderedStrategies) {
      const model = strategy.modelMapper ? strategy.modelMapper(modelAction.model) : modelAction.model;
      const isImageModel = model.includes("image");
      const wrapOpts = isImageModel ? { ...strategy.wrapOpts, requestType: "image_gen" as const } : strategy.wrapOpts;
      const requestBody = maybeWrap(body.parsed, body.forwardBody, projectId, model, wrapOpts);

      const headers: Record<string, string> = {
        ...strategy.headers,
        Authorization: `Bearer ${accessToken}`,
        "Content-Type": "application/json",
        Accept: body.stream ? "text/event-stream" : "application/json",
      };

      logger.info(`Google strategy=${strategy.name} account=${account} model=${model}`);

      // Antigravity forces streaming endpoint for gemini-3-pro* and image models (matches CLIProxyAPI behavior)
      const forceStream = strategy.name === "antigravity" && (model.startsWith("gemini-3-pro") || isImageModel);
      const action = forceStream ? "streamGenerateContent" : modelAction.action;

      for (const endpoint of strategy.endpoints) {
        const url = buildUrl(endpoint, action);
        try {
          const forceStreamNonStreaming = forceStream && !body.stream;
          const response = await forward({
            url,
            body: requestBody,
            streaming: forceStreamNonStreaming ? true : body.stream,
            headers,
            providerName: `Google/${strategy.name}`,
            rewrite: unwrapThenRewrite,
            email,
          });

          // When we forced streaming but client expects JSON, buffer SSE and return last chunk
          if (forceStreamNonStreaming && response.ok && response.body) {
            const merged = await bufferSSEToJSON(response);
            if (merged) {
              markSuccess(account, strategy);
              return merged;
            }
          }

          if (response.status === 401 || response.status === 403) {
            return response;
          }

          if (response.status === 404) {
            lastResponse = response;
            logger.debug(`Google strategy=${strategy.name} model not found (404), trying next endpoint`);
            continue;
          }

          if (response.status === 429) {
            saw429 = true;
            lastResponse = response;
            logger.debug(`Google strategy=${strategy.name} failed (${response.status}), trying next`);
            break;
          }

          if (response.status >= 500) {
            lastResponse = response;
            logger.debug(`Google strategy=${strategy.name} failed (${response.status}), trying next`);
            continue;
          }

          markSuccess(account, strategy);
          return response;
        } catch (err) {
          lastResponse = apiError(502, `Google/${strategy.name} endpoint failed: ${String(err)}`);
          logger.debug(`Google strategy=${strategy.name} endpoint error`, { error: String(err) });
        }
      }

      markFailure(account, strategy);
    }

    if (saw429) {
      return lastResponse ?? apiError(429, "All Google strategies rate limited", "rate_limit_error");
    }

    return lastResponse ?? apiError(502, "All Google strategies exhausted");
  },
};

```

## File: src\proxy\rewriter.ts
```
/**
 * SSE response rewriting: model name substitution + thinking block suppression.
 *
 * Thinking blocks are filtered when tool_use is present because the Amp client
 * struggles with both simultaneously (ref: CLIProxyAPI response_rewriter.go:72-94).
 */

import { modelFieldPaths } from "../constants.ts";

/** Pre-split field paths — avoids .split(".") on every SSE chunk. */
const MODEL_FIELD_PARTS = modelFieldPaths.map((p) => p.split("."));

export function rewrite(originalModel: string): (data: string) => string {
  return (data: string) => {
    if (data === "[DONE]") return data;

    try {
      const parsed = JSON.parse(data) as Record<string, unknown>;
      let modified = false;

      for (const parts of MODEL_FIELD_PARTS) {
        const current = getField(parsed, parts);
        if (current !== undefined && current !== originalModel) {
          setField(parsed, parts, originalModel);
          modified = true;
        }
      }

      if (suppressThinking(parsed)) modified = true;

      return modified ? JSON.stringify(parsed) : data;
    } catch {
      return data;
    }
  };
}

function getField(obj: Record<string, unknown>, parts: string[]): unknown {
  let current: unknown = obj;
  for (const part of parts) {
    if (current == null || typeof current !== "object") return undefined;
    current = (current as Record<string, unknown>)[part];
  }
  return current;
}

function setField(obj: Record<string, unknown>, parts: string[], value: unknown): void {
  let current: unknown = obj;
  for (let i = 0; i < parts.length - 1; i++) {
    if (current == null || typeof current !== "object") return;
    current = (current as Record<string, unknown>)[parts[i]!];
  }
  if (current != null && typeof current === "object") {
    (current as Record<string, unknown>)[parts[parts.length - 1]!] = value;
  }
}

function suppressThinking(data: Record<string, unknown>): boolean {
  const content = data.content;
  if (!Array.isArray(content)) return false;

  const hasToolUse = content.some((b: Record<string, unknown>) => b.type === "tool_use");
  if (!hasToolUse) return false;

  const hasThinking = content.some((b: Record<string, unknown>) => b.type === "thinking");
  if (!hasThinking) return false;

  data.content = content.filter((b: Record<string, unknown>) => b.type !== "thinking");
  return true;
}

```

## File: src\proxy\upstream.ts
```
/** Reverse proxy to ampcode.com for non-intercepted routes and fallback. */

import { logger } from "../utils/logger.ts";

export async function forward(request: Request, ampUpstreamUrl: string, ampApiKey?: string): Promise<Response> {
  const url = new URL(request.url);
  const upstreamUrl = new URL(url.pathname + url.search, ampUpstreamUrl);

  const upstreamHost = new URL(ampUpstreamUrl).host;
  const headers = new Headers(request.headers);
  if (ampApiKey) headers.set("Authorization", `Bearer ${ampApiKey}`);
  headers.set("Host", upstreamHost);

  logger.debug("Forwarding to Amp upstream", { provider: "amp" });

  try {
    const response = await fetch(upstreamUrl.toString(), {
      method: request.method,
      headers,
      redirect: "manual",
      body: request.method !== "GET" && request.method !== "HEAD" ? request.body : undefined,
      duplex: "half" as const,
    });

    const responseHeaders = new Headers(response.headers);
    responseHeaders.delete("Content-Encoding");
    responseHeaders.delete("Content-Length");

    return new Response(response.body, {
      status: response.status,
      statusText: response.statusText,
      headers: responseHeaders,
    });
  } catch (err) {
    logger.error("Upstream proxy error", { error: String(err) });
    return Response.json({ error: "Failed to connect to Amp upstream", details: String(err) }, { status: 502 });
  }
}

```

## File: src\routing\affinity.ts
```
/** Thread+provider → (quotaPool, account) affinity map.
 *  Ensures a thread sticks to the same account per provider for session consistency.
 *  Key is composite (threadId, ampProvider) so a single thread can hold
 *  independent affinities for different providers (e.g. anthropic AND google). */

import type { QuotaPool } from "./cooldown.ts";

interface AffinityEntry {
  pool: QuotaPool;
  account: number;
  lastUsedAt: number;
}

/** Affinity expires after 2 hours of inactivity. */
const TTL_MS = 2 * 3600_000;
/** Cleanup stale entries every 10 minutes. */
const CLEANUP_INTERVAL_MS = 10 * 60_000;

class AffinityStore {
  private map = new Map<string, AffinityEntry>();
  private counts = new Map<string, number>();
  private cleanupTimer: Timer | null = null;

  private key(threadId: string, ampProvider: string): string {
    return `${threadId}\0${ampProvider}`;
  }

  private countKey(pool: QuotaPool, account: number): string {
    return `${pool}:${account}`;
  }

  private incCount(pool: QuotaPool, account: number): void {
    const k = this.countKey(pool, account);
    this.counts.set(k, (this.counts.get(k) ?? 0) + 1);
  }

  private decCount(pool: QuotaPool, account: number): void {
    const k = this.countKey(pool, account);
    const v = (this.counts.get(k) ?? 0) - 1;
    if (v <= 0) this.counts.delete(k);
    else this.counts.set(k, v);
  }

  private removeExpired(k: string, entry: AffinityEntry): void {
    this.map.delete(k);
    this.decCount(entry.pool, entry.account);
  }

  /** Read affinity without side effects. Returns undefined if expired or missing. */
  peek(threadId: string, ampProvider: string): AffinityEntry | undefined {
    const k = this.key(threadId, ampProvider);
    const entry = this.map.get(k);
    if (!entry) return undefined;
    if (Date.now() - entry.lastUsedAt > TTL_MS) {
      this.removeExpired(k, entry);
      return undefined;
    }
    return entry;
  }

  /** Read affinity and touch (extend TTL). */
  get(threadId: string, ampProvider: string): AffinityEntry | undefined {
    const entry = this.peek(threadId, ampProvider);
    if (entry) entry.lastUsedAt = Date.now();
    return entry;
  }

  set(threadId: string, ampProvider: string, pool: QuotaPool, account: number): void {
    const k = this.key(threadId, ampProvider);
    const existing = this.map.get(k);
    if (existing) {
      if (existing.pool !== pool || existing.account !== account) {
        this.decCount(existing.pool, existing.account);
        this.incCount(pool, account);
      }
    } else {
      this.incCount(pool, account);
    }
    this.map.set(k, { pool, account, lastUsedAt: Date.now() });
  }

  /** Break affinity when account is exhausted — allow re-routing. */
  clear(threadId: string, ampProvider: string): void {
    const k = this.key(threadId, ampProvider);
    const existing = this.map.get(k);
    if (existing) {
      this.decCount(existing.pool, existing.account);
      this.map.delete(k);
    }
  }

  /** Count active threads pinned to a specific (pool, account). */
  activeCount(pool: QuotaPool, account: number): number {
    return this.counts.get(this.countKey(pool, account)) ?? 0;
  }

  /** Start periodic cleanup of expired entries. Call once at server startup. */
  startCleanup(): void {
    if (this.cleanupTimer) return;
    this.cleanupTimer = setInterval(() => {
      const now = Date.now();
      for (const [k, entry] of this.map) {
        if (now - entry.lastUsedAt > TTL_MS) {
          this.removeExpired(k, entry);
        }
      }
    }, CLEANUP_INTERVAL_MS);
  }

  reset(): void {
    this.map.clear();
    this.counts.clear();
    if (this.cleanupTimer) {
      clearInterval(this.cleanupTimer);
      this.cleanupTimer = null;
    }
  }
}

/** Singleton instance for production use. */
export const affinity = new AffinityStore();

```

## File: src\routing\cooldown.ts
```
/** Per-(quotaPool, account) cooldown tracking.
 *  Distinguishes short burst 429s from quota exhaustion. */

import { logger } from "../utils/logger.ts";

export type QuotaPool = "anthropic" | "codex" | "google";

interface CooldownEntry {
  until: number;
  exhausted: boolean;
  consecutive429: number;
}

/** When detected as exhausted, cooldown for this long. */
/** 403 = account disabled/revoked — long cooldown. */
const FORBIDDEN_COOLDOWN_MS = 24 * 3600_000;
const EXHAUSTED_COOLDOWN_MS = 2 * 3600_000;
/** Retry-After threshold (seconds) above which we consider quota exhausted. */
const EXHAUSTED_THRESHOLD_S = 300;
/** Consecutive 429 count to trigger exhaustion detection. */
const EXHAUSTED_CONSECUTIVE = 3;
/** Default burst cooldown when no Retry-After header. */
const DEFAULT_BURST_S = 30;

class CooldownTracker {
  private entries = new Map<string, CooldownEntry>();

  private key(pool: QuotaPool, account: number): string {
    return `${pool}:${account}`;
  }

  private getEntry(pool: QuotaPool, account: number): CooldownEntry | undefined {
    const k = this.key(pool, account);
    const entry = this.entries.get(k);
    if (!entry) return undefined;
    if (Date.now() >= entry.until) {
      this.entries.delete(k);
      return undefined;
    }
    return entry;
  }

  isCoolingDown(pool: QuotaPool, account: number): boolean {
    return this.getEntry(pool, account) !== undefined;
  }

  isExhausted(pool: QuotaPool, account: number): boolean {
    return this.getEntry(pool, account)?.exhausted ?? false;
  }

  record429(pool: QuotaPool, account: number, retryAfterSeconds?: number): void {
    const k = this.key(pool, account);
    const entry = this.entries.get(k) ?? { until: 0, exhausted: false, consecutive429: 0 };

    entry.consecutive429++;
    const retryAfter = retryAfterSeconds ?? DEFAULT_BURST_S;

    if (retryAfter > EXHAUSTED_THRESHOLD_S || entry.consecutive429 >= EXHAUSTED_CONSECUTIVE) {
      entry.exhausted = true;
      entry.until = Date.now() + EXHAUSTED_COOLDOWN_MS;
      logger.warn(`Quota exhausted: ${k}`, { cooldownMinutes: EXHAUSTED_COOLDOWN_MS / 60_000 });
    } else {
      entry.until = Date.now() + retryAfter * 1000;
      logger.debug(`Burst cooldown: ${k}`, { retryAfterSeconds: retryAfter });
    }

    this.entries.set(k, entry);
  }

  /** 403 = account forbidden/revoked. Immediately disable for 24h. */
  record403(pool: QuotaPool, account: number): void {
    const k = this.key(pool, account);
    this.entries.set(k, { until: Date.now() + FORBIDDEN_COOLDOWN_MS, exhausted: true, consecutive429: 0 });
    logger.warn(`Account disabled (403): ${k}`, { cooldownHours: FORBIDDEN_COOLDOWN_MS / 3600_000 });
  }

  /** Return shortest remaining wait (ms) among non-exhausted entries for the given candidates.
   *  Returns undefined if no candidates are cooling down or all are exhausted. */
  shortestBurstWait(candidates: { pool: QuotaPool; account: number }[]): number | undefined {
    let shortest: number | undefined;
    const now = Date.now();
    for (const c of candidates) {
      const entry = this.entries.get(this.key(c.pool, c.account));
      if (!entry || entry.exhausted) continue;
      const remaining = entry.until - now;
      if (remaining > 0 && (shortest === undefined || remaining < shortest)) {
        shortest = remaining;
      }
    }
    return shortest;
  }

  recordSuccess(pool: QuotaPool, account: number): void {
    this.entries.delete(this.key(pool, account));
  }

  reset(): void {
    this.entries.clear();
  }
}

/** Singleton instance for production use. */
export const cooldown = new CooldownTracker();

/** Parse Retry-After header (seconds or HTTP-date). */
export function parseRetryAfter(header: string | null): number | undefined {
  if (!header) return undefined;
  const seconds = Number(header);
  if (!Number.isNaN(seconds)) return seconds;
  const date = Date.parse(header);
  if (!Number.isNaN(date)) return Math.max(0, Math.ceil((date - Date.now()) / 1000));
  return undefined;
}

```

## File: src\routing\retry.ts
```
/** Retry logic: cache-preserving wait + reroute after retryable failures (429/403). */

import type { ProxyConfig } from "../config/config.ts";
import type { ParsedBody } from "../server/body.ts";
import { logger } from "../utils/logger.ts";
import { cooldown, parseRetryAfter, type QuotaPool } from "./cooldown.ts";
import { buildCandidates, type RouteResult, recordSuccess, reroute } from "./router.ts";

/** Max reroute attempts before falling back to upstream. */
const MAX_REROUTE_ATTEMPTS = 4;
/** Max seconds to wait-and-retry on the same account (preserves prompt cache). */
const CACHE_PRESERVE_WAIT_MAX_S = 10;
/** Max ms to wait when all candidates are burst-cooling before giving up. */
const BURST_WAIT_MAX_MS = 30_000;

/** Status codes that trigger rerouting to a different account/pool. */
const REROUTABLE_STATUSES = new Set([429, 403]);

interface RerouteContext {
  providerName: string;
  ampModel: string | null;
  config: ProxyConfig;
  sub: string;
  body: ParsedBody;
  headers: Headers;
  rewrite: ((data: string) => string) | undefined;
  threadId?: string;
}

/** Wait briefly and retry on the same account to preserve prompt cache (429 only). */
export async function tryWithCachePreserve(
  route: RouteResult,
  sub: string,
  body: ParsedBody,
  headers: Headers,
  rewrite: ((data: string) => string) | undefined,
  initialResponse: Response,
): Promise<Response | null> {
  const retryAfter = parseRetryAfter(initialResponse.headers.get("retry-after"));
  if (retryAfter === undefined || retryAfter > CACHE_PRESERVE_WAIT_MAX_S) return null;

  logger.debug(`Waiting ${retryAfter}s to preserve prompt cache on account=${route.account}`);
  await Bun.sleep(retryAfter * 1000);
  const response = await route.handler!.forward(sub, body, headers, rewrite, route.account);

  if (response.status !== 429 && response.status !== 403 && response.status !== 401) {
    recordSuccess(route.pool!, route.account);
    return response;
  }
  if (response.status === 429) {
    const nextRetryAfter = parseRetryAfter(response.headers.get("retry-after"));
    cooldown.record429(route.pool!, route.account, nextRetryAfter);
  }
  if (response.status === 403) {
    cooldown.record403(route.pool!, route.account);
  }
  return null;
}

/** Reroute to different accounts/pools after a retryable failure (429/403). */
export async function tryReroute(
  ctx: RerouteContext,
  initialRoute: RouteResult,
  status: number,
): Promise<Response | null> {
  recordFailure(initialRoute.pool!, initialRoute.account, status);

  let currentPool = initialRoute.pool!;
  let currentAccount = initialRoute.account;

  for (let attempt = 0; attempt < MAX_REROUTE_ATTEMPTS; attempt++) {
    let next = reroute(ctx.providerName, ctx.ampModel, ctx.config, currentPool, currentAccount, ctx.threadId);

    // All candidates cooling down — wait for shortest burst then retry
    if (!next?.handler) {
      const candidates = buildCandidates(ctx.providerName, ctx.config);
      const waitMs = cooldown.shortestBurstWait(candidates);
      if (waitMs && waitMs <= BURST_WAIT_MAX_MS) {
        logger.info(`All accounts cooling, waiting ${Math.ceil(waitMs / 1000)}s for burst cooldown`);
        await Bun.sleep(waitMs + 100); // small buffer
        next = reroute(ctx.providerName, ctx.ampModel, ctx.config, currentPool, currentAccount, ctx.threadId);
      }
    }

    if (!next?.handler) break;

    logger.info(`REROUTE (${status}) -> ${next.decision} account=${next.account}`);
    const response = await next.handler.forward(ctx.sub, ctx.body, ctx.headers, ctx.rewrite, next.account);

    if (REROUTABLE_STATUSES.has(response.status) && next.pool) {
      recordFailure(next.pool, next.account, response.status);
      currentPool = next.pool;
      currentAccount = next.account;
      continue;
    }

    if (response.status !== 401) {
      if (next.pool) recordSuccess(next.pool, next.account);
      return response;
    }
    break;
  }

  return null;
}

/** Record the appropriate cooldown based on status code. */
function recordFailure(pool: QuotaPool, account: number, status: number): void {
  if (status === 403) {
    cooldown.record403(pool, account);
  } else {
    cooldown.record429(pool, account);
  }
}

```

## File: src\routing\router.ts
```
/**
 * Route decision: local provider (free) or Amp upstream (paid).
 *
 * Multi-account aware:
 * - Thread affinity: same thread sticks to same account
 * - Cooldown: skip 429'd accounts, detect quota exhaustion
 * - Least-connections: prefer accounts with fewer active threads
 * - Google: single pool with internal strategy fallback (gemini/antigravity)
 */

import type { ProviderName } from "../auth/store.ts";
import * as store from "../auth/store.ts";
import type { ProxyConfig } from "../config/config.ts";
import { provider as anthropic } from "../providers/anthropic.ts";
import type { Provider } from "../providers/base.ts";
import { provider as codex } from "../providers/codex.ts";
import { provider as google } from "../providers/google.ts";
import { logger, type RouteDecision } from "../utils/logger.ts";
import { affinity } from "./affinity.ts";
import { cooldown, type QuotaPool } from "./cooldown.ts";

interface ProviderEntry {
  provider: Provider;
  pool: QuotaPool;
  credentialName: ProviderName;
}

/** Maps ampProvider name → list of provider entries (checked against config at lookup time). */
const PROVIDER_REGISTRY = new Map<string, { configKey: keyof ProxyConfig["providers"]; entries: ProviderEntry[] }>([
  [
    "anthropic",
    {
      configKey: "anthropic",
      entries: [{ provider: anthropic, pool: "anthropic", credentialName: "anthropic" }],
    },
  ],
  [
    "openai",
    {
      configKey: "codex",
      entries: [{ provider: codex, pool: "codex", credentialName: "codex" }],
    },
  ],
  [
    "google",
    {
      configKey: "google",
      entries: [{ provider: google, pool: "google", credentialName: "google" }],
    },
  ],
]);

/** Reverse map: QuotaPool → Provider (built once at module init). */
const POOL_TO_PROVIDER = new Map<QuotaPool, Provider>();
for (const [, { entries }] of PROVIDER_REGISTRY) {
  for (const entry of entries) {
    POOL_TO_PROVIDER.set(entry.pool, entry.provider);
  }
}

export interface RouteResult {
  decision: RouteDecision;
  provider: string;
  model: string;
  handler: Provider | null;
  account: number;
  pool: QuotaPool | null;
}

interface Candidate {
  provider: Provider;
  pool: QuotaPool;
  account: number;
}

export function routeRequest(
  ampProvider: string,
  model: string | null,
  config: ProxyConfig,
  threadId?: string,
): RouteResult {
  const modelStr = model ?? "unknown";

  // Early exit if provider is disabled in config
  const reg = PROVIDER_REGISTRY.get(ampProvider);
  if (!reg || !config.providers[reg.configKey]) {
    logger.route("AMP_UPSTREAM", ampProvider, modelStr);
    return result(null, ampProvider, modelStr, 0, null);
  }

  // Check thread affinity (keyed by threadId + ampProvider)
  if (threadId) {
    const pinned = affinity.get(threadId, ampProvider);
    if (pinned && !cooldown.isExhausted(pinned.pool, pinned.account)) {
      const handler = providerForPool(pinned.pool);
      if (handler?.isAvailable(pinned.account)) {
        if (!cooldown.isCoolingDown(pinned.pool, pinned.account)) {
          logger.route(handler.routeDecision, ampProvider, modelStr);
          return result(handler, ampProvider, modelStr, pinned.account, pinned.pool);
        }
        // Burst cooldown — still pinned but cooling, let it fall through to find alternative
      }
    }
    // Affinity broken (exhausted / unavailable) — clear and re-route
    if (pinned) affinity.clear(threadId, ampProvider);
  }

  // Build candidate list
  const candidates = buildCandidates(ampProvider, config);
  if (candidates.length === 0) {
    logger.route("AMP_UPSTREAM", ampProvider, modelStr);
    return result(null, ampProvider, modelStr, 0, null);
  }

  // Pick best candidate: not cooling down, least active threads
  const picked = pickCandidate(candidates);
  if (!picked) {
    logger.route("AMP_UPSTREAM", ampProvider, modelStr);
    return result(null, ampProvider, modelStr, 0, null);
  }

  // Pin thread affinity
  if (threadId) affinity.set(threadId, ampProvider, picked.pool, picked.account);

  logger.route(picked.provider.routeDecision, ampProvider, modelStr);
  return result(picked.provider, ampProvider, modelStr, picked.account, picked.pool);
}

/** Record a failure on the current account and pick the next candidate.
 *  Caller is responsible for recording the failure (429/403) on cooldown before calling. */
export function reroute(
  ampProvider: string,
  model: string | null,
  config: ProxyConfig,
  failedPool: QuotaPool,
  failedAccount: number,
  threadId?: string,
): RouteResult | null {
  if (threadId && cooldown.isExhausted(failedPool, failedAccount)) {
    affinity.clear(threadId, ampProvider);
  }

  const modelStr = model ?? "unknown";
  const candidates = buildCandidates(ampProvider, config);
  const picked = pickCandidate(candidates);

  if (!picked) return null;

  if (threadId) affinity.set(threadId, ampProvider, picked.pool, picked.account);
  logger.route(picked.provider.routeDecision, ampProvider, modelStr);
  return result(picked.provider, ampProvider, modelStr, picked.account, picked.pool);
}

/** Record a successful response — clears cooldown. */
export function recordSuccess(pool: QuotaPool, account: number): void {
  cooldown.recordSuccess(pool, account);
}

export function buildCandidates(ampProvider: string, config: ProxyConfig): Candidate[] {
  const reg = PROVIDER_REGISTRY.get(ampProvider);
  if (!reg || !config.providers[reg.configKey]) return [];

  const candidates: Candidate[] = [];
  for (const entry of reg.entries) {
    addAccountCandidates(candidates, entry.provider, entry.pool, entry.credentialName);
  }
  return candidates;
}

function addAccountCandidates(
  candidates: Candidate[],
  provider: Provider,
  pool: QuotaPool,
  providerName: ProviderName,
): void {
  for (const { account, credentials } of store.getAll(providerName)) {
    if (credentials.refreshToken) {
      candidates.push({ provider, pool, account });
    }
  }
}

function pickCandidate(candidates: Candidate[]): Candidate | null {
  // Filter out cooling-down accounts
  const available = candidates.filter((c) => !cooldown.isCoolingDown(c.pool, c.account));
  if (available.length === 0) return null;

  // Pick the one with least active threads (least-connections)
  // When multiple candidates have the same load, pick randomly for even distribution
  let bestLoad = affinity.activeCount(available[0]!.pool, available[0]!.account);
  let ties: Candidate[] = [available[0]!];

  for (let i = 1; i < available.length; i++) {
    const load = affinity.activeCount(available[i]!.pool, available[i]!.account);
    if (load < bestLoad) {
      bestLoad = load;
      ties = [available[i]!];
    } else if (load === bestLoad) {
      ties.push(available[i]!);
    }
  }

  return ties[Math.floor(Math.random() * ties.length)]!;
}

function providerForPool(pool: QuotaPool): Provider | null {
  return POOL_TO_PROVIDER.get(pool) ?? null;
}

function result(
  handler: Provider | null,
  provider: string,
  model: string,
  account: number,
  pool: QuotaPool | null,
): RouteResult {
  const decision: RouteDecision = handler?.routeDecision ?? "AMP_UPSTREAM";
  return { decision, provider, model, handler, account, pool };
}

```

## File: src\server\body.ts
```
/** Request body — lazy parsing with regex fast path.
 *  Fast path: regex extracts model + stream flag without JSON.parse.
 *  Slow path: full JSON.parse only when .parsed or .forwardBody is accessed
 *  (e.g. Google CCA wrapping, model rewrite). */

import { resolveModel, rewriteBodyModel } from "../utils/models.ts";
import * as path from "../utils/path.ts";

export interface ParsedBody {
  /** Original raw body string (for upstream fallback). */
  readonly raw: string;
  /** Amp model name from body.model (before mapping). */
  readonly ampModel: string | null;
  /** Whether body.stream === true. */
  readonly stream: boolean;
  /** Body string to send to provider (re-serialized only if model was remapped). */
  readonly forwardBody: string;
  /** Parsed JSON object — lazy, only materialized when accessed (Google CCA wrapping). */
  readonly parsed: Record<string, unknown> | null;
}

/** Fast-path regex to extract "model" and "stream" without JSON.parse. */
const MODEL_RE = /"model"\s*:\s*"([^"]+)"/;
const STREAM_RE = /"stream"\s*:\s*true\b/;

export function parseBody(raw: string, sub: string): ParsedBody {
  const fallbackModel = path.modelFromUrl(sub);
  if (!raw) return { raw, parsed: null, ampModel: fallbackModel, stream: false, forwardBody: raw };

  const ampModel = raw.match(MODEL_RE)?.[1] ?? fallbackModel;
  const stream = STREAM_RE.test(raw);
  const providerModel = ampModel ? resolveModel(ampModel) : null;
  const needsRewrite = !!(ampModel && providerModel && providerModel !== ampModel);

  let _parsed: Record<string, unknown> | null | undefined;
  function ensureParsed(): Record<string, unknown> | null {
    if (_parsed === undefined) {
      try {
        _parsed = JSON.parse(raw) as Record<string, unknown>;
      } catch {
        _parsed = null;
      }
    }
    return _parsed;
  }

  let _forwardBody: string | undefined;
  function ensureForwardBody(): string {
    if (_forwardBody === undefined) {
      if (needsRewrite) {
        const p = ensureParsed();
        _forwardBody = p ? rewriteBodyModel(p, providerModel!) : raw;
      } else {
        _forwardBody = raw;
      }
    }
    return _forwardBody;
  }

  return {
    raw,
    ampModel,
    stream,
    get parsed() {
      return ensureParsed();
    },
    get forwardBody() {
      return ensureForwardBody();
    },
  };
}

```

## File: src\server\server.ts
```
/** HTTP server — routes provider requests through local OAuth or Amp upstream. */

import { maybeShowAd } from "../cli/ads.ts";
import type { ProxyConfig } from "../config/config.ts";
import * as rewriter from "../proxy/rewriter.ts";
import * as upstream from "../proxy/upstream.ts";
import { affinity } from "../routing/affinity.ts";
import { tryReroute, tryWithCachePreserve } from "../routing/retry.ts";
import { recordSuccess, routeRequest } from "../routing/router.ts";
import { handleInternal, isLocalMethod } from "../tools/internal.ts";
import { logger } from "../utils/logger.ts";
import * as path from "../utils/path.ts";
import { apiError } from "../utils/responses.ts";
import { stats } from "../utils/stats.ts";
import { type ParsedBody, parseBody } from "./body.ts";

export function startServer(config: ProxyConfig): ReturnType<typeof Bun.serve> {
  const server = Bun.serve({
    port: config.port,
    hostname: config.hostname,
    idleTimeout: 255, // seconds — LLM streaming responses can take minutes

    async fetch(req) {
      const startTime = Date.now();
      const url = new URL(req.url);
      let status = 500;
      try {
        const response = await handle(req, url, config);
        status = response.status;
        return response;
      } catch (err) {
        logger.error("Unhandled server error", { error: String(err) });
        return apiError(status, "Internal proxy error");
      } finally {
        logger.info(`${req.method} ${url.pathname}${url.search} ${status}`, { duration: Date.now() - startTime });
      }
    },
  });

  affinity.startCleanup();
  logger.info(`ampcode-connector listening on http://${config.hostname}:${config.port}`);

  const shutdown = () => {
    logger.info("Shutting down...");
    server.stop();
    process.exit(0);
  };

  process.on("SIGTERM", shutdown);
  process.on("SIGINT", shutdown);

  return server;
}

async function handle(req: Request, url: URL, config: ProxyConfig): Promise<Response> {
  const { pathname, search } = url;

  if ((pathname === "/" || pathname === "/status") && req.method === "GET") {
    return healthCheck(config);
  }

  if (path.browser(pathname)) {
    const target = new URL(pathname + search, config.ampUpstreamUrl);
    return Response.redirect(target.toString(), 302);
  }

  if (path.passthrough(pathname)) {
    if (pathname.startsWith("/api/internal") && isLocalMethod(search)) {
      return handleInternal(req, search, config);
    }
    return upstream.forward(req, config.ampUpstreamUrl, config.ampApiKey);
  }

  const providerName = path.provider(pathname);
  if (providerName) return handleProvider(req, providerName, pathname, config);

  return upstream.forward(req, config.ampUpstreamUrl, config.ampApiKey);
}

async function handleProvider(
  req: Request,
  providerName: string,
  pathname: string,
  config: ProxyConfig,
): Promise<Response> {
  const startTime = Date.now();
  const sub = path.subpath(pathname);
  const threadId = req.headers.get("x-amp-thread-id") ?? req.headers.get("x-session-id") ?? undefined;

  const rawBody = req.method === "POST" ? await req.text() : "";
  const body = parseBody(rawBody, sub);
  const ampModel = body.ampModel;
  const route = routeRequest(providerName, ampModel, config, threadId);

  logger.info(
    `ROUTE ${route.decision} provider=${providerName} model=${ampModel ?? "?"} account=${route.account} sub=${sub}`,
  );

  let response: Response;

  if (route.handler) {
    const rewrite = ampModel ? rewriter.rewrite(ampModel) : undefined;
    const handlerResponse = await route.handler.forward(sub, body, req.headers, rewrite, route.account);

    if (
      (handlerResponse.status === 429 || handlerResponse.status === 403 || handlerResponse.status === 404) &&
      route.pool
    ) {
      const ctx = { providerName, ampModel, config, sub, body, headers: req.headers, rewrite, threadId };
      // 429: try short wait to preserve prompt cache first
      const cached =
        handlerResponse.status === 429
          ? await tryWithCachePreserve(route, sub, body, req.headers, rewrite, handlerResponse)
          : null;
      if (cached) {
        response = cached;
      } else {
        const rerouted = await tryReroute(ctx, route, handlerResponse.status);
        response = rerouted ?? (await fallbackUpstream(req, body, config));
      }
    } else if (handlerResponse.status === 401) {
      logger.debug("Local provider denied, falling back to upstream");
      response = await fallbackUpstream(req, body, config);
    } else {
      if (route.pool) recordSuccess(route.pool, route.account);
      response = handlerResponse;
    }
  } else {
    response = await fallbackUpstream(req, body, config);
  }

  stats.record({
    timestamp: new Date().toISOString(),
    route: route.decision,
    provider: providerName,
    model: ampModel ?? "unknown",
    statusCode: response.status,
    durationMs: Date.now() - startTime,
  });

  maybeShowAd();

  return response;
}

/** Fall back to Amp upstream when local providers fail. */
function fallbackUpstream(req: Request, body: ParsedBody, config: ProxyConfig): Promise<Response> {
  const upstreamReq = new Request(req.url, {
    method: req.method,
    headers: req.headers,
    body: body.raw || undefined,
  });
  return upstream.forward(upstreamReq, config.ampUpstreamUrl, config.ampApiKey);
}

function healthCheck(config: ProxyConfig): Response {
  return Response.json({
    status: "ok",
    service: "ampcode-connector",
    port: config.port,
    upstream: config.ampUpstreamUrl,
    providers: config.providers,
    stats: stats.snapshot(),
  });
}

```

## File: src\tools\internal.ts
```
/** Dispatcher for /api/internal?{method} — routes to local handlers or upstream. */

import type { ProxyConfig } from "../config/config.ts";
import * as upstream from "../proxy/upstream.ts";
import { logger } from "../utils/logger.ts";
import { handleWebRead } from "./web-read.ts";
import { handleSearch } from "./web-search.ts";

interface HandlerContext {
  params: Record<string, unknown>;
  config: ProxyConfig;
  forward: () => Promise<Response>;
}

type Handler = (ctx: HandlerContext) => Promise<Response>;

const handlers: Record<string, Handler> = {
  extractWebPageContent: async ({ params }) => {
    const url = str(params, "url");
    if (!url) return error("invalid-params", "missing 'url'");
    return json(
      await handleWebRead({ url, objective: str(params, "objective"), forceRefetch: bool(params, "forceRefetch") }),
    );
  },

  webSearch2: async ({ params, config, forward }) => {
    if (!config.exaApiKey) {
      logger.warn("webSearch2: no exaApiKey configured, forwarding upstream");
      return forward();
    }
    const objective = str(params, "objective");
    if (!objective) return error("invalid-params", "missing 'objective'");
    return handleSearch(
      { objective, searchQueries: strArray(params, "searchQueries"), maxResults: num(params, "maxResults") },
      config.exaApiKey,
    ).then(json, (err) => {
      logger.warn("webSearch2 local failed, falling back to upstream", { error: String(err) });
      return forward();
    });
  },
};

export function isLocalMethod(search: string): boolean {
  return search.replace("?", "") in handlers;
}

export async function handleInternal(req: Request, search: string, config: ProxyConfig): Promise<Response> {
  const method = search.replace("?", "");
  const body = req.method === "POST" ? await req.text() : "";

  let params: Record<string, unknown>;
  try {
    params = JSON.parse(body).params ?? {};
  } catch {
    return error("invalid-body", "Invalid JSON body");
  }

  logger.info(`[INTERNAL] ${method} params=${JSON.stringify(params).slice(0, 200)}`);

  const forward = () => {
    const rebuilt = new Request(req.url, { method: req.method, headers: req.headers, body: body || undefined });
    return upstream.forward(rebuilt, config.ampUpstreamUrl, config.ampApiKey);
  };

  const handler = handlers[method];
  return handler ? handler({ params, config, forward }) : forward();
}

function str(p: Record<string, unknown>, k: string): string | undefined {
  const v = p[k];
  return typeof v === "string" ? v : undefined;
}

function num(p: Record<string, unknown>, k: string): number | undefined {
  const v = p[k];
  return typeof v === "number" ? v : undefined;
}

function bool(p: Record<string, unknown>, k: string): boolean | undefined {
  const v = p[k];
  return typeof v === "boolean" ? v : undefined;
}

function strArray(p: Record<string, unknown>, k: string): string[] | undefined {
  const v = p[k];
  return Array.isArray(v) && v.every((i: unknown) => typeof i === "string") ? (v as string[]) : undefined;
}

function json(data: unknown): Response {
  return Response.json(data);
}

function error(code: string, message: string): Response {
  return Response.json({ ok: false, error: { code, message } });
}

```

## File: src\tools\web-read.ts
```
/** Local handler for extractWebPageContent — fetches a URL, converts to Markdown, ranks by objective. */

import TurndownService from "turndown";
import { gfm } from "turndown-plugin-gfm";
import { logger } from "../utils/logger.ts";

interface WebReadParams {
  url: string;
  objective?: string;
  forceRefetch?: boolean;
}

type WebReadResult =
  | { ok: true; result: { excerpts: string[] } | { fullContent: string } }
  | { ok: false; error: { code: string; message: string } };

interface Section {
  heading: string;
  text: string;
  index: number;
}

interface ScoredSection {
  text: string;
  score: number;
  index: number;
}

type FetchOk = { ok: true; body: string; contentType: string };
type FetchErr = WebReadResult & { ok: false };

const FETCH = {
  TIMEOUT_MS: 30_000,
  USER_AGENT: "Mozilla/5.0 (compatible; AmpBot/1.0)",
} as const;

const CACHE = {
  MAX_ENTRIES: 50,
  TTL_MS: 5 * 60 * 1000,
} as const;

const RANKING = {
  MAX_SECTIONS: 10,
  MAX_SECTION_WORDS: 500,
  MIN_KEYWORD_LEN: 3,
  HEADING_BOOST: 2,
  BIGRAM_BOOST: 1.5,
  POSITION_DECAY: 0.1,
  BM25_K1: 1.5,
  BM25_B: 0.75,
} as const;

const CLIPPING = {
  MAX_BYTES: 262_144, // 256 KB — CLI truncation limit
  MIN_TAIL_BYTES: 100,
  EXCERPT_SEP_BYTES: 2, // "\n\n" separator
} as const;

const turndown = new TurndownService({ headingStyle: "atx", codeBlockStyle: "fenced" });
turndown.use(gfm);
turndown.remove(["script", "style", "img"]);

// biome-ignore format: compact
const STOP_WORDS = new Set(
  ("the and for are but not you all can her was one our out " +
  "has have had been from this that with they which their will " +
  "each make like just over such than them very some what about " +
  "into more other then these when where how does also after " +
  "should would could being there before between those through while using").split(" "),
);

const encoder = new TextEncoder();
const decoder = new TextDecoder("utf-8", { fatal: false });

const cache = new Map<string, { markdown: string; createdAt: number }>();

function getCached(url: string): string | undefined {
  const entry = cache.get(url);
  if (!entry) return undefined;

  if (Date.now() - entry.createdAt > CACHE.TTL_MS) {
    cache.delete(url);
    return undefined;
  }

  // Re-insert to promote as most-recent (LRU)
  cache.delete(url);
  cache.set(url, entry);
  return entry.markdown;
}

function setCache(url: string, markdown: string): void {
  if (cache.size >= CACHE.MAX_ENTRIES) {
    const oldest = cache.keys().next().value!;
    cache.delete(oldest);
  }
  cache.set(url, { markdown, createdAt: Date.now() });
}

export async function handleWebRead({ url, objective, forceRefetch }: WebReadParams): Promise<WebReadResult> {
  let markdown = forceRefetch ? undefined : getCached(url);

  if (!markdown) {
    const page = await fetchPage(url);
    if (!page.ok) return page;
    markdown = convertToMarkdown(page.body, page.contentType);
    setCache(url, markdown);
  }

  if (objective) {
    return { ok: true, result: { excerpts: rankExcerpts(markdown, objective) } };
  }
  return { ok: true, result: { fullContent: clipText(markdown) } };
}

async function fetchPage(url: string): Promise<FetchOk | FetchErr> {
  let response: Response;
  try {
    response = await fetch(url, {
      signal: AbortSignal.timeout(FETCH.TIMEOUT_MS),
      redirect: "follow",
      headers: { "User-Agent": FETCH.USER_AGENT },
    });
  } catch (error) {
    logger.warn("web-read fetch failed", { url, error: String(error) });
    return fetchError(`Failed to fetch ${url}: ${String(error)}`);
  }

  if (!response.ok) {
    return fetchError(`HTTP ${response.status} from ${url}`);
  }

  const body = await response.text();
  const contentType = response.headers.get("content-type") ?? "";
  return { ok: true, body, contentType };
}

function fetchError(message: string): FetchErr {
  return { ok: false, error: { code: "fetch-error", message } };
}

function convertToMarkdown(raw: string, contentType: string): string {
  if (contentType.includes("text/html") || contentType.includes("application/xhtml")) {
    return turndown.turndown(raw);
  }

  if (contentType.includes("application/json")) {
    try {
      return `\`\`\`json\n${JSON.stringify(JSON.parse(raw), null, 2)}\n\`\`\``;
    } catch {
      return raw;
    }
  }

  return raw;
}

function rankExcerpts(markdown: string, objective: string): string[] {
  const sections = splitSections(markdown);
  if (!sections.length) return [clipText(markdown)];
  const { unigrams, bigrams } = parseTerms(objective);
  if (!unigrams.length) return [clipText(markdown)];
  const unigramPatterns = unigrams.map((w) => new RegExp(`\\b${RegExp.escape(w)}\\b`, "g"));
  const idfWeights = computeIdf(sections, unigramPatterns);
  const avgDocLen = sections.reduce((sum, s) => sum + (s.text.split(/\s+/).length || 1), 0) / sections.length;
  const totalSections = sections.length;
  const scored = sections.map((section) =>
    scoreSection(section, unigramPatterns, bigrams, idfWeights, avgDocLen, totalSections),
  );
  const hits = scored.filter((s) => s.score > 0);
  if (!hits.length) return [clipText(markdown)];
  hits.sort((a, b) => b.score - a.score || a.index - b.index);
  const top = hits.slice(0, RANKING.MAX_SECTIONS);
  top.sort((a, b) => a.index - b.index);
  return clipMany(top.map((s) => s.text));
}

function parseTerms(objective: string): { unigrams: string[]; bigrams: RegExp[] } {
  const words = objective
    .toLowerCase()
    .split(/\W+/)
    .filter((word) => word.length >= RANKING.MIN_KEYWORD_LEN && !STOP_WORDS.has(word));

  const bigrams = words
    .slice(0, -1)
    .map((word, i) => new RegExp(`\\b${RegExp.escape(word)}\\W+${RegExp.escape(words[i + 1]!)}\\b`));

  return { unigrams: words, bigrams };
}

function computeIdf(sections: Section[], patterns: RegExp[]): number[] {
  const lowerTexts = sections.map((section) => section.text.toLowerCase());
  const totalSections = sections.length;
  return patterns.map((pattern) => {
    const docFreq = lowerTexts.filter((text) => {
      pattern.lastIndex = 0;
      return pattern.test(text);
    }).length;
    return docFreq > 0 ? Math.log((totalSections - docFreq + 0.5) / (docFreq + 0.5) + 1) : 0;
  });
}

function scoreSection(
  section: Section,
  unigramPatterns: RegExp[],
  bigrams: RegExp[],
  idfWeights: number[],
  avgDocLen: number,
  totalSections: number,
): ScoredSection {
  const lowerText = section.text.toLowerCase();
  const lowerHeading = section.heading.toLowerCase();
  const docLen = lowerText.split(/\s+/).length || 1;

  // BM25 scoring
  const { BM25_K1: k1, BM25_B: b } = RANKING;
  let score = 0;
  for (let i = 0; i < unigramPatterns.length; i++) {
    const pattern = unigramPatterns[i]!;
    pattern.lastIndex = 0;
    const matches = lowerText.match(pattern);
    if (matches) {
      const tf = matches.length;
      score += idfWeights[i]! * ((tf * (k1 + 1)) / (tf + k1 * (1 - b + b * (docLen / avgDocLen))));
    }
  }
  // Bigram bonus
  for (const pattern of bigrams) {
    if (pattern.test(lowerText)) score *= RANKING.BIGRAM_BOOST;
  }

  // Heading match boost (reuse pre-compiled patterns)
  if (section.heading) {
    if (
      unigramPatterns.some((pattern) => {
        pattern.lastIndex = 0;
        return pattern.test(lowerHeading);
      })
    ) {
      score *= RANKING.HEADING_BOOST;
    }
  }

  // Position decay — earlier sections get mild boost
  score *= 1 + RANKING.POSITION_DECAY * (1 - section.index / totalSections);
  return { text: section.text, score, index: section.index };
}

function splitSections(markdown: string): Section[] {
  const raw = parseHeadingSections(markdown);
  return chunkOversizedSections(raw);
}

function parseHeadingSections(markdown: string): Section[] {
  const sections: Section[] = [];
  let heading = "";
  let body: string[] = [];

  const flush = () => {
    const joined = body.join("\n").trim();
    if (heading || joined) {
      const text = heading ? `${heading}\n${joined}` : joined;
      sections.push({ heading, text, index: sections.length });
    }
  };

  for (const line of markdown.split("\n")) {
    if (/^#{1,6}\s/.test(line)) {
      flush();
      heading = line;
      body = [];
    } else {
      body.push(line);
    }
  }
  flush();

  return sections;
}

function chunkOversizedSections(sections: Section[]): Section[] {
  const result: Section[] = [];

  for (const section of sections) {
    const wordCount = section.text.split(/\s+/).length;
    if (wordCount <= RANKING.MAX_SECTION_WORDS) {
      result.push({ ...section, index: result.length });
      continue;
    }

    const paragraphs = section.text.split(/\n{2,}/);
    let chunk: string[] = [];
    let chunkWords = 0;

    for (const paragraph of paragraphs) {
      const paraWords = paragraph.split(/\s+/).length;
      if (chunkWords + paraWords > RANKING.MAX_SECTION_WORDS && chunk.length > 0) {
        result.push({ heading: section.heading, text: chunk.join("\n\n"), index: result.length });
        chunk = [];
        chunkWords = 0;
      }
      chunk.push(paragraph);
      chunkWords += paraWords;
    }

    if (chunk.length > 0) {
      result.push({ heading: section.heading, text: chunk.join("\n\n"), index: result.length });
    }
  }

  return result;
}

function clipText(text: string): string {
  const bytes = encoder.encode(text);
  if (bytes.length <= CLIPPING.MAX_BYTES) return text;
  return decoder.decode(bytes.slice(0, CLIPPING.MAX_BYTES)).replace(/\uFFFD+$/, "");
}

function clipMany(excerpts: string[]): string[] {
  let usedBytes = 0;
  const result: string[] = [];

  for (const excerpt of excerpts) {
    const excerptBytes = encoder.encode(excerpt).length + CLIPPING.EXCERPT_SEP_BYTES;
    if (usedBytes + excerptBytes > CLIPPING.MAX_BYTES) {
      const remaining = CLIPPING.MAX_BYTES - usedBytes;
      if (remaining > CLIPPING.MIN_TAIL_BYTES) result.push(clipText(excerpt));
      break;
    }
    result.push(excerpt);
    usedBytes += excerptBytes;
  }

  return result.length > 0 ? result : [clipText(excerpts[0]!)];
}

```

## File: src\tools\web-search.ts
```
/** Local handler for webSearch2 — searches via Exa API. */

import Exa from "exa-js";
import { logger } from "../utils/logger.ts";

let _exa: InstanceType<typeof Exa> | null = null;
let _exaKey: string | null = null;

function getExa(apiKey: string): InstanceType<typeof Exa> {
  if (!_exa || _exaKey !== apiKey) {
    _exa = new Exa(apiKey);
    _exaKey = apiKey;
  }
  return _exa;
}

interface SearchParams {
  objective: string;
  searchQueries?: string[];
  maxResults?: number;
}

interface SearchResultItem {
  title: string;
  url: string;
  excerpts: string[];
}

interface SearchResponse {
  ok: true;
  result: { results: SearchResultItem[]; showParallelAttribution: boolean };
}

export async function handleSearch(params: SearchParams, exaApiKey: string): Promise<SearchResponse> {
  const { objective, searchQueries, maxResults = 5 } = params;
  const query = searchQueries?.length ? searchQueries.join(" ") : objective;

  const exa = getExa(exaApiKey);
  const response = await exa.search(query, {
    numResults: maxResults,
    type: "auto",
    contents: {
      highlights: { query: objective },
    },
  });

  const results: SearchResultItem[] = response.results.map((r) => ({
    title: r.title ?? "",
    url: r.url,
    excerpts: r.highlights?.length ? r.highlights : [],
  }));

  logger.info(`[SEARCH] Exa returned ${results.length} results for "${query.slice(0, 80)}"`);
  return { ok: true, result: { results, showParallelAttribution: false } };
}

```

## File: src\types\turndown-plugin-gfm.d.ts
```
declare module "turndown-plugin-gfm" {
  import type TurndownService from "turndown";
  export function gfm(service: TurndownService): void;
  export function tables(service: TurndownService): void;
  export function strikethrough(service: TurndownService): void;
  export function taskListItems(service: TurndownService): void;
  export function highlightedCodeBlock(service: TurndownService): void;
}

```

## File: src\utils\browser.ts
```
/** Cross-platform: macOS (open), Linux (xdg-open), Windows (start). */
export async function open(url: string): Promise<boolean> {
  const commands: Record<string, string[]> = {
    darwin: ["open", url],
    linux: ["xdg-open", url],
    win32: ["cmd", "/c", "start", url],
  };

  const cmd = commands[process.platform];
  if (!cmd) return false;

  try {
    const proc = Bun.spawn(cmd);
    await proc.exited;
    return true;
  } catch {
    return false;
  }
}

```

## File: src\utils\code-assist.ts
```
/** Cloud Code Assist request/URL helpers shared by Gemini CLI and Antigravity. */

interface WrapOptions {
  projectId: string;
  model: string;
  body: Record<string, unknown>;
  userAgent: "antigravity" | "pi-coding-agent";
  requestIdPrefix: "agent" | "pi";
  requestType?: "agent" | "image_gen";
}

/** Wrap a raw request body in the Cloud Code Assist envelope. */
function wrapRequest(opts: WrapOptions): string {
  const isImageGen = opts.requestType === "image_gen";
  const requestId = isImageGen
    ? `image_gen/${Date.now()}/${crypto.randomUUID()}/12`
    : `${opts.requestIdPrefix}-${Date.now()}-${crypto.randomUUID().slice(0, 8)}`;

  return JSON.stringify({
    project: opts.projectId,
    model: opts.model,
    request: opts.body,
    ...(opts.requestType && { requestType: opts.requestType }),
    userAgent: opts.userAgent,
    requestId,
  });
}

/** Build the Cloud Code Assist URL for a given action. Preserves the original action
 *  (generateContent vs streamGenerateContent). Only adds ?alt=sse for streaming actions. */
export function buildUrl(endpoint: string, action: string): string {
  const streaming = action.toLowerCase().includes("stream");
  return `${endpoint}/v1internal:${action}${streaming ? "?alt=sse" : ""}`;
}

/** Unwrap Cloud Code Assist SSE envelope: {"response":{...},"traceId":"..."} → inner response.
 *  Returns empty string for [DONE] sentinel (Google SDK doesn't expect it). */
export function unwrap(data: string): string {
  if (data === "[DONE]") return "";
  try {
    const parsed = JSON.parse(data) as { response?: unknown };
    if (parsed.response !== undefined) return JSON.stringify(parsed.response);
    return data;
  } catch {
    return data;
  }
}

/** Chain CCA unwrap with an optional rewrite function. */
export function withUnwrap(rewrite?: (d: string) => string): (d: string) => string {
  return rewrite ? (d: string) => rewrite(unwrap(d)) : unwrap;
}

/** Ensure every function_response part has a non-empty name.
 *  Gemini API rejects requests where function_response.name is empty.
 *  Uses two strategies:
 *  1. Positional: a model turn with N functionCall parts is followed by a user turn
 *     with N functionResponse parts in the same order — match by index.
 *  2. ID-based fallback: match function_response.id → function_call.id.
 *  Handles both camelCase (functionCall) and snake_case (function_call) keys. */
function fixFunctionResponseNames(body: Record<string, unknown>): void {
  const contents = body.contents;
  if (!Array.isArray(contents)) return;

  type Part = Record<string, unknown>;
  type Content = { role?: string; parts?: Part[] };
  const getFc = (p: Part) => (p.functionCall ?? p.function_call) as Record<string, unknown> | undefined;
  const getFr = (p: Part) => (p.functionResponse ?? p.function_response) as Record<string, unknown> | undefined;

  // Pass 1: positional matching — pair consecutive model/user turns
  for (let i = 0; i < contents.length - 1; i++) {
    const modelTurn = contents[i] as Content;
    const userTurn = contents[i + 1] as Content;
    if (modelTurn.role !== "model" || userTurn.role !== "user") continue;
    if (!Array.isArray(modelTurn.parts) || !Array.isArray(userTurn.parts)) continue;

    const fcParts = modelTurn.parts.filter((p) => getFc(p as Part));
    const frParts = userTurn.parts.filter((p) => getFr(p as Part));
    if (fcParts.length === 0 || fcParts.length !== frParts.length) continue;

    for (let j = 0; j < frParts.length; j++) {
      const fr = getFr(frParts[j] as Part)!;
      if (typeof fr.name === "string" && fr.name) continue;
      const fc = getFc(fcParts[j] as Part)!;
      if (typeof fc.name === "string") {
        fr.name = fc.name;
      }
    }
  }

  // Pass 2: ID-based fallback for any remaining empty names
  const nameById = new Map<string, string>();
  for (const content of contents) {
    const parts = (content as Content)?.parts;
    if (!Array.isArray(parts)) continue;
    for (const part of parts) {
      const fc = getFc(part as Part);
      if (fc && typeof fc.name === "string" && typeof fc.id === "string") {
        nameById.set(fc.id, fc.name);
      }
    }
  }

  if (nameById.size === 0) return;

  for (const content of contents) {
    const parts = (content as Content)?.parts;
    if (!Array.isArray(parts)) continue;
    for (const part of parts) {
      const fr = getFr(part as Part);
      if (!fr || (typeof fr.name === "string" && fr.name)) continue;
      const resolved = typeof fr.id === "string" ? nameById.get(fr.id) : undefined;
      if (resolved) {
        fr.name = resolved;
      }
    }
  }
}

/** Wrap body in CCA envelope if not already wrapped. */
export function maybeWrap(
  parsed: Record<string, unknown> | null,
  raw: string,
  projectId: string,
  model: string,
  opts: {
    userAgent: "antigravity" | "pi-coding-agent";
    requestIdPrefix: "agent" | "pi";
    requestType?: "agent" | "image_gen";
  },
): string {
  if (!parsed) return raw;
  if (parsed.project) return raw;
  fixFunctionResponseNames(parsed);
  return wrapRequest({ projectId, model, body: parsed, ...opts });
}

```

## File: src\utils\encoding.ts
```
/** Encode bytes to base64url (no padding). */
export function toBase64url(buffer: Uint8Array): string {
  return Buffer.from(buffer).toString("base64url");
}

/** Decode base64url string to bytes. Handles both base64url and standard base64. */
export function fromBase64url(input: string): Uint8Array {
  return new Uint8Array(Buffer.from(input, "base64url"));
}

```

## File: src\utils\logger.ts
```
/** Structured logging with route decision tracking. */

export type RouteDecision = "LOCAL_CLAUDE" | "LOCAL_CODEX" | "LOCAL_GOOGLE" | "AMP_UPSTREAM";

export type LogLevel = "debug" | "info" | "warn" | "error";

interface LogEntry {
  timestamp: string;
  level: LogLevel;
  message: string;
  route?: RouteDecision;
  provider?: string;
  model?: string;
  duration?: number;
  error?: string;
  [key: string]: unknown;
}

const LOG_LEVELS: Record<LogLevel, number> = {
  debug: 0,
  info: 1,
  warn: 2,
  error: 3,
};

const isTTY = !!process.stdout.isTTY;

const RESET = "\x1b[0m";
const DIM = "\x1b[2m";
const GREEN = "\x1b[32m";
const YELLOW = "\x1b[33m";
const RED = "\x1b[31m";

const LEVEL_COLORS: Record<LogLevel, string> = {
  debug: DIM,
  info: "",
  warn: YELLOW,
  error: RED,
};

const ROUTE_COLORS: Record<RouteDecision, string> = {
  LOCAL_CLAUDE: GREEN,
  LOCAL_CODEX: GREEN,
  LOCAL_GOOGLE: GREEN,
  AMP_UPSTREAM: YELLOW,
};

function colorize(text: string, color: string): string {
  if (!isTTY || !color) return text;
  return `${color}${text}${RESET}`;
}

let currentLevel: LogLevel = "info";

export function setLogLevel(level: LogLevel): void {
  currentLevel = level;
}

function shouldLog(level: LogLevel): boolean {
  return LOG_LEVELS[level] >= LOG_LEVELS[currentLevel];
}

function format(entry: LogEntry): string {
  const { timestamp, level, message, route, provider, model, duration, error } = entry;

  const tag = colorize(`[${level.toUpperCase().padEnd(5)}]`, LEVEL_COLORS[level]);
  let line = `${timestamp} ${tag} ${message}`;
  if (route) line += ` route=${colorize(route, ROUTE_COLORS[route])}`;
  if (provider) line += ` provider=${provider}`;
  if (model) line += ` model=${model}`;
  if (duration !== undefined) line += ` duration=${duration}ms`;
  if (error) line += ` error=${error}`;

  return line;
}

type Meta = Partial<Omit<LogEntry, "timestamp" | "level" | "message">>;

function log(level: LogLevel, message: string, meta?: Meta): void {
  if (!shouldLog(level)) return;

  const entry: LogEntry = {
    timestamp: new Date().toISOString(),
    level,
    message,
    ...meta,
  };

  const line = format(entry);

  if (level === "error") {
    console.error(line);
  } else if (level === "warn") {
    console.warn(line);
  } else {
    console.log(line);
  }
}

export const logger = {
  debug: (message: string, meta?: Meta) => log("debug", message, meta),
  info: (message: string, meta?: Meta) => log("info", message, meta),
  warn: (message: string, meta?: Meta) => log("warn", message, meta),
  error: (message: string, meta?: Meta) => log("error", message, meta),

  route(decision: RouteDecision, provider: string, model: string): void {
    log("info", "Route decision", { route: decision, provider, model });
  },
};

```

## File: src\utils\models.ts
```
/** Centralized model name mapping: Amp CLI model → provider API model.
 *  Amp's proxy may use aliased model names that differ from the provider's API.
 *  This module resolves the correct model name and provides the serialized body. */

/** Suffix patterns stripped when forwarding to the real provider API. */
const STRIP_SUFFIXES = ["-api-preview"] as const;

/** Resolve the model name the provider API expects.
 *  Returns the original if no mapping applies. */
export function resolveModel(ampModel: string): string {
  for (const suffix of STRIP_SUFFIXES) {
    if (ampModel.endsWith(suffix)) return ampModel.slice(0, -suffix.length);
  }
  return ampModel;
}

/** Return body string with provider model name substituted.
 *  Shallow-copies parsed to avoid mutating the shared ParsedBody.parsed reference. */
export function rewriteBodyModel(parsed: Record<string, unknown>, providerModel: string): string {
  return JSON.stringify({ ...parsed, model: providerModel });
}

```

## File: src\utils\path.ts
```
/** URL path parsing for Amp CLI provider routes. */

import { browserPrefixes, passthroughExact, passthroughPrefixes } from "../constants.ts";

const PROVIDER_RE = /^\/api\/provider\/([^/]+)/;
const SUBPATH_RE = /^\/api\/provider\/[^/]+(\/.*)/;
const MODEL_RE = /models\/([^/:]+)/;
const GOOGLE_MODEL_RE = /models\/([^/:]+):(\w+)/;

export function passthrough(pathname: string): boolean {
  if ((passthroughExact as readonly string[]).includes(pathname)) return true;
  return passthroughPrefixes.some((prefix) => pathname.startsWith(prefix));
}

export function browser(pathname: string): boolean {
  return browserPrefixes.some((prefix) => pathname === prefix || pathname.startsWith(`${prefix}/`));
}

export function provider(pathname: string): string | null {
  const match = pathname.match(PROVIDER_RE);
  return match?.[1] ?? null;
}

export function subpath(pathname: string): string {
  const match = pathname.match(SUBPATH_RE);
  return match?.[1] ?? pathname;
}

export function modelFromUrl(url: string): string | null {
  const match = url.match(MODEL_RE);
  return match?.[1] ?? null;
}

export function googleModel(url: string): { model: string; action: string } | null {
  const match = url.match(GOOGLE_MODEL_RE);
  if (!match) return null;
  return { model: match[1]!, action: match[2]! };
}

```

## File: src\utils\responses.ts
```
export function apiError(status: number, message: string, type = "api_error"): Response {
  return Response.json({ error: { message, type, code: String(status) } }, { status });
}

```

## File: src\utils\stats.ts
```
/** Request statistics tracking with ring buffer. */

import type { RouteDecision } from "../utils/logger.ts";

export interface RequestEntry {
  timestamp: string;
  route: RouteDecision;
  provider: string;
  model: string;
  statusCode: number;
  durationMs: number;
}

export interface StatsSnapshot {
  totalRequests: number;
  requestsByRoute: Partial<Record<RouteDecision, number>>;
  count429: number;
  averageDurationMs: number;
  uptimeMs: number;
}

export class StatsRecorder {
  private readonly maxEntries: number;
  private buffer: RequestEntry[] = [];
  private writeIndex = 0;
  private totalCount = 0;
  private readonly startedAt = Date.now();

  constructor(maxEntries = 1000) {
    this.maxEntries = maxEntries;
  }

  record(entry: RequestEntry): void {
    if (this.buffer.length < this.maxEntries) {
      this.buffer.push(entry);
    } else {
      this.buffer[this.writeIndex] = entry;
    }
    this.writeIndex = (this.writeIndex + 1) % this.maxEntries;
    this.totalCount++;
  }

  snapshot(): StatsSnapshot {
    const requestsByRoute: Partial<Record<RouteDecision, number>> = {};
    let count429 = 0;
    let totalDuration = 0;

    for (const entry of this.buffer) {
      requestsByRoute[entry.route] = (requestsByRoute[entry.route] ?? 0) + 1;
      if (entry.statusCode === 429) count429++;
      totalDuration += entry.durationMs;
    }

    return {
      totalRequests: this.totalCount,
      requestsByRoute,
      count429,
      averageDurationMs: this.buffer.length > 0 ? totalDuration / this.buffer.length : 0,
      uptimeMs: Date.now() - this.startedAt,
    };
  }

  recentRequests(n: number): RequestEntry[] {
    const count = Math.min(n, this.buffer.length);
    if (count === 0) return [];

    const result: RequestEntry[] = [];
    let idx = (this.writeIndex - count + this.buffer.length) % this.buffer.length;
    for (let i = 0; i < count; i++) {
      result.push(this.buffer[idx]!);
      idx = (idx + 1) % this.buffer.length;
    }
    return result;
  }

  reset(): void {
    this.buffer = [];
    this.writeIndex = 0;
    this.totalCount = 0;
  }
}

/** Singleton instance for production use. */
export const stats = new StatsRecorder();

```

## File: src\utils\streaming.ts
```
/** SSE (Server-Sent Events) stream parsing, encoding, and transformation. */

export interface Chunk {
  event?: string;
  data: string;
  id?: string;
  retry?: number;
}

export function parse(raw: string): Chunk[] {
  const chunks: Chunk[] = [];

  for (const block of raw.split("\n\n")) {
    if (!block.trim()) continue;

    const chunk: Partial<Chunk> = {};
    for (const line of block.split("\n")) {
      if (line.startsWith("event:")) {
        chunk.event = line.slice(6).trim();
      } else if (line.startsWith("data:")) {
        const value = line.slice(5).trimStart();
        chunk.data = chunk.data ? `${chunk.data}\n${value}` : value;
      } else if (line.startsWith("id:")) {
        chunk.id = line.slice(3).trim();
      } else if (line.startsWith("retry:")) {
        const val = parseInt(line.slice(6).trim(), 10);
        if (!Number.isNaN(val)) chunk.retry = val;
      }
    }

    if (chunk.data !== undefined) chunks.push(chunk as Chunk);
  }

  return chunks;
}

export function encode(chunk: Chunk): string {
  let result = "";
  if (chunk.event) result += `event: ${chunk.event}\n`;
  if (chunk.id) result += `id: ${chunk.id}\n`;
  if (chunk.retry !== undefined) result += `retry: ${chunk.retry}\n`;

  for (const line of chunk.data.split("\n")) {
    result += `data: ${line}\n`;
  }

  result += "\n";
  return result;
}

const decoder = new TextDecoder();
const encoder = new TextEncoder();

function transform(source: ReadableStream<Uint8Array>, fn: (data: string) => string): ReadableStream<Uint8Array> {
  let buffer = "";

  const stream = new TransformStream<Uint8Array, Uint8Array>({
    transform(raw, controller) {
      buffer += decoder.decode(raw, { stream: true }).replaceAll("\r\n", "\n");

      const boundary = buffer.lastIndexOf("\n\n");
      if (boundary === -1) return;

      const complete = buffer.slice(0, boundary + 2);
      buffer = buffer.slice(boundary + 2);

      for (const chunk of parse(complete)) {
        chunk.data = fn(chunk.data);
        if (chunk.data) controller.enqueue(encoder.encode(encode(chunk)));
      }
    },

    flush(controller) {
      if (buffer.trim()) {
        for (const chunk of parse(buffer)) {
          chunk.data = fn(chunk.data);
          if (chunk.data) controller.enqueue(encoder.encode(encode(chunk)));
        }
      }
      buffer = "";
    },
  });

  return source.pipeThrough(stream);
}

const SSE_HEADERS: Readonly<Record<string, string>> = {
  "Content-Type": "text/event-stream",
  "Cache-Control": "no-cache",
  Connection: "keep-alive",
};

const forwardedHeaders = [
  "x-request-id",
  "request-id",
  "anthropic-ratelimit-requests-limit",
  "anthropic-ratelimit-requests-remaining",
  "anthropic-ratelimit-tokens-limit",
  "anthropic-ratelimit-tokens-remaining",
  "x-ratelimit-limit-requests",
  "x-ratelimit-remaining-requests",
  "x-ratelimit-limit-tokens",
  "x-ratelimit-remaining-tokens",
] as const;

export function proxy(upstream: Response, rewrite?: (data: string) => string): Response {
  if (!upstream.body) {
    return new Response("No response body", { status: 502 });
  }

  const body = rewrite ? transform(upstream.body, rewrite) : upstream.body;

  const h: Record<string, string> = { ...SSE_HEADERS };
  for (const name of forwardedHeaders) {
    const value = upstream.headers.get(name);
    if (value) h[name] = value;
  }

  return new Response(body, { status: upstream.status, headers: h });
}

```

## File: src\utils\update-check.ts
```
/** Check npm registry for newer versions on startup. */

import { line, s } from "../cli/ansi.ts";

const PACKAGE_NAME = "ampcode-connector";
const REGISTRY_URL = `https://registry.npmjs.org/${PACKAGE_NAME}/latest`;
const TIMEOUT_MS = 3_000;

function currentVersion(): string {
  // Read from package.json at import time
  const pkg = require("../../package.json");
  return pkg.version;
}

async function fetchLatestVersion(): Promise<string | null> {
  try {
    const res = await fetch(REGISTRY_URL, {
      signal: AbortSignal.timeout(TIMEOUT_MS),
    });
    if (!res.ok) return null;
    const data = (await res.json()) as { version: string };
    return data.version;
  } catch {
    return null;
  }
}

function isNewer(latest: string, current: string): boolean {
  const parse = (v: string) => v.split(".").map(Number);
  const [la = 0, lb = 0, lc = 0] = parse(latest);
  const [ca = 0, cb = 0, cc = 0] = parse(current);
  return la > ca || (la === ca && lb > cb) || (la === ca && lb === cb && lc > cc);
}

/** Non-blocking update check — logs a notice if a newer version exists. */
export async function checkForUpdates(): Promise<void> {
  const current = currentVersion();
  const latest = await fetchLatestVersion();

  if (!latest || !isNewer(latest, current)) return;

  line();
  line(`${s.yellow}⬆ Update available${s.reset}  ${s.dim}${current}${s.reset} → ${s.green}${latest}${s.reset}`);
  line(`  Run ${s.cyan}bunx ampcode-connector@latest${s.reset} to update`);
  line();
}

```

## File: tests\code-assist.test.ts
```
/** Integration test: @google/genai SDK → proxy → Google CCA → response.
 *
 *  Proves the proxy correctly translates between Amp CLI's Vertex AI format
 *  and Cloud Code Assist's /v1internal envelope — using the real SDK and real endpoint. */

import { afterAll, beforeAll, describe, expect, test } from "bun:test";
import { GoogleGenAI } from "@google/genai";
import { google } from "../src/auth/configs.ts";
import * as oauth from "../src/auth/oauth.ts";
import * as store from "../src/auth/store.ts";
import { provider as googleProvider } from "../src/providers/google.ts";
import * as rewriter from "../src/proxy/rewriter.ts";
import type { ParsedBody } from "../src/server/body.ts";
import * as path from "../src/utils/path.ts";

let creds: ReturnType<typeof store.get>;

beforeAll(async () => {
  creds = store.get("google");
  if (!creds) throw new Error("No google credentials — run `bun run login` first");
  const freshToken = await oauth.token(google);
  if (!freshToken) throw new Error("Failed to refresh google token");
});

/** Minimal proxy that uses the unified Google provider. */
function proxyServer() {
  return Bun.serve({
    port: 0,
    async fetch(req) {
      const { pathname } = new URL(req.url);
      const sub = path.subpath(pathname);
      const raw = req.method === "POST" ? await req.text() : "";
      const parsed = raw ? (JSON.parse(raw) as Record<string, unknown>) : null;
      const model = (parsed && typeof parsed.model === "string" ? parsed.model : null) ?? path.modelFromUrl(sub);
      const body: ParsedBody = {
        raw,
        parsed,
        ampModel: model,
        stream: parsed?.stream === true,
        forwardBody: raw,
      };
      const rewrite = model ? rewriter.rewrite(model) : undefined;
      return googleProvider.forward(sub, body, req.headers, rewrite);
    },
  });
}

describe("google provider via @google/genai SDK", () => {
  let server: ReturnType<typeof Bun.serve>;
  let client: InstanceType<typeof GoogleGenAI>;

  beforeAll(() => {
    server = proxyServer();
    client = new GoogleGenAI({
      apiKey: "placeholder",
      vertexai: true,
      httpOptions: {
        baseUrl: `http://localhost:${server.port}/api/provider/google`,
        headers: { Authorization: "Bearer test" },
      },
    });
  });

  afterAll(() => server?.stop());

  test("non-streaming generateContent", async () => {
    const result = await client.models.generateContent({
      model: "gemini-3-flash",
      contents: [{ role: "user", parts: [{ text: "Say hi in one word" }] }],
      config: { maxOutputTokens: 500, temperature: 0.1 },
    });

    expect(result.candidates).toBeDefined();
    expect(result.candidates!.length).toBeGreaterThan(0);
    expect(result.text).toBeTruthy();
    expect(result.modelVersion).toContain("gemini");
  });

  test("streaming generateContentStream", async () => {
    const stream = await client.models.generateContentStream({
      model: "gemini-3-flash",
      contents: [{ role: "user", parts: [{ text: "Say hello in one word" }] }],
      config: { maxOutputTokens: 500, temperature: 0.1 },
    });

    let chunks = 0;
    let gotContent = false;
    for await (const chunk of stream) {
      chunks++;
      if (chunk.text) gotContent = true;
    }

    expect(chunks).toBeGreaterThan(0);
    expect(gotContent).toBe(true);
  });
});

describe("direct SDK to CCA rejects Vertex paths", () => {
  test("returns 404 (proves proxy translation is required)", async () => {
    const direct = new GoogleGenAI({
      apiKey: "placeholder",
      vertexai: true,
      httpOptions: {
        baseUrl: "https://cloudcode-pa.googleapis.com",
        headers: { Authorization: `Bearer ${creds!.accessToken}` },
      },
    });

    try {
      await direct.models.generateContent({
        model: "gemini-3-flash",
        contents: [{ role: "user", parts: [{ text: "hi" }] }],
        config: { maxOutputTokens: 10 },
      });
      throw new Error("Should have thrown");
    } catch (e: unknown) {
      expect((e as { status: number }).status).toBe(404);
    }
  });
});

```

## File: tests\forward.test.ts
```
import { afterAll, beforeAll, describe, expect, test } from "bun:test";
import { denied, type ForwardOptions, forward } from "../src/providers/forward.ts";

/** Minimal HTTP server that simulates provider responses. */
const baseUrl = "http://mock.local";
const originalFetch = globalThis.fetch;

// Track requests for assertions
const requests: { url: string; body: string; headers: Record<string, string> }[] = [];

// Configurable response behavior
const nextResponses: Array<{ status: number; body: string; headers?: Record<string, string> } | { error: Error }> = [];

function enqueue(status: number, body: string, headers?: Record<string, string>): void {
  nextResponses.push({ status, body, headers });
}

function enqueueError(error: Error): void {
  nextResponses.push({ error });
}

beforeAll(() => {
  globalThis.fetch = (async (input, init) => {
    const req = input instanceof Request ? input : new Request(String(input), init);
    const body = await req.text();
    const hdrs: Record<string, string> = {};
    req.headers.forEach((v, k) => {
      hdrs[k] = v;
    });
    requests.push({ url: req.url, body, headers: hdrs });

    const next = nextResponses.shift();
    if (!next) return new Response("no mock configured", { status: 500 });
    if ("error" in next) throw next.error;

    return new Response(next.body, {
      status: next.status,
      headers: { "Content-Type": "application/json", ...next.headers },
    });
  }) as typeof fetch;
});

afterAll(() => {
  globalThis.fetch = originalFetch;
});

function opts(overrides?: Partial<ForwardOptions>): ForwardOptions {
  return {
    url: `${baseUrl}/test`,
    body: '{"prompt":"hello"}',
    streaming: false,
    headers: { "Content-Type": "application/json" },
    providerName: "TestProvider",
    ...overrides,
  };
}

function clearRequests(): void {
  requests.length = 0;
  nextResponses.length = 0;
}

describe("forward", () => {
  test("returns successful JSON response", async () => {
    clearRequests();
    enqueue(200, '{"result":"ok"}');

    const res = await forward(opts());
    expect(res.status).toBe(200);
    expect(await res.json()).toEqual({ result: "ok" });
    expect(requests).toHaveLength(1);
    expect(requests[0]!.body).toBe('{"prompt":"hello"}');
  });

  test("retries on 500 and eventually succeeds", async () => {
    clearRequests();
    enqueue(500, "server error");
    enqueue(500, "server error");
    enqueue(200, '{"result":"recovered"}');

    const res = await forward(opts());
    expect(res.status).toBe(200);
    expect(await res.json()).toEqual({ result: "recovered" });
    expect(requests).toHaveLength(3);
  });

  test("retries on fetch error and eventually succeeds", async () => {
    clearRequests();
    enqueueError(new Error("ECONNRESET"));
    enqueue(200, '{"ok":true}');

    const res = await forward(opts());
    expect(res.status).toBe(200);
    expect(requests).toHaveLength(2);
  });

  test("returns error response on non-retryable 4xx", async () => {
    clearRequests();
    enqueue(422, '{"error":"validation"}');

    const res = await forward(opts());
    expect(res.status).toBe(422);
    expect(await res.text()).toBe('{"error":"validation"}');
    expect(requests).toHaveLength(1);
  });

  test("returns 429 without retry (handled at routing layer)", async () => {
    clearRequests();
    enqueue(429, '{"error":"rate limited"}');

    const res = await forward(opts());
    expect(res.status).toBe(429);
    expect(requests).toHaveLength(1);
  });

  test("applies rewrite to non-streaming response", async () => {
    clearRequests();
    enqueue(200, '{"model":"real-model"}');

    const rewrite = (data: string) => data.replace("real-model", "fake-model");
    const res = await forward(opts({ rewrite }));
    expect(res.status).toBe(200);
    expect(await res.text()).toBe('{"model":"fake-model"}');
  });

  test("logs email context on error", async () => {
    clearRequests();
    enqueue(403, '{"error":"forbidden"}');

    const res = await forward(opts({ email: "user@test.com" }));
    expect(res.status).toBe(403);
  });

  test("exhausts retries on persistent 500", async () => {
    clearRequests();
    enqueue(500, "fail");
    enqueue(500, "fail");
    enqueue(500, "fail");
    enqueue(500, "fail"); // attempt 0,1,2,3

    const res = await forward(opts());
    // After MAX_RETRIES (3), the 4th 500 is returned as-is
    expect(res.status).toBe(500);
    expect(requests).toHaveLength(4);
  });

  test("returns actionable Anthropic transport diagnostics after fetch retries are exhausted", async () => {
    clearRequests();
    enqueueError(new Error("ECONNRESET"));
    enqueueError(new Error("ECONNRESET"));
    enqueueError(new Error("ECONNRESET"));
    enqueueError(new Error("ECONNRESET"));

    const res = await forward(
      opts({
        providerName: "Anthropic",
      }),
    );

    expect(res.status).toBe(502);
    const body = (await res.json()) as { error: { message: string; type: string } };
    expect(body.error.type).toBe("connection_error");
    expect(body.error.message).toContain("Anthropic connection error after retries were exhausted.");
    expect(body.error.message).toContain("MTU");
  });
});

describe("denied", () => {
  test("returns 401 with provider name", async () => {
    const res = denied("Anthropic");
    expect(res.status).toBe(401);
    const body = (await res.json()) as { error: { message: string } };
    expect(body.error.message).toContain("Anthropic");
    expect(body.error.message).toContain("login");
  });
});

```

## File: tests\middleware.test.ts
```
import { describe, expect, test } from "bun:test";
import * as path from "../src/utils/path.ts";

describe("path.passthrough", () => {
  test("identifies management routes", () => {
    expect(path.passthrough("/api/internal")).toBe(true);
    expect(path.passthrough("/api/internal/config")).toBe(true);
    expect(path.passthrough("/api/user")).toBe(true);
    expect(path.passthrough("/api/user/profile")).toBe(true);
    expect(path.passthrough("/api/auth")).toBe(true);
    expect(path.passthrough("/api/auth/login")).toBe(true);
    expect(path.passthrough("/api/meta")).toBe(true);
    expect(path.passthrough("/api/telemetry")).toBe(true);
    expect(path.passthrough("/api/threads")).toBe(true);
    expect(path.passthrough("/api/threads/123")).toBe(true);
    expect(path.passthrough("/api/otel")).toBe(true);
    expect(path.passthrough("/api/tab")).toBe(true);
    expect(path.passthrough("/api/durable-thread-workers")).toBe(true);
  });

  test("rejects browser routes (handled separately)", () => {
    expect(path.passthrough("/threads")).toBe(false);
    expect(path.passthrough("/docs")).toBe(false);
    expect(path.passthrough("/settings")).toBe(false);
    expect(path.passthrough("/auth")).toBe(false);
  });

  test("identifies exact match routes", () => {
    expect(path.passthrough("/threads.rss")).toBe(true);
    expect(path.passthrough("/news.rss")).toBe(true);
    expect(path.browser("/threads.rss")).toBe(false);
    expect(path.browser("/news.rss")).toBe(false);
  });

  test("rejects provider routes", () => {
    expect(path.passthrough("/api/provider/anthropic/v1/messages")).toBe(false);
    expect(path.passthrough("/api/provider/openai/v1/chat/completions")).toBe(false);
    expect(path.passthrough("/api/provider/google/v1beta/models")).toBe(false);
  });

  test("rejects root path", () => {
    expect(path.passthrough("/")).toBe(false);
  });
});

describe("path.browser", () => {
  test("identifies auth routes", () => {
    expect(path.browser("/auth")).toBe(true);
    expect(path.browser("/auth/cli-login")).toBe(true);
    expect(path.browser("/auth/sign-in")).toBe(true);
    expect(path.browser("/auth/callback")).toBe(true);
  });

  test("identifies other browser routes", () => {
    expect(path.browser("/threads")).toBe(true);
    expect(path.browser("/threads/abc")).toBe(true);
    expect(path.browser("/docs")).toBe(true);
    expect(path.browser("/docs/api")).toBe(true);
    expect(path.browser("/settings")).toBe(true);
  });

  test("rejects API routes", () => {
    expect(path.browser("/api/internal")).toBe(false);
    expect(path.browser("/api/provider/anthropic/v1/messages")).toBe(false);
  });
});

describe("path.provider", () => {
  test("extracts anthropic", () => {
    expect(path.provider("/api/provider/anthropic/v1/messages")).toBe("anthropic");
  });

  test("extracts openai", () => {
    expect(path.provider("/api/provider/openai/v1/chat/completions")).toBe("openai");
  });

  test("extracts google", () => {
    expect(path.provider("/api/provider/google/v1beta/models/gemini-pro:generateContent")).toBe("google");
  });

  test("extracts other Amp providers (passthrough to upstream)", () => {
    expect(path.provider("/api/provider/xai/v1/chat/completions")).toBe("xai");
    expect(path.provider("/api/provider/cerebras/v1/chat/completions")).toBe("cerebras");
    expect(path.provider("/api/provider/fireworks/v1/chat/completions")).toBe("fireworks");
    expect(path.provider("/api/provider/groq/v1/chat/completions")).toBe("groq");
    expect(path.provider("/api/provider/baseten/v1/chat/completions")).toBe("baseten");
    expect(path.provider("/api/provider/kimi/v1/chat/completions")).toBe("kimi");
  });

  test("returns null for non-provider paths", () => {
    expect(path.provider("/api/internal")).toBeNull();
    expect(path.provider("/")).toBeNull();
    expect(path.provider("/api/user")).toBeNull();
  });
});

describe("path.subpath", () => {
  test("extracts sub-path for anthropic", () => {
    expect(path.subpath("/api/provider/anthropic/v1/messages")).toBe("/v1/messages");
  });

  test("extracts sub-path for openai", () => {
    expect(path.subpath("/api/provider/openai/v1/chat/completions")).toBe("/v1/chat/completions");
  });

  test("extracts sub-path for google", () => {
    expect(path.subpath("/api/provider/google/v1beta/models/gemini-pro:generateContent")).toBe(
      "/v1beta/models/gemini-pro:generateContent",
    );
  });

  test("returns original path if no match", () => {
    expect(path.subpath("/api/internal")).toBe("/api/internal");
  });
});

```

## File: tests\rewriter.test.ts
```
import { describe, expect, test } from "bun:test";
import * as rewriter from "../src/proxy/rewriter.ts";
import * as sse from "../src/utils/streaming.ts";

describe("rewriter.rewrite", () => {
  const rewrite = rewriter.rewrite("claude-opus-4-6");

  test("rewrites model field in JSON data", () => {
    const data = JSON.stringify({ model: "claude-sonnet-4-20250514", content: "hello" });
    const result = rewrite(data);
    const parsed = JSON.parse(result);
    expect(parsed.model).toBe("claude-opus-4-6");
  });

  test("rewrites nested model fields", () => {
    const data = JSON.stringify({
      message: { model: "claude-sonnet-4-20250514", role: "assistant" },
    });
    const result = rewrite(data);
    const parsed = JSON.parse(result);
    expect(parsed.message.model).toBe("claude-opus-4-6");
  });

  test("passes through [DONE] marker", () => {
    expect(rewrite("[DONE]")).toBe("[DONE]");
  });

  test("passes through non-JSON data unchanged", () => {
    expect(rewrite("not json")).toBe("not json");
  });

  test("does not add model field if not present", () => {
    const data = JSON.stringify({ content: "hello", role: "assistant" });
    const result = rewrite(data);
    const parsed = JSON.parse(result);
    expect(parsed.model).toBeUndefined();
  });

  test("suppresses thinking blocks when tool_use is present", () => {
    const data = JSON.stringify({
      content: [
        { type: "thinking", text: "Let me think..." },
        { type: "tool_use", name: "read_file", input: {} },
        { type: "text", text: "Here is the result" },
      ],
    });
    const result = rewrite(data);
    const parsed = JSON.parse(result);
    expect(parsed.content).toHaveLength(2);
    expect(parsed.content[0].type).toBe("tool_use");
    expect(parsed.content[1].type).toBe("text");
  });

  test("keeps thinking blocks when no tool_use", () => {
    const data = JSON.stringify({
      content: [
        { type: "thinking", text: "Let me think..." },
        { type: "text", text: "Here is the result" },
      ],
    });
    const result = rewrite(data);
    const parsed = JSON.parse(result);
    expect(parsed.content).toHaveLength(2);
    expect(parsed.content[0].type).toBe("thinking");
  });
});

describe("sse.parse", () => {
  test("parses single event", () => {
    const chunk = 'data: {"model":"claude"}\n\n';
    const events = sse.parse(chunk);
    expect(events).toHaveLength(1);
    expect(events[0]!.data).toBe('{"model":"claude"}');
  });

  test("parses multiple events", () => {
    const chunk = 'data: {"chunk":1}\n\ndata: {"chunk":2}\n\n';
    const events = sse.parse(chunk);
    expect(events).toHaveLength(2);
  });

  test("parses event with event type", () => {
    const chunk = 'event: message\ndata: {"text":"hi"}\n\n';
    const events = sse.parse(chunk);
    expect(events).toHaveLength(1);
    expect(events[0]!.event).toBe("message");
    expect(events[0]!.data).toBe('{"text":"hi"}');
  });

  test("handles [DONE] marker", () => {
    const chunk = "data: [DONE]\n\n";
    const events = sse.parse(chunk);
    expect(events).toHaveLength(1);
    expect(events[0]!.data).toBe("[DONE]");
  });

  test("ignores empty chunks", () => {
    expect(sse.parse("")).toHaveLength(0);
    expect(sse.parse("\n\n")).toHaveLength(0);
  });
});

describe("sse.encode", () => {
  test("encodes basic data event", () => {
    const encoded = sse.encode({ data: '{"model":"claude"}' });
    expect(encoded).toBe('data: {"model":"claude"}\n\n');
  });

  test("encodes event with type", () => {
    const encoded = sse.encode({ event: "message", data: "hello" });
    expect(encoded).toBe("event: message\ndata: hello\n\n");
  });

  test("encodes multi-line data", () => {
    const encoded = sse.encode({ data: "line1\nline2" });
    expect(encoded).toBe("data: line1\ndata: line2\n\n");
  });
});

```

## File: tests\router.test.ts
```
import { describe, expect, test } from "bun:test";
import { parseBody } from "../src/server/body.ts";
import { resolveModel, rewriteBodyModel } from "../src/utils/models.ts";
import * as path from "../src/utils/path.ts";

describe("path.modelFromUrl", () => {
  test("extracts model from Gemini-style path", () => {
    expect(path.modelFromUrl("/v1beta/models/gemini-pro:generateContent")).toBe("gemini-pro");
  });

  test("extracts model from streaming path", () => {
    expect(path.modelFromUrl("/v1beta/models/gemini-3-flash-preview:streamGenerateContent")).toBe(
      "gemini-3-flash-preview",
    );
  });

  test("returns null for non-matching path", () => {
    expect(path.modelFromUrl("/v1/messages")).toBeNull();
  });

  test("returns null for empty path", () => {
    expect(path.modelFromUrl("")).toBeNull();
  });

  test("extracts from nested model path", () => {
    expect(path.modelFromUrl("/api/v1beta/models/gemini-pro:generateContent")).toBe("gemini-pro");
  });
});

describe("resolveModel", () => {
  test("strips -api-preview suffix", () => {
    expect(resolveModel("gpt-5.3-codex-api-preview")).toBe("gpt-5.3-codex");
  });

  test("leaves normal models unchanged", () => {
    expect(resolveModel("gpt-5.2-codex")).toBe("gpt-5.2-codex");
    expect(resolveModel("claude-opus-4-6")).toBe("claude-opus-4-6");
    expect(resolveModel("gemini-3-pro-preview")).toBe("gemini-3-pro-preview");
  });
});

describe("rewriteBodyModel", () => {
  test("replaces model in body string", () => {
    const parsed = { model: "gpt-5.3-codex-api-preview", stream: true };
    const result = rewriteBodyModel(parsed, "gpt-5.3-codex");
    expect(JSON.parse(result).model).toBe("gpt-5.3-codex");
  });

  test("preserves other fields", () => {
    const parsed = { model: "gpt-5.3-codex-api-preview", messages: [{ role: "user" }], stream: true };
    const result = rewriteBodyModel(parsed, "gpt-5.3-codex");
    const out = JSON.parse(result);
    expect(out.model).toBe("gpt-5.3-codex");
    expect(out.messages).toEqual([{ role: "user" }]);
    expect(out.stream).toBe(true);
  });

  test("does not mutate original parsed object", () => {
    const parsed = { model: "gpt-5.3-codex-api-preview", stream: true };
    rewriteBodyModel(parsed, "gpt-5.3-codex");
    expect(parsed.model).toBe("gpt-5.3-codex-api-preview");
  });
});

describe("parseBody", () => {
  test("extracts model from JSON body", () => {
    const body = parseBody(JSON.stringify({ model: "claude-opus-4-6", stream: true }), "/v1/messages");
    expect(body.ampModel).toBe("claude-opus-4-6");
    expect(body.stream).toBe(true);
    expect(body.forwardBody).toBe(body.raw);
  });

  test("falls back to URL model when body has no model field", () => {
    const body = parseBody(JSON.stringify({ stream: true }), "/v1beta/models/gemini-pro:generateContent");
    expect(body.ampModel).toBe("gemini-pro");
  });

  test("returns null model for empty body", () => {
    const body = parseBody("", "/v1/messages");
    expect(body.ampModel).toBeNull();
    expect(body.stream).toBe(false);
  });

  test("rewrites -api-preview model in forwardBody", () => {
    const raw = JSON.stringify({ model: "gpt-5.3-codex-api-preview", stream: true });
    const body = parseBody(raw, "/v1/chat/completions");
    expect(body.ampModel).toBe("gpt-5.3-codex-api-preview");
    expect(JSON.parse(body.forwardBody).model).toBe("gpt-5.3-codex");
    expect(body.raw).toBe(raw);
  });

  test("handles invalid JSON gracefully", () => {
    const body = parseBody("not json", "/v1/messages");
    expect(body.parsed).toBeNull();
    expect(body.forwardBody).toBe("not json");
  });
});

```


```
