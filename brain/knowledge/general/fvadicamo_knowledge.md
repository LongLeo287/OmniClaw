---
id: fvadicamo-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:25.789189
---

# KNOWLEDGE EXTRACT: fvadicamo
> **Extracted on:** 2026-03-30 17:37:23
> **Source:** fvadicamo

---

## File: `dev-agent-skills.md`
```markdown
# 📦 fvadicamo/dev-agent-skills [🔖 PENDING/APPROVE]
🔗 https://github.com/fvadicamo/dev-agent-skills


## Meta
- **Stars:** ⭐ 54 | **Forks:** 🍴 5
- **Language:** N/A | **License:** MIT
- **Last updated:** 2026-03-23
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Claude Code skills plugin for Git, GitHub, and skill authoring workflows

## README (trích đầu)
```
# dev-agent-skills

Agent skills for development workflows - Git, GitHub, and skill authoring.

These skills are designed for [Claude Code](https://claude.com/claude-code), the CLI tool by Anthropic.

## Why these skills?

Claude Code already knows how to commit, create PRs, and review code. But without structured guidance it tends to:

- Use inconsistent commit formats across a session
- Skip target branch confirmation and create PRs against the wrong branch
- Not search for task documentation or validate task completion before opening a PR
- Suggest labels that don't exist in the project
- Process review comments in random order instead of by severity
- Use the wrong GitHub API syntax for replying to threads (`-f` instead of `--input -`)
- Generate verbose merge messages that clutter the git log
- Merge without verifying all review comments have been addressed

These skills add structured workflows that prevent these issues. They don't replace Claude's capabilities - they guide them through the right sequence of steps.

There are no official Anthropic skills for Git/GitHub workflows. This plugin fills that gap.

## Quick install

```bash
# Add marketplace
/plugin marketplace add fvadicamo/dev-agent-skills

# Install plugins
/plugin install github-workflow@dev-agent-skills
/plugin install skill-authoring@dev-agent-skills
```

## How skills work

Skills are **model-invoked** - Claude automatically activates them based on your request:

- "Create a commit" -> activates `git-commit`
- "Open a PR" -> activates `github-pr-creation`
- "Merge the PR" -> activates `github-pr-merge`
- "Address review comments" -> activates `github-pr-review`
- "Help me create a skill" -> activates `creating-skills`

## Plugin: github-workflow

Skills for Git and GitHub workflows following [Conventional Commits](https://www.conventionalcommits.org/).

### git-commit

Creates commits following Conventional Commits format with type/scope/subject.

**What it adds over Claude's default behavior:**

| Without this skill | With this skill |
|--------------------|-----------------|
| Inconsistent commit format across a session | Enforces CC format with required scope, max 50 chars, imperative tense |
| Ignores existing commit style in the project | Dynamic context injection loads recent commits so Claude matches the style |
| Sometimes uses generic messages ("update code") | Strict rules against vague messages |
| No HEREDOC for multi-line commits | Provides HEREDOC pattern for clean multi-line messages |

Additional features:
- Checks CLAUDE.md for project-specific commit conventions
- Extra commit type `security` beyond standard CC

### github-pr-creation

Creates Pull Requests with automated validation, task tracking, and label suggestions.

**What it adds over Claude's default behavior:**

| Without this skill | With this skill |
|--------------------|-----------------|
| Often skips target branch confirmation | Always asks user to confirm base branch |
| Doesn't search for 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

