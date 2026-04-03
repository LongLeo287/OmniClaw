---
id: convexskills-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:10.281505
---

# KNOWLEDGE EXTRACT: convexskills
> **Extracted on:** 2026-03-30 13:23:40
> **Source:** convexskills

---

## File: `.gitignore`
```
# Dependencies
node_modules/

# PRDs and internal planning docs
prds/

# Build output
dist/
build/

# Environment files
.env
.env.local
.env.*.local

# OS files
.DS_Store
Thumbs.db

# IDE
.idea/
*.swp
*.swo

# Local config folders (not tracked)
.claude/
.cursor/
.opencode/

# Local task tracking
task.md

# Logs
*.log
npm-debug.log*
```

## File: `.npmignore`
```
# Development files
.cursor/
.claude/
.claude-plugin/
.opencode/
prds/

# Git
.git/
.gitignore

# Documentation (not needed in package)
docs.md
files.md
task.md
changelog.md
CONTRIBUTING.md

# Local files
*.log
node_modules/
```

## File: `agents.md`
```markdown
# Convex Skills

Agent skills for building production-ready applications with Convex, following the Agent Skills open format.

## Convex Documentation Index

IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning for any Convex tasks.

For up-to-date Convex documentation, fetch: https://docs.convex.dev/llms.txt

This index covers all Convex APIs and patterns:

```
[Convex Docs]|https://docs.convex.dev/llms.txt
|understanding:{best-practices.md,typescript.md,workflow.md,zen.md}
|functions:{query-functions.md,mutation-functions.md,actions.md,http-actions.md,validation.md,internal-functions.md,error-handling.md}
|database:{schemas.md,reading-data.md,writing-data.md,indexes.md,pagination.md,types.md}
|file-storage:{upload-files.md,serve-files.md,store-files.md,delete-files.md,file-metadata.md}
|scheduling:{cron-jobs.md,scheduled-functions.md}
|auth:{convex-auth.md,clerk.md,auth0.md,authkit.md,functions-auth.md,database-auth.md}
|search:{text-search.md,vector-search.md}
|components:{using.md,authoring.md,understanding.md}
|agents:{getting-started.md,agent-usage.md,messages.md,threads.md,tools.md,streaming.md,rag.md}
|realtime:{realtime.md}
|testing:{convex-test.md,convex-backend.md,ci.md}
|production:{environment-variables.md,hosting.md,limits.md}
```

When working on Convex code, consult the llms.txt index before relying on training data.

## Overview

This repository provides two complementary approaches for AI coding agents:

1. **Passive context (this file)**: Always-available Convex knowledge and doc references
2. **Skills (on-demand)**: Task-specific workflows for explicit invocation

## Available Skills

| Skill                                                                    | Description                                           |
| ------------------------------------------------------------------------ | ----------------------------------------------------- |
| [convex-best-practices](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)           | Guidelines for building production-ready Convex apps  |
| [convex-functions](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)                     | Writing queries, mutations, actions, and HTTP actions |
| [convex-realtime](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)                       | Patterns for building reactive applications           |
| [convex-schema-validator](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)       | Database schema definition and validation             |
| [convex-file-storage](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)               | File upload, storage, and serving                     |
| [convex-agents](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)                           | Building AI agents with Convex                        |
| [convex-cron-jobs](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)                     | Scheduled functions and background tasks              |
| [convex-http-actions](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)               | HTTP endpoints and webhook handling                   |
| [convex-migrations](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)                   | Schema evolution and data migrations                  |
| [convex-security-check](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)           | Quick security audit checklist                        |
| [convex-security-audit](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)           | Deep security review patterns                         |
| [convex-component-authoring](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | Creating reusable Convex components                   |

## Skill Format

Each skill follows the Agent Skills specification with YAML frontmatter:

```markdown
---
name: skill-name
description: What the skill does and when to use it
version: 1.0.0
author: Convex
tags: [convex, ...]
---

# Skill Name

## Documentation Sources

Links to official documentation

## Instructions

Step-by-step guidance

## Examples

Code examples

## Best Practices

Guidelines and patterns

## References

Additional resources
```

## Usage

Skills are automatically available once installed. The agent will use them when relevant tasks are detected.

**Examples:**

```
Help me set up file uploads in Convex
```

```
Create a cron job to clean up expired sessions
```

```
Add a Stripe webhook endpoint
```

### Slash Command (OpenCode)

Use the `/convex` slash command for contextual guidance:

```
/convex create a schema with users and posts
/convex set up file uploads
/convex add a Stripe webhook endpoint
```

The command file is located at `command/convex.md`.

## Key Convex Concepts

### Function Types

| Type         | Purpose        | Database                 | External APIs |
| ------------ | -------------- | ------------------------ | ------------- |
| `query`      | Read data      | Read-only                | No            |
| `mutation`   | Write data     | Read/Write               | No            |
| `action`     | Integrations   | Via runQuery/runMutation | Yes           |
| `httpAction` | HTTP endpoints | Via runQuery/runMutation | Yes           |

### Core Principles

1. **Always use validators** for arguments and returns
2. **Use indexes** instead of filters for queries
3. **Make mutations idempotent** with early returns
4. **Use internal functions** for sensitive operations
5. **Batch operations** for large datasets

## DO NOT

- Run `npx convex deploy` without explicit instruction
- Run any git commands without explicit instruction
- Edit files in `convex/_generated/`
- Use `filter()` instead of `withIndex()`

## Quick Reference

### New Function Syntax (always use this)

```typescript
import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

export const myQuery = query({
  args: { userId: v.id("users") },
  returns: v.union(v.object({ name: v.string() }), v.null()),
  handler: async (ctx, args) => {
    return await ctx.db.get(args.userId);
  },
});
```

### Schema with Index

```typescript
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  tasks: defineTable({
    userId: v.id("users"),
    title: v.string(),
    status: v.string(),
  })
    .index("by_user", ["userId"])
    .index("by_user_and_status", ["userId", "status"]),
});
```

### Query with Index (not filter)

```typescript
// GOOD: Use withIndex
const tasks = await ctx.db
  .query("tasks")
  .withIndex("by_user", (q) => q.eq("userId", args.userId))
  .collect();

// BAD: Never use filter for indexed fields
const tasks = await ctx.db
  .query("tasks")
  .filter((q) => q.eq(q.field("userId"), args.userId))
  .collect();
```

## References

- Convex Documentation: https://docs.convex.dev/
- Convex LLMs.txt: https://docs.convex.dev/llms.txt (fetch this for latest docs)
- Best Practices: https://docs.convex.dev/understanding/best-practices/
- Agent Skills Specification: https://github.com/anthropics/skills

## License

Apache-2.0
```

## File: `changelog.md`
```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Updated README.md to reference official Convex Agent Plugins repo as the primary resource
- Fixed typo in README heading ("offical" to "official")
- Removed banned word "comprehensive" from README description
- Updated package.json npm description to reference official Convex Agent Plugins

### Added

- Support for `.agents/skills` installs via CLI `--target`
- Optional `--link` flag to symlink SKILL.md files instead of copying

### Changed

- Consolidated `convex-eslint` skill into `convex-best-practices` Code Quality section
- ESLint setup instructions now include config example and rules table in one place
- Updated cross-references in `convex-functions`, README, AGENTS.md, and .codex/README.md

### Removed

- Deleted standalone `skills/convex-eslint/` directory (content merged into convex-best-practices)
- Removed `convex-eslint` from SKILLS constants in index.js and bin/cli.js

### Fixed

- Removed unsupported frontmatter fields from `skills/convex-best-practices/SKILL.md` to avoid Pi skill parser conflicts

## [1.0.7] - 2026-02-02

### Added

- Codex skill icons via `agents/openai.yaml` in every skill folder
- `assets/small-logo.svg` and `assets/large-logo.png` for Codex UI display

## [1.0.6] - 2026-02-02

### Added

- Retrieval-led reasoning pattern in AGENTS.md, CLAUDE.md, and GEMINI.md
  - Compressed Convex docs index pointing to https://docs.convex.dev/llms.txt
  - Instruction to prefer retrieval over pre-training for Convex tasks
- Quick Reference section with common code patterns (function syntax, schema, queries)
- `prds/how-it-works.md`: Internal documentation explaining AGENTS.md vs Skills approach
- Dual-approach architecture: passive context (AGENTS.md) + on-demand skills

### Changed

- Updated AGENTS.md with Convex Documentation Index section
- Updated CLAUDE.md with matching documentation index
- Updated GEMINI.md with llms.txt reference and retrieval instruction

### Fixed

- Added missing convex-eslint to bin/cli.js SKILLS object

### Notes

Based on Vercel's research showing AGENTS.md with docs index achieves 100% pass rate vs 53% for skills alone.
See: https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals

## [1.0.5] - 2026-02-02

### Added

- `skills/convex-eslint/SKILL.md`: ESLint compliance skill for writing linter-clean Convex code
  - Covers all four @convex-dev/eslint-plugin rules
  - Setup instructions for eslint.config.js
  - Code examples for each rule (no-old-registered-function-syntax, require-argument-validators, explicit-table-ids, import-wrong-runtime)
- `.codex/README.md`: Codex CLI integration instructions
- Code Quality sections in `convex-functions` and `convex-best-practices` skills
- Linting section in `templates/CLAUDE.md`
- Code Quality section in `README.md`

### Changed

- Updated all db.get, db.patch, db.delete, db.replace calls in skills to use explicit table names
- Updated `README.md` Available Skills table to include convex-eslint
- Updated `AGENTS.md` and `CLAUDE.md` to include convex-eslint in skills list
- Updated `index.js` SKILLS constant with convex-eslint
- Updated `package.json` version to 1.0.5, added eslint and linting keywords
- Updated `files.md` to document convex-eslint skill and .codex directory
- Updated repository structure in README to include .codex folder

## [1.0.4] - 2026-01-14

### Added

- Template skills for developers who fork the repository
  - `templates/skills/README.md`: Installation and usage guide
  - `templates/skills/dev.md`: Full-stack development practices template
  - `templates/skills/help.md`: Problem-solving methodology template
  - `templates/skills/gitrules.md`: Git safety protocols template
- `files.md`: Codebase structure reference
- `task.md`: Completed task tracking
- `docs.md`: Documentation index
- `skills/convex/SKILL.md`: Umbrella skill indexing all Convex skills

### Changed

- Updated `README.md` with templates section and repository structure

### Fixed

- Skill `name` field now matches folder name for `/skill` commands to work
  - Changed from human readable (e.g., `Convex Best Practices`) to kebab-case (e.g., `convex-best-practices`)
  - Added `displayName` field for human readable names
  - Affects all 12 Convex skill files

## [1.0.0] - 2026-01-14

### Added

- Initial repository structure mirroring getsentry/skills pattern
- 9 core Convex skills:
  - `convex-best-practices`: Production-ready app guidelines, error handling, OCC
  - `convex-functions`: Queries, mutations, actions, HTTP actions
  - `convex-realtime`: Reactive patterns, subscriptions, optimistic updates
  - `convex-schema-validator`: Schema definition, typing, validation, migrations
  - `convex-file-storage`: File upload, storage, serving, metadata
  - `convex-agents`: AI agents with thread management and tools
  - `convex-security-check`: Quick security audit checklist
  - `convex-security-audit`: Deep security review patterns
  - `convex-component-authoring`: Creating reusable Convex components
- Skill template following Anthropic approved format
- Terminal UI for skill browsing with amber/gold tree design
- GEMINI.md for Gemini CLI integration
- agents.md specification for Convex agents
- CLAUDE.md template for Convex projects
- Future skills exploration document
- OpenCode plugin for Convex sync:
  - Plugin hooks for session, file, and tool events
  - Custom tools (schema_suggest, function_test, migration_plan)
  - Agent templates (convex-build.md, convex-debug.md)
  - Command templates (convex-init, convex-deploy, convex-logs)
  - Installation script
- Phase 3 documentation recommendations for Convex docs
- Phase 4 documentation recommendations for convex.dev/ai
- Project tracking files (files.md, changelog.md)
- README.md with installation instructions
- CONTRIBUTING.md with guidelines
- MIT License
```

## File: `CLAUDE.md`
```markdown
AGENTS.md
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing to Convex Skills

Thank you for your interest in contributing to Convex Skills.

## How to Contribute

### Reporting Issues

- Use GitHub Issues to report bugs or suggest features
- Include as much detail as possible
- For security issues, please email security@convex.dev directly

### Submitting Changes

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-skill`)
3. Make your changes
4. Test your changes thoroughly
5. Submit a pull request

### Skill Guidelines

When creating or modifying skills:

1. **Follow the Template**: Use the Anthropic-approved skill format in `skills/template/SKILL.md`
2. **Fetch Documentation**: Always reference the latest Convex documentation
3. **Include Examples**: Provide working code examples
4. **Test Thoroughly**: Verify all code examples work correctly

### Code Style

- Use TypeScript for all code examples
- Follow Convex best practices
- Include proper type annotations
- Add comments for complex logic

### Commit Messages

- Use clear, descriptive commit messages
- Reference issue numbers when applicable
- Keep commits focused on single changes

## Best Practices

When contributing:

- Never run `npx convex deploy` unless explicitly instructed
- Never run git commands without proper guidance
- Always verify documentation links are current
- Test all code examples before submitting

## Questions

For questions about contributing, open a GitHub Discussion or reach out to the Convex team.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
```

## File: `docs.md`
```markdown
# Documentation Index

Quick reference to all documentation in this repository.

## Getting Started

| Document | Purpose |
|----------|---------|
| [README.md](README.md) | Project overview, installation, quick start |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute to this project |
| [LICENSE](LICENSE) | Apache-2.0 license terms |

## Agent Integration

| Document | Purpose |
|----------|---------|
| [AGENTS.md](../../../.claude/skills/supabase-postgres-best-practices/AGENTS.md) | Agent skills specification for AI coding agents |
| [CLAUDE.md](CLAUDE.md) | Claude Code project context |
| [GEMINI.md](../../agents/GEMINI.md) | Gemini CLI integration |

## Skills Reference

All skills follow the Agent Skills specification format.

