---
id: github.com-buildermethods-agent-os-59809cca-knowle
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:35.976844
---

# KNOWLEDGE EXTRACT: github.com_buildermethods_agent-os_59809cca
> **Extracted on:** 2026-04-01 15:32:59
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007524587/github.com_buildermethods_agent-os_59809cca

---

## File: `.gitignore`
```
# macOS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# IDE
.vscode/
.idea/
*.swp
*.swo

# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Dependencies
node_modules/

# Temporary files
*.tmp
*.temp
```

## File: `CHANGELOG.md`
```markdown
# Changelog

Get notified of major releases by subscribing here:
https://buildermethods.com/agent-os

## [3.0] - 2026-01-20

Agent OS v3 is a major release that refocuses the framework on what it does best—establishing and injecting standards—while deferring to modern AI tools for the parts they now handle better.

**[Full v3 documentation and video walkthrough →](https://buildermethods.com/agent-os)**

### Why the major version bump?

AI coding tools have evolved significantly since Agent OS's original release in mid-2025. Claude Code's plan mode, extended thinking, and improved models now handle much of the scaffolding that earlier versions provided:

- **Spec writing** — Now best handled using Plan mode
- **Task breakdown** — Tools like Claude Code automatically create and track todo lists
- **Implementation orchestration** — Frontier models manage task delegation on their own

Rather than reinvent these functions, v3 focuses on Agent OS's core strengths: establishing standards, injecting them smartly, and enhancing spec-driven development.

### What's new in v3

**New standards tools:**
- `/discover-standards` — Lets the agent surface, suggest, and create standards from your codebase
- `/inject-standards` — Injects relevant standards into any context (conversations, plans, Claude Skills) using the new `index.yml` file for automatic detection
- **Sync script** — Syncs project standards back to your base profiles

**Spec workflow changes:**
- Spec creation now defers to **Plan Mode** (Claude Code, Cursor, or any agent with plan mode)—the industry-standard approach to spec-driven development in 2026+
- `/shape-spec` enhances plan mode by prompting targeted questions that consider your standards and product mission, then saves the resulting plan to your Agent OS spec folder

**Simplified architecture:**
- Profile inheritance now defined in main `config.yml` instead of separate files
- Product planning phase streamlined with AskUserQuestion tool integration
- Implementation/orchestration phases retired—frontier models handle this well on their own now

### Backward compatibility

**Your content stays the same.** Standards, specs, and product docs use the same format and transfer directly to v3.

**Commands and scripts are new.** The installation process is simpler, but commands are different. Use `/inject-standards` to bake your standards into subagents, Claude Skills, or any prompt you create.

v2 documentation remains available for those who prefer to stay on v2, but v3 is recommended for all new projects.

## [2.1.1] - 2025-10-29

- Replaced references to 'spec-researcher' (depreciated agent name) with 'spec-shaper'.
- Clarified --dry-run output to user to reassure we're in dry-run mode
- Tightened up template and istructions for writing spec.md, aiming to keep it shorter, easier to scan, and covering only the essentials.
- Tweaked create-task-list workflow for consistency.
- When planning product roadmap, removed instruction to limit it to 12 items.

## [2.1.0] - 2025-10-21

Version 2.1 implemented a round of significant changes to how things work in Agent OS.  Here is a summary of what's new in version 2.1.0:

### TL;DR

Here's the brief overview. It's all detailed below and the [docs](https://buildermethods.com/agent-os) have been updated to reflect all of this.

- Option to leverage Claude Code's new "Skills" feature for reading standards
- Option to enable or disable delegating to Claude Code subagents
- Replaced "single/multi-agent modes" with more flexible configuration options
- Retired the short-lived "roles" system. Too complex, and better handled with standard tooling (more below).
- Removed documentation & verification bloat
- Went from 4 to 6 more specific development phases (use 'em all or pick and choose!):
  1. plan-product -- (no change) Plan your product's mission & roadmap
  2. shape-spec -- For shaping and planning a feature before writing it up
  3. write-spec -- For writing your spec.md
  4. create-tasks -- For creating your tasks.md
  5. implement-tasks -- Simple single-agent implementation of tasks.md
  6. orchestrate-tasks -- For more advanced, fine-grain control and multi-agent orchestration of tasks.md.
- Simplified & improved project upgrade script

Let's unpack these updates in detail:

### Claude Code Skills support

2.1 adds official support for [Claude Code Skills](https://docs.claude.com/en/brain/knowledge/docs_legacy/claude-code/skills).

When the config option standards_as_claude_code_skills is true, this will convert all of your standards into Claude Code Skills and _not_ inject references to those Standards like Agent OS normally would.

2.1 also provides a Claude Code command, `improve-skills` which you **definitely should** run after installing Agent OS in your project with the skills option turned on.  This command is designed to improve and rewrite each of your Claude Code Skills descriptions to make them more useable and discoverable by Claude Code.

### Enable/Disable delegation to Claude Code subagents

2.1 introduces an config option to enable or disable delegating tasks to Claude Code subagents.  You can disable subagents by setting use_claude_code_subagents to false.

When set to false, and when using Claude Code, you can still run Agent OS commands in Claude Code, and instead of delegating most tasks to subagents, Claude Code's main agent will execute everything.

While you lose some context efficiency of using subagents, you can token efficiency and some speed gains without the use of subagents.

### Replaced "single-agent & multi-agent modes" with new config options

2.0.x had introduced the concepts of multi-agent and single-agent modes, where multi-agent mode was designed for using Claude Code with subagents.  This naming and configuration design proved suboptimal and inflexible, so 2.1.0 does away with the terms "single-agent mode" and "multi-agent mode".

Now we configure Agent OS using these boolean options in your base ~/agent-os/config.yml:

claude_code_commands: true/false
use_claude_code_subagents: true/false
agent_os_commands: true/false

The benefits of this new configuration approach are:

- Now you can use Agent OS with Claude Code *with* or *without* delegating to subagents.  (subagents bring many benefits like context efficiency, but also come with some tradeoffs—higher token usage, less transparency, slower to finish tasks).

- Before, when you had *both* single-agent and multi-agent modes enabled, your project's agent-os/commands/ folder ended up with "multi-agent/" and "single-agent/" subfolders for each command, which is confusing and clumsy to use.  Now in 2.1.0, your project's agent-os/commands/ folder will not have these additional "modes" subfolders.

- Easier to integrate additional feature configurations as they become available, so that you can mix and match the exact set of features that fit your preferred coding tools and workflow style.  For example, we're also introducing an option to make use of the new Claude Code Skills feature (or you can opt out).  More on this below.

### Retired (short-lived) "Roles" system

2.0.x had introduced a concept of "Roles", where your roles/implementers.yml and roles/verifiers.yml contained convoluted lists of agents that could be assigned to implement tasks.  It also had a script for adding additional "roles".

All of that is removed in 2.1.0.  That system added no real benefit over simply using available tooling (like Claude Code's own subagent generator) for spinning up your subagents.

2.1.0 introduces an 'orchestrate-tasks' phase, which achieves the same thing that the old "Roles" system intended:  Advanced orchestration of multiple specialized subagents to carry out a complex implementation.  More on this below.

### Removed documentation & verification bloat

2.0.x had introduced a bunch of "bloat" that quickly proved unnecessary and inefficient.  These bits have been removed in 2.1.0:

- Verification of your spec (although the spec-verifier Claude Code subagent is still available for you to call on, if/when you want)
- Documentation of every task's implementation
- Specialized verifiers (backend-verifier, frontend-verifier)

The final overall verification step for a spec's implementation remains intact.

### From 4 to 6 more specific development phases

While some users use all of Agent OS' workflow for everything, many have been picking the parts they find useful and discarding those that don't fit their workflow—AS THEY SHOULD!

2.1.0 establishes this as a core principle of Agent OS:  You can use as much or as little of it as you want!

With that in mind, we've moved from 4 to 6 different phases of development that can _potentially_ be powered by Agent OS:

1. `plan-product` -- No changes here.  This is for establishing your product's mission, roadmap and tech-stack.

2. `shape-spec` -- Use this when you need to take your rough idea for a feature and shape it into a well-scoped and strategized plan, before officially writing it up.  This is where the agent asks you clarifying questions and ends up producing your requirements.md.
  - Already got your requirements shaped?  Skip this and drop those right into your spec's requirements.md 👍

3. `write-spec` -- Takes your requirements.md and formalizes it into a clear and concise spec.md.

4. `create-tasks` -- Takes your spec.md and breaks it down into a tasks list, grouped, prioritized and ready for implementation.

5. `implement-tasks` -- Just want to build right now(!), then use this to implement your tasks.md with your main agent.

6. `orchestrate-tasks` -- Got a big complex feature and want to orchestrate multiple agents, with more fine-grain control over their contexts?  Use this.  It provides a structure to delegate your task groups to any Claude Code subagents you've created.  Or if you're not using Claude Code, it generates targeted prompt files (as was established in 2.0.x).

### Simplified & improved project upgrade script

Now whenever you need to upgrade your Agent OS project installation (to a new version or to push configuration changes or standards changes to a project), now when you run project-install.sh or project-update.sh, the system will:

- Check and compare your incoming version & configs to your current project's
- Show you what will stay intact or be removed & re-installed
- Ask you to confirm to proceed.


## [2.0.5] - 2025-10-16

- Updated base installation update options to include a "Full update" option, which is the easiest way to pull and update the latest Agent OS stuff (default profile, scripts) without losing your base installation's custom profiles.
- The "Full update" option also dynamically updates your base install config.yml version number without changing your configurations.

## [2.0.4] - 2025-10-14

- Fixed multi-agent-mode not installing the roles/ files in the project agent-os folder.
- Clarified spec-research instructions.
- In single-agent mode, added verification prompt generation to the implementation phase.

## [2.0.3] - 2025-10-10

- Updated instructions and default standards to reduce excessive tests writing and test running during feature development to improve speed and token useage.
- For Claude Code users:
  - Replaced hard-coding of 'opus' model setting on agents with 'inherit' so that it inherits whichever model your Claude Code is currently using.
  - Updated create-role script to add the "Inherit" option when creating new agents.

## [2.0.2] - 2025-10-09

- Clarified /create-spec command so that task list creation doesn't begin until spec.md has been written.
- Clarified spec-writer workflow to ensure actual code isn't written in spec.md.
- Fixed instructions to ensure spec-verification.md is stored in the spec's verication folder.
- Ensured Claude Code subagents are installed to a project's .claude/agents/agent-os and not sub-folders within that.
- Fixed compilation of Claude Code implementer and verifier agents not replacing their dynamic tags.
- Added instruction in single-agent mode to inform user of next command to run during spec creation process.

## [2.0.1] - 2025-10-08

### Fixed

#### Installation Script Compatibility Issues

Fixed bugs in the project installation scripts (`project-install.sh`, `project-update.sh`, and `common-functions.sh`) that caused installations to fail in certain bash environments. These issues were triggered by stricter bash implementations and configurations, particularly when `set -e` (exit on error) was enabled.

## [2.0.0] - 2025-10-07

Agent OS 2.0 is a major new release that brings several core architectural changes and improvements.

The big headline here is the dual mode architecture for supporting both multi-agent tools (Claude Code) and single-agent tools (every other tool).

[this page](https://buildermethods.com/agent-os/version-2) documents:

- The new features in Agent OS 2.0
- Architectural changes in 2.0
- What changed from 1.x
- Updating guide

[The Agent OS docs](https://buildermethods.com/agent-os) also received a complete overhaul and expansion.  It's now broken out into multiple pages that document every detail of how to install, use and customize Agent OS.

## [1.4.2] - 2025-08-24

### Enforced full three-phase task execution

- Updated `instructions/core/execute-tasks.md` to strictly require all three phases (pre-execution, execution loop, post-execution) and to invoke `instructions/core/post-execution-tasks.md` after task completion.

### Post-execution process overhaul

- Renamed `instructions/core/complete-tasks.md` to `instructions/core/post-execution-tasks.md`.
- Improved the post-execution workflow by adding clarity and removing bloat in instructions.

## [1.4.1] - 2025-08-18

### Replaced Decisions with Recaps

Earlier versions added a decisions.md inside a project's .agent-os/product/.  In practice, this was rarely used and didn't help future development.

It's been replaced with a new system for creating "Recaps"—short summaries of what was built—after every feature spec's implementation has been completed.  Similar to a changelog, but more descriptive and context-focused.  These recaps are easy to reference by both humans and AI agents.

Recaps are automatically generated via the new complete-tasks.md process.

### Added Project-Manager Subagent

A goal of this update was to tighten up the processes for creating specs and executing tasks, ensuring these processes are executed reliably.  Sounds like the job for a "project manager".

This update introduces a new subagent (for Claude Code) called project-manager which handles all task completion, status updates, and reporting progress back to you.

### Spec Creation & Task Execution Reliability Improvements

Several changes to the instructions, processes, and executions, all aimed at helping agents follow the process steps consistently.

- Consolidated task execution instructions with clear step-by-step processes
- Added post-flight verification rules to ensure instruction compliance
- Improved subagent delegation tracking and reporting
- Standardized test suite verification and git workflow integration
- Enhanced task completion criteria validation and status management

## [1.4.0] - 2025-08-17

BIG updates in this one!  Thanks for all the feedback, requests and support 🙏

### All New Installation Process

The way Agent OS gets installed is structured differently from prior versions.  The new system works as follows:

There are 2 installation processes:
- Your "Base installation" (now optional, but still recommended!)
- Your "Project installation"

**"Base installation"**
- Installs all of the Agent OS files to a location of your choosing on your system where they can be customized (especially your standards) and maintained.
- Project installations copy files from your base installation, so they can be customized and self-contained within each individual project.
- Your base installation now has a config.yml

To install the Agent OS base installation,

1. cd to a location of your choice (your system's home folder is a good choice).

2. Run one of these commands:
  - Agent OS with Claude Code support:
  `curl -sSL https://raw.githubusercontent.com/buildermethods/agent-os/main/setup/base.sh | bash -s -- --claude-code`
  - Agent OS with Cursor support:
  `curl -sSL https://raw.githubusercontent.com/buildermethods/agent-os/main/setup/base.sh | bash -s -- --cursor`
  - Agent OS with Claude Code & Cursor support:
  `curl -sSL https://raw.githubusercontent.com/buildermethods/agent-os/main/setup/base.sh | bash -s -- --claude-code --cursor`

