---
id: makepad
type: knowledge
owner: OA_Triage
---
# makepad
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Agent Skills for Makepad

[English](./README.md) | [中文](./README.zh-CN.md) | [日本語](./README.ja.md)

[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](./.claude-plugin/plugin.json)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

Agent skills for building cross-platform UI applications with the [Makepad](https://github.com/makepad/makepad) framework in Rust.

## About Makepad

[Makepad](https://github.com/makepad/makepad) is a next-generation UI framework written in Rust that enables building high-performance, cross-platform applications. Key features include:

- **Cross-Platform**: Single codebase for Desktop (macOS, Windows, Linux), Mobile (Android, iOS), and Web (WebAssembly)
- **GPU-Accelerated**: Custom shader-based rendering with SDF (Signed Distance Field) drawing
- **Live Design**: Hot-reloadable `live_design!` DSL for rapid UI development
- **High Performance**: Native compilation, no virtual DOM, minimal runtime overhead

## About Robius

[Project Robius](https://github.com/project-robius) is an open-source initiative to build a full-featured application development framework in Rust. Production applications built with Makepad include:

- **[Robrix](https://github.com/project-robius/robrix)** - A Matrix chat client showcasing real-time messaging, E2E encryption, and complex UI patterns
- **[Moly](https://github.com/moxin-org/moly)** - An AI model manager demonstrating data-heavy interfaces and async operations

These skills are extracted from patterns used in Robrix and Moly.

## Installation

### Plugin Marketplace (Recommended)

Install via Claude Code's plugin marketplace:

```bash
# Step 1: Add marketplace
/plugin marketplace add ZhangHanDong/makepad-skills

# Step 2: Install the plugin (includes all 20 skills)
/plugin install makepad-skills@makepad-skills-marketplace
```

**Using Plugin Skills:**

Plugin skills are accessed via namespace format (they won't appear in `/skills` list, but can be loaded):

```bash
# Load specific skills by namespace
/makepad-skills:makepad-widgets
/makepad-skills:makepad-layout
/makepad-skills:robius-widget-patterns

# Or just ask questions - hooks will auto-route to relevant skills
"How do I create a Makepad button?"
"makepad 布局怎么居中？"
```

**Manage installed plugins:**

```bash
/plugin                  # List installed plugins
/plugin uninstall makepad-skills@makepad-skills-marketplace  # Uninstall
```

### Shell Script Install

Use the install script for one-command setup:

```bash
# Install to current project
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash

# Install with hooks enabled
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --with-hooks

# Install to specific project
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --target /path/to/project

# Install for Codex (.codex/skills)
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --agent codex

# Install for Gemini CLI (.gemini/skills)
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --agent gemini
```

Gemini CLI note: Skills are experimental. Enable `experimental.skills` in `/settings` if needed.

**Script features:**
- Auto-detects Rust/Makepad projects (checks for Cargo.toml)
- Backs up existing skills before installation
- `--with-hooks` copies and configures self-evolution hooks (Claude Code only)
- `--agent codex|claude-code|gemini` chooses Codex, Claude Code, or Gemini CLI (default: claude-code)
- `--target` allows installing to any project directory
- Colored output with clear progress indicators

**Available options:**

| Option | Description |
|--------|-------------|
| `--target DIR` | Install to specific directory (default: current) |
| `--with-hooks` | Enable self-evolution hooks (Claude Code only) |
| `--agent AGENT` | Set agent: `codex`, `claude-code`, or `gemini` (default: `claude-code`) |
| `--branch NAME` | Use specific branch (default: main) |
| `--help` | Show help message |

### Manual Install

```bash
# Clone this repo
git clone https://github.com/ZhangHanDong/makepad-skills.git

# Copy to your project (https://code.claude.com/docs/en/skills)
cp -r makepad-skills/skills your-project/.claude/skills

# Copy to your project for Codex (https://developers.openai.com/codex/skills)
cp -r makepad-skills/skills your-project/.codex/skills

# Copy to your project for Gemini CLI (https://geminicli.com/docs/cli/skills/)
cp -r makepad-skills/skills your-project/.gemini/skills
```

Your project structure should look like (use `.codex` or `.gemini` instead of `.claude`):

```
your-project/
├── .claude/
│   └── skills/
│       ├── .claude-plugin/
│       │   └── plugin.json
│       │
│       ├── # === Core Skills (16) ===
│       ├── makepad-basics/
│       ├── makepad-dsl/
│       ├── makepad-layout/
│       ├── makepad-widgets/
│       ├── makepad-event-action/
│       ├── makepad-animation/
│       ├── makepad-shaders/
│       ├── makepad-platform/
│       ├── makepad-font/
│       ├── makepad-splash/
│       ├── robius-app-architecture/
│       ├── robius-widget-patterns/
│       ├── robius-event-action/
│       ├── robius-state-management/
│       ├── robius-matrix-integration/
│       ├── molykit/
│       │
│       ├── # === Extended Skills (3) ===
│       ├── makepad-deployment/
│       ├── makepad-reference/
│       │
│       ├── evolution/          # Self-evolution system
│       │   └── templates/      # Contribution templates
│       └── CONTRIBUTING.md
├── src/
└── Cargo.toml
```

See [Claude Code Skills documentation](https://docs.anthropic.com/en/docs/claude-code/skills) for more details.

## GitHub Actions Packaging

Use the Makepad Packaging Action to build and release Makepad apps in CI. It wraps `cargo-packager` (desktop) and `cargo-makepad` (mobile), and can upload artifacts to GitHub Releases.

Marketplace: [makepad-packaging-action](https://github.com/marketplace/actions/makepad-packaging-action)

```yaml
- uses: Project-Robius-China/makepad-packaging-action@v1
  with:
    args: --target x86_64-unknown-linux-gnu --release
```

Notes:
- Desktop packages must run on matching OS runners.
- iOS builds require macOS runners.

## Architecture: Atomic Skills for Collaboration

### Why Atomic Structure?

v2.1 introduces an **atomic skill structure** designed for collaborative development:

```
robius-widget-patterns/
├── SKILL.md              # Index file
├── _base/                # Official patterns (numbered, atomic)
│   ├── 01-widget-extension.md
│   ├── 02-modal-overlay.md
│   ├── ...
│   └── 18-drag-drop-reorder.md
└── community/            # Your contributions
    └── {descriptive-pattern-name}.md
```

**Benefits:**
- **No merge conflicts**: Your `community/` files never conflict with official `_base/` updates
- **Parallel development**: Multiple users can contribute simultaneously
- **Clear attribution**: Your GitHub handle in filename provides credit
- **Progressive disclosure**: SKILL.md index → individual pattern details

### Self-Evolution: Enriching Skills from Your Development

The self-evolution feature allows you to capture patterns discovered during your development and add them to the skills.

#### How It Works

1. **During Development**: You discover a useful pattern, shader, or error solution while building with Makepad

2. **Capture the Pattern**: Ask Claude to save it:
   ```
   User: This tooltip positioning logic is useful. Save it as a community pattern.
   Claude: [Creates community/{handle}-tooltip-positioning.md using template]
   ```

3. **Auto-Detection** (with hooks enabled): When you encounter and fix errors, the system can automatically capture solutions to troubleshooting

#### Enable Self-Evolution Hooks (Optional)

```bash
# Copy hooks from evolution to your project
cp -r your-project/.claude/skills/evolution/hooks your-project/.claude/skills/hooks

# Make hooks executable
chmod +x your-project/.claude/skills/hooks/*.sh

# Add hooks config to your .claude/settings.json
# See skills/evolution/hooks/settings.example.json for the configuration
```

#### Manual Pattern Creation

Ask Claude directly:
```
User: Create a community pattern for the drag-drop reordering I just implemented
Claude: I'll create a pattern using the template...
```

Claude will:
1. Use the template from `evolution/templates/pattern-template.md`
2. Create file at `robius-widget-patterns/community/{descriptive-pattern-name}.md`
3. Fill in the frontmatter and content

### Community Contribution Guide

#### Contributing Patterns

1. **Create your pattern file** in the appropriate robius-* skill's community directory:
   - Widget patterns → `robius-widget-patterns/community/`
   - State patterns → `robius-state-management/community/`
   - Async patterns → `robius-app-architecture/community/`

2. **Use the template**: Copy from `evolution/templates/pattern-template.md`

3. **Required frontmatter**:
   ```yaml
   ---
   name: my-pattern-name
   author: your-github-handle
   source: project-where-you-discovered-this
   date: 2024-01-15
   tags: [tag1, tag2, tag3]
   level: beginner|intermediate|advanced
   ---
   ```

4. **Submit PR** to the main repository

#### Contributing Shaders/Effects

1. **Create your effect file**:
   ```
   makepad-shaders/community/{github-handle}-{effect-name}.md
   ```

2. **Use the template**: Copy from `evolution/templates/shader-template.md`

#### Contributing Error Solutions

1. **Create troubleshooting entry**:
   ```
   makepad-reference/troubleshooting/{error-name}.md
   ```

2. **Use the template**: Copy from `evolution/templates/troubleshooting-template.md`

#### Syncing with Upstream

Keep your local skills updated while preserving your contributions:

```bash
# If you've forked the repo
git fetch upstream
git merge upstream/main --no-edit
# Your community/ files won't conflict with _base/ changes
```

#### Promotion Path

High-quality community contributions may be promoted to `_base/`:
- Pattern is widely useful and well-tested
- Documentation is complete
- Community feedback is positive
- Credit preserved via `author` field

## Skills Overview (v3.0 Flat Structure)

### Core Skills (16)

#### Makepad Core (10 Skills)

| Skill | Description | When to Use |
|-------|-------------|-------------|
| [makepad-basics](./skills/makepad-basics/) | App structure, `live_design!`, `app_main!` | "Create a new Makepad app" |
| [makepad-dsl](./skills/makepad-dsl/) | DSL syntax, inheritance, prototypes | "How to define widgets in DSL" |
| [makepad-layout](./skills/makepad-layout/) | Flow, sizing, spacing, alignment | "Center a widget", "Arrange elements" |
| [makepad-widgets](./skills/makepad-widgets/) | Common widgets, custom widgets | "Create a button", "Build a form" |
| [makepad-event-action](./skills/makepad-event-action/) | Event handling, actions | "Handle click events" |
| [makepad-animation](./skills/makepad-animation/) | Animator, states, transitions | "Add hover animation" |
| [makepad-shaders](./skills/makepad-shaders/) | Shaders, SDF, gradients, visual effects | "Custom visual effects" |
| [makepad-platform](./skills/makepad-platform/) | Platform support | "Build for Android/iOS" |
| [makepad-font](./skills/makepad-font/) | Font, text, typography | "Change font, text styling" |
| [makepad-splash](./skills/makepad-splash/) | Splash scripting language | "Dynamic UI scripting" |

#### Robius Patterns (5 Skills)

| Skill | Description | When to Use |
|-------|-------------|-------------|
| [robius-app-architecture](./skills/robius-app-architecture/) | Tokio, async/sync patterns | "Structure an async app" |
| [robius-widget-patterns](./skills/robius-widget-patterns/) | Reusable widgets, `apply_over` | "Create reusable components" |
| [robius-event-action](./skills/robius-event-action/) | Custom actions, `MatchEvent` | "Custom event handling" |
| [robius-state-management](./skills/robius-state-management/) | AppState, persistence | "Save/load app state" |
| [robius-matrix-integration](./skills/robius-matrix-integration/) | Matrix SDK integration | "Chat client features" |

#### MolyKit (1 Skill)

| Skill | Description | When to Use |
|-------|-------------|-------------|
| [molykit](./skills/molykit/) | AI chat, SSE streaming, `BotClient` | "AI chat integration" |

### Extended Skills (3)

**Note:** Production patterns are now integrated into robius-* skills:
- Widget patterns (11) → `robius-widget-patterns/_base/`
- State patterns (5) → `robius-state-management/_base/`
- Async patterns (3) → `robius-app-architecture/_base/`

#### [makepad-deployment](./skills/makepad-deployment/SKILL.md) - Build & Package

Build for desktop (Linux, Windows, macOS), mobile (Android, iOS), and web (WebAssembly).

#### [makepad-reference](./skills/makepad-reference/SKILL.md) - Reference Materials

| File | Description | When to Use |
|------|-------------|-------------|
| troubleshooting.md | Common errors and fixes | "Apply error: no matching field" |
| code-quality.md | Makepad-aware refactoring | "Simplify this code" |
| adaptive-layout.md | Desktop/mobile responsive | "Support both desktop and mobile" |

#### [evolution](./skills/evolution/SKILL.md) - Self-Improvement

| Component | Description |
|-----------|-------------|
| `templates/` | Pattern, shader, and troubleshooting templates |
| `hooks/` | Auto-detection and validation hooks |
| `references/` | Collaboration guidelines |

## Usage Examples

### Create a New Project
```
User: Create a new Makepad app called "my-app" with a counter button
Claude: [Uses makepad-basics for scaffolding, makepad-widgets for button/counter]
```

### Add a Tooltip
```
User: Add a tooltip that shows user info on hover
Claude: [Uses robius-widget-patterns/_base/14-callout-tooltip.md for complete implementation]
```

### Save a Custom Pattern
```
User: Save this infinite scroll implementation as a community pattern
Claude: [Creates robius-widget-patterns/community/infinite-scroll.md]
```

### Fix Compilation Error
```
User: Getting "no matching field: font" error
Claude: [Uses makepad-reference/troubleshooting.md to identify correct text_style syntax]
```

## What You Can Build

With these skills, Claude can help you:

- Initialize new Makepad projects with proper structure
- Create custom widgets with `live_design!` DSL
- Handle events and user interactions
- Write GPU shaders for visual effects
- Implement smooth animations
- Manage application state with async/tokio
- Build responsive desktop/mobile layouts
- Package apps for all platforms
- **Capture and share patterns** you discover during development

## Projects Built with These Skills

Real-world projects created using makepad-skills and Claude Code:

| Project | Description | Time |
|---------|-------------|------|
| [makepad-skills-demo](https://github.com/ZhangHanDong/makepad-skills
... [TRUNCATED]
```

### File: CLAUDE.md
```md
# Makepad Skills - Claude Instructions

## CRITICAL: Hook-Based Skill Loading

**IMPORTANT:** When you see a message starting with `[makepad-skills]` in the conversation, you MUST:

1. **Read the routing instruction** - e.g., `[makepad-skills] Routing to: makepad-widgets makepad-layout`
2. **Immediately call the Skill tool** for EACH skill listed before doing anything else
3. **Do not skip this step** - the skills contain essential Makepad knowledge

Example:
```
[makepad-skills] Routing to: makepad-widgets makepad-layout
```
→ Call `Skill(makepad-widgets)` then `Skill(makepad-layout)` FIRST, then answer the question.

---

## Skill Routing

For Makepad/Robius/MolyKit questions, use **context detection** and **skill dependencies** to load multiple related skills.

### Context Detection (Load Skill Bundles)

When user intent matches these contexts, load the entire skill bundle:

| Context | Trigger Keywords | Load These Skills |
|---------|------------------|-------------------|
| **Full App Development** | "build app", "create app", "从零", "完整应用", "app architecture" | makepad-basics, makepad-dsl, makepad-layout, makepad-widgets, makepad-event-action, robius-app-architecture |
| **UI Design** | "ui design", "界面设计", "design ui" | makepad-dsl, makepad-layout, makepad-widgets, makepad-animation, makepad-shaders |
| **Widget/Component Creation** | "create widget", "创建组件", "自定义组件", "custom component" | makepad-widgets, makepad-dsl, makepad-layout, makepad-animation, makepad-shaders, makepad-font, makepad-event-action |
| **Production Patterns** | "best practice", "robrix pattern", "实际项目", "production" | robius-app-architecture, robius-widget-patterns, robius-state-management, robius-event-action |

### Skill Dependencies (Auto-Load Related Skills)

When loading a skill, automatically include its dependencies:

| Primary Skill | Also Load |
|---------------|-----------|
| makepad-widgets | makepad-layout, makepad-dsl |
| makepad-animation | makepad-shaders |
| makepad-shaders | makepad-widgets |
| makepad-font | makepad-widgets |
| robius-app-architecture | makepad-basics, makepad-event-action |
| robius-widget-patterns | makepad-widgets, makepad-layout |
| robius-event-action | makepad-event-action |

### Single Skill Keywords (Fallback)

For specific questions, match keywords to individual skills:

| Keywords | Skill |
|----------|-------|
| getting started, `live_design!`, `app_main!` | makepad-basics |
| DSL syntax, inheritance, `<Widget>`, `Foo = { }` | makepad-dsl |
| layout, Flow, Walk, padding, center, align | makepad-layout |
| View, Button, Label, widget | makepad-widgets |
| event, action, Hit, FingerDown, handle_event | makepad-event-action |
| animator, state, transition, hover | makepad-animation |
| shader, draw_bg, Sdf2d, gradient, glow | makepad-shaders |
| platform, macOS, Android, iOS, WASM | makepad-platform |
| font, text, glyph, typography | makepad-font |
| splash, script, cx.eval | makepad-splash |
| Tokio, async, submit_async_request | robius-app-architecture |
| apply_over, modal, collapsible, pageflip | robius-widget-patterns |
| custom action, MatchEvent, post_action | robius-event-action |
| AppState, persistence, Scope::with_data | robius-state-management |
| Matrix SDK, sliding sync, MatrixRequest | robius-matrix-integration |
| BotClient, OpenAI, SSE streaming | molykit |
| deploy, package, APK, IPA | makepad-deployment |
| troubleshoot, error, debug | makepad-reference |

### Extended Skills

**Note:** Production patterns are integrated into robius-* skills:
- Widget patterns (modal, collapsible, drag-drop) → `robius-widget-patterns/_base/`
- State patterns (theme switching, state machine) → `robius-state-management/_base/`
- Async patterns (streaming, tokio) → `robius-app-architecture/_base/`

## Usage Examples

### Full App Development (Bundle)
```
User: "我想从零开发一个 Makepad 应用"
-> Detect: Full app context
-> Load: makepad-basics, makepad-dsl, makepad-layout, makepad-widgets,
         makepad-event-action, robius-app-architecture
-> Answer with complete app structure, widgets, events, and async patterns
```

### Widget Creation (Bundle)
```
User: "帮我创建一个自定义按钮组件"
-> Detect: Widget creation context
-> Load: makepad-widgets, makepad-dsl, makepad-layout, makepad-animation,
         makepad-shaders, makepad-font, makepad-event-action
-> Answer with widget structure, styling, animations, and event handling
```

### Simple Question (Single + Dependencies)
```
User: "如何设置字体大小"
-> Match: makepad-font
-> Auto-load dependency: makepad-widgets
-> Load: makepad-font, makepad-widgets
-> Answer with text_style, font_size, and widget context
```

### Production App (Bundle)
```
User: "参考 Robrix 的最佳实践"
-> Detect: Production context
-> Load: robius-app-architecture, robius-widget-patterns,
         robius-state-management, robius-event-action
         + dependencies: makepad-basics, makepad-widgets, makepad-layout, makepad-event-action
-> Answer with production-ready patterns from Robrix/Moly codebases
```

## Key Patterns

### Makepad Widget Definition
```rust
#[derive(Live, LiveHook, Widget)]
pub struct MyWidget {
    #[deref] view: View,
    #[live] property: f64,
    #[rust] internal_state: State,
    #[animator] animator: Animator,
}
```

### Robius Async Pattern
```rust
// UI -> Async
submit_async_request(MatrixRequest::SendMessage { ... });

// Async -> UI
Cx::post_action(MessageSentAction { ... });
SignalToUI::set_ui_signal();
```

### MolyKit Cross-Platform Async
```rust
// Platform-agnostic spawning
spawn(async move {
    let result = fetch_data().await;
    Cx::post_action(DataReady(result));
    SignalToUI::set_ui_signal();
});
```

## Default Project Settings

When creating Makepad projects:

```toml
[package]
edition = "2024"

[dependencies]
makepad-widgets = { git = "https://github.com/makepad/makepad", branch = "dev" }

[features]
default = []
nightly = ["makepad-widgets/nightly"]
```

## Source Codebases

For deeper reference, check these codebases:

- **Makepad**: `/path/to/makepad` - Framework source
- **Robrix**: `/path/to/robrix` - Matrix client example
- **Moly**: `/path/to/moly` - AI chat example
- **MolyKit**: `/path/to/moly/moly-kit` - AI chat toolkit

```

### File: install.sh
```sh
#!/bin/bash
#
# Makepad Skills Installer
# https://github.com/ZhangHanDong/makepad-skills
#
# Usage:
#   curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash
#   curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --with-hooks
#   curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --target /path/to/project
#   curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --agent your_agent
#

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default values
REPO_URL="https://github.com/ZhangHanDong/makepad-skills"
BRANCH="main"
TARGET_DIR=""
WITH_HOOKS=false
TARGET_AGENT="claude-code"
TEMP_DIR=""

# Print colored message
info() { echo -e "${BLUE}[INFO]${NC} $1"; }
success() { echo -e "${GREEN}[OK]${NC} $1"; }
warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
error() { echo -e "${RED}[ERROR]${NC} $1"; exit 1; }

# Print banner
print_banner() {
    echo ""
    echo -e "${BLUE}╔══════════════════════════════════════════════╗${NC}"
    echo -e "${BLUE}║${NC}      ${GREEN}Makepad Skills Installer v3.0.0${NC}         ${BLUE}║${NC}"
    echo -e "${BLUE}║${NC}      Agent Skills for Makepad                ${BLUE}║${NC}"
    echo -e "${BLUE}╚══════════════════════════════════════════════╝${NC}"
    echo ""
}

# Show usage
usage() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --target DIR      Install to specific directory (default: current directory)"
    echo "  --with-hooks      Also install and configure hooks (Claude Code only)"
    echo "  --agent AGENT     Set agent (default: claude-code)"
    echo "  --list-agents     Show supported agents and exit"
    echo "  --branch BRANCH   Use specific branch (default: main)"
    echo "  --help            Show this help message"
    echo ""
    echo "Examples:"
    echo "  # Install to current project"
    echo "  $0"
    echo ""
    echo "  # Install with hooks enabled"
    echo "  $0 --with-hooks"
    echo ""
    echo "  # Install to specific project"
    echo "  $0 --target /path/to/my-makepad-project"
    echo ""
    echo "  # Install for a specific agent"
    echo "  $0 --agent your_agent"
    echo ""
}

list_agents() {
    echo "Supported agents:"
    echo "  - claude-code (default)"
    echo "  - codex"
    echo "  - gemini"
}

# Parse arguments
parse_args() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            --target)
                TARGET_DIR="$2"
                shift 2
                ;;
            --with-hooks)
                WITH_HOOKS=true
                shift
                ;;
            --agent)
                if [[ -z "$2" ]]; then
                    error "Missing value for --agent (codex|claude-code|gemini)"
                fi
                TARGET_AGENT="$2"
                shift 2
                ;;
            --list-agents)
                list_agents
                exit 0
                ;;
            --codex)
                TARGET_AGENT="codex"
                shift
                ;;
            --claude|--claude-code)
                TARGET_AGENT="claude-code"
                shift
                ;;
            --branch)
                BRANCH="$2"
                shift 2
                ;;
            --help)
                usage
                exit 0
                ;;
            *)
                error "Unknown option: $1"
                ;;
        esac
    done
}

