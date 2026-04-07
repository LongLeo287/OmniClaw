---
id: opik
type: knowledge
owner: OA_Triage
---
# opik
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align="center"><b><a href="README.md">English</a> | <a href="readme_CN.md">简体中文</a> | <a href="readme_JP.md">日本語</a> | <a href="readme_PT_BR.md">Português (Brasil)</a> | <a href="readme_KO.md">한국어</a><br><a href="readme_ES.md">Español</a> | <a href="readme_FR.md">Français</a> | <a href="readme_DE.md">Deutsch</a> | <a href="readme_RU.md">Русский</a> | <a href="readme_AR.md">العربية</a> | <a href="readme_HI.md">हिन्दी</a> | <a href="readme_TR.md">Türkçe</a></b></div>


<h1 align="center" style="border-bottom: none">
    <div>
        <a href="https://www.comet.com/site/products/opik/?from=llm&utm_source=opik&utm_medium=github&utm_content=header_img&utm_campaign=opik"><picture>
            <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/comet-ml/opik/refs/heads/main/apps/opik-documentation/documentation/static/img/logo-dark-mode.svg">
            <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/comet-ml/opik/refs/heads/main/apps/opik-documentation/documentation/static/img/opik-logo.svg">
            <img alt="Comet Opik logo" src="https://raw.githubusercontent.com/comet-ml/opik/refs/heads/main/apps/opik-documentation/documentation/static/img/opik-logo.svg" width="200" />
        </picture></a>
        <br>
        Opik
    </div>
</h1>
<h2 align="center" style="border-bottom: none">Open-source AI Observability, Evaluation, and Optimization</h2>
<p align="center">
Opik helps you build, test, and optimize generative AI application that run better, from prototype to production.  From RAG chatbots to code assistants to complex agentic systems, Opik provides comprehensive tracing, evaluation, and automatic prompt and tool optimization to take the guesswork out of AI development.
</p>

<div align="center">

