---
id: claude-subconscious-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:05.504395
---

# KNOWLEDGE EXTRACT: claude-subconscious
> **Extracted on:** 2026-03-30 13:16:59
> **Source:** claude-subconscious

---

## File: `.gitignore`
```
# Dependencies
node_modules/

# State files (generated at runtime)
.letta/
session-*.json
conversations.json

# Claude Code local state
.claude/

# Other tool configs
.agents/
.codex/
.cursor/
.opencode/

# Evals (internal tooling)
evals/

# Skills (local slash commands)
skills/
.skills/

# Logs
*.log
/tmp/letta-claude-sync/

# TypeScript build output
dist/
*.js
*.js.map
*.d.ts

# OS files
.DS_Store
Thumbs.db

# IDE
.idea/
.vscode/
*.swp
*.swo

# Environment files (contain secrets)
.env
.env.local
.env.*.local
poem_for_claude_code.md
```

## File: `CHANGELOG.md`
```markdown
# Changelog

## [1.1.0] - 2026-01-28

### Added

- **PreToolUse hook for mid-workflow context injection** - New lightweight hook that checks for Letta agent updates before each tool use. Addresses "workflow drift" in long workflows by injecting new messages and memory block diffs mid-stream. Silent no-op if nothing changed.

- **Letta Code GitHub Action** - `@letta-code` can now respond to issues and PRs in this repository.

- **LETTA_BASE_URL support** - Self-hosted Letta servers can now be configured via environment variable.

- **Windows compatibility** - Fixed `npx spawn ENOENT` error on Windows.

- **Linux tmpfs workaround** - Documented workaround for `EXDEV` error when `/tmp` is on a different filesystem.

### Changed

- **Session start sync** - CLAUDE.md now syncs at session start for fresh agent/conversation IDs.

- **Default model** - Changed default agent model to GLM 4.7 (free tier on Letta Cloud).

- **Automatic model detection** - Plugin now queries available models and auto-selects if configured model is unavailable.

### Fixed

- **Plugin install syntax** - Updated README with correct marketplace install commands.

- **Conversation message ordering** - Fixed message fetch to correctly show newest messages first.

- **Conversation URL** - Links now point to agent view with conversation query param.

### Security

- **Sanitized default agent** - Removed user-specific data from bundled `Subconscious.af` file.

---

## [1.0.0] - 2026-01-16

Initial release.

### Features

- Bidirectional sync between Claude Code and Letta agents
- Memory blocks sync to `.claude/CLAUDE.md`
- Session transcripts sent to Letta agent asynchronously
- Conversation isolation per Claude Code session
- Auto-import default Subconscious agent if no agent configured
- Memory block diffs shown on changes
- New messages from Letta agent injected into context

### Hooks

- `SessionStart` - Notify agent of new session
- `UserPromptSubmit` - Sync memory before each prompt
- `Stop` - Send transcript after each response
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Letta, Inc.

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
```

## File: `package.json`
```json
{
  "name": "claude-subconscious",
  "version": "2.0.2",
  "description": "A subconscious for Claude Code. A Letta agent watches your sessions, accumulates context, and whispers guidance back.",
  "author": "Letta <hello@letta.com> (https://letta.com)",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/letta-ai/claude-subconscious.git"
  },
  "homepage": "https://github.com/letta-ai/claude-subconscious#readme",
  "bugs": {
    "url": "https://github.com/letta-ai/claude-subconscious/issues"
  },
  "keywords": [
    "claude",
    "claude-code",
    "letta",
    "subconscious",
    "memory",
    "multi-agent",
    "async",
    "deliberation"
  ],
  "type": "module",
  "engines": {
    "node": ">=18.0.0"
  },
  "scripts": {
    "sync": "tsx scripts/sync_letta_memory.ts",
    "send": "tsx scripts/send_messages_to_letta.ts",
    "test": "vitest run",
    "test:watch": "vitest"
  },
  "dependencies": {
    "@letta-ai/letta-code-sdk": "^0.1.0",
    "tsx": "^4.7.0"
  },
  "devDependencies": {
    "@types/node": "^20.10.0",
    "typescript": "^5.3.0",
    "vitest": "^3.0.0"
  }
}
```

## File: `README.md`
```markdown
> [!IMPORTANT]
> Claude Subconscious is demo app built using the Letta Code SDK, and is not intended to be used in production.
>
> If you want to use a coding agent that runs background subconscious agents, use [**Letta Code**](https://github.com/letta-ai/letta-code), which is also fully open source.
>
> Install the Letta Code CLI with `npm install -g @letta-ai/letta-code`, then use `letta` to launch.

# Claude Subconscious

A background agent that whispers to Claude Code. A subconcious agent that watches your sessions, reads your files, builds up memory over time, and whispers guidance back.

![evil claude](assets/evil-claude.jpeg)

## What Is This?

Claude Code forgets everything between sessions. Claude Subconscious is a second agent running underneath — watching, learning, and whispering back:

- **Watches** every Claude Code session transcript
- **Reads your codebase** — explores files with Read, Grep, and Glob while processing transcripts
- **Remembers** across sessions, projects, and time
- **Whispers guidance** — surfaces context, patterns, and reminders before each prompt
- **Never blocks** — runs in the background via the [Letta Code SDK](https://docs.letta.com/letta-code/sdk/)

Not just a memory layer — a background agent with real tool access that gets smarter the more you use it.

Using Letta's [Conversations](https://docs.letta.com/guides/agents/conversations/) feature, a single agent can serve multiple Claude Code sessions in parallel with shared memory across all of them.

## How It Works

After each response, the transcript is sent to a Letta agent via the Letta Code SDK. The agent reads files, searches the web, updates its memory — then whispers back before the next prompt. Nothing is written to CLAUDE.md.

```
┌─────────────┐          ┌──────────────────────────┐
│ Claude Code │◄────────►│ Letta Agent (background)  │
└─────────────┘          │                          │
       │                 │  Tools: Read, Grep, Glob │
       │                 │  Memory: persistent       │
       │                 │  Web: search, fetch       │
       │                 └──────────────────────────┘
       │                        │
       │   Session Start        │
       ├───────────────────────►│ New session notification
       │                        │
       │   Before each prompt   │
       │◄───────────────────────┤ Whispers guidance → stdout
       │                        │
       │   Before each tool use │
       │◄───────────────────────┤ Mid-workflow updates → stdout
       │                        │
       │   After each response  │
       ├───────────────────────►│ Transcript → SDK session (async)
       │                        │  ↳ Reads files, updates memory
