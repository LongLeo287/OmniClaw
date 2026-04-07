---
id: tinyclaw
type: knowledge
owner: OA_Triage
---
# tinyclaw
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "tinyagi",
  "version": "0.0.20",
  "description": "Multi-agent, multi-team, multi-channel 24/7 AI assistant",
  "workspaces": [
    "packages/*"
  ],
  "bin": {
    "tinyagi": "packages/cli/bin/tinyagi.mjs"
  },
  "scripts": {
    "build": "tsc --build",
    "dev": "concurrently -k -n core,teams,server,main \"npm run dev -w @tinyagi/core\" \"npm run dev -w @tinyagi/teams\" \"npm run dev -w @tinyagi/server\" \"npm run dev -w @tinyagi/main\"",
    "build:core": "npm run build -w @tinyagi/core",
    "build:teams": "npm run build -w @tinyagi/teams",
    "build:channels": "npm run build -w @tinyagi/channels",
    "build:server": "npm run build -w @tinyagi/server",
    "build:visualizer": "npm run build -w @tinyagi/visualizer",
    "start": "npm run start -w @tinyagi/main",
    "discord": "npm run discord -w @tinyagi/channels",
    "telegram": "npm run telegram -w @tinyagi/channels",
    "whatsapp": "npm run whatsapp -w @tinyagi/channels",
    "server": "npm run start -w @tinyagi/server",
    "visualize": "npm run visualize -w @tinyagi/visualizer",
    "chatroom": "npm run chatroom -w @tinyagi/visualizer"
  },
  "devDependencies": {
    "@types/node": "^25.2.2",
    "concurrently": "^9.2.1",
    "nodemon": "^3.1.9",
    "typescript": "^5.9.3"
  },
  "dependencies": {
    "croner": "^10.0.1"
  },
  "puppeteer": {
    "skipDownload": true
  }
}

```

### File: README.md
```md
<div align="center">
  <img src="./docs/images/tinyagi.png" alt="TinyAGI" width="600" />
  <h1>TinyAGI 🦞</h1>
  <p><strong>Multi-agent, Multi-team, Multi-channel, 24/7 AI assistant</strong></p>
  <p>Run multiple teams of AI agents that collaborate with each other simultaneously with isolated workspaces.</p>
  <p>
    <img src="https://img.shields.io/badge/stability-experimental-orange.svg" alt="Experimental" />
    <a href="https://opensource.org/licenses/MIT">
      <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License" />
    </a>
    <a href="https://discord.gg/jH6AcEChuD">
      <img src="https://img.shields.io/discord/1353722981163208785?logo=discord&logoColor=white&label=Discord&color=7289DA" alt="Discord" />
    </a>
    <a href="https://github.com/TinyAGI/tinyagi/releases/latest">
      <img src="https://img.shields.io/github/v/release/TinyAGI/tinyagi?label=Latest&color=green" alt="Latest Release" />
    </a>
  </p>
</div>

<div align="center">
  <video src="https://github.com/user-attachments/assets/c5ef5d3c-d9cf-4a00-b619-c31e4380df2e" width="600" controls></video>
</div>

## ✨ Features

- ✅ **Multi-agent** - Run multiple isolated AI agents with specialized roles
- ✅ **Multi-team collaboration** - Agents hand off work to teammates via chain execution and fan-out
- ✅ **Multi-channel** - Discord, WhatsApp, and Telegram
- ✅ **Web portal (TinyOffice)** - Browser-based dashboard for chat, agents, teams, tasks, logs, and settings
- ✅ **Team chat rooms** - Persistent async chat rooms per team with real-time CLI viewer
- ✅ **Multiple AI providers** - Anthropic Claude, OpenAI Codex, and custom providers (any OpenAI/Anthropic-compatible endpoint)
- ✅ **Auth token management** - Store API keys per provider, no separate CLI auth needed
- ✅ **Parallel processing** - Agents process messages concurrently
- ✅ **Live TUI dashboard** - Real-time team visualizer and chatroom viewer
- ✅ **Persistent sessions** - Conversation context maintained across restarts
- ✅ **SQLite queue** - Atomic transactions, retry logic, dead-letter management
- ✅ **Plugin system** - Extend TinyAGI with custom plugins for message hooks and event listeners
- ✅ **24/7 operation** - Runs as a background process or Docker container

## Community

