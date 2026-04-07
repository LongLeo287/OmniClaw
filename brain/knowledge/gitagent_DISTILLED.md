---
id: gitagent
type: knowledge
owner: OA_Triage
---
# gitagent
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "@shreyaskapale/gitagent",
  "version": "0.1.7",
  "description": "A framework-agnostic, git-native standard for defining AI agents",
  "type": "module",
  "bin": {
    "gitagent": "./dist/index.js"
  },
  "scripts": {
    "build": "tsc && chmod +x dist/index.js",
    "dev": "tsc --watch",
    "start": "node dist/index.js",
    "test": "node --test dist/**/*.test.js",
    "prepublishOnly": "npm run build"
  },
  "keywords": [
    "ai",
    "agent",
    "git",
    "mcp",
    "a2a",
    "finra",
    "compliance",
    "claude-code",
    "openai",
    "crewai",
    "langchain",
    "agent-framework",
    "agent-standard",
    "ai-agent",
    "llm",
    "agent-definition",
    "version-control"
  ],
  "author": "shreyaskapale",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/open-gitagent/gitagent.git"
  },
  "homepage": "https://gitagent.sh",
  "bugs": {
    "url": "https://github.com/open-gitagent/gitagent/issues"
  },
  "engines": {
    "node": ">=18"
  },
  "files": [
    "dist/",
    "spec/",
    "examples/",
    "README.md",
    "docs.md"
  ],
  "dependencies": {
    "ajv": "^8.17.1",
    "ajv-formats": "^3.0.1",
    "chalk": "^5.3.0",
    "commander": "^12.1.0",
    "inquirer": "^9.3.7",
    "js-yaml": "^4.1.0"
  },
  "devDependencies": {
    "@types/inquirer": "^9.0.7",
    "@types/js-yaml": "^4.0.9",
    "@types/node": "^22.10.0",
    "typescript": "^5.7.0"
  }
}

```

### File: README.md
```md
<p align="center">
  <img src="banner.png" alt="gitagent banner" width="700" />
</p>

# gitagent | your repository becomes your agent

