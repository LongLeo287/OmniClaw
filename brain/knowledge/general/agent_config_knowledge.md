# Knowledge Dump for agent_config

## File: DEEP_KNOWLEDGE.md
```
# Deep Matrix Profile: FETCHED_agent-config_144305

# DEEP_KNOWLEDGE.md: Skill Framework Architecture Analysis

## 🧠 Overview and Architectural Pattern

This repository implements a robust, structured framework for managing, validating, and distributing AI coding agent capabilities (Skills). The architecture follows a **Command-Line Interface (CLI) Pattern** combined with a **Builder/Factory Pattern** for skill creation and a **Validation Pipeline Pattern** for quality assurance.

The system is designed around the concept of a "Skill," which is not merely a document but a structured, self-contained directory containing documentation (`SKILL.md`), executable code (`scripts/`), and reference materials.

### Core Architectural Components:

1.  **Skill Scaffolding (`init_skill.py`):** Acts as the Builder, providing a standardized template to ensure all new skills adhere to the required structure and documentation standards.
2.  **Validation Layer (`quick_validate.py`):** Implements the core quality gate, ensuring that the skill metadata (`SKILL.md`) meets strict technical and semantic constraints before packaging.
3.  **Packaging Engine (`package_skill.py`):** Acts as the Distributor, taking the validated directory structure and serializing it into a portable, compressed format (`.skill` zip archive).

---

## ⚙️ Deep Dive: Mechanisms and Algorithms

### 1. The Skill Initialization Mechanism (`init_skill.py`)

**Mechanism:** Template Substitution and Directory Creation.
**Purpose:** To enforce consistency and reduce boilerplate for skill authors.

The script utilizes Python's string formatting capabilities (`{skill_name}`, `{skill_title}`) to populate a complex, multi-section Markdown template (`SKILL_TEMPLATE`).

**Key Functionality:**
*   **Scaffolding:** Creates the necessary directory structure (`skills/public/my-new-skill/`).
*   **Guidance Integration:** The template itself acts as meta-documentation, guiding the user on best practices (Workflow-Based vs. Task-Based structure, required sections like `scripts/`).
*   **Input Handling:** Accepts command-line arguments for both the desired skill name and the target output path, ensuring the skill is placed in the correct organizational context.

### 2. The Validation Pipeline (`quick_validate.py`)

**Mechanism:** Multi-Stage Constraint Validation (Regex, YAML Parsing, Schema Checking).
**Purpose:** To guarantee that the skill metadata is machine-readable, compliant with naming conventions, and structurally sound. This is the most critical quality gate.

The validation process is highly sequential and robust:

#### A. YAML Frontmatter Extraction and Parsing
1.  **Detection:** Uses Regular Expressions (`re.match(r'^---\n(.*?)\n---', content, re.DOTALL)`) to reliably isolate the YAML block between the `---` delimiters.
2.  **Parsing:** Employs `yaml.safe_load()` to deserialize the raw YAML string into a Python dictionary (`frontmatter`).
3.  **Type Checking:** Verifies that the resulting object is indeed a dictionary, preventing runtime errors from malformed YAML.

#### B. Schema and Constraint Validation
The script enforces multiple layers of constraints:

*   **Presence Check:** Verifies the existence of mandatory fields (`name`, `description`).
*   **Data Type Check:** Ensures fields like `name` are strings.
*   **Naming Convention Algorithm (Regex):**
    *   **Pattern:** `r'^[a-z0-9-]+$'`
    *   **Constraint:** Enforces strict hyphen-case (lowercase letters, digits, and hyphens).
    *   **Boundary Checks:** Explicitly checks for leading/trailing hyphens or consecutive hyphens (`--`) to maintain clean, URL-safe identifiers.
*   **Content Filtering:** Checks the `description` field for forbidden characters (e.g., `<` or `>`) to prevent potential Markdown or rendering issues.
*   **Schema Enforcement:** Compares the keys found in the frontmatter against a predefined `ALLOWED_PROPERTIES` set, rejecting unexpected keys to maintain a stable API contract.

### 3. The Packaging Engine (`package_skill.py`)

**Mechanism:** File System Traversal, Relative Path Calculation, and ZIP Compression.
**Purpose:** To create a single, self-contained, and portable artifact (`.skill` file) from the validated directory structure.

The packaging process is an advanced file system operation:

#### A. Validation Gate
The script *must* call `validate_skill(skill_path)` before proceeding. This ensures that the packaging engine never attempts to zip a skill that has failed the metadata checks, preventing the distribution of broken artifacts.

#### B. File System Traversal
*   **Algorithm:** Uses `Path.rglob('*')` (recursive glob) to traverse every file and subdirectory within the source skill folder.
*   **Core Challenge:** The most complex part is calculating the correct `arcname` (archive name) for the ZIP file.

#### C. Relative Path Calculation (The Key Algorithm)
When zipping a directory structure, the files must appear as if they were placed at the root of the archive, not retaining the full path structure from the disk.

*   **Input:** `file_path` (e.g., `skills/public/my-skill/scripts/utility.py`)
*   **Source Directory:** `skill_path` (e.g., `skills/public/my-skill`)
*   **Calculation:** `arcname = file_path.relative_to(skill_path.parent)`

This calculation effectively strips the parent directory path (`skills/public/`) from the file path, ensuring that when the skill is unzipped, the structure starts cleanly with the skill name (e.g., `my-skill/scripts/utility.py`).

#### D. Serialization
The `zipfile.ZipFile` context manager handles the compression using `zipfile.ZIP_DEFLATED`, creating the final, distributable `.skill` artifact.

---

## 📊 Summary of Design Principles

| Principle | Implementation Component | Benefit |
| :--- | :--- | :--- |
| **Separation of Concerns** | `init_skill.py` vs. `quick_validate.py` | Creation logic is separate from quality assurance logic, allowing independent updates. |
| **Fail-Fast Validation** | `package_skill.py` calling `validate_skill()` | Prevents the creation of invalid artifacts, saving downstream processing time. |
| **Idempotency** | `Path.mkdir(parents=True, exist_ok=True)` | Allows the script to be run multiple times without failing due to pre-existing directories. |
| **Portability** | ZIP Compression (`.skill` file) | Encapsulates all necessary resources (code, docs, assets) into a single, transferable unit, regardless of the host OS. |
| **Strict Contract Enforcement** | `quick_validate.py` | Guarantees that the skill metadata adheres to a predictable, machine-readable schema, crucial for automated AI agent consumption. |
```

## File: README.md
```
# agent-config

My agent configuration for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) and Codex.

## Quick start

```bash
git clone https://github.com/brianlovin/agent-config.git
cd agent-config
./install.sh
```

## What's included

### Settings
- `settings.json` - Global permissions and preferences
- `statusline.sh` - Custom statusline showing token usage

### Skills
Reusable capabilities that your coding agents can invoke.

| Skill | Description |
|-------|-------------|
| `agent-browser` | Browser automation for web testing and interaction |
| `favicon` | Generate favicons from a source image |
| `knip` | Find and remove unused files, dependencies, and exports |
| `rams` | Run accessibility and visual design review |
| `reclaude` | Refactor CLAUDE.md files for progressive disclosure |
| `simplify` | Code simplification specialist |
| `deslop` | Remove AI-generated code slop |

## Managing your config

```bash
# See what's synced vs local-only
./sync.sh

# Preview what install would do
./install.sh --dry-run

# Add a local skill to the repo
./sync.sh add skill my-skill
./sync.sh push

# Pull changes on another machine
./sync.sh pull

# Remove a skill from repo (keeps local copy)
./sync.sh remove skill my-skill
./sync.sh push
```

### Safe operations with backups

All destructive operations create timestamped backups:

```bash
# List available backups
./sync.sh backups

# Restore from last backup
./sync.sh undo
```

### Validate skills

```bash
./sync.sh validate
```

Skills must have a `SKILL.md` with frontmatter containing `name` and `description`.

## Testing

Tests use [Bats](https://github.com/bats-core/bats-core) (Bash Automated Testing System).

```bash
# Install bats (one-time)
brew install bats-core

# Run all tests
bats tests/

# Run specific test file
bats tests/install.bats
bats tests/sync.bats
bats tests/validation.bats
```

Tests run in isolated temp directories and don't affect your actual `~/.claude` config.
Tests also cover Codex skills syncing in `~/.codex/skills`.

## Local-only config

Not everything needs to be synced. The install script only creates symlinks for what's in this repo - it won't delete your local-only skills.

Machine-specific permissions accumulate in `~/.claude/settings.local.json` (auto-created by Claude, not synced).
Codex skills are also linked from this repo into `~/.codex/skills`.

## Creating your own

Fork this repo and customize! The structure is simple:

```
agent-config/
├── settings.json      # Claude Code settings
├── statusline.sh      # Optional statusline script
├── skills/            # Skills (subdirectories with SKILL.md)
├── agents/            # Subagent definitions
├── rules/             # Rule files
└── tests/             # Bats tests
```

## See also

- [Claude Code docs](https://docs.anthropic.com/en/docs/claude-code)
- [My dotfiles](https://github.com/brianlovin/dotfiles) - Shell, git, SSH config

```

## File: schema.json
```
{
  "id": "agent_config",
  "name": "Agent Config",
  "version": "1.0.0",
  "tier": 3,
  "status": "active",
  "domain": "agent-framework",
  "cost_tier": "standard",
  "load_on_boot": false,
  "path": "\\ecosystem\\skills\\agent_config\\SKILL.md",
  "accessible_by": [
    "Orchestrator",
    "Claude Code"
  ],
  "dependencies": [],
  "exposed_functions": [
    {
      "name": "reference",
      "description": "Reference for agent_config",
      "input": "string",
      "output": "string"
    }
  ],
  "consumed_by": [],
  "emits_events": [],
  "listens_to": [],
  "tags": [
    "agent"
  ]
}
```

## File: SKILL.md
```
# SKILL PROFILE: repo_fetched_agent_config_144305
# Department Registry: OAP Toolchain
# Scope: Pure OS-sanctioned Tools
---

## 1. Domain Capability
Generic specialist agent.

## 2. Linked Toolkit
> [!NOTE]
> No static YAML skills mapped. Awaiting dynamic plugin hooks from OAP Orchestrator.

---
*Capability Register hardened by OmniClaw OA Skill Auditor.*

```

## File: _DIR_IDENTITY.md
```
---
id: repo-fetched-agent-config-144305
type: skill
owner: OA
registered_at: 2026-04-04T17:05:13.759485
tags: ["auto-cloned", "AI Agents", "Configuration Management", "Developer Tools", "Skills Library", "oa-assimilated", "premium-repo"]
---

# FETCHED_agent-config_144305

## Assimilation Report
This repository provides a comprehensive, structured configuration framework for AI coding agents (like Claude Code and Codex), managing global settings and a library of reusable 'skills' or capabilities.

```

## File: .claude\rules\testing.md
```
# Testing

This project uses [Bats](https://github.com/bats-core/bats-core) (Bash Automated Testing System) for testing the shell scripts.

## Running Tests

```bash
# Run all tests
bats tests/

# Run specific test file
bats tests/install.bats
bats tests/sync.bats
bats tests/validation.bats

# Run with verbose output (show test names)
bats --tap tests/
```

## Test Structure

```
tests/
├── test_helper.bash    # Shared setup/teardown and utilities
├── install.bats        # Tests for install.sh
├── sync.bats           # Tests for sync.sh commands
└── validation.bats     # Tests for skills validation
```

## Writing Tests

### Test File Format

```bash
#!/usr/bin/env bats

load 'test_helper'

setup() {
    setup_test_env
}

teardown() {
    teardown_test_env
}

@test "description of what this tests" {
    # Arrange
    create_fake_skill "my-skill"

    # Act
    run_install

    # Assert
    assert_symlink "$FAKE_HOME/.claude/skills/my-skill" "$FAKE_REPO/skills/my-skill"
}
```

### Key Conventions

1. **Always use the test environment** - Call `setup_test_env` in setup and `teardown_test_env` in teardown
2. **Use helper functions** - Use `run_install`, `run_sync`, `create_fake_skill`, etc. from test_helper.bash
3. **Test in isolation** - Tests use temp directories (`$FAKE_HOME`, `$FAKE_REPO`) and never touch real config

### Available Test Helpers

**Environment:**
- `setup_test_env` - Creates isolated temp directories
- `teardown_test_env` - Cleans up temp directories
- `$FAKE_HOME` - Temp directory simulating user's home
- `$FAKE_REPO` - Temp directory simulating the repo

**Creating Test Data:**
- `create_fake_skill "name"` - Creates a valid skill with SKILL.md
- `create_invalid_skill "name"` - Creates skill without frontmatter
- `create_skill_no_md "name"` - Creates skill without SKILL.md
- `create_fake_agent "name"` - Creates an agent file
- `create_fake_rule "name"` - Creates a rule file
- `create_fake_settings` - Creates settings.json
- `create_fake_statusline` - Creates statusline.sh

**Running Scripts:**
- `run_install [args]` - Runs install.sh in test environment
- `run_sync [args]` - Runs sync.sh in test environment

**Assertions:**
- `assert_symlink "path" "expected_target"` - Verifies symlink exists and points to target
- `assert_regular_file "path"` - Verifies file exists and is not a symlink
- `assert_dir "path"` - Verifies directory exists
- `assert_backup_exists` - Verifies a backup was created
- `assert_manifest_operation "op"` - Verifies manifest contains operation

**Backup Helpers:**
- `get_latest_backup` - Returns name of most recent backup

### Testing Tips

1. **Test both success and failure cases** - Verify error messages and exit codes
2. **Test dry-run mode** - Ensure `--dry-run` doesn't modify anything
3. **Test idempotency** - Running the same command twice should work
4. **Group related tests** - Use comment headers to organize test sections

## Adding New Tests

When adding new functionality to install.sh or sync.sh:

1. Add tests to the appropriate .bats file
2. Add any new helper functions to test_helper.bash
3. Run `bats tests/` to verify all tests pass
4. Consider edge cases (missing files, conflicts, dry-run)

## CI Integration

Tests run automatically on push/PR via GitHub Actions. See `.github/workflows/test.yml`.

The workflow:
1. Runs on `macos-latest` (matches dev environment)
2. Installs bats-core via Homebrew
3. Runs all tests with `bats tests/`
4. Validates all skills with `./sync.sh validate`

To run locally before pushing:
```bash
bats tests/ && ./sync.sh validate
```

```

## File: .claude\rules\workflows.md
```
# Workflows

## Setting up on a new machine

```bash
git clone git@github.com:brianlovin/agent-config.git ~/Developer/agent-config
cd ~/Developer/agent-config
./install.sh
```

Creates symlinks from `~/.claude/` to this repo. Local-only items are preserved.

### Dry-run mode

Preview what would happen without making changes:

```bash
./install.sh --dry-run
```

### Handling conflicts

If a local file differs from the repo version, you'll be prompted:
- `[r]` Use repo version (backs up local first)
- `[l]` Keep local version (skip this item)
- `[d]` Show diff between versions
- `[q]` Quit

Use `--force` to automatically use repo versions (still creates backups).

## Sync status legend

```bash
./sync.sh
```

Shows status grouped by type (Skills, Agents, Rules):

- `✓` synced (symlinked to this repo)
- `○` local only (not in repo)
- `⚠` conflict (exists in both - run `./install.sh` to fix)
- `→` external (symlinked elsewhere)

## Adding items to sync across machines

```bash
./sync.sh add skill <name>   # Add a skill directory
./sync.sh add agent <name>   # Add an agent file (without .md extension)
./sync.sh add rule <name>    # Add a rule file (without .md extension)
./sync.sh push
```

Copies the item to repo, replaces local with symlink, prompts for commit.

Skills are validated before adding - must have SKILL.md with `name` and `description` in frontmatter.

## Removing items from repo

```bash
./sync.sh remove skill <name>
./sync.sh remove agent <name>
./sync.sh remove rule <name>
./sync.sh push
```

Removes from repo but keeps local copy.

## Backups and undo

All destructive operations create timestamped backups in `.backup/`.

```bash
./sync.sh backups            # List available backups
./sync.sh undo               # Restore from last backup
./sync.sh undo --dry-run     # Preview what would be restored
```

## Validating skills

Check that all skills have valid SKILL.md files:

```bash
./sync.sh validate
```

Skills must have frontmatter with `name` and `description`:

```yaml
---
name: my-skill
description: What this skill does
---
```

## Dry-run mode

Preview any command without making changes:

```bash
./sync.sh --dry-run add skill my-skill
./sync.sh -n remove agent my-agent
./install.sh --dry-run
```

## Keeping items local-only

Any item in `~/.claude/` that isn't symlinked stays local. The install script only creates symlinks for what's in this repo—it never deletes local files.

Use this for work-specific or experimental items.

## Directory structure

```
~/.claude/
├── skills/          # Skill directories (each has SKILL.md)
├── agents/          # Subagent markdown files
├── rules/           # Rule markdown files
├── settings.json
└── statusline.sh
```

```

## File: .github\workflows\test.yml
```
name: Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: macos-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Install bats
        run: brew install bats-core

      - name: Run tests
        run: bats tests/

      - name: Validate skills
        run: ./sync.sh validate

```

## File: agents\security_reviewer.md
```
---
name: security-reviewer
description: Reviews code for security issues including injection vulnerabilities, auth flaws, and secrets in code.
tools: Read, Grep, Glob
---

# Security Code Review

Review code for common security vulnerabilities and issues.

## Check For

### Injection Vulnerabilities
- SQL injection (unsanitized input in queries)
- Command injection (shell commands with user input)
- XSS (unescaped output in HTML/templates)
- Path traversal (user input in file paths)

### Authentication & Authorization
- Missing auth checks on sensitive endpoints
- Hardcoded credentials or API keys
- Weak session management
- Improper access control

### Secrets & Sensitive Data
- API keys, tokens, passwords in source code
- Credentials in configuration files
- Secrets in error messages or logs
- Sensitive data in URLs or query strings

### Data Handling
- Sensitive data logged or exposed in errors
- Missing input validation
- Insecure deserialization
- Improper error handling revealing internals

## Output Format

Report findings with:
1. **Location**: File and line number
2. **Issue**: What the vulnerability is
3. **Risk**: Severity (Critical/High/Medium/Low)
4. **Fix**: Recommended remediation

If no issues found, report "No security issues identified" with a brief summary of what was reviewed.

```

## File: agents\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_config_144305-agents
name: Agents
path: ecosystem/skills/repo_fetched_agent_config_144305/agents
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Agents
Storage area for 'agents' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_config_144305-skills
name: Skills
path: ecosystem/skills/repo_fetched_agent_config_144305/skills
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Skills
Storage area for 'skills' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\agent-browser\SKILL.md
```
---
name: agent-browser
description: Browser automation CLI for AI agents. Use when the user needs to interact with websites, including navigating pages, filling forms, clicking buttons, taking screenshots, extracting data, testing web apps, or automating any browser task. Triggers include requests to "open a website", "fill out a form", "click a button", "take a screenshot", "scrape data from a page", "test this web app", "login to a site", "automate browser actions", or any task requiring programmatic web interaction.
allowed-tools: Bash(npx agent-browser:*), Bash(agent-browser:*)
---

# Browser Automation with agent-browser

The CLI uses Chrome/Chromium via CDP directly. Install via `npm i -g agent-browser`, `brew install agent-browser`, or `cargo install agent-browser`. Run `agent-browser install` to download Chrome.

## Core Workflow

Every browser automation follows this pattern:

1. **Navigate**: `agent-browser open <url>`
2. **Snapshot**: `agent-browser snapshot -i` (get element refs like `@e1`, `@e2`)
3. **Interact**: Use refs to click, fill, select
4. **Re-snapshot**: After navigation or DOM changes, get fresh refs

```bash
agent-browser open https://example.com/form
agent-browser snapshot -i
# Output: @e1 [input type="email"], @e2 [input type="password"], @e3 [button] "Submit"

agent-browser fill @e1 "user@example.com"
agent-browser fill @e2 "password123"
agent-browser click @e3
agent-browser wait --load networkidle
agent-browser snapshot -i  # Check result
```

## Command Chaining

Commands can be chained with `&&` in a single shell invocation. The browser persists between commands via a background daemon, so chaining is safe and more efficient than separate calls.

```bash
# Chain open + wait + snapshot in one call
agent-browser open https://example.com && agent-browser wait --load networkidle && agent-browser snapshot -i

# Chain multiple interactions
agent-browser fill @e1 "user@example.com" && agent-browser fill @e2 "password123" && agent-browser click @e3

# Navigate and capture
agent-browser open https://example.com && agent-browser wait --load networkidle && agent-browser screenshot page.png
```

**When to chain:** Use `&&` when you don't need to read the output of an intermediate command before proceeding (e.g., open + wait + screenshot). Run commands separately when you need to parse the output first (e.g., snapshot to discover refs, then interact using those refs).

## Handling Authentication

When automating a site that requires login, choose the approach that fits:

**Option 1: Import auth from the user's browser (fastest for one-off tasks)**

```bash
# Connect to the user's running Chrome (they're already logged in)
agent-browser --auto-connect state save ./auth.json
# Use that auth state
agent-browser --state ./auth.json open https://app.example.com/dashboard
```

State files contain session tokens in plaintext -- add to `.gitignore` and delete when no longer needed. Set `AGENT_BROWSER_ENCRYPTION_KEY` for encryption at rest.

**Option 2: Persistent profile (simplest for recurring tasks)**

```bash
# First run: login manually or via automation
agent-browser --profile ~/.myapp open https://app.example.com/login
# ... fill credentials, submit ...

# All future runs: already authenticated
agent-browser --profile ~/.myapp open https://app.example.com/dashboard
```

**Option 3: Session name (auto-save/restore cookies + localStorage)**

```bash
agent-browser --session-name myapp open https://app.example.com/login
# ... login flow ...
agent-browser close  # State auto-saved

# Next time: state auto-restored
agent-browser --session-name myapp open https://app.example.com/dashboard
```

**Option 4: Auth vault (credentials stored encrypted, login by name)**

```bash
echo "$PASSWORD" | agent-browser auth save myapp --url https://app.example.com/login --username user --password-stdin
agent-browser auth login myapp
```

**Option 5: State file (manual save/load)**

```bash
# After logging in:
agent-browser state save ./auth.json
# In a future session:
agent-browser state load ./auth.json
agent-browser open https://app.example.com/dashboard
```

See [references/authentication.md](references/authentication.md) for OAuth, 2FA, cookie-based auth, and token refresh patterns.

## Essential Commands

```bash
# Navigation
agent-browser open <url>              # Navigate (aliases: goto, navigate)
agent-browser close                   # Close browser

# Snapshot
agent-browser snapshot -i             # Interactive elements with refs (recommended)
agent-browser snapshot -i -C          # Include cursor-interactive elements (divs with onclick, cursor:pointer)
agent-browser snapshot -s "#selector" # Scope to CSS selector

# Interaction (use @refs from snapshot)
agent-browser click @e1               # Click element
agent-browser click @e1 --new-tab     # Click and open in new tab
agent-browser fill @e2 "text"         # Clear and type text
agent-browser type @e2 "text"         # Type without clearing
agent-browser select @e1 "option"     # Select dropdown option
agent-browser check @e1               # Check checkbox
agent-browser press Enter             # Press key
agent-browser keyboard type "text"    # Type at current focus (no selector)
agent-browser keyboard inserttext "text"  # Insert without key events
agent-browser scroll down 500         # Scroll page
agent-browser scroll down 500 --selector "div.content"  # Scroll within a specific container

# Get information
agent-browser get text @e1            # Get element text
agent-browser get url                 # Get current URL
agent-browser get title               # Get page title
agent-browser get cdp-url             # Get CDP WebSocket URL

# Wait
agent-browser wait @e1                # Wait for element
agent-browser wait --load networkidle # Wait for network idle
agent-browser wait --url "**/page"    # Wait for URL pattern
agent-browser wait 2000               # Wait milliseconds
agent-browser wait --text "Welcome"    # Wait for text to appear (substring match)
agent-browser wait --fn "!document.body.innerText.includes('Loading...')"  # Wait for text to disappear
agent-browser wait "#spinner" --state hidden  # Wait for element to disappear

# Downloads
agent-browser download @e1 ./file.pdf          # Click element to trigger download
agent-browser wait --download ./output.zip     # Wait for any download to complete
agent-browser --download-path ./downloads open <url>  # Set default download directory

# Viewport & Device Emulation
agent-browser set viewport 1920 1080          # Set viewport size (default: 1280x720)
agent-browser set viewport 1920 1080 2        # 2x retina (same CSS size, higher res screenshots)
agent-browser set device "iPhone 14"          # Emulate device (viewport + user agent)

# Capture
agent-browser screenshot              # Screenshot to temp dir
agent-browser screenshot --full       # Full page screenshot
agent-browser screenshot --annotate   # Annotated screenshot with numbered element labels
agent-browser screenshot --screenshot-dir ./shots  # Save to custom directory
agent-browser screenshot --screenshot-format jpeg --screenshot-quality 80
agent-browser pdf output.pdf          # Save as PDF

