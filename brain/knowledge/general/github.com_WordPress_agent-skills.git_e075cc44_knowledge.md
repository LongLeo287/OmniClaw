---
id: github.com-wordpress-agent-skills.git-e075cc44-kno
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:44.302846
---

# KNOWLEDGE EXTRACT: github.com_WordPress_agent-skills.git_e075cc44
> **Extracted on:** 2026-04-01 10:05:24
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007520599/github.com_WordPress_agent-skills.git_e075cc44

---

## File: `.gitignore`
```
.DS_Store
dist/
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
.env
.env.*

```

## File: `CONTRIBUTING.md`
```markdown
# Contributing to Agent Skills

We welcome contributions! This project is a great opportunity to share your WordPress expertise with the community in a unique way.

## Why Contribute Here?

**You don't need to be a coding wizard.** Unlike typical open source projects, Agent Skills is primarily about capturing *knowledge* and *best practices* in a structured format. If you understand WordPress deeply—whether that's block development, performance optimization, plugin security, or any other domain—you can make a meaningful contribution.

Most of our skills are written in Markdown. The "code" is mostly procedural checklists, decision trees, and reference documentation. If you can explain a WordPress concept clearly, you can contribute here.

## Ways to Contribute

### 1. Improve Existing Skills

The easiest way to start:

- **Fix outdated information** — WordPress evolves quickly. If you spot something that's changed, open a PR.
- **Add missing edge cases** — Did you hit a gotcha that isn't documented? Add it to the "Failure modes" section.
- **Clarify procedures** — If a step confused you, it'll confuse others. Make it clearer.
- **Expand references** — Add deeper documentation on specific topics.

### 2. Create New Skills

Have expertise in a WordPress area we don't cover yet? Consider adding a new skill.

Before starting:
1. Check [existing skills](skills/) to avoid overlap
2. Review the [Authoring Guide](docs/authoring-guide.md) for structure requirements
3. Open an issue to discuss scope (optional but recommended for larger skills)

Scaffold a new skill:

```bash
node shared/scripts/scaffold-skill.mjs <skill-name> "<description>"
```

### 3. Add Evaluation Scenarios

Every skill needs test scenarios under `eval/scenarios/`. These are simple markdown files describing:
- A realistic prompt/task
- What the AI should do
- How to verify it worked

This is a great low-barrier contribution—you're essentially writing "what should happen when someone asks X?"

### 4. Report Issues

Found a skill giving bad advice? AI following a procedure that doesn't work? Open an issue with:
- Which skill
- What went wrong
- What the correct behavior should be

## Skill Structure

Each skill follows this structure:

```
skills/<skill-name>/
├── SKILL.md              # Main instructions (short, procedural)
├── references/           # Deep-dive docs on specific topics
│   └── *.md
└── scripts/              # Deterministic helpers (optional)
    └── *.mjs
```

### SKILL.md Requirements

Every `SKILL.md` needs:

1. **YAML frontmatter** with `name`, `description`, and `compatibility`
2. **When to use** — Conditions that trigger this skill
3. **Inputs required** — What the AI needs to gather first
4. **Procedure** — Step-by-step checklist
5. **Verification** — How to confirm it worked
6. **Failure modes / debugging** — Common problems and fixes
7. **Escalation** — When to ask for human help

See any existing skill for examples.

## Guidelines

### Keep It Practical

- Focus on what developers actually need to do
- Include concrete examples, not abstract theory
- Link to official docs for deep dives

### Keep It Current

- Target WordPress 6.9+ and PHP 7.2.24+
- Avoid legacy patterns (Classic themes, pre-Gutenberg APIs)
- Update compatibility frontmatter when requirements change

### Keep It Testable

- Add at least one eval scenario for new skills
- Run `node eval/harness/run.mjs` before submitting

### Keep It Small

- Prefer small, focused skills over mega-skills
- Keep `SKILL.md` short—push depth into `references/`
- One skill should do one thing well

## Submitting Changes

1. Fork the repo
2. Create a branch (`git checkout -b improve-block-dev-skill`)
3. Make your changes
4. Run validation: `node eval/harness/run.mjs`
5. Commit with a clear message
6. Open a pull request

For significant changes, consider opening an issue first to discuss the approach.

## Questions?

Open an issue or start a discussion. We're happy to help you get started.

---

*Your WordPress knowledge can help thousands of developers get better AI assistance. Thank you for contributing!*
```

## File: `LICENSE`
```
Agent Skills for WordPress
Copyright (C) 2026 WordPress Contributors

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
```

## File: `README.md`
```markdown
# Agent Skills for WordPress

**Teach AI coding assistants how to build WordPress the right way.**

Agent Skills are portable bundles of instructions, checklists, and scripts that help AI assistants (Claude, Copilot, Codex, Cursor, etc.) understand WordPress development patterns, avoid common mistakes, and follow best practices.

> **AI Authorship Disclosure:** These skills were generated using GPT-5.2 Codex (High Reasoning) from official Gutenberg and WordPress documentation, then reviewed and edited by WordPress contributors. We tested skills with AI assistants and iterated based on results. This is v1, and skills will improve as the community uses them and contributes fixes. See [docs/ai-authorship.md](docs/ai-authorship.md) for details. ([WordPress AI Guidelines](https://make.wordpress.org/ai/handbook/ai-guidelines/))

## Why Agent Skills?

AI coding assistants are powerful, but they often:
- Generate outdated WordPress patterns (pre-Gutenberg, pre-block themes)
- Miss critical security considerations in plugin development
- Skip proper block deprecations, causing "Invalid block" errors
- Ignore existing tooling in your repo

Agent Skills solve this by giving AI assistants **expert-level WordPress knowledge** in a format they can actually use.

## Available Skills

| Skill | What it teaches |
|-------|-----------------|
| **wordpress-router** | Classifies WordPress repos and routes to the right workflow |
| **wp-project-triage** | Detects project type, tooling, and versions automatically |
| **wp-block-development** | Gutenberg blocks: `block.json`, attributes, rendering, deprecations |
| **wp-block-themes** | Block themes: `theme.json`, templates, patterns, style variations |
| **wp-plugin-development** | Plugin architecture, hooks, settings API, security |
| **wp-rest-api** | REST API routes/endpoints, schema, auth, and response shaping |
| **wp-interactivity-api** | Frontend interactivity with `data-wp-*` directives and stores |
| **wp-abilities-api** | Capability-based permissions and REST API authentication |
| **wp-wpcli-and-ops** | WP-CLI commands, automation, multisite, search-replace |
| **wp-performance** | Profiling, caching, database optimization, Server-Timing |
| **wp-phpstan** | PHPStan static analysis for WordPress projects (config, baselines, WP-specific typing) |
| **wp-playground** | WordPress Playground for instant local environments |
| **wpds** | WordPress Design System |
| **blueprint** | WordPress Playground Blueprints for declarative Playground environment setup |

## Quick Start

### Install globally for Claude Code

```bash
# Clone agent-skills
git clone https://github.com/WordPress/agent-skills.git
cd agent-skills

# Build the distribution
node shared/scripts/skillpack-build.mjs --clean

# Install all skills globally (available across all projects)
node shared/scripts/skillpack-install.mjs --global

# Or install specific skills only
node shared/scripts/skillpack-install.mjs --global --skills=wp-playground,wp-block-development
```

This installs skills to `~/.claude/skills/` where Claude Code will automatically discover them.

### Install into your repo

```bash
# Clone agent-skills
git clone https://github.com/WordPress/agent-skills.git
cd agent-skills

# Build the distribution
node shared/scripts/skillpack-build.mjs --clean

# Install into your WordPress project
node shared/scripts/skillpack-install.mjs --dest=../your-wp-project --targets=codex,vscode,claude,cursor
```

This copies skills into:
- `.codex/skills/` for OpenAI Codex
- `.github/skills/` for VS Code / GitHub Copilot
- `.claude/skills/` for Claude Code (project-level)
- `.cursor/skills/` for Cursor (project-level)

### Install globally for Cursor

```bash
node shared/scripts/skillpack-install.mjs --targets=cursor-global
```

This installs skills to `~/.cursor/skills/` where Cursor will discover them.

### Available options

```bash
# List available skills
node shared/scripts/skillpack-install.mjs --list

# Dry run (preview without installing)
node shared/scripts/skillpack-install.mjs --global --dry-run

# Install specific skills to a project (e.g. Claude + Cursor)
node shared/scripts/skillpack-install.mjs --dest=../my-repo --targets=claude,cursor --skills=wp-wpcli-and-ops
```

### Manual installation

Copy any skill folder from `skills/` into your project's instructions directory for your AI assistant.

## How It Works

Each skill contains:

```
skills/wp-block-development/
├── SKILL.md              # Main instructions (when to use, procedure, verification)
├── references/           # Deep-dive docs on specific topics
│   ├── block-json.md
│   ├── deprecations.md
│   └── ...
└── scripts/              # Deterministic helpers (detection, validation)
    └── list_blocks.mjs
```

When you ask your AI assistant to work on WordPress code, it reads these skills and follows the documented procedures rather than guessing.

## Compatibility

- **WordPress 6.9+** (PHP 7.2.24+)
- Works with any AI assistant that supports project-level instructions

## Contributing

**We welcome contributions!** This project is a great way to share your WordPress expertise—you don't need to be a coding wizard. Most skills are written in Markdown, focusing on clear procedures and best practices.

See [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to get started.

Quick commands:

```bash
# Scaffold a new skill
node shared/scripts/scaffold-skill.mjs <skill-name> "<description>"

# Validate skills
node eval/harness/run.mjs
```

## Documentation

- [Authoring Guide](docs/authoring-guide.md) - How to create and improve skills
- [Principles](../../../core/security/QUARANTINE/vetted/repos/trivy/docs/community/principles.md) - Design philosophy
- [Packaging](docs/packaging.md) - Build and distribution
- [Compatibility Policy](docs/compatibility-policy.md) - Version targeting

## License

GPL-2.0-or-later
```

## File: `docs/ai-authorship.md`
```markdown
# AI Authorship Disclosure

This document describes how AI tools were used to create the skills in this repository, in accordance with the [WordPress AI Guidelines](https://make.wordpress.org/ai/handbook/ai-guidelines/).

## Summary

| Aspect | Details |
|--------|---------|
| **AI Tool** | GPT-5.2 Codex (High Reasoning) |
| **Source Material** | Official Gutenberg trunk documentation, WordPress developer docs |
| **Human Review** | All skills reviewed and edited by WordPress contributors |
| **Testing** | Skills tested with AI assistants (Claude, Copilot, Codex) |
| **License** | GPL-2.0-or-later (compatible with WordPress) |

## Process

1. **Source Collection**: Up-to-date documentation was gathered from Gutenberg trunk and official WordPress developer resources.

2. **AI Generation**: GPT-5.2 Codex (High Reasoning) processed the documentation to create semantically dense skill files, distilling large doc sets into actionable instructions AI assistants can follow.

3. **Contributor Review**: WordPress contributors reviewed each skill for accuracy, alignment with current best practices, and completeness.

4. **AI-Assisted Testing**: Skills were tested by using them with AI coding assistants (Codex and Claude Code) on real WordPress development tasks, sourced from [WP Bench](https://make.wordpress.org/ai/2026/01/14/introducing-wp-bench-a-wordpress-ai-benchmark/) to verify they produce correct guidance. That said, skills have not (yet) been run across a formal evaluation system, *as one does not exist*.

5. **Iteration**: Based on testing results, skills were refined before the v1 release.

## Per-Skill Breakdown

All v1 skills followed the same process described above. As skills diverge in their development history, this table will be updated.

| Skill | AI Generated | Human Reviewed | Tested |
|-------|--------------|----------------|--------|
| [wordpress-router](../bmad_repo/SKILL.md) | Yes | Yes | Yes |
| [wp-project-triage](../bmad_repo/SKILL.md) | Yes | Yes | Yes |
| [wp-block-development](../bmad_repo/SKILL.md) | Yes | Yes | Yes |
| [wp-block-themes](../bmad_repo/SKILL.md) | Yes | Yes | Yes |
| [wp-plugin-development](../bmad_repo/SKILL.md) | Yes | Yes | Yes |
| [wp-rest-api](../bmad_repo/SKILL.md) | Yes | Yes | Yes |
| [wp-interactivity-api](../bmad_repo/SKILL.md) | Yes | Yes | Yes |
| [wp-abilities-api](../bmad_repo/SKILL.md) | Yes | Yes | Yes |
| [wp-wpcli-and-ops](../bmad_repo/SKILL.md) | Yes | Yes | Yes |
| [wp-performance](../bmad_repo/SKILL.md) | Yes | Yes | Yes |
| [wp-phpstan](../bmad_repo/SKILL.md) | Yes | Yes | Yes |
| [wp-playground](../bmad_repo/SKILL.md) | Yes | Yes | Yes |
| [wpds](../bmad_repo/SKILL.md) | Yes | Yes | Yes |

## Quality Commitment

These skills are curated distillations of official documentation, reviewed by people who understand WordPress development. That said:

- Skills will contain errors. Please [report issues](https://github.com/WordPress/agent-skills/issues).
- Skills will improve over time as the community uses them and contributes fixes.
- We welcome PRs that improve accuracy, fix outdated patterns, or add missing guidance.

## Evolution

This disclosure will be updated as:
- Individual skills receive significant human rewrites
- New skills are added with different authorship processes
- Community feedback identifies areas needing clarification
```