[![npm version](https://img.shields.io/npm/v/@shreyaskapale/gitagent)](https://www.npmjs.com/package/@shreyaskapale/gitagent)
[![CI](https://github.com/open-gitagent/gitagent/actions/workflows/ci.yml/badge.svg)](https://github.com/open-gitagent/gitagent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Spec: v0.1.0](https://img.shields.io/badge/spec-v0.1.0-blue)](https://github.com/open-gitagent/gitagent/blob/main/spec/SPECIFICATION.md)
[![Node >= 18](https://img.shields.io/badge/node-%3E%3D18-brightgreen)](https://nodejs.org)

A framework-agnostic, git-native standard for defining AI agents. Clone a repo, get an agent.

## Why

Every AI framework has its own structure. There's no universal, portable way to define an agent that works across Claude Code, OpenAI, LangChain, CrewAI, and AutoGen. **gitagent** fixes that.

- **Git-native** — Version control, branching, diffing, and collaboration built in
- **Framework-agnostic** — Export to any framework with adapters
- **Compliance-ready** — First-class support for FINRA, Federal Reserve, SEC, and segregation of duties
- **Composable** — Agents can extend, depend on, and delegate to other agents

## The Standard

Your repository becomes your agent. Drop these files into any git repo and it becomes a portable, framework-agnostic agent definition — everything else (CLI, adapters, patterns) builds on top of it.

```
my-agent/
│
│   # ── Core Identity (required) ──────────────────────────
├── agent.yaml              # Manifest — name, version, model, skills, tools, compliance
├── SOUL.md                 # Identity, personality, communication style, values
│
│   # ── Behavior & Rules ──────────────────────────────────
├── RULES.md                # Hard constraints, must-always/must-never, safety boundaries
├── DUTIES.md               # Segregation of duties policy and role boundaries
├── AGENTS.md               # Framework-agnostic fallback instructions
│
│   # ── Capabilities ──────────────────────────────────────
├── skills/                 # Reusable capability modules (SKILL.md + scripts)
│   └── code-review/
│       ├── SKILL.md
│       └── review.sh
├── tools/                  # MCP-compatible tool definitions (YAML schemas)
├── workflows/              # Multi-step procedures/playbooks
│
│   # ── Knowledge & Memory ────────────────────────────────
├── knowledge/              # Reference documents the agent can consult
├── memory/                 # Persistent cross-session memory
│   └── runtime/            # Live agent state (dailylog.md, context.md)
│
│   # ── Lifecycle & Ops ───────────────────────────────────
├── hooks/                  # Lifecycle event handlers (bootstrap.md, teardown.md)
├── config/                 # Environment-specific overrides
├── compliance/             # Regulatory compliance artifacts
│
│   # ── Composition ───────────────────────────────────────
├── agents/                 # Sub-agent definitions (recursive structure)
│   └── fact-checker/
│       ├── agent.yaml
│       ├── SOUL.md
│       └── DUTIES.md       # This agent's role, permissions, boundaries
├── examples/               # Calibration interactions (few-shot)
│
│   # ── Runtime ───────────────────────────────────────────
└── .gitagent/              # Runtime state (gitignored)
```

Only two files are required: **`agent.yaml`** (the manifest) and **`SOUL.md`** (the identity). Everything else is optional — add what you need, ignore the rest.

## Patterns

These are the architectural patterns that emerge when you define agents as git-native file systems.

### Human-in-the-Loop for RL Agents
When an agent learns a new skill or writes to memory, it opens a branch + PR for human review before merging.

<img src="patterns/human-in-the-loop.png" alt="Human-in-the-Loop" width="600" />

### Segregation of Duties (SOD)
No single agent should control a critical process end-to-end. Define roles (`maker`, `checker`, `executor`, `auditor`), a conflict matrix (which roles can't be the same agent), and handoff workflows — all in `agent.yaml` + `DUTIES.md`. The validator catches violations before deployment.

```yaml
compliance:
  segregation_of_duties:
    roles:
      - id: maker
        description: Creates proposals
        permissions: [create, submit]
      - id: checker
        description: Reviews and approves
        permissions: [review, approve, reject]
    conflicts:
      - [maker, checker]         # maker cannot approve own work
    assignments:
      loan-originator: [maker]
      credit-reviewer: [checker]
    handoffs:
      - action: credit_decision
        required_roles: [maker, checker]
        approval_required: true
    enforcement: strict
```

### Live Agent Memory
The `memory/` folder holds a `runtime/` subfolder where agents write live knowledge — `dailylog.md`, `key-decisions.md`, and `context.md` — persisting state across sessions.

<img src="patterns/live-agent-memory.png" alt="Live Agent Memory" width="600" />

### Agent Versioning
Every change to your agent is a git commit. Roll back broken prompts, revert bad skills, and explore past versions — full undo history for your agent.

<img src="patterns/agent-versioning.png" alt="Agent Versioning" width="600" />

### Shared Context & Skills via Monorepo
Root-level `context.md`, `skills/`, `tools/` are automatically shared across every agent in the monorepo. No duplication, one source of truth.

<img src="patterns/shared-context.png" alt="Shared Context" width="600" />

### Branch-based Deployment
Use git branches (`dev` → `staging` → `main`) to promote agent changes through environments, just like shipping software.

<img src="patterns/branch-deployment.png" alt="Branch-based Deployment" width="600" />

### Knowledge Tree
The `knowledge/` folder stores entity relationships as a hierarchical tree with embeddings, letting agents reason over structured data at runtime.

<img src="patterns/knowledge-tree.png" alt="Knowledge Tree" width="600" />

### Agent Forking & Remixing
Fork any public agent repo, customize its `SOUL.md`, add your own skills, and PR improvements back upstream — open-source collaboration for AI agents.

<img src="patterns/agent-forking.png" alt="Agent Forking & Remixing" width="600" />

### CI/CD for Agents
Run `gitagent validate` on every push via GitHub Actions. Test agent behavior in CI, block bad merges, and auto-deploy — treat agent quality like code quality.

<img src="patterns/ci-cd-agents.png" alt="CI/CD for Agents" width="600" />

### Agent Diff & Audit Trail
`git diff` shows exactly what changed between agent versions. `git blame` traces every line to who wrote it and when — full traceability out of the box.

<img src="patterns/agent-diff-audit.png" alt="Agent Diff & Audit Trail" width="600" />

### Tagged Releases
Tag stable agent versions like `v1.1.0`. Pin production to a tag, canary new versions on staging, and roll back instantly if something breaks.

<img src="patterns/tagged-releases.png" alt="Tagged Releases" width="600" />

### Secret Management via .gitignore
Agent tools that need API keys read from a local `.env` file — kept out of version control via `.gitignore`. Agent config is shareable, secrets stay local.

<img src="patterns/secret-management.png" alt="Secret Management" width="600" />

### Agent Lifecycle with Hooks
Define `bootstrap.md` and `teardown.md` in the `hooks/` folder to control what an agent does on startup and before it stops.

<img src="patterns/agent-automation-hooks.png" alt="Agent Lifecycle Hooks" width="600" />

### SkillsFlow
Deterministic, multi-step workflows defined in `workflows/` as YAML. Chain `skill:`, `agent:`, and `tool:` steps with `depends_on` ordering, `${{ }}` template data flow, and per-step `prompt:` overrides. Every run follows the same path — no LLM discretion on execution order.

```yaml
name: code-review-flow
description: Full code review pipeline
triggers:
  - pull_request

steps:
  lint:
    skill: static-analysis
    inputs:
      path: ${{ trigger.changed_files }}

  review:
    agent: code-reviewer
    depends_on: [lint]
    prompt: |
      Focus on security and performance.
      Flag any use of eval() or raw SQL.
    inputs:
      findings: ${{ steps.lint.outputs.issues }}

  test:
    tool: bash
    depends_on: [lint]
    inputs:
      command: "npm test -- --coverage"

  report:
    skill: review-summary
    depends_on: [review, test]
    conditions:
      - ${{ steps.review.outputs.severity != 'none' }}
    inputs:
      review: ${{ steps.review.outputs.comments }}
      coverage: ${{ steps.test.outputs.report }}

error_handling:
  on_failure: notify
  channel: "#eng-reviews"
```

### Porting Framework Agents to GitAgent

Agents built in frameworks like NVIDIA AIQ, LangGraph, or CrewAI have their identity split across config files, Jinja2 templates, and Python code. gitagent extracts the **identity layer** — prompts, rules, roles, tool schemas — into a portable, versionable format.

> **What ports cleanly:** system prompts, persona definitions, hard constraints, tool schemas, role/SOD policies, model preferences.
>
> **What stays in the framework:** runtime orchestration (state machines, graph wiring), live tool execution, memory I/O, iterative loops.

This pattern is demonstrated with [NVIDIA's AIQ Deep Researcher](https://github.com/NVIDIA-AI-Blueprints/aiq) — a 3-agent hierarchy (orchestrator → planner → researcher) that produces cited research reports. The gitagent version captures the agent's identity, rules, and SOD policy so you can:

- **Fork for a new domain** — edit `SOUL.md` for legal/medical/finance research without touching Python
- **Version prompts independently** — `git diff` when the orchestrator's style regresses
- **Validate SOD** — `gitagent validate --compliance` ensures the orchestrator can't also be the researcher
- **Export to other runtimes** — same identity on Claude Code, OpenAI, or as a raw system prompt

```
examples/nvidia-deep-researcher/
├── agent.yaml                  # Manifest + SOD policy
├── SOUL.md                     # Orchestrator identity (from orchestrator.j2)
├── RULES.md                    # Citation rules, report constraints
├── DUTIES.md                   # Role separation: orchestrator ↔ planner ↔ researcher
├── agents/planner/             # Planner sub-agent (from planner.j2)
├── agents/researcher/          # Researcher sub-agent (from researcher.j2)
├── skills/{web,paper,knowledge}-search/
├── tools/*.yaml                # MCP-compatible tool schemas
└── config/                     # Model assignments per environment
```

See [`examples/nvidia-deep-researcher/`](examples/nvidia-deep-researcher/) for the full working example.

## Quick Start

```bash
# Install
npm install -g gitagent

# Create a new agent
gitagent init --template standard

# Validate
gitagent validate

# View agent info
gitagent info

# Export to system prompt
gitagent export --format system-prompt
```

## agent.yaml

The only file with a strict schema. Minimal example:

```yaml
spec_version: "0.1.0"
name: my-agent
version: 0.1.0
description: A helpful assistant agent
```

Full example with compliance:

```yaml
spec_version: "0.1.0"
name: compliance-analyst
version: 1.0.0
description: Financial compliance analysis agent
model:
  preferred: claude-opus-4-6
compliance:
  risk_tier: high
  frameworks: [finra, federal_reserve, sec]
  supervision:
    human_in_the_loop: always
    kill_switch: true
  recordkeeping:
    audit_logging: true
    retention_period: 7y
    immutable: true
  model_risk:
    validation_cadence: quarterly
    ongoing_monitoring: true
  segregation_of_duties:
    roles:
      - id: analyst
        permissions: [create, submit]
      - id: reviewer
        permissions: [review, approve, reject]
    conflicts:
      - [analyst, reviewer]
    assignments:
      compliance-analyst: [analyst]
      fact-checker: [reviewer]
    enforcement: strict
```

## CLI Commands

| Command | Description |
|---------|-------------|
| `gitagent init [--template]` | Scaffold new agent (`minimal`, `standard`, `full`) |
| `gitagent validate [--compliance]` | Validate against spec and regulatory requirements |
| `gitagent info` | Display agent summary |
| `gitagent export --format <fmt>` | Export to other formats (see adapters below) |
| `gitagent import --from <fmt> <path>` | Import (`claude`, `cursor`, `crewai`, `opencode`) |
| `gitagent run <source> --adapter <a>` | Run an agent from a git repo or local directory |
| `gitagent install` | Resolve and install git-based dependencies |
| `gitagent audit` | Generate compliance audit report |
| `gitagent skills <cmd>` | Manage skills (`search`, `install`, `list`, `info`) |
| `gitagent lyzr <cmd>` | Manage Lyzr agents (`create`, `update`, `info`, `run`) |

## Compliance

gitagent has first-class support for financial regulatory compliance:

### FINRA
- **Rule 3110** — Supervision: human-in-the-loop, escalation triggers, kill switch
- **Rule 4511** — Recordkeeping: immutable audit logs, retention periods, SEC 17a-4 compliance
- **Rule 2210** — Communications: fair/balanced enforcement, no misleading statements
- **Reg Notice 24-09** — Existing rules apply to GenAI/LLMs

### Federal Reserve
- **SR 11-7** — Model Risk Management: validation cadence, ongoing monitoring, outcomes analysis
- **SR 23-4** — Third-Party Risk: vendor due diligence, SOC reports, subcontractor assessment

### SEC / CFPB
- **Reg S-P** — Customer privacy, PII handling
- **CFPB Circular 2022-03** — Explainable adverse action, Less Discriminatory Alternative search

### Segregation of Duties
- **Roles & Permissions** — Define maker, checker, executor, auditor roles with controlled permissions
- **Conflict Matrix** — Declare which role pairs cannot be held by the same agent
- **Handoff Workflows** — Require multi-agent participation for critical actions (credit decisions, regulatory filings)
- **Isolation** — Full state and credential segregation between roles
- **DUTIES.md** — Root-level policy + per-agent role declarations
- **Enforcement** — Strict (blocks deployment) or advisory (warnings only)

Inspired by [Salient AI](https://www.trysalient.com/)'s purpose-built agent architecture and the [FINOS AI Governance Framework](https://air-governance-framework.finos.org/mitigations/mi-22_multi-agent-isolation-and-segmentation.html).

Run `gitagent audit` for a full compliance checklist against your agent configuration.

## Adapters

Adapters are used by both `export` and `run`. Available adapters:

| Adapter | Description |
|---------|-------------|
| `system-prompt` | Concatenated system prompt (works with any LLM) |
| `claude-code` | Claude Code compatible CLAUDE.md |
| `openai` | OpenAI Agents SDK Python code |
| `crewai` | CrewAI YAML configuration |
| `lyzr` | Lyzr Studio agent |
| `g
... [TRUNCATED]
```

### File: CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

This project follows the [Contributor Covenant v2.1](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).

By participating in this project, you agree to abide by its terms.

## Reporting

If you experience or witness unacceptable behavior, please report it by contacting the project maintainers at **shreyas@lyzr.ai**.

Reports will be reviewed and investigated promptly and fairly. All reporters will be treated with respect and confidentiality.

## Enforcement

Project maintainers are responsible for clarifying and enforcing standards of acceptable behavior and will take appropriate and fair corrective action in response to any behavior that they deem inappropriate.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant](https://www.contributor-covenant.org), version 2.1.

```

### File: CONTRIBUTING.md
```md
# Contributing to gitagent

Thanks for your interest in contributing! gitagent is an early-stage project (v0.1.x), which means the spec, CLI, and adapters are still evolving. That also means your contributions can have an outsized impact on the direction of the project.

Because things move fast, some contributions may need to be reworked as the design evolves — we'll always communicate why and work with you on it.

## Where contributions matter most

**High impact:**
- **Adapter fidelity** — Most exports are lossy today. If you use CrewAI, OpenAI SDK, LangGraph, or any supported framework day-to-day, you're better positioned than anyone to improve that adapter.
- **Bug reports with reproduction steps** — A good bug report includes: the command you ran, the full error output, your OS, Node version, and gitagent version.
- **Compliance review** — The compliance schema was designed by engineers and would benefit greatly from review by folks who work in regulated industries (FINRA, SEC, Fed, CFPB).

**Also welcome:**
- New adapters (LangGraph, LangChain, Autogen, Semantic Kernel)
- Better `import` fidelity from existing frameworks
- Test coverage (we're light on tests — help is very welcome here)

**A few guidelines to keep things smooth:**
- For new features, please open an issue first so we can discuss the approach together.
- We prefer focused PRs over large refactors — it makes review easier for everyone.
- If the code is already working and clear, it probably doesn't need additional comments or formatting changes.

## Setup

```bash
git clone https://github.com/open-gitagent/gitagent.git
cd gitagent
npm install
npm run build
```

This compiles TypeScript from `src/` into `dist/`. The entry point is `src/index.ts`.

To test your local build:

```bash
node dist/index.js <command>
# or link it globally:
npm link
gitagent <command>
```

### Watch mode

```bash
npm run dev
```

Recompiles on file changes. You still need to re-run the command manually.

## Project structure

```
src/
├── index.ts              # CLI entry point (Commander.js)
├── commands/             # One file per CLI command
│   ├── run.ts            # gitagent run
│   ├── init.ts           # gitagent init
│   ├── validate.ts       # gitagent validate
│   ├── export.ts         # gitagent export
│   ├── import.ts         # gitagent import
│   ├── audit.ts          # gitagent audit
│   ├── skills.ts         # gitagent skills
│   ├── install.ts        # gitagent install
│   ├── info.ts           # gitagent info
│   └── lyzr.ts           # gitagent lyzr
├── runners/              # Runtime adapters (execute agents)
│   ├── claude.ts         # Claude Code runner
│   ├── openai.ts         # OpenAI Agents SDK runner
│   ├── crewai.ts         # CrewAI runner
│   ├── lyzr.ts           # Lyzr Studio runner
│   ├── openclaw.ts       # OpenClaw runner
│   ├── nanobot.ts        # Nanobot runner
│   ├── github.ts         # GitHub Models runner
│   └── git.ts            # Auto-detect meta-runner
├── adapters/             # Export adapters (generate config)
├── templates/            # Scaffolding templates for `init`
└── utils/
    ├── loader.ts         # Loads agent.yaml + SOUL.md + skills
    ├── schemas.ts        # JSON Schema definitions
    ├── git-cache.ts      # Clone/cache logic
    ├── skill-discovery.ts
    ├── skill-loader.ts
    ├── auth-provision.ts
    ├── format.ts
    └── registry-provider.ts
```

### How it fits together

1. `commands/run.ts` parses flags, calls `git-cache.ts` to clone the repo, calls `loader.ts` to read the agent, then delegates to a runner in `runners/`.
2. Each runner in `runners/` takes the loaded agent and translates it to framework-specific CLI args or code, then spawns the process.
3. `commands/export.ts` does the same loading but writes output files instead of executing.

## Writing a new adapter

This is the most useful contribution you can make. Here's how:

### 1. Create the runner

Add `src/runners/yourframework.ts`:

```typescript
import { spawnSync } from 'child_process';

export async function runYourFramework(options: {
  dir: string;
  prompt?: string;
  agentConfig: any;
  systemPrompt: string;
}) {
  const { dir, prompt, agentConfig, systemPrompt } = options;

  // Transform gitagent config into your framework's format.
  // Be honest about what you can and can't map.

  // Spawn your framework's CLI or generate code.
  const result = spawnSync('your-cli', args, {
    cwd: dir,
    stdio: 'inherit',
  });

  return result;
}
```

### 2. Register it in `commands/run.ts`

Add your adapter to the switch statement that dispatches on `-a <adapter>`.

### 3. Add export support (optional)

If your framework has a config file format, add an exporter in `commands/export.ts` or `src/adapters/`.

### 4. Document what's lossy

Every adapter loses something — that's expected. Please document it clearly:
- What gitagent fields map to your framework?
- What gets dropped?
- What requires manual setup (API keys, extra dependencies)?

This honesty helps users make informed decisions about which adapter to use.

## Modifying the spec

Changes to the agent standard (repository layout, `agent.yaml` schema, new file conventions) have a wider blast radius than code changes — they affect every adapter, every existing agent, and every user.

**Process:**
1. Open an issue describing the problem the change solves.
2. Show a concrete example of an agent that hits the limitation.
3. Propose the minimal change that fixes it.
4. Let's discuss before jumping to code.

This isn't gatekeeping — it's just making sure spec changes are well-considered since they're hard to undo.

## Pull request process

1. **Fork and branch.** Branch from `main`. Name branches descriptively: `fix/npx-binary-resolution`, `adapter/langgraph`, `spec/memory-schema`.

2. **Keep it focused.** One logical change per PR. If your PR covers multiple things (e.g., new adapter + loader refactor + README update), we may ask you to split it — just to make review manageable.

3. **Build must pass.**
   ```bash
   npm run build
   ```
   If it doesn't compile, don't open the PR.

4. **Test manually.** There's no test suite worth mentioning. Run your change against a real agent. Include the command you ran and the output in the PR description.

5. **Write a clear PR description.** What does it do? Why? What did you test? What's lossy or incomplete?

6. **Don't bump the version.** Maintainers handle versioning and npm publishing.

## Commit messages

Use conventional commits:

```
fix: resolve npx binary shadowing for claude runner
feat: add langgraph export adapter
docs: update adapter table in README
chore: bump dependencies
```

First line under 72 characters. Body if needed. Don't overthink it.

## Code style

- TypeScript, strict mode.
- Keep it simple — prefer straightforward code over clever abstractions. Three similar lines is often better than a premature helper function.
- This is a CLI tool, so we keep the architecture flat. No ORMs, no DI frameworks, no deep class hierarchies.
- If you need a new dependency, mention it in the PR — we try to keep the dependency tree small for supply chain safety.
- Error messages should help the user fix the problem. "Failed to load agent.yaml: file not found at /path" is great. A bare "Error" isn't helpful.

## What happens after you submit

- **Small fixes** (typos, clear bugs): merged quickly.
- **New adapters**: reviewed for correctness, merged after manual testing.
- **Spec changes**: discussed thoroughly — may be deferred to a future version if the timing isn't right.
- **Large refactors**: best to discuss in an issue first so we can align on approach.

Response time varies — this is a small team. If your PR sits for a bit, feel free to ping. We appreciate your patience and want to give every contribution proper attention.

## Reporting security issues

Please don't open a public issue for security vulnerabilities. Email shreyas@lyzr.ai directly and we'll work with you to address it.

## License

By contributing, you agree your contributions are licensed under MIT, same as the project.

## Thank you

Every contribution — whether it's a bug report, a typo fix, or a new adapter — helps make gitagent better. We're grateful you're here.

```

### File: docs.md
```md
# gitagent Documentation

A framework-agnostic, git-native standard for defining AI agents.

**Clone a repo, get an agent.**

---

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Core Concepts](#core-concepts)
- [Directory Structure](#directory-structure)
- [Agent Manifest (agent.yaml)](#agent-manifest)
- [CLI Commands](#cli-commands)
  - [init](#init)
  - [validate](#validate)
  - [info](#info)
  - [export](#export)
  - [import](#import)
  - [install](#install)
  - [audit](#audit)
  - [skills](#skills)
  - [run](#run)
  - [lyzr](#lyzr)
- [Export Formats](#export-formats)
- [Adapters & Runners](#adapters--runners)
  - [Claude](#claude-runner)
  - [OpenAI](#openai-runner)
  - [CrewAI](#crewai-runner)
  - [OpenClaw](#openclaw-runner)
  - [Nanobot](#nanobot-runner)
  - [Lyzr](#lyzr-runner)
  - [GitHub Models](#github-models-runner)
  - [Git (Auto-Detect)](#git-runner-auto-detect)
- [Skills System](#skills-system)
- [Compliance](#compliance)
- [Inheritance & Composition](#inheritance--composition)
- [Git Caching](#git-caching)
- [Authentication](#authentication)
- [Environment Variables](#environment-variables)
- [Examples](#examples)
- [JSON Schemas](#json-schemas)

---

## Installation

```bash
npm install -g gitagent
```

Verify:

```bash
gitagent --version   # 0.1.0
gitagent --help
```

---

## Quick Start

```bash
# Create a new agent
gitagent init --template standard --dir ./my-agent

# Validate it
gitagent validate -d ./my-agent

# Run it locally with Claude Code
gitagent run -d ./my-agent

# Run from a git repo
gitagent run -r https://github.com/user/my-agent -p "Hello"

# Run with a different adapter
gitagent run -d ./my-agent -a github -p "Summarize this project"

# Clone + auto-detect best adapter + run
gitagent run -r https://github.com/user/my-agent -a git -p "Hello"

# Deploy to Lyzr Studio and chat
gitagent lyzr run -r https://github.com/user/my-agent -p "Hello"

# Export to another framework
gitagent export -f openai -d ./my-agent -o agent.py
```

---

## Core Concepts

**Git-native** — Every agent is a git repo. Version control, branching, diffing, PRs, and collaboration come free.

**Framework-agnostic** — Define your agent once, export to Claude Code, OpenAI, CrewAI, OpenClaw, Nanobot, Lyzr, or GitHub Models with adapters.

**Compliance-ready** — First-class support for FINRA, Federal Reserve, SEC, and CFPB regulatory requirements baked into the manifest.

**Composable** — Agents can extend parent agents, declare dependencies, and delegate to sub-agents.

---

## Directory Structure

```
my-agent/
├── agent.yaml          # [REQUIRED] Manifest — name, version, model, skills, tools, compliance
├── SOUL.md             # [REQUIRED] Identity, personality, communication style, values
├── RULES.md            # Hard constraints, must-always/must-never, safety boundaries
├── PROMPT.md           # Default task framing and output format
├── AGENTS.md           # Framework-agnostic fallback instructions
├── skills/             # Reusable capability modules (SKILL.md + scripts)
│   └── my-skill/
│       ├── SKILL.md    # Frontmatter + instructions
│       ├── scripts/    # Executable scripts
│       ├── references/ # Reference documents
│       └── assets/     # Static assets
├── tools/              # MCP-compatible tool definitions (YAML schemas)
│   └── my-tool.yaml
├── knowledge/          # Reference documents the agent can consult
│   ├── index.yaml      # Document index with always_load flags
│   └── docs/
├── memory/             # Persistent cross-session memory
│   ├── MEMORY.md       # Working memory (max 200 lines)
│   └── memory.yaml     # Memory configuration
├── workflows/          # Multi-step procedures/playbooks
├── hooks/              # Lifecycle event handlers
│   ├── hooks.yaml      # Hook definitions
│   └── scripts/        # Hook scripts
├── examples/           # Calibration interactions (few-shot)
├── agents/             # Sub-agent definitions (recursive structure)
│   └── sub-agent/
│       ├── agent.yaml
│       └── SOUL.md
├── compliance/         # Regulatory compliance artifacts
│   ├── risk-assessment.md
│   ├── regulatory-map.yaml
│   └── validation-schedule.yaml
├── config/             # Environment-specific overrides
│   └── default.yaml
├── .gitagent_adapter   # Optional: hint for git runner auto-detection (e.g. "lyzr", "github")
├── .lyzr_agent_id      # Auto-generated: Lyzr Studio agent ID (after lyzr create)
├── .github_models      # Optional: hint for git runner to use GitHub Models adapter
└── .gitagent/          # Runtime state (gitignored)
```

Only `agent.yaml` and `SOUL.md` are required. Everything else is optional.

---

## Agent Manifest

`agent.yaml` is the only file with a strict schema. It defines the agent's identity, model preferences, capabilities, and compliance configuration.

### Minimal

```yaml
spec_version: "0.1.0"
name: my-agent
version: 0.1.0
description: A helpful assistant agent
```

### Standard

```yaml
spec_version: "0.1.0"
name: code-review-agent
version: 1.0.0
description: Automated code review agent with best-practice enforcement
author: gitagent-examples
license: MIT

model:
  preferred: claude-sonnet-4-5-20250929
  fallback:
    - claude-haiku-4-5-20251001
  constraints:
    temperature: 0.2
    max_tokens: 4096

skills:
  - code-review

tools:
  - lint-check
  - complexity-analysis

runtime:
  max_turns: 20
  timeout: 120

tags:
  - code-review
  - developer-tools
```

### Full (with Compliance)

```yaml
spec_version: "0.1.0"
name: compliance-analyst
version: 1.0.0
description: Financial compliance analysis agent
author: Acme Corp
license: MIT

model:
  preferred: claude-opus-4-6
  fallback:
    - claude-sonnet-4-5-20250929
  constraints:
    temperature: 0.2
    max_tokens: 4096
    top_p: 0.9

skills:
  - code-review
  - security-audit

tools:
  - search-codebase
  - run-tests

agents:
  fact-checker:
    description: Verifies factual claims
    delegation:
      mode: auto
      triggers:
        - "verify this claim"

delegation:
  mode: auto
  router: semantic

runtime:
  max_turns: 50
  temperature: 0.3
  timeout: 300

a2a:
  url: https://api.example.com/agent
  capabilities:
    - code-review
    - compliance-check
  authentication:
    type: bearer
    required: true
  protocols:
    - a2a-v1

extends: https://github.com/org/base-agent.git

dependencies:
  - name: fact-checker
    source: https://github.com/org/fact-checker.git
    version: ^1.0.0
    mount: agents/fact-checker
    vendor_management:
      due_diligence_date: "2024-01-15"
      soc_report: true
      risk_assessment: low

compliance:
  risk_tier: high
  frameworks:
    - finra
    - federal_reserve
    - sec
  supervision:
    designated_supervisor: John Smith
    review_cadence: weekly
    human_in_the_loop: always
    escalation_triggers:
      - condition: pii_detected
        action: halt_and_escalate
    override_capability: true
    kill_switch: true
  recordkeeping:
    audit_logging: true
    log_format: structured_json
    retention_period: 7y
    log_contents:
      - prompts_and_responses
      - tool_calls
      - decision_pathways
      - model_version
      - timestamps
    immutable: true
  model_risk:
    inventory_id: MRM-2024-001
    validation_cadence: quarterly
    validation_type: full
    ongoing_monitoring: true
    outcomes_analysis: true
    drift_detection: true
  data_governance:
    pii_handling: redact
    data_classification: confidential
    consent_required: true
    cross_border: false
    bias_testing: true
  communications:
    type: correspondence
    pre_review_required: true
    fair_balanced: true
    no_misleading: true
    disclosures_required: true
  vendor_management:
    due_diligence_complete: true
    soc_report_required: true
    vendor_ai_notification: true
    subcontractor_assessment: true

tags:
  - finance
  - compliance
metadata:
  team: platform
```

---

## CLI Commands

### init

Scaffold a new agent repository.

```bash
gitagent init [options]
```

| Option | Default | Description |
|--------|---------|-------------|
| `-t, --template <name>` | `standard` | Template: `minimal`, `standard`, or `full` |
| `-d, --dir <dir>` | `.` | Target directory |

**Templates:**

| Template | Files Created |
|----------|---------------|
| `minimal` | `agent.yaml`, `SOUL.md` |
| `standard` | `agent.yaml`, `SOUL.md`, `RULES.md`, `AGENTS.md`, `skills/`, `knowledge/`, `tools/` |
| `full` | Everything in standard + `memory/`, `hooks/`, `examples/`, `agents/`, `compliance/`, `config/`, `.gitignore` |

```bash
gitagent init --template minimal
gitagent init --template full --dir ./my-agent
```

---

### validate

Validate an agent against the specification and optionally check regulatory compliance.

```bash
gitagent validate [options]
```

| Option | Default | Description |
|--------|---------|-------------|
| `-d, --dir <dir>` | `.` | Agent directory |
| `-c, --compliance` | `false` | Include regulatory compliance validation |

**What gets validated:**

- **agent.yaml** — JSON schema validation, referenced skills/tools/agents exist
- **SOUL.md** — Exists, not empty, has real content
- **Skills** — Valid frontmatter, name matches directory, description length, instruction size
- **Hooks** — Valid YAML, referenced scripts exist
- **Tools** — Valid YAML schema

**With `--compliance`:**

- Risk tier required when compliance section exists
- High/critical tiers require human-in-the-loop and audit logging
- FINRA: fair_balanced and no_misleading enforcement
- Federal Reserve: model_risk section with ongoing_monitoring
- SEC: audit logging, PII handling checks
- CFPB: bias testing recommendation
- Compliance artifacts directory check
- Vendor management metadata for dependencies

```bash
gitagent validate
gitagent validate --compliance
gitagent validate -d ./examples/full --compliance
```

---

### info

Display a formatted summary of the agent configuration.

```bash
gitagent info [options]
```

| Option | Default | Description |
|--------|---------|-------------|
| `-d, --dir <dir>` | `.` | Agent directory |

Shows: name, version, description, author, license, model preferences, skills, tools, sub-agents, runtime config, compliance settings, tags, and a SOUL.md preview.

```bash
gitagent info
gitagent info -d ./examples/standard
```

---

### export

Export an agent to another framework's format.

```bash
gitagent export [options]
```

| Option | Default | Description |
|--------|---------|-------------|
| `-f, --format <format>` | *(required)* | Export format (see table below) |
| `-d, --dir <dir>` | `.` | Agent directory |
| `-o, --output <path>` | stdout | Output file path |

**Supported formats:**

| Format | Output | Description |
|--------|--------|-------------|
| `system-prompt` | Markdown | Concatenated system prompt for any LLM |
| `claude-code` | Markdown | Claude Code `CLAUDE.md` file |
| `openai` | Python | OpenAI Agents SDK code with tool definitions |
| `crewai` | YAML | CrewAI crew configuration |
| `openclaw` | JSON + Markdown | OpenClaw workspace (config + AGENTS.md + skills) |
| `nanobot` | JSON + Markdown | Nanobot config.json + system prompt |
| `lyzr` | JSON | Lyzr Studio API payload (agent creation) |
| `github` | JSON | GitHub Models API chat completions payload |

```bash
# Print system prompt to terminal
gitagent export --format system-prompt

# Save Claude Code format to file
gitagent export --format claude-code --output CLAUDE.md

# Generate OpenAI Python code
gitagent export --format openai --output agent.py

# Preview Lyzr API payload
gitagent export --format lyzr -d ./examples/lyzr-agent

# Preview GitHub Models payload
gitagent export --format github -d ./examples/standard

# Export CrewAI config
gitagent export --format crewai -d ./examples/standard
```

---

### import

Import from another agent framework into gitagent format.

```bash
gitagent import --from <format> <path> [options]
```

| Option | Default | Description |
|--------|---------|-------------|
| `--from <format>` | *(required)* | Source format: `claude`, `cursor`, `crewai` |
| `<path>` | *(required)* | Source file or directory |
| `-d, --dir <dir>` | `.` | Target directory |

**Import sources:**

| Source | What it reads | What it creates |
|--------|---------------|-----------------|
| `claude` | `CLAUDE.md`, `.claude/skills/` | `agent.yaml`, `SOUL.md`, `RULES.md`, imported skills |
| `cursor` | `.cursorrules` or `AGENTS.md` | `agent.yaml`, `SOUL.md`, `AGENTS.md` |
| `crewai` | CrewAI YAML config | `agent.yaml`, `SOUL.md`, sub-agents in `agents/` |

```bash
gitagent import --from claude ./my-claude-project
gitagent import --from cursor ./.cursorrules
gitagent import --from crewai ./crew.yaml --dir ./imported-agent
```

---

### install

Resolve and install git-based agent dependencies declared in `agent.yaml`.

```bash
gitagent install [options]
```

| Option | Default | Description |
|--------|---------|-------------|
| `-d, --dir <dir>` | `.` | Agent directory |

For each entry in `dependencies`:
- Local paths are copied
- Git URLs are shallow-cloned at the specified version/branch
- Target directory is `mount` path or `.gitagent/deps/<name>`
- Validates that installed dependencies contain `agent.yaml`

```bash
gitagent install
gitagent install -d ./my-agent
```

---

### audit

Generate a comprehensive compliance audit report.

```bash
gitagent audit [options]
```

| Option | Default | Description |
|--------|---------|-------------|
| `-d, --dir <dir>` | `.` | Agent directory |

**Report sections:**

1. **Risk Classification** — Risk tier and applicable frameworks
2. **Supervision (FINRA Rule 3110)** — Supervisor assignment, review cadence, human-in-the-loop, escalation triggers, override capability, kill switch
3. **Recordkeeping (FINRA 4511 / SEC 17a-4)** — Audit logging, log format, retention period, log contents, immutability
4. **Model Risk Management (SR 11-7)** — Inventory ID, validation cadence, ongoing monitoring, outcomes analysis, drift detection
5. **Data Governance (Reg S-P, CFPB)** — PII handling, data classification, consent, cross-border, bias testing
6. **Communications Compliance (FINRA 2210)** — Type classification, fair/balanced, no misleading, pre-review, disclosures
7. **Vendor Management (SR 23-4)** — Due diligence, SOC reports, vendor AI notification, subcontractor assessment
8. **Compliance Artifacts** — Directory and file existence checks
9. **Audit Hooks** — hooks.yaml and compliance-flagged hooks

```bash
gitagent audit
gitagent audit -d ./examples/full
```

---

### skills

Manage agent skills — search registries, install, list, and inspect.

#### skills search

```bash
gitagent skills search <query> [options]
```

| Option | Default | Description |
|--------|---------|-------------|
| `-p, --provider <name>` | `skillsmp` | Registry: `skillsmp` or `github` |
| `-d, --dir <dir>` | `.` | Agent directory |
| `-l, --limit <n>` | `20` | Max results |

#### skills install

```
... [TRUNCATED]
```

### File: hackathon.md
```md
# gitagent Hackathon

## The Challenge

Build an AI agent that lives in a git repo. Define it using the gitagent standard, bring it to life with gitclaw, and optionally deploy it serverlessly with clawless.

## How It Works

### Step 1: Define Your Agent (gitagent format)

Create a git repo with this structure:

```
my-agent/
├── agent.yaml          # Manifest: name, version, description, skills, model
├── SOUL.md             # Who your agent is — personality, values, expertise
├── RULES.md            # What your agent must/must never do
├── skills/
│   └── my-skill/
│       └── SKILL.md    # A capability with YAML frontmatter + instructions
└── tools/              # Optional: tool definitions (YAML schemas)
```

**`agent.yaml`** — the manifest:
```yaml
spec_version: "0.1.0"
name: my-hackathon-agent
version: 0.1.0
description: "What your agent does in one line"
model:
  preferred: claude-sonnet-4-5-20250929
skills:
  - my-skill
tags:
  - hackathon
```

**`SOUL.md`** — your agent's identity:
```markdown
# Soul

## Core Identity
I am a [role]. I specialize in [domain].

## Communication Style
[How your agent talks, thinks, responds]

## Values
- [What matters to your agent]
```

**`RULES.md`** — hard constraints:
```markdown
# Rules

## Must Always
- [Non-negotiable behaviors]

## Must Never
- [Hard boundaries]
```

**`skills/my-skill/SKILL.md`** — a capability:
```markdown
---
name: my-skill
description: "What this skill does"
allowed-tools: Bash Read Write
---

# My Skill

Instructions for how the agent should execute this skill.
```

Validate your agent:
```bash
npx gitagent validate
npx gitagent info
```

### Step 2: Build Your Agent (gitclaw SDK)

Use [gitclaw](https://github.com/open-gitagent/gitclaw) to turn your repo into a running agent:

```bash
npm install gitclaw
```

gitclaw reads your gitagent repo and creates a fully functional AI agent — with the identity from SOUL.md, rules from RULES.md, skills from skills/, and tools from tools/. Your agent definition is the git repo. gitclaw is the runtime.

See the [gitclaw README](https://github.com/open-gitagent/gitclaw) for full SDK docs, examples, and API reference.

### Step 3 (Optional): Deploy Serverlessly (clawless)

Want your agent running in the browser with zero infrastructure? Use [clawless](https://github.com/open-gitagent/clawless) — a serverless runtime powered by WebContainers.

```bash
npm install clawless
```

> **Important:** clawless runs in a WebContainer environment with **Node.js/npm only**. Your agent's skills and tools must be Node-compatible. No Python, no system binaries, no Docker. If your skill runs `node` or `npx`, it works. If it needs `python` or `apt-get`, use gitclaw instead.

See the [clawless README](https://github.com/open-gitagent/clawless) for setup, deployment, and limitations.

## Judging Criteria

| Criteria | Weight | What We're Looking For |
|----------|--------|----------------------|
| **Agent Quality** | 30% | Does the agent do something useful? Is the SOUL.md compelling? Are the rules well-defined? |
| **Skill Design** | 25% | Are skills focused, well-documented, and practical? Do they follow the SKILL.md standard? |
| **Working Demo** | 25% | Does it actually run via gitclaw or clawless? Can we see it in action? |
| **Creativity** | 20% | Surprise us. Novel use cases, clever skill compositions, unexpected domains. |

## Resources

| Resource | Link |
|----------|------|
| gitagent standard | https://github.com/open-gitagent/gitagent |
| gitagent spec | https://github.com/open-gitagent/gitagent/blob/main/spec/SPECIFICATION.md |
| gitclaw SDK | https://github.com/open-gitagent/gitclaw |
| clawless (serverless) | https://github.com/open-gitagent/clawless |
| Example agents | https://github.com/open-gitagent/gitagent/tree/main/examples |
| gitagent CLI docs | Run `npx gitagent --help` |

## Quick Reference: gitagent CLI

```bash
npx gitagent init                    # Scaffold a new agent
npx gitagent validate                # Validate your agent
npx gitagent info                    # Show agent summary
npx gitagent export -f system-prompt # Preview as system prompt
npx gitagent export -f claude-code   # Export for Claude Code
npx gitagent export -f cursor        # Export for Cursor
```

## FAQ

**Q: Do I need to use a specific LLM?**
A: No. gitagent is model-agnostic. Set `model.preferred` in agent.yaml to whatever you want — Claude, GPT, Gemini, Llama, etc. gitclaw handles the runtime.

**Q: Can my agent have multiple skills?**
A: Yes. Add as many as you want under `skills/`. Each gets its own directory with a SKILL.md file.

**Q: Can I use sub-agents?**
A: Yes. Add them under `agents/` — each sub-agent is a full gitagent directory with its own agent.yaml, SOUL.md, etc.

**Q: What if my skill needs Python?**
A: Use gitclaw (not clawless). clawless only supports Node.js/npm environments. gitclaw has no such limitation.

**Q: Can I start from an existing agent config?**
A: Yes. `gitagent import --from claude <path>` or `gitagent import --from cursor <path>` converts existing configs to gitagent format.

---

Build something great. Your agent is a git repo. Make it count.

```

### File: package_lock.json
```json
{
  "name": "gitagent",
  "version": "0.1.7",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "gitagent",
      "version": "0.1.7",
      "license": "MIT",
      "dependencies": {
        "ajv": "^8.17.1",
        "ajv-formats": "^3.0.1",
        "chalk": "^5.3.0",
        "commander": "^12.1.0",
        "inquirer": "^9.3.7",
        "js-yaml": "^4.1.0"
      },
      "bin": {
        "gitagent": "dist/index.js"
      },
      "devDependencies": {
        "@types/inquirer": "^9.0.7",
        "@types/js-yaml": "^4.0.9",
        "@types/node": "^22.10.0",
        "typescript": "^5.7.0"
      }
    },
    "node_modules/@inquirer/external-editor": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/@inquirer/external-editor/-/external-editor-1.0.3.tgz",
      "integrity": "sha512-RWbSrDiYmO4LbejWY7ttpxczuwQyZLBUyygsA9Nsv95hpzUWwnNTVQmAq3xuh7vNwCp07UTmE5i11XAEExx4RA==",
      "license": "MIT",
      "dependencies": {
        "chardet": "^2.1.1",
        "iconv-lite": "^0.7.0"
      },
      "engines": {
        "node": ">=18"
      },
      "peerDependencies": {
        "@types/node": ">=18"
      },
      "peerDependenciesMeta": {
        "@types/node": {
          "optional": true
        }
      }
    },
    "node_modules/@inquirer/figures": {
      "version": "1.0.15",
      "resolved": "https://registry.npmjs.org/@inquirer/figures/-/figures-1.0.15.tgz",
      "integrity": "sha512-t2IEY+unGHOzAaVM5Xx6DEWKeXlDDcNPeDyUpsRc6CUhBfU3VQOEl+Vssh7VNp1dR8MdUJBWhuObjXCsVpjN5g==",
      "license": "MIT",
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@types/inquirer": {
      "version": "9.0.9",
      "resolved": "https://registry.npmjs.org/@types/inquirer/-/inquirer-9.0.9.tgz",
      "integrity": "sha512-/mWx5136gts2Z2e5izdoRCo46lPp5TMs9R15GTSsgg/XnZyxDWVqoVU3R9lWnccKpqwsJLvRoxbCjoJtZB7DSw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/through": "*",
        "rxjs": "^7.2.0"
      }
    },
    "node_modules/@types/js-yaml": {
      "version": "4.0.9",
      "resolved": "https://registry.npmjs.org/@types/js-yaml/-/js-yaml-4.0.9.tgz",
      "integrity": "sha512-k4MGaQl5TGo/iipqb2UDG2UwjXziSWkh0uysQelTlJpX1qGlpUZYm8PnO4DxG1qBomtJUdYJ6qR6xdIah10JLg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@types/node": {
      "version": "22.19.11",
      "resolved": "https://registry.npmjs.org/@types/node/-/node-22.19.11.tgz",
      "integrity": "sha512-BH7YwL6rA93ReqeQS1c4bsPpcfOmJasG+Fkr6Y59q83f9M1WcBRHR2vM+P9eOisYRcN3ujQoiZY8uk5W+1WL8w==",
      "devOptional": true,
      "license": "MIT",
      "dependencies": {
        "undici-types": "~6.21.0"
      }
    },
    "node_modules/@types/through": {
      "version": "0.0.33",
      "resolved": "https://registry.npmjs.org/@types/through/-/through-0.0.33.tgz",
      "integrity": "sha512-HsJ+z3QuETzP3cswwtzt2vEIiHBk/dCcHGhbmG5X3ecnwFD/lPrMpliGXxSCg03L9AhrdwA4Oz/qfspkDW+xGQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/node": "*"
      }
    },
    "node_modules/ajv": {
      "version": "8.18.0",
      "resolved": "https://registry.npmjs.org/ajv/-/ajv-8.18.0.tgz",
      "integrity": "sha512-PlXPeEWMXMZ7sPYOHqmDyCJzcfNrUr3fGNKtezX14ykXOEIvyK81d+qydx89KY5O71FKMPaQ2vBfBFI5NHR63A==",
      "license": "MIT",
      "dependencies": {
        "fast-deep-equal": "^3.1.3",
        "fast-uri": "^3.0.1",
        "json-schema-traverse": "^1.0.0",
        "require-from-string": "^2.0.2"
      },
      "funding": {
        "type": "github",
        "url": "https://github.com/sponsors/epoberezkin"
      }
    },
    "node_modules/ajv-formats": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/ajv-formats/-/ajv-formats-3.0.1.tgz",
      "integrity": "sha512-8iUql50EUR+uUcdRQ3HDqa6EVyo3docL8g5WJ3FNcWmu62IbkGUue/pEyLBW8VGKKucTPgqeks4fIU1DA4yowQ==",
      "license": "MIT",
      "dependencies": {
        "ajv": "^8.0.0"
      },
      "peerDependencies": {
        "ajv": "^8.0.0"
      },
      "peerDependenciesMeta": {
        "ajv": {
          "optional": true
        }
      }
    },
    "node_modules/ansi-escapes": {
      "version": "4.3.2",
      "resolved": "https://registry.npmjs.org/ansi-escapes/-/ansi-escapes-4.3.2.tgz",
      "integrity": "sha512-gKXj5ALrKWQLsYG9jlTRmR/xKluxHV+Z9QEwNIgCfM1/uwPMCuzVVnh5mwTd+OuBZcwSIMbqssNWRm1lE51QaQ==",
      "license": "MIT",
      "dependencies": {
        "type-fest": "^0.21.3"
      },
      "engines": {
        "node": ">=8"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/ansi-regex": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz",
      "integrity": "sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==",
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/ansi-styles": {
      "version": "4.3.0",
      "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-4.3.0.tgz",
      "integrity": "sha512-zbB9rCJAT1rbjiVDb2hqKFHNYLxgtk8NURxZ3IZwD3F6NtxbXZQCnnSi1Lkx+IDohdPlFp222wVALIheZJQSEg==",
      "license": "MIT",
      "dependencies": {
        "color-convert": "^2.0.1"
      },
      "engines": {
        "node": ">=8"
      },
      "funding": {
        "url": "https://github.com/chalk/ansi-styles?sponsor=1"
      }
    },
    "node_modules/argparse": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/argparse/-/argparse-2.0.1.tgz",
      "integrity": "sha512-8+9WqebbFzpX9OR+Wa6O29asIogeRMzcGtAINdpMHHyAg10f05aSFVBbcEqGf/PXw1EjAZ+q2/bEBg3DvurK3Q==",
      "license": "Python-2.0"
    },
    "node_modules/base64-js": {
      "version": "1.5.1",
      "resolved": "https://registry.npmjs.org/base64-js/-/base64-js-1.5.1.tgz",
      "integrity": "sha512-AKpaYlHn8t4SVbOHCy+b5+KKgvR4vrsD8vbvrbiQJps7fKDTkjkDry6ji0rUJjC0kzbNePLwzxq8iypo41qeWA==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT"
    },
    "node_modules/bl": {
      "version": "4.1.0",
      "resolved": "https://registry.npmjs.org/bl/-/bl-4.1.0.tgz",
      "integrity": "sha512-1W07cM9gS6DcLperZfFSj+bWLtaPGSOHWhPiGzXmvVJbRLdG82sH/Kn8EtW1VqWVA54AKf2h5k5BbnIbwF3h6w==",
      "license": "MIT",
      "dependencies": {
        "buffer": "^5.5.0",
        "inherits": "^2.0.4",
        "readable-stream": "^3.4.0"
      }
    },
    "node_modules/buffer": {
      "version": "5.7.1",
      "resolved": "https://registry.npmjs.org/buffer/-/buffer-5.7.1.tgz",
      "integrity": "sha512-EHcyIPBQ4BSGlvjB16k5KgAJ27CIsHY/2JBmCRReo48y9rQ3MaUzWX3KVlBa4U7MyX02HdVj0K7C3WaB3ju7FQ==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "base64-js": "^1.3.1",
        "ieee754": "^1.1.13"
      }
    },
    "node_modules/chalk": {
      "version": "5.6.2",
      "resolved": "https://registry.npmjs.org/chalk/-/chalk-5.6.2.tgz",
      "integrity": "sha512-7NzBL0rN6fMUW+f7A6Io4h40qQlG+xGmtMxfbnH/K7TAtt8JQWVQK+6g0UXKMeVJoyV5EkkNsErQ8pVD3bLHbA==",
      "license": "MIT",
      "engines": {
        "node": "^12.17.0 || ^14.13 || >=16.0.0"
      },
      "funding": {
        "url": "https://github.com/chalk/chalk?sponsor=1"
      }
    },
    "node_modules/chardet": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/chardet/-/chardet-2.1.1.tgz",
      "integrity": "sha512-PsezH1rqdV9VvyNhxxOW32/d75r01NY7TQCmOqomRo15ZSOKbpTFVsfjghxo6JloQUCGnH4k1LGu0R4yCLlWQQ==",
      "license": "MIT"
    },
    "node_modules/cli-cursor": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/cli-cursor/-/cli-cursor-3.1.0.tgz",
      "integrity": "sha512-I/zHAwsKf9FqGoXM4WWRACob9+SNukZTd94DWF57E4toouRulbCxcUh6RKUEOQlYTHJnzkPMySvPNaaSLNfLZw==",
      "license": "MIT",
      "dependencies": {
        "restore-cursor": "^3.1.0"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/cli-spinners": {
      "version": "2.9.2",
      "resolved": "https://registry.npmjs.org/cli-spinners/-/cli-spinners-2.9.2.tgz",
      "integrity": "sha512-ywqV+5MmyL4E7ybXgKys4DugZbX0FC6LnwrhjuykIjnK9k8OQacQ7axGKnjDXWNhns0xot3bZI5h55H8yo9cJg==",
      "license": "MIT",
      "engines": {
        "node": ">=6"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/cli-width": {
      "version": "4.1.0",
      "resolved": "https://registry.npmjs.org/cli-width/-/cli-width-4.1.0.tgz",
      "integrity": "sha512-ouuZd4/dm2Sw5Gmqy6bGyNNNe1qt9RpmxveLSO7KcgsTnU7RXfsw+/bukWGo1abgBiMAic068rclZsO4IWmmxQ==",
      "license": "ISC",
      "engines": {
        "node": ">= 12"
      }
    },
    "node_modules/clone": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/clone/-/clone-1.0.4.tgz",
      "integrity": "sha512-JQHZ2QMW6l3aH/j6xCqQThY/9OH4D/9ls34cgkUBiEeocRTU04tHfKPBsUK1PqZCUQM7GiA0IIXJSuXHI64Kbg==",
      "license": "MIT",
      "engines": {
        "node": ">=0.8"
      }
    },
    "node_modules/color-convert": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/color-convert/-/color-convert-2.0.1.tgz",
      "integrity": "sha512-RRECPsj7iu/xb5oKYcsFHSppFNnsj/52OVTRKb4zP5onXwVF3zVmmToNcOfGC+CRDpfK/U584fMg38ZHCaElKQ==",
      "license": "MIT",
      "dependencies": {
        "color-name": "~1.1.4"
      },
      "engines": {
        "node": ">=7.0.0"
      }
    },
    "node_modules/color-name": {
      "version": "1.1.4",
      "resolved": "https://registry.npmjs.org/color-name/-/color-name-1.1.4.tgz",
      "integrity": "sha512-dOy+3AuW3a2wNbZHIuMZpTcgjGuLU/uBL/ubcZF9OXbDo8ff4O8yVp5Bf0efS8uEoYo5q4Fx7dY9OgQGXgAsQA==",
      "license": "MIT"
    },
    "node_modules/commander": {
      "version": "12.1.0",
      "resolved": "https://registry.npmjs.org/commander/-/commander-12.1.0.tgz",
      "integrity": "sha512-Vw8qHK3bZM9y/P10u3Vib8o/DdkvA2OtPtZvD871QKjy74Wj1WSKFILMPRPSdUSx5RFK1arlJzEtA4PkFgnbuA==",
      "license": "MIT",
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/defaults": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/defaults/-/defaults-1.0.4.tgz",
      "integrity": "sha512-eFuaLoy/Rxalv2kr+lqMlUnrDWV+3j4pljOIJgLIhI058IQfWJ7vXhyEIHu+HtC738klGALYxOKDO0bQP3tg8A==",
      "license": "MIT",
      "dependencies": {
        "clone": "^1.0.2"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/emoji-regex": {
      "version": "8.0.0",
      "resolved": "https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz",
      "integrity": "sha512-MSjYzcWNOA0ewAHpz0MxpYFvwg6yjy1NG3xteoqz644VCo/RPgnr1/GGt+ic3iJTzQ8Eu3TdM14SawnVUmGE6A==",
      "license": "MIT"
    },
    "node_modules/fast-deep-equal": {
      "version": "3.1.3",
      "resolved": "https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-3.1.3.tgz",
      "integrity": "sha512-f3qQ9oQy9j2AhBe/H9VC91wLmKBCCU/gDOnKNAYG5hswO7BLKj09Hc5HYNz9cGI++xlpDCIgDaitVs03ATR84Q==",
      "license": "MIT"
    },
    "node_modules/fast-uri": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/fast-uri/-/fast-uri-3.1.0.tgz",
      "integrity": "sha512-iPeeDKJSWf4IEOasVVrknXpaBV0IApz/gp7S2bb7Z4Lljbl2MGJRqInZiUrQwV16cpzw/D3S5j5Julj/gT52AA==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/fastify"
        },
        {
          "type": "opencollective",
          "url": "https://opencollective.com/fastify"
        }
      ],
      "license": "BSD-3-Clause"
    },
    "node_modules/has-flag": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/has-flag/-/has-flag-4.0.0.tgz",
      "integrity": "sha512-EykJT/Q1KjTWctppgIAgfSO0tKVuZUjhgMr17kqTumMl6Afv3EISleU7qZUzoXDFTAHTDC4NOoG/ZxU3EvlMPQ==",
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/iconv-lite": {
      "version": "0.7.2",
      "resolved": "https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.7.2.tgz",
      "integrity": "sha512-im9DjEDQ55s9fL4EYzOAv0yMqmMBSZp6G0VvFyTMPKWxiSBHUj9NW/qqLmXUwXrrM7AvqSlTCfvqRb0cM8yYqw==",
      "license": "MIT",
      "dependencies": {
        "safer-buffer": ">= 2.1.2 < 3.0.0"
      },
      "engines": {
        "node": ">=0.10.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/express"
      }
    },
    "node_modules/ieee754": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/ieee754/-/ieee754-1.2.1.tgz",
      "integrity": "sha512-dcyqhDvX1C46lXZcVqCpK+FtMRQVdIMN6/Df5js2zouUsqG7I6sFxitIC+7KYK29KdXOLHdu9zL4sFnoVQnqaA==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "BSD-3-Clause"
    },
    "node_modules/inherits": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz",
      "integrity": "sha512-k/vGaX4/Yla3WzyMCvTQOXYeIHvqOKtnqBduzTHpzpQZzAskKMhZ2K+EnBiSM9zGSoIFeMpXKxa4dYeZIQqewQ==",
      "license": "ISC"
    },
    "node_modules/inquirer": {
      "version": "9.3.8",
      "resolved": "https://registry.npmjs.org/inquirer/-/inquirer-9.3.8.tgz",
      "integrity": "sha512-pFGGdaHrmRKMh4WoDDSowddgjT1Vkl90atobmTeSmcPGdYiwikch/m/Ef5wRaiamHejtw0cUUMMerzDUXCci2w==",
      "license": "MIT",
      "dependencies": {
        "@inquirer/external-editor": "^1.0.2",
        "@inquirer/figures": "^1.0.3",
        "ansi-escapes": "^4.3.2",
        "cli-width": "^4.1.0",
        "mute-stream": "1.0.0",
        "ora": "^5.4.1",
        "run-async": "^3.0.0",
        "rxjs": "^7.8.1",
        "string-width": "^4.2.3",
        "strip-ansi": "^6.0.1",
        "wrap-ansi": "^6.2.0",
        "yoctocolors-cjs": "^2.1.2"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/is-fullwidth-code-point": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/is-fullwidth-code-
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
