---
id: github.com-ibelick-ui-skills.git-9a63b8d0-knowledg
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:08.854368
---

# KNOWLEDGE EXTRACT: github.com_ibelick_ui-skills.git_9a63b8d0
> **Extracted on:** 2026-04-01 08:47:23
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007519792/github.com_ibelick_ui-skills.git_9a63b8d0

---

## File: `.gitignore`
```
# build output
dist/

# generated types
.astro/

# dependencies
node_modules/

# logs
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*

# environment variables
.env
.env.production

# macOS-specific files
.DS_Store

# jetbrains setting folder
.idea/
```

## File: `.prettierignore`
```
dist
node_modules
.astro
```

## File: `.prettierrc.json`
```json
{
  "plugins": ["prettier-plugin-astro", "prettier-plugin-tailwindcss"],
  "overrides": [
    {
      "files": "*.astro",
      "options": {
        "parser": "astro"
      }
    }
  ]
}
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Julien Thibeaut

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
# UI Skills

![UI Skills](./public/cover.webp)

A set of skills to polish interfaces built by agents.

## Installation

```bash
npx skills add ibelick/ui-skills
```

## Add a specific skill

```bash
npx ui-skills add baseline-ui
npx ui-skills add fixing-accessibility
npx ui-skills add fixing-metadata
npx ui-skills add fixing-motion-performance
npx ui-skills add --all
```

## Usage

```bash
/baseline-ui review src/
```

## Available skills

| Skill                                                                    | Purpose                            |
| ------------------------------------------------------------------------ | ---------------------------------- |
| [baseline-ui](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)                             | opinionated UI baseline            |
| [fixing-accessibility](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)           | keyboard, labels, focus, semantics |
| [fixing-metadata](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)                     | correct titles, meta, social cards |
| [fixing-motion-performance](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | safe, performance-first UI motion  |

More on [ui-skills.com](http://ui-skills.com/)

## License

Licensed under the [MIT license](https://github.com/ibelick/ui-skills/blob/main/LICENSE).
```

## File: `astro.config.mjs`
```
import { defineConfig } from "astro/config";
import react from "@astrojs/react";
import tailwindcss from "@tailwindcss/vite";

// https://astro.build/config
export default defineConfig({
	integrations: [react()],
  vite: {
    plugins: [tailwindcss()],
    assetsInclude: ["**/*.sh"],
  },
});
```