normalize_agent() {
    case "$TARGET_AGENT" in
        codex)
            ;;
        gemini)
            ;;
        claude|claude-code)
            TARGET_AGENT="claude-code"
            ;;
        *)
            error "Unknown agent: $TARGET_AGENT (expected codex, claude-code, or gemini)"
            ;;
    esac
}

agent_label() {
    if [[ "$TARGET_AGENT" == "codex" ]]; then
        echo "Codex"
    elif [[ "$TARGET_AGENT" == "gemini" ]]; then
        echo "Gemini CLI"
    else
        echo "Claude Code"
    fi
}

skills_base_dir() {
    if [[ "$TARGET_AGENT" == "codex" ]]; then
        echo "$TARGET_DIR/.codex"
    elif [[ "$TARGET_AGENT" == "gemini" ]]; then
        echo "$TARGET_DIR/.gemini"
    else
        echo "$TARGET_DIR/.claude"
    fi
}

skills_dir() {
    echo "$(skills_base_dir)/skills"
}

# Check dependencies
check_deps() {
    info "Checking dependencies..."

    # Need either curl or git
    if ! command -v curl &> /dev/null && ! command -v git &> /dev/null; then
        error "Either curl or git is required. Please install one of them first."
    fi

    # Need unzip if using curl
    if command -v curl &> /dev/null && ! command -v unzip &> /dev/null; then
        if ! command -v git &> /dev/null; then
            error "unzip is required when using curl. Please install unzip or git."
        fi
        warn "unzip not found, will use git instead"
    fi

    success "Dependencies OK"
}