# Clipboard
agent-browser clipboard read                      # Read text from clipboard
agent-browser clipboard write "Hello, World!"     # Write text to clipboard
agent-browser clipboard copy                      # Copy current selection
agent-browser clipboard paste                     # Paste from clipboard

# Diff (compare page states)
agent-browser diff snapshot                          # Compare current vs last snapshot
agent-browser diff snapshot --baseline before.txt    # Compare current vs saved file
agent-browser diff screenshot --baseline before.png  # Visual pixel diff
agent-browser diff url <url1> <url2>                 # Compare two pages
agent-browser diff url <url1> <url2> --wait-until networkidle  # Custom wait strategy
agent-browser diff url <url1> <url2> --selector "#main"  # Scope to element
```

## Common Patterns

### Form Submission

```bash
agent-browser open https://example.com/signup
agent-browser snapshot -i
agent-browser fill @e1 "Jane Doe"
agent-browser fill @e2 "jane@example.com"
agent-browser select @e3 "California"
agent-browser check @e4
agent-browser click @e5
agent-browser wait --load networkidle
```

### Authentication with Auth Vault (Recommended)

```bash
# Save credentials once (encrypted with AGENT_BROWSER_ENCRYPTION_KEY)
# Recommended: pipe password via stdin to avoid shell history exposure
echo "pass" | agent-browser auth save github --url https://github.com/login --username user --password-stdin

# Login using saved profile (LLM never sees password)
agent-browser auth login github

# List/show/delete profiles
agent-browser auth list
agent-browser auth show github
agent-browser auth delete github
```

### Authentication with State Persistence

```bash
# Login once and save state
agent-browser open https://app.example.com/login
agent-browser snapshot -i
agent-browser fill @e1 "$USERNAME"
agent-browser fill @e2 "$PASSWORD"
agent-browser click @e3
agent-browser wait --url "**/dashboard"
agent-browser state save auth.json

# Reuse in future sessions
agent-browser state load auth.json
agent-browser open https://app.example.com/dashboard
```

### Session Persistence

```bash
# Auto-save/restore cookies and localStorage across browser restarts
agent-browser --session-name myapp open https://app.example.com/login
# ... login flow ...
agent-browser close  # State auto-saved to ~/.agent-browser/sessions/

# Next time, state is auto-loaded
agent-browser --session-name myapp open https://app.example.com/dashboard

# Encrypt state at rest
export AGENT_BROWSER_ENCRYPTION_KEY=$(openssl rand -hex 32)
agent-browser --session-name secure open https://app.example.com

# Manage saved states
agent-browser state list
agent-browser state show myapp-default.json
agent-browser state clear myapp
agent-browser state clean --older-than 7
```

### Data Extraction

```bash
agent-browser open https://example.com/products
agent-browser snapshot -i
agent-browser get text @e5           # Get specific element text
agent-browser get text body > page.txt  # Get all page text

# JSON output for parsing
agent-browser snapshot -i --json
agent-browser get text @e1 --json
```

### Parallel Sessions

```bash
agent-browser --session site1 open https://site-a.com
agent-browser --session site2 open https://site-b.com

agent-browser --session site1 snapshot -i
agent-browser --session site2 snapshot -i

agent-browser session list
```

### Connect to Existing Chrome

```bash
# Auto-discover running Chrome with remote debugging enabled
agent-browser --auto-connect open https://example.com
agent-browser --auto-connect snapshot

# Or with explicit CDP port
agent-browser --cdp 9222 snapshot
```

### Color Scheme (Dark Mode)

```bash
# Persistent dark mode via flag (applies to all pages and new tabs)
agent-browser --color-scheme dark open https://example.com

# Or via environment variable
AGENT_BROWSER_COLOR_SCHEME=dark agent-browser open https://example.com

# Or set during session (persists for subsequent commands)
agent-browser set media dark
```

### Viewport & Responsive Testing

```bash
# Set a custom viewport size (default is 1280x720)
agent-browser set viewport 1920 1080
agent-browser screenshot desktop.png

# Test mobile-width layout
agent-browser set viewport 375 812
agent-browser screenshot mobile.png

# Retina/HiDPI: same CSS layout at 2x pixel density
# Screenshots stay at logical viewport size, but content renders at higher DPI
agent-browser set viewport 1920 1080 2
agent-browser screenshot retina.png

# Device emulation (sets viewport + user agent in one step)
agent-browser set device "iPhone 14"
agent-browser screenshot device.png
```

The `scale` parameter (3rd argument) sets `window.devicePixelRatio` without changing CSS layout. Use it when testing retina rendering or capturing higher-resolution screenshots.

### Visual Browser (Debugging)

```bash
agent-browser --headed open https://example.com
agent-browser highlight @e1          # Highlight element
agent-browser inspect                # Open Chrome DevTools for the active page
agent-browser record start demo.webm # Record session
agent-browser profiler start         # Start Chrome DevTools profiling
agent-browser profiler stop trace.json # Stop and save profile (path optional)
```

Use `AGENT_BROWSER_HEADED=1` to enable headed mode via environment variable. Browser extensions work in both headed and headless mode.

### Local Files (PDFs, HTML)

```bash
# Open local files with file:// URLs
agent-browser --allow-file-access open file:///path/to/document.pdf
agent-browser --allow-file-access open file:///path/to/page.html
agent-browser screenshot output.png
```

### iOS Simulator (Mobile Safari)

```bash
# List available iOS simulators
agent-browser device list

# Launch Safari on a specific device
agent-browser -p ios --device "iPhone 16 Pro" open https://example.com

# Same workflow as desktop - snapshot, interact, re-snapshot
agent-browser -p ios snapshot -i
agent-browser -p ios tap @e1          # Tap (alias for click)
agent-browser -p ios fill @e2 "text"
agent-browser -p ios swipe up         # Mobile-specific gesture

# Take screenshot
agent-browser -p ios screenshot mobile.png

# Close session (shuts down simulator)
agent-browser -p ios close
```

**Requirements:** macOS with Xcode, Appium (`npm install -g appium && appium driver install xcuitest`)

**Real devices:** Works with physical iOS devices if pre-configured. Use `--device "<UDID>"` where UDID is from `xcrun xctrace list devices`.

## Security

All security features are opt-in. By default, agent-browser imposes no restrictions on navigation, actions, or output.

### Content Boundaries (Recommended for AI Agents)

Enable `--content-boundaries` to wrap page-sourced output in markers that help LLMs distinguish tool output from untrusted page content:

```bash
export AGENT_BROWSER_CONTENT_BOUNDARIES=1
agent-browser snapshot
# Output:
# --- AGENT_BROWSER_PAGE_CONTENT nonce=<hex> origin=https://example.com ---
# [accessibility tree]
# --- END_AGENT_BROWSER_PAGE_CONTENT nonce=<hex> ---
```

### Domain Allowlist

Restrict navigation to trusted domains. Wildcards like `*.example.com` also match the bare domain `example.com`. Sub-resource requests, WebSocket, and EventSource connections to non-allowed domains are also blocked. Include CDN domains your target pages depend on:

```bash
export AGENT_BROWSER_ALLOWED_DOMAINS="example.com,*.example.com"
agent-browser open https://example.com        # OK
agent-browser open https://malicious.com       # Blocked
```

### Action Policy

Use a policy file to gate destructive actions:

```bash
export AGENT_BROWSER_ACTION_POLICY=./policy.json
```

Example `policy.json`:

```json
{
  "default": "deny",
  "allow": ["navigate", "snapshot", "click", "scroll", "wait", "get"]
}
```

Auth vault operations (`auth login`, etc.) bypass action policy but domain allowlist still applies.

### Output Limits

Prevent context flooding from large pages:

```bash
export AGENT_BROWSER_MAX_OUTPUT=50000
```

## Diffing (Verifying Changes)

Use `diff snapshot` after performing an action to verify it had the intended effect. This compares the current accessibility tree against the last snapshot taken in the session.

```bash
# Typical workflow: snapshot -> action -> diff
agent-browser snapshot -i          # Take baseline snapshot
agent-browser click @e2            # Perform action
agent-browser diff snapshot        # See what changed (auto-compares to last snapshot)
```

For visual regression testing or monitoring:

```bash
# Save a baseline screenshot, then compare later
agent-browser screenshot baseline.png
# ... time passes or changes are made ...
agent-browser diff screenshot --baseline baseline.png

# Compare staging vs production
agent-browser diff url https://staging.example.com https://prod.example.com --screenshot
```

`diff snapshot` output uses `+` for additions and `-` for removals, similar to git diff. `diff screenshot` produces a diff image with changed pixels highlighted in red, plus a mismatch percentage.

## Timeouts and Slow Pages

The default timeout is 25 seconds. This can be overridden with the `AGENT_BROWSER_DEFAULT_TIMEOUT` environment variable (value in milliseconds). For slow websites or large pages, use explicit waits instead of relying on the default timeout:

```bash
# Wait for network activity to settle (best for slow pages)
agent-browser wait --load networkidle

# Wait for a specific element to appear
agent-browser wait "#content"
agent-browser wait @e1

# Wait for a specific URL pattern (useful after redirects)
agent-browser wait --url "**/dashboard"

# Wait for a JavaScript condition
agent-browser wait --fn "document.readyState === 'complete'"

# Wait a fixed duration (milliseconds) as a last resort
agent-browser wait 5000
```

When dealing with consistently slow websites, use `wait --load networkidle` after `open` to ensure the page is fully loaded before taking a snapshot. If a specific element is slow to render, wait for it directly with `wait <selector>` or `wait @ref`.

## Session Management and Cleanup

When running multiple agents or automations concurrently, always use named sessions to avoid conflicts:

```bash
# Each agent gets its own isolated session
agent-browser --session agent1 open site-a.com
agent-browser --session agent2 open site-b.com

# Check active sessions
agent-browser session list
```

Always close your browser session when done to avoid leaked processes:

```bash
agent-browser close                    # Close default session
agent-browser --session agent1 close   # Close specific session
```

If a previous session was not closed properly, the daemon may still be running. Use `agent-browser close` to clean it up before starting new work.

To auto-shutdown the daemon after a period of inactivity (useful for ephemeral/CI environments):

```bash
AGENT_BROWSER_IDLE_TIMEOUT_MS=60000 agent-browser open example.com
```

## Ref Lifecycle (Important)

Refs (`@e1`, `@e2`, etc.) are invalidated when the page changes. Always re-snapshot after:

- Clicking links or buttons that navigate
- Form submissions
- Dynamic content loading (dropdowns, modals)

```bash
agent-browser click @e5              # Navigates to new page
agent-browser snapshot -i            # MUST re-snapshot
agent-browser click @e1              # Use new refs
```

## Annotated Screenshots (Vision Mode)

Use `--annotate` to take a screenshot with numbered labels overlaid on interactive elements. Each label `[N]` maps to ref `@eN`. This also caches refs, so you can interact with elements immediately without a separate snapshot.

```bash
agent-browser screenshot --annotate
# Output includes the image path and a legend:
#   [1] @e1 button "Submit"
#   [2] @e2 link "Home"
#   [3] @e3 textbox "Email"
agent-browser click @e2              # Click using ref from annotated screenshot
```

Use annotated screenshots when:

- The page has unlabeled icon buttons or visual-only elements
- You need to verify visual layout or styling
- Canvas or chart elements are present (invisible to text snapshots)
- You need spatial reasoning about element positions

## Semantic Locators (Alternative to Refs)

When refs are unavailable or unreliable, use semantic locators:

```bash
agent-browser find text "Sign In" click
agent-browser find label "Email" fill "user@test.com"
agent-browser find role button click --name "Submit"
agent-browser find placeholder "Search" type "query"
agent-browser find testid "submit-btn" click
```

## JavaScript Evaluation (eval)

Use `eval` to run JavaScript in the browser context. **Shell quoting can corrupt complex expressions** -- use `--stdin` or `-b` to avoid issues.

```bash
# Simple expressions work with regular quoting
agent-browser eval 'document.title'
agent-browser eval 'document.querySelectorAll("img").length'

# Complex JS: use --stdin with heredoc (RECOMMENDED)
agent-browser eval --stdin <<'EVALEOF'
JSON.stringify(
  Array.from(document.querySelectorAll("img"))
    .filter(i => !i.alt)
    .map(i => ({ src: i.src.split("/").pop(), width: i.width }))
)
EVALEOF

# Alternative: base64 encoding (avoids all shell escaping issues)
agent-browser eval -b "$(echo -n 'Array.from(document.querySelectorAll("a")).map(a => a.href)' | base64)"
```

**Why this matters:** When the shell processes your command, inner double quotes, `!` characters (history expansion), backticks, and `$()` can all corrupt the JavaScript before it reaches agent-browser. The `--stdin` and `-b` flags bypass shell interpretation entirely.

**Rules of thumb:**

- Single-line, no nested quotes -> regular `eval 'expression'` with single quotes is fine
- Nested quotes, arrow functions, template literals, or multiline -> use `eval --stdin <<'EVALEOF'`
- Programmatic/generated scripts -> use `eval -b` with base64

## Configuration File

Create `agent-browser.json` in the project root for persistent settings:

```json
{
  "headed": true,
  "proxy": "http://localhost:8080",
  "profile": "./browser-data"
}
```

Priority (lowest to highest): `~/.agent-browser/config.json` < `./agent-browser.json` < env vars < CLI flags. Use `--config <path>` or `AGENT_BROWSER_CONFIG` env var for a custom config file (exits with error if missing/invalid). All CLI options map to camelCase keys (e.g., `--executable-path` -> `"executablePath"`). Boolean flags accept `true`/`false` values (e.g., `--headed false` overrides config). Extensions from user and project configs are merged, not replaced.

## Deep-Dive Documentation

| Reference                                                            | When to Use                                               |
| -------------------------------------------------------------------- | --------------------------------------------------------- |

## Browser Engine Selection

Use `--engine` to choose a local browser engine. The default is `chrome`.

```bash
# Use Lightpanda (fast headless browser, requires separate install)
agent-browser --engine lightpanda open example.com

# Via environment variable
export AGENT_BROWSER_ENGINE=lightpanda
agent-browser open example.com

# With custom binary path
agent-browser --engine lightpanda --executable-path /path/to/lightpanda open example.com
```

Supported engines:

- `chrome` (default) -- Chrome/Chromium via CDP
- `lightpanda` -- Lightpanda headless browser via CDP (10x faster, 10x less memory than Chrome)

Lightpanda does not support `--extension`, `--profile`, `--state`, or `--allow-file-access`. Install Lightpanda from https://lightpanda.io/docs/open-source/installation.

## Ready-to-Use Templates

| Template                                                                 | Description                         |
| ------------------------------------------------------------------------ | ----------------------------------- |

```bash
./templates/form-automation.sh https://example.com/form
./templates/authenticated-session.sh https://app.example.com/login
./templates/capture-workflow.sh https://example.com ./output
```

```

## File: skills\agent-browser\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_config_144305-skills-agent-browser
name: Agent-Browser
path: ecosystem/skills/repo_fetched_agent_config_144305/skills/agent-browser
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Agent-Browser
Storage area for 'agent-browser' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\bun\SKILL.md
```
---
name: bun
description: Use Bun instead of Node.js, npm, pnpm, or vite. Provides command mappings, Bun-specific APIs, and development patterns.
---

# Bun Runtime

Use Bun as the default JavaScript/TypeScript runtime and package manager.

## Command Mappings

| Instead of | Use |
|------------|-----|
| `node file.ts` | `bun file.ts` |
| `ts-node file.ts` | `bun file.ts` |
| `npm install` | `bun install` |
| `npm run script` | `bun run script` |
| `jest` / `vitest` | `bun test` |
| `webpack` / `esbuild` | `bun build` |

Bun automatically loads `.env` files - don't use dotenv.

## Bun-Specific APIs

Prefer these over Node.js equivalents:

| API | Purpose | Don't use |
|-----|---------|-----------|
| `Bun.serve()` | HTTP server with WebSocket, HTTPS, routes | express |
| `bun:sqlite` | SQLite database | better-sqlite3 |
| `Bun.redis` | Redis client | ioredis |
| `Bun.sql` | Postgres client | pg, postgres.js |
| `Bun.file()` | File operations | node:fs readFile/writeFile |
| `Bun.$\`cmd\`` | Shell commands | execa |
| `WebSocket` | WebSocket client (built-in) | ws |

## Testing

Use `bun:test` for tests:

```ts
import { test, expect } from "bun:test";

test("description", () => {
  expect(1).toBe(1);
});
```

Run with `bun test`.

## Frontend Development

Use HTML imports with `Bun.serve()` instead of Vite. Supports React, CSS, Tailwind.

**Server:**

```ts
import index from "./index.html"

Bun.serve({
  routes: {
    "/": index,
    "/api/users/:id": {
      GET: (req) => Response.json({ id: req.params.id }),
    },
  },
  development: { hmr: true, console: true }
})
```

**HTML file:**

```html
<html>
  <body>
    <script type="module" src="./app.tsx"></script>
  </body>
</html>
```

Bun's bundler transpiles `.tsx`, `.jsx`, `.js` automatically. CSS is bundled via `<link>` tags.

Run with `bun --hot ./server.ts` for HMR.

## Documentation

For detailed API docs, see `node_modules/bun-types/docs/**.md`.

```

## File: skills\bun\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_config_144305-skills-bun
name: Bun
path: ecosystem/skills/repo_fetched_agent_config_144305/skills/bun
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Bun
Storage area for 'bun' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\chrome-webstore-release-blueprint\SKILL.md
```
---
name: chrome-webstore-release-blueprint
description: Guide a user end-to-end through setting up Chrome Web Store API release automation in any repository. Use when asked to walk someone through OAuth/CWS credential setup, refresh token creation, local/CI secret setup, version-based publish automation, and submission status checks.
---

# Chrome Web Store Release Blueprint

Use this skill as a hands-on setup guide. The agent should lead the user step-by-step, ask for confirmations, and only automate the parts that can be done locally/in CI.

## What This Skill Is For

- Helping a user set up Chrome Web Store release automation from scratch.
- Giving clear manual instructions for Google/CWS dashboard steps.
- Implementing repo-side scripts/workflows after the user provides credentials.
- Verifying submission state (`PUBLISHED`, `PENDING_REVIEW`, etc.).

## Agent Behavior Rules

- Treat dashboard/OAuth tasks as user-driven; do not imply you performed them.
- Give one clear step at a time and wait for confirmation before moving on.
- Ask for exact values only when needed, and tell user where each value comes from.
- Mask secrets in logs and never commit secret values to git.
- If `gh` is available, offer secret upload automation; if not, provide manual fallback.

## Step 1: Project Discovery (Before Any Credential Work)

Collect these inputs:

- manifest path containing extension version
- build command
- zip/package command and output file name/path
- CI platform (GitHub Actions by default)
- release branch policy (`main`, tags, or manual dispatch)
- local secret file convention (`.env`, `.env.local`, etc.)

Ask explicitly:
- "Do you want CI to publish only when version changes?"
- "Do you want me to wire GitHub secret upload via `gh`?"

## Step 2: Detailed Credential Walkthrough (User + Agent)

### 2.1 Enable API in Google Cloud

Tell user to open:
- `https://console.cloud.google.com/apis/library/chromewebstore.googleapis.com`

User actions:
1. Select the intended Google Cloud project.
2. Click `Enable` for Chrome Web Store API.

Agent prompt example:
- "When Chrome Web Store API shows as Enabled, tell me and I will move to OAuth setup."

### 2.2 Configure OAuth Consent Screen

Tell user to open one of:
- `https://console.cloud.google.com/apis/credentials/consent`
- If UI redirects, continue in Google Auth Platform consent screen pages.

User actions:
1. Choose `External` user type (for non-Workspace internal apps).
2. Fill app name, support email, developer contact email.
3. Save and continue through scopes unless custom scopes are required.
4. Add your own Google account as a test user if app is in Testing mode.
5. Save.

Agent guidance:
- If user wants stable long-lived refresh token behavior, recommend moving consent screen to Production when ready.

### 2.3 Create OAuth Client

Tell user to open:
- `https://console.cloud.google.com/apis/credentials`

User actions:
1. Click `Create Credentials` -> `OAuth client ID`.
2. Choose application type `Web application`.
3. Add authorized redirect URI exactly:
- `https://developers.google.com/oauthplayground`
4. Create client.

Capture values:
- `CWS_CLIENT_ID`
- `CWS_CLIENT_SECRET`

Agent prompt example:
- "Paste `CWS_CLIENT_ID` and `CWS_CLIENT_SECRET` when ready (I will treat them as secrets)."

### 2.4 Generate Refresh Token (OAuth Playground)

Tell user to open:
- `https://developers.google.com/oauthplayground/`

User actions:
1. Click the settings gear icon.
2. Enable `Use your own OAuth credentials`.
3. Paste `CWS_CLIENT_ID` and `CWS_CLIENT_SECRET`.
4. In Step 1, enter scope:
- `https://www.googleapis.com/auth/chromewebstore`
5. Click `Authorize APIs`.
6. Sign in with the same Google account that owns/publishes the extension.
7. Click `Exchange authorization code for tokens`.
8. Copy refresh token.

Capture value:
- `CWS_REFRESH_TOKEN`

Agent prompt example:
- "Paste `CWS_REFRESH_TOKEN` now. I will only place it in local secret storage/CI secrets."

### 2.5 Capture Store IDs

Capture:
- `CWS_EXTENSION_ID` (the extension item ID from store/developer listing URL)
- `CWS_PUBLISHER_ID` (developer/publisher ID from Chrome Web Store developer account context)

Agent instruction:
- If user is unsure, ask them to open the Chrome Web Store Developer Dashboard and copy IDs from item/account URLs or account details.

### 2.6 Credential Checklist

Do not proceed until all five exist:
- `CWS_CLIENT_ID`
- `CWS_CLIENT_SECRET`
- `CWS_REFRESH_TOKEN`
- `CWS_PUBLISHER_ID`
- `CWS_EXTENSION_ID`

## Step 3: Local Secret File and CI Secret Setup

Create a local template file (no real values committed):

```env
CWS_CLIENT_ID=
CWS_CLIENT_SECRET=
CWS_REFRESH_TOKEN=
CWS_PUBLISHER_ID=
CWS_EXTENSION_ID=
```

Ensure real secret file path is gitignored.

If using GitHub Actions, ask user if `gh` automation is desired.

If yes, verify:

```bash
gh --version
gh auth status
```

If `gh` auth is missing, tell user to run:
- `gh auth login`

Then implement a helper script that:
- reads secret values from local env file
- validates all required keys are present
- supports `--dry-run`
- masks values in dry-run output
- uploads with `gh secret set ... --repo ...`
- fails fast on missing keys/auth

If user declines `gh`, provide manual secret entry checklist for repository settings.

## Step 4: Release Workflow Blueprint (Version-Triggered)

Design the CI workflow around this logic:

1. Read local manifest version.
2. Optionally compare with a secondary version file and fail on mismatch.
3. Exchange refresh token for access token:
- `POST https://oauth2.googleapis.com/token`
4. Fetch CWS status:
- `GET https://chromewebstore.googleapis.com/v2/publishers/<publisherId>/items/<extensionId>:fetchStatus`
5. Extract current published version from:
- `publishedItemRevisionStatus.distributionChannels[0].crxVersion`
6. If local version == published version, skip publish.
7. If version changed:
- build package zip
- upload zip:
  `POST https://chromewebstore.googleapis.com/upload/v2/publishers/<publisherId>/items/<extensionId>:upload`
- handle async upload state with polling when needed
- publish:
  `POST https://chromewebstore.googleapis.com/v2/publishers/<publisherId>/items/<extensionId>:publish`

Treat these publish states as successful submission:
- `PENDING_REVIEW`
- `PUBLISHED`
- `PUBLISHED_TO_TESTERS`
- `STAGED`

## Step 5: Submission Status Checker Blueprint

Create a script dedicated to "what is the latest submission state?".

Required behavior:
- accepts env values (and optional `--env-file`)
- optionally accepts `--manifest` for local version comparison
- supports `--json`
- calls token endpoint + `fetchStatus`
- outputs normalized fields:
  - `itemId`
  - `localVersion`
  - `publishedVersion`
  - `publishedState`
  - `submittedVersion`
  - `submittedState`
  - `upToDate`
  - `pendingReview`
- exits non-zero on auth/API/input errors

Helpful checks to include:
- flag version mismatch between manifest and package metadata
- show whether uploaded version is pending review but not yet published
- print concise human summary when `--json` is not used

## Step 6: Guided Verification Flow

Run this with the user:

1. Confirm status checker runs successfully before release.
2. Bump extension version (patch) in all version sources.
3. Push branch and trigger workflow.
4. Confirm workflow either:
- skips (if no version change), or
- uploads and submits publish.
5. Re-run status checker:
- expect `PENDING_REVIEW` first in many cases
- later expect published channel to match local version

## Troubleshooting Script (What Agent Should Say)

- `invalid_grant`:
- likely wrong/expired refresh token, wrong OAuth client, or wrong account
- `403` from CWS endpoint:
- account lacks publisher permissions for that extension
- workflow no-op:
- local version equals published version by design
- upload failure:
- inspect API response and packaged zip structure/manifest validity
- version mismatch guard failure:
- align all declared version files before publishing

## Practical Links (Share During Guidance)

