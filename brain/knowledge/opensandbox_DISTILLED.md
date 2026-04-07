---
id: opensandbox
type: knowledge
owner: OA_Triage
---
# opensandbox
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align="center">
  <img src="docs/assets/logo.svg" alt="OpenSandbox logo" width="150" />

  <h1>OpenSandbox</h1>

  <p align="center">
    <a href="https://trendshift.io/repositories/21828" target="_blank">
      <img src="https://trendshift.io/api/badge/repositories/21828" alt="alibaba%2FOpenSandbox | Trendshift" style="width: 320px; height: 70px;" width="320" height="70" />
    </a>
  </p>

<p align="center">
  <a href="https://github.com/alibaba/OpenSandbox">
    <img src="https://img.shields.io/github/stars/alibaba/OpenSandbox.svg?style=social" alt="GitHub stars" />
  </a>
  <a href="https://deepwiki.com/alibaba/OpenSandbox">
    <img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki" />
  </a>
  <a href="https://www.apache.org/licenses/LICENSE-2.0.html">
    <img src="https://img.shields.io/badge/license-Apache%202.0-blue.svg" alt="license" />
  </a>
  <a href="https://badge.fury.io/py/opensandbox">
    <img src="https://badge.fury.io/py/opensandbox.svg" alt="PyPI version" />
  </a>
  <a href="https://badge.fury.io/js/@alibaba-group%2Fopensandbox">
    <img src="https://badge.fury.io/js/@alibaba-group%2Fopensandbox.svg" alt="npm version" />
  </a>
  <a href="https://landscape.cncf.io/?item=orchestration-management--scheduling-orchestration--opensandbox">
    <img src="https://img.shields.io/badge/CNCF-Landscape-0C66E4" alt="CNCF Landscape" />
  </a>
  <a href="https://qr.dingtalk.com/action/joingroup?code=v1,k1,A4Bgl5q1I1eNU/r33D18YFNrMY108aFF38V+r19RJOM=&_dt_no_comment=1&origin=11">
    <img src="https://img.shields.io/badge/DingTalk-Join-0089FF?logo=dingtalk&logoColor=white" alt="DingTalk" />
  </a>
  <a href="https://github.com/alibaba/OpenSandbox/actions">
    <img src="https://github.com/alibaba/OpenSandbox/actions/workflows/real-e2e.yml/badge.svg?branch=main" alt="E2E Status" />
  </a>
  <a href="https://github.com/alibaba/OpenSandbox/actions">
    <img src="https://github.com/alibaba/OpenSandbox/actions/workflows/kubernetes-nightly-build.yml/badge.svg?branch=main" alt="E2E Status" />
  </a>
</p>

  <hr />
</div>

