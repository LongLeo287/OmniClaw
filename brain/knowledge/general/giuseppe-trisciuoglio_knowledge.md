---
id: giuseppe-trisciuoglio-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:48.395405
---

# KNOWLEDGE EXTRACT: giuseppe-trisciuoglio
> **Extracted on:** 2026-03-30 17:37:59
> **Source:** giuseppe-trisciuoglio

---

## File: `developer-kit.md`
```markdown
# 📦 giuseppe-trisciuoglio/developer-kit [🔖 PENDING/APPROVE]
🔗 https://github.com/giuseppe-trisciuoglio/developer-kit


## Meta
- **Stars:** ⭐ 176 | **Forks:** 🍴 17
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
 Modular plugin marketplace for Claude Code and agentic CLIs, with validated, spec-driven skills, agents, commands, and workflows for Java, TypeScript, Python, PHP, AWS, and AI.

## README (trích đầu)
```
# Developer Kit for Claude Code

[![Security Scan](https://github.com/giuseppe-trisciuoglio/developer-kit/actions/workflows/security-scan.yml/badge.svg)](https://github.com/giuseppe-trisciuoglio/developer-kit/actions/workflows/security-scan.yml)
[![Plugin Validation](https://github.com/giuseppe-trisciuoglio/developer-kit/actions/workflows/plugin-validation.yml/badge.svg)](https://github.com/giuseppe-trisciuoglio/developer-kit/actions/workflows/plugin-validation.yml)

> A modular plugin system of reusable skills, agents, and commands for automating development tasks in Claude Code

**Listed on:**
- [context7](https://context7.com/giuseppe-trisciuoglio/developer-kit?tab=skills) — Skills marketplace
- [skills.sh](https://skills.sh/giuseppe-trisciuoglio/developer-kit) — AI skills directory

**Developer Kit for Claude Code** teaches Claude how to **perform development tasks in a repeatable way** across
multiple languages and frameworks. Built as a modular marketplace, you can install only the plugins you need.

## Quick Start

```bash
# Install from marketplace (recommended)
/plugin marketplace add giuseppe-trisciuoglio/developer-kit

# Or install from local directory
/plugin install /path/to/developer-kit
```

**Claude Desktop**: [Enable Skills in Settings](https://claude.ai/settings/capabilities)

---

## Architecture

Developer Kit is organized as a **modular marketplace** with 11 independent plugins:

```
plugins/
├── developer-kit-core/            # Core agents/commands/skills (required)
├── developer-kit-java/            # Java/Spring Boot/LangChain4J/AWS SDK/GraalVM Native Image
├── developer-kit-typescript/      # NestJS/React/React Native/Next.js/Drizzle/Monorepo
├── developer-kit-python/          # Python development/AWS Lambda
├── developer-kit-php/             # PHP/WordPress/AWS Lambda
├── developer-kit-aws/             # AWS CloudFormation/AWS Architecture
├── developer-kit-ai/              # Prompt Engineering/RAG/Chunking
├── developer-kit-devops/          # Docker/GitHub Actions
├── developer-kit-project-management/  # LRA workflow/Meetings
├── developer-kit-tools/           # Additional development tools and MCP integrations
└── github-spec-kit/               # GitHub specification integration
```

Current marketplace totals: **116 skills**, **43 agents**, and **44 commands** across the 11 plugin manifests.

Language plugins (Java, TypeScript, Python, PHP) include **coding rules** (`rules/` directory) that auto-activate via `globs:` path-scoped matching to enforce naming conventions, project structure, language best practices, and error handling patterns. They also include **LSP server configurations** (`.lsp.json`) for real-time code intelligence, diagnostics, and navigation features.

---

## Workflow

The Developer Kit follows a systematic development workflow that ensures high-quality, well-documented features from idea to implementation:

### 1. Brainstorming Phase

**Command:** `/devkit.brainstorm [idea-description]`

Start her
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

