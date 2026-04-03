---
id: -civ-analysis
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:48.043067
---

# CIV Analysis — MiniMax-MCP-JS

**Date:** 2026-03-18 | **Analyst:** content-analyst-agent | **Score:** 75/100

## Purpose

MiniMax-MCP-JS — JavaScript/TypeScript variant của MiniMax MCP server. Enables Node.js / web environments để gọi MiniMax TTS, Image Gen, Video Gen qua MCP protocol. 109⭐.

## Conflicts

- Companion của `MiniMax-MCP` (Python) — JS variant, không conflict.
- Mở rộng MiniMax stack cho web/Node.js contexts.

## Recommended Department

**Engineering** — Node.js/web frontend integration với MiniMax APIs.

## Routing Decision

`plugins/MiniMax-MCP-JS` ✅

## Quality Assessment

- **Stars:** 109 — moderate | **Age:** 11 months
- **Language:** TypeScript
- **Risk:** LOW — official MiniMax org

## NLM Use Case

Dùng khi build web app cần TTS/image gen — complement `MiniMax-MCP` Python version.