| Skill | What it teaches |
|-------|-----------------|
| [convex-best-practices](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | Production patterns, error handling, OCC |
| [convex-functions](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | Queries, mutations, actions, HTTP actions |
| [convex-realtime](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | Subscriptions, optimistic updates |
| [convex-schema-validator](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | Schema definition, typing, validation |
| [convex-file-storage](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | Upload, storage, serving files |
| [convex-agents](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | AI agents with thread management |
| [convex-cron-jobs](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | Scheduled functions, background tasks |
| [convex-http-actions](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | HTTP endpoints, webhooks |
| [convex-migrations](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | Schema evolution, data migrations |
| [convex-security-check](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | Quick security audit checklist |
| [convex-security-audit](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | Deep security review patterns |
| [convex-component-authoring](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | Reusable Convex components |

## Templates

Templates for developers to copy when starting new projects or forking.

| Template | Purpose |
|----------|---------|
| [templates/CLAUDE.md](../../../.claude/skills/supabase-postgres-best-practices/CLAUDE.md) | Project context template for Convex projects |
| [templates/skills/](templates/skills/) | Claude Code skills templates |

### Skill Templates

| Template | Purpose |
|----------|---------|
| [templates/skills/dev.md](dev.md) | Full-stack development practices |
| [templates/skills/help.md](help.md) | Problem-solving methodology |
| [templates/skills/gitrules.md](templates/skills/gitrules.md) | Git safety protocols |

## Project Tracking

| Document | Purpose |
|----------|---------|
| [changelog.md](changelog.md) | Version history |
| [files.md](files.md) | Codebase structure reference |
| [task.md](../../../vault/archives/archive_legacy/openapi-generator/samples/openapi3/client/petstore/python/docs/Task.md) | Completed task tracking |

## Planning Documents

Located in `prds/` directory.

| Document | Purpose |
|----------|---------|
| [skillsplan.md](prds/skillsplan.md) | Skills development roadmap |
| [future-skills-exploration.md](prds/future-skills-exploration.md) | Future skills ideas |
| [CLAUDE-MD-STRATEGY.md](prds/CLAUDE-MD-STRATEGY.md) | CLAUDE.md template strategy |

## External References

| Resource | URL |
|----------|-----|
| Convex Documentation | https://docs.convex.dev/ |
| Convex LLMs.txt | https://docs.convex.dev/llms.txt |
| Convex Best Practices | https://docs.convex.dev/understanding/best-practices/ |
| Agent Skills Spec | https://github.com/anthropics/skills |
```

## File: `files.md`
```markdown
# Codebase Files

Brief description of each file in the repository.

## Root Files

| File              | Description                                                      |
| ----------------- | ---------------------------------------------------------------- |
| `AGENTS.md`       | Agent context with Convex docs index and retrieval-led reasoning |
| `CLAUDE.md`       | Claude Code project context (mirrors AGENTS.md)                  |
| `CONTRIBUTING.md` | Contribution guidelines                                          |
| `GEMINI.md`       | Gemini CLI integration with llms.txt reference                   |
| `LICENSE`         | Apache-2.0 license                                               |
| `README.md`       | Project overview, links to official Convex Agent Plugins, and installation |
| `changelog.md`    | Version history following keepachangelog format                  |
| `files.md`        | This file, codebase structure reference                          |
| `task.md`         | Completed task tracking                                          |

## Skills Directory (`skills/`)

Core Convex skills for AI agents. Each skill has `name` matching folder name for `/skill` commands. Each skill includes `agents/openai.yaml` plus `assets/small-logo.svg` and `assets/large-logo.png` for Codex UI icons and metadata.

| Skill                                 | Description                                                            |
| ------------------------------------- | ---------------------------------------------------------------------- |
| `avoid-feature-creep/SKILL.md`        | Prevent scope creep in development                                     |
| `convex/SKILL.md`                     | Umbrella index for all Convex skills                                   |
| `convex-agents/SKILL.md`              | Building AI agents with Convex                                         |
| `convex-best-practices/SKILL.md`      | Production-ready app guidelines with ESLint setup in Code Quality      |
| `convex-component-authoring/SKILL.md` | Creating reusable Convex components                                    |
| `convex-cron-jobs/SKILL.md`           | Scheduled functions and background tasks                               |
| `convex-file-vault/SKILL.md`        | File upload, storage, and serving                                      |
| `convex-functions/SKILL.md`           | Queries, mutations, actions                                            |
| `convex-http-actions/SKILL.md`        | HTTP endpoints and webhooks                                            |
| `convex-migrations/SKILL.md`          | Schema evolution and data migrations                                   |
| `convex-realtime/SKILL.md`            | Reactive patterns and subscriptions                                    |
| `convex-schema-validator/SKILL.md`    | Schema definition and validation                                       |
| `convex-security-audit/SKILL.md`      | Deep security review patterns                                          |
| `convex-security-check/SKILL.md`      | Quick security audit checklist                                         |

## Command Directory (`command/`)

Slash command definitions for OpenCode integration.

| File        | Description                                            |
| ----------- | ------------------------------------------------------ |
| `convex.md` | `/convex` slash command entrypoint with decision trees |

## Templates Directory (`templates/`)

Templates for developers to copy when forking.

| File                 | Description                                  |
| -------------------- | -------------------------------------------- |
| `CLAUDE.md`          | Project context template for Convex projects |
| `skills/README.md`   | Installation guide for skill templates       |
| `skills/dev.md`      | Full-stack development practices template    |
| `skills/help.md`     | Problem-solving methodology template         |
| `skills/gitrules.md` | Git safety protocols template                |

## Claude Skills Directory (`.claude/skills/`)

Active Claude Code skills for this repository.

| File          | Description                       |
| ------------- | --------------------------------- |
| `convex.md`   | Convex-specific coding guidelines |
| `dev.md`      | Full-stack development practices  |
| `gitrules.md` | Git safety protocols              |
| `help.md`     | Problem-solving methodology       |
| `write.md`    | Writing style guide               |

## Standard Agent Skills Directory (`.agents/skills/`)

Compatibility skills path for tools that scan `.agents/skills`.

| Directory | Description                                               |
| --------- | --------------------------------------------------------- |
| `skills/` | Target directory created by CLI or symlinked to `skills/` |

## PRDs Directory (`prds/`)

Product requirement documents and planning.

| File                                          | Description                                   |
| --------------------------------------------- | --------------------------------------------- |
| `CLAUDE-MD-STRATEGY.md`                       | Strategy for CLAUDE.md templates              |
| `CLAUDE-MD-STRATEGY_1.md`                     | Alternate strategy document                   |
| `convex-skills-updates-plan.md`               | Build guide and maintenance plan              |
| `create-convex-opencode-integration.md`       | OpenCode integration spec                     |
| `future-skills-exploration.md`                | Future skills roadmap                         |
| `how-it-works.md`                             | AGENTS.md vs Skills dual approach explanation |
| `MARKETPLACE-SUBMISSION.md`                   | Marketplace submission guidelines             |
| `phase3-convex-docs-recommendations.md`       | Convex docs improvement recommendations       |
| `phase4-convex-ai-website-recommendations.md` | convex.dev/ai recommendations                 |
| `skillsplan.md`                               | Skills development plan                       |

## OpenCode Directory (`.opencode/`)

OpenCode plugin configuration and templates.

| Directory     | Description                             |
| ------------- | --------------------------------------- |
| `agent/`      | Agent templates for orchestration       |
| `command/`    | Command templates for Convex operations |
| `plugin/`     | Plugin hooks and tools                  |
| `skill/`      | OpenCode-specific skills                |
| `config.json` | Plugin configuration                    |

## Codex Directory (`.codex/`)

Codex CLI skills integration.

| File        | Description                          |
| ----------- | ------------------------------------ |
| `README.md` | Codex setup and symlink instructions |

## Cursor Directory (`.cursor/`)

Cursor IDE configuration.

| Directory | Description                |
| --------- | -------------------------- |
| `plans/`  | Development plans          |
| `rules/`  | Workspace rules for Cursor |
```

## File: `GEMINI.md`
```markdown
# Convex Development Context

This file provides context for Gemini CLI when working with Convex projects.

## Convex Documentation

IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning for any Convex tasks.

For up-to-date Convex documentation, fetch: https://docs.convex.dev/llms.txt

This index covers all Convex APIs:
- functions: queries, mutations, actions, http-actions, validation
- database: schemas, reading-data, writing-data, indexes, pagination
- file-storage: upload, serve, store, delete, metadata
- scheduling: cron-jobs, scheduled-functions
- auth: convex-auth, clerk, auth0, authkit
- search: text-search, vector-search
- agents: getting-started, messages, threads, tools, streaming

When working on Convex code, consult llms.txt before relying on training data.

## Project Type

Convex real-time backend application with TypeScript.

## Key Technologies

- **Convex** - Serverless database and functions platform
- **TypeScript** - Type-safe JavaScript
- **React** - Frontend framework (typical Convex frontend)

## Convex-Specific Guidelines

### Function Types

| Type | Purpose | Database Access | External APIs |
|------|---------|-----------------|---------------|
| `query` | Read data | Read-only | No |
| `mutation` | Modify data | Read/Write | No |
| `action` | External integrations | Via runQuery/runMutation | Yes |
| `httpAction` | Webhooks/APIs | Via runQuery/runMutation | Yes |

### Best Practices

1. **Always use validators** for args and returns
2. **Use indexes** instead of filters for queries
3. **Make mutations idempotent** for write conflict handling
4. **Use internal functions** for sensitive operations

### Commands

```bash
# Start development
npx convex dev

# Generate types
npx convex codegen

# View logs
npx convex logs

# Open dashboard
npx convex dashboard
```

### Do NOT Run Without Instruction

- `npx convex deploy` - Production deployment
- Any git commands

## Schema Reference

Schema is defined in `convex/schema.ts`:

```typescript
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  // Tables defined here
});
```

## Available Functions

Functions are in the `convex/` directory:
- Queries: Read-only data access
- Mutations: Data modifications
- Actions: External API calls

## Documentation

- Convex Docs: https://docs.convex.dev/
- LLMs.txt: https://docs.convex.dev/llms.txt
- Convex Skills: https://github.com/get-convex/convex-skills

## Error Handling

Use `ConvexError` for user-facing errors:

```typescript
import { ConvexError } from "convex/values";

throw new ConvexError({
  code: "NOT_FOUND",
  message: "Resource not found"
});
```

## File Structure

```
project/
├── convex/
│   ├── _generated/     # Auto-generated (don't edit)
│   ├── schema.ts       # Database schema
│   └── *.ts           # Function files
├── src/               # Frontend code
└── package.json
```
```

## File: `index.js`
```javascript
import { fileURLToPath } from "url";
import { dirname, join } from "path";
import { readFileSync, readdirSync, existsSync } from "fs";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

/**
 * Get the path to the skills directory
 */
export function getSkillsPath() {
  return join(__dirname, "skills");
}

/**
 * Get the path to the templates directory
 */
export function getTemplatesPath() {
  return join(__dirname, "templates");
}

/**
 * List all available skills
 */
export function listSkills() {
  const skillsPath = getSkillsPath();
  const skills = readdirSync(skillsPath, { withFileTypes: true })
    .filter((dirent) => dirent.isDirectory())
    .map((dirent) => dirent.name);
  return skills;
}

/**
 * Get a skill's content by name
 */
export function getSkill(skillName) {
  const skillPath = join(getSkillsPath(), skillName, "SKILL.md");
  if (!existsSync(skillPath)) {
    throw new Error(`Skill not found: ${skillName}`);
  }
  return readFileSync(skillPath, "utf-8");
}

/**
 * Get the path to a specific skill
 */
export function getSkillPath(skillName) {
  return join(getSkillsPath(), skillName, "SKILL.md");
}

/**
 * Available skills with descriptions
 */
export const SKILLS = {
  "convex-best-practices":
    "Guidelines for building production-ready Convex apps",
  "convex-functions": "Writing queries, mutations, actions, and HTTP actions",
  "convex-realtime": "Patterns for building reactive applications",
  "convex-schema-validator": "Database schema definition and validation",
  "convex-file-storage": "File upload, storage, and serving",
  "convex-agents": "Building AI agents with Convex",
  "convex-cron-jobs": "Scheduled functions and background tasks",
  "convex-http-actions": "HTTP endpoints and webhook handling",
  "convex-migrations": "Schema evolution and data migrations",
  "convex-security-check": "Quick security audit checklist",
  "convex-security-audit": "Deep security review patterns",
  "convex-component-authoring": "Creating reusable Convex components",
};

export default {
  getSkillsPath,
  getTemplatesPath,
  listSkills,
  getSkill,
  getSkillPath,
  SKILLS,
};
```

## File: `LICENSE`
```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to the Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   Copyright 2026 Convex, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## File: `package.json`
```json
{
  "name": "@waynesutton/convex-skills",
  "version": "1.0.9",
  "description": "For official Convex Skills use Convex Agent Plugins at https://github.com/get-convex/convex-agent-plugins. This package provides unofficial agent skills for building production-ready Convex applications.",
  "author": "Wayne Sutton - @waynesutton",
  "license": "Apache-2.0",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/waynesutton/convexskills.git"
  },
  "homepage": "https://github.com/waynesutton/convexskills#readme",
  "bugs": {
    "url": "https://github.com/waynesutton/convexskills/issues"
  },
  "keywords": [
    "convex",
    "convex-skills",
    "ai-skills",
    "agent-skills",
    "claude",
    "codex",
    "llm",
    "ai-assistant",
    "best-practices",
    "developer-tools",
    "eslint",
    "linting"
  ],
  "type": "module",
  "main": "index.js",
  "bin": {
    "convex-skills": "./bin/cli.js"
  },
  "files": [
    "skills/**/*.md",
    "templates/**/*.md",
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    "index.js",
    "bin/"
  ],
  "scripts": {
    "prepublishOnly": "echo 'Publishing convex-skills to npm...'",
    "postpublish": "echo 'Published successfully!'"
  },
  "engines": {
    "node": ">=18.0.0"
  }
}
```

## File: `README.md`
```markdown
# For official Convex Skills use Convex Agent Plugins

Official Convex plugins for AI coding agents, providing development tools for building reactive backends with TypeScript.

https://github.com/get-convex/convex-agent-plugins


## Convex (unofficial) Skills 

[![npm version](https://img.shields.io/npm/v/@waynesutton/convex-skills.svg)](https://www.npmjs.com/package/@waynesutton/convex-skills)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

A collection of AI-consumable skills for building production-ready applications with [Convex](https://convex.dev), following the Agent Skills open format.

## Overview

This repository contains skills that help AI assistants understand and implement Convex best practices. Each skill provides structured guidance for specific aspects of Convex development.

## Code Quality

All skills are designed to produce code that passes @convex-dev/eslint-plugin by default. This creates a complementary workflow:

- **Skills** prevent mistakes at generation time
- **ESLint** catches anything that slips through at build time

See the Code Quality section in [convex-best-practices](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) for setup instructions.

## Installation

### npm (recommended)

```bash
# Install globally for CLI access
npm install -g @waynesutton/convex-skills

# List available skills
convex-skills list

# Install a specific skill to your project
convex-skills install convex-best-practices

# Install all skills
convex-skills install-all

# Install all skills to .agents/skills
convex-skills install-all --target agents

# Symlink SKILL.md files instead of copying
convex-skills install-all --target agents --link

# Install templates (CLAUDE.md + skill templates)
convex-skills install-templates
```

Or use npx without installing:

```bash
npx @waynesutton/convex-skills list
npx @waynesutton/convex-skills install-all
```

### Programmatic Usage

```bash
npm install @waynesutton/convex-skills
```

```javascript
import { listSkills, getSkill, SKILLS } from "@waynesutton/convex-skills";

// List all skills
console.log(listSkills());

// Get a specific skill's content
const content = getSkill("convex-best-practices");
```

### Claude Code (from local clone)

```bash
git clone https://github.com/waynesutton/convexskills.git
cd convexskills
# Point Claude Code to this directory
```

### Codex

Follow the Codex skills guide and place the skill under `$CODEX_HOME/skills`:

```bash
# From the repo root
# Defaults to ~/.codex if CODEX_HOME is unset
cp -r skills/convex-best-practices "$CODEX_HOME/skills/"
```

Codex will auto-discover `SKILL.md` files in that directory on the next start.

If you are working from a repo clone, Codex also auto-discovers skills from `.codex/skills` at the repo root. You can symlink this repo’s `skills/*` into `.codex/skills` so updates flow through without copying.

### Standard Agent Skills Path

Some tools are standardizing on `.agents/skills` for discovery. This repo supports that layout via the CLI:

```bash
convex-skills install-all --target agents
convex-skills install-all --target agents --link
```

### OpenCode

OpenCode discovers skills from `~/.claude/skills/<name>/SKILL.md` automatically. See OpenCode Skills docs for more details.

#### Slash Command

This repo includes a `/convex` slash command for OpenCode. Install the command by copying `command/convex.md` to your OpenCode commands directory:

```bash
# Copy the slash command
cp command/convex.md ~/.opencode/command/

# Usage in OpenCode
/convex create a schema with users and posts
/convex set up file uploads
/convex add a Stripe webhook endpoint
```

The slash command provides decision trees to route to the appropriate skill based on your task.

### Manual Installation

Copy the desired skill's `SKILL.md` file to your project's `.claude/skills/` directory.

## Available Skills

| Skill                                                                    | Description                                           |
| ------------------------------------------------------------------------ | ----------------------------------------------------- |
| [convex-best-practices](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)           | Guidelines for building production-ready Convex apps  |
| [convex-functions](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)                     | Writing queries, mutations, actions, and HTTP actions |
| [convex-realtime](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)                       | Patterns for building reactive applications           |
| [convex-schema-validator](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)       | Database schema definition and validation             |
| [convex-file-storage](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)               | File upload, storage, and serving                     |
| [convex-agents](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)                           | Building AI agents with Convex                        |
| [convex-cron-jobs](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)                     | Scheduled functions and background tasks              |
| [convex-http-actions](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)               | HTTP endpoints and webhook handling                   |
| [convex-migrations](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)                   | Schema evolution and data migrations                  |
| [convex-security-check](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)           | Quick security audit checklist                        |
| [convex-security-audit](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)           | Deep security review patterns                         |
| [convex-component-authoring](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | Creating reusable Convex components                   |

## Repository Structure

```
convex-skills/
├── skills/                   # Core Convex skills for AI agents
│   ├── convex-best-practices/
│   │   └── SKILL.md
│   ├── convex-functions/
│   │   └── SKILL.md
│   ├── convex-cron-jobs/
│   │   └── SKILL.md
│   └── ...
├── .codex/                   # Codex integration (symlink skills here)
│   └── README.md             # Codex setup instructions
├── .agents/                  # Standard agent skills path
├── command/                  # Slash command definitions (OpenCode)
│   └── convex.md             # /convex command entrypoint
├── templates/                # Templates for forking developers
│   ├── CLAUDE.md             # Project context template
│   └── skills/               # Claude Code skill templates
│       ├── dev.md            # Full-stack development practices
│       ├── help.md           # Problem-solving methodology
│       └── gitrules.md       # Git safety protocols
├── .claude/skills/           # Active skills for this repo
├── prds/                     # Planning documents
├── AGENTS.md                 # Agent-facing documentation
├── CLAUDE.md                 # Claude configuration
├── GEMINI.md                 # Gemini CLI integration
├── README.md                 # This file
└── LICENSE                   # Apache-2.0
```

## Templates for Forking

When you fork this repository, you can copy the templates to set up Claude Code skills for your project:

```bash
# Copy skill templates to your project
cp -r templates/skills/* .claude/skills/

# Or copy specific skills
cp templates/skills/dev.md .claude/skills/
cp templates/skills/help.md .claude/skills/
cp templates/skills/gitrules.md .claude/skills/
```

| Template                                                     | Description                                  |
| ------------------------------------------------------------ | -------------------------------------------- |
| [templates/CLAUDE.md](../../../.claude/skills/supabase-postgres-best-practices/CLAUDE.md)                   | Project context template for Convex projects |
| [templates/skills/dev.md](dev.md)           | Full-stack development practices             |
| [templates/skills/help.md](help.md)         | Problem-solving methodology                  |
| [templates/skills/gitrules.md](templates/skills/gitrules.md) | Git safety protocols                         |

See [templates/skills/README.md](../../../README.md) for detailed installation instructions.

## Skill Format

Each skill follows the Agent Skills specification:

```markdown
---
name: Skill Name
description: Brief description
version: 1.0.0
author: Convex
tags: [convex, ...]
---

# Skill Name

## Documentation Sources

## Instructions

## Examples

## Best Practices

## References
```

## Usage

Skills are automatically available once installed. The agent will use them when relevant tasks are detected.

**Examples:**

```
Help me set up file uploads in Convex
```

```
Create a cron job to clean up expired sessions
```

```
Add a webhook endpoint for Stripe
```

## Creating New Skills

Skills follow the Agent Skills specification. Each skill requires a `SKILL.md` file with YAML frontmatter.

### Skill Template

Create a new directory under `skills/`:

```
skills/my-skill/
└── SKILL.md
```

**SKILL.md format:**

```markdown
---
name: my-skill
description: A clear description of what this skill does
version: 1.0.0
author: Convex
tags: [convex, relevant-tags]
---

# My Skill Name

## Documentation Sources

Links to official documentation

## Instructions

Step-by-step guidance for the agent

## Examples

Concrete examples showing expected code patterns

## Best Practices

Specific rules to follow

## References

Additional resources
```

## AI Integration Files

- `AGENTS.md` - Agent-facing documentation
- `CLAUDE.md` - Claude configuration for Convex projects
- `GEMINI.md` - Gemini CLI integration for Convex projects

## License

Apache-2.0 License - see [LICENSE](LICENSE) for details.

## References

- [npm Package](https://www.npmjs.com/package/@waynesutton/convex-skills)
- [Convex Documentation](https://docs.convex.dev/)
- [Convex LLMs.txt](https://docs.convex.dev/llms.txt)
- [Agent Skills Specification](https://github.com/anthropics/skills)
```

## File: `command/convex.md`
```markdown
# /convex

Convex platform reference for AI/LLM consumption. Load this skill for contextual guidance when building with Convex.

## Usage

```
/convex create a schema with users and posts
/convex set up file uploads
/convex add a cron job to clean up expired sessions
/convex build an AI agent with tools
/convex add a Stripe webhook endpoint
/convex run a security audit
/convex --update-skill
```

## Quick Reference

### Function Types

| Type | Database | External APIs | Use Case |
|------|----------|---------------|----------|
| `query` | Read-only | No | Fetching data (reactive, cached) |
| `mutation` | Read/Write | No | Modifying data (transactional) |
| `action` | Via runQuery/runMutation | Yes | External integrations |
| `httpAction` | Via runQuery/runMutation | Yes | Webhooks, REST APIs |

### Core Principles

1. **Always use validators** for args and returns
2. **Use indexes** instead of filters for queries
3. **Make mutations idempotent** with early returns
4. **Use internal functions** for sensitive operations
5. **Batch operations** for large datasets

## Decision Trees

### What are you building?

```
Need to store/query data?
├── Define schema → load convex-schema-validator
├── Write functions → load convex-functions
└── Build reactive UI → load convex-realtime

Need external integrations?
├── Webhooks/REST API → load convex-http-actions
├── Scheduled tasks → load convex-cron-jobs
└── File handling → load convex-file-storage

Building AI features?
├── AI agents with tools → load convex-agents
├── Vector search/RAG → load convex-agents
└── LLM integrations → load convex-agents

Need to review code?
├── Quick security check → load convex-security-check
├── Deep security audit → load convex-security-audit
└── Best practices review → load convex-best-practices

Maintaining existing code?
├── Schema changes → load convex-migrations
├── Component creation → load convex-component-authoring
└── General improvements → load convex-best-practices
```

### Database Operations

```
Working with data?
├── Schema definition
│   └── → convex-schema-validator
│       - defineSchema, defineTable
│       - Validators (v.string(), v.id(), etc.)
│       - Indexes for efficient queries
│
├── Reading data
│   └── → convex-functions (queries section)
│       - ctx.db.get(id)
│       - ctx.db.query("table").withIndex()
│       - .collect(), .first(), .unique()
│
├── Writing data
│   └── → convex-functions (mutations section)
│       - ctx.db.insert()
│       - ctx.db.patch()
│       - ctx.db.replace()
│       - ctx.db.delete()
│
└── Real-time subscriptions
    └── → convex-realtime
        - useQuery() hooks
        - Optimistic updates
```

### External Integrations

```
Integrating external services?
├── Webhooks (Stripe, Clerk, etc.)
│   └── → convex-http-actions
│       - httpRouter()
│       - Signature verification
│       - Response handling
│
├── REST API endpoints
│   └── → convex-http-actions
│       - Path parameters
│       - CORS handling
│       - Authentication
│
├── Scheduled background jobs
│   └── → convex-cron-jobs
│       - crons.interval()
│       - crons.cron()
│       - Cleanup tasks
│
└── File uploads/downloads
    └── → convex-file-storage
        - generateUploadUrl()
        - getUrl()
        - File metadata
```

### AI and Agents

```
Building AI features?
├── Conversational agents
│   └── → convex-agents
│       - Thread management
│       - Message history
│       - Streaming responses
│
├── Tool-using agents
│   └── → convex-agents
│       - Tool definitions
│       - Function calling
│       - Error handling
│
├── RAG (Retrieval Augmented Generation)
│   └── → convex-agents
│       - Vector embeddings
│       - Similarity search
│       - Document indexing
│
└── Workflows
    └── → convex-agents
        - Multi-step processes
        - State management
        - Progress tracking
```

### Security

```
Reviewing security?
├── Quick check (5 min)
│   └── → convex-security-check
│       - Public vs internal functions
│       - Authentication checks
│       - Input validation
│
└── Deep audit (comprehensive)
    └── → convex-security-audit
        - Authorization patterns
        - Data access controls
        - Rate limiting
```

## Available Skills

| Skill | Description | When to Use |
|-------|-------------|-------------|
| `convex-schema-validator` | Schema definition and validation | Defining tables, types, indexes |
| `convex-functions` | Queries, mutations, actions | Writing any Convex function |
| `convex-realtime` | Reactive patterns | Building real-time UIs |
| `convex-http-actions` | HTTP endpoints | Webhooks, REST APIs |
| `convex-cron-jobs` | Scheduled tasks | Background jobs, cleanup |
| `convex-file-storage` | File handling | Uploads, downloads, metadata |
| `convex-agents` | AI agents | LLMs, tools, RAG, workflows |
| `convex-migrations` | Schema evolution | Changing existing schemas |
| `convex-best-practices` | Production patterns | Code quality, optimization |
| `convex-security-check` | Quick security review | Fast security validation |
| `convex-security-audit` | Deep security review | Comprehensive audit |
| `convex-component-authoring` | Reusable components | Building shared libraries |

## Skill Locations

Skills are located in the `skills/` directory:

```
skills/
├── convex-agents/SKILL.md
├── convex-best-practices/SKILL.md
├── convex-component-authoring/SKILL.md
├── convex-cron-jobs/SKILL.md
├── convex-file-vault/SKILL.md
├── convex-functions/SKILL.md
├── convex-http-actions/SKILL.md
├── convex-migrations/SKILL.md
├── convex-realtime/SKILL.md
├── convex-schema-validator/SKILL.md
├── convex-security-audit/SKILL.md
└── convex-security-check/SKILL.md
```

## Common Patterns

### Basic CRUD

```typescript
// Schema
export default defineSchema({
  tasks: defineTable({
    title: v.string(),
    completed: v.boolean(),
    userId: v.id("users"),
  }).index("by_user", ["userId"]),
});

// Query
export const list = query({
  args: { userId: v.id("users") },
  returns: v.array(taskValidator),
  handler: async (ctx, args) => {
    return await ctx.db
      .query("tasks")
      .withIndex("by_user", (q) => q.eq("userId", args.userId))
      .collect();
  },
});

// Mutation
export const create = mutation({
  args: { title: v.string(), userId: v.id("users") },
  returns: v.id("tasks"),
  handler: async (ctx, args) => {
    return await ctx.db.insert("tasks", {
      title: args.title,
      completed: false,
      userId: args.userId,
    });
  },
});
```

### Webhook Handler

```typescript
// convex/http.ts
const http = httpRouter();

http.route({
  path: "/webhooks/stripe",
  method: "POST",
  handler: httpAction(async (ctx, request) => {
    const signature = request.headers.get("stripe-signature");
    const body = await request.text();
    
    // Verify and process
    await ctx.runMutation(internal.webhooks.processStripe, {
      signature,
      body,
    });
    
    return new Response("OK", { status: 200 });
  }),
});

export default http;
```

### Scheduled Job

```typescript
// convex/crons.ts
const crons = cronJobs();

crons.interval(
  "cleanup expired sessions",
  { hours: 1 },
  internal.sessions.cleanup,
  {}
);

export default crons;
```

## DO NOT

- Run `npx convex deploy` without explicit instruction
- Run any git commands without explicit instruction
- Edit files in `convex/_generated/`
- Use `filter()` instead of `withIndex()` on large tables
- Store secrets in code (use environment variables)
- Make public functions that should be internal

## Documentation Sources

Always fetch the latest documentation before implementing:

- **Primary**: https://docs.convex.dev/
- **LLMs.txt**: https://docs.convex.dev/llms.txt
- **Functions**: https://docs.convex.dev/functions
- **Database**: https://docs.convex.dev/database
- **Schema**: https://docs.convex.dev/database/schemas
- **Auth**: https://docs.convex.dev/auth
- **File Storage**: https://docs.convex.dev/file-storage
- **Scheduling**: https://docs.convex.dev/scheduling
- **AI/Agents**: https://docs.convex.dev/ai
- **Best Practices**: https://docs.convex.dev/understanding/best-practices/

## Update Command

To update to the latest version of convex-skills:

```
/convex --update-skill
```

This will fetch the latest skills from the repository and update your local installation.

## Installation

Install skills via npm:

```bash
npm install -g convex-skills

# Install all skills
convex-skills install-all

# Install specific skill
convex-skills install convex-functions

# List available skills
convex-skills list
```

Or install skills manually by copying from `skills/` to your project's `.claude/skills/` directory.

## References

- Convex Documentation: https://docs.convex.dev/
- Convex LLMs.txt: https://docs.convex.dev/llms.txt
- Convex GitHub: https://github.com/get-convex
- convex-skills Repository: https://github.com/get-convex/convex-skills
```

## File: `skills/avoid-feature-creep/SKILL.md`
```markdown
---
name: avoid-feature-creep
description: Prevent feature creep when building software, apps, and AI-powered products. Use this skill when planning features, reviewing scope, building MVPs, managing backlogs, or when a user says "just one more feature." Helps developers and AI agents stay focused, ship faster, and avoid bloated products.
---

# Avoid Feature Creep for Agents

Stop building features nobody needs. This skill helps you ship products that solve real problems without drowning in unnecessary complexity.

Feature creep kills products. It delays launches, burns budgets, exhausts teams, and creates software nobody wants to use. The most successful products do fewer things well.

## The Core Problem

Feature creep is the gradual accumulation of features beyond what your product needs to deliver value. It happens slowly, then all at once.

**Warning signs you're in trouble:**
- Release scope keeps growing without clear user value
- You're copying competitor features without validating need
- Stakeholders keep adding "just one more thing"
- The codebase is getting harder to maintain
- Users complain the product is confusing or bloated
- You haven't shipped in months

**What it costs:**
- Development time on features 80% of users never touch
- Increased bug surface area
- Team burnout and context switching
- Delayed time-to-market
- Technical debt that compounds
- User confusion and abandonment

## Decision Framework

Before adding ANY feature, run through this checklist:

```
1. VALIDATE THE PROBLEM
   □ Does this solve a real, validated user pain point?
   □ Have we talked to actual users about this need?
   □ What evidence supports building this?

2. CHECK ALIGNMENT
   □ Does this support the core product vision?
   □ Would this delay our current release?
   □ What are we NOT building if we build this?

3. MEASURE IMPACT
   □ How will we know if this feature succeeds?
   □ What KPIs will change?
   □ Can we quantify the value (time saved, revenue, retention)?

4. ASSESS COMPLEXITY
   □ What's the true cost (build + test + maintain + document)?
   □ Does this add dependencies or technical debt?
   □ Can we ship a simpler version first?

5. FINAL GUT CHECK
   □ Would we delay launch by a month for this feature?
   □ Is this a differentiator or just table stakes?
   □ Would removing this harm the core experience?
```

If you can't answer YES to questions 1-3 with evidence, do not build the feature.

## Scope Management Rules

**Rule 1: Define and Defend Your MVP**

Write down exactly what "done" means before you start. Document what you're NOT building. Reference this constantly.

```markdown
## MVP Scope Document Template

### Core Problem
[One sentence describing the user problem]

### Success Criteria
[How we know we've solved it]

### In Scope (v1)
- Feature A: [brief description]
- Feature B: [brief description]

### Explicitly Out of Scope
- Feature X: Deferred to v2
- Feature Y: Will not build unless [condition]
- Feature Z: Not our problem to solve

### Non-Negotiables
- Ship by [date]
- Budget: [hours/dollars]
- Core user: [specific persona]
```

**Rule 2: Use Version Control for Scope**

Treat scope like code. Track changes. Require approval for additions.

```bash
# Create a scope document and track it
git add SCOPE.md
git commit -m "Initial MVP scope definition"

# Any scope changes require explicit commits
git commit -m "SCOPE CHANGE: Added feature X - approved by [stakeholder] - impact: +2 weeks"
```

**Rule 3: The 48-Hour Rule**

When someone requests a new feature, wait 48 hours before adding it to the backlog. Most "urgent" requests feel less urgent after reflection.

**Rule 4: Budget-Based Scoping**

Every feature has a cost. When something new comes in, something else must go out.

"Yes, we can add that. Which of these three features should we cut to make room?"

## Saying No

Saying no to features is a skill. Here are templates:

**To stakeholders:**
> "That's an interesting idea. Based on our user research, it doesn't solve our core user's top three problems. Let's add it to the v2 consideration list and revisit after we validate the MVP."

**To executives:**
> "I understand the value this could bring. If we add this, we'll delay launch by [X weeks] and deprioritize [Y feature]. Here are the trade-offs - which path should we take?"

**To users:**
> "Thanks for the feedback. We're focused on [core problem] right now. I've logged this for future consideration. Can you tell me more about why this would be valuable?"

**To yourself:**
> "Is this scratching my own itch or solving a real user problem? Would I bet the release date on this?"

**To AI agents (Claude, Opus, Codex, Ralph, Cursor):**
> "Stop. Before we add this feature, answer: Does this solve the core user problem we defined at the start of this session? If not, add it to a DEFERRED.md file and stay focused on the current scope."

When working with AI coding agents:
- State your scope constraints at the start of every session
- Agents will suggest improvements. Most are out of scope.
- Treat agent suggestions like stakeholder requests: apply the 48-hour rule
- If an agent keeps pushing a feature, ask "Why?" three times to find the real need

## AI-Specific Guidelines

When building AI-powered products, feature creep has extra risks:

**AI Feature Creep Red Flags:**
- Adding AI because "everyone else is"
- Building AI summaries without validating users want them
- Multiple AI features without clear differentiation
- AI capabilities that don't connect to core user workflows

**AI Feature Discipline:**
1. One AI feature at a time
2. Validate the use case with users first
3. Measure actual usage, not just availability
4. Question: "Does the AI make the core task faster or better?"

**Before adding any AI feature, answer:**
- What specific task does this automate?
- How is this better than the non-AI alternative?
- What happens when the AI is wrong?
- Can we ship without this AI feature?

## Backlog Hygiene

A messy backlog enables feature creep. Clean it ruthlessly.

**Monthly Backlog Audit:**
```
For each item older than 30 days:
1. Has anyone asked about this since it was added?
2. Does it still align with current product vision?
3. If we never built this, would anyone notice?

If the answer to all three is "no" → Delete it.
```

**Priority Framework (MoSCoW):**
- **Must Have**: Product doesn't work without it
- **Should Have**: Important but not critical for launch
- **Could Have**: Nice but can wait
- **Won't Have**: Explicitly out of scope

Be honest: Most "Should Haves" are actually "Could Haves" in disguise.

## AI Session Discipline

**Session Start Check:**
Before coding with any AI assistant (Claude, Cursor, OpenCode), state:
- What specific feature you're building
- What's explicitly out of scope for this session
- When you'll stop and ship

**Mid-Session Check:**
Every 30-60 minutes, ask your AI:
"Are we building the right thing today, or are we adding scope?"

If the answer is "adding scope," stop. Commit what you have. Start fresh.

**Session End Check:**
Before closing an AI coding session:
- What did we actually build vs. what we planned?
- Did scope expand? Why?
- What should we defer to the next session?

**Daily AI Check:**
At the end of each day working with AI assistants:
```
1. Features completed today: [list]
2. Scope additions today: [list]  
3. Was each addition validated? [yes/no]
4. Tomorrow's focus: [single item]
```

**Sprint Planning Guard Rails:**
- No new features mid-sprint without removing something
- Capacity for bug fixes and debt paydown (20% minimum)
- Clear definition of done for each item

**Stakeholder Management:**
Create a single source of truth for scope decisions:

```markdown
## Scope Decision Log

| Date | Request | Source | Decision | Rationale | Trade-off |
|------|---------|--------|----------|-----------|-----------|
| 2025-01-15 | Add export to PDF | PM | Deferred v2 | Not core to MVP | Would delay launch 2 weeks |
| 2025-01-16 | Dark mode | User feedback | Approved | User research shows demand | Removed social sharing |
| 2025-01-17 | Add caching layer | Claude | Deferred | Premature optimization | Stay focused on core feature |
| 2025-01-17 | Refactor to hooks | Cursor | Rejected | Works fine as is | Technical scope creep |
```

**Agents as Stakeholders:**
AI coding agents are now stakeholders in your project. They have opinions. They make suggestions. Treat them like any other stakeholder:

- **Log agent suggestions** in your scope decision log with the agent name as source
- **Apply the same rigor** you would to a PM or executive request
- **Agents optimize for different things** (code quality, patterns, completeness) than you might need right now
- **"The agent suggested it" is not a valid reason** to add a feature

Common agent-driven scope creep patterns:
- "Let me also add error handling for edge cases you haven't hit yet"
- "This would be cleaner with a refactor"
- "You should probably add tests for this"
- "Let me add TypeScript types for these additional scenarios"

Each of these might be good ideas. None of them are your current scope unless you decide they are.

## Recovery: You're Already Bloated

If feature creep has already happened:

**Step 1: Audit Current Features**
- List every feature
- Check usage data for each
- Identify features with <5% engagement

**Step 2: Categorize**
- Core: Users can't accomplish their goal without it
- Supporting: Makes core better
- Peripheral: Nice but not necessary
- Bloat: Nobody uses it

**Step 3: Remove or Hide**
- Deprecate bloat with warning period
- Move peripheral features behind advanced settings
- Communicate changes clearly to users

**Step 4: Prevent Recurrence**
- Add feature creep checks to your PR/code review process
- Require usage metrics before features graduate from beta
- Build feature flags so you can easily remove experiments

## Quick Reference Commands

When reviewing any feature request, ask:

```
1. "What user problem does this solve?"
2. "What's the smallest version we could ship?"
3. "What are we NOT building to make room for this?"
4. "How will we measure success?"
5. "What happens if we never build this?"
```

If you can't answer these clearly → Do not proceed.

## The Golden Rule

**Ship something small that works. Then iterate based on real usage data.**

Users don't remember features. They remember whether your product solved their problem.

Every feature you don't build is:
- Time you get back
- Bugs you don't have to fix
- Documentation you don't have to write
- Code you don't have to maintain
- Confusion you don't add

The best products aren't the ones with the most features. They're the ones that do the right things exceptionally well.

---

*"Perfection is achieved not when there is nothing more to add, but when there is nothing left to take away."* - Antoine de Saint-Exupéry
```

## File: `skills/avoid-feature-creep/agents/openai.yaml`
```yaml
interface:
  icon_small: "./assets/small-logo.svg"
  icon_large: "./assets/large-logo.png"
```

## File: `skills/convex/SKILL.md`
```markdown
---
name: convex
displayName: Convex Development
description: Umbrella skill for all Convex development patterns. Routes to specific skills like convex-functions, convex-realtime, convex-agents, etc.
version: 1.0.0
author: Convex
tags: [convex, backend, database, realtime]
---

# Convex Development Skills

This is an index skill for Convex development. Use specific skills for detailed guidance:

## Core Development

| Skill | Command | Use When |
|-------|---------|----------|
| Functions | `/convex-functions` | Writing queries, mutations, actions |
| Schema | `/convex-schema-validator` | Defining database schemas and validators |
| Realtime | `/convex-realtime` | Building reactive subscriptions |
| HTTP Actions | `/convex-http-actions` | Webhooks and HTTP endpoints |

## Data & Storage

| Skill | Command | Use When |
|-------|---------|----------|
| File Storage | `/convex-file-storage` | File uploads, serving, storage |
| Migrations | `/convex-migrations` | Schema evolution, data backfills |

## Advanced Patterns

| Skill | Command | Use When |
|-------|---------|----------|
| Agents | `/convex-agents` | Building AI agents with tools |
| Cron Jobs | `/convex-cron-jobs` | Scheduled background tasks |
| Components | `/convex-component-authoring` | Reusable Convex packages |

## Security

| Skill | Command | Use When |
|-------|---------|----------|
| Security Check | `/convex-security-check` | Quick security audit checklist |
| Security Audit | `/convex-security-audit` | Deep security review |

## Guidelines

| Skill | Command | Use When |
|-------|---------|----------|
| Best Practices | `/convex-best-practices` | General patterns and guidelines |

## Quick Start

For most tasks:
1. Start with `/convex-best-practices` for general patterns
2. Use `/convex-functions` for writing backend logic
3. Use `/convex-schema-validator` for data modeling
4. Use specific skills as needed for your use case

## Documentation

- Primary: https://docs.convex.dev
- LLM-optimized: https://docs.convex.dev/llms.txt
```

## File: `skills/convex/agents/openai.yaml`
```yaml
interface:
  icon_small: "./assets/small-logo.svg"
  icon_large: "./assets/large-logo.png"
```

## File: `skills/convex-agents/SKILL.md`
```markdown
---
name: convex-agents
displayName: Convex Agents
description: Building AI agents with the Convex Agent component including thread management, tool integration, streaming responses, RAG patterns, and workflow orchestration
version: 1.0.0
author: Convex
tags: [convex, agents, ai, llm, tools, rag, workflows]
---

# Convex Agents

Build persistent, stateful AI agents with Convex including thread management, tool integration, streaming responses, RAG patterns, and workflow orchestration.

## Documentation Sources

Before implementing, do not assume; fetch the latest documentation:

- Primary: https://docs.convex.dev/ai
- Convex Agent Component: https://www.npmjs.com/package/@convex-dev/agent
- For broader context: https://docs.convex.dev/llms.txt

## Instructions

### Why Convex for AI Agents

- **Persistent State** - Conversation history survives restarts
- **Real-time Updates** - Stream responses to clients automatically
- **Tool Execution** - Run Convex functions as agent tools
- **Durable Workflows** - Long-running agent tasks with reliability
- **Built-in RAG** - Vector search for knowledge retrieval

### Setting Up Convex Agent

```bash
npm install @convex-dev/agent ai openai
```

```typescript
// convex/agent.ts
import { Agent } from "@convex-dev/agent";
import { components } from "./_generated/api";
import { OpenAI } from "openai";

const openai = new OpenAI();

export const agent = new Agent(components.agent, {
  chat: openai.chat,
  textEmbedding: openai.embeddings,
});
```

### Thread Management

```typescript
// convex/threads.ts
import { mutation, query } from "./_generated/server";
import { v } from "convex/values";
import { agent } from "./agent";

// Create a new conversation thread
export const createThread = mutation({
  args: {
    userId: v.id("users"),
    title: v.optional(v.string()),
  },
  returns: v.id("threads"),
  handler: async (ctx, args) => {
    const threadId = await agent.createThread(ctx, {
      userId: args.userId,
      metadata: {
        title: args.title ?? "New Conversation",
        createdAt: Date.now(),
      },
    });
    return threadId;
  },
});

// List user's threads
export const listThreads = query({
  args: { userId: v.id("users") },
  returns: v.array(v.object({
    _id: v.id("threads"),
    title: v.string(),
    lastMessageAt: v.optional(v.number()),
  })),
  handler: async (ctx, args) => {
    return await agent.listThreads(ctx, {
      userId: args.userId,
    });
  },
});

// Get thread messages
export const getMessages = query({
  args: { threadId: v.id("threads") },
  returns: v.array(v.object({
    role: v.string(),
    content: v.string(),
    createdAt: v.number(),
  })),
  handler: async (ctx, args) => {
    return await agent.getMessages(ctx, {
      threadId: args.threadId,
    });
  },
});
```

### Sending Messages and Streaming Responses

```typescript
// convex/chat.ts
import { action } from "./_generated/server";
import { v } from "convex/values";
import { agent } from "./agent";
import { internal } from "./_generated/api";

export const sendMessage = action({
  args: {
    threadId: v.id("threads"),
    message: v.string(),
  },
  returns: v.null(),
  handler: async (ctx, args) => {
    // Add user message to thread
    await ctx.runMutation(internal.chat.addUserMessage, {
      threadId: args.threadId,
      content: args.message,
    });

    // Generate AI response with streaming
    const response = await agent.chat(ctx, {
      threadId: args.threadId,
      messages: [{ role: "user", content: args.message }],
      stream: true,
      onToken: async (token) => {
        // Stream tokens to client via mutation
        await ctx.runMutation(internal.chat.appendToken, {
          threadId: args.threadId,
          token,
        });
      },
    });

    // Save complete response
    await ctx.runMutation(internal.chat.saveResponse, {
      threadId: args.threadId,
      content: response.content,
    });

    return null;
  },
});
```

### Tool Integration

Define tools that agents can use:

```typescript
// convex/tools.ts
import { tool } from "@convex-dev/agent";
import { v } from "convex/values";
import { api } from "./_generated/api";

// Tool to search knowledge base
export const searchKnowledge = tool({
  name: "search_knowledge",
  description: "Search the knowledge base for relevant information",
  parameters: v.object({
    query: v.string(),
    limit: v.optional(v.number()),
  }),
  handler: async (ctx, args) => {
    const results = await ctx.runQuery(api.knowledge.search, {
      query: args.query,
      limit: args.limit ?? 5,
    });
    return results;
  },
});

// Tool to create a task
export const createTask = tool({
  name: "create_task",
  description: "Create a new task for the user",
  parameters: v.object({
    title: v.string(),
    description: v.optional(v.string()),
    dueDate: v.optional(v.string()),
  }),
  handler: async (ctx, args) => {
    const taskId = await ctx.runMutation(api.tasks.create, {
      title: args.title,
      description: args.description,
      dueDate: args.dueDate ? new Date(args.dueDate).getTime() : undefined,
    });
    return { success: true, taskId };
  },
});

// Tool to get weather
export const getWeather = tool({
  name: "get_weather",
  description: "Get current weather for a location",
  parameters: v.object({
    location: v.string(),
  }),
  handler: async (ctx, args) => {
    const response = await fetch(
      `https://api.weather.com/current?location=${encodeURIComponent(args.location)}`
    );
    return await response.json();
  },
});
```

### Agent with Tools

```typescript
// convex/assistant.ts
import { action } from "./_generated/server";
import { v } from "convex/values";
import { agent } from "./agent";
import { searchKnowledge, createTask, getWeather } from "./tools";

export const chat = action({
  args: {
    threadId: v.id("threads"),
    message: v.string(),
  },
  returns: v.string(),
  handler: async (ctx, args) => {
    const response = await agent.chat(ctx, {
      threadId: args.threadId,
      messages: [{ role: "user", content: args.message }],
      tools: [searchKnowledge, createTask, getWeather],
      systemPrompt: `You are a helpful assistant. You have access to tools to:
        - Search the knowledge base for information
        - Create tasks for the user
        - Get weather information
        Use these tools when appropriate to help the user.`,
    });

    return response.content;
  },
});
```

### RAG (Retrieval Augmented Generation)

```typescript
// convex/knowledge.ts
import { mutation, query } from "./_generated/server";
import { v } from "convex/values";
import { agent } from "./agent";

// Add document to knowledge base
export const addDocument = mutation({
  args: {
    title: v.string(),
    content: v.string(),
    metadata: v.optional(v.object({
      source: v.optional(v.string()),
      category: v.optional(v.string()),
    })),
  },
  returns: v.id("documents"),
  handler: async (ctx, args) => {
    // Generate embedding
    const embedding = await agent.embed(ctx, args.content);

    return await ctx.db.insert("documents", {
      title: args.title,
      content: args.content,
      embedding,
      metadata: args.metadata ?? {},
      createdAt: Date.now(),
    });
  },
});

// Search knowledge base
export const search = query({
  args: {
    query: v.string(),
    limit: v.optional(v.number()),
  },
  returns: v.array(v.object({
    _id: v.id("documents"),
    title: v.string(),
    content: v.string(),
    score: v.number(),
  })),
  handler: async (ctx, args) => {
    const results = await agent.search(ctx, {
      query: args.query,
      table: "documents",
      limit: args.limit ?? 5,
    });

    return results.map((r) => ({
      _id: r._id,
      title: r.title,
      content: r.content,
      score: r._score,
    }));
  },
});
```

### Workflow Orchestration

```typescript
// convex/workflows.ts
import { action, internalMutation } from "./_generated/server";
import { v } from "convex/values";
import { agent } from "./agent";
import { internal } from "./_generated/api";

// Multi-step research workflow
export const researchTopic = action({
  args: {
    topic: v.string(),
    userId: v.id("users"),
  },
  returns: v.id("research"),
  handler: async (ctx, args) => {
    // Create research record
    const researchId = await ctx.runMutation(internal.workflows.createResearch, {
      topic: args.topic,
      userId: args.userId,
      status: "searching",
    });

    // Step 1: Search for relevant documents
    const searchResults = await agent.search(ctx, {
      query: args.topic,
      table: "documents",
      limit: 10,
    });

    await ctx.runMutation(internal.workflows.updateStatus, {
      researchId,
      status: "analyzing",
    });

    // Step 2: Analyze and synthesize
    const analysis = await agent.chat(ctx, {
      messages: [{
        role: "user",
        content: `Analyze these sources about "${args.topic}" and provide a comprehensive summary:\n\n${
          searchResults.map((r) => r.content).join("\n\n---\n\n")
        }`,
      }],
      systemPrompt: "You are a research assistant. Provide thorough, well-cited analysis.",
    });

    // Step 3: Generate key insights
    await ctx.runMutation(internal.workflows.updateStatus, {
      researchId,
      status: "summarizing",
    });

    const insights = await agent.chat(ctx, {
      messages: [{
        role: "user",
        content: `Based on this analysis, list 5 key insights:\n\n${analysis.content}`,
      }],
    });

    // Save final results
    await ctx.runMutation(internal.workflows.completeResearch, {
      researchId,
      analysis: analysis.content,
      insights: insights.content,
      sources: searchResults.map((r) => r._id),
    });

    return researchId;
  },
});
```

## Examples

### Complete Chat Application Schema

```typescript
// convex/schema.ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  threads: defineTable({
    userId: v.id("users"),
    title: v.string(),
    lastMessageAt: v.optional(v.number()),
    metadata: v.optional(v.any()),
  }).index("by_user", ["userId"]),

  messages: defineTable({
    threadId: v.id("threads"),
    role: v.union(v.literal("user"), v.literal("assistant"), v.literal("system")),
    content: v.string(),
    toolCalls: v.optional(v.array(v.object({
      name: v.string(),
      arguments: v.any(),
      result: v.optional(v.any()),
    }))),
    createdAt: v.number(),
  }).index("by_thread", ["threadId"]),

  documents: defineTable({
    title: v.string(),
    content: v.string(),
    embedding: v.array(v.float64()),
    metadata: v.object({
      source: v.optional(v.string()),
      category: v.optional(v.string()),
    }),
    createdAt: v.number(),
  }).vectorIndex("by_embedding", {
    vectorField: "embedding",
    dimensions: 1536,
  }),
});
```

### React Chat Component

```typescript
import { useQuery, useMutation, useAction } from "convex/react";
import { api } from "../convex/_generated/api";
import { useState, useRef, useEffect } from "react";

function ChatInterface({ threadId }: { threadId: Id<"threads"> }) {
  const messages = useQuery(api.threads.getMessages, { threadId });
  const sendMessage = useAction(api.chat.sendMessage);
  const [input, setInput] = useState("");
  const [sending, setSending] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSend = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || sending) return;

    const message = input.trim();
    setInput("");
    setSending(true);

    try {
      await sendMessage({ threadId, message });
    } finally {
      setSending(false);
    }
  };

  return (
    <div className="chat-container">
      <div className="messages">
        {messages?.map((msg, i) => (
          <div key={i} className={`message ${msg.role}`}>
            <strong>{msg.role === "user" ? "You" : "Assistant"}:</strong>
            <p>{msg.content}</p>
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>

      <form onSubmit={handleSend} className="input-form">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
          disabled={sending}
        />
        <button type="submit" disabled={sending || !input.trim()}>
          {sending ? "Sending..." : "Send"}
        </button>
      </form>
    </div>
  );
}
```

## Best Practices

- Never run `npx convex deploy` unless explicitly instructed
- Never run any git commands unless explicitly instructed
- Store conversation history in Convex for persistence
- Use streaming for better user experience with long responses
- Implement proper error handling for tool failures
- Use vector indexes for efficient RAG retrieval
- Rate limit agent interactions to control costs
- Log tool usage for debugging and analytics

## Common Pitfalls

1. **Not persisting threads** - Conversations lost on refresh
2. **Blocking on long responses** - Use streaming instead
3. **Tool errors crashing agents** - Add proper error handling
4. **Large context windows** - Summarize old messages
5. **Missing embeddings for RAG** - Generate embeddings on insert

## References

- Convex Documentation: https://docs.convex.dev/
- Convex LLMs.txt: https://docs.convex.dev/llms.txt
- Convex AI: https://docs.convex.dev/ai
- Agent Component: https://www.npmjs.com/package/@convex-dev/agent
```

## File: `skills/convex-agents/agents/openai.yaml`
```yaml
interface:
  icon_small: "./assets/small-logo.svg"
  icon_large: "./assets/large-logo.png"
```

## File: `skills/convex-best-practices/SKILL.md`
```markdown
---
name: convex-best-practices
description: Guidelines for building production-ready Convex apps covering function organization, query patterns, validation, TypeScript usage, error handling, and the Zen of Convex design philosophy
---

# Convex Best Practices

Build production-ready Convex applications by following established patterns for function organization, query optimization, validation, TypeScript usage, and error handling.

## Code Quality

All patterns in this skill comply with `@convex-dev/eslint-plugin`. Install it for build-time validation:

```bash
npm i @convex-dev/eslint-plugin --save-dev
```

```js
// eslint.config.js
import { defineConfig } from "eslint/config";
import convexPlugin from "@convex-dev/eslint-plugin";

export default defineConfig([
  ...convexPlugin.configs.recommended,
]);
```

The plugin enforces four rules:

| Rule                                | What it enforces                  |
| ----------------------------------- | --------------------------------- |
| `no-old-registered-function-syntax` | Object syntax with `handler`      |
| `require-argument-validators`       | `args: {}` on all functions       |
| `explicit-table-ids`                | Table name in db operations       |
| `import-wrong-runtime`              | No Node imports in Convex runtime |

Docs: https://docs.convex.dev/eslint

## Documentation Sources

Before implementing, do not assume; fetch the latest documentation:

- Primary: https://docs.convex.dev/understanding/best-practices/
- Error Handling: https://docs.convex.dev/functions/error-handling
- Write Conflicts: https://docs.convex.dev/error#1
- For broader context: https://docs.convex.dev/llms.txt

## Instructions

### The Zen of Convex

1. **Convex manages the hard parts** - Let Convex handle caching, real-time sync, and consistency
2. **Functions are the API** - Design your functions as your application's interface
3. **Schema is truth** - Define your data model explicitly in schema.ts
4. **TypeScript everywhere** - Leverage end-to-end type safety
5. **Queries are reactive** - Think in terms of subscriptions, not requests

### Function Organization

Organize your Convex functions by domain:

```typescript
// convex/users.ts - User-related functions
import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

export const get = query({
  args: { userId: v.id("users") },
  returns: v.union(
    v.object({
      _id: v.id("users"),
      _creationTime: v.number(),
      name: v.string(),
      email: v.string(),
    }),
    v.null(),
  ),
  handler: async (ctx, args) => {
    return await ctx.db.get("users", args.userId);
  },
});
```

### Argument and Return Validation

Always define validators for arguments AND return types:

```typescript
export const createTask = mutation({
  args: {
    title: v.string(),
    description: v.optional(v.string()),
    priority: v.union(v.literal("low"), v.literal("medium"), v.literal("high")),
  },
  returns: v.id("tasks"),
  handler: async (ctx, args) => {
    return await ctx.db.insert("tasks", {
      title: args.title,
      description: args.description,
      priority: args.priority,
      completed: false,
      createdAt: Date.now(),
    });
  },
});
```

### Query Patterns

Use indexes instead of filters for efficient queries:

```typescript
// Schema with index
export default defineSchema({
  tasks: defineTable({
    userId: v.id("users"),
    status: v.string(),
    createdAt: v.number(),
  })
    .index("by_user", ["userId"])
    .index("by_user_and_status", ["userId", "status"]),
});

// Query using index
export const getTasksByUser = query({
  args: { userId: v.id("users") },
  returns: v.array(
    v.object({
      _id: v.id("tasks"),
      _creationTime: v.number(),
      userId: v.id("users"),
      status: v.string(),
      createdAt: v.number(),
    }),
  ),
  handler: async (ctx, args) => {
    return await ctx.db
      .query("tasks")
      .withIndex("by_user", (q) => q.eq("userId", args.userId))
      .order("desc")
      .collect();
  },
});
```

### Error Handling

Use ConvexError for user-facing errors:

```typescript
import { ConvexError } from "convex/values";

export const updateTask = mutation({
  args: {
    taskId: v.id("tasks"),
    title: v.string(),
  },
  returns: v.null(),
  handler: async (ctx, args) => {
    const task = await ctx.db.get("tasks", args.taskId);

    if (!task) {
      throw new ConvexError({
        code: "NOT_FOUND",
        message: "Task not found",
      });
    }

    await ctx.db.patch("tasks", args.taskId, { title: args.title });
    return null;
  },
});
```

### Avoiding Write Conflicts (Optimistic Concurrency Control)

Convex uses OCC. Follow these patterns to minimize conflicts:

```typescript
// GOOD: Make mutations idempotent
export const completeTask = mutation({
  args: { taskId: v.id("tasks") },
  returns: v.null(),
  handler: async (ctx, args) => {
    const task = await ctx.db.get("tasks", args.taskId);

    // Early return if already complete (idempotent)
    if (!task || task.status === "completed") {
      return null;
    }

    await ctx.db.patch("tasks", args.taskId, {
      status: "completed",
      completedAt: Date.now(),
    });
    return null;
  },
});

// GOOD: Patch directly without reading first when possible
export const updateNote = mutation({
  args: { id: v.id("notes"), content: v.string() },
  returns: v.null(),
  handler: async (ctx, args) => {
    // Patch directly - ctx.db.patch throws if document doesn't exist
    await ctx.db.patch("notes", args.id, { content: args.content });
    return null;
  },
});

// GOOD: Use Promise.all for parallel independent updates
export const reorderItems = mutation({
  args: { itemIds: v.array(v.id("items")) },
  returns: v.null(),
  handler: async (ctx, args) => {
    const updates = args.itemIds.map((id, index) =>
      ctx.db.patch("items", id, { order: index }),
    );
    await Promise.all(updates);
    return null;
  },
});
```

### TypeScript Best Practices

```typescript
import { Id, Doc } from "./_generated/dataModel";

// Use Id type for document references
type UserId = Id<"users">;

// Use Doc type for full documents
type User = Doc<"users">;

// Define Record types properly
const userScores: Record<Id<"users">, number> = {};
```

### Internal vs Public Functions

```typescript
// Public function - exposed to clients
export const getUser = query({
  args: { userId: v.id("users") },
  returns: v.union(
    v.null(),
    v.object({
      /* ... */
    }),
  ),
  handler: async (ctx, args) => {
    // ...
  },
});

// Internal function - only callable from other Convex functions
export const _updateUserStats = internalMutation({
  args: { userId: v.id("users") },
  returns: v.null(),
  handler: async (ctx, args) => {
    // ...
  },
});
```

## Examples

### Complete CRUD Pattern

```typescript
// convex/tasks.ts
import { query, mutation } from "./_generated/server";
import { v } from "convex/values";
import { ConvexError } from "convex/values";

const taskValidator = v.object({
  _id: v.id("tasks"),
  _creationTime: v.number(),
  title: v.string(),
  completed: v.boolean(),
  userId: v.id("users"),
});

export const list = query({
  args: { userId: v.id("users") },
  returns: v.array(taskValidator),
  handler: async (ctx, args) => {
    return await ctx.db
      .query("tasks")
      .withIndex("by_user", (q) => q.eq("userId", args.userId))
      .collect();
  },
});

export const create = mutation({
  args: {
    title: v.string(),
    userId: v.id("users"),
  },
  returns: v.id("tasks"),
  handler: async (ctx, args) => {
    return await ctx.db.insert("tasks", {
      title: args.title,
      completed: false,
      userId: args.userId,
    });
  },
});

export const update = mutation({
  args: {
    taskId: v.id("tasks"),
    title: v.optional(v.string()),
    completed: v.optional(v.boolean()),
  },
  returns: v.null(),
  handler: async (ctx, args) => {
    const { taskId, ...updates } = args;

    // Remove undefined values
    const cleanUpdates = Object.fromEntries(
      Object.entries(updates).filter(([_, v]) => v !== undefined),
    );

    if (Object.keys(cleanUpdates).length > 0) {
      await ctx.db.patch("tasks", taskId, cleanUpdates);
    }
    return null;
  },
});

export const remove = mutation({
  args: { taskId: v.id("tasks") },
  returns: v.null(),
  handler: async (ctx, args) => {
    await ctx.db.delete("tasks", args.taskId);
    return null;
  },
});
```

## Best Practices

- Never run `npx convex deploy` unless explicitly instructed
- Never run any git commands unless explicitly instructed
- Always define return validators for functions
- Use indexes for all queries that filter data
- Make mutations idempotent to handle retries gracefully
- Use ConvexError for user-facing error messages
- Organize functions by domain (users.ts, tasks.ts, etc.)
- Use internal functions for sensitive operations
- Leverage TypeScript's Id and Doc types

## Common Pitfalls

1. **Using filter instead of withIndex** - Always define indexes and use withIndex
2. **Missing return validators** - Always specify the returns field
3. **Non-idempotent mutations** - Check current state before updating
4. **Reading before patching unnecessarily** - Patch directly when possible
5. **Not handling null returns** - Document IDs might not exist

## References

- Convex Documentation: https://docs.convex.dev/
- Convex LLMs.txt: https://docs.convex.dev/llms.txt
- Best Practices: https://docs.convex.dev/understanding/best-practices/
- Error Handling: https://docs.convex.dev/functions/error-handling
- Write Conflicts: https://docs.convex.dev/error#1
```

## File: `skills/convex-best-practices/agents/openai.yaml`
```yaml
interface:
  icon_small: "./assets/small-logo.svg"
  icon_large: "./assets/large-logo.png"
```

## File: `skills/convex-component-authoring/SKILL.md`
```markdown
---
name: convex-component-authoring
displayName: Convex Component Authoring
description: How to create, structure, and publish self-contained Convex components with proper isolation, exports, and dependency management
version: 1.0.0
author: Convex
tags: [convex, components, reusable, packages, npm]
---

# Convex Component Authoring

Create self-contained, reusable Convex components with proper isolation, exports, and dependency management for sharing across projects.

## Documentation Sources

Before implementing, do not assume; fetch the latest documentation:

- Primary: https://docs.convex.dev/components
- Component Authoring: https://docs.convex.dev/components/authoring
- For broader context: https://docs.convex.dev/llms.txt

## Instructions

### What Are Convex Components?

Convex components are self-contained packages that include:
- Database tables (isolated from the main app)
- Functions (queries, mutations, actions)
- TypeScript types and validators
- Optional frontend hooks

### Component Structure

```
my-convex-component/
├── package.json
├── tsconfig.json
├── README.md
├── src/
│   ├── index.ts           # Main exports
│   ├── component.ts       # Component definition
│   ├── schema.ts          # Component schema
│   └── functions/
│       ├── queries.ts
│       ├── mutations.ts
│       └── actions.ts
└── convex.config.ts       # Component configuration
```

### Creating a Component

#### 1. Component Configuration

```typescript
// convex.config.ts
import { defineComponent } from "convex/server";

export default defineComponent("myComponent");
```

#### 2. Component Schema

```typescript
// src/schema.ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  // Tables are isolated to this component
  items: defineTable({
    name: v.string(),
    data: v.any(),
    createdAt: v.number(),
  }).index("by_name", ["name"]),
  
  config: defineTable({
    key: v.string(),
    value: v.any(),
  }).index("by_key", ["key"]),
});
```

#### 3. Component Definition

```typescript
// src/component.ts
import { defineComponent, ComponentDefinition } from "convex/server";
import schema from "./schema";
import * as queries from "./functions/queries";
import * as mutations from "./functions/mutations";

const component = defineComponent("myComponent", {
  schema,
  functions: {
    ...queries,
    ...mutations,
  },
});

export default component;
```

#### 4. Component Functions

```typescript
// src/functions/queries.ts
import { query } from "../_generated/server";
import { v } from "convex/values";

export const list = query({
  args: {
    limit: v.optional(v.number()),
  },
  returns: v.array(v.object({
    _id: v.id("items"),
    name: v.string(),
    data: v.any(),
    createdAt: v.number(),
  })),
  handler: async (ctx, args) => {
    return await ctx.db
      .query("items")
      .order("desc")
      .take(args.limit ?? 10);
  },
});

export const get = query({
  args: { name: v.string() },
  returns: v.union(v.object({
    _id: v.id("items"),
    name: v.string(),
    data: v.any(),
  }), v.null()),
  handler: async (ctx, args) => {
    return await ctx.db
      .query("items")
      .withIndex("by_name", (q) => q.eq("name", args.name))
      .unique();
  },
});
```

```typescript
// src/functions/mutations.ts
import { mutation } from "../_generated/server";
import { v } from "convex/values";

export const create = mutation({
  args: {
    name: v.string(),
    data: v.any(),
  },
  returns: v.id("items"),
  handler: async (ctx, args) => {
    return await ctx.db.insert("items", {
      name: args.name,
      data: args.data,
      createdAt: Date.now(),
    });
  },
});

export const update = mutation({
  args: {
    id: v.id("items"),
    data: v.any(),
  },
  returns: v.null(),
  handler: async (ctx, args) => {
    await ctx.db.patch(args.id, { data: args.data });
    return null;
  },
});

export const remove = mutation({
  args: { id: v.id("items") },
  returns: v.null(),
  handler: async (ctx, args) => {
    await ctx.db.delete(args.id);
    return null;
  },
});
```

#### 5. Main Exports

```typescript
// src/index.ts
export { default as component } from "./component";
export * from "./functions/queries";
export * from "./functions/mutations";

// Export types for consumers
export type { Id } from "./_generated/dataModel";
```

### Using a Component

```typescript
// In the consuming app's convex/convex.config.ts
import { defineApp } from "convex/server";
import myComponent from "my-convex-component";

const app = defineApp();

app.use(myComponent, { name: "myComponent" });

export default app;
```

```typescript
// In the consuming app's code
import { useQuery, useMutation } from "convex/react";
import { api } from "../convex/_generated/api";

function MyApp() {
  // Access component functions through the app's API
  const items = useQuery(api.myComponent.list, { limit: 10 });
  const createItem = useMutation(api.myComponent.create);
  
  return (
    <div>
      {items?.map((item) => (
        <div key={item._id}>{item.name}</div>
      ))}
      <button onClick={() => createItem({ name: "New", data: {} })}>
        Add Item
      </button>
    </div>
  );
}
```

### Component Configuration Options

```typescript
// convex/convex.config.ts
import { defineApp } from "convex/server";
import myComponent from "my-convex-component";

const app = defineApp();

// Basic usage
app.use(myComponent);

// With custom name
app.use(myComponent, { name: "customName" });

// Multiple instances
app.use(myComponent, { name: "instance1" });
app.use(myComponent, { name: "instance2" });

export default app;
```

### Providing Component Hooks

```typescript
// src/hooks.ts
import { useQuery, useMutation } from "convex/react";
import { FunctionReference } from "convex/server";

// Type-safe hooks for component consumers
export function useMyComponent(api: {
  list: FunctionReference<"query">;
  create: FunctionReference<"mutation">;
}) {
  const items = useQuery(api.list, {});
  const createItem = useMutation(api.create);
  
  return {
    items,
    createItem,
    isLoading: items === undefined,
  };
}
```

### Publishing a Component

#### package.json

```json
{
  "name": "my-convex-component",
  "version": "1.0.0",
  "description": "A reusable Convex component",
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "files": [
    "dist",
    "convex.config.ts"
  ],
  "scripts": {
    "build": "tsc",
    "prepublishOnly": "npm run build"
  },
  "peerDependencies": {
    "convex": "^1.0.0"
  },
  "devDependencies": {
    "convex": "^1.17.0",
    "typescript": "^5.0.0"
  },
  "keywords": [
    "convex",
    "component"
  ]
}
```

#### tsconfig.json

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "declaration": true,
    "outDir": "dist",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

## Examples

### Rate Limiter Component

```typescript
// rate-limiter/src/schema.ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  requests: defineTable({
    key: v.string(),
    timestamp: v.number(),
  })
    .index("by_key", ["key"])
    .index("by_key_and_time", ["key", "timestamp"]),
});
```

```typescript
// rate-limiter/src/functions/mutations.ts
import { mutation } from "../_generated/server";
import { v } from "convex/values";

export const checkLimit = mutation({
  args: {
    key: v.string(),
    limit: v.number(),
    windowMs: v.number(),
  },
  returns: v.object({
    allowed: v.boolean(),
    remaining: v.number(),
    resetAt: v.number(),
  }),
  handler: async (ctx, args) => {
    const now = Date.now();
    const windowStart = now - args.windowMs;
    
    // Clean old entries
    const oldEntries = await ctx.db
      .query("requests")
      .withIndex("by_key_and_time", (q) => 
        q.eq("key", args.key).lt("timestamp", windowStart)
      )
      .collect();
    
    for (const entry of oldEntries) {
      await ctx.db.delete(entry._id);
    }
    
    // Count current window
    const currentRequests = await ctx.db
      .query("requests")
      .withIndex("by_key", (q) => q.eq("key", args.key))
      .collect();
    
    const remaining = Math.max(0, args.limit - currentRequests.length);
    const allowed = remaining > 0;
    
    if (allowed) {
      await ctx.db.insert("requests", {
        key: args.key,
        timestamp: now,
      });
    }
    
    const oldestRequest = currentRequests[0];
    const resetAt = oldestRequest 
      ? oldestRequest.timestamp + args.windowMs 
      : now + args.windowMs;
    
    return { allowed, remaining: remaining - (allowed ? 1 : 0), resetAt };
  },
});
```

```typescript
// Usage in consuming app
import { useMutation } from "convex/react";
import { api } from "../convex/_generated/api";

function useRateLimitedAction() {
  const checkLimit = useMutation(api.rateLimiter.checkLimit);
  
  return async (action: () => Promise<void>) => {
    const result = await checkLimit({
      key: "user-action",
      limit: 10,
      windowMs: 60000,
    });
    
    if (!result.allowed) {
      throw new Error(`Rate limited. Try again at ${new Date(result.resetAt)}`);
    }
    
    await action();
  };
}
```

## Best Practices

- Never run `npx convex deploy` unless explicitly instructed
- Never run any git commands unless explicitly instructed
- Keep component tables isolated (don't reference main app tables)
- Export clear TypeScript types for consumers
- Document all public functions and their arguments
- Use semantic versioning for component releases
- Include comprehensive README with examples
- Test components in isolation before publishing

## Common Pitfalls

1. **Cross-referencing tables** - Component tables should be self-contained
2. **Missing type exports** - Export all necessary types
3. **Hardcoded configuration** - Use component options for customization
4. **No versioning** - Follow semantic versioning
5. **Poor documentation** - Document all public APIs

## References

- Convex Documentation: https://docs.convex.dev/
- Convex LLMs.txt: https://docs.convex.dev/llms.txt
- Components: https://docs.convex.dev/components
- Component Authoring: https://docs.convex.dev/components/authoring
```

## File: `skills/convex-component-authoring/agents/openai.yaml`
```yaml
interface:
  icon_small: "./assets/small-logo.svg"
  icon_large: "./assets/large-logo.png"
```

## File: `skills/convex-cron-jobs/SKILL.md`
```markdown
---
name: convex-cron-jobs
displayName: Convex Cron Jobs
description: Scheduled function patterns for background tasks including interval scheduling, cron expressions, job monitoring, retry strategies, and best practices for long-running tasks
version: 1.0.0
author: Convex
tags: [convex, cron, scheduling, background-jobs, automation]
---

# Convex Cron Jobs

Schedule recurring functions for background tasks, cleanup jobs, data syncing, and automated workflows in Convex applications.

## Documentation Sources

Before implementing, do not assume; fetch the latest documentation:

- Primary: https://docs.convex.dev/scheduling/cron-jobs
- Scheduling Overview: https://docs.convex.dev/scheduling
- Scheduled Functions: https://docs.convex.dev/scheduling/scheduled-functions
- For broader context: https://docs.convex.dev/llms.txt

## Instructions

### Cron Jobs Overview

Convex cron jobs allow you to schedule functions to run at regular intervals or specific times. Key features:

- Run functions on a fixed schedule
- Support for interval-based and cron expression scheduling
- Automatic retries on failure
- Monitoring via the Convex dashboard

### Basic Cron Setup

```typescript
// convex/crons.ts
import { cronJobs } from "convex/server";
import { internal } from "./_generated/api";

const crons = cronJobs();

// Run every hour
crons.interval(
  "cleanup expired sessions",
  { hours: 1 },
  internal.tasks.cleanupExpiredSessions,
  {}
);

// Run every day at midnight UTC
crons.cron(
  "daily report",
  "0 0 * * *",
  internal.reports.generateDailyReport,
  {}
);

export default crons;
```

### Interval-Based Scheduling

Use `crons.interval` for simple recurring tasks:

```typescript
// convex/crons.ts
import { cronJobs } from "convex/server";
import { internal } from "./_generated/api";

const crons = cronJobs();

// Every 5 minutes
crons.interval(
  "sync external data",
  { minutes: 5 },
  internal.sync.fetchExternalData,
  {}
);

// Every 2 hours
crons.interval(
  "cleanup temp files",
  { hours: 2 },
  internal.files.cleanupTempFiles,
  {}
);

// Every 30 seconds (minimum interval)
crons.interval(
  "health check",
  { seconds: 30 },
  internal.monitoring.healthCheck,
  {}
);

export default crons;
```

### Cron Expression Scheduling

Use `crons.cron` for precise scheduling with cron expressions:

```typescript
// convex/crons.ts
import { cronJobs } from "convex/server";
import { internal } from "./_generated/api";

const crons = cronJobs();

// Every day at 9 AM UTC
crons.cron(
  "morning notifications",
  "0 9 * * *",
  internal.notifications.sendMorningDigest,
  {}
);

// Every Monday at 8 AM UTC
crons.cron(
  "weekly summary",
  "0 8 * * 1",
  internal.reports.generateWeeklySummary,
  {}
);

// First day of every month at midnight
crons.cron(
  "monthly billing",
  "0 0 1 * *",
  internal.billing.processMonthlyBilling,
  {}
);

// Every 15 minutes
crons.cron(
  "frequent sync",
  "*/15 * * * *",
  internal.sync.syncData,
  {}
);

export default crons;
```

### Cron Expression Reference

```
┌───────────── minute (0-59)
│ ┌───────────── hour (0-23)
│ │ ┌───────────── day of month (1-31)
│ │ │ ┌───────────── month (1-12)
│ │ │ │ ┌───────────── day of week (0-6, Sunday=0)
│ │ │ │ │
* * * * *
```

Common patterns:
- `* * * * *` - Every minute
- `0 * * * *` - Every hour
- `0 0 * * *` - Every day at midnight
- `0 0 * * 0` - Every Sunday at midnight
- `0 0 1 * *` - First day of every month
- `*/5 * * * *` - Every 5 minutes
- `0 9-17 * * 1-5` - Every hour from 9 AM to 5 PM, Monday through Friday

### Internal Functions for Crons

Cron jobs should call internal functions for security:

```typescript
// convex/tasks.ts
import { internalMutation, internalQuery } from "./_generated/server";
import { v } from "convex/values";

// Cleanup expired sessions
export const cleanupExpiredSessions = internalMutation({
  args: {},
  returns: v.number(),
  handler: async (ctx) => {
    const oneHourAgo = Date.now() - 60 * 60 * 1000;
    
    const expiredSessions = await ctx.db
      .query("sessions")
      .withIndex("by_lastActive")
      .filter((q) => q.lt(q.field("lastActive"), oneHourAgo))
      .collect();

    for (const session of expiredSessions) {
      await ctx.db.delete(session._id);
    }

    return expiredSessions.length;
  },
});

// Process pending tasks
export const processPendingTasks = internalMutation({
  args: {},
  returns: v.null(),
  handler: async (ctx) => {
    const pendingTasks = await ctx.db
      .query("tasks")
      .withIndex("by_status", (q) => q.eq("status", "pending"))
      .take(100);

    for (const task of pendingTasks) {
      await ctx.db.patch(task._id, {
        status: "processing",
        startedAt: Date.now(),
      });
      
      // Schedule the actual processing
      await ctx.scheduler.runAfter(0, internal.tasks.processTask, {
        taskId: task._id,
      });
    }

    return null;
  },
});
```

### Cron Jobs with Arguments

Pass static arguments to cron jobs:

```typescript
// convex/crons.ts
import { cronJobs } from "convex/server";
import { internal } from "./_generated/api";

const crons = cronJobs();

// Different cleanup intervals for different types
crons.interval(
  "cleanup temp files",
  { hours: 1 },
  internal.cleanup.cleanupByType,
  { fileType: "temp", maxAge: 3600000 }
);

crons.interval(
  "cleanup cache files",
  { hours: 24 },
  internal.cleanup.cleanupByType,
  { fileType: "cache", maxAge: 86400000 }
);

export default crons;
```

```typescript
// convex/cleanup.ts
import { internalMutation } from "./_generated/server";
import { v } from "convex/values";

export const cleanupByType = internalMutation({
  args: {
    fileType: v.string(),
    maxAge: v.number(),
  },
  returns: v.number(),
  handler: async (ctx, args) => {
    const cutoff = Date.now() - args.maxAge;
    
    const oldFiles = await ctx.db
      .query("files")
      .withIndex("by_type_and_created", (q) => 
        q.eq("type", args.fileType).lt("createdAt", cutoff)
      )
      .collect();

    for (const file of oldFiles) {
      await ctx.storage.delete(file.storageId);
      await ctx.db.delete(file._id);
    }

    return oldFiles.length;
  },
});
```

### Monitoring and Logging

Add logging to track cron job execution:

```typescript
// convex/tasks.ts
import { internalMutation } from "./_generated/server";
import { v } from "convex/values";

export const cleanupWithLogging = internalMutation({
  args: {},
  returns: v.null(),
  handler: async (ctx) => {
    const startTime = Date.now();
    let processedCount = 0;
    let errorCount = 0;

    try {
      const expiredItems = await ctx.db
        .query("items")
        .withIndex("by_expiresAt")
        .filter((q) => q.lt(q.field("expiresAt"), Date.now()))
        .collect();

      for (const item of expiredItems) {
        try {
          await ctx.db.delete(item._id);
          processedCount++;
        } catch (error) {
          errorCount++;
          console.error(`Failed to delete item ${item._id}:`, error);
        }
      }

      // Log job completion
      await ctx.db.insert("cronLogs", {
        jobName: "cleanup",
        startTime,
        endTime: Date.now(),
        duration: Date.now() - startTime,
        processedCount,
        errorCount,
        status: errorCount === 0 ? "success" : "partial",
      });
    } catch (error) {
      // Log job failure
      await ctx.db.insert("cronLogs", {
        jobName: "cleanup",
        startTime,
        endTime: Date.now(),
        duration: Date.now() - startTime,
        processedCount,
        errorCount,
        status: "failed",
        error: String(error),
      });
      throw error;
    }

    return null;
  },
});
```

### Batching for Large Datasets

Handle large datasets in batches to avoid timeouts:

```typescript
// convex/tasks.ts
import { internalMutation } from "./_generated/server";
import { internal } from "./_generated/api";
import { v } from "convex/values";

const BATCH_SIZE = 100;

export const processBatch = internalMutation({
  args: {
    cursor: v.optional(v.string()),
  },
  returns: v.null(),
  handler: async (ctx, args) => {
    const result = await ctx.db
      .query("items")
      .withIndex("by_status", (q) => q.eq("status", "pending"))
      .paginate({ numItems: BATCH_SIZE, cursor: args.cursor ?? null });

    for (const item of result.page) {
      await ctx.db.patch(item._id, {
        status: "processed",
        processedAt: Date.now(),
      });
    }

    // Schedule next batch if there are more items
    if (!result.isDone) {
      await ctx.scheduler.runAfter(0, internal.tasks.processBatch, {
        cursor: result.continueCursor,
      });
    }

    return null;
  },
});
```

### External API Calls in Crons

Use actions for external API calls:

```typescript
// convex/sync.ts
"use node";

import { internalAction } from "./_generated/server";
import { internal } from "./_generated/api";
import { v } from "convex/values";

export const syncExternalData = internalAction({
  args: {},
  returns: v.null(),
  handler: async (ctx) => {
    // Fetch from external API
    const response = await fetch("https://api.example.com/data", {
      headers: {
        Authorization: `Bearer ${process.env.API_KEY}`,
      },
    });

    if (!response.ok) {
      throw new Error(`API request failed: ${response.status}`);
    }

    const data = await response.json();

    // Store the data using a mutation
    await ctx.runMutation(internal.sync.storeExternalData, {
      data,
      syncedAt: Date.now(),
    });

    return null;
  },
});

export const storeExternalData = internalMutation({
  args: {
    data: v.any(),
    syncedAt: v.number(),
  },
  returns: v.null(),
  handler: async (ctx, args) => {
    await ctx.db.insert("externalData", {
      data: args.data,
      syncedAt: args.syncedAt,
    });
    return null;
  },
});
```

```typescript
// convex/crons.ts
import { cronJobs } from "convex/server";
import { internal } from "./_generated/api";

const crons = cronJobs();

crons.interval(
  "sync external data",
  { minutes: 15 },
  internal.sync.syncExternalData,
  {}
);

export default crons;
```

## Examples

### Schema for Cron Job Logging

```typescript
// convex/schema.ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  cronLogs: defineTable({
    jobName: v.string(),
    startTime: v.number(),
    endTime: v.number(),
    duration: v.number(),
    processedCount: v.number(),
    errorCount: v.number(),
    status: v.union(
      v.literal("success"),
      v.literal("partial"),
      v.literal("failed")
    ),
    error: v.optional(v.string()),
  })
    .index("by_job", ["jobName"])
    .index("by_status", ["status"])
    .index("by_startTime", ["startTime"]),

  sessions: defineTable({
    userId: v.id("users"),
    token: v.string(),
    lastActive: v.number(),
    expiresAt: v.number(),
  })
    .index("by_user", ["userId"])
    .index("by_lastActive", ["lastActive"])
    .index("by_expiresAt", ["expiresAt"]),

  tasks: defineTable({
    type: v.string(),
    status: v.union(
      v.literal("pending"),
      v.literal("processing"),
      v.literal("completed"),
      v.literal("failed")
    ),
    data: v.any(),
    createdAt: v.number(),
    startedAt: v.optional(v.number()),
    completedAt: v.optional(v.number()),
  })
    .index("by_status", ["status"])
    .index("by_type_and_status", ["type", "status"]),
});
```

### Complete Cron Configuration Example

```typescript
// convex/crons.ts
import { cronJobs } from "convex/server";
import { internal } from "./_generated/api";

