---
id: millionco-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:08.191644
---

# KNOWLEDGE EXTRACT: millionco
> **Extracted on:** 2026-03-30 17:42:49
> **Source:** millionco

---

## File: `react-doctor.md`
```markdown
# 📦 millionco/react-doctor [🔖 PENDING/APPROVE]
🔗 https://github.com/millionco/react-doctor
🌐 https://react.doctor

## Meta
- **Stars:** ⭐ 5981 | **Forks:** 🍴 189
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Let coding agents diagnose and fix your React code

## README (trích đầu)
```
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/react-doctor-readme-logo-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/react-doctor-readme-logo-light.svg">
  <img alt="React Doctor" src="./assets/react-doctor-readme-logo-light.svg" width="180" height="40">
</picture>

[![version](https://img.shields.io/npm/v/react-doctor?style=flat&colorA=000000&colorB=000000)](https://npmjs.com/package/react-doctor)
[![downloads](https://img.shields.io/npm/dt/react-doctor.svg?style=flat&colorA=000000&colorB=000000)](https://npmjs.com/package/react-doctor)

Let coding agents diagnose and fix your React code.

One command scans your codebase for security, performance, correctness, and architecture issues, then outputs a **0–100 score** with actionable diagnostics.

### [See it in action →](https://react.doctor)

https://github.com/user-attachments/assets/07cc88d9-9589-44c3-aa73-5d603cb1c570

## How it works

React Doctor detects your framework (Next.js, Vite, Remix, etc.), React version, and compiler setup, then runs two analysis passes **in parallel**:

1. **Lint**: Checks 60+ rules across state & effects, performance, architecture, bundle size, security, correctness, accessibility, and framework-specific categories (Next.js, React Native). Rules are toggled automatically based on your project setup.
2. **Dead code**: Detects unused files, exports, types, and duplicates.

Diagnostics are filtered through your config, then scored by severity (errors weigh more than warnings) to produce a **0–100 health score** (75+ Great, 50–74 Needs work, <50 Critical).

## Install

Run this at your project root:

```bash
npx -y react-doctor@latest .
```

Use `--verbose` to see affected files and line numbers:

```bash
npx -y react-doctor@latest . --verbose
```

## Install for your coding agent

Teach your coding agent all 47+ React best practice rules:

```bash
curl -fsSL https://react.doctor/install-skill.sh | bash
```

Supports Cursor, Claude Code, Amp Code, Codex, Gemini CLI, OpenCode, Windsurf, and Antigravity.

## GitHub Actions

```yaml
- uses: actions/checkout@v5
  with:
    fetch-depth: 0 # required for --diff
- uses: millionco/react-doctor@main
  with:
    diff: main
    github-token: ${{ secrets.GITHUB_TOKEN }}
```

| Input          | Default | Description                                                       |
| -------------- | ------- | ----------------------------------------------------------------- |
| `directory`    | `.`     | Project directory to scan                                         |
| `verbose`      | `true`  | Show file details per rule                                        |
| `project`      |         | Workspace project(s) to scan (comma-separated)                    |
| `diff`         |         | Base branch for diff mode. Only changed files are scanned         |
| `github-token` |         | When set on `pull_request` events, posts findings as a PR comment |
| `node-version` | `20`    | Nod
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

