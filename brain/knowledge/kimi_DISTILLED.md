---
id: kimi
type: knowledge
owner: OA_Triage
---
# kimi
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Kimi Code CLI

[![Commit Activity](https://img.shields.io/github/commit-activity/w/MoonshotAI/kimi-cli)](https://github.com/MoonshotAI/kimi-cli/graphs/commit-activity)
[![Checks](https://img.shields.io/github/check-runs/MoonshotAI/kimi-cli/main)](https://github.com/MoonshotAI/kimi-cli/actions)
[![Version](https://img.shields.io/pypi/v/kimi-cli)](https://pypi.org/project/kimi-cli/)
[![Downloads](https://img.shields.io/pypi/dw/kimi-cli)](https://pypistats.org/packages/kimi-cli)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/MoonshotAI/kimi-cli)

[Kimi Code](https://www.kimi.com/code/) | [Documentation](https://moonshotai.github.io/kimi-cli/en/) | [文档](https://moonshotai.github.io/kimi-cli/zh/)

Kimi Code CLI is an AI agent that runs in the terminal, helping you complete software development tasks and terminal operations. It can read and edit code, execute shell commands, search and fetch web pages, and autonomously plan and adjust actions during execution.

## Getting Started

See [Getting Started](https://moonshotai.github.io/kimi-cli/en/guides/getting-started.html) for how to install and start using Kimi Code CLI.

## Key Features

### Shell command mode

Kimi Code CLI is not only a coding agent, but also a shell. You can switch the shell command mode by pressing `Ctrl-X`. In this mode, you can directly run shell commands without leaving Kimi Code CLI.

![](./docs/media/shell-mode.gif)

> [!NOTE]
> Built-in shell commands like `cd` are not supported yet.

### VS Code extension

Kimi Code CLI can be integrated with [Visual Studio Code](https://code.visualstudio.com/) via the [Kimi Code VS Code Extension](https://marketplace.visualstudio.com/items?itemName=moonshot-ai.kimi-code).

![VS Code Extension](./docs/media/vscode.png)

### IDE integration via ACP

Kimi Code CLI supports [Agent Client Protocol] out of the box. You can use it together with any ACP-compatible editor or IDE.

[Agent Client Protocol]: https://github.com/agentclientprotocol/agent-client-protocol

To use Kimi Code CLI with ACP clients, make sure to run Kimi Code CLI in the terminal and send `/login` to complete the login first. Then, you can configure your ACP client to start Kimi Code CLI as an ACP agent server with command `kimi acp`.

For example, to use Kimi Code CLI with [Zed](https://zed.dev/) or [JetBrains](https://blog.jetbrains.com/ai/2025/12/bring-your-own-ai-agent-to-jetbrains-ides/), add the following configuration to your `~/.config/zed/settings.json` or `~/.jetbrains/acp.json` file:

```json
{
  "agent_servers": {
    "Kimi Code CLI": {
      "type": "custom",
      "command": "kimi",
      "args": ["acp"],
      "env": {}
    }
  }
}
```

Then you can create Kimi Code CLI threads in IDE's agent panel.

![](./docs/media/acp-integration.gif)

### Zsh integration

You can use Kimi Code CLI together with Zsh, to empower your shell experience with AI agent capabilities.

Install the [zsh-kimi-cli](https://github.com/MoonshotAI/zsh-kimi-cli) plugin via:

```sh
git clone https://github.com/MoonshotAI/zsh-kimi-cli.git \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/kimi-cli
```

> [!NOTE]
> If you are using a plugin manager other than Oh My Zsh, you may need to refer to the plugin's README for installation instructions.

Then add `kimi-cli` to your Zsh plugin list in `~/.zshrc`:

```sh
plugins=(... kimi-cli)
```

After restarting Zsh, you can switch to agent mode by pressing `Ctrl-X`.

### MCP support

Kimi Code CLI supports MCP (Model Context Protocol) tools.

**`kimi mcp` sub-command group**

You can manage MCP servers with `kimi mcp` sub-command group. For example:

```sh
# Add streamable HTTP server:
kimi mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: ctx7sk-your-key"

# Add streamable HTTP server with OAuth authorization:
kimi mcp add --transport http --auth oauth linear https://mcp.linear.app/mcp

# Add stdio server:
kimi mcp add --transport stdio chrome-devtools -- npx chrome-devtools-mcp@latest

# List added MCP servers:
kimi mcp list

# Remove an MCP server:
kimi mcp remove chrome-devtools

# Authorize an MCP server:
kimi mcp auth linear
```

**Ad-hoc MCP configuration**

Kimi Code CLI also supports ad-hoc MCP server configuration via CLI option.

Given an MCP config file in the well-known MCP config format like the following:

```json
{
  "mcpServers": {
    "context7": {
      "url": "https://mcp.context7.com/mcp",
      "headers": {
        "CONTEXT7_API_KEY": "YOUR_API_KEY"
      }
    },
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```

Run `kimi` with `--mcp-config-file` option to connect to the specified MCP servers:

```sh
kimi --mcp-config-file /path/to/mcp.json
```

### More

See more features in the [Documentation](https://moonshotai.github.io/kimi-cli/en/).

## Development

To develop Kimi Code CLI, run:

```sh
git clone https://github.com/MoonshotAI/kimi-cli.git
cd kimi-cli

make prepare  # prepare the development environment
```

Then you can start working on Kimi Code CLI.

Refer to the following commands after you make changes:

```sh
uv run kimi  # run Kimi Code CLI

make format  # format code
make check  # run linting and type checking
make test  # run tests
make test-kimi-cli  # run Kimi Code CLI tests only
make test-kosong  # run kosong tests only
make test-pykaos  # run pykaos tests only
make build-web  # build the web UI and sync it into the package (requires Node.js/npm)
make build  # build python packages
make build-bin  # build standalone binary
make help  # show all make targets
```

Note: `make build` and `make build-bin` automatically run `make build-web` to embed the web UI.

```

### File: docs\package.json
```json
{
  "name": "kimi-cli-docs",
  "private": true,
  "type": "module",
  "scripts": {
    "sync": "node scripts/sync-changelog.mjs",
    "dev": "npm run sync && vitepress dev",
    "build": "npm run sync && vitepress build",
    "preview": "vitepress preview"
  },
  "devDependencies": {
    "vitepress": "^1.5.0"
  },
  "dependencies": {
    "mermaid": "^11.12.2",
    "vitepress-plugin-llms": "^1.10.0",
    "vitepress-plugin-mermaid": "^2.0.17"
  }
}
```

### File: .pre-commit-config.yaml
```yaml
default_install_hook_types:
  - pre-commit

repos:
  - repo: local
    hooks:
      - id: make-format-kimi-cli
        name: make format-kimi-cli
        entry: make format-kimi-cli
        language: system
        pass_filenames: false
      - id: make-check-kimi-cli
        name: make check-kimi-cli
        entry: make check-kimi-cli
        language: system
        pass_filenames: false

```

### File: AGENTS.md
```md
# Kimi Code CLI

## Quick commands (use uv)

- `make prepare` (sync deps for all workspace packages and install git hooks)
- `make format`
- `make check`
- `make test`
- `make ai-test`
- `make build` / `make build-bin`

If running tools directly, use `uv run ...`.

## Project overview

Kimi Code CLI is a Python CLI agent for software engineering workflows. It supports an interactive
shell UI, ACP server mode for IDE integrations, and MCP tool loading.

## Tech stack

- Python 3.12+ (tooling configured for 3.14)
- CLI framework: Typer
- Async runtime: asyncio
- LLM framework: kosong
- MCP integration: fastmcp
- Logging: loguru
- Package management/build: uv + uv_build; PyInstaller for binaries
- Tests: pytest + pytest-asyncio; lint/format: ruff; types: pyright + ty

## Architecture overview

- **CLI entry**: `src/kimi_cli/cli/__init__.py` (Typer) parses flags (UI mode, agent spec, config, MCP)
  and routes into `KimiCLI` in `src/kimi_cli/app.py`.
- **App/runtime setup**: `KimiCLI.create` loads config (`src/kimi_cli/config.py`), chooses a
  model/provider (`src/kimi_cli/llm.py`), builds a `Runtime` (`src/kimi_cli/soul/agent.py`),
  loads an agent spec, restores `Context`, then constructs `KimiSoul`.
- **Agent specs**: YAML under `src/kimi_cli/agents/` loaded by `src/kimi_cli/agentspec.py`.
  Specs can `extend` base agents, select tools by import path, and register builtin subagent
  types via the `subagents` field. Subagent instances are persisted separately under the session
  directory and can be resumed by `agent_id`. System prompts live alongside specs; builtin args
  include `KIMI_NOW`, `KIMI_WORK_DIR`, `KIMI_WORK_DIR_LS`, `KIMI_AGENTS_MD`, `KIMI_SKILLS`, `KIMI_OS`, `KIMI_SHELL`
  (this file is injected via `KIMI_AGENTS_MD`).
- **Tooling**: `src/kimi_cli/soul/toolset.py` loads tools by import path, injects dependencies,
  and runs tool calls. Built-in tools live in `src/kimi_cli/tools/` (agent, shell, file, web,
  todo, background, dmail, think, plan). MCP tools are loaded via `fastmcp`; CLI management is
  in `src/kimi_cli/mcp.py` and stored in the share dir.
- **Subagents**: `LaborMarket` in `src/kimi_cli/soul/agent.py` registers builtin subagent types.
  The `Agent` tool (`src/kimi_cli/tools/agent/`) creates or resumes subagent instances, while
  `SubagentStore` persists instance metadata, prompts, wire logs, and context under
  `session/subagents/<agent_id>/`.
- **Core loop**: `src/kimi_cli/soul/kimisoul.py` is the main agent loop. It accepts user input,
  handles slash commands (`src/kimi_cli/soul/slash.py`), appends to `Context`
  (`src/kimi_cli/soul/context.py`), calls the LLM (kosong), runs tools, and performs compaction
  (`src/kimi_cli/soul/compaction.py`) when needed.
- **Approvals**: `src/kimi_cli/soul/approval.py` is the tool-facing facade. `ApprovalRuntime`
  in `src/kimi_cli/approval_runtime/` is the session-level source of truth for pending approvals,
  and approval requests are projected onto the root wire stream for Shell/Web style UIs.
- **UI/Wire**: `src/kimi_cli/soul/run_soul` connects `KimiSoul` to a `Wire`
  (`src/kimi_cli/wire/`) so UI loops can stream events. UIs live in `src/kimi_cli/ui/`
  (shell/print/acp/wire).
- **Shell UI**: `src/kimi_cli/ui/shell/` handles interactive TUI input, shell command mode,
  and slash command autocomplete; it is the default interactive experience.
- **Slash commands**: Soul-level commands live in `src/kimi_cli/soul/slash.py`; shell-level
  commands live in `src/kimi_cli/ui/shell/slash.py`. The shell UI exposes both and dispatches
  based on the registry. Standard skills register `/skill:<skill-name>` and load `SKILL.md`
  as a user prompt; flow skills register `/flow:<skill-name>` and execute the embedded flow.

## Major modules and interfaces

- `src/kimi_cli/app.py`: `KimiCLI.create(...)` and `KimiCLI.run(...)` are the main programmatic
  entrypoints; this is what UI layers use.
- `src/kimi_cli/soul/agent.py`: `Runtime` (config, session, builtins), `Agent` (system prompt +
  toolset), and `LaborMarket` (builtin subagent type registry).
- `src/kimi_cli/soul/kimisoul.py`: `KimiSoul.run(...)` is the loop boundary; it emits Wire
  messages and executes tools via `KimiToolset`.
- `src/kimi_cli/soul/context.py`: conversation history + checkpoints; used by DMail for
  checkpointed replies.
- `src/kimi_cli/soul/toolset.py`: load tools, run tool calls, bridge to MCP tools.
- `src/kimi_cli/ui/*`: shell/print/acp frontends; they consume `Wire` messages.
- `src/kimi_cli/wire/*`: event types and transport used between soul and UI.

## Repo map

- `src/kimi_cli/agents/`: built-in agent YAML specs and prompts
- `src/kimi_cli/prompts/`: shared prompt templates
- `src/kimi_cli/soul/`: core runtime/loop, context, compaction, approvals
- `src/kimi_cli/tools/`: built-in tools
- `src/kimi_cli/ui/`: UI frontends (shell/print/acp/wire)
- `src/kimi_cli/acp/`: ACP server components
- `packages/kosong/`, `packages/kaos/`: workspace deps
  + Kosong is an LLM abstraction layer designed for modern AI agent applications.
    It unifies message structures, asynchronous tool orchestration, and pluggable
    chat providers so you can build agents with ease and avoid vendor lock-in.
  + PyKAOS is a lightweight Python library providing an abstraction layer for agents
    to interact with operating systems. File operations and command executions via KAOS
    can be easily switched between local environment and remote systems over SSH.
- `tests/`, `tests_ai/`: test suites
- `klips`: Kimi Code CLI Improvement Proposals

## Conventions and quality

- Python >=3.12 (ty config uses 3.14); line length 100.
- Ruff handles lint + format (rules: E, F, UP, B, SIM, I); pyright + ty for type checks.
- Tests use pytest + pytest-asyncio; files are `tests/test_*.py`.
- CLI entry points: `kimi` / `kimi-cli` -> `src/kimi_cli/__main__.py` (routes to `src/kimi_cli/cli/__init__.py`).
- User config: `~/.kimi/config.toml`; logs, sessions, and MCP config live in `~/.kimi/`.

## Git commit messages

Conventional Commits format:

```
<type>(<scope>): <subject>
```

Allowed types:
`feat`, `fix`, `test`, `refactor`, `chore`, `style`, `docs`, `perf`, `build`, `ci`, `revert`.

## Versioning

The project follows a **minor-bump-only** versioning scheme (`MAJOR.MINOR.PATCH`):

- **Patch** version is always `0`. Never bump it.
- **Minor** version is bumped for any change: new features, improvements, bug fixes, etc.
- **Major** version is only changed by explicit manual decision; it stays unchanged during
  normal development.

Examples: `0.68.0` → `0.69.0` → `0.70.0`; never `0.68.1`.

This rule applies to all packages in the repo (root, `packages/*`, `sdks/*`) as well as release
and skill workflows.

## Release workflow

1. Ensure `main` is up to date (pull latest).
2. Create a release branch, e.g. `bump-0.68` or `bump-pykaos-0.5.3`.
3. Update `CHANGELOG.md`: rename `[Unreleased]` to `[0.68] - YYYY-MM-DD`.
4. Update `pyproject.toml` version.
5. Run `uv sync` to align `uv.lock`.
6. Commit the branch and open a PR.
7. Merge the PR, then switch back to `main` and pull latest.
8. Tag and push:
   - `git tag 0.68` or `git tag pykaos-0.5.3`
   - `git push --tags`
9. GitHub Actions handles the release after tags are pushed.

```

### File: CHANGELOG.md
```md
# Changelog

<!--
Release notes will be parsed and available as /release-notes
The parser extracts for each version:
  - a short description (first paragraph after the version header)
  - bullet entries beginning with "- " under that version (across any subsections)
Internal builds may append content to the Unreleased section.
Only write entries that are worth mentioning to users.
-->

## Unreleased

- Todo: Refactor SetTodoList to persist state and prevent tool call storms — todos are now persisted to session state (root agent) and independent state files (sub-agents); adds query mode (omit `todos` to read current state) and clear mode (pass `[]`); includes anti-storm guidance in tool description to prevent repeated calls without progress (fixes #1710)
- ReadFile: Add total line count to every read response and support negative `line_offset` for tail mode — the tool now reports `Total lines in file: N.` in its message so the model can plan subsequent reads; negative `line_offset` (e.g. `-100`) reads the last N lines using a sliding window, useful for viewing recent log output without shell commands; the absolute value is capped at 1000 (MAX_LINES)
- Shell: Fix black background on inline code and code blocks in Markdown rendering — `NEUTRAL_MARKDOWN_THEME` now overrides all Rich default `markdown.*` styles to `"none"`, preventing Rich's built-in `"cyan on black"` from leaking through on non-black terminals

## 1.30.0 (2026-04-02)

- Shell: Refine idle background completion auto-trigger — resumed shell sessions no longer auto-start a foreground turn from stale pending background notifications before the user sends a message, and fresh background completions now wait briefly while the user is actively typing to avoid stealing the prompt or breaking CJK IME composition
- Core: Fix interrupted foreground turns leaving unbalanced wire events — `TurnEnd` is now emitted even when a turn exits via cancellation or step interruption, preventing dirty session wire logs from accumulating across resume cycles
- Core: Improve session startup resilience — `--continue`/`--resume` now tolerate malformed `context.jsonl` records and corrupted subagent, background-task, or notification artifacts; the CLI skips invalid persisted state where possible instead of failing to restore the session
- CLI: Improve `kimi export` session export UX — `kimi export` now previews the previous session for the current working directory and asks for confirmation, showing the session ID, title, and last user-message time; adds `--yes` to skip confirmation; also fixes explicit session-ID invocations where `--output` after the argument was incorrectly parsed as a subcommand
- Grep: Add `include_ignored` parameter to search files excluded by `.gitignore` — when set to `true`, ripgrep's `--no-ignore` flag is enabled, allowing searches in gitignored artifacts such as build outputs or `node_modules`; sensitive files (like `.env`) remain filtered by the sensitive-file protection layer; defaults to `false` to preserve existing behavior
- Core: Add sensitive file protection to Grep and Read tools — `.env`, SSH private keys (`id_rsa`, `id_ed25519`, `id_ecdsa`), and cloud credentials (`.aws/credentials`, `.gcp/credentials`) are now detected and blocked; Grep filters them from results with a warning, Read rejects them outright; `.env.example`/`.env.sample`/`.env.template` are exempted
- Core: Fix parallel foreground subagent approval requests hanging the session — in interactive shell mode, `_set_active_approval_sink` no longer flushes pending approval requests to the live view sink (which cannot render approval modals); requests stay in the pending queue for the prompt modal path; also adds a 300-second timeout to `wait_for_response` so that any unresolved approval request eventually raises `ApprovalCancelledError` instead of hanging forever
- CLI: Add `--session`/`--resume` (`-S`/`-r`) flag to resume sessions — without an argument opens an interactive session picker (shell UI only); with a session ID resumes that specific session; replaces the reverted `--pick-session`/`--list-sessions` design with a unified optional-value flag
- CLI: Add CJK-safe `shorten()` utility — replaces all `textwrap.shorten` calls so that CJK text without spaces is truncated gracefully instead of collapsing to just the placeholder
- Core: Fix skills in brand directories (e.g. `~/.kimi/skills/`) silently disappearing when a generic directory (`~/.config/agents/skills/`) exists but is empty — skill directory discovery now searches brand and generic directory groups independently and merges both results, instead of stopping at the first existing directory across all candidates
- Core: Add `merge_all_available_skills` config option — when enabled, skills from all existing brand directories (`~/.kimi/skills/`, `~/.claude/skills/`, `~/.codex/skills/`) are loaded and merged instead of using only the first one found; same-name skills follow priority order kimi > claude > codex; disabled by default
- CLI: Add `--plan` flag and `default_plan_mode` config option — start new sessions in plan mode via `kimi --plan` or by setting `default_plan_mode = true` in `~/.kimi/config.toml`; resumed sessions preserve their existing plan mode state
- Shell: Add `/undo` and `/fork` commands for session forking — `/undo` lets you pick a previous turn and fork a new session with the selected message pre-filled for re-editing; `/fork` duplicates the entire session history into a new session; the original session is always preserved
- CLI: Add `-r` as a short alias for `--session` and print a resume hint (`kimi -r <session-id>`) whenever a session exits — covers normal exit, Ctrl-C, `/undo`, `/fork`, and `/sessions` switch so users can always find their way back
- Core: Fix `custom_headers` not being passed to non-Kimi providers — OpenAI, Anthropic, Google GenAI, and Vertex AI providers now correctly forward custom headers configured in `providers.*.custom_headers`

## 1.29.0 (2026-04-01)

- Core: Support hierarchical `AGENTS.md` loading — the CLI now discovers and merges `AGENTS.md` files from the git project root down to the working directory, including `.kimi/AGENTS.md` at each level; deeper files take priority under a 32 KiB budget cap, ensuring the most specific instructions are never truncated
- Core: Fix empty sessions lingering on disk after exit — sessions created but never used are now cleaned up on all exit paths (failure exit, session switch, unexpected errors), not just on successful exit
- Shell: Add `KIMI_CLI_PASTE_CHAR_THRESHOLD` and `KIMI_CLI_PASTE_LINE_THRESHOLD` environment variables to control when pasted text is folded into a placeholder — lowering these thresholds works around CJK input method breakage after multiline paste on some terminals (e.g., XShell over SSH)
- Shell: Fix diff panel rendering corruption on terminals without truecolor support (e.g. Xshell) — `render_to_ansi` no longer hardcodes 24-bit color; Rich now auto-detects terminal capability via `COLORTERM`/`TERM` environment variables
- Web: Fix white screen after CLI upgrade caused by browser caching stale `index.html` — the server now returns `Cache-Control: no-cache` for HTML and `immutable` for hashed assets, preventing 404s on renamed chunks
- Core: Fix file write converting LF to CRLF on Windows — `writetext` now opens files with `newline=""` to prevent Python's universal newline translation from silently converting `\n` to `\r\n`
- Core: Support `socks://` proxy scheme — proxy tools like V2RayN set `ALL_PROXY=socks://...` which httpx/aiohttp don't recognise; the CLI now normalises `socks://` to `socks5://` at startup so all HTTP clients and subprocesses work correctly behind a SOCKS proxy
- Shell: Add `/title` (alias `/rename`) command to manually set session titles — titles are now stored in `state.json` alongside other session state; legacy `metadata.json` is automatically migrated on first load
- Shell: Fix garbled pager output when `MANPAGER` is set (e.g. `bat`) — the console pager now ignores `MANPAGER` and delegates to `pydoc.pager()`, preserving `PAGER` and all platform-specific fallbacks
- Explore: Enhance explore agent with specialist role, thoroughness levels, and automatic environment context — explore agents now gather repository environment information at launch to improve investigation quality; the main agent is guided to prefer explore for codebase research and plan mode encourages explore-first investigation
- Shell: Fix tool call display showing raw OSC 8 escape bytes (e.g. `8;id=391551;https://…`) instead of clean text — hyperlink sequences are now wrapped as zero-width escapes for prompt_toolkit compatibility, preserving clickable links in supported terminals
- Core: Add OS and shell information to the system prompt — the model now knows which platform it is running on and receives a Windows-specific instruction to prefer built-in tools over Shell commands, preventing Linux command errors in PowerShell
- Shell: Fix `command` parameter description saying "bash command" regardless of platform — the description is now platform-neutral
- Web: Fix auto-title overwriting manual session rename — when a user renames a session through the web UI, the new title is now preserved and no longer replaced by the auto-generated title
## 1.28.0 (2026-03-30)

- Core: Fix file write/replace tools freezing the event loop — diff computation (`build_diff_blocks`) is now offloaded to a thread via `asyncio.to_thread`, preventing the UI from hanging when editing large files
- Shell: Fix `_watch_root_wire_hub` silently dying on handler exceptions — the watcher now catches and logs exceptions (matching the pattern in `wire/server.py`) and handles `QueueShutDown` gracefully, preventing approval flow from silently breaking mid-session
- Core: Skip O(n²) diff computation for huge files (>10 000 lines) — files above the threshold now show a summary block instead of computing a full diff, and unchanged files short-circuit immediately
- Wire: Add `is_summary` field to `DiffDisplayBlock` (Wire 1.8) — marks diff blocks that contain a line-count summary instead of actual diff content, allowing clients to render them appropriately
- Web: Render large-file diff summaries — when a diff block is marked `is_summary`, the web UI shows a compact "File too large for inline diff" notice with line counts instead of attempting to compute a diff
- Auth: Fix OAuth users getting "incorrect API KEY" when running skills or after idle — 401 errors now show a clear "please /login" message instead of the raw API error; the ACP layer correctly triggers re-login flow for VS Code extension users
- Web: Fix session title generation always failing for OAuth users — the title generator now uses OAuth tokens and refreshes them before calling the model
- Core: Add timeout protection for Agent tool and HTTP requests — all `aiohttp` sessions now default to 120 s total / 60 s read timeout; the Agent tool gains an optional `timeout` parameter (foreground default 10 min, background default 15 min); background agent tasks are marked `timed_out` on expiry with proper notification semantics
- Grep: Fix tool hanging and becoming uninterruptible — replaced blocking `ripgrepy.run()` with async subprocess execution; the tool now responds to Ctrl-C immediately and has a 20-second timeout with partial result return
- Grep: Add token efficiency improvements — default `head_limit` of 250 with `offset` pagination, `--hidden` search with VCS directory exclusion, `files_with_matches` sorted by modification time, relative path output, and `--max-columns 500` for non-content modes
- Grep: `line_number` (`-n`) now defaults to `true` in content mode — line numbers are included by default so the model can reference precise code locations
- Grep: `count_matches` mode now includes a summary in the message — e.g. "Found 30 total occurrences across 10 files."
- ACP: Fix `ValueError: list.index(x): x not in list` crash when ACP is launched via `kimi-code` or `kimi-cli` entry-points (e.g. JetBrains AI Assistant)
- Core: Fix OpenAI-compatible APIs (e.g. One API) returning 400 errors in multi-turn conversations when the server returns `reasoning_content` by default — `reasoning_effort` is now auto-set to `"medium"` when history contains thinking content and `reasoning_key` is configured
- Shell: Add `/theme` command and dark/light theme support — users with light terminal backgrounds can now switch to a light color palette via `/theme light` or `theme = "light"` in `config.toml`; diff highlights, task browser, prompt UI, and MCP status colors all adapt to the selected theme
- Core: Fix context overflow before compaction — tool result tokens are now estimated and included in the auto-compaction trigger check, preventing "exceeded model token limit" errors when large tool outputs push the context beyond the model limit between API calls
- Core: Add hooks system (Beta) — configure `[[hooks]]` in `config.toml` to run custom shell commands at 13 lifecycle events including `PreToolUse`, `PostToolUse`, `SessionStart`, `Stop`, etc.; supports regex matching, timeout handling, and blocking operations via exit code 2
- Shell: Add `/hooks` command — list all configured hooks with event counts
- Wire: Add `HookTriggered` and `HookResolved` event types (Wire 1.7) — notify clients when hooks start and finish executing, including event type, target, action (allow/block), and duration
- Wire: Add `HookRequest` and `HookResponse` message types — allow wire clients to subscribe to hook events and provide their own handling logic with allow/block decisions
- CLI: `--skills-dir` now supports multiple directories and overrides default discovery — when specified, the directories replace user/project skills discovery (repeatable flag)
- Shell: Fix notification messages leaking into session replay and export — background task notification tags (`<notification>`, `<task-notification>`) are now filtered out when resuming a session (`/sessions`) and when exporting (`/export`) or importing (`/import`) conversation history
- Web: The "Open" button in the workspace header now remembers the last-used application — clicking "Open" directly opens with the previous choice, while the dropdown arrow lets you pick a different app
- Web: Fix archived sessions count badge showing only the loaded page size — the badge now displays "100+" when more archived sessions exist beyond the first page
- Shell: Fix pasted text placeholders not expanded in modal answers — clipboard content pasted into approval or question panels is now correctly interpolated before being sent to the model
- Vis: Add `--network / -n` flag — launch the visualizer on all network interfaces with auto-detected LAN IP display, matching `kimi web` behavior
- Vis: Add `/vis` slash command — switch from the interactive shell to the tracing visualizer in one step, mirroring the existing `/web` command
- Vis: Improve session list performance — async backend scanning, request
... [TRUNCATED]
```

### File: CONTRIBUTING.md
```md
# Contributing to Kimi Code CLI

Thank you for being interested in contributing to Kimi Code CLI!

We welcome all kinds of contributions, including bug fixes, features, document improvements, typo fixes, etc. To maintain a high-quality codebase and user experience, we provide the following guidelines for contributions:

1. We only merge pull requests that align with our roadmap. For any pull request that introduces changes larger than 100 lines of code, we highly recommend discussing with us by [raising an issue](https://github.com/MoonshotAI/kimi-cli/issues) or in an existing issue before you start working on it. Otherwise your pull request may be closed or ignored without review.
2. We insist on high code quality. Please ensure your code is as good as, if not better than, the code written by frontier coding agents. Changes may be requested before your pull request can be merged.

## Prek hooks

We use [prek](https://github.com/j178/prek) to run formatting and checks via git hooks.

Recommended setup:
1. Run `make prepare` to sync dependencies and install the prek hooks.
2. Optionally run on all files before sending a PR: `prek run --all-files`.

Manual setup (if you do not want to use `make prepare`):
1. Install prek (pick one): `uv tool install prek`, `pipx install prek`, or `pip install prek`.
2. Install the hooks in this repo: `prek install`.

After installation, the hooks run on every commit. The repo uses prek workspace mode, so only the
projects with changed files run their hooks. You can skip them for an intermediate commit with
`git commit --no-verify`, or run them manually with `prek run --all-files`.

The hooks execute the relevant `make format-*` and `make check-*` targets, so ensure dependencies
are installed (`make prepare` or `uv sync`).

```

### File: SECURITY.md
```md
# Security Policy

## Supported Versions

Currently, Kimi CLI only provides security support for the latest version.

## Reporting a Vulnerability

Please report a vulnerability via the [MoonshotAI/kimi-cli - Security](https://github.com/MoonshotAI/kimi-cli/security) page, or open an [issue](https://github.com/MoonshotAI/kimi-cli/issues) if it can be published publicly.

```

### File: .github\pr-title-checker-config.json
```json
{
    "LABEL": {
        "name": "Invalid PR Title",
        "color": "B60205"
    },
    "CHECKS": {
        "regexp": "^(feat|fix|test|refactor|chore|style|docs|perf|build|ci|revert)(\\(.*\\))?:.*"
    },
    "MESSAGES": {
        "failure": "The PR title is invalid. Please refer to https://www.conventionalcommits.org/en/v1.0.0/ for the convention."
    }
}

```

### File: .github\pull_request_template.md
```md
<!--
Thank you for your contribution to Kimi Code CLI!
Please make sure you already discussed the feature or bugfix you are proposing in an issue with the maintainers.
Please understand that if you have not gotten confirmation from the maintainers, your pull request may be closed or ignored without further review due to limited bandwidth.

See https://github.com/MoonshotAI/kimi-cli/blob/main/CONTRIBUTING.md for more.
-->

## Related Issue

<!-- Please link to the issue here. -->

Resolve #(issue_number)

## Description

<!-- Please describe your changes in detail. -->

## Checklist

- [ ] I have read the [CONTRIBUTING](https://github.com/MoonshotAI/kimi-cli/blob/main/CONTRIBUTING.md) document.
- [ ] I have linked the related issue, if any.
- [ ] I have added tests that prove my fix is effective or that my feature works.
- [ ] I have run `make gen-changelog` to update the changelog.
- [ ] I have run `make gen-docs` to update the user documentation.

```

### File: docs\.pre-commit-config.yaml
```yaml
orphan: true

# Docs changes do not need pre-commit hooks.
repos: []

```

### File: docs\AGENTS.md
```md
# Documentation Agent Guide

This repository uses VitePress for the documentation site. The current docs are structural scaffolds only; everything beyond the headings is placeholder guidance. The `Reference Code` blocks are there to guide future writing and should be removed once the docs are complete.

## Structure

- Locales live under `docs/en/` and `docs/zh/` with mirrored paths and filenames.
- Main sections (nav + sidebar) are:
  - Guides: getting-started, use-cases, interaction, sessions, ides, integrations
  - Customization: mcp, skills, agents, print-mode, wire-mode
  - Configuration: config-files, providers, overrides, env-vars, data-locations
  - Reference: kimi-command, kimi-acp, kimi-mcp, slash-commands, keyboard, tools, exit-codes
  - FAQ: setup, interaction, acp, mcp, print-wire, updates
  - Release notes: changelog, breaking-changes
- Navigation and sidebar are defined in `docs/.vitepress/config.ts`. Any new or renamed page must be wired there for both locales.

## Source of truth

- **Changelog page**: The English version (`docs/en/release-notes/changelog.md`) is the source of truth. It is auto-synced from the root `CHANGELOG.md` via script. The Chinese changelog should be translated from the English version.
- **All other pages**: The Chinese version (`docs/zh/`) is the source of truth. English translations should be based on the Chinese docs.

Only the Chinese documentation and the English changelog are manually reviewed. Other translations (e.g., English versions of non-changelog pages) may be auto-generated by AI agents.

## Authoring workflow

- Each page is a scaffold: expand the bullets into prose while keeping the section ordering, and keep the `::: info Reference Code` blocks aligned with the relevant section.
- For changelog: edit the root `CHANGELOG.md`, then run `npm run sync` to update the English docs.
- For other pages: edit the Chinese version first, then translate to English.

## Naming conventions

- Filenames are kebab-case and mirror across locales (same slug in `docs/en/` and `docs/zh/`).
- Use consistent section labels that match the sidebar titles.
- Use backticks for flags, commands, subcommands, command arguments, file paths, code identifiers, type names, field names, field values, and keyboard shortcuts.

## Wording conventions

- Do not change H1 titles or nav/sidebar labels.
- English H2+ headings use sentence case (only the first word capitalized unless it is a proper noun). Treat "Wire" as a proper noun; do not treat "agent", "shell mode", or "print mode" as proper nouns.
- Chinese H2+ headings keep English words in sentence case; preserve proper nouns listed in the term table below.
- Use `API key` in English and `API 密钥` in Chinese; keep `JSON`, `JSONL`, `OAuth`, `macOS`, and `uv` as-is.
- Use straight double quotes with spaces for quoted content: `"被引内容"` (not curly quotes). Add a space before and after the quoted text when adjacent to CJK characters. Use corner brackets `「」` for special terms (e.g., `「工具」`, `「会话」`).
- Prefer "终端" over "命令行" in Chinese when both are applicable (e.g., "运行在终端中", "终端界面", "终端操作").
- Use "工具调用" / "tool call", not "工具使用" / "tool use".
- Use inline code for tool names (e.g., `Task`, `ReadFile`, `Shell`).

Term mapping (Chinese <-> English, and proper noun handling):

| Chinese | English | Proper noun (zh) | Proper noun (en) |
| --- | --- | --- | --- |
| Agent | agent | yes | no |
| Shell | shell | yes | no |
| Shell 模式 | shell mode | yes | no |
| Print 模式 | print mode | yes | no |
| Wire 模式 | Wire mode | yes | yes (Wire) |
| Thinking 模式 | thinking mode | yes | no |
| MCP | MCP | yes | yes |
| ACP | ACP | yes | yes |
| Kimi Code CLI | Kimi Code CLI | yes | yes |
| Agent Skills | Agent Skills | yes | yes |
| Skill | skill | yes | no |
| 系统提示词 | system prompt | no | no |
| 提示词 | prompt | no | no |
| 会话 | session | no | no |
| 上下文 | context | no | no |
| 子 Agent | subagent | yes (Agent) | no |
| API 密钥 | API key | yes | no |
| JSON | JSON | yes | yes |
| JSONL | JSONL | yes | yes |
| OAuth | OAuth | yes | yes |
| macOS | macOS | yes | yes |
| uv | uv | yes | yes |
| 审批请求 | approval request | no | no |
| 斜杠命令 | slash command | no | no |
| 工具调用 | tool call | no | no |
| Frontmatter | frontmatter | yes | no |
| User 消息 | user message | yes (User) | no |
| Assistant 消息 | assistant message | yes (Assistant) | no |
| Tool 消息 | tool message | yes (Tool) | no |
| 轮次 | turn | no | no |
| 供应商 | provider | no | no |
| Prompt Flow | Prompt Flow | yes | yes |
| Ralph 循环 | Ralph Loop | yes | yes |
| Diff | diff | yes | no |

JetBrains IDE terminology (Chinese UI translations):

| English | Chinese |
| --- | --- |
| AI Chat | AI 聊天 |
| Registry | 注册表 |
| Configure ACP agents | (未翻译) |

## Typography

- **Spacing around mixed content**: Add a space between Chinese characters and English words, numbers, inline code, or links. Exception: no space before full-width punctuation.
  - ✓ 在 Python 中使用 \`class\` 关键字
  - ✗ 在Python中使用\`class\`关键字
  - ✓ 详见 \[配置文件\](./config.md)。
  - ✗ 详见\[配置文件\](./config.md)。
- **Full-width punctuation**: Use full-width punctuation in Chinese text: `，。；：？！（）` not `, . ; : ? ! ( )`.
- **Code block language**: Always specify language for fenced code blocks (e.g., ` ```sh `, ` ```toml `, ` ```json `). Exception: natural language examples (user prompts) may omit the language.
- **Callout titles**: Use short category titles for callout blocks (`::: tip`, `::: warning`, `::: info`, `::: danger`). Put the detailed description in the block content, not the title.
  - Chinese: use `提示` for tip, `注意` for warning, `说明` for info, `警告` for danger.
  - English: use no title or short words like `Note` for warning.
  - ✓ `::: tip 提示` + content starting with the key point
  - ✓ `::: warning 注意` + content `\`KIMI_SHARE_DIR\` 不影响 Skills 的搜索路径。...`
  - ✗ `::: warning 不影响 Skills` (title too long, should be in content)
  - ✗ `::: tip Skills 路径独立于 KIMI_SHARE_DIR` (title too long)
- **Version info blocks**: For version change callouts, use `::: info` with a category title (Added/Changed/Removed in English; 新增/变更/移除 in Chinese). The content should be a complete sentence.
  - ✓ `::: info 新增` + content `新增于 Wire 1.2。`
  - ✗ `::: info 新增于 Wire 1.2` (title too long)
  - ✓ `::: info Changed` + content `Renamed in Wire 1.1. ...`
  - ✗ `::: info Renamed in Wire 1.1` (title too long)

## Writing style

- **Natural narrative**: Organize content like writing an article, guiding readers smoothly through the material.
- **Avoid fragmentation**: Don't turn every point into a subheading; use paragraph transitions instead.
- **Global perspective**: "Getting Started" introduces core concepts only; detailed usage belongs in later pages.
- **Progressive depth**: Guides → Customization → Configuration → Reference, information deepens gradually.
- **No "next steps"**: VitePress already provides prev/next navigation; don't add manual `::: tip 接下来` blocks at page end.

### Example: good vs bad

Outline prompt:

```
* Install and upgrade
  * System requirements: Python 3.12+, recommend uv
  * Install, upgrade, uninstall steps
```

**Bad** (mechanical conversion to headings):

```markdown
## Install and upgrade

### System requirements

- Python 3.12+
- Recommend uv

### Install

...

### Upgrade

...
```

**Good** (natural narrative):

```markdown
## Install and upgrade

Kimi Code CLI requires Python 3.12+. We recommend using uv for installation and management.

If you haven't installed uv yet, please refer to the uv installation docs first. Install Kimi Code CLI:

(code block)

Verify the installation:

(code block)

Upgrade to the latest version:

(code block)
```

## Build and preview

- Docs are built with VitePress from `docs/`.
- Common commands (run inside `docs/`):
  - `npm install` (or `bun install` if you use bun)
  - `npm run dev`
  - `npm run build`
  - `npm run preview`
- The build output is `docs/.vitepress/dist`.

## Changelog syncing

The English changelog (`docs/en/release-notes/changelog.md`) is auto-generated from the root `CHANGELOG.md`. Do not edit it manually.

- The sync script is `docs/scripts/sync-changelog.mjs`.
- It runs automatically before `npm run dev` and `npm run build`.
- To run manually: `npm run sync` (from the `docs/` directory).
- The script converts title format (`## [0.69] - 2025-12-29` → `## 0.69 (2025-12-29)`) and removes HTML comments.

```

### File: docs\index.md
```md
---
layout: home
hero:
  name: Kimi Code CLI
  text: ' '
  actions:
    - theme: brand
      text: 简体中文
      link: /zh/
    - theme: alt
      text: English
      link: /en/
---

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vitepress'

onMounted(() => {
  const router = useRouter()
  const lang = navigator.language || navigator.userLanguage
  if (lang.startsWith('zh')) {
    router.go('/zh/')
  } else {
    router.go('/en/')
  }
})
</script>

```

### File: scripts\build_vis.py
```py
from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VIS_DIR = ROOT / "vis"
DIST_DIR = VIS_DIR / "dist"
NODE_MODULES = VIS_DIR / "node_modules"
STATIC_DIR = ROOT / "src" / "kimi_cli" / "vis" / "static"


REQUIRED_VIS_TYPE_FILES = (
    NODE_MODULES / "vite" / "client.d.ts",
    NODE_MODULES / "typescript" / "lib" / "typescript.d.ts",
)


def has_required_vis_type_files() -> bool:
    return all(path.is_file() for path in REQUIRED_VIS_TYPE_FILES)


def resolve_npm() -> str | None:
    candidates = ["npm"]
    if os.name == "nt":
        candidates.extend(["npm.cmd", "npm.exe", "npm.bat"])
    for candidate in candidates:
        npm = shutil.which(candidate)
        if npm:
            return npm
    return None


def check_node_version() -> bool:
    """Vite 7 requires Node.js ^20.19.0 || >=22.12.0."""
    node = shutil.which("node")
    if not node:
        return False
    try:
        result = subprocess.run([node, "--version"], capture_output=True, text=True, check=False)
        version = result.stdout.strip().lstrip("v")
        parts = [int(x) for x in version.split(".")[:3]]
        major, minor = parts[0], parts[1] if len(parts) > 1 else 0
        ok = (major == 20 and minor >= 19) or (major >= 22 and (major > 22 or minor >= 12))
        if not ok:
            print(
                f"Node.js ^20.19.0 or >=22.12.0 required (Vite 7), found v{version}",
                file=sys.stderr,
            )
            return False
    except Exception:
        pass
    return True


def run_npm(npm: str, args: list[str]) -> int:
    try:
        result = subprocess.run([npm, *args], check=False)
    except FileNotFoundError:
        print(
            "npm not found or failed to execute. Install Node.js (npm) and ensure it is on PATH.",
            file=sys.stderr,
        )
        return 1
    return result.returncode


def main() -> int:
    npm = resolve_npm()
    if npm is None:
        print("npm not found. Install Node.js (npm) to build the vis UI.", file=sys.stderr)
        return 1

    if not check_node_version():
        return 1

    needs_install = (not NODE_MODULES.exists()) or (not has_required_vis_type_files())
    if needs_install:
        if NODE_MODULES.exists():
            print("vis dependencies are incomplete; reinstalling with devDependencies...")
        returncode = run_npm(npm, ["--prefix", str(VIS_DIR), "ci", "--include=dev"])
        if returncode != 0:
            return returncode

    returncode = run_npm(npm, ["--prefix", str(VIS_DIR), "run", "build"])
    if returncode != 0:
        return returncode

    if not DIST_DIR.exists():
        print("vis/dist not found after build. Check the vis build output.", file=sys.stderr)
        return 1

    if STATIC_DIR.exists():
        shutil.rmtree(STATIC_DIR)
    STATIC_DIR.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(DIST_DIR, STATIC_DIR)

    print(f"Synced vis UI to {STATIC_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

```

### File: scripts\build_web.py
```py
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEB_DIR = ROOT / "web"
DIST_DIR = WEB_DIR / "dist"
NODE_MODULES = WEB_DIR / "node_modules"
STATIC_DIR = ROOT / "src" / "kimi_cli" / "web" / "static"

STRICT_VERSION = os.environ.get("KIMI_WEB_STRICT_VERSION", "").lower() in {"1", "true", "yes"}

REQUIRED_WEB_TYPE_FILES = (
    NODE_MODULES / "vite" / "client.d.ts",
    NODE_MODULES / "@types" / "node" / "index.d.ts",
)


def read_pyproject_version() -> str:
    with (ROOT / "pyproject.toml").open("rb") as handle:
        data = tomllib.load(handle)
    return str(data["project"]["version"])


def find_version_in_dist(version: str) -> bool:
    search_suffixes = {".js", ".css", ".html", ".map"}
    version_with_prefix = f"v{version}"
    found_plain = False

    for path in DIST_DIR.rglob("*"):
        if not path.is_file() or path.suffix not in search_suffixes:
            continue
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if version_with_prefix in content:
            return True
        if version in content:
            found_plain = True

    return found_plain


def resolve_npm() -> str | None:
    candidates = ["npm"]
    if os.name == "nt":
        candidates.extend(["npm.cmd", "npm.exe", "npm.bat"])
    for candidate in candidates:
        npm = shutil.which(candidate)
        if npm:
            return npm
    return None


def run_npm(npm: str, args: list[str]) -> int:
    try:
        result = subprocess.run([npm, *args], check=False)
    except FileNotFoundError:
        print(
            "npm not found or failed to execute. Install Node.js (npm) and ensure it is on PATH.",
            file=sys.stderr,
        )
        return 1
    return result.returncode


def has_required_web_type_files() -> bool:
    return all(path.is_file() for path in REQUIRED_WEB_TYPE_FILES)


def main() -> int:
    npm = resolve_npm()
    if npm is None:
        print("npm not found. Install Node.js (npm) to build the web UI.", file=sys.stderr)
        return 1

    expected_version = read_pyproject_version()
    explicit_expected = os.environ.get("KIMI_WEB_EXPECT_VERSION")
    if explicit_expected and explicit_expected != expected_version:
        print(
            f"web version mismatch: pyproject={expected_version}, expected={explicit_expected}",
            file=sys.stderr,
        )
        return 1

    needs_install = (not NODE_MODULES.exists()) or (not has_required_web_type_files())
    if needs_install:
        if NODE_MODULES.exists():
            print("web dependencies are incomplete; reinstalling with devDependencies...")
        returncode = run_npm(npm, ["--prefix", str(WEB_DIR), "ci", "--include=dev"])
        if returncode != 0:
            return returncode

    returncode = run_npm(npm, ["--prefix", str(WEB_DIR), "run", "build"])
    if returncode != 0:
        return returncode

    if not DIST_DIR.exists():
        print("web/dist not found after build. Check the web build output.", file=sys.stderr)
        return 1
    if STRICT_VERSION and not find_version_in_dist(expected_version):
        print(
            f"web version not found in build output; expected version {expected_version}",
            file=sys.stderr,
        )
        return 1

    if STATIC_DIR.exists():
        shutil.rmtree(STATIC_DIR)
    STATIC_DIR.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(DIST_DIR, STATIC_DIR)

    print(f"Synced web UI to {STATIC_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

```

### File: scripts\check_kimi_dependency_versions.py
```py
from __future__ import annotations

import argparse
import re
import sys
import tomllib
from pathlib import Path


def load_project_table(pyproject_path: Path) -> dict:
    with pyproject_path.open("rb") as handle:
        data = tomllib.load(handle)

    project = data.get("project")
    if not isinstance(project, dict):
        raise ValueError(f"Missing [project] table in {pyproject_path}")

    return project


def load_project_version(pyproject_path: Path) -> str:
    project = load_project_table(pyproject_path)
    version = project.get("version")
    if not isinstance(version, str) or not version:
        raise ValueError(f"Missing project.version in {pyproject_path}")
    return version


def find_pinned_dependency(deps: list[str], name: str) -> str | None:
    pattern = re.compile(rf"^{re.escape(name)}(?:\[[^\]]+\])?(.+)$")
    for dep in deps:
        match = pattern.match(dep)
        if not match:
            continue
        spec = match.group(1)
        pinned = re.match(r"^==(.+)$", spec)
        if pinned:
            return pinned.group(1)
        return None
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate kimi-cli dependency versions.")
    parser.add_argument("--root-pyproject", type=Path, required=True)
    parser.add_argument("--kosong-pyproject", type=Path, required=True)
    parser.add_argument("--pykaos-pyproject", type=Path, required=True)
    args = parser.parse_args()

    try:
        root_project = load_project_table(args.root_pyproject)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    deps = root_project.get("dependencies", [])
    if not isinstance(deps, list):
        print(
            f"error: project.dependencies must be a list in {args.root_pyproject}",
            file=sys.stderr,
        )
        return 1

    errors: list[str] = []
    for name, pyproject_path in (
        ("kosong", args.kosong_pyproject),
        ("pykaos", args.pykaos_pyproject),
    ):
        try:
            package_version = load_project_version(pyproject_path)
        except ValueError as exc:
            errors.append(str(exc))
            continue

        pinned_version = find_pinned_dependency(deps, name)
        if pinned_version is None:
            errors.append(f"Missing pinned dependency for {name} in {args.root_pyproject}.")
            continue

        if pinned_version != package_version:
            errors.append(
                f"{name} version mismatch: root depends on {pinned_version}, "
                f"but {pyproject_path} has {package_version}."
            )

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print("ok: kimi-cli dependencies match workspace package versions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