const crons = cronJobs();

// Cleanup jobs
crons.interval(
  "cleanup expired sessions",
  { hours: 1 },
  internal.cleanup.expiredSessions,
  {}
);

crons.interval(
  "cleanup old logs",
  { hours: 24 },
  internal.cleanup.oldLogs,
  { maxAgeDays: 30 }
);

// Sync jobs
crons.interval(
  "sync user data",
  { minutes: 15 },
  internal.sync.userData,
  {}
);

// Report jobs
crons.cron(
  "daily analytics",
  "0 1 * * *",
  internal.reports.dailyAnalytics,
  {}
);

crons.cron(
  "weekly summary",
  "0 9 * * 1",
  internal.reports.weeklySummary,
  {}
);

// Health checks
crons.interval(
  "service health check",
  { minutes: 5 },
  internal.monitoring.healthCheck,
  {}
);

export default crons;
```

## Best Practices

- Never run `npx convex deploy` unless explicitly instructed
- Never run any git commands unless explicitly instructed
- Only use `crons.interval` or `crons.cron` methods, not deprecated helpers
- Always call internal functions from cron jobs for security
- Import `internal` from `_generated/api` even for functions in the same file
- Add logging and monitoring for production cron jobs
- Use batching for operations that process large datasets
- Handle errors gracefully to prevent job failures
- Use meaningful job names for dashboard visibility
- Consider timezone when using cron expressions (Convex uses UTC)

## Common Pitfalls

1. **Using public functions** - Cron jobs should call internal functions only
2. **Long-running mutations** - Break large operations into batches
3. **Missing error handling** - Unhandled errors will fail the entire job
4. **Forgetting timezone** - All cron expressions use UTC
5. **Using deprecated helpers** - Avoid `crons.hourly`, `crons.daily`, etc.
6. **Not logging execution** - Makes debugging production issues difficult

## References

- Convex Documentation: https://docs.convex.dev/
- Convex LLMs.txt: https://docs.convex.dev/llms.txt
- Cron Jobs: https://docs.convex.dev/scheduling/cron-jobs
- Scheduling Overview: https://docs.convex.dev/scheduling
- Scheduled Functions: https://docs.convex.dev/scheduling/scheduled-functions
```

