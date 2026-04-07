---
id: dev-agent-skills
type: knowledge
owner: OA_Triage
---
# dev-agent-skills
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
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
| Doesn't search for task documentation | Searches Kiro, Cursor, Trae, GitHub Issues, and generic paths for task specs |
| No task completion validation | Maps commits to tasks and reports missing sub-tasks before creating PR |
| Suggests labels that may not exist in the project | Checks `gh label list` first, matches available labels, suggests creating missing ones |
| Generic PR body | 7 type-specific templates (feature, release, bugfix, hotfix, refactoring, docs, CI/CD) |
| May skip tests | Tests must pass before PR creation |

### github-pr-merge

Merges Pull Requests after validating a pre-merge checklist.

**What it adds over Claude's default behavior:**

| Without this skill | With this skill |
|--------------------|-----------------|
| May merge without checking review comments | Detects unreplied comments via jq query, stops merge and redirects to review skill |
| Inconsistent merge strategy | Always merge commit (`--merge`), never squash/rebase |
| Verbose or empty merge messages | Concise format: 3-5 bullets + reviews/tests/refs (~10 lines max) |
| May skip CI/lint checks | Full pre-merge checklist (tests, lint, CI, comments) with summary shown to user |
| Forgets branch cleanup | Auto-deletes remote branch, switches to develop and pulls |

### github-pr-review

Handles PR review comments and feedback resolution.

**What it adds over Claude's default behavior:**

| Without this skill | With this skill |
|--------------------|-----------------|
| Processes comments in random order | Classifies by severity (CRITICAL > HIGH > MEDIUM > LOW) and processes in order |
| No severity detection | Detects Gemini badges, Cursor HTML comments, and keyword-based severity |
| One commit per fix regardless of impact | Batch strategy: separate commits for functional fixes, single batch for cosmetic |
| May use `-f in_reply_to=...` (broken) | Uses correct `--input -` JSON syntax for thread replies |
| Generic or no replies to threads | Standard templates: Fixed, Won't fix, By design, Deferred, Acknowledged |
| Triggers bot review loops on every push | Strategies to avoid loops: batch pushes, draft PR, skip keywords |
| Forgets to submit formal review | Prompts `gh pr review` with appropriate flag (approve/request-changes/comment) |

## Plugin: skill-authoring

### creating-skills

Guide for creating Claude Code skills following Anthropic's official best practices.

**What it adds over Claude's default behavior:**

Claude knows the basics of skill creation, but this skill provides a comprehensive, up-to-date reference covering features that Claude may not know about or consistently apply.

- Complete frontmatter reference (all 10 fields including `allowed-tools`, `context`, `agent`, `hooks`)
- Invocation control matrix (`disable-model-invocation`, `user-invocable`)
- Dynamic features: context injection (`` !`cmd` ``), string substitutions (`$ARGUMENTS`), subagent execution
- Degrees of freedom concept for matching specificity to task fragility
- Directory structure with `scripts/`, `references/`, and `assets/` resource types
- Description formula, naming conventions, progressive disclosure patterns

#### Comparison with the official skill-creator

This skill complements the official [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) from Anthropic. They serve different purposes and can be used together.

| Feature | This skill | Official skill-creator |
|---------|-----------|----------------------|
| Complete frontmatter reference (10 fields) | Yes | No (only 5 fields) |
| Invocation control matrix | Yes | No |
| Dynamic context injection (`` !`cmd` ``) | Yes, with examples | No |
| String substitutions (`$ARGUMENTS`, `$1`) | Yes | No |
| Subagent execution (`context: fork`) | Yes, with example | No |
| Discovery hierarchy | Yes | No |
| Context budget (2%, 16k fallback) | Yes | No |
| Skills/commands unification | Yes | No |
| Frontmatter validation rules | Yes | No |
| 6 feature-specific examples | Yes | No |
| Scaffolding script (`init_skill.py`) | No | Yes |
| Packaging script (`package_skill.py`) | No | Yes |
| Validation script (`quick_validate.py`) | No | Yes |
| Workflow patterns reference | No | Yes |
| Output patterns reference | No | Yes |

**In short**: this skill is a practical, up-to-date reference for all available features. The official skill is a conceptual guide with scaffolding/packaging tools. Install both for the most complete experience.

