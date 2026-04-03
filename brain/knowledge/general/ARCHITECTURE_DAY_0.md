---
id: architecture-day-0
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:50.033168
---

# OmniClaw Architecture: Day 0 (The OS-Agnostic Blueprint)

**Date:** 2026-04-01 | **Author:** OmniClaw CEO & Antigravity (Architects)

## The Macro-Structure (Mind, Body, Nervous System)
OmniClaw is not just a script; it is an Artificial Operating System. To achieve enterprise-scale stability and prevent data pollution (hallucinations), the system is strictly decoupled into three physical domains:

1. **`brain/` (The Mind / Memory State):** Contains all historical context, rules, prompts, and knowledge feeds. This is a read-dominant region for Agents (via RAG). It is entirely devoid of executable logic to preserve the purity of the vector index.
2. **`ecosystem/` (The Body / Action State):** Contains executable code, MCP servers, agent scripts, and plugins. Action-dominant.
3. **`core/` (The Nervous System):** Contains autonomic background daemons like the OmniClaw Health Daemon (OHD) that silently heal, sanitize, and protect the OS without agent intervention.

## The Multi-Tenant Horizon (`brain/memory/tenants`)
While OmniClaw natively operates on a Corporate Brain model (`brain/corp`), the `brain/memory/` tier (specifically `tenants/`) acts as the architectural scaffolding for a future SaaS pivot. When OmniClaw scales into a Centralized Orchestrator managing multiple B2B projects simultaneously, the `tenants/` directory will provide zero-knowledge isolation between concurrent corporate brains. Until then, these directories remain gracefully dormant.

## Absolute Directives
- **Zero Local Hardcodes:** No file shall ever cite a local machine path (e.g., `D:\LongLeo\...`). OmniClaw is 100% OS-Agnostic.
- **English-Only Core:** System logic runs purely on Technical English to maintain global open-source viability.
- **Brand Purity:** The enterprise is strictly "OmniClaw" (not "OmniClaw Corp" or other variants).