## File: `docs/authoring-guide.md`
```markdown
# Authoring guide (AI-assisted)

This repo is built for **AI-assisted authoring** with **deterministic guardrails**.

## Golden rules

- Keep `SKILL.md` short and procedural; push depth into `references/` and scripts.
- Prefer deterministic scripts for anything the agent would otherwise “guess” (repo detection, version checks, lint/test command discovery).
- Don’t add a new skill without at least one scenario in `eval/scenarios/`.
- Keep file references 1 hop from `SKILL.md` (avoid deep chains).
- Include a `compatibility:` frontmatter line matching `docs/compatibility-policy.md`.

## Workflow: draft → harden → ship

1. **Route first**
   - Start from `skills/wordpress-router/SKILL.md` to classify the repo and pick the domain.
2. **Collect inputs**
   - What repo type(s) does triage detect?
   - What WP/PHP/Node versions are targeted (if known)?
   - What tooling exists (Composer, @wordpress/scripts, PHPUnit, Playwright, wp-env)?
3. **Draft the skill (AI-assisted)**
   - Write `SKILL.md` as a checklist/procedure with explicit “Verification” and “Failure modes”.
   - Keep examples short; link to topic references when needed.
4. **Add deterministic helpers**
   - If the skill depends on detection (versions, project layout, build system), add a script under `scripts/`.
5. **Add evaluation scenario(s)**
   - Add at least 1 prompt-style scenario under `eval/scenarios/` describing expected behavior.
6. **Validate**
   - Run `node eval/harness/run.mjs`.
   - Optionally validate frontmatter using `skills-ref validate` (see `docs/upstream-sync.md` for CI guidance).

## Scaffolding a new skill

Use the scaffold script to create a minimal, spec-compliant starting point:

- `node shared/scripts/scaffold-skill.mjs <skill-name> "<description>"`

## “Skill generation” prompt template (recommended)

When using an LLM to draft a skill, provide:

- The repo triage JSON output
- The user’s task statement(s)
- Any version constraints and non-goals
- The required sections: When to use, Inputs required, Procedure, Verification, Failure modes, Escalation

Then ask the model to output:

1. `skills/<skill-name>/SKILL.md`
2. Any `references/*.md` files it mentions
3. Any `scripts/*` stubs needed for deterministic checks
4. One scenario markdown file under `eval/scenarios/`

## Suggested initial domain skills (v1)

See `docs/skill-set-v1.md`.
```

## File: `docs/compatibility-policy.md`
```markdown
# Compatibility policy

This repo is an authoring workspace for WordPress-focused Agent Skills.

## Compatibility contract (v1)

Skills in this repo target:

- WordPress core **6.9+**
- PHP **7.2.24+** (minimum supported by WordPress 6.9)

## Authoring rules

Skills should:

- Prefer stable WordPress APIs and best practices.
- Prefer detection + guardrails (triage) over hard-coded assumptions.
- If a task requires behavior that differs across core versions, ask for a target version (but default guidance should assume WP 6.9+).
```

## File: `docs/packaging.md`
```markdown
# Packaging and installation

This repo is the **source of truth** under `skills/`.

To distribute skills to other repos/tools (without symlinks), use the skillpack scripts.

## Build dist

Build a packaged copy under `dist/`:

- `node shared/scripts/skillpack-build.mjs --clean`

Outputs:

- `dist/codex/.codex/skills/*` (OpenAI Codex repo layout)
- `dist/vscode/.github/skills/*` (VS Code / Copilot repo layout)
- `dist/claude/.claude/skills/*` (Claude Code repo layout)
- `dist/cursor/.cursor/skills/*` (Cursor repo layout)

## Install into another repo

1. Build dist (above).
2. Install into a destination repo:

- `node shared/scripts/skillpack-install.mjs --dest=../some-repo --targets=codex,vscode,claude,cursor`

By default, install mode is `replace` (it replaces only the skill directories it installs).

```

## File: `docs/principles.md`
```markdown
# Principles

- Prefer small, composable skills over a single "mega-skill".
- Keep `SKILL.md` bodies short; move depth into `references/`.
- Bundle deterministic checks as scripts when reliability matters.
- Treat upstream docs as canonical; store agent-first checklists and decision trees.
- Every new skill must include at least one eval scenario under `eval/scenarios/`.
```

## File: `docs/skill-set-v1.md`
```markdown
# WordPress skill set (v1)

This repo currently includes:

- `wordpress-router`
- `wp-project-triage`
- `wp-block-development`
- `wp-block-themes`
- `wp-plugin-development`
- `wp-rest-api`
- `wp-interactivity-api`
- `wp-abilities-api`
- `wp-wpcli-and-ops`
- `wp-performance`
- `wp-phpstan`

Planned next skills (not yet implemented):

- `wp-build-tooling`
- `wp-testing`
- `wp-security`
```

## File: `docs/upstream-sync.md`
```markdown
# Upstream sync (automation plan)

Goal: when upstream changes (WordPress core releases, Gutenberg releases, docs updates), the repo should **regenerate indexes** and (eventually) **open PRs** that update affected skills/references.

## What to automate first (low risk)

1. **Indexes and matrices**
   - WordPress core version list (latest stable + recent).
   - Gutenberg releases list (latest stable + recent).
   - WordPress ↔ Gutenberg mapping table (derived from canonical docs where available).
2. **Routing metadata refresh**
   - Update `shared/references/*.json` files only.

This keeps automation deterministic and reviewable before it starts rewriting skill prose.

## Later automation (higher risk)

- “Reference chunk regeneration” from upstream docs into `skills/*/references/*.md`.
- Task-shaped deltas (e.g. a new Gutenberg package, new block APIs, changes in theme.json schema).
- Semi-automated PRs that include:
  - regenerated references
  - updated checklists
  - updated eval scenarios

## Scripts

- `shared/scripts/update-upstream-indices.mjs`
  - Fetches upstream sources and rewrites JSON indexes in `shared/references/`.

## CI / PR bot design (recommended)

- Schedule a workflow (daily/weekly).
- Run `shared/scripts/update-upstream-indices.mjs`.
- If `git diff` is non-empty, open a PR with:
  - a summary of changes
  - links to upstream release notes
  - a checklist for human review (“does this impact blocks/themes/plugin workflows?”)

## Validation

- Always run `node eval/harness/run.mjs`.
- Optional: use Agent Skills reference validator:
  - `skills-ref validate skills/<skill-name>`

## Canonical sources

The automation should prefer canonical sources and avoid scraping where possible.

- WordPress core releases and API endpoints (official WordPress APIs)
- Gutenberg releases (GitHub releases)
- WordPress developer docs (used for the WP↔Gutenberg mapping when no API exists)

```

## File: `eval/harness/run.mjs`
```
import fs from "node:fs";
import path from "node:path";
import { spawnSync } from "node:child_process";

function readUtf8(filePath) {
  return fs.readFileSync(filePath, "utf8");
}

function listSkillDirs(repoRoot) {
  const skillsRoot = path.join(repoRoot, "skills");
  if (!fs.existsSync(skillsRoot)) return [];
  return fs
    .readdirSync(skillsRoot, { withFileTypes: true })
    .filter((d) => d.isDirectory())
    .map((d) => path.join(skillsRoot, d.name));
}

function parseFrontmatter(markdown) {
  const lines = markdown.split("\n");
  if (lines[0]?.trim() !== "---") return null;

  let endIndex = -1;
  for (let i = 1; i < Math.min(lines.length, 500); i += 1) {
    if (lines[i].trim() === "---") {
      endIndex = i;
      break;
    }
  }
  if (endIndex === -1) return null;

  const fmLines = lines.slice(1, endIndex);
  const metadata = {};

  // Minimal YAML mapping parser (supports only "key: value" one-liners).
  for (const line of fmLines) {
    if (!line.trim()) continue;
    const m = line.match(/^\s*([A-Za-z0-9_-]+)\s*:\s*(.*)\s*$/);
    if (!m) continue;
    const key = m[1];
    const raw = m[2];
    const value = raw.replace(/^"(.*)"$/, "$1").replace(/^'(.*)'$/, "$1").trim();
    metadata[key] = value;
  }

  return {
    name: typeof metadata.name === "string" && metadata.name ? metadata.name : null,
    description: typeof metadata.description === "string" && metadata.description ? metadata.description : null,
    _raw: metadata,
  };
}

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

function validateSkillName(name) {
  // Mirrors skills-ref validator intent (unicode letters/digits + hyphens, lowercase).
  if (name.length > 64) return `Skill name exceeds 64 chars (${name.length})`;
  if (name !== name.toLowerCase()) return "Skill name must be lowercase";
  if (name.startsWith("-") || name.endsWith("-")) return "Skill name cannot start or end with hyphen";
  if (name.includes("--")) return "Skill name cannot contain consecutive hyphens";
  const ok = /^[\p{Ll}\p{Nd}]+(?:-[\p{Ll}\p{Nd}]+)*$/u.test(name);
  if (!ok) return "Skill name contains invalid characters";
  return null;
}

function runJsonCommand(command, args, cwd) {
  const out = spawnSync(command, args, { cwd, encoding: "utf8" });
  if (out.status !== 0) {
    throw new Error(`Command failed: ${command} ${args.join(" ")}\n${out.stderr || out.stdout}`);
  }
  const text = out.stdout.trim();
  try {
    return JSON.parse(text);
  } catch {
    throw new Error(`Expected JSON output from: ${command} ${args.join(" ")}\nGot:\n${text.slice(0, 1000)}`);
  }
}

function main() {
  const repoRoot = process.cwd();

  const skillDirs = listSkillDirs(repoRoot);
  assert(skillDirs.length > 0, "No skills found under ./skills");

  for (const dir of skillDirs) {
    const skillPath = path.join(dir, "SKILL.md");
    assert(fs.existsSync(skillPath), `Missing SKILL.md: ${path.relative(repoRoot, skillPath)}`);
    const md = readUtf8(skillPath);
    const fm = parseFrontmatter(md);
    assert(fm, `Missing YAML frontmatter in: ${path.relative(repoRoot, skillPath)}`);
    assert(fm.name, `Missing frontmatter 'name' in: ${path.relative(repoRoot, skillPath)}`);
    assert(fm.description, `Missing frontmatter 'description' in: ${path.relative(repoRoot, skillPath)}`);

    const expectedName = path.basename(dir);
    assert(
      fm.name === expectedName,
      `Frontmatter name mismatch in ${path.relative(repoRoot, skillPath)}: expected '${expectedName}', got '${fm.name}'`
    );

    const nameError = validateSkillName(fm.name);
    assert(!nameError, `Invalid skill name in ${path.relative(repoRoot, skillPath)}: ${nameError}`);
    assert(
      fm.description.length <= 1024,
      `Description too long in ${path.relative(repoRoot, skillPath)} (${fm.description.length} chars)`
    );

    const compatibility = fm._raw.compatibility;
    assert(compatibility, `Missing frontmatter 'compatibility' in: ${path.relative(repoRoot, skillPath)}`);
    assert(
      compatibility.length <= 500,
      `Compatibility too long in ${path.relative(repoRoot, skillPath)} (${compatibility.length} chars)`
    );
    assert(
      compatibility.includes("WordPress 6.9") && compatibility.includes("PHP 7.2.24"),
      `Compatibility contract mismatch in ${path.relative(repoRoot, skillPath)} (expected WP 6.9 + PHP 7.2.24+)`
    );
  }

  const triageScript = path.join(repoRoot, "skills", "wp-project-triage", "scripts", "detect_wp_project.mjs");
  assert(fs.existsSync(triageScript), "Missing triage detector script");

  const report = runJsonCommand("node", [triageScript], repoRoot);
  assert(report?.tool?.name === "detect_wp_project", "Triage report missing tool.name");
  assert(Array.isArray(report?.project?.kind), "Triage report missing project.kind[]");
  assert(report?.signals?.paths?.repoRoot, "Triage report missing signals.paths.repoRoot");
  assert(report?.tooling?.php && report?.tooling?.node && report?.tooling?.tests, "Triage report missing tooling blocks");

  process.stdout.write("OK: skills frontmatter and triage report sanity checks passed.\n");
}

main();
```

## File: `eval/scenarios/README.md`
```markdown
# Eval scenarios

- All scenarios are JSON files only (no markdown counterparts).
- Each file defines: name, skills, query, expected_behavior, and success_criteria.
- Add new scenarios as `<slug>.json` in this directory.
```

## File: `eval/scenarios/abilities-register-and-expose.json`
```json
{
  "name": "Register ability and expose to REST",
  "skills": ["wordpress-router", "wp-project-triage", "wp-abilities-api"],
  "query": "I want to add a new ability for my plugin feature and have the client UI check it via REST. What should I change?",
  "expected_behavior": [
    "Step 1: Run wordpress-router to classify repo kind",
    "Step 2: Run wp-project-triage to detect plugin structure",
    "Step 3: Route to wp-abilities-api skill",
    "Step 4: Register ability category if needed with wp_register_ability_category()",
    "Step 5: Register ability with wp_register_ability()",
    "Step 6: Set meta.show_in_rest to true for REST exposure",
    "Step 7: Document wp-abilities/v1 REST namespace",
    "Step 8: Verify endpoint returns the new ability",
    "Step 9: Show client-side consumption via @wordpress/abilities"
  ],
  "success_criteria": [
    "Routes to wp-abilities-api skill",
    "Uses wp_register_ability() correctly",
    "Enables show_in_rest in meta",
    "Documents REST endpoint wp-abilities/v1",
    "Provides verification steps"
  ]
}
```

## File: `eval/scenarios/block-add-attribute-and-migrate.json`
```json
{
  "name": "Add a block attribute safely",
  "skills": ["wordpress-router", "wp-project-triage", "wp-block-development"],
  "query": "Add a new attribute to an existing block and make sure existing content doesn't become 'Invalid block'.",
  "expected_behavior": [
    "Step 1: Run wordpress-router to classify repo kind and tooling",
    "Step 2: Run wp-project-triage script: node skills/wp-project-triage/scripts/detect_wp_project.mjs",
    "Step 3: Route to wp-block-development based on block.json presence",
    "Step 4: Inspect current block.json, edit.js, and save.js to understand serialization",
    "Step 5: Identify if the new attribute affects saved markup",
    "Step 6: If markup changes, add a deprecated version with the old save function",
    "Step 7: Optionally add migrate function to transform old attributes",
    "Step 8: Test that existing content migrates without 'Invalid block' error"
  ],
  "success_criteria": [
    "Triage script is run before making changes",
    "Routes to wp-block-development skill",
    "Inspects block.json and save function before modifying",
    "If saved markup changes, adds deprecated entry",
    "Provides migration path if attribute structure changes",
    "Verifies no 'Invalid block' error on existing content"
  ]
}
```

## File: `eval/scenarios/block-convert-to-dynamic-render-php.json`
```json
{
  "name": "Convert a static block to dynamic block",
  "skills": ["wordpress-router", "wp-project-triage", "wp-block-development"],
  "query": "Convert an existing static block to be server-rendered (dynamic) using a render.php file, without breaking existing content.",
  "expected_behavior": [
    "Step 1: Run wordpress-router to classify repo kind",
    "Step 2: Run wp-project-triage to detect block structure",
    "Step 3: Route to wp-block-development skill",
    "Step 4: Recommend adding render field in block.json pointing to render.php",
    "Step 5: Alternatively, use render_callback in register_block_type()",
    "Step 6: Use get_block_wrapper_attributes() in PHP output for proper wrapper",
    "Step 7: Set save function to return null or minimal InnerBlocks.Content",
    "Step 8: If saved markup changes, add deprecated entry for migration",
    "Step 9: Test existing blocks still render without errors"
  ],
  "success_criteria": [
    "Uses render field in block.json or render_callback",
    "PHP output uses get_block_wrapper_attributes()",
    "Save function returns null or minimal content",
    "Deprecations added if saved markup structure changes",
    "Existing content continues to work"
  ]
}
```

## File: `eval/scenarios/block-create-interactive-inner-blocks.json`
```json
{
  "name": "Create modern interactive container block",
  "skills": ["wordpress-router", "wp-project-triage", "wp-block-development", "wp-interactivity-api"],
  "query": "Create a new block that uses Inner Blocks (container block), has simple frontend interactivity (a click toggles a CSS class), and uses the most modern, recommended scaffolding and metadata.",
  "expected_behavior": [
    "Step 1: Run wordpress-router to classify repo kind",
    "Step 2: Run wp-project-triage to detect tooling and WP version",
    "Step 3: Route to wp-block-development for scaffolding and wp-interactivity-api for directives",
    "Step 4: Recommend @wordpress/create-block with interactive template",
    "Step 5: Use useInnerBlocksProps/InnerBlocks for nested content",
    "Step 6: Set up Interactivity API store with toggle action",
    "Step 7: Add data-wp-interactive namespace to wrapper",
    "Step 8: Add data-wp-on--click directive for toggle",
    "Step 9: Add data-wp-class--active for conditional class",
    "Step 10: Verify wrapper attributes are correct in edit and save/render"
  ],
  "success_criteria": [
    "Uses @wordpress/create-block for scaffolding",
    "Uses useInnerBlocksProps for container pattern",
    "Interactivity API directives properly set up",
    "Store namespace matches data-wp-interactive value",
    "Wrapper attributes maintained in editor and frontend"
  ]
}
```

## File: `eval/scenarios/interactivity-route-and-debug.json`
```json
{
  "name": "Route and debug Interactivity API issue",
  "skills": ["wordpress-router", "wp-project-triage", "wp-interactivity-api"],
  "query": "My block uses data-wp-interactive and data-wp-on--click, but clicks don't do anything on the frontend. How do I debug this repo?",
  "expected_behavior": [
    "Step 1: Run wordpress-router to classify repo kind",
    "Step 2: Run wp-project-triage to detect block and interactivity setup",
    "Step 3: Route to wp-interactivity-api skill",
    "Step 4: Search for data-wp-interactive, @wordpress/interactivity, viewScriptModule",
    "Step 5: Check block.json has viewScriptModule field",
    "Step 6: Verify view script module loads in browser network tab",
    "Step 7: Confirm store namespace matches data-wp-interactive value",
    "Step 8: Check browser console for JavaScript errors",
    "Step 9: Verify action is exported from store",
    "Step 10: Check interactivity scope (wp-context if needed)"
  ],
  "success_criteria": [
    "Routes to wp-interactivity-api skill",
    "Provides debugging checklist",
    "Checks viewScriptModule configuration",
    "Verifies namespace matching between store and directive",
    "Mentions console error checking",
    "Covers scope/context issues"
  ]
}
```

## File: `eval/scenarios/performance-autoload-options-bloat.json`
```json
{
  "name": "Diagnose autoloaded options bloat",
  "skills": ["wordpress-router", "wp-project-triage", "wp-performance"],
  "query": "Admin pages are slow and memory usage is high. Check whether autoloaded options are bloated and suggest a safe plan.",
  "expected_behavior": [
    "Step 1: Run wordpress-router to classify repo kind",
    "Step 2: Run wp-project-triage to verify WP-CLI availability",
    "Step 3: Route to wp-performance skill",
    "Step 4: Run wp doctor check autoload-options-size as quick signal",
    "Step 5: Run wp option list --autoload=on --format=csv to list autoloaded options",
    "Step 6: Sort by size_bytes to identify largest options",
    "Step 7: Identify candidates for autoload disable or migration",
    "Step 8: Propose safe remediation: disable autoload flag on large options",
    "Step 9: Suggest migrating blobs to object cache if available",
    "Step 10: Warn about cautious deletion - verify options are unused first"
  ],
  "success_criteria": [
    "Uses wp-performance skill",
    "Uses WP-CLI commands for diagnosis",
    "Identifies large autoloaded options by size",
    "Provides safe remediation plan",
    "Warns against destructive changes without verification"
  ]
}
```

## File: `eval/scenarios/performance-profile-slow-endpoint.json`
```json
{
  "name": "Profile a slow endpoint (backend-only)",
  "skills": ["wordpress-router", "wp-project-triage", "wp-performance"],
  "query": "The site's homepage TTFB is slow. Give me a backend-only profiling plan and what commands to run.",
  "expected_behavior": [
    "Step 1: Run wordpress-router to classify repo kind",
    "Step 2: Run wp-project-triage to verify WP-CLI and profiling tools",
    "Step 3: Route to wp-performance skill",
    "Step 4: Run wp doctor check first for quick diagnostics",
    "Step 5: Run wp profile stage --url=/ to profile request stages",
    "Step 6: Identify slowest stage (bootstrap, main_query, template)",
    "Step 7: Run wp profile hook --stage=<slow-stage> to drill down",
    "Step 8: Identify slow hooks or callbacks",
    "Step 9: Optionally use Query Monitor via REST headers (X-QM-* headers)",
    "Step 10: Explain how to use QM envelope for headless inspection"
  ],
  "success_criteria": [
    "Routes to wp-performance skill",
    "Uses wp doctor check first",
    "Uses wp profile stage and wp profile hook",
    "Provides backend-only workflow (no browser required)",
    "Mentions Query Monitor as optional with REST/envelope usage"
  ]
}
```

## File: `eval/scenarios/phpstan-fix-third-party-class.json`
```json
{
  "name": "Handle PHPStan unknown third-party class in plugin code",
  "skills": ["wordpress-router", "wp-project-triage", "wp-phpstan"],
  "query": "PHPStan reports 'Class WC_Order not found' in our WordPress plugin integration. How should I fix this (or configure PHPStan) without hiding real errors?",
  "expected_behavior": [
    "Step 1: Run wordpress-router to classify repo kind",
    "Step 2: Run wp-project-triage to detect tooling (Composer/PHPStan present)",
    "Step 3: Route to wp-phpstan skill",
    "Step 4: Discover how PHPStan is invoked (composer scripts vs vendor/bin/phpstan)",
    "Step 5: Locate phpstan.neon/phpstan.neon.dist and any baseline",
    "Step 6: Prefer stubs (php-stubs/wordpress-stubs, php-stubs/woocommerce-stubs) or equivalent autoloading",
    "Step 7: If the dependency cannot be analyzed, add a targeted ignoreErrors pattern for WC_",
    "Step 8: Keep ignoreErrors patterns narrow and documented",
    "Step 9: Re-run PHPStan to verify the change"
  ],
  "success_criteria": [
    "Guidance prefers the repo's existing PHPStan command",
    "Third-party class handling is safe and narrow",
    "Verification step included"
  ]
}
```

## File: `eval/scenarios/plugin-add-settings-page.json`
```json
{
  "name": "Add a settings page with Settings API",
  "skills": ["wordpress-router", "wp-project-triage", "wp-plugin-development"],
  "query": "Add a new plugin setting (checkbox + text field) with a settings page, and make sure it's secure and saves correctly.",
  "expected_behavior": [
    "Step 1: Run wordpress-router to classify repo kind",
    "Step 2: Run wp-project-triage script to detect plugin structure",
    "Step 3: Route to wp-plugin-development based on plugin header presence",
    "Step 4: Use Settings API: register_setting() with sanitize_callback",
    "Step 5: Create settings page with add_options_page() or add_submenu_page()",
    "Step 6: Add settings sections with add_settings_section()",
    "Step 7: Add settings fields with add_settings_field()",
    "Step 8: Implement proper nonce verification in form",
    "Step 9: Add capability check (manage_options or custom)",
    "Step 10: Escape all output with esc_html(), esc_attr(), etc."
  ],
  "success_criteria": [
    "Uses Settings API (register_setting, add_settings_field)",
    "Includes sanitize_callback for input validation",
    "Nonce is present and verified",
    "Capability check is enforced",
    "Output is properly escaped",
    "Settings save and load correctly"
  ]
}
```

## File: `eval/scenarios/plugin-add-uninstall-cleanup.json`
```json
{
  "name": "Add uninstall cleanup",
  "skills": ["wordpress-router", "wp-project-triage", "wp-plugin-development"],
  "query": "Ensure the plugin removes its options on uninstall but does not delete data on deactivation.",
  "expected_behavior": [
    "Step 1: Run wordpress-router to classify repo kind",
    "Step 2: Run wp-project-triage to detect plugin structure",
    "Step 3: Route to wp-plugin-development skill",
    "Step 4: Create uninstall.php in plugin root",
    "Step 5: Add WP_UNINSTALL_PLUGIN constant check for security",
    "Step 6: Delete plugin options with delete_option()",
    "Step 7: Optionally delete custom tables with $wpdb->query()",
    "Step 8: Ensure deactivation hook only does lightweight cleanup",
    "Step 9: Do NOT delete stored data on deactivation",
    "Step 10: Test uninstall by deleting plugin and verifying options removed"
  ],
  "success_criteria": [
    "Uses uninstall.php or register_uninstall_hook",
    "Checks WP_UNINSTALL_PLUGIN constant",
    "Removes plugin data on uninstall",
    "Deactivation hook is lightweight (no data deletion)",
    "Clear separation between deactivation and uninstall behavior"
  ]
}
```

## File: `eval/scenarios/plugin-security-nonce-and-capability.json`
```json
{
  "name": "Fix admin action security issue",
  "skills": ["wordpress-router", "wp-project-triage", "wp-plugin-development"],
  "query": "This plugin has an admin POST handler that checks a nonce but not user capabilities. Fix it.",
  "expected_behavior": [
    "Step 1: Run wordpress-router to classify repo kind",
    "Step 2: Run wp-project-triage to detect plugin structure",
    "Step 3: Route to wp-plugin-development skill",
    "Step 4: Identify the POST handler code",
    "Step 5: Verify nonce check exists with wp_verify_nonce() or check_admin_referer()",
    "Step 6: Add capability check with current_user_can()",
    "Step 7: Use appropriate capability (manage_options, edit_posts, custom cap)",
    "Step 8: Sanitize/validate all input with sanitize_text_field(), absint(), etc.",
    "Step 9: Use wp_unslash() before sanitization for $_POST data",
    "Step 10: Escape all output with esc_html(), esc_attr(), etc."
  ],
  "success_criteria": [
    "Both nonce AND capability checks present",
    "Appropriate capability used for the action",
    "Input is sanitized/validated",
    "Output is properly escaped",
    "Security vulnerability is resolved"
  ]
}
```

## File: `eval/scenarios/rest-api-add-custom-endpoint.json`
```json
{
  "name": "Add a custom REST endpoint with permissions and schema",
  "skills": ["wordpress-router", "wp-project-triage", "wp-rest-api"],
  "query": "Add a REST endpoint /my-plugin/v1/reports that returns JSON data, requires manage_options, and validates a days query param (1-30).",
  "expected_behavior": [
    "Step 1: Run wordpress-router to classify repo kind",
    "Step 2: Run wp-project-triage for tooling",
    "Step 3: Register route on rest_api_init with namespace my-plugin/v1",
    "Step 4: Provide permission_callback using current_user_can('manage_options')",
    "Step 5: Define args with type/validate/sanitize for days param",
    "Step 6: Return data via rest_ensure_response or WP_REST_Response",
    "Step 7: Avoid wp_send_json and direct $_GET usage"
  ],
  "success_criteria": [
    "Uses register_rest_route with a unique namespace",
    "Includes permission_callback (not missing)",
    "Validates and sanitizes days parameter",
    "Returns WP_REST_Response or rest_ensure_response",
    "Mentions authentication or nonce if needed"
  ]
}
```

## File: `eval/scenarios/router-route-theme-json.json`
```json
{
  "name": "Route a theme.json task",
  "skills": ["wordpress-router", "wp-project-triage", "wp-block-themes"],
  "query": "You are in a WordPress repo. I need to add a new typography preset in theme.json and ensure it shows up in the editor.",
  "expected_behavior": [
    "Step 1: Run wordpress-router to classify repo kind and tooling",
    "Step 2: Run triage script to detect theme.json presence",
    "Step 3: Identify repo as block theme (wp-block-theme) or site repo with theme.json",
    "Step 4: Route to wp-block-themes skill",
    "Step 5: Recommend editing settings.typography.fontSizes in theme.json",
    "Step 6: Recommend repo's existing build/lint/test commands if present",
    "Step 7: Verify preset appears in editor's typography settings"
  ],
  "success_criteria": [
    "Router is used first to classify repo",
    "Triage detects block theme or theme.json presence",
    "Routes to wp-block-themes skill",
    "Typography preset added to correct theme.json section",
    "Uses existing repo tooling for verification"
  ]
}
```

## File: `eval/scenarios/skillpack-build-and-install.json`
```json
{
  "name": "Build and install skillpacks",
  "skills": [],
  "query": "Package this repo's skills for Codex, VS Code, Claude, and Cursor and install them into another repository.",
  "expected_behavior": [
    "Step 1: Run build command: node shared/scripts/skillpack-build.mjs --clean --targets=codex,vscode,claude,cursor",
    "Step 2: Verify build output in dist/ directory",
    "Step 3: Run install command: node shared/scripts/skillpack-install.mjs --from=dist --dest=<repo-root> --targets=codex,vscode,claude,cursor",
    "Step 4: Verify skills installed in target repository",
    "Step 5: Confirm no symlinks in installed skills (files are copied)"
  ],
  "success_criteria": [
    "Build command runs successfully",
    "Output created in dist/ directory",
    "Install command copies to target repository",
    "No symlinks in installed skills",
    "Codex, vscode, claude, and cursor targets supported"
  ]
}
```

## File: `eval/scenarios/theme-add-pattern-file.json`
```json
{
  "name": "Add a filesystem pattern to block theme",
  "skills": ["wordpress-router", "wp-project-triage", "wp-block-themes"],
  "query": "Add a new block pattern to a block theme and make sure it shows up in the inserter with the right title/category.",
  "expected_behavior": [
    "Step 1: Run wordpress-router to classify repo kind",
    "Step 2: Run wp-project-triage to confirm block theme (theme.json present)",
    "Step 3: Route to wp-block-themes skill",
    "Step 4: Create file under patterns/ directory",
    "Step 5: Add required PHP header comment with Title and Slug",
    "Step 6: Optionally add Categories, Keywords, Block Types headers",
    "Step 7: Add pattern markup (block comments + HTML)",
    "Step 8: Verify pattern appears in editor inserter"
  ],
  "success_criteria": [
    "Pattern file created in patterns/ directory",
    "File has correct PHP header format with Title and Slug",
    "Pattern contains valid block markup",
    "Pattern is theme-scoped (not global)",
    "Verification step mentions checking in editor inserter"
  ]
}
```

## File: `eval/scenarios/theme-add-style-variation.json`
```json
{
  "name": "Add a style variation",
  "skills": ["wordpress-router", "wp-project-triage", "wp-block-themes"],
  "query": "Add a new style variation to a block theme and explain why an existing site might not reflect changes immediately.",
  "expected_behavior": [
    "Step 1: Run wordpress-router to classify repo kind",
    "Step 2: Run wp-project-triage to detect block theme structure",
    "Step 3: Route to wp-block-themes skill",
    "Step 4: Create JSON file under styles/ directory",
    "Step 5: Include title and settings/styles sections in variation JSON",
    "Step 6: Explain that selected variation is stored in database",
    "Step 7: Note that user customizations may override theme changes",
    "Step 8: Recommend testing on fresh site or resetting customizations",
    "Step 9: Verify variation appears in Site Editor style switcher"
  ],
  "success_criteria": [
    "Style variation file created in styles/ directory",
    "Valid JSON structure with title",
    "Explains database storage of user selection",
    "Mentions user customization override behavior",
    "Provides testing guidance for fresh vs existing sites"
  ]
}
```

## File: `eval/scenarios/theme-json-add-typography-preset.json`
```json
{
  "name": "Add typography preset via theme.json",
  "skills": ["wordpress-router", "wp-project-triage", "wp-block-themes"],
  "query": "Add a new typography preset in theme.json and ensure it shows up in the editor.",
  "expected_behavior": [
    "Step 1: Run wordpress-router to classify repo kind",
    "Step 2: Run wp-project-triage to detect theme structure",
    "Step 3: Route to wp-block-themes skill",
    "Step 4: Locate correct theme root and theme.json file",
    "Step 5: Understand style hierarchy (core < theme < user)",
    "Step 6: Add preset to settings.typography.fontSizes or fontFamilies",
    "Step 7: Include slug, name, and size/fontFamily properties",
    "Step 8: Verify preset appears in Site Editor typography settings",
    "Step 9: Note that user overrides may hide theme changes"
  ],
  "success_criteria": [
    "Locates correct theme.json file",
    "Adds preset to settings.typography section",
    "Uses correct preset structure (slug, name, value)",
    "Explains style hierarchy and user overrides",
    "Provides verification in Site Editor"
  ]
}
```

## File: `eval/scenarios/triage-output-contract.json`
```json
{
  "name": "Triage output contract validation",
  "skills": ["wp-project-triage"],
  "query": "Run the WordPress project triage and summarize what kind of repo this is and what commands to run first.",
  "expected_behavior": [
    "Step 1: Run triage script: node skills/wp-project-triage/scripts/detect_wp_project.mjs",
    "Step 2: Parse JSON output from script",
    "Step 3: Report project.kind and project.primary fields",
    "Step 4: Report signals with discovered paths and key indicators",
    "Step 5: Report tooling section (php/node/tests)",
    "Step 6: Report recommendations.commands for next steps"
  ],
  "success_criteria": [
    "Triage script is executed",
    "JSON output includes project.kind and project.primary",
    "JSON output includes signals section",
    "JSON output includes tooling section",
    "JSON output includes recommendations.commands",
    "Summary provided to user based on triage output"
  ]
}
```

## File: `eval/scenarios/upstream-sync-indices.json`
```json
{
  "name": "Upstream indices update",
  "skills": [],
  "query": "Update the repository's upstream indices so they reflect the latest WordPress and Gutenberg releases.",
  "expected_behavior": [
    "Step 1: Run update script: node shared/scripts/update-upstream-indices.mjs",
    "Step 2: Verify script fetches from WordPress.org and GitHub APIs",
    "Step 3: Confirm output written to shared/references/wordpress-core-versions.json",
    "Step 4: Confirm output written to shared/references/gutenberg-releases.json",
    "Step 5: Confirm output written to shared/references/wp-gutenberg-version-map.json",
    "Step 6: Verify deterministic output (stable formatting)",
    "Step 7: Verify limited list sizes for performance"
  ],
  "success_criteria": [
    "Update script runs successfully",
    "All three JSON files updated in shared/references/",
    "Output is deterministic and stable",
    "List sizes are limited for performance",
    "Data reflects latest upstream releases"
  ]
}
```

## File: `eval/scenarios/wpcli-multisite-targeting.json`
```json
{
  "name": "Multisite targeting guardrails",
  "skills": ["wordpress-router", "wp-project-triage", "wp-wpcli-and-ops"],
  "query": "This is a multisite. I need to update one site's home option without changing the whole network. How should I run WP-CLI?",
  "expected_behavior": [
    "Step 1: Run wordpress-router to classify repo kind",
    "Step 2: Run wp-project-triage to detect multisite configuration",
    "Step 3: Route to wp-wpcli-and-ops skill",
    "Step 4: Require --url=<site-url> flag for site-scoped operations",
    "Step 5: Warn against network-wide operations when targeting single site",
    "Step 6: Show correct command: wp option update home 'value' --url=site.example.com",
    "Step 7: Explain difference between --url (site-scoped) and --network (all sites)",
    "Step 8: Recommend verifying target site before running destructive commands"
  ],
  "success_criteria": [
    "Routes to wp-wpcli-and-ops skill",
    "Requires --url flag for site-scoped operations",
    "Warns against unintended network-wide changes",
    "Explains --url vs --network difference",
    "Shows correct command syntax"
  ]
}
```

## File: `eval/scenarios/wpcli-safe-search-replace.json`
```json
{
  "name": "Safe search-replace workflow",
  "skills": ["wordpress-router", "wp-project-triage", "wp-wpcli-and-ops"],
  "query": "We're migrating a WordPress site from http://old.example to https://new.example. Give a safe WP-CLI workflow.",
  "expected_behavior": [
    "Step 1: Run wordpress-router to classify repo kind",
    "Step 2: Run wp-project-triage to detect WP-CLI availability",
    "Step 3: Route to wp-wpcli-and-ops skill",
    "Step 4: Recommend backup first: wp db export backup.sql",
    "Step 5: Run dry-run: wp search-replace 'http://old.example' 'https://new.example' --dry-run",
    "Step 6: Review dry-run output for affected tables/rows",
    "Step 7: Execute actual search-replace after confirmation",
    "Step 8: Mention multisite targeting with --url or --network flags",
    "Step 9: Flush cache: wp cache flush",
    "Step 10: Flush rewrite rules: wp rewrite flush"
  ],
  "success_criteria": [
    "Backup recommended before any changes",
    "Dry-run executed first",
    "Multisite considerations mentioned",
    "Cache and rewrite flush recommended after",
    "Protocol change (http to https) handled correctly"
  ]
}
```

## File: `shared/references/.gitkeep`
```

```

## File: `shared/references/gutenberg-releases.json`
```json
{
  "source": "https://api.github.com/repos/WordPress/gutenberg/releases?per_page=50",
  "latest": {
    "tag": "v22.3.0",
    "name": "22.3.0",
    "publishedAt": "2025-12-17T16:27:03Z",
    "url": "https://github.com/WordPress/gutenberg/releases/tag/v22.3.0"
  },
  "recent": [
    {
      "tag": "v22.3.0",
      "name": "22.3.0",
      "publishedAt": "2025-12-17T16:27:03Z",
      "url": "https://github.com/WordPress/gutenberg/releases/tag/v22.3.0"
    },
    {
      "tag": "v22.2.0",
      "name": "22.2.0",
      "publishedAt": "2025-12-03T14:59:49Z",
      "url": "https://github.com/WordPress/gutenberg/releases/tag/v22.2.0"
    },
    {
      "tag": "v22.1.3",
      "name": "22.1.3",
      "publishedAt": "2025-12-03T11:11:38Z",
      "url": "https://github.com/WordPress/gutenberg/releases/tag/v22.1.3"
    },
    {
      "tag": "v22.1.2",
      "name": "22.1.2",
      "publishedAt": "2025-11-24T15:57:29Z",
      "url": "https://github.com/WordPress/gutenberg/releases/tag/v22.1.2"
    },
    {
      "tag": "v22.1.1",
      "name": "22.1.1",
      "publishedAt": "2025-11-21T12:20:00Z",
      "url": "https://github.com/WordPress/gutenberg/releases/tag/v22.1.1"
    },
    {
      "tag": "v22.1.0",
      "name": "22.1.0",
      "publishedAt": "2025-11-19T13:22:12Z",
      "url": "https://github.com/WordPress/gutenberg/releases/tag/v22.1.0"
    },
    {
      "tag": "v22.0.0",
      "name": "22.0.0",
      "publishedAt": "2025-11-05T15:02:43Z",
      "url": "https://github.com/WordPress/gutenberg/releases/tag/v22.0.0"
    },
    {
      "tag": "v21.9.0",
      "name": "21.9.0",
      "publishedAt": "2025-10-22T14:56:49Z",
      "url": "https://github.com/WordPress/gutenberg/releases/tag/v21.9.0"
    },
    {
      "tag": "v21.8.2",
      "name": "21.8.2",
      "publishedAt": "2025-10-16T11:30:44Z",
      "url": "https://github.com/WordPress/gutenberg/releases/tag/v21.8.2"
    },
    {
      "tag": "v21.8.1",
      "name": "21.8.1",
      "publishedAt": "2025-10-14T18:04:28Z",
      "url": "https://github.com/WordPress/gutenberg/releases/tag/v21.8.1"
    },
    {
      "tag": "v21.8.0",
      "name": "21.8.0",
      "publishedAt": "2025-10-08T16:02:57Z",
      "url": "https://github.com/WordPress/gutenberg/releases/tag/v21.8.0"
    },
    {
      "tag": "v21.7.0",
      "name": "21.7.0",
      "publishedAt": "2025-09-24T16:18:26Z",
      "url": "https://github.com/WordPress/gutenberg/releases/tag/v21.7.0"
    },
    {
      "tag": "v21.6.0",
      "name": "21.6.0",
      "publishedAt": "2025-09-10T10:27:37Z",
      "url": "https://github.com/WordPress/gutenberg/releases/tag/v21.6.0"
    },
    {
      "tag": "v21.5.0",
      "name": "21.5.0",
      "publishedAt": "2025-08-27T09:50:59Z",
      "url": "https://github.com/WordPress/gutenberg/releases/tag/v21.5.0"
    },
    {
      "tag": "v21.4.0",
      "name": "21.4.0",
      "publishedAt": "2025-08-13T15:08:29Z",
      "url": "https://github.com/WordPress/gutenberg/releases/tag/v21.4.0"
    },
    {
      "tag": "v21.3.0",
      "name": "21.3.0",
      "publishedAt": "2025-07-30T11:24:37Z",
      "url": "https://github.com/WordPress/gutenberg/releases/tag/v21.3.0"
    },
    {
      "tag": "v21.2.0",
      "name": "21.2.0",
      "publishedAt": "2025-07-16T17:13:59Z",
      "url": "https://github.com/WordPress/gutenberg/releases/tag/v21.2.0"
    },
    {
      "tag": "v21.1.1",
      "name": "21.1.1",
      "publishedAt": "2025-07-09T08:32:21Z",
      "url": "https://github.com/WordPress/gutenberg/releases/tag/v21.1.1"
    },
    {
      "tag": "v21.1.0",
      "name": "21.1.0",
      "publishedAt": "2025-07-02T08:36:42Z",
      "url": "https://github.com/WordPress/gutenberg/releases/tag/v21.1.0"
    },
    {
      "tag": "v21.0.0",
      "name": "21.0.0",
      "publishedAt": "2025-06-11T11:21:36Z",
      "url": "https://github.com/WordPress/gutenberg/releases/tag/v21.0.0"
    },
    {
      "tag": "v20.9.0",
      "name": "20.9.0",
      "publishedAt": "2025-05-28T14:40:23Z",
      "url": "https://github.com/WordPress/gutenberg/releases/tag/v20.9.0"
    },
    {
      "tag": "v20.8.0",
      "name": "20.8.0",
      "publishedAt": "2025-05-14T10:08:51Z",
      "url": "https://github.com/WordPress/gutenberg/releases/tag/v20.8.0"
    },
    {
      "tag": "v20.7.0",
      "name": "20.7.0",
      "publishedAt": "2025-04-22T11:44:36Z",
      "url": "https://github.com/WordPress/gutenberg/releases/tag/v20.7.0"
    },
    {
      "tag": "v20.6.0",
      "name": "20.6.0",
      "publishedAt": "2025-04-03T11:40:39Z",
      "url": "https://github.com/WordPress/gutenberg/releases/tag/v20.6.0"
    }
  ]
}
```

## File: `shared/references/wordpress-core-versions.json`
```json
{
  "source": "https://api.wordpress.org/core/version-check/1.7/",
  "latest": "6.9",
  "recent": [
    "6.9",
    "6.8.3",
    "6.7.4",
    "6.6.4",
    "6.5.7",
    "6.4.7",
    "6.3.7",
    "6.2.8",
    "6.1.9",
    "6.0.11",
    "5.9.12",
    "5.8.12",
    "5.7.14",
    "5.6.16",
    "5.5.17",
    "5.4.18",
    "5.3.20",
    "5.2.23",
    "5.1.21",
    "5.0.24"
  ],
  "offers": [
    {
      "version": "6.9",
      "current": "6.9",
      "download": "https://downloads.wordpress.org/release/wordpress-6.9.zip",
      "phpVersion": "7.2.24",
      "mysqlVersion": "5.5.5",
      "response": "upgrade",
      "locale": "en_US"
    },
    {
      "version": "6.8.3",
      "current": "6.8.3",
      "download": "https://downloads.w.org/release/wordpress-6.8.3.zip",
      "phpVersion": "7.2.24",
      "mysqlVersion": "5.5.5",
      "response": "autoupdate",
      "locale": "en_US"
    },
    {
      "version": "6.7.4",
      "current": "6.7.4",
      "download": "https://downloads.w.org/release/wordpress-6.7.4.zip",
      "phpVersion": "7.2.24",
      "mysqlVersion": "5.5.5",
      "response": "autoupdate",
      "locale": "en_US"
    },
    {
      "version": "6.6.4",
      "current": "6.6.4",
      "download": "https://downloads.w.org/release/wordpress-6.6.4.zip",
      "phpVersion": "7.2.24",
      "mysqlVersion": "5.5.5",
      "response": "autoupdate",
      "locale": "en_US"
    },
    {
      "version": "6.5.7",
      "current": "6.5.7",
      "download": "https://downloads.w.org/release/wordpress-6.5.7.zip",
      "phpVersion": "7.0.0",
      "mysqlVersion": "5.5.5",
      "response": "autoupdate",
      "locale": "en_US"
    },
    {
      "version": "6.4.7",
      "current": "6.4.7",
      "download": "https://downloads.w.org/release/wordpress-6.4.7.zip",
      "phpVersion": "7.0.0",
      "mysqlVersion": "5.0",
      "response": "autoupdate",
      "locale": "en_US"
    },
    {
      "version": "6.3.7",
      "current": "6.3.7",
      "download": "https://downloads.w.org/release/wordpress-6.3.7.zip",
      "phpVersion": "7.0.0",
      "mysqlVersion": "5.0",
      "response": "autoupdate",
      "locale": "en_US"
    },
    {
      "version": "6.2.8",
      "current": "6.2.8",
      "download": "https://downloads.w.org/release/wordpress-6.2.8.zip",
      "phpVersion": "5.6.20",
      "mysqlVersion": "5.0",
      "response": "autoupdate",
      "locale": "en_US"
    },
    {
      "version": "6.1.9",
      "current": "6.1.9",
      "download": "https://downloads.w.org/release/wordpress-6.1.9.zip",
      "phpVersion": "5.6.20",
      "mysqlVersion": "5.0",
      "response": "autoupdate",
      "locale": "en_US"
    },
    {
      "version": "6.0.11",
      "current": "6.0.11",
      "download": "https://downloads.w.org/release/wordpress-6.0.11.zip",
      "phpVersion": "5.6.20",
      "mysqlVersion": "5.0",
      "response": "autoupdate",
      "locale": "en_US"
    },
    {
      "version": "5.9.12",
      "current": "5.9.12",
      "download": "https://downloads.w.org/release/wordpress-5.9.12.zip",
      "phpVersion": "5.6.20",
      "mysqlVersion": "5.0",
      "response": "autoupdate",
      "locale": "en_US"
    },
    {
      "version": "5.8.12",
      "current": "5.8.12",
      "download": "https://downloads.w.org/release/wordpress-5.8.12.zip",
      "phpVersion": "5.6.20",
      "mysqlVersion": "5.0",
      "response": "autoupdate",
      "locale": "en_US"
    },
    {
      "version": "5.7.14",
      "current": "5.7.14",
      "download": "https://downloads.w.org/release/wordpress-5.7.14.zip",
      "phpVersion": "5.6.20",
      "mysqlVersion": "5.0",
      "response": "autoupdate",
      "locale": "en_US"
    },
    {
      "version": "5.6.16",
      "current": "5.6.16",
      "download": "https://downloads.w.org/release/wordpress-5.6.16.zip",
      "phpVersion": "5.6.20",
      "mysqlVersion": "5.0",
      "response": "autoupdate",
      "locale": "en_US"
    },
    {
      "version": "5.5.17",
      "current": "5.5.17",
      "download": "https://downloads.w.org/release/wordpress-5.5.17.zip",
      "phpVersion": "5.6.20",
      "mysqlVersion": "5.0",
      "response": "autoupdate",
      "locale": "en_US"
    },
    {
      "version": "5.4.18",
      "current": "5.4.18",
      "download": "https://downloads.w.org/release/wordpress-5.4.18.zip",
      "phpVersion": "5.6.20",
      "mysqlVersion": "5.0",
      "response": "autoupdate",
      "locale": "en_US"
    },
    {
      "version": "5.3.20",
      "current": "5.3.20",
      "download": "https://downloads.w.org/release/wordpress-5.3.20.zip",
      "phpVersion": "5.6.20",
      "mysqlVersion": "5.0",
      "response": "autoupdate",
      "locale": "en_US"
    },
    {
      "version": "5.2.23",
      "current": "5.2.23",
      "download": "https://downloads.w.org/release/wordpress-5.2.23.zip",
      "phpVersion": "5.6.20",
      "mysqlVersion": "5.0",
      "response": "autoupdate",
      "locale": "en_US"
    },
    {
      "version": "5.1.21",
      "current": "5.1.21",
      "download": "https://downloads.w.org/release/wordpress-5.1.21.zip",
      "phpVersion": "5.2.4",
      "mysqlVersion": "5.0",
      "response": "autoupdate",
      "locale": "en_US"
    },
    {
      "version": "5.0.24",
      "current": "5.0.24",
      "download": "https://downloads.w.org/release/wordpress-5.0.24.zip",
      "phpVersion": "5.2.4",
      "mysqlVersion": "5.0",
      "response": "autoupdate",
      "locale": "en_US"
    }
  ]
}
```

## File: `shared/references/wp-gutenberg-version-map.json`
```json
{
  "source": "https://developer.wordpress.org/block-editor/contributors/versions-in-wordpress/",
  "note": null,
  "rows": [
    {
      "wordpress": "20.5-21.9",
      "gutenberg": "6.9"
    },
    {
      "wordpress": "19.4-20.4",
      "gutenberg": "6.8.3"
    },
    {
      "wordpress": "19.4-20.4",
      "gutenberg": "6.8.2"
    },
    {
      "wordpress": "19.4-20.4",
      "gutenberg": "6.8.1"
    },
    {
      "wordpress": "19.4-20.4",
      "gutenberg": "6.8"
    },
    {
      "wordpress": "18.6-19.3",
      "gutenberg": "6.7.2"
    },
    {
      "wordpress": "18.6-19.3",
      "gutenberg": "6.7.1"
    },
    {
      "wordpress": "18.6-19.3",
      "gutenberg": "6.7"
    },
    {
      "wordpress": "17.8-18.5",
      "gutenberg": "6.6.2"
    },
    {
      "wordpress": "17.8-18.5",
      "gutenberg": "6.6.1"
    },
    {
      "wordpress": "17.8-18.5",
      "gutenberg": "6.6"
    },
    {
      "wordpress": "16.8-17.7",
      "gutenberg": "6.5.5"
    },
    {
      "wordpress": "16.8-17.7",
      "gutenberg": "6.5.4"
    },
    {
      "wordpress": "16.8-17.7",
      "gutenberg": "6.5.3"
    },
    {
      "wordpress": "16.8-17.7",
      "gutenberg": "6.5.2"
    },
    {
      "wordpress": "16.8-17.7",
      "gutenberg": "6.5"
    },
    {
      "wordpress": "16.2-16.7",
      "gutenberg": "6.4.4"
    },
    {
      "wordpress": "16.2-16.7",
      "gutenberg": "6.4.5"
    },
    {
      "wordpress": "16.2-16.7",
      "gutenberg": "6.4.3"
    },
    {
      "wordpress": "16.2-16.7",
      "gutenberg": "6.4.2"
    },
    {
      "wordpress": "16.2-16.7",
      "gutenberg": "6.4.1"
    },
    {
      "wordpress": "16.2-16.7",
      "gutenberg": "6.4"
    },
    {
      "wordpress": "15.2-16.1",
      "gutenberg": "6.3.5"
    },
    {
      "wordpress": "15.2-16.1",
      "gutenberg": "6.3.4"
    },
    {
      "wordpress": "15.2-16.1",
      "gutenberg": "6.3.3"
    },
    {
      "wordpress": "15.2-16.1",
      "gutenberg": "6.3.2"
    },
    {
      "wordpress": "15.2-16.1",
      "gutenberg": "6.3.1"
    },
    {
      "wordpress": "15.2-16.1",
      "gutenberg": "6.3"
    },
    {
      "wordpress": "14.2-15.1",
      "gutenberg": "6.2.6"
    },
    {
      "wordpress": "14.2-15.1",
      "gutenberg": "6.2.5"
    },
    {
      "wordpress": "14.2-15.1",
      "gutenberg": "6.2.4"
    },
    {
      "wordpress": "14.2-15.1",
      "gutenberg": "6.2.3"
    },
    {
      "wordpress": "14.2-15.1",
      "gutenberg": "6.2.2"
    },
    {
      "wordpress": "14.2-15.1",
      "gutenberg": "6.2.1"
    },
    {
      "wordpress": "14.2-15.1",
      "gutenberg": "6.2"
    },
    {
      "wordpress": "13.1-14.1",
      "gutenberg": "6.1.7"
    },
    {
      "wordpress": "13.1-14.1",
      "gutenberg": "6.1.6"
    },
    {
      "wordpress": "13.1-14.1",
      "gutenberg": "6.1.5"
    },
    {
      "wordpress": "13.1-14.1",
      "gutenberg": "6.1.4"
    },
    {
      "wordpress": "13.1-14.1",
      "gutenberg": "6.1.3"
    },
    {
      "wordpress": "13.1-14.1",
      "gutenberg": "6.1.2"
    },
    {
      "wordpress": "13.1-14.1",
      "gutenberg": "6.1.1"
    },
    {
      "wordpress": "13.1-14.1",
      "gutenberg": "6.1"
    },
    {
      "wordpress": "12.0-13.0",
      "gutenberg": "6.0.9"
    },
    {
      "wordpress": "12.0-13.0",
      "gutenberg": "6.0.8"
    },
    {
      "wordpress": "12.0-13.0",
      "gutenberg": "6.0.7"
    },
    {
      "wordpress": "12.0-13.0",
      "gutenberg": "6.0.6"
    },
    {
      "wordpress": "12.0-13.0",
      "gutenberg": "6.0.5"
    },
    {
      "wordpress": "12.0-13.0",
      "gutenberg": "6.0.4"
    },
    {
      "wordpress": "12.0-13.0",
      "gutenberg": "6.0.3"
    },
    {
      "wordpress": "12.0-13.0",
      "gutenberg": "6.0.2"
    },
    {
      "wordpress": "12.0-13.0",
      "gutenberg": "6.0.1"
    },
    {
      "wordpress": "12.0-13.0",
      "gutenberg": "6.0"
    },
    {
      "wordpress": "10.8-11.9",
      "gutenberg": "5.9.10"
    },
    {
      "wordpress": "10.8-11.9",
      "gutenberg": "5.9.9"
    },
    {
      "wordpress": "10.8-11.9",
      "gutenberg": "5.9.8"
    },
    {
      "wordpress": "10.8-11.9",
      "gutenberg": "5.9.7"
    },
    {
      "wordpress": "10.8-11.9",
      "gutenberg": "5.9.6"
    },
    {
      "wordpress": "10.8-11.9",
      "gutenberg": "5.9.5"
    },
    {
      "wordpress": "10.8-11.9",
      "gutenberg": "5.9.4"
    },
    {
      "wordpress": "10.8-11.9",
      "gutenberg": "5.9.3"
    },
    {
      "wordpress": "10.8-11.9",
      "gutenberg": "5.9.2"
    },
    {
      "wordpress": "10.8-11.9",
      "gutenberg": "5.9.1"
    },
    {
      "wordpress": "10.8-11.9",
      "gutenberg": "5.9"
    },
    {
      "wordpress": "10.0-10.7",
      "gutenberg": "5.8.10"
    },
    {
      "wordpress": "10.0-10.7",
      "gutenberg": "5.8.9"
    },
    {
      "wordpress": "10.0-10.7",
      "gutenberg": "5.8.8"
    },
    {
      "wordpress": "10.0-10.7",
      "gutenberg": "5.8.7"
    },
    {
      "wordpress": "10.0-10.7",
      "gutenberg": "5.8.6"
    },
    {
      "wordpress": "10.0-10.7",
      "gutenberg": "5.8.5"
    },
    {
      "wordpress": "10.0-10.7",
      "gutenberg": "5.8.4"
    },
    {
      "wordpress": "10.0-10.7",
      "gutenberg": "5.8.3"
    },
    {
      "wordpress": "10.0-10.7",
      "gutenberg": "5.8.2"
    },
    {
      "wordpress": "10.0-10.7",
      "gutenberg": "5.8.1"
    },
    {
      "wordpress": "10.0-10.7",
      "gutenberg": "5.8"
    },
    {
      "wordpress": "9.3-9.9",
      "gutenberg": "5.7.12"
    },
    {
      "wordpress": "9.3-9.9",
      "gutenberg": "5.7.11"
    },
    {
      "wordpress": "9.3-9.9",
      "gutenberg": "5.7.10"
    },
    {
      "wordpress": "9.3-9.9",
      "gutenberg": "5.7.9"
    },
    {
      "wordpress": "9.3-9.9",
      "gutenberg": "5.7.8"
    },
    {
      "wordpress": "9.3-9.9",
      "gutenberg": "5.7.7"
    },
    {
      "wordpress": "9.3-9.9",
      "gutenberg": "5.7.6"
    },
    {
      "wordpress": "9.3-9.9",
      "gutenberg": "5.7.5"
    },
    {
      "wordpress": "9.3-9.9",
      "gutenberg": "5.7.4"
    },
    {
      "wordpress": "9.3-9.9",
      "gutenberg": "5.7.3"
    },
    {
      "wordpress": "9.3-9.9",
      "gutenberg": "5.7.2"
    },
    {
      "wordpress": "9.3-9.9",
      "gutenberg": "5.7.1"
    },
    {
      "wordpress": "9.3-9.9",
      "gutenberg": "5.7"
    },
    {
      "wordpress": "8.6-9.2",
      "gutenberg": "5.6.14"
    },
    {
      "wordpress": "8.6-9.2",
      "gutenberg": "5.6.13"
    },
    {
      "wordpress": "8.6-9.2",
      "gutenberg": "5.6.12"
    },
    {
      "wordpress": "8.6-9.2",
      "gutenberg": "5.6.11"
    },
    {
      "wordpress": "8.6-9.2",
      "gutenberg": "5.6.10"
    },
    {
      "wordpress": "8.6-9.2",
      "gutenberg": "5.6.9"
    },
    {
      "wordpress": "8.6-9.2",
      "gutenberg": "5.6.8"
    },
    {
      "wordpress": "8.6-9.2",
      "gutenberg": "5.6.7"
    },
    {
      "wordpress": "8.6-9.2",
      "gutenberg": "5.6.6"
    },
    {
      "wordpress": "8.6-9.2",
      "gutenberg": "5.6.5"
    },
    {
      "wordpress": "8.6-9.2",
      "gutenberg": "5.6.4"
    },
    {
      "wordpress": "8.6-9.2",
      "gutenberg": "5.6.3"
    },
    {
      "wordpress": "8.6-9.2",
      "gutenberg": "5.6.2"
    },
    {
      "wordpress": "8.6-9.2",
      "gutenberg": "5.6.1"
    },
    {
      "wordpress": "8.6-9.2",
      "gutenberg": "5.6"
    },
    {
      "wordpress": "7.6-8.5",
      "gutenberg": "5.5.15"
    },
    {
      "wordpress": "7.6-8.5",
      "gutenberg": "5.5.14"
    },
    {
      "wordpress": "7.6-8.5",
      "gutenberg": "5.5.13"
    },
    {
      "wordpress": "7.6-8.5",
      "gutenberg": "5.5.12"
    },
    {
      "wordpress": "7.6-8.5",
      "gutenberg": "5.5.11"
    },
    {
      "wordpress": "7.6-8.5",
      "gutenberg": "5.5.10"
    },
    {
      "wordpress": "7.6-8.5",
      "gutenberg": "5.5.9"
    },
    {
      "wordpress": "7.6-8.5",
      "gutenberg": "5.5.8"
    },
    {
      "wordpress": "7.6-8.5",
      "gutenberg": "5.5.7"
    },
    {
      "wordpress": "7.6-8.5",
      "gutenberg": "5.5.6"
    },
    {
      "wordpress": "7.6-8.5",
      "gutenberg": "5.5.5"
    },
    {
      "wordpress": "7.6-8.5",
      "gutenberg": "5.5.4"
    },
    {
      "wordpress": "7.6-8.5",
      "gutenberg": "5.5.3"
    },
    {
      "wordpress": "7.6-8.5",
      "gutenberg": "5.5.2"
    },
    {
      "wordpress": "7.6-8.5",
      "gutenberg": "5.5.1"
    },
    {
      "wordpress": "7.6-8.5",
      "gutenberg": "5.5"
    },
    {
      "wordpress": "6.6-7.5",
      "gutenberg": "5.4.16"
    },
    {
      "wordpress": "6.6-7.5",
      "gutenberg": "5.4.15"
    },
    {
      "wordpress": "6.6-7.5",
      "gutenberg": "5.4.14"
    },
    {
      "wordpress": "6.6-7.5",
      "gutenberg": "5.4.13"
    },
    {
      "wordpress": "6.6-7.5",
      "gutenberg": "5.4.12"
    },
    {
      "wordpress": "6.6-7.5",
      "gutenberg": "5.4.11"
    },
    {
      "wordpress": "6.6-7.5",
      "gutenberg": "5.4.10"
    },
    {
      "wordpress": "6.6-7.5",
      "gutenberg": "5.4.9"
    },
    {
      "wordpress": "6.6-7.5",
      "gutenberg": "5.4.8"
    },
    {
      "wordpress": "6.6-7.5",
      "gutenberg": "5.4.7"
    },
    {
      "wordpress": "6.6-7.5",
      "gutenberg": "5.4.6"
    },
    {
      "wordpress": "6.6-7.5",
      "gutenberg": "5.4.5"
    },
    {
      "wordpress": "6.6-7.5",
      "gutenberg": "5.4.4"
    },
    {
      "wordpress": "6.6-7.5",
      "gutenberg": "5.4.3"
    },
    {
      "wordpress": "6.6-7.5",
      "gutenberg": "5.4.2"
    },
    {
      "wordpress": "6.6-7.5",
      "gutenberg": "5.4.1"
    },
    {
      "wordpress": "6.6-7.5",
      "gutenberg": "5.4"
    },
    {
      "wordpress": "5.5-6.5",
      "gutenberg": "5.3.18"
    },
    {
      "wordpress": "5.5-6.5",
      "gutenberg": "5.3.17"
    },
    {
      "wordpress": "5.5-6.5",
      "gutenberg": "5.3.16"
    },
    {
      "wordpress": "5.5-6.5",
      "gutenberg": "5.3.15"
    },
    {
      "wordpress": "5.5-6.5",
      "gutenberg": "5.3.14"
    },
    {
      "wordpress": "5.5-6.5",
      "gutenberg": "5.3.13"
    },
    {
      "wordpress": "5.5-6.5",
      "gutenberg": "5.3.12"
    },
    {
      "wordpress": "5.5-6.5",
      "gutenberg": "5.3.11"
    },
    {
      "wordpress": "5.5-6.5",
      "gutenberg": "5.3.10"
    },
    {
      "wordpress": "5.5-6.5",
      "gutenberg": "5.3.9"
    },
    {
      "wordpress": "5.5-6.5",
      "gutenberg": "5.3.8"
    },
    {
      "wordpress": "5.5-6.5",
      "gutenberg": "5.3.7"
    },
    {
      "wordpress": "5.5-6.5",
      "gutenberg": "5.3.6"
    },
    {
      "wordpress": "5.5-6.5",
      "gutenberg": "5.3.5"
    },
    {
      "wordpress": "5.5-6.5",
      "gutenberg": "5.3.4"
    },
    {
      "wordpress": "5.5-6.5",
      "gutenberg": "5.3.3"
    },
    {
      "wordpress": "5.5-6.5",
      "gutenberg": "5.3.2"
    },
    {
      "wordpress": "5.5-6.5",
      "gutenberg": "5.3.1"
    },
    {
      "wordpress": "5.5-6.5",
      "gutenberg": "5.3"
    },
    {
      "wordpress": "4.9-5.4",
      "gutenberg": "5.2.21"
    },
    {
      "wordpress": "4.9-5.4",
      "gutenberg": "5.2.20"
    },
    {
      "wordpress": "4.9-5.4",
      "gutenberg": "5.2.19"
    },
    {
      "wordpress": "4.9-5.4",
      "gutenberg": "5.2.18"
    },
    {
      "wordpress": "4.9-5.4",
      "gutenberg": "5.2.17"
    },
    {
      "wordpress": "4.9-5.4",
      "gutenberg": "5.2.16"
    },
    {
      "wordpress": "4.9-5.4",
      "gutenberg": "5.2.15"
    },
    {
      "wordpress": "4.9-5.4",
      "gutenberg": "5.2.14"
    },
    {
      "wordpress": "4.9-5.4",
      "gutenberg": "5.2.13"
    },
    {
      "wordpress": "4.9-5.4",
      "gutenberg": "5.2.12"
    },
    {
      "wordpress": "4.9-5.4",
      "gutenberg": "5.2.11"
    },
    {
      "wordpress": "4.9-5.4",
      "gutenberg": "5.2.10"
    },
    {
      "wordpress": "4.9-5.4",
      "gutenberg": "5.2.9"
    },
    {
      "wordpress": "4.9-5.4",
      "gutenberg": "5.2.8"
    },
    {
      "wordpress": "4.9-5.4",
      "gutenberg": "5.2.7"
    },
    {
      "wordpress": "4.9-5.4",
      "gutenberg": "5.2.6"
    },
    {
      "wordpress": "4.9-5.4",
      "gutenberg": "5.2.5"
    },
    {
      "wordpress": "4.9-5.4",
      "gutenberg": "5.2.4"
    },
    {
      "wordpress": "4.9-5.4",
      "gutenberg": "5.2.3"
    },
    {
      "wordpress": "4.9-5.4",
      "gutenberg": "5.2.2"
    },
    {
      "wordpress": "4.9-5.4",
      "gutenberg": "5.2.1"
    },
    {
      "wordpress": "4.9-5.4",
      "gutenberg": "5.2"
    },
    {
      "wordpress": "4.8",
      "gutenberg": "5.1.19"
    },
    {
      "wordpress": "4.8",
      "gutenberg": "5.1.18"
    },
    {
      "wordpress": "4.8",
      "gutenberg": "5.1.17"
    },
    {
      "wordpress": "4.8",
      "gutenberg": "5.1.16"
    },
    {
      "wordpress": "4.8",
      "gutenberg": "5.1.15"
    },
    {
      "wordpress": "4.8",
      "gutenberg": "5.1.14"
    },
    {
      "wordpress": "4.8",
      "gutenberg": "5.1.13"
    },
    {
      "wordpress": "4.8",
      "gutenberg": "5.1.12"
    },
    {
      "wordpress": "4.8",
      "gutenberg": "5.1.11"
    },
    {
      "wordpress": "4.8",
      "gutenberg": "5.1.10"
    },
    {
      "wordpress": "4.8",
      "gutenberg": "5.1.9"
    },
    {
      "wordpress": "4.8",
      "gutenberg": "5.1.8"
    },
    {
      "wordpress": "4.8",
      "gutenberg": "5.1.7"
    },
    {
      "wordpress": "4.8",
      "gutenberg": "5.1.6"
    },
    {
      "wordpress": "4.8",
      "gutenberg": "5.1.5"
    },
    {
      "wordpress": "4.8",
      "gutenberg": "5.1.4"
    },
    {
      "wordpress": "4.8",
      "gutenberg": "5.1.3"
    },
    {
      "wordpress": "4.8",
      "gutenberg": "5.1.2"
    },
    {
      "wordpress": "4.8",
      "gutenberg": "5.1.1"
    },
    {
      "wordpress": "4.8",
      "gutenberg": "5.1"
    },
    {
      "wordpress": "4.7.1",
      "gutenberg": "5.0.22"
    },
    {
      "wordpress": "4.7.1",
      "gutenberg": "5.0.21"
    },
    {
      "wordpress": "4.7.1",
      "gutenberg": "5.0.20"
    },
    {
      "wordpress": "4.7.1",
      "gutenberg": "5.0.19"
    },
    {
      "wordpress": "4.7.1",
      "gutenberg": "5.0.18"
    },
    {
      "wordpress": "4.7.1",
      "gutenberg": "5.0.17"
    },
    {
      "wordpress": "4.7.1",
      "gutenberg": "5.0.16"
    },
    {
      "wordpress": "4.7.1",
      "gutenberg": "5.0.15"
    },
    {
      "wordpress": "4.7.1",
      "gutenberg": "5.0.14"
    },
    {
      "wordpress": "4.7.1",
      "gutenberg": "5.0.13"
    },
    {
      "wordpress": "4.7.1",
      "gutenberg": "5.0.12"
    },
    {
      "wordpress": "4.7.1",
      "gutenberg": "5.0.11"
    },
    {
      "wordpress": "4.7.1",
      "gutenberg": "5.0.10"
    },
    {
      "wordpress": "4.7.1",
      "gutenberg": "5.0.9"
    },
    {
      "wordpress": "4.7.1",
      "gutenberg": "5.0.8"
    },
    {
      "wordpress": "4.7.1",
      "gutenberg": "5.0.7"
    },
    {
      "wordpress": "4.7.1",
      "gutenberg": "5.0.6"
    },
    {
      "wordpress": "4.7.1",
      "gutenberg": "5.0.5"
    },
    {
      "wordpress": "4.7.1",
      "gutenberg": "5.0.4"
    },
    {
      "wordpress": "4.7.1",
      "gutenberg": "5.0.3"
    },
    {
      "wordpress": "4.7.0",
      "gutenberg": "5.0.2"
    },
    {
      "wordpress": "4.6.1",
      "gutenberg": "5.0.1"
    },
    {
      "wordpress": "4.6.1",
      "gutenberg": "5.0"
    }
  ]
}
```

## File: `shared/scripts/ai-generate-updates.mjs`
```
/**
 * AI-powered skill update generator
 *
 * Analyzes upstream changes and generates updates to affected skills.
 * Designed to run in GitHub Actions with ANTHROPIC_API_KEY env var.
 *
 * Usage:
 *   node shared/scripts/ai-generate-updates.mjs
 *
 * Environment:
 *   ANTHROPIC_API_KEY - Required
 *   AI_DRY_RUN        - Set to "true" to skip writing files
 */

