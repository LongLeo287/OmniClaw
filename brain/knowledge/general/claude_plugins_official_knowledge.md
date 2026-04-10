# Knowledge Dump for claude_plugins_official

## File: README.md
```
# Claude Plugins Official

**Skill ID:** `claude_plugins_official` | **Domain:** `forms` | **Tier:** 3

## Summary
A curated directory of high-quality plugins for Claude Code.

## Usage
Consult `payload/` for concrete source code and implementation patterns.

```

## File: schema.json
```
{
  "id": "claude_plugins_official",
  "name": "Claude Plugins Official",
  "version": "1.0.0",
  "tier": 3,
  "status": "active",
  "domain": "forms",
  "cost_tier": "standard",
  "load_on_boot": false,
  "path": "$OMNICLAW_ROOT\\ecosystem\\skills\\claude_plugins_official\\SKILL.md",
  "accessible_by": [
    "Orchestrator",
    "Claude Code"
  ],
  "dependencies": [],
  "exposed_functions": [
    {
      "name": "reference",
      "description": "Reference for claude_plugins_official",
      "input": "string",
      "output": "string"
    }
  ],
  "consumed_by": [],
  "emits_events": [],
  "listens_to": [],
  "tags": [
    "forms"
  ]
}
```

## File: SKILL.md
```
---
id: claude_plugins_official
name: Claude Plugins Official
version: 1.0.0
tier: 3
status: active
author: OA Forge Pipeline
updated: 2026-04-09
domain: forms
cost_tier: standard
load_on_boot: false
accessible_by:
  - Orchestrator
  - Claude Code
dependencies: []
exposed_functions:
  - name: reference
    description: Reference knowledge and templates from claude_plugins_official.
    input: query string
    output: code snippets, documentation, patterns
consumed_by: []
emits_events: []
listens_to: []
tags: ["forms"]
---

# Claude Plugins Official

## Overview
A curated directory of high-quality plugins for Claude Code.

## Usage
Agents working on `forms` tasks should reference this skill.
Inspect `payload/` for concrete source code and implementation patterns.

## Key Capabilities
- Domain: `forms`
- Source templates available in `payload/`
- Tags: forms

```

## File: _DIR_IDENTITY.md
```
---
id: claude_plugins_official
type: skill
owner: OA Forge Pipeline
registered_at: 2026-04-09
tags: ["forms", "forge-in-place", "forms"]
---

# Claude Plugins Official

Forged in-place from raw repository: `claude_plugins_official`
Domain: `forms`

```