## License

MIT License - see [LICENSE](LICENSE) for details.

```

### File: CHANGELOG.md
```md
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.1] - 2026-03-23

### Fixed

#### github-pr-review
- Added fallback to `pulls/$PR/reviews/$REVIEW_ID/comments` endpoint when review-attached inline comments are not surfaced by the general `pulls/$PR/comments` endpoint (cross-checks "Actionable comments posted: N" count)
- Added missing CodeRabbit type indicators to severity table (`_🚨 Critical_`, `_⚡ Performance_`)
- Documented secondary color badge override rule (e.g., `_💡 Suggestion_ | _🟠 Major_` binds to HIGH, not MEDIUM)
- Added reference to CodeRabbit global "Prompt for all review comments with AI agents" block for cross-comment context
- Added `?per_page=100` to all fetch API calls to handle PRs with many comments

## [1.2.0] - 2026-02-20

### Changed

#### github-pr-review
- Added CodeRabbit severity detection to `references/severity_guide.md`: emoji+italic pattern (`_⚠️ Potential issue_`, `_🧹 Nitpick_`, `_🔧 Optional_`, etc.), secondary color badges (`_🟡 Minor_`, `_🟠 Major_`) as binding severity indicator
- Documented CodeRabbit "outside diff" comments pattern: embedded in PR-level review body `<details>` blocks, not in `pulls/$PR/comments`
- Step 1: added `pulls/$PR/reviews` fetch alongside `pulls/$PR/comments` to capture outside diff comments
- Step 1: replaced raw fetch commands with inline `--jq` filters to avoid `!=` operator, which Claude Code's Bash tool escapes as `\!=` breaking jq
- Updated severity table in step 1 with CodeRabbit indicators
- Current PR context now includes milestone: `PR #N: title (state) | Milestone: name`
- Added step 7: verify milestone at end of review; suggest assigning if missing and open milestones exist (never assigns automatically)

#### github-pr-creation
- Added `.s2s/plans/*.md` to task documentation search paths (Spec2Ship projects)
- Added `chore/*`, `ci/*`, `docs/*` branch patterns to title prefix table
- Added breaking change handling: add `breaking` label + `## Breaking changes` body section
- Added step 9: detect open milestones and assign if exactly one is active; ask user if multiple exist
- Updated `gh pr create` command with `--milestone`, `--reviewer`, correct multi-`--label` syntax
- Added `--draft` usage note (WIP, CI wait, AI bot trigger)

#### github-pr-merge
- Added step 2: check PR milestone before merge; warn (not block) if open milestones exist but PR has none
- Added milestone line to pre-merge checklist summary (step 4)
- Added step 7: after merge, check `open_issues` on milestone; offer to close it if all items are done
- Renumbered steps: old 2→3, 3→4, 4→5, 5→6; new steps are 2 and 7

## [1.1.0] - 2026-02-07

### Added

- **CLAUDE.md**: project-level instructions for contributors
- **.gitignore**: exclude local settings from version control
- **README.md**: "Why these skills?" section with value propositions and Without/With comparison tables for each skill

### Changed

#### git-commit
- Streamlined SKILL.md from 236 to 54 lines (-77%)
- Added dynamic context injection (`!`git log``) to match existing project commit style
- Removed content Claude already knows (CC types, subject rules, git basics, trailers, breaking changes)
- Removed merge commits section (belongs to github-pr-creation)
- Moved good/bad examples to `references/commit_examples.md`

#### github-pr-creation
- Streamlined SKILL.md from 202 to 138 lines (-32%)
- Added dynamic context injection for current branch and unpushed commits
- Expanded task documentation search with paths for Kiro, Cursor, Trae, GitHub Issues
- Reworked label suggestion to check available project labels first via `gh label list`
- Trimmed `references/pr_templates.md` from 461 to 188 lines (templates only)
- Removed `references/conventional_commits.md` (duplicated standard CC knowledge)

#### github-pr-merge
- Streamlined SKILL.md from 211 to 113 lines (-46%)
- Added dynamic context injection for current PR info
- Simplified unreplied comments check to single jq command
- Removed redundant sections (Quick Start, Pre-Merge Checklist table, Error Handling)