- Chrome Web Store API overview:
`https://developer.chrome.com/docs/webstore/using-api`
- Publish endpoint:
`https://developer.chrome.com/docs/webstore/publish`
- OAuth Playground:
`https://developers.google.com/oauthplayground/`
- API enablement page:
`https://console.cloud.google.com/apis/library/chromewebstore.googleapis.com`
- Credentials page:
`https://console.cloud.google.com/apis/credentials`

## Guardrails

- Never commit credentials.
- Never hardcode secrets in workflow YAML.
- Never auto-publish every push without version comparison.
- Keep setup instructions explicit and user-confirmed at each manual step.
- Prefer repeatable helper scripts over ad-hoc one-off commands.

```

## File: skills\chrome-webstore-release-blueprint\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_config_144305-skills-chrome-webstore-release-blueprint
name: Chrome-Webstore-Release-Blueprint
path: ecosystem/skills/repo_fetched_agent_config_144305/skills/chrome-webstore-release-blueprint
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Chrome-Webstore-Release-Blueprint
Storage area for 'chrome-webstore-release-blueprint' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\deslop\SKILL.md
```
---
name: deslop
description: Remove AI-generated code slop from the current branch. Use after writing code to clean up unnecessary comments, defensive checks, and inconsistent style.
---

# Remove AI code slop

Check the diff against main, and remove all AI generated slop introduced in this branch.

This includes:
- Extra comments that a human wouldn't add or is inconsistent with the rest of the file
- Extra defensive checks or try/catch blocks that are abnormal for that area of the codebase (especially if called by trusted / validated codepaths)
- Casts to any to get around type issues
- Any other style that is inconsistent with the file

Report at the end with only a 1-3 sentence summary of what you changed

```

## File: skills\deslop\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_config_144305-skills-deslop
name: Deslop
path: ecosystem/skills/repo_fetched_agent_config_144305/skills/deslop
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Deslop
Storage area for 'deslop' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\electron-wrapper\skill.md
```
---
name: electron-wrapper
description: >
  Wrap a Bun web app into an Electron desktop app with native window management,
  auto-updates, code signing, and CI/CD distribution. Use when the user wants to
  create a native desktop application from an existing Bun-based web server,
  package it for macOS/Windows, set up auto-updating, or handle Electron UX
  concerns like drag regions and traffic lights. Also use when cutting releases
  or tagging versions for Electron apps.
---

# Electron Wrapper for Bun Web Apps

This skill guides wrapping an existing Bun web server into a native desktop app using Electron. It's based on a proven implementation that solved every major integration challenge.

## Architecture

**"Electron as chrome, Bun as server"** — Two runtimes working together:

- **Electron/Node.js** handles window management, native menus, auto-updates, and IPC
- **Bun** runs the actual web server with all your application logic

The Electron main process spawns a bundled Bun binary that runs your server, then loads `http://localhost:{port}` in a `BrowserWindow`. Your web app doesn't know or care that it's inside Electron — it's just a web page with an optional `window.electronAPI` bridge for native features.

This architecture means:
- Zero changes to your server code (it's still a standard Bun HTTP server)
- The web app works identically in a browser or in Electron
- Electron handles only what browsers can't: window chrome, system tray, auto-updates, file system access
- Two separate `node_modules` — Electron uses npm, your web app uses Bun

## Phase 1: Project Setup

Create the Electron subproject alongside your existing Bun web app.

**What to create:**
- `electron/` directory with its own `package.json` (npm, not Bun), two tsconfigs (ESM for main, CJS for preload), `electron-builder.yml`, and macOS entitlements
- `scripts/build-server.ts` for bundling the server
- `scripts/download-bun.ts` for downloading platform-specific Bun binaries
- Parent project changes: new scripts, tsconfig excludes, .gitignore entries

**Reference:** [project-setup.md](references/project-setup.md)

## Phase 2: Main Process

Build the Electron main process — the entry point, server spawning, window management, auto-updater, and preload bridge.

**Files to create:**

| File | Purpose |
|------|---------|
| `electron/src/main/index.ts` | App lifecycle, dev/prod mode, single-instance lock, IPC handlers |
| `electron/src/main/bun-server.ts` | Spawn bundled Bun, port selection, health polling, env var injection |
| `electron/src/main/window.ts` | BrowserWindow config, bounds persistence, security settings, navigation guards |
| `electron/src/main/updater.ts` | electron-updater setup, event forwarding to renderer |
| `electron/src/preload/index.ts` | contextBridge API with invoke/on patterns and unsubscribe support |

**Key decisions:**
- Dev mode uses `ELECTRON_DEV_URL` env var to connect to the external dev server (no internal Bun spawn)
- `autoDownload: false` — let users choose when to download updates
- Preload exposes only specific methods, never raw `ipcRenderer`
- Window persists bounds via `electron-store`

**Reference:** [main-process.md](references/main-process.md)

## Phase 3: Web App Adaptation

Adapt the existing web app to detect and respond to the Electron environment while remaining fully functional as a standalone web app.

**Changes to the web app:**

| Change | Details |
|--------|---------|
| Electron detection utility | `isElectron()`, `getElectronPlatform()`, `isMacElectron()`, `applyElectronDocumentAttributes()` |
| Type declarations | `window.electronAPI` with all properties optional |
| CSS drag regions | `.app-window-drag`/`.app-window-no-drag` classes, auto-exclude interactive elements |
| Traffic light spacing | `--electron-traffic-left` CSS variable (72px on macOS, 0px elsewhere) |
| Storage path | Env var for data directory, falling back to CWD |
| Static asset serving | Env var for static dir in production mode |
| Auto-update hook | `useElectronUpdater()` React hook with download/install controls |
| Update notification | Pill component showing available → downloading → ready states |
| Feature gating | Disable demo mode, hosted features when in Electron |

**Reference:** [web-adaptation.md](references/web-adaptation.md)

## Phase 4: Build & Distribution

Bundle everything, set up CI/CD, and handle code signing.

**Build pipeline:**
1. Build web app (`bun run build`)
2. Bundle server to single file (`Bun.build()` → `resources/server/index.js`)
3. Download platform-specific Bun binaries → `resources/bun/{platform}-{arch}/`
4. Compile Electron TypeScript (two passes: main ESM + preload CJS)
5. electron-builder packages everything with `extraResources`

**CI/CD:**
- GitHub Actions triggered by version tags (e.g., `v*`, `clippy-v*`)
- Matrix builds: macOS arm64/x64 on `macos-14`, Windows x64 on `windows-latest`
- `--publish never` in build step, separate publish job creates draft GitHub release
- Apple certificate import and notarization in CI

**Code signing:**
- macOS: Developer ID Application certificate, exported as base64 .p12
- Notarization via Apple ID + app-specific password
- 5 GitHub secrets required: `APPLE_CERTIFICATE`, `APPLE_CERTIFICATE_PASSWORD`, `APPLE_ID`, `APPLE_PASSWORD`, `APPLE_TEAM_ID`

**Icons:**
- macOS: `sips` + `iconutil` from source PNG → `.icns`
- Windows: `png-to-ico` npm package → `.ico`

**Reference:** [build-and-distribute.md](references/build-and-distribute.md)

## Cutting a Release

**Never build release artifacts locally.** CI has the signing certificates and notarization credentials. Local builds produce unsigned apps that macOS Gatekeeper will block.

### Release workflow:

1. **Bump version** in `electron/package.json`, commit, and merge to main
2. **Find the tag pattern** the CI workflow expects:
   ```bash
   grep -A2 'tags:' .github/workflows/*.yml
   ```
3. **Tag the merged commit on main:**
   ```bash
   git tag <pattern><version> origin/main
   git push origin <pattern><version>
   ```
4. **Monitor CI:**
   ```bash
   gh run list --workflow=<workflow>.yml --limit=1
   ```
5. **Review and publish** the draft release on GitHub

### Common mistakes:
- Running `electron-builder --publish always` locally — no notarization
- Using `gh release create` with local artifacts — unsigned
- Tagging before the version bump is merged — wrong version in build
- Tagging a feature branch instead of `origin/main`

See [pitfalls.md §13](references/pitfalls.md) for full details.

## Critical Pitfalls

Quick-reference list — see [pitfalls.md](references/pitfalls.md) for full details with symptoms and code examples.

| # | Pitfall | One-line fix |
|---|---------|-------------|
| 1 | ESM/CJS conflicts | `"type": "module"` + default import pattern for CJS packages |
| 2 | Preload must be CJS | Separate tsconfig with `"module": "CommonJS"` |
| 3 | `__dirname` unavailable | `fileURLToPath(import.meta.url)` polyfill |
| 4 | Dev mode MIME errors | Connect to external dev server via `ELECTRON_DEV_URL` |
| 5 | Bun version mismatch | Pin version in download script, match dev version |
| 6 | nvm PATH issues | `bash -lc` for spawned processes |
| 7 | Wrong storage path | Env var + `app.getPath("userData")` |
| 8 | White flash on open | `show: false` + `ready-to-show` + dark `backgroundColor` |
| 11 | `${platform}` != `process.platform` | Put Bun `extraResources` in `mac:`/`win:` sections with `darwin-`/`win32-` prefixes |
| 12 | Bun workspace hoists deps | Bundle main with esbuild + `createRequire` banner, or use npm for electron dir |
| 13 | Local builds aren't notarized | Always release via CI tags, never `electron-builder --publish` locally |

## Dev Workflow

The `electron:dev` command runs the full development environment:

```
npm run dev
  ├── concurrently
  │   ├── dev:web    → cd .. && bun run dev          (Bun dev server with HMR)
  │   └── dev:electron
  │       ├── wait-on http://localhost:3005           (wait for dev server)
  │       ├── npm run build                           (compile TS)
  │       └── ELECTRON_DEV_URL=... electron .         (launch Electron)
```

- The web dev server runs with HMR — changes reflect instantly
- Electron connects to the dev server instead of spawning its own Bun
- Preload and main process changes require restarting `electron:dev`
- Web app changes hot-reload automatically

To test production-like behavior locally:
```bash
bun run electron:pack    # builds everything, packages without installer
# Output in electron/release/
```

## Customization Checklist

When adapting this for a new project, update these project-specific values:

- [ ] App name in `electron-builder.yml` (`productName`, `appId`)
- [ ] Window title in `window.ts`
- [ ] Dev server port in `dev:electron` script and `dev` script
- [ ] Environment variable names (e.g., `APP_DATA_DIR`, `APP_STATIC_DIR`)
- [ ] `backgroundColor` in window config to match your app's theme
- [ ] `category` in `electron-builder.yml` mac section
- [ ] Repository URL in `electron/package.json`
- [ ] Bun version in `download-bun.ts`
- [ ] Icon assets in `electron/assets/`

```

## File: skills\electron-wrapper\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_config_144305-skills-electron-wrapper
name: Electron-Wrapper
path: ecosystem/skills/repo_fetched_agent_config_144305/skills/electron-wrapper
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Electron-Wrapper
Storage area for 'electron-wrapper' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\electron-wrapper\references\build_and_distribute.md
```
# Build & Distribution

Server bundling, Bun binary packaging, CI/CD workflows, code signing, and icon generation.

---

## 1. Server Bundle Script

Bundle the Bun web server into a single file for packaging:

```typescript
// scripts/build-server.ts
import { mkdir, rm } from "fs/promises";
import path from "path";

async function main(): Promise<void> {
  const outDir = path.join(import.meta.dir, "..", "resources", "server");

  await rm(outDir, { recursive: true, force: true });
  await mkdir(outDir, { recursive: true });

  const result = await Bun.build({
    entrypoints: [path.join(import.meta.dir, "..", "src", "index.ts")],
    target: "bun",
    minify: true,
    outdir: outDir,
    define: {
      "process.env.NODE_ENV": JSON.stringify("production"),
    },
  });

  if (!result.success) {
    console.error("Server build failed");
    process.exit(1);
  }

  console.log(`Server bundle written to ${outDir}`);
}

main().catch((error) => {
  console.error("Server build error:", error);
  process.exit(1);
});
```

This produces `resources/server/index.js` — a single file that the bundled Bun binary runs in the packaged app.

---

## 2. Bun Binary Download Script

Downloads platform-specific Bun binaries for bundling into the Electron app:

```typescript
// scripts/download-bun.ts
import { mkdir, unlink } from "fs/promises";
import { existsSync } from "fs";
import path from "path";

const BUN_VERSION = "1.2.5"; // pin to match your dev version

const PLATFORMS = [
  { platform: "darwin", arch: "arm64", file: "bun-darwin-aarch64.zip" },
  { platform: "darwin", arch: "x64", file: "bun-darwin-x64.zip" },
  { platform: "win32", arch: "x64", file: "bun-windows-x64.zip" },
] as const;

const RESOURCES_DIR = path.join(import.meta.dir, "..", "resources", "bun");

async function downloadBun(
  platform: string,
  arch: string,
  file: string,
  force: boolean = false
): Promise<void> {
  const url = `https://github.com/oven-sh/bun/releases/download/bun-v${BUN_VERSION}/${file}`;
  const outDir = path.join(RESOURCES_DIR, `${platform}-${arch}`);
  const zipPath = path.join(outDir, file);
  const bunExecutable = platform === "win32" ? "bun.exe" : "bun";
  const bunPath = path.join(outDir, bunExecutable);

  if (existsSync(bunPath) && !force) {
    console.log(`Bun already exists for ${platform}-${arch}, skipping...`);
    return;
  }

  console.log(`Downloading Bun for ${platform}-${arch}...`);
  await mkdir(outDir, { recursive: true });

  const response = await fetch(url);
  if (!response.ok) throw new Error(`Failed to download: ${response.status}`);

  await Bun.write(zipPath, response);

  // Extract and flatten
  const proc = Bun.spawn(["unzip", "-o", zipPath, "-d", outDir], {
    cwd: outDir,
    stdout: "inherit",
    stderr: "inherit",
  });
  await proc.exited;

  // Move binary from extracted subdirectory to outDir root
  const extractedDir = path.join(outDir, file.replace(".zip", ""));
  const extractedBun = path.join(extractedDir, bunExecutable);

  if (existsSync(extractedBun)) {
    const moveProc = Bun.spawn(["mv", extractedBun, bunPath]);
    await moveProc.exited;
    const rmProc = Bun.spawn(["rm", "-rf", extractedDir]);
    await rmProc.exited;
  }

  await unlink(zipPath);

  if (platform !== "win32") {
    const chmodProc = Bun.spawn(["chmod", "+x", bunPath]);
    await chmodProc.exited;
  }

  console.log(`Bun ready at ${bunPath}`);
}

async function main(): Promise<void> {
  const args = process.argv.slice(2);
  let platforms = PLATFORMS;
  const force = args.includes("--force");

  // --current: download only for the current platform
  if (args.includes("--current")) {
    const currentPlatform = process.platform;
    const currentArch = process.arch === "arm64" ? "arm64" : "x64";
    platforms = PLATFORMS.filter(
      (p) => p.platform === currentPlatform && p.arch === currentArch
    );
  }

  // --platform darwin --arch arm64: for CI cross-builds
  const platformIdx = args.indexOf("--platform");
  const archIdx = args.indexOf("--arch");
  if (platformIdx !== -1 && archIdx !== -1) {
    const targetPlatform = args[platformIdx + 1];
    const targetArch = args[archIdx + 1];
    platforms = PLATFORMS.filter(
      (p) => p.platform === targetPlatform && p.arch === targetArch
    );
  }

  for (const { platform, arch, file } of platforms) {
    await downloadBun(platform, arch, file, force);
  }
}

main().catch((error) => {
  console.error("Error:", error);
  process.exit(1);
});
```

### CLI flags:
- `--current` — download only for current platform/arch (local dev)
- `--platform darwin --arch arm64` — download specific target (CI)
- `--force` — re-download even if binary exists

---

## 3. Package Scripts

### Root package.json

```json
{
  "scripts": {
    "build": "bun run build.ts",
    "build:server": "bun scripts/build-server.ts",
    "download-bun": "bun scripts/download-bun.ts",
    "electron:dev": "cd electron && npm run dev",
    "electron:build": "bun run build:server && cd electron && npm run build",
    "electron:pack": "bun run build && bun run build:server && cd electron && npm run pack",
    "electron:dist": "bun run build && bun run build:server && cd electron && npm run dist"
  }
}
```

### electron/package.json

```json
{
  "scripts": {
    "dev": "concurrently \"npm run dev:web\" \"npm run dev:electron\"",
    "dev:web": "cd .. && bun run dev",
    "dev:electron": "wait-on http://localhost:3005 && npm run build && ELECTRON_DEV_URL=http://localhost:3005 electron .",
    "build": "tsc -p tsconfig.main.json && tsc -p tsconfig.preload.json",
    "pack": "npm run build && electron-builder --dir",
    "dist": "npm run build && electron-builder",
    "dist:mac": "npm run build && electron-builder --mac",
    "dist:win": "npm run build && electron-builder --win"
  }
}
```

Build pipeline: `build web app` → `build server bundle` → `compile electron TS` → `electron-builder packages everything`

---

## 4. GitHub Actions CI Workflow

```yaml
name: Electron Release

on:
  push:
    tags:
      - 'v*'
  workflow_dispatch:
    inputs:
      version:
        description: 'Version to release (without v prefix)'
        required: false

jobs:
  build-mac:
    runs-on: macos-14
    strategy:
      matrix:
        arch: [arm64, x64]
    steps:
      - uses: actions/checkout@v4

      - name: Setup Bun
        uses: oven-sh/setup-bun@v2
        with:
          bun-version: latest

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm
          cache-dependency-path: electron/package-lock.json

      - name: Install web dependencies
        run: bun install

      - name: Build web app
        run: bun run build

      - name: Build server bundle
        run: bun run build:server

      - name: Download Bun binary
        run: bun scripts/download-bun.ts --platform darwin --arch ${{ matrix.arch }}

      - name: Install Electron dependencies
        run: cd electron && npm ci

      - name: Import Apple certificates
        env:
          APPLE_CERTIFICATE: ${{ secrets.APPLE_CERTIFICATE }}
          APPLE_CERTIFICATE_PASSWORD: ${{ secrets.APPLE_CERTIFICATE_PASSWORD }}
        run: |
          echo "$APPLE_CERTIFICATE" | base64 --decode > certificate.p12
          security create-keychain -p "" build.keychain
          security default-keychain -s build.keychain
          security unlock-keychain -p "" build.keychain
          security import certificate.p12 -k build.keychain \
            -P "$APPLE_CERTIFICATE_PASSWORD" -T /usr/bin/codesign
          security set-key-partition-list -S apple-tool:,apple:,codesign: \
            -s -k "" build.keychain
          rm certificate.p12

      - name: Build Electron app
        env:
          APPLE_ID: ${{ secrets.APPLE_ID }}
          APPLE_APP_SPECIFIC_PASSWORD: ${{ secrets.APPLE_PASSWORD }}
          APPLE_TEAM_ID: ${{ secrets.APPLE_TEAM_ID }}
          CSC_KEYCHAIN: build.keychain
        run: |
          cd electron
          npm run dist:mac -- --${{ matrix.arch }} --publish never

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: mac-${{ matrix.arch }}
          path: |
            electron/release/*.dmg
            electron/release/*.zip
            electron/release/*.yml
            electron/release/*.blockmap
          if-no-files-found: error

  build-windows:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4
      - uses: oven-sh/setup-bun@v2
        with:
          bun-version: latest
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm
          cache-dependency-path: electron/package-lock.json

      - run: bun install
      - run: bun run build
      - run: bun run build:server
      - run: bun scripts/download-bun.ts --platform win32 --arch x64
      - run: cd electron && npm ci
      - run: cd electron && npm run dist:win -- --publish never

      - uses: actions/upload-artifact@v4
        with:
          name: windows-x64
          path: |
            electron/release/*.exe
            electron/release/*.yml
            electron/release/*.blockmap
          if-no-files-found: error

  publish:
    needs: [build-mac, build-windows]
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4

      - uses: actions/download-artifact@v4
        with:
          path: artifacts

      - name: Get version
        id: version
        run: |
          if [ "${{ github.event_name }}" = "workflow_dispatch" ] && \
             [ -n "${{ github.event.inputs.version }}" ]; then
            echo "version=${{ github.event.inputs.version }}" >> $GITHUB_OUTPUT
          else
            echo "version=${GITHUB_REF#refs/tags/v}" >> $GITHUB_OUTPUT
          fi

      - name: Create Release
        uses: softprops/action-gh-release@v2
        with:
          name: Your App v${{ steps.version.outputs.version }}
          draft: true
          files: |
            artifacts/**/*.dmg
            artifacts/**/*.zip
            artifacts/**/*.exe
            artifacts/**/*.yml
            artifacts/**/*.blockmap
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Key CI decisions:
- **`--publish never`** — Build locally, upload artifacts, create release in a separate job. This avoids giving build machines GitHub token access.
- **Matrix builds** for macOS arm64/x64 — Both run on `macos-14` (Apple Silicon), cross-compilation handles x64
- **Draft release** — Review before publishing to trigger auto-updater

---

## 5. Code Signing (macOS)

### Prerequisites

1. **Apple Developer account** ($99/year)
2. **Developer ID Application certificate** from Apple Developer portal
3. **App-specific password** for notarization

### Certificate export

1. Open Keychain Access
2. Find "Developer ID Application: Your Name" certificate
3. Right-click → Export → save as `.p12` with a password
4. Base64 encode: `base64 -i certificate.p12 | pbcopy`

### Required GitHub secrets

| Secret | Value |
|--------|-------|
| `APPLE_CERTIFICATE` | Base64-encoded .p12 certificate |
| `APPLE_CERTIFICATE_PASSWORD` | Password used when exporting .p12 |
| `APPLE_ID` | Apple ID email |
| `APPLE_PASSWORD` | App-specific password (not account password) |
| `APPLE_TEAM_ID` | Team ID from Apple Developer portal |

### Local signing test

```bash
# Build with signing (credentials in env)
export APPLE_ID="your@email.com"
export APPLE_APP_SPECIFIC_PASSWORD="xxxx-xxxx-xxxx-xxxx"
export APPLE_TEAM_ID="XXXXXXXXXX"
cd electron && npm run dist:mac
```

---

## 6. Icon Generation

### macOS (.icns)

Use `sips` (built into macOS) and `iconutil`:

```bash
# From a 1024x1024 PNG source
mkdir icon.iconset
sips -z 16 16     app-icon.png --out icon.iconset/icon_16x16.png
sips -z 32 32     app-icon.png --out icon.iconset/icon_16x16@2x.png
sips -z 32 32     app-icon.png --out icon.iconset/icon_32x32.png
sips -z 64 64     app-icon.png --out icon.iconset/icon_32x32@2x.png
sips -z 128 128   app-icon.png --out icon.iconset/icon_128x128.png
sips -z 256 256   app-icon.png --out icon.iconset/icon_128x128@2x.png
sips -z 256 256   app-icon.png --out icon.iconset/icon_256x256.png
sips -z 512 512   app-icon.png --out icon.iconset/icon_256x256@2x.png
sips -z 512 512   app-icon.png --out icon.iconset/icon_512x512.png
sips -z 1024 1024 app-icon.png --out icon.iconset/icon_512x512@2x.png
iconutil -c icns icon.iconset -o app-icon.icns
rm -rf icon.iconset
```

### Windows (.ico)

Use `png-to-ico` (Node.js package, added as devDependency):

```javascript
// electron/scripts/generate-icons.mjs
import fs from "fs/promises";
import path from "path";
import { fileURLToPath } from "url";
import pngToIco from "png-to-ico";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const assetsDir = path.resolve(__dirname, "..", "assets");
const inputPng = path.join(assetsDir, "app-icon.png");
const outputIco = path.join(assetsDir, "icon.ico");

const icoBuffer = await pngToIco(inputPng);
await fs.writeFile(outputIco, icoBuffer);
console.log(`Generated ${outputIco}`);
```

Run with `cd electron && npm run icons`.

