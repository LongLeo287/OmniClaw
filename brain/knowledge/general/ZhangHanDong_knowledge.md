---
id: zhanghandong-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:47.884024
---

# KNOWLEDGE EXTRACT: ZhangHanDong
> **Extracted on:** 2026-03-30 18:01:27
> **Source:** ZhangHanDong

---

## File: `makepad-skills.md`
```markdown
# 📦 ZhangHanDong/makepad-skills [🔖 PENDING/APPROVE]
🔗 https://github.com/ZhangHanDong/makepad-skills


## Meta
- **Stars:** ⭐ 725 | **Forks:** 🍴 82
- **Language:** Shell | **License:** MIT
- **Last updated:** 2026-03-23
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Build App with Makepad and AI skills

## README (trích đầu)
```
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
curl -fsSL https:
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

