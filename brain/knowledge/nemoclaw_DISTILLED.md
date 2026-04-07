---
id: nemoclaw
type: knowledge
owner: OA_Triage
---
# nemoclaw
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "nemoclaw",
  "version": "0.1.0",
  "description": "NemoClaw — run OpenClaw inside OpenShell with NVIDIA inference",
  "license": "Apache-2.0",
  "bin": {
    "nemoclaw": "./bin/nemoclaw.js"
  },
  "scripts": {
    "test": "vitest run",
    "lint": "eslint .",
    "lint:fix": "eslint . --fix",
    "format": "prettier --write 'bin/**/*.js' 'test/**/*.js'",
    "format:check": "prettier --check 'bin/**/*.js' 'test/**/*.js'",
    "typecheck": "tsc -p jsconfig.json",
    "build:cli": "tsc -p tsconfig.src.json",
    "typecheck:cli": "tsc -p tsconfig.cli.json",
    "prepare": "if command -v tsc >/dev/null 2>&1 || [ -x node_modules/.bin/tsc ]; then npm run build:cli; fi && npm install --omit=dev --ignore-scripts 2>/dev/null || true && if [ -d .git ]; then if command -v prek >/dev/null 2>&1; then prek install; elif [ -d node_modules/@j178/prek ]; then echo \"ERROR: prek package found but binary not in PATH\" && exit 1; else echo \"Skipping git hook setup (prek not installed)\"; fi; fi",
    "prepublishOnly": "cd nemoclaw && env -u npm_config_global -u npm_config_prefix -u npm_config_omit npm install --ignore-scripts && ./node_modules/.bin/tsc"
  },
  "dependencies": {
    "p-retry": "^4.6.2",
    "yaml": "^2.8.3"
  },
  "bundleDependencies": [
    "p-retry"
  ],
  "files": [
    "bin/",
    "nemoclaw/dist/",
    "nemoclaw/openclaw.plugin.json",
    "nemoclaw/package.json",
    "nemoclaw-blueprint/",
    "scripts/",
    "Dockerfile",
    ".dockerignore"
  ],
  "engines": {
    "node": ">=22.16.0"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/NVIDIA/NemoClaw.git"
  },
  "devDependencies": {
    "@commitlint/cli": "^20.5.0",
    "@commitlint/config-conventional": "^20.5.0",
    "@eslint/js": "^10.0.1",
    "@j178/prek": "^0.3.6",
    "@types/node": "^25.5.0",
    "@vitest/coverage-v8": "^4.1.0",
    "eslint": "^10.1.0",
    "execa": "^9.6.1",
    "prettier": "^3.8.1",
    "tsx": "^4.21.0",
    "typescript": "^6.0.2",
    "vitest": "^4.1.0"
  }
}

```

### File: README.md
```md
# 🦞 NVIDIA NemoClaw: Reference Stack for Running OpenClaw in OpenShell

