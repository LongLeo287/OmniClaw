---
id: repo-fetched-claude-code-123444
type: knowledge
owner: OA
registered_at: 2026-04-05T04:16:48.955486
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_claude-code_123444

## Assimilation Report
Auto-cloned repository: FETCHED_claude-code_123444

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Claude Code

![](https://img.shields.io/badge/Node.js-18%2B-brightgreen?style=flat-square) [![npm]](https://www.npmjs.com/package/@anthropic-ai/claude-code)

[npm]: https://img.shields.io/npm/v/@anthropic-ai/claude-code.svg?style=flat-square

Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows -- all through natural language commands. Use it in your terminal, IDE, or tag @claude on Github.

**Learn more in the [official documentation](https://code.claude.com/docs/en/overview)**.

<img src="./demo.gif" />

## Get started
> [!NOTE]
> Installation via npm is deprecated. Use one of the recommended methods below.

For more installation options, uninstall steps, and troubleshooting, see the [setup documentation](https://code.claude.com/docs/en/setup).

1. Install Claude Code:

    **MacOS/Linux (Recommended):**
    ```bash
    curl -fsSL https://claude.ai/install.sh | bash
    ```

    **Homebrew (MacOS/Linux):**
    ```bash
    brew install --cask claude-code
    ```

    **Windows (Recommended):**
    ```powershell
    irm https://claude.ai/install.ps1 | iex
    ```

    **WinGet (Windows):**
    ```powershell
    winget install Anthropic.ClaudeCode
    ```

    **NPM (Deprecated):**
    ```bash
    npm install -g @anthropic-ai/claude-code
    ```

2. Navigate to your project directory and run `claude`.

## Plugins

This repository includes several Claude Code plugins that extend functionality with custom commands and agents. See the [plugins directory](./plugins/README.md) for detailed documentation on available plugins.

## Reporting Bugs

We welcome your feedback. Use the `/bug` command to report issues directly within Claude Code, or file a [GitHub issue](https://github.com/anthropics/claude-code/issues).

## Connect on Discord

Join the [Claude Developers Discord](https://anthropic.com/discord) to connect with other developers using Claude Code. Get help, share feedback, and discuss your projects with the community.

## Data collection, usage, and retention

When you use Claude Code, we collect feedback, which includes usage data (such as code acceptance or rejections), associated conversation data, and user feedback submitted via the `/bug` command.

### How we use your data

See our [data usage policies](https://code.claude.com/docs/en/data-usage).

### Privacy safeguards

We have implemented several safeguards to protect your data, including limited retention periods for sensitive information, restricted access to user session data, and clear policies against using feedback for model training.

For full details, please review our [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) and [Privacy Policy](https://www.anthropic.com/legal/privacy).

```

### File: plugins\README.md
```md
# Claude Code Plugins

This directory contains some official Claude Code plugins that extend functionality through custom commands, agents, and workflows. These are examples of what's possible with the Claude Code plugin system—many more plugins are available through community marketplaces.

## What are Claude Code Plugins?

Claude Code plugins are extensions that enhance Claude Code with custom slash commands, specialized agents, hooks, and MCP servers. Plugins can be shared across projects and teams, providing consistent tooling and workflows.

Learn more in the [official plugins documentation](https://docs.claude.com/en/docs/claude-code/plugins).

## Plugins in This Directory

| Name | Description | Contents |
|------|-------------|----------|
| [agent-sdk-dev](./agent-sdk-dev/) | Development kit for working with the Claude Agent SDK | **Command:** `/new-sdk-app` - Interactive setup for new Agent SDK projects<br>**Agents:** `agent-sdk-verifier-py`, `agent-sdk-verifier-ts` - Validate SDK applications against best practices |
| [claude-opus-4-5-migration](./claude-opus-4-5-migration/) | Migrate code and prompts from Sonnet 4.x and Opus 4.1 to Opus 4.5 | **Skill:** `claude-opus-4-5-migration` - Automated migration of model strings, beta headers, and prompt adjustments |
| [code-review](./code-review/) | Automated PR code review using multiple specialized agents with confidence-based scoring to filter false positives | **Command:** `/code-review` - Automated PR review workflow<br>**Agents:** 5 parallel Sonnet agents for CLAUDE.md compliance, bug detection, historical context, PR history, and code comments |
| [commit-commands](./commit-commands/) | Git workflow automation for committing, pushing, and creating pull requests | **Commands:** `/commit`, `/commit-push-pr`, `/clean_gone` - Streamlined git operations |
| [explanatory-output-style](./explanatory-output-style/) | Adds educational insights about implementation choices and codebase patterns (mimics the deprecated Explanatory output style) | **Hook:** SessionStart - Injects educational context at the start of each session |
| [feature-dev](./feature-dev/) | Comprehensive feature development workflow with a structured 7-phase approach | **Command:** `/feature-dev` - Guided feature development workflow<br>**Agents:** `code-explorer`, `code-architect`, `code-reviewer` - For codebase analysis, architecture design, and quality review |
| [frontend-design](./frontend-design/) | Create distinctive, production-grade frontend interfaces that avoid generic AI aesthetics | **Skill:** `frontend-design` - Auto-invoked for frontend work, providing guidance on bold design choices, typography, animations, and visual details |
| [hookify](./hookify/) | Easily create custom hooks to prevent unwanted behaviors by analyzing conversation patterns or explicit instructions | **Commands:** `/hookify`, `/hookify:list`, `/hookify:configure`, `/hookify:help`<br>**Agent:** `conversation-analyzer` - Analyzes conversations for problematic behaviors<br>**Skill:** `writing-rules` - Guidance on hookify rule syntax |
| [learning-output-style](./learning-output-style/) | Interactive learning mode that requests meaningful code contributions at decision points (mimics the unshipped Learning output style) | **Hook:** SessionStart - Encourages users to write meaningful code (5-10 lines) at decision points while receiving educational insights |
| [plugin-dev](./plugin-dev/) | Comprehensive toolkit for developing Claude Code plugins with 7 expert skills and AI-assisted creation | **Command:** `/plugin-dev:create-plugin` - 8-phase guided workflow for building plugins<br>**Agents:** `agent-creator`, `plugin-validator`, `skill-reviewer`<br>**Skills:** Hook development, MCP integration, plugin structure, settings, commands, agents, and skill development |
| [pr-review-toolkit](./pr-review-toolkit/) | Comprehensive PR review agents specializing in comments, tests, error handling, type design, code quality, and code simplification | **Command:** `/pr-review-toolkit:review-pr` - Run with optional review aspects (comments, tests, errors, types, code, simplify, all)<br>**Agents:** `comment-analyzer`, `pr-test-analyzer`, `silent-failure-hunter`, `type-design-analyzer`, `code-reviewer`, `code-simplifier` |
| [ralph-wiggum](./ralph-wiggum/) | Interactive self-referential AI loops for iterative development. Claude works on the same task repeatedly until completion | **Commands:** `/ralph-loop`, `/cancel-ralph` - Start/stop autonomous iteration loops<br>**Hook:** Stop - Intercepts exit attempts to continue iteration |
| [security-guidance](./security-guidance/) | Security reminder hook that warns about potential security issues when editing files | **Hook:** PreToolUse - Monitors 9 security patterns including command injection, XSS, eval usage, dangerous HTML, pickle deserialization, and os.system calls |

## Installation

These plugins are included in the Claude Code repository. To use them in your own projects:

1. Install Claude Code globally:
```bash
npm install -g @anthropic-ai/claude-code
```

2. Navigate to your project and run Claude Code:
```bash
claude
```

3. Use the `/plugin` command to install plugins from marketplaces, or configure them in your project's `.claude/settings.json`.

For detailed plugin installation and configuration, see the [official documentation](https://docs.claude.com/en/docs/claude-code/plugins).

## Plugin Structure

Each plugin follows the standard Claude Code plugin structure:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json          # Plugin metadata
├── commands/                # Slash commands (optional)
├── agents/                  # Specialized agents (optional)
├── skills/                  # Agent Skills (optional)
├── hooks/                   # Event handlers (optional)
├── .mcp.json                # External tool configuration (optional)
└── README.md                # Plugin documentation
```

## Contributing

When adding new plugins to this directory:

1. Follow the standard plugin structure
2. Include a comprehensive README.md
3. Add plugin metadata in `.claude-plugin/plugin.json`
4. Document all commands and agents
5. Provide usage examples

## Learn More

- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code/overview)
- [Plugin System Documentation](https://docs.claude.com/en/docs/claude-code/plugins)
- [Agent SDK Documentation](https://docs.claude.com/en/api/agent-sdk/overview)

```

### File: examples\settings\README.md
```md
# Settings Examples

Example Claude Code settings files, primarily intended for organization-wide deployments. Use these are starting points — adjust them to fit your needs.

These may be applied at any level of the [settings hierarchy](https://code.claude.com/docs/en/settings#settings-files), though certain properties only take effect if specified in enterprise settings (e.g. `strictKnownMarketplaces`, `allowManagedHooksOnly`, `allowManagedPermissionRulesOnly`).


## Configuration Examples

> [!WARNING]
> These examples are community-maintained snippets which may be unsupported or incorrect. You are responsible for the correctness of your own settings configuration.

| Setting | [`settings-lax.json`](./settings-lax.json) | [`settings-strict.json`](./settings-strict.json) | [`settings-bash-sandbox.json`](./settings-bash-sandbox.json) |
|---------|:---:|:---:|:---:|
| Disable `--dangerously-skip-permissions` | ✅ | ✅ | |
| Block plugin marketplaces | ✅ | ✅ | |
| Block user and project-defined permission `allow` / `ask` / `deny` | | ✅ | ✅ |
| Block user and project-defined hooks | | ✅ | |
| Deny web fetch and search tools | | ✅ | |
| Bash tool requires approval | | ✅ | |
| Bash tool must run inside of sandbox | | | ✅ |

## Tips
- Consider merging snippets of the above examples to reach your desired configuration
- Settings files must be valid JSON
- Before deploying configuration files to your organization, test them locally by applying to `managed-settings.json`, `settings.json` or `settings.local.json`
- The `sandbox` property only applies to the `Bash` tool; it does not apply to other tools (like Read, Write, WebSearch, WebFetch, MCPs), hooks, or internal commands

## Full Documentation

See https://code.claude.com/docs/en/settings for complete documentation on all available managed settings.

```

### File: plugins\agent-sdk-dev\README.md
```md
# Agent SDK Development Plugin

A comprehensive plugin for creating and verifying Claude Agent SDK applications in Python and TypeScript.

## Overview

The Agent SDK Development Plugin streamlines the entire lifecycle of building Agent SDK applications, from initial scaffolding to verification against best practices. It helps you quickly start new projects with the latest SDK versions and ensures your applications follow official documentation patterns.

## Features

### Command: `/new-sdk-app`

Interactive command that guides you through creating a new Claude Agent SDK application.

**What it does:**
- Asks clarifying questions about your project (language, name, agent type, starting point)
- Checks for and installs the latest SDK version
- Creates all necessary project files and configuration
- Sets up proper environment files (.env.example, .gitignore)
- Provides a working example tailored to your use case
- Runs type checking (TypeScript) or syntax validation (Python)
- Automatically verifies the setup using the appropriate verifier agent

**Usage:**
```bash
/new-sdk-app my-project-name
```

Or simply:
```bash
/new-sdk-app
```

The command will interactively ask you:
1. Language choice (TypeScript or Python)
2. Project name (if not provided)
3. Agent type (coding, business, custom)
4. Starting point (minimal, basic, or specific example)
5. Tooling preferences (npm/yarn/pnpm or pip/poetry)

**Example:**
```bash
/new-sdk-app customer-support-agent
# → Creates a new Agent SDK project for a customer support agent
# → Sets up TypeScript or Python environment
# → Installs latest SDK version
# → Verifies the setup automatically
```

### Agent: `agent-sdk-verifier-py`

Thoroughly verifies Python Agent SDK applications for correct setup and best practices.

**Verification checks:**
- SDK installation and version
- Python environment setup (requirements.txt, pyproject.toml)
- Correct SDK usage and patterns
- Agent initialization and configuration
- Environment and security (.env, API keys)
- Error handling and functionality
- Documentation completeness

**When to use:**
- After creating a new Python SDK project
- After modifying an existing Python SDK application
- Before deploying a Python SDK application

**Usage:**
The agent runs automatically after `/new-sdk-app` creates a Python project, or you can trigger it by asking:
```
"Verify my Python Agent SDK application"
"Check if my SDK app follows best practices"
```

**Output:**
Provides a comprehensive report with:
- Overall status (PASS / PASS WITH WARNINGS / FAIL)
- Critical issues that prevent functionality
- Warnings about suboptimal patterns
- List of passed checks
- Specific recommendations with SDK documentation references

### Agent: `agent-sdk-verifier-ts`

Thoroughly verifies TypeScript Agent SDK applications for correct setup and best practices.

**Verification checks:**
- SDK installation and version
- TypeScript configuration (tsconfig.json)
- Correct SDK usage and patterns
- Type safety and imports
- Agent initialization and configuration
- Environment and security (.env, API keys)
- Error handling and functionality
- Documentation completeness

**When to use:**
- After creating a new TypeScript SDK project
- After modifying an existing TypeScript SDK application
- Before deploying a TypeScript SDK application

**Usage:**
The agent runs automatically after `/new-sdk-app` creates a TypeScript project, or you can trigger it by asking:
```
"Verify my TypeScript Agent SDK application"
"Check if my SDK app follows best practices"
```

**Output:**
Provides a comprehensive report with:
- Overall status (PASS / PASS WITH WARNINGS / FAIL)
- Critical issues that prevent functionality
- Warnings about suboptimal patterns
- List of passed checks
- Specific recommendations with SDK documentation references

## Workflow Example

Here's a typical workflow using this plugin:

1. **Create a new project:**
```bash
/new-sdk-app code-reviewer-agent
```

2. **Answer the interactive questions:**
```
Language: TypeScript
Agent type: Coding agent (code review)
Starting point: Basic agent with common features
```

3. **Automatic verification:**
The command automatically runs `agent-sdk-verifier-ts` to ensure everything is correctly set up.

4. **Start developing:**
```bash
# Set your API key
echo "ANTHROPIC_API_KEY=your_key_here" > .env

# Run your agent
npm start
```

5. **Verify after changes:**
```
"Verify my SDK application"
```

## Installation

This plugin is included in the Claude Code repository. To use it:

1. Ensure Claude Code is installed
2. The plugin commands and agents are automatically available

## Best Practices

- **Always use the latest SDK version**: `/new-sdk-app` checks for and installs the latest version
- **Verify before deploying**: Run the verifier agent before deploying to production
- **Keep API keys secure**: Never commit `.env` files or hardcode API keys
- **Follow SDK documentation**: The verifier agents check against official patterns
- **Type check TypeScript projects**: Run `npx tsc --noEmit` regularly
- **Test your agents**: Create test cases for your agent's functionality

## Resources

- [Agent SDK Overview](https://docs.claude.com/en/api/agent-sdk/overview)
- [TypeScript SDK Reference](https://docs.claude.com/en/api/agent-sdk/typescript)
- [Python SDK Reference](https://docs.claude.com/en/api/agent-sdk/python)
- [Agent SDK Examples](https://docs.claude.com/en/api/agent-sdk/examples)

## Troubleshooting

### Type errors in TypeScript project

**Issue**: TypeScript project has type errors after creation

**Solution**:
- The `/new-sdk-app` command runs type checking automatically
- If errors persist, check that you're using the latest SDK version
- Verify your `tsconfig.json` matches SDK requirements

### Python import errors

**Issue**: Cannot import from `claude_agent_sdk`

**Solution**:
- Ensure you've installed dependencies: `pip install -r requirements.txt`
- Activate your virtual environment if using one
- Check that the SDK is installed: `pip show claude-agent-sdk`

### Verification fails with warnings

**Issue**: Verifier agent reports warnings

**Solution**:
- Review the specific warnings in the report
- Check the SDK documentation references provided
- Warnings don't prevent functionality but indicate areas for improvement

## Author

Ashwin Bhat (ashwin@anthropic.com)

## Version

1.0.0

```

### File: plugins\claude-opus-4-5-migration\README.md
```md
# Claude Opus 4.5 Migration Plugin

Migrate your code and prompts from Sonnet 4.x and Opus 4.1 to Opus 4.5.

## Overview

This skill updates your code and prompts to be compatible with Opus 4.5. It automates the migration process, handling model strings, beta headers, and other configuration details. If you run into any issues with Opus 4.5 after migration, you can continue using this skill to adjust your prompts.

## Usage

```
"Migrate my codebase to Opus 4.5"
```

## Learn More

Refer to our [prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices) for best practices on prompting Claude models.

## Authors

William Hu (whu@anthropic.com)

```

### File: plugins\code-review\README.md
```md
# Code Review Plugin

Automated code review for pull requests using multiple specialized agents with confidence-based scoring to filter false positives.

## Overview

The Code Review Plugin automates pull request review by launching multiple agents in parallel to independently audit changes from different perspectives. It uses confidence scoring to filter out false positives, ensuring only high-quality, actionable feedback is posted.

## Commands

### `/code-review`

Performs automated code review on a pull request using multiple specialized agents.

**What it does:**
1. Checks if review is needed (skips closed, draft, trivial, or already-reviewed PRs)
2. Gathers relevant CLAUDE.md guideline files from the repository
3. Summarizes the pull request changes
4. Launches 4 parallel agents to independently review:
   - **Agents #1 & #2**: Audit for CLAUDE.md compliance
   - **Agent #3**: Scan for obvious bugs in changes
   - **Agent #4**: Analyze git blame/history for context-based issues
5. Scores each issue 0-100 for confidence level
6. Filters out issues below 80 confidence threshold
7. Outputs review (to terminal by default, or as PR comment with `--comment` flag)

**Usage:**
```bash
/code-review [--comment]
```

**Options:**
- `--comment`: Post the review as a comment on the pull request (default: outputs to terminal only)

**Example workflow:**
```bash
# On a PR branch, run locally (outputs to terminal):
/code-review

# Post review as PR comment:
/code-review --comment

# Claude will:
# - Launch 4 review agents in parallel
# - Score each issue for confidence
# - Output issues ≥80 confidence (to terminal or PR depending on flag)
# - Skip if no high-confidence issues found
```

**Features:**
- Multiple independent agents for comprehensive review
- Confidence-based scoring reduces false positives (threshold: 80)
- CLAUDE.md compliance checking with explicit guideline verification
- Bug detection focused on changes (not pre-existing issues)
- Historical context analysis via git blame
- Automatic skipping of closed, draft, or already-reviewed PRs
- Links directly to code with full SHA and line ranges

**Review comment format:**
```markdown
## Code review

Found 3 issues:

1. Missing error handling for OAuth callback (CLAUDE.md says "Always handle OAuth errors")

https://github.com/owner/repo/blob/abc123.../src/auth.ts#L67-L72

2. Memory leak: OAuth state not cleaned up (bug due to missing cleanup in finally block)

https://github.com/owner/repo/blob/abc123.../src/auth.ts#L88-L95

3. Inconsistent naming pattern (src/conventions/CLAUDE.md says "Use camelCase for functions")

https://github.com/owner/repo/blob/abc123.../src/utils.ts#L23-L28
```

**Confidence scoring:**
- **0**: Not confident, false positive
- **25**: Somewhat confident, might be real
- **50**: Moderately confident, real but minor
- **75**: Highly confident, real and important
- **100**: Absolutely certain, definitely real

**False positives filtered:**
- Pre-existing issues not introduced in PR
- Code that looks like a bug but isn't
- Pedantic nitpicks
- Issues linters will catch
- General quality issues (unless in CLAUDE.md)
- Issues with lint ignore comments

## Installation

This plugin is included in the Claude Code repository. The command is automatically available when using Claude Code.

## Best Practices

### Using `/code-review`
- Maintain clear CLAUDE.md files for better compliance checking
- Trust the 80+ confidence threshold - false positives are filtered
- Run on all non-trivial pull requests
- Review agent findings as a starting point for human review
- Update CLAUDE.md based on recurring review patterns

### When to use
- All pull requests with meaningful changes
- PRs touching critical code paths
- PRs from multiple contributors
- PRs where guideline compliance matters

### When not to use
- Closed or draft PRs (automatically skipped anyway)
- Trivial automated PRs (automatically skipped)
- Urgent hotfixes requiring immediate merge
- PRs already reviewed (automatically skipped)

## Workflow Integration

### Standard PR review workflow:
```bash
# Create PR with changes
# Run local review (outputs to terminal)
/code-review

# Review the automated feedback
# Make any necessary fixes

# Optionally post as PR comment
/code-review --comment

# Merge when ready
```

### As part of CI/CD:
```bash
# Trigger on PR creation or update
# Use --comment flag to post review comments
/code-review --comment
# Skip if review already exists
```

## Requirements

- Git repository with GitHub integration
- GitHub CLI (`gh`) installed and authenticated
- CLAUDE.md files (optional but recommended for guideline checking)

## Troubleshooting

### Review takes too long

**Issue**: Agents are slow on large PRs

**Solution**:
- Normal for large changes - agents run in parallel
- 4 independent agents ensure thoroughness
- Consider splitting large PRs into smaller ones

### Too many false positives

**Issue**: Review flags issues that aren't real

**Solution**:
- Default threshold is 80 (already filters most false positives)
- Make CLAUDE.md more specific about what matters
- Consider if the flagged issue is actually valid

### No review comment posted

**Issue**: `/code-review` runs but no comment appears

**Solution**:
Check if:
- PR is closed (reviews skipped)
- PR is draft (reviews skipped)
- PR is trivial/automated (reviews skipped)
- PR already has review (reviews skipped)
- No issues scored ≥80 (no comment needed)

### Link formatting broken

**Issue**: Code links don't render correctly in GitHub

**Solution**:
Links must follow this exact format:
```
https://github.com/owner/repo/blob/[full-sha]/path/file.ext#L[start]-L[end]
```
- Must use full SHA (not abbreviated)
- Must use `#L` notation
- Must include line range with at least 1 line of context

### GitHub CLI not working

**Issue**: `gh` commands fail

**Solution**:
- Install GitHub CLI: `brew install gh` (macOS) or see [GitHub CLI installation](https://cli.github.com/)
- Authenticate: `gh auth login`
- Verify repository has GitHub remote

## Tips

- **Write specific CLAUDE.md files**: Clear guidelines = better reviews
- **Include context in PRs**: Helps agents understand intent
- **Use confidence scores**: Issues ≥80 are usually correct
- **Iterate on guidelines**: Update CLAUDE.md based on patterns
- **Review automatically**: Set up as part of PR workflow
- **Trust the filtering**: Threshold prevents noise

## Configuration

### Adjusting confidence threshold

The default threshold is 80. To adjust, modify the command file at `commands/code-review.md`:
```markdown
Filter out any issues with a score less than 80.
```

Change `80` to your preferred threshold (0-100).

### Customizing review focus

Edit `commands/code-review.md` to add or modify agent tasks:
- Add security-focused agents
- Add performance analysis agents
- Add accessibility checking agents
- Add documentation quality checks

## Technical Details

### Agent architecture
- **2x CLAUDE.md compliance agents**: Redundancy for guideline checks
- **1x bug detector**: Focused on obvious bugs in changes only
- **1x history analyzer**: Context from git blame and history
- **Nx confidence scorers**: One per issue for independent scoring

### Scoring system
- Each issue independently scored 0-100
- Scoring considers evidence strength and verification
- Threshold (default 80) filters low-confidence issues
- For CLAUDE.md issues: verifies guideline explicitly mentions it

### GitHub integration
Uses `gh` CLI for:
- Viewing PR details and diffs
- Fetching repository data
- Reading git blame and history
- Posting review comments

## Author

Boris Cherny (boris@anthropic.com)

## Version

1.0.0

```

### File: plugins\commit-commands\README.md
```md
# Commit Commands Plugin

Streamline your git workflow with simple commands for committing, pushing, and creating pull requests.

## Overview

The Commit Commands Plugin automates common git operations, reducing context switching and manual command execution. Instead of running multiple git commands, use a single slash command to handle your entire workflow.

## Commands

### `/commit`

Creates a git commit with an automatically generated commit message based on staged and unstaged changes.

**What it does:**
1. Analyzes current git status
2. Reviews both staged and unstaged changes
3. Examines recent commit messages to match your repository's style
4. Drafts an appropriate commit message
5. Stages relevant files
6. Creates the commit

**Usage:**
```bash
/commit
```

**Example workflow:**
```bash
# Make some changes to your code
# Then simply run:
/commit

# Claude will:
# - Review your changes
# - Stage the files
# - Create a commit with an appropriate message
# - Show you the commit status
```

**Features:**
- Automatically drafts commit messages that match your repo's style
- Follows conventional commit practices
- Avoids committing files with secrets (.env, credentials.json)
- Includes Claude Code attribution in commit message

### `/commit-push-pr`

Complete workflow command that commits, pushes, and creates a pull request in one step.

**What it does:**
1. Creates a new branch (if currently on main)
2. Stages and commits changes with an appropriate message
3. Pushes the branch to origin
4. Creates a pull request using `gh pr create`
5. Provides the PR URL

**Usage:**
```bash
/commit-push-pr
```

**Example workflow:**
```bash
# Make your changes
# Then run:
/commit-push-pr

# Claude will:
# - Create a feature branch (if needed)
# - Commit your changes
# - Push to remote
# - Open a PR with summary and test plan
# - Give you the PR URL to review
```

**Features:**
- Analyzes all commits in the branch (not just the latest)
- Creates comprehensive PR descriptions with:
  - Summary of changes (1-3 bullet points)
  - Test plan checklist
  - Claude Code attribution
- Handles branch creation automatically
- Uses GitHub CLI (`gh`) for PR creation

**Requirements:**
- GitHub CLI (`gh`) must be installed and authenticated
- Repository must have a remote named `origin`

### `/clean_gone`

Cleans up local branches that have been deleted from the remote repository.

**What it does:**
1. Lists all local branches to identify [gone] status
2. Identifies and removes worktrees associated with [gone] branches
3. Deletes all branches marked as [gone]
4. Provides feedback on removed branches

**Usage:**
```bash
/clean_gone
```

**Example workflow:**
```bash
# After PRs are merged and remote branches are deleted
/clean_gone

# Claude will:
# - Find all branches marked as [gone]
# - Remove any associated worktrees
# - Delete the stale local branches
# - Report what was cleaned up
```

**Features:**
- Handles both regular branches and worktree branches
- Safely removes worktrees before deleting branches
- Shows clear feedback about what was removed
- Reports if no cleanup was needed

**When to use:**
- After merging and deleting remote branches
- When your local branch list is cluttered with stale branches
- During regular repository maintenance

## Installation

This plugin is included in the Claude Code repository. The commands are automatically available when using Claude Code.

## Best Practices

### Using `/commit`
- Review the staged changes before committing
- Let Claude analyze your changes and match your repo's commit style
- Trust the automated message, but verify it's accurate
- Use for routine commits during development

### Using `/commit-push-pr`
- Use when you're ready to create a PR
- Ensure all your changes are complete and tested
- Claude will analyze the full branch history for the PR description
- Review the PR description and edit if needed
- Use when you want to minimize context switching

### Using `/clean_gone`
- Run periodically to keep your branch list clean
- Especially useful after merging multiple PRs
- Safe to run - only removes branches already deleted remotely
- Helps maintain a tidy local repository

## Workflow Integration

### Quick commit workflow:
```bash
# Write code
/commit
# Continue development
```

### Feature branch workflow:
```bash
# Develop feature across multiple commits
/commit  # First commit
# More changes
/commit  # Second commit
# Ready to create PR
/commit-push-pr
```

### Maintenance workflow:
```bash
# After several PRs are merged
/clean_gone
# Clean workspace ready for next feature
```

## Requirements

- Git must be installed and configured
- For `/commit-push-pr`: GitHub CLI (`gh`) must be installed and authenticated
- Repository must be a git repository with a remote

## Troubleshooting

### `/commit` creates empty commit

**Issue**: No changes to commit

**Solution**:
- Ensure you have unstaged or staged changes
- Run `git status` to verify changes exist

### `/commit-push-pr` fails to create PR

**Issue**: `gh pr create` command fails

**Solution**:
- Install GitHub CLI: `brew install gh` (macOS) or see [GitHub CLI installation](https://cli.github.com/)
- Authenticate: `gh auth login`
- Ensure repository has a GitHub remote

### `/clean_gone` doesn't find branches

**Issue**: No branches marked as [gone]

**Solution**:
- Run `git fetch --prune` to update remote tracking
- Branches must be deleted from the remote to show as [gone]

## Tips

- **Combine with other tools**: Use `/commit` during development, then `/commit-push-pr` when ready
- **Let Claude draft messages**: The commit message analysis learns from your repo's style
- **Regular cleanup**: Run `/clean_gone` weekly to maintain a clean branch list
- **Review before pushing**: Always review the commit message and changes before pushing

## Author

Anthropic (support@anthropic.com)

## Version

1.0.0

```

### File: plugins\explanatory-output-style\README.md
```md
# Explanatory Output Style Plugin

This plugin recreates the deprecated Explanatory output style as a SessionStart
hook.

WARNING: Do not install this plugin unless you are fine with incurring the token
cost of this plugin's additional instructions and output.

## What it does

When enabled, this plugin automatically adds instructions at the start of each
session that encourage Claude to:

1. Provide educational insights about implementation choices
2. Explain codebase patterns and decisions
3. Balance task completion with learning opportunities

## How it works

The plugin uses a SessionStart hook to inject additional context into every
session. This context instructs Claude to provide brief educational explanations
before and after writing code, formatted as:

```
`★ Insight ─────────────────────────────────────`
[2-3 key educational points]
`─────────────────────────────────────────────────`
```

## Usage

Once installed, the plugin activates automatically at the start of every
session. No additional configuration is needed.

The insights focus on:

- Specific implementation choices for your codebase
- Patterns and conventions in your code
- Trade-offs and design decisions
- Codebase-specific details rather than general programming concepts

## Migration from Output Styles

This plugin replaces the deprecated "Explanatory" output style setting. If you
previously used:

```json
{
  "outputStyle": "Explanatory"
}
```

You can now achieve the same behavior by installing this plugin instead.

More generally, this SessionStart hook pattern is roughly equivalent to
CLAUDE.md, but it is more flexible and allows for distribution through plugins.

Note: Output styles that involve tasks besides software development, are better
expressed as
[subagents](https://docs.claude.com/en/docs/claude-code/sub-agents), not as
SessionStart hooks. Subagents change the system prompt while SessionStart hooks
add to the default system prompt.

## Managing changes

- Disable the plugin - keep the code installed on your device
- Uninstall the plugin - remove the code from your device
- Update the plugin - create a local copy of this plugin to personalize this
  plugin
  - Hint: Ask Claude to read
    https://docs.claude.com/en/docs/claude-code/plugins.md and set it up for
    you!

```

### File: plugins\feature-dev\README.md
```md
# Feature Development Plugin

A comprehensive, structured workflow for feature development with specialized agents for codebase exploration, architecture design, and quality review.

## Overview

The Feature Development Plugin provides a systematic 7-phase approach to building new features. Instead of jumping straight into code, it guides you through understanding the codebase, asking clarifying questions, designing architecture, and ensuring quality—resulting in better-designed features that integrate seamlessly with your existing code.

## Philosophy

Building features requires more than just writing code. You need to:
- **Understand the codebase** before making changes
- **Ask questions** to clarify ambiguous requirements
- **Design thoughtfully** before implementing
- **Review for quality** after building

This plugin embeds these practices into a structured workflow that runs automatically when you use the `/feature-dev` command.

## Command: `/feature-dev`

Launches a guided feature development workflow with 7 distinct phases.

**Usage:**
```bash
/feature-dev Add user authentication with OAuth
```

Or simply:
```bash
/feature-dev
```

The command will guide you through the entire process interactively.

## The 7-Phase Workflow

### Phase 1: Discovery

**Goal**: Understand what needs to be built

**What happens:**
- Clarifies the feature request if it's unclear
- Asks what problem you're solving
- Identifies constraints and requirements
- Summarizes understanding and confirms with you

**Example:**
```
You: /feature-dev Add caching
Claude: Let me understand what you need...
        - What should be cached? (API responses, computed values, etc.)
        - What are your performance requirements?
        - Do you have a preferred caching solution?
```

### Phase 2: Codebase Exploration

**Goal**: Understand relevant existing code and patterns

**What happens:**
- Launches 2-3 `code-explorer` agents in parallel
- Each agent explores different aspects (similar features, architecture, UI patterns)
- Agents return comprehensive analyses with key files to read
- Claude reads all identified files to build deep understanding
- Presents comprehensive summary of findings

**Agents launched:**
- "Find features similar to [feature] and trace implementation"
- "Map the architecture and abstractions for [area]"
- "Analyze current implementation of [related feature]"

**Example output:**
```
Found similar features:
- User authentication (src/auth/): Uses JWT tokens, middleware pattern
- Session management (src/session/): Redis-backed, 24hr expiry
- API security (src/api/middleware/): Rate limiting, CORS

Key files to understand:
- src/auth/AuthService.ts:45 - Core authentication logic
- src/middleware/authMiddleware.ts:12 - Request authentication
- src/config/security.ts:8 - Security configuration
```

### Phase 3: Clarifying Questions

**Goal**: Fill in gaps and resolve all ambiguities

**What happens:**
- Reviews codebase findings and feature request
- Identifies underspecified aspects:
  - Edge cases
  - Error handling
  - Integration points
  - Backward compatibility
  - Performance needs
- Presents all questions in an organized list
- **Waits for your answers before proceeding**

**Example:**
```
Before designing the architecture, I need to clarify:

1. OAuth provider: Which OAuth providers? (Google, GitHub, custom?)
2. User data: Store OAuth tokens or just user profile?
3. Existing auth: Replace current auth or add alongside?
4. Sessions: Integrate with existing session management?
5. Error handling: How to handle OAuth failures?
```

**Critical**: This phase ensures nothing is ambiguous before design begins.

### Phase 4: Architecture Design

**Goal**: Design multiple implementation approaches

**What happens:**
- Launches 2-3 `code-architect` agents with different focuses:
  - **Minimal changes**: Smallest change, maximum reuse
  - **Clean architecture**: Maintainability, elegant abstractions
  - **Pragmatic balance**: Speed + quality
- Reviews all approaches
- Forms opinion on which fits best for this task
- Presents comparison with trade-offs and recommendation
- **Asks which approach you prefer**

**Example output:**
```
I've designed 3 approaches:

Approach 1: Minimal Changes
- Extend existing AuthService with OAuth methods
- Add new OAuth routes to existing auth router
- Minimal refactoring required
Pros: Fast, low risk
Cons: Couples OAuth to existing auth, harder to test

Approach 2: Clean Architecture
- New OAuthService with dedicated interface
- Separate OAuth router and middleware
- Refactor AuthService to use common interface
Pros: Clean separation, testable, maintainable
Cons: More files, more refactoring

Approach 3: Pragmatic Balance
- New OAuthProvider abstraction
- Integrate into existing AuthService
- Minimal refactoring, good boundaries
Pros: Balanced complexity and cleanliness
Cons: Some coupling remains

Recommendation: Approach 3 - gives you clean boundaries without
excessive refactoring, and fits your existing architecture well.

Which approach would you like to use?
```

### Phase 5: Implementation

**Goal**: Build the feature

**What happens:**
- **Waits for explicit approval** before starting
- Reads all relevant files identified in previous phases
- Implements following chosen architecture
- Follows codebase conventions strictly
- Writes clean, well-documented code
- Updates todos as progress is made

**Notes:**
- Implementation only starts after you approve
- Follows patterns discovered in Phase 2
- Uses architecture designed in Phase 4
- Continuously tracks progress

### Phase 6: Quality Review

**Goal**: Ensure code is simple, DRY, elegant, and functionally correct

**What happens:**
- Launches 3 `code-reviewer` agents in parallel with different focuses:
  - **Simplicity/DRY/Elegance**: Code quality and maintainability
  - **Bugs/Correctness**: Functional correctness and logic errors
  - **Conventions/Abstractions**: Project standards and patterns
- Consolidates findings
- Identifies highest severity issues
- **Presents findings and asks what you want to do**:
  - Fix now
  - Fix later
  - Proceed as-is
- Addresses issues based on your decision

**Example output:**
```
Code Review Results:

High Priority Issues:
1. Missing error handling in OAuth callback (src/auth/oauth.ts:67)
2. Memory leak: OAuth state not cleaned up (src/auth/oauth.ts:89)

Medium Priority:
1. Could simplify token refresh logic (src/auth/oauth.ts:120)
2. Consider extracting OAuth config validation

All tests pass. Code follows project conventions.

What would you like to do?
```

### Phase 7: Summary

**Goal**: Document what was accomplished

**What happens:**
- Marks all todos complete
- Summarizes:
  - What was built
  - Key decisions made
  - Files modified
  - Suggested next steps

**Example:**
```
Feature Complete: OAuth Authentication

What was built:
- OAuth provider abstraction supporting Google and GitHub
- OAuth routes and middleware integrated with existing auth
- Token refresh and session integration
- Error handling for all OAuth flows

Key decisions:
- Used pragmatic approach with OAuthProvider abstraction
- Integrated with existing session management
- Added OAuth state to prevent CSRF

Files modified:
- src/auth/OAuthProvider.ts (new)
- src/auth/AuthService.ts
- src/routes/auth.ts
- src/middleware/authMiddleware.ts

Suggested next steps:
- Add tests for OAuth flows
- Add more OAuth providers (Microsoft, Apple)
- Update documentation
```

## Agents

### `code-explorer`

**Purpose**: Deeply analyzes existing codebase features by tracing execution paths

**Focus areas:**
- Entry points and call chains
- Data flow and transformations
- Architecture layers and patterns
- Dependencies and integrations
- Implementation details

**When triggered:**
- Automatically in Phase 2
- Can be invoked manually when exploring code

**Output:**
- Entry points with file:line references
- Step-by-step execution flow
- Key components and responsibilities
- Architecture insights
- List of essential files to read

### `code-architect`

**Purpose**: Designs feature architectures and implementation blueprints

**Focus areas:**
- Codebase pattern analysis
- Architecture decisions
- Component design
- Implementation roadmap
- Data flow and build sequence

**When triggered:**
- Automatically in Phase 4
- Can be invoked manually for architecture design

**Output:**
- Patterns and conventions found
- Architecture decision with rationale
- Complete component design
- Implementation map with specific files
- Build sequence with phases

### `code-reviewer`

**Purpose**: Reviews code for bugs, quality issues, and project conventions

**Focus areas:**
- Project guideline compliance (CLAUDE.md)
- Bug detection
- Code quality issues
- Confidence-based filtering (only reports high-confidence issues ≥80)

**When triggered:**
- Automatically in Phase 6
- Can be invoked manually after writing code

**Output:**
- Critical issues (confidence 75-100)
- Important issues (confidence 50-74)
- Specific fixes with file:line references
- Project guideline references

## Usage Patterns

### Full workflow (recommended for new features):
```bash
/feature-dev Add rate limiting to API endpoints
```

Let the workflow guide you through all 7 phases.

### Manual agent invocation:

**Explore a feature:**
```
"Launch code-explorer to trace how authentication works"
```

**Design architecture:**
```
"Launch code-architect to design the caching layer"
```

**Review code:**
```
"Launch code-reviewer to check my recent changes"
```

## Best Practices

1. **Use the full workflow for complex features**: The 7 phases ensure thorough planning
2. **Answer clarifying questions thoughtfully**: Phase 3 prevents future confusion
3. **Choose architecture deliberately**: Phase 4 gives you options for a reason
4. **Don't skip code review**: Phase 6 catches issues before they reach production
5. **Read the suggested files**: Phase 2 identifies key files—read them to understand context

## When to Use This Plugin

**Use for:**
- New features that touch multiple files
- Features requiring architectural decisions
- Complex integrations with existing code
- Features where requirements are somewhat unclear

**Don't use for:**
- Single-line bug fixes
- Trivial changes
- Well-defined, simple tasks
- Urgent hotfixes

## Requirements

- Claude Code installed
- Git repository (for code review)
- Project with existing codebase (workflow assumes existing code to learn from)

## Troubleshooting

### Agents take too long

**Issue**: Code exploration or architecture agents are slow

**Solution**:
- This is normal for large codebases
- Agents run in parallel when possible
- The thoroughness pays off in better understanding

### Too many clarifying questions

**Issue**: Phase 3 asks too many questions

**Solution**:
- Be more specific in your initial feature request
- Provide context about constraints upfront
- Say "whatever you think is best" if truly no preference

### Architecture options overwhelming

**Issue**: Too many architecture options in Phase 4

**Solution**:
- Trust the recommendation—it's based on codebase analysis
- If still unsure, ask for more explanation
- Pick the pragmatic option when in doubt

## Tips

- **Be specific in your feature request**: More detail = fewer clarifying questions
- **Trust the process**: Each phase builds on the previous one
- **Review agent outputs**: Agents provide valuable insights about your codebase
- **Don't skip phases**: Each phase serves a purpose
- **Use for learning**: The exploration phase teaches you about your own codebase

## Author

Sid Bidasaria (sbidasaria@anthropic.com)

## Version

1.0.0

```

### File: plugins\frontend-design\README.md
```md
# Frontend Design Plugin

Generates distinctive, production-grade frontend interfaces that avoid generic AI aesthetics.

## What It Does

Claude automatically uses this skill for frontend work. Creates production-ready code with:

- Bold aesthetic choices
- Distinctive typography and color palettes
- High-impact animations and visual details
- Context-aware implementation

## Usage

```
"Create a dashboard for a music streaming app"
"Build a landing page for an AI security startup"
"Design a settings panel with dark mode"
```

Claude will choose a clear aesthetic direction and implement production code with meticulous attention to detail.

## Learn More

See the [Frontend Aesthetics Cookbook](https://github.com/anthropics/claude-cookbooks/blob/main/coding/prompting_for_frontend_aesthetics.ipynb) for detailed guidance on prompting for high-quality frontend design.

## Authors

Prithvi Rajasekaran (prithvi@anthropic.com)
Alexander Bricken (alexander@anthropic.com)

```

### File: plugins\hookify\README.md
```md
# Hookify Plugin

Easily create custom hooks to prevent unwanted behaviors by analyzing conversation patterns or from explicit instructions.

## Overview

The hookify plugin makes it simple to create hooks without editing complex `hooks.json` files. Instead, you create lightweight markdown configuration files that define patterns to watch for and messages to show when those patterns match.

**Key features:**
- 🎯 Analyze conversations to find unwanted behaviors automatically
- 📝 Simple markdown configuration files with YAML frontmatter
- 🔍 Regex pattern matching for powerful rules
- 🚀 No coding required - just describe the behavior
- 🔄 Easy enable/disable without restarting

## Quick Start

### 1. Create Your First Rule

```bash
/hookify Warn me when I use rm -rf commands
```

This analyzes your request and creates `.claude/hookify.warn-rm.local.md`.

### 2. Test It Immediately

**No restart needed!** Rules take effect on the very next tool use.

Ask Claude to run a command that should trigger the rule:
```
Run rm -rf /tmp/test
```

You should see the warning message immediately!

## Usage

### Main Command: /hookify

**With arguments:**
```
/hookify Don't use console.log in TypeScript files
```
Creates a rule from your explicit instructions.

**Without arguments:**
```
/hookify
```
Analyzes recent conversation to find behaviors you've corrected or been frustrated by.

### Helper Commands

**List all rules:**
```
/hookify:list
```

**Configure rules interactively:**
```
/hookify:configure
```
Enable/disable existing rules through an interactive interface.

**Get help:**
```
/hookify:help
```

## Rule Configuration Format

### Simple Rule (Single Pattern)

`.claude/hookify.dangerous-rm.local.md`:
```markdown
---
name: block-dangerous-rm
enabled: true
event: bash
pattern: rm\s+-rf
action: block
---

⚠️ **Dangerous rm command detected!**

This command could delete important files. Please:
- Verify the path is correct
- Consider using a safer approach
- Make sure you have backups
```

**Action field:**
- `warn`: Shows warning but allows operation (default)
- `block`: Prevents operation from executing (PreToolUse) or stops session (Stop events)

### Advanced Rule (Multiple Conditions)

`.claude/hookify.sensitive-files.local.md`:
```markdown
---
name: warn-sensitive-files
enabled: true
event: file
action: warn
conditions:
  - field: file_path
    operator: regex_match
    pattern: \.env$|credentials|secrets
  - field: new_text
    operator: contains
    pattern: KEY
---

🔐 **Sensitive file edit detected!**

Ensure credentials are not hardcoded and file is in .gitignore.
```

**All conditions must match** for the rule to trigger.

## Event Types

- **`bash`**: Triggers on Bash tool commands
- **`file`**: Triggers on Edit, Write, MultiEdit tools
- **`stop`**: Triggers when Claude wants to stop (for completion checks)
- **`prompt`**: Triggers on user prompt submission
- **`all`**: Triggers on all events

## Pattern Syntax

Use Python regex syntax:

| Pattern | Matches | Example |
|---------|---------|---------|
| `rm\s+-rf` | rm -rf | rm -rf /tmp |
| `console\.log\(` | console.log( | console.log("test") |
| `(eval\|exec)\(` | eval( or exec( | eval("code") |
| `\.env$` | files ending in .env | .env, .env.local |
| `chmod\s+777` | chmod 777 | chmod 777 file.txt |

**Tips:**
- Use `\s` for whitespace
- Escape special chars: `\.` for literal dot
- Use `|` for OR: `(foo|bar)`
- Use `.*` to match anything
- Set `action: block` for dangerous operations
- Set `action: warn` (or omit) for informational warnings

## Examples

### Example 1: Block Dangerous Commands

```markdown
---
name: block-destructive-ops
enabled: true
event: bash
pattern: rm\s+-rf|dd\s+if=|mkfs|format
action: block
---

🛑 **Destructive operation detected!**

This command can cause data loss. Operation blocked for safety.
Please verify the exact path and use a safer approach.
```

**This rule blocks the operation** - Claude will not be allowed to execute these commands.

### Example 2: Warn About Debug Code

```markdown
---
name: warn-debug-code
enabled: true
event: file
pattern: console\.log\(|debugger;|print\(
action: warn
---

🐛 **Debug code detected**

Remember to remove debugging statements before committing.
```

**This rule warns but allows** - Claude sees the message but can still proceed.

### Example 3: Require Tests Before Stopping

```markdown
---
name: require-tests-run
enabled: false
event: stop
action: block
conditions:
  - field: transcript
    operator: not_contains
    pattern: npm test|pytest|cargo test
---

**Tests not detected in transcript!**

Before stopping, please run tests to verify your changes work correctly.
```

**This blocks Claude from stopping** if no test commands appear in the session transcript. Enable only when you want strict enforcement.

## Advanced Usage

### Multiple Conditions

Check multiple fields simultaneously:

```markdown
---
name: api-key-in-typescript
enabled: true
event: file
conditions:
  - field: file_path
    operator: regex_match
    pattern: \.tsx?$
  - field: new_text
    operator: regex_match
    pattern: (API_KEY|SECRET|TOKEN)\s*=\s*["']
---

🔐 **Hardcoded credential in TypeScript!**

Use environment variables instead of hardcoded values.
```

### Operators Reference

- `regex_match`: Pattern must match (most common)
- `contains`: String must contain pattern
- `equals`: Exact string match
- `not_contains`: String must NOT contain pattern
- `starts_with`: String starts with pattern
- `ends_with`: String ends with pattern

### Field Reference

**For bash events:**
- `command`: The bash command string

**For file events:**
- `file_path`: Path to file being edited
- `new_text`: New content being added (Edit, Write)
- `old_text`: Old content being replaced (Edit only)
- `content`: File content (Write only)

**For prompt events:**
- `user_prompt`: The user's submitted prompt text

**For stop events:**
- Use general matching on session state

## Management

### Enable/Disable Rules

**Temporarily disable:**
Edit the `.local.md` file and set `enabled: false`

**Re-enable:**
Set `enabled: true`

**Or use interactive tool:**
```
/hookify:configure
```

### Delete Rules

Simply delete the `.local.md` file:
```bash
rm .claude/hookify.my-rule.local.md
```

### View All Rules

```
/hookify:list
```

## Installation

This plugin is part of the Claude Code Marketplace. It should be auto-discovered when the marketplace is installed.

**Manual testing:**
```bash
cc --plugin-dir /path/to/hookify
```

## Requirements

- Python 3.7+
- No external dependencies (uses stdlib only)

## Troubleshooting

**Rule not triggering:**
1. Check rule file exists in `.claude/` directory (in project root, not plugin directory)
2. Verify `enabled: true` in frontmatter
3. Test regex pattern separately
4. Rules should work immediately - no restart needed
5. Try `/hookify:list` to see if rule is loaded

**Import errors:**
- Ensure Python 3 is available: `python3 --version`
- Check hookify plugin is installed

**Pattern not matching:**
- Test regex: `python3 -c "import re; print(re.search(r'pattern', 'text'))"`
- Use unquoted patterns in YAML to avoid escaping issues
- Start simple, then add complexity

**Hook seems slow:**
- Keep patterns simple (avoid complex regex)
- Use specific event types (bash, file) instead of "all"
- Limit number of active rules

## Contributing

Found a useful rule pattern? Consider sharing example files via PR!

## Future Enhancements

- Severity levels (error/warning/info distinctions)
- Rule templates library
- Interactive pattern builder
- Hook testing utilities
- JSON format support (in addition to markdown)

## License

MIT License

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
