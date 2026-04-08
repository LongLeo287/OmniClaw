Reference documentation for the SDD phase sub-agents and skill system. For quick start, see the [main README](../README.md).

# Sub-Agents & Skill Registry

## SDD Phase Sub-Agents

Each sub-agent is a SKILL.md file — pure Markdown instructions that any AI assistant can follow. The preferred path is for the orchestrator to pre-resolve relevant skills from the registry and inject compact rules into each sub-agent prompt. Sub-agents still support registry/path fallback for backward compatibility.

| Sub-Agent | Skill File | What It Does |
|-----------|-----------|-------------|
| **Init** | `sdd-init/SKILL.md` | Detects project stack, bootstraps persistence, builds skill registry |
| **Explorer** | `sdd-explore/SKILL.md` | Reads codebase, compares approaches, identifies risks |
| **Proposer** | `sdd-propose/SKILL.md` | Creates `proposal.md` with intent, scope, rollback plan |
| **Spec Writer** | `sdd-spec/SKILL.md` | Writes delta specs (ADDED/MODIFIED/REMOVED) with Given/When/Then |
| **Designer** | `sdd-design/SKILL.md` | Creates `design.md` with architecture decisions and rationale |
| **Task Planner** | `sdd-tasks/SKILL.md` | Breaks down into phased, numbered task checklist |
| **Implementer** | `sdd-apply/SKILL.md` | Writes code following specs and design, marks tasks complete. v2.0: TDD workflow support |
| **Verifier** | `sdd-verify/SKILL.md` | Validates implementation against specs with real test execution. v2.0: spec compliance matrix |
| **Archiver** | `sdd-archive/SKILL.md` | Merges delta specs into main specs, moves to archive |
| **Skill Registry** | `skill-registry/SKILL.md` | Scans user skills + project conventions, writes `.atl/skill-registry.md` |
| **Judgment Day** | `judgment-day/SKILL.md` | Runs dual adversarial review with two blind judges and a fix loop |
| **Go Testing** | `go-testing/SKILL.md` | Shared conventions for Go tests, including Bubbletea and teatest patterns |
| **Skill Creator** | `skill-creator/SKILL.md` | Creates new reusable skills following the project skill spec |
| **Branch + PR** | `branch-pr/SKILL.md` | Branches changes and opens pull requests with repo conventions |
| **Issue Creation** | `issue-creation/SKILL.md` | Creates GitHub issues with the repo's structured templates |

### Sub-Agent Result Contract

Each sub-agent must return a structured envelope with these fields:

| Field | Description |
|-------|-------------|
| `status` | `success`, `partial`, or `blocked` |
| `executive_summary` | 1-3 sentence summary of what was done |
| `detailed_report` | (optional) Full phase output, or omit if already inline |
| `artifacts` | List of artifact keys/paths written |
| `next_recommended` | The next SDD phase to run, or "none" |
| `risks` | Risks discovered, or "None" |
| `skill_resolution` | `injected`, `fallback-registry`, `fallback-path`, or `none` |

Example:

```markdown
**Status**: success
**Summary**: Proposal created for `{change-name}`. Defined scope, approach, and rollback plan.
**Artifacts**: Engram `sdd/{change-name}/proposal` | `openspec/changes/{change-name}/proposal.md`
**Next**: sdd-spec or sdd-design
**Risks**: None
```

`executive_summary` is intentionally short. `detailed_report` can be as long as needed for complex architecture work.

### Sub-Agent Context Protocol

Sub-agents start with a **fresh context**. The orchestrator is responsible for resolving the skill registry once, matching relevant skills, and injecting compact rules into the sub-agent prompt as `## Project Standards (auto-resolved)`. If that block is missing, sub-agents fall back to registry lookup or explicit `SKILL: Load` paths.

Sub-agents are also instructed to save discoveries, decisions, and bug fixes to engram automatically (non-SDD sub-agents) or via the mandatory persist step (SDD phases).

---

## Shared Conventions

All skills reference three shared convention files in `skills/_shared/`. Critical engram calls (`mem_search`, `mem_save`, `mem_get_observation`) are also **inlined directly in each skill** so sub-agents don't need to follow multi-hop file references.

| File | Purpose |
|------|---------|
| `persistence-contract.md` | Mode resolution rules, sub-agent context protocol, skill registry loading protocol |
| `engram-convention.md` | Supplementary reference for deterministic naming (`sdd/{change-name}/{artifact-type}`) and two-step recovery. Critical calls are inlined in skills. |
| `openspec-convention.md` | Filesystem paths for each artifact, directory structure, config.yaml reference, and archive layout |
| `skill-resolver.md` | Universal protocol for delegators to inject compact rules from the skill registry |

**Why inline + shared:**
- **Sub-agents fail multi-hop chains** — A 3-hop read chain (skill → convention file → actual instructions) breaks non-Claude models. Inlining the critical calls eliminates this.
- **Deterministic recovery** — Engram artifact naming follows a strict `sdd/{change}/{type}` convention with `topic_key`, so any skill can reliably find artifacts created by other skills.
- **Consistent mode behavior** — All skills resolve `engram | openspec | hybrid | none` the same way. `openspec` and `hybrid` are never chosen automatically.

---

## Skill Registry

Sub-agents start with a **fresh context** — they do not know what user skills exist (React, TDD, Playwright, etc.). The skill registry solves this, and the orchestrator uses it to inject compact rules before each delegation.

**How it works:**
1. `/sdd-init` or `/skill-registry` scans your installed skills and project conventions
2. Writes `.atl/skill-registry.md` in the project root (mode-independent, always created)
3. If engram is available, also saves to engram (cross-session bonus)
4. The orchestrator reads the registry once and caches the **Compact Rules** section plus the trigger table
5. For each delegation, the orchestrator injects matching rules as `## Project Standards (auto-resolved)`
6. Fallback order if standards were not injected: `mem_search(query: "skill-registry", project: "{project}")` → `.atl/skill-registry.md` → explicit `SKILL: Load` paths
7. Delegations report `skill_resolution` so the orchestrator can detect and repair cache loss after compaction

**Preferred path:** the orchestrator pre-resolves compact rules. Sub-agent self-loading is only a compatibility fallback.

**What it contains:**
- User skills table: trigger → skill name → path (e.g., "React components" → `react-19` → `~/.claude/skills/react-19/SKILL.md`)
- Compact rules blocks: short, pre-digested instructions that delegators paste directly into sub-agent prompts
- Project conventions found: `agents.md`, `CLAUDE.md`, `.cursorrules`, etc.

**When to update:** Run `/skill-registry` after installing or removing skills.

---

## Per-Agent Model Routing

Each agent can have a `model` field in `opencode.json` that defines which model it should use. When the orchestrator delegates via `delegate(prompt, agent)` or `Task`, the background-agents plugin passes the `model` through to `session.prompt()`, so the sub-agent runs on its configured model.

**Example** (`opencode.multi.json`):

```json
{
  "sdd-explore": {
    "model": "<your-provider/your-model>",
    "mode": "subagent",
    ...
  },
  "sdd-spec": {
    "model": "<your-provider/your-model>",
    "mode": "subagent",
    ...
  }
}
```

For single-model setups (`opencode.single.json`), omit the `model` field entirely — all agents inherit OpenCode's global default model.

**Alternative: `@agent-name` text mentions.** OpenCode also supports routing via `@agent-name` mentions in the orchestrator's output, which triggers native agent routing. This is an alternative to `delegate()` but is NOT required — `delegate()` handles model routing correctly.