<!-- start-badges -->
[![License](https://img.shields.io/badge/License-Apache_2.0-blue)](https://github.com/NVIDIA/NemoClaw/blob/main/LICENSE)
[![Security Policy](https://img.shields.io/badge/Security-Report%20a%20Vulnerability-red)](https://github.com/NVIDIA/NemoClaw/blob/main/SECURITY.md)
[![Project Status](https://img.shields.io/badge/status-alpha-orange)](https://github.com/NVIDIA/NemoClaw/blob/main/docs/about/release-notes.md)
[![Discord](https://img.shields.io/badge/Discord-Join-7289da)](https://discord.gg/XFpfPv9Uvx)
<!-- end-badges -->

<!-- start-intro -->
NVIDIA NemoClaw is an open source reference stack that simplifies running [OpenClaw](https://openclaw.ai) always-on assistants more safely.
It installs the [NVIDIA OpenShell](https://github.com/NVIDIA/OpenShell) runtime, part of NVIDIA Agent Toolkit, which provides additional security for running autonomous agents.
<!-- end-intro -->

> **Alpha software**
>
> NemoClaw is available in early preview starting March 16, 2026.
> This software is not production-ready.
> Interfaces, APIs, and behavior may change without notice as we iterate on the design.
> The project is shared to gather feedback and enable early experimentation.
> We welcome issues and discussion from the community while the project evolves.

NemoClaw adds guided onboarding, a hardened blueprint, state management, messaging bridges, routed inference, and layered protection on top of the [NVIDIA OpenShell](https://github.com/NVIDIA/OpenShell) runtime. For the full feature list, refer to [Overview](https://docs.nvidia.com/nemoclaw/latest/about/overview.html). For the system diagram, component model, and blueprint lifecycle, refer to [How It Works](https://docs.nvidia.com/nemoclaw/latest/about/how-it-works.html) and [Architecture](https://docs.nvidia.com/nemoclaw/latest/reference/architecture.html).

## Getting Started

Follow these steps to install NemoClaw and run your first sandboxed OpenClaw agent.

<!-- start-quickstart-guide -->

### Prerequisites

Before getting started, check the prerequisites to ensure you have the necessary software and hardware to run NemoClaw.

#### Hardware

| Resource | Minimum        | Recommended      |
|----------|----------------|------------------|
| CPU      | 4 vCPU         | 4+ vCPU          |
| RAM      | 8 GB           | 16 GB            |
| Disk     | 20 GB free     | 40 GB free       |

The sandbox image is approximately 2.4 GB compressed. During image push, the Docker daemon, k3s, and the OpenShell gateway run alongside the export pipeline, which buffers decompressed layers in memory. On machines with less than 8 GB of RAM, this combined usage can trigger the OOM killer. If you cannot add memory, configuring at least 8 GB of swap can work around the issue at the cost of slower performance.

#### Software

| Dependency | Version                          |
|------------|----------------------------------|
| Linux      | Ubuntu 22.04 LTS or later |
| Node.js    | 22.16 or later |
| npm        | 10 or later |
| Container runtime | Supported runtime installed and running |
| [OpenShell](https://github.com/NVIDIA/OpenShell) | Installed |

#### Container Runtimes

| Platform | Supported runtimes | Notes |
|----------|--------------------|-------|
| Linux | Docker | Primary supported path. |
| macOS (Apple Silicon) | Colima, Docker Desktop | Install Xcode Command Line Tools (`xcode-select --install`) and start the runtime before running the installer. |
| macOS (Intel) | Podman | Not supported yet. Depends on OpenShell support for Podman on macOS. |
| Windows WSL | Docker Desktop (WSL backend) | Supported target path. |
| DGX Spark | Docker | Refer to the [DGX Spark setup guide](https://github.com/NVIDIA/NemoClaw/blob/main/spark-install.md) for cgroup v2 and Docker configuration. |

### Install NemoClaw and Onboard OpenClaw Agent

Download and run the installer script.
The script installs Node.js if it is not already present, then runs the guided onboard wizard to create a sandbox, configure inference, and apply security policies.

> **ℹ️ Note**
>
> NemoClaw creates a fresh OpenClaw instance inside the sandbox during the onboarding process.

```bash
curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash
```

If you use nvm or fnm to manage Node.js, the installer may not update your current shell's PATH.
If `nemoclaw` is not found after install, run `source ~/.bashrc` (or `source ~/.zshrc` for zsh) or open a new terminal.

When the install completes, a summary confirms the running environment:

```text
──────────────────────────────────────────────────
Sandbox      my-assistant (Landlock + seccomp + netns)
Model        nvidia/nemotron-3-super-120b-a12b (NVIDIA Endpoints)
──────────────────────────────────────────────────
Run:         nemoclaw my-assistant connect
Status:      nemoclaw my-assistant status
Logs:        nemoclaw my-assistant logs --follow
──────────────────────────────────────────────────

[INFO]  === Installation complete ===
```

### Chat with the Agent

Connect to the sandbox, then chat with the agent through the TUI or the CLI.

```bash
nemoclaw my-assistant connect
```

In the sandbox shell, open the OpenClaw terminal UI and start a chat:

```bash
openclaw tui
```

Alternatively, send a single message and print the response:

```bash
openclaw agent --agent main --local -m "hello" --session-id test
```

### Uninstall

To remove NemoClaw and all resources created during setup, run the uninstall script:

```bash
curl -fsSL https://raw.githubusercontent.com/NVIDIA/NemoClaw/refs/heads/main/uninstall.sh | bash
```

| Flag               | Effect                                              |
|--------------------|-----------------------------------------------------|
| `--yes`            | Skip the confirmation prompt.                       |
| `--keep-openshell` | Leave the `openshell` binary installed.              |
| `--delete-models`  | Also remove NemoClaw-pulled Ollama models.           |

For troubleshooting installation or onboarding issues, see the [Troubleshooting guide](https://docs.nvidia.com/nemoclaw/latest/reference/troubleshooting.html).

<!-- end-quickstart-guide -->

## Documentation

Refer to the following pages on the official documentation website for more information on NemoClaw.

| Page | Description |
|------|-------------|
| [Overview](https://docs.nvidia.com/nemoclaw/latest/about/overview.html) | What NemoClaw does and how it fits together. |
| [How It Works](https://docs.nvidia.com/nemoclaw/latest/about/how-it-works.html) | Plugin, blueprint, sandbox lifecycle, and protection layers. |
| [Architecture](https://docs.nvidia.com/nemoclaw/latest/reference/architecture.html) | Plugin structure, blueprint lifecycle, sandbox environment, and host-side state. |
| [Inference Options](https://docs.nvidia.com/nemoclaw/latest/inference/inference-options.html) | Supported providers, validation, and routed inference configuration. |
| [Network Policies](https://docs.nvidia.com/nemoclaw/latest/reference/network-policies.html) | Baseline rules, operator approval flow, and egress control. |
| [Customize Network Policy](https://docs.nvidia.com/nemoclaw/latest/network-policy/customize-network-policy.html) | Static and dynamic policy changes, presets. |
| [Security Best Practices](https://docs.nvidia.com/nemoclaw/latest/security/best-practices.html) | Controls reference, risk framework, and posture profiles for sandbox security. |
| [Sandbox Hardening](https://docs.nvidia.com/nemoclaw/latest/deployment/sandbox-hardening.html) | Container security measures, capability drops, process limits. |
| [CLI Commands](https://docs.nvidia.com/nemoclaw/latest/reference/commands.html) | Full NemoClaw CLI command reference. |
| [Troubleshooting](https://docs.nvidia.com/nemoclaw/latest/reference/troubleshooting.html) | Common issues and resolution steps. |

## Project Structure

The following directories make up the NemoClaw repository.

```text
NemoClaw/
├── bin/              # CLI entry point and library modules (CJS)
├── nemoclaw/         # TypeScript plugin (Commander CLI extension)
│   └── src/
│       ├── blueprint/    # Runner, snapshot, SSRF validation, state
│       ├── commands/     # Slash commands, migration state
│       └── onboard/      # Onboarding config
├── nemoclaw-blueprint/   # Blueprint YAML and network policies
├── scripts/          # Install helpers, setup, automation
├── test/             # Integration and E2E tests
└── docs/             # User-facing docs (Sphinx/MyST)
```

## Community

Join the NemoClaw community to ask questions, share feedback, and report issues.

- [Discord](https://discord.gg/XFpfPv9Uvx)
- [GitHub Discussions](https://github.com/NVIDIA/NemoClaw/discussions)
- [GitHub Issues](https://github.com/NVIDIA/NemoClaw/issues)

## Contributing

We welcome contributions. See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup, coding standards, and the PR process.

## Security

NVIDIA takes security seriously.
If you discover a vulnerability in NemoClaw, **DO NOT open a public issue.**
Use one of the private reporting channels described in [SECURITY.md](SECURITY.md):

- Submit a report through the [NVIDIA Vulnerability Disclosure Program](https://www.nvidia.com/en-us/security/report-vulnerability/).
- Send an email to [psirt@nvidia.com](mailto:psirt@nvidia.com) encrypted with the [NVIDIA PGP key](https://www.nvidia.com/en-us/security/pgp-key).
- Use [GitHub's private vulnerability reporting](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configuring-private-vulnerability-reporting-for-a-repository) to submit a report directly on this repository.

For security bulletins and PSIRT policies, visit the [NVIDIA Product Security](https://www.nvidia.com/en-us/security/) portal.

## Notice and Disclaimer

This software automatically retrieves, accesses or interacts with external materials. Those retrieved materials are not distributed with this software and are governed solely by separate terms, conditions and licenses. You are solely responsible for finding, reviewing and complying with all applicable terms, conditions, and licenses, and for verifying the security, integrity and suitability of any retrieved materials for your specific use case. This software is provided "AS IS", without warranty of any kind. The author makes no representations or warranties regarding any retrieved materials, and assumes no liability for any losses, damages, liabilities or legal consequences from your use or inability to use this software or any retrieved materials. Use this software and the retrieved materials at your own risk.

## License

Apache 2.0. See [LICENSE](LICENSE).

```

### File: k8s\README.md
```md
# NemoClaw on Kubernetes

> **⚠️ Experimental**: This deployment method is intended for **trying out NemoClaw on Kubernetes**, not for production use. It requires a **privileged pod** running **Docker-in-Docker (DinD)** to create isolated sandbox environments. Operational requirements (storage, runtime, security policies) vary by cluster configuration.

Run [NemoClaw](https://github.com/NVIDIA/NemoClaw) on Kubernetes with GPU inference powered by [Dynamo](https://github.com/ai-dynamo/dynamo) or any OpenAI-compatible endpoint.

---

## Quick Start

### Prerequisites

- Kubernetes cluster with `kubectl` access
- An OpenAI-compatible inference endpoint (Dynamo vLLM, vLLM, etc.)
- Permissions to create **privileged pods** (required for Docker-in-Docker)
- Sufficient node resources (~8GB memory, 2 CPUs for DinD container)

### 1. Deploy NemoClaw

```bash
kubectl create namespace nemoclaw
kubectl apply -f https://raw.githubusercontent.com/NVIDIA/NemoClaw/main/k8s/nemoclaw-k8s.yaml
```

### 2. Check Logs

```bash
kubectl logs -f nemoclaw -n nemoclaw -c workspace
```

Wait for "Onboard complete" message.

### 3. Connect to Your Sandbox

```bash
kubectl exec -it nemoclaw -n nemoclaw -c workspace -- nemoclaw my-assistant connect
```

You're now inside a secure sandbox with an AI agent ready to help.

---

## Configuration

Edit the environment variables in `nemoclaw-k8s.yaml` before deploying:

| Variable | Required | Description |
|----------|----------|-------------|
| `DYNAMO_HOST` | Yes | Inference endpoint for socat proxy (e.g., `vllm-frontend.dynamo.svc:8000`) |
| `NEMOCLAW_ENDPOINT_URL` | Yes | URL the sandbox uses (usually `http://host.openshell.internal:8000/v1`) |
| `COMPATIBLE_API_KEY` | Yes | API key (use `dummy` for Dynamo/vLLM) |
| `NEMOCLAW_MODEL` | Yes | Model name (e.g., `meta-llama/Llama-3.1-8B-Instruct`) |
| `NEMOCLAW_SANDBOX_NAME` | No | Sandbox name (default: `my-assistant`) |

### Example: Custom Endpoint

```yaml
env:
  - name: DYNAMO_HOST
    value: "my-vllm.my-namespace.svc.cluster.local:8000"
  - name: NEMOCLAW_ENDPOINT_URL
    value: "http://host.openshell.internal:8000/v1"
  - name: COMPATIBLE_API_KEY
    value: "dummy"
  - name: NEMOCLAW_MODEL
    value: "mistralai/Mistral-7B-Instruct-v0.3"
```

---

## Using NemoClaw

### Access the Workspace Shell

```bash
kubectl exec -it nemoclaw -n nemoclaw -c workspace -- bash
```

### Check Sandbox Status

```bash
kubectl exec nemoclaw -n nemoclaw -c workspace -- nemoclaw list
kubectl exec nemoclaw -n nemoclaw -c workspace -- nemoclaw my-assistant status
```

### Connect to Sandbox

```bash
kubectl exec -it nemoclaw -n nemoclaw -c workspace -- nemoclaw my-assistant connect
```

### Test Inference

From inside the sandbox:

```bash
curl -s https://inference.local/v1/models

curl -s https://inference.local/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"meta-llama/Llama-3.1-8B-Instruct","messages":[{"role":"user","content":"Hello!"}],"max_tokens":50}'
```

### Verify Local Inference

Confirm NemoClaw is using your Dynamo/vLLM endpoint:

```bash
# Check model from sandbox
kubectl exec -it nemoclaw -n nemoclaw -c workspace -- nemoclaw my-assistant connect
sandbox@my-assistant:~$ curl -s https://inference.local/v1/models
# Should show your model (e.g., meta-llama/Llama-3.1-8B-Instruct)

# Compare with Dynamo directly (from workspace)
kubectl exec nemoclaw -n nemoclaw -c workspace -- curl -s http://localhost:8000/v1/models
# Should show the same model

# Check provider configuration
kubectl exec nemoclaw -n nemoclaw -c workspace -- openshell inference get
# Shows: Provider: compatible-endpoint, Model: <your-model>

# Test the agent
sandbox@my-assistant:~$ openclaw agent --agent main -m "What is 7 times 8?"
# Should respond with 56
```

---

## Architecture

```text
┌─────────────────────────────────────────────────────────────────┐
│                     Kubernetes Cluster                          │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │                    NemoClaw Pod                           │  │
│  │                                                           │  │
│  │  ┌─────────────────┐    ┌─────────────────────────────┐   │  │
│  │  │ Docker-in-Docker│    │    Workspace Container      │   │  │
│  │  │                 │    │                             │   │  │
│  │  │  ┌───────────┐  │    │  nemoclaw CLI               │   │  │
│  │  │  │    k3s    │  │◄───│  openshell CLI              │   │  │
│  │  │  │  cluster  │  │    │                             │   │  │
│  │  │  │           │  │    │  socat proxy ───────────────│───│──┼──► Dynamo/vLLM
│  │  │  │ ┌───────┐ │  │    │  localhost:8000             │   │  │
│  │  │  │ │Sandbox│ │  │    │                             │   │  │
│  │  │  │ └───────┘ │  │    │  host.openshell.internal    │   │  │
│  │  │  └───────────┘  │    │  routes to socat            │   │  │
│  │  └─────────────────┘    └─────────────────────────────┘   │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

**How it works:**

1. NemoClaw runs in a privileged pod with Docker-in-Docker
2. OpenShell creates a nested k3s cluster for sandbox isolation
3. A socat proxy bridges K8s DNS to the nested environment
4. Inside the sandbox, `host.openshell.internal:8000` routes to the inference endpoint

---

## Troubleshooting

### Pod won't start

```bash
kubectl describe pod nemoclaw -n nemoclaw
```

Common issues:

- Missing privileged security context
- Insufficient memory (needs ~8GB for DinD)

### Docker daemon not starting

```bash
kubectl logs nemoclaw -n nemoclaw -c dind
```

Usually resolves after 30-60 seconds.

### Inference not working

Check socat is running:

```bash
kubectl exec nemoclaw -n nemoclaw -c workspace -- pgrep -a socat
```

Test endpoint directly:

```bash
kubectl exec nemoclaw -n nemoclaw -c workspace -- curl -s http://localhost:8000/v1/models
```

---

## Learn More

- [NemoClaw Documentation](https://docs.nvidia.com/nemoclaw)
- [OpenShell](https://github.com/NVIDIA/OpenShell)
- [Dynamo](https://github.com/ai-dynamo/dynamo)
- [OpenClaw](https://openclaw.ai)

```

### File: test\package.json
```json
{ "type": "module" }

```

### File: .coderabbit.yaml
```yaml
# yaml-language-server: $schema=https://coderabbit.ai/integrations/schema.v2.json
language: "en-US"
early_access: false
reviews:
  profile: "chill"
  request_changes_workflow: false
  high_level_summary: true
  poem: true
  review_status: true
  review_details: false
  auto_review:
    enabled: true
    drafts: false
  path_instructions:
    - path: "docs/**"
      instructions: |
        You are an editorial reviewer for NemoClaw documentation.
        Review every docs change against the style guide below. Flag violations
        inline as review comments. Do not rewrite the content — point out the
        issue and cite the relevant rule so the author can fix it.

        ## Voice and Tone

        - Active voice required. Flag passive constructions.
          Bad: "A gateway is created by the CLI."
          Good: "The CLI creates a gateway."
        - Second person ("you") when addressing the reader.
        - Present tense. Flag future tense ("will") in descriptions of current behavior.
        - No hedge words: flag "simply," "just," "easily," "of course."

        ## LLM-Generated Patterns (Flag These)

        These are common in AI-generated text and erode trust with technical readers.
        Flag every occurrence:

        - Unnecessary bold on routine instructions ("This is a **critical** step"
          when nothing is actually critical). Bold is reserved for UI labels,
          parameter names, and genuine warnings.
        - Excessive em dashes. One per paragraph is fine; multiple per paragraph
          or em dashes used instead of commas/periods should be flagged.
        - Superlatives and marketing language ("powerful," "robust," "seamless,"
          "cutting-edge"). Say what it does, not how great it is.
        - Emoji in documentation prose.
        - Rhetorical questions ("Want to secure your agents? Look no further!").
          State the purpose directly.
        - Filler introductions ("In this section, we will explore..."). Start
          with the content.

        ## Formatting Rules

        - Every sentence must end with a period.
        - One sentence per line in source (makes diffs readable). Flag paragraphs
          where multiple sentences appear on the same line.
        - CLI commands, file paths, flags, parameter names, and values must use
          inline `code` formatting.
        - CLI code blocks must use the `console` language tag with `$` prompt
          prefix. Flag ```bash or ```shell for CLI examples.
        - Use MyST admonitions (:::{tip}, :::{note}, :::{warning}) for callouts,
          not bold text or blockquotes.
        - No nested admonitions.
        - Do not number section titles. Flag "Section 1: ...", "Step 3: ...", etc.
        - No colons in titles. Flag "Inference: Cloud and Local" — should be
          "Cloud and Local Inference."
        - Colons should only introduce a list. Flag colons used as general
          punctuation between clauses.

        ## Word List (Flag Incorrect Usage)

        | Correct        | Incorrect (flag these)                              |
        |----------------|------------------------------------------------------|
        | NVIDIA         | Nvidia, nvidia                                       |
        | NemoClaw       | nemoclaw (in prose), Nemoclaw                        |
        | OpenClaw       | openclaw (in prose), Openclaw                        |
        | OpenShell      | Open Shell, openShell, Openshell, openshell (in prose)|
        | CLI            | cli, Cli                                             |
        | API key        | api key, API Key                                     |
        | mTLS           | MTLS, mtls                                           |
        | YAML           | yaml (in prose), Yaml                                |
        | gateway        | Gateway (unless starting a sentence)                 |
        | sandbox        | Sandbox (unless starting a sentence)                 |

        Words inside code blocks or inline code spans are exempt from the word
        list (e.g., `nemoclaw onboard` is correct).

        ## Page Structure

        When reviewing new pages, verify:
        - SPDX license header is present after frontmatter.
        - Frontmatter includes title, description, keywords, topics, tags,
          content type, difficulty, audience, and status fields.
        - H1 heading matches the `title.page` frontmatter value.
        - Page starts with a one- or two-sentence introduction.
        - Sections use H2 and H3, each starting with an introductory sentence.
        - A "Next Steps" section at the bottom links to related pages.

        ## Severity

        - Word list and voice violations: flag as suggestions.
        - Missing SPDX header, broken cross-references, or incorrect code
          block language: flag as issues.
        - LLM-generated patterns (bold overuse, em dashes, superlatives,
          hedge words): flag as suggestions with the note "LLM pattern detected."
    - path: "**/*.md"
      instructions: |
        This rule applies to all Markdown files project-wide. For files
        under docs/, the stricter docs/** rules defined earlier in this
        file take precedence; this rule adds baseline checks for every
        other Markdown file (README, CONTRIBUTING, architecture docs, etc.).

        - NVIDIA must be all caps (not Nvidia, nvidia).
        - NemoClaw, OpenClaw, and OpenShell must use correct casing.
        - No emoji in technical prose.
chat:
  auto_reply: true

```

### File: .markdownlint-cli2.yaml
```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

# markdownlint-cli2 configuration
# https://github.com/DavidAnson/markdownlint-cli2
#
# All default rules are enabled unless listed below.

config:
  default: true

  # --- Permanently disabled (style preferences) ---
  MD004: false  # ul-style — mixed */- is fine
  MD013: false  # line-length — 80-char limit too strict for docs prose
  MD014: false  # commands-show-output — $ prefix in code blocks is intentional
  MD024: false  # no-duplicate-heading — duplicate names in different sections are fine
  MD033: false  # no-inline-html — HTML in markdown is common on GitHub
  MD060: false  # table-column-style — table pipe spacing is cosmetic

  # --- Permanently disabled (false positives) ---
  # Front matter uses a complex `title:` object (with page/nav sub-keys),
  # not a plain title string. The default regex falsely matches it as an h1.
  MD025:
    front_matter_title: ""

ignores:
  - "node_modules/**"

```

### File: .pre-commit-config.yaml
```yaml
# NemoClaw — prek hook configuration
# prek: https://github.com/j178/prek — single binary, no Python required for the runner
# Installed as an npm devDependency (@j178/prek) — available after `npm install`.
# All git hooks (pre-commit, commit-msg, pre-push) are managed by prek via this file only.
# The "prepare" script in package.json runs `prek install` (writes `.git/hooks/*`).
# If you previously used Husky, run: git config --unset core.hooksPath
# then `npm install` again so Git uses the hooks prek installs.
#
# Usage:
#   npx prek install
#   npx prek run --all-files
#
# CI / diff-only runs:
#   npx prek run --from-ref <base> --to-ref HEAD
#
# Priority groups (prek runs same-priority hooks in parallel):
#   0  — General file fixers (whitespace, EOF, line endings)
#   4  — SPDX header insertion (--fix)
#   5  — Shell / TS formatters (shfmt, prettier)
#   6  — Fixes that should follow formatters (ruff check --fix, eslint --fix)
#  10  — Linters and read-only checks
#  20  — Project-level checks (vitest, coverage, ratchet)

exclude: ^(nemoclaw/dist/|nemoclaw/node_modules/|docs/_build/|\.venv/|uv\.lock$)

# Which git hook shims `prek install` writes (separate from each hook's `stages:`).
# https://prek.j178.dev/configuration/#default_install_hook_types
default_install_hook_types:
  - pre-commit
  - commit-msg
  - pre-push

repos:
  # ── Priority 0: general file fixers ───────────────────────────────────────
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v6.0.0
    hooks:
      - id: trailing-whitespace
        priority: 0
      - id: end-of-file-fixer
        priority: 0
      - id: mixed-line-ending
        args: ["--fix=lf"]
        priority: 0

  # ── Priority 0: reject force-added ignored files ───────────────────────────
  # Catches `git add -f` of files that .gitignore would normally block.
  # Single source of truth stays in .gitignore — no duplicate list here.
  - repo: local
    hooks:
      - id: no-force-added-ignored
        name: Reject force-added ignored files
        entry: bash -c 'IGNORED=$(git ls-files --ignored --exclude-standard --cached -- "$@") && if [ -n "$IGNORED" ]; then echo "Force-added files that .gitignore would block:" && echo "$IGNORED" && exit 1; fi' --
        language: system
        always_run: true
        pass_filenames: false
        priority: 0

  # ── Priority 4: SPDX headers (insert if missing; runs before language formatters) ──
  - repo: local
    hooks:
      - id: spdx-headers
        name: SPDX license headers (insert if missing)
        entry: bash scripts/check-spdx-headers.sh --fix
        language: system
        files: ^(nemoclaw/src/.*\.ts|scripts/.*\.ts|nemoclaw-blueprint/.*\.py|.*\.sh)$
        exclude: ^nemoclaw-blueprint/.*__init__\.py$
        pass_filenames: true
        priority: 4

  # ── Priority 5: formatters ────────────────────────────────────────────────
  - repo: https://github.com/scop/pre-commit-shfmt
    rev: v3.12.0-2
    hooks:
      - id: shfmt
        args:
          - -w
          - -i
          - "2"
          - -ci
          - -bn
        priority: 5

  - repo: local
    hooks:
      - id: prettier-plugin
        name: Prettier (plugin)
        entry: bash -c 'root="$(git rev-parse --show-toplevel)" && cd "$root/nemoclaw" && files=() && for f in "$@"; do files+=("${f#nemoclaw/}"); done && npx prettier --write "${files[@]}"' --
        language: system
        files: ^nemoclaw/.*\.ts$
        pass_filenames: true
        priority: 5

      - id: prettier-js
        name: Prettier (JavaScript)
        entry: npx prettier --write
        language: system
        files: ^(bin|test)/.*\.js$
        pass_filenames: true
        priority: 5

  # ── Priority 6: auto-fix after formatting ─────────────────────────────────
  - repo: local
    hooks:
      - id: eslint-plugin
        name: ESLint (plugin)
        entry: bash -c 'root="$(git rev-parse --show-toplevel)" && cd "$root/nemoclaw" && files=() && for f in "$@"; do files+=("${f#nemoclaw/}"); done && npx eslint --fix "${files[@]}"' --
        language: system
        files: ^nemoclaw/.*\.ts$
        pass_filenames: true
        priority: 6

  - repo: local
    hooks:
      - id: eslint-cli
        name: ESLint (CLI)
        entry: npx eslint --fix
        language: system
        files: ^(bin|test|scripts|docs/_ext)/.*\.js$
        pass_filenames: true
        priority: 6

  # ── Priority 10: linters and validation ─────────────────────────────────────
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v6.0.0
    hooks:
      - id: check-merge-conflict
        priority: 10
      - id: check-added-large-files
        args: ["--maxkb=2000"]
        priority: 10
      - id: check-case-conflict
        priority: 10
      - id: check-yaml
        priority: 10
      - id: check-toml
        priority: 10
      - id: check-json
        priority: 10
      - id: detect-private-key
        priority: 10
      - id: check-executables-have-shebangs
        priority: 10
      - id: check-shebang-scripts-are-executable
        priority: 10

  - repo: https://github.com/shellcheck-py/shellcheck-py
    rev: v0.11.0.1
    hooks:
      - id: shellcheck
        priority: 10

  - repo: local
    hooks:
      - id: hadolint
        name: hadolint
        entry: hadolint
        language: system
        files: (Dockerfile[^/]*|.*\.dockerfile)$
        types: [file]
        priority: 10

  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.30.1
    hooks:
      - id: gitleaks
        name: gitleaks (secret scan)
        priority: 10

  - repo: https://github.com/DavidAnson/markdownlint-cli2
    rev: v0.22.0
    hooks:
      - id: markdownlint-cli2
        priority: 10

  # ── commit-msg hooks ────────────────────────────────────────────────────────
  - repo: https://github.com/alessandrojcm/commitlint-pre-commit-hook
    rev: v9.24.0
    hooks:
      - id: commitlint
        stages: [commit-msg]
        additional_dependencies: ["@commitlint/config-conventional@20"]
        priority: 10

  # ── pre-push hooks ─────────────────────────────────────────────────────────
  - repo: local
    hooks:
      - id: tsc-plugin
        name: TypeScript (plugin)
        entry: bash -c 'cd nemoclaw && npx tsc --noEmit --incremental'
        language: system
        pass_filenames: false
        files: ^nemoclaw/
        stages: [pre-push]
        priority: 10

      - id: tsc-js
        name: TypeScript (JS config)
        entry: bash -c 'npm run build:cli && npx tsc -p jsconfig.json'
        language: system
        pass_filenames: false
        files: ^(bin|test|scripts)/.*\.js$
        stages: [pre-push]
        priority: 10

      - id: tsc-cli
        name: TypeScript (CLI)
        entry: npx tsc -p tsconfig.cli.json
        language: system
        pass_filenames: false
        files: ^(bin|scripts)/
        types_or: [ts, tsx]
        stages: [pre-push]
        priority: 10

      - id: version-tag-sync
        name: package.json ↔ git tag version sync
        entry: bash scripts/check-version-tag-sync.sh
        language: system
        always_run: true
        pass_filenames: false
        stages: [pre-push]
        priority: 10

  # ── Priority 20: project-level checks (coverage + ratchet) ─────────────────
  - repo: local
    hooks:
      - id: test-cli
        name: Test (CLI)
        entry: bash -c 'npm run build:cli && npx vitest run --project cli --coverage --coverage.reporter=text --coverage.reporter=json-summary --coverage.reportsDirectory=coverage/cli --coverage.include="bin/**/*.js" --coverage.include="dist/lib/**/*.js" --coverage.exclude="test/**/*.js" --coverage.exclude="test/**/*.ts" && npx tsx scripts/check-coverage-ratchet.ts coverage/cli/coverage-summary.json ci/coverage-threshold-cli.json "CLI coverage"'
        language: system
        pass_filenames: false
        files: ^(bin/|src/|test/)
        priority: 20

      - id: test-plugin
        name: Test (plugin)
        entry: bash -c 'npx vitest run --project plugin --coverage --coverage.reporter=text --coverage.reporter=json-summary --coverage.reportsDirectory=coverage/plugin --coverage.include="nemoclaw/src/**/*.ts" --coverage.exclude="**/*.test.ts" && npx tsx scripts/check-coverage-ratchet.ts coverage/plugin/coverage-summary.json ci/coverage-threshold-plugin.json "Plugin coverage"'
        language: system
        pass_filenames: false
        files: ^nemoclaw/
        priority: 20

default_language_version:
  python: python3

fail_fast: false

```

### File: AGENTS.md
```md
# AGENTS.md

## Project Context

NVIDIA NemoClaw runs OpenClaw AI assistants inside hardened OpenShell sandboxes with NVIDIA Nemotron inference. This file provides agent-specific guidance for working on this codebase.

## Quick Reference

| Task | Command |
|------|---------|
| Install all deps | `npm install && cd nemoclaw && npm install && npm run build && cd .. && cd nemoclaw-blueprint && uv sync && cd ..` |
| Run all tests | `npm test` |
| Run plugin tests | `cd nemoclaw && npm test` |
| Run all linters | `make check` |
| Type-check CLI | `npm run typecheck:cli` |
| Build plugin | `cd nemoclaw && npm run build` |
| Build docs | `make docs` |

## Key Architecture Decisions

### Dual-Language Stack

- **CLI and plugin**: JavaScript (CJS in `bin/`, ESM in `test/`) and TypeScript (`nemoclaw/src/`)
- **Blueprint**: YAML configuration (`nemoclaw-blueprint/`)
- **Docs**: Sphinx/MyST Markdown
- **Tooling scripts**: Bash and Python

The `bin/` directory uses CommonJS intentionally — it's the CLI entry point that must work without a build step. The `nemoclaw/` plugin uses TypeScript and requires compilation.

### Testing Strategy

Tests are organized into three Vitest projects defined in `vitest.config.ts`:

1. **`cli`** — `test/**/*.test.{js,ts}` — integration tests for CLI behavior
2. **`plugin`** — `nemoclaw/src/**/*.test.ts` — unit tests co-located with source
3. **`e2e-brev`** — `test/e2e/brev-e2e.test.js` — cloud E2E (requires `BREV_API_TOKEN`)

When writing tests:

- Root-level tests (`test/`) use ESM imports
- Plugin tests use TypeScript and are co-located with their source files
- Mock external dependencies; don't call real NVIDIA APIs in unit tests
- E2E tests run on ephemeral Brev cloud instances

### Security Model

NemoClaw isolates agents inside OpenShell sandboxes with:

- Network policies (`nemoclaw-blueprint/policies/`) controlling egress
- Credential sanitization to prevent leaks
- SSRF validation (`nemoclaw/src/blueprint/ssrf.ts`)
- Docker capability drops and process limits

Security-sensitive code paths require extra test coverage.

## Working with This Repo

### Before Making Changes

1. Read `CONTRIBUTING.md` for the full contributor guide
2. Run `make check` to verify your environment is set up correctly
3. Check that `npm test` passes before starting

### Common Patterns

**Adding a CLI command:**

- Entry point: `bin/nemoclaw.js` (routes to `bin/lib/` modules)
- Keep `bin/lib/` modules as CommonJS
- Add tests in `test/`

**Adding a plugin feature:**

- Source: `nemoclaw/src/`
- Co-locate tests as `*.test.ts`
- Build with `cd nemoclaw && npm run build`

**Adding a network policy preset:**

- Add YAML to `nemoclaw-blueprint/policies/presets/`
- Follow existing preset structure (see `slack.yaml`, `discord.yaml`)

**Updating docs:**

- Edit under `docs/` (never `.agents/skills/nemoclaw-*/*.md`)
- Regenerate skills: `python scripts/docs-to-skills.py docs/ .agents/skills/ --prefix nemoclaw`
- Preview: `make docs-live`

### Gotchas

- `npm install` at root triggers `prek install` which sets up git hooks. If hooks fail, check that `core.hooksPath` is unset: `git config --unset core.hooksPath`
- The `nemoclaw/` subdirectory has its own `package.json`, `node_modules/`, and ESLint config — it's a separate npm project
- SPDX headers are auto-inserted by pre-commit hooks; don't worry about adding them manually
- Coverage thresholds are ratcheted in `ci/coverage-threshold-*.json` — new code should not decrease CLI or plugin coverage
- The `.claude/skills` symlink points to `.agents/skills` — both paths resolve to the same content

```

### File: CLAUDE.md
```md
# CLAUDE.md

## Project Overview

NVIDIA NemoClaw is an open-source reference stack for running [OpenClaw](https://openclaw.ai) always-on assistants inside [NVIDIA OpenShell](https://github.com/NVIDIA/OpenShell) sandboxes with NVIDIA inference (Nemotron). It provides CLI tooling, a blueprint for sandbox orchestration, and security hardening.

**Status:** Alpha (March 2026+). Interfaces may change without notice.

## Architecture

| Path | Language | Purpose |
|------|----------|---------|
| `bin/` | JavaScript (CJS) | CLI entry point (`nemoclaw.js`) and library modules |
| `bin/lib/` | JavaScript (CJS) | Core CLI logic: onboard, credentials, inference, policies, preflight, runner |
| `nemoclaw/` | TypeScript | Plugin project (Commander CLI extension for OpenClaw) |
| `nemoclaw/src/blueprint/` | TypeScript | Runner, snapshot, SSRF validation, state management |
| `nemoclaw/src/commands/` | TypeScript | Slash commands, migration state |
| `nemoclaw/src/onboard/` | TypeScript | Onboarding config |
| `nemoclaw-blueprint/` | YAML | Blueprint definition and network policies |
| `scripts/` | Bash/JS/TS | Install helpers, setup, automation, E2E tooling |
| `test/` | JavaScript (ESM) | Root-level integration tests (Vitest) |
| `test/e2e/` | Bash/JS | End-to-end tests (Brev cloud instances) |
| `docs/` | Markdown (MyST) | User-facing docs (Sphinx) |
| `k8s/` | YAML | Kubernetes deployment manifests |

## Development Commands

```bash
# Install dependencies
npm install                              # root deps (OpenClaw + CLI)
cd nemoclaw && npm install && npm run build && cd ..  # TypeScript plugin
cd nemoclaw-blueprint && uv sync && cd ..             # Python deps

# Build
cd nemoclaw && npm run build      # compile TypeScript plugin
cd nemoclaw && npm run dev        # watch mode

# Test
npm test                          # root-level tests (Vitest)
cd nemoclaw && npm test           # plugin unit tests (Vitest)

# Lint / check
make check                        # all linters via prek (pre-commit hooks)
npx prek run --all-files          # same as make check
npm run typecheck:cli             # type-check CLI (bin/, scripts/)

# Format
make format                       # auto-format TypeScript

# Docs
make docs                         # build docs (Sphinx/MyST)
make docs-live                    # serve locally with auto-rebuild
```

## Test Structure

- **Root tests** (`test/*.test.js`): Integration tests run via Vitest (ESM)
- **Plugin tests** (`nemoclaw/src/**/*.test.ts`): Unit tests co-located with source
- **E2E tests** (`test/e2e/`): Cloud-based E2E on Brev instances, triggered only when `BREV_API_TOKEN` is set

Vitest config (`vitest.config.ts`) defines three projects: `cli`, `plugin`, and `e2e-brev`.

## Code Style and Conventions

### Commit Messages

Conventional Commits required. Enforced by commitlint via prek `commit-msg` hook.

```text
<type>(<scope>): <description>
```

Types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `ci`, `perf`, `merge`

### SPDX Headers

Every source file must include an SPDX license header. The pre-commit hook auto-inserts them:

```javascript
// SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
```

For shell scripts use `#` comments. For Markdown use HTML comments.

### JavaScript

- `bin/` and `scripts/`: **CommonJS** (`require`/`module.exports`), Node.js 22.16+
- `test/`: **ESM** (`import`/`export`)
- ESLint config in `eslint.config.mjs`
- Cyclomatic complexity limit: 20 (ratcheting down to 15)
- Unused vars pattern: prefix with `_`

### TypeScript

- Plugin code in `nemoclaw/src/` with its own ESLint config
- CLI type-checking via `tsconfig.cli.json`
- Plugin type-checking via `nemoclaw/tsconfig.json`

### Shell Scripts

- ShellCheck enforced (`.shellcheckrc` at root)
- `shfmt` for formatting
- All scripts must have shebangs and be executable

### No External Project Links

Do not add links to third-party code repositories, community collections, or unofficial resources. Links to official tool documentation (Node.js, Python, uv) are acceptable.

## Git Hooks (prek)

All hooks managed by [prek](https://prek.j178.dev/) (installed via `npm install`):

| Hook | What runs |
|------|-----------|
| **pre-commit** | File fixers, formatters, linters, Vitest (plugin) |
| **commit-msg** | commitlint (Conventional Commits) |
| **pre-push** | TypeScript type check (tsc --noEmit for plugin, JS, CLI) |

## Documentation

- Source of truth: `docs/` directory
- `.agents/skills/nemoclaw-*/*.md` is **autogenerated** — never edit directly
- After changing docs, regenerate skills:

  ```bash
  python3 scripts/docs-to-skills.py docs/ .agents/skills/ --prefix nemoclaw
  ```

- Follow style guide in `docs/CONTRIBUTING.md`

## PR Requirements

- Create feature branch from `main`
- Run `make check` and `npm test` before submitting
- Follow PR template (`.github/PULL_REQUEST_TEMPLATE.md`)
- Update docs for any user-facing behavior changes
- No secrets, API keys, or credentials committed
- Limit open PRs to fewer than 10

```

### File: CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Overview

Define the code of conduct followed and enforced for NemoClaw

### Intended audience

Community | Developers | Project Leads

## Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, sex characteristics, gender identity and expression,
level of experience, education, socio-economic status, nationality, personal
appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
  advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
  address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

## Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting <GitHub_Conduct@nvidia.com>. All complaints will be reviewed and
investigated and will result in a response that is deemed necessary and appropriate
to the circumstances. The project team is obligated to maintain confidentiality with
regard to the reporter of an incident. Further details of specific enforcement policies
may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at <https://www.contributor-covenant.org/version/1/4/code-of-conduct.html>

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see
<https://www.contributor-covenant.org/faq>

```

### File: commitlint.config.js
```js
// SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

module.exports = {
  extends: ["@commitlint/config-conventional"],
  rules: {
    "type-enum": [
      2,
      "always",
      [
        "feat",
        "fix",
        "docs",
        "chore",
        "refactor",
        "test",
        "ci",
        "perf",
        "merge",
      ],
    ],
  },
};

```

### File: CONTRIBUTING.md
```md
# Contributing to NVIDIA NemoClaw

Thank you for your interest in contributing to NVIDIA NemoClaw. This guide covers how to set up your development environment, run tests, and submit changes.

## Before You Open an Issue

Open an issue when you encounter one of the following situations.

- A real bug that you confirmed and could not fix.
- A feature proposal with a design — not a "please build this" request.
- Security vulnerabilities must follow [SECURITY.md](SECURITY.md) — **not** GitHub issues.

## Prerequisites

Install the following before you begin.

- Node.js 22.16+ and npm 10+
- Python 3.11+ (for blueprint and documentation builds)
- Docker (running)
- [uv](https://docs.astral.sh/uv/) (for Python dependency management)
- [hadolint](https://github.com/hadolint/hadolint) (Dockerfile linter — `brew install hadolint` on macOS)

## Getting Started

Install the root dependencies and build the TypeScript plugin:

```bash
# Install root dependencies (OpenClaw + CLI entry point)
npm install

# Install and build the TypeScript plugin
cd nemoclaw && npm install && npm run build && cd ..

# Install Python deps for the blueprint
cd nemoclaw-blueprint && uv sync && cd ..
```

## Building

The TypeScript plugin lives in `nemoclaw/` and compiles with `tsc`:

```bash
cd nemoclaw
npm run build        # one-time compile
npm run dev          # watch mode
```

The CLI (`bin/`, `scripts/`) is type-checked separately:

```bash
npm run typecheck:cli   # or: npx tsc -p tsconfig.cli.json
```

## Main Tasks

These are the primary `make` and `npm` targets for day-to-day development:

| Task | Purpose |
|------|---------|
| `make check` | Run all linters (TypeScript + Python) |
| `make lint` | Same as `make check` |
| `make format` | Auto-format TypeScript and Python source |
| `npm run typecheck:cli` | Type-check CLI TypeScript (`bin/`, `scripts/`) |
| `npm test` | Run root-level tests (`test/*.test.js`) |
| `cd nemoclaw && npm test` | Run plugin unit tests (Vitest) |
| `make docs` | Build documentation (Sphinx/MyST) |
| `make docs-live` | Serve docs locally with auto-rebuild |
| `npx prek run --all-files` | Run all hooks from `.pre-commit-config.yaml` — see below |

### Git hooks (prek)

All git hooks are managed by [prek](https://prek.j178.dev/), a fast, single-binary pre-commit hook runner installed as a devDependency (`@j178/prek`). The `npm install` step runs `prek install` automatically via the `prepare` script, which wires up the following hooks from [`.pre-commit-config.yaml`](.pre-commit-config.yaml):

| Hook | What runs |
|------|-----------|
| **pre-commit** | File fixers, formatters, linters, Vitest (plugin) |
| **commit-msg** | commitlint (Conventional Commits) |
| **pre-push** | TypeScript type check (`tsc --noEmit` for plugin, JS, and CLI) |

For a full manual check: `npx prek run --all-files`. For scoped runs: `npx prek run --from-ref <base> --to-ref HEAD`.

If you still have `core.hooksPath` set from an old Husky setup, Git will ignore `.git/hooks`. Run `git config --unset core.hooksPath` in this repo, then `npm install` so `prek install` (via `prepare`) can register the hooks.

`make check` remains the primary documented linter entry point.

## Project Structure

The repository is organized as follows.

| Path | Purpose |
|------|---------|
| `nemoclaw/` | TypeScript plugin (Commander CLI, OpenClaw extension) |
| `nemoclaw-blueprint/` | Python blueprint for sandbox orchestration |
| `bin/` | CLI entry point (`nemoclaw.js`) |
| `scripts/` | Install helpers and automation scripts |
| `test/` | Root-level integration tests |
| `docs/` | User-facing documentation (Sphinx/MyST) |

## Language Policy

All new source files must be TypeScript. Do not add new `.js` files to the project. When modifying an existing JavaScript file, prefer migrating it to TypeScript in the same PR.

Existing JavaScript in `bin/` and `scripts/` is being incrementally migrated (see `src/lib/` for completed migrations). Tests in `test/` may remain ESM JavaScript for now but new test files should use TypeScript where practical.

Shell scripts (`scripts/*.sh`) must pass ShellCheck and use `shfmt` formatting.

## Documentation

If your change affects user-facing behavior (new commands, changed defaults, new features, bug fixes that contradict existing docs), update the relevant pages under `docs/` in the same PR.

If you use an AI coding agent (Cursor, Claude Code, Codex, etc.), the repo includes the `/update-docs` skill that drafts doc updates. Use them before writing from scratch and follow the style guide in [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md).

To build and preview docs locally:

```bash
make docs       # build the docs
make docs-live  # serve locally with auto-rebuild
```

See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for the full style guide and writing conventions.

### Doc-to-Skills Pipeline

The `docs/` directory is the source of truth for user-facing documentation.
The script `scripts/docs-to-skills.py` converts doc pages into agent skills under `.agents/skills/`.
These generated skills let AI agents answer user questions and walk through procedures without reading raw doc pages.

Always edit pages in `docs/`.
Never edit generated skill files under `.agents/skills/nemoclaw-*/` — your changes will be overwritten on the next run.

After changing any page in `docs/`, regenerate the skills from the repo root:

```bash
python scripts/docs-to-skills.py docs/ .agents/skills/ --prefix nemoclaw
```

Always use this exact output path (`.agents/skills/`) and prefix (`nemoclaw`) so skill names and locations stay consistent.

Preview what would change before writing files:

```bash
python scripts/docs-to-skills.py docs/ .agents/skills/ --prefix nemoclaw --dry-run
```

Other useful flags:

| Flag | Purpose |
|------|---------|
| `--strategy <name>` | Grouping strategy: `smart` (default), `grouped`, or `individual`. |
| `--name-map CAT=NAME` | Override a generated skill name (e.g. `--name-map about=overview`). |
| `--exclude <file>` | Skip specific files (e.g. `--exclude "release-notes.md"`). |

#### Generated skill structure

Each skill directory contains:

```text
.agents/skills/<skill-name>/
├── SKILL.md              # Frontmatter + procedures + related skills
└── references/           # Detailed concept and reference content (loaded on demand)
    ├── <concept-page>.md
    └── <reference-page>.md
```

Agents load the `references/` directory only when needed (progressive disclosure).
The `SKILL.md` itself stays under 500 lines so agents can read it quickly.

## Pull Requests

We welcome contributions. Every PR requires maintainer review. To keep the review queue healthy, limit the number of open PRs you have at any time to fewer than 10.

> [!WARNING]
> Accounts that repeatedly exceed this limit or submit automated bulk PRs may have their PRs closed or their access restricted.

### No External Project Links

Do not add links to third-party code repositories, community collections, or unofficial resources in documentation, README files, or code. This includes "awesome lists," community template repositories, wrapper projects, and similar community-maintained resources — regardless of popularity or utility.

Links to official documentation for tools we depend on (e.g., Node.js, Python, uv) and industry standards (e.g., Conventional Commits) are acceptable.

**Why:** External repositories are outside our control. They can change ownership, inject malicious content, or misrepresent an endorsement by NVIDIA. Keeping references within our own repo avoids these risks entirely.

If you believe an external resource belongs in our docs, open an issue to discuss it with maintainers first.

### Submitting a Pull Request

Follow these steps to submit a pull request.

1. Create a feature branch from `main`.
2. Make your changes with tests.
3. Run `make check` and `npm test` to verify.
4. Open a PR.

### Commit Messages

This project uses [Conventional Commits](https://www.conventionalcommits.org/). All commit messages must follow the format:

```text
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

**Types:**

- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation only
- `chore` - Maintenance tasks (dependencies, build config)
- `refactor` - Code change that neither fixes a bug nor adds a feature
- `test` - Adding or updating tests
- `ci` - CI/CD changes
- `perf` - Performance improvements

**Examples:**

```text
feat(cli): add --profile flag to nemoclaw onboard
fix(blueprint): handle missing API key gracefully
docs: update quickstart for new install wizard
chore(deps): bump commander to 13.2
```

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
