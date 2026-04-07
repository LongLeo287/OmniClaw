---
id: rune
type: knowledge
owner: OA_Triage
---
# rune
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "@rune-kit/rune",
  "version": "2.8.0",
  "description": "61-skill mesh for AI coding assistants — 5-layer architecture, 200+ connections, 8 platforms (Claude Code, Cursor, Windsurf, Antigravity, Codex, OpenCode, OpenClaw, Generic)",
  "type": "module",
  "bin": {
    "rune": "./compiler/bin/rune.js"
  },
  "scripts": {
    "build": "node compiler/bin/rune.js build",
    "doctor": "node compiler/bin/rune.js doctor && node scripts/version-sync-check.js",
    "test": "node --test compiler/__tests__/*.test.js scripts/__tests__/*.test.js",
    "test:coverage": "c8 --reporter=text --reporter=lcov node --test compiler/__tests__/*.test.js scripts/__tests__/*.test.js",
    "lint": "biome check .",
    "lint:fix": "biome check --fix .",
    "format": "biome format --write .",
    "ci": "biome check . && node --test compiler/__tests__/*.test.js scripts/__tests__/*.test.js && node compiler/bin/rune.js doctor",
    "version-check": "node scripts/version-sync-check.js",
    "prepublishOnly": "node scripts/version-sync-check.js"
  },
  "keywords": [
    "claude-code",
    "cursor",
    "windsurf",
    "antigravity",
    "codex",
    "opencode",
    "openclaw",
    "ai-assistant",
    "ai-coding",
    "skills",
    "coding-agent",
    "tdd",
    "multi-platform"
  ],
  "author": "runedev",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/rune-kit/rune"
  },
  "engines": {
    "node": ">=18"
  },
  "files": [
    "compiler/",
    "skills/",
    "extensions/",
    "contexts/",
    "commands/",
    "agents/",
    "hooks/",
    "references/"
  ],
  "homepage": "https://rune-kit.github.io/rune",
  "bugs": {
    "url": "https://github.com/rune-kit/rune/issues"
  },
  "devDependencies": {
    "@biomejs/biome": "^2.4.7",
    "c8": "^10.1.3"
  }
}

```

### File: README.md
```md
<p align="center">
  <img src="assets/banner.svg" alt="Rune — Skill Mesh for AI Coding Assistants" width="100%">
</p>

<p align="center">
  <strong>Less skills. Deeper connections.</strong><br>
  A lean, interconnected skill ecosystem for AI coding assistants.<br>
  61 skills · 200+ mesh connections · 8 platforms · MIT
</p>

<p align="center">
  <a href="https://rune-kit.github.io/rune"><img src="https://img.shields.io/badge/Landing_Page-rune--kit.github.io-blue?style=for-the-badge" alt="Landing Page"></a>
  <a href="https://rune-kit.github.io/rune#pricing"><img src="https://img.shields.io/badge/Pro_%2449-lifetime-blueviolet?style=for-the-badge" alt="Rune Pro $49"></a>
  <a href="https://rune-kit.github.io/rune#pricing"><img src="https://img.shields.io/badge/Business_%24149-lifetime-orange?style=for-the-badge" alt="Rune Business $149"></a>
  <a href="https://t.me/xlabs_updates"><img src="https://img.shields.io/badge/Telegram-Updates-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Updates"></a>
</p>

<p align="center">
  <strong>Claude Code</strong> (native plugin) · <strong>Cursor</strong> · <strong>Windsurf</strong> · <strong>Google Antigravity</strong> · <strong>OpenAI Codex</strong> · <strong>OpenCode</strong> · any AI IDE
</p>

## Why Rune?