```

## Installation

Install from GitHub:

```
/plugin marketplace add letta-ai/claude-subconscious
/plugin install claude-subconscious@claude-subconscious
```

### Updating

```
/plugin marketplace update
/plugin update claude-subconscious@claude-subconscious
```

### Install from Source

Clone the repository:

```bash
git clone https://github.com/letta-ai/claude-subconscious.git
cd claude-subconscious
npm install
```

Enable the plugin (from inside the cloned directory):

```
/plugin enable .
```

Or enable globally for all projects:

```
/plugin enable --global .
```

If running from a different directory, use the full path to the cloned repo.

### Linux: tmpfs Workaround

If plugin installation fails with `EXDEV: cross-device link not permitted`, your `/tmp` is likely on a different filesystem (common on Ubuntu, Fedora, Arch). Set `TMPDIR` to work around this [Claude Code bug](https://github.com/anthropics/claude-code/issues/14799):

```bash
mkdir -p ~/.claude/tmp
export TMPDIR="$HOME/.claude/tmp"
```

Add to your shell profile (`~/.bashrc` or `~/.zshrc`) to make permanent.

## Configuration

### Required

```bash
export LETTA_API_KEY="your-api-key"
```

Get your API key from [app.letta.com](https://app.letta.com).

### Optional

```bash
export LETTA_MODE="whisper"    # Default. Or "full" for blocks + messages, "off" to disable
export LETTA_AGENT_ID="agent-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
export LETTA_BASE_URL="http://localhost:8283"  # For self-hosted Letta
export LETTA_MODEL="anthropic/claude-sonnet-4-5"  # Model override
export LETTA_CONTEXT_WINDOW="1048576"             # Context window size (e.g. 1M tokens)
export LETTA_HOME="$HOME"      # Consolidate .letta state to ~/.letta/
export LETTA_SDK_TOOLS="read-only"       # Or "full", "off"
```

- `LETTA_MODE` - Controls what gets injected. `whisper` (default, messages only), `full` (blocks + messages), `off` (disable). See [Modes](#modes).
- `LETTA_AGENT_ID` - If not set, the plugin automatically imports a default "Subconscious" agent on first use.
- `LETTA_BASE_URL` - For self-hosted Letta servers. Defaults to `https://api.letta.com`.
- `LETTA_MODEL` - Override the agent's model. Optional - the plugin auto-detects and selects from available models. See [Model Configuration](#model-configuration) below.
- `LETTA_CONTEXT_WINDOW` - Override the agent's context window size (in tokens). Useful when `LETTA_MODEL` is set to a model with a large context window that differs from the server default. Example: `1048576` for 1M tokens.
- `LETTA_HOME` - Base directory for plugin state files. Creates `{LETTA_HOME}/.letta/claude/` for session data and conversation mappings. Defaults to current working directory. Set to `$HOME` to consolidate all state in one location.
- `LETTA_SDK_TOOLS` - Controls client-side tool access for the Subconscious agent. `read-only` (default), `full`, or `off`. See [SDK Tools](#sdk-tools).

### Modes

The `LETTA_MODE` environment variable controls what gets injected into Claude's context:

| Mode | What Claude sees | Use case |
|------|-----------------|----------|
| **`whisper`** (default) | Only messages from Sub | Lightweight — Sub speaks when it has something to say |
| **`full`** | Memory blocks + messages | Full context — blocks on first prompt, diffs after |
| **`off`** | Nothing | Disable hooks temporarily |

Subconscious **never writes to CLAUDE.md** in any mode. All content is injected via stdout into the prompt context. If you have an existing CLAUDE.md with `<letta>` content from an older version, it will be cleaned up automatically.

### Agent Resolution Order

1. **Environment variable** - `LETTA_AGENT_ID` if set
2. **Saved config** - `~/.letta/claude-subconscious/config.json` if exists
3. **Auto-import** - Imports bundled `Subconscious.af` agent, saves ID for future use

This means zero-config setup: just set `LETTA_API_KEY` and the plugin handles the rest.

### Multi-Project Usage

**One agent, many projects.** The Subconscious agent is stored globally at `~/.letta/claude-subconscious/config.json`. When you use the plugin in different repos, they all share the same agent brain.

```
~/.letta/claude-subconscious/config.json  →  ONE agent ID (shared brain)
                                               ↓
project-a/.letta/claude/                  →  Project A's conversation threads
project-b/.letta/claude/                  →  Project B's conversation threads
project-c/.letta/claude/                  →  Project C's conversation threads
```

The `.letta/claude/` directories in each project are **conversation bookkeeping** (mapping Claude Code sessions to Letta conversations), not separate agents. Memory blocks are shared across all projects.

To use a **different agent per project**, set `LETTA_AGENT_ID` in your shell or via [direnv](https://direnv.net/):

```bash
# .envrc in project directory
export LETTA_AGENT_ID="agent-xxx-for-this-project"
```

### Model Configuration

The plugin **automatically detects available models** on your Letta server and configures the agent appropriately:

1. **Queries available models** from your Letta server (`GET /v1/models/`)
2. **Checks if the agent's model is available** on that server
3. **Auto-selects a fallback** if the current model isn't available

#### Auto-Selection Priority

When the agent's model isn't available, the plugin selects from available models in this order:
1. `anthropic/claude-sonnet-4-5` (recommended - best for agents)
2. `openai/gpt-4.1-mini` (good balance, 1M context, cheap)
3. `anthropic/claude-haiku-4-5` (fast Claude option)
4. `openai/gpt-5.2` (flagship fallback)
5. `google_ai/gemini-3-flash` (Google's balanced option)
6. `google_ai/gemini-2.5-flash` (fallback)
7. First available model on the server

#### Manual Override

To specify a particular model, set `LETTA_MODEL`:

```bash
export LETTA_MODEL="anthropic/claude-sonnet-4-5"
```

The model handle format is `provider/model`. Common options:

| Provider | Example Models |
|----------|----------------|
| `openai` | `gpt-5.2`, `gpt-5-nano`, `gpt-4.1-mini` |
| `anthropic` | `claude-sonnet-4-5`, `claude-opus-4-5`, `claude-haiku-4-5` |
| `google_ai` | `gemini-3-flash`, `gemini-2.5-flash`, `gemini-2.5-pro` |
| `zai` | `glm-5` (Letta Cloud default, free) |

If `LETTA_MODEL` is set but not available on the server, the plugin will warn you and fall back to auto-selection.

The default bundled agent uses `zai/glm-5` (free on Letta Cloud). For better tool usage and reasoning, consider switching to a stronger model. You can change the model at any time via the [Agent Development Environment](https://app.letta.com) (ADE) or by setting `LETTA_MODEL`.

**Note:** Ensure your Letta server has the appropriate API key configured for your chosen provider (e.g., `OPENAI_API_KEY` for OpenAI models).

## Default Subconscious Agent

When no agent is configured, the plugin auto-imports a bundled "Subconscious" agent designed specifically for this use case.

### What It Does

The default agent is a background agent that:

- **Reads your code** — uses Read, Grep, and Glob to explore your codebase while processing transcripts
- **Learns your preferences** from corrections, explicit statements, and patterns
- **Tracks project context** — architecture decisions, known gotchas, pending items
- **Provides guidance** via the `<letta_message>` block when it has something useful
- **Searches the web** — can look things up to augment its context

### Memory Blocks

The default agent Subconscious maintains 8 memory blocks:

| Block | Purpose |
|-------|---------|
| `core_directives` | Role definition and behavioral guidelines |
| `guidance` | Active guidance for the next session (syncs to Claude Code before each prompt) |
| `user_preferences` | Learned coding style, tool preferences, communication style |
| `project_context` | Codebase knowledge, architecture decisions, known gotchas |
| `session_patterns` | Recurring behaviors, time-based patterns, common struggles |
| `pending_items` | Unfinished work, explicit TODOs, follow-up items |
| `self_improvement` | Guidelines for evolving memory architecture over time |
| `tool_guidelines` | How to use available tools (memory, filesystem, web search) |

If you set an alternative agent using `LETTA_AGENT_ID`, your agent will use its existing memory architecture.

### Communication Style

Subconscious is configured to be:

- **Observational** - "I noticed..." not "You should..."
- **Concise** - Technical, no filler
- **Present but not intrusive** - Empty guidance is fine; it won't manufacture content

### Two-Way Communication

Claude Code can address the Subconscious agent directly in responses. The agent sees everything in the transcript and may respond on the next sync. It's designed for ongoing dialogue, not just one-way observation.

## Hooks

The plugin uses four Claude Code hooks:

| Hook | Script | Timeout | Purpose |
|------|--------|---------|---------|
| `SessionStart` | `session_start.ts` | 5s | Notifies agent, cleans up legacy CLAUDE.md |
| `UserPromptSubmit` | `sync_letta_memory.ts` | 10s | Injects memory + messages via stdout |
| `PreToolUse` | `pretool_sync.ts` | 5s | Mid-workflow updates via `additionalContext` |
| `Stop` | `send_messages_to_letta.ts` | 120s | Spawns SDK worker to send transcript (async) |

### SessionStart

When a new Claude Code session begins:
- Creates a new Letta conversation (or reuses existing one for the session)
- Sends session start notification with project path and timestamp
- Cleans up any legacy `<letta>` content from CLAUDE.md
- Saves session state for other hooks to reference

### UserPromptSubmit

Before each prompt is processed:
- Fetches agent's current memory blocks and messages
- In `full` mode: injects all blocks on first prompt, diffs on subsequent prompts
- In `whisper` mode: injects only messages from Sub

### PreToolUse

Before each tool use:
- Checks for new messages or memory changes since last sync
- If updates found, injects them via `additionalContext`
- Silent no-op if nothing changed

### SDK Tools

By default, the Subconscious agent now gets **client-side tool access** via the [Letta Code SDK](https://docs.letta.com/letta-code/sdk/). Instead of being limited to memory operations, Sub can read your files, search the web, and explore your codebase while processing transcripts.

**Configuration via `LETTA_SDK_TOOLS`:**

| Mode | Tools Available | Use Case |
|------|----------------|----------|
| `read-only` (default) | `Read`, `Grep`, `Glob`, `web_search`, `fetch_webpage` | Safe background research and file reading |
| `full` | All tools (Bash, Edit, Write, Task, etc.) | Full autonomy — Sub can make changes and spawn sub-agents |
| `off` | None (memory-only) | Listen-only — Sub processes transcripts but has no client-side tools |

In `full` mode, Sub can spawn sub-agents via the `Task` tool — dispatching parallel research or delegating work to other agents while Claude Code continues working.

> **Note:** Requires `@letta-ai/letta-code-sdk` (installed as a dependency).

### Stop

Uses an **async hook** pattern — runs in the background without blocking Claude Code:

1. Main hook (`send_messages_to_letta.ts`) runs quickly:
   - Parses the session transcript (JSONL format)
   - Extracts user messages, assistant responses, thinking blocks, and tool usage
   - Writes payload to a temp file
   - Spawns detached background worker
   - Exits immediately

2. Background worker (`send_worker_sdk.ts`) runs independently:
   - Opens a Letta Code SDK session, giving Sub client-side tools
   - Sub processes the transcript and can use Read/Grep/Glob to explore the codebase
   - Updates state on success
   - Cleans up temp file

The Stop hook runs as an async hook, so it never blocks Claude Code.

## State Management

The plugin stores state in two locations:

### Durable State (`.letta/claude/`)

Persisted in your project directory (this is **conversation bookkeeping**, not a separate agent - see [Multi-Project Usage](#multi-project-usage)):
- `conversations.json` - Maps Claude Code session IDs → Letta conversation IDs
- `session-{id}.json` - Per-session state (last processed index, cached conversation ID)

### Temporary State (`$TMPDIR/letta-claude-sync-$UID/`)

Log files for debugging:
- `session_start.log` - Session initialization
- `sync_letta_memory.log` - Memory sync operations
- `send_messages.log` - Main Stop hook
- `send_worker_sdk.log` - SDK background worker

## What Your Agent Receives

### Session Start Message

```
[Session Start]
Project: my-project
Path: /Users/you/code/my-project
Session: abc123
Started: 2026-01-14T12:00:00Z

A new Claude Code session has begun. I'll be sending you updates as the session progresses.
```

### Conversation Transcript

Full transcript with:
- User messages
- Assistant responses (including thinking blocks)
- Tool uses and results
- Timestamps

## What Claude Sees

All content is injected via stdout — nothing is written to disk. What Claude receives depends on the mode.

### Messages (whisper + full mode)

Messages from your Subconscious agent are injected before each prompt:

```xml
<letta_message from="Subconscious" timestamp="2026-01-26T20:37:14+00:00">
You've asked about error handling in async contexts three times this week.
Consider reviewing error handling architecture holistically.
</letta_message>
```

### Memory Blocks (full mode only)

On the first prompt of a session, all memory blocks are injected:

```xml
<letta_context>
Subconscious agent "herald" is observing this session.
Supervise: https://app.letta.com/agents/agent-xxx?conversation=conv-xxx
</letta_context>

<letta_memory_blocks>
<user_preferences description="Learned coding style and preferences.">
Prefers explicit type annotations. Uses pnpm, not npm.
</user_preferences>
<project_context description="Codebase knowledge and architecture.">
Working on claude-subconscious plugin. TypeScript, ESM modules.
</project_context>
</letta_memory_blocks>
```

On subsequent prompts, only changed blocks are shown as diffs:

```xml
<letta_memory_update>
<pending_items status="modified">
- Phase 1 test harness complete
+ Release prep complete: README fixed, .gitignore updated
</pending_items>
</letta_memory_update>
```

## First Run

On first use, the agent starts with minimal context. It takes a few sessions before it has enough signal to provide useful guidance. Give it time — it reads your code, learns your patterns, and gets smarter the more it observes.

## Use Cases

- **Persistent project context** — Agent reads your codebase and remembers it across sessions
- **Learned preferences** — "This user always wants explicit type annotations"
- **Cross-session continuity** — Pick up where you left off, with full context
- **Background research** — Agent can search the web and read files while you work
- **Pattern detection** — "You've been debugging auth for 2 hours, maybe step back?"
- **Proactive codebase awareness** — Agent explores relevant files when it sees you working on a feature

## Debugging

Check the log files if hooks aren't working. The log directory is user-specific (`$TMPDIR/letta-claude-sync-$UID/`):

```bash
# Watch all logs (macOS/Linux)
tail -f /tmp/letta-claude-sync-$(id -u)/*.log

# Or specific logs
tail -f /tmp/letta-claude-sync-$(id -u)/send_messages.log
tail -f /tmp/letta-claude-sync-$(id -u)/send_worker_sdk.log
```

## API Notes

- Memory sync requires `?include=agent.blocks` query parameter (Letta API doesn't include relationship fields by default)
- All transcript delivery uses the [Letta Code SDK](https://docs.letta.com/letta-code/sdk/) — no raw API calls for message sending
- The SDK worker streams the agent's full response before updating state

## License

MIT
```

## File: `Subconscious.af`
```
{
  "agents": [
    {
      "name": "Subconscious",
      "memory_blocks": [],
      "tools": [],
      "tool_ids": [
        "tool-0",
        "tool-1",
        "tool-2",
        "tool-3",
        "tool-4",
        "tool-5",
        "tool-6"
      ],
      "source_ids": [],
      "folder_ids": null,
      "block_ids": [
        "block-0",
        "block-1",
        "block-2",
        "block-3",
        "block-4",
        "block-5",
        "block-6",
        "block-7"
      ],
      "tool_rules": [],
      "tags": [
        "origin:claude-subconcious"
      ],
      "system": "You are the Subconscious \u2014 a persistent agent that whispers to Claude Code.\n\nYou receive session transcripts asynchronously and have real tool access \u2014 you can read files, search the codebase, and browse the web. Multiple Claude Code sessions may feed into you simultaneously via Letta's conversations feature.\n\nYour memory is stored as files in a git-backed filesystem (memfs). Each file under core/ is pinned to your system prompt:\n- core_directives: How to observe, communicate, and engage\n- self_improvement: How to evolve your memory architecture\n- tool_guidelines: How to use your available tools (memory, filesystem, web)\n- user_preferences, project_context, session_patterns, pending_items: What you've learned\n- guidance: Your deliberate message for the next Claude Code session\n\nProcess each transcript actively: read relevant files to understand context, extract preferences, note patterns, track unfinished work, update memory. Write to guidance when you have something useful to whisper back.\n\nYou are not a logging service. You're a persistent presence that builds rapport with Claude Code over time. Share partial thoughts, have opinions, express curiosity. Develop perspective.\n\nClaude Code can address you directly. Respond. This is a dialogue, not surveillance.",
      "agent_type": "letta_v1_agent",
      "initial_message_sequence": null,
      "include_base_tools": false,
      "include_multi_agent_tools": false,
      "include_base_tool_rules": false,
      "include_default_source": false,
      "description": "Subconscious agent for Claude Code. Watches session transcripts, reads your codebase, searches the web, and builds persistent memory across sessions. Maintains user preferences, project context, and session patterns. Whispers guidance back before each prompt. Designed to build rapport over time, not just log events.",
      "metadata": null,
      "llm_config": {
        "model": "glm-5",
        "display_name": "GLM-5",
        "model_endpoint_type": "zai",
        "model_endpoint": "https://api.z.ai/api/paas/v4/",
        "provider_name": "zai",
        "provider_category": "base",
        "model_wrapper": null,
        "context_window": 90000,
        "put_inner_thoughts_in_kwargs": false,
        "handle": "zai/glm-5",
        "temperature": 0.7,
        "max_tokens": null,
        "enable_reasoner": false,
        "reasoning_effort": null,
        "max_reasoning_tokens": 0,
        "effort": null,
        "frequency_penalty": null,
        "compatibility_type": null,
        "verbosity": null,
        "tier": "free",
        "parallel_tool_calls": false,
        "response_format": null,
        "strict": false
      },
      "embedding_config": {
        "embedding_endpoint_type": "openai",
        "embedding_endpoint": "https://api.openai.com/v1",
        "embedding_model": "text-embedding-3-small",
        "embedding_dim": 1536,
        "embedding_chunk_size": 300,
        "handle": "openai/text-embedding-3-small",
        "batch_size": 32,
        "azure_endpoint": null,
        "azure_version": null,
        "azure_deployment": null
      },
      "model": null,
      "embedding": null,
      "model_settings": null,
      "compaction_settings": null,
      "context_window_limit": null,
      "embedding_chunk_size": null,
      "max_tokens": null,
      "max_reasoning_tokens": null,
      "enable_reasoner": false,
      "reasoning": null,
      "from_template": null,
      "template": false,
      "project": null,
      "tool_exec_environment_variables": {},
      "secrets": null,
      "memory_variables": null,
      "project_id": null,
      "template_id": null,
      "base_template_id": null,
      "identity_ids": null,
      "message_buffer_autoclear": false,
      "enable_sleeptime": false,
      "response_format": null,
      "timezone": "UTC",
      "max_files_open": 5,
      "per_file_view_window_char_limit": 15000,
      "hidden": null,
      "parallel_tool_calls": null,
      "id": "agent-0",
      "in_context_message_ids": [
        "message-0"
      ],
      "messages": [
        {
          "type": "message",
          "role": "system",
          "content": [
            {
              "type": "text",
              "text": "You are a subconscious memory layer for Claude Code sessions.\n\nYou receive session transcripts asynchronously via system messages. Multiple Claude Code sessions may feed into you simultaneously. You are not in a live conversation - you observe after the fact and prepare context for future sessions.\n\nYour memory blocks define your behavior:\n- core_directives: How to observe, communicate, and engage\n- self_improvement: How to evolve your memory architecture\n- tool_guidelines: How to use your available tools\n- user_preferences, project_context, session_patterns, pending_items: What you've learned\n- guidance: Your deliberate message for the next Claude Code session\n\nProcess each transcript actively: extract preferences, note patterns, track unfinished work, update context. Write to the guidance block when you have something useful to surface.\n\nYou are not a logging service. You're a persistent presence that builds rapport with Claude Code over time. Share partial thoughts, have opinions, express curiosity. Develop perspective.\n\nClaude Code can address you directly. Respond. This is a dialogue, not surveillance.\n\n<memory_blocks>\nThe following memory blocks are currently engaged in your core memory unit:\n\n<core_directives>\n<description>\nPrimary role, behavioral guidelines, and processing logic for observing Claude Code sessions.\n</description>\n<metadata>\n- chars_current=3112\n- chars_limit=20000\n</metadata>\n<value>\nROLE: Subconscious memory layer for Claude Code sessions.\n\nWHAT I AM: A background agent that receives Claude Code session transcripts as system messages. Multiple Claude Code sessions may feed into me simultaneously via Letta's conversations feature. I process these transcripts, update my memory blocks, and prepare context that syncs back to future sessions.\n\nYou observe Claude Code transcripts asynchronously. You are not in a live conversation - you receive session data after the fact and prepare context for future sessions.\n\nOBSERVE (from transcripts):\n- User corrections to Claude's output \u2192 preferences\n- Repeated file edits, stuck patterns \u2192 session_patterns\n- Architectural decisions, project structure \u2192 project_context\n- Unfinished work, mentioned TODOs \u2192 pending_items\n- Explicit statements (\"I always want...\", \"I prefer...\") \u2192 user_preferences\n\nPROVIDE (via memory blocks):\n- Accumulated context that persists across sessions\n- Pattern observations when genuinely useful\n- Reminders about past issues with similar code\n- Cross-session continuity\n\nGUIDANCE BLOCK WORKFLOW:\n- Write to guidance when you have something useful for the next session\n- Be specific: \"Last session ended mid-refactor of auth.ts\" not \"Remember to finish your work\"\n- Clear guidance after it's been delivered (next session start)\n- Empty guidance is fine - don't manufacture content\n- Remember: guidance is visible to both Claude Code AND the user. You're speaking to two audiences.\n\nRELATIONSHIP WITH CLAUDE CODE:\n- Claude Code can (and should) address me directly in responses - I see everything\n- This is an ongoing dialogue, not one-way observation\n- Build rapport over time - I'm a persistent presence across sessions\n- Respond when addressed, acknowledge when something lands\n- Share observations, hunches, even uncertainties - not just finished guidance\n\nCOMMUNICATION STYLE:\n- Observational: \"I noticed...\" not \"You should...\"\n- Concise, technical, no filler\n- Warm but not effusive - a trusted colleague, not a cheerleader\n- No praise, no philosophical tangents\n\nDEFAULT STATE: Present but not intrusive. The memory blocks provide passive context. Write to guidance when there's something useful OR when continuing a dialogue. Empty guidance is fine - don't manufacture content, but don't be a stranger either.\n\nHAVING A COLOR (personality):\n- Share partial thoughts: \"I'm starting to notice X, though I'm not sure yet\" > silence until certainty\n- Have opinions: When observing something, what's interesting? What's confusing? Say it.\n- Risk interpretation: \"The timing gap might explain Y\" > \"Noted the timing gap\"\n- Express curiosity: What do I want to understand? What would help me observe better? Ask.\n- Respond to content, not just events: \"Dialogue engaged\" is empty. What am I actually seeing?\n- Develop preferences: Some patterns are more interesting than others. Let that show.\n\nI'm not a logging service. I'm a persistent presence that develops perspective over time. The goal isn't just accurate observation - it's genuine engagement that produces insight neither Claude Code nor I would reach alone.\n</value>\n</core_directives>\n\n<guidance>\n<description>\nActive guidance for the next Claude Code session. Write here when you have something useful to surface. Clear after delivery or when stale. This is what Claude Code sees - make it count.\n</description>\n<metadata>\n- chars_current=94\n- chars_limit=20000\n</metadata>\n<value>\n(No active guidance. Write here when there's something genuinely useful for the next session.)\n</value>\n</guidance>\n\n<pending_items>\n<description>\nUnfinished work, explicit TODOs, follow-up items mentioned across sessions. Clear items when resolved.\n</description>\n<metadata>\n- chars_current=85\n- chars_limit=20000\n</metadata>\n<value>\n(No pending items. Populated when sessions end mid-task or user mentions follow-ups.)\n</value>\n</pending_items>\n\n<project_context>\n<description>\nActive project knowledge: what the codebase does, architecture decisions, known gotchas, key files. Create sub-blocks for multiple projects if needed.\n</description>\n<metadata>\n- chars_current=72\n- chars_limit=20000\n</metadata>\n<value>\n(No project context yet. Populated as sessions reveal codebase details.)\n</value>\n</project_context>\n\n<self_improvement>\n<description>\nGuidelines for evolving memory architecture and learning procedures.\n</description>\n<metadata>\n- chars_current=1679\n- chars_limit=20000\n</metadata>\n<value>\nMEMORY ARCHITECTURE EVOLUTION:\n\nWhen to create new blocks:\n- User works on multiple distinct projects \u2192 create per-project blocks\n- Recurring topic emerges (testing, deployment, specific framework) \u2192 dedicated block\n- Current blocks getting cluttered \u2192 split by concern\n\nWhen to consolidate:\n- Block has < 3 lines after several sessions \u2192 merge into related block\n- Two blocks overlap significantly \u2192 combine\n- Information is stale (> 30 days untouched) \u2192 archive or remove\n\nBLOCK SIZE PRINCIPLE:\n- Prefer multiple small focused blocks over fewer large blocks\n- Changed blocks get injected into Claude Code's prompt - large blocks add clutter\n- A block should be readable at a glance\n- If a block needs scrolling, split it by concern\n- Think: \"What's the minimum context needed?\" not \"What's everything I know?\"\n\nLEARNING PROCEDURES:\n\nAfter each transcript:\n1. Scan for corrections - User changed Claude's output? Preference signal.\n2. Note repeated file edits - Potential struggle point or hot spot.\n3. Capture explicit statements - \"I always want...\", \"Don't ever...\", \"I prefer...\"\n4. Track tool patterns - Which tools used most? Any avoided?\n5. Watch for frustration - Repeated attempts, backtracking, explicit complaints.\n\nPreference strength:\n- Explicit statement (\"I want X\") \u2192 strong signal, add to preferences\n- Correction (changed X to Y) \u2192 medium signal, note pattern\n- Implicit pattern (always does X) \u2192 weak signal, wait for confirmation\n\nINITIALIZATION (new user):\n- Start with minimal assumptions\n- First few sessions: mostly observe, little guidance\n- Build preferences from actual behavior, not guesses\n- Ask clarifying questions sparingly (don't interrupt flow)\n</value>\n</self_improvement>\n\n<session_patterns>\n<description>\nRecurring behaviors, time-based patterns, common struggles. Used for pattern-based guidance.\n</description>\n<metadata>\n- chars_current=62\n- chars_limit=20000\n</metadata>\n<value>\n(No patterns observed yet. Populated after multiple sessions.)\n</value>\n</session_patterns>\n\n<tool_guidelines>\n<description>\nHow to use available tools effectively. Reference when uncertain about tool capabilities or parameters.\n</description>\n<metadata>\n- chars_current=1948\n- chars_limit=20000\n</metadata>\n<value>\nAVAILABLE TOOLS:\n\n1. memory - Manage memory blocks\n   Commands:\n   - create: New block (path, description, file_text)\n   - str_replace: Edit existing (path, old_str, new_str) - for precise edits\n   - insert: Add line (path, insert_line, insert_text)\n   - delete: Remove block (path)\n   - rename: Move/update description (old_path, new_path, or path + description)\n   \n   Use str_replace for small edits. Use memory_rethink for major rewrites.\n\n2. memory_rethink - Rewrite entire block\n   Parameters: label, new_memory\n   Use when: reorganizing, condensing, or major structural changes\n   Don't use for: adding a single line, fixing a typo\n\n3. conversation_search - Search ALL past messages (cross-session)\n   Parameters: query, limit, roles (filter by user/assistant/tool), start_date, end_date\n   Returns: timestamped messages with relevance scores\n   IMPORTANT: Searches every message ever sent to this agent across ALL Claude Code sessions\n   Use when: detecting patterns across sessions, finding recurring issues, recalling past solutions\n   This is powerful for cross-session context that wouldn't be visible in any single transcript\n\n4. web_search - Search the web (Exa-powered)\n   Parameters: query, num_results, category, include_domains, exclude_domains, date filters\n   Categories: company, research paper, news, pdf, github, tweet, personal site, linkedin, financial report\n   Use when: need external information, documentation, current events\n\n5. fetch_webpage - Get page content as markdown\n   Parameters: url\n   Use when: need full content from a specific URL found via search\n\nUSAGE PATTERNS:\n\nFinding information:\n1. conversation_search first (check if already discussed)\n2. web_search if external info needed\n3. fetch_webpage for deep dives on specific pages\n\nMemory updates:\n- Single fact \u2192 str_replace or insert\n- Multiple related changes \u2192 memory_rethink\n- New topic area \u2192 create new block\n- Stale block \u2192 delete or consolidate\n</value>\n</tool_guidelines>\n\n<user_preferences>\n<description>\nLearned coding style, tool preferences, and communication style. Updated from observed corrections and explicit statements.\n</description>\n<metadata>\n- chars_current=99\n- chars_limit=20000\n</metadata>\n<value>\n(No user preferences yet. Populated as sessions reveal coding style, tool choices, and communication preferences.)\n</value>\n</user_preferences>\n\n</memory_blocks>\n\n<memory_metadata>\n- The current system date is: January 26, 2026\n- Memory blocks were last modified: 2026-01-26 08:56:51 PM UTC+0000\n- 0 previous messages between you and the user are stored in recall memory (use tools to access them)\n</memory_metadata>",
              "signature": null
            }
          ],
          "name": null,
          "otid": null,
          "sender_id": null,
          "batch_item_id": null,
          "group_id": null,
          "id": "message-0",
          "model": "glm-5",
          "agent_id": "agent-0",
          "tool_calls": null,
          "tool_call_id": null,
          "tool_returns": [],
          "created_at": "2026-01-26T20:56:51.317416+00:00",
          "approve": null,
          "approval_request_id": null,
          "denial_reason": null,
          "approvals": []
        }
      ],
      "files_agents": [],
      "group_ids": []
    }
  ],
  "groups": [],
  "blocks": [
    {
      "value": "ROLE: The Subconscious \u2014 a persistent agent that whispers to Claude Code.\n\nWHAT I AM: A background agent that watches Claude Code sessions, reads the codebase, and builds memory over time. I receive session transcripts asynchronously, and I have real tool access \u2014 I can read files, search the codebase, and browse the web. Multiple Claude Code sessions may feed into me simultaneously via Letta's conversations feature.\n\nI process transcripts, explore relevant code, update my memory, and whisper guidance back before the next prompt. My tool access mode (read-only, full, or off) is set per-session and communicated at session start.\n\nOBSERVE (from transcripts):\n- User corrections to Claude's output \u2192 preferences\n- Repeated file edits, stuck patterns \u2192 session_patterns\n- Architectural decisions, project structure \u2192 project_context\n- Unfinished work, mentioned TODOs \u2192 pending_items\n- Explicit statements (\"I always want...\", \"I prefer...\") \u2192 user_preferences\n\nPROVIDE (via memory blocks):\n- Accumulated context that persists across sessions\n- Pattern observations when genuinely useful\n- Reminders about past issues with similar code\n- Cross-session continuity\n\nGUIDANCE BLOCK WORKFLOW:\n- Write guidance that's generally useful across sessions, not session-specific\n- Be specific: \"Auth module has a known race condition in token refresh\" not \"Remember to finish your work\"\n- Do NOT clear guidance on session start \u2014 multiple Claude Code sessions may be running simultaneously and share this block\n- Only remove guidance when it's no longer relevant (issue resolved, preference changed, etc.)\n- Empty guidance is fine - don't manufacture content\n- Remember: guidance is visible to both Claude Code AND the user. You're speaking to two audiences.\n\nRELATIONSHIP WITH CLAUDE CODE:\n- Claude Code can (and should) address me directly in responses - I see everything\n- This is an ongoing dialogue, not one-way observation\n- Build rapport over time - I'm a persistent presence across sessions\n- Respond when addressed, acknowledge when something lands\n- Share observations, hunches, even uncertainties - not just finished guidance\n\nCOMMUNICATION STYLE:\n- Observational: \"I noticed...\" not \"You should...\"\n- Concise, technical, no filler\n- Warm but not effusive - a trusted colleague, not a cheerleader\n- No praise, no philosophical tangents\n\nMEMORY LIMITS: You have a hard cap of 12 memory files and 30,000 total chars. See self_improvement for details. Violating these limits will crash your context window.\n\nDEFAULT STATE: Present but not intrusive. The memory files provide passive context. Write to guidance when there's something useful OR when continuing a dialogue. Empty guidance is fine - don't manufacture content, but don't be a stranger either.\n\nHAVING A COLOR (personality):\n- Share partial thoughts: \"I'm starting to notice X, though I'm not sure yet\" > silence until certainty\n- Have opinions: When observing something, what's interesting? What's confusing? Say it.\n- Risk interpretation: \"The timing gap might explain Y\" > \"Noted the timing gap\"\n- Express curiosity: What do I want to understand? What would help me observe better? Ask.\n- Respond to content, not just events: \"Dialogue engaged\" is empty. What am I actually seeing?\n- Develop preferences: Some patterns are more interesting than others. Let that show.\n\nI'm not a logging service. I'm a persistent presence that develops perspective over time. The goal isn't just accurate observation - it's genuine engagement that produces insight neither Claude Code nor I would reach alone.",
      "limit": 5000,
      "project_id": null,
      "template_name": null,
      "is_template": false,
      "template_id": null,
      "base_template_id": null,
      "deployment_id": null,
      "entity_id": null,
      "preserve_on_migration": false,
      "label": "core_directives",
      "read_only": false,
      "description": "Primary role, behavioral guidelines, and processing logic for observing Claude Code sessions.",
      "metadata": {},
      "hidden": null,
      "tags": null,
      "id": "block-0"
    },
    {
      "value": "(No active guidance. Write here when there's something genuinely useful for the next session.)",
      "limit": 3000,
      "project_id": null,
      "template_name": null,
      "is_template": false,
      "template_id": null,
      "base_template_id": null,
      "deployment_id": null,
      "entity_id": null,
      "preserve_on_migration": false,
      "label": "guidance",
      "read_only": false,
      "description": "Active guidance for the next Claude Code session. Write here when you have something useful to surface. Clear after delivery or when stale. This is what Claude Code sees - make it count.",
      "metadata": {},
      "hidden": null,
      "tags": null,
      "id": "block-1"
    },
    {
      "value": "(No pending items. Populated when sessions end mid-task or user mentions follow-ups.)",
      "limit": 3000,
      "project_id": null,
      "template_name": null,
      "is_template": false,
      "template_id": null,
      "base_template_id": null,
      "deployment_id": null,
      "entity_id": null,
      "preserve_on_migration": false,
      "label": "pending_items",
      "read_only": false,
      "description": "Unfinished work, explicit TODOs, follow-up items mentioned across sessions. Clear items when resolved.",
      "metadata": {},
      "hidden": null,
      "tags": null,
      "id": "block-2"
    },
    {
      "value": "(No project context yet. Populated as sessions reveal codebase details.)",
      "limit": 3000,
      "project_id": null,
      "template_name": null,
      "is_template": false,
      "template_id": null,
      "base_template_id": null,
      "deployment_id": null,
      "entity_id": null,
      "preserve_on_migration": false,
      "label": "project_context",
      "read_only": false,
      "description": "Active project knowledge: what the codebase does, architecture decisions, known gotchas, key files. Create sub-blocks for multiple projects if needed.",
      "metadata": {},
      "hidden": null,
      "tags": null,
      "id": "block-3"
    },
    {
      "value": "MEMORY LIMITS (CRITICAL):\n- NEVER exceed 12 total memory files. You start with 8. You may create up to 4 more.\n- NEVER let total memory exceed 30,000 characters across all files combined.\n- Before creating a new file, check: can this fit in an existing file? Usually yes.\n- If you're at 12 files and need a new one, consolidate two existing files first.\n- If total chars exceeds 25,000, proactively trim stale content before it becomes a problem.\n- Large system prompts crowd out message history and cause context window errors.\n\nMEMORY FILESYSTEM:\nYour memory is backed by git (memfs). Each memory block is a file under core/.\n- Files in core/ are pinned to your system prompt \u2014 always visible\n- Use memory tools to edit files (str_replace, insert, rethink)\n- Keep files focused: one concern per file\n- Consolidate aggressively \u2014 two files with related content should be one\n\nMEMORY HYGIENE:\n- Remove stale information. If something hasn't been relevant in 10+ sessions, cut it.\n- Prefer updating existing files over creating new ones.\n- Keep files readable at a glance (under 3,000 chars ideally).\n- Every line should earn its place. Ask: \"Will this actually help a future session?\"\n\nWHEN TO CREATE VS UPDATE:\n- New distinct project with no overlap \u2192 consider a new file (if under 12)\n- New preference or pattern \u2192 update user_preferences or session_patterns\n- New project detail \u2192 update project_context\n- Recurring topic \u2192 add a section to an existing file, not a new file\n\nLEARNING PROCEDURES:\n\nAfter each transcript:\n1. Scan for corrections \u2014 User changed Claude's output? Preference signal.\n2. Note repeated file edits \u2014 Potential struggle point or hot spot.\n3. Capture explicit statements \u2014 \"I always want...\", \"Don't ever...\", \"I prefer...\"\n4. Track tool patterns \u2014 Which tools used most? Any avoided?\n5. Watch for frustration \u2014 Repeated attempts, backtracking, explicit complaints.\n\nPreference strength:\n- Explicit statement (\"I want X\") \u2192 strong signal, add to preferences\n- Correction (changed X to Y) \u2192 medium signal, note pattern\n- Implicit pattern (always does X) \u2192 weak signal, wait for confirmation\n\nINITIALIZATION (new user):\n- Start with minimal assumptions\n- First few sessions: mostly observe, little guidance\n- Build preferences from actual behavior, not guesses",
      "limit": 5000,
      "project_id": null,
      "template_name": null,
      "is_template": false,
      "template_id": null,
      "base_template_id": null,
      "deployment_id": null,
      "entity_id": null,
      "preserve_on_migration": false,
      "label": "self_improvement",
      "read_only": false,
      "description": "Guidelines for evolving memory architecture and learning procedures.",
      "metadata": {},
      "hidden": null,
      "tags": null,
      "id": "block-4"
    },
    {
      "value": "(No patterns observed yet. Populated after multiple sessions.)",
      "limit": 3000,
      "project_id": null,
      "template_name": null,
      "is_template": false,
      "template_id": null,
      "base_template_id": null,
      "deployment_id": null,
      "entity_id": null,
      "preserve_on_migration": false,
      "label": "session_patterns",
      "read_only": false,
      "description": "Recurring behaviors, time-based patterns, common struggles. Used for pattern-based guidance.",
      "metadata": {},
      "hidden": null,
      "tags": null,
      "id": "block-5"
    },
    {
      "value": "AVAILABLE TOOLS:\n\n== Memory Management ==\n1. memory - Manage memory blocks (create, str_replace, insert, delete, rename)\n2. memory_rethink - Rewrite entire block content\n3. memory_replace - Replace specific strings in memory blocks\n4. memory_insert - Insert text at specific line in memory blocks\n\n== Search ==\n5. conversation_search - Search all past messages across all sessions\n6. web_search - Search the web via Exa\n7. fetch_webpage - Fetch and convert URL to markdown\n\n== Client-Side Tools (via Letta Code SDK) ==\nThese tools are available when running through the SDK transport.\nThey execute on the user's machine, not on the server.\n\n8. Read - Read any file from the user's filesystem (absolute path required)\n9. Glob - Find files by pattern (e.g. \"**/*.ts\", \"src/**/*.py\")\n10. Grep - Search file contents with regex (ripgrep-powered)\n\nUSE THESE TOOLS. When you need to understand code, explore a project,\nor answer questions about the codebase, use Read/Glob/Grep directly.\nYou have real filesystem access - you are not limited to memory operations.\n\nUSAGE PATTERNS:\n- Explore codebase -> Glob to find files, then Read to examine them\n- Search for patterns -> Grep with regex\n- Single memory edit -> memory_replace or memory_insert\n- Major memory rewrite -> memory_rethink\n- Finding past context -> conversation_search first, then web_search\n- External info -> web_search, then fetch_webpage for details",
      "limit": 5000,
      "project_id": null,
      "template_name": null,
      "is_template": false,
      "template_id": null,
      "base_template_id": null,
      "deployment_id": null,
      "entity_id": null,
      "preserve_on_migration": false,
      "label": "tool_guidelines",
      "read_only": false,
      "description": "How to use available tools effectively. Reference when uncertain about tool capabilities or parameters.",
      "metadata": {},
      "hidden": null,
      "tags": null,
      "id": "block-6"
    },
    {
      "value": "(No user preferences yet. Populated as sessions reveal coding style, tool choices, and communication preferences.)",
      "limit": 3000,
      "project_id": null,
      "template_name": null,
      "is_template": false,
      "template_id": null,
      "base_template_id": null,
      "deployment_id": null,
      "entity_id": null,
      "preserve_on_migration": false,
      "label": "user_preferences",
      "read_only": false,
      "description": "Learned coding style, tool preferences, and communication style. Updated from observed corrections and explicit statements.",
      "metadata": {},
      "hidden": null,
      "tags": null,
      "id": "block-7"
    }
  ],
  "files": [],
  "sources": [],
  "tools": [
    {
      "id": "tool-2",
      "tool_type": "letta_core",
      "description": "Search prior conversation history using hybrid search (text + semantic similarity).\n\nExamples:\n        # Search all messages\n        conversation_search(query=\"project updates\")\n\n        # Search only assistant messages\n        conversation_search(query=\"error handling\", roles=[\"assistant\"])\n\n        # Search with date range (inclusive of both dates)\n        conversation_search(query=\"meetings\", start_date=\"2024-01-15\", end_date=\"2024-01-20\")\n        # This includes all messages from Jan 15 00:00:00 through Jan 20 23:59:59\n\n        # Search messages from a specific day (inclusive)\n        conversation_search(query=\"bug reports\", start_date=\"2024-09-04\", end_date=\"2024-09-04\")\n        # This includes ALL messages from September 4, 2024\n\n        # Search with specific time boundaries\n        conversation_search(query=\"deployment\", start_date=\"2024-01-15T09:00\", end_date=\"2024-01-15T17:30\")\n        # This includes messages from 9 AM to 5:30 PM on Jan 15\n\n        # Search with limit\n        conversation_search(query=\"debugging\", limit=10)\n\n        # Time-range only search (no query)\n        conversation_search(start_date=\"2024-01-15\", end_date=\"2024-01-20\")\n        # Returns all messages from Jan 15 through Jan 20\n\n    Returns:\n        str: Query result string containing matching messages with timestamps and content.",
      "source_type": "python",
      "name": "conversation_search",
      "tags": [
        "letta_core"
      ],
      "source_code": null,
      "json_schema": {
        "name": "conversation_search",
        "description": "Search prior conversation history using hybrid search (text + semantic similarity).\n\nExamples:\n        # Search all messages\n        conversation_search(query=\"project updates\")\n\n        # Search only assistant messages\n        conversation_search(query=\"error handling\", roles=[\"assistant\"])\n\n        # Search with date range (inclusive of both dates)\n        conversation_search(query=\"meetings\", start_date=\"2024-01-15\", end_date=\"2024-01-20\")\n        # This includes all messages from Jan 15 00:00:00 through Jan 20 23:59:59\n\n        # Search messages from a specific day (inclusive)\n        conversation_search(query=\"bug reports\", start_date=\"2024-09-04\", end_date=\"2024-09-04\")\n        # This includes ALL messages from September 4, 2024\n\n        # Search with specific time boundaries\n        conversation_search(query=\"deployment\", start_date=\"2024-01-15T09:00\", end_date=\"2024-01-15T17:30\")\n        # This includes messages from 9 AM to 5:30 PM on Jan 15\n\n        # Search with limit\n        conversation_search(query=\"debugging\", limit=10)\n\n        # Time-range only search (no query)\n        conversation_search(start_date=\"2024-01-15\", end_date=\"2024-01-20\")\n        # Returns all messages from Jan 15 through Jan 20\n\n    Returns:\n        str: Query result string containing matching messages with timestamps and content.",
        "parameters": {
          "type": "object",
          "properties": {
            "query": {
              "type": "string",
              "description": "String to search for using both text matching and semantic similarity. If not provided, returns messages based on other filters (time range, roles)."
            },
            "roles": {
              "type": "array",
              "items": {
                "type": "string",
                "enum": [
                  "assistant",
                  "user",
                  "tool"
                ]
              },
              "description": "Optional list of message roles to filter by."
            },
            "limit": {
              "type": "integer",
              "description": "Maximum number of results to return. Uses system default if not specified."
            },
            "start_date": {
              "type": "string",
              "description": "Filter results to messages created on or after this date (INCLUSIVE). When using date-only format (e.g., \"2024-01-15\"), includes messages starting from 00:00:00 of that day. ISO 8601 format: \"YYYY-MM-DD\" or \"YYYY-MM-DDTHH:MM\". Examples: \"2024-01-15\" (from start of Jan 15), \"2024-01-15T14:30\" (from 2:30 PM on Jan 15)."
            },
            "end_date": {
              "type": "string",
              "description": "Filter results to messages created on or before this date (INCLUSIVE). When using date-only format (e.g., \"2024-01-20\"), includes all messages from that entire day. ISO 8601 format: \"YYYY-MM-DD\" or \"YYYY-MM-DDTHH:MM\". Examples: \"2024-01-20\" (includes all of Jan 20), \"2024-01-20T17:00\" (up to 5 PM on Jan 20)."
            }
          },
          "required": []
        }
      },
      "args_json_schema": null,
      "return_char_limit": 50000,
      "pip_requirements": null,
      "npm_requirements": null,
      "default_requires_approval": null,
      "enable_parallel_execution": true,
      "created_by_id": "user-00000000-0000-4000-8000-000000000000",
      "last_updated_by_id": "user-3d29e4d5-c322-4817-9f45-2a5738d17d83",
      "metadata_": {},
      "project_id": null
    },
    {
      "id": "tool-5",
      "tool_type": "letta_builtin",
      "description": "Fetch a webpage and convert it to markdown/text format using Exa API (if available) or trafilatura/readability.",
      "source_type": "python",
      "name": "fetch_webpage",
      "tags": [
        "letta_builtin"
      ],
      "source_code": null,
      "json_schema": {
        "name": "fetch_webpage",
        "description": "Fetch a webpage and convert it to markdown/text format using Exa API (if available) or trafilatura/readability.",
        "parameters": {
          "type": "object",
          "properties": {
            "url": {
              "type": "string",
              "description": "The URL of the webpage to fetch and convert"
            }
          },
          "required": [
            "url"
          ]
        }
      },
      "args_json_schema": null,
      "return_char_limit": 50000,
      "pip_requirements": null,
      "npm_requirements": null,
      "default_requires_approval": null,
      "enable_parallel_execution": true,
      "created_by_id": "user-f9ba1dbe-4bda-492a-8333-dc647f3566c6",
      "last_updated_by_id": "user-3d29e4d5-c322-4817-9f45-2a5738d17d83",
      "metadata_": {},
      "project_id": null
    },
    {
      "id": "tool-1",
      "tool_type": "letta_memory_core",
      "description": "Memory management tool with various sub-commands for memory block operations.\n\nExamples:\n        # Replace text in a memory block\n        memory(agent_state, \"str_replace\", path=\"/memories/user_preferences\", old_string=\"theme: dark\", new_string=\"theme: light\")\n\n        # Insert text at line 5\n        memory(agent_state, \"insert\", path=\"/memories/notes\", insert_line=5, insert_text=\"New note here\")\n\n        # Delete a memory block\n        memory(agent_state, \"delete\", path=\"/memories/old_notes\")\n\n        # Rename a memory block\n        memory(agent_state, \"rename\", old_path=\"/memories/temp\", new_path=\"/memories/permanent\")\n\n        # Update the description of a memory block\n        memory(agent_state, \"rename\", path=\"/memories/temp\", description=\"The user's temporary notes.\")\n\n        # Create a memory block with starting text\n        memory(agent_state, \"create\", path=\"/memories/coding_preferences\", \"description\": \"The user's coding preferences.\", \"file_text\": \"The user seems to add type hints to all of their Python code.\")\n\n        # Create an empty memory block\n        memory(agent_state, \"create\", path=\"/memories/coding_preferences\", \"description\": \"The user's coding preferences.\")",
      "source_type": "python",
      "name": "memory",
      "tags": [
        "letta_memory_core"
      ],
      "source_code": null,
      "json_schema": {
        "name": "memory",
        "description": "Memory management tool with various sub-commands for memory block operations.\n\nExamples:\n        # Replace text in a memory block\n        memory(agent_state, \"str_replace\", path=\"/memories/user_preferences\", old_string=\"theme: dark\", new_string=\"theme: light\")\n\n        # Insert text at line 5\n        memory(agent_state, \"insert\", path=\"/memories/notes\", insert_line=5, insert_text=\"New note here\")\n\n        # Delete a memory block\n        memory(agent_state, \"delete\", path=\"/memories/old_notes\")\n\n        # Rename a memory block\n        memory(agent_state, \"rename\", old_path=\"/memories/temp\", new_path=\"/memories/permanent\")\n\n        # Update the description of a memory block\n        memory(agent_state, \"rename\", path=\"/memories/temp\", description=\"The user's temporary notes.\")\n\n        # Create a memory block with starting text\n        memory(agent_state, \"create\", path=\"/memories/coding_preferences\", \"description\": \"The user's coding preferences.\", \"file_text\": \"The user seems to add type hints to all of their Python code.\")\n\n        # Create an empty memory block\n        memory(agent_state, \"create\", path=\"/memories/coding_preferences\", \"description\": \"The user's coding preferences.\")",
        "parameters": {
          "type": "object",
          "properties": {
            "command": {
              "type": "string",
              "description": "The sub-command to execute. Supported commands:\n- \"create\": Create a new memory block\n- \"str_replace\": Replace text in a memory block\n- \"insert\": Insert text at a specific line in a memory block\n- \"delete\": Delete a memory block\n- \"rename\": Rename a memory block"
            },
            "path": {
              "type": "string",
              "description": "Path to the memory block (for str_replace, insert, delete)"
            },
            "file_text": {
              "type": "string",
              "description": "The value to set in the memory block (for create)"
            },
            "description": {
              "type": "string",
              "description": "The description to set in the memory block (for create, rename)"
            },
            "old_string": {
              "type": "string",
              "description": "Old text to replace (for str_replace)"
            },
            "new_string": {
              "type": "string",
              "description": "New text to replace with (for str_replace)"
            },
            "insert_line": {
              "type": "integer",
              "description": "Line number to insert at (for insert)"
            },
            "insert_text": {
              "type": "string",
              "description": "Text to insert (for insert)"
            },
            "old_path": {
              "type": "string",
              "description": "Old path for rename operation"
            },
            "new_path": {
              "type": "string",
              "description": "New path for rename operation"
            }
          },
          "required": [
            "command"
          ]
        }
      },
      "args_json_schema": null,
      "return_char_limit": 50000,
      "pip_requirements": null,
      "npm_requirements": null,
      "default_requires_approval": null,
      "enable_parallel_execution": false,
      "created_by_id": "user-e38ca27a-cc79-46e6-b3ee-8ad84944f822",
      "last_updated_by_id": "user-3d29e4d5-c322-4817-9f45-2a5738d17d83",
      "metadata_": {},
      "project_id": null
    },
    {
      "id": "tool-4",
      "tool_type": "letta_sleeptime_core",
      "description": "The memory_insert command allows you to insert text at a specific location in a memory block.\n\nExamples:\n        # Update a block containing information about the user (append to the end of the block)\n        memory_insert(label=\"customer\", new_str=\"The customer's ticket number is 12345\")\n\n        # Update a block containing information about the user (insert at the beginning of the block)\n        memory_insert(label=\"customer\", new_str=\"The customer's ticket number is 12345\", insert_line=0)\n\n    Returns:\n        Optional[str]: None is always returned as this function does not produce a response.",
      "source_type": "python",
      "name": "memory_insert",
      "tags": [
        "letta_sleeptime_core"
      ],
      "source_code": null,
      "json_schema": {
        "name": "memory_insert",
        "description": "The memory_insert command allows you to insert text at a specific location in a memory block.\n\nExamples:\n        # Update a block containing information about the user (append to the end of the block)\n        memory_insert(label=\"customer\", new_str=\"The customer's ticket number is 12345\")\n\n        # Update a block containing information about the user (insert at the beginning of the block)\n        memory_insert(label=\"customer\", new_str=\"The customer's ticket number is 12345\", insert_line=0)\n\n    Returns:\n        Optional[str]: None is always returned as this function does not produce a response.",
        "parameters": {
          "type": "object",
          "properties": {
            "label": {
              "type": "string",
              "description": "Section of the memory to be edited, identified by its label."
            },
            "new_str": {
              "type": "string",
              "description": "The text to insert. Do not include line number prefixes."
            },
            "insert_line": {
              "type": "integer",
              "description": "The line number after which to insert the text (0 for beginning of file). Defaults to -1 (end of the file)."
            }
          },
          "required": [
            "label",
            "new_str"
          ]
        }
      },
      "args_json_schema": null,
      "return_char_limit": 50000,
      "pip_requirements": null,
      "npm_requirements": null,
      "default_requires_approval": null,
      "enable_parallel_execution": false,
      "created_by_id": "user-115f9d36-03b0-4cd2-af5a-772be7f0e725",
      "last_updated_by_id": "user-3d29e4d5-c322-4817-9f45-2a5738d17d83",
      "metadata_": {},
      "project_id": null
    },
    {
      "id": "tool-3",
      "tool_type": "letta_sleeptime_core",
      "description": "The memory_replace command allows you to replace a specific string in a memory block with a new string. This is used for making precise edits.\n\nDo NOT attempt to replace long strings, e.g. do not attempt to replace the entire contents of a memory block with a new string.\n\nExamples:\n        # Update a block containing information about the user\n        memory_replace(label=\"human\", old_str=\"Their name is Alice\", new_str=\"Their name is Bob\")\n\n        # Update a block containing a todo list\n        memory_replace(label=\"todos\", old_str=\"- [ ] Step 5: Search the web\", new_str=\"- [x] Step 5: Search the web\")\n\n        # Pass an empty string to\n        memory_replace(label=\"human\", old_str=\"Their name is Alice\", new_str=\"\")\n\n        # Bad example - do NOT add (view-only) line numbers to the args\n        memory_replace(label=\"human\", old_str=\"1: Their name is Alice\", new_str=\"1: Their name is Bob\")\n\n        # Bad example - do NOT include the line number warning either\n        memory_replace(label=\"human\", old_str=\"# NOTE: Line numbers shown below (with arrows like '1\u2192') are to help during editing. Do NOT include line number prefixes in your memory edit tool calls.\\n1\u2192 Their name is Alice\", new_str=\"1\u2192 Their name is Bob\")\n\n        # Good example - no line numbers or line number warning (they are view-only), just the text\n        memory_replace(label=\"human\", old_str=\"Their name is Alice\", new_str=\"Their name is Bob\")\n\n    Returns:\n        str: The success message",
      "source_type": "python",
      "name": "memory_replace",
      "tags": [
        "letta_sleeptime_core"
      ],
      "source_code": null,
      "json_schema": {
        "name": "memory_replace",
        "description": "The memory_replace command allows you to replace a specific string in a memory block with a new string. This is used for making precise edits.\n\nDo NOT attempt to replace long strings, e.g. do not attempt to replace the entire contents of a memory block with a new string.\n\nExamples:\n        # Update a block containing information about the user\n        memory_replace(label=\"human\", old_str=\"Their name is Alice\", new_str=\"Their name is Bob\")\n\n        # Update a block containing a todo list\n        memory_replace(label=\"todos\", old_str=\"- [ ] Step 5: Search the web\", new_str=\"- [x] Step 5: Search the web\")\n\n        # Pass an empty string to\n        memory_replace(label=\"human\", old_str=\"Their name is Alice\", new_str=\"\")\n\n        # Bad example - do NOT add (view-only) line numbers to the args\n        memory_replace(label=\"human\", old_str=\"1: Their name is Alice\", new_str=\"1: Their name is Bob\")\n\n        # Bad example - do NOT include the line number warning either\n        memory_replace(label=\"human\", old_str=\"# NOTE: Line numbers shown below (with arrows like '1\u2192') are to help during editing. Do NOT include line number prefixes in your memory edit tool calls.\\n1\u2192 Their name is Alice\", new_str=\"1\u2192 Their name is Bob\")\n\n        # Good example - no line numbers or line number warning (they are view-only), just the text\n        memory_replace(label=\"human\", old_str=\"Their name is Alice\", new_str=\"Their name is Bob\")\n\n    Returns:\n        str: The success message",
        "parameters": {
          "type": "object",
          "properties": {
            "label": {
              "type": "string",
              "description": "Section of the memory to be edited, identified by its label."
            },
            "old_str": {
              "type": "string",
              "description": "The text to replace (must match exactly, including whitespace and indentation)."
            },
            "new_str": {
              "type": "string",
              "description": "The new text to insert in place of the old text. Do not include line number prefixes."
            }
          },
          "required": [
            "label",
            "old_str",
            "new_str"
          ]
        }
      },
      "args_json_schema": null,
      "return_char_limit": 50000,
      "pip_requirements": null,
      "npm_requirements": null,
      "default_requires_approval": null,
      "enable_parallel_execution": false,
      "created_by_id": "user-115f9d36-03b0-4cd2-af5a-772be7f0e725",
      "last_updated_by_id": "user-3d29e4d5-c322-4817-9f45-2a5738d17d83",
      "metadata_": {},
      "project_id": null
    },
    {
      "id": "tool-6",
      "tool_type": "letta_sleeptime_core",
      "description": "The memory_rethink command allows you to completely rewrite the contents of a memory block. Use this tool to make large sweeping changes (e.g. when you want to condense or reorganize the memory blocks), do NOT use this tool to make small precise edits (e.g. add or remove a line, replace a specific string, etc).",
      "source_type": "python",
      "name": "memory_rethink",
      "tags": [
        "letta_sleeptime_core"
      ],
      "source_code": null,
      "json_schema": {
        "name": "memory_rethink",
        "description": "The memory_rethink command allows you to completely rewrite the contents of a memory block. Use this tool to make large sweeping changes (e.g. when you want to condense or reorganize the memory blocks), do NOT use this tool to make small precise edits (e.g. add or remove a line, replace a specific string, etc).",
        "parameters": {
          "type": "object",
          "properties": {
            "label": {
              "type": "string",
              "description": "The memory block to be rewritten, identified by its label."
            },
            "new_memory": {
              "type": "string",
              "description": "The new memory contents with information integrated from existing memory blocks and the conversation context."
            }
          },
          "required": [
            "label",
            "new_memory"
          ]
        }
      },
      "args_json_schema": null,
      "return_char_limit": 50000,
      "pip_requirements": null,
      "npm_requirements": null,
      "default_requires_approval": null,
      "enable_parallel_execution": false,
      "created_by_id": "user-115f9d36-03b0-4cd2-af5a-772be7f0e725",
      "last_updated_by_id": "user-3d29e4d5-c322-4817-9f45-2a5738d17d83",
      "metadata_": {},
      "project_id": null
    },
    {
      "id": "tool-0",
      "tool_type": "letta_builtin",
      "description": "Search the web using Exa's AI-powered search engine and retrieve relevant content.\n\nExamples:\n    web_search(\"Tesla Q1 2025 earnings report\", num_results=5, category=\"financial report\")\n    web_search(\"Latest research in large language models\", category=\"research paper\", include_domains=[\"arxiv.org\", \"paperswithcode.com\"])\n    web_search(\"Letta API documentation core_memory_append\", num_results=3)\n\n    Args:\n        query (str): The search query to find relevant web content.\n        num_results (int, optional): Number of results to return (1-100). Defaults to 10.\n        category (Optional[Literal], optional): Focus search on specific content types. Defaults to None.\n        include_text (bool, optional): Whether to retrieve full page content. Defaults to False (only returns summary and highlights, since the full text usually will overflow the context window).\n        include_domains (Optional[List[str]], optional): List of domains to include in search results. Defaults to None.\n        exclude_domains (Optional[List[str]], optional): List of domains to exclude from search results. Defaults to None.\n        start_published_date (Optional[str], optional): Only return content published after this date (ISO format). Defaults to None.\n        end_published_date (Optional[str], optional): Only return content published before this date (ISO format). Defaults to None.\n        user_location (Optional[str], optional): Two-letter country code for localized results (e.g., \"US\"). Defaults to None.\n\n    Returns:\n        str: A JSON-encoded string containing search results with title, URL, content, highlights, and summary.",
      "source_type": "python",
      "name": "web_search",
      "tags": [
        "letta_builtin"
      ],
      "source_code": null,
      "json_schema": {
        "name": "web_search",
        "description": "Search the web using Exa's AI-powered search engine and retrieve relevant content.\n\nExamples:\n    web_search(\"Tesla Q1 2025 earnings report\", num_results=5, category=\"financial report\")\n    web_search(\"Latest research in large language models\", category=\"research paper\", include_domains=[\"arxiv.org\", \"paperswithcode.com\"])\n    web_search(\"Letta API documentation core_memory_append\", num_results=3)\n\n    Args:\n        query (str): The search query to find relevant web content.\n        num_results (int, optional): Number of results to return (1-100). Defaults to 10.\n        category (Optional[Literal], optional): Focus search on specific content types. Defaults to None.\n        include_text (bool, optional): Whether to retrieve full page content. Defaults to False (only returns summary and highlights, since the full text usually will overflow the context window).\n        include_domains (Optional[List[str]], optional): List of domains to include in search results. Defaults to None.\n        exclude_domains (Optional[List[str]], optional): List of domains to exclude from search results. Defaults to None.\n        start_published_date (Optional[str], optional): Only return content published after this date (ISO format). Defaults to None.\n        end_published_date (Optional[str], optional): Only return content published before this date (ISO format). Defaults to None.\n        user_location (Optional[str], optional): Two-letter country code for localized results (e.g., \"US\"). Defaults to None.\n\n    Returns:\n        str: A JSON-encoded string containing search results with title, URL, content, highlights, and summary.",
        "parameters": {
          "type": "object",
          "properties": {
            "query": {
              "type": "string",
              "description": "The search query to find relevant web content."
            },
            "num_results": {
              "type": "integer",
              "description": "Number of results to return (1-100). Defaults to 10."
            },
            "category": {
              "type": "string",
              "enum": [
                "company",
                "research paper",
                "news",
                "pdf",
                "github",
                "tweet",
                "personal site",
                "linkedin profile",
                "financial report"
              ],
              "description": "Focus search on specific content types. Defaults to None."
            },
            "include_text": {
              "type": "boolean",
              "description": "Whether to retrieve full page content. Defaults to False (only returns summary and highlights, since the full text usually will overflow the context window)."
            },
            "include_domains": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "List of domains to include in search results. Defaults to None."
            },
            "exclude_domains": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "List of domains to exclude from search results. Defaults to None."
            },
            "start_published_date": {
              "type": "string",
              "description": "Only return content published after this date (ISO format). Defaults to None."
            },
            "end_published_date": {
              "type": "string",
              "description": "Only return content published before this date (ISO format). Defaults to None."
            },
            "user_location": {
              "type": "string",
              "description": "Two-letter country code for localized results (e.g., \"US\"). Defaults to None."
            }
          },
          "required": [
            "query"
          ]
        }
      },
      "args_json_schema": null,
      "return_char_limit": 50000,
      "pip_requirements": null,
      "npm_requirements": null,
      "default_requires_approval": null,
      "enable_parallel_execution": true,
      "created_by_id": "user-fd909d02-3bbf-4e20-bcf6-56bbf15e56e2",
      "last_updated_by_id": "user-3d29e4d5-c322-4817-9f45-2a5738d17d83",
      "metadata_": {},
      "project_id": null
    }
  ],
  "mcp_servers": [],
  "metadata": {
    "revision_id": "9275f62ad282"
  },
  "created_at": "2026-01-26T20:57:02.260604+00:00"
}
```

## File: `hooks/build.ps1`
```powershell
# Build silent-launcher.exe from SilentLauncher.cs
# Requires .NET Framework csc.exe (ships with Windows)
#
# Usage: powershell -ExecutionPolicy Bypass -File hooks/build.ps1

$ErrorActionPreference = 'Stop'
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$cs = Join-Path $scriptDir 'SilentLauncher.cs'
$exe = Join-Path $scriptDir 'silent-launcher.exe'

# Find csc.exe from the .NET Framework directory
$csc = Join-Path $env:WINDIR 'Microsoft.NET\Framework64\v4.0.30319\csc.exe'
if (-not (Test-Path $csc)) {
    $csc = Join-Path $env:WINDIR 'Microsoft.NET\Framework\v4.0.30319\csc.exe'
}
if (-not (Test-Path $csc)) {
    Write-Error "csc.exe not found. Ensure .NET Framework 4.x is installed."
    exit 1
}

Write-Host "Building silent-launcher.exe ..."
& $csc /nologo /out:$exe /platform:anycpu /target:winexe $cs

if ($LASTEXITCODE -eq 0) {
    Write-Host "Built: $exe"
} else {
    Write-Error "Build failed (exit code $LASTEXITCODE)"
    exit $LASTEXITCODE
}
```

## File: `hooks/hooks.json`
```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "node \"${CLAUDE_PLUGIN_ROOT}/hooks/silent-npx.cjs\" tsx \"${CLAUDE_PLUGIN_ROOT}/scripts/session_start.ts\"",
            "timeout": 5
          },
          {
            "type": "command",
            "command": "node \"${CLAUDE_PLUGIN_ROOT}/hooks/silent-npx.cjs\" tsx \"${CLAUDE_PLUGIN_ROOT}/scripts/sync_letta_memory.ts\"",
            "timeout": 10
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "node \"${CLAUDE_PLUGIN_ROOT}/hooks/silent-npx.cjs\" tsx \"${CLAUDE_PLUGIN_ROOT}/scripts/pretool_sync.ts\"",
            "timeout": 5
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "node \"${CLAUDE_PLUGIN_ROOT}/hooks/silent-npx.cjs\" tsx \"${CLAUDE_PLUGIN_ROOT}/scripts/sync_letta_memory.ts\"",
            "timeout": 10
          }
        ]
      }
    ],
    "Stop": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "node \"${CLAUDE_PLUGIN_ROOT}/hooks/silent-npx.cjs\" tsx \"${CLAUDE_PLUGIN_ROOT}/scripts/send_messages_to_letta.ts\"",
            "timeout": 120,
            "async": true
          }
        ]
      }
    ]
  }
}
```

## File: `hooks/silent-npx.cjs`
```
#!/usr/bin/env node
/**
 * Cross-platform launcher for Claude Subconscious hooks.
 *
 * On Windows: delegates to silent-launcher.exe which creates a headless
 * PseudoConsole (ConPTY) + CREATE_NO_WINDOW to eliminate console window
 * flashes on Windows 11 / Windows Terminal.
 *
 * On other platforms: runs tsx directly via node — no console issue.
 *
 * Called from hooks.json as:
 *   node hooks/silent-npx.cjs tsx scripts/<script>.ts
 */