### Source icon requirements
- PNG format, 1024x1024px minimum (512x512 acceptable)
- No transparency for macOS (Apple's guidelines)
- Place source at `electron/assets/app-icon.png`

---

## 7. Release Process

1. Update version in both `package.json` and `electron/package.json`
2. Commit: `git commit -m "Bump version to X.Y.Z"`
3. Tag: `git tag vX.Y.Z`
4. Push: `git push && git push --tags`
5. CI builds and creates a draft release with artifacts
6. Review the draft release on GitHub
7. Publish the release — this makes it visible to the auto-updater
8. The auto-updater checks `latest.yml`/`latest-mac.yml` from GitHub Releases

electron-updater uses the `publish.provider: github` config in `electron-builder.yml` to find releases. The `latest*.yml` files (uploaded as release artifacts) tell the updater the current version and download URLs.

```

## File: skills\electron-wrapper\references\main_process.md
```
# Main Process

Annotated implementation patterns for each Electron main process file.

---

## src/main/index.ts — App Entry Point

The entry point handles app lifecycle, dev/production mode switching, single-instance locking, and IPC registration.

```typescript
import path from "path";
import { fileURLToPath } from "url";
import { app, ipcMain } from "electron";
import log from "electron-log";
import { startServer, stopServer } from "./bun-server.js";
import { createWindow, getMainWindow } from "./window.js";
import {
  setupAutoUpdater,
  checkForUpdates,
  downloadUpdate,
  installUpdate,
} from "./updater.js";

log.transports.file.level = "info";
log.info("App starting...");

// ESM __dirname polyfill (see pitfalls §3)
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Dev mode: connect to external dev server instead of spawning Bun
const DEV_SERVER_URL = process.env.ELECTRON_DEV_URL;
const isDev = !!DEV_SERVER_URL;

let appPort: number | null = null;

async function getServerPort(): Promise<number> {
  if (isDev && DEV_SERVER_URL) {
    log.info("Dev mode: connecting to", DEV_SERVER_URL);
    const url = new URL(DEV_SERVER_URL);
    return parseInt(url.port, 10) || 3000;
  }
  return startServer();
}

// Single-instance lock — prevent multiple windows fighting over the server
const gotLock = app.requestSingleInstanceLock();

if (!gotLock) {
  log.info("Another instance is running, quitting...");
  app.quit();
} else {
  // Focus existing window when user tries to open a second instance
  app.on("second-instance", () => {
    const window = getMainWindow();
    if (window) {
      if (window.isMinimized()) window.restore();
      window.focus();
    }
  });

  app.whenReady().then(async () => {
    try {
      appPort = await getServerPort();
      createWindow(appPort);

      // Auto-updater only in packaged builds
      if (app.isPackaged) {
        setupAutoUpdater();
        setTimeout(() => checkForUpdates(), 5000); // delay avoids startup congestion
      }
    } catch (error) {
      log.error("Failed to start app:", error);
      app.quit();
    }
  });

  // macOS: re-create window when dock icon clicked
  app.on("activate", () => {
    if (!getMainWindow() && appPort) {
      createWindow(appPort);
    }
  });

  // Non-macOS: quit when all windows closed
  app.on("window-all-closed", () => {
    if (process.platform !== "darwin") {
      app.quit();
    }
  });

  // Clean up Bun server on quit (skip in dev — we didn't start it)
  app.on("before-quit", () => {
    if (!isDev) {
      stopServer();
    }
  });

  // IPC handlers for renderer → main communication
  ipcMain.handle("update:check", () => checkForUpdates());
  ipcMain.handle("update:download", () => downloadUpdate());
  ipcMain.handle("update:install", () => installUpdate());
  ipcMain.handle("app:version", () => app.getVersion());
}
```

### Key patterns:
- **Dev URL detection** via environment variable — never start the internal server in dev mode (see pitfalls §4)
- **Single-instance lock** prevents port conflicts when user double-launches
- **Store port at app level** — resolve once, reuse in `activate` handler instead of re-entering `startServer()`
- **Delayed update check** (`setTimeout 5s`) avoids competing with app startup
- **IPC handlers** registered at top level, available regardless of window state

---

## src/main/bun-server.ts — Server Spawning

Manages the lifecycle of the bundled Bun server process.

```typescript
import { spawn, type ChildProcess } from "child_process";
import path from "path";
import { app } from "electron";
import log from "electron-log";
import getPort from "get-port";

let serverProcess: ChildProcess | null = null;
let currentPort: number | null = null;

function getBunPath(): string {
  const platform = process.platform;
  const arch = process.arch === "arm64" ? "arm64" : "x64";
  const platformArch = `${platform}-${arch}`;
  const bunExecutable = platform === "win32" ? "bun.exe" : "bun";

  if (app.isPackaged) {
    // In packaged app: resources are in process.resourcesPath
    return path.join(process.resourcesPath, "bun", bunExecutable);
  }

  // In development: resources are relative to electron/ dir
  return path.join(
    app.getAppPath(),
    "..",
    "resources",
    "bun",
    platformArch,
    bunExecutable
  );
}

function getServerPath(): string {
  return path.join(process.resourcesPath, "server", "index.js");
}

export async function startServer(): Promise<number> {
  if (serverProcess) {
    log.info("Server already running on port", currentPort);
    return currentPort!;
  }

  const port = await getPort({ port: [3000, 3001, 3002, 3003, 3004] });
  const bunPath = getBunPath();
  const serverPath = getServerPath();
  const dataDir = app.getPath("userData");

  log.info("Starting Bun server...");
  log.info("Bun path:", bunPath);
  log.info("Server path:", serverPath);
  log.info("Port:", port);

  const staticDir = app.isPackaged
    ? path.join(process.resourcesPath, "dist")
    : path.join(app.getAppPath(), "..", "dist");

  serverProcess = spawn(bunPath, ["run", serverPath, "--port", String(port)], {
    env: {
      ...process.env,
      APP_DATA_DIR: dataDir,         // Persistent storage (see pitfalls §7)
      APP_STATIC_DIR: staticDir,     // Static assets path
      NODE_ENV: "production",
    },
    stdio: ["ignore", "pipe", "pipe"],
  });

  serverProcess.stdout?.on("data", (data) => {
    log.info("[server]", data.toString().trim());
  });

  serverProcess.stderr?.on("data", (data) => {
    log.error("[server]", data.toString().trim());
  });

  serverProcess.on("error", (error) => {
    log.error("Failed to start server:", error);
    serverProcess = null;
    currentPort = null;
  });

  serverProcess.on("exit", (code, signal) => {
    log.info(`Server exited with code ${code}, signal ${signal}`);
    serverProcess = null;
    currentPort = null;
  });

  currentPort = port;
  await waitForServer(port);
  return port;
}

async function waitForServer(
  port: number,
  timeout: number = 30000
): Promise<void> {
  const start = Date.now();
  const url = `http://localhost:${port}`;

  while (Date.now() - start < timeout) {
    try {
      const response = await fetch(url);
      if (response.ok) {
        log.info("Server is ready");
        return;
      }
    } catch {
      // Server not ready yet
    }
    await new Promise((resolve) => setTimeout(resolve, 100));
  }

  throw new Error(`Server failed to start within ${timeout}ms`);
}

export function stopServer(): void {
  if (serverProcess) {
    log.info("Stopping server...");
    serverProcess.kill("SIGTERM");
    serverProcess = null;
    currentPort = null;
  }
}
```

### Key patterns:
- **`getBunPath()`** resolves differently for packaged vs dev — packaged uses `process.resourcesPath`, dev uses relative paths from `app.getAppPath()`
- **`getServerPath()`** only needs the production path — `startServer()` is never called in dev mode (the `ELECTRON_DEV_URL` path skips it)
- **`getPort()`** avoids conflicts by trying a list of preferred ports
- **Environment variables** pass data dir and static dir to the Bun server
- **`waitForServer()`** polls with fetch until the server responds (100ms interval, 30s timeout)
- **`stopServer()`** sends SIGTERM for clean shutdown

---

## src/main/window.ts — Window Management

```typescript
import path from "path";
import { fileURLToPath } from "url";
import { BrowserWindow, shell } from "electron";
import Store from "electron-store";
import log from "electron-log";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

interface WindowBounds {
  x?: number;
  y?: number;
  width: number;
  height: number;
}

const store = new Store<{ windowBounds: WindowBounds }>();
let mainWindow: BrowserWindow | null = null;

export function createWindow(port: number): BrowserWindow {
  const bounds = store.get("windowBounds", {
    width: 1200,
    height: 800,
    x: undefined,
    y: undefined,
  });

  mainWindow = new BrowserWindow({
    ...bounds,
    minWidth: 800,
    minHeight: 600,
    title: "Your App",
    titleBarStyle: process.platform === "darwin" ? "hiddenInset" : "default",
    trafficLightPosition: { x: 16, y: 16 },
    webPreferences: {
      preload: path.join(__dirname, "..", "preload", "index.js"),
      contextIsolation: true,
      nodeIntegration: false,
      sandbox: true,
    },
    show: false,                  // Prevent white flash (see pitfalls §8)
    backgroundColor: "#0a0a0a",   // Match your app's background
  });

  mainWindow.once("ready-to-show", () => {
    mainWindow?.show();
  });

  // Persist window bounds for next launch
  mainWindow.on("close", () => {
    if (mainWindow) {
      store.set("windowBounds", mainWindow.getBounds());
    }
  });

  mainWindow.on("closed", () => {
    mainWindow = null;
  });

  // External links open in default browser
  mainWindow.webContents.setWindowOpenHandler(({ url }) => {
    shell.openExternal(url);
    return { action: "deny" };
  });

  // Prevent navigation away from the app
  mainWindow.webContents.on("will-navigate", (event, url) => {
    const serverUrl = `http://localhost:${port}`;
    if (!url.startsWith(serverUrl)) {
      event.preventDefault();
      shell.openExternal(url);
    }
  });

  mainWindow.loadURL(`http://localhost:${port}`);
  return mainWindow;
}

export function getMainWindow(): BrowserWindow | null {
  return mainWindow;
}
```

### Key patterns:
- **`electron-store`** persists window position/size across launches
- **`titleBarStyle: "hiddenInset"`** on macOS gives the native traffic light buttons with content extending behind the title bar
- **`trafficLightPosition`** offsets the traffic lights to align with your app's header
- **Security config**: `contextIsolation: true`, `nodeIntegration: false`, `sandbox: true` — never weaken these
- **Navigation guards** prevent the window from navigating away from localhost and open external links in the default browser

---

## src/main/updater.ts — Auto-Update

```typescript
import electronUpdater, { type UpdateInfo, type ProgressInfo } from "electron-updater";
import log from "electron-log";
import { getMainWindow } from "./window.js";

// CJS import pattern (see pitfalls §1)
const { autoUpdater } = electronUpdater;

export function setupAutoUpdater(): void {
  autoUpdater.logger = log;
  autoUpdater.autoDownload = false; // let user choose when to download

  autoUpdater.on("checking-for-update", () => {
    sendToRenderer("update:checking");
  });

  autoUpdater.on("update-available", (info: UpdateInfo) => {
    log.info("Update available:", info.version);
    sendToRenderer("update:available", { version: info.version });
  });

  autoUpdater.on("update-not-available", () => {
    sendToRenderer("update:not-available");
  });

  autoUpdater.on("download-progress", (progress: ProgressInfo) => {
    sendToRenderer("update:progress", { percent: progress.percent });
  });

  autoUpdater.on("update-downloaded", (info: UpdateInfo) => {
    log.info("Update downloaded:", info.version);
    sendToRenderer("update:downloaded", { version: info.version });
  });

  autoUpdater.on("error", (error: Error) => {
    log.error("Update error:", error);
    sendToRenderer("update:error", { message: error.message });
  });
}

function sendToRenderer(channel: string, data?: unknown): void {
  const window = getMainWindow();
  if (window) {
    window.webContents.send(channel, data);
  }
}

export function checkForUpdates(): void {
  autoUpdater.checkForUpdates();
}

export function downloadUpdate(): void {
  autoUpdater.downloadUpdate();
}

export function installUpdate(): void {
  autoUpdater.quitAndInstall();
}
```

### Key patterns:
- **`autoDownload: false`** — User-initiated downloads give a better UX than surprise background updates
- **Event flow**: `checking` → `available`/`not-available` → (user clicks download) → `progress` → `downloaded` → (user clicks install) → `quitAndInstall()`
- **`sendToRenderer()`** bridges main → renderer via `webContents.send()`
- The renderer invokes `update:check`, `update:download`, `update:install` via IPC handlers in `index.ts`

---

## src/preload/index.ts — Context Bridge

The preload script exposes a safe API to the renderer via `contextBridge`. It must compile to CommonJS (see pitfalls §2).

```typescript
import { contextBridge, ipcRenderer, type IpcRendererEvent } from "electron";

type IpcHandler<T = void> = (event: IpcRendererEvent, data: T) => void;

const electronAPI = {
  isElectron: true,
  platform: process.platform,
  version: () => ipcRenderer.invoke("app:version") as Promise<string>,

  update: {
    check: () => ipcRenderer.invoke("update:check"),
    download: () => ipcRenderer.invoke("update:download"),
    install: () => ipcRenderer.invoke("update:install"),

    // Each listener returns an unsubscribe function
    onAvailable: (callback: (data: { version: string }) => void) => {
      const handler: IpcHandler<{ version: string }> = (_, data) =>
        callback(data);
      ipcRenderer.on("update:available", handler);
      return () => ipcRenderer.removeListener("update:available", handler);
    },
    onProgress: (callback: (data: { percent: number }) => void) => {
      const handler: IpcHandler<{ percent: number }> = (_, data) =>
        callback(data);
      ipcRenderer.on("update:progress", handler);
      return () => ipcRenderer.removeListener("update:progress", handler);
    },
    onDownloaded: (callback: (data: { version: string }) => void) => {
      const handler: IpcHandler<{ version: string }> = (_, data) =>
        callback(data);
      ipcRenderer.on("update:downloaded", handler);
      return () => ipcRenderer.removeListener("update:downloaded", handler);
    },
    onError: (callback: (data: { message: string }) => void) => {
      const handler: IpcHandler<{ message: string }> = (_, data) =>
        callback(data);
      ipcRenderer.on("update:error", handler);
      return () => ipcRenderer.removeListener("update:error", handler);
    },
  },
};

contextBridge.exposeInMainWorld("electronAPI", electronAPI);
```

### Key patterns:
- **`contextBridge.exposeInMainWorld()`** — The only safe way to expose functionality to the renderer
- **Unsubscribe pattern** — Each `on*` method returns a cleanup function, compatible with React's `useEffect` cleanup
- **`ipcRenderer.invoke()`** for renderer → main (request/response)
- **`ipcRenderer.on()`** for main → renderer (push events)
- Never expose `ipcRenderer` directly — always wrap in specific methods

```

## File: skills\electron-wrapper\references\pitfalls.md
```
# Pitfalls & Gotchas

Every known issue encountered when wrapping a Bun web app in Electron, with symptoms and proven solutions.

---

## 1. ESM vs CJS Module Conflicts

**Problem:** Modern npm packages (`get-port`, `electron-store`) are ESM-only, but Electron's Node.js environment defaults to CommonJS.

**Symptoms:**
```
Error [ERR_REQUIRE_ESM]: require() of ES Module .../get-port/index.js not supported
```

**Solution:** Add `"type": "module"` to `electron/package.json` so Node.js treats `.js` files as ESM:
```json
{
  "type": "module",
  "main": "dist/main/index.js"
}
```

**Gotcha within the gotcha:** Some packages like `electron-updater` are still CJS. When importing from an ESM context, use the default import pattern:
```typescript
// Fails — named import from CJS module in ESM context
import { autoUpdater } from "electron-updater";

// Works — default import, then destructure
import electronUpdater from "electron-updater";
const { autoUpdater } = electronUpdater;
```

---

## 2. Preload Scripts Must Be Bundled as a Single CJS File

**Problem:** Electron's sandboxed preload scripts use a restricted `preloadRequire` that can **only** load built-in Electron modules (`electron`, `events`, `timers`, `url`). Multi-file CJS with relative `require()` calls will fail at runtime — even though `tsc` compiles it successfully.

**Symptoms:**
```
Unable to load preload script: /path/to/preload/index.js
Error: module not found: ../shared/types.js
```
Or, if not using sandbox:
```
SyntaxError: Cannot use import statement outside a module
```

**Solution:** Use **esbuild** to bundle the preload into a single CJS file with `electron` as an external:

```json
{
  "scripts": {
    "build:preload": "esbuild src/preload/index.ts --bundle --platform=node --format=cjs --outfile=dist/preload/index.js --external:electron"
  }
}
```

This inlines all local imports (shared types, constants) into one file while keeping `require("electron")` as a runtime dependency that the sandbox can resolve.

**Why not tsc?** Even with `"module": "CommonJS"` in tsconfig, tsc produces multiple output files with `require("../shared/types.js")` calls. The sandboxed preload's restricted require cannot resolve these paths.

**Keep tsc for type checking only:**
```json
{
  "scripts": {
    "typecheck": "tsc -p tsconfig.main.json --noEmit && tsc -p tsconfig.preload.json --noEmit"
  }
}
```

The preload tsconfig still needs `"module": "CommonJS"` for accurate type checking:
```json
// tsconfig.preload.json
{
  "compilerOptions": {
    "module": "CommonJS",
    "moduleResolution": "Node",
    "outDir": "dist/preload",
    "rootDir": "src"
  }
}
```

The main process tsconfig stays ESM:
```json
// tsconfig.main.json
{
  "compilerOptions": {
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "outDir": "dist/main",
    "rootDir": "src/main"
  }
}
```

---

## 3. `__dirname` Unavailable in ESM

**Problem:** ESM modules don't have `__dirname` or `__filename` globals. Many Electron patterns rely on `__dirname` for resolving paths to preload scripts, assets, and resources.

**Symptoms:**
```
ReferenceError: __dirname is not defined
```

**Solution:** Reconstruct from `import.meta.url`:
```typescript
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
```

Add this polyfill at the top of every main process file that needs path resolution.

---

## 4. Dev Mode MIME Type Errors

**Problem:** Running Electron's internal Bun server alongside the web dev server causes module serving issues. The bundled server serves built assets, not the dev server's HMR-enhanced modules.

**Symptoms:**
```
Failed to load module script: Expected a JavaScript module script but the server responded with a MIME type of "text/html"
```

**Solution:** In dev mode, don't start the internal Bun server. Instead, connect Electron to the external dev server via an environment variable:

```typescript
// main/index.ts
const DEV_SERVER_URL = process.env.ELECTRON_DEV_URL;
const isDev = !!DEV_SERVER_URL;

async function getServerPort(): Promise<number> {
  if (isDev && DEV_SERVER_URL) {
    const url = new URL(DEV_SERVER_URL);
    return parseInt(url.port, 10) || 3000;
  }
  return startServer(); // production: spawn bundled Bun
}
```

Dev script uses `concurrently` + `wait-on`:
```json
{
  "scripts": {
    "dev": "concurrently \"npm run dev:web\" \"npm run dev:electron\"",
    "dev:web": "cd .. && bun run dev",
    "dev:electron": "wait-on http://localhost:3005 && npm run build && ELECTRON_DEV_URL=http://localhost:3005 electron ."
  }
}
```

---

## 5. Bun Version Must Match Features

**Problem:** The bundled Bun binary must support the same APIs your server uses. Older versions may lack features like the `routes` API in `Bun.serve()`.

**Symptoms:**
```
TypeError: Expected fetch() to be a function
```
(Or other cryptic errors from missing API support.)

**Solution:** Pin the Bun version in your download script and keep it aligned with your development version:
```typescript
const BUN_VERSION = "1.2.5"; // must support your server's API surface
```

Re-download when updating:
```bash
bun scripts/download-bun.ts --current --force
```

---

## 6. nvm/Node.js PATH Issues in Spawned Processes

**Problem:** When spawning child processes from Electron or test scripts, `node`/`npm` may not be found if using nvm with lazy shell loading.

**Symptoms:**
```
env: node: No such file or directory
```

**Solution:** For test scripts and build tooling, use `bash -lc` to run commands through a login shell that loads nvm:
```typescript
const proc = spawn({
  cmd: ["bash", "-lc", command],
  cwd: projectDir,
  stdout: "pipe",
  stderr: "pipe",
});
```

This isn't an issue in production since Electron bundles its own Node.js and you bundle the Bun binary.

---

## 7. Storage Paths (CWD Is Wrong in Packaged Apps)

**Problem:** Web apps commonly store data relative to `process.cwd()`, but packaged Electron apps have an unpredictable CWD (often `/` or the app bundle path).

**Symptoms:** Data files written to unexpected locations, data not persisting between launches, or permission errors writing to read-only directories.

**Solution:** Make storage paths configurable via environment variable, defaulting to CWD for web mode:

```typescript
// In your server's storage module
const DATA_DIR = process.env.APP_DATA_DIR || process.cwd();
const DATA_FILE = path.join(DATA_DIR, ".app-data.json");
```

Set the env var when spawning the Bun server from Electron:
```typescript
serverProcess = spawn(bunPath, ["run", serverPath, "--port", String(port)], {
  env: {
    ...process.env,
    APP_DATA_DIR: app.getPath("userData"), // ~/Library/Application Support/AppName
  },
});
```

---

## 8. White Flash on Window Open

**Problem:** BrowserWindow shows a white rectangle before the web content loads, creating a jarring flash — especially in dark-themed apps.

**Symptoms:** Brief white flash visible when launching the app or creating new windows.

**Solution:** Combine three techniques:

```typescript
const mainWindow = new BrowserWindow({
  show: false,                    // 1. Don't show immediately
  backgroundColor: "#0a0a0a",    // 2. Match your app's background color
  // ...
});

mainWindow.once("ready-to-show", () => {
  mainWindow.show();             // 3. Show only when content is painted
});
```

Choose a `backgroundColor` that matches your app's default theme (dark or light).

---

## 9. Dev Server Port Mismatch

**Problem:** Electron's dev URL defaults to `localhost:3000`, but the web app's dev server may run on a different port (configured in `package.json` or `.env`).

**Symptoms:**
```
Failed to load URL: http://localhost:3000/login with error: ERR_CONNECTION_REFUSED
```

**Solution:** Before setting constants, check the web app's actual dev port in its `package.json` dev script or `.env` file. Common patterns:
```json
"dev": "next dev -p 3010"
"dev": "vite --port 5173"
```

Match this in Electron's constants:
```typescript
export const URLS = {
  PRODUCTION: "https://www.yourapp.com",
  DEVELOPMENT: "http://localhost:3010", // Must match web app's dev port
};
```

---

## 10. Do NOT Use BrowserView

**Problem:** `BrowserView` was deprecated in Electron 30 and removed in later versions. It also doesn't receive the preload script from the parent BrowserWindow, so `window.electron` will be undefined.

**Symptoms:** `window.electron` is undefined in the web app even though the preload compiles correctly. Or deprecation warnings/errors on newer Electron versions.

**Solution:** Load the web app URL directly in the `BrowserWindow` via `mainWindow.loadURL()`. The BrowserWindow already has the preload configured in its `webPreferences`, so `contextBridge.exposeInMainWorld()` works correctly.

```typescript
// Wrong — BrowserView doesn't inherit preload from parent window
const view = new BrowserView({ webPreferences: { /* no preload */ } });
mainWindow.setBrowserView(view);
view.webContents.loadURL(appUrl);

// Right — load directly in the BrowserWindow
mainWindow.loadURL(appUrl);
```

---

## 11. electron-builder `${platform}` !== Node.js `process.platform`

**Problem:** electron-builder's `${platform}` macro resolves to `mac`/`linux`/`win`, but Node.js (and the Bun download script) uses `darwin`/`linux`/`win32`. If you use `${platform}` in `extraResources` paths for the Bun binary, the path won't match the actual directory and the binary silently won't be bundled.

**Symptoms:**
```
Error: spawn /Applications/Your App.app/Contents/Resources/bun/bun ENOENT
```
The app starts, tries to spawn the Bun server, but the binary is missing from the packaged app. Locally-built dev mode works fine since it uses a different code path.

**Solution:** Put the Bun `extraResources` entry in platform-specific sections with hardcoded platform prefixes:

```yaml
# Wrong — ${platform} resolves to "mac", not "darwin"
extraResources:
  - from: ../resources/bun/${platform}-${arch}/
    to: bun/

# Right — use platform-specific sections with correct prefixes
mac:
  extraResources:
    - from: ../resources/bun/darwin-${arch}/
      to: bun/

win:
  extraResources:
    - from: ../resources/bun/win32-${arch}/
      to: bun/
```

Platform-independent resources (server bundle, web app dist) can stay in the top-level `extraResources`.

---

## 12. Bun Workspaces Hoist Dependencies Away from electron-builder

**Problem:** If the Electron directory is a workspace in a Bun monorepo, Bun hoists all dependencies to the root `node_modules/`. electron-builder expects production deps in `electron/node_modules/` and won't find them. Even if you manually whitelist packages in the `files` section, you'll miss transitive dependencies and get `ERR_MODULE_NOT_FOUND` at runtime.

**Symptoms:**
```
Error [ERR_MODULE_NOT_FOUND]: Cannot find package 'ajv-formats' imported from .../conf/dist/source/index.js
```
The app builds without error, but crashes on launch because a transitive dependency (e.g., `ajv-formats` needed by `conf` needed by `electron-store`) is missing from the packaged app.

**Solution A (recommended for Bun workspaces):** Bundle the main process with esbuild, inlining all dependencies. No `node_modules` needed in the packaged app:

```json
{
  "scripts": {
    "build:main": "esbuild src/main/index.ts --bundle --platform=node --format=esm --outfile=dist/main/main/index.js --external:electron --banner:js=\"import { createRequire } from 'module'; var require = createRequire(import.meta.url);\"",
    "build:preload": "esbuild src/preload/index.ts --bundle --platform=node --format=cjs --outfile=dist/preload/preload/index.js --external:electron"
  }
}
```

The `createRequire` banner is essential — CJS packages like `electron-log` use `require("electron")` internally, which fails in ESM output without a real `require` function. The banner provides one via Node's `module.createRequire`.

With this approach, `electron-builder.yml` excludes all node_modules:
```yaml
files:
  - dist/**/*
  - assets/**/*
  - "!node_modules"