## File: payload\DEEP_KNOWLEDGE.md
```
# Deep Matrix Profile: FETCHED_claude-plugins-official_123528

# DEEP\_KNOWLEDGE.md: Architectural Analysis of the Claude Code Plugin Ecosystem

This report analyzes the source code of the Claude Code Plugin Repository, detailing its architectural patterns, core algorithms, and primary mechanisms for integrating external and internal tooling. The repository adheres to a strict **Model Context Protocol (MCP)**, establishing a standardized, isolated, and highly controlled environment for plugin execution.

---

## 🏛️ I. Architectural Overview: The Model Context Protocol (MCP)

The entire system is built around the concept of the Model Context Protocol (MCP). This protocol dictates that plugins must operate as self-contained, process-isolated servers that communicate solely via Standard Input/Output (STDIO).

### A. Core Architectural Pattern: Process Isolation & STDIN/STDOUT
1. **Decoupling:** Each external plugin (Discord, Telegram, iMessage, etc.) runs as a separate, dedicated process spawned by the main Claude Code runtime. This prevents a failure in one plugin from crashing the entire system.
2. **Communication Channel:** All interaction—tool requests, tool results, and system messages—are serialized JSON objects passed over `stdin` and read from `stdout`.
3. **Tool Calling Interface:** The plugin exposes its capabilities (tools) by implementing specific request handlers (`ListToolsRequestSchema`, `CallToolRequestSchema`), allowing the LLM to interact with the plugin's functionality programmatically, rather than just through conversational text.

### B. Security and State Management
*   **Credential Handling:** Sensitive credentials (e.g., `DISCORD_BOT_TOKEN`, `TELEGRAM_BOT_TOKEN`) are loaded from a dedicated, permission-locked `.env` file (`chmodSync(ENV_FILE, 0o600)`). This enforces strict ownership and limits exposure.
*   **State Persistence:** Each channel maintains a dedicated state directory (`~/.claude/channels/<plugin>/`) containing `access.json` and `inbox/outbox` directories. This structure enforces granular, per-channel access control and history management.
*   **Safety Net:** All plugins implement `process.on('unhandledRejection')` and `process.on('uncaughtException')` handlers. This is a critical resilience pattern, ensuring that even catastrophic runtime errors are logged to `stderr` rather than causing a silent process death, thus maintaining the tool-serving capability.

---

## ⚙️ II. Plugin-Specific Mechanisms and Constraints

The plugins demonstrate diverse mechanisms tailored to their respective external services, while maintaining the MCP contract.

### A. `external_plugins\discord\server.ts` (Discord)
*   **Mechanism:** Uses the `discord.js` library to interact with the Discord API.
*   **Constraint Enforcement:** The code explicitly notes that Discord's search API is not exposed to bots, limiting the plugin's lookback capability to `fetch_messages` only.
*   **State Management:** Manages state via `~/.claude/channels/discord/access.json`, indicating a dedicated skill (`/discord:access`) handles pairing and permission granting.
*   **Key Feature:** Supports advanced features like guild-channel support and mention-triggering, requiring complex state tracking.

### B. `external_plugins\telegram\server.ts` (Telegram)
*   **Mechanism:** Utilizes the `grammy` library for bot interaction.
*   **Constraint Enforcement:** Acknowledges the limitation that the Telegram Bot API lacks history or search capabilities, restricting the plugin to "Reply-only tools."
*   **State Management:** Similar to Discord, uses `~/.claude/channels/telegram/access.json` and an `.env` file for token management.
*   **Architecture:** Highly focused on secure credential loading and explicit error handling for token validation.

### C. `external_plugins\imessage\server.ts` (iMessage)
*   **Mechanism:** This is the most complex and OS-dependent plugin. It bypasses network APIs entirely, relying on local system access.
    *   **History:** Reads the SQLite database (`~/Library/Messages/chat.db`).
    *   **Sending:** Uses `child_process.spawnSync` to execute `osascript` (AppleScript) to interact with the native Messages.app.
*   **Critical Dependencies/Risks:**
    1.  **Permissions:** Requires **Full Disk Access** (a major system-level permission) to read the `chat.db`.
    2.  **Automation:** Requires specific **Automation permissions** for Messages.app.
*   **Design Pattern:** This plugin exemplifies the "Local System Integration" pattern, where the MCP is adapted to bridge LLM capabilities with deep, OS-level APIs, bypassing standard internet protocols.

### D. `external_plugins\fakechat\server.ts` (FakeChat)
*   **Mechanism:** A purely local, simulated environment. It uses `bun`'s `ServerWebSocket` to manage multiple connected clients.
*   **Purpose:** Serves as a controlled testing sandbox for the channel contract.
*   **Tooling:** Defines specialized tools (`reply`, `edit_message`) that mimic real-world chat interactions but operate only within the local process memory, ensuring no external service calls are made.

---

## 🐍 III. Deep Dive: The `hookify` Plugin (The Interception Layer)

The `hookify` plugin is the most sophisticated component, implementing a **Cross-Cutting Concern** pattern. It does not interact with an external service but intercepts and modifies the core execution flow of the Claude Code agent.

### A. Core Algorithm: Rule Matching and Evaluation
The `RuleEngine` class implements a state machine evaluation algorithm:

1.  **Input Capture:** The plugin hooks into specific lifecycle events (`PreToolUse`, `PostToolUse`, `Stop`, `UserPromptSubmit`).
2.  **Configuration Loading (`config_loader.py`):**
    *   It parses Markdown files (`.local.md`) which contain YAML frontmatter.
    *   It uses dataclasses (`Condition`, `Rule`) to structure the rules, supporting two modes: **Legacy Pattern Matching** (simple regex on one field) and **Modern Condition Lists** (structured list of `field: operator: pattern`).
3.  **Condition Evaluation (`RuleEngine`):**
    *   The `_rule_matches` method iterates through the rule's `conditions`.
    *   It uses `re.compile` with `@lru_cache` to optimize regex matching performance, preventing redundant compilation of patterns.
    *   A rule matches only if *all* defined conditions evaluate to `True` against the `input_data` (e.g., `tool_name`, `tool_input`).
4.  **Decision Logic (Prioritization):**
    *   The engine separates matching rules into two categories: `blocking_rules` (action='block') and `warning_rules` (action='warn').
    *   **Priority Rule:** If *any* blocking rule matches, the operation is immediately halted (`decision: "block"`).
    *   **Warning Rule:** If no blocking rules match, but warning rules do, the operation proceeds, but the system message is polluted with warnings.
    *   **Success:** If no rules match, the operation proceeds silently.

### B. Hook Execution Flow (The Hooks)
The plugin utilizes a dedicated hook for each lifecycle event, ensuring the correct context is passed:

| Hook File | Event Trigger | Input Data Focus | Output Action |
| :--- | :--- | :--- | :--- |
| `pretooluse.py` | Before tool execution | `tool_name`, `tool_input` | **Deny/Allow:** Can block the tool call entirely. |
| `posttooluse.py` | After tool execution | `tool_name`, `tool_input` | **System Message:** Can inject context or warnings based on the result. |
| `stop.py` | Agent decides to stop | N/A (Stop signal) | **System Message:** Controls the final output message. |
| `userpromptsubmit.py` | User submits prompt | Full prompt context | **System Message:** Allows pre-processing or modification of the user's input. |

---

## 📊 IV. Summary of Architectural Patterns

| Pattern | Description | Implementation Example | Benefit |
| :--- | :--- | :--- | :--- |
| **Microservice/Process Isolation** | Running each plugin in its own dedicated process. | All `external_plugins/*server.ts` | Fault tolerance; failure containment. |
| **Observer/Event Hooking** | The `hookify` plugin listens to specific lifecycle events. | `pretooluse.py`, `posttooluse.py` | Non-invasive interception of core logic flow. |
| **State Pattern** | Managing distinct, persistent state for each channel/plugin. | `access.json`, `inbox/outbox` directories. | Contextual awareness and history tracking. |
| **Strategy Pattern** | The `RuleEngine` uses different matching strategies (regex vs. structured conditions). | `Condition` class structure. | Flexibility in defining complex, evolving business logic. |
| **Facade Pattern** | The `RuleEngine` provides a simple `evaluate_rules` interface, hiding the complexity of regex compilation, event mapping, and priority logic. | `RuleEngine.evaluate_rules()` | Clean, predictable API for the calling agent. |
```

## File: payload\README.md
```
# Claude Code Plugins Directory

A curated directory of high-quality plugins for Claude Code.

> **⚠️ Important:** Make sure you trust a plugin before installing, updating, or using it. Anthropic does not control what MCP servers, files, or other software are included in plugins and cannot verify that they will work as intended or that they won't change. See each plugin's homepage for more information.

## Structure

- **`/plugins`** - Internal plugins developed and maintained by Anthropic
- **`/external_plugins`** - Third-party plugins from partners and the community

## Installation

Plugins can be installed directly from this marketplace via Claude Code's plugin system.

To install, run `/plugin install {plugin-name}@claude-plugins-official`

or browse for the plugin in `/plugin > Discover`

## Contributing

### Internal Plugins

Internal plugins are developed by Anthropic team members. See `/plugins/example-plugin` for a reference implementation.

### External Plugins

Third-party partners can submit plugins for inclusion in the marketplace. External plugins must meet quality and security standards for approval. To submit a new plugin, use the [plugin directory submission form](https://clau.de/plugin-directory-submission).

## Plugin Structure

Each plugin follows a standard structure:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json      # Plugin metadata (required)
├── .mcp.json            # MCP server configuration (optional)
├── commands/            # Slash commands (optional)
├── agents/              # Agent definitions (optional)
├── skills/              # Skill definitions (optional)
└── README.md            # Documentation
```

## License

Please see each linked plugin for the relevant LICENSE file.

## Documentation

For more information on developing Claude Code plugins, see the [official documentation](https://code.claude.com/docs/en/plugins).

```

## File: payload\upgrade_proposal.md
```
# System Upgrade Proposal: FETCHED_claude-plugins-official_123528

> [!TIP]
> This actionable proposal was automatically drafted by OA Academy because this repository scored 8/10.

## Application Vision for OmniClaw
OmniClaw can integrate this structure by treating the plugin directory definitions (e.g., `plugin.json`, `commands/`, `agents/`) as a standardized manifest for external tool integration. Instead of relying solely on Anthropic's system, OmniClaw would parse these manifests to dynamically register new capabilities (skills/tools) into its own core OS, allowing it to execute third-party logic (MCP servers) directly within its multi-agent execution loop, effectively creating a universal plugin gateway for AI agents.

## Next Action Items
1. Review the `DEEP_KNOWLEDGE.md` to understand the architecture.
2. Isolate the target modules identified in the vision.
3. Wrap the modules into an OmniClaw Skill or Agent in `ecosystem/`.

```

## File: payload\_DIR_IDENTITY.md
```
---
id: claude_plugins_official
type: plugin
owner: OA
registered_at: 2026-04-09T17:28:24.320584
tags: ["auto-cloned", "plugin", "directory", "Claude Code", "oa-assimilated"]
---

# claude_plugins_official

## Assimilation Report
This repository serves as a directory for plugins designed for use with Claude Code, including both internal and external plugins. It emphasizes the importance of trusting plugins before installation and provides guidelines for contributing and using them.

## Application for OmniClaw
OmniClaw can integrate this plugin directory into its own ecosystem to manage and distribute AI plugins. By adopting a similar structure, OmniClaw could provide a curated marketplace for its own plugins, ensuring quality control and user trust. This integration would enhance the overall usability and security of the platform.

```

## File: payload\.claude-plugin\marketplace.json
```
{
  "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
  "name": "claude-plugins-official",
  "description": "Directory of popular Claude Code extensions including development tools, productivity plugins, and MCP integrations",
  "owner": {
    "name": "Anthropic",
    "email": "support@anthropic.com"
  },
  "plugins": [
    {
      "name": "adspirer-ads-agent",
      "description": "Cross-platform ad management for Google Ads, Meta Ads, TikTok Ads, and LinkedIn Ads. 91 tools for keyword research, campaign creation, performance analysis, and budget optimization.",
      "category": "productivity",
      "source": {
        "source": "url",
        "url": "https://github.com/amekala/adspirer-mcp-plugin.git",
        "sha": "aa70dbdbbbb843e94a794c10c2b13f5dd66b5e40"
      },
      "homepage": "https://www.adspirer.com"
    },
    {
      "name": "agent-sdk-dev",
      "description": "Development kit for working with the Claude Agent SDK",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/agent-sdk-dev",
      "category": "development",
      "homepage": "https://github.com/anthropics/claude-plugins-public/tree/main/plugins/agent-sdk-dev"
    },
    {
      "name": "ai-firstify",
      "description": "AI-first project auditor and re-engineer based on the 9 design principles and 7 design patterns from the TechWolf AI-First Bootcamp",
      "source": {
        "source": "git-subdir",
        "url": "techwolf-ai/ai-first-toolkit",
        "path": "plugins/ai-firstify",
        "ref": "main",
        "sha": "7f18e11d694b9ae62ea3009fbbc175f08ae913df"
      },
      "homepage": "https://ai-first.techwolf.ai"
    },
    {
      "name": "ai-plugins",
      "description": "Set up endorctl and use Endor Labs to scan, prioritize, and fix security risks across your software supply chain",
      "source": {
        "source": "url",
        "url": "https://github.com/endorlabs/ai-plugins.git",
        "sha": "a0f1d5632b6f9e6c26eaa9806f5d8d454ca5b06f"
      },
      "homepage": "https://www.endorlabs.com"
    },
    {
      "name": "aikido",
      "description": "Aikido Security scanning for Claude Code — SAST, secrets, and IaC vulnerability detection powered by the Aikido MCP server.",
      "source": {
        "source": "url",
        "url": "https://github.com/AikidoSec/aikido-claude-plugin.git",
        "sha": "d7fa8b8e192680d9a26c1a5dcaead7cf5cdb7139"
      },
      "homepage": "https://github.com/AikidoSec/aikido-claude-plugin"
    },
    {
      "name": "amazon-location-service",
      "description": "Guide developers through adding maps, places search, geocoding, routing, and other geospatial features with Amazon Location Service, including authentication setup, SDK integration, and best practices.",
      "category": "location",
      "source": {
        "source": "git-subdir",
        "url": "https://github.com/awslabs/agent-plugins.git",
        "path": "plugins/amazon-location-service",
        "ref": "main"
      },
      "homepage": "https://github.com/awslabs/agent-plugins"
    },
    {
      "name": "asana",
      "description": "Asana project management integration. Create and manage tasks, search projects, update assignments, track progress, and integrate your development workflow with Asana's work management platform.",
      "category": "productivity",
      "source": "./external_plugins/asana",
      "homepage": "https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/asana"
    },
    {
      "name": "astronomer-data-agents",
      "description": "Data engineering for Apache Airflow and Astronomer. Author DAGs with best practices, debug pipeline failures, trace data lineage, profile tables, migrate Airflow 2 to 3, and manage local and cloud deployments.",
      "category": "development",
      "source": {
        "source": "url",
        "url": "https://github.com/astronomer/agents.git",
        "sha": "7ef022b02f5296b5ecc52ba0db3ba9345ec03c9e"
      },
      "homepage": "https://github.com/astronomer/agents"
    },
    {
      "name": "atlan",
      "description": "Atlan data catalog plugin for Claude Code. Search, explore, govern, and manage your data assets through natural language. Powered by the Atlan MCP server with semantic search, lineage traversal, glossary management, data quality rules, and more.",
      "source": {
        "source": "url",
        "url": "https://github.com/atlanhq/agent-toolkit.git",
        "sha": "acdf284da6aa98b14f8dad90a9827006d8df425c"
      },
      "homepage": "https://docs.atlan.com/"
    },
    {
      "name": "atlassian",
      "description": "Connect to Atlassian products including Jira and Confluence. Search and create issues, access documentation, manage sprints, and integrate your development workflow with Atlassian's collaboration tools.",
      "category": "productivity",
      "source": {
        "source": "url",
        "url": "https://github.com/atlassian/atlassian-mcp-server.git"
      },
      "homepage": "https://github.com/atlassian/atlassian-mcp-server"
    },
    {
      "name": "atomic-agents",
      "description": "Comprehensive development workflow for building AI agents with the Atomic Agents framework. Includes specialized agents for schema design, architecture planning, code review, and tool development. Features guided workflows, progressive-disclosure skills, and best practice validation.",
      "category": "development",
      "source": {
        "source": "url",
        "url": "https://github.com/BrainBlend-AI/atomic-agents.git",
        "path": "claude-plugin/atomic-agents"
      },
      "homepage": "https://github.com/BrainBlend-AI/atomic-agents",
      "tags": [
        "community-managed"
      ]
    },
    {
      "name": "autofix-bot",
      "description": "Code review agent that detects security vulnerabilities, code quality issues, and hardcoded secrets. Combines 5,000+ static analyzers to scan your code and dependencies for CVEs.",
      "author": {
        "name": "DeepSource Corp"
      },
      "category": "security",
      "source": "./external_plugins/autofix-bot",
      "homepage": "https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/autofix-bot"
    },
    {
      "name": "aws-serverless",
      "description": "Design, build, deploy, test, and debug serverless applications with AWS Serverless services.",
      "category": "development",
      "source": {
        "source": "git-subdir",
        "url": "https://github.com/awslabs/agent-plugins.git",
        "path": "plugins/aws-serverless",
        "ref": "main"
      },
      "homepage": "https://github.com/awslabs/agent-plugins"
    },
    {
      "name": "brightdata-plugin",
      "description": "Web scraping, Google search, structured data extraction, and MCP server integration powered by Bright Data. Includes 7 skills: scrape any webpage as markdown (with bot detection/CAPTCHA bypass), search Google with structured JSON results, extract data from 40+ websites (Amazon, LinkedIn, Instagram, TikTok, YouTube, and more), orchestrate Bright Data's 60+ MCP tools, built-in best practices for Web Unlocker, SERP API, Web Scraper API, and Browser API, Python SDK best practices for the brightda...",
      "source": {
        "source": "url",
        "url": "https://github.com/brightdata/skills.git",
        "sha": "e671da495f7ec0ed6be5e9fa71e260f886a1dc36"
      },
      "homepage": "https://docs.brightdata.com"
    },
    {
      "name": "chrome-devtools-mcp",
      "description": "Control and inspect a live Chrome browser from your coding agent. Record performance traces, analyze network requests, check console messages with source-mapped stack traces, and automate browser actions with Puppeteer.",
      "category": "development",
      "source": {
        "source": "url",
        "url": "https://github.com/ChromeDevTools/chrome-devtools-mcp.git",
        "sha": "c2d8009ff75f76bce1ec4cf79c2467b50d81725e"
      },
      "homepage": "https://github.com/ChromeDevTools/chrome-devtools-mcp"
    },
    {
      "name": "circleback",
      "description": "Circleback conversational context integration. Search and access meetings, emails, calendar events, and more.",
      "category": "productivity",
      "source": {
        "source": "url",
        "url": "https://github.com/circlebackai/claude-code-plugin.git"
      },
      "homepage": "https://github.com/circlebackai/claude-code-plugin.git"
    },
    {
      "name": "clangd-lsp",
      "description": "C/C++ language server (clangd) for code intelligence",
      "version": "1.0.0",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/clangd-lsp",
      "category": "development",
      "strict": false,
      "lspServers": {
        "clangd": {
          "command": "clangd",
          "args": [
            "--background-index"
          ],
          "extensionToLanguage": {
            ".c": "c",
            ".h": "c",
            ".cpp": "cpp",
            ".cc": "cpp",
            ".cxx": "cpp",
            ".hpp": "cpp",
            ".hxx": "cpp",
            ".C": "cpp",
            ".H": "cpp"
          }
        }
      }
    },
    {
      "name": "claude-code-setup",
      "description": "Analyze codebases and recommend tailored Claude Code automations such as hooks, skills, MCP servers, and subagents.",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/claude-code-setup",
      "category": "productivity",
      "homepage": "https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-code-setup"
    },
    {
      "name": "claude-md-management",
      "description": "Tools to maintain and improve CLAUDE.md files - audit quality, capture session learnings, and keep project memory current.",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/claude-md-management",
      "category": "productivity",
      "homepage": "https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-md-management"
    },
    {
      "name": "cloudinary",
      "description": "Use Cloudinary directly in Claude. Manage assets, apply transformations, optimize media, and more through natural conversation.",
      "source": {
        "source": "url",
        "url": "https://github.com/cloudinary-devs/cloudinary-plugin.git",
        "sha": "137c5d7acd9c3f10e80cd2a400486971e1664f31"
      },
      "homepage": "https://cloudinary.com/documentation"
    },
    {
      "name": "cockroachdb",
      "description": "CockroachDB plugin for Claude Code — explore schemas, write optimized SQL, debug queries, and manage distributed database clusters directly from your AI coding agent.",
      "source": {
        "source": "url",
        "url": "https://github.com/cockroachdb/claude-plugin.git",
        "sha": "a54566e03c852567589ef85bb449d1e4de229667"
      },
      "homepage": "https://github.com/cockroachdb/claude-plugin"
    },
    {
      "name": "code-review",
      "description": "Automated code review for pull requests using multiple specialized agents with confidence-based scoring to filter false positives",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/code-review",
      "category": "productivity",
      "homepage": "https://github.com/anthropics/claude-plugins-public/tree/main/plugins/code-review"
    },
    {
      "name": "code-simplifier",
      "description": "Agent that simplifies and refines code for clarity, consistency, and maintainability while preserving functionality. Focuses on recently modified code.",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/code-simplifier",
      "category": "productivity",
      "homepage": "https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-simplifier"
    },
    {
      "name": "coderabbit",
      "description": "Your code review partner. CodeRabbit provides external validation using a specialized AI architecture and 40+ integrated static analyzers—offering a different perspective that catches bugs, security vulnerabilities, logic errors, and edge cases. Context-aware analysis via AST parsing and codegraph relationships. Automatically incorporates CLAUDE.md and project coding guidelines into reviews. Useful after writing or modifying code, before commits, when implementing complex or security-sensitive logic, or when a second opinion would increase confidence in the changes. Returns specific findings with suggested fixes that can be applied immediately. Free to use.",
      "category": "productivity",
      "source": {
        "source": "url",
        "url": "https://github.com/coderabbitai/claude-plugin.git"
      },
      "homepage": "https://github.com/coderabbitai/claude-plugin.git"
    },
    {
      "name": "commit-commands",
      "description": "Commands for git commit workflows including commit, push, and PR creation",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/commit-commands",
      "category": "productivity",
      "homepage": "https://github.com/anthropics/claude-plugins-public/tree/main/plugins/commit-commands"
    },
    {
      "name": "context7",
      "description": "Upstash Context7 MCP server for up-to-date documentation lookup. Pull version-specific documentation and code examples directly from source repositories into your LLM context.",
      "category": "development",
      "source": "./external_plugins/context7",
      "homepage": "https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/context7",
      "tags": [
        "community-managed"
      ]
    },
    {
      "name": "csharp-lsp",
      "description": "C# language server for code intelligence",
      "version": "1.0.0",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/csharp-lsp",
      "category": "development",
      "strict": false,
      "lspServers": {
        "csharp-ls": {
          "command": "csharp-ls",
          "extensionToLanguage": {
            ".cs": "csharp"
          }
        }
      }
    },
    {
      "name": "data",
      "description": "Data engineering for Apache Airflow and Astronomer. Author DAGs with best practices, debug pipeline failures, trace data lineage, profile tables, migrate Airflow 2 to 3, and manage local and cloud deployments.",
      "category": "development",
      "source": {
        "source": "url",
        "url": "https://github.com/astronomer/agents.git",
        "sha": "7ef022b02f5296b5ecc52ba0db3ba9345ec03c9e"
      },
      "homepage": "https://github.com/astronomer/agents"
    },
    {
      "name": "data-engineering",
      "description": "Data engineering plugin - warehouse exploration, pipeline authoring, Airflow integration",
      "source": {
        "source": "url",
        "url": "https://github.com/astronomer/agents.git",
        "sha": "85d6053b1e21724f9cefb1e3f5219bd54fc77224"
      },
      "homepage": "https://github.com/astronomer/agents"
    },
    {
      "name": "deploy-on-aws",
      "description": "Deploy applications to AWS with architecture recommendations, cost estimates, and IaC deployment.",
      "category": "deployment",
      "source": {
        "source": "git-subdir",
        "url": "https://github.com/awslabs/agent-plugins.git",
        "path": "plugins/deploy-on-aws",
        "ref": "main"
      },
      "homepage": "https://github.com/awslabs/agent-plugins"
    },
    {
      "name": "discord",
      "description": "Discord messaging bridge with built-in access control. Manage pairing, allowlists, and policy via /discord:access.",
      "category": "productivity",
      "source": "./external_plugins/discord"
    },
    {
      "name": "elixir-ls-lsp",
      "description": "Elixir language server (ElixirLS) for Claude Code — provides code intelligence and diagnostics for .ex, .exs, and .heex files.",
      "source": {
        "source": "url",
        "url": "https://github.com/MikaelFangel/claude-elixir-ls-lsp.git",
        "sha": "806a6eeeb88b9a306a59b3212a1d5d88aa5c70af"
      },
      "homepage": "https://elixir-lsp.github.io/elixir-ls/"
    },
    {
      "name": "explanatory-output-style",
      "description": "Adds educational insights about implementation choices and codebase patterns (mimics the deprecated Explanatory output style)",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/explanatory-output-style",
      "category": "learning",
      "homepage": "https://github.com/anthropics/claude-plugins-public/tree/main/plugins/explanatory-output-style"
    },
    {
      "name": "fakechat",
      "description": "Localhost web chat for testing the channel notification flow. No tokens, no access control, no third-party service.",
      "category": "development",
      "source": "./external_plugins/fakechat"
    },
    {
      "name": "fastly-agent-toolkit",
      "description": "Fastly development tools and platform skills",
      "source": {
        "source": "url",
        "url": "https://github.com/fastly/fastly-agent-toolkit.git",
        "sha": "d9ba949011e725be55cae11acc741aa1f1f393d3"
      },
      "homepage": "https://github.com/fastly/fastly-agent-toolkit/blob/main/README.md"
    },
    {
      "name": "feature-dev",
      "description": "Comprehensive feature development workflow with specialized agents for codebase exploration, architecture design, and quality review",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/feature-dev",
      "category": "development",
      "homepage": "https://github.com/anthropics/claude-plugins-public/tree/main/plugins/feature-dev"
    },
    {
      "name": "fiftyone",
      "description": "Build high-quality datasets and computer vision models. Visualize datasets, analyze models, find duplicates, run inference, evaluate predictions, and develop custom plugins.",
      "source": {
        "source": "url",
        "url": "https://github.com/voxel51/fiftyone-skills.git",
        "sha": "593e0553fc9fd94db52386ada2c9e2074a6ecf89"
      },
      "homepage": "https://docs.voxel51.com/"
    },
    {
      "name": "figma",
      "description": "Figma design platform integration. Access design files, extract component information, read design tokens, and translate designs into code. Bridge the gap between design and development workflows.",
      "category": "design",
      "source": {
        "source": "url",
        "url": "https://github.com/figma/mcp-server-guide.git"
      },
      "homepage": "https://github.com/figma/mcp-server-guide"
    },
    {
      "name": "firebase",
      "description": "Google Firebase MCP integration. Manage Firestore databases, authentication, cloud functions, hosting, and storage. Build and manage your Firebase backend directly from your development workflow.",
      "category": "database",
      "source": "./external_plugins/firebase",
      "homepage": "https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/firebase"
    },
    {
      "name": "firecrawl",
      "description": "Web scraping and crawling powered by Firecrawl. Turn any website into clean, LLM-ready markdown or structured data. Scrape single pages, crawl entire sites, search the web, and extract structured information. Includes an AI agent for autonomous multi-source data gathering - just describe what you need and it finds, navigates, and extracts automatically.",
      "category": "development",
      "source": {
        "source": "url",
        "url": "https://github.com/firecrawl/firecrawl-claude-plugin.git"
      },
      "homepage": "https://github.com/firecrawl/firecrawl-claude-plugin.git"
    },
    {
      "name": "firetiger",
      "description": "Claude Code plugin for Firetiger observability workflows and MCP-powered investigations.",
      "source": {
        "source": "url",
        "url": "https://github.com/firetiger-oss/claude-plugin.git",
        "sha": "51421ce20adc7c30eb014e6847c7087ed34cb879"
      },
      "homepage": "https://www.firetiger.com/"
    },
    {
      "name": "flint",
      "description": "Build and manage websites with Flint's AI website builder through natural conversation.",
      "source": {
        "source": "url",
        "url": "https://github.com/tryflint/claude-code-plugin.git",
        "sha": "f3d56e33ed2fb3ed9b4f02e0fc65d0a79b24bf4d"
      },
      "homepage": "https://www.tryflint.com/docs/claude-code-plugin"
    },
    {
      "name": "followrabbit",
      "description": "Cloud cost optimization for GCP infrastructure. Review changes for cost impact and auto-apply savings recommendations using the followrabbit CLI.",
      "source": {
        "source": "url",
        "url": "https://github.com/followrabbit-ai/awesome-rabbit.git",
        "sha": "f59ec3d1f6337a6ed825ef06836a221ed3d2ffb0"
      },
      "homepage": "https://subscriptions.agentic.followrabbit.ai/"
    },
    {
      "name": "frontend-design",
      "description": "Create distinctive, production-grade frontend interfaces with high design quality. Generates creative, polished code that avoids generic AI aesthetics.",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/frontend-design",
      "category": "development",
      "homepage": "https://github.com/anthropics/claude-plugins-public/tree/main/plugins/frontend-design"
    },
    {
      "name": "github",
      "description": "Official GitHub MCP server for repository management. Create issues, manage pull requests, review code, search repositories, and interact with GitHub's full API directly from Claude Code.",
      "category": "productivity",
      "source": "./external_plugins/github",
      "homepage": "https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/github"
    },
    {
      "name": "gitlab",
      "description": "GitLab DevOps platform integration. Manage repositories, merge requests, CI/CD pipelines, issues, and wikis. Full access to GitLab's comprehensive DevOps lifecycle tools.",
      "category": "productivity",
      "source": "./external_plugins/gitlab",
      "homepage": "https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/gitlab"
    },
    {
      "name": "goodmem",
      "description": "GoodMem memory infrastructure for AI agents. Use Python SDK skills to write code that manages embedders, spaces, and memories, or use MCP tools to perform GoodMem operations directly via natural language.",
      "source": {
        "source": "url",
        "url": "https://github.com/PAIR-Systems-Inc/goodmem-claude-code-plugin.git",
        "sha": "215568baf203887b5d7f8245e0503dd4a81336c2"
      },
      "homepage": "https://github.com/PAIR-Systems-Inc/goodmem-claude-code-plugin"
    },
    {
      "name": "gopls-lsp",
      "description": "Go language server for code intelligence and refactoring",
      "version": "1.0.0",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/gopls-lsp",
      "category": "development",
      "strict": false,
      "lspServers": {
        "gopls": {
          "command": "gopls",
          "extensionToLanguage": {
            ".go": "go"
          }
        }
      }
    },
    {
      "name": "greptile",
      "description": "AI-powered codebase search and understanding. Query your repositories using natural language to find relevant code, understand dependencies, and get contextual answers about your codebase architecture.",
      "category": "development",
      "source": "./external_plugins/greptile",
      "homepage": "https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/greptile"
    },
    {
      "name": "helius",
      "description": "Build on Solana with Helius — live blockchain tools, expert coding patterns, and autonomous account signup",
      "source": {
        "source": "git-subdir",
        "url": "helius-labs/core-ai",
        "path": "helius-plugin",
        "ref": "main",
        "sha": "05ea4d1128d46618266bbcc23a5e7019c57be0d6"
      },
      "homepage": "https://www.helius.dev/docs"
    },
    {
      "name": "hookify",
      "description": "Easily create custom hooks to prevent unwanted behaviors by analyzing conversation patterns or from explicit instructions. Define rules via simple markdown files.",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/hookify",
      "category": "productivity",
      "homepage": "https://github.com/anthropics/claude-plugins-public/tree/main/plugins/hookify"
    },
    {
      "name": "huggingface-skills",
      "description": "Build, train, evaluate, and use open source AI models, datasets, and spaces.",
      "category": "development",
      "source": {
        "source": "url",
        "url": "https://github.com/huggingface/skills.git"
      },
      "homepage": "https://github.com/huggingface/skills.git"
    },
    {
      "name": "imessage",
      "description": "iMessage messaging bridge with built-in access control. Reads chat.db directly, sends via AppleScript. Manage pairing, allowlists, and policy via /imessage:access.",
      "category": "productivity",
      "source": "./external_plugins/imessage"
    },
    {
      "name": "intercom",
      "description": "Intercom integration for Claude Code. Search conversations, analyze customer support patterns, look up contacts and companies, and install the Intercom Messenger. Connect your Intercom workspace to get real-time insights from customer data.",
      "category": "productivity",
      "source": {
        "source": "url",
        "url": "https://github.com/intercom/claude-plugin-external.git",
        "sha": "eeef353eead2e3dc5f33f64dbaae54e1309e0d45"
      },
      "homepage": "https://github.com/intercom/claude-plugin-external"
    },
    {
      "name": "jdtls-lsp",
      "description": "Java language server (Eclipse JDT.LS) for code intelligence",
      "version": "1.0.0",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/jdtls-lsp",
      "category": "development",
      "strict": false,
      "lspServers": {
        "jdtls": {
          "command": "jdtls",
          "extensionToLanguage": {
            ".java": "java"
          },
          "startupTimeout": 120000
        }
      }
    },
    {
      "name": "kotlin-lsp",
      "description": "Kotlin language server for code intelligence",
      "version": "1.0.0",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/kotlin-lsp",
      "category": "development",
      "strict": false,
      "lspServers": {
        "kotlin-lsp": {
          "command": "kotlin-lsp",
          "args": [
            "--stdio"
          ],
          "extensionToLanguage": {
            ".kt": "kotlin",
            ".kts": "kotlin"
          },
          "startupTimeout": 120000
        }
      }
    },
    {
      "name": "laravel-boost",
      "description": "Laravel development toolkit MCP server. Provides intelligent assistance for Laravel applications including Artisan commands, Eloquent queries, routing, migrations, and framework-specific code generation.",
      "category": "development",
      "source": "./external_plugins/laravel-boost",
      "homepage": "https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/laravel-boost"
    },
    {
      "name": "learning-output-style",
      "description": "Interactive learning mode that requests meaningful code contributions at decision points (mimics the unshipped Learning output style)",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/learning-output-style",
      "category": "learning",
      "homepage": "https://github.com/anthropics/claude-plugins-public/tree/main/plugins/learning-output-style"
    },
    {
      "name": "legalzoom",
      "description": "Attorney guidance and legal tools for business and personal needs. AI-powered document review identifies critical risks and important clauses, advises when to engage an attorney, and routes to LegalZoom's network when professional expertise is needed.",
      "category": "productivity",
      "source": {
        "source": "git-subdir",
        "url": "legalzoom/claude-plugins",
        "path": "plugins/legalzoom",
        "ref": "main",
        "sha": "f9fd8a0ca6e1421bc1aacb113a109663a7a6f6d8"
      },
      "homepage": "https://www.legalzoom.com/"
    },
    {
      "name": "linear",
      "description": "Linear issue tracking integration. Create issues, manage projects, update statuses, search across workspaces, and streamline your software development workflow with Linear's modern issue tracker.",
      "category": "productivity",
      "source": "./external_plugins/linear",
      "homepage": "https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/linear"
    },
    {
      "name": "lua-lsp",
      "description": "Lua language server for code intelligence",
      "version": "1.0.0",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/lua-lsp",
      "category": "development",
      "strict": false,
      "lspServers": {
        "lua": {
          "command": "lua-language-server",
          "extensionToLanguage": {
            ".lua": "lua"
          }
        }
      }
    },
    {
      "name": "math-olympiad",
      "description": "Solve competition math (IMO, Putnam, USAMO) with adversarial verification that catches what self-verification misses. Fresh-context verifiers attack proofs with specific failure patterns. Calibrated abstention over bluffing.",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/math-olympiad",
      "category": "math",
      "homepage": "https://github.com/anthropics/claude-plugins-official/tree/main/plugins/math-olympiad"
    },
    {
      "name": "mcp-server-dev",
      "description": "Skills for designing and building MCP servers that work seamlessly with Claude. Guides you through deployment models (remote HTTP, MCPB, local), tool design patterns, auth, and interactive MCP apps.",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/mcp-server-dev",
      "category": "development",
      "homepage": "https://github.com/anthropics/claude-plugins-official/tree/main/plugins/mcp-server-dev"
    },
    {
      "name": "microsoft-docs",
      "description": "Access official Microsoft documentation, API references, and code samples for Azure, .NET, Windows, and more.",
      "category": "development",
      "source": {
        "source": "url",
        "url": "https://github.com/MicrosoftDocs/mcp.git"
      },
      "homepage": "https://github.com/microsoftdocs/mcp"
    },
    {
      "name": "migration-to-aws",
      "description": "Assess current cloud provider usage and billing to estimate and compare AWS services and pricing, with recommendations for migration or continued use of current provider.",
      "category": "migration",
      "source": {
        "source": "git-subdir",
        "url": "https://github.com/awslabs/agent-plugins.git",
        "path": "plugins/migration-to-aws",
        "ref": "main"
      },
      "homepage": "https://github.com/awslabs/agent-plugins"
    },
    {
      "name": "mintlify",
      "description": "Build beautiful documentation sites with Mintlify. Convert non-markdown files into properly formatted MDX pages, add and modify content with correct component use, and automate documentation updates.",
      "category": "development",
      "source": {
        "source": "url",
        "url": "https://github.com/mintlify/mintlify-claude-plugin.git",
        "sha": "ce435be18a700dc849d6a63a80da4816d1e2128c"
      },
      "homepage": "https://www.mintlify.com/"
    },
    {
      "name": "mongodb",
      "description": "Official Claude plugin for MongoDB (MCP Server + Skills). Connect to databases, explore data, manage collections, optimize queries, generate reliable code, implement best practices, develop advanced features, and more.",
      "category": "database",
      "source": {
        "source": "url",
        "url": "https://github.com/mongodb/agent-skills.git",
        "sha": "c47079f65e88a113c52d1ce0618684cef300246c"
      },
      "homepage": "https://www.mongodb.com/docs/mcp-server/overview/"
    },
    {
      "name": "neon",
      "description": "Manage your Neon projects and databases with the neon-postgres agent skill and the Neon MCP Server.",
      "category": "database",
      "source": {
        "source": "git-subdir",
        "url": "neondatabase/agent-skills",
        "path": "plugins/neon-postgres",
        "ref": "main",
        "sha": "54d7a9db2ddd476f84d5d1fd7bac323907858a8b"
      },
      "homepage": "https://github.com/neondatabase/agent-skills/tree/main/plugins/neon-postgres"
    },
    {
      "name": "netlify-skills",
      "description": "Netlify platform skills for Claude Code — functions, edge functions, blobs, database, image CDN, forms, config, CLI, frameworks, caching, AI gateway, and deployment.",
      "category": "development",
      "source": {
        "source": "url",
        "url": "https://github.com/netlify/context-and-tools.git"
      },
      "homepage": "https://github.com/netlify/context-and-tools"
    },
    {
      "name": "nightvision",
      "description": "Skills for working with NightVision, a DAST and API Discovery platform that finds exploitable vulnerabilities in web applications and REST APIs",
      "source": {
        "source": "url",
        "url": "https://github.com/nvsecurity/nightvision-skills.git",
        "sha": "7d7a3f342bbf4d02b6e012279800cf91ff0c1c97"
      },
      "homepage": "https://github.com/nvsecurity/nightvision-skills"
    },
    {
      "name": "nimble",
      "description": "Nimble web data toolkit — search, extract, map, crawl the web and work with structured data agents",
      "source": {
        "source": "url",
        "url": "https://github.com/Nimbleway/agent-skills.git",
        "sha": "cf391e95bd8ac009e3641f172434a1d130dde7fe"
      },
      "homepage": "https://docs.nimbleway.com/integrations/agent-skills/plugin-installation"
    },
    {
      "name": "notion",
      "description": "Notion workspace integration. Search pages, create and update documents, manage databases, and access your team's knowledge base directly from Claude Code for seamless documentation workflows.",
      "category": "productivity",
      "source": {
        "source": "url",
        "url": "https://github.com/makenotion/claude-code-notion-plugin.git"
      },
      "homepage": "https://github.com/makenotion/claude-code-notion-plugin"
    },
    {
      "name": "opsera-devsecops",
      "description": "Opsera DevSecOps Agent — AI-powered architecture analysis, security scanning, compliance auditing, and SQL security for your codebase. Free trial included.",
      "source": {
        "source": "url",
        "url": "https://github.com/opsera-agents/opsera-devsecops.git",
        "sha": "e797228134ee7d3199594eb0ee5a659df40c91da"
      },
      "homepage": "https://opsera.ai/agents"
    },
    {
      "name": "optibot",
      "description": "AI code review that catches production-breaking bugs, business logic issues, and security vulnerabilities — directly in Claude Code.",
      "source": {
        "source": "url",
        "url": "https://github.com/Optimal-AI/optibot-skill.git",
        "sha": "981db1f630c3116d7df0a71e5967af55b08e813c"
      },
      "homepage": "https://getoptimal.ai"
    },
    {
      "name": "pagerduty",
      "description": "Enhance code quality and security through PagerDuty risk scoring and incident correlation. Score pre-commit diffs against historical incident data and surface deployment risk before you ship.",
      "category": "monitoring",
      "source": {
        "source": "url",
        "url": "https://github.com/PagerDuty/claude-code-plugins.git",
        "sha": "b16c23e0d790deceaa7a6182616d0e36673f2eae"
      },
      "homepage": "https://github.com/PagerDuty/claude-code-plugins"
    },
    {
      "name": "php-lsp",
      "description": "PHP language server (Intelephense) for code intelligence",
      "version": "1.0.0",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/php-lsp",
      "category": "development",
      "strict": false,
      "lspServers": {
        "intelephense": {
          "command": "intelephense",
          "args": [
            "--stdio"
          ],
          "extensionToLanguage": {
            ".php": "php"
          }
        }
      }
    },
    {
      "name": "pinecone",
      "description": "Pinecone vector database integration. Streamline your Pinecone development with powerful tools for managing vector indexes, querying data, and rapid prototyping. Use slash commands like /quickstart to generate AGENTS.md files and initialize Python projects and /query to quickly explore indexes. Access the Pinecone MCP server for creating, describing, upserting and querying indexes with Claude. Perfect for developers building semantic search, RAG applications, recommendation systems, and other vector-based applications with Pinecone.",
      "category": "database",
      "source": {
        "source": "url",
        "url": "https://github.com/pinecone-io/pinecone-claude-code-plugin.git"
      },
      "homepage": "https://github.com/pinecone-io/pinecone-claude-code-plugin"
    },
    {
      "name": "planetscale",
      "description": "An authenticated hosted MCP server that accesses your PlanetScale organizations, databases, branches, schema, and Insights data. Query against your data, surface slow queries, and get organizational and account information.",
      "category": "database",
      "source": {
        "source": "url",
        "url": "https://github.com/planetscale/claude-plugin.git",
        "sha": "f1066cac5bb956bbbb05918f5b07fe0e873d44ea"
      },
      "homepage": "https://planetscale.com/"
    },
    {
      "name": "playground",
      "description": "Creates interactive HTML playgrounds — self-contained single-file explorers with visual controls, live preview, and prompt output with copy button. Includes templates for design playgrounds, data explorers, concept maps, and document critique.",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/playground",
      "category": "development",
      "homepage": "https://github.com/anthropics/claude-plugins-official/tree/main/plugins/playground"
    },
    {
      "name": "playwright",
      "description": "Browser automation and end-to-end testing MCP server by Microsoft. Enables Claude to interact with web pages, take screenshots, fill forms, click elements, and perform automated browser testing workflows.",
      "category": "testing",
      "source": "./external_plugins/playwright",
      "homepage": "https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/playwright"
    },
    {
      "name": "plugin-dev",
      "description": "Comprehensive toolkit for developing Claude Code plugins. Includes 7 expert skills covering hooks, MCP integration, commands, agents, and best practices. AI-assisted plugin creation and validation.",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/plugin-dev",
      "category": "development",
      "homepage": "https://github.com/anthropics/claude-plugins-public/tree/main/plugins/plugin-dev"
    },
    {
      "name": "posthog",
      "description": "Access PostHog analytics, feature flags, experiments, error tracking, and insights directly from Claude Code.",
      "category": "monitoring",
      "source": {
        "source": "url",
        "url": "https://github.com/PostHog/ai-plugin.git"
      },
      "homepage": "https://posthog.com/docs/model-context-protocol"
    },
    {
      "name": "postiz",
      "description": "Social media automation CLI for scheduling posts, managing integrations, uploading media, and tracking analytics across 28+ platforms including X, LinkedIn, Reddit, YouTube, TikTok, Instagram, and more",
      "source": {
        "source": "url",
        "url": "https://github.com/gitroomhq/postiz-agent.git",
        "sha": "c5d1bf5f7e95a71e230fc19ae2150ddd9c549854"
      },
      "homepage": "https://postiz.com/agent"
    },
    {
      "name": "postman",
      "description": "Full API lifecycle management for Claude Code. Sync collections, generate client code, discover APIs, run tests, create mocks, publish docs, and audit security. Powered by the Postman MCP Server.",
      "category": "development",
      "source": {
        "source": "url",
        "url": "https://github.com/Postman-Devrel/postman-claude-code-plugin.git",
        "sha": "40b11ac3466c500cf4625ac016d5c01cd00046f4"
      },
      "homepage": "https://learning.postman.com/docs/developer/postman-mcp-server/"
    },
    {
      "name": "pr-review-toolkit",
      "description": "Comprehensive PR review agents specializing in comments, tests, error handling, type design, code quality, and code simplification",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/pr-review-toolkit",
      "category": "productivity",
      "homepage": "https://github.com/anthropics/claude-plugins-public/tree/main/plugins/pr-review-toolkit"
    },
    {
      "name": "prisma",
      "description": "Prisma MCP integration for Postgres database management, schema migrations, SQL queries, and connection string management. Provision Prisma Postgres databases, run migrations, and interact with your data directly.",
      "source": {
        "source": "url",
        "url": "https://github.com/prisma/claude-plugin.git",
        "sha": "815dbc4a045a29e3b81510ba0e3ab806f1baaf0e"
      },
      "homepage": "https://prisma.io"
    },
    {
      "name": "product-tracking-skills",
      "description": "AI agent skills that make SaaS products data-ready for product analytics — from codebase scan to tracking plan to working instrumentation code.",
      "source": {
        "source": "url",
        "url": "https://github.com/Accoil/product-tracking-skills.git",
        "sha": "341f8cf47d8b5dda550222152377c50aee34c723"
      },
      "homepage": "https://www.accoil.com/product-tracking"
    },
    {
      "name": "pyright-lsp",
      "description": "Python language server (Pyright) for type checking and code intelligence",
      "version": "1.0.0",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/pyright-lsp",
      "category": "development",
      "strict": false,
      "lspServers": {
        "pyright": {
          "command": "pyright-langserver",
          "args": [
            "--stdio"
          ],
          "extensionToLanguage": {
            ".py": "python",
            ".pyi": "python"
          }
        }
      }
    },
    {
      "name": "qodo-skills",
      "description": "Qodo Skills provides a curated library of reusable AI agent capabilities that extend Claude's functionality for software development workflows. Each skill is designed to integrate seamlessly into your development process, enabling tasks like code quality checks, automated testing, security scanning, and compliance validation. Skills operate across your entire SDLC—from IDE to CI/CD—ensuring consistent standards and catching issues early.",
      "category": "development",
      "source": {
        "source": "url",
        "url": "https://github.com/qodo-ai/qodo-skills.git"
      },
      "homepage": "https://github.com/qodo-ai/qodo-skills.git"
    },
    {
      "name": "railway",
      "description": "Deploy and manage apps, databases, and infrastructure on Railway. Covers project setup, deploys, environment configuration, networking, troubleshooting, and monitoring.",
      "category": "deployment",
      "source": {
        "source": "git-subdir",
        "url": "railwayapp/railway-skills",
        "path": "plugins/railway",
        "ref": "main",
        "sha": "d52f3741a6a33a3191d6138eb3d6c3355cb970d1"
      },
      "homepage": "https://docs.railway.com/ai/claude-code-plugin"
    },
    {
      "name": "ralph-loop",
      "description": "Interactive self-referential AI loops for iterative development, implementing the Ralph Wiggum technique. Claude works on the same task repeatedly, seeing its previous work, until completion.",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/ralph-loop",
      "category": "development",
      "homepage": "https://github.com/anthropics/claude-plugins-public/tree/main/plugins/ralph-loop"
    },
    {
      "name": "rc",
      "description": "Configure RevenueCat projects, apps, products, entitlements, and offerings directly from Claude Code. Manage your in-app purchase backend without leaving your development workflow.",
      "category": "development",
      "source": {
        "source": "url",
        "url": "https://github.com/RevenueCat/rc-claude-code-plugin.git",
        "sha": "af7cb77996aee4e7e3c109c5afec81f716139032"
      },
      "homepage": "https://www.revenuecat.com"
    },
    {
      "name": "remember",
      "description": "Continuous memory for Claude Code. Extracts, summarizes, and compresses conversations into tiered daily logs. Claude remembers what you did yesterday.",
      "source": {
        "source": "url",
        "url": "https://github.com/Digital-Process-Tools/claude-remember.git",
        "sha": "779ab61d8d412230eeec1840b8ca104bebea4358"
      },
      "homepage": "https://github.com/Digital-Process-Tools/claude-remember"
    },
    {
      "name": "revenuecat",
      "description": "Configure RevenueCat projects, apps, products, entitlements, and offerings directly from Claude Code. Manage your in-app purchase backend without leaving your development workflow.",
      "category": "development",
      "source": {
        "source": "url",
        "url": "https://github.com/RevenueCat/rc-claude-code-plugin.git",
        "sha": "af7cb77996aee4e7e3c109c5afec81f716139032"
      },
      "homepage": "https://www.revenuecat.com"
    },
    {
      "name": "ruby-lsp",
      "description": "Ruby language server for code intelligence and analysis",
      "version": "1.0.0",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/ruby-lsp",
      "category": "development",
      "strict": false,
      "lspServers": {
        "ruby-lsp": {
          "command": "ruby-lsp",
          "extensionToLanguage": {
            ".rb": "ruby",
            ".rake": "ruby",
            ".gemspec": "ruby",
            ".ru": "ruby",
            ".erb": "erb"
          }
        }
      }
    },
    {
      "name": "rust-analyzer-lsp",
      "description": "Rust language server for code intelligence and analysis",
      "version": "1.0.0",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/rust-analyzer-lsp",
      "category": "development",
      "strict": false,
      "lspServers": {
        "rust-analyzer": {
          "command": "rust-analyzer",
          "extensionToLanguage": {
            ".rs": "rust"
          }
        }
      }
    },
    {
      "name": "sanity-plugin",
      "description": "Sanity content platform integration with MCP server, agent skills, and slash commands. Query and author content, build and optimize GROQ queries, design schemas, and set up Visual Editing.",
      "category": "development",
      "author": {
        "name": "Sanity"
      },
      "source": {
        "source": "url",
        "url": "https://github.com/sanity-io/agent-toolkit.git",
        "sha": "4b1fb10bd707a22cf0cdfad5374ffc885f2ffa8d"
      },
      "homepage": "https://www.sanity.io"
    },
    {
      "name": "searchfit-seo",
      "description": "Free AI-powered SEO toolkit — audit websites, plan content strategy, optimize pages, generate schema markup, cluster keywords, and track AI visibility. Works with any website or codebase.",
      "source": {
        "source": "url",
        "url": "https://github.com/searchfit/searchfit-seo.git",
        "sha": "ced1a99a9fadfc10aa573a05829fc1bd357d4e4c"
      },
      "homepage": "https://searchfit.ai"
    },
    {
      "name": "security-guidance",
      "description": "Security reminder hook that warns about potential security issues when editing files, including command injection, XSS, and unsafe code patterns",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/security-guidance",
      "category": "security",
      "homepage": "https://github.com/anthropics/claude-plugins-public/tree/main/plugins/security-guidance"
    },
    {
      "name": "semgrep",
      "description": "Semgrep catches security vulnerabilities in real-time and guides Claude to write secure code from the start.",
      "category": "security",
      "source": {
        "source": "git-subdir",
        "url": "https://github.com/semgrep/mcp-marketplace.git",
        "path": "plugin"
      },
      "homepage": "https://github.com/semgrep/mcp-marketplace.git"
    },
    {
      "name": "sentry",
      "description": "Sentry error monitoring integration. Access error reports, analyze stack traces, search issues by fingerprint, and debug production errors directly from your development environment.",
      "category": "monitoring",
      "source": {
        "source": "url",
        "url": "https://github.com/getsentry/sentry-for-claude.git"
      },
      "homepage": "https://github.com/getsentry/sentry-for-claude/tree/main"
    },
    {
      "name": "serena",
      "description": "Semantic code analysis MCP server providing intelligent code understanding, refactoring suggestions, and codebase navigation through language server protocol integration.",
      "category": "development",
      "source": "./external_plugins/serena",
      "homepage": "https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/serena",
      "tags": [
        "community-managed"
      ]
    },
    {
      "name": "skill-creator",
      "description": "Create new skills, improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, update or optimize an existing skill, run evals to test a skill, or benchmark skill performance with variance analysis.",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/skill-creator",
      "category": "development",
      "homepage": "https://github.com/anthropics/claude-plugins-official/tree/main/plugins/skill-creator"
    },
    {
      "name": "slack",
      "description": "Slack workspace integration. Search messages, access channels, read threads, and stay connected with your team's communications while coding. Find relevant discussions and context quickly.",
      "category": "productivity",
      "source": {
        "source": "url",
        "url": "https://github.com/slackapi/slack-mcp-plugin.git"
      },
      "homepage": "https://github.com/slackapi/slack-mcp-plugin/tree/main"
    },
    {
      "name": "sonarqube-agent-plugins",
      "description": "Integrate SonarQube code quality and security analysis into Claude Code: namespaced slash commands, a guided skill to setup the SonarQube CLI, and a startup check for CLI wiring. MCP server registration and secrets-scanning hooks are installed by the SonarQube CLI as part of setup.",
      "category": "security",
      "source": {
        "source": "url",
        "url": "https://github.com/SonarSource/sonarqube-agent-plugins.git",
        "sha": "0cae644cee9318e6245b62ca779abdc60e6daa49"
      },
      "homepage": "https://github.com/SonarSource/sonarqube-agent-plugins"
    },
    {
      "name": "sonatype-guide",
      "description": "Sonatype Guide MCP server for software supply chain intelligence and dependency security. Analyze dependencies for vulnerabilities, get secure version recommendations, and check component quality metrics.",
      "category": "security",
      "source": {
        "source": "url",
        "url": "https://github.com/sonatype/sonatype-guide-claude-plugin.git"
      },
      "homepage": "https://github.com/sonatype/sonatype-guide-claude-plugin.git"
    },
    {
      "name": "sourcegraph",
      "description": "Code search and understanding across codebases. Search, read, and trace references across repositories; analyze refactor impact; investigate incidents via commit and diff search; run targeted security sweeps.",
      "category": "development",
      "source": {
        "source": "url",
        "url": "https://github.com/sourcegraph-community/sourcegraph-claudecode-plugin.git",
        "sha": "cfe3d44476957b16d1575261bef6b2dc7cb1e0b7"
      },
      "homepage": "https://sourcegraph.com"
    },
    {
      "name": "stagehand",
      "description": "Browser automation skill for Claude Code using Stagehand. Automate web interactions, extract data, and navigate websites using natural language.",
      "version": "0.1.0",
      "author": {
        "name": "Browserbase"
      },
      "source": {
        "source": "github",
        "repo": "browserbase/agent-browse"
      },
      "category": "automation",
      "keywords": [
        "browser",
        "automation",
        "stagehand",
        "web-scraping"
      ],
      "homepage": "https://github.com/browserbase/agent-browse",
      "strict": false,
      "skills": [
        "./.claude/skills/browser-automation"
      ]
    },
    {
      "name": "stripe",
      "description": "Stripe development plugin for Claude",
      "category": "development",
      "source": {
        "source": "git-subdir",
        "url": "stripe/ai",
        "path": "providers/claude/plugin",
        "ref": "main"
      },
      "homepage": "https://github.com/stripe/ai/tree/main/providers/claude/plugin"
    },
    {
      "name": "sumup",
      "description": "SumUp payment integrations across terminal and online checkout flows. Build Android and iOS POS apps with SumUp card readers, online checkout with server SDKs and the checkout widget, and control card readers remotely via Cloud API.",
      "category": "development",
      "source": {
        "source": "url",
        "url": "https://github.com/sumup/sumup-skills.git",
        "sha": "802476c39a0422d3277e37288b03968ad731bc30"
      },
      "homepage": "https://www.sumup.com/"
    },
    {
      "name": "supabase",
      "description": "Supabase MCP integration for database operations, authentication, storage, and real-time subscriptions. Manage your Supabase projects, run SQL queries, and interact with your backend directly.",
      "category": "database",
      "source": "./external_plugins/supabase",
      "homepage": "https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/supabase"
    },
    {
      "name": "superpowers",
      "description": "Superpowers teaches Claude brainstorming, subagent driven development with built in code review, systematic debugging, and red/green TDD. Additionally, it teaches Claude how to author and test new skills.",
      "category": "development",
      "source": {
        "source": "url",
        "url": "https://github.com/obra/superpowers.git"
      },
      "homepage": "https://github.com/obra/superpowers.git"
    },
    {
      "name": "swift-lsp",
      "description": "Swift language server (SourceKit-LSP) for code intelligence",
      "version": "1.0.0",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/swift-lsp",
      "category": "development",
      "strict": false,
      "lspServers": {
        "sourcekit-lsp": {
          "command": "sourcekit-lsp",
          "extensionToLanguage": {
            ".swift": "swift"
          }
        }
      }
    },
    {
      "name": "telegram",
      "description": "Telegram messaging bridge with built-in access control. Manage pairing, allowlists, and policy via /telegram:access.",
      "category": "productivity",
      "source": "./external_plugins/telegram"
    },
    {
      "name": "terraform",
      "description": "The Terraform MCP Server provides seamless integration with Terraform ecosystem, enabling advanced automation and interaction capabilities for Infrastructure as Code (IaC) development.",
      "author": {
        "name": "HashiCorp",
        "email": "support@hashicorp.com"
      },
      "category": "development",
      "source": "./external_plugins/terraform",
      "homepage": "https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/terraform"
    },
    {
      "name": "typescript-lsp",
      "description": "TypeScript/JavaScript language server for enhanced code intelligence",
      "version": "1.0.0",
      "author": {
        "name": "Anthropic",
        "email": "support@anthropic.com"
      },
      "source": "./plugins/typescript-lsp",
      "category": "development",
      "strict": false,
      "lspServers": {
        "typescript": {
          "command": "typescript-language-server",
          "args": [
            "--stdio"
          ],
          "extensionToLanguage": {
            ".ts": "typescript",
            ".tsx": "typescriptreact",
            ".js": "javascript",
            ".jsx": "javascriptreact",
            ".mts": "typescript",
            ".cts": "typescript",
            ".mjs": "javascript",
            ".cjs": "javascript"
          }
        }
      }
    },
    {
      "name": "ui5",
      "description": "SAPUI5 / OpenUI5 plugin for Claude. Create and validate UI5 projects, access API documentation, run UI5 linter, get development guidelines and best practices for UI5 development.",
      "category": "development",
      "source": {
        "source": "git-subdir",
        "url": "UI5/plugins-claude",
        "path": "plugins/ui5",
        "ref": "main",
        "sha": "5070dfc1cef711d6efad40beb43750027039d71f"
      },
      "homepage": "https://github.com/UI5/plugins-claude"
    },
    {
      "name": "ui5-typescript-conversion",
      "description": "SAPUI5 / OpenUI5 plugin for Claude. Convert JavaScript based UI5 projects to TypeScript.",
      "category": "development",
      "source": {
        "source": "git-subdir",
        "url": "UI5/plugins-claude",
        "path": "plugins/ui5-typescript-conversion",
        "ref": "main",
        "sha": "5070dfc1cef711d6efad40beb43750027039d71f"
      },
      "homepage": "https://github.com/UI5/plugins-claude"
    },
    {
      "name": "vercel",
      "description": "Vercel deployment platform integration. Manage deployments, check build status, access logs, configure domains, and control your frontend infrastructure directly from Claude Code.",
      "category": "deployment",
      "source": {
        "source": "url",
        "url": "https://github.com/vercel/vercel-plugin.git"
      },
      "homepage": "https://github.com/vercel/vercel-plugin"
    },
    {
      "name": "voila-api",
      "description": "Definitive guide for the Voila API. Covers shipment creation (Manual/Smart Shipping), real-time tracking, detailed history, manifesting, collections, webhooks, and third-party integrations (Sorted, Peoplevox, Mintsoft, Veeqo, JD).",
      "source": {
        "source": "url",
        "url": "https://github.com/TSedmanDC/Voila-API-Skill.git",
        "sha": "b9cfcb860cb5ae4ece57d67422a6cdd92ef96739"
      },
      "homepage": "https://github.com/TSedmanDC/Voila-API-Skill"
    },
    {
      "name": "wix",
      "description": "Build, manage, and deploy Wix sites and apps. CLI development skills for dashboard extensions, backend APIs, site widgets, and service plugins with the Wix Design System, plus MCP server for site management.",
      "category": "development",
      "source": {
        "source": "url",
        "url": "https://github.com/wix/skills.git",
        "sha": "15dda227e34959b1340e33bb9aede7e23a273f42"
      },
      "homepage": "https://dev.wix.com/docs/wix-cli/guides/development/about-wix-skills"
    },
    {
      "name": "wordpress.com",
      "description": "Uses Claude Code to create and edit WordPress sites with WordPress Studio before deploying changes to your WordPress.com site.",
      "source": {
        "source": "url",
        "url": "https://github.com/Automattic/claude-code-wordpress.com.git",
        "sha": "e4d23c3bffdcdb7f70134ab6a1a110258ff75cfd"
      },
      "homepage": "https://developer.wordpress.com/wordpress-com-claude-code-plugin/"
    },
    {
      "name": "zapier",
      "description": "Connect 8,000+ apps to your AI workflow. Discover, enable, and execute Zapier actions directly from your client.",
      "category": "productivity",
      "source": {
        "source": "git-subdir",
        "url": "zapier/zapier-mcp",
        "path": "plugins/zapier",
        "ref": "main",
        "sha": "b93007e9a726c6ee93c57a949e732744ef5acbfd"
      },
      "homepage": "https://github.com/zapier/zapier-mcp/tree/main/plugins/zapier"
    }
  ]
}

```

## File: payload\.github\scripts\check-marketplace-sorted.ts
```
#!/usr/bin/env bun
/**
 * Checks that marketplace.json plugins are alphabetically sorted by name.
 *
 * Usage:
 *   bun check-marketplace-sorted.ts           # check, exit 1 if unsorted
 *   bun check-marketplace-sorted.ts --fix     # sort in place
 */