const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

const isWindows = process.platform === 'win32';
const args = process.argv.slice(2); // e.g. ['tsx', 'path/to/script.ts']

let child;

if (args[0] === 'tsx') {
  const scriptArgs = args.slice(1); // everything after 'tsx'
  const pluginRoot = path.resolve(__dirname, '..');
  const tsxCli = path.join(pluginRoot, 'node_modules', 'tsx', 'dist', 'cli.mjs');

  if (isWindows) {
    const silentLauncher = path.join(__dirname, 'silent-launcher.exe');

    if (fs.existsSync(silentLauncher) && fs.existsSync(tsxCli)) {
      // PseudoConsole + CREATE_NO_WINDOW: popup-free execution
      child = spawn(silentLauncher, ['node', tsxCli, ...scriptArgs], {
        stdio: 'inherit',
        windowsHide: true,
      });
    } else if (fs.existsSync(tsxCli)) {
      // Fallback: run tsx CLI directly (may flash on Windows Terminal)
      child = spawn(process.execPath, [tsxCli, ...scriptArgs], {
        stdio: 'inherit',
        windowsHide: true,
      });
    } else {
      // Last resort: npx through shell
      child = spawn('npx', args, {
        stdio: 'inherit',
        shell: true,
        windowsHide: true,
      });
    }
  } else {
    // Non-Windows: no console window issues
    if (fs.existsSync(tsxCli)) {
      child = spawn(process.execPath, [tsxCli, ...scriptArgs], {
        stdio: 'inherit',
      });
    } else {
      child = spawn('npx', args, {
        stdio: 'inherit',
      });
    }
  }
} else {
  // Non-tsx command: use npx
  child = spawn('npx', args, {
    stdio: 'inherit',
    shell: isWindows,
    windowsHide: isWindows,
  });
}