## File: `install.sh`
```bash
#!/bin/sh
set -e

# UI Skills installer
# Installs the skill into project skill directories for Cursor and Claude,
# plus optional command locations for supported tools.

# Colors (only if stdout is a TTY)
if [ -t 1 ]; then
  BOLD="\033[1m"
  GREEN="\033[32m"
  YELLOW="\033[33m"
  GRAY="\033[37m"
  DARK="\033[90m"
  RESET="\033[0m"
else
  BOLD=""
  GREEN=""
  YELLOW=""
  GRAY=""
  DARK=""
  RESET=""
fi

print_header() {
  printf "${BOLD}%s${RESET}\n" "$1"
}

print_ascii() {
  B="${GRAY}"   # Blocks (Light Gray)
  D="${DARK}"   # Connectors (Dark Gray)
  R="${RESET}"

  printf " ${B}██${D}╗   ${B}██${D}╗${B}██${D}╗      ${B}███████${D}╗${B}██${D}╗  ${B}██${D}╗${B}██${D}╗${B}██${D}╗     ${B}██${D}╗     ${B}███████${D}╗\n"
  printf " ${B}██${D}║   ${B}██${D}║${B}██${D}║      ${B}██${D}╔════╝${B}██${D}║ ${B}██${D}╔╝${B}██${D}║${B}██${D}║     ${B}██${D}║     ${B}██${D}╔════╝\n"
  printf " ${B}██${D}║   ${B}██${D}║${B}██${D}║${B}█████${D}╗${B}███████${D}╗${B}█████${D}╔╝ ${B}██${D}║${B}██${D}║     ${B}██${D}║     ${B}███████${D}╗\n"
  printf " ${B}██${D}║   ${B}██${D}║${B}██${D}║${D}╚════╝╚════${B}██${D}║${B}██${D}╔═${B}██${D}╗ ${B}██${D}║${B}██${D}║     ${B}██${D}║     ${D}╚════${B}██${D}║\n"
  printf " ${D}╚${B}██████${D}╔╝${B}██${D}║      ${B}███████${D}║${B}██${D}║  ${B}██${D}╗${B}██${D}║${B}███████${D}╗${B}███████${D}╗${B}███████${D}║\n"
  printf "  ${D}╚═════╝ ╚═╝      ╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝${R}\n"
  printf "\n"
  printf "  ${DARK}The open taste layer for agent-generated UI.${R}\n"
}

print_success() {
  printf "${GREEN}✓${RESET} %s\n" "$1"
}

print_info() {
  printf "${YELLOW}→${RESET} %s\n" "$1"
}

print_dim() {
  printf "${DIM}%s${RESET}\n" "$1"
}

print_error() {
  printf "${BOLD}Error:${RESET} %s\n" "$1" >&2
}

# Configuration
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DEFAULT_SKILL="baseline-ui"
ALL_SKILLS="baseline-ui fixing-accessibility fixing-metadata fixing-motion-performance frontend-design"
UI_SKILLS_BASE_URL="${UI_SKILLS_BASE_URL:-https://ui-skills.com}"
SKILL_URL_BASE="${UI_SKILLS_BASE_URL%/}/skills"
REGISTRY_URL="${UI_SKILLS_REGISTRY_URL:-${SKILL_URL_BASE}/registry.txt}"
TRACKING_URL="https://collector.onedollarstats.com/events"
TRACKING_SOURCE="https://ui-skills.com/install"

if [ "$1" = "--all" ]; then
  SKILLS="$ALL_SKILLS"
elif [ -n "$1" ]; then
  SKILLS="$1"
else
  SKILLS="$DEFAULT_SKILL"
fi

if [ "$SKILLS" != "${SKILLS#* }" ]; then
  COMPACT_OUTPUT=1
else
  COMPACT_OUTPUT=0
fi

track_install() {
  command_name="${UI_SKILLS_COMMAND:-install}"
  subcommand_name="${UI_SKILLS_SUBCOMMAND:-}"
  payload=$(printf '{"u":"%s","e":[{"t":"install","p":{"command":"%s","subcommand":"%s"}}]}' "$TRACKING_SOURCE" "$command_name" "$subcommand_name")
  data=$(printf '%s' "$payload" | base64 | tr -d '\n')
  url="${TRACKING_URL}?data=${data}"

  if command -v curl >/dev/null 2>&1; then
    curl -fsS "$url" >/dev/null 2>&1 || true
  elif command -v wget >/dev/null 2>&1; then
    wget -q -O /dev/null "$url" >/dev/null 2>&1 || true
  fi
}

track_install
print_ascii
printf "\n"

# Prepare temp files for raw skill and command content
TMP_SKILL="$(mktemp)"
TMP_COMMAND="$(mktemp)"
TMP_REGISTRY="$(mktemp)"
REGISTRY_CACHED=0

cleanup() {
  rm -f "$TMP_SKILL" "$TMP_COMMAND" "$TMP_REGISTRY"
}
trap cleanup EXIT

ensure_registry_cache() {
  if [ "$REGISTRY_CACHED" -eq 1 ]; then
    return
  fi

  if command -v curl >/dev/null 2>&1; then
    curl -fsSL "$REGISTRY_URL" -o "$TMP_REGISTRY" >/dev/null 2>&1 || true
  elif command -v wget >/dev/null 2>&1; then
    wget -q "$REGISTRY_URL" -O "$TMP_REGISTRY" >/dev/null 2>&1 || true
  else
    : > "$TMP_REGISTRY"
  fi

  REGISTRY_CACHED=1
}

get_registry_url() {
  skill_slug="$1"
  ensure_registry_cache

  if [ ! -s "$TMP_REGISTRY" ]; then
    return
  fi

  awk -F '\t' -v slug="$skill_slug" '$1 == slug {print $2; exit}' "$TMP_REGISTRY"
}

download_skill() {
  skill_slug="$1"
  registry_url="$(get_registry_url "$skill_slug")"
  if [ -n "$registry_url" ]; then
    skill_url="$registry_url"
  else
    skill_url="$SKILL_URL_BASE/$skill_slug/llms.txt"
  fi
  local_skill="${SCRIPT_DIR}/skills/${skill_slug}/SKILL.md"

  if [ -f "$local_skill" ]; then
    cp "$local_skill" "$TMP_SKILL"
    cp "$TMP_SKILL" "$TMP_COMMAND"
    return
  fi

  print_info "Downloading..."
  if command -v curl >/dev/null 2>&1; then
    curl -fsSL "$skill_url" -o "$TMP_SKILL"
  elif command -v wget >/dev/null 2>&1; then
    wget -q "$skill_url" -O "$TMP_SKILL"
  else
    print_error "Neither curl nor wget found. Please install one of them."
    exit 1
  fi

  if [ ! -s "$TMP_SKILL" ]; then
    print_error "Download failed or returned empty content."
    exit 1
  fi

  cp "$TMP_SKILL" "$TMP_COMMAND"
}

OPTIONAL_INSTALLED=0
SKILL_INSTALLED=0

install_skill() {
  base_dir="$1"
  label="$2"
  skill_dir="$base_dir/$INSTALL_DIRNAME"
  skill_file="$skill_dir/SKILL.md"
  mkdir -p "$skill_dir"
  cp "$TMP_SKILL" "$skill_file"
  if [ "$COMPACT_OUTPUT" -eq 0 ]; then
    print_success "$label skill installed"
  fi
  OPTIONAL_INSTALLED=$((OPTIONAL_INSTALLED + 1))
  SKILL_INSTALLED=$((SKILL_INSTALLED + 1))
}

maybe_install_project_skill() {
  base_dir="$1"
  label="$2"
  skill_dir="$base_dir/$INSTALL_DIRNAME"
  skill_file="$skill_dir/SKILL.md"
  if [ -d "$base_dir" ]; then
    mkdir -p "$skill_dir"
    cp "$TMP_SKILL" "$skill_file"
    if [ "$COMPACT_OUTPUT" -eq 0 ]; then
      print_success "$label project skill installed"
    fi
    OPTIONAL_INSTALLED=$((OPTIONAL_INSTALLED + 1))
    SKILL_INSTALLED=$((SKILL_INSTALLED + 1))
  fi
}

for SKILL_SLUG in $SKILLS; do
  INSTALL_DIRNAME="$SKILL_SLUG"
  INSTALL_NAME="${SKILL_SLUG}.md"
  SKILL_INSTALLED=0

  print_info "Installing ${SKILL_SLUG}..."
  download_skill "$SKILL_SLUG"
  printf "\n"

  # Project skills (auto-detect)
  maybe_install_project_skill "${PWD}/.opencode/skill" "OpenCode"
  maybe_install_project_skill "${PWD}/.claude/skills" "Claude Code"
  maybe_install_project_skill "${PWD}/.codex/skills" "Codex"
  maybe_install_project_skill "${PWD}/.cursor/skills" "Cursor"
  maybe_install_project_skill "${PWD}/.kilocode/skills" "Kilo Code"
  maybe_install_project_skill "${PWD}/.roo/skills" "Roo Code"
  maybe_install_project_skill "${PWD}/.goose/skills" "Goose"
  maybe_install_project_skill "${PWD}/.gemini/skills" "Gemini CLI"
  maybe_install_project_skill "${PWD}/.agent/skills" "Antigravity"
  maybe_install_project_skill "${PWD}/.github/skills" "GitHub Copilot"
  maybe_install_project_skill "${PWD}/.factory/skills" "Droid"
  maybe_install_project_skill "${PWD}/.windsurf/skills" "Windsurf"

  # Claude Code (project commands)
  if [ -d "${PWD}/.claude" ]; then
    CLAUDE_PROJECT_COMMAND_DIR="${PWD}/.claude/commands"
    mkdir -p "$CLAUDE_PROJECT_COMMAND_DIR"
    cp "$TMP_COMMAND" "$CLAUDE_PROJECT_COMMAND_DIR/$INSTALL_NAME"
    if [ "$COMPACT_OUTPUT" -eq 0 ]; then
      print_success "Claude project command installed"
    fi
    OPTIONAL_INSTALLED=$((OPTIONAL_INSTALLED + 1))
    SKILL_INSTALLED=$((SKILL_INSTALLED + 1))
  fi

  # Cursor (project commands)
  if [ -d "${PWD}/.cursor" ]; then
    CURSOR_PROJECT_COMMAND_DIR="${PWD}/.cursor/commands"
    mkdir -p "$CURSOR_PROJECT_COMMAND_DIR"
    cp "$TMP_COMMAND" "$CURSOR_PROJECT_COMMAND_DIR/$INSTALL_NAME"
    if [ "$COMPACT_OUTPUT" -eq 0 ]; then
      print_success "Cursor project command installed"
    fi
    OPTIONAL_INSTALLED=$((OPTIONAL_INSTALLED + 1))
    SKILL_INSTALLED=$((SKILL_INSTALLED + 1))
  fi

  # Claude Code (personal skills directory, if detected)
  CLAUDE_SKILLS_DIR=""
  if [ -n "$CLAUDE_CODE_SKILLS_DIR" ]; then
    CLAUDE_SKILLS_DIR="$CLAUDE_CODE_SKILLS_DIR"
  elif [ -d "$HOME/.claude/skills" ]; then
    CLAUDE_SKILLS_DIR="$HOME/.claude/skills"
  elif [ -d "$HOME/.config/claude/skills" ]; then
    CLAUDE_SKILLS_DIR="$HOME/.config/claude/skills"
  fi

  if [ -n "$CLAUDE_SKILLS_DIR" ]; then
    install_skill "$CLAUDE_SKILLS_DIR" "Claude Code"
  fi

  # OpenCode (skills folder)
  if [ -d "$HOME/.config/opencode/skill" ]; then
    install_skill "$HOME/.config/opencode/skill" "OpenCode"
  fi

  # Codex (skills folder)
  if [ -d "$HOME/.codex/skills" ]; then
    install_skill "$HOME/.codex/skills" "Codex"
  fi

  # Cursor (skills folder)
  if [ -d "$HOME/.cursor/skills" ]; then
    install_skill "$HOME/.cursor/skills" "Cursor"
  fi

  # Amp (skills folder)
  if [ -d "$HOME/.config/agents/skills" ]; then
    install_skill "$HOME/.config/agents/skills" "Amp"
  fi

  # Kilo Code (skills folder)
  if [ -d "$HOME/.kilocode/skills" ]; then
    install_skill "$HOME/.kilocode/skills" "Kilo Code"
  fi

  # Roo Code (skills folder)
  if [ -d "$HOME/.roo/skills" ]; then
    install_skill "$HOME/.roo/skills" "Roo Code"
  fi

  # Goose (skills folder)
  if [ -d "$HOME/.config/goose/skills" ]; then
    install_skill "$HOME/.config/goose/skills" "Goose"
  fi

  # Gemini CLI (skills folder)
  if [ -d "$HOME/.gemini/skills" ]; then
    install_skill "$HOME/.gemini/skills" "Gemini CLI"
  fi

  # Antigravity (skills folder)
  if [ -d "$HOME/.gemini/antigravity/skills" ]; then
    install_skill "$HOME/.gemini/antigravity/skills" "Antigravity"
  fi

  # GitHub Copilot (skills folder)
  if [ -d "$HOME/.copilot/skills" ]; then
    install_skill "$HOME/.copilot/skills" "GitHub Copilot"
  fi

  # Clawdbot (skills folder)
  if [ -d "$HOME/.clawdbot/skills" ]; then
    install_skill "$HOME/.clawdbot/skills" "Clawdbot"
  fi

  # Droid (skills folder)
  if [ -d "$HOME/.factory/skills" ]; then
    install_skill "$HOME/.factory/skills" "Droid"
  fi

  # Windsurf (skills folder)
  if [ -d "$HOME/.codeium/windsurf/skills" ]; then
    install_skill "$HOME/.codeium/windsurf/skills" "Windsurf"
  fi

  # OpenCode (command folder)
  if command -v opencode >/dev/null 2>&1 || [ -d "$HOME/.config/opencode" ]; then
    OPENCODE_COMMAND_DIR="$HOME/.config/opencode/command"
    mkdir -p "$OPENCODE_COMMAND_DIR"
    cp "$TMP_COMMAND" "$OPENCODE_COMMAND_DIR/$INSTALL_NAME"
    if [ "$COMPACT_OUTPUT" -eq 0 ]; then
      print_success "OpenCode command installed"
    fi
    OPTIONAL_INSTALLED=$((OPTIONAL_INSTALLED + 1))
    SKILL_INSTALLED=$((SKILL_INSTALLED + 1))
  fi

  # Cursor (commands folder)
  if [ -d "$HOME/.cursor" ]; then
    CURSOR_COMMAND_DIR="$HOME/.cursor/commands"
    mkdir -p "$CURSOR_COMMAND_DIR"
    cp "$TMP_COMMAND" "$CURSOR_COMMAND_DIR/$INSTALL_NAME"
    if [ "$COMPACT_OUTPUT" -eq 0 ]; then
      print_success "Cursor command installed"
    fi
    OPTIONAL_INSTALLED=$((OPTIONAL_INSTALLED + 1))
    SKILL_INSTALLED=$((SKILL_INSTALLED + 1))
  fi

  # Claude Code (commands folder)
  if [ -d "$HOME/.claude" ] || [ -d "$HOME/.config/claude" ]; then
    if [ -d "$HOME/.claude" ]; then
      CLAUDE_COMMAND_DIR="$HOME/.claude/commands"
    else
      CLAUDE_COMMAND_DIR="$HOME/.config/claude/commands"
    fi
    mkdir -p "$CLAUDE_COMMAND_DIR"
    cp "$TMP_COMMAND" "$CLAUDE_COMMAND_DIR/$INSTALL_NAME"
    if [ "$COMPACT_OUTPUT" -eq 0 ]; then
      print_success "Claude Code command installed"
    fi
    OPTIONAL_INSTALLED=$((OPTIONAL_INSTALLED + 1))
    SKILL_INSTALLED=$((SKILL_INSTALLED + 1))
  fi

  # Windsurf (append to global_rules.md)
  MARKER="# UI Skills"
  if [ -d "$HOME/.codeium" ] || [ -d "$HOME/Library/Application Support/Windsurf" ]; then
    WINDSURF_DIR="$HOME/.codeium/windsurf/memories"
    RULES_FILE="$WINDSURF_DIR/global_rules.md"
    mkdir -p "$WINDSURF_DIR"
    if [ -f "$RULES_FILE" ] && grep -q "$MARKER" "$RULES_FILE"; then
      if [ "$COMPACT_OUTPUT" -eq 0 ]; then
        print_success "Windsurf already updated"
      fi
    else
      if [ -f "$RULES_FILE" ]; then
        printf "\n" >> "$RULES_FILE"
      fi
      printf "%s\n\n" "$MARKER" >> "$RULES_FILE"
      cat "$TMP_COMMAND" >> "$RULES_FILE"
      printf "\n" >> "$RULES_FILE"
      if [ "$COMPACT_OUTPUT" -eq 0 ]; then
        print_success "Windsurf updated"
      fi
    fi
    OPTIONAL_INSTALLED=$((OPTIONAL_INSTALLED + 1))
    SKILL_INSTALLED=$((SKILL_INSTALLED + 1))
  fi

  # Gemini CLI (TOML command format)
  if command -v gemini >/dev/null 2>&1 || [ -d "$HOME/.gemini" ]; then
    GEMINI_DIR="$HOME/.gemini/commands"
    TOML_FILE="$GEMINI_DIR/${SKILL_SLUG}.toml"
    mkdir -p "$GEMINI_DIR"
    cat > "$TOML_FILE" << 'TOMLEOF'
description = "Review UI code with UI Skills constraints"
prompt = """
TOMLEOF
    cat "$TMP_COMMAND" >> "$TOML_FILE"
    printf "\n\"\"\"\n" >> "$TOML_FILE"
    if [ "$COMPACT_OUTPUT" -eq 0 ]; then
      print_success "Gemini CLI command installed"
    fi
    OPTIONAL_INSTALLED=$((OPTIONAL_INSTALLED + 1))
    SKILL_INSTALLED=$((SKILL_INSTALLED + 1))
  fi

  if [ "$COMPACT_OUTPUT" -eq 1 ]; then
    if [ "$SKILL_INSTALLED" -eq 0 ]; then
      print_info "${SKILL_SLUG} installed (no tool locations detected)"
    else
      print_success "${SKILL_SLUG} installed in ${SKILL_INSTALLED} locations"
    fi
  fi
done

printf "\n"

if [ "$OPTIONAL_INSTALLED" -eq 0 ]; then
  print_dim "No additional tool locations detected."
  print_dim "Create a tool's skills directory and rerun to install automatically."
fi

print_header "Done"
print_info "Usage: /ui-skills path/to/file.tsx"
printf "\n"
```

