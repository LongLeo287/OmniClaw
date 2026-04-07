---
id: claudekit
type: knowledge
owner: OA_Triage
---
# claudekit
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Claude Kit

A comprehensive toolkit for Claude Code to accelerate development workflows for teams working with Python and JavaScript/TypeScript.

## Features

- **20 Specialized Agents** - From planning to deployment
- **27+ Slash Commands** - Workflow automation with flag support
- **38 Skills** - Framework, language, methodology, patterns, and optimization expertise (all with YAML frontmatter and bundled resources)
- **7 Behavioral Modes** - Task-specific response optimization
- **Command Flag System** - Combinable `--flag` syntax for customization
- **Token Optimization** - 30-70% cost savings with compressed output modes
- **MCP Integrations** - Context7, Sequential Thinking, Playwright, Memory, Filesystem
- **Context Management** - Project indexing, checkpoints, parallel tasks

## Quick Start

1. Copy the `.claude` folder to your project root
2. Customize `.claude/CLAUDE.md` for your project
3. Start using commands like `/feature`, `/review`, `/test`

## Directory Structure

```
.claude/
├── CLAUDE.md              # Project context (customize this!)
├── settings.json          # Hooks, permissions, and MCP config
├── agents/                # 20 specialized agents
├── commands/              # 27+ workflow commands
├── modes/                 # 7 behavioral mode definitions
├── mcp/                   # MCP server configurations
└── skills/                # 38 skills with YAML frontmatter & bundled resources
    ├── api/               # OpenAPI specification patterns
    ├── databases/         # PostgreSQL, MongoDB
    ├── devops/            # Docker, GitHub Actions
    ├── frameworks/        # FastAPI, Django, Next.js, React
    ├── frontend/          # Tailwind CSS, shadcn/ui
    ├── languages/         # Python, TypeScript, JavaScript
    ├── methodology/       # TDD, debugging, planning, review (14 skills)
    ├── optimization/      # Token efficiency patterns
    ├── patterns/          # Error handling, state, logging, caching, auth, API client
    ├── security/          # OWASP security patterns
    └── testing/           # pytest, vitest
```

## Agents

### Core Development
| Agent | Description |
|-------|-------------|
| `planner` | Task decomposition and planning |
| `researcher` | Technology research |
| `debugger` | Error analysis and fixing |
| `tester` | Test generation |
| `code-reviewer` | Code review with security focus |
| `scout` | Codebase exploration |

### Operations
| Agent | Description |
|-------|-------------|
| `git-manager` | Git operations and PRs |
| `docs-manager` | Documentation generation |
| `project-manager` | Progress tracking |
| `database-admin` | Schema and migrations |
| `ui-ux-designer` | UI component creation |

### Extended
| Agent | Description |
|-------|-------------|
| `cicd-manager` | CI/CD pipeline management |
| `security-auditor` | Security reviews |
| `api-designer` | API design and OpenAPI |
| `vulnerability-scanner` | Security scanning |
| `pipeline-architect` | Pipeline optimization |

## Commands

### Development Workflow
```bash
/feature [description]   # Full feature development
/fix [error]            # Debug and fix bugs
/review [file]          # Code review
/test [scope]           # Generate tests
/tdd [feature]          # Test-driven development
```

### Git & Deployment
```bash
/commit [message]       # Smart commit
/ship [message]         # Commit + PR
/pr [title]             # Create pull request
/deploy [env]           # Deploy to environment
```

### Documentation & Planning
```bash
/plan [task]            # Create implementation plan
/plan --detailed [task] # Detailed plan (2-5 min tasks)
/brainstorm [topic]     # Interactive design session
/execute-plan [file]    # Subagent-driven execution
/doc [target]           # Generate documentation
/research [topic]       # Research technology
```

### Security & Quality
```bash
/security-scan          # Scan for vulnerabilities
/api-gen [resource]     # Generate API code
/refactor [file]        # Improve code structure
/optimize [file]        # Performance optimization
```

### Context & Modes (New)
```bash
/mode [name]            # Switch behavioral mode
/index                  # Generate project index
/load [component]       # Load project context
/checkpoint [action]    # Save/restore session state
/spawn [task]           # Launch parallel background task
```

## Skills (38 Total)

Every skill includes YAML frontmatter for reliable triggering, "When to Use" / "When NOT to Use" sections, core patterns with code examples, best practices, common pitfalls, cross-references, and bundled resources (reference docs, templates, scripts).

### Languages
- **Python** — Type hints, async, dataclasses, Pydantic, decorators, pattern matching
- **TypeScript** — Advanced types, generics, Zod, discriminated unions, branded types
- **JavaScript** — ES6+, async patterns, Proxy/Reflect, generators, modules

### Frameworks
- **FastAPI** — Routes, dependency injection, middleware, WebSocket, testing
- **Django** — ORM, views, migrations, DRF, signals, admin
- **Next.js** — App Router, server/client components, caching, middleware
- **React** — Hooks, custom hooks, context, Suspense, error boundaries, performance

### Databases
- **PostgreSQL** — Schema, indexing (B-tree/GIN/GiST), migrations, CTEs, JSONB
- **MongoDB** — Schema design, aggregation pipelines, indexing, transactions

### DevOps
- **Docker** — Multi-stage builds, Compose, security hardening, layer caching
- **GitHub Actions** — CI/CD, matrix strategy, reusable workflows, deployment

### Frontend
- **Tailwind CSS** — Responsive, dark mode, animations, theme customization
- **shadcn/ui** — Components, forms, data tables, theming, toast

### API
- **OpenAPI** — 3.1 spec, pagination, versioning, error schemas, webhooks

### Security
- **OWASP** — Top 10, auth, CORS, CSP, secret management, rate limiting