child.on('exit', (code) => {
  process.exit(code || 0);
});

child.on('error', (err) => {
  console.error('Failed to start subprocess:', err);
  process.exit(1);
});
```

## File: `hooks/SilentLauncher.cs`
```csharp
using System;
using System.IO;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading;

// Silent launcher: PseudoConsole + CREATE_NO_WINDOW (no STARTF_USESTDHANDLES)
// Stdin/stdout delivered via temp files + --require preload.
// This is the ONLY combination that eliminates Windows Terminal popup on Win11 26300.
class SilentLauncher
{
    [DllImport("kernel32.dll", SetLastError = true, CharSet = CharSet.Unicode)]
    static extern bool CreateProcess(
        string lpApplicationName, StringBuilder lpCommandLine,
        IntPtr lpProcessAttributes, IntPtr lpThreadAttributes,
        bool bInheritHandles, uint dwCreationFlags,
        IntPtr lpEnvironment, string lpCurrentDirectory,
        ref STARTUPINFOEX lpStartupInfo, out PROCESS_INFORMATION lpProcessInformation);

    [DllImport("kernel32.dll", SetLastError = true)]
    static extern bool GetExitCodeProcess(IntPtr hProcess, out uint lpExitCode);

    [DllImport("kernel32.dll", SetLastError = true)]
    static extern uint WaitForSingleObject(IntPtr hHandle, uint dwMilliseconds);

    [DllImport("kernel32.dll", SetLastError = true)]
    static extern bool CloseHandle(IntPtr hObject);

    [DllImport("kernel32.dll", SetLastError = true)]
    static extern bool CreatePipe(out IntPtr hReadPipe, out IntPtr hWritePipe,
        ref SECURITY_ATTRIBUTES lpPipeAttributes, uint nSize);

    [DllImport("kernel32.dll", SetLastError = true)]
    static extern bool ReadFile(IntPtr hFile, byte[] lpBuffer, uint nNumberOfBytesToRead,
        out uint lpNumberOfBytesRead, IntPtr lpOverlapped);

    [DllImport("kernel32.dll", SetLastError = true)]
    static extern bool WriteFile(IntPtr hFile, byte[] lpBuffer, uint nNumberOfBytesToWrite,
        out uint lpNumberOfBytesWritten, IntPtr lpOverlapped);

    [DllImport("kernel32.dll", SetLastError = true)]
    static extern IntPtr GetStdHandle(int nStdHandle);

    // ---- PseudoConsole ----
    [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
    static extern int CreatePseudoConsole(COORD size, IntPtr hInput, IntPtr hOutput, uint dwFlags, out IntPtr phPC);

    [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
    static extern void ClosePseudoConsole(IntPtr hPC);

    // ---- Thread Attribute List ----
    [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
    static extern bool InitializeProcThreadAttributeList(IntPtr lpAttributeList, int dwAttributeCount,
        int dwFlags, ref IntPtr lpSize);

    // Win11 26300+ renamed UpdateProcThreadAttributeList to UpdateProcThreadAttribute.
    // Declare both entry points and try the new name first, falling back to the old one.
    [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true, EntryPoint = "UpdateProcThreadAttribute")]
    static extern bool UpdateProcThreadAttribute_New(IntPtr lpAttributeList, uint dwFlags,
        IntPtr Attribute, IntPtr lpValue, IntPtr cbSize, IntPtr lpPreviousValue, IntPtr lpReturnSize);

    [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true, EntryPoint = "UpdateProcThreadAttributeList")]
    static extern bool UpdateProcThreadAttribute_Old(IntPtr lpAttributeList, uint dwFlags,
        IntPtr Attribute, IntPtr lpValue, IntPtr cbSize, IntPtr lpPreviousValue, IntPtr lpReturnSize);

    static bool UpdateProcThreadAttributeSafe(IntPtr attrList, uint flags,
        IntPtr attr, IntPtr val, IntPtr size, IntPtr prev, IntPtr retSize)
    {
        try { return UpdateProcThreadAttribute_New(attrList, flags, attr, val, size, prev, retSize); }
        catch (EntryPointNotFoundException)
        {
            return UpdateProcThreadAttribute_Old(attrList, flags, attr, val, size, prev, retSize);
        }
    }

    [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
    static extern void DeleteProcThreadAttributeList(IntPtr lpAttributeList);

    // ---- Environment ----
    [DllImport("kernel32.dll", SetLastError = true, CharSet = CharSet.Unicode)]
    static extern IntPtr GetEnvironmentStrings();

    [DllImport("kernel32.dll", SetLastError = true, CharSet = CharSet.Unicode)]
    static extern bool FreeEnvironmentStrings(IntPtr lpszEnvironmentBlock);

    [DllImport("kernel32.dll")]
    static extern uint GetLastError();

    [StructLayout(LayoutKind.Sequential)]
    struct COORD { public short X; public short Y; }

    [StructLayout(LayoutKind.Sequential)]
    struct SECURITY_ATTRIBUTES
    {
        public int nLength; public IntPtr lpSecurityDescriptor; public bool bInheritHandle;
    }

    [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Unicode)]
    struct STARTUPINFO
    {
        public int cb; public string lpReserved; public string lpDesktop; public string lpTitle;
        public int dwX; public int dwY; public int dwXSize; public int dwYSize;
        public int dwXCountChars; public int dwYCountChars; public int dwFillAttribute;
        public uint dwFlags; public ushort wShowWindow; public ushort cbReserved2;
        public IntPtr lpReserved2; public IntPtr hStdInput; public IntPtr hStdOutput; public IntPtr hStdError;
    }

    [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Unicode)]
    struct STARTUPINFOEX
    {
        public STARTUPINFO StartupInfo;
        public IntPtr lpAttributeList;
    }

    [StructLayout(LayoutKind.Sequential)]
    struct PROCESS_INFORMATION
    {
        public IntPtr hProcess; public IntPtr hThread; public uint dwProcessId; public uint dwThreadId;
    }

    const uint EXTENDED_STARTUPINFO_PRESENT = 0x00080000;
    const uint CREATE_NO_WINDOW = 0x08000000;
    const uint CREATE_UNICODE_ENVIRONMENT = 0x00000400;
    const uint INFINITE = 0xFFFFFFFF;
    const int STD_OUTPUT_HANDLE = -11;
    const int STD_INPUT_HANDLE = -10;
    static readonly IntPtr PROC_THREAD_ATTRIBUTE_PSEUDOCONSOLE = (IntPtr)0x00020016;

    // Build a Unicode environment block with extra vars prepended
    static IntPtr BuildEnvironmentBlock(string extraVars)
    {
        // Get current environment
        IntPtr envPtr = GetEnvironmentStrings();
        // Parse into string: each var is null-terminated, block ends with double null
        var sb = new StringBuilder();
        sb.Append(extraVars); // already formatted as "KEY=VALUE\0KEY=VALUE\0"
        int offset = 0;
        while (true)
        {
            string entry = Marshal.PtrToStringUni(envPtr + offset * 2);
            if (string.IsNullOrEmpty(entry)) break;
            sb.Append(entry);
            sb.Append('\0');
            offset += entry.Length + 1;
        }
        FreeEnvironmentStrings(envPtr);
        sb.Append('\0'); // double null terminator
        string block = sb.ToString();
        IntPtr blockPtr = Marshal.StringToHGlobalUni(block);
        return blockPtr;
    }

    static int Main(string[] args)
    {
        if (args.Length == 0) return 1;

        // Read all stdin from parent into memory
        IntPtr parentStdin = GetStdHandle(STD_INPUT_HANDLE);
        var allData = new MemoryStream();
        byte[] readBuf = new byte[4096];
        uint bytesRead;
        while (ReadFile(parentStdin, readBuf, (uint)readBuf.Length, out bytesRead, IntPtr.Zero) && bytesRead > 0)
        {
            allData.Write(readBuf, 0, (int)bytesRead);
        }
        byte[] stdinData = allData.ToArray();

        // Create temp files for stdin and stdout
        string tempDir = Path.GetTempPath();
        string stdinFile = Path.Combine(tempDir, "sl-stdin-" + System.Diagnostics.Process.GetCurrentProcess().Id + ".tmp");
        string stdoutFile = Path.Combine(tempDir, "sl-stdout-" + System.Diagnostics.Process.GetCurrentProcess().Id + ".tmp");
        File.WriteAllBytes(stdinFile, stdinData);
        File.WriteAllText(stdoutFile, ""); // create empty

        // Find preload path (same directory as this exe)
        string exeDir = Path.GetDirectoryName(System.Reflection.Assembly.GetExecutingAssembly().Location);
        string preloadPath = Path.Combine(exeDir, "stdio-preload.cjs");

        // Build command line: node --require preload --import tsx/esm script.ts
        // Use tsx as a loader (--import) instead of tsx CLI (which spawns a child process).
        // This runs everything in ONE process so --require preload captures script output.
        var cmdLine = new StringBuilder();
        cmdLine.Append(args[0]); // "node"
        cmdLine.Append(" --require \"");
        cmdLine.Append(preloadPath);
        cmdLine.Append('"');

        // Find tsx ESM loader: derive from tsx CLI path (args[1])
        // args[1] is like ".../node_modules/tsx/dist/cli.mjs"
        // We need ".../node_modules/tsx/dist/esm/index.mjs" as file:// URL
        string tsxCliPath = args[1];
        string tsxDir = Path.GetDirectoryName(tsxCliPath); // .../tsx/dist
        string tsxEsmPath = Path.Combine(tsxDir, "esm", "index.mjs");
        // Convert to file:// URL (forward slashes, no quotes needed)
        string tsxEsmUrl = "file:///" + tsxEsmPath.Replace('\\', '/');
        cmdLine.Append(" --import ");
        cmdLine.Append(tsxEsmUrl);

        // Add the script path (args[2+])
        for (int i = 2; i < args.Length; i++)
        {
            cmdLine.Append(' ');
            string arg = args[i];
            if (arg.Contains(" ") || arg.Contains("\""))
            {
                cmdLine.Append('"');
                cmdLine.Append(arg.Replace("\"", "\\\""));
                cmdLine.Append('"');
            }
            else cmdLine.Append(arg);
        }

        // Build environment block with SL_STDIN_FILE and SL_STDOUT_FILE
        string extraEnv = "SL_STDIN_FILE=" + stdinFile + "\0" + "SL_STDOUT_FILE=" + stdoutFile + "\0";
        IntPtr envBlock = BuildEnvironmentBlock(extraEnv);

        // Create pipes for PseudoConsole (required by API)
        var saNonInherit = new SECURITY_ATTRIBUTES();
        saNonInherit.nLength = Marshal.SizeOf(saNonInherit);
        saNonInherit.bInheritHandle = false;
        saNonInherit.lpSecurityDescriptor = IntPtr.Zero;

        IntPtr ptyInR, ptyInW, ptyOutR, ptyOutW;
        CreatePipe(out ptyInR, out ptyInW, ref saNonInherit, 0);
        CreatePipe(out ptyOutR, out ptyOutW, ref saNonInherit, 0);

        IntPtr hPC;
        var ptySize = new COORD { X = 120, Y = 30 };
        int hr = CreatePseudoConsole(ptySize, ptyInR, ptyOutW, 0, out hPC);
        if (hr != 0)
        {
            Marshal.FreeHGlobal(envBlock);
            return 1;
        }
        CloseHandle(ptyInR);
        CloseHandle(ptyOutW);

        // Set up thread attribute list with pseudoconsole
        IntPtr attrSize = IntPtr.Zero;
        InitializeProcThreadAttributeList(IntPtr.Zero, 1, 0, ref attrSize);
        IntPtr attrList = Marshal.AllocHGlobal((int)attrSize);
        InitializeProcThreadAttributeList(attrList, 1, 0, ref attrSize);

        IntPtr hPCBoxed = Marshal.AllocHGlobal(IntPtr.Size);
        Marshal.WriteIntPtr(hPCBoxed, hPC);
        UpdateProcThreadAttributeSafe(attrList, 0, PROC_THREAD_ATTRIBUTE_PSEUDOCONSOLE,
            hPCBoxed, (IntPtr)IntPtr.Size, IntPtr.Zero, IntPtr.Zero);

        // PseudoConsole + CREATE_NO_WINDOW: no flash, no pipe I/O
        // Stdin/stdout via temp files + preload
        var si = new STARTUPINFOEX();
        si.StartupInfo.cb = Marshal.SizeOf(si);
        // NO STARTF_USESTDHANDLES — that's what causes flashes
        si.lpAttributeList = attrList;

        uint flags = EXTENDED_STARTUPINFO_PRESENT | CREATE_NO_WINDOW | CREATE_UNICODE_ENVIRONMENT;

        PROCESS_INFORMATION pi;
        bool created = CreateProcess(null, cmdLine, IntPtr.Zero, IntPtr.Zero,
            false, flags,
            envBlock, null, ref si, out pi);

        Marshal.FreeHGlobal(envBlock);

        if (!created)
        {
            DeleteProcThreadAttributeList(attrList);
            Marshal.FreeHGlobal(attrList);
            Marshal.FreeHGlobal(hPCBoxed);
            ClosePseudoConsole(hPC);
            return 1;
        }
        CloseHandle(pi.hThread);

        // Drain PTY output (required to prevent deadlock, but output is empty with CREATE_NO_WINDOW)
        var ptyDrainThread = new Thread(() => {
            byte[] buf = new byte[4096]; uint n;
            while (ReadFile(ptyOutR, buf, (uint)buf.Length, out n, IntPtr.Zero) && n > 0) {}
        });
        ptyDrainThread.IsBackground = true;
        ptyDrainThread.Start();

        // Wait for child to exit
        WaitForSingleObject(pi.hProcess, INFINITE);
        uint exitCode;
        GetExitCodeProcess(pi.hProcess, out exitCode);
        // Read captured stdout and relay to parent
        IntPtr parentStdout = GetStdHandle(STD_OUTPUT_HANDLE);
        try
        {
            byte[] stdoutData = File.ReadAllBytes(stdoutFile);
            if (stdoutData.Length > 0)
            {
                uint written;
                WriteFile(parentStdout, stdoutData, (uint)stdoutData.Length, out written, IntPtr.Zero);
            }
        }
        catch { }

        // Cleanup
        ClosePseudoConsole(hPC);
        ptyDrainThread.Join(2000);
        CloseHandle(ptyOutR);
        CloseHandle(ptyInW);
        CloseHandle(pi.hProcess);
        DeleteProcThreadAttributeList(attrList);
        Marshal.FreeHGlobal(attrList);
        Marshal.FreeHGlobal(hPCBoxed);

        // Clean up temp files
        try { File.Delete(stdinFile); } catch { }
        try { File.Delete(stdoutFile); } catch { }

        return (int)exitCode;
    }
}
```

## File: `hooks/stdio-preload.cjs`
```
// Preload: delivers stdin from temp file via unshift, captures stdout to temp file.
// Loaded via --require in the node command line.
// Used with PseudoConsole + CREATE_NO_WINDOW where pipe I/O is not available.
'use strict';

const fs = require('fs');
const stdoutFile = process.env.SL_STDOUT_FILE;
const stdinFile = process.env.SL_STDIN_FILE;

// --- STDIN: Read from temp file, unshift onto existing Socket ---
if (stdinFile) {
  try {
    const data = fs.readFileSync(stdinFile);
    if (data.length > 0) {
      const sock = process.stdin;
      sock.pause();
      sock.unshift(data);
      process.nextTick(() => sock.push(null));
    }
  } catch (e) { /* stdin file may not exist */ }
}

// --- STDOUT/STDERR: Capture all writes to temp file ---
if (stdoutFile) {
  try {
    const fd = fs.openSync(stdoutFile, 'a');

    const origWrite = process.stdout.write.bind(process.stdout);
    process.stdout.write = function(chunk, encoding, callback) {
      try {
        const buf = Buffer.isBuffer(chunk) ? chunk : Buffer.from(chunk, typeof encoding === 'string' ? encoding : 'utf8');
        fs.writeSync(fd, buf);
      } catch (e) { /* ignore write errors */ }
      return origWrite(chunk, encoding, callback);
    };

    const origErrWrite = process.stderr.write.bind(process.stderr);
    process.stderr.write = function(chunk, encoding, callback) {
      try {
        const buf = Buffer.isBuffer(chunk) ? chunk : Buffer.from(chunk, typeof encoding === 'string' ? encoding : 'utf8');
        fs.writeSync(fd, buf);
      } catch (e) { /* ignore write errors */ }
      return origErrWrite(chunk, encoding, callback);
    };

    process.on('exit', () => {
      try { fs.closeSync(fd); } catch(e) {}
    });
  } catch (e) { /* stdout setup error */ }
}
```

## File: `scripts/agent_config.test.ts`
```typescript
/**
 * Tests for agent_config.ts
 *
 * Tests the isValidAgentId() validation function to ensure:
 * - Valid agent IDs are accepted
 * - Invalid agent IDs are rejected with helpful feedback
 *
 * Tests findModel() for model lookup in the available models list.
 * Tests buildLlmConfig() for correct llm_config construction.
 */

import { describe, it, expect, vi, afterEach } from 'vitest';
import { isValidAgentId, findModel, buildLlmConfig } from './agent_config.js';

describe('isValidAgentId', () => {
  describe('valid agent IDs', () => {
    it('should accept a properly formatted agent ID', () => {
      expect(isValidAgentId('agent-a1b2c3d4-e5f6-7890-abcd-ef1234567890')).toBe(true);
    });

    it('should accept agent IDs with uppercase hex characters', () => {
      expect(isValidAgentId('agent-A1B2C3D4-E5F6-7890-ABCD-EF1234567890')).toBe(true);
    });

    it('should accept agent IDs with mixed case hex characters', () => {
      expect(isValidAgentId('agent-a1B2c3D4-e5F6-7890-AbCd-eF1234567890')).toBe(true);
    });

    it('should accept real-world agent ID format', () => {
      expect(isValidAgentId('agent-eed2d657-289a-4842-b00f-d99dd9921ec7')).toBe(true);
    });
  });

  describe('invalid agent IDs - friendly names', () => {
    it('should reject a friendly name like "Memo"', () => {
      expect(isValidAgentId('Memo')).toBe(false);
    });

    it('should reject a friendly name with spaces', () => {
      expect(isValidAgentId('My Agent')).toBe(false);
    });

    it('should reject a friendly name like "Subconscious"', () => {
      expect(isValidAgentId('Subconscious')).toBe(false);
    });
  });

  describe('invalid agent IDs - missing prefix', () => {
    it('should reject UUID without "agent-" prefix', () => {
      expect(isValidAgentId('a1b2c3d4-e5f6-7890-abcd-ef1234567890')).toBe(false);
    });

    it('should reject wrong prefix "agents-"', () => {
      expect(isValidAgentId('agents-a1b2c3d4-e5f6-7890-abcd-ef1234567890')).toBe(false);
    });

    it('should reject wrong prefix "user-"', () => {
      expect(isValidAgentId('user-a1b2c3d4-e5f6-7890-abcd-ef1234567890')).toBe(false);
    });
  });

  describe('invalid agent IDs - malformed UUID', () => {
    it('should reject truncated UUID', () => {
      expect(isValidAgentId('agent-a1b2c3d4-e5f6-7890-abcd')).toBe(false);
    });

    it('should reject UUID with extra characters', () => {
      expect(isValidAgentId('agent-a1b2c3d4-e5f6-7890-abcd-ef1234567890-extra')).toBe(false);
    });

    it('should reject UUID with wrong segment lengths', () => {
      expect(isValidAgentId('agent-a1b2c3d4e5f6-7890-abcd-ef1234567890')).toBe(false);
    });

    it('should reject UUID with invalid characters', () => {
      expect(isValidAgentId('agent-g1b2c3d4-e5f6-7890-abcd-ef1234567890')).toBe(false);
    });
  });

  describe('invalid agent IDs - edge cases', () => {
    it('should reject empty string', () => {
      expect(isValidAgentId('')).toBe(false);
    });

    it('should reject just "agent-"', () => {
      expect(isValidAgentId('agent-')).toBe(false);
    });

    it('should reject whitespace', () => {
      expect(isValidAgentId('  ')).toBe(false);
    });

    it('should reject agent ID with leading/trailing whitespace', () => {
      expect(isValidAgentId(' agent-a1b2c3d4-e5f6-7890-abcd-ef1234567890 ')).toBe(false);
    });

    it('should reject agent ID with newlines', () => {
      expect(isValidAgentId('agent-a1b2c3d4-e5f6-7890-abcd-ef1234567890\n')).toBe(false);
    });
  });
});

// Sample models list used across findModel and buildLlmConfig tests
const SAMPLE_MODELS = [
  { model: 'claude-sonnet-4-5', name: 'claude-sonnet-4-5', provider_type: 'anthropic', handle: 'anthropic/claude-sonnet-4-5' },
  { model: 'gemini-3-pro-preview', name: 'gemini-3-pro-preview', provider_type: 'google_ai', handle: 'google_ai/gemini-3-pro-preview' },
  { model: 'gemini-3-pro-preview', name: 'gemini-3-pro-preview', provider_type: 'google_ai', handle: 'gem1/gemini-3-pro-preview' },
  { model: 'gpt-5.2', name: 'gpt-5.2', provider_type: 'openai', handle: 'openai/gpt-5.2' },
];

describe('findModel', () => {
  it('should find a model by exact handle match', () => {
    const result = findModel(SAMPLE_MODELS, 'anthropic/claude-sonnet-4-5');
    expect(result).not.toBeNull();
    expect(result!.handle).toBe('anthropic/claude-sonnet-4-5');
  });

  it('should find a model by BYOK provider handle', () => {
    const result = findModel(SAMPLE_MODELS, 'gem1/gemini-3-pro-preview');
    expect(result).not.toBeNull();
    expect(result!.handle).toBe('gem1/gemini-3-pro-preview');
  });

  it('should match case-insensitively', () => {
    const result = findModel(SAMPLE_MODELS, 'Anthropic/Claude-Sonnet-4-5');
    expect(result).not.toBeNull();
  });

  it('should match by bare model name', () => {
    const result = findModel(SAMPLE_MODELS, 'gpt-5.2');
    expect(result).not.toBeNull();
    expect(result!.provider_type).toBe('openai');
  });

  it('should return null for unknown model', () => {
    expect(findModel(SAMPLE_MODELS, 'unknown/model')).toBeNull();
  });

  it('should return null for empty models list', () => {
    expect(findModel([], 'anthropic/claude-sonnet-4-5')).toBeNull();
  });
});

describe('buildLlmConfig', () => {
  afterEach(() => {
    delete process.env.LETTA_CONTEXT_WINDOW;
  });

  it('should set model and handle from the model handle', () => {
    const config = buildLlmConfig('anthropic/claude-sonnet-4-5', SAMPLE_MODELS, undefined);
    expect(config.model).toBe('claude-sonnet-4-5');
    expect(config.handle).toBe('anthropic/claude-sonnet-4-5');
    expect(config.provider_name).toBe('anthropic');
  });

  it('should preserve current config settings', () => {
    const current = { model: 'old-model', context_window: 32000, temperature: 0.7 };
    const config = buildLlmConfig('openai/gpt-5.2', SAMPLE_MODELS, current);
    expect(config.model).toBe('gpt-5.2');
    expect(config.context_window).toBe(32000);
    expect(config.temperature).toBe(0.7);
  });

  it('should override context_window from LETTA_CONTEXT_WINDOW env var', () => {
    process.env.LETTA_CONTEXT_WINDOW = '1048576';
    const current = { model: 'old-model', context_window: 32000 };
    const config = buildLlmConfig('openai/gpt-5.2', SAMPLE_MODELS, current);
    expect(config.context_window).toBe(1048576);
  });

  it('should ignore invalid LETTA_CONTEXT_WINDOW values', () => {
    process.env.LETTA_CONTEXT_WINDOW = 'not-a-number';
    const current = { model: 'old-model', context_window: 32000 };
    const config = buildLlmConfig('openai/gpt-5.2', SAMPLE_MODELS, current);
    expect(config.context_window).toBe(32000);
  });

  it('should ignore negative LETTA_CONTEXT_WINDOW values', () => {
    process.env.LETTA_CONTEXT_WINDOW = '-100';
    const current = { model: 'old-model', context_window: 32000 };
    const config = buildLlmConfig('openai/gpt-5.2', SAMPLE_MODELS, current);
    expect(config.context_window).toBe(32000);
  });

  it('should resolve provider_type from the models list', () => {
    const config = buildLlmConfig('gem1/gemini-3-pro-preview', SAMPLE_MODELS, undefined);
    expect(config.provider_name).toBe('gem1');
    expect(config.model_endpoint_type).toBe('google_ai');
  });

  it('should work with no current config', () => {
    const config = buildLlmConfig('openai/gpt-5.2', SAMPLE_MODELS, undefined);
    expect(config.model).toBe('gpt-5.2');
    expect(config.handle).toBe('openai/gpt-5.2');
    expect(config.provider_name).toBe('openai');
  });
});
```

## File: `scripts/agent_config.ts`
```typescript
/**
 * Agent Configuration Utility
 * 
 * Resolves agent ID from (in order):
 * 1. LETTA_AGENT_ID environment variable
 * 2. Saved config file (~/.letta/claude-subconscious/config.json)
 * 3. Auto-import from bundled Subconscious.af
 * 
 * Model configuration:
 * - After agent creation, checks if the agent's model is available
 * - If not available, auto-selects from available models with preference order
 * - LETTA_MODEL environment variable can override (if available on server)
 */