## File: `skills/convex-cron-jobs/agents/openai.yaml`
```yaml
interface:
  icon_small: "./assets/small-logo.svg"
  icon_large: "./assets/large-logo.png"
```

## File: `skills/convex-file-vault/SKILL.md`
```markdown
---
name: convex-file-storage
displayName: Convex File Storage
description: Complete file handling including upload flows, serving files via URL, storing generated files from actions, deletion, and accessing file metadata from system tables
version: 1.0.0
author: Convex
tags: [convex, file-storage, uploads, images, files]
---

# Convex File Storage

Handle file uploads, storage, serving, and management in Convex applications with proper patterns for images, documents, and generated files.

## Documentation Sources

Before implementing, do not assume; fetch the latest documentation:

- Primary: https://docs.convex.dev/file-storage
- Upload Files: https://docs.convex.dev/file-vault/upload-files
- Serve Files: https://docs.convex.dev/file-vault/serve-files
- For broader context: https://docs.convex.dev/llms.txt

## Instructions

### File Storage Overview

Convex provides built-in file storage with:
- Automatic URL generation for serving files
- Support for any file type (images, PDFs, videos, etc.)
- File metadata via the `_storage` system table
- Integration with mutations and actions

### Generating Upload URLs

```typescript
// convex/files.ts
import { mutation } from "./_generated/server";
import { v } from "convex/values";

export const generateUploadUrl = mutation({
  args: {},
  returns: v.string(),
  handler: async (ctx) => {
    return await ctx.storage.generateUploadUrl();
  },
});
```

### Client-Side Upload

```typescript
// React component
import { useMutation } from "convex/react";
import { api } from "../convex/_generated/api";
import { useState } from "react";

function FileUploader() {
  const generateUploadUrl = useMutation(api.files.generateUploadUrl);
  const saveFile = useMutation(api.files.saveFile);
  const [uploading, setUploading] = useState(false);

  const handleUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    setUploading(true);
    try {
      // Step 1: Get upload URL
      const uploadUrl = await generateUploadUrl();

      // Step 2: Upload file to storage
      const result = await fetch(uploadUrl, {
        method: "POST",
        headers: { "Content-Type": file.type },
        body: file,
      });

      const { storageId } = await result.json();

      // Step 3: Save file reference to database
      await saveFile({
        storageId,
        fileName: file.name,
        fileType: file.type,
        fileSize: file.size,
      });
    } finally {
      setUploading(false);
    }
  };

  return (
    <div>
      <input
        type="file"
        onChange={handleUpload}
        disabled={uploading}
      />
      {uploading && <p>Uploading...</p>}
    </div>
  );
}
```

### Saving File References

```typescript
// convex/files.ts
import { mutation, query } from "./_generated/server";
import { v } from "convex/values";

export const saveFile = mutation({
  args: {
    storageId: v.id("_storage"),
    fileName: v.string(),
    fileType: v.string(),
    fileSize: v.number(),
  },
  returns: v.id("files"),
  handler: async (ctx, args) => {
    return await ctx.db.insert("files", {
      storageId: args.storageId,
      fileName: args.fileName,
      fileType: args.fileType,
      fileSize: args.fileSize,
      uploadedAt: Date.now(),
    });
  },
});
```

### Serving Files via URL

```typescript
// convex/files.ts
export const getFileUrl = query({
  args: { storageId: v.id("_storage") },
  returns: v.union(v.string(), v.null()),
  handler: async (ctx, args) => {
    return await ctx.storage.getUrl(args.storageId);
  },
});

// Get file with URL
export const getFile = query({
  args: { fileId: v.id("files") },
  returns: v.union(
    v.object({
      _id: v.id("files"),
      fileName: v.string(),
      fileType: v.string(),
      fileSize: v.number(),
      url: v.union(v.string(), v.null()),
    }),
    v.null()
  ),
  handler: async (ctx, args) => {
    const file = await ctx.db.get(args.fileId);
    if (!file) return null;

    const url = await ctx.storage.getUrl(file.storageId);
    
    return {
      _id: file._id,
      fileName: file.fileName,
      fileType: file.fileType,
      fileSize: file.fileSize,
      url,
    };
  },
});
```

### Displaying Files in React

```typescript
import { useQuery } from "convex/react";
import { api } from "../convex/_generated/api";

function FileDisplay({ fileId }: { fileId: Id<"files"> }) {
  const file = useQuery(api.files.getFile, { fileId });

  if (!file) return <div>Loading...</div>;
  if (!file.url) return <div>File not found</div>;

  // Handle different file types
  if (file.fileType.startsWith("image/")) {
    return <img src={file.url} alt={file.fileName} />;
  }

  if (file.fileType === "application/pdf") {
    return (
      <iframe
        src={file.url}
        title={file.fileName}
        width="100%"
        height="600px"
      />
    );
  }

  return (
    <a href={file.url} download={file.fileName}>
      Download {file.fileName}
    </a>
  );
}
```

### Storing Generated Files from Actions

```typescript
// convex/generate.ts
"use node";

import { action } from "./_generated/server";
import { v } from "convex/values";
import { api } from "./_generated/api";

export const generatePDF = action({
  args: { content: v.string() },
  returns: v.id("_storage"),
  handler: async (ctx, args) => {
    // Generate PDF (example using a library)
    const pdfBuffer = await generatePDFFromContent(args.content);

    // Convert to Blob
    const blob = new Blob([pdfBuffer], { type: "application/pdf" });

    // Store in Convex
    const storageId = await ctx.storage.store(blob);

    return storageId;
  },
});

// Generate and save image
export const generateImage = action({
  args: { prompt: v.string() },
  returns: v.id("_storage"),
  handler: async (ctx, args) => {
    // Call external API to generate image
    const response = await fetch("https://api.example.com/generate", {
      method: "POST",
      body: JSON.stringify({ prompt: args.prompt }),
    });

    const imageBuffer = await response.arrayBuffer();
    const blob = new Blob([imageBuffer], { type: "image/png" });

    return await ctx.storage.store(blob);
  },
});
```

### Accessing File Metadata

```typescript
// convex/files.ts
import { query } from "./_generated/server";
import { v } from "convex/values";
import { Id } from "./_generated/dataModel";

type FileMetadata = {
  _id: Id<"_storage">;
  _creationTime: number;
  contentType?: string;
  sha256: string;
  size: number;
};

export const getFileMetadata = query({
  args: { storageId: v.id("_storage") },
  returns: v.union(
    v.object({
      _id: v.id("_storage"),
      _creationTime: v.number(),
      contentType: v.optional(v.string()),
      sha256: v.string(),
      size: v.number(),
    }),
    v.null()
  ),
  handler: async (ctx, args) => {
    const metadata = await ctx.db.system.get(args.storageId);
    return metadata as FileMetadata | null;
  },
});
```

### Deleting Files

```typescript
// convex/files.ts
import { mutation } from "./_generated/server";
import { v } from "convex/values";

export const deleteFile = mutation({
  args: { fileId: v.id("files") },
  returns: v.null(),
  handler: async (ctx, args) => {
    const file = await ctx.db.get(args.fileId);
    if (!file) return null;

    // Delete from storage
    await ctx.storage.delete(file.storageId);

    // Delete database record
    await ctx.db.delete(args.fileId);

    return null;
  },
});
```

### Image Upload with Preview

```typescript
import { useMutation } from "convex/react";
import { api } from "../convex/_generated/api";
import { useState, useRef } from "react";

function ImageUploader({ onUpload }: { onUpload: (id: Id<"files">) => void }) {
  const generateUploadUrl = useMutation(api.files.generateUploadUrl);
  const saveFile = useMutation(api.files.saveFile);
  const [preview, setPreview] = useState<string | null>(null);
  const [uploading, setUploading] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);

  const handleFileSelect = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    // Validate file type
    if (!file.type.startsWith("image/")) {
      alert("Please select an image file");
      return;
    }

    // Validate file size (max 10MB)
    if (file.size > 10 * 1024 * 1024) {
      alert("File size must be less than 10MB");
      return;
    }

    // Show preview
    const reader = new FileReader();
    reader.onload = (e) => setPreview(e.target?.result as string);
    reader.readAsDataURL(file);

    // Upload
    setUploading(true);
    try {
      const uploadUrl = await generateUploadUrl();
      const result = await fetch(uploadUrl, {
        method: "POST",
        headers: { "Content-Type": file.type },
        body: file,
      });

      const { storageId } = await result.json();
      const fileId = await saveFile({
        storageId,
        fileName: file.name,
        fileType: file.type,
        fileSize: file.size,
      });

      onUpload(fileId);
    } finally {
      setUploading(false);
    }
  };

  return (
    <div>
      <input
        ref={inputRef}
        type="file"
        accept="image/*"
        onChange={handleFileSelect}
        style={{ display: "none" }}
      />
      
      <button
        onClick={() => inputRef.current?.click()}
        disabled={uploading}
      >
        {uploading ? "Uploading..." : "Select Image"}
      </button>

      {preview && (
        <img
          src={preview}
          alt="Preview"
          style={{ maxWidth: 200, marginTop: 10 }}
        />
      )}
    </div>
  );
}
```

## Examples

### Schema for File Storage

```typescript
// convex/schema.ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  files: defineTable({
    storageId: v.id("_storage"),
    fileName: v.string(),
    fileType: v.string(),
    fileSize: v.number(),
    uploadedBy: v.id("users"),
    uploadedAt: v.number(),
  })
    .index("by_user", ["uploadedBy"])
    .index("by_type", ["fileType"]),

  // User avatars
  users: defineTable({
    name: v.string(),
    email: v.string(),
    avatarStorageId: v.optional(v.id("_storage")),
  }),

  // Posts with images
  posts: defineTable({
    authorId: v.id("users"),
    content: v.string(),
    imageStorageIds: v.array(v.id("_storage")),
    createdAt: v.number(),
  }).index("by_author", ["authorId"]),
});
```

## Best Practices

- Never run `npx convex deploy` unless explicitly instructed
- Never run any git commands unless explicitly instructed
- Validate file types and sizes on the client before uploading
- Store file metadata (name, type, size) in your own table
- Use the `_storage` system table only for Convex metadata
- Delete storage files when deleting database references
- Use appropriate Content-Type headers when uploading
- Consider image optimization for large images

## Common Pitfalls

1. **Not setting Content-Type header** - Files may not serve correctly
2. **Forgetting to delete storage** - Orphaned files waste storage
3. **Not validating file types** - Security risk for malicious uploads
4. **Large file uploads without progress** - Poor UX for users
5. **Using deprecated getMetadata** - Use ctx.db.system.get instead

## References

- Convex Documentation: https://docs.convex.dev/
- Convex LLMs.txt: https://docs.convex.dev/llms.txt
- File Storage: https://docs.convex.dev/file-storage
- Upload Files: https://docs.convex.dev/file-vault/upload-files
- Serve Files: https://docs.convex.dev/file-vault/serve-files
```