# Determine target directory
determine_target() {
    if [[ -z "$TARGET_DIR" ]]; then
        TARGET_DIR="$(pwd)"
    fi

    # Expand to absolute path
    TARGET_DIR="$(cd "$TARGET_DIR" 2>/dev/null && pwd)" || error "Target directory does not exist: $TARGET_DIR"

    info "Target directory: $TARGET_DIR"

    # Check if it looks like a project directory
    if [[ ! -f "$TARGET_DIR/Cargo.toml" ]]; then
        warn "No Cargo.toml found. This may not be a Rust/Makepad project."
        read -p "Continue anyway? [y/N] " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 1
        fi
    fi
}

# Clone or download repository
download_skills() {
    info "Downloading makepad-skills..."

    TEMP_DIR=$(mktemp -d)
    trap "rm -rf $TEMP_DIR" EXIT

    # Try ZIP download first (no git required)
    local ZIP_URL="https://github.com/ZhangHanDong/makepad-skills/archive/refs/heads/${BRANCH}.zip"

    if command -v curl &> /dev/null; then
        curl -fsSL "$ZIP_URL" -o "$TEMP_DIR/makepad-skills.zip" 2>/dev/null
        if [[ $? -eq 0 && -f "$TEMP_DIR/makepad-skills.zip" ]]; then
            unzip -q "$TEMP_DIR/makepad-skills.zip" -d "$TEMP_DIR" 2>/dev/null
            mv "$TEMP_DIR/makepad-skills-${BRANCH}" "$TEMP_DIR/makepad-skills"
            success "Downloaded via ZIP"
            return
        fi
    fi

    # Fallback to git clone
    if command -v git &> /dev/null; then
        git clone --depth 1 --branch "$BRANCH" "$REPO_URL" "$TEMP_DIR/makepad-skills" 2>/dev/null && \
            success "Downloaded via git" && return
    fi

    error "Failed to download. Please check your internet connection."
}