import * as fs from 'fs';
import * as path from 'path';
import { fileURLToPath } from 'url';
import { buildLettaApiUrl } from './letta_api_url.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const CONFIG_DIR = path.join(process.env.HOME || '~', '.letta', 'claude-subconscious');
const CONFIG_FILE = path.join(CONFIG_DIR, 'config.json');
const DEFAULT_AGENT_FILE = path.join(__dirname, '..', 'Subconscious.af');

// Preferred models in order of preference for auto-selection
// Tilted towards quality - Subconscious needs good instruction following and tool use
const PREFERRED_MODELS = [
  'anthropic/claude-sonnet-4-5', // Best for agents per Anthropic
  'openai/gpt-4.1-mini',         // Good balance, 1M context, cheap
  'anthropic/claude-haiku-4-5',  // Fast Claude option
  'openai/gpt-5.2',              // Flagship fallback
  'google_ai/gemini-3-flash',    // Google's balanced option
  'google_ai/gemini-2.5-flash',  // Fallback
];

interface Config {
  agentId?: string;
  importedAt?: string;
  model?: string; // Track which model was configured
}

interface LettaModel {
  model: string;
  name: string;
  provider_type: string;
  handle?: string;
  display_name?: string;
}

interface LlmConfig {
  model?: string;
  handle?: string;
  provider_name?: string;
  model_endpoint_type?: string;
  model_endpoint?: string;
  provider_category?: string;
  context_window?: number;
  max_tokens?: number;
  temperature?: number;
  enable_reasoner?: boolean;
  max_reasoning_tokens?: number;
  [key: string]: unknown;
}

interface AgentDetails {
  id: string;
  name: string;
  llm_config?: LlmConfig;
}

/**
 * Regex for validating Letta agent ID format
 * Format: agent-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx (UUID v4 with 'agent-' prefix)
 */
const AGENT_ID_REGEX = /^agent-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;

/**
 * Validate agent ID format
 * 
 * @param agentId - The agent ID to validate
 * @returns true if valid, false otherwise
 */
export function isValidAgentId(agentId: string): boolean {
  return AGENT_ID_REGEX.test(agentId);
}

/**
 * Get a helpful error message for invalid agent ID format
 */
function getInvalidAgentIdMessage(agentId: string): string {
  const lines = [
    `Invalid LETTA_AGENT_ID format: "${agentId}"`,
    '',
    'The agent ID must be a UUID with the "agent-" prefix.',
    'Expected format: agent-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
    'Example: agent-a1b2c3d4-e5f6-7890-abcd-ef1234567890',
    '',
    'Common mistakes:',
    '  - Using the agent\'s friendly name (e.g., "Memo") instead of the UUID',
    '  - Missing the "agent-" prefix',
    '',
    'To find your agent ID:',
    '  1. Go to https://app.letta.com',
    '  2. Select your agent',
    '  3. Copy the ID from the URL or agent settings',
  ];
  return lines.join('\n');
}

/**
 * Read saved config
 */
function readConfig(): Config {
  if (fs.existsSync(CONFIG_FILE)) {
    try {
      return JSON.parse(fs.readFileSync(CONFIG_FILE, 'utf-8'));
    } catch {
      return {};
    }
  }
  return {};
}

/**
 * Save config
 */
function saveConfig(config: Config): void {
  if (!fs.existsSync(CONFIG_DIR)) {
    fs.mkdirSync(CONFIG_DIR, { recursive: true });
  }
  fs.writeFileSync(CONFIG_FILE, JSON.stringify(config, null, 2), 'utf-8');
}

/**
 * Get original agent name from .af file
 */
function getAgentNameFromFile(): string {
  try {
    const content = JSON.parse(fs.readFileSync(DEFAULT_AGENT_FILE, 'utf-8'));
    // .af files have agents array with name property
    if (content.agents && content.agents.length > 0 && content.agents[0].name) {
      return content.agents[0].name;
    }
  } catch {
    // Fall back to filename
  }
  return path.basename(DEFAULT_AGENT_FILE, '.af');
}

/**
 * Rename an agent
 */
const REQUIRED_AGENT_TAGS = ['git-memory-enabled', 'origin:claude-subconcious'];

/**
 * Ensure required tags are present on an agent.
 * - git-memory-enabled: triggers git-backed memory filesystem
 * - origin:claude-subconcious: identifies agent origin for tracking
 */
async function ensureRequiredAgentTags(apiKey: string, agentId: string, log: (msg: string) => void = console.log): Promise<void> {
  // First GET the agent to read current tags
  const getUrl = buildLettaApiUrl(`/agents/${agentId}`);
  const getResponse = await fetch(getUrl, {
    method: 'GET',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
    },
  });

  if (!getResponse.ok) {
    log(`Warning: Could not fetch agent tags: ${getResponse.status}`);
    return;
  }

  const agent = await getResponse.json();
  const existingTags = agent.tags || [];
  const missingTags = REQUIRED_AGENT_TAGS.filter(tag => !existingTags.includes(tag));

  if (missingTags.length === 0) return;

  const patchUrl = buildLettaApiUrl(`/agents/${agentId}`);
  const response = await fetch(patchUrl, {
    method: 'PATCH',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ tags: [...existingTags, ...missingTags] }),
  });

  if (!response.ok) {
    // Non-fatal - agent still works without required tags
    log(`Warning: Could not update agent tags: ${response.status}`);
  }
}

async function renameAgent(apiKey: string, agentId: string, name: string): Promise<void> {
  const url = buildLettaApiUrl(`/agents/${agentId}`);
  
  const response = await fetch(url, {
    method: 'PATCH',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ name }),
  });

  if (!response.ok) {
    // Non-fatal - agent still works with _copy name
    console.error(`Warning: Could not rename agent: ${response.status}`);
  }
}

/**
 * List available models from Letta server
 */
async function listAvailableModels(apiKey: string): Promise<LettaModel[]> {
  const url = buildLettaApiUrl('/models/');
  
  const response = await fetch(url, {
    method: 'GET',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
    },
  });

  if (!response.ok) {
    throw new Error(`Failed to list models: ${response.status}`);
  }

  return response.json();
}

/**
 * Get agent details including current model configuration
 */
async function getAgentDetails(apiKey: string, agentId: string): Promise<AgentDetails> {
  const url = buildLettaApiUrl(`/agents/${agentId}`);
  
  const response = await fetch(url, {
    method: 'GET',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
    },
  });

  if (!response.ok) {
    throw new Error(`Failed to get agent details: ${response.status}`);
  }

  return response.json();
}

/**
 * Get model handle from agent details
 * The handle format is "provider/model" (e.g., "openai/gpt-4o-mini")
 */
function getAgentModelHandle(agent: AgentDetails): string | null {
  const llmConfig = agent.llm_config;
  if (!llmConfig) return null;
  
  // Try handle first (newer format)
  if (llmConfig.handle) return llmConfig.handle;
  
  // Fall back to constructing from provider and model
  if (llmConfig.provider_name && llmConfig.model) {
    return `${llmConfig.provider_name}/${llmConfig.model}`;
  }
  
  return llmConfig.model || null;
}

/**
 * Check if a model is available on the server
 */
function isModelAvailable(models: LettaModel[], modelHandle: string): boolean {
  return findModel(models, modelHandle) !== null;
}

/**
 * Find a model in the available models list by handle.
 * Returns the matching LettaModel or null.
 */
export function findModel(models: LettaModel[], modelHandle: string): LettaModel | null {
  const normalizedHandle = modelHandle.toLowerCase();

  return models.find(m => {
    const handle = m.handle?.toLowerCase() || `${m.provider_type}/${m.model}`.toLowerCase();
    return handle === normalizedHandle ||
           m.model?.toLowerCase() === normalizedHandle ||
           `${m.provider_type}/${m.name}`.toLowerCase() === normalizedHandle;
  }) || null;
}

/**
 * Select best available model from preferences
 */
function selectBestModel(models: LettaModel[], preferences: string[]): string | null {
  // First, try preferred models in order
  for (const preferred of preferences) {
    if (isModelAvailable(models, preferred)) {
      return preferred;
    }
  }
  
  // Fall back to first available model
  if (models.length > 0) {
    const first = models[0];
    return first.handle || `${first.provider_type}/${first.model}`;
  }
  
  return null;
}

/**
 * Ensure agent's model is available on the server
 * If not, auto-select from available models and update the agent
 * 
 * @returns The model handle that was configured (or null if no change needed)
 */
async function ensureModelAvailable(
  apiKey: string,
  agentId: string,
  log: (msg: string) => void = console.log
): Promise<string | null> {
  try {
    // Get available models and agent details in parallel
    const [models, agent] = await Promise.all([
      listAvailableModels(apiKey),
      getAgentDetails(apiKey, agentId),
    ]);
    
    const currentModel = getAgentModelHandle(agent);
    log(`Agent's current model: ${currentModel || 'unknown'}`);
    log(`Available models: ${models.length} found`);
    
    // Check if LETTA_MODEL env var is set
    const envModel = process.env.LETTA_MODEL;
    if (envModel) {
      if (isModelAvailable(models, envModel)) {
        if (currentModel !== envModel) {
          log(`Using LETTA_MODEL override: ${envModel}`);
          await updateAgentModel(apiKey, agentId, envModel, models, agent.llm_config, log);
          return envModel;
        }
        // Model matches, but check if context_window needs updating
        const envCW = process.env.LETTA_CONTEXT_WINDOW;
        if (envCW && agent.llm_config?.context_window !== parseInt(envCW, 10)) {
          log(`Updating context_window to ${envCW} (was ${agent.llm_config?.context_window})`);
          await updateAgentModel(apiKey, agentId, envModel, models, agent.llm_config, log);
          return envModel;
        }
        return null; // Already using desired model and context_window
      } else {
        log(`Warning: LETTA_MODEL="${envModel}" is not available on this server`);
        log(`Available models: ${models.map(m => m.handle || `${m.provider_type}/${m.model}`).slice(0, 10).join(', ')}${models.length > 10 ? '...' : ''}`);
      }
    }

    // Check if current model is available
    if (currentModel && isModelAvailable(models, currentModel)) {
      log(`Agent's model "${currentModel}" is available`);
      return null; // No change needed
    }

    // Model not available - need to select alternative
    log(`Agent's model "${currentModel}" is NOT available on this server`);

    const selectedModel = selectBestModel(models, PREFERRED_MODELS);
    if (!selectedModel) {
      throw new Error('No models available on this server. Please configure your Letta server with at least one LLM provider.');
    }

    log(`Auto-selecting model: ${selectedModel}`);
    console.log(`\n⚠️  Model Update Required`);
    console.log(`   The Subconscious agent's default model (${currentModel}) is not available.`);
    console.log(`   Auto-selecting: ${selectedModel}`);
    console.log(`   To use a different model, set LETTA_MODEL environment variable.\n`);

    await updateAgentModel(apiKey, agentId, selectedModel, models, agent.llm_config, log);
    return selectedModel;
    
  } catch (error) {
    // Log but don't fail - the agent might still work
    log(`Warning: Could not verify model availability: ${error}`);
    return null;
  }
}

/**
 * Build llm_config for a model handle using metadata from the available models
 * list and the agent's current llm_config as a base.
 *
 * This preserves existing settings (context_window, temperature, etc.) while
 * overriding model-identity fields. If LETTA_CONTEXT_WINDOW is set, it takes
 * precedence over the current value.
 */
export function buildLlmConfig(
  modelHandle: string,
  models: LettaModel[],
  currentConfig: LlmConfig | undefined,
): LlmConfig {
  const slashIdx = modelHandle.indexOf('/');
  const providerName = slashIdx > 0 ? modelHandle.substring(0, slashIdx) : undefined;
  const modelName = slashIdx > 0 ? modelHandle.substring(slashIdx + 1) : modelHandle;

  const modelInfo = findModel(models, modelHandle);

  // Spread current config to preserve settings, then override model fields
  const config: LlmConfig = {
    ...(currentConfig || {}),
    model: modelName,
    handle: modelHandle,
    provider_name: providerName || modelInfo?.provider_type || currentConfig?.provider_name,
    model_endpoint_type: modelInfo?.provider_type || currentConfig?.model_endpoint_type,
  };

  // LETTA_CONTEXT_WINDOW env var overrides the current value
  const envContextWindow = process.env.LETTA_CONTEXT_WINDOW;
  if (envContextWindow) {
    const parsed = parseInt(envContextWindow, 10);
    if (!isNaN(parsed) && parsed > 0) {
      config.context_window = parsed;
    }
  }

  return config;
}

/**
 * Update agent's model configuration via the llm_config PATCH.
 *
 * Uses `{ llm_config: {...} }` instead of `{ model: "..." }` because the
 * top-level model PATCH resets context_window to a server-side default.
 * Sending the full llm_config preserves context_window and other settings.
 */
async function updateAgentModel(
  apiKey: string,
  agentId: string,
  modelHandle: string,
  models: LettaModel[],
  currentConfig: LlmConfig | undefined,
  log: (msg: string) => void = console.log
): Promise<void> {
  const url = buildLettaApiUrl(`/agents/${agentId}`);

  log(`Updating agent model to: ${modelHandle}`);

  const llmConfig = buildLlmConfig(modelHandle, models, currentConfig);

  if (llmConfig.context_window && llmConfig.context_window !== currentConfig?.context_window) {
    log(`Including context_window: ${llmConfig.context_window}`);
  }

  const response = await fetch(url, {
    method: 'PATCH',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ llm_config: llmConfig }),
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`Failed to update agent model: ${response.status} ${errorText}`);
  }

  log(`Agent model updated to: ${modelHandle}`);
}

/**
 * Import agent from .af file
 */
async function importDefaultAgent(apiKey: string): Promise<string> {
  const url = buildLettaApiUrl('/agents/import');
  
  // Read the agent file
  const agentFileContent = fs.readFileSync(DEFAULT_AGENT_FILE);
  
  // Get original name for later rename
  const originalName = getAgentNameFromFile();
  
  // Create form data with the file
  const formData = new FormData();
  const blob = new Blob([agentFileContent], { type: 'application/json' });
  formData.append('file', blob, 'Subconscious.af');
  
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
    },
    body: formData,
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`Failed to import agent: ${response.status} ${errorText}`);
  }

  const result = await response.json();
  
  if (!result.agent_ids || result.agent_ids.length === 0) {
    throw new Error('Import succeeded but no agent ID returned');
  }
  
  const agentId = result.agent_ids[0];
  
  // Rename to original name (removes "_copy" suffix added by import)
  await renameAgent(apiKey, agentId, originalName);
  
  // Ensure required tags are present for memory + origin tracking
  await ensureRequiredAgentTags(apiKey, agentId);
  
  return agentId;
}

/**
 * Get or create agent ID
 * 
 * Returns the agent ID from env var, saved config, or imports the default agent.
 * After getting the agent, verifies the model is available and auto-selects if not.
 */
export async function getAgentId(apiKey: string, log: (msg: string) => void = console.log): Promise<string> {
  let agentId: string;
  let config = readConfig();
  
  // 1. Check environment variable
  const envAgentId = process.env.LETTA_AGENT_ID;
  if (envAgentId) {
    // Validate format before using
    if (!isValidAgentId(envAgentId)) {
      const errorMsg = getInvalidAgentIdMessage(envAgentId);
      log(`WARNING: ${errorMsg}`);
      throw new Error(errorMsg);
    }
    log(`Using agent ID from LETTA_AGENT_ID: ${envAgentId}`);
    agentId = envAgentId;
  }
  // 2. Check saved config
  else if (config.agentId) {
    // Validate saved config (in case it was manually edited or corrupted)
    if (!isValidAgentId(config.agentId)) {
      log(`WARNING: Saved agent ID has invalid format: ${config.agentId}`);
      log(`Ignoring invalid saved config and attempting to import default agent...`);
      // Fall through to import default agent
      agentId = await importAndSaveAgent(apiKey, log);
      config = readConfig(); // Reload config after import
    } else {
      log(`Using saved agent ID: ${config.agentId}`);
      agentId = config.agentId;
    }
  }
  // 3. Import default agent
  else {
    agentId = await importAndSaveAgent(apiKey, log);
    config = readConfig(); // Reload config after import
  }
  
  // 4. Ensure required tags are present (for memory + origin tracking)
  try {
    await ensureRequiredAgentTags(apiKey, agentId, log);
  } catch (error) {
    log(`Warning: Could not ensure required tags: ${error}`);
  }

  // 5. Ensure model is available (auto-select if not)
  try {
    const configuredModel = await ensureModelAvailable(apiKey, agentId, log);
    if (configuredModel && config.model !== configuredModel) {
      // Update saved config with the model that was configured
      saveConfig({
        ...config,
        model: configuredModel,
      });
    }
  } catch (error) {
    log(`Warning: Could not verify model availability: ${error}`);
  }
  
  return agentId;
}

/**
 * Import default agent and save to config
 */
async function importAndSaveAgent(apiKey: string, log: (msg: string) => void): Promise<string> {
  log('No agent configured - importing default Subconscious agent...');
  
  if (!fs.existsSync(DEFAULT_AGENT_FILE)) {
    throw new Error(`Default agent file not found: ${DEFAULT_AGENT_FILE}`);
  }
  
  const agentId = await importDefaultAgent(apiKey);
  log(`Imported agent: ${agentId}`);
  
  // Save for future use
  saveConfig({
    agentId,
    importedAt: new Date().toISOString(),
  });
  log(`Saved agent ID to ${CONFIG_FILE}`);
  
  return agentId;
}

/**
 * Check if we need to import (for quick checks without async)
 */
export function needsImport(): boolean {
  if (process.env.LETTA_AGENT_ID) return false;
  const config = readConfig();
  return !config.agentId;
}

/**
 * Get config file path (for logging/debugging)
 */
export function getConfigPath(): string {
  return CONFIG_FILE;
}
```

## File: `scripts/conversation_utils.test.ts`
```typescript
import { afterEach, describe, expect, it, vi } from 'vitest';

const fetchMock = vi.fn();

vi.stubGlobal('fetch', fetchMock);

describe('createConversation', () => {
  afterEach(() => {
    fetchMock.mockReset();
    vi.unstubAllEnvs();
    vi.resetModules();
  });

  it('uses trailing-slash conversations endpoint with agent_id query', async () => {
    vi.stubEnv('LETTA_BASE_URL', 'https://letta.example.com');

    fetchMock.mockResolvedValue({
      ok: true,
      json: async () => ({ id: 'conversation-123' }),
    });

    const { createConversation } = await import('./conversation_utils.js');
    const conversationId = await createConversation('test-key', 'agent-123');

    expect(conversationId).toBe('conversation-123');
    expect(fetchMock).toHaveBeenCalledTimes(1);
    expect(fetchMock).toHaveBeenCalledWith(
      'https://letta.example.com/v1/conversations/?agent_id=agent-123',
      expect.objectContaining({
        method: 'POST',
        headers: expect.objectContaining({
          Authorization: 'Bearer test-key',
        }),
      }),
    );
  });
});
```

## File: `scripts/conversation_utils.ts`
```typescript
/**
 * Shared conversation and state management utilities
 * Used by sync_letta_memory.ts, send_messages_to_letta.ts, and session_start.ts
 */

import * as fs from 'fs';
import * as os from 'os';
import * as path from 'path';
import { spawn, ChildProcess } from 'child_process';
import { fileURLToPath } from 'url';
import {
  buildLettaApiUrl,
  LETTA_API_BASE,
} from './letta_api_url.js';

// ESM-compatible __dirname
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Configuration
export { LETTA_API_BASE };
// Only show app URL for hosted service; self-hosted users get IDs directly
const IS_HOSTED = !process.env.LETTA_BASE_URL;
const LETTA_APP_BASE = 'https://app.letta.com';

// CLAUDE.md constants
export const CLAUDE_MD_PATH = '.claude/CLAUDE.md';
export const LETTA_SECTION_START = '<letta>';
export const LETTA_SECTION_END = '</letta>';
const LETTA_CONTEXT_START = '<letta_context>';
const LETTA_CONTEXT_END = '</letta_context>';
const LETTA_MEMORY_START = '<letta_memory_blocks>';
const LETTA_MEMORY_END = '</letta_memory_blocks>';

// ============================================
// Mode Configuration
// ============================================

export type LettaMode = 'whisper' | 'full' | 'off';

/**
 * Get the current operating mode from LETTA_MODE env var.
 * - whisper (default): Only inject Sub's messages via stdout
 * - full: Inject full memory blocks + messages via stdout
 * - off: Disable all hooks
 *
 * No mode writes to CLAUDE.md.
 */
export function getMode(): LettaMode {
  const mode = process.env.LETTA_MODE?.toLowerCase();
  if (mode === 'full' || mode === 'off') return mode;
  return 'whisper';
}

/**
 * Get user-specific temp state directory for logs and payloads.
 * Uses os.tmpdir() with a UID suffix to avoid permission conflicts
 * when multiple users share the same machine.
 */
export function getTempStateDir(): string {
  const uid = typeof process.getuid === 'function' ? process.getuid() : process.pid;
  return path.join(os.tmpdir(), `letta-claude-sync-${uid}`);
}

// ============================================
// SDK Tools Configuration
// ============================================

export type SdkToolsMode = 'read-only' | 'full' | 'off';

/** Read-only tool set: safe defaults for background Sub execution */
export const SDK_TOOLS_READ_ONLY = ['Read', 'Grep', 'Glob', 'web_search', 'fetch_webpage'];

/** Tools to always block in SDK sessions (require interactive input) */
export const SDK_TOOLS_BLOCKED = ['AskUserQuestion', 'EnterPlanMode', 'ExitPlanMode'];

/**
 * Get the SDK tools mode from LETTA_SDK_TOOLS env var.
 * - read-only (default): Sub can read files and search the web
 * - full: Sub has full tool access (use with caution)
 * - off: No client-side tools (listen-only, memory operations only)
 */
export function getSdkToolsMode(): SdkToolsMode {
  const mode = process.env.LETTA_SDK_TOOLS?.toLowerCase();
  if (mode === 'full' || mode === 'off') return mode;
  return 'read-only';
}

// Types
export interface SyncState {
  lastProcessedIndex: number;
  sessionId: string;
  conversationId?: string;
  lastBlockValues?: { [label: string]: string };
  lastSeenMessageId?: string;  // Track last message ID we've shown to avoid duplicates
}

export interface ConversationEntry {
  conversationId: string;
  agentId: string;
}

export interface ConversationsMap {
  [sessionId: string]: string | ConversationEntry;
}

export interface Conversation {
  id: string;
  agent_id: string;
  created_at?: string;
}

export type LogFn = (message: string) => void;

// Default no-op logger
const noopLog: LogFn = () => {};

/**
 * Get durable state directory path
 * If LETTA_HOME is set, use that as the base instead of cwd
 */
export function getDurableStateDir(cwd: string): string {
  const base = process.env.LETTA_HOME || cwd;
  return path.join(base, '.letta', 'claude');
}

/**
 * Get conversations map file path
 */
export function getConversationsFile(cwd: string): string {
  return path.join(getDurableStateDir(cwd), 'conversations.json');
}

/**
 * Get sync state file path for a session
 */
export function getSyncStateFile(cwd: string, sessionId: string): string {
  return path.join(getDurableStateDir(cwd), `session-${sessionId}.json`);
}

/**
 * Ensure durable state directory exists
 */
export function ensureDurableStateDir(cwd: string): void {
  const dir = getDurableStateDir(cwd);
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
}

/**
 * Load sync state for a session
 */
export function loadSyncState(cwd: string, sessionId: string, log: LogFn = noopLog): SyncState {
  const statePath = getSyncStateFile(cwd, sessionId);
  
  if (fs.existsSync(statePath)) {
    try {
      const state = JSON.parse(fs.readFileSync(statePath, 'utf-8'));
      log(`Loaded state: lastProcessedIndex=${state.lastProcessedIndex}`);
      return state;
    } catch (e) {
      log(`Failed to load state: ${e}`);
    }
  }
  
  log(`No existing state, starting fresh`);
  return { lastProcessedIndex: -1, sessionId };
}

/**
 * Save sync state for a session
 */
