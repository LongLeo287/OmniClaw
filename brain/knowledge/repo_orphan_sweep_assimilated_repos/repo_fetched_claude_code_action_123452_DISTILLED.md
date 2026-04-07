---
id: repo-fetched-claude-code-action-123452
type: knowledge
owner: OA
registered_at: 2026-04-05T04:14:25.857737
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_claude-code-action_123452

## Assimilation Report
Auto-cloned repository: FETCHED_claude-code-action_123452

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "@anthropic-ai/claude-code-action",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "format": "prettier --write .",
    "format:check": "prettier --check .",
    "install-hooks": "bun run scripts/install-hooks.sh",
    "test": "bun test",
    "typecheck": "tsc --noEmit"
  },
  "dependencies": {
    "@actions/core": "^1.10.1",
    "@actions/github": "^6.0.1",
    "@anthropic-ai/claude-agent-sdk": "^0.2.92",
    "@modelcontextprotocol/sdk": "^1.11.0",
    "@octokit/graphql": "^8.2.2",
    "@octokit/rest": "^21.1.1",
    "@octokit/webhooks-types": "^7.6.1",
    "node-fetch": "^3.3.2",
    "shell-quote": "^1.8.3",
    "zod": "^3.24.4"
  },
  "devDependencies": {
    "@types/bun": "1.2.11",
    "@types/node": "^20.0.0",
    "@types/node-fetch": "^2.6.12",
    "@types/shell-quote": "^1.7.5",
    "prettier": "3.5.3",
    "typescript": "^5.8.3"
  }
}

