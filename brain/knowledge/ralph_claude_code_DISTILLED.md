---
id: ralph-claude-code
type: knowledge
owner: OA_Triage
---
# ralph-claude-code
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "ralph-claude-code",
  "version": "1.0.0",
  "description": "> **Autonomous AI development loop with intelligent exit detection and rate limiting**",
  "main": "index.js",
  "directories": {
    "doc": "docs",
    "example": "examples",
    "test": "tests"
  },
  "scripts": {
    "test": "bats tests/unit/ tests/integration/",
    "test:unit": "bats tests/unit/",
    "test:integration": "bats tests/integration/",
    "test:e2e": "bats tests/e2e/"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/frankbria/ralph-claude-code.git"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "bugs": {
    "url": "https://github.com/frankbria/ralph-claude-code/issues"
  },
  "homepage": "https://github.com/frankbria/ralph-claude-code#readme",
  "devDependencies": {
    "bats": "^1.12.0",
    "bats-assert": "^2.2.0",
    "bats-support": "^0.3.0"
  }
}

```

### File: README.md
```md
# Ralph for Claude Code

[![CI](https://github.com/frankbria/ralph-claude-code/actions/workflows/test.yml/badge.svg)](https://github.com/frankbria/ralph-claude-code/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Version](https://img.shields.io/badge/version-0.11.5-blue)
![Tests](https://img.shields.io/badge/tests-556%20passing-green)
[![GitHub Issues](https://img.shields.io/github/issues/frankbria/ralph-claude-code)](https://github.com/frankbria/ralph-claude-code/issues)
[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge.svg)](https://github.com/hesreallyhim/awesome-claude-code)
[![Follow on X](https://img.shields.io/twitter/follow/FrankBria18044?style=social)](https://x.com/FrankBria18044)

> **Autonomous AI development loop with intelligent exit detection and rate limiting**

Ralph is an implementation of the Geoffrey Huntley's technique for Claude Code that enables continuous autonomous development cycles he named after [Ralph Wiggum](https://ghuntley.com/ralph/). It enables continuous autonomous development cycles where Claude Code iteratively improves your project until completion, with built-in safeguards to prevent infinite loops and API overuse.

**Install once, use everywhere** - Ralph becomes a global command available in any directory.

## Project Status

**Version**: v0.11.5 - Active Development
**Core Features**: Working and tested
**Test Coverage**: 566 tests, 100% pass rate

### What's Working Now
- Autonomous development loops with intelligent exit detection
- **Dual-condition exit gate**: Requires BOTH completion indicators AND explicit EXIT_SIGNAL
- Rate limiting with hourly reset (100 calls/hour, configurable)
- Circuit breaker with advanced error detection (prevents runaway loops)
- Response analyzer with semantic understanding and two-stage error filtering
- **JSON output format support with automatic fallback to text parsing**
- **Session continuity with `--resume` flag for context preservation (no session hijacking)**
- **Session expiration with configurable timeout (default: 24 hours)**
- **Modern CLI flags: `--output-format`, `--allowed-tools`, `--no-continue`**
- **Interactive project enablement with `ralph-enable` wizard**
- **`.ralphrc` configuration file for project settings**
- **Live streaming output with `--live` flag for real-time Claude Code visibility**
- Multi-line error matching for accurate stuck loop detection
- 5-hour API limit handling with user prompts
- tmux integration for live monitoring
- PRD import functionality
- **CI/CD pipeline with GitHub Actions**
- **Dedicated uninstall script for clean removal**

### Recent Improvements

**v0.11.5 - Community Bug Fixes** (latest)
- Fixed API limit false positive: Timeout (exit code 124) no longer misidentified as API 5-hour limit (#183)
- Three-layer API limit detection: timeout guard → structural JSON (`rate_limit_event`) → filtered text fallback
- Unattended mode: API limit prompt now auto-waits on timeout instead of exiting
- Fixed bash 3.x compatibility: `${,,}` lowercase substitution replaced with POSIX `tr` (#187)
- Added 8 new tests for API limit detection (548 → 566 tests)

**v0.11.4 - Bug Fixes & Compatibility**
- Fixed progress detection: Git commits within a loop now count as progress (#141)
- Fixed checkbox regex: Date entries `[2026-01-29]` no longer counted as checkboxes (#144)
- Fixed session hijacking: Use `--resume <session_id>` instead of `--continue` (#151)
- Fixed EXIT_SIGNAL override: `STATUS: COMPLETE` with `EXIT_SIGNAL: false` now continues working (#146)
- Fixed ralph-import hanging indefinitely (added `--print` flag for non-interactive mode)
- Fixed ralph-import absolute path handling
- Fixed cross-platform date commands for macOS with Homebrew coreutils
- Added configurable circuit breaker thresholds via environment variables (#99)
- Added tmux support for non-zero `base-index` configurations
- Added 13 new regression tests for progress detection and checkbox regex

**v0.11.3 - Live Streaming & Beads Fix**
- Added live streaming output mode with `--live` flag for real-time Claude Code visibility (#125)
- Fixed beads task import using correct `bd list` arguments (#150)
- Applied CodeRabbit review fixes: camelCase variables, status-respecting fallback, jq guards
- Added 12 new tests for live streaming and beads import improvements

**v0.11.2 - Setup Permissions Fix**
- Fixed issue #136: `ralph-setup` now creates `.ralphrc` with consistent tool permissions
- Updated default `ALLOWED_TOOLS` to include `Edit`, `Bash(npm *)`, and `Bash(pytest)`
- Both `ralph-setup` and `ralph-enable` now create identical `.ralphrc` configurations
- Monitor now forwards all CLI parameters to inner ralph loop (#126)
- Added 16 new tests for permissions and parameter forwarding

**v0.11.1 - Completion Indicators Fix**
- Fixed premature exit after exactly 5 loops in JSON output mode
- `completion_indicators` now only accumulates when `EXIT_SIGNAL: true`
- Aligns with documented dual-condition exit gate behavior

**v0.11.0 - Ralph Enable Wizard**
- Added `ralph-enable` interactive wizard for enabling Ralph in existing projects
- 5-phase wizard: Environment Detection → Task Source Selection → Configuration → File Generation → Verification
- Auto-detects project type (TypeScript, Python, Rust, Go) and framework (Next.js, FastAPI, Django)
- Imports tasks from beads, GitHub Issues, or PRD documents
- Added `ralph-enable-ci` non-interactive version for CI/automation
- New library components: `enable_core.sh`, `wizard_utils.sh`, `task_sources.sh`

**v0.10.1 - Bug Fixes & Monitor Path Corrections**
- Fixed `ralph_monitor.sh` hardcoded paths for v0.10.0 compatibility
- Fixed EXIT_SIGNAL parsing in JSON format
- Added safety circuit breaker (force exit after 5 consecutive completion indicators)
- Fixed checkbox parsing for indented markdown

**v0.10.0 - .ralph/ Subfolder Structure (BREAKING CHANGE)**
- **Breaking**: Moved all Ralph-specific files to `.ralph/` subfolder
- Project root stays clean: only `src/`, `README.md`, and user files remain
- Added `ralph-migrate` command for upgrading existing projects

<details>
<summary>Earlier versions (v0.9.x)</summary>

**v0.9.9 - EXIT_SIGNAL Gate & Uninstall Script**
- Fixed premature exit bug: completion indicators now require Claude's explicit `EXIT_SIGNAL: true`
- Added dedicated `uninstall.sh` script for clean Ralph removal

**v0.9.8 - Modern CLI for PRD Import**
- Modernized `ralph_import.sh` to use Claude Code CLI JSON output format
- Enhanced error handling with structured JSON error messages

**v0.9.7 - Session Lifecycle Management**
- Complete session lifecycle management with automatic reset triggers
- Added `--reset-session` CLI flag for manual session reset

**v0.9.6 - JSON Output & Session Management**
- Extended `parse_json_response()` to support Claude Code CLI JSON format
- Added session management functions

**v0.9.5 - v0.9.0** - PRD import tests, project setup tests, installation tests, prompt file fix, modern CLI commands, circuit breaker enhancements

</details>

### In Progress
- Expanding test coverage
- [Automated badge updates](#138)

**Timeline to v1.0**: ~4 weeks | [Full roadmap](IMPLEMENTATION_PLAN.md) | **Contributions welcome!**

## Features

- **Autonomous Development Loop** - Continuously executes Claude Code with your project requirements
- **Intelligent Exit Detection** - Dual-condition check requiring BOTH completion indicators AND explicit EXIT_SIGNAL
- **Session Continuity** - Preserves context across loop iterations with automatic session management
- **Session Expiration** - Configurable timeout (default: 24 hours) with automatic session reset
- **Rate Limiting** - Built-in API call management with hourly limits and countdown timers
- **5-Hour API Limit Handling** - Three-layer detection (timeout guard, JSON parsing, filtered text) with auto-wait for unattended mode
- **Live Monitoring** - Real-time dashboard showing loop status, progress, and logs
- **Task Management** - Structured approach with prioritized task lists and progress tracking
- **Project Templates** - Quick setup for new projects with best-practice structure
- **Interactive Project Setup** - `ralph-enable` wizard for existing projects with task import
- **Configuration Files** - `.ralphrc` for project-specific settings and tool permissions
- **Comprehensive Logging** - Detailed execution logs with timestamps and status tracking
- **Configurable Timeouts** - Set execution timeout for Claude Code operations (1-120 minutes)
- **Verbose Progress Mode** - Optional detailed progress updates during execution
- **Response Analyzer** - AI-powered analysis of Claude Code responses with semantic understanding
- **Circuit Breaker** - Advanced error detection with two-stage filtering, multi-line error matching, and automatic recovery
- **CI/CD Integration** - GitHub Actions workflow with automated testing
- **Clean Uninstall** - Dedicated uninstall script for complete removal
- **Live Streaming Output** - Real-time visibility into Claude Code execution with `--live` flag

## Quick Start

Ralph has two phases: **one-time installation** and **per-project setup**.

```
INSTALL ONCE              USE MANY TIMES
+-----------------+          +----------------------+
| ./install.sh    |    ->    | ralph-setup project1 |
|                 |          | ralph-enable         |
| Adds global     |          | ralph-import prd.md  |
| commands        |          | ...                  |
+-----------------+          +----------------------+
```

### Phase 1: Install Ralph (One Time Only)

Install Ralph globally on your system:

```bash
git clone https://github.com/frankbria/ralph-claude-code.git
cd ralph-claude-code
./install.sh
```

This adds `ralph`, `ralph-monitor`, `ralph-setup`, `ralph-import`, `ralph-migrate`, `ralph-enable`, and `ralph-enable-ci` commands to your PATH.

> **Note**: You only need to do this once per system. After installation, you can delete the cloned repository if desired.

### Phase 2: Initialize Projects (Per Project)

#### Option A: Enable Ralph in Existing Project (Recommended)
```bash
cd my-existing-project

# Interactive wizard - auto-detects project type and imports tasks
ralph-enable

# Or with specific task source
ralph-enable --from beads
ralph-enable --from github --label "sprint-1"
ralph-enable --from prd ./docs/requirements.md

# Start autonomous development
ralph --monitor
```

#### Option B: Import Existing PRD/Specifications
```bash
# Convert existing PRD/specs to Ralph format
ralph-import my-requirements.md my-project
cd my-project

# Review and adjust the generated files:
# - .ralph/PROMPT.md (Ralph instructions)
# - .ralph/fix_plan.md (task priorities)
# - .ralph/specs/requirements.md (technical specs)

# Start autonomous development
ralph --monitor
```

#### Option C: Create New Project from Scratch
```bash
# Create blank Ralph project
ralph-setup my-awesome-project
cd my-awesome-project

# Configure your project requirements manually
# Edit .ralph/PROMPT.md with your project goals
# Edit .ralph/specs/ with detailed specifications
# Edit .ralph/fix_plan.md with initial priorities

# Start autonomous development
ralph --monitor
```

### Ongoing Usage (After Setup)

Once Ralph is installed and your project is initialized:

```bash
# Navigate to any Ralph project and run:
ralph --monitor              # Integrated tmux monitoring (recommended)

# Or use separate terminals:
ralph                        # Terminal 1: Ralph loop
ralph-monitor               # Terminal 2: Live monitor dashboard
```

### Uninstalling Ralph

To completely remove Ralph from your system:

```bash
# Run the uninstall script
./uninstall.sh

# Or if you deleted the repo, download and run:
curl -sL https://raw.githubusercontent.com/frankbria/ralph-claude-code/main/uninstall.sh | bash
```

## Understanding Ralph Files

After running `ralph-enable` or `ralph-import`, you'll have a `.ralph/` directory with several files. Here's what each file does and whether you need to edit it:

| File | Auto-Generated? | You Should... |
|------|-----------------|---------------|
| `.ralph/PROMPT.md` | Yes (smart defaults) | **Review & customize** project goals and principles |
| `.ralph/fix_plan.md` | Yes (can import tasks) | **Add/modify** specific implementation tasks |
| `.ralph/AGENT.md` | Yes (detects build commands) | Rarely edit (auto-maintained by Ralph) |
| `.ralph/specs/` | Empty directory | Add files when PROMPT.md isn't detailed enough |
| `.ralph/specs/stdlib/` | Empty directory | Add reusable patterns and conventions |
| `.ralphrc` | Yes (project-aware) | Rarely edit (sensible defaults) |

### Key File Relationships

```
PROMPT.md (high-level goals)
    ↓
specs/ (detailed requirements when needed)
    ↓
fix_plan.md (specific tasks Ralph executes)
    ↓
AGENT.md (build/test commands - auto-maintained)
```

### When to Use specs/

- **Simple projects**: PROMPT.md + fix_plan.md is usually enough
- **Complex features**: Add specs/feature-name.md for detailed requirements
- **Team conventions**: Add specs/stdlib/convention-name.md for reusable patterns

See the [User Guide](docs/user-guide/) for detailed explanations and the [examples/](examples/) directory for realistic project configurations.

## How It Works

Ralph operates on a simple but powerful cycle:

1. **Read Instructions** - Loads `PROMPT.md` with your project requirements
2. **Execute Claude Code** - Runs Claude Code with current context and priorities
3. **Track Progress** - Updates task lists and logs execution results
4. **Evaluate Completion** - Checks for exit conditions and project completion signals
5. **Repeat** - Continues until project is complete or limits are reached

### Intelligent Exit Detection

Ralph uses a **dual-condition check** to prevent premature exits during productive iterations:

**Exit requires BOTH conditions:**
1. `completion_indicators >= 2` (heuristic detection from natural language patterns)
2. Claude's explicit `EXIT_SIGNAL: true` in the RALPH_STATUS block

**Example behavior:**
```
Loop 5: Claude outputs "Phase complete, moving to next feature"
        → completion_indicators: 3 (high confidence from patterns)
        → EXIT_SIGNAL: false (Claude says more work needed)
        → Result: CONTINUE (respects Claude's explicit intent)

Loop 8: Claude outputs "All tasks complete, project ready"
        → completion_indicators: 4
        → EXIT_SIGNAL: true (Claude confirms done)
        → Result: EXIT with "project_complete"
```

**Other exit conditions:**
- All tasks in `.ralph/fix_plan.md` marked complete
- Multiple consecutive "done" signals from Claude Code
- Too many test-focused loops (indicating feature completeness)
- Claude API 5-hour usage limit reached (with user prompt to wait or exit)

## Enabling Ralph in Existing Projects

The `ralph-enable` command provides an interactive wizard for adding Ralph to existing projects:

```bash
cd m
... [TRUNCATED]
```

### File: CLAUDE.md
```md
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the Ralph for Claude Code repository - an autonomous AI development loop system that enables continuous development cycles with intelligent exit detection and rate limiting.

See [README.md](README.md) for version info, changelog, and user documentation.

## Core Architecture

The system consists of four main bash scripts and a modular library system:

### Main Scripts

1. **ralph_loop.sh** - The main autonomous loop that executes Claude Code repeatedly
2. **ralph_monitor.sh** - Live monitoring dashboard for tracking loop status
3. **setup.sh** - Project initialization script for new Ralph projects
4. **create_files.sh** - Bootstrap script that creates the entire Ralph system
5. **ralph_import.sh** - PRD/specification import tool that converts documents to Ralph format
   - Uses modern Claude Code CLI with `--output-format json` for structured responses
   - Implements `detect_response_format()` and `parse_conversion_response()` for JSON parsing
   - Backward compatible with older CLI versions (automatic text fallback)
6. **ralph_enable.sh** - Interactive wizard for enabling Ralph in existing projects
   - Multi-step wizard with environment detection, task source selection, configuration
   - Imports tasks from beads, GitHub Issues, or PRD documents
   - Generates `.ralphrc` project configuration file
7. **ralph_enable_ci.sh** - Non-interactive version for CI/automation
   - Same functionality as interactive version with CLI flags
   - JSON output mode for machine parsing
   - Exit codes: 0 (success), 1 (error), 2 (already enabled)

### Library Components (lib/)

The system uses a modular architecture with reusable components in the `lib/` directory:

1. **lib/circuit_breaker.sh** - Circuit breaker pattern implementation
   - Prevents runaway loops by detecting stagnation
   - Three states: CLOSED (normal), HALF_OPEN (monitoring), OPEN (halted)
   - Configurable thresholds for no-progress and error detection
   - Automatic state transitions and recovery

2. **lib/response_analyzer.sh** - Intelligent response analysis
   - Analyzes Claude Code output for completion signals
   - **JSON output format detection and parsing** (with text fallback)
   - Supports both flat JSON format and Claude CLI format (`result`, `sessionId`, `metadata`)
   - Extracts structured fields: status, exit_signal, work_type, files_modified, asking_questions, question_count
   - **Question detection**: `detect_questions()` with `QUESTION_PATTERNS` array — detects when Claude asks questions instead of acting autonomously (Issue #190)
   - **Session management**: `store_session_id()`, `get_last_session_id()`, `should_resume_session()`
   - Automatic session persistence to `.ralph/.claude_session_id` file with 24-hour expiration
   - Session lifecycle: `get_session_id()`, `reset_session()`, `log_session_transition()`, `init_session_tracking()`
   - Session history tracked in `.ralph/.ralph_session_history` (last 50 transitions)
   - Session auto-reset on: circuit breaker open, manual interrupt, project completion
   - Detects test-only loops, stuck error patterns, and question-only loops
   - Two-stage error filtering to eliminate false positives
   - Multi-line error matching for accurate stuck loop detection
   - **Mode-specific heuristic exit**: In JSON mode, heuristics are suppressed entirely — only an explicit `EXIT_SIGNAL: true` in a RALPH_STATUS block can set `exit_signal=true` (Issue #224). In text mode, exit requires `confidence_score >= 70` AND `has_completion_signal=true` (raised from the old `>= 40 OR has_completion_signal` to prevent documentation keywords like "setup is done" from triggering false-positive exits).

3. **lib/date_utils.sh** - Cross-platform date utilities
   - ISO timestamp generation for logging
   - Epoch time calculations for rate limiting
   - ISO-to-epoch conversion for cooldown timer comparisons (`parse_iso_to_epoch()`)

4. **lib/timeout_utils.sh** - Cross-platform timeout command utilities
   - Detects and uses appropriate timeout command for the platform
   - Linux: Uses standard `timeout` from GNU coreutils
   - macOS: Uses `gtimeout` from Homebrew coreutils
   - `portable_timeout()` function for seamless cross-platform execution
   - Automatic detection with caching for performance

5. **lib/enable_core.sh** - Shared logic for ralph enable commands
   - Idempotency checks: `check_existing_ralph()`, `is_ralph_enabled()`
   - Safe file operations: `safe_create_file()`, `safe_create_dir()`
   - Project detection: `detect_project_context()`, `detect_git_info()`, `detect_task_sources()`
   - Template generation: `generate_prompt_md()`, `generate_agent_md()`, `generate_fix_plan_md()`, `generate_ralphrc()`

6. **lib/wizard_utils.sh** - Interactive prompt utilities for enable wizard
   - User prompts: `confirm()`, `prompt_text()`, `prompt_number()`
   - Selection utilities: `select_option()`, `select_multiple()`, `select_with_default()`
   - Output formatting: `print_header()`, `print_bullet()`, `print_success/warning/error/info()`
   - POSIX-compatible: Uses `tr '[:upper:]' '[:lower:]'` instead of `${,,}` for bash 3.x support (Issue #187)

7. **lib/task_sources.sh** - Task import from external sources
   - Beads integration: `check_beads_available()`, `fetch_beads_tasks()`, `get_beads_count()`
   - GitHub integration: `check_github_available()`, `fetch_github_tasks()`, `get_github_issue_count()`
   - PRD extraction: `extract_prd_tasks()`, supports checkbox and numbered list formats
   - Task normalization: `normalize_tasks()`, `prioritize_tasks()`, `import_tasks_from_sources()`

8. **lib/file_protection.sh** - File integrity validation for Ralph projects (Issue #149)
   - `RALPH_REQUIRED_PATHS` array: critical files needed for the loop to function
   - `validate_ralph_integrity()`: checks all required paths exist, sets `RALPH_MISSING_FILES`
   - `get_integrity_report()`: human-readable report with missing files and recovery instructions
   - Lightweight validation that runs every loop iteration

9. **lib/log_utils.sh** - Log management utilities (Issue #18)
   - `rotate_logs()`: rotates `$LOG_DIR/ralph.log` at 10MB, keeping 4 archived files (`.log.1`–`.log.4`)
   - Cross-platform `stat` support: GNU (`stat -c%s`) with BSD (`stat -f%z`) fallback

## Key Commands

### Installation
```bash
# Install Ralph globally (run once)
./install.sh

# Uninstall Ralph
./install.sh uninstall
```

### Setting Up a New Project
```bash
# Create a new Ralph-managed project (run from anywhere)
ralph-setup my-project-name
cd my-project-name
```

### Migrating Existing Projects
```bash
# Migrate from flat structure to .ralph/ subfolder (v0.10.0+)
cd existing-project
ralph-migrate
```

### Enabling Ralph in Existing Projects
```bash
# Interactive wizard (recommended for humans)
cd existing-project
ralph-enable

# With specific task source
ralph-enable --from beads
ralph-enable --from github --label "sprint-1"
ralph-enable --from prd ./docs/requirements.md

# Force overwrite existing .ralph/
ralph-enable --force

# Non-interactive for CI/scripts
ralph-enable-ci                              # Sensible defaults
ralph-enable-ci --from github               # With task source
ralph-enable-ci --project-type typescript   # Override detection
ralph-enable-ci --json                      # Machine-readable output
```

### Running the Ralph Loop
```bash
# Start with integrated tmux monitoring (recommended)
ralph --monitor

# Start without monitoring
ralph

# With custom parameters and monitoring
ralph --monitor --calls 50 --prompt my_custom_prompt.md

# Check current status
ralph --status

# Circuit breaker management
ralph --reset-circuit
ralph --circuit-status
ralph --auto-reset-circuit   # Auto-reset OPEN state on startup

# Session management
ralph --reset-session    # Reset session state manually

# Backup and rollback (requires git; Issue #23)
ralph --backup           # Enable automatic backup before each loop
ralph -b                 # Short form of --backup
ralph --rollback         # List available backup branches
ralph --rollback ralph-backup-loop-3-1775155286  # Roll back to a specific backup
```

### Monitoring
```bash
# Integrated tmux monitoring (recommended)
ralph --monitor

# Manual monitoring in separate terminal
ralph-monitor

# tmux session management
tmux list-sessions
tmux attach -t <session-name>
```

### Running Tests
```bash
# Run all tests
npm test

# Run specific test suites
npm run test:unit
npm run test:integration

# Run individual test files
bats tests/unit/test_cli_parsing.bats
bats tests/unit/test_json_parsing.bats
bats tests/unit/test_cli_modern.bats
bats tests/unit/test_enable_core.bats
bats tests/unit/test_task_sources.bats
bats tests/unit/test_ralph_enable.bats
bats tests/unit/test_circuit_breaker_recovery.bats
bats tests/unit/test_file_protection.bats
bats tests/unit/test_integrity_check.bats
```

## Ralph Loop Configuration

The loop is controlled by several key files and environment variables within the `.ralph/` subfolder:

- **.ralph/PROMPT.md** - Main prompt file that drives each loop iteration
- **.ralph/fix_plan.md** - Prioritized task list that Ralph follows
- **.ralph/AGENT.md** - Build and run instructions maintained by Ralph
- **.ralph/status.json** - Real-time status tracking (JSON format)
- **.ralph/logs/** - Execution logs for each loop iteration

### Rate Limiting
- Default: 100 API calls per hour (configurable via `--calls` flag)
- Optional token limit per hour via `MAX_TOKENS_PER_HOUR` in `.ralphrc` (0 = disabled, default)
  - Extracts `input_tokens + output_tokens` from each Claude response (both stream-json and CLI formats)
  - Blocks further calls once the hourly token budget is exhausted
  - Counters reset together on the hour
- Automatic hourly reset with countdown display
- Call and token tracking persists across script restarts

### Modern CLI Configuration (Phase 1.1)

Ralph uses modern Claude Code CLI flags for structured communication:

**Configuration Variables:**
```bash
CLAUDE_CODE_CMD="claude"              # Claude Code CLI command (configurable via .ralphrc, Issue #97)
CLAUDE_OUTPUT_FORMAT="json"           # Output format: json (default) or text
CLAUDE_ALLOWED_TOOLS="Write,Read,Edit,Bash(git add *),Bash(git commit *),...,Bash(npm *),Bash(pytest)"  # Allowed tool permissions (see File Protection)
CLAUDE_USE_CONTINUE=true              # Enable session continuity
CLAUDE_MIN_VERSION="2.0.76"           # Minimum Claude CLI version
CLAUDE_AUTO_UPDATE=true               # Auto-update Claude CLI at startup (set false for air-gapped environments)
CLAUDE_MODEL=""                       # Model override (e.g. claude-sonnet-4-6); empty = CLI default (Issue #228)
CLAUDE_EFFORT=""                      # Effort level override (e.g. high, low); empty = CLI default (Issue #228)
ENABLE_NOTIFICATIONS=false            # Desktop notifications (Issue #22); set true or use --notify / -n flag
ENABLE_BACKUP=false                   # Automatic git backup branches (Issue #23); set true or use --backup / -b flag
```

**Auto-Update Configuration:**
- `CLAUDE_AUTO_UPDATE` controls whether Ralph checks npm registry and attempts `npm update -g` at startup
- **Local workstation / home server**: Keep `true` (default) — CLI updates include bug fixes and new features that improve Ralph's effectiveness. The 200-500ms startup overhead is negligible for loops that run hours
- **Docker container**: Set `false` in `.ralphrc` — container is ephemeral and version is pinned at image build time. The npm registry query and potential update are pure overhead
- **Air-gapped environment**: Set `false` — npm registry is unreachable, the check will timeout and log a warning
- Update failure is non-blocking: Ralph logs a warning and continues the loop normally

**Claude Code CLI Command (Issue #97):**
- `CLAUDE_CODE_CMD` defaults to `"claude"` (global install)
- Configurable via `.ralphrc` for alternative installations (e.g., `"npx @anthropic-ai/claude-code"`)
- Auto-detected during `ralph-enable` and `ralph-setup` (prefers `claude` if available, falls back to npx)
- Validated at startup with `validate_claude_command()` — displays clear error with installation instructions if not found
- After validation, `check_claude_version()` verifies minimum version compatibility and `check_claude_updates()` queries npm registry for latest version with auto-update attempt (Issue #190)
- Both functions use `compare_semver()` for proper major→minor→patch sequential comparison (safe for any patch number, unlike integer arithmetic)
- Environment variable `CLAUDE_CODE_CMD` takes precedence over `.ralphrc`

**Model and Effort Overrides (Issue #228):**
- `CLAUDE_MODEL` sets the `--model` flag on every Claude invocation (e.g., `CLAUDE_MODEL=claude-sonnet-4-6`). Leave empty to use the CLI's default model.
- `CLAUDE_EFFORT` sets the `--effort` flag (e.g., `CLAUDE_EFFORT=high` or `CLAUDE_EFFORT=low`). Leave empty to use the CLI's default.
- Both variables can be set in `.ralphrc` or as environment variables. The environment variable takes precedence over `.ralphrc`.

**CLI Options:**
- `--output-format json|text` - Set Claude output format (default: json). Note: `--live` mode requires JSON and will auto-switch from text to json.
- `--allowed-tools "Write,Read,Bash(git *)"` - Restrict allowed tools
- `--no-continue` - Disable session continuity, start fresh each loop

**Loop Context:**
Each loop iteration injects context via `build_loop_context()`:
- Current loop number
- Remaining tasks from fix_plan.md
- Circuit breaker state (if not CLOSED)
- Previous loop work summary
- Corrective guidance if previous loop detected questions (Issue #190)

**Session Continuity:**
- Sessions are preserved in `.ralph/.claude_session_id`
- Use `--continue` flag to maintain context across loops
- Disable with `--no-continue` for isolated iterations

### Intelligent Exit Detection
The loop uses a dual-condition check to prevent premature exits during productive iterations:

**Exit requires BOTH conditions:**
1. `recent_completion_indicators >= 2` (heuristic-based detection from natural language patterns)
2. Claude's explicit `EXIT_SIGNAL: true` in the RALPH_STATUS block

The `EXIT_SIGNAL` value is read from `.ralph/.response_analysis` (at `.analysis.exit_signal`) which is populated by `response_analyzer.sh` from Claude's RALPH_STATUS output block.

**Other exit conditions (checked before completion indicators):**
- Multiple consecutive "done" signals from Claude Code (`done_signals >= 2`)
- Too many test-only loops indicating feature completeness (`test_loops >= 3`)
- All items in .ralph/fix_plan.md marked as completed

**Example behavior when EXIT_SIGNAL is false:**
```
Loop 5: Claude outputs "Phase complete, moving to next feature"
        → completion_indicators: 3 (high confidence from patterns)
        → EXIT_SIGNAL: fals
... [TRUNCATED]
```

### File: CONTRIBUTING.md
```md
# Contributing to Ralph for Claude Code

Thank you for your interest in contributing to Ralph! This guide will help you get started and ensure your contributions follow our established patterns and quality standards.

**Every contribution matters** - from fixing typos to implementing major features. We appreciate your help in making Ralph better!

## Table of Contents

1. [Getting Started](#getting-started)
2. [Development Workflow](#development-workflow)
3. [Code Style Guidelines](#code-style-guidelines)
4. [Testing Requirements](#testing-requirements)
5. [Pull Request Process](#pull-request-process)
6. [Code Review Guidelines](#code-review-guidelines)
7. [Quality Standards](#quality-standards)
8. [Community Guidelines](#community-guidelines)

---

## Getting Started

### Prerequisites

Before contributing, ensure you have the following installed:

- **Bash 4.0+** - For script execution
- **jq** - JSON processing (required)
- **git** - Version control (required)
- **tmux** - Terminal multiplexer (recommended)
- **Node.js 18+** - For running tests via npm

### Clone the Repository

```bash
# Fork the repository on GitHub first, then clone your fork
git clone https://github.com/YOUR_USERNAME/ralph-claude-code.git
cd ralph-claude-code
```

### Install Dependencies

```bash
# Install BATS testing framework and dependencies
npm install

# Verify BATS is available
./node_modules/.bin/bats --version

# Optional: Install Ralph globally for testing
./install.sh
```

### Verify Your Setup

```bash
# Run the test suite to ensure everything works
npm test

# You should see output like:
# ✓ 276 tests passed (100% pass rate)
```

### Project Structure

```
ralph-claude-code/
├── ralph_loop.sh        # Main loop script
├── ralph_monitor.sh     # Live monitoring dashboard
├── setup.sh             # Project initialization
├── ralph_import.sh      # PRD import tool
├── install.sh           # Global installation script
├── lib/                 # Modular library components
│   ├── circuit_breaker.sh
│   ├── response_analyzer.sh
│   └── date_utils.sh
├── templates/           # Project templates
├── tests/               # Test suite
│   ├── unit/            # Unit tests
│   ├── integration/     # Integration tests
│   ├── e2e/             # End-to-end tests
│   └── helpers/         # Test utilities
└── docs/                # Documentation
```

---

## Development Workflow

### Branch Naming Conventions

Always create a feature branch - never work directly on `main`:

| Branch Type | Format | Example |
|-------------|--------|---------|
| New features | `feature/<feature-name>` | `feature/log-rotation` |
| Bug fixes | `fix/<issue-name>` | `fix/rate-limit-reset` |
| Documentation | `docs/<doc-update>` | `docs/api-reference` |
| Tests | `test/<test-area>` | `test/circuit-breaker` |
| Refactoring | `refactor/<area>` | `refactor/response-analyzer` |

```bash
# Create a new feature branch
git checkout -b feature/my-awesome-feature
```

### Commit Message Format

We use [Conventional Commits](https://www.conventionalcommits.org/) for clear, structured commit history:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types:**

| Type | Description | Example |
|------|-------------|---------|
| `feat` | New feature | `feat(loop): add dry-run mode` |
| `fix` | Bug fix | `fix(monitor): correct refresh rate` |
| `docs` | Documentation only | `docs(readme): update installation steps` |
| `test` | Adding/updating tests | `test(setup): add template validation tests` |
| `refactor` | Code change (no features/fixes) | `refactor(analyzer): simplify error detection` |
| `chore` | Maintenance tasks | `chore(deps): update bats-assert` |

**Examples from Recent Commits:**

```bash
# Feature addition
feat(import): add JSON output format support

# Bug fix with scope
fix(loop): replace non-existent --prompt-file with -p flag

# Documentation update
docs(status): update IMPLEMENTATION_STATUS.md with phased structure

# Test addition
test(cli): add 27 comprehensive CLI parsing tests
```

**Writing Good Commit Messages:**

- Use imperative mood ("add" not "added")
- Explain WHAT changed and WHY (not HOW)
- Keep the subject line under 72 characters
- Reference issues when applicable (`fixes #123`)

### Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Contribution Workflow                            │
└─────────────────────────────────────────────────────────────────────┘

  ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
  │  1. Fork │────>│ 2. Clone │────>│ 3. Branch│────>│ 4. Code  │
  └──────────┘     └──────────┘     └──────────┘     └──────────┘
                                                           │
                                                           v
  ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
  │ 8. Merge │<────│  7. PR   │<────│ 6. Push  │<────│ 5. Test  │
  └──────────┘     │ Approved │     └──────────┘     │ (100%)   │
                   └──────────┘                      └──────────┘
                        ^
                        │
                   ┌──────────┐
                   │  CI/CD   │
                   │  Passes  │
                   └──────────┘
```

---

## Code Style Guidelines

### Bash Best Practices

Ralph follows consistent bash conventions across all scripts:

**File Structure:**

```bash
#!/bin/bash
# Script description
# Purpose and usage notes

# Source dependencies
source "$(dirname "${BASH_SOURCE[0]}")/lib/date_utils.sh"

# Configuration constants (UPPER_CASE)
MAX_CALLS_PER_HOUR=100
CB_NO_PROGRESS_THRESHOLD=3
STATUS_FILE="status.json"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Helper functions (snake_case)
helper_function() {
    local param1=$1
    local param2=$2
    # Implementation
}

# Main logic
main() {
    # Entry point
}

# Export functions for reuse
export -f helper_function

# Execute main if run directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
```

**Naming Conventions:**

| Element | Convention | Example |
|---------|------------|---------|
| Functions | snake_case | `get_circuit_state()` |
| Local variables | snake_case | `local loop_count=0` |
| Constants | UPPER_SNAKE_CASE | `MAX_CALLS_PER_HOUR` |
| File names | snake_case.sh | `circuit_breaker.sh` |
| Control files | snake_case.md | `fix_plan.md`, `AGENT.md` |

**Function Documentation:**

```bash
# Get current circuit breaker state
# Returns the state as a string: CLOSED, HALF_OPEN, or OPEN
# Falls back to CLOSED if state file doesn't exist
get_circuit_state() {
    if [[ ! -f "$CB_STATE_FILE" ]]; then
        echo "$CB_STATE_CLOSED"
        return
    fi

    jq -r '.state' "$CB_STATE_FILE" 2>/dev/null || echo "$CB_STATE_CLOSED"
}
```

**Error Handling:**

```bash
# Always validate inputs
if [[ -z "$1" ]]; then
    echo -e "${RED}Error: Missing required argument${NC}" >&2
    exit 1
fi

# Use proper exit codes
# 0 = success, 1 = general error, 2 = invalid usage
```

**Cross-Platform Compatibility:**

```bash
# Use portable date commands
if command -v gdate &> /dev/null; then
    DATE_CMD="gdate"  # macOS with coreutils
else
    DATE_CMD="date"   # Linux
fi
```

**JSON State Management:**

```bash
# Always validate JSON before parsing
if ! jq '.' "$STATE_FILE" > /dev/null 2>&1; then
    echo "Error: Invalid JSON in state file"
    return 1
fi

# Use jq for safe parsing
local state=$(jq -r '.state' "$STATE_FILE" 2>/dev/null || echo "CLOSED")
```

---

## Testing Requirements

### Mandatory Testing Standards

**All new features must include tests. This is non-negotiable.**

| Requirement | Standard | Enforcement |
|-------------|----------|-------------|
| Test Pass Rate | 100% | **Mandatory** - CI blocks merge |
| Test Coverage | 85% | Aspirational - informational only |

> **Note on Coverage:** Bash code coverage with kcov cannot trace subprocess executions. Test pass rate is the enforced quality gate, not coverage percentage.

### Test Organization

```
tests/
├── unit/                       # Fast, isolated tests
│   ├── test_cli_parsing.bats   # CLI argument tests
│   ├── test_json_parsing.bats  # JSON output parsing
│   ├── test_exit_detection.bats
│   ├── test_rate_limiting.bats
│   ├── test_session_continuity.bats
│   └── test_cli_modern.bats
├── integration/                # Multi-component tests
│   ├── test_loop_execution.bats
│   ├── test_edge_cases.bats
│   ├── test_installation.bats
│   ├── test_project_setup.bats
│   └── test_prd_import.bats
├── e2e/                        # End-to-end workflows
└── helpers/
    └── test_helper.bash        # Shared test utilities
```

### Running Tests

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `npm test` | Run all tests | Before committing, before PR |
| `npm run test:unit` | Unit tests only | During development |
| `npm run test:integration` | Integration tests only | Testing interactions |
| `bats tests/unit/test_file.bats` | Single test file | Debugging specific tests |

### Writing Tests

**Test Structure:**

```bash
#!/usr/bin/env bats
# Unit Tests for Feature X

load '../helpers/test_helper'

# Setup runs before each test
setup() {
    source "$(dirname "$BATS_TEST_FILENAME")/../helpers/test_helper.bash"

    # Create isolated test environment
    export TEST_TEMP_DIR="$(mktemp -d /tmp/ralph-test.XXXXXX)"
    cd "$TEST_TEMP_DIR"

    # Initialize test state
    echo "0" > ".call_count"
}

# Teardown runs after each test
teardown() {
    cd /
    rm -rf "$TEST_TEMP_DIR"
}

# Test: Descriptive name explaining what's being tested
@test "can_make_call returns success when under limit" {
    echo "50" > ".call_count"
    export MAX_CALLS_PER_HOUR=100

    run can_make_call
    assert_success
}

# Test: Failure case
@test "can_make_call returns failure when at limit" {
    echo "100" > ".call_count"
    export MAX_CALLS_PER_HOUR=100

    run can_make_call
    assert_failure
}
```

**Test Best Practices:**

1. **Test both success and failure cases**
2. **Use descriptive test names** that explain the scenario
3. **Isolate tests** - each test should be independent
4. **Mock external dependencies** (Claude CLI, tmux, etc.)
5. **Test edge cases** (empty files, invalid input, boundary values)
6. **Add comments** for complex test scenarios

**Available Test Helpers:**

```bash
# From tests/helpers/test_helper.bash

assert_success      # Check command succeeded (exit 0)
assert_failure      # Check command failed (exit != 0)
assert_equal        # Compare two values
assert_output       # Check command output
assert_file_exists  # Verify file exists
assert_dir_exists   # Verify directory exists
strip_colors        # Remove ANSI color codes
create_mock_prompt  # Create test PROMPT.md
create_mock_fix_plan # Create test fix_plan.md
create_mock_status  # Create test status.json
```

---

## Pull Request Process

### Before Creating a PR

Run through this checklist:

- [ ] All tests pass locally (`npm test`)
- [ ] New code includes appropriate tests
- [ ] Commits follow conventional format
- [ ] Documentation updated if needed
- [ ] No debug code or console.log statements
- [ ] No secrets or credentials committed

### Creating the PR

1. **Push your branch:**
   ```bash
   git push origin feature/my-feature
   ```

2. **Open a Pull Request** on GitHub with:

**PR Title:** Follow conventional commit format
```
feat(loop): add dry-run mode for testing
```

**PR Description Template:**
```markdown
## Summary

Brief description of what this PR does (1-3 bullet points).

- Adds dry-run mode to preview loop execution
- Includes new CLI flag `--dry-run`
- Logs actions without making actual changes

## Test Plan

- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing completed

## Related Issues

Fixes #123
Related to #456

## Screenshots (if applicable)

[Add screenshots for UI/output changes]

## Breaking Changes

[List any breaking changes, or "None"]
```

### After PR Creation

1. **Wait for CI/CD** - GitHub Actions will run all tests
2. **Address review feedback** - Make requested changes promptly
3. **Keep PR updated** - Rebase if main branch has changed

---

## Code Review Guidelines

### For Contributors

**Responding to Feedback:**

- Thank reviewers for their time
- Ask questions if requirements are unclear
- Make requested changes promptly
- Update PR description as changes evolve
- Don't take feedback personally - it's about the code

**If You Disagree:**

- Explain your reasoning clearly
- Provide context for your decisions
- Be open to alternative approaches
- Defer to maintainer judgment when in doubt

### For Reviewers

**What to Check:**

| Area | Questions to Ask |
|------|------------------|
| **Correctness** | Does the code do what it claims? |
| **Tests** | Are tests comprehensive? Do they pass? |
| **Style** | Does it follow bash conventions? |
| **Documentation** | Are comments and docs updated? |
| **Breaking Changes** | Will this affect existing users? |
| **Performance** | Any obvious performance issues? |

**Review Best Practices:**

1. **Be constructive** - Focus on improvements, not criticism
2. **Be specific** - Point to exact lines when possible
3. **Explain why** - Help contributors learn
4. **Acknowledge good work** - Note well-written code
5. **Approve when ready** - Don't hold PRs hostage

---

## Quality Standards

### Quality Gates

All PRs must pass these automated checks:

| Gate | Requirement | Enforcement |
|------|-------------|-------------|
| Unit Tests | 100% pass | **Blocks merge** |
| Integration Tests | 100% pass | **Blocks merge** |
| Coverage | 85% | Informational only |
| Conventional Commits | Required | Manual review |
| Documentation | Updated | Manual review |

### Documentation Standards

**When to Update Documentation:**

- Adding new CLI flags → Update README.md, CLAUDE.md
- Adding new features → Update README.md "Features" section
- Changing behavior → Update relevant docs
- Adding new patterns → Update CLAUDE.md

**Keep in Sync:**

1. **CLAUDE.md** - Technical specifications, quality standards
2. **README.md** - User-facing documentation, installation
3. **Templates** - Keep template files current
4. **Inline comments** - Update when code changes

### Feature Completion Checklist

Before marking any feature complete:

- [ ] All tests pass (100% pass rate)
- [ ] Script functionality manually tested
- [ ] Commits follow conventional format
- [ ] All commits pushed to remote
- [ ] CI/CD pipeline passes
- [ ] CLAUDE.md updated (if new patterns)
- [ ] README.md updated (if user-facing)
- [ ] Breaking changes documented
- [ ] Installation verified (if applicable)

---

## Community Guidelines

### Priority Contribution Areas

**High Priority - Help Needed!**

1. **Test Implementation** - Expand test coverage
   - See [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md) for specifications

2. **Feature
... [TRUNCATED]
```

### File: create_files.sh
```sh
#!/bin/bash

# Quick script to create all Ralph files in your GitHub repo
set -e

echo "🚀 Creating Ralph for Claude Code repository structure..."

# Create directories
# Note: Project structure uses .ralph/ subfolder for Ralph-specific files
# src/ stays at root for compatibility with existing tooling
mkdir -p {src,templates/specs}

# Create main scripts
cat > ralph_loop.sh << 'EOF'
#!/bin/bash

# Claude Code Ralph Loop with Rate Limiting and Documentation
# Adaptation of the Ralph technique for Claude Code with usage management

set -e  # Exit on any error

# Configuration - Ralph files live in .ralph/ subfolder
RALPH_DIR="${RALPH_DIR:-.ralph}"
PROMPT_FILE="$RALPH_DIR/PROMPT.md"
LOG_DIR="$RALPH_DIR/logs"
DOCS_DIR="$RALPH_DIR/docs/generated"
STATUS_FILE="$RALPH_DIR/status.json"
CLAUDE_CODE_CMD="npx @anthropic/claude-code"
MAX_CALLS_PER_HOUR=100  # Adjust based on your plan
SLEEP_DURATION=3600     # 1 hour in seconds
CALL_COUNT_FILE="$RALPH_DIR/.call_count"
TIMESTAMP_FILE="$RALPH_DIR/.last_reset"

# Exit detection configuration
EXIT_SIGNALS_FILE="$RALPH_DIR/.exit_signals"
MAX_CONSECUTIVE_TEST_LOOPS=3
MAX_CONSECUTIVE_DONE_SIGNALS=2
TEST_PERCENTAGE_THRESHOLD=30  # If more than 30% of recent loops are test-only, flag it

# Colors for terminal output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

# Initialize directories
mkdir -p "$LOG_DIR" "$DOCS_DIR"

# Initialize call tracking
init_call_tracking() {
    local current_hour=$(date +%Y%m%d%H)
    local last_reset_hour=""
    
    if [[ -f "$TIMESTAMP_FILE" ]]; then
        last_reset_hour=$(cat "$TIMESTAMP_FILE")
    fi
    
    # Reset counter if it's a new hour
    if [[ "$current_hour" != "$last_reset_hour" ]]; then
        echo "0" > "$CALL_COUNT_FILE"
        echo "$current_hour" > "$TIMESTAMP_FILE"
        log_status "INFO" "Call counter reset for new hour: $current_hour"
    fi
    
    # Initialize exit signals tracking if it doesn't exist
    if [[ ! -f "$EXIT_SIGNALS_FILE" ]]; then
        echo '{"test_only_loops": [], "done_signals": [], "completion_indicators": []}' > "$EXIT_SIGNALS_FILE"
    fi
}

# Log function with timestamps and colors
log_status() {
    local level=$1
    local message=$2
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    local color=""
    
    case $level in
        "INFO")  color=$BLUE ;;
        "WARN")  color=$YELLOW ;;
        "ERROR") color=$RED ;;
        "SUCCESS") color=$GREEN ;;
        "LOOP") color=$PURPLE ;;
    esac
    
    echo -e "${color}[$timestamp] [$level] $message${NC}"
    echo "[$timestamp] [$level] $message" >> "$LOG_DIR/ralph.log"
}

# Update status JSON for external monitoring
update_status() {
    local loop_count=$1
    local calls_made=$2
    local last_action=$3
    local status=$4
    local exit_reason=${5:-""}
    
    cat > "$STATUS_FILE" << STATUSEOF
{
    "timestamp": "$(date -Iseconds)",
    "loop_count": $loop_count,
    "calls_made_this_hour": $calls_made,
    "max_calls_per_hour": $MAX_CALLS_PER_HOUR,
    "last_action": "$last_action",
    "status": "$status",
    "exit_reason": "$exit_reason",
    "next_reset": "$(date -d '+1 hour' -Iseconds | cut -d'T' -f2 | cut -d'+' -f1)"
}
STATUSEOF
}

# Check if we can make another call
can_make_call() {
    local calls_made=0
    if [[ -f "$CALL_COUNT_FILE" ]]; then
        calls_made=$(cat "$CALL_COUNT_FILE")
    fi
    
    if [[ $calls_made -ge $MAX_CALLS_PER_HOUR ]]; then
        return 1  # Cannot make call
    else
        return 0  # Can make call
    fi
}

# Increment call counter
increment_call_counter() {
    local calls_made=0
    if [[ -f "$CALL_COUNT_FILE" ]]; then
        calls_made=$(cat "$CALL_COUNT_FILE")
    fi
    
    ((calls_made++))
    echo "$calls_made" > "$CALL_COUNT_FILE"
    echo "$calls_made"
}

# Wait for rate limit reset with countdown
wait_for_reset() {
    local calls_made=$(cat "$CALL_COUNT_FILE" 2>/dev/null || echo "0")
    log_status "WARN" "Rate limit reached ($calls_made/$MAX_CALLS_PER_HOUR). Waiting for reset..."
    
    # Calculate time until next hour
    local current_minute=$(date +%M)
    local current_second=$(date +%S)
    local wait_time=$(((60 - current_minute - 1) * 60 + (60 - current_second)))
    
    log_status "INFO" "Sleeping for $wait_time seconds until next hour..."
    
    # Countdown display
    while [[ $wait_time -gt 0 ]]; do
        local hours=$((wait_time / 3600))
        local minutes=$(((wait_time % 3600) / 60))
        local seconds=$((wait_time % 60))
        
        printf "\r${YELLOW}Time until reset: %02d:%02d:%02d${NC}" $hours $minutes $seconds
        sleep 1
        ((wait_time--))
    done
    printf "\n"
    
    # Reset counter
    echo "0" > "$CALL_COUNT_FILE"
    echo "$(date +%Y%m%d%H)" > "$TIMESTAMP_FILE"
    log_status "SUCCESS" "Rate limit reset! Ready for new calls."
}

# Check if we should gracefully exit
should_exit_gracefully() {
    if [[ ! -f "$EXIT_SIGNALS_FILE" ]]; then
        return 1  # Don't exit, file doesn't exist
    fi
    
    local signals=$(cat "$EXIT_SIGNALS_FILE")
    
    # Count recent signals (last 5 loops)
    local recent_test_loops=$(echo "$signals" | jq '.test_only_loops | length')
    local recent_done_signals=$(echo "$signals" | jq '.done_signals | length')
    local recent_completion_indicators=$(echo "$signals" | jq '.completion_indicators | length')
    
    # Check for exit conditions
    
    # 1. Too many consecutive test-only loops
    if [[ $recent_test_loops -ge $MAX_CONSECUTIVE_TEST_LOOPS ]]; then
        log_status "WARN" "Exit condition: Too many test-focused loops ($recent_test_loops >= $MAX_CONSECUTIVE_TEST_LOOPS)"
        echo "test_saturation"
        return 0
    fi
    
    # 2. Multiple "done" signals
    if [[ $recent_done_signals -ge $MAX_CONSECUTIVE_DONE_SIGNALS ]]; then
        log_status "WARN" "Exit condition: Multiple completion signals ($recent_done_signals >= $MAX_CONSECUTIVE_DONE_SIGNALS)"
        echo "completion_signals"
        return 0
    fi
    
    # 3. Strong completion indicators
    if [[ $recent_completion_indicators -ge 2 ]]; then
        log_status "WARN" "Exit condition: Strong completion indicators ($recent_completion_indicators)"
        echo "project_complete"
        return 0
    fi
    
    # 4. Check fix_plan.md for completion
    # Fix #144: Only match valid markdown checkboxes, not date entries like [2026-01-29]
    # Valid patterns: "- [ ]" (uncompleted) and "- [x]" or "- [X]" (completed)
    if [[ -f "$RALPH_DIR/fix_plan.md" ]]; then
        local uncompleted_items=$(grep -cE "^[[:space:]]*- \[ \]" "$RALPH_DIR/fix_plan.md" 2>/dev/null || echo "0")
        local completed_items=$(grep -cE "^[[:space:]]*- \[[xX]\]" "$RALPH_DIR/fix_plan.md" 2>/dev/null || echo "0")
        local total_items=$((uncompleted_items + completed_items))

        if [[ $total_items -gt 0 ]] && [[ $completed_items -eq $total_items ]]; then
            log_status "WARN" "Exit condition: All fix_plan.md items completed ($completed_items/$total_items)"
            echo "plan_complete"
            return 0
        fi
    fi
    
    return 1  # Don't exit
}

# Main execution function
execute_claude_code() {
    local calls_made=$(increment_call_counter)
    local timestamp=$(date '+%Y-%m-%d_%H-%M-%S')
    local output_file="$LOG_DIR/claude_output_${timestamp}.log"
    local loop_count=$1
    
    log_status "LOOP" "Executing Claude Code (Call $calls_made/$MAX_CALLS_PER_HOUR)"
    
    # Execute Claude Code with the prompt
    if $CLAUDE_CODE_CMD < "$PROMPT_FILE" > "$output_file" 2>&1; then
        log_status "SUCCESS" "Claude Code execution completed successfully"
        
        # Extract key information from output if possible
        if grep -q "error\|Error\|ERROR" "$output_file"; then
            log_status "WARN" "Errors detected in output, check: $output_file"
        fi
        
        return 0
    else
        log_status "ERROR" "Claude Code execution failed, check: $output_file"
        return 1
    fi
}

# Cleanup function
cleanup() {
    log_status "INFO" "Ralph loop interrupted. Cleaning up..."
    update_status "$loop_count" "$(cat "$CALL_COUNT_FILE" 2>/dev/null || echo "0")" "interrupted" "stopped"
    exit 0
}

# Set up signal handlers
trap cleanup SIGINT SIGTERM

# Main loop
main() {
    local loop_count=0
    
    log_status "SUCCESS" "🚀 Ralph loop starting with Claude Code"
    log_status "INFO" "Max calls per hour: $MAX_CALLS_PER_HOUR"
    log_status "INFO" "Logs: $LOG_DIR/ | Docs: $DOCS_DIR/ | Status: $STATUS_FILE"
    
    # Check if prompt file exists
    if [[ ! -f "$PROMPT_FILE" ]]; then
        log_status "ERROR" "Prompt file '$PROMPT_FILE' not found!"
        exit 1
    fi
    
    while true; do
        ((loop_count++))
        init_call_tracking
        
        log_status "LOOP" "=== Starting Loop #$loop_count ==="
        
        # Check rate limits
        if ! can_make_call; then
            wait_for_reset
            continue
        fi
        
        # Check for graceful exit conditions
        local exit_reason=$(should_exit_gracefully)
        if [[ $? -eq 0 ]]; then
            log_status "SUCCESS" "🏁 Graceful exit triggered: $exit_reason"
            update_status "$loop_count" "$(cat "$CALL_COUNT_FILE")" "graceful_exit" "completed" "$exit_reason"
            
            log_status "SUCCESS" "🎉 Ralph has completed the project! Final stats:"
            log_status "INFO" "  - Total loops: $loop_count"
            log_status "INFO" "  - API calls used: $(cat "$CALL_COUNT_FILE")"
            log_status "INFO" "  - Exit reason: $exit_reason"
            
            break
        fi
        
        # Update status
        local calls_made=$(cat "$CALL_COUNT_FILE" 2>/dev/null || echo "0")
        update_status "$loop_count" "$calls_made" "executing" "running"
        
        # Execute Claude Code
        if execute_claude_code "$loop_count"; then
            update_status "$loop_count" "$(cat "$CALL_COUNT_FILE")" "completed" "success"
            
            # Brief pause between successful executions
            sleep 5
        else
            update_status "$loop_count" "$(cat "$CALL_COUNT_FILE")" "failed" "error"
            log_status "WARN" "Execution failed, waiting 30 seconds before retry..."
            sleep 30
        fi
        
        log_status "LOOP" "=== Completed Loop #$loop_count ==="
    done
}

# Help function
show_help() {
    cat << HELPEOF
Ralph Loop for Claude Code

Usage: $0 [OPTIONS]

Options:
    -h, --help          Show this help message
    -c, --calls NUM     Set max calls per hour (default: $MAX_CALLS_PER_HOUR)
    -p, --prompt FILE   Set prompt file (default: $PROMPT_FILE)
    -s, --status        Show current status and exit

Files created:
    - $LOG_DIR/: All execution logs
    - $DOCS_DIR/: Generated documentation
    - $STATUS_FILE: Current status (JSON)

Example:
    $0 --calls 50 --prompt my_prompt.md

HELPEOF
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            show_help
            exit 0
            ;;
        -c|--calls)
            MAX_CALLS_PER_HOUR="$2"
            shift 2
            ;;
        -p|--prompt)
            PROMPT_FILE="$2"
            shift 2
            ;;
        -s|--status)
            if [[ -f "$STATUS_FILE" ]]; then
                echo "Current Status:"
                cat "$STATUS_FILE" | jq . 2>/dev/null || cat "$STATUS_FILE"
            else
                echo "No status file found. Ralph may not be running."
            fi
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            show_help
            exit 1
            ;;
    esac
done

# Start the main loop
main
EOF

# Create monitor script (simplified for brevity)
cat > ralph_monitor.sh << 'EOF'
#!/bin/bash

# Ralph Status Monitor - Live terminal dashboard for the Ralph loop
set -e

RALPH_DIR="${RALPH_DIR:-.ralph}"
STATUS_FILE="$RALPH_DIR/status.json"
LOG_FILE="$RALPH_DIR/logs/ralph.log"
REFRESH_INTERVAL=2

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m'

# Clear screen and hide cursor
clear_screen() {
    clear
    printf '\033[?25l'  # Hide cursor
}

# Show cursor on exit
show_cursor() {
    printf '\033[?25h'  # Show cursor
}

# Cleanup function
cleanup() {
    show_cursor
    echo
    echo "Monitor stopped."
    exit 0
}

# Set up signal handlers
trap cleanup SIGINT SIGTERM EXIT

# Main display function
display_status() {
    clear_screen
    
    # Header
    echo -e "${WHITE}╔════════════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${WHITE}║                           🤖 RALPH MONITOR                              ║${NC}"
    echo -e "${WHITE}║                        Live Status Dashboard                           ║${NC}"
    echo -e "${WHITE}╚════════════════════════════════════════════════════════════════════════╝${NC}"
    echo
    
    # Status section
    if [[ -f "$STATUS_FILE" ]]; then
        # Parse JSON status
        local status_data=$(cat "$STATUS_FILE")
        local loop_count=$(echo "$status_data" | jq -r '.loop_count // "0"' 2>/dev/null || echo "0")
        local calls_made=$(echo "$status_data" | jq -r '.calls_made_this_hour // "0"' 2>/dev/null || echo "0")
        local max_calls=$(echo "$status_data" | jq -r '.max_calls_per_hour // "100"' 2>/dev/null || echo "100")
        local status=$(echo "$status_data" | jq -r '.status // "unknown"' 2>/dev/null || echo "unknown")
        
        echo -e "${CYAN}┌─ Current Status ────────────────────────────────────────────────────────┐${NC}"
        echo -e "${CYAN}│${NC} Loop Count:     ${WHITE}#$loop_count${NC}"
        echo -e "${CYAN}│${NC} Status:         ${GREEN}$status${NC}"
        echo -e "${CYAN}│${NC} API Calls:      $calls_made/$max_calls"
        echo -e "${CYAN}└─────────────────────────────────────────────────────────────────────────┘${NC}"
        echo
        
    else
        echo -e "${RED}┌─ Status ────────────────────────────────────────────────────────────────┐${NC}"
        echo -e "${RED}│${NC} Status file not found. Ralph may not be running."
        echo -e "${RED}└─────────────────────────────────────────────────────────────────────────┘${NC}"
        echo
    fi
    
    # Recent logs
    echo -e "${BLUE}┌─ Recent Activity ───────────────────────────────────────────────────────┐${NC}"
    if [[ -f "$LOG_FILE" ]]; then
        tail -n 8 "$LOG_FILE" | while IFS= read -r line; do
            echo -e "${BLUE}│${NC} $line"
        done
    else
        echo -e "${BLUE}│${NC} No log file found"
    fi
    echo -e "${BLUE}└─────────────────────────────────────────────────────────────────────────┘${NC}"
    
    # Footer
    echo
    echo -e "${YELLOW}Controls: Ctrl+C to exit | Refreshes every ${REFRESH_INTERVAL}s | $(date '+%H:%M:%S')${NC}"
}

# Main monitor loop
main() {

... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