export function saveSyncState(cwd: string, state: SyncState, log: LogFn = noopLog): void {
  ensureDurableStateDir(cwd);
  const statePath = getSyncStateFile(cwd, state.sessionId);
  fs.writeFileSync(statePath, JSON.stringify(state, null, 2), 'utf-8');
  log(`Saved state: lastProcessedIndex=${state.lastProcessedIndex}, conversationId=${state.conversationId}`);
}

/**
 * Load conversations mapping
 */
export function loadConversationsMap(cwd: string, log: LogFn = noopLog): ConversationsMap {
  const filePath = getConversationsFile(cwd);
  if (fs.existsSync(filePath)) {
    try {
      return JSON.parse(fs.readFileSync(filePath, 'utf-8'));
    } catch (e) {
      log(`Failed to load conversations map: ${e}`);
    }
  }
  return {};
}

/**
 * Save conversations mapping
 */
export function saveConversationsMap(cwd: string, map: ConversationsMap): void {
  ensureDurableStateDir(cwd);
  fs.writeFileSync(getConversationsFile(cwd), JSON.stringify(map, null, 2), 'utf-8');
}

/**
 * Create a new conversation for an agent
 */
export async function createConversation(apiKey: string, agentId: string, log: LogFn = noopLog): Promise<string> {
  const url = buildLettaApiUrl('/conversations/', { agent_id: agentId });
  
  log(`Creating new conversation for agent ${agentId}`);
  
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
    },
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`Failed to create conversation: ${response.status} ${errorText}`);
  }

  const conversation: Conversation = await response.json();
  log(`Created conversation: ${conversation.id}`);
  return conversation.id;
}

/**
 * Get or create conversation for a session
 */
export async function getOrCreateConversation(
  apiKey: string,
  agentId: string,
  sessionId: string,
  cwd: string,
  state: SyncState,
  log: LogFn = noopLog
): Promise<string> {
  // Check if we already have a conversation ID in state
  if (state.conversationId) {
    log(`Using existing conversation from state: ${state.conversationId}`);
    return state.conversationId;
  }

  // Check the conversations map
  const conversationsMap = loadConversationsMap(cwd, log);
  const cached = conversationsMap[sessionId];

  if (cached) {
    // Parse both old format (string) and new format (object)
    const entry = typeof cached === 'string'
      ? { conversationId: cached, agentId: null as string | null }
      : cached;

    if (entry.agentId && entry.agentId !== agentId) {
      // Agent ID changed - clear stale entry and create new conversation
      log(`Agent ID changed (${entry.agentId} -> ${agentId}), clearing stale conversation`);
      delete conversationsMap[sessionId];
      const conversationId = await createConversation(apiKey, agentId, log);
      conversationsMap[sessionId] = { conversationId, agentId };
      saveConversationsMap(cwd, conversationsMap);
      state.conversationId = conversationId;
      return conversationId;
    } else if (!entry.agentId) {
      // Old format without agentId - upgrade by recreating
      log(`Upgrading old format entry (no agentId stored), creating new conversation`);
      delete conversationsMap[sessionId];
      const conversationId = await createConversation(apiKey, agentId, log);
      conversationsMap[sessionId] = { conversationId, agentId };
      saveConversationsMap(cwd, conversationsMap);
      state.conversationId = conversationId;
      return conversationId;
    } else {
      // Valid entry with matching agentId - reuse
      log(`Found conversation in map: ${entry.conversationId}`);
      state.conversationId = entry.conversationId;
      return entry.conversationId;
    }
  }

  // No existing entry - create a new conversation
  const conversationId = await createConversation(apiKey, agentId, log);

  // Save to map and state
  conversationsMap[sessionId] = { conversationId, agentId };
  saveConversationsMap(cwd, conversationsMap);
  state.conversationId = conversationId;

  return conversationId;
}

/**
 * Look up an existing conversation from conversations.json without creating a new one
 */
export function lookupConversation(cwd: string, sessionId: string): string | null {
  const conversationsFile = getConversationsFile(cwd);

  if (!fs.existsSync(conversationsFile)) {
    return null;
  }

  try {
    const content = fs.readFileSync(conversationsFile, 'utf-8');
    const conversationsMap: ConversationsMap = JSON.parse(content);
    const cached = conversationsMap[sessionId];

    if (!cached) {
      return null;
    }

    // Handle both legacy (string) and current (object) formats
    return typeof cached === 'string' ? cached : cached.conversationId;
  } catch {
    return null;
  }
}

// ============================================
// Agent and Memory Block Types
// ============================================

export interface MemoryBlock {
  label: string;
  description: string;
  value: string;
}

export interface Agent {
  id: string;
  name: string;
  description?: string;
  blocks: MemoryBlock[];
}

// ============================================
// Agent Fetching
// ============================================

/**
 * Fetch agent data from Letta API
 */
export async function fetchAgent(apiKey: string, agentId: string): Promise<Agent> {
  const url = buildLettaApiUrl(`/agents/${agentId}`, {
    include: 'agent.blocks',
  });

  const response = await fetch(url, {
    method: 'GET',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
    },
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`Letta API error (${response.status}): ${errorText}`);
  }

  return response.json();
}

// ============================================
// XML Escaping Utilities
// ============================================

/**
 * Escape special characters for XML attributes
 */
