---
id: hig-doctor-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:52.029817
---

# OmniClaw Knowledge Report: hig-doctor

## Tech Stack
Node.js/NPM

## File Statistics
```json
{
  "": 4,
  ".yml": 1,
  ".md": 177,
  ".json": 14,
  ".png": 3,
  ".mjs": 2,
  ".jsx": 3,
  ".js": 7,
  ".lock": 2,
  ".ts": 19,
  ".tsx": 31,
  ".css": 1,
  ".svg": 3,
  ".txt": 1
}
```

## README Snippet
```markdown
# Apple HIG Skills

Apple Human Interface Guidelines as agent skills for Claude Code, Cursor, and other AI coding agents.

14 skills covering the complete Apple HIG — foundations, components, patterns, inputs, platforms, and technologies. Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/) (February 2025).

## Install

```bash
npx skills add raintree-technology/apple-hig-skills
```

Or install via Claude Code plugin:

```
/plugin marketplace add raintree-technology/apple-hig-skills
```

## HIG Audit

Audit any project for Apple HIG compliance. Works with SwiftUI, UIKit, React, Next.js, Vue, Nuxt, Svelte, SvelteKit, Angular, React Native, Flutter, Jetpack Compose, Android XML, and plain HTML/CSS. Detects 349 patterns across accessibility, color systems, typography, responsive layout, dark mode, motion, i18n, and more.

Requires [Bun](https://bun.sh).

```bash
cd packages/hig-doctor/src-termcast
bun install
bun run audit <directory>
```

Example output:

```
  HIG Audit: website   100/100
  nextjs · 751 detections · 56 files

  ────────────────────────────────────────────────────────────────────
  Foundations                610  ███████████████████░  593 good
  Interaction Patterns        34  ███████████████████░  32 good
  Layout & Navigation         42  █████░░░░░░░░░░░░░░░  11 good
  Controls                    25  ░░░░░░░░░░░░░░░░░░░░
  Input Methods               17  ████████████████░░░░  14 good
  ────────────────────
```

**Processed by OmniClaw Automated Intake**