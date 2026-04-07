---
id: ai-devkit
type: knowledge
owner: OA_Triage
---
# ai-devkit
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "ai-devkit",
  "version": "0.21.1",
  "private": true,
  "description": "A CLI toolkit for AI-assisted software development with phase templates and environment setup",
  "scripts": {
    "nx": "nx",
    "build": "nx run-many -t build",
    "lint": "nx run-many -t lint",
    "test": "nx run-many -t test",
    "test:watch": "nx run-many -t test --watch",
    "test:coverage": "nx run-many -t test --coverage",
    "test:e2e": "jest --config e2e/jest.config.js"
  },
  "workspaces": [
    "apps/*",
    "packages/*"
  ],
  "keywords": [
    "ai",
    "development",
    "cli",
    "templates",
    "cursor",
    "claude"
  ],
  "author": "",
  "license": "MIT",
  "devDependencies": {
    "@nx/js": "^22.4.0",
    "nx": "^22.4.0"
  },
  "engines": {
    "node": ">=20.20.0"
  }
}

```

### File: README.md
```md
# AI DevKit

**The toolkit for AI-assisted software development.**

AI DevKit helps AI coding agents work more effectively with your codebase. It provides structured workflows, persistent memory, and reusable skills — so agents follow the same engineering standards as senior developers.