import { readFileSync, writeFileSync } from "fs";
import { join } from "path";

const MARKETPLACE = join(import.meta.dir, "../../.claude-plugin/marketplace.json");

type Plugin = { name: string; [k: string]: unknown };
type Marketplace = { plugins: Plugin[]; [k: string]: unknown };

const raw = readFileSync(MARKETPLACE, "utf8");
const mp: Marketplace = JSON.parse(raw);

const cmp = (a: Plugin, b: Plugin) =>
  a.name.toLowerCase().localeCompare(b.name.toLowerCase());

if (process.argv.includes("--fix")) {
  mp.plugins.sort(cmp);
  writeFileSync(MARKETPLACE, JSON.stringify(mp, null, 2) + "\n");
  console.log(`sorted ${mp.plugins.length} plugins`);
  process.exit(0);
}

for (let i = 1; i < mp.plugins.length; i++) {
  if (cmp(mp.plugins[i - 1], mp.plugins[i]) > 0) {
    console.error(
      `marketplace.json plugins are not sorted: ` +
        `'${mp.plugins[i - 1].name}' should come after '${mp.plugins[i].name}' (index ${i})`,
    );
    console.error(`  run: bun .github/scripts/check-marketplace-sorted.ts --fix`);
    process.exit(1);
  }
}