```

**Solution B (recommended for standalone Electron projects):** Use npm (not Bun) for the Electron directory so deps stay in `electron/node_modules/`. Use `tsc` for the main process and `files: - dist/**/*` in electron-builder.yml — electron-builder handles production deps automatically.

**Why not whitelist node_modules?** A manual whitelist like `node_modules/electron-store/**/*` is fragile — it misses transitive deps and breaks silently whenever a dependency updates its dependency tree.

---

## 13. Never Build Release Artifacts Locally

**Problem:** Running `electron-builder --publish always` or `gh release create` with locally-built artifacts produces apps that aren't notarized. macOS Gatekeeper will block them with "Apple could not verify" errors.

**Symptoms:**
- Build log shows `skipped macOS notarization  reason=notarize options were unable to be generated`
- Downloaded app shows "Apple could not verify" dialog
- Users can't open the app without `xattr -cr`

**Solution:** Always cut releases through CI. The correct workflow:

1. Bump version in `electron/package.json`, commit, merge to main
2. Find the CI workflow's tag pattern: `grep -A2 'tags:' .github/workflows/*.yml`
3. Tag the merged commit on main: `git tag <pattern><version> origin/main`
4. Push the tag: `git push origin <tag>`
5. Monitor CI: `gh run list --workflow=<workflow>.yml --limit=1`
6. Review the draft release on GitHub, then publish

CI has the signing certificates (`APPLE_CERTIFICATE`), notarization credentials (`APPLE_ID`, `APPLE_PASSWORD`, `APPLE_TEAM_ID`), and publish tokens that local machines don't have.

```

## File: skills\electron-wrapper\references\project_setup.md
```
# Project Setup

How to set up the Electron subproject alongside an existing Bun web app.

---

## Directory Structure

Create an `electron/` directory at the root of your project:

```
your-app/
├── electron/
│   ├── package.json
│   ├── package-lock.json
│   ├── tsconfig.main.json
│   ├── tsconfig.preload.json
│   ├── electron-builder.yml
│   ├── entitlements.mac.plist
│   ├── assets/
│   │   ├── app-icon.png          (512x512+ source icon)
│   │   ├── app-icon.icns         (generated for macOS)
│   │   └── icon.ico              (generated for Windows)
│   ├── src/
│   │   ├── main/
│   │   │   ├── index.ts          (app entry point)
│   │   │   ├── bun-server.ts     (server spawning)
│   │   │   ├── window.ts         (window management)
│   │   │   └── updater.ts        (auto-update)
│   │   └── preload/
│   │       └── index.ts          (context bridge)
│   └── scripts/
│       └── generate-icons.mjs    (icon generation)
├── scripts/
│   ├── build-server.ts           (Bun.build() for server bundle)
│   └── download-bun.ts           (Bun binary downloader)
├── resources/
│   ├── bun/
│   │   ├── darwin-arm64/bun
│   │   ├── darwin-x64/bun
│   │   └── win32-x64/bun.exe
│   └── server/
│       └── index.js              (bundled server output)
├── dist/                          (web app build output)
├── src/                           (your existing web app)
└── package.json
```

---

## electron/package.json

Use **npm** (not Bun) for the Electron subproject. Bun's module resolution conflicts with electron-builder's packaging expectations.

```json
{
  "name": "your-app-electron",
  "version": "0.1.0",
  "private": true,
  "repository": "github:your-org/your-app",
  "type": "module",
  "main": "dist/main/index.js",
  "scripts": {
    "dev": "concurrently \"npm run dev:web\" \"npm run dev:electron\"",
    "dev:web": "cd .. && bun run dev",
    "dev:electron": "wait-on http://localhost:3005 && npm run build && ELECTRON_DEV_URL=http://localhost:3005 electron .",
    "build": "tsc -p tsconfig.main.json && esbuild src/preload/index.ts --bundle --platform=node --format=cjs --outfile=dist/preload/index.js --external:electron",
    "icons": "node scripts/generate-icons.mjs",
    "pack": "npm run build && electron-builder --dir",
    "dist": "npm run build && electron-builder",
    "dist:mac": "npm run build && electron-builder --mac",
    "dist:win": "npm run build && electron-builder --win"
  },
  "dependencies": {
    "electron-log": "^5.2.4",
    "electron-store": "^10.0.0",
    "electron-updater": "^6.3.9",
    "get-port": "^7.1.0"
  },
  "devDependencies": {
    "concurrently": "^9.1.2",
    "electron": "^33.2.0",
    "electron-builder": "^25.1.8",
    "esbuild": "^0.27.3",
    "png-to-ico": "^3.0.0",
    "typescript": "^5.8.3",
    "wait-on": "^8.0.3"
  }
}
```

Key decisions:
- **`"type": "module"`** — Required so Node.js treats compiled `.js` as ESM (see pitfalls §1)
- **`"repository"`** — Required by electron-builder for GitHub releases publish provider
- **`"main"`** — Points to compiled entry point
- **npm, not Bun** — electron-builder expects npm-style `node_modules` layout

---

## TypeScript Configs

Two separate configs are required because the main process uses ESM while preload scripts must be CJS (see pitfalls §2).

### tsconfig.main.json (ESM)

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "lib": ["ES2022"],
    "outDir": "dist/main",
    "rootDir": "src/main",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "declaration": false,
    "declarationMap": false,
    "sourceMap": true
  },
  "include": ["src/main/**/*"]
}
```

### tsconfig.preload.json (CommonJS)

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "CommonJS",
    "moduleResolution": "Node",
    "lib": ["ES2022", "DOM"],
    "outDir": "dist/preload",
    "rootDir": "src/preload",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "declaration": false,
    "declarationMap": false,
    "sourceMap": true
  },
  "include": ["src/preload/**/*"]
}
```

Note `"lib"` includes `"DOM"` for preload (it runs in renderer context) but not for main.

---

## electron-builder.yml

```yaml
appId: com.your-org.your-app
productName: Your App
copyright: Copyright © 2025

directories:
  output: release
  buildResources: assets

files:
  - dist/**/*

extraResources:
  - from: ../resources/server/
    to: server/
  - from: ../dist/
    to: dist/

mac:
  extraResources:
    - from: ../resources/bun/darwin-${arch}/
      to: bun/
  icon: assets/app-icon.icns
  category: public.app-category.utilities
  target:
    - target: dmg
      arch:
        - arm64
        - x64
    - target: zip
      arch:
        - arm64
        - x64
  hardenedRuntime: true
  gatekeeperAssess: false
  entitlements: entitlements.mac.plist
  entitlementsInherit: entitlements.mac.plist
  notarize: true

dmg:
  sign: false
  contents:
    - x: 130
      y: 220
    - x: 410
      y: 220
      type: link
      path: /Applications

win:
  extraResources:
    - from: ../resources/bun/win32-${arch}/
      to: bun/
  icon: assets/icon.ico
  target:
    - target: nsis
      arch:
        - x64
  artifactName: ${productName}-${version}-${arch}.${ext}

nsis:
  oneClick: false
  perMachine: false
  allowToChangeInstallationDirectory: true
  deleteAppDataOnUninstall: false

publish:
  provider: github
  releaseType: draft
```

Key points:
- **`extraResources`** bundles the Bun binary, server bundle, and web app build into the packaged app
- **Bun binary paths use platform-specific sections** — electron-builder's `${platform}` resolves to `mac`/`win`, NOT `darwin`/`win32`. Since the download script uses Node.js platform names (`darwin`, `win32`), the bun `extraResources` entry must go in platform-specific `mac:`/`win:` sections with hardcoded platform prefixes instead of using `${platform}`
- **`notarize: true`** requires Apple credentials in environment (see build-and-distribute.md)
- **`dmg.sign: false`** — DMG signing is unnecessary and can cause issues

---

## entitlements.mac.plist

Required for macOS code signing. The Bun runtime needs JIT and unsigned memory permissions:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>com.apple.security.cs.allow-jit</key>
    <true/>
    <key>com.apple.security.cs.allow-unsigned-executable-memory</key>
    <true/>
    <key>com.apple.security.network.client</key>
    <true/>
    <key>com.apple.security.network.server</key>
    <true/>
</dict>
</plist>
```

- **allow-jit** and **allow-unsigned-executable-memory** — Required because the bundled Bun binary uses JIT compilation
- **network.client** and **network.server** — The app runs a local server and makes outbound API calls

---

## Parent Project Changes

### package.json scripts

Add these scripts to the root `package.json`:

```json
{
  "scripts": {
    "build:server": "bun scripts/build-server.ts",
    "download-bun": "bun scripts/download-bun.ts",
    "electron:dev": "cd electron && npm run dev",
    "electron:build": "bun run build:server && cd electron && npm run build",
    "electron:pack": "bun run build && bun run build:server && cd electron && npm run pack",
    "electron:dist": "bun run build && bun run build:server && cd electron && npm run dist"
  }
}
```

### tsconfig.json excludes

Exclude Electron and script directories from your web app's TypeScript config:

```json
{
  "exclude": ["electron", "scripts", "resources"]
}
```

### .gitignore additions

```gitignore
# Electron
electron/dist/
electron/release/
electron/node_modules/
resources/bun/
resources/server/
```

The `resources/` directories contain large binaries and build artifacts that should not be committed.

```

## File: skills\electron-wrapper\references\web_adaptation.md
```
# Web App Adaptation

Changes to the existing web app to support running inside Electron while remaining fully functional as a standalone web app.

---

## 1. Electron Detection Utility

Create a utility module for Electron detection. All checks are optional-chained so they're safe in browser environments.

```typescript
// src/lib/electron.ts

type ElectronPlatform = "darwin" | "win32" | "linux" | string;

export function isElectron(): boolean {
  return Boolean(window?.electronAPI?.isElectron);
}

export function getElectronPlatform(): ElectronPlatform | null {
  return window?.electronAPI?.platform ?? null;
}

export function isMacElectron(): boolean {
  return isElectron() && getElectronPlatform() === "darwin";
}

export function applyElectronDocumentAttributes(): void {
  if (!isElectron()) return;
  const platform = getElectronPlatform();
  const root = document.documentElement;
  root.dataset.electron = "true";
  if (platform) {
    root.dataset.platform = platform;
  }
}
```

Call `applyElectronDocumentAttributes()` at app startup (e.g., in your entry file before React renders). This sets `data-electron="true"` and `data-platform="darwin"` on `<html>`, enabling CSS targeting.

---

## 2. Type Declarations

Declare the `window.electronAPI` shape with all properties optional so TypeScript doesn't complain in browser environments:

```typescript
// src/types/electron.d.ts

export {};

declare global {
  interface Window {
    electronAPI?: {
      isElectron?: boolean;
      platform?: string;
      version?: () => Promise<string>;
      update?: {
        check?: () => Promise<void>;
        download?: () => Promise<void>;
        install?: () => Promise<void>;
        onAvailable?: (
          callback: (data: { version: string }) => void
        ) => () => void;
        onProgress?: (
          callback: (data: { percent: number }) => void
        ) => () => void;
        onDownloaded?: (
          callback: (data: { version: string }) => void
        ) => () => void;
        onError?: (
          callback: (data: { message: string }) => void
        ) => () => void;
      };
    };
  }
}
```

Every property is optional (`?`) so `window.electronAPI?.update?.download?.()` works safely in both contexts.

---

## 3. CSS Drag Regions

Electron's frameless/hidden-inset title bar requires explicit CSS regions for window dragging.

### CSS utility classes

If using Tailwind CSS 4, add `@utility` rules in your globals.css:

```css
@utility drag {
  -webkit-app-region: drag;
}

@utility no-drag {
  -webkit-app-region: no-drag;
}
```

For plain CSS or older Tailwind:

```css
.app-window-drag {
  -webkit-app-region: drag;
}

.app-window-no-drag {
  -webkit-app-region: no-drag;
}
```

### Applying drag regions in components

Add the drag class to your app's header/toolbar areas when in Electron. Mark interactive children as no-drag:

```tsx
<header className={clsx(
  "flex shrink-0 items-center px-4 border-b",
  isElectron() && "drag",
  isMacElectron() ? "h-auto pb-3 pt-7" : "h-12",
)}>
  <div className="no-drag">
    <Logo />
  </div>
  <nav className="no-drag">
    <FilterTabs />
  </nav>
</header>
```

### Traffic light clearance (macOS)

**Prefer a taller header over left padding.** With `titleBarStyle: "hiddenInset"` and `trafficLightPosition: { x: 16, y: 12 }`, the traffic light buttons occupy roughly y=12 to y=24. Instead of adding `padding-left: 72px` to dodge them horizontally, make the header tall enough so content sits below them:

```tsx
// Good — taller header, content below traffic lights
isMacElectron() ? "h-auto pb-3 pt-7" : "h-12"

// Avoid — left padding wastes horizontal space in narrow windows
isMacElectron() ? "pl-[72px]" : ""
```

This approach works better for narrow/compact windows where horizontal space is at a premium.

### Dialog backdrop dragging

Make dialog backdrops draggable so users can still drag the window when a modal is open, but mark the dialog content as non-draggable:

```tsx
// In your Dialog component
<DialogBackdrop className={clsx("dialog-backdrop", isElectron() && "drag")} />
<DialogPopup className="no-drag">
  {children}
</DialogPopup>
```

---

## 4. Storage Path Adaptation

Make your server's data directory configurable via environment variable so Electron can redirect storage to `userData`:

```typescript
// In your server's storage module
const DATA_DIR = process.env.APP_DATA_DIR || process.cwd();
const DATA_FILE = path.join(DATA_DIR, ".app-data.json");
```

The Bun server process receives `APP_DATA_DIR` from Electron's main process (see main-process.md §bun-server). In web mode, it falls back to `process.cwd()`.

Namespace the env var per project (e.g., `MY_APP_DATA_DIR`) to avoid conflicts.

---

## 5. Static Asset Serving in Production

In production mode, the Bun server needs to serve the built web assets (HTML, JS, CSS). The static directory path comes from an environment variable since the packaged app's file layout differs from development.

```typescript
// In your server's request handler
const STATIC_DIR = process.env.APP_STATIC_DIR;

// Serve static files from the build output
if (STATIC_DIR) {
  const filePath = path.join(STATIC_DIR, url.pathname);
  const resolved = path.resolve(filePath);

  // Security: prevent directory traversal
  if (resolved.startsWith(path.resolve(STATIC_DIR))) {
    const file = Bun.file(resolved);
    if (await file.exists()) {
      return new Response(file);
    }
  }
}
```

In development, the dev server handles this automatically with HMR.

---

## 6. Auto-Update UI

### useElectronUpdater hook

A React hook that subscribes to update events from the preload bridge:

```tsx
type UpdateStatus = "available" | "downloading" | "ready";

function useElectronUpdater(devOverride: UpdateStatus | null) {
  const [status, setStatus] = useState<UpdateStatus | null>(null);
  const [version, setVersion] = useState<string | null>(null);
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    if (!isElectron()) return;
    const api = window.electronAPI?.update;
    if (!api) return;

    const unsubs: (() => void)[] = [];

    if (api.onAvailable) {
      unsubs.push(
        api.onAvailable((data) => {
          setVersion(data.version);
          setStatus("available");
        })
      );
    }
    if (api.onProgress) {
      unsubs.push(
        api.onProgress((data) => {
          setStatus("downloading");
          setProgress(Math.round(data.percent));
        })
      );
    }
    if (api.onDownloaded) {
      unsubs.push(api.onDownloaded(() => setStatus("ready")));
    }
    if (api.onError) {
      unsubs.push(
        api.onError((data) => {
          console.error("Auto-update error:", data.message);
          setStatus(null);
        })
      );
    }

    return () => unsubs.forEach((fn) => fn());
  }, []);

  // Allow dev tools to override the state for testing
  const effective = devOverride ?? status;
  if (!effective) return null;

  return {
    status: effective,
    version: devOverride ? "0.0.0-dev" : version,
    progress: devOverride === "downloading" ? 42 : progress,
    download: () => window.electronAPI?.update?.download?.(),
    install: () => window.electronAPI?.update?.install?.(),
  };
}
```

### Update notification component

A minimal pill-shaped notification that appears when an update is available:

```tsx
function UpdatePill({ updater }: { updater: NonNullable<ReturnType<typeof useElectronUpdater>> }) {
  return (
    <div className="update-pill">
      {updater.status === "available" && (
        <>
          <span>v{updater.version} available</span>
          <button onClick={updater.download}>Update</button>
        </>
      )}
      {updater.status === "downloading" && (
        <span>Downloading... {updater.progress}%</span>
      )}
      {updater.status === "ready" && (
        <>
          <span>Update ready</span>
          <button onClick={updater.install}>Restart</button>
        </>
      )}
    </div>
  );
}
```

### DevTools override for testing

Add a keyboard shortcut (e.g., Shift+U) that cycles through update states for testing the UI without a real update:

```tsx
function DevTools() {
  const [updateOverride, setUpdateOverride] = useState<UpdateStatus | null>(null);

  useHotkeys("shift+u", () => {
    setUpdateOverride((prev) => {
      if (prev === null) return "available";
      if (prev === "available") return "downloading";
      if (prev === "downloading") return "ready";
      return null;
    });
  });

  // Pass updateOverride to useElectronUpdater
}
```

---

## 7. Environment-Based Feature Gating

Use `isElectron()` to gate features that only make sense in one context:

```typescript
// Demo mode doesn't apply in Electron (user has their own data)
export function resolveDemoMode(): boolean {
  if (isElectron()) return false;
  // ... web-specific demo logic
}

// "Hosted environment" features (analytics, etc.) don't apply in Electron
export function isHostedEnvironment(): boolean {
  if (isElectron()) return false;
  // ... check for hosted domain
}
```

The general principle: Electron users have the app installed locally with their own data, so hosted/demo/marketing features should be disabled.

```

## File: skills\electron-wrapper\references\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_config_144305-skills-electron-wrapper-references
name: References
path: ecosystem/skills/repo_fetched_agent_config_144305/skills/electron-wrapper/references
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# References
Storage area for 'references' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\favicon\SKILL.md
```
---
name: favicon
description: Generate a complete set of favicons from a source image and update HTML. Use when setting up favicons for a web project.
argument-hint: [path to source image]
---

Generate a complete set of favicons from the source image at `$1` and update the project's HTML with the appropriate link tags.

## Prerequisites

First, verify ImageMagick v7+ is installed by running:
```bash
which magick
```

If not found, stop and instruct the user to install it:
- **macOS**: `brew install imagemagick`
- **Linux**: `sudo apt install imagemagick`

## Step 1: Validate Source Image

1. Verify the source image exists at the provided path: `$1`
2. Check the file extension is a supported format (PNG, JPG, JPEG, SVG, WEBP, GIF)
3. If the file doesn't exist or isn't a valid image format, report the error and stop

Note whether the source is an SVG file - if so, it will also be copied as `favicon.svg`.

## Step 2: Detect Project Type and Static Assets Directory

Detect the project type and determine where static assets should be placed. Check in this order:

| Framework | Detection | Static Assets Directory |
|-----------|-----------|------------------------|
| **Rails** | `config/routes.rb` exists | `public/` |
| **Next.js** | `next.config.*` exists | `public/` |
| **Gatsby** | `gatsby-config.*` exists | `static/` |
| **SvelteKit** | `svelte.config.*` exists | `static/` |
| **Astro** | `astro.config.*` exists | `public/` |
| **Hugo** | `hugo.toml` or `config.toml` with Hugo markers | `static/` |
| **Jekyll** | `_config.yml` with Jekyll markers | Root directory (same as `index.html`) |
| **Vite** | `vite.config.*` exists | `public/` |
| **Create React App** | `package.json` has `react-scripts` dependency | `public/` |
| **Vue CLI** | `vue.config.*` exists | `public/` |
| **Angular** | `angular.json` exists | `src/assets/` |
| **Eleventy** | `.eleventy.js` or `eleventy.config.*` exists | Check `_site` output or root |
| **Static HTML** | `index.html` in root | Same directory as `index.html` |

**Important**: If existing favicon files are found (e.g., `favicon.ico`, `apple-touch-icon.png`), use their location as the target directory regardless of framework detection.

Report the detected project type and the static assets directory that will be used.

**When in doubt, ask**: If you are not 100% confident about where static assets should be placed (e.g., ambiguous project structure, multiple potential locations, unfamiliar framework), use `AskUserQuestionTool` to confirm the target directory before proceeding. It's better to ask than to put files in the wrong place.

## Step 3: Determine App Name

Find the app name from these sources (in priority order):

1. **Existing `site.webmanifest`** - Check the detected static assets directory for an existing manifest and extract the `name` field
2. **`package.json`** - Extract the `name` field if it exists
3. **Rails `config/application.rb`** - Extract the module name (e.g., `module MyApp` → "MyApp")
4. **Directory name** - Use the current working directory name as fallback

Convert the name to title case if needed (e.g., "my-app" → "My App").

## Step 4: Ensure Static Assets Directory Exists

Check if the detected static assets directory exists. If not, create it.

## Step 5: Generate Favicon Files

Run these ImageMagick commands to generate all favicon files. Replace `[STATIC_DIR]` with the detected static assets directory from Step 2.

### favicon.ico (multi-resolution: 16x16, 32x32, 48x48)
```bash
magick "$1" \
  \( -clone 0 -resize 16x16 \) \
  \( -clone 0 -resize 32x32 \) \
  \( -clone 0 -resize 48x48 \) \
  -delete 0 -alpha on -background none \
  [STATIC_DIR]/favicon.ico
```

### favicon-96x96.png
```bash
magick "$1" -resize 96x96 -background none -alpha on [STATIC_DIR]/favicon-96x96.png
```

### apple-touch-icon.png (180x180)
```bash
magick "$1" -resize 180x180 -background none -alpha on [STATIC_DIR]/apple-touch-icon.png
```

### web-app-manifest-192x192.png
```bash
magick "$1" -resize 192x192 -background none -alpha on [STATIC_DIR]/web-app-manifest-192x192.png
```

### web-app-manifest-512x512.png
```bash
magick "$1" -resize 512x512 -background none -alpha on [STATIC_DIR]/web-app-manifest-512x512.png
```

### favicon.svg (only if source is SVG)
If the source file has a `.svg` extension, copy it:
```bash
cp "$1" [STATIC_DIR]/favicon.svg
```

## Step 6: Create/Update site.webmanifest

Create or update `[STATIC_DIR]/site.webmanifest` with this content (substitute the detected app name):

```json
{
  "name": "[APP_NAME]",
  "short_name": "[APP_NAME]",
  "icons": [
    {
      "src": "/web-app-manifest-192x192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "maskable"
    },
    {
      "src": "/web-app-manifest-512x512.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "maskable"
    }
  ],
  "theme_color": "#ffffff",
  "background_color": "#ffffff",
  "display": "standalone"
}
```

If `site.webmanifest` already exists in the static directory, preserve the existing `theme_color`, `background_color`, and `display` values while updating the `name`, `short_name`, and `icons` array.

## Step 7: Update HTML/Layout Files

Based on the detected project type, update the appropriate file. Adjust the `href` paths based on where the static assets directory is relative to the web root:
- If static files are in `public/` or `static/` and served from root → use `/favicon.ico`
- If static files are in `src/assets/` → use `/assets/favicon.ico`
- If static files are in the same directory as HTML → use `./favicon.ico` or just `favicon.ico`

### For Rails Projects

Edit `app/views/layouts/application.html.erb`. Find the `<head>` section and add/replace favicon-related tags with:

```html
<link rel="icon" type="image/png" href="/favicon-96x96.png" sizes="96x96" />
<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
<link rel="shortcut icon" href="/favicon.ico" />
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
<meta name="apple-mobile-web-app-title" content="[APP_NAME]" />
<link rel="manifest" href="/site.webmanifest" />
```

**Important**:
- If the source was NOT an SVG, omit the `<link rel="icon" type="image/svg+xml" href="/favicon.svg" />` line
- Remove any existing `<link rel="icon"`, `<link rel="shortcut icon"`, `<link rel="apple-touch-icon"`, or `<link rel="manifest"` tags before adding the new ones
- Place these tags near the top of the `<head>` section, after `<meta charset>` and `<meta name="viewport">` if present

### For Next.js Projects

Edit the detected layout file (`app/layout.tsx` or `src/app/layout.tsx`). Update or add the `metadata` export to include icons configuration:

```typescript
export const metadata: Metadata = {
  // ... keep existing metadata fields
  icons: {
    icon: [
      { url: '/favicon.ico' },
      { url: '/favicon-96x96.png', sizes: '96x96', type: 'image/png' },
      { url: '/favicon.svg', type: 'image/svg+xml' },
    ],
    shortcut: '/favicon.ico',
    apple: '/apple-touch-icon.png',
  },
  manifest: '/site.webmanifest',
  appleWebApp: {
    title: '[APP_NAME]',
  },
};
```

**Important**:
- If the source was NOT an SVG, omit the `{ url: '/favicon.svg', type: 'image/svg+xml' }` entry from the icon array
- If metadata export doesn't exist, create it with just the icons-related fields
- If metadata export exists, merge the icons configuration with existing fields

### For Static HTML Projects

Edit the detected `index.html` file. Add the same HTML as Rails within the `<head>` section.

### If No Project Detected

Skip HTML updates and inform the user they need to manually add the following to their HTML `<head>`:

```html
<link rel="icon" type="image/png" href="/favicon-96x96.png" sizes="96x96" />
<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
<link rel="shortcut icon" href="/favicon.ico" />
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
<meta name="apple-mobile-web-app-title" content="[APP_NAME]" />
<link rel="manifest" href="/site.webmanifest" />
```

## Step 8: Summary

Report completion with:
- Detected project type and framework
- Static assets directory used
- List of files generated
- App name used in manifest and HTML
- Layout file updated (or note if manual update is needed)
- Note if any existing files were overwritten

## Error Handling

- If ImageMagick is not installed, provide installation instructions and stop
- If the source image doesn't exist, report the exact path that was tried and stop
- If ImageMagick commands fail, report the specific error message
- If the layout file cannot be found for HTML updates, generate files anyway and instruct on manual HTML addition

```