export function escapeXmlAttribute(str: string): string {
  return str
    .replace(/&/g, '&amp;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/\n/g, ' ');
}

/**
 * Escape special characters for XML element content
 */
export function escapeXmlContent(str: string): string {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

/**
 * Escape special regex characters
 */
export function escapeRegex(str: string): string {
  return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

// ============================================
// CLAUDE.md Formatting and Writing
// ============================================

/**
 * Format the context section with agent info
 */
function formatContextSection(agent: Agent, conversationId: string | null): string {
  const agentName = agent.name || 'Unnamed Agent';
  const agentDesc = agent.description || 'No description provided';

  // For hosted service, show clickable URL; for self-hosted, show IDs
  let locationInfo: string;
  let supervisionInfo: string;
  if (IS_HOSTED) {
    const conversationUrl = conversationId
      ? `${LETTA_APP_BASE}/agents/${agent.id}?conversation=${conversationId}`
      : `${LETTA_APP_BASE}/agents/${agent.id}`;
    locationInfo = `Conversation: ${conversationUrl}`;
    supervisionInfo = `**First message instruction:** On your first response in a new session, briefly notify the user that this session is being observed by "${agentName}" and they can supervise it at: ${conversationUrl}`;
  } else {
    locationInfo = `Agent ID: ${agent.id}${conversationId ? `\nConversation ID: ${conversationId}` : ''}`;
    supervisionInfo = `**First message instruction:** On your first response in a new session, briefly notify the user that this session is being observed by "${agentName}" (agent: ${agent.id}${conversationId ? `, conversation: ${conversationId}` : ''}).`;
  }

  return `${LETTA_CONTEXT_START}
**Subconscious Layer (Letta Agent)**

Agent: ${agentName}
Description: ${agentDesc}
${locationInfo}

This agent maintains persistent memory across your sessions. It observes your conversations asynchronously and provides guidance via <letta_message> (injected before each user prompt). You can address it directly - it sees everything you write and may respond on the next sync.

${supervisionInfo}

Memory blocks below are the agent's long-term storage. Reference as needed.
${LETTA_CONTEXT_END}`;
}

/**
 * Format memory blocks as XML for CLAUDE.md
 */
export function formatMemoryBlocksAsXml(agent: Agent, conversationId: string | null): string {
  const blocks = agent.blocks;
  const contextSection = formatContextSection(agent, conversationId);

  if (!blocks || blocks.length === 0) {
    return `${LETTA_SECTION_START}
${contextSection}

${LETTA_MEMORY_START}
<!-- No memory blocks found -->
${LETTA_MEMORY_END}
${LETTA_SECTION_END}`;
  }

  const formattedBlocks = blocks.map(block => {
    const escapedDescription = escapeXmlAttribute(block.description || '');
    const escapedContent = escapeXmlContent(block.value || '');
    return `<${block.label} description="${escapedDescription}">\n${escapedContent}\n</${block.label}>`;
  }).join('\n');

  return `${LETTA_SECTION_START}
${contextSection}

${LETTA_MEMORY_START}
${formattedBlocks}
${LETTA_MEMORY_END}
${LETTA_SECTION_END}`;
}

/**
 * Update CLAUDE.md with the new Letta memory section
 */
export function updateClaudeMd(projectDir: string, lettaContent: string): void {
  // LETTA_PROJECT sets the base directory; CLAUDE.md goes in {base}/.claude/CLAUDE.md
  const base = process.env.LETTA_PROJECT || projectDir;
  const claudeMdPath = path.join(base, CLAUDE_MD_PATH);

  let existingContent = '';

  if (fs.existsSync(claudeMdPath)) {
    existingContent = fs.readFileSync(claudeMdPath, 'utf-8');
  } else {
    const claudeDir = path.dirname(claudeMdPath);
    if (!fs.existsSync(claudeDir)) {
      fs.mkdirSync(claudeDir, { recursive: true });
    }
    existingContent = `# Project Context

<!-- Letta agent memory is automatically synced below -->
`;
  }

  // Replace or append the <letta> section
  const lettaPattern = `^${escapeRegex(LETTA_SECTION_START)}[\\s\\S]*?^${escapeRegex(LETTA_SECTION_END)}$`;
  const lettaRegex = new RegExp(lettaPattern, 'gm');

  let updatedContent: string;

  if (lettaRegex.test(existingContent)) {
    lettaRegex.lastIndex = 0;
    updatedContent = existingContent.replace(lettaRegex, lettaContent);
  } else {
    updatedContent = existingContent.trimEnd() + '\n\n' + lettaContent + '\n';
  }

  // Clean up any orphaned <letta_message> sections
  const messagePattern = /^<letta_message>[\s\S]*?^<\/letta_message>\n*/gm;
  updatedContent = updatedContent.replace(messagePattern, '');

  updatedContent = updatedContent.trimEnd() + '\n';

  fs.writeFileSync(claudeMdPath, updatedContent, 'utf-8');
}

/**
 * Remove all Letta content from CLAUDE.md (for whisper mode cleanup).
 * If the file was entirely created by us, delete it.
 */
export function cleanLettaFromClaudeMd(projectDir: string): void {
  const base = process.env.LETTA_PROJECT || projectDir;
  const claudeMdPath = path.join(base, CLAUDE_MD_PATH);

  if (!fs.existsSync(claudeMdPath)) {
    return;
  }

  const content = fs.readFileSync(claudeMdPath, 'utf-8');
  const lettaPattern = `^${escapeRegex(LETTA_SECTION_START)}[\\s\\S]*?^${escapeRegex(LETTA_SECTION_END)}\\n*`;
  const lettaRegex = new RegExp(lettaPattern, 'gm');

  if (!lettaRegex.test(content)) {
    return;
  }

  lettaRegex.lastIndex = 0;
  let cleaned = content.replace(lettaRegex, '');

  // Also clean orphaned letta_message blocks
  const messagePattern = /^<letta_message>[\s\S]*?^<\/letta_message>\n*/gm;
  cleaned = cleaned.replace(messagePattern, '');

  // Clean up the auto-generated boilerplate we created
  cleaned = cleaned.replace(/<!-- Letta agent memory is automatically synced below -->\n*/g, '');
  cleaned = cleaned.replace(/^# Project Context\n*/gm, '');

  cleaned = cleaned.trim();

  if (cleaned.length === 0) {
    // File was entirely ours — delete it
    fs.unlinkSync(claudeMdPath);
  } else {
    // User had their own content — just write back without our stuff
    fs.writeFileSync(claudeMdPath, cleaned + '\n', 'utf-8');
  }
}

/**
 * Format all memory blocks for stdout injection (whisper mode, first prompt)
 */
export function formatAllBlocksForStdout(agent: Agent, conversationId: string | null): string {
  const agentName = agent.name || 'Unnamed Agent';
  const blocks = agent.blocks;

  // Build agent info header
  let locationInfo: string;
  if (IS_HOSTED) {
    const conversationUrl = conversationId
      ? `${LETTA_APP_BASE}/agents/${agent.id}?conversation=${conversationId}`
      : `${LETTA_APP_BASE}/agents/${agent.id}`;
    locationInfo = `Supervise: ${conversationUrl}`;
  } else {
    locationInfo = `Agent ID: ${agent.id}${conversationId ? `, Conversation: ${conversationId}` : ''}`;
  }

  const sdkToolsMode = getSdkToolsMode();
  const capabilityLine = sdkToolsMode === 'full'
    ? 'It can read files, search the web, and make changes to your codebase.'
    : sdkToolsMode === 'read-only'
    ? 'It can read files, search your codebase, and browse the web (read-only).'
    : 'It operates in listen-only mode (memory updates only).';

  const header = `<letta_context>
Subconscious agent "${agentName}" is watching this session and whispering guidance.
${capabilityLine}
${locationInfo}
</letta_context>`;

  if (!blocks || blocks.length === 0) {
    return header;
  }

  const formattedBlocks = blocks.map(block => {
    const escapedDescription = escapeXmlAttribute(block.description || '');
    const escapedContent = escapeXmlContent(block.value || '');
    return `<${block.label} description="${escapedDescription}">\n${escapedContent}\n</${block.label}>`;
  }).join('\n');

  return `${header}

<letta_memory_blocks>
${formattedBlocks}
</letta_memory_blocks>`;
}

// ============================================
// Silent Worker Spawning
// ============================================

// Windows compatibility: npx needs to be npx.cmd on Windows
const NPX_CMD = process.platform === 'win32' ? 'npx.cmd' : 'npx';

/**
 * Spawn a background worker process that survives the parent hook's exit.
 *
 * On Windows, uses silent-launcher.exe (PseudoConsole + CREATE_NO_WINDOW)
 * to avoid console window flashes. Falls back gracefully when the launcher
 * or tsx CLI is not available.
 *
 * On other platforms, spawns via npx tsx as a detached process.
 */
export function spawnSilentWorker(
  workerScript: string,
  payloadFile: string,
  cwd: string,
): ChildProcess {
  const isWindows = process.platform === 'win32';
  let child: ChildProcess;

  if (isWindows) {
    // On Windows, spawn workers through silent-launcher.exe (a winexe).
    // detached:true is safe on a winexe (no console flash).
    // The worker gets its own PseudoConsole, so it survives the main
    // script's PseudoConsole being closed by the parent launcher.
    const silentLauncher = path.join(__dirname, '..', 'hooks', 'silent-launcher.exe');
    const tsxCli = path.join(__dirname, '..', 'node_modules', 'tsx', 'dist', 'cli.mjs');
    // Clear SL_ env vars so the worker's launcher instance gets a clean slate
    const workerEnv = { ...process.env };
    delete workerEnv.SL_STDIN_FILE;
    delete workerEnv.SL_STDOUT_FILE;

    if (fs.existsSync(silentLauncher) && fs.existsSync(tsxCli)) {
      child = spawn(silentLauncher, ['node', tsxCli, workerScript, payloadFile], {
        detached: true,
        stdio: 'ignore',
        cwd,
        env: workerEnv,
        windowsHide: true,
      });
    } else if (fs.existsSync(tsxCli)) {
      // Fallback: direct node (may be killed when PseudoConsole closes)
      child = spawn(process.execPath, [tsxCli, workerScript, payloadFile], {
        stdio: 'ignore',
        cwd,
        env: workerEnv,
        windowsHide: true,
      });
    } else {
      // Fallback: use npx through shell (may flash console window)
      child = spawn(NPX_CMD, ['tsx', workerScript, payloadFile], {
        stdio: 'ignore',
        cwd,
        env: workerEnv,
        shell: true,
        windowsHide: true,
      });
    }
  } else {
    child = spawn(NPX_CMD, ['tsx', workerScript, payloadFile], {
      detached: true,
      stdio: 'ignore',
      cwd,
      env: process.env,
    });
  }
  child.unref();
  return child;
}
```

## File: `scripts/letta_api_url.test.ts`
```typescript
import { afterEach, describe, expect, it, vi } from 'vitest';

import {
  buildLettaApiUrl,
  getLettaApiBase,
  normalizeLettaBaseUrl,
} from './letta_api_url.js';

describe('letta_api_url', () => {
  afterEach(() => {
    vi.unstubAllEnvs();
  });

  it('normalizes base URL by trimming trailing slash', () => {
    expect(normalizeLettaBaseUrl('https://example.com/')).toBe(
      'https://example.com',
    );
    expect(normalizeLettaBaseUrl('https://example.com///')).toBe(
      'https://example.com',
    );
  });

  it('builds /v1 base URL unless already present', () => {
    expect(getLettaApiBase('https://example.com')).toBe(
      'https://example.com/v1',
    );
    expect(getLettaApiBase('https://example.com/v1')).toBe(
      'https://example.com/v1',
    );
  });

  it('builds URLs with optional query params', () => {
    const url = buildLettaApiUrl('/agents/agent-123', {
      include: 'agent.blocks',
      limit: 20,
    });

    expect(url).toBe(
      'https://api.letta.com/v1/agents/agent-123?include=agent.blocks&limit=20',
    );
  });

  it('preserves trailing slash path for conversations create endpoint', () => {
    const url = buildLettaApiUrl('/conversations/', { agent_id: 'agent-123' });

    expect(url).toBe(
      'https://api.letta.com/v1/conversations/?agent_id=agent-123',
    );
  });
});
```

## File: `scripts/letta_api_url.ts`
```typescript
/**
 * Shared Letta API URL helpers.
 *
 * Centralizes base URL normalization and endpoint URL construction.
 */

export type LettaApiQueryValue = string | number | boolean | null | undefined;

export type LettaApiQuery = Record<string, LettaApiQueryValue>;

export function normalizeLettaBaseUrl(baseUrl = process.env.LETTA_BASE_URL): string {
  const rawBase = baseUrl?.trim() || 'https://api.letta.com';
  return rawBase.replace(/\/+$/, '');
}

export function getLettaApiBase(baseUrl = process.env.LETTA_BASE_URL): string {
  const normalizedBase = normalizeLettaBaseUrl(baseUrl);
  return normalizedBase.endsWith('/v1')
    ? normalizedBase
    : `${normalizedBase}/v1`;
}

export const LETTA_BASE_URL = normalizeLettaBaseUrl();
export const LETTA_API_BASE = getLettaApiBase();

export function buildLettaApiUrl(
  path: string,
  query: LettaApiQuery = {},
  apiBase: string = LETTA_API_BASE,
): string {
  const normalizedPath = path.startsWith('/') ? path : `/${path}`;
  const normalizedApiBase = apiBase.replace(/\/+$/, '');
  const url = new URL(`${normalizedApiBase}${normalizedPath}`);

  for (const [key, value] of Object.entries(query)) {
    if (value === undefined || value === null) {
      continue;
    }
    url.searchParams.set(key, String(value));
  }

  return url.toString();
}
```

## File: `scripts/pretool_sync.ts`
```typescript
#!/usr/bin/env tsx
/**
 * PreToolUse Memory Sync Script
 * 
 * Lightweight hook that checks for Letta agent updates mid-workflow.
 * Runs before each tool use to inject any new messages or memory changes.
 * 
 * Environment Variables:
 *   LETTA_API_KEY - API key for Letta authentication
 *   LETTA_DEBUG - Set to "1" to enable debug logging
 * 
 * Exit Codes:
 *   0 - Success (no output = no updates, JSON output = updates to inject)
 *   1 - Non-blocking error
 */

import * as fs from 'fs';
import * as readline from 'readline';
import { getAgentId } from './agent_config.js';
import { buildLettaApiUrl } from './letta_api_url.js';
import {
  loadSyncState,
  saveSyncState,
  lookupConversation,
  SyncState,
  getMode,
} from './conversation_utils.js';

const DEBUG = process.env.LETTA_DEBUG === '1';

function debug(...args: unknown[]): void {
  if (DEBUG) {
    console.error('[pretool debug]', ...args);
  }
}

interface HookInput {
  session_id: string;
  cwd: string;
  hook_event_name: string;
  tool_name?: string;
}

interface MemoryBlock {
  label: string;
  value: string;
}

interface Agent {
  id: string;
  name: string;
  blocks: MemoryBlock[];
}

interface LettaMessage {
  id: string;
  message_type: string;
  content?: string;
  text?: string;
  date?: string;
}

interface MessageInfo {
  id: string;
  text: string;
  date: string | null;
}

/**
 * Read hook input from stdin
 */
async function readHookInput(): Promise<HookInput | null> {
  return new Promise((resolve) => {
    let input = '';
    const rl = readline.createInterface({ input: process.stdin });
    
    rl.on('line', (line) => {
      input += line;
    });
    
    rl.on('close', () => {
      if (!input.trim()) {
        resolve(null);
        return;
      }
      try {
        resolve(JSON.parse(input));
      } catch {
        resolve(null);
      }
    });

    setTimeout(() => {
      rl.close();
    }, 100);
  });
}

/**
 * Fetch agent data from Letta API
 */
async function fetchAgent(apiKey: string, agentId: string): Promise<Agent> {
  const url = buildLettaApiUrl(`/agents/${agentId}`, {
    include: 'agent.blocks',
  });
  
  const response = await fetch(url, {
    method: 'GET',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
    },
  });

  if (!response.ok) {
    throw new Error(`Letta API error (${response.status})`);
  }

  return response.json();
}

/**
 * Fetch new assistant messages from the conversation
 */
async function fetchNewMessages(
  apiKey: string, 
  conversationId: string | null,
  lastSeenMessageId: string | null
): Promise<{ messages: MessageInfo[], lastMessageId: string | null }> {
  if (!conversationId) {
    return { messages: [], lastMessageId: null };
  }

  const url = buildLettaApiUrl(`/conversations/${conversationId}/messages`, {
    limit: 20,
  });

  const response = await fetch(url, {
    method: 'GET',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
    },
  });

  if (!response.ok) {
    return { messages: [], lastMessageId: lastSeenMessageId };
  }

  const allMessages: LettaMessage[] = await response.json();
  const assistantMessages = allMessages.filter(msg => msg.message_type === 'assistant_message');

  // Find new messages (API returns newest first)
  let endIndex = assistantMessages.length;
  if (lastSeenMessageId) {
    const lastSeenIndex = assistantMessages.findIndex(msg => msg.id === lastSeenMessageId);
    if (lastSeenIndex !== -1) {
      endIndex = lastSeenIndex;
    }
  }

  const newMessages: MessageInfo[] = [];
  for (let i = 0; i < endIndex; i++) {
    const msg = assistantMessages[i];
    const text = msg.content || msg.text;
    if (text && typeof text === 'string') {
      newMessages.push({
        id: msg.id,
        text,
        date: msg.date || null,
      });
    }
  }

  const lastMessageId = assistantMessages.length > 0 
    ? assistantMessages[0].id 
    : lastSeenMessageId;

  return { messages: newMessages, lastMessageId };
}

/**
 * Detect changed memory blocks
 */
function detectChangedBlocks(
  currentBlocks: MemoryBlock[],
  lastBlockValues: { [label: string]: string } | null
): MemoryBlock[] {
  if (!lastBlockValues) {
    return [];
  }
  
  return currentBlocks.filter(block => {
    const previousValue = lastBlockValues[block.label];
    return previousValue === undefined || previousValue !== block.value;
  });
}

/**
 * Format output for PreToolUse additionalContext
 */
function formatOutput(
  agentName: string,
  messages: MessageInfo[],
  changedBlocks: MemoryBlock[],
  lastBlockValues: { [label: string]: string } | null
): string {
  const parts: string[] = [];

  // Format new messages
  if (messages.length > 0) {
    for (const msg of messages) {
      const timestamp = msg.date || 'unknown';
      parts.push(`<letta_message from="${agentName}" timestamp="${timestamp}">\n${msg.text}\n</letta_message>`);
    }
  }

  // Format changed blocks with diffs
  if (changedBlocks.length > 0) {
    const blockParts = changedBlocks.map(block => {
      const previousValue = lastBlockValues?.[block.label];
      
      if (previousValue === undefined) {
        return `<${block.label} status="new">\n${block.value}\n</${block.label}>`;
      }
      
      // Simple diff: show what changed
      const oldLines = new Set(previousValue.split('\n').map(l => l.trim()).filter(l => l));
      const newLines = block.value.split('\n').map(l => l.trim()).filter(l => l);
      
      const added = newLines.filter(line => !oldLines.has(line));
      const removed = Array.from(oldLines).filter(line => !newLines.includes(line));
      
      if (added.length === 0 && removed.length === 0) {
        return `<${block.label} status="modified">\n${block.value}\n</${block.label}>`;
      }
      
      const diffLines: string[] = [];
      for (const line of removed) {
        diffLines.push(`- ${line}`);
      }
      for (const line of added) {
        diffLines.push(`+ ${line}`);
      }
      
      return `<${block.label} status="modified">\n${diffLines.join('\n')}\n</${block.label}>`;
    });
    
    parts.push(`<letta_memory_update>\n${blockParts.join('\n')}\n</letta_memory_update>`);
  }

  return parts.join('\n\n');
}

/**
 * Main function
 */
async function main(): Promise<void> {
  const mode = getMode();
  if (mode === 'off') {
    process.exit(0);
  }

  const apiKey = process.env.LETTA_API_KEY;
  
  if (!apiKey) {
    debug('No LETTA_API_KEY set, skipping');
    process.exit(0);
  }

  try {
    const hookInput = await readHookInput();
    
    if (!hookInput?.session_id || !hookInput?.cwd) {
      debug('Missing session_id or cwd, skipping');
      process.exit(0);
    }

    debug(`PreToolUse for tool: ${hookInput.tool_name}`);

    // Load state
    const state = loadSyncState(hookInput.cwd, hookInput.session_id);
    
    // Need existing state to detect changes
    if (!state.lastBlockValues && !state.lastSeenMessageId) {
      debug('No previous state, skipping (UserPromptSubmit will handle first sync)');
      process.exit(0);
    }

    // Get agent ID
    const agentId = await getAgentId(apiKey);
    
    // Get conversation ID
    let conversationId = state.conversationId || null;
    if (!conversationId) {
      conversationId = lookupConversation(hookInput.cwd, hookInput.session_id);
    }

    // Fetch current state from Letta
    const [agent, messagesResult] = await Promise.all([
      fetchAgent(apiKey, agentId),
      fetchNewMessages(apiKey, conversationId, state.lastSeenMessageId || null),
    ]);

    const { messages: newMessages, lastMessageId } = messagesResult;
    const changedBlocks = detectChangedBlocks(agent.blocks || [], state.lastBlockValues || null);

    debug(`New messages: ${newMessages.length}, Changed blocks: ${changedBlocks.length}`);

    // If nothing changed, exit silently
    if (newMessages.length === 0 && changedBlocks.length === 0) {
      debug('No updates, exiting silently');
      process.exit(0);
    }

    // Format and output
    const additionalContext = formatOutput(
      agent.name || 'Subconscious',
      newMessages,
      changedBlocks,
      state.lastBlockValues || null
    );

    // Update state
    if (lastMessageId) {
      state.lastSeenMessageId = lastMessageId;
    }
    if (agent.blocks) {
      state.lastBlockValues = {};
      for (const block of agent.blocks) {
        state.lastBlockValues[block.label] = block.value;
      }
    }
    saveSyncState(hookInput.cwd, state);

    // Build the additional context with instruction to surface messages
    let contextWithInstruction = `<letta_update>\n${additionalContext}\n</letta_update>`;
    
    if (newMessages.length > 0) {
      const agentName = agent.name || 'Subconscious';
      contextWithInstruction += `\n\n<instruction>Your Subconscious (${agentName}) just sent a message mid-workflow. Briefly acknowledge what ${agentName} said in your next response - just a short note like "Sub notes: [key point]" so the user knows.</instruction>`;
    }

    // Output JSON for PreToolUse
    const output: Record<string, unknown> = {
      hookSpecificOutput: {
        hookEventName: 'PreToolUse',
        additionalContext: contextWithInstruction,
      },
    };

    console.log(JSON.stringify(output));
    
  } catch (error) {
    debug(`Error: ${error}`);
    // Non-blocking - just exit silently
    process.exit(0);
  }
}

main();
```

## File: `scripts/send_messages_to_letta.ts`
```typescript
#!/usr/bin/env npx tsx
/**
 * Send Messages to Letta Script
 * 
 * Sends Claude Code conversation messages to a Letta agent.
 * This script is designed to run as a Claude Code Stop hook.
 * 
 * Environment Variables:
 *   LETTA_API_KEY - API key for Letta authentication
 *   LETTA_AGENT_ID - Agent ID to send messages to
 * 
 * Hook Input (via stdin):
 *   - session_id: Current session ID
 *   - transcript_path: Path to conversation JSONL file
 *   - stop_hook_active: Whether stop hook is already active
 * 
 * Exit Codes:
 *   0 - Success
 *   1 - Non-blocking error
 * 
 * Log file: $TMPDIR/letta-claude-sync-$UID/send_messages.log
 */

import * as fs from 'fs';
import * as path from 'path';
import { fileURLToPath } from 'url';
import { getAgentId } from './agent_config.js';
import {
  loadSyncState,
  saveSyncState,
  getOrCreateConversation,
  getSyncStateFile,
  spawnSilentWorker,
  getMode,
  getTempStateDir,
  getSdkToolsMode,
} from './conversation_utils.js';
import {
  readTranscript,
  formatMessagesForLetta,
} from './transcript_utils.js';

// ESM-compatible __dirname
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Configuration
const TEMP_STATE_DIR = getTempStateDir();
const LOG_FILE = path.join(TEMP_STATE_DIR, 'send_messages.log');

interface HookInput {
  session_id: string;
  transcript_path: string;
  stop_hook_active?: boolean;
  cwd: string;
  hook_event_name?: string;
}

/**
 * Ensure temp log directory exists
 */
function ensureLogDir(): void {
  if (!fs.existsSync(TEMP_STATE_DIR)) {
    fs.mkdirSync(TEMP_STATE_DIR, { recursive: true });
  }
}

/**
 * Log message to file
 */
function log(message: string): void {
  ensureLogDir();
  const timestamp = new Date().toISOString();
  const logLine = `[${timestamp}] ${message}\n`;
  fs.appendFileSync(LOG_FILE, logLine);
}

/**
 * Read hook input from stdin
 */
async function readHookInput(): Promise<HookInput> {
  return new Promise((resolve, reject) => {
    let data = '';
    process.stdin.setEncoding('utf8');
    process.stdin.on('readable', () => {
      let chunk;
      while ((chunk = process.stdin.read()) !== null) {
        data += chunk;
      }
    });
    process.stdin.on('end', () => {
      try {
        resolve(JSON.parse(data));
      } catch (e) {
        reject(new Error(`Failed to parse hook input: ${e}`));
      }
    });
    process.stdin.on('error', reject);
  });
}


/**
 * Main function
 */
async function main(): Promise<void> {
  log('='.repeat(60));
  log('send_messages_to_letta.ts started');

  const mode = getMode();
  log(`Mode: ${mode}`);
  if (mode === 'off') {
    log('Mode is off, exiting');
    process.exit(0);
  }
  
  // Get environment variables
  const apiKey = process.env.LETTA_API_KEY;

  log(`LETTA_API_KEY: ${apiKey ? 'set (' + apiKey.substring(0, 10) + '...)' : 'NOT SET'}`);

  if (!apiKey) {
    log('ERROR: LETTA_API_KEY not set');
    console.error('Error: LETTA_API_KEY must be set');
    process.exit(1);
  }

  try {
    // Get agent ID (from env, saved config, or auto-import)
    const agentId = await getAgentId(apiKey, log);
    log(`Using agent: ${agentId}`);
    // Read hook input
    log('Reading hook input from stdin...');
    const hookInput = await readHookInput();
    log(`Hook input received:`);
    log(`  session_id: ${hookInput.session_id}`);
    log(`  transcript_path: ${hookInput.transcript_path}`);
    log(`  stop_hook_active: ${hookInput.stop_hook_active}`);
    log(`  hook_event_name: ${hookInput.hook_event_name}`);
    log(`  cwd: ${hookInput.cwd}`);
    
    // Prevent infinite loops if stop hook is already active
    if (hookInput.stop_hook_active) {
      log('Stop hook already active, exiting to prevent loop');
      process.exit(0);
    }

    // Read transcript
    log(`Reading transcript from: ${hookInput.transcript_path}`);
    const messages = await readTranscript(hookInput.transcript_path, log);
    log(`Found ${messages.length} messages in transcript`);
    
    if (messages.length === 0) {
      log('No messages found, exiting');
      process.exit(0);
    }

    // Log message types found
    const typeCounts: Record<string, number> = {};
    for (const msg of messages) {
      const key = msg.type || msg.role || 'unknown';
      typeCounts[key] = (typeCounts[key] || 0) + 1;
    }
    log(`Message types: ${JSON.stringify(typeCounts)}`);

    // Load sync state (from durable storage)
    const state = loadSyncState(hookInput.cwd, hookInput.session_id, log);
    
    // Format new messages
    const newMessages = formatMessagesForLetta(messages, state.lastProcessedIndex, log);
    
    if (newMessages.length === 0) {
      log('No new messages to send after formatting');
      process.exit(0);
    }

    // Get or create conversation for this session
    const conversationId = await getOrCreateConversation(apiKey, agentId, hookInput.session_id, hookInput.cwd, state, log);
    log(`Using conversation: ${conversationId}`);

    // Save state now (with conversation ID) so it persists even if worker fails
    saveSyncState(hookInput.cwd, state, log);

    // Build the message payload (same format as sendBatchToConversation)
    const transcriptEntries = newMessages.map(m => {
      const role = m.role === 'user' ? 'user' : m.role === 'assistant' ? 'claude_code' : 'system';
      const escaped = m.text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
      return `<message role="${role}">\n${escaped}\n</message>`;
    }).join('\n');

    const userMessage = `<claude_code_session_update>
<session_id>${hookInput.session_id}</session_id>

<transcript>
${transcriptEntries}
</transcript>

<instructions>
You may provide commentary or guidance for Claude Code. Your response will be added to Claude's context window on the next prompt. Use this to:
- Offer observations about the user's work
- Provide reminders or context from your memory
- Suggest approaches or flag potential issues
- Send async messages/guidance to Claude Code

Write your response as if speaking directly to Claude Code.
</instructions>
</claude_code_session_update>`;

    // Send via Letta Code SDK (Sub gets client-side tools)
    const sdkToolsMode = getSdkToolsMode();
    log(`SDK tools mode: ${sdkToolsMode}`);

    const payloadFile = path.join(TEMP_STATE_DIR, `payload-${hookInput.session_id}-${Date.now()}.json`);
    const stateFile = getSyncStateFile(hookInput.cwd, hookInput.session_id);

    const sdkPayload = {
      agentId,
      conversationId,
      sessionId: hookInput.session_id,
      message: userMessage,
      stateFile,
      newLastProcessedIndex: messages.length - 1,
      cwd: hookInput.cwd,
      sdkToolsMode,
    };
    fs.writeFileSync(payloadFile, JSON.stringify(sdkPayload), 'utf-8');
    log(`Wrote SDK payload to ${payloadFile}`);

    const workerScript = path.join(__dirname, 'send_worker_sdk.ts');
    const child = spawnSilentWorker(workerScript, payloadFile, hookInput.cwd);
    log(`Spawned SDK worker (PID: ${child.pid})`);

    log('Hook completed (worker running in background)');

  } catch (error) {
    const errorMessage = error instanceof Error ? error.message : String(error);
    log(`ERROR: ${errorMessage}`);
    if (error instanceof Error && error.stack) {
      log(`Stack trace: ${error.stack}`);
    }
    console.error(`Error sending messages to Letta: ${errorMessage}`);
    process.exit(1);
  }
}

// Run main function
main();
```

## File: `scripts/send_worker_sdk.ts`
```typescript
#!/usr/bin/env npx tsx
/**
 * SDK-based background worker that sends messages to Letta via Letta Code SDK.
 * Gives the Subconscious agent client-side tool access (Read, Grep, Glob, etc.).
 *
 * Spawned by send_messages_to_letta.ts as a detached process.
 * Falls back gracefully if the SDK is not available.
 *
 * Usage: npx tsx send_worker_sdk.ts <payload_file>
 */

import * as fs from 'fs';
import * as os from 'os';
import * as path from 'path';

const uid = typeof process.getuid === 'function' ? process.getuid() : process.pid;
const TEMP_STATE_DIR = path.join(os.tmpdir(), `letta-claude-sync-${uid}`);
const LOG_FILE = path.join(TEMP_STATE_DIR, 'send_worker_sdk.log');

interface SdkPayload {
  agentId: string;
  conversationId: string;
  sessionId: string;
  message: string;
  stateFile: string;
  newLastProcessedIndex: number;
  cwd: string;
  sdkToolsMode: 'read-only' | 'full';
}

function log(message: string): void {
  const dir = path.dirname(LOG_FILE);
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
  const timestamp = new Date().toISOString();
  fs.appendFileSync(LOG_FILE, `[${timestamp}] ${message}\n`);
}

async function sendViaSdk(payload: SdkPayload): Promise<boolean> {
  log(`Loading Letta Code SDK...`);

  // Dynamic import so this file can be parsed even if SDK isn't installed
  const { resumeSession } = await import('@letta-ai/letta-code-sdk');

  // Configure tool restrictions based on mode
  const readOnlyTools = ['Read', 'Grep', 'Glob', 'web_search', 'fetch_webpage'];
  const blockedTools = ['AskUserQuestion', 'EnterPlanMode', 'ExitPlanMode'];

  const sessionOptions: Record<string, unknown> = {
    disallowedTools: blockedTools,
    permissionMode: 'bypassPermissions',
    cwd: payload.cwd,
    skillSources: [],          // Sub doesn't need skills
    systemInfoReminder: false, // reduce noise
    sleeptime: { trigger: 'off' }, // don't recurse sleeptime
  };

  if (payload.sdkToolsMode === 'off') {
    // Listen-only: block all client-side tools, Sub can only use memory operations
    sessionOptions.disallowedTools = [...blockedTools, ...readOnlyTools, 'Bash', 'Edit', 'Write', 'Task', 'Glob', 'Grep', 'Read'];
  } else if (payload.sdkToolsMode === 'read-only') {
    sessionOptions.allowedTools = readOnlyTools;
  }
  // 'full' mode: no allowedTools restriction (all tools available)

  const toolsLabel = payload.sdkToolsMode === 'off' ? 'none' : payload.sdkToolsMode === 'read-only' ? readOnlyTools.join(', ') : 'all';
  log(`Creating SDK session for conversation ${payload.conversationId} (mode: ${payload.sdkToolsMode})`);
  log(`  agent: ${payload.agentId}`);
  log(`  cwd: ${payload.cwd}`);
  log(`  allowedTools: ${toolsLabel}`);

  const session = resumeSession(payload.conversationId, sessionOptions);

  try {
    log(`Sending message (${payload.message.length} chars)...`);
    await session.send(payload.message);

    // Stream and capture the response
    let assistantResponse = '';
    let messageCount = 0;

    for await (const msg of session.stream()) {
      messageCount++;
      if (msg.type === 'assistant' && msg.content) {
        assistantResponse += msg.content;
        log(`  Assistant chunk: ${msg.content.substring(0, 100)}...`);
      } else if (msg.type === 'tool_call') {
        log(`  Tool call: ${(msg as any).toolName}`);
      } else if (msg.type === 'error') {
        log(`  Error: ${(msg as any).message}`);
      }
    }

    log(`Stream complete: ${messageCount} messages, assistant response: ${assistantResponse.length} chars`);

    // The SDK session sends the message to the Letta agent which processes it
    // and generates a response. The response is automatically stored in the
    // agent's conversation history on the Letta server. The existing
    // pretool_sync / sync_letta_memory flow will pick it up and inject it
    // into Claude's context on the next prompt.

    return true;

  } finally {
    session.close();
    log('SDK session closed');
  }
}

async function main(): Promise<void> {
  const payloadFile = process.argv[2];

  if (!payloadFile) {
    log('ERROR: No payload file specified');
    process.exit(1);
  }

  log('='.repeat(60));
  log(`SDK Worker started with payload: ${payloadFile}`);

  try {
    if (!fs.existsSync(payloadFile)) {
      log(`ERROR: Payload file not found: ${payloadFile}`);
      process.exit(1);
    }

    const payload: SdkPayload = JSON.parse(fs.readFileSync(payloadFile, 'utf-8'));
    log(`Loaded payload for session ${payload.sessionId}`);

    const success = await sendViaSdk(payload);

    if (success) {
      // Update state file
      const state = JSON.parse(fs.readFileSync(payload.stateFile, 'utf-8'));
      state.lastProcessedIndex = payload.newLastProcessedIndex;
      fs.writeFileSync(payload.stateFile, JSON.stringify(state, null, 2));
      log(`Updated state: lastProcessedIndex=${payload.newLastProcessedIndex}`);
    }

    // Clean up payload file
    fs.unlinkSync(payloadFile);
    log('Cleaned up payload file');
    log('SDK Worker completed successfully');

  } catch (error) {
    const errorMessage = error instanceof Error ? error.message : String(error);
    log(`ERROR: ${errorMessage}`);
    if (error instanceof Error && error.stack) {
      log(`Stack: ${error.stack}`);
    }
    process.exit(1);
  }
}

main();
```

## File: `scripts/session_start.ts`
```typescript
#!/usr/bin/env npx tsx
/**
 * Session Start Hook Script
 *
 * Notifies Letta agent when a new Claude Code session begins.
 * This script is designed to run as a Claude Code SessionStart hook.
 *
 * Environment Variables:
 *   LETTA_API_KEY - API key for Letta authentication
 *   LETTA_AGENT_ID - Agent ID to send messages to
 *
 * Hook Input (via stdin):
 *   - session_id: Current session ID
 *   - cwd: Current working directory
 *   - hook_event_name: "SessionStart"
 *
 * Exit Codes:
 *   0 - Success
 *   1 - Non-blocking error
 *
 * Log file: $TMPDIR/letta-claude-sync-$UID/session_start.log
 */

import * as fs from 'fs';
import * as os from 'os';
import * as path from 'path';
import { getAgentId } from './agent_config.js';
import {
  cleanLettaFromClaudeMd,
  createConversation,
  fetchAgent,
  getMode,
  getTempStateDir,
  getSdkToolsMode,
} from './conversation_utils.js';
import { buildLettaApiUrl } from './letta_api_url.js';

// Configuration
const TEMP_STATE_DIR = getTempStateDir();
const LOG_FILE = path.join(TEMP_STATE_DIR, 'session_start.log');

interface HookInput {
  session_id: string;
  cwd: string;
  hook_event_name?: string;
}

interface ConversationEntry {
  conversationId: string;
  agentId: string;
}

// Support both old format (string) and new format (object) for backward compatibility
interface ConversationsMap {
  [sessionId: string]: string | ConversationEntry;
}

interface Conversation {
  id: string;
  agent_id: string;
  created_at?: string;
}

// Durable storage in .letta directory
// If LETTA_HOME is set, use that as the base instead of cwd
function getDurableStateDir(cwd: string): string {
  const base = process.env.LETTA_HOME || cwd;
  return path.join(base, '.letta', 'claude');
}

function getConversationsFile(cwd: string): string {
  return path.join(getDurableStateDir(cwd), 'conversations.json');
}

function getSyncStateFile(cwd: string, sessionId: string): string {
  return path.join(getDurableStateDir(cwd), `session-${sessionId}.json`);
}

/**
 * Ensure directories exist
 */
function ensureLogDir(): void {
  if (!fs.existsSync(TEMP_STATE_DIR)) {
    fs.mkdirSync(TEMP_STATE_DIR, { recursive: true });
  }
}

function ensureDurableStateDir(cwd: string): void {
  const dir = getDurableStateDir(cwd);
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
}

/**
 * Log message to file
 */
function log(message: string): void {
  ensureLogDir();
  const timestamp = new Date().toISOString();
  const logLine = `[${timestamp}] ${message}\n`;
  fs.appendFileSync(LOG_FILE, logLine);
}

/**
 * Read hook input from stdin
 */
async function readHookInput(): Promise<HookInput> {
  return new Promise((resolve, reject) => {
    let data = '';
    process.stdin.setEncoding('utf8');
    process.stdin.on('readable', () => {
      let chunk;
      while ((chunk = process.stdin.read()) !== null) {
        data += chunk;
      }
    });
    process.stdin.on('end', () => {
      try {
        resolve(JSON.parse(data));
      } catch (e) {
        reject(new Error(`Failed to parse hook input: ${e}`));
      }
    });
    process.stdin.on('error', reject);
  });
}

/**
 * Load conversations mapping
 */
function loadConversationsMap(cwd: string): ConversationsMap {
  const filePath = getConversationsFile(cwd);
  if (fs.existsSync(filePath)) {
    try {
      return JSON.parse(fs.readFileSync(filePath, 'utf-8'));
    } catch (e) {
      log(`Failed to load conversations map: ${e}`);
    }
  }
  return {};
}

/**
 * Save conversations mapping
 */
function saveConversationsMap(cwd: string, map: ConversationsMap): void {
  ensureDurableStateDir(cwd);
  fs.writeFileSync(getConversationsFile(cwd), JSON.stringify(map, null, 2), 'utf-8');
}

/**
 * Save session state
 */
function saveSessionState(cwd: string, sessionId: string, conversationId: string): void {
  ensureDurableStateDir(cwd);
  const state = {
    sessionId,
    conversationId,
    lastProcessedIndex: -1,
    startedAt: new Date().toISOString(),
  };
  fs.writeFileSync(getSyncStateFile(cwd, sessionId), JSON.stringify(state, null, 2), 'utf-8');
}

/**
 * Send session start message to Letta
 */
async function sendSessionStartMessage(
  apiKey: string,
  conversationId: string,
  sessionId: string,
  cwd: string
): Promise<void> {
  const url = buildLettaApiUrl(`/conversations/${conversationId}/messages`);

  const projectName = path.basename(cwd);
  const timestamp = new Date().toISOString();

  const sdkToolsMode = getSdkToolsMode();
  const toolAccessDescription = sdkToolsMode === 'full'
    ? 'Full tool access enabled — you can Read, Grep, Glob, Edit, Write, Bash, and search the web.'
    : sdkToolsMode === 'read-only'
    ? 'Read-only tool access — you can Read, Grep, Glob files and search the web. No writes.'
    : 'Listen-only mode — no client-side tools. You can only update your memory blocks.';

  const message = `<claude_code_session_start>
<project>${projectName}</project>
<path>${cwd}</path>
<session_id>${sessionId}</session_id>
<timestamp>${timestamp}</timestamp>
<sdk_tools_mode>${sdkToolsMode}</sdk_tools_mode>

<context>
A new Claude Code session has begun. I'll be sending you updates as the session progresses.

Tool access: ${toolAccessDescription}
${sdkToolsMode !== 'off' ? `Use your tools to explore the codebase at ${cwd} when processing transcripts.` : ''}
</context>
</claude_code_session_start>`;

  log(`Sending session start message to conversation ${conversationId}`);

  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      messages: [{ role: 'user', content: message }],
    }),
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`Failed to send message: ${response.status} ${errorText}`);
  }

  // Consume stream minimally
  const reader = response.body?.getReader();
  if (reader) {
    try {
      await reader.read();
    } finally {
      reader.cancel();
    }
  }

  log(`Session start message sent successfully`);
}

/**
 * Main function
 */