console.log(`ok: ${mp.plugins.length} plugins sorted`);

```

## File: payload\.github\scripts\validate-frontmatter.ts
```
#!/usr/bin/env bun
/**
 * Validates YAML frontmatter in agent, skill, and command .md files.
 *
 * Usage:
 *   bun validate-frontmatter.ts                    # scan current directory
 *   bun validate-frontmatter.ts /path/to/dir       # scan specific directory
 *   bun validate-frontmatter.ts file1.md file2.md  # validate specific files
 */

import { parse as parseYaml } from "yaml";
import { readdir, readFile } from "fs/promises";
import { basename, join, relative, resolve } from "path";

// Characters that require quoting in YAML values when unquoted:
// {} [] flow indicators, * anchor/alias, & anchor, # comment,
// ! tag, | > block scalars, % directive, @ ` reserved
const YAML_SPECIAL_CHARS = /[{}[\]*&#!|>%@`]/;
const FRONTMATTER_REGEX = /^---\s*\n([\s\S]*?)---\s*\n?/;

/**
 * Pre-process frontmatter text to quote values containing special YAML
 * characters. This allows glob patterns like **\/*.{ts,tsx} to parse.
 */
function quoteSpecialValues(text: string): string {
  const lines = text.split("\n");
  const result: string[] = [];

  for (const line of lines) {
    const match = line.match(/^([a-zA-Z_-]+):\s+(.+)$/);
    if (match) {
      const [, key, value] = match;
      if (!key || !value) {
        result.push(line);
        continue;
      }
      // Skip already-quoted values
      if (
        (value.startsWith('"') && value.endsWith('"')) ||
        (value.startsWith("'") && value.endsWith("'"))
      ) {
        result.push(line);
        continue;
      }
      if (YAML_SPECIAL_CHARS.test(value)) {
        const escaped = value.replace(/\\/g, "\\\\").replace(/"/g, '\\"');
        result.push(`${key}: "${escaped}"`);
        continue;
      }
    }
    result.push(line);
  }

  return result.join("\n");
}

interface ParseResult {
  frontmatter: Record<string, unknown>;
  content: string;
  error?: string;
}

function parseFrontmatter(markdown: string): ParseResult {
  const match = markdown.match(FRONTMATTER_REGEX);

  if (!match) {
    return {
      frontmatter: {},
      content: markdown,
      error: "No frontmatter found",
    };
  }

  const frontmatterText = quoteSpecialValues(match[1] || "");
  const content = markdown.slice(match[0].length);

  try {
    const parsed = parseYaml(frontmatterText);
    if (parsed && typeof parsed === "object" && !Array.isArray(parsed)) {
      return { frontmatter: parsed as Record<string, unknown>, content };
    }
    return {
      frontmatter: {},
      content,
      error: `YAML parsed but result is not an object (got ${typeof parsed}${Array.isArray(parsed) ? " array" : ""})`,
    };
  } catch (err) {
    return {
      frontmatter: {},
      content,
      error: `YAML parse failed: ${err instanceof Error ? err.message : err}`,
    };
  }
}

// --- Validation ---

type FileType = "agent" | "skill" | "command";

interface ValidationIssue {
  level: "error" | "warning";
  message: string;
}

function validateAgent(
  frontmatter: Record<string, unknown>
): ValidationIssue[] {
  const issues: ValidationIssue[] = [];

  if (!frontmatter["name"] || typeof frontmatter["name"] !== "string") {
    issues.push({ level: "error", message: 'Missing required "name" field' });
  }
  if (
    !frontmatter["description"] ||
    typeof frontmatter["description"] !== "string"
  ) {
    issues.push({
      level: "error",
      message: 'Missing required "description" field',
    });
  }

  return issues;
}

function validateSkill(
  frontmatter: Record<string, unknown>
): ValidationIssue[] {
  const issues: ValidationIssue[] = [];

  if (!frontmatter["description"] && !frontmatter["when_to_use"]) {
    issues.push({
      level: "error",
      message: 'Missing required "description" field',
    });
  }

  return issues;
}

function validateCommand(
  frontmatter: Record<string, unknown>
): ValidationIssue[] {
  const issues: ValidationIssue[] = [];

  if (
    !frontmatter["description"] ||
    typeof frontmatter["description"] !== "string"
  ) {
    issues.push({
      level: "error",
      message: 'Missing required "description" field',
    });
  }

  return issues;
}

// --- File type detection ---

function detectFileType(filePath: string): FileType | null {
  // Only match agents/ and commands/ at the plugin root level, not nested
  // inside skill content (e.g. plugins/foo/skills/bar/agents/ is skill content,
  // not an agent definition).
  const inSkillContent = /\/skills\/[^/]+\//.test(filePath);
  if (filePath.includes("/agents/") && !inSkillContent) return "agent";
  if (filePath.includes("/skills/") && basename(filePath) === "SKILL.md")
    return "skill";
  if (filePath.includes("/commands/") && !inSkillContent) return "command";
  return null;
}

// --- File discovery ---

async function findMdFiles(
  baseDir: string
): Promise<{ path: string; type: FileType }[]> {
  const results: { path: string; type: FileType }[] = [];

  async function walk(dir: string) {
    const entries = await readdir(dir, { withFileTypes: true });
    for (const entry of entries) {
      const fullPath = join(dir, entry.name);
      if (entry.isDirectory()) {
        await walk(fullPath);
      } else if (entry.name.endsWith(".md")) {
        const type = detectFileType(fullPath);
        if (type) {
          results.push({ path: fullPath, type });
        }
      }
    }
  }

  await walk(baseDir);
  return results;
}

// --- Main ---

async function main() {
  const args = process.argv.slice(2);

  let files: { path: string; type: FileType }[];
  let baseDir: string;

  if (args.length > 0 && args.every((a) => a.endsWith(".md"))) {
    baseDir = process.cwd();
    files = [];
    for (const arg of args) {
      const fullPath = resolve(arg);
      const type = detectFileType(fullPath);
      if (type) {
        files.push({ path: fullPath, type });
      }
    }
  } else {
    baseDir = args[0] || process.cwd();
    files = await findMdFiles(baseDir);
  }

  let totalErrors = 0;
  let totalWarnings = 0;

  console.log(`Validating ${files.length} frontmatter files...\n`);

  for (const { path: filePath, type } of files) {
    const rel = relative(baseDir, filePath);
    const content = await readFile(filePath, "utf-8");
    const result = parseFrontmatter(content);

    const issues: ValidationIssue[] = [];

    if (result.error) {
      issues.push({ level: "error", message: result.error });
    }

    if (!result.error) {
      switch (type) {
        case "agent":
          issues.push(...validateAgent(result.frontmatter));
          break;
        case "skill":
          issues.push(...validateSkill(result.frontmatter));
          break;
        case "command":
          issues.push(...validateCommand(result.frontmatter));
          break;
      }
    }

    if (issues.length > 0) {
      console.log(`${rel} (${type})`);
      for (const issue of issues) {
        const prefix = issue.level === "error" ? "  ERROR" : "  WARN ";
        console.log(`${prefix}: ${issue.message}`);
        if (issue.level === "error") totalErrors++;
        else totalWarnings++;
      }
      console.log();
    }
  }

  console.log("---");
  console.log(
    `Validated ${files.length} files: ${totalErrors} errors, ${totalWarnings} warnings`
  );

  if (totalErrors > 0) {
    process.exit(1);
  }
}

main().catch((err) => {
  console.error("Fatal error:", err);
  process.exit(2);
});

```

## File: payload\.github\scripts\validate-marketplace.ts
```
#!/usr/bin/env bun
/**
 * Validates marketplace.json: well-formed JSON, plugins array present,
 * each entry has required fields, and no duplicate plugin names.
 *
 * Usage:
 *   bun validate-marketplace.ts <path-to-marketplace.json>
 */

import { readFile } from "fs/promises";

async function main() {
  const filePath = process.argv[2];
  if (!filePath) {
    console.error("Usage: validate-marketplace.ts <path-to-marketplace.json>");
    process.exit(2);
  }

  const content = await readFile(filePath, "utf-8");

  let parsed: unknown;
  try {
    parsed = JSON.parse(content);
  } catch (err) {
    console.error(
      `ERROR: ${filePath} is not valid JSON: ${err instanceof Error ? err.message : err}`
    );
    process.exit(1);
  }

  if (!parsed || typeof parsed !== "object" || Array.isArray(parsed)) {
    console.error(`ERROR: ${filePath} must be a JSON object`);
    process.exit(1);
  }

  const marketplace = parsed as Record<string, unknown>;
  if (!Array.isArray(marketplace.plugins)) {
    console.error(`ERROR: ${filePath} missing "plugins" array`);
    process.exit(1);
  }

  const errors: string[] = [];
  const seen = new Set<string>();
  const required = ["name", "description", "source"] as const;

  marketplace.plugins.forEach((p, i) => {
    if (!p || typeof p !== "object") {
      errors.push(`plugins[${i}]: must be an object`);
      return;
    }
    const entry = p as Record<string, unknown>;
    for (const field of required) {
      if (!entry[field]) {
        errors.push(`plugins[${i}] (${entry.name ?? "?"}): missing required field "${field}"`);
      }
    }
    if (typeof entry.name === "string") {
      if (seen.has(entry.name)) {
        errors.push(`plugins[${i}]: duplicate plugin name "${entry.name}"`);
      }
      seen.add(entry.name);
    }
  });

  if (errors.length) {
    console.error(`ERROR: ${filePath} has ${errors.length} validation error(s):`);
    for (const e of errors) console.error(`  - ${e}`);
    process.exit(1);
  }

  console.log(`OK: ${marketplace.plugins.length} plugins, no duplicates, all required fields present`);
}

main().catch((err) => {
  console.error("Fatal error:", err);
  process.exit(2);
});

```

## File: payload\.github\workflows\close-external-prs.yml
```
name: Close External PRs

on:
  pull_request_target:
    types: [opened]

permissions:
  pull-requests: write
  issues: write

jobs:
  check-membership:
    if: vars.DISABLE_EXTERNAL_PR_CHECK != 'true'
    runs-on: ubuntu-latest
    steps:
      - name: Check if author has write access
        uses: actions/github-script@v7
        with:
          script: |
            const author = context.payload.pull_request.user.login;

            const { data } = await github.rest.repos.getCollaboratorPermissionLevel({
              owner: context.repo.owner,
              repo: context.repo.repo,
              username: author
            });

            if (['admin', 'write'].includes(data.permission)) {
              console.log(`${author} has ${data.permission} access, allowing PR`);
              return;
            }

            console.log(`${author} has ${data.permission} access, closing PR`);

            await github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.payload.pull_request.number,
              body: `Thanks for your interest! This repo only accepts contributions from Anthropic team members. If you'd like to submit a plugin to the marketplace, please submit your plugin [here](https://clau.de/plugin-directory-submission).`
            });

            await github.rest.pulls.update({
              owner: context.repo.owner,
              repo: context.repo.repo,
              pull_number: context.payload.pull_request.number,
              state: 'closed'
            });