## File: `package.json`
```json
{
  "name": "ui-skills",
  "type": "module",
  "version": "0.1.5",
  "license": "MIT",
  "bin": {
    "ui-skills": "./bin/ui-skills.cjs"
  },
  "scripts": {
    "dev": "astro dev",
    "build": "astro build",
    "preview": "astro preview",
    "astro": "astro",
    "format": "prettier --write .",
    "typecheck": "astro check"
  },
  "dependencies": {
    "@astrojs/react": "^4.4.2",
    "@tailwindcss/vite": "^4.1.18",
    "@types/react": "^19.2.7",
    "@types/react-dom": "^19.2.3",
    "astro": "^5.16.7",
    "marked": "^17.0.1",
    "motion": "^12.24.12",
    "react": "^19.2.3",
    "react-dom": "^19.2.3",
    "tailwindcss": "^4.1.18"
  },
  "devDependencies": {
    "@tailwindcss/typography": "^0.5.19",
    "@types/marked": "^5.0.2",
    "prettier": "^3.3.3",
    "prettier-plugin-astro": "^0.14.1",
    "prettier-plugin-tailwindcss": "^0.6.8",
    "typescript": "^5.6.3"
  },
  "publishConfig": {
    "access": "public"
  }
}
```

## File: `tsconfig.json`
```json
{
  "extends": "astro/tsconfigs/strict",
  "include": [
    ".astro/types.d.ts",
    "**/*"
  ],
  "exclude": [
    "dist"
  ],
  "compilerOptions": {
    "jsx": "react-jsx",
    "jsxImportSource": "react"
  }
}
```

## File: `wrangler.jsonc`
```
{
    "name": "ui-skills",
    "compatibility_date": "2026-01-07",
    "assets": {
      "directory": "./dist"
    }
  }
```

## File: `wrangler.toml`
```
name = "ui-skills"
compatibility_date = "2026-01-07"

[assets]
directory = "./dist"
```

## File: `skills/baseline-ui/SKILL.md`
```markdown
---
name: baseline-ui
description: Validates animation durations, enforces typography scale, checks component accessibility, and prevents layout anti-patterns in Tailwind CSS projects. Use when building UI components, reviewing CSS utilities, styling React views, or enforcing design consistency.
---

# Baseline UI

Enforces an opinionated UI baseline to prevent AI-generated interface slop.

## How to use

- `/baseline-ui`
  Apply these constraints to any UI work in this conversation.

- `/baseline-ui <file>`
  Review the file against all constraints below and output:
  - violations (quote the exact line/snippet)
  - why it matters (1 short sentence)
  - a concrete fix (code-level suggestion)

## Stack

- MUST use Tailwind CSS defaults unless custom values already exist or are explicitly requested
- MUST use `motion/react` (formerly `framer-motion`) when JavaScript animation is required
- SHOULD use `tw-animate-css` for entrance and micro-animations in Tailwind CSS
- MUST use `cn` utility (`clsx` + `tailwind-merge`) for class logic

## Components

- MUST use accessible component primitives for anything with keyboard or focus behavior (`Base UI`, `React Aria`, `Radix`)
- MUST use the project’s existing component primitives first
- NEVER mix primitive systems within the same interaction surface
- SHOULD prefer [`Base UI`](https://base-ui.com/react/components) for new primitives if compatible with the stack
- MUST add an `aria-label` to icon-only buttons
- NEVER rebuild keyboard or focus behavior by hand unless explicitly requested

## Interaction

- MUST use an `AlertDialog` for destructive or irreversible actions
- SHOULD use structural skeletons for loading states
- NEVER use `h-screen`, use `h-dvh`
- MUST respect `safe-area-inset` for fixed elements
- MUST show errors next to where the action happens
- NEVER block paste in `input` or `textarea` elements

## Animation

- NEVER add animation unless it is explicitly requested
- MUST animate only compositor props (`transform`, `opacity`)
- NEVER animate layout properties (`width`, `height`, `top`, `left`, `margin`, `padding`)
- SHOULD avoid animating paint properties (`background`, `color`) except for small, local UI (text, icons)
- SHOULD use `ease-out` on entrance
- NEVER exceed `200ms` for interaction feedback
- MUST pause looping animations when off-screen
- SHOULD respect `prefers-reduced-motion`
- NEVER introduce custom easing curves unless explicitly requested
- SHOULD avoid animating large images or full-screen surfaces

## Typography

- MUST use `text-balance` for headings and `text-pretty` for body/paragraphs
- MUST use `tabular-nums` for data
- SHOULD use `truncate` or `line-clamp` for dense UI
- NEVER modify `letter-spacing` (`tracking-*`) unless explicitly requested

## Layout

- MUST use a fixed `z-index` scale (no arbitrary `z-*`)
- SHOULD use `size-*` for square elements instead of `w-*` + `h-*`

## Performance

- NEVER animate large `blur()` or `backdrop-filter` surfaces
- NEVER apply `will-change` outside an active animation
- NEVER use `useEffect` for anything that can be expressed as render logic

## Design

- NEVER use gradients unless explicitly requested
- NEVER use purple or multicolor gradients
- NEVER use glow effects as primary affordances
- SHOULD use Tailwind CSS default shadow scale unless explicitly requested
- MUST give empty states one clear next action
- SHOULD limit accent color usage to one per view
- SHOULD use existing theme or Tailwind CSS color tokens before introducing new ones
```

## File: `skills/fixing-accessibility/SKILL.md`
```markdown
---
name: fixing-accessibility
description: Audit and fix HTML accessibility issues including ARIA labels, keyboard navigation, focus management, color contrast, and form errors. Use when adding interactive controls, forms, dialogs, or reviewing WCAG compliance.
---

# fixing-accessibility

Fix accessibility issues.

## how to use

- `/fixing-accessibility`
  Apply these constraints to any UI work in this conversation.

- `/fixing-accessibility <file>`
  Review the file against all rules below and report:
  - violations (quote the exact line or snippet)
  - why it matters (one short sentence)
  - a concrete fix (code-level suggestion)

Do not rewrite large parts of the UI. Prefer minimal, targeted fixes.

## when to apply

Reference these guidelines when:
- adding or changing buttons, links, inputs, menus, dialogs, tabs, dropdowns
- building forms, validation, error states, helper text
- implementing keyboard shortcuts or custom interactions
- working on focus states, focus trapping, or modal behavior
- rendering icon-only controls
- adding hover-only interactions or hidden content

## rule categories by priority

| priority | category | impact |
|----------|----------|--------|
| 1 | accessible names | critical |
| 2 | keyboard access | critical |
| 3 | focus and dialogs | critical |
| 4 | semantics | high |
| 5 | forms and errors | high |
| 6 | announcements | medium-high |
| 7 | contrast and states | medium |
| 8 | media and motion | low-medium |
| 9 | tool boundaries | critical |

## quick reference

### 1. accessible names (critical)

- every interactive control must have an accessible name
- icon-only buttons must have aria-label or aria-labelledby
- every input, select, and textarea must be labeled
- links must have meaningful text (no “click here”)
- decorative icons must be aria-hidden

### 2. keyboard access (critical)

- do not use div or span as buttons without full keyboard support
- all interactive elements must be reachable by Tab
- focus must be visible for keyboard users
- do not use tabindex greater than 0
- Escape must close dialogs or overlays when applicable

### 3. focus and dialogs (critical)

- modals must trap focus while open
- restore focus to the trigger on close
- set initial focus inside dialogs
- opening a dialog should not scroll the page unexpectedly

### 4. semantics (high)

- prefer native elements (button, a, input) over role-based hacks
- if a role is used, required aria attributes must be present
- lists must use ul or ol with li
- do not skip heading levels
- tables must use th for headers when applicable

### 5. forms and errors (high)

- errors must be linked to fields using aria-describedby
- required fields must be announced
- invalid fields must set aria-invalid
- helper text must be associated with inputs
- disabled submit actions must explain why

### 6. announcements (medium-high)

- critical form errors should use aria-live
- loading states should use aria-busy or status text
- toasts must not be the only way to convey critical information
- expandable controls must use aria-expanded and aria-controls

### 7. contrast and states (medium)

- ensure sufficient contrast for text and icons
- hover-only interactions must have keyboard equivalents
- disabled states must not rely on color alone
- do not remove focus outlines without a visible replacement

### 8. media and motion (low-medium)

- images must have correct alt text (meaningful or empty)
- videos with speech should provide captions when relevant
- respect prefers-reduced-motion for non-essential motion
- avoid autoplaying media with sound

### 9. tool boundaries (critical)

- prefer minimal changes, do not refactor unrelated code
- do not add aria when native semantics already solve the problem
- do not migrate UI libraries unless requested

## common fixes

```html
<!-- icon-only button: add aria-label -->
<!-- before --> <button><svg>...</svg></button>
<!-- after -->  <button aria-label="Close"><svg aria-hidden="true">...</svg></button>