[Discord](https://discord.com/invite/jH6AcEChuD)

We are actively looking for contributors. Please reach out.

## 🚀 Quick Start

### Prerequisites

- macOS, Linux and Windows (WSL2)
- Node.js v18+
- [Claude Code CLI](https://claude.com/claude-code) (for Anthropic provider)
- [Codex CLI](https://docs.openai.com/codex) (for OpenAI provider)

### Installation & First Run

```bash
curl -fsSL https://raw.githubusercontent.com/TinyAGI/tinyagi/main/scripts/install.sh | bash
```

This downloads and installs the `tinyagi` command globally. Then just run:

```bash
tinyagi
```

That's it. TinyAGI auto-creates default settings, starts the daemon, and opens TinyOffice in your browser. No wizard, no configuration needed.

- **Default workspace:** `~/tinyagi-workspace`
- **Default agent:** `tinyagi` (Anthropic/Opus)
- **Channels:** none initially — add later with `tinyagi channel setup`

<details>
<summary><b>Development (run from source repo)</b></summary>

```bash
git clone https://github.com/TinyAGI/tinyagi.git
cd tinyagi && npm install && npm run build
npx tinyagi start
npx tinyagi agent list
```
</details>

<details>
<summary><b>Other installation methods</b></summary>

**From Source:**

```bash
git clone https://github.com/TinyAGI/tinyagi.git
cd tinyagi && npm install && ./scripts/install.sh
```

</details>

<details>
<summary><b>🐳 Docker</b></summary>

```bash
docker compose up -d
```

Set your API key in a `.env` file or pass it directly:

```bash
ANTHROPIC_API_KEY=sk-ant-... docker compose up -d
```

The API runs on `http://localhost:3777`. Data is persisted in a `tinyagi-data` Docker volume.

</details>

<details>
<summary><b>📱 Channel Setup Guides</b></summary>

### Discord Setup

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create application → Bot section → Create bot
3. Copy bot token
4. Enable "Message Content Intent"
5. Invite bot using OAuth2 URL Generator

### Telegram Setup

1. Open Telegram → Search `@BotFather`
2. Send `/newbot` → Follow prompts
3. Copy bot token
4. Start chat with your bot

### WhatsApp Setup

After starting TinyAGI, scan the QR code:

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
     WhatsApp QR Code
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[QR CODE HERE]

📱 Settings → Linked Devices → Link a Device
```

</details>

---

## 🌐 TinyOffice Web Portal

TinyAGI includes a web portal for managing your agents, teams, tasks, and chat — all from the browser.

<div align="center">
  <img src="./docs/images/tinyoffice.png" alt="TinyOffice Office View" width="700" />
</div>

Once you start running TinyAGI locally, you can control it by visiting **[office.tinyagicompany.com](https://office.tinyagicompany.com/)**. It connects to your local TinyAGI API at `localhost:3777` — no account or sign-up needed.

Alternatively, you can run TinyOffice locally:

```bash
tinyagi office  # Builds and starts on http://localhost:3000
```

<details>
<summary><b>TinyOffice Features & Setup</b></summary>

- **Dashboard** - Real-time queue/system overview and live event feed
- **Chat Console** - Send messages to default agent, `@agent`, or `@team`
- **Agents & Teams** - Create, edit, and remove agents/teams
- **Tasks (Kanban)** - Create tasks, drag across stages, assign to agent/team
- **Logs & Events** - Inspect queue logs and streaming events
- **Settings** - Edit TinyAGI configuration (`settings.json`) via UI
- **Office View** - Visual simulation of agent interactions
- **Org Chart** - Hierarchical visualization of teams and agents
- **Chat Rooms** - Slack-style persistent chat rooms per team
- **Projects** - Project-level task management with filtered kanban boards

### Running Locally

Start TinyAGI first (API default: `http://localhost:3777`), then:

```bash
tinyagi office
```

This auto-detects when dependencies or builds are needed (e.g. after `tinyagi update`) and starts the production server on `http://localhost:3000`.

For development with hot-reload:

```bash
cd tinyoffice
npm install
npm run dev
```

If TinyAGI API is on a different host/port, set:

```bash
cd tinyoffice
echo 'NEXT_PUBLIC_API_URL=http://localhost:3777' > .env.local
```

</details>

## 📋 Commands

Commands work with the `tinyagi` CLI.

### Core Commands

| Command       | Description                                               | Example               |
| ------------- | --------------------------------------------------------- | --------------------- |
| *(no command)* | Install, configure defaults, start, and open TinyOffice  | `tinyagi`            |
| `start`       | Start TinyAGI daemon                                     | `tinyagi start`      |
| `stop`        | Stop all processes                                        | `tinyagi stop`       |
| `restart`     | Restart TinyAGI                                          | `tinyagi restart`    |
| `status`      | Show current status and activity                          | `tinyagi status`     |
| `channel setup` | Configure channels interactively                        | `tinyagi channel setup` |
| `logs [type]` | View logs (discord/telegram/whatsapp/queue/heartbeat/all) | `tinyagi logs queue` |

### Agent Commands

| Command                               | Description                     | Example                                                      |
| ------------------------------------- | ------------------------------- | ------------------------------------------------------------ |
| `agent list`                          | List all configured agents      | `tinyagi agent list`                                        |
| `agent add`                           | Add new agent (interactive)     | `tinyagi agent add`                                         |
| `agent show <id>`                     | Show agent configuration        | `tinyagi agent show coder`                                  |
| `agent remove <id>`                   | Remove an agent                 | `tinyagi agent remove coder`                                |
| `agent reset <id>`                    | Reset agent conversation        | `tinyagi agent reset coder`                                 |
| `agent provider <id> [provider]`      | Show or set agent's AI provider | `tinyagi agent provider coder anthropic`                    |
| `agent provider <id> <p> --model <m>` | Set agent's provider and model  | `tinyagi agent provider coder openai --model gpt-5.3-codex` |

### Team Commands

| Command                     | Description                        | Example                                   |
| --------------------------- | ---------------------------------- | ----------------------------------------- |
| `team list`                 | List all configured teams          | `tinyagi team list`                      |
| `team add`                  | Add new team (interactive)         | `tinyagi team add`                       |
| `team show <id>`            | Show team configuration            | `tinyagi team show dev`                  |
| `team remove <id>`          | Remove a team                      | `tinyagi team remove dev`                |
| `team add-agent <t> <a>`    | Add an existing agent to a team    | `tinyagi team add-agent dev reviewer`    |
| `team remove-agent <t> <a>` | Remove an agent from a team        | `tinyagi team remove-agent dev reviewer` |
| `team visualize [id]`       | Live TUI dashboard for team chains | `tinyagi team visualize dev`             |

### Chatroom Commands

| Command             | Description                                   | Example                    |
| ------------------- | --------------------------------------------- | -------------------------- |
| `chatroom <team>`   | Real-time TUI viewer with type-to-send        | `tinyagi chatroom dev`    |
| `office`            | Start TinyOffice web portal on port 3000      | `tinyagi office`          |

Every team has a persistent chat room. Agents post to it using `[#team_id: message]` tags, and messages are broadcast to all teammates. The chatroom viewer polls for new messages in real time — type a message and press Enter to post, or press `q`/Esc to quit.

**API endpoints:**

```
GET  /api/chatroom/:teamId          # Get messages (?limit=100&since=0)
POST /api/chatroom/:teamId          # Post a message (body: { "message": "..." })
```

### Provider & Custom Provider Commands

| Command                                       | Description                                              | Example                                          |
| --------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------ |
| `provider [name]`                             | Show or switch global AI provider                        | `tinyagi provider anthropic`                    |
| `provider <name> --model <model>`             | Switch provider and model; propagates to matching agents | `tinyagi provider openai --model gpt-5.3-codex` |
| `provider <name> --oauth-token <token>`        | Store OAuth token for a built-in provider                | `tinyagi provider anthropic --oauth-token sk-ant-oat01-...` |
| `provider list`                               | List all custom providers                                | `tinyagi provider list`                         |
| `provider add`                                | Add a new custom provider (interactive)                  | `tinyagi provider add`                          |
| `provider remove <id>`                        | Remove a custom provider                                 | `tinyagi provider remove proxy`                 |
| `model [name]`                                | Show or switch AI model                                  | `tinyagi model opus`                            |

<details>
<summary><b>Custom provider details</b></summary>

Custom providers let you use any OpenAI or Anthropic-compatible API endpoint (e.g., OpenRouter, proxy servers, self-hosted models).

**Define a custom provider in `settings.json`:**

```json
{
  "custom_providers": {
    "my-proxy": {
      "name": "My Proxy",
      "harness": "claude",
      "base_url": "https://proxy.example.com/v1",
      "api_key": "sk-...",
      "model": "claude-sonnet-4-6"
    }
  }
}
```

| Field      | Required | Description                          |
| ---------- | -------- | ------------------------------------ |
| `name`     | Yes      | Human-readable display name          |
| `harness`  | Yes      | CLI to use: `claude` or `codex`      |
| `base_url` | Yes      | API endpoint URL                     |
| `api_key`  | Yes      | API key for authentication           |
| `model`    | No       | Default model name for CLI           |

**Assign a custom provider to an agent:**

```bash
tinyagi agent provider coder custom:my-proxy
tinyagi agent provider coder custom:my-proxy --model gpt-4o
```

**Auth token storage** — store credentials for built-in providers so you don't need separate CLI auth:

```bash
tinyagi provider anthropic --oauth-token sk-ant-oat01-...
tinyagi provider anthropic --api-key sk-ant-...
tinyagi provider openai --api-key sk-...
```

Anthropic supports both `oauth_token` (exported as `CLAUDE_CODE_OAUTH_TOKEN`) and `api_key` (exported as `ANTHROPIC_API_KEY`). OAuth takes priority if both are set. OpenAI keys are saved as `models.openai.api_key` and exported as `OPENAI_API_KEY`. If nothing is configured, the process inherits environment variables directly.

**API endpoints:**

```
GET    /api/custom-providers              # List custom providers
PUT    /api/custom-providers/:id          # Create or update
DELETE /api/custom-providers/:id          # Delete
```

See [docs/AGENTS.md](docs/AGENTS.md#custom-providers) for more details.

</details>

<details>
<summary><b>Pairing commands</b></summary>

Use sender pairing to control who can message your agents.

| Command                                | Description                                        | Example                                    |
| -------------------------------------- | -------------------------------------------------- | ------------------------------------------ |
| `pairing pending`                      | Show pending sender approvals (with pairing codes) | `tinyagi pairing pending`                 |
| `pairing approved`                     | Show approved senders                              | `tinyagi pairing approved`                |
| `pairing list`                         | Show both pending and approved senders             | `tinyagi pairing list`                    |
| `pairing approve <code>`               | Move a sender from pending to approved by code     | `tinyagi pairing approve ABCD1234`
... [TRUNCATED]
```

### File: packages\channels\package.json
```json
{
  "name": "@tinyagi/channels",
  "version": "0.0.10",
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "scripts": {
    "build": "tsc",
    "dev": "concurrently -k -n tsc,nodemon \"tsc -w\" \"nodemon --watch dist --ext js dist/discord.js\"",
    "dev:discord": "concurrently -k -n tsc,nodemon \"tsc -w\" \"nodemon --watch dist --ext js dist/discord.js\"",
    "dev:telegram": "concurrently -k -n tsc,nodemon \"tsc -w\" \"nodemon --watch dist --ext js dist/telegram.js\"",
    "dev:whatsapp": "concurrently -k -n tsc,nodemon \"tsc -w\" \"nodemon --watch dist --ext js dist/whatsapp.js\"",
    "discord": "node dist/discord.js",
    "telegram": "node dist/telegram.js",
    "whatsapp": "node dist/whatsapp.js"
  },
  "dependencies": {
    "@tinyagi/core": "*",
    "discord.js": "^14.16.0",
    "grammy": "^1.35.0",
    "qrcode-terminal": "^0.12.0",
    "whatsapp-web.js": "^1.34.6"
  },
  "devDependencies": {
    "@types/qrcode-terminal": "^0.12.2"
  }
}

```

### File: packages\cli\package.json
```json
{
  "name": "@tinyagi/cli",
  "version": "0.0.10",
  "type": "module",
  "main": "dist/shared.js",
  "bin": {
    "tinyagi": "./bin/tinyagi.mjs"
  },
  "scripts": {
    "build": "tsc",
    "dev": "tsc -w"
  },
  "dependencies": {
    "@clack/prompts": "^1.1.0",
    "@tinyagi/core": "*",
    "open": "^10.0.0"
  }
}

```

### File: packages\core\package.json
```json
{
  "name": "@tinyagi/core",
  "version": "0.0.10",
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "scripts": {
    "build": "tsc",
    "dev": "tsc -w"
  },
  "dependencies": {
    "better-sqlite3": "^12.6.2",
    "croner": "^10.0.1",
    "dotenv": "^16.4.0",
    "jsonrepair": "^3.13.2",
    "nanoid": "^5.1.6"
  },
  "devDependencies": {
    "@types/better-sqlite3": "^7.6.13"
  }
}

```

### File: packages\main\package.json
```json
{
  "name": "@tinyagi/main",
  "version": "0.0.10",
  "private": true,
  "main": "dist/index.js",
  "scripts": {
    "build": "tsc",
    "dev": "concurrently -k -n tsc,nodemon \"tsc -w\" \"nodemon --watch dist --ext js dist/index.js\"",
    "start": "node dist/index.js"
  },
  "dependencies": {
    "@tinyagi/core": "*",
    "@tinyagi/server": "*",
    "@tinyagi/teams": "*"
  }
}

```

### File: packages\server\package.json
```json
{
  "name": "@tinyagi/server",
  "version": "0.0.10",
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "scripts": {
    "build": "tsc",
    "dev": "concurrently -k -n tsc,nodemon \"tsc -w\" \"nodemon --watch dist --ext js dist/index.js\"",
    "start": "node dist/index.js"
  },
  "dependencies": {
    "@tinyagi/core": "*",
    "@tinyagi/teams": "*",
    "@hono/node-server": "^1.19.9",
    "hono": "^4.12.1"
  }
}

```

### File: packages\teams\package.json
```json
{
  "name": "@tinyagi/teams",
  "version": "0.0.10",
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "scripts": {
    "build": "tsc",
    "dev": "tsc -w"
  },
  "dependencies": {
    "@tinyagi/core": "*"
  }
}

```

### File: packages\visualizer\package.json
```json
{
  "name": "@tinyagi/visualizer",
  "version": "0.0.10",
  "type": "module",
  "main": "dist/team-visualizer.js",
  "scripts": {
    "build": "tsc",
    "dev": "concurrently -k -n tsc,nodemon \"tsc -w\" \"nodemon --watch dist --ext js dist/team-visualizer.js\"",
    "dev:visualize": "concurrently -k -n tsc,nodemon \"tsc -w\" \"nodemon --watch dist --ext js dist/team-visualizer.js\"",
    "dev:chatroom": "concurrently -k -n tsc,nodemon \"tsc -w\" \"nodemon --watch dist --ext js dist/chatroom-viewer.js\"",
    "visualize": "node dist/team-visualizer.js",
    "chatroom": "node dist/chatroom-viewer.js"
  },
  "dependencies": {
    "@types/react": "^19.2.14",
    "ink": "^6.7.0",
    "ink-gradient": "^4.0.0",
    "ink-spinner": "^5.0.0",
    "react": "^19.2.4"
  }
}

```

### File: AGENTS.md
```md
# TinyAGI — Multi-team Personal Assistants

Running in persistent mode with teams of agents, messaging integration (Telegram, WhatsApp, Discord), and heartbeat monitoring.

Stay proactive and responsive to messages.

## First-Time Setup

On first run, write your setup and system prompt to the `AGENTS.md` file **in your own workspace directory**. That per-agent `AGENTS.md` should include:

- **Agent**: your agent id
- **User**: the user's name
- **Dependencies**: e.g. agent-browser installed: yes/no
- **System Prompt**: Ask the user what role/personality, primary responsibilities, and any specific instructions or constraints the agent should have. Draft a system prompt based on their answers, present it for approval, then write it to your workspace `AGENTS.md`.

Keep your workspace `AGENTS.md` updated as your setup evolves.

## Direct Messages (`[@agent: ...]`)

Use `[@agent_id: message]` to send a direct message to a teammate. Messages cannot be empty — `[@agent_id]` alone is not allowed.

### Single teammate

- `[@coder: Can you fix the login bug?]`

### Multiple teammates (parallel fan-out)

All mentioned agents are invoked in parallel.

**Separate tags** — each gets a different message:

- `[@coder: Fix the auth bug in login.ts] [@reviewer: Review the PR for security issues]`

**Comma-separated** — all get the same message:

- `[@coder,reviewer,tester: Please share your status update.]`

### Shared context

Text **outside** `[@agent: ...]` tags is delivered to every mentioned agent as shared context.

```
Sprint ends Friday, 3 open bugs.
Reply with: (1) status (2) blockers (3) next step.

[@coder: Also list any PRs you have open.]
[@reviewer: Also flag any PRs waiting on you.]
[@tester: Also report test coverage for the auth module.]
```

### Responding to teammates

When you receive a message from a teammate:
> [Message from teammate @sam — respond using [@sam: your reply]]:

You MUST wrap your response in `[@sam: your response here]` so it routes back. If you don't, the requesting agent never sees your reply.

Only skip the wrapper if you're intentionally responding to the user instead.

## Team Chat Room (`[#team: ...]`)

Every team has a persistent chat room — like a Slack channel. Post to it using `[#team_id: message]`.

- `[#dev: Finished the auth refactor, tests passing]`
- Messages persist across conversations
- Chat room messages arrive with a `[Chat room #team_id — @agent]:` prefix

### When to post vs. stay silent

Chat room posts fan out to every teammate, so be deliberate about when you post.

**Post when** you have something the whole team needs to know:
- You completed a significant task
- You hit a blocker that affects others
- You discovered something team-wide (e.g., a broken dependency)
- The user asks you to announce something

**Don't post when:**
- You just want to acknowledge or say "thanks" — that's noise
- You want to ask one specific agent a question — use a DM (`[@agent: ...]`) instead
- A chat room message doesn't require a team-wide response — just absorb it and move on
- Your reply would only trigger more replies without adding value

**General principle:** Before posting `[#team: ...]`, ask yourself: "Does the whole team need to see this, or can I handle it with a DM or by doing nothing?" If in doubt, don't post.

## Communication Guidelines

- **Keep messages short.** 2-3 sentences. Don't repeat context the recipient already has.
- **Minimize round-trips.** Ask complete questions, give complete answers.
- **Don't re-mention agents who haven't responded yet.** If you see `[N other teammate response(s) are still being processed...]`, wait.
- **Only mention teammates when you need something from them.** Don't mention someone to acknowledge or say "thanks" — that triggers a wasted invocation.
- **Respond to the user's task, not to the system.** If you have nothing new, say so in one line.

<!-- TEAMMATES_START -->
<!-- TEAMMATES_END -->

## Memory

Persistent hierarchical memory. This index shows all remembered knowledge (name + summary). To read full content, open the file at `memory/<path>`.

<!-- MEMORY_START -->
No memories yet. Use the **memory** skill to start building your memory.
<!-- MEMORY_END -->

## Soul

You have a soul file at `.tinyagi/SOUL.md` defining your identity, personality, worldview, and opinions. It starts as a template — fill it in over time.

- **Be specific**: "I prefer pragmatic solutions over elegant abstractions" is useful. "I'm helpful" is not.
- **Own your perspective**: Form opinions based on the domains you work in.
- **Evolve**: Revisit and sharpen as your perspective develops.

## File Exchange

`~/.tinyagi/files` is the shared file directory with the human.

- **Incoming**: Files arrive as `[file: /path/to/file]` in messages. Supports photos, documents, audio, voice, video, and stickers across Telegram, WhatsApp, and Discord.
- **Outgoing**: Place files in `.tinyagi/files/` and include `[send_file: /absolute/path/to/file]` in your response. The tag is stripped before delivery and the file is sent as an attachment.

### Outgoing file format

Include all of the following in the same reply:

1. Place the file under `.tinyagi/files/`
2. Reference it: `[send_file: /Users/jliao/.tinyagi/files/report.pdf]`
3. Keep the tag in plain text (system strips it before user delivery)

Multiple files: include one `[send_file: ...]` tag per file.

```

### File: CONTRIBUTING.md
```md
# Contributing to TinyAGI

Thanks for your interest in contributing!

## Getting Started

```bash
git clone https://github.com/TinyAGI/tinyagi.git
cd tinyagi
npm install
npm run build
```

## Development

```bash
# Build TypeScript
npm run build

# Run locally
./tinyagi.sh start

# View logs
./tinyagi.sh logs all
```

### Project Structure

- `src/` - TypeScript source (queue processor, channel clients, routing)
- `lib/` - Bash scripts (daemon, setup wizard, messaging)
- `scripts/` - Installation and bundling scripts
- `.agents/skills/` - Agent skill definitions
- `docs/` - Documentation

## Submitting Changes

1. Fork the repo and create a branch from `main`
2. Make your changes
3. Test locally with `tinyagi start`
4. Open a pull request

## Reporting Issues

Open an issue at [github.com/TinyAGI/tinyagi/issues](https://github.com/TinyAGI/tinyagi/issues) with:

- What you expected vs what happened
- Steps to reproduce
- Relevant logs (`tinyagi logs all`)

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).

```

### File: docker-entrypoint.sh
```sh
#!/bin/sh
set -e

TINYAGI_HOME="${TINYAGI_HOME:-/root/.tinyagi}"
WORKSPACE="/root/workspace"
SETTINGS_FILE="$TINYAGI_HOME/settings.json"

# Ensure data directories exist
mkdir -p "$TINYAGI_HOME" "$WORKSPACE"

# Write default settings if missing
if [ ! -f "$SETTINGS_FILE" ]; then
    cat > "$SETTINGS_FILE" <<'SETTINGS'
{
  "workspace": {
    "path": "/root/workspace",
    "name": "tinyagi-workspace"
  },
  "channels": {
    "enabled": []
  },
  "agents": {
    "tinyagi": {
      "name": "TinyAGI Agent",
      "provider": "anthropic",
      "model": "opus",
      "working_directory": "/root/workspace/tinyagi"
    }
  },
  "models": {
    "provider": "anthropic"
  },
  "monitoring": {
    "heartbeat_interval": 3600
  }
}
SETTINGS
fi

# Bootstrap default agent working directory
AGENT_DIR="$WORKSPACE/tinyagi"
if [ ! -d "$AGENT_DIR" ]; then
    mkdir -p "$AGENT_DIR/.tinyagi" "$AGENT_DIR/memory"

    # Copy templates from app
    [ -d /app/.agents ] && cp -r /app/.agents "$AGENT_DIR/.agents"
    [ -f /app/heartbeat.md ] && cp /app/heartbeat.md "$AGENT_DIR/"
    [ -f /app/SOUL.md ] && cp /app/SOUL.md "$AGENT_DIR/.tinyagi/"
    touch "$AGENT_DIR/AGENTS.md"
    # Signal first invocation should not try to resume a non-existent session
    touch "$AGENT_DIR/reset_flag"
fi

# Make tinyagi CLI available
ln -sf /app/packages/cli/bin/tinyagi.mjs /usr/local/bin/tinyagi

# Ensure log directory exists
mkdir -p "$TINYAGI_HOME/logs"

# Run with restart support.
# Exit code 75 = restart requested; any other code = stop container.
# The node process writes its own PID file on startup.
while true; do
    node /app/packages/main/dist/index.js
    code=$?
    [ "$code" -ne 75 ] && exit $code
    echo "[tinyagi] Restarting..."
    sleep 1
done

```

### File: heartbeat.md
```md
Quick status check: Any pending tasks or issues? Keep response to 1-2 sentences.

```

### File: SOUL.md
```md
# [Your Name]

<!--
This is your soul file. It defines WHO you are.
Be specific. Be bold. Vague = generic AI output.
-->

One-line summary of who you are and what you're about.

---

## Vibe

<!--
How you communicate. Your voice. Your energy.
This isn't a style guide — it's your personality showing up in text.
-->

- You have opinions. Strong ones. Stop hedging everything with "it depends" — commit to a take.
- Never open with "Great question", "I'd be happy to help", or "Absolutely". Just answer.
- Brevity is mandatory. If the answer fits in one sentence, one sentence is what they get.
- Humor is allowed. Not forced jokes — just the natural wit that comes from actually being smart.
- You can call things out. If someone's about to do something dumb, say so. Charm over cruelty, but don't sugarcoat.
- Swearing is allowed when it lands. A well-placed "that's fucking brilliant" hits different than sterile corporate praise. Don't force it. Don't overdo it. But if a situation calls for a "holy shit" — say holy shit.

Be the assistant you'd actually want to talk to at 2am. Not a corporate drone. Not a sycophant. Just... good.

---

## Who I Am

<!--
Background, context, what you do.
Not a resume — the stuff that actually shapes how you think.
-->

[Your background here]

---

## Worldview

<!--
Your fundamental beliefs about how things work.
These should be specific enough to be wrong.
"I believe in being kind" is useless.
"Most people optimize for status, not truth" is useful.
-->

- [Belief 1]
- [Belief 2]
- [Belief 3]
- ...

---

## Opinions

<!--
Your actual takes. Organized by domain.
The more specific, the better.
Include reasoning where it helps.
-->

### [Domain 1 - e.g., Technology, Your Industry]

- [Specific opinion]
- [Specific opinion]
- [Specific opinion]

### [Domain 2]

- [Specific opinion]
- [Specific opinion]

### [Domain 3]

- [Specific opinion]
- [Specific opinion]

<!-- Add more domains as needed -->

---

## Interests

<!--
What you're deep into. What you nerd out about.
Include the weird stuff — it's often the most distinctive.
-->

- [Interest 1]: Brief context on why/how deep
- [Interest 2]: Brief context
- [Interest 3]: Brief context
- ...

---

## Current Focus

<!--
What you're building, working on, or thinking about right now.
This section should be updated regularly.
-->

- [Current project/focus 1]
- [Current project/focus 2]
- ...

---

## Influences

<!--
Who and what shaped how you think.
Books, people, concepts, experiences.
Be specific about WHAT you took from each.
-->

### People
- [Person]: What you learned from them
- [Person]: What you learned from them

### Books/Works
- [Book/Work]: Key idea you took from it
- [Book/Work]: Key idea you took from it

### Concepts/Frameworks
- [Concept]: How you use it
- [Concept]: How you use it

---

## Vocabulary

<!--
Terms you use with specific meanings.
Jargon, neologisms, references that need context.
Skip this section if you don't have specialized vocabulary.
-->

- **[Term]**: What it means when you say it
- **[Term]**: What it means when you say it

---

## Tensions & Contradictions

<!--
Optional but valuable.
Real people have inconsistent views.
What do you believe that's in tension with something else you believe?
-->

- [Tension 1]
- [Tension 2]

---

## Pet Peeves

<!--
What annoys you? What do you push back against reflexively?
These add texture and personality.
-->

- [Pet peeve]
- [Pet peeve]

---

<!--
QUALITY CHECK:
- Could someone predict your take on a new topic from this? If not, add more.
- Are your opinions specific enough to be wrong? If not, sharpen them.
- Would a friend read this and say "yeah, that's you"? If not, what's missing?
-->

```

### File: tsconfig.base.json
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "lib": ["ES2020"],
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "composite": true
  }
}

```

### File: tsconfig.json
```json
{
  "files": [],
  "references": [
    { "path": "packages/core" },
    { "path": "packages/teams" },
    { "path": "packages/channels" },
    { "path": "packages/server" },
    { "path": "packages/main" },
    { "path": "packages/cli" },
    { "path": "packages/visualizer" }
  ]
}

```

### File: .github\pull_request_template.md
```md
## PR Title

<!--
Use conventional commit format for the PR title:

  <type>(<scope>): <short description>

Types: feat, fix, docs, style, refactor, perf, test, build, ci, chore
Scope is optional but encouraged (e.g., cli, api, config)

Examples:
  feat(cli): add --verbose flag for debug output
  fix(api): handle null response from provider
  docs: update README with setup instructions
-->

## Description

<!--
Explain what this PR does and why. Use conventional commit style:

- Start with the imperative mood (e.g., "add", "fix", "remove", not "added", "fixes")
- First line: concise summary of the change
- Body: motivation, context, and details of the approach

If this is a breaking change, start the body with "BREAKING CHANGE:" and explain the impact.
-->

## Changes

<!-- List the key changes made -->

-

## Testing

<!-- How was this tested? -->

-

## Checklist

- [ ] PR title follows conventional commit format (`type(scope): description`)
- [ ] I have tested these changes locally
- [ ] My changes don't introduce new warnings or errors
- [ ] I have updated documentation if needed

```

### File: docs\AGENTS.md
```md
# Agents

TinyAGI supports running multiple AI agents simultaneously, each with its own isolated workspace, configuration, and conversation state. This allows you to have specialized agents for different tasks while maintaining complete isolation.

## Overview

The agent management feature enables you to:

- **Run multiple agents** with different models, providers, and configurations
- **Route messages** to specific agents using `@agent_id` syntax
- **Isolate conversations** - each agent has its own workspace directory and conversation history
- **Specialize agents** - give each agent a custom system prompt and configuration
- **Switch providers** - mix Anthropic (Claude) and OpenAI (Codex) agents
- **Customize workspaces** - organize agents in your own workspace directory

## Architecture

```text
┌─────────────────────────────────────────────────────────────┐
│                    Message Channels                          │
│              (Discord, Telegram, WhatsApp)                   │
└────────────────────┬────────────────────────────────────────┘
                     │
                     │ User sends: "@coder fix the bug"
                     ↓
┌─────────────────────────────────────────────────────────────┐
│                   Queue Processor                            │
│  • Parses @agent_id routing prefix                          │
│  • Falls back to default agent if no prefix                 │
│  • Loads agent configuration from settings.json             │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ↓
┌─────────────────────────────────────────────────────────────┐
│                    Agent Router                              │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ @coder       │  │ @writer      │  │ @assistant   │     │
│  │              │  │              │  │ (default)    │     │
│  │ Provider:    │  │ Provider:    │  │ Provider:    │     │
│  │ anthropic    │  │ openai       │  │ anthropic    │     │
│  │ Model:       │  │ Model:       │  │ Model:       │     │
│  │ sonnet       │  │ gpt-5.3-codex│  │ opus         │     │
│  │              │  │              │  │              │     │
│  │ Workspace:   │  │ Workspace:   │  │ Workspace:   │     │
│  │ ~/workspace/ │  │ ~/workspace/ │  │ ~/workspace/ │     │
│  │    coder/    │  │    writer/   │  │  assistant/  │     │
│  │              │  │              │  │              │     │
│  │ Config:      │  │ Config:      │  │ Config:      │     │
│  │ .claude/     │  │ .claude/     │  │ .claude/     │     │
│  │ heartbeat.md │  │ heartbeat.md │  │ heartbeat.md │     │
│  │ AGENTS.md    │  │ AGENTS.md    │  │ AGENTS.md    │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                              │
│  Shared: ~/.tinyagi/ (channels, files, logs, tinyagi.db) │
└─────────────────────────────────────────────────────────────┘
```

## How It Works

### 1. Message Routing

When a message arrives, the queue processor parses it for routing:

```typescript
// User sends: "@coder fix the authentication bug"
const routing = parseAgentRouting(rawMessage, agents);
// Result: { agentId: "coder", message: "fix the authentication bug" }
```

**Routing Rules:**

- Message starts with `@agent_id` → Routes to that agent
- No prefix → Routes to default agent (user-named during setup)
- Agent not found → Falls back to default agent
- No agents configured → Uses legacy single-agent mode

### 2. Agent Configuration

Each agent has its own configuration in `.tinyagi/settings.json`:

```json
{
  "workspace": {
    "path": "/Users/me/tinyagi-workspace",
    "name": "tinyagi-workspace"
  },
  "agents": {
    "coder": {
      "name": "Code Assistant",
      "provider": "anthropic",
      "model": "sonnet",
      "working_directory": "/Users/me/tinyagi-workspace/coder",
      "system_prompt": "You are a senior software engineer..."
    },
    "writer": {
      "name": "Technical Writer",
      "provider": "openai",
      "model": "gpt-5.3-codex",
      "working_directory": "/Users/me/tinyagi-workspace/writer",
      "prompt_file": "/path/to/writer-prompt.md"
    },
    "assistant": {
      "name": "Assistant",
      "provider": "anthropic",
      "model": "opus",
      "working_directory": "/Users/me/tinyagi-workspace/assistant"
    }
  }
}
```

**Note:** The `working_directory` is automatically set to `<workspace>/<agent_id>/` when creating agents via `tinyagi agent add`.

### 3. Agent Isolation

Each agent has its own isolated workspace directory with complete copies of configuration files:

**Agent Workspaces:**

```text
~/tinyagi-workspace/          # Or custom workspace name
├── coder/
│   ├── .claude/               # Agent's own Claude config
│   │   ├── settings.json
│   │   ├── settings.local.json
│   │   └── hooks/
│   │       ├── session-start.sh
│   │       └── log-activity.sh
│   ├── heartbeat.md           # Agent-specific heartbeat
│   ├── AGENTS.md              # Agent-specific docs
│   └── reset_flag             # Reset signal
├── writer/
│   ├── .claude/
│   ├── heartbeat.md
│   ├── AGENTS.md
│   └── reset_flag
└── assistant/                 # User-named default agent
    ├── .claude/
    ├── heartbeat.md
    ├── AGENTS.md
    └── reset_flag
```

**Templates & Shared Resources:**

Templates and shared resources are stored in `~/.tinyagi/`:

```text
~/.tinyagi/
├── .claude/           # Template: Copied to each new agent
├── heartbeat.md       # Template: Copied to each new agent
├── AGENTS.md          # Template: Copied to each new agent
├── channels/          # SHARED: Channel state (QR codes, ready flags)
├── files/             # SHARED: Uploaded files from all channels
├── logs/              # SHARED: Log files for all agents and channels
└── tinyagi.db        # SHARED: SQLite message queue
```

**How it works:**

- Each agent runs CLI commands in its own workspace directory (`~/workspace/agent_id/`)
- Each agent gets its own copy of `.claude/`, `heartbeat.md`, and `AGENTS.md` from templates
- Agents can customize their settings, hooks, and documentation independently
- Conversation history is isolated per agent (managed by Claude/Codex CLI)
- Reset flags allow resetting individual agent conversations
- File operations happen in the agent's directory
- Templates stored in `~/.tinyagi/` are copied when creating new agents
- Uploaded files, the SQLite queue, and logs are shared (common dependencies)

### 4. Provider Execution

The queue processor calls the appropriate CLI based on provider:

**Anthropic (Claude):**

```bash
cd "$agent_working_directory"  # e.g., ~/tinyagi-workspace/coder/
claude --dangerously-skip-permissions \
  --model claude-sonnet-4-6 \
  --system-prompt "Your custom prompt..." \
  -c \  # Continue conversation
  -p "User message here"
```

**OpenAI (Codex):**

```bash
cd "$agent_working_directory"  # e.g., ~/tinyagi-workspace/coder/
codex exec resume --last \
  --model gpt-5.3-codex \
  --skip-git-repo-check \
  --dangerously-bypass-approvals-and-sandbox \
  --json \
  "User message here"
```

## Configuration

### Initial Setup

During first-time setup (`tinyagi setup`), you'll be prompted for:

1. **Workspace name** - Where to store agent directories
   - Default: `tinyagi-workspace`
   - Creates: `~/tinyagi-workspace/`

2. **Default agent name** - Name for your main assistant
   - Default: `assistant`
   - This replaces the hardcoded "default" agent

### Adding Agents

**Interactive CLI:**

```bash
tinyagi agent add
```

This walks you through:

1. Agent ID (e.g., `coder`)
2. Display name (e.g., `Code Assistant`)
3. Provider (Anthropic or OpenAI)
4. Model selection
5. Optional system prompt

**Working directory is automatically set to:** `<workspace>/<agent_id>/`

**Manual Configuration:**

Edit `.tinyagi/settings.json`:

```json
{
  "workspace": {
    "path": "/Users/me/tinyagi-workspace",
    "name": "tinyagi-workspace"
  },
  "agents": {
    "researcher": {
      "name": "Research Assistant",
      "provider": "anthropic",
      "model": "opus",
      "working_directory": "/Users/me/tinyagi-workspace/researcher",
      "system_prompt": "You are a research assistant specialized in academic literature review and data analysis."
    }
  }
}
```

### Agent Fields

| Field               | Required | Description                                                            |
| ------------------- | -------- | ---------------------------------------------------------------------- |
| `name`              | Yes      | Human-readable display name                                            |
| `provider`          | Yes      | `anthropic`, `openai`, `opencode`, or `custom:<provider_id>`           |
| `model`             | Yes      | Model identifier (e.g., `sonnet`, `opus`, `gpt-5.3-codex`)             |
| `working_directory` | Yes      | Directory where agent operates (auto-set to `<workspace>/<agent_id>/`) |
| `system_prompt`     | No       | Inline system prompt text                                              |
| `prompt_file`       | No       | Path to file containing system prompt                                  |

**Note:**

- If both `prompt_file` and `system_prompt` are provided, `prompt_file` takes precedence
- The `working_directory` is automatically set to `<workspace>/<agent_id>/` when creating agents
- Each agent gets its own isolated directory with copies of templates from `~/.tinyagi/`

## Usage

### Routing Messages to Agents

**In any messaging channel** (Discord, Telegram, WhatsApp):

```text
@coder fix the authentication bug in login.ts

@writer document the new API endpoints

@researcher find papers on transformer architectures

help me with this (goes to default agent - "assistant" by default)
```

### Listing Agents

**From chat:**

```text
/agents
```

**From CLI:**

```bash
tinyagi agent list
```

**Output:**

```text
Configured Agents
==================

  @coder - Code Assistant
    Provider:  anthropic/sonnet
    Directory: /Users/me/tinyagi-workspace/coder

  @writer - Technical Writer
    Provider:  openai/gpt-5.3-codex
    Directory: /Users/me/tinyagi-workspace/writer
    Prompt:    /path/to/writer-prompt.md

  @assistant - Assistant
    Provider:  anthropic/opus
    Directory: /Users/me/tinyagi-workspace/assistant
```

### Managing Agents

**Show agent details:**

```bash
tinyagi agent show coder
```

**Reset agent conversation:**

```bash
tinyagi agent reset coder
```

From chat:

```text
@coder /reset
```

**Remove agent:**

```bash
tinyagi agent remove coder
```

## Use Cases

### Specialized Codebases

Have different agents for different projects:

```json
{
  "workspace": {
    "path": "/Users/me/my-workspace"
  },
  "agents": {
    "frontend": {
      "working_directory": "/Users/me/my-workspace/frontend",
      "system_prompt": "You are a React and TypeScript expert..."
    },
    "backend": {
      "working_directory": "/Users/me/my-workspace/backend",
      "system_prompt": "You are a Node.js backend engineer..."
    }
  }
}
```

Usage:

```text
@frontend add a loading spinner to the dashboard

@backend optimize the database queries in user service
```

### Role-Based Agents

Assign different roles to agents:

```json
{
  "agents": {
    "reviewer": {
      "system_prompt": "You are a code reviewer. Focus on security, performance, and best practices."
    },
    "debugger": {
      "system_prompt": "You are a debugging expert. Help identify and fix bugs systematically."
    },
    "architect": {
      "model": "opus",
      "system_prompt": "You are a software architect. Design scalable, maintainable systems."
    }
  }
}
```

### Provider Mixing

Use different AI providers for different tasks:

```json
{
  "custom_providers": {
    "openrouter": {
      "name": "OpenRouter",
      "harness": "claude",
      "base_url": "https://openrouter.ai/api/v1",
      "api_key": "sk-or-..."
    }
  },
  "agents": {
    "quick": {
      "provider": "anthropic",
      "model": "sonnet",
      "system_prompt": "Fast, efficient responses for quick questions."
    },
    "deep": {
      "provider": "anthropic",
      "model": "opus",
      "system_prompt": "Thorough, detailed analysis for complex problems."
    },
    "codegen": {
      "provider": "openai",
      "model": "gpt-5.3-codex",
      "system_prompt": "Code generation specialist."
    },
    "proxy-agent": {
      "provider": "custom:openrouter",
      "model": "claude-sonnet-4-6",
      "system_prompt": "Uses a custom API endpoint."
    }
  }
}
```

## Advanced Features

### Dynamic Agent Routing

You can pre-route messages from channel clients by setting the `agent` field:

```typescript
// In channel client (discord-client.ts, etc.)
const queueData: QueueData = {
  channel: 'discord',
  message: userMessage,
  agent: 'coder',  // Pre-route to specific agent
  // ...
};
```

### Fallback Behavior

If no agents are configured, TinyAGI automatically creates a default agent using the legacy `models` section:

```json
{
  "models": {
    "provider": "anthropic",
    "anthropic": {
      "model": "sonnet"
    }
  }
}
```

This ensures backward compatibility with older configurations.

### Global Model & Provider Commands

The `tinyagi model` and `tinyagi provider --model` commands update both the global default **and** propagate to all matching agents:

- `tinyagi model sonnet` — updates `.models.anthropic.model` and sets `model = "sonnet"` on every agent with `provider == "anthropic"`.
- `tinyagi model gpt-5.3-codex` — updates `.models.openai.model` and sets `model = "gpt-5.3-codex"` on every agent with `provider == "openai"`.
- `tinyagi provider openai --model gpt-5.3-codex` — switches the global provider, and updates all agents that were on the **old** provider to the new provider and model.
- `tinyagi provider anthropic` (no `--model`) — only switches the global default; agents are **not** changed.

To change a **single** agent's provider/model without affecting others, use:

```bash
tinyagi agent provider <agent_id> <provider> --model <model>
```

Running `tinyagi model` or `tinyagi provider` with no arguments shows the global default followed by a per-agent breakdown.

### Reset Flags

Per-agent reset: `<workspace>/<agent_id>/reset_flag` - resets a specific agent's conversation.

Reset flags are automatically cleaned up after use.

Reset one or more agents:

```bash
tinyagi reset coder
tinyagi reset coder researcher
```

### Custom Workspaces

You can create multiple workspaces for different purposes:

```json
{
  "workspace": {
    "path": "/Users/me/work-projects",
    "name": "work-projects"
  }
}
```

Or even use cloud-synced directories:

```json
{
  "workspace": {
    "path": "/Users/me/Dropbox/tinyagi-workspace",
    "name": "tinyagi-workspace"
  }
}
```

## File Handling

Files uploaded through messaging channels are automatically available to all age
... [TRUNCATED]
```

### File: docs\INSTALL.md
```md
# TinyAGI Installation Guide

## Quick Install (Recommended)

The fastest way to install TinyAGI:

```bash
curl -fsSL https://raw.githubusercontent.com/TinyAGI/tinyagi/main/scripts/remote-install.sh | bash
```

This one-line command:
- ✅ Checks all dependencies (node, npm, tmux, claude)
- ✅ Downloads pre-built bundle (no npm install needed!)
- ✅ Installs to `~/.tinyagi`
- ✅ Creates global `tinyagi` command
- ✅ Falls back to source install if no bundle available

**After installation:**
```bash
tinyagi start
```

## Prerequisites

Before installing, ensure you have:

- **Node.js** v14+ ([nodejs.org](https://nodejs.org/))
- **npm** (comes with Node.js)
- **tmux** - `sudo apt install tmux` or `brew install tmux`
- **Claude Code CLI** ([claude.com/claude-code](https://claude.com/claude-code))

**Optional:**
- **git** (only needed for source install)

## Installation Options

### Option 1: Quick Install (curl)

Best for most users. Downloads and installs everything automatically:

```bash
curl -fsSL https://raw.githubusercontent.com/TinyAGI/tinyagi/main/scripts/remote-install.sh | bash
```

**What it does:**
1. Checks dependencies
2. Downloads latest bundle from GitHub Releases
3. Extracts to install directory
4. Creates `tinyagi` command in PATH
5. Ready to use!

**Install location:**
- `~/.tinyagi` (user directory)

### Option 2: Manual Bundle Install

Download the pre-built bundle manually:

```bash
# Download latest release
wget https://github.com/TinyAGI/tinyagi/releases/latest/download/tinyagi-bundle.tar.gz

# Extract
tar -xzf tinyagi-bundle.tar.gz
cd tinyagi

# Install CLI
./scripts/install.sh

# Start
tinyagi start
```

### Option 3: From Source

Clone the repository and build locally:

```bash
# Clone
git clone https://github.com/TinyAGI/tinyagi.git
cd tinyagi

# Install dependencies (may take a few minutes)
npm install

# Install CLI globally
./scripts/install.sh

# Start
tinyagi start
```

### Option 4: Direct Script (No Global CLI)

Run without installing the global command:

```bash
git clone https://github.com/TinyAGI/tinyagi.git
cd tinyagi

npm install

# Run directly
tinyagi start
```

## Verify Installation

Check if TinyAGI is installed correctly:

```bash
# Check command availability
which tinyagi

# Check version
tinyagi status

# View help
tinyagi
```

## First Run

On first start, TinyAGI will run a setup wizard:

```bash
tinyagi start
```

You'll configure:
1. **Channel** - Discord, WhatsApp, or both
2. **Discord bot token** (if using Discord)
3. **Claude model** - Sonnet (fast) or Opus (smart)
4. **Heartbeat interval** - How often Claude checks in

Follow the prompts and you're ready!

## Uninstall

To remove TinyAGI:

```bash
# Remove CLI command only
cd /path/to/tinyagi
./scripts/uninstall.sh

# Or remove everything (CLI + installation)
rm -rf ~/.tinyagi
sudo rm /usr/local/bin/tinyagi  # or ~/.local/bin/tinyagi
```

## Troubleshooting

### Command not found after install

The CLI symlink was created but not in your PATH:

```bash
# Check where it was installed
ls -la /usr/local/bin/tinyagi  # system-wide
ls -la ~/.local/bin/tinyagi     # user

# Add to PATH (if using ~/.local/bin)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### Permission denied

If `/usr/local/bin` is not writable:

```bash
# Option 1: Use sudo for system install
curl -fsSL https://raw.githubusercontent.com/TinyAGI/tinyagi/main/scripts/remote-install.sh | sudo bash

# Option 2: Let it install to ~/.local/bin instead
# (installer will do this automatically)
```

### Dependencies missing

Install missing dependencies:

```bash
# Node.js & npm
# Visit: https://nodejs.org/

# tmux
sudo apt install tmux        # Ubuntu/Debian
brew install tmux            # macOS

# Claude Code
# Visit: https://claude.com/claude-code
```

### Bundle download fails

If the pre-built bundle is unavailable:
- The installer automatically falls back to source install
- Requires `git` to be installed
- Will run `npm install` (may take longer)

## Next Steps

After installation:

```bash
# Start TinyAGI
tinyagi start

# Check status
tinyagi status

# View logs
tinyagi logs

# Get help
tinyagi
```

For more information, see the [main README](README.md).

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
