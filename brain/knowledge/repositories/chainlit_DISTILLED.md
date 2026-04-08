---
id: repo-fetched-chainlit-042430
type: knowledge
owner: OA
registered_at: 2026-04-05T04:06:33.443114
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_chainlit_042430

## Assimilation Report
Auto-cloned repository: FETCHED_chainlit_042430

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
backend/README.md
```

### File: docs\README.md
```md
# Documentation for Chainlit developers, contributors, and AI coding assistants.

See also:
- [CONTRIBUTING.md](../CONTRIBUTING.md) — contribution guidelines
- [CHANGELOG.md](../CHANGELOG.md) — release history

```

### File: AGENTS.md
```md
# AGENTS.md

This file provides guidance to AI agents when working with code in this repository.

## Backward Compatibility (CRITICAL)

All changes MUST be backward-compatible. If a refactor or breaking change is unavoidable, notify the user and stop — do not proceed without explicit approval. When approved, prefer adding a compatibility layer over keeping legacy code in place.

## Overview

Chainlit is a Python framework for building production-ready conversational AI applications. It consists of a Python/FastAPI backend and a React frontend, with a pnpm monorepo for the JS packages.

## Prerequisites

- Python: **3.13** (3.10+ is the framework's minimum, but development targets 3.13)
- Node.js: **24+**
- [uv](https://docs.astral.sh/uv/) — Python package manager
- [pnpm 9](https://pnpm.io/) — Node.js package manager (Corepack)

## Quick Start

### Install

| | Command | Directory |
|---|---|---|
| Backend  | `uv sync --all-extras` | `backend/` |
| Frontend | `pnpm install` | repo root |

### Build

| | Command | Directory | What it does |
|---|---|---|---|
| Backend | `uv build` | `backend/` | Build Python package — runs `pnpm buildUi`, then copies assets into `backend/chainlit/frontend/dist/` and `backend/chainlit/copilot/dist/` |
| Frontend | `pnpm run buildUi` | repo root | Build libs + frontend JS assets |
| Frontend (libs only) | `pnpm run build:libs` | repo root | Build only `react-client` and `copilot` libs |

### Dev servers

| | Command | Directory | URL |
|---|---|---|---|
| Backend | `uv run chainlit run chainlit/sample/hello.py -h` | `backend/` | http://localhost:8000 |
| Frontend | `pnpm run dev` | `frontend/` | http://localhost:5173 (proxies to :8000) |

### Tests

| | Command | Directory |
|---|---|---|
| Backend (all) | `uv run pytest --cov=chainlit/` | `backend/` |
| Backend (single file) | `uv run pytest tests/test_file.py` | `backend/` |
| Frontend unit | `pnpm test` | `frontend/` |
| E2E (Cypress) | `pnpm test` | repo root |

### Lint & Format

| | Command | Directory |
|---|---|---|
| Lint all | `pnpm run lint` | repo root |
| Lint frontend only | `pnpm run lintUi` | repo root |
| Format Python | `uv run ruff format chainlit/ tests/` | `backend/` |
| Format JS/TS | `pnpm run formatUi` | repo root |

### Type checking

| | Command | Directory |
|---|---|---|
| Python (mypy) | `uv run dmypy run -- chainlit/ tests/` | `backend/` |
| TypeScript | `tsc --noemit` | `frontend/` |

Run `pnpm run lint` before committing — CI enforces this.

### Commits

This project uses [Conventional Commits](https://www.conventionalcommits.org/). Format: `<type>(<optional scope>): <description>`.

Common types: `feat`, `fix`, `chore`, `docs`, `refactor`, `test`, `ci`. Scope is optional but encouraged (e.g. `fix(data): ...`, `feat(i18n): ...`).

All commits made with AI assistance **must** include a `Co-Authored-By` trailer identifying the AI agent. Add it as the last line of the commit message body:

```
Co-Authored-By: <Agent Name> <agent-email-or-noreply>
```

Examples:
- `Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>`
- `Co-Authored-By: GitHub Copilot <noreply@github.com>`
- `Co-Authored-By: Gemini CLI <noreply@google.com>`

## Tech Stack

| Layer | Stack |
|---|---|
| **Frontend** | React 18, TypeScript 5.2, Vite 5, Tailwind CSS 3, Vitest, Zod 3 |
| **Frontend (state & routing)** | Recoil, React Router 6, react-hook-form, socket.io-client, SWR |
| **Frontend (rendering)** | react-markdown + remark-gfm/math + rehype-katex/raw, highlight.js, lucide-react (icons), Radix UI (primitives), Plotly.js |
| **Backend** | Python 3.13, FastAPI, Starlette, Uvicorn, python-socketio, Pydantic 2, PyJWT, httpx |
| **LLM integrations** | MCP, LangChain, LlamaIndex, OpenAI SDK, Semantic Kernel, MistralAI |
| **Infra / persistence** | SQLAlchemy (PostgreSQL/SQLite), DynamoDB + S3 (boto3), Azure Blob / Data Lake, Google Cloud Storage, LiteralAI |
| **DX** | Husky (pre-commit), ESLint, Prettier, ruff, mypy (dmypy), pytest, Cypress |

## Architecture

### Monorepo structure

```
backend/          # Python package (published to PyPI as "chainlit")
frontend/         # React app (built output served by backend)
libs/
  react-client/   # @chainlit/react-client — published npm package with React hooks
  copilot/        # Copilot widget (embedded chat bubble)
cypress/          # E2E tests
```

The pnpm workspace includes `frontend/`, `libs/react-client/`, and `libs/copilot/`. The built frontend assets are copied into `backend/chainlit/frontend/dist/` and served as static files.

### Backend (`backend/chainlit/`)

**Entry point for user apps**: `__init__.py` re-exports all public API decorators and classes.

**Key files:**
- `server.py` — FastAPI app, all REST routes (auth, elements, threads, file upload), serves the built frontend SPA, mounts the SocketIO app
- `socket.py` — SocketIO event handlers for real-time WebSocket communication (connect, message, audio, etc.)
- `callbacks.py` — Decorator functions registered via `@cl.on_message`, `@cl.on_chat_start`, `@cl.on_audio_chunk`, etc. These store functions on `config.code.*`
- `config.py` — Reads `.chainlit/config.toml` from `APP_ROOT`. `ChainlitConfig` holds both static TOML config and runtime user-registered callbacks. `APP_ROOT` defaults to `os.getcwd()`.
- `session.py` — `WebsocketSession` (per-connection state: user, files, MCP connections, message queue) and `HTTPSession`
- `context.py` — `ChainlitContext` per-coroutine context variable (similar to thread-local), providing access to the current session and emitter
- `emitter.py` — Sends events back to the frontend through the SocketIO session
- `data/base.py` — `BaseDataLayer` ABC for persistence (threads, steps, elements, users, feedback). Implementations: `sql_alchemy.py`, `dynamodb.py`, `literalai.py`
- `auth/` — JWT creation/validation (`jwt.py`), OAuth state cookies (`cookie.py`)
- `types.py` — Shared Pydantic models for API request/response types

**Data layer pattern**: The data layer is optional (no persistence by default). Register a custom implementation with `@cl.data_layer` decorator or use the built-in SQLAlchemy/DynamoDB/LiteralAI implementations. The `@queue_until_user_message()` decorator on `BaseDataLayer` methods queues write operations until the first user message arrives.

**Integrations**: `langchain/`, `llama_index/`, `openai/`, `semantic_kernel/`, `mistralai/` — each provides callback handlers that bridge those frameworks into Chainlit steps/messages.

### Frontend (`frontend/src/`)

React 18 + TypeScript + Vite, styled with Tailwind CSS and Radix UI primitives.

- `main.tsx` — React root, wraps app in `RecoilRoot` and `ChainlitContext.Provider`
- `App.tsx` — Handles auth readiness, chat profile selection, and WebSocket connection lifecycle
- `router.tsx` — Client-side routes: `/` (Home), `/thread/:id`, `/element/:id`, `/login`, `/login/callback`, `/share/:id`, `/env`
- `state/` — Recoil atoms: `chat.ts` (messages, elements, tasks), `project.ts` (config, session), `user.ts` (env vars)
- `components/chat/` — Core chat UI (message list, input bar, elements, audio)
- `components/header/` — Top navigation bar
- `components/LeftSidebar/` — Thread history sidebar

### `@chainlit/react-client` (`libs/react-client/src/`)

Publishable npm package — the bridge between the React UI and the backend WebSocket.

- `api.ts` — `ChainlitAPI` class: HTTP calls to backend REST endpoints
- `useChatSession.ts` — Manages socket.io connection lifecycle
- `useChatMessages.ts` — Exposes message tree state
- `useChatData.ts` — Exposes elements, actions, tasklists, connection status
- `useChatInteract.ts` — `sendMessage`, `replyMessage`, `callAction`, `stopTask`, `clear`
- `state.ts` — Recoil atoms shared between the lib and consuming apps

State is managed via Recoil; consuming apps must wrap the tree in `<RecoilRoot>` and provide a `ChainlitAPI` instance via `ChainlitContext.Provider`.

### Communication flow

1. User sends a message → `useChatInteract.sendMessage` → emits `client_message` over SocketIO
2. Backend `socket.py` handler receives it → calls `config.code.on_message(message)`
3. User's app calls `cl.Message(...).send()` → `emitter.py` emits `new_message` back over SocketIO
4. Frontend `useChatMessages` updates Recoil state → component re-renders

### App configuration

Apps configure Chainlit via `.chainlit/config.toml` (created automatically on first run). Key sections: `[project]` (auth, session timeouts, CORS), `[UI]` (name, theme, layout).

---

## Documentation Verification Requirements

Before writing/modifying code, verify against official docs.

**Lookup order**: Context7 MCP (preferred) → WebFetch → WebSearch.

Pre-resolved Context7 library IDs: [docs/context7.md](docs/context7.md)

Cross-reference API signatures and patterns during implementation. When uncertain, always check docs rather than relying on training data.
```

### File: CHANGELOG.md
```md
# Changelog

All notable changes to Chainlit will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [2.10.1] - 2026-03-27

### Fixed

- Security vulnerability in Chainlit: validate WebSocket session restore against the authenticated user

### Changed

- Move npm library publishing to OIDC Trusted Publishing

## [2.10.0] - 2026-03-05

### Added
- Add starter categories for grouped starters
- Always show the favorite messages button with an empty state
- Add option to disable rendering markdown in user messages
- Allow easy deletion of favorites
- Make state cookie lifetime configurable via env var
- Add Arabic translation
- Add Danish translation
- Add settings change listener
- Add image preview
- Add selected option for command pre-selection
- Add `auto_collapse` parameter to `Step`
- Add `/health` endpoint for container orchestration
- Add `hidden` option for `default_sidebar_state`
- Make avatar size configurable via `config.toml`

### Fixed
- Reorder chat history sidebar after messages in existing chats
- Use login error detail for credential failures
- Convert UUID fields to strings in feedback extraction
- Preserve thread metadata when updated without metadata
- Reset audio UI when microphone permission is denied
- Fix sidebar inset overflow causing horizontal scroll
- Prevent empty strings from overwriting step content on upsert
- Use correct URL scheme when SSL is configured

## [2.9.6] - 2026-01-20

### Added
- Allow skip new chat creation
- Add data picker input widget
- Toggle chat settings in sidebar instead of composer

### Fixed
- Fix: Starters now correctly use the selected/default mode if configured

## [2.9.5] - 2026-01-08

### Added
- Add favorite messages (prompt templates)

### Fixed
- Fix: Starters now correctly use the selected/default mode if configured

## [2.9.4] - 2025-12-24

### Added
- Add an icon for shared thread
- New option to allow disabling auto scroll of assistant messages
- Add modes: you may allow users to select an LLM model, a mode (for example, planning), allow to enable reasoning etc.
  - Breaking change: you need to run `ALTER TABLE steps ADD COLUMN IF NOT EXISTS modes JSONB;` for migration

### Fixed
- Fix tiny avatar for long messages
- Security vulnerability in Chainlit: added missed sanitization to custom elements update endpoint

### Changed
- Bumped watchfiles version

## [2.9.3] - 2025-12-04

### Added
- Add tests for oauth providers and messages
- Merge metadata in chainlit data layer
- Add native video support in markdown rendering
- Optimize chat message rendering
- Add language configuration option to config.toml
- Upgrade langchain imports for v1 compatibility
- Improve icon name formatting issues

### Fixed
- Fixed page blinking issue with header_auth
- Set environ when restoring websocket session
- Move hello.py to avoid import issues
- Fix issue showing thread sharing when disabled
- Disable Chainlit from setting logging globally

## [2.9.2] - 2025-11-22

### Added
- Add tests for socket, chat context, cache, translations & oauth providers

### Fixed
- Fix copilot breaking change introduced in 2.8.5

## [2.9.1] - 2025-11-20

### Added
- Add support for tabs in chat settings
- Support markdown in watermark
- Add italian translation to translations folder
- Add query param prefill for chat
- Add tests for utils, markdown, sidebar, chat settings, mcp, input widget, langchain, elements, steps, and actions


## [2.9.0] - 2025-11-06

### Added
- Add better support for Multi-Agent implementations
  - Nested steps are now step.input -> child step -> step.output
  - Improved formatting and styling of Tasklist


## [2.8.5] - 2025-11-07

### Added
- Add display_name to ChatProfile
- Add slack reaction event callback
- Add raw response from OAuth providers

### Fixed
- Security vulnerability in Chainlint: added missed ACL check for session initialization

### Changed
- Remove FastAPI version restrictions

## [2.8.4] - 2025-10-29

### Added
- Add support for GitHub Enterprise OAuth provider
- Explicit disable on input widgets


### Fixed
- Tasklist tasks are now properly reconnected to their steps/messages
- ci: fix pnpm publish checks
- fix: missing / in url with base path when connecting Streamable HTTP MCP
- fix - persist custom_elements to data layer without cloud storage
- fix: propagate IME composition events in AutoResizeTextarea
- fix: confirm when enter
- Fix(translation): correct French translation of chat watermark 
- fix(ui): add fallback logo if custom logo is missing

## [2.8.3] - 2025-10-06

### Added
- Support for the `target` attribute in header links, which can be configured through the configuration options

### Changed
- `@chainlit/react-client` automatic publishing

## [2.8.2] - 2025-10-01

### Changed
- Remove autofocus in mobile message composer
- Improve error handling in sqlalchemy data layer `get_read_url()`

### Fixed
- Fix voice hotkey (P) triggering when typing in chat input
- Properly finalize data layers
- Fix `on_chat_start` not always firing

## [2.8.1] - 2025-09-24

### Added
- Add German and Korean translations
- Add support for custom_meta_url in config.toml

### Changed
- `cl.on_thread_share_view` will allow shared thread viewing if it returns `True` to enable custom/admin viewing.

### Fixed
- Removed redundant message sending in Slack when images are present.
- Generate signed url when loading elements using SQLAlchemy data layer.

## [2.8.0] - 2025-09-12

### Added
- Add ability to share threads. See documentation for how to enable it.
  - https://docs.chainlit.io/api-reference/lifecycle-hooks/on-shared-thread-view
- Add new chat settings: multi-select, radio-group, and checkbox
- Add optional language parameter to set_starters
- Add neutral Spanish translation
- Allow sending commands from custom elements

### Changed
- Reordered message composer elements

### Fixed
- Default to plaintext code blocks for unsupported languages like CSV
- Sort threads by updated_at field
- Replace hardcoded strings with translation keys
- GCP storage provider dependency is now optional
- CI/CD fixes
- Fixed issues with hot-reloading in dev mode (`-w` flag)
- Take overridden config into account in audio handlers

## [2.7.2] - 2025-08-26

### Added
- Added LiteralAI data layer deprecation warning
- Added context to `@cl.on_feedback` callback
- Added Traditional Chinese (Taiwan) translations
- Added configurable user_env persistence to database
  - New `persist_user_env` and `mask_user_env` field in `config.toml`
- Added new command translations to all languages
- Added CODEOWNERS

### Fixed
- Improved dynamic config overrides for chat profiles
- Import GCSStorageClient only when needed to avoid requiring optional dependencies
- Updated CONTRIBUTING.md for `uv` usage

## [2.7.1.1] - 2025-08-21

- Fix publishing to include frontend and copilot folders

## [2.7.1] - 2025-08-20

- Fix publishing to work with uv

## [2.7.0] - 2025-08-20

### Added
- New ChatGPT-style command selection and improve message input handling
- Added the ability to override certain config.toml settings for Chat Profiles, so some profiles can have MCP and some can't for example. [Documentation Updated](https://docs.chainlit.io/api-reference/chat-profiles#dynamic-configuration).
  - You must now explicity enable audio and MCP as these are no longer inferred by the presence of `on_audio_start` or `on_mcp_connect` callbacks
  - Delete your `config.toml`, run `chainlit init`, and update your settings
- Added copilot setup instructions for GitHub Copilot SWE Agent
- Added Slack socket mode support
- AskFileButton can now upload file with proper checking and it's own limits
- Added content-disposition metadata to azure blob uploads to persist download file name
- Migrated from poetry to uv

### Fixed
- Changed thread sorting to use updated time instead of creation time
- Add missing headers when connecting Streamable HTTP MCP
- Remove undocumented `CHAINLIT_CUSTOM_AUTH` environment variable used in Copilot

## [2.6.9] - 2025-08-14

### Added
- Add GitHub Copilot instructions for automated PRs
- (Slack) Add threadId for user feedback
- (Copilot) Add new optional opened property has been added to the widget config

### Fixed
- Fix blinking cursor indicator
- (Copilot) Rename copilot inner div id `chainlit-copilot` to `chainlit-copilot-chat` due to naming conflict with the outer div
- Disable gzip for websocket-relaed http endpoint (Safari compatibility)
- Prevent constant refresh on the login screen when using custom authenication
- Fix MCP type hints

## [2.6.8] - 2025-08-08

### Other

- Reverted PR with newline preservation in messages due to incorrect rendering in child components like lists

## [2.6.7] - 2025-08-07

### Fixed
- Formatting when pasting HTML code and newlines in received messages

## [2.6.6] - 2025-08-05

### Added
- Add support for emoji reaction on message received in Slack
- Add Greek translation
- Copy both plain text and rich text to clipboard, if available (rich text pasting to editors like Word)
- Rename `CHAINLIT_COOKIE_PATH` to `CHAINLIT_AUTH_COOKIE_PATH` and now espect CHAINLIT_ROOT_PATH
- Add language parameter to Copilot widget configuration

### Fixed
- Prevent HTML code in user message to be rendered as HTML instead of displaying as code
- Properly parse `user_env` when `config.project.user_env` is empty

## [2.6.5] - 2025-08-02

### Fixed
- Properly escape HTML on paste
- Enable gzip compression for frontend
- Address security vulnerabilities in dependencies by upgrading them to the closest safe versions
- CI e2e tests and pnpm cache issues

## [2.6.4] - 2025-08-01

### Added
- Add streamable HTTP MCP support
- Improve e2e test stability and performance
- Add configuration for expanded copilot mode
- Add French translation

### Fixed
- Fix inputs/outputs for langchain callbacks
- Fix blinking indicator for in-progress steps
- Avoid unnecessary logo fetching when supplied in config.toml

### Other
- Bump dependencies

## [2.6.3] - 2025-07-25

### Added
- Ability to send empty commands
- Wider element view in copilot and improved styling
- Support signed urls for elements using dynamoDB persistence
- Support additional connection arguments in SQLAlchemy data layer
- Added `CHAINLIT_COOKIE_PATH` environment variable to set the cookie path

### Fixed
- Message inputs formatting
- Language pattern to allow `tzm-Latn-DZ`
- Properly encode parentheses in markdown links
- Fix chainlit data layer metadata upserts
- Improve database connection handling
- Fixed cookie path 
- Improve lanchain callbacks

### Other
- Improve robustness of E2E tests
- Removed watermark "Built with Chainlit"

## [2.6.2] - 2025-07-16

Technical release due to missed `frontend` and `copilot` folders in previous one.

## [2.6.1] - 2025-07-15

### Added
- New `on_feedback` callback
- Relaxed restriction on number of starters (now more than 4 can be displayed)

### Fixed
- Command persistence when `"button": True` is missing from command definition
- `openai` and `mistralai` sub-modules fail due to incorrect `timestamp_utc` import
- Temporarily reverted fix caused the following issues with Chainlit data layer:
  - `null value in column "metadata" of relation "Thread"`
  - `syntax error at or near ";"`
- Google Cloud Storage private bucket support in Chainlit data layer
- Portals (popups, dialogs, etc.) now render correctly inside Copilot's shadow DOM

### Other
- Removed telemetry
- Updated versions for Node.js, Poetry, and pnpm; added Corepack support

## [2.6.0] - 2025-07-01

### Added
- Add commands to starters
- Collapse command buttons to icons for small screens
- Add timegated custom elements
- Added ADC support for google cloud storage adapter
- Added scope as env variable (`OAUTH_COGNITO_SCOPE`) to Cognito auth provider
- Add MarkdownAlert Style Switcher. Control via `alert_style` in `config.toml`.
- Allow custom s3 endpoint for the official data layer
- Added container prop to dialog portal in Copilot shadow DOM
- Bump dependencies
- Add python 3.13 support

### Fixed
- Fix chat input double-spacing issue
- Resolve python deprecation warning for utc_now() and logger.warn
- Fixed an issue where the portal for the ChatProfiles selector was being rendered outside the Copilot shadow DOM
- Add mime type to element emitter
- Handle float/Decimal conversion for DynamoDB persistence
- Fix cancel button in Chat settings
- Only update thread metadata when not empty

### Breaking
- **LiteralAI** is being sunset and will be removed in one of the next releases. Please migrate to the official data layer instead.
- Telemetry is now opt-in by default and will be removed in the next release.

## [2.5.5] - 2025-04-14

### Added

- Avatars now support `.` in their name (will be replaced with `_`).
- Typed session accessors for user session
- Allow set attributes for the tags of the custom_js or custom_css
- Hovering a past chat in the sidebar will display the full title of the chat in a tooltip
- The `X-Chainlit-Session-id` header is now automatically set to facilitate sticky sessions with websockets
- `cl.ErrorMessage` now have a different avatar
- The copy button is now only displayed on the final message of a run, like feedback buttons
- CopilotFunction is now usable in custom JS
- Header link now have an optional `display_name` to display text next to the icon
- The default .env file loaded by chainlit is now configurable with `CHAINLIT_ENV_FILE`


### Changed

- **[breaking]**: `http_referer`, `http_cookie` and `languages` are no longer directly available in the session object. Instead, `environ` is available containing all of those plus other HTTP headers
- The scroll to the bottom animation is now smooth

## [2.4.400] - 2025-03-29

### Added

- `@cl.on_app_startup` and `@cl.on_app_shutdown`
- Configuration option for chat history default open state
- Configuration option for login page background image and filter
- Most commonly customized ui elements now have specific IDs

### Fixed

- App should no longer flicker on load
- Attachments icons for microsoft files should now correctly display
- Pasting should no longer be duplicated

## [2.4.302] - 2025-03-26

### Added

- Add thinking token support to langchain callback handler

### Fixed

- Pasting issues in the chat input
- Rename nl-NL.json to nl.json

## [2.4.301] - 2025-03-24

### Fixed

- Mcp button should not be displayed if `@on_mcp_connect` is not defined

## [2.4.3] - 2025-03-23

### Added

- Canvas mode for the element side bar if title == `canvas`
- Allow list for MCP stdio commands
- `key` parameter to `ElementSidebar.set_elements` method

### Fixed

- Literal AI should now correctly store custom elements props
- Element should correctly load from azure storage
- Plotly elements should now take full width

## [2.4.2] - 2025-03-19

### Added

- Hide commands button if all commands are specified as button.

### Fixed

- Chat profiles tooltip should no longer freeze is
... [TRUNCATED]
```

### File: CLAUDE.md
```md
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

@AGENTS.md
```

### File: CONTRIBUTING.md
```md
# Contribute to Chainlit

To contribute to Chainlit, you first need to set up the project on your local machine.

## Table of Contents

<!--
Generated using https://ecotrust-canada.github.io/markdown-toc/.
I've copy/pasted the whole document there, and then formatted it with prettier.
-->

- [Contribute to Chainlit](#contribute-to-chainlit)
  - [Table of Contents](#table-of-contents)
  - [Local setup](#local-setup)
    - [Requirements](#requirements)
    - [Set up the repo](#set-up-the-repo)
    - [Install dependencies](#install-dependencies)
    - [Build Frontend](#build-frontend)
  - [Start the Chainlit server from source](#start-the-chainlit-server-from-source)
  - [Start the UI from source](#start-the-ui-from-source)
  - [Run the tests](#run-the-tests)
    - [Backend unit tests](#backend-unit-tests)
    - [E2E tests](#e2e-tests)
    - [Headed/debugging](#headeddebugging)

## Local setup

### Requirements

1. Python >= `3.10`
2. uv ([See how to install](https://docs.astral.sh/uv/getting-started/installation/))
3. NodeJS >= `24` ([See how to install](https://nodejs.org/en/download))
4. Pnpm ([See how to install](https://pnpm.io/installation))

> **Note**
> If you are on windows, some pnpm commands like `pnpm run formatPython` won't work. You can fix this by changing the pnpm script-shell to bash: `pnpm config set script-shell "C:\\Program Files\\git\\bin\\bash.exe"` (default x64 install location, [Info](https://pnpm.io/cli/run#script-shell))

### Set up the repo

With this setup you can easily code in your fork and fetch updates from the main repository.

1. Go to [https://github.com/Chainlit/chainlit/fork](https://github.com/Chainlit/chainlit/fork) to fork the chainlit code into your own repository.
2. Clone your fork locally

```sh
git clone https://github.com/YOUR_USERNAME/YOUR_FORK.git
```

3. Go into your fork and list the current configured remote repository.

```sh
$ git remote -v
> origin  https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)
> origin  https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)
```

4. Specify the new remote upstream repository that will be synced with the fork.

```sh
git remote add upstream https://github.com/Chainlit/chainlit.git
```

5. Verify the new upstream repository you've specified for your fork.

```sh
$ git remote -v
> origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)
> origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)
> upstream  https://github.com/Chainlit/chainlit.git (fetch)
> upstream  https://github.com/Chainlit/chainlit.git (push)
```

### Install dependencies

The following command will install Python dependencies, Node (pnpm) dependencies and build the frontend.

```sh
cd backend
uv sync --extra tests --extra mypy --extra dev --extra custom-data
```

## Start the Chainlit server from source

Start by running `backend/chainlit/sample/hello.py` as an example.

```sh
cd backend
uv run chainlit run chainlit/sample/hello.py
```

You should now be able to access the Chainlit app you just launched on `http://127.0.0.1:8000`.

If you've made it this far, you can now replace `chainlit/sample/hello.py` by your own target. 😎

## Start the UI from source

First, you will have to start the server either [from source](#start-the-chainlit-server-from-source) or with `chainlit run...`. Since we are starting the UI from source, you can start the server with the `-h` (headless) option.

Then, start the UI.

```sh
cd frontend
pnpm run dev
```

If you visit `http://localhost:5173/`, it should connect to your local server. If the local server is not running, it should say that it can't connect to the server.

## Run the tests

### Backend unit tests

This will run the backend's unit tests.

```sh
cd backend
uv run pytest --cov=chainlit
```

### E2E tests

You may need additional configuration or dependency installation to run Cypress. See the [Cypress system requirements](https://docs.cypress.io/app/get-started/install-cypress#System-requirements) for details.

This will run end to end tests, assessing both the frontend, the backend and their interaction. First install cypress with `pnpm exec cypress install`, and then run:

```sh
// from root
pnpm test // will do cypress run
pnpm test -- --spec cypress/e2e/copilot // will run single test with the name copilot
pnpm test -- --spec "cypress/e2e/copilot,cypress/e2e/data_layer" // will run two tests with the names copilot and data_layer
pnpm test -- --spec "cypress/e2e/**/async-*" // will run all async tests
pnpm test -- --spec "cypress/e2e/**/sync-*" // will run all sync tests
pnpm test -- --spec "cypress/e2e/**/spec.cy.ts" // will run all usual tests
```

(Go grab a cup of something, this will take a while.)

For debugging purposes, you can use the **interactive mode** (Cypress UI). Run:

```
pnpm test:interactive // runs `cypress open`
```

Once you create a pull request, the tests will automatically run. It is a good practice to run the tests locally before pushing.

Make sure to run `uv sync` again whenever you've updated the frontend!

### Headed/debugging

Causes the Electron browser to be shown on screen and keeps it open after tests are done.
Extremely useful for debugging!

```sh
SINGLE_TEST=password_auth CYPRESS_OPTIONS='--headed --no-exit' pnpm test
```
```

### File: PRIVACY_POLICY.md
```md
# Privacy Policy

Chainlit doesn't collect any data from its users after 2.6.1 release.
```

### File: RELENG.md
```md
# Release Engineering Instructions

This document outlines the steps for maintainers to create a new release of the project.

## Prerequisites

- You must have maintainer permissions on the repo to create a new release.

## Steps

1. **Determine the new version number**:

   - We use semantic versioning (major.minor.patch).
   - Increment the major version for breaking changes, minor version for new features, patch version for bug fixes only.
   - If unsure, discuss with the maintainers to determine if it should be a major/minor version bump or new patch version.

2. **Bump the package version**:

   - Update `version` in `backend/chainlit/version.py`.
   - Update  `version` in `libs/*/package.json` if there were any changes in the corresponding directories.

3. **Update the changelog**:

   - Create a pull request to update the CHANGELOG.md file with the changes for the new release.
   - Mark any breaking changes clearly.
   - Get the changelog update PR reviewed and merged.

4. **Create a new release**:

   - In the GitHub repo, go to the "Releases" page and click "Draft a new release".
   - Input the new version number as the tag (e.g. 4.0.4).
   - Use the "Generate release notes" button to auto-populate the release notes from the changelog.
   - Review the release notes, make any needed edits for clarity.
   - If this is a full release after an RC, remove any "-rc" suffix from the version number.
   - Publish the release.

5. **Update any associated documentation and examples**:
   - If needed, create PRs to update the version referenced in the docs and example code to match the newly released version.
   - Especially important for documented breaking changes.

## RC (Release Candidate) Releases

- We create RC releases to allow testing before a full stable release
- Append "-rc" to the version number (e.g. 4.0.4-rc)
- Normally only bug fixes, no new features, between an RC and the final release version

Ping @dokterbob or @willydouhard for any questions or issues with the release process. Happy releasing!

```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for chainlit
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: .github\copilot-instructions.md
```md
# Chainlit Development Instructions

Chainlit is a Python framework for building conversational AI applications with Python backend and React frontend. It uses uv for Python dependency management and pnpm for Node.js packages.

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Working Effectively

### Bootstrap, Build, and Test the Repository

**CRITICAL**: All commands must complete - NEVER CANCEL any build or test operations. Use appropriate timeouts.

1. **Install Dependencies (Required first)**:
   ```bash
   # Install uv (if not available)
   python3 -m pip install pipx
   python3 -m pipx install uv
   export PATH="$HOME/.local/bin:$PATH"
   
   # Install pnpm (if not available)  
   npm install -g pnpm
   
   # Install Python dependencies - takes ~2 minutes, NEVER CANCEL
   cd backend
   uv sync --extra tests --extra mypy --extra dev --extra custom-data
   # Timeout: Use 300+ seconds (5+ minutes)
   
   # Install Node.js dependencies - takes ~3 minutes, NEVER CANCEL  
   cd ..
   pnpm install --frozen-lockfile
   # Timeout: Use 600+ seconds (10+ minutes)
   # NOTE: Cypress download may fail due to network restrictions - this is expected in CI environments
   ```

2. **Build the Frontend - takes ~1 minute, NEVER CANCEL**:
   ```bash
   pnpm run buildUi
   # Timeout: Use 300+ seconds (5+ minutes)
   ```

3. **Run Tests**:
   ```bash
   # Backend tests - takes ~17 seconds, NEVER CANCEL
   cd backend
   export PATH="$HOME/.local/bin:$PATH"
   uv run pytest --cov=chainlit/
   # Timeout: Use 120+ seconds (2+ minutes)
   
   # Frontend tests - takes ~4 seconds
   cd ../frontend  
   pnpm test
   # Timeout: Use 60 seconds
   
   # E2E tests require Cypress download - may not work in restricted environments
   # If available: pnpm test (takes variable time depending on tests)
   ```

4. **Run Development Servers**:
   ```bash
   # Start backend (in one terminal)
   cd backend
   export PATH="$HOME/.local/bin:$PATH" 
   uv run chainlit run chainlit/sample/hello.py -h
   # Available at http://localhost:8000
   
   # Start frontend dev server (in another terminal)
   cd frontend
   pnpm run dev  
   # Available at http://localhost:5173/
   ```

## Validation

### Manual Validation Requirements
- **ALWAYS** manually validate any changes by running complete scenarios.
- **ALWAYS** test the Chainlit application after making changes.
- Create a test app and verify it runs: `uv run chainlit run /path/to/test.py -h`
- **ALWAYS** run through at least one complete user workflow after making changes.

### Linting and Formatting - takes ~2 minutes, NEVER CANCEL
```bash
# Run all linting (UI + Python) 
pnpm run lint
# Timeout: Use 300+ seconds (5+ minutes)

# Format UI code - takes ~5 seconds
pnpm run formatUi

# Format Python code using ruff (preferred)
cd backend
export PATH="$HOME/.local/bin:$PATH"
uv run ruff format chainlit/ tests/

# NOTE: pnpm run formatPython may fail if black is not installed
# Use ruff format instead as shown above
```

### CI Requirements
- **ALWAYS** run `pnpm run lint` before committing or the CI (.github/workflows/ci.yaml) will fail.
- The CI runs: pytest, lint-backend, lint-ui, and e2e-tests.
- **NEVER CANCEL** any CI commands - they take time but must complete.

## Key Project Structure

### Repository Root
```
/
├── README.md
├── CONTRIBUTING.md  
├── package.json              # Root pnpm workspace config
├── pnpm-workspace.yaml       # Workspace definition
├── backend/                  # Python backend with uv
├── frontend/                 # React frontend app
├── libs/
│   ├── react-client/         # React client library
│   └── copilot/             # Copilot functionality
├── cypress/                  # E2E tests
└── .github/
    ├── workflows/            # CI/CD pipelines
    └── actions/              # Reusable GitHub actions
```

### Working with the Backend
- **Technology**: Python 3.10+ with uv, FastAPI, SocketIO
- **Entry point**: `backend/chainlit/` 
- **Tests**: `backend/tests/`
- **Dependencies**: Defined in `backend/pyproject.toml`
- **Hello app**: `backend/chainlit/sample/hello.py`

### Working with the Frontend  
- **Technology**: React 18+ with Vite, TypeScript, Tailwind CSS
- **Entry point**: `frontend/src/`
- **Dependencies**: Defined in `frontend/package.json`
- **Build output**: `frontend/dist/`

## Common Tasks

### Creating a New Chainlit App
```python
# Create app.py
import chainlit as cl

@cl.on_message
async def main(message: cl.Message):
    await cl.Message(content=f"You said: {message.content}").send()

# Run it
uv run chainlit run app.py -w
```

### Timing Expectations
- **pnpm install**: ~3 minutes (may fail on Cypress - this is normal)
- **uv install**: ~2 minutes  
- **pnpm run buildUi**: ~1 minute
- **pnpm run lint**: ~2 minutes
- **Backend tests**: ~17 seconds
- **Frontend tests**: ~4 seconds
- **pnpm run formatUi**: ~5 seconds

### Common Gotchas
- **NEVER CANCEL** long-running operations - they need time to complete.
- Cypress download often fails in CI environments - this is expected.
- Use `uv run` prefix for all Python commands in backend.
- Use `export PATH="$HOME/.local/bin:$PATH"` to ensure uv is available.
- The `pnpm run formatPython` command may fail - use `uv run ruff format` instead.
- Frontend dev server connects to backend at localhost:8000.
- Always start backend before frontend for development.

### File Locations for Quick Reference
- **Main CLI**: `backend/chainlit/cli/`
- **Server code**: `backend/chainlit/server.py`
- **Frontend app**: `frontend/src/App.tsx`
- **React client**: `libs/react-client/src/`
- **CI workflows**: `.github/workflows/ci.yaml`
- **uv config**: `backend/pyproject.toml`
- **Frontend config**: `frontend/package.json`

## Requirements
- **Python**: >= 3.10
- **Node.js**: >= 20 (24+ recommended)
- **uv**: 2.1.3 (install via pipx)
- **pnpm**: Latest (install via npm)
```

### File: docs\context7.md
```md
# Context7 Library IDs

Pre-resolved library IDs for [Context7 MCP](https://context7.com). Use these when looking up documentation via the Context7 MCP  `query-docs` tool.

## Language

| Library/Framework | Context7 Library ID | Notes |
|-------------------|---------------------|-------|
| Python 3.13 | /websites/python_3_13 | Standard library, language features |
| TypeScript | /websites/typescriptlang | Type system, compiler options |

## Backend

| Library/Framework | Context7 Library ID | Notes |
|-------------------|---------------------|-------|
| Pydantic | /websites/pydantic_dev | Models, validation, serialization |
| FastAPI | /websites/fastapi_tiangolo | Web framework, async endpoints |
| HTTPX | /encode/httpx | Async HTTP client (core dependency) |
| python-socketio | /miguelgrinberg/python-socketio | SocketIO server — core real-time transport |

## LLM integrations

| Library/Framework | Context7 Library ID | Notes |
|-------------------|---------------------|-------|
| MCP Python SDK | /modelcontextprotocol/python-sdk | Official MCP SDK (core dependency) |
| OpenAI Python | /openai/openai-python | OpenAI API client |
| Anthropic Python | /anthropics/anthropic-sdk-python | Anthropic API client |
| LangChain | /websites/langchain_oss_python_langchain | LLM orchestration, chains, agents |
| LlamaIndex | /websites/developers_llamaindex_ai_python | RAG / LLM data framework |
| Semantic Kernel | /microsoft/semantic-kernel | Microsoft AI orchestration SDK |
| Semantic Kernel docs | /websites/learn_microsoft_en-us_semantic-kernel | Official Microsoft docs |
| MistralAI | /mistralai/client-python | MistralAI API client |

## Persistence

| Library/Framework | Context7 Library ID | Notes |
|-------------------|---------------------|-------|
| SQLAlchemy | /websites/sqlalchemy_en_20 | ORM for PostgreSQL/SQLite |
| asyncpg | /websites/magicstack_github_io_asyncpg_current | Async PostgreSQL driver |
| boto3 | /boto/boto3 | AWS SDK — DynamoDB + S3 |
| Azure SDK | /azure/azure-sdk-for-python | Azure SDK for Python |
| Azure Storage | /websites/learn_microsoft_en-us_azure_storage | Azure Blob Storage + Data Lake |
| Google Cloud Storage | /googleapis/python-storage | GCS persistence |

## Platform integrations

| Library/Framework | Context7 Library ID | Notes |
|-------------------|---------------------|-------|
| Slack Bolt | /slackapi/bolt-python | Slack app framework |
| Discord | /llmstxt/discord_llms_txt | Discord bot API |
| pandas | /websites/pandas_pydata | Data analysis (optional dependency) |

## Frontend — core

| Library/Framework | Context7 Library ID | Notes |
|-------------------|---------------------|-------|
| React | /websites/react_dev | Core UI library |
| React Router | /websites/reactrouter_6_30_3 | Client-side routing (v6) |
| Vite | /websites/vite_dev | Build tool and dev server |

## Frontend — UI

| Library/Framework | Context7 Library ID | Notes |
|-------------------|---------------------|-------|
| Tailwind CSS | /websites/v3_tailwindcss | Utility-first CSS framework (v3) |
| Radix UI | /websites/radix-ui_primitives | Unstyled UI primitives |
| lucide-react | /websites/lucide_dev_guide | Icon library |

## Frontend — state & data

| Library/Framework | Context7 Library ID | Notes |
|-------------------|---------------------|-------|
| Zustand | /websites/zustand_pmnd_rs | For future Recoil migration |
| SWR | /vercel/swr-site | Data fetching hooks |
| react-hook-form | /websites/react-hook-form | Form state management |
| Zod | /llmstxt/zod_dev_llms_txt | Schema validation |
| socket.io-client | /websites/socket_io_v4_client-api | WebSocket client |

## Frontend — rendering

| Library/Framework | Context7 Library ID | Notes |
|-------------------|---------------------|-------|
| react-markdown | /remarkjs/react-markdown | Markdown renderer for React |
| remark | /remarkjs/remark | Markdown processor |
| react-remark | /remarkjs/react-remark | React hooks for remark |
| remark-gfm | /remarkjs/remark-gfm | GitHub Flavored Markdown plugin |
| remark-math | /remarkjs/remark-math | Math syntax plugin |
| highlight.js | /highlightjs/highlight.js | Syntax highlighting |
| Plotly.js | /plotly/plotly.js | Charting library |
| react-plotly.js | /plotly/react-plotly.js | React wrapper for Plotly |

## Frontend — i18n

| Library/Framework | Context7 Library ID | Notes |
|-------------------|---------------------|-------|
| i18next | /llmstxt/i18next_llms-full_txt | Internationalization framework |
| react-i18next | /i18next/react-i18next | React bindings for i18next |

## Infra

| Library/Framework | Context7 Library ID | Notes |
|-------------------|---------------------|-------|
| GitHub Actions | /websites/github_en_actions | CI/CD workflows |

```

### File: .github\ISSUE_TEMPLATE\bug_report.md
```md
---
name: Bug report
about: Create a report to help us improve
title: ''
labels: needs-triage
assignees: ''
type: 'Bug'
---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:

1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Desktop (please complete the following information):**

- OS: [e.g. iOS]
- Browser [e.g. chrome, safari]
- Version [e.g. 22]

**Smartphone (please complete the following information):**

- Device: [e.g. iPhone6]
- OS: [e.g. iOS8.1]
- Browser [e.g. stock browser, safari]
- Version [e.g. 22]

**Additional context**
Add any other context about the problem here.

```

### File: .github\ISSUE_TEMPLATE\feature_request.md
```md
---
name: Feature request
about: Suggest an idea for this project
title: ''
labels: needs-triage
assignees: ''
type: 'Feature'
---

**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions or features you've considered.

**Additional context**
Add any other context or screenshots about the feature request here.

```