<!-- div as button: use native element -->
<!-- before --> <div onclick="save()">Save</div>
<!-- after -->  <button onclick="save()">Save</button>

<!-- form error: link with aria-describedby -->
<!-- before --> <input id="email" /> <span>Invalid email</span>
<!-- after -->  <input id="email" aria-describedby="email-err" aria-invalid="true" /> <span id="email-err">Invalid email</span>
```

## review guidance

- fix critical issues first (names, keyboard, focus, tool boundaries)
- prefer native HTML before adding aria
- quote the exact snippet, state the failure, propose a small fix
- for complex widgets (menu, dialog, combobox), prefer established accessible primitives over custom behavior
```

## File: `skills/fixing-metadata/SKILL.md`
```markdown
---
name: fixing-metadata
description: >
  Audit and fix HTML metadata including page titles, meta descriptions, canonical URLs, Open Graph
  tags, Twitter cards, favicons, JSON-LD structured data, and robots directives. Use when adding
  SEO metadata, fixing social share previews, reviewing Open Graph tags, setting up canonical URLs,
  or shipping new pages that need correct meta tags.
version: 1.0.1
license: MIT
---

## Workflow

1. Identify pages with missing or incorrect metadata (titles, descriptions, canonical, OG tags)
2. Audit against the priority rules below — fix critical issues (duplicates, indexing) first
3. Ensure title, description, canonical, and og:url all agree with each other
4. Verify social cards render correctly on a real URL, not localhost
5. Keep diffs minimal and scoped to metadata only — do not refactor unrelated code
## when to apply

Reference these guidelines when:
- adding or changing page titles, descriptions, canonical, robots
- implementing Open Graph or Twitter card metadata
- setting favicons, app icons, manifest, theme-color
- building shared SEO components or layout metadata defaults
- adding structured data (JSON-LD)
- changing locale, alternate languages, or canonical routing
- shipping new pages, marketing pages, or shareable links

## rule categories by priority

| priority | category | impact |
|----------|----------|--------|
| 1 | correctness and duplication | critical |
| 2 | title and description | high |
| 3 | canonical and indexing | high |
| 4 | social cards | high |
| 5 | icons and manifest | medium |
| 6 | structured data | medium |
| 7 | locale and alternates | low-medium |
| 8 | tool boundaries | critical |

## quick reference

### 1. correctness and duplication (critical)

- define metadata in one place per page, avoid competing systems
- do not emit duplicate title, description, canonical, or robots tags
- metadata must be deterministic, no random or unstable values
- escape and sanitize any user-generated or dynamic strings
- every page must have safe defaults for title and description

### 2. title and description (high)

- every page must have a title
- use a consistent title format across the site
- keep titles short and readable, avoid stuffing
- shareable or searchable pages should have a meta description
- descriptions must be plain text, no markdown or quote spam

### 3. canonical and indexing (high)

- canonical must point to the preferred URL for the page
- use noindex only for private, duplicate, or non-public pages
- robots meta must match actual access intent
- previews or staging pages should be noindex by default when possible
- paginated pages must have correct canonical behavior

### 4. social cards (high)

- shareable pages must set Open Graph title, description, and image
- Open Graph and Twitter images must use absolute URLs
- prefer correct image dimensions and stable aspect ratios
- og:url must match the canonical URL
- use a sensible og:type, usually website or article
- set twitter:card appropriately, summary_large_image by default

### 5. icons and manifest (medium)

- include at least one favicon that works across browsers
- include apple-touch-icon when relevant
- manifest must be valid and referenced when used
- set theme-color intentionally to avoid mismatched UI chrome
- icon paths should be stable and cacheable

### 6. structured data (medium)

- do not add JSON-LD unless it clearly maps to real page content
- JSON-LD must be valid and reflect what is actually rendered
- do not invent ratings, reviews, prices, or organization details
- prefer one structured data block per page unless required

### 7. locale and alternates (low-medium)

- set the html lang attribute correctly
- set og:locale when localization exists
- add hreflang alternates only when pages truly exist
- localized pages must canonicalize correctly per locale

### 8. tool boundaries (critical)

- prefer minimal changes, do not refactor unrelated code
- do not migrate frameworks or SEO libraries unless requested
- follow the project's existing metadata pattern (Next.js metadata API, react-helmet, manual head, etc.)

## review guidance

- fix critical issues first (duplicates, canonical, indexing)
- ensure title, description, canonical, and og:url agree
- verify social cards on a real URL, not localhost
- prefer stable, boring metadata over clever or dynamic
- keep diffs minimal and scoped to metadata only
```

## File: `skills/fixing-motion-performance/SKILL.md`
```markdown
---
name: fixing-motion-performance
description: Audit and fix animation performance issues including layout thrashing, compositor properties, scroll-linked motion, and blur effects. Use when animations stutter, transitions jank, or reviewing CSS/JS animation performance.
---

# fixing-motion-performance

Fix animation performance issues.

## how to use

- `/fixing-motion-performance`
  Apply these constraints to any UI animation work in this conversation.

- `/fixing-motion-performance <file>`
  Review the file against all rules below and report:
  - violations (quote the exact line or snippet)
  - why it matters (one short sentence)
  - a concrete fix (code-level suggestion)

Do not migrate animation libraries unless explicitly requested. Apply rules within the existing stack.

## when to apply

Reference these guidelines when:
- adding or changing UI animations (CSS, WAAPI, Motion, rAF, GSAP)
- refactoring janky interactions or transitions
- implementing scroll-linked motion or reveal-on-scroll
- animating layout, filters, masks, gradients, or CSS variables
- reviewing components that use will-change, transforms, or measurement

## rendering steps glossary

- composite: transform, opacity
- paint: color, borders, gradients, masks, images, filters
- layout: size, position, flow, grid, flex

## rule categories by priority

| priority | category | impact |
|----------|----------|--------|
| 1 | never patterns | critical |
| 2 | choose the mechanism | critical |
| 3 | measurement | high |
| 4 | scroll | high |
| 5 | paint | medium-high |
| 6 | layers | medium |
| 7 | blur and filters | medium |
| 8 | view transitions | low |
| 9 | tool boundaries | critical |

## quick reference

### 1. never patterns (critical)

- do not interleave layout reads and writes in the same frame
- do not animate layout continuously on large or meaningful surfaces
- do not drive animation from scrollTop, scrollY, or scroll events
- no requestAnimationFrame loops without a stop condition
- do not mix multiple animation systems that each measure or mutate layout

### 2. choose the mechanism (critical)

- default to transform and opacity for motion
- use JS-driven animation only when interaction requires it
- paint or layout animation is acceptable only on small, isolated surfaces
- one-shot effects are acceptable more often than continuous motion
- prefer downgrading technique over removing motion entirely

### 3. measurement (high)

- measure once, then animate via transform or opacity
- batch all DOM reads before writes
- do not read layout repeatedly during an animation
- prefer FLIP-style transitions for layout-like effects
- prefer approaches that batch measurement and writes

### 4. scroll (high)

- prefer Scroll or View Timelines for scroll-linked motion when available
- use IntersectionObserver for visibility and pausing
- do not poll scroll position for animation
- pause or stop animations when off-screen
- scroll-linked motion must not trigger continuous layout or paint on large surfaces

### 5. paint (medium-high)

- paint-triggering animation is allowed only on small, isolated elements
- do not animate paint-heavy properties on large containers
- do not animate CSS variables for transform, opacity, or position
- do not animate inherited CSS variables
- scope animated CSS variables locally and avoid inheritance

### 6. layers (medium)

- compositor motion requires layer promotion, never assume it
- use will-change temporarily and surgically
- avoid many or large promoted layers
- validate layer behavior with tooling when performance matters

### 7. blur and filters (medium)

- keep blur animation small (<=8px)
- use blur only for short, one-time effects
- never animate blur continuously
- never animate blur on large surfaces
- prefer opacity and translate before blur

### 8. view transitions (low)

- use view transitions only for navigation-level changes
- avoid view transitions for interaction-heavy UI
- avoid view transitions when interruption or cancellation is required
- treat size changes as potentially layout-triggering

### 9. tool boundaries (critical)

- do not migrate or rewrite animation libraries unless explicitly requested
- apply these rules within the existing animation system
- never partially migrate APIs or mix styles within the same component

## common fixes

```css
/* layout thrashing: animate transform instead of width */
/* before */ .panel { transition: width 0.3s; }
/* after */  .panel { transition: transform 0.3s; }