[![Python SDK](https://img.shields.io/pypi/v/opik)](https://pypi.org/project/opik/)
[![License](https://img.shields.io/github/license/comet-ml/opik)](https://github.com/comet-ml/opik/blob/main/LICENSE)
[![Build](https://github.com/comet-ml/opik/actions/workflows/build_apps.yml/badge.svg)](https://github.com/comet-ml/opik/actions/workflows/build_apps.yml)
<!-- [![Quick Start](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/comet-ml/opik/blob/main/apps/opik-documentation/documentation/docs/cookbook/opik_quickstart.ipynb) -->

</div>

<p align="center">
    <a href="https://www.comet.com/site/products/opik/?from=llm&utm_source=opik&utm_medium=github&utm_content=website_button&utm_campaign=opik"><b>Website</b></a> •
    <a href="https://chat.comet.com"><b>Slack Community</b></a> •
    <a href="https://x.com/Cometml"><b>Twitter</b></a> •
    <a href="https://www.comet.com/docs/opik/changelog"><b>Changelog</b></a> •
    <a href="https://www.comet.com/docs/opik/?from=llm&utm_source=opik&utm_medium=github&utm_content=docs_button&utm_campaign=opik"><b>Documentation</b></a>
</p>

<div align="center" style="margin-top: 1em; margin-bottom: 1em;">
<a href="#-what-is-opik">🚀 What is Opik?</a> • <a href="#%EF%B8%8F-opik-server-installation">🛠️ Opik Server Installation</a> • <a href="#-opik-client-sdk">💻 Opik Client SDK</a> • <a href="#-logging-traces-with-integrations">📝 Logging Traces</a><br>
<a href="#-llm-as-a-judge-metrics">🧑‍⚖️ LLM as a Judge</a> • <a href="#-evaluating-your-llm-application">🔍 Evaluating your Application</a> • <a href="#-star-us-on-github">⭐ Star Us</a> • <a href="#-contributing">🤝 Contributing</a>
</div>

<br>

[![Opik platform screenshot (thumbnail)](readme-thumbnail-new.png)](https://www.comet.com/signup?from=llm&utm_source=opik&utm_medium=github&utm_content=readme_banner&utm_campaign=opik)

<a id="-what-is-opik"></a>
## 🚀 What is Opik?

Opik (built by [Comet](https://www.comet.com?from=llm&utm_source=opik&utm_medium=github&utm_content=what_is_opik_link&utm_campaign=opik)) is an open-source platform designed to streamline the entire lifecycle of LLM applications. It empowers developers to evaluate, test, monitor, and optimize their models and agentic systems. Key offerings include:

- **Comprehensive Observability**: Deep tracing of LLM calls, conversation logging, and agent activity.
- **Advanced Evaluation**: Robust prompt evaluation, LLM-as-a-judge, and experiment management.
- **Production-Ready**: Scalable monitoring dashboards and online evaluation rules for production.
- **Opik Agent Optimizer**: Dedicated SDK and set of optimizers to enhance prompts and agents.
- **Opik Guardrails**: Features to help you implement safe and responsible AI practices.

<br>

Key capabilities include:

- **Development & Tracing:**
  - Track all LLM calls and traces with detailed context during development and in production ([Quickstart](https://www.comet.com/docs/opik/quickstart/?from=llm&utm_source=opik&utm_medium=github&utm_content=quickstart_link&utm_campaign=opik)).
  - Extensive 3rd-party integrations for easy observability: Seamlessly integrate with a growing list of frameworks, supporting many of the largest and most popular ones natively (including recent additions like **Google ADK**, **Autogen**, and **Flowise AI**). ([Integrations](https://www.comet.com/docs/opik/integrations/overview/?from=llm&utm_source=opik&utm_medium=github&utm_content=integrations_link&utm_campaign=opik))
  - Annotate traces and spans with feedback scores via the [Python SDK](https://www.comet.com/docs/opik/tracing/annotate_traces/#annotating-traces-and-spans-using-the-sdk?from=llm&utm_source=opik&utm_medium=github&utm_content=sdk_link&utm_campaign=opik) or the [UI](https://www.comet.com/docs/opik/tracing/annotate_traces/#annotating-traces-through-the-ui?from=llm&utm_source=opik&utm_medium=github&utm_content=ui_link&utm_campaign=opik).
  - Experiment with prompts and models in the [Prompt Playground](https://www.comet.com/docs/opik/prompt_engineering/playground).

- **Evaluation & Testing**:
  - Automate your LLM application evaluation with [Datasets](https://www.comet.com/docs/opik/evaluation/manage_datasets/?from=llm&utm_source=opik&utm_medium=github&utm_content=datasets_link&utm_campaign=opik) and [Experiments](https://www.comet.com/docs/opik/evaluation/evaluate_your_llm/?from=llm&utm_source=opik&utm_medium=github&utm_content=eval_link&utm_campaign=opik).
  - Leverage powerful LLM-as-a-judge metrics for complex tasks like [hallucination detection](https://www.comet.com/docs/opik/evaluation/metrics/hallucination/?from=llm&utm_source=opik&utm_medium=github&utm_content=hallucination_link&utm_campaign=opik), [moderation](https://www.comet.com/docs/opik/evaluation/metrics/moderation/?from=llm&utm_source=opik&utm_medium=github&utm_content=moderation_link&utm_campaign=opik), and RAG assessment ([Answer Relevance](https://www.comet.com/docs/opik/evaluation/metrics/answer_relevance/?from=llm&utm_source=opik&utm_medium=github&utm_content=alex_link&utm_campaign=opik), [Context Precision](https://www.comet.com/docs/opik/evaluation/metrics/context_precision/?from=llm&utm_source=opik&utm_medium=github&utm_content=context_link&utm_campaign=opik)).
  - Integrate evaluations into your CI/CD pipeline with our [PyTest integration](https://www.comet.com/docs/opik/testing/pytest_integration/?from=llm&utm_source=opik&utm_medium=github&utm_content=pytest_link&utm_campaign=opik).

- **Production Monitoring & Optimization**:
  - Log high volumes of production traces: Opik is designed for scale (40M+ traces/day).
  - Monitor feedback scores, trace counts, and token usage over time in the [Opik Dashboard](https://www.comet.com/docs/opik/production/production_monitoring/?from=llm&utm_source=opik&utm_medium=github&utm_content=dashboard_link&utm_campaign=opik).
  - Utilize [Online Evaluation Rules](https://www.comet.com/docs/opik/production/rules/?from=llm&utm_source=opik&utm_medium=github&utm_content=dashboard_link&utm_campaign=opik) with LLM-as-a-Judge metrics to identify production issues.
  - Leverage **Opik Agent Optimizer** and **Opik Guardrails** to continuously improve and secure your LLM applications in production.

> [!TIP]
> If you are looking for features that Opik doesn't have today, please raise a new [Feature request](https://github.com/comet-ml/opik/issues/new/choose) 🚀

<br>

<a id="%EF%B8%8F-opik-server-installation"></a>
## 🛠️ Opik Server Installation

Get your Opik server running in minutes. Choose the option that best suits your needs:

### Option 1: Comet.com Cloud (Easiest & Recommended)

Access Opik instantly without any setup. Ideal for quick starts and hassle-free maintenance.

👉 [Create your free Comet account](https://www.comet.com/signup?from=llm&utm_source=opik&utm_medium=github&utm_content=install_create_link&utm_campaign=opik)

### Option 2: Self-Host Opik for Full Control

Deploy Opik in your own environment. Choose between Docker for local setups or Kubernetes for scalability.

#### Self-Hosting with Docker Compose (for Local Development & Testing)

This is the simplest way to get a local Opik instance running. Note the new `./opik.sh` installation script:

On Linux or Mac Environment:

```bash
# Clone the Opik repository
git clone https://github.com/comet-ml/opik.git

# Navigate to the repository
cd opik

# Start the Opik platform
./opik.sh
```

On Windows Environment:

```powershell
# Clone the Opik repository
git clone https://github.com/comet-ml/opik.git

# Navigate to the repository
cd opik

# Start the Opik platform
powershell -ExecutionPolicy ByPass -c ".\\opik.ps1"
```

**Service Profiles for Development**

The Opik installation scripts now support service profiles for different development scenarios:

```bash
# Start full Opik suite (default behavior)
./opik.sh

# Start only infrastructure services (databases, caches etc.)
./opik.sh --infra

# Start infrastructure + backend services
./opik.sh --backend

# Enable guardrails with any profile
./opik.sh --guardrails # Guardrails with full Opik suite
./opik.sh --backend --guardrails # Guardrails with infrastructure + backend
```

Use the `--help` or `--info` options to troubleshoot issues. Dockerfiles now ensure containers run as non-root users for enhanced security. Once all is up and running, you can now visit [localhost:5173](http://localhost:5173) on your browser! For detailed instructions, see the [Local Deployment Guide](https://www.comet.com/docs/opik/self-host/local_deployment?from=llm&utm_source=opik&utm_medium=github&utm_content=self_host_link&utm_campaign=opik).

#### Self-Hosting with Kubernetes & Helm (for Scalable Deployments)

For production or larger-scale self-hosted deployments, Opik can be installed on a Kubernetes cluster using our Helm chart. Click the badge for the full [Kubernetes Installation Guide using Helm](https://www.comet.com/docs/opik/self-host/kubernetes/#kubernetes-installation?from=llm&utm_source=opik&utm_medium=github&utm_content=kubernetes_link&utm_campaign=opik).

[![Kubernetes](https://img.shields.io/badge/Kubernetes-%23326ce5.svg?&logo=kubernetes&logoColor=white)](https://www.comet.com/docs/opik/self-host/kubernetes/#kubernetes-installation?from=llm&utm_source=opik&utm_medium=github&utm_content=kubernetes_link&utm_campaign=opik)

> [!IMPORTANT]
> **Version 1.7.0 Changes**: Please check the [changelog](https://github.com/comet-ml/opik/blob/main/CHANGELOG.md) for important updates and breaking changes.

<a id="-opik-client-sdk"></a>
## 💻 Opik Client SDK

Opik provides a suite of client libraries and a REST API to interact with the Opik server. This includes SDKs for Python, TypeScript, and Ruby (via OpenTelemetry), allowing for seamless integration into your workflows. For detailed API and SDK references, see the [Opik Client Reference Documentation](https://www.comet.com/docs/opik/reference/overview?from=llm&utm_source=opik&utm_medium=github&utm_content=reference_link&utm_campaign=opik).

### Python SDK Quick Start

To get started with the Python SDK:

Install the package:

```bash
# install using pip
pip install opik

# or install with uv
uv pip install opik
```

Configure the python SDK by running the `opik configure` command, which will prompt you for your Opik server address (for self-hosted instances) or your API key and workspace (for Comet.com):

```bash
opik configure
```

> [!TIP]
> You can also call `opik.configure(use_local=True)` from your Python code to configure the SDK to run on a local self-hosted installation, or provide API key and workspace details directly for Comet.com. Refer to the [Python SDK documentation](https://www.comet.com/docs/opik/python-sdk-reference/?from=llm&utm_source=opik&utm_medium=github&utm_content=python_sdk_docs_link&utm_campaign=opik) for more configuration options.

You are now ready to start logging traces using the [Python SDK](https://www.comet.com/docs/opik/python-sdk-reference/?from=llm&utm_source=opik&utm_medium=github&utm_content=sdk_link2&utm_campaign=opik).

<a id="-logging-traces-with-integrations"></a>
### 📝 Logging Traces with Integrations

The easiest way to log traces is to use one of our direct integrations. Opik supports a wide array of frameworks, including recent additions like **Google ADK**, **Autogen**, **AG2**, and **Flowise AI**:

| Integration           | Description                                             | Documentation                                                                                                                                                                  |
| --------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ADK                   | Log traces for Google Agent Development Kit (ADK)       | [Documentation](https://www.comet.com/docs/opik/integrations/adk?utm_source=opik&utm_medium=github&utm_content=google_adk_link&utm_campaign=opik)                              |
| AG2                   | Log traces for AG2 LLM calls                            | [Documentation](https://www.comet.com/docs/opik/integrations/ag2?utm_source=opik&utm_medium=github&utm_content=ag2_link&utm_campaign=opik)                                     |
| AIsuite               | Log traces for aisuite LLM calls                        | [Documentation](https://www.comet.com/docs/opik/integrations/aisuite?utm_source=opik&utm_medium=github&utm_content=aisuite_link&utm_campaign=opik)                             |
| Agno                  | Log traces for Agno agent orchestration framework calls | [Documentation](https://www.comet.com/docs/opik/integrations/agno?utm_source=opik&utm_medium=github&utm_content=agno_link&utm_campaign=opik)                                   |
| Anthropic             | Log traces for Anthropic LLM calls                      | [Documentation](https://www.comet.com/docs/opik/integrations/anthropic?utm_source=opik&utm_medium=github&utm_content=anthropic_link&utm_campaign=opik)                         |
| Autogen           
... [TRUNCATED]
```

### File: scripts\README.md
```md
# Scripts

## General guidelines

Scripts in this folder are meant to be run from the repository base folder. Example:

```bash
./scripts/generate_openapi.sh
```

## Scripts list

### `generate_openapi.sh`

Use this script to generate an updated OpenAPI specification file for the documentation application and the SDKs,
and also to build the SDKs autogenerated code, for any supported language by Fern.

You require to install Fern to run this script.

See:

- https://buildwithfern.com/

### `start_openapi_server.sh`

Use this script to start a local server with an updated OpenAPI specification file, to be able to test the specification
quickly.

Open the server in your browser at http://localhost:3003/

See:

- https://github.com/Redocly/redoc
- https://docs.oracle.com/en/java/javase/23/docs/specs/man/jwebserver.html

### `sync-codex.sh`

Synchronize `.agents/rules/*.mdc` into Codex-friendly markdown and generate a local
`AGENTS.override.md` for Codex sessions.

Usage:

```bash
./scripts/sync-codex.sh .agents AGENTS.md AGENTS.override.md
```

This script is executed by `make codex`.

### `dev-runner.sh`

Development environment runner script for local Opik development. This script manages Docker infrastructure,
backend, and frontend services for development workflows.

#### Quick Start

```bash
# Full restart with rebuild (default)
./scripts/dev-runner.sh

# Or explicitly
./scripts/dev-runner.sh --restart
```

#### Available Commands

**Standard Mode** (Backend and Frontend as local processes):

| Command | Description |
|---------|-------------|
| `--start` | Start services without rebuilding |
| `--stop` | Stop all services |
| `--restart` | Stop, rebuild, and start all services (default) |
| `--quick-restart` | Quick restart: rebuild backend only, keep infrastructure running |
| `--verify` | Check status of all services |

**BE-Only Mode** (Backend as local process, Frontend in Docker):

| Command | Description |
|---------|-------------|
| `--be-only-start` | Start services without rebuilding |
| `--be-only-stop` | Stop all services |
| `--be-only-restart` | Stop, rebuild, and start services |
| `--be-only-verify` | Check status of services |

**Other Commands**:

| Command | Description |
|---------|-------------|
| `--build-be` | Build backend only |
| `--build-fe` | Build frontend only |
| `--migrate` | Run database migrations |
| `--lint-be` | Lint backend code |
| `--lint-fe` | Lint frontend code |
| `--logs` | Show recent logs |
| `--debug` | Enable debug mode (combine with other flags) |
| `--help` | Show help message |

---

## Multi-Worktree Support

The `dev-runner.sh` and `opik.sh` scripts support running multiple Opik development environments
simultaneously from different git worktrees. Each worktree automatically gets isolated ports and
Docker containers.

### How It Works

1. **Worktree Detection**: The script identifies your worktree by its directory name
2. **Port Offset Calculation**: A deterministic offset (0-99) is calculated from an MD5 hash of your project path
3. **Port Assignment**: All service ports are offset from their base values
4. **Docker Isolation**: Each worktree gets a unique Docker Compose project name (`opik-<worktree-id>`)

### Port Assignments

| Service | Base Port | Formula |
|---------|-----------|---------|
| Backend | 8080 | 8080 + offset |
| Frontend | 5174 | 5174 + offset |
| MySQL | 3306 | 3306 + offset |
| Redis | 6379 | 6379 + offset |
| ClickHouse HTTP | 8123 | 8123 + offset |
| ClickHouse Native | 9000 | 9000 + offset |
| Python Backend | 8000 | 8000 + offset |
| Zookeeper | 2181 | 2181 + offset |
| MinIO API | 9001 | 9001 + offset |
| MinIO Console | 9090 | 9090 + offset |

### Manual Port Override

If you need to use a specific port offset (e.g., to avoid conflicts or use standard ports):

```bash
# Use standard ports (offset 0)
OPIK_PORT_OFFSET=0 ./scripts/dev-runner.sh --restart

# Use a specific offset
OPIK_PORT_OFFSET=10 ./scripts/dev-runner.sh --restart
```

### Running Multiple Worktrees

```bash
# Terminal 1: Main branch
cd ~/opik
./scripts/dev-runner.sh --restart
# Services running on ports based on hash of ~/opik

# Terminal 2: Feature branch worktree
cd ~/opik-worktrees/feature-xyz
./scripts/dev-runner.sh --restart
# Services running on different ports based on hash of ~/opik-worktrees/feature-xyz
```

### Port Collision Detection

The script automatically checks for port conflicts before starting services. If a collision
is detected, you'll see an error message with suggestions:

```
[ERROR] Port 8122 (Backend) is already in use

Port collision detected! Another process is using one or more required ports.
This might be caused by:
  - Another Opik instance running from a different worktree
  - Stale containers from a previous run
  - Other services using the same ports

To resolve:
  1. Stop other Opik instances: ./scripts/dev-runner.sh --stop
  2. Use a different port offset: export OPIK_PORT_OFFSET=<0-99>
  3. Check running processes: lsof -i :8122
```

### File Isolation

Each worktree also gets isolated log and PID files:

| File | Path |
|------|------|
| Backend PID | `/tmp/opik-<worktree-id>-backend.pid` |
| Frontend PID | `/tmp/opik-<worktree-id>-frontend.pid` |
| Backend Log | `/tmp/opik-<worktree-id>-backend.log` |
| Frontend Log | `/tmp/opik-<worktree-id>-frontend.log` |

### Docker Container Naming

Docker containers are prefixed with the worktree project name:

- Main repo (`opik`): `opik-opik-mysql-1`, `opik-opik-backend-1`, etc.
- Worktree (`feature-xyz`): `opik-feature-xyz-mysql-1`, `opik-feature-xyz-backend-1`, etc.

### Environment Variables

| Variable | Description |
|----------|-------------|
| `OPIK_PORT_OFFSET` | Override automatic port offset (0-99) |
| `DEBUG_MODE=true` | Enable verbose debug output |

### SDK Configuration

When using the Opik SDK with a worktree-based development environment, configure it to use your
worktree's backend port (shown when you start the environment):

```bash
# Configure SDK (use the backend port shown at startup)
export OPIK_URL_OVERRIDE='http://localhost:8080'  # or your worktree's port
export OPIK_WORKSPACE='default'
```

Or edit `~/.opik.config`:
```ini
[opik]
url_override = http://localhost:8122
workspace = default
```

```

### File: .agents\skills\README.md
```md
# Skills Index

Domain-specific agent skills for the Opik monorepo. Each skill provides patterns, conventions, and guidance for a specific area of the codebase.

| Skill | Path | Description |
|-------|------|-------------|
| diagram-generation | `diagram-generation/` | Generate self-contained HTML architecture diagrams. Use when creating visual diagrams for PRs, task plans, or architectural explanations. |
| documentation | `documentation/` | Feature documentation and release notes patterns. Use when documenting changes, writing PR descriptions, or preparing releases. |
| local-dev | `local-dev/` | Local development environment setup and commands. Use when helping with dev server, Docker, or local testing. |
| opik-backend | `opik-backend/` | Java backend patterns for Opik. Use when working in `apps/opik-backend`, designing APIs, database operations, or services. |
| opik-frontend | `opik-frontend/` | React frontend patterns for Opik. Use when working in `apps/opik-frontend`, on components, state, or data fetching. |
| playwright-e2e | `playwright-e2e/` | Playwright E2E test generation workflow. Use when generating, fixing, or planning automated tests in `tests_end_to_end/`. |
| python-sdk | `python-sdk/` | Python SDK patterns for Opik. Use when working in `sdks/python`, on SDK APIs, integrations, or message processing. |
| typescript-sdk | `typescript-sdk/` | TypeScript SDK patterns for Opik. Use when working in `sdks/typescript`. |

Each skill directory contains a `SKILL.md` entry point plus supporting documents (testing, code quality, patterns, etc.).

```

### File: extensions\cursor\package.json
```json
{
  "name": "opik",
  "displayName": "Opik - Save and share your chat history",
  "description": "Export your chat history from Cursor to Opik.",
  "repository": "https://github.com/comet-ml/opik",
  "publisher": "opik",
  "version": "0.3.4",
  "preview": false,
  "engines": {
    "vscode": "^1.90.0"
  },
  "categories": [
    "Other"
  ],
  "activationEvents": [
    "onStartupFinished"
  ],
  "main": "./out/extension.js",
  "icon": "icon.png",
  "contributes": {
    "commands": [
      {
        "command": "opik.resetState",
        "title": "Reset Extension State",
        "category": "Opik"
      }
    ],
    "configuration": [
      {
        "title": "Opik Configuration",
        "properties": {
          "opik.apiKey": {
            "type": "string",
            "default": "",
            "markdownDescription": "Opik API Key for authentication. Get your key at [Comet Settings](https://www.comet.com/api/my/settings/). \n\nAlternatively, you can set this in `~/.opik.config` file.",
            "order": 0
          },
          "opik.apiUrl": {
            "type": "string",
            "default": "https://www.comet.com/opik/api",
            "markdownDescription": "API URL for Opik backend. Change this only if you're using a self-hosted instance.",
            "order": 1
          },
          "opik.workspace": {
            "type": "string",
            "default": "default",
            "markdownDescription": "Workspace name where your traces will be stored.",
            "order": 2
          },
          "opik.projectName": {
            "type": "string",
            "default": "cursor",
            "markdownDescription": "Project name for organizing Cursor chat sessions within your workspace.",
            "order": 3
          }
        }
      },
      {
        "title": "MCP Server",
        "properties": {
          "opik.mcp.enabled": {
            "type": "boolean",
            "default": true,
            "markdownDescription": "Enable automatic registration of the Opik MCP server with Cursor to provide enhanced context in your chats."
          }
        }
      },
      {
        "title": "Advanced",
        "properties": {
          "opik.enableDebugLogs": {
            "type": "boolean",
            "default": false,
            "markdownDescription": "Enable detailed debug logging for troubleshooting. Logs will appear in the Output panel under 'Opik Debug'."
          }
        }
      }
    ]
  },
  "scripts": {
    "vscode:prepublish": "npm run esbuild-base -- --minify",
    "build": "vsce pack",
    "compile": "tsc -p ./",
    "esbuild-base": "esbuild ./src/extension.ts --bundle --outfile=out/extension.js --external:vscode --external:fsevents --format=cjs --platform=node",
    "esbuild": "npm run esbuild-base -- --sourcemap",
    "esbuild-watch": "npm run esbuild-base -- --sourcemap --watch",
    "deploy": "vsce publish",
    "watch": "tsc -watch -p ./",
    "pretest": "npm run compile && npm run lint",
    "lint": "eslint src",
    "test": "vscode-test"
  },
  "devDependencies": {
    "@types/mocha": "^10.0.10",
    "@types/node": "20.x",
    "@types/uuid": "^10.0.0",
    "@types/vscode": "^1.90.0",
    "@typescript-eslint/eslint-plugin": "^8.28.0",
    "@typescript-eslint/parser": "^8.28.0",
    "@vscode/test-cli": "^0.0.10",
    "@vscode/test-electron": "^2.4.1",
    "@vscode/vsce": "^3.7.1",
    "esbuild": "^0.24.2",
    "eslint": "^9.23.0",
    "typescript": "^5.8.2"
  },
  "dependencies": {
    "@sentry/node": "^10.38.0",
    "glob": "^11.1.0",
    "node-fetch": "^3.3.2",
    "opik": "^1.10.9",
    "uuid": "^11.0.3"
  }
}

```

### File: extensions\cursor\README.md
```md
# Opik

The `Opik` extension for VSCode will allow you to save your Cursor chat sessions in Opik.  You can share these chat sessions with your team or even on Twitter / X if you are so inclined ! Your vibe coding session no longer need to be private !

![Screenshot of Opik dashboard](./readme_image.png)

Learn more about:
- [Opik](https://github.com/comet-ml/opik) is an Open-Source LLM evaluation platform that allows you to keep track of all your LLM chat conversations in one place.
- [Cursor](https://www.cursor.com/) is "the" AI Code Editor.

When you use this extension, it will automatically upload your Cursor chats to Opik and make them available in the `cursor` project. You will be to view the conversations in the `thread` tab and view your token usage in the metrics tab, you'd be surprised how many tokens you consume!

## Installation

### Installing in Cursor

To install this extension in Cursor, navigate to the extensions tab in the top left (above the file and folder list) and search for `Opik`. Click on the extension and simply click on Install.

Once it is installed, you will be prompted in the bottom right of the screen to enter your Opik API key. You can create a free Opik account at [https://www.comet.com/signup](https://www.comet.com/signup?from=llm). Refer to the Congiguration section below for additional information.

### Configuration

To configure the extension, open up VSCode settings (Ctrl + ,), find the setting called "Opik: Opik API Key", and enter your Opik API key. You can create a free Opik account at [https://www.comet.com/signup](https://www.comet.com/signup?from=llm).

## Usage

Once installed, there is nothing for you to do ! Just sit back and enjoy your coding experience knowing that all your chat history is saved in Opik

> 💻: This extension is currently under development 🚧. Please report any bugs on [Github](https://github.com/comet-ml/opik) if you run into any issues.

## Local Development

This extension is Open-Source and available on [Github](https://github.com/comet-ml/opik).

In order to debug the application, you will need to:
1. Run `npm run compile` - This is to compile the Typescript extension to javascript
2. Navigate to `./out/extension.js` and press `F5`.

```

### File: sdks\python\README.md
```md
# Opik Python SDK

[![PyPI version](https://img.shields.io/pypi/v/opik.svg)](https://pypi.org/project/opik/)
[![Python versions](https://img.shields.io/pypi/pyversions/opik.svg)](https://pypi.org/project/opik/)
[![Downloads](https://static.pepy.tech/badge/opik)](https://pepy.tech/project/opik)
[![License](https://img.shields.io/github/license/comet-ml/opik)](https://github.com/comet-ml/opik/blob/main/LICENSE)

The Opik Python SDK allows you to integrate your Python applications with the Opik platform, enabling comprehensive tracing, evaluation, and monitoring of your LLM systems. Opik helps you build, evaluate, and optimize LLM systems that run better, faster, and cheaper.

Opik is an open-source LLM evaluation platform by [Comet](https://www.comet.com?from=llm&utm_source=opik&utm_medium=github&utm_content=python_sdk_readme&utm_campaign=opik). For more information about the broader Opik ecosystem, visit our main [GitHub repository](https://github.com/comet-ml/opik), [Website](https://www.comet.com/site/products/opik/), or [Documentation](https://www.comet.com/docs/opik/).

## Quickstart

Get started quickly with Opik using our interactive notebook:

<a href="https://colab.research.google.com/github/comet-ml/opik/blob/master/apps/opik-documentation/documentation/docs/cookbook/opik_quickstart.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open Quickstart In Colab"/>
</a>

## Installation

Install the `opik` package using pip or uv:

```bash
# using pip
pip install opik

# using uv (faster)
uv pip install opik
```

## Configuration

Configure the Python SDK by running the `opik configure` command. This will prompt you for your Opik server address (for self-hosted instances) or your API key and workspace (for Comet.com):

```bash
opik configure
```

You can also configure the SDK programmatically in your Python code:
```python
import opik

# For Comet.com Cloud
opik.configure(
    api_key="YOUR_API_KEY",
    workspace="YOUR_WORKSPACE", # Usually found in your Comet URL: https://www.comet.com/YOUR_WORKSPACE/...
    project_name="optional-project-name" # Optional: set a default project for traces
)

# For self-hosted Opik instances
# opik.configure(use_local=True, project_name="optional-project-name")
```
Refer to the [Python SDK documentation](https://www.comet.com/docs/opik/python-sdk-reference/) for more configuration options.

### Dynamic Tracing Control

Control tracing behavior at runtime without code changes:

```python
import opik

# Disable tracing globally
opik.set_tracing_active(False)

# Check current state
print(opik.is_tracing_active())  # False

# Re-enable tracing
opik.set_tracing_active(True)

# Reset to configuration default
opik.reset_tracing_to_config_default()
```

This is useful for:
- Performance optimization in high-throughput systems
- Conditional tracing based on user type or request parameters
- Debugging and troubleshooting without redeployment
- Implementing sampling strategies
- Calls already in progress when you disable tracing still finish logging.

See `examples/dynamic_tracing_cookbook.py` for comprehensive usage patterns.

## Basic Usage: Tracing

The easiest way to log traces is to use the `@opik.track` decorator:

```python
import opik

# Ensure Opik is configured (see Configuration section above)
# opik.configure(...)

@opik.track
def my_llm_function(user_question: str) -> str:
    # Your LLM call or business logic here
    # For example:
    # response = openai.ChatCompletion.create(...)
    response = f"Echoing: {user_question}"

    # You can add metadata to your trace
    opik.set_tags(["example", "basic-usage"])
    opik.log_metadata({"question_length": len(user_question)})

    return response

my_llm_function("Hello, Opik!")
```
Traces will appear in your configured Opik project. Opik also offers many direct [integrations](https://www.comet.com/docs/opik/integrations/overview/) for popular LLM frameworks.

## CLI Commands

Opik provides powerful CLI commands for exporting and importing data between projects:

- **Export**: Export traces, datasets, and prompts from projects to local JSON files
- **Import**: Import data from local files into projects
- **Migration**: Move data between projects or environments
- **Backup**: Create local backups of your project data

For detailed information about the CLI export/import functionality, see [Import/Export Commands](../../apps/opik-documentation/documentation/fern/docs/tracing/import_export_commands.mdx).

## Development & Contribution Guidelines

For a more general contribution guide (backend + frontend + SDK) see our root [Contribution guide](../../CONTRIBUTING.md).

# Coding guidelines
This guide is still in progress, however, it already contains useful information that you should know before submitting your PR.

## General
We care a lot about the code maintainability. Well-organized logic which is easy to extend, re-factor and, most importantly - **read**, is what we are striving for.
1. Follow [SOLID](https://realpython.com/solid-principles-python/) principles. Pay special attention to the "Single Responsibility" one.
2. Avoid large modules, large classes, and large functions. Separate the code properly and describe this separation with names, not with comments. (See [1])
3. If the name is not used outside of the class/module - it should be `_protected`.
4. Don't violate the access rules! We know that Python allows you to access _protected/__private variables, but in Opik we are quite strict about not abusing that, whether it's an internal code or a test (don't forget about [3]!).
5. Use comments only for something non-trivial that is hard to describe in any other way. Apart from these cases, comments should be used to answer the question "Why?" not "What?".

## Imports
1. Import module - not name.
    Instead of this:
    ```python
    from threading import Thread  # bad!
    thread = Thread()
    ```
    do this:
    ```python
    import threading  # good!
    thread = threading.Thread
    ```

2. If the import statement is too big, you can do the following
    ```python
    from opik.rest_api.core import error as rest_api_error  # ok!
    ```

3. If you are working in the namespace, you likely don't need to keep most of the parent namespaces
    ```python
    # inside opik.api_objects.dataset
    from . import dataset_item  # ok!
    ```

4. Of course, there might be exceptions from this rule, for example, some common types can be imported as is.
    ```python
    from typing import Dict, List  # ok!
    from opik.types import FeedbackScoreDict  # ok!
    ```

## Naming
1. Avoid abbreviations. In the vast majority of cases, it is not a problem to use variable names. People spend more time understanding what "fs" means than reading the word "files" or "file_system".
   ```python
   for d in dataset_items:  # bad!

   for item in dataset_items:  # ok!
       ...
   for dataset_item in dataset_items  # ok!
       ...
   ```
2. Avoid creating modules like `utils.py`, `helpers.py`, `misc.py` etc. Especially in the big namespaces. They can quickly become dumps where people put everything that they haven't been able to create a better place for in 10 seconds after they started thinking about it. You can create those files though, but they should be localized in their namespaces designed for some specific features. In vast majority of cases there are better module names.

## Testing
We highly encourage writing tests and we develop a lot of features in a test-driven way.
1. Test public API, don't violate privacy.
2. If you are an external contributor - make sure that the unit tests and e2e tests are green (they can be executed anywhere because they don't require any API keys or permissions). For internal Opik developers everything should be green in the CI.
3. If you have `if-statements` in your code or some non-trivial boiler-plate code - it's probably a reason to think about add some unit tests for that. The more complex your code, the higher chance you'll be asked to provide unit tests for it.
4. If you are introducing a new feature that includes communication with the backend - it's better to add some e2e tests for that (at least the happy flow one).
5. Avoid testing with e2e tests something that can be tested with unit tests. E2E tests are time-consuming.
6. If you are introducing a change in one of the integrations (or a new integration), make sure the integration tests are working. They usually require API keys configured for the services the integration works with. When the external contributor opens a PR, their tests will not use our Github secrets so consider providing your repo with an API key required for the integration. In that case, we will see that the tests are green.
7. We are using `fake_backend` fixture together with a special Opik assertions DSL(domain-specific language) for a lot of unit tests and library integration tests. We encourage you to use it as well! There is plenty of examples, you can take a look at `tests/unit/decorator/test_tracker_outputs.py` or `tests/library_integration/openai/test_openai.py`. It provides a pretty simple API for specifying the traces content you expect your feature to log.

```

### File: sdks\python\setup.py
```py
import os

from setuptools import find_packages, setup

project_urls = {"Source code": "https://github.com/comet-ml/opik"}

HERE = os.path.abspath(os.path.dirname(__file__))
version = os.environ.get("VERSION")
if version is None:
    version_file = os.path.join(HERE, "..", "..", "version.txt")
    if os.path.exists(version_file):
        with open(version_file) as fp:
            version = fp.read().strip()
    else:
        version = "0.0.1"

setup(
    author="Comet ML Inc.",
    author_email="mail@comet.com",
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],
    description="Comet tool for logging and evaluating LLM traces",
    long_description=open(
        os.path.join(HERE, "..", "..", "README.md"), encoding="utf-8"
    ).read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "boto3-stubs[bedrock-runtime]>=1.34.110",
        "click",
        "httpx",  # some older version of openai/litellm are broken with httpx>=0.28.0
        "rapidfuzz>=3.0.0,<4.0.0",
        # LiteLLM dependency comments:
        # - Exclude litellm 1.75.0-1.75.5 (broken callbacks system)
        # - Exclude versions 1.77.2-1.77.4: introduce C++ compiler dependency (madoka), fixed in 1.77.5
        #   See: https://github.com/BerriAI/litellm/issues/14762
        # - Exclude versions 1.77.5-1.79.1: remove trace_id/parent_span_id passthrough, fixed in 1.79.2+
        #   See: https://github.com/BerriAI/litellm/pull/15529
        # Please keep this list in sync with the one in sdks/opik_optimizer/pyproject.toml
        "litellm>=1.79.2,!=1.75.0,!=1.75.1,!=1.75.2,!=1.75.3,!=1.75.4,!=1.75.5,!=1.77.3,!=1.77.4,!=1.77.5,!=1.77.7,!=1.78.0,!=1.78.2,!=1.78.3,!=1.78.4,!=1.78.5,!=1.78.6,!=1.78.7,!=1.79.0,!=1.79.1",
        "openai",
        "pydantic-settings>=2.0.0,<3.0.0,!=2.9.0",
        "pydantic>=2.0.0,<3.0.0",
        "pytest",
        "rich",
        "sentry_sdk>=2.0.0",
        "tenacity",
        "tqdm",
        "uuid6",
        "jinja2",
    ],
    extras_require={
        "proxy": [
            "fastapi>=0.100.0",
            "uvicorn>=0.23.0",
        ],
    },
    entry_points={
        "pytest11": [
            "opik = opik.plugins.pytest.hooks",
        ],
        "console_scripts": ["opik = opik.cli:cli"],
    },
    keywords="opik",
    name="opik",
    include_package_data=True,
    package_data={"opik": ["py.typed"]},
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://www.comet.com",
    project_urls=project_urls,
    version=version,
    zip_safe=False,
    license="Apache 2.0 License",
)

```

### File: sdks\python\design\README.md
```md
# Opik Python SDK Design Documentation

Comprehensive architecture documentation for contributors and team members. These guides explain how the SDK works internally, not how to use it.

## 📚 Documentation

| Document | Priority | Description |
|----------|----------|-------------|
| **[API and Data Flow](API_AND_DATA_FLOW.md)** | ⭐ Start Here | Core architecture, 3 layers, sync vs async operations, batching, message processing |
| **[Testing](TESTING.md)** | 🔵 Essential | Test categories, fake backend, TraceModel/SpanModel patterns |
| **[Integrations](INTEGRATIONS.md)** | 🟣 As Needed | Integration patterns (method patching, callback, hybrid), streaming strategies |
| **[Evaluation](EVALUATION.md)** | 🟣 As Needed | Evaluation engine, all 4 evaluation methods, metrics architecture |

## 🚀 Quick Start

### First-Time Contributors

1. Read **[API and Data Flow](API_AND_DATA_FLOW.md)** - Understand core architecture
2. Read **[Testing](TESTING.md)** - Learn testing patterns
3. Choose domain doc based on your task

### By Task

| Task | Document | Key Sections |
|------|----------|--------------|
| Understanding `@opik.track` | [API and Data Flow](API_AND_DATA_FLOW.md) | Decorator Data Flow, Context Management |
| Adding integration | [Integrations](INTEGRATIONS.md) | Integration Patterns, existing integrations |
| Creating metric, evaluation pipelines | [Evaluation](EVALUATION.md) | Metrics Architecture |
| Debugging performance | [API and Data Flow](API_AND_DATA_FLOW.md) | Batching System, Performance |
| Writing tests | [Testing](TESTING.md) | Testing Patterns, fake backend |

## 🔄 Maintenance

**Update documentation when**:
- Major architectural changes
- New patterns introduced
- New integrations added
- Performance optimizations

**Quality standards**:
- Accurate (reflects codebase)
- Clear (easy for newcomers)
- Practical (real examples)

---

**Last Updated**: 2025-01-20

**Questions?** Open an issue or contact the SDK team.

```

### File: .pre-commit-config.yaml
```yaml
---
repos:
  - repo: local
    hooks:
      - id: helm-docs
        name: helm-docs
        language: docker_image
        entry: jnorwood/helm-docs:v1.14.2
        args:
          - --chart-search-root=deployment/helm_chart/opik
        files: (README\.md\.gotmpl|values\.yaml|Chart\.yaml)$
        pass_filenames: false

...

```

### File: AGENTS.md
```md
# Repository Guidelines

## Scope & Inheritance
- This is the canonical monorepo guide for shared contribution policy.
- Module-level `AGENTS.md` files should keep only module-specific guidance and reference this file for shared rules.

## Project Structure & Module Organization
This repository is a multi-module Opik codebase. Main areas:
- `apps/opik-backend`: Java backend (source in `src/main/java`, tests in `src/test/java`).
- `apps/opik-frontend`: React/TypeScript frontend (`src` and related assets/config).
- `apps/opik-documentation`: documentation website and generated API docs.
- `sdks/python`, `sdks/typescript`, `sdks/opik_optimizer`: SDK packages and examples.
- `deployment`, `scripts`, `extensions`: infra, tooling, and integration extension points.
- `tests_end_to_end`, `tests_load`: cross-stack and performance test suites.

## Build, Test, and Development Commands
- `./opik.sh` — run default local stack via Docker.
- `./opik.sh --build` — rebuild images and run the full stack.
- `./opik.sh --verify` — run stack health checks.
- `./opik.sh --stop` — stop local services.
- `scripts/dev-runner.sh` — fast local process mode (BE + FE).
- `scripts/dev-runner.sh --be-only-restart` — backend-focused local development.
- `scripts/dev-runner.sh --build-be` / `--build-fe` — build one side only.
- `scripts/dev-runner.sh --lint-be` — Java lint/format checks.
- `scripts/dev-runner.sh --lint-fe` — frontend lint/type checks via `npm`.
- `cd apps/opik-frontend && npm run lint && npm run test` — run ESLint + Vitest.
- `cd apps/opik-frontend && npm run build` — production frontend build.
- `cd apps/opik-backend && mvn test` — backend unit/integration tests.
- `cd apps/opik-backend && mvn spotless:apply` — apply Java formatting.
- `cd sdks/python && pip install -r tests/test_requirements.txt && pip install -r tests/unit/test_requirements.txt && pytest tests/unit tests/e2e` — Python SDK test suites.
- `make precommit-sdks` — run module-specific pre-commit checks across all SDKs from their local docs (do not duplicate SDK-specific command lines in multiple places).
- `cd sdks/typescript && npm run lint && npm run test && npm run build` — TS SDK checks.
- `cd tests_end_to_end/typescript-tests && TEST_SUITE=sanity npm test` — cross-stack Playwright sanity suite.

## Coding Style & Naming Conventions
- Use existing module formatters/conventions and keep edits scoped; avoid blanket reformatting.
- For detailed coding rules, defer to module-level `AGENTS.md` files and skill docs (for example `.agents/skills/python-sdk/good-code.md`) instead of duplicating style guidance here.

## Testing Guidelines
- Frameworks: Vitest (frontend + TS SDK), Playwright (frontend E2E), Maven/JUnit (backend), pytest (Python SDK).
- Naming conventions:
  - Java: `*Test.java` in `apps/opik-backend/src/test/java`.
  - Python: `test_*.py` grouped under `tests/unit`, `tests/integration`, `tests/e2e`.
  - TypeScript/JS: `*.test.ts` under `tests`.
- Cover changed behavior with unit tests first; add integration/E2E when cross-layer behavior changes.
- For SDK integration tests requiring external services, document any required keys in the PR.
- For end-to-end execution across backend/frontend, use:
  - `./opik.sh` or `scripts/dev-runner.sh` to start local services
  - `tests_end_to_end/typescript-tests/README.md` for suite-specific command and helper-service setup

## Agent Contribution Workflow
- This repository is a monorepo; submodule `AGENTS.md` files inherit this workflow by default.
- Read `CONTRIBUTING.md` and `.github/pull_request_template.md` before editing or opening a PR.
- Link tracked work in PRs with `Fixes #<id>` or `Resolves #<id>`.
- Use GitHub CLI for PR flow and prefer draft PRs first (`gh pr create --draft`).
- Prefer worktrees for parallel workstreams when touching multiple components.
- Run relevant unit tests and formatters for the touched area before requesting review.

## Commit & Pull Request Guidelines
- PR title and first commit should use semantic style with ticket prefix: `[OPIK-1234] [COMPONENT] feat|fix|refactor|docs: short summary`.
- Follow existing component prefixes (`[FE]`, `[SDK]`, `[DOCS]`, `[NA]`, `[INFRA]`, etc.).
- PR descriptions should include: change summary, test coverage run, and linked issue references (`Resolves #...`).
- Follow `pull_request_template.md` sections: Details, checklist, Issues, Testing, Documentation.
- Include screenshots or short recordings for user-visible UI changes when possible.

## Ignored Surfaces
- `.github/instructions/` contains GitHub Copilot-specific instruction files. Other agents should ignore this directory and use `.agents/` as the canonical source.
- `.github/copilot-instructions.md` is GitHub Copilot code review guidance only.

## Security & Configuration Tips
- Keep secrets and API keys out of source control; use local `.env` or shell variables.
- For local self-hosted testing, ensure dependencies are configured (MySQL, ClickHouse, Redis) before running backend tests.
- Prefer `opik configure --use_local` when running SDK examples against your local deployment.

## Generated Files
- `apps/opik-backend/src/main/resources/model_prices_and_context_window.json` and `apps/opik-frontend/src/data/model_prices_and_context_window.json` are generated artifacts.
- Do not edit these files directly; updates should come from the repository updater automation.

```

### File: CHANGELOG.md
```md
# Changelog

> **Note**: This changelog only contains breaking and critical changes for self-hosted deployments. For a complete changelog, please see our [official changelog](https://www.comet.com/docs/opik/changelog).

### Release 1.7.15, 2025-05-05

#### Critical Changes
- Updated port mapping when using `opik.sh` - This may affect existing deployments
- Fixed persistence when using Docker compose deployments - Requires reconfiguration for existing deployments

### Release 1.7.11, 2025-04-21

#### Security Change
- Updated Dockerfiles to ensure all containers run as non root users - This is a security-critical change that requires container recreation

### Release 1.7.0, 2025-04-09 [#](https://www.comet.com/docs/opik/self-host/local_deployment#troubleshooting)

#### Backward Incompatible Change

In this release, we migrated the Clickhouse table engines to their replicated version. The migration was automated, and we don't expect any errors. However, if you have any issues, please check [this link](https://www.comet.com/docs/opik/self-host/local_deployment#troubleshooting) or feel free to open an issue in this repository.

### Release 1.0.3, 2024-10-29 [#](apps/opik-backend/data-migrations/1.0.3/README.md)

#### Backward Incompatible Change

The structure of dataset items has changed to include new dynamic fields. Dataset items logged before version 1.0.3 will still show but would not be searchable. 
If you would like to migrate previous dataset items to the new format, please see the instructions below: [dataset item migration](apps/opik-backend/data-migrations/1.0.3/README.md) for more information*.

### Release 1.0.2, 2024-10-21

#### Backward Incompatible Change
- Updated datasets to support more flexible data schema - This change affects how dataset items are structured and may require updates to existing dataset insertion code. See [Dataset Documentation](https://www.comet.com/docs/opik/datasets/overview) for details.
- The `context` field is now optional in the [Hallucination metric](https://www.comet.com/docs/opik/evaluation/metrics/overview#hallucination) - This may affect existing evaluation configurations

### Release 1.0.1, 2024-09-30

#### Backward Incompatible Change
- Changed dataset item insertion behavior - Duplicate items are now silently ignored instead of being ingested, which may affect data collection workflows. See [Dataset Documentation](https://www.comet.com/docs/opik/datasets/overview) for details.

### Release 1.0.0, 2024-11-25

#### Backward Incompatible Change
- Updated OpenAI integration to track structured output calls using `beta.chat.completions.parse` - This may affect existing OpenAI integration code. See [OpenAI Integration Documentation](https://www.comet.com/docs/opik/integrations/openai) for details.
- Fixed issue with `update_current_span` and `update_current_trace` that did not support updating the `output` field - This may affect existing trace update code. See [Tracing Documentation](https://www.comet.com/docs/opik/tracing/overview) for details.

### Release 1.0.0, 2025-03-17

#### Backward Incompatible Change
- Added support for images in google.genai calls - This may affect existing Gemini integration code. See [Gemini Integration Documentation](https://www.comet.com/docs/opik/integrations/gemini) for details.
- [LangFlow integration](https://github.com/langflow-ai/langflow/pull/6928) has been merged - This may affect existing LangFlow deployments



```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