3. Customize your /standards (just like earlier versions)

**Project installation**

- Now each project codebase gets it's own self-contained installation of Agent OS.  It no longer references instructions or standards that reside elsewhere on your system.  These all get installed directly into your project's .agent-os folder, which brings several benefits:
  - No external references = more reliable Agent OS commands & workflows.
  - You can commit your instructions, standards, Claude Code commands and agents to your project's github repo for team access.
  - You can customize standards differently per project than what's in your base installation.

Your project installation command will be based on where you installed the Agent OS base installation.
- If you've installed it to your system's home folder, then your project installation command will be `~/.agent-os/setup/project.sh`.
- If you've installed it elsewhere, your command will be `/path/to/agent-os/setup/project.sh`
(after your base installation, it will show you _your_ project installation command. It's a good idea to save it or make an alias if you work on many projects.)

If (for whatever reason) you didn't install the base installation, you can still install Agent OS directly into a project, by pulling it directly off of the public github repo using the following command.
- Note: This means your standards folder won't inherit your defaults from a base installation. You'd need to customize the files in the standards folder for this project.
`curl -sSL https://raw.githubusercontent.com/buildermethods/agent-os/main/setup/project.sh | bash -s -- --no-base --claude-code --cursor`

### Agent OS config.yml

When you install the Agent OS base installation, that now includes a config.yml file.  Currently this file is used for:
- Tracking the Agent OS version you have installed
- Which coding agents (Claude Code, Cursor) you're using
- Project Types (new! read on...)

### Project Types

If you work on different types of projects, you can define different sets of standards, code style, and instructions for each!

- By default, a new installation of Agent OS into a project will copy its instructions and standards from your base installation's /instructions and /standards.
- You can define additional project types by doing the following:
  - Setup a folder (typically inside your base installation's .agent-os folder, but it can be anywhere on your system) which contains /instructions and /standards folders (copy these from your base install, then customize).
  - Define the project type's folder location on your system in your base install's config.yml
- Using project types:
  - If you've named a project type, 'ruby-on-rails', when running your project install command, add the flag --project-type=ruby-on-rails.
  - To make a project type your default for new projects, set it's name as the value for default_project_type in config.yml

### Removed or changed in version 1.4.0:

This update does away with the old installation script files:
- setup.sh (replaced by /setup/base.sh and /setup/project.sh)
- setup-claude-code.sh (now you add --claude-code flag to the install commands or enable it in your Agent OS config.yml)
- setup-cursor.sh (now you add --cursor flag to the install commands or enable it in your Agent OS config.yml)

Claude Code Agent OS commands now should _not_ be installed in the `~/.agent-os/.claude/commands` folder.  Now, these are copied from ~/.agent-os/commands into each project's `~/.claude/commands` folder (this prevents duplicate commands showing in in Claude Code's commands list).  The same approach applies to Claude Code subagents files.

### Upgrading to version 1.4.0

Follow these steps to update a previous version to 1.4.0:

1. If you've customized any files in /instructions, back those up now. They will be overwritten.

2. Navigate to your home directory (or whichever location you want to have your Agent OS base installation)

3. Run the following to command, which includes flags to overwrite your /instructions (remove the --cursor flag if not using Cursor):
`curl -sSL https://raw.githubusercontent.com/buildermethods/agent-os/main/setup/base.sh | bash -s -- --overwrite-instructions --claude-code --cursor`

4. If your ~/.claude/commands contain Agent OS commands, remove those and copy the versions that are now in your base installation's commands folder into your _project's_ `.claude/commands` folder.

5. Navigate to your project. Run your project installation command to install Agent OS instructions and standards into your project's installation. If your Agent OS base installation is in your system's home folder (like previous versions), then your project installation will be: `~/.agent-os/setup/project.sh`

## [1.3.1] - 2025-08-02

### Added
- **Date-Checker Subagent** - New specialized Claude Code subagent for accurate date determination using file system timestamps
  - Uses temporary file creation to extract current date in YYYY-MM-DD format
  - Includes context checking to avoid duplication
  - Provides clear validation and error handling

### Changed
- **Create-Spec Instructions** - Updated `instructions/core/create-spec.md` to use the new date-checker subagent
  - Replaced complex inline date determination logic with simple subagent delegation
  - Simplified step 4 (date_determination) by removing 45 lines of validation and fallback code
  - Cleaner instruction flow with specialized agent handling date logic

### Improved
- **Code Maintainability** - Date determination logic centralized in reusable subagent
- **Instruction Clarity** - Simplified create-spec workflow with cleaner delegation pattern
- **Error Handling** - More robust date determination with dedicated validation rules

## [1.3.0] - 2025-08-01

### Added
- **Pre-flight Check System** - New `meta/pre-flight.md` instruction for centralized agent detection and initialization
- **Proactive Agent Usage** - Updated agent descriptions to encourage proactive use when appropriate
- **Structured Instruction Organization** - New folder structure with `core/` and `meta/` subdirectories

### Changed
- **Instruction File Structure** - Reorganized all instruction files into subdirectories:
  - Core instructions moved to `instructions/core/` (plan-product, create-spec, execute-tasks, execute-task, analyze-product)
  - Meta instructions in `instructions/meta/` (pre-flight, more to come)
- **Simplified XML Metadata** - Removed verbose `<ai_meta>` and `<step_metadata>` blocks for cleaner, more readable instructions
- **Subagent Integration** - Replaced manual agent detection with centralized pre-flight check across all instruction files to enforce delegation and preserve main agent's context.
- **Step Definitions** - Added `subagent` attribute to steps for clearer delegation of work to help enforce delegation and preserve main agent's context.
- **Setup Script** - Updated to create subdirectories and download files to new locations

### Improved
- **Code Clarity** - Removed redundant XML instructions in favor of descriptive step purposes
- **Agent Efficiency** - Centralized agent detection reduces repeated checks throughout workflows
- **Maintainability** - Cleaner instruction format with less XML boilerplate
- **User Experience** - Clearer indication of when specialized agents will be used proactively

### Removed
- **CLAUDE.md** - Removed deprecated Claude Code configuration file (functionality moved to pre-flight system, preventing over-reading instructions into context)
- **Redundant Instructions** - Eliminated verbose ACTION/MODIFY/VERIFY instruction blocks

## [1.2.0] - 2025-07-29

### Added
- **Claude Code Specialized Subagents** - New agents to offload specific tasks for improved efficiency:
  - `test-runner.md` - Handles test execution and failure analysis with minimal toolset
  - `context-fetcher.md` - Retrieves information from files while checking context to avoid duplication
  - `git-workflow.md` - Manages git operations, branches, commits, and PR creation
  - `file-creator.md` - Creates files, directories, and applies consistent templates
- **Agent Detection Pattern** - Single check at process start with boolean flags for efficiency
- **Subagent Integration** across all instruction files with automatic fallback for non-Claude Code users

### Changed
- **Instruction Files** - All updated to support conditional agent usage:
  - `execute-tasks.md` - Uses git-workflow (branch management, PR creation), test-runner (full suite), and context-fetcher (loading lite files)
  - `execute-task.md` - Uses context-fetcher (best practices, code style) and test-runner (task-specific tests)
  - `plan-product.md` - Uses file-creator (directory creation) and context-fetcher (tech stack defaults)
  - `create-spec.md` - Uses file-creator (spec folder) and context-fetcher (mission/roadmap checks)
- **Standards Files** - Updated for conditional agent usage:
  - `code-style.md` - Uses context-fetcher for loading language-specific style guides
- **Setup Scripts** - Enhanced to install Claude Code agents:
  - `setup-claude-code.sh` - Downloads all agents to `~/.claude/agents/` directory

### Improved
- **Context Efficiency** - Specialized agents use minimal context for their specific tasks
- **Code Organization** - Complex operations delegated to focused agents with clear responsibilities
- **Error Handling** - Agents provide targeted error analysis and recovery strategies
- **Maintainability** - Cleaner main agent code with operations abstracted to subagents
- **Performance** - Reduced context checks through one-time agent detection pattern

### Technical Details
- Each agent uses only necessary tools (e.g., test-runner uses only Bash, Read, Grep, Glob)
- Automatic fallback ensures compatibility for users without Claude Code
- Consistent `IF has_[agent_name]:` pattern reduces code complexity
- All agents follow Agent OS conventions (branch naming, commit messages, file templates)

## [1.1.0] - 2025-07-29

### Added
- New `mission-lite.md` file generation in product initialization for efficient AI context usage
- New `spec-lite.md` file generation in spec creation for condensed spec summaries
- New `execute-task.md` instruction file for individual task execution with TDD workflow
- Task execution loop in `execute-tasks.md` that calls `execute-task.md` for each parent task
- Language-specific code style guides:
  - `standards/code-style/css-style.md` for CSS and TailwindCSS
  - `standards/code-style/html-style.md` for HTML markup
  - `standards/code-style/javascript-style.md` for JavaScript
- Conditional loading blocks in `best-practices.md` and `code-style.md` to prevent duplicate context loading
- Context-aware file loading throughout all instruction files

### Changed
- Optimized `plan-product.md` to generate condensed versions of documents
- Enhanced `create-spec.md` with conditional context loading for mission-lite and tech-stack files
- Simplified technical specification structure by removing multiple approach options
- Made external dependencies section conditional in technical specifications
- Updated `execute-tasks.md` to use minimal context loading strategy
- Improved `execute-task.md` with selective reading of relevant documentation sections
- Modified roadmap progress check to be conditional and context-aware
- Updated decision documentation to avoid loading decisions.md and use conditional checks
- Restructured task execution to follow typical TDD pattern (tests first, implementation, verification)

### Improved
- Context efficiency by 60-80% through conditional loading and lite file versions
- Reduced duplication when files are referenced multiple times in a workflow
- Clearer separation between task-specific and full test suite execution
- More intelligent file loading that checks current context before reading
- Better organization of code style rules with language-specific files

### Fixed
- Duplicate content loading when instruction files are called in loops
- Unnecessary loading of full documentation files when condensed versions suffice
- Redundant test suite runs between individual task execution and overall workflow

## [1.0.0] - 2025-07-21

### Added
- Initial release of Agent OS framework
- Core instruction files:
  - `plan-product.md` for product initialization
  - `create-spec.md` for feature specification
  - `execute-tasks.md` for task execution
  - `analyze-product.md` for existing codebase analysis
- Standard files:
  - `tech-stack.md` for technology choices
  - `code-style.md` for formatting rules
  - `best-practices.md` for development guidelines
- Product documentation structure:
  - `mission.md` for product vision
  - `roadmap.md` for development phases
  - `decisions.md` for decision logging
  - `tech-stack.md` for technical architecture
- Setup scripts for easy installation
- Integration with AI coding assistants (Claude Code, Cursor)
- Task management with TDD workflow
- Spec creation and organization system

[1.4.1]: https://github.com/buildermethods/agent-os/compare/v1.4.0...v1.4.1
[1.4.2]: https://github.com/buildermethods/agent-os/compare/v1.4.1...v1.4.2
[1.4.0]: https://github.com/buildermethods/agent-os/compare/v1.3.1...v1.4.0
[1.3.1]: https://github.com/buildermethods/agent-os/compare/v1.3.0...v1.3.1
[1.3.0]: https://github.com/buildermethods/agent-os/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/buildermethods/agent-os/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/buildermethods/agent-os/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/buildermethods/agent-os/releases/tag/v1.0.0
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2025 CasJam Media LLC (Builder Methods)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `README.md`
```markdown
<img width="1200" height="675" alt="Agent OS" src="https://github.com/user-attachments/assets/97ad4491-d199-4b9b-9482-ae710291dfb4" />

## Agents that build the way you would

[Agent OS](https://buildermethods.com/agent-os) helps you shape better specs, keeps agents aligned in a lightweight system that fits how you already build.

Works alongside Claude Code, Cursor, Antigravity, and other AI tools. Any language, any framework.

**Core capabilities:**

- **Discover Standards** — Extract patterns and conventions from your codebase into documented standards
- **Deploy Standards** — Intelligently inject relevant standards based on what you're building
- **Shape Spec** — Create better plans that lead to better builds
- **Index Standards** — Keep your standards organized and discoverable

---

### Documentation & Installation

Docs, installation, usage, & best practices 👉 [It's all here](https://buildermethods.com/agent-os)

---

### Follow updates & releases

Read the [changelog](CHANGELOG.md)

[Subscribe to be notified of major new releases of Agent OS](https://buildermethods.com/agent-os)

---

### Created by Brian Casel @ Builder Methods

Created by Brian Casel, the creator of [Builder Methods](https://buildermethods.com), where Brian helps professional software developers and teams build with AI.

Get Brian's free resources on building with AI:
- [Builder Briefing newsletter](https://buildermethods.com)
- [YouTube](https://youtube.com/@briancasel)

Join [Builder Methods Pro](https://buildermethods.com/pro) for official support and connect with our community of AI-first builders:

```

## File: `config.yml`
```yaml
version: 3.0
default_profile: default

# Optional: define inheritance relationships for profiles
# Profiles not listed here still work, they just have no inheritance
# profiles:
#   profile-a:
#     inherits_from: default
#   profile-b:
#     inherits_from: profile-a
```

## File: `commands/agent-os/discover-standards.md`
```markdown
# Discover Standards

Extract tribal knowledge from your codebase into concise, documented standards.

## Important Guidelines

- **Always use AskUserQuestion tool** when asking the user anything
- **Write concise standards** — Use minimal words. Standards must be scannable by AI agents without bloating context windows.
- **Offer suggestions** — Present options the user can confirm, choose between, or correct. Don't make them think harder than necessary.

## Process

### Step 1: Determine Focus Area

Check if the user specified an area when running this command. If they did, skip to Step 2.

If no area was specified:

1. Analyze the codebase structure (folders, file types, patterns)
2. Identify 3-5 major areas. Examples:
   - **Frontend areas:** UI components, styling/CSS, state management, forms, routing
   - **Backend areas:** API routes, database/models, authentication, background jobs
   - **Cross-cutting:** Error handling, validation, testing, naming conventions, file structure
3. Use AskUserQuestion to present the areas:

```
I've identified these areas in your codebase:

1. **API Routes** (src/api/) — Request handling, response formats
2. **Database** (src/models/, src/db/) — Models, queries, migrations
3. **React Components** (src/components/) — UI patterns, props, state
4. **Authentication** (src/auth/) — Login, sessions, permissions

Which area should we focus on for discovering standards? (Pick one, or suggest a different area)
```

Wait for user response before proceeding.

### Step 2: Analyze & Present Findings

Once an area is determined:

1. Read key files in that area (5-10 representative files)
2. Look for patterns that are:
   - **Unusual or unconventional** — Not standard framework/library patterns
   - **Opinionated** — Specific choices that could have gone differently
   - **Tribal** — Things a new developer wouldn't know without being told
   - **Consistent** — Patterns repeated across multiple files

3. Use AskUserQuestion to present findings and let user select:

```
I analyzed [area] and found these potential standards worth documenting:

1. **API Response Envelope** — All responses use { success, data, error } structure
2. **Error Codes** — Custom error codes like AUTH_001, DB_002 with specific meanings
3. **Pagination Pattern** — Cursor-based pagination with consistent param names

Which would you like to document?

Options:
- "Yes, all of them"
- "Just 1 and 3"
- "Add: [your suggestion]"
- "Skip this area"
```

Wait for user selection before proceeding.

### Step 3: Ask Why, Then Draft Each Standard

**IMPORTANT:** For each selected standard, you MUST complete this full loop before moving to the next standard:

1. **Ask 1-2 clarifying questions** about the "why" behind the pattern. Use your AskUserQuestion tool for this.
2. **Wait for user response**
3. **Draft the standard** incorporating their answer
4. **Confirm with user** before creating the file
5. **Create the file** if approved

Example questions to ask (adapt based on the specific standard):

- "What problem does this pattern solve? Why not use the default/common approach?"
- "Are there exceptions where this pattern shouldn't be used?"
- "What's the most common mistake a developer or agent makes with this?"

**Do NOT batch all questions upfront.** Process one standard at a time through the full loop.

### Step 4: Create the Standard File

For each standard (after completing Step 3's Q&A):

1. Determine the appropriate folder (create if needed):
   - `api/`, `database/`, `javascript/`, `css/`, `backend/`, `testing/`, `global/`

2. Check if a related standard file already exists — append to it if so

3. Draft the content and use AskUserQuestion to confirm:

```
Here's the draft for api/response-format.md:

---
# API Response Format

All API responses use this envelope:

\`\`\`json
{ "success": true, "data": { ... } }
{ "success": false, "error": { "code": "...", "message": "..." } }
\`\`\`

- Never return raw data without the envelope
- Error responses must include both code and message
- Success responses omit the error field entirely
---

Create this file? (yes / edit: [your changes] / skip)
```

4. Create or update the file in `agent-os/standards/[folder]/`
5. **Then repeat Steps 3-4 for the next selected standard**

### Step 5: Update the Index

After all standards are created:

1. Scan `agent-os/standards/` for all `.md` files
2. For each new file without an index entry, use AskUserQuestion:

```
New standard needs an index entry:
  File: api/response-format.md

Suggested description: "API response envelope structure and error format"

Accept this description? (yes / or type a better one)
```

3. Update `agent-os/standards/index.yml`:

```yaml
api:
  response-format:
    description: API response envelope structure and error format
```

Alphabetize by folder, then by filename.

### Step 6: Offer to Continue

Use AskUserQuestion:

```
Standards created for [area]:
- api/response-format.md
- api/error-codes.md

Would you like to discover standards in another area, or are we done?
```

## Output Location

All standards: `agent-os/standards/[folder]/[standard].md`
Index file: `agent-os/standards/index.yml`

## Writing Concise Standards

Standards will be injected into AI context windows. Every word costs tokens. Follow these rules:

- **Lead with the rule** — State what to do first, explain why second (if needed)
- **Use code examples** — Show, don't tell
- **Skip the obvious** — Don't document what the code already makes clear
- **One standard per concept** — Don't combine unrelated patterns
- **Bullet points over paragraphs** — Scannable beats readable

**Good:**
```markdown
# Error Responses

Use error codes: `AUTH_001`, `DB_001`, `VAL_001`

\`\`\`json
{ "success": false, "error": { "code": "AUTH_001", "message": "..." } }
\`\`\`

- Always include both code and message
- Log full error server-side, return safe message to client
```

**Bad:**
```markdown
# Error Handling Guidelines

When an error occurs in our application, we have established a consistent pattern for how errors should be formatted and returned to the client. This helps maintain consistency across our API and makes it easier for frontend developers to handle errors appropriately...
[continues for 3 more paragraphs]
```

## Example: Full Loop for One Standard

Here's how to process a single standard through the complete workflow:

**1. Present findings (Step 2):**
```
I found these patterns in your API code:
1. **Response Envelope** — All responses use { success, data, error }
2. **Error Codes** — Custom codes like AUTH_001

Which would you like to document?
```

User: "Both"

**2. Ask why for first standard (Step 3):**
```
For the Response Envelope pattern:
- What problem does this solve? Why not return raw data?
- Are there any endpoints that don't use this pattern?
```

User: "We use it so the frontend always knows where to find the data. All endpoints use it, no exceptions."

**3. Draft first standard (Step 3 continued):**
```
Here's the draft for api/response-envelope.md:

---
# Response Envelope

All API responses use this structure:
\`\`\`json
{ "success": true, "data": { ... } }
{ "success": false, "error": { ... } }
\`\`\`

- Frontend always checks `success` first, then reads `data` or `error`
- No exceptions — every endpoint uses this format
---

Create this file?
```

User: "Yes"

**4. Create file, then move to next standard:**

[Create the file]

**5. Ask why for second standard (back to Step 3):**
```
For the Error Codes pattern:
- What's the naming convention for codes?
- Where should new error codes be documented?
```

User: "Format is AREA_NUMBER like AUTH_001. We keep a list in the wiki."

**6. Draft second standard, confirm, create file...**

[Continue until all selected standards are done]

**Key point:** Complete the full ask → draft → confirm → create cycle for each standard before starting the next one.
```

## File: `commands/agent-os/index-standards.md`
```markdown
# Index Standards

Rebuild and maintain the standards index file (`index.yml`).

## Purpose

The index enables `/inject-standards` to suggest relevant standards without reading all files. It maps each standard to a brief description for quick matching.

## Process

### Step 1: Scan for Standards Files

1. List all `.md` files in `agent-os/standards/` and its subfolders
2. Build a list of all standards organized by folder:
   ```
   root/coding-style.md        # Files in standards/ root use "root" as the folder name
   root/naming.md
   api/response-format.md
   api/error-handling.md
   database/migrations.md
   ```

**Note:** `root` is a reserved keyword — it refers to `.md` files directly in `agent-os/standards/` (not in a subfolder). Do not create an actual folder named "root".

### Step 2: Load Existing Index

Read `agent-os/standards/index.yml` if it exists. Note which entries already have descriptions.

### Step 3: Identify Changes

Compare the file scan with the existing index:

- **New files** — Standards files without index entries
- **Deleted files** — Index entries for files that no longer exist
- **Existing files** — Already indexed, keep as-is

### Step 4: Handle New Files

For each new standard file that needs an index entry:

1. Read the file to understand its content
2. Use AskUserQuestion to propose a description:

```
New standard needs indexing:
  File: api/response-format.md

Suggested description: "API response envelope structure and error format"

Accept? (yes / or type a better description)
```

Keep descriptions to **one short sentence** — they're for matching, not documentation.

### Step 5: Handle Deleted Files

If there are index entries for files that no longer exist:

1. List them for the user
2. Remove them from the index automatically (no confirmation needed)

Report: "Removed 2 stale index entries: api/old-pattern.md, testing/deprecated.md"

### Step 6: Write Updated Index

Generate `agent-os/standards/index.yml` with this structure:

```yaml
folder-name:
  file-name:
    description: Brief description here
```

**Rules:**
- Alphabetize folders
- Alphabetize files within each folder
- File names without `.md` extension
- One-line descriptions only

**Example:**
```yaml
root:
  coding-style:
    description: General coding style, formatting, linting rules
  naming:
    description: File naming, variable naming, class naming conventions

api:
  error-handling:
    description: Error codes, exception handling, error response format
  response-format:
    description: API response envelope structure, status codes, pagination

database:
  migrations:
    description: Migration file structure, naming conventions, rollback patterns
```

**Note:** `root` appears first and contains standards files that live directly in `agent-os/standards/` (not in subfolders).

### Step 7: Report Results

Summarize what changed:

```
Index updated:
  ✓ 2 new entries added
  ✓ 1 stale entry removed
  ✓ 8 entries unchanged

Total: 9 standards indexed
```

## When to Run

- After manually creating or deleting standards files
- If `/inject-standards` suggestions seem out of sync
- To clean up a messy or outdated index

**Note:** `/discover-standards` runs this automatically as its final step, so you usually don't need to call it separately after discovering standards.

## Output

Updates `agent-os/standards/index.yml`
```

## File: `commands/agent-os/inject-standards.md`
```markdown
# Inject Standards

Inject relevant standards into the current context, formatted appropriately for the situation.

## Usage Modes

This command supports two modes:

### Auto-Suggest Mode (no arguments)
```
/inject-standards
```
Analyzes context and suggests relevant standards.

### Explicit Mode (with arguments)
```
/inject-standards api                           # All standards in api/
/inject-standards api/response-format           # Single file
/inject-standards api/response-format api/auth  # Multiple files
/inject-standards root                          # All standards in the root folder
/inject-standards root/naming                   # Single file from root folder
```
Directly injects specified standards without suggestions.

**Note:** `root` is a reserved keyword — it refers to `.md` files directly in `agent-os/standards/` (not in a subfolder).

## Process

### Step 1: Detect Context Scenario

Before injecting standards, determine which scenario we're in. Read the current conversation and check if we're in plan mode.

**Three scenarios:**

1. **Conversation** — Regular chat, implementing code, answering questions
2. **Creating a Skill** — Building a `.claude/skills/` file
3. **Shaping/Planning** — In plan mode, building a spec, running `/shape-spec`

**Detection logic:**

- If currently in plan mode OR conversation clearly mentions "spec", "plan", "shape" → **Shaping/Planning**
- If conversation clearly mentions creating a skill, editing `.claude/skills/`, or building a reusable procedure → **Creating a Skill**
- Otherwise → **Ask to confirm** (do not assume)

**If neither skill nor plan is clearly detected**, use AskUserQuestion to confirm:

```
I'll inject the relevant standards. How should I format them?

1. **Conversation** — Read standards into our chat (for implementation work)
2. **Skill** — Output file references to include in a skill you're building
3. **Plan** — Output file references to include in a plan/spec

Which scenario? (1, 2, or 3)
```

Always ask when uncertain — don't assume conversation by default.

### Step 2: Read the Index (Auto-Suggest Mode)

Read `agent-os/standards/index.yml` to get the list of available standards and their descriptions.

If index.yml doesn't exist or is empty:
```
No standards index found. Run /discover-standards first to create standards,
or /index-standards if you have standards files without an index.
```

### Step 3: Analyze Work Context

Look at the current conversation to understand what the user is working on:
- What type of work? (API, database, UI, etc.)
- What technologies mentioned?
- What's the goal?

### Step 4: Match and Suggest

Match index descriptions against the context. Use AskUserQuestion to present suggestions:

```
Based on your task, these standards may be relevant:

1. **api/response-format** — API response envelope structure, status codes
2. **api/error-handling** — Error codes, exception handling, error responses
3. **global/naming** — File naming, variable naming conventions

Inject these standards? (yes / just 1 and 3 / add: database/migrations / none)
```

Keep suggestions focused — typically 2-5 standards. Don't overwhelm with too many options.

### Step 5: Inject Based on Scenario

Format the output differently based on the detected scenario:

---

#### Scenario: Conversation

Read the standards and announce them:

```
I've read the following standards as they are relevant to what we're working on:

--- Standard: api/response-format ---

[full content of the standard file]

--- End Standard ---

--- Standard: api/error-handling ---

[full content of the standard file]

--- End Standard ---

**Key points:**
- All API responses use { success, data, error } envelope
- Error codes follow AUTH_xxx, DB_xxx pattern
```

---

#### Scenario: Creating a Skill

First, use AskUserQuestion to determine how to include the standards:

```
How should these standards be included in your skill?

1. **References** — Add @ file paths that point to the standards (keeps skill lightweight, standards stay in sync)
2. **Copy content** — Paste the full standards content into the skill (self-contained, but won't update if standards change)

Which approach? (1 or 2)
```

**If References (option 1):**

```
Be sure to include references to the following standards files in the appropriate location in the file(s) that make up this skill:

@agent-os/standards/api/response-format.md
@agent-os/standards/api/error-handling.md
@agent-os/standards/global/naming.md

These standards cover:
- API response envelope structure, status codes
- Error codes, exception handling, error responses
- File naming, variable naming conventions
```

**If Copy content (option 2):**

```
Include the following standards content in your skill:

--- Standard: api/response-format ---

[full content of the standard file]

--- End Standard ---

--- Standard: api/error-handling ---

[full content of the standard file]

--- End Standard ---

These standards cover:
- API response envelope structure, status codes
- Error codes, exception handling, error responses
- File naming, variable naming conventions
```

---

#### Scenario: Shaping/Planning

First, use AskUserQuestion to determine how to include the standards:

```
How should these standards be included in your plan?

1. **References** — Add @ file paths that point to the standards (keeps plan lightweight, standards stay in sync)
2. **Copy content** — Paste the full standards content into the plan (self-contained, but won't update if standards change)

Which approach? (1 or 2)
```

**If References (option 1):**

```
Be sure to include references to the following standards files in the appropriate location in the plan we're building:

@agent-os/standards/api/response-format.md
@agent-os/standards/api/error-handling.md
@agent-os/standards/global/naming.md

These standards cover:
- API response envelope structure, status codes
- Error codes, exception handling, error responses
- File naming, variable naming conventions
```

**If Copy content (option 2):**

```
Include the following standards content in your plan:

--- Standard: api/response-format ---

[full content of the standard file]

--- End Standard ---

--- Standard: api/error-handling ---

[full content of the standard file]

--- End Standard ---

These standards cover:
- API response envelope structure, status codes
- Error codes, exception handling, error responses
- File naming, variable naming conventions
```

---

### Step 6: Surface Related Skills (Conversation scenario only)

When in conversation scenario, check if `.claude/skills/` exists and contains related skills:

```
Related Skills you might want to use:
- create-api-endpoint — Scaffolds new API endpoints following these standards
```

Don't invoke skills automatically — just surface them for awareness.

---

## Explicit Mode

When arguments are provided, skip the suggestion step but still detect scenario.

### Step 1: Detect Scenario

Same as auto-suggest mode.

### Step 2: Parse Arguments

Arguments can be:
- **Folder name** — `api` → inject all `.md` files in `agent-os/standards/api/`
- **Folder/file** — `api/response-format` → inject `agent-os/standards/api/response-format.md`
- **Root folder** — `root` → inject all `.md` files directly in `agent-os/standards/` (not in subfolders)
- **Root file** — `root/naming` → inject `agent-os/standards/naming.md`

Multiple arguments inject multiple standards.

### Step 3: Validate

Check that specified files/folders exist. If not:

```
Standard not found: api/nonexistent

Available standards in api/:
- response-format
- error-handling
- authentication

Did you mean one of these?
```

### Step 4: Inject Based on Scenario

Same formatting as auto-suggest mode, based on detected scenario.

---

## Tips

- **Run early** — Inject standards at the start of a task, before implementation
- **Be specific** — If you know which standards apply, use explicit mode
- **Check the index** — If suggestions seem wrong, run `/index-standards` to rebuild
- **Keep standards concise** — Injected standards consume tokens; shorter is better

## Integration

This command is called internally by `/shape-spec` to inject relevant standards during planning. You can also invoke it directly anytime you need standards in context.
```

## File: `commands/agent-os/plan-product.md`
```markdown
# Plan Product

Establish foundational product documentation through an interactive conversation. Creates mission, roadmap, and tech stack files in `agent-os/product/`.

## Important Guidelines

- **Always use AskUserQuestion tool** when asking the user anything
- **Keep it lightweight** — gather enough to create useful docs without over-documenting
- **One question at a time** — don't overwhelm with multiple questions

## Process

### Step 1: Check for Existing Product Docs

Check if `agent-os/product/` exists and contains any of these files:
- `mission.md`
- `roadmap.md`
- `tech-stack.md`

**If any files exist**, use AskUserQuestion:

```
I found existing product documentation:
- mission.md: [exists/missing]
- roadmap.md: [exists/missing]
- tech-stack.md: [exists/missing]

Would you like to:
1. Start fresh (replace all)
2. Update specific files
3. Cancel

(Choose 1, 2, or 3)
```

If option 2, ask which files to update and only gather info for those.
If option 3, stop here.

**If no files exist**, proceed to Step 2.

### Step 2: Gather Product Vision (for mission.md)

Use AskUserQuestion:

```
Let's define your product's mission.

**What problem does this product solve?**

(Describe the core problem or pain point you're addressing)
```

After they respond, use AskUserQuestion:

```
**Who is this product for?**

(Describe your target users or audience)
```

After they respond, use AskUserQuestion:

```
**What makes your solution unique?**

(What's the key differentiator or approach?)
```

### Step 3: Gather Roadmap (for roadmap.md)

Use AskUserQuestion:

```
Now let's outline your development roadmap.

**What are the must-have features for launch (MVP)?**

(List the core features needed for the first usable version)
```

After they respond, use AskUserQuestion:

```
**What features are planned for after launch?**

(List features you'd like to add in future phases, or say "none yet")
```

### Step 4: Establish Tech Stack (for tech-stack.md)

First, check if `agent-os/standards/global/tech-stack.md` exists.

**If the tech-stack standard exists**, read it and use AskUserQuestion:

```
I found a tech stack standard in your standards:

[Summarize the key technologies from global/tech-stack.md]

Does this project use the same tech stack, or does it differ?

1. Same as standard (use as-is)
2. Different (I'll specify)

(Choose 1 or 2)
```

If they choose option 1, use the standard's content for tech-stack.md.
If they choose option 2, proceed to ask them to specify (see below).

**If no tech-stack standard exists** (or they chose option 2 above), use AskUserQuestion:

```
**What technologies does this project use?**

Please describe your tech stack:
- Frontend: (e.g., React, Vue, vanilla JS, or N/A)
- Backend: (e.g., Rails, Node, Django, or N/A)
- Database: (e.g., PostgreSQL, MongoDB, or N/A)
- Other: (hosting, APIs, tools, etc.)
```

### Step 5: Generate Files

Create the `agent-os/product/` directory if it doesn't exist.

Generate each file based on the information gathered:

#### mission.md

```markdown
# Product Mission

## Problem

[Insert what problem this product solves - from Step 2]

## Target Users

[Insert who this product is for - from Step 2]

## Solution

[Insert what makes the solution unique - from Step 2]
```

#### roadmap.md

```markdown
# Product Roadmap

## Phase 1: MVP

[Insert must-have features for launch - from Step 3]

## Phase 2: Post-Launch

[Insert planned future features - from Step 3, or "To be determined" if they said none yet]
```

#### tech-stack.md

```markdown
# Tech Stack

[Organize the tech stack information into logical sections]

## Frontend

[Frontend technologies, or "N/A" if not applicable]

## Backend

[Backend technologies, or "N/A" if not applicable]

## Database

[Database choice, or "N/A" if not applicable]

## Other

[Other tools, hosting, services - or omit this section if nothing mentioned]
```

### Step 6: Confirm Completion

After creating all files, output to user:

```
✓ Product documentation created:

  agent-os/product/mission.md
  agent-os/product/roadmap.md
  agent-os/product/tech-stack.md

Review these files to ensure they accurately capture your product vision.
You can edit them directly or run /plan-product again to update.
```

## Tips

- If the user provides very brief answers, that's fine — the docs can be expanded later
- If they want to skip a section, create the file with a placeholder like "To be defined"
- The `/shape-spec` command will read these files when planning features, so having them populated helps with context
```

## File: `commands/agent-os/shape-spec.md`
```markdown
# Shape Spec

Gather context and structure planning for significant work. **Run this command while in plan mode.**

## Important Guidelines

- **Always use AskUserQuestion tool** when asking the user anything
- **Offer suggestions** — Present options the user can confirm, adjust, or correct
- **Keep it lightweight** — This is shaping, not exhaustive documentation

## Prerequisites

This command **must be run in plan mode**.

**Before proceeding, check if you are currently in plan mode.**

If NOT in plan mode, **stop immediately** and tell the user:

```
Shape-spec must be run in plan mode. Please enter plan mode first, then run /shape-spec again.
```

Do not proceed with any steps below until confirmed to be in plan mode.

## Process

### Step 1: Clarify What We're Building

Use AskUserQuestion to understand the scope:

```
What are we building? Please describe the feature or change.

(Be as specific as you like — I'll ask follow-up questions if needed)
```

Based on their response, ask 1-2 clarifying questions if the scope is unclear. Examples:
- "Is this a new feature or a change to existing functionality?"
- "What's the expected outcome when this is done?"
- "Are there any constraints or requirements I should know about?"

### Step 2: Gather Visuals

Use AskUserQuestion:

```
Do you have any visuals to reference?

- Mockups or wireframes
- Screenshots of similar features
- Examples from other apps

(Paste images, share file paths, or say "none")
```

If visuals are provided, note them for inclusion in the spec folder.

### Step 3: Identify Reference Implementations

Use AskUserQuestion:

```
Is there similar code in this codebase I should reference?

Examples:
- "The comments feature is similar to what we're building"
- "Look at how src/features/notifications/ handles real-time updates"
- "No existing references"

(Point me to files, folders, or features to study)
```

If references are provided, read and analyze them to inform the plan.

### Step 4: Check Product Context

Check if `agent-os/product/` exists and contains files.

If it exists, read key files (like `mission.md`, `roadmap.md`, `tech-stack.md`) and use AskUserQuestion:

```
I found product context in agent-os/product/. Should this feature align with any specific product goals or constraints?

Key points from your product docs:
- [summarize relevant points]

(Confirm alignment or note any adjustments)
```

If no product folder exists, skip this step.

### Step 5: Surface Relevant Standards

Read `agent-os/standards/index.yml` to identify relevant standards based on the feature being built.

Use AskUserQuestion to confirm:

```
Based on what we're building, these standards may apply:

1. **api/response-format** — API response envelope structure
2. **api/error-handling** — Error codes and exception handling
3. **database/migrations** — Migration patterns

Should I include these in the spec? (yes / adjust: remove 3, add frontend/forms)
```

Read the confirmed standards files to include their content in the plan context.

### Step 6: Generate Spec Folder Name

Create a folder name using this format:
```
YYYY-MM-DD-HHMM-{feature-slug}/
```

Where:
- Date/time is current timestamp
- Feature slug is derived from the feature description (lowercase, hyphens, max 40 chars)

Example: `2026-01-15-1430-user-comment-core/`

**Note:** If `agent-os/specs/` doesn't exist, create it when saving the spec folder.

### Step 7: Structure the Plan

Now build the plan with **Task 1 always being "Save spec documentation"**.

Present this structure to the user:

```
Here's the plan structure. Task 1 saves all our shaping work before implementation begins.

---

## Task 1: Save Spec Documentation

Create `agent-os/specs/{folder-name}/` with:

- **plan.md** — This full plan
- **shape.md** — Shaping notes (scope, decisions, context from our conversation)
- **standards.md** — Relevant standards that apply to this work
- **references.md** — Pointers to reference implementations studied
- **visuals/** — Any mockups or screenshots provided

## Task 2: [First implementation task]

[Description based on the feature]

## Task 3: [Next task]

...

---

Does this plan structure look right? I'll fill in the implementation tasks next.
```

### Step 8: Complete the Plan

After Task 1 is confirmed, continue building out the remaining implementation tasks based on:
- The feature scope from Step 1
- Patterns from reference implementations (Step 3)
- Constraints from standards (Step 5)

Each task should be specific and actionable.

### Step 9: Ready for Execution

When the full plan is ready:

```
Plan complete. When you approve and execute:

1. Task 1 will save all spec documentation first
2. Then implementation tasks will proceed

Ready to start? (approve / adjust)
```

## Output Structure

The spec folder will contain:

```
agent-os/specs/{YYYY-MM-DD-HHMM-feature-slug}/
├── plan.md           # The full plan
├── shape.md          # Shaping decisions and context
├── standards.md      # Which standards apply and key points
├── references.md     # Pointers to similar code
└── visuals/          # Mockups, screenshots (if any)
```

## shape.md Content

The shape.md file should capture:

```markdown
# {Feature Name} — Shaping Notes

## Scope

[What we're building, from Step 1]

## Decisions

- [Key decisions made during shaping]
- [Constraints or requirements noted]

## Context

- **Visuals:** [List of visuals provided, or "None"]
- **References:** [Code references studied]
- **Product alignment:** [Notes from product context, or "N/A"]

## Standards Applied

- api/response-format — [why it applies]
- api/error-handling — [why it applies]
```

## standards.md Content

Include the full content of each relevant standard:

```markdown
# Standards for {Feature Name}

The following standards apply to this work.

---

## api/response-format

[Full content of the standard file]

---

## api/error-handling

[Full content of the standard file]
```

## references.md Content

```markdown
# References for {Feature Name}

## Similar Implementations

### {Reference 1 name}

- **Location:** `src/features/comments/`
- **Relevance:** [Why this is relevant]
- **Key patterns:** [What to borrow from this]

### {Reference 2 name}

...
```

## Tips

- **Keep shaping fast** — Don't over-document. Capture enough to start, refine as you build.
- **Visuals are optional** — Not every feature needs mockups.
- **Standards guide, not dictate** — They inform the plan but aren't always mandatory.
- **Specs are discoverable** — Months later, someone can find this spec and understand what was built and why.
```

## File: `profiles/default/global/tech-stack.md`
```markdown
# Tech Stack

## Frontend

- React 18 with TypeScript
- Tailwind CSS v4 for styling
- Vite for build tooling

## Backend

- Node.js with Express
- TypeScript

## Database

- PostgreSQL

## Other
```

## File: `scripts/common-functions.sh`
```bash
#!/bin/bash

# =============================================================================
# Agent OS Common Functions
# Shared utilities for Agent OS scripts
# =============================================================================

# Colors for output
RED='\033[38;2;255;32;86m'
GREEN='\033[38;2;0;234;179m'
YELLOW='\033[38;2;255;185;0m'
BLUE='\033[38;2;0;208;255m'
PURPLE='\033[38;2;142;81;255m'
NC='\033[0m' # No Color

# -----------------------------------------------------------------------------
# Output Functions
# -----------------------------------------------------------------------------

# Print colored output
print_color() {
    local color=$1
    shift
    echo -e "${color}$@${NC}"
}

# Print section header
print_section() {
    echo ""
    print_color "$BLUE" "=== $1 ==="
    echo ""
}

# Print status message
print_status() {
    print_color "$BLUE" "$1"
}

# Print success message
print_success() {
    print_color "$GREEN" "✓ $1"
}

# Print warning message
print_warning() {
    print_color "$YELLOW" "⚠️  $1"
}

# Print error message
print_error() {
    print_color "$RED" "✗ $1"
}

# Print verbose message (only in verbose mode)
print_verbose() {
    if [[ "$VERBOSE" == "true" ]]; then
        echo "[VERBOSE] $1" >&2
    fi
}

# -----------------------------------------------------------------------------
# YAML Parsing (Simple)
# -----------------------------------------------------------------------------

# Get a simple value from YAML (key: value format)
get_yaml_value() {
    local file=$1
    local key=$2
    local default=$3

    if [[ ! -f "$file" ]]; then
        echo "$default"
        return
    fi

    local value=$(grep "^${key}:" "$file" | sed "s/^${key}:[[:space:]]*//" | sed 's/[[:space:]]*$//')

    if [[ -n "$value" ]]; then
        echo "$value"
    else
        echo "$default"
    fi
}

# Get inherits_from value for a profile from config.yml
# Returns empty string if profile has no inheritance defined
get_profile_inherits_from() {
    local config_file=$1
    local profile_name=$2

    if [[ ! -f "$config_file" ]]; then
        echo ""
        return
    fi

    # Use awk to find the inherits_from value for the given profile
    # Format:
    # profiles:
    #   profile-name:
    #     inherits_from: parent-profile
    local value=$(awk -v profile="$profile_name" '
        /^profiles:/ { in_profiles=1; next }
        /^[a-zA-Z]/ && !/^[[:space:]]/ { in_profiles=0 }
        in_profiles && $0 ~ "^  "profile":$" { in_target=1; next }
        in_profiles && in_target && /^  [a-zA-Z0-9_-]+:$/ { in_target=0 }
        in_profiles && in_target && /inherits_from:/ {
            sub(/^[[:space:]]*inherits_from:[[:space:]]*/, "")
            gsub(/[[:space:]]*$/, "")
            print
            exit
        }
    ' "$config_file")

    echo "$value"
}

# Build the profile inheritance chain (from base to requested profile)
# Returns newline-separated list of profiles, base first
# Exits with error if circular dependency detected
get_profile_inheritance_chain() {
    local config_file=$1
    local profile_name=$2
    local profiles_dir=$3

    local chain=""
    local visited=""
    local current="$profile_name"

    # Build chain by following inherits_from links
    while [[ -n "$current" ]]; do
        # Check for circular dependency
        if echo "$visited" | grep -q "^${current}$"; then
            # Build the cycle path for error message
            local cycle_path="$current"
            local trace="$profile_name"
            while [[ "$trace" != "$current" ]] || [[ -z "$cycle_path" || "$cycle_path" == "$current" ]]; do
                local parent=$(get_profile_inherits_from "$config_file" "$trace")
                if [[ "$trace" == "$profile_name" ]]; then
                    cycle_path="$trace"
                else
                    cycle_path="$cycle_path → $trace"
                fi
                if [[ "$parent" == "$current" ]]; then
                    cycle_path="$cycle_path → $current"
                    break
                fi
                trace="$parent"
            done
            echo "CIRCULAR:$cycle_path"
            return 1
        fi

        # Check that profile directory exists
        if [[ ! -d "$profiles_dir/$current" ]]; then
            echo "NOTFOUND:$current"
            return 1
        fi

        # Add to visited list
        if [[ -n "$visited" ]]; then
            visited="$visited"$'\n'"$current"
        else
            visited="$current"
        fi

        # Add to chain (prepend so base ends up first)
        if [[ -n "$chain" ]]; then
            chain="$current"$'\n'"$chain"
        else
            chain="$current"
        fi

        # Get parent profile
        current=$(get_profile_inherits_from "$config_file" "$current")
    done

    echo "$chain"
}

# -----------------------------------------------------------------------------
# File Operations
# -----------------------------------------------------------------------------

# Create directory if it doesn't exist
ensure_dir() {
    local dir=$1
    if [[ ! -d "$dir" ]]; then
        mkdir -p "$dir"
        print_verbose "Created directory: $dir"
    fi
}

# Copy file with directory creation
copy_file() {
    local source=$1
    local dest=$2

    ensure_dir "$(dirname "$dest")"
    cp "$source" "$dest"
    print_verbose "Copied: $source -> $dest"
}

# Copy directory contents recursively (excluding .backups/)
copy_standards() {
    local source_dir=$1
    local dest_dir=$2
    local count=0

    if [[ ! -d "$source_dir" ]]; then
        return 0
    fi

    ensure_dir "$dest_dir"

    # Find all .md files, excluding .backups directory
    while IFS= read -r -d '' file; do
        local relative_path="${file#$source_dir/}"
        local dest_file="$dest_dir/$relative_path"

        ensure_dir "$(dirname "$dest_file")"
        cp "$file" "$dest_file"
        ((count++))
    done < <(find "$source_dir" -name "*.md" -type f ! -path "*/.backups/*" -print0 2>/dev/null)

    echo "$count"
}
```

## File: `scripts/project-install.sh`
```bash
#!/bin/bash

# =============================================================================
# Agent OS Project Installation Script
# Installs Agent OS into a project's codebase
# =============================================================================

set -e

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASE_DIR="$(dirname "$SCRIPT_DIR")"
PROJECT_DIR="$(pwd)"

# Source common functions
source "$SCRIPT_DIR/common-functions.sh"

# -----------------------------------------------------------------------------
# Default Values
# -----------------------------------------------------------------------------

VERBOSE="false"
PROFILE=""
COMMANDS_ONLY="false"

# -----------------------------------------------------------------------------
# Help Function
# -----------------------------------------------------------------------------

show_help() {
    cat << EOF
Usage: $0 [OPTIONS]

Install Agent OS into the current project directory.

Options:
    --profile <name>     Use specified profile (default: from config.yml)
    --commands-only      Only update commands, preserve existing standards
    --verbose            Show detailed output
    -h, --help           Show this help message

Examples:
    $0
    $0 --profile rails
    $0 --commands-only

EOF
    exit 0
}

# -----------------------------------------------------------------------------
# Parse Command Line Arguments
# -----------------------------------------------------------------------------

parse_arguments() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            --profile)
                PROFILE="$2"
                shift 2
                ;;
            --commands-only)
                COMMANDS_ONLY="true"
                shift
                ;;
            --verbose)
                VERBOSE="true"
                shift
                ;;
            -h|--help)
                show_help
                ;;
            *)
                print_error "Unknown option: $1"
                show_help
                ;;
        esac
    done
}