```

### File: README.md
```md
![Claude Code Action responding to a comment](https://github.com/user-attachments/assets/1d60c2e9-82ed-4ee5-b749-f9e021c85f4d)

# Claude Code Action

A general-purpose [Claude Code](https://claude.ai/code) action for GitHub PRs and issues that can answer questions and implement code changes. This action intelligently detects when to activate based on your workflow context—whether responding to @claude mentions, issue assignments, or executing automation tasks with explicit prompts. It supports multiple authentication methods including Anthropic direct API, Amazon Bedrock, Google Vertex AI, and Microsoft Foundry.

## Features

- 🎯 **Intelligent Mode Detection**: Automatically selects the appropriate execution mode based on your workflow context—no configuration needed
- 🤖 **Interactive Code Assistant**: Claude can answer questions about code, architecture, and programming
- 🔍 **Code Review**: Analyzes PR changes and suggests improvements
- ✨ **Code Implementation**: Can implement simple fixes, refactoring, and even new features
- 💬 **PR/Issue Integration**: Works seamlessly with GitHub comments and PR reviews
- 🛠️ **Flexible Tool Access**: Access to GitHub APIs and file operations (additional tools can be enabled via configuration)
- 📋 **Progress Tracking**: Visual progress indicators with checkboxes that dynamically update as Claude completes tasks
- 📊 **Structured Outputs**: Get validated JSON results that automatically become GitHub Action outputs for complex automations
- 🏃 **Runs on Your Infrastructure**: The action executes entirely on your own GitHub runner (Anthropic API calls go to your chosen provider)
- ⚙️ **Simplified Configuration**: Unified `prompt` and `claude_args` inputs provide clean, powerful configuration aligned with Claude Code SDK

## 📦 Upgrading from v0.x?

**See our [Migration Guide](./docs/migration-guide.md)** for step-by-step instructions on updating your workflows to v1.0. The new version simplifies configuration while maintaining compatibility with most existing setups.

## Quickstart

The easiest way to set up this action is through [Claude Code](https://claude.ai/code) in the terminal. Just open `claude` and run `/install-github-app`.

This command will guide you through setting up the GitHub app and required secrets.

**Note**:

- You must be a repository admin to install the GitHub app and add secrets
- This quickstart method is only available for direct Anthropic API users. For AWS Bedrock, Google Vertex AI, or Microsoft Foundry setup, see [docs/cloud-providers.md](./docs/cloud-providers.md).

## 📚 Solutions & Use Cases

Looking for specific automation patterns? Check our **[Solutions Guide](./docs/solutions.md)** for complete working examples including:

- **🔍 Automatic PR Code Review** - Full review automation
- **📂 Path-Specific Reviews** - Trigger on critical file changes
- **👥 External Contributor Reviews** - Special handling for new contributors
- **📝 Custom Review Checklists** - Enforce team standards
- **🔄 Scheduled Maintenance** - Automated repository health checks
- **🏷️ Issue Triage & Labeling** - Automatic categorization
- **📖 Documentation Sync** - Keep docs updated with code changes
- **🔒 Security-Focused Reviews** - OWASP-aligned security analysis
- **📊 DIY Progress Tracking** - Create tracking comments in automation mode

Each solution includes complete working examples, configuration details, and expected outcomes.

## Documentation

- **[Solutions Guide](./docs/solutions.md)** - **🎯 Ready-to-use automation patterns**
- **[Migration Guide](./docs/migration-guide.md)** - **⭐ Upgrading from v0.x to v1.0**
- [Setup Guide](./docs/setup.md) - Manual setup, custom GitHub apps, and security best practices
- [Usage Guide](./docs/usage.md) - Basic usage, workflow configuration, and input parameters
- [Custom Automations](./docs/custom-automations.md) - Examples of automated workflows and custom prompts
- [Configuration](./docs/configuration.md) - MCP servers, permissions, environment variables, and advanced settings
- [Experimental Features](./docs/experimental.md) - Execution modes and network restrictions
- [Cloud Providers](./docs/cloud-providers.md) - AWS Bedrock, Google Vertex AI, and Microsoft Foundry setup
- [Capabilities & Limitations](./docs/capabilities-and-limitations.md) - What Claude can and cannot do
- [Security](./docs/security.md) - Access control, permissions, and commit signing
- [FAQ](./docs/faq.md) - Common questions and troubleshooting

## 📚 FAQ

Having issues or questions? Check out our [Frequently Asked Questions](./docs/faq.md) for solutions to common problems and detailed explanations of Claude's capabilities and limitations.

## License

This project is licensed under the MIT License—see the LICENSE file for details.

```

### File: base-action\package.json
```json
{
  "name": "@anthropic-ai/claude-code-base-action",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "format": "prettier --write .",
    "format:check": "prettier --check .",
    "install-hooks": "bun run scripts/install-hooks.sh",
    "test": "bun test",
    "typecheck": "tsc --noEmit"
  },
  "dependencies": {
    "@actions/core": "^1.10.1",
    "@anthropic-ai/claude-agent-sdk": "^0.2.92",
    "shell-quote": "^1.8.3"
  },
  "devDependencies": {
    "@types/bun": "^1.2.12",
    "@types/node": "^20.0.0",
    "@types/shell-quote": "^1.7.5",
    "prettier": "3.5.3",
    "typescript": "^5.8.3"
  }
}

```

### File: base-action\README.md
```md
# Claude Code Base Action

This GitHub Action allows you to run [Claude Code](https://www.anthropic.com/claude-code) within your GitHub Actions workflows. You can use this to build any custom workflow on top of Claude Code.

For simply tagging @claude in issues and PRs out of the box, [check out the Claude Code action and GitHub app](https://github.com/anthropics/claude-code-action).

## Usage

Add the following to your workflow file:

```yaml
# Using a direct prompt
- name: Run Claude Code with direct prompt
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Your prompt here"
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}

# Or using a prompt from a file
- name: Run Claude Code with prompt file
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt_file: "/path/to/prompt.txt"
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}

# Or limiting the conversation turns
- name: Run Claude Code with limited turns
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Your prompt here"
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
    max_turns: "5" # Limit conversation to 5 turns
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}

# Using custom system prompts
- name: Run Claude Code with custom system prompt
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Build a REST API"
    system_prompt: "You are a senior backend engineer. Focus on security, performance, and maintainability."
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}

# Or appending to the default system prompt
- name: Run Claude Code with appended system prompt
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Create a database schema"
    append_system_prompt: "After writing code, be sure to code review yourself."
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}

# Using custom environment variables
- name: Run Claude Code with custom environment variables
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Deploy to staging environment"
    claude_env: |
      ENVIRONMENT: staging
      API_URL: https://api-staging.example.com
      DEBUG: true
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}

# Using fallback model for handling API errors
- name: Run Claude Code with fallback model
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Review and fix TypeScript errors"
    model: "claude-opus-4-1-20250805"
    fallback_model: "claude-sonnet-4-20250514"
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}

# Using OAuth token instead of API key
- name: Run Claude Code with OAuth token
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Update dependencies"
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
    claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
```

## Inputs

| Input                     | Description                                                                                                             | Required | Default                      |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------- | ---------------------------- |
| `prompt`                  | The prompt to send to Claude Code                                                                                       | No\*     | ''                           |
| `prompt_file`             | Path to a file containing the prompt to send to Claude Code                                                             | No\*     | ''                           |
| `allowed_tools`           | Comma-separated list of allowed tools for Claude Code to use                                                            | No       | ''                           |
| `disallowed_tools`        | Comma-separated list of disallowed tools that Claude Code cannot use                                                    | No       | ''                           |
| `max_turns`               | Maximum number of conversation turns (default: no limit)                                                                | No       | ''                           |
| `mcp_config`              | Path to the MCP configuration JSON file, or MCP configuration JSON string                                               | No       | ''                           |
| `settings`                | Path to Claude Code settings JSON file, or settings JSON string                                                         | No       | ''                           |
| `system_prompt`           | Override system prompt                                                                                                  | No       | ''                           |
| `append_system_prompt`    | Append to system prompt                                                                                                 | No       | ''                           |
| `claude_env`              | Custom environment variables to pass to Claude Code execution (YAML multiline format)                                   | No       | ''                           |
| `model`                   | Model to use (provider-specific format required for Bedrock/Vertex)                                                     | No       | 'claude-4-0-sonnet-20250219' |
| `anthropic_model`         | DEPRECATED: Use 'model' instead                                                                                         | No       | 'claude-4-0-sonnet-20250219' |
| `fallback_model`          | Enable automatic fallback to specified model when default model is overloaded                                           | No       | ''                           |
| `anthropic_api_key`       | Anthropic API key (required for direct Anthropic API)                                                                   | No       | ''                           |
| `claude_code_oauth_token` | Claude Code OAuth token (alternative to anthropic_api_key)                                                              | No       | ''                           |
| `use_bedrock`             | Use Amazon Bedrock with OIDC authentication instead of direct Anthropic API                                             | No       | 'false'                      |
| `use_vertex`              | Use Google Vertex AI with OIDC authentication instead of direct Anthropic API                                           | No       | 'false'                      |
| `use_node_cache`          | Whether to use Node.js dependency caching (set to true only for Node.js projects with lock files)                       | No       | 'false'                      |
| `show_full_output`        | Show full JSON output (⚠️ May expose secrets - see [security docs](../docs/security.md#️-full-output-security-warning)) | No       | 'false'\*\*                  |

\*Either `prompt` or `prompt_file` must be provided, but not both.

\*\*`show_full_output` is automatically enabled when GitHub Actions debug mode is active. See [security documentation](../docs/security.md#️-full-output-security-warning) for important security considerations.

## Outputs

| Output           | Description                                                |
| ---------------- | ---------------------------------------------------------- |
| `conclusion`     | Execution status of Claude Code ('success' or 'failure')   |
| `execution_file` | Path to the JSON file containing Claude Code execution log |

## Environment Variables

The following environment variables can be used to configure the action:

| Variable       | Description                                           | Default |
| -------------- | ----------------------------------------------------- | ------- |
| `NODE_VERSION` | Node.js version to use (e.g., '18.x', '20.x', '22.x') | '18.x'  |

Example usage:

```yaml
- name: Run Claude Code with Node.js 20
  uses: anthropics/claude-code-base-action@beta
  env:
    NODE_VERSION: "20.x"
  with:
    prompt: "Your prompt here"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

## Custom Environment Variables

You can pass custom environment variables to Claude Code execution using the `claude_env` input. This allows Claude to access environment-specific configuration during its execution.

The `claude_env` input accepts YAML multiline format with key-value pairs:

```yaml
- name: Deploy with custom environment
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Deploy the application to the staging environment"
    claude_env: |
      ENVIRONMENT: staging
      API_BASE_URL: https://api-staging.example.com
      DATABASE_URL: ${{ secrets.STAGING_DB_URL }}
      DEBUG: true
      LOG_LEVEL: debug
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

### Features:

- **YAML Format**: Use standard YAML key-value syntax (`KEY: value`)
- **Multiline Support**: Define multiple environment variables in a single input
- **Comments**: Lines starting with `#` are ignored
- **GitHub Secrets**: Can reference GitHub secrets using `${{ secrets.SECRET_NAME }}`
- **Runtime Access**: Environment variables are available to Claude during execution

### Example Use Cases:

```yaml
# Development configuration
claude_env: |
  NODE_ENV: development
  API_URL: http://localhost:3000
  DEBUG: true

# Production deployment
claude_env: |
  NODE_ENV: production
  API_URL: https://api.example.com
  DATABASE_URL: ${{ secrets.PROD_DB_URL }}
  REDIS_URL: ${{ secrets.REDIS_URL }}

# Feature flags and configuration
claude_env: |
  FEATURE_NEW_UI: enabled
  MAX_RETRIES: 3
  TIMEOUT_MS: 5000
```

## Using Settings Configuration

You can provide Claude Code settings configuration in two ways:

### Option 1: Settings Configuration File

Provide a path to a JSON file containing Claude Code settings:

```yaml
- name: Run Claude Code with settings file
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Your prompt here"
    settings: "path/to/settings.json"
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

### Option 2: Inline Settings Configuration

Provide the settings configuration directly as a JSON string:

```yaml
- name: Run Claude Code with inline settings
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Your prompt here"
    settings: |
      {
        "model": "claude-opus-4-1-20250805",
        "env": {
          "DEBUG": "true",
          "API_URL": "https://api.example.com"
        },
        "permissions": {
          "allow": ["Bash", "Read"],
          "deny": ["WebFetch"]
        },
        "hooks": {
          "PreToolUse": [{
            "matcher": "Bash",
            "hooks": [{
              "type": "command",
              "command": "echo Running bash command..."
            }]
          }]
        }
      }
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

The settings file supports all Claude Code settings options including:

- `model`: Override the default model
- `env`: Environment variables for the session
- `permissions`: Tool usage permissions
- `hooks`: Pre/post tool execution hooks
- `includeCoAuthoredBy`: Include co-authored-by in git commits
- And more...

**Note**: The `enableAllProjectMcpServers` setting is always set to `true` by this action to ensure MCP servers work correctly.

## Using MCP Config

You can provide MCP configuration in two ways:

### Option 1: MCP Configuration File

Provide a path to a JSON file containing MCP configuration:

```yaml
- name: Run Claude Code with MCP config file
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Your prompt here"
    mcp_config: "path/to/mcp-config.json"
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

### Option 2: Inline MCP Configuration

Provide the MCP configuration directly as a JSON string:

```yaml
- name: Run Claude Code with inline MCP config
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Your prompt here"
    mcp_config: |
      {
        "mcpServers": {
          "server-name": {
            "command": "node",
            "args": ["./server.js"],
            "env": {
              "API_KEY": "your-api-key"
            }
          }
        }
      }
    allowed_tools: "Bash(git:*),View,GlobTool,GrepTool,BatchTool"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

The MCP config file should follow this format:

```json
{
  "mcpServers": {
    "server-name": {
      "command": "node",
      "args": ["./server.js"],
      "env": {
        "API_KEY": "your-api-key"
      }
    }
  }
}
```

You can combine MCP config with other inputs like allowed tools:

```yaml
# Using multiple inputs together
- name: Run Claude Code with MCP and custom tools
  uses: anthropics/claude-code-base-action@beta
  with:
    prompt: "Access the custom MCP server and use its tools"
    mcp_config: "mcp-config.json"
    allowed_tools: "Bash(git:*),View,mcp__server-name__custom_tool"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

## Example: PR Code Review

```yaml
name: Claude Code Review

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  code-review:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v6
        with:
          fetch-depth: 0

      - name: Run Code Review with Claude
        id: code-review
        uses: anthropics/claude-code-base-action@beta
        with:
          prompt: "Review the PR changes. Focus on code quality, potential bugs, and performance issues. Suggest improvements where appropriate. Write your review as markdown text."
          allowed_tools: "Bash(git diff --name-only HEAD~1),Bash(git diff HEAD~1),View,GlobTool,GrepTool,Write"
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}

      - name: Extract and Comment PR Review
        if: steps.code-review.outputs.conclusion == 'success'
        uses: actions/github-script@v7
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          script: |
            const fs = require('fs');
            const executionFile = '${{ steps.code-review.outputs.execution_file }}';
            const executionLog = JSON.parse(fs.readFileSync(executionFile, 'utf8')
... [TRUNCATED]
```

### File: base-action\test\mcp-test\package.json
```json
{
  "name": "mcp-test",
  "version": "1.0.0",
  "dependencies": {
    "@modelcontextprotocol/sdk": "^1.24.0"
  }
}

```

### File: CLAUDE.md
```md
# CLAUDE.md

## Commands

```bash
bun test                # Run tests
bun run typecheck       # TypeScript type checking
bun run format          # Format with prettier
bun run format:check    # Check formatting
```

## What This Is

A GitHub Action that lets Claude respond to `@claude` mentions on issues/PRs (tag mode) or run tasks via `prompt` input (agent mode). Mode is auto-detected: if `prompt` is provided, it's agent mode; if triggered by a comment/issue event with `@claude`, it's tag mode. See `src/modes/detector.ts`.

## How It Runs

Single entrypoint: `src/entrypoints/run.ts` orchestrates everything — prepare (auth, permissions, trigger check, branch/comment creation), install Claude Code CLI, execute Claude via `base-action/` functions (imported directly, not subprocess), then cleanup (update tracking comment, write step summary). SSH signing cleanup and token revocation are separate `always()` steps in `action.yml`.

`base-action/` is also published standalone as `@anthropic-ai/claude-code-base-action`. Don't break its public API. It reads config from `INPUT_`-prefixed env vars (set by `action.yml`), not from action inputs directly.

## Key Concepts

**Auth priority**: `github_token` input (user-provided) > GitHub App OIDC token (default). The `claude_code_oauth_token` and `anthropic_api_key` are for the Claude API, not GitHub. Token setup lives in `src/github/token.ts`.

**Mode lifecycle**: `detectMode()` in `src/modes/detector.ts` picks the mode name ("tag" or "agent"). Trigger checking and prepare dispatch are inlined in `run.ts`: tag mode calls `prepareTagMode()` from `src/modes/tag/`, agent mode calls `prepareAgentMode()` from `src/modes/agent/`.

**Prompt construction**: Tag mode's `prepareTagMode()` builds the prompt by fetching GitHub data (`src/github/data/fetcher.ts`), formatting it as markdown (`src/github/data/formatter.ts`), and writing it to a temp file via `createPrompt()`. Agent mode writes the user's prompt directly. The prompt includes issue/PR body, comments, diff, and CI status. This is the most important part of the action — it's what Claude sees.

## Things That Will Bite You

- **Strict TypeScript**: `noUnusedLocals` and `noUnusedParameters` are enabled. Typecheck will fail on unused variables.
- **Discriminated unions for GitHub context**: `GitHubContext` is a union type — call `isEntityContext(context)` before accessing entity-specific fields like `context.issue` or `context.pullRequest`.
- **Token lifecycle matters**: The GitHub App token is obtained early and revoked in a separate `always()` step in `action.yml`. If you move token revocation into `run.ts`, it won't run if the process crashes. Same for SSH signing cleanup.
- **Error phase attribution**: The catch block in `run.ts` uses `prepareCompleted` to distinguish prepare failures from execution failures. The tracking comment shows different messages for each.
- **`action.yml` outputs reference step IDs**: Outputs like `execution_file`, `branch_name`, `github_token` reference `steps.run.outputs.*`. If you rename the step ID, update the outputs section too.
- **Integration testing** happens in a separate repo (`install-test`), not here. The tests in this repo are unit tests.

## Code Conventions

- Runtime is Bun, not Node. Use `bun test`, not `jest`.
- `moduleResolution: "bundler"` — imports don't need `.js` extensions.
- GitHub API calls should use retry logic (`src/utils/retry.ts`).
- MCP servers are auto-installed at runtime to `~/.claude/mcp/github-{type}-server/`.

```

### File: CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

- Demonstrating empathy and kindness toward other people
- Being respectful of differing opinions, viewpoints, and experiences
- Giving and gracefully accepting constructive feedback
- Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
- Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

- The use of sexualized language or imagery, and sexual attention or
  advances of any kind
- Trolling, insulting or derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information, such as a physical or email
  address, without their explicit permission
- Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
claude-code-action-coc@anthropic.com.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior, harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.

```

### File: CONTRIBUTING.md
```md
# Contributing to Claude Code Action

Thank you for your interest in contributing to Claude Code Action! This document provides guidelines and instructions for contributing to the project.

## Getting Started

### Prerequisites

- [Bun](https://bun.sh/) runtime
- [Docker](https://www.docker.com/) (for running GitHub Actions locally)
- [act](https://github.com/nektos/act) (installed automatically by our test script)
- An Anthropic API key (for testing)

### Setup

1. Fork the repository on GitHub and clone your fork:

   ```bash
   git clone https://github.com/your-username/claude-code-action.git
   cd claude-code-action
   ```

2. Install dependencies:

   ```bash
   bun install
   ```

3. Set up your Anthropic API key:
   ```bash
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```

## Development

### Available Scripts

- `bun test` - Run all tests
- `bun run typecheck` - Type check the code
- `bun run format` - Format code with Prettier
- `bun run format:check` - Check code formatting

## Testing

### Running Tests Locally

1. **Unit Tests**:

   ```bash
   bun test
   ```

## Pull Request Process

1. Create a new branch from `main`:

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit them:

   ```bash
   git add .
   git commit -m "feat: add new feature"
   ```

3. Run tests and formatting:

   ```bash
   bun test
   bun run typecheck
   bun run format:check
   ```

4. Push your branch and create a Pull Request:

   ```bash
   git push origin feature/your-feature-name
   ```

5. Ensure all CI checks pass

6. Request review from maintainers

## Action Development

### Testing Your Changes

When modifying the action:

1. Test in a real GitHub Actions workflow by:
   - Creating a test repository
   - Using your branch as the action source:
     ```yaml
     uses: your-username/claude-code-action@your-branch
     ```

### Debugging

- Use `console.log` for debugging in development
- Check GitHub Actions logs for runtime issues
- Use `act` with `-v` flag for verbose output:
  ```bash
  act push -v --secret ANTHROPIC_API_KEY="$ANTHROPIC_API_KEY"
  ```

## Common Issues

### Docker Issues

Make sure Docker is running before using `act`. You can check with:

```bash
docker ps
```

```

### File: github-app-manifest.json
```json
{
  "name": "Claude Code Custom App",
  "description": "Custom GitHub App for Claude Code Action - AI-powered coding assistant for GitHub workflows",
  "url": "https://github.com/anthropics/claude-code-action",
  "hook_attributes": {
    "url": "https://example.com/github/webhook",
    "active": false
  },
  "redirect_url": "https://github.com/settings/apps/new",
  "callback_urls": [],
  "setup_url": "https://github.com/anthropics/claude-code-action/blob/main/docs/setup.md",
  "public": false,
  "default_permissions": {
    "contents": "write",
    "issues": "write",
    "pull_requests": "write",
    "actions": "read",
    "metadata": "read"
  },
  "default_events": [
    "issue_comment",
    "issues",
    "pull_request",
    "pull_request_review",
    "pull_request_review_comment"
  ]
}

```

### File: ROADMAP.md
```md
# Claude Code GitHub Action Roadmap

Thank you for trying out the beta of our GitHub Action! This document outlines our path to `v1.0`. Items are not necessarily in priority order.

## Path to 1.0

- ~**Ability to see GitHub Action CI results** - This will enable Claude to look at CI failures and make updates to PRs to fix test failures, lint errors, and the like.~
- **Cross-repo support** - Enable Claude to work across multiple repositories in a single session
- **Ability to modify workflow files** - Let Claude update GitHub Actions workflows and other CI configuration files
- **Support for workflow_dispatch and repository_dispatch events** - Dispatch Claude on events triggered via API from other workflows or from other services
- **Ability to disable commit signing** - Option to turn off GPG signing for environments where it's not required. This will enable Claude to use normal `git` bash commands for committing. This will likely become the default behavior once added.
- **Better code review behavior** - Support inline comments on specific lines, provide higher quality reviews with more actionable feedback
- ~**Support triggering @claude from bot users** - Allow automation and bot accounts to invoke Claude~
- **Customizable base prompts** - Full control over Claude's initial context with template variables like `$PR_COMMENTS`, `$PR_FILES`, etc. Users can replace our default prompt entirely while still accessing key contextual data

---

**Note:** This roadmap represents our current vision for reaching `v1.0` and is subject to change based on user feedback and development priorities.

We welcome feedback on these planned features! If you're interested in contributing to any of these features, please open an issue to discuss implementation details with us. We're also open to suggestions for new features not listed here.

```

### File: SECURITY.md
```md
# Security Policy

Thank you for helping us keep this action and the systems they interact with secure.

## Reporting Security Issues

This repository is maintained by [Anthropic](https://www.anthropic.com/).

The security of our systems and user data is Anthropic’s top priority. We appreciate the work of security researchers acting in good faith in identifying and reporting potential vulnerabilities.

Our security program is managed on HackerOne and we ask that any validated vulnerability in this functionality be reported through their [submission form](https://hackerone.com/anthropic-vdp/reports/new?type=team&report_type=vulnerability).

## Vulnerability Disclosure Program

Our Vulnerability Program Guidelines are defined on our [HackerOne program page](https://hackerone.com/anthropic-vdp).

```

### File: tsconfig.json
```json
{
  "compilerOptions": {
    // Environment setup & latest features
    "lib": ["ESNext"],
    "target": "ESNext",
    "module": "ESNext",
    "moduleDetection": "force",
    "jsx": "react-jsx",
    "allowJs": true,

    // Bundler mode (Bun-specific)
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "verbatimModuleSyntax": true,
    "noEmit": true,

    // Best practices
    "strict": true,
    "skipLibCheck": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedIndexedAccess": true,

    // Some stricter flags
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noPropertyAccessFromIndexSignature": false
  },
  "include": ["src/**/*", "base-action/**/*", "test/**/*"],
  "exclude": ["node_modules"]
}

```

### File: .claude\settings.json
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "bun run format"
          }
        ],
        "matcher": "Edit|Write|MultiEdit"
      }
    ]
  }
}

```

### File: base-action\CLAUDE.md
```md
# CLAUDE.md

## Common Commands

### Development Commands

- Build/Type check: `bun run typecheck`
- Format code: `bun run format`
- Check formatting: `bun run format:check`
- Run tests: `bun test`
- Install dependencies: `bun install`

### Action Testing

- Test action locally: `./test-local.sh`
- Test specific file: `bun test test/prepare-prompt.test.ts`

## Architecture Overview

This is a GitHub Action that allows running Claude Code within GitHub workflows. The action consists of:

### Core Components

1. **Action Definition** (`action.yml`): Defines inputs, outputs, and the composite action steps
2. **Prompt Preparation** (`src/index.ts`): Runs Claude Code with specified arguments

### Key Design Patterns

- Uses Bun runtime for development and execution
- JSON streaming output format for execution logs
- Composite action pattern to orchestrate multiple steps
- Provider-agnostic design supporting Anthropic API, AWS Bedrock, and Google Vertex AI

## Provider Authentication

1. **Anthropic API** (default): Requires API key via `anthropic_api_key` input
2. **AWS Bedrock**: Uses OIDC authentication when `use_bedrock: true`
3. **Google Vertex AI**: Uses OIDC authentication when `use_vertex: true`

## Testing Strategy

### Local Testing

- Use `act` tool to run GitHub Actions workflows locally
- `test-local.sh` script automates local testing setup
- Requires `ANTHROPIC_API_KEY` environment variable

### Test Structure

- Unit tests for configuration logic
- Integration tests for prompt preparation
- Full workflow tests in `.github/workflows/test-base-action.yml`

## Important Technical Details

- Outputs execution logs as JSON to `/tmp/claude-execution-output.json`
- Timeout enforcement via `timeout` command wrapper
- Strict TypeScript configuration with Bun-specific settings

```

### File: base-action\CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

- Demonstrating empathy and kindness toward other people
- Being respectful of differing opinions, viewpoints, and experiences
- Giving and gracefully accepting constructive feedback
- Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
- Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

- The use of sexualized language or imagery, and sexual attention or
  advances of any kind
- Trolling, insulting or derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information, such as a physical or email
  address, without their explicit permission
- Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
claude-code-action-coc@anthropic.com.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior, harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.

```

### File: base-action\CONTRIBUTING.md
```md
# Contributing to Claude Code Base Action

Thank you for your interest in contributing to Claude Code Base Action! This document provides guidelines and instructions for contributing to the project.

## Getting Started

### Prerequisites

- [Bun](https://bun.sh/) runtime
- [Docker](https://www.docker.com/) (for running GitHub Actions locally)
- [act](https://github.com/nektos/act) (installed automatically by our test script)
- An Anthropic API key (for testing)

### Setup

1. Fork the repository on GitHub and clone your fork:

   ```bash
   git clone https://github.com/your-username/claude-code-base-action.git
   cd claude-code-base-action
   ```

2. Install dependencies:

   ```bash
   bun install
   ```

3. Set up your Anthropic API key:
   ```bash
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```

## Development

### Available Scripts

- `bun test` - Run all tests
- `bun run typecheck` - Type check the code
- `bun run format` - Format code with Prettier
- `bun run format:check` - Check code formatting

## Testing

### Running Tests Locally

1. **Unit Tests**:

   ```bash
   bun test
   ```

2. **Integration Tests** (using GitHub Actions locally):

   ```bash
   ./test-local.sh
   ```

   This script:

   - Installs `act` if not present (requires Homebrew on macOS)
   - Runs the GitHub Action workflow locally using Docker
   - Requires your `ANTHROPIC_API_KEY` to be set

   On Apple Silicon Macs, the script automatically adds the `--container-architecture linux/amd64` flag to avoid compatibility issues.

## Pull Request Process

1. Create a new branch from `main`:

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit them:

   ```bash
   git add .
   git commit -m "feat: add new feature"
   ```

3. Run tests and formatting:

   ```bash
   bun test
   bun run typecheck
   bun run format:check
   ```

4. Push your branch and create a Pull Request:

   ```bash
   git push origin feature/your-feature-name
   ```

5. Ensure all CI checks pass

6. Request review from maintainers

## Action Development

### Testing Your Changes

When modifying the action:

1. Test locally with the test script:

   ```bash
   ./test-local.sh
   ```

2. Test in a real GitHub Actions workflow by:
   - Creating a test repository
   - Using your branch as the action source:
     ```yaml
     uses: your-username/claude-code-base-action@your-branch
     ```

### Debugging

- Use `console.log` for debugging in development
- Check GitHub Actions logs for runtime issues
- Use `act` with `-v` flag for verbose output:
  ```bash
  act push -v --secret ANTHROPIC_API_KEY="$ANTHROPIC_API_KEY"
  ```

## Common Issues

### Docker Issues

Make sure Docker is running before using `act`. You can check with:

```bash
docker ps
```

```

### File: base-action\MIRROR_DISCLAIMER.md
```md
# ⚠️ This is a Mirror Repository

This repository is an automated mirror of the `base-action` directory from [anthropics/claude-code-action](https://github.com/anthropics/claude-code-action).

**Do not submit PRs or issues to this repository.** Instead, please contribute to the main repository:

- 🐛 [Report issues](https://github.com/anthropics/claude-code-action/issues)
- 🔧 [Submit pull requests](https://github.com/anthropics/claude-code-action/pulls)
- 📖 [View documentation](https://github.com/anthropics/claude-code-action#readme)

---

```

### File: base-action\package-lock.json
```json
{
  "name": "@anthropic-ai/claude-code-base-action",
  "version": "1.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "@anthropic-ai/claude-code-base-action",
      "version": "1.0.0",
      "dependencies": {
        "@actions/core": "^1.10.1",
        "shell-quote": "^1.8.3"
      },
      "devDependencies": {
        "@types/bun": "^1.2.12",
        "@types/node": "^20.0.0",
        "@types/shell-quote": "^1.7.5",
        "prettier": "3.5.3",
        "typescript": "^5.8.3"
      }
    },
    "node_modules/@actions/core": {
      "version": "1.11.1",
      "resolved": "https://registry.npmjs.org/@actions/core/-/core-1.11.1.tgz",
      "integrity": "sha512-hXJCSrkwfA46Vd9Z3q4cpEpHB1rL5NG04+/rbqW9d3+CSvtB1tYe8UTpAlixa1vj0m/ULglfEK2UKxMGxCxv5A==",
      "license": "MIT",
      "dependencies": {
        "@actions/exec": "^1.1.1",
        "@actions/http-client": "^2.0.1"
      }
    },
    "node_modules/@actions/exec": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/@actions/exec/-/exec-1.1.1.tgz",
      "integrity": "sha512-+sCcHHbVdk93a0XT19ECtO/gIXoxvdsgQLzb2fE2/5sIZmWQuluYyjPQtrtTHdU1YzTZ7bAPN4sITq2xi1679w==",
      "license": "MIT",
      "dependencies": {
        "@actions/io": "^1.0.1"
      }
    },
    "node_modules/@actions/http-client": {
      "version": "2.2.3",
      "resolved": "https://registry.npmjs.org/@actions/http-client/-/http-client-2.2.3.tgz",
      "integrity": "sha512-mx8hyJi/hjFvbPokCg4uRd4ZX78t+YyRPtnKWwIl+RzNaVuFpQHfmlGVfsKEJN8LwTCvL+DfVgAM04XaHkm6bA==",
      "license": "MIT",
      "dependencies": {
        "tunnel": "^0.0.6",
        "undici": "^5.25.4"
      }
    },
    "node_modules/@actions/io": {
      "version": "1.1.3",
      "resolved": "https://registry.npmjs.org/@actions/io/-/io-1.1.3.tgz",
      "integrity": "sha512-wi9JjgKLYS7U/z8PPbco+PvTb/nRWjeoFlJ1Qer83k/3C5PHQi28hiVdeE2kHXmIL99mQFawx8qt/JPjZilJ8Q==",
      "license": "MIT"
    },
    "node_modules/@fastify/busboy": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/@fastify/busboy/-/busboy-2.1.1.tgz",
      "integrity": "sha512-vBZP4NlzfOlerQTnba4aqZoMhE/a9HY7HRqoOPaETQcSQuWEIyZMHGfVu6w9wGtGK5fED5qRs2DteVCjOH60sA==",
      "license": "MIT",
      "engines": {
        "node": ">=14"
      }
    },
    "node_modules/@types/bun": {
      "version": "1.3.1",
      "resolved": "https://registry.npmjs.org/@types/bun/-/bun-1.3.1.tgz",
      "integrity": "sha512-4jNMk2/K9YJtfqwoAa28c8wK+T7nvJFOjxI4h/7sORWcypRNxBpr+TPNaCfVWq70tLCJsqoFwcf0oI0JU/fvMQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "bun-types": "1.3.1"
      }
    },
    "node_modules/@types/node": {
      "version": "20.19.23",
      "resolved": "https://registry.npmjs.org/@types/node/-/node-20.19.23.tgz",
      "integrity": "sha512-yIdlVVVHXpmqRhtyovZAcSy0MiPcYWGkoO4CGe/+jpP0hmNuihm4XhHbADpK++MsiLHP5MVlv+bcgdF99kSiFQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "undici-types": "~6.21.0"
      }
    },
    "node_modules/@types/react": {
      "version": "19.2.2",
      "resolved": "https://registry.npmjs.org/@types/react/-/react-19.2.2.tgz",
      "integrity": "sha512-6mDvHUFSjyT2B2yeNx2nUgMxh9LtOWvkhIU3uePn2I2oyNymUAX1NIsdgviM4CH+JSrp2D2hsMvJOkxY+0wNRA==",
      "dev": true,
      "license": "MIT",
      "peer": true,
      "dependencies": {
        "csstype": "^3.0.2"
      }
    },
    "node_modules/@types/shell-quote": {
      "version": "1.7.5",
      "resolved": "https://registry.npmjs.org/@types/shell-quote/-/shell-quote-1.7.5.tgz",
      "integrity": "sha512-+UE8GAGRPbJVQDdxi16dgadcBfQ+KG2vgZhV1+3A1XmHbmwcdwhCUwIdy+d3pAGrbvgRoVSjeI9vOWyq376Yzw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/bun-types": {
      "version": "1.3.1",
      "resolved": "https://registry.npmjs.org/bun-types/-/bun-types-1.3.1.tgz",
      "integrity": "sha512-NMrcy7smratanWJ2mMXdpatalovtxVggkj11bScuWuiOoXTiKIu2eVS1/7qbyI/4yHedtsn175n4Sm4JcdHLXw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/node": "*"
      },
      "peerDependencies": {
        "@types/react": "^19"
      }
    },
    "node_modules/csstype": {
      "version": "3.1.3",
      "resolved": "https://registry.npmjs.org/csstype/-/csstype-3.1.3.tgz",
      "integrity": "sha512-M1uQkMl8rQK/szD0LNhtqxIPLpimGm8sOBwU7lLnCpSbTyY3yeU1Vc7l4KT5zT4s/yOxHH5O7tIuuLOCnLADRw==",
      "dev": true,
      "license": "MIT",
      "peer": true
    },
    "node_modules/prettier": {
      "version": "3.5.3",
      "resolved": "https://registry.npmjs.org/prettier/-/prettier-3.5.3.tgz",
      "integrity": "sha512-QQtaxnoDJeAkDvDKWCLiwIXkTgRhwYDEQCghU9Z6q03iyek/rxRh/2lC3HB7P8sWT2xC/y5JDctPLBIGzHKbhw==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "prettier": "bin/prettier.cjs"
      },
      "engines": {
        "node": ">=14"
      },
      "funding": {
        "url": "https://github.com/prettier/prettier?sponsor=1"
      }
    },
    "node_modules/shell-quote": {
      "version": "1.8.3",
      "resolved": "https://registry.npmjs.org/shell-quote/-/shell-quote-1.8.3.tgz",
      "integrity": "sha512-ObmnIF4hXNg1BqhnHmgbDETF8dLPCggZWBjkQfhZpbszZnYur5DUljTcCHii5LC3J5E0yeO/1LIMyH+UvHQgyw==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/tunnel": {
      "version": "0.0.6",
      "resolved": "https://registry.npmjs.org/tunnel/-/tunnel-0.0.6.tgz",
      "integrity": "sha512-1h/Lnq9yajKY2PEbBadPXj3VxsDDu844OnaAo52UVmIzIvwwtBPIuNvkjuzBlTWpfJyUbG3ez0KSBibQkj4ojg==",
      "license": "MIT",
      "engines": {
        "node": ">=0.6.11 <=0.7.0 || >=0.7.3"
      }
    },
    "node_modules/typescript": {
      "version": "5.9.3",
      "resolved": "https://registry.npmjs.org/typescript/-/typescript-5.9.3.tgz",
      "integrity": "sha512-jl1vZzPDinLr9eUt3J/t7V6FgNEw9QjvBPdysz9KfQDD41fQrC2Y4vKQdiaUpFT4bXlb1RHhLpp8wtm6M5TgSw==",
      "dev": true,
      "license": "Apache-2.0",
      "bin": {
        "tsc": "bin/tsc",
        "tsserver": "bin/tsserver"
      },
      "engines": {
        "node": ">=14.17"
      }
    },
    "node_modules/undici": {
      "version": "5.29.0",
      "resolved": "https://registry.npmjs.org/undici/-/undici-5.29.0.tgz",
      "integrity": "sha512-raqeBD6NQK4SkWhQzeYKd1KmIG6dllBOTt55Rmkt4HtI9mwdWtJljnrXjAFUBLTSN67HWrOIZ3EPF4kjUw80Bg==",
      "license": "MIT",
      "dependencies": {
        "@fastify/busboy": "^2.0.0"
      },
      "engines": {
        "node": ">=14.0"
      }
    },
    "node_modules/undici-types": {
      "version": "6.21.0",
      "resolved": "https://registry.npmjs.org/undici-types/-/undici-types-6.21.0.tgz",
      "integrity": "sha512-iwDZqg0QAGrg9Rav5H4n0M64c3mkR59cJ6wQp+7C4nI0gsmExaedaYLNO44eT4AtBBwjbTiGPMlt2Md0T9H9JQ==",
      "dev": true,
      "license": "MIT"
    }
  }
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
