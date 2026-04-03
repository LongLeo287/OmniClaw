---
id: wrsmith108-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:47.036904
---

# KNOWLEDGE EXTRACT: wrsmith108
> **Extracted on:** 2026-03-30 18:01:18
> **Source:** wrsmith108

---

## File: `linear-claude-skill.md`
```markdown
# 📦 wrsmith108/linear-claude-skill [🔖 PENDING/APPROVE]
🔗 https://github.com/wrsmith108/linear-claude-skill


## Meta
- **Stars:** ⭐ 73 | **Forks:** 🍴 11
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Agent skill for managing Linear issues, projects, and teams. MCP tools, SDK automation, GraphQL API patterns.

## README (trích đầu)
```
# Linear Skill for Claude Code

A comprehensive [Claude Code](https://claude.ai/code) skill for managing Linear issues, projects, and teams. Provides patterns for MCP tools, SDK automation, and GraphQL API access.

## Features

- **esbuild Pre-compilation** — 18x faster CLI startup (~50ms vs ~1s) with transparent tsx fallback
- **Label Taxonomy System** — Domain-based labels for consistent categorization and agent routing
- **First-Time Setup Check** — Automatic configuration validation with actionable guidance
- **High-Level Operations** — Simple commands for initiatives, projects, and status updates
- **Sub-Issue Management** — Create and manage parent-child issue relationships
- **Discovery Before Creation** — Mandatory checks to prevent duplicate projects/issues
- **MCP Tool Integration** — Simple operations via Linear MCP server
- **SDK Automation** — Complex operations with TypeScript scripts
- **GraphQL API** — Direct API access for advanced queries
- **Project Management** — Content, descriptions, milestones, resource links
- **Bulk Sync** — Synchronize code changes with Linear via CLI, agents, or hooks
- **Image Uploads** — Upload images to Linear's S3 storage and attach to issues
- **Smoke Tests** — Automated verification of build output and CLI behavior

## Quick Start (New Users)

### 1. Install the Skill

```bash
git clone https://github.com/wrsmith108/linear-claude-skill ~/.claude/skills/linear
cd ~/.claude/skills/linear && npm install
```

### 2. Run Setup Check

```bash
npm run setup
```

This checks your configuration and tells you exactly what's missing.

### 3. Get Your API Key (If Needed)

1. Open [Linear](https://linear.app) in your browser
2. Go to **Settings** → **Security & access** → **Personal API keys**
3. Click **Create key** and copy it (starts with `lin_api_`)
4. Add to your environment:

```bash
# Add to shell profile
echo 'export LINEAR_API_KEY='[REDACTED_API_KEY]'' >> ~/.zshrc
source ~/.zshrc
```

### 4. Verify It Works

```bash
npm run ops -- whoami
```

You should see your name and organization.

### 5. Build for Faster Startup (Optional)

```bash
npm run build
```

Pre-compiles TypeScript to JavaScript for ~18x faster CLI cold starts. Without building, commands still work via tsx (slower but functional).

### 6. Start Using It

```bash
# Create an initiative
npm run ops -- create-initiative "My Project"

# Create a project
npm run ops -- create-project "Phase 1" "My Project"

# Create a sub-issue under a parent
npm run ops -- create-sub-issue ENG-100 "Add tests" "Unit tests for feature"

# Set parent-child relationships for existing issues
npm run ops -- set-parent ENG-100 ENG-101 ENG-102

# Update issue status
npm run ops -- status Done ENG-123 ENG-124

# See all commands
npm run ops -- help
```

---

## Installation

```bash
# Clone directly to your skills directory
git clone https://github.com/wrsmith108/linear-claude-skill ~/.claude/skills/linear
cd ~/.claude/skills/linear && npm install
```

## Prerequi
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `varlock-claude-skill.md`
```markdown
# 📦 wrsmith108/varlock-claude-skill [🔖 PENDING/APPROVE]
🔗 https://github.com/wrsmith108/varlock-claude-skill


## Meta
- **Stars:** ⭐ 16 | **Forks:** 🍴 0
- **Language:** N/A | **License:** MIT
- **Last updated:** 2026-03-14
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Claude Code skill for secure environment variable management with Varlock. Never expose secrets in Claude sessions.

## README (trích đầu)
```
# Varlock Skill for Claude Code

> Secure-by-default environment variable management. Ensures secrets are **never exposed** in Claude sessions.

## Why This Skill?

When working with Claude Code, secrets can accidentally leak into:
- Terminal output
- Claude's input/output context
- Log files or traces
- Git commits or diffs

This skill wraps [Varlock](https://varlock.dev) to enforce secure patterns and prevent accidental exposure.

## Installation

### Option A: One-liner (Recommended)

```bash
mkdir -p ~/.claude/skills/varlock && curl -sSL https://raw.githubusercontent.com/wrsmith108/varlock-claude-skill/main/skills/varlock/SKILL.md -o ~/.claude/skills/varlock/SKILL.md
```

### Option B: Manual

```bash
git clone https://github.com/wrsmith108/varlock-claude-skill /tmp/varlock-skill
cp -r /tmp/varlock-skill/skills/varlock ~/.claude/skills/
rm -rf /tmp/varlock-skill
```

## Prerequisites

Install the Varlock CLI:

```bash
curl -sSfL https://varlock.dev/install.sh | sh -s -- --force-no-brew
export PATH="$HOME/.varlock/bin:$PATH"
```

## Core Principle

**Secrets must NEVER appear in Claude's context.**

| Never Do | Safe Alternative |
|----------|------------------|
| `cat .env` | `cat .env.schema` |
| `echo $SECRET` | `varlock load` |
| `printenv \| grep API` | `varlock load \| grep API` |

## Quick Reference

```bash
# Validate all secrets (shows masked values)
varlock load

# Quiet validation (no output on success)
varlock load --quiet

# Run command with secrets injected
varlock run -- npm start

# View schema (safe - no values)
cat .env.schema
```

## Schema File

Create `.env.schema` to define variable types and sensitivity:

```bash
# Global defaults
# @defaultSensitive=true @defaultRequired=infer

# Public config
# @type=enum(development,staging,production) @sensitive=false
NODE_ENV=development

# Sensitive secrets
# @type=string(startsWith=sk_) @required @sensitive
STRIPE_SECRET_KEY=

# @type=url @required @sensitive
DATABASE_URL=
```

### Annotations

| Annotation | Effect |
|------------|--------|
| `@sensitive` | Value masked in all output |
| `@sensitive=false` | Value shown (for public keys) |
| `@required` | Must be present |
| `@type=string(startsWith=X)` | Prefix validation |


## Handling Secret Requests

When users ask Claude to:

- **"Check if API key is set"** → `varlock load | grep API_KEY`
- **"Debug authentication"** → `varlock load` (validates all)
- **"Update a secret"** → Decline; ask user to update manually
- **"Show me .env"** → `cat .env.schema` instead

## Credits

This skill wraps [Varlock](https://github.com/dmno-dev/varlock) by [DMNO](https://dmno.dev).

## License

MIT

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

