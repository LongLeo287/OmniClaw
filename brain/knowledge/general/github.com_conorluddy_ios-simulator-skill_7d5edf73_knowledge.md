---
id: github.com-conorluddy-ios-simulator-skill-7d5edf73
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:41.898324
---

# KNOWLEDGE EXTRACT: github.com_conorluddy_ios-simulator-skill_7d5edf73
> **Extracted on:** 2026-04-01 07:53:39
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007519241/github.com_conorluddy_ios-simulator-skill_7d5edf73

---

## File: `.gitignore`
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# Python virtual environments
env/
venv/
ENV/
env.bak/
venv.bak/

# Python cache and build
.mypy_cache/
.ruff_cache/
.pytest_cache/
*.egg-info/
dist/
build/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# macOS
.DS_Store
.AppleDouble
.LSOverride

# Xcode (for testing)
*.xcodeproj/xcuserdata/
*.xcworkspace/xcuserdata/
DerivedData/
*.xcresult/

# Logs
*.log

# Temporary files
*.tmp
*.temp
.cache/

# Release artifacts (built by CI)
*.zip

# Local skill config (user-specific)
skill/scripts/.claude/skills/ios-simulator-skill/config.json

# Other
.claude
```

## File: `.pre-commit-config.yaml`
```yaml
# Pre-commit hooks for ios-simulator-skill
# Install: pre-commit install
# Run manually: pre-commit run --all-files

repos:
  # Black - Code formatter
  - repo: https://github.com/psf/black
    rev: 24.10.0
    hooks:
      - id: black
        name: Format Python code with Black
        language_version: python3.12
        files: ^skill/scripts/.*\.py$

  # Ruff - Fast linter (replaces Flake8, isort, etc)
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.7.4
    hooks:
      - id: ruff
        name: Lint with Ruff
        args: [--fix, --exit-non-zero-on-fix]
        files: ^skill/scripts/.*\.py$

  # General file checks
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: trailing-whitespace
        name: Trim trailing whitespace
      - id: end-of-file-fixer
        name: Fix end of files
      - id: check-yaml
        name: Check YAML syntax
      - id: check-added-large-files
        name: Check for large files
        args: ['--maxkb=500']
      - id: mixed-line-ending
        name: Fix mixed line endings
        args: ['--fix=lf']
```

## File: `CLAUDE.md`
```markdown
# CLAUDE.md - Developer Guide

This file provides guidance to Claude Code and developers working with this repository.

## Project Overview

iOS Simulator Skill is a production-ready Agent Skill providing 21 scripts for iOS app building, testing, and automation. It wraps Apple's `xcrun simctl` and Facebook's `idb` tools with semantic interfaces designed for AI agents and developers.

**Key Statistics:**
- 21 production scripts (~8,500 lines)
- 5 script categories (Build, Navigation, Testing, Permissions, Lifecycle)
- 6 shared utility modules (~1,400 lines)
- 100% token-optimized default output
- Full test coverage on all new features

## Project Structure

```
ios-simulator-skill/            # Repository root
├── ios-simulator-skill/        # Distributable package
│   ├── SKILL.md               # Entry point (table of contents)
│   └── scripts/               # 21 production scripts
│       ├── build_and_test.py
│       ├── xcode/             # Xcode integration module
│       ├── log_monitor.py
│       ├── screen_mapper.py
│       ├── navigator.py
│       ├── gesture.py
│       ├── keyboard.py
│       ├── app_launcher.py
│       ├── accessibility_audit.py
│       ├── visual_diff.py
│       ├── test_recorder.py
│       ├── app_state_capture.py
│       ├── clipboard.py
│       ├── status_bar.py
│       ├── push_notification.py
│       ├── privacy_manager.py
│       ├── simctl_boot.py
│       ├── simctl_shutdown.py
│       ├── simctl_create.py
│       ├── simctl_delete.py
│       ├── simctl_erase.py
│       ├── sim_health_check.sh
│       └── common/            # Shared utilities
├── .github/workflows/
├── pyproject.toml
└── README.md
```

## Architecture Patterns

### Pattern 1: Class-Based Script Design

All scripts use class-based architecture for testability:

```python
class DeviceManager:
    def __init__(self, udid: str | None = None):
        self.udid = udid

    def execute(self, **kwargs) -> tuple[bool, str]:
        # Return (success, message) tuple
        pass

def main():
    parser = argparse.ArgumentParser()
    manager = DeviceManager(args.udid)
    success, message = manager.execute()
    print(message)
    sys.exit(0 if success else 1)
```

### Pattern 2: Auto-UDID Detection

All scripts support optional `--udid` with auto-detection:

```python
try:
    udid = resolve_device_identifier(args.udid)  # May be None
except RuntimeError as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
```

### Pattern 3: Output Formatting

Consistent format across all scripts:

```
# Default (3-5 lines)
Device booted: iPhone 16 Pro (ABC123) [2.1s]

# --verbose (50+ lines)
Device booted successfully.
Device UDID: ABC123DEF456...
Boot time: 2.1 seconds

# --json (20-30 lines)
{"action": "boot", "udid": "ABC123", "success": true}
```

### Pattern 4: Batch Operations

Most scripts support batch operations:

```bash
python scripts/simctl_boot.py --all
python scripts/simctl_boot.py --type iPhone
```

## Script Categories

### Build & Development (2)
- **build_and_test.py**: Build with progressive disclosure
- **log_monitor.py**: Real-time log monitoring

### Navigation & Interaction (5)
- **screen_mapper.py**: Analyze screen
- **navigator.py**: Semantic element finding
- **gesture.py**: Touch simulation
- **keyboard.py**: Text input and keys
- **app_launcher.py**: App lifecycle

### Testing & Analysis (5)
- **accessibility_audit.py**: WCAG compliance
- **visual_diff.py**: Screenshot comparison
- **test_recorder.py**: Test documentation
- **app_state_capture.py**: Debugging snapshots
- **sim_health_check.sh**: Environment verification

### Advanced Testing & Permissions (4)
- **clipboard.py**: Clipboard management
- **status_bar.py**: Status bar control
- **push_notification.py**: Push notifications
- **privacy_manager.py**: Permission management

### Device Lifecycle Management (5)
- **simctl_boot.py**: Boot device
- **simctl_shutdown.py**: Shutdown device
- **simctl_create.py**: Create device
- **simctl_delete.py**: Delete device
- **simctl_erase.py**: Reset device

## Shared Utilities

### device_utils.py (~450 lines)
- `resolve_device_identifier()`: UDID/name/booted resolution
- `list_simulators()`: List with state filtering
- `_extract_device_type()`: Parse device type from name

### screenshot_utils.py (~346 lines)
- `capture_screenshot()`: File or inline mode
- `generate_screenshot_name()`: Semantic naming
- `resize_screenshot()`: Token optimization

### cache_utils.py (~258 lines)
- `ProgressiveCache`: Large output caching with TTL

## Quality Standards

1. Type hints (modern Python syntax)
2. Docstrings on all functions
3. Specific exception handling
4. --help support on all scripts
5. Black formatter compliance
6. Ruff linter (0 errors)
7. Never use shell=True

## Token Efficiency

96% reduction in typical output:

- Default: 3-5 lines (5-10 tokens)
- Verbose: 50+ lines (400+ tokens)
- JSON: 20-30 lines (20-30 tokens)

This keeps AI agent conversations focused and cost-effective.

## Contributing

New scripts should:
- Use class-based design for > 50 lines of logic
- Support --udid and auto-detection
- Support --json output
- Provide --help documentation
- Follow Black and Ruff standards
- Update SKILL.md table of contents
- Work with real simulators before submission

## Release Process

1. Update version in SKILL.md frontmatter, pyproject.toml
2. Verify CI passes (Black, Ruff)
3. Create GitHub release with vX.X.X tag
4. Attach zipped ios-simulator-skill/ directory

## Design Philosophy

**Semantic**: Find elements by meaning, not pixels.

**Progressive**: Minimal output by default, details on demand.

**Accessible**: Built on standard iOS accessibility APIs.

**Zero-Config**: Works immediately with no setup.

**Structured**: JSON and formatted text, not raw logs.

**Reusable**: Common patterns across all scripts.

This design works for both developers and AI agents.
```

## File: `DEV.md`
```markdown
# iOS Simulator Skill - Development Repository