Most skill ecosystems are either **too many isolated skills** (540+ that don't talk to each other) or **rigid pipelines** (A → B → C, if B fails everything stops).

Rune is a **mesh** — 61 skills with 200+ connections across a 5-layer architecture. Skills call each other bidirectionally, forming resilient workflows that adapt when things go wrong.

```
Pipeline:  A → B → C → D         (B fails = stuck)
Hub-Spoke: A → HUB → C           (HUB fails = stuck)
Mesh:      A ↔ B ↔ C             (B fails = A reaches C via D→E)
           ↕       ↕
           D ↔ E ↔ F
```

## Benchmark: With Rune vs Without Rune

We ran 10 standardized coding tasks on Claude Code — once **without** Rune (vanilla), once **with** Rune — and measured tokens, cost, duration, and correctness.

### Headline Results

```
                Without Rune    With Rune     Delta
Avg Tokens:     541,400         454,491       ↓ 16%
Avg Cost:       $0.69           $0.65         ↓ 6%
Avg Duration:   2.3 min         2.1 min       ↓ 9%
Avg Tool Calls: 14              13            ↓ 7%
Correctness:    9/10            9/10          =
```

### Where Rune Shines: Complex Tasks

| Task | Difficulty | Tokens | Cost | Duration | Tools |
|------|-----------|--------|------|----------|-------|
| Refactor 450-line component | Medium | **-62%** | **-17%** | **-32%** | **-27%** |
| Full feature (auth + API + tests) | Complex | **-36%** | **-29%** | **-31%** | **-27%** |
| Add Zod validation | Easy | -9% | **-28%** | **-32%** | 0% |
| Dark mode across 6 components | Hard | ~0% | +10% | -7% | -6% |

Rune doesn't make Claude smarter — Claude already knows how to code. Rune makes Claude **disciplined**. The more complex the task, the more discipline matters.

> _"Without Rune, Claude writes code that works. With Rune, Claude writes code that lasts."_

<details>
<summary>Full 10-task breakdown</summary>

| # | Task | Diff | Tokens | Cost | Time | Correct |
|---|------|------|--------|------|------|---------|
| 1 | Zod Validation | Easy | -9% | -28% | -32% | ✅ → ✅ |
| 2 | Fix N+1 Query | Easy | +12% | +25% | +3% | ❌ → ❌ |
| 3 | Cursor Pagination | Med | +12% | +19% | -9% | ✅ → ✅ |
| 4 | Security Review | Med | +13% | +32% | +3% | ✅ → ✅ |
| 5 | Rate Limiting | Med | +12% | +5% | +5% | ✅ → ✅ |
| 6 | Refactor Component | Med | **-62%** | **-17%** | **-32%** | ✅ → ✅ |
| 7 | Dark Mode (6 files) | Hard | ~0% | +10% | -7% | ✅ → ✅ |
| 8 | DB Migration | Hard | +52% | +11% | +49% | ✅ → ✅ |
| 9 | Memory Leak Debug | Hard | +13% | +28% | -2% | ✅ → ✅ |
| 10 | Full Auth System | Complex | **-36%** | **-29%** | **-31%** | ✅ → ✅ |

_Methodology: Claude Code CLI headless mode (`claude -p --output-format json`), 10 tasks with fixture code, pattern-based correctness evaluation. Source: [`Benchmark/`](Benchmark/)_

</details>

---

## What's New (v2.8.0)

- **Anti-Loop Intelligence** — 7 core skills enriched with execution loop detection, saturation analysis, error pattern matching, artifact folding, budget-aware progression, and recovery policy routing
- **cook v2.1.0** — observation/effect ratio tracking (detects stuck agents reading without writing) + budget-aware phase progression with hard caps on replans, quality retries, and session tool calls
- **completion-gate v1.8.0** — execution loop audit: classifies tool calls as observation vs effect, flags imbalanced ratios and repeating sequences in gate reports
- **scout v0.3.0** — info saturation detection: tracks entity discovery rate and content similarity to stop scanning when diminishing returns detected
- **research v0.4.0** — diminishing returns detection: monitors new-entity ratio and result overlap across searches to skip redundant queries
- **context-engine v0.9.0** — artifact folding: large tool outputs (>4000 chars or >120 lines) saved to `.rune/artifacts/` with compact preview in context
- **debug v1.0.0** — known error pattern catalog: 8 error archetypes (STATELESS_LOSS, MODULE_NOT_FOUND, TYPE_MISMATCH, ASYNC_DEADLOCK, etc.) with recovery hints + error fingerprinting for dedup
- **fix v0.8.0** — recovery policy matrix: classifies errors into 8 types (INPUT_REQUIRED→PROMPT_USER, TIMEOUT→RETRY, POLICY_BLOCKED→ABORT, etc.) before attempting fixes
- **Source attribution cleanup** — removed all enrichment credit lines from skill files to reduce context noise

### Previous (v2.7.0)

- **Deep Knowledge** — 8 core skills enriched with battle-tested patterns: context compaction, structured cumulative memory, milestone analysis, multi-provider adapters, AI-driven interview, prompt-as-API-contract, token budget tracking, incremental stream processing
- **946 Tests** — compiler + signals + hooks + scripts + status + visualizer validation

### Previous (v2.6.0)

- **Mesh Signals** — event-driven skill communication via frontmatter. Skills declare `emit` and `listen` signals; compiler builds a signal graph in `skill-index.json`. 17 signals across 15 core skills
- **Signal Validation** — `scripts/validate-signals.js` checks orphan listeners (hard error), unlistened emitters (warning), signal naming conventions
- **Mesh Contract** (v2.5.0) — `.rune/contract.md` project-level invariants enforced by cook + sentinel as hard gates
- **Tier Override** — Pro/Business packs override Free packs with skill-level merging
- **Scripts Bundling** — compiler copies `scripts/` directories, resolves `{scripts_dir}` placeholders

### Signal Graph

Skills communicate through declarative signals — no runtime event bus, just metadata for discovery, validation, and routing:

```
scout ──emit:codebase.scanned──→ plan, brainstorm
fix ────emit:code.changed──────→ test, sentinel, review, preflight, verification
test ───emit:tests.passed──────→ deploy
test ───emit:tests.failed──────→ debug
sentinel─emit:security.passed──→ deploy
debug ──emit:bug.diagnosed─────→ fix
deploy ─emit:deploy.complete───→ watchdog
cook ───emit:phase.complete────→ session-bridge
```

## What Rune Is (and Isn't)

Rune started as a **Claude Code plugin** and now compiles to **every major AI IDE**. Same 61 skills, same mesh connections, same workflows — zero knowledge loss across platforms.

| | Rune Provides | Claude Code Provides |
|---|---|---|
| **Workflows** | 8-phase TDD cycle (cook), parallel DAG execution (team), rescue pipelines | Basic tool calling |
| **Quality Gates** | preflight + sentinel + review + completion-gate (parallel) | None built-in |
| **Domain Knowledge** | 14 extension packs (trading, SaaS, mobile, etc.) | General-purpose |
| **Cross-Session State** | .rune/ directory (decisions, conventions, progress) | Conversation only |
| **Mesh Resilience** | 200+ skill connections, fail-loud-route-around | Linear execution |
| **Cost Optimization** | Auto model selection (haiku/sonnet/opus per task) | Single model |
| | | |
| **Sandbox & Permissions** | — | Claude Code handles this |
| **Agent Spawning** | — | Claude Code's Task/Agent system |
| **MCP Integration** | — | Claude Code's MCP protocol |
| **File System Access** | — | Claude Code's tool permissions |

### Common Misconceptions

| "Rune doesn't have..." | Reality |
|---|---|
| Task graph / DAG | `team` skill: DAG decomposition → parallel worktree agents → merge coordination |
| CI quality gates | `verification` skill: lint + typecheck + tests + build (actual commands, not LLM review) |
| Memory / state | `session-bridge` + `journal`: cross-session decisions, conventions, ADRs, module health |
| Multi-model strategy | Every skill has assigned model: haiku (scan), sonnet (code), opus (architecture) |
| Agent specialization | 61 specialized skills with dedicated roles (architect, coder, reviewer, scanner, researcher, BA, scaffolder) — each runs as a Task agent via Claude Code |
| Security scanning | `sentinel`: OWASP patterns, secret scanning, dependency audit. `sast`: static analysis |

## Install

### Claude Code (Native Plugin)

```bash
# Install via Claude Code CLI
claude plugin add rune-kit/rune
```

Or add manually in `~/.claude/settings.json` under `installed_plugins`.

Full mesh: subagents, hooks, adaptive routing, mesh analytics.

### Cursor / Windsurf / Antigravity / Any IDE

```bash
# Compile Rune skills for your platform
npx @rune-kit/rune init

# Or specify platform explicitly
npx @rune-kit/rune init --platform cursor
npx @rune-kit/rune init --platform windsurf
npx @rune-kit/rune init --platform antigravity
```

This compiles all 61 skills into your IDE's rules format. Same knowledge, same workflows.

### Platform Comparison

| Feature | Claude Code | Cursor / Windsurf / Others |
|---------|-------------|---------------------------|
| Skills available | 61/61 | 61/61 |
| Mesh connections | 200+ (programmatic) | 200+ (rule references) |
| Workflows & HARD-GATEs | Full | Full |
| Extension packs | 14 | 14 |
| Subagent parallelism | Native | Sequential fallback |
| Lifecycle hooks | 8 hooks (JS runtime) | Inline MUST/NEVER constraints |
| Adaptive model routing | haiku/sonnet/opus | Single model |
| Mesh analytics | Real-time metrics | Not available |

**Same power, different delivery.** Claude Code gets execution efficiency; other IDEs get the same knowledge and workflows.

## Quick Start

```bash
# Onboard any project (generates CLAUDE.md + .rune/ context)
/rune onboard

# Build a feature (full TDD cycle)
/rune cook "add user authentication with JWT"

# Debug an issue
/rune debug "login returns 401 for valid credentials"

# Security scan before commit
/rune sentinel

# Refactor legacy code safely
/rune rescue

# Full project health audit
/rune audit

# Respond to a production incident
/rune incident "login service returning 503 for 30% of users"

# Generate design system before building UI
/rune design "trading dashboard with real-time data"

# Bootstrap a new project from scratch (v2.1.0)
/rune scaffold "REST API with auth, payments, and Docker"

# Deep requirement analysis before building
/rune ba "integrate Telegram bot with trading signals"

# Auto-generate project documentation
/rune docs init

# Build an MCP server
/rune mcp-builder "weather API with forecast tools"
```

## Architecture

### 5-Layer Model

```
╔══════════════════════════════════════════════════════╗
║  L0: ROUTER (1)                                      ║
║  Meta-enforcement — routes every action               ║
║  skill-router                                         ║
╠══════════════════════════════════════════════════════╣
║  L1: ORCHESTRATORS (5)                                ║
║  Full lifecycle workflows                             ║
║  cook │ team │ launch │ rescue │ scaffold             ║
╠══════════════════════════════════════════════════════╣
║  L2: WORKFLOW HUBS (28)                               ║
║  Cross-hub mesh — the key differentiator              ║
║                                                        ║
║  Creation:    plan │ scout │ brainstorm │ design │     ║
║               skill-forge │ ba │ mcp-builder           ║
║  Development: debug │ fix │ test │ review │ db         ║
║  Quality:     sentinel │ preflight │ onboard │         ║
║               audit │ perf │ review-intake │           ║
║               logic-guardian                            ║
║  Delivery:    deploy │ marketing │ incident │ docs     ║
║  Rescue:      autopsy │ safeguard │ surgeon            ║
║  Security:    adversary                                ║
║  Velocity:    retro                                    ║
╠══════════════════════════════════════════════════════╣
║  L3: UTILITIES (27)                                   ║
║  Stateless, pure capabilities                         ║
║                                                        ║
║  Knowledge:   research │ docs-seeker │ trend-scout     ║
║  Reasoning:   problem-solver │ sequential-thinking     ║
║  Validation:  verification │ hallucination-guard │     ║
║               completion-gate │ constraint-check │     ║
║               sast │ integrity-check                   ║
║  State:       context-engine │ journal │               ║
║               session-bridge                           ║
║  Monitoring:  watchdog │ scope-guard                   ║
║  Media:       browser-pilot │ asset-creator │          ║
║               video-creator                            ║
║  Deps:        dependency-doctor                        ║
║  Workspace:   worktree                                 ║
║  Git:         git                                      ║
║  Documents:   doc-processor                            ║
║  Security:    sentinel-env                             ║
║  Memory:      neural-memory                            ║
║  Packs:       context-pack                             ║
║  Slides:      slides                                   ║
╠══════════════════════════════════════════════════════╣
║  L4: EXTENSION PACKS (14)                             ║
║  Domain-specific, install what you need                ║
║                                                        ║
║  @rune/ui │ @rune/backend │ @rune/devops │            ║
║  @rune/mobile │ @rune/security │ @rune/trading │      ║
║  @rune/saas │ @rune/ecommerce │ @rune/ai-ml │        ║
║  @rune/gamedev │ @rune/content │ @rune/analytics │    ║
║  @rune/chrome-ext │ @rune/zalo                         ║
╚══════════════════════════════════════════════════════╝
```

### Layer Rules

| Layer | Can Call | Called By | State |
|-------|---------|----------|-------|
| L0 Router | L1-L3 (routing) | Every message | Stateless |
| L1 Orchestrators | L2, L3 | L0, User | Stateful (workflow) |
| L2 Workflow Hubs | L2 (cross-hub), L3 | L1, L2 | Stateful (task) |
| L3 Utilities | Nothing (pure)* | L1, L2 | Stateless |
| L4 Extensions | L3 | L2 (domain match) | Config-based |

\*L3→L3 exceptions: `context-engin
... [TRUNCATED]
```

### File: rune\package.json
```json
{
  "name": "@rune-kit/rune",
  "version": "2.5.0",
  "description": "61-skill mesh for AI coding assistants — 5-layer architecture, 200+ connections, 8 platforms (Claude Code, Cursor, Windsurf, Antigravity, Codex, OpenCode, OpenClaw, Generic)",
  "type": "module",
  "bin": {
    "rune": "./compiler/bin/rune.js"
  },
  "scripts": {
    "build": "node compiler/bin/rune.js build",
    "doctor": "node compiler/bin/rune.js doctor && node scripts/version-sync-check.js",
    "test": "node --test compiler/__tests__/*.test.js scripts/__tests__/*.test.js",
    "test:coverage": "c8 --reporter=text --reporter=lcov node --test compiler/__tests__/*.test.js scripts/__tests__/*.test.js",
    "lint": "biome check .",
    "lint:fix": "biome check --fix .",
    "format": "biome format --write .",
    "ci": "biome check . && node --test compiler/__tests__/*.test.js scripts/__tests__/*.test.js && node compiler/bin/rune.js doctor",
    "version-check": "node scripts/version-sync-check.js",
    "prepublishOnly": "node scripts/version-sync-check.js"
  },
  "keywords": [
    "claude-code",
    "cursor",
    "windsurf",
    "antigravity",
    "codex",
    "opencode",
    "openclaw",
    "ai-assistant",
    "ai-coding",
    "skills",
    "coding-agent",
    "tdd",
    "multi-platform"
  ],
  "author": "runedev",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/rune-kit/rune"
  },
  "engines": {
    "node": ">=18"
  },
  "files": [
    "compiler/",
    "skills/",
    "extensions/",
    "contexts/",
    "commands/",
    "agents/",
    "hooks/",
    "references/"
  ],
  "homepage": "https://rune-kit.github.io/rune",
  "bugs": {
    "url": "https://github.com/rune-kit/rune/issues"
  },
  "devDependencies": {
    "@biomejs/biome": "^2.4.7",
    "c8": "^10.1.3"
  }
}

```

### File: rune\README.md
```md
<p align="center">
  <img src="assets/banner.svg" alt="Rune — Skill Mesh for AI Coding Assistants" width="100%">
</p>

<p align="center">
  <strong>Less skills. Deeper connections.</strong><br>
  A lean, interconnected skill ecosystem for AI coding assistants.<br>
  61 skills · 200+ mesh connections · 8 platforms · MIT
</p>

<p align="center">
  <a href="https://rune-kit.github.io/rune"><img src="https://img.shields.io/badge/Landing_Page-rune--kit.github.io-blue?style=for-the-badge" alt="Landing Page"></a>
  <a href="https://rune-kit.github.io/rune#pricing"><img src="https://img.shields.io/badge/Pro_%2449-lifetime-blueviolet?style=for-the-badge" alt="Rune Pro $49"></a>
  <a href="https://rune-kit.github.io/rune#pricing"><img src="https://img.shields.io/badge/Business_%24149-lifetime-orange?style=for-the-badge" alt="Rune Business $149"></a>
</p>

<p align="center">
  <strong>Claude Code</strong> (native plugin) · <strong>Cursor</strong> · <strong>Windsurf</strong> · <strong>Google Antigravity</strong> · <strong>OpenAI Codex</strong> · <strong>OpenCode</strong> · any AI IDE
</p>

## Why Rune?

Most skill ecosystems are either **too many isolated skills** (540+ that don't talk to each other) or **rigid pipelines** (A → B → C, if B fails everything stops).

Rune is a **mesh** — 61 skills with 200+ connections across a 5-layer architecture. Skills call each other bidirectionally, forming resilient workflows that adapt when things go wrong.

```
Pipeline:  A → B → C → D         (B fails = stuck)
Hub-Spoke: A → HUB → C           (HUB fails = stuck)
Mesh:      A ↔ B ↔ C             (B fails = A reaches C via D→E)
           ↕       ↕
           D ↔ E ↔ F
```

## Benchmark: With Rune vs Without Rune

We ran 10 standardized coding tasks on Claude Code — once **without** Rune (vanilla), once **with** Rune — and measured tokens, cost, duration, and correctness.

### Headline Results

```
                Without Rune    With Rune     Delta
Avg Tokens:     541,400         454,491       ↓ 16%
Avg Cost:       $0.69           $0.65         ↓ 6%
Avg Duration:   2.3 min         2.1 min       ↓ 9%
Avg Tool Calls: 14              13            ↓ 7%
Correctness:    9/10            9/10          =
```

### Where Rune Shines: Complex Tasks

| Task | Difficulty | Tokens | Cost | Duration | Tools |
|------|-----------|--------|------|----------|-------|
| Refactor 450-line component | Medium | **-62%** | **-17%** | **-32%** | **-27%** |
| Full feature (auth + API + tests) | Complex | **-36%** | **-29%** | **-31%** | **-27%** |
| Add Zod validation | Easy | -9% | **-28%** | **-32%** | 0% |
| Dark mode across 6 components | Hard | ~0% | +10% | -7% | -6% |

Rune doesn't make Claude smarter — Claude already knows how to code. Rune makes Claude **disciplined**. The more complex the task, the more discipline matters.

> _"Without Rune, Claude writes code that works. With Rune, Claude writes code that lasts."_

<details>
<summary>Full 10-task breakdown</summary>

| # | Task | Diff | Tokens | Cost | Time | Correct |
|---|------|------|--------|------|------|---------|
| 1 | Zod Validation | Easy | -9% | -28% | -32% | ✅ → ✅ |
| 2 | Fix N+1 Query | Easy | +12% | +25% | +3% | ❌ → ❌ |
| 3 | Cursor Pagination | Med | +12% | +19% | -9% | ✅ → ✅ |
| 4 | Security Review | Med | +13% | +32% | +3% | ✅ → ✅ |
| 5 | Rate Limiting | Med | +12% | +5% | +5% | ✅ → ✅ |
| 6 | Refactor Component | Med | **-62%** | **-17%** | **-32%** | ✅ → ✅ |
| 7 | Dark Mode (6 files) | Hard | ~0% | +10% | -7% | ✅ → ✅ |
| 8 | DB Migration | Hard | +52% | +11% | +49% | ✅ → ✅ |
| 9 | Memory Leak Debug | Hard | +13% | +28% | -2% | ✅ → ✅ |
| 10 | Full Auth System | Complex | **-36%** | **-29%** | **-31%** | ✅ → ✅ |

_Methodology: Claude Code CLI headless mode (`claude -p --output-format json`), 10 tasks with fixture code, pattern-based correctness evaluation. Source: [`Benchmark/`](Benchmark/)_

</details>

---

## What's New (v2.5.0)

- **Compiled Intent Mesh (CIM)** — compile-time generated `skill-index.json` with intent keywords, mesh graph, and chain predictions. Zero runtime deps. `intent-router` hook auto-suggests skills from user prompts
- **Privacy Mesh** — three-tier pre-tool guard (ALLOW/WARN/BLOCK) with content scanning, skill-aware elevation, per-project `.rune/privacy.json` config
- **Split Pack Auto-Discovery** — compiler now auto-discovers skill files from `skills/` subdirectory when `format: split` packs have no explicit manifest
- **Tier Override** — Pro/Business packs override Free packs with skill-level merging
- **Scripts Bundling** — compiler copies `scripts/` directories, resolves `{scripts_dir}` placeholders
- **61 Core Skills** — +2 since v2.4.0: slides, retro
- **550 Tests** — compiler + hooks + scripts validation

## What Rune Is (and Isn't)

Rune started as a **Claude Code plugin** and now compiles to **every major AI IDE**. Same 61 skills, same mesh connections, same workflows — zero knowledge loss across platforms.

| | Rune Provides | Claude Code Provides |
|---|---|---|
| **Workflows** | 8-phase TDD cycle (cook), parallel DAG execution (team), rescue pipelines | Basic tool calling |
| **Quality Gates** | preflight + sentinel + review + completion-gate (parallel) | None built-in |
| **Domain Knowledge** | 14 extension packs (trading, SaaS, mobile, etc.) | General-purpose |
| **Cross-Session State** | .rune/ directory (decisions, conventions, progress) | Conversation only |
| **Mesh Resilience** | 200+ skill connections, fail-loud-route-around | Linear execution |
| **Cost Optimization** | Auto model selection (haiku/sonnet/opus per task) | Single model |
| | | |
| **Sandbox & Permissions** | — | Claude Code handles this |
| **Agent Spawning** | — | Claude Code's Task/Agent system |
| **MCP Integration** | — | Claude Code's MCP protocol |
| **File System Access** | — | Claude Code's tool permissions |

### Common Misconceptions

| "Rune doesn't have..." | Reality |
|---|---|
| Task graph / DAG | `team` skill: DAG decomposition → parallel worktree agents → merge coordination |
| CI quality gates | `verification` skill: lint + typecheck + tests + build (actual commands, not LLM review) |
| Memory / state | `session-bridge` + `journal`: cross-session decisions, conventions, ADRs, module health |
| Multi-model strategy | Every skill has assigned model: haiku (scan), sonnet (code), opus (architecture) |
| Agent specialization | 61 specialized skills with dedicated roles (architect, coder, reviewer, scanner, researcher, BA, scaffolder) — each runs as a Task agent via Claude Code |
| Security scanning | `sentinel`: OWASP patterns, secret scanning, dependency audit. `sast`: static analysis |

## Install

### Claude Code (Native Plugin)

```bash
# Install via Claude Code CLI
claude plugin add rune-kit/rune
```

Or add manually in `~/.claude/settings.json` under `installed_plugins`.

Full mesh: subagents, hooks, adaptive routing, mesh analytics.

### Cursor / Windsurf / Antigravity / Any IDE

```bash
# Compile Rune skills for your platform
npx @rune-kit/rune init

# Or specify platform explicitly
npx @rune-kit/rune init --platform cursor
npx @rune-kit/rune init --platform windsurf
npx @rune-kit/rune init --platform antigravity
```

This compiles all 61 skills into your IDE's rules format. Same knowledge, same workflows.

### Platform Comparison

| Feature | Claude Code | Cursor / Windsurf / Others |
|---------|-------------|---------------------------|
| Skills available | 61/61 | 61/61 |
| Mesh connections | 200+ (programmatic) | 200+ (rule references) |
| Workflows & HARD-GATEs | Full | Full |
| Extension packs | 14 | 14 |
| Subagent parallelism | Native | Sequential fallback |
| Lifecycle hooks | 8 hooks (JS runtime) | Inline MUST/NEVER constraints |
| Adaptive model routing | haiku/sonnet/opus | Single model |
| Mesh analytics | Real-time metrics | Not available |

**Same power, different delivery.** Claude Code gets execution efficiency; other IDEs get the same knowledge and workflows.

## Quick Start

```bash
# Onboard any project (generates CLAUDE.md + .rune/ context)
/rune onboard

# Build a feature (full TDD cycle)
/rune cook "add user authentication with JWT"

# Debug an issue
/rune debug "login returns 401 for valid credentials"

# Security scan before commit
/rune sentinel

# Refactor legacy code safely
/rune rescue

# Full project health audit
/rune audit

# Respond to a production incident
/rune incident "login service returning 503 for 30% of users"

# Generate design system before building UI
/rune design "trading dashboard with real-time data"

# Bootstrap a new project from scratch (v2.1.0)
/rune scaffold "REST API with auth, payments, and Docker"

# Deep requirement analysis before building
/rune ba "integrate Telegram bot with trading signals"

# Auto-generate project documentation
/rune docs init

# Build an MCP server
/rune mcp-builder "weather API with forecast tools"
```

## Architecture

### 5-Layer Model

```
╔══════════════════════════════════════════════════════╗
║  L0: ROUTER (1)                                      ║
║  Meta-enforcement — routes every action               ║
║  skill-router                                         ║
╠══════════════════════════════════════════════════════╣
║  L1: ORCHESTRATORS (5)                                ║
║  Full lifecycle workflows                             ║
║  cook │ team │ launch │ rescue │ scaffold             ║
╠══════════════════════════════════════════════════════╣
║  L2: WORKFLOW HUBS (28)                               ║
║  Cross-hub mesh — the key differentiator              ║
║                                                        ║
║  Creation:    plan │ scout │ brainstorm │ design │     ║
║               skill-forge │ ba │ mcp-builder           ║
║  Development: debug │ fix │ test │ review │ db         ║
║  Quality:     sentinel │ preflight │ onboard │         ║
║               audit │ perf │ review-intake │           ║
║               logic-guardian                            ║
║  Delivery:    deploy │ marketing │ incident │ docs     ║
║  Rescue:      autopsy │ safeguard │ surgeon            ║
║  Security:    adversary                                ║
║  Velocity:    retro                                    ║
╠══════════════════════════════════════════════════════╣
║  L3: UTILITIES (27)                                   ║
║  Stateless, pure capabilities                         ║
║                                                        ║
║  Knowledge:   research │ docs-seeker │ trend-scout     ║
║  Reasoning:   problem-solver │ sequential-thinking     ║
║  Validation:  verification │ hallucination-guard │     ║
║               completion-gate │ constraint-check │     ║
║               sast │ integrity-check                   ║
║  State:       context-engine │ journal │               ║
║               session-bridge                           ║
║  Monitoring:  watchdog │ scope-guard                   ║
║  Media:       browser-pilot │ asset-creator │          ║
║               video-creator                            ║
║  Deps:        dependency-doctor                        ║
║  Workspace:   worktree                                 ║
║  Git:         git                                      ║
║  Documents:   doc-processor                            ║
║  Security:    sentinel-env                             ║
║  Memory:      neural-memory                            ║
║  Packs:       context-pack                             ║
║  Slides:      slides                                   ║
╠══════════════════════════════════════════════════════╣
║  L4: EXTENSION PACKS (14)                             ║
║  Domain-specific, install what you need                ║
║                                                        ║
║  @rune/ui │ @rune/backend │ @rune/devops │            ║
║  @rune/mobile │ @rune/security │ @rune/trading │      ║
║  @rune/saas │ @rune/ecommerce │ @rune/ai-ml │        ║
║  @rune/gamedev │ @rune/content │ @rune/analytics │    ║
║  @rune/chrome-ext │ @rune/zalo                         ║
╚══════════════════════════════════════════════════════╝
```

### Layer Rules

| Layer | Can Call | Called By | State |
|-------|---------|----------|-------|
| L0 Router | L1-L3 (routing) | Every message | Stateless |
| L1 Orchestrators | L2, L3 | L0, User | Stateful (workflow) |
| L2 Workflow Hubs | L2 (cross-hub), L3 | L1, L2 | Stateful (task) |
| L3 Utilities | Nothing (pure)* | L1, L2 | Stateless |
| L4 Extensions | L3 | L2 (domain match) | Config-based |

\*L3→L3 exceptions: `context-engine`→`session-bridge`, `hallucination-guard`→`research`, `session-bridge`→`integrity-check`

### Cost Intelligence

Every skill has an auto-selected model for optimal cost:

| Task Type | Model | Cost |
|-----------|-------|------|
| Scan, search, validate | Haiku | Cheapest |
| Write code, fix bugs, review | Sonnet | Default |
| Architecture, security audit | Opus | Deep reasoning |

Typical feature: ~$0.05-0.15 (vs ~$0.60 all-opus).

## Key Workflows

### `/rune cook` — Build a Feature

```
Phase 0 RESUME     → detect existing .rune/plan-*.md, load active phase
Phase 1 UNDERSTAND → scout scans codebase, ba elicits requirements
Phase 2 PLAN       → plan creates master plan + phase files
Phase 3 TEST       → test writes failing tests (TDD red)
Phase 4 IMPLEMENT  → fix writes code (TDD green)
Phase 5 QUALITY    → preflight + sentinel + review (parallel)
Phase 6 VERIFY     → verification + hallucination-guard
Phase 7 COMMIT     → git creates semantic commit
Phase 8 BRIDGE     → session-bridge saves state, announce next phase
```

Multi-session: Phase 0 detects existing plans and resumes from the current phase. One phase per session = small context = better code.

### `/rune rescue` — Refactor Legacy Code

```
Phase 0 RECON      → autopsy assesses damage (health score)
Phase 1 SAFETY NET → safeguard writes characterization tests
Phase 2-N SURGERY  → surgeon refactors 1 module per session
Phase N+1 CLEANUP  → remove @legacy markers
Phase N+2 VERIFY   → health score comparison (before vs after)
```

### `/rune launch` — Deploy + Market

```
Phase 1 PRE-FLIGHT → full test suite
Phase 2 DEPLOY     → push to platform
Phase 3 VERIFY     → live site checks + monitoring
Phase 4 MARKET     → landing copy, social, SEO
Phase 5 ANNOUNCE   → publish content
```

## Mesh Resilience

If a skill fails, the mesh adapts:

| If this fails... | Rune tries... |
|---|---|
| debug can't find cause | problem-solver (different reasoning) |
| docs-seeker can't find docs | research (broader web search) |
| scout can't find files | research + docs-seeker |
| test can't run | deploy fix env, then test again |

Loop prevention: max 2 visits per skill, max chain depth 8.

## Cross-Session Persistence

Rune preserves context across sessions via `.rune/`:

```
.rune/
├── decisions.md     — architectural decisions log
├── conventions.md   — established patterns & style
├── progress.md      — task progress tracker
└── session-log.md   — brief s
... [TRUNCATED]
```

### File: compiler\adapters\index.js
```js
/**
 * Adapter Registry
 *
 * Central registry for all platform adapters.
 */

import antigravity from './antigravity.js';
import claude from './claude.js';
import codex from './codex.js';
import cursor from './cursor.js';
import generic from './generic.js';
import openclaw from './openclaw.js';
import opencode from './opencode.js';
import windsurf from './windsurf.js';

const adapters = {
  claude,
  cursor,
  windsurf,
  antigravity,
  generic,
  openclaw,
  codex,
  opencode,
};

/**
 * Get adapter by platform name
 * @param {string} platform
 * @returns {object} adapter
 */
export function getAdapter(platform) {
  const adapter = adapters[platform];
  if (!adapter) {
    const available = Object.keys(adapters).join(', ');
    throw new Error(`Unknown platform "${platform}". Available: ${available}`);
  }
  return adapter;
}

/**
 * List all available platform names
 * @returns {string[]}
 */
export function listPlatforms() {
  return Object.keys(adapters);
}

export { adapters };

```

### File: rune\compiler\adapters\index.js
```js
/**
 * Adapter Registry
 *
 * Central registry for all platform adapters.
 */

import antigravity from './antigravity.js';
import claude from './claude.js';
import codex from './codex.js';
import cursor from './cursor.js';
import generic from './generic.js';
import openclaw from './openclaw.js';
import opencode from './opencode.js';
import windsurf from './windsurf.js';

const adapters = {
  claude,
  cursor,
  windsurf,
  antigravity,
  generic,
  openclaw,
  codex,
  opencode,
};

/**
 * Get adapter by platform name
 * @param {string} platform
 * @returns {object} adapter
 */
export function getAdapter(platform) {
  const adapter = adapters[platform];
  if (!adapter) {
    const available = Object.keys(adapters).join(', ');
    throw new Error(`Unknown platform "${platform}". Available: ${available}`);
  }
  return adapter;
}

/**
 * List all available platform names
 * @returns {string[]}
 */
export function listPlatforms() {
  return Object.keys(adapters);
}

export { adapters };

```

### File: biome.json
```json
{
  "$schema": "https://biomejs.dev/schemas/2.4.7/schema.json",
  "vcs": {
    "enabled": true,
    "clientKind": "git",
    "useIgnoreFile": true
  },
  "files": {
    "includes": [
      "**/compiler/**/*.js",
      "**/scripts/**/*.js",
      "**/scripts/__tests__/**/*.js",
      "!**/node_modules",
      "!**/builds",
      "!**/*.md",
      "!**/*.json"
    ]
  },
  "formatter": {
    "enabled": true,
    "indentStyle": "space",
    "indentWidth": 2,
    "lineWidth": 120
  },
  "linter": {
    "enabled": true,
    "rules": {
      "recommended": true,
      "correctness": {
        "noUnusedVariables": "warn",
        "noUnusedImports": "warn"
      },
      "style": {
        "useConst": "error"
      },
      "suspicious": {
        "noExplicitAny": "off",
        "noVar": "error",
        "noAssignInExpressions": "off",
        "useIterableCallbackReturn": "off",
        "noConsole": { "level": "off", "options": { "allow": ["log"] } }
      },
      "complexity": {
        "noForEach": "off"
      }
    }
  },
  "javascript": {
    "formatter": {
      "quoteStyle": "single",
      "trailingCommas": "all",
      "semicolons": "always"
    }
  }
}

```

### File: CHANGELOG.md
```md
# Changelog

All notable changes to Rune are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [2.5.0] - 2026-03-25

### Added
- **Compiled Intent Mesh (CIM)** — compile-time `skill-index.json` generation with intent keywords, adjacency graph, and chain predictions
- **intent-router hook** — UserPromptSubmit hook that auto-suggests skill routing based on prompt analysis against compiled index
- **Privacy Mesh** — three-tier pre-tool guard (ALLOW/WARN/BLOCK) with content scanning for AWS keys, GitHub tokens, Stripe keys, etc.
- **Per-project privacy config** — `.rune/privacy.json` for custom BLOCK/WARN/ALLOW patterns and elevated skills
- **Skill-aware elevation** — sentinel, review, audit bypass WARN tier; BLOCK tier cannot be bypassed
- **Split pack auto-discovery** — compiler discovers skill files from `skills/` subdir when `format: split` packs have no explicit manifest
- **550 tests** — 18 new tests for skill-index generation, hook behavior, and split pack discovery

### Fixed
- **Command injection** in `version-sync-check.js` — replaced `execSync` with `execFileSync`
- **Dynamic doctor threshold** — skill count no longer hardcoded, scans source directory
- **Split pack builds** — packs with `format: split` but no `skills:` YAML array now build correctly

### Changed
- Skill count: 60→61 (L3: +1 slides)
- Hook count: 8→10 (intent-router, pre-tool-guard rewrite)
- Pre-tool-guard: simple WARN → three-tier Privacy Mesh with content scanning

## [2.4.0] - 2026-03-24

### Added
- **Scripts Bundling** — compiler copies `scripts/` directories and resolves `{scripts_dir}` placeholders in skill output
- **slides** skill (L3) — presentation/slide generation utility
- **Mesh Contract** — `.rune/contract.md` enforced by cook and sentinel

### Changed
- Skill count: 59→60 (L3: 26→27)

## [2.3.0] - 2026-03-22

### Added
- **Tier Override** — compiler resolves Pro/Business skills over Free counterparts with `discoverTieredPacks()`
- Skill-level merging for tiered packs (Pro overrides Free, Business overrides both)
- 8 tests for tier override functionality

### Changed
- Compiler emitter supports multi-tier pack resolution

## [2.2.6] - 2026-03-18

### Improved
- **cook v1.0.0** — Two-stage Mid-Run Signal Detection (keyword fast-path for Cancel/Pause/Status/Steer + context classification for longer messages), Hash-Based Tool Loop Detection (3x warn, 5x force stop, content-aware stuck detection)
- **debug v0.6.0** — Hash-Based Evidence Loop Detection (re-read/re-test/re-grep detection), hypothesis category diversity rule (Data/Control Flow/Environment/State must rotate across cycles)

### Sources
- nextlevelbuilder/goclaw (832★) — two-stage intent classification, SHA256-based loop detection

## [2.2.5] - 2026-03-18

### Improved
- **ba v0.3.0** — Structured Elicitation Frameworks (PICO, INVEST, Jobs-to-be-Done) with decision table for framework selection per requirement type
- **research v0.3.0** — Minimum 3 Complementary Sources HARD-GATE, source type taxonomy, domain diversity rule, triangulation-based synthesis
- **completion-gate v1.4.0** — Default-FAIL QA mindset HARD-GATE, adversarial validation checklist, skeptic sweep on weakest claims

### Sources
- K-Dense claude-scientific-skills (170 skills, literature-review PICO pattern)
- msitarzewski/agency-agents (50.8k★, Default-FAIL QA mindset)

## [2.2.4] - 2026-03-17

### Improved
- **plan v0.6.0** — Workflow Registry 4-view (by Workflow, Component, User Journey, State)
- **team v0.5.0** — NEXUS Handoff Templates with metadata/context/deliverables/quality/evidence
- **cook v0.9.0** — NEXUS-enhanced Cook Report with Deliverables table + Acceptance Criteria tracking

### Sources
- msitarzewski/agency-agents (50.8k★)

## [2.2.3] - 2026-03-15

### Improved
- **7 core skills enriched** from CLI-Anything (17.4k★), GSD (30.8k★), taste-skill (3.4k★)
- test v0.5.0, verification v0.5.0, cook v0.8.0, plan v0.5.0, hallucination-guard v0.3.0, sentinel-env v0.2.0, completion-gate v1.3.0

## [2.2.2] - 2026-03-14

### Improved
- **4 core skills enriched** from superpowers (89k★)
- review v0.3.0, review-intake v1.1.0, skill-forge v1.2.0, completion-gate v1.2.0

## [2.2.1] - 2026-03-14

### Added
- **Enforcement Upgrade** — Antigravity-level IDE compliance across all platforms
  - skill-router v1.2.0: 5-type Request Classifier (CODE_CHANGE|QUESTION|DEBUG|REVIEW|EXPLORE), File Ownership Matrix, Self-Verification HARD-GATE, Routing Proof line
  - brainstorm v0.4.0: Problem Restatement requirement, Dynamic Questioning (P0/P1/P2)
  - cook v0.6.0: Clarification Gate (2-question minimum), Phase Transition Protocol
  - `compiler/transforms/compliance.js`: distributes enforcement preamble to all non-Claude platform builds
- **L4 Pack Enrichment** — all 13 free packs now rated Deep (500+ lines)
  - @rune/ecommerce 675→1212: multi-currency, fraud detection, checkout optimization, search/filtering, webhooks
  - @rune/content 382→1567: search integration, newsletter, scheduling, accessibility, rich media, analytics
  - @rune/gamedev 393→1513: multiplayer/networking, audio, input, ECS, particles, camera, scene management
- Antigravity Kit gap analysis documentation

### Changed
- Compiler pipeline: 7→8 stages (added compliance transform after subagents, before hooks)
- Free pack total lines: 8,253→11,096
- Grand total across 19 packs: 14,170→17,013

## [2.2.0] - 2026-03-09

### Added
- **OpenCode adapter** — 8th supported platform
- **Skills catalog page** — browsable skill listing
- Guides and documentation updates

## [2.1.1] - 2026-03-12

### Added
- **tools: field** on all 55 skills — permission scope per skill
- **@rune-pro/sales** pack (6 skills, private repo)
- **@rune-pro/data-science** pack (7 skills, 1356 lines)
- **@rune-pro/support** pack (6 skills, 802 lines)
- **@rune/chrome-ext** pack (6 skills, 995 lines, FREE)

### Changed
- L4 Tier 1 packs enriched: ui 225→947, security 216→536, backend 257→678, saas 276→805
- Pricing model: subscription → lifetime ($49 Pro, $149 Business)
- Pro packs moved to private repo (rune-kit/rune-pro)

## [2.1.0] - 2026-03-11

### Added
- **6 new skills** (55→58 after adversary + sentinel-env later): ba, scaffold, docs, git, mcp-builder, doc-processor
- **cook v0.5.0**: Phase-aware execution, phase-file resume, master plan tracking
- **plan v0.4.0**: Amateur-Proof Template with master plan + phase files
- **@rune-pro/product** pack (6 skills, 1253 lines)
- **@rune/trading**: experiment-loop skill

### Changed
- Skill count: 49→55 (L1: 4→5, L2: 23→26, L3: 21→23)
- Mesh connections: 170+→200+

## [2.0.0] - 2026-03-08

### Added
- **Multi-platform compiler** — 3-stage pipeline (Parse → Transform → Emit)
- 6 compiler transforms: cross-refs, tool-names, frontmatter, subagents, hooks, branding
- 5 platform adapters: claude, cursor, windsurf, antigravity, generic
- CLI: `npx @rune-kit/rune init|build|doctor`
- All 49 skills compile to ALL platforms with zero knowledge loss

### Changed
- Architecture: from Claude-Code-only to multi-platform mesh

## [1.5.1] - 2025-03-05

### Added
- **Agent Skills standard compliance** — adopted frontmatter fields from Anthropic's official skills spec.
- `context: fork` on all L1 orchestrators (cook, team, launch, rescue) — run in isolated subagent context.
- `disable-model-invocation: true` on side-effect skills (launch, deploy, incident) — prevents Claude from auto-triggering deployments or incident responses.
- `user-invocable: false` on internal L3 utilities (completion-gate, constraint-check, integrity-check, context-engine, scope-guard, worktree, skill-router) — Claude-only background skills.
- Dynamic context injection (`!`command``) on skill-router — injects live routing overrides and skill metrics before Claude reads the routing table.
- Pushy descriptions on all L1 orchestrators — prevents undertriggering per Anthropic's best practice.
- Explicit `skills[]` array in marketplace.json listing all 49 skill paths.

## [1.5.0] - 2025-03-05

### Added
- **logic-guardian** (L2, Quality group) — protects complex business logic from accidental AI deletion/overwrite. Maintains `.rune/logic-manifest.json`, enforces pre-edit gates, validates post-edit diffs.
- **trade-logic** skill in `@rune/trading` extension — trading-specific logic preservation: entry/exit specs, indicator parameter registry, production-backtest sync, state machine documentation, backtest result linkage.
- **docs/TRADE-MATRIX.md** — complete NxN skill-to-skill delegation matrix (4 matrices: L1->L2, L2<->L2, L1/L2->L3, L3->L3 exceptions).
- Plugin instruction feed for proactive skill usage across all projects.
- Session-start hook loads `logic-manifest.json` when present.
- CHANGELOG.md (this file).

### Changed
- Skill count: 48 -> 49 (L2 hubs: 22 -> 23).
- Mesh connections: 160+ -> 170+.
- Updated skill-router routing table with logic-guardian entry.
- Updated ARCHITECTURE.md, README.md, marketplace.json with new counts.

## [1.4.0] - 2025-03-03

### Added
- Behavioral contexts (dev, research, review modes) injected via `.rune/active-context.md`.
- Pre-compact hook preserves critical context before auto-compaction.
- Enhanced cook with L4 extension pack detection (Phase 1.5).
- Enhanced launch with artifact dependency scanning.
- Cross-IDE analysis documentation.

## [1.3.0] - 2025-02-28

### Added
- H3 Intelligence: mesh analytics, adaptive routing, community packs.
- metrics-collector hook captures skill invocations to tmpdir JSONL.
- context-watch extended with tool counters and session timestamp.
- post-session-reflect flushes metrics to `.rune/metrics/`.
- audit Phase 8: Mesh Analytics (`/rune metrics`).
- skill-router Step 0: adaptive routing via `routing-overrides.json`.
- cook Phase 8: skill-sourced metrics and auto routing overrides.
- `/rune pack` commands for community L4 packs.
- `docs/COMMUNITY-PACKS.md` guide.

## [1.2.0] - 2025-02-27

### Added
- Wave 2: SAST skill, constraint-check skill.
- Pre-tool-guard hook, secrets-scan hook.
- Updated plugin manifest with hook definitions.

## [1.1.0] - 2025-02-26

### Added
- Option A lean upgrade: 10 patches across existing skills, 2 new skills, 1 hook.
- skill-forge and review-intake skills.

## [1.0.0] - 2025-02-25

### Added
- Initial release: 44 core skills across 5-layer mesh architecture.
- L0 Router (skill-router), L1 Orchestrators (cook, team, launch, rescue).
- L2 Workflow Hubs and L3 Utilities.
- 12 L4 Extension Packs.
- Cross-session persistence via `.rune/` directory.

```

### File: CLAUDE.md
```md
# Rune — Project Configuration

## Overview

Rune is an interconnected skill ecosystem for AI coding assistants.
61 core skills | 5-layer mesh architecture | 200+ connections | Multi-platform.
Philosophy: "Less skills. Deeper connections."

Works on: Claude Code (native plugin) · Cursor · Windsurf · Google Antigravity · OpenAI Codex · OpenCode · any AI IDE.

## Tech Stack

- Claude Code Plugin System (native)
- Multi-platform compiler (Node.js) — compiles to Cursor, Windsurf, Antigravity, Codex, OpenCode, generic
- Agent Skills SKILL.md format
- Git for version control
- Markdown + JSON for configuration
- JavaScript for hooks/scripts

## Directory Structure

```
rune/
├── .claude-plugin/     # Plugin manifest (Claude Code native)
│   ├── plugin.json     # Plugin metadata
│   └── marketplace.json # Marketplace catalog
├── skills/             # Core skills — SINGLE SOURCE OF TRUTH
├── extensions/         # L4 extension packs (one dir per pack)
├── compiler/           # Multi-platform compiler
│   ├── bin/rune.js     # CLI (init, build, doctor)
│   ├── parser.js       # SKILL.md → IR
│   ├── transformer.js  # Transform pipeline
│   ├── emitter.js      # IR → platform files
│   ├── adapters/       # Platform adapters (claude, cursor, windsurf, antigravity, codex, openclaw, opencode, generic)
│   └── transforms/     # Cross-refs, tool-names, frontmatter, subagents, hooks, branding
├── commands/           # Slash command definitions
├── agents/             # Subagent definitions
├── contexts/           # Behavioral mode injection (dev, research, review)
├── hooks/              # Event hooks (session-start, pre-compact, etc.)
├── scripts/            # Executable scripts for skills
└── docs/               # Documentation, templates, and plans
```

## Mandatory Skill Routing

**ALWAYS invoke skills via the Skill tool. NEVER "mentally apply" a skill or do the work casually.**

When the user's intent matches a skill, invoke it BEFORE writing any code or analysis:

| User Intent | Invoke | NOT This |
|-------------|--------|----------|
| "brainstorm", "ideas", "explore options" | `rune:brainstorm` | Casually listing ideas without framework |
| "plan", "design architecture", "break this down" | `rune:plan` | Writing an inline plan without phase files |
| "build", "implement", "fix", "refactor", "add feature" | `rune:cook` | Writing code without scout/plan/test cycle |
| "review", "check this code" | `rune:review` | Skimming code without file:line findings |
| "test", "write tests" | `rune:test` | Writing tests after implementation (TDD violation) |
| "deploy", "ship", "go live" | `rune:launch` | Running deploy without pre-flight verification |
| "debug", "why is this broken" | `rune:debug` | Guessing at fixes without hypothesis testing |
| "security check", "audit security" | `rune:sentinel` | Surface-level security comments |
| "research", "find out about" | `rune:research` | Single-source answers without triangulation |
| "new project", "bootstrap", "scaffold" | `rune:scaffold` | Creating files without requirements/plan |
| Large task (5+ files, 3+ modules) | `rune:team` | Sequential cook on parallel-eligible work |
| Legacy cleanup (health <40) | `rune:rescue` | Ad-hoc refactoring without safety nets |

**Workflow chains are enforced by each skill's Step 0 prerequisite check:**
- `cook` → checks for approved plan (invokes `plan` if missing)
- `plan` → checks for codebase context (invokes `scout` if missing)
- `fix` → checks for diagnosis (invokes `debug` if missing)
- `deploy` → checks for passing tests + security (invokes `verification` + `sentinel` if missing)

## Conventions

- Every skill MUST have a SKILL.md following docs/SKILL-TEMPLATE.md
- Every extension MUST have a PACK.md following docs/EXTENSION-TEMPLATE.md
- Skill names: lowercase kebab-case, max 64 chars
- Layer rules: L1 calls L2/L3. L2 calls L2/L3. L3 calls nothing (except documented L3→L3 coordination).
- Exception: `team` (L1) can call other L1 orchestrators (meta-orchestration pattern).
- Model selection: haiku (scan), sonnet (code), opus (architecture)
- Commit messages: conventional commits (feat, fix, docs, chore)

## Commands

- Validate plugin: `claude plugin validate .`
- Test locally: `claude --plugin-dir .`
- Build for Cursor: `node compiler/bin/rune.js build --platform cursor --output <project-dir>`
- Build for Windsurf: `node compiler/bin/rune.js build --platform windsurf --output <project-dir>`
- Build for Codex: `node compiler/bin/rune.js build --platform codex --output <project-dir>`
- Build for OpenCode: `node compiler/bin/rune.js build --platform opencode --output <project-dir>`
- Validate build: `node compiler/bin/rune.js doctor`
- Project dashboard: `node compiler/bin/rune.js status` (tiered neofetch)
- Mesh visualizer: `node compiler/bin/rune.js visualize` (interactive graph)
- Run tests: `npm test` (946 tests — compiler + signals + hooks + scripts + status + visualizer)
- Run tests with coverage: `npm run test:coverage` (c8 + lcov)
- Lint: `npm run lint` (Biome)
- Lint + fix: `npm run lint:fix`
- Full CI check: `npm run ci` (lint + test + doctor)

## Current Wave

61 core skills built (v2.8.0 — "Anti-Loop Intelligence").

### L0 Router (1)
skill-router — meta-enforcement layer, routes every action through the correct skill

### L1 Orchestrators (5)
cook, team, launch, rescue, scaffold

### L2 Workflow Hubs (28)
plan, scout, brainstorm, design, skill-forge, debug, fix, test, review, db,
sentinel, preflight, onboard, deploy, marketing, perf,
autopsy, safeguard, surgeon, audit, incident, review-intake, logic-guardian,
ba, docs, mcp-builder, adversary, retro

### L3 Utilities (27)
research, docs-seeker, trend-scout, problem-solver, sequential-thinking,
verification, hallucination-guard, completion-gate, constraint-check, sast, integrity-check,
context-engine, context-pack, journal, session-bridge, neural-memory, worktree,
watchdog, scope-guard, browser-pilot, asset-creator, video-creator, slides,
dependency-doctor, git, doc-processor, sentinel-env

### L4 Extension Packs (14)
@rune/ui, @rune/backend, @rune/devops, @rune/mobile, @rune/security,
@rune/trading, @rune/saas, @rune/ecommerce, @rune/ai-ml, @rune/gamedev,
@rune/content, @rune/analytics, @rune/chrome-ext, @rune/zalo

All layers complete. Repository: https://github.com/rune-kit/rune

### Rune Pro (Premium Extensions — separate private repo)
Repository: https://github.com/rune-kit/rune-pro (private)
@rune-pro/product (✅), @rune-pro/sales (✅), @rune-pro/data-science (✅), @rune-pro/support (✅)
Pricing: $49 lifetime (Pro), $149 lifetime (Business)
Pro packs use same PACK.md format, install into `extensions/pro-*/`.

### Rune Business (Enterprise Extensions — separate private repo)
Repository: https://github.com/rune-kit/rune-business (private)
@rune-business/finance (✅), @rune-business/legal (✅), @rune-business/hr (✅), @rune-business/enterprise-search (✅)
4 packs, 26 skills. $149 lifetime.

## Full Spec

See `docs/ARCHITECTURE.md` for the 5-layer architecture reference.

<!-- gitnexus:start -->
# GitNexus — Code Intelligence

This project is indexed by GitNexus as **Free** (549 symbols, 690 relationships, 16 execution flows). Use the GitNexus MCP tools to understand code, assess impact, and navigate safely.

> If any GitNexus tool warns the index is stale, run `npx gitnexus analyze` in terminal first.

## Always Do

- **MUST run impact analysis before editing any symbol.** Before modifying a function, class, or method, run `gitnexus_impact({target: "symbolName", direction: "upstream"})` and report the blast radius (direct callers, affected processes, risk level) to the user.
- **MUST run `gitnexus_detect_changes()` before committing** to verify your changes only affect expected symbols and execution flows.
- **MUST warn the user** if impact analysis returns HIGH or CRITICAL risk before proceeding with edits.
- When exploring unfamiliar code, use `gitnexus_query({query: "concept"})` to find execution flows instead of grepping. It returns process-grouped results ranked by relevance.
- When you need full context on a specific symbol — callers, callees, which execution flows it participates in — use `gitnexus_context({name: "symbolName"})`.

## When Debugging

1. `gitnexus_query({query: "<error or symptom>"})` — find execution flows related to the issue
2. `gitnexus_context({name: "<suspect function>"})` — see all callers, callees, and process participation
3. `READ gitnexus://repo/Free/process/{processName}` — trace the full execution flow step by step
4. For regressions: `gitnexus_detect_changes({scope: "compare", base_ref: "main"})` — see what your branch changed

## When Refactoring

- **Renaming**: MUST use `gitnexus_rename({symbol_name: "old", new_name: "new", dry_run: true})` first. Review the preview — graph edits are safe, text_search edits need manual review. Then run with `dry_run: false`.
- **Extracting/Splitting**: MUST run `gitnexus_context({name: "target"})` to see all incoming/outgoing refs, then `gitnexus_impact({target: "target", direction: "upstream"})` to find all external callers before moving code.
- After any refactor: run `gitnexus_detect_changes({scope: "all"})` to verify only expected files changed.

## Never Do

- NEVER edit a function, class, or method without first running `gitnexus_impact` on it.
- NEVER ignore HIGH or CRITICAL risk warnings from impact analysis.
- NEVER rename symbols with find-and-replace — use `gitnexus_rename` which understands the call graph.
- NEVER commit changes without running `gitnexus_detect_changes()` to check affected scope.

## Tools Quick Reference

| Tool | When to use | Command |
|------|-------------|---------|
| `query` | Find code by concept | `gitnexus_query({query: "auth validation"})` |
| `context` | 360-degree view of one symbol | `gitnexus_context({name: "validateUser"})` |
| `impact` | Blast radius before editing | `gitnexus_impact({target: "X", direction: "upstream"})` |
| `detect_changes` | Pre-commit scope check | `gitnexus_detect_changes({scope: "staged"})` |
| `rename` | Safe multi-file rename | `gitnexus_rename({symbol_name: "old", new_name: "new", dry_run: true})` |
| `cypher` | Custom graph queries | `gitnexus_cypher({query: "MATCH ..."})` |

## Impact Risk Levels

| Depth | Meaning | Action |
|-------|---------|--------|
| d=1 | WILL BREAK — direct callers/importers | MUST update these |
| d=2 | LIKELY AFFECTED — indirect deps | Should test |
| d=3 | MAY NEED TESTING — transitive | Test if critical path |

## Resources

| Resource | Use for |
|----------|---------|
| `gitnexus://repo/Free/context` | Codebase overview, check index freshness |
| `gitnexus://repo/Free/clusters` | All functional areas |
| `gitnexus://repo/Free/processes` | All execution flows |
| `gitnexus://repo/Free/process/{name}` | Step-by-step execution trace |

## Self-Check Before Finishing

Before completing any code modification task, verify:
1. `gitnexus_impact` was run for all modified symbols
2. No HIGH/CRITICAL risk warnings were ignored
3. `gitnexus_detect_changes()` confirms changes match expected scope
4. All d=1 (WILL BREAK) dependents were updated

## CLI

- Re-index: `npx gitnexus analyze`
- Check freshness: `npx gitnexus status`
- Generate docs: `npx gitnexus wiki`

<!-- gitnexus:end -->

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