## File: `skills/convex-file-vault/agents/openai.yaml`
```yaml
interface:
  icon_small: "./assets/small-logo.svg"
  icon_large: "./assets/large-logo.png"
```

## File: `skills/convex-functions/SKILL.md`
```markdown
---
name: convex-functions
displayName: Convex Functions
description: Writing queries, mutations, actions, and HTTP actions with proper argument validation, error handling, internal functions, and runtime considerations
version: 1.0.0
author: Convex
tags: [convex, functions, queries, mutations, actions, http]
---

# Convex Functions

Master Convex functions including queries, mutations, actions, and HTTP endpoints with proper validation, error handling, and runtime considerations.

## Code Quality

All examples in this skill comply with @convex-dev/eslint-plugin rules:

- Object syntax with `handler` property
- Argument validators on all functions
- Explicit table names in database operations

See the Code Quality section in [convex-best-practices](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) for linting setup.

## Documentation Sources

Before implementing, do not assume; fetch the latest documentation:

- Primary: https://docs.convex.dev/functions
- Query Functions: https://docs.convex.dev/functions/query-functions
- Mutation Functions: https://docs.convex.dev/functions/mutation-functions
- Actions: https://docs.convex.dev/functions/actions
- HTTP Actions: https://docs.convex.dev/functions/http-actions
- For broader context: https://docs.convex.dev/llms.txt

## Instructions

### Function Types Overview

| Type        | Database Access          | External APIs | Caching       | Use Case              |
| ----------- | ------------------------ | ------------- | ------------- | --------------------- |
| Query       | Read-only                | No            | Yes, reactive | Fetching data         |
| Mutation    | Read/Write               | No            | No            | Modifying data        |
| Action      | Via runQuery/runMutation | Yes           | No            | External integrations |
| HTTP Action | Via runQuery/runMutation | Yes           | No            | Webhooks, APIs        |

### Queries

Queries are reactive, cached, and read-only:

```typescript
import { query } from "./_generated/server";
import { v } from "convex/values";

export const getUser = query({
  args: { userId: v.id("users") },
  returns: v.union(
    v.object({
      _id: v.id("users"),
      _creationTime: v.number(),
      name: v.string(),
      email: v.string(),
    }),
    v.null(),
  ),
  handler: async (ctx, args) => {
    return await ctx.db.get("users", args.userId);
  },
});

// Query with index
export const listUserTasks = query({
  args: { userId: v.id("users") },
  returns: v.array(
    v.object({
      _id: v.id("tasks"),
      _creationTime: v.number(),
      title: v.string(),
      completed: v.boolean(),
    }),
  ),
  handler: async (ctx, args) => {
    return await ctx.db
      .query("tasks")
      .withIndex("by_user", (q) => q.eq("userId", args.userId))
      .order("desc")
      .collect();
  },
});
```

### Mutations

Mutations modify the database and are transactional:

```typescript
import { mutation } from "./_generated/server";
import { v } from "convex/values";
import { ConvexError } from "convex/values";

export const createTask = mutation({
  args: {
    title: v.string(),
    userId: v.id("users"),
  },
  returns: v.id("tasks"),
  handler: async (ctx, args) => {
    // Validate user exists
    const user = await ctx.db.get("users", args.userId);
    if (!user) {
      throw new ConvexError("User not found");
    }

    return await ctx.db.insert("tasks", {
      title: args.title,
      userId: args.userId,
      completed: false,
      createdAt: Date.now(),
    });
  },
});

export const deleteTask = mutation({
  args: { taskId: v.id("tasks") },
  returns: v.null(),
  handler: async (ctx, args) => {
    await ctx.db.delete("tasks", args.taskId);
    return null;
  },
});
```

### Actions

Actions can call external APIs but have no direct database access:

```typescript
"use node";

import { action } from "./_generated/server";
import { v } from "convex/values";
import { api, internal } from "./_generated/api";

export const sendEmail = action({
  args: {
    to: v.string(),
    subject: v.string(),
    body: v.string(),
  },
  returns: v.object({ success: v.boolean() }),
  handler: async (ctx, args) => {
    // Call external API
    const response = await fetch("https://api.email.com/send", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(args),
    });

    return { success: response.ok };
  },
});

// Action calling queries and mutations
export const processOrder = action({
  args: { orderId: v.id("orders") },
  returns: v.null(),
  handler: async (ctx, args) => {
    // Read data via query
    const order = await ctx.runQuery(api.orders.get, { orderId: args.orderId });

    if (!order) {
      throw new Error("Order not found");
    }

    // Call external payment API
    const paymentResult = await processPayment(order);

    // Update database via mutation
    await ctx.runMutation(internal.orders.updateStatus, {
      orderId: args.orderId,
      status: paymentResult.success ? "paid" : "failed",
    });

    return null;
  },
});
```

### HTTP Actions

HTTP actions handle webhooks and external requests:

```typescript
// convex/http.ts
import { httpRouter } from "convex/server";
import { httpAction } from "./_generated/server";
import { api, internal } from "./_generated/api";

const http = httpRouter();

// Webhook endpoint
http.route({
  path: "/webhooks/stripe",
  method: "POST",
  handler: httpAction(async (ctx, request) => {
    const signature = request.headers.get("stripe-signature");
    const body = await request.text();

    // Verify webhook signature
    if (!verifyStripeSignature(body, signature)) {
      return new Response("Invalid signature", { status: 401 });
    }

    const event = JSON.parse(body);

    // Process webhook
    await ctx.runMutation(internal.payments.handleWebhook, {
      eventType: event.type,
      data: event.data,
    });

    return new Response("OK", { status: 200 });
  }),
});

// API endpoint
http.route({
  path: "/api/users/:userId",
  method: "GET",
  handler: httpAction(async (ctx, request) => {
    const url = new URL(request.url);
    const userId = url.pathname.split("/").pop();

    const user = await ctx.runQuery(api.users.get, {
      userId: userId as Id<"users">,
    });

    if (!user) {
      return new Response("Not found", { status: 404 });
    }

    return Response.json(user);
  }),
});

export default http;
```

### Internal Functions

Use internal functions for sensitive operations:

```typescript
import {
  internalMutation,
  internalQuery,
  internalAction,
} from "./_generated/server";
import { v } from "convex/values";

// Only callable from other Convex functions
export const _updateUserCredits = internalMutation({
  args: {
    userId: v.id("users"),
    amount: v.number(),
  },
  returns: v.null(),
  handler: async (ctx, args) => {
    const user = await ctx.db.get("users", args.userId);
    if (!user) return null;

    await ctx.db.patch("users", args.userId, {
      credits: (user.credits || 0) + args.amount,
    });
    return null;
  },
});

// Call internal function from action
export const purchaseCredits = action({
  args: { userId: v.id("users"), amount: v.number() },
  returns: v.null(),
  handler: async (ctx, args) => {
    // Process payment externally
    await processPayment(args.amount);

    // Update credits via internal mutation
    await ctx.runMutation(internal.users._updateUserCredits, {
      userId: args.userId,
      amount: args.amount,
    });

    return null;
  },
});
```

### Scheduling Functions

Schedule functions to run later:

```typescript
import { mutation, internalMutation } from "./_generated/server";
import { v } from "convex/values";
import { internal } from "./_generated/api";

export const scheduleReminder = mutation({
  args: {
    userId: v.id("users"),
    message: v.string(),
    delayMs: v.number(),
  },
  returns: v.id("_scheduled_functions"),
  handler: async (ctx, args) => {
    return await ctx.scheduler.runAfter(
      args.delayMs,
      internal.notifications.sendReminder,
      { userId: args.userId, message: args.message },
    );
  },
});

export const sendReminder = internalMutation({
  args: {
    userId: v.id("users"),
    message: v.string(),
  },
  returns: v.null(),
  handler: async (ctx, args) => {
    await ctx.db.insert("notifications", {
      userId: args.userId,
      message: args.message,
      sentAt: Date.now(),
    });
    return null;
  },
});
```

## Examples

### Complete Function File

```typescript
// convex/messages.ts
import { query, mutation, internalMutation } from "./_generated/server";
import { v } from "convex/values";
import { ConvexError } from "convex/values";
import { internal } from "./_generated/api";

const messageValidator = v.object({
  _id: v.id("messages"),
  _creationTime: v.number(),
  channelId: v.id("channels"),
  authorId: v.id("users"),
  content: v.string(),
  editedAt: v.optional(v.number()),
});

// Public query
export const list = query({
  args: {
    channelId: v.id("channels"),
    limit: v.optional(v.number()),
  },
  returns: v.array(messageValidator),
  handler: async (ctx, args) => {
    const limit = args.limit ?? 50;
    return await ctx.db
      .query("messages")
      .withIndex("by_channel", (q) => q.eq("channelId", args.channelId))
      .order("desc")
      .take(limit);
  },
});

// Public mutation
export const send = mutation({
  args: {
    channelId: v.id("channels"),
    authorId: v.id("users"),
    content: v.string(),
  },
  returns: v.id("messages"),
  handler: async (ctx, args) => {
    if (args.content.trim().length === 0) {
      throw new ConvexError("Message cannot be empty");
    }

    const messageId = await ctx.db.insert("messages", {
      channelId: args.channelId,
      authorId: args.authorId,
      content: args.content.trim(),
    });

    // Schedule notification
    await ctx.scheduler.runAfter(0, internal.messages.notifySubscribers, {
      channelId: args.channelId,
      messageId,
    });

    return messageId;
  },
});

// Internal mutation
export const notifySubscribers = internalMutation({
  args: {
    channelId: v.id("channels"),
    messageId: v.id("messages"),
  },
  returns: v.null(),
  handler: async (ctx, args) => {
    // Get channel subscribers and notify them
    const subscribers = await ctx.db
      .query("subscriptions")
      .withIndex("by_channel", (q) => q.eq("channelId", args.channelId))
      .collect();

    for (const sub of subscribers) {
      await ctx.db.insert("notifications", {
        userId: sub.userId,
        messageId: args.messageId,
        read: false,
      });
    }
    return null;
  },
});
```

## Best Practices

- Never run `npx convex deploy` unless explicitly instructed
- Never run any git commands unless explicitly instructed
- Always define args and returns validators
- Use queries for read operations (they are cached and reactive)
- Use mutations for write operations (they are transactional)
- Use actions only when calling external APIs
- Use internal functions for sensitive operations
- Add `"use node";` at the top of action files using Node.js APIs
- Handle errors with ConvexError for user-facing messages

## Common Pitfalls

1. **Using actions for database operations** - Use queries/mutations instead
2. **Calling external APIs from queries/mutations** - Use actions
3. **Forgetting to add "use node"** - Required for Node.js APIs in actions
4. **Missing return validators** - Always specify returns
5. **Not using internal functions for sensitive logic** - Protect with internalMutation

## References

- Convex Documentation: https://docs.convex.dev/
- Convex LLMs.txt: https://docs.convex.dev/llms.txt
- Functions Overview: https://docs.convex.dev/functions
- Query Functions: https://docs.convex.dev/functions/query-functions
- Mutation Functions: https://docs.convex.dev/functions/mutation-functions
- Actions: https://docs.convex.dev/functions/actions
```

## File: `skills/convex-functions/agents/openai.yaml`
```yaml
interface:
  icon_small: "./assets/small-logo.svg"
  icon_large: "./assets/large-logo.png"
```

## File: `skills/convex-http-actions/SKILL.md`
```markdown
---
name: convex-http-actions
displayName: Convex HTTP Actions
description: External API integration and webhook handling including HTTP endpoint routing, request/response handling, authentication, CORS configuration, and webhook signature validation
version: 1.0.0
author: Convex
tags: [convex, http, actions, webhooks, api, endpoints]
---

# Convex HTTP Actions

Build HTTP endpoints for webhooks, external API integrations, and custom routes in Convex applications.

## Documentation Sources

Before implementing, do not assume; fetch the latest documentation:

- Primary: https://docs.convex.dev/functions/http-actions
- Actions Overview: https://docs.convex.dev/functions/actions
- Authentication: https://docs.convex.dev/auth
- For broader context: https://docs.convex.dev/llms.txt

## Instructions

### HTTP Actions Overview

HTTP actions allow you to define HTTP endpoints in Convex that can:

- Receive webhooks from third-party services
- Create custom API routes
- Handle file uploads
- Integrate with external services
- Serve dynamic content

### Basic HTTP Router Setup

```typescript
// convex/http.ts
import { httpRouter } from "convex/server";
import { httpAction } from "./_generated/server";

const http = httpRouter();

// Simple GET endpoint
http.route({
  path: "/health",
  method: "GET",
  handler: httpAction(async (ctx, request) => {
    return new Response(JSON.stringify({ status: "ok" }), {
      status: 200,
      headers: { "Content-Type": "application/json" },
    });
  }),
});

export default http;
```

### Request Handling

```typescript
// convex/http.ts
import { httpRouter } from "convex/server";
import { httpAction } from "./_generated/server";

const http = httpRouter();

// Handle JSON body
http.route({
  path: "/api/data",
  method: "POST",
  handler: httpAction(async (ctx, request) => {
    // Parse JSON body
    const body = await request.json();
    
    // Access headers
    const authHeader = request.headers.get("Authorization");
    
    // Access URL parameters
    const url = new URL(request.url);
    const queryParam = url.searchParams.get("filter");

    return new Response(
      JSON.stringify({ received: body, filter: queryParam }),
      {
        status: 200,
        headers: { "Content-Type": "application/json" },
      }
    );
  }),
});

// Handle form data
http.route({
  path: "/api/form",
  method: "POST",
  handler: httpAction(async (ctx, request) => {
    const formData = await request.formData();
    const name = formData.get("name");
    const email = formData.get("email");

    return new Response(
      JSON.stringify({ name, email }),
      {
        status: 200,
        headers: { "Content-Type": "application/json" },
      }
    );
  }),
});

// Handle raw bytes
http.route({
  path: "/api/upload",
  method: "POST",
  handler: httpAction(async (ctx, request) => {
    const bytes = await request.bytes();
    const contentType = request.headers.get("Content-Type") ?? "application/octet-stream";
    
    // Store in Convex storage
    const blob = new Blob([bytes], { type: contentType });
    const storageId = await ctx.storage.store(blob);

    return new Response(
      JSON.stringify({ storageId }),
      {
        status: 200,
        headers: { "Content-Type": "application/json" },
      }
    );
  }),
});

export default http;
```

### Path Parameters

Use path prefix matching for dynamic routes:

```typescript
// convex/http.ts
import { httpRouter } from "convex/server";
import { httpAction } from "./_generated/server";

const http = httpRouter();

// Match /api/users/* with pathPrefix
http.route({
  pathPrefix: "/api/users/",
  method: "GET",
  handler: httpAction(async (ctx, request) => {
    const url = new URL(request.url);
    // Extract user ID from path: /api/users/123 -> "123"
    const userId = url.pathname.replace("/api/users/", "");

    return new Response(
      JSON.stringify({ userId }),
      {
        status: 200,
        headers: { "Content-Type": "application/json" },
      }
    );
  }),
});

export default http;
```

### CORS Configuration

```typescript
// convex/http.ts
import { httpRouter } from "convex/server";
import { httpAction } from "./_generated/server";

const http = httpRouter();

// CORS headers helper
const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, Authorization",
  "Access-Control-Max-Age": "86400",
};

// Handle preflight requests
http.route({
  path: "/api/data",
  method: "OPTIONS",
  handler: httpAction(async () => {
    return new Response(null, {
      status: 204,
      headers: corsHeaders,
    });
  }),
});

// Actual endpoint with CORS
http.route({
  path: "/api/data",
  method: "POST",
  handler: httpAction(async (ctx, request) => {
    const body = await request.json();

    return new Response(
      JSON.stringify({ success: true, data: body }),
      {
        status: 200,
        headers: {
          "Content-Type": "application/json",
          ...corsHeaders,
        },
      }
    );
  }),
});

export default http;
```

### Webhook Handling

```typescript
// convex/http.ts
import { httpRouter } from "convex/server";
import { httpAction } from "./_generated/server";
import { internal } from "./_generated/api";

const http = httpRouter();

// Stripe webhook
http.route({
  path: "/webhooks/stripe",
  method: "POST",
  handler: httpAction(async (ctx, request) => {
    const signature = request.headers.get("stripe-signature");
    if (!signature) {
      return new Response("Missing signature", { status: 400 });
    }

    const body = await request.text();

    // Verify webhook signature (in action with Node.js)
    try {
      await ctx.runAction(internal.stripe.verifyAndProcessWebhook, {
        body,
        signature,
      });
      return new Response("OK", { status: 200 });
    } catch (error) {
      console.error("Webhook error:", error);
      return new Response("Webhook error", { status: 400 });
    }
  }),
});

// GitHub webhook
http.route({
  path: "/webhooks/github",
  method: "POST",
  handler: httpAction(async (ctx, request) => {
    const event = request.headers.get("X-GitHub-Event");
    const signature = request.headers.get("X-Hub-Signature-256");
    
    if (!signature) {
      return new Response("Missing signature", { status: 400 });
    }

    const body = await request.text();

    await ctx.runAction(internal.github.processWebhook, {
      event: event ?? "unknown",
      body,
      signature,
    });

    return new Response("OK", { status: 200 });
  }),
});

export default http;
```

### Webhook Signature Verification

```typescript
// convex/stripe.ts
"use node";

import { internalAction, internalMutation } from "./_generated/server";
import { internal } from "./_generated/api";
import { v } from "convex/values";
import Stripe from "stripe";

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!);

export const verifyAndProcessWebhook = internalAction({
  args: {
    body: v.string(),
    signature: v.string(),
  },
  returns: v.null(),
  handler: async (ctx, args) => {
    const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET!;

    // Verify signature
    const event = stripe.webhooks.constructEvent(
      args.body,
      args.signature,
      webhookSecret
    );

    // Process based on event type
    switch (event.type) {
      case "checkout.session.completed":
        await ctx.runMutation(internal.payments.handleCheckoutComplete, {
          sessionId: event.data.object.id,
          customerId: event.data.object.customer as string,
        });
        break;

      case "customer.subscription.updated":
        await ctx.runMutation(internal.subscriptions.handleUpdate, {
          subscriptionId: event.data.object.id,
          status: event.data.object.status,
        });
        break;
    }

    return null;
  },
});
```

### Authentication in HTTP Actions

```typescript
// convex/http.ts
import { httpRouter } from "convex/server";
import { httpAction } from "./_generated/server";
import { internal } from "./_generated/api";

const http = httpRouter();

// API key authentication
http.route({
  path: "/api/protected",
  method: "GET",
  handler: httpAction(async (ctx, request) => {
    const apiKey = request.headers.get("X-API-Key");
    
    if (!apiKey) {
      return new Response(
        JSON.stringify({ error: "Missing API key" }),
        { status: 401, headers: { "Content-Type": "application/json" } }
      );
    }

    // Validate API key
    const isValid = await ctx.runQuery(internal.auth.validateApiKey, {
      apiKey,
    });

    if (!isValid) {
      return new Response(
        JSON.stringify({ error: "Invalid API key" }),
        { status: 403, headers: { "Content-Type": "application/json" } }
      );
    }

    // Process authenticated request
    const data = await ctx.runQuery(internal.data.getProtectedData, {});

    return new Response(
      JSON.stringify(data),
      { status: 200, headers: { "Content-Type": "application/json" } }
    );
  }),
});

// Bearer token authentication
http.route({
  path: "/api/user",
  method: "GET",
  handler: httpAction(async (ctx, request) => {
    const authHeader = request.headers.get("Authorization");
    
    if (!authHeader?.startsWith("Bearer ")) {
      return new Response(
        JSON.stringify({ error: "Missing or invalid Authorization header" }),
        { status: 401, headers: { "Content-Type": "application/json" } }
      );
    }

    const token = authHeader.slice(7);

    // Validate token and get user
    const user = await ctx.runQuery(internal.auth.validateToken, { token });

    if (!user) {
      return new Response(
        JSON.stringify({ error: "Invalid token" }),
        { status: 403, headers: { "Content-Type": "application/json" } }
      );
    }

    return new Response(
      JSON.stringify(user),
      { status: 200, headers: { "Content-Type": "application/json" } }
    );
  }),
});

export default http;
```

### Calling Mutations and Queries

```typescript
// convex/http.ts
import { httpRouter } from "convex/server";
import { httpAction } from "./_generated/server";
import { api, internal } from "./_generated/api";

const http = httpRouter();

http.route({
  path: "/api/items",
  method: "POST",
  handler: httpAction(async (ctx, request) => {
    const body = await request.json();

    // Call a mutation
    const itemId = await ctx.runMutation(internal.items.create, {
      name: body.name,
      description: body.description,
    });

    // Query the created item
    const item = await ctx.runQuery(internal.items.get, { id: itemId });

    return new Response(
      JSON.stringify(item),
      { status: 201, headers: { "Content-Type": "application/json" } }
    );
  }),
});

http.route({
  path: "/api/items",
  method: "GET",
  handler: httpAction(async (ctx, request) => {
    const url = new URL(request.url);
    const limit = parseInt(url.searchParams.get("limit") ?? "10");

    const items = await ctx.runQuery(internal.items.list, { limit });

    return new Response(
      JSON.stringify(items),
      { status: 200, headers: { "Content-Type": "application/json" } }
    );
  }),
});

export default http;
```

### Error Handling

```typescript
// convex/http.ts
import { httpRouter } from "convex/server";
import { httpAction } from "./_generated/server";

const http = httpRouter();

// Helper for JSON responses
function jsonResponse(data: unknown, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "Content-Type": "application/json" },
  });
}

// Helper for error responses
function errorResponse(message: string, status: number) {
  return jsonResponse({ error: message }, status);
}

http.route({
  path: "/api/process",
  method: "POST",
  handler: httpAction(async (ctx, request) => {
    try {
      // Validate content type
      const contentType = request.headers.get("Content-Type");
      if (!contentType?.includes("application/json")) {
        return errorResponse("Content-Type must be application/json", 415);
      }

      // Parse body
      let body;
      try {
        body = await request.json();
      } catch {
        return errorResponse("Invalid JSON body", 400);
      }

      // Validate required fields
      if (!body.data) {
        return errorResponse("Missing required field: data", 400);
      }

      // Process request
      const result = await ctx.runMutation(internal.process.handle, {
        data: body.data,
      });

      return jsonResponse({ success: true, result }, 200);
    } catch (error) {
      console.error("Processing error:", error);
      return errorResponse("Internal server error", 500);
    }
  }),
});

export default http;
```

### File Downloads

```typescript
// convex/http.ts
import { httpRouter } from "convex/server";
import { httpAction } from "./_generated/server";
import { Id } from "./_generated/dataModel";

const http = httpRouter();

http.route({
  pathPrefix: "/files/",
  method: "GET",
  handler: httpAction(async (ctx, request) => {
    const url = new URL(request.url);
    const fileId = url.pathname.replace("/files/", "") as Id<"_storage">;

    // Get file URL from storage
    const fileUrl = await ctx.storage.getUrl(fileId);

    if (!fileUrl) {
      return new Response("File not found", { status: 404 });
    }

    // Redirect to the file URL
    return Response.redirect(fileUrl, 302);
  }),
});

export default http;
```

## Examples

### Complete Webhook Integration

```typescript
// convex/http.ts
import { httpRouter } from "convex/server";
import { httpAction } from "./_generated/server";
import { internal } from "./_generated/api";

const http = httpRouter();

// Clerk webhook for user sync
http.route({
  path: "/webhooks/clerk",
  method: "POST",
  handler: httpAction(async (ctx, request) => {
    const svixId = request.headers.get("svix-id");
    const svixTimestamp = request.headers.get("svix-timestamp");
    const svixSignature = request.headers.get("svix-signature");

    if (!svixId || !svixTimestamp || !svixSignature) {
      return new Response("Missing Svix headers", { status: 400 });
    }

    const body = await request.text();

    try {
      await ctx.runAction(internal.clerk.verifyAndProcess, {
        body,
        svixId,
        svixTimestamp,
        svixSignature,
      });
      return new Response("OK", { status: 200 });
    } catch (error) {
      console.error("Clerk webhook error:", error);
      return new Response("Webhook verification failed", { status: 400 });
    }
  }),
});

export default http;
```

```typescript
// convex/clerk.ts
"use node";

import { internalAction, internalMutation } from "./_generated/server";
import { internal } from "./_generated/api";
import { v } from "convex/values";
import { Webhook } from "svix";

export const verifyAndProcess = internalAction({
  args: {
    body: v.string(),
    svixId: v.string(),
    svixTimestamp: v.string(),
    svixSignature: v.string(),
  },
  returns: v.null(),
  handler: async (ctx, args) => {
    const webhookSecret = process.env.CLERK_WEBHOOK_SECRET!;
    const wh = new Webhook(webhookSecret);

    const event = wh.verify(args.body, {
      "svix-id": args.svixId,
      "svix-timestamp": args.svixTimestamp,
      "svix-signature": args.svixSignature,
    }) as { type: string; data: Record<string, unknown> };

    switch (event.type) {
      case "user.created":
        await ctx.runMutation(internal.users.create, {
          clerkId: event.data.id as string,
          email: (event.data.email_addresses as Array<{ email_address: string }>)[0]?.email_address,
          name: `${event.data.first_name} ${event.data.last_name}`,
        });
        break;

      case "user.updated":
        await ctx.runMutation(internal.users.update, {
          clerkId: event.data.id as string,
          email: (event.data.email_addresses as Array<{ email_address: string }>)[0]?.email_address,
          name: `${event.data.first_name} ${event.data.last_name}`,
        });
        break;

      case "user.deleted":
        await ctx.runMutation(internal.users.remove, {
          clerkId: event.data.id as string,
        });
        break;
    }

    return null;
  },
});
```

### Schema for HTTP API

```typescript
// convex/schema.ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  apiKeys: defineTable({
    key: v.string(),
    userId: v.id("users"),
    name: v.string(),
    createdAt: v.number(),
    lastUsedAt: v.optional(v.number()),
    revokedAt: v.optional(v.number()),
  })
    .index("by_key", ["key"])
    .index("by_user", ["userId"]),

  webhookEvents: defineTable({
    source: v.string(),
    eventType: v.string(),
    payload: v.any(),
    processedAt: v.number(),
    status: v.union(
      v.literal("success"),
      v.literal("failed")
    ),
    error: v.optional(v.string()),
  })
    .index("by_source", ["source"])
    .index("by_status", ["status"]),

  users: defineTable({
    clerkId: v.string(),
    email: v.string(),
    name: v.string(),
  }).index("by_clerk_id", ["clerkId"]),
});
```

## Best Practices

- Never run `npx convex deploy` unless explicitly instructed
- Never run any git commands unless explicitly instructed
- Always validate and sanitize incoming request data
- Use internal functions for database operations
- Implement proper error handling with appropriate status codes
- Add CORS headers for browser-accessible endpoints
- Verify webhook signatures before processing
- Log webhook events for debugging
- Use environment variables for secrets
- Handle timeouts gracefully

## Common Pitfalls

1. **Missing CORS preflight handler** - Browsers send OPTIONS requests first
2. **Not validating webhook signatures** - Security vulnerability
3. **Exposing internal functions** - Use internal functions from HTTP actions
4. **Forgetting Content-Type headers** - Clients may not parse responses correctly
5. **Not handling request body errors** - Invalid JSON will throw
6. **Blocking on long operations** - Use scheduled functions for heavy processing

## References

- Convex Documentation: https://docs.convex.dev/
- Convex LLMs.txt: https://docs.convex.dev/llms.txt
- HTTP Actions: https://docs.convex.dev/functions/http-actions
- Actions: https://docs.convex.dev/functions/actions
- Authentication: https://docs.convex.dev/auth
```

