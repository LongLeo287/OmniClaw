---
id: cloudai-x-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:06.712681
---

# KNOWLEDGE EXTRACT: CloudAI-X
> **Extracted on:** 2026-03-30 17:34:26
> **Source:** CloudAI-X

---

## File: `claude-workflow-v2.md`
```markdown
# 📦 CloudAI-X/claude-workflow-v2 [🔖 PENDING/APPROVE]
🔗 https://github.com/CloudAI-X/claude-workflow-v2


## Meta
- **Stars:** ⭐ 1304 | **Forks:** 🍴 187
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Universal Claude Code workflow plugin with agents, skills, hooks, and commands

## README (trích đầu)
```
# project-starter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-v1.0.33+-blue.svg)](https://code.claude.com)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/CloudAI-X/claude-workflow-v2/pulls)

A universal Claude Code workflow plugin with specialized agents, skills, hooks, and output styles for any software project. Compatible with [skills.sh](https://skills.sh) — works with Claude Code, Cursor, Codex, and 35+ AI agents.

---

## Quick Start

### Option 1: skills.sh (Recommended — Any Agent)

```bash
npx skills add CloudAI-X/claude-workflow-v2
```

Installs skills to Claude Code, Cursor, Codex, Windsurf, Cline, and 35+ other AI agents automatically.

### Option 2: npx (Claude Code — Full Plugin)

```bash
npx install-claude-workflow-v2@latest
```

Installs the complete plugin: agents, commands, skills, and hooks.

### Option 3: CLI (Per-Session)

```bash
# Clone the plugin
git clone https://github.com/CloudAI-X/claude-workflow-v2.git

# Run Claude Code with the plugin
claude --plugin-dir ./claude-workflow-v2
```

### Option 4: Agent SDK

```typescript
import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const message of query({
  prompt: "Hello",
  options: {
    plugins: [{ type: "local", path: "./claude-workflow-v2" }],
  },
})) {
  // Plugin commands, agents, and skills are now available
}
```

### Option 5: Install Permanently

```bash
# Install from marketplace (when available)
claude plugin install project-starter

# Or install from local directory
claude plugin install ./claude-workflow-v2
```

### Verify Installation

After loading the plugin, verify it's working:

```
> /plugin
```

Tab to **Installed** - you should see `project-starter` listed.
Tab to **Errors** - should be empty (no errors).

These commands become available:

```
/project-starter:architect    # Architecture-first mode
/project-starter:rapid        # Ship fast mode
/project-starter:commit       # Auto-generate commit message
/project-starter:verify-changes  # Multi-agent verification
```

---

## What's Included

| Component    | Count | Description                                                             |
| ------------ | ----- | ----------------------------------------------------------------------- |
| **Agents**   | 7     | Specialized subagents for code review, debugging, security, etc.        |
| **Commands** | 26    | Slash commands for workflows, output styles, planning, and onboarding   |
| **Skills**   | 14    | Knowledge domains with on-demand context loading                        |
| **Hooks**    | 14    | Automation scripts for formatting, security, metrics, and notifications |

---

## Usage Examples

### Commands in Action

**Auto-commit your changes:**

```
> /project-starter:commit

Looking at staged changes...
✓ Created commit: feat(auth): add JWT refresh token endpoin
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `threejs-skills.md`
```markdown
# 📦 CloudAI-X/threejs-skills [🔖 PENDING/APPROVE]
🔗 https://github.com/CloudAI-X/threejs-skills


## Meta
- **Stars:** ⭐ 1848 | **Forks:** 🍴 204
- **Language:** N/A | **License:** Unknown
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
(No description)

## README (trích đầu)
```
# Three.js Skills for Claude Code

A curated collection of Three.js skill files that provide Claude Code with foundational knowledge for creating 3D elements and interactive experiences.

## Purpose

When working with Three.js, Claude Code starts with general programming knowledge but lacks specific Three.js API details, best practices, and common patterns. These skill files bridge that gap by providing:

- Accurate API references and constructor signatures
- Working code examples for common use cases
- Performance optimization tips
- Integration patterns between different Three.js systems

## Installation

Clone this repository into your project or copy the `.claude/skills` directory:

```bash
git clone https://github.com/pinkforest/threejs-playground.git
```

Or add as a submodule:

```bash
git submodule add https://github.com/pinkforest/threejs-playground.git
```

## Skills Included

| Skill                      | Description                                                             |
| -------------------------- | ----------------------------------------------------------------------- |
| **threejs-fundamentals**   | Scene setup, cameras, renderer, Object3D hierarchy, coordinate systems  |
| **threejs-geometry**       | Built-in shapes, BufferGeometry, custom geometry, instancing            |
| **threejs-materials**      | PBR materials, basic/phong/standard materials, shader materials         |
| **threejs-lighting**       | Light types, shadows, environment lighting, light helpers               |
| **threejs-textures**       | Texture types, UV mapping, environment maps, render targets             |
| **threejs-animation**      | Keyframe animation, skeletal animation, morph targets, animation mixing |
| **threejs-loaders**        | GLTF/GLB loading, texture loading, async patterns, caching              |
| **threejs-shaders**        | GLSL basics, ShaderMaterial, uniforms, custom effects                   |
| **threejs-postprocessing** | EffectComposer, bloom, DOF, screen effects, custom passes               |
| **threejs-interaction**    | Raycasting, camera controls, mouse/touch input, object selection        |

## How It Works

Claude Code automatically loads skill files from the `.claude/skills` directory when they match the context of your request. When you ask Claude Code to:

- Create a 3D scene → `threejs-fundamentals` is loaded
- Add lighting and shadows → `threejs-lighting` is loaded
- Load a GLTF model → `threejs-loaders` is loaded
- Create custom visual effects → `threejs-shaders` and `threejs-postprocessing` are loaded

## Usage Examples

### Basic Scene Setup

Ask Claude Code:

> "Create a basic Three.js scene with a rotating cube"

Claude Code will use `threejs-fundamentals` to generate accurate boilerplate with proper renderer setup, animation loop, and resize handling.

### Loading 3D Models

Ask Claude Code:

> "Load a GLTF model with Draco compression and play its animations"

Claude Code will use `threejs-loaders` and
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