#### github-pr-review
- Streamlined SKILL.md from 236 to 111 lines (-53%)
- Added dynamic context injection for current PR info
- Integrated reply API gotcha (`--input -` vs `-f`) into workflow step
- Renamed `references/gemini_severity_guide.md` to `references/severity_guide.md`
- Added Cursor comment severity detection to severity guide

#### creating-skills
- Streamlined SKILL.md from 262 to 159 lines (-39%)
- Added complete frontmatter reference (10 fields including `allowed-tools`, `context`, `agent`, `hooks`)
- Added invocation control matrix, dynamic features (context injection, string substitutions, subagent execution)
- Added degrees of freedom concept and `assets/` resource type
- Rewrote `references/official_best_practices.md` with context budget, frontmatter validation, discovery hierarchy, skills/commands unification
- Rewrote `references/skill_examples.md` with 6 concrete examples of new features

## [1.0.0] - 2025-12-21

### Added

- Initial release with 5 skills organized in 2 plugins

#### github-workflow plugin
- **git-commit**: Conventional Commits format with type/scope/subject
- **github-pr-creation**: PR creation with validation and task tracking
- **github-pr-merge**: Pre-merge checklist validation
- **github-pr-review**: PR review comment resolution with severity classification

#### skill-authoring plugin
- **creating-skills**: Guide for creating Claude Code skills

```

### File: CLAUDE.md
```md
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

A collection of Claude Code agent skills for development workflows, distributed as a plugin marketplace. Contains 5 skills organized into 2 plugins:

- **github-workflow** plugin: `git-commit`, `github-pr-creation`, `github-pr-merge`, `github-pr-review`
- **skill-authoring** plugin: `creating-skills`

Skills are model-invoked (Claude activates them based on user intent, not slash commands).

## Architecture

```
.claude-plugin/
  marketplace.json        # Plugin registry: defines plugins, skill paths, metadata
skills/
  <skill-name>/
    SKILL.md              # Main skill file (YAML frontmatter + markdown body)
    references/           # Optional deep-dive docs loaded on demand
```

### Key file: `marketplace.json`

Defines the plugin structure. Each plugin has a `skills` array pointing to skill directories. When adding or removing skills, update both the plugin's `skills` array and the corresponding directory.

### Skill anatomy

Every skill requires a `SKILL.md` with:
1. **YAML frontmatter** (`name` + `description`) - the description is critical for discovery, it determines when Claude activates the skill
2. **Markdown body** - workflow instructions, kept under 500 lines

Reference files in `references/` provide extended examples and documentation that Claude loads only when needed (progressive disclosure).

## Conventions

- **Commits**: Conventional Commits format - `type(scope): subject` (see `skills/git-commit/SKILL.md`)
- **Naming**: lowercase, hyphens between words, no spaces (e.g., `github-pr-review`)
- **Merge strategy**: always merge commits (`--merge`), never squash/rebase
- **Changelog**: follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) format
- **Versioning**: [Semantic Versioning](https://semver.org/spec/v2.0.0.html)

## Writing skills

When creating or editing skills, follow the patterns in `skills/creating-skills/SKILL.md`:

- Description formula: `<What it does>. Use when <trigger phrases>. <Key capabilities>.`
- SKILL.md body under 500 lines; move detailed content to `references/`
- Only create helper scripts when they add real value (complex processing, JSON transformation), not for single-command wrappers
- Mark critical constraints with bold **ALWAYS**/**NEVER** in "Important Rules" sections
- Include trigger phrases in descriptions so Claude activates the skill on the right user intents

```

### File: .claude-plugin\marketplace.json
```json
{
  "name": "dev-agent-skills",
  "owner": {
    "name": "Francesco Vadicamo",
    "email": "fvadicamo@gmail.com"
  },
  "metadata": {
    "description": "Agent skills for development workflows - Git, GitHub, and skill authoring",
    "version": "1.2.1"
  },
  "plugins": [
    {
      "name": "github-workflow",
      "description": "Git commit, PR creation, review, and merge skills following Conventional Commits",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/git-commit",
        "./skills/github-pr-creation",
        "./skills/github-pr-merge",
        "./skills/github-pr-review"
      ]
    },
    {
      "name": "skill-authoring",
      "description": "Guide for creating Claude Code skills following Anthropic's best practices",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/creating-skills"
      ]
    }
  ]
}

```