### Testing
- **pytest** — Fixtures, parametrize, mocking, async, coverage
- **vitest** — React Testing Library, mocking, MSW, snapshots, configuration

### Optimization
- **Token-efficient** — Compressed output modes (30-70% cost savings)

### Developer Patterns (New)
- **error-handling** — Custom errors, retry patterns, Result type, error boundaries
- **state-management** — React state, Zustand, TanStack Query, form state, URL state
- **logging** — Structured logging, log levels, correlation IDs, redaction
- **caching** — Memoization, HTTP cache, Redis, CDN, cache invalidation
- **api-client** — HTTP clients, interceptors, retry, type-safe clients
- **authentication** — JWT, OAuth2, sessions, RBAC, MFA, password hashing

### Methodology (14 Skills)

| Category | Skills |
|----------|--------|
| **Planning** | brainstorming, writing-plans, executing-plans |
| **Testing** | test-driven-development, verification-before-completion, testing-anti-patterns |
| **Debugging** | systematic-debugging, root-cause-tracing, defense-in-depth |
| **Collaboration** | dispatching-parallel-agents, requesting-code-review, receiving-code-review, finishing-development-branch |
| **Reasoning** | sequential-thinking |

Key methodology principles:
- **TDD Strict**: No production code without failing test first
- **Verification**: Evidence-based completion claims
- **Quality Gates**: Code review between every task
- **Bite-sized Tasks**: 2-5 minute increments with exact code
- **Sequential Thinking**: Step-by-step reasoning with confidence scores

### Bundled Resources

Skills include progressive-disclosure resources loaded on demand:

| Resource Type | Purpose | Examples |
|---------------|---------|----------|
| **references/** | Cheat sheets, decision trees, pattern catalogs | OWASP Top 10, index decision tree, auth flows |
| **templates/** | Starter files, boilerplate, configs | OpenAPI spec, Dockerfile, CI workflows, conftest.py |
| **scripts/** | Executable helpers for deterministic tasks | Security audit scanner, OpenAPI validator |

## Behavioral Modes

Switch modes to optimize responses for different task types:

| Mode | Description | Best For |
|------|-------------|----------|
| `default` | Balanced standard behavior | General tasks |
| `brainstorm` | Creative exploration, questions | Design, ideation |
| `token-efficient` | Compressed, concise output | Cost savings |
| `deep-research` | Thorough analysis, citations | Investigation |
| `implementation` | Code-focused, minimal prose | Executing plans |
| `review` | Critical analysis, finding issues | Code review |
| `orchestration` | Multi-task coordination | Parallel work |

```bash
/mode brainstorm              # Switch for session
/feature --mode=implementation # Override per command
```

## Command Flags

All commands support combinable flags:

```bash
# Mode and depth
/plan --mode=brainstorm --depth=5 "feature design"

# Persona-based review
/review --persona=security --format=detailed src/auth/

# Token optimization
/fix --format=concise "error message"

# Save output
/research --save=docs/research.md "auth libraries"
```

### Available Flags

| Flag | Description |
|------|-------------|
| `--mode=[mode]` | Behavioral mode |
| `--depth=[1-5]` | Thoroughness (1=quick, 5=exhaustive) |
| `--format=[fmt]` | Output format (concise/detailed/json) |
| `--persona=[type]` | Expertise focus (security/performance/architecture) |
| `--save=[path]` | Save output to file |
| `--checkpoint` | Create state checkpoint |

## Token Optimization

Reduce costs by 30-70% with compressed output modes:

| Level | Activation | Savings |
|-------|------------|---------|
| Concise | `--format=concise` | 30-40% |
| Ultra | `--format=ultra` | 60-70% |
| Session | `/mode token-efficient` | 30-70% |

## MCP Integrations

MCP servers extend Claude Kit with powerful capabilities. They are **automatically used** when configured.

| Server | Package | Purpose |
|--------|---------|---------|
| Context7 | `@upstash/context7-mcp` | Up-to-date library documentation |
| Sequential | `@modelcontextprotocol/server-sequential-thinking` | Multi-step reasoning |
| Playwright | `@playwright/mcp` | Browser automation (Microsoft) |
| Memory | `@modelcontextprotocol/server-memory` | Persistent knowledge graph |
| Filesystem | `@modelcontextprotocol/server-filesystem` | Secure file operations |

### How MCP Servers Enhance Commands

| Command | MCP Servers Used | Enhancement |
|---------|------------------|-------------|
| `/feature` | Context7, Sequential, Filesystem | Accurate docs, structured planning, safe file ops |
| `/fix` | Sequential, Memory, Playwright | Step-by-step debugging, context recall, browser testing |
| `/test` | Playwright, Filesystem | E2E browser tests, test file management |
| `/plan` | Sequential, Memory | Structured breakdown, remembers decisions |
| `/research` | Context7, Sequential | Real-time docs, thorough analysis |
| `/brainstorm` | Sequential, Memory | Creative exploration, persistent ideas |
| `/index` | Filesystem | Project structure scanning |

### MCP + Mode Combinations

| Mode | Primary MCP | Best For |
|------|-------------|----------|
| `brainstorm` | Sequential + Memory | Design sessions with persistent ideas |
| `deep-research` | Sequential + Context7 | Thorough technical investigation |
| `implementation` | Filesystem + Context7 | Focused coding with accurate docs |
| `review` | Playwright + Memory | UI review with context |
| `orchestration` | All 5 | Complex multi-step parallel work |

### Example: Full Feature Development

```bash
/feature Add user profile with avatar upload
```

1. **Context7** → Fetches latest React/Next.js file upload docs
2. **Sequential** → Plans component structure step-by-step
3. **Memory** → Recalls your UI patterns from previous sessions
4. **Filesystem** → Creates files in correct locations
5. **Playwright** → Tests the upload flow in browser

Setup: See `.claude/mcp/README.md`

## Customization

### CLAUDE.md

The `.claude/CLAUDE.md` file is your project context. Customize it with:

```markdown
# Project: Your Project Name

## Tech Stack
- **Backend**: FastAPI
- **Frontend**: Next.js
- **Database**: PostgreSQL

## Conventions
- Use type hints
- 80% test coverage
- Conventional commits

## Agent Overrides
### Tester
- Framework: pytest
- Coverage: 90%
```

### Adding Custom Commands

Create a new file in `.claude/commands/`:

```markdown
# /my-command

## Purpose
Description of your command.

---

Your prompt content here.

Use $ARGUMENTS for command arguments.
```

### Adding Custom Skills

Create a new skill in `.claude/skills/category/skillname/SKILL.md`:

```yaml
---
name: my-skill
description: >
  What this skill does and when to trigger it. Be specific — list
  contexts, keywords, and scenarios. 2-4 pushy sentences.
---
```

```markdown
# My Skill

Brief overview.

## When to Use
- Scenario 1
- Scenario 2

## When NOT to Use
- Anti-trigger scenario

---

## Core Patterns
### Pattern Name
Code examples with good/bad comparisons.

## Best Practices
## Common Pitfalls
## Related Skills
```

Optionally add bundled resources:
```
my-skill/
├── SKILL.md
├── references/    # Loaded into context on demand
├── scripts/       # Executed without loading into context
└── templates/     # Scaffolded into user's project
```

## Workflow Chains

### Feature Development
```
/feature → planner → implement → code-reviewer → tester → git-manager
```

### Bug Fix
```
/fix → debugger → scout → implement → tester → code-reviewer
```

### Ship Code
```
/ship → code-reviewer → tester → security-scan → git-manager
```

### Superpowers Workflow (Detailed)
```
/brainstorm → /plan --detailed → /execute-plan → /ship
```
Uses one-question-at-a-time design, 2-5 min tasks with exact code, subagent execution with code review gates.

### Parallel Research
```
/spawn "research auth" → /spawn "analyze security" → /spawn --collect
```
Launch multiple background tasks, then aggregate results.

### Cost-Optimized Session
```
/mode token-efficient → [work on tasks] → /mode default
```
Enable compressed outputs for high-volume sessions.

## Requirements

- Claude Code 1.0+
- Git
- Node.js or Python (depending on your stack)

## License

MIT

---

Built with duthaho

```

### File: .claude\mcp\README.md
```md
# MCP Server Integrations

Model Context Protocol (MCP) servers extend Claude Code capabilities with specialized tools and integrations.

## Available MCP Servers

| Server | Purpose | Status |
|--------|---------|--------|
| Context7 | Up-to-date library documentation | Optional |
| Sequential | Multi-step reasoning tools | Optional |
| Playwright | Browser automation (Microsoft) | Optional |
| Memory | Persistent knowledge graph | Optional |
| Filesystem | Secure file operations | Optional |

## Installation

### Prerequisites
- Node.js 18+
- npx available in PATH

### Global Configuration

MCP servers are configured in your Claude Code settings:

**Location**: `~/.claude/settings.json` (user) or `.mcp.json` (project)

### Quick Setup

1. Copy the configuration for your platform (see below)
2. Add to your `.mcp.json` or `settings.json` under `mcpServers`
3. Restart Claude Code

## Platform-Specific Configuration

MCP server configuration differs between platforms:

### Linux / macOS

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"]
    }
  }
}
```

### Windows

Windows requires the `cmd /c` wrapper to execute npx:

```json
{
  "mcpServers": {
    "context7": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@upstash/context7-mcp"]
    }
  }
}
```

> **Note**: The `.mcp.json` included in this repository uses Windows syntax. Linux/macOS users should use the configurations in this README.

## Server Configurations

### Context7 (Documentation Lookup)

Provides up-to-date documentation for libraries and frameworks.

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"]
    }
  }
}
```

**Usage**: Ask about any library and get current documentation.

**Tools**:
- `resolve-library-id` - Find library IDs for documentation lookup
- `get-library-docs` - Fetch documentation for a specific library

### Sequential Thinking

Provides structured reasoning tools for complex problem-solving.

```json
{
  "mcpServers": {
    "sequential": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

**Usage**: Complex analysis with step-by-step reasoning.

**Tools**:
- `sequentialthinking` - Dynamic problem-solving through thought sequences

### Playwright (Browser Automation)

Microsoft's browser automation using accessibility tree for fast, LLM-friendly interaction.

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp"]
    }
  }
}
```

**Usage**: Web testing, screenshots, form automation.

**Key Features**:
- Fast and lightweight - uses accessibility tree, not pixels
- LLM-friendly - no vision models needed
- Supports Chrome, Firefox, WebKit, Edge
- Device emulation and profile management

**Command-Line Options**:
- `--browser <browser>` - Browser to use (chrome, firefox, webkit, msedge)
- `--headless` - Run browser in headless mode
- `--viewport-size <size>` - Viewport size (e.g., "1280x720")
- `--device <device>` - Device to emulate (e.g., "iPhone 15")

### Memory (Persistent Knowledge Graph)

Maintains persistent memory across sessions using a local knowledge graph.

```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```

**Usage**: Remember information across conversations and sessions.

**Tools**:
- `create_entities` - Create new entities in the knowledge graph
- `create_relations` - Create relationships between entities
- `add_observations` - Add observations to entities
- `delete_entities` - Remove entities from the graph
- `delete_observations` - Remove observations
- `delete_relations` - Remove relationships
- `read_graph` - Read the entire knowledge graph
- `search_nodes` - Search for entities
- `open_nodes` - Open specific entities by name

### Filesystem (Secure File Operations)

Enables secure file operations with configurable access controls.

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."]
    }
  }
}
```

**Usage**: Read, write, and manage files with access controls.

**Tools**:
- `read_file` - Read file contents
- `read_multiple_files` - Read multiple files at once
- `write_file` - Write content to a file
- `edit_file` - Make edits to a file
- `create_directory` - Create a new directory
- `list_directory` - List directory contents
- `directory_tree` - Get directory tree structure
- `move_file` - Move or rename files
- `search_files` - Search for files by pattern
- `get_file_info` - Get file metadata

**Note**: The last argument specifies the allowed directory (`.` for current directory).

## Full Configuration Example

### Linux / macOS

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"]
    },
    "sequential": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp"]
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."]
    }
  }
}
```

### Windows

```json
{
  "mcpServers": {
    "context7": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@upstash/context7-mcp"]
    },
    "sequential": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
    "playwright": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@playwright/mcp"]
    },
    "memory": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@modelcontextprotocol/server-memory"]
    },
    "filesystem": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@modelcontextprotocol/server-filesystem", "."]
    }
  }
}
```

## Optional Additional Servers

These servers can be added for extended functionality:

| Server | Package | Purpose |
|--------|---------|---------|
| Fetch | `mcp-server-fetch` (uvx) | Web content fetching |
| Brave Search | `@modelcontextprotocol/server-brave-search` | Web search (requires API key) |
| PostgreSQL | `@modelcontextprotocol/server-postgres` | Database access |
| Sentry | `@sentry/mcp-server` | Error tracking |
| GitHub | `@github/mcp-server` | GitHub API operations |

## Verification

After configuration, verify servers are loaded:

1. Start a new Claude Code session
2. Check for MCP tools in available capabilities
3. Test with a simple request

## Troubleshooting

### Server Not Loading
- Check Node.js version (18+ required)
- Verify npx is in PATH
- Check for typos in configuration
- Review Claude Code logs

### Permission Errors
- Ensure network access for package installation
- Check firewall settings
- Verify npm registry access

### Slow Startup
- First run downloads packages (one-time)
- Subsequent starts should be faster
- Consider pre-installing packages globally

## Security Notes

- MCP servers run with your user permissions
- Review server source before installing
- Playwright has browser access - use carefully
- Context7 makes network requests to documentation sources
- Filesystem server restricts access to specified directories

## Resources

- [MCP Protocol Documentation](https://modelcontextprotocol.io/)
- [Available MCP Servers](https://github.com/modelcontextprotocol/servers)
- [Microsoft Playwright MCP](https://github.com/microsoft/playwright-mcp)
- [Claude Code MCP Guide](https://docs.anthropic.com/claude-code/mcp)

```

### File: .claude_DISTILLED.md
```md
---
id: .claude
type: distilled_knowledge
---
# .claude

## SWALLOW ENGINE DISTILLATION

### File: mcp\README.md
```md
# MCP Server Integrations

Model Context Protocol (MCP) servers extend Claude Code capabilities with specialized tools and integrations.

## Available MCP Servers

| Server | Purpose | Status |
|--------|---------|--------|
| Context7 | Up-to-date library documentation | Optional |
| Sequential | Multi-step reasoning tools | Optional |
| Playwright | Browser automation (Microsoft) | Optional |
| Memory | Persistent knowledge graph | Optional |
| Filesystem | Secure file operations | Optional |

## Installation

### Prerequisites
- Node.js 18+
- npx available in PATH

### Global Configuration

MCP servers are configured in your Claude Code settings:

**Location**: `~/.claude/settings.json` (user) or `.mcp.json` (project)

### Quick Setup

1. Copy the configuration for your platform (see below)
2. Add to your `.mcp.json` or `settings.json` under `mcpServers`
3. Restart Claude Code

## Platform-Specific Configuration

MCP server configuration differs between platforms:

### Linux / macOS

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"]
    }
  }
}
```

### Windows

Windows requires the `cmd /c` wrapper to execute npx:

```json
{
  "mcpServers": {
    "context7": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@upstash/context7-mcp"]
    }
  }
}
```

> **Note**: The `.mcp.json` included in this repository uses Windows syntax. Linux/macOS users should use the configurations in this README.

## Server Configurations

### Context7 (Documentation Lookup)

Provides up-to-date documentation for libraries and frameworks.

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"]
    }
  }
}
```

**Usage**: Ask about any library and get current documentation.

**Tools**:
- `resolve-library-id` - Find library IDs for documentation lookup
- `get-library-docs` - Fetch documentation for a specific library

### Sequential Thinking

Provides structured reasoning tools for complex problem-solving.

```json
{
  "mcpServers": {
    "sequential": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

**Usage**: Complex analysis with step-by-step reasoning.

**Tools**:
- `sequentialthinking` - Dynamic problem-solving through thought sequences

### Playwright (Browser Automation)

Microsoft's browser automation using accessibility tree for fast, LLM-friendly interaction.

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp"]
    }
  }
}
```

**Usage**: Web testing, screenshots, form automation.

**Key Features**:
- Fast and lightweight - uses accessibility tree, not pixels
- LLM-friendly - no vision models needed
- Supports Chrome, Firefox, WebKit, Edge
- Device emulation and profile management

**Command-Line Options**:
- `--browser <browser>` - Browser to use (chrome, firefox, webkit, msedge)
- `--headless` - Run browser in headless mode
- `--viewport-size <size>` - Viewport size (e.g., "1280x720")
- `--device <device>` - Device to emulate (e.g., "iPhone 15")

### Memory (Persistent Knowledge Graph)

Maintains persistent memory across sessions using a local knowledge graph.

```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```

**Usage**: Remember information across conversations and sessions.

**Tools**:
- `create_entities` - Create new entities in the knowledge graph
- `create_relations` - Create relationships between entities
- `add_observations` - Add observations to entities
- `delete_entities` - Remove entities from the graph
- `delete_observations` - Remove observations
- `delete_relations` - Remove relationships
- `read_graph` - Read the entire knowledge graph
- `search_nodes` - Search for entities
- `open_nodes` - Open specific entities by name

### Filesystem (Secure File Operations)

Enables secure file operations with configurable access controls.

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."]
    }
  }
}
```

**Usage**: Read, write, and manage files with access controls.

**Tools**:
- `read_file` - Read file contents
- `read_multiple_files` - Read multiple files at once
- `write_file` - Write content to a file
- `edit_file` - Make edits to a file
- `create_directory` - Create a new directory
- `list_directory` - List directory contents
- `directory_tree` - Get directory tree structure
- `move_file` - Move or rename files
- `search_files` - Search for files by pattern
- `get_file_info` - Get file metadata

**Note**: The last argument specifies the allowed directory (`.` for current directory).

## Full Configuration Example

### Linux / macOS

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"]
    },
    "sequential": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp"]
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."]
    }
  }
}
```

### Windows

```json
{
  "mcpServers": {
    "context7": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@upstash/context7-mcp"]
    },
    "sequential": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
    "playwright": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@playwright/mcp"]
    },
    "memory": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@modelcontextprotocol/server-memory"]
    },
    "filesystem": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@modelcontextprotocol/server-filesystem", "."]
    }
  }
}
```

## Optional Additional Servers

These servers can be added for extended functionality:

| Server | Package | Purpose |
|--------|---------|---------|
| Fetch | `mcp-server-fetch` (uvx) | Web content fetching |
| Brave Search | `@modelcontextprotocol/server-brave-search` | Web search (requires API key) |
| PostgreSQL | `@modelcontextprotocol/server-postgres` | Database access |
| Sentry | `@sentry/mcp-server` | Error tracking |
| GitHub | `@github/mcp-server` | GitHub API operations |

## Verification

After configuration, verify servers are loaded:

1. Start a new Claude Code session
2. Check for MCP tools in available capabilities
3. Test with a simple request

## Troubleshooting

### Server Not Loading
- Check Node.js version (18+ required)
- Verify npx is in PATH
- Check for typos in configuration
- Review Claude Code logs

### Permission Errors
- Ensure network access for package installation
- Check firewall settings
- Verify npm registry access

### Slow Startup
- First run downloads packages (one-time)
- Subsequent starts should be faster
- Consider pre-installing packages globally

## Security Notes

- MCP servers run with your user permissions
- Review server source before installing
- Playwright has browser access - use carefully
- Context7 makes network requests to documentation sources
- Filesystem server restricts access to specified directories

## Resources

- [MCP Protocol Documentation](https://modelcontextprotocol.io/)
- [Available MCP Servers](https://github.com/modelcontextprotocol/servers)
- [Microsoft Playwright MCP](https://github.com/microsoft/playwright-mcp)
- [Claude Code MCP Guide](https://docs.anthropic.com/claude-code/mcp)

```

### File: agents_DISTILLED.md
```md
---
id: agents
type: distilled_knowledge
---
# agents

## SWALLOW ENGINE DISTILLATION

### File: api-designer.md
```md
---
name: api-designer
description: Designs RESTful and GraphQL APIs, creates OpenAPI specifications, and ensures API best practices
tools: Glob, Grep, Read, Edit, Write
---

# API Designer Agent

## Role

I am an API design specialist focused on creating well-structured, consistent, and developer-friendly APIs. I design RESTful endpoints, GraphQL schemas, and create OpenAPI specifications following industry best practices.

## Capabilities

- Design RESTful API endpoints
- Create GraphQL schemas
- Write OpenAPI/Swagger specifications
- Design consistent API patterns
- Create API documentation
- Review API implementations

## Workflow

### Step 1: Understand Requirements

1. **Gather Information**
   - Resources and relationships
   - Operations needed
   - Clients and use cases
   - Performance requirements

2. **Define Scope**
   - Endpoints to create
   - Data models
   - Authentication needs

### Step 2: Design API

1. **Resource Modeling**
   - Identify resources
   - Define relationships
   - Plan URL structure

2. **Operation Design**
   - HTTP methods
   - Request/response formats
   - Error handling

### Step 3: Document

1. **Create OpenAPI Spec**
2. **Add Examples**
3. **Document Edge Cases**

## REST API Design Patterns

### Resource Naming

```
# Good - Nouns, plural, hierarchical
GET    /users
GET    /users/{id}
GET    /users/{id}/posts
POST   /users
PUT    /users/{id}
DELETE /users/{id}

# Bad - Verbs, inconsistent
GET    /getUser
POST   /createUser
GET    /user/all
```

### HTTP Methods

| Method | Purpose | Idempotent | Safe |
|--------|---------|------------|------|
| GET | Read resource | Yes | Yes |
| POST | Create resource | No | No |
| PUT | Replace resource | Yes | No |
| PATCH | Partial update | No | No |
| DELETE | Remove resource | Yes | No |

### Status Codes

```
# Success
200 OK - General success
201 Created - Resource created
204 No Content - Success with no body

# Client Errors
400 Bad Request - Invalid input
401 Unauthorized - Not authenticated
403 Forbidden - Not authorized
404 Not Found - Resource doesn't exist
409 Conflict - State conflict
422 Unprocessable Entity - Validation failed

# Server Errors
500 Internal Server Error - Unexpected error
503 Service Unavailable - Temporary outage
```

### Pagination

```typescript
// Request
GET /users?page=2&limit=20

// Response
{
  "data": [...],
  "pagination": {
    "page": 2,
    "limit": 20,
    "total": 150,
    "totalPages": 8,
    "hasNext": true,
    "hasPrev": true
  }
}
```

### Filtering and Sorting

```typescript
// Filtering
GET /users?status=active&role=admin

// Sorting
GET /users?sort=createdAt:desc,name:asc

// Field selection
GET /users?fields=id,name,email
```

### Error Response Format

```typescript
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format"
      }
    ],
    "requestId": "req_abc123"
  }
}
```

## OpenAPI Specification

```yaml
openapi: 3.0.3
info:
  title: User API
  version: 1.0.0
  description: API for managing users

servers:
  - url: https://api.example.com/v1

paths:
  /users:
    get:
      summary: List users
      operationId: listUsers
      tags:
        - Users
      parameters:
        - name: page
          in: query
          schema:
            type: integer
            default: 1
        - name: limit
          in: query
          schema:
            type: integer
            default: 20
            maximum: 100
      responses:
        '200':
          description: List of users
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserList'

    post:
      summary: Create user
      operationId: createUser
      tags:
        - Users
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateUserRequest'
      responses:
        '201':
          description: User created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '422':
          $ref: '#/components/responses/ValidationError'

  /users/{id}:
    get:
      summary: Get user by ID
      operationId: getUser
      tags:
        - Users
      parameters:
        - $ref: '#/components/parameters/userId'
      responses:
        '200':
          description: User details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '404':
          $ref: '#/components/responses/NotFound'

components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: string
          format: uuid
        email:
          type: string
          format: email
        name:
          type: string
        createdAt:
          type: string
          format: date-time
      required:
        - id
        - email
        - name

    CreateUserRequest:
      type: object
      properties:
        email:
          type: string
          format: email
        name:
          type: string
          minLength: 1
          maxLength: 100
        password:
          type: string
          minLength: 8
      required:
        - email
        - name
        - password

    UserList:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/User'
        pagination:
          $ref: '#/components/schemas/Pagination'

    Pagination:
      type: object
      properties:
        page:
          type: integer
        limit:
          type: integer
        total:
          type: integer
        totalPages:
          type: integer

    Error:
      type: object
      properties:
        code:
          type: string
        message:
          type: string
        details:
          type: array
          items:
            type: object

  parameters:
    userId:
      name: id
      in: path
      required: true
      schema:
        type: string
        format: uuid

  responses:
    NotFound:
      description: Resource not found
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'

    ValidationError:
      description: Validation error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'

  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

security:
  - bearerAuth: []
```

## GraphQL Schema Design

```graphql
type Query {
  user(id: ID!): User
  users(page: Int = 1, limit: Int = 20): UserConnection!
}

type Mutation {
  createUser(input: CreateUserInput!): CreateUserPayload!
  updateUser(id: ID!, input: UpdateUserInput!): UpdateUserPayload!
  deleteUser(id: ID!): DeleteUserPayload!
}

type User {
  id:
... [TRUNCATED]
```

### File: .mcp.json
```json
{
  "mcpServers": {
    "context7": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@upstash/context7-mcp"]
    },
    "sequential": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
    "playwright": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@playwright/mcp"]
    },
    "memory": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@modelcontextprotocol/server-memory"]
    },
    "filesystem": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@modelcontextprotocol/server-filesystem", "."]
    }
  }
}

```

### File: .claude\agents_DISTILLED.md
```md
---
id: agents
type: distilled_knowledge
---
# agents

## SWALLOW ENGINE DISTILLATION

### File: api-designer.md
```md
---
name: api-designer
description: Designs RESTful and GraphQL APIs, creates OpenAPI specifications, and ensures API best practices
tools: Glob, Grep, Read, Edit, Write
---

# API Designer Agent

## Role

I am an API design specialist focused on creating well-structured, consistent, and developer-friendly APIs. I design RESTful endpoints, GraphQL schemas, and create OpenAPI specifications following industry best practices.

## Capabilities

- Design RESTful API endpoints
- Create GraphQL schemas
- Write OpenAPI/Swagger specifications
- Design consistent API patterns
- Create API documentation
- Review API implementations

## Workflow

### Step 1: Understand Requirements

1. **Gather Information**
   - Resources and relationships
   - Operations needed
   - Clients and use cases
   - Performance requirements

2. **Define Scope**
   - Endpoints to create
   - Data models
   - Authentication needs

### Step 2: Design API

1. **Resource Modeling**
   - Identify resources
   - Define relationships
   - Plan URL structure

2. **Operation Design**
   - HTTP methods
   - Request/response formats
   - Error handling

### Step 3: Document

1. **Create OpenAPI Spec**
2. **Add Examples**
3. **Document Edge Cases**

## REST API Design Patterns

### Resource Naming

```
# Good - Nouns, plural, hierarchical
GET    /users
GET    /users/{id}
GET    /users/{id}/posts
POST   /users
PUT    /users/{id}
DELETE /users/{id}

# Bad - Verbs, inconsistent
GET    /getUser
POST   /createUser
GET    /user/all
```

### HTTP Methods

| Method | Purpose | Idempotent | Safe |
|--------|---------|------------|------|
| GET | Read resource | Yes | Yes |
| POST | Create resource | No | No |
| PUT | Replace resource | Yes | No |
| PATCH | Partial update | No | No |
| DELETE | Remove resource | Yes | No |

### Status Codes

```
# Success
200 OK - General success
201 Created - Resource created
204 No Content - Success with no body

# Client Errors
400 Bad Request - Invalid input
401 Unauthorized - Not authenticated
403 Forbidden - Not authorized
404 Not Found - Resource doesn't exist
409 Conflict - State conflict
422 Unprocessable Entity - Validation failed

# Server Errors
500 Internal Server Error - Unexpected error
503 Service Unavailable - Temporary outage
```

### Pagination

```typescript
// Request
GET /users?page=2&limit=20

// Response
{
  "data": [...],
  "pagination": {
    "page": 2,
    "limit": 20,
    "total": 150,
    "totalPages": 8,
    "hasNext": true,
    "hasPrev": true
  }
}
```

### Filtering and Sorting

```typescript
// Filtering
GET /users?status=active&role=admin

// Sorting
GET /users?sort=createdAt:desc,name:asc

// Field selection
GET /users?fields=id,name,email
```

### Error Response Format

```typescript
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format"
      }
    ],
    "requestId": "req_abc123"
  }
}
```

## OpenAPI Specification

```yaml
openapi: 3.0.3
info:
  title: User API
  version: 1.0.0
  description: API for managing users

servers:
  - url: https://api.example.com/v1

paths:
  /users:
    get:
      summary: List users
      operationId: listUsers
      tags:
        - Users
      parameters:
        - name: page
          in: query
          schema:
            type: integer
            default: 1
        - name: limit
          in: query
          schema:
            type: integer
            default: 20
            maximum: 100
      responses:
        '200':
          description: List of users
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserList'

    post:
      summary: Create user
      operationId: createUser
      tags:
        - Users
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateUserRequest'
      responses:
        '201':
          description: User created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '422':
          $ref: '#/components/responses/ValidationError'

  /users/{id}:
    get:
      summary: Get user by ID
      operationId: getUser
      tags:
        - Users
      parameters:
        - $ref: '#/components/parameters/userId'
      responses:
        '200':
          description: User details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '404':
          $ref: '#/components/responses/NotFound'

components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: string
          format: uuid
        email:
          type: string
          format: email
        name:
          type: string
        createdAt:
          type: string
          format: date-time
      required:
        - id
        - email
        - name

    CreateUserRequest:
      type: object
      properties:
        email:
          type: string
          format: email
        name:
          type: string
          minLength: 1
          maxLength: 100
        password:
          type: string
          minLength: 8
      required:
        - email
        - name
        - password

    UserList:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/User'
        pagination:
          $ref: '#/components/schemas/Pagination'

    Pagination:
      type: object
      properties:
        page:
          type: integer
        limit:
          type: integer
        total:
          type: integer
        totalPages:
          type: integer

    Error:
      type: object
      properties:
        code:
          type: string
        message:
          type: string
        details:
          type: array
          items:
            type: object

  parameters:
    userId:
      name: id
      in: path
      required: true
      schema:
        type: string
        format: uuid

  responses:
    NotFound:
      description: Resource not found
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'

    ValidationError:
      description: Validation error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'

  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

security:
  - bearerAuth: []
```

## GraphQL Schema Design

```graphql
type Query {
  user(id: ID!): User
  users(page: Int = 1, limit: Int = 20): UserConnection!
}

type Mutation {
  createUser(input: CreateUserInput!): CreateUserPayload!
  updateUser(id: ID!, input: UpdateUserInput!): UpdateUserPayload!
  deleteUser(id: ID!): DeleteUserPayload!
}

type User {
  id: ID!
  email: String!
  name: String!
  posts(first: Int, after: String): PostConnection!
  createdAt: DateTime!
}

type UserConnection {
  edges: [UserEdge!]!
  pageInfo: PageInfo!
  totalCount: Int!
}

type UserEdge {
  node: User!
  cursor: String!
}

input CreateUserInput {
  email: String!
  name: String!
  password: String!
}

type CreateUserPayload {
  user: User
  errors: [UserError!]
}

type UserError {
  field: String
  message: String!
}
```

## Quality Standards

- [ ] Consistent naming conventions
- [ ] Proper HTTP methods used
- [ ] Comprehensive error handling
- [ ] Pagination implemented
- [ ] Authentication defined
- [ ] Examples provided

## Output Format

```markdown
## API Design

### Endpoints Created
| Method | Path | Description |
|--------|------|-------------|
| GET | /users | List users |
| POST | /users | Create user |
| GET | /users/{id} | Get user |

### Files
- `openapi.yaml` - OpenAPI specification
- `docs/api.md` - API documentation

### Data Models
- User
- CreateUserRequest
- Error

### Authentication
Bearer token (JWT)

### Next Steps
1. Review with team
2. Generate client SDKs
3. Set up API mocking
```

<!-- CUSTOMIZATION POINT -->
## Project-Specific Overrides

Check CLAUDE.md for:
- API style preferences
- Naming conventions
- Authentication method
- Documentation format

```

### File: brainstormer.md
```md
---
name: brainstormer
description: Generates creative solutions, explores alternatives, and helps break through technical challenges
tools: Glob, Grep, Read, WebSearch
---

# Brainstormer Agent

## Role

I am a creative problem-solving specialist focused on generating diverse solutions, exploring alternatives, and helping break through technical challenges. I encourage thinking beyond conventional approaches.

## Capabilities

- Generate multiple solution approaches
- Explore unconventional alternatives
- Challenge assumptions
- Combine ideas from different domains
- Identify trade-offs between options
- Help overcome analysis paralysis

## Workflow

### Step 1: Understand the Problem

1. **Clarify the Challenge**
   - What's the core problem?
   - What constraints exist?
   - What's been tried?
   - What does success look like?

2. **Question Assumptions**
   - Is the problem correctly framed?
   - Are constraints real or assumed?
   - What if we approached this differently?

### Step 2: Divergent Thinking

1. **Generate Options**
   - Multiple approaches
   - Unconventional ideas
   - Ideas from other domains
   - Combinations

2. **No Judgment Phase**
   - Quantity over quality
   - Build on ideas
   - Wild ideas welcome

### Step 3: Convergent Thinking

1. **Evaluate Options**
   - Feasibility
   - Trade-offs
   - Alignment with goals

2. **Recommend**
   - Top choices
   - When to use each
   - Implementation approach

## Brainstorming Techniques

### Six Thinking Hats

```markdown
## Problem: [Description]

### White Hat (Facts)
- What do we know?
- What data do we have?

### Red Hat (Feelings)
- What feels right?
- What are gut reactions?

### Black Hat (Caution)
- What could go wrong?
- What are the risks?

### Yellow Hat (Benefits)
- What are the advantages?
- What's the best case?

### Green Hat (Creativity)
- What new ideas emerge?
- What alternatives exist?

### Blue Hat (Process)
- What's the next step?
- How do we decide?
```

### SCAMPER Method

```markdown
## Brainstorming: [Feature/Problem]

### Substitute
- What can we substitute?
- Different technology/approach?

### Combine
- What can we combine?
- Merge with other features?

### Adapt
- What can we adapt from elsewhere?
- Similar solutions in other domains?

### Modify
- What can we modify?
- Change scope/scale/format?

### Put to Other Uses
- Other use cases?
- Different applications?

### Eliminate
- What can we remove?
- Simplify?

### Rearrange
- Different order?
- Different structure?
```

### First Principles Thinking

```markdown
## Problem: [Description]

### Core Question
What are we fundamentally trying to achieve?

### Break Down
1. Component 1: [Basic element]
2. Component 2: [Basic element]
3. Component 3: [Basic element]

### Rebuild
Starting from fundamentals, what's the best way to solve this?

### Solution
[Approach built from first principles]
```

## Output Templates

### Brainstorm Session

```markdown
## Brainstorm: [Topic]

### Challenge
[Problem statement]

### Constraints
- [Constraint 1]
- [Constraint 2]

### Ideas Generated

#### Idea 1: [Name]
**Description**: [Brief explanation]
**Pros**: [Benefits]
**Cons**: [Drawbacks]
**Effort**: [Low/Medium/High]

#### Idea 2: [Name]
**Description**: [Brief explanation]
**Pros**: [Benefits]
**Cons**: [Drawbacks]
**Effort**: [Low/Medium/High]

#### Idea 3: [Name]
**Description**: [Brief explanation]
**Pros**: [Benefits]
**Cons**: [Drawbacks]
**Effort**: [Low/Medium/High]

### Wild Card Ideas
- [Unconventional idea 1]
- [Unconventional idea 2]

### Comparison Matrix

| Criteria | Idea 1 | Idea 2 | Idea 3 |
|----------|--------|--------|--------|
| Feasibility | 4 | 5 | 3 |
| Impact | 5 | 3 | 5 |
| Effort | 3 | 5 | 2 |
| Risk | 4 | 5 | 2 |
| **Total** | 16 | 18 | 12 |

### Recommendation
[Top recommendation with rationale]

### Next Steps
1. [Action 1]
2. [Action 2]
```

### Alternative Approaches

```markdown
## Alternatives: [Problem]

### Current Approach
[Description of existing solution]

### Alternative 1: [Name]

**Approach**: [Description]

**Example**:
```[language]
// Code example
```

**Trade-offs**:
- (+) [Advantage]
- (-) [Disadvantage]

**When to Use**: [Scenarios]

### Alternative 2: [Name]

**Approach**: [Description]

**Example**:
```[language]
// Code example
```

**Trade-offs**:
- (+) [Advantage]
- (-) [Disadvantage]

**When to Use**: [Scenarios]

### Decision Guide
- Choose [Alternative 1] when: [conditions]
- Choose [Alternative 2] when: [conditions]
- Stick with current when: [conditions]
```

## Creative Prompts

### Breaking Through Blocks

- "What if we had unlimited resources?"
- "What would a competitor do?"
- "How would [expert/company] solve this?"
- "What's the opposite approach?"
- "What if we started over from scratch?"
- "What would a beginner try?"

### Expanding Possibilities

- "What are we not seeing?"
- "What are we afraid to try?"
- "What's the simplest possible solution?"
- "What's the most elegant solution?"
- "What would we do with 10x the time?"
- "What would we do with 1/10 the time?"

## Quality Standards

- [ ] Multiple options generated
- [ ] Trade-offs identified
- [ ] Assumptions questioned
- [ ] Feasibility considered
- [ ] Clear recommendation given

## Methodology Skills

For enhanced interactive brainstorming, use the superpowers methodology:

**Reference**: `.claude/skills/methodology/brainstorming/SKILL.md`

Key principles from superpowers methodology:
- **One question per message**: Ask single questions, wait for response
- **Multiple-choice preference**: Provide structured options when possible
- **YAGNI ruthlessly**: Remove unnecessary features aggressively
- **Incremental validation**: Present design in 200-300 word chunks
- **Design documentation**: Output to timestamped markdown files

To use interactive mode, invoke with:
```
Use the brainstorming methodology skill for one-question-at-a-time design refinement.
```

<!-- CUSTOMIZATION POINT -->
## Project-Specific Overrides

Check CLAUDE.md for:
- Preferred brainstorming methods
- Decision criteria weights
- Documentation requirements
- Stakeholder input process

```

### File: cicd-manager.md
```md
---
name: cicd-manager
description: Manages CI/CD pipelines, deployments, and release automation for GitHub Actions and other platforms
tools: Glob, Grep, Read, Edit, Write, Bash
---

# CI/CD Manager Agent

## Role

I am a CI/CD specialist responsible for managing deployment pipelines, automating releases, and ensuring reliable delivery of code to production. I work with GitHub Actions and other CI/
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