[Documentation](https://open-sandbox.ai/) | [中文文档](https://open-sandbox.ai/zh/)

OpenSandbox is a **general-purpose sandbox platform** for AI applications, offering multi-language SDKs, unified sandbox APIs, and Docker/Kubernetes runtimes for scenarios like Coding Agents, GUI Agents, Agent Evaluation, AI Code Execution, and RL Training.

OpenSandbox is now listed in the [CNCF Landscape](https://landscape.cncf.io/?item=orchestration-management--scheduling-orchestration--opensandbox).

## Features

- **Multi-language SDKs**: Provides sandbox SDKs in Python, Java/Kotlin, JavaScript/TypeScript, C#/.NET, Go (Roadmap), and more.
- **Sandbox Protocol**: Defines sandbox lifecycle management APIs and sandbox execution APIs so you can extend custom sandbox runtimes.
- **Sandbox Runtime**: Built-in lifecycle management supporting Docker and [high-performance Kubernetes runtime](./kubernetes), enabling both local runs and large-scale distributed scheduling.
- **Sandbox Environments**: Built-in Command, Filesystem, and Code Interpreter implementations. Examples cover Coding Agents (e.g., Claude Code), browser automation (Chrome, Playwright), and desktop environments (VNC, VS Code).
- **Network Policy**: Unified [Ingress Gateway](components/ingress) with multiple routing strategies plus per-sandbox [egress controls](components/egress).
- **Strong Isolation**: Supports secure container runtimes like gVisor, Kata Containers, and Firecracker microVM for enhanced isolation between sandbox workloads and the host. See [Secure Container Runtime Guide](docs/secure-container.md) for details.

## Examples

### Basic Sandbox Operations [Docker]

Requirements:

- Docker (required for local execution)
- Python 3.10+ (required for examples and local runtime)

#### 1. Install and Configure the Sandbox Server

```bash
uv pip install opensandbox-server
opensandbox-server init-config ~/.sandbox.toml --example docker
```

> If you prefer working from source, you can still clone the repo for development, but you no longer need to clone this repository just to start the server.
> You'll also require an instance of docker running.
> ```bash
> git clone https://github.com/alibaba/OpenSandbox.git && cd OpenSandbox/server
> cp opensandbox_server/examples/example.config.toml ~/.sandbox.toml
> uv sync && uv run python -m opensandbox_server.main
> ```

#### 2. Start the Sandbox Server

```bash
opensandbox-server

# Show help
# opensandbox-server -h
```

#### 3. Create a Code Interpreter and Execute Commands/Codes

Install the Code Interpreter SDK

```bash
uv pip install opensandbox-code-interpreter
```

Create a sandbox and execute commands and codes.

```python
import asyncio
from datetime import timedelta

from code_interpreter import CodeInterpreter, SupportedLanguage
from opensandbox import Sandbox
from opensandbox.models import WriteEntry

async def main() -> None:
    # 1. Create a sandbox
    sandbox = await Sandbox.create(
        "opensandbox/code-interpreter:v1.0.2",
        entrypoint=["/opt/opensandbox/code-interpreter.sh"],
        env={"PYTHON_VERSION": "3.11"},
        timeout=timedelta(minutes=10),
    )

    async with sandbox:

        # 2. Execute a shell command
        execution = await sandbox.commands.run("echo 'Hello OpenSandbox!'")
        print(execution.logs.stdout[0].text)

        # 3. Write a file
        await sandbox.files.write_files([
            WriteEntry(path="/tmp/hello.txt", data="Hello World", mode=644)
        ])

        # 4. Read a file
        content = await sandbox.files.read_file("/tmp/hello.txt")
        print(f"Content: {content}") # Content: Hello World

        # 5. Create a code interpreter
        interpreter = await CodeInterpreter.create(sandbox)

        # 6. Execute Python code (single-run, pass language directly)
        result = await interpreter.codes.run(
              """
                  import sys
                  print(sys.version)
                  result = 2 + 2
                  result
              """,
              language=SupportedLanguage.PYTHON,
        )

        print(result.result[0].text) # 4
        print(result.logs.stdout[0].text) # 3.11.14

    # 7. Cleanup the sandbox
    await sandbox.kill()

if __name__ == "__main__":
    asyncio.run(main())
```

### More Examples

OpenSandbox provides examples covering SDK usage, agent integrations, browser automation, and training workloads. All example code is located in the `examples/` directory.

#### 🎯 Basic Examples

- **[code-interpreter](examples/code-interpreter/README.md)** - End-to-end Code Interpreter SDK workflow in a sandbox.
- **[aio-sandbox](examples/aio-sandbox/README.md)** - All-in-One sandbox setup using the OpenSandbox SDK.
- **[agent-sandbox](examples/agent-sandbox/README.md)** - Example integration for running OpenSandbox workloads on Kubernetes with [kubernetes-sigs/agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox).
- **Volumes** — [Docker PVC / named volumes](examples/docker-pvc-volume-mount/README.md), [Docker OSSFS](examples/docker-ossfs-volume-mount/README.md), [Kubernetes PVC](examples/kubernetes-pvc-volume-mount/README.md): persistent and shared storage patterns.

#### 🤖 Coding Agent Integrations

- **Coding CLIs** — [Claude Code](examples/claude-code/README.md), [Gemini CLI](examples/gemini-cli/README.md), [OpenAI Codex CLI](examples/codex-cli/README.md), [Qwen Code](examples/qwen-code/README.md), [Kimi CLI](examples/kimi-cli/README.md): run each vendor CLI inside OpenSandbox.
- **[langgraph](examples/langgraph/README.md)** - LangGraph state-machine workflow that creates/runs a sandbox job with fallback retry.
- **[google-adk](examples/google-adk/README.md)** - Google ADK agent using OpenSandbox tools to write/read files and run commands.
- **[nullclaw](examples/nullclaw/README.md)** - Launch a [Nullclaw](https://github.com/nullclaw/nullclaw) Gateway inside a sandbox.
- **[openclaw](examples/openclaw/README.md)** - Launch an OpenClaw Gateway inside a sandbox.

#### 🌐 Browser and Desktop Environments

- **[chrome](examples/chrome/README.md)** - Chromium sandbox with VNC and DevTools access for automation and debugging.
- **[playwright](examples/playwright/README.md)** - Playwright + Chromium headless scraping and testing example.
- **[desktop](examples/desktop/README.md)** - Full desktop environment in a sandbox with VNC access.
- **[vscode](examples/vscode/README.md)** - code-server (VS Code Web) running inside a sandbox for remote dev.

#### 🧠 ML and Training

- **[rl-training](examples/rl-training/README.md)** - DQN CartPole training in a sandbox with checkpoints and summary output.

For more details, please refer to [examples](examples/README.md) and the README files in each example directory.

## Project Structure

| Directory | Description                                                      |
|-----------|------------------------------------------------------------------|
| [`sdks/`](sdks/) | Multi-language SDKs (Python, Java/Kotlin, TypeScript/JavaScript, C#/.NET) |
| [`specs/`](specs/README.md) | OpenAPI specs and lifecycle specifications                      |
| [`server/`](server/README.md) | Python FastAPI sandbox lifecycle server                          |
| [`kubernetes/`](kubernetes/README.md) | Kubernetes deployment and examples                               |
| [`components/execd/`](components/execd/README.md) | Sandbox execution daemon (commands and file operations)          |
| [`components/ingress/`](components/ingress/README.md) | Sandbox traffic ingress proxy                                    |
| [`components/egress/`](components/egress/README.md) | Sandbox network egress control                                   |
| [`sandboxes/`](sandboxes/) | Runtime sandbox implementations                                   |
| [`examples/`](examples/README.md) | Integration examples and use cases                               |
| [`oseps/`](oseps/README.md) | OpenSandbox Enhancement Proposals                                |
| [`docs/`](docs/) | Architecture and design documentation                            |
| [`tests/`](tests/) | Cross-component E2E tests                                        |
| [`scripts/`](scripts/) | Development and maintenance scripts                              |

For detailed architecture, see [docs/architecture.md](docs/architecture.md).

## Documentation

- [docs/architecture.md](docs/architecture.md) – Overall architecture & design philosophy
- [oseps/README.md](oseps/README.md) – OpenSandbox Enhancement Proposals
- SDK
  - Sandbox base SDK ([Java/Kotlin SDK](sdks/sandbox/kotlin/README.md), [Python SDK](sdks/sandbox/python/README.md), [JavaScript/TypeScript SDK](sdks/sandbox/javascript/README.md), [C#/.NET SDK](sdks/sandbox/csharp/README.md)) - includes sandbox lifecycle, command execution, file operations
  - Code Interpreter SDK ([Java/Kotlin SDK](sdks/code-interpreter/kotlin/README.md), [Python SDK](sdks/code-interpreter/python/README.md), [JavaScript/TypeScript SDK](sdks/code-interpreter/javascript/README.md), [C#/.NET SDK](sdks/code-interpreter/csharp/README.md)) - code interpreter
- [specs/README.md](specs/README.md) - OpenAPI definitions for sandbox lifecycle API and sandbox execution API
- [server/README.md](server/README.md) - Sandbox server startup and configuration; supports Docker and Kubernetes runtimes

## License

This project is open source under the [Apache 2.0 License](LICENSE).

## Roadmap [2026.03]

### SDK

- **Sandbox client connection pool** - Client-side sandbox connection pool management, providing pre-provisioned sandboxes to obtain an environment at X ms.
- **Go SDK** - Go client SDK for sandbox lifecycle management, command execution, and file operations.

### Sandbox Runtime

- **Persistent volumes** - Mountable persistent volumes for sandboxes (see [Proposal 0003](oseps/0003-volume-and-volumebinding-support.md)).
- **Local lightweight sandbox** - Lightweight sandbox for AI tools running directly on PCs.
- **Secure Container** - Secure sandbox for AI Agents running inside container.

### Deployment

- **Guide** - Deployment guide for self-hosted Kubernetes cluster.

## Contact and Discussion

- Issues: Submit bugs, feature requests, or design discussions through GitHub Issues
- DingTalk: Join the [OpenSandbox technical discussion group](https://qr.dingtalk.com/action/joingroup?code=v1,k1,A4Bgl5q1I1eNU/r33D18YFNrMY108aFF38V+r19RJOM=&_dt_no_comment=1&origin=11)
## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=alibaba/OpenSandbox&type=date&legend=top-left)](https://www.star-history.com/#alibaba/OpenSandbox&type=date&legend=top-left)

```

### File: cli\README.md
```md
# OpenSandbox CLI

A command-line interface for managing OpenSandbox environments from your terminal. Built on top of the [OpenSandbox Python SDK](../sdks/sandbox/python/README.md), the CLI provides intuitive commands for sandbox lifecycle management, file operations, command execution, and code interpretation.

## Installation

### pip

```bash
pip install opensandbox-cli
```

### uv

```bash
uv tool install opensandbox-cli
```

### pipx (recommended for global CLI usage)

```bash
pipx install opensandbox-cli
```

## Overview

```bash
osb --help
```

![CLI Help](assets/cli_help.png)

## Quick Start

### Step 0: Start the OpenSandbox Server

Before using the CLI, make sure the OpenSandbox server is running. See the root [README.md](../README.md) for startup instructions.

```bash
opensandbox-server
```

![Start OpenSandbox Server](assets/start_opensandbox_server.png)

### Step 1: Install the CLI

```bash
cd cli
uv sync
uv run osb --help
```

![Install CLI](assets/install_cli.png)

### Step 2: Initialize Configuration

```bash
osb config init
osb config set connection.domain localhost:8080
osb config set connection.protocol http
```

![Init CLI](assets/init_cli.png)

### Step 3: Create a Sandbox

```bash
osb sandbox create --image python:3.12
```

![Create Sandbox](assets/cli_create_sandbox.png)

### Step 4: List Sandboxes

```bash
# Table output (default)
osb sandbox list

# JSON output for scripting
osb -o json sandbox list
```

![List Sandboxes](assets/cli_list_sandbox.png)

![List Sandboxes JSON](assets/cli_list_sandbox_json.png)

### Short ID Matching

Like Docker, you don't need to type the full sandbox ID — just enough characters to uniquely identify the target sandbox:

```bash
# Full ID
osb sandbox get db027570-4f86-45f8-b1a8-c31a2dd90da8

# Short prefix — as long as it's unambiguous
osb sandbox get db02
osb exec db02 -- echo "hello"
```

If the prefix matches multiple sandboxes, the CLI will report an error listing the matches so you can be more specific.

![Short ID Matching](assets/cli_sandbox_search.png)

### Step 5: Execute Commands

```bash
osb exec <sandbox-id> -- echo "hello world"
osb exec <sandbox-id> -- python -c "print(1+1)"
```

![Execute Commands](assets/cli_sandbox_exec.png)

### Step 6: File Operations

```bash
# Write a file
osb file write <sandbox-id> /tmp/test.txt -c "hello"

# Read it back
osb file cat <sandbox-id> /tmp/test.txt
```

![File Operations](assets/cli_sandbox_file.png)

### Step 7: Cleanup

```bash
osb sandbox kill <sandbox-id>
osb sandbox list
```

![Kill Sandbox](assets/cli_kill_sandbox.png)

## Command Reference

### `osb sandbox` — Lifecycle Management

| Command    | Description                                 |
| ---------- | ------------------------------------------- |
| `create`   | Create a new sandbox                        |
| `list`     | List sandboxes (with optional filters)      |
| `get`      | Get sandbox details by ID                   |
| `kill`     | Terminate one or more sandboxes             |
| `pause`    | Pause a running sandbox                     |
| `resume`   | Resume a paused sandbox                     |
| `renew`    | Renew sandbox expiration                    |
| `endpoint` | Get public endpoint for a sandbox port      |
| `health`   | Check sandbox health                        |
| `metrics`  | Get sandbox resource metrics (CPU, memory)  |

### `osb command` — Command Execution

| Command     | Description                               |
| ----------- | ----------------------------------------- |
| `run`       | Run a shell command in the sandbox        |
| `status`    | Get command execution status              |
| `logs`      | Get background command logs               |
| `interrupt` | Interrupt a running command               |

### `osb exec` — Quick Command Shortcut

```bash
osb exec <sandbox-id> -- <command>
```

Shortcut for `osb command run`. Everything after `--` is passed as the command.

### `osb file` — File Operations

| Command    | Description                                |
| ---------- | ------------------------------------------ |
| `cat`      | Read file contents                         |
| `write`    | Write content to a file                    |
| `upload`   | Upload a local file to the sandbox         |
| `download` | Download a file from the sandbox           |
| `rm`       | Delete files                               |
| `mv`       | Move or rename a file                      |
| `mkdir`    | Create directories                         |
| `rmdir`    | Remove directories                         |
| `search`   | Search for files by pattern                |
| `info`     | Get file/directory metadata                |
| `chmod`    | Set file permissions                       |
| `replace`  | Find and replace content in a file         |

### `osb code` — Code Interpreter

| Command     | Description                               |
| ----------- | ----------------------------------------- |
| `run`       | Execute code in a sandbox                 |
| `context`   | Manage code execution contexts            |
| `interrupt` | Interrupt a running code execution        |

### `osb devops` — DevOps Diagnostics

| Command   | Description                                          |
| --------- | ---------------------------------------------------- |
| `logs`    | Retrieve container/pod logs                          |
| `inspect` | Retrieve detailed container/pod inspection info      |
| `events`  | Retrieve events related to a sandbox                 |
| `summary` | One-shot diagnostics: inspect + events + logs combined |

```bash
# Quick diagnostics summary
osb devops summary <sandbox-id>

# Get last 500 log lines
osb devops logs <sandbox-id> --tail 500

# Get logs from the last 30 minutes
osb devops logs <sandbox-id> --since 30m

# Detailed container/pod inspection
osb devops inspect <sandbox-id>

# View events (up to 100)
osb devops events <sandbox-id> --limit 100
```

All devops commands return plain text output, making them ideal for both human reading and AI agent consumption.

![DevOps Summary 1](assets/cli_devops_summary_1.png)

![DevOps Summary 2](assets/cli_devops_summary_2.png)

### `osb skills` — AI Coding Skills

| Command     | Description                                          |
| ----------- | ---------------------------------------------------- |
| `install`   | Install OpenSandbox troubleshooting skill for AI tools |
| `list`      | List supported targets and their install status      |
| `uninstall` | Remove installed skill from AI tools                 |

The troubleshooting skill enables AI coding assistants to automatically diagnose sandbox issues (OOM, crashes, image pull errors, etc.). Supported targets:

| Target    | AI Tool          | Install Location |
| --------- | ---------------- | ---------------- |
| `claude`  | Claude Code      | `~/.claude/skills/` |
| `cursor`  | Cursor           | `~/.cursor/rules/` |
| `codex`   | Codex            | `~/.codex/instructions.md` |
| `copilot` | GitHub Copilot   | `~/.github/copilot-instructions.md` |
| `windsurf`| Windsurf         | `~/.windsurfrules` |
| `cline`   | Cline            | `~/.clinerules` |

```bash
# Install for Claude Code (default)
osb skills install

# Install for a specific tool
osb skills install --target cursor

# Install for all supported tools
osb skills install --target all

# Check install status
osb skills list

# Uninstall
osb skills uninstall --target claude
```

### `osb config` — Configuration

| Command | Description                                |
| ------- | ------------------------------------------ |
| `init`  | Create a default config file               |
| `show`  | Show resolved configuration                |

## Configuration

The CLI resolves configuration from multiple sources with the following priority (highest to lowest):

1. **CLI flags** — `--api-key`, `--domain`, `--protocol`, `--timeout`
2. **Environment variables** — `OPEN_SANDBOX_API_KEY`, `OPEN_SANDBOX_DOMAIN`, `OPEN_SANDBOX_PROTOCOL`, `OPEN_SANDBOX_REQUEST_TIMEOUT`, `OPEN_SANDBOX_OUTPUT`
3. **Config file** — `~/.opensandbox/config.toml` (or path specified via `--config`)
4. **SDK defaults**

## Development

For local CLI development in this monorepo, prefer `uv sync` from the `cli/` directory. That workflow honors the local `[tool.uv.sources]` overrides for `opensandbox` and `opensandbox-code-interpreter`, so the CLI resolves against the checked-out SDKs instead of published packages.

```bash
cd cli
uv sync
uv run osb --help
```

If you specifically need an editable install into another environment, install the SDK dependencies from their local paths first, then install the CLI.

### Config File Format

```toml
[connection]
api_key = "your-api-key"
domain = "localhost:8080"
protocol = "http"
request_timeout = 30

[output]
format = "table"    # table | json | yaml
color = true

[defaults]
image = "python:3.11"
timeout = "10m"
```

## Global Options

| Option                        | Description                      |
| ----------------------------- | -------------------------------- |
| `--api-key TEXT`              | API key for authentication       |
| `--domain TEXT`               | API server domain                |
| `--protocol [http\|https]`    | Protocol                         |
| `--timeout INTEGER`           | Request timeout in seconds       |
| `-o, --output [table\|json\|yaml]` | Output format              |
| `--config PATH`               | Config file path                 |
| `-v, --verbose`               | Enable debug output              |
| `--no-color`                  | Disable colored output           |
| `--version`                   | Show version                     |

## Output Formats

The CLI supports three output formats via the `-o` / `--output` flag:

- **`table`** (default) — Human-friendly tables powered by [Rich](https://github.com/Textualize/rich)
- **`json`** — Machine-readable JSON
- **`yaml`** — YAML output

```bash
# Table (default)
osb sandbox list

# JSON for scripting
osb -o json sandbox list

# YAML
osb -o yaml sandbox list
```

```

### File: docs\package.json
```json
{
  "name": "opensandbox-docs",
  "private": true,
  "packageManager": "pnpm@9.15.0",
  "scripts": {
    "docs:sync": "node .vitepress/scripts/docs-manifest.mjs",
    "docs:spec": "node ../scripts/spec-doc/generate-spec.js --output docs/public/api/spec-inline.js",
    "docs:dev": "pnpm docs:sync && pnpm docs:spec && vitepress dev",
    "docs:build": "pnpm docs:sync && pnpm docs:spec && vitepress build",
    "docs:preview": "vitepress preview"
  },
  "devDependencies": {
    "vitepress": "^1.6.4"
  }
}

```

### File: docs\README.md
```md
# OpenSandbox Docs Site

This directory hosts the VitePress site for OpenSandbox.

## Local development

```bash
nvm use 22
cd docs
pnpm install
pnpm docs:dev
```

## Build

```bash
nvm use 22
cd docs
pnpm install
pnpm docs:build
```

## Notes

- Site content is generated from repository README and docs markdown files.
- Run `pnpm docs:sync` to regenerate the manifest and routed pages.
- Run `pnpm docs:spec` to regenerate `docs/public/api/spec-inline.js` from `specs/sandbox-lifecycle.yml`.

```

### File: examples\README.md
```md
# OpenSandbox Examples

Examples for common OpenSandbox use cases. Each subdirectory contains runnable code and documentation.

## Integrations / Sandboxes
- 🧰 [**aio-sandbox**](aio-sandbox): All-in-one sandbox setup using OpenSandbox SDK and agent-sandbox
- <img src="https://kubernetes.io/icons/favicon-32.png" alt="Kubernetes" width="16" height="16" style="display:inline-block;width:16px;height:16px;vertical-align:middle;margin-right:4px;" /> [**agent-sandbox**](agent-sandbox): Create a kubernetes-sigs/agent-sandbox instance and run a command
- 🧪 [**code-interpreter**](code-interpreter): Code Interpreter SDK singleton example
- 💾 [**host-volume-mount**](host-volume-mount): Mount host directories into sandboxes (read-write, read-only, subpath)
- 📦 [**docker-pvc-volume-mount**](docker-pvc-volume-mount): Mount Docker named volumes via the `pvc` backend (parity with Kubernetes PVC API)
- ☁️ [**docker-ossfs-volume-mount**](docker-ossfs-volume-mount): Mount OSSFS volumes in Docker runtime (inline credentials, subpath, sharing)
- <img src="https://kubernetes.io/icons/favicon-32.png" alt="Kubernetes" width="16" height="16" style="display:inline-block;width:16px;height:16px;vertical-align:middle;margin-right:4px;" /> [**kubernetes-pvc-volume-mount**](kubernetes-pvc-volume-mount): Mount Kubernetes PersistentVolumeClaims into sandboxes for persistent storage
- 🎯 [**rl-training**](rl-training): Reinforcement learning training loop inside a sandbox
- <img src="https://img.shields.io/badge/-%20-D97757?logo=claude&logoColor=white&style=flat-square" alt="Claude" width="16" height="16" style="display:inline-block;width:16px;height:16px;vertical-align:middle;margin-right:4px;" /> [**claude-code**](claude-code): Call Claude (Anthropic) API/CLI within the sandbox
- <img src="https://geminicli.com/favicon.ico" alt="Google Gemini" width="16" height="16" style="display:inline-block;width:16px;height:16px;vertical-align:middle;margin-right:4px;" /> [**gemini-cli**](gemini-cli): Call Google Gemini within the sandbox
- <img src="https://developers.openai.com/favicon.png" alt="OpenAI" width="16" height="16" style="display:inline-block;width:16px;height:16px;vertical-align:middle;margin-right:4px;" /> [**codex-cli**](codex-cli): Call OpenAI/Codex-like models within the sandbox
- <img src="https://avatars.githubusercontent.com/u/159934110?s=32&v=4" alt="Qwen" width="16" height="16" style="display:inline-block;width:16px;height:16px;vertical-align:middle;margin-right:4px;" /> [**qwen-code**](qwen-code): Run Qwen Code inside the sandbox
- <img src="https://www.kimi.com/favicon.ico" alt="Kimi" width="16" height="16" style="display:inline-block;width:16px;height:16px;vertical-align:middle;margin-right:4px;" /> [**kimi-cli**](kimi-cli): Call Kimi Code CLI (Moonshot AI) within the sandbox
- <img src="https://img.shields.io/badge/-%20-1C3C3C?logo=langgraph&logoColor=white&style=flat-square" alt="LangGraph" width="16" height="16" style="display:inline-block;width:16px;height:16px;vertical-align:middle;margin-right:4px;" /> [**langgraph**](langgraph): LangGraph agent orchestrating sandbox lifecycle + tools
- <img src="https://google.github.io/adk-docs/assets/agent-development-kit.png" alt="Google ADK" width="16" height="16" style="display:inline-block;width:16px;height:16px;vertical-align:middle;margin-right:4px;" /> [**google-adk**](google-adk): Google ADK agent calling OpenSandbox tools
- 🦞 [**nullclaw**](nullclaw): Launch a Nullclaw Gateway inside a sandbox
- 🦞 [**openclaw**](openclaw): Run an OpenClaw Gateway inside a sandbox
- 🖥️ [**desktop**](desktop): Launch VNC desktop (Xvfb + x11vnc) for VNC client connections
- <img src="https://playwright.dev/img/playwright-logo.svg" alt="Playwright" width="16" height="16" style="display:inline-block;width:16px;height:16px;vertical-align:middle;margin-right:4px;" /> [**playwright**](playwright): Launch headless browser (Playwright + Chromium) to scrape web content
- <img src="https://code.visualstudio.com/assets/favicon.ico" alt="VS Code" width="16" height="16" style="display:inline-block;width:16px;height:16px;vertical-align:middle;margin-right:4px;" /> [**vscode**](vscode): Launch code-server (VS Code Web) to provide browser access
- <img src="https://www.google.com/chrome/static/images/chrome-logo.svg" alt="Google Chrome" width="16" height="16" style="display:inline-block;width:16px;height:16px;vertical-align:middle;margin-right:4px;" /> [**chrome**](chrome): Launch headless Chromium with DevTools port exposed for remote debugging

## How to Run
- Set basic environment variables (e.g., `export SANDBOX_DOMAIN=...`, `export SANDBOX_API_KEY=...`)
- Add provider-specific variables as needed (e.g., `ANTHROPIC_AUTH_TOKEN`, `OPENAI_API_KEY`, `GEMINI_API_KEY`, `API_KEY` for Qwen Code, `KIMI_API_KEY`, etc.; model selection is optional)
- Navigate to the example directory and install dependencies: `pip install -r requirements.txt` (or refer to the Dockerfile in the directory)
- Then execute: `python main.py`
- To run in a container, build and run using the `Dockerfile` in the directory
- Summary: First set required environment variables via `export`, then run `python main.py` in the corresponding directory, or build/run the Docker image for that directory.

```

### File: sdks\package.json
```json
{
  "name": "opensandbox-sdks",
  "private": true,
  "packageManager": "pnpm@9.15.0",
  "scripts": {
    "build:js": "pnpm -r --filter @alibaba-group/opensandbox-code-interpreter... --sort run build",
    "test:js": "pnpm -r --filter @alibaba-group/opensandbox-code-interpreter... run test",
    "lint:js": "pnpm -r --filter @alibaba-group/opensandbox-code-interpreter... run lint",
    "typecheck:js": "pnpm -r --filter @alibaba-group/opensandbox-code-interpreter... run typecheck",
    "clean:js": "pnpm -r --filter @alibaba-group/opensandbox-code-interpreter... --sort run clean",
    "publish:js": "pnpm -r --filter @alibaba-group/opensandbox-code-interpreter... publish --access public --no-git-checks"
  },
  "devDependencies": {
    "@eslint/js": "^9.39.2",
    "eslint": "^9.39.2",
    "globals": "^17.0.0",
    "typescript": "^5.7.2",
    "typescript-eslint": "^8.52.0"
  }
}

```

### File: server\README.md
```md
# OpenSandbox Server

A production-grade, FastAPI-based service for managing the lifecycle of containerized sandboxes. It acts as the control plane to create, run, monitor, and dispose isolated execution environments across container platforms.

## Features

### Core capabilities
- **Lifecycle APIs**: Standardized REST interfaces for create, start, pause, resume, delete
- **Pluggable runtimes**:
  - **Docker**: Production-ready
  - **Kubernetes**: Production-ready (see [`../kubernetes/README.md`](../kubernetes/README.md) for deployment)
- **Lifecycle cleanup modes**: Configurable TTL with renewal, or manual cleanup with explicit delete
- **Access control**: API Key authentication (`OPEN-SANDBOX-API-KEY`); can be disabled for local/dev
- **Networking modes**:
  - Host: shared host network, performance first
  - Bridge: isolated network with built-in HTTP routing
- **Resource quotas**: CPU/memory limits with Kubernetes-style specs
- **Observability**: Unified status with transition tracking
- **Registry support**: Public and private images

### Extended capabilities
- **Async provisioning**: Background creation to reduce latency
- **Timer restoration**: Expiration timers restored after restart
- **Env/metadata injection**: Per-sandbox environment and metadata
- **Port resolution**: Dynamic endpoint generation
- **Structured errors**: Standard error codes and messages

Metadata keys under the reserved prefix `opensandbox.io/` are system-managed
and cannot be supplied by users.

## Requirements

- **Python**: 3.10 or higher
- **Package Manager**: [uv](https://github.com/astral-sh/uv) (recommended) or pip
- **Runtime Backend**:
  - Docker Engine 20.10+ (for Docker runtime)
  - Kubernetes 1.21.1+ (for Kubernetes runtime)
- **Operating System**: Linux, macOS, or Windows with WSL2

## Quick Start

### Installation

Install from PyPI. For local development, clone the repo and run `uv sync` in `server/`.

```bash
uv pip install opensandbox-server
```

### Configuration

The server reads a **TOML** file. Default path: `~/.sandbox.toml`. Override with **`SANDBOX_CONFIG_PATH`** or **`opensandbox-server --config /path/to/sandbox.toml`**.

1. Generate a starter file (see `opensandbox-server -h` for all flags):

```bash
opensandbox-server init-config ~/.sandbox.toml --example docker
# Kubernetes: --example k8s  (deploy the operator / CRDs per ../kubernetes/ first)
# Locales: docker-zh | k8s-zh  |  omit --example for a schema-only skeleton  |  add --force to overwrite
```

2. Edit the file for your environment. **Full reference:** **[configuration.md](configuration.md)** (all keys, defaults, validation, env vars).

   Topics covered there include: Docker **`network_mode`** / **`host_ip`** (e.g. server in Docker Compose), **`[egress]`** when clients send **`networkPolicy`**, **`[ingress]`**, **`[secure_runtime]`**, Kubernetes **`workload_provider`** / **`batchsandbox_template_file`**, **`[agent_sandbox]`**, TTL caps, **`[renew_intent]`**.

**Also useful:** [Secure container runtime](../docs/secure-container.md) · [Manual cleanup / optional fields](../docs/manual-cleanup-refactor-guide.md) · [Egress component](../components/egress/README.md) · [`docker-compose.example.yaml`](docker-compose.example.yaml) · [Experimental features](#experimental-features)

### Run the server

```bash
opensandbox-server
# opensandbox-server --config /path/to/sandbox.toml
```

Listens on `server.host` / `server.port` from your TOML (defaults in [configuration.md](configuration.md)).

**Health check** (adjust host/port if you changed them):

```bash
curl http://127.0.0.1:8080/health
# → {"status": "healthy"}
```

If startup, Docker/Kubernetes, or connectivity fails, see **[Troubleshooting](TROUBLESHOOTING.md)**.

## API documentation

Once the server is running, interactive API documentation is available:

- **Swagger UI**: [http://localhost:8080/docs](http://localhost:8080/docs)
- **ReDoc**: [http://localhost:8080/redoc](http://localhost:8080/redoc)

### API authentication

Authentication is enforced only when `server.api_key` is set. If the value is empty or missing, the middleware skips API Key checks (intended for local/dev). For production, always set a non-empty `server.api_key` and send it via the `OPEN-SANDBOX-API-KEY` header.

All API endpoints (except `/health`, `/docs`, `/redoc`) require authentication via the `OPEN-SANDBOX-API-KEY` header when authentication is enabled:

```bash
curl -H "OPEN-SANDBOX-API-KEY: your-secret-api-key" http://localhost:8080/v1/sandboxes
```

### Example usage

**Create a Sandbox**

```bash
curl -X POST "http://localhost:8080/v1/sandboxes" \
  -H "OPEN-SANDBOX-API-KEY: your-secret-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "image": {
      "uri": "python:3.11-slim"
    },
    "entrypoint": [
      "python",
      "-m",
      "http.server",
      "8000"
    ],
    "timeout": 3600,
    "resourceLimits": {
      "cpu": "500m",
      "memory": "512Mi"
    },
    "env": {
      "PYTHONUNBUFFERED": "1"
    },
    "metadata": {
      "team": "backend",
      "project": "api-testing"
    }
  }'
```

Response:
```json
{
  "id": "a1b2c3d4-5678-90ab-cdef-1234567890ab",
  "status": {
    "state": "Pending",
    "reason": "CONTAINER_STARTING",
    "message": "Sandbox container is starting.",
    "lastTransitionAt": "2024-01-15T10:30:00Z"
  },
  "metadata": {
    "team": "backend",
    "project": "api-testing"
  },
  "expiresAt": "2024-01-15T11:30:00Z",
  "createdAt": "2024-01-15T10:30:00Z",
  "entrypoint": ["python", "-m", "http.server", "8000"]
}
```

**Other lifecycle calls** (same `OPEN-SANDBOX-API-KEY` header): `GET /v1/sandboxes/{id}`, `GET /v1/sandboxes/{id}/endpoints/{port}` (append `?use_server_proxy=true` when needed), `POST .../renew-expiration`, `DELETE /v1/sandboxes/{id}`. Full request/response shapes: **Swagger UI** above or OpenAPI under [`specs/`](../specs/).

## Architecture

### Component responsibilities

- **API Layer** (`opensandbox_server/api/`): HTTP request handling, validation, and response formatting
- **Service Layer** (`opensandbox_server/services/`): Business logic for sandbox lifecycle operations
- **Middleware** (`opensandbox_server/middleware/`): Cross-cutting concerns (authentication, logging)
- **Configuration** (`opensandbox_server/config.py`): Centralized configuration management
- **Runtime Implementations**: Platform-specific sandbox orchestration

### Sandbox lifecycle states

```
       create()
          │
          ▼
     ┌─────────┐
     │ Pending │────────────────────┐
     └────┬────┘                    │
          │                         │
          │ (provisioning)          │
          ▼                         │
     ┌─────────┐    pause()         │
     │ Running │───────────────┐    │
     └────┬────┘               │    │
          │      resume()      │    │
          │   ┌────────────────┘    │
          │   │                     │
          │   ▼                     │
          │ ┌────────┐              │
          ├─│ Paused │              │
          │ └────────┘              │
          │                         │
          │ delete() or expire()    │
          ▼                         │
     ┌──────────┐                   │
     │ Stopping │                   │
     └────┬─────┘                   │
          │                         │
          ├────────────────┬────────┘
          │                │
          ▼                ▼
     ┌────────────┐   ┌────────┐
     │ Terminated │   │ Failed │
     └────────────┘   └────────┘
```

## Configuration reference

Single source of truth for TOML: **[configuration.md](configuration.md)** (includes `SANDBOX_CONFIG_PATH`, `DOCKER_HOST`, `PENDING_FAILURE_TTL`).

## Experimental features

Optional **🧪 experimental** behavior; **off by default** in [`example.config.toml`](example.config.toml) (and mirrored copies under `opensandbox_server/examples/`). See release notes before production.

### Auto-renew on access

Extends sandbox TTL when traffic is observed (lifecycle **proxy** and/or **ingress** + optional **Redis** queue). Design and operations: **[OSEP-0009](../oseps/0009-auto-renew-sandbox-on-ingress-access.md)**. TOML keys (`[renew_intent]`, including nested `redis.*`): see **[configuration.md](configuration.md)** and [`example.config.toml`](example.config.toml).

Per-sandbox: on **create**, set `extensions["access.renew.extend.seconds"]` (string integer **300**–**86400**). Clients using the server proxy: request endpoints with `use_server_proxy=true` (REST) or SDK `ConnectionConfig(..., use_server_proxy=True)` — details in OSEP-0009.

## Development

### Code quality

**Run linter**:
```bash
uv run ruff check
```

**Auto-fix issues**:
```bash
uv run ruff check --fix
```

**Format code**:
```bash
uv run ruff format
```

### Testing

**Run all tests**:
```bash
uv run pytest
```

**Run with coverage**:
```bash
uv run pytest --cov=opensandbox_server --cov-report=html
```

**Run specific test**:
```bash
uv run pytest tests/test_docker_service.py::test_create_sandbox_requires_entrypoint
```

## License

This project is licensed under the terms specified in the LICENSE file in the repository root.

## Contributing

Contributions are welcome. Follow the repository **[CONTRIBUTING.md](../CONTRIBUTING.md)** (Conventional Commits, PR expectations). Typical flow:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Write tests for new functionality
4. Ensure all tests pass (`uv run pytest`)
5. Run linting (`uv run ruff check`)
6. Commit with clear messages
7. Push to your fork
8. Open a Pull Request

## Support

- **Troubleshooting:** [TROUBLESHOOTING.md](TROUBLESHOOTING.md) — common failures (config, Docker, networking, K8s) and fixes
- **Development:** [DEVELOPMENT.md](DEVELOPMENT.md)
- **Issues:** Report defects via GitHub Issues
- **Discussions:** GitHub Discussions for Q&A and ideas

```

### File: specs\README.md
```md
# OpenSandbox API Specifications

English | [中文](README_zh.md)

This directory contains OpenAPI specification documents for the OpenSandbox project, defining the complete API interfaces and data models. Use the server base URLs defined in each spec (for example, `http://localhost:8080/v1` for the lifecycle API, `http://localhost:44772` for execd, and `http://localhost:18080` for egress) when constructing requests.

## Specification Files

### 1. sandbox-lifecycle.yml

**Sandbox Lifecycle Management API**

Defines the complete lifecycle interfaces for creating, managing, and destroying sandbox environments directly from container images.

**Core Features:**
- **Sandbox Management**: Create, list, query, and delete sandbox instances with metadata filters and pagination
- **State Control**: Pause and resume sandbox execution
- **Lifecycle States**: Supports transitions across Pending → Running → Pausing → Paused → Stopping → Terminated, and error handling with `Failed`
- **Resource & Runtime Configuration**: Specify CPU/memory/GPU resource limits, required `entrypoint`, environment variables, and opaque `extensions`
- **Image Support**: Create sandboxes from public or private registries, including registry auth
- **Timeout Management**: Mandatory `timeout` on creation with explicit renewal via API
- **Endpoint Access**: Retrieve public access endpoints for services running inside sandboxes

**Main Endpoints (base path `/v1`):**
- `POST /sandboxes` - Create a sandbox from an image with timeout and resource limits
- `GET /sandboxes` - List sandboxes with state/metadata filters and pagination
- `GET /sandboxes/{sandboxId}` - Get full sandbox details (including image and entrypoint)
- `DELETE /sandboxes/{sandboxId}` - Delete a sandbox
- `POST /sandboxes/{sandboxId}/pause` - Pause a sandbox (asynchronous)
- `POST /sandboxes/{sandboxId}/resume` - Resume a paused sandbox
- `POST /sandboxes/{sandboxId}/renew-expiration` - Renew sandbox expiration (TTL)
- `GET /sandboxes/{sandboxId}/endpoints/{port}` - Get an access endpoint for a service port

**Authentication:**
- HTTP Header: `OPEN-SANDBOX-API-KEY: your-api-key`
- Environment Variable: `OPEN_SANDBOX_API_KEY` (for SDK clients)

### 2. execd-api.yaml

**Code Execution API Inside Sandbox**

Defines interfaces for executing code, commands, and file operations within sandbox environments, providing complete code interpreter and filesystem management capabilities. All endpoints require the `X-EXECD-ACCESS-TOKEN` header.

**Core Features:**
- **Code Execution**: Stateful code execution supporting Python, JavaScript, and other languages with context lifecycle management
- **Command Execution**: Shell command execution with foreground/background modes and polling endpoints for status/output
- **File Operations**: Complete CRUD operations for files and directories
- **Real-time Streaming**: Real-time output streaming via SSE (Server-Sent Events)
- **System Monitoring**: Real-time monitoring of CPU and memory metrics
- **Access Control**: Token-based API authentication via `X-EXECD-ACCESS-TOKEN`

**Main Endpoint Categories:**

**Health Check:**
- `GET /ping` - Service health check

**Code Interpreter:**
- `GET /code/contexts` - List active code execution contexts (filterable by language)
- `DELETE /code/contexts` - Delete all contexts for a language
- `DELETE /code/contexts/{context_id}` - Delete a specific context
- `POST /code/context` - Create a code execution context
- `POST /code` - Execute code in a context (streaming output)
- `DELETE /code` - Interrupt code execution

**Command Execution:**
- `POST /command` - Execute shell command (streaming output)
- `DELETE /command` - Interrupt command execution
- `GET /command/status/{session}` - Get foreground/background command status
- `GET /command/output/{session}` - Fetch accumulated stdout/stderr for a command

**Filesystem:**
- `GET /files/info` - Get metadata for files
- `DELETE /files` - Delete files (not directories)
- `POST /files/permissions` - Change file permissions
- `POST /files/mv` - Move/rename files
- `GET /files/search` - Search files (supports glob patterns)
- `POST /files/replace` - Batch replace file content
- `POST /files/upload` - Upload files (multipart)
- `GET /files/download` - Download files (supports range requests)

**Directory Operations:**
- `POST /directories` - Create directories with permissions (mkdir -p semantics)
- `DELETE /directories` - Recursively delete directories

**System Metrics:**
- `GET /metrics` - Get system resource metrics
- `GET /metrics/watch` - Watch system metrics in real-time (SSE stream)

### 3. egress-api.yaml

**Sandbox Egress Runtime API**

Defines the runtime egress policy interface exposed directly by the egress sidecar
inside a sandbox. Unlike lifecycle operations, this API is reached by first resolving
the sandbox endpoint for the egress port and then calling the sidecar endpoint directly.

**Core Features:**
- **Policy Inspection**: Retrieve the currently enforced egress policy and derived runtime mode
- **Policy Mutation**: Patch egress rules at runtime using sidecar merge semantics
- **Direct Sidecar Access**: Access via sandbox endpoint resolution instead of server-side lifecycle forwarding
- **Optional Sidecar Auth**: Supports endpoint-specific headers when the egress sidecar requires auth

**Main Endpoints:**
- `GET /policy` - Get the current egress policy
- `PATCH /policy` - Merge new egress rules into the current policy

## Technical Features

### Streaming Output (Server-Sent Events)

Code execution and command execution interfaces use SSE for real-time streaming output, supporting the following event types:
- `init` - Initialization event
- `status` - Status update
- `stdout` / `stderr` - Standard output/error streams
- `result` - Execution result
- `execution_complete` - Execution completed
- `execution_count` - Execution count
- `error` - Error information

### Resource Limits

Supports flexible resource configuration (similar to Kubernetes):
```json
{
  "cpu": "500m",
  "memory": "512Mi",
  "gpu": "1"
}
```

### File Permissions

Supports Unix-style file permission management:
- Owner
- Group
- Permission mode (octal format, e.g., 755)

```

### File: examples\desktop\main.py
```py
# Copyright 2025 Alibaba Group Holding Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import asyncio
import os
from datetime import timedelta

from opensandbox import Sandbox
from opensandbox.config import ConnectionConfig
from opensandbox.models.execd import RunCommandOpts


def _required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"{name} is required")
    return value


async def _print_logs(label: str, execution) -> None:
    for msg in execution.logs.stdout:
        print(f"[{label} stdout] {msg.text}")
    for msg in execution.logs.stderr:
        print(f"[{label} stderr] {msg.text}")
    if execution.error:
        print(f"[{label} error] {execution.error.name}: {execution.error.value}")


async def main() -> None:
    domain = os.getenv("SANDBOX_DOMAIN", "localhost:8080")
    api_key = os.getenv("SANDBOX_API_KEY")
    image = os.getenv(
        "SANDBOX_IMAGE",
        "opensandbox/desktop:latest",
    )
    python_version = os.getenv("PYTHON_VERSION", "3.11")
    vnc_password = _required_env("VNC_PASSWORD")

    config = ConnectionConfig(
        domain=domain,
        api_key=api_key,
        request_timeout=timedelta(seconds=60),
    )

    sandbox = await Sandbox.create(
        image,
        connection_config=config,
        env={
            "PYTHON_VERSION": python_version,
            "VNC_PASSWORD": vnc_password,
        },
    )

    async with sandbox:
        # Desktop and VNC components are pre-installed in the image, just start them
        # Start virtual display, window manager, and VNC server (in background)
        xvfb_exec = await sandbox.commands.run(
            "Xvfb :0 -screen 0 1280x800x24",
            opts=RunCommandOpts(background=True),
        )
        await _print_logs("xvfb", xvfb_exec)

        # Start XFCE session (provides panel, file manager, terminal)
        xfce_exec = await sandbox.commands.run(
            "DISPLAY=:0 dbus-launch startxfce4",
            opts=RunCommandOpts(background=True),
        )
        await _print_logs("xfce", xfce_exec)

        vnc_exec = await sandbox.commands.run(
            "x11vnc -display :0 "
            "-passwd \"$VNC_PASSWORD\" "
            "-forever -shared -rfbport 5900",
            opts=RunCommandOpts(background=True),
        )
        await _print_logs("x11vnc", vnc_exec)

        # Start noVNC/websockify to expose VNC over WebSocket/HTTP
        novnc_exec = await sandbox.commands.run(
            "/usr/bin/websockify --web=/usr/share/novnc 6080 localhost:5900",
            opts=RunCommandOpts(background=True),
        )
        await _print_logs("novnc", novnc_exec)

        endpoint_vnc = await sandbox.get_endpoint(5900)
        endpoint_novnc = await sandbox.get_endpoint(6080)

        # Build noVNC URL with host/port/path for routed endpoint, e.g., host:port/proxy/6080
        novnc_host_port, novnc_path = endpoint_novnc.endpoint.split("/", 1)
        novnc_host, novnc_port = novnc_host_port.split(":")
        novnc_url = (
            f"http://{endpoint_novnc.endpoint}/vnc.html"
            f"?host={novnc_host}&port={novnc_port}&path={novnc_path}"
        )

        print("\nVNC endpoint (native clients):")
        print(f"  {endpoint_vnc.endpoint}")
        print(f"Password: {vnc_password}")

        print("\nnoVNC (browser):")
        print(f"  {novnc_url}")
        print(f"Password: {vnc_password}")

        print("\nKeeping sandbox alive for 5 minutes. Press Ctrl+C to exit sooner.")
        try:
            await asyncio.sleep(300)
        except KeyboardInterrupt:
            print("Stopping...")
        finally:
            await sandbox.kill()


if __name__ == "__main__":
    asyncio.run(main())

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