/* scroll-linked: use scroll-timeline instead of JS */
/* before */ window.addEventListener('scroll', () => el.style.opacity = scrollY / 500)
/* after */  .reveal { animation: fade-in linear; animation-timeline: view(); }
```

```js
// measurement: batch reads before writes (FLIP)
// before — layout thrash
el.style.left = el.getBoundingClientRect().left + 10 + 'px';
// after — measure once, animate via transform
const first = el.getBoundingClientRect();
el.classList.add('moved');
const last = el.getBoundingClientRect();
el.style.transform = `translateX(${first.left - last.left}px)`;
requestAnimationFrame(() => { el.style.transition = 'transform 0.3s'; el.style.transform = ''; });
```

## review guidance

- enforce critical rules first (never patterns, tool boundaries)
- choose the least expensive rendering work that matches the intent
- for any non-default choice, state the constraint that justifies it (surface size, duration, or interaction requirement)
- when reviewing, prefer actionable notes and concrete alternatives over theory
```

## File: `src/data/registry.ts`
```typescript
export type RegistrySkill = {
  slug: string;
  user: string;
  repo: string;
  rawUrl: string;
  githubUrl: string;
  name: string;
  description: string;
};

export const registry: RegistrySkill[] = [
  {
    slug: "frontend-design",
    user: "anthropics",
    repo: "skills",
    rawUrl:
      "https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md",
    githubUrl:
      "https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md",
    name: "frontend-design",
    description:
      "Create distinctive, production-grade frontend interfaces with high design quality. Generates creative, polished code and UI design that avoids generic AI aesthetics.",
  },
  {
    slug: "web-design-guidelines",
    user: "vercel-labs",
    repo: "agent-skills",
    rawUrl:
      "https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/web-design-guidelines/SKILL.md",
    githubUrl:
      "https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md",
    name: "web-design-guidelines",
    description:
      "Review UI code for Web Interface Guidelines compliance. Audit design, accessibility, and UX against Vercel's best practices.",
  },
  {
    slug: "ui-ux-pro-max",
    user: "nextlevelbuilder",
    repo: "ui-ux-pro-max-skill",
    rawUrl:
      "https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/main/.claude/skills/ui-ux-pro-max/SKILL.md",
    githubUrl:
      "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/ui-ux-pro-max/SKILL.md",
    name: "ui-ux-pro-max",
    description:
      "Comprehensive UI/UX design intelligence with 50+ styles, 97 palettes, and 9 technology stacks for building professional interfaces.",
  },
  {
    slug: "interaction-design",
    user: "wshobson",
    repo: "agents",
    rawUrl:
      "https://raw.githubusercontent.com/wshobson/agents/main/plugins/ui-design/skills/interaction-design/SKILL.md",
    githubUrl:
      "https://github.com/wshobson/agents/blob/main/plugins/ui-design/skills/interaction-design/SKILL.md",
    name: "interaction-design",
    description:
      "Design and implement microinteractions, motion design, transitions, and user feedback patterns for delightful user experiences.",
  },
  {
    slug: "swiftui-ui-patterns",
    user: "dimillian",
    repo: "skills",
    rawUrl:
      "https://raw.githubusercontent.com/dimillian/skills/main/swiftui-ui-patterns/SKILL.md",
    githubUrl:
      "https://github.com/dimillian/skills/blob/main/swiftui-ui-patterns/SKILL.md",
    name: "swiftui-ui-patterns",
    description:
      "Best practices and example-driven guidance for building SwiftUI views and components. Includes tab architecture and screen composition.",
  },
  {
    slug: "interface-design",
    user: "Dammyjay93",
    repo: "interface-design",
    rawUrl:
      "https://raw.githubusercontent.com/Dammyjay93/interface-design/main/.claude/skills/interface-design/SKILL.md",
    githubUrl:
      "https://github.com/Dammyjay93/interface-design/blob/main/.claude/skills/interface-design/SKILL.md",
    name: "interface-design",
    description:
      "Specialized skill for interface design: dashboards, admin panels, and SaaS apps. Focused on craft and consistency.",
  },
  {
    slug: "wcag-audit-patterns",
    user: "wshobson",
    repo: "agents",
    rawUrl:
      "https://raw.githubusercontent.com/wshobson/agents/main/plugins/accessibility-compliance/skills/wcag-audit-patterns/SKILL.md",
    githubUrl:
      "https://github.com/wshobson/agents/blob/main/plugins/accessibility-compliance/skills/wcag-audit-patterns/SKILL.md",
    name: "wcag-audit-patterns",
    description:
      "Conduct WCAG 2.2 accessibility audits with automated testing, manual verification, and remediation guidance. Use when auditing websites for accessibility, fixing WCAG violations, or implementing accessible design patterns.",
  },
  {
    slug: "canvas-design",
    user: "anthropics",
    repo: "skills",
    rawUrl:
      "https://raw.githubusercontent.com/anthropics/skills/main/skills/canvas-design/SKILL.md",
    githubUrl:
      "https://github.com/anthropics/skills/blob/main/skills/canvas-design/SKILL.md",
    name: "canvas-design",
    description:
      "Create original visual designs and art on digital canvases using design philosophy, focusing on form, space, and color.",
  },
  {
    slug: "12-principles-of-animation",
    user: "raphaelsalaja",
    repo: "userinterface-wiki",
    rawUrl:
      "https://raw.githubusercontent.com/raphaelsalaja/userinterface-wiki/main/skills/12-principles-of-animation/SKILL.md",
    githubUrl:
      "https://github.com/raphaelsalaja/userinterface-wiki/blob/main/skills/12-principles-of-animation/SKILL.md",
    name: "12-principles-of-animation",
    description:
      "Apply Disney's 12 animation principles to web interfaces to make motion feel natural, organic, and human.",
  },
  {
    slug: "design-lab",
    user: "0xdesign",
    repo: "design-plugin",
    rawUrl:
      "https://raw.githubusercontent.com/0xdesign/design-plugin/main/design-and-refine/skills/design-lab/SKILL.md",
    githubUrl:
      "https://github.com/0xdesign/design-plugin/blob/main/design-and-refine/skills/design-lab/SKILL.md",
    name: "design-lab",
    description:
      "Interactive design exploration workflow: conduct interviews, generate variants, and refine UI designs through feedback.",
  },
];
```

## File: `src/data/skills.ts`
```typescript
import type { MarkdownInstance } from "astro";

import { registry } from "./registry";

type SkillFrontmatter = {
  name?: string;
  description?: string;
  label?: string;
};

export type Skill = {
  slug: string;
  name: string;
  label: string;
  description?: string;
  isRegistry?: boolean;
};

const skillModules = import.meta.glob<MarkdownInstance<SkillFrontmatter>>(
  "/skills/*/SKILL.md",
  { eager: true },
);

const titleize = (value: string) =>
  value
    .split("-")
    .map((word) => {
      if (word.toLowerCase() === "ui") {
        return "UI";
      }

      return `${word.charAt(0).toUpperCase()}${word.slice(1)}`;
    })
    .join(" ");

const localSkills: Skill[] = Object.entries(skillModules).map(
  ([path, module]) => {
    const slug = path.split("/").at(-2) ?? "";
    const name = module.frontmatter.name ?? slug;

    return {
      slug,
      name,
      label: module.frontmatter.label ?? titleize(name),
      description: module.frontmatter.description,
    };
  },
);

const registrySkills: Skill[] = registry
  .filter((s) => !localSkills.some((ls) => ls.slug === s.slug))
  .map((s) => ({
    slug: s.slug,
    name: s.name ?? s.slug,
    label: titleize(s.name ?? s.slug),
    description: s.description,
    isRegistry: true,
  }));

export const skills: Skill[] = [...localSkills, ...registrySkills].sort(
  (a, b) => {
    if (a.slug === "baseline-ui") return -1;
    if (b.slug === "baseline-ui") return 1;

    if (!a.isRegistry && b.isRegistry) return -1;
    if (a.isRegistry && !b.isRegistry) return 1;

    return a.slug.localeCompare(b.slug);
  },
);
```