# -----------------------------------------------------------------------------
# Validation Functions
# -----------------------------------------------------------------------------

validate_base_installation() {
    if [[ ! -d "$BASE_DIR" ]]; then
        print_error "Agent OS base installation not found"
        exit 1
    fi

    if [[ ! -f "$BASE_DIR/config.yml" ]]; then
        print_error "Base installation config.yml not found"
        exit 1
    fi
}

validate_not_in_base() {
    if [[ "$PROJECT_DIR" == "$BASE_DIR" ]]; then
        print_error "Cannot install Agent OS in the base installation directory"
        echo ""
        echo "Navigate to your project directory first:"
        echo "  cd /path/to/your/project"
        echo ""
        exit 1
    fi
}

# -----------------------------------------------------------------------------
# Configuration Functions
# -----------------------------------------------------------------------------

load_configuration() {
    local config_file="$BASE_DIR/config.yml"

    # Get default profile from config
    local default_profile=$(get_yaml_value "$config_file" "default_profile" "default")

    # Use command line profile or default
    EFFECTIVE_PROFILE="${PROFILE:-$default_profile}"

    # Validate profile exists
    if [[ ! -d "$BASE_DIR/profiles/$EFFECTIVE_PROFILE" ]]; then
        print_error "Profile not found: $EFFECTIVE_PROFILE"
        exit 1
    fi

    # Build inheritance chain
    local chain_result=$(get_profile_inheritance_chain "$config_file" "$EFFECTIVE_PROFILE" "$BASE_DIR/profiles")

    # Check for errors
    if [[ "$chain_result" == CIRCULAR:* ]]; then
        local cycle_path="${chain_result#CIRCULAR:}"
        echo ""
        print_error "Circular dependency detected in profile inheritance chain:"
        echo "  $cycle_path"
        echo ""
        echo "Please fix the inheritance configuration in:"
        echo "  $config_file"
        echo ""
        echo "The 'profiles' section contains a circular reference that must be resolved."
        exit 1
    fi

    if [[ "$chain_result" == NOTFOUND:* ]]; then
        local missing_profile="${chain_result#NOTFOUND:}"
        print_error "Profile not found: $missing_profile"
        echo ""
        echo "This profile is referenced in the inheritance chain but doesn't exist."
        echo "Check the 'profiles' section in: $config_file"
        exit 1
    fi

    # Store the inheritance chain (newline-separated, base first)
    INHERITANCE_CHAIN="$chain_result"

    print_verbose "Using profile: $EFFECTIVE_PROFILE"
    print_verbose "Inheritance chain: $(echo "$INHERITANCE_CHAIN" | tr '\n' ' ')"
}

