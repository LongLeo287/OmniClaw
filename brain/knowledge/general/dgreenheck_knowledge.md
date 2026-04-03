---
id: dgreenheck-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:19.851193
---

# KNOWLEDGE EXTRACT: dgreenheck
> **Extracted on:** 2026-03-30 17:35:57
> **Source:** dgreenheck

---

## File: `webgpu-claude-skill.md`
```markdown
# 📦 dgreenheck/webgpu-claude-skill [🔖 PENDING/APPROVE]
🔗 https://github.com/dgreenheck/webgpu-claude-skill


## Meta
- **Stars:** ⭐ 460 | **Forks:** 🍴 46
- **Language:** JavaScript | **License:** Unknown
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A Claude skill for developing WebGPU applications with Three.js

## README (trích đầu)
```
# WebGPU Three.js TSL Skill

An Agent Skill for developing WebGPU-enabled Three.js applications using TSL (Three.js Shading Language).

## Overview

This skill provides Claude with comprehensive knowledge for:

- Setting up Three.js with WebGPU renderer
- Writing shaders using TSL (Three.js Shading Language)
- Creating node-based materials
- Building GPU compute shaders
- Implementing post-processing effects
- Integrating custom WGSL code

## Installation

### Claude Code

```bash
# Install from this repository
/skill install webgpu-threejs-tsl@<your-github-username>/webgpu-claude-skill
```

### Manual Installation

Copy the `skills/webgpu-threejs-tsl` folder to:
- **Global**: `~/.claude/skills/`
- **Project**: `<project>/.claude/skills/`

## Skill Structure

```
skills/webgpu-threejs-tsl/
├── SKILL.md                    # Entry point with overview
├── REFERENCE.md                # Quick reference cheatsheet
├── brain/knowledge/docs_legacy/
│   ├── core-concepts.md        # Types, operators, uniforms, control flow
│   ├── materials.md            # Node materials and properties
│   ├── compute-shaders.md      # GPU compute documentation
│   ├── post-processing.md      # Built-in and custom effects
│   ├── wgsl-integration.md     # Custom WGSL functions
│   └── device-loss.md          # GPU device loss handling and recovery
├── examples/
│   ├── basic-setup.js          # Minimal WebGPU project
│   ├── custom-material.js      # Custom shader material
│   ├── particle-system.js      # GPU compute particles
│   ├── post-processing.js      # Effect pipeline
│   └── earth-shader.js         # Complete Earth with atmosphere
└── templates/
    ├── webgpu-project.js       # Starter project template
    └── compute-shader.js       # Compute shader template
```

## Topics Covered

### Core Concepts
- Types and constructors (float, vec2, vec3, vec4, color, uniform)
- Vector swizzling
- Operators and math functions
- Control flow (If, Loop, Fn)
- Time and animation

### Materials
- All node material types
- Material properties (color, roughness, metalness, etc.)
- Physical material features (clearcoat, transmission, iridescence)
- Vertex displacement

### Compute Shaders
- Instanced array buffers
- Parallel physics simulation
- Particle systems
- Atomic operations and barriers

### Post-Processing
- Built-in effects (bloom, blur, FXAA, DOF)
- Custom effects with Fn()
- Effect chaining
- Multiple render targets

### WGSL Integration
- Custom WGSL functions with wgslFn()
- Hybrid TSL/WGSL approaches
- Performance optimization

### Device Loss Handling
- Detecting GPU device loss
- Recovery strategies
- Testing with destroy() and Chrome GPU crash
- State preservation and restoration

## Quick Example

```javascript
import * as THREE from 'three/webgpu';
import { color, time, oscSine, normalWorld, cameraPosition, positionWorld, Fn, float } from 'three/tsl';

// WebGPU renderer
const renderer = new THREE.WebGPURenderer();
await renderer.init();

// TSL material with animated fresnel
const
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

