---
id: alinaqi-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:46.208655
---

# KNOWLEDGE EXTRACT: alinaqi
> **Extracted on:** 2026-03-30 17:29:07
> **Source:** alinaqi

---

## File: `claude-bootstrap.md`
```markdown
# 📦 alinaqi/claude-bootstrap [🔖 PENDING/APPROVE]
🔗 https://github.com/alinaqi/claude-bootstrap


## Meta
- **Stars:** ⭐ 552 | **Forks:** 🍴 43
- **Language:** Shell | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Opinionated project initialization for Claude Code. Security-first, spec-driven, AI-native.

## README (trích đầu)
```
# Claude Bootstrap

> An opinionated project initialization system for Claude Code. **Agent teams by default, strict TDD pipeline, multi-engine code review, security-first.**

**The bottleneck has moved from code generation to code comprehension.** AI can generate infinite code, but humans still need to review, understand, and maintain it. Claude Bootstrap provides guardrails that keep AI-generated code simple, secure, and verifiable.

**New in v2.7.0:** Tiered Code Graph system — every project gets a persistent knowledge graph via MCP. Claude queries the graph for sub-ms symbol lookup, dependency analysis, and blast radius instead of brute-force file reads. Opt-in CPG analysis (Joern + CodeQL) adds AST + CFG + PDG for deep data flow and security auditing.

**v2.5.0:** Every project now runs as a coordinated team of AI agents. A Team Lead orchestrates, a Quality Agent enforces TDD, a Security Agent scans for vulnerabilities, a Code Review Agent runs multi-engine reviews, a Merger Agent creates PRs, and dedicated Feature Agents implement each feature in parallel - all following an immutable pipeline: **Spec > Tests > Fail > Implement > Pass > Review > Security > PR.**

## Core Philosophy

```
┌────────────────────────────────────────────────────────────────┐
│  ITERATIVE LOOPS BY DEFAULT                                    │
│  ─────────────────────────────────────────────────────────────│
│  Every task runs in a self-referential loop until tests pass.  │
│  Claude iterates autonomously. You describe what, not how.     │
│  Powered by Ralph Wiggum - iteration > perfection.             │
├────────────────────────────────────────────────────────────────┤
│  TESTS FIRST, ALWAYS                                           │
│  ─────────────────────────────────────────────────────────────│
│  Features: Write tests → Watch them fail → Implement → Pass    │
│  Bugs: Find test gap → Write failing test → Fix → Pass         │
│  No code ships without a test that failed first.               │
├────────────────────────────────────────────────────────────────┤
│  SIMPLICITY IS NON-NEGOTIABLE                                  │
│  ─────────────────────────────────────────────────────────────│
│  20 lines per function │ 200 lines per file │ 3 params max     │
│  If you can't understand the whole system in one session,      │
│  it's too complex.                                             │
├────────────────────────────────────────────────────────────────┤
│  SECURITY BY DEFAULT                                           │
│  ─────────────────────────────────────────────────────────────│
│  No secrets in code │ No secrets in client env vars            │
│  Dependency scanning │ Pre-commit hooks │ CI enforcement       │
├────────────────────────────────────────────────────────────────┤
│  CODE REVIEWS ARE MANDATORY                                    │
│  ─────────────────────────────────────────────────────────────│
│  Every commit requires /code-review before push.  
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