# -----------------------------------------------------------------------------
# Confirmation Functions
# -----------------------------------------------------------------------------

confirm_standards_overwrite() {
    if [[ "$COMMANDS_ONLY" == "true" ]]; then
        return 0
    fi

    local existing_standards="$PROJECT_DIR/agent-os/standards"

    if [[ -d "$existing_standards" ]]; then
        echo ""
        print_warning "Existing standards folder detected at: $existing_standards"
        echo ""
        echo "This will overwrite your existing standards with standards from the '$EFFECTIVE_PROFILE' profile."
        echo ""
        read -p "Do you want to continue? (y/N) " -n 1 -r
        echo ""
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo ""
            echo "Installation cancelled."
            echo ""
            echo "To update only commands without touching standards, use:"
            echo "  $0 --commands-only"
            echo ""
            exit 0
        fi
    fi
}

# -----------------------------------------------------------------------------
# Installation Functions
# -----------------------------------------------------------------------------

create_project_structure() {
    print_status "Creating project structure..."

    ensure_dir "$PROJECT_DIR/agent-os"
    ensure_dir "$PROJECT_DIR/agent-os/standards"

    print_success "Created agent-os/ directory structure"
}

install_standards() {
    if [[ "$COMMANDS_ONLY" == "true" ]]; then
        print_status "Skipping standards (--commands-only)"
        return
    fi

    echo ""
    print_status "Installing standards..."

    local project_standards="$PROJECT_DIR/agent-os/standards"
    local profiles_used=0

    # Temp file to track file sources (format: relative_path|profile_name)
    local sources_file=$(mktemp)
    trap "rm -f $sources_file" EXIT

    # Process each profile in the inheritance chain (base first, so later ones override)
    while IFS= read -r profile_name; do
        [[ -z "$profile_name" ]] && continue

        local profile_standards="$BASE_DIR/profiles/$profile_name/standards"

        if [[ ! -d "$profile_standards" ]]; then
            continue
        fi

        local profile_file_count=0

        # Find all .md files in this profile, excluding .backups
        while IFS= read -r -d '' file; do
            local relative_path="${file#$profile_standards/}"
            local dest_file="$project_standards/$relative_path"

            ensure_dir "$(dirname "$dest_file")"
            cp "$file" "$dest_file"

            # Track the source - remove old entry if exists, add new one
            grep -v "^${relative_path}|" "$sources_file" > "${sources_file}.tmp" 2>/dev/null || true
            mv "${sources_file}.tmp" "$sources_file"
            echo "${relative_path}|${profile_name}" >> "$sources_file"
            ((profile_file_count++))
        done < <(find "$profile_standards" -name "*.md" -type f ! -path "*/.backups/*" -print0 2>/dev/null)

        if [[ "$profile_file_count" -gt 0 ]]; then
            ((profiles_used++))
        fi
    done <<< "$INHERITANCE_CHAIN"

    # Count profiles in chain to determine if we show sources
    local chain_count=$(echo "$INHERITANCE_CHAIN" | grep -c .)

    # Count and display
    local total_count=$(wc -l < "$sources_file" | tr -d ' ')

    if [[ "$total_count" -gt 0 ]]; then
        # Sort and display files - only show source if inheritance is present
        sort "$sources_file" | while IFS='|' read -r filepath profile; do
            if [[ "$chain_count" -gt 1 ]]; then
                echo "  $filepath (from $profile)"
            else
                echo "  $filepath"
            fi
        done

        if [[ "$profiles_used" -gt 1 ]]; then
            print_success "Installed $total_count standards files (from $profiles_used profiles)"
        else
            print_success "Installed $total_count standards files"
        fi
    else
        print_success "No standards to install (profile is empty)"
    fi
}