```

## File: payload\.github\workflows\validate-frontmatter.yml
```
name: Validate Frontmatter

on:
  pull_request:
    paths:
      - '**/agents/*.md'
      - '**/skills/*/SKILL.md'
      - '**/commands/*.md'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: oven-sh/setup-bun@v2

      - name: Install dependencies
        run: cd .github/scripts && bun install yaml

      - name: Get changed frontmatter files
        id: changed
        run: |
          # Use diff-filter=AMRC to exclude deleted files (D) - only Added, Modified, Renamed, Copied
          FILES=$(gh pr diff ${{ github.event.pull_request.number }} --name-only --diff-filter=AMRC | grep -E '(agents/.*\.md|skills/.*/SKILL\.md|commands/.*\.md)$' || true)
          echo "files<<EOF" >> "$GITHUB_OUTPUT"
          echo "$FILES" >> "$GITHUB_OUTPUT"
          echo "EOF" >> "$GITHUB_OUTPUT"
        env:
          GH_TOKEN: ${{ github.token }}

      - name: Validate frontmatter
        if: steps.changed.outputs.files != ''
        run: |
          echo "${{ steps.changed.outputs.files }}" | xargs bun .github/scripts/validate-frontmatter.ts

```

## File: payload\.github\workflows\validate-marketplace.yml
```
name: Validate Marketplace JSON

on:
  pull_request:
    paths:
      - '.claude-plugin/marketplace.json'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: oven-sh/setup-bun@v2

      - name: Validate marketplace.json
        run: bun .github/scripts/validate-marketplace.ts .claude-plugin/marketplace.json

      - name: Check plugins sorted
        run: bun .github/scripts/check-marketplace-sorted.ts

```