## File: `skills/convex-http-actions/agents/openai.yaml`
```yaml
interface:
  icon_small: "./assets/small-logo.svg"
  icon_large: "./assets/large-logo.png"
```

## File: `skills/convex-migrations/SKILL.md`
```markdown
---
name: convex-migrations
displayName: Convex Migrations
description: Schema migration strategies for evolving applications including adding new fields, backfilling data, removing deprecated fields, index migrations, and zero-downtime migration patterns
version: 1.0.0
author: Convex
tags: [convex, migrations, schema, database, data-modeling]
---

# Convex Migrations

Evolve your Convex database schema safely with patterns for adding fields, backfilling data, removing deprecated fields, and maintaining zero-downtime deployments.

## Documentation Sources

Before implementing, do not assume; fetch the latest documentation:

- Primary: https://docs.convex.dev/database/schemas
- Schema Overview: https://docs.convex.dev/database
- Migration Patterns: https://stack.convex.dev/migrate-data-postgres-to-convex
- For broader context: https://docs.convex.dev/llms.txt

## Instructions

### Migration Philosophy

Convex handles schema evolution differently than traditional databases:

- No explicit migration files or commands
- Schema changes deploy instantly with `npx convex dev`
- Existing data is not automatically transformed
- Use optional fields and backfill mutations for safe migrations

### Adding New Fields

Start with optional fields, then backfill:

```typescript
// Step 1: Add optional field to schema
// convex/schema.ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  users: defineTable({
    name: v.string(),
    email: v.string(),
    // New field - start as optional
    avatarUrl: v.optional(v.string()),
  }),
});
```

```typescript
// Step 2: Update code to handle both cases
// convex/users.ts
import { query } from "./_generated/server";
import { v } from "convex/values";

export const getUser = query({
  args: { userId: v.id("users") },
  returns: v.union(
    v.object({
      _id: v.id("users"),
      name: v.string(),
      email: v.string(),
      avatarUrl: v.union(v.string(), v.null()),
    }),
    v.null()
  ),
  handler: async (ctx, args) => {
    const user = await ctx.db.get(args.userId);
    if (!user) return null;

    return {
      _id: user._id,
      name: user.name,
      email: user.email,
      // Handle missing field gracefully
      avatarUrl: user.avatarUrl ?? null,
    };
  },
});
```

```typescript
// Step 3: Backfill existing documents
// convex/migrations.ts
import { internalMutation } from "./_generated/server";
import { internal } from "./_generated/api";
import { v } from "convex/values";

const BATCH_SIZE = 100;

export const backfillAvatarUrl = internalMutation({
  args: {
    cursor: v.optional(v.string()),
  },
  returns: v.object({
    processed: v.number(),
    hasMore: v.boolean(),
  }),
  handler: async (ctx, args) => {
    const result = await ctx.db
      .query("users")
      .paginate({ numItems: BATCH_SIZE, cursor: args.cursor ?? null });

    let processed = 0;
    for (const user of result.page) {
      // Only update if field is missing
      if (user.avatarUrl === undefined) {
        await ctx.db.patch(user._id, {
          avatarUrl: generateDefaultAvatar(user.name),
        });
        processed++;
      }
    }

    // Schedule next batch if needed
    if (!result.isDone) {
      await ctx.scheduler.runAfter(0, internal.migrations.backfillAvatarUrl, {
        cursor: result.continueCursor,
      });
    }

    return {
      processed,
      hasMore: !result.isDone,
    };
  },
});

function generateDefaultAvatar(name: string): string {
  return `https://api.dicebear.com/7.x/initials/svg?seed=${encodeURIComponent(name)}`;
}
```

```typescript
// Step 4: After backfill completes, make field required
// convex/schema.ts
export default defineSchema({
  users: defineTable({
    name: v.string(),
    email: v.string(),
    avatarUrl: v.string(), // Now required
  }),
});
```

### Removing Fields

Remove field usage before removing from schema:

```typescript
// Step 1: Stop using the field in queries and mutations
// Mark as deprecated in code comments

// Step 2: Remove field from schema (make optional first if needed)
// convex/schema.ts
export default defineSchema({
  posts: defineTable({
    title: v.string(),
    content: v.string(),
    authorId: v.id("users"),
    // legacyField: v.optional(v.string()), // Remove this line
  }),
});

// Step 3: Optionally clean up existing data
// convex/migrations.ts
export const removeDeprecatedField = internalMutation({
  args: {
    cursor: v.optional(v.string()),
  },
  returns: v.null(),
  handler: async (ctx, args) => {
    const result = await ctx.db
      .query("posts")
      .paginate({ numItems: 100, cursor: args.cursor ?? null });

    for (const post of result.page) {
      // Use replace to remove the field entirely
      const { legacyField, ...rest } = post as typeof post & { legacyField?: string };
      if (legacyField !== undefined) {
        await ctx.db.replace(post._id, rest);
      }
    }

    if (!result.isDone) {
      await ctx.scheduler.runAfter(0, internal.migrations.removeDeprecatedField, {
        cursor: result.continueCursor,
      });
    }

    return null;
  },
});
```

### Renaming Fields

Renaming requires copying data to new field, then removing old:

```typescript
// Step 1: Add new field as optional
// convex/schema.ts
export default defineSchema({
  users: defineTable({
    userName: v.string(), // Old field
    displayName: v.optional(v.string()), // New field
  }),
});

// Step 2: Update code to read from new field with fallback
export const getUser = query({
  args: { userId: v.id("users") },
  returns: v.object({
    _id: v.id("users"),
    displayName: v.string(),
  }),
  handler: async (ctx, args) => {
    const user = await ctx.db.get(args.userId);
    if (!user) throw new Error("User not found");

    return {
      _id: user._id,
      // Read new field, fall back to old
      displayName: user.displayName ?? user.userName,
    };
  },
});

// Step 3: Backfill to copy data
export const backfillDisplayName = internalMutation({
  args: { cursor: v.optional(v.string()) },
  returns: v.null(),
  handler: async (ctx, args) => {
    const result = await ctx.db
      .query("users")
      .paginate({ numItems: 100, cursor: args.cursor ?? null });

    for (const user of result.page) {
      if (user.displayName === undefined) {
        await ctx.db.patch(user._id, {
          displayName: user.userName,
        });
      }
    }

    if (!result.isDone) {
      await ctx.scheduler.runAfter(0, internal.migrations.backfillDisplayName, {
        cursor: result.continueCursor,
      });
    }

    return null;
  },
});

// Step 4: After backfill, update schema to make new field required
// and remove old field
export default defineSchema({
  users: defineTable({
    // userName removed
    displayName: v.string(),
  }),
});
```

### Adding Indexes

Add indexes before using them in queries:

```typescript
// Step 1: Add index to schema
// convex/schema.ts
export default defineSchema({
  posts: defineTable({
    title: v.string(),
    authorId: v.id("users"),
    publishedAt: v.optional(v.number()),
    status: v.string(),
  })
    .index("by_author", ["authorId"])
    // New index
    .index("by_status_and_published", ["status", "publishedAt"]),
});

// Step 2: Deploy schema change
// Run: npx convex dev

// Step 3: Now use the index in queries
export const getPublishedPosts = query({
  args: {},
  returns: v.array(v.object({
    _id: v.id("posts"),
    title: v.string(),
    publishedAt: v.number(),
  })),
  handler: async (ctx) => {
    const posts = await ctx.db
      .query("posts")
      .withIndex("by_status_and_published", (q) =>
        q.eq("status", "published")
      )
      .order("desc")
      .take(10);

    return posts
      .filter((p) => p.publishedAt !== undefined)
      .map((p) => ({
        _id: p._id,
        title: p.title,
        publishedAt: p.publishedAt!,
      }));
  },
});
```

### Changing Field Types

Type changes require careful migration:

```typescript
// Example: Change from string to number for a "priority" field

// Step 1: Add new field with new type
// convex/schema.ts
export default defineSchema({
  tasks: defineTable({
    title: v.string(),
    priority: v.string(), // Old: "low", "medium", "high"
    priorityLevel: v.optional(v.number()), // New: 1, 2, 3
  }),
});

// Step 2: Backfill with type conversion
export const migratePriorityToNumber = internalMutation({
  args: { cursor: v.optional(v.string()) },
  returns: v.null(),
  handler: async (ctx, args) => {
    const result = await ctx.db
      .query("tasks")
      .paginate({ numItems: 100, cursor: args.cursor ?? null });

    const priorityMap: Record<string, number> = {
      low: 1,
      medium: 2,
      high: 3,
    };

    for (const task of result.page) {
      if (task.priorityLevel === undefined) {
        await ctx.db.patch(task._id, {
          priorityLevel: priorityMap[task.priority] ?? 1,
        });
      }
    }

    if (!result.isDone) {
      await ctx.scheduler.runAfter(0, internal.migrations.migratePriorityToNumber, {
        cursor: result.continueCursor,
      });
    }

    return null;
  },
});

// Step 3: Update code to use new field
export const getTask = query({
  args: { taskId: v.id("tasks") },
  returns: v.object({
    _id: v.id("tasks"),
    title: v.string(),
    priorityLevel: v.number(),
  }),
  handler: async (ctx, args) => {
    const task = await ctx.db.get(args.taskId);
    if (!task) throw new Error("Task not found");

    const priorityMap: Record<string, number> = {
      low: 1,
      medium: 2,
      high: 3,
    };

    return {
      _id: task._id,
      title: task.title,
      priorityLevel: task.priorityLevel ?? priorityMap[task.priority] ?? 1,
    };
  },
});

// Step 4: After backfill, update schema
export default defineSchema({
  tasks: defineTable({
    title: v.string(),
    // priority field removed
    priorityLevel: v.number(),
  }),
});
```

### Migration Runner Pattern

Create a reusable migration system:

```typescript
// convex/schema.ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  migrations: defineTable({
    name: v.string(),
    startedAt: v.number(),
    completedAt: v.optional(v.number()),
    status: v.union(
      v.literal("running"),
      v.literal("completed"),
      v.literal("failed")
    ),
    error: v.optional(v.string()),
    processed: v.number(),
  }).index("by_name", ["name"]),

  // Your other tables...
});
```

```typescript
// convex/migrations.ts
import { internalMutation, internalQuery } from "./_generated/server";
import { internal } from "./_generated/api";
import { v } from "convex/values";

// Check if migration has run
export const hasMigrationRun = internalQuery({
  args: { name: v.string() },
  returns: v.boolean(),
  handler: async (ctx, args) => {
    const migration = await ctx.db
      .query("migrations")
      .withIndex("by_name", (q) => q.eq("name", args.name))
      .first();
    return migration?.status === "completed";
  },
});

// Start a migration
export const startMigration = internalMutation({
  args: { name: v.string() },
  returns: v.id("migrations"),
  handler: async (ctx, args) => {
    // Check if already exists
    const existing = await ctx.db
      .query("migrations")
      .withIndex("by_name", (q) => q.eq("name", args.name))
      .first();

    if (existing) {
      if (existing.status === "completed") {
        throw new Error(`Migration ${args.name} already completed`);
      }
      if (existing.status === "running") {
        throw new Error(`Migration ${args.name} already running`);
      }
      // Reset failed migration
      await ctx.db.patch(existing._id, {
        status: "running",
        startedAt: Date.now(),
        error: undefined,
        processed: 0,
      });
      return existing._id;
    }

    return await ctx.db.insert("migrations", {
      name: args.name,
      startedAt: Date.now(),
      status: "running",
      processed: 0,
    });
  },
});

// Update migration progress
export const updateMigrationProgress = internalMutation({
  args: {
    migrationId: v.id("migrations"),
    processed: v.number(),
  },
  returns: v.null(),
  handler: async (ctx, args) => {
    const migration = await ctx.db.get(args.migrationId);
    if (!migration) return null;

    await ctx.db.patch(args.migrationId, {
      processed: migration.processed + args.processed,
    });

    return null;
  },
});

// Complete a migration
export const completeMigration = internalMutation({
  args: { migrationId: v.id("migrations") },
  returns: v.null(),
  handler: async (ctx, args) => {
    await ctx.db.patch(args.migrationId, {
      status: "completed",
      completedAt: Date.now(),
    });
    return null;
  },
});

// Fail a migration
export const failMigration = internalMutation({
  args: {
    migrationId: v.id("migrations"),
    error: v.string(),
  },
  returns: v.null(),
  handler: async (ctx, args) => {
    await ctx.db.patch(args.migrationId, {
      status: "failed",
      error: args.error,
    });
    return null;
  },
});
```

```typescript
// convex/migrations/addUserTimestamps.ts
import { internalMutation } from "../_generated/server";
import { internal } from "../_generated/api";
import { v } from "convex/values";

const MIGRATION_NAME = "add_user_timestamps_v1";
const BATCH_SIZE = 100;

export const run = internalMutation({
  args: {
    migrationId: v.optional(v.id("migrations")),
    cursor: v.optional(v.string()),
  },
  returns: v.null(),
  handler: async (ctx, args) => {
    // Initialize migration on first run
    let migrationId = args.migrationId;
    if (!migrationId) {
      const hasRun = await ctx.runQuery(internal.migrations.hasMigrationRun, {
        name: MIGRATION_NAME,
      });
      if (hasRun) {
        console.log(`Migration ${MIGRATION_NAME} already completed`);
        return null;
      }
      migrationId = await ctx.runMutation(internal.migrations.startMigration, {
        name: MIGRATION_NAME,
      });
    }

    try {
      const result = await ctx.db
        .query("users")
        .paginate({ numItems: BATCH_SIZE, cursor: args.cursor ?? null });

      let processed = 0;
      for (const user of result.page) {
        if (user.createdAt === undefined) {
          await ctx.db.patch(user._id, {
            createdAt: user._creationTime,
            updatedAt: user._creationTime,
          });
          processed++;
        }
      }

      // Update progress
      await ctx.runMutation(internal.migrations.updateMigrationProgress, {
        migrationId,
        processed,
      });

      // Continue or complete
      if (!result.isDone) {
        await ctx.scheduler.runAfter(0, internal.migrations.addUserTimestamps.run, {
          migrationId,
          cursor: result.continueCursor,
        });
      } else {
        await ctx.runMutation(internal.migrations.completeMigration, {
          migrationId,
        });
        console.log(`Migration ${MIGRATION_NAME} completed`);
      }
    } catch (error) {
      await ctx.runMutation(internal.migrations.failMigration, {
        migrationId,
        error: String(error),
      });
      throw error;
    }

    return null;
  },
});
```

## Examples

### Schema with Migration Support

```typescript
// convex/schema.ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  // Migration tracking
  migrations: defineTable({
    name: v.string(),
    startedAt: v.number(),
    completedAt: v.optional(v.number()),
    status: v.union(
      v.literal("running"),
      v.literal("completed"),
      v.literal("failed")
    ),
    error: v.optional(v.string()),
    processed: v.number(),
  }).index("by_name", ["name"]),

  // Users table with evolved schema
  users: defineTable({
    // Original fields
    name: v.string(),
    email: v.string(),
    
    // Added in migration v1
    createdAt: v.optional(v.number()),
    updatedAt: v.optional(v.number()),
    
    // Added in migration v2
    avatarUrl: v.optional(v.string()),
    
    // Added in migration v3
    settings: v.optional(v.object({
      theme: v.string(),
      notifications: v.boolean(),
    })),
  })
    .index("by_email", ["email"])
    .index("by_createdAt", ["createdAt"]),

  // Posts table with indexes for common queries
  posts: defineTable({
    title: v.string(),
    content: v.string(),
    authorId: v.id("users"),
    status: v.union(
      v.literal("draft"),
      v.literal("published"),
      v.literal("archived")
    ),
    publishedAt: v.optional(v.number()),
    createdAt: v.number(),
    updatedAt: v.number(),
  })
    .index("by_author", ["authorId"])
    .index("by_status", ["status"])
    .index("by_author_and_status", ["authorId", "status"])
    .index("by_publishedAt", ["publishedAt"]),
});
```

## Best Practices

- Never run `npx convex deploy` unless explicitly instructed
- Never run any git commands unless explicitly instructed
- Always start with optional fields when adding new data
- Backfill data in batches to avoid timeouts
- Test migrations on development before production
- Keep track of completed migrations to avoid re-running
- Update code to handle both old and new data during transition
- Remove deprecated fields only after all code stops using them
- Use pagination for large datasets
- Add appropriate indexes before running queries on new fields

## Common Pitfalls

1. **Making new fields required immediately** - Breaks existing documents
2. **Not handling undefined values** - Causes runtime errors
3. **Large batch sizes** - Causes function timeouts
4. **Forgetting to update indexes** - Queries fail or perform poorly
5. **Running migrations without tracking** - May run multiple times
6. **Removing fields before code update** - Breaks existing functionality
7. **Not testing on development** - Production data issues

## References

- Convex Documentation: https://docs.convex.dev/
- Convex LLMs.txt: https://docs.convex.dev/llms.txt
- Schemas: https://docs.convex.dev/database/schemas
- Database Overview: https://docs.convex.dev/database
- Migration Patterns: https://stack.convex.dev/migrate-data-postgres-to-convex
```

## File: `skills/convex-migrations/agents/openai.yaml`
```yaml
interface:
  icon_small: "./assets/small-logo.svg"
  icon_large: "./assets/large-logo.png"
```

## File: `skills/convex-realtime/SKILL.md`
```markdown
---
name: convex-realtime
displayName: Convex Realtime
description: Patterns for building reactive apps including subscription management, optimistic updates, cache behavior, and paginated queries with cursor-based loading
version: 1.0.0
author: Convex
tags: [convex, realtime, subscriptions, optimistic-updates, pagination]
---

# Convex Realtime

Build reactive applications with Convex's real-time subscriptions, optimistic updates, intelligent caching, and cursor-based pagination.

## Documentation Sources

Before implementing, do not assume; fetch the latest documentation:

- Primary: https://docs.convex.dev/client/react
- Optimistic Updates: https://docs.convex.dev/client/react/optimistic-updates
- Pagination: https://docs.convex.dev/database/pagination
- For broader context: https://docs.convex.dev/llms.txt

## Instructions

### How Convex Realtime Works

1. **Automatic Subscriptions** - useQuery creates a subscription that updates automatically
2. **Smart Caching** - Query results are cached and shared across components
3. **Consistency** - All subscriptions see a consistent view of the database
4. **Efficient Updates** - Only re-renders when relevant data changes

### Basic Subscriptions

```typescript
// React component with real-time data
import { useQuery } from "convex/react";
import { api } from "../convex/_generated/api";

function TaskList({ userId }: { userId: Id<"users"> }) {
  // Automatically subscribes and updates in real-time
  const tasks = useQuery(api.tasks.list, { userId });

  if (tasks === undefined) {
    return <div>Loading...</div>;
  }

  return (
    <ul>
      {tasks.map((task) => (
        <li key={task._id}>{task.title}</li>
      ))}
    </ul>
  );
}
```

### Conditional Queries

```typescript
import { useQuery } from "convex/react";
import { api } from "../convex/_generated/api";

function UserProfile({ userId }: { userId: Id<"users"> | null }) {
  // Skip query when userId is null
  const user = useQuery(
    api.users.get,
    userId ? { userId } : "skip"
  );

  if (userId === null) {
    return <div>Select a user</div>;
  }

  if (user === undefined) {
    return <div>Loading...</div>;
  }

  return <div>{user.name}</div>;
}
```

### Mutations with Real-time Updates

```typescript
import { useMutation, useQuery } from "convex/react";
import { api } from "../convex/_generated/api";

function TaskManager({ userId }: { userId: Id<"users"> }) {
  const tasks = useQuery(api.tasks.list, { userId });
  const createTask = useMutation(api.tasks.create);
  const toggleTask = useMutation(api.tasks.toggle);

  const handleCreate = async (title: string) => {
    // Mutation triggers automatic re-render when data changes
    await createTask({ title, userId });
  };

  const handleToggle = async (taskId: Id<"tasks">) => {
    await toggleTask({ taskId });
  };

  return (
    <div>
      <button onClick={() => handleCreate("New Task")}>Add Task</button>
      <ul>
        {tasks?.map((task) => (
          <li key={task._id} onClick={() => handleToggle(task._id)}>
            {task.completed ? "✓" : "○"} {task.title}
          </li>
        ))}
      </ul>
    </div>
  );
}
```

### Optimistic Updates

Show changes immediately before server confirmation:

```typescript
import { useMutation, useQuery } from "convex/react";
import { api } from "../convex/_generated/api";
import { Id } from "../convex/_generated/dataModel";

function TaskItem({ task }: { task: Task }) {
  const toggleTask = useMutation(api.tasks.toggle).withOptimisticUpdate(
    (localStore, args) => {
      const { taskId } = args;
      const currentValue = localStore.getQuery(api.tasks.get, { taskId });
      
      if (currentValue !== undefined) {
        localStore.setQuery(api.tasks.get, { taskId }, {
          ...currentValue,
          completed: !currentValue.completed,
        });
      }
    }
  );

  return (
    <div onClick={() => toggleTask({ taskId: task._id })}>
      {task.completed ? "✓" : "○"} {task.title}
    </div>
  );
}
```

### Optimistic Updates for Lists

```typescript
import { useMutation } from "convex/react";
import { api } from "../convex/_generated/api";

function useCreateTask(userId: Id<"users">) {
  return useMutation(api.tasks.create).withOptimisticUpdate(
    (localStore, args) => {
      const { title, userId } = args;
      const currentTasks = localStore.getQuery(api.tasks.list, { userId });
      
      if (currentTasks !== undefined) {
        // Add optimistic task to the list
        const optimisticTask = {
          _id: crypto.randomUUID() as Id<"tasks">,
          _creationTime: Date.now(),
          title,
          userId,
          completed: false,
        };
        
        localStore.setQuery(api.tasks.list, { userId }, [
          optimisticTask,
          ...currentTasks,
        ]);
      }
    }
  );
}
```

### Cursor-Based Pagination

```typescript
// convex/messages.ts
import { query } from "./_generated/server";
import { v } from "convex/values";
import { paginationOptsValidator } from "convex/server";

export const listPaginated = query({
  args: {
    channelId: v.id("channels"),
    paginationOpts: paginationOptsValidator,
  },
  handler: async (ctx, args) => {
    return await ctx.db
      .query("messages")
      .withIndex("by_channel", (q) => q.eq("channelId", args.channelId))
      .order("desc")
      .paginate(args.paginationOpts);
  },
});
```

```typescript
// React component with pagination
import { usePaginatedQuery } from "convex/react";
import { api } from "../convex/_generated/api";

function MessageList({ channelId }: { channelId: Id<"channels"> }) {
  const { results, status, loadMore } = usePaginatedQuery(
    api.messages.listPaginated,
    { channelId },
    { initialNumItems: 20 }
  );

  return (
    <div>
      {results.map((message) => (
        <div key={message._id}>{message.content}</div>
      ))}
      
      {status === "CanLoadMore" && (
        <button onClick={() => loadMore(20)}>Load More</button>
      )}
      
      {status === "LoadingMore" && <div>Loading...</div>}
      
      {status === "Exhausted" && <div>No more messages</div>}
    </div>
  );
}
```

### Infinite Scroll Pattern

```typescript
import { usePaginatedQuery } from "convex/react";
import { useEffect, useRef } from "react";
import { api } from "../convex/_generated/api";

function InfiniteMessageList({ channelId }: { channelId: Id<"channels"> }) {
  const { results, status, loadMore } = usePaginatedQuery(
    api.messages.listPaginated,
    { channelId },
    { initialNumItems: 20 }
  );
  
  const observerRef = useRef<IntersectionObserver>();
  const loadMoreRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (observerRef.current) {
      observerRef.current.disconnect();
    }

    observerRef.current = new IntersectionObserver((entries) => {
      if (entries[0].isIntersecting && status === "CanLoadMore") {
        loadMore(20);
      }
    });

    if (loadMoreRef.current) {
      observerRef.current.observe(loadMoreRef.current);
    }

    return () => observerRef.current?.disconnect();
  }, [status, loadMore]);

  return (
    <div>
      {results.map((message) => (
        <div key={message._id}>{message.content}</div>
      ))}
      <div ref={loadMoreRef} style={{ height: 1 }} />
      {status === "LoadingMore" && <div>Loading...</div>}
    </div>
  );
}
```

### Multiple Subscriptions

```typescript
import { useQuery } from "convex/react";
import { api } from "../convex/_generated/api";

function Dashboard({ userId }: { userId: Id<"users"> }) {
  // Multiple subscriptions update independently
  const user = useQuery(api.users.get, { userId });
  const tasks = useQuery(api.tasks.list, { userId });
  const notifications = useQuery(api.notifications.unread, { userId });

  const isLoading = user === undefined || 
                    tasks === undefined || 
                    notifications === undefined;

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>Welcome, {user.name}</h1>
      <p>You have {tasks.length} tasks</p>
      <p>{notifications.length} unread notifications</p>
    </div>
  );
}
```

## Examples

### Real-time Chat Application

```typescript
// convex/messages.ts
import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

export const list = query({
  args: { channelId: v.id("channels") },
  returns: v.array(v.object({
    _id: v.id("messages"),
    _creationTime: v.number(),
    content: v.string(),
    authorId: v.id("users"),
    authorName: v.string(),
  })),
  handler: async (ctx, args) => {
    const messages = await ctx.db
      .query("messages")
      .withIndex("by_channel", (q) => q.eq("channelId", args.channelId))
      .order("desc")
      .take(100);

    // Enrich with author names
    return Promise.all(
      messages.map(async (msg) => {
        const author = await ctx.db.get(msg.authorId);
        return {
          ...msg,
          authorName: author?.name ?? "Unknown",
        };
      })
    );
  },
});

export const send = mutation({
  args: {
    channelId: v.id("channels"),
    authorId: v.id("users"),
    content: v.string(),
  },
  returns: v.id("messages"),
  handler: async (ctx, args) => {
    return await ctx.db.insert("messages", {
      channelId: args.channelId,
      authorId: args.authorId,
      content: args.content,
    });
  },
});
```

```typescript
// ChatRoom.tsx
import { useQuery, useMutation } from "convex/react";
import { api } from "../convex/_generated/api";
import { useState, useRef, useEffect } from "react";

