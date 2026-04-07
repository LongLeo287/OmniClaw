---
id: qwen
type: knowledge
owner: OA_Triage
---
# qwen
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "@qwen-code/qwen-code",
  "version": "0.14.1",
  "engines": {
    "node": ">=20.0.0"
  },
  "type": "module",
  "workspaces": [
    "packages/*",
    "packages/channels/base",
    "packages/channels/telegram",
    "packages/channels/weixin",
    "packages/channels/dingtalk",
    "packages/channels/plugin-example"
  ],
  "repository": {
    "type": "git",
    "url": "git+https://github.com/QwenLM/qwen-code.git"
  },
  "config": {
    "sandboxImageUri": "ghcr.io/qwenlm/qwen-code:0.14.1"
  },
  "scripts": {
    "start": "cross-env node scripts/start.js",
    "dev": "node scripts/dev.js",
    "debug": "cross-env DEBUG=1 node --inspect-brk scripts/start.js",
    "generate": "node scripts/generate-git-commit-info.js",
    "generate:settings-schema": "tsx scripts/generate-settings-schema.ts",
    "build": "node scripts/build.js",
    "build-and-start": "npm run build && npm run start",
    "build:vscode": "node scripts/build_vscode_companion.js",
    "build:all": "npm run build && npm run build:sandbox && npm run build:vscode",
    "build:packages": "npm run build --workspaces",
    "build:sandbox": "node scripts/build_sandbox.js",
    "bundle": "npm run generate && node esbuild.config.js && node scripts/copy_bundle_assets.js",
    "test": "npm run test --workspaces --if-present --parallel",
    "test:ci": "npm run test:ci --workspaces --if-present --parallel && npm run test:scripts",
    "test:scripts": "vitest run --config ./scripts/tests/vitest.config.ts",
    "test:e2e": "cross-env VERBOSE=true KEEP_OUTPUT=true npm run test:integration:sandbox:none",
    "test:integration:all": "npm run test:integration:sandbox:none && npm run test:integration:sandbox:docker && npm run test:integration:sandbox:podman",
    "test:integration:sandbox:none": "cross-env QWEN_SANDBOX=false vitest run --root ./integration-tests",
    "test:integration:sandbox:docker": "cross-env QWEN_SANDBOX=docker npm run build:sandbox && QWEN_SANDBOX=docker vitest run --root ./integration-tests",
    "test:integration:sandbox:podman": "cross-env QWEN_SANDBOX=podman vitest run --root ./integration-tests",
    "test:integration:sdk:sandbox:none": "cross-env QWEN_SANDBOX=false vitest run --root ./integration-tests --poolOptions.threads.maxThreads 2 sdk-typescript",
    "test:integration:sdk:sandbox:docker": "cross-env QWEN_SANDBOX=docker npm run build:sandbox && QWEN_SANDBOX=docker vitest run --root ./integration-tests --poolOptions.threads.maxThreads 2 sdk-typescript",
    "test:integration:cli:sandbox:none": "cross-env QWEN_SANDBOX=false vitest run --root ./integration-tests cli",
    "test:integration:cli:sandbox:docker": "cross-env QWEN_SANDBOX=docker npm run build:sandbox && QWEN_SANDBOX=docker vitest run --root ./integration-tests cli",
    "test:integration:interactive:sandbox:none": "cross-env QWEN_SANDBOX=false vitest run --root ./integration-tests interactive",
    "test:integration:interactive:sandbox:docker": "cross-env QWEN_SANDBOX=docker npm run build:sandbox && QWEN_SANDBOX=docker vitest run --root ./integration-tests interactive",
    "test:terminal-bench": "cross-env VERBOSE=true KEEP_OUTPUT=true vitest run --config ./vitest.terminal-bench.config.ts --root ./integration-tests",
    "test:terminal-bench:oracle": "cross-env VERBOSE=true KEEP_OUTPUT=true vitest run --config ./vitest.terminal-bench.config.ts --root ./integration-tests -t 'oracle'",
    "test:terminal-bench:qwen": "cross-env VERBOSE=true KEEP_OUTPUT=true vitest run --config ./vitest.terminal-bench.config.ts --root ./integration-tests -t 'qwen'",
    "lint": "eslint . --ext .ts,.tsx && eslint integration-tests",
    "lint:fix": "eslint . --fix && eslint integration-tests --fix",
    "lint:ci": "eslint . --ext .ts,.tsx --max-warnings 0 && eslint integration-tests --max-warnings 0",
    "lint:all": "node scripts/lint.js",
    "format": "prettier --experimental-cli --write .",
    "typecheck": "npm run typecheck --workspaces --if-present",
    "check-i18n": "npm run check-i18n --workspace=packages/cli",
    "preflight": "npm run clean && npm ci && npm run format && npm run lint:ci && npm run build && npm run typecheck && npm run test:ci",
    "prepare": "husky && npm run build && npm run bundle",
    "prepare:package": "node scripts/prepare-package.js",
    "release:version": "node scripts/version.js",
    "telemetry": "node scripts/telemetry.js",
    "check:lockfile": "node scripts/check-lockfile.js",
    "clean": "node scripts/clean.js",
    "pre-commit": "node scripts/pre-commit.js"
  },
  "overrides": {
    "wrap-ansi": "9.0.2",
    "ansi-regex": "6.2.2",
    "cliui": {
      "wrap-ansi": "7.0.0"
    },
    "baseline-browser-mapping": "^2.9.19"
  },
  "bin": {
    "qwen": "dist/cli.js"
  },
  "files": [
    "dist/",
    "README.md",
    "LICENSE"
  ],
  "devDependencies": {
    "@types/marked": "^5.0.2",
    "@types/mime-types": "^3.0.1",
    "@types/minimatch": "^5.1.2",
    "@types/mock-fs": "^4.13.4",
    "@types/shell-quote": "^1.7.5",
    "@types/uuid": "^10.0.0",
    "@vitest/coverage-v8": "^3.1.1",
    "@vitest/eslint-plugin": "^1.3.4",
    "@xterm/headless": "^5.5.0",
    "@xterm/xterm": "^6.0.0",
    "cross-env": "^7.0.3",
    "esbuild": "^0.25.0",
    "eslint": "^9.24.0",
    "eslint-config-prettier": "^10.1.2",
    "eslint-plugin-import": "^2.31.0",
    "eslint-plugin-license-header": "^0.8.0",
    "eslint-plugin-react": "^7.37.5",
    "eslint-plugin-react-hooks": "^5.2.0",
    "glob": "^10.5.0",
    "globals": "^16.0.0",
    "husky": "^9.1.7",
    "json": "^11.0.0",
    "lint-staged": "^16.1.6",
    "memfs": "^4.42.0",
    "mnemonist": "^0.40.3",
    "mock-fs": "^5.5.0",
    "msw": "^2.10.4",
    "npm-run-all": "^4.1.5",
    "prettier": "^3.5.3",
    "react-devtools-core": "^4.28.5",
    "semver": "^7.7.2",
    "strip-ansi": "^7.1.2",
    "tsx": "^4.20.3",
    "typescript-eslint": "^8.30.1",
    "vitest": "^3.2.4",
    "yargs": "^17.7.2"
  },
  "dependencies": {
    "@testing-library/dom": "^10.4.1",
    "simple-git": "^3.28.0"
  },
  "optionalDependencies": {
    "@lydell/node-pty": "1.2.0-beta.10",
    "@lydell/node-pty-darwin-arm64": "1.2.0-beta.10",
    "@lydell/node-pty-darwin-x64": "1.2.0-beta.10",
    "@lydell/node-pty-linux-x64": "1.2.0-beta.10",
    "@lydell/node-pty-win32-arm64": "1.2.0-beta.10",
    "@lydell/node-pty-win32-x64": "1.2.0-beta.10"
  },
  "lint-staged": {
    "*.{js,jsx,ts,tsx}": [
      "prettier --write",
      "eslint --fix --max-warnings 0"
    ],
    "*.{json,md}": [
      "prettier --write"
    ]
  }
}