# Install skills
install_skills() {
    local SKILLS_DIR
    SKILLS_DIR="$(skills_dir)"

    info "Installing skills for $(agent_label) to $SKILLS_DIR..."

    # Create base directory if needed
    mkdir -p "$(skills_base_dir)"

    # Backup existing skills if present
    if [[ -d "$SKILLS_DIR" ]]; then
        local BACKUP_DIR="$SKILLS_DIR.backup.$(date +%Y%m%d%H%M%S)"
        warn "Existing skills found. Backing up to $BACKUP_DIR"
        mv "$SKILLS_DIR" "$BACKUP_DIR"
    fi

    # Copy skills
    cp -r "$TEMP_DIR/makepad-skills/skills" "$SKILLS_DIR"

    success "Skills installed"
}

# Install hooks
install_hooks() {
    if [[ "$WITH_HOOKS" != true ]]; then
        return
    fi

    if [[ "$TARGET_AGENT" != "claude-code" ]]; then
        warn "Hooks are only supported in Claude Code. Skipping hook installation."
        return
    fi

    local BASE_DIR
    BASE_DIR="$(skills_base_dir)"
    local HOOKS_SRC="$TEMP_DIR/makepad-skills/.claude/hooks"
    local HOOKS_DST="$BASE_DIR/hooks"
    local SETTINGS_SRC="$TEMP_DIR/makepad-skills/.claude/settings.json"
    local SETTINGS_DST="$BASE_DIR/settings.json"

    info "Installing hooks to $HOOKS_DST..."

    # Create hooks directory
    mkdir -p "$HOOKS_DST"

    # Copy hook scripts
    if [[ -d "$HOOKS_SRC" ]]; then
        cp "$HOOKS_SRC"/*.sh "$HOOKS_DST/" 2>/dev/null || true
        chmod +x "$HOOKS_DST"/*.sh 2>/dev/null || true
        success "Hook scripts installed"
    else
        warn "Hook scripts source not found in .claude/hooks/, skipping"
    fi

    # Install settings.json (with UserPromptSubmit hook)
    if [[ -f "$SETTINGS_SRC" ]]; then
        if [[ -f "$SETTINGS_DST" ]]; then
            # Backup existing settings
            local BACKUP_SETTINGS="$SETTINGS_DST.backup.$(date +%Y%m%d%H%M%S)"
            warn "Existing settings.json found. Backing up to $BACKUP_SETTINGS"
            cp "$SETTINGS_DST" "$BACKUP_SETTINGS"
        fi
        cp "$SETTINGS_SRC" "$SETTINGS_DST"
        success "settings.json installed with UserPromptSubmit hook"
    else
        warn "settings.json source not found, creating default..."
        # Create default settings.json
        cat > "$SETTINGS_DST" << 'SETTINGS_EOF'
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/makepad-skill-router.sh"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash|Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/pre-tool.sh"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/post-bash.sh"
          }
        ]
      }
    ]
  }
}
SETTINGS_EOF
        success "Default settings.json created"
    fi

    echo ""
    info "Hooks are now configured for auto-triggering!"
    echo "  - UserPromptSubmit: Routes queries to appropriate skills"
    echo "  - PreToolUse: Detects Makepad version"
    echo "  - PostToolUse: Self-correction on errors"
}

# Print summary
print_summary() {
    local SKILLS_DIR
    SKILLS_DIR="$(skills_dir)"

    echo ""
    echo -e "${GREEN}════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}  Installation Complete!${NC}"
    echo -e "${GREEN}════════════════════════════════════════════════${NC}"
    echo ""
    echo "  Agent: $(agent_label)"
    echo "  Skills installed to: $SKILLS_DIR"
    echo ""
    echo "  Structure (19 Skills):"
    echo "  ├── # Core Skills (16)"
    echo "  ├── makepad-basics/          (App structure)"
    echo "  ├── makepad-dsl/             (DSL syntax)"
    echo "  ├── makepad-layout/          (Layout system)"
    echo "  ├── makepad-widgets/         (Widget components)"
    echo "  ├── makepad-event-action/    (Event handling)"
    echo "  ├── makepad-animation/       (Animation)"
    echo "  ├── makepad-shaders/         (Shaders & visual effects)"
    echo "  ├── makepad-platform/        (Platform support)"
    echo "  ├── makepad-font/            (Font, typography)"
    echo "  ├── makepad-splash/          (Splash scripting)"
    echo "  ├── robius-*/                (5 Robius patterns with _base/)"
    echo "  ├── molykit/                 (AI chat toolkit)"
    echo "  ├── # Extended Skills (3)"
    echo "  ├── makepad-deployment/      (Build & package)"
    echo "  ├── makepad-reference/       (Troubleshooting)"
    echo "  └── evolution/               (Self-improvement)"
    echo ""
    echo "  Quick Start:"
    if [[ "$TARGET_AGENT" == "codex" ]]; then
        echo "  1. Open your project with Codex"
        echo "  2. Ask: \"Create a simple Makepad counter app\""
    elif [[ "$TARGET_AGENT" == "gemini" ]]; then
        echo "  1. Open your project with Gemini CLI"
        echo "  2. Ask: \"Create a simple Makepad counter app\""
    else
        echo "  1. Open your project with Claude Code"
        echo "  2. Ask: \"Create a simple Makepad counter app\""
    fi
    echo ""
    if [[ "$TARGET_AGENT" != "claude-code" ]]; then
        if [[ "$WITH_HOOKS" == true ]]; then
            echo -e "  ${YELLOW}Hooks are only supported in Claude Code.${NC}"
            echo ""
        fi
    else
        if [[ "$WITH_HOOKS" == true ]]; then
            echo -e "  ${GREEN}Hooks are installed and auto-configured!${NC}"
            echo "  Skills will auto-trigger based on your questions."
            echo ""
        else
            echo "  To enable auto-triggering hooks, run:"
            echo "  curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --with-hooks --target $TARGET_DIR"
            echo ""
        fi
    fi
    echo "  Documentation: https://github.com/ZhangHanDong/makepad-skills"
    echo ""
}

# Main
main() {
    print_banner
    parse_args "$@"
    normalize_agent
    check_deps
    determine_target
    download_skills
    install_skills
    install_hooks
    print_summary
}

main "$@"

```

### File: metadata.json
```json
{
  "name": "makepad-skills",
  "version": "2.0.0",
  "description": "Comprehensive Makepad, Robius, and MolyKit skills for Claude with auto-triggering",
  "author": "makepad-skills contributors",
  "license": "MIT",
  "repository": "https://github.com/ZhangHanDong/makepad-skills",

  "stats": {
    "makepad_skills": 11,
    "robius_skills": 5,
    "molykit_skills": 1,
    "extended_skills": 3,
    "total_skills": 20
  },

  "skills": {
    "router": [
      "makepad-router"
    ],
    "makepad": [
      "makepad-basics",
      "makepad-dsl",
      "makepad-layout",
      "makepad-widgets",
      "makepad-event-action",
      "makepad-animation",
      "makepad-shaders",
      "makepad-platform",
      "makepad-font",
      "makepad-splash"
    ],
    "robius": [
      "robius-app-architecture",
      "robius-widget-patterns",
      "robius-event-action",
      "robius-state-management",
      "robius-matrix-integration"
    ],
    "molykit": [
      "molykit"
    ],
    "extended": [
      "makepad-deployment",
      "makepad-reference",
      "evolution"
    ]
  },

  "triggers": {
    "makepad": [
      "makepad", "live_design!", "app_main!", "Widget", "View", "Button",
      "Label", "TextInput", "draw_bg", "Sdf2d", "shader", "animator",
      "Flow", "Walk", "Size", "Padding", "WidgetRef", "WidgetAction"
    ],
    "robius": [
      "robius", "robrix", "AppState", "Scope::with_data", "MatrixRequest",
      "TimelineUpdate", "submit_async_request", "MatchEvent", "handle_actions",
      "widget extension", "modal", "collapsible", "LRU cache", "drag-drop",
      "theme switching", "state machine", "persistence", "async loading", "tokio"
    ],
    "molykit": [
      "molykit", "moly-kit", "BotClient", "BotContext", "PlatformSend",
      "SSE streaming", "AI chat", "OpenAI Makepad"
    ],
    "extended": [
      "deployment", "android", "iOS", "WASM", "packaging",
      "GitHub Actions", "CI", "action", "marketplace", "release",
      "troubleshooting", "error", "code quality", "adaptive layout",
      "self-evolution", "hooks", "templates", "contribution"
    ]
  },

  "source_projects": {
    "makepad": "https://github.com/makepad/makepad",
    "robrix": "https://github.com/project-robius/robrix",
    "moly": "https://github.com/moxin-org/moly",
    "molykit": "https://github.com/moxin-org/moly/tree/main/moly-kit"
  },

  "compatibility": {
    "claude_code_min_version": "2.1.0",
    "makepad_version": "0.6.0+",
    "rust_edition": "2024"
  },

  "last_updated": "2026-02-04",
  "quality_checks": {
    "skill_frontmatter": true,
    "llms_txt_present": true,
    "references_present": true
  }
}

