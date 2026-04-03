---
id: shynlee04-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:13.639119
---

# KNOWLEDGE EXTRACT: shynlee04
> **Extracted on:** 2026-03-30 17:53:20
> **Source:** shynlee04

---

## File: `hivemind-plugin.md`
```markdown
# 📦 shynlee04/hivemind-plugin [🔖 PENDING/APPROVE]
🔗 https://github.com/shynlee04/hivemind-plugin


## Meta
- **Stars:** ⭐ 53 | **Forks:** 🍴 18
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-01
- **Status in AI OS:** 🔖 PENDING/APPROVE

## Description:
(No description)

## README (excerpt)
```
# HiveMind Context Governance

> **The operating system for AI coding sessions.**

## 🇻🇳 v2.8 Release prioritizing Vietnamese market

HiveMind is an [OpenCode](https://opencode.ai) plugin that helps AI agents avoid context drift, forgetting Architecture decisions, and losing Status: when sessions run long. v2.8 focus: clear onboarding, tight governance, and practical deployment for Vietnamese teams first.

### 10 impressive demo scenarios for launch
1. `SaaS 0→1 for non-coders`: Q&A menu + auto-lane to produce deployable PRD.
2. `Rescue enterprise team's chaotic prompts`: extract requirements, ambiguity map, risk register.
3. `War-room production incident`: force agent through evidence checklist before concluding fix.
4. `TDD autopilot`: agent automatically transitions from `spec -> build -> validate` with test gate.
5. `MCP-first research sprint`: coordinate Context7/DeepWiki/Tavily/Exa/Repomix and score confidence.
6. `Brownfield modernization`: scan old codebase, plan refactor workflow by lane and checkpoint.
7. `Cross-domain planning`: same framework for dev + marketing + finance + office-ops.
8. `Subagent swarm governance`: parallel tasking while maintaining trace, export, and review.
9. `Bilingual coaching mode`: EN/VI output with same structure, supporting multi-role team onboarding.
10. `No-command recovery`: user speaks naturally, system auto-realigns to appropriate command and requests next-step permission.

# 🇻🇳 Vietnamese Guide (Detailed)

> *This section is not a translation — written specifically for Vietnamese users, with deeper explanation of how it works and why.*

**Find this useful?** [![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee-support-orange?logo=buy-me-a-coffee&logoColor=white)](https://buymeacoffee.com/shynlee04l)

## What is HiveMind?

Imagine you hire a very skilled AI programmer, but he has one Problem: **every 30 minutes he forgets everything he's doing**.

That's exactly what happens with current AI coding agents:
- Working on feature A, suddenly jumps to feature B without checkpoint
- After context compaction (when memory runs out), forgets why Architecture X was decided
- Delegates to subagent, receives Result: but doesn't synthesize back
- New session starts from zero — knows nothing about previous session

**HiveMind solves all** with a simple but effective context governance system.

## How It Works (Easy Explanation)

Every AI working session follows a process:

```
declare_intent → map_context → [work] → compact_session
   (declare)       (update)     (code)      (archive)
```

### Step 1: Declare Intent — `declare_intent`

Before starting any work, agent must state clearly:
- **What's being done**: "Building authentication system"
- **How**: `plan_driven` (planned), `quick_fix` (quick fix), or `exploration` (exploration)

If not declared, in `strict` mode agent will be locked — cannot write files until declaration. This ensures every task has clear intent.
```

---

*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```