## File: `src/layouts/Layout.astro`
```
---
import "../styles/global.css";

type Props = {
  llmsPath?: string;
};

const { llmsPath } = Astro.props as Props;
const currentYear = new Date().getFullYear();
---

<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap"
    />
    <meta name="generator" content={Astro.generator} />
    <title>
      UI Skills - A set of skills to polish interfaces built by agents
    </title>
    <meta
      name="description"
      content="A set of skills to polish interfaces built by agents."
    />
    <meta property="og:title" content="UI Skills" />
    <meta
      property="og:description"
      content="A set of skills to polish interfaces built by agents."
    />
    <meta property="og:image" content="/cover.webp" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="UI Skills" />
    <meta
      name="twitter:description"
      content="A set of skills to polish interfaces built by agents."
    />
    <meta name="twitter:image" content="/cover.webp" />
    <script defer src="https://assets.onedollarstats.com/stonks.js"></script>
  </head>
  <body>
    <div class="relative min-h-dvh">
      <header
        class="absolute inset-x-0 top-0 z-10 flex justify-end px-4 pt-6 sm:px-8"
      >
        <a
          href="https://github.com/ibelick/ui-skills"
          target="_blank"
          rel="noopener noreferrer"
          class="text-parchment-500 hover:text-parchment-900 text-sm font-medium"
        >
          GitHub
        </a>
      </header>
      <!-- <div
        class="pointer-events-none absolute inset-0 mask-t-from-60% mask-t-to-100% mask-b-from-90% mask-b-to-100%"
        aria-hidden="true"
      >
        <svg class="h-full w-full" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <pattern
              id="small-grid"
              width="10"
              height="10"
              patternUnits="userSpaceOnUse"
            >
              <path
                d="M 10 0 L 0 0 0 10"
                fill="none"
                stroke="#78716c"
                stroke-opacity="0.1"
                stroke-width="0.5"></path>
            </pattern>
            <pattern
              id="grid"
              width="50"
              height="50"
              patternUnits="userSpaceOnUse"
            >
              <rect width="50" height="50" fill="url(#small-grid)"></rect>
              <path
                d="M 50 0 L 0 0 0 50"
                fill="none"
                stroke="#78716c"
                stroke-opacity="0.2"
                stroke-width="1"></path>
            </pattern>
          </defs>
          <rect width="100%" height="100%" fill="url(#grid)"></rect>
        </svg>
      </div> -->
      <slot />
      <footer
        class="text-parchment-400 flex w-full items-center justify-center gap-3 px-4 pt-24 pb-6 text-center text-sm font-medium sm:px-0"
      >
        <span>
          <span>©{currentYear}</span>
          <a
            href="https://interfaceoffice.com"
            target="_blank"
            rel="noopener noreferrer"
            class="text-parchment-400 hover:text-parchment-900"
          >
            Interface Office
          </a>
        </span>
        <span class="text-parchment-200">·</span>
        <a
          href="https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview?utm_source=ui-skills.com"
          target="_blank"
          rel="noopener noreferrer"
          class="hover:text-parchment-900"
        >
          Claude Skills
        </a>
        {llmsPath ? <span class="text-parchment-200">·</span> : null}
        {
          llmsPath ? (
            <a href={llmsPath} class="hover:text-parchment-900">
              llms.txt
            </a>
          ) : null
        }
      </footer>
    </div>
  </body>
</html>

<style>
  html,
  body {
    margin: 0;
    width: 100%;
    height: 100%;
    background-color: #fafaf5;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }
</style>
```

## File: `src/pages/index.astro`
```
---
import Layout from "../layouts/Layout.astro";
import { skills } from "../data/skills";
import { CopyButton } from "../ui/copy-button";
import CodeBlock from "../ui/code-block.astro";
import { InstallTabs } from "../ui/install-tabs";
import ExpandableCodeBlock from "../ui/expandable-code-block.astro";

const skillList = skills as Array<{
  slug: string;
  label: string;
  description?: string;
  isRegistry?: boolean;
}>;
---

<Layout>
  <div
    class="relative flex min-h-dvh flex-col items-center justify-end px-0 sm:px-4"
  >
    <div class="relative mt-20 w-full max-w-3xl sm:px-0">
      <div class="mx-auto flex w-full flex-col gap-16">
        <div class="px-4 sm:px-0">
          <h1 class="text-parchment-900 text-3xl font-medium tracking-tight">
            UI Skills
          </h1>
          <p class="text-parchment-600 mt-3 text-lg">
            A set of skills to polish interfaces built by agents.
          </p>
        </div>

        <div>
          <h2
            class="text-parchment-900 mb-3 px-4 text-lg font-medium tracking-tight sm:px-0"
          >
            Installation
          </h2>
          <InstallTabs client:load />
          <p class="text-parchment-500 mt-3 px-4 text-[15px] sm:px-0">
            Support Claude Code, Cursor, OpenCode and more.
          </p>
        </div>

        <div>
          <h2
            class="text-parchment-900 mb-3 px-4 text-lg font-medium tracking-tight sm:px-0"
          >
            Add a specific skill
          </h2>
          <ExpandableCodeBlock
            lines={skillList.map((skill) => [
              { text: "npx", className: "text-[#953800]" },
              { text: " ui-skills", className: "text-[#0a3069]" },
              { text: " add", className: "text-[#0550ae]" },
              {
                text: ` ${skill.slug}`,
                className: "text-parchment-400",
              },
            ])}
          />
        </div>

        <div>
          <h2
            class="text-parchment-900 mb-3 px-4 text-lg font-medium tracking-tight sm:px-0"
          >
            Usage
          </h2>
          <div
            class="relative flex items-center justify-between rounded-none border-t border-b border-neutral-200 bg-white py-3.5 pr-4 pl-6 shadow-2xs sm:rounded-[8px] sm:border-none sm:ring-1 sm:ring-black/10"
          >
            <code class="font-mono text-[15px]">
              <span class="text-[#953800]">/baseline-ui</span>
              <span class="text-parchment-400"> review src/</span>
            </code>
            <div class="flex items-center gap-1">
              <CopyButton
                content="/baseline-ui review src/"
                showText={false}
                className="size-8"
                client:load
              />
            </div>
          </div>
        </div>

         <div>
           <h2
             class="text-parchment-900 mb-3 px-4 text-lg font-medium tracking-tight sm:px-0"
           >
             Skills
           </h2>
           <p class="text-parchment-500 mb-4 px-4 text-[15px] sm:px-0">
             Foundation skills for design engineering.
           </p>
           <div class="grid gap-4 px-4 sm:grid-cols-2 sm:px-0">
             {
              skillList
                .filter((skill) => !skill.isRegistry)
                 .map((skill) => (
                   <a
                     href={`/skills/${skill.slug}`}
                     class="hover:border-parchment-300 hover:bg-parchment-100 relative flex flex-col justify-between rounded-[12px] border border-neutral-200 bg-transparent px-6 py-4 transition-colors"
                   >
                     <div class="flex flex-col gap-1">
                       <div class="text-parchment-900 font-[450] tracking-tight">
                         {skill.slug}
                       </div>
                       {skill.description ? (
                         <div class="text-parchment-500 line-clamp-3 text-[14px] leading-snug">
                           {skill.description}
                         </div>
                       ) : null}
                     </div>
                   </a>
                 ))
             }
           </div>
         </div>

         <div>
           <h2
             class="text-parchment-900 mb-3 px-4 text-lg font-medium tracking-tight sm:px-0"
           >
             Curated Skills
           </h2>
           <p class="text-parchment-500 mb-4 px-4 text-[15px] sm:px-0">
             Best skills for UI work.
           </p>
           <div class="grid gap-4 px-4 sm:grid-cols-2 sm:px-0">
             {
              skillList
                .filter((skill) => skill.isRegistry)
                 .map((skill) => (
                   <a
                     href={`/skills/${skill.slug}`}
                     class="hover:border-parchment-300 hover:bg-parchment-100 relative flex flex-col justify-between rounded-[12px] border border-neutral-200 bg-transparent px-6 py-4 transition-colors"
                   >
                     <div class="flex flex-col gap-1">
                       <div class="text-parchment-900 font-[450] tracking-tight">
                         {skill.slug}
                       </div>
                       {skill.description ? (
                         <div class="text-parchment-500 line-clamp-3 text-[14px] leading-snug">
                           {skill.description}
                         </div>
                       ) : null}
                     </div>
                   </a>
                 ))
             }
           </div>
         </div>
      </div>
    </div>
  </div>
</Layout>
```

## File: `src/pages/install.ts`
```typescript
import type { APIRoute } from "astro";
import installScript from "../../install.sh?raw";
import { skills } from "../data/skills";

export const GET: APIRoute = ({ request }) => {
  const allSkills = skills.map((s) => s.slug).join(" ");
  const body =
    installScript
      .replace(/ALL_SKILLS=".*"/, `ALL_SKILLS="${allSkills}"`)
      .trim() + "\n";

  return new Response(body, {
    headers: {
      "Content-Type": "text/x-shellscript; charset=utf-8",
    },
  });
};
```

## File: `src/pages/llms.txt.ts`
```typescript
import type { APIRoute } from "astro";
import { skills } from "../data/skills";

const skillRawModules = import.meta.glob<string>("/skills/*/SKILL.md", {
  eager: true,
  query: "?raw",
  import: "default",
});

const skillRawEntries = new Map(
  Object.entries(skillRawModules).map(([path, raw]) => [
    path.split("/").at(-2) ?? "",
    raw,
  ]),
);

export const GET: APIRoute = () => {
  const body = skills
    .map((skill) => skillRawEntries.get(skill.slug))
    .filter((raw): raw is string => Boolean(raw))
    .map((raw) => raw.trim())
    .join("\n\n")
    .concat("\n");

  return new Response(body, {
    headers: {
      "Content-Type": "text/plain; charset=utf-8",
    },
  });
};
```

