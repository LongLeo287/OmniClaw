---
id: macaly-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:06.372124
---

# KNOWLEDGE EXTRACT: macaly
> **Extracted on:** 2026-03-30 17:42:04
> **Source:** macaly

---

## File: `almostnode.md`
```markdown
# 📦 macaly/almostnode [🔖 PENDING/APPROVE]
🔗 https://github.com/macaly/almostnode
🌐 http://almostnode.dev/

## Meta
- **Stars:** ⭐ 1013 | **Forks:** 🍴 85
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Node.js in your browser. Just like that.

## README (trích đầu)
```
# almostnode

**Node.js in your browser. Just like that.**

A lightweight, browser-native Node.js runtime environment. Run Node.js code, install npm packages, and develop with Vite or Next.js - all without a server.

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue.svg)](https://www.typescriptlang.org/)
[![Node.js](https://img.shields.io/badge/Node.js-%3E%3D20-green.svg)](https://nodejs.org/)

Built by the creators of [Macaly.com](https://macaly.com) — a tool that lets anyone build websites and web apps, even without coding experience. Think Claude Code for non-developers.

> **Warning:** This project is experimental and may contain bugs. Use with caution in production environments.

---

## Features

- **Virtual File System** - Full in-memory filesystem with Node.js-compatible API
- **Node.js API Shims** - 40+ shimmed modules (`fs`, `path`, `http`, `events`, and more)
- **npm Package Installation** - Install and run real npm packages in the browser with automatic bin stub creation
- **Run Any CLI Tool** - npm packages with `bin` entries (vitest, eslint, tsc, etc.) work automatically
- **Dev Servers** - Built-in Vite and Next.js development servers
- **Hot Module Replacement** - React Refresh support for instant updates
- **TypeScript Support** - First-class TypeScript/TSX transformation via esbuild-wasm
- **Service Worker Architecture** - Intercepts requests for seamless dev experience
- **Optional Web Worker Support** - Offload code execution to a Web Worker for improved UI responsiveness
- **Secure by Default** - Cross-origin sandbox support for running untrusted code safely

---

## Requirements

- **Node.js 20+** - Required for development and building
- **Modern browser** - Chrome, Firefox, Safari, or Edge with ES2020+ support

> **Note:** almostnode runs in the browser and emulates Node.js 20 APIs. The Node.js requirement is only for development tooling (Vite, Vitest, TypeScript).

---

## Quick Start

### Installation

```bash
npm install almostnode
```

### Basic Usage

```typescript
import { createContainer } from 'almostnode';

// Create a Node.js container in the browser
const container = createContainer();

// Execute JavaScript code directly
const result = container.execute(`
  const path = require('path');
  const fs = require('fs');

  // Use Node.js APIs in the browser!
  fs.writeFileSync('/hello.txt', 'Hello from the browser!');
  module.exports = fs.readFileSync('/hello.txt', 'utf8');
`);

console.log(result.exports); // "Hello from the browser!"
```

> **⚠️ Security Warning:** The example above runs code on the main thread with full access to your page. **Do not use `createContainer()` or `container.execute()` with untrusted code.** For untrusted code, use `createRuntime()` with a cross-origin sandbox - see [Sandbox Setup](#sandbox-setup).

### Running Untrusted Code Securely

```typescript
import { createRuntime, VirtualFS } from 'almo
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