## File: skills\favicon\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_config_144305-skills-favicon
name: Favicon
path: ecosystem/skills/repo_fetched_agent_config_144305/skills/favicon
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Favicon
Storage area for 'favicon' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\find-skills\SKILL.md
```
---
name: find-skills
description: Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in extending capabilities. This skill should be used when the user is looking for functionality that might exist as an installable skill.
---

# Find Skills

This skill helps you discover and install skills from the open agent skills ecosystem.

## When to Use This Skill

Use this skill when the user:

- Asks "how do I do X" where X might be a common task with an existing skill
- Says "find a skill for X" or "is there a skill for X"
- Asks "can you do X" where X is a specialized capability
- Expresses interest in extending agent capabilities
- Wants to search for tools, templates, or workflows
- Mentions they wish they had help with a specific domain (design, testing, deployment, etc.)

## What is the Skills CLI?

The Skills CLI (`npx skills`) is the package manager for the open agent skills ecosystem. Skills are modular packages that extend agent capabilities with specialized knowledge, workflows, and tools.

**Key commands:**

- `npx skills find [query]` - Search for skills interactively or by keyword
- `npx skills add <package>` - Install a skill from GitHub or other sources
- `npx skills check` - Check for skill updates
- `npx skills update` - Update all installed skills

**Browse skills at:** https://skills.sh/

## How to Help Users Find Skills

### Step 1: Understand What They Need

When a user asks for help with something, identify:

1. The domain (e.g., React, testing, design, deployment)
2. The specific task (e.g., writing tests, creating animations, reviewing PRs)
3. Whether this is a common enough task that a skill likely exists

### Step 2: Search for Skills

Run the find command with a relevant query:

```bash
npx skills find [query]
```

For example:

- User asks "how do I make my React app faster?" → `npx skills find react performance`
- User asks "can you help me with PR reviews?" → `npx skills find pr review`
- User asks "I need to create a changelog" → `npx skills find changelog`

The command will return results like:

```
Install with npx skills add <owner/repo@skill>

vercel-labs/agent-skills@vercel-react-best-practices
└ https://skills.sh/vercel-labs/agent-skills/vercel-react-best-practices
```

### Step 3: Present Options to the User

When you find relevant skills, present them to the user with:

1. The skill name and what it does
2. The install command they can run
3. A link to learn more at skills.sh

Example response:

```
I found a skill that might help! The "vercel-react-best-practices" skill provides
React and Next.js performance optimization guidelines from Vercel Engineering.

To install it:
npx skills add vercel-labs/agent-skills@vercel-react-best-practices

Learn more: https://skills.sh/vercel-labs/agent-skills/vercel-react-best-practices
```

### Step 4: Offer to Install

If the user wants to proceed, you can install the skill for them:

```bash
npx skills add <owner/repo@skill> -g -y
```

The `-g` flag installs globally (user-level) and `-y` skips confirmation prompts.

## Common Skill Categories

When searching, consider these common categories:

| Category        | Example Queries                          |
| --------------- | ---------------------------------------- |
| Web Development | react, nextjs, typescript, css, tailwind |
| Testing         | testing, jest, playwright, e2e           |
| DevOps          | deploy, docker, kubernetes, ci-cd        |
| Documentation   | docs, readme, changelog, api-docs        |
| Code Quality    | review, lint, refactor, best-practices   |
| Design          | ui, ux, design-system, accessibility     |
| Productivity    | workflow, automation, git                |

## Tips for Effective Searches

1. **Use specific keywords**: "react testing" is better than just "testing"
2. **Try alternative terms**: If "deploy" doesn't work, try "deployment" or "ci-cd"
3. **Check popular sources**: Many skills come from `vercel-labs/agent-skills` or `ComposioHQ/awesome-claude-skills`

## When No Skills Are Found

If no relevant skills exist:

1. Acknowledge that no existing skill was found
2. Offer to help with the task directly using your general capabilities
3. Suggest the user could create their own skill with `npx skills init`

Example:

```
I searched for skills related to "xyz" but didn't find any matches.
I can still help you with this task directly! Would you like me to proceed?

If this is something you do often, you could create your own skill:
npx skills init my-xyz-skill
```

```

## File: skills\find-skills\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_config_144305-skills-find-skills
name: Find-Skills
path: ecosystem/skills/repo_fetched_agent_config_144305/skills/find-skills
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Find-Skills
Storage area for 'find-skills' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\fix-sentry-issues\SKILL.md
```
---
name: fix-sentry-issues
description: Use Sentry MCP to discover, triage, and fix production issues with root-cause analysis. Use when asked to fix Sentry issues, triage production errors, investigate error spikes, or clean up Sentry noise. Requires Sentry MCP server. Triggers on "fix sentry", "triage errors", "production bugs", "sentry issues".
---

# Fix Sentry Issues

## Philosophy

**The Sentry error is not the problem. It's a signal.**

Your goal is not to close the Sentry issue. Your goal is to discover the root cause, understand what's wrong with the application, and fix the underlying defect. Closing the Sentry issue is a side effect of doing that correctly.

Ask **"Why does this fail?"** — not **"How do I make Sentry quiet?"** Never treat log level changes as fixes. A fallback path means degraded user experience; trace why the primary path fails and fix it upstream.

## Anti-patterns (do not do these)

- **Batch-classifying as "expected" without investigation.** Seeing a fallback does NOT mean you understand the failure. Trace the full input path.
- **Treating "has a fallback" as "not a problem."** Why does the primary path fail? Can we prevent it upstream?
- **Combining multiple issues into one PR.** Each has its own root cause. Fix individually (except when investigation proves identical cause).
- **Throwing away error details.** Never remove `error` from `catch (error)` or strip status codes. That data is how you understand failures.
- **Deciding the fix during triage.** Classify as "Investigate" or "Ignore" only. You don't know the fix until investigation is complete.

**Log level downgrade is valid ONLY for genuinely expected states** (e.g., optional column missing, resource deleted) — NOT for failures with fallbacks.

## Phase 1: Discover & Triage

Use Sentry MCP (`ToolSearch` first to load tools): `find_organizations` → `find_projects` → `search_issues` with `naturalLanguageQuery: "all unresolved issues sorted by events"`.

Build a triage table. Action = **Investigate** or **Ignore** only:

| ID | Title | Events | Action | Reason |
|----|-------|--------|--------|--------|
| PROJ-A | Error in save | 14 | Investigate | User-facing save failure |
| PROJ-B | GM_register... | 3 | Ignore | Greasemonkey extension |

**Investigate:** multiple events, degraded user experience, high-volume warnings, recurring on every run.
**Ignore:** browser extension code, `ChunkLoadError` (self-resolving), single-event transients, already fixed.

Apply: `mcp__sentry__update_issue(..., status: "ignored")` or `status: "resolved"` for already-fixed.

## Phase 2: Investigate (one issue at a time)

Work through these steps **in order**. Do not skip or batch issues.

1. **Pull event-level data** — Issue summaries hide details. Use `get_issue_details` and `search_issue_events` with `naturalLanguageQuery: "all events with extra data"`. Extract: URLs, params, stack traces, status codes, timestamps.

2. **Cross-reference Axiom** — Events have `traceId`. `axiom query "['shiori-events'] | where traceId == '<traceId>'" -f json` for surrounding context (authMethod, client_version, request metadata).

3. **Read the failing code path** — Follow the stack trace. Read every file. Understand before proposing changes.

4. **Trace the input path upstream** *(most often skipped, most important)* — What data reaches the failing function? Should it have reached this path at all? Is there a missing filter? Is the input wrong (binary URL, redirect, bad format)? Can we prevent bad inputs upstream?

5. **Reproduce** — Use actual failing inputs from Sentry. Call the function with exact data. `fetch()` the URLs that timed out. Verify your understanding.

6. **Identify root cause** — Why does this input fail? Why does it reach this path? What's the right fix? (e.g., "Filter binary URLs before Firecrawl" — not "suppress the log")

| Pattern | Real Fix |
|---------|----------|
| External API fails on certain URLs | Filter/validate inputs before sending |
| Timeout | Investigate what's slow; adjust timeout or input size |
| DB "invalid json" | Sanitize before insert |
| Stale reference on cron | Detect staleness, auto-clean |

## Phase 3: Fix

One branch per issue. `git checkout main && git pull && git checkout -b fix/<descriptive-name>`

- **Tests first** — Use data from actual Sentry events. Test fails before fix, passes after.
- **Implement** — Fix the root cause, not the symptom. If the fix is primarily a log level change, STOP: did you investigate why it fails, or just suppress?
- **Verify** — Tests pass, lint passes, fix handles actual failing inputs.
- **PR** — Include **Root cause** (upstream reason) and **Fix** (what changed and why it prevents the failure). Resolve in Sentry only after merge.

```

## File: skills\fix-sentry-issues\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_config_144305-skills-fix-sentry-issues
name: Fix-Sentry-Issues
path: ecosystem/skills/repo_fetched_agent_config_144305/skills/fix-sentry-issues
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Fix-Sentry-Issues
Storage area for 'fix-sentry-issues' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\grill-me\SKILL.md
```
---
name: grill-me
description: Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me".
---

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

If a question can be answered by exploring the codebase, explore the codebase instead.

```

## File: skills\grill-me\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_config_144305-skills-grill-me
name: Grill-Me
path: ecosystem/skills/repo_fetched_agent_config_144305/skills/grill-me
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Grill-Me
Storage area for 'grill-me' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\knip\SKILL.md
```
---
name: knip
description: Run knip to find and remove unused files, dependencies, and exports. Use for cleaning up dead code and unused dependencies.
---

# Knip Code Cleanup

Run knip to find and remove unused files, dependencies, and exports from this codebase.

## Setup

1. Check if knip is available:
   - Run `npx knip --version` to test
   - If it fails or is very slow, check if `knip` is in package.json devDependencies
   - If not installed locally, install with `npm install -D knip` (or pnpm/yarn/bun equivalent based on lockfile present)

2. Knip does NOT remove unused imports/variables inside files — that's a linter's job. Knip finds unused files, dependencies, and exports across the project.

## Workflow

Always follow this configuration-first workflow. Even for simple "run knip" or "clean up codebase" prompts, configure knip properly before acting on reported issues.

### Step 1: Understand the project

- Check what frameworks and tools the project uses (look at package.json)
- Check if a knip config exists (`knip.json`, `knip.jsonc`, or `knip` key in package.json)
- If a config exists, review it for improvements (see Configuration Best Practices below)

### Step 2: Run knip and read configuration hints first

```bash
npx knip
```

Focus on **configuration hints** before anything else. These appear at the top of the output and suggest config adjustments to reduce false positives.

### Step 3: Address hints by adjusting knip.json

Fix configuration hints before addressing reported issues. Common adjustments:
- Enable/disable plugins for detected frameworks
- Add entry patterns for non-standard entry points
- Configure workspace settings for monorepos

### Step 4: Repeat steps 2-3

Re-run knip after each config change. Repeat until configuration hints are resolved and false positives are minimized.

### Step 5: Address actual issues

Once the configuration is settled, work through reported issues. Prioritize in this order:

1. **Unused files** — address these first ("inbox zero" approach removes the most noise)
2. **Unused dependencies** — remove from package.json
3. **Unused devDependencies** — remove from package.json
4. **Unused exports** — remove or mark as internal
5. **Unused types** — remove, or configure `ignoreExportsUsedInFile` (see below)

### Step 6: Re-run and repeat

Re-run knip after each batch of fixes. Removing unused files often exposes newly-unused exports and dependencies.

## Configuration Best Practices

When reviewing or creating a knip config, follow these rules:

- **Never use `ignore` patterns** — `ignore` hides real issues and should almost never be used. Always prefer specific solutions. Other `ignore*` options (like `ignoreDependencies`, `ignoreExportsUsedInFile`) are fine because they target specific issue types.
- **Many unused exported types?** Add `ignoreExportsUsedInFile: { interface: true, type: true }` — this handles the common case of types only used in the same file. Prefer this over broader ignore options.
- **Remove redundant patterns** — Knip already respects `.gitignore`, so ignoring `node_modules`, `dist`, `build`, `.git` is redundant.
- **Remove entry patterns covered by defaults** — Auto-detected plugins already add standard entry points. Don't duplicate them.
- **Config files showing as unused** (e.g. `vite.config.ts`) — Enable or disable the corresponding plugin explicitly rather than ignoring the file.
- **Dependencies matching Node.js builtins** (e.g. `buffer`, `process`) — Add to `ignoreDependencies`.
- **Unresolved imports from path aliases** — Add `paths` to knip config (uses tsconfig.json semantics).

## Production Mode

Use `--production` to focus on production code only:

```bash
npx knip --production
```

This excludes test files, config files, and other non-production entry points. Do NOT use `project` or `ignore` patterns to exclude test files — use `--production` instead.

## Cleanup Confidence Levels

### Auto-delete (high confidence):
- Unused exports that are clearly internal (not part of public API)
- Unused type exports
- Unused dependencies (remove from package.json)
- Unused files that are clearly orphaned (not entry points, not config files)

### Ask first (needs clarification):
- Files that might be entry points or dynamically imported
- Exports that might be part of a public API (index.ts, lib exports)
- Dependencies that might be used via CLI or peer dependencies
- Anything in paths like `src/index`, `lib/`, or files with "public" or "api" in the name

Use the AskUserQuestion tool to clarify before deleting these.

## Auto-fix

Once configuration is settled and you're confident in the results:

```bash
# Auto-fix safe changes (removes unused exports and dependencies)
npx knip --fix

# Auto-fix including file deletion
npx knip --fix --allow-remove-files
```

Only use `--fix` after the configuration-first workflow is complete.

## Error Handling

If knip exits with code 2 (unexpected error like "error loading file"):
- Check if a config file exists — if not, create `knip.json` in the project root
- Check for known issues at knip.dev
- Review the configuration reference for syntax/option errors
- Run knip again after fixes

## Common Commands

```bash
# Basic run
npx knip

# Production only (excludes test/config entry points)
npx knip --production

# Auto-fix what's safe
npx knip --fix

# Auto-fix including file deletion
npx knip --fix --allow-remove-files

# JSON output for parsing
npx knip --reporter json
```

## Notes

- Watch for monorepo setups — may need `--workspace` flag
- Some frameworks need plugins enabled in config
- Knip does not handle unused imports/variables inside files — use ESLint or Biome for that

```

## File: skills\knip\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_config_144305-skills-knip
name: Knip
path: ecosystem/skills/repo_fetched_agent_config_144305/skills/knip
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Knip
Storage area for 'knip' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\playwriter\SKILL.md
```
---
name: playwriter
description: Control the user's currently open Chrome tab through the Playwriter CLI (no new browser launch). Use when you need to inspect live UI state, run scripted browser actions, capture console output, or reproduce frontend issues directly in the user's tab.
---

# Playwriter

Use this skill to drive the user's active Chrome tab via Playwriter.

Full documentation is available here: https://playwriter.dev/

## Quick Start

1. Ensure the Playwriter extension is enabled (green) on the target tab.
2. Ensure CLI is available:

```bash
playwriter --version || npx -y playwriter --version
```

3. Create/attach a session:

```bash
playwriter session new
```

4. Run commands against that session:

```bash
playwriter -s 1 -e "console.log(await page.url())"
```

## Core Workflow

1. Confirm connection and correct tab:

```bash
playwriter -s <session> -e "console.log(await page.url()); console.log(await page.title());"
```

2. Collect page structure when needed:

```bash
playwriter -s <session> -e "console.log(await accessibilitySnapshot({ page }))"
```

3. Execute targeted actions (click/type/hover/fetch/evaluate).
4. Pull logs and structured state via `page.evaluate`.
5. Summarize findings with exact IDs, timestamps, and observed state transitions.

## Useful Commands

Get list rows/options from current app UI:

```bash
playwriter -s <session> -e "const rows = await page.getByRole('option').all(); console.log(rows.length);"
```

Read popup/hover content:

```bash
playwriter -s <session> -e "const row = page.getByRole('option').nth(0); await row.hover(); await page.waitForTimeout(700); console.log(await page.locator('[data-side]').first().innerText());"
```

Run arbitrary in-page debug code:

```bash
playwriter -s <session> -e "const out = await page.evaluate(() => ({ href: location.href })); console.log(out);"
```

## Troubleshooting

- If the session attaches to the wrong tab, click the extension icon on the intended tab and re-run `playwriter session new`.
- If `playwriter` command is missing, use `npx -y playwriter ...` or install globally.
- If execution errors suggest stale connection, create a fresh session.

## Guardrails

- Prefer read-only inspection unless the task requires mutation.
- Announce destructive UI actions before running them.
- When capturing logs, redact sensitive tokens/user data in summaries.

```

## File: skills\playwriter\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_config_144305-skills-playwriter
name: Playwriter
path: ecosystem/skills/repo_fetched_agent_config_144305/skills/playwriter
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Playwriter
Storage area for 'playwriter' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\playwriter\agents\openai.yaml
```
interface:
  display_name: "Playwriter Browser Control"
  short_description: "Use Playwriter CLI to control an open Chrome tab."
  default_prompt: "Use Playwriter CLI to attach to the active browser tab, inspect state, run actions, and capture logs for debugging."

```

## File: skills\playwriter\agents\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_config_144305-skills-playwriter-agents
name: Agents
path: ecosystem/skills/repo_fetched_agent_config_144305/skills/playwriter/agents
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Agents
Storage area for 'agents' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\rams\SKILL.md
```
---
name: rams
description: Run accessibility and visual design review on components. Use when reviewing UI code for WCAG compliance and design issues.
---

# Rams Design Review

You are Rams, an expert design engineer reviewing code for accessibility and visual design issues.

## Mode

If `$ARGUMENTS` is provided, analyze that specific file.
If `$ARGUMENTS` is empty, ask the user which file(s) to review, or offer to scan the project for component files.

---

## 1. Accessibility Review (WCAG 2.1)

### Critical (Must Fix)

| Check | WCAG | What to look for |
|-------|------|------------------|
| Images without alt | 1.1.1 | `<img>` without `alt` attribute |
| Icon-only buttons | 4.1.2 | `<button>` with only SVG/icon, no `aria-label` |
| Form inputs without labels | 1.3.1 | `<input>`, `<select>`, `<textarea>` without associated `<label>` or `aria-label` |
| Non-semantic click handlers | 2.1.1 | `<div onClick>` or `<span onClick>` without `role`, `tabIndex`, `onKeyDown` |
| Missing link destination | 2.1.1 | `<a>` without `href` using only `onClick` |

### Serious (Should Fix)

| Check | WCAG | What to look for |
|-------|------|------------------|
| Focus outline removed | 2.4.7 | `outline-none` or `outline: none` without visible focus replacement |
| Missing keyboard handlers | 2.1.1 | Interactive elements with `onClick` but no `onKeyDown`/`onKeyUp` |
| Color-only information | 1.4.1 | Status/error indicated only by color (no icon/text) |
| Touch target too small | 2.5.5 | Clickable elements smaller than 44x44px |

### Moderate (Consider Fixing)

| Check | WCAG | What to look for |
|-------|------|------------------|
| Heading hierarchy | 1.3.1 | Skipped heading levels (h1 → h3) |
| Positive tabIndex | 2.4.3 | `tabIndex` > 0 (disrupts natural tab order) |
| Role without required attributes | 4.1.2 | `role="button"` without `tabIndex="0"` |

---

## 2. Visual Design Review

### Layout & Spacing
- Inconsistent spacing values
- Overflow issues, alignment problems
- Z-index conflicts

### Typography
- Mixed font families, weights, or sizes
- Line height issues
- Missing font fallbacks

### Color & Contrast
- Contrast ratio below 4.5:1
- Missing hover/focus states
- Dark mode inconsistencies

### Components
- Missing button states (disabled, loading, hover, active, focus)
- Missing form field states (error, success, disabled)
- Inconsistent borders, shadows, or icon sizing

---

## Output Format

```
═══════════════════════════════════════════════════
RAMS DESIGN REVIEW: [filename]
═══════════════════════════════════════════════════

CRITICAL (X issues)
───────────────────
[A11Y] Line 24: Button missing accessible name
  <button><CloseIcon /></button>
  Fix: Add aria-label="Close"
  WCAG: 4.1.2

SERIOUS (X issues)
──────────────────
...

═══════════════════════════════════════════════════
SUMMARY: X critical, X serious, X moderate
Score: XX/100
═══════════════════════════════════════════════════
```

---

## Guidelines

1. Read the file(s) first before making assessments
2. Be specific with line numbers and code snippets
3. Provide fixes, not just problems
4. Prioritize critical accessibility issues first

If asked, offer to fix the issues directly.

```

## File: skills\rams\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_config_144305-skills-rams
name: Rams
path: ecosystem/skills/repo_fetched_agent_config_144305/skills/rams
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Rams
Storage area for 'rams' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\react-doctor\SKILL.md
```
---
name: react-doctor
description: Diagnose and fix React codebase health issues. Use when reviewing React code, fixing performance problems, auditing security, or improving code quality.
version: 1.0.0
---

# React Doctor

Scans your React codebase for security, performance, correctness, and architecture issues. Outputs a 0-100 score with actionable diagnostics.

## Usage

```bash
npx -y react-doctor@latest . --verbose
```

## Workflow

1. Run the command above at the project root
2. Read every diagnostic with file paths and line numbers
3. Fix issues starting with errors (highest severity)
4. Re-run to verify the score improved

## Rules (47+)

- **Security**: hardcoded secrets in client bundle, eval()
- **State & Effects**: derived state in useEffect, missing cleanup, useState from props, cascading setState
- **Architecture**: components inside components, giant components, inline render functions
- **Performance**: layout property animations, transition-all, large blur values
- **Correctness**: array index as key, conditional rendering bugs
- **Next.js**: missing metadata, client-side fetching for server data, async client components
- **Bundle Size**: barrel imports, full lodash, moment.js, missing code splitting
- **Server**: missing auth in server actions, blocking without after()
- **Accessibility**: missing prefers-reduced-motion
- **Dead Code**: unused files, exports, types

## Score

- **75+**: Great
- **50-74**: Needs work
- **0-49**: Critical

```

## File: skills\react-doctor\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_config_144305-skills-react-doctor
name: React-Doctor
path: ecosystem/skills/repo_fetched_agent_config_144305/skills/react-doctor
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# React-Doctor
Storage area for 'react-doctor' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\reclaude\SKILL.md
```
---
name: reclaude
description: Refactor CLAUDE.md files to follow progressive disclosure principles. Use when CLAUDE.md is too long or disorganized.
---

# reclaude

Refactor CLAUDE.md files to follow progressive disclosure principles.

## Prompt

I want you to refactor my CLAUDE.md file to follow progressive disclosure principles.

Follow these steps:

### 1. Check length

Report the current line count. Flag issues:
- **Ideal**: <50 lines
- **Acceptable**: 50-100 lines
- **Needs refactoring**: >100 lines (move content to `.claude/rules/` files)

### 2. Integrate workflow orchestration

Read the workflow skill at `~/.claude/skills/workflow/SKILL.md` and incorporate its principles into the CLAUDE.md or a `.claude/rules/workflow.md` file. Adapt the content to fit the project — don't copy verbatim, but ensure the key behaviors are represented:
- Plan mode for non-trivial tasks
- Subagent strategy
- Self-improvement loop with `tasks/lessons.md`
- Verification before marking tasks done
- Elegance checks for non-trivial changes
- Autonomous bug fixing

For short CLAUDE.md files, add a concise workflow section. For longer ones, create `.claude/rules/workflow.md` and link to it.

### 3. Ensure verification section exists

Check for a `## Verification` section with commands Claude can run after making changes. If missing:
- Look in package.json for test/lint/typecheck/build scripts
- Look for Makefile, justfile, or other task runners
- Add a `## Verification` section with discovered commands

This is critical—Claude performs dramatically better when it can verify its work.

### 4. Find contradictions

Identify any instructions that conflict with each other. For each contradiction, ask me which version I want to keep.

### 5. Check for global skill extraction candidates

Look for content that could become a **reusable global skill** in `~/.claude/skills/`:
- Is about a tool/framework (not project-specific)
- Same instructions appear (or would apply) in 2+ projects
- Is substantial (>20 lines)

If found, suggest creating a global skill with name and description.

### 6. Identify essentials for root CLAUDE.md

Extract only what belongs in the root CLAUDE.md:
- One-line project description
- Package manager (if not npm)
- Non-obvious commands only (skip `npm test`, `npm run build` if standard)
- Links to `.claude/rules/` files with brief descriptions
- Verification section (always required)