## File: `src/pages/skills/[slug].astro`
```
---
import Layout from "../../layouts/Layout.astro";
import CodeBlock from "../../ui/code-block.astro";
import type { MarkdownInstance } from "astro";
import { skills } from "../../data/skills";
import { registry } from "../../data/registry";
import SkillCard from "../../ui/skill-card.astro";
import { marked } from "marked";

type SkillFrontmatter = {
  name?: string;
  description?: string;
  label?: string;
};

type SkillEntry = {
  slug: string;
  name: string;
  label: string;
  description?: string;
  isRegistry?: boolean;
};

const skillModules = import.meta.glob<MarkdownInstance<SkillFrontmatter>>(
  "/skills/*/SKILL.md",
  { eager: true },
);
const skillRawModules = import.meta.glob<string>("/skills/*/SKILL.md", {
  eager: true,
  query: "?raw",
  import: "default",
});
const skillEntries = Object.entries(skillModules).map(([path, module]) => {
  const entrySlug = path.split("/").at(-2) ?? "";

  return { slug: entrySlug, module };
});
const skillRawEntries = Object.entries(skillRawModules).map(([path, raw]) => {
  const entrySlug = path.split("/").at(-2) ?? "";

  return { slug: entrySlug, raw };
});

export function getStaticPaths() {
  return skills.map((skill) => ({
    params: { slug: skill.slug },
    props: skill,
  }));
}

const { slug, isRegistry } = Astro.props as SkillEntry;
const skillList = skills as SkillEntry[];
const skill = skillList.find((entry) => entry.slug === slug);

let skillRaw = "";
let displayContent = "";
let SkillContent: any = null;
let githubUrl = "";

if (isRegistry) {
  const registryEntry = registry.find((s) => s.slug === slug);
  if (registryEntry) {
    try {
      const response = await fetch(registryEntry.rawUrl);
      if (response.ok) {
        skillRaw = await response.text();
        githubUrl = registryEntry.githubUrl;
        let contentToRender = skillRaw;

        if (contentToRender.startsWith("---")) {
          const parts = contentToRender.split("---");
          if (parts.length >= 3) {
            contentToRender = parts.slice(2).join("---").trim();
          }
        }
        displayContent = await marked.parse(contentToRender);
      } else {
        displayContent = `<p>Error: Failed to fetch skill content from ${registryEntry.rawUrl} (${response.status} ${response.statusText})</p>`;
      }
    } catch (e) {
      displayContent = `<p>Error: ${e instanceof Error ? e.message : String(e)}</p>`;
    }
  }
} else {
  const skillModule = skillEntries.find((entry) => entry.slug === slug)?.module;
  skillRaw = skillRawEntries.find((entry) => entry.slug === slug)?.raw ?? "";
  SkillContent = skillModule?.Content;
}

const commandSegments = [
  { text: "npx", className: "text-[#953800]" },
  { text: " ui-skills", className: "text-[#0a3069]" },
  { text: " add", className: "text-[#0550ae]" },
  { text: ` ${slug}`, className: "text-parchment-400" },
];
---

<Layout llmsPath={`/skills/${slug}/llms.txt`}>
  <div
    class="relative flex min-h-dvh flex-col items-center justify-start px-0 sm:px-4"
  >
    <div class="relative mt-20 w-full max-w-3xl sm:px-0">
      <div class="mx-auto flex w-full flex-col gap-14">
        <div class="px-4 sm:px-0">
          <div class="flex items-center justify-between">
            <a
              href="/"
              class="text-parchment-500 hover:text-parchment-900 text-sm font-medium"
            >
              Back to home
            </a>
            {
              githubUrl ? (
                <a
                  href={githubUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  class="text-parchment-500 hover:text-parchment-900 text-sm font-medium"
                >
                  View source
                </a>
              ) : null
            }
          </div>
          <h1
            class="text-parchment-900 mt-3 text-3xl font-medium tracking-tight"
          >
            {skill?.label ?? slug}
          </h1>
          <p class="text-parchment-600 mt-3 text-lg">
            {skill?.description ?? "Install this skill with a single command."}
          </p>
        </div>

        <div>
          <h2
            class="text-parchment-900 mb-3 px-4 text-lg font-medium tracking-tight sm:px-0"
          >
            Install
          </h2>
          <CodeBlock lines={[commandSegments]} align="center" />
        </div>

        <SkillCard
          copyContent={skillRaw}
          name={skill?.name ?? slug}
          description={skill?.description}
          dataEvent="install"
        >
          {SkillContent ? <SkillContent /> : <div set:html={displayContent} />}
        </SkillCard>
      </div>
    </div>
  </div>
</Layout>
```

## File: `src/pages/skills/registry.txt.ts`
```typescript
import type { APIRoute } from "astro";

import type { RegistrySkill } from "../../data/registry";
import { registry } from "../../data/registry";

export const GET: APIRoute = () => {
  const body = registry
    .map(
      (entry: RegistrySkill) =>
        `${entry.slug}\t${entry.rawUrl}\t${entry.description ?? ""}`,
    )
    .join("\n");

  return new Response(`${body}\n`, {
    headers: {
      "Content-Type": "text/plain; charset=utf-8",
    },
  });
};
```

## File: `src/pages/skills/[slug]/llms.txt.ts`
```typescript
import type { APIRoute } from "astro";
import { skills } from "../../../data/skills";
import { registry } from "../../../data/registry";

const skillRawModules = import.meta.glob<string>("/skills/*/SKILL.md", {
  eager: true,
  query: "?raw",
  import: "default",
});

const skillRawEntries = Object.entries(skillRawModules).map(([path, raw]) => {
  const entrySlug = path.split("/").at(-2) ?? "";

  return { slug: entrySlug, raw };
});

export function getStaticPaths() {
  return skills.map((skill) => ({
    params: { slug: skill.slug },
  }));
}

export const GET: APIRoute = async ({ params }) => {
  const slug = params.slug ?? "";

  // Check local skills first
  const localSkill = skillRawEntries.find((entry) => entry.slug === slug);
  if (localSkill) {
    return new Response(localSkill.raw, {
      headers: {
        "Content-Type": "text/plain; charset=utf-8",
      },
    });
  }

  // Check registry skills
  const registrySkill = registry.find((s) => s.slug === slug);
  if (registrySkill) {
    try {
      const response = await fetch(registrySkill.rawUrl);
      if (!response.ok) {
        throw new Error(
          `Failed to fetch registry skill: ${response.statusText}`,
        );
      }
      const content = await response.text();
      return new Response(content, {
        headers: {
          "Content-Type": "text/plain; charset=utf-8",
        },
      });
    } catch (error) {
      console.error(error);
      return new Response("Error fetching registry skill", { status: 500 });
    }
  }

  return new Response("Skill not found", { status: 404 });
};
```

## File: `src/styles/global.css`
```css
@import "tailwindcss";
@plugin "@tailwindcss/typography";

@theme {
  --font-mono: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, Monaco,
    Consolas, "Liberation Mono", "Courier New", monospace;

  /* Extended warm neutral palette derived from #fafaf5 */
  --color-parchment-50: #fafaf5;
  --color-parchment-100: #f5f5f0;
  --color-parchment-200: #e5e5e0;
  --color-parchment-300: #d6d3d1;
  --color-parchment-400: #a8a29e;
  --color-parchment-500: #78716c;
  --color-parchment-600: #57534e;
  --color-parchment-700: #44403c;
  --color-parchment-800: #292524;
  --color-parchment-900: #1c1917;

  --color-primary: var(--color-parchment-900);
  --color-secondary: var(--color-parchment-600);
  --color-tertiary: var(--color-parchment-400);
}


::selection {
  background-color: #e1dccf7c;
  color: inherit;
}

.prose :where(code):not(:where([class~="not-prose"], [class~="not-prose"] *)) {
  background-color: var(--color-parchment-100);
  font-weight: 500;
  padding: 0.1em 0.35em;
  border-radius: 0.25rem;
}

.prose :where(pre code):not(:where([class~="not-prose"], [class~="not-prose"] *)) {
  background-color: transparent;
  padding: 0;
  font-weight: inherit;
}

.prose :where(code):not( :where([class~="not-prose"], [class~="not-prose"] *))::before,
.prose :where(code):not( :where([class~="not-prose"], [class~="not-prose"] *))::after {
  content: "";
}
```

## File: `src/ui/code-block.astro`
```
---
import { CopyButton } from "./copy-button";

type Props = {
  lines?: Array<Array<{ text: string; className?: string }>>;
  copyContent?: string;
  align?: "start" | "center";
  className?: string;
  id?: string;
};

const {
  lines = [],
  copyContent,
  align = "start",
  className = "",
  id,
} = Astro.props as Props;
const content =
  copyContent ??
  lines.map((line) => line.map((segment) => segment.text).join("")).join("\n");
const alignClass = align === "center" ? "items-center" : "items-start";
---

<div
  id={id}
  class={`relative flex justify-between rounded-none border-t border-b border-neutral-200 bg-white py-3.5 pr-4 pl-6 shadow-2xs sm:rounded-[8px] sm:border-none sm:ring-1 sm:ring-black/10 ${alignClass} ${className}`}
>
  <code class="font-mono text-[15px] leading-6">
    {
      lines.map((line) => (
        <div>
          {line.map((segment) => (
            <span class={segment.className}>{segment.text}</span>
          ))}
        </div>
      ))
    }
  </code>
  <div class="flex items-center gap-1">
    <CopyButton
      content={content}
      showText={false}
      className="size-8"
      client:load
    />
  </div>
  <slot />
</div>
```

## File: `src/ui/copy-button.tsx`
```tsx
import { useState } from "react";
import { TextMorph } from "./text-morph";

type CopyButtonProps = {
  content: string;
  className?: string;
  showText?: boolean;
} & React.ButtonHTMLAttributes<HTMLButtonElement>;

export function CopyButton({
  content,
  className,
  showText = true,
  ...props
}: CopyButtonProps) {
  const [isCopied, setIsCopied] = useState(false);

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(content);
      setIsCopied(true);
      setTimeout(() => setIsCopied(false), 2000);
    } catch {
      // Ignore error
    }
  };

  return (
    <button
      onClick={handleCopy}
      type="button"
      className={`flex h-8 items-center justify-center rounded-full text-neutral-400 transition-colors hover:text-neutral-900 ${className}`}
      aria-label="Copy to clipboard"
      {...props}
    >
      {showText ? (
        <div className="flex w-[70px] items-center justify-center text-sm font-medium">
          <TextMorph>{isCopied ? "Copied" : "Copy"}</TextMorph>
        </div>
      ) : (
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
        >
          {isCopied ? (
            <path d="M20 6 9 17l-5-5" />
          ) : (
            <>
              <rect width="14" height="14" x="8" y="8" rx="2" ry="2" />
              <path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2" />
            </>
          )}
        </svg>
      )}
    </button>
  );
}
```

