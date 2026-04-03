---
id: getsentry-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:26.965635
---

# KNOWLEDGE EXTRACT: getsentry
> **Extracted on:** 2026-03-30 17:37:58
> **Source:** getsentry

---

## File: `skills.md`
```markdown
# 📦 getsentry/skills [🔖 PENDING/APPROVE]
🔗 https://github.com/getsentry/skills


## Meta
- **Stars:** ⭐ 470 | **Forks:** 🍴 16
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Agent Skills used by the Sentry team for development.

## README (trích đầu)
```
# Sentry Skills

> [!NOTE]
> For skills to help set up Sentry in your project or debug production issues, see https://github.com/getsentry/sentry-for-ai

Agent skills for Sentry employees, following the [Agent Skills](https://agentskills.io) open format.

## Installation

### Claude Code

```bash
claude plugin marketplace add getsentry/skills
claude plugin install sentry-skills@sentry-skills
```

Restart Claude Code after installation. Skills activate automatically when relevant.

**Update:**

```bash
claude plugin marketplace update
claude plugin update sentry-skills@sentry-skills
```

Or run `/plugin` to open the plugin manager.

### Skills Package (skills.sh)

For agents supporting the [skills.sh](https://skills.sh) ecosystem:

```bash
npx skills add getsentry/skills
```

Works with Claude Code, Cursor, Cline, GitHub Copilot, and other compatible agents.

## Available Skills

| Skill | Description |
|-------|-------------|
| [agents-md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | This skill should be used when the user asks to "create AGENTS.md", "update AGENTS.md", "maintain agent docs", "set up CLAUDE.md", or needs to keep agent instructions concise. |
| [blog-writing-guide](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | Write, review, and improve blog posts for the Sentry engineering blog following Sentry's specific writing standards, voice, and quality bar. |
| [brand-guidelines](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | Write copy following Sentry brand guidelines. |
| [claude-settings-audit](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | Analyze a repository to generate recommended Claude Code settings.json permissions. |
| [code-review](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | Perform code reviews following Sentry engineering practices. |
| [code-simplifier](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | Simplifies and refines code for clarity, consistency, and maintainability while preserving all functionality. |
| [commit](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | ALWAYS use this skill when committing code changes — never commit directly without it. |
| [create-branch](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | Create git branches following Sentry naming conventions. |
| [django-access-review](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | Django access control and IDOR security review. |
| [django-perf-review](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | Django performance code review. |
| [doc-coauthoring](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | Guide users through a structured workflow for co-authoring documentation. |
| [find-bugs](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | Find bugs, security vulnerabilities, and code quality issues in local branch changes. |
| [gh-review-requests](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | Fetch unread GitHub notifications for open PR
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