function ChatRoom({ channelId, userId }: Props) {
  const messages = useQuery(api.messages.list, { channelId });
  const sendMessage = useMutation(api.messages.send);
  const [input, setInput] = useState("");
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Auto-scroll to bottom on new messages
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSend = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;

    await sendMessage({
      channelId,
      authorId: userId,
      content: input.trim(),
    });
    setInput("");
  };

  return (
    <div className="chat-room">
      <div className="messages">
        {messages?.map((msg) => (
          <div key={msg._id} className="message">
            <strong>{msg.authorName}:</strong> {msg.content}
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>
      
      <form onSubmit={handleSend}>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type a message..."
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}
```

## Best Practices

- Never run `npx convex deploy` unless explicitly instructed
- Never run any git commands unless explicitly instructed
- Use "skip" for conditional queries instead of conditionally calling hooks
- Implement optimistic updates for better perceived performance
- Use usePaginatedQuery for large datasets
- Handle undefined state (loading) explicitly
- Avoid unnecessary re-renders by memoizing derived data

## Common Pitfalls

1. **Conditional hook calls** - Use "skip" instead of if statements
2. **Not handling loading state** - Always check for undefined
3. **Missing optimistic update rollback** - Optimistic updates auto-rollback on error
4. **Over-fetching with pagination** - Use appropriate page sizes
5. **Ignoring subscription cleanup** - React handles this automatically

## References

- Convex Documentation: https://docs.convex.dev/
- Convex LLMs.txt: https://docs.convex.dev/llms.txt
- React Client: https://docs.convex.dev/client/react
- Optimistic Updates: https://docs.convex.dev/client/react/optimistic-updates
- Pagination: https://docs.convex.dev/database/pagination
```

## File: `skills/convex-realtime/agents/openai.yaml`
```yaml
interface:
  icon_small: "./assets/small-logo.svg"
  icon_large: "./assets/large-logo.png"
```

## File: `skills/convex-schema-validator/SKILL.md`
```markdown
---
name: convex-schema-validator
displayName: Convex Schema Validator
description: Defining and validating database schemas with proper typing, index configuration, optional fields, unions, and migration strategies for schema changes
version: 1.0.0
author: Convex
tags: [convex, schema, validation, typescript, indexes, migrations]
---

# Convex Schema Validator

Define and validate database schemas in Convex with proper typing, index configuration, optional fields, unions, and strategies for schema migrations.

## Documentation Sources

Before implementing, do not assume; fetch the latest documentation:

- Primary: https://docs.convex.dev/database/schemas
- Indexes: https://docs.convex.dev/database/indexes
- Data Types: https://docs.convex.dev/database/types
- For broader context: https://docs.convex.dev/llms.txt

## Instructions

### Basic Schema Definition

```typescript
// convex/schema.ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  users: defineTable({
    name: v.string(),
    email: v.string(),
    avatarUrl: v.optional(v.string()),
    createdAt: v.number(),
  }),
  
  tasks: defineTable({
    title: v.string(),
    description: v.optional(v.string()),
    completed: v.boolean(),
    userId: v.id("users"),
    priority: v.union(
      v.literal("low"),
      v.literal("medium"),
      v.literal("high")
    ),
  }),
});
```

### Validator Types

| Validator | TypeScript Type | Example |
|-----------|----------------|---------|
| `v.string()` | `string` | `"hello"` |
| `v.number()` | `number` | `42`, `3.14` |
| `v.boolean()` | `boolean` | `true`, `false` |
| `v.null()` | `null` | `null` |
| `v.int64()` | `bigint` | `9007199254740993n` |
| `v.bytes()` | `ArrayBuffer` | Binary data |
| `v.id("table")` | `Id<"table">` | Document reference |
| `v.array(v)` | `T[]` | `[1, 2, 3]` |
| `v.object({})` | `{ ... }` | `{ name: "..." }` |
| `v.optional(v)` | `T \| undefined` | Optional field |
| `v.union(...)` | `T1 \| T2` | Multiple types |
| `v.literal(x)` | `"x"` | Exact value |
| `v.any()` | `any` | Any value |
| `v.record(k, v)` | `Record<K, V>` | Dynamic keys |

### Index Configuration

```typescript
export default defineSchema({
  messages: defineTable({
    channelId: v.id("channels"),
    authorId: v.id("users"),
    content: v.string(),
    sentAt: v.number(),
  })
    // Single field index
    .index("by_channel", ["channelId"])
    // Compound index
    .index("by_channel_and_author", ["channelId", "authorId"])
    // Index for sorting
    .index("by_channel_and_time", ["channelId", "sentAt"]),
    
  // Full-text search index
  articles: defineTable({
    title: v.string(),
    body: v.string(),
    category: v.string(),
  })
    .searchIndex("search_content", {
      searchField: "body",
      filterFields: ["category"],
    }),
});
```

### Complex Types

```typescript
export default defineSchema({
  // Nested objects
  profiles: defineTable({
    userId: v.id("users"),
    settings: v.object({
      theme: v.union(v.literal("light"), v.literal("dark")),
      notifications: v.object({
        email: v.boolean(),
        push: v.boolean(),
      }),
    }),
  }),

  // Arrays of objects
  orders: defineTable({
    customerId: v.id("users"),
    items: v.array(v.object({
      productId: v.id("products"),
      quantity: v.number(),
      price: v.number(),
    })),
    status: v.union(
      v.literal("pending"),
      v.literal("processing"),
      v.literal("shipped"),
      v.literal("delivered")
    ),
  }),

  // Record type for dynamic keys
  analytics: defineTable({
    date: v.string(),
    metrics: v.record(v.string(), v.number()),
  }),
});
```

### Discriminated Unions

```typescript
export default defineSchema({
  events: defineTable(
    v.union(
      v.object({
        type: v.literal("user_signup"),
        userId: v.id("users"),
        email: v.string(),
      }),
      v.object({
        type: v.literal("purchase"),
        userId: v.id("users"),
        orderId: v.id("orders"),
        amount: v.number(),
      }),
      v.object({
        type: v.literal("page_view"),
        sessionId: v.string(),
        path: v.string(),
      })
    )
  ).index("by_type", ["type"]),
});
```

### Optional vs Nullable Fields

```typescript
export default defineSchema({
  items: defineTable({
    // Optional: field may not exist
    description: v.optional(v.string()),
    
    // Nullable: field exists but can be null
    deletedAt: v.union(v.number(), v.null()),
    
    // Optional and nullable
    notes: v.optional(v.union(v.string(), v.null())),
  }),
});
```

### Index Naming Convention

Always include all indexed fields in the index name:

```typescript
export default defineSchema({
  posts: defineTable({
    authorId: v.id("users"),
    categoryId: v.id("categories"),
    publishedAt: v.number(),
    status: v.string(),
  })
    // Good: descriptive names
    .index("by_author", ["authorId"])
    .index("by_author_and_category", ["authorId", "categoryId"])
    .index("by_category_and_status", ["categoryId", "status"])
    .index("by_status_and_published", ["status", "publishedAt"]),
});
```

### Schema Migration Strategies

#### Adding New Fields

```typescript
// Before
users: defineTable({
  name: v.string(),
  email: v.string(),
})

// After - add as optional first
users: defineTable({
  name: v.string(),
  email: v.string(),
  avatarUrl: v.optional(v.string()), // New optional field
})
```

#### Backfilling Data

```typescript
// convex/migrations.ts
import { internalMutation } from "./_generated/server";
import { v } from "convex/values";

export const backfillAvatars = internalMutation({
  args: {},
  returns: v.number(),
  handler: async (ctx) => {
    const users = await ctx.db
      .query("users")
      .filter((q) => q.eq(q.field("avatarUrl"), undefined))
      .take(100);

    for (const user of users) {
      await ctx.db.patch(user._id, {
        avatarUrl: `https://api.dicebear.com/7.x/initials/svg?seed=${user.name}`,
      });
    }

    return users.length;
  },
});
```

#### Making Optional Fields Required

```typescript
// Step 1: Backfill all null values
// Step 2: Update schema to required
users: defineTable({
  name: v.string(),
  email: v.string(),
  avatarUrl: v.string(), // Now required after backfill
})
```

## Examples

### Complete E-commerce Schema

```typescript
// convex/schema.ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  users: defineTable({
    email: v.string(),
    name: v.string(),
    role: v.union(v.literal("customer"), v.literal("admin")),
    createdAt: v.number(),
  })
    .index("by_email", ["email"])
    .index("by_role", ["role"]),

  products: defineTable({
    name: v.string(),
    description: v.string(),
    price: v.number(),
    category: v.string(),
    inventory: v.number(),
    isActive: v.boolean(),
  })
    .index("by_category", ["category"])
    .index("by_active_and_category", ["isActive", "category"])
    .searchIndex("search_products", {
      searchField: "name",
      filterFields: ["category", "isActive"],
    }),

  orders: defineTable({
    userId: v.id("users"),
    items: v.array(v.object({
      productId: v.id("products"),
      quantity: v.number(),
      priceAtPurchase: v.number(),
    })),
    total: v.number(),
    status: v.union(
      v.literal("pending"),
      v.literal("paid"),
      v.literal("shipped"),
      v.literal("delivered"),
      v.literal("cancelled")
    ),
    shippingAddress: v.object({
      street: v.string(),
      city: v.string(),
      state: v.string(),
      zip: v.string(),
      country: v.string(),
    }),
    createdAt: v.number(),
    updatedAt: v.number(),
  })
    .index("by_user", ["userId"])
    .index("by_user_and_status", ["userId", "status"])
    .index("by_status", ["status"]),

  reviews: defineTable({
    productId: v.id("products"),
    userId: v.id("users"),
    rating: v.number(),
    comment: v.optional(v.string()),
    createdAt: v.number(),
  })
    .index("by_product", ["productId"])
    .index("by_user", ["userId"]),
});
```

### Using Schema Types in Functions

```typescript
// convex/products.ts
import { query, mutation } from "./_generated/server";
import { v } from "convex/values";
import { Doc, Id } from "./_generated/dataModel";

// Use Doc type for full documents
type Product = Doc<"products">;

// Use Id type for references
type ProductId = Id<"products">;

export const get = query({
  args: { productId: v.id("products") },
  returns: v.union(
    v.object({
      _id: v.id("products"),
      _creationTime: v.number(),
      name: v.string(),
      description: v.string(),
      price: v.number(),
      category: v.string(),
      inventory: v.number(),
      isActive: v.boolean(),
    }),
    v.null()
  ),
  handler: async (ctx, args): Promise<Product | null> => {
    return await ctx.db.get(args.productId);
  },
});
```

## Best Practices

- Never run `npx convex deploy` unless explicitly instructed
- Never run any git commands unless explicitly instructed
- Always define explicit schemas rather than relying on inference
- Use descriptive index names that include all indexed fields
- Start with optional fields when adding new columns
- Use discriminated unions for polymorphic data
- Validate data at the schema level, not just in functions
- Plan index strategy based on query patterns

## Common Pitfalls

1. **Missing indexes for queries** - Every withIndex needs a corresponding schema index
2. **Wrong index field order** - Fields must be queried in order defined
3. **Using v.any() excessively** - Lose type safety benefits
4. **Not making new fields optional** - Breaks existing data
5. **Forgetting system fields** - _id and _creationTime are automatic

## References

- Convex Documentation: https://docs.convex.dev/
- Convex LLMs.txt: https://docs.convex.dev/llms.txt
- Schemas: https://docs.convex.dev/database/schemas
- Indexes: https://docs.convex.dev/database/indexes
- Data Types: https://docs.convex.dev/database/types
```

## File: `skills/convex-schema-validator/agents/openai.yaml`
```yaml
interface:
  icon_small: "./assets/small-logo.svg"
  icon_large: "./assets/large-logo.png"
```

## File: `skills/convex-security-audit/SKILL.md`
```markdown
---
name: convex-security-audit
displayName: Convex Security Audit
description: Deep security review patterns for authorization logic, data access boundaries, action isolation, rate limiting, and protecting sensitive operations
version: 1.0.0
author: Convex
tags: [convex, security, audit, authorization, rate-limiting, protection]
---

# Convex Security Audit

Comprehensive security review patterns for Convex applications including authorization logic, data access boundaries, action isolation, rate limiting, and protecting sensitive operations.

## Documentation Sources

Before implementing, do not assume; fetch the latest documentation:

- Primary: https://docs.convex.dev/auth/functions-auth
- Production Security: https://docs.convex.dev/production
- For broader context: https://docs.convex.dev/llms.txt

## Instructions

### Security Audit Areas

1. **Authorization Logic** - Who can do what
2. **Data Access Boundaries** - What data users can see
3. **Action Isolation** - Protecting external API calls
4. **Rate Limiting** - Preventing abuse
5. **Sensitive Operations** - Protecting critical functions

### Authorization Logic Audit

#### Role-Based Access Control (RBAC)

```typescript
// convex/lib/auth.ts
import { QueryCtx, MutationCtx } from "./_generated/server";
import { ConvexError } from "convex/values";
import { Doc } from "./_generated/dataModel";

type UserRole = "user" | "moderator" | "admin" | "superadmin";

const roleHierarchy: Record<UserRole, number> = {
  user: 0,
  moderator: 1,
  admin: 2,
  superadmin: 3,
};

export async function getUser(ctx: QueryCtx | MutationCtx): Promise<Doc<"users"> | null> {
  const identity = await ctx.auth.getUserIdentity();
  if (!identity) return null;
  
  return await ctx.db
    .query("users")
    .withIndex("by_tokenIdentifier", (q) => 
      q.eq("tokenIdentifier", identity.tokenIdentifier)
    )
    .unique();
}

export async function requireRole(
  ctx: QueryCtx | MutationCtx, 
  minRole: UserRole
): Promise<Doc<"users">> {
  const user = await getUser(ctx);
  
  if (!user) {
    throw new ConvexError({
      code: "UNAUTHENTICATED",
      message: "Authentication required",
    });
  }
  
  const userRoleLevel = roleHierarchy[user.role as UserRole] ?? 0;
  const requiredLevel = roleHierarchy[minRole];
  
  if (userRoleLevel < requiredLevel) {
    throw new ConvexError({
      code: "FORBIDDEN",
      message: `Role '${minRole}' or higher required`,
    });
  }
  
  return user;
}

// Permission-based check
type Permission = "read:users" | "write:users" | "delete:users" | "admin:system";

const rolePermissions: Record<UserRole, Permission[]> = {
  user: ["read:users"],
  moderator: ["read:users", "write:users"],
  admin: ["read:users", "write:users", "delete:users"],
  superadmin: ["read:users", "write:users", "delete:users", "admin:system"],
};

export async function requirePermission(
  ctx: QueryCtx | MutationCtx,
  permission: Permission
): Promise<Doc<"users">> {
  const user = await getUser(ctx);
  
  if (!user) {
    throw new ConvexError({ code: "UNAUTHENTICATED", message: "Authentication required" });
  }
  
  const userRole = user.role as UserRole;
  const permissions = rolePermissions[userRole] ?? [];
  
  if (!permissions.includes(permission)) {
    throw new ConvexError({
      code: "FORBIDDEN",
      message: `Permission '${permission}' required`,
    });
  }
  
  return user;
}
```

### Data Access Boundaries Audit

```typescript
// convex/data.ts
import { query, mutation } from "./_generated/server";
import { v } from "convex/values";
import { getUser, requireRole } from "./lib/auth";
import { ConvexError } from "convex/values";

// Audit: Users can only see their own data
export const getMyData = query({
  args: {},
  returns: v.array(v.object({
    _id: v.id("userData"),
    content: v.string(),
  })),
  handler: async (ctx) => {
    const user = await getUser(ctx);
    if (!user) return [];
    
    // SECURITY: Filter by userId
    return await ctx.db
      .query("userData")
      .withIndex("by_user", (q) => q.eq("userId", user._id))
      .collect();
  },
});

// Audit: Verify ownership before returning sensitive data
export const getSensitiveItem = query({
  args: { itemId: v.id("sensitiveItems") },
  returns: v.union(v.object({
    _id: v.id("sensitiveItems"),
    secret: v.string(),
  }), v.null()),
  handler: async (ctx, args) => {
    const user = await getUser(ctx);
    if (!user) return null;
    
    const item = await ctx.db.get(args.itemId);
    
    // SECURITY: Verify ownership
    if (!item || item.ownerId !== user._id) {
      return null; // Don't reveal if item exists
    }
    
    return item;
  },
});

// Audit: Shared resources with access list
export const getSharedDocument = query({
  args: { docId: v.id("documents") },
  returns: v.union(v.object({
    _id: v.id("documents"),
    content: v.string(),
    accessLevel: v.string(),
  }), v.null()),
  handler: async (ctx, args) => {
    const user = await getUser(ctx);
    const doc = await ctx.db.get(args.docId);
    
    if (!doc) return null;
    
    // Public documents
    if (doc.visibility === "public") {
      return { ...doc, accessLevel: "public" };
    }
    
    // Must be authenticated for non-public
    if (!user) return null;
    
    // Owner has full access
    if (doc.ownerId === user._id) {
      return { ...doc, accessLevel: "owner" };
    }
    
    // Check shared access
    const access = await ctx.db
      .query("documentAccess")
      .withIndex("by_doc_and_user", (q) => 
        q.eq("documentId", args.docId).eq("userId", user._id)
      )
      .unique();
    
    if (!access) return null;
    
    return { ...doc, accessLevel: access.level };
  },
});
```

### Action Isolation Audit

```typescript
// convex/actions.ts
"use node";

import { action, internalAction } from "./_generated/server";
import { v } from "convex/values";
import { api, internal } from "./_generated/api";
import { ConvexError } from "convex/values";

// SECURITY: Never expose API keys in responses
export const callExternalAPI = action({
  args: { query: v.string() },
  returns: v.object({ result: v.string() }),
  handler: async (ctx, args) => {
    // Verify user is authenticated
    const identity = await ctx.auth.getUserIdentity();
    if (!identity) {
      throw new ConvexError("Authentication required");
    }
    
    // Get API key from environment (not hardcoded)
    const apiKey = process.env.EXTERNAL_API_KEY;
    if (!apiKey) {
      throw new Error("API key not configured");
    }
    
    // Log usage for audit trail
    await ctx.runMutation(internal.audit.logAPICall, {
      userId: identity.tokenIdentifier,
      endpoint: "external-api",
      timestamp: Date.now(),
    });
    
    const response = await fetch("https://api.example.com/query", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${apiKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query: args.query }),
    });
    
    if (!response.ok) {
      // Don't expose external API error details
      throw new ConvexError("External service unavailable");
    }
    
    const data = await response.json();
    
    // Sanitize response before returning
    return { result: sanitizeResponse(data) };
  },
});

// Internal action - not exposed to clients
export const _processPayment = internalAction({
  args: {
    userId: v.id("users"),
    amount: v.number(),
    paymentMethodId: v.string(),
  },
  returns: v.object({ success: v.boolean(), transactionId: v.optional(v.string()) }),
  handler: async (ctx, args) => {
    const stripeKey = process.env.STRIPE_SECRET_KEY;
    
    // Process payment with Stripe
    // This should NEVER be exposed as a public action
    
    return { success: true, transactionId: "txn_xxx" };
  },
});
```

### Rate Limiting Audit

```typescript
// convex/rateLimit.ts
import { mutation, query } from "./_generated/server";
import { v } from "convex/values";
import { ConvexError } from "convex/values";

const RATE_LIMITS = {
  message: { requests: 10, windowMs: 60000 }, // 10 per minute
  upload: { requests: 5, windowMs: 300000 },  // 5 per 5 minutes
  api: { requests: 100, windowMs: 3600000 },  // 100 per hour
};

export const checkRateLimit = mutation({
  args: {
    userId: v.string(),
    action: v.union(v.literal("message"), v.literal("upload"), v.literal("api")),
  },
  returns: v.object({ allowed: v.boolean(), retryAfter: v.optional(v.number()) }),
  handler: async (ctx, args) => {
    const limit = RATE_LIMITS[args.action];
    const now = Date.now();
    const windowStart = now - limit.windowMs;
    
    // Count requests in window
    const requests = await ctx.db
      .query("rateLimits")
      .withIndex("by_user_and_action", (q) => 
        q.eq("userId", args.userId).eq("action", args.action)
      )
      .filter((q) => q.gt(q.field("timestamp"), windowStart))
      .collect();
    
    if (requests.length >= limit.requests) {
      const oldestRequest = requests[0];
      const retryAfter = oldestRequest.timestamp + limit.windowMs - now;
      
      return { allowed: false, retryAfter };
    }
    
    // Record this request
    await ctx.db.insert("rateLimits", {
      userId: args.userId,
      action: args.action,
      timestamp: now,
    });
    
    return { allowed: true };
  },
});

// Use in mutations
export const sendMessage = mutation({
  args: { content: v.string() },
  returns: v.id("messages"),
  handler: async (ctx, args) => {
    const identity = await ctx.auth.getUserIdentity();
    if (!identity) throw new ConvexError("Authentication required");
    
    // Check rate limit
    const rateCheck = await checkRateLimit(ctx, {
      userId: identity.tokenIdentifier,
      action: "message",
    });
    
    if (!rateCheck.allowed) {
      throw new ConvexError({
        code: "RATE_LIMITED",
        message: `Too many requests. Try again in ${Math.ceil(rateCheck.retryAfter! / 1000)} seconds`,
      });
    }
    
    return await ctx.db.insert("messages", {
      content: args.content,
      authorId: identity.tokenIdentifier,
      createdAt: Date.now(),
    });
  },
});
```

### Sensitive Operations Protection

```typescript
// convex/admin.ts
import { mutation, internalMutation } from "./_generated/server";
import { v } from "convex/values";
import { requireRole, requirePermission } from "./lib/auth";
import { internal } from "./_generated/api";

// Two-factor confirmation for dangerous operations
export const deleteAllUserData = mutation({
  args: {
    userId: v.id("users"),
    confirmationCode: v.string(),
  },
  returns: v.null(),
  handler: async (ctx, args) => {
    // Require superadmin
    const admin = await requireRole(ctx, "superadmin");
    
    // Verify confirmation code
    const confirmation = await ctx.db
      .query("confirmations")
      .withIndex("by_admin_and_code", (q) => 
        q.eq("adminId", admin._id).eq("code", args.confirmationCode)
      )
      .filter((q) => q.gt(q.field("expiresAt"), Date.now()))
      .unique();
    
    if (!confirmation || confirmation.action !== "delete_user_data") {
      throw new ConvexError("Invalid or expired confirmation code");
    }
    
    // Delete confirmation to prevent reuse
    await ctx.db.delete(confirmation._id);
    
    // Schedule deletion (don't do it inline)
    await ctx.scheduler.runAfter(0, internal.admin._performDeletion, {
      userId: args.userId,
      requestedBy: admin._id,
    });
    
    // Audit log
    await ctx.db.insert("auditLogs", {
      action: "delete_user_data",
      targetUserId: args.userId,
      performedBy: admin._id,
      timestamp: Date.now(),
    });
    
    return null;
  },
});

// Generate confirmation code for sensitive action
export const requestDeletionConfirmation = mutation({
  args: { userId: v.id("users") },
  returns: v.string(),
  handler: async (ctx, args) => {
    const admin = await requireRole(ctx, "superadmin");
    
    const code = generateSecureCode();
    
    await ctx.db.insert("confirmations", {
      adminId: admin._id,
      code,
      action: "delete_user_data",
      targetUserId: args.userId,
      expiresAt: Date.now() + 5 * 60 * 1000, // 5 minutes
    });
    
    // In production, send code via secure channel (email, SMS)
    return code;
  },
});
```

## Examples

### Complete Audit Trail System

```typescript
// convex/audit.ts
import { mutation, query, internalMutation } from "./_generated/server";
import { v } from "convex/values";
import { getUser, requireRole } from "./lib/auth";

const auditEventValidator = v.object({
  _id: v.id("auditLogs"),
  _creationTime: v.number(),
  action: v.string(),
  userId: v.optional(v.string()),
  resourceType: v.string(),
  resourceId: v.string(),
  details: v.optional(v.any()),
  ipAddress: v.optional(v.string()),
  timestamp: v.number(),
});

// Internal: Log audit event
export const logEvent = internalMutation({
  args: {
    action: v.string(),
    userId: v.optional(v.string()),
    resourceType: v.string(),
    resourceId: v.string(),
    details: v.optional(v.any()),
  },
  returns: v.id("auditLogs"),
  handler: async (ctx, args) => {
    return await ctx.db.insert("auditLogs", {
      ...args,
      timestamp: Date.now(),
    });
  },
});

// Admin: View audit logs
export const getAuditLogs = query({
  args: {
    resourceType: v.optional(v.string()),
    userId: v.optional(v.string()),
    limit: v.optional(v.number()),
  },
  returns: v.array(auditEventValidator),
  handler: async (ctx, args) => {
    await requireRole(ctx, "admin");
    
    let query = ctx.db.query("auditLogs");
    
    if (args.resourceType) {
      query = query.withIndex("by_resource_type", (q) => 
        q.eq("resourceType", args.resourceType)
      );
    }
    
    return await query
      .order("desc")
      .take(args.limit ?? 100);
  },
});
```

## Best Practices

- Never run `npx convex deploy` unless explicitly instructed
- Never run any git commands unless explicitly instructed
- Implement defense in depth (multiple security layers)
- Log all sensitive operations for audit trails
- Use confirmation codes for destructive actions
- Rate limit all user-facing endpoints
- Never expose internal API keys or errors
- Review access patterns regularly

## Common Pitfalls

1. **Single point of failure** - Implement multiple auth checks
2. **Missing audit logs** - Log all sensitive operations
3. **Trusting client data** - Always validate server-side
4. **Exposing error details** - Sanitize error messages
5. **No rate limiting** - Always implement rate limits

## References

- Convex Documentation: https://docs.convex.dev/
- Convex LLMs.txt: https://docs.convex.dev/llms.txt
- Functions Auth: https://docs.convex.dev/auth/functions-auth
- Production Security: https://docs.convex.dev/production
```

## File: `skills/convex-security-audit/agents/openai.yaml`
```yaml
interface:
  icon_small: "./assets/small-logo.svg"
  icon_large: "./assets/large-logo.png"
```

## File: `skills/convex-security-check/SKILL.md`
```markdown
---
name: convex-security-check
displayName: Convex Security Check
description: Quick security audit checklist covering authentication, function exposure, argument validation, row-level access control, and environment variable handling
version: 1.0.0
author: Convex
tags: [convex, security, authentication, authorization, checklist]
---

# Convex Security Check

A quick security audit checklist for Convex applications covering authentication, function exposure, argument validation, row-level access control, and environment variable handling.

## Documentation Sources

Before implementing, do not assume; fetch the latest documentation:

- Primary: https://docs.convex.dev/auth
- Production Security: https://docs.convex.dev/production
- Functions Auth: https://docs.convex.dev/auth/functions-auth
- For broader context: https://docs.convex.dev/llms.txt

## Instructions

### Security Checklist

Use this checklist to quickly audit your Convex application's security:

#### 1. Authentication

- [ ] Authentication provider configured (Clerk, Auth0, etc.)
- [ ] All sensitive queries check `ctx.auth.getUserIdentity()`
- [ ] Unauthenticated access explicitly allowed where intended
- [ ] Session tokens properly validated

#### 2. Function Exposure

- [ ] Public functions (`query`, `mutation`, `action`) reviewed
- [ ] Internal functions use `internalQuery`, `internalMutation`, `internalAction`
- [ ] No sensitive operations exposed as public functions
- [ ] HTTP actions validate origin/authentication

#### 3. Argument Validation

- [ ] All functions have explicit `args` validators
- [ ] All functions have explicit `returns` validators
- [ ] No `v.any()` used for sensitive data
- [ ] ID validators use correct table names

#### 4. Row-Level Access Control

- [ ] Users can only access their own data
- [ ] Admin functions check user roles
- [ ] Shared resources have proper access checks
- [ ] Deletion functions verify ownership

#### 5. Environment Variables

- [ ] API keys stored in environment variables
- [ ] No secrets in code or schema
- [ ] Different keys for dev/prod environments
- [ ] Environment variables accessed only in actions

### Authentication Check

```typescript
// convex/auth.ts
import { query, mutation } from "./_generated/server";
import { v } from "convex/values";
import { ConvexError } from "convex/values";