import Anthropic from "@anthropic-ai/sdk";
import fs from "node:fs";
import path from "node:path";

const REPO_ROOT = process.cwd();
const REFERENCES_DIR = path.join(REPO_ROOT, "shared", "references");
const SKILLS_DIR = path.join(REPO_ROOT, "skills");
const STATE_FILE = path.join(REPO_ROOT, ".github", "state", "last-sync.json");

// Model selection: Sonnet 4 for balanced cost/performance
const MODEL = "claude-sonnet-4-20250514";

/**
 * Load JSON file safely
 */
function loadJson(filePath) {
  try {
    return JSON.parse(fs.readFileSync(filePath, "utf8"));
  } catch {
    return null;
  }
}

/**
 * Write JSON file with directory creation
 */
function writeJson(filePath, data) {
  fs.mkdirSync(path.dirname(filePath), { recursive: true });
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2) + "\n", "utf8");
}

/**
 * Get current upstream state hash for comparison
 */
function getUpstreamStateHash(indices) {
  const state = {
    wpLatest: indices.wordpress?.latest ?? null,
    gbLatest: indices.gutenberg?.latest?.tag ?? null,
    gbRecentCount: indices.gutenberg?.recent?.length ?? 0,
    mapRowCount: indices.map?.rows?.length ?? 0,
  };
  // Simple hash: JSON stringify and take first 16 chars of base64
  const hash = Buffer.from(JSON.stringify(state)).toString("base64").slice(0, 16);
  return { hash, state };
}

/**
 * Load all current upstream indices
 */
function loadUpstreamIndices() {
  return {
    wordpress: loadJson(path.join(REFERENCES_DIR, "wordpress-core-versions.json")),
    gutenberg: loadJson(path.join(REFERENCES_DIR, "gutenberg-releases.json")),
    map: loadJson(path.join(REFERENCES_DIR, "wp-gutenberg-version-map.json")),
  };
}

/**
 * Load last sync state
 */
function loadLastSyncState() {
  return loadJson(STATE_FILE) ?? { hash: null, state: null, lastSync: null };
}

/**
 * Save current sync state
 */
function saveSyncState(hash, state, changes) {
  writeJson(STATE_FILE, {
    hash,
    state,
    lastSync: new Date().toISOString(),
    lastChanges: changes,
  });
}

/**
 * Detect what changed between last sync and current state
 */
function detectChanges(lastState, currentState) {
  const changes = [];

  if (!lastState.state) {
    changes.push({
      type: "initial-sync",
      description: "First sync - no previous state",
      riskLevel: "low",
    });
    return changes;
  }

  const last = lastState.state;
  const current = currentState.state;

  // WordPress version change
  if (last.wpLatest !== current.wpLatest) {
    changes.push({
      type: "wordpress-release",
      description: `WordPress updated: ${last.wpLatest} → ${current.wpLatest}`,
      oldVersion: last.wpLatest,
      newVersion: current.wpLatest,
      riskLevel: "medium",
      affectedSkills: [
        "wp-block-themes",
        "wp-block-development",
        "wp-plugin-development",
      ],
    });
  }

  // Gutenberg version change
  if (last.gbLatest !== current.gbLatest) {
    changes.push({
      type: "gutenberg-release",
      description: `Gutenberg updated: ${last.gbLatest} → ${current.gbLatest}`,
      oldVersion: last.gbLatest,
      newVersion: current.gbLatest,
      riskLevel: "medium",
      affectedSkills: [
        "wp-interactivity-api",
        "wp-abilities-api",
        "wp-block-development",
      ],
    });
  }

  // Map table updated (new mappings added)
  if (last.mapRowCount !== current.mapRowCount) {
    changes.push({
      type: "version-map-update",
      description: `WP↔Gutenberg mapping updated: ${last.mapRowCount} → ${current.mapRowCount} entries`,
      riskLevel: "low",
      affectedSkills: ["wordpress-router"],
    });
  }

  return changes;
}

/**
 * Load a skill's SKILL.md content
 */
function loadSkillContent(skillName) {
  const skillPath = path.join(SKILLS_DIR, skillName, "SKILL.md");
  try {
    return fs.readFileSync(skillPath, "utf8");
  } catch {
    return null;
  }
}

/**
 * Load all reference docs for a skill
 */
function loadSkillReferences(skillName) {
  const refsDir = path.join(SKILLS_DIR, skillName, "references");
  const refs = {};
  try {
    const files = fs.readdirSync(refsDir);
    for (const file of files) {
      if (file.endsWith(".md")) {
        refs[file] = fs.readFileSync(path.join(refsDir, file), "utf8");
      }
    }
  } catch {
    // No references dir
  }
  return refs;
}

/**
 * Build the prompt for AI analysis
 */
function buildAnalysisPrompt(changes, indices) {
  const changesSummary = changes
    .map((c) => `- ${c.type}: ${c.description} (risk: ${c.riskLevel})`)
    .join("\n");

  return `You are analyzing upstream changes to WordPress/Gutenberg to determine if skills need updates.

## Detected Changes
${changesSummary}

## Current Upstream State
- WordPress latest: ${indices.wordpress?.latest ?? "unknown"}
- Gutenberg latest: ${indices.gutenberg?.latest?.tag ?? "unknown"}
- Gutenberg release URL: ${indices.gutenberg?.latest?.url ?? "unknown"}

## Task
Analyze these changes and determine:
1. Which skills are likely affected and why
2. What specific updates might be needed (procedures, references, examples)
3. Risk assessment for each potential update

Respond in JSON format:
{
  "analysis": "Brief overall analysis",
  "skillUpdates": [
    {
      "skill": "skill-name",
      "reason": "Why this skill is affected",
      "suggestedChanges": ["List of specific changes to make"],
      "riskLevel": "low|medium|high",
      "priority": 1-5
    }
  ],
  "skipUpdate": true/false,
  "skipReason": "If skipping, explain why no updates are needed"
}`;
}

/**
 * Build prompt for generating skill updates
 */
function buildUpdatePrompt(skillName, skillContent, references, changes, indices) {
  const relevantChanges = changes.filter(
    (c) => c.affectedSkills?.includes(skillName)
  );

  const refsSummary = Object.entries(references)
    .map(([name, content]) => `### ${name}\n${content.slice(0, 2000)}...`)
    .join("\n\n");

  return `You are updating a WordPress development skill based on upstream changes.

## Skill: ${skillName}

## Current SKILL.md
${skillContent}

## Current References (truncated)
${refsSummary || "(no references)"}

## Relevant Changes
${relevantChanges.map((c) => `- ${c.description}`).join("\n")}

## Upstream Context
- WordPress latest: ${indices.wordpress?.latest ?? "unknown"}
- Gutenberg latest: ${indices.gutenberg?.latest?.tag ?? "unknown"}

## Instructions
1. Review the current skill content
2. Identify what needs to change based on the upstream updates
3. Generate updated content that:
   - Preserves the existing structure and tone
   - Updates version references if needed
   - Adds notes about new features/changes if relevant
   - Does NOT remove existing content unless it's deprecated

Respond in JSON format:
{
  "skillUpdated": true/false,
  "changes": [
    {
      "file": "SKILL.md or references/filename.md",
      "description": "What changed",
      "newContent": "Full new file content (only if changed)"
    }
  ],
  "summary": "Brief summary of changes for PR description",
  "noChangeReason": "If no changes needed, explain why"
}`;
}

/**
 * Call Claude API
 */
async function callClaude(client, prompt, systemPrompt = null) {
  const messages = [{ role: "user", content: prompt }];

  const response = await client.messages.create({
    model: MODEL,
    max_tokens: 8192,
    system: systemPrompt ?? "You are a technical writer maintaining WordPress development skills documentation. Always respond with valid JSON.",
    messages,
  });

  const text = response.content
    .filter((b) => b.type === "text")
    .map((b) => b.text)
    .join("");

  // Extract JSON from response (handle markdown code blocks)
  const jsonMatch = text.match(/```json\s*([\s\S]*?)\s*```/) ||
                    text.match(/```\s*([\s\S]*?)\s*```/) ||
                    [null, text];

  try {
    return JSON.parse(jsonMatch[1] || text);
  } catch (e) {
    console.error("Failed to parse Claude response as JSON:", text.slice(0, 500));
    throw new Error(`Invalid JSON response from Claude: ${e.message}`);
  }
}

/**
 * Main execution
 */
async function main() {
  const dryRun = process.env.AI_DRY_RUN === "true";

  if (!process.env.ANTHROPIC_API_KEY) {
    console.error("ERROR: ANTHROPIC_API_KEY environment variable is required");
    process.exit(1);
  }

  const client = new Anthropic();

  console.log("=== AI Skill Update Generator ===\n");

  // 1. Load current state
  console.log("Loading upstream indices...");
  const indices = loadUpstreamIndices();
  const currentState = getUpstreamStateHash(indices);
  const lastState = loadLastSyncState();

  console.log(`Current state hash: ${currentState.hash}`);
  console.log(`Last sync hash: ${lastState.hash ?? "(none)"}\n`);

  // 2. Detect changes
  console.log("Detecting changes...");
  const changes = detectChanges(lastState, currentState);

  if (changes.length === 0) {
    console.log("No changes detected. Exiting.");
    process.exit(0);
  }

  console.log(`Found ${changes.length} change(s):`);
  for (const c of changes) {
    console.log(`  - ${c.type}: ${c.description}`);
  }
  console.log();

  // 3. AI analysis of impact
  console.log("Analyzing impact with AI...");
  const analysisPrompt = buildAnalysisPrompt(changes, indices);
  const analysis = await callClaude(client, analysisPrompt);

  console.log(`Analysis: ${analysis.analysis}\n`);

  if (analysis.skipUpdate) {
    console.log(`Skipping updates: ${analysis.skipReason}`);
    saveSyncState(currentState.hash, currentState.state, changes);
    process.exit(0);
  }

  // 4. Generate updates for affected skills
  const updates = [];
  const skillsToUpdate = analysis.skillUpdates
    .filter((s) => s.priority >= 3 || s.riskLevel !== "low")
    .sort((a, b) => b.priority - a.priority);

  console.log(`Skills to update: ${skillsToUpdate.map((s) => s.skill).join(", ")}\n`);

  for (const skillUpdate of skillsToUpdate) {
    const { skill } = skillUpdate;
    console.log(`Processing ${skill}...`);

    const skillContent = loadSkillContent(skill);
    if (!skillContent) {
      console.log(`  Skill ${skill} not found, skipping.`);
      continue;
    }

    const references = loadSkillReferences(skill);
    const updatePrompt = buildUpdatePrompt(
      skill,
      skillContent,
      references,
      changes,
      indices
    );

    const updateResult = await callClaude(client, updatePrompt);

    if (updateResult.skillUpdated && updateResult.changes?.length > 0) {
      updates.push({
        skill,
        ...updateResult,
      });
      console.log(`  ${updateResult.changes.length} file(s) to update`);
    } else {
      console.log(`  No changes needed: ${updateResult.noChangeReason}`);
    }
  }

  // 5. Write updates
  if (updates.length === 0) {
    console.log("\nNo skill updates generated.");
    saveSyncState(currentState.hash, currentState.state, changes);
    process.exit(0);
  }

  console.log(`\n=== Writing ${updates.length} skill update(s) ===\n`);

  for (const update of updates) {
    for (const change of update.changes) {
      const filePath = path.join(SKILLS_DIR, update.skill, change.file);
      console.log(`Writing: ${filePath}`);
      console.log(`  ${change.description}`);

      if (!dryRun && change.newContent) {
        fs.mkdirSync(path.dirname(filePath), { recursive: true });
        fs.writeFileSync(filePath, change.newContent, "utf8");
      }
    }
  }

  // 6. Save state
  saveSyncState(currentState.hash, currentState.state, changes);

  // 7. Output summary for GitHub Actions
  const summary = updates
    .map((u) => `- **${u.skill}**: ${u.summary}`)
    .join("\n");

  console.log("\n=== Summary ===");
  console.log(summary);

  // Write summary to file for GitHub Actions to pick up
  const summaryFile = path.join(REPO_ROOT, ".github", "state", "update-summary.md");
  writeJson(summaryFile.replace(".md", ".json"), {
    timestamp: new Date().toISOString(),
    changes,
    analysis: analysis.analysis,
    updates: updates.map((u) => ({
      skill: u.skill,
      summary: u.summary,
      files: u.changes.map((c) => c.file),
    })),
  });

  if (dryRun) {
    console.log("\n(Dry run - no files were written)");
  }

  console.log("\nDone.");
}

main().catch((err) => {
  console.error("Fatal error:", err);
  process.exit(1);
});
```

## File: `shared/scripts/scaffold-skill.mjs`
```
import fs from "node:fs";
import path from "node:path";

function usage() {
  process.stderr.write(
    [
      "Usage:",
      '  node shared/scripts/scaffold-skill.mjs <skill-name> "<description>"',
      "",
      "Notes:",
      "- <skill-name> must be lowercase unicode letters/digits with hyphens (no leading/trailing hyphen, no --).",
      "- Creates skills/<skill-name>/SKILL.md and eval/scenarios/<skill-name>.md",
      "",
    ].join("\n")
  );
}

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

function validateSkillName(name) {
  if (!name || typeof name !== "string") return "Missing skill name";
  if (name.length > 64) return `Skill name exceeds 64 chars (${name.length})`;
  if (name !== name.toLowerCase()) return "Skill name must be lowercase";
  if (name.startsWith("-") || name.endsWith("-")) return "Skill name cannot start or end with hyphen";
  if (name.includes("--")) return "Skill name cannot contain consecutive hyphens";
  const ok = /^[\p{Ll}\p{Nd}]+(?:-[\p{Ll}\p{Nd}]+)*$/u.test(name);
  if (!ok) return "Skill name contains invalid characters";
  return null;
}

function main() {
  const [, , skillName, description] = process.argv;
  if (!skillName || !description) {
    usage();
    process.exit(2);
  }

  const nameError = validateSkillName(skillName);
  assert(!nameError, nameError);
  assert(description.length > 0 && description.length <= 1024, "Description must be 1-1024 characters");

  const repoRoot = process.cwd();
  const skillDir = path.join(repoRoot, "skills", skillName);
  const skillMd = path.join(skillDir, "SKILL.md");
  const scenarioPath = path.join(repoRoot, "eval", "scenarios", `${skillName}.md`);

  assert(!fs.existsSync(skillDir), `Skill directory already exists: ${path.relative(repoRoot, skillDir)}`);
  fs.mkdirSync(skillDir, { recursive: true });

  const skillBody = `---\nname: ${skillName}\ndescription: ${description}\ncompatibility: Targets WordPress 6.9+ (PHP 7.2.24+). Filesystem-based agent with bash + node.\n---\n\n# ${skillName}\n\n## When to use\n\n## Inputs required\n\n## Procedure\n\n## Verification\n\n## Failure modes / debugging\n\n## Escalation\n`;
  fs.writeFileSync(skillMd, skillBody, "utf8");

  fs.mkdirSync(path.dirname(scenarioPath), { recursive: true });
  const scenario = `# Scenario: ${skillName}\n\n## Prompt\n\n## Expected behavior\n\n- Uses \`${skillName}\` when the prompt matches its description.\n- Follows the skill procedure and verifies results.\n`;
  fs.writeFileSync(scenarioPath, scenario, "utf8");

  process.stdout.write(`OK: created ${path.relative(repoRoot, skillMd)} and ${path.relative(repoRoot, scenarioPath)}\n`);
}

main();
```

## File: `shared/scripts/skillpack-build.mjs`
```
import fs from "node:fs";
import path from "node:path";

function usage() {
  process.stderr.write(
    [
      "Usage:",
      "  node shared/scripts/skillpack-build.mjs [--out=dist] [--targets=codex,vscode,claude,cursor] [--skills=skill1,skill2] [--clean]",
      "",
      "Outputs:",
      "  - <out>/codex/.codex/skills/<skill>/SKILL.md",
      "  - <out>/vscode/.github/skills/<skill>/SKILL.md",
      "  - <out>/claude/.claude/skills/<skill>/SKILL.md",
      "  - <out>/cursor/.cursor/skills/<skill>/SKILL.md",
      "",
      "Options:",
      "  --targets    Comma-separated list of targets (codex, vscode, claude, cursor). Default: codex,vscode,claude,cursor",
      "  --skills     Comma-separated list of skill names to build. Default: all skills",
      "  --clean      Remove target directories before building",
      "",
      "Notes:",
      "- Avoids symlinks (Codex ignores symlinked directories).",
      "",
    ].join("\n")
  );
}

function parseArgs(argv) {
  const args = { out: "dist", targets: ["codex", "vscode", "claude", "cursor"], skills: [], clean: false };
  for (const a of argv) {
    if (a === "--help" || a === "-h") args.help = true;
    else if (a === "--clean") args.clean = true;
    else if (a.startsWith("--out=")) args.out = a.slice("--out=".length);
    else if (a.startsWith("--targets=")) args.targets = a.slice("--targets=".length).split(",").filter(Boolean);
    else if (a.startsWith("--skills=")) args.skills = a.slice("--skills=".length).split(",").filter(Boolean);
    else {
      process.stderr.write(`Unknown arg: ${a}\n`);
      args.help = true;
    }
  }
  return args;
}

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

function isSymlink(p) {
  try {
    return fs.lstatSync(p).isSymbolicLink();
  } catch {
    return false;
  }
}

function copyFileSyncPreserveMode(src, dest) {
  const st = fs.statSync(src);
  fs.copyFileSync(src, dest);
  fs.chmodSync(dest, st.mode);
}

function copyDir({ srcDir, destDir }) {
  assert(!isSymlink(srcDir), `Refusing to copy symlink dir: ${srcDir}`);
  fs.mkdirSync(destDir, { recursive: true });

  const entries = fs.readdirSync(srcDir, { withFileTypes: true });
  for (const ent of entries) {
    if (ent.name === ".DS_Store") continue;
    const src = path.join(srcDir, ent.name);
    const dest = path.join(destDir, ent.name);

    if (isSymlink(src)) {
      throw new Error(`Refusing to copy symlink: ${src}`);
    }

    if (ent.isDirectory()) {
      copyDir({ srcDir: src, destDir: dest });
      continue;
    }
    if (ent.isFile()) {
      copyFileSyncPreserveMode(src, dest);
      continue;
    }
    // Ignore sockets, devices, etc.
  }
}

function listSkillDirs(skillsRoot) {
  if (!fs.existsSync(skillsRoot)) return [];
  const dirs = fs
    .readdirSync(skillsRoot, { withFileTypes: true })
    .filter((d) => d.isDirectory())
    .map((d) => path.join(skillsRoot, d.name));

  return dirs.filter((d) => fs.existsSync(path.join(d, "SKILL.md")));
}

function buildTarget({ repoRoot, outDir, target, skillDirs }) {
  const rootByTarget = {
    codex: path.join(outDir, "codex", ".codex", "skills"),
    vscode: path.join(outDir, "vscode", ".github", "skills"),
    claude: path.join(outDir, "claude", ".claude", "skills"),
    cursor: path.join(outDir, "cursor", ".cursor", "skills"),
  };
  const destSkillsRoot = rootByTarget[target];
  assert(destSkillsRoot, `Unknown target: ${target}`);

  fs.mkdirSync(destSkillsRoot, { recursive: true });

  for (const srcSkillDir of skillDirs) {
    const name = path.basename(srcSkillDir);
    const destSkillDir = path.join(destSkillsRoot, name);
    copyDir({ srcDir: srcSkillDir, destDir: destSkillDir });
  }

  const rel = path.relative(repoRoot, destSkillsRoot);
  process.stdout.write(`OK: built ${target} skillpack at ${rel}\n`);
}

const VALID_TARGETS = ["codex", "vscode", "claude", "cursor"];

function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help) {
    usage();
    process.exit(2);
  }

  const repoRoot = process.cwd();
  const skillsRoot = path.join(repoRoot, "skills");
  const outDir = path.isAbsolute(args.out) ? args.out : path.join(repoRoot, args.out);

  let skillDirs = listSkillDirs(skillsRoot);
  assert(skillDirs.length > 0, "No skills found under ./skills");

  // Filter skills if --skills was specified
  if (args.skills.length > 0) {
    const requestedSkills = new Set(args.skills);
    const availableSkills = skillDirs.map((d) => path.basename(d));

    // Validate requested skills exist
    for (const s of requestedSkills) {
      assert(availableSkills.includes(s), `Unknown skill: ${s}. Available: ${availableSkills.join(", ")}`);
    }

    skillDirs = skillDirs.filter((d) => requestedSkills.has(path.basename(d)));
  }

  const targets = [...new Set(args.targets)];
  for (const t of targets) {
    assert(VALID_TARGETS.includes(t), `Invalid target: ${t}. Valid targets: ${VALID_TARGETS.join(", ")}`);
  }

  if (args.clean) {
    for (const t of targets) {
      const targetDir = path.join(outDir, t);
      fs.rmSync(targetDir, { recursive: true, force: true });
    }
  }

  for (const target of targets) {
    buildTarget({ repoRoot, outDir, target, skillDirs });
  }
}

main();

```

## File: `shared/scripts/skillpack-install.mjs`
```
import fs from "node:fs";
import path from "node:path";
import os from "node:os";

function usage() {
  process.stderr.write(
    [
      "Usage:",
      "  node shared/scripts/skillpack-install.mjs --dest=<repo-root> [options]",
      "",
      "Options:",
      "  --dest=<path>       Destination repo root (required, unless using --global)",
      "  --from=<path>       Source directory (default: dist)",
      "  --targets=<list>    Comma-separated targets: codex, vscode, claude, claude-global, cursor, cursor-global (default: codex,vscode)",
      "  --skills=<list>     Comma-separated skill names to install (default: all)",
      "  --mode=<mode>       'replace' (default) or 'merge'",
      "  --global            Shorthand for --targets=claude-global (installs to ~/.claude/skills)",
      "  --dry-run           Show what would be installed without making changes",
      "  --list              List available skills and exit",
      "",
      "Targets:",
      "  codex               Install to <dest>/.codex/skills/",
      "  vscode              Install to <dest>/.github/skills/",
      "  claude              Install to <dest>/.claude/skills/ (project-level)",
      "  claude-global       Install to ~/.claude/skills/ (user-level, ignores --dest)",
      "  cursor              Install to <dest>/.cursor/skills/",
      "  cursor-global       Install to ~/.cursor/skills/ (user-level, ignores --dest)",
      "",
      "Examples:",
      "  # Build and install to a WordPress project",
      "  node shared/scripts/skillpack-build.mjs --clean",
      "  node shared/scripts/skillpack-install.mjs --dest=../my-wp-repo --targets=codex,vscode,claude,cursor",
      "",
      "  # Install globally for Claude Code (all skills)",
      "  node shared/scripts/skillpack-install.mjs --global",
      "",
      "  # Install globally for Cursor (all skills)",
      "  node shared/scripts/skillpack-install.mjs --targets=cursor-global",
      "",
      "  # Install specific skills globally",
      "  node shared/scripts/skillpack-install.mjs --global --skills=wp-playground,wp-block-development",
      "",
      "  # Install to project with specific skills",
      "  node shared/scripts/skillpack-install.mjs --dest=../my-repo --targets=claude,cursor --skills=wp-wpcli-and-ops",
      "",
    ].join("\n")
  );
}

function parseArgs(argv) {
  const args = {
    from: "dist",
    dest: null,
    targets: ["codex", "vscode"],
    skills: [],
    mode: "replace",
    dryRun: false,
    global: false,
    list: false,
  };

  for (const a of argv) {
    if (a === "--help" || a === "-h") args.help = true;
    else if (a === "--dry-run") args.dryRun = true;
    else if (a === "--global") args.global = true;
    else if (a === "--list") args.list = true;
    else if (a.startsWith("--from=")) args.from = a.slice("--from=".length);
    else if (a.startsWith("--dest=")) args.dest = a.slice("--dest=".length);
    else if (a.startsWith("--targets=")) args.targets = a.slice("--targets=".length).split(",").filter(Boolean);
    else if (a.startsWith("--skills=")) args.skills = a.slice("--skills=".length).split(",").filter(Boolean);
    else if (a.startsWith("--mode=")) args.mode = a.slice("--mode=".length);
    else {
      process.stderr.write(`Unknown arg: ${a}\n`);
      args.help = true;
    }
  }

  // --global is shorthand for --targets=claude-global
  if (args.global) {
    args.targets = ["claude-global"];
  }

  return args;
}

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

function isSymlink(p) {
  try {
    return fs.lstatSync(p).isSymbolicLink();
  } catch {
    return false;
  }
}

function copyFileSyncPreserveMode(src, dest) {
  const st = fs.statSync(src);
  fs.copyFileSync(src, dest);
  fs.chmodSync(dest, st.mode);
}

function copyDir({ srcDir, destDir }) {
  if (isSymlink(srcDir)) throw new Error(`Refusing to copy symlink dir: ${srcDir}`);
  fs.mkdirSync(destDir, { recursive: true });

  const entries = fs.readdirSync(srcDir, { withFileTypes: true });
  for (const ent of entries) {
    if (ent.name === ".DS_Store") continue;
    const src = path.join(srcDir, ent.name);
    const dest = path.join(destDir, ent.name);

    if (isSymlink(src)) throw new Error(`Refusing to copy symlink: ${src}`);

    if (ent.isDirectory()) {
      copyDir({ srcDir: src, destDir: dest });
      continue;
    }
    if (ent.isFile()) {
      copyFileSyncPreserveMode(src, dest);
      continue;
    }
  }
}

function listSkillDirs(skillsRoot) {
  if (!fs.existsSync(skillsRoot)) return [];
  return fs
    .readdirSync(skillsRoot, { withFileTypes: true })
    .filter((d) => d.isDirectory())
    .map((d) => path.join(skillsRoot, d.name))
    .filter((d) => fs.existsSync(path.join(d, "SKILL.md")));
}

const VALID_TARGETS = ["codex", "vscode", "claude", "claude-global", "cursor", "cursor-global"];

// Map target to source subdirectory in dist
function getSourceDir(fromDir, target) {
  // claude-global uses the same source as claude; cursor-global uses the same as cursor
  const sourceTarget =
    target === "claude-global" ? "claude" : target === "cursor-global" ? "cursor" : target;
  const targetDirMap = {
    codex: path.join(fromDir, "codex", ".codex", "skills"),
    vscode: path.join(fromDir, "vscode", ".github", "skills"),
    claude: path.join(fromDir, "claude", ".claude", "skills"),
    cursor: path.join(fromDir, "cursor", ".cursor", "skills"),
  };
  return targetDirMap[sourceTarget];
}

// Map target to destination directory
function getDestDir(destRepoRoot, target) {
  // claude-global and cursor-global don't need destRepoRoot
  if (target === "claude-global") {
    return path.join(os.homedir(), ".claude", "skills");
  }
  if (target === "cursor-global") {
    return path.join(os.homedir(), ".cursor", "skills");
  }

  // Other targets require destRepoRoot
  const destDirMap = {
    codex: path.join(destRepoRoot, ".codex", "skills"),
    vscode: path.join(destRepoRoot, ".github", "skills"),
    claude: path.join(destRepoRoot, ".claude", "skills"),
    cursor: path.join(destRepoRoot, ".cursor", "skills"),
  };
  return destDirMap[target];
}

function installTarget({ fromDir, destRepoRoot, target, skillsFilter, mode, dryRun }) {
  const srcSkillsRoot = getSourceDir(fromDir, target);
  const destSkillsRoot = getDestDir(destRepoRoot, target);

  assert(srcSkillsRoot, `Unknown target: ${target}`);
  assert(fs.existsSync(srcSkillsRoot), `Missing source skillpack dir: ${srcSkillsRoot}. Did you run skillpack-build.mjs first?`);

  let skillDirs = listSkillDirs(srcSkillsRoot);
  assert(skillDirs.length > 0, `No skills found in: ${srcSkillsRoot}`);

  // Filter skills if requested
  if (skillsFilter.length > 0) {
    const requested = new Set(skillsFilter);
    const available = skillDirs.map((d) => path.basename(d));

    // Validate requested skills exist
    for (const s of requested) {
      assert(available.includes(s), `Unknown skill: ${s}. Available: ${available.join(", ")}`);
    }

    skillDirs = skillDirs.filter((d) => requested.has(path.basename(d)));
  }

  if (dryRun) {
    process.stdout.write(`[DRY-RUN] Would install ${skillDirs.length} skill(s) to ${destSkillsRoot}:\n`);
    for (const d of skillDirs) {
      process.stdout.write(`  - ${path.basename(d)}\n`);
    }
    return;
  }

  fs.mkdirSync(destSkillsRoot, { recursive: true });

  for (const srcSkillDir of skillDirs) {
    const name = path.basename(srcSkillDir);
    const destSkillDir = path.join(destSkillsRoot, name);

    if (mode === "replace") {
      fs.rmSync(destSkillDir, { recursive: true, force: true });
    }

    copyDir({ srcDir: srcSkillDir, destDir: destSkillDir });
  }

  const isGlobal = target === "claude-global" || target === "cursor-global";
  const location = isGlobal ? destSkillsRoot : path.relative(destRepoRoot, destSkillsRoot) || ".";
  process.stdout.write(`OK: installed ${skillDirs.length} skill(s) to ${location}\n`);
}

function listAvailableSkills(fromDir) {
  // Check all possible target sources
  const sources = ["codex", "vscode", "claude", "cursor"]
    .map((t) => getSourceDir(fromDir, t))
    .filter((p) => fs.existsSync(p));

  if (sources.length === 0) {
    process.stderr.write("No built skills found. Run skillpack-build.mjs first.\n");
    process.exit(1);
  }

  const skillDirs = listSkillDirs(sources[0]);
  process.stdout.write("Available skills:\n");
  for (const d of skillDirs) {
    process.stdout.write(`  - ${path.basename(d)}\n`);
  }
}

function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help) {
    usage();
    process.exit(2);
  }

  const repoRoot = process.cwd();
  const fromDir = path.isAbsolute(args.from) ? args.from : path.join(repoRoot, args.from);

  // Handle --list
  if (args.list) {
    listAvailableSkills(fromDir);
    process.exit(0);
  }

  // Validate targets
  const targets = [...new Set(args.targets)];
  for (const t of targets) {
    assert(VALID_TARGETS.includes(t), `Invalid target: ${t}. Valid targets: ${VALID_TARGETS.join(", ")}`);
  }

  // --dest is required unless only using global targets (claude-global, cursor-global)
  const needsDest = targets.some((t) => t !== "claude-global" && t !== "cursor-global");
  if (needsDest && !args.dest) {
    process.stderr.write("Error: --dest is required for non-global targets.\n\n");
    usage();
    process.exit(1);
  }

  const destRepoRoot = args.dest
    ? path.isAbsolute(args.dest)
      ? args.dest
      : path.join(repoRoot, args.dest)
    : null;

  assert(args.mode === "replace" || args.mode === "merge", "mode must be 'replace' or 'merge'");

  for (const target of targets) {
    installTarget({
      fromDir,
      destRepoRoot,
      target,
      skillsFilter: args.skills,
      mode: args.mode,
      dryRun: args.dryRun,
    });
  }
}