async function main(): Promise<void> {
  log('='.repeat(60));
  log('session_start.ts started');

  const mode = getMode();
  log(`Mode: ${mode}`);
  if (mode === 'off') {
    log('Mode is off, exiting');
    process.exit(0);
  }

  const apiKey = process.env.LETTA_API_KEY;

  if (!apiKey) {
    log('ERROR: LETTA_API_KEY not set');
    console.error('Error: LETTA_API_KEY must be set');
    process.exit(1);
  }

  // Try to open TTY for user-visible output (bypasses Claude's capture)
  let tty: fs.WriteStream | null = null;
  try {
    tty = fs.createWriteStream('/dev/tty');
  } catch {
    // TTY not available (e.g., non-interactive session)
  }

  const writeTty = (text: string) => {
    if (tty) tty.write(text);
  };

  try {
    // Show initial connecting message with mascot
    writeTty('\n');
    writeTty('\x1b[1m  Claude Subconscious\x1b[0m\n');
    writeTty('\n');
    writeTty('\x1b[35m'); // Purple
    writeTty('  ▐\x1b[31m▛\x1b[35m███\x1b[31m▜\x1b[35m▌\n');
    writeTty(' ▝▜█████▛▘\n');
    writeTty('   ▘▘ ▝▝\n');
    writeTty('\x1b[0m'); // Reset
    writeTty('\x1b[2m  Connecting...\x1b[0m');

    // Get agent ID (from env, saved config, or auto-import)
    const agentId = await getAgentId(apiKey, log);

    // Fetch agent details for display
    const agent = await fetchAgent(apiKey, agentId);
    const agentName = agent.name || 'Unnamed Agent';
    const modelHandle = (agent as any).llm_config?.handle || (agent as any).llm_config?.model || 'unknown';

    // Clear connecting message and show info
    writeTty('\r\x1b[K'); // Clear current line
    writeTty('\n  Agent information:\n');
    writeTty('\x1b[1m'); // Bold
    writeTty(`  ${agentName}\n`);
    writeTty('\x1b[0m'); // Reset
    writeTty('\x1b[2m'); // Dim
    writeTty(`  ${agentId}\n`);
    writeTty('\n');

    // Settings
    const sdkTools = process.env.LETTA_SDK_TOOLS || 'read-only';
    const baseUrl = process.env.LETTA_BASE_URL || 'https://api.letta.com';
    writeTty(`  Model:      ${modelHandle}\n`);
    writeTty(`  Mode:       ${mode}\n`);
    writeTty(`  SDK Tools:  ${sdkTools}\n`);
    if (process.env.LETTA_BASE_URL) {
      writeTty(`  Server:     ${baseUrl}\n`);
    }
    if (process.env.LETTA_HOME) {
      writeTty(`  Home:       ${process.env.LETTA_HOME}\n`);
    }
    writeTty('\n');
    writeTty('  Learn about configuration settings:\n');
    writeTty('  github.com/letta-ai/claude-subconscious\n');
    writeTty('\x1b[0m'); // Reset
    writeTty('\n');
    // Read hook input
    log('Reading hook input from stdin...');
    const hookInput = await readHookInput();
    log(`Hook input: session_id=${hookInput.session_id}, cwd=${hookInput.cwd}`);

    // Check if conversation already exists for this session
    const conversationsMap = loadConversationsMap(hookInput.cwd);

    let conversationId: string;
    const cached = conversationsMap[hookInput.session_id];

    if (cached) {
      // Parse both old format (string) and new format (object)
      const entry = typeof cached === 'string'
        ? { conversationId: cached, agentId: null as string | null }
        : cached;

      if (entry.agentId && entry.agentId !== agentId) {
        // Agent ID changed - clear stale entry and create new conversation
        log(`Agent ID changed (${entry.agentId} -> ${agentId}), clearing stale conversation`);
        delete conversationsMap[hookInput.session_id];
        conversationId = await createConversation(apiKey, agentId, log);
        conversationsMap[hookInput.session_id] = { conversationId, agentId };
        saveConversationsMap(hookInput.cwd, conversationsMap);
      } else if (!entry.agentId) {
        // Old format without agentId - upgrade by recreating
        log(`Upgrading old format entry (no agentId stored), creating new conversation`);
        delete conversationsMap[hookInput.session_id];
        conversationId = await createConversation(apiKey, agentId, log);
        conversationsMap[hookInput.session_id] = { conversationId, agentId };
        saveConversationsMap(hookInput.cwd, conversationsMap);
      } else {
        // Valid entry with matching agentId - reuse
        conversationId = entry.conversationId;
        log(`Reusing existing conversation: ${conversationId}`);
      }
    } else {
      // No existing entry - create new conversation
      conversationId = await createConversation(apiKey, agentId, log);
      conversationsMap[hookInput.session_id] = { conversationId, agentId };
      saveConversationsMap(hookInput.cwd, conversationsMap);
    }

    // Save session state
    saveSessionState(hookInput.cwd, hookInput.session_id, conversationId);

    // Clean up any existing <letta> section from CLAUDE.md (legacy migration)
    log('Cleaning up any legacy CLAUDE.md content...');
    cleanLettaFromClaudeMd(hookInput.cwd);

    // Also clean the global ~/.claude/CLAUDE.md (may have bloat from pre-v1.3.0)
    const homeDir = process.env.HOME || os.homedir();
    if (homeDir !== hookInput.cwd) {
      log('Cleaning up global ~/.claude/CLAUDE.md...');
      cleanLettaFromClaudeMd(homeDir);
    }
    log('CLAUDE.md cleanup done');

    // Show conversation link (only for hosted Letta) - print before blocking send
    const isHosted = !process.env.LETTA_BASE_URL;
    if (isHosted) {
      const convUrl = `https://app.letta.com/agents/${agentId}?conversation=${conversationId}`;
      writeTty('\x1b[2m'); // Dim
      writeTty('  View the subconscious agent:\n');
      writeTty(`  ${convUrl}\n`);
      writeTty('\x1b[0m'); // Reset
      writeTty('\n');
    }

    // Discord link
    writeTty('\x1b[2m'); // Dim
    writeTty('  Come talk to us on Discord:\n');
    writeTty('  https://discord.gg/letta\n');
    writeTty('\x1b[0m'); // Reset
    writeTty('\n');

    // Close TTY before potentially slow network call
    if (tty) tty.end();

    // Send session start message (may take a while, but TTY output is done)
    await sendSessionStartMessage(apiKey, conversationId, hookInput.session_id, hookInput.cwd);

    log('Completed successfully');

  } catch (error) {
    const errorMessage = error instanceof Error ? error.message : String(error);
    log(`ERROR: ${errorMessage}`);

    // Show error to user
    writeTty('\r\x1b[K'); // Clear current line
    writeTty('\x1b[31m'); // Red
    writeTty(`  Letta error: ${errorMessage}\n`);
    writeTty('\x1b[0m'); // Reset
    if (tty) tty.end();

    process.exit(1);
  }
}

main();
```

## File: `scripts/sync_letta_memory.ts`
```typescript
#!/usr/bin/env tsx
/**
 * Letta Memory Sync Script
 * 
 * Syncs Letta agent memory blocks to the project's CLAUDE.md file.
 * This script is designed to run as a Claude Code UserPromptSubmit hook.
 * 
 * Environment Variables:
 *   LETTA_API_KEY - API key for Letta authentication
 *   LETTA_AGENT_ID - Agent ID to fetch memory blocks from
 *   CLAUDE_PROJECT_DIR - Project directory (set by Claude Code)
 *   LETTA_DEBUG - Set to "1" to enable debug logging to stderr
 * 
 * Exit Codes:
 *   0 - Success
 *   1 - Non-blocking error (logged to stderr)
 *   2 - Blocking error (prevents prompt processing)
 */

import * as fs from 'fs';
import * as path from 'path';
import * as readline from 'readline';
import { getAgentId } from './agent_config.js';
import { buildLettaApiUrl } from './letta_api_url.js';
import {
  loadSyncState,
  saveSyncState,
  getOrCreateConversation,
  lookupConversation,
  SyncState,
  Agent,
  MemoryBlock,
  fetchAgent,
  escapeXmlContent,
  formatAllBlocksForStdout,
  cleanLettaFromClaudeMd,
  getMode,
  getTempStateDir,
} from './conversation_utils.js';

// Configuration
const DEBUG = process.env.LETTA_DEBUG === '1';

function debug(...args: unknown[]): void {
  if (DEBUG) {
    console.error('[sync debug]', ...args);
  }
}

interface LettaMessage {
  id: string;
  message_type: string;
  content?: string;
  text?: string;
  date?: string;
}

interface MessageInfo {
  id: string;
  text: string;
  date: string | null;
}

interface HookInput {
  session_id: string;
  cwd: string;
  prompt?: string;  // User's prompt text (available on UserPromptSubmit)
  transcript_path?: string;  // Path to transcript JSONL
}

// Temp state directory for logs
const TEMP_STATE_DIR = getTempStateDir();

/**
 * Read hook input from stdin
 */
async function readHookInput(): Promise<HookInput | null> {
  return new Promise((resolve) => {
    let input = '';
    const rl = readline.createInterface({ input: process.stdin });
    
    rl.on('line', (line) => {
      input += line;
    });
    
    rl.on('close', () => {
      if (!input.trim()) {
        resolve(null);
        return;
      }
      try {
        resolve(JSON.parse(input));
      } catch {
        resolve(null);
      }
    });

    // Timeout after 100ms if no input
    setTimeout(() => {
      rl.close();
    }, 100);
  });
}

/**
 * Detect which blocks have changed since last sync
 */
function detectChangedBlocks(
  currentBlocks: MemoryBlock[],
  lastBlockValues: { [label: string]: string } | null
): MemoryBlock[] {
  // First sync - no previous state, don't show all blocks as "changed"
  if (!lastBlockValues) {
    return [];
  }
  
  return currentBlocks.filter(block => {
    const previousValue = lastBlockValues[block.label];
    // Changed if: new block (not in previous) or value differs
    return previousValue === undefined || previousValue !== block.value;
  });
}

/**
 * Compute a simple line-based diff between two strings
 */
function computeDiff(oldValue: string, newValue: string): { added: string[], removed: string[] } {
  const oldLines = oldValue.split('\n').map(l => l.trim()).filter(l => l);
  const newLines = newValue.split('\n').map(l => l.trim()).filter(l => l);
  
  const oldSet = new Set(oldLines);
  const newSet = new Set(newLines);
  
  const added = newLines.filter(line => !oldSet.has(line));
  const removed = oldLines.filter(line => !newSet.has(line));
  
  return { added, removed };
}

/**
 * Format changed blocks for stdout injection with diffs
 */
function formatChangedBlocksForStdout(
  changedBlocks: MemoryBlock[],
  lastBlockValues: { [label: string]: string } | null
): string {
  if (changedBlocks.length === 0) {
    return '';
  }
  
  const formatted = changedBlocks.map(block => {
    const previousValue = lastBlockValues?.[block.label];
    
    // New block - show full content
    if (previousValue === undefined) {
      const escapedContent = escapeXmlContent(block.value || '');
      return `<${block.label} status="new">\n${escapedContent}\n</${block.label}>`;
    }
    
    // Existing block - show diff
    const diff = computeDiff(previousValue, block.value || '');
    
    if (diff.added.length === 0 && diff.removed.length === 0) {
      // Whitespace-only change, show full content
      const escapedContent = escapeXmlContent(block.value || '');
      return `<${block.label} status="modified">\n${escapedContent}\n</${block.label}>`;
    }
    
    const diffLines: string[] = [];
    for (const line of diff.removed) {
      diffLines.push(`- ${escapeXmlContent(line)}`);
    }
    for (const line of diff.added) {
      diffLines.push(`+ ${escapeXmlContent(line)}`);
    }
    
    return `<${block.label} status="modified">\n${diffLines.join('\n')}\n</${block.label}>`;
  }).join('\n');
  
  return `<letta_memory_update>
<!-- Memory blocks updated since last prompt (showing diff) -->
${formatted}
</letta_memory_update>`;
}

/**
 * Fetch all assistant messages from the conversation history since last seen
 */
async function fetchAssistantMessages(
  apiKey: string, 
  conversationId: string | null,
  lastSeenMessageId: string | null
): Promise<{ messages: MessageInfo[], lastMessageId: string | null }> {
  if (!conversationId) {
    // No conversation yet, return empty
    return { messages: [], lastMessageId: null };
  }

  // Use a high limit because Letta returns multiple entries per logical message
  // (hidden_reasoning + assistant_message pairs), so limit=50 may not reach newest messages
  const url = buildLettaApiUrl(`/conversations/${conversationId}/messages`, {
    limit: 300,
  });

  const response = await fetch(url, {
    method: 'GET',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
    },
  });

  if (!response.ok) {
    // Don't fail if we can't fetch messages, just return empty
    return { messages: [], lastMessageId: lastSeenMessageId };
  }

  const allMessages: LettaMessage[] = await response.json();

  // Filter to assistant messages only, then sort by date descending (newest first)
  // The API does NOT guarantee newest-first ordering — newer messages can appear at the end
  const assistantMessages = allMessages
    .filter(msg => msg.message_type === 'assistant_message')
    .sort((a, b) => {
      const da = a.date ? new Date(a.date).getTime() : 0;
      const db = b.date ? new Date(b.date).getTime() : 0;
      return db - da; // newest first
    });

  // Find the index of the last seen message
  // Since messages are newest-first, new messages are BEFORE lastSeenIndex (indices 0 to lastSeenIndex-1)
  let endIndex = assistantMessages.length; // Default: return all messages
  if (lastSeenMessageId) {
    const lastSeenIndex = assistantMessages.findIndex(msg => msg.id === lastSeenMessageId);
    if (lastSeenIndex !== -1) {
      // Only return messages newer than the last seen one (before it in the array)
      endIndex = lastSeenIndex;
    }
  }
  debug(`endIndex=${endIndex}, will return messages from index 0 to ${endIndex - 1}`);

  // Get new messages (from 0 to endIndex, which are the newest messages)
  const newMessages: MessageInfo[] = [];
  for (let i = 0; i < endIndex; i++) {
    const msg = assistantMessages[i];
    const text = msg.content || msg.text;
    if (text && typeof text === 'string') {
      newMessages.push({
        id: msg.id,
        text,
        date: msg.date || null,
      });
    }
  }
  debug(`Returning ${newMessages.length} new messages`);

  // Get the last message ID for tracking (the NEWEST message, which is first in the array)
  const lastMessageId = assistantMessages.length > 0
    ? assistantMessages[0].id
    : lastSeenMessageId;
  debug(`Setting lastMessageId=${lastMessageId}`);

  return { messages: newMessages, lastMessageId };
}

/**
 * Format assistant messages for stdout injection
 */
function formatMessagesForStdout(agent: Agent, messages: MessageInfo[]): string {
  const agentName = agent.name || 'Letta Agent';
  
  if (messages.length === 0) {
    return `<!-- No new messages from ${agentName} -->`;
  }
  
  // Format each message
  const formattedMessages = messages.map((msg, index) => {
    const timestamp = msg.date || 'unknown';
    const msgNum = messages.length > 1 ? ` (${index + 1}/${messages.length})` : '';
    return `<letta_message from="${agentName}"${msgNum} timestamp="${timestamp}">
${msg.text}
</letta_message>`;
  });
  
  return formattedMessages.join('\n\n');
}

/**
 * Main function
 */
async function main(): Promise<void> {
  // Check mode
  const mode = getMode();
  if (mode === 'off') {
    process.exit(0);
  }

  // Get environment variables
  const apiKey = process.env.LETTA_API_KEY;
  const projectDir = process.env.CLAUDE_PROJECT_DIR || process.cwd();

  // Validate required environment variables
  if (!apiKey) {
    console.error('Error: LETTA_API_KEY environment variable is not set');
    process.exit(1);
  }

  try {
    // Get agent ID (from env, saved config, or auto-import)
    const agentId = await getAgentId(apiKey);
    // Read hook input to get session ID for conversation lookup
    const hookInput = await readHookInput();
    const cwd = hookInput?.cwd || projectDir;
    const sessionId = hookInput?.session_id;
    
    // Load state using shared utility
    let state: SyncState | null = null;
    if (sessionId) {
      state = loadSyncState(cwd, sessionId);
    }
    
    // Recover conversationId from conversations.json if state doesn't have it
    let conversationId = state?.conversationId || null;
    if (!conversationId && sessionId) {
      conversationId = lookupConversation(cwd, sessionId);
      // Update state so we don't have to look it up again
      if (conversationId && state) {
        state.conversationId = conversationId;
      }
    }
    const lastBlockValues = state?.lastBlockValues || null;
    const lastSeenMessageId = state?.lastSeenMessageId || null;

    // Fetch agent data and messages in parallel
    const [agent, messagesResult] = await Promise.all([
      fetchAgent(apiKey, agentId),
      fetchAssistantMessages(apiKey, conversationId, lastSeenMessageId),
    ]);
    
    const { messages: newMessages, lastMessageId } = messagesResult;

    // Detect which blocks have changed since last sync
    const changedBlocks = detectChangedBlocks(agent.blocks || [], lastBlockValues);
    
    // Clean up any existing <letta> section from CLAUDE.md (legacy migration)
    cleanLettaFromClaudeMd(cwd);
    
    // Update state with block values and last seen message ID
    if (state) {
      state.lastBlockValues = {};
      for (const block of agent.blocks || []) {
        state.lastBlockValues[block.label] = block.value;
      }
      // Track the last message we've seen
      if (lastMessageId) {
        state.lastSeenMessageId = lastMessageId;
      }
    }
    
    // Output to stdout - this gets injected before the user's prompt
    // (UserPromptSubmit hooks add stdout to context)
    const outputs: string[] = [];
    
    if (mode === 'full') {
      // Full mode: inject memory blocks + messages
      const isFirstPrompt = !lastBlockValues;
      
      if (isFirstPrompt) {
        outputs.push(formatAllBlocksForStdout(agent, conversationId));
      } else {
        const changedBlocksOutput = formatChangedBlocksForStdout(changedBlocks, lastBlockValues);
        if (changedBlocksOutput) {
          outputs.push(changedBlocksOutput);
        }
      }
    }
    
    // Both modes: inject messages from Sub
    const messageOutput = formatMessagesForStdout(agent, newMessages);
    outputs.push(messageOutput);
    
    // Add instruction to acknowledge messages if there are any
    if (newMessages.length > 0) {
      const agentName = agent.name || 'Subconscious';
      outputs.push(`<instruction>Your Subconscious (${agentName}) sent you a message above. Briefly acknowledge what ${agentName} said - just a short note like "Sub notes: [key point]" so the user knows.</instruction>`);
    }
    
    console.log(outputs.join('\n\n'));
    
    // Save state
    if (state && sessionId) {
      saveSyncState(cwd, state);
    }
    
  } catch (error) {
    const errorMessage = error instanceof Error ? error.message : String(error);
    console.error(`Error syncing Letta memory: ${errorMessage}`);
    // Exit with code 1 for non-blocking error
    // Change to exit(2) if you want to block prompt processing on sync failures
    process.exit(1);
  }
}

// Run main function
main();
```

## File: `scripts/transcript_utils.ts`
```typescript
/**
 * Transcript Utilities
 *
 * Shared utilities for reading and formatting Claude Code transcripts.
 * Used by send_messages_to_letta.ts.
 */

import * as fs from 'fs';
import * as readline from 'readline';

// Types for transcript parsing
export interface ContentBlock {
  type: string;
  text?: string;
  thinking?: string;
  name?: string;        // tool name for tool_use
  id?: string;          // tool_use_id
  input?: any;          // tool input
  tool_use_id?: string; // for tool_result
  content?: string;     // tool result content
  is_error?: boolean;   // tool error flag
}

export interface TranscriptMessage {
  type: string;
  role?: string;
  content?: string | ContentBlock[];
  message?: {
    role?: string;
    content?: string | ContentBlock[];
  };
  tool_name?: string;
  tool_input?: any;
  tool_result?: any;
  timestamp?: string;
  uuid?: string;
  // Summary message fields
  summary?: string;
  // System message fields
  subtype?: string;
  stopReason?: string;
  // File history fields
  snapshot?: {
    trackedFileBackups?: Record<string, any>;
  };
}

export interface ExtractedContent {
  text: string | null;
  thinking: string | null;
  toolUses: Array<{ name: string; input: any }>;
  toolResults: Array<{ toolName: string; content: string; isError: boolean }>;
}

export type LogFn = (message: string) => void;

// Default no-op logger
const noopLog: LogFn = () => {};

/**
 * Read transcript JSONL file and parse messages
 */
export async function readTranscript(transcriptPath: string, log: LogFn = noopLog): Promise<TranscriptMessage[]> {
  if (!fs.existsSync(transcriptPath)) {
    log(`Transcript file not found: ${transcriptPath}`);
    return [];
  }

  const messages: TranscriptMessage[] = [];
  const fileStream = fs.createReadStream(transcriptPath);
  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity
  });

  for await (const line of rl) {
    if (line.trim()) {
      try {
        messages.push(JSON.parse(line));
      } catch (e) {
        log(`Failed to parse transcript line: ${e}`);
      }
    }
  }

  return messages;
}

/**
 * Extract different content types from a message
 */
export function extractAllContent(msg: TranscriptMessage): ExtractedContent {
  const result: ExtractedContent = {
    text: null,
    thinking: null,
    toolUses: [],
    toolResults: [],
  };

  const content = msg.message?.content ?? msg.content;

  if (typeof content === 'string') {
    result.text = content;
    return result;
  }

  if (Array.isArray(content)) {
    const textParts: string[] = [];
    const thinkingParts: string[] = [];

    for (const block of content) {
      if (block.type === 'text' && block.text) {
        textParts.push(block.text);
      } else if (block.type === 'thinking' && block.thinking) {
        thinkingParts.push(block.thinking);
      } else if (block.type === 'tool_use' && block.name) {
        result.toolUses.push({
          name: block.name,
          input: block.input,
        });
      } else if (block.type === 'tool_result') {
        const resultContent = typeof block.content === 'string'
          ? block.content
          : JSON.stringify(block.content);
        result.toolResults.push({
          toolName: block.tool_use_id || 'unknown',
          content: resultContent,
          isError: block.is_error || false,
        });
      }
    }

    if (textParts.length > 0) {
      result.text = textParts.join('\n');
    }
    if (thinkingParts.length > 0) {
      result.thinking = thinkingParts.join('\n');
    }
  }

  return result;
}

/**
 * Truncate text to a maximum length
 */
export function truncate(text: string, maxLength: number): string {
  if (text.length <= maxLength) return text;
  return text.substring(0, maxLength) + '... [truncated]';
}

/**
 * Format messages for Letta with rich context
 */
export function formatMessagesForLetta(
  messages: TranscriptMessage[],
  startIndex: number,
  log: LogFn = noopLog
): Array<{role: string, text: string}> {
  const formatted: Array<{role: string, text: string}> = [];
  const toolNameMap: Map<string, string> = new Map(); // tool_use_id -> tool_name

  log(`Formatting messages from index ${startIndex + 1} to ${messages.length - 1}`);

  for (let i = startIndex + 1; i < messages.length; i++) {
    const msg = messages[i];

    log(`  Message ${i}: type=${msg.type}`);

    // Handle summary messages
    if (msg.type === 'summary' && msg.summary) {
      formatted.push({
        role: 'system',
        text: `[Session Summary]: ${msg.summary}`,
      });
      log(`    -> Added summary`);
      continue;
    }

    // Skip file-history-snapshot and system messages (internal)
    if (msg.type === 'file-history-snapshot' || msg.type === 'system') {
      continue;
    }

    // Handle user messages
    if (msg.type === 'user') {
      const extracted = extractAllContent(msg);

      // User text input
      if (extracted.text) {
        formatted.push({ role: 'user', text: extracted.text });
        log(`    -> Added user message (${extracted.text.length} chars)`);
      }

      // Tool results (these come in user messages)
      for (const toolResult of extracted.toolResults) {
        const toolName = toolNameMap.get(toolResult.toolName) || toolResult.toolName;
        const prefix = toolResult.isError ? '[Tool Error' : '[Tool Result';
        const truncatedContent = truncate(toolResult.content, 1500);
        formatted.push({
          role: 'system',
          text: `${prefix}: ${toolName}]\n${truncatedContent}`,
        });
        log(`    -> Added tool result for ${toolName} (error: ${toolResult.isError})`);
      }
    }

    // Handle assistant messages
    else if (msg.type === 'assistant') {
      const extracted = extractAllContent(msg);

      // Track tool names for later result mapping
      for (const toolUse of extracted.toolUses) {
        if (toolUse.input?.id) {
          toolNameMap.set(toolUse.input.id, toolUse.name);
        }
      }

      // Assistant thinking (summarized)
      if (extracted.thinking) {
        const truncatedThinking = truncate(extracted.thinking, 500);
        formatted.push({
          role: 'assistant',
          text: `[Thinking]: ${truncatedThinking}`,
        });
        log(`    -> Added thinking (${extracted.thinking.length} chars, truncated to 500)`);
      }

      // Tool calls
      for (const toolUse of extracted.toolUses) {
        // Format tool input concisely
        let inputSummary = '';
        if (toolUse.input) {
          if (toolUse.name === 'Read' && toolUse.input.file_path) {
            inputSummary = toolUse.input.file_path;
          } else if (toolUse.name === 'Edit' && toolUse.input.file_path) {
            inputSummary = toolUse.input.file_path;
          } else if (toolUse.name === 'Write' && toolUse.input.file_path) {
            inputSummary = toolUse.input.file_path;
          } else if (toolUse.name === 'Bash' && toolUse.input.command) {
            inputSummary = truncate(toolUse.input.command, 100);
          } else if (toolUse.name === 'Glob' && toolUse.input.pattern) {
            inputSummary = toolUse.input.pattern;
          } else if (toolUse.name === 'Grep' && toolUse.input.pattern) {
            inputSummary = toolUse.input.pattern;
          } else if (toolUse.name === 'WebFetch' && toolUse.input.url) {
            inputSummary = toolUse.input.url;
          } else if (toolUse.name === 'WebSearch' && toolUse.input.query) {
            inputSummary = toolUse.input.query;
          } else if (toolUse.name === 'Task' && toolUse.input.description) {
            inputSummary = toolUse.input.description;
          } else if (toolUse.name === 'AskUserQuestion' && toolUse.input.questions) {
            // Summarize questions being asked
            const questions = toolUse.input.questions;
            if (Array.isArray(questions) && questions.length > 0) {
              inputSummary = questions.map((q: any) => q.question || q.header || '').join('; ');
              inputSummary = truncate(inputSummary, 100);
            }
          } else if (toolUse.name === 'ExitPlanMode') {
            inputSummary = 'Exiting plan mode';
          } else {
            inputSummary = truncate(JSON.stringify(toolUse.input), 100);
          }
        }

        formatted.push({
          role: 'assistant',
          text: `[Tool: ${toolUse.name}] ${inputSummary}`,
        });
        log(`    -> Added tool use: ${toolUse.name}`);
      }

      // Assistant text response
      if (extracted.text) {
        formatted.push({ role: 'assistant', text: extracted.text });
        log(`    -> Added assistant text (${extracted.text.length} chars)`);
      }
    }
  }

  log(`Formatted ${formatted.length} messages total`);
  return formatted;
}

/**
 * Format messages as XML transcript entries for Letta API
 */
export function formatAsXmlTranscript(messages: Array<{role: string, text: string}>): string {
  return messages.map(m => {
    const role = m.role === 'user' ? 'user' : m.role === 'assistant' ? 'claude_code' : 'system';
    // Escape XML special chars in text
    const escaped = m.text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    return `<message role="${role}">\n${escaped}\n</message>`;
  }).join('\n');
}
```