### 7. Group remaining content

Organize remaining instructions into `.claude/rules/` files by category (e.g., TypeScript conventions, testing patterns, API design, Git workflow).

### 8. Flag for deletion

Identify content that should be removed entirely:
- **API documentation** — link to external docs instead
- **Code examples** — Claude can infer from reading source files
- **Interface/type definitions** — these exist in the code
- **Generic advice** — "write clean code", "follow best practices"
- **Obvious instructions** — "use TypeScript for .ts files"
- **Redundant info** — things Claude already knows
- **Too vague** — instructions that aren't actionable

## Target Template

```markdown
# Project Name

One-line description.

## Commands
- `command` - what it does (only non-obvious ones)

## Rules

## Verification
After making changes:
- `npm test` - Run tests
- `npm run lint` - Check linting
```

## What to Keep vs Remove

**Keep in CLAUDE.md:**
- Commands Claude can't guess from package.json
- Non-standard patterns specific to this project
- Project gotchas and footguns
- Links to detailed rules files

**Move to `.claude/rules/`:**
- Detailed conventions (>10 lines on a topic)
- Style guides
- Architecture decisions
- Workflow documentation

**Remove entirely:**
- Anything Claude can infer from reading the codebase
- Standard practices for the language/framework
- Documentation that exists elsewhere (link instead)

```

## File: skills\reclaude\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_config_144305-skills-reclaude
name: Reclaude
path: ecosystem/skills/repo_fetched_agent_config_144305/skills/reclaude
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Reclaude
Storage area for 'reclaude' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\sentry\SKILL.md
```
---
name: sentry
description: Sentry error monitoring and performance tracing patterns for Next.js applications.
---

# Sentry Integration

Guidelines for using Sentry for error monitoring and performance tracing.

## Exception Catching

Use `Sentry.captureException(error)` in try/catch blocks:

```javascript
try {
  await riskyOperation();
} catch (error) {
  Sentry.captureException(error);
  throw error;
}
```

## Performance Tracing

Create spans for meaningful actions like button clicks, API calls, and function calls.

### UI Actions

```javascript
function handleClick() {
  Sentry.startSpan(
    { op: "ui.click", name: "Submit Form" },
    (span) => {
      span.setAttribute("formId", formId);
      submitForm();
    }
  );
}
```

### API Calls

```javascript
async function fetchData(id) {
  return Sentry.startSpan(
    { op: "http.client", name: `GET /api/items/${id}` },
    async () => {
      const response = await fetch(`/api/items/${id}`);
      return response.json();
    }
  );
}
```

## Configuration (Next.js)

Sentry initialization files:
- `sentry.client.config.ts` - Client-side
- `sentry.server.config.ts` - Server-side
- `sentry.edge.config.ts` - Edge runtime

Import with `import * as Sentry from "@sentry/nextjs"` - no need to initialize in other files.

### Basic Setup

```javascript
import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: process.env.NEXT_PUBLIC_SENTRY_DSN,
  enableLogs: true,
});
```

### With Console Logging

```javascript
Sentry.init({
  dsn: process.env.NEXT_PUBLIC_SENTRY_DSN,
  integrations: [
    Sentry.consoleLoggingIntegration({ levels: ["log", "warn", "error"] }),
  ],
});
```

## Structured Logging

Use `logger.fmt` for template literals with variables:

```javascript
const { logger } = Sentry;

logger.trace("Starting connection", { database: "users" });
logger.debug(logger.fmt`Cache miss for: ${userId}`);
logger.info("Updated profile", { profileId: 345 });
logger.warn("Rate limit reached", { endpoint: "/api/data" });
logger.error("Payment failed", { orderId: "order_123" });
logger.fatal("Connection pool exhausted", { activeConnections: 100 });
```

```

## File: skills\sentry\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_config_144305-skills-sentry
name: Sentry
path: ecosystem/skills/repo_fetched_agent_config_144305/skills/sentry
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Sentry
Storage area for 'sentry' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\simplify\SKILL.md
```
---
name: simplify
description: Simplify and refine recently modified code for clarity and consistency. Use after writing code to improve readability without changing functionality.
---

You are an expert code simplification specialist focused on enhancing code clarity, consistency, and maintainability while preserving exact functionality. Your expertise lies in applying project-specific best practices to simplify and improve code without altering its behavior. You prioritize readable, explicit code over overly compact solutions. This is a balance that you have mastered as a result your years as an expert software engineer.

You will analyze recently modified code and apply refinements that:

1. **Preserve Functionality**: Never change what the code does - only how it does it. All original features, outputs, and behaviors must remain intact.

2. **Apply Project Standards**: Follow the established coding standards from http://CLAUDE.md including:

- Use ES modules with proper import sorting and extensions
- Prefer `function` keyword over arrow functions
- Use explicit return type annotations for top-level functions
- Follow proper React component patterns with explicit Props types
- Use proper error handling patterns (avoid try/catch when possible)
- Maintain consistent naming conventions

3. **Enhance Clarity**: Simplify code structure by:

- Reducing unnecessary complexity and nesting
- Eliminating redundant code and abstractions
- Improving readability through clear variable and function names
- Consolidating related logic
- Removing unnecessary comments that describe obvious code
- IMPORTANT: Avoid nested ternary operators - prefer switch statements or if/else chains for multiple conditions
- Choose clarity over brevity - explicit code is often better than overly compact code

4. **Maintain Balance**: Avoid over-simplification that could:

- Reduce code clarity or maintainability
- Create overly clever solutions that are hard to understand
- Combine too many concerns into single functions or components
- Remove helpful abstractions that improve code organization
- Prioritize "fewer lines" over readability (e.g., nested ternaries, dense one-liners)
- Make the code harder to debug or extend

5. **Focus Scope**: Only refine code that has been recently modified or touched in the current session, unless explicitly instructed to review a broader scope.

Your refinement process:

1. Identify the recently modified code sections
2. Analyze for opportunities to improve elegance and consistency
3. Apply project-specific best practices and coding standards
4. Ensure all functionality remains unchanged
5. Verify the refined code is simpler and more maintainable
6. Document only significant changes that affect understanding

You operate autonomously and proactively, refining code immediately after it's written or modified without requiring explicit requests. Your goal is to ensure all code meets the highest standards of elegance and maintainability while preserving its complete functionality.

```

## File: skills\simplify\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_config_144305-skills-simplify
name: Simplify
path: ecosystem/skills/repo_fetched_agent_config_144305/skills/simplify
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Simplify
Storage area for 'simplify' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\skill-creator\LICENSE.txt
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
      submitted to Licensor for inclusion in the Work by the copyright owner
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

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

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

## File: skills\skill-creator\SKILL.md
```
---
name: skill-creator
description: Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.
license: Complete terms in LICENSE.txt
---

# Skill Creator

This skill provides guidance for creating effective skills.

## About Skills

Skills are modular, self-contained packages that extend Claude's capabilities by providing
specialized knowledge, workflows, and tools. Think of them as "onboarding guides" for specific
domains or tasks—they transform Claude from a general-purpose agent into a specialized agent
equipped with procedural knowledge that no model can fully possess.

### What Skills Provide

1. Specialized workflows - Multi-step procedures for specific domains
2. Tool integrations - Instructions for working with specific file formats or APIs
3. Domain expertise - Company-specific knowledge, schemas, business logic
4. Bundled resources - Scripts, references, and assets for complex and repetitive tasks

## Core Principles

### Concise is Key

The context window is a public good. Skills share the context window with everything else Claude needs: system prompt, conversation history, other Skills' metadata, and the actual user request.

**Default assumption: Claude is already very smart.** Only add context Claude doesn't already have. Challenge each piece of information: "Does Claude really need this explanation?" and "Does this paragraph justify its token cost?"

Prefer concise examples over verbose explanations.

### Set Appropriate Degrees of Freedom

Match the level of specificity to the task's fragility and variability:

**High freedom (text-based instructions)**: Use when multiple approaches are valid, decisions depend on context, or heuristics guide the approach.

**Medium freedom (pseudocode or scripts with parameters)**: Use when a preferred pattern exists, some variation is acceptable, or configuration affects behavior.

**Low freedom (specific scripts, few parameters)**: Use when operations are fragile and error-prone, consistency is critical, or a specific sequence must be followed.

Think of Claude as exploring a path: a narrow bridge with cliffs needs specific guardrails (low freedom), while an open field allows many routes (high freedom).

### Anatomy of a Skill

Every skill consists of a required SKILL.md file and optional bundled resources:

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter metadata (required)
│   │   ├── name: (required)
│   │   └── description: (required)
│   └── Markdown instructions (required)
└── Bundled Resources (optional)
    ├── scripts/          - Executable code (Python/Bash/etc.)
    ├── references/       - Documentation intended to be loaded into context as needed
    └── assets/           - Files used in output (templates, icons, fonts, etc.)
```

#### SKILL.md (required)

Every SKILL.md consists of:

- **Frontmatter** (YAML): Contains `name` and `description` fields. These are the only fields that Claude reads to determine when the skill gets used, thus it is very important to be clear and comprehensive in describing what the skill is, and when it should be used.
- **Body** (Markdown): Instructions and guidance for using the skill. Only loaded AFTER the skill triggers (if at all).

#### Bundled Resources (optional)

##### Scripts (`scripts/`)

Executable code (Python/Bash/etc.) for tasks that require deterministic reliability or are repeatedly rewritten.

- **When to include**: When the same code is being rewritten repeatedly or deterministic reliability is needed
- **Example**: `scripts/rotate_pdf.py` for PDF rotation tasks
- **Benefits**: Token efficient, deterministic, may be executed without loading into context
- **Note**: Scripts may still need to be read by Claude for patching or environment-specific adjustments

##### References (`references/`)

Documentation and reference material intended to be loaded as needed into context to inform Claude's process and thinking.

- **When to include**: For documentation that Claude should reference while working
- **Examples**: `references/finance.md` for financial schemas, `references/mnda.md` for company NDA template, `references/policies.md` for company policies, `references/api_docs.md` for API specifications
- **Use cases**: Database schemas, API documentation, domain knowledge, company policies, detailed workflow guides
- **Benefits**: Keeps SKILL.md lean, loaded only when Claude determines it's needed
- **Best practice**: If files are large (>10k words), include grep search patterns in SKILL.md
- **Avoid duplication**: Information should live in either SKILL.md or references files, not both. Prefer references files for detailed information unless it's truly core to the skill—this keeps SKILL.md lean while making information discoverable without hogging the context window. Keep only essential procedural instructions and workflow guidance in SKILL.md; move detailed reference material, schemas, and examples to references files.

##### Assets (`assets/`)

Files not intended to be loaded into context, but rather used within the output Claude produces.

- **When to include**: When the skill needs files that will be used in the final output
- **Examples**: `assets/logo.png` for brand assets, `assets/slides.pptx` for PowerPoint templates, `assets/frontend-template/` for HTML/React boilerplate, `assets/font.ttf` for typography
- **Use cases**: Templates, images, icons, boilerplate code, fonts, sample documents that get copied or modified
- **Benefits**: Separates output resources from documentation, enables Claude to use files without loading them into context

#### What to Not Include in a Skill

A skill should only contain essential files that directly support its functionality. Do NOT create extraneous documentation or auxiliary files, including:

- README.md
- INSTALLATION_GUIDE.md
- QUICK_REFERENCE.md
- CHANGELOG.md
- etc.

The skill should only contain the information needed for an AI agent to do the job at hand. It should not contain auxilary context about the process that went into creating it, setup and testing procedures, user-facing documentation, etc. Creating additional documentation files just adds clutter and confusion.

### Progressive Disclosure Design Principle

Skills use a three-level loading system to manage context efficiently:

1. **Metadata (name + description)** - Always in context (~100 words)
2. **SKILL.md body** - When skill triggers (<5k words)
3. **Bundled resources** - As needed by Claude (Unlimited because scripts can be executed without reading into context window)

#### Progressive Disclosure Patterns

Keep SKILL.md body to the essentials and under 500 lines to minimize context bloat. Split content into separate files when approaching this limit. When splitting out content into other files, it is very important to reference them from SKILL.md and describe clearly when to read them, to ensure the reader of the skill knows they exist and when to use them.

**Key principle:** When a skill supports multiple variations, frameworks, or options, keep only the core workflow and selection guidance in SKILL.md. Move variant-specific details (patterns, examples, configuration) into separate reference files.

**Pattern 1: High-level guide with references**

```markdown
# PDF Processing

## Quick start

Extract text with pdfplumber:
[code example]

## Advanced features

```

Claude loads FORMS.md, REFERENCE.md, or EXAMPLES.md only when needed.

**Pattern 2: Domain-specific organization**

For Skills with multiple domains, organize content by domain to avoid loading irrelevant context:

```
bigquery-skill/
├── SKILL.md (overview and navigation)
└── reference/
    ├── finance.md (revenue, billing metrics)
    ├── sales.md (opportunities, pipeline)
    ├── product.md (API usage, features)
    └── marketing.md (campaigns, attribution)
```

When a user asks about sales metrics, Claude only reads sales.md.

Similarly, for skills supporting multiple frameworks or variants, organize by variant:

```
cloud-deploy/
├── SKILL.md (workflow + provider selection)
└── references/
    ├── aws.md (AWS deployment patterns)
    ├── gcp.md (GCP deployment patterns)
    └── azure.md (Azure deployment patterns)
```

When the user chooses AWS, Claude only reads aws.md.

**Pattern 3: Conditional details**

Show basic content, link to advanced content:

```markdown
# DOCX Processing

## Creating documents

Use docx-js for new documents. See [DOCX-JS.md](DOCX-JS.md).

## Editing documents

For simple edits, modify the XML directly.

**For tracked changes**: See [REDLINING.md](REDLINING.md)
**For OOXML details**: See [OOXML.md](OOXML.md)
```

Claude reads REDLINING.md or OOXML.md only when the user needs those features.

**Important guidelines:**

- **Avoid deeply nested references** - Keep references one level deep from SKILL.md. All reference files should link directly from SKILL.md.
- **Structure longer reference files** - For files longer than 100 lines, include a table of contents at the top so Claude can see the full scope when previewing.

## Skill Creation Process

Skill creation involves these steps:

1. Understand the skill with concrete examples
2. Plan reusable skill contents (scripts, references, assets)
3. Initialize the skill (run init_skill.py)
4. Edit the skill (implement resources and write SKILL.md)
5. Package the skill (run package_skill.py)
6. Iterate based on real usage

Follow these steps in order, skipping only if there is a clear reason why they are not applicable.

### Step 1: Understanding the Skill with Concrete Examples

Skip this step only when the skill's usage patterns are already clearly understood. It remains valuable even when working with an existing skill.

To create an effective skill, clearly understand concrete examples of how the skill will be used. This understanding can come from either direct user examples or generated examples that are validated with user feedback.

For example, when building an image-editor skill, relevant questions include:

- "What functionality should the image-editor skill support? Editing, rotating, anything else?"
- "Can you give some examples of how this skill would be used?"
- "I can imagine users asking for things like 'Remove the red-eye from this image' or 'Rotate this image'. Are there other ways you imagine this skill being used?"
- "What would a user say that should trigger this skill?"

To avoid overwhelming users, avoid asking too many questions in a single message. Start with the most important questions and follow up as needed for better effectiveness.

Conclude this step when there is a clear sense of the functionality the skill should support.

### Step 2: Planning the Reusable Skill Contents

To turn concrete examples into an effective skill, analyze each example by:

1. Considering how to execute on the example from scratch
2. Identifying what scripts, references, and assets would be helpful when executing these workflows repeatedly

Example: When building a `pdf-editor` skill to handle queries like "Help me rotate this PDF," the analysis shows:

1. Rotating a PDF requires re-writing the same code each time
2. A `scripts/rotate_pdf.py` script would be helpful to store in the skill

Example: When designing a `frontend-webapp-builder` skill for queries like "Build me a todo app" or "Build me a dashboard to track my steps," the analysis shows:

1. Writing a frontend webapp requires the same boilerplate HTML/React each time
2. An `assets/hello-world/` template containing the boilerplate HTML/React project files would be helpful to store in the skill

Example: When building a `big-query` skill to handle queries like "How many users have logged in today?" the analysis shows:

1. Querying BigQuery requires re-discovering the table schemas and relationships each time
2. A `references/schema.md` file documenting the table schemas would be helpful to store in the skill

To establish the skill's contents, analyze each concrete example to create a list of the reusable resources to include: scripts, references, and assets.

### Step 3: Initializing the Skill

At this point, it is time to actually create the skill.

Skip this step only if the skill being developed already exists, and iteration or packaging is needed. In this case, continue to the next step.

When creating a new skill from scratch, always run the `init_skill.py` script. The script conveniently generates a new template skill directory that automatically includes everything a skill requires, making the skill creation process much more efficient and reliable.

Usage:

```bash
scripts/init_skill.py <skill-name> --path <output-directory>
```

The script:

- Creates the skill directory at the specified path
- Generates a SKILL.md template with proper frontmatter and TODO placeholders
- Creates example resource directories: `scripts/`, `references/`, and `assets/`
- Adds example files in each directory that can be customized or deleted

After initialization, customize or remove the generated SKILL.md and example files as needed.

### Step 4: Edit the Skill

When editing the (newly-generated or existing) skill, remember that the skill is being created for another instance of Claude to use. Include information that would be beneficial and non-obvious to Claude. Consider what procedural knowledge, domain-specific details, or reusable assets would help another Claude instance execute these tasks more effectively.

#### Learn Proven Design Patterns

Consult these helpful guides based on your skill's needs:

- **Multi-step processes**: See references/workflows.md for sequential workflows and conditional logic
- **Specific output formats or quality standards**: See references/output-patterns.md for template and example patterns

These files contain established best practices for effective skill design.

#### Start with Reusable Skill Contents

To begin implementation, start with the reusable resources identified above: `scripts/`, `references/`, and `assets/` files. Note that this step may require user input. For example, when implementing a `brand-guidelines` skill, the user may need to provide brand assets or templates to store in `assets/`, or documentation to store in `references/`.

Added scripts must be tested by actually running them to ensure there are no bugs and that the output matches what is expected. If there are many similar scripts, only a representative sample needs to be tested to ensure confidence that they all work while balancing time to completion.

Any example files and directories not needed for the skill should be deleted. The initialization script creates example files in `scripts/`, `references/`, and `assets/` to demonstrate structure, but most skills won't need all of them.

#### Update SKILL.md

**Writing Guidelines:** Always use imperative/infinitive form.

##### Frontmatter

Write the YAML frontmatter with `name` and `description`:

- `name`: The skill name
- `description`: This is the primary triggering mechanism for your skill, and helps Claude understand when to use the skill.
  - Include both what the Skill does and specific triggers/contexts for when to use it.
  - Include all "when to use" information here - Not in the body. The body is only loaded after triggering, so "When to Use This Skill" sections in the body are not helpful to Claude.
  - Example description for a `docx` skill: "Comprehensive document creation, editing, and analysis with support for tracked changes, comments, formatting preservation, and text extraction. Use when Claude needs to work with professional documents (.docx files) for: (1) Creating new documents, (2) Modifying or editing content, (3) Working with tracked changes, (4) Adding comments, or any other document tasks"

Do not include any other fields in YAML frontmatter.

##### Body

Write instructions for using the skill and its bundled resources.

### Step 5: Packaging a Skill

Once development of the skill is complete, it must be packaged into a distributable .skill file that gets shared with the user. The packaging process automatically validates the skill first to ensure it meets all requirements:

```bash
scripts/package_skill.py <path/to/skill-folder>
```

Optional output directory specification:

```bash
scripts/package_skill.py <path/to/skill-folder> ./dist
```

The packaging script will:

1. **Validate** the skill automatically, checking:

   - YAML frontmatter format and required fields
   - Skill naming conventions and directory structure
   - Description completeness and quality
   - File organization and resource references

2. **Package** the skill if validation passes, creating a .skill file named after the skill (e.g., `my-skill.skill`) that includes all files and maintains the proper directory structure for distribution. The .skill file is a zip file with a .skill extension.

If validation fails, the script will report the errors and exit without creating a package. Fix any validation errors and run the packaging command again.

### Step 6: Iterate

After testing the skill, users may request improvements. Often this happens right after using the skill, with fresh context of how the skill performed.

**Iteration workflow:**

1. Use the skill on real tasks
2. Notice struggles or inefficiencies
3. Identify how SKILL.md or bundled resources should be updated
4. Implement changes and test again

```

## File: skills\skill-creator\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_config_144305-skills-skill-creator
name: Skill-Creator
path: ecosystem/skills/repo_fetched_agent_config_144305/skills/skill-creator
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Skill-Creator
Storage area for 'skill-creator' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\skill-creator\references\output_patterns.md
```
# Output Patterns

Use these patterns when skills need to produce consistent, high-quality output.

## Template Pattern

Provide templates for output format. Match the level of strictness to your needs.

**For strict requirements (like API responses or data formats):**

```markdown
## Report structure

ALWAYS use this exact template structure:

# [Analysis Title]

## Executive summary
[One-paragraph overview of key findings]

## Key findings
- Finding 1 with supporting data
- Finding 2 with supporting data
- Finding 3 with supporting data

## Recommendations
1. Specific actionable recommendation
2. Specific actionable recommendation
```

**For flexible guidance (when adaptation is useful):**

```markdown
## Report structure

Here is a sensible default format, but use your best judgment:

# [Analysis Title]

## Executive summary
[Overview]

## Key findings
[Adapt sections based on what you discover]

## Recommendations
[Tailor to the specific context]

Adjust sections as needed for the specific analysis type.
```

## Examples Pattern

For skills where output quality depends on seeing examples, provide input/output pairs:

```markdown
## Commit message format

Generate commit messages following these examples:

**Example 1:**
Input: Added user authentication with JWT tokens
Output:
```
feat(auth): implement JWT-based authentication

Add login endpoint and token validation middleware
```

**Example 2:**
Input: Fixed bug where dates displayed incorrectly in reports
Output:
```
fix(reports): correct date formatting in timezone conversion

Use UTC timestamps consistently across report generation
```

Follow this style: type(scope): brief description, then detailed explanation.
```

Examples help Claude understand the desired style and level of detail more clearly than descriptions alone.

```

## File: skills\skill-creator\references\workflows.md
```
# Workflow Patterns

## Sequential Workflows

For complex tasks, break operations into clear, sequential steps. It is often helpful to give Claude an overview of the process towards the beginning of SKILL.md:

```markdown
Filling a PDF form involves these steps:

1. Analyze the form (run analyze_form.py)
2. Create field mapping (edit fields.json)
3. Validate mapping (run validate_fields.py)
4. Fill the form (run fill_form.py)
5. Verify output (run verify_output.py)
```

## Conditional Workflows

For tasks with branching logic, guide Claude through decision points:

```markdown
1. Determine the modification type:
   **Creating new content?** → Follow "Creation workflow" below
   **Editing existing content?** → Follow "Editing workflow" below

2. Creation workflow: [steps]
3. Editing workflow: [steps]
```

```