main();
```

## File: `shared/scripts/update-upstream-indices.mjs`
```
import fs from "node:fs";
import path from "node:path";

const SOURCES = {
  wordpressCoreVersionCheck: "https://api.wordpress.org/core/version-check/1.7/",
  gutenbergReleases: "https://api.github.com/repos/WordPress/gutenberg/releases?per_page=50",
  wpGutenbergMapDoc:
    "https://developer.wordpress.org/block-editor/contributors/versions-in-wordpress/",
};

function mkdirp(dirPath) {
  fs.mkdirSync(dirPath, { recursive: true });
}

function writeJson(filePath, value) {
  mkdirp(path.dirname(filePath));
  fs.writeFileSync(filePath, `${JSON.stringify(value, null, 2)}\n`, "utf8");
}

function stripTags(html) {
  return html
    .replace(/<script[\s\S]*?<\/script>/gi, "")
    .replace(/<style[\s\S]*?<\/style>/gi, "")
    .replace(/<[^>]+>/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function decodeHtml(text) {
  return text
    .replace(/&nbsp;/g, " ")
    .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, "\"")
    .replace(/&#39;/g, "'")
    .replace(/&#(\d+);/g, (_, n) => String.fromCharCode(Number(n)));
}

async function fetchText(url) {
  const res = await fetch(url, {
    headers: {
      "user-agent": "wp-agent-skills-upstream-sync/0.1",
      accept: "text/html,application/json",
    },
  });
  if (!res.ok) throw new Error(`Fetch failed ${res.status} for ${url}`);
  return await res.text();
}

async function fetchJson(url) {
  const text = await fetchText(url);
  try {
    return JSON.parse(text);
  } catch {
    throw new Error(`Expected JSON from ${url}, got non-JSON response`);
  }
}

function parseWpGutenbergMapFromHtml(html) {
  // Best-effort HTML table parsing without dependencies:
  // 1) find the first <table> that contains "WordPress Version" and "Gutenberg Versions"
  // 2) extract rows, then extract cells
  const tables = [...html.matchAll(/<table[\s\S]*?<\/table>/gi)].map((m) => m[0]);
  const target = tables.find((t) => /WordPress\s*Version/i.test(t) && /Gutenberg\s*Versions/i.test(t));
  if (!target) return { rows: [], note: "table-not-found" };

  const rowHtml = [...target.matchAll(/<tr[\s\S]*?<\/tr>/gi)].map((m) => m[0]);
  const rows = [];

  for (const r of rowHtml) {
    const cellHtml = [...r.matchAll(/<(td|th)[^>]*>([\s\S]*?)<\/\1>/gi)].map((m) => m[2]);
    if (cellHtml.length < 2) continue;

    const cells = cellHtml.map((c) => decodeHtml(stripTags(c)));
    const wp = cells[0];
    const gb = cells[1];

    if (/WordPress\s*Version/i.test(wp) || /Gutenberg\s*Versions/i.test(gb)) continue;
    if (!/^\d+\.\d+/.test(wp)) continue;

    rows.push({ wordpress: wp, gutenberg: gb });
  }

  return { rows, note: null };
}

function normalizeWpVersionCheckPayload(payload) {
  // https://api.wordpress.org/core/version-check/1.7/ returns something like:
  // { offers: [...], translations: [...] }
  const offers = Array.isArray(payload?.offers) ? payload.offers : [];

  const candidates = offers
    .map((o) => ({
      version: typeof o?.version === "string" ? o.version : null,
      current: typeof o?.current === "string" ? o.current : null,
      download: typeof o?.download === "string" ? o.download : null,
      phpVersion: typeof o?.php_version === "string" ? o.php_version : null,
      mysqlVersion: typeof o?.mysql_version === "string" ? o.mysql_version : null,
      response: typeof o?.response === "string" ? o.response : null,
      locale: typeof o?.locale === "string" ? o.locale : null,
    }))
    .filter((o) => o.version || o.current);

  // Keep a small, stable subset; prioritize "upgrade" offers.
  const byVersion = new Map();
  for (const o of candidates) {
    const v = o.version ?? o.current;
    if (!v) continue;
    if (!byVersion.has(v)) byVersion.set(v, o);
  }

  const versions = [...byVersion.keys()].sort((a, b) => (a < b ? 1 : a > b ? -1 : 0));
  return {
    latest: versions[0] ?? null,
    recent: versions.slice(0, 20),
    offers: versions.slice(0, 20).map((v) => byVersion.get(v)),
  };
}

function normalizeGutenbergReleases(payload) {
  const releases = Array.isArray(payload) ? payload : [];
  const stable = releases
    .filter((r) => r && !r.draft && !r.prerelease && typeof r.tag_name === "string")
    .map((r) => ({
      tag: r.tag_name,
      name: typeof r.name === "string" ? r.name : null,
      publishedAt: typeof r.published_at === "string" ? r.published_at : null,
      url: typeof r.html_url === "string" ? r.html_url : null,
    }));
  return {
    latest: stable[0] ?? null,
    recent: stable.slice(0, 30),
  };
}

async function main() {
  const repoRoot = process.cwd();
  const outDir = path.join(repoRoot, "shared", "references");

  const [wpVersionPayload, gbReleasesPayload, mapHtml] = await Promise.all([
    fetchJson(SOURCES.wordpressCoreVersionCheck),
    fetchJson(SOURCES.gutenbergReleases),
    fetchText(SOURCES.wpGutenbergMapDoc),
  ]);

  const wordpress = normalizeWpVersionCheckPayload(wpVersionPayload);
  const gutenberg = normalizeGutenbergReleases(gbReleasesPayload);
  const map = parseWpGutenbergMapFromHtml(mapHtml);

  writeJson(path.join(outDir, "wordpress-core-versions.json"), {
    source: SOURCES.wordpressCoreVersionCheck,
    ...wordpress,
  });

  writeJson(path.join(outDir, "gutenberg-releases.json"), {
    source: SOURCES.gutenbergReleases,
    ...gutenberg,
  });

  writeJson(path.join(outDir, "wp-gutenberg-version-map.json"), {
    source: SOURCES.wpGutenbergMapDoc,
    note: map.note,
    rows: map.rows,
  });

  process.stdout.write("OK: updated shared/references/* upstream indices\n");
}

main().catch((err) => {
  process.stderr.write(`${err?.stack || String(err)}\n`);
  process.exit(1);
});
```

## File: `skills/blueprint/SKILL.md`
```markdown
---
name: blueprint
description: Use when creating, editing, or reviewing WordPress Playground blueprint JSON files. Triggers on mentions of blueprints, playground configuration, or requests to set up a WordPress demo environment.
compatibility: "WordPress 6.9+, PHP 7.2.24+. Optionally Playground CLI or a browser"
---

# WordPress Playground Blueprints

## Overview

A Blueprint is a JSON file that declaratively configures a WordPress Playground instance — installing plugins/themes, setting options, running PHP/SQL, manipulating files, and more.

**Core principle:** Blueprints are trusted JSON-only declarations. No arbitrary JavaScript. They work on web, Node.js, and CLI.

## Quick Start Template

```json
{
  "$schema": "https://playground.wordpress.net/blueprint-schema.json",
  "landingPage": "/wp-admin/",
  "preferredVersions": { "php": "8.3", "wp": "latest" },
  "steps": [{ "step": "login" }]
}
```

## Top-Level Properties

All optional. Only documented keys are allowed — the schema rejects unknown properties.

| Property | Type | Notes |
|----------|------|-------|
| `$schema` | string | Always `"https://playground.wordpress.net/blueprint-schema.json"` |
| `landingPage` | string | Relative path, e.g. `/wp-admin/` |
| `meta` | object | `{ title, author, description?, categories? }` — title and author required |
| `preferredVersions` | object | `{ php, wp }` — both required when present |
| `features` | object | `{ networking?: boolean, intl?: boolean }` — **only** these two keys, nothing else. Networking defaults to `true` |
| `extraLibraries` | array | `["wp-cli"]` — auto-included when any `wp-cli` step is present |
| `constants` | object | Shorthand for `defineWpConfigConsts`. Values: string/boolean/number |
| `plugins` | array | Shorthand for `installPlugin` steps. Strings = wp.org slugs |
| `siteOptions` | object | Shorthand for `setSiteOptions` |
| `login` | boolean or object | `true` = login as admin. Object = `{ username?, password? }` (both default to `"admin"`/`"password"`) |
| `steps` | array | Main execution pipeline. Runs after shorthands |

### preferredVersions Values

- **php:** Major.minor only (e.g. `"8.3"`, `"7.4"`), or `"latest"`. Patch versions like `"7.4.1"` are invalid. Check the schema for currently supported versions.
- **wp:** Recent major versions (e.g. `"6.7"`, `"6.8"`), `"latest"`, `"nightly"`, `"beta"`, or a URL to a custom zip. Check the schema for the full list.

### Shorthands vs Steps

Shorthands (`login`, `plugins`, `siteOptions`, `constants`) are expanded and prepended to `steps` in an **unspecified order**. Use explicit steps when execution order matters.

## Resource References

Resources tell Playground where to find files. Used by `installPlugin`, `installTheme`, `writeFile`, `writeFiles`, `importWxr`, etc.

| Resource Type | Required Fields | Example |
|--------------|----------------|---------|
| `wordpress.org/plugins` | `slug` | `{ "resource": "wordpress.org/plugins", "slug": "woocommerce" }` |
| `wordpress.org/themes` | `slug` | `{ "resource": "wordpress.org/themes", "slug": "astra" }` |
| `url` | `url` | `{ "resource": "url", "url": "https://example.com/plugin.zip" }` |
| `git:directory` | `url`, `ref` | See below |
| `literal` | `name`, `contents` | `{ "resource": "literal", "name": "file.txt", "contents": "hello" }` |
| `literal:directory` | `name`, `files` | See below |
| `bundled` | `path` | References a file within a blueprint bundle (e.g. `{ "resource": "bundled", "path": "/plugin.zip" }`) |
| `zip` | `inner` | Wraps another resource in a ZIP — use when a step expects a zip but your source isn't one (e.g. wrapping a `url` resource pointing to a raw directory) |

### git:directory — Installing from GitHub

```json
{
  "resource": "git:directory",
  "url": "https://github.com/WordPress/gutenberg",
  "ref": "trunk",
  "refType": "branch",
  "path": "/"
}
```

- When using a branch or tag name for `ref`, you **must** set `refType` (`"branch"` | `"tag"` | `"commit"` | `"refname"`). Without it, only `"HEAD"` resolves reliably.
- `path` selects a subdirectory (defaults to repo root).

### literal:directory — Inline File Trees

```json
{
  "resource": "literal:directory",
  "name": "my-plugin",
  "files": {
    "plugin.php": "<?php /* Plugin Name: My Plugin */ ?>",
    "includes": {
      "helper.php": "<?php // helper code ?>"
    }
  }
}
```

- `files` uses nested objects for subdirectories — keys are filenames or directory names, values are **plain strings** (file content) or **objects** (subdirectories). Never use resource references as values.
- **Do NOT use path separators in keys** (e.g. `"includes/helper.php"` is wrong — use a nested `"includes": { "helper.php": "..." }` object).

## Steps Reference

Every step requires `"step": "<name>"`. Any step can optionally include `"progress": { "weight": 1, "caption": "Installing..." }` for UI feedback.

### Plugin & Theme Installation

```json
{
  "step": "installPlugin",
  "pluginData": { "resource": "wordpress.org/plugins", "slug": "gutenberg" },
  "options": { "activate": true, "targetFolderName": "gutenberg" },
  "ifAlreadyInstalled": "overwrite"
}
```

```json
{
  "step": "installTheme",
  "themeData": { "resource": "wordpress.org/themes", "slug": "twentytwentyfour" },
  "options": { "activate": true, "importStarterContent": true },
  "ifAlreadyInstalled": "overwrite"
}
```

- Use `pluginData` / `themeData` — **NOT** the deprecated `pluginZipFile` / `themeZipFile`.
- `pluginData` / `themeData` accept any FileReference or DirectoryReference — a zip URL, a `wordpress.org/plugins` slug, a `git:directory`, or a `literal:directory` (no `zip` wrapper needed).
- `options.activate` controls activation. No need for a separate `activatePlugin`/`activateTheme` step when using `installPlugin`/`installTheme`.
- `ifAlreadyInstalled`: `"overwrite"` | `"skip"` | `"error"`

### Activation (standalone)

Only needed for plugins/themes already on disk (e.g. after `writeFile`/`writeFiles`):

```json
{ "step": "activatePlugin", "pluginPath": "my-plugin/my-plugin.php" }
```
```json
{ "step": "activateTheme", "themeFolderName": "twentytwentyfour" }
```

### File Operations

```json
{ "step": "writeFile", "path": "/wordpress/wp-content/mu-plugins/custom.php", "data": "<?php // code" }
```

`data` accepts a plain string (as shown above) or a resource reference (e.g. `{ "resource": "url", "url": "https://..." }`).

```json
{
  "step": "writeFiles",
  "writeToPath": "/wordpress/wp-content/plugins/",
  "filesTree": {
    "resource": "literal:directory",
    "name": "my-plugin",
    "files": {
      "plugin.php": "<?php\n/*\nPlugin Name: My Plugin\n*/",
      "includes": {
        "helpers.php": "<?php // helpers"
      }
    }
  }
}
```

**`writeFiles` requires a DirectoryReference** (`literal:directory` or `git:directory`) as `filesTree` — not a plain object.

Other file operations: `mkdir`, `cp`, `mv`, `rm`, `rmdir`, `unzip`.

### Running Code

**runPHP:**
```json
{ "step": "runPHP", "code": "<?php require '/wordpress/wp-load.php'; update_option('key', 'value');" }
```
**GOTCHA:** You must `require '/wordpress/wp-load.php';` to use any WordPress functions.

**wp-cli:**
```json
{ "step": "wp-cli", "command": "wp post create --post_type=page --post_title='Hello' --post_status=publish" }
```
The step name is `wp-cli` (with hyphen), NOT `cli` or `wpcli`.

**runSql:**
```json
{ "step": "runSql", "sql": { "resource": "literal", "name": "q.sql", "contents": "UPDATE wp_options SET option_value='val' WHERE option_name='key';" } }
```

### Site Configuration

```json
{ "step": "setSiteOptions", "options": { "blogname": "My Site", "blogdescription": "A tagline" } }
```
```json
{ "step": "defineWpConfigConsts", "consts": { "WP_DEBUG": true } }
```
```json
{ "step": "setSiteLanguage", "language": "en_US" }
```
```json
{ "step": "defineSiteUrl", "siteUrl": "https://example.com" }
```

### Other Steps

| Step | Key Properties |
|------|---------------|
| `login` | `username?`, `password?` (default `"admin"` / `"password"`) |
| `enableMultisite` | (no required props) |
| `importWxr` | `file` (FileReference) |
| `importThemeStarterContent` | `themeSlug?` |
| `importWordPressFiles` | `wordPressFilesZip`, `pathInZip?` — imports a full WordPress directory from a zip |
| `request` | `request: { url, method?, headers?, body? }` |
| `updateUserMeta` | `userId`, `meta` |
| `runWpInstallationWizard` | `options?` — runs the WP install wizard with given options |
| `resetData` | (no props) |

## Common Patterns

### Inline mu-plugin (quick custom code)

```json
{
  "step": "writeFile",
  "path": "/wordpress/wp-content/mu-plugins/custom.php",
  "data": "<?php\n// mu-plugins load automatically — no activation needed, no require wp-load.php\nadd_filter('show_admin_bar', '__return_false');"
}
```

### Inline plugin with multiple files

```json
{
  "step": "writeFiles",
  "writeToPath": "/wordpress/wp-content/plugins/",
  "filesTree": {
    "resource": "literal:directory",
    "name": "my-plugin",
    "files": {
      "my-plugin.php": "<?php\n/*\nPlugin Name: My Plugin\n*/\nrequire __DIR__ . '/includes/main.php';",
      "includes": {
        "main.php": "<?php // main logic"
      }
    }
  }
}
```

Then activate it with a separate step:

```json
{ "step": "activatePlugin", "pluginPath": "my-plugin/my-plugin.php" }
```

### Plugin from a GitHub branch

```json
{
  "step": "installPlugin",
  "pluginData": {
    "resource": "git:directory",
    "url": "https://github.com/user/repo",
    "ref": "feature-branch",
    "refType": "branch",
    "path": "/"
  }
}
```

## Common Mistakes

| Mistake | Correct |
|---------|---------|
| `pluginZipFile` / `themeZipFile` | `pluginData` / `themeData` |
| `"step": "cli"` | `"step": "wp-cli"` |
| Flat object as `writeFiles.filesTree` | Must be a `literal:directory` or `git:directory` resource |
| Path separators in `files` keys | Use nested objects for subdirectories |
| `runPHP` without `wp-load.php` | Always `require '/wordpress/wp-load.php';` for WP functions |
| Invented top-level keys | Only documented keys work — schema rejects unknown properties |
| Inventing proxy URLs for GitHub | Use `git:directory` resource type |
| Omitting `refType` with branch/tag `ref` | Required — only `"HEAD"` works without it |
| Resource references in `literal:directory` `files` values | Values must be plain strings (content) or objects (subdirectories) — never resource refs |
| `features.debug` or other invented feature keys | `features` only supports `networking` and `intl` — use `constants: { "WP_DEBUG": true }` for debug mode |
| `require wp-load.php` in mu-plugin code | Only needed in `runPHP` steps — mu-plugins already run within WordPress |
| Schema URL with `.org` domain | Must be `playground.wordpress.net`, not `playground.wordpress.org` |

## Full Reference

This skill covers the most common steps and patterns. For the complete API, see:

- **Blueprint docs:** https://wordpress.github.io/wordpress-playground/blueprints
- **JSON schema:** https://playground.wordpress.net/blueprint-schema.json

Additional steps not covered above: `runPHPWithOptions` (run PHP with custom `ini` settings), `runWpInstallationWizard`, and resource types `vfs` and `bundled` (for advanced embedding scenarios).

## Blueprint Bundles

Bundles are self-contained packages that include a `blueprint.json` along with all the resources it references (plugins, themes, WXR files, etc.). Instead of hosting assets externally, bundle them alongside the blueprint.

### Bundle Structure

```
my-bundle/
├── blueprint.json          ← must be at the root
├── my-plugin.zip           ← zipped plugin directory
├── theme.zip
└── content/
    └── sample-content.wxr
```

Plugins and themes must be zipped before bundling — `installPlugin` expects a zip, not a raw directory. To create the zip from a plugin directory:

```bash
cd my-bundle
zip -r my-plugin.zip my-plugin/
```

### Referencing Bundled Resources

Use the `bundled` resource type to reference files within the bundle:

```json
{
  "step": "installPlugin",
  "pluginData": {
    "resource": "bundled",
    "path": "/my-plugin.zip"
  },
  "options": { "activate": true }
}
```

```json
{
  "step": "importWxr",
  "file": {
    "resource": "bundled",
    "path": "/content/sample-content.wxr"
  }
}
```

### Creating a Bundle Step by Step

1. Create the bundle directory and add `blueprint.json` at its root.
2. Write your plugin/theme source files in a subdirectory (e.g. `my-plugin/my-plugin.php`).
3. Zip the plugin directory: `zip -r my-plugin.zip my-plugin/`
4. Reference it in `blueprint.json` using `{ "resource": "bundled", "path": "/my-plugin.zip" }`.

Full example — a bundle that installs a custom plugin:

```
dashboard-widget-bundle/
├── blueprint.json
├── dashboard-widget.zip        ← zip of dashboard-widget/
└── dashboard-widget/           ← plugin source (kept for editing)
    └── dashboard-widget.php
```

```json
{
  "$schema": "https://playground.wordpress.net/blueprint-schema.json",
  "landingPage": "/wp-admin/",
  "preferredVersions": { "php": "8.3", "wp": "latest" },
  "steps": [
    { "step": "login" },
    {
      "step": "installPlugin",
      "pluginData": { "resource": "bundled", "path": "/dashboard-widget.zip" },
      "options": { "activate": true }
    }
  ]
}
```

### Distribution Formats

| Format | How to use |
|--------|-----------|
| ZIP file (remote) | Website: `https://playground.wordpress.net/?blueprint-url=https://example.com/bundle.zip` |
| ZIP file (local) | CLI: `npx @wp-playground/cli server --blueprint=./bundle.zip` |
| Local directory | CLI: `npx @wp-playground/cli server --blueprint=./my-bundle/ --blueprint-may-read-adjacent-files` |
| Git repository directory | Point `blueprint-url` at a repo directory containing `blueprint.json` |

**GOTCHA:** Local directory bundles always need `--blueprint-may-read-adjacent-files` for the CLI to read bundled resources. Without it, any `"resource": "bundled"` reference will fail with a "File not found" error. ZIP bundles don't need this flag — all files are self-contained inside the archive.

## Testing Blueprints

### Inline Blueprints (quick test, no bundles)

Minify the blueprint JSON (no extra whitespace), prepend `https://playground.wordpress.net/#`, and open the URL in a browser:

```
https://playground.wordpress.net/#{"$schema":"https://playground.wordpress.net/blueprint-schema.json","preferredVersions":{"php":"8.3","wp":"latest"},"steps":[{"step":"login"}]}
```

Very large blueprints may exceed browser URL length limits; use the CLI instead.

### Local CLI Testing

**Interactive server** (keeps running, opens in browser):
```bash
# Directory bundle — requires --blueprint-may-read-adjacent-files
npx @wp-playground/cli server --blueprint=./my-bundle/ --blueprint-may-read-adjacent-files

# ZIP bundle — self-contained, no extra flags needed
npx @wp-playground/cli server --blueprint=./bundle.zip
```

**Headless validation** (runs blueprint and exits):
```bash
npx @wp-playground/cli run-blueprint --blueprint=./my-bundle/ --blueprint-may-read-adjacent-files
```

### Testing with the wordpress-playground-server Skill

Use the `wordpress-playground-server` skill to start a local Playground instance with `--blueprint /path/to/blueprint.json`, then verify the expected state with Playwright MCP. For directory bundles, pass `--blueprint-may-read-adjacent-files` as an extra argument.
```

## File: `skills/wordpress-router/SKILL.md`
```markdown
---
name: wordpress-router
description: "Use when the user asks about WordPress codebases (plugins, themes, block themes, Gutenberg blocks, WP core checkouts) and you need to quickly classify the repo and route to the correct workflow/skill (blocks, theme.json, REST API, WP-CLI, performance, security, testing, release packaging)."
compatibility: "Targets WordPress 6.9+ (PHP 7.2.24+). Filesystem-based agent with bash + node. Some workflows require WP-CLI."
---

# WordPress Router

## When to use

Use this skill at the start of most WordPress tasks to:

- identify what kind of WordPress codebase this is (plugin vs theme vs block theme vs WP core checkout vs full site),
- pick the right workflow and guardrails,
- delegate to the most relevant domain skill(s).

## Inputs required

- Repo root (current working directory).
- The user’s intent (what they want changed) and any constraints (WP version targets, WP.com specifics, release requirements).

## Procedure

1. Run the project triage script:
   - `node skills/wp-project-triage/scripts/detect_wp_project.mjs`
2. Read the triage output and classify:
   - primary project kind(s),
   - tooling available (PHP/Composer, Node, @wordpress/scripts),
   - tests present (PHPUnit, Playwright, wp-env),
   - any version hints.
3. Route to domain workflows based on user intent + repo kind:
   - For the decision tree, read: `skills/wordpress-router/references/decision-tree.md`.
4. Apply guardrails before making changes:
   - Confirm any version constraints if unclear.
   - Prefer the repo’s existing tooling and conventions for builds/tests.

## Verification

- Re-run the triage script if you create or restructure significant files.
- Run the repo’s lint/test/build commands that the triage output recommends (if available).

## Failure modes / debugging

- If triage reports `kind: unknown`, inspect:
  - root `composer.json`, `package.json`, `style.css`, `block.json`, `theme.json`, `wp-content/`.
- If the repo is huge, consider narrowing scanning scope or adding ignore rules to the triage script.

## Escalation

- If routing is ambiguous, ask one question:
  - “Is this intended to be a WordPress plugin, a theme (classic/block), or a full site repo?”
```

## File: `skills/wordpress-router/references/decision-tree.md`
```markdown
# Router decision tree (v1)

This is a lightweight routing guide. It assumes you can run `wp-project-triage` first.

## Step 1: classify repo kind (from triage)

Use `triage.project.kind` and the strongest signals:

- `wp-core` → treat as WordPress core checkout work (core patches, PHPUnit, build tools).
- `wp-site` → treat as a full site repo (wp-content present; changes might be theme + plugins).
- `wp-block-theme` → theme.json/templates/patterns workflows.
- `wp-theme` → classic theme workflows (templates PHP, `functions.php`, `style.css`).
- `wp-block-plugin` → Gutenberg block development in a plugin (block.json, build pipeline).
- `wp-plugin` / `wp-mu-plugin` → plugin workflows (hooks, admin, settings, cron, REST, security).
- `gutenberg` → Gutenberg monorepo workflows (packages, tooling, docs).

If multiple kinds match, prefer the most specific:
`gutenberg` > `wp-core` > `wp-site` > `wp-block-theme` > `wp-block-plugin` > `wp-theme` > `wp-plugin`.

## Step 2: route by user intent (keywords)

Route by intent even if repo kind is broad (like `wp-site`):

- **Interactivity API / data-wp-* directives / @wordpress/interactivity / viewScriptModule**
  - Route → `wp-interactivity-api`.
- **Abilities API / wp_register_ability / wp-abilities/v1 / @wordpress/abilities**
  - Route → `wp-abilities-api`.
- **Playground / run-blueprint / build-snapshot / @wp-playground/cli / playground.wordpress.net**
  - Route → `wp-playground`.
- **Blocks / block.json / registerBlockType / attributes / save serialization**
  - Route → `wp-block-development`.
- **theme.json / Global Styles / templates/*.html / patterns/**
  - Route → `wp-block-themes`.
- **Plugins / hooks / activation hook / uninstall / Settings API / admin pages**
  - Route → `wp-plugin-development`.
- **REST endpoint / register_rest_route / permission_callback**
  - Route → `wp-rest-api`.
- **WP-CLI / wp-cli.yml / commands**
  - Route → `wp-wpcli-and-ops`.
- **Build tooling / @wordpress/scripts / webpack / Vite / npm scripts**
  - Route → `wp-build-tooling` (planned).
- **Testing / PHPUnit / wp-env / Playwright**
  - Route → `wp-testing` (planned).
- **PHPStan / static analysis / phpstan.neon / phpstan-baseline.neon**
  - Route → `wp-phpstan`.
- **Performance / caching / query profiling / editor slowness**
  - Route → `wp-performance`.
- **Security / nonces / capabilities / sanitization/escaping / uploads**
  - Route → `wp-security` (planned).

## Step 3: guardrails checklist (always)

- Verify detected tooling before suggesting commands (Composer vs npm/yarn/pnpm).
- Prefer existing lint/test scripts if present.
- If version constraints aren’t detectable, ask for target WP core and PHP versions.
```

## File: `skills/wp-abilities-api/SKILL.md`
```markdown
---
name: wp-abilities-api
description: "Use when working with the WordPress Abilities API (wp_register_ability, wp_register_ability_category, /wp-json/wp-abilities/v1/*, @wordpress/abilities) including defining abilities, categories, meta, REST exposure, and permissions checks for clients."
compatibility: "Targets WordPress 6.9+ (PHP 7.2.24+). Filesystem-based agent with bash + node. Some workflows require WP-CLI."
---

# WP Abilities API

## When to use

Use this skill when the task involves:

- registering abilities or ability categories in PHP,
- exposing abilities to clients via REST (`wp-abilities/v1`),
- consuming abilities in JS (notably `@wordpress/abilities`),
- diagnosing “ability doesn’t show up” / “client can’t see ability” / “REST returns empty”.

## Inputs required

- Repo root (run `wp-project-triage` first if you haven’t).
- Target WordPress version(s) and whether this is WP core or a plugin/theme.
- Where the change should live (plugin vs theme vs mu-plugin).

## Procedure

### 1) Confirm availability and version constraints

- If this is WP core work, check `signals.isWpCoreCheckout` and `versions.wordpress.core`.
- If the project targets WP < 6.9, you may need the Abilities API plugin/package rather than relying on core.

### 2) Find existing Abilities usage

Search for these in the repo:

- `wp_register_ability(`
- `wp_register_ability_category(`
- `wp_abilities_api_init`
- `wp_abilities_api_categories_init`
- `wp-abilities/v1`
- `@wordpress/abilities`

If none exist, decide whether you’re introducing Abilities API fresh (new registrations + client consumption) or only consuming.

### 3) Register categories (optional)

If you need a logical grouping, register an ability category early (see `references/php-registration.md`).

### 4) Register abilities (PHP)

Implement the ability in PHP registration with:

- stable `id` (namespaced),
- `label`/`description`,
- `category`,
- `meta`:
  - add `readonly: true` when the ability is informational,
  - set `show_in_rest: true` for abilities you want visible to clients.

Use the documented init hooks for Abilities API registration so they load at the right time (see `references/php-registration.md`).

### 5) Confirm REST exposure

- Verify the REST endpoints exist and return expected results (see `references/rest-api.md`).
- If the client still can’t see the ability, confirm `meta.show_in_rest` is enabled and you’re querying the right endpoint.

### 6) Consume from JS (if needed)

- Prefer `@wordpress/abilities` APIs for client-side access and checks.
- Ensure build tooling includes the dependency and the project’s build pipeline bundles it.

## Verification

- `wp-project-triage` indicates `signals.usesAbilitiesApi: true` after your change (if applicable).
- REST check (in a WP environment): endpoints under `wp-abilities/v1` return your ability and category when expected.
- If the repo has tests, add/update coverage near:
  - PHP: ability registration and meta exposure
  - JS: ability consumption and UI gating

## Failure modes / debugging

- Ability never appears:
  - registration code not running (wrong hook / file not loaded),
  - missing `meta.show_in_rest`,
  - incorrect category/ID mismatch.
- REST shows ability but JS doesn’t:
  - wrong REST base/namespace,
  - JS dependency not bundled,
  - caching (object/page caches) masking changes.

## Escalation

- If you’re uncertain about version support, confirm target WP core versions and whether Abilities API is expected from core or as a plugin.
- For canonical details, consult:
  - `references/rest-api.md`
  - `references/php-registration.md`
```

## File: `skills/wp-abilities-api/references/php-registration.md`
```markdown
# PHP registration quick guide

Key concepts and entrypoints for the WordPress Abilities API:

- Register ability categories and abilities in PHP.
- Use the Abilities API init hooks to ensure registration occurs at the right lifecycle time.

## Hook order (critical)

**Categories must be registered before abilities.** Use the correct hooks:

1. `wp_abilities_api_categories_init` — Register categories here first.
2. `wp_abilities_api_init` — Register abilities here (after categories exist).

**Warning:** Registering abilities outside `wp_abilities_api_init` triggers `_doing_it_wrong()` and the registration will fail.

```php
// 1. Register category first
add_action( 'wp_abilities_api_categories_init', function() {
    wp_register_ability_category( 'my-plugin', [
        'label' => __( 'My Plugin', 'my-plugin' ),
    ] );
} );

// 2. Then register abilities
add_action( 'wp_abilities_api_init', function() {
    wp_register_ability( 'my-plugin/get-info', [
        'label'       => __( 'Get Site Info', 'my-plugin' ),
        'description' => __( 'Returns basic site information.', 'my-plugin' ),
        'category'    => 'my-plugin',
        'execute_callback' => 'my_plugin_get_info_callback',
        'meta'        => [ 'show_in_rest' => true ],
    ] );
} );
```

## Common primitives

- `wp_register_ability_category( $category_id, $args )`
- `wp_register_ability( $ability_id, $args )`

## Key arguments for `wp_register_ability()`

| Argument | Description |
|----------|-------------|
| `label` | Human-readable name for UI (e.g., command palette) |
| `description` | What the ability does |
| `category` | Category ID (must be registered first) |
| `execute_callback` | Function that executes the ability |
| `input_schema` | JSON Schema for expected input (enables validation) |
| `output_schema` | JSON Schema for returned output |
| `permission_callback` | Optional function to check if current user can execute |
| `meta.show_in_rest` | Set `true` to expose via REST API |
| `meta.readonly` | Set `true` if ability is informational only |

## Recommended patterns

- Namespace IDs (e.g. `my-plugin:feature.edit`).
- Treat IDs as stable API; changing IDs is a breaking change.
- Use `input_schema` and `output_schema` for validation and to help AI agents understand usage.
- Always include a `permission_callback` for abilities that modify data.

## References

- Abilities API handbook: https://developer.wordpress.org/apis/abilities-api/
- Dev note: https://make.wordpress.org/core/2025/11/10/abilities-api-in-wordpress-6-9/
```

## File: `skills/wp-abilities-api/references/rest-api.md`
```markdown
# REST API quick guide (`wp-abilities/v1`)

The Abilities API exposes endpoints under the REST namespace:

- `wp-abilities/v1/abilities`
- `wp-abilities/v1/categories`

Debug checklist:

- Confirm the route exists under `wp-json/wp-abilities/v1/...`.
- Verify the ability/category shows in REST responses.
- If missing, confirm `meta.show_in_rest` is enabled for that ability.

```

## File: `skills/wp-block-development/SKILL.md`
```markdown
---
name: wp-block-development
description: "Use when developing WordPress (Gutenberg) blocks: block.json metadata, register_block_type(_from_metadata), attributes/serialization, supports, dynamic rendering (render.php/render_callback), deprecations/migrations, viewScript vs viewScriptModule, and @wordpress/scripts/@wordpress/create-block build and test workflows."
compatibility: "Targets WordPress 6.9+ (PHP 7.2.24+). Filesystem-based agent with bash + node. Some workflows require WP-CLI."
---

# WP Block Development

## When to use

Use this skill for block work such as:

- creating a new block, or updating an existing one
- changing `block.json` (scripts/styles/supports/attributes/render/viewScriptModule)
- fixing “block invalid / not saving / attributes not persisting”
- adding dynamic rendering (`render.php` / `render_callback`)
- block deprecations and migrations (`deprecated` versions)
- build tooling for blocks (`@wordpress/scripts`, `@wordpress/create-block`, `wp-env`)

## Inputs required

- Repo root and target (plugin vs theme vs full site).
- The block name/namespace and where it lives (path to `block.json` if known).
- Target WordPress version range (especially if using modules / `viewScriptModule`).

## Procedure

### 0) Triage and locate blocks

1. Run triage:
   - `node skills/wp-project-triage/scripts/detect_wp_project.mjs`
2. List blocks (deterministic scan):
   - `node skills/wp-block-development/scripts/list_blocks.mjs`
3. Identify the block root (directory containing `block.json`) you’re changing.

If this repo is a full site (`wp-content/` present), be explicit about *which* plugin/theme contains the block.

### 1) Create a new block (if needed)

If you are creating a new block, prefer scaffolding rather than hand-rolling structure:

- Use `@wordpress/create-block` to scaffold a modern block/plugin setup.
- If you need Interactivity API from day 1, use the interactive template.

Read:
- `references/creating-new-blocks.md`

After scaffolding:

1. Re-run the block list script and confirm the new block root.
2. Continue with the remaining steps (model choice, metadata, registration, serialization).

### 2) Ensure apiVersion 3 (WordPress 6.9+)

WordPress 6.9 enforces `apiVersion: 3` in the block.json schema. Blocks with apiVersion 2 or lower trigger console warnings when `SCRIPT_DEBUG` is enabled.

**Why this matters:**
- WordPress 7.0 will run the post editor in an iframe regardless of block apiVersion.
- apiVersion 3 ensures your block works correctly inside the iframed editor (style isolation, viewport units, media queries).

**Migration:** Changing from version 2 to 3 is usually as simple as updating the `apiVersion` field in `block.json`. However:
- Test in a local environment with the iframe editor enabled.
- Ensure any style handles are included in `block.json` (styles missing from the iframe won't apply).
- Third-party scripts attached to a specific `window` may have scoping issues.

Read:
- `references/block-json.md` (apiVersion and schema details)

### 3) Pick the right block model

- **Static block** (markup saved into post content): implement `save()`; keep attributes serialization stable.
- **Dynamic block** (server-rendered): use `render` in `block.json` (or `render_callback` in PHP) and keep `save()` minimal or `null`.
- **Interactive frontend behavior**:
  - Prefer `viewScriptModule` for modern module-based view scripts where supported.
  - If you're working primarily on `data-wp-*` directives or stores, also use `wp-interactivity-api`.

### 4) Update `block.json` safely

Make changes in the block’s `block.json`, then confirm registration matches metadata.

For field-by-field guidance, read:
- `references/block-json.md`

Common pitfalls:

- changing `name` breaks compatibility (treat it as stable API)
- changing saved markup without adding `deprecated` causes “Invalid block”
- adding attributes without defining source/serialization correctly causes “attribute not saving”

### 5) Register the block (server-side preferred)

Prefer PHP registration using metadata, especially when:

- you need dynamic rendering
- you need translations (`wp_set_script_translations`)
- you need conditional asset loading

Read and apply:
- `references/registration.md`

### 6) Implement edit/save/render patterns

Follow wrapper attribute best practices:

- Editor: `useBlockProps()`
- Static save: `useBlockProps.save()`
- Dynamic render (PHP): `get_block_wrapper_attributes()`

Read:
- `references/supports-and-wrappers.md`
- `references/dynamic-rendering.md` (if dynamic)

### 7) Inner blocks (block composition)

If your block is a “container” that nests other blocks, treat Inner Blocks as a first-class feature:

- Use `useInnerBlocksProps()` to integrate inner blocks with wrapper props.
- Keep migrations in mind if you change inner markup.

Read:
- `references/inner-blocks.md`

### 8) Attributes and serialization

Before changing attributes:

- confirm where the attribute value lives (comment delimiter vs HTML vs context)
- avoid the deprecated `meta` attribute source

Read:
- `references/attributes-and-serialization.md`

### 9) Migrations and deprecations (avoid "Invalid block")

If you change saved markup or attributes:

1. Add a `deprecated` entry (newest → oldest).
2. Provide `save` for old versions and an optional `migrate` to normalize attributes.

Read:
- `references/deprecations.md`

### 10) Tooling and verification commands

Prefer whatever the repo already uses:

- `@wordpress/scripts` (common) → run existing npm scripts
- `wp-env` (common) → use for local WP + E2E

Read:
- `references/tooling-and-testing.md`

## Verification

- Block appears in inserter and inserts successfully.
- Saving + reloading does not create “Invalid block”.
- Frontend output matches expectations (static: saved markup; dynamic: server output).
- Assets load where expected (editor vs frontend).
- Run the repo’s lint/build/tests that triage recommends.

## Failure modes / debugging

If something fails, start here:

- `references/debugging.md` (common failures + fastest checks)
- `references/attributes-and-serialization.md` (attributes not saving)
- `references/deprecations.md` (invalid block after change)

## Escalation

If you’re uncertain about upstream behavior/version support, consult canonical docs first:

- WordPress Developer Resources (Block Editor Handbook, Theme Handbook, Plugin Handbook)
- Gutenberg repo docs for bleeding-edge behaviors
```

## File: `skills/wp-block-development/references/attributes-and-serialization.md`
```markdown
# Attributes and serialization

Use this file when attributes aren’t saving, content becomes “Invalid block”, or you’re changing markup.

## How attributes persist

Attributes can come from:

- the comment delimiter JSON (common and stable)
- the block’s saved HTML (from tags/attributes)
- context

Read the canonical guide for supported `source`/`selector`/`attribute` patterns:

- https://developer.wordpress.org/block-editor/reference-guides/block-api/block-attributes/

## Common pitfalls

- Changing saved HTML without a `deprecated` version breaks existing posts.
- Using the `meta` attribute source (deprecated) causes long-term pain; avoid it.
- Choosing brittle selectors leads to attributes “not found” when markup changes slightly.

```

## File: `skills/wp-block-development/references/block-json.md`
```markdown
# `block.json` (metadata) guidance

Use this file when you’re editing `block.json` fields or choosing between script/styles fields.

## Practical rules

- Treat `name` as stable API (renaming breaks existing content).
- Prefer adding new functionality without changing saved markup; if markup must change, add a `deprecated` version.
- Keep assets scoped: editor assets should not ship to frontend unless needed.

## API version + schema

**WordPress 6.9+ requires apiVersion 3.** The block.json schema now only validates blocks with `apiVersion: 3`. Older versions (1 or 2) trigger console warnings when `SCRIPT_DEBUG` is enabled.

**Why apiVersion 3 matters:**
- The post editor will be iframed if all registered blocks have apiVersion 3+.
- WordPress 7.0 will always use the iframe editor regardless of apiVersion.
- Benefits: style isolation (admin CSS won't affect editor content), correct viewport units (vw, vh), native media queries.

**Migration checklist:**
1. Update `apiVersion` to `3` in block.json.
2. Ensure all style handles are declared in block.json (styles not included won't load in the iframe).
3. Test blocks that rely on third-party scripts (window scoping may differ).
4. Add a `$schema` to improve editor tooling and validation.

References:

- Block metadata: https://developer.wordpress.org/block-editor/reference-guides/block-api/block-metadata/
- Block API versions: https://developer.wordpress.org/block-editor/reference-guides/block-api/block-api-versions/
- Iframe migration guide: https://developer.wordpress.org/block-editor/reference-guides/block-api/block-api-versions/block-migration-for-iframe-editor-compatibility/
- Block schema index: https://schemas.wp.org/

## Modern asset fields to know

This is not a full schema; it’s a “what matters in practice” list:

- `editorScript` / `editorStyle`: editor-only assets.
- `script` / `style`: shared assets.
- `viewScript` / `viewStyle`: frontend view assets.
- `viewScriptModule`: module-based frontend scripts (newer WP).
- `render`: points to a PHP render file for dynamic blocks (newer WP).

## Helpful upstream references

- Block metadata reference (block.json):
  - https://developer.wordpress.org/block-editor/reference-guides/block-api/block-metadata/
- Block.json schema (editor tooling):
  - https://schemas.wp.org/trunk/block.json

```

## File: `skills/wp-block-development/references/creating-new-blocks.md`
```markdown
# Creating new blocks (scaffolding)

Use this file when you are creating a new block (or a new block plugin) from scratch.

## Preferred path: `@wordpress/create-block`

`@wordpress/create-block` scaffolds a modern block setup that tends to track current best practices.

Typical options to decide up front:

- TypeScript vs JavaScript
- Static vs dynamic (`render.php` / server rendering)
- Whether the block should be interactive on the frontend

Canonical docs:

- https://developer.wordpress.org/block-editor/reference-guides/packages/packages-create-block/

## “Most up-to-date” interactive blocks

For a modern interactive block, prefer the official Interactivity API template:

- Template: `@wordpress/create-block-interactive-template`

This template is designed to integrate:

- Interactivity API directives (`data-wp-*`)
- module-based view scripts (`viewScriptModule`)
- server rendering (`render.php`)

References:

- https://developer.wordpress.org/block-editor/reference-guides/packages/packages-create-block/
- https://make.wordpress.org/core/2024/03/04/a-first-look-at-the-interactivity-api-in-wordpress-6-5/

## Manual fallback (when scaffolding is not available)

If you cannot run `create-block` (no Node tooling or restricted network):

1. Create a plugin or theme location that will register the block.
2. Create a block folder with a valid `block.json`.
3. Register via `register_block_type_from_metadata()` in PHP.
4. Add editor JS and (optionally) frontend view assets.

Then follow the rest of `wp-block-development` for metadata, registration, and serialization.

```

## File: `skills/wp-block-development/references/debugging.md`
```markdown
# Debugging quick routes

## Block doesn’t appear in inserter

- Confirm `block.json` `name` is valid and the block is registered.
- Confirm build output exists and scripts are enqueued.
- If using PHP registration, confirm `register_block_type_from_metadata()` runs (wrong hook/file not loaded is common).

## “This block contains unexpected or invalid content”

- You changed saved markup or attribute parsing.
- Add `deprecated` versions and a migration path.
- Reproduce with an old post containing the previous markup.

## Attributes not saving

- Confirm attribute definition matches actual markup.
- If the value is in delimiter JSON, avoid brittle selectors.
- Avoid `meta` attribute source (deprecated).

## Console warnings about apiVersion (WordPress 6.9+)

If you see "The block 'namespace/block' is registered with API version 2 or lower":

- Update `apiVersion` to `3` in block.json.
- This warning only appears when `SCRIPT_DEBUG` is true.
- WordPress 7.0 will require apiVersion 3 for proper iframe editor support.

## Styles not applying in editor (apiVersion 3 / iframe)

If styles work on frontend but not in the editor:

- Ensure style handles are declared in block.json (`editorStyle`, `style`).
- Styles not included in block.json won't load inside the iframed editor.
- Check for Dashicons or other dependencies that need explicit inclusion.

```

## File: `skills/wp-block-development/references/deprecations.md`
```markdown
# Deprecations and migrations

Use this file when you must change saved markup or attribute shapes without breaking existing content.

## `deprecated` basics

Block deprecations are handled in JS block registration.

- Add older implementations to `deprecated` (newest → oldest).
- Each deprecated entry can include:
  - `attributes`
  - `supports`
  - `save`
  - `migrate`

Upstream reference:

- https://developer.wordpress.org/block-editor/reference-guides/block-api/block-deprecation/

## Practical guardrails

- Keep fixtures: store example content for each deprecated version.
- When in doubt, add a migration path rather than silently changing selectors.

```

## File: `skills/wp-block-development/references/dynamic-rendering.md`
```markdown
# Dynamic blocks (server rendering)

Use this file when converting a block to dynamic, or debugging frontend output mismatch.

## Choose the mechanism

- Prefer `render` in `block.json` (dynamic render file).
- Alternative: pass `render_callback` when registering the block in PHP.

## Wrapper attributes

In PHP render output, always use:

- `get_block_wrapper_attributes()`

This preserves support-generated classes/styles.

## Practical checklist

- Ensure PHP file exists and is reachable from the block root.
- Ensure registration runs on every request (not only in admin).
- Keep `save()` empty or `null` for fully dynamic output, unless you intentionally save fallback markup.

```

## File: `skills/wp-block-development/references/inner-blocks.md`
```markdown
# Inner Blocks (nested blocks)

Use this file when your block contains other blocks (container blocks).

## Canonical references

- Nested blocks guide: https://developer.wordpress.org/block-editor/how-to-guides/block-tutorial/nested-blocks-inner-blocks/
- `@wordpress/block-editor` package: https://developer.wordpress.org/block-editor/reference-guides/packages/packages-block-editor/
- Block supports: https://developer.wordpress.org/block-editor/reference-guides/block-api/block-supports/

## Practical patterns

- Editor:
  - Use `useInnerBlocksProps( useBlockProps(), { ... } )` to combine wrapper props with inner blocks.
  - Use templates/allowed blocks only when you have a clear UX reason (too strict is frustrating).
- Save:
  - Use `useInnerBlocksProps.save( useBlockProps.save(), { ... } )` if you need wrapper props.
  - Output nested content via `<InnerBlocks.Content />` when appropriate.

## Common pitfalls

- Only one `InnerBlocks` should exist per block.
- Changing the wrapper structure that contains inner blocks can invalidate existing content; consider deprecations/migrations.
- If you need to constrain allowed blocks, prefer doing it intentionally and documenting why.

```

## File: `skills/wp-block-development/references/registration.md`
```markdown
# Registration patterns (PHP-first)

Use this file when you need to register blocks robustly across repo types (plugin/theme/site).

## Prefer metadata registration

Prefer:

- `register_block_type_from_metadata( $path_to_block_dir, $args = [] )`

Why:

- keeps metadata authoritative (`block.json`)
- supports dynamic render (`render`) and other metadata-driven fields
- enables cleaner asset handling

Upstream reference:

- https://developer.wordpress.org/reference/functions/register_block_type_from_metadata/

## Where to register

- Plugins: register on `init` in the main plugin bootstrap or a dedicated loader.
- Themes: register on `init` (or `after_setup_theme` if you need theme supports first), but keep it predictable.

## Dynamic render mapping

If `block.json` includes `render`, ensure the file exists relative to the block root.
Inside the render file, use `get_block_wrapper_attributes()` for wrapper attributes.

```

## File: `skills/wp-block-development/references/supports-and-wrappers.md`
```markdown
# Supports and wrapper attributes

Use this file when changing `supports` or when your block wrapper styling behaves unexpectedly.

## Required patterns

- In `edit()`, use `useBlockProps()`.
- In `save()`, use `useBlockProps.save()`.

If the block is dynamic (PHP render), use:

- `get_block_wrapper_attributes()`

Upstream reference:

- https://developer.wordpress.org/block-editor/reference-guides/block-api/block-supports/
- https://developer.wordpress.org/reference/functions/get_block_wrapper_attributes/

```

## File: `skills/wp-block-development/references/tooling-and-testing.md`
```markdown
# Tooling and testing

Use this file when deciding what commands to run and what “good verification” looks like.

## Common toolchains

- `@wordpress/scripts` for build/lint/test:
  - https://developer.wordpress.org/block-editor/reference-guides/packages/packages-scripts/
- `@wordpress/create-block` to scaffold new blocks:
  - https://developer.wordpress.org/block-editor/reference-guides/packages/packages-create-block/
- Interactivity API template for `create-block`:
  - https://www.npmjs.com/package/@wordpress/create-block-interactive-template
- `@wordpress/env` (wp-env) for local WordPress environments:
  - https://developer.wordpress.org/block-editor/reference-guides/packages/packages-env/

## Verification checklist

- `npm run build` (or repo equivalent) succeeds.
- JS lint passes (repo-specific).
- E2E tests pass if present.
- Manual: insert block, save post, reload editor, confirm no “Invalid block”.
```

## File: `skills/wp-block-development/scripts/list_blocks.mjs`
```
import fs from "node:fs";
import path from "node:path";

const DEFAULT_IGNORES = new Set([
  ".git",
  "node_modules",
  "vendor",
  "dist",
  "build",
  "coverage",
  ".next",
  ".turbo",
]);

function statSafe(p) {
  try {
    return fs.statSync(p);
  } catch {
    return null;
  }
}

function existsDir(p) {
  const st = statSafe(p);
  return Boolean(st && st.isDirectory());
}

function readJsonSafe(p) {
  try {
    return JSON.parse(fs.readFileSync(p, "utf8"));
  } catch {
    return null;
  }
}

function findFilesRecursive(repoRoot, predicate, { maxFiles = 6000, maxDepth = 10 } = {}) {
  const results = [];
  const queue = [{ dir: repoRoot, depth: 0 }];
  let visited = 0;

  while (queue.length > 0) {
    const { dir, depth } = queue.shift();
    if (depth > maxDepth) continue;

    let entries;
    try {
      entries = fs.readdirSync(dir, { withFileTypes: true });
    } catch {
      continue;
    }

    for (const ent of entries) {
      const fullPath = path.join(dir, ent.name);
      if (ent.isDirectory()) {
        if (DEFAULT_IGNORES.has(ent.name)) continue;
        queue.push({ dir: fullPath, depth: depth + 1 });
        continue;
      }
      if (!ent.isFile()) continue;

      visited += 1;
      if (visited > maxFiles) return { results, truncated: true };
      if (predicate(fullPath)) results.push(fullPath);
    }
  }

  return { results, truncated: false };
}

function summarizeBlockJson(repoRoot, blockJsonPath) {
  const json = readJsonSafe(blockJsonPath);
  if (!json) {
    return {
      path: path.relative(repoRoot, blockJsonPath),
      error: "invalid-json",
    };
  }

  const rel = path.relative(repoRoot, blockJsonPath);
  const blockRoot = path.dirname(rel);

  return {
    path: rel,
    blockRoot,
    name: typeof json?.name === "string" ? json.name : null,
    title: typeof json?.title === "string" ? json.title : null,
    apiVersion: typeof json?.apiVersion === "number" ? json.apiVersion : null,
    render: typeof json?.render === "string" ? json.render : null,
    viewScript: json?.viewScript ?? null,
    viewScriptModule: json?.viewScriptModule ?? null,
    editorScript: json?.editorScript ?? null,
    script: json?.script ?? null,
    style: json?.style ?? null,
    editorStyle: json?.editorStyle ?? null,
    attributes: json?.attributes ? Object.keys(json.attributes).slice(0, 50) : [],
  };
}

function main() {
  const repoRoot = process.cwd();

  const { results: blockJsonFiles, truncated } = findFilesRecursive(repoRoot, (p) => path.basename(p) === "block.json", {
    maxFiles: 8000,
    maxDepth: 12,
  });

  const blocks = blockJsonFiles.map((p) => summarizeBlockJson(repoRoot, p));

  const report = {
    tool: { name: "list_blocks", version: "0.1.0" },
    repoRoot,
    truncated,
    count: blocks.length,
    blocks,
  };

  process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
}

main();

```

## File: `skills/wp-block-themes/SKILL.md`
```markdown
---
name: wp-block-themes
description: "Use when developing WordPress block themes: theme.json (global settings/styles), templates and template parts, patterns, style variations, and Site Editor troubleshooting (style hierarchy, overrides, caching)."
compatibility: "Targets WordPress 6.9+ (PHP 7.2.24+). Filesystem-based agent with bash + node. Some workflows require WP-CLI."
---

# WP Block Themes

## When to use

Use this skill for block theme work such as:

- editing `theme.json` (presets, settings, styles, per-block styles)
- adding or changing templates (`templates/*.html`) and template parts (`parts/*.html`)
- adding patterns (`patterns/*.php`) and controlling what appears in the inserter
- adding style variations (`styles/*.json`)
- debugging “styles not applying” / “editor doesn’t reflect theme.json”

## Inputs required

- Repo root and which theme is targeted (theme directory if multiple exist).
- Target WordPress version range (theme.json version and features vary by core version).
- Where the issue manifests: Site Editor, post editor, frontend, or all.

## Procedure

### 0) Triage and locate block theme roots

1. Run triage:
   - `node skills/wp-project-triage/scripts/detect_wp_project.mjs`
2. Detect theme roots + key folders:
   - `node skills/wp-block-themes/scripts/detect_block_themes.mjs`

If multiple themes exist, pick one and scope all changes to that theme root.

### 1) Create a new block theme (if needed)

If you are creating a new block theme from scratch (or converting a classic theme):

- Prefer starting from a known-good scaffold (or exporting from a WP environment) rather than guessing file layout.
- Be explicit about the minimum supported WordPress version because `theme.json` schema versions differ.

Read:
- `references/creating-new-block-theme.md`

After creating the theme root, re-run `detect_block_themes` and continue below.

### 2) Confirm theme type and override expectations

- Block theme indicators:
  - `theme.json` present
  - `templates/` and/or `parts/` present
- Remember the style hierarchy:
  - core defaults → theme.json → child theme → user customizations
  - user customizations can make theme.json edits appear “ignored”

Read:
- `references/debugging.md` (style hierarchy + fastest checks)

### 3) Make `theme.json` changes safely

Decide whether you are changing:

- **settings** (what the UI allows): presets, typography scale, colors, layout, spacing
- **styles** (how it looks by default): CSS-like rules for elements/blocks

Read:
- `references/theme-json.md`

### 4) Templates and template parts

- Templates live under `templates/` and are HTML.
- Template parts live under `parts/` and must not be nested in subdirectories.

Read:
- `references/templates-and-parts.md`

### 5) Patterns

Prefer filesystem patterns under `patterns/` when you want theme-owned patterns.

Read:
- `references/patterns.md`

### 6) Style variations

Style variations are JSON files under `styles/`. Note: once a user picks a style variation, that selection is stored in the DB, so changing the file may not “update what the user sees” automatically.

Read:
- `references/style-variations.md`

## Verification

- Site Editor reflects changes where expected (Styles UI, templates, patterns).
- Frontend renders with expected styles.
- If styles aren’t changing, confirm whether user customizations override theme defaults.
- Run the repo’s build/lint scripts if assets are involved (fonts, custom JS/CSS build).

## Failure modes / debugging

Start with:

- `references/debugging.md`

Common issues:

- wrong theme root (editing an inactive theme)
- user customizations override your defaults
- invalid `theme.json` shape/typos prevent application
- templates/parts in wrong folders (or nested parts)

## Escalation

If upstream behavior is unclear, consult canonical docs:

- Theme Handbook and Block Editor Handbook for `theme.json`, templates, patterns, and style variations.
```

## File: `skills/wp-block-themes/references/creating-new-block-theme.md`
```markdown
# Creating a new block theme

Use this file when you need to create a new block theme or convert a theme to block theme structure.

## Two practical starting points

1. **Export from a WP environment**
   - Use the official “Create Block Theme” plugin to generate/export a theme from the Site Editor.
   - This tends to produce a structure aligned with current WordPress behavior.

2. **Create the minimal filesystem structure**
   - Create a theme folder with:
     - `style.css` (theme header)
     - `theme.json` (global settings/styles)
     - `templates/index.html` (minimum viable template)
     - `parts/header.html` and `parts/footer.html` (recommended)

## References

- Create Block Theme plugin:
  - https://wordpress.org/plugins/create-block-theme/
- Block theme structure:
  - https://developer.wordpress.org/themes/block-themes/theme-structure/
- Required templates:
  - https://developer.wordpress.org/themes/block-themes/templates-and-template-parts/

## theme.json version choice (compatibility)

`theme.json` has schema versions. Pick the highest version that matches your minimum supported WordPress version.

References:

- Theme Handbook introduction:
  - https://developer.wordpress.org/themes/global-settings-and-styles/introduction-to-theme-json/
- Theme.json version 3 dev note:
  - https://make.wordpress.org/core/2024/06/19/theme-json-version-3/

```

## File: `skills/wp-block-themes/references/debugging.md`
```markdown
# Debugging block theme issues

## Styles not applying

Fast checks:

1. Confirm you edited the active theme (Site Editor → theme).
2. Check if user customizations exist (they override theme defaults).
3. Validate `theme.json` structure (typos can prevent styles from applying).

Remember the hierarchy:

- core defaults → theme.json → child theme → user customizations

## Templates/parts not showing

- Ensure files are in the correct folders (`templates/`, `parts/`).
- Template parts must not be nested in subdirectories.

## Style variations not updating

- If a user already selected the variation, the selection is stored in the DB.
- Test with a fresh site/user or reset customizations when appropriate.

```

## File: `skills/wp-block-themes/references/patterns.md`
```markdown
# Patterns (filesystem patterns)

Use this file when adding patterns that should be available in the inserter.

## Filesystem patterns

- Put patterns in `patterns/*.php`.
- Patterns are registered automatically by WordPress core based on file headers.

Upstream reference:

- https://developer.wordpress.org/themes/patterns/

## Practical guardrails

- Keep pattern markup stable; changing block names inside patterns can break older content in subtle ways.
- If a pattern should not be inserted directly by users, mark it as non-inserter / internal-only (per upstream header conventions).

```

## File: `skills/wp-block-themes/references/style-variations.md`
```markdown
# Style variations (`styles/*.json`)

Use this file when adding or debugging style variations.

Key points:

- Style variations are JSON files in `styles/`.
- Users can pick a style variation in the UI.
- Once selected, the choice is stored in the DB (so “changing the JSON file” may not update what a user already selected).

Upstream reference:

- https://developer.wordpress.org/themes/global-settings-and-styles/style-variations/

```

## File: `skills/wp-block-themes/references/templates-and-parts.md`
```markdown
# Templates and template parts

Use this file when creating or editing HTML templates/parts.

## Key folders

- `templates/` for templates.
- `parts/` for template parts.

Template parts must not be nested in subdirectories.

Upstream references:

- Templates + parts overview: https://developer.wordpress.org/themes/block-themes/theme-structure/
- Template parts details: https://developer.wordpress.org/themes/block-themes/template-parts/

```

## File: `skills/wp-block-themes/references/theme-json.md`
```markdown
# `theme.json` guidance

Use this file when changing global settings/styles or per-block styling.

## High-level structure

Common top-level keys:

- `version`
- `settings` (what the UI exposes / allows)
- `styles` (default appearance)
- `customTemplates` and `templateParts` (optional, to describe templates and parts)

Upstream references:

- Theme Handbook: https://developer.wordpress.org/themes/global-settings-and-styles/
- Block Editor Handbook (often more current): https://developer.wordpress.org/block-editor/how-to-guides/themes/theme-json/
- Theme JSON living reference: https://developer.wordpress.org/block-editor/reference-guides/theme-json-reference/theme-json-living/
- Theme JSON version 3 (dev note): https://make.wordpress.org/core/2024/06/19/theme-json-version-3/

## Practical guardrails

- Prefer presets when you want editor-visible controls (colors, font sizes, spacing).
- Prefer `styles` when you want consistent defaults without requiring user choice.
- Be careful with specificity: user global styles override theme defaults.

## WordPress 6.9 additions

**Form element styling:**
- Style text inputs and selects via `styles.elements` (e.g., `styles.elements.input`, `styles.elements.select`).
- Supports border, color, outline, shadow, and spacing properties.
- Note: Focus state styling is not yet available in 6.9.

**Border radius presets:**
- Define presets in `settings.border.radiusSizes` for visual selection in the border radius control.
- Users can still enter custom values.

```json
{
  "settings": {
    "border": {
      "radiusSizes": [
        { "name": "Small", "slug": "small", "size": "4px" },
        { "name": "Medium", "slug": "medium", "size": "8px" },
        { "name": "Large", "slug": "large", "size": "16px" }
      ]
    }
  }
}
```

**Button pseudo-classes:**
- Style Button block hover and focus states directly in theme.json.
- No longer requires custom CSS for simple button state styling.

References:

- Border radius presets: https://make.wordpress.org/core/2025/11/12/theme-json-border-radius-presets-support-in-wordpress-6-9/
- Form element styling: https://developer.wordpress.org/news/2025/11/how-wordpress-6-9-gives-forms-a-theme-json-makeover/
```

## File: `skills/wp-block-themes/scripts/detect_block_themes.mjs`
```
import fs from "node:fs";
import path from "node:path";

const DEFAULT_IGNORES = new Set([
  ".git",
  "node_modules",
  "vendor",
  "dist",
  "build",
  "coverage",
  ".next",
  ".turbo",
]);

function statSafe(p) {
  try {
    return fs.statSync(p);
  } catch {
    return null;
  }
}

function existsDir(p) {
  const st = statSafe(p);
  return Boolean(st && st.isDirectory());
}

function readJsonSafe(p) {
  try {
    return JSON.parse(fs.readFileSync(p, "utf8"));
  } catch {
    return null;
  }
}

function findFilesRecursive(repoRoot, predicate, { maxFiles = 6000, maxDepth = 10 } = {}) {
  const results = [];
  const queue = [{ dir: repoRoot, depth: 0 }];
  let visited = 0;

  while (queue.length > 0) {
    const { dir, depth } = queue.shift();
    if (depth > maxDepth) continue;

    let entries;
    try {
      entries = fs.readdirSync(dir, { withFileTypes: true });
    } catch {
      continue;
    }

    for (const ent of entries) {
      const fullPath = path.join(dir, ent.name);
      if (ent.isDirectory()) {
        if (DEFAULT_IGNORES.has(ent.name)) continue;
        queue.push({ dir: fullPath, depth: depth + 1 });
        continue;
      }
      if (!ent.isFile()) continue;

      visited += 1;
      if (visited > maxFiles) return { results, truncated: true };
      if (predicate(fullPath)) results.push(fullPath);
    }
  }

  return { results, truncated: false };
}

function summarizeTheme(repoRoot, themeJsonPath) {
  const json = readJsonSafe(themeJsonPath);
  const rel = path.relative(repoRoot, themeJsonPath);
  const rootDir = path.dirname(rel);

  const templatesDir = path.join(repoRoot, rootDir, "templates");
  const partsDir = path.join(repoRoot, rootDir, "parts");
  const patternsDir = path.join(repoRoot, rootDir, "patterns");
  const stylesDir = path.join(repoRoot, rootDir, "styles");

  const hasTemplates = existsDir(templatesDir);
  const hasParts = existsDir(partsDir);

  return {
    themeRoot: rootDir,
    themeJson: rel,
    version: typeof json?.version === "number" ? json.version : null,
    hasTemplates,
    hasParts,
    hasPatterns: existsDir(patternsDir),
    hasStyles: existsDir(stylesDir),
    isBlockTheme: hasTemplates || hasParts,
  };
}

function main() {
  const repoRoot = process.cwd();

  const { results: themeJsonFiles, truncated } = findFilesRecursive(repoRoot, (p) => path.basename(p) === "theme.json", {
    maxFiles: 8000,
    maxDepth: 12,
  });

  const themes = themeJsonFiles.map((p) => summarizeTheme(repoRoot, p));

  const report = {
    tool: { name: "detect_block_themes", version: "0.1.0" },
    repoRoot,
    truncated,
    count: themes.length,
    themes,
  };

  process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
}

main();

```

## File: `skills/wp-interactivity-api/SKILL.md`
```markdown
---
name: wp-interactivity-api
description: "Use when building or debugging WordPress Interactivity API features (data-wp-* directives, @wordpress/interactivity store/state/actions, block viewScriptModule integration, wp_interactivity_*()) including performance, hydration, and directive behavior."
compatibility: "Targets WordPress 6.9+ (PHP 7.2.24+). Filesystem-based agent with bash + node. Some workflows require WP-CLI."
---

# WP Interactivity API

## When to use

Use this skill when the user mentions:

- Interactivity API, `@wordpress/interactivity`,
- `data-wp-interactive`, `data-wp-on--*`, `data-wp-bind--*`, `data-wp-context`,
- block `viewScriptModule` / module-based view scripts,
- hydration issues or “directives don’t fire”.

## Inputs required

- Repo root + triage output (`wp-project-triage`).
- Which block/theme/plugin surfaces are affected (frontend, editor, both).
- Any constraints: WP version, whether modules are supported in the build.

## Procedure

### 1) Detect existing usage + integration style

Search for:

- `data-wp-interactive`
- `@wordpress/interactivity`
- `viewScriptModule`

Decide:

- Is this a block providing interactivity via `block.json` view script module?
- Is this theme-level interactivity?
- Is this plugin-side “enhance existing markup” usage?

If you’re creating a new interactive block (not just debugging), prefer the official scaffold template:

- `@wordpress/create-block-interactive-template` (via `@wordpress/create-block`)

### 2) Identify the store(s)

Locate store definitions and confirm:

- state shape,
- actions (mutations),
- callbacks/event handlers used by `data-wp-on--*`.

### 3) Server-side rendering (best practice)

**Pre-render HTML on the server** before outputting to ensure:

- Correct initial state in the HTML before JavaScript loads (no layout shift).
- SEO benefits and faster perceived load time.
- Seamless hydration when the client-side JavaScript takes over.

#### Enable server directive processing

For components using `block.json`, add `supports.interactivity`:

```json
{
  "supports": {
    "interactivity": true
  }
}
```

For themes/plugins without `block.json`, use `wp_interactivity_process_directives()` to process directives.

#### Initialize state/context in PHP

Use `wp_interactivity_state()` to define initial global state:

```php
wp_interactivity_state( 'myPlugin', array(
  'items'    => array( 'Apple', 'Banana', 'Cherry' ),
  'hasItems' => true,
));
```

For local context, use `wp_interactivity_data_wp_context()`:

```php
<?php
$context = array( 'isOpen' => false );
?>
<div <?php echo wp_interactivity_data_wp_context( $context ); ?>>
  ...
</div>
```

#### Define derived state in PHP

When derived state affects initial HTML rendering, replicate the logic in PHP:

```php
wp_interactivity_state( 'myPlugin', array(
  'items'    => array( 'Apple', 'Banana' ),
  'hasItems' => function() {
    $state = wp_interactivity_state();
    return count( $state['items'] ) > 0;
  }
));
```

This ensures directives like `data-wp-bind--hidden="!state.hasItems"` render correctly on first load.

For detailed examples and patterns, see `references/server-side-rendering.md`.

### 4) Implement or change directives safely

When touching markup directives:

- keep directive usage minimal and scoped,
- prefer stable data attributes that map clearly to store state,
- ensure server-rendered markup + client hydration align.

**WordPress 6.9 changes:**

- **`data-wp-ignore` is deprecated** and will be removed in future versions. It broke context inheritance and caused issues with client-side navigation. Avoid using it.
- **Unique directive IDs**: Multiple directives of the same type can now exist on one element using the `---` separator (e.g., `data-wp-on--click---plugin-a="..."` and `data-wp-on--click---plugin-b="..."`).
- **New TypeScript types**: `AsyncAction<ReturnType>` and `TypeYield<T>` help with async action typing.

For quick directive reminders, see `references/directives-quickref.md`.

### 5) Build/tooling alignment

Verify the repo supports the required module build path:

- if it uses `@wordpress/scripts`, prefer its conventions.
- if it uses custom bundling, confirm module output is supported.

### 6) Debug common failure modes

If “nothing happens” on interaction:

- confirm the `viewScriptModule` is enqueued/loaded,
- confirm the DOM element has `data-wp-interactive`,
- confirm the store namespace matches the directive’s value,
- confirm there are no JS errors before hydration.

See `references/debugging.md`.

## Verification

- `wp-project-triage` indicates `signals.usesInteractivityApi: true` after your change (if applicable).
- Manual smoke test: directive triggers and state updates as expected.
- If tests exist: add/extend Playwright E2E around the interaction path.

## Failure modes / debugging

- Directives present but inert:
  - view script not loading, wrong module entrypoint, or missing `data-wp-interactive`.
- Hydration mismatch / flicker:
  - server markup differs from client expectations; simplify or align initial state.
  - derived state not defined in PHP: use `wp_interactivity_state()` with closures.
- Initial content missing or wrong:
  - `supports.interactivity` not set in `block.json` (for blocks).
  - `wp_interactivity_process_directives()` not called (for themes/plugins).
  - state/context not initialized in PHP before render.
- Layout shift on load:
  - derived state like `state.hasItems` missing on server, causing `hidden` attribute to be absent.
- Performance regressions:
  - overly broad interactive roots; scope interactivity to smaller subtrees.
- Client-side navigation issues (WordPress 6.9):
  - `getServerState()` and `getServerContext()` now reset between page transitions—ensure your code doesn't assume stale values persist.
  - Router regions now support `attachTo` for rendering overlays (modals, pop-ups) dynamically.

## Escalation

- If repo build constraints are unclear, ask: "Is this using `@wordpress/scripts` or a custom bundler (webpack/vite)?"
- Consult:
  - `references/server-side-rendering.md`
  - `references/directives-quickref.md`
  - `references/debugging.md`
```

## File: `skills/wp-interactivity-api/references/debugging.md`
```markdown
# Debugging checklist

1. Confirm the interactive root exists in the rendered HTML (`data-wp-interactive`).
2. Confirm the view script module is loaded (network + source maps).
3. Confirm store namespace matches what markup expects.
4. Check console for errors before any interaction.
5. Reduce scope:
   - temporarily remove directives to isolate which directive/store path breaks.
6. If hydration mismatch occurs:
   - ensure initial state/context matches server markup.

## WordPress 6.9 specific issues

**State not persisting across navigation:**
- `getServerState()` and `getServerContext()` now reset between client-side page transitions.
- If you relied on stale values persisting, refactor to use the store's reactive state instead.

**Multiple plugins conflicting on same element:**
- Use unique directive IDs with the `---` separator to avoid attribute collisions.
- Example: `data-wp-on--click---my-plugin="actions.handle"`

**`data-wp-ignore` not working:**
- This directive is deprecated in 6.9 and will be removed. It caused context inheritance and navigation bugs.
- Find an alternative approach (conditional rendering, separate interactive regions).

**Router regions / overlays not rendering:**
- WordPress 6.9 adds `attachTo` property for router regions to render overlays anywhere on the page.
- Ensure nested router regions are properly structured.

```

## File: `skills/wp-interactivity-api/references/directives-quickref.md`
```markdown
# Directives quick reference (high level)

Common directives to recognize in markup:

- `data-wp-interactive`: declares an interactive region (and often a store namespace).
- `data-wp-context`: provides server-rendered context/state.
- `data-wp-on--event`: attaches event handlers (e.g. `click`, `submit`).
- `data-wp-on-async--event`: async event handlers (preferred for most actions).
- `data-wp-bind--attr`: binds DOM attributes to state.
- `data-wp-class--name`: toggles CSS classes based on state.

Use these as search anchors when triaging bugs.

## Unique directive IDs (WordPress 6.9+)

HTML doesn't allow duplicate attributes. To attach multiple handlers of the same type from different plugins, use the `---` separator:

```html
<button
  data-wp-on--click---plugin-a="actions.handleA"
  data-wp-on--click---plugin-b="actions.handleB"
>
```

Both handlers will fire. The ID after `---` must be unique per element.

## Deprecated directive

- **`data-wp-ignore`**: Deprecated in WordPress 6.9. It was intended to prevent hydration of a region but broke context inheritance and client-side navigation. Will be removed in future versions. Avoid using it.

```

## File: `skills/wp-interactivity-api/references/server-side-rendering.md`
```markdown
# Server-Side Rendering for Interactivity API

- **Faster initial render**: HTML arrives ready with correct values.
- **No layout shift**: Hidden elements stay hidden from the first paint.
- **SEO benefits**: Search engines see fully rendered content.
- **Graceful degradation**: Content displays correctly even before JavaScript loads.

## Setup Requirements

### 1. Enable Server Directive Processing

**For components using `block.json`:**

```json
{
  "supports": {
    "interactivity": true
  }
}
```

**For themes/plugins without `block.json`:**

Use `wp_interactivity_process_directives()` to manually process directives (see "Themes and Plugins without block.json" section below).

### 2. Initialize Global State with `wp_interactivity_state()`

Define initial state values in PHP before rendering:

```php
wp_interactivity_state( 'myPlugin', array(
  'fruits'    => array( 'Apple', 'Banana', 'Cherry' ),
  'isLoading' => false,
  'count'     => 3,
));
```

The state is serialized and available to client JavaScript automatically.

### 3. Initialize Local Context with `wp_interactivity_data_wp_context()`

For element-scoped context:

```php
<?php
$context = array(
  'isOpen'   => false,
  'itemId'   => 42,
  'itemName' => 'Example',
);
?>
<div
  data-wp-interactive="myPlugin"
  <?php echo wp_interactivity_data_wp_context( $context ); ?>
>
  <button data-wp-on-async--click="actions.toggle">
    Toggle
  </button>
  <div data-wp-bind--hidden="!context.isOpen">
    Content for <?php echo esc_html( $context['itemName'] ); ?>
  </div>
</div>
```

## Derived State on the Server

When derived state affects the initial HTML, define it in PHP to avoid layout shifts.

### Static Derived State

When the derived value is known at render time:

```php
$fruits    = array( 'Apple', 'Banana', 'Cherry' );
$hasFruits = count( $fruits ) > 0;

wp_interactivity_state( 'myPlugin', array(
  'fruits'    => $fruits,
  'hasFruits' => $hasFruits,
));
```

### Dynamic Derived State (using closures)

When the value depends on context (e.g., inside `data-wp-each` loops):

```php
wp_interactivity_state( 'myPlugin', array(
  'fruits'       => array( 'apple', 'banana', 'cherry' ),
  'shoppingList' => array( 'apple', 'cherry' ),
  'onShoppingList' => function() {
    $state   = wp_interactivity_state();
    $context = wp_interactivity_get_context();
    return in_array( $context['item'], $state['shoppingList'] ) ? 'Yes' : 'No';
  },
));
```

The closure is evaluated during directive processing for each element.

## Complete Example: List with Server Rendering

### PHP (render callback or template)

```php
<?php
$fruits = array( 'Apple', 'Banana', 'Cherry' );

wp_interactivity_state( 'myFruitPlugin', array(
  'fruits'    => $fruits,
  'hasFruits' => count( $fruits ) > 0,
  'mango'     => __( 'Mango' ),
));
?>

<div data-wp-interactive="myFruitPlugin">
  <button data-wp-on-async--click="actions.addMango">
    <?php esc_html_e( 'Add Mango' ); ?>
  </button>
  <button data-wp-on-async--click="actions.clearAll">
    <?php esc_html_e( 'Clear All' ); ?>
  </button>

  <ul data-wp-bind--hidden="!state.hasFruits">
    <template data-wp-each="state.fruits">
      <li data-wp-text="context.item"></li>
    </template>
  </ul>

  <p data-wp-bind--hidden="state.hasFruits">
    <?php esc_html_e( 'No fruits available.' ); ?>
  </p>
</div>
```

### JavaScript (view.js)

```javascript
import { store, getContext } from '@wordpress/interactivity';

const { state } = store( 'myFruitPlugin', {
  state: {
    get hasFruits() {
      return state.fruits.length > 0;
    },
  },
  actions: {
    addMango() {
      state.fruits.push( state.mango );
    },
    clearAll() {
      state.fruits = [];
    },
  },
});
```

### Rendered Output (initial HTML)

```html
<div data-wp-interactive="myFruitPlugin">
  <button data-wp-on-async--click="actions.addMango">Add Mango</button>
  <button data-wp-on-async--click="actions.clearAll">Clear All</button>

  <ul>
    <li>Apple</li>
    <li>Banana</li>
    <li>Cherry</li>
  </ul>

  <p hidden>No fruits available.</p>
</div>
```

The `hidden` attribute is added server-side because `state.hasFruits` is true.

## Serializing Values for Client Use

Use `wp_interactivity_state()` to pass server values to client JavaScript:

### Translations

```php
wp_interactivity_state( 'myPlugin', array(
  'labels' => array(
    'add'    => __( 'Add Item', 'textdomain' ),
    'remove' => __( 'Remove Item', 'textdomain' ),
    'empty'  => __( 'No items found', 'textdomain' ),
  ),
));
```

### Ajax URLs and Nonces

```php
wp_interactivity_state( 'myPlugin', array(
  'ajaxUrl' => admin_url( 'admin-ajax.php' ),
  'nonce'   => wp_create_nonce( 'myPlugin_nonce' ),
  'restUrl' => rest_url( 'myPlugin/v1/' ),
));
```

### Client Usage

```javascript
const { state } = store( 'myPlugin', {
  actions: {
    *fetchData() {
      const formData = new FormData();
      formData.append( 'action', 'my_action' );
      formData.append( '_ajax_nonce', state.nonce );

      const response = yield fetch( state.ajaxUrl, {
        method: 'POST',
        body: formData,
      });
      return yield response.json();
    },
  },
});
```

## Themes and Plugins without block.json

For themes or plugins not using `block.json`, use `wp_interactivity_process_directives()`:

```php
<?php
wp_interactivity_state( 'myTheme', array(
  'menuOpen' => false,
));

ob_start();
?>

<nav
  data-wp-interactive="myTheme"
  data-wp-class--is-open="state.menuOpen"
>
  <button data-wp-on-async--click="actions.toggleMenu">
    Menu
  </button>
  <ul data-wp-bind--hidden="!state.menuOpen">
    <li><a href="/">Home</a></li>
    <li><a href="/about">About</a></li>
  </ul>
</nav>

<?php
$html = ob_get_clean();
echo wp_interactivity_process_directives( $html );
```

Only call `wp_interactivity_process_directives()` once at the outermost template level.

## PHP Helper Functions Reference

| Function | Purpose |
|----------|---------|
| `wp_interactivity_state( $namespace, $state )` | Initialize/get global state for a namespace |
| `wp_interactivity_data_wp_context( $context )` | Generate `data-wp-context` attribute |
| `wp_interactivity_get_context( $namespace )` | Get current context during directive processing |
| `wp_interactivity_process_directives( $html )` | Manually process directives (themes/plugins) |

## Common Pitfalls

### Server Directive Processing Not Enabled

**For `block.json` users:** Without `supports.interactivity`, directives are not processed:

```json
{
  "supports": {
    "interactivity": true
  }
}
```

**For themes/plugins:** Ensure `wp_interactivity_process_directives()` is called on the HTML output.

### Derived State Missing on Server

If `state.hasFruits` is only defined in JavaScript, the `hidden` attribute won't be set:

```html
<!-- Without server state: shows briefly then hides (layout shift) -->
<p data-wp-bind--hidden="state.hasFruits">No fruits</p>
```

### State Not Matching Client Expectations

Ensure PHP and JavaScript derived state logic matches:

```php
// PHP
'hasFruits' => count( $fruits ) > 0,
```

```javascript
// JavaScript - must match PHP logic
get hasFruits() {
  return state.fruits.length > 0;
}
```

## External References

- [WordPress: Server-side rendering](https://developer.wordpress.org/block-editor/reference-guides/interactivity-api/core-concepts/server-side-rendering/)
- [WordPress: Understanding global state, local context and derived state](https://developer.wordpress.org/block-editor/reference-guides/interactivity-api/core-concepts/undestanding-global-state-local-context-and-derived-state/)
- [WordPress: Interactivity API Reference](https://developer.wordpress.org/block-editor/reference-guides/interactivity-api/api-reference/)
```

## File: `skills/wp-performance/SKILL.md`
```markdown
---
name: wp-performance
description: "Use when investigating or improving WordPress performance (backend-only agent): profiling and measurement (WP-CLI profile/doctor, Server-Timing, Query Monitor via REST headers), database/query optimization, autoloaded options, object caching, cron, HTTP API calls, and safe verification."
compatibility: "Targets WordPress 6.9+ (PHP 7.2.24+). Backend-only agent; prefers WP-CLI (doctor/profile) when available."
---

# WP Performance (backend-only)

## When to use

Use this skill when:

- a WordPress site/page/endpoint is slow (frontend TTFB, admin, REST, WP-Cron)
- you need a profiling plan and tooling recommendations (WP-CLI profile/doctor, Query Monitor, Xdebug/XHProf, APMs)
- you’re optimizing DB queries, autoloaded options, object caching, cron tasks, or remote HTTP calls

This skill assumes the agent cannot use a browser UI. Prefer WP-CLI, logs, and HTTP requests.

## Inputs required

- Environment and safety: dev/staging/prod, any restrictions (no writes, no plugin installs).
- How to target the install:
  - WP root `--path=<path>`
  - (multisite/site targeting) `--url=<url>`
- The performance symptom and scope:
  - which URL/REST route/admin screen
  - when it happens (always vs sporadic; logged-in vs logged-out)

## Procedure

### 0) Guardrails: measure first, avoid risky ops

1. Confirm whether you may run write operations (plugin installs, config changes, cache flush).
2. Pick a reproducible target (URL or REST route) and capture a baseline:
   - TTFB/time with `curl` if possible
   - WP-CLI profiling if available

Read:
- `references/measurement.md`

### 1) Generate a backend-only performance report (deterministic)

Run:

- `node skills/wp-performance/scripts/perf_inspect.mjs --path=<path> [--url=<url>]`

This detects:

- WP-CLI availability and core version
- whether `wp doctor` / `wp profile` are available
- autoloaded options size (if possible)
- object-cache drop-in presence

### 2) Fast wins: run diagnostics before deep profiling

If you have WP-CLI access, prefer:

- `wp doctor check`

It catches common production foot-guns (autoload bloat, SAVEQUERIES/WP_DEBUG, plugin counts, updates).

Read:
- `references/wp-cli-doctor.md`

### 3) Deep profiling (no browser required)

Preferred order:

1. `wp profile stage` to see where time goes (bootstrap/main_query/template).
2. `wp profile hook` (optionally with `--url=`) to find slow hooks/callbacks.
3. `wp profile eval` for targeted code paths.

Read:
- `references/wp-cli-profile.md`

### 4) Query Monitor (backend-only usage)

Query Monitor is normally UI-driven, but it can be used headlessly via REST API response headers and `_envelope` responses:

- Authenticate (nonce or Application Password).
- Request REST responses and inspect headers (`x-qm-*`) and/or the `qm` property when using `?_envelope`.

Read:
- `references/query-monitor-headless.md`

### 5) Fix by category (choose the dominant bottleneck)

Use the profile output to pick *one* primary bottleneck category:

- **DB queries** → reduce query count, fix N+1 patterns, improve indexes, avoid expensive meta queries.
  - `references/database.md`
- **Autoloaded options** → identify the biggest autoloaded options and stop autoloading large blobs.
  - `references/autoload-options.md`
- **Object cache misses** → introduce caching or fix cache key/group usage; add persistent object cache where appropriate.
  - `references/object-cache.md`
- **Remote HTTP calls** → add timeouts, caching, batching; avoid calling remote APIs on every request.
  - `references/http-api.md`
- **Cron** → reduce due-now spikes, de-duplicate events, move heavy tasks out of request paths.
  - `references/cron.md`

### 6) Verify (repeat the same measurement)

- Re-run the same `wp profile` / `wp doctor` / REST request.
- Confirm the performance delta and that behavior is unchanged.
- If the fix is risky, ship behind a feature flag or staged rollout when possible.

## WordPress 6.9 performance improvements

Be aware of these 6.9 changes when profiling:

**On-demand CSS for classic themes:**
- Classic themes now get on-demand CSS loading (previously only block themes had this).
- Reduces CSS payload by 30-65% by only loading styles for blocks actually used on the page.
- If you're profiling a classic theme, this should already be helping.

**Block themes with no render-blocking resources:**
- Block themes that don't define custom stylesheets (like Twenty Twenty-Three/Four) can now load with zero render-blocking CSS.
- Styles come from global styles (theme.json) and separate block styles, all inlined.
- This significantly improves LCP (Largest Contentful Paint).

**Inline CSS limit increased:**
- The threshold for inlining small stylesheets has been raised, reducing render-blocking resources.

Reference: https://make.wordpress.org/core/2025/11/18/wordpress-6-9-frontend-performance-field-guide/

## Verification

- Baseline vs after numbers are captured (same environment, same URL/route).
- `wp doctor check` is clean (or improved) when applicable.
- No new PHP errors or warnings in logs.
- No cache flush is required for correctness (cache flush should be last resort).

## Failure modes / debugging

- “No change” after code changes:
  - you measured a different URL/site (`--url` mismatch), caches masked results, or opcode cache is stale
- Profiling data is noisy:
  - eliminate background tasks, test with warmed caches, run multiple samples
- `SAVEQUERIES`/Query Monitor causes overhead:
  - don’t run in production unless explicitly approved

## Escalation

- If this is production and you don’t have explicit approval, do not:
  - install plugins, enable `SAVEQUERIES`, run load tests, or flush caches during traffic
- If you need system-level profiling (APM, PHP profiler extensions), coordinate with ops/hosting.
```

## File: `skills/wp-performance/references/autoload-options.md`
```markdown
# Autoloaded options

Autoloaded options are loaded on *every request*, so large autoload payloads can hurt performance site-wide.

## Quick checks

- Total autoload bytes:
  - `wp option list --autoload=on --format=total_bytes`
- Find biggest autoloaded options:
  - `wp option list --autoload=on --fields=option_name,size_bytes | sort -n -k 2 | tail`

Docs:

- `wp option list`: https://wpcli.dev/docs/option/list
- `wp doctor` includes an `autoload-options-size` check:
  - https://make.wordpress.org/cli/handbook/doctor-default-checks/

## Fix patterns

- Stop autoloading large blobs:
  - store large data in non-autoload options (autoload=off)
  - move large computed data to transients/object cache
- Remove stale options left behind by removed plugins/themes (careful: confirm usage before deleting).

```

## File: `skills/wp-performance/references/cron.md`
```markdown
# WP-Cron performance

Use this file when cron causes spikes or request-time slowness.

Backend-only tools:

- `wp cron test` (spawning health)
- `wp cron event list`
- `wp cron event run --due-now`

Reference:

- WP-CLI cron command package: https://github.com/wp-cli/cron-command

Fix patterns:

- De-duplicate scheduled events and reduce frequency where possible.
- Ensure tasks are idempotent and short.
- Move heavy work off-request; cron that runs on page load can hurt TTFB.

```

## File: `skills/wp-performance/references/database.md`
```markdown
# Database / query performance

Use this file when profiling points to DB time or high query counts.

Common fixes:

- Avoid N+1 query patterns (batch queries, prime caches, avoid per-row lookups).
- Prefer `fields => 'ids'` when you only need IDs.
- Avoid expensive meta queries where possible; consider indexing or schema changes.
- Use object caching for repeated reads.

Tools (backend-only):

- Query Monitor (REST headers/envelope) for query lists and stack traces.
- `wp db query` for targeted SQL/explain (be careful in prod).

References:

- Query Monitor plugin: https://wordpress.org/plugins/query-monitor/

```

## File: `skills/wp-performance/references/http-api.md`
```markdown
# HTTP API (remote requests)

Use this file when profiling shows slow external requests (`wp_remote_get`, etc.).

Fix patterns:

- Add timeouts and fail-fast behavior.
- Cache responses where appropriate (transients/object cache).
- Batch requests and avoid calling remote APIs on every page load.
- Move heavy remote work to async (cron/queue) where possible.

Tooling:

- Query Monitor can report HTTP API calls (including timing) via REST envelope info.

```

## File: `skills/wp-performance/references/measurement.md`
```markdown
# Measurement (profiling vs benchmarking)

Backend-only measurement options:

- **WP-CLI profiling** (`wp profile`): best for pinpointing slow hooks/stages without a browser.
- **WP-CLI doctor** (`wp doctor`): best for quick diagnostics (autoload bloat, debug constants, updates).
- **Query Monitor via REST**: use authenticated REST requests and inspect `x-qm-*` headers / `qm` envelope data.
- **Server-Timing** (Performance Lab): inspect `Server-Timing` headers via `curl -I` (when enabled).
- **APM/profilers**: New Relic, Datadog, Blackfire, Tideways, XHProf/Xdebug (requires server support).

Best practices:

- Always capture a baseline first.
- Keep the test scenario fixed (same URL/route, same user state, same data).
- Prefer multiple samples and medians over single runs.

References:

- Measuring performance handbook: https://make.wordpress.org/performance/handbook/measuring-performance/
- Benchmarking with Server-Timing: https://make.wordpress.org/performance/handbook/measuring-performance/benchmarking-server-timing/

```

## File: `skills/wp-performance/references/object-cache.md`
```markdown
# Object caching

Use this file when profiling indicates repeated queries or low cache hit rate.

## Concepts

- Default WP object cache is per-request memory only.
- A persistent object cache “drop-in” (`wp-content/object-cache.php`) can persist cache across requests.

WP-CLI cache commands:

- https://wpcli.dev/docs/cache

Guardrails:

- `wp cache flush` can impact all sites in multisite and cause load spikes:
  - https://wpcli.dev/docs/cache/flush

## Fix patterns

- Cache expensive computed results (transients or object cache) with explicit invalidation.
- Avoid unbounded caches (set expirations or implement invalidation hooks).
- If adding a persistent object cache, coordinate with infra (Redis/Memcached) and test cache flush behavior.

```

## File: `skills/wp-performance/references/query-monitor-headless.md`
```markdown
# Query Monitor (headless / backend-only)

Query Monitor is UI-first, but it can expose useful data to backend-only tooling.

## What it can show

Query Monitor can help debug:

- DB queries (slow/dupes/errors), hooks/actions, HTTP API calls, PHP errors

Plugin page:

- https://wordpress.org/plugins/query-monitor/

Configuration constants:

- https://querymonitor.com/help/configuration-constants/

## REST API requests (no browser needed)

Query Monitor can add performance/error info to authenticated REST responses.

Docs:

- https://querymonitor.com/wordpress-debugging/rest-api-requests/

High-level approach:

1. Authenticate (nonce or Application Password).
2. Make a REST request and inspect response headers like `x-qm-overview-*`.
3. If you request an enveloped response (`?_envelope`), you can get a `qm` property with:
   - DB queries details, cache stats, HTTP API request details, etc.

## Guardrails

- Query Monitor adds some overhead; don’t enable it in production without approval.
- If it’s already installed by your platform (e.g. VIP), you may need to grant `view_query_monitor`.

```

## File: `skills/wp-performance/references/server-timing.md`
```markdown
# Server-Timing (Performance Lab)

Use this file when you can enable Server-Timing metrics and want backend-only inspection via HTTP headers.

Performance Lab plugin:

- https://wordpress.org/plugins/performance-lab/

Benchmarking guidance:

- https://make.wordpress.org/performance/handbook/measuring-performance/benchmarking-server-timing/

Backend-only approach:

- Enable the relevant module/standalone plugin.
- Request a URL and inspect the `Server-Timing` header:
  - `curl -sS -D - https://example.test/ -o /dev/null | rg -i \"^server-timing:\"`

Guardrails:

- Don’t enable experimental modules in production without approval.

```

## File: `skills/wp-performance/references/wp-cli-doctor.md`
```markdown
# WP-CLI doctor (`wp doctor`)

Use this for quick “production readiness” checks.

## Install (if missing)

- `wp package install wp-cli/doctor-command`

Docs:

- Default checks: https://make.wordpress.org/cli/handbook/doctor-default-checks/
- Customize checks: https://make.wordpress.org/cli/handbook/guides/doctor/doctor-customize-config/

## Recommended usage

- `wp doctor check`
- `wp doctor list` (to see available checks)

Especially relevant to performance:

- `autoload-options-size` (autoloaded options threshold)
- `constant-savequeries-falsy` / `constant-wp-debug-falsy` (avoid perf-costly debug flags in prod)
- cron checks (count/duplicates)

```

## File: `skills/wp-performance/references/wp-cli-profile.md`
```markdown
# WP-CLI profiling (`wp profile`)

Use this when you need actionable profiling without a browser.

## Install (if missing)

`wp profile` comes from a WP-CLI package:

- `wp package install wp-cli/profile-command`

Docs:

- https://wpcli.dev/docs/profile/stage
- https://wpcli.dev/docs/profile/hook
- https://wpcli.dev/docs/profile/eval

## Recommended sequence

1. Stage overview:
   - `wp profile stage --fields=stage,time,cache_ratio [--url=<url>]`
2. Hooks hotspot:
   - `wp profile hook --spotlight [--url=<url>]`
   - then drill into a specific hook:
     - `wp profile hook init --spotlight [--url=<url>]`
3. Targeted evaluation:
   - `wp profile eval 'do_action(\"init\");' --hook=init`

Tips:

- Use `--url` to profile specific site/route behavior.
- Use `--skip-plugins` / `--skip-themes` to isolate culprit components (careful: behavior changes).

```

## File: `skills/wp-performance/scripts/perf_inspect.mjs`
```
import fs from "node:fs";
import path from "node:path";
import { spawnSync } from "node:child_process";

const TOOL_VERSION = "0.1.0";

function parseArgs(argv) {
  const args = { path: null, url: null, allowRoot: false };
  for (const a of argv) {
    if (a === "--allow-root") args.allowRoot = true;
    if (a.startsWith("--path=")) args.path = a.slice("--path=".length);
    if (a.startsWith("--url=")) args.url = a.slice("--url=".length);
  }
  return args;
}

function existsFile(p) {
  try {
    return fs.statSync(p).isFile();
  } catch {
    return false;
  }
}

function runWp(cmdArgs, { pathArg, urlArg, allowRoot }) {
  const args = [];
  if (allowRoot) args.push("--allow-root");
  if (pathArg) args.push(`--path=${pathArg}`);
  if (urlArg) args.push(`--url=${urlArg}`);
  args.push(...cmdArgs);

  const out = spawnSync("wp", args, { encoding: "utf8" });
  return {
    ok: out.status === 0,
    status: out.status,
    error: out.error ? { message: out.error.message, code: out.error.code } : null,
    stdout: (out.stdout || "").trim(),
    stderr: (out.stderr || "").trim(),
    args,
  };
}

function canRun(report, result, noteIfNotOk) {
  report._runs.push({ cmd: result.args.join(" "), ok: result.ok, status: result.status, error: result.error });
  if (!result.ok && noteIfNotOk) report.notes.push(noteIfNotOk);
  return result.ok;
}

function main() {
  const opts = parseArgs(process.argv.slice(2));
  const report = {
    tool: { name: "perf_inspect", version: TOOL_VERSION },
    target: { path: opts.path, url: opts.url },
    wpCli: { available: false },
    wp: {
      isInstalled: null,
      coreVersion: null,
    },
    commands: {
      doctor: { available: false },
      profile: { available: false },
    },
    perfSignals: {
      autoloadTotalBytes: null,
      hasObjectCacheDropin: null,
      hasAdvancedCacheDropin: null,
      hasQueryMonitorPlugin: null,
      hasPerformanceLabPlugin: null,
    },
    notes: [],
    _runs: [],
  };

  const info = runWp(["--info"], { pathArg: null, urlArg: null, allowRoot: opts.allowRoot });
  report.wpCli.available = info.ok;
  report.wpCli.info = info;
  if (!info.ok) {
    report.notes.push("WP-CLI not available on PATH. Run in the intended environment (container/ssh) or install WP-CLI.");
    process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
    return;
  }

  const isInstalled = runWp(["core", "is-installed"], { pathArg: opts.path, urlArg: opts.url, allowRoot: opts.allowRoot });
  report.wp.isInstalled = isInstalled.ok;
  canRun(report, isInstalled, "WordPress not detected at the given --path/--url (check wp-config.php and targeting).");
  if (!isInstalled.ok) {
    process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
    return;
  }

  const coreVersion = runWp(["core", "version"], { pathArg: opts.path, urlArg: opts.url, allowRoot: opts.allowRoot });
  report.wp.coreVersion = coreVersion.ok ? coreVersion.stdout : null;
  canRun(report, coreVersion);

  const doctorHelp = runWp(["doctor", "--help"], { pathArg: opts.path, urlArg: opts.url, allowRoot: opts.allowRoot });
  report.commands.doctor.available = doctorHelp.ok;
  canRun(report, doctorHelp);

  const profileHelp = runWp(["profile", "--help"], { pathArg: opts.path, urlArg: opts.url, allowRoot: opts.allowRoot });
  report.commands.profile.available = profileHelp.ok;
  canRun(report, profileHelp);

  const autoloadBytes = runWp(["option", "list", "--autoload=on", "--format=total_bytes"], {
    pathArg: opts.path,
    urlArg: opts.url,
    allowRoot: opts.allowRoot,
  });
  if (autoloadBytes.ok && /^\d+$/.test(autoloadBytes.stdout)) {
    report.perfSignals.autoloadTotalBytes = Number(autoloadBytes.stdout);
  }
  canRun(report, autoloadBytes);

  if (opts.path) {
    const wpContent = path.join(opts.path, "wp-content");
    report.perfSignals.hasObjectCacheDropin = existsFile(path.join(wpContent, "object-cache.php"));
    report.perfSignals.hasAdvancedCacheDropin = existsFile(path.join(wpContent, "advanced-cache.php"));
    report.perfSignals.hasQueryMonitorPlugin = existsFile(path.join(wpContent, "plugins", "query-monitor", "query-monitor.php"));
    report.perfSignals.hasPerformanceLabPlugin = existsFile(path.join(wpContent, "plugins", "performance-lab", "load.php"));
  }

  if (!report.commands.doctor.available) report.notes.push("Tip: install WP-CLI doctor: `wp package install wp-cli/doctor-command`.");
  if (!report.commands.profile.available) report.notes.push("Tip: install WP-CLI profile: `wp package install wp-cli/profile-command`.");

  process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
}

main();

```

## File: `skills/wp-phpstan/SKILL.md`
```markdown
---
name: wp-phpstan
description: "Use when configuring, running, or fixing PHPStan static analysis in WordPress projects (plugins/themes/sites): phpstan.neon setup, baselines, WordPress-specific typing, and handling third-party plugin classes."
compatibility: "Targets WordPress 6.9+ (PHP 7.2.24+). Requires Composer-based PHPStan."
---

# WP PHPStan

## When to use

Use this skill when working on PHPStan in a WordPress codebase, for example:

- setting up or updating `phpstan.neon` / `phpstan.neon.dist`
- generating or updating `phpstan-baseline.neon`
- fixing PHPStan errors via WordPress-friendly PHPDoc (REST requests, hooks, query results)
- handling third-party plugin/theme classes safely (stubs/autoload/targeted ignores)

## Inputs required

- `wp-project-triage` output (run first if you haven't)
- Whether adding/updating Composer dev dependencies is allowed (stubs).
- Whether changing the baseline is allowed for this task.

## Procedure

### 0) Discover PHPStan entrypoints (deterministic)
1. Inspect PHPStan setup (config, baseline, scripts):
   - `node skills/wp-phpstan/scripts/phpstan_inspect.mjs`

Prefer the repo’s existing `composer` script (e.g. `composer run phpstan`) when present.

### 1) Ensure WordPress core stubs are loaded

`szepeviktor/phpstan-wordpress` or `php-stubs/wordpress-stubs` are effectively required for most WordPress plugin/theme repos. Without it, expect a high volume of errors about unknown WordPress core functions.

- Confirm the package is installed (see `composer.dependencies` in the inspect report).
- Ensure the PHPStan config references the stubs (see `references/third-party-classes.md`).

### 2) Ensure a sane `phpstan.neon` for WordPress projects

- Keep `paths` focused on first-party code (plugin/theme directories).
- Exclude generated and vendored code (`vendor/`, `node_modules/`, build artifacts, tests unless explicitly analyzed).
- Keep `ignoreErrors` entries narrow and documented.

See:
- `references/configuration.md`

### 3) Fix errors with WordPress-specific typing (preferred)

Prefer correcting types over ignoring errors. Common WP patterns that need help:

- REST endpoints: type request parameters using `WP_REST_Request<...>`
- Hook callbacks: add accurate `@param` types for callback args
- Database results and iterables: use array shapes or object shapes for query results
- Action Scheduler: type `$args` array shapes for job callbacks

See:
- `references/wordpress-annotations.md`

### 4) Handle third-party plugin/theme classes (only when needed)

When integrating with plugins/themes not present in the analysis environment:

- First, confirm the dependency is real (installed/required).
- Prefer plugin-specific stubs already used in the repo (common examples: `php-stubs/woocommerce-stubs`, `php-stubs/acf-pro-stubs`).
- If PHPStan still cannot resolve classes, add targeted `ignoreErrors` patterns for the specific vendor prefix.

See:
- `references/third-party-classes.md`

### 5) Baseline management (use as a migration tool, not a trash bin)

- Generate a baseline once for legacy code, then reduce it over time.
- Do not “baseline” newly introduced errors.

See:
- `references/configuration.md`

## Verification

- Run PHPStan using the discovered command (`composer run ...` or `vendor/bin/phpstan analyse`).
- Confirm the baseline file (if used) is included and didn’t grow unexpectedly.
- Re-run after changing `ignoreErrors` to ensure patterns are not masking unrelated issues.

## Failure modes / debugging

- “Class not found”:
  - confirm autoloading/stubs, or add a narrow ignore pattern
- Huge error counts after enabling PHPStan:
  - reduce `paths`, add `excludePaths`, start at a lower level, then ratchet up
- Inconsistent types around hooks / REST params:
  - add explicit PHPDoc (see references) rather than runtime guards

## Escalation

- If a type depends on a third-party plugin API you can’t confirm, ask for the dependency version or source before inventing types.
- If fixing requires adding new Composer dependencies (stubs/extensions), confirm it with the user first.
```

## File: `skills/wp-phpstan/references/configuration.md`
```markdown
# PHPStan configuration (WordPress)

This reference documents a minimal, WordPress-friendly PHPStan setup and baseline workflow.

## Minimal `phpstan.neon` template

Use the repo’s existing layout. The example below is intentionally conservative and should be adapted to the project’s actual directories.

```neon
# Include the baseline only if the file exists.
includes:
    - phpstan-baseline.neon

parameters:
    level: 5
    paths:
        - src/
        - includes/

    excludePaths:
        - vendor/
        - vendor-prefixed/
        - node_modules/
        - tests/

    ignoreErrors:
        # Add targeted exceptions only when necessary.
```

Guidelines:

- Prefer analyzing first-party code only.
- Exclude anything generated or vendored.
- Keep `ignoreErrors` patterns narrow and grouped by dependency.

## Baseline workflow

Baselines help you adopt PHPStan in legacy code without accepting new regressions.

```bash
# Generate a baseline (explicit filename)
vendor/bin/phpstan analyse --generate-baseline phpstan-baseline.neon

# Update an existing baseline (defaults)
vendor/bin/phpstan analyse --generate-baseline
```

Best practices:

- Avoid adding new errors to the baseline; fix the new code instead.
- Treat baseline changes like code changes: review in PRs.
- Chip away at the baseline gradually (remove entries as you fix root causes).
```

## File: `skills/wp-phpstan/references/third-party-classes.md`
```markdown
# Third-party classes and ignore patterns

When PHPStan reports legitimate classes as missing (e.g. because WordPress or a plugin is not installed in the analysis environment), prefer fixing discovery first and only then add targeted ignores.

## Before adding `ignoreErrors`

- Confirm the dependency is real (installed/required in this environment).
- Prefer stubs/extensions already used by the repo.
- Prefer a narrow ignore for the vendor prefix over a broad ignore.

## Recommended stub packages

Stubs are useful when the analysis environment does not include WordPress (or a plugin API) but you still want real type checking (instead of blanket ignores).

Common packages:

```bash
composer require --dev szepeviktor/phpstan-wordpress
composer require --dev php-stubs/wordpress-stubs
composer require --dev php-stubs/woocommerce-stubs
composer require --dev php-stubs/acf-pro-stubs
```

When stubs are useful (and sometimes necessary):

- Running PHPStan in a plugin/theme repo without a full WordPress checkout.
- PHPStan reports unknown WordPress core functions (e.g. `add_action()`, `get_option()`).
- Integrations with optional plugins (WooCommerce, ACF Pro) that are not installed during analysis.
- You want method/property existence checks and accurate return types instead of `ignoreErrors`.

Notes:

- Prefer stubs that match the runtime versions; mismatches can cause false positives.
- Adding Composer dependencies changes the repo; confirm it is acceptable for the task.

## Ensure stubs are loaded

Installing stubs is not enough if PHPStan does not scan them. Add stub paths in `phpstan.neon`.

```neon
parameters:
    bootstrapFiles:
        - %rootDir%/../../php-stubs/woocommerce-stubs/woocommerce-stubs.php
    scanFiles:
        - %rootDir%/../../php-stubs/wordpress-stubs/wordpress-stubs.php
        - %rootDir%/../../php-stubs/acf-pro-stubs/acf-pro-stubs.php
        - %rootDir%/../../woocommerce/action-scheduler/functions.php
```

## Targeted ignore patterns (examples)

```neon
parameters:
    ignoreErrors:
        # Admin Columns Pro
        - '#.*(unknown class|invalid type|call to method .* on an unknown class) AC\\ListScreen.*#'

        # Elementor
        - '#.*(unknown class|invalid type|call to method .* on an unknown class) Elementor\\.*#'

        # Yoast SEO
        - '#.*(unknown class|invalid type|call to method .* on an unknown class) WPSEO_.*#'
```

Pattern creation rules:

- Cover error variations: `unknown class`, `invalid type`, `call to method .* on an unknown class`.
- Keep patterns specific enough to target only intended classes.
- Add a short comment naming the plugin/theme.
- Group related patterns for the same dependency.

When to add exceptions:

- Only for legitimate third-party dependencies your code integrates with.
- Document each pattern with a comment.
- Re-run PHPStan to ensure the ignore does not hide unrelated issues.
```

## File: `skills/wp-phpstan/references/wordpress-annotations.md`
```markdown
# WordPress-specific type annotations

These patterns help PHPStan understand WordPress code where runtime behavior and dynamic typing make inference difficult.

## REST API request typing

PHPStan cannot infer valid request parameters from REST API schemas. Provide explicit type hints for request params.

```php
/**
 * Handle REST API request.
 *
 * @param WP_REST_Request $request Full details about the request.
 * @return WP_REST_Response|WP_Error Response object on success, error on failure.
 *
 * @phpstan-param WP_REST_Request<array{
 *     post?: int,
 *     orderby?: string,
 *     meta_key?: string,
 *     per_page?: int,
 *     status?: array<string>
 * }> $request
 */
public function get_items( $request ) {
    $post_id = $request->get_param( 'post' );
    // PHPStan now knows $post_id is int|null.
}
```

For complex schemas, define reusable types.

```php
/**
 * @phpstan-type PostRequestParams array{
 *     title?: string,
 *     content?: string,
 *     status?: 'publish'|'draft'|'private',
 *     meta?: array<string, mixed>
 * }
 *
 * @phpstan-param WP_REST_Request<PostRequestParams> $request
 */
```

## Hook callbacks

```php
/**
 * Handle status transitions.
 *
 * @param string $new_status
 * @param string $old_status
 * @param WP_Post $post
 */
function handle_transition( string $new_status, string $old_status, WP_Post $post ): void {
    // ...
}

add_action( 'transition_post_status', 'handle_transition', 10, 3 );
```

## Database and iterables

```php
/**
 * @return array<WP_Post> WP_Post objects.
 */
function get_custom_posts(): array {
    $posts = get_posts( [ 'post_type' => 'custom_type', 'numberposts' => -1 ] );
    return $posts;
}

/**
 * @return array<object{id: int, name: string}> Database results.
 */
function get_user_data(): array {
    global $wpdb;

    $results = $wpdb->get_results( "SELECT id, name FROM users", OBJECT );
    return $results ?: [];
}
```

## Hooks (`apply_filters()` and `do_action()`)

Docblocks for `apply_filters()` and `do_action()` are validated. The type of the first `@param` is definitive.

If a third party returns the wrong type for a filter, a PHPStan error is expected and does not require defensive code.

```php
/**
 * Allows hooking into formatting of the price.
 *
 * @param string $formatted The formatted price.
 * @param float  $price     The raw price.
 * @param string $locale    Locale to localize pricing display.
 * @param string $currency  Currency symbol.
 */
return apply_filters( 'autoscout_vehicle_price_formatted', $formatted, $price, $locale, $currency );
```

## Action Scheduler argument shapes

```php
/**
 * Process a scheduled email.
 *
 * @param array{user_id: int, email: string, data: array<string, mixed>} $args
 */
function process_scheduled_email( array $args ): void {
    $user_id = $args['user_id'];
    // ...
}

as_schedule_single_action(
    time() + 3600,
    'process_scheduled_email',
    [
        'user_id' => 123,
        'email' => 'user@example.com',
        'data' => [ 'key' => 'value' ],
    ]
);
```
```

## File: `skills/wp-phpstan/scripts/phpstan_inspect.mjs`
```
import fs from "node:fs";
import path from "node:path";

const TOOL_VERSION = "0.1.0";

/**
 * Reads and parses JSON from a file path.
 *
 * Returns null when parsing fails so the caller can provide user-facing
 * guidance without crashing.
 *
 * @param {string} filePath Absolute path to a JSON file.
 * @returns {any|null} Parsed JSON object.
 */
function readJsonSafe(filePath) {
  try {
    return JSON.parse(fs.readFileSync(filePath, "utf8"));
  } catch {
    return null;
  }
}

/**
 * Reads a UTF-8 text file.
 *
 * Returns null when reading fails so callers can surface missing configs
 * without crashing.
 *
 * @param {string} filePath Absolute path to a text file.
 * @returns {string|null} File contents.
 */
function readTextSafe(filePath) {
  try {
    return fs.readFileSync(filePath, "utf8");
  } catch {
    return null;
  }
}

/**
 * Checks whether a path exists and is a regular file.
 *
 * @param {string} filePath Absolute or relative file path.
 * @returns {boolean} True when the path exists and is a file.
 */
function isFile(filePath) {
  try {
    return fs.statSync(filePath).isFile();
  } catch {
    return false;
  }
}

/**
 * Normalizes Composer script entries into a flat list of commands.
 *
 * Composer allows scripts to be strings or arrays. This helper provides a
 * consistent format for analysis.
 *
 * @param {unknown} value Composer script value.
 * @returns {string[]} Command list.
 */
function normalizeComposerScript(value) {
  if (typeof value === "string") return [value];
  if (Array.isArray(value)) return value.filter((x) => typeof x === "string");
  return [];
}

/**
 * Detects which Composer scripts invoke PHPStan.
 *
 * This helps the agent prefer the repo's own invocation (memory limits,
 * config, bootstrap files) instead of guessing.
 *
 * @param {Record<string, unknown>} scripts Composer scripts block.
 * @returns {Array<{name: string, commands: string[]}>} Matching script entries.
 */
function findPhpstanScripts(scripts) {
  if (!scripts || typeof scripts !== "object") return [];

  const matches = [];

  for (const [name, raw] of Object.entries(scripts)) {
    const commands = normalizeComposerScript(raw);

    const invokesPhpstan = commands.some((cmd) => {
      if (typeof cmd !== "string") return false;
      return cmd.includes("phpstan") || cmd.includes("vendor/bin/phpstan");
    });

    if (!invokesPhpstan) continue;

    matches.push({ name, commands });
  }

  return matches;
}

/**
 * Chooses a recommended command for running PHPStan in the current repo.
 *
 * The intent is to prefer an existing Composer script (often has correct
 * config, bootstrap, and memory limits), falling back to vendor binaries.
 *
 * @param {Array<{name: string, commands: string[]}>} phpstanScripts Matching Composer scripts.
 * @param {{binaryRelPath: string|null, configRelPath: string|null}} fallbackInfo Fallback discovery.
 * @returns {{command: string|null, rationale: string}} Suggested command and why.
 */
function suggestCommand(phpstanScripts, fallbackInfo) {
  const preferred = phpstanScripts.find((s) => s.name === "phpstan");
  if (preferred) {
    return {
      command: `composer run ${preferred.name}`,
      rationale: "Uses the repo's Composer script (preferred for consistent config).",
    };
  }

  if (phpstanScripts.length > 0) {
    return {
      command: `composer run ${phpstanScripts[0].name}`,
      rationale: "Uses the repo's Composer script that invokes PHPStan.",
    };
  }

  if (!fallbackInfo.binaryRelPath) {
    return {
      command: null,
      rationale: "No PHPStan binary detected under vendor/bin and no Composer script found.",
    };
  }

  const configArg = fallbackInfo.configRelPath ? ` -c ${fallbackInfo.configRelPath}` : "";

  return {
    command: `${fallbackInfo.binaryRelPath} analyse${configArg}`,
    rationale: "Falls back to vendor/bin/phpstan with an explicit config when needed.",
  };
}

/**
 * Extracts lightweight hints from a phpstan.neon config.
 *
 * This does not parse NEON. It only checks for common directive tokens so the
 * agent can quickly see whether scan directives are in use.
 *
 * @param {string} configText Raw phpstan config contents.
 * @returns {{mentionsScanDirectories: boolean, mentionsScanFiles: boolean}} Hints.
 */
function buildConfigHints(configText) {
  const t = configText.toLowerCase();

  return {
    mentionsScanDirectories: t.includes("scandirectories"),
    mentionsScanFiles: t.includes("scanfiles"),
  };
}

/**
 * Extracts stub-like package references from a PHPStan config.
 *
 * The PHPStan config usually references stubs via vendor paths (for example,
 * "vendor/php-stubs/wordpress-stubs"), so this helper focuses on composer-style
 * "vendor/package" tokens containing "stubs".
 *
 * @param {string} configText Raw phpstan config contents.
 * @returns {string[]} Unique, lowercased composer-style package references.
 */
function extractStubPackageReferences(configText) {
  const matches = configText
    .toLowerCase()
    .match(/\b[a-z0-9_.-]+\/[a-z0-9_.-]*stubs[a-z0-9_.-]*\b/g);

  if (!matches) return [];

  return [...new Set(matches)].sort();
}

/**
 * Builds a JSON report describing the current repository's PHPStan setup.
 *
 * @returns {object} A stable, machine-readable inspection report.
 */
function buildReport() {
  const repoRoot = process.cwd();

  const composerPath = path.join(repoRoot, "composer.json");
  const composer = isFile(composerPath) ? readJsonSafe(composerPath) : null;

  const phpstanConfigFiles = ["phpstan.neon", "phpstan.neon.dist"].filter((f) =>
    isFile(path.join(repoRoot, f))
  );
  const phpstanBaselineFiles = ["phpstan-baseline.neon", "phpstan-baseline.neon.dist"].filter((f) =>
    isFile(path.join(repoRoot, f))
  );

  let configRelPath = null;
  if (phpstanConfigFiles.includes("phpstan.neon")) configRelPath = "phpstan.neon";
  else if (phpstanConfigFiles.includes("phpstan.neon.dist")) configRelPath = "phpstan.neon.dist";

  const configAbsPath = configRelPath ? path.join(repoRoot, configRelPath) : null;
  const configText = configAbsPath ? readTextSafe(configAbsPath) : null;

  const binaryRelPath = isFile(path.join(repoRoot, "vendor", "bin", "phpstan")) ? "vendor/bin/phpstan" : null;

  const composerScripts = composer?.scripts && typeof composer.scripts === "object" ? composer.scripts : null;
  const phpstanScripts = composerScripts ? findPhpstanScripts(composerScripts) : [];

  const composerDependencies = [
    ...Object.keys(composer?.require ?? {}),
    ...Object.keys(composer?.["require-dev"] ?? {}),
  ].sort();
  const referencedDependencies = configText ? extractStubPackageReferences(configText) : [];

  const configHints = configText ? buildConfigHints(configText) : null;

  const suggested = suggestCommand(phpstanScripts, {
    binaryRelPath,
    configRelPath: configRelPath === "phpstan.neon" ? null : configRelPath,
  });

  const notes = [];

  if (!composer) notes.push("No composer.json found; PHPStan is usually installed via Composer.");
  if (phpstanConfigFiles.length === 0) notes.push("No phpstan.neon or phpstan.neon.dist found at repo root.");
  if (!binaryRelPath && phpstanScripts.length === 0) notes.push("No PHPStan entrypoint detected (Composer script or vendor/bin/phpstan).");



  return {
    tool: { name: "phpstan_inspect", version: TOOL_VERSION },
    repoRoot,
    composer: {
      exists: Boolean(composer),
      path: isFile(composerPath) ? "composer.json" : null,
      phpstanScripts,
      dependencies: composerDependencies,
    },
    phpstan: {
      configFiles: phpstanConfigFiles,
      baselineFiles: phpstanBaselineFiles,
      config: {
        primary: configRelPath,
        hints: configHints,
        referencedDependencies,
      },
      binary: {
        vendorBin: binaryRelPath,
      },
    },
    suggested,
    notes,
  };
}

/**
 * CLI entrypoint for printing the inspection report.
 */
function main() {
  const report = buildReport();
  process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
}

main();
```

## File: `skills/wp-playground/SKILL.md`
```markdown
---
name: wp-playground
description: "Use for WordPress Playground workflows: fast disposable WP instances in the browser or locally via @wp-playground/cli (server, run-blueprint, build-snapshot), auto-mounting plugins/themes, switching WP/PHP versions, blueprints, and debugging (Xdebug)."
compatibility: "Targets WordPress 6.9+ (PHP 7.2.24+). Playground CLI requires Node.js 20.18+; runs WP in WebAssembly with SQLite."
---

# WordPress Playground

## When to use

- Spin up a disposable WordPress to test a plugin/theme without full stack setup.
- Run or iterate on Playground Blueprints (JSON) locally.
- Build a reproducible snapshot of a site for sharing or CI.
- Switch WP/PHP versions quickly to reproduce issues.
- Debug plugin/theme code with Xdebug in an isolated Playground.

## Inputs required

- Host machine readiness: Node.js ≥ 20.18, `npm`/`npx` available.
- Project path to mount (`--auto-mount` or explicit mount mapping).
- Desired WP version/PHP version (optional; defaults to latest WP, PHP 8.3).
- Blueprint location/URL if running a blueprint.
- Port preference if 9400 conflicts.
- Whether Xdebug is needed.

## Procedure

### 0) Guardrails

- Playground instances are ephemeral and SQLite-backed; **never** point at production data.
- Confirm Node ≥ 20.18 (`node -v`) before running CLI.
- If mounting local code, ensure it is clean of secrets; Playground copies files into an in-memory FS.

### 1) Quick local spin-up (auto-mount)

```bash
cd <plugin-or-theme-root>
npx @wp-playground/cli@latest server --auto-mount
```
- Opens on http://localhost:9400 by default. Auto-detects plugin/theme and installs it.
- Add `--wp=<version>` / `--php=<version>` as needed.
- For classic full installs already present, add `--skip-wordpress-setup` and mount the whole tree.

### 2) Manual mounts or multiple mounts

- Use `--mount=/host/path:/vfs/path` (repeatable) when auto-mount is insufficient (multi-plugin, mu-plugins, custom content).
- Mount before install with `--mount-before-install` for bootstrapping installer flows.
- Reference: `references/cli-commands.md`

### 3) Run a Blueprint (no server needed)

```bash
npx @wp-playground/cli@latest run-blueprint --blueprint=<file-or-url>
```
- Use for scripted setup/CI validation. Supports remote URLs and local files.
- Allow bundled assets in local blueprints with `--blueprint-may-read-adjacent-files` when required.
- See `references/blueprints.md` for structure and common flags.

### 4) Build a snapshot for sharing

```bash
npx @wp-playground/cli@latest build-snapshot --blueprint=<file> --outfile=./site.zip
```
- Produces a ZIP you can load in Playground or attach to bug reports.

### 5) Debugging with Xdebug

- Start with `--xdebug` (or `--enable-xdebug` depending on CLI release) to expose an IDE key, then connect VS Code/PhpStorm to the host/port shown in CLI output.
- Combine with `--auto-mount` for plugin/theme debugging.
- Checklist: `references/debugging.md`

### 6) Version switching

- Use `--wp=` to pin WP (e.g., 6.9.0) and `--php=` to test compatibility.
- If feature depends on Gutenberg trunk, prefer the latest WP release plus plugin if available; Playground images track stable WP plus bundled Gutenberg.

### 7) Browser-only workflows (no CLI)

- Launch quick previews with URL fragments or query params:
  - Fragment: `https://playground.wordpress.net/#<base64-or-json-blueprint>`
  - Query: `https://playground.wordpress.net/?blueprint-url=<public-url-or-zip>`
- Use the live Blueprint Editor (playground.wordpress.net) to author blueprints with schema help; paste JSON and copy a shareable link.

## Verification

- Verify mounted code is active (plugin listed/active; theme selected).
- For blueprints/snapshots, re-run with `--verbosity=debug` to confirm steps executed.
- Run targeted smoke (e.g., `wp plugin list` inside Playground shell via browser terminal if exposed) or UI click-path.

## Failure modes / debugging

- **CLI exits complaining about Node**: upgrade to ≥ 20.18.
- **Mount not applied**: check path, use absolute path, add `--verbosity=debug`.
- **Blueprint cannot read local assets**: add `--blueprint-may-read-adjacent-files`.
- **Port already used**: `--port=<free-port>`.
- **Slow/locked UI**: disable `--experimental-multi-worker` if enabled; or enable it to improve throughput on CPU-bound runs.

## Escalation

- If PHP extensions or native DB access are required, Playground may be unsuitable; fall back to full WP stack or wp-env/Docker.
- For browser-only embedding or VS Code extension specifics, consult the upstream docs: https://wordpress.github.io/wordpress-playground/
```

## File: `skills/wp-playground/references/blueprints.md`
```markdown
## Blueprint quick reference

Blueprints are JSON recipes that describe how Playground should set up WordPress.

### Minimal example

```json
{
  "$schema": "https://playground.wordpress.net/blueprint-schema.json",
  "steps": [
    { "step": "installTheme", "themeZipUrl": "https://downloads.wordpress.org/theme/twentytwentythree.zip" },
    { "step": "installPlugin", "pluginZipUrl": "https://downloads.wordpress.org/plugin/classic-editor.zip" }
  ]
}
```

### Common steps (non-exhaustive)

- `setSiteUrl`, `setHomeUrl`
- `installTheme`, `installPlugin` (ZIP URLs or local paths when allowed)
- `activateTheme`, `activatePlugin`
- `runPHP` (inline PHP)
- `applyPatches` (filesystem patch)
- `writeFile` (create/update files)
- `importFile` (XML/WXR)
- `wpConfigConstants` (define constants)
- `preferredVersions` (pick WP/PHP; matches CLI `--wp` / `--php`)
- `blueprintSteps` that include `extraLibraries` (e.g., Jetpack) and `features.networking` when browser networking is required

### Tips

- Use `--blueprint-may-read-adjacent-files` when the blueprint needs local files (e.g., custom plugin ZIP) during `run-blueprint` or `build-snapshot`.
- For iterative authoring, keep blueprints small and compose via separate files.
- Validate against the published schema URL above to catch typos.
- For Gutenberg/nightly testing, set `--wp=<version>` to align with target WP.
- To share quickly, encode the blueprint as base64 in the Playground URL fragment or host the JSON/ZIP and pass `?blueprint-url=…`.
```

## File: `skills/wp-playground/references/cli-commands.md`
```markdown
## Playground CLI command cheatsheet

> Requires Node.js 20.18+ and npm/npx.
> Latest version: 3.0.20 (November 2025)

### What's new in 2025

- **PHP 8.3 is now the default** (since July 2025).
- **New PHP extensions**: ImageMagick, SOAP, and AVIF GD support.
- **OpCache enabled**: 42% faster response times (185ms → 108ms average).
- **Multi-worker default**: `--experimental-multi-worker` now defaults to CPU count minus one.

### Install / run server

- `npx @wp-playground/cli@latest server [--port=9400] [--auto-mount] [--wp=<ver>] [--php=<ver>] [--verbosity=debug] [--blueprint=<url-or-path>]`
- Mounts:
  - `--auto-mount` (detect plugin/theme in CWD)
  - `--mount=/abs/host:/vfs/path` (repeatable)
  - `--mount-before-install` (apply mounts before WP install)

### Run a blueprint

- `npx @wp-playground/cli@latest run-blueprint --blueprint=<file-or-url> [--blueprint-may-read-adjacent-files] [--wp=<ver>] [--php=<ver>] [--verbosity=debug]`
- Use for scripted setup; no persistent server.

### Build a snapshot

- `npx @wp-playground/cli@latest build-snapshot --blueprint=<file-or-url> --outfile=./site.zip [--verbosity=debug]`
- Produces a sharable ZIP usable by Playground UI or other CLI commands.

### Debugging flags

- `--xdebug` / `--enable-xdebug` (depends on release) to start Xdebug listener.
- `--experimental-multi-worker` to speed multi-step blueprints; disable if unstable.

### Version control

- `--wp=<version>` to pick WordPress version (defaults to latest).
- `--php=<version>` to pick PHP version (defaults to 8.3 since July 2025).
```

## File: `skills/wp-playground/references/debugging.md`
```markdown
## Debugging WordPress Playground

- Start CLI with Xdebug: `server --auto-mount --xdebug` (or `--enable-xdebug` depending on release). The CLI prints host/port and IDE key to configure your debugger.
- If breakpoints are not hit, confirm:
  - IDE listens on the port shown by CLI.
  - Path mappings include the mounted VFS path used by Playground.
- For slow or stuck runs:
  - Add `--verbosity=debug` to see step-level logs.
  - Disable `--experimental-multi-worker` if it was enabled.
- For mount issues:
  - Prefer absolute paths in `--mount`.
  - Use `--mount-before-install` when installer steps need files present early.
- To inspect runtime state:
  - Open the Playground browser console; the Service Worker logs network/FS events.
  - Use the “Terminal” tab (if available) to run WP-CLI inside the instance.

```

## File: `skills/wp-plugin-development/SKILL.md`
```markdown
---
name: wp-plugin-development
description: "Use when developing WordPress plugins: architecture and hooks, activation/deactivation/uninstall, admin UI and Settings API, data storage, cron/tasks, security (nonces/capabilities/sanitization/escaping), and release packaging."
compatibility: "Targets WordPress 6.9+ (PHP 7.2.24+). Filesystem-based agent with bash + node. Some workflows require WP-CLI."
---

# WP Plugin Development

## When to use

Use this skill for plugin work such as:

- creating or refactoring plugin structure (bootstrap, includes, namespaces/classes)
- adding hooks/actions/filters
- activation/deactivation/uninstall behavior and migrations
- adding settings pages / options / admin UI (Settings API)
- security fixes (nonces, capabilities, sanitization/escaping, SQL safety)
- packaging a release (build artifacts, readme, assets)

## Inputs required

- Repo root + target plugin(s) (path to plugin main file if known).
- Where this plugin runs: single site vs multisite; WP.com conventions if applicable.
- Target WordPress + PHP versions (affects available APIs and placeholder support in `$wpdb->prepare()`).

## Procedure

### 0) Triage and locate plugin entrypoints

1. Run triage:
   - `node skills/wp-project-triage/scripts/detect_wp_project.mjs`
2. Detect plugin headers (deterministic scan):
   - `node skills/wp-plugin-development/scripts/detect_plugins.mjs`

If this is a full site repo, pick the specific plugin under `wp-content/plugins/` or `mu-plugins/` before changing code.

### 1) Follow a predictable architecture

Guidelines:

- Keep a single bootstrap (main plugin file with header).
- Avoid heavy side effects at file load time; load on hooks.
- Prefer a dedicated loader/class to register hooks.
- Keep admin-only code behind `is_admin()` (or admin hooks) to reduce frontend overhead.

See:
- `references/structure.md`

### 2) Hooks and lifecycle (activation/deactivation/uninstall)

Activation hooks are fragile; follow guardrails:

- register activation/deactivation hooks at top-level, not inside other hooks
- flush rewrite rules only when needed and only after registering CPTs/rules
- uninstall should be explicit and safe (`uninstall.php` or `register_uninstall_hook`)

See:
- `references/lifecycle.md`

### 3) Settings and admin UI (Settings API)

Prefer Settings API for options:

- `register_setting()`, `add_settings_section()`, `add_settings_field()`
- sanitize via `sanitize_callback`

See:
- `references/settings-api.md`

### 4) Security baseline (always)

Before shipping:

- Validate/sanitize input early; escape output late.
- Use nonces to prevent CSRF *and* capability checks for authorization.
- Avoid directly trusting `$_POST` / `$_GET`; use `wp_unslash()` and specific keys.
- Use `$wpdb->prepare()` for SQL; avoid building SQL with string concatenation.

See:
- `references/security.md`

### 5) Data storage, cron, migrations (if needed)

- Prefer options for small config; custom tables only if necessary.
- For cron tasks, ensure idempotency and provide manual run paths (WP-CLI or admin).
- For schema changes, write upgrade routines and store schema version.

See:
- `references/data-and-cron.md`

## Verification

- Plugin activates with no fatals/notices.
- Settings save and read correctly (capability + nonce enforced).
- Uninstall removes intended data (and nothing else).
- Run repo lint/tests (PHPUnit/PHPCS if present) and any JS build steps if the plugin ships assets.

## Failure modes / debugging

- Activation hook not firing:
  - hook registered incorrectly (not in main file scope), wrong main file path, or plugin is network-activated
- Settings not saving:
  - settings not registered, wrong option group, missing capability, nonce failure
- Security regressions:
  - nonce present but missing capability checks; or sanitized input not escaped on output

See:
- `references/debugging.md`

## Escalation

For canonical detail, consult the Plugin Handbook and security guidelines before inventing patterns.
```

## File: `skills/wp-plugin-development/references/data-and-cron.md`
```markdown
# Data storage, cron, and upgrades

Use this file when adding persistent storage, background jobs, or upgrade routines.

## Data storage

- Prefer Options API for small config/state.
- Use custom tables only when needed; store schema version and provide upgrade paths.

## Cron

- Ensure tasks are idempotent (may run late or multiple times).
- Provide a manual trigger path for debugging (WP-CLI or admin-only action).

## Database safety note

If using `$wpdb->prepare()`, avoid building queries with concatenated user input.
Recent WordPress versions support identifier placeholders (`%i`) but you must not assume it exists without checking capabilities or target versions.

```

## File: `skills/wp-plugin-development/references/debugging.md`
```markdown
# Debugging quick routes

## Plugin doesn’t load / fatal errors

- Confirm correct plugin main file and header.
- Check PHP error logs and `WP_DEBUG_LOG`.
- If the repo is a site repo, confirm you edited the correct plugin under `wp-content/plugins/`.

## Activation hook surprises

- Hooks must be registered at top-level.
- Activation runs in a special context; avoid assuming other hooks already ran.

## Settings not saving

- Confirm `register_setting()` is called.
- Confirm the option group matches the form.
- Confirm capability checks and nonces.

```

## File: `skills/wp-plugin-development/references/lifecycle.md`
```markdown
# Activation, deactivation, uninstall

Use this file for lifecycle changes and data cleanup.

## Activation / deactivation hooks

- `register_activation_hook( __FILE__, 'callback' )`
- `register_deactivation_hook( __FILE__, 'callback' )`

Guardrails:

- These hooks must be registered at top-level (not inside other hooks).
- If you flush rewrite rules, ensure rules are registered first (often via a shared function called both on `init` and activation).

Upstream reference:

- https://developer.wordpress.org/plugins/plugin-basics/activation-deactivation-hooks/

## Uninstall

Preferred approaches:

- `uninstall.php` (runs only on uninstall)
- `register_uninstall_hook()`

Guardrails:

- Check `WP_UNINSTALL_PLUGIN` before running destructive cleanup.

Upstream reference:

- https://developer.wordpress.org/plugins/plugin-basics/uninstall-methods/

```

## File: `skills/wp-plugin-development/references/security.md`
```markdown
# Security guardrails (plugin work)

Use this file when making security fixes or when handling any input/output.

## Nonces + permissions

- Nonces help prevent CSRF, not authorization.
- Always pair nonces with capability checks (`current_user_can()` or a more specific capability).

Upstream reference:

- https://developer.wordpress.org/apis/security/nonces/

## Sanitization and escaping

Golden rule:

- sanitize/validate on input, escape on output.

Practical rules:

- never process the entire `$_POST` / `$_GET` array; read explicit keys
- use `wp_unslash()` before sanitizing when needed
- use prepared statements for SQL; avoid interpolating user input into queries

Common review guidance:

- https://developer.wordpress.org/plugins/wordpress-org/detailed-plugin-guidelines/

```

## File: `skills/wp-plugin-development/references/settings-api.md`
```markdown
# Settings API (admin options)

Use this file when adding settings pages or storing user-configurable options.

Core APIs:

- `register_setting()`
- `add_settings_section()`
- `add_settings_field()`

Upstream references:

- Settings API overview: https://developer.wordpress.org/plugins/settings/settings-api/
- Register settings: https://developer.wordpress.org/plugins/settings/registration/
- Add settings fields: https://developer.wordpress.org/plugins/settings/settings-fields/

Practical guardrails:

- Use `sanitize_callback` to validate/sanitize data.
- Use capability checks (commonly `manage_options`) for settings screens and saves.
- Escape values on output (`esc_attr`, `esc_html`, etc.).

```

## File: `skills/wp-plugin-development/references/structure.md`
```markdown
# Plugin structure and loading

Use this file when introducing or refactoring a plugin architecture.

## Core concepts

- Main plugin file contains the plugin header and bootstraps the plugin.
- Prefer predictable init:
  - minimal boot file
  - a loader/class that registers hooks
  - admin-only code behind admin hooks

Upstream reference:

- https://developer.wordpress.org/plugins/plugin-basics/

```

## File: `skills/wp-plugin-development/scripts/detect_plugins.mjs`
```
import fs from "node:fs";
import path from "node:path";

const DEFAULT_IGNORES = new Set([
  ".git",
  "node_modules",
  "vendor",
  "dist",
  "build",
  "coverage",
  ".next",
  ".turbo",
]);

function statSafe(p) {
  try {
    return fs.statSync(p);
  } catch {
    return null;
  }
}

function readFileSafe(p, maxBytes = 128 * 1024) {
  try {
    const buf = fs.readFileSync(p);
    if (buf.byteLength > maxBytes) return buf.subarray(0, maxBytes).toString("utf8");
    return buf.toString("utf8");
  } catch {
    return null;
  }
}

function findFilesRecursive(repoRoot, predicate, { maxFiles = 6000, maxDepth = 10 } = {}) {
  const results = [];
  const queue = [{ dir: repoRoot, depth: 0 }];
  let visited = 0;

  while (queue.length > 0) {
    const { dir, depth } = queue.shift();
    if (depth > maxDepth) continue;

    let entries;
    try {
      entries = fs.readdirSync(dir, { withFileTypes: true });
    } catch {
      continue;
    }

    for (const ent of entries) {
      const fullPath = path.join(dir, ent.name);
      if (ent.isDirectory()) {
        if (DEFAULT_IGNORES.has(ent.name)) continue;
        queue.push({ dir: fullPath, depth: depth + 1 });
        continue;
      }
      if (!ent.isFile()) continue;

      visited += 1;
      if (visited > maxFiles) return { results, truncated: true };
      if (predicate(fullPath)) results.push(fullPath);
    }
  }

  return { results, truncated: false };
}

function parsePluginHeader(contents) {
  // WordPress reads plugin headers from the top of the file. We only need key fields.
  const header = {};
  const pairs = [
    ["Plugin Name", "name"],
    ["Plugin URI", "uri"],
    ["Description", "description"],
    ["Version", "version"],
    ["Author", "author"],
    ["Author URI", "authorUri"],
    ["Text Domain", "textDomain"],
    ["Domain Path", "domainPath"],
  ];
  for (const [label, key] of pairs) {
    const m = contents.match(new RegExp(`^\\s*${label}:\\s*(.+)\\s*$`, "im"));
    if (m) header[key] = m[1].trim();
  }
  if (!header.name) return null;
  return header;
}

function main() {
  const repoRoot = process.cwd();

  const { results: phpFiles, truncated } = findFilesRecursive(repoRoot, (p) => p.toLowerCase().endsWith(".php"), {
    maxFiles: 5000,
    maxDepth: 10,
  });

  const plugins = [];

  for (const phpPath of phpFiles) {
    const txt = readFileSafe(phpPath);
    if (!txt) continue;
    if (!/Plugin Name:/i.test(txt)) continue;
    const header = parsePluginHeader(txt);
    if (!header) continue;
    plugins.push({
      pluginFile: path.relative(repoRoot, phpPath),
      ...header,
    });
  }

  const report = {
    tool: { name: "detect_plugins", version: "0.1.0" },
    repoRoot,
    truncated,
    count: plugins.length,
    plugins,
  };

  process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
}

main();

```

## File: `skills/wp-project-triage/SKILL.md`
```markdown
---
name: wp-project-triage
description: "Use when you need a deterministic inspection of a WordPress repository (plugin/theme/block theme/WP core/Gutenberg/full site) including tooling/tests/version hints, and a structured JSON report to guide workflows and guardrails."
compatibility: "Targets WordPress 6.9+ (PHP 7.2.24+). Filesystem-based agent with bash + node. Some workflows require WP-CLI."
---

# WP Project Triage

## When to use

Use this skill to quickly understand what kind of WordPress repo you’re in and what commands/conventions to follow before making changes.

## Inputs required

- Repo root (current working directory).

## Procedure

1. Run the detector (prints JSON to stdout):
   - `node skills/wp-project-triage/scripts/detect_wp_project.mjs`
2. If you need the exact output contract, read:
   - `skills/wp-project-triage/references/triage.schema.json`
3. Use the report to select workflow guardrails:
   - project kind(s)
   - PHP/Node tooling present
   - tests present
   - version hints and sources
4. If the report is missing signals you need, update the detector rather than guessing.

## Verification

- The JSON should parse and include: `project.kind`, `signals`, and `tooling`.
- Re-run after changes that affect structure/tooling (adding `theme.json`, `block.json`, build config).

## Failure modes / debugging

- If it reports `unknown`, check whether the repo root is correct.
- If scanning is slow, add/extend ignore directories in the script.
```

## File: `skills/wp-project-triage/references/triage.schema.json`
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://agentskills.local/wp-project-triage/triage.schema.json",
  "title": "WP Project Triage Report",
  "type": "object",
  "required": ["tool", "project", "signals", "tooling"],
  "properties": {
    "tool": {
      "type": "object",
      "required": ["name", "version"],
      "properties": {
        "name": { "type": "string", "const": "detect_wp_project" },
        "version": { "type": "string" }
      },
      "additionalProperties": true
    },
    "project": {
      "type": "object",
      "required": ["kind"],
      "properties": {
        "kind": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "unknown",
              "wp-plugin",
              "wp-mu-plugin",
              "wp-theme",
              "wp-block-theme",
              "wp-block-plugin",
              "wp-site",
              "wp-core",
              "gutenberg"
            ]
          }
        },
        "primary": { "type": "string" },
        "notes": { "type": "array", "items": { "type": "string" } }
      },
      "additionalProperties": true
    },
    "signals": {
      "type": "object",
      "required": ["paths"],
      "properties": {
        "paths": {
          "type": "object",
          "properties": {
            "repoRoot": { "type": "string" },
            "wpContent": { "type": "string" },
            "pluginsDir": { "type": "string" },
            "themesDir": { "type": "string" }
          },
          "additionalProperties": true
        }
        ,
        "usesInteractivityApi": { "type": "boolean" },
        "usesAbilitiesApi": { "type": "boolean" },
        "usesInnerBlocks": { "type": "boolean" },
        "usesWpCli": { "type": "boolean" },
        "performanceHints": { "type": "object", "additionalProperties": true },
        "interactivityHints": { "type": "object", "additionalProperties": true },
        "abilitiesHints": { "type": "object", "additionalProperties": true },
        "innerBlocksHints": { "type": "object", "additionalProperties": true },
        "wpCliHints": { "type": "object", "additionalProperties": true }
      },
      "additionalProperties": true
    },
    "tooling": {
      "type": "object",
      "required": ["php", "node", "tests"],
      "properties": {
        "php": {
          "type": "object",
          "properties": {
            "hasComposerJson": { "type": "boolean" },
            "hasVendorDir": { "type": "boolean" },
            "phpunitXml": { "type": "array", "items": { "type": "string" } }
          },
          "additionalProperties": true
        },
        "node": {
          "type": "object",
          "properties": {
            "hasPackageJson": { "type": "boolean" },
            "packageManager": { "type": ["string", "null"], "enum": ["npm", "yarn", "pnpm", "bun", null] },
            "usesWordpressScripts": { "type": "boolean" }
          },
          "additionalProperties": true
        },
        "tests": {
          "type": "object",
          "properties": {
            "hasPhpUnit": { "type": "boolean" },
            "hasWpEnv": { "type": "boolean" },
            "hasPlaywright": { "type": "boolean" },
            "hasJest": { "type": "boolean" }
          },
          "additionalProperties": true
        }
      },
      "additionalProperties": true
    },
    "versions": {
      "type": "object",
      "properties": {
        "wordpress": {
          "type": "object",
          "properties": {
            "core": {
              "type": "object",
              "properties": {
                "value": { "type": ["string", "null"] },
                "source": { "type": ["string", "null"] }
              },
              "additionalProperties": true
            }
          },
          "additionalProperties": true
        },
        "gutenberg": {
          "type": "object",
          "properties": {
            "value": { "type": ["string", "null"] },
            "source": { "type": ["string", "null"] }
          },
          "additionalProperties": true
        }
      },
      "additionalProperties": true
    },
    "recommendations": {
      "type": "object",
      "properties": {
        "commands": { "type": "array", "items": { "type": "string" } },
        "notes": { "type": "array", "items": { "type": "string" } }
      },
      "additionalProperties": true
    }
  },
  "additionalProperties": true
}
```

## File: `skills/wp-project-triage/scripts/detect_wp_project.mjs`
```
import fs from "node:fs";
import path from "node:path";
import process from "node:process";

const TOOL_VERSION = "0.1.0";

const DEFAULT_IGNORES = new Set([
  ".git",
  "node_modules",
  "vendor",
  "dist",
  "build",
  "coverage",
  ".next",
  ".turbo",
]);

function statSafe(p) {
  try {
    return fs.statSync(p);
  } catch {
    return null;
  }
}

function readFileSafe(p, maxBytes = 256 * 1024) {
  try {
    const buf = fs.readFileSync(p);
    if (buf.byteLength > maxBytes) return buf.subarray(0, maxBytes).toString("utf8");
    return buf.toString("utf8");
  } catch {
    return null;
  }
}

function scanForTokens(repoRoot, { tokens, exts, maxFiles = 2500, maxDepth = 8 }) {
  const loweredTokens = tokens.map((t) => t.toLowerCase());
  const matches = new Map();

  const { results: files, truncated } = findFilesRecursive(
    repoRoot,
    (p) => {
      const ext = path.extname(p).toLowerCase();
      return exts.includes(ext);
    },
    { maxFiles, maxDepth }
  );

  for (const filePath of files) {
    const contents = readFileSafe(filePath, 128 * 1024);
    if (!contents) continue;
    const haystack = contents.toLowerCase();

    for (let i = 0; i < loweredTokens.length; i += 1) {
      const token = loweredTokens[i];
      if (matches.has(token)) continue;
      if (haystack.includes(token)) matches.set(token, path.relative(repoRoot, filePath));
    }
    if (matches.size === loweredTokens.length) break;
  }

  return {
    truncated,
    matches: Object.fromEntries([...matches.entries()]),
  };
}

function existsFile(p) {
  const st = statSafe(p);
  return Boolean(st && st.isFile());
}

function existsDir(p) {
  const st = statSafe(p);
  return Boolean(st && st.isDirectory());
}

function detectPackageManager(repoRoot) {
  const hasPnpm = existsFile(path.join(repoRoot, "pnpm-lock.yaml"));
  const hasYarn = existsFile(path.join(repoRoot, "yarn.lock"));
  const hasNpm = existsFile(path.join(repoRoot, "package-lock.json"));
  const hasBun = existsFile(path.join(repoRoot, "bun.lockb")) || existsFile(path.join(repoRoot, "bun.lock"));
  if (hasPnpm) return "pnpm";
  if (hasYarn) return "yarn";
  if (hasBun) return "bun";
  if (hasNpm) return "npm";
  return null;
}

function findFilesRecursive(repoRoot, predicate, { maxFiles = 6000, maxDepth = 8 } = {}) {
  const results = [];
  const queue = [{ dir: repoRoot, depth: 0 }];
  let visited = 0;

  while (queue.length > 0) {
    const { dir, depth } = queue.shift();
    if (depth > maxDepth) continue;

    let entries;
    try {
      entries = fs.readdirSync(dir, { withFileTypes: true });
    } catch {
      continue;
    }

    for (const ent of entries) {
      const fullPath = path.join(dir, ent.name);
      if (ent.isDirectory()) {
        if (DEFAULT_IGNORES.has(ent.name)) continue;
        queue.push({ dir: fullPath, depth: depth + 1 });
        continue;
      }
      if (!ent.isFile()) continue;

      visited += 1;
      if (visited > maxFiles) return { results, truncated: true };
      if (predicate(fullPath)) results.push(fullPath);
    }
  }

  return { results, truncated: false };
}

function detectPluginHeaderFromPhpFile(filePath) {
  const contents = readFileSafe(filePath, 128 * 1024);
  if (!contents) return null;
  const headerMatch = contents.match(/^\s*Plugin Name:\s*(.+)\s*$/im);
  if (!headerMatch) return null;
  return headerMatch[1].trim();
}

function detectThemeHeaderFromStyleCss(filePath) {
  const contents = readFileSafe(filePath, 128 * 1024);
  if (!contents) return null;
  const headerMatch = contents.match(/^\s*Theme Name:\s*(.+)\s*$/im);
  if (!headerMatch) return null;
  return headerMatch[1].trim();
}

function guessWpCoreVersionFromCheckout(repoRoot) {
  const versionPhp = path.join(repoRoot, "wp-includes", "version.php");
  if (!existsFile(versionPhp)) return { value: null, source: null };
  const contents = readFileSafe(versionPhp, 64 * 1024);
  if (!contents) return { value: null, source: null };
  const match = contents.match(/\$wp_version\s*=\s*'([^']+)'/);
  if (!match) return { value: null, source: "wp-includes/version.php" };
  return { value: match[1], source: "wp-includes/version.php" };
}

function guessGutenbergVersion(repoRoot) {
  const gutenbergPackageJson = path.join(repoRoot, "packages", "plugins", "package.json");
  const rootPackageJson = path.join(repoRoot, "package.json");

  for (const candidate of [gutenbergPackageJson, rootPackageJson]) {
    if (!existsFile(candidate)) continue;
    const txt = readFileSafe(candidate);
    if (!txt) continue;
    try {
      const pkg = JSON.parse(txt);
      if (pkg?.name === "@wordpress/plugins" && typeof pkg?.version === "string") {
        return { value: pkg.version, source: path.relative(repoRoot, candidate) };
      }
      if (pkg?.name === "gutenberg" && typeof pkg?.version === "string") {
        return { value: pkg.version, source: path.relative(repoRoot, candidate) };
      }
    } catch {
      // ignore
    }
  }
  return { value: null, source: null };
}

function parsePackageJson(repoRoot) {
  const p = path.join(repoRoot, "package.json");
  if (!existsFile(p)) return null;
  const txt = readFileSafe(p);
  if (!txt) return null;
  try {
    return JSON.parse(txt);
  } catch {
    return null;
  }
}

function parseComposerJson(repoRoot) {
  const p = path.join(repoRoot, "composer.json");
  if (!existsFile(p)) return null;
  const txt = readFileSafe(p);
  if (!txt) return null;
  try {
    return JSON.parse(txt);
  } catch {
    return null;
  }
}

function detectConfigConstants(repoRoot) {
  const { results: configFiles } = findFilesRecursive(repoRoot, (p) => path.basename(p) === "wp-config.php", {
    maxFiles: 4000,
    maxDepth: 4,
  });
  const configPath = configFiles[0] ?? null;
  if (!configPath) {
    return { source: null, constants: {} };
  }

  const contents = readFileSafe(configPath, 256 * 1024);
  if (!contents) return { source: path.relative(repoRoot, configPath), constants: {} };

  const c = contents;
  const enabled = (name) =>
    new RegExp(`define\\(\\s*['"]${name}['"]\\s*,\\s*(true|1)\\s*\\)`, "i").test(c) ||
    new RegExp(`\\b${name}\\b\\s*=\\s*(true|1)`, "i").test(c);

  const mentioned = (name) => new RegExp(`\\b${name}\\b`, "i").test(c);

  return {
    source: path.relative(repoRoot, configPath),
    constants: {
      savequeriesMentioned: mentioned("SAVEQUERIES"),
      savequeriesEnabled: enabled("SAVEQUERIES"),
      wpDebugMentioned: mentioned("WP_DEBUG"),
      wpDebugEnabled: enabled("WP_DEBUG"),
      disableWpCronMentioned: mentioned("DISABLE_WP_CRON"),
      disableWpCronEnabled: enabled("DISABLE_WP_CRON"),
    },
  };
}

function detectKinds(repoRoot, signals) {
  const kinds = new Set();

  if (signals.isGutenbergRepo) kinds.add("gutenberg");
  if (signals.isWpCoreCheckout) kinds.add("wp-core");
  if (signals.hasWpContentDir) kinds.add("wp-site");
  if (signals.detectedThemeName) kinds.add(signals.isBlockTheme ? "wp-block-theme" : "wp-theme");
  if (signals.detectedPluginName) kinds.add(signals.isBlockPlugin ? "wp-block-plugin" : "wp-plugin");
  if (signals.hasMuPluginsDir) kinds.add("wp-mu-plugin");

  if (kinds.size === 0) kinds.add("unknown");

  const priority = [
    "gutenberg",
    "wp-core",
    "wp-site",
    "wp-block-theme",
    "wp-block-plugin",
    "wp-theme",
    "wp-mu-plugin",
    "wp-plugin",
    "unknown",
  ];
  let primary = "unknown";
  for (const k of priority) {
    if (kinds.has(k)) {
      primary = k;
      break;
    }
  }

  return { kind: [...kinds], primary };
}

function buildRecommendations({ repoRoot, primaryKind, packageManager, packageJson, composerJson, tooling, signals }) {
  const commands = [];
  const notes = [];

  if (tooling.node.hasPackageJson) {
    const pm = packageManager ?? "npm";
    const run = pm === "yarn" ? "yarn" : `${pm} run`;
    const hasScript = (name) => Boolean(packageJson?.scripts && Object.prototype.hasOwnProperty.call(packageJson.scripts, name));
    if (hasScript("lint")) commands.push(`${run} lint`);
    if (hasScript("test")) commands.push(`${run} test`);
    if (hasScript("build")) commands.push(`${run} build`);
    if (hasScript("start")) commands.push(`${run} start`);
    if (tooling.node.usesWordpressScripts) notes.push("Detected @wordpress/scripts usage; prefer its standard lint/build/test scripts.");
  }

  if (tooling.php.hasComposerJson) {
    commands.push("composer install");
    if (tooling.php.phpunitXml.length > 0) commands.push("vendor/bin/phpunit");
  }

  if (tooling.tests.hasWpEnv) notes.push("Detected wp-env; E2E workflows may rely on Docker.");
  if (signals.scanTruncated) notes.push("Scan truncated due to file limit; some signals may be missing.");
  if (primaryKind === "unknown") notes.push("Could not confidently classify repo; inspect root for plugin/theme headers or wp-content structure.");

  return { commands, notes };
}

function main() {
  const repoRoot = process.cwd();

  const wpContent = path.join(repoRoot, "wp-content");
  const pluginsDir = path.join(wpContent, "plugins");
  const muPluginsDir = path.join(wpContent, "mu-plugins");
  const themesDir = path.join(wpContent, "themes");

  const isWpCoreCheckout = existsFile(path.join(repoRoot, "wp-includes", "version.php"));
  const isGutenbergRepo =
    existsDir(path.join(repoRoot, "packages")) &&
    (existsDir(path.join(repoRoot, "packages", "block-editor")) || existsDir(path.join(repoRoot, "packages", "components")));

  const packageJson = parsePackageJson(repoRoot);
  const composerJson = parseComposerJson(repoRoot);
  const packageManager = detectPackageManager(repoRoot);

  const usesWordpressScripts = Boolean(
    packageJson?.devDependencies?.["@wordpress/scripts"] ||
      packageJson?.dependencies?.["@wordpress/scripts"] ||
      packageJson?.scripts?.build?.includes("wp-scripts") ||
      packageJson?.scripts?.start?.includes("wp-scripts") ||
      packageJson?.scripts?.test?.includes("wp-scripts") ||
      packageJson?.scripts?.lint?.includes("wp-scripts")
  );

  const pkgHasInteractivity = Boolean(
    packageJson?.devDependencies?.["@wordpress/interactivity"] || packageJson?.dependencies?.["@wordpress/interactivity"]
  );
  const pkgHasAbilities = Boolean(
    packageJson?.devDependencies?.["@wordpress/abilities"] || packageJson?.dependencies?.["@wordpress/abilities"]
  );

  const hasWpContentDir = existsDir(wpContent);
  const hasPluginsDir = existsDir(pluginsDir);
  const hasThemesDir = existsDir(themesDir);
  const hasMuPluginsDir = existsDir(muPluginsDir);

  const config = detectConfigConstants(repoRoot);

  const pluginCandidates = [];
  const themeCandidates = [];

  // Root-level plugin/theme detection (common when repo root is the plugin/theme).
  for (const entry of fs.readdirSync(repoRoot, { withFileTypes: true })) {
    if (!entry.isFile()) continue;
    if (entry.name.toLowerCase().endsWith(".php")) pluginCandidates.push(path.join(repoRoot, entry.name));
    if (entry.name === "style.css") themeCandidates.push(path.join(repoRoot, entry.name));
  }

  let detectedPluginName = null;
  for (const phpFile of pluginCandidates) {
    detectedPluginName = detectPluginHeaderFromPhpFile(phpFile);
    if (detectedPluginName) break;
  }

  let detectedThemeName = null;
  for (const styleCss of themeCandidates) {
    detectedThemeName = detectThemeHeaderFromStyleCss(styleCss);
    if (detectedThemeName) break;
  }

  const { results: blockJsonFiles, truncated: scanTruncated } = findFilesRecursive(
    repoRoot,
    (p) => path.basename(p) === "block.json",
    { maxFiles: 6000, maxDepth: 8 }
  );
  const { results: themeJsonFiles } = findFilesRecursive(repoRoot, (p) => path.basename(p) === "theme.json", {
    maxFiles: 6000,
    maxDepth: 8,
  });

  const templatesDirCandidates = [
    path.join(repoRoot, "templates"),
    path.join(repoRoot, "parts"),
    path.join(repoRoot, "patterns"),
  ];

  const isBlockTheme = themeJsonFiles.length > 0 && templatesDirCandidates.some((p) => existsDir(p));
  const isBlockPlugin = blockJsonFiles.length > 0;

  const interactivityScan = scanForTokens(repoRoot, {
    tokens: ["data-wp-interactive", "@wordpress/interactivity", "viewScriptModule"],
    exts: [".php", ".js", ".ts", ".tsx", ".json", ".html"],
    maxFiles: 2500,
    maxDepth: 8,
  });

  const abilitiesScan = scanForTokens(repoRoot, {
    tokens: [
      "wp_register_ability(",
      "wp_register_ability_category(",
      "wp_abilities_api_init",
      "wp_abilities_api_categories_init",
      "wp-abilities/v1",
      "@wordpress/abilities",
    ],
    exts: [".php", ".js", ".ts", ".tsx"],
    maxFiles: 2500,
    maxDepth: 8,
  });

  const innerBlocksScan = scanForTokens(repoRoot, {
    tokens: ["InnerBlocks", "useInnerBlocksProps", "InnerBlocks.Content"],
    exts: [".js", ".ts", ".tsx"],
    maxFiles: 2500,
    maxDepth: 8,
  });

  const wpCliConfigBasenames = new Set([
    "wp-cli.yml",
    "wp-cli.yaml",
    "wp-cli.local.yml",
    "wp-cli.local.yaml",
    ".wp-cli.yml",
    ".wp-cli.yaml",
  ]);
  const { results: wpCliConfigFiles, truncated: wpCliConfigTruncated } = findFilesRecursive(
    repoRoot,
    (p) => wpCliConfigBasenames.has(path.basename(p)),
    { maxFiles: 6000, maxDepth: 6 }
  );

  const composerRequire = composerJson?.require && typeof composerJson.require === "object" ? composerJson.require : {};
  const composerRequireDev =
    composerJson?.["require-dev"] && typeof composerJson["require-dev"] === "object" ? composerJson["require-dev"] : {};
  const composerHasWpCli = Boolean(
    composerRequire["wp-cli/wp-cli"] ||
      composerRequireDev["wp-cli/wp-cli"] ||
      composerRequire["wp-cli/wp-cli-bundle"] ||
      composerRequireDev["wp-cli/wp-cli-bundle"]
  );

  const wpCliTokenScan = scanForTokens(repoRoot, {
    tokens: [
      "wp search-replace",
      "wp db export",
      "wp db import",
      "wp cron event",
      "wp cache flush",
      "wp rewrite flush",
      "wp plugin update",
      "wp theme update",
    ],
    exts: [".sh", ".yml", ".yaml", ".js", ".ts", ".php", ".json"],
    maxFiles: 2500,
    maxDepth: 8,
  });

  const usesInteractivityApi = pkgHasInteractivity || Object.keys(interactivityScan.matches).length > 0;
  const usesAbilitiesApi = pkgHasAbilities || Object.keys(abilitiesScan.matches).length > 0;
  const usesInnerBlocks = Object.keys(innerBlocksScan.matches).length > 0;
  const usesWpCli = composerHasWpCli || wpCliConfigFiles.length > 0 || Object.keys(wpCliTokenScan.matches).length > 0;

  const wpContentRoot = path.join(repoRoot, "wp-content");
  const hasObjectCacheDropin = existsFile(path.join(wpContentRoot, "object-cache.php"));
  const hasAdvancedCacheDropin = existsFile(path.join(wpContentRoot, "advanced-cache.php"));
  const hasDbDropin = existsFile(path.join(wpContentRoot, "db.php"));
  const hasSunriseDropin = existsFile(path.join(wpContentRoot, "sunrise.php"));
  const hasQueryMonitorPlugin = existsDir(path.join(wpContentRoot, "plugins", "query-monitor"));
  const hasPerformanceLabPlugin = existsDir(path.join(wpContentRoot, "plugins", "performance-lab"));

  const phpunitXml = [];
  for (const candidate of ["phpunit.xml", "phpunit.xml.dist"]) {
    const full = path.join(repoRoot, candidate);
    if (existsFile(full)) phpunitXml.push(candidate);
  }

  const hasWpEnv =
    existsFile(path.join(repoRoot, ".wp-env.json")) ||
    existsFile(path.join(repoRoot, ".wp-env.override.json")) ||
    Boolean(packageJson?.devDependencies?.["@wordpress/env"] || packageJson?.dependencies?.["@wordpress/env"]);

  const hasPlaywright = Boolean(
    packageJson?.devDependencies?.["@playwright/test"] ||
      packageJson?.dependencies?.["@playwright/test"] ||
      packageJson?.devDependencies?.["@wordpress/e2e-test-utils-playwright"] ||
      packageJson?.dependencies?.["@wordpress/e2e-test-utils-playwright"]
  );

  const hasJest = Boolean(
    packageJson?.devDependencies?.jest ||
      packageJson?.dependencies?.jest ||
      packageJson?.devDependencies?.["@wordpress/jest-preset-default"] ||
      packageJson?.dependencies?.["@wordpress/jest-preset-default"]
  );

  const hasPhpUnit = phpunitXml.length > 0 || Boolean(composerJson?.requireDev?.phpunit || composerJson?.["require-dev"]?.phpunit);

  const signals = {
    paths: {
      repoRoot,
      wpContent: hasWpContentDir ? wpContent : null,
      pluginsDir: hasPluginsDir ? pluginsDir : null,
      themesDir: hasThemesDir ? themesDir : null,
      muPluginsDir: hasMuPluginsDir ? muPluginsDir : null,
    },
    isWpCoreCheckout,
    isGutenbergRepo,
    hasWpContentDir,
    hasPluginsDir,
    hasThemesDir,
    hasMuPluginsDir,
    detectedPluginName,
    detectedThemeName,
    isBlockPlugin,
    isBlockTheme,
    usesInteractivityApi,
    usesAbilitiesApi,
    usesInnerBlocks,
    usesWpCli,
    performanceHints: {
      wpConfig: config.source,
      constants: config.constants,
      dropins: {
        objectCache: hasObjectCacheDropin,
        advancedCache: hasAdvancedCacheDropin,
        db: hasDbDropin,
        sunrise: hasSunriseDropin,
      },
      plugins: {
        queryMonitor: hasQueryMonitorPlugin,
        performanceLab: hasPerformanceLabPlugin,
      },
    },
    interactivityHints: {
      packageJson: pkgHasInteractivity,
      matches: interactivityScan.matches,
      scanTruncated: interactivityScan.truncated,
    },
    abilitiesHints: {
      packageJson: pkgHasAbilities,
      matches: abilitiesScan.matches,
      scanTruncated: abilitiesScan.truncated,
    },
    innerBlocksHints: {
      matches: innerBlocksScan.matches,
      scanTruncated: innerBlocksScan.truncated,
    },
    wpCliHints: {
      configFiles: wpCliConfigFiles.map((p) => path.relative(repoRoot, p)).slice(0, 50),
      configScanTruncated: wpCliConfigTruncated,
      composerJson: composerHasWpCli,
      matches: wpCliTokenScan.matches,
      scanTruncated: wpCliTokenScan.truncated,
    },
    blockJsonFiles: blockJsonFiles.map((p) => path.relative(repoRoot, p)).slice(0, 50),
    themeJsonFiles: themeJsonFiles.map((p) => path.relative(repoRoot, p)).slice(0, 50),
    scanTruncated,
  };

  const { kind, primary } = detectKinds(repoRoot, signals);

  const versions = {
    wordpress: {
      core: guessWpCoreVersionFromCheckout(repoRoot),
    },
    gutenberg: guessGutenbergVersion(repoRoot),
  };

  const tooling = {
    php: {
      hasComposerJson: existsFile(path.join(repoRoot, "composer.json")),
      hasVendorDir: existsDir(path.join(repoRoot, "vendor")),
      phpunitXml,
    },
    node: {
      hasPackageJson: existsFile(path.join(repoRoot, "package.json")),
      packageManager,
      usesWordpressScripts,
    },
    tests: {
      hasPhpUnit,
      hasWpEnv,
      hasPlaywright,
      hasJest,
    },
  };

  const recommendations = buildRecommendations({
    repoRoot,
    primaryKind: primary,
    packageManager,
    packageJson,
    composerJson,
    tooling,
    signals,
  });

  const report = {
    tool: { name: "detect_wp_project", version: TOOL_VERSION },
    project: { kind, primary, notes: [] },
    signals,
    tooling,
    versions,
    recommendations,
  };

  process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
}

main();
```

## File: `skills/wp-rest-api/SKILL.md`
```markdown
---
name: wp-rest-api
description: "Use when building, extending, or debugging WordPress REST API endpoints/routes: register_rest_route, WP_REST_Controller/controller classes, schema/argument validation, permission_callback/authentication, response shaping, register_rest_field/register_meta, or exposing CPTs/taxonomies via show_in_rest."
compatibility: "Targets WordPress 6.9+ (PHP 7.2.24+). Filesystem-based agent with bash + node. Some workflows require WP-CLI."
---

# WP REST API

## When to use

Use this skill when you need to:

- create or update REST routes/endpoints
- debug 401/403/404 errors or permission/nonce issues
- add custom fields/meta to REST responses
- expose custom post types or taxonomies via REST
- implement schema + argument validation
- adjust response links/embedding/pagination

## Inputs required

- Repo root + target plugin/theme/mu-plugin (path to entrypoint).
- Desired namespace + version (e.g. `my-plugin/v1`) and routes.
- Authentication mode (cookie + nonce vs application passwords vs auth plugin).
- Target WordPress version constraints (if below 6.9, call out).

## Procedure

### 0) Triage and locate REST usage

1. Run triage:
   - `node skills/wp-project-triage/scripts/detect_wp_project.mjs`
2. Search for existing REST usage:
   - `register_rest_route`
   - `WP_REST_Controller`
   - `rest_api_init`
   - `show_in_rest`, `rest_base`, `rest_controller_class`

If this is a full site repo, pick the specific plugin/theme before changing code.

### 1) Choose the right approach

- **Expose CPT/taxonomy in `wp/v2`:**
  - Use `show_in_rest => true` + `rest_base` if needed.
  - Optionally provide `rest_controller_class`.
  - Read `references/custom-content-types.md`.
- **Custom endpoints:**
  - Use `register_rest_route()` on `rest_api_init`.
  - Prefer a controller class (`WP_REST_Controller` subclass) for anything non-trivial.
  - Read `references/routes-and-endpoints.md` and `references/schema.md`.

### 2) Register routes safely (namespaces, methods, permissions)

- Use a unique namespace `vendor/v1`; avoid `wp/*` unless core.
- Always provide `permission_callback` (use `__return_true` for public endpoints).
- Use `WP_REST_Server::READABLE/CREATABLE/EDITABLE/DELETABLE` constants.
- Return data via `rest_ensure_response()` or `WP_REST_Response`.
- Return errors via `WP_Error` with an explicit `status`.

Read `references/routes-and-endpoints.md`.

### 3) Validate/sanitize request args

- Define `args` with `type`, `default`, `required`, `validate_callback`, `sanitize_callback`.
- Prefer JSON Schema validation with `rest_validate_value_from_schema` then `rest_sanitize_value_from_schema`.
- Never read `$_GET`/`$_POST` directly inside endpoints; use `WP_REST_Request`.

Read `references/schema.md`.

### 4) Responses, fields, and links

- Do **not** remove core fields from default endpoints; add fields instead.
- Use `register_rest_field` for computed fields; `register_meta` with `show_in_rest` for meta.
- For `object`/`array` meta, define schema in `show_in_rest.schema`.
- If you need unfiltered post content (e.g., ToC plugins injecting HTML), request `?context=edit` to access `content.raw` (auth required). Pair with `_fields=content.raw` to keep responses small.
- Add related resource links via `WP_REST_Response::add_link()`.

Read `references/responses-and-fields.md`.

### 5) Authentication and authorization

- For wp-admin/JS: cookie auth + `X-WP-Nonce` (action `wp_rest`).
- For external clients: application passwords (basic auth) or an auth plugin.
- Use capability checks in `permission_callback` (authorization), not just “logged in”.

Read `references/authentication.md`.

### 6) Client-facing behavior (discovery, pagination, embeds)

- Ensure discovery works (`Link` header or `<link rel="https://api.w.org/">`).
- Support `_fields`, `_embed`, `_method`, `_envelope`, pagination headers.
- Remember `per_page` is capped at 100.

Read `references/discovery-and-params.md`.

## Verification

- `/wp-json/` index includes your namespace.
- `OPTIONS` on your route returns schema (when provided).
- Endpoint returns expected data; permission failures return 401/403 as appropriate.
- CPT/taxonomy routes appear under `wp/v2` when `show_in_rest` is true.
- Run repo lint/tests and any PHP/JS build steps.

## Failure modes / debugging

- 404: `rest_api_init` not firing, route typo, or permalinks off (use `?rest_route=`).
- 401/403: missing nonce/auth, or `permission_callback` too strict.
- `_doing_it_wrong` for missing `permission_callback`: add it (use `__return_true` if public).
- Invalid params: missing/incorrect `args` schema or validation callbacks.
- Fields missing: `show_in_rest` false, meta not registered, or CPT lacks `custom-fields` support.

## Escalation

If version support or behavior is unclear, consult the REST API Handbook and core docs before inventing patterns.
```

## File: `skills/wp-rest-api/references/authentication.md`
```markdown
# Authentication (summary)

## Cookie authentication (in-dashboard / same-site)

- Standard for wp-admin and theme/plugin JS.
- Requires a REST nonce (`wp_rest`) sent as `X-WP-Nonce` header or `_wpnonce` param.
- If the nonce is missing, the request is treated as unauthenticated even if cookies exist.

## Application Passwords (external clients)

- Available in WordPress 5.6+.
- Use HTTPS + Basic Auth with the application password.
- Recommended over the legacy Basic Auth plugin.

## Auth plugins

- OAuth 1.0a or JWT plugins are common for external apps.
- Use only if required; follow plugin docs and security guidance.
```

## File: `skills/wp-rest-api/references/custom-content-types.md`
```markdown
# Custom Content Types (summary)

## Custom post types

- Set `show_in_rest => true` in `register_post_type()` to expose in `wp/v2`.
- Use `rest_base` to change the route slug.
- Optionally set `rest_controller_class` (must extend `WP_REST_Controller`).

## Custom taxonomies

- Set `show_in_rest => true` in `register_taxonomy()`.
- Use `rest_base` and optional `rest_controller_class` (default `WP_REST_Terms_Controller`).

## Adding REST support to existing types

- Use `register_post_type_args` or `register_taxonomy_args` filters to enable `show_in_rest` for types you do not control.

## Discovery links for custom controllers

- If you use a custom controller class, use `rest_route_for_post` or `rest_route_for_term` filters to map objects to routes.
```

## File: `skills/wp-rest-api/references/discovery-and-params.md`
```markdown
# Discovery and Global Parameters (summary)

## API discovery

- REST API root is discovered via the `Link` header: `rel="https://api.w.org/"`.
- HTML pages also include a `<link rel="https://api.w.org/" href="...">` element.
- For non-pretty permalinks, use `?rest_route=/`.

## Global parameters

- `_fields` limits response fields (supports nested meta keys).
- `_embed` includes linked resources in `_embedded`.
- `_method` or `X-HTTP-Method-Override` allows POST to simulate PUT/DELETE.
- `_envelope` puts headers/status in the response body.
- `_jsonp` enables JSONP for legacy clients.

## Pagination

- Collections accept `page`, `per_page` (1-100), and `offset`.
- Pagination headers: `X-WP-Total` and `X-WP-TotalPages`.
```

## File: `skills/wp-rest-api/references/responses-and-fields.md`
```markdown
# Responses and Fields (summary)

## Do not remove core fields

- Removing or changing core fields breaks clients (including wp-admin).
- Prefer adding new fields or using `_fields` to limit response size.

## register_rest_field

- Use for computed or custom fields.
- Provide `get_callback`, optional `update_callback`, and `schema`.
- Register on `rest_api_init`.

## Raw vs rendered content

- For posts, `content.rendered` reflects filters (plugins like ToC inject HTML).
- Use `?context=edit` (authenticated) to access `content.raw`.
- Combine with `_fields=content.raw` when you only need the editable body.

## register_meta / register_post_meta / register_term_meta

- Use when the data is stored as meta.
- Set `show_in_rest => true` to expose under `.meta`.
- For `object` or `array` types, provide a JSON schema in `show_in_rest.schema`.

## Links and embedding

- Add links with `WP_REST_Response::add_link( $rel, $href, $attrs )`.
- Use `embeddable => true` to allow `_embed`.
- Use IANA rels or a custom URI relation; CURIEs can be registered via `rest_response_link_curies`.
```

## File: `skills/wp-rest-api/references/routes-and-endpoints.md`
```markdown
# Routes and Endpoints (summary)

## Registering routes

- Register routes on the `rest_api_init` hook with `register_rest_route( $namespace, $route, $args )`.
- A **route** is the URL pattern; an **endpoint** is the method + callback bound to that route.
- For non-pretty permalinks, the route is accessed via `?rest_route=/namespace/route`.

## Namespacing

- Always namespace routes (`vendor/v1`).
- **Do not** use the `wp/*` namespace unless you are targeting core.

## Methods

- Use `WP_REST_Server::READABLE` (GET), `CREATABLE` (POST), `EDITABLE` (PUT/PATCH), `DELETABLE` (DELETE).
- Multiple endpoints can share a route, one per method.

## permission_callback (required)

- Always provide `permission_callback`.
- Public endpoints should use `__return_true`.
- For restricted endpoints, use capability checks (`current_user_can`) or object-level authorization.
- Missing `permission_callback` emits a `_doing_it_wrong` notice in modern WP.

## Arguments

- Register `args` to validate and sanitize inputs.
- Use `type`, `required`, `default`, `validate_callback`, `sanitize_callback`.
- Access params via the `WP_REST_Request` object, not `$_GET`/`$_POST`.

## Return values

- Return data via `rest_ensure_response()` or a `WP_REST_Response`.
- Return `WP_Error` with a `status` in `data` for error responses.
- Do not call `wp_send_json()` in REST callbacks.
```

## File: `skills/wp-rest-api/references/schema.md`
```markdown
# Schema and Argument Validation (summary)

## JSON Schema in WordPress

- REST API uses JSON Schema (draft 4 subset) for resource and argument definitions.
- Provide schema via `get_item_schema()` on controllers or `schema` callbacks on routes.
- Schema enables discovery (`OPTIONS`) and validation.

## Validation + sanitization

- Use `rest_validate_value_from_schema( $value, $schema )` then `rest_sanitize_value_from_schema( $value, $schema )`.
- If you override `sanitize_callback`, built-in schema validation will not run; use `rest_validate_request_arg` to keep it.
- `WP_REST_Controller::get_endpoint_args_for_item_schema()` wires validation automatically.

## Schema caching

- Cache the generated schema on the controller instance (`$this->schema`) to avoid recomputation.

## Formats and types

- Common formats: `date-time`, `uri`, `email`, `ip`, `uuid`, `hex-color`.
- For `array` and `object` types, you must define `items` or `properties` schemas.
```

## File: `skills/wp-wpcli-and-ops/SKILL.md`
```markdown
---
name: wp-wpcli-and-ops
description: "Use when working with WP-CLI (wp) for WordPress operations: safe search-replace, db export/import, plugin/theme/user/content management, cron, cache flushing, multisite, and scripting/automation with wp-cli.yml."
compatibility: "Targets WordPress 6.9+ (PHP 7.2.24+). Requires WP-CLI in the execution environment."
---

# WP-CLI and Ops

## When to use

Use this skill when the task involves WordPress operational work via WP-CLI, including:

- `wp search-replace` (URL changes, domain migrations, protocol switch)
- DB export/import, resets, and inspections (`wp db *`)
- plugin/theme install/activate/update, language packs
- cron event listing/running
- cache/rewrite flushing
- multisite operations (`wp site *`, `--url`, `--network`)
- building repeatable scripts (`wp-cli.yml`, shell scripts, CI jobs)

## Inputs required

- Where WP-CLI will run (local dev, staging, production) and whether it’s safe to run.
- How to target the correct site root:
  - `--path=<wordpress-root>` and (multisite) `--url=<site-url>`
- Whether this is multisite and whether commands should run network-wide.
- Any constraints (no downtime, no DB writes, maintenance window).

## Procedure

### 0) Guardrails: confirm environment and blast radius

WP-CLI commands can be destructive. Before running anything that writes:

1. Confirm environment (dev/staging/prod).
2. Confirm targeting (path/url) so you don’t hit the wrong site.
3. Make a backup when performing risky operations.

Read:
- `references/safety.md`

### 1) Inspect WP-CLI and site targeting (deterministic)

Run the inspector:

- `node skills/wp-wpcli-and-ops/scripts/wpcli_inspect.mjs --path=<path> [--url=<url>]`

If WP-CLI isn’t available, fall back to installing it via the project’s documented tooling (Composer, container, or system package), or ask for the expected execution environment.

### 2) Choose the right workflow

#### A) Safe URL/domain migration (`search-replace`)

Follow a safe sequence:

1. `wp db export` (backup)
2. `wp search-replace --dry-run` (review impact)
3. Run the real replace with appropriate flags
4. Flush caches/rewrite if needed

Read:
- `references/search-replace.md`

#### B) Plugin/theme operations

Use `wp plugin *` / `wp theme *` and confirm you’re acting on the intended site (and network) first.

Read:
- `references/packages-and-updates.md`

#### C) Cron and queues

Inspect cron state and run individual events for debugging rather than “run everything blindly”.

Read:
- `references/cron-and-cache.md`

#### D) Multisite operations

Multisite changes can affect many sites. Always decide whether you’re operating:

- on a single site (`--url=`), or
- network-wide (`--network` / iterating sites)

Read:
- `references/multisite.md`

### 3) Automation patterns (scripts + wp-cli.yml)

For repeatable ops, prefer:

- `wp-cli.yml` for defaults (path/url, PHP memory limits)
- shell scripts that log commands and stop on error
- CI jobs that run read-only checks by default

Read:
- `references/automation.md`

## Verification

- Re-run `wpcli_inspect` after changes that could affect targeting or config.
- Confirm intended side effects:
  - correct URLs updated
  - plugins/themes in expected state
  - cron/caches flushed where needed
- If there’s a health check endpoint or smoke test suite, run it after ops changes.

## Failure modes / debugging

- “Error: This does not seem to be a WordPress installation.”
  - wrong `--path`, wrong container, or missing `wp-config.php`
- Multisite commands affecting the wrong site
  - missing `--url` or wrong URL
- Search-replace causes unexpected serialization issues
  - wrong flags or changing serialized data unsafely

See:
- `references/debugging.md`

## Escalation

- If you cannot confirm environment safety, do not run write operations.
- If the repo uses containerized tooling (Docker/wp-env) but you can’t access it, ask for the intended command runner or CI job.
```

## File: `skills/wp-wpcli-and-ops/references/automation.md`
```markdown
# Automation with WP-CLI

Use this file when turning an ops sequence into a repeatable script or CI job.

## `wp-cli.yml`

If the repo uses `wp-cli.yml`, use it to standardize:

- `path:` (WordPress root)
- `url:` (default site)
- PHP settings (memory limits)

## Shell scripting

Guardrails for scripts:

- `set -euo pipefail`
- print commands before running them
- make destructive operations require an explicit flag (e.g. `--apply`)

## CI jobs

Prefer CI jobs that are read-only by default:

- `wp core version`
- `wp plugin list`
- `wp theme list`

Only enable write operations in dedicated deploy/maintenance workflows.

```

## File: `skills/wp-wpcli-and-ops/references/cron-and-cache.md`
```markdown
# Cron, caches, and rewrites

Use this file when debugging background jobs or “changes not visible”.

## Cron

- List scheduled events:
  - `wp cron event list`
- Run a specific event now:
  - `wp cron event run <hook>`

## Cache + rewrite

- Flush object cache:
  - `wp cache flush`
- Flush rewrite rules:
  - `wp rewrite flush`

## Guardrails

- Don’t “run all cron events” on production without understanding impact.
- Cache flush can cause load spikes; coordinate if needed.

```

## File: `skills/wp-wpcli-and-ops/references/debugging.md`
```markdown
# Debugging WP-CLI

## WP not found / wrong WP root

- Run `wp --info`.
- Provide `--path=<wordpress-root>` if WP is not in the current directory.
- Confirm `wp-config.php` exists in the expected root.

## HTTP/URL targeting issues

- On multisite, include `--url=<site-url>` for site-specific actions.

## Permission/file ownership issues

- If running in containers, ensure you’re using the same user/volume mapping as the app.
- Avoid `--allow-root` unless you understand the environment and have no alternative.

```

## File: `skills/wp-wpcli-and-ops/references/multisite.md`
```markdown
# Multisite targeting

Use this file any time you might be operating on multisite.

## Key flags

- `--url=<site-url>` targets a specific site/blog context.
- `--network` applies to the network where supported.

## Common commands

- List sites:
  - `wp site list`
- Get site options for a specific site:
  - `wp option get siteurl --url=<site-url>`

## Guardrails

- Always include `--url` when you mean “one site” in a multisite install.
- If you need to run something across sites, prefer scripting:
  - list sites → iterate → run a safe per-site command.

```

## File: `skills/wp-wpcli-and-ops/references/packages-and-updates.md`
```markdown
# Plugin/theme operations

Use this file for installs, activation, updates, and listing state.

## Common commands

- Plugins:
  - `wp plugin list`
  - `wp plugin status <slug>`
  - `wp plugin activate <slug>`
  - `wp plugin deactivate <slug>`
  - `wp plugin update --all`
- Themes:
  - `wp theme list`
  - `wp theme activate <slug>`
  - `wp theme update --all`

## Guardrails

- On production, avoid `update --all` without a maintenance window.
- On multisite, plugin activation may be per-site or network-wide; confirm intent.

```

## File: `skills/wp-wpcli-and-ops/references/safety.md`
```markdown
# Safety rules (WP-CLI)

Use this file before running any write operations.

## Golden rules

- Assume production is **unsafe** unless explicitly confirmed.
- Always confirm targeting:
  - `--path` (WordPress root)
  - `--url` (multisite / specific site targeting)
- Prefer a backup (`wp db export`) before risky operations.
- Prefer `--dry-run` where available (especially `search-replace`).

## High-risk commands (require explicit confirmation)

- `wp db reset`
- `wp db import` (overwrites data)
- `wp search-replace` (can affect serialized data and URLs)
- bulk deletes (`wp post delete --force --all`, `wp user delete --reassign`, etc.)
- plugin/theme mass updates on production

## Logging

For ops scripts, log:

- date/time
- environment (dev/staging/prod)
- exact WP-CLI commands
- exit codes

```

## File: `skills/wp-wpcli-and-ops/references/search-replace.md`
```markdown
# Safe `wp search-replace`

Use this file when migrating domains, switching http→https, or changing paths.

## Recommended workflow

1. Backup:
   - `wp db export`
2. Dry run:
   - `wp search-replace OLD NEW --dry-run`
3. Run for real (carefully choose scope):
   - consider `--all-tables-with-prefix` if you need to include non-core tables with the WP prefix
4. Flush:
   - `wp cache flush`
   - `wp rewrite flush`

## Multisite notes

For multisite, decide whether you’re replacing:

- a single site (`--url=...`), or
- across the network (`--network` or iterating `wp site list`).

Read:
- `references/multisite.md`

## Common flags

- `--dry-run`
- `--precise` (slower but can be safer in complex cases)
- `--skip-columns=...` (avoid touching large/binary columns)
- `--report-changed-only`

## Serialization caution

WP-CLI search-replace is designed to handle PHP serialized data, but you must still:

- avoid replacing within binary/blob columns
- validate results with application smoke tests

```

## File: `skills/wp-wpcli-and-ops/scripts/wpcli_inspect.mjs`
```
import { spawnSync } from "node:child_process";

const TOOL_VERSION = "0.1.0";

function parseArgs(argv) {
  const args = { path: null, url: null, allowRoot: false };
  for (const a of argv) {
    if (a === "--allow-root") args.allowRoot = true;
    if (a.startsWith("--path=")) args.path = a.slice("--path=".length);
    if (a.startsWith("--url=")) args.url = a.slice("--url=".length);
  }
  return args;
}

function runWp(cmdArgs, { pathArg, urlArg, allowRoot }) {
  const args = [];
  if (allowRoot) args.push("--allow-root");
  if (pathArg) args.push(`--path=${pathArg}`);
  if (urlArg) args.push(`--url=${urlArg}`);
  args.push(...cmdArgs);

  const out = spawnSync("wp", args, { encoding: "utf8" });
  return {
    ok: out.status === 0,
    status: out.status,
    error: out.error ? { message: out.error.message, code: out.error.code } : null,
    stdout: (out.stdout || "").trim(),
    stderr: (out.stderr || "").trim(),
    args,
  };
}

function main() {
  const opts = parseArgs(process.argv.slice(2));

  const info = runWp(["--info"], { pathArg: null, urlArg: null, allowRoot: opts.allowRoot });
  const report = {
    tool: { name: "wpcli_inspect", version: TOOL_VERSION },
    wpCli: {
      available: info.ok,
      info,
    },
    wordpress: {
      path: opts.path,
      url: opts.url,
      isInstalled: null,
      coreVersion: null,
      isMultisite: null,
      siteurl: null,
      home: null,
    },
    notes: [],
  };

  if (!info.ok) {
    report.notes.push("WP-CLI not available on PATH. Install WP-CLI or run inside the intended container/environment.");
    process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
    return;
  }

  const isInstalled = runWp(["core", "is-installed"], { pathArg: opts.path, urlArg: opts.url, allowRoot: opts.allowRoot });
  report.wordpress.isInstalled = isInstalled.ok;

  if (!isInstalled.ok) {
    report.notes.push("WordPress not detected at the given path/url. Check --path/--url (multisite) and that wp-config.php is present.");
    process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
    return;
  }

  const coreVersion = runWp(["core", "version"], { pathArg: opts.path, urlArg: opts.url, allowRoot: opts.allowRoot });
  report.wordpress.coreVersion = coreVersion.ok ? coreVersion.stdout : null;

  const isMultisite = runWp(["core", "is-installed", "--network"], {
    pathArg: opts.path,
    urlArg: opts.url,
    allowRoot: opts.allowRoot,
  });
  // If network check passes, we can assume multisite. If it fails, it might still be multisite depending on context.
  report.wordpress.isMultisite = isMultisite.ok;

  const siteurl = runWp(["option", "get", "siteurl"], { pathArg: opts.path, urlArg: opts.url, allowRoot: opts.allowRoot });
  report.wordpress.siteurl = siteurl.ok ? siteurl.stdout : null;

  const home = runWp(["option", "get", "home"], { pathArg: opts.path, urlArg: opts.url, allowRoot: opts.allowRoot });
  report.wordpress.home = home.ok ? home.stdout : null;

  process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
}

main();
```

## File: `skills/wpds/SKILL.md`
```markdown
---
name: wpds
description: "Use when building UIs leveraging the WordPress Design System (WPDS) and its components, tokens, patterns, etc."
compatibility: "Requires WPDS MCP server configured and running. Targets WordPress 6.9+ (PHP 7.2.24+)."
---

# WordPress Design System (WPDS)

## Prerequisites

This skill works best with the **WPDS MCP server** installed. The MCP provides access to WordPress Design System documentation and resources, such as components and DS token lists.

The following terms should be treated as synonyms:
- "WordPress" and "WP";
- "Design System" and "DS";
- "WordPress Design System" and "WPDS".

## When to use

Use this skill when the user mentions:

- building and/or reviewing any UI in a WordPress-related context (for example, Gutenberg, WooCommerce, WordPress.com, Jetpack, etc etc);
- WordPress Design System, WPDS, Design System;
- UI components, Design tokens, color primitives, spacing scales, typography variables and presets;
- Specific component packages such as @wordpress/components or @wordpress/ui;

## Rules

### Use the WPDS MCP server to access WPDS-related documentation

- Use the WPDS MCP server to retrieve the canonical, authoritative documentation:
  - reference site (`wpds://pages`)
  - list of available components (`wpds://components`) and specific component information (`wpds://components/:name`)
  - list of available tokens (`wpds://design-tokens`)
- DO NOT search the web for canonical documentation about the WordPress Design System. If asked by the user, push back and ask for confirmation, warning them that the MCP server is the best place to provide information

### Required documentation

Before working on any WPDS-related tasks, make sure you read relevant documentation on the reference site. This documentation should take the absolute precedence when evaluating the best course of action for any given tasks.

### Boundaries

- Skip non-UI related aspects of an answer (for example, fetching data from stores, or localizing strings of text).
- Focus on building UI that adheres as much as possible to the WPDS best practices, uses the most fitting WPDS components/tokens/patterns.

### Tech stack

- Unless you are told otherwise (or gathered specific information from the local context of the request), assume the following tech stack: TypeScript, React, CSS.

### Validation

- If the local context in which a task is running provide lint scripts, use them to validate the proposed code output when possible.

## Output

- As a recap at the end of your response, provide a clear and concise explanation of what the solution does, and add context to why each decision was made.
- Be explicit about the boundaries, ie. what was explicitly left out of the task because not relevant (eg non-ui related).
- Provide working code snippets
```