```

### File: README.ja.md
```md
# Makepad 向け Claude Skills

[English](./README.md) | [中文](./README.zh-CN.md) | [日本語](./README.ja.md)

[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](./.claude-plugin/plugin.json)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

Rust の [Makepad](https://github.com/makepad/makepad) フレームワークを使用してクロスプラットフォーム UI アプリケーションを構築するための Agent Skills です。

## Makepad について

[Makepad](https://github.com/makepad/makepad) は、Rust で書かれた次世代 UI フレームワークで、高性能なクロスプラットフォームアプリケーションの構築を可能にします。主な特徴：

- **クロスプラットフォーム**：単一のコードベースでデスクトップ（macOS、Windows、Linux）、モバイル（Android、iOS）、Web（WebAssembly）に対応
- **GPU アクセラレーション**：SDF（Signed Distance Field）描画によるカスタムシェーダーベースのレンダリング
- **ライブデザイン**：ホットリロード可能な `live_design!` DSL による迅速な UI 開発
- **高パフォーマンス**：ネイティブコンパイル、仮想 DOM なし、最小限のランタイムオーバーヘッド

## Robius について

[Project Robius](https://github.com/project-robius) は、Rust でフル機能のアプリケーション開発フレームワークを構築するオープンソースイニシアチブです。Makepad で構築された本番アプリケーション：

- **[Robrix](https://github.com/project-robius/robrix)** - リアルタイムメッセージング、E2E 暗号化、複雑な UI パターンを実装した Matrix チャットクライアント
- **[Moly](https://github.com/moxin-org/moly)** - データ集約型インターフェースと非同期操作を実装した AI モデルマネージャー

これらの Skills は Robrix と Moly で使用されているパターンから抽出されています。

## インストール

### プラグインマーケットプレイス（推奨）

Claude Code のプラグインマーケットプレイス経由でインストール：

```bash
# ステップ 1：マーケットプレイスを追加
/plugin marketplace add ZhangHanDong/makepad-skills

# ステップ 2：プラグインをインストール（1つまたは複数選択）
/plugin install makepad-full@makepad-skills-marketplace        # 全スキル
/plugin install makepad-core@makepad-skills-marketplace        # コア + 入門
/plugin install makepad-graphics@makepad-skills-marketplace    # グラフィックス & シェーダー
/plugin install makepad-patterns@makepad-skills-marketplace    # プロダクションパターン
/plugin install makepad-deployment@makepad-skills-marketplace  # プラットフォームパッケージング
/plugin install makepad-reference@makepad-skills-marketplace   # API ドキュメント & トラブルシューティング
```

**利用可能なプラグイン：**

| プラグイン | 説明 |
|-----------|------|
| `makepad-full` | 全スキルを含む完全パッケージ |
| `makepad-core` | 入門、レイアウト、ウィジェット、イベント |
| `makepad-graphics` | SDF 描画、シェーダー、アニメーション |
| `makepad-patterns` | 非同期、ステートマシン、オーバーレイ、リスト |
| `makepad-deployment` | Android、iOS、WASM パッケージング |
| `makepad-reference` | API ドキュメント、トラブルシューティング、コード品質 |
| `makepad-evolution` | 自己進化テンプレートとフック |

### スクリプトインストール

インストールスクリプトでワンコマンドセットアップ：

```bash
# 現在のプロジェクトにインストール
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash

# hooks を有効にしてインストール
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --with-hooks

# 特定のプロジェクトにインストール
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --target /path/to/project

# Codex 向けにインストール（.codex/skills）
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --agent codex

# Gemini CLI 向けにインストール（.gemini/skills）
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --agent gemini
```

Gemini CLI 補足: Skills は実験的機能です。必要に応じて `/settings` で `experimental.skills` を有効化してください。

**スクリプト機能：**
- Rust/Makepad プロジェクトを自動検出（Cargo.toml をチェック）
- インストール前に既存の skills をバックアップ
- `--with-hooks` で自己進化フックをコピーして設定（Claude Code のみ）
- `--agent codex|claude-code|gemini` で Codex、Claude Code、または Gemini CLI を選択（デフォルト: claude-code）
- `--target` で任意のプロジェクトディレクトリにインストール可能
- カラー出力で進捗を明確に表示

**利用可能なオプション：**

| オプション | 説明 |
|-----------|------|
| `--target DIR` | 特定のディレクトリにインストール（デフォルト：現在のディレクトリ） |
| `--with-hooks` | 自己進化フックを有効化（Claude Code のみ） |
| `--agent AGENT` | エージェント指定: `codex`、`claude-code`、または `gemini`（デフォルト: `claude-code`） |
| `--branch NAME` | 特定のブランチを使用（デフォルト：main） |
| `--help` | ヘルプメッセージを表示 |

### 手動インストール

```bash
# このリポジトリをクローン
git clone https://github.com/ZhangHanDong/makepad-skills.git

# プロジェクトにコピー（https://code.claude.com/docs/en/skills）
cp -r makepad-skills/skills your-project/.claude/skills

# Codex プロジェクトにコピー（https://developers.openai.com/codex/skills）
cp -r makepad-skills/skills your-project/.codex/skills

# Gemini CLI プロジェクトにコピー（https://geminicli.com/docs/cli/skills/）
cp -r makepad-skills/skills your-project/.gemini/skills
```

インストール後のプロジェクト構造（Codex/Gemini は `.claude` を `.codex`/`.gemini` に置き換えてください）：

```
your-project/
├── .claude/
│   └── skills/
│       ├── .claude-plugin/
│       │   └── plugin.json
│       ├── 00-getting-started/
│       ├── 01-core/
│       ├── 02-components/
│       ├── 03-graphics/
│       │   ├── _base/          # 公式 skills（アトミック）
│       │   └── community/      # コミュニティ貢献
│       ├── 04-patterns/
│       │   ├── _base/          # 公式 patterns（アトミック）
│       │   └── community/      # コミュニティ貢献
│       ├── 05-deployment/
│       ├── 06-reference/
│       ├── 99-evolution/
│       │   └── templates/      # 貢献テンプレート
│       └── CONTRIBUTING.md
├── src/
└── Cargo.toml
```

詳細は [Claude Code Skills 公式ドキュメント](https://docs.anthropic.com/en/docs/claude-code/skills) を参照してください。

## GitHub Actions パッケージング

Makepad Packaging Action を使って CI で Makepad アプリをパッケージングできます。内部で `cargo-packager`（デスクトップ）と `cargo-makepad`（モバイル）を実行し、GitHub Releases へのアップロードに対応します。

Marketplace: [makepad-packaging-action](https://github.com/marketplace/actions/makepad-packaging-action)

```yaml
- uses: Project-Robius-China/makepad-packaging-action@v1
  with:
    args: --target x86_64-unknown-linux-gnu --release
```

注意：
- デスクトップは対応 OS の runner が必要です。
- iOS は macOS runner が必要です。

## アーキテクチャ：コラボレーション向けアトミック Skills

### なぜアトミック構造？

v2.1 では、協調開発向けに設計された**アトミック skill 構造**を導入しました：

```
04-patterns/
├── SKILL.md              # インデックスファイル
├── _base/                # 公式 patterns（番号付き、アトミック）
│   ├── 01-widget-extension.md
│   ├── 02-modal-overlay.md
│   ├── ...
│   └── 14-callout-tooltip.md
└── community/            # あなたの貢献
    ├── README.md
    └── {GitHub ユーザー名}-{パターン名}.md
```

**メリット：**
- **マージ競合なし**：`community/` のファイルは公式 `_base/` の更新と競合しません
- **並列開発**：複数のユーザーが同時に貢献可能
- **明確な帰属**：ファイル名の GitHub ユーザー名がクレジットを提供
- **段階的開示**：SKILL.md インデックス → 個別パターンの詳細

### 自己進化：開発から Skills を蓄積

自己進化機能により、開発中に発見したパターンをキャプチャして skills に追加できます。

#### 仕組み

1. **開発中**：Makepad でアプリを構築する際に、有用なパターン、シェーダー、エラー解決策を発見

2. **パターンをキャプチャ**：Claude に保存を依頼：
   ```
   ユーザー: このツールチップ配置ロジックは便利です。コミュニティパターンとして保存して
   Claude: [テンプレートを使用して community/{ユーザー名}-tooltip-positioning.md を作成]
   ```

3. **自動検出**（hooks 有効時）：エラーを遭遇して修正すると、システムが自動的に解決策を troubleshooting にキャプチャ

#### 自己進化フックを有効にする（オプション）

```bash
# 99-evolution からプロジェクトに hooks をコピー
cp -r your-project/.claude/skills/99-evolution/hooks your-project/.claude/skills/hooks

# フックに実行権限を付与
chmod +x your-project/.claude/skills/hooks/*.sh

# フック設定を .claude/settings.json に追加
# skills/99-evolution/hooks/settings.example.json を参照
```

#### 手動パターン作成

Claude に直接依頼：
```
ユーザー: さっき実装したドラッグ&ドロップ並べ替えをコミュニティパターンとして保存して
Claude: テンプレートを使用して作成します...
```

Claude は：
1. `99-evolution/templates/pattern-template.md` テンプレートを使用
2. `04-patterns/community/{あなたのユーザー名}-drag-drop-reorder.md` にファイルを作成
3. frontmatter とコンテンツを入力

### コミュニティ貢献ガイド

#### パターンの貢献

1. **パターンファイルを作成**：
   ```
   04-patterns/community/{GitHub ユーザー名}-{パターン名}.md
   ```

2. **テンプレートを使用**：`99-evolution/templates/pattern-template.md` からコピー

3. **必須の frontmatter**：
   ```yaml
   ---
   name: my-pattern-name
   author: your-github-handle
   source: project-where-you-discovered-this
   date: 2024-01-15
   tags: [tag1, tag2, tag3]
   level: beginner|intermediate|advanced
   ---
   ```

4. **メインリポジトリに PR を送信**

#### シェーダー/エフェクトの貢献

1. **エフェクトファイルを作成**：
   ```
   03-graphics/community/{GitHub ユーザー名}-{エフェクト名}.md
   ```

2. **テンプレートを使用**：`99-evolution/templates/shader-template.md` からコピー

#### エラー解決策の貢献

1. **troubleshooting エントリを作成**：
   ```
   06-reference/troubleshooting/{エラー名}.md
   ```

2. **テンプレートを使用**：`99-evolution/templates/troubleshooting-template.md` からコピー

#### アップストリームとの同期

ローカル skills を更新しながら、貢献を保持：

```bash
# リポジトリをフォークしている場合
git fetch upstream
git merge upstream/main --no-edit
# community/ ファイルは _base/ の変更と競合しません
```

#### 昇格パス

高品質なコミュニティ貢献は `_base/` に昇格される可能性があります：
- パターンが広く有用で十分にテストされている
- ドキュメントが完全
- コミュニティのフィードバックがポジティブ
- `author` フィールドでクレジットを保持

## Skills 一覧 (v2.1 アトミック構造)

### [00-getting-started](./skills/00-getting-started/SKILL.md) - プロジェクトセットアップ

| ファイル | 説明 | 使用場面 |
|----------|------|----------|
| [init.md](./skills/00-getting-started/init.md) | プロジェクトスキャフォールディング | 「新しい Makepad アプリを作成」 |
| [project-structure.md](./skills/00-getting-started/project-structure.md) | ディレクトリ構成 | 「プロジェクトをどう整理すべき？」 |

### [01-core](./skills/01-core/SKILL.md) - コア開発

| ファイル | 説明 | 使用場面 |
|----------|------|----------|
| [layout.md](./skills/01-core/layout.md) | フロー、サイズ、間隔、配置 | 「UI 要素を配置」 |
| [widgets.md](./skills/01-core/widgets.md) | 一般的なウィジェット、カスタムウィジェット | 「ボタンの作り方は？」 |
| [events.md](./skills/01-core/events.md) | イベント処理、ヒットテスト | 「クリックイベントの処理」 |
| [styling.md](./skills/01-core/styling.md) | フォント、テキストスタイル、SVG アイコン | 「フォントサイズを変更」「アイコンを追加」 |

### [02-components](./skills/02-components/SKILL.md) - ウィジェットギャラリー

全ビルトインウィジェット参照（ui_zoo から）：Button、TextInput、Slider、Checkbox、Label、Image、ScrollView、PortalList、PageFlip など。

### [03-graphics](./skills/03-graphics/SKILL.md) - グラフィックスとアニメーション（アトミック）

`_base/` に 14 個の独立 skills：

| カテゴリ | Skills |
|----------|--------|
| シェーダー基礎 | `01-shader-structure`, `02-shader-math` |
| SDF 描画 | `03-sdf-shapes`, `04-sdf-drawing`, `05-progress-track` |
| アニメーション | `06-animator-basics`, `07-easing-functions`, `08-keyframe-animation`, `09-loading-spinner` |
| ビジュアルエフェクト | `10-hover-effect`, `11-gradient-effects`, `12-shadow-glow`, `13-disabled-state`, `14-toggle-checkbox` |

`community/` にはカスタムエフェクトを追加。

### [04-patterns](./skills/04-patterns/SKILL.md) - プロダクションパターン（アトミック）

`_base/` に 14 個の独立 patterns：

| カテゴリ | Patterns |
|----------|----------|
| ウィジェットパターン | `01-widget-extension`, `02-modal-overlay`, `03-collapsible`, `04-list-template`, `05-lru-view-cache`, `06-global-registry`, `07-radio-navigation` |
| データパターン | `08-async-loading`, `09-streaming-results`, `10-state-machine`, `11-theme-switching`, `12-local-persistence` |
| 高度なパターン | `13-tokio-integration`, `14-callout-tooltip` |

`community/` にはカスタムパターンを追加。

### [05-deployment](./skills/05-deployment/SKILL.md) - ビルドとパッケージ

デスクトップ（Linux、Windows、macOS）、モバイル（Android、iOS）、Web（WebAssembly）向けにビルド。

### [06-reference](./skills/06-reference/SKILL.md) - リファレンス

| ファイル | 説明 | 使用場面 |
|----------|------|----------|
| [troubleshooting.md](./skills/06-reference/troubleshooting.md) | よくあるエラーと修正 | 「Apply error: no matching field」 |
| [code-quality.md](./skills/06-reference/code-quality.md) | Makepad 対応のリファクタリング | 「このコードを簡略化」 |
| [adaptive-layout.md](./skills/06-reference/adaptive-layout.md) | デスクトップ/モバイルレスポンシブ | 「デスクトップとモバイル両方に対応」 |

### [99-evolution](./skills/99-evolution/SKILL.md) - 自己改善

| コンポーネント | 説明 |
|---------------|------|
| `templates/` | パターン、シェーダー、troubleshooting テンプレート |
| `hooks/` | 自動検出と検証フック |

## 使用例

### 新規プロジェクト作成
```
ユーザー: カウンターボタン付きの "my-app" という Makepad アプリを作成
Claude: [00-getting-started でプロジェクト作成、01-core でボタン/カウンター実装]
```

### ツールチップを追加
```
ユーザー: ホバー時にユーザー情報を表示するツールチップを追加
Claude: [04-patterns/_base/14-callout-tooltip.md で完全な実装を取得]
```

### カスタムパターンを保存
```
ユーザー: この無限スクロール実装をコミュニティパターンとして保存
Claude: [04-patterns/community/yourhandle-infinite-scroll.md を作成]
```

### コンパイルエラー修正
```
ユーザー: "no matching field: font" エラーが発生
Claude: [06-reference/troubleshooting.md で正しい text_style 構文を特定]
```

## 構築できるもの

これらの Skills を使用すると、Claude は以下をサポートします：

- 適切な構造で新しい Makepad プロジェクトを初期化
- `live_design!` DSL でカスタムウィジェットを作成
- イベントとユーザーインタラクションを処理
- 視覚効果用の GPU シェーダーを作成
- スムーズなアニメーションを実装
- async/tokio でアプリケーション状態を管理
- レスポンシブなデスクトップ/モバイルレイアウトを構築
- すべてのプラットフォーム向けにアプリをパッケージ化
- 開発中に発見したパターンを**キャプチャして共有**

## これらの Skills で構築されたプロジェクト

makepad-skills と Claude Code を使用して作成された実際のプロジェクト：

| プロジェクト | 説明 | 所要時間 |
|-------------|------|----------|
| [makepad-skills-demo](https://github.com/ZhangHanDong/makepad-skills-demo) | 為替レート変換アプリのデモ | 約 20 分 |
| [makepad-component](https://github.com/ZhangHanDong/makepad-component) | 再利用可能な Makepad コンポーネントライブラリ | - |

### makepad-skills-demo スクリーンショット

<p align="center">
  <img src="./assets/skill-app-demo.jpg" width="60%" alt="為替レート変換アプリ" />
</p>

### makepad-component スクリーンショット

<p align="center">
  <img src="./assets/mc1.png" width="45%" alt="コンポーネント 1" />
  <img src="./assets/mc2.png" width="45%" alt="コンポーネント 2" />
</p>
<p align="center">
  <img src="./assets/mc3.png" width="45%" alt="コンポーネント 3" />
  <img src="./assets/mc4.png" width="45%" alt="コンポーネント 4" />
</p>

## リソース

- [Makepad リポジトリ](https://github.com/makepad/makepad)
- [Makepad サンプル](https://github.com/makepad/makepad/tree/main/examples)
- [Project Robius](https://github.com/project-robius)
- [Robrix](https://github.com/project-robius/robrix)
- [Moly](https://github.com/moxin-org/moly)

## ライセンス

MIT

```

### File: README.zh-CN.md
```md
# Makepad 的 Agent Skills

[English](./README.md) | [中文](./README.zh-CN.md) | [日本語](./README.ja.md)

[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](./.claude-plugin/plugin.json)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

用于在 Rust 中使用 [Makepad](https://github.com/makepad/makepad) 框架构建跨平台 UI 应用的 Agent Skills。

## 关于 Makepad

[Makepad](https://github.com/makepad/makepad) 是一个用 Rust 编写的新一代 UI 框架，能够构建高性能的跨平台应用。主要特性包括：

- **跨平台**：单一代码库支持桌面端（macOS、Windows、Linux）、移动端（Android、iOS）和 Web（WebAssembly）
- **GPU 加速**：基于自定义着色器的渲染，使用 SDF（有向距离场）绘制
- **实时设计**：可热重载的 `live_design!` DSL，实现快速 UI 开发
- **高性能**：原生编译，无虚拟 DOM，极低的运行时开销

## 关于 Robius

[Project Robius](https://github.com/project-robius) 是一个开源项目，致力于用 Rust 构建功能完整的应用开发框架。使用 Makepad 构建的生产级应用包括：

- **[Robrix](https://github.com/project-robius/robrix)** - Matrix 聊天客户端，展示了实时消息、端到端加密和复杂 UI 模式
- **[Moly](https://github.com/moxin-org/moly)** - AI 模型管理器，展示了数据密集型界面和异步操作

这些 Skills 提取自 Robrix 和 Moly 中使用的模式。

## 安装

### 插件市场安装（推荐）

通过 Claude Code 的插件市场安装：

```bash
# 第一步：添加市场
/plugin marketplace add ZhangHanDong/makepad-skills

# 第二步：安装插件（选择一个或多个）
/plugin install makepad-full@makepad-skills-marketplace        # 全部技能
/plugin install makepad-core@makepad-skills-marketplace        # 核心 + 入门
/plugin install makepad-graphics@makepad-skills-marketplace    # 图形 & 着色器
/plugin install makepad-patterns@makepad-skills-marketplace    # 生产模式
/plugin install makepad-deployment@makepad-skills-marketplace  # 平台打包
/plugin install makepad-reference@makepad-skills-marketplace   # API 文档 & 问题排查
```

**可用插件：**

| 插件 | 说明 |
|------|------|
| `makepad-full` | 包含所有技能的完整包 |
| `makepad-core` | 入门、布局、组件、事件 |
| `makepad-graphics` | SDF 绘图、着色器、动画 |
| `makepad-patterns` | 异步、状态机、弹窗、列表 |
| `makepad-deployment` | Android、iOS、WASM 打包 |
| `makepad-reference` | API 文档、问题排查、代码质量 |
| `makepad-evolution` | 自我进化模板和 hooks |

### 脚本安装

使用安装脚本一键完成：

```bash
# 安装到当前项目
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash

# 安装并启用 hooks
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --with-hooks

# 安装到指定项目
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --target /path/to/project

# --agent 不指定默认为: claude

# 安装到 Codex（.codex/skills）
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --agent codex

# 安装到 Gemini CLI（.gemini/skills）
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --agent gemini
```

Gemini CLI 说明：Skills 目前为实验性功能，如需使用请在 `/settings` 中启用 `experimental.skills`。

**脚本特性：**
- 自动检测 Rust/Makepad 项目（检查 Cargo.toml）
- 安装前自动备份已有 skills
- `--with-hooks` 复制并配置自我进化 hooks（仅 Claude Code）
- `--agent codex|claude-code|gemini` 选择 Codex、Claude Code 或 Gemini CLI（默认：claude-code）
- `--target` 支持安装到任意项目目录
- 彩色输出，清晰的进度提示

**可用选项：**

| 选项 | 说明 |
|------|------|
| `--target DIR` | 安装到指定目录（默认：当前目录） |
| `--with-hooks` | 启用自我进化 hooks（仅 Claude Code） |
| `--agent AGENT` | 设置Agent：`codex`、`claude-code` 或 `gemini`（默认：`claude-code`） |
| `--branch NAME` | 使用指定分支（默认：main） |
| `--help` | 显示帮助信息 |

### 手动安装

```bash
# 克隆此仓库
git clone https://github.com/ZhangHanDong/makepad-skills.git

# 复制到你的项目（https://code.claude.com/docs/en/skills）
cp -r makepad-skills/skills your-project/.claude/skills

# 复制到 Codex 项目（https://developers.openai.com/codex/skills）
cp -r makepad-skills/skills your-project/.codex/skills

# 复制到 Gemini CLI 项目（https://geminicli.com/docs/cli/skills/）
cp -r makepad-skills/skills your-project/.gemini/skills
```

安装后的项目结构（Codex/Gemini 请将 `.claude` 替换为 `.codex`/`.gemini`）：

```
your-project/
├── .claude/
│   └── skills/
│       ├── .claude-plugin/
│       │   └── plugin.json
│       ├── 00-getting-started/
│       ├── 01-core/
│       ├── 02-components/
│       ├── 03-graphics/
│       │   ├── _base/          # 官方 skills（原子化）
│       │   └── community/      # 社区贡献
│       ├── 04-patterns/
│       │   ├── _base/          # 官方 patterns（原子化）
│       │   └── community/      # 社区贡献
│       ├── 05-deployment/
│       ├── 06-reference/
│       ├── 99-evolution/
│       │   └── templates/      # 贡献模板
│       └── CONTRIBUTING.md
├── src/
└── Cargo.toml
```

更多详情请参阅 [Claude Code Skills 官方文档](https://docs.anthropic.com/en/docs/claude-code/skills)。

## GitHub Actions 打包

使用 Makepad Packaging Action 在 CI 中打包并发布 Makepad 应用。内部封装 `cargo-packager`（桌面）与 `cargo-makepad`（移动），并支持上传产物到 GitHub Releases。

Marketplace: [makepad-packaging-action](https://github.com/marketplace/actions/makepad-packaging-action)

```yaml
- uses: Project-Robius-China/makepad-packaging-action@v1
  with:
    args: --target x86_64-unknown-linux-gnu --release
```

注意：
- 桌面包必须在对应 OS runner 上构建。
- iOS 需要 macOS runner。

## 架构：面向协作的原子化 Skills

### 为什么采用原子化结构？

v2.1 引入了**原子化 skill 结构**，专为协作开发设计：

```
04-patterns/
├── SKILL.md              # 索引文件
├── _base/                # 官方 patterns（编号、原子化）
│   ├── 01-widget-extension.md
│   ├── 02-modal-overlay.md
│   ├── ...
│   └── 14-callout-tooltip.md
└── community/            # 你的贡献
    ├── README.md
    └── {github用户名}-{pattern名称}.md
```

**优势：**
- **无合并冲突**：你的 `community/` 文件永远不会与官方 `_base/` 更新冲突
- **并行开发**：多个用户可以同时贡献
- **清晰归属**：文件名中的 GitHub 用户名提供署名
- **渐进式披露**：SKILL.md 索引 → 单个 pattern 详情

### 自我进化：从开发中沉淀 Skills

自我进化功能允许你捕获开发过程中发现的模式，并添加到 skills 中。

#### 工作原理

1. **开发过程中**：你在使用 Makepad 构建应用时发现有用的模式、着色器或错误解决方案

2. **捕获模式**：让 Claude 保存它：
   ```
   用户：这个 tooltip 定位逻辑很有用，保存为社区 pattern
   Claude：[使用模板创建 community/{用户名}-tooltip-positioning.md]
   ```

3. **自动检测**（启用 hooks 后）：当你遇到并修复错误时，系统可以自动将解决方案捕获到 troubleshooting

#### 启用自我进化 Hooks（可选）

```bash
# 从 99-evolution 复制 hooks 到项目
cp -r your-project/.claude/skills/99-evolution/hooks your-project/.claude/skills/hooks

# 添加执行权限
chmod +x your-project/.claude/skills/hooks/*.sh

# 将 hooks 配置添加到 .claude/settings.json
# 参考 skills/99-evolution/hooks/settings.example.json
```

#### 手动创建 Pattern

直接让 Claude 创建：
```
用户：把我刚才实现的拖拽排序保存为社区 pattern
Claude：我将使用模板创建...
```

Claude 会：
1. 使用 `99-evolution/templates/pattern-template.md` 模板
2. 在 `04-patterns/community/{你的用户名}-drag-drop-reorder.md` 创建文件
3. 填写 frontmatter 和内容

### 社区贡献指南

#### 贡献 Patterns

1. **创建 pattern 文件**：
   ```
   04-patterns/community/{github用户名}-{pattern名称}.md
   ```

2. **使用模板**：从 `99-evolution/templates/pattern-template.md` 复制

3. **必需的 frontmatter**：
   ```yaml
   ---
   name: my-pattern-name
   author: your-github-handle
   source: project-where-you-discovered-this
   date: 2024-01-15
   tags: [tag1, tag2, tag3]
   level: beginner|intermediate|advanced
   ---
   ```

4. **提交 PR** 到主仓库

#### 贡献着色器/效果

1. **创建效果文件**：
   ```
   03-graphics/community/{github用户名}-{效果名称}.md
   ```

2. **使用模板**：从 `99-evolution/templates/shader-template.md` 复制

#### 贡献错误解决方案

1. **创建 troubleshooting 条目**：
   ```
   06-reference/troubleshooting/{错误名称}.md
   ```

2. **使用模板**：从 `99-evolution/templates/troubleshooting-template.md` 复制

#### 与上游同步

保持本地 skills 更新，同时保留你的贡献：

```bash
# 如果你已 fork 仓库
git fetch upstream
git merge upstream/main --no-edit
# 你的 community/ 文件不会与 _base/ 变更冲突
```

#### 晋升路径

高质量的社区贡献可能会被提升到 `_base/`：
- Pattern 广泛有用且经过充分测试
- 文档完整
- 社区反馈积极
- 通过 `author` 字段保留署名

## Skills 概览 (v2.1 原子化结构)

### [00-getting-started](./skills/00-getting-started/SKILL.md) - 项目设置

| 文件 | 描述 | 使用场景 |
|------|------|----------|
| [init.md](./skills/00-getting-started/init.md) | 项目脚手架 | "创建一个新的 Makepad 应用" |
| [project-structure.md](./skills/00-getting-started/project-structure.md) | 目录组织 | "我应该如何组织项目？" |

### [01-core](./skills/01-core/SKILL.md) - 核心开发

| 文件 | 描述 | 使用场景 |
|------|------|----------|
| [layout.md](./skills/01-core/layout.md) | 流式布局、尺寸、间距、对齐 | "排列 UI 元素" |
| [widgets.md](./skills/01-core/widgets.md) | 常用组件、自定义组件 | "如何创建按钮？" |
| [events.md](./skills/01-core/events.md) | 事件处理、命中测试 | "处理点击事件" |
| [styling.md](./skills/01-core/styling.md) | 字体、文本样式、SVG 图标 | "修改字体大小"、"添加图标" |

### [02-components](./skills/02-components/SKILL.md) - 组件库

所有内置组件参考（来自 ui_zoo）：Button、TextInput、Slider、Checkbox、Label、Image、ScrollView、PortalList、PageFlip 等。

### [03-graphics](./skills/03-graphics/SKILL.md) - 图形与动画（原子化）

`_base/` 中包含 14 个独立 skills：

| 类别 | Skills |
|------|--------|
| 着色器基础 | `01-shader-structure`, `02-shader-math` |
| SDF 绘制 | `03-sdf-shapes`, `04-sdf-drawing`, `05-progress-track` |
| 动画 | `06-animator-basics`, `07-easing-functions`, `08-keyframe-animation`, `09-loading-spinner` |
| 视觉效果 | `10-hover-effect`, `11-gradient-effects`, `12-shadow-glow`, `13-disabled-state`, `14-toggle-checkbox` |

另有 `community/` 存放你的自定义效果。

### [04-patterns](./skills/04-patterns/SKILL.md) - 生产模式（原子化）

`_base/` 中包含 14 个独立 patterns：

| 类别 | Patterns |
|------|----------|
| 组件模式 | `01-widget-extension`, `02-modal-overlay`, `03-collapsible`, `04-list-template`, `05-lru-view-cache`, `06-global-registry`, `07-radio-navigation` |
| 数据模式 | `08-async-loading`, `09-streaming-results`, `10-state-machine`, `11-theme-switching`, `12-local-persistence` |
| 高级模式 | `13-tokio-integration`, `14-callout-tooltip` |

另有 `community/` 存放你的自定义 patterns。

### [05-deployment](./skills/05-deployment/SKILL.md) - 构建与打包

构建桌面端（Linux、Windows、macOS）、移动端（Android、iOS）和 Web（WebAssembly）。

### [06-reference](./skills/06-reference/SKILL.md) - 参考资料

| 文件 | 描述 | 使用场景 |
|------|------|----------|
| [troubleshooting.md](./skills/06-reference/troubleshooting.md) | 常见错误及修复 | "Apply error: no matching field" |
| [code-quality.md](./skills/06-reference/code-quality.md) | Makepad 感知的重构 | "简化这段代码" |
| [adaptive-layout.md](./skills/06-reference/adaptive-layout.md) | 桌面/移动端响应式 | "同时支持桌面端和移动端" |

### [99-evolution](./skills/99-evolution/SKILL.md) - 自我改进

| 组件 | 描述 |
|------|------|
| `templates/` | Pattern、shader 和 troubleshooting 模板 |
| `hooks/` | 自动检测和验证 hooks |

## 使用示例

### 创建新项目
```
用户：创建一个名为 "my-app" 的 Makepad 应用，包含一个计数器按钮
Claude：[使用 00-getting-started 搭建项目，使用 01-core 实现按钮/计数器]
```

### 添加 Tooltip
```
用户：添加一个悬停时显示用户信息的 tooltip
Claude：[使用 04-patterns/_base/14-callout-tooltip.md 获取完整实现]
```

### 保存自定义 Pattern
```
用户：把这个无限滚动实现保存为社区 pattern
Claude：[创建 04-patterns/community/yourhandle-infinite-scroll.md]
```

### 修复编译错误
```
用户：遇到 "no matching field: font" 错误
Claude：[使用 06-reference/troubleshooting.md 识别正确的 text_style 语法]
```

## 你可以构建什么

使用这些 Skills，Claude 可以帮助你：

- 使用正确的结构初始化新的 Makepad 项目
- 使用 `live_design!` DSL 创建自定义组件
- 处理事件和用户交互
- 编写 GPU 着色器实现视觉效果
- 实现流畅的动画
- 使用 async/tokio 管理应用状态
- 构建响应式的桌面端/移动端布局
- 为所有平台打包应用
- **捕获并分享**你在开发过程中发现的模式

## 基于这些 Skills 构建的项目

使用 makepad-skills 和 Claude Code 创建的真实项目：

| 项目 | 描述 | 耗时 |
|------|------|------|
| [makepad-skills-demo](https://github.com/ZhangHanDong/makepad-skills-demo) | 汇率转换应用示例 | 约 20 分钟 |
| [makepad-component](https://github.com/ZhangHanDong/makepad-component) | 可复用的 Makepad 组件库 | - |

### makepad-skills-demo 截图

<p align="center">
  <img src="./assets/skill-app-demo.jpg" width="60%" alt="汇率转换应用" />
</p>

### makepad-component 截图

<p align="center">
  <img src="./assets/mc1.png" width="45%" alt="组件 1" />
  <img src="./assets/mc2.png" width="45%" alt="组件 2" />
</p>
<p align="center">
  <img src="./assets/mc3.png" width="45%" alt="组件 3" />
  <img src="./assets/mc4.png" width="45%" alt="组件 4" />
</p>

## 资源

- [Makepad 仓库](https://github.com/makepad/makepad)
- [Makepad 示例](https://github.com/makepad/makepad/tree/main/examples)
- [Project Robius](https://github.com/project-robius)
- [Robrix](https://github.com/project-robius/robrix)
- [Moly](https://github.com/moxin-org/moly)

## 许可证

MIT

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