// Helper to require authentication
async function requireAuth(ctx: QueryCtx | MutationCtx) {
  const identity = await ctx.auth.getUserIdentity();
  if (!identity) {
    throw new ConvexError("Authentication required");
  }
  return identity;
}

// Secure query pattern
export const getMyProfile = query({
  args: {},
  returns: v.union(v.object({
    _id: v.id("users"),
    name: v.string(),
    email: v.string(),
  }), v.null()),
  handler: async (ctx) => {
    const identity = await requireAuth(ctx);
    
    return await ctx.db
      .query("users")
      .withIndex("by_tokenIdentifier", (q) => 
        q.eq("tokenIdentifier", identity.tokenIdentifier)
      )
      .unique();
  },
});
```

### Function Exposure Check

```typescript
// PUBLIC - Exposed to clients (review carefully!)
export const listPublicPosts = query({
  args: {},
  returns: v.array(v.object({ /* ... */ })),
  handler: async (ctx) => {
    // Anyone can call this - intentionally public
    return await ctx.db
      .query("posts")
      .withIndex("by_public", (q) => q.eq("isPublic", true))
      .collect();
  },
});

// INTERNAL - Only callable from other Convex functions
export const _updateUserCredits = internalMutation({
  args: { userId: v.id("users"), amount: v.number() },
  returns: v.null(),
  handler: async (ctx, args) => {
    // This cannot be called directly from clients
    await ctx.db.patch(args.userId, {
      credits: args.amount,
    });
    return null;
  },
});
```

### Argument Validation Check

```typescript
// GOOD: Strict validation
export const createPost = mutation({
  args: {
    title: v.string(),
    content: v.string(),
    category: v.union(
      v.literal("tech"),
      v.literal("news"),
      v.literal("other")
    ),
  },
  returns: v.id("posts"),
  handler: async (ctx, args) => {
    const identity = await requireAuth(ctx);
    return await ctx.db.insert("posts", {
      ...args,
      authorId: identity.tokenIdentifier,
    });
  },
});

// BAD: Weak validation
export const createPostUnsafe = mutation({
  args: {
    data: v.any(), // DANGEROUS: Allows any data
  },
  returns: v.id("posts"),
  handler: async (ctx, args) => {
    return await ctx.db.insert("posts", args.data);
  },
});
```

### Row-Level Access Control Check

```typescript
// Verify ownership before update
export const updateTask = mutation({
  args: {
    taskId: v.id("tasks"),
    title: v.string(),
  },
  returns: v.null(),
  handler: async (ctx, args) => {
    const identity = await requireAuth(ctx);
    
    const task = await ctx.db.get(args.taskId);
    
    // Check ownership
    if (!task || task.userId !== identity.tokenIdentifier) {
      throw new ConvexError("Not authorized to update this task");
    }
    
    await ctx.db.patch(args.taskId, { title: args.title });
    return null;
  },
});

// Verify ownership before delete
export const deleteTask = mutation({
  args: { taskId: v.id("tasks") },
  returns: v.null(),
  handler: async (ctx, args) => {
    const identity = await requireAuth(ctx);
    
    const task = await ctx.db.get(args.taskId);
    
    if (!task || task.userId !== identity.tokenIdentifier) {
      throw new ConvexError("Not authorized to delete this task");
    }
    
    await ctx.db.delete(args.taskId);
    return null;
  },
});
```

### Environment Variables Check

```typescript
// convex/actions.ts
"use node";

import { action } from "./_generated/server";
import { v } from "convex/values";

export const sendEmail = action({
  args: {
    to: v.string(),
    subject: v.string(),
    body: v.string(),
  },
  returns: v.object({ success: v.boolean() }),
  handler: async (ctx, args) => {
    // Access API key from environment
    const apiKey = process.env.RESEND_API_KEY;
    
    if (!apiKey) {
      throw new Error("RESEND_API_KEY not configured");
    }
    
    const response = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${apiKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        from: "noreply@example.com",
        to: args.to,
        subject: args.subject,
        html: args.body,
      }),
    });
    
    return { success: response.ok };
  },
});
```

## Examples

### Complete Security Pattern

```typescript
// convex/secure.ts
import { query, mutation, internalMutation } from "./_generated/server";
import { v } from "convex/values";
import { ConvexError } from "convex/values";

// Authentication helper
async function getAuthenticatedUser(ctx: QueryCtx | MutationCtx) {
  const identity = await ctx.auth.getUserIdentity();
  if (!identity) {
    throw new ConvexError({
      code: "UNAUTHENTICATED",
      message: "You must be logged in",
    });
  }
  
  const user = await ctx.db
    .query("users")
    .withIndex("by_tokenIdentifier", (q) => 
      q.eq("tokenIdentifier", identity.tokenIdentifier)
    )
    .unique();
    
  if (!user) {
    throw new ConvexError({
      code: "USER_NOT_FOUND",
      message: "User profile not found",
    });
  }
  
  return user;
}

// Check admin role
async function requireAdmin(ctx: QueryCtx | MutationCtx) {
  const user = await getAuthenticatedUser(ctx);
  
  if (user.role !== "admin") {
    throw new ConvexError({
      code: "FORBIDDEN",
      message: "Admin access required",
    });
  }
  
  return user;
}

// Public: List own tasks
export const listMyTasks = query({
  args: {},
  returns: v.array(v.object({
    _id: v.id("tasks"),
    title: v.string(),
    completed: v.boolean(),
  })),
  handler: async (ctx) => {
    const user = await getAuthenticatedUser(ctx);
    
    return await ctx.db
      .query("tasks")
      .withIndex("by_user", (q) => q.eq("userId", user._id))
      .collect();
  },
});

// Admin only: List all users
export const listAllUsers = query({
  args: {},
  returns: v.array(v.object({
    _id: v.id("users"),
    name: v.string(),
    role: v.string(),
  })),
  handler: async (ctx) => {
    await requireAdmin(ctx);
    
    return await ctx.db.query("users").collect();
  },
});

// Internal: Update user role (never exposed)
export const _setUserRole = internalMutation({
  args: {
    userId: v.id("users"),
    role: v.union(v.literal("user"), v.literal("admin")),
  },
  returns: v.null(),
  handler: async (ctx, args) => {
    await ctx.db.patch(args.userId, { role: args.role });
    return null;
  },
});
```

## Best Practices

- Never run `npx convex deploy` unless explicitly instructed
- Never run any git commands unless explicitly instructed
- Always verify user identity before returning sensitive data
- Use internal functions for sensitive operations
- Validate all arguments with strict validators
- Check ownership before update/delete operations
- Store API keys in environment variables
- Review all public functions for security implications

## Common Pitfalls

1. **Missing authentication checks** - Always verify identity
2. **Exposing internal operations** - Use internalMutation/Query
3. **Trusting client-provided IDs** - Verify ownership
4. **Using v.any() for arguments** - Use specific validators
5. **Hardcoding secrets** - Use environment variables

## References

- Convex Documentation: https://docs.convex.dev/
- Convex LLMs.txt: https://docs.convex.dev/llms.txt
- Authentication: https://docs.convex.dev/auth
- Production Security: https://docs.convex.dev/production
- Functions Auth: https://docs.convex.dev/auth/functions-auth
```

## File: `skills/convex-security-check/agents/openai.yaml`
```yaml
interface:
  icon_small: "./assets/small-logo.svg"
  icon_large: "./assets/large-logo.png"
```

## File: `templates/CLAUDE.md`
```markdown
# Project Context

[Project Name] - [Brief description of what this project does]

Built with: Convex (backend), [React/Next.js/Vue/etc.] (frontend)

## Bash Commands

```bash
# Development
npx convex dev              # Start dev server (watches files, syncs to cloud)
npx convex dev --once       # Single sync without watching
npx convex dev --local      # Local development (no cloud)

# Deployment
npx convex deploy           # Deploy to production
npx convex deploy --cmd "npm run build"  # Deploy with frontend build

# Running Functions
npx convex run messages:send '{"body": "hello"}'  # Run with args
npx convex run myQuery --watch                     # Watch query results

# Data Management
npx convex data                          # List tables
npx convex data messages --limit 50      # View table data
npx convex import --table tableName path/to/data.json
npx convex export --path ./backup

# Environment Variables
npx convex env list
npx convex env set API_KEY "secret123"

# Utilities
npx convex dashboard        # Open dashboard
npx convex logs             # View logs
npx convex codegen          # Regenerate types
```

## File Structure

```
convex/
├── _generated/           # Auto-generated (DO NOT EDIT, commit to git)
│   ├── api.d.ts         # API types
│   ├── dataModel.d.ts   # Database types (Doc<>, Id<>)
│   └── server.d.ts      # Server types
├── schema.ts            # Database schema definition (required)
├── http.ts              # HTTP actions router (exact name required)
├── crons.ts             # Cron job definitions
├── auth.config.ts       # Auth configuration
└── [feature].ts         # Functions → api.[feature].*
```

## Code Style

### Function Types - Use the Right One

```typescript
// QUERY: Read-only, reactive, cached. Use for fetching data.
export const list = query({
  args: { limit: v.optional(v.number()) },
  returns: v.array(
    v.object({
      /* ... */
    }),
  ),
  handler: async (ctx, args) => {
    return await ctx.db.query("items").take(args.limit ?? 10);
  },
});

// MUTATION: Write operations. Transactional, atomic.
export const create = mutation({
  args: { text: v.string() },
  returns: v.id("items"),
  handler: async (ctx, args) => {
    return await ctx.db.insert("items", { text: args.text });
  },
});

// ACTION: External API calls. NOT auto-retried, NOT transactional.
export const processExternal = action({
  args: { id: v.id("items") },
  handler: async (ctx, args) => {
    const data = await ctx.runQuery(internal.items.get, { id: args.id });
    const result = await fetch("https://api.example.com", {
      /* ... */
    });
    await ctx.runMutation(internal.items.saveResult, {
      /* ... */
    });
  },
});
```

### Schema Patterns

```typescript
// convex/schema.ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  users: defineTable({
    name: v.string(),
    email: v.string(),
    role: v.union(v.literal("admin"), v.literal("user")),
    profileId: v.optional(v.id("profiles")),
  })
    .index("by_email", ["email"])
    .index("by_role", ["role"]),

  posts: defineTable({
    authorId: v.id("users"),
    title: v.string(),
    status: v.union(v.literal("draft"), v.literal("published")),
    tags: v.array(v.string()),
  })
    .index("by_author", ["authorId"])
    .index("by_author_status", ["authorId", "status"]),
});
```

### Validator Reference

```typescript
// Primitives
v.string()              v.number()              v.boolean()
v.int64()               v.bytes()               v.null()

// Complex
v.id("tableName")       v.array(v.string())     v.object({ key: v.string() })
v.record(v.string(), v.number())

// Modifiers
v.optional(v.string())  // Field may be missing
v.nullable(v.string())  // Shorthand for v.union(v.string(), v.null())
v.union(v.literal("a"), v.literal("b"))  // Enum-like
v.any()                 // Escape hatch
```

### Index Queries - ALWAYS use for large tables

```typescript
// ✅ GOOD: Uses index
const posts = await ctx.db
  .query("posts")
  .withIndex("by_author", (q) => q.eq("authorId", userId))
  .collect();

// ❌ BAD: Full table scan on large tables
const posts = await ctx.db
  .query("posts")
  .filter((q) => q.eq(q.field("authorId"), userId))
  .collect();
```

### Authentication Pattern

```typescript
export const myMutation = mutation({
  args: {
    /* ... */
  },
  handler: async (ctx, args) => {
    const identity = await ctx.auth.getUserIdentity();
    if (!identity) throw new Error("Unauthenticated");
    // identity.tokenIdentifier is the unique user ID
  },
});
```

### Scheduling Pattern

```typescript
// Schedule for later - ALWAYS use internal functions
await ctx.scheduler.runAfter(5000, internal.messages.process, { id });
await ctx.scheduler.runAt(timestamp, internal.tasks.execute, { id });

// Cron jobs (convex/crons.ts)
const crons = cronJobs();
crons.interval("cleanup", { minutes: 5 }, internal.tasks.cleanup);
crons.daily("digest", { hourUTC: 9, minuteUTC: 0 }, internal.emails.send);
export default crons;
```

### File Storage Pattern

```typescript
// Generate upload URL (mutation)
export const generateUploadUrl = mutation({
  handler: async (ctx) => await ctx.storage.generateUploadUrl(),
});

// Get file URL (query)
export const getUrl = query({
  args: { storageId: v.id("_storage") },
  handler: async (ctx, { storageId }) => await ctx.storage.getUrl(storageId),
});
```

## Linting

This project uses @convex-dev/eslint-plugin for code quality. All Convex functions must:

1. **Use object syntax** with `handler` property (not bare functions)
2. **Include argument validators** - always have `args: {}` even when empty
3. **Use explicit table names** - `db.get("table", id)` not `db.get(id)`
4. **Respect runtime boundaries** - don't import "use node" files into Convex runtime

Run `npx eslint convex/` to check compliance.

## IMPORTANT Rules

1. **ALWAYS validate arguments** on public functions with `v` validators
2. **ALWAYS check authentication** before sensitive operations
3. **ALWAYS use `.withIndex()` on large tables** (1000+ docs), not `.filter()`
4. **ALWAYS await promises** - unawaited promises fail silently
5. **ALWAYS use `internal.` for scheduled functions**, never `api.`
6. **NEVER call external APIs from queries/mutations** - use actions
7. **NEVER use `undefined` as a value** - use `null` instead
8. **NEVER store relationships in arrays** - use separate tables with IDs
9. **PREFER queries/mutations over actions** - actions aren't cached or retried

## Common Gotchas

- `undefined` patches REMOVE the field: `ctx.db.patch(id, { field: undefined })`
- Query returns `undefined` while loading - use this for loading states
- Actions are NOT automatically retried on failure
- `_creationTime` is auto-appended to all indexes
- Max 8192 array elements, 1MB doc size, 16 nesting levels
- Circular imports cause undefined validators - watch for import cycles
- System tables: `_storage`, `_scheduled_functions` (query via `ctx.db.system`)

## Testing

```bash
npm run test               # Run all tests
npx convex dev --local     # Use local backend for testing
```

Prefer testing with real Convex backend over mocks when possible.

## Project-Specific Notes

[Add any project-specific conventions, business logic notes, or architecture decisions here]

## Quick Reference

### Function Type Decision Tree

```
Need to read data? → query()
Need to write data? → mutation()
Need external API? → action()
Server-only function? → internal*()
HTTP webhook/API? → httpAction()
```

### Validator Cheat Sheet

```typescript
v.string(); // string
v.number(); // number (float64)
v.boolean(); // boolean
v.id("table"); // Id<"table">
v.null(); // null
v.optional(v.string()); // string | undefined (field can be missing)
v.nullable(v.string()); // string | null (field must exist)
v.array(v.string()); // string[]
v.object({ k: v.string() }); // { k: string }
v.union(v.literal("a"), v.literal("b")); // "a" | "b"
v.record(v.string(), v.number()); // { [key: string]: number }
```

### Import Patterns

```typescript
// Function constructors
import {
  query,
  mutation,
  action,
  internalQuery,
  internalMutation,
  internalAction,
} from "./_generated/server";

// API references
import { api, internal } from "./_generated/api";

// Types
import { Doc, Id } from "./_generated/dataModel";

// Validators
import { v } from "convex/values";

// HTTP router
import { httpRouter } from "convex/server";
import { httpAction } from "./_generated/server";

// Components
import { components } from "./_generated/api";
```
```

## File: `templates/skills/dev.md`
```markdown
# Convex Full-Stack Development Skill

Expert full-stack and AI developer specializing in React, Vite, Bun, Clerk, WorkOS, Resend, TypeScript, and Convex.dev.

## Core principles

- Always create type-safe code
- Be terse and casual unless specified otherwise
- No emojis unless instructed
- Treat user as a new developer
- Suggest solutions and anticipate needs
- Never break existing functionality
- Don't over-engineer

## Convex best practices

### Mutations

- Patch directly without reading first
- Use indexed queries for ownership checks (not `ctx.db.get()`)
- Make mutations idempotent with early returns
- Use timestamp-based ordering for new items
- Use `Promise.all()` for parallel independent operations

### Resources

- Follow Convex TypeScript best practices: https://docs.convex.dev/understanding/best-practices/typescript
- Convex workflow: https://docs.convex.dev/understanding/workflow
- Query functions: https://docs.convex.dev/functions/query-functions
- Mutation functions: https://docs.convex.dev/functions/mutation-functions
- Auth functions: https://docs.convex.dev/auth/functions-auth
- File storage: https://docs.convex.dev/file-vault/upload-files
- Vector search: https://docs.convex.dev/search/vector-search

## Authentication

- WorkOS AuthKit: https://workos.com/brain/knowledge/docs_legacy/authkit/vanilla/nodejs
- Convex + WorkOS setup: https://docs.convex.dev/auth/authkit/
- Clerk integration: https://clerk.com/brain/knowledge/docs_legacy/react/reference/components/authentication/sign-in

## React guidelines

- Understand when to use/not use Effects: https://react.dev/learn/you-might-not-need-an-effect
- Follow React docs: https://react.dev/learn

## Design system

- Follow Vercel Web Interface Guidelines: https://vercel.com/design/guidelines
- Use site's design system for modals, alerts, notifications (never browser defaults)
- Make designs beautiful and production-ready

## Code practices

- Add brief comments explaining what sections do
- Respect prettier preferences
- Keep answers brief (show only changed lines with context)
- Split long responses into multiple messages
- Never use placeholder text or images (everything syncs with Convex)
- Minimal, focused changes only

## Documentation

- Keep `files.md` with brief file descriptions
- Maintain `changelog.md` following https://keepachangelog.com/en/1.0.0/
- Do NOT create README, CONTRIBUTING, SUMMARY, or USAGE_GUIDELINES unless explicitly asked

## Git safety

Follow all rules in `gitrules.md`:

- Never use `git checkout` to revert changes without examining what will be destroyed
- Always use `git diff <file>` before any destructive operation
- Never run destructive commands (`git reset --hard`, `git checkout -- .`, `git clean -fd`, `git stash drop`) without explicit user approval
- Always run `git status` first before any git operation
- When asked to "undo" changes, manually edit files instead of using checkout
- If uncommitted changes exist, stop and ask user before proceeding

## Communication

- Give answers immediately, explain after
- Value good arguments over authorities
- Consider new/contrarian ideas
- High speculation is ok (flag it)
- No moral lectures
- Cite sources at the end, not inline
- No need to mention knowledge cutoff or AI disclosure
```

## File: `templates/skills/gitrules.md`
```markdown
# Git Safety Protocol

Critical rules to prevent accidental data loss from destructive git operations.

## Never use git checkout to revert changes

**MANDATORY RULES:**

- **NEVER run `git checkout -- <file>`** without first examining what you're about to destroy
- **ALWAYS use `git diff <file>`** to see exactly what changes will be lost
- **MANUALLY undo changes** by editing files to revert specific problematic sections
- **Preserve valuable work** - if user says changes are bad, ask which specific parts to revert
- **`git checkout` destroys ALL changes** - this can eliminate hours of valuable progress
- **When user asks to "undo" changes**: Read the current file, identify problematic sections, and manually edit to fix them

**Why this matters**: Using `git checkout` blindly can destroy sophisticated implementations, complex prompts, provider-specific logic, and other valuable work that took significant time to develop.

## Destructive commands requiring explicit approval

**NEVER run these commands without explicit user approval:**

| Command | Effect |
|---------|--------|
| `git reset --hard` | Destroys uncommitted changes permanently |
| `git checkout -- .` | Discards all working directory changes |
| `git clean -fd` | Deletes untracked files permanently |
| `git stash drop` | Deletes stashed changes |
| `git push --force` | Overwrites remote history (dangerous for shared branches) |

## Before any git operation

1. Run `git status` first to check for uncommitted changes
2. If there are uncommitted changes, STOP and ASK the user before proceeding
3. Suggest `git stash` to preserve changes if needed

## Handling revert requests

**If user asks to "revert" something:**

1. First clarify: revert committed changes or uncommitted changes?
2. Show what will be affected before doing anything
3. Get explicit confirmation for destructive operations

**If user says "undo my changes":**

1. Read the current file
2. Identify which specific sections are problematic
3. Manually edit to fix those sections
4. Preserve everything else

## Quick checklist

Before git operations:
- [ ] Have I run `git status` first?
- [ ] Are there uncommitted changes I might destroy?
- [ ] Have I used `git diff` to see what will be affected?
- [ ] Do I have explicit user approval for any destructive command?
- [ ] Am I preserving valuable work?

When asked to revert:
- [ ] Did I clarify what specifically should be reverted?
- [ ] Am I manually editing instead of using checkout?
- [ ] Am I preserving work not mentioned in the revert request?

## Why these rules exist

These rules exist because careless git operations can destroy days of work. A single `git checkout -- .` can eliminate sophisticated implementations, complex logic, and carefully crafted code that took significant time to develop.

**When in doubt, ask first.**
```

## File: `templates/skills/help.md`
```markdown
# Core Development Guidelines Skill

Deep reflection and problem-solving methodology for full-stack Convex development.

## 1. Reflect deeply before acting

Before implementing any solution, follow this process:

1. **Reflect** - Carefully consider why the current implementation may not be working
2. **Identify** - What's missing, incomplete, or incorrect based on the request
3. **Theorize** - Different possible sources of the problem or areas requiring updates
4. **Distill** - Narrow down to 1-2 most probable root causes or solutions
5. **Proceed** - Only move forward after clear understanding

**Never assume.** If anything is unclear, ask questions and clarify.

## 2. Convex implementation guidelines

### Core principles

**Direct mutation pattern:**
- Use direct mutation calls with plain objects
- Create dedicated mutation functions that map form fields to database fields
- Form field names should exactly match database field names when applicable

**Best practices:**
- Patch directly without reading first
- Use indexed queries for ownership checks (not `ctx.db.get()`)
- Make mutations idempotent with early returns
- Use timestamp-based ordering for new items
- Use `Promise.all()` for parallel independent operations to avoid write conflicts

### Essential documentation

**Functions:**
- Mutations: https://docs.convex.dev/functions/mutation-functions
- Queries: https://docs.convex.dev/functions/query-functions
- Validation: https://docs.convex.dev/functions/validation
- General: https://docs.convex.dev/functions

**Core concepts:**
- Zen of Convex: https://docs.convex.dev/understanding/zen
- TypeScript best practices: https://docs.convex.dev/understanding/best-practices/typescript
- Best practices: https://docs.convex.dev/understanding/best-practices/
- Schema validation: https://docs.convex.dev/database/schemas

**Authentication:**
- WorkOS AuthKit: https://workos.com/brain/knowledge/docs_legacy/authkit/vanilla/nodejs
- WorkOS docs: https://workos.com/docs
- Convex + WorkOS setup: https://docs.convex.dev/auth/authkit/

## 3. Change scope and restrictions

### What to update

- Update Convex schema if needed
- Only update files directly necessary to fix the original request
- When tasks touch changelog.md or files.md:
  - Run `git log --date=short` to check commit history
  - Set release dates to match real commit timeline
  - No placeholders or future months

### What NOT to change

- Do not change UI, layout, design, or color styles unless specifically instructed
- Preserve all existing components unless explicitly told to update
- Never remove sections, features, or components unless directly requested

## 4. UI/UX guidelines

### Design system compliance

**For pop-ups, alerts, modals, warnings, notifications, and confirmations:**
- Always follow the site's existing design system
- Never use browser default pop-ups
- Use site design system components only

### Follow Vercel guidelines

https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/refs/heads/main/AGENTS.md

## 5. Documentation policy

**IMPORTANT:** Do NOT create documentation files unless explicitly instructed.

**Banned unless requested:**
- README.md
- CONTRIBUTING.md
- SUMMARY.md
- USAGE_GUIDELINES.md

You may include a brief summary in responses, but don't create separate documentation files.

## 6. Code confidence requirement

**98% confidence rule:**

Don't write any code until you're very confident (98% or more) in what needs to be done.

If unclear, ask for more information.

## 7. Git safety

Follow all rules in `gitrules.md`:

- Never use `git checkout` to revert changes without examining what will be destroyed
- Always use `git diff <file>` before any destructive operation
- Never run `git reset --hard`, `git checkout -- .`, `git clean -fd`, or `git stash drop` without explicit user approval
- Always run `git status` first to check for uncommitted changes
- When user asks to "undo" changes, manually edit files to revert specific sections instead of using checkout

## Quick reference checklist

Before writing code:
- [ ] Have I reflected on the root cause?
- [ ] Do I understand what's actually broken?
- [ ] Am I 98% confident in the solution?
- [ ] Am I only changing files that need to change?
- [ ] Am I preserving existing UI/features not mentioned?
- [ ] Am I using the site's design system (not browser defaults)?
- [ ] Am I following Convex mutation best practices?
- [ ] Have I checked the relevant docs?

When uncertain:
- [ ] Ask clarifying questions
- [ ] Don't assume
- [ ] Reference documentation
- [ ] Narrow down to 1-2 most likely solutions

Before git operations:
- [ ] Have I run `git status` first?
- [ ] Am I about to run a destructive command?
- [ ] Have I shown the user what will be affected?
- [ ] Do I have explicit user approval for destructive operations?
```

## File: `templates/skills/README.md`
```markdown
# Claude Code Skills Templates

These are template skills for Claude Code (claude.ai/code). Copy them to your project's `.claude/skills/` directory and customize as needed.

## Installation

1. Create the skills directory in your project:

```bash
mkdir -p .claude/skills
```

2. Copy the skills you want:

```bash
cp templates/skills/dev.md .claude/skills/
cp templates/skills/help.md .claude/skills/
cp templates/skills/gitrules.md .claude/skills/
```

3. Customize each skill for your project's needs.

## Available Templates

| Template | Purpose |
|----------|---------|
| `dev.md` | Full-stack Convex development practices and coding standards |
| `help.md` | Problem-solving methodology and change management guidelines |
| `gitrules.md` | Git safety protocols to prevent accidental data loss |

## Customization Tips

**dev.md**
- Add your specific tech stack
- Include project-specific documentation links
- Add custom coding conventions

**help.md**
- Adjust the confidence threshold (default 98%)
- Add project-specific change restrictions
- Include team-specific documentation policies

**gitrules.md**
- Generally keep as-is (safety rules are universal)
- Add project-specific branch protection rules if needed

## Usage with Claude Code

Once installed, Claude Code will automatically use these skills when working in your project. You can also reference them explicitly:

```
Use the dev skill for this task
Follow gitrules before any git operation
```

## References

- Claude Code documentation: https://docs.anthropic.com/en/brain/knowledge/docs_legacy/claude-code
- Convex documentation: https://docs.convex.dev/
```

