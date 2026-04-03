---
id: raintree-technology-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:06.576020
---

# KNOWLEDGE EXTRACT: raintree-technology
> **Extracted on:** 2026-03-30 17:52:59
> **Source:** raintree-technology

---

## File: `hig-doctor.md`
```markdown
# 📦 raintree-technology/hig-doctor [🔖 PENDING/APPROVE]
🔗 https://github.com/raintree-technology/hig-doctor
🌐 https://apple.raintree.technology/

## Meta
- **Stars:** ⭐ 28 | **Forks:** 🍴 2
- **Language:** TypeScript | **License:** NOASSERTION
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Apple HIG audit CLI + 14 agent skills for AI coding assistants — score any project for HIG compliance across 12 frameworks

## README (trích đầu)
```
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
  ────────────────────────────────────────────────────────────────────
  Totals                     751  650 good  101 patterns

  Excellent — Strong HIG compliance across the board.
```

### Options

| Flag | Description |
|------|-------------|
| `--export` | Write a full audit report to `<directory>/hig-audit.md` |
| `--stdout` | Print raw audit markdown to stdout (pipe to an AI for evaluation) |
| `--json` | Print structured results as JSON (for CI/scripts) |
| `--help` | Show help |

### What it detects

The audit scans code, stylesheets, and config files, then categorizes findings across HIG areas:

- **Foundations** — semantic vs hardcoded colors, Dynamic Type vs fixed font sizes, dark mode, motion preferences, accessibility labels, focus management, heading hierarchy, landmark regions, touch targets, i18n/RTL support
- **Layout & Navigation** — navigation patterns, responsive breakpoints, semantic HTML, adaptive layout, sidebar/tab patterns
- **Controls** — buttons, toggles, form elements, interactive controls, labels
- **Content Display** — images, collections, tables, cards, accordions, lists
- **Input Methods** — keyboard support, gesture handling, form validation, input types, fieldset/legend, autocomplete
- **Interaction Patterns** — drag and drop, pull-to-refresh, undo, animations, haptics, error handling
- **Dialogs & Presentations** — modals, sheets, alerts, popovers, toasts, tooltips
- **Menus & Actions** — dropdown menus, context menus, toolbars, menu roles
- **Search & Navigatio
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