```

### File: README.md
```md
<div align="center">

[![npm version](https://img.shields.io/npm/v/@qwen-code/qwen-code.svg)](https://www.npmjs.com/package/@qwen-code/qwen-code)
[![License](https://img.shields.io/github/license/QwenLM/qwen-code.svg)](./LICENSE)
[![Node.js Version](https://img.shields.io/badge/node-%3E%3D20.0.0-brightgreen.svg)](https://nodejs.org/)
[![Downloads](https://img.shields.io/npm/dm/@qwen-code/qwen-code.svg)](https://www.npmjs.com/package/@qwen-code/qwen-code)

<a href="https://trendshift.io/repositories/15287" target="_blank"><img src="https://trendshift.io/api/badge/repositories/15287" alt="QwenLM%2Fqwen-code | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

**An open-source AI agent that lives in your terminal.**

<a href="https://qwenlm.github.io/qwen-code-docs/zh/users/overview">中文</a> |
<a href="https://qwenlm.github.io/qwen-code-docs/de/users/overview">Deutsch</a> |
<a href="https://qwenlm.github.io/qwen-code-docs/fr/users/overview">français</a> |
<a href="https://qwenlm.github.io/qwen-code-docs/ja/users/overview">日本語</a> |
<a href="https://qwenlm.github.io/qwen-code-docs/ru/users/overview">Русский</a> |
<a href="https://qwenlm.github.io/qwen-code-docs/pt-BR/users/overview">Português (Brasil)</a>

</div>

## 🎉 News

- **2026-04-02**: Qwen3.6-Plus is now live! Sign in via Qwen OAuth to use it directly, or get an API key from [Alibaba Cloud ModelStudio](https://modelstudio.console.alibabacloud.com/ap-southeast-1?tab=doc#/doc/?type=model&url=2840914_2&modelId=qwen3.6-plus) to access it through the OpenAI-compatible API.

- **2026-02-16**: Qwen3.5-Plus is now live!

## Why Qwen Code?

Qwen Code is an open-source AI agent for the terminal, optimized for Qwen series models. It helps you understand large codebases, automate tedious work, and ship faster.

- **Multi-protocol, OAuth free tier**: use OpenAI / Anthropic / Gemini-compatible APIs, or sign in with Qwen OAuth for 1,000 free requests/day.
- **Open-source, co-evolving**: both the framework and the Qwen3-Coder model are open-source—and they ship and evolve together.
- **Agentic workflow, feature-rich**: rich built-in tools (Skills, SubAgents) for a full agentic workflow and a Claude Code-like experience.
- **Terminal-first, IDE-friendly**: built for developers who live in the command line, with optional integration for VS Code, Zed, and JetBrains IDEs.

![](https://gw.alicdn.com/imgextra/i1/O1CN01D2DviS1wwtEtMwIzJ_!!6000000006373-2-tps-1600-900.png)

## Installation

### Quick Install (Recommended)

#### Linux / macOS

```bash
bash -c "$(curl -fsSL https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen.sh)"
```

#### Windows (Run as Administrator CMD)

```cmd
curl -fsSL -o %TEMP%\install-qwen.bat https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen.bat && %TEMP%\install-qwen.bat
```

> **Note**: It's recommended to restart your terminal after installation to ensure environment variables take effect.

### Manual Installation

#### Prerequisites

Make sure you have Node.js 20 or later installed. Download it from [nodejs.org](https://nodejs.org/en/download).

#### NPM

```bash
npm install -g @qwen-code/qwen-code@latest
```

#### Homebrew (macOS, Linux)

```bash
brew install qwen-code
```

## Quick Start

```bash
# Start Qwen Code (interactive)
qwen

# Then, in the session:
/help
/auth
```

On first use, you'll be prompted to sign in. You can run `/auth` anytime to switch authentication methods.

Example prompts:

```text
What does this project do?
Explain the codebase structure.
Help me refactor this function.
Generate unit tests for this module.
```

<details>
<summary>Click to watch a demo video</summary>

<video src="https://cloud.video.taobao.com/vod/HLfyppnCHplRV9Qhz2xSqeazHeRzYtG-EYJnHAqtzkQ.mp4" controls>
Your browser does not support the video tag.
</video>

</details>

## 🦞 Use Qwen Code for Coding Tasks in Claw

Copy the prompt below and paste it into your agent:

```
Use Qwen Code as a coding agent. First, fetch and read this skill reference:
https://raw.githubusercontent.com/QwenLM/qwen-code/refs/heads/main/.qwen/skills/qwen-code-claw/SKILL.md
Then follow the instructions inside to install, authenticate, and use Qwen Code via acpx for all coding tasks.
```

## Authentication

Qwen Code supports two authentication methods:

- **Qwen OAuth (recommended & free)**: sign in with your `qwen.ai` account in a browser.
- **API-KEY**: use an API key to connect to any supported provider (OpenAI, Anthropic, Google GenAI, Alibaba Cloud ModelStudio, and other compatible endpoints).

#### Qwen OAuth (recommended)

Start `qwen`, then run:

```bash
/auth
```

Choose **Qwen OAuth** and complete the browser flow. Your credentials are cached locally so you usually won't need to log in again.

> **Note:** In non-interactive or headless environments (e.g., CI, SSH, containers), you typically **cannot** complete the OAuth browser login flow. In these cases, please use the API-KEY authentication method.

#### API-KEY (flexible)

Use this if you want more flexibility over which provider and model to use. Supports multiple protocols:

- **OpenAI-compatible**: Alibaba Cloud ModelStudio, ModelScope, OpenAI, OpenRouter, and other OpenAI-compatible providers
- **Anthropic**: Claude models
- **Google GenAI**: Gemini models

The **recommended** way to configure models and providers is by editing `~/.qwen/settings.json` (create it if it doesn't exist). This file lets you define all available models, API keys, and default settings in one place.

##### Quick Setup in 3 Steps

**Step 1:** Create or edit `~/.qwen/settings.json`

Here is a complete example:

```json
{
  "modelProviders": {
    "openai": [
      {
        "id": "qwen3.6-plus",
        "name": "qwen3.6-plus",
        "baseUrl": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "description": "Qwen3-Coder via Dashscope",
        "envKey": "DASHSCOPE_API_KEY"
      }
    ]
  },
  "env": {
    "DASHSCOPE_API_KEY": "sk-xxxxxxxxxxxxx"
  },
  "security": {
    "auth": {
      "selectedType": "openai"
    }
  },
  "model": {
    "name": "qwen3.6-plus"
  }
}
```

**Step 2:** Understand each field

| Field                        | What it does                                                                                                                          |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `modelProviders`             | Declares which models are available and how to connect to them. Keys like `openai`, `anthropic`, `gemini` represent the API protocol. |
| `modelProviders[].id`        | The model ID sent to the API (e.g. `qwen3.6-plus`, `gpt-4o`).                                                                         |
| `modelProviders[].envKey`    | The name of the environment variable that holds your API key.                                                                         |
| `modelProviders[].baseUrl`   | The API endpoint URL (required for non-default endpoints).                                                                            |
| `env`                        | A fallback place to store API keys (lowest priority; prefer `.env` files or `export` for sensitive keys).                             |
| `security.auth.selectedType` | The protocol to use on startup (`openai`, `anthropic`, `gemini`, `vertex-ai`).                                                        |
| `model.name`                 | The default model to use when Qwen Code starts.                                                                                       |

**Step 3:** Start Qwen Code — your configuration takes effect automatically:

```bash
qwen
```

Use the `/model` command at any time to switch between all configured models.

##### More Examples

<details>
<summary>Coding Plan (Alibaba Cloud ModelStudio) — fixed monthly fee, higher quotas</summary>

```json
{
  "modelProviders": {
    "openai": [
      {
        "id": "qwen3.6-plus",
        "name": "qwen3.6-plus (Coding Plan)",
        "baseUrl": "https://coding.dashscope.aliyuncs.com/v1",
        "description": "qwen3.6-plus from ModelStudio Coding Plan",
        "envKey": "BAILIAN_CODING_PLAN_API_KEY"
      },
      {
        "id": "qwen3.5-plus",
        "name": "qwen3.5-plus (Coding Plan)",
        "baseUrl": "https://coding.dashscope.aliyuncs.com/v1",
        "description": "qwen3.5-plus with thinking enabled from ModelStudio Coding Plan",
        "envKey": "BAILIAN_CODING_PLAN_API_KEY",
        "generationConfig": {
          "extra_body": {
            "enable_thinking": true
          }
        }
      },
      {
        "id": "glm-4.7",
        "name": "glm-4.7 (Coding Plan)",
        "baseUrl": "https://coding.dashscope.aliyuncs.com/v1",
        "description": "glm-4.7 with thinking enabled from ModelStudio Coding Plan",
        "envKey": "BAILIAN_CODING_PLAN_API_KEY",
        "generationConfig": {
          "extra_body": {
            "enable_thinking": true
          }
        }
      },
      {
        "id": "kimi-k2.5",
        "name": "kimi-k2.5 (Coding Plan)",
        "baseUrl": "https://coding.dashscope.aliyuncs.com/v1",
        "description": "kimi-k2.5 with thinking enabled from ModelStudio Coding Plan",
        "envKey": "BAILIAN_CODING_PLAN_API_KEY",
        "generationConfig": {
          "extra_body": {
            "enable_thinking": true
          }
        }
      }
    ]
  },
  "env": {
    "BAILIAN_CODING_PLAN_API_KEY": "sk-xxxxxxxxxxxxx"
  },
  "security": {
    "auth": {
      "selectedType": "openai"
    }
  },
  "model": {
    "name": "qwen3.6-plus"
  }
}
```

> Subscribe to the Coding Plan and get your API key at [Alibaba Cloud ModelStudio(Beijing)](https://bailian.console.aliyun.com/cn-beijing?tab=coding-plan#/efm/coding-plan-index) or [Alibaba Cloud ModelStudio(intl)](https://modelstudio.console.alibabacloud.com/?tab=coding-plan#/efm/coding-plan-index).

</details>

<details>
<summary>Multiple providers (OpenAI + Anthropic + Gemini)</summary>

```json
{
  "modelProviders": {
    "openai": [
      {
        "id": "gpt-4o",
        "name": "GPT-4o",
        "envKey": "OPENAI_API_KEY",
        "baseUrl": "https://api.openai.com/v1"
      }
    ],
    "anthropic": [
      {
        "id": "claude-sonnet-4-20250514",
        "name": "Claude Sonnet 4",
        "envKey": "ANTHROPIC_API_KEY"
      }
    ],
    "gemini": [
      {
        "id": "gemini-2.5-pro",
        "name": "Gemini 2.5 Pro",
        "envKey": "GEMINI_API_KEY"
      }
    ]
  },
  "env": {
    "OPENAI_API_KEY": "sk-xxxxxxxxxxxxx",
    "ANTHROPIC_API_KEY": "sk-ant-xxxxxxxxxxxxx",
    "GEMINI_API_KEY": "AIzaxxxxxxxxxxxxx"
  },
  "security": {
    "auth": {
      "selectedType": "openai"
    }
  },
  "model": {
    "name": "gpt-4o"
  }
}
```

</details>

<details>
<summary>Enable thinking mode (for supported models like qwen3.5-plus)</summary>

```json
{
  "modelProviders": {
    "openai": [
      {
        "id": "qwen3.5-plus",
        "name": "qwen3.5-plus (thinking)",
        "envKey": "DASHSCOPE_API_KEY",
        "baseUrl": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "generationConfig": {
          "extra_body": {
            "enable_thinking": true
          }
        }
      }
    ]
  },
  "env": {
    "DASHSCOPE_API_KEY": "sk-xxxxxxxxxxxxx"
  },
  "security": {
    "auth": {
      "selectedType": "openai"
    }
  },
  "model": {
    "name": "qwen3.5-plus"
  }
}
```

</details>

> **Tip:** You can also set API keys via `export` in your shell or `.env` files, which take higher priority than `settings.json` → `env`. See the [authentication guide](https://qwenlm.github.io/qwen-code-docs/en/users/configuration/auth/) for full details.

> **Security note:** Never commit API keys to version control. The `~/.qwen/settings.json` file is in your home directory and should stay private.

## Usage

As an open-source terminal agent, you can use Qwen Code in four primary ways:

1. Interactive mode (terminal UI)
2. Headless mode (scripts, CI)
3. IDE integration (VS Code, Zed)
4. TypeScript SDK

#### Interactive mode

```bash
cd your-project/
qwen
```

Run `qwen` in your project folder to launch the interactive terminal UI. Use `@` to reference local files (for example `@src/main.ts`).

#### Headless mode

```bash
cd your-project/
qwen -p "your question"
```

Use `-p` to run Qwen Code without the interactive UI—ideal for scripts, automation, and CI/CD. Learn more: [Headless mode](https://qwenlm.github.io/qwen-code-docs/en/users/features/headless).

#### IDE integration

Use Qwen Code inside your editor (VS Code, Zed, and JetBrains IDEs):

- [Use in VS Code](https://qwenlm.github.io/qwen-code-docs/en/users/integration-vscode/)
- [Use in Zed](https://qwenlm.github.io/qwen-code-docs/en/users/integration-zed/)
- [Use in JetBrains IDEs](https://qwenlm.github.io/qwen-code-docs/en/users/integration-jetbrains/)

#### TypeScript SDK

Build on top of Qwen Code with the TypeScript SDK:

- [Use the Qwen Code SDK](./packages/sdk-typescript/README.md)

## Commands & Shortcuts

### Session Commands

- `/help` - Display available commands
- `/clear` - Clear conversation history
- `/compress` - Compress history to save tokens
- `/stats` - Show current session information
- `/bug` - Submit a bug report
- `/exit` or `/quit` - Exit Qwen Code

### Keyboard Shortcuts

- `Ctrl+C` - Cancel current operation
- `Ctrl+D` - Exit (on empty line)
- `Up/Down` - Navigate command history

> Learn more about [Commands](https://qwenlm.github.io/qwen-code-docs/en/users/features/commands/)
>
> **Tip**: In YOLO mode (`--yolo`), vision switching happens automatically without prompts when images are detected. Learn more about [Approval Mode](https://qwenlm.github.io/qwen-code-docs/en/users/features/approval-mode/)

## Configuration

Qwen Code can be configured via `settings.json`, environment variables, and CLI flags.

| File                    | Scope         | Description                                                                             |
| ----------------------- | ------------- | --------------------------------------------------------------------------------------- |
| `~/.qwen/settings.json` | User (global) | Applies to all your Qwen Code sessions. **Recommended for `modelProviders` and `env`.** |
| `.qwen/settings.json`   | Project       | Applies only when running Qwen Code in this project. Overrides user settings.           |

The most commonly used top-level fields in `settings.json`:

| Field                        | Description                                                                                          |
| ---------------------------- | ---------------------------------------------------------------------------------------------------- |
| `modelProviders`             | Define available models per protocol (`openai`, `anthropic`, `gemini`, `vertex-ai`).         
... [TRUNCATED]
```

### File: requirements.txt
```txt
transformers>=4.32.0,<4.38.0
accelerate
tiktoken
einops
transformers_stream_generator==0.0.4
scipy

```

### File: setup.py
```py
# Copyright 2023 The Qwen team, Alibaba Group. All rights reserved.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re

from setuptools import find_packages, setup


def get_version() -> str:
    with open('qwen_agent/__init__.py', encoding='utf-8') as f:
        version = re.search(
            r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
            f.read(),
            re.MULTILINE,
        ).group(1)
    return version


def read_description() -> str:
    with open('README.md', 'r', encoding='UTF-8') as f:
        long_description = f.read()
    return long_description


# To update the package at PyPI:
# ```bash
# python setup.py sdist bdist_wheel
# twine upload dist/*
# ```
setup(
    name='qwen-agent',
    version=get_version(),
    author='Qwen Team',
    author_email='tujianhong.tjh@alibaba-inc.com',
    description='Qwen-Agent: Enhancing LLMs with Agent Workflows, RAG, Function Calling, and Code Interpreter.',
    long_description=read_description(),
    long_description_content_type='text/markdown',
    keywords=['LLM', 'Agent', 'Function Calling', 'RAG', 'Code Interpreter'],
    packages=find_packages(exclude=['examples', 'examples.*', 'qwen_server', 'qwen_server.*']),
    package_data={
        'qwen_agent': [
            'utils/qwen.tiktoken', 'tools/resource/*.ttf', 'tools/resource/*.py', 'gui/assets/*.css',
            'gui/assets/*.jpeg'
        ],
    },

    # Minimal dependencies for Function Calling:
    install_requires=[
        'dashscope>=1.11.0',
        'eval_type_backport',
        'json5',
        'jsonlines',
        'jsonschema',
        'openai',
        'pydantic>=2.3.0',
        'requests',
        'tiktoken',
        'pillow',
        'dotenv',
    ],
    extras_require={
        # Extra dependencies for RAG:
        'rag': [
            'charset-normalizer',
            'rank_bm25',
            'jieba',
            'snowballstemmer',
            'beautifulsoup4',
            'pdfminer.six',
            'pdfplumber',
            'python-docx',
            'python-pptx',
            'pandas',
            'tabulate',
        ],

        # Extra dependencies for MCP:
        'mcp': ['mcp'],

        # Extra dependencies for Python Executor, which is primarily for solving math problems:
        'python_executor': [
            'pebble',
            'multiprocess',
            'timeout_decorator',
            'python-dateutil',
            'sympy',
            'numpy',
            'scipy',
        ],

        # Extra dependencies for Code Interpreter:
        'code_interpreter': [
            'anyio>=3.7.1',
            'fastapi>=0.103.1',
            'jupyter>=1.0.0',
            'uvicorn>=0.23.2',
        ],

        # Extra dependencies for Gradio-based GUI:
        'gui': [
            # Gradio has bad version compatibility. Therefore, we use `==` instead of `>=`.
            'pydantic==2.9.2',
            'pydantic-core==2.23.4',
            'gradio==5.23.1',
            'gradio-client==1.8.0',
            'modelscope_studio==1.1.7',
        ],
    },
    url='https://github.com/QwenLM/Qwen-Agent',
)

```

### File: benchmark\code_interpreter\README.md
```md
# Code Interpreter Benchmark

## Introduction
To assess LLM's ability to use the Python Code Interpreter for tasks such as mathematical problem solving, data visualization, and other general-purpose tasks such as file handling and web scraping, we have created and open-sourced a benchmark specifically designed for evaluating these capabilities.

### Metrics
The metrics are divided into two parts: code executability and code correctness.
- Code executability: evaluating the ability of the LLM-generated code to be executed.
- Code correctness: evaluating whether the LLM-generated code runs correctly.

### Domain
When evaluating the accuracy of the code execution results for code correctness, we further divide it into two specific domains: `Math`, `Visualization`.
In terms of code executability, we calculate executable rate of the generated code for `General problem-solving`.

## Results
- Qwen-7B-Chat refers to the version updated after September 25, 2023.
- The code correctness judger model for `Visualization` has changed from `Qwen-vl-chat` to `gpt-4-vision-preview` in the version 20231206.

<table>
    <tr>
        <th colspan="5" align="center">In-house Code Interpreter Benchmark (Version 20231206)</th>
    </tr>
    <tr>
        <th rowspan="2" align="center">Model</th>
        <th colspan="3" align="center">Accuracy of Code Execution Results (%)</th>
        <th colspan="1" align="center">Executable Rate of Code (%)</th>
    </tr>
    <tr>
        <th align="center">Math↑</th><th align="center">Visualization-Hard↑</th><th align="center">Visualization-Easy↑</th><th align="center">General↑</th>
    </tr>
    <tr>
        <td>GPT-4</td>
        <td align="center">82.8</td>
        <td align="center">66.7</td>
        <td align="center">60.8</td>
        <td align="center">82.8</td>
    </tr>
    <tr>
        <td>GPT-3.5</td>
        <td align="center">47.3</td>
        <td align="center">33.3</td>
        <td align="center">55.7</td>
        <td align="center">74.1</td>
    </tr>
    <tr>
        <td>LLaMA2-13B-Chat</td>
        <td align="center">8.3</td>
        <td align="center">1.2</td>
        <td align="center">15.2</td>
        <td align="center">48.3</td>
    </tr>
    <tr>
        <td>CodeLLaMA-13B-Instruct</td>
        <td align="center">28.2</td>
        <td align="center">15.5</td>
        <td align="center">21.5</td>
        <td align="center">74.1</td>
    </tr>
    <tr>
        <td>InternLM-20B-Chat</td>
        <td align="center">34.6</td>
        <td align="center">10.7</td>
        <td align="center">24.1</td>
        <td align="center">65.5</td>
    </tr>
    <tr>
        <td>ChatGLM3-6B</td>
        <td align="center">54.2</td>
        <td align="center">4.8</td>
        <td align="center">15.2</td>
        <td align="center">62.1</td>
    </tr>
    <tr>
        <td>Qwen-1.8B-Chat</td>
        <td align="center">25.6</td>
        <td align="center">21.4</td>
        <td align="center">22.8</td>
        <td align="center">65.5</td>
    </tr>
    <tr>
        <td>Qwen-7B-Chat</td>
        <td align="center">41.9</td>
        <td align="center">23.8</td>
        <td align="center">38.0</td>
        <td align="center">67.2</td>
    </tr>
    <tr>
        <td>Qwen-14B-Chat</td>
        <td align="center">58.4</td>
        <td align="center">31.0</td>
        <td align="center">45.6</td>
        <td align="center">65.5</td>
    </tr>
    <tr>
        <td>Qwen-72B-Chat</td>
        <td align="center">72.7</td>
        <td align="center">41.7</td>
        <td align="center">43.0</td>
        <td align="center">82.8</td>
    </tr>
</table>

Furthermore, we also provide the results of `Qwen-vl-plus` as the code correctness judger model for `Visualization` task to serve as a reference.

<table>
    <tr>
        <th colspan="3" align="center">Code Correctness Judger Model = Qwen-vl-plus</th>
    </tr>
    <tr>
        <th rowspan="2" align="center">Model</th>
        <th colspan="2" align="center">Accuracy of Code Execution Results (%)</th>
    </tr>
    <tr>
        <th align="center">Visualization-Hard↑</th>
        <th align="center">Visualization-Easy↑</th>
    </tr>
    <tr>
        <td>LLaMA2-13B-Chat</td>
        <td align="center">2.4</td>
        <td align="center">17.7</td>
    </tr>
    <tr>
        <td>CodeLLaMA-13B-Instruct</td>
        <td align="center">17.9</td>
        <td align="center">34.2</td>
    </tr>
    <tr>
        <td>InternLM-20B-Chat</td>
        <td align="center">9.5</td>
        <td align="center">31.7</td>
    </tr>
    <tr>
        <td>ChatGLM3-6B</td>
        <td align="center">10.7</td>
        <td align="center">29.1</td>
    </tr>
    <tr>
        <td>Qwen-1.8B-Chat</td>
        <td align="center">32.1</td>
        <td align="center">32.9</td>
    </tr>
    <tr>
        <td>Qwen-7B-Chat</td>
        <td align="center">26.2</td>
        <td align="center">39.2</td>
    </tr>
    <tr>
        <td>Qwen-14B-Chat</td>
        <td align="center">36.9</td>
        <td align="center">41.8</td>
    </tr>
    <tr>
        <td>Qwen-72B-Chat</td>
        <td align="center">38.1</td>
        <td align="center">38.0</td>
    </tr>
</table>



## Usage

### Installation

```shell
git clone https://github.com/QwenLM/Qwen-Agent.git
cd benchmark
pip install -r requirements.txt
```

### Dataset Download
```shell
cd benchmark
wget https://qianwen-res.oss-cn-beijing.aliyuncs.com/assets/qwen_agent/benchmark_code_interpreter_data.zip
unzip benchmark_code_interpreter_data.zip
mkdir eval_data
mv eval_code_interpreter_v1.jsonl eval_data/
```

### Evaluation
To reproduce the comprehensive results of benchmark, you can run the following script:

```Shell
python inference_and_execute.py --model {model_name}
```

{model_name}:
- qwen-1.8b-chat
- qwen-7b-chat
- qwen-14b-chat
- qwen-72b-chat
- llama-2-7b-chat
- llama-2-13b-chat
- codellama-7b-instruct
- codellama-13b-instruct
- internlm-7b-chat-1.1
- internlm-20b-chat

The benchmark will run the test cases and generate the performance results. The results will be saved in the `output_data` directory.

**Notes**:
Please install `simhei.ttf` font for proper display in matplotlib when evaluating visualization task. You can do this by preparing `simhei.ttf` (which can be found on any Windows PC) and then running the following code snippet:
```python
import os
import matplotlib
target_font_path = os.path.join(
    os.path.abspath(
        os.path.join(matplotlib.matplotlib_fname(), os.path.pardir)),
        'fonts', 'ttf', 'simhei.ttf')
os.system(f'cp simhei.ttf {target_font_path}')
font_list_cache = os.path.join(matplotlib.get_cachedir(), 'fontlist-*.json')
os.system(f'rm -f {font_list_cache}')
```

#### Code Executable Rate
```Shell
python inference_and_execute.py --task {task_name} --model {model_name}
```

{task_name}:
- `general`: General problem-solving task


#### Code Correctness Rate
```Shell
python inference_and_execute.py --task {task_name} --model {model_name}
```

{task_name}:
- `visualization`: Visualization task
- `gsm8k`: Math task


## Configuration
The inference_and_exec.py file contains the following configurable options:

- `--model`: The model to test which can be one of `qwen-72b-chat`, `qwen-14b-chat`, `qwen-7b-chat`, `qwen-1.8b-chat`, `qwen-7b-chat`, `llama-2-7b-chat`, `llama-2-13b-chat`, `codellama-7b-instruct`, `codellama-13b-instruct`, `internlm-7b-chat-1.1`, `internlm-20b-chat`.
- `--task`: The test task which can be one of `all`, `visualization`, `general`, `gsm8k`.
- `--output-path`: The path for saving evaluation result.
- `--input-path`: The path for placing evaluation data.
- `--output-fname`: The file name for evaluation result.
- `--input-fname`: The file name for evaluation data.
- `--force`: Force generation and will overwrite the cached results.
- `--eval-only`: Only calculate evaluation metrics without re-inference.
- `--eval-code-exec-only`: Only evaluate code executable rate
- `--gen-exec-only`: Only generate and execuate code without calculating evaluation metrics.
- `--gen-only`: Only generate without execuating code and calculating evaluation metrics.
- `--vis-judger`: The model to judge the result correctness for `Visualization` task which can be one of `gpt-4-vision-preview`, `qwen-vl-chat`, `qwen-vl-plus`. It is set to `gpt-4-vision-preview` by default in the version 20231206, and `Qwen-vl-chat` has been deprecated.

```

### File: benchmark\code_interpreter\requirements.txt
```txt
accelerate>=0.20.3
func_timeout
json5
matplotlib
numpy
openai
pandas
PrettyTable
scipy
seaborn
sympy
transformers==4.33.1
transformers_stream_generator

```

### File: packages\cli\package.json
```json
{
  "name": "@qwen-code/qwen-code",
  "version": "0.14.1",
  "description": "Qwen Code",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/QwenLM/qwen-code.git"
  },
  "type": "module",
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "bin": {
    "qwen": "dist/index.js"
  },
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js"
    }
  },
  "scripts": {
    "build": "node ../../scripts/build_package.js",
    "start": "node dist/index.js",
    "debug": "node --inspect-brk dist/index.js",
    "lint": "eslint . --ext .ts,.tsx",
    "format": "prettier --write .",
    "test": "vitest run",
    "test:ci": "vitest run",
    "typecheck": "tsc --noEmit",
    "check-i18n": "tsx ../../scripts/check-i18n.ts"
  },
  "files": [
    "dist"
  ],
  "config": {
    "sandboxImageUri": "ghcr.io/qwenlm/qwen-code:0.14.1"
  },
  "dependencies": {
    "@agentclientprotocol/sdk": "^0.14.1",
    "@google/genai": "1.30.0",
    "@iarna/toml": "^2.2.5",
    "@modelcontextprotocol/sdk": "^1.25.1",
    "@qwen-code/channel-base": "file:../channels/base",
    "@qwen-code/channel-telegram": "file:../channels/telegram",
    "@qwen-code/channel-weixin": "file:../channels/weixin",
    "@qwen-code/channel-dingtalk": "file:../channels/dingtalk",
    "@qwen-code/qwen-code-core": "file:../core",
    "@qwen-code/web-templates": "file:../web-templates",
    "@types/update-notifier": "^6.0.8",
    "ansi-regex": "^6.2.2",
    "command-exists": "^1.2.9",
    "comment-json": "^4.2.5",
    "diff": "^7.0.0",
    "dotenv": "^17.1.0",
    "fzf": "^0.5.2",
    "glob": "^10.5.0",
    "highlight.js": "^11.11.1",
    "ink": "^6.2.3",
    "ink-gradient": "^3.0.0",
    "ink-link": "^4.1.0",
    "ink-spinner": "^5.0.0",
    "lowlight": "^3.3.0",
    "open": "^10.1.2",
    "p-limit": "^7.3.0",
    "prompts": "^2.4.2",
    "react": "^19.1.0",
    "read-package-up": "^11.0.0",
    "shell-quote": "^1.8.3",
    "simple-git": "^3.28.0",
    "string-width": "^7.1.0",
    "strip-ansi": "^7.1.0",
    "strip-json-comments": "^3.1.1",
    "undici": "^6.22.0",
    "update-notifier": "^7.3.1",
    "wrap-ansi": "9.0.2",
    "yargs": "^17.7.2",
    "zod": "^3.23.8"
  },
  "devDependencies": {
    "@babel/runtime": "^7.27.6",
    "@google/gemini-cli-test-utils": "file:../test-utils",
    "@qwen-code/qwen-code-test-utils": "file:../test-utils",
    "@testing-library/react": "^16.3.0",
    "@types/archiver": "^6.0.3",
    "@types/command-exists": "^1.2.3",
    "@types/diff": "^7.0.2",
    "@types/dotenv": "^6.1.1",
    "@types/node": "^20.11.24",
    "@types/prompts": "^2.4.9",
    "@types/react": "^19.1.8",
    "@types/react-dom": "^19.1.6",
    "@types/semver": "^7.7.0",
    "@types/shell-quote": "^1.7.5",
    "@types/yargs": "^17.0.32",
    "archiver": "^7.0.1",
    "ink-testing-library": "^4.0.0",
    "jsdom": "^26.1.0",
    "pretty-format": "^30.0.2",
    "react-dom": "^19.1.0",
    "typescript": "^5.3.3",
    "vitest": "^3.1.1"
  },
  "optionalDependencies": {
    "@teddyzhu/clipboard": "^0.0.5",
    "@teddyzhu/clipboard-darwin-arm64": "0.0.5",
    "@teddyzhu/clipboard-darwin-x64": "0.0.5",
    "@teddyzhu/clipboard-linux-arm64-gnu": "0.0.5",
    "@teddyzhu/clipboard-linux-x64-gnu": "0.0.5",
    "@teddyzhu/clipboard-win32-arm64-msvc": "0.0.5",
    "@teddyzhu/clipboard-win32-x64-msvc": "0.0.5"
  },
  "engines": {
    "node": ">=20"
  }
}

```

### File: packages\core\package.json
```json
{
  "name": "@qwen-code/qwen-code-core",
  "version": "0.14.1",
  "description": "Qwen Code Core",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/QwenLM/qwen-code.git"
  },
  "type": "module",
  "main": "dist/index.js",
  "scripts": {
    "build": "node ../../scripts/build_package.js",
    "lint": "eslint . --ext .ts,.tsx",
    "format": "prettier --write .",
    "test": "vitest run",
    "test:ci": "vitest run",
    "typecheck": "tsc --noEmit",
    "postinstall": "node scripts/postinstall.js"
  },
  "files": [
    "dist",
    "vendor",
    "scripts/postinstall.js"
  ],
  "dependencies": {
    "@anthropic-ai/sdk": "^0.36.1",
    "@google/genai": "1.30.0",
    "@iarna/toml": "^2.2.5",
    "@modelcontextprotocol/sdk": "^1.25.1",
    "@opentelemetry/api": "^1.9.0",
    "@opentelemetry/exporter-logs-otlp-grpc": "^0.203.0",
    "@opentelemetry/exporter-logs-otlp-http": "^0.203.0",
    "@opentelemetry/exporter-metrics-otlp-grpc": "^0.203.0",
    "@opentelemetry/exporter-metrics-otlp-http": "^0.203.0",
    "@opentelemetry/exporter-trace-otlp-grpc": "^0.203.0",
    "@opentelemetry/exporter-trace-otlp-http": "^0.203.0",
    "@opentelemetry/instrumentation-http": "^0.203.0",
    "@opentelemetry/sdk-node": "^0.203.0",
    "@types/html-to-text": "^9.0.4",
    "@xterm/headless": "5.5.0",
    "ajv": "^8.17.1",
    "ajv-formats": "^3.0.0",
    "async-mutex": "^0.5.0",
    "chardet": "^2.1.0",
    "iconv-lite": "^0.6.3",
    "chokidar": "^4.0.3",
    "diff": "^7.0.0",
    "dotenv": "^17.1.0",
    "extract-zip": "^2.0.1",
    "fast-levenshtein": "^2.0.6",
    "fast-uri": "^3.0.6",
    "fdir": "^6.4.6",
    "fzf": "^0.5.2",
    "glob": "^10.5.0",
    "google-auth-library": "^10.5.0",
    "html-to-text": "^9.0.5",
    "https-proxy-agent": "^7.0.6",
    "ignore": "^7.0.0",
    "jsonrepair": "^3.13.0",
    "marked": "^15.0.12",
    "mime": "4.0.7",
    "mnemonist": "^0.40.3",
    "open": "^10.1.2",
    "openai": "5.11.0",
    "picomatch": "^4.0.1",
    "prompts": "^2.4.2",
    "shell-quote": "^1.8.3",
    "simple-git": "^3.28.0",
    "strip-ansi": "^7.1.0",
    "tar": "^7.5.2",
    "undici": "^6.22.0",
    "uuid": "^9.0.1",
    "web-tree-sitter": "^0.24.7",
    "ws": "^8.18.0"
  },
  "optionalDependencies": {
    "@lydell/node-pty": "1.2.0-beta.10",
    "@lydell/node-pty-darwin-arm64": "1.2.0-beta.10",
    "@lydell/node-pty-darwin-x64": "1.2.0-beta.10",
    "@lydell/node-pty-linux-x64": "1.2.0-beta.10",
    "@lydell/node-pty-win32-arm64": "1.2.0-beta.10",
    "@lydell/node-pty-win32-x64": "1.2.0-beta.10"
  },
  "devDependencies": {
    "@qwen-code/qwen-code-test-utils": "file:../test-utils",
    "@types/diff": "^7.0.2",
    "@types/dotenv": "^6.1.1",
    "@types/fast-levenshtein": "^0.0.4",
    "@types/minimatch": "^5.1.2",
    "@types/picomatch": "^4.0.1",
    "@types/prompts": "^2.4.9",
    "@types/tar": "^6.1.13",
    "@types/ws": "^8.5.10",
    "msw": "^2.3.4",
    "tree-sitter-wasms": "^0.1.13",
    "typescript": "^5.3.3",
    "vitest": "^3.1.1"
  },
  "engines": {
    "node": ">=20"
  }
}

```

### File: packages\test-utils\package.json
```json
{
  "name": "@qwen-code/qwen-code-test-utils",
  "version": "0.14.1",
  "private": true,
  "main": "src/index.ts",
  "license": "Apache-2.0",
  "type": "module",
  "scripts": {
    "build": "node ../../scripts/build_package.js",
    "typecheck": "tsc --noEmit"
  },
  "devDependencies": {
    "typescript": "^5.3.3"
  },
  "engines": {
    "node": ">=20"
  }
}

```

### File: packages\webui\package.json
```json
{
  "name": "@qwen-code/webui",
  "version": "0.14.1",
  "description": "Shared UI components for Qwen Code packages",
  "type": "module",
  "main": "./dist/index.cjs",
  "module": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js",
      "require": "./dist/index.cjs"
    },
    "./followup": {
      "types": "./dist/followup.d.ts",
      "import": "./dist/followup.js",
      "require": "./dist/followup.cjs"
    },
    "./icons": {
      "types": "./dist/components/icons/index.d.ts",
      "import": "./dist/components/icons/index.js",
      "require": "./dist/components/icons/index.cjs"
    },
    "./tailwind.preset": "./tailwind.preset.cjs",
    "./styles.css": "./dist/styles.css"
  },
  "files": [
    "dist",
    "tailwind.preset.cjs"
  ],
  "sideEffects": [
    "**/*.css"
  ],
  "publishConfig": {
    "access": "public"
  },
  "scripts": {
    "dev": "vite build --watch",
    "build": "vite build && vite build --config vite.config.followup.ts",
    "typecheck": "tsc --noEmit",
    "lint": "eslint src --ext .ts,.tsx",
    "lint:fix": "eslint src --ext .ts,.tsx --fix",
    "storybook": "storybook dev -p 6006",
    "build-storybook": "storybook build"
  },
  "peerDependencies": {
    "@qwen-code/qwen-code-core": ">=0.13.1",
    "react": "^18.0.0 || ^19.0.0",
    "react-dom": "^18.0.0 || ^19.0.0"
  },
  "peerDependenciesMeta": {
    "@qwen-code/qwen-code-core": {
      "optional": true
    }
  },
  "dependencies": {
    "markdown-it": "^14.1.0"
  },
  "devDependencies": {
    "@types/markdown-it": "^14.1.2",
    "@types/react": "^19.1.8",
    "@types/react-dom": "^19.1.6",
    "@vitejs/plugin-react": "^4.2.0",
    "autoprefixer": "^10.4.0",
    "postcss": "^8.4.0",
    "tailwindcss": "^3.4.0",
    "typescript": "^5.0.0",
    "vite": "^5.0.0",
    "vite-plugin-dts": "^4.5.4",
    "storybook": "^10.1.11",
    "@storybook/react-vite": "^10.1.11",
    "@chromatic-com/storybook": "^5.0.0",
    "@storybook/addon-vitest": "^10.1.11",
    "@storybook/addon-a11y": "^10.1.11",
    "@storybook/addon-docs": "^10.1.11",
    "@storybook/addon-onboarding": "^10.1.11",
    "eslint-plugin-storybook": "^10.1.11",
    "playwright": "^1.57.0",
    "@vitest/browser": "^3.2.4",
    "@vitest/coverage-v8": "^3.2.4"
  },
  "keywords": [
    "qwen",
    "ui",
    "components",
    "shared"
  ],
  "author": "Qwen Team",
  "license": "MIT"
}

```

### File: packages\webui\README.md
```md
# @qwen-code/webui

A shared React component library for Qwen Code applications, providing cross-platform UI components with consistent styling and behavior.

## Features

- **Cross-platform support**: Components work seamlessly across VS Code extension, web, and other platforms
- **Platform Context**: Abstraction layer for platform-specific capabilities
- **Tailwind CSS**: Shared styling preset for consistent design
- **TypeScript**: Full type definitions for all components
- **Storybook**: Interactive component documentation and development
- **Multiple Build Formats**: Supports ESM, CJS, and UMD formats for different environments
- **CDN Usage**: Can be loaded directly in browsers via CDN

## Installation

```bash
npm install @qwen-code/webui
```

## CDN Usage

You can also use this library directly in the browser via CDN:

### Option 1: With JSX Support (using Babel)

```html
<!DOCTYPE html>
<html>
  <head>
    <!-- Load React -->
    <script
      crossorigin
      src="https://unpkg.com/react@18/umd/react.production.min.js"
    ></script>
    <script
      crossorigin
      src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"
    ></script>

    <!-- Load Babel Standalone for JSX processing -->
    <script src="https://unpkg.com/@babel/standalone@7.23.6/babel.min.js"></script>

    <!-- Manually create the jsxRuntime object to satisfy the dependency -->
    <script>
      // Provide a minimal JSX runtime for builds that expect react/jsx-runtime globals.
      const withKey = (props, key) =>
        key == null ? props : Object.assign({}, props, { key });
      const jsx = (type, props, key) =>
        React.createElement(type, withKey(props, key));
      const jsxRuntime = {
        Fragment: React.Fragment,
        jsx,
        jsxs: jsx,
        jsxDEV: jsx,
      };

      window.ReactJSXRuntime = jsxRuntime;
      window['react/jsx-runtime'] = jsxRuntime;
      window['react/jsx-dev-runtime'] = jsxRuntime;
    </script>

    <!-- Load the webui library -->
    <script src="https://unpkg.com/@qwen-code/webui@0.1.0-beta.2/dist/index.umd.js"></script>

    <!-- Load the CSS -->
    <link
      rel="stylesheet"
      href="https://unpkg.com/@qwen-code/webui@0.1.0-beta.2/dist/styles.css"
    />
  </head>
  <body>
    <div id="root"></div>

    <script type="text/babel">
      // Access components from the global QwenCodeWebUI object
      const { ChatViewer } = QwenCodeWebUI;

      // Use the components with JSX support
      const App = () => (
        <ChatViewer messages={/* your messages */} />
      );

      ReactDOM.render(<App />, document.getElementById('root'));
    </script>
  </body>
</html>
```

### Option 2: Without JSX (using React.createElement directly)

```html
<!DOCTYPE html>
<html>
  <head>
    <!-- Load React -->
    <script
      crossorigin
      src="https://unpkg.com/react@18/umd/react.production.min.js"
    ></script>
    <script
      crossorigin
      src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"
    ></script>

    <!-- Manually create the jsxRuntime object to satisfy the dependency -->
    <script>
      // Provide a minimal JSX runtime for builds that expect react/jsx-runtime globals.
      const withKey = (props, key) =>
        key == null ? props : Object.assign({}, props, { key });
      const jsx = (type, props, key) =>
        React.createElement(type, withKey(props, key));
      const jsxRuntime = {
        Fragment: React.Fragment,
        jsx,
        jsxs: jsx,
        jsxDEV: jsx,
      };

      window.ReactJSXRuntime = jsxRuntime;
      window['react/jsx-runtime'] = jsxRuntime;
      window['react/jsx-dev-runtime'] = jsxRuntime;
    </script>

    <!-- Load the webui library -->
    <script src="https://unpkg.com/@qwen-code/webui@0.1.0-beta.2/dist/index.umd.js"></script>

    <!-- Load the CSS -->
    <link
      rel="stylesheet"
      href="https://unpkg.com/@qwen-code/webui@0.1.0-beta.2/dist/styles.css"
    />
  </head>
  <body>
    <div id="root"></div>

    <script>
      // Access components from the global QwenCodeWebUI object
      const { ChatViewer } = QwenCodeWebUI;

      // Use the components with React.createElement (no JSX)
      const App = React.createElement(ChatViewer, {
        messages: [
          /* your messages */
        ],
      });

      ReactDOM.render(App, document.getElementById('root'));
    </script>
  </body>
</html>
```

For a complete working example, see [examples/cdn-usage-demo.html](./examples/cdn-usage-demo.html).

## Quick Start

```tsx
import { Button, Input, Tooltip } from '@qwen-code/webui';
import { PlatformProvider } from '@qwen-code/webui/context';

function App() {
  return (
    <PlatformProvider value={platformContext}>
      <Button variant="primary" onClick={handleClick}>
        Click me
      </Button>
    </PlatformProvider>
  );
}
```

## Components

### UI Components

#### Button

```tsx
import { Button } from '@qwen-code/webui';

<Button variant="primary" size="md" loading={false}>
  Submit
</Button>;
```

**Props:**

- `variant`: 'primary' | 'secondary' | 'danger' | 'ghost' | 'outline'
- `size`: 'sm' | 'md' | 'lg'
- `loading`: boolean
- `leftIcon`: ReactNode
- `rightIcon`: ReactNode
- `fullWidth`: boolean

#### Input

```tsx
import { Input } from '@qwen-code/webui';

<Input
  label="Email"
  placeholder="Enter email"
  error={hasError}
  errorMessage="Invalid email"
/>;
```

**Props:**

- `size`: 'sm' | 'md' | 'lg'
- `error`: boolean
- `errorMessage`: string
- `label`: string
- `helperText`: string
- `leftElement`: ReactNode
- `rightElement`: ReactNode

#### Tooltip

```tsx
import { Tooltip } from '@qwen-code/webui';

<Tooltip content="Helpful tip">
  <span>Hover me</span>
</Tooltip>;
```

### Icons

```tsx
import { FileIcon, FolderIcon, CheckIcon } from '@qwen-code/webui/icons';

<FileIcon size={16} className="text-gray-500" />;
```

Available icon categories:

- **FileIcons**: FileIcon, FolderIcon, SaveDocumentIcon
- **StatusIcons**: CheckIcon, ErrorIcon, WarningIcon, LoadingIcon
- **NavigationIcons**: ArrowLeftIcon, ArrowRightIcon, ChevronIcon
- **EditIcons**: EditIcon, DeleteIcon, CopyIcon
- **SpecialIcons**: SendIcon, StopIcon, CloseIcon

### Layout Components

- `Container`: Main layout wrapper
- `Header`: Application header
- `Footer`: Application footer
- `Sidebar`: Side navigation
- `Main`: Main content area

### Message Components

- `Message`: Chat message display
- `MessageList`: List of messages
- `MessageInput`: Message input field
- `WaitingMessage`: Loading/waiting state
- `InterruptedMessage`: Interrupted state display

## Platform Context

The Platform Context provides an abstraction layer for platform-specific capabilities:

```tsx
import { PlatformProvider, usePlatform } from '@qwen-code/webui/context';

const platformContext = {
  postMessage: (message) => vscode.postMessage(message),
  onMessage: (handler) => {
    window.addEventListener('message', handler);
    return () => window.removeEventListener('message', handler);
  },
  openFile: (path) => {
    /* platform-specific */
  },
  platform: 'vscode',
};

function App() {
  return (
    <PlatformProvider value={platformContext}>
      <YourApp />
    </PlatformProvider>
  );
}

function Component() {
  const { postMessage, platform } = usePlatform();
  // Use platform capabilities
}
```

## Tailwind Preset

Use the shared Tailwind preset for consistent styling:

```js
// tailwind.config.js
module.exports = {
  presets: [require('@qwen-code/webui/tailwind.preset.cjs')],
  // your customizations
};
```

## Development

### Running Storybook

```bash
cd packages/webui
npm run storybook
```

### Building

```bash
npm run build
```

### Type Checking

```bash
npm run typecheck
```

## Project Structure

```
packages/webui/
├── src/
│   ├── components/
│   │   ├── icons/          # Icon components
│   │   ├── layout/         # Layout components
│   │   ├── messages/       # Message components
│   │   └── ui/             # UI primitives
│   ├── context/            # Platform context
│   ├── hooks/              # Custom hooks
│   └── types/              # Type definitions
├── .storybook/             # Storybook config
├── tailwind.preset.cjs     # Shared Tailwind preset
└── vite.config.ts          # Build configuration
```

## License

Apache-2.0

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