[![npm version](https://img.shields.io/npm/v/ai-devkit.svg)](https://www.npmjs.com/package/ai-devkit)
[![npm downloads](https://img.shields.io/npm/dt/ai-devkit.svg)](https://www.npmjs.com/package/ai-devkit)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Quick Start

```bash
npx ai-devkit@latest init
```

This launches an interactive setup wizard that configures your project for AI-assisted development in under a minute.

## Supported Agents

| Agent | Status |
|-------|--------|
| [Claude Code](https://www.anthropic.com/claude-code) | ✅ Supported |
| [GitHub Copilot](https://code.visualstudio.com/) | ✅ Supported |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | ✅ Supported |
| [Cursor](https://cursor.sh/) | ✅ Supported |
| [opencode](https://opencode.ai/) | ✅ Supported |
| [Antigravity](https://antigravity.google/) | ✅ Supported |
| [Codex CLI](https://github.com/openai/codex) | ✅ Supported |
| [Windsurf](https://windsurf.com/) | 🚧 Testing |
| [Kilo Code](https://github.com/Kilo-Org/kilocode) | 🚧 Testing |
| [Roo Code](https://roocode.com/) | 🚧 Testing |
| [Amp](https://ampcode.com/) | 🚧 Testing |

## Documentation

📖 **Visit [ai-devkit.com](https://ai-devkit.com/docs/) for the full documentation**, including:

- Getting started guide
- Phase-based development workflow
- Memory system setup
- Skill management
- Agent configuration

## Contributing

We welcome contributions! See the [Contributing Guide](./CONTRIBUTING.md) for details.

```bash
git clone https://github.com/Codeaholicguy/ai-devkit.git
cd ai-devkit
npm install
npm run build
```

## License

MIT

```

### File: .agent_DISTILLED.md
```md
---
id: .agent
type: distilled_knowledge
---
# .agent

## SWALLOW ENGINE DISTILLATION

### File: workflows_DISTILLED.md
```md
---
id: workflows
type: distilled_knowledge
---
# workflows

## SWALLOW ENGINE DISTILLATION

### File: capture-knowledge.md
```md
---
description: Document a code entry point in knowledge docs.
---

Guide me through creating a structured understanding of a code entry point and saving it to the knowledge docs.

1. **Gather & Validate Entry Point** — If not already provided, ask for: entry point (file, folder, function, API), why it matters (feature, bug, investigation), and desired depth or focus areas. Confirm the entry point exists; if ambiguous or not found, clarify or suggest alternatives.
2. **Use Memory for Context** — Search memory for prior knowledge about this module/domain: `npx ai-devkit@latest memory search --query "<entry point or subsystem>"`.
3. **Collect Source Context** — Read the primary file/module and summarize purpose, exports, key patterns. For folders: list structure, highlight key modules. For functions/APIs: capture signature, parameters, return values, error handling. Extract essential snippets (avoid large dumps).
4. **Analyze Dependencies** — Build a dependency view up to depth 3, tracking visited nodes to avoid loops. Categorize: imports, function calls, services, external packages. Note external systems or generated code to exclude.
5. **Synthesize Explanation** — Draft overview (purpose, language, high-level behavior). Detail core logic, execution flow, key patterns. Highlight error handling, performance, security considerations. Identify potential improvements or risks.
6. **Create Documentation** — Normalize name to kebab-case (`calculateTotalPrice` → `calculate-total-price`). Create `docs/ai/implementation/knowledge-{name}.md` with sections: Overview, Implementation Details, Dependencies, Visual Diagrams, Additional Insights, Metadata, Next Steps. Include mermaid diagrams when they clarify flows or relationships. Add metadata (analysis date, depth, files touched).
7. **Store Reusable Knowledge** — If insights should persist across sessions, store them using `npx ai-devkit@latest memory store ...`.
8. **Review & Next Actions** — Summarize key insights and open questions. Suggest related areas for deeper dives, confirm file path, and suggest `/remember` for key long-lived rules.

```

### File: check-implementation.md
```md
---
description: Compare implementation with design and requirements docs to ensure alignment.
---

Compare the current implementation with the design in `docs/ai/design/` and requirements in `docs/ai/requirements/`.

1. If not already provided, ask for: feature/branch description, list of modified files, relevant design doc(s), and any known constraints or assumptions.
2. **Use Memory for Context** — Search memory for known constraints and prior decisions before assessing mismatches: `npx ai-devkit@latest memory search --query "<feature implementation alignment>"`.
3. For each design doc: summarize key architectural decisions and constraints, highlight components, interfaces, and data flows that must be respected.
4. File-by-file comparison: confirm implementation matches design intent, note deviations or missing pieces, flag logic gaps, edge cases, or security issues, suggest simplifications or refactors, and identify missing tests or documentation updates.
5. **Store Reusable Knowledge** — Save recurring alignment lessons/patterns with `npx ai-devkit@latest memory store ...`.
6. Summarize findings with recommended next steps.
7. **Next Command Guidance** — If major design issues are found, go back to `/review-design` or `/execute-plan`; if aligned, continue to `/writing-test`.

```

### File: code-review.md
```md
---
description: Pre-push code review against design docs.
---

Perform a local code review **before** pushing changes.

1. **Gather Context** — If not already provided, ask for: feature/branch description, list of modified files, relevant design doc(s) (e.g., `docs/ai/design/feature-{name}.md`), known constraints or risky areas, and which tests have been run. Also review the latest diff via `git status` and `git diff --stat`.
2. **Use Memory for Context** — Search memory for project review standards and recurring pitfalls: `npx ai-devkit@latest memory search --query "code review checklist project conventions"`.
3. **Understand Design Alignment** — For each design doc, summarize architectural intent and critical constraints.
4. **File-by-File Review** — For every modified file: check alignment with design/requirements and flag deviations, spot logic issues/edge cases/redundant code, flag security concerns (input validation, secrets, auth, data handling), check error handling/performance/observability, and identify missing or outdated tests.
5. **Cross-Cutting Concerns** — Verify naming consistency and project conventions. Confirm docs/comments updated where behavior changed. Identify missing tests (unit, integration, E2E). Check for needed configuration/migration updates.
6. **Store Reusable Knowledge** — Save durable review findings/checklists with `npx ai-devkit@latest memory store ...`.
7. **Summarize Findings** — Categorize each finding as **blocking**, **important**, or **nice-to-have** with: file, issue, impact, recommendation, and design reference.
8. **Next Command Guidance** — If blocking issues remain, return to `/execute-plan` (code fixes) or `/writing-test` (test gaps); if clean, proceed with push/PR workflow.

```

### File: debug-leak.md
```md
---
description: debug
---

test
```

### File: debug.md
```md
---
description: Debug an issue with structured root-cause analysis before changing code.
---

Help me debug an issue. Clarify expectations, identify gaps, and agree on a fix plan before changing code.

1. **Gather Context** — If not already provided, ask for: issue description (what is happening vs what should happen), error messages/logs/screenshots, recent related changes or deployments, and scope of impact.
2. **Use Memory for Context** — Search memory for similar incidents/fixes before deep investigation: `npx ai-devkit@latest memory search --query "<issue symptoms or error>"`.
3. **Clarify Reality vs Expectation** — Restate observed vs expected behavior. Confirm relevant requirements or docs that define the expectation. Define acceptance criteria for the fix.
4. **Reproduce & Isolate** — Determine reproducibility (always, intermittent, environment-specific). Capture reproduction steps. List suspected components or modules.
5. **Analyze Potential Causes** — Brainstorm root causes (data, config, code regressions, external dependencies). Gather supporting evidence (logs, metrics, traces). Highlight unknowns needing investigation.
6. **Resolve** — Present resolution options (quick fix, refactor, rollback, etc.) with pros/cons and risks. Ask which option to pursue. Summarize chosen approach, pre-work, success criteria, and validation steps.
7. **Store Reusable Knowledge** — Save root-cause and fix patterns via `npx ai-devkit@latest memory store ...`.
8. **Next Command Guidance** — After selecting a fix path, continue with `/execute-plan`; when implemented, use `/check-implementation` and `/writing-test`.

```

### File: execute-plan.md
```md
---
description: Execute a feature plan task by task.
---

Help me work through a feature plan one task at a time.

1. **Gather Context** — If not already provided, ask for: feature name (kebab-case, e.g., `user-authentication`), brief feature/branch description, planning doc path (default `docs/ai/planning/feature-{name}.md`), and any supporting docs (design, requirements, implementation).
2. **Use Memory for Context** — Search for prior implementation notes/patterns before starting: `npx ai-devkit@latest memory search --query "<feature implementation plan>"`.
3. **Load & Present Plan** — Read the planning doc and parse task lists (headings + checkboxes). Present an ordered task queue grouped by section, with status: `todo`, `in-progress`, `done`, `blocked`.
4. **Interactive Task Execution** — For each task in order: display context and full bullet text, reference relevant design/requirements docs, offer to outline sub-steps before starting, prompt for status update (`done`, `in-progress`, `blocked`, `skipped`) with short notes after work, and if blocked record blocker and move to a "Blocked" list.
5. **Update Planning Doc** — After each completed or status-changed task, run `/update-planning` to keep `docs/ai/planning/feature-{name}.md` accurate.
6. **Store Reusable Knowledge** — Save reusable implementation guidance/decisions with `npx ai-devkit@latest memory store ...`.
7. **Session Summary** — Produce a summary: Completed, In Progress (with next steps), Blocked (with blockers), Skipped/Deferred, and New Tasks.
8. **Next Command Guidance** — Continue `/execute-plan` until plan completion; then run `/check-implementation`.

```

### File: new-requirement.md
```md
---
description: Scaffold feature documentation from requirements through planning.
---

Guide me through adding a new feature, from requirements documentation to implementation readiness.

1. **Capture Requirement** — If not already provided, ask for: feature name (kebab-case, e.g., `user-authentication`), what problem it solves and who will use it, and key user stories.
2. **Use Memory for Context** — Before asking repetitive clarification questions, search memory for related decisions or conventions via `npx ai-devkit@latest memory search --query "<feature/topic>"` and reuse relevant context.
3. **Create Feature Documentation Structure** — Copy each template's content (preserving YAML frontmatter and section headings) into feature-specific files:
   - `docs/ai/requirements/README.md` → `docs/ai/requirements/feature-{name}.md`
   - `docs/ai/design/README.md` → `docs/ai/design/feature-{name}.md`
   - `docs/ai/planning/README.md` → `docs/ai/planning/feature-{name}.md`
   - `docs/ai/implementation/README.md` → `docs/ai/implementation/feature-{name}.md`
   - `docs/ai/testing/README.md` → `docs/ai/testing/feature-{name}.md`
4. **Requirements Phase** — Fill out `docs/ai/requirements/feature-{name}.md`: problem statement, goals/non-goals, user stories, success criteria, constraints, open questions.
5. **Design Phase** — Fill out `docs/ai/design/feature-{name}.md`: architecture changes, data models, API/interfaces, components, design decisions, security and performance considerations.
6. **Planning Phase** — Fill out `docs/ai/planning/feature-{name}.md`: task breakdown with subtasks, dependencies, effort estimates, implementation order, risks.
7. **Store Reusable Knowledge** — When important conventions or decisions are finalized, store them via `npx ai-devkit@latest memory store --title "<title>" --content "<knowledge>" --tags "<tags>"`.
8. **Next Command Guidance** — Run `/review-requirements` first, then `/review-design`. If both pass, continue with `/execute-plan`.

```

### File: remember.md
```md
---
description: Store reusable guidance in the knowledge memory service.
---

Help me store it in the knowledge memory service.

1. **Capture Knowledge** — If not already provided, ask for: a short explicit title (5-12 words), detailed content (markdown, examples encouraged), optional tags (keywords like "api", "testing"), and optional scope (`global`, `project:<name>`, `repo:<name>`). If vague, ask follow-ups to make it specific and actionable.
2. **Search Before Store** — Check for existing similar entries first with `npx ai-devkit@latest memory search --query "<topic>"` to avoid duplicates.
3. **Validate Quality** — Ensure it is specific and reusable (not generic advice). Avoid storing secrets or sensitive data.
4. **Store** — Call `memory.storeKnowledge` with title, content, tags, scope. If MCP tools are unavailable, use `npx ai-devkit@latest memory store` instead.
5. **Confirm** — Summarize what was saved and offer to retrieve related memory entries when helpful.
6. **Next Command Guidance** — Continue with the current lifecycle phase command (`/execute-plan`, `/check-implementation`, `/writing-test`, etc.) as needed.

```

### File: review-design.md
```md
---
description: Review feature design for completeness.
---

Review the design documentation in `docs/ai/design/feature-{name}.md` (and the project-level README if relevant).

1. **Use Memory for Context** — Search memory for prior architecture constraints/patterns: `npx ai-devkit@latest memory search --query "<feature design architecture>"`.
2. Summarize:
   - Architecture overview (ensure mermaid diagram is present and accurate)
   - Key components and their responsibilities
   - Technology choices and rationale
   - Data models and relationships
   - API/interface contracts (inputs, outputs, auth)
   - Major design decisions and trade-offs
   - Non-functional requirements that must be preserved
3. **Clarify and explore (loop until converged)**:
   - **Ask clarification questions** for every gap, inconsistency, or misalignment between requirements and design. Do not just list issues — actively ask specific questions to resolve them.
   - **Brainstorm and explore options** — For key architecture decisions, trade-offs, or areas with multiple viable approaches, proactively brainstorm alternatives. Present options with pros/cons and trade-offs. Challenge assumptions and surface creative alternatives.
   - **Repeat** — Continue looping until the user is satisfied with the chosen approach and no open questions remain.
4. **Store Reusable Knowledge** — Persist approved design patterns/constraints with `npx ai-devkit@latest memory store ...` when they will help future work.
5. **Next Command Guidance** — If requirements gaps are found, return to `/review-requirements`; if design is sound, continue to `/execute-plan`.

```

### File: review-requirements.md
```md
---
description: Review feature requirements for completeness.
---

Review `docs/ai/requirements/feature-{name}.md` and the project-level template `docs/ai/requirements/README.md` to ensure structure and content alignment.

1. **Use Memory for Context** — Search memory for related requirements/domain decisions before starting: `npx ai-devkit@latest memory search --query "<feature requirements>"`.
2. Summarize:
   - Core problem statement and affected users
   - Goals, non-goals, and success criteria
   - Primary user stories & critical flows
   - Constraints, assumptions, open questions
   - Any missing sections or deviations from the template
3. **Clarify and explore (loop until converged)**:
   - **Ask clarification questions** for every gap, contradiction, or ambiguity. Do not just list issues — actively ask specific questions to resolve them.
   - **Brainstorm and explore options** — For key decisions, trade-offs, or areas with multiple viable approaches, proactively brainstorm alternatives. Present options with pros/cons and trade-offs. Challenge assumptions and surface creative alternatives.
   - **Repe
... [TRUNCATED]
```

### File: .ai-devkit.json
```json
{
  "version": "0.4.2",
  "environments": [
    "cursor",
    "claude",
    "github",
    "gemini",
    "codex",
    "antigravity"
  ],
  "createdAt": "2025-12-28T13:35:45.251Z",
  "updatedAt": "2026-04-03T18:41:38.363Z",
  "phases": [
    "requirements",
    "design",
    "planning",
    "implementation",
    "testing"
  ],
  "skills": [
    {
      "registry": "codeaholicguy/ai-devkit",
      "name": "memory"
    },
    {
      "registry": "codeaholicguy/ai-devkit",
      "name": "dev-lifecycle"
    },
    {
      "registry": "codeaholicguy/ai-devkit",
      "name": "debug"
    },
    {
      "registry": "codeaholicguy/ai-devkit",
      "name": "simplify-implementation"
    },
    {
      "registry": "codeaholicguy/ai-devkit",
      "name": "technical-writer"
    },
    {
      "registry": "codeaholicguy/ai-devkit",
      "name": "verify"
    },
    {
      "registry": "codeaholicguy/ai-devkit",
      "name": "tdd"
    }
  ]
}

```

### File: .claude-plugin_DISTILLED.md
```md
---
id: .claude-plugin
type: distilled_knowledge
---
# .claude-plugin

## SWALLOW ENGINE DISTILLATION

### File: plugin.json
```json
{
  "name": "ai-devkit",
  "version": "0.21.1",
  "description": "Structured AI-assisted development with phase workflows, persistent memory, and reusable skills",
  "author": {
    "name": "Hoang Nguyen",
    "email": "hoang@codeaholicguy.com"
  },
  "homepage": "https://ai-devkit.com/",
  "repository": "https://github.com/codeaholicguy/ai-devkit",
  "license": "MIT",
  "keywords": [
    "ai",
    "development",
    "sdlc",
    "workflow",
    "memory",
    "skills",
    "testing",
    "code-review",
    "debugging"
  ]
}

```


```

### File: .claude_DISTILLED.md
```md
---
id: .claude
type: distilled_knowledge
---
# .claude

## SWALLOW ENGINE DISTILLATION

### File: commands_DISTILLED.md
```md
---
id: commands
type: distilled_knowledge
---
# commands

## SWALLOW ENGINE DISTILLATION

### File: capture-knowledge.md
```md
---
description: Document a code entry point in knowledge docs.
---

Guide me through creating a structured understanding of a code entry point and saving it to the knowledge docs.

1. **Gather & Validate Entry Point** — If not already provided, ask for: entry point (file, folder, function, API), why it matters (feature, bug, investigation), and desired depth or focus areas. Confirm the entry point exists; if ambiguous or not found, clarify or suggest alternatives.
2. **Use Memory for Context** — Search memory for prior knowledge about this module/domain: `npx ai-devkit@latest memory search --query "<entry point or subsystem>"`.
3. **Collect Source Context** — Read the primary file/module and summarize purpose, exports, key patterns. For folders: list structure, highlight key modules. For functions/APIs: capture signature, parameters, return values, error handling. Extract essential snippets (avoid large dumps).
4. **Analyze Dependencies** — Build a dependency view up to depth 3, tracking visited nodes to avoid loops. Categorize: imports, function calls, services, external packages. Note external systems or generated code to exclude.
5. **Synthesize Explanation** — Draft overview (purpose, language, high-level behavior). Detail core logic, execution flow, key patterns. Highlight error handling, performance, security considerations. Identify potential improvements or risks.
6. **Create Documentation** — Normalize name to kebab-case (`calculateTotalPrice` → `calculate-total-price`). Create `docs/ai/implementation/knowledge-{name}.md` with sections: Overview, Implementation Details, Dependencies, Visual Diagrams, Additional Insights, Metadata, Next Steps. Include mermaid diagrams when they clarify flows or relationships. Add metadata (analysis date, depth, files touched).
7. **Store Reusable Knowledge** — If insights should persist across sessions, store them using `npx ai-devkit@latest memory store ...`.
8. **Review & Next Actions** — Summarize key insights and open questions. Suggest related areas for deeper dives, confirm file path, and suggest `/remember` for key long-lived rules.

```

### File: check-implementation.md
```md
---
description: Compare implementation with design and requirements docs to ensure alignment.
---

Compare the current implementation with the design in `docs/ai/design/` and requirements in `docs/ai/requirements/`.

1. If not already provided, ask for: feature/branch description, list of modified files, relevant design doc(s), and any known constraints or assumptions.
2. **Use Memory for Context** — Search memory for known constraints and prior decisions before assessing mismatches: `npx ai-devkit@latest memory search --query "<feature implementation alignment>"`.
3. For each design doc: summarize key architectural decisions and constraints, highlight components, interfaces, and data flows that must be respected.
4. File-by-file comparison: confirm implementation matches design intent, note deviations or missing pieces, flag logic gaps, edge cases, or security issues, suggest simplifications or refactors, and identify missing tests or documentation updates.
5. **Store Reusable Knowledge** — Save recurring alignment lessons/patterns with `npx ai-devkit@latest memory store ...`.
6. Summarize findings with recommended next steps.
7. **Next Command Guidance** — If major design issues are found, go back to `/review-design` or `/execute-plan`; if aligned, continue to `/writing-test`.

```

### File: code-review.md
```md
---
description: Pre-push code review against design docs.
---

Perform a local code review **before** pushing changes.

1. **Gather Context** — If not already provided, ask for: feature/branch description, list of modified files, relevant design doc(s) (e.g., `docs/ai/design/feature-{name}.md`), known constraints or risky areas, and which tests have been run. Also review the latest diff via `git status` and `git diff --stat`.
2. **Use Memory for Context** — Search memory for project review standards and recurring pitfalls: `npx ai-devkit@latest memory search --query "code review checklist project conventions"`.
3. **Understand Design Alignment** — For each design doc, summarize architectural intent and critical constraints.
4. **File-by-File Review** — For every modified file: check alignment with design/requirements and flag deviations, spot logic issues/edge cases/redundant code, flag security concerns (input validation, secrets, auth, data handling), check error handling/performance/observability, and identify missing or outdated tests.
5. **Cross-Cutting Concerns** — Verify naming consistency and project conventions. Confirm docs/comments updated where behavior changed. Identify missing tests (unit, integration, E2E). Check for needed configuration/migration updates.
6. **Store Reusable Knowledge** — Save durable review findings/checklists with `npx ai-devkit@latest memory store ...`.
7. **Summarize Findings** — Categorize each finding as **blocking**, **important**, or **nice-to-have** with: file, issue, impact, recommendation, and design reference.
8. **Next Command Guidance** — If blocking issues remain, return to `/execute-plan` (code fixes) or `/writing-test` (test gaps); if clean, proceed with push/PR workflow.

```

### File: debug.md
```md
---
description: Debug an issue with structured root-cause analysis before changing code.
---

Help me debug an issue. Clarify expectations, identify gaps, and agree on a fix plan before changing code.

1. **Gather Context** — If not already provided, ask for: issue description (what is happening vs what should happen), error messages/logs/screenshots, recent related changes or deployments, and scope of impact.
2. **Use Memory for Context** — Search memory for similar incidents/fixes before deep investigation: `npx ai-devkit@latest memory search --query "<issue symptoms or error>"`.
3. **Clarify Reality vs Expectation** — Restate observed vs expected behavior. Confirm relevant requirements or docs that define the expectation. Define acceptance criteria for the fix.
4. **Reproduce & Isolate** — Determine reproducibility (always, intermittent, environment-specific). Capture reproduction steps. List suspected components or modules.
5. **Analyze Potential Causes** — Brainstorm root causes (data, config, code regressions, external dependencies). Gather supporting evidence (logs, metrics, traces). Highlight unknowns needing investigation.
6. **Resolve** — Present resolution options (quick fix, refactor, rollback, etc.) with pros/cons and risks. Ask which option to pursue. Summarize chosen approach, pre-work, success criteria, and validation steps.
7. **Store Reusable Knowledge** — Save root-cause and fix patterns via `npx ai-devkit@latest memory store ...`.
8. **Next Command Guidance** — After selecting a fix path, continue with `/execute-plan`; when implemented, use `/check-implementation` and `/writing-test`.

```

### File: execute-plan.md
```md
---
description: Execute a feature plan task by task.
---

Help me work through a feature plan one task at a time.

1. **Gather Context** — If not already provided, ask for: feature name (kebab-case, e.g., `user-authentication`), brief feature/branch description, planning doc path (default `docs/ai/planning/feature-{name}.md`), and any supporting docs (design, requirements, implementation).
2. **Use Memory for Context** — Search for prior implementation notes/patterns before starting: `npx ai-devkit@latest memory search --query "<feature implementation plan>"`.
3. **Load & Present Plan** — Read the planning doc and parse task lists (headings + checkboxes). Present an ordered task queue grouped by section, with status: `todo`, `in-progress`, `done`, `blocked`.
4. **Interactive Task Execution** — For each task in order: display context and full bullet text, reference relevant design/requirements docs, offer to outline sub-steps before starting, prompt for status update (`done`, `in-progress`, `blocked`, `skipped`) with short notes after work, and if blocked record blocker and move to a "Blocked" list.
5. **Update Planning Doc** — After each completed or status-changed task, run `/update-planning` to keep `docs/ai/planning/feature-{name}.md` accurate.
6. **Store Reusable Knowledge** — Save reusable implementation guidance/decisions with `npx ai-devkit@latest memory store ...`.
7. **Session Summary** — Produce a summary: Completed, In Progress (with next steps), Blocked (with blockers), Skipped/Deferred, and New Tasks.
8. **Next Command Guidance** — Continue `/execute-plan` until plan completion; then run `/check-implementation`.

```

### File: new-requirement.md
```md
---
description: Scaffold feature documentation from requirements through planning.
---

Guide me through adding a new feature, from requirements documentation to implementation readiness.

1. **Capture Requirement** — If not already provided, ask for: feature name (kebab-case, e.g., `user-authentication`), what problem it solves and who will use it, and key user stories.
2. **Use Memory for Context** — Before asking repetitive clarification questions, search memory for related decisions or conventions via `npx ai-devkit@latest memory search --query "<feature/topic>"` and reuse relevant context.
3. **Create Feature Documentation Structure** — Copy each template's content (preserving YAML frontmatter and section headings) into feature-specific files:
   - `docs/ai/requirements/README.md` → `docs/ai/requirements/feature-{name}.md`
   - `docs/ai/design/README.md` → `docs/ai/design/feature-{name}.md`
   - `docs/ai/planning/README.md` → `docs/ai/planning/feature-{name}.md`
   - `docs/ai/implementation/README.md` → `docs/ai/implementation/feature-{name}.md`
   - `docs/ai/testing/README.md` → `docs/ai/testing/feature-{name}.md`
4. **Requirements Phase** — Fill out `docs/ai/requirements/feature-{name}.md`: problem statement, goals/non-goals, user stories, success criteria, constraints, open questions.
5. **Design Phase** — Fill out `docs/ai/design/feature-{name}.md`: architecture changes, data models, API/interfaces, components, design decisions, security and performance considerations.
6. **Planning Phase** — Fill out `docs/ai/planning/feature-{name}.md`: task breakdown with subtasks, dependencies, effort estimates, implementation order, risks.
7. **Store Reusable Knowledge** — When important conventions or decisions are finalized, store them via `npx ai-devkit@latest memory store --title "<title>" --content "<knowledge>" --tags "<tags>"`.
8. **Next Command Guidance** — Run `/review-requirements` first, then `/review-design`. If both pass, continue with `/execute-plan`.

```

### File: remember.md
```md
---
description: Store reusable guidance in the knowledge memory service.
---

Help me store it in the knowledge memory service.

1. **Capture Knowledge** — If not already provided, ask for: a short explicit title (5-12 words), detailed content (markdown, examples encouraged), optional tags (keywords like "api", "testing"), and optional scope (`global`, `project:<name>`, `repo:<name>`). If vague, ask follow-ups to make it specific and actionable.
2. **Search Before Store** — Check for existing similar entries first with `npx ai-devkit@latest memory search --query "<topic>"` to avoid duplicates.
3. **Validate Quality** — Ensure it is specific and reusable (not generic advice). Avoid storing secrets or sensitive data.
4. **Store** — Call `memory.storeKnowledge` with title, content, tags, scope. If MCP tools are unavailable, use `npx ai-devkit@latest memory store` instead.
5. **Confirm** — Summarize what was saved and offer to retrieve related memory entries when helpful.
6. **Next Command Guidance** — Continue with the current lifecycle phase command (`/execute-plan`, `/check-implementation`, `/writing-test`, etc.) as needed.

```

### File: review-design.md
```md
---
description: Review feature design for completeness.
---

Review the design documentation in `docs/ai/design/feature-{name}.md` (and the project-level README if relevant).

1. **Use Memory for Context** — Search memory for prior architecture constraints/patterns: `npx ai-devkit@latest memory search --query "<feature design architecture>"`.
2. Summarize:
   - Architecture overview (ensure mermaid diagram is present and accurate)
   - Key components and their responsibilities
   - Technology choices and rationale
   - Data models and relationships
   - API/interface contracts (inputs, outputs, auth)
   - Major design decisions and trade-offs
   - Non-functional requirements that must be preserved
3. **Clarify and explore (loop until converged)**:
   - **Ask clarification questions** for every gap, inconsistency, or misalignment between requirements and design. Do not just list issues — actively ask specific questions to resolve them.
   - **Brainstorm and explore options** — For key architecture decisions, trade-offs, or areas with multiple viable approaches, proactively brainstorm alternatives. Present options with pros/cons and trade-offs. Challenge assumptions and surface creative alternatives.
   - **Repeat** — Continue looping until the user is satisfied with the chosen approach and no open questions remain.
4. **Store Reusable Knowledge** — Persist approved design patterns/constraints with `npx ai-devkit@latest memory store ...` when they will help future work.
5. **Next Command Guidance** — If requirements gaps are found, return to `/review-requirements`; if design is sound, continue to `/execute-plan`.

```

### File: review-requirements.md
```md
---
description: Review feature requirements for completeness.
---

Review `docs/ai/requirements/feature-{name}.md` and the project-level template `docs/ai/requirements/README.md` to ensure structure and content alignment.

1. **Use Memory for Context** — Search memory for related requirements/domain decisions before starting: `npx ai-devkit@latest memory search --query "<feature requirements>"`.
2. Summarize:
   - Core problem statement and affected users
   - Goals, non-goals, and success criteria
   - Primary user stories & critical flows
   - Constraints, assumptions, open questions
   - Any missing sections or deviations from the template
3. **Clarify and explore (loop until converged)**:
   - **Ask clarification questions** for every gap, contradiction, or ambiguity. Do not just list issues — actively ask specific questions to resolve them.
   - **Brainstorm and explore options** — For key decisions, trade-offs, or areas with multiple viable approaches, proactively brainstorm alternatives. Present options with pros/cons and trade-offs. Challenge assumptions and surface creative alternatives.
   - **Repeat** — Continue looping until the user is satisfied with the chosen a
... [TRUNCATED]
```

### File: .codex_DISTILLED.md
```md
---
id: .codex
type: distilled_knowledge
---
# .codex

## SWALLOW ENGINE DISTILLATION

### File: commands_DISTILLED.md
```md
---
id: commands
type: distilled_knowledge
---
# commands

## SWALLOW ENGINE DISTILLATION

### File: capture-knowledge.md
```md
---
description: Document a code entry point in knowledge docs.
---

Guide me through creating a structured understanding of a code entry point and saving it to the knowledge docs.

1. **Gather & Validate Entry Point** — If not already provided, ask for: entry point (file, folder, function, API), why it matters (feature, bug, investigation), and desired depth or focus areas. Confirm the entry point exists; if ambiguous or not found, clarify or suggest alternatives.
2. **Use Memory for Context** — Search memory for prior knowledge about this module/domain: `npx ai-devkit@latest memory search --query "<entry point or subsystem>"`.
3. **Collect Source Context** — Read the primary file/module and summarize purpose, exports, key patterns. For folders: list structure, highlight key modules. For functions/APIs: capture signature, parameters, return values, error handling. Extract essential snippets (avoid large dumps).
4. **Analyze Dependencies** — Build a dependency view up to depth 3, tracking visited nodes to avoid loops. Categorize: imports, function calls, services, external packages. Note external systems or generated code to exclude.
5. **Synthesize Explanation** — Draft overview (purpose, language, high-level behavior). Detail core logic, execution flow, key patterns. Highlight error handling, performance, security considerations. Identify potential improvements or risks.
6. **Create Documentation** — Normalize name to kebab-case (`calculateTotalPrice` → `calculate-total-price`). Create `docs/ai/implementation/knowledge-{name}.md` with sections: Overview, Implementation Details, Dependencies, Visual Diagrams, Additional Insights, Metadata, Next Steps. Include mermaid diagrams when they clarify flows or relationships. Add metadata (analysis date, depth, files touched).
7. **Store Reusable Knowledge** — If insights should persist across sessions, store them using `npx ai-devkit@latest memory store ...`.
8. **Review & Next Actions** — Summarize key insights and open questions. Suggest related areas for deeper dives, confirm file path, and suggest `/remember` for key long-lived rules.

```

### File: check-implementation.md
```md
---
description: Compare implementation with design and requirements docs to ensure alignment.
---

Compare the current implementation with the design in `docs/ai/design/` and requirements in `docs/ai/requirements/`.

1. If not already provided, ask for: feature/branch description, list of modified files, relevant design doc(s), and any known constraints or assumptions.
2. **Use Memory for Context** — Search memory for known constraints and prior decisions before assessing mismatches: `npx ai-devkit@latest memory search --query "<feature implementation alignment>"`.
3. For each design doc: summarize key architectural decisions and constraints, highlight components, interfaces, and data flows that must be respected.
4. File-by-file comparison: confirm implementation matches design intent, note deviations or missing pieces, flag logic gaps, edge cases, or security issues, suggest simplifications or refactors, and identify missing tests or documentation updates.
5. **Store Reusable Knowledge** — Save recurring alignment lessons/patterns with `npx ai-devkit@latest memory store ...`.
6. Summarize findings with recommended next steps.
7. **Next Command Guidance** — If major design issues are found, go back to `/review-design` or `/execute-plan`; if aligned, continue to `/writing-test`.

```

### File: code-review.md
```md
---
description: Pre-push code review against design docs.
---

Perform a local code review **before** pushing changes.

1. **Gather Context** — If not already provided, ask for: feature/branch description, list of modified files, relevant design doc(s) (e.g., `docs/ai/design/feature-{name}.md`), known constraints or risky areas, and which tests have been run. Also review the latest diff via `git status` and `git diff --stat`.
2. **Use Memory for Context** — Search memory for project review standards and recurring pitfalls: `npx ai-devkit@latest memory search --query "code review checklist project conventions"`.
3. **Understand Design Alignment** — For each design doc, summarize architectural intent and critical constraints.
4. **File-by-File Review** — For every modified file: check alignment with design/requirements and flag deviations, spot logic issues/edge cases/redundant code, flag security concerns (input validation, secrets, auth, data handling), check error handling/performance/observability, and identify missing or outdated tests.
5. **Cross-Cutting Concerns** — Verify naming consistency and project conventions. Confirm docs/comments updated where behavior changed. Identify missing tests (unit, integration, E2E). Check for needed configuration/migration updates.
6. **Store Reusable Knowledge** — Save durable review findings/checklists with `npx ai-devkit@latest memory store ...`.
7. **Summarize Findings** — Categorize each finding as **blocking**, **important**, or **nice-to-have** with: file, issue, impact, recommendation, and design reference.
8. **Next Command Guidance** — If blocking issues remain, return to `/execute-plan` (code fixes) or `/writing-test` (test gaps); if clean, proceed with push/PR workflow.

```

### File: debug.md
```md
---
description: Debug an issue with structured root-cause analysis before changing code.
---

Help me debug an issue. Clarify expectations, identify gaps, and agree on a fix plan before changing code.

1. **Gather Context** — If not already provided, ask for: issue description (what is happening vs what should happen), error messages/logs/screenshots, recent related changes or deployments, and scope of impact.
2. **Use Memory for Context** — Search memory for similar incidents/fixes before deep investigation: `npx ai-devkit@latest memory search --query "<issue symptoms or error>"`.
3. **Clarify Reality vs Expectation** — Restate observed vs expected behavior. Confirm relevant requirements or docs that define the expectation. Define acceptance criteria for the fix.
4. **Reproduce & Isolate** — Determine reproducibility (always, intermittent, environment-specific). Capture reproduction steps. List suspected components or modules.
5. **Analyze Potential Causes** — Brainstorm root causes (data, config, code regressions, external dependencies). Gather supporting evidence (logs, metrics, traces). Highlight unknowns needing investigation.
6. **Resolve** — Present resolution options (quick fix, refactor, rollback, etc.) with pros/cons and risks. Ask which option to pursue. Summarize chosen approach, pre-work, success criteria, and validation steps.
7. **Store Reusable Knowledge** — Save root-cause and fix patterns via `npx ai-devkit@latest memory store ...`.
8. **Next Command Guidance** — After selecting a fix path, continue with `/execute-plan`; when implemented, use `/check-implementation` and `/writing-test`.

```

### File: execute-plan.md
```md
---
description: Execute a feature plan task by task.
---

Help me work through a feature plan one task at a time.

1. **Gather Context** — If not already provided, ask for: feature name (kebab-case, e.g., `user-authentication`), brief feature/branch description, planning doc path (default `docs/ai/planning/feature-{name}.md`), and any supporting docs (design, requirements, implementation).
2. **Use Memory for Context** — Search for prior implementation notes/patterns before starting: `npx ai-devkit@latest memory search --query "<feature implementation plan>"`.
3. **Load & Present Plan** — Read the planning doc and parse task lists (headings + checkboxes). Present an ordered task queue grouped by section, with status: `todo`, `in-progress`, `done`, `blocked`.
4. **Interactive Task Execution** — For each task in order: display context and full bullet text, reference relevant design/requirements docs, offer to outline sub-steps before starting, prompt for status update (`done`, `in-progress`, `blocked`, `skipped`) with short notes after work, and if blocked record blocker and move to a "Blocked" list.
5. **Update Planning Doc** — After each completed or status-changed task, run `/update-planning` to keep `docs/ai/planning/feature-{name}.md` accurate.
6. **Store Reusable Knowledge** — Save reusable implementation guidance/decisions with `npx ai-devkit@latest memory store ...`.
7. **Session Summary** — Produce a summary: Completed, In Progress (with next steps), Blocked (with blockers), Skipped/Deferred, and New Tasks.
8. **Next Command Guidance** — Continue `/execute-plan` until plan completion; then run `/check-implementation`.

```

### File: new-requirement.md
```md
---
description: Scaffold feature documentation from requirements through planning.
---

Guide me through adding a new feature, from requirements documentation to implementation readiness.

1. **Capture Requirement** — If not already provided, ask for: feature name (kebab-case, e.g., `user-authentication`), what problem it solves and who will use it, and key user stories.
2. **Use Memory for Context** — Before asking repetitive clarification questions, search memory for related decisions or conventions via `npx ai-devkit@latest memory search --query "<feature/topic>"` and reuse relevant context.
3. **Create Feature Documentation Structure** — Copy each template's content (preserving YAML frontmatter and section headings) into feature-specific files:
   - `docs/ai/requirements/README.md` → `docs/ai/requirements/feature-{name}.md`
   - `docs/ai/design/README.md` → `docs/ai/design/feature-{name}.md`
   - `docs/ai/planning/README.md` → `docs/ai/planning/feature-{name}.md`
   - `docs/ai/implementation/README.md` → `docs/ai/implementation/feature-{name}.md`
   - `docs/ai/testing/README.md` → `docs/ai/testing/feature-{name}.md`
4. **Requirements Phase** — Fill out `docs/ai/requirements/feature-{name}.md`: problem statement, goals/non-goals, user stories, success criteria, constraints, open questions.
5. **Design Phase** — Fill out `docs/ai/design/feature-{name}.md`: architecture changes, data models, API/interfaces, components, design decisions, security and performance considerations.
6. **Planning Phase** — Fill out `docs/ai/planning/feature-{name}.md`: task breakdown with subtasks, dependencies, effort estimates, implementation order, risks.
7. **Store Reusable Knowledge** — When important conventions or decisions are finalized, store them via `npx ai-devkit@latest memory store --title "<title>" --content "<knowledge>" --tags "<tags>"`.
8. **Next Command Guidance** — Run `/review-requirements` first, then `/review-design`. If both pass, continue with `/execute-plan`.

```

### File: remember.md
```md
---
description: Store reusable guidance in the knowledge memory service.
---

Help me store it in the knowledge memory service.

1. **Capture Knowledge** — If not already provided, ask for: a short explicit title (5-12 words), detailed content (markdown, examples encouraged), optional tags (keywords like "api", "testing"), and optional scope (`global`, `project:<name>`, `repo:<name>`). If vague, ask follow-ups to make it specific and actionable.
2. **Search Before Store** — Check for existing similar entries first with `npx ai-devkit@latest memory search --query "<topic>"` to avoid duplicates.
3. **Validate Quality** — Ensure it is specific and reusable (not generic advice). Avoid storing secrets or sensitive data.
4. **Store** — Call `memory.storeKnowledge` with title, content, tags, scope. If MCP tools are unavailable, use `npx ai-devkit@latest memory store` instead.
5. **Confirm** — Summarize what was saved and offer to retrieve related memory entries when helpful.
6. **Next Command Guidance** — Continue with the current lifecycle phase command (`/execute-plan`, `/check-implementation`, `/writing-test`, etc.) as needed.

```

### File: review-design.md
```md
---
description: Review feature design for completeness.
---

Review the design documentation in `docs/ai/design/feature-{name}.md` (and the project-level README if relevant).

1. **Use Memory for Context** — Search memory for prior architecture constraints/patterns: `npx ai-devkit@latest memory search --query "<feature design architecture>"`.
2. Summarize:
   - Architecture overview (ensure mermaid diagram is present and accurate)
   - Key components and their responsibilities
   - Technology choices and rationale
   - Data models and relationships
   - API/interface contracts (inputs, outputs, auth)
   - Major design decisions and trade-offs
   - Non-functional requirements that must be preserved
3. **Clarify and explore (loop until converged)**:
   - **Ask clarification questions** for every gap, inconsistency, or misalignment between requirements and design. Do not just list issues — actively ask specific questions to resolve them.
   - **Brainstorm and explore options** — For key architecture decisions, trade-offs, or areas with multiple viable approaches, proactively brainstorm alternatives. Present options with pros/cons and trade-offs. Challenge assumptions and surface creative alternatives.
   - **Repeat** — Continue looping until the user is satisfied with the chosen approach and no open questions remain.
4. **Store Reusable Knowledge** — Persist approved design patterns/constraints with `npx ai-devkit@latest memory store ...` when they will help future work.
5. **Next Command Guidance** — If requirements gaps are found, return to `/review-requirements`; if design is sound, continue to `/execute-plan`.

```

### File: review-requirements.md
```md
---
description: Review feature requirements for completeness.
---

Review `docs/ai/requirements/feature-{name}.md` and the project-level template `docs/ai/requirements/README.md` to ensure structure and content alignment.

1. **Use Memory for Context** — Search memory for related requirements/domain decisions before starting: `npx ai-devkit@latest memory search --query "<feature requirements>"`.
2. Summarize:
   - Core problem statement and affected users
   - Goals, non-goals, and success criteria
   - Primary user stories & critical flows
   - Constraints, assumptions, open questions
   - Any missing sections or deviations from the template
3. **Clarify and explore (loop until converged)**:
   - **Ask clarification questions** for every gap, contradiction, or ambiguity. Do not just list issues — actively ask specific questions to resolve them.
   - **Brainstorm and explore options** — For key decisions, trade-offs, or areas with multiple viable approaches, proactively brainstorm alternatives. Present options with pros/cons and trade-offs. Challenge assumptions and surface creative alternatives.
   - **Repeat** — Continue looping until the user is satisfied with the chosen app
... [TRUNCATED]
```

### File: .cursor-plugin_DISTILLED.md
```md
---
id: .cursor-plugin
type: distilled_knowledge
---
# .cursor-plugin

## SWALLOW ENGINE DISTILLATION

### File: plugin.json
```json
{
  "name": "ai-devkit",
  "version": "0.21.1",
  "description": "AI-assisted development toolkit with structured SDLC workflows, persistent memory, and reusable skills",
  "author": {
    "name": "Hoang Nguyen",
    "email": "hoang@codeaholicguy.com"
  },
  "homepage": "https://ai-devkit.com",
  "repository": "https://github.com/codeaholicguy/ai-devkit",
  "license": "MIT",
  "keywords": [
    "ai",
    "development",
    "sdlc",
    "workflow",
    "memory",
    "skills",
    "testing",
    "code-review",
    "debugging"
  ],
  "commands": "./commands/",
  "skills": "./skills/"
}

```


```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