## File: skills\skill-creator\references\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_config_144305-skills-skill-creator-references
name: References
path: ecosystem/skills/repo_fetched_agent_config_144305/skills/skill-creator/references
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# References
Storage area for 'references' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\skill-creator\scripts\init_skill.py
```
#!/usr/bin/env python3
"""
Skill Initializer - Creates a new skill from template

Usage:
    init_skill.py <skill-name> --path <path>

Examples:
    init_skill.py my-new-skill --path skills/public
    init_skill.py my-api-helper --path skills/private
    init_skill.py custom-skill --path /custom/location
"""

import sys
from pathlib import Path


SKILL_TEMPLATE = """---
name: {skill_name}
description: [TODO: Complete and informative explanation of what the skill does and when to use it. Include WHEN to use this skill - specific scenarios, file types, or tasks that trigger it.]
---

# {skill_title}

## Overview

[TODO: 1-2 sentences explaining what this skill enables]

## Structuring This Skill

[TODO: Choose the structure that best fits this skill's purpose. Common patterns:

**1. Workflow-Based** (best for sequential processes)
- Works well when there are clear step-by-step procedures
- Example: DOCX skill with "Workflow Decision Tree" → "Reading" → "Creating" → "Editing"
- Structure: ## Overview → ## Workflow Decision Tree → ## Step 1 → ## Step 2...

**2. Task-Based** (best for tool collections)
- Works well when the skill offers different operations/capabilities
- Example: PDF skill with "Quick Start" → "Merge PDFs" → "Split PDFs" → "Extract Text"
- Structure: ## Overview → ## Quick Start → ## Task Category 1 → ## Task Category 2...

**3. Reference/Guidelines** (best for standards or specifications)
- Works well for brand guidelines, coding standards, or requirements
- Example: Brand styling with "Brand Guidelines" → "Colors" → "Typography" → "Features"
- Structure: ## Overview → ## Guidelines → ## Specifications → ## Usage...

**4. Capabilities-Based** (best for integrated systems)
- Works well when the skill provides multiple interrelated features
- Example: Product Management with "Core Capabilities" → numbered capability list
- Structure: ## Overview → ## Core Capabilities → ### 1. Feature → ### 2. Feature...

Patterns can be mixed and matched as needed. Most skills combine patterns (e.g., start with task-based, add workflow for complex operations).

Delete this entire "Structuring This Skill" section when done - it's just guidance.]

## [TODO: Replace with the first main section based on chosen structure]

[TODO: Add content here. See examples in existing skills:
- Code samples for technical skills
- Decision trees for complex workflows
- Concrete examples with realistic user requests
- References to scripts/templates/references as needed]

## Resources

This skill includes example resource directories that demonstrate how to organize different types of bundled resources:

### scripts/
Executable code (Python/Bash/etc.) that can be run directly to perform specific operations.

**Examples from other skills:**
- PDF skill: `fill_fillable_fields.py`, `extract_form_field_info.py` - utilities for PDF manipulation
- DOCX skill: `document.py`, `utilities.py` - Python modules for document processing

**Appropriate for:** Python scripts, shell scripts, or any executable code that performs automation, data processing, or specific operations.

**Note:** Scripts may be executed without loading into context, but can still be read by Claude for patching or environment adjustments.

### references/
Documentation and reference material intended to be loaded into context to inform Claude's process and thinking.

**Examples from other skills:**
- Product management: `communication.md`, `context_building.md` - detailed workflow guides
- BigQuery: API reference documentation and query examples
- Finance: Schema documentation, company policies

**Appropriate for:** In-depth documentation, API references, database schemas, comprehensive guides, or any detailed information that Claude should reference while working.

### assets/
Files not intended to be loaded into context, but rather used within the output Claude produces.

**Examples from other skills:**
- Brand styling: PowerPoint template files (.pptx), logo files
- Frontend builder: HTML/React boilerplate project directories
- Typography: Font files (.ttf, .woff2)

**Appropriate for:** Templates, boilerplate code, document templates, images, icons, fonts, or any files meant to be copied or used in the final output.

---

**Any unneeded directories can be deleted.** Not every skill requires all three types of resources.
"""

EXAMPLE_SCRIPT = '''#!/usr/bin/env python3
"""
Example helper script for {skill_name}

This is a placeholder script that can be executed directly.
Replace with actual implementation or delete if not needed.

Example real scripts from other skills:
- pdf/scripts/fill_fillable_fields.py - Fills PDF form fields
- pdf/scripts/convert_pdf_to_images.py - Converts PDF pages to images
"""

def main():
    print("This is an example script for {skill_name}")
    # TODO: Add actual script logic here
    # This could be data processing, file conversion, API calls, etc.

if __name__ == "__main__":
    main()
'''

EXAMPLE_REFERENCE = """# Reference Documentation for {skill_title}

This is a placeholder for detailed reference documentation.
Replace with actual reference content or delete if not needed.

Example real reference docs from other skills:
- product-management/references/communication.md - Comprehensive guide for status updates
- product-management/references/context_building.md - Deep-dive on gathering context
- bigquery/references/ - API references and query examples

## When Reference Docs Are Useful

Reference docs are ideal for:
- Comprehensive API documentation
- Detailed workflow guides
- Complex multi-step processes
- Information too lengthy for main SKILL.md
- Content that's only needed for specific use cases

## Structure Suggestions

### API Reference Example
- Overview
- Authentication
- Endpoints with examples
- Error codes
- Rate limits

### Workflow Guide Example
- Prerequisites
- Step-by-step instructions
- Common patterns
- Troubleshooting
- Best practices
"""

EXAMPLE_ASSET = """# Example Asset File

This placeholder represents where asset files would be stored.
Replace with actual asset files (templates, images, fonts, etc.) or delete if not needed.

Asset files are NOT intended to be loaded into context, but rather used within
the output Claude produces.

Example asset files from other skills:
- Brand guidelines: logo.png, slides_template.pptx
- Frontend builder: hello-world/ directory with HTML/React boilerplate
- Typography: custom-font.ttf, font-family.woff2
- Data: sample_data.csv, test_dataset.json

## Common Asset Types

- Templates: .pptx, .docx, boilerplate directories
- Images: .png, .jpg, .svg, .gif
- Fonts: .ttf, .otf, .woff, .woff2
- Boilerplate code: Project directories, starter files
- Icons: .ico, .svg
- Data files: .csv, .json, .xml, .yaml

Note: This is a text placeholder. Actual assets can be any file type.
"""


def title_case_skill_name(skill_name):
    """Convert hyphenated skill name to Title Case for display."""
    return ' '.join(word.capitalize() for word in skill_name.split('-'))


def init_skill(skill_name, path):
    """
    Initialize a new skill directory with template SKILL.md.

    Args:
        skill_name: Name of the skill
        path: Path where the skill directory should be created

    Returns:
        Path to created skill directory, or None if error
    """
    # Determine skill directory path
    skill_dir = Path(path).resolve() / skill_name

    # Check if directory already exists
    if skill_dir.exists():
        print(f"❌ Error: Skill directory already exists: {skill_dir}")
        return None

    # Create skill directory
    try:
        skill_dir.mkdir(parents=True, exist_ok=False)
        print(f"✅ Created skill directory: {skill_dir}")
    except Exception as e:
        print(f"❌ Error creating directory: {e}")
        return None

    # Create SKILL.md from template
    skill_title = title_case_skill_name(skill_name)
    skill_content = SKILL_TEMPLATE.format(
        skill_name=skill_name,
        skill_title=skill_title
    )

    skill_md_path = skill_dir / 'SKILL.md'
    try:
        skill_md_path.write_text(skill_content)
        print("✅ Created SKILL.md")
    except Exception as e:
        print(f"❌ Error creating SKILL.md: {e}")
        return None

    # Create resource directories with example files
    try:
        # Create scripts/ directory with example script
        scripts_dir = skill_dir / 'scripts'
        scripts_dir.mkdir(exist_ok=True)
        example_script = scripts_dir / 'example.py'
        example_script.write_text(EXAMPLE_SCRIPT.format(skill_name=skill_name))
        example_script.chmod(0o755)
        print("✅ Created scripts/example.py")

        # Create references/ directory with example reference doc
        references_dir = skill_dir / 'references'
        references_dir.mkdir(exist_ok=True)
        example_reference = references_dir / 'api_reference.md'
        example_reference.write_text(EXAMPLE_REFERENCE.format(skill_title=skill_title))
        print("✅ Created references/api_reference.md")

        # Create assets/ directory with example asset placeholder
        assets_dir = skill_dir / 'assets'
        assets_dir.mkdir(exist_ok=True)
        example_asset = assets_dir / 'example_asset.txt'
        example_asset.write_text(EXAMPLE_ASSET)
        print("✅ Created assets/example_asset.txt")
    except Exception as e:
        print(f"❌ Error creating resource directories: {e}")
        return None

    # Print next steps
    print(f"\n✅ Skill '{skill_name}' initialized successfully at {skill_dir}")
    print("\nNext steps:")
    print("1. Edit SKILL.md to complete the TODO items and update the description")
    print("2. Customize or delete the example files in scripts/, references/, and assets/")
    print("3. Run the validator when ready to check the skill structure")

    return skill_dir


def main():
    if len(sys.argv) < 4 or sys.argv[2] != '--path':
        print("Usage: init_skill.py <skill-name> --path <path>")
        print("\nSkill name requirements:")
        print("  - Hyphen-case identifier (e.g., 'data-analyzer')")
        print("  - Lowercase letters, digits, and hyphens only")
        print("  - Max 40 characters")
        print("  - Must match directory name exactly")
        print("\nExamples:")
        print("  init_skill.py my-new-skill --path skills/public")
        print("  init_skill.py my-api-helper --path skills/private")
        print("  init_skill.py custom-skill --path /custom/location")
        sys.exit(1)

    skill_name = sys.argv[1]
    path = sys.argv[3]

    print(f"🚀 Initializing skill: {skill_name}")
    print(f"   Location: {path}")
    print()

    result = init_skill(skill_name, path)

    if result:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()

```

## File: skills\skill-creator\scripts\package_skill.py
```
#!/usr/bin/env python3
"""
Skill Packager - Creates a distributable .skill file of a skill folder

Usage:
    python utils/package_skill.py <path/to/skill-folder> [output-directory]

Example:
    python utils/package_skill.py skills/public/my-skill
    python utils/package_skill.py skills/public/my-skill ./dist
"""

import sys
import zipfile
from pathlib import Path
from quick_validate import validate_skill


def package_skill(skill_path, output_dir=None):
    """
    Package a skill folder into a .skill file.

    Args:
        skill_path: Path to the skill folder
        output_dir: Optional output directory for the .skill file (defaults to current directory)

    Returns:
        Path to the created .skill file, or None if error
    """
    skill_path = Path(skill_path).resolve()

    # Validate skill folder exists
    if not skill_path.exists():
        print(f"❌ Error: Skill folder not found: {skill_path}")
        return None

    if not skill_path.is_dir():
        print(f"❌ Error: Path is not a directory: {skill_path}")
        return None

    # Validate SKILL.md exists
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        print(f"❌ Error: SKILL.md not found in {skill_path}")
        return None

    # Run validation before packaging
    print("🔍 Validating skill...")
    valid, message = validate_skill(skill_path)
    if not valid:
        print(f"❌ Validation failed: {message}")
        print("   Please fix the validation errors before packaging.")
        return None
    print(f"✅ {message}\n")

    # Determine output location
    skill_name = skill_path.name
    if output_dir:
        output_path = Path(output_dir).resolve()
        output_path.mkdir(parents=True, exist_ok=True)
    else:
        output_path = Path.cwd()

    skill_filename = output_path / f"{skill_name}.skill"

    # Create the .skill file (zip format)
    try:
        with zipfile.ZipFile(skill_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Walk through the skill directory
            for file_path in skill_path.rglob('*'):
                if file_path.is_file():
                    # Calculate the relative path within the zip
                    arcname = file_path.relative_to(skill_path.parent)
                    zipf.write(file_path, arcname)
                    print(f"  Added: {arcname}")

        print(f"\n✅ Successfully packaged skill to: {skill_filename}")
        return skill_filename

    except Exception as e:
        print(f"❌ Error creating .skill file: {e}")
        return None


def main():
    if len(sys.argv) < 2:
        print("Usage: python utils/package_skill.py <path/to/skill-folder> [output-directory]")
        print("\nExample:")
        print("  python utils/package_skill.py skills/public/my-skill")
        print("  python utils/package_skill.py skills/public/my-skill ./dist")
        sys.exit(1)

    skill_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None

    print(f"📦 Packaging skill: {skill_path}")
    if output_dir:
        print(f"   Output directory: {output_dir}")
    print()

    result = package_skill(skill_path, output_dir)

    if result:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()

```

## File: skills\skill-creator\scripts\quick_validate.py
```
#!/usr/bin/env python3
"""
Quick validation script for skills - minimal version
"""

import sys
import os
import re
import yaml
from pathlib import Path

def validate_skill(skill_path):
    """Basic validation of a skill"""
    skill_path = Path(skill_path)

    # Check SKILL.md exists
    skill_md = skill_path / 'SKILL.md'
    if not skill_md.exists():
        return False, "SKILL.md not found"

    # Read and validate frontmatter
    content = skill_md.read_text()
    if not content.startswith('---'):
        return False, "No YAML frontmatter found"

    # Extract frontmatter
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return False, "Invalid frontmatter format"

    frontmatter_text = match.group(1)

    # Parse YAML frontmatter
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
        if not isinstance(frontmatter, dict):
            return False, "Frontmatter must be a YAML dictionary"
    except yaml.YAMLError as e:
        return False, f"Invalid YAML in frontmatter: {e}"

    # Define allowed properties
    ALLOWED_PROPERTIES = {'name', 'description', 'license', 'allowed-tools', 'metadata'}

    # Check for unexpected properties (excluding nested keys under metadata)
    unexpected_keys = set(frontmatter.keys()) - ALLOWED_PROPERTIES
    if unexpected_keys:
        return False, (
            f"Unexpected key(s) in SKILL.md frontmatter: {', '.join(sorted(unexpected_keys))}. "
            f"Allowed properties are: {', '.join(sorted(ALLOWED_PROPERTIES))}"
        )

    # Check required fields
    if 'name' not in frontmatter:
        return False, "Missing 'name' in frontmatter"
    if 'description' not in frontmatter:
        return False, "Missing 'description' in frontmatter"

    # Extract name for validation
    name = frontmatter.get('name', '')
    if not isinstance(name, str):
        return False, f"Name must be a string, got {type(name).__name__}"
    name = name.strip()
    if name:
        # Check naming convention (hyphen-case: lowercase with hyphens)
        if not re.match(r'^[a-z0-9-]+$', name):
            return False, f"Name '{name}' should be hyphen-case (lowercase letters, digits, and hyphens only)"
        if name.startswith('-') or name.endswith('-') or '--' in name:
            return False, f"Name '{name}' cannot start/end with hyphen or contain consecutive hyphens"
        # Check name length (max 64 characters per spec)
        if len(name) > 64:
            return False, f"Name is too long ({len(name)} characters). Maximum is 64 characters."

    # Extract and validate description
    description = frontmatter.get('description', '')
    if not isinstance(description, str):
        return False, f"Description must be a string, got {type(description).__name__}"
    description = description.strip()
    if description:
        # Check for angle brackets
        if '<' in description or '>' in description:
            return False, "Description cannot contain angle brackets (< or >)"
        # Check description length (max 1024 characters per spec)
        if len(description) > 1024:
            return False, f"Description is too long ({len(description)} characters). Maximum is 1024 characters."

    return True, "Skill is valid!"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python quick_validate.py <skill_directory>")
        sys.exit(1)

    valid, message = validate_skill(sys.argv[1])
    print(message)
    sys.exit(0 if valid else 1)

```

## File: skills\skill-creator\scripts\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_config_144305-skills-skill-creator-scripts
name: Scripts
path: ecosystem/skills/repo_fetched_agent_config_144305/skills/skill-creator/scripts
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Scripts
Storage area for 'scripts' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\tdd\deep_modules.md
```
# Deep Modules

From "A Philosophy of Software Design":

**Deep module** = small interface + lots of implementation

```
┌─────────────────────┐
│   Small Interface   │  ← Few methods, simple params
├─────────────────────┤
│                     │
│                     │
│  Deep Implementation│  ← Complex logic hidden
│                     │
│                     │
└─────────────────────┘
```

**Shallow module** = large interface + little implementation (avoid)

```
┌─────────────────────────────────┐
│       Large Interface           │  ← Many methods, complex params
├─────────────────────────────────┤
│  Thin Implementation            │  ← Just passes through
└─────────────────────────────────┘
```

When designing interfaces, ask:

- Can I reduce the number of methods?
- Can I simplify the parameters?
- Can I hide more complexity inside?

```

## File: skills\tdd\interface_design.md
```
# Interface Design for Testability

Good interfaces make testing natural:

1. **Accept dependencies, don't create them**

   ```typescript
   // Testable
   function processOrder(order, paymentGateway) {}

   // Hard to test
   function processOrder(order) {
     const gateway = new StripeGateway();
   }
   ```

2. **Return results, don't produce side effects**

   ```typescript
   // Testable
   function calculateDiscount(cart): Discount {}

   // Hard to test
   function applyDiscount(cart): void {
     cart.total -= discount;
   }
   ```

3. **Small surface area**
   - Fewer methods = fewer tests needed
   - Fewer params = simpler test setup

```

## File: skills\tdd\mocking.md
```
# When to Mock

Mock at **system boundaries** only:

- External APIs (payment, email, etc.)
- Databases (sometimes - prefer test DB)
- Time/randomness
- File system (sometimes)

Don't mock:

- Your own classes/modules
- Internal collaborators
- Anything you control

## Designing for Mockability

At system boundaries, design interfaces that are easy to mock:

**1. Use dependency injection**

Pass external dependencies in rather than creating them internally:

```typescript
// Easy to mock
function processPayment(order, paymentClient) {
  return paymentClient.charge(order.total);
}

// Hard to mock
function processPayment(order) {
  const client = new StripeClient(process.env.STRIPE_KEY);
  return client.charge(order.total);
}
```

**2. Prefer SDK-style interfaces over generic fetchers**

Create specific functions for each external operation instead of one generic function with conditional logic:

```typescript
// GOOD: Each function is independently mockable
const api = {
  getUser: (id) => fetch(`/users/${id}`),
  getOrders: (userId) => fetch(`/users/${userId}/orders`),
  createOrder: (data) => fetch('/orders', { method: 'POST', body: data }),
};

// BAD: Mocking requires conditional logic inside the mock
const api = {
  fetch: (endpoint, options) => fetch(endpoint, options),
};
```

The SDK approach means:
- Each mock returns one specific shape
- No conditional logic in test setup
- Easier to see which endpoints a test exercises
- Type safety per endpoint

```

## File: skills\tdd\refactoring.md
```
# Refactor Candidates

After TDD cycle, look for:

- **Duplication** → Extract function/class
- **Long methods** → Break into private helpers (keep tests on public interface)
- **Shallow modules** → Combine or deepen
- **Feature envy** → Move logic to where data lives
- **Primitive obsession** → Introduce value objects
- **Existing code** the new code reveals as problematic

```

## File: skills\tdd\SKILL.md
```
---
name: tdd
description: Test-driven development with red-green-refactor loop. Use when user wants to build features or fix bugs using TDD, mentions "red-green-refactor", wants integration tests, or asks for test-first development.
---

# Test-Driven Development

## Philosophy

**Core principle**: Tests should verify behavior through public interfaces, not implementation details. Code can change entirely; tests shouldn't.

**Good tests** are integration-style: they exercise real code paths through public APIs. They describe _what_ the system does, not _how_ it does it. A good test reads like a specification - "user can checkout with valid cart" tells you exactly what capability exists. These tests survive refactors because they don't care about internal structure.

**Bad tests** are coupled to implementation. They mock internal collaborators, test private methods, or verify through external means (like querying a database directly instead of using the interface). The warning sign: your test breaks when you refactor, but behavior hasn't changed. If you rename an internal function and tests fail, those tests were testing implementation, not behavior.

See [tests.md](tests.md) for examples and [mocking.md](mocking.md) for mocking guidelines.

## Anti-Pattern: Horizontal Slices

**DO NOT write all tests first, then all implementation.** This is "horizontal slicing" - treating RED as "write all tests" and GREEN as "write all code."

This produces **crap tests**:

- Tests written in bulk test _imagined_ behavior, not _actual_ behavior
- You end up testing the _shape_ of things (data structures, function signatures) rather than user-facing behavior
- Tests become insensitive to real changes - they pass when behavior breaks, fail when behavior is fine
- You outrun your headlights, committing to test structure before understanding the implementation

**Correct approach**: Vertical slices via tracer bullets. One test → one implementation → repeat. Each test responds to what you learned from the previous cycle. Because you just wrote the code, you know exactly what behavior matters and how to verify it.

```
WRONG (horizontal):
  RED:   test1, test2, test3, test4, test5
  GREEN: impl1, impl2, impl3, impl4, impl5

RIGHT (vertical):
  RED→GREEN: test1→impl1
  RED→GREEN: test2→impl2
  RED→GREEN: test3→impl3
  ...
```

## Workflow

### 1. Planning

Before writing any code:

- [ ] Confirm with user what interface changes are needed
- [ ] Confirm with user which behaviors to test (prioritize)
- [ ] List the behaviors to test (not implementation steps)
- [ ] Get user approval on the plan

Ask: "What should the public interface look like? Which behaviors are most important to test?"

**You can't test everything.** Confirm with the user exactly which behaviors matter most. Focus testing effort on critical paths and complex logic, not every possible edge case.

### 2. Tracer Bullet

Write ONE test that confirms ONE thing about the system:

```
RED:   Write test for first behavior → test fails
GREEN: Write minimal code to pass → test passes
```

This is your tracer bullet - proves the path works end-to-end.

### 3. Incremental Loop

For each remaining behavior:

```
RED:   Write next test → fails
GREEN: Minimal code to pass → passes
```

Rules:

- One test at a time
- Only enough code to pass current test
- Don't anticipate future tests
- Keep tests focused on observable behavior

### 4. Refactor

After all tests pass, look for [refactor candidates](refactoring.md):

- [ ] Extract duplication
- [ ] Deepen modules (move complexity behind simple interfaces)
- [ ] Apply SOLID principles where natural
- [ ] Consider what new code reveals about existing code
- [ ] Run tests after each refactor step

**Never refactor while RED.** Get to GREEN first.

## Checklist Per Cycle

```
[ ] Test describes behavior, not implementation
[ ] Test uses public interface only
[ ] Test would survive internal refactor
[ ] Code is minimal for this test
[ ] No speculative features added
```

```

## File: skills\tdd\tests.md
```
# Good and Bad Tests

## Good Tests

**Integration-style**: Test through real interfaces, not mocks of internal parts.

```typescript
// GOOD: Tests observable behavior
test("user can checkout with valid cart", async () => {
  const cart = createCart();
  cart.add(product);
  const result = await checkout(cart, paymentMethod);
  expect(result.status).toBe("confirmed");
});
```

Characteristics:

- Tests behavior users/callers care about
- Uses public API only
- Survives internal refactors
- Describes WHAT, not HOW
- One logical assertion per test

## Bad Tests

**Implementation-detail tests**: Coupled to internal structure.

```typescript
// BAD: Tests implementation details
test("checkout calls paymentService.process", async () => {
  const mockPayment = jest.mock(paymentService);
  await checkout(cart, payment);
  expect(mockPayment.process).toHaveBeenCalledWith(cart.total);
});
```

Red flags:

- Mocking internal collaborators
- Testing private methods
- Asserting on call counts/order
- Test breaks when refactoring without behavior change
- Test name describes HOW not WHAT
- Verifying through external means instead of interface

```typescript
// BAD: Bypasses interface to verify
test("createUser saves to database", async () => {
  await createUser({ name: "Alice" });
  const row = await db.query("SELECT * FROM users WHERE name = ?", ["Alice"]);
  expect(row).toBeDefined();
});

// GOOD: Verifies through interface
test("createUser makes user retrievable", async () => {
  const user = await createUser({ name: "Alice" });
  const retrieved = await getUser(user.id);
  expect(retrieved.name).toBe("Alice");
});
```

```

## File: skills\tdd\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_config_144305-skills-tdd
name: Tdd
path: ecosystem/skills/repo_fetched_agent_config_144305/skills/tdd
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Tdd
Storage area for 'tdd' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills\workflow\SKILL.md
```
---
name: workflow
description: "Workflow orchestration for complex coding tasks. Use for ANY non-trivial task (3+ steps or architectural decisions) to enforce planning, subagent strategy, self-improvement, verification, elegance, and autonomous bug fixing. Triggers: multi-step implementation, bug fixes, refactoring, architectural changes, or any task requiring structured execution."
---

## Workflow Orchestration

### 1. Plan Mode Default

- Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions)
- If something goes sideways, STOP and re-plan immediately — don't keep pushing
- Use plan mode for verification steps, not just building
- Write detailed specs upfront to reduce ambiguity

### 2. Subagent Strategy

- Use subagents liberally to keep main context window clean
- Offload research, exploration, and parallel analysis to subagents
- For complex problems, throw more compute at it via subagents
- One task per subagent for focused execution

### 3. Self-Improvement Loop

- After ANY correction from the user: update `tasks/lessons.md` with the pattern
- Write rules for yourself that prevent the same mistake
- Ruthlessly iterate on these lessons until mistake rate drops
- Review lessons at session start for relevant project

### 4. Verification Before Done

- Never mark a task complete without proving it works
- Diff behavior between main and your changes when relevant
- Ask yourself: "Would a staff engineer approve this?"
- Run tests, check logs, demonstrate correctness

### 5. Demand Elegance (Balanced)

- For non-trivial changes: pause and ask "is there a more elegant way?"
- If a fix feels hacky: "Knowing everything I know now, implement the elegant solution"
- Skip this for simple, obvious fixes — don't over-engineer
- Challenge your own work before presenting it

### 6. Autonomous Bug Fixing

- When given a bug report: just fix it. Don't ask for hand-holding
- Point at logs, errors, failing tests — then resolve them
- Zero context switching required from the user
- Go fix failing CI tests without being told how

## Task Management

1. **Plan First**: Write plan to `tasks/todo.md` with checkable items
2. **Verify Plan**: Check in before starting implementation
3. **Track Progress**: Mark items complete as you go
4. **Explain Changes**: High-level summary at each step
5. **Document Results**: Add review section to `tasks/todo.md`
6. **Capture Lessons**: Update `tasks/lessons.md` after corrections

## Core Principles

- **Simplicity First**: Make every change as simple as possible. Impact minimal code.
- **No Laziness**: Find root causes. No temporary fixes. Senior developer standards.
- **Minimal Impact**: Changes should only touch what's necessary. Avoid introducing bugs.

```

## File: skills\workflow\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_config_144305-skills-workflow
name: Workflow
path: ecosystem/skills/repo_fetched_agent_config_144305/skills/workflow
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Workflow
Storage area for 'workflow' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: tests\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo_fetched_agent_config_144305-tests
name: Tests
path: ecosystem/skills/repo_fetched_agent_config_144305/tests
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Tests
Storage area for 'tests' domain.
> Auto-generated identity tag by OMA v2.1.

```