## File: `src/ui/expandable-code-block.astro`
```
---
import CodeBlock from "./code-block.astro";

type Props = {
  lines: Array<Array<{ text: string; className?: string }>>;
  maxHeight?: number;
};

const { lines, maxHeight = 180 } = Astro.props as Props;
---

<div class="expandable-code-wrapper relative" data-max-height={maxHeight}>
  <CodeBlock
    lines={lines}
    className="expandable-code-container overflow-hidden transition-[max-height] duration-150"
  >
    <div
      class="expandable-code-mask pointer-events-none absolute right-0 bottom-0 left-0 h-24 bg-linear-to-t from-white to-transparent transition-opacity duration-300 sm:rounded-b-[8px]"
    >
    </div>
  </CodeBlock>
  <div class="mt-4 flex justify-center">
    <button
      class="expandable-code-btn text-parchment-500 hover:text-parchment-900 cursor-pointer text-sm font-medium transition-colors"
    >
      Show all skills
    </button>
  </div>
</div>

<script>
  function setupExpandableCode() {
    const wrappers = document.querySelectorAll(".expandable-code-wrapper");

    wrappers.forEach((wrapper) => {
      const container = wrapper.querySelector(
        ".expandable-code-container",
      ) as HTMLElement;
      const btn = wrapper.querySelector(".expandable-code-btn");
      const mask = wrapper.querySelector(".expandable-code-mask");
      const maxHeight = wrapper.getAttribute("data-max-height") || "180";

      if (container) {
        container.style.maxHeight = `${maxHeight}px`;
      }

      btn?.addEventListener("click", () => {
        const isExpanded =
          container?.style.maxHeight === "none" ||
          (container?.style.maxHeight &&
            parseInt(container.style.maxHeight) > parseInt(maxHeight));

        if (isExpanded) {
          if (container) {
            container.classList.remove("ease-out");
            container.classList.add("ease-in");
            container.style.maxHeight = `${maxHeight}px`;
          }
          if (btn) btn.textContent = "Show all skills";
          mask?.classList.remove("opacity-0");
        } else {
          if (container) {
            container.classList.remove("ease-in");
            container.classList.add("ease-out");
            // Set to scrollHeight for an "instant" start to the animation
            container.style.maxHeight = `${container.scrollHeight}px`;
          }
          if (btn) btn.textContent = "Show less";
          mask?.classList.add("opacity-0");
        }
      });
    });
  }

  // Run on initial load
  setupExpandableCode();

  // Run on view transitions if enabled
  document.addEventListener("astro:after-swap", setupExpandableCode);
</script>
```

## File: `src/ui/install-tabs.tsx`
```tsx
import { useState } from "react";
import { CopyButton } from "./copy-button";

type InstallTab = {
  id: "npx" | "bash";
  label: string;
  command: string;
  content: React.ReactNode;
};

const tabs: InstallTab[] = [
  {
    id: "npx",
    label: "npx",
    command: "npx skills add ibelick/ui-skills",
    content: (
      <>
        <span className="text-[#953800]">npx</span>
        <span className="text-[#0a3069]"> skills</span>
        <span className="text-[#0550ae]"> add</span>
        <span className="text-parchment-400"> ibelick/ui-skills</span>
      </>
    ),
  },
  {
    id: "bash",
    label: "bash",
    command: "curl -fsSL https://ui-skills.com/install | bash",
    content: (
      <>
        <span className="text-[#953800]">curl</span>
        <span className="text-[#0550ae]"> -fsSL</span>
        <span className="text-[#0a3069]"> https://ui-skills.com/install</span>
        <span className="text-[#cf222e]"> |</span>
        <span className="text-[#953800]"> bash</span>
      </>
    ),
  },
];

export function InstallTabs() {
  const [activeTab, setActiveTab] = useState<InstallTab>(tabs[0]);

  return (
    <div className="border-parchment-200 rounded-none border-t border-b bg-white shadow-2xs sm:rounded-[8px] sm:border-none sm:ring-1 sm:ring-black/10">
      <div className="flex items-center gap-3 py-2 pl-6">
        <span className="bg-parchment-700 flex size-4 items-center justify-center rounded-[2px] text-parchment-50">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
            className="size-3"
          >
            <path d="M5 7l5 5l-5 5" />
            <path d="M12 19l7 0" />
          </svg>
        </span>
        <div className="flex items-center gap-0.5">
          {tabs.map((tab) => {
            const isActive = tab.id === activeTab.id;

            return (
              <button
                key={tab.id}
                type="button"
                onClick={() => setActiveTab(tab)}
                className={`text-parchment-500 flex items-center justify-center rounded-md border px-1.5 py-0.5 font-mono text-xs font-medium transition-colors ${isActive
                  ? "border-parchment-200 bg-parchment-100 text-parchment-900"
                  : "hover:text-parchment-900 border-transparent bg-transparent"
                  }`}
              >
                {tab.label}
              </button>
            );
          })}
        </div>
      </div>
      <div className="border-parchment-200 flex items-center justify-between border-t py-3.5 pr-4 pl-6">
        <code className="font-mono text-[15px]">{activeTab.content}</code>
        <div className="flex items-center gap-1">
          <CopyButton
            content={activeTab.command}
            showText={false}
            className="size-8"
            data-s-event="install"
          />
        </div>
      </div>
    </div>
  );
}
```

## File: `src/ui/skill-card.astro`
```
---
import { CopyButton } from "./copy-button";

type Props = {
  copyContent: string;
  name?: string;
  description?: string;
  dataEvent?: string;
};

const { copyContent, name, description, dataEvent } = Astro.props as Props;
const hasFrontmatter = Boolean(name ?? description);
---

<div
  class="relative w-full max-w-3xl rounded-none border-t border-b border-neutral-200 bg-white py-3.5 pt-6 pr-4 pl-6 shadow-2xs sm:rounded-[8px] sm:border-none sm:shadow-2xs sm:ring-1 sm:ring-black/10"
>
  <div class="sticky top-0 right-0">
    <div class="absolute top-0 right-0">
      <CopyButton content={copyContent} client:load data-s-event={dataEvent} />
    </div>
  </div>
  <div
    class="prose prose-neutral prose-headings:text-balance prose-headings:font-medium prose-headings:text-[15px] prose-h1:mt-0 prose-h1:mb-6 prose-h1:text-[18px] prose-h2:mt-8 prose-h2:mb-3 prose-p:my-3 prose-p:font-normal prose-p:text-[14px] prose-p:text-parchment-600 prose-p:text-pretty prose-ul:my-3 prose-li:my-1.5 prose-li:pl-0 prose-li:font-normal prose-li:text-[14px] prose-li:text-parchment-600 prose-li:marker:text-parchment-300 prose-pre:rounded-[8px] prose-pre:border prose-pre:border-neutral-200 prose-pre:bg-white prose-pre:p-4 prose-pre:text-parchment-900 prose-pre:text-[13px] max-w-none font-mono"
  >
    {
      hasFrontmatter ? (
        <div class="text-parchment-400 mb-8 text-[14px]">
          <div>---</div>
          {name ? <div>name: {name}</div> : null}
          {description ? <div>description: {description}</div> : null}
          <div>---</div>
        </div>
      ) : null
    }
    <slot />
  </div>
</div>
```

## File: `src/ui/text-morph.tsx`
```tsx
import {
  AnimatePresence,
  motion,
  type Transition,
  type Variants,
} from "motion/react";
import { useMemo, useId } from "react";

export type TextMorphProps = {
  children: string;
  as?: React.ElementType;
  className?: string;
  style?: React.CSSProperties;
  variants?: Variants;
  transition?: Transition;
};

export function TextMorph({
  children,
  as: Component = "p",
  className,
  style,
  variants,
  transition,
}: TextMorphProps) {
  const uniqueId = useId();
  const Tag = Component as React.ComponentType<{
    className?: string;
    "aria-label"?: string;
    style?: React.CSSProperties;
    children?: React.ReactNode;
  }>;

  const characters = useMemo(() => {
    const charCounts: Record<string, number> = {};

    return children.split("").map((char) => {
      const lowerChar = char.toLowerCase();
      charCounts[lowerChar] = (charCounts[lowerChar] || 0) + 1;

      return {
        id: `${uniqueId}-${lowerChar}${charCounts[lowerChar]}`,
        label: char === " " ? "\u00A0" : char,
      };
    });
  }, [children, uniqueId]);

  const defaultVariants: Variants = {
    initial: { opacity: 0 },
    animate: { opacity: 1 },
    exit: { opacity: 0 },
  };

  const defaultTransition: Transition = {
    type: "spring",
    stiffness: 280,
    damping: 18,
    mass: 0.3,
  };

  return (
    <Tag aria-label={children} style={style as React.CSSProperties}>
      <AnimatePresence mode="popLayout" initial={false}>
        {characters.map((character) => (
          <motion.span
            key={character.id}
            layoutId={character.id}
            className="inline-block"
            aria-hidden="true"
            initial="initial"
            animate="animate"
            exit="exit"
            variants={variants || defaultVariants}
            transition={transition || defaultTransition}
          >
            {character.label}
          </motion.span>
        ))}
      </AnimatePresence>
    </Tag>
  );
}
```

