# Token Economics of Orchestrator Delegation

## 1. Executive Summary

The orchestrator+sub-agent model in `agent-teams-lite` trades a **fixed overhead per sub-agent** (~11,850 tokens) for **context isolation**: work done by sub-agents disappears from the orchestrator's context when they finish. Three independent analyses measured real file sizes from the codebase. Six optimizations were implemented, reducing overhead ~38% per SDD pipeline. For tasks touching 8+ files, delegation wins by 13,000+ tokens. For large features, the margin exceeds 100,000 tokens.

---

## 2. The Problem: Context Window Economics

Every LLM turn reprocesses the full conversation history:

```
cost_turn_N = system_prompt + Σ(all_previous_messages) + current_message
```

This makes inline orchestrator work exponentially expensive:

- **Context pollution**: Every file read, grep, and edit confirmation stays in history permanently
- **Compaction is lossy**: When the context hits the limit, the model summarizes — losing file contents and tool results. Recovery re-reads those files, growing the context further
- **The flywheel**: inline work → context growth → compaction → re-reads → more growth → faster compaction

Delegation breaks this flywheel because sub-agent file reads never enter the orchestrator's context.

---

## 3. Measurements

All measurements derived from real file sizes (bytes ÷ 3.5 chars/token for markdown).

### Fixed overhead per sub-agent launch

| Component | Tokens |
|-----------|--------|
| System prompt (CLAUDE.md) | 7,554 |
| AGENTS.md workspace rules | 651 |
| Skill file (range across all skills) | 1,796–2,812 |
| Engram skill registry lookup | 1,028 |
| Launch prompt + result envelope | 300–500 |
| **Total per delegation** | **~11,850–12,866** |

> The system prompt dominates. Prior estimates of ~3,700T used the example CLAUDE.md (2,440T), not the actual installed one (7,554T).

### Crossover point

The break-even is a function of dependency count, not a fixed number:

```
crossover(N_deps) = (system_prompt + skill_file + N_deps × avg_dep_size) / avg_file_size
```

| Scenario | Crossover (files) |
|----------|-----------------|
| No SDD dependencies | ~8 files |
| 1–2 SDD artifact reads | ~10 files |
| 4 SDD dependencies (sdd-apply) | ~12 files |

### Compaction cost comparison

| Model | Cost per compaction | Events (large feature) | Total |
|-------|--------------------|-----------------------|-------|
| Inline | 15,000–55,000T | 2–4 | ~75,000T |
| Delegation | ~4,500T | 0–1 | ~4,500T |

Delegation recovery uses engram references (~300T) instead of re-reading files (~3,000–15,000T per artifact).

---

## 4. The Real Driver

Token savings come from three sources with very different weights:

| Driver | Share of savings | Mechanism |
|--------|-----------------|-----------|
| Context scope isolation | ~60% | Sub-agent file reads never enter orchestrator history |
| Compaction avoidance | ~25% | Fewer tokens in orchestrator = fewer compaction triggers |
| Error reduction | ~10% | Smaller failure domain per sub-agent |
| Parallelism bonus | ~5% | Independent phases can run concurrently |

The primary driver is **not** skill guidance or error reduction. It is that files read by sub-agents **disappear** when they return.

---

## 5. Optimizations Implemented

Six changes reduced fixed overhead ~38% per full SDD pipeline:

| # | Optimization | Savings/pipeline | Rationale |
|---|-------------|-----------------|-----------|
| 1 | Remove `persistence-contract.md` reads | ~22,000T | Sub-agents already have inline instructions; file read was redundant |
| 2 | Artifact size budgets (word limits) | ~14,000T | Verbose artifacts compound across all downstream phases |
| 3 | Skill registry pre-resolution | ~11,400T | Orchestrator resolves once; sub-agents skip search |
| 4 | Common boilerplate extraction | ~4,200T | Shared file for return envelope + upsert notes |
| 5 | Orchestrator doc compression | ~4,200 chars | Tables over prose for lookup data |
| 6 | Parallel engram reads | ~800T | Batch `mem_search`/`mem_get_observation` calls |

---

## 6. Review Process and Corrections

Three independent AI reviewers evaluated the optimizations across three rounds.

**Round 1 findings:**
- Skill registry instructions contradicted between orchestrator and skill files
- Anti-patterns collapsed to one line lost compliance weight for AI agents
- "See common file" reference was too passive — agents need explicit instruction
- Token budgets should use word counts (stable across models), not token counts
- CLAUDE.md diverged from examples

**Round 2 findings (post-fix audit):**
- Registry story unified across all files ✅
- Anti-patterns restored to explicit `DO NOT` bullets ✅
- Minor: fallback line and README still referenced old model → fixed in Round 3 ✅

---

## 7. Decision Rules

| Scenario | Files | Recommendation |
|----------|-------|---------------|
| Trivial edit (rename, 1 file) | 1 | Inline |
| Small fix needing context | 2–7 | Inline if <6 turns expected |
| Medium feature | 8–15 | Delegate |
| Large feature / SDD | 15+ | Delegate (mandatory) |
| Multi-day work | Any | Full SDD pipeline with delegation |

> **Per-file delegation is wasteful** (overhead ~1,209% for a 1-file task). Per-phase delegation is the sweet spot.

---

## 8. Key Insights

1. **The orchestrator is an event loop with O(1) state; sub-agents are stateless workers.** Keep them that way.

2. **Delegation doesn't make sub-agents smarter — it makes their failure domain smaller.** A sub-agent that fails affects only itself; inline failure corrupts orchestrator state.

3. **Engram passes references, not content.** Each SDD artifact reference costs ~50T to pass; passing the content inline would cost 3,000–15,000T per artifact.

4. **System prompt size is the dominant variable.** Compressing CLAUDE.md from 7,554T to even 4,000T would drop the crossover from ~8 files to ~5 files — making delegation viable for a much larger class of tasks.

5. **The crossover shifts with each optimization.** As overhead decreases, more tasks benefit from delegation. Optimization is a multiplier, not a one-time fix.