This is the **development repository** for the iOS Simulator Skill. Users should download the packaged skill from [GitHub Releases](https://github.com/YOUR_USERNAME/ios-simulator-skill/releases).

## What is This?

A production-ready Claude Code skill providing 21+ scripts for iOS simulator testing and automation with:
- 🏗️ **Ultra token-efficient build automation** with progressive disclosure
- 🔍 **Real-time log monitoring** with intelligent filtering
- 🎯 **Accessibility-driven navigation** (semantic, not pixel-based)
- ♿ **WCAG accessibility auditing**
- 📸 **Visual regression testing**
- 🎬 **Test recording and documentation**

**Total:** ~10,000 lines of production Python code

## For Users: Installation

Download the latest release and extract to your Claude skills directory:

```bash
# Download from releases
curl -L https://github.com/YOUR_USERNAME/ios-simulator-skill/releases/latest/download/ios-simulator-skill-v1.0.0.zip -o skill.zip

# Extract to Claude Code skills directory
unzip skill.zip -d ~/.claude/skills/ios-simulator-skill

# Restart Claude Code
```

See [`ios-simulator-skill/SKILL.md`](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) for usage documentation.

## For Contributors: Development Setup

### Prerequisites

- macOS 11+ (required for iOS simulator)
- Xcode Command Line Tools: `xcode-select --install`
- Python 3.12+
- Git

### Setup

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/ios-simulator-skill.git
cd ios-simulator-skill

# Install development dependencies
pip3 install black ruff mypy pre-commit

# Install pre-commit hooks
pre-commit install

# Verify setup
pre-commit run --all-files
```

### Development Workflow

```bash
# Make changes to ios-simulator-skill/scripts/
vim ios-simulator-skill/scripts/build_and_test.py

# Hooks run automatically on commit (Black, Ruff, mypy)
git add ios-simulator-skill/scripts/build_and_test.py
git commit -m "feat: improve build error reporting"

# Push and create PR
git push origin feature-branch
# Open PR on GitHub - lint workflow runs automatically
```

### Linting Tools

All code in `ios-simulator-skill/scripts/` is checked with **STRICT** configuration:

- **Black** - Auto-formats to consistent style (line length: 100)
- **Ruff** - Fast linter catching bugs, style issues, unused imports
- **mypy** - Strict type checking (all type hints required)

Configuration in [`pyproject.toml`](pyproject.toml).

### Running Linters Manually

```bash
# Format code
black ios-simulator-skill/scripts/

# Lint code (with auto-fix)
ruff check --fix ios-simulator-skill/scripts/

# Type check
mypy ios-simulator-skill/scripts/

# Or run all checks
pre-commit run --all-files
```

### Repository Structure

```
ios-simulator-skill/                   # Repository root
├── ios-simulator-skill/               # Distributable package (packaged in releases)
│   ├── SKILL.md                      # Entry point with YAML frontmatter
│   └── scripts/                      # 21+ production scripts (~10,000 lines)
│
├── .github/workflows/                 # CI/CD automation
│   ├── release.yml                   # Auto-package on release
│   ├── lint.yml                      # Run linters on PRs
│   └── validate-version.yml          # Ensure version consistency
│
├── pyproject.toml                     # Linting configuration
├── .pre-commit-config.yaml            # Git hooks
└── README.md                          # This file (dev guide)
```

### Creating a Release

```bash
# 1. Update version in pyproject.toml
vim pyproject.toml  # Update version = "1.1.0"

# 2. Commit version bump
git add pyproject.toml
git commit -m "chore: bump version to 1.1.0"
git push origin main

# 3. Create and push tag
git tag v1.1.0
git push origin v1.1.0

# 4. Create GitHub release
# Go to: https://github.com/YOUR_USERNAME/ios-simulator-skill/releases/new
# - Tag: v1.1.0
# - Title: "Release v1.1.0"
# - Description: (auto-generated or write your own)
# - Publish release

# 5. GitHub Actions automatically:
#    - Validates version consistency
#    - Packages skill/ directory
#    - Attaches ios-simulator-skill-v1.1.0.zip to release
```

### Testing

```bash
# Test scripts locally with booted simulator
open -a Simulator

# Run health check
bash ios-simulator-skill/scripts/sim_health_check.sh

# Test individual scripts
python ios-simulator-skill/scripts/build_and_test.py --help
python ios-simulator-skill/scripts/screen_mapper.py

# Test skill installation
mkdir -p ~/.claude/skills/ios-simulator-skill-test
cp -r ios-simulator-skill/* ~/.claude/skills/ios-simulator-skill-test/
# Restart Claude Code and verify
```

## Code Style Guidelines

From [`CLAUDE.md`](CLAUDE.md):

- **Jackson's Law**: Minimal code to solve the problem
- **Guard clauses**: Validate inputs first, happy path last
- **Functions < 50 lines**: Keep functions focused
- **Files < 300 lines**: Keep modules understandable
- **Actionable errors**: Always explain what failed and how to fix
- **Type hints**: All functions use type annotations (enforced by mypy --strict)
- **Security**: Never `shell=True`, always validate paths

## GitHub Actions Workflows

### release.yml
- **Trigger:** When release is published
- **Actions:** Validate structure → Zip ios-simulator-skill/ → Upload to release

### lint.yml
- **Trigger:** On PR to main (for Python files)
- **Actions:** Run Black, Ruff, mypy → Block merge if fails

### validate-version.yml
- **Trigger:** On release published
- **Actions:** Check pyproject.toml version matches git tag

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make changes (hooks will run on commit)
4. Push and create a PR
5. Wait for lint workflow to pass
6. Request review

## License

MIT License - see [LICENSE.md](LICENSE.md)

## Questions?

- **Usage questions**: See [ios-simulator-skill/SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)
- **Bug reports**: [Open an issue](https://github.com/YOUR_USERNAME/ios-simulator-skill/issues)
- **Development questions**: [Open a discussion](https://github.com/YOUR_USERNAME/ios-simulator-skill/discussions)
```

## File: `LICENSE.md`
```markdown
MIT License

Copyright (c) 2025 Conor Luddy

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
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/conorluddy/ios-simulator-skill)

# iOS Simulator Skill for Claude Code

Production-ready automation for iOS app testing and building. 21 scripts optimized for both human developers and AI agents.

This is basically a Skill version of my XCode MCP: [https://github.com/conorluddy/xc-mcp](https://github.com/conorluddy/xc-mcp)


> [!WARNING]
> You want to take the `ios-simulator-skill` directory from this repo and drop it into your skills directory - not this entire repo. I'll update this soon with an easier approach. Feel free to fork this and get Claude to adjust it to your specific needs.


MCPs load a lot of tokens into the context window when they're active, but also seem to work really well. Skills don't load in any context. I'll make a plugin next and try to find the balance...

Updated: The Plugin version lets you easily disable MCPs for different tool groups. Optimise your context window by only enabling the tools you're actively using, such as xcodebuild: [https://github.com/conorluddy/xclaude-plugin](https://github.com/conorluddy/xclaude-plugin)

## What It Does

Instead of pixel-based navigation that breaks when UI changes:

```bash
# Fragile - breaks if UI changes
idb ui tap 320 400

# Robust - finds by meaning
python scripts/navigator.py --find-text "Login" --tap
```

Uses semantic navigation on accessibility APIs to interact with elements by their meaning, not coordinates. Works across different screen sizes and survives UI redesigns.

## Features

- **21 production scripts** for building, testing, and automation
- **Semantic navigation** - find elements by text, type, or ID
- **Token optimized** - 96% reduction vs raw tools (3-5 lines default)
- **Zero configuration** - works immediately on macOS with Xcode
- **Structured output** - JSON and formatted text, easy to parse
- **Auto-UDID detection** - no need to specify device each time
- **Batch operations** - boot, delete, erase multiple simulators at once
- **Comprehensive testing** - WCAG compliance, visual diffs, accessibility audits
- **CI/CD ready** - JSON output, exit codes, automated device lifecycle

## Installation

### As Claude Code Skill

```bash
# Personal installation
git clone https://github.com/conorluddy/ios-simulator-skill.git ~/.claude/skills/ios-simulator-skill

# Project installation
git clone https://github.com/conorluddy/ios-simulator-skill.git .claude/skills/ios-simulator-skill
```

Restart Claude Code. The skill loads automatically.

### From Release

```bash
# Download latest release
curl -L https://github.com/conorluddy/ios-simulator-skill/releases/download/vX.X.X/ios-simulator-skill-vX.X.X.zip -o skill.zip

# Extract
unzip skill.zip -d ~/.claude/skills/ios-simulator-skill
```

## Prerequisites

- macOS 12+
- Xcode Command Line Tools (`xcode-select --install`)
- Python 3
- IDB (optional, for interactive features: `brew tap facebook/fb && brew install idb-companion`)

## Quick Start

```bash
# 1. Check environment
bash ~/.claude/skills/ios-simulator-skill/scripts/sim_health_check.sh

# 2. Launch your app
python ~/.claude/skills/ios-simulator-skill/scripts/app_launcher.py --launch com.example.app

# 3. See what's on screen
python ~/.claude/skills/ios-simulator-skill/scripts/screen_mapper.py
# Output:
# Screen: LoginViewController (45 elements, 7 interactive)
# Buttons: "Login", "Cancel", "Forgot Password"
# TextFields: 2 (0 filled)

# 4. Tap login button
python ~/.claude/skills/ios-simulator-skill/scripts/navigator.py --find-text "Login" --tap

# 5. Enter text
python ~/.claude/skills/ios-simulator-skill/scripts/navigator.py --find-type TextField --enter-text "user@test.com"

# 6. Check accessibility
python ~/.claude/skills/ios-simulator-skill/scripts/accessibility_audit.py
```

## 21 Scripts Organized by Category

### Build & Development
- **build_and_test.py** - Build projects, run tests, parse results
- **log_monitor.py** - Real-time log monitoring

### Navigation & Interaction
- **screen_mapper.py** - Analyze current screen
- **navigator.py** - Find and interact with elements
- **gesture.py** - Swipes, scrolls, pinches
- **keyboard.py** - Text input and hardware buttons
- **app_launcher.py** - App lifecycle control

### Testing & Analysis
- **accessibility_audit.py** - WCAG compliance checking
- **visual_diff.py** - Screenshot comparison
- **test_recorder.py** - Automated test documentation
- **app_state_capture.py** - Debugging snapshots
- **sim_health_check.sh** - Environment verification

### Advanced Testing & Permissions
- **clipboard.py** - Clipboard management
- **status_bar.py** - Status bar control
- **push_notification.py** - Push notifications
- **privacy_manager.py** - Permission management

### Device Lifecycle
- **simctl_boot.py** - Boot simulator
- **simctl_shutdown.py** - Shutdown simulator
- **simctl_create.py** - Create simulator
- **simctl_delete.py** - Delete simulator
- **simctl_erase.py** - Factory reset

See **SKILL.md** for complete reference.

## How It Works with Claude Code

Claude Code automatically detects when to use this skill based on your request. You don't need to manually invoke it.

**Example conversation:**

```
You: "Set up my iOS app for testing"
Claude: [Uses simctl_boot.py and app_launcher.py automatically]

You: "Tap the login button"
Claude: [Uses navigator.py to find and tap]

You: "Check if the form is accessible"
Claude: [Uses accessibility_audit.py]
```

You can also run scripts manually when needed.

## Usage Examples

### Example 1: Login Flow

```bash
# Launch app
python scripts/app_launcher.py --launch com.example.app

# Map screen to find fields
python scripts/screen_mapper.py

# Enter credentials
python scripts/navigator.py --find-type TextField --index 0 --enter-text "user@test.com"
python scripts/navigator.py --find-type SecureTextField --enter-text "password"

# Tap login
python scripts/navigator.py --find-text "Login" --tap

# Verify accessibility
python scripts/accessibility_audit.py
```

### Example 2: Test Documentation

```bash
# Record test execution
python scripts/test_recorder.py --test-name "Login Flow" --output test-reports/

# Generates:
# - Screenshots per step
# - Accessibility trees
# - Markdown report with timing
```

### Example 3: Visual Testing

```bash
# Capture baseline
python scripts/app_state_capture.py --output baseline/

# Make changes...

# Compare
python scripts/visual_diff.py baseline/screenshot.png current/screenshot.png
```

### Example 4: Permission Testing

```bash
# Grant permissions
python scripts/privacy_manager.py --bundle-id com.example.app --grant camera,location

# Test app behavior with permissions...

# Revoke permissions
python scripts/privacy_manager.py --bundle-id com.example.app --revoke camera,location
```

### Example 5: Device Lifecycle in CI/CD

```bash
# Create test device
DEVICE_ID=$(python scripts/simctl_create.py --device "iPhone 16 Pro" --json | jq -r '.new_udid')

# Run tests
python scripts/build_and_test.py --project MyApp.xcodeproj

# Clean up
python scripts/simctl_delete.py --udid $DEVICE_ID --yes
```

## Design Principles

**Semantic Navigation**: Find elements by meaning (text, type, ID) not pixel coordinates. Survives UI changes and works across device sizes.

**Token Efficiency**: Default output is 3-5 lines. Use `--verbose` for details or `--json` for machine parsing. 96% reduction vs raw tools.

**Accessibility-First**: Built on iOS accessibility APIs for reliability. Better for users with accessibility needs and more robust for automation.

**Zero Configuration**: Works immediately on any macOS with Xcode. No complex setup, no configuration files.

**Structured Data**: Scripts output JSON or formatted text, not raw logs. Easy to parse, integrate, and understand.

**Auto-Learning**: Build system learns your device preference and remembers it for next time.

## Requirements

**System:**
- macOS 12 or later
- Xcode Command Line Tools
- Python 3

**Optional:**
- IDB (for interactive features)
- Pillow (for visual_diff.py: `pip3 install pillow`)

## Documentation

- **SKILL.md** - Complete script reference and table of contents
- **CLAUDE.md** - Architecture and developer guide
- **references/** - Deep documentation on specific topics
- **examples/** - Complete automation workflows

## Output Efficiency

All scripts minimize output by default:

| Task | Raw Tools | This Skill | Savings |
|------|-----------|-----------|---------|
| Screen analysis | 200+ lines | 5 lines | 97.5% |
| Find & tap button | 100+ lines | 1 line | 99% |
| Enter text | 50+ lines | 1 line | 98% |
| Login flow | 400+ lines | 15 lines | 96% |

This efficiency keeps AI agent conversations focused and cost-effective.

## Evaluation

This skill is tested using [Claude Code evals](https://docs.claude.com/en/brain/knowledge/docs_legacy/claude-code/evals) — automated benchmarks that compare agent performance with and without the skill installed.

### Results (Iteration 1)

| Condition | Pass Rate |
|-----------|-----------|
| With skill | **100%** (3/3) |
| Without skill | **46%** (≈1.4/3) |

### What's Tested

Three eval scenarios cover the skill's core capabilities:

1. **Environment & Discovery** — Health check, list simulators, identify booted device
2. **Build & Navigate** — Build an app, launch it, map the screen, tap a button
3. **Test & Capture** — Accessibility audit, app state snapshot, status bar override

Each eval checks that the agent uses skill scripts (not raw `xcrun simctl`), follows progressive disclosure, and completes all requested steps.

### Running Evals

```bash
# From repo root
claude evals run evals/evals.json --skill ios-simulator-skill
```

Eval definitions live in `evals/evals.json`.

## Troubleshooting

### Environment Issues

```bash
# Run health check
bash ~/.claude/skills/ios-simulator-skill/scripts/sim_health_check.sh

# Checks: macOS, Xcode, simctl, IDB, Python, simulators, packages
```

### Script Help

```bash
# All scripts support --help
python scripts/navigator.py --help
python scripts/accessibility_audit.py --help
```

### Not Finding Elements

```bash
# Use verbose mode to see all elements
python scripts/screen_mapper.py --verbose

# Check for exact text match
python scripts/navigator.py --find-text "Exact Button Text" --tap
```

## Contributing

> [!WARNING]
> I appreciate contributions, but please note that this repo and my other public repos are far down in the priority queue of what I'm working on, so I'll be slow to review anything. Your best bet is really just to fork the repo and customise it to your own needs.

Contributions should:
- Maintain token efficiency (minimal default output)
- Follow accessibility-first design
- Support `--help` documentation
- Support `--json` for CI/CD
- Pass Black formatter and Ruff linter
- Include type hints
- Update SKILL.md

## License

MIT License - Allows commercial use and distribution.

## Support

- **Issues**: Create GitHub issue with reproduction steps
- **Documentation**: See SKILL.md and references/
- **Examples**: Check examples/ directory
- **Skills Docs**: https://docs.claude.com/en/brain/knowledge/docs_legacy/claude-code/skills

---

**Built for AI agents. Optimized for developers.**
```

## File: `pyproject.toml`
```
[project]
name = "ios-simulator-skill"
version = "1.3.0"
description = "Build, test, and automate iOS apps with accessibility-driven navigation"
readme = "README.md"
requires-python = ">=3.12"
license = {file = "LICENSE.md"}

[tool.black]
line-length = 100
target-version = ["py312"]
include = '\.pyi?$'
extend-exclude = '''
/(
    \.git
  | \.ruff_cache
  | \.venv
  | build
  | dist
)/
'''

[tool.ruff]
line-length = 100
target-version = "py312"
# Only check skill code, not root-level dev scripts
include = ["ios-simulator-skill/scripts/**/*.py"]

[tool.ruff.lint]
# Enable ALL recommended rules (strict mode)
select = [
    "E",      # pycodestyle errors
    "W",      # pycodestyle warnings
    "F",      # pyflakes
    "I",      # isort
    "N",      # pep8-naming
    "UP",     # pyupgrade
    "B",      # flake8-bugbear
    "C4",     # flake8-comprehensions
    "SIM",    # flake8-simplify
    "RET",    # flake8-return
    "ARG",    # flake8-unused-arguments
    "PTH",    # flake8-use-pathlib
    "PL",     # pylint
    "RUF",    # ruff-specific rules
]

# Strict mode with pragmatic exceptions for CLI tools
ignore = [
    "PLR0913",  # Too many arguments - common in CLI tools
    "PLR2004",  # Magic values - acceptable for coordinates/constants
    "PLR0912",  # Too many branches - acceptable for CLI scripts
    "PLR0915",  # Too many statements - acceptable for main() functions
    "PLR0911",  # Too many return statements
    "PLC0415",  # Import outside top-level - lazy imports are intentional
    "PTH123",   # Use Path.open() - open() is fine for simple cases
    "PTH119",   # Use Path - os.path is fine for simple cases
    "E501",     # Line too long - Black handles this, some long lines OK
    "E722",     # Bare except - acceptable for top-level error handling
    "RUF012",   # Mutable class attributes - acceptable for constants
    "RUF001",   # Ambiguous characters - intentional use of emoji
    "RUF005",   # Iterable unpacking - list concatenation is readable
    "ARG001",   # Unused function arguments - required by signal handlers
    "SIM102",   # Nested if statements - more readable in some cases
    "PLW2901",  # Redefined loop variable - acceptable in some contexts
    "F401",     # Unused import - may be used in __init__.py exports
    "N806",     # Non-lowercase variable - acceptable for constants
]

[tool.ruff.lint.isort]
known-first-party = ["xcode"]
```

## File: `ios-simulator-skill/SKILL.md`
```markdown
---
name: ios-simulator-skill
version: 1.3.0
description: 21 production-ready scripts for iOS app testing, building, and automation. Provides semantic UI navigation, build automation, accessibility testing, and simulator lifecycle management. Optimized for AI agents with minimal token output.
---

# iOS Simulator Skill

Build, test, and automate iOS applications using accessibility-driven navigation and structured data instead of pixel coordinates.

## Quick Start

```bash
# 1. Check environment
bash scripts/sim_health_check.sh

# 2. Launch app
python scripts/app_launcher.py --launch com.example.app

# 3. Map screen to see elements
python scripts/screen_mapper.py

# 4. Tap button
python scripts/navigator.py --find-text "Login" --tap

# 5. Enter text
python scripts/navigator.py --find-type TextField --enter-text "user@example.com"
```

All scripts support `--help` for detailed options and `--json` for machine-readable output.

## Navigation Strategy

**Always prefer the accessibility tree over screenshots for navigation.** The accessibility tree gives you element types, labels, frames, and tap targets — structured data that's cheaper and more reliable than image analysis.

Use this priority:
1. `screen_mapper.py` → structured element list (5-7 lines, ~10 tokens)
2. `navigator.py --find-text/--find-type/--find-id` → semantic interaction
3. Screenshots → only for visual verification, bug reports, or visual diff

Screenshots cost 1,600–6,300 tokens depending on size. The accessibility tree costs 10–50 tokens in default mode.

## 21 Production Scripts

### Build & Development (2 scripts)

1. **build_and_test.py** - Build Xcode projects, run tests, parse results with progressive disclosure
   - Build with live result streaming
   - Parse errors and warnings from xcresult bundles
   - Retrieve detailed build logs on demand
   - Options: `--project`, `--scheme`, `--clean`, `--test`, `--verbose`, `--json`

2. **log_monitor.py** - Real-time log monitoring with intelligent filtering
   - Stream logs or capture by duration
   - Filter by severity (error/warning/info/debug)
   - Deduplicate repeated messages
   - Options: `--app`, `--severity`, `--follow`, `--duration`, `--output`, `--json`

### Navigation & Interaction (5 scripts)

3. **screen_mapper.py** - Analyze current screen and list interactive elements
   - Element type breakdown
   - Interactive button list
   - Text field status
   - Options: `--verbose`, `--hints`, `--json`

4. **navigator.py** - Find and interact with elements semantically
   - Find by text (fuzzy matching)
   - Find by element type
   - Find by accessibility ID
   - Enter text or tap elements
   - Options: `--find-text`, `--find-type`, `--find-id`, `--tap`, `--enter-text`, `--json`

5. **gesture.py** - Perform swipes, scrolls, pinches, and complex gestures
   - Directional swipes (up/down/left/right)
   - Multi-swipe scrolling
   - Pinch zoom
   - Long press
   - Pull to refresh
   - Options: `--swipe`, `--scroll`, `--pinch`, `--long-press`, `--refresh`, `--json`

6. **keyboard.py** - Text input and hardware button control
   - Type text (fast or slow)
   - Special keys (return, delete, tab, space, arrows)
   - Hardware buttons (home, lock, volume, screenshot)
   - Key combinations
   - Options: `--type`, `--key`, `--button`, `--slow`, `--clear`, `--dismiss`, `--json`

7. **app_launcher.py** - App lifecycle management
   - Launch apps by bundle ID
   - Terminate apps
   - Install/uninstall from .app bundles
   - Deep link navigation
   - List installed apps
   - Check app state
   - Options: `--launch`, `--terminate`, `--install`, `--uninstall`, `--open-url`, `--list`, `--state`, `--json`

### Testing & Analysis (5 scripts)

8. **accessibility_audit.py** - Check WCAG compliance on current screen
   - Critical issues (missing labels, empty buttons, no alt text)
   - Warnings (missing hints, small touch targets)
   - Info (missing IDs, deep nesting)
   - Options: `--verbose`, `--output`, `--json`

9. **visual_diff.py** - Compare two screenshots for visual changes
   - Pixel-by-pixel comparison
   - Threshold-based pass/fail
   - Generate diff images
   - Options: `--threshold`, `--output`, `--details`, `--json`

10. **test_recorder.py** - Automatically document test execution
    - Capture screenshots and accessibility trees per step
    - Generate markdown reports with timing data
    - Options: `--test-name`, `--output`, `--verbose`, `--json`

11. **app_state_capture.py** - Create comprehensive debugging snapshots
    - Screenshot, UI hierarchy, app logs, device info
    - Markdown summary for bug reports
    - Options: `--app-bundle-id`, `--output`, `--log-lines`, `--json`

12. **sim_health_check.sh** - Verify environment is properly configured
    - Check macOS, Xcode, simctl, IDB, Python
    - List available and booted simulators
    - Verify Python packages (Pillow)

### Advanced Testing & Permissions (4 scripts)

13. **clipboard.py** - Manage simulator clipboard for paste testing
    - Copy text to clipboard
    - Test paste flows without manual entry
    - Options: `--copy`, `--test-name`, `--expected`, `--json`

14. **status_bar.py** - Override simulator status bar appearance
    - Presets: clean (9:41, 100% battery), testing (11:11, 50%), low-battery (20%), airplane (offline)
    - Custom time, network, battery, WiFi settings
    - Options: `--preset`, `--time`, `--data-network`, `--battery-level`, `--clear`, `--json`

15. **push_notification.py** - Send simulated push notifications
    - Simple mode (title + body + badge)
    - Custom JSON payloads
    - Test notification handling and deep links
    - Options: `--bundle-id`, `--title`, `--body`, `--badge`, `--payload`, `--json`

16. **privacy_manager.py** - Grant, revoke, and reset app permissions
    - 13 supported services (camera, microphone, location, contacts, photos, calendar, health, etc.)
    - Batch operations (comma-separated services)
    - Audit trail with test scenario tracking
    - Options: `--bundle-id`, `--grant`, `--revoke`, `--reset`, `--list`, `--json`

### Device Lifecycle Management (5 scripts)

17. **simctl_boot.py** - Boot simulators with optional readiness verification
    - Boot by UDID or device name
    - Wait for device ready with timeout
    - Batch boot operations (--all, --type)
    - Performance timing
    - Options: `--udid`, `--name`, `--wait-ready`, `--timeout`, `--all`, `--type`, `--json`

18. **simctl_shutdown.py** - Gracefully shutdown simulators
    - Shutdown by UDID or device name
    - Optional verification of shutdown completion
    - Batch shutdown operations
    - Options: `--udid`, `--name`, `--verify`, `--timeout`, `--all`, `--type`, `--json`

19. **simctl_create.py** - Create simulators dynamically
    - Create by device type and iOS version
    - List available device types and runtimes
    - Custom device naming
    - Returns UDID for CI/CD integration
    - Options: `--device`, `--runtime`, `--name`, `--list-devices`, `--list-runtimes`, `--json`

20. **simctl_delete.py** - Permanently delete simulators
    - Delete by UDID or device name
    - Safety confirmation by default (skip with --yes)
    - Batch delete operations
    - Smart deletion (--old N to keep N per device type)
    - Options: `--udid`, `--name`, `--yes`, `--all`, `--type`, `--old`, `--json`

21. **simctl_erase.py** - Factory reset simulators without deletion
    - Preserve device UUID (faster than delete+create)
    - Erase all, by type, or booted simulators
    - Optional verification
    - Options: `--udid`, `--name`, `--verify`, `--timeout`, `--all`, `--type`, `--booted`, `--json`

## Common Patterns

**Auto-UDID Detection**: Most scripts auto-detect the booted simulator if --udid is not provided.

**Device Name Resolution**: Use device names (e.g., "iPhone 16 Pro") instead of UDIDs - scripts resolve automatically.

**Batch Operations**: Many scripts support `--all` for all simulators or `--type iPhone` for device type filtering.

**Output Formats**: Default is concise human-readable output. Use `--json` for machine-readable output in CI/CD.

**Help**: All scripts support `--help` for detailed options and examples.

**Screenshot Sizing**: Screenshots are resized to save tokens. Presets: `full` (3-4 tiles, ~5K tokens), `half` (1 tile, ~1.6K tokens, default), `quarter` (1 tile, ~800 tokens, less detail). Use `quarter` for quick visual checks, `half` for readable UI, `full` only when pixel-level detail matters. Scripts that capture screenshots (`app_state_capture.py`, `test_recorder.py`) default to `half`.

## Typical Workflow

1. Verify environment: `bash scripts/sim_health_check.sh`
2. Launch app: `python scripts/app_launcher.py --launch com.example.app`
3. Analyze screen: `python scripts/screen_mapper.py`
4. Interact: `python scripts/navigator.py --find-text "Button" --tap`
5. Verify: `python scripts/accessibility_audit.py`
6. Debug if needed: `python scripts/app_state_capture.py --app-bundle-id com.example.app`

## Requirements

- macOS 12+
- Xcode Command Line Tools
- Python 3
- IDB (optional, for interactive features)

## Documentation

- **SKILL.md** (this file) - Script reference and quick start
- **README.md** - Installation and examples
- **CLAUDE.md** - Architecture and implementation details
- **references/** - Deep documentation on specific topics
- **examples/** - Complete automation workflows

## Key Design Principles

**Semantic Navigation**: Find elements by meaning (text, type, ID) not pixel coordinates. Survives UI changes.

**Token Efficiency**: Concise default output (3-5 lines) with optional verbose and JSON modes for detailed results.

**Accessibility-First**: Built on standard accessibility APIs for reliability and compatibility.

**Zero Configuration**: Works immediately on any macOS with Xcode. No setup required.

**Structured Data**: Scripts output JSON or formatted text, not raw logs. Easy to parse and integrate.

**Auto-Learning**: Build system remembers your device preference. Configuration stored per-project.

---

Use these scripts directly or let Claude Code invoke them automatically when your request matches the skill description.
```

## File: `ios-simulator-skill/scripts/accessibility_audit.py`
```python
#!/usr/bin/env python3
"""
iOS Simulator Accessibility Audit

Scans the current simulator screen for accessibility compliance issues.
Optimized for minimal token output while maintaining functionality.

Usage: python scripts/accessibility_audit.py [options]
"""

import argparse
import json
import subprocess
import sys
from dataclasses import asdict, dataclass
from typing import Any

from common import flatten_tree, get_accessibility_tree, resolve_udid


@dataclass
class Issue:
    """Represents an accessibility issue."""

    severity: str  # critical, warning, info
    rule: str
    element_type: str
    issue: str
    fix: str

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return asdict(self)


class AccessibilityAuditor:
    """Performs accessibility audits on iOS simulator screens."""

    # Critical rules that block users
    CRITICAL_RULES = {
        "missing_label": lambda e: e.get("type") in ["Button", "Link"] and not e.get("AXLabel"),
        "empty_button": lambda e: e.get("type") == "Button"
        and not (e.get("AXLabel") or e.get("AXValue")),
        "image_no_alt": lambda e: e.get("type") == "Image" and not e.get("AXLabel"),
    }

    # Warnings that degrade UX
    WARNING_RULES = {
        "missing_hint": lambda e: e.get("type") in ["Slider", "TextField"] and not e.get("help"),
        "missing_traits": lambda e: e.get("type") and not e.get("traits"),
    }

    # Info level suggestions
    INFO_RULES = {
        "no_identifier": lambda e: not e.get("AXUniqueId"),
        "deep_nesting": lambda e: e.get("depth", 0) > 5,
    }

    def __init__(self, udid: str | None = None):
        """Initialize auditor with optional device UDID."""
        self.udid = udid

    def get_accessibility_tree(self) -> dict:
        """Fetch accessibility tree from simulator using shared utility."""
        return get_accessibility_tree(self.udid, nested=True)

    @staticmethod
    def _is_small_target(element: dict) -> bool:
        """Check if touch target is too small (< 44x44 points)."""
        frame = element.get("frame", {})
        width = frame.get("width", 0)
        height = frame.get("height", 0)
        return width < 44 or height < 44

    def _flatten_tree(self, node: dict, depth: int = 0) -> list[dict]:
        """Flatten nested accessibility tree for easier processing using shared utility."""
        return flatten_tree(node, depth)

    def audit_element(self, element: dict) -> list[Issue]:
        """Audit a single element for accessibility issues."""
        issues = []

        # Check critical rules
        for rule_name, rule_func in self.CRITICAL_RULES.items():
            if rule_func(element):
                issues.append(
                    Issue(
                        severity="critical",
                        rule=rule_name,
                        element_type=element.get("type", "Unknown"),
                        issue=self._get_issue_description(rule_name),
                        fix=self._get_fix_suggestion(rule_name),
                    )
                )

        # Check warnings (skip if critical issues found)
        if not issues:
            for rule_name, rule_func in self.WARNING_RULES.items():
                if rule_func(element):
                    issues.append(
                        Issue(
                            severity="warning",
                            rule=rule_name,
                            element_type=element.get("type", "Unknown"),
                            issue=self._get_issue_description(rule_name),
                            fix=self._get_fix_suggestion(rule_name),
                        )
                    )

        # Check info level (only if verbose or no other issues)
        if not issues:
            for rule_name, rule_func in self.INFO_RULES.items():
                if rule_func(element):
                    issues.append(
                        Issue(
                            severity="info",
                            rule=rule_name,
                            element_type=element.get("type", "Unknown"),
                            issue=self._get_issue_description(rule_name),
                            fix=self._get_fix_suggestion(rule_name),
                        )
                    )

        return issues

    def _get_issue_description(self, rule: str) -> str:
        """Get human-readable issue description."""
        descriptions = {
            "missing_label": "Interactive element missing accessibility label",
            "empty_button": "Button has no text or label",
            "image_no_alt": "Image missing alternative text",
            "missing_hint": "Complex control missing hint",
            "small_touch_target": "Touch target smaller than 44x44pt",
            "missing_traits": "Element missing accessibility traits",
            "no_identifier": "Missing accessibility identifier",
            "deep_nesting": "Deeply nested (>5 levels)",
        }
        return descriptions.get(rule, "Accessibility issue")

    def _get_fix_suggestion(self, rule: str) -> str:
        """Get fix suggestion for issue."""
        fixes = {
            "missing_label": "Add accessibilityLabel",
            "empty_button": "Set button title or accessibilityLabel",
            "image_no_alt": "Add accessibilityLabel with description",
            "missing_hint": "Add accessibilityHint",
            "small_touch_target": "Increase to minimum 44x44pt",
            "missing_traits": "Set appropriate accessibilityTraits",
            "no_identifier": "Add accessibilityIdentifier for testing",
            "deep_nesting": "Simplify view hierarchy",
        }
        return fixes.get(rule, "Review accessibility")

    def audit(self, verbose: bool = False) -> dict[str, Any]:
        """Perform full accessibility audit."""
        # Get accessibility tree
        tree = self.get_accessibility_tree()

        # Flatten for processing
        elements = self._flatten_tree(tree)

        # Audit each element
        all_issues = []
        for element in elements:
            issues = self.audit_element(element)
            for issue in issues:
                issue_dict = issue.to_dict()
                # Add minimal element info for context
                issue_dict["element"] = {
                    "type": element.get("type", "Unknown"),
                    "label": element.get("AXLabel", "")[:30] if element.get("AXLabel") else None,
                }
                all_issues.append(issue_dict)

        # Count by severity
        critical = len([i for i in all_issues if i["severity"] == "critical"])
        warning = len([i for i in all_issues if i["severity"] == "warning"])
        info = len([i for i in all_issues if i["severity"] == "info"])

        # Build result (token-optimized)
        result = {
            "summary": {
                "total": len(elements),
                "issues": len(all_issues),
                "critical": critical,
                "warning": warning,
                "info": info,
            }
        }

        if verbose:
            # Full details only if requested
            result["issues"] = all_issues
        else:
            # Default: top issues only (token-efficient)
            result["top_issues"] = self._get_top_issues(all_issues)

        return result

    def _get_top_issues(self, issues: list[dict]) -> list[dict]:
        """Get top 3 issues grouped by type (token-efficient)."""
        if not issues:
            return []

        # Group by rule
        grouped = {}
        for issue in issues:
            rule = issue["rule"]
            if rule not in grouped:
                grouped[rule] = {
                    "severity": issue["severity"],
                    "rule": rule,
                    "count": 0,
                    "fix": issue["fix"],
                }
            grouped[rule]["count"] += 1

        # Sort by severity and count
        severity_order = {"critical": 0, "warning": 1, "info": 2}
        sorted_issues = sorted(
            grouped.values(), key=lambda x: (severity_order[x["severity"]], -x["count"])
        )

        return sorted_issues[:3]


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Audit iOS simulator screen for accessibility issues"
    )
    parser.add_argument(
        "--udid",
        help="Device UDID (auto-detects booted simulator if not provided)",
    )
    parser.add_argument("--output", help="Save JSON report to file")
    parser.add_argument(
        "--verbose", action="store_true", help="Include all issue details (increases output)"
    )

    args = parser.parse_args()

    # Resolve UDID with auto-detection
    try:
        udid = resolve_udid(args.udid)
    except RuntimeError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Perform audit
    auditor = AccessibilityAuditor(udid=udid)

    try:
        result = auditor.audit(verbose=args.verbose)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Output results
    if args.output:
        # Save to file
        with open(args.output, "w") as f:
            json.dump(result, f, indent=2)
        # Print minimal summary
        summary = result["summary"]
        print(f"Audit complete: {summary['issues']} issues ({summary['critical']} critical)")
        print(f"Report saved to: {args.output}")
    # Print to stdout (token-optimized by default)
    elif args.verbose:
        print(json.dumps(result, indent=2))
    else:
        # Ultra-compact output
        summary = result["summary"]
        print(f"Elements: {summary['total']}, Issues: {summary['issues']}")
        print(
            f"Critical: {summary['critical']}, Warning: {summary['warning']}, Info: {summary['info']}"
        )

        if result.get("top_issues"):
            print("\nTop issues:")
            for issue in result["top_issues"]:
                print(
                    f"  [{issue['severity']}] {issue['rule']} ({issue['count']}x) - {issue['fix']}"
                )

    # Exit with error if critical issues found
    if result["summary"]["critical"] > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
```

## File: `ios-simulator-skill/scripts/app_launcher.py`
```python
#!/usr/bin/env python3
"""
iOS App Launcher - App Lifecycle Control

Launches, terminates, and manages iOS apps in the simulator.
Handles deep links and app switching.

Usage: python scripts/app_launcher.py --launch com.example.app
"""

import argparse
import contextlib
import subprocess
import sys
import time

from common import build_simctl_command, resolve_udid


class AppLauncher:
    """Controls app lifecycle on iOS simulator."""

    def __init__(self, udid: str | None = None):
        """Initialize app launcher."""
        self.udid = udid

    def launch(self, bundle_id: str, wait_for_debugger: bool = False) -> tuple[bool, int | None]:
        """
        Launch an app.

        Args:
            bundle_id: App bundle identifier
            wait_for_debugger: Wait for debugger attachment

        Returns:
            (success, pid) tuple
        """
        cmd = build_simctl_command("launch", self.udid, bundle_id)

        if wait_for_debugger:
            cmd.insert(3, "--wait-for-debugger")  # Insert after "launch" operation

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            # Parse PID from output if available
            pid = None
            if result.stdout:
                # Output format: "com.example.app: <PID>"
                parts = result.stdout.strip().split(":")
                if len(parts) > 1:
                    with contextlib.suppress(ValueError):
                        pid = int(parts[1].strip())
            return (True, pid)
        except subprocess.CalledProcessError:
            return (False, None)

    def terminate(self, bundle_id: str) -> bool:
        """
        Terminate an app.

        Args:
            bundle_id: App bundle identifier

        Returns:
            Success status
        """
        cmd = build_simctl_command("terminate", self.udid, bundle_id)

        try:
            subprocess.run(cmd, capture_output=True, check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def install(self, app_path: str) -> bool:
        """
        Install an app.

        Args:
            app_path: Path to .app bundle

        Returns:
            Success status
        """
        cmd = build_simctl_command("install", self.udid, app_path)

        try:
            subprocess.run(cmd, capture_output=True, check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def uninstall(self, bundle_id: str) -> bool:
        """
        Uninstall an app.

        Args:
            bundle_id: App bundle identifier

        Returns:
            Success status
        """
        cmd = build_simctl_command("uninstall", self.udid, bundle_id)

        try:
            subprocess.run(cmd, capture_output=True, check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def open_url(self, url: str) -> bool:
        """
        Open URL (for deep linking).

        Args:
            url: URL to open (http://, myapp://, etc.)

        Returns:
            Success status
        """
        cmd = build_simctl_command("openurl", self.udid, url)

        try:
            subprocess.run(cmd, capture_output=True, check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def list_apps(self) -> list[dict[str, str]]:
        """
        List installed apps.

        Returns:
            List of app info dictionaries
        """
        cmd = build_simctl_command("listapps", self.udid)

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)

            # Parse plist output using plutil to convert to JSON
            plist_data = result.stdout

            # Use plutil to convert plist to JSON
            convert_cmd = ["plutil", "-convert", "json", "-o", "-", "-"]
            convert_result = subprocess.run(
                convert_cmd, check=False, input=plist_data, capture_output=True, text=True
            )

            apps = []
            if convert_result.returncode == 0:
                import json

                try:
                    data = json.loads(convert_result.stdout)
                    for bundle_id, app_info in data.items():
                        # Skip system internal apps that are hidden
                        if app_info.get("ApplicationType") == "Hidden":
                            continue

                        apps.append(
                            {
                                "bundle_id": bundle_id,
                                "name": app_info.get(
                                    "CFBundleDisplayName", app_info.get("CFBundleName", bundle_id)
                                ),
                                "path": app_info.get("Path", ""),
                                "version": app_info.get("CFBundleVersion", "Unknown"),
                                "type": app_info.get("ApplicationType", "User"),
                            }
                        )
                except json.JSONDecodeError:
                    pass

            return apps
        except subprocess.CalledProcessError:
            return []

    def get_app_state(self, bundle_id: str) -> str:
        """
        Get app state (running, suspended, etc.).

        Args:
            bundle_id: App bundle identifier

        Returns:
            State string or 'unknown'
        """
        # Check if app is running by trying to get its PID
        cmd = build_simctl_command("spawn", self.udid, "launchctl", "list")

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            if bundle_id in result.stdout:
                return "running"
            return "not running"
        except subprocess.CalledProcessError:
            return "unknown"

    def restart_app(self, bundle_id: str, delay: float = 1.0) -> bool:
        """
        Restart an app (terminate then launch).

        Args:
            bundle_id: App bundle identifier
            delay: Delay between terminate and launch

        Returns:
            Success status
        """
        # Terminate
        self.terminate(bundle_id)
        time.sleep(delay)

        # Launch
        success, _ = self.launch(bundle_id)
        return success


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Control iOS app lifecycle")

    # Actions
    parser.add_argument("--launch", help="Launch app by bundle ID")
    parser.add_argument("--terminate", help="Terminate app by bundle ID")
    parser.add_argument("--restart", help="Restart app by bundle ID")
    parser.add_argument("--install", help="Install app from .app path")
    parser.add_argument("--uninstall", help="Uninstall app by bundle ID")
    parser.add_argument("--open-url", help="Open URL (deep link)")
    parser.add_argument("--list", action="store_true", help="List installed apps")
    parser.add_argument("--state", help="Get app state by bundle ID")

    # Options
    parser.add_argument(
        "--wait-for-debugger", action="store_true", help="Wait for debugger when launching"
    )
    parser.add_argument(
        "--udid",
        help="Device UDID (auto-detects booted simulator if not provided)",
    )

    args = parser.parse_args()

    # Resolve UDID with auto-detection
    try:
        udid = resolve_udid(args.udid)
    except RuntimeError as e:
        print(f"Error: {e}")
        sys.exit(1)

    launcher = AppLauncher(udid=udid)

    # Execute requested action
    if args.launch:
        success, pid = launcher.launch(args.launch, args.wait_for_debugger)
        if success:
            if pid:
                print(f"Launched {args.launch} (PID: {pid})")
            else:
                print(f"Launched {args.launch}")
        else:
            print(f"Failed to launch {args.launch}")
            sys.exit(1)

    elif args.terminate:
        if launcher.terminate(args.terminate):
            print(f"Terminated {args.terminate}")
        else:
            print(f"Failed to terminate {args.terminate}")
            sys.exit(1)

    elif args.restart:
        if launcher.restart_app(args.restart):
            print(f"Restarted {args.restart}")
        else:
            print(f"Failed to restart {args.restart}")
            sys.exit(1)

    elif args.install:
        if launcher.install(args.install):
            print(f"Installed {args.install}")
        else:
            print(f"Failed to install {args.install}")
            sys.exit(1)

    elif args.uninstall:
        if launcher.uninstall(args.uninstall):
            print(f"Uninstalled {args.uninstall}")
        else:
            print(f"Failed to uninstall {args.uninstall}")
            sys.exit(1)

    elif args.open_url:
        if launcher.open_url(args.open_url):
            print(f"Opened URL: {args.open_url}")
        else:
            print(f"Failed to open URL: {args.open_url}")
            sys.exit(1)

    elif args.list:
        apps = launcher.list_apps()
        if apps:
            print(f"Installed apps ({len(apps)}):")
            for app in apps[:10]:  # Limit for token efficiency
                print(f"  {app['bundle_id']}: {app['name']} (v{app['version']})")
            if len(apps) > 10:
                print(f"  ... and {len(apps) - 10} more")
        else:
            print("No apps found or failed to list")

    elif args.state:
        state = launcher.get_app_state(args.state)
        print(f"{args.state}: {state}")

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
```

## File: `ios-simulator-skill/scripts/app_state_capture.py`
```python
#!/usr/bin/env python3
"""
App State Capture for iOS Simulator

Captures complete app state including screenshot, accessibility tree, and logs.
Optimized for minimal token output.

Usage: python scripts/app_state_capture.py [options]
"""

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from common import (
    capture_screenshot,
    count_elements,
    get_accessibility_tree,
    resolve_udid,
)


class AppStateCapture:
    """Captures comprehensive app state for debugging."""

    def __init__(
        self,
        app_bundle_id: str | None = None,
        udid: str | None = None,
        inline: bool = False,
        screenshot_size: str = "half",
    ):
        """
        Initialize state capture.

        Args:
            app_bundle_id: Optional app bundle ID for log filtering
            udid: Optional device UDID (uses booted if not specified)
            inline: If True, return screenshots as base64 (for vision-based automation)
            screenshot_size: 'full', 'half', 'quarter', 'thumb' (default: 'half')
        """
        self.app_bundle_id = app_bundle_id
        self.udid = udid
        self.inline = inline
        self.screenshot_size = screenshot_size

    def capture_screenshot(self, output_path: Path) -> bool:
        """Capture screenshot of current screen."""
        cmd = ["xcrun", "simctl", "io"]

        if self.udid:
            cmd.append(self.udid)
        else:
            cmd.append("booted")

        cmd.extend(["screenshot", str(output_path)])

        try:
            subprocess.run(cmd, capture_output=True, check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def capture_accessibility_tree(self, output_path: Path) -> dict:
        """Capture accessibility tree using shared utility."""
        try:
            # Use shared utility to fetch tree
            tree = get_accessibility_tree(self.udid, nested=True)

            # Save tree
            with open(output_path, "w") as f:
                json.dump(tree, f, indent=2)

            # Return summary using shared utility
            return {"captured": True, "element_count": count_elements(tree)}
        except Exception as e:
            return {"captured": False, "error": str(e)}

    def capture_logs(self, output_path: Path, line_limit: int = 100) -> dict:
        """Capture recent app logs."""
        if not self.app_bundle_id:
            # Can't capture logs without app ID
            return {"captured": False, "reason": "No app bundle ID specified"}

        # Get app name from bundle ID (simplified)
        app_name = self.app_bundle_id.split(".")[-1]

        cmd = ["xcrun", "simctl", "spawn"]

        if self.udid:
            cmd.append(self.udid)
        else:
            cmd.append("booted")

        cmd.extend(
            [
                "log",
                "show",
                "--predicate",
                f'process == "{app_name}"',
                "--last",
                "1m",  # Last 1 minute
                "--style",
                "compact",
            ]
        )

        try:
            result = subprocess.run(cmd, check=False, capture_output=True, text=True, timeout=5)
            logs = result.stdout

            # Limit lines for token efficiency
            lines = logs.split("\n")
            if len(lines) > line_limit:
                lines = lines[-line_limit:]

            # Save logs
            with open(output_path, "w") as f:
                f.write("\n".join(lines))

            # Analyze for issues
            warning_count = sum(1 for line in lines if "warning" in line.lower())
            error_count = sum(1 for line in lines if "error" in line.lower())

            return {
                "captured": True,
                "lines": len(lines),
                "warnings": warning_count,
                "errors": error_count,
            }
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
            return {"captured": False, "error": str(e)}

    def capture_device_info(self) -> dict:
        """Get device information."""
        cmd = ["xcrun", "simctl", "list", "devices", "booted"]

        if self.udid:
            # Specific device info
            cmd = ["xcrun", "simctl", "list", "devices"]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)

            # Parse output for device info (simplified)
            lines = result.stdout.split("\n")
            device_info = {}

            for line in lines:
                if "iPhone" in line or "iPad" in line:
                    # Extract device name and state
                    parts = line.strip().split("(")
                    if parts:
                        device_info["name"] = parts[0].strip()
                        if len(parts) > 2:
                            device_info["udid"] = parts[1].replace(")", "").strip()
                            device_info["state"] = parts[2].replace(")", "").strip()
                    break

            return device_info
        except subprocess.CalledProcessError:
            return {}

    def capture_all(
        self, output_dir: str, log_lines: int = 100, app_name: str | None = None
    ) -> dict:
        """
        Capture complete app state.

        Args:
            output_dir: Directory to save artifacts
            log_lines: Number of log lines to capture
            app_name: App name for semantic naming (for inline mode)

        Returns:
            Summary of captured state
        """
        # Create output directory (only if not in inline mode)
        output_path = Path(output_dir)
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        if not self.inline:
            capture_dir = output_path / f"app-state-{timestamp}"
            capture_dir.mkdir(parents=True, exist_ok=True)
        else:
            capture_dir = None

        summary = {
            "timestamp": datetime.now().isoformat(),
            "screenshot_mode": "inline" if self.inline else "file",
        }

        if capture_dir:
            summary["output_dir"] = str(capture_dir)

        # Capture screenshot using new unified utility
        screenshot_result = capture_screenshot(
            self.udid,
            size=self.screenshot_size,
            inline=self.inline,
            app_name=app_name,
        )

        if self.inline:
            # Inline mode: store base64
            summary["screenshot"] = {
                "mode": "inline",
                "base64": screenshot_result["base64_data"],
                "width": screenshot_result["width"],
                "height": screenshot_result["height"],
                "size_preset": self.screenshot_size,
            }
        else:
            # File mode: save to disk
            screenshot_path = capture_dir / "screenshot.png"
            # Move temp file to target location
            import shutil

            shutil.move(screenshot_result["file_path"], screenshot_path)
            summary["screenshot"] = {
                "mode": "file",
                "file": "screenshot.png",
                "size_bytes": screenshot_result["size_bytes"],
            }

        # Capture accessibility tree
        if not self.inline or capture_dir:
            accessibility_path = (capture_dir or output_path) / "accessibility-tree.json"
        else:
            accessibility_path = None

        if accessibility_path:
            tree_info = self.capture_accessibility_tree(accessibility_path)
            summary["accessibility"] = tree_info

        # Capture logs (if app ID provided)
        if self.app_bundle_id:
            if not self.inline or capture_dir:
                logs_path = (capture_dir or output_path) / "app-logs.txt"
            else:
                logs_path = None

            if logs_path:
                log_info = self.capture_logs(logs_path, log_lines)
                summary["logs"] = log_info

        # Get device info
        device_info = self.capture_device_info()
        if device_info:
            summary["device"] = device_info
            # Save device info (file mode only)
            if capture_dir:
                with open(capture_dir / "device-info.json", "w") as f:
                    json.dump(device_info, f, indent=2)

        # Save summary (file mode only)
        if capture_dir:
            with open(capture_dir / "summary.json", "w") as f:
                json.dump(summary, f, indent=2)

            # Create markdown summary
            self._create_summary_md(capture_dir, summary)

        return summary

    def _create_summary_md(self, capture_dir: Path, summary: dict) -> None:
        """Create markdown summary file."""
        md_path = capture_dir / "summary.md"

        with open(md_path, "w") as f:
            f.write("# App State Capture\n\n")
            f.write(f"**Timestamp:** {summary['timestamp']}\n\n")

            if "device" in summary:
                f.write("## Device\n")
                device = summary["device"]
                f.write(f"- Name: {device.get('name', 'Unknown')}\n")
                f.write(f"- UDID: {device.get('udid', 'N/A')}\n")
                f.write(f"- State: {device.get('state', 'Unknown')}\n\n")

            f.write("## Screenshot\n")
            f.write("![Current Screen](screenshot.png)\n\n")

            if "accessibility" in summary:
                acc = summary["accessibility"]
                f.write("## Accessibility\n")
                if acc.get("captured"):
                    f.write(f"- Elements: {acc.get('element_count', 0)}\n")
                else:
                    f.write(f"- Error: {acc.get('error', 'Unknown')}\n")
                f.write("\n")

            if "logs" in summary:
                logs = summary["logs"]
                f.write("## Logs\n")
                if logs.get("captured"):
                    f.write(f"- Lines: {logs.get('lines', 0)}\n")
                    f.write(f"- Warnings: {logs.get('warnings', 0)}\n")
                    f.write(f"- Errors: {logs.get('errors', 0)}\n")
                else:
                    f.write(f"- {logs.get('reason', logs.get('error', 'Not captured'))}\n")
                f.write("\n")

            f.write("## Files\n")
            f.write("- `screenshot.png` - Current screen\n")
            f.write("- `accessibility-tree.json` - Full UI hierarchy\n")
            if self.app_bundle_id:
                f.write("- `app-logs.txt` - Recent app logs\n")
            f.write("- `device-info.json` - Device details\n")
            f.write("- `summary.json` - Complete capture metadata\n")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Capture complete app state for debugging")
    parser.add_argument(
        "--app-bundle-id", help="App bundle ID for log filtering (e.g., com.example.app)"
    )
    parser.add_argument(
        "--output", default=".", help="Output directory (default: current directory)"
    )
    parser.add_argument(
        "--log-lines", type=int, default=100, help="Number of log lines to capture (default: 100)"
    )
    parser.add_argument(
        "--udid",
        help="Device UDID (auto-detects booted simulator if not provided)",
    )
    parser.add_argument(
        "--inline",
        action="store_true",
        help="Return screenshots as base64 (inline mode for vision-based automation)",
    )
    parser.add_argument(
        "--size",
        choices=["full", "half", "quarter", "thumb"],
        default="half",
        help="Screenshot size for token optimization (default: half)",
    )
    parser.add_argument("--app-name", help="App name for semantic screenshot naming")

    args = parser.parse_args()

    # Resolve UDID with auto-detection
    try:
        udid = resolve_udid(args.udid)
    except RuntimeError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Create capturer
    capturer = AppStateCapture(
        app_bundle_id=args.app_bundle_id,
        udid=udid,
        inline=args.inline,
        screenshot_size=args.size,
    )

    # Capture state
    try:
        summary = capturer.capture_all(
            output_dir=args.output, log_lines=args.log_lines, app_name=args.app_name
        )

        # Token-efficient output
        if "output_dir" in summary:
            print(f"State captured: {summary['output_dir']}/")
        else:
            # Inline mode
            print(
                f"State captured (inline mode): {summary['screenshot']['width']}x{summary['screenshot']['height']}"
            )

        # Report any issues found
        if "logs" in summary and summary["logs"].get("captured"):
            logs = summary["logs"]
            if logs["errors"] > 0 or logs["warnings"] > 0:
                print(f"Issues found: {logs['errors']} errors, {logs['warnings']} warnings")

        if "accessibility" in summary and summary["accessibility"].get("captured"):
            print(f"Elements: {summary['accessibility']['element_count']}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```

## File: `ios-simulator-skill/scripts/build_and_test.py`
```python
#!/usr/bin/env python3
"""
Build and Test Automation for Xcode Projects

Ultra token-efficient build automation with progressive disclosure via xcresult bundles.

Features:
- Minimal default output (5-10 tokens)
- Progressive disclosure for error/warning/log details
- Native xcresult bundle support
- Clean modular architecture

Usage Examples:
    # Build (minimal output)
    python scripts/build_and_test.py --project MyApp.xcodeproj
    # Output: Build: SUCCESS (0 errors, 3 warnings) [xcresult-20251018-143052]

    # Get error details
    python scripts/build_and_test.py --get-errors xcresult-20251018-143052

    # Get warnings
    python scripts/build_and_test.py --get-warnings xcresult-20251018-143052

    # Get build log
    python scripts/build_and_test.py --get-log xcresult-20251018-143052

    # Get everything as JSON
    python scripts/build_and_test.py --get-all xcresult-20251018-143052 --json

    # List recent builds
    python scripts/build_and_test.py --list-xcresults

    # Verbose mode (for debugging)
    python scripts/build_and_test.py --project MyApp.xcodeproj --verbose
"""

import argparse
import sys
from pathlib import Path

# Import our modular components
from xcode import BuildRunner, OutputFormatter, XCResultCache, XCResultParser


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Build and test Xcode projects with progressive disclosure",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Build project (minimal output)
  python scripts/build_and_test.py --project MyApp.xcodeproj

  # Run tests
  python scripts/build_and_test.py --project MyApp.xcodeproj --test

  # Get error details from previous build
  python scripts/build_and_test.py --get-errors xcresult-20251018-143052

  # Get all details as JSON
  python scripts/build_and_test.py --get-all xcresult-20251018-143052 --json

  # List recent builds
  python scripts/build_and_test.py --list-xcresults
        """,
    )

    # Build/test mode arguments
    build_group = parser.add_argument_group("Build/Test Options")
    project_group = build_group.add_mutually_exclusive_group()
    project_group.add_argument("--project", help="Path to .xcodeproj file")
    project_group.add_argument("--workspace", help="Path to .xcworkspace file")

    build_group.add_argument("--scheme", help="Build scheme (auto-detected if not specified)")
    build_group.add_argument(
        "--configuration",
        default="Debug",
        help="Build configuration (default: Debug). Accepts any valid Xcode configuration.",
    )
    build_group.add_argument("--simulator", help="Simulator name (default: iPhone 15)")
    build_group.add_argument("--clean", action="store_true", help="Clean before building")
    build_group.add_argument("--test", action="store_true", help="Run tests")
    build_group.add_argument("--suite", help="Specific test suite to run")

    # Progressive disclosure arguments
    disclosure_group = parser.add_argument_group("Progressive Disclosure Options")
    disclosure_group.add_argument(
        "--get-errors", metavar="XCRESULT_ID", help="Get error details from xcresult"
    )
    disclosure_group.add_argument(
        "--get-warnings", metavar="XCRESULT_ID", help="Get warning details from xcresult"
    )
    disclosure_group.add_argument(
        "--get-log", metavar="XCRESULT_ID", help="Get build log from xcresult"
    )
    disclosure_group.add_argument(
        "--get-all", metavar="XCRESULT_ID", help="Get all details from xcresult"
    )
    disclosure_group.add_argument(
        "--list-xcresults", action="store_true", help="List recent xcresult bundles"
    )

    # Output options
    output_group = parser.add_argument_group("Output Options")
    output_group.add_argument("--verbose", action="store_true", help="Show detailed output")
    output_group.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    # Initialize cache
    cache = XCResultCache()

    # Handle list mode
    if args.list_xcresults:
        xcresults = cache.list()
        if args.json:
            import json

            print(json.dumps(xcresults, indent=2))
        elif not xcresults:
            print("No xcresult bundles found")
        else:
            print(f"Recent XCResult bundles ({len(xcresults)}):")
            print()
            for xc in xcresults:
                print(f"  {xc['id']}")
                print(f"    Created: {xc['created']}")
                print(f"    Size: {xc['size_mb']} MB")
                print()
        return 0

    # Handle retrieval modes
    xcresult_id = args.get_errors or args.get_warnings or args.get_log or args.get_all

    if xcresult_id:
        xcresult_path = cache.get_path(xcresult_id)

        if not xcresult_path or not xcresult_path.exists():
            print(f"Error: XCResult bundle not found: {xcresult_id}", file=sys.stderr)
            print("Use --list-xcresults to see available bundles", file=sys.stderr)
            return 1

        # Load cached stderr for progressive disclosure
        cached_stderr = cache.get_stderr(xcresult_id)
        parser = XCResultParser(xcresult_path, stderr=cached_stderr)

        # Get errors
        if args.get_errors:
            errors = parser.get_errors()
            if args.json:
                import json

                print(json.dumps(errors, indent=2))
            else:
                print(OutputFormatter.format_errors(errors))
            return 0

        # Get warnings
        if args.get_warnings:
            warnings = parser.get_warnings()
            if args.json:
                import json

                print(json.dumps(warnings, indent=2))
            else:
                print(OutputFormatter.format_warnings(warnings))
            return 0

        # Get log
        if args.get_log:
            log = parser.get_build_log()
            if log:
                print(OutputFormatter.format_log(log))
            else:
                print("No build log available", file=sys.stderr)
                return 1
            return 0

        # Get all
        if args.get_all:
            error_count, warning_count = parser.count_issues()
            errors = parser.get_errors()
            warnings = parser.get_warnings()
            build_log = parser.get_build_log()

            if args.json:
                import json

                data = {
                    "xcresult_id": xcresult_id,
                    "error_count": error_count,
                    "warning_count": warning_count,
                    "errors": errors,
                    "warnings": warnings,
                    "log_preview": build_log[:1000] if build_log else None,
                }
                print(json.dumps(data, indent=2))
            else:
                print(f"XCResult: {xcresult_id}")
                print(f"Errors: {error_count}, Warnings: {warning_count}")
                print()
                if errors:
                    print(OutputFormatter.format_errors(errors, limit=10))
                    print()
                if warnings:
                    print(OutputFormatter.format_warnings(warnings, limit=10))
                    print()
                if build_log:
                    print("Build Log (last 30 lines):")
                    print(OutputFormatter.format_log(build_log, lines=30))
            return 0

    # Build/test mode
    if not args.project and not args.workspace:
        # Try to auto-detect in current directory
        cwd = Path.cwd()
        projects = list(cwd.glob("*.xcodeproj"))
        workspaces = list(cwd.glob("*.xcworkspace"))

        if workspaces:
            args.workspace = str(workspaces[0])
        elif projects:
            args.project = str(projects[0])
        else:
            parser.error("No project or workspace specified and none found in current directory")

    # Initialize builder
    builder = BuildRunner(
        project_path=args.project,
        workspace_path=args.workspace,
        scheme=args.scheme,
        configuration=args.configuration,
        simulator=args.simulator,
        cache=cache,
    )

    # Execute build or test
    if args.test:
        success, xcresult_id, stderr = builder.test(test_suite=args.suite)
    else:
        success, xcresult_id, stderr = builder.build(clean=args.clean)

    if not xcresult_id and not stderr:
        print("Error: Build/test failed without creating xcresult or error output", file=sys.stderr)
        return 1

    # Save stderr to cache for progressive disclosure
    if xcresult_id and stderr:
        cache.save_stderr(xcresult_id, stderr)

    # Parse results
    xcresult_path = cache.get_path(xcresult_id) if xcresult_id else None
    parser = XCResultParser(xcresult_path, stderr=stderr)
    error_count, warning_count = parser.count_issues()

    # Format output
    status = "SUCCESS" if success else "FAILED"

    # Collect errors on failure (used by all output modes)
    errors = parser.get_errors() if not success else None
    hints = OutputFormatter.generate_hints(errors) if errors else None

    # Collect test info and failed tests when testing
    test_info = None
    failed_tests = None
    if args.test and xcresult_path:
        test_results = parser.get_test_results()
        if test_results:
            test_info = {
                "total": test_results.get("total", 0),
                "passed": test_results.get("passed", 0),
                "failed": test_results.get("failed", 0),
                "duration": test_results.get("duration", 0.0),
            }
        if not success:
            failed_tests = parser.get_failed_tests()

    if args.verbose:
        # Verbose mode with error/warning details
        verbose_errors = errors if error_count > 0 else None
        warnings = parser.get_warnings() if warning_count > 0 else None

        output = OutputFormatter.format_verbose(
            status=status,
            error_count=error_count,
            warning_count=warning_count,
            xcresult_id=xcresult_id or "N/A",
            errors=verbose_errors,
            warnings=warnings,
            test_info=test_info,
        )
        print(output)
    elif args.json:
        # JSON mode
        data = {
            "success": success,
            "xcresult_id": xcresult_id or None,
            "error_count": error_count,
            "warning_count": warning_count,
        }
        if test_info:
            data["test_info"] = test_info
        if not success:
            if errors:
                data["errors"] = errors[:10]
            if failed_tests:
                data["failed_tests"] = failed_tests[:10]
        if hints:
            data["hints"] = hints
        import json

        print(json.dumps(data, indent=2))
    else:
        # Minimal mode (default)
        output = OutputFormatter.format_minimal(
            status=status,
            error_count=error_count,
            warning_count=warning_count,
            xcresult_id=xcresult_id or "N/A",
            test_info=test_info,
            hints=hints,
            errors=errors,
            failed_tests=failed_tests,
        )
        print(output)

    # Exit with appropriate code
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
```

## File: `ios-simulator-skill/scripts/clipboard.py`
```python
#!/usr/bin/env python3
"""
iOS Simulator Clipboard Manager

Copy text to simulator clipboard for testing paste flows.
Optimized for minimal token output.

Usage: python scripts/clipboard.py --copy "text to copy"
"""

import argparse
import subprocess
import sys

from common import resolve_udid


class ClipboardManager:
    """Manages clipboard operations on iOS simulator."""

    def __init__(self, udid: str | None = None):
        """Initialize clipboard manager.

        Args:
            udid: Optional device UDID (auto-detects booted simulator if None)
        """
        self.udid = udid

    def copy(self, text: str) -> bool:
        """
        Copy text to simulator clipboard.

        Args:
            text: Text to copy to clipboard

        Returns:
            Success status
        """
        cmd = ["xcrun", "simctl", "pbcopy"]

        if self.udid:
            cmd.append(self.udid)
        else:
            cmd.append("booted")

        cmd.append(text)

        try:
            subprocess.run(cmd, capture_output=True, check=True)
            return True
        except subprocess.CalledProcessError:
            return False


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Copy text to iOS simulator clipboard")
    parser.add_argument("--copy", required=True, help="Text to copy to clipboard")
    parser.add_argument(
        "--udid",
        help="Device UDID (auto-detects booted simulator if not provided)",
    )
    parser.add_argument("--test-name", help="Test scenario name for tracking")
    parser.add_argument("--expected", help="Expected behavior after paste")

    args = parser.parse_args()

    # Resolve UDID with auto-detection
    try:
        udid = resolve_udid(args.udid)
    except RuntimeError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Create manager and copy text
    manager = ClipboardManager(udid=udid)

    if manager.copy(args.copy):
        # Token-efficient output
        output = f'Copied: "{args.copy}"'

        if args.test_name:
            output += f" (test: {args.test_name})"

        print(output)

        # Provide usage guidance
        if args.expected:
            print(f"Expected: {args.expected}")

        print()
        print("Next steps:")
        print("1. Tap text field with: python scripts/navigator.py --find-type TextField --tap")
        print("2. Paste with: python scripts/keyboard.py --key return")
        print("   Or use Cmd+V gesture with: python scripts/keyboard.py --key cmd+v")

    else:
        print("Failed to copy text to clipboard")
        sys.exit(1)


if __name__ == "__main__":
    main()
```

## File: `ios-simulator-skill/scripts/gesture.py`
```python
#!/usr/bin/env python3
"""
iOS Gesture Controller - Swipes and Complex Gestures

Performs navigation gestures like swipes, scrolls, and pinches.
Token-efficient output for common navigation patterns.

This script handles touch gestures for iOS simulator automation. It provides
directional swipes, multi-swipe scrolling, pull-to-refresh, and pinch gestures.
Automatically detects screen size from the device for accurate gesture positioning.

Key Features:
- Directional swipes (up, down, left, right)
- Multi-swipe scrolling with customizable amount
- Pull-to-refresh gesture
- Pinch to zoom (in/out)
- Custom swipe between any two points
- Drag and drop simulation
- Auto-detects screen dimensions from device

Usage Examples:
    # Simple directional swipe
    python scripts/gesture.py --swipe up --udid <device-id>

    # Scroll down multiple times
    python scripts/gesture.py --scroll down --scroll-amount 3 --udid <device-id>

    # Pull to refresh
    python scripts/gesture.py --refresh --udid <device-id>

    # Custom swipe coordinates
    python scripts/gesture.py --swipe-from 100,500 --swipe-to 100,100 --udid <device-id>

    # Pinch to zoom
    python scripts/gesture.py --pinch out --udid <device-id>

    # Long press at coordinates
    python scripts/gesture.py --long-press 200,300 --duration 2.0 --udid <device-id>

Output Format:
    Swiped up
    Scrolled down (3x)
    Performed pull to refresh

Gesture Details:
- Swipes use 70% of screen by default (configurable)
- Scrolls are multiple small 30% swipes with delays
- Start points are offset from edges for reliability
- Screen size auto-detected from accessibility tree root element
- Falls back to iPhone 14 dimensions (390x844) if detection fails

Technical Details:
- Uses `idb ui swipe x1 y1 x2 y2` for gesture execution
- Duration parameter converts to milliseconds for IDB
- Automatically fetches screen size on initialization
- Parses IDB accessibility tree to get root frame dimensions
- All coordinates calculated as fractions of screen size for device independence
"""

import argparse
import subprocess
import sys
import time

from common import (
    get_device_screen_size,
    get_screen_size,
    resolve_udid,
    transform_screenshot_coords,
)


class GestureController:
    """Performs gestures on iOS simulator."""

    # Standard screen dimensions (will be detected if possible)
    DEFAULT_WIDTH = 390  # iPhone 14
    DEFAULT_HEIGHT = 844

    def __init__(self, udid: str | None = None):
        """Initialize gesture controller."""
        self.udid = udid
        self.screen_size = self._get_screen_size()

    def _get_screen_size(self) -> tuple[int, int]:
        """Try to detect screen size from device using shared utility."""
        return get_screen_size(self.udid)

    def swipe(self, direction: str, distance_ratio: float = 0.7) -> bool:
        """
        Perform directional swipe.

        Args:
            direction: up, down, left, right
            distance_ratio: How far to swipe (0.0-1.0 of screen)

        Returns:
            Success status
        """
        width, height = self.screen_size
        center_x = width // 2
        center_y = height // 2

        # Calculate swipe coordinates based on direction
        if direction == "up":
            start = (center_x, int(height * 0.7))
            end = (center_x, int(height * (1 - distance_ratio + 0.3)))
        elif direction == "down":
            start = (center_x, int(height * 0.3))
            end = (center_x, int(height * (distance_ratio - 0.3 + 0.3)))
        elif direction == "left":
            start = (int(width * 0.8), center_y)
            end = (int(width * (1 - distance_ratio + 0.2)), center_y)
        elif direction == "right":
            start = (int(width * 0.2), center_y)
            end = (int(width * (distance_ratio - 0.2 + 0.2)), center_y)
        else:
            return False

        return self.swipe_between(start, end)

    def swipe_between(
        self, start: tuple[int, int], end: tuple[int, int], duration: float = 0.3
    ) -> bool:
        """
        Swipe between two points.

        Args:
            start: Starting coordinates (x, y)
            end: Ending coordinates (x, y)
            duration: Swipe duration in seconds

        Returns:
            Success status
        """
        cmd = ["idb", "ui", "swipe"]
        cmd.extend([str(start[0]), str(start[1]), str(end[0]), str(end[1])])

        # IDB doesn't support duration directly, but we can add delay
        if duration != 0.3:
            cmd.extend(["--duration", str(int(duration * 1000))])

        if self.udid:
            cmd.extend(["--udid", self.udid])

        try:
            subprocess.run(cmd, capture_output=True, check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def scroll(self, direction: str, amount: int = 3) -> bool:
        """
        Perform multiple small swipes to scroll.

        Args:
            direction: up, down
            amount: Number of small swipes

        Returns:
            Success status
        """
        for _ in range(amount):
            if not self.swipe(direction, distance_ratio=0.3):
                return False
            time.sleep(0.2)  # Small delay between swipes
        return True

    def tap_and_hold(self, x: int, y: int, duration: float = 2.0) -> bool:
        """
        Long press at coordinates.

        Args:
            x, y: Coordinates
            duration: Hold duration in seconds

        Returns:
            Success status
        """
        # IDB doesn't have native long press, simulate with tap
        # In real implementation, might need to use different approach
        cmd = ["idb", "ui", "tap", str(x), str(y)]

        if self.udid:
            cmd.extend(["--udid", self.udid])

        try:
            subprocess.run(cmd, capture_output=True, check=True)
            # Simulate hold with delay
            time.sleep(duration)
            return True
        except subprocess.CalledProcessError:
            return False

    def pinch(self, direction: str = "out", center: tuple[int, int] | None = None) -> bool:
        """
        Perform pinch gesture (zoom in/out).

        Args:
            direction: 'in' (zoom out) or 'out' (zoom in)
            center: Center point for pinch

        Returns:
            Success status
        """
        if not center:
            width, height = self.screen_size
            center = (width // 2, height // 2)

        # Calculate pinch points
        offset = 100 if direction == "out" else 50

        if direction == "out":
            # Zoom in - fingers move apart
            start1 = (center[0] - 20, center[1] - 20)
            end1 = (center[0] - offset, center[1] - offset)
            start2 = (center[0] + 20, center[1] + 20)
            end2 = (center[0] + offset, center[1] + offset)
        else:
            # Zoom out - fingers move together
            start1 = (center[0] - offset, center[1] - offset)
            end1 = (center[0] - 20, center[1] - 20)
            start2 = (center[0] + offset, center[1] + offset)
            end2 = (center[0] + 20, center[1] + 20)

        # Perform two swipes simultaneously (simulated)
        success1 = self.swipe_between(start1, end1)
        success2 = self.swipe_between(start2, end2)

        return success1 and success2

    def drag_and_drop(self, start: tuple[int, int], end: tuple[int, int]) -> bool:
        """
        Drag element from one position to another.

        Args:
            start: Starting coordinates
            end: Ending coordinates

        Returns:
            Success status
        """
        # Use slow swipe to simulate drag
        return self.swipe_between(start, end, duration=1.0)

    def refresh(self) -> bool:
        """Pull to refresh gesture."""
        width, _ = self.screen_size
        start = (width // 2, 100)
        end = (width // 2, 400)
        return self.swipe_between(start, end)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Perform gestures on iOS simulator")

    # Gesture options
    parser.add_argument(
        "--swipe", choices=["up", "down", "left", "right"], help="Perform directional swipe"
    )
    parser.add_argument("--swipe-from", help="Custom swipe start coordinates (x,y)")
    parser.add_argument("--swipe-to", help="Custom swipe end coordinates (x,y)")
    parser.add_argument(
        "--scroll", choices=["up", "down"], help="Scroll in direction (multiple small swipes)"
    )
    parser.add_argument(
        "--scroll-amount", type=int, default=3, help="Number of scroll swipes (default: 3)"
    )
    parser.add_argument("--long-press", help="Long press at coordinates (x,y)")
    parser.add_argument(
        "--duration", type=float, default=2.0, help="Duration for long press in seconds"
    )
    parser.add_argument(
        "--pinch", choices=["in", "out"], help="Pinch gesture (in=zoom out, out=zoom in)"
    )
    parser.add_argument("--refresh", action="store_true", help="Pull to refresh gesture")

    # Coordinate transformation
    parser.add_argument(
        "--screenshot-coords",
        action="store_true",
        help="Interpret swipe coordinates as from a screenshot (requires --screenshot-width/height)",
    )
    parser.add_argument(
        "--screenshot-width",
        type=int,
        help="Screenshot width for coordinate transformation",
    )
    parser.add_argument(
        "--screenshot-height",
        type=int,
        help="Screenshot height for coordinate transformation",
    )

    parser.add_argument(
        "--udid",
        help="Device UDID (auto-detects booted simulator if not provided)",
    )

    args = parser.parse_args()

    # Resolve UDID with auto-detection
    try:
        udid = resolve_udid(args.udid)
    except RuntimeError as e:
        print(f"Error: {e}")
        sys.exit(1)

    controller = GestureController(udid=udid)

    # Execute requested gesture
    if args.swipe:
        if controller.swipe(args.swipe):
            print(f"Swiped {args.swipe}")
        else:
            print(f"Failed to swipe {args.swipe}")
            sys.exit(1)

    elif args.swipe_from and args.swipe_to:
        # Custom swipe
        start = tuple(map(int, args.swipe_from.split(",")))
        end = tuple(map(int, args.swipe_to.split(",")))

        # Handle coordinate transformation if requested
        if args.screenshot_coords:
            if not args.screenshot_width or not args.screenshot_height:
                print(
                    "Error: --screenshot-coords requires --screenshot-width and --screenshot-height"
                )
                sys.exit(1)

            device_w, device_h = get_device_screen_size(udid)
            start = transform_screenshot_coords(
                start[0],
                start[1],
                args.screenshot_width,
                args.screenshot_height,
                device_w,
                device_h,
            )
            end = transform_screenshot_coords(
                end[0],
                end[1],
                args.screenshot_width,
                args.screenshot_height,
                device_w,
                device_h,
            )
            print("Transformed screenshot coords to device coords")

        if controller.swipe_between(start, end):
            print(f"Swiped from {start} to {end}")
        else:
            print("Failed to swipe")
            sys.exit(1)

    elif args.scroll:
        if controller.scroll(args.scroll, args.scroll_amount):
            print(f"Scrolled {args.scroll} ({args.scroll_amount}x)")
        else:
            print(f"Failed to scroll {args.scroll}")
            sys.exit(1)

    elif args.long_press:
        coords = tuple(map(int, args.long_press.split(",")))
        if controller.tap_and_hold(coords[0], coords[1], args.duration):
            print(f"Long pressed at {coords} for {args.duration}s")
        else:
            print("Failed to long press")
            sys.exit(1)

    elif args.pinch:
        if controller.pinch(args.pinch):
            action = "Zoomed in" if args.pinch == "out" else "Zoomed out"
            print(action)
        else:
            print(f"Failed to pinch {args.pinch}")
            sys.exit(1)

    elif args.refresh:
        if controller.refresh():
            print("Performed pull to refresh")
        else:
            print("Failed to refresh")
            sys.exit(1)

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
```

## File: `ios-simulator-skill/scripts/keyboard.py`
```python
#!/usr/bin/env python3
"""
iOS Keyboard Controller - Text Entry and Hardware Buttons

Handles keyboard input, special keys, and hardware button simulation.
Token-efficient text entry and navigation control.

This script provides text input and hardware button control for iOS simulator
automation. It handles both typing text strings and pressing special keys like
return, delete, tab, etc. Also controls hardware buttons like home and lock.

Key Features:
- Type text strings into focused elements
- Press special keys (return, delete, tab, space, arrows)
- Hardware button simulation (home, lock, volume, screenshot)
- Character-by-character typing with delays (for animations)
- Multiple key press support
- iOS HID key code mapping for reliability

Usage Examples:
    # Type text into focused field
    python scripts/keyboard.py --type "hello@example.com" --udid <device-id>

    # Press return key to submit
    python scripts/keyboard.py --key return --udid <device-id>

    # Press delete 3 times
    python scripts/keyboard.py --key delete --key delete --key delete --udid <device-id>

    # Press home button
    python scripts/keyboard.py --button home --udid <device-id>

    # Press lock button
    python scripts/keyboard.py --button lock --udid <device-id>

    # Type with delay between characters (for animations)
    python scripts/keyboard.py --type "slow typing" --delay 0.1 --udid <device-id>

Output Format:
    Typed: "hello@example.com"
    Pressed return
    Pressed home button

Special Keys Supported:
- return/enter: Submit forms, new lines (HID code 40)
- delete/backspace: Remove characters (HID code 42)
- tab: Navigate between fields (HID code 43)
- space: Space character (HID code 44)
- escape: Cancel/dismiss (HID code 41)
- up/down/left/right: Arrow keys (HID codes 82/81/80/79)

Hardware Buttons Supported:
- home: Return to home screen
- lock/power: Lock device
- volume-up/volume-down: Volume control
- ringer: Toggle mute
- screenshot: Capture screen

Technical Details:
- Uses `idb ui text` for typing text strings
- Uses `idb ui key <code>` for special keys with iOS HID codes
- HID codes from Apple's UIKeyboardHIDUsage specification
- Hardware buttons use `xcrun simctl` button actions
- Text entry works on currently focused element
- Special keys are integers (40=Return, 42=Delete, etc.)
"""

import argparse
import subprocess
import sys
import time

from common import resolve_udid


class KeyboardController:
    """Controls keyboard and hardware buttons on iOS simulator."""

    # Special key mappings to iOS HID key codes
    # See: https://developer.apple.com/documentation/uikit/uikeyboardhidusage
    SPECIAL_KEYS = {
        "return": 40,
        "enter": 40,
        "delete": 42,
        "backspace": 42,
        "tab": 43,
        "space": 44,
        "escape": 41,
        "up": 82,
        "down": 81,
        "left": 80,
        "right": 79,
    }

    # Hardware button mappings
    HARDWARE_BUTTONS = {
        "home": "HOME",
        "lock": "LOCK",
        "volume-up": "VOLUME_UP",
        "volume-down": "VOLUME_DOWN",
        "ringer": "RINGER",
        "power": "LOCK",  # Alias
        "screenshot": "SCREENSHOT",
    }

    def __init__(self, udid: str | None = None):
        """Initialize keyboard controller."""
        self.udid = udid

    def type_text(self, text: str, delay: float = 0.0) -> bool:
        """
        Type text into current focus.

        Args:
            text: Text to type
            delay: Delay between characters (for slow typing effect)

        Returns:
            Success status
        """
        if delay > 0:
            # Type character by character with delay
            for char in text:
                if not self._type_single(char):
                    return False
                time.sleep(delay)
            return True
        # Type all at once (efficient)
        return self._type_single(text)

    def _type_single(self, text: str) -> bool:
        """Type text using IDB."""
        cmd = ["idb", "ui", "text", text]
        if self.udid:
            cmd.extend(["--udid", self.udid])

        try:
            subprocess.run(cmd, capture_output=True, check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def press_key(self, key: str, count: int = 1) -> bool:
        """
        Press a special key.

        Args:
            key: Key name (return, delete, tab, etc.)
            count: Number of times to press

        Returns:
            Success status
        """
        # Map key name to IDB key code
        key_code = self.SPECIAL_KEYS.get(key.lower())
        if not key_code:
            # Try as literal integer key code
            try:
                key_code = int(key)
            except ValueError:
                return False

        cmd = ["idb", "ui", "key", str(key_code)]
        if self.udid:
            cmd.extend(["--udid", self.udid])

        try:
            for _ in range(count):
                subprocess.run(cmd, capture_output=True, check=True)
                if count > 1:
                    time.sleep(0.1)  # Small delay for multiple presses
            return True
        except subprocess.CalledProcessError:
            return False

    def press_key_sequence(self, keys: list[str]) -> bool:
        """
        Press a sequence of keys.

        Args:
            keys: List of key names

        Returns:
            Success status
        """
        cmd_base = ["idb", "ui", "key-sequence"]

        # Map keys to codes
        mapped_keys = []
        for key in keys:
            mapped = self.SPECIAL_KEYS.get(key.lower())
            if mapped is None:
                # Try as integer
                try:
                    mapped = int(key)
                except ValueError:
                    return False
            mapped_keys.append(str(mapped))

        cmd = cmd_base + mapped_keys

        if self.udid:
            cmd.extend(["--udid", self.udid])

        try:
            subprocess.run(cmd, capture_output=True, check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def press_hardware_button(self, button: str) -> bool:
        """
        Press hardware button.

        Args:
            button: Button name (home, lock, volume-up, etc.)

        Returns:
            Success status
        """
        button_code = self.HARDWARE_BUTTONS.get(button.lower())
        if not button_code:
            return False

        cmd = ["idb", "ui", "button", button_code]
        if self.udid:
            cmd.extend(["--udid", self.udid])

        try:
            subprocess.run(cmd, capture_output=True, check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def clear_text(self, select_all: bool = True) -> bool:
        """
        Clear text in current field.

        Args:
            select_all: Use Cmd+A to select all first

        Returns:
            Success status
        """
        if select_all:
            # Select all then delete
            # Note: This might need adjustment for iOS keyboard shortcuts
            success = self.press_key_combo(["cmd", "a"])
            if success:
                return self.press_key("delete")
        else:
            # Just delete multiple times
            return self.press_key("delete", count=50)
        return None

    def press_key_combo(self, keys: list[str]) -> bool:
        """
        Press key combination (like Cmd+A).

        Args:
            keys: List of keys to press together

        Returns:
            Success status
        """
        # IDB doesn't directly support key combos
        # This is a workaround - may need platform-specific handling
        if "cmd" in keys or "command" in keys:
            # Handle common shortcuts
            if "a" in keys:
                # Select all - might work with key sequence
                return self.press_key_sequence(["command", "a"])
            if "c" in keys:
                return self.press_key_sequence(["command", "c"])
            if "v" in keys:
                return self.press_key_sequence(["command", "v"])
            if "x" in keys:
                return self.press_key_sequence(["command", "x"])

        # Try as sequence
        return self.press_key_sequence(keys)

    def dismiss_keyboard(self) -> bool:
        """Dismiss on-screen keyboard."""
        # Common ways to dismiss keyboard on iOS
        # Try Done button first, then Return
        success = self.press_key("return")
        if not success:
            # Try tapping outside (would need coordinate)
            pass
        return success


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Control keyboard and hardware buttons")

    # Text input
    parser.add_argument("--type", help="Type text into current focus")
    parser.add_argument("--slow", action="store_true", help="Type slowly (character by character)")

    # Special keys
    parser.add_argument("--key", help="Press special key (return, delete, tab, space, etc.)")
    parser.add_argument("--key-sequence", help="Press key sequence (comma-separated)")
    parser.add_argument("--count", type=int, default=1, help="Number of times to press key")

    # Hardware buttons
    parser.add_argument(
        "--button",
        choices=["home", "lock", "volume-up", "volume-down", "ringer", "screenshot"],
        help="Press hardware button",
    )

    # Other operations
    parser.add_argument("--clear", action="store_true", help="Clear current text field")
    parser.add_argument("--dismiss", action="store_true", help="Dismiss keyboard")

    parser.add_argument(
        "--udid",
        help="Device UDID (auto-detects booted simulator if not provided)",
    )

    args = parser.parse_args()

    # Resolve UDID with auto-detection
    try:
        udid = resolve_udid(args.udid)
    except RuntimeError as e:
        print(f"Error: {e}")
        sys.exit(1)

    controller = KeyboardController(udid=udid)

    # Execute requested action
    if args.type:
        delay = 0.1 if args.slow else 0.0
        if controller.type_text(args.type, delay):
            if args.slow:
                print(f'Typed: "{args.type}" (slowly)')
            else:
                print(f'Typed: "{args.type}"')
        else:
            print("Failed to type text")
            sys.exit(1)

    elif args.key:
        if controller.press_key(args.key, args.count):
            if args.count > 1:
                print(f"Pressed {args.key} ({args.count}x)")
            else:
                print(f"Pressed {args.key}")
        else:
            print(f"Failed to press {args.key}")
            sys.exit(1)

    elif args.key_sequence:
        keys = args.key_sequence.split(",")
        if controller.press_key_sequence(keys):
            print(f"Pressed sequence: {' -> '.join(keys)}")
        else:
            print("Failed to press key sequence")
            sys.exit(1)

    elif args.button:
        if controller.press_hardware_button(args.button):
            print(f"Pressed {args.button} button")
        else:
            print(f"Failed to press {args.button}")
            sys.exit(1)

    elif args.clear:
        if controller.clear_text():
            print("Cleared text field")
        else:
            print("Failed to clear text")
            sys.exit(1)

    elif args.dismiss:
        if controller.dismiss_keyboard():
            print("Dismissed keyboard")
        else:
            print("Failed to dismiss keyboard")
            sys.exit(1)

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
```

## File: `ios-simulator-skill/scripts/log_monitor.py`
```python
#!/usr/bin/env python3
"""
iOS Simulator Log Monitoring and Analysis

Real-time log streaming from iOS simulators with intelligent filtering, error detection,
and token-efficient summarization. Enhanced version of app_state_capture.py's log capture.

Features:
- Real-time log streaming from booted simulators
- Smart filtering by app bundle ID, subsystem, category, severity
- Error/warning classification and deduplication
- Duration-based or continuous follow mode
- Token-efficient summaries with full logs saved to file
- Integration with test_recorder and app_state_capture

Usage Examples:
    # Monitor app logs in real-time (follow mode)
    python scripts/log_monitor.py --app com.myapp.MyApp --follow

    # Capture logs for specific duration
    python scripts/log_monitor.py --app com.myapp.MyApp --duration 30s

    # Extract errors and warnings only from last 5 minutes
    python scripts/log_monitor.py --severity error,warning --last 5m

    # Save logs to file
    python scripts/log_monitor.py --app com.myapp.MyApp --duration 1m --output logs/

    # Verbose output with full log lines
    python scripts/log_monitor.py --app com.myapp.MyApp --verbose
"""

import argparse
import json
import re
import signal
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path


class LogMonitor:
    """Monitor and analyze iOS simulator logs with intelligent filtering."""

    def __init__(
        self,
        app_bundle_id: str | None = None,
        device_udid: str | None = None,
        severity_filter: list[str] | None = None,
    ):
        """
        Initialize log monitor.

        Args:
            app_bundle_id: Filter logs by app bundle ID
            device_udid: Device UDID (uses booted if not specified)
            severity_filter: List of severities to include (error, warning, info, debug)
        """
        self.app_bundle_id = app_bundle_id
        self.device_udid = device_udid or "booted"
        self.severity_filter = severity_filter or ["error", "warning", "info", "debug"]

        # Log storage
        self.log_lines: list[str] = []
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.info_messages: list[str] = []

        # Statistics
        self.error_count = 0
        self.warning_count = 0
        self.info_count = 0
        self.debug_count = 0
        self.total_lines = 0

        # Deduplication
        self.seen_messages: set[str] = set()

        # Process control
        self.log_process: subprocess.Popen | None = None
        self.interrupted = False

    def parse_time_duration(self, duration_str: str) -> float:
        """
        Parse duration string to seconds.

        Args:
            duration_str: Duration like "30s", "5m", "1h"

        Returns:
            Duration in seconds
        """
        match = re.match(r"(\d+)([smh])", duration_str.lower())
        if not match:
            raise ValueError(
                f"Invalid duration format: {duration_str}. Use format like '30s', '5m', '1h'"
            )

        value, unit = match.groups()
        value = int(value)

        if unit == "s":
            return value
        if unit == "m":
            return value * 60
        if unit == "h":
            return value * 3600

        return 0

    def classify_log_line(self, line: str) -> str | None:
        """
        Classify log line by severity.

        Args:
            line: Log line to classify

        Returns:
            Severity level (error, warning, info, debug) or None
        """
        line_lower = line.lower()

        # Error patterns
        error_patterns = [
            r"\berror\b",
            r"\bfault\b",
            r"\bfailed\b",
            r"\bexception\b",
            r"\bcrash\b",
            r"❌",
        ]

        # Warning patterns
        warning_patterns = [r"\bwarning\b", r"\bwarn\b", r"\bdeprecated\b", r"⚠️"]

        # Info patterns
        info_patterns = [r"\binfo\b", r"\bnotice\b", r"ℹ️"]

        for pattern in error_patterns:
            if re.search(pattern, line_lower):
                return "error"

        for pattern in warning_patterns:
            if re.search(pattern, line_lower):
                return "warning"

        for pattern in info_patterns:
            if re.search(pattern, line_lower):
                return "info"

        return "debug"

    def deduplicate_message(self, line: str) -> bool:
        """
        Check if message is duplicate.

        Args:
            line: Log line

        Returns:
            True if this is a new message, False if duplicate
        """
        # Create signature by removing timestamps and process IDs
        signature = re.sub(r"\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}", "", line)
        signature = re.sub(r"\[\d+\]", "", signature)
        signature = re.sub(r"\s+", " ", signature).strip()

        if signature in self.seen_messages:
            return False

        self.seen_messages.add(signature)
        return True

    def process_log_line(self, line: str):
        """
        Process a single log line.

        Args:
            line: Log line to process
        """
        if not line.strip():
            return

        self.total_lines += 1
        self.log_lines.append(line)

        # Classify severity
        severity = self.classify_log_line(line)

        # Skip if not in filter
        if severity not in self.severity_filter:
            return

        # Deduplicate (for errors and warnings)
        if severity in ["error", "warning"] and not self.deduplicate_message(line):
            return

        # Store by severity
        if severity == "error":
            self.error_count += 1
            self.errors.append(line)
        elif severity == "warning":
            self.warning_count += 1
            self.warnings.append(line)
        elif severity == "info":
            self.info_count += 1
            if len(self.info_messages) < 20:  # Keep only recent info
                self.info_messages.append(line)
        else:  # debug
            self.debug_count += 1

    def stream_logs(
        self,
        follow: bool = False,
        duration: float | None = None,
        last_minutes: float | None = None,
    ) -> bool:
        """
        Stream logs from simulator.

        Args:
            follow: Follow mode (continuous streaming)
            duration: Capture duration in seconds
            last_minutes: Show logs from last N minutes

        Returns:
            True if successful
        """
        # Build log stream command
        cmd = ["xcrun", "simctl", "spawn", self.device_udid, "log", "stream"]

        # Add filters
        if self.app_bundle_id:
            # Filter by process name (extracted from bundle ID)
            app_name = self.app_bundle_id.split(".")[-1]
            cmd.extend(["--predicate", f'processImagePath CONTAINS "{app_name}"'])

        # Add time filter for historical logs
        if last_minutes:
            start_time = datetime.now() - timedelta(minutes=last_minutes)
            time_str = start_time.strftime("%Y-%m-%d %H:%M:%S")
            cmd.extend(["--start", time_str])

        # Setup signal handler for graceful interruption
        def signal_handler(sig, frame):
            self.interrupted = True
            if self.log_process:
                self.log_process.terminate()

        signal.signal(signal.SIGINT, signal_handler)

        try:
            # Start log streaming process
            self.log_process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,  # Line buffered
            )

            # Track start time for duration
            start_time = datetime.now()

            # Process log lines
            for line in iter(self.log_process.stdout.readline, ""):
                if not line:
                    break

                # Process the line
                self.process_log_line(line.rstrip())

                # Print in follow mode
                if follow:
                    severity = self.classify_log_line(line)
                    if severity in self.severity_filter:
                        print(line.rstrip())

                # Check duration
                if duration and (datetime.now() - start_time).total_seconds() >= duration:
                    break

                # Check if interrupted
                if self.interrupted:
                    break

            # Wait for process to finish
            self.log_process.wait()
            return True

        except Exception as e:
            print(f"Error streaming logs: {e}", file=sys.stderr)
            return False

        finally:
            if self.log_process:
                self.log_process.terminate()

    def get_summary(self, verbose: bool = False) -> str:
        """
        Get log summary.

        Args:
            verbose: Include full log details

        Returns:
            Formatted summary string
        """
        lines = []

        # Header
        if self.app_bundle_id:
            lines.append(f"Logs for: {self.app_bundle_id}")
        else:
            lines.append("Logs for: All processes")

        # Statistics
        lines.append(f"Total lines: {self.total_lines}")
        lines.append(
            f"Errors: {self.error_count}, Warnings: {self.warning_count}, Info: {self.info_count}"
        )

        # Top issues
        if self.errors:
            lines.append(f"\nTop Errors ({len(self.errors)}):")
            for error in self.errors[:5]:  # Show first 5
                lines.append(f"  ❌ {error[:120]}")  # Truncate long lines

        if self.warnings:
            lines.append(f"\nTop Warnings ({len(self.warnings)}):")
            for warning in self.warnings[:5]:  # Show first 5
                lines.append(f"  ⚠️  {warning[:120]}")

        # Verbose output
        if verbose and self.log_lines:
            lines.append("\n=== Recent Log Lines ===")
            for line in self.log_lines[-50:]:  # Last 50 lines
                lines.append(line)

        return "\n".join(lines)

    def get_json_output(self) -> dict:
        """Get log results as JSON."""
        return {
            "app_bundle_id": self.app_bundle_id,
            "device_udid": self.device_udid,
            "statistics": {
                "total_lines": self.total_lines,
                "errors": self.error_count,
                "warnings": self.warning_count,
                "info": self.info_count,
                "debug": self.debug_count,
            },
            "errors": self.errors[:20],  # Limit to 20
            "warnings": self.warnings[:20],
            "sample_logs": self.log_lines[-50:],  # Last 50 lines
        }

    def save_logs(self, output_dir: str) -> str:
        """
        Save logs to file.

        Args:
            output_dir: Directory to save logs

        Returns:
            Path to saved log file
        """
        # Create output directory
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        app_name = self.app_bundle_id.split(".")[-1] if self.app_bundle_id else "simulator"
        log_file = output_path / f"{app_name}-{timestamp}.log"

        # Write all log lines
        with open(log_file, "w") as f:
            f.write("\n".join(self.log_lines))

        # Also save JSON summary
        json_file = output_path / f"{app_name}-{timestamp}-summary.json"
        with open(json_file, "w") as f:
            json.dump(self.get_json_output(), f, indent=2)

        return str(log_file)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Monitor and analyze iOS simulator logs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Monitor app in real-time
  python scripts/log_monitor.py --app com.myapp.MyApp --follow

  # Capture logs for 30 seconds
  python scripts/log_monitor.py --app com.myapp.MyApp --duration 30s

  # Show errors/warnings from last 5 minutes
  python scripts/log_monitor.py --severity error,warning --last 5m

  # Save logs to file
  python scripts/log_monitor.py --app com.myapp.MyApp --duration 1m --output logs/
        """,
    )

    # Filtering options
    parser.add_argument(
        "--app", dest="app_bundle_id", help="App bundle ID to filter logs (e.g., com.myapp.MyApp)"
    )
    parser.add_argument("--device-udid", help="Device UDID (uses booted if not specified)")
    parser.add_argument(
        "--severity", help="Comma-separated severity levels (error,warning,info,debug)"
    )

    # Time options
    time_group = parser.add_mutually_exclusive_group()
    time_group.add_argument(
        "--follow", action="store_true", help="Follow mode (continuous streaming)"
    )
    time_group.add_argument("--duration", help="Capture duration (e.g., 30s, 5m, 1h)")
    time_group.add_argument(
        "--last", dest="last_minutes", help="Show logs from last N minutes (e.g., 5m)"
    )

    # Output options
    parser.add_argument("--output", help="Save logs to directory")
    parser.add_argument("--verbose", action="store_true", help="Show detailed output")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    # Parse severity filter
    severity_filter = None
    if args.severity:
        severity_filter = [s.strip().lower() for s in args.severity.split(",")]

    # Initialize monitor
    monitor = LogMonitor(
        app_bundle_id=args.app_bundle_id,
        device_udid=args.device_udid,
        severity_filter=severity_filter,
    )

    # Parse duration
    duration = None
    if args.duration:
        duration = monitor.parse_time_duration(args.duration)

    # Parse last minutes
    last_minutes = None
    if args.last_minutes:
        last_minutes = monitor.parse_time_duration(args.last_minutes) / 60

    # Stream logs
    print("Monitoring logs...", file=sys.stderr)
    if args.app_bundle_id:
        print(f"App: {args.app_bundle_id}", file=sys.stderr)

    success = monitor.stream_logs(follow=args.follow, duration=duration, last_minutes=last_minutes)

    if not success:
        sys.exit(1)

    # Save logs if requested
    if args.output:
        log_file = monitor.save_logs(args.output)
        print(f"\nLogs saved to: {log_file}", file=sys.stderr)

    # Output results
    if not args.follow:  # Don't show summary in follow mode
        if args.json:
            print(json.dumps(monitor.get_json_output(), indent=2))
        else:
            print("\n" + monitor.get_summary(verbose=args.verbose))

    sys.exit(0)


if __name__ == "__main__":
    main()
```

## File: `ios-simulator-skill/scripts/navigator.py`
```python
#!/usr/bin/env python3
"""
iOS Simulator Navigator - Smart Element Finder and Interactor

Finds and interacts with UI elements using accessibility data.
Prioritizes structured navigation over pixel-based interaction.

This script is the core automation tool for iOS simulator navigation. It finds
UI elements by text, type, or accessibility ID and performs actions on them
(tap, enter text). Uses semantic element finding instead of fragile pixel coordinates.

Key Features:
- Find elements by text (fuzzy or exact matching)
- Find elements by type (Button, TextField, etc.)
- Find elements by accessibility identifier
- Tap elements at their center point
- Enter text into text fields
- List all tappable elements on screen
- Automatic element caching for performance

Usage Examples:
    # Find and tap a button by text
    python scripts/navigator.py --find-text "Login" --tap --udid <device-id>

    # Enter text into first text field
    python scripts/navigator.py --find-type TextField --index 0 --enter-text "username" --udid <device-id>

    # Tap element by accessibility ID
    python scripts/navigator.py --find-id "submitButton" --tap --udid <device-id>

    # List all interactive elements
    python scripts/navigator.py --list --udid <device-id>

    # Tap at specific coordinates (fallback)
    python scripts/navigator.py --tap-at 200,400 --udid <device-id>

Output Format:
    Tapped: Button "Login" at (320, 450)
    Entered text in: TextField "Username"
    Not found: text='Submit'

Navigation Priority (best to worst):
    1. Find by accessibility label/text (most reliable)
    2. Find by element type + index (good for forms)
    3. Find by accessibility ID (precise but app-specific)
    4. Tap at coordinates (last resort, fragile)

Technical Details:
- Uses IDB's accessibility tree via `idb ui describe-all --json --nested`
- Caches tree for multiple operations (call with force_refresh to update)
- Finds elements by parsing tree recursively
- Calculates tap coordinates from element frame center
- Uses `idb ui tap` for tapping, `idb ui text` for text entry
- Extracts data from AXLabel, AXValue, and AXUniqueId fields
"""

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass

from common import (
    flatten_tree,
    get_accessibility_tree,
    get_device_screen_size,
    resolve_udid,
    transform_screenshot_coords,
)


@dataclass
class Element:
    """Represents a UI element from accessibility tree."""

    type: str
    label: str | None
    value: str | None
    identifier: str | None
    frame: dict[str, float]
    traits: list[str]
    enabled: bool = True

    @property
    def center(self) -> tuple[int, int]:
        """Calculate center point for tapping."""
        x = int(self.frame["x"] + self.frame["width"] / 2)
        y = int(self.frame["y"] + self.frame["height"] / 2)
        return (x, y)

    @property
    def description(self) -> str:
        """Human-readable description."""
        label = self.label or self.value or self.identifier or "Unnamed"
        return f'{self.type} "{label}"'


class Navigator:
    """Navigates iOS apps using accessibility data."""

    def __init__(self, udid: str | None = None):
        """Initialize navigator with optional device UDID."""
        self.udid = udid
        self._tree_cache = None

    def get_accessibility_tree(self, force_refresh: bool = False) -> dict:
        """Get accessibility tree (cached for efficiency)."""
        if self._tree_cache and not force_refresh:
            return self._tree_cache

        # Delegate to shared utility
        self._tree_cache = get_accessibility_tree(self.udid, nested=True)
        return self._tree_cache

    def _flatten_tree(self, node: dict, elements: list[Element] | None = None) -> list[Element]:
        """Flatten accessibility tree into list of elements."""
        if elements is None:
            elements = []

        # Create element from node
        if node.get("type"):
            element = Element(
                type=node.get("type", "Unknown"),
                label=node.get("AXLabel"),
                value=node.get("AXValue"),
                identifier=node.get("AXUniqueId"),
                frame=node.get("frame", {}),
                traits=node.get("traits", []),
                enabled=node.get("enabled", True),
            )
            elements.append(element)

        # Process children
        for child in node.get("children", []):
            self._flatten_tree(child, elements)

        return elements

    def list_elements(self, force_refresh: bool = False) -> list[Element]:
        """Get flat list of all UI elements on current screen."""
        tree = self.get_accessibility_tree(force_refresh)
        return self._flatten_tree(tree)

    def find_element(
        self,
        text: str | None = None,
        element_type: str | None = None,
        identifier: str | None = None,
        index: int = 0,
        fuzzy: bool = True,
    ) -> Element | None:
        """
        Find element by various criteria.

        Args:
            text: Text to search in label/value
            element_type: Type of element (Button, TextField, etc.)
            identifier: Accessibility identifier
            index: Which matching element to return (0-based)
            fuzzy: Use fuzzy matching for text

        Returns:
            Element if found, None otherwise
        """
        tree = self.get_accessibility_tree()
        elements = self._flatten_tree(tree)

        matches = []

        for elem in elements:
            # Skip disabled elements
            if not elem.enabled:
                continue

            # Check type
            if element_type and elem.type != element_type:
                continue

            # Check identifier (exact match)
            if identifier and elem.identifier != identifier:
                continue

            # Check text (in label or value)
            if text:
                elem_text = (elem.label or "") + " " + (elem.value or "")
                if fuzzy:
                    if text.lower() not in elem_text.lower():
                        continue
                elif text not in (elem.label, elem.value):
                    continue

            matches.append(elem)

        if matches and index < len(matches):
            return matches[index]

        return None

    def tap(self, element: Element) -> bool:
        """Tap on an element."""
        x, y = element.center
        return self.tap_at(x, y)

    def tap_at(self, x: int, y: int) -> bool:
        """Tap at specific coordinates."""
        cmd = ["idb", "ui", "tap", str(x), str(y)]
        if self.udid:
            cmd.extend(["--udid", self.udid])

        try:
            subprocess.run(cmd, capture_output=True, check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def enter_text(self, text: str, element: Element | None = None) -> bool:
        """
        Enter text into element or current focus.

        Args:
            text: Text to enter
            element: Optional element to tap first

        Returns:
            Success status
        """
        # Tap element if provided
        if element:
            if not self.tap(element):
                return False
            # Small delay for focus
            import time

            time.sleep(0.5)

        # Enter text
        cmd = ["idb", "ui", "text", text]
        if self.udid:
            cmd.extend(["--udid", self.udid])

        try:
            subprocess.run(cmd, capture_output=True, check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def find_and_tap(
        self,
        text: str | None = None,
        element_type: str | None = None,
        identifier: str | None = None,
        index: int = 0,
    ) -> tuple[bool, str]:
        """
        Find element and tap it.

        Returns:
            (success, message) tuple
        """
        element = self.find_element(text, element_type, identifier, index)

        if not element:
            criteria = []
            if text:
                criteria.append(f"text='{text}'")
            if element_type:
                criteria.append(f"type={element_type}")
            if identifier:
                criteria.append(f"id={identifier}")
            return (False, f"Not found: {', '.join(criteria)}")

        if self.tap(element):
            return (True, f"Tapped: {element.description} at {element.center}")
        return (False, f"Failed to tap: {element.description}")

    def find_and_enter_text(
        self,
        text_to_enter: str,
        find_text: str | None = None,
        element_type: str | None = "TextField",
        identifier: str | None = None,
        index: int = 0,
    ) -> tuple[bool, str]:
        """
        Find element and enter text into it.

        Returns:
            (success, message) tuple
        """
        element = self.find_element(find_text, element_type, identifier, index)

        if not element:
            return (False, "TextField not found")

        if self.enter_text(text_to_enter, element):
            return (True, f"Entered text in: {element.description}")
        return (False, "Failed to enter text")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Navigate iOS apps using accessibility data")

    # Finding options
    parser.add_argument("--find-text", help="Find element by text (fuzzy match)")
    parser.add_argument("--find-exact", help="Find element by exact text")
    parser.add_argument("--find-type", help="Element type (Button, TextField, etc.)")
    parser.add_argument("--find-id", help="Accessibility identifier")
    parser.add_argument("--index", type=int, default=0, help="Which match to use (0-based)")

    # Action options
    parser.add_argument("--tap", action="store_true", help="Tap the found element")
    parser.add_argument("--tap-at", help="Tap at coordinates (x,y)")
    parser.add_argument("--enter-text", help="Enter text into element")

    # Coordinate transformation
    parser.add_argument(
        "--screenshot-coords",
        action="store_true",
        help="Interpret tap coordinates as from a screenshot (requires --screenshot-width/height)",
    )
    parser.add_argument(
        "--screenshot-width",
        type=int,
        help="Screenshot width for coordinate transformation",
    )
    parser.add_argument(
        "--screenshot-height",
        type=int,
        help="Screenshot height for coordinate transformation",
    )

    # Other options
    parser.add_argument(
        "--udid",
        help="Device UDID (auto-detects booted simulator if not provided)",
    )
    parser.add_argument("--list", action="store_true", help="List all tappable elements")

    args = parser.parse_args()

    # Resolve UDID with auto-detection
    try:
        udid = resolve_udid(args.udid)
    except RuntimeError as e:
        print(f"Error: {e}")
        sys.exit(1)

    navigator = Navigator(udid=udid)

    # List mode
    if args.list:
        elements = navigator.list_elements()

        # Filter to tappable elements
        tappable = [
            e
            for e in elements
            if e.enabled and e.type in ["Button", "Link", "Cell", "TextField", "SecureTextField"]
        ]

        print(f"Tappable elements ({len(tappable)}):")
        for elem in tappable[:10]:  # Limit output for tokens
            print(f"  {elem.type}: \"{elem.label or elem.value or 'Unnamed'}\" {elem.center}")

        if len(tappable) > 10:
            print(f"  ... and {len(tappable) - 10} more")
        sys.exit(0)

    # Direct tap at coordinates
    if args.tap_at:
        coords = args.tap_at.split(",")
        if len(coords) != 2:
            print("Error: --tap-at requires x,y format")
            sys.exit(1)

        x, y = int(coords[0]), int(coords[1])

        # Handle coordinate transformation if requested
        if args.screenshot_coords:
            if not args.screenshot_width or not args.screenshot_height:
                print(
                    "Error: --screenshot-coords requires --screenshot-width and --screenshot-height"
                )
                sys.exit(1)

            device_w, device_h = get_device_screen_size(udid)
            x, y = transform_screenshot_coords(
                x,
                y,
                args.screenshot_width,
                args.screenshot_height,
                device_w,
                device_h,
            )
            print(
                f"Transformed screenshot coords ({coords[0]}, {coords[1]}) "
                f"to device coords ({x}, {y})"
            )

        if navigator.tap_at(x, y):
            print(f"Tapped at ({x}, {y})")
        else:
            print(f"Failed to tap at ({x}, {y})")
            sys.exit(1)

    # Find and tap
    elif args.tap:
        text = args.find_text or args.find_exact
        fuzzy = args.find_text is not None

        success, message = navigator.find_and_tap(
            text=text, element_type=args.find_type, identifier=args.find_id, index=args.index
        )

        print(message)
        if not success:
            sys.exit(1)

    # Find and enter text
    elif args.enter_text:
        text = args.find_text or args.find_exact

        success, message = navigator.find_and_enter_text(
            text_to_enter=args.enter_text,
            find_text=text,
            element_type=args.find_type or "TextField",
            identifier=args.find_id,
            index=args.index,
        )

        print(message)
        if not success:
            sys.exit(1)

    # Just find (no action)
    else:
        text = args.find_text or args.find_exact
        fuzzy = args.find_text is not None

        element = navigator.find_element(
            text=text,
            element_type=args.find_type,
            identifier=args.find_id,
            index=args.index,
            fuzzy=fuzzy,
        )

        if element:
            print(f"Found: {element.description} at {element.center}")
        else:
            print("Element not found")
            sys.exit(1)


if __name__ == "__main__":
    main()
```

## File: `ios-simulator-skill/scripts/privacy_manager.py`
```python
#!/usr/bin/env python3
"""
iOS Privacy & Permissions Manager

Grant/revoke app permissions for testing permission flows.
Supports 13+ services with audit trail tracking.

Usage: python scripts/privacy_manager.py --grant camera --bundle-id com.app
"""

import argparse
import subprocess
import sys
from datetime import datetime

from common import resolve_udid


class PrivacyManager:
    """Manages iOS app privacy and permissions."""

    # Supported services
    SUPPORTED_SERVICES = {
        "camera": "Camera access",
        "microphone": "Microphone access",
        "location": "Location services",
        "contacts": "Contacts access",
        "photos": "Photos library access",
        "calendar": "Calendar access",
        "health": "Health data access",
        "reminders": "Reminders access",
        "motion": "Motion & fitness",
        "keyboard": "Keyboard access",
        "mediaLibrary": "Media library",
        "calls": "Call history",
        "siri": "Siri access",
    }

    def __init__(self, udid: str | None = None):
        """Initialize privacy manager.

        Args:
            udid: Optional device UDID (auto-detects booted simulator if None)
        """
        self.udid = udid

    def grant_permission(
        self,
        bundle_id: str,
        service: str,
        scenario: str | None = None,
        step: int | None = None,
    ) -> bool:
        """
        Grant permission for app.

        Args:
            bundle_id: App bundle ID
            service: Service name (camera, microphone, location, etc.)
            scenario: Test scenario name for audit trail
            step: Step number in test scenario

        Returns:
            Success status
        """
        if service not in self.SUPPORTED_SERVICES:
            print(f"Error: Unknown service '{service}'")
            print(f"Supported: {', '.join(self.SUPPORTED_SERVICES.keys())}")
            return False

        cmd = ["xcrun", "simctl", "privacy"]

        if self.udid:
            cmd.append(self.udid)
        else:
            cmd.append("booted")

        cmd.extend(["grant", service, bundle_id])

        try:
            subprocess.run(cmd, capture_output=True, check=True)

            # Log audit entry
            self._log_audit("grant", bundle_id, service, scenario, step)

            return True
        except subprocess.CalledProcessError:
            return False

    def revoke_permission(
        self,
        bundle_id: str,
        service: str,
        scenario: str | None = None,
        step: int | None = None,
    ) -> bool:
        """
        Revoke permission for app.

        Args:
            bundle_id: App bundle ID
            service: Service name
            scenario: Test scenario name for audit trail
            step: Step number in test scenario

        Returns:
            Success status
        """
        if service not in self.SUPPORTED_SERVICES:
            print(f"Error: Unknown service '{service}'")
            return False

        cmd = ["xcrun", "simctl", "privacy"]

        if self.udid:
            cmd.append(self.udid)
        else:
            cmd.append("booted")

        cmd.extend(["revoke", service, bundle_id])

        try:
            subprocess.run(cmd, capture_output=True, check=True)

            # Log audit entry
            self._log_audit("revoke", bundle_id, service, scenario, step)

            return True
        except subprocess.CalledProcessError:
            return False

    def reset_permission(
        self,
        bundle_id: str,
        service: str,
        scenario: str | None = None,
        step: int | None = None,
    ) -> bool:
        """
        Reset permission to default.

        Args:
            bundle_id: App bundle ID
            service: Service name
            scenario: Test scenario name for audit trail
            step: Step number in test scenario

        Returns:
            Success status
        """
        if service not in self.SUPPORTED_SERVICES:
            print(f"Error: Unknown service '{service}'")
            return False

        cmd = ["xcrun", "simctl", "privacy"]

        if self.udid:
            cmd.append(self.udid)
        else:
            cmd.append("booted")

        cmd.extend(["reset", service, bundle_id])

        try:
            subprocess.run(cmd, capture_output=True, check=True)

            # Log audit entry
            self._log_audit("reset", bundle_id, service, scenario, step)

            return True
        except subprocess.CalledProcessError:
            return False

    @staticmethod
    def _log_audit(
        action: str,
        bundle_id: str,
        service: str,
        scenario: str | None = None,
        step: int | None = None,
    ) -> None:
        """Log permission change to audit trail (for test tracking).

        Args:
            action: grant, revoke, or reset
            bundle_id: App bundle ID
            service: Service name
            scenario: Test scenario name
            step: Step number
        """
        # Could write to file, but for now just log to stdout for transparency
        timestamp = datetime.now().isoformat()
        location = f" (step {step})" if step else ""
        scenario_info = f" in {scenario}" if scenario else ""
        print(
            f"[Audit] {timestamp}: {action.upper()} {service} for {bundle_id}{scenario_info}{location}"
        )


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Manage iOS app privacy and permissions")

    # Required
    parser.add_argument("--bundle-id", required=True, help="App bundle ID (e.g., com.example.app)")

    # Action (mutually exclusive)
    action_group = parser.add_mutually_exclusive_group(required=True)
    action_group.add_argument(
        "--grant",
        help="Grant permission (service name or comma-separated list)",
    )
    action_group.add_argument(
        "--revoke", help="Revoke permission (service name or comma-separated list)"
    )
    action_group.add_argument(
        "--reset",
        help="Reset permission to default (service name or comma-separated list)",
    )
    action_group.add_argument(
        "--list",
        action="store_true",
        help="List all supported services",
    )

    # Test tracking
    parser.add_argument(
        "--scenario",
        help="Test scenario name for audit trail",
    )
    parser.add_argument("--step", type=int, help="Step number in test scenario")

    # Device
    parser.add_argument(
        "--udid",
        help="Device UDID (auto-detects booted simulator if not provided)",
    )

    args = parser.parse_args()

    # List supported services
    if args.list:
        print("Supported Privacy Services:\n")
        for service, description in PrivacyManager.SUPPORTED_SERVICES.items():
            print(f"  {service:<15} - {description}")
        print()
        print("Examples:")
        print("  python scripts/privacy_manager.py --grant camera --bundle-id com.app")
        print("  python scripts/privacy_manager.py --revoke location --bundle-id com.app")
        print("  python scripts/privacy_manager.py --grant camera,photos --bundle-id com.app")
        sys.exit(0)

    # Resolve UDID with auto-detection
    try:
        udid = resolve_udid(args.udid)
    except RuntimeError as e:
        print(f"Error: {e}")
        sys.exit(1)

    manager = PrivacyManager(udid=udid)

    # Parse service names (support comma-separated list)
    if args.grant:
        services = [s.strip() for s in args.grant.split(",")]
        action = "grant"
        action_fn = manager.grant_permission
    elif args.revoke:
        services = [s.strip() for s in args.revoke.split(",")]
        action = "revoke"
        action_fn = manager.revoke_permission
    else:  # reset
        services = [s.strip() for s in args.reset.split(",")]
        action = "reset"
        action_fn = manager.reset_permission

    # Execute action for each service
    all_success = True
    for service in services:
        if service not in PrivacyManager.SUPPORTED_SERVICES:
            print(f"Error: Unknown service '{service}'")
            all_success = False
            continue

        success = action_fn(
            args.bundle_id,
            service,
            scenario=args.scenario,
            step=args.step,
        )

        if success:
            description = PrivacyManager.SUPPORTED_SERVICES[service]
            print(f"✓ {action.capitalize()} {service}: {description}")
        else:
            print(f"✗ Failed to {action} {service}")
            all_success = False

    if not all_success:
        sys.exit(1)

    # Summary
    if len(services) > 1:
        print(f"\nPermissions {action}ed: {', '.join(services)}")

    if args.scenario:
        print(f"Test scenario: {args.scenario}" + (f" (step {args.step})" if args.step else ""))


if __name__ == "__main__":
    main()
```

## File: `ios-simulator-skill/scripts/push_notification.py`
```python
#!/usr/bin/env python3
"""
iOS Push Notification Simulator

Send simulated push notifications to test notification handling.
Supports custom payloads and test tracking.

Usage: python scripts/push_notification.py --bundle-id com.app --title "Alert" --body "Message"
"""

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

from common import resolve_udid


class PushNotificationSender:
    """Sends simulated push notifications to iOS simulator."""

    def __init__(self, udid: str | None = None):
        """Initialize push notification sender.

        Args:
            udid: Optional device UDID (auto-detects booted simulator if None)
        """
        self.udid = udid

    def send(
        self,
        bundle_id: str,
        payload: dict | str,
        _test_name: str | None = None,
        _expected_behavior: str | None = None,
    ) -> bool:
        """
        Send push notification to app.

        Args:
            bundle_id: Target app bundle ID
            payload: Push payload (dict or JSON string) or path to JSON file
            test_name: Test scenario name for tracking
            expected_behavior: Expected behavior after notification arrives

        Returns:
            Success status
        """
        # Handle different payload formats
        if isinstance(payload, str):
            # Check if it's a file path
            payload_path = Path(payload)
            if payload_path.exists():
                with open(payload_path) as f:
                    payload_data = json.load(f)
            else:
                # Try to parse as JSON string
                try:
                    payload_data = json.loads(payload)
                except json.JSONDecodeError:
                    print(f"Error: Invalid JSON payload: {payload}")
                    return False
        else:
            payload_data = payload

        # Ensure payload has aps dictionary
        if "aps" not in payload_data:
            payload_data = {"aps": payload_data}

        # Create temp file with payload
        try:
            with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
                json.dump(payload_data, f)
                temp_payload_path = f.name

            # Build simctl command
            cmd = ["xcrun", "simctl", "push"]

            if self.udid:
                cmd.append(self.udid)
            else:
                cmd.append("booted")

            cmd.extend([bundle_id, temp_payload_path])

            # Send notification
            subprocess.run(cmd, capture_output=True, text=True, check=True)

            # Clean up temp file
            Path(temp_payload_path).unlink()

            return True

        except subprocess.CalledProcessError as e:
            print(f"Error sending push notification: {e.stderr}")
            return False
        except Exception as e:
            print(f"Error: {e}")
            return False

    def send_simple(
        self,
        bundle_id: str,
        title: str | None = None,
        body: str | None = None,
        badge: int | None = None,
        sound: bool = True,
    ) -> bool:
        """
        Send simple push notification with common parameters.

        Args:
            bundle_id: Target app bundle ID
            title: Alert title
            body: Alert body
            badge: Badge number
            sound: Whether to play sound

        Returns:
            Success status
        """
        payload = {}

        if title or body:
            alert = {}
            if title:
                alert["title"] = title
            if body:
                alert["body"] = body
            payload["alert"] = alert

        if badge is not None:
            payload["badge"] = badge

        if sound:
            payload["sound"] = "default"

        # Wrap in aps
        full_payload = {"aps": payload}

        return self.send(bundle_id, full_payload)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Send simulated push notification to iOS app")

    # Required
    parser.add_argument(
        "--bundle-id", required=True, help="Target app bundle ID (e.g., com.example.app)"
    )

    # Simple payload options
    parser.add_argument("--title", help="Alert title (for simple notifications)")
    parser.add_argument("--body", help="Alert body message")
    parser.add_argument("--badge", type=int, help="Badge number")
    parser.add_argument("--no-sound", action="store_true", help="Don't play notification sound")

    # Custom payload
    parser.add_argument(
        "--payload",
        help="Custom JSON payload file or inline JSON string",
    )

    # Test tracking
    parser.add_argument("--test-name", help="Test scenario name for tracking")
    parser.add_argument(
        "--expected",
        help="Expected behavior after notification",
    )

    # Device
    parser.add_argument(
        "--udid",
        help="Device UDID (auto-detects booted simulator if not provided)",
    )

    args = parser.parse_args()

    # Resolve UDID with auto-detection
    try:
        udid = resolve_udid(args.udid)
    except RuntimeError as e:
        print(f"Error: {e}")
        sys.exit(1)

    sender = PushNotificationSender(udid=udid)

    # Send notification
    if args.payload:
        # Custom payload mode
        success = sender.send(args.bundle_id, args.payload)
    else:
        # Simple notification mode
        success = sender.send_simple(
            args.bundle_id,
            title=args.title,
            body=args.body,
            badge=args.badge,
            sound=not args.no_sound,
        )

    if success:
        # Token-efficient output
        output = "Push notification sent"

        if args.test_name:
            output += f" (test: {args.test_name})"

        print(output)

        if args.expected:
            print(f"Expected: {args.expected}")

        print()
        print("Notification details:")
        if args.title:
            print(f"  Title: {args.title}")
        if args.body:
            print(f"  Body: {args.body}")
        if args.badge:
            print(f"  Badge: {args.badge}")

        print()
        print("Verify notification handling:")
        print("1. Check app log output: python scripts/log_monitor.py --app " + args.bundle_id)
        print(
            "2. Capture state: python scripts/app_state_capture.py --app-bundle-id "
            + args.bundle_id
        )

    else:
        print("Failed to send push notification")
        sys.exit(1)


if __name__ == "__main__":
    main()
```

## File: `ios-simulator-skill/scripts/screen_mapper.py`
```python
#!/usr/bin/env python3
"""
iOS Screen Mapper - Current Screen Analyzer

Maps the current screen's UI elements for navigation decisions.
Provides token-efficient summaries of available interactions.

This script analyzes the iOS simulator screen using IDB's accessibility tree
and provides a compact, actionable summary of what's currently visible and
interactive on the screen. Perfect for AI agents making navigation decisions.

Key Features:
- Token-efficient output (5-7 lines by default)
- Identifies buttons, text fields, navigation elements
- Counts interactive and focusable elements
- Progressive detail with --verbose flag
- Navigation hints with --hints flag

Usage Examples:
    # Quick summary (default)
    python scripts/screen_mapper.py --udid <device-id>

    # Detailed element breakdown
    python scripts/screen_mapper.py --udid <device-id> --verbose

    # Include navigation suggestions
    python scripts/screen_mapper.py --udid <device-id> --hints

    # Full JSON output for parsing
    python scripts/screen_mapper.py --udid <device-id> --json

Output Format (default):
    Screen: LoginViewController (45 elements, 7 interactive)
    Buttons: "Login", "Cancel", "Forgot Password"
    TextFields: 2 (0 filled)
    Navigation: NavBar: "Sign In"
    Focusable: 7 elements

Technical Details:
- Uses IDB's accessibility tree via `idb ui describe-all --json --nested`
- Parses IDB's array format: [{ root element with children }]
- Identifies element types: Button, TextField, NavigationBar, TabBar, etc.
- Extracts labels from AXLabel, AXValue, and AXUniqueId fields
"""

import argparse
import json
import subprocess
import sys
from collections import defaultdict

from common import get_accessibility_tree, resolve_udid


class ScreenMapper:
    """
    Analyzes current screen for navigation decisions.

    This class fetches the iOS accessibility tree from IDB and analyzes it
    to provide actionable summaries for navigation. It categorizes elements
    by type, counts interactive elements, and identifies key UI patterns.

    Attributes:
        udid (Optional[str]): Device UDID to target, or None for booted device
        INTERACTIVE_TYPES (Set[str]): Element types that users can interact with

    Design Philosophy:
        - Token efficiency: Provide minimal but complete information
        - Progressive disclosure: Summary by default, details on request
        - Navigation-focused: Highlight elements relevant for automation
    """

    # Element types we care about for navigation
    # These are the accessibility element types that indicate user interaction points
    INTERACTIVE_TYPES = {
        "Button",
        "Link",
        "TextField",
        "SecureTextField",
        "Cell",
        "Switch",
        "Slider",
        "Stepper",
        "SegmentedControl",
        "TabBar",
        "NavigationBar",
        "Toolbar",
    }

    def __init__(self, udid: str | None = None):
        """
        Initialize screen mapper.

        Args:
            udid: Optional device UDID. If None, uses booted simulator.

        Example:
            mapper = ScreenMapper(udid="656DC652-1C9F-4AB2-AD4F-F38E65976BDA")
            mapper = ScreenMapper()  # Uses booted device
        """
        self.udid = udid

    def get_accessibility_tree(self) -> dict:
        """
        Fetch accessibility tree from iOS simulator via IDB.

        Delegates to shared utility for consistent tree fetching across all scripts.
        """
        return get_accessibility_tree(self.udid, nested=True)

    def analyze_tree(self, node: dict, depth: int = 0) -> dict:
        """Analyze accessibility tree for navigation info."""
        analysis = {
            "elements_by_type": defaultdict(list),
            "total_elements": 0,
            "interactive_elements": 0,
            "text_fields": [],
            "buttons": [],
            "navigation": {},
            "screen_name": None,
            "focusable": 0,
        }

        self._analyze_recursive(node, analysis, depth)

        # Post-process for clean output
        analysis["elements_by_type"] = dict(analysis["elements_by_type"])

        return analysis

    def _analyze_recursive(self, node: dict, analysis: dict, depth: int):
        """Recursively analyze tree nodes."""
        elem_type = node.get("type")
        label = node.get("AXLabel", "")
        value = node.get("AXValue", "")
        identifier = node.get("AXUniqueId", "")

        # Count element
        if elem_type:
            analysis["total_elements"] += 1

            # Track by type
            if elem_type in self.INTERACTIVE_TYPES:
                analysis["interactive_elements"] += 1

                # Store concise info (label only, not full node)
                elem_info = label or value or identifier or "Unnamed"
                analysis["elements_by_type"][elem_type].append(elem_info)

                # Special handling for common types
                if elem_type == "Button":
                    analysis["buttons"].append(elem_info)
                elif elem_type in ("TextField", "SecureTextField"):
                    analysis["text_fields"].append(
                        {"type": elem_type, "label": elem_info, "has_value": bool(value)}
                    )
                elif elem_type == "NavigationBar":
                    analysis["navigation"]["nav_title"] = label or "Navigation"
                elif elem_type == "TabBar":
                    # Count tab items
                    tab_count = len(node.get("children", []))
                    analysis["navigation"]["tab_count"] = tab_count

            # Track focusable elements
            if node.get("enabled", False) and elem_type in self.INTERACTIVE_TYPES:
                analysis["focusable"] += 1

        # Try to identify screen name from view controller
        if not analysis["screen_name"] and identifier:
            if "ViewController" in identifier or "Screen" in identifier:
                analysis["screen_name"] = identifier

        # Process children
        for child in node.get("children", []):
            self._analyze_recursive(child, analysis, depth + 1)

    def format_summary(self, analysis: dict, verbose: bool = False) -> str:
        """Format analysis as token-efficient summary."""
        lines = []

        # Screen identification (1 line)
        screen = analysis["screen_name"] or "Unknown Screen"
        total = analysis["total_elements"]
        interactive = analysis["interactive_elements"]
        lines.append(f"Screen: {screen} ({total} elements, {interactive} interactive)")

        # Buttons summary (1 line)
        if analysis["buttons"]:
            button_list = ", ".join(f'"{b}"' for b in analysis["buttons"][:5])
            if len(analysis["buttons"]) > 5:
                button_list += f" +{len(analysis['buttons']) - 5} more"
            lines.append(f"Buttons: {button_list}")

        # Text fields summary (1 line)
        if analysis["text_fields"]:
            field_count = len(analysis["text_fields"])
            [f["type"] for f in analysis["text_fields"]]
            filled = sum(1 for f in analysis["text_fields"] if f["has_value"])
            lines.append(f"TextFields: {field_count} ({filled} filled)")

        # Navigation summary (1 line)
        nav_parts = []
        if "nav_title" in analysis["navigation"]:
            nav_parts.append(f"NavBar: \"{analysis['navigation']['nav_title']}\"")
        if "tab_count" in analysis["navigation"]:
            nav_parts.append(f"TabBar: {analysis['navigation']['tab_count']} tabs")
        if nav_parts:
            lines.append(f"Navigation: {', '.join(nav_parts)}")

        # Focusable count (1 line)
        lines.append(f"Focusable: {analysis['focusable']} elements")

        # Verbose mode adds element type breakdown
        if verbose:
            lines.append("\nElements by type:")
            for elem_type, items in analysis["elements_by_type"].items():
                if items:  # Only show types that exist
                    lines.append(f"  {elem_type}: {len(items)}")
                    for item in items[:3]:  # Show first 3
                        lines.append(f"    - {item}")
                    if len(items) > 3:
                        lines.append(f"    ... +{len(items) - 3} more")

        return "\n".join(lines)

    def get_navigation_hints(self, analysis: dict) -> list[str]:
        """Generate navigation hints based on screen analysis."""
        hints = []

        # Check for common patterns
        if "Login" in str(analysis.get("buttons", [])):
            hints.append("Login screen detected - find TextFields for credentials")

        if analysis["text_fields"]:
            unfilled = [f for f in analysis["text_fields"] if not f["has_value"]]
            if unfilled:
                hints.append(f"{len(unfilled)} empty text field(s) - may need input")

        if not analysis["buttons"] and not analysis["text_fields"]:
            hints.append("No interactive elements - try swiping or going back")

        if "tab_count" in analysis.get("navigation", {}):
            hints.append(f"Tab bar available with {analysis['navigation']['tab_count']} tabs")

        return hints


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Map current screen UI elements")
    parser.add_argument("--verbose", action="store_true", help="Show detailed element breakdown")
    parser.add_argument("--json", action="store_true", help="Output raw JSON analysis")
    parser.add_argument("--hints", action="store_true", help="Include navigation hints")
    parser.add_argument(
        "--udid",
        help="Device UDID (auto-detects booted simulator if not provided)",
    )

    args = parser.parse_args()

    # Resolve UDID with auto-detection
    try:
        udid = resolve_udid(args.udid)
    except RuntimeError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Create mapper and analyze
    mapper = ScreenMapper(udid=udid)
    tree = mapper.get_accessibility_tree()
    analysis = mapper.analyze_tree(tree)

    # Output based on format
    if args.json:
        # Full JSON (verbose)
        print(json.dumps(analysis, indent=2, default=str))
    else:
        # Token-efficient summary (default)
        summary = mapper.format_summary(analysis, verbose=args.verbose)
        print(summary)

        # Add hints if requested
        if args.hints:
            hints = mapper.get_navigation_hints(analysis)
            if hints:
                print("\nHints:")
                for hint in hints:
                    print(f"  - {hint}")


if __name__ == "__main__":
    main()
```

## File: `ios-simulator-skill/scripts/sim_health_check.sh`
```bash
#!/usr/bin/env bash
#
# iOS Simulator Testing Environment Health Check
#
# Verifies that all required tools and dependencies are properly installed
# and configured for iOS simulator testing.
#
# Usage: bash scripts/sim_health_check.sh [--help]

set -e

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check flags
SHOW_HELP=false

# Parse arguments
for arg in "$@"; do
    case $arg in
        --help|-h)
            SHOW_HELP=true
            shift
            ;;
    esac
done

if [ "$SHOW_HELP" = true ]; then
    cat <<EOF
iOS Simulator Testing - Environment Health Check

Verifies that your environment is properly configured for iOS simulator testing.

Usage: bash scripts/sim_health_check.sh [options]

Options:
  --help, -h    Show this help message

This script checks for:
  - Xcode Command Line Tools installation
  - iOS Simulator availability
  - IDB (iOS Development Bridge) installation
  - Available simulator devices
  - Python 3 installation (for scripts)

Exit codes:
  0 - All checks passed
  1 - One or more checks failed (see output for details)
EOF
    exit 0
fi

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}  iOS Simulator Testing - Environment Health Check${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

CHECKS_PASSED=0
CHECKS_FAILED=0

# Function to print check status
check_passed() {
    echo -e "${GREEN}✓${NC} $1"
    CHECKS_PASSED=$((CHECKS_PASSED + 1))
}

check_failed() {
    echo -e "${RED}✗${NC} $1"
    CHECKS_FAILED=$((CHECKS_FAILED + 1))
}

check_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

# Check 1: macOS
echo -e "${BLUE}[1/8]${NC} Checking operating system..."
if [[ "$OSTYPE" == "darwin"* ]]; then
    OS_VERSION=$(sw_vers -productVersion)
    check_passed "macOS detected (version $OS_VERSION)"
else
    check_failed "Not running on macOS (detected: $OSTYPE)"
    echo "       iOS Simulator testing requires macOS"
fi
echo ""

# Check 2: Xcode Command Line Tools
echo -e "${BLUE}[2/8]${NC} Checking Xcode Command Line Tools..."
if command -v xcrun &> /dev/null; then
    XCODE_PATH=$(xcode-select -p 2>/dev/null || echo "not found")
    if [ "$XCODE_PATH" != "not found" ]; then
        XCODE_VERSION=$(xcodebuild -version 2>/dev/null | head -n 1 || echo "Unknown")
        check_passed "Xcode Command Line Tools installed"
        echo "       Path: $XCODE_PATH"
        echo "       Version: $XCODE_VERSION"
    else
        check_failed "Xcode Command Line Tools path not set"
        echo "       Run: xcode-select --install"
    fi
else
    check_failed "xcrun command not found"
    echo "       Install Xcode Command Line Tools: xcode-select --install"
fi
echo ""

# Check 3: simctl availability
echo -e "${BLUE}[3/8]${NC} Checking simctl (Simulator Control)..."
if command -v xcrun &> /dev/null && xcrun simctl help &> /dev/null; then
    check_passed "simctl is available"
else
    check_failed "simctl not available"
    echo "       simctl comes with Xcode Command Line Tools"
fi
echo ""

# Check 4: IDB installation
echo -e "${BLUE}[4/8]${NC} Checking IDB (iOS Development Bridge)..."
if command -v idb &> /dev/null; then
    IDB_PATH=$(which idb)
    IDB_VERSION=$(idb --version 2>/dev/null || echo "Unknown")
    check_passed "IDB is installed"
    echo "       Path: $IDB_PATH"
    echo "       Version: $IDB_VERSION"
else
    check_warning "IDB not found in PATH"
    echo "       IDB is optional but provides advanced UI automation"
    echo "       Install: https://fbidb.io/brain/knowledge/docs_legacy/installation"
    echo "       Recommended: brew tap facebook/fb && brew install idb-companion"
fi
echo ""

# Check 5: Python 3 installation
echo -e "${BLUE}[5/8]${NC} Checking Python 3..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    check_passed "Python 3 is installed (version $PYTHON_VERSION)"
else
    check_failed "Python 3 not found"
    echo "       Python 3 is required for testing scripts"
    echo "       Install: brew install python3"
fi
echo ""

# Check 6: Available simulators
echo -e "${BLUE}[6/8]${NC} Checking available iOS Simulators..."
if command -v xcrun &> /dev/null; then
    SIMULATOR_COUNT=$(xcrun simctl list devices available 2>/dev/null | grep -c "iPhone\|iPad" || echo "0")

    if [ "$SIMULATOR_COUNT" -gt 0 ]; then
        check_passed "Found $SIMULATOR_COUNT available simulator(s)"

        # Show first 5 simulators
        echo ""
        echo "       Available simulators (showing up to 5):"
        xcrun simctl list devices available 2>/dev/null | grep "iPhone\|iPad" | head -5 | while read -r line; do
            echo "       - $line"
        done
    else
        check_warning "No simulators found"
        echo "       Create simulators via Xcode or simctl"
        echo "       Example: xcrun simctl create 'iPhone 15' 'iPhone 15'"
    fi
else
    check_failed "Cannot check simulators (simctl not available)"
fi
echo ""

# Check 7: Booted simulators
echo -e "${BLUE}[7/8]${NC} Checking booted simulators..."
if command -v xcrun &> /dev/null; then
    BOOTED_SIMS=$(xcrun simctl list devices booted 2>/dev/null | grep -c "iPhone\|iPad" || echo "0")

    if [ "$BOOTED_SIMS" -gt 0 ]; then
        check_passed "$BOOTED_SIMS simulator(s) currently booted"

        echo ""
        echo "       Booted simulators:"
        xcrun simctl list devices booted 2>/dev/null | grep "iPhone\|iPad" | while read -r line; do
            echo "       - $line"
        done
    else
        check_warning "No simulators currently booted"
        echo "       Boot a simulator to begin testing"
        echo "       Example: xcrun simctl boot <device-udid>"
        echo "       Or: open -a Simulator"
    fi
else
    check_failed "Cannot check booted simulators (simctl not available)"
fi
echo ""

# Check 8: Required Python packages (optional check)
echo -e "${BLUE}[8/8]${NC} Checking Python packages..."
if command -v python3 &> /dev/null; then
    MISSING_PACKAGES=()

    # Check for PIL/Pillow (for visual_diff.py)
    if python3 -c "import PIL" 2>/dev/null; then
        check_passed "Pillow (PIL) installed - visual diff available"
    else
        MISSING_PACKAGES+=("pillow")
        check_warning "Pillow (PIL) not installed - visual diff won't work"
    fi

    if [ ${#MISSING_PACKAGES[@]} -gt 0 ]; then
        echo ""
        echo "       Install missing packages:"
        echo "       pip3 install ${MISSING_PACKAGES[*]}"
    fi
else
    check_warning "Cannot check Python packages (Python 3 not available)"
fi
echo ""

# Summary
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}  Summary${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "Checks passed: ${GREEN}$CHECKS_PASSED${NC}"
if [ "$CHECKS_FAILED" -gt 0 ]; then
    echo -e "Checks failed: ${RED}$CHECKS_FAILED${NC}"
    echo ""
    echo -e "${YELLOW}Action required:${NC} Fix the failed checks above before testing"
    exit 1
else
    echo ""
    echo -e "${GREEN}✓ Environment is ready for iOS simulator testing${NC}"
    echo ""
    echo "Next steps:"
    echo "  1. Boot a simulator: open -a Simulator"
    echo "  2. Launch your app: xcrun simctl launch booted <bundle-id>"
    echo "  3. Run accessibility audit: python scripts/accessibility_audit.py"
    exit 0
fi
```

## File: `ios-simulator-skill/scripts/sim_list.py`
```python
#!/usr/bin/env python3
"""
iOS Simulator Listing with Progressive Disclosure

Lists available simulators with token-efficient summaries.
Full details available on demand via cache IDs.

Achieves 96% token reduction (57k→2k tokens) for common queries.

Usage Examples:
    # Concise summary (default)
    python scripts/sim_list.py

    # Get full details for cached list
    python scripts/sim_list.py --get-details <cache-id>

    # Get recommendations
    python scripts/sim_list.py --suggest

    # Filter by device type
    python scripts/sim_list.py --device-type iPhone

Output (default):
    Simulator Summary [cache-sim-20251028-143052]
    ├─ Total: 47 devices
    ├─ Available: 31
    └─ Booted: 1

    ✓ iPhone 16 Pro (iOS 18.1) [ABC-123...]

    Use --get-details cache-sim-20251028-143052 for full list

Technical Details:
- Uses xcrun simctl list devices
- Caches results with 1-hour TTL
- Reduces output by 96% by default
- Token efficiency: summary = ~30 tokens, full list = ~1500 tokens
"""

import argparse
import json
import subprocess
import sys
from typing import Any

from common import get_cache


class SimulatorLister:
    """Lists iOS simulators with progressive disclosure."""

    def __init__(self):
        """Initialize lister with cache."""
        self.cache = get_cache()

    def list_simulators(self) -> dict:
        """
        Get list of all simulators.

        Returns:
            Dict with structure:
            {
                "devices": [...],
                "runtimes": [...],
                "total_devices": int,
                "available_devices": int,
                "booted_devices": [...]
            }
        """
        try:
            result = subprocess.run(
                ["xcrun", "simctl", "list", "devices", "--json"],
                capture_output=True,
                text=True,
                check=True,
            )

            return json.loads(result.stdout)
        except (subprocess.CalledProcessError, json.JSONDecodeError):
            return {"devices": {}, "runtimes": []}

    def parse_devices(self, sim_data: dict) -> list[dict]:
        """
        Parse simulator data into flat list.

        Returns:
            List of device dicts with runtime info
        """
        devices = []

        devices_by_runtime = sim_data.get("devices", {})

        for runtime_str, device_list in devices_by_runtime.items():
            # Extract iOS version from runtime string
            # Format: "iOS 18.1", "tvOS 18", etc.
            runtime_name = runtime_str.replace(" Simulator", "").strip()

            for device in device_list:
                devices.append(
                    {
                        "name": device.get("name"),
                        "udid": device.get("udid"),
                        "state": device.get("state"),
                        "runtime": runtime_name,
                        "is_available": device.get("isAvailable", False),
                    }
                )

        return devices

    def get_concise_summary(self, devices: list[dict]) -> dict:
        """
        Generate concise summary with cache ID.

        Returns 96% fewer tokens than full list.
        """
        booted = [d for d in devices if d["state"] == "Booted"]
        available = [d for d in devices if d["is_available"]]
        iphone = [d for d in available if "iPhone" in d["name"]]

        # Cache full list for later retrieval
        cache_id = self.cache.save(
            {
                "devices": devices,
                "timestamp": __import__("datetime").datetime.now().isoformat(),
            },
            "simulator-list",
        )

        return {
            "cache_id": cache_id,
            "summary": {
                "total_devices": len(devices),
                "available_devices": len(available),
                "booted_devices": len(booted),
            },
            "quick_access": {
                "booted": booted[:3] if booted else [],
                "recommended_iphone": iphone[:3] if iphone else [],
            },
        }

    def get_full_list(
        self,
        cache_id: str,
        device_type: str | None = None,
        runtime: str | None = None,
    ) -> list[dict] | None:
        """
        Retrieve full simulator list from cache.

        Args:
            cache_id: Cache ID from concise summary
            device_type: Filter by type (iPhone, iPad, etc.)
            runtime: Filter by iOS version

        Returns:
            List of devices matching filters
        """
        data = self.cache.get(cache_id)
        if not data:
            return None

        devices = data.get("devices", [])

        # Apply filters
        if device_type:
            devices = [d for d in devices if device_type in d["name"]]
        if runtime:
            devices = [d for d in devices if runtime.lower() in d["runtime"].lower()]

        return devices

    def suggest_simulators(self, limit: int = 4) -> list[dict]:
        """
        Get simulator recommendations.

        Returns:
            List of recommended simulators (best candidates for building)
        """
        all_sims = self.list_simulators()
        devices = self.parse_devices(all_sims)

        # Score devices for recommendations
        scored = []
        for device in devices:
            score = 0

            # Prefer booted
            if device["state"] == "Booted":
                score += 10
            # Prefer available
            if device["is_available"]:
                score += 5
            # Prefer recent iOS versions
            ios_version = device["runtime"]
            if "18" in ios_version:
                score += 3
            elif "17" in ios_version:
                score += 2
            # Prefer iPhones over other types
            if "iPhone" in device["name"]:
                score += 1

            scored.append({"device": device, "score": score})

        # Sort by score and return top N
        scored.sort(key=lambda x: x["score"], reverse=True)
        return [s["device"] for s in scored[:limit]]


def format_device(device: dict) -> str:
    """Format device for display."""
    state_icon = "✓" if device["state"] == "Booted" else " "
    avail_icon = "●" if device["is_available"] else "○"
    name = device["name"]
    runtime = device["runtime"]
    udid_short = device["udid"][:8] + "..."
    return f"{state_icon} {avail_icon} {name} ({runtime}) [{udid_short}]"


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="List iOS simulators with progressive disclosure")
    parser.add_argument(
        "--get-details",
        metavar="CACHE_ID",
        help="Get full details for cached simulator list",
    )
    parser.add_argument("--suggest", action="store_true", help="Get simulator recommendations")
    parser.add_argument(
        "--device-type",
        help="Filter by device type (iPhone, iPad, Apple Watch, etc.)",
    )
    parser.add_argument("--runtime", help="Filter by iOS version (e.g., iOS-18, iOS-17)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    lister = SimulatorLister()

    # Get full list with details
    if args.get_details:
        devices = lister.get_full_list(
            args.get_details, device_type=args.device_type, runtime=args.runtime
        )

        if devices is None:
            print(f"Error: Cache ID not found or expired: {args.get_details}")
            sys.exit(1)

        if args.json:
            print(json.dumps(devices, indent=2))
        else:
            print(f"Simulators ({len(devices)}):\n")
            for device in devices:
                print(f"  {format_device(device)}")

    # Get recommendations
    elif args.suggest:
        suggestions = lister.suggest_simulators()

        if args.json:
            print(json.dumps(suggestions, indent=2))
        else:
            print("Recommended Simulators:\n")
            for i, device in enumerate(suggestions, 1):
                print(f"{i}. {format_device(device)}")

    # Default: concise summary
    else:
        all_sims = lister.list_simulators()
        devices = lister.parse_devices(all_sims)
        summary = lister.get_concise_summary(devices)

        if args.json:
            print(json.dumps(summary, indent=2))
        else:
            # Human-readable concise output
            cache_id = summary["cache_id"]
            s = summary["summary"]
            q = summary["quick_access"]

            print(f"Simulator Summary [{cache_id}]")
            print(f"├─ Total: {s['total_devices']} devices")
            print(f"├─ Available: {s['available_devices']}")
            print(f"└─ Booted: {s['booted_devices']}")

            if q["booted"]:
                print()
                for device in q["booted"]:
                    print(f"  {format_device(device)}")

            print()
            print(f"Use --get-details {cache_id} for full list")


if __name__ == "__main__":
    main()
```

## File: `ios-simulator-skill/scripts/simctl_boot.py`
```python
#!/usr/bin/env python3
"""
Boot iOS simulators and wait for readiness.

This script boots one or more simulators and optionally waits for them to reach
a ready state. It measures boot time and provides progress feedback.

Key features:
- Boot by UDID or device name
- Wait for device readiness with configurable timeout
- Measure boot performance
- Batch boot operations (boot all, boot by type)
- Progress reporting for CI/CD pipelines
"""

import argparse
import subprocess
import sys
import time

from common.device_utils import (
    get_booted_device_udid,
    list_simulators,
    resolve_device_identifier,
)


class SimulatorBooter:
    """Boot iOS simulators with optional readiness waiting."""

    def __init__(self, udid: str | None = None):
        """Initialize booter with optional device UDID."""
        self.udid = udid

    def boot(self, wait_ready: bool = False, timeout_seconds: int = 120) -> tuple[bool, str]:
        """
        Boot simulator and optionally wait for readiness.

        Args:
            wait_ready: Wait for device to be ready before returning
            timeout_seconds: Maximum seconds to wait for readiness

        Returns:
            (success, message) tuple
        """
        if not self.udid:
            return False, "Error: Device UDID not specified"

        start_time = time.time()

        # Check if already booted
        try:
            booted = get_booted_device_udid()
            if booted == self.udid:
                elapsed = time.time() - start_time
                return True, (f"Device already booted: {self.udid} " f"[checked in {elapsed:.1f}s]")
        except RuntimeError:
            pass  # No booted device, proceed with boot

        # Execute boot command
        try:
            cmd = ["xcrun", "simctl", "boot", self.udid]
            result = subprocess.run(cmd, check=False, capture_output=True, text=True, timeout=30)

            if result.returncode != 0:
                error = result.stderr.strip()
                return False, f"Boot failed: {error}"
        except subprocess.TimeoutExpired:
            return False, "Boot command timed out"
        except Exception as e:
            return False, f"Boot error: {e}"

        # Optionally wait for readiness
        if wait_ready:
            ready, wait_message = self._wait_for_ready(timeout_seconds)
            elapsed = time.time() - start_time
            if ready:
                return True, (f"Device booted and ready: {self.udid} " f"[{elapsed:.1f}s total]")
            return False, wait_message

        elapsed = time.time() - start_time
        return True, (
            f"Device booted: {self.udid} [boot in {elapsed:.1f}s] "
            "(use --wait-ready to wait for availability)"
        )

    def _wait_for_ready(self, timeout_seconds: int = 120) -> tuple[bool, str]:
        """
        Wait for device to reach ready state.

        Args:
            timeout_seconds: Maximum seconds to wait

        Returns:
            (success, message) tuple
        """
        start_time = time.time()
        poll_interval = 0.5
        checks = 0

        while time.time() - start_time < timeout_seconds:
            try:
                checks += 1
                # Check if device responds to simctl commands
                result = subprocess.run(
                    ["xcrun", "simctl", "spawn", self.udid, "launchctl", "list"],
                    check=False,
                    capture_output=True,
                    text=True,
                    timeout=5,
                )

                if result.returncode == 0:
                    elapsed = time.time() - start_time
                    return True, (
                        f"Device ready: {self.udid} " f"[{elapsed:.1f}s, {checks} checks]"
                    )
            except (subprocess.TimeoutExpired, RuntimeError):
                pass  # Not ready yet

            time.sleep(poll_interval)

        elapsed = time.time() - start_time
        return False, (
            f"Boot timeout: Device did not reach ready state "
            f"within {elapsed:.1f}s ({checks} checks)"
        )

    @staticmethod
    def boot_all() -> tuple[int, int]:
        """
        Boot all available simulators.

        Returns:
            (succeeded, failed) tuple with counts
        """
        simulators = list_simulators(state="available")
        succeeded = 0
        failed = 0

        for sim in simulators:
            booter = SimulatorBooter(udid=sim["udid"])
            success, _message = booter.boot(wait_ready=False)
            if success:
                succeeded += 1
            else:
                failed += 1

        return succeeded, failed

    @staticmethod
    def boot_by_type(device_type: str) -> tuple[int, int]:
        """
        Boot all simulators of a specific type.

        Args:
            device_type: Device type filter (e.g., "iPhone", "iPad")

        Returns:
            (succeeded, failed) tuple with counts
        """
        simulators = list_simulators(state="available")
        succeeded = 0
        failed = 0

        for sim in simulators:
            if device_type.lower() in sim["name"].lower():
                booter = SimulatorBooter(udid=sim["udid"])
                success, _message = booter.boot(wait_ready=False)
                if success:
                    succeeded += 1
                else:
                    failed += 1

        return succeeded, failed


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Boot iOS simulators and wait for readiness")
    parser.add_argument(
        "--udid",
        help="Device UDID or name (required unless using --all or --type)",
    )
    parser.add_argument(
        "--name",
        help="Device name (alternative to --udid)",
    )
    parser.add_argument(
        "--wait-ready",
        action="store_true",
        help="Wait for device to reach ready state",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=120,
        help="Timeout for --wait-ready in seconds (default: 120)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Boot all available simulators",
    )
    parser.add_argument(
        "--type",
        help="Boot all simulators of a specific type (e.g., iPhone, iPad)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON",
    )

    args = parser.parse_args()

    # Handle batch operations
    if args.all:
        succeeded, failed = SimulatorBooter.boot_all()
        if args.json:
            import json

            print(
                json.dumps(
                    {
                        "action": "boot_all",
                        "succeeded": succeeded,
                        "failed": failed,
                        "total": succeeded + failed,
                    }
                )
            )
        else:
            total = succeeded + failed
            print(f"Boot summary: {succeeded}/{total} succeeded, " f"{failed} failed")
        sys.exit(0 if failed == 0 else 1)

    if args.type:
        succeeded, failed = SimulatorBooter.boot_by_type(args.type)
        if args.json:
            import json

            print(
                json.dumps(
                    {
                        "action": "boot_by_type",
                        "type": args.type,
                        "succeeded": succeeded,
                        "failed": failed,
                        "total": succeeded + failed,
                    }
                )
            )
        else:
            total = succeeded + failed
            print(f"Boot {args.type} summary: {succeeded}/{total} succeeded, " f"{failed} failed")
        sys.exit(0 if failed == 0 else 1)

    # Resolve device identifier
    device_id = args.udid or args.name
    if not device_id:
        print("Error: Specify --udid, --name, --all, or --type", file=sys.stderr)
        sys.exit(1)

    try:
        udid = resolve_device_identifier(device_id)
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Boot device
    booter = SimulatorBooter(udid=udid)
    success, message = booter.boot(wait_ready=args.wait_ready, timeout_seconds=args.timeout)

    if args.json:
        import json

        print(
            json.dumps(
                {
                    "action": "boot",
                    "device_id": device_id,
                    "udid": udid,
                    "success": success,
                    "message": message,
                }
            )
        )
    else:
        print(message)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
```

## File: `ios-simulator-skill/scripts/simctl_create.py`
```python
#!/usr/bin/env python3
"""
Create iOS simulators dynamically.

This script creates new simulators with specified device type and iOS version.
Useful for CI/CD pipelines that need on-demand test device provisioning.

Key features:
- Create by device type (iPhone 16 Pro, iPad Air, etc.)
- Specify iOS version (17.0, 18.0, etc.)
- Custom device naming
- Return newly created device UDID
- List available device types and runtimes
"""

import argparse
import subprocess
import sys
from typing import Optional

from common.device_utils import list_simulators


class SimulatorCreator:
    """Create iOS simulators with specified configurations."""

    def __init__(self):
        """Initialize simulator creator."""
        pass

    def create(
        self,
        device_type: str,
        ios_version: str | None = None,
        custom_name: str | None = None,
    ) -> tuple[bool, str, str | None]:
        """
        Create new iOS simulator.

        Args:
            device_type: Device type (e.g., "iPhone 16 Pro", "iPad Air")
            ios_version: iOS version (e.g., "18.0"). If None, uses latest.
            custom_name: Custom device name. If None, uses default.

        Returns:
            (success, message, new_udid) tuple
        """
        # Get available device types and runtimes
        available_types = self._get_device_types()
        if not available_types:
            return False, "Failed to get available device types", None

        # Normalize device type
        device_type_id = None
        for dt in available_types:
            if device_type.lower() in dt["name"].lower():
                device_type_id = dt["identifier"]
                break

        if not device_type_id:
            return (
                False,
                f"Device type '{device_type}' not found. "
                f"Use --list-devices for available types.",
                None,
            )

        # Get available runtimes
        available_runtimes = self._get_runtimes()
        if not available_runtimes:
            return False, "Failed to get available runtimes", None

        # Resolve iOS version
        runtime_id = None
        if ios_version:
            for rt in available_runtimes:
                if ios_version in rt["name"]:
                    runtime_id = rt["identifier"]
                    break

            if not runtime_id:
                return (
                    False,
                    f"iOS version '{ios_version}' not found. "
                    f"Use --list-runtimes for available versions.",
                    None,
                )
        # Use latest runtime
        elif available_runtimes:
            runtime_id = available_runtimes[-1]["identifier"]

        if not runtime_id:
            return False, "No iOS runtime available", None

        # Create device
        try:
            # Build device name
            device_name = (
                custom_name or f"{device_type_id.split('.')[-1]}-{ios_version or 'latest'}"
            )

            cmd = [
                "xcrun",
                "simctl",
                "create",
                device_name,
                device_type_id,
                runtime_id,
            ]

            result = subprocess.run(cmd, check=False, capture_output=True, text=True, timeout=60)

            if result.returncode != 0:
                error = result.stderr.strip() or result.stdout.strip()
                return False, f"Creation failed: {error}", None

            # Extract UDID from output
            new_udid = result.stdout.strip()

            return (
                True,
                f"Device created: {device_name} ({device_type}) iOS {ios_version or 'latest'} "
                f"UDID: {new_udid}",
                new_udid,
            )

        except subprocess.TimeoutExpired:
            return False, "Creation command timed out", None
        except Exception as e:
            return False, f"Creation error: {e}", None

    @staticmethod
    def _get_device_types() -> list[dict]:
        """
        Get available device types.

        Returns:
            List of device type dicts with "name" and "identifier" keys
        """
        try:
            cmd = ["xcrun", "simctl", "list", "devicetypes", "-j"]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)

            import json

            data = json.loads(result.stdout)
            devices = []

            for device in data.get("devicetypes", []):
                devices.append(
                    {
                        "name": device.get("name", ""),
                        "identifier": device.get("identifier", ""),
                    }
                )

            return devices
        except Exception:
            return []

    @staticmethod
    def _get_runtimes() -> list[dict]:
        """
        Get available iOS runtimes.

        Returns:
            List of runtime dicts with "name" and "identifier" keys
        """
        try:
            cmd = ["xcrun", "simctl", "list", "runtimes", "-j"]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)

            import json

            data = json.loads(result.stdout)
            runtimes = []

            for runtime in data.get("runtimes", []):
                # Only include iOS runtimes (skip watchOS, tvOS, etc.)
                identifier = runtime.get("identifier", "")
                if "iOS" in identifier or "iOS" in runtime.get("name", ""):
                    runtimes.append(
                        {
                            "name": runtime.get("name", ""),
                            "identifier": runtime.get("identifier", ""),
                        }
                    )

            # Sort by version number (latest first)
            runtimes.sort(key=lambda r: r.get("identifier", ""), reverse=True)

            return runtimes
        except Exception:
            return []

    @staticmethod
    def list_device_types() -> list[dict]:
        """
        List all available device types.

        Returns:
            List of device types with name and identifier
        """
        return SimulatorCreator._get_device_types()

    @staticmethod
    def list_runtimes() -> list[dict]:
        """
        List all available iOS runtimes.

        Returns:
            List of runtimes with name and identifier
        """
        return SimulatorCreator._get_runtimes()


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Create iOS simulators dynamically")
    parser.add_argument(
        "--device",
        required=False,
        help="Device type (e.g., 'iPhone 16 Pro', 'iPad Air')",
    )
    parser.add_argument(
        "--runtime",
        help="iOS version (e.g., '18.0', '17.0'). Defaults to latest.",
    )
    parser.add_argument(
        "--name",
        help="Custom device name. Defaults to auto-generated.",
    )
    parser.add_argument(
        "--list-devices",
        action="store_true",
        help="List all available device types",
    )
    parser.add_argument(
        "--list-runtimes",
        action="store_true",
        help="List all available iOS runtimes",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON",
    )

    args = parser.parse_args()

    creator = SimulatorCreator()

    # Handle info queries
    if args.list_devices:
        devices = creator.list_device_types()
        if args.json:
            import json

            print(json.dumps({"devices": devices}))
        else:
            print(f"Available device types ({len(devices)}):")
            for dev in devices[:20]:  # Show first 20
                print(f"  - {dev['name']}")
            if len(devices) > 20:
                print(f"  ... and {len(devices) - 20} more")
        sys.exit(0)

    if args.list_runtimes:
        runtimes = creator.list_runtimes()
        if args.json:
            import json

            print(json.dumps({"runtimes": runtimes}))
        else:
            print(f"Available iOS runtimes ({len(runtimes)}):")
            for rt in runtimes:
                print(f"  - {rt['name']}")
        sys.exit(0)

    # Create device
    if not args.device:
        print(
            "Error: Specify --device, --list-devices, or --list-runtimes",
            file=sys.stderr,
        )
        sys.exit(1)

    success, message, new_udid = creator.create(
        device_type=args.device,
        ios_version=args.runtime,
        custom_name=args.name,
    )

    if args.json:
        import json

        print(
            json.dumps(
                {
                    "action": "create",
                    "device_type": args.device,
                    "runtime": args.runtime,
                    "success": success,
                    "message": message,
                    "new_udid": new_udid,
                }
            )
        )
    else:
        print(message)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
```

## File: `ios-simulator-skill/scripts/simctl_delete.py`
```python
#!/usr/bin/env python3
"""
Delete iOS simulators permanently.

This script permanently removes simulators and frees disk space.
Includes safety confirmation to prevent accidental deletion.

Key features:
- Delete by UDID or device name
- Confirmation required for safety
- Batch delete operations
- Report freed disk space estimate
"""

import argparse
import subprocess
import sys
from typing import Optional

from common.device_utils import (
    list_simulators,
    resolve_device_identifier,
)


class SimulatorDeleter:
    """Delete iOS simulators with safety confirmation."""

    def __init__(self, udid: str | None = None):
        """Initialize with optional device UDID."""
        self.udid = udid

    def delete(self, confirm: bool = False) -> tuple[bool, str]:
        """
        Delete simulator permanently.

        Args:
            confirm: Skip confirmation prompt (for batch operations)

        Returns:
            (success, message) tuple
        """
        if not self.udid:
            return False, "Error: Device UDID not specified"

        # Safety confirmation
        if not confirm:
            try:
                response = input(
                    f"Permanently delete simulator {self.udid}? " f"(type 'yes' to confirm): "
                )
                if response.lower() != "yes":
                    return False, "Deletion cancelled by user"
            except KeyboardInterrupt:
                return False, "Deletion cancelled"

        # Execute delete command
        try:
            cmd = ["xcrun", "simctl", "delete", self.udid]
            result = subprocess.run(cmd, check=False, capture_output=True, text=True, timeout=60)

            if result.returncode != 0:
                error = result.stderr.strip() or result.stdout.strip()
                return False, f"Deletion failed: {error}"

            return True, f"Device deleted: {self.udid} [disk space freed]"

        except subprocess.TimeoutExpired:
            return False, "Deletion command timed out"
        except Exception as e:
            return False, f"Deletion error: {e}"

    @staticmethod
    def delete_all(confirm: bool = False) -> tuple[int, int]:
        """
        Delete all simulators permanently.

        Args:
            confirm: Skip confirmation prompt

        Returns:
            (succeeded, failed) tuple with counts
        """
        simulators = list_simulators(state=None)

        if not confirm:
            count = len(simulators)
            try:
                response = input(
                    f"Permanently delete ALL {count} simulators? " f"(type 'yes' to confirm): "
                )
                if response.lower() != "yes":
                    return 0, count
            except KeyboardInterrupt:
                return 0, count

        succeeded = 0
        failed = 0

        for sim in simulators:
            deleter = SimulatorDeleter(udid=sim["udid"])
            success, _message = deleter.delete(confirm=True)
            if success:
                succeeded += 1
            else:
                failed += 1

        return succeeded, failed

    @staticmethod
    def delete_by_type(device_type: str, confirm: bool = False) -> tuple[int, int]:
        """
        Delete all simulators of a specific type.

        Args:
            device_type: Device type filter (e.g., "iPhone", "iPad")
            confirm: Skip confirmation prompt

        Returns:
            (succeeded, failed) tuple with counts
        """
        simulators = list_simulators(state=None)
        matching = [s for s in simulators if device_type.lower() in s["name"].lower()]

        if not matching:
            return 0, 0

        if not confirm:
            count = len(matching)
            try:
                response = input(
                    f"Permanently delete {count} {device_type} simulators? "
                    f"(type 'yes' to confirm): "
                )
                if response.lower() != "yes":
                    return 0, count
            except KeyboardInterrupt:
                return 0, count

        succeeded = 0
        failed = 0

        for sim in matching:
            deleter = SimulatorDeleter(udid=sim["udid"])
            success, _message = deleter.delete(confirm=True)
            if success:
                succeeded += 1
            else:
                failed += 1

        return succeeded, failed

    @staticmethod
    def delete_old(keep_count: int = 3, confirm: bool = False) -> tuple[int, int]:
        """
        Delete older simulators, keeping most recent versions.

        Useful for cleanup after testing multiple iOS versions.
        Keeps the most recent N simulators of each type.

        Args:
            keep_count: Number of recent simulators to keep per type (default: 3)
            confirm: Skip confirmation prompt

        Returns:
            (succeeded, failed) tuple with counts
        """
        simulators = list_simulators(state=None)

        # Group by device type
        by_type: dict[str, list] = {}
        for sim in simulators:
            dev_type = sim["type"]
            if dev_type not in by_type:
                by_type[dev_type] = []
            by_type[dev_type].append(sim)

        # Find candidates for deletion (older ones)
        to_delete = []
        for _dev_type, sims in by_type.items():
            # Sort by runtime (iOS version) - keep newest
            sorted_sims = sorted(sims, key=lambda s: s["runtime"], reverse=True)
            # Mark older ones for deletion
            to_delete.extend(sorted_sims[keep_count:])

        if not to_delete:
            return 0, 0

        if not confirm:
            count = len(to_delete)
            try:
                response = input(
                    f"Delete {count} older simulators, keeping {keep_count} per type? "
                    f"(type 'yes' to confirm): "
                )
                if response.lower() != "yes":
                    return 0, count
            except KeyboardInterrupt:
                return 0, count

        succeeded = 0
        failed = 0

        for sim in to_delete:
            deleter = SimulatorDeleter(udid=sim["udid"])
            success, _message = deleter.delete(confirm=True)
            if success:
                succeeded += 1
            else:
                failed += 1

        return succeeded, failed


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Delete iOS simulators permanently")
    parser.add_argument(
        "--udid",
        help="Device UDID or name (required unless using batch options)",
    )
    parser.add_argument(
        "--name",
        help="Device name (alternative to --udid)",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Skip confirmation prompt",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Delete all simulators",
    )
    parser.add_argument(
        "--type",
        help="Delete all simulators of a specific type (e.g., iPhone)",
    )
    parser.add_argument(
        "--old",
        type=int,
        metavar="KEEP_COUNT",
        help="Delete older simulators, keeping this many per type (e.g., --old 3)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON",
    )

    args = parser.parse_args()

    # Handle batch operations
    if args.all:
        succeeded, failed = SimulatorDeleter.delete_all(confirm=args.yes)
        if args.json:
            import json

            print(
                json.dumps(
                    {
                        "action": "delete_all",
                        "succeeded": succeeded,
                        "failed": failed,
                        "total": succeeded + failed,
                    }
                )
            )
        else:
            total = succeeded + failed
            print(f"Delete summary: {succeeded}/{total} succeeded, " f"{failed} failed")
        sys.exit(0 if failed == 0 else 1)

    if args.type:
        succeeded, failed = SimulatorDeleter.delete_by_type(args.type, confirm=args.yes)
        if args.json:
            import json

            print(
                json.dumps(
                    {
                        "action": "delete_by_type",
                        "type": args.type,
                        "succeeded": succeeded,
                        "failed": failed,
                        "total": succeeded + failed,
                    }
                )
            )
        else:
            total = succeeded + failed
            print(f"Delete {args.type} summary: {succeeded}/{total} succeeded, " f"{failed} failed")
        sys.exit(0 if failed == 0 else 1)

    if args.old is not None:
        succeeded, failed = SimulatorDeleter.delete_old(keep_count=args.old, confirm=args.yes)
        if args.json:
            import json

            print(
                json.dumps(
                    {
                        "action": "delete_old",
                        "keep_count": args.old,
                        "succeeded": succeeded,
                        "failed": failed,
                        "total": succeeded + failed,
                    }
                )
            )
        else:
            total = succeeded + failed
            print(
                f"Delete old summary: {succeeded}/{total} succeeded, "
                f"{failed} failed (kept {args.old} per type)"
            )
        sys.exit(0 if failed == 0 else 1)

    # Delete single device
    device_id = args.udid or args.name
    if not device_id:
        print("Error: Specify --udid, --name, --all, --type, or --old", file=sys.stderr)
        sys.exit(1)

    try:
        udid = resolve_device_identifier(device_id)
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Delete device
    deleter = SimulatorDeleter(udid=udid)
    success, message = deleter.delete(confirm=args.yes)

    if args.json:
        import json

        print(
            json.dumps(
                {
                    "action": "delete",
                    "device_id": device_id,
                    "udid": udid,
                    "success": success,
                    "message": message,
                }
            )
        )
    else:
        print(message)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
```

## File: `ios-simulator-skill/scripts/simctl_erase.py`
```python
#!/usr/bin/env python3
"""
Erase iOS simulators (factory reset).

This script performs a factory reset on simulators, returning them to
a clean state while preserving the device UUID. Much faster than
delete + create for CI/CD cleanup.

Key features:
- Erase by UDID or device name
- Preserve device UUID (faster than delete)
- Verify erase completion
- Batch erase operations (all, by type)
"""

import argparse
import subprocess
import sys
import time
from typing import Optional

from common.device_utils import (
    list_simulators,
    resolve_device_identifier,
)


class SimulatorEraser:
    """Erase iOS simulators with optional verification."""

    def __init__(self, udid: str | None = None):
        """Initialize with optional device UDID."""
        self.udid = udid

    def erase(self, verify: bool = True, timeout_seconds: int = 30) -> tuple[bool, str]:
        """
        Erase simulator and optionally verify completion.

        Performs a factory reset, clearing all app data and settings
        while preserving the simulator UUID.

        Args:
            verify: Wait for erase to complete and verify state
            timeout_seconds: Maximum seconds to wait for verification

        Returns:
            (success, message) tuple
        """
        if not self.udid:
            return False, "Error: Device UDID not specified"

        start_time = time.time()

        # Execute erase command
        try:
            cmd = ["xcrun", "simctl", "erase", self.udid]
            result = subprocess.run(cmd, check=False, capture_output=True, text=True, timeout=60)

            if result.returncode != 0:
                error = result.stderr.strip()
                return False, f"Erase failed: {error}"
        except subprocess.TimeoutExpired:
            return False, "Erase command timed out"
        except Exception as e:
            return False, f"Erase error: {e}"

        # Optionally verify erase completion
        if verify:
            ready, verify_message = self._verify_erase(timeout_seconds)
            elapsed = time.time() - start_time
            if ready:
                return True, (
                    f"Device erased: {self.udid} " f"[factory reset complete, {elapsed:.1f}s]"
                )
            return False, verify_message

        elapsed = time.time() - start_time
        return True, (
            f"Device erase initiated: {self.udid} [{elapsed:.1f}s] "
            "(use --verify to wait for completion)"
        )

    def _verify_erase(self, timeout_seconds: int = 30) -> tuple[bool, str]:
        """
        Verify erase has completed.

        Polls device state to confirm erase finished successfully.

        Args:
            timeout_seconds: Maximum seconds to wait

        Returns:
            (success, message) tuple
        """
        start_time = time.time()
        poll_interval = 0.5
        checks = 0

        while time.time() - start_time < timeout_seconds:
            try:
                checks += 1
                # Check if device can be queried (indicates boot status)
                result = subprocess.run(
                    ["xcrun", "simctl", "spawn", self.udid, "launchctl", "list"],
                    check=False,
                    capture_output=True,
                    text=True,
                    timeout=5,
                )

                # Device responding = erase likely complete
                if result.returncode == 0:
                    elapsed = time.time() - start_time
                    return True, (
                        f"Erase verified: {self.udid} " f"[{elapsed:.1f}s, {checks} checks]"
                    )
            except (subprocess.TimeoutExpired, RuntimeError):
                pass  # Not ready yet, keep polling

            time.sleep(poll_interval)

        elapsed = time.time() - start_time
        return False, (
            f"Erase verification timeout: Device did not respond "
            f"within {elapsed:.1f}s ({checks} checks)"
        )

    @staticmethod
    def erase_all() -> tuple[int, int]:
        """
        Erase all simulators (factory reset).

        Returns:
            (succeeded, failed) tuple with counts
        """
        simulators = list_simulators(state=None)
        succeeded = 0
        failed = 0

        for sim in simulators:
            eraser = SimulatorEraser(udid=sim["udid"])
            success, _message = eraser.erase(verify=False)
            if success:
                succeeded += 1
            else:
                failed += 1

        return succeeded, failed

    @staticmethod
    def erase_by_type(device_type: str) -> tuple[int, int]:
        """
        Erase all simulators of a specific type.

        Args:
            device_type: Device type filter (e.g., "iPhone", "iPad")

        Returns:
            (succeeded, failed) tuple with counts
        """
        simulators = list_simulators(state=None)
        succeeded = 0
        failed = 0

        for sim in simulators:
            if device_type.lower() in sim["name"].lower():
                eraser = SimulatorEraser(udid=sim["udid"])
                success, _message = eraser.erase(verify=False)
                if success:
                    succeeded += 1
                else:
                    failed += 1

        return succeeded, failed

    @staticmethod
    def erase_booted() -> tuple[int, int]:
        """
        Erase all currently booted simulators.

        Returns:
            (succeeded, failed) tuple with counts
        """
        simulators = list_simulators(state="booted")
        succeeded = 0
        failed = 0

        for sim in simulators:
            eraser = SimulatorEraser(udid=sim["udid"])
            success, _message = eraser.erase(verify=False)
            if success:
                succeeded += 1
            else:
                failed += 1

        return succeeded, failed


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Erase iOS simulators (factory reset)")
    parser.add_argument(
        "--udid",
        help="Device UDID or name (required unless using --all, --type, or --booted)",
    )
    parser.add_argument(
        "--name",
        help="Device name (alternative to --udid)",
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        help="Wait for erase to complete and verify state",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=30,
        help="Timeout for --verify in seconds (default: 30)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Erase all simulators (factory reset)",
    )
    parser.add_argument(
        "--type",
        help="Erase all simulators of a specific type (e.g., iPhone)",
    )
    parser.add_argument(
        "--booted",
        action="store_true",
        help="Erase all currently booted simulators",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON",
    )

    args = parser.parse_args()

    # Handle batch operations
    if args.all:
        succeeded, failed = SimulatorEraser.erase_all()
        if args.json:
            import json

            print(
                json.dumps(
                    {
                        "action": "erase_all",
                        "succeeded": succeeded,
                        "failed": failed,
                        "total": succeeded + failed,
                    }
                )
            )
        else:
            total = succeeded + failed
            print(f"Erase summary: {succeeded}/{total} succeeded, " f"{failed} failed")
        sys.exit(0 if failed == 0 else 1)

    if args.type:
        succeeded, failed = SimulatorEraser.erase_by_type(args.type)
        if args.json:
            import json

            print(
                json.dumps(
                    {
                        "action": "erase_by_type",
                        "type": args.type,
                        "succeeded": succeeded,
                        "failed": failed,
                        "total": succeeded + failed,
                    }
                )
            )
        else:
            total = succeeded + failed
            print(f"Erase {args.type} summary: {succeeded}/{total} succeeded, " f"{failed} failed")
        sys.exit(0 if failed == 0 else 1)

    if args.booted:
        succeeded, failed = SimulatorEraser.erase_booted()
        if args.json:
            import json

            print(
                json.dumps(
                    {
                        "action": "erase_booted",
                        "succeeded": succeeded,
                        "failed": failed,
                        "total": succeeded + failed,
                    }
                )
            )
        else:
            total = succeeded + failed
            print(f"Erase booted summary: {succeeded}/{total} succeeded, " f"{failed} failed")
        sys.exit(0 if failed == 0 else 1)

    # Erase single device
    device_id = args.udid or args.name
    if not device_id:
        print("Error: Specify --udid, --name, --all, --type, or --booted", file=sys.stderr)
        sys.exit(1)

    try:
        udid = resolve_device_identifier(device_id)
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Erase device
    eraser = SimulatorEraser(udid=udid)
    success, message = eraser.erase(verify=args.verify, timeout_seconds=args.timeout)

    if args.json:
        import json

        print(
            json.dumps(
                {
                    "action": "erase",
                    "device_id": device_id,
                    "udid": udid,
                    "success": success,
                    "message": message,
                }
            )
        )
    else:
        print(message)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
```

## File: `ios-simulator-skill/scripts/simctl_shutdown.py`
```python
#!/usr/bin/env python3
"""
Shutdown iOS simulators with optional state verification.

This script shuts down one or more running simulators and optionally
verifies completion. Supports batch operations for efficient cleanup.

Key features:
- Shutdown by UDID or device name
- Verify shutdown completion with timeout
- Batch shutdown operations (all, by type)
- Progress reporting for CI/CD pipelines
"""

import argparse
import subprocess
import sys
import time
from typing import Optional

from common.device_utils import (
    list_simulators,
    resolve_device_identifier,
)


class SimulatorShutdown:
    """Shutdown iOS simulators with optional verification."""

    def __init__(self, udid: str | None = None):
        """Initialize with optional device UDID."""
        self.udid = udid

    def shutdown(self, verify: bool = True, timeout_seconds: int = 30) -> tuple[bool, str]:
        """
        Shutdown simulator and optionally verify completion.

        Args:
            verify: Wait for shutdown to complete
            timeout_seconds: Maximum seconds to wait for shutdown

        Returns:
            (success, message) tuple
        """
        if not self.udid:
            return False, "Error: Device UDID not specified"

        start_time = time.time()

        # Check if already shutdown
        simulators = list_simulators(state="booted")
        if not any(s["udid"] == self.udid for s in simulators):
            elapsed = time.time() - start_time
            return True, (f"Device already shutdown: {self.udid} " f"[checked in {elapsed:.1f}s]")

        # Execute shutdown command
        try:
            cmd = ["xcrun", "simctl", "shutdown", self.udid]
            result = subprocess.run(cmd, check=False, capture_output=True, text=True, timeout=30)

            if result.returncode != 0:
                error = result.stderr.strip()
                return False, f"Shutdown failed: {error}"
        except subprocess.TimeoutExpired:
            return False, "Shutdown command timed out"
        except Exception as e:
            return False, f"Shutdown error: {e}"

        # Optionally verify shutdown
        if verify:
            ready, verify_message = self._verify_shutdown(timeout_seconds)
            elapsed = time.time() - start_time
            if ready:
                return True, (f"Device shutdown confirmed: {self.udid} " f"[{elapsed:.1f}s total]")
            return False, verify_message

        elapsed = time.time() - start_time
        return True, (
            f"Device shutdown: {self.udid} [{elapsed:.1f}s] "
            "(use --verify to wait for confirmation)"
        )

    def _verify_shutdown(self, timeout_seconds: int = 30) -> tuple[bool, str]:
        """
        Verify device has fully shutdown.

        Args:
            timeout_seconds: Maximum seconds to wait

        Returns:
            (success, message) tuple
        """
        start_time = time.time()
        poll_interval = 0.5
        checks = 0

        while time.time() - start_time < timeout_seconds:
            try:
                checks += 1
                # Check booted devices
                simulators = list_simulators(state="booted")
                if not any(s["udid"] == self.udid for s in simulators):
                    elapsed = time.time() - start_time
                    return True, (
                        f"Device shutdown verified: {self.udid} "
                        f"[{elapsed:.1f}s, {checks} checks]"
                    )
            except RuntimeError:
                pass  # Error checking, retry

            time.sleep(poll_interval)

        elapsed = time.time() - start_time
        return False, (
            f"Shutdown verification timeout: Device did not fully shutdown "
            f"within {elapsed:.1f}s ({checks} checks)"
        )

    @staticmethod
    def shutdown_all() -> tuple[int, int]:
        """
        Shutdown all booted simulators.

        Returns:
            (succeeded, failed) tuple with counts
        """
        simulators = list_simulators(state="booted")
        succeeded = 0
        failed = 0

        for sim in simulators:
            shutdown = SimulatorShutdown(udid=sim["udid"])
            success, _message = shutdown.shutdown(verify=False)
            if success:
                succeeded += 1
            else:
                failed += 1

        return succeeded, failed

    @staticmethod
    def shutdown_by_type(device_type: str) -> tuple[int, int]:
        """
        Shutdown all booted simulators of a specific type.

        Args:
            device_type: Device type filter (e.g., "iPhone", "iPad")

        Returns:
            (succeeded, failed) tuple with counts
        """
        simulators = list_simulators(state="booted")
        succeeded = 0
        failed = 0

        for sim in simulators:
            if device_type.lower() in sim["name"].lower():
                shutdown = SimulatorShutdown(udid=sim["udid"])
                success, _message = shutdown.shutdown(verify=False)
                if success:
                    succeeded += 1
                else:
                    failed += 1

        return succeeded, failed


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Shutdown iOS simulators with optional verification"
    )
    parser.add_argument(
        "--udid",
        help="Device UDID or name (required unless using --all or --type)",
    )
    parser.add_argument(
        "--name",
        help="Device name (alternative to --udid)",
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        help="Wait for shutdown to complete and verify state",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=30,
        help="Timeout for --verify in seconds (default: 30)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Shutdown all booted simulators",
    )
    parser.add_argument(
        "--type",
        help="Shutdown all booted simulators of a specific type (e.g., iPhone)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON",
    )

    args = parser.parse_args()

    # Handle batch operations
    if args.all:
        succeeded, failed = SimulatorShutdown.shutdown_all()
        if args.json:
            import json

            print(
                json.dumps(
                    {
                        "action": "shutdown_all",
                        "succeeded": succeeded,
                        "failed": failed,
                        "total": succeeded + failed,
                    }
                )
            )
        else:
            total = succeeded + failed
            print(f"Shutdown summary: {succeeded}/{total} succeeded, " f"{failed} failed")
        sys.exit(0 if failed == 0 else 1)

    if args.type:
        succeeded, failed = SimulatorShutdown.shutdown_by_type(args.type)
        if args.json:
            import json

            print(
                json.dumps(
                    {
                        "action": "shutdown_by_type",
                        "type": args.type,
                        "succeeded": succeeded,
                        "failed": failed,
                        "total": succeeded + failed,
                    }
                )
            )
        else:
            total = succeeded + failed
            print(
                f"Shutdown {args.type} summary: {succeeded}/{total} succeeded, " f"{failed} failed"
            )
        sys.exit(0 if failed == 0 else 1)

    # Resolve device identifier
    device_id = args.udid or args.name
    if not device_id:
        print("Error: Specify --udid, --name, --all, or --type", file=sys.stderr)
        sys.exit(1)

    try:
        udid = resolve_device_identifier(device_id)
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Shutdown device
    shutdown = SimulatorShutdown(udid=udid)
    success, message = shutdown.shutdown(verify=args.verify, timeout_seconds=args.timeout)

    if args.json:
        import json

        print(
            json.dumps(
                {
                    "action": "shutdown",
                    "device_id": device_id,
                    "udid": udid,
                    "success": success,
                    "message": message,
                }
            )
        )
    else:
        print(message)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
```

## File: `ios-simulator-skill/scripts/simulator_selector.py`
```python
#!/usr/bin/env python3
"""
Intelligent Simulator Selector

Suggests the best available iOS simulators based on:
- Recently used (from config)
- Latest iOS version
- Common models for testing
- Boot status

Usage Examples:
    # Get suggestions for user selection
    python scripts/simulator_selector.py --suggest

    # List all available simulators
    python scripts/simulator_selector.py --list

    # Boot a specific simulator
    python scripts/simulator_selector.py --boot "67A99DF0-27BD-4507-A3DE-B7D8C38F764A"

    # Get suggestions as JSON for programmatic use
    python scripts/simulator_selector.py --suggest --json
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

# Try to import config from build_and_test if available
try:
    from xcode.config import Config
except ImportError:
    Config = None


class SimulatorInfo:
    """Information about an iOS simulator."""

    def __init__(
        self,
        name: str,
        udid: str,
        ios_version: str,
        status: str,
    ):
        """Initialize simulator info."""
        self.name = name
        self.udid = udid
        self.ios_version = ios_version
        self.status = status
        self.reasons: list[str] = []

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "device": self.name,
            "udid": self.udid,
            "ios": self.ios_version,
            "status": self.status,
            "reasons": self.reasons,
        }


class SimulatorSelector:
    """Intelligent simulator selection."""

    # Common iPhone models ranked by testing priority
    COMMON_MODELS = [
        "iPhone 16 Pro",
        "iPhone 16",
        "iPhone 15 Pro",
        "iPhone 15",
        "iPhone SE (3rd generation)",
    ]

    def __init__(self):
        """Initialize selector."""
        self.simulators: list[SimulatorInfo] = []
        self.config: dict | None = None
        self.last_used_simulator: str | None = None

        # Load config if available
        if Config:
            try:
                config = Config.load()
                self.last_used_simulator = config.get_preferred_simulator()
            except Exception:
                pass

    def list_simulators(self) -> list[SimulatorInfo]:
        """
        List all available simulators.

        Returns:
            List of SimulatorInfo objects
        """
        try:
            result = subprocess.run(
                ["xcrun", "simctl", "list", "devices", "--json"],
                capture_output=True,
                text=True,
                check=True,
            )

            data = json.loads(result.stdout)
            simulators = []

            # Parse devices by iOS version
            for runtime, devices in data.get("devices", {}).items():
                # Extract iOS version from runtime (e.g., "com.apple.CoreSimulator.SimRuntime.iOS-18-0")
                ios_version_match = re.search(r"iOS-(\d+-\d+)", runtime)
                if not ios_version_match:
                    continue

                ios_version = ios_version_match.group(1).replace("-", ".")

                for device in devices:
                    name = device.get("name", "")
                    udid = device.get("udid", "")
                    is_available = device.get("isAvailable", False)

                    if not is_available or "iPhone" not in name:
                        continue

                    status = device.get("state", "").capitalize()
                    sim_info = SimulatorInfo(name, udid, ios_version, status)
                    simulators.append(sim_info)

            self.simulators = simulators
            return simulators

        except subprocess.CalledProcessError as e:
            print(f"Error listing simulators: {e.stderr}", file=sys.stderr)
            return []
        except json.JSONDecodeError as e:
            print(f"Error parsing simulator list: {e}", file=sys.stderr)
            return []

    def get_suggestions(self, count: int = 4) -> list[SimulatorInfo]:
        """
        Get top N suggested simulators.

        Ranking factors:
        1. Recently used (from config)
        2. Latest iOS version
        3. Common models
        4. Boot status (Booted preferred)

        Args:
            count: Number of suggestions to return

        Returns:
            List of suggested SimulatorInfo objects
        """
        if not self.simulators:
            return []

        # Score each simulator
        scored = []
        for sim in self.simulators:
            score = self._score_simulator(sim)
            scored.append((score, sim))

        # Sort by score (descending)
        scored.sort(key=lambda x: x[0], reverse=True)

        # Return top N
        suggestions = [sim for _, sim in scored[:count]]

        # Add reasons to each suggestion
        for i, sim in enumerate(suggestions, 1):
            if i == 1:
                sim.reasons.append("Recommended")

            # Check if recently used
            if self.last_used_simulator and self.last_used_simulator == sim.name:
                sim.reasons.append("Recently used")

            # Check if latest iOS
            latest_ios = max(s.ios_version for s in self.simulators)
            if sim.ios_version == latest_ios:
                sim.reasons.append("Latest iOS")

            # Check if common model
            for j, model in enumerate(self.COMMON_MODELS):
                if model in sim.name:
                    sim.reasons.append(f"#{j+1} common model")
                    break

            # Check if booted
            if sim.status == "Booted":
                sim.reasons.append("Currently running")

        return suggestions

    def _score_simulator(self, sim: SimulatorInfo) -> float:
        """
        Score a simulator for ranking.

        Higher score = better recommendation.

        Args:
            sim: Simulator to score

        Returns:
            Score value
        """
        score = 0.0

        # Recently used gets highest priority (100 points)
        if self.last_used_simulator and self.last_used_simulator == sim.name:
            score += 100

        # Latest iOS version (50 points)
        latest_ios = max(s.ios_version for s in self.simulators)
        if sim.ios_version == latest_ios:
            score += 50

        # Common models (30-20 points based on ranking)
        for i, model in enumerate(self.COMMON_MODELS):
            if model in sim.name:
                score += 30 - (i * 2)  # Higher ranking models get more points
                break

        # Currently booted (10 points)
        if sim.status == "Booted":
            score += 10

        # iOS version number (minor factor for breaking ties)
        ios_numeric = float(sim.ios_version.replace(".", ""))
        score += ios_numeric * 0.1

        return score

    def boot_simulator(self, udid: str) -> bool:
        """
        Boot a simulator.

        Args:
            udid: Simulator UDID

        Returns:
            True if successful, False otherwise
        """
        try:
            subprocess.run(
                ["xcrun", "simctl", "boot", udid],
                capture_output=True,
                check=True,
            )
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error booting simulator: {e.stderr}", file=sys.stderr)
            return False


def format_suggestions(suggestions: list[SimulatorInfo], json_format: bool = False) -> str:
    """
    Format suggestions for output.

    Args:
        suggestions: List of suggestions
        json_format: If True, output as JSON

    Returns:
        Formatted string
    """
    if json_format:
        data = {"suggestions": [s.to_dict() for s in suggestions]}
        return json.dumps(data, indent=2)

    if not suggestions:
        return "No simulators available"

    lines = ["Available Simulators:\n"]
    for i, sim in enumerate(suggestions, 1):
        lines.append(f"{i}. {sim.name} (iOS {sim.ios_version})")
        if sim.reasons:
            lines.append(f"   {', '.join(sim.reasons)}")
        lines.append(f"   UDID: {sim.udid}")
        lines.append("")

    return "\n".join(lines)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Intelligent iOS simulator selector",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Get suggestions for user selection
  python scripts/simulator_selector.py --suggest

  # List all available simulators
  python scripts/simulator_selector.py --list

  # Boot a specific simulator
  python scripts/simulator_selector.py --boot <UDID>

  # Get suggestions as JSON
  python scripts/simulator_selector.py --suggest --json
        """,
    )

    parser.add_argument(
        "--suggest",
        action="store_true",
        help="Get top simulator suggestions",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all available simulators",
    )
    parser.add_argument(
        "--boot",
        metavar="UDID",
        help="Boot specific simulator by UDID",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=4,
        help="Number of suggestions (default: 4)",
    )

    args = parser.parse_args()

    selector = SimulatorSelector()

    if args.boot:
        # Boot specific simulator
        success = selector.boot_simulator(args.boot)
        if success:
            print(f"Booted simulator: {args.boot}")
            return 0
        return 1

    if args.list:
        # List all simulators
        simulators = selector.list_simulators()
        output = format_suggestions(simulators, args.json)
        print(output)
        return 0

    if args.suggest:
        # Get suggestions
        selector.list_simulators()
        suggestions = selector.get_suggestions(args.count)
        output = format_suggestions(suggestions, args.json)
        print(output)
        return 0

    # Default: show suggestions
    selector.list_simulators()
    suggestions = selector.get_suggestions(args.count)
    output = format_suggestions(suggestions, args.json)
    print(output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

## File: `ios-simulator-skill/scripts/status_bar.py`
```python
#!/usr/bin/env python3
"""
iOS Status Bar Controller

Override simulator status bar for clean screenshots and testing.
Control time, network, wifi, battery display.

Usage: python scripts/status_bar.py --preset clean
"""

import argparse
import subprocess
import sys

from common import resolve_udid


class StatusBarController:
    """Controls iOS simulator status bar appearance."""

    # Preset configurations
    PRESETS = {
        "clean": {
            "time": "9:41",
            "data_network": "5g",
            "wifi_mode": "active",
            "battery_state": "charged",
            "battery_level": 100,
        },
        "testing": {
            "time": "11:11",
            "data_network": "4g",
            "wifi_mode": "active",
            "battery_state": "discharging",
            "battery_level": 50,
        },
        "low_battery": {
            "time": "9:41",
            "data_network": "5g",
            "wifi_mode": "active",
            "battery_state": "discharging",
            "battery_level": 20,
        },
        "airplane": {
            "time": "9:41",
            "data_network": "none",
            "wifi_mode": "failed",
            "battery_state": "charged",
            "battery_level": 100,
        },
    }

    def __init__(self, udid: str | None = None):
        """Initialize status bar controller.

        Args:
            udid: Optional device UDID (auto-detects booted simulator if None)
        """
        self.udid = udid

    def override(
        self,
        time: str | None = None,
        data_network: str | None = None,
        wifi_mode: str | None = None,
        battery_state: str | None = None,
        battery_level: int | None = None,
    ) -> bool:
        """
        Override status bar appearance.

        Args:
            time: Time in HH:MM format (e.g., "9:41")
            data_network: Network type (none, 1x, 3g, 4g, 5g, lte, lte-a)
            wifi_mode: WiFi state (active, searching, failed)
            battery_state: Battery state (charging, charged, discharging)
            battery_level: Battery percentage (0-100)

        Returns:
            Success status
        """
        cmd = ["xcrun", "simctl", "status_bar"]

        if self.udid:
            cmd.append(self.udid)
        else:
            cmd.append("booted")

        cmd.append("override")

        # Add parameters if provided
        if time:
            cmd.extend(["--time", time])
        if data_network:
            cmd.extend(["--dataNetwork", data_network])
        if wifi_mode:
            cmd.extend(["--wifiMode", wifi_mode])
        if battery_state:
            cmd.extend(["--batteryState", battery_state])
        if battery_level is not None:
            cmd.extend(["--batteryLevel", str(battery_level)])

        try:
            subprocess.run(cmd, capture_output=True, check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def clear(self) -> bool:
        """
        Clear status bar override and restore defaults.

        Returns:
            Success status
        """
        cmd = ["xcrun", "simctl", "status_bar"]

        if self.udid:
            cmd.append(self.udid)
        else:
            cmd.append("booted")

        cmd.append("clear")

        try:
            subprocess.run(cmd, capture_output=True, check=True)
            return True
        except subprocess.CalledProcessError:
            return False


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Override iOS simulator status bar for screenshots and testing"
    )

    # Preset option
    parser.add_argument(
        "--preset",
        choices=list(StatusBarController.PRESETS.keys()),
        help="Use preset configuration (clean, testing, low-battery, airplane)",
    )

    # Custom options
    parser.add_argument(
        "--time",
        help="Override time (HH:MM format, e.g., '9:41')",
    )
    parser.add_argument(
        "--data-network",
        choices=["none", "1x", "3g", "4g", "5g", "lte", "lte-a"],
        help="Data network type",
    )
    parser.add_argument(
        "--wifi-mode",
        choices=["active", "searching", "failed"],
        help="WiFi state",
    )
    parser.add_argument(
        "--battery-state",
        choices=["charging", "charged", "discharging"],
        help="Battery state",
    )
    parser.add_argument(
        "--battery-level",
        type=int,
        help="Battery level 0-100",
    )

    # Other options
    parser.add_argument(
        "--clear",
        action="store_true",
        help="Clear status bar override and restore defaults",
    )
    parser.add_argument(
        "--udid",
        help="Device UDID (auto-detects booted simulator if not provided)",
    )

    args = parser.parse_args()

    # Resolve UDID with auto-detection
    try:
        udid = resolve_udid(args.udid)
    except RuntimeError as e:
        print(f"Error: {e}")
        sys.exit(1)

    controller = StatusBarController(udid=udid)

    # Clear mode
    if args.clear:
        if controller.clear():
            print("Status bar override cleared - defaults restored")
        else:
            print("Failed to clear status bar override")
            sys.exit(1)

    # Preset mode
    elif args.preset:
        preset = StatusBarController.PRESETS[args.preset]
        if controller.override(**preset):
            print(f"Status bar: {args.preset} preset applied")
            print(
                f"  Time: {preset['time']}, "
                f"Network: {preset['data_network']}, "
                f"Battery: {preset['battery_level']}%"
            )
        else:
            print(f"Failed to apply {args.preset} preset")
            sys.exit(1)

    # Custom mode
    elif any(
        [
            args.time,
            args.data_network,
            args.wifi_mode,
            args.battery_state,
            args.battery_level is not None,
        ]
    ):
        if controller.override(
            time=args.time,
            data_network=args.data_network,
            wifi_mode=args.wifi_mode,
            battery_state=args.battery_state,
            battery_level=args.battery_level,
        ):
            output = "Status bar override applied:"
            if args.time:
                output += f" Time={args.time}"
            if args.data_network:
                output += f" Network={args.data_network}"
            if args.battery_level is not None:
                output += f" Battery={args.battery_level}%"
            print(output)
        else:
            print("Failed to override status bar")
            sys.exit(1)

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
```

## File: `ios-simulator-skill/scripts/test_recorder.py`
```python
#!/usr/bin/env python3
"""
Test Recorder for iOS Simulator Testing

Records test execution with automatic screenshots and documentation.
Optimized for minimal token output during execution.

Usage:
    As a script: python scripts/test_recorder.py --test-name "Test Name" --output dir/
    As a module: from scripts.test_recorder import TestRecorder
"""

import argparse
import json
import subprocess
import time
from datetime import datetime
from pathlib import Path

from common import (
    capture_screenshot,
    count_elements,
    generate_screenshot_name,
    get_accessibility_tree,
    resolve_udid,
)


class TestRecorder:
    """Records test execution with screenshots and accessibility snapshots."""

    def __init__(
        self,
        test_name: str,
        output_dir: str = "test-artifacts",
        udid: str | None = None,
        inline: bool = False,
        screenshot_size: str = "half",
        app_name: str | None = None,
    ):
        """
        Initialize test recorder.

        Args:
            test_name: Name of the test being recorded
            output_dir: Directory for test artifacts
            udid: Optional device UDID (uses booted if not specified)
            inline: If True, return screenshots as base64 (for vision-based automation)
            screenshot_size: 'full', 'half', 'quarter', 'thumb' (default: 'half')
            app_name: App name for semantic screenshot naming
        """
        self.test_name = test_name
        self.udid = udid
        self.inline = inline
        self.screenshot_size = screenshot_size
        self.app_name = app_name
        self.start_time = time.time()
        self.steps: list[dict] = []
        self.current_step = 0

        # Create timestamped output directory
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        safe_name = test_name.lower().replace(" ", "-")
        self.output_dir = Path(output_dir) / f"{safe_name}-{timestamp}"
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Create subdirectories (only if not in inline mode)
        if not inline:
            self.screenshots_dir = self.output_dir / "screenshots"
            self.screenshots_dir.mkdir(exist_ok=True)
        else:
            self.screenshots_dir = None

        self.accessibility_dir = self.output_dir / "accessibility"
        self.accessibility_dir.mkdir(exist_ok=True)

        # Token-efficient output
        mode_str = "(inline mode)" if inline else ""
        print(f"Recording: {test_name} {mode_str}")
        print(f"Output: {self.output_dir}/")

    def step(
        self,
        description: str,
        screen_name: str | None = None,
        state: str | None = None,
        assertion: str | None = None,
        metadata: dict | None = None,
    ):
        """
        Record a test step with automatic screenshot.

        Args:
            description: Step description
            screen_name: Screen name for semantic naming
            state: State description for semantic naming
            assertion: Optional assertion to verify
            metadata: Optional metadata for the step
        """
        self.current_step += 1
        step_time = time.time() - self.start_time

        # Capture screenshot using new utility
        screenshot_result = capture_screenshot(
            self.udid,
            size=self.screenshot_size,
            inline=self.inline,
            app_name=self.app_name,
            screen_name=screen_name or description,
            state=state,
        )

        # Capture accessibility tree
        accessibility_path = (
            self.accessibility_dir
            / f"{self.current_step:03d}-{description.lower().replace(' ', '-')[:20]}.json"
        )
        element_count = self._capture_accessibility(accessibility_path)

        # Store step data
        step_data = {
            "number": self.current_step,
            "description": description,
            "timestamp": step_time,
            "element_count": element_count,
            "accessibility": accessibility_path.name,
            "screenshot_mode": screenshot_result["mode"],
            "screenshot_size": self.screenshot_size,
        }

        # Handle screenshot data based on mode
        if screenshot_result["mode"] == "file":
            step_data["screenshot"] = screenshot_result["file_path"]
            step_data["screenshot_name"] = Path(screenshot_result["file_path"]).name
        else:
            # Inline mode
            step_data["screenshot_base64"] = screenshot_result["base64_data"]
            step_data["screenshot_dimensions"] = (
                screenshot_result["width"],
                screenshot_result["height"],
            )

        if assertion:
            step_data["assertion"] = assertion
            step_data["assertion_passed"] = True

        if metadata:
            step_data["metadata"] = metadata

        self.steps.append(step_data)

        # Token-efficient output (single line)
        status = "✓" if not assertion or step_data.get("assertion_passed") else "✗"
        screenshot_info = (
            f" [{screenshot_result['width']}x{screenshot_result['height']}]" if self.inline else ""
        )
        print(
            f"{status} Step {self.current_step}: {description} ({step_time:.1f}s){screenshot_info}"
        )

    def _capture_screenshot(self, output_path: Path) -> bool:
        """Capture screenshot using simctl."""
        cmd = ["xcrun", "simctl", "io"]

        if self.udid:
            cmd.append(self.udid)
        else:
            cmd.append("booted")

        cmd.extend(["screenshot", str(output_path)])

        try:
            subprocess.run(cmd, capture_output=True, check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def _capture_accessibility(self, output_path: Path) -> int:
        """Capture accessibility tree and return element count."""
        try:
            # Use shared utility to fetch tree
            tree = get_accessibility_tree(self.udid, nested=True)

            # Save tree
            with open(output_path, "w") as f:
                json.dump(tree, f, indent=2)

            # Count elements using shared utility
            return count_elements(tree)
        except Exception:
            return 0

    def generate_report(self) -> dict[str, str]:
        """
        Generate markdown test report.

        Returns:
            Dictionary with paths to generated files
        """
        duration = time.time() - self.start_time
        report_path = self.output_dir / "report.md"

        # Generate markdown
        with open(report_path, "w") as f:
            f.write(f"# Test Report: {self.test_name}\n\n")
            f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"**Duration:** {duration:.1f} seconds\n")
            f.write(f"**Steps:** {len(self.steps)}\n\n")

            # Steps section
            f.write("## Test Steps\n\n")
            for step in self.steps:
                f.write(
                    f"### Step {step['number']}: {step['description']} ({step['timestamp']:.1f}s)\n\n"
                )
                f.write(f"![Screenshot](screenshots/{step['screenshot']})\n\n")

                if step.get("assertion"):
                    status = "✓" if step.get("assertion_passed") else "✗"
                    f.write(f"**Assertion:** {step['assertion']} {status}\n\n")

                if step.get("metadata"):
                    f.write("**Metadata:**\n")
                    for key, value in step["metadata"].items():
                        f.write(f"- {key}: {value}\n")
                    f.write("\n")

                f.write(f"**Accessibility Elements:** {step['element_count']}\n\n")
                f.write("---\n\n")

            # Summary
            f.write("## Summary\n\n")
            f.write(f"- Total steps: {len(self.steps)}\n")
            f.write(f"- Duration: {duration:.1f}s\n")
            f.write(f"- Screenshots: {len(self.steps)}\n")
            f.write(f"- Accessibility snapshots: {len(self.steps)}\n")

        # Save metadata JSON
        metadata_path = self.output_dir / "metadata.json"
        with open(metadata_path, "w") as f:
            json.dump(
                {
                    "test_name": self.test_name,
                    "duration": duration,
                    "steps": self.steps,
                    "timestamp": datetime.now().isoformat(),
                },
                f,
                indent=2,
            )

        # Token-efficient output
        print(f"Report: {report_path}")

        return {
            "markdown_path": str(report_path),
            "metadata_path": str(metadata_path),
            "output_dir": str(self.output_dir),
        }


def main():
    """Main entry point for command-line usage."""
    parser = argparse.ArgumentParser(
        description="Record test execution with screenshots and documentation"
    )
    parser.add_argument("--test-name", required=True, help="Name of the test being recorded")
    parser.add_argument(
        "--output", default="test-artifacts", help="Output directory for test artifacts"
    )
    parser.add_argument(
        "--udid",
        help="Device UDID (auto-detects booted simulator if not provided)",
    )
    parser.add_argument(
        "--inline",
        action="store_true",
        help="Return screenshots as base64 (inline mode for vision-based automation)",
    )
    parser.add_argument(
        "--size",
        choices=["full", "half", "quarter", "thumb"],
        default="half",
        help="Screenshot size for token optimization (default: half)",
    )
    parser.add_argument("--app-name", help="App name for semantic screenshot naming")

    args = parser.parse_args()

    # Resolve UDID with auto-detection
    try:
        udid = resolve_udid(args.udid)
    except RuntimeError as e:
        print(f"Error: {e}")
        import sys

        sys.exit(1)

    # Create recorder
    TestRecorder(
        test_name=args.test_name,
        output_dir=args.output,
        udid=udid,
        inline=args.inline,
        screenshot_size=args.size,
        app_name=args.app_name,
    )

    print("Test recorder initialized. Use the following methods:")
    print('  recorder.step("description") - Record a test step')
    print("  recorder.generate_report() - Generate final report")
    print()
    print("Example:")
    print('  recorder.step("Launch app", screen_name="Splash")')
    print(
        '  recorder.step("Enter credentials", screen_name="Login", state="Empty", metadata={"user": "test"})'
    )
    print('  recorder.step("Verify login", assertion="Home screen visible")')
    print("  recorder.generate_report()")


if __name__ == "__main__":
    main()
```

## File: `ios-simulator-skill/scripts/visual_diff.py`
```python
#!/usr/bin/env python3
"""
Visual Diff Tool for iOS Simulator Screenshots

Compares two screenshots pixel-by-pixel to detect visual changes.
Optimized for minimal token output.

Usage: python scripts/visual_diff.py baseline.png current.png [options]
"""

import argparse
import json
import os
import sys
from pathlib import Path

try:
    from PIL import Image, ImageChops, ImageDraw
except ImportError:
    print("Error: Pillow not installed. Run: pip3 install pillow")
    sys.exit(1)


class VisualDiffer:
    """Performs visual comparison between screenshots."""

    def __init__(self, threshold: float = 0.01):
        """
        Initialize differ with threshold.

        Args:
            threshold: Maximum acceptable difference ratio (0.01 = 1%)
        """
        self.threshold = threshold

    def compare(self, baseline_path: str, current_path: str) -> dict:
        """
        Compare two images and return difference metrics.

        Args:
            baseline_path: Path to baseline image
            current_path: Path to current image

        Returns:
            Dictionary with comparison results
        """
        # Load images
        try:
            baseline = Image.open(baseline_path)
            current = Image.open(current_path)
        except FileNotFoundError as e:
            print(f"Error: Image not found - {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Error: Failed to load image - {e}")
            sys.exit(1)

        # Verify dimensions match
        if baseline.size != current.size:
            return {
                "error": "Image dimensions do not match",
                "baseline_size": baseline.size,
                "current_size": current.size,
            }

        # Convert to RGB if needed
        if baseline.mode != "RGB":
            baseline = baseline.convert("RGB")
        if current.mode != "RGB":
            current = current.convert("RGB")

        # Calculate difference
        diff = ImageChops.difference(baseline, current)

        # Calculate metrics
        total_pixels = baseline.size[0] * baseline.size[1]
        diff_pixels = self._count_different_pixels(diff)
        diff_percentage = (diff_pixels / total_pixels) * 100

        # Determine pass/fail
        passed = diff_percentage <= (self.threshold * 100)

        return {
            "dimensions": baseline.size,
            "total_pixels": total_pixels,
            "different_pixels": diff_pixels,
            "difference_percentage": round(diff_percentage, 2),
            "threshold_percentage": self.threshold * 100,
            "passed": passed,
            "verdict": "PASS" if passed else "FAIL",
        }

    def _count_different_pixels(self, diff_image: Image.Image) -> int:
        """Count number of pixels that are different."""
        # Convert to grayscale for easier processing
        diff_gray = diff_image.convert("L")

        # Count non-zero pixels (different)
        pixels = diff_gray.getdata()
        return sum(1 for pixel in pixels if pixel > 10)  # Threshold for noise

    def generate_diff_image(self, baseline_path: str, current_path: str, output_path: str) -> None:
        """Generate highlighted difference image."""
        baseline = Image.open(baseline_path).convert("RGB")
        current = Image.open(current_path).convert("RGB")

        # Create difference image
        diff = ImageChops.difference(baseline, current)

        # Enhance differences with red overlay
        diff_enhanced = Image.new("RGB", baseline.size)
        for x in range(baseline.size[0]):
            for y in range(baseline.size[1]):
                diff_pixel = diff.getpixel((x, y))
                if sum(diff_pixel) > 30:  # Threshold for visibility
                    # Highlight in red
                    diff_enhanced.putpixel((x, y), (255, 0, 0))
                else:
                    # Keep original
                    diff_enhanced.putpixel((x, y), current.getpixel((x, y)))

        diff_enhanced.save(output_path)

    def generate_side_by_side(
        self, baseline_path: str, current_path: str, output_path: str
    ) -> None:
        """Generate side-by-side comparison image."""
        baseline = Image.open(baseline_path)
        current = Image.open(current_path)

        # Create combined image
        width = baseline.size[0] * 2 + 10  # 10px separator
        height = max(baseline.size[1], current.size[1])
        combined = Image.new("RGB", (width, height), color=(128, 128, 128))

        # Paste images
        combined.paste(baseline, (0, 0))
        combined.paste(current, (baseline.size[0] + 10, 0))

        combined.save(output_path)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Compare screenshots for visual differences")
    parser.add_argument("baseline", help="Path to baseline screenshot")
    parser.add_argument("current", help="Path to current screenshot")
    parser.add_argument(
        "--output",
        default=".",
        help="Output directory for diff artifacts (default: current directory)",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.01,
        help="Acceptable difference threshold (0.01 = 1%%, default: 0.01)",
    )
    parser.add_argument(
        "--details", action="store_true", help="Show detailed output (increases tokens)"
    )

    args = parser.parse_args()

    # Create output directory if needed
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Initialize differ
    differ = VisualDiffer(threshold=args.threshold)

    # Perform comparison
    result = differ.compare(args.baseline, args.current)

    # Handle dimension mismatch
    if "error" in result:
        print(f"Error: {result['error']}")
        print(f"Baseline: {result['baseline_size']}")
        print(f"Current: {result['current_size']}")
        sys.exit(1)

    # Generate artifacts
    diff_image_path = output_dir / "diff.png"
    comparison_image_path = output_dir / "side-by-side.png"

    try:
        differ.generate_diff_image(args.baseline, args.current, str(diff_image_path))
        differ.generate_side_by_side(args.baseline, args.current, str(comparison_image_path))
    except Exception as e:
        print(f"Warning: Could not generate images - {e}")

    # Output results (token-optimized)
    if args.details:
        # Detailed output
        report = {
            "summary": {
                "baseline": args.baseline,
                "current": args.current,
                "threshold": args.threshold,
                "passed": result["passed"],
            },
            "results": result,
            "artifacts": {
                "diff_image": str(diff_image_path),
                "comparison_image": str(comparison_image_path),
            },
        }
        print(json.dumps(report, indent=2))
    else:
        # Minimal output (default)
        print(f"Difference: {result['difference_percentage']}% ({result['verdict']})")
        if result["different_pixels"] > 0:
            print(f"Changed pixels: {result['different_pixels']:,}")
        print(f"Artifacts saved to: {output_dir}/")

    # Save JSON report
    report_path = output_dir / "diff-report.json"
    with open(report_path, "w") as f:
        json.dump(
            {
                "baseline": os.path.basename(args.baseline),
                "current": os.path.basename(args.current),
                "results": result,
                "artifacts": {"diff": "diff.png", "comparison": "side-by-side.png"},
            },
            f,
            indent=2,
        )

    # Exit with error if test failed
    sys.exit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
```

## File: `ios-simulator-skill/scripts/common/__init__.py`
```python
"""
Common utilities shared across iOS simulator scripts.

This module centralizes genuinely reused code patterns to eliminate duplication
while respecting Jackson's Law - no over-abstraction, only truly shared logic.

Organization:
- device_utils: Device detection, command building, coordinate transformation
- idb_utils: IDB-specific operations (accessibility tree, element manipulation)
- cache_utils: Progressive disclosure caching for large outputs
- screenshot_utils: Screenshot capture with file and inline modes
"""

from .cache_utils import ProgressiveCache, get_cache
from .device_utils import (
    build_idb_command,
    build_simctl_command,
    get_booted_device_udid,
    get_device_screen_size,
    resolve_udid,
    transform_screenshot_coords,
)
from .idb_utils import (
    count_elements,
    flatten_tree,
    get_accessibility_tree,
    get_screen_size,
)
from .screenshot_utils import (
    capture_screenshot,
    format_screenshot_result,
    generate_screenshot_name,
    get_size_preset,
    resize_screenshot,
)

__all__ = [
    # cache_utils
    "ProgressiveCache",
    # device_utils
    "build_idb_command",
    "build_simctl_command",
    # screenshot_utils
    "capture_screenshot",
    # idb_utils
    "count_elements",
    "flatten_tree",
    "format_screenshot_result",
    "generate_screenshot_name",
    "get_accessibility_tree",
    "get_booted_device_udid",
    "get_cache",
    "get_device_screen_size",
    "get_screen_size",
    "get_size_preset",
    "resize_screenshot",
    "resolve_udid",
    "transform_screenshot_coords",
]
```

## File: `ios-simulator-skill/scripts/common/cache_utils.py`
```python
#!/usr/bin/env python3
"""
Progressive disclosure cache for large outputs.

Implements cache system to support progressive disclosure pattern:
- Return concise summary with cache_id for large outputs
- User retrieves full details on demand via cache_id
- Reduces token usage by 96% for common queries

Cache directory: ~/.ios-simulator-skill/cache/
Cache expiration: Configurable per cache type (default 1 hour)

Used by:
- sim_list.py - Simulator listing progressive disclosure
- Future: build logs, UI trees, etc.
"""

import json
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any


class ProgressiveCache:
    """Cache for progressive disclosure pattern.

    Stores large outputs with timestamped IDs for on-demand retrieval.
    Automatically cleans up expired entries.
    """

    def __init__(self, cache_dir: str | None = None, max_age_hours: int = 1):
        """Initialize cache system.

        Args:
            cache_dir: Cache directory path (default: ~/.ios-simulator-skill/cache/)
            max_age_hours: Max age for cache entries before expiration (default: 1 hour)
        """
        if cache_dir is None:
            cache_dir = str(Path("~/.ios-simulator-skill/cache").expanduser())

        self.cache_dir = Path(cache_dir)
        self.max_age_hours = max_age_hours

        # Create cache directory if needed
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def save(self, data: dict[str, Any], cache_type: str) -> str:
        """Save data to cache and return cache_id.

        Args:
            data: Dictionary data to cache
            cache_type: Type of cache ('simulator-list', 'build-log', 'ui-tree', etc.)

        Returns:
            Cache ID like 'sim-20251028-143052' for use in progressive disclosure

        Example:
            cache_id = cache.save({'devices': [...]}, 'simulator-list')
            # Returns: 'sim-20251028-143052'
        """
        # Generate cache_id with timestamp
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        cache_prefix = cache_type.split("-", maxsplit=1)[0]  # e.g., 'sim' from 'simulator-list'
        cache_id = f"{cache_prefix}-{timestamp}"

        # Save to file
        cache_file = self.cache_dir / f"{cache_id}.json"
        with open(cache_file, "w") as f:
            json.dump(
                {
                    "cache_id": cache_id,
                    "cache_type": cache_type,
                    "created_at": datetime.now().isoformat(),
                    "data": data,
                },
                f,
                indent=2,
            )

        return cache_id

    def get(self, cache_id: str) -> dict[str, Any] | None:
        """Retrieve data from cache by cache_id.

        Args:
            cache_id: Cache ID from save() or list_entries()

        Returns:
            Cached data dictionary, or None if not found/expired

        Example:
            data = cache.get('sim-20251028-143052')
            if data:
                print(f"Found {len(data)} devices")
        """
        cache_file = self.cache_dir / f"{cache_id}.json"

        if not cache_file.exists():
            return None

        # Check if expired
        if self._is_expired(cache_file):
            cache_file.unlink()  # Delete expired file
            return None

        try:
            with open(cache_file) as f:
                entry = json.load(f)
                return entry.get("data")
        except (OSError, json.JSONDecodeError):
            return None

    def list_entries(self, cache_type: str | None = None) -> list[dict[str, Any]]:
        """List available cache entries with metadata.

        Args:
            cache_type: Filter by type (e.g., 'simulator-list'), or None for all

        Returns:
            List of cache entries with id, type, created_at, age_seconds

        Example:
            entries = cache.list_entries('simulator-list')
            for entry in entries:
                print(f"{entry['id']} - {entry['age_seconds']}s old")
        """
        entries = []

        for cache_file in sorted(self.cache_dir.glob("*.json"), reverse=True):
            # Check if expired
            if self._is_expired(cache_file):
                cache_file.unlink()
                continue

            try:
                with open(cache_file) as f:
                    entry = json.load(f)

                    # Filter by type if specified
                    if cache_type and entry.get("cache_type") != cache_type:
                        continue

                    created_at = datetime.fromisoformat(entry.get("created_at", ""))
                    age_seconds = (datetime.now() - created_at).total_seconds()

                    entries.append(
                        {
                            "id": entry.get("cache_id"),
                            "type": entry.get("cache_type"),
                            "created_at": entry.get("created_at"),
                            "age_seconds": int(age_seconds),
                        }
                    )
            except (OSError, json.JSONDecodeError, ValueError):
                continue

        return entries

    def cleanup(self, max_age_hours: int | None = None) -> int:
        """Remove expired cache entries.

        Args:
            max_age_hours: Age threshold (default: uses instance max_age_hours)

        Returns:
            Number of entries deleted

        Example:
            deleted = cache.cleanup()
            print(f"Deleted {deleted} expired cache entries")
        """
        if max_age_hours is None:
            max_age_hours = self.max_age_hours

        deleted = 0

        for cache_file in self.cache_dir.glob("*.json"):
            if self._is_expired(cache_file, max_age_hours):
                cache_file.unlink()
                deleted += 1

        return deleted

    def clear(self, cache_type: str | None = None) -> int:
        """Clear all cache entries of a type.

        Args:
            cache_type: Type to clear (e.g., 'simulator-list'), or None to clear all

        Returns:
            Number of entries deleted

        Example:
            cleared = cache.clear('simulator-list')
            print(f"Cleared {cleared} simulator list entries")
        """
        deleted = 0

        for cache_file in self.cache_dir.glob("*.json"):
            if cache_type is None:
                # Clear all
                cache_file.unlink()
                deleted += 1
            else:
                # Clear by type
                try:
                    with open(cache_file) as f:
                        entry = json.load(f)
                        if entry.get("cache_type") == cache_type:
                            cache_file.unlink()
                            deleted += 1
                except (OSError, json.JSONDecodeError):
                    pass

        return deleted

    def _is_expired(self, cache_file: Path, max_age_hours: int | None = None) -> bool:
        """Check if cache file is expired.

        Args:
            cache_file: Path to cache file
            max_age_hours: Age threshold (default: uses instance max_age_hours)

        Returns:
            True if file is older than max_age_hours
        """
        if max_age_hours is None:
            max_age_hours = self.max_age_hours

        try:
            with open(cache_file) as f:
                entry = json.load(f)
                created_at = datetime.fromisoformat(entry.get("created_at", ""))
                age = datetime.now() - created_at
                return age > timedelta(hours=max_age_hours)
        except (OSError, json.JSONDecodeError, ValueError):
            return True


# Module-level cache instances (lazy-loaded)
_cache_instances: dict[str, ProgressiveCache] = {}


def get_cache(cache_dir: str | None = None) -> ProgressiveCache:
    """Get or create global cache instance.

    Args:
        cache_dir: Custom cache directory (uses default if None)

    Returns:
        ProgressiveCache instance
    """
    # Use cache_dir as key, or 'default' if None
    key = cache_dir or "default"

    if key not in _cache_instances:
        _cache_instances[key] = ProgressiveCache(cache_dir)

    return _cache_instances[key]
```

## File: `ios-simulator-skill/scripts/common/device_utils.py`
```python
#!/usr/bin/env python3
"""
Shared device and simulator utilities.

Common patterns for interacting with simulators via xcrun simctl and IDB.
Standardizes command building and device targeting to prevent errors.

Follows Jackson's Law - only extracts genuinely reused patterns.

Used by:
- app_launcher.py (8 call sites) - App lifecycle commands
- Multiple scripts (15+ locations) - IDB command building
- navigator.py, gesture.py - Coordinate transformation
- test_recorder.py, app_state_capture.py - Auto-UDID detection
"""

import json
import re
import subprocess


def build_simctl_command(
    operation: str,
    udid: str | None = None,
    *args,
) -> list[str]:
    """
    Build xcrun simctl command with proper device handling.

    Standardizes command building to prevent device targeting bugs.
    Automatically uses "booted" if no UDID provided.

    Used by:
    - app_launcher.py: launch, terminate, install, uninstall, openurl, listapps, spawn
    - Multiple scripts: generic simctl operations

    Args:
        operation: simctl operation (launch, terminate, install, etc.)
        udid: Device UDID (uses 'booted' if None)
        *args: Additional command arguments

    Returns:
        Complete command list ready for subprocess.run()

    Examples:
        # Launch app on booted simulator
        cmd = build_simctl_command("launch", None, "com.app.bundle")
        # Returns: ["xcrun", "simctl", "launch", "booted", "com.app.bundle"]

        # Launch on specific device
        cmd = build_simctl_command("launch", "ABC123", "com.app.bundle")
        # Returns: ["xcrun", "simctl", "launch", "ABC123", "com.app.bundle"]

        # Install app on specific device
        cmd = build_simctl_command("install", "ABC123", "/path/to/app.app")
        # Returns: ["xcrun", "simctl", "install", "ABC123", "/path/to/app.app"]
    """
    cmd = ["xcrun", "simctl", operation]

    # Add device (booted or specific UDID)
    cmd.append(udid if udid else "booted")

    # Add remaining arguments
    cmd.extend(str(arg) for arg in args)

    return cmd


def build_idb_command(
    operation: str,
    udid: str | None = None,
    *args,
) -> list[str]:
    """
    Build IDB command with proper device targeting.

    Standardizes IDB command building across all scripts using IDB.
    Handles device UDID consistently.

    Used by:
    - navigator.py: ui tap, ui text, ui describe-all
    - gesture.py: ui swipe, ui tap
    - keyboard.py: ui key, ui text, ui tap
    - And more: 15+ locations

    Args:
        operation: IDB operation path (e.g., "ui tap", "ui text", "ui describe-all")
        udid: Device UDID (omits --udid flag if None, IDB uses booted by default)
        *args: Additional command arguments

    Returns:
        Complete command list ready for subprocess.run()

    Examples:
        # Tap on booted simulator
        cmd = build_idb_command("ui tap", None, "200", "400")
        # Returns: ["idb", "ui", "tap", "200", "400"]

        # Tap on specific device
        cmd = build_idb_command("ui tap", "ABC123", "200", "400")
        # Returns: ["idb", "ui", "tap", "200", "400", "--udid", "ABC123"]

        # Get accessibility tree
        cmd = build_idb_command("ui describe-all", "ABC123", "--json", "--nested")
        # Returns: ["idb", "ui", "describe-all", "--json", "--nested", "--udid", "ABC123"]

        # Enter text
        cmd = build_idb_command("ui text", None, "hello world")
        # Returns: ["idb", "ui", "text", "hello world"]
    """
    # Split operation into parts (e.g., "ui tap" -> ["ui", "tap"])
    cmd = ["idb"] + operation.split()

    # Add arguments
    cmd.extend(str(arg) for arg in args)

    # Add device targeting if specified (optional for IDB, uses booted by default)
    if udid:
        cmd.extend(["--udid", udid])

    return cmd


def get_booted_device_udid() -> str | None:
    """
    Auto-detect currently booted simulator UDID.

    Queries xcrun simctl for booted devices and returns first match.

    Returns:
        UDID of booted simulator, or None if no simulator is booted.

    Example:
        udid = get_booted_device_udid()
        if udid:
            print(f"Booted simulator: {udid}")
        else:
            print("No simulator is currently booted")
    """
    try:
        result = subprocess.run(
            ["xcrun", "simctl", "list", "devices", "booted"],
            capture_output=True,
            text=True,
            check=True,
        )

        # Parse output to find UDID
        # Format: "  iPhone 16 Pro (ABC123-DEF456) (Booted)"
        for line in result.stdout.split("\n"):
            # Look for UUID pattern in parentheses
            match = re.search(r"\(([A-F0-9\-]{36})\)", line)
            if match:
                return match.group(1)

        return None
    except subprocess.CalledProcessError:
        return None


def resolve_udid(udid_arg: str | None) -> str:
    """
    Resolve device UDID with auto-detection fallback.

    If udid_arg is provided, returns it immediately.
    If None, attempts to auto-detect booted simulator.
    Raises error if neither is available.

    Args:
        udid_arg: Explicit UDID from command line, or None

    Returns:
        Valid UDID string

    Raises:
        RuntimeError: If no UDID provided and no booted simulator found

    Example:
        try:
            udid = resolve_udid(args.udid)  # args.udid might be None
            print(f"Using device: {udid}")
        except RuntimeError as e:
            print(f"Error: {e}")
            sys.exit(1)
    """
    if udid_arg:
        return udid_arg

    booted_udid = get_booted_device_udid()
    if booted_udid:
        return booted_udid

    raise RuntimeError(
        "No device UDID provided and no simulator is currently booted.\n"
        "Boot a simulator or provide --udid explicitly:\n"
        "  xcrun simctl boot <device-name>\n"
        "  python scripts/script_name.py --udid <device-udid>"
    )


def get_device_screen_size(udid: str) -> tuple[int, int]:
    """
    Get actual screen dimensions for device via accessibility tree.

    Queries IDB accessibility tree to determine actual device resolution.
    Falls back to iPhone 14 defaults (390x844) if detection fails.

    Args:
        udid: Device UDID

    Returns:
        Tuple of (width, height) in pixels

    Example:
        width, height = get_device_screen_size("ABC123")
        print(f"Device screen: {width}x{height}")
    """
    try:
        cmd = build_idb_command("ui describe-all", udid, "--json")
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)

        # Parse JSON response
        data = json.loads(result.stdout)
        tree = data[0] if isinstance(data, list) and len(data) > 0 else data

        # Get frame size from root element
        if tree and "frame" in tree:
            frame = tree["frame"]
            width = int(frame.get("width", 390))
            height = int(frame.get("height", 844))
            return (width, height)

        # Fallback
        return (390, 844)
    except Exception:
        # Graceful fallback to iPhone 14 Pro defaults
        return (390, 844)


def resolve_device_identifier(identifier: str) -> str:
    """
    Resolve device name or partial UDID to full UDID.

    Supports multiple identifier formats:
    - Full UDID: "ABC-123-DEF456..." (36 character UUID)
    - Device name: "iPhone 16 Pro" (matches full name)
    - Partial match: "iPhone 16" (matches first device containing this string)
    - Special: "booted" (resolves to currently booted device)

    Args:
        identifier: Device UDID, name, or special value "booted"

    Returns:
        Full device UDID

    Raises:
        RuntimeError: If identifier cannot be resolved

    Example:
        udid = resolve_device_identifier("iPhone 16 Pro")
        # Returns: "ABC123DEF456..."

        udid = resolve_device_identifier("booted")
        # Returns UDID of booted simulator
    """
    # Handle "booted" special case
    if identifier.lower() == "booted":
        booted = get_booted_device_udid()
        if booted:
            return booted
        raise RuntimeError(
            "No simulator is currently booted. "
            "Boot a simulator first: xcrun simctl boot <device-udid>"
        )

    # Check if already a full UDID (36 character UUID format)
    if re.match(r"^[A-F0-9\-]{36}$", identifier, re.IGNORECASE):
        return identifier.upper()

    # Try to match by device name
    simulators = list_simulators(state=None)
    exact_matches = [s for s in simulators if s["name"].lower() == identifier.lower()]
    if exact_matches:
        return exact_matches[0]["udid"]

    # Try partial match
    partial_matches = [s for s in simulators if identifier.lower() in s["name"].lower()]
    if partial_matches:
        return partial_matches[0]["udid"]

    # No match found
    raise RuntimeError(
        f"Device '{identifier}' not found. "
        f"Use 'xcrun simctl list devices' to see available simulators."
    )


def list_simulators(state: str | None = None) -> list[dict]:
    """
    List iOS simulators with optional state filtering.

    Queries xcrun simctl and returns structured list of simulators.
    Optionally filters by state (available, booted, all).

    Args:
        state: Optional filter - "available", "booted", or None for all

    Returns:
        List of simulator dicts with keys:
        - "name": Device name (e.g., "iPhone 16 Pro")
        - "udid": Device UDID (36 char UUID)
        - "state": Device state ("Booted", "Shutdown", "Unavailable")
        - "runtime": iOS version (e.g., "iOS 18.0", "unavailable")
        - "type": Device type ("iPhone", "iPad", "Apple Watch", etc.)

    Example:
        # List all simulators
        all_sims = list_simulators()
        print(f"Total simulators: {len(all_sims)}")

        # List only available simulators
        available = list_simulators(state="available")
        for sim in available:
            print(f"{sim['name']} ({sim['state']}) - {sim['udid']}")

        # List only booted simulators
        booted = list_simulators(state="booted")
        for sim in booted:
            print(f"Booted: {sim['name']}")
    """
    try:
        # Query simctl for device list
        cmd = ["xcrun", "simctl", "list", "devices", "-j"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)

        data = json.loads(result.stdout)
        simulators = []

        # Parse JSON response
        # Format: {"devices": {"iOS 18.0": [{...}, {...}], "iOS 17.0": [...], ...}}
        for ios_version, devices in data.get("devices", {}).items():
            for device in devices:
                sim = {
                    "name": device.get("name", "Unknown"),
                    "udid": device.get("udid", ""),
                    "state": device.get("state", "Unknown"),
                    "runtime": ios_version,
                    "type": _extract_device_type(device.get("name", "")),
                }
                simulators.append(sim)

        # Apply state filtering
        if state == "booted":
            return [s for s in simulators if s["state"] == "Booted"]
        if state == "available":
            return [s for s in simulators if s["state"] == "Shutdown"]  # Available to boot
        if state is None:
            return simulators
        return [s for s in simulators if s["state"].lower() == state.lower()]

    except (subprocess.CalledProcessError, json.JSONDecodeError, KeyError) as e:
        raise RuntimeError(f"Failed to list simulators: {e}") from e


def _extract_device_type(device_name: str) -> str:
    """
    Extract device type from device name.

    Parses device name to determine type (iPhone, iPad, Watch, etc.).

    Args:
        device_name: Full device name (e.g., "iPhone 16 Pro")

    Returns:
        Device type string

    Example:
        _extract_device_type("iPhone 16 Pro")  # Returns "iPhone"
        _extract_device_type("iPad Air")        # Returns "iPad"
        _extract_device_type("Apple Watch Series 9") # Returns "Watch"
    """
    if "iPhone" in device_name:
        return "iPhone"
    if "iPad" in device_name:
        return "iPad"
    if "Watch" in device_name or "Apple Watch" in device_name:
        return "Watch"
    if "TV" in device_name or "Apple TV" in device_name:
        return "TV"
    return "Unknown"


def transform_screenshot_coords(
    x: float,
    y: float,
    screenshot_width: int,
    screenshot_height: int,
    device_width: int,
    device_height: int,
) -> tuple[int, int]:
    """
    Transform screenshot coordinates to device coordinates.

    Handles the case where a screenshot was downscaled (e.g., to 'half' size)
    and needs to be transformed back to actual device pixel coordinates
    for accurate tapping.

    The transformation is linear:
    device_x = (screenshot_x / screenshot_width) * device_width
    device_y = (screenshot_y / screenshot_height) * device_height

    Args:
        x, y: Coordinates in the screenshot
        screenshot_width, screenshot_height: Screenshot dimensions (e.g., 195, 422)
        device_width, device_height: Actual device dimensions (e.g., 390, 844)

    Returns:
        Tuple of (device_x, device_y) in device pixels

    Example:
        # Screenshot taken at 'half' size: 195x422 (from 390x844 device)
        device_x, device_y = transform_screenshot_coords(
            100, 200,  # Tap point in screenshot
            195, 422,  # Screenshot dimensions
            390, 844   # Device dimensions
        )
        print(f"Tap at device coords: ({device_x}, {device_y})")
        # Output: Tap at device coords: (200, 400)
    """
    device_x = int((x / screenshot_width) * device_width)
    device_y = int((y / screenshot_height) * device_height)
    return (device_x, device_y)
```

## File: `ios-simulator-skill/scripts/common/idb_utils.py`
```python
#!/usr/bin/env python3
"""
Shared IDB utility functions.

This module provides common IDB operations used across multiple scripts.
Follows Jackson's Law - only shared code that's truly reused, not speculative.

Used by:
- navigator.py - Accessibility tree navigation
- screen_mapper.py - UI element analysis
- accessibility_audit.py - WCAG compliance checking
- test_recorder.py - Test documentation
- app_state_capture.py - State snapshots
- gesture.py - Touch gesture operations
"""

import json
import subprocess
import sys


def get_accessibility_tree(udid: str | None = None, nested: bool = True) -> dict:
    """
    Fetch accessibility tree from IDB.

    The accessibility tree represents the complete UI hierarchy of the current
    screen, with all element properties needed for semantic navigation.

    Args:
        udid: Device UDID (uses booted simulator if None)
        nested: Include nested structure (default True). If False, returns flat array.

    Returns:
        Root element of accessibility tree as dict.
        Structure: {
            "type": "Window",
            "AXLabel": "App Name",
            "frame": {"x": 0, "y": 0, "width": 390, "height": 844},
            "children": [...]
        }

    Raises:
        SystemExit: If IDB command fails or returns invalid JSON

    Example:
        tree = get_accessibility_tree("UDID123")
        # Root is Window element with all children nested
    """
    cmd = ["idb", "ui", "describe-all", "--json"]
    if nested:
        cmd.append("--nested")
    if udid:
        cmd.extend(["--udid", udid])

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        tree_data = json.loads(result.stdout)

        # IDB returns array format, extract first element (root)
        if isinstance(tree_data, list) and len(tree_data) > 0:
            return tree_data[0]
        return tree_data
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to get accessibility tree: {e.stderr}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: Invalid JSON from idb", file=sys.stderr)
        sys.exit(1)


def flatten_tree(node: dict, depth: int = 0, elements: list[dict] | None = None) -> list[dict]:
    """
    Flatten nested accessibility tree into list of elements.

    Converts the hierarchical accessibility tree into a flat list where each
    element includes its depth for context.

    Used by:
    - navigator.py - Element finding
    - screen_mapper.py - Element analysis
    - accessibility_audit.py - Audit scanning

    Args:
        node: Root node of tree (typically from get_accessibility_tree)
        depth: Current depth (used internally, start at 0)
        elements: Accumulator list (used internally, start as None)

    Returns:
        Flat list of elements, each with "depth" key indicating nesting level.
        Structure of each element: {
            "type": "Button",
            "AXLabel": "Login",
            "frame": {...},
            "depth": 2,
            ...
        }

    Example:
        tree = get_accessibility_tree()
        flat = flatten_tree(tree)
        for elem in flat:
            print(f"{'  ' * elem['depth']}{elem.get('type')}: {elem.get('AXLabel')}")
    """
    if elements is None:
        elements = []

    # Add current node with depth tracking
    node_copy = node.copy()
    node_copy["depth"] = depth
    elements.append(node_copy)

    # Process children recursively
    for child in node.get("children", []):
        flatten_tree(child, depth + 1, elements)

    return elements


def count_elements(node: dict) -> int:
    """
    Count total elements in tree (recursive).

    Traverses entire tree counting all elements for reporting purposes.

    Used by:
    - test_recorder.py - Element counting per step
    - screen_mapper.py - Summary statistics

    Args:
        node: Root node of tree

    Returns:
        Total element count including root and all descendants

    Example:
        tree = get_accessibility_tree()
        total = count_elements(tree)
        print(f"Screen has {total} elements")
    """
    count = 1
    for child in node.get("children", []):
        count += count_elements(child)
    return count


def get_screen_size(udid: str | None = None) -> tuple[int, int]:
    """
    Get screen dimensions from accessibility tree.

    Extracts the screen size from the root element's frame. Useful for
    gesture calculations and coordinate normalization.

    Used by:
    - gesture.py - Gesture positioning
    - Potentially: screenshot positioning, screen-aware scaling

    Args:
        udid: Device UDID (uses booted if None)

    Returns:
        (width, height) tuple. Defaults to (390, 844) if detection fails
        or tree cannot be accessed.

    Example:
        width, height = get_screen_size()
        center_x = width // 2
        center_y = height // 2
    """
    DEFAULT_WIDTH = 390  # iPhone 14
    DEFAULT_HEIGHT = 844

    try:
        tree = get_accessibility_tree(udid, nested=False)
        frame = tree.get("frame", {})
        width = int(frame.get("width", DEFAULT_WIDTH))
        height = int(frame.get("height", DEFAULT_HEIGHT))
        return (width, height)
    except Exception:
        # Silently fall back to defaults if tree access fails
        return (DEFAULT_WIDTH, DEFAULT_HEIGHT)
```

## File: `ios-simulator-skill/scripts/common/screenshot_utils.py`
```python
#!/usr/bin/env python3
"""
Screenshot utilities with dual-mode support.

Provides unified screenshot handling with:
- File-based mode: Persistent artifacts for test documentation
- Inline base64 mode: Vision-based automation for agent analysis
- Size presets: Token optimization (full/half/quarter/thumb)
- Semantic naming: {appName}_{screenName}_{state}_{timestamp}.png

Supports resize operations via PIL (optional dependency).

Used by:
- test_recorder.py - Step-based screenshot recording
- app_state_capture.py - State snapshot captures
"""

import base64
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

# Try to import PIL for resizing, but make it optional
try:
    from PIL import Image

    HAS_PIL = True
except ImportError:
    HAS_PIL = False


def generate_screenshot_name(
    app_name: str | None = None,
    screen_name: str | None = None,
    state: str | None = None,
    timestamp: str | None = None,
    extension: str = "png",
) -> str:
    """Generate semantic screenshot filename.

    Format: {appName}_{screenName}_{state}_{timestamp}.{ext}
    Falls back to: screenshot_{timestamp}.{ext}

    Args:
        app_name: Application name (e.g., 'MyApp')
        screen_name: Screen name (e.g., 'Login')
        state: State description (e.g., 'Empty', 'Filled', 'Error')
        timestamp: ISO timestamp (uses current time if None)
        extension: File extension (default: 'png')

    Returns:
        Semantic filename ready for safe file creation

    Example:
        name = generate_screenshot_name('MyApp', 'Login', 'Empty')
        # Returns: 'MyApp_Login_Empty_20251028-143052.png'

        name = generate_screenshot_name()
        # Returns: 'screenshot_20251028-143052.png'
    """
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    # Build semantic name
    if app_name or screen_name or state:
        parts = [app_name, screen_name, state]
        parts = [p for p in parts if p]  # Filter None/empty
        name = "_".join(parts) + f"_{timestamp}"
    else:
        name = f"screenshot_{timestamp}"

    return f"{name}.{extension}"


def get_size_preset(size: str = "half") -> tuple[float, float]:
    """Get scale factors for size preset.

    Args:
        size: 'full', 'half', 'quarter', 'thumb'

    Returns:
        Tuple of (scale_x, scale_y) for resizing

    Example:
        scale_x, scale_y = get_size_preset('half')
        # Returns: (0.5, 0.5)
    """
    presets = {
        "full": (1.0, 1.0),
        "half": (0.5, 0.5),
        "quarter": (0.25, 0.25),
        "thumb": (0.1, 0.1),
    }
    return presets.get(size, (0.5, 0.5))


def resize_screenshot(
    input_path: str,
    output_path: str | None = None,
    size: str = "half",
    quality: int = 85,
) -> tuple[str, int, int]:
    """Resize screenshot for token optimization.

    Requires PIL (Pillow). Falls back gracefully without it.

    Args:
        input_path: Path to original screenshot
        output_path: Output path (uses input_path if None)
        size: 'full', 'half', 'quarter', 'thumb'
        quality: JPEG quality (1-100, default: 85)

    Returns:
        Tuple of (output_path, width, height) of resized image

    Raises:
        FileNotFoundError: If input file doesn't exist
        ValueError: If PIL not installed and size != 'full'

    Example:
        output, w, h = resize_screenshot(
            'screenshot.png',
            'screenshot_half.png',
            'half'
        )
        print(f"Resized to {w}x{h}")
    """
    input_file = Path(input_path)
    if not input_file.exists():
        raise FileNotFoundError(f"Screenshot not found: {input_path}")

    # If full size, just copy
    if size == "full":
        if output_path:
            import shutil

            shutil.copy(input_path, output_path)
            output_file = Path(output_path)
        else:
            output_file = input_file

        # Get original dimensions
        if HAS_PIL:
            img = Image.open(str(output_file))
            return (str(output_file), img.width, img.height)
        return (str(output_file), 0, 0)  # Dimensions unknown without PIL

    # Need PIL to resize
    if not HAS_PIL:
        raise ValueError(
            f"Size preset '{size}' requires PIL (Pillow). " "Install with: pip3 install pillow"
        )

    # Open original image
    img = Image.open(str(input_file))
    orig_w, orig_h = img.size

    # Calculate new size
    scale_x, scale_y = get_size_preset(size)
    new_w = int(orig_w * scale_x)
    new_h = int(orig_h * scale_y)

    # Resize with high-quality resampling
    resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)

    # Determine output path
    if output_path is None:
        # Insert size marker before extension
        stem = input_file.stem
        suffix = input_file.suffix
        output_path = str(input_file.parent / f"{stem}_{size}{suffix}")

    # Save resized image
    resized.save(output_path, quality=quality, optimize=True)

    return (output_path, new_w, new_h)


def capture_screenshot(
    udid: str,
    output_path: str | None = None,
    size: str = "half",
    inline: bool = False,
    app_name: str | None = None,
    screen_name: str | None = None,
    state: str | None = None,
) -> dict[str, Any]:
    """Capture screenshot with flexible output modes.

    Supports both file-based (persistent artifacts) and inline base64 modes
    (for vision-based automation).

    Args:
        udid: Device UDID
        output_path: File path for file mode (generates semantic name if None)
        size: 'full', 'half', 'quarter', 'thumb' (default: 'half')
        inline: If True, returns base64 data instead of saving to file
        app_name: App name for semantic naming
        screen_name: Screen name for semantic naming
        state: State description for semantic naming

    Returns:
        Dict with mode-specific fields:

        File mode:
        {
            'mode': 'file',
            'file_path': str,
            'size_bytes': int,
            'width': int,
            'height': int,
            'size_preset': str
        }

        Inline mode:
        {
            'mode': 'inline',
            'base64_data': str,
            'mime_type': 'image/png',
            'width': int,
            'height': int,
            'size_preset': str
        }

    Example:
        # File mode
        result = capture_screenshot('ABC123', app_name='MyApp')
        print(f"Saved to: {result['file_path']}")

        # Inline mode
        result = capture_screenshot('ABC123', inline=True, size='half')
        print(f"Screenshot: {result['width']}x{result['height']}")
        print(f"Base64: {result['base64_data'][:50]}...")
    """
    try:
        # Capture raw screenshot to temp file
        temp_path = "/tmp/ios_simulator_screenshot.png"
        cmd = ["xcrun", "simctl", "io", udid, "screenshot", temp_path]

        subprocess.run(cmd, capture_output=True, text=True, check=True)

        if inline:
            # Inline mode: resize and convert to base64
            # Resize if needed
            if size != "full" and HAS_PIL:
                resized_path, width, height = resize_screenshot(temp_path, size=size)
            else:
                resized_path = temp_path
                # Get dimensions via PIL if available
                if HAS_PIL:
                    img = Image.open(resized_path)
                    width, height = img.size
                else:
                    width, height = 390, 844  # Fallback to common device size

            # Read and encode as base64
            with open(resized_path, "rb") as f:
                base64_data = base64.b64encode(f.read()).decode("utf-8")

            # Clean up temp files
            Path(temp_path).unlink(missing_ok=True)
            if resized_path != temp_path:
                Path(resized_path).unlink(missing_ok=True)

            return {
                "mode": "inline",
                "base64_data": base64_data,
                "mime_type": "image/png",
                "width": width,
                "height": height,
                "size_preset": size,
            }

        # File mode: save to output path with semantic naming
        if output_path is None:
            output_path = generate_screenshot_name(app_name, screen_name, state)

        # Resize if needed
        if size != "full" and HAS_PIL:
            final_path, width, height = resize_screenshot(temp_path, output_path, size)
        else:
            # Just move temp to output
            import shutil

            shutil.move(temp_path, output_path)
            final_path = output_path

            # Get dimensions via PIL if available
            if HAS_PIL:
                img = Image.open(final_path)
                width, height = img.size
            else:
                width, height = 390, 844  # Fallback

        # Get file size
        size_bytes = Path(final_path).stat().st_size

        return {
            "mode": "file",
            "file_path": final_path,
            "size_bytes": size_bytes,
            "width": width,
            "height": height,
            "size_preset": size,
        }

    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to capture screenshot: {e.stderr}") from e
    except Exception as e:
        raise RuntimeError(f"Screenshot capture error: {e!s}") from e


def format_screenshot_result(result: dict[str, Any]) -> str:
    """Format screenshot result for human-readable output.

    Args:
        result: Result dictionary from capture_screenshot()

    Returns:
        Formatted string for printing

    Example:
        result = capture_screenshot('ABC123', inline=True)
        print(format_screenshot_result(result))
    """
    if result["mode"] == "file":
        return (
            f"Screenshot: {result['file_path']}\n"
            f"Dimensions: {result['width']}x{result['height']}\n"
            f"Size: {result['size_bytes']} bytes"
        )
    return (
        f"Screenshot (inline): {result['width']}x{result['height']}\n"
        f"Base64 length: {len(result['base64_data'])} chars"
    )
```

## File: `ios-simulator-skill/scripts/xcode/__init__.py`
```python
"""
Xcode build automation module.

Provides structured, modular access to xcodebuild and xcresult functionality.
"""

from .builder import BuildRunner
from .cache import XCResultCache
from .config import Config
from .reporter import OutputFormatter
from .xcresult import XCResultParser

__all__ = ["BuildRunner", "Config", "OutputFormatter", "XCResultCache", "XCResultParser"]
```

## File: `ios-simulator-skill/scripts/xcode/builder.py`
```python
"""
Xcode build execution.

Handles xcodebuild command construction and execution with xcresult generation.
"""

import re
import subprocess
import sys
from pathlib import Path

from .cache import XCResultCache
from .config import Config


class BuildRunner:
    """
    Execute xcodebuild commands with xcresult bundle generation.

    Handles scheme auto-detection, command construction, and build/test execution.
    """

    def __init__(
        self,
        project_path: str | None = None,
        workspace_path: str | None = None,
        scheme: str | None = None,
        configuration: str = "Debug",
        simulator: str | None = None,
        cache: XCResultCache | None = None,
    ):
        """
        Initialize build runner.

        Args:
            project_path: Path to .xcodeproj
            workspace_path: Path to .xcworkspace
            scheme: Build scheme (auto-detected if not provided)
            configuration: Build configuration (Debug/Release)
            simulator: Simulator name
            cache: XCResult cache (creates default if not provided)
        """
        self.project_path = project_path
        self.workspace_path = workspace_path
        self.scheme = scheme
        self.configuration = configuration
        self.simulator = simulator
        self.cache = cache or XCResultCache()

    def auto_detect_scheme(self) -> str | None:
        """
        Auto-detect build scheme from project/workspace.

        Returns:
            Detected scheme name or None
        """
        cmd = ["xcodebuild", "-list"]

        if self.workspace_path:
            cmd.extend(["-workspace", self.workspace_path])
        elif self.project_path:
            cmd.extend(["-project", self.project_path])
        else:
            return None

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)

            # Parse schemes from output
            in_schemes_section = False
            for line in result.stdout.split("\n"):
                line = line.strip()

                if "Schemes:" in line:
                    in_schemes_section = True
                    continue

                if in_schemes_section and line and not line.startswith("Build"):
                    # First scheme in list
                    return line

        except subprocess.CalledProcessError as e:
            print(f"Error auto-detecting scheme: {e}", file=sys.stderr)

        return None

    def get_simulator_destination(self) -> str:
        """
        Get xcodebuild destination string.

        Uses config preferences with fallback to auto-detection.

        Priority:
            1. --simulator CLI flag (self.simulator)
            2. Config preferred_simulator
            3. Config last_used_simulator
            4. Auto-detect first iPhone
            5. Generic iOS Simulator

        Returns:
            Destination string for -destination flag
        """
        # Priority 1: CLI flag
        if self.simulator:
            return f"platform=iOS Simulator,name={self.simulator}"

        # Priority 2-3: Config preferences
        try:
            # Determine project directory from project/workspace path
            project_dir = None
            if self.project_path:
                project_dir = Path(self.project_path).parent
            elif self.workspace_path:
                project_dir = Path(self.workspace_path).parent

            config = Config.load(project_dir=project_dir)
            preferred = config.get_preferred_simulator()

            if preferred:
                # Check if preferred simulator exists
                if self._simulator_exists(preferred):
                    return f"platform=iOS Simulator,name={preferred}"
                print(f"Warning: Preferred simulator '{preferred}' not available", file=sys.stderr)
                if config.should_fallback_to_any_iphone():
                    print("Falling back to auto-detection...", file=sys.stderr)
                else:
                    # Strict mode: don't fallback
                    return f"platform=iOS Simulator,name={preferred}"

        except Exception as e:
            print(f"Warning: Could not load config: {e}", file=sys.stderr)

        # Priority 4-5: Auto-detect
        return self._auto_detect_simulator()

    def _simulator_exists(self, name: str) -> bool:
        """
        Check if simulator with given name exists and is available.

        Args:
            name: Simulator name (e.g., "iPhone 16 Pro")

        Returns:
            True if simulator exists and is available
        """
        try:
            result = subprocess.run(
                ["xcrun", "simctl", "list", "devices", "available", "iOS"],
                capture_output=True,
                text=True,
                check=True,
            )

            # Check if simulator name appears in available devices
            return any(name in line and "(" in line for line in result.stdout.split("\n"))

        except subprocess.CalledProcessError:
            return False

    def _extract_simulator_name_from_destination(self, destination: str) -> str | None:
        """
        Extract simulator name from destination string.

        Args:
            destination: Destination string (e.g., "platform=iOS Simulator,name=iPhone 16 Pro")

        Returns:
            Simulator name or None
        """
        # Pattern: name=<simulator name>
        match = re.search(r"name=([^,]+)", destination)
        if match:
            return match.group(1).strip()
        return None

    def _auto_detect_simulator(self) -> str:
        """
        Auto-detect best available iOS simulator.

        Returns:
            Destination string for -destination flag
        """
        try:
            result = subprocess.run(
                ["xcrun", "simctl", "list", "devices", "available", "iOS"],
                capture_output=True,
                text=True,
                check=True,
            )

            # Parse available simulators, prefer latest iPhone
            # Looking for lines like: "iPhone 16 Pro (12345678-1234-1234-1234-123456789012) (Shutdown)"
            for line in result.stdout.split("\n"):
                if "iPhone" in line and "(" in line:
                    # Extract device name
                    name = line.split("(")[0].strip()
                    if name:
                        return f"platform=iOS Simulator,name={name}"

            # Fallback to generic iOS Simulator if no iPhone found
            return "generic/platform=iOS Simulator"

        except subprocess.CalledProcessError as e:
            print(f"Warning: Could not auto-detect simulator: {e}", file=sys.stderr)
            return "generic/platform=iOS Simulator"

    def build(self, clean: bool = False) -> tuple[bool, str, str]:
        """
        Build the project.

        Args:
            clean: Perform clean build

        Returns:
            Tuple of (success: bool, xcresult_id: str, stderr: str)
        """
        # Auto-detect scheme if needed
        if not self.scheme:
            self.scheme = self.auto_detect_scheme()
            if not self.scheme:
                print("Error: Could not auto-detect scheme. Use --scheme", file=sys.stderr)
                return (False, "", "")

        # Generate xcresult ID and path
        xcresult_id = self.cache.generate_id()
        xcresult_path = self.cache.get_path(xcresult_id)

        # Build command
        cmd = ["xcodebuild", "-quiet"]  # Suppress verbose output

        if clean:
            cmd.append("clean")

        cmd.append("build")

        if self.workspace_path:
            cmd.extend(["-workspace", self.workspace_path])
        elif self.project_path:
            cmd.extend(["-project", self.project_path])
        else:
            print("Error: No project or workspace specified", file=sys.stderr)
            return (False, "", "")

        cmd.extend(
            [
                "-scheme",
                self.scheme,
                "-configuration",
                self.configuration,
                "-destination",
                self.get_simulator_destination(),
                "-resultBundlePath",
                str(xcresult_path),
            ]
        )

        # Execute build
        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True, check=False  # Don't raise on non-zero exit
            )

            success = result.returncode == 0

            # xcresult bundle should be created even on failure
            if not xcresult_path.exists():
                print("Warning: xcresult bundle was not created", file=sys.stderr)
                return (success, "", result.stderr)

            # Auto-update config with last used simulator (on success only)
            if success:
                try:
                    # Determine project directory from project/workspace path
                    project_dir = None
                    if self.project_path:
                        project_dir = Path(self.project_path).parent
                    elif self.workspace_path:
                        project_dir = Path(self.workspace_path).parent

                    config = Config.load(project_dir=project_dir)
                    destination = self.get_simulator_destination()
                    simulator_name = self._extract_simulator_name_from_destination(destination)

                    if simulator_name:
                        config.update_last_used_simulator(simulator_name)
                        config.save()

                except Exception as e:
                    # Don't fail build if config update fails
                    print(f"Warning: Could not update config: {e}", file=sys.stderr)

            return (success, xcresult_id, result.stderr)

        except Exception as e:
            print(f"Error executing build: {e}", file=sys.stderr)
            return (False, "", str(e))

    def test(self, test_suite: str | None = None) -> tuple[bool, str, str]:
        """
        Run tests.

        Args:
            test_suite: Specific test suite to run

        Returns:
            Tuple of (success: bool, xcresult_id: str, stderr: str)
        """
        # Auto-detect scheme if needed
        if not self.scheme:
            self.scheme = self.auto_detect_scheme()
            if not self.scheme:
                print("Error: Could not auto-detect scheme. Use --scheme", file=sys.stderr)
                return (False, "", "")

        # Generate xcresult ID and path
        xcresult_id = self.cache.generate_id()
        xcresult_path = self.cache.get_path(xcresult_id)

        # Build command
        cmd = ["xcodebuild", "-quiet", "test"]

        if self.workspace_path:
            cmd.extend(["-workspace", self.workspace_path])
        elif self.project_path:
            cmd.extend(["-project", self.project_path])
        else:
            print("Error: No project or workspace specified", file=sys.stderr)
            return (False, "", "")

        cmd.extend(
            [
                "-scheme",
                self.scheme,
                "-destination",
                self.get_simulator_destination(),
                "-resultBundlePath",
                str(xcresult_path),
            ]
        )

        if test_suite:
            cmd.extend(["-only-testing", test_suite])

        # Execute tests
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=False)

            success = result.returncode == 0

            # xcresult bundle should be created even on failure
            if not xcresult_path.exists():
                print("Warning: xcresult bundle was not created", file=sys.stderr)
                return (success, "", result.stderr)

            # Auto-update config with last used simulator (on success only)
            if success:
                try:
                    # Determine project directory from project/workspace path
                    project_dir = None
                    if self.project_path:
                        project_dir = Path(self.project_path).parent
                    elif self.workspace_path:
                        project_dir = Path(self.workspace_path).parent

                    config = Config.load(project_dir=project_dir)
                    destination = self.get_simulator_destination()
                    simulator_name = self._extract_simulator_name_from_destination(destination)

                    if simulator_name:
                        config.update_last_used_simulator(simulator_name)
                        config.save()

                except Exception as e:
                    # Don't fail test if config update fails
                    print(f"Warning: Could not update config: {e}", file=sys.stderr)

            return (success, xcresult_id, result.stderr)

        except Exception as e:
            print(f"Error executing tests: {e}", file=sys.stderr)
            return (False, "", str(e))
```

## File: `ios-simulator-skill/scripts/xcode/cache.py`
```python
"""
XCResult cache management.

Handles storage, retrieval, and lifecycle of xcresult bundles for progressive disclosure.
"""

import shutil
from datetime import datetime
from pathlib import Path


class XCResultCache:
    """
    Manage xcresult bundle cache for progressive disclosure.

    Stores xcresult bundles with timestamp-based IDs and provides
    retrieval and cleanup operations.
    """

    # Default cache directory
    DEFAULT_CACHE_DIR = Path.home() / ".ios-simulator-skill" / "xcresults"

    def __init__(self, cache_dir: Path | None = None):
        """
        Initialize cache manager.

        Args:
            cache_dir: Custom cache directory (uses default if not specified)
        """
        self.cache_dir = cache_dir or self.DEFAULT_CACHE_DIR
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def generate_id(self, prefix: str = "xcresult") -> str:
        """
        Generate timestamped xcresult ID.

        Args:
            prefix: ID prefix (default: "xcresult")

        Returns:
            ID string like "xcresult-20251018-143052"
        """
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        return f"{prefix}-{timestamp}"

    def get_path(self, xcresult_id: str) -> Path:
        """
        Get full path for xcresult ID.

        Args:
            xcresult_id: XCResult ID

        Returns:
            Path to xcresult bundle
        """
        # Handle both with and without .xcresult extension
        if xcresult_id.endswith(".xcresult"):
            return self.cache_dir / xcresult_id
        return self.cache_dir / f"{xcresult_id}.xcresult"

    def exists(self, xcresult_id: str) -> bool:
        """
        Check if xcresult bundle exists.

        Args:
            xcresult_id: XCResult ID

        Returns:
            True if bundle exists
        """
        return self.get_path(xcresult_id).exists()

    def save(self, source_path: Path, xcresult_id: str | None = None) -> str:
        """
        Save xcresult bundle to cache.

        Args:
            source_path: Source xcresult bundle path
            xcresult_id: Optional custom ID (generates if not provided)

        Returns:
            xcresult ID
        """
        if not source_path.exists():
            raise FileNotFoundError(f"Source xcresult not found: {source_path}")

        # Generate ID if not provided
        if not xcresult_id:
            xcresult_id = self.generate_id()

        # Get destination path
        dest_path = self.get_path(xcresult_id)

        # Copy xcresult bundle (it's a directory)
        if dest_path.exists():
            shutil.rmtree(dest_path)

        shutil.copytree(source_path, dest_path)

        return xcresult_id

    def list(self, limit: int = 10) -> list[dict]:
        """
        List recent xcresult bundles.

        Args:
            limit: Maximum number to return

        Returns:
            List of xcresult metadata dicts
        """
        if not self.cache_dir.exists():
            return []

        results = []
        for path in sorted(
            self.cache_dir.glob("*.xcresult"), key=lambda p: p.stat().st_mtime, reverse=True
        )[:limit]:
            # Calculate bundle size
            size_bytes = sum(f.stat().st_size for f in path.rglob("*") if f.is_file())

            results.append(
                {
                    "id": path.stem,
                    "path": str(path),
                    "created": datetime.fromtimestamp(path.stat().st_mtime).isoformat(),
                    "size_mb": round(size_bytes / (1024 * 1024), 2),
                }
            )

        return results

    def cleanup(self, keep_recent: int = 20) -> int:
        """
        Clean up old xcresult bundles.

        Args:
            keep_recent: Number of recent bundles to keep

        Returns:
            Number of bundles removed
        """
        if not self.cache_dir.exists():
            return 0

        # Get all bundles sorted by modification time
        all_bundles = sorted(
            self.cache_dir.glob("*.xcresult"), key=lambda p: p.stat().st_mtime, reverse=True
        )

        # Remove old bundles
        removed = 0
        for bundle_path in all_bundles[keep_recent:]:
            shutil.rmtree(bundle_path)
            removed += 1

        return removed

    def get_size_mb(self, xcresult_id: str) -> float:
        """
        Get size of xcresult bundle in MB.

        Args:
            xcresult_id: XCResult ID

        Returns:
            Size in MB
        """
        path = self.get_path(xcresult_id)
        if not path.exists():
            return 0.0

        size_bytes = sum(f.stat().st_size for f in path.rglob("*") if f.is_file())
        return round(size_bytes / (1024 * 1024), 2)

    def save_stderr(self, xcresult_id: str, stderr: str) -> None:
        """
        Save stderr output alongside xcresult bundle.

        Args:
            xcresult_id: XCResult ID
            stderr: stderr output from xcodebuild
        """
        if not stderr:
            return

        stderr_path = self.cache_dir / f"{xcresult_id}.stderr"
        stderr_path.write_text(stderr, encoding="utf-8")

    def get_stderr(self, xcresult_id: str) -> str:
        """
        Retrieve cached stderr output.

        Args:
            xcresult_id: XCResult ID

        Returns:
            stderr content or empty string if not found
        """
        stderr_path = self.cache_dir / f"{xcresult_id}.stderr"
        if not stderr_path.exists():
            return ""

        return stderr_path.read_text(encoding="utf-8")
```

## File: `ios-simulator-skill/scripts/xcode/config.py`
```python
"""
Configuration management for iOS Simulator Skill.

Handles loading, validation, and auto-updating of project-local config files.
"""

import json
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


class Config:
    """
    Project-local configuration with auto-learning.

    Config file location: .claude/skills/<skill-directory-name>/config.json

    The skill directory name is auto-detected from the installation location,
    so configs work regardless of what users name the skill directory.

    Auto-updates last_used_simulator after successful builds.
    """

    DEFAULT_CONFIG = {
        "device": {
            "preferred_simulator": None,
            "preferred_os_version": None,
            "fallback_to_any_iphone": True,
            "last_used_simulator": None,
            "last_used_at": None,
        }
    }

    def __init__(self, data: dict[str, Any], config_path: Path):
        """
        Initialize config.

        Args:
            data: Config data dict
            config_path: Path to config file
        """
        self.data = data
        self.config_path = config_path

    @staticmethod
    def load(project_dir: Path | None = None) -> "Config":
        """
        Load config from project directory.

        Args:
            project_dir: Project root (defaults to cwd)

        Returns:
            Config instance (creates default if not found)

        Note:
            The skill directory name is auto-detected from the installation location,
            so configs work regardless of what users name the skill directory.
        """
        if project_dir is None:
            project_dir = Path.cwd()

        # Auto-detect skill directory name from actual installation location
        # This file is at: skill/scripts/xcode/config.py
        # Navigate up to skill/ directory and use its name
        skill_root = Path(__file__).parent.parent.parent  # xcode/ -> scripts/ -> skill/
        skill_name = skill_root.name

        config_path = project_dir / ".claude" / "skills" / skill_name / "config.json"

        # Load existing config
        if config_path.exists():
            try:
                with open(config_path) as f:
                    data = json.load(f)

                # Merge with defaults (in case new fields added)
                merged = Config._merge_with_defaults(data)
                return Config(merged, config_path)

            except json.JSONDecodeError as e:
                print(f"Warning: Invalid JSON in {config_path}: {e}", file=sys.stderr)
                print("Using default config", file=sys.stderr)
                return Config(Config.DEFAULT_CONFIG.copy(), config_path)
            except Exception as e:
                print(f"Warning: Could not load config: {e}", file=sys.stderr)
                return Config(Config.DEFAULT_CONFIG.copy(), config_path)

        # Return default config (will be created on first save)
        return Config(Config.DEFAULT_CONFIG.copy(), config_path)

    @staticmethod
    def _merge_with_defaults(data: dict[str, Any]) -> dict[str, Any]:
        """
        Merge user config with defaults.

        Args:
            data: User config data

        Returns:
            Merged config with all default fields
        """
        merged = Config.DEFAULT_CONFIG.copy()

        # Deep merge device section
        if "device" in data:
            merged["device"].update(data["device"])

        return merged

    def save(self) -> None:
        """
        Save config to file atomically.

        Uses temp file + rename for atomic writes.
        Creates parent directories if needed.
        """
        try:
            # Create parent directories
            self.config_path.parent.mkdir(parents=True, exist_ok=True)

            # Atomic write: temp file + rename
            temp_path = self.config_path.with_suffix(".tmp")

            with open(temp_path, "w") as f:
                json.dump(self.data, f, indent=2)
                f.write("\n")  # Trailing newline

            # Atomic rename
            temp_path.replace(self.config_path)

        except Exception as e:
            print(f"Warning: Could not save config: {e}", file=sys.stderr)

    def update_last_used_simulator(self, name: str) -> None:
        """
        Update last used simulator and timestamp.

        Args:
            name: Simulator name (e.g., "iPhone 16 Pro")
        """
        self.data["device"]["last_used_simulator"] = name
        self.data["device"]["last_used_at"] = datetime.now(UTC).isoformat()

    def get_preferred_simulator(self) -> str | None:
        """
        Get preferred simulator.

        Returns:
            Simulator name or None

        Priority:
            1. preferred_simulator (manual preference)
            2. last_used_simulator (auto-learned)
            3. None (use auto-detection)
        """
        device = self.data.get("device", {})

        # Manual preference takes priority
        if device.get("preferred_simulator"):
            return device["preferred_simulator"]

        # Auto-learned preference
        if device.get("last_used_simulator"):
            return device["last_used_simulator"]

        return None

    def should_fallback_to_any_iphone(self) -> bool:
        """
        Check if fallback to any iPhone is enabled.

        Returns:
            True if should fallback, False otherwise
        """
        return self.data.get("device", {}).get("fallback_to_any_iphone", True)
```

## File: `ios-simulator-skill/scripts/xcode/reporter.py`
```python
"""
Build/test output formatting.

Provides multiple output formats with progressive disclosure support.
"""

import json


class OutputFormatter:
    """
    Format build/test results for display.

    Supports ultra-minimal default output, verbose mode, and JSON output.
    """

    @staticmethod
    def format_minimal(
        status: str,
        error_count: int,
        warning_count: int,
        xcresult_id: str,
        test_info: dict | None = None,
        hints: list[str] | None = None,
        errors: list[dict] | None = None,
        failed_tests: list[dict] | None = None,
    ) -> str:
        """
        Format ultra-minimal output (5-10 tokens on success, more on failure).

        On failure, automatically surfaces top errors/failed tests inline so agents
        don't need a second round-trip with --get-errors.

        Args:
            status: Build status (SUCCESS/FAILED)
            error_count: Number of errors
            warning_count: Number of warnings
            xcresult_id: XCResult bundle ID
            test_info: Optional test results dict
            hints: Optional list of actionable hints
            errors: Optional error list to surface on failure
            failed_tests: Optional failed test list to surface on failure

        Returns:
            Minimal formatted string
        """
        lines = []

        if test_info:
            # Test mode
            total = test_info.get("total", 0)
            passed = test_info.get("passed", 0)
            failed = test_info.get("failed", 0)
            duration = test_info.get("duration", 0.0)

            test_status = "PASS" if failed == 0 else "FAIL"
            lines.append(
                f"Tests: {test_status} ({passed}/{total} passed, {duration:.1f}s) [{xcresult_id}]"
            )
        else:
            # Build mode
            lines.append(
                f"Build: {status} ({error_count} errors, {warning_count} warnings) [{xcresult_id}]"
            )

        # Surface errors inline on failure
        if status == "FAILED" and errors:
            lines.append("")
            lines.append(OutputFormatter.format_errors(errors, limit=5))

        # Surface failed tests inline on failure
        if failed_tests:
            lines.append("")
            lines.append(OutputFormatter.format_test_failures(failed_tests, limit=5))

        # Add hints if provided and build failed
        if hints and status == "FAILED":
            lines.append("")
            lines.extend(hints)

        return "\n".join(lines)

    @staticmethod
    def format_test_failures(failed_tests: list[dict], limit: int = 5) -> str:
        """
        Format failed test details.

        Args:
            failed_tests: List of dicts with test_name and failure_message
            limit: Maximum failures to show

        Returns:
            Formatted failure list
        """
        if not failed_tests:
            return "No test failures found."

        lines = [f"Failed tests ({len(failed_tests)}):"]
        lines.append("")

        for i, test in enumerate(failed_tests[:limit], 1):
            name = test.get("test_name", "Unknown")
            message = test.get("failure_message", "")
            lines.append(f"{i}. {name}")
            if message:
                lines.append(f"   {message}")
            lines.append("")

        if len(failed_tests) > limit:
            lines.append(f"... and {len(failed_tests) - limit} more failures")

        return "\n".join(lines)

    @staticmethod
    def format_errors(errors: list[dict], limit: int = 10) -> str:
        """
        Format error details.

        Args:
            errors: List of error dicts
            limit: Maximum errors to show

        Returns:
            Formatted error list
        """
        if not errors:
            return "No errors found."

        lines = [f"Errors ({len(errors)}):"]
        lines.append("")

        for i, error in enumerate(errors[:limit], 1):
            message = error.get("message", "Unknown error")
            location = error.get("location", {})

            # Format location
            loc_parts = []
            if location.get("file"):
                file_path = location["file"].replace("file://", "")
                loc_parts.append(file_path)
            if location.get("line"):
                loc_parts.append(f"line {location['line']}")

            location_str = ":".join(loc_parts) if loc_parts else "unknown location"

            lines.append(f"{i}. {message}")
            lines.append(f"   Location: {location_str}")
            lines.append("")

        if len(errors) > limit:
            lines.append(f"... and {len(errors) - limit} more errors")

        return "\n".join(lines)

    @staticmethod
    def format_warnings(warnings: list[dict], limit: int = 10) -> str:
        """
        Format warning details.

        Args:
            warnings: List of warning dicts
            limit: Maximum warnings to show

        Returns:
            Formatted warning list
        """
        if not warnings:
            return "No warnings found."

        lines = [f"Warnings ({len(warnings)}):"]
        lines.append("")

        for i, warning in enumerate(warnings[:limit], 1):
            message = warning.get("message", "Unknown warning")
            location = warning.get("location", {})

            # Format location
            loc_parts = []
            if location.get("file"):
                file_path = location["file"].replace("file://", "")
                loc_parts.append(file_path)
            if location.get("line"):
                loc_parts.append(f"line {location['line']}")

            location_str = ":".join(loc_parts) if loc_parts else "unknown location"

            lines.append(f"{i}. {message}")
            lines.append(f"   Location: {location_str}")
            lines.append("")

        if len(warnings) > limit:
            lines.append(f"... and {len(warnings) - limit} more warnings")

        return "\n".join(lines)

    @staticmethod
    def format_log(log: str, lines: int = 50) -> str:
        """
        Format build log (show last N lines).

        Args:
            log: Full build log
            lines: Number of lines to show

        Returns:
            Formatted log excerpt
        """
        if not log:
            return "No build log available."

        log_lines = log.strip().split("\n")

        if len(log_lines) <= lines:
            return log

        # Show last N lines
        excerpt = log_lines[-lines:]
        return f"... (showing last {lines} lines of {len(log_lines)})\n\n" + "\n".join(excerpt)

    @staticmethod
    def format_json(data: dict) -> str:
        """
        Format data as JSON.

        Args:
            data: Data to format

        Returns:
            Pretty-printed JSON string
        """
        return json.dumps(data, indent=2)

    @staticmethod
    def generate_hints(errors: list[dict]) -> list[str]:
        """
        Generate actionable hints based on error types.

        Args:
            errors: List of error dicts

        Returns:
            List of hint strings
        """
        hints = []
        error_types: set[str] = set()

        # Collect error types
        for error in errors:
            error_type = error.get("type", "unknown")
            error_types.add(error_type)

        # Generate hints based on error types
        if "provisioning" in error_types:
            hints.append("Provisioning profile issue detected:")
            hints.append("  • Ensure you have a valid provisioning profile for iOS Simulator")
            hints.append(
                '  • For simulator builds, use CODE_SIGN_IDENTITY="" CODE_SIGNING_REQUIRED=NO'
            )
            hints.append("  • Or specify simulator explicitly: --simulator 'iPhone 16 Pro'")

        if "signing" in error_types:
            hints.append("Code signing issue detected:")
            hints.append("  • For simulator builds, code signing is not required")
            hints.append("  • Ensure build settings target iOS Simulator, not physical device")
            hints.append("  • Check destination: platform=iOS Simulator,name=<device>")

        if not error_types or "build" in error_types:
            # Generic hints when error type is unknown
            if any("destination" in error.get("message", "").lower() for error in errors):
                hints.append("Device selection issue detected:")
                hints.append("  • List available simulators: xcrun simctl list devices available")
                hints.append("  • Specify simulator: --simulator 'iPhone 16 Pro'")

        return hints

    @staticmethod
    def format_verbose(
        status: str,
        error_count: int,
        warning_count: int,
        xcresult_id: str,
        errors: list[dict] | None = None,
        warnings: list[dict] | None = None,
        test_info: dict | None = None,
    ) -> str:
        """
        Format verbose output with error/warning details.

        Args:
            status: Build status
            error_count: Error count
            warning_count: Warning count
            xcresult_id: XCResult ID
            errors: Optional error list
            warnings: Optional warning list
            test_info: Optional test results

        Returns:
            Verbose formatted output
        """
        lines = []

        # Header
        if test_info:
            total = test_info.get("total", 0)
            passed = test_info.get("passed", 0)
            failed = test_info.get("failed", 0)
            duration = test_info.get("duration", 0.0)

            test_status = "PASS" if failed == 0 else "FAIL"
            lines.append(f"Tests: {test_status}")
            lines.append(f"  Total: {total}")
            lines.append(f"  Passed: {passed}")
            lines.append(f"  Failed: {failed}")
            lines.append(f"  Duration: {duration:.1f}s")
        else:
            lines.append(f"Build: {status}")

        lines.append(f"XCResult: {xcresult_id}")
        lines.append("")

        # Errors
        if errors and len(errors) > 0:
            lines.append(OutputFormatter.format_errors(errors, limit=5))
            lines.append("")

        # Warnings
        if warnings and len(warnings) > 0:
            lines.append(OutputFormatter.format_warnings(warnings, limit=5))
            lines.append("")

        # Summary
        lines.append(f"Summary: {error_count} errors, {warning_count} warnings")

        return "\n".join(lines)
```

## File: `ios-simulator-skill/scripts/xcode/xcresult.py`
```python
"""
XCResult bundle parser.

Extracts structured data from xcresult bundles using xcresulttool.
"""

import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


class XCResultParser:
    """
    Parse xcresult bundles to extract build/test data.

    Uses xcresulttool to extract structured JSON data from Apple's
    xcresult bundle format.
    """

    def __init__(self, xcresult_path: Path, stderr: str = ""):
        """
        Initialize parser.

        Args:
            xcresult_path: Path to xcresult bundle
            stderr: Optional stderr output for fallback parsing
        """
        self.xcresult_path = xcresult_path
        self.stderr = stderr

        if xcresult_path and not xcresult_path.exists():
            raise FileNotFoundError(f"XCResult bundle not found: {xcresult_path}")

    def get_build_results(self) -> dict | None:
        """
        Get build results as JSON.

        Returns:
            Parsed JSON dict or None on error
        """
        return self._run_xcresulttool(["get", "build-results"])

    def get_test_results(self) -> dict | None:
        """
        Get test results summary as JSON.

        Returns:
            Parsed JSON dict or None on error
        """
        return self._run_xcresulttool(["get", "test-results", "summary"])

    def get_failed_tests(self) -> list[dict]:
        """
        Get failed test details from xcresult bundle.

        Returns:
            List of dicts with test_name and failure_message.
            Returns [] if parsing fails or no failures found.
        """
        try:
            data = self._run_xcresulttool(["get", "test-results", "tests"])
            if not data:
                return []

            failed = []
            # The structure varies by Xcode version — walk recursively
            nodes = data if isinstance(data, list) else data.get("testNodes", [])
            self._collect_failed_tests(nodes, failed)
            return failed

        except Exception as e:
            print(f"Warning: Could not parse failed tests: {e}", file=sys.stderr)
            return []

    def _collect_failed_tests(self, nodes: list, failed: list[dict]) -> None:
        """Recursively collect failed test cases from test node tree."""
        if not isinstance(nodes, list):
            return

        for node in nodes:
            if not isinstance(node, dict):
                continue

            is_test_case = node.get("nodeType") == "Test Case"
            is_failed = node.get("result") == "Failed"

            if is_test_case and is_failed:
                failed.append(
                    {
                        "test_name": node.get("name", "Unknown"),
                        "failure_message": node.get("details", ""),
                    }
                )

            # Recurse into children
            children = node.get("children", [])
            self._collect_failed_tests(children, failed)

    def get_build_log(self) -> str | None:
        """
        Get build log as plain text.

        Returns:
            Build log string or None on error
        """
        result = self._run_xcresulttool(["get", "log", "--type", "build"], parse_json=False)
        return result if result else None

    def count_issues(self) -> tuple[int, int]:
        """
        Count errors and warnings from build results.

        Returns:
            Tuple of (error_count, warning_count)
        """
        error_count = 0
        warning_count = 0

        build_results = self.get_build_results()

        if build_results:
            try:
                # Try top-level errors/warnings first (newer xcresult format)
                if "errors" in build_results and isinstance(build_results.get("errors"), list):
                    error_count = len(build_results["errors"])
                if "warnings" in build_results and isinstance(build_results.get("warnings"), list):
                    warning_count = len(build_results["warnings"])

                # If not found, try legacy format: actions[0].buildResult.issues
                if error_count == 0 and warning_count == 0:
                    actions = build_results.get("actions", {}).get("_values", [])
                    if actions:
                        build_result = actions[0].get("buildResult", {})
                        issues = build_result.get("issues", {})

                        # Count errors
                        error_summaries = issues.get("errorSummaries", {}).get("_values", [])
                        error_count = len(error_summaries)

                        # Count warnings
                        warning_summaries = issues.get("warningSummaries", {}).get("_values", [])
                        warning_count = len(warning_summaries)

            except (KeyError, IndexError, TypeError) as e:
                print(f"Warning: Could not parse issue counts from xcresult: {e}", file=sys.stderr)

        # If no errors found in xcresult but stderr available, count stderr errors
        if error_count == 0 and self.stderr:
            stderr_errors = self._parse_stderr_errors()
            error_count = len(stderr_errors)

        return (error_count, warning_count)

    def get_errors(self) -> list[dict]:
        """
        Get detailed error information.

        Returns:
            List of error dicts with message, file, line info
        """
        build_results = self.get_build_results()
        errors = []

        # Try to get errors from xcresult
        if build_results:
            try:
                # Try top-level errors first (newer xcresult format)
                if "errors" in build_results and isinstance(build_results.get("errors"), list):
                    for error in build_results["errors"]:
                        errors.append(
                            {
                                "message": error.get("message", "Unknown error"),
                                "type": error.get("issueType", "error"),
                                "location": self._extract_location_from_url(error.get("sourceURL")),
                            }
                        )

                # If not found, try legacy format: actions[0].buildResult.issues
                if not errors:
                    actions = build_results.get("actions", {}).get("_values", [])
                    if actions:
                        build_result = actions[0].get("buildResult", {})
                        issues = build_result.get("issues", {})
                        error_summaries = issues.get("errorSummaries", {}).get("_values", [])

                        for error in error_summaries:
                            errors.append(
                                {
                                    "message": error.get("message", {}).get(
                                        "_value", "Unknown error"
                                    ),
                                    "type": error.get("issueType", {}).get("_value", "error"),
                                    "location": self._extract_location(error),
                                }
                            )

            except (KeyError, IndexError, TypeError) as e:
                print(f"Warning: Could not parse errors from xcresult: {e}", file=sys.stderr)

        # If no errors found in xcresult but stderr available, parse stderr
        if not errors and self.stderr:
            errors = self._parse_stderr_errors()

        return errors

    def get_warnings(self) -> list[dict]:
        """
        Get detailed warning information.

        Returns:
            List of warning dicts with message, file, line info
        """
        build_results = self.get_build_results()
        if not build_results:
            return []

        warnings = []

        try:
            # Try top-level warnings first (newer xcresult format)
            if "warnings" in build_results and isinstance(build_results.get("warnings"), list):
                for warning in build_results["warnings"]:
                    warnings.append(
                        {
                            "message": warning.get("message", "Unknown warning"),
                            "type": warning.get("issueType", "warning"),
                            "location": self._extract_location_from_url(warning.get("sourceURL")),
                        }
                    )

            # If not found, try legacy format: actions[0].buildResult.issues
            if not warnings:
                actions = build_results.get("actions", {}).get("_values", [])
                if not actions:
                    return []

                build_result = actions[0].get("buildResult", {})
                issues = build_result.get("issues", {})
                warning_summaries = issues.get("warningSummaries", {}).get("_values", [])

                for warning in warning_summaries:
                    warnings.append(
                        {
                            "message": warning.get("message", {}).get("_value", "Unknown warning"),
                            "type": warning.get("issueType", {}).get("_value", "warning"),
                            "location": self._extract_location(warning),
                        }
                    )

        except (KeyError, IndexError, TypeError) as e:
            print(f"Warning: Could not parse warnings: {e}", file=sys.stderr)

        return warnings

    def _extract_location(self, issue: dict) -> dict:
        """
        Extract file location from issue.

        Args:
            issue: Issue dict from xcresult

        Returns:
            Location dict with file, line, column
        """
        location = {"file": None, "line": None, "column": None}

        try:
            doc_location = issue.get("documentLocationInCreatingWorkspace", {})
            location["file"] = doc_location.get("url", {}).get("_value")
            location["line"] = doc_location.get("startingLineNumber", {}).get("_value")
            location["column"] = doc_location.get("startingColumnNumber", {}).get("_value")
        except (KeyError, TypeError):
            pass

        return location

    def _extract_location_from_url(self, source_url: str | None) -> dict:
        """
        Extract file location from sourceURL (newer xcresult format).

        Args:
            source_url: Source URL like "file:///path/to/file.swift#StartingLineNumber=134&..."

        Returns:
            Location dict with file, line, column
        """
        location = {"file": None, "line": None, "column": None}

        if not source_url:
            return location

        try:
            # Split URL and fragment
            if "#" in source_url:
                file_part, fragment = source_url.split("#", 1)

                # Extract file path
                location["file"] = file_part.replace("file://", "")

                # Parse fragment parameters
                params = {}
                for param in fragment.split("&"):
                    if "=" in param:
                        key, value = param.split("=", 1)
                        params[key] = value

                # Extract line and column
                location["line"] = (
                    int(params.get("StartingLineNumber", 0)) + 1
                    if "StartingLineNumber" in params
                    else None
                )
                location["column"] = (
                    int(params.get("StartingColumnNumber", 0)) + 1
                    if "StartingColumnNumber" in params
                    else None
                )
            else:
                # No fragment, just file path
                location["file"] = source_url.replace("file://", "")

        except (ValueError, AttributeError):
            pass

        return location

    def _run_xcresulttool(self, args: list[str], parse_json: bool = True) -> Any | None:
        """
        Run xcresulttool command.

        Args:
            args: Command arguments (after 'xcresulttool')
            parse_json: Whether to parse output as JSON

        Returns:
            Parsed JSON dict, plain text, or None on error
        """
        if not self.xcresult_path:
            return None

        cmd = ["xcrun", "xcresulttool"] + args + ["--path", str(self.xcresult_path)]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)

            if parse_json:
                return json.loads(result.stdout)
            return result.stdout

        except subprocess.CalledProcessError as e:
            print(f"Error running xcresulttool: {e}", file=sys.stderr)
            print(f"stderr: {e.stderr}", file=sys.stderr)
            return None
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON from xcresulttool: {e}", file=sys.stderr)
            return None

    def _parse_stderr_errors(self) -> list[dict]:
        """
        Parse common errors from stderr output as fallback.

        Returns:
            List of error dicts parsed from stderr
        """
        errors = []

        if not self.stderr:
            return errors

        # Pattern 0: Swift/Clang compilation errors (e.g., "/path/file.swift:135:59: error: message")
        compilation_error_pattern = (
            r"^(?P<file>[^:]+):(?P<line>\d+):(?P<column>\d+):\s*error:\s*(?P<message>.+?)$"
        )
        for match in re.finditer(compilation_error_pattern, self.stderr, re.MULTILINE):
            errors.append(
                {
                    "message": match.group("message").strip(),
                    "type": "compilation",
                    "location": {
                        "file": match.group("file"),
                        "line": int(match.group("line")),
                        "column": int(match.group("column")),
                    },
                }
            )

        # Pattern 1: xcodebuild top-level errors (e.g., "xcodebuild: error: Unable to find...")
        xcodebuild_error_pattern = r"xcodebuild:\s*error:\s*(?P<message>.*?)(?:\n\n|\Z)"
        for match in re.finditer(xcodebuild_error_pattern, self.stderr, re.DOTALL):
            message = match.group("message").strip()
            # Clean up multi-line messages
            message = " ".join(line.strip() for line in message.split("\n") if line.strip())
            errors.append(
                {
                    "message": message,
                    "type": "build",
                    "location": {"file": None, "line": None, "column": None},
                }
            )

        # Pattern 2: Provisioning profile errors
        provisioning_pattern = r"error:.*?provisioning profile.*?(?:doesn't|does not|cannot).*?(?P<message>.*?)(?:\n|$)"
        for match in re.finditer(provisioning_pattern, self.stderr, re.IGNORECASE):
            errors.append(
                {
                    "message": f"Provisioning profile error: {match.group('message').strip()}",
                    "type": "provisioning",
                    "location": {"file": None, "line": None, "column": None},
                }
            )

        # Pattern 3: Code signing errors
        signing_pattern = r"error:.*?(?:code sign|signing).*?(?P<message>.*?)(?:\n|$)"
        for match in re.finditer(signing_pattern, self.stderr, re.IGNORECASE):
            errors.append(
                {
                    "message": f"Code signing error: {match.group('message').strip()}",
                    "type": "signing",
                    "location": {"file": None, "line": None, "column": None},
                }
            )

        # Pattern 4: Generic compilation errors (but not if already captured)
        if not errors:
            generic_error_pattern = r"^(?:\*\*\s)?(?:error|❌):\s*(?P<message>.*?)(?:\n|$)"
            for match in re.finditer(generic_error_pattern, self.stderr, re.MULTILINE):
                message = match.group("message").strip()
                errors.append(
                    {
                        "message": message,
                        "type": "build",
                        "location": {"file": None, "line": None, "column": None},
                    }
                )

        # Pattern 5: Specific "No profiles" error
        if "No profiles for" in self.stderr:
            no_profile_pattern = r"No profiles for '(?P<bundle_id>.*?)' were found"
            for match in re.finditer(no_profile_pattern, self.stderr):
                errors.append(
                    {
                        "message": f"No provisioning profile found for bundle ID '{match.group('bundle_id')}'",
                        "type": "provisioning",
                        "location": {"file": None, "line": None, "column": None},
                    }
                )

        return errors
```

## File: `references/accessibility_checklist.md`
```markdown
# iOS Accessibility Checklist

## Critical Rules (Must Fix)

### 1. Interactive elements need labels
**Check:** `accessibilityLabel != nil`
**Fix:** Add descriptive label

### 2. Buttons need text
**Check:** `label || value != ""`
**Fix:** Set button title or accessibilityLabel

### 3. Images need descriptions
**Check:** `isImage && accessibilityLabel`
**Fix:** Add alt text via accessibilityLabel

## Warnings (Should Fix)

### 4. Complex controls need hints
**Check:** `accessibilityHint for custom controls`
**Fix:** Explain what happens on activation

### 5. Grouped elements need containers
**Check:** `isAccessibilityElement on containers`
**Fix:** Group related elements

### 6. Text fields need placeholders
**Check:** `placeholder || accessibilityLabel`
**Fix:** Add placeholder text

## Info (Nice to Have)

### 7. Automation identifiers
**Check:** `accessibilityIdentifier != nil`
**Fix:** Add for UI testing

### 8. Trait specification
**Check:** `accessibilityTraits set correctly`
**Fix:** Use .button, .link, .header appropriately

### 9. Frame size adequate
**Check:** `frame.width >= 44 && frame.height >= 44`
**Fix:** Minimum touch target 44x44pt

## Quick Audit Command

```bash
python scripts/accessibility_audit.py
```

## iOS Code Fixes

```swift
// Label
button.accessibilityLabel = "Submit form"

// Hint
slider.accessibilityHint = "Adjusts volume"

// Identifier
view.accessibilityIdentifier = "login-button"

// Traits
label.accessibilityTraits = .header
```
```

## File: `references/idb_quick.md`
```markdown
# IDB Quick Reference

## UI Automation Commands

### ui describe-all
**Usage:** `idb ui describe-all --json --nested`
**Output:** Complete accessibility tree
**Key:** Foundation for accessibility auditing

### ui tap
**Usage:** `idb ui tap <x> <y>`
**Output:** None (success) or error

### ui swipe
**Usage:** `idb ui swipe <x1> <y1> <x2> <y2>`
**Output:** None (success) or error

### ui text
**Usage:** `idb ui text "<text>"`
**Output:** None (success) or error

### ui describe-point
**Usage:** `idb ui describe-point <x> <y> --json`
**Output:** Element at coordinates

## Other Essential Commands

### list-targets
**Usage:** `idb list-targets`
**Output:** Available simulators with UDIDs

### screenshot
**Usage:** `idb screenshot --udid <udid> output.png`
**Output:** PNG file saved

### list-apps
**Usage:** `idb list-apps --udid <udid>`
**Output:** Installed apps with bundle IDs

## Common Patterns

```bash
# Get accessibility tree
idb ui describe-all --json --nested > tree.json

# Basic interaction
idb ui tap 200 400
idb ui text "username@example.com"
idb ui tap 200 500  # Submit button
```

## Troubleshooting
See `troubleshooting.md`
```

## File: `references/simctl_quick.md`
```markdown
# simctl Quick Reference

## Essential Commands Only

### list devices
**Usage:** `xcrun simctl list devices`
**Output:** Device list with UDIDs and states
**Key:** Use `booted` as UDID for current device

### boot
**Usage:** `xcrun simctl boot <device-udid>`
**Output:** None (success) or error

### launch
**Usage:** `xcrun simctl launch booted <bundle-id>`
**Output:** PID of launched app

### install
**Usage:** `xcrun simctl install booted <app-path>`
**Output:** None (success) or error

### io screenshot
**Usage:** `xcrun simctl io booted screenshot <file.png>`
**Output:** PNG file saved
**Options:** `--type=png|jpeg` (default: png)

### io recordVideo
**Usage:** `xcrun simctl io booted recordVideo <file.mp4>`
**Output:** Video file (Ctrl+C to stop)
**Options:** `--codec=h264|hevc` (default: hevc)

### get_app_container
**Usage:** `xcrun simctl get_app_container booted <bundle-id> data`
**Output:** Path to app's data directory

### spawn log
**Usage:** `xcrun simctl spawn booted log stream --predicate 'process == "<app>"'`
**Output:** Live log stream

## Common Patterns

```bash
# Get booted device UDID
xcrun simctl list devices | grep Booted

# Quick app test
xcrun simctl boot <udid>
xcrun simctl install booted app.app
xcrun simctl launch booted com.example.app
xcrun simctl io booted screenshot test.png
```

## Troubleshooting
See `troubleshooting.md`
```

## File: `references/test_patterns.md`
```markdown
# Test Patterns

## Smoke Test
```bash
xcrun simctl boot <udid>
xcrun simctl launch booted <bundle-id>
python scripts/accessibility_audit.py
xcrun simctl io booted screenshot smoke.png
```

## Visual Regression
```bash
# Baseline
xcrun simctl io booted screenshot baseline.png

# After changes
xcrun simctl io booted screenshot current.png
python scripts/visual_diff.py baseline.png current.png
```

## Full Accessibility Audit
```bash
# Each screen
for screen in home login settings; do
  # Navigate to screen (app-specific)
  python scripts/accessibility_audit.py --output $screen.json
done
```

## Bug Report Capture
```bash
python scripts/app_state_capture.py \
  --app-bundle-id com.example.app \
  --output bug-report/
```

## Multi-Device Test
```bash
for device in "iPhone 15" "iPad Pro"; do
  udid=$(xcrun simctl create test-$device "$device")
  xcrun simctl boot $udid
  xcrun simctl install $udid app.app
  xcrun simctl launch $udid com.example.app
  xcrun simctl io $udid screenshot $device.png
  xcrun simctl delete $udid
done
```

## Performance Baseline
```bash
# Capture initial state
xcrun simctl io booted screenshot perf-before.png
# Run performance test
xcrun simctl launch booted com.example.app
sleep 5
xcrun simctl io booted screenshot perf-after.png
python scripts/visual_diff.py perf-before.png perf-after.png
```

## Login Flow Test
```python
from scripts.test_recorder import TestRecorder

rec = TestRecorder("Login Test")
rec.step("Launch app")
# idb ui tap 200 400  # Login button
rec.step("Enter credentials")
# idb ui text "user@example.com"
rec.step("Submit")
# idb ui tap 200 500
rec.generate_report()
```
```

## File: `references/troubleshooting.md`
```markdown
# Troubleshooting

## Problem → Solution Format

### Simulator won't boot
**Fix:** `killall Simulator && xcrun simctl erase <udid>`

### IDB not connecting
**Fix:** `idb kill && idb companion --boot-status-check`

### App won't launch
**Fix:** `xcrun simctl terminate booted <bundle-id> && xcrun simctl launch booted <bundle-id>`

### Screenshot fails
**Fix:** Ensure simulator booted: `xcrun simctl boot <udid>`

### "No booted devices"
**Fix:** `open -a Simulator` or `xcrun simctl boot <udid>`

### IDB "Target not found"
**Fix:** `idb list-targets` to verify UDID

### Permission denied
**Fix:** `chmod +x scripts/*.sh`

### Python module not found
**Fix:** `pip3 install pillow` (for visual_diff.py)

### Accessibility tree empty
**Fix:** App must be in foreground: `xcrun simctl launch booted <bundle-id>`

### Video recording hangs
**Fix:** Ctrl+C to stop recording, file saves on interrupt

### Logs not showing
**Fix:** Use correct app name: `xcrun simctl spawn booted log stream --predicate 'process == "AppName"'`

### Device storage full
**Fix:** `xcrun simctl erase <udid>` (warning: deletes all data)

## Quick Diagnostics

```bash
# Check simulator state
xcrun simctl list devices | grep Booted

# Verify IDB connection
idb list-targets

# Test basic interaction
xcrun simctl io booted screenshot test.png
```
```