create_index() {
    echo ""
    print_status "Updating standards index..."

    local standards_dir="$PROJECT_DIR/agent-os/standards"
    local index_file="$standards_dir/index.yml"
    local temp_file="$standards_dir/.index_temp.yml"
    local old_index=""

    # Save existing index content for description lookup
    if [[ -f "$index_file" ]]; then
        old_index=$(cat "$index_file")
    fi

    local entry_count=0
    local new_count=0

    # Start fresh
    echo "# Agent OS Standards Index" > "$temp_file"
    echo "" >> "$temp_file"

    # Helper to get existing description from old index
    # Looks for pattern: folder:\n  filename:\n    description: ...
    get_existing_description() {
        local folder="$1"
        local filename="$2"

        if [[ -z "$old_index" ]]; then
            return 1
        fi

        # Use awk to find the description for this folder/file combo
        local desc=$(echo "$old_index" | awk -v folder="$folder" -v file="$filename" '
            $0 ~ "^"folder":$" { in_folder=1; next }
            /^[a-zA-Z0-9_-]+:$/ { in_folder=0 }
            in_folder && $0 ~ "^  "file":$" { in_file=1; next }
            in_folder && /^  [a-zA-Z0-9_-]+:$/ { in_file=0 }
            in_folder && in_file && /description:/ {
                sub(/^[[:space:]]*description:[[:space:]]*/, "")
                print
                exit
            }
        ')

        if [[ -n "$desc" && "$desc" != "Needs description - run /index-standards" ]]; then
            echo "$desc"
            return 0
        fi
        return 1
    }

    # First, handle root-level .md files (not in subfolders)
    local root_files=$(find "$standards_dir" -maxdepth 1 -name "*.md" -type f 2>/dev/null | sort)
    if [[ -n "$root_files" ]]; then
        echo "root:" >> "$temp_file"
        while IFS= read -r file; do
            local filename=$(basename "$file" .md)
            local desc=$(get_existing_description "root" "$filename")
            if [[ -z "$desc" ]]; then
                desc="Needs description - run /index-standards"
                ((new_count++))
            fi
            echo "  $filename:" >> "$temp_file"
            echo "    description: $desc" >> "$temp_file"
            ((entry_count++))
        done <<< "$root_files"
        echo "" >> "$temp_file"
    fi

    # Then handle files in subfolders
    local folders=$(find "$standards_dir" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | sort)
    for folder in $folders; do
        local folder_name=$(basename "$folder")
        local md_files=$(find "$folder" -name "*.md" -type f 2>/dev/null | sort)

        if [[ -n "$md_files" ]]; then
            echo "$folder_name:" >> "$temp_file"
            while IFS= read -r file; do
                local filename=$(basename "$file" .md)
                local desc=$(get_existing_description "$folder_name" "$filename")
                if [[ -z "$desc" ]]; then
                    desc="Needs description - run /index-standards"
                    ((new_count++))
                fi
                echo "  $filename:" >> "$temp_file"
                echo "    description: $desc" >> "$temp_file"
                ((entry_count++))
            done <<< "$md_files"
            echo "" >> "$temp_file"
        fi
    done

    # Move temp file to final location
    mv "$temp_file" "$index_file"

    if [[ "$entry_count" -gt 0 ]]; then
        if [[ "$new_count" -gt 0 ]]; then
            print_success "Updated index.yml ($entry_count entries, $new_count new)"
        else
            print_success "Updated index.yml ($entry_count entries)"
        fi
    else
        print_success "Created index.yml (no standards to index)"
    fi
}

install_commands() {
    echo ""
    print_status "Installing commands..."

    local commands_source="$BASE_DIR/commands/agent-os"
    local commands_dest="$PROJECT_DIR/.claude/commands/agent-os"

    if [[ ! -d "$commands_source" ]]; then
        print_warning "No commands found in base installation"
        return
    fi

    ensure_dir "$commands_dest"

    local count=0
    for file in "$commands_source"/*.md; do
        if [[ -f "$file" ]]; then
            cp "$file" "$commands_dest/"
            ((count++))
        fi
    done

    if [[ "$count" -gt 0 ]]; then
        print_success "Installed $count commands to .claude/commands/agent-os/"
    else
        print_warning "No command files found"
    fi
}

# -----------------------------------------------------------------------------
# Main Execution
# -----------------------------------------------------------------------------

main() {
    print_section "Agent OS Project Installation"

    # Parse arguments
    parse_arguments "$@"

    # Validations
    validate_not_in_base
    validate_base_installation

    # Load configuration
    load_configuration

    # Show configuration
    echo ""
    print_status "Configuration:"

    # Display inheritance chain
    local chain_depth=0
    local chain_display=""
    # Read chain in reverse order (from requested profile back to base) for display
    local reversed_chain=$(echo "$INHERITANCE_CHAIN" | tac)
    while IFS= read -r profile_name; do
        [[ -z "$profile_name" ]] && continue
        if [[ "$chain_depth" -eq 0 ]]; then
            chain_display="  Profile: $profile_name"
        else
            local indent=""
            for ((i=0; i<chain_depth; i++)); do
                indent="$indent  "
            done
            chain_display="$chain_display"$'\n'"$indent  ↳ inherits from: $profile_name"
        fi
        ((chain_depth++))
    done <<< "$reversed_chain"
    echo "$chain_display"

    echo "  Commands only: $COMMANDS_ONLY"

    # Confirm overwrite if standards folder exists
    confirm_standards_overwrite

    echo ""

    # Install
    create_project_structure
    install_standards
    create_index
    install_commands

    echo ""
    print_success "Agent OS installed successfully!"
    echo ""
    echo "Next steps:"
    echo "  1. Run /discover-standards to extract patterns from your codebase"
    echo "  2. Run /inject-standards to inject standards into your context"
    echo ""
}

# Run main function
main "$@"
```

## File: `scripts/sync-to-profile.sh`
```bash
#!/bin/bash

# =============================================================================
# Agent OS Sync to Profile Script
# Syncs project standards back to a base profile for reuse
# =============================================================================

set -e

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASE_DIR="$(dirname "$SCRIPT_DIR")"
PROJECT_DIR="$(pwd)"

# Source common functions
source "$SCRIPT_DIR/common-functions.sh"

# -----------------------------------------------------------------------------
# Default Values
# -----------------------------------------------------------------------------

VERBOSE="false"
PROFILE=""
NEW_PROFILE=""
SYNC_ALL="false"
OVERWRITE="false"

# Arrays for file handling
declare -a STANDARDS_FILES
declare -a SELECTED_FILES

# -----------------------------------------------------------------------------
# Help Function
# -----------------------------------------------------------------------------

show_help() {
    cat << EOF
Usage: $0 [OPTIONS]

Sync project standards back to a base profile for reuse.

Options:
    --profile <name>       Target profile (skips selection prompt)
    --new-profile <name>   Create a new profile with these standards
    --all                  Sync all standards (skips file selection)
    --overwrite            Overwrite existing files without prompting
    --verbose              Show detailed output
    -h, --help             Show this help message

Examples:
    $0
    $0 --profile rails
    $0 --all --overwrite
    $0 --new-profile nextjs --all

EOF
    exit 0
}

# -----------------------------------------------------------------------------
# Parse Command Line Arguments
# -----------------------------------------------------------------------------

parse_arguments() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            --profile)
                PROFILE="$2"
                shift 2
                ;;
            --new-profile)
                NEW_PROFILE="$2"
                shift 2
                ;;
            --all)
                SYNC_ALL="true"
                shift
                ;;
            --overwrite)
                OVERWRITE="true"
                shift
                ;;
            --verbose)
                VERBOSE="true"
                shift
                ;;
            -h|--help)
                show_help
                ;;
            *)
                print_error "Unknown option: $1"
                show_help
                ;;
        esac
    done
}

# -----------------------------------------------------------------------------
# Validation Functions
# -----------------------------------------------------------------------------

validate_base_installation() {
    if [[ ! -d "$BASE_DIR" ]]; then
        print_error "Agent OS base installation not found"
        exit 1
    fi

    if [[ ! -d "$BASE_DIR/profiles" ]]; then
        print_error "No profiles directory in base installation"
        exit 1
    fi
}

validate_project_standards() {
    local standards_dir="$PROJECT_DIR/agent-os/standards"

    if [[ ! -d "$standards_dir" ]]; then
        print_error "No standards directory found at agent-os/standards/"
        echo ""
        echo "Run project-install.sh first to set up Agent OS in this project."
        exit 1
    fi
}

# -----------------------------------------------------------------------------
# Standards Discovery
# -----------------------------------------------------------------------------

find_standards_files() {
    local standards_dir="$PROJECT_DIR/agent-os/standards"
    STANDARDS_FILES=()

    # Find all .md files, excluding .backups directory
    while IFS= read -r -d '' file; do
        local relative_path="${file#$standards_dir/}"
        STANDARDS_FILES+=("$relative_path")
    done < <(find "$standards_dir" -name "*.md" -type f ! -path "*/.backups/*" -print0 2>/dev/null | sort -z)

    if [[ ${#STANDARDS_FILES[@]} -eq 0 ]]; then
        print_error "No standards to sync."
        echo ""
        echo "Create standards first using /discover-standards or manually."
        exit 1
    fi

    print_verbose "Found ${#STANDARDS_FILES[@]} standards files"
}

# -----------------------------------------------------------------------------
# Profile Selection
# -----------------------------------------------------------------------------

list_existing_profiles() {
    local profiles=()
    for dir in "$BASE_DIR/profiles"/*/; do
        if [[ -d "$dir" ]]; then
            local name=$(basename "$dir")
            profiles+=("$name")
        fi
    done
    echo "${profiles[@]}"
}

select_profile() {
    # If --new-profile was specified, use that
    if [[ -n "$NEW_PROFILE" ]]; then
        PROFILE="$NEW_PROFILE"
        create_profile_if_needed
        return
    fi

    # If --profile was specified, validate it
    if [[ -n "$PROFILE" ]]; then
        if [[ ! -d "$BASE_DIR/profiles/$PROFILE" ]]; then
            echo ""
            read -p "Profile '$PROFILE' doesn't exist. Create it? (y/n): " create_choice
            if [[ "$create_choice" =~ ^[Yy] ]]; then
                create_new_profile "$PROFILE"
            else
                print_error "Cancelled."
                exit 1
            fi
        fi
        return
    fi

    # Interactive profile selection
    echo ""
    print_status "Available profiles:"
    echo ""

    local profiles=($(list_existing_profiles))
    local i=1

    for profile in "${profiles[@]}"; do
        echo "  $i) $profile"
        ((i++))
    done
    echo "  $i) [Create new profile]"
    echo ""

    local max_choice=$i
    local choice

    while true; do
        read -p "Select profile (1-$max_choice): " choice

        if [[ "$choice" =~ ^[0-9]+$ ]] && [[ "$choice" -ge 1 ]] && [[ "$choice" -le "$max_choice" ]]; then
            break
        fi
        echo "Invalid choice. Please enter a number between 1 and $max_choice."
    done

    if [[ "$choice" -eq "$max_choice" ]]; then
        # Create new profile
        echo ""
        read -p "Enter new profile name: " PROFILE
        if [[ -z "$PROFILE" ]]; then
            print_error "Profile name cannot be empty."
            exit 1
        fi
        create_new_profile "$PROFILE"
    else
        PROFILE="${profiles[$((choice-1))]}"
    fi

    print_verbose "Selected profile: $PROFILE"
}

create_profile_if_needed() {
    if [[ ! -d "$BASE_DIR/profiles/$PROFILE" ]]; then
        create_new_profile "$PROFILE"
    fi
}

create_new_profile() {
    local name="$1"
    local profile_dir="$BASE_DIR/profiles/$name"

    mkdir -p "$profile_dir/standards"
    print_success "Created new profile: $name"
}

# -----------------------------------------------------------------------------
# File Selection
# -----------------------------------------------------------------------------

select_files() {
    # If --all was specified, select all files
    if [[ "$SYNC_ALL" == "true" ]]; then
        SELECTED_FILES=("${STANDARDS_FILES[@]}")
        print_verbose "Selected all ${#SELECTED_FILES[@]} files"
        return
    fi

    # Initialize selection array (all selected by default)
    local selected=()
    for ((i=0; i<${#STANDARDS_FILES[@]}; i++)); do
        selected[$i]=1
    done

    # Calculate lines to clear (files + 5 for header/footer)
    local lines_to_clear=$((${#STANDARDS_FILES[@]} + 7))

    display_file_selection() {
        echo ""
        print_status "Select standards to sync:"
        echo ""
        local i=1
        for file in "${STANDARDS_FILES[@]}"; do
            if [[ ${selected[$((i-1))]} -eq 1 ]]; then
                echo "  $i) [x] $file"
            else
                echo "  $i) [ ] $file"
            fi
            ((i++))
        done
        echo ""
        echo ""
        echo "  Enter number to toggle   a) All   n) None   d) Done"
        echo ""
    }

    clear_display() {
        # Move cursor up and clear lines
        for ((i=0; i<lines_to_clear; i++)); do
            tput cuu1 2>/dev/null || echo -ne "\033[1A"
            tput el 2>/dev/null || echo -ne "\033[2K"
        done
    }

    local first_display=true

    while true; do
        if [[ "$first_display" == "true" ]]; then
            first_display=false
        else
            clear_display
        fi

        display_file_selection
        read -p "Toggle (1-${#STANDARDS_FILES[@]}), a, n, or d: " choice

        case "$choice" in
            a|A)
                for ((i=0; i<${#STANDARDS_FILES[@]}; i++)); do
                    selected[$i]=1
                done
                ;;
            n|N)
                for ((i=0; i<${#STANDARDS_FILES[@]}; i++)); do
                    selected[$i]=0
                done
                ;;
            d|D)
                break
                ;;
            *)
                if [[ "$choice" =~ ^[0-9]+$ ]] && [[ "$choice" -ge 1 ]] && [[ "$choice" -le ${#STANDARDS_FILES[@]} ]]; then
                    local idx=$((choice-1))
                    if [[ ${selected[$idx]} -eq 1 ]]; then
                        selected[$idx]=0
                    else
                        selected[$idx]=1
                    fi
                fi
                # Invalid input just redisplays
                ;;
        esac
    done

    # Build selected files array
    SELECTED_FILES=()
    for ((i=0; i<${#STANDARDS_FILES[@]}; i++)); do
        if [[ ${selected[$i]} -eq 1 ]]; then
            SELECTED_FILES+=("${STANDARDS_FILES[$i]}")
        fi
    done

    if [[ ${#SELECTED_FILES[@]} -eq 0 ]]; then
        print_error "No files selected."
        exit 1
    fi

    print_verbose "Selected ${#SELECTED_FILES[@]} files"
}

# -----------------------------------------------------------------------------
# Conflict Detection
# -----------------------------------------------------------------------------

check_conflicts() {
    local profile_standards="$BASE_DIR/profiles/$PROFILE/standards"
    local conflicts=()

    for file in "${SELECTED_FILES[@]}"; do
        if [[ -f "$profile_standards/$file" ]]; then
            conflicts+=("$file")
        fi
    done

    if [[ ${#conflicts[@]} -eq 0 ]]; then
        return 0
    fi

    # If --overwrite specified, just backup and continue
    if [[ "$OVERWRITE" == "true" ]]; then
        backup_files "${conflicts[@]}"
        return 0
    fi

    # Prompt user
    echo ""
    print_warning "${#conflicts[@]} file(s) already exist in profile '$PROFILE':"
    for file in "${conflicts[@]}"; do
        echo "    - $file"
    done
    echo ""

    while true; do
        echo "What do you want to do?"
        echo "  1) Overwrite all (with backup)"
        echo "  2) Skip existing files"
        echo "  3) Cancel"
        echo ""
        read -p "Choice (1-3): " conflict_choice

        case "$conflict_choice" in
            1)
                backup_files "${conflicts[@]}"
                return 0
                ;;
            2)
                # Remove conflicts from selected files
                local new_selected=()
                for file in "${SELECTED_FILES[@]}"; do
                    local is_conflict=false
                    for conflict in "${conflicts[@]}"; do
                        if [[ "$file" == "$conflict" ]]; then
                            is_conflict=true
                            break
                        fi
                    done
                    if [[ "$is_conflict" == "false" ]]; then
                        new_selected+=("$file")
                    fi
                done
                SELECTED_FILES=("${new_selected[@]}")

                if [[ ${#SELECTED_FILES[@]} -eq 0 ]]; then
                    print_warning "No files left to sync after skipping conflicts."
                    exit 0
                fi
                return 0
                ;;
            3)
                print_error "Cancelled."
                exit 1
                ;;
            *)
                echo "Invalid choice."
                ;;
        esac
    done
}

# -----------------------------------------------------------------------------
# Backup Functions
# -----------------------------------------------------------------------------

backup_files() {
    local files=("$@")

    if [[ ${#files[@]} -eq 0 ]]; then
        return
    fi

    local profile_standards="$BASE_DIR/profiles/$PROFILE/standards"
    local timestamp=$(date +"%Y-%m-%d-%H%M")
    local backup_dir="$profile_standards/.backups/$timestamp"

    mkdir -p "$backup_dir"

    local backup_count=0
    for file in "${files[@]}"; do
        local source_file="$profile_standards/$file"
        local backup_file="$backup_dir/$file"

        if [[ -f "$source_file" ]]; then
            mkdir -p "$(dirname "$backup_file")"
            cp "$source_file" "$backup_file"
            ((backup_count++))
            print_verbose "Backed up: $file"
        fi
    done

    if [[ "$backup_count" -gt 0 ]]; then
        print_success "Backed up $backup_count file(s) to .backups/$timestamp/"
    fi
}

# -----------------------------------------------------------------------------
# Sync Execution
# -----------------------------------------------------------------------------

execute_sync() {
    local project_standards="$PROJECT_DIR/agent-os/standards"
    local profile_standards="$BASE_DIR/profiles/$PROFILE/standards"

    local sync_count=0
    for file in "${SELECTED_FILES[@]}"; do
        local source_file="$project_standards/$file"
        local dest_file="$profile_standards/$file"

        # Create directory if needed
        mkdir -p "$(dirname "$dest_file")"

        # Copy the file
        cp "$source_file" "$dest_file"
        ((sync_count++))
        print_verbose "Synced: $file"
    done

    echo ""
    print_success "Synced $sync_count file(s) to profile '$PROFILE'"
}

# -----------------------------------------------------------------------------
# Main Execution
# -----------------------------------------------------------------------------

main() {
    print_section "Agent OS Sync to Profile"

    # Parse arguments
    parse_arguments "$@"

    # Validations
    validate_base_installation
    validate_project_standards

    # Find standards files
    find_standards_files

    # Select target profile
    select_profile

    # Select files to sync
    select_files

    # Show summary
    echo ""
    print_status "Sync summary:"
    echo "  Profile: $PROFILE"
    echo "  Files to sync: ${#SELECTED_FILES[@]}"
    echo ""

    # Check for conflicts and handle them
    check_conflicts

    # Execute sync
    execute_sync

    echo ""
}

# Run main function
main "$@"
```

