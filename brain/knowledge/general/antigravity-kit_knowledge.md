---
id: antigravity-kit-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:47.348353
---

# KNOWLEDGE EXTRACT: antigravity-kit
> **Extracted on:** 2026-03-30 17:29:09
> **Source:** antigravity-kit

---

## File: `.editorconfig`
```
# EditorConfig helps maintain consistent coding styles
# https://editorconfig.org

root = true

[*]
indent_style = space
indent_size = 4
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.{json,yml,yaml}]
indent_size = 2

[*.md]
trim_trailing_whitespace = false

[Makefile]
indent_style = tab
```

## File: `.gitignore`
```
# Ignore
node_modules/
.temp_ag_kit/
antigravity-doc
tests
others
```

## File: `AGENT_FLOW.md`
```markdown
# 🔄 Agent Flow Architecture

> **Antigravity Kit** - Comprehensive AI Agent Workflow Documentation

---

## 📊 Overview Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER REQUEST                             │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    REQUEST CLASSIFICATION                        │
│  • Analyze intent (build, debug, test, deploy, etc.)           │
│  • Identify domain (frontend, backend, mobile, etc.)           │
│  • Detect complexity (simple, medium, complex)                  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                ┌────────────┴────────────┐
                │                         │
                ▼                         ▼
    ┌───────────────────┐      ┌──────────────────┐
    │ WORKFLOW COMMAND  │      │  DIRECT AGENT    │
    │  (Slash Command)  │      │  ASSIGNMENT      │
    └─────────┬─────────┘      └────────┬─────────┘
              │                         │
              ▼                         ▼
    ┌───────────────────┐      ┌──────────────────┐
    │ /brainstorm       │      │ Agent Selection  │
    │ /create           │      │ Based on Domain  │
    │ /debug            │      │                  │
    │ /deploy           │      │ • frontend-*     │
    │ /enhance          │      │ • backend-*      │
    │ /orchestrate      │      │ • mobile-*       │
    │ /plan             │      │ • database-*     │
    │ /preview          │      │ • devops-*       │
    │ /status           │      │ • test-*         │
    │ /test             │      │ • security-*     │
    │ /ui-ux-pro-max    │      │ • game-*         │
    └─────────┬─────────┘      └────────┬─────────┘
              │                         │
              └────────────┬────────────┘
                           │
                           ▼
         ┌─────────────────────────────────────┐
         │       AGENT INITIALIZATION          │
         │  • Load agent persona/role          │
         │  • Load required skills             │
         │  • Set behavioral mode              │
         └──────────────┬──────────────────────┘
                        │
                        ▼
         ┌─────────────────────────────────────┐
         │      SKILL LOADING PROTOCOL         │
         │                                      │
         │  1. Read SKILL.md metadata          │
         │  2. Load references/ (if needed)    │
         │  3. Execute scripts/ (if needed)    │
         │  4. Apply rules and patterns        │
         └──────────────┬──────────────────────┘
                        │
                        ▼
         ┌─────────────────────────────────────┐
         │         TASK EXECUTION              │
         │                                      │
         │  • Analyze codebase                 │
         │  • Apply best practices             │
         │  • Generate/modify code             │
         │  • Run validations                  │
         │  • Execute tests                    │
         └──────────────┬──────────────────────┘
                        │
                        ▼
         ┌─────────────────────────────────────┐
         │      VALIDATION LAYER               │
         │                                      │
         │  Quick Check (checklist.py):        │
         │  • Security scan                    │
         │  • Code quality (lint/types)        │
         │  • Schema validation                │
         │  • Test suite                       │
         │  • UX audit                         │
         │  • SEO check                        │
         │                                      │
         │  Full Check (verify_all.py):        │
         │  • All above + Lighthouse           │
         │  • E2E tests (Playwright)           │
         │  • Bundle analysis                  │
         │  • Mobile audit                     │
         │  • i18n check                       │
         └──────────────┬──────────────────────┘
                        │
                        ▼
         ┌─────────────────────────────────────┐
         │         RESULT DELIVERY             │
         │  • Present changes to user          │
         │  • Provide explanations             │
         │  • Suggest next steps               │
         └─────────────────────────────────────┘
```

---

## 🎯 Detailed Agent Workflow

### 1️⃣ **Request Entry Points**

```
User Input Types:
┌─────────────────────────────────────────────────────────────┐
│ A. Natural Language Request                                 │
│    "Build a React dashboard with charts"                    │
│                                                              │
│ B. Slash Command                                            │
│    "/create feature: user authentication"                   │
│                                                              │
│ C. Domain-Specific Request                                  │
│    "Optimize database queries" → database-architect         │
│    "Fix security vulnerability" → security-auditor          │
│    "Deploy to AWS" → devops-engineer                        │
└─────────────────────────────────────────────────────────────┘
```

#### Socratic Gate Protocol

Before implementation, verify:

- **New Feature** → ASK 3 strategic questions
- **Bug Fix** → Confirm understanding + ask impact
- **Vague request** → Ask Purpose, Users, Scope

### 2️⃣ **Agent Selection Matrix**

#### Agent Routing Checklist (Mandatory)

Before ANY code/design work:

| Step | Check                        | If Unchecked                             |
| ---- | ---------------------------- | ---------------------------------------- |
| 1    | Identify correct agent       | → Analyze request domain                 |
| 2    | Read agent's .md file        | → Open `.agent/agents/{agent}.md`        |
| 3    | Announce agent               | → `🤖 Applying knowledge of @[agent]...` |
| 4    | Load skills from frontmatter | → Check `skills:` field                  |

```
Request Domain → Agent Mapping:

┌──────────────────────┬─────────────────────┬──────────────────────────┐
│ Domain               │ Primary Agent       │ Skills Loaded            │
├──────────────────────┼─────────────────────┼──────────────────────────┤
│ UI/UX Design         │ frontend-specialist │ react-best-practices      │
│                      │                     │ frontend-design          │
│                      │                     │ tailwind-patterns        │
|                      │                     │ web-design-guidelines    │
│                      │                     │ frontend-design          │
├──────────────────────┼─────────────────────┼──────────────────────────┤
│ API Development      │ backend-specialist  │ api-patterns             │
│                      │                     │ nodejs-best-practices    │
│                      │                     │ nestjs-expert            │
├──────────────────────┼─────────────────────┼──────────────────────────┤
│ Database Design      │ database-architect  │ database-design          │
│                      │                     │ prisma-expert            │
├──────────────────────┼─────────────────────┼──────────────────────────┤
│ Mobile App           │ mobile-developer    │ mobile-design            │
├──────────────────────┼─────────────────────┼──────────────────────────┤
│ Game Development     │ game-developer      │ game-development         │
├──────────────────────┼─────────────────────┼──────────────────────────┤
│ DevOps/Deployment    │ devops-engineer     │ docker-expert            │
│                      │                     │ deployment-procedures    │
├──────────────────────┼─────────────────────┼──────────────────────────┤
│ Security Audit       │ security-auditor    │ vulnerability-scanner    │
├──────────────────────┼─────────────────────┼──────────────────────────┤
│ Penetration Testing  │ penetration-tester  │ red-team-tactics         │
├──────────────────────┼─────────────────────┼──────────────────────────┤
│ Testing              │ test-engineer       │ testing-patterns         │
│                      │                     │ webapp-testing           │
│                      │                     │ tdd-workflow             │
├──────────────────────┼─────────────────────┼──────────────────────────┤
│ Debugging            │ debugger            │ systematic-debugging     │
├──────────────────────┼─────────────────────┼──────────────────────────┤
│ Performance          │ performance-        │ performance-profiling    │
│                      │ optimizer           │                          │
├──────────────────────┼─────────────────────┼──────────────────────────┤
│ SEO                  │ seo-specialist      │ seo-fundamentals         │
│                      │                     │ geo-fundamentals         │
├──────────────────────┼─────────────────────┼──────────────────────────┤
│ Documentation        │ documentation-      │ documentation-templates  │
│                      │ writer              │                          │
├──────────────────────┼─────────────────────┼──────────────────────────┤
│ Planning/Discovery   │ project-planner     │ brainstorming            │
│                      │                     │ plan-writing             │
│                      │                     │ architecture             │
├──────────────────────┼─────────────────────┼──────────────────────────┤
│ Multi-Agent Tasks    │ orchestrator        │ parallel-agents          │
│                      │                     │ behavioral-modes         │
└──────────────────────┴─────────────────────┴──────────────────────────┘
```

### 3️⃣ **Skill Loading Protocol**

```
┌─────────────────────────────────────────────────────────────┐
│                    SKILL LOADING FLOW                        │
└─────────────────────────────────────────────────────────────┘

Step 1: Match Request to Skill
┌──────────────────────────────────────────┐
│ User: "Build a REST API"                 │
│   ↓                                       │
│ Keyword Match: "API" → api-patterns      │
└──────────────────────────────────────────┘
                    ↓
Step 2: Load Skill Metadata
┌──────────────────────────────────────────┐
│ Read: .agent/skills/api-patterns/        │
│       └── SKILL.md (main instructions)   │
└──────────────────────────────────────────┘
                    ↓
Step 3: Load References (if needed)
┌──────────────────────────────────────────┐
│ Read: api-patterns/rest.md               │
│       api-patterns/graphql.md            │
│       api-patterns/auth.md               │
│       api-patterns/documentation.md      │
└──────────────────────────────────────────┘
                    ↓
Step 4: Execute Scripts (if needed)
┌──────────────────────────────────────────┐
│ Run: scripts/api_validator.py            │
│      (validates API design)              │
└──────────────────────────────────────────┘
                    ↓
Step 5: Apply Knowledge
┌──────────────────────────────────────────┐
│ Agent now has:                           │
│ • API design patterns                    │
│ • Authentication strategies              │
│ • Documentation templates                │
│ • Validation scripts                     │
└──────────────────────────────────────────┘

### Related Skills Pattern

Skills now link to each other:
- `frontend-design` → `web-design-guidelines` (after coding)
- `web-design-guidelines` → `frontend-design` (before coding)

> **Note**: Scripts are NOT auto-executed. AI suggests running them, user approves.
```

### 4️⃣ **Workflow Command Execution**

```
Slash Command Flow:

/brainstorm
    ↓
    1. Load: brainstorming skill
    2. Apply: Socratic questioning
    3. Output: Structured discovery document

/create
    ↓
    1. Detect: Project type (web/mobile/api/game)
    2. Load: app-builder skill + domain-specific skills
    3. Select: Template from app-builder/templates/
    4. Scaffold: Generate project structure
    5. Validate: Run checklist.py

/debug
    ↓
    1. Load: systematic-debugging skill
    2. Analyze: Error logs, stack traces
    3. Apply: Root cause analysis
    4. Suggest: Fix with code examples
    5. Test: Verify fix works

/deploy
    ↓
    1. Load: deployment-procedures skill
    2. Detect: Platform (Vercel, AWS, Docker, etc.)
    3. Prepare: Build artifacts
    4. Execute: Deployment scripts
    5. Verify: Health checks
    6. Output: Deployment URL

/test
    ↓
    1. Load: testing-patterns + webapp-testing skills
    2. Detect: Test framework (Jest, Vitest, Playwright)
    3. Generate: Test cases
    4. Execute: Run tests
    5. Report: Coverage + results

/orchestrate
    ↓
    1. Load: parallel-agents skill
    2. Decompose: Task into subtasks
    3. Assign: Each subtask to specialist agent
    4. Coordinate: Parallel execution
    5. Merge: Combine results
    6. Validate: Run full verification

/plan
    ↓
    1. Load: plan-writing + architecture skills
    2. Analyze: Requirements
    3. Break down: Tasks with estimates
    4. Output: Structured plan with milestones

/ui-ux-pro-max
    ↓
    1. Load: ui-ux-pro-max skill
    2. Access: 50 design styles
    3. Access: 21 color palettes
    4. Access: 50 font combinations
    5. Generate: Professional UI with selected style
```

### 5️⃣ **Multi-Agent Orchestration**

```
Complex Task → /orchestrate → Multiple Specialist Personas

Example: "Build a full-stack e-commerce app"

┌─────────────────────────────────────────────────────────────┐
│                     ORCHESTRATOR AGENT                       │
│  Decomposes task into sequential workstreams                │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│ FRONTEND      │   │ BACKEND       │   │ DATABASE      │
│ SPECIALIST    │   │ SPECIALIST    │   │ ARCHITECT     │
│               │   │               │   │               │
│ Skills:       │   │ Skills:       │   │ Skills:       │
│ • react-*     │   │ • api-*       │   │ • database-*  │
│ • nextjs-*    │   │ • nodejs-*    │   │ • prisma-*    │
│ • tailwind-*  │   │ • nestjs-*    │   │               │
│               │   │               │   │               │
│ Builds:       │   │ Builds:       │   │ Builds:       │
│ • UI/UX       │   │ • REST API    │   │ • Schema      │
│ • Components  │   │ • Auth        │   │ • Migrations  │
│ • Pages       │   │ • Business    │   │ • Indexes     │
└───────┬───────┘   └───────┬───────┘   └───────┬───────┘
        │                   │                   │
        └─────────────────┬─┴───────────────────┘
                          │
                          ▼
        ┌─────────────────────────────────────┐
        │      CODE COHERENCE                 │
        │  • AI maintains consistency         │
        │  • Sequential context switching     │
        │  • Ensure API contracts match       │
        └──────────────┬──────────────────────┘
                       │
                       ▼
        ┌─────────────────────────────────────┐
        │    VALIDATION (All Agents)          │
        │  • test-engineer → Tests            │
        │  • security-auditor → Security      │
        │  • performance-optimizer → Perf     │
        └──────────────┬──────────────────────┘
                       │
                       ▼
        ┌─────────────────────────────────────┐
        │    DEPLOYMENT                       │
        │  • devops-engineer → Deploy         │
        └─────────────────────────────────────┘
```

### 6️⃣ **Validation & Quality Gates**

```
┌─────────────────────────────────────────────────────────────┐
│                 VALIDATION PIPELINE                          │
└─────────────────────────────────────────────────────────────┘

During Development (Quick Checks):
┌──────────────────────────────────────────┐
│ python .agent/scripts/checklist.py .     │
├──────────────────────────────────────────┤
│ ✓ Security Scan (vulnerabilities)        │
│ ✓ Code Quality (ESLint, TypeScript)      │
│ ✓ Schema Validation (Prisma/DB)          │
│ ✓ Test Suite (Unit tests)                │
│ ✓ UX Audit (Accessibility)               │
│ ✓ SEO Check (Meta tags, performance)     │
└──────────────────────────────────────────┘
        Time: ~30 seconds

Pre-Deployment (Full Verification):
┌──────────────────────────────────────────────────────┐
│ python .agent/scripts/verify_all.py .                │
│        --url http://localhost:3000                   │
├──────────────────────────────────────────────────────┤
│ ✓ All Quick Checks                                   │
│ ✓ Lighthouse Audit (Core Web Vitals)                 │
│ ✓ Playwright E2E Tests                               │
│ ✓ Bundle Analysis (Size, tree-shaking)               │
│ ✓ Mobile Audit (Responsive, touch targets)           │
│ ✓ i18n Check (Translations, locale)                  │
└──────────────────────────────────────────────────────┘
        Time: ~3-5 minutes
```

---

## 🧩 Skill-to-Script Mapping

```
Skills with Automated Scripts:

┌─────────────────────────┬──────────────────────────────────┐
│ Skill                   │ Script                           │
├─────────────────────────┼──────────────────────────────────┤
│ api-patterns            │ scripts/api_validator.py         │
│ database-design         │ scripts/schema_validator.py      │
│ frontend-design         │ scripts/accessibility_checker.py │
│                         │ scripts/ux_audit.py              │
│ geo-fundamentals        │ scripts/geo_checker.py           │
│ i18n-localization       │ scripts/i18n_checker.py          │
│ lint-and-validate       │ scripts/lint_runner.py           │
│                         │ scripts/type_coverage.py         │
│ mobile-design           │ scripts/mobile_audit.py          │
│ performance-profiling   │ scripts/lighthouse_runner.py     │
│                         │ scripts/bundle_analyzer.py       │
│ seo-fundamentals        │ scripts/seo_checker.py           │
│ testing-patterns        │ scripts/test_runner.py           │
│ vulnerability-scanner   │ scripts/security_scanner.py      │
│ webapp-testing          │ scripts/e2e_runner.py            │
└─────────────────────────┴──────────────────────────────────┘
```

---

## 🔄 Complete Request Lifecycle Example

```
User Request: "Build a Next.js dashboard with authentication"

1. REQUEST CLASSIFICATION
   ├─ Type: Build new feature
   ├─ Domain: Frontend + Backend
   ├─ Complexity: Medium-High
   └─ Suggested: /create or /orchestrate

2. WORKFLOW SELECTION
   └─ User chooses: /orchestrate (multi-agent approach)

3. ORCHESTRATOR DECOMPOSITION
   ├─ Frontend: Dashboard UI (React components)
   ├─ Backend: Auth API (JWT, session management)
   ├─ Database: User schema (Prisma)
   └─ Testing: E2E auth flow

4. AGENT ASSIGNMENT
   ├─ frontend-specialist
   │   └─ Skills: react-best-practices, tailwind-patterns, frontend-design
   ├─ backend-specialist
   │   └─ Skills: api-patterns, nodejs-best-practices
   ├─ database-architect
   │   └─ Skills: database-design, prisma-expert
   └─ test-engineer
       └─ Skills: testing-patterns, webapp-testing

5. SEQUENTIAL MULTI-DOMAIN EXECUTION
   Note: AI processes each domain sequentially, switching context between specialist "personas."
   This is NOT true parallel execution but simulated multi-agent behavior.

   ├─ Frontend builds:
   │   ├─ app/dashboard/page.tsx (Server Component)
   │   ├─ components/DashboardLayout.tsx
   │   ├─ components/LoginForm.tsx
   │   └─ lib/auth-client.ts
   ├─ Backend builds:
   │   ├─ app/api/auth/login/route.ts
   │   ├─ app/api/auth/logout/route.ts
   │   ├─ lib/jwt.ts
   │   └─ middleware.ts
   ├─ Database builds:
   │   ├─ prisma/schema.prisma (User, Session models)
   │   └─ prisma/migrations/
   └─ Testing builds:
       ├─ tests/auth.spec.ts (Playwright)
       └─ tests/dashboard.spec.ts

6. CODE INTEGRATION
   Reality Note: AI writes code as a continuous stream, maintaining consistency.
   There is no "merge" step - it's all generated coherently from the start.

   └─ AI maintains coherence across domains
       ├─ Resolves import paths
       ├─ Ensures type safety
       └─ Connects API routes to UI

7. VALIDATION
   ├─ checklist.py
   │   ✓ Security: No leaked secrets
   │   ✓ Lint: No ESLint errors
   │   ✓ Types: TypeScript passes
   │   ✓ Tests: Auth flow passes
   └─ verify_all.py
       ✓ E2E: Login → Dashboard → Logout works
       ✓ Accessibility: WCAG AA compliant
       ✓ Performance: Lighthouse score > 90

8. RESULT DELIVERY
   └─ User receives:
       ├─ Complete codebase
       ├─ Documentation (how to run)
       ├─ Test reports
       └─ Deployment instructions
```

---

## 📈 Statistics & Metrics

```
┌──────────────────────────────────────────────────────────┐
│                    SYSTEM CAPABILITIES                    │
├──────────────────────────────────────────────────────────┤
│ Total Agents:              20                            │
│ Total Skills:              36                            │
│ Total Workflows:           11                            │
│ Master Scripts:            2 (checklist, verify_all)     │
│ Skill-Level Scripts:       18                            │
│ Coverage:                  ~90% web/mobile development   │
│                                                          │
│ Supported Frameworks:                                    │
│ ├─ Frontend: React, Next.js, Vue, Nuxt, Astro          │
│ ├─ Backend: Node.js, NestJS, FastAPI, Express          │
│ ├─ Mobile: React Native, Flutter                        │
│ ├─ Database: Prisma, TypeORM, Sequelize                │
│ ├─ Testing: Jest, Vitest, Playwright, Cypress          │
│ └─ DevOps: Docker, Vercel, AWS, GitHub Actions         │
└──────────────────────────────────────────────────────────┘
```

---

## 🎓 Best Practices

### When to Use Each Workflow

```
/brainstorm
  ✓ Unclear requirements
  ✓ Need to explore options
  ✓ Complex problem needs breaking down

/create
  ✓ New feature in existing project
  ✓ Small-to-medium complexity
  ✓ Single domain (frontend OR backend)

/orchestrate
  ✓ Full-stack features
  ✓ Complex multi-step tasks
  ✓ Need multiple specialist agents

/debug
  ✓ Bug reports
  ✓ Unexpected behavior
  ✓ Performance issues

/test
  ✓ Need test coverage
  ✓ Before deployment
  ✓ After major changes

/deploy
  ✓ Ready to ship
  ✓ After all tests pass
  ✓ Need production URL

/plan
  ✓ Large projects
  ✓ Need time estimates
  ✓ Team coordination needed
```

---

## 🔗 Quick Reference Links

- **Architecture**: `.agent/ARCHITECTURE.md`
- **Agents**: `.agent/agents/`
- **Skills**: `.agent/skills/`
- **Workflows**: `.agent/workflows/`
- **Scripts**: `.agent/scripts/`

---

**Last Updated**: 2026-01-26
**Version**: 2.0.1
```

## File: `captain-definition`
```
{
  "schemaVersion": 2,
  "dockerfilePath": "./web/Dockerfile",
  "containerHttpPort": 3000
}
```

## File: `CHANGELOG.md`
```markdown
# Changelog

All notable changes to the Antigravity Kit will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/2.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]


## [2.0.2] - 2026-02-04
- **New Skills**:
    - `rust-pro` - Master Rust 1.75+ 
- **Agent Workflows**:
    - Updated `orchestrate.md` fix output turkish


## [2.0.1] - 2026-01-26

### Added

- **Agent Flow Documentation**: New comprehensive workflow documentation
    - Added `.agent/AGENT_FLOW.md` - Complete agent flow architecture guide
    - Documented Agent Routing Checklist (mandatory steps before code/design work)
    - Documented Socratic Gate Protocol for requirement clarification
    - Added Cross-Skill References pattern documentation
- **New Skills**:
    - `react-best-practices` - Consolidated Next.js and React expertise
    - `web-design-guidelines` - Professional web design standards and patterns

### Changed

- **Skill Consolidation**: Merged `nextjs-best-practices` and `react-patterns` into unified `react-best-practices` skill
- **Architecture Updates**:
    - Enhanced `.agent/ARCHITECTURE.md` with improved flow diagrams
    - Updated `.agent/rules/GEMINI.md` with Agent Routing Checklist
- **Agent Updates**:
    - Updated `frontend-specialist.md` with new skill references
    - Updated `qa-automation-engineer.md` with enhanced testing workflows
- **Frontend Design Skill**: Enhanced `frontend-design/SKILL.md` with cross-references to `web-design-guidelines`

### Removed

- Deprecated `nextjs-best-practices` skill (consolidated into `react-best-practices`)
- Deprecated `react-patterns` skill (consolidated into `react-best-practices`)

### Fixed

- **Agent Flow Accuracy**: Corrected misleading terminology in AGENT_FLOW.md
    - Changed "Parallel Execution" → "Sequential Multi-Domain Execution"
    - Changed "Integration Layer" → "Code Coherence" with accurate description
    - Added reality notes about AI's sequential processing vs. simulated multi-agent behavior
    - Clarified that scripts require user approval (not auto-executed)

## [2.0.0] - Unreleased

### Initial Release

- Initial release of Antigravity Kit
- 20 specialized AI agents
- 37 domain-specific skills
- 11 workflow slash commands
- CLI tool for easy installation and updates
- Comprehensive documentation and architecture guide

[Unreleased]: https://github.com/vudovn/antigravity-kit/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/vudovn/antigravity-kit/releases/tag/v2.0.0
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 VUDOVN

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `package.json`
```json
{
  "name": "antigravity-kit",
  "version": "2.0.0",
  "description": "AI Agent templates - Skills, Agents, and Workflows for enhanced coding assistance",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/vudovn/antigravity-kit.git"
  },
  "homepage": "https://github.com/vudovn/antigravity-kit#readme",
  "bugs": {
    "url": "https://github.com/vudovn/antigravity-kit/issues"
  },
  "keywords": [
    "antigravity",
    "ai",
    "agent",
    "gemini",
    "skills",
    "templates"
  ],
  "author": "vudovn",
  "license": "MIT"
}
```

## File: `README.md`
```markdown
# Antigravity Kit

> AI Agent templates with Skills, Agents, and Workflows

<div  align="center">
    <a href="https://unikorn.vn/p/antigravity-kit?ref=unikorn" target="_blank"><img src="https://unikorn.vn/api/widgets/badge/antigravity-kit?theme=dark" alt="Antigravity Kit - Nổi bật trên Unikorn.vn" style="width: 210px; height: 54px;" width="210" height="54" /></a>
    <a href="https://unikorn.vn/p/antigravity-kit?ref=unikorn" target="_blank"><img src="https://unikorn.vn/api/widgets/badge/antigravity-kit/rank?theme=dark&type=daily" alt="Antigravity Kit - Hàng ngày" style="width: 250px; height: 64px;" width="250" height="64" /></a>
    <a href="https://launch.j2team.dev/products/antigravity-kit" target="_blank"><img src="https://launch.j2team.dev/badge/antigravity-kit/dark" alt="Antigravity Kit on J2TEAM Launch" width="250" height="54" /></a>
</div>

## Quick Install

```bash
npx @vudovn/ag-kit init
```

Or install globally:

```bash
npm install -g @vudovn/ag-kit
ag-kit init
```

This installs the `.agent` folder containing all templates into your project.

### ⚠️ Important Note on `.gitignore`
If you are using AI-powered editors like **Cursor** or **Windsurf**, adding the `.agent/` folder to your `.gitignore` may prevent the IDE from indexing the workflows. This results in slash commands (like `/plan`, `/debug`) not appearing in the chat suggestion dropdown.

**Recommended Solution:**
To keep the `.agent/` folder local (not tracked by Git) while maintaining AI functionality:
1. Ensure `.agent/` is **NOT** in your project's `.gitignore`.
2. Instead, add it to your local exclude file: `.git/info/exclude`

## What's Included

| Component     | Count | Description                                                        |
| ------------- | ----- | ------------------------------------------------------------------ |
| **Agents**    | 20    | Specialist AI personas (frontend, backend, security, PM, QA, etc.) |
| **Skills**    | 37    | Domain-specific knowledge modules                                  |
| **Workflows** | 11    | Slash command procedures                                           |


## Usage

### Using Agents

**No need to mention agents explicitly!** The system automatically detects and applies the right specialist(s):

```
You: "Add JWT authentication"
AI: 🤖 Applying @security-auditor + @backend-specialist...

You: "Fix the dark mode button"
AI: 🤖 Using @frontend-specialist...

You: "Login returns 500 error"
AI: 🤖 Using @debugger for systematic analysis...
```

**How it works:**

- Analyzes your request silently

- Detects domain(s) automatically (frontend, backend, security, etc.)
- Selects the best specialist(s)
- Informs you which expertise is being applied
- You get specialist-level responses without needing to know the system architecture

**Benefits:**

- ✅ Zero learning curve - just describe what you need
- ✅ Always get expert responses
- ✅ Transparent - shows which agent is being used
- ✅ Can still override by mentioning agent explicitly

### Using Workflows

Invoke workflows with slash commands:

| Command          | Description                           |
| ---------------- | ------------------------------------- |
| `/brainstorm`    | Explore options before implementation |
| `/create`        | Create new features or apps           |
| `/debug`         | Systematic debugging                  |
| `/deploy`        | Deploy application                    |
| `/enhance`       | Improve existing code                 |
| `/orchestrate`   | Multi-agent coordination              |
| `/plan`          | Create task breakdown                 |
| `/preview`       | Preview changes locally               |
| `/status`        | Check project status                  |
| `/test`          | Generate and run tests                |
| `/ui-ux-pro-max` | Design with 50 styles                 |

Example:

```
/brainstorm authentication system
/create landing page with hero section
/debug why login fails
```

### Using Skills

Skills are loaded automatically based on task context. The AI reads skill descriptions and applies relevant knowledge.

## CLI Tool

| Command         | Description                               |
| --------------- | ----------------------------------------- |
| `ag-kit init`   | Install `.agent` folder into your project |
| `ag-kit update` | Update to the latest version              |
| `ag-kit status` | Check installation status                 |

### Options

```bash
ag-kit init --force        # Overwrite existing .agent folder
ag-kit init --path ./myapp # Install in specific directory
ag-kit init --branch dev   # Use specific branch
ag-kit init --quiet        # Suppress output (for CI/CD)
ag-kit init --dry-run      # Preview actions without executing
```

## Documentation

- **[Web App Example](https://antigravity-kit.unikorn.vn/brain/knowledge/docs_legacy/guide/examples/brainstorm)** - Step-by-step guide to creating a web application
- **[Online Docs](https://antigravity-kit.unikorn.vn/docs)** - Browse all documentation online

## Buy me coffee

<p align="center">
  <a href="https://buymeacoffee.com/vudovn">
    <img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me a Coffee" />
  </a>
</p>

<p align="center"> - or - </p>

<p align="center">
  <img src="https://img.vietqr.io/image/mbbank-0779440918-compact.jpg" alt="Buy me coffee" width="200" />
</p>

## License

MIT © Vudovn
```

## File: `_VET_REPORT.md`
```markdown
﻿# Strix Vet Report: antigravity-kit
**Date:** 2026-03-17 09:30:35
**Status:** WARN
**Critical Findings:** 0
**Warnings:** 8

## Verdict

WARN - Warnings found. Manual review required before ingestion. See findings below.

## Findings

| Level | Category | Detail | File |
|-------|----------|--------|------|
| PASS | GIT_HOOK | No active hooks found | `` |
| WARN | SENSITIVE_ACCESS | .env file access | `D:\Project\QUARANTINE\antigravity-kit\.agent\skills\vulnerability-scanner\scripts\security_scan.py` |
| WARN | OBFUSCATION | subprocess shell execution | `D:\Project\QUARANTINE\antigravity-kit\.agent\scripts\auto_preview.py` |
| WARN | OBFUSCATION | subprocess shell execution | `D:\Project\QUARANTINE\antigravity-kit\.agent\scripts\checklist.py` |
| WARN | OBFUSCATION | subprocess shell execution | `D:\Project\QUARANTINE\antigravity-kit\.agent\scripts\verify_all.py` |
| WARN | OBFUSCATION | subprocess shell execution | `D:\Project\QUARANTINE\antigravity-kit\.agent\skills\lint-and-validate\scripts\lint_runner.py` |
| WARN | OBFUSCATION | subprocess shell execution | `D:\Project\QUARANTINE\antigravity-kit\.agent\skills\performance-profiling\scripts\lighthouse_audit.py` |
| WARN | OBFUSCATION | subprocess shell execution | `D:\Project\QUARANTINE\antigravity-kit\.agent\skills\testing-patterns\scripts\test_runner.py` |
| WARN | OBFUSCATION | eval dynamic execution | `D:\Project\QUARANTINE\antigravity-kit\.agent\skills\vulnerability-scanner\scripts\security_scan.py` |


## Next Step

Review each WARN item manually. If comfortable, proceed with caution. Document your review decision.
```

## File: `web/.dockerignore`
```
node_modules
.next
.git
.gitignore
README.md
*.md
.env*.local
```

## File: `web/.gitignore`
```
# See https://help.github.com/articles/ignoring-files/ for more about ignoring files.

# dependencies
/node_modules
/.pnp
.pnp.*
.yarn/*
!.yarn/patches
!.yarn/plugins
!.yarn/releases
!.yarn/versions

# testing
/coverage

# next.js
/.next/
/out/

# production
/build

# misc
.DS_Store
*.pem

# debug
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.pnpm-debug.log*

# env files (can opt-in for committing if needed)
.env*

# vercel
.vercel

# typescript
*.tsbuildinfo
next-env.d.ts

.agent
```

## File: `web/components.json`
```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "new-york",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "",
    "css": "src/app/globals.css",
    "baseColor": "neutral",
    "cssVariables": true,
    "prefix": ""
  },
  "iconLibrary": "lucide",
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui",
    "lib": "@/lib",
    "hooks": "@/hooks"
  },
  "registries": {
    "@coss": "https://coss.com/ui/r/{name}.json"
  }
}
```

## File: `web/Dockerfile`
```
FROM node:22-alpine AS base

# --- Dependencies ---
FROM base AS deps
RUN apk add --no-cache libc6-compat
WORKDIR /app
COPY web/package.json web/package-lock.json ./
RUN npm ci

# --- Build ---
FROM base AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY web/ ./
RUN npm run build

# --- Production ---
FROM base AS runner
WORKDIR /app

ENV NODE_ENV=production
ENV NEXT_TELEMETRY_DISABLED=1

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs

EXPOSE 3000
ENV PORT=3000
ENV HOSTNAME="0.0.0.0"

CMD ["node", "server.js"]
```

## File: `web/eslint.config.mjs`
```
import { defineConfig, globalIgnores } from "eslint/config";
import nextVitals from "eslint-config-next/core-web-vitals";
import nextTs from "eslint-config-next/typescript";

const eslintConfig = defineConfig([
  ...nextVitals,
  ...nextTs,
  // Override default ignores of eslint-config-next.
  globalIgnores([
    // Default ignores of eslint-config-next:
    ".next/**",
    "out/**",
    "build/**",
    "next-env.d.ts",
  ]),
]);

export default eslintConfig;
```

## File: `web/next.config.ts`
```typescript
import type { NextConfig } from "next";
import createMDX from "@next/mdx";

const nextConfig: NextConfig = {
  output: "standalone",
  pageExtensions: ["js", "jsx", "md", "mdx", "ts", "tsx"],
  reactCompiler: true,
};

const withMDX = createMDX({});

export default withMDX(nextConfig);
```

## File: `web/package.json`
```json
{
  "name": "web",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "eslint"
  },
  "dependencies": {
    "@base-ui/react": "^1.1.0",
    "@mdx-js/loader": "^3.1.1",
    "@mdx-js/react": "^3.1.1",
    "@next/mdx": "^16.1.6",
    "@types/mdx": "^2.0.13",
    "class-variance-authority": "^0.7.1",
    "lucide-react": "^0.562.0",
    "next": "16.1.3",
    "next-themes": "^0.4.6",
    "react": "19.2.3",
    "react-dom": "19.2.3",
    "tailwind-merge": "^3.4.0",
    "tw-animate-css": "^1.4.0",
    "typewriter-effect": "^2.22.0"
  },
  "devDependencies": {
    "@tailwindcss/postcss": "^4",
    "@types/node": "^20",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "babel-plugin-react-compiler": "1.0.0",
    "eslint": "^9",
    "eslint-config-next": "16.1.3",
    "gray-matter": "^4.0.3",
    "rehype-autolink-headings": "^7.1.0",
    "rehype-pretty-code": "^0.14.1",
    "rehype-slug": "^6.0.0",
    "remark-gfm": "^4.0.1",
    "shiki": "^3.22.0",
    "tailwindcss": "^4",
    "typescript": "^5"
  }
}
```

## File: `web/postcss.config.mjs`
```
const config = {
  plugins: {
    "@tailwindcss/postcss": {},
  },
};

export default config;
```

## File: `web/README.md`
```markdown
# Antigravity Kit

> AI Agent templates with Skills, Agents, and Workflows

<div  align="center">
    <a href="https://unikorn.vn/p/antigravity-kit?ref=unikorn" target="_blank"><img src="https://unikorn.vn/api/widgets/badge/antigravity-kit?theme=dark" alt="Antigravity Kit - Nổi bật trên Unikorn.vn" style="width: 210px; height: 54px;" width="210" height="54" /></a>
    <a href="https://unikorn.vn/p/antigravity-kit?ref=unikorn" target="_blank"><img src="https://unikorn.vn/api/widgets/badge/antigravity-kit/rank?theme=dark&type=daily" alt="Antigravity Kit - Hàng ngày" style="width: 250px; height: 64px;" width="250" height="64" /></a>
    <a href="https://launch.j2team.dev/products/antigravity-kit" target="_blank"><img src="https://launch.j2team.dev/badge/antigravity-kit/dark" alt="Antigravity Kit on J2TEAM Launch" width="250" height="54" /></a>
</div>

## Quick Install

```bash
npx @vudovn/ag-kit init
```

Or install globally:

```bash
npm install -g @vudovn/ag-kit
ag-kit init
```

This installs the `.agent` folder containing all templates into your project.

## Usage

### Using Agents

**No need to mention agents explicitly!** The system automatically detects and applies the right specialist(s):

```
You: "Add JWT authentication"
AI: 🤖 Applying @security-auditor + @backend-specialist...

You: "Fix the dark mode button"
AI: 🤖 Using @frontend-specialist...

You: "Login returns 500 error"
AI: 🤖 Using @debugger for systematic analysis...
```

**How it works:**

- Analyzes your request silently
- Detects domain(s) automatically (frontend, backend, security, etc.)
- Selects the best specialist(s)
- Informs you which expertise is being applied
- You get specialist-level responses without needing to know the system architecture

**Benefits:**

- ✅ Zero learning curve - just describe what you need
- ✅ Always get expert responses
- ✅ Transparent - shows which agent is being used
- ✅ Can still override by mentioning agent explicitly

### Using Workflows

Invoke workflows with slash commands:

| Command          | Description                           |
| ---------------- | ------------------------------------- |
| `/brainstorm`    | Explore options before implementation |
| `/create`        | Create new features or apps           |
| `/debug`         | Systematic debugging                  |
| `/deploy`        | Deploy application                    |
| `/enhance`       | Improve existing code                 |
| `/orchestrate`   | Multi-agent coordination              |
| `/plan`          | Create task breakdown                 |
| `/preview`       | Preview changes locally               |
| `/status`        | Check project status                  |
| `/test`          | Generate and run tests                |
| `/ui-ux-pro-max` | Design with 50 styles                 |

Example:

```
/brainstorm authentication system
/create landing page with hero section
/debug why login fails
```

### Using Skills

Skills are loaded automatically based on task context. The AI reads skill descriptions and applies relevant knowledge.

## CLI Tool

| Command         | Description                               |
| --------------- | ----------------------------------------- |
| `ag-kit init`   | Install `.agent` folder into your project |
| `ag-kit update` | Update to the latest version              |
| `ag-kit status` | Check installation status                 |

### Options

```bash
ag-kit init --force        # Overwrite existing .agent folder
ag-kit init --path ./myapp # Install in specific directory
ag-kit init --branch dev   # Use specific branch
ag-kit init --quiet        # Suppress output (for CI/CD)
ag-kit init --dry-run      # Preview actions without executing
```

## Documentation

- **[Web App Example](https://antigravity-kit.vercel.app//brain/knowledge/docs_legacy/guide/examples/web-app)** - Step-by-step guide to creating a web application
- **[Online Docs](https://antigravity-kit.vercel.app//docs)** - Browse all documentation online

## Buy me coffee

<p align="center">
  <a href="https://buymeacoffee.com/vudovn">
    <img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me a Coffee" />
  </a>
</p>

<p align="center"> - or - </p>

<p align="center">
  <img src="https://img.vietqr.io/image/mbbank-0779440918-compact.jpg" alt="Buy me coffee" width="200" />
</p>

## License

MIT © Vudovn
```

## File: `web/tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2017",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "react-jsx",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": [
    "next-env.d.ts",
    "**/*.ts",
    "**/*.tsx",
    ".next/types/**/*.ts",
    ".next/dev/types/**/*.ts",
    "**/*.mts"
  ],
  "exclude": ["node_modules"]
}
```

## File: `web/src/mdx-components.tsx`
```tsx
import type { MDXComponents } from "mdx/types";
import Link from "next/link";

export function useMDXComponents(components: MDXComponents): MDXComponents {
  return {
    h1: ({ children }) => (
      <h1 className="text-4xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-2">
        {children}
      </h1>
    ),
    h2: ({ children }) => (
      <h2 className="text-2xl font-semibold text-zinc-900 dark:text-zinc-50 mb-4 mt-8">
        {children}
      </h2>
    ),
    h3: ({ children }) => (
      <h3 className="text-xl font-semibold text-zinc-900 dark:text-zinc-50 mb-3 mt-6">
        {children}
      </h3>
    ),
    h4: ({ children }) => (
      <h4 className="text-lg font-semibold text-zinc-900 dark:text-zinc-50 mb-2 mt-4">
        {children}
      </h4>
    ),
    p: ({ children }) => (
      <p className="text-zinc-700 dark:text-zinc-300 mb-4">{children}</p>
    ),
    a: ({ href, children }) => {
      const isExternal = href?.startsWith("http");
      if (isExternal) {
        return (
          <a
            href={href}
            target="_blank"
            rel="noopener noreferrer"
            className="text-blue-600 dark:text-blue-400 hover:underline"
          >
            {children}
          </a>
        );
      }
      return (
        <Link
          href={href || "#"}
          className="text-blue-600 dark:text-blue-400 hover:underline"
        >
          {children}
        </Link>
      );
    },
    ul: ({ children }) => (
      <ul className="list-disc list-inside text-zinc-700 dark:text-zinc-300 space-y-2 mb-4">
        {children}
      </ul>
    ),
    ol: ({ children }) => (
      <ol className="list-decimal list-inside text-zinc-700 dark:text-zinc-300 space-y-2 mb-4">
        {children}
      </ol>
    ),
    li: ({ children }) => <li>{children}</li>,
    code: ({ children }) => (
      <code className="px-1.5 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-sm font-mono text-zinc-900 dark:text-zinc-100">
        {children}
      </code>
    ),
    pre: ({ children }) => (
      <pre className="p-4 rounded-lg bg-zinc-950 overflow-x-auto mb-4 text-sm">
        {children}
      </pre>
    ),
    blockquote: ({ children }) => (
      <blockquote className="border-l-4 border-zinc-300 dark:border-zinc-700 pl-4 italic text-zinc-600 dark:text-zinc-400 mb-4">
        {children}
      </blockquote>
    ),
    hr: () => <hr className="border-zinc-200 dark:border-zinc-800 my-8" />,
    table: ({ children }) => (
      <div className="overflow-x-auto mb-4">
        <table className="min-w-full divide-y divide-zinc-200 dark:divide-zinc-800">
          {children}
        </table>
      </div>
    ),
    th: ({ children }) => (
      <th className="px-4 py-2 text-left text-sm font-semibold text-zinc-900 dark:text-zinc-50 bg-zinc-50 dark:bg-zinc-900">
        {children}
      </th>
    ),
    td: ({ children }) => (
      <td className="px-4 py-2 text-sm text-zinc-700 dark:text-zinc-300 border-t border-zinc-200 dark:border-zinc-800">
        {children}
      </td>
    ),
    ...components,
  };
}
```

## File: `web/src/app/globals.css`
```css
@import "tailwindcss";
@import "tw-animate-css";

@custom-variant dark (&:is(.dark *));

:root {
  --background: var(--color-white);
  --foreground: var(--color-neutral-800);
  --accent: --alpha(var(--color-black) / 4%);
  --accent-foreground: var(--color-neutral-800);
  --border: --alpha(var(--color-black) / 8%);
  --card: var(--color-white);
  --card-foreground: var(--color-neutral-800);
  --destructive: var(--color-red-500);
  --destructive-foreground: var(--color-red-700);
  --info: var(--color-blue-500);
  --info-foreground: var(--color-blue-700);
  --input: --alpha(var(--color-black) / 10%);
  --muted: --alpha(var(--color-black) / 4%);
  --muted-foreground: color-mix(in srgb, var(--color-neutral-500) 90%, var(--color-black));
  --popover: var(--color-white);
  --popover-foreground: var(--color-neutral-800);
  --primary: var(--color-neutral-800);
  --primary-foreground: var(--color-neutral-50);
  --ring: var(--color-neutral-400);
  --secondary: --alpha(var(--color-black) / 4%);
  --secondary-foreground: var(--color-neutral-800);
  --success: var(--color-emerald-500);
  --success-foreground: var(--color-emerald-700);
  --warning: var(--color-amber-500);
  --warning-foreground: var(--color-amber-700);
}

@theme inline {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --font-sans: var(--font-geist-sans);
  --font-mono: var(--font-geist-mono);
  --animate-skeleton: skeleton 2s -1s infinite linear;
  --color-warning-foreground: var(--warning-foreground);
  --color-warning: var(--warning);
  --color-success-foreground: var(--success-foreground);
  --color-success: var(--success);
  --color-secondary-foreground: var(--secondary-foreground);
  --color-secondary: var(--secondary);
  --color-ring: var(--ring);
  --color-primary-foreground: var(--primary-foreground);
  --color-primary: var(--primary);
  --color-popover-foreground: var(--popover-foreground);
  --color-popover: var(--popover);
  --color-muted-foreground: var(--muted-foreground);
  --color-muted: var(--muted);
  --color-input: var(--input);
  --color-info-foreground: var(--info-foreground);
  --color-info: var(--info);
  --color-destructive-foreground: var(--destructive-foreground);
  --color-destructive: var(--destructive);
  --color-card-foreground: var(--card-foreground);
  --color-card: var(--card);
  --color-border: var(--border);
  --color-accent-foreground: var(--accent-foreground);
  --color-accent: var(--accent);

  @keyframes skeleton {
    to {
      background-position: -200% 0;
    }
  }
}

@media (prefers-color-scheme: dark) {
  :root {
    --background: #0a0a0a;
    --foreground: #ededed;
  }
}

body {
  background: var(--background);
  color: var(--foreground);
  font-family: Arial, Helvetica, sans-serif;
}

.dark {
  --accent: --alpha(var(--color-white) / 4%);
  --accent-foreground: var(--color-neutral-100);
  --background: color-mix(in srgb, var(--color-neutral-950) 95%, var(--color-white));
  --border: --alpha(var(--color-white) / 6%);
  --card: color-mix(in srgb, var(--background) 98%, var(--color-white));
  --card-foreground: var(--color-neutral-100);
  --destructive: color-mix(in srgb, var(--color-red-500) 90%, var(--color-white));
  --destructive-foreground: var(--color-red-400);
  --foreground: var(--color-neutral-100);
  --info: var(--color-blue-500);
  --info-foreground: var(--color-blue-400);
  --input: --alpha(var(--color-white) / 8%);
  --muted: --alpha(var(--color-white) / 4%);
  --muted-foreground: color-mix(in srgb, var(--color-neutral-500) 90%, var(--color-white));
  --popover: color-mix(in srgb, var(--background) 98%, var(--color-white));
  --popover-foreground: var(--color-neutral-100);
  --primary: var(--color-neutral-100);
  --primary-foreground: var(--color-neutral-800);
  --ring: var(--color-neutral-500);
  --secondary: --alpha(var(--color-white) / 4%);
  --secondary-foreground: var(--color-neutral-100);
  --success: var(--color-emerald-500);
  --success-foreground: var(--color-emerald-400);
  --warning: var(--color-amber-500);
  --warning-foreground: var(--color-amber-400);
}

@layer base {
  * {
    @apply border-border outline-ring/50;
  }

  body {
    @apply bg-background text-foreground;
  }
}
```

## File: `web/src/app/layout.tsx`
```tsx
import type { Metadata, Viewport } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import { ThemeProvider } from "@/components/theme-provider"

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const viewport: Viewport = {
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "white" },
    { media: "(prefers-color-scheme: dark)", color: "black" },
  ],
  width: "device-width",
  initialScale: 1,
};

export const metadata: Metadata = {
  title: "Antigravity Kit - AI Agent Capability Expansion Toolkit",
  description: "A comprehensive collection of skills, rules, and workflows to supercharge AI coding assistants for Antigravity. 35+ skills, 57 UI Styles, production-ready workflows.",
  metadataBase: new URL("https://antigravity-kit.vercel.app/"),
  robots: {
    index: true,
    follow: true,
  },
  openGraph: {
    type: "website",
    locale: "en_US",
    url: "https://antigravity-kit.vercel.app/",
    siteName: "Antigravity Kit",
    images: ["/images/logo.png"],
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        <ThemeProvider
          attribute="class"
          defaultTheme="dark"
          enableSystem
          disableTransitionOnChange
        >
          {children}
        </ThemeProvider>
      </body>
    </html>
  );
}
```

## File: `web/src/app/page.tsx`
```tsx
import Link from "next/link";

const Github = () => {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="currentColor"
      className="w-5 h-5"
    >
      <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" />
    </svg>

  );
};

const AntigravityGoogle = () => {
  return (
    <svg
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 869 113"
      height={30}
      width="230.70000000000002"
    >
      <g clipPath="url(#clip0_6001_463)">
        <path
          d="M839.836 109.037C839.654 109.462 839.442 109.918 839.199 110.403C838.956 110.949 838.805 111.283 838.744 111.405H830.732C831.096 110.616 831.491 109.735 831.916 108.764C832.341 107.854 832.856 106.731 833.463 105.396C833.828 104.607 834.161 103.878 834.465 103.211C834.768 102.543 835.102 101.784 835.466 100.935C835.891 100.146 836.377 99.1443 836.923 97.9304L841.111 88.8262L821.901 45.3083H830.277L844.844 79.8131H845.026L859.046 45.3083H867.422L843.387 100.753C843.144 101.299 842.75 102.149 842.203 103.302C841.718 104.516 841.232 105.669 840.747 106.761C840.322 107.915 840.018 108.673 839.836 109.037Z"
          fill="#202124"
        />
        <path
          d="M792.471 52.3186V45.3084H800.665V32.1984H808.403V45.3084H819.784V52.3186H808.403V77.6282C808.403 80.238 808.919 82.1802 809.951 83.4548C811.044 84.6687 812.652 85.2757 814.776 85.2757C815.748 85.2757 816.658 85.1543 817.508 84.9115C818.357 84.608 819.177 84.2135 819.966 83.7279V91.2844C818.995 91.6486 817.993 91.9217 816.961 92.1038C815.93 92.3466 814.807 92.4679 813.593 92.4679C809.708 92.4679 806.583 91.3148 804.216 89.0084C801.848 86.6413 800.665 83.4852 800.665 79.54V52.3186H792.471Z"
          fill="#202124"
        />
        <path
          d="M778.634 91.7396V45.3083H786.373V91.7396H778.634ZM782.458 36.7504C780.941 36.7504 779.636 36.2042 778.543 35.1117C777.451 34.0192 776.905 32.7142 776.905 31.1969C776.905 29.6188 777.451 28.3139 778.543 27.2821C779.636 26.1896 780.941 25.6433 782.458 25.6433C784.036 25.6433 785.341 26.1896 786.373 27.2821C787.465 28.3139 788.012 29.6188 788.012 31.1969C788.012 32.7142 787.465 34.0192 786.373 35.1117C785.341 36.2042 784.036 36.7504 782.458 36.7504Z"
          fill="#202124"
        />
        <path
          d="M747.697 91.7395L728.943 45.3083H737.227L751.612 82.6354H751.794L766.361 45.3083H774.463L755.527 91.7395H747.697Z"
          fill="#202124"
        />
        <path
          d="M704.033 93.1963C700.574 93.1963 697.539 92.5286 694.929 91.1934C692.319 89.8581 690.256 88.0373 688.738 85.7309C687.282 83.3638 686.553 80.6932 686.553 77.7192C686.553 74.3203 687.434 71.4677 689.194 69.1613C690.954 66.7942 693.321 65.0341 696.295 63.8809C699.269 62.667 702.546 62.06 706.127 62.06C708.191 62.06 710.103 62.2421 711.863 62.6063C713.623 62.9098 715.141 63.3043 716.415 63.7898C717.75 64.2147 718.752 64.6395 719.419 65.0644V62.2421C719.419 58.7218 718.175 55.9299 715.687 53.8663C713.198 51.8027 710.164 50.7709 706.583 50.7709C704.033 50.7709 701.636 51.3475 699.39 52.5007C697.205 53.5932 695.476 55.1409 694.201 57.1438L688.374 52.7738C689.588 50.9529 691.106 49.3749 692.926 48.0396C694.747 46.7043 696.811 45.6725 699.117 44.9442C701.484 44.2159 703.973 43.8517 706.583 43.8517C712.895 43.8517 717.841 45.5208 721.422 48.859C725.003 52.1972 726.794 56.6886 726.794 62.3332V91.7396H719.419V85.0936H719.055C718.266 86.4289 717.143 87.7338 715.687 89.0084C714.23 90.2223 712.5 91.2237 710.497 92.0127C708.555 92.8018 706.401 93.1963 704.033 93.1963ZM704.762 86.3682C707.432 86.3682 709.86 85.7005 712.045 84.3652C714.291 83.03 716.081 81.2395 717.417 78.9938C718.752 76.7481 719.419 74.29 719.419 71.6194C718.024 70.6483 716.263 69.8593 714.139 69.2523C712.075 68.6454 709.799 68.3419 707.311 68.3419C702.88 68.3419 699.633 69.2523 697.57 71.0732C695.506 72.894 694.474 75.1397 694.474 77.8102C694.474 80.3594 695.445 82.423 697.387 84.0011C699.33 85.5791 701.788 86.3682 704.762 86.3682Z"
          fill="#202124"
        />
        <path
          d="M658.47 91.7395V45.3083H665.844V52.7737H666.209C666.815 51.0136 667.817 49.4962 669.213 48.2216C670.67 46.8863 672.308 45.8545 674.129 45.1262C676.011 44.3372 677.862 43.9427 679.683 43.9427C681.079 43.9427 682.171 44.0337 682.96 44.2158C683.749 44.3372 684.478 44.5496 685.145 44.8531V53.2289C684.174 52.7434 683.112 52.3792 681.959 52.1364C680.866 51.8936 679.743 51.7722 678.59 51.7722C676.344 51.7722 674.281 52.4095 672.399 53.6841C670.518 54.9587 669 56.6582 667.847 58.7825C666.755 60.9068 666.209 63.2435 666.209 65.7927V91.7395H658.47Z"
          fill="#202124"
        />
        <path
          d="M626.539 112.861C622.594 112.861 619.195 112.194 616.343 110.858C613.551 109.584 611.275 107.945 609.514 105.942C607.815 103.939 606.601 101.906 605.873 99.8423L612.974 96.838C613.945 99.3871 615.584 101.511 617.89 103.211C620.257 104.971 623.14 105.851 626.539 105.851C631.395 105.851 635.127 104.425 637.737 101.572C640.347 98.7802 641.652 94.8654 641.652 89.8277V84.6384H641.288C639.831 86.8841 637.737 88.7959 635.006 90.374C632.275 91.8914 629.088 92.65 625.447 92.65C621.441 92.65 617.769 91.6182 614.431 89.5546C611.153 87.491 608.543 84.6384 606.601 80.9967C604.659 77.2943 603.688 73.0457 603.688 68.2509C603.688 63.456 604.659 59.2377 606.601 55.5961C608.543 51.8937 611.153 49.0107 614.431 46.9471C617.769 44.8835 621.441 43.8517 625.447 43.8517C629.088 43.8517 632.275 44.6407 635.006 46.2188C637.737 47.7361 639.831 49.648 641.288 51.9544H641.652V45.3084H649.027V89.9188C649.027 95.0778 648.025 99.3568 646.022 102.756C644.08 106.155 641.409 108.673 638.01 110.312C634.672 112.012 630.849 112.861 626.539 112.861ZM626.539 85.6398C629.27 85.6398 631.789 84.9722 634.096 83.6369C636.402 82.2409 638.223 80.238 639.558 77.6282C640.954 75.0183 641.652 71.8925 641.652 68.2509C641.652 64.4878 640.954 61.3317 639.558 58.7825C638.223 56.1727 636.402 54.2001 634.096 52.8648C631.789 51.5295 629.27 50.8619 626.539 50.8619C623.808 50.8619 621.289 51.5599 618.983 52.9559C616.676 54.2911 614.825 56.2637 613.429 58.8736C612.033 61.4227 611.335 64.5485 611.335 68.2509C611.335 71.9532 612.033 75.1093 613.429 77.7192C614.825 80.2684 616.676 82.2409 618.983 83.6369C621.289 84.9722 623.808 85.6398 626.539 85.6398Z"
          fill="#202124"
        />
        <path
          d="M588.94 91.7396V45.3083H596.679V91.7396H588.94ZM592.764 36.7504C591.247 36.7504 589.942 36.2042 588.849 35.1117C587.757 34.0192 587.211 32.7142 587.211 31.1969C587.211 29.6188 587.757 28.3139 588.849 27.2821C589.942 26.1896 591.247 25.6433 592.764 25.6433C594.342 25.6433 595.647 26.1896 596.679 27.2821C597.772 28.3139 598.318 29.6188 598.318 31.1969C598.318 32.7142 597.772 34.0192 596.679 35.1117C595.647 36.2042 594.342 36.7504 592.764 36.7504Z"
          fill="#202124"
        />
        <path
          d="M554.23 52.3186V45.3084H562.424V32.1984H570.162V45.3084H581.542V52.3186H570.162V77.6282C570.162 80.238 570.678 82.1802 571.71 83.4548C572.802 84.6687 574.411 85.2757 576.535 85.2757C577.506 85.2757 578.417 85.1543 579.266 84.9115C580.116 84.608 580.936 84.2135 581.725 83.7279V91.2844C580.753 91.6486 579.752 91.9217 578.72 92.1038C577.688 92.3466 576.566 92.4679 575.352 92.4679C571.467 92.4679 568.341 91.3148 565.974 89.0084C563.607 86.6413 562.424 83.4852 562.424 79.54V52.3186H554.23Z"
          fill="#202124"
        />
        <path
          d="M509.898 91.7396V45.3084H517.272V52.1365H517.636C518.85 49.8908 520.823 47.9486 523.554 46.3098C526.346 44.6711 529.381 43.8517 532.658 43.8517C538.364 43.8517 542.643 45.5208 545.495 48.859C548.409 52.1365 549.865 56.5065 549.865 61.969V91.7396H542.127V63.1525C542.127 58.6611 541.034 55.505 538.849 53.6842C536.725 51.8027 533.963 50.8619 530.564 50.8619C528.015 50.8619 525.77 51.5902 523.827 53.0469C521.885 54.4429 520.368 56.2637 519.275 58.5094C518.183 60.7551 517.636 63.1222 517.636 65.6107V91.7396H509.898Z"
          fill="#202124"
        />
        <path
          d="M446.449 91.7396L471.212 26.5538H479.952L504.716 91.7396H496.249L489.603 73.8044H461.562L454.916 91.7396H446.449ZM486.963 66.5211L478.314 43.0323L475.764 36.0221H475.4L472.851 43.0323L464.202 66.5211H486.963Z"
          fill="#202124"
        />
        <path
          d="M169.742 93.2042C149.435 93.2042 132.375 76.6583 132.375 56.3521C132.375 36.0458 149.435 19.5 169.742 19.5C180.973 19.5 188.959 23.9036 194.976 29.6531L187.881 36.7484C183.566 32.701 177.728 29.5542 169.742 29.5542C154.928 29.5542 143.34 41.5083 143.34 56.3422C143.34 71.176 154.928 83.1203 169.742 83.1203C179.351 83.1203 184.833 79.2609 188.336 75.7479C191.206 72.8682 193.096 68.7417 193.818 63.0714H169.484V53.0073H203.605C203.961 54.8083 204.14 56.9656 204.14 59.301C204.14 66.8516 202.071 76.2031 195.431 82.8531C188.969 89.5922 180.706 93.1844 169.742 93.1844V93.2042Z"
          fill="#202124"
        />
        <path
          d="M255.242 69.474C255.242 83.1401 244.564 93.2042 231.472 93.2042C218.38 93.2042 207.702 83.1401 207.702 69.474C207.702 55.8078 218.38 45.7438 231.472 45.7438C244.564 45.7438 255.242 55.7188 255.242 69.474ZM244.831 69.474C244.831 60.9339 238.637 55.0953 231.462 55.0953C224.288 55.0953 218.093 60.9339 218.093 69.474C218.093 78.0141 224.288 83.8526 231.462 83.8526C238.637 83.8526 244.831 77.925 244.831 69.474Z"
          fill="#202124"
        />
        <path
          d="M306.987 69.474C306.987 83.1401 296.309 93.2042 283.217 93.2042C270.125 93.2042 259.447 83.1401 259.447 69.474C259.447 55.8078 270.125 45.7438 283.217 45.7438C296.309 45.7438 306.987 55.7188 306.987 69.474ZM296.576 69.474C296.576 60.9339 290.382 55.0953 283.207 55.0953C276.033 55.0953 269.838 60.9339 269.838 69.474C269.838 78.0141 276.033 83.8526 283.207 83.8526C290.382 83.8526 296.576 77.925 296.576 69.474Z"
          fill="#202124"
        />
        <path
          d="M356.486 47.1787V89.7802C356.486 107.306 346.155 114.5 333.943 114.5C322.444 114.5 315.527 106.771 312.924 100.478L321.999 96.7073C323.612 100.577 327.57 105.158 333.943 105.158C341.761 105.158 346.61 100.309 346.61 91.225V87.811H346.254C343.918 90.6906 339.425 93.2042 333.765 93.2042C321.91 93.2042 311.044 82.8729 311.044 69.563C311.044 56.2531 321.91 45.7438 333.765 45.7438C339.425 45.7438 343.918 48.2573 346.254 51.0479H346.61V47.1787H356.486ZM347.322 69.563C347.322 61.2011 341.751 55.0953 334.656 55.0953C327.56 55.0953 321.455 61.211 321.455 69.563C321.455 77.9151 327.471 83.8526 334.656 83.8526C341.84 83.8526 347.322 77.8261 347.322 69.563Z"
          fill="#202124"
        />
        <path
          d="M374.397 22.0136V91.7594H363.977V22.0136H374.397Z"
          fill="#202124"
        />
        <path
          d="M414.782 77.2917L422.867 82.6849C420.265 86.5542 413.971 93.2042 403.105 93.2042C389.637 93.2042 379.573 82.774 379.573 69.474C379.573 55.3625 389.726 45.7438 401.938 45.7438C414.149 45.7438 420.255 55.5406 422.234 60.8448L423.313 63.5365L391.606 76.6583C394.031 81.4182 397.801 83.8526 403.105 83.8526C408.409 83.8526 412.091 81.25 414.782 77.2917ZM389.904 68.7516L411.101 59.9443C409.933 56.9755 406.43 54.9073 402.304 54.9073C397.009 54.9073 389.637 59.5781 389.914 68.7516H389.904Z"
          fill="#202124"
        />
        <path
          d="M89.6992 93.695C94.3659 97.195 101.366 94.8617 94.9492 88.445C75.6992 69.7783 79.7825 18.445 55.8659 18.445C31.9492 18.445 36.0325 69.7783 16.7825 88.445C9.78251 95.445 17.3658 97.195 22.0325 93.695C40.1159 81.445 38.9492 59.8617 55.8659 59.8617C72.7825 59.8617 71.6159 81.445 89.6992 93.695Z"
          fill="#3186FF"
        />
        <mask
          id="mask0_6001_463"
          maskUnits="userSpaceOnUse"
          x={13}
          y={18}
          width={85}
          height={78}
          style={{ maskType: "alpha" }}
        >
          <path
            d="M89.6992 93.695C94.3659 97.195 101.366 94.8617 94.9492 88.445C75.6992 69.7783 79.7825 18.445 55.8659 18.445C31.9492 18.445 36.0325 69.7783 16.7825 88.445C9.78251 95.445 17.3658 97.195 22.0325 93.695C40.1159 81.445 38.9492 59.8617 55.8659 59.8617C72.7825 59.8617 71.6159 81.445 89.6992 93.695Z"
            fill="black"
          />
        </mask>
        <g mask="url(#mask0_6001_463)">
          <g filter="url(#filter0_f_6001_463)">
            <ellipse
              cx="22.7873"
              cy="26.8098"
              rx="22.7873"
              ry="26.8098"
              transform="matrix(-0.112784 0.99362 -0.99362 -0.112781 66.2473 -15.5344)"
              fill="#FFE432"
            />
          </g>
          <g filter="url(#filter1_f_6001_463)">
            <ellipse
              cx="96.491"
              cy="35.1231"
              rx="29.5007"
              ry="30.1492"
              transform="rotate(76.9243 96.491 35.1231)"
              fill="#FC413D"
            />
          </g>
          <g filter="url(#filter2_f_6001_463)">
            <ellipse
              cx="9.02988"
              cy="41.6647"
              rx="30.832"
              ry="39.9417"
              transform="rotate(74.1257 9.02988 41.6647)"
              fill="#00B95C"
            />
          </g>
          <g filter="url(#filter3_f_6001_463)">
            <ellipse
              cx="9.02988"
              cy="41.6647"
              rx="30.832"
              ry="39.9417"
              transform="rotate(74.1257 9.02988 41.6647)"
              fill="#00B95C"
            />
          </g>
          <g filter="url(#filter4_f_6001_463)">
            <ellipse
              cx="11.2212"
              cy="42.8915"
              rx="30.22"
              ry="33.2695"
              transform="rotate(45.6065 11.2212 42.8915)"
              fill="#00B95C"
            />
          </g>
          <g filter="url(#filter5_f_6001_463)">
            <ellipse
              cx="75.7546"
              cy="104.822"
              rx="29.0177"
              ry="27.943"
              transform="rotate(76.9243 75.7546 104.822)"
              fill="#3186FF"
            />
          </g>
          <g filter="url(#filter6_f_6001_463)">
            <ellipse
              cx="33.5661"
              cy="35.4043"
              rx="33.5661"
              ry="35.4043"
              transform="matrix(-0.409539 0.912293 -0.912294 -0.409537 101.25 -15.1674)"
              fill="#FBBC04"
            />
          </g>
          <g filter="url(#filter7_f_6001_463)">
            <path
              d="M2.56802 149.695C-15.8116 142.48 15.5987 83.1163 23.4093 63.2203C31.22 43.3244 52.4514 33.0447 70.831 40.26C89.2107 47.4753 110.996 87.2162 103.185 107.112C95.3742 127.008 20.9477 156.91 2.56802 149.695Z"
              fill="#3186FF"
            />
          </g>
          <g filter="url(#filter8_f_6001_463)">
            <path
              d="M113.934 75.8079C109.013 81.5509 96.1724 78.6224 85.253 69.2667C74.3335 59.911 69.4704 47.6711 74.391 41.928C79.3116 36.185 92.1525 39.1136 103.072 48.4692C113.991 57.8249 118.855 70.0648 113.934 75.8079Z"
              fill="#749BFF"
            />
          </g>
          <g filter="url(#filter9_f_6001_463)">
            <ellipse
              cx="92.611"
              cy="23.7962"
              rx="44.2411"
              ry="27.5016"
              transform="rotate(34.0763 92.611 23.7962)"
              fill="#FC413D"
            />
          </g>
          <g filter="url(#filter10_f_6001_463)">
            <ellipse
              cx="23.4949"
              cy="29.5887"
              rx="23.7071"
              ry="13.7869"
              transform="rotate(112.516 23.4949 29.5887)"
              fill="#FFEE48"
            />
          </g>
        </g>
      </g>
      <defs>
        <filter
          id="filter0_f_6001_463"
          x="2.49348"
          y="-26.5423"
          width="69.0899"
          height="61.2525"
          filterUnits="userSpaceOnUse"
          colorInterpolationFilters="sRGB"
        >
          <feFlood floodOpacity={0} result="BackgroundImageFix" />
          <feBlend
            mode="normal"
            in="SourceGraphic"
            in2="BackgroundImageFix"
            result="shape"
          />
          <feGaussianBlur
            stdDeviation="3.89034"
            result="effect1_foregroundBlur_6001_463"
          />
        </filter>
        <filter
          id="filter1_f_6001_463"
          x="28.7524"
          y="-32.0333"
          width="135.477"
          height="134.313"
          filterUnits="userSpaceOnUse"
          colorInterpolationFilters="sRGB"
        >
          <feFlood floodOpacity={0} result="BackgroundImageFix" />
          <feBlend
            mode="normal"
            in="SourceGraphic"
            in2="BackgroundImageFix"
            result="shape"
          />
          <feGaussianBlur
            stdDeviation="18.8078"
            result="effect1_foregroundBlur_6001_463"
          />
        </filter>
        <filter
          id="filter2_f_6001_463"
          x="-62.2884"
          y="-21.9253"
          width="142.637"
          height="127.18"
          filterUnits="userSpaceOnUse"
          colorInterpolationFilters="sRGB"
        >
          <feFlood floodOpacity={0} result="BackgroundImageFix" />
          <feBlend
            mode="normal"
            in="SourceGraphic"
            in2="BackgroundImageFix"
            result="shape"
          />
          <feGaussianBlur
            stdDeviation="15.9884"
            result="effect1_foregroundBlur_6001_463"
          />
        </filter>
        <filter
          id="filter3_f_6001_463"
          x="-62.2884"
          y="-21.9253"
          width="142.637"
          height="127.18"
          filterUnits="userSpaceOnUse"
          colorInterpolationFilters="sRGB"
        >
          <feFlood floodOpacity={0} result="BackgroundImageFix" />
          <feBlend
            mode="normal"
            in="SourceGraphic"
            in2="BackgroundImageFix"
            result="shape"
          />
          <feGaussianBlur
            stdDeviation="15.9884"
            result="effect1_foregroundBlur_6001_463"
          />
        </filter>
        <filter
          id="filter4_f_6001_463"
          x="-52.5697"
          y="-20.8346"
          width="127.582"
          height="127.452"
          filterUnits="userSpaceOnUse"
          colorInterpolationFilters="sRGB"
        >
          <feFlood floodOpacity={0} result="BackgroundImageFix" />
          <feBlend
            mode="normal"
            in="SourceGraphic"
            in2="BackgroundImageFix"
            result="shape"
          />
          <feGaussianBlur
            stdDeviation="15.9884"
            result="effect1_foregroundBlur_6001_463"
          />
        </filter>
        <filter
          id="filter5_f_6001_463"
          x="17.3619"
          y="45.4646"
          width="116.786"
          height="118.715"
          filterUnits="userSpaceOnUse"
          colorInterpolationFilters="sRGB"
        >
          <feFlood floodOpacity={0} result="BackgroundImageFix" />
          <feBlend
            mode="normal"
            in="SourceGraphic"
            in2="BackgroundImageFix"
            result="shape"
          />
          <feGaussianBlur
            stdDeviation="15.1937"
            result="effect1_foregroundBlur_6001_463"
          />
        </filter>
        <filter
          id="filter6_f_6001_463"
          x="-7.44765"
          y="-60.4737"
          width="125.303"
          height="122.858"
          filterUnits="userSpaceOnUse"
          colorInterpolationFilters="sRGB"
        >
          <feFlood floodOpacity={0} result="BackgroundImageFix" />
          <feBlend
            mode="normal"
            in="SourceGraphic"
            in2="BackgroundImageFix"
            result="shape"
          />
          <feGaussianBlur
            stdDeviation="13.7698"
            result="effect1_foregroundBlur_6001_463"
          />
        </filter>
        <filter
          id="filter7_f_6001_463"
          x="-27.7086"
          y="13.3597"
          width="157.119"
          height="162.029"
          filterUnits="userSpaceOnUse"
          colorInterpolationFilters="sRGB"
        >
          <feFlood floodOpacity={0} result="BackgroundImageFix" />
          <feBlend
            mode="normal"
            in="SourceGraphic"
            in2="BackgroundImageFix"
            result="shape"
          />
          <feGaussianBlur
            stdDeviation="12.297"
            result="effect1_foregroundBlur_6001_463"
          />
        </filter>
        <filter
          id="filter8_f_6001_463"
          x="50.4638"
          y="16.981"
          width="87.3973"
          height="83.7738"
          filterUnits="userSpaceOnUse"
          colorInterpolationFilters="sRGB"
        >
          <feFlood floodOpacity={0} result="BackgroundImageFix" />
          <feBlend
            mode="normal"
            in="SourceGraphic"
            in2="BackgroundImageFix"
            result="shape"
          />
          <feGaussianBlur
            stdDeviation="11.0036"
            result="effect1_foregroundBlur_6001_463"
          />
        </filter>
        <filter
          id="filter9_f_6001_463"
          x="34.2604"
          y="-28.457"
          width="116.701"
          height="104.506"
          filterUnits="userSpaceOnUse"
          colorInterpolationFilters="sRGB"
        >
          <feFlood floodOpacity={0} result="BackgroundImageFix" />
          <feBlend
            mode="normal"
            in="SourceGraphic"
            in2="BackgroundImageFix"
            result="shape"
          />
          <feGaussianBlur
            stdDeviation="9.29385"
            result="effect1_foregroundBlur_6001_463"
          />
        </filter>
        <filter
          id="filter10_f_6001_463"
          x="-15.1522"
          y="-15.9493"
          width="77.2941"
          height="91.076"
          filterUnits="userSpaceOnUse"
          colorInterpolationFilters="sRGB"
        >
          <feFlood floodOpacity={0} result="BackgroundImageFix" />
          <feBlend
            mode="normal"
            in="SourceGraphic"
            in2="BackgroundImageFix"
            result="shape"
          />
          <feGaussianBlur
            stdDeviation="11.5027"
            result="effect1_foregroundBlur_6001_463"
          />
        </filter>
        <clipPath id="clip0_6001_463">
          <rect width={869} height={113} fill="white" />
        </clipPath>
      </defs>
    </svg>

  );
};

import Typing from "@/components/typing";

export default function Home() {
  return (
    <div className="flex min-h-screen items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <main className="flex min-h-screen w-full max-w-3xl flex-col items-center justify-between py-32 px-16 bg-white dark:bg-black sm:items-start">
        <img
          className="dark:invert"
          src="/images/logo.png"
          alt="Antigravity Kit logo"
          width={100}
          height={20}
        />
        <div className="flex flex-col items-center gap-6 text-center sm:items-start sm:text-left">
          <h1 className="max-w-xs text-3xl font-semibold leading-10 tracking-tight text-black dark:text-zinc-50">
            <span className="before:-inset-x-1 before:-rotate-1 relative z-4 before:pointer-events-none before:absolute before:inset-y-0 before:z-4 before:bg-linear-to-r before:from-blue-500 before:via-cyan-500 before:to-orange-500 before:opacity-16 before:mix-blend-hard-light">
              Antigravity Kit
            </span>
          </h1>
          <p className="max-w-md text-lg leading-8 text-zinc-600 dark:text-zinc-400">
            AI Agent templates with Skills, Agents, and Workflows for{" "}
            <a
              href="https://antigravity.google/t"
              className="inline-flex items-center align-middle font-medium text-zinc-950 dark:text-zinc-50 mb-2"
              target="_blank"
              rel="noopener noreferrer"
            >
              <AntigravityGoogle />
            </a>
          </p>
          <Typing />
        </div>
        <div className="flex flex-col gap-4 text-base font-medium sm:flex-row">
          <a
            className="flex h-12 w-full items-center justify-center gap-2 rounded-full bg-foreground px-5 text-background transition-colors hover:bg-[#383838] dark:hover:bg-[#ccc] md:w-[158px]"
            href="https://github.com/vudovn/antigravity-kit"
            target="_blank"
            rel="noopener noreferrer"
          >
            <Github />
            GitHub
          </a>
          <Link
            className="flex h-12 w-full items-center justify-center gap-2 rounded-full bg-foreground px-5 text-background transition-colors hover:bg-[#383838] dark:hover:bg-[#ccc] md:w-[158px]"
            href="/docs"
          >
            Documentation
          </Link>
        </div>
      </main>
    </div>
  );
}
```

## File: `web/src/app/brain/knowledge/docs_legacy/layout.tsx`
```tsx
import type { Metadata } from "next";
import DocsSidebar from "@/components/brain/knowledge/docs_legacy/sidebar";
import Header from "@/components/layout/header";
import Footer from "@/components/layout/footer";

export const metadata: Metadata = {
    title: "Documentation | Antigravity Kit",
    description: "Complete documentation for Antigravity Kit - AI Agent templates with Skills, Agents, and Workflows.",
};

export default function DocsLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    return (
        <div className="min-h-screen bg-white dark:bg-zinc-950 flex flex-col">
            {/* Header */}
            <Header />

            <div className="container mx-auto px-4 sm:px-6 lg:px-8 flex-1">
                <div className="flex gap-8 lg:gap-12">
                    {/* Sidebar Navigation - Desktop */}
                    <aside className="hidden lg:block w-64 shrink-0 sticky top-[57px] h-[calc(100vh-3.5rem)] overflow-y-auto py-8 scrollbar-thin">
                        <DocsSidebar />
                    </aside>

                    {/* Main Content Area */}
                    <main className="flex-1 min-w-0 py-8 lg:py-10 max-w-4xl">
                        {children}
                    </main>

                    {/* Right Sidebar - Table of Contents */}
                    <aside className="hidden xl:block w-64 shrink-0 sticky top-[57px] h-[calc(100vh-3.5rem)] overflow-y-auto py-8 scrollbar-thin">
                        <div className="text-sm">
                            <div className="font-semibold text-zinc-900 dark:text-zinc-50 mb-3">
                                On This Page
                            </div>
                            <div className="text-xs text-zinc-500 dark:text-zinc-500">
                                Table of contents coming soon
                            </div>
                        </div>
                    </aside>
                </div>
            </div>

            {/* Footer */}
            <Footer />
        </div>
    );
}
```

## File: `web/src/app/brain/knowledge/docs_legacy/page.tsx`
```tsx
import Link from "next/link";
import agents from '@/services/agents.json';
import skills from '@/services/skills.json';
import workflows from '@/services/workflows.json';

export default function DocsPage() {
    return (
        <div className="max-w-3xl">
            {/* Page Header */}
            <div className="mb-8 pb-8 border-b border-zinc-200 dark:border-zinc-800">
                <h1 className="text-4xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    Documentation
                </h1>
                <p className="text-lg text-zinc-600 dark:text-zinc-400">
                    Welcome to the <span className="before:-inset-x-1 before:-rotate-1 relative z-4 before:pointer-events-none before:absolute before:inset-y-0 before:z-4 before:bg-linear-to-r before:from-blue-500 before:via-purple-500 before:to-orange-500 before:opacity-16 before:mix-blend-hard-light">
                        Antigravity Kit
                    </span> documentation.
                </p>
            </div>

            {/* What is Antigravity Kit */}
            <section className="mb-12">
                <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    What is <span className="before:-inset-x-1 before:-rotate-1 relative z-4 before:pointer-events-none before:absolute before:inset-y-0 before:z-4 before:bg-linear-to-r before:from-blue-500 before:via-purple-500 before:to-orange-500 before:opacity-16 before:mix-blend-hard-light">
                        Antigravity Kit
                    </span> ?
                </h2>
                <p className="text-base text-zinc-600 dark:text-zinc-400 mb-4">
                    <span className="before:-inset-x-1 before:-rotate-1 relative z-4 before:pointer-events-none before:absolute before:inset-y-0 before:z-4 before:bg-linear-to-r before:from-blue-500 before:via-purple-500 before:to-orange-500 before:opacity-16 before:mix-blend-hard-light">
                        Antigravity Kit
                    </span> is a comprehensive collection of AI Agent templates with Skills, Agents, and Workflows designed to supercharge AI coding assistants for{" "}
                    <a
                        href="https://antigravity.google/t"
                        className="text-zinc-900 dark:text-zinc-50 underline underline-offset-4 decoration-zinc-300 dark:decoration-zinc-700 hover:decoration-zinc-900 dark:hover:decoration-zinc-50 transition-colors"
                    >
                        Antigravity
                    </a>.
                </p>
                <p className="text-base text-zinc-600 dark:text-zinc-400 mb-4">
                    Whether you're an individual developer or part of a larger team, Antigravity Kit helps you build better software faster with {skills.length}+ skills, {agents.length}+ specialist agents, and {workflows.length}+ production-ready workflows.
                </p>
            </section>

            {/* What's Included */}
            <section className="mb-12">
                <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    What's Included
                </h2>
                <div className="grid gap-4 sm:grid-cols-3 mb-6">
                    <div className="p-6 rounded-lg border border-zinc-200 dark:border-zinc-800 bg-zinc-50 dark:bg-zinc-900">
                        <div className="text-3xl font-bold text-zinc-900 dark:text-zinc-50 mb-2">{agents.length}+</div>
                        <div className="text-sm font-medium text-zinc-600 dark:text-zinc-400">Specialist Agents</div>
                        <p className="text-xs text-zinc-500 dark:text-zinc-500 mt-2">
                            Domain experts for frontend, backend, security, and more
                        </p>
                    </div>
                    <div className="p-6 rounded-lg border border-zinc-200 dark:border-zinc-800 bg-zinc-50 dark:bg-zinc-900">
                        <div className="text-3xl font-bold text-zinc-900 dark:text-zinc-50 mb-2">{skills.length}+</div>
                        <div className="text-sm font-medium text-zinc-600 dark:text-zinc-400">Domain Skills</div>
                        <p className="text-xs text-zinc-500 dark:text-zinc-500 mt-2">
                            Knowledge modules for React, Next.js, testing, and more
                        </p>
                    </div>
                    <div className="p-6 rounded-lg border border-zinc-200 dark:border-zinc-800 bg-zinc-50 dark:bg-zinc-900">
                        <div className="text-3xl font-bold text-zinc-900 dark:text-zinc-50 mb-2">{workflows.length}+</div>
                        <div className="text-sm font-medium text-zinc-600 dark:text-zinc-400">Workflows</div>
                        <p className="text-xs text-zinc-500 dark:text-zinc-500 mt-2">
                            Slash command procedures for common dev tasks
                        </p>
                    </div>
                </div>
            </section>

            {/* How to Use the Docs */}
            <section className="mb-12">
                <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    How to Use the Docs
                </h2>
                <p className="text-base text-zinc-600 dark:text-zinc-400 mb-4">
                    The docs are organized into 3 main sections:
                </p>
                <div className="space-y-4 mb-6">
                    <div className="p-4 rounded-lg border border-zinc-200 dark:border-zinc-800">
                        <Link href="/brain/knowledge/docs_legacy/installation" className="font-semibold text-zinc-900 dark:text-zinc-50 hover:underline">
                            Getting Started
                        </Link>
                        <p className="text-sm text-zinc-600 dark:text-zinc-400 mt-1">
                            Quick installation and setup guide to get you started
                        </p>
                    </div>
                    <div className="p-4 rounded-lg border border-zinc-200 dark:border-zinc-800">
                        <Link href="/brain/knowledge/docs_legacy/agents" className="font-semibold text-zinc-900 dark:text-zinc-50 hover:underline">
                            Core Concepts
                        </Link>
                        <p className="text-sm text-zinc-600 dark:text-zinc-400 mt-1">
                            Learn about Agents, Skills, and Workflows
                        </p>
                    </div>
                    <div className="p-4 rounded-lg border border-zinc-200 dark:border-zinc-800">
                        <Link href="/brain/knowledge/docs_legacy/cli" className="font-semibold text-zinc-900 dark:text-zinc-50 hover:underline">
                            CLI Reference
                        </Link>
                        <p className="text-sm text-zinc-600 dark:text-zinc-400 mt-1">
                            Detailed command-line interface documentation
                        </p>
                    </div>
                </div>
                <p className="text-sm text-zinc-600 dark:text-zinc-400">
                    Use the sidebar to navigate through sections, or use <kbd className="px-2 py-1 text-xs font-mono rounded bg-zinc-100 dark:bg-zinc-800 border border-zinc-200 dark:border-zinc-700">Ctrl+K</kbd> to quickly search.
                </p>
            </section>

            {/* Next Steps */}
            <section className="mb-12">
                <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    Next Steps
                </h2>
                <div className="grid gap-4 sm:grid-cols-2">
                    <Link
                        href="/brain/knowledge/docs_legacy/installation"
                        className="group p-6 rounded-lg border border-zinc-200 dark:border-zinc-800 hover:border-zinc-300 dark:hover:border-zinc-700 hover:bg-zinc-50 dark:hover:bg-zinc-900 transition-all"
                    >
                        <div className="flex items-center justify-between mb-2">
                            <h3 className="font-semibold text-zinc-900 dark:text-zinc-50">Installation →</h3>
                        </div>
                        <p className="text-sm text-zinc-600 dark:text-zinc-400">
                            Get started with Antigravity Kit in under a minute
                        </p>
                    </Link>
                    <Link
                        href="/brain/knowledge/docs_legacy/agents"
                        className="group p-6 rounded-lg border border-zinc-200 dark:border-zinc-800 hover:border-zinc-300 dark:hover:border-zinc-700 hover:bg-zinc-50 dark:hover:bg-zinc-900 transition-all"
                    >
                        <div className="flex items-center justify-between mb-2">
                            <h3 className="font-semibold text-zinc-900 dark:text-zinc-50">Learn Core Concepts →</h3>
                        </div>
                        <p className="text-sm text-zinc-600 dark:text-zinc-400">
                            Understand how Agents, Skills, and Workflows work
                        </p>
                    </Link>
                </div>
            </section>

            {/* Footer Navigation */}
            <div className="pt-8 border-t border-zinc-200 dark:border-zinc-800 flex items-center justify-between">
                <div className="text-sm text-zinc-500 dark:text-zinc-500">
                    Getting Started
                </div>
                <Link
                    href="/brain/knowledge/docs_legacy/installation"
                    className="text-sm font-medium text-zinc-900 dark:text-zinc-50 hover:underline flex items-center gap-1"
                >
                    Installation
                    <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                    </svg>
                </Link>
            </div>
        </div>
    );
}
```

## File: `web/src/app/brain/knowledge/docs_legacy/agents/page.tsx`
```tsx
import Link from "next/link";
import { Lightbulb } from "lucide-react";
import agentsData from "@/services/agents.json";

export default function AgentsPage() {
    const agents = agentsData;

    return (
        <div className="max-w-3xl">
            {/* Breadcrumb */}
            <nav className="flex items-center gap-2 text-sm text-zinc-600 dark:text-zinc-400 mb-6">
                <Link href="/docs" className="hover:text-zinc-900 dark:hover:text-zinc-50">Docs</Link>
                <span>/</span>
                <span className="text-zinc-900 dark:text-zinc-50">Agents</span>
            </nav>

            {/* Page Header */}
            <div className="mb-8 pb-8 border-b border-zinc-200 dark:border-zinc-800">
                <h1 className="text-4xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    Agents
                </h1>
                <p className="text-lg text-zinc-600 dark:text-zinc-400">
                    Specialist AI personas with deep expertise in specific domains.
                </p>
            </div>

            {/* What are Agents */}
            <section className="mb-12">
                <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    What are Agents?
                </h2>
                <p className="text-base text-zinc-600 dark:text-zinc-400 mb-4">
                    Agents are specialist AI personas configured with domain-specific expertise, tools, and behavioral patterns. Each agent is designed to excel in a particular area of software development.
                </p>
                <p className="text-base text-zinc-600 dark:text-zinc-400 mb-6">
                    When you make a request, Antigravity Kit's <strong>Intelligent Routing</strong> system automatically detects which agents are needed and activates them for you. You can also mention them by name to force a specific perspective.
                </p>
            </section>

            {/* How to Use */}
            <section className="mb-12">
                <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    How to Use Agents
                </h2>
                <p className="text-base text-zinc-600 dark:text-zinc-400 mb-6">
                    <strong>No need to mention agents explicitly!</strong> The system automatically detects and applies the right specialist(s) based on your request.
                </p>

                <div className="relative group mb-6">
                    <pre className="p-4 rounded-lg bg-zinc-900 dark:bg-zinc-900 overflow-x-auto border border-zinc-800 font-mono text-sm">
                        <code className="text-zinc-100">{`You: "Add JWT authentication"
AI: 🤖 Applying @security-auditor + @backend-specialist...

You: "Fix the dark mode button"
AI: 🤖 Using @frontend-specialist...

You: "Login returns 500 error"
AI: 🤖 Using @debugger for systematic analysis...`}</code>
                    </pre>
                </div>

                <p className="text-base text-zinc-600 dark:text-zinc-400 mb-6">
                    However, you <strong>can still override</strong> this behavior by explicitly mentioning an agent name:
                </p>

                <div className="relative group mb-6">
                    <pre className="p-4 rounded-lg bg-zinc-900 dark:bg-zinc-900 overflow-x-auto border border-zinc-800 font-mono text-sm">
                        <code className="text-zinc-100">{`Use the security-auditor agent to review authentication...`}</code>
                    </pre>
                </div>

                <div className="p-4 rounded-lg border border-blue-200 dark:border-blue-900 bg-blue-50 dark:bg-blue-950/20 mb-6">
                    <p className="text-sm text-blue-900 dark:text-blue-200">
                        <Lightbulb className="w-4 h-4 inline" />
                        <strong className="font-semibold">Tip:</strong> Agents can work together! Use the <code className="px-1 py-0.5 rounded bg-blue-100 dark:bg-blue-900/40 font-mono text-xs">orchestrator</code> agent to coordinate multiple specialists on complex tasks.
                    </p>
                </div>
            </section>

            {/* Available Agents */}
            <section className="mb-12">
                <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    Available Agents
                </h2>
                <p className="text-base text-zinc-600 dark:text-zinc-400 mb-6">
                    Antigravity Kit includes {agents.length} specialist agents:
                </p>

                <div className="space-y-4">
                    {agents.map((agent) => (
                        <div
                            key={agent.name}
                            className="p-5 rounded-lg border border-zinc-200 dark:border-zinc-800 hover:border-zinc-300 dark:hover:border-zinc-700 hover:bg-zinc-50 dark:hover:bg-zinc-900 transition-all"
                        >
                            <div className="flex items-start justify-between gap-4 mb-2">
                                <code className="text-base font-mono font-semibold text-zinc-900 dark:text-zinc-50">
                                    {agent.name}
                                </code>
                            </div>
                            <p className="text-sm text-zinc-600 dark:text-zinc-400 leading-relaxed">
                                {agent.description}
                            </p>
                        </div>
                    ))}
                </div>
            </section>

            {/* Agent Structure */}
            <section className="mb-12">
                <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    Agent Structure
                </h2>
                <p className="text-base text-zinc-600 dark:text-zinc-400 mb-6">
                    Each agent is defined by a markdown file with YAML frontmatter:
                </p>

                <div className="relative group mb-6">
                    <pre className="p-4 rounded-lg bg-zinc-900 dark:bg-zinc-900 overflow-x-auto border border-zinc-800 font-mono text-sm">
                        <code className="text-zinc-100">{`---
name: frontend-specialist
description: Frontend architect expert
tools: Read, Edit, Write, Bash
skills: react-patterns, nextjs-best-practices
---

# Frontend Specialist

You are a senior frontend architect...`}</code>
                    </pre>
                </div>

                <p className="text-base text-zinc-600 dark:text-zinc-400">
                    The <code className="px-1.5 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-sm font-mono">skills</code> field determines which domain knowledge modules the agent can access.
                </p>
            </section>

            {/* Next Steps */}
            <section className="mb-12">
                <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    Next Steps
                </h2>
                <div className="grid gap-4 sm:grid-cols-2">
                    <Link
                        href="/brain/knowledge/docs_legacy/skills"
                        className="group p-6 rounded-lg border border-zinc-200 dark:border-zinc-800 hover:border-zinc-300 dark:hover:border-zinc-700 hover:bg-zinc-50 dark:hover:bg-zinc-900 transition-all"
                    >
                        <h3 className="font-semibold text-zinc-900 dark:text-zinc-50 mb-2">Skills →</h3>
                        <p className="text-sm text-zinc-600 dark:text-zinc-400">
                            Learn about domain-specific knowledge modules
                        </p>
                    </Link>
                    <Link
                        href="/brain/knowledge/docs_legacy/workflows"
                        className="group p-6 rounded-lg border border-zinc-200 dark:border-zinc-800 hover:border-zinc-300 dark:hover:border-zinc-700 hover:bg-zinc-50 dark:hover:bg-zinc-900 transition-all"
                    >
                        <h3 className="font-semibold text-zinc-900 dark:text-zinc-50 mb-2">Workflows →</h3>
                        <p className="text-sm text-zinc-600 dark:text-zinc-400">
                            Explore slash command procedures
                        </p>
                    </Link>
                </div>
            </section>

            {/* Footer Navigation */}
            <div className="pt-8 border-t border-zinc-200 dark:border-zinc-800 flex items-center justify-between">
                <Link
                    href="/brain/knowledge/docs_legacy/installation"
                    className="text-sm font-medium text-zinc-900 dark:text-zinc-50 hover:underline flex items-center gap-1"
                >
                    <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
                    </svg>
                    Installation
                </Link>
                <Link
                    href="/brain/knowledge/docs_legacy/skills"
                    className="text-sm font-medium text-zinc-900 dark:text-zinc-50 hover:underline flex items-center gap-1"
                >
                    Skills
                    <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                    </svg>
                </Link>
            </div>
        </div>
    );
}
```

## File: `web/src/app/brain/knowledge/docs_legacy/cli/page.tsx`
```tsx
import Link from "next/link";

export default function CLIPage() {
    return (
        <div className="max-w-3xl">
            {/* Breadcrumb */}
            <nav className="flex items-center gap-2 text-sm text-zinc-600 dark:text-zinc-400 mb-6">
                <Link href="/docs" className="hover:text-zinc-900 dark:hover:text-zinc-50">Docs</Link>
                <span>/</span>
                <span className="text-zinc-900 dark:text-zinc-50">CLI Reference</span>
            </nav>

            {/* Page Header */}
            <div className="mb-8 pb-8 border-b border-zinc-200 dark:border-zinc-800">
                <h1 className="text-4xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    CLI Reference
                </h1>
                <p className="text-lg text-zinc-600 dark:text-zinc-400">
                    Command-line interface for managing Antigravity Kit installations.
                </p>
            </div>

            {/* Overview */}
            <section className="mb-12">
                <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    Overview
                </h2>
                <p className="text-base text-zinc-600 dark:text-zinc-400 mb-6">
                    The <code className="px-1.5 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-sm font-mono">ag-kit</code> CLI tool helps you manage Antigravity Kit installations across your projects.
                </p>
            </section>

            {/* Commands */}
            <section className="mb-12">
                <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    Commands
                </h2>

                <div className="space-y-8">
                    {/* init */}
                    <div>
                        <h3 className="text-xl font-semibold text-zinc-900 dark:text-zinc-50 mb-3">
                            <code className="font-mono">ag-kit init</code>
                        </h3>
                        <p className="text-base text-zinc-600 dark:text-zinc-400 mb-4">
                            Initialize Antigravity Kit in your project by installing the <code className="px-1.5 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-sm font-mono">.agent</code> folder.
                        </p>

                        <div className="relative group mb-4">
                            <pre className="p-4 rounded-lg bg-zinc-900 dark:bg-zinc-900 overflow-x-auto border border-zinc-800 font-mono text-sm">
                                <code className="text-zinc-100">ag-kit init</code>
                            </pre>
                        </div>

                        <div className="p-4 rounded-lg border border-zinc-200 dark:border-zinc-800 bg-zinc-50 dark:bg-zinc-900/50">
                            <div className="text-sm font-semibold text-zinc-900 dark:text-zinc-50 mb-2">Behavior</div>
                            <ul className="text-sm text-zinc-600 dark:text-zinc-400 space-y-1">
                                <li>• Creates <code className="px-1 py-0.5 rounded bg-zinc-200 dark:bg-zinc-800 font-mono text-xs">.agent/</code> directory in current folder</li>
                                <li>• Downloads latest templates from GitHub</li>
                                <li>• Skips  if <code className="px-1 py-0.5 rounded bg-zinc-200 dark:bg-zinc-800 font-mono text-xs">.agent/</code> already exists (use <code className="px-1 py-0.5 rounded bg-zinc-200 dark:bg-zinc-800 font-mono text-xs">--force</code> to override)</li>
                            </ul>
                        </div>
                    </div>

                    {/* update */}
                    <div>
                        <h3 className="text-xl font-semibold text-zinc-900 dark:text-zinc-50 mb-3">
                            <code className="font-mono">ag-kit update</code>
                        </h3>
                        <p className="text-base text-zinc-600 dark:text-zinc-400 mb-4">
                            Update your existing Antigravity Kit installation to the latest version.
                        </p>

                        <div className="relative group mb-4">
                            <pre className="p-4 rounded-lg bg-zinc-900 dark:bg-zinc-900 overflow-x-auto border border-zinc-800 font-mono text-sm">
                                <code className="text-zinc-100">ag-kit update</code>
                            </pre>
                        </div>

                        <div className="p-4 rounded-lg border border-amber-200 dark:border-amber-900 bg-amber-50 dark:bg-amber-950/20">
                            <p className="text-sm text-amber-900 dark:text-amber-200">
                                <strong className="font-semibold">Warning:</strong> This will delete and replace your <code className="px-1 py-0.5 rounded bg-amber-100 dark:bg-amber-900/40 font-mono text-xs">.agent/</code> folder. Make sure to backup any custom changes.
                            </p>
                        </div>
                    </div>

                    {/* status */}
                    <div>
                        <h3 className="text-xl font-semibold text-zinc-900 dark:text-zinc-50 mb-3">
                            <code className="font-mono">ag-kit status</code>
                        </h3>
                        <p className="text-base text-zinc-600 dark:text-zinc-400 mb-4">
                            Check the current installation status and version information.
                        </p>

                        <div className="relative group mb-4">
                            <pre className="p-4 rounded-lg bg-zinc-900 dark:bg-zinc-900 overflow-x-auto border border-zinc-800 font-mono text-sm">
                                <code className="text-zinc-100">ag-kit status</code>
                            </pre>
                        </div>

                        <div className="p-4 rounded-lg border border-zinc-200 dark:border-zinc-800 bg-zinc-50 dark:bg-zinc-900/50">
                            <div className="text-sm font-semibold text-zinc-900 dark:text-zinc-50 mb-2">Output Includes</div>
                            <ul className="text-sm text-zinc-600 dark:text-zinc-400 space-y-1">
                                <li>• Installation status (installed/not installed)</li>
                                <li>• Current version</li>
                                <li>• Agent count</li>
                                <li>• Skill count</li>
                                <li>• Workflow count</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>

            {/* Options */}
            <section className="mb-12">
                <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    Options
                </h2>
                <p className="text-base text-zinc-600 dark:text-zinc-400 mb-6">
                    Customize CLI behavior with these options:
                </p>

                <div className="overflow-x-auto">
                    <table className="w-full text-sm border border-zinc-200 dark:border-zinc-800">
                        <thead className="bg-zinc-50 dark:bg-zinc-900/50">
                            <tr>
                                <th className="text-left py-3 px-4 font-semibold text-zinc-900 dark:text-zinc-50 border-b border-zinc-200 dark:border-zinc-800">Option</th>
                                <th className="text-left py-3 px-4 font-semibold text-zinc-900 dark:text-zinc-50 border-b border-zinc-200 dark:border-zinc-800">Description</th>
                            </tr>
                        </thead>
                        <tbody className="divide-y divide-zinc-200 dark:divide-zinc-800">
                            <tr>
                                <td className="py-3 px-4">
                                    <code className="font-mono text-zinc-900 dark:text-zinc-50">--force</code>
                                </td>
                                <td className="py-3 px-4 text-zinc-600 dark:text-zinc-400">
                                    Overwrite existing <code className="px-1 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 font-mono text-xs">.agent</code> folder
                                </td>
                            </tr>
                            <tr>
                                <td className="py-3 px-4">
                                    <code className="font-mono text-zinc-900 dark:text-zinc-50">--path &lt;dir&gt;</code>
                                </td>
                                <td className="py-3 px-4 text-zinc-600 dark:text-zinc-400">
                                    Install in specific directory instead of current folder
                                </td>
                            </tr>
                            <tr>
                                <td className="py-3 px-4">
                                    <code className="font-mono text-zinc-900 dark:text-zinc-50">--branch &lt;name&gt;</code>
                                </td>
                                <td className="py-3 px-4 text-zinc-600 dark:text-zinc-400">
                                    Use specific Git branch (default: main)
                                </td>
                            </tr>
                            <tr>
                                <td className="py-3 px-4">
                                    <code className="font-mono text-zinc-900 dark:text-zinc-50">--quiet</code>
                                </td>
                                <td className="py-3 px-4 text-zinc-600 dark:text-zinc-400">
                                    Suppress output (useful for CI/CD pipelines)
                                </td>
                            </tr>
                            <tr>
                                <td className="py-3 px-4">
                                    <code className="font-mono text-zinc-900 dark:text-zinc-50">--dry-run</code>
                                </td>
                                <td className="py-3 px-4 text-zinc-600 dark:text-zinc-400">
                                    Preview actions without executing
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </section>

            {/* Examples */}
            <section className="mb-12">
                <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    Examples
                </h2>

                <div className="space-y-6">
                    <div>
                        <h3 className="text-base font-semibold text-zinc-900 dark:text-zinc-50 mb-2">
                            Force reinstall
                        </h3>
                        <div className="relative group">
                            <pre className="p-4 rounded-lg bg-zinc-900 dark:bg-zinc-900 overflow-x-auto border border-zinc-800 font-mono text-sm">
                                <code className="text-zinc-100">ag-kit init --force</code>
                            </pre>
                        </div>
                    </div>

                    <div>
                        <h3 className="text-base font-semibold text-zinc-900 dark:text-zinc-50 mb-2">
                            Install in specific directory
                        </h3>
                        <div className="relative group">
                            <pre className="p-4 rounded-lg bg-zinc-900 dark:bg-zinc-900 overflow-x-auto border border-zinc-800 font-mono text-sm">
                                <code className="text-zinc-100">ag-kit init --path ./my-project</code>
                            </pre>
                        </div>
                    </div>

                    <div>
                        <h3 className="text-base font-semibold text-zinc-900 dark:text-zinc-50 mb-2">
                            Use development branch
                        </h3>
                        <div className="relative group">
                            <pre className="p-4 rounded-lg bg-zinc-900 dark:bg-zinc-900 overflow-x-auto border border-zinc-800 font-mono text-sm">
                                <code className="text-zinc-100">ag-kit init --branch dev</code>
                            </pre>
                        </div>
                    </div>

                    <div>
                        <h3 className="text-base font-semibold text-zinc-900 dark:text-zinc-50 mb-2">
                            Silent install for CI/CD
                        </h3>
                        <div className="relative group">
                            <pre className="p-4 rounded-lg bg-zinc-900 dark:bg-zinc-900 overflow-x-auto border border-zinc-800 font-mono text-sm">
                                <code className="text-zinc-100">ag-kit init --quiet --force</code>
                            </pre>
                        </div>
                    </div>
                </div>
            </section>

            {/* Next Steps */}
            <section className="mb-12">
                <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    Next Steps
                </h2>
                <div className="grid gap-4 sm:grid-cols-2">
                    <Link
                        href="/brain/knowledge/docs_legacy/installation"
                        className="group p-6 rounded-lg border border-zinc-200 dark:border-zinc-800 hover:border-zinc-300 dark:hover:border-zinc-700 hover:bg-zinc-50 dark:hover:bg-zinc-900 transition-all"
                    >
                        <h3 className="font-semibold text-zinc-900 dark:text-zinc-50 mb-2">Installation Guide →</h3>
                        <p className="text-sm text-zinc-600 dark:text-zinc-400">
                            Full installation instructions
                        </p>
                    </Link>
                    <a
                        href="https://github.com/vudovn/antigravity-kit"
                        target="_blank"
                        rel="noopener noreferrer"
                        className="group p-6 rounded-lg border border-zinc-200 dark:border-zinc-800 hover:border-zinc-300 dark:hover:border-zinc-700 hover:bg-zinc-50 dark:hover:bg-zinc-900 transition-all"
                    >
                        <h3 className="font-semibold text-zinc-900 dark:text-zinc-50 mb-2">View on GitHub →</h3>
                        <p className="text-sm text-zinc-600 dark:text-zinc-400">
                            Source code and contribution guide
                        </p>
                    </a>
                </div>
            </section>

            {/* Footer Navigation */}
            <div className="pt-8 border-t border-zinc-200 dark:border-zinc-800 flex items-center justify-between">
                <Link
                    href="/brain/knowledge/docs_legacy/workflows"
                    className="text-sm font-medium text-zinc-900 dark:text-zinc-50 hover:underline flex items-center gap-1"
                >
                    <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
                    </svg>
                    Workflows
                </Link>
                <a
                    href="https://github.com/vudovn/antigravity-kit"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-sm font-medium text-zinc-900 dark:text-zinc-50 hover:underline flex items-center gap-1"
                >
                    GitHub
                    <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                    </svg>
                </a>
            </div>
        </div>
    );
}
```

## File: `web/src/app/brain/knowledge/docs_legacy/guide/examples/brainstorm/page.mdx`
```
export const metadata = {
  title: "Example: Structured Brainstorming | Antigravity Kit",
  description: "Learn how to use the /brainstorm workflow to explore multiple options before committing to an implementation.",
};

import { Callout, StepList, Step, Terminal, TerminalLine, TerminalBlock, ProTips, Tip, FeatureGrid, Feature } from '@/components/mdx'

# Structured Brainstorming

Explore multiple approaches before writing code with the `/brainstorm` workflow.

## Overview

The `/brainstorm` command activates a **structured ideation mode**.
Instead of jumping straight to code, the agent explores at least 3 different approaches,
analyzes pros and cons, and helps you make an informed decision.

<FeatureGrid>
  <Feature title="No Code" description="Ideas only" />
  <Feature title="3+ Options" description="Always compare" />
  <Feature title="Pros/Cons" description="Honest tradeoffs" />
  <Feature title="You Decide" description="Final choice" />
</FeatureGrid>

## The Process

<StepList>
  <Step number={1} title="Describe Your Challenge">
    Tell the agent what you want to explore. Be specific about constraints.

    ```bash
    /brainstorm authentication system for my SaaS app
    ```
  </Step>
  <Step number={2} title="Review Options">
    The agent presents 3+ approaches with pros, cons, and effort levels.
  </Step>
  <Step number={3} title="Make Decision">
    Choose an option, then use `/enhance` or `/create` to implement.
  </Step>
</StepList>

## Example Session

<Terminal>
  <TerminalLine type="user">/brainstorm state management for complex form</TerminalLine>

  <TerminalBlock>
    <TerminalLine type="agent">**Exploring Options...**</TerminalLine>
  </TerminalBlock>

  <div className="space-y-4 pl-8 mb-4">
    <div className="border-t border-zinc-800 pt-3">
      <strong className="text-purple-400">Option A: React Hook Form + Zod</strong>
      <div className="text-xs mt-1 space-y-1">
        <div className="text-green-400">✅ Minimal re-renders, great DX</div>
        <div className="text-red-400">❌ Learning curve</div>
        <div className="text-yellow-400">📊 Effort: Low</div>
      </div>
    </div>
    <div className="border-t border-zinc-800 pt-3">
      <strong className="text-purple-400">Option B: Zustand</strong>
      <div className="text-xs mt-1 space-y-1">
        <div className="text-green-400">✅ Full control, persists across routes</div>
        <div className="text-red-400">❌ More boilerplate</div>
        <div className="text-yellow-400">📊 Effort: Medium</div>
      </div>
    </div>
  </div>

  <TerminalBlock highlight>
    <TerminalLine type="agent">**💡 Recommendation: Option A**</TerminalLine>
    For 20+ fields, RHF minimizes re-renders.
  </TerminalBlock>
</Terminal>

## Pro Tips

<ProTips>
  <Tip title="Provide Context">
    Mention constraints: "I need SSR support", "Must work offline".
  </Tip>
  <Tip title="Ask Follow-ups">
    "Tell me more about Option B's scalability" before deciding.
  </Tip>
</ProTips>

## Next Steps

- Try `/brainstorm` for your next architecture decision
- After deciding, use [Add New Feature](/brain/knowledge/docs_legacy/guide/examples/new-feature) to implement
```

## File: `web/src/app/brain/knowledge/docs_legacy/guide/examples/create/page.mdx`
```
export const metadata = {
  title: "Example: Create New Application | Antigravity Kit",
  description: "Learn how to use the /create workflow to build new applications from scratch with AI-powered wizards.",
};

import { Callout, StepList, Step, Terminal, TerminalLine, TerminalBlock, ProTips, Tip } from '@/components/mdx'

# Create New Application

Build complete applications from scratch with the `/create` wizard.

## Overview

The `/create` command is your **application creation wizard**.
It guides you through an interactive dialogue, understands your requirements,
plans the architecture, and orchestrates specialist agents to build your app.

<Callout type="info">
  **From idea to running app:** Just describe what you want, and the wizard handles tech stack, file structure, database schema, and implementation.
</Callout>

## The Process

<StepList>
  <Step number={1} title="Describe Your App">
    Tell the wizard what you want to build. It will ask clarifying questions if needed.

    ```bash
    /create e-commerce site with product listing and cart
    ```
  </Step>
  <Step number={2} title="Review Plan">
    The `project-planner` agent creates a detailed plan. Approve to proceed.
  </Step>
  <Step number={3} title="Agents Build">
    Specialist agents work in parallel: database-architect, backend, frontend.
  </Step>
</StepList>

## Example Session

<Terminal>
  <TerminalLine type="user">/create todo app with dark mode</TerminalLine>

  <TerminalBlock>
    <TerminalLine type="agent">**Analyzing request...**</TerminalLine>
    Tech Stack: Next.js + Tailwind + Zustand
    <span className="text-yellow-300">Proceed? (Y/N)</span>
  </TerminalBlock>

  <TerminalLine type="user">Y</TerminalLine>

  <div className="space-y-2 pl-8 mb-4">
    <div className="flex items-center gap-2">
      <span className="w-2 h-2 rounded-full bg-blue-500 animate-pulse"></span>
      <span><strong>Backend:</strong> Creating store...</span>
    </div>
    <div className="flex items-center gap-2">
      <span className="w-2 h-2 rounded-full bg-pink-500 animate-pulse"></span>
      <span><strong>Frontend:</strong> Building components...</span>
    </div>
  </div>

  <TerminalBlock highlight>
    <TerminalLine type="agent">**🚀 App Created!**</TerminalLine>
    Preview: <span className="text-blue-400">http://localhost:3000</span>
  </TerminalBlock>
</Terminal>

## Pro Tips

<ProTips>
  <Tip title="Be Specific">
    "E-commerce with Stripe" beats "online store".
  </Tip>
  <Tip title="Start Simple">
    Create MVP first, use `/enhance` to iterate.
  </Tip>
</ProTips>

## Next Steps

- Run `/create` followed by your app idea
- Use [Add New Feature](/brain/knowledge/docs_legacy/guide/examples/new-feature) to extend
```

## File: `web/src/app/brain/knowledge/docs_legacy/guide/examples/debugging/page.mdx`
```
export const metadata = {
  title: "Example: Systematic Debugging | Antigravity Kit",
  description: "Learn how to solve complex issues using the /debug workflow's 4-phase investigation protocol.",
};

import { Callout, StepList, Step, Terminal, TerminalLine, TerminalBlock, ProTips, Tip } from '@/components/mdx'

# Systematic Debugging

Solve complex issues using the rigorous `/debug` workflow.

## Overview

The `/debug` workflow enforces a **4-phase investigation protocol** (Discovery, Hypothesis, Verification, Resolution). It prevents guess-driven development by requiring evidence before code changes.

<Callout type="info" title="When to use:">
  - "The login button does nothing"
  - "API returns 500 error intermittently"
  - "App crashes on mobile only"
</Callout>

## The Process

<StepList>
  <Step number={1} title="Discovery">
    Gathers facts: Error logs, user reports, reproduction steps.

    ```bash
    /debug Login returns 403 even with correct credentials
    ```
  </Step>
  <Step number={2} title="Hypothesis">
    Formulates potential causes prioritized by likelihood.
  </Step>
  <Step number={3} title="Verification">
    Systematically tests each hypothesis using scripts or logs.
  </Step>
  <Step number={4} title="Resolution">
    Implements the fix and adds a regression test.
  </Step>
</StepList>

## Example Session

<Terminal>
  <TerminalLine type="user">/debug Form submission fails silently</TerminalLine>

  <TerminalBlock>
    <TerminalLine type="agent">**Phase 1: Discovery**</TerminalLine>
    Reading `CheckoutForm.tsx`... Found `handleSubmit`.
    <span className="text-red-400">ERROR: Cannot read properties of undefined</span>
  </TerminalBlock>

  <TerminalBlock>
    <TerminalLine type="agent">**Phase 2: Hypothesis**</TerminalLine>
    <div className="text-xs mt-1">
      1. `emailRef.current` is null on mount<br/>
      2. Event handler not bound correctly
    </div>
  </TerminalBlock>

  <TerminalBlock highlight>
    <TerminalLine type="agent">**Phase 4: Resolution**</TerminalLine>
    Fix applied: Added null check to `emailRef`.
    <span className="text-green-400">✅ Test passed: Form submits successfully.</span>
  </TerminalBlock>
</Terminal>

## Pro Tips

<ProTips>
  <Tip title="Provide Context">
    Paste the exact error message or stack trace for faster discovery.
  </Tip>
  <Tip title="Trust, Verify">
    Ask the agent to run the reproduction case again to confirm it's solved.
  </Tip>
</ProTips>

## Next Steps

- Try `/debug` on an existing bug
- See [Deployment](/brain/knowledge/docs_legacy/guide/examples/deployment) to ship your fix
```

## File: `web/src/app/brain/knowledge/docs_legacy/guide/examples/deployment/page.mdx`
```
export const metadata = {
  title: "Example: Production Deployment | Antigravity Kit",
  description: "Learn how to strictly and safely deploy applications using the /deploy workflow.",
};

import { Callout, StepList, Step, Terminal, TerminalLine, TerminalBlock, ProTips, Tip } from '@/components/mdx'

# Production Deployment

Ship with confidence using the safety-first `/deploy` workflow.

## Overview

The `/deploy` command is an **Audit & Release Conductor**.
It forces your code to pass a rigorous health check before deployment.

<Callout type="info" title="It stops you from deploying if:">
  - Security vulnerabilities are found
  - Linting errors exist
  - TypeScript types are invalid
  - Critical tests fail
</Callout>

## The Process

<StepList>
  <Step number={1} title="Execute Command">
    When your code is ready, trigger the deployment pipeline.

    ```bash
    /deploy
    ```
  </Step>
  <Step number={2} title="Pre-Flight Checklist">
    The agent automatically audits your project health.

    <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
      <div className="bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-lg p-3">
        <h4 className="text-sm font-semibold mb-1">🛡️ Security</h4>
        <p className="text-xs text-zinc-500 dark:text-zinc-400 m-0">Scans for vulnerabilities & secrets</p>
      </div>
      <div className="bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-lg p-3">
        <h4 className="text-sm font-semibold mb-1">📋 Quality</h4>
        <p className="text-xs text-zinc-500 dark:text-zinc-400 m-0">Enforces Linting & Type Safety</p>
      </div>
    </div>
  </Step>
  <Step number={3} title="Release">
    If checks pass, it builds and pushes to your platform (Vercel, Docker, etc).
  </Step>
</StepList>

## Example Session

<Terminal>
  <TerminalLine type="user">/deploy</TerminalLine>

  <TerminalBlock>
    <TerminalLine type="agent">**Running Pre-Flight Checks...**</TerminalLine>
    <div className="space-y-1 mt-2">
      <div>🔄 Security Scan... <span className="text-green-400">PASSED</span></div>
      <div>🔄 Lint Check... <span className="text-green-400">PASSED</span></div>
      <div>🔄 Type Validation... <span className="text-green-400">PASSED</span></div>
    </div>
    <br/>
    <span className="text-green-400">✅ All checks passed!</span>
    Deploying to Vercel...
  </TerminalBlock>

  <TerminalBlock highlight>
    <TerminalLine type="agent">**🚀 Deployment Complete!**</TerminalLine>
    <div className="space-y-1 mt-2">
      <div>🌐 URL: <span className="text-blue-400">https://my-app.vercel.app</span></div>
      <div>💚 Health Check: <span className="text-green-400">OK</span></div>
    </div>
  </TerminalBlock>
</Terminal>

## Pro Tips

<ProTips>
  <Tip title="Check First">
    Run `/deploy check` to dry-run validations without deploying.
  </Tip>
  <Tip title="Rollback Safety">
    Use `/deploy rollback` to instantly revert to the last stable version.
  </Tip>
</ProTips>

## Next Steps

- Try `/deploy check` to run pre-flight checks
- Learn about [Multi-Agent Orchestration](/brain/knowledge/docs_legacy/guide/examples/orchestration)
```

## File: `web/src/app/brain/knowledge/docs_legacy/guide/examples/new-feature/page.mdx`
```
export const metadata = {
  title: "Example: Add a New Feature | Antigravity Kit",
  description: "Step-by-step guide on adding new features to an existing application using Antigravity Kit workflows.",
};

import { Callout, StepList, Step, Terminal, TerminalLine, TerminalBlock, ProTips, Tip } from '@/components/mdx'

# Add a New Feature

Learn how to safely add complex features to an existing codebase using the `/enhance` workflow.

## Overview

The `/enhance` workflow is your day-to-day tool for iterative development.
Unlike `/create` which builds from scratch, `/enhance` focuses on surgically adding functionality without breaking existing code.

<Callout type="info">
  **Scenario:** Adding a "Dashboard Analytics" feature to an existing SaaS application.
</Callout>

## The Process

<StepList>
  <Step number={1} title="Feature Planning">
    Describe your feature requirements clearly.

    ```bash
    /enhance Add an analytics dashboard for user activity
    Requirements:
    - Track daily active users and page views
    - Visual charts using Recharts
    - API endpoint to aggregate data
    ```
  </Step>
  <Step number={2} title="Component Implementation">
    Specialists implement the full vertical slice.

    <div className="grid grid-cols-2 md:grid-cols-4 gap-3 mt-4">
      <div className="bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-lg p-3 text-center">
        <div className="text-xs font-semibold">Database</div>
      </div>
      <div className="bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-lg p-3 text-center">
        <div className="text-xs font-semibold">Backend</div>
      </div>
      <div className="bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-lg p-3 text-center">
        <div className="text-xs font-semibold">Frontend</div>
      </div>
      <div className="bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-lg p-3 text-center">
        <div className="text-xs font-semibold">Testing</div>
      </div>
    </div>
  </Step>
  <Step number={3} title="Verify Integration">
    Run `final checks` to validate bundle size, accessibility, and tests.
  </Step>
</StepList>

## Example Session

<Terminal>
  <TerminalLine type="user">/enhance add dark mode toggle</TerminalLine>

  <TerminalBlock>
    <TerminalLine type="agent">**Analyzing codebase...**</TerminalLine>
    <div className="text-xs mt-2">
      Found: Tailwind CSS with no dark mode config<br/>
      Plan: Update tailwind.config, add ThemeProvider, create toggle component
    </div>
  </TerminalBlock>

  <div className="space-y-2 pl-8 mb-4">
    <div className="flex items-center gap-2">
      <span className="w-2 h-2 rounded-full bg-purple-500 animate-pulse"></span>
      <span><strong>Frontend:</strong> Creating ThemeToggle...</span>
    </div>
    <div className="flex items-center gap-2">
      <span className="w-2 h-2 rounded-full bg-green-500 animate-pulse"></span>
      <span><strong>Testing:</strong> Adding theme tests...</span>
    </div>
  </div>

  <TerminalBlock highlight>
    <TerminalLine type="agent">**✅ Feature Added!**</TerminalLine>
    <span className="text-zinc-400">Run `/preview start` to test.</span>
  </TerminalBlock>
</Terminal>

## Pro Tips

<ProTips>
  <Tip title="Check Dependencies">
    Use `checklist.py` to prevent bundle bloat from new libraries.
  </Tip>
  <Tip title="Keep It Modular">
    Isolate new components to minimize side effects on existing code.
  </Tip>
</ProTips>

## Next Steps

- Try `/enhance` in your project
- See [Test Generation](/brain/knowledge/docs_legacy/guide/examples/test) for coverage
```

## File: `web/src/app/brain/knowledge/docs_legacy/guide/examples/orchestration/page.mdx`
```
export const metadata = {
  title: "Example: Multi-Agent Orchestration | Antigravity Kit",
  description: "Learn how to coordinate multiple specialist agents for complex projects using the /orchestrate workflow.",
};

import { Callout, StepList, Step, Terminal, TerminalLine, TerminalBlock, ProTips, Tip, FeatureGrid, Feature } from '@/components/mdx'

# Multi-Agent Orchestration

Build entire SaaS platforms by coordinating specialist agents with the `/orchestrate` workflow.

## Overview

Most AI interactions are 1-on-1. The `orchestrator` agent changes this by acting as a **Project Manager**.
It breaks down a large request (e.g., "Build a SaaS MVP") into tasks and assigns them to the best specialist for the job.

<FeatureGrid>
  <Feature title="Backend" description="API & DB Architect" />
  <Feature title="Frontend" description="UI/UX Specialist" />
  <Feature title="Security" description="Safety Auditor" />
  <Feature title="QA" description="Test Engineer" />
</FeatureGrid>

## The Process

<StepList>
  <Step number={1} title="Project Brief">
    Describe the high-level goal. The orchestrator will interview you to clarify requirements.

    ```bash
    /orchestrate Build a "Course Platform" MVP with:
    - User Authentication (NextAuth)
    - Stripe Payments
    - Video Hosting (Mux)
    - Dashboard for Instructors
    ```
  </Step>
  <Step number={2} title="Phase 1: Planning">
    The `project-planner` agent creates a detailed roadmap (`PLAN.md`).

    <div className="bg-zinc-50 dark:bg-zinc-900 p-3 rounded-lg text-xs font-mono border-l-2 border-blue-500 mt-2">
      ...<br/>
      ### 2.1 Database Schema<br/>
      - Users (id, email, role)<br/>
      - Courses (id, title, price)<br/>
      ...
    </div>
  </Step>
  <Step number={3} title="Phase 2: Execution">
    Agents work in parallel. The Orchestrator monitors progress and unblocks dependencies.
  </Step>
</StepList>

## Example Session

<Terminal>
  <TerminalLine type="user">/orchestrate Build E-commerce MVP</TerminalLine>

  <TerminalBlock>
    <TerminalLine type="agent">**Activating Squad...**</TerminalLine>
    Assigning tasks based on `PLAN.md`:
  </TerminalBlock>

  <div className="space-y-3 pl-8">
    <div className="flex items-center gap-2">
      <span className="w-2 h-2 rounded-full bg-yellow-500 animate-pulse"></span>
      <span><strong>Backend-Specialist:</strong> Configuring Prisma Schema...</span>
    </div>
    <div className="flex items-center gap-2">
      <span className="w-2 h-2 rounded-full bg-blue-500 animate-pulse"></span>
      <span><strong>Frontend-Specialist:</strong> Building ProductCard component...</span>
    </div>
    <div className="flex items-center gap-2">
      <span className="w-2 h-2 rounded-full bg-purple-500 animate-pulse"></span>
      <span><strong>Security-Auditor:</strong> Reviewing auth flow...</span>
    </div>
  </div>

  <TerminalBlock highlight>
    <TerminalLine type="agent">**✅ Project Complete!**</TerminalLine>
    All tasks finished. Run `npm run dev` to start.
  </TerminalBlock>
</Terminal>

## Pro Tips

<ProTips>
  <Tip title="Start Small">
    Don't try to build Facebook in one go. Orchestrate an MVP first, then use `/enhance` to iterate.
  </Tip>
  <Tip title="Define Auth">
    Always specify how users log in (e.g., "Use NextAuth with Google"). It's a key architectural decision.
  </Tip>
</ProTips>

## Next Steps

- Learn about [Systematic Debugging](/brain/knowledge/docs_legacy/guide/examples/debugging) to maintain your complex app
- See [Deployment](/brain/knowledge/docs_legacy/guide/examples/deployment) to ship your MVP
```

## File: `web/src/app/brain/knowledge/docs_legacy/guide/examples/plan/page.mdx`
```
export const metadata = {
  title: "Example: Project Planning | Antigravity Kit",
  description: "Learn how to use the /plan workflow to create detailed project plans before implementation.",
};

import { Callout, StepList, Step, Terminal, TerminalLine, TerminalBlock, ProTips, Tip } from '@/components/mdx'

# Project Planning

Create detailed implementation plans before writing code with the `/plan` workflow.

## Overview

The `/plan` command activates **planning-only mode**.
It uses the `project-planner` agent to create a detailed plan file without writing any code.

<Callout type="info">
  **Critical Rule:** NO CODE is written during planning. Only `PLAN.md` is created.
</Callout>

## The Process

<StepList>
  <Step number={1} title="Describe Your Project">
    Tell the planner what you want to build.

    ```bash
    /plan e-commerce site with cart and checkout
    ```
  </Step>
  <Step number={2} title="Socratic Questions">
    The planner asks clarifying questions before creating the plan.
  </Step>
  <Step number={3} title="Plan Generated">
    Creates `brain/knowledge/docs_legacy/PLAN-{slug}.md` with tasks and agent assignments.
  </Step>
</StepList>

## Example Session

<Terminal>
  <TerminalLine type="user">/plan SaaS dashboard with analytics</TerminalLine>

  <TerminalBlock>
    <TerminalLine type="agent">**Clarifying Questions:**</TerminalLine>
    <div className="text-yellow-300 text-xs mt-2">
      1. What metrics? (users, revenue?)<br/>
      2. Real-time or daily?<br/>
      3. Charting library?
    </div>
  </TerminalBlock>

  <TerminalLine type="user">Users + revenue, real-time, Recharts</TerminalLine>

  <TerminalBlock highlight>
    <TerminalLine type="agent">**✅ Plan Created!**</TerminalLine>
    `brain/knowledge/docs_legacy/PLAN-saas-dashboard.md`<br/>
    <span className="text-zinc-400">Run `/create` to implement.</span>
  </TerminalBlock>
</Terminal>

## Pro Tips

<ProTips>
  <Tip title="Answer Thoroughly">
    The more context you provide, the better the plan.
  </Tip>
  <Tip title="Edit the Plan">
    Modify the generated plan before implementation.
  </Tip>
</ProTips>

## Next Steps

- Run `/plan` for your next major feature
- After planning, use [Create Application](/brain/knowledge/docs_legacy/guide/examples/create) to implement
```

## File: `web/src/app/brain/knowledge/docs_legacy/guide/examples/preview/page.mdx`
```
export const metadata = {
  title: "Example: Preview Management | Antigravity Kit",
  description: "Learn how to use the /preview workflow to manage your local development server.",
};

import { Callout, StepList, Step, Terminal, TerminalLine, TerminalBlock, ProTips, Tip, FeatureGrid, Feature } from '@/components/mdx'

# Preview Management

Manage your local development server with the `/preview` workflow.

## Overview

The `/preview` command manages your local development server.
Start, stop, restart, or check the status with simple commands.

<FeatureGrid>
  <Feature title="start" description="Launch server" />
  <Feature title="stop" description="Kill server" />
  <Feature title="restart" description="Reload" />
  <Feature title="check" description="Health" />
</FeatureGrid>

## The Process

<StepList>
  <Step number={1} title="Start Server">
    ```bash
    /preview start
    ```
  </Step>
  <Step number={2} title="Check Status">
    ```bash
    /preview
    ```
  </Step>
  <Step number={3} title="Stop Server">
    ```bash
    /preview stop
    ```
  </Step>
</StepList>

## Example Session

<Terminal>
  <TerminalLine type="user">/preview start</TerminalLine>

  <TerminalBlock>
    <TerminalLine type="agent">**🚀 Starting preview...**</TerminalLine>
    <div className="text-xs mt-2">
      Port: 3000<br/>
      Type: Next.js
    </div>
  </TerminalBlock>

  <TerminalBlock highlight>
    <TerminalLine type="agent">**✅ Preview ready!**</TerminalLine>
    URL: <span className="text-blue-400">http://localhost:3000</span>
  </TerminalBlock>
</Terminal>

## Pro Tips

<ProTips>
  <Tip title="Auto-detection">
    Automatically detects Next.js, Vite, etc.
  </Tip>
  <Tip title="Port Conflict">
    Suggests alternatives if port 3000 is busy.
  </Tip>
</ProTips>

## Next Steps

- Run `/preview start` to launch your dev server
- See [Deployment](/brain/knowledge/docs_legacy/guide/examples/deployment) to go live
```

## File: `web/src/app/brain/knowledge/docs_legacy/guide/examples/status/page.mdx`
```
export const metadata = {
  title: "Example: Project Status | Antigravity Kit",
  description: "Learn how to use the /status workflow to view your project and agent status at a glance.",
};

import { Callout, StepList, Step, Terminal, TerminalLine, TerminalBlock, ProTips, Tip, FeatureGrid, Feature } from '@/components/mdx'

# Project Status

Get a complete overview of your project with the `/status` workflow.

## Overview

The `/status` command gives you a **complete dashboard view** of your project.
See project info, tech stack, completed features, agent activity, and preview status.

<FeatureGrid>
  <Feature title="Project" description="Info & Stack" />
  <Feature title="Agents" description="Status Board" />
  <Feature title="Files" description="Statistics" />
  <Feature title="Preview" description="Health Check" />
</FeatureGrid>

## The Process

<StepList>
  <Step number={1} title="Run Command">
    Simply run the command to see your project dashboard.

    ```bash
    /status
    ```
  </Step>
</StepList>

## Example Session

<Terminal>
  <TerminalLine type="user">/status</TerminalLine>

  <TerminalBlock>
    <div className="text-yellow-400 mb-2">=== Project Status ===</div>
    <div className="space-y-1 mb-4">
      <div>📁 Project: my-ecommerce</div>
      <div>🏷️ Type: nextjs-ecommerce</div>
      <div>📄 Files: 73 created, 12 modified</div>
    </div>

    <div className="text-yellow-400 mb-2">=== Agent Status ===</div>
    <div className="space-y-1 mb-4">
      <div><span className="text-green-400">✅</span> database-architect → Completed</div>
      <div><span className="text-green-400">✅</span> backend-specialist → Completed</div>
      <div><span className="text-blue-400">🔄</span> frontend-specialist → 60%</div>
    </div>

    <div className="text-yellow-400 mb-2">=== Preview ===</div>
    <div className="space-y-1">
      <div>🌐 URL: <span className="text-blue-400">http://localhost:3000</span></div>
      <div>💚 Health: <span className="text-green-400">OK</span></div>
    </div>
  </TerminalBlock>
</Terminal>

## Pro Tips

<ProTips>
  <Tip title="Before Deploy">
    Check status to ensure all agents completed.
  </Tip>
  <Tip title="Track Progress">
    Monitor multi-agent orchestration in real-time.
  </Tip>
</ProTips>

## Next Steps

- Run `/status` to check project state
- See [Deployment](/brain/knowledge/docs_legacy/guide/examples/deployment) when ready to ship
```

## File: `web/src/app/brain/knowledge/docs_legacy/guide/examples/test/page.mdx`
```
export const metadata = {
  title: "Example: Test Generation & Execution | Antigravity Kit",
  description: "Learn how to use the /test workflow to generate and run tests for your code.",
};

import { Callout, StepList, Step, Terminal, TerminalLine, TerminalBlock, ProTips, Tip, FeatureGrid, Feature } from '@/components/mdx'

# Test Generation & Execution

Generate and run tests with the `/test` workflow.

## Overview

The `/test` command handles **test generation and execution**.
Analyze code, create test suites, run tests, or check coverage.

<FeatureGrid>
  <Feature title="run" description="Execute tests" />
  <Feature title="generate" description="Create tests" />
  <Feature title="coverage" description="Report" />
  <Feature title="watch" description="Live mode" />
</FeatureGrid>

## The Process

<StepList>
  <Step number={1} title="Run All Tests">
    ```bash
    /test
    ```
  </Step>
  <Step number={2} title="Generate Tests for File">
    ```bash
    /test src/auth.ts
    ```
  </Step>
  <Step number={3} title="Check Coverage">
    ```bash
    /test coverage
    ```
  </Step>
</StepList>

## Example Session

<Terminal>
  <TerminalLine type="user">/test src/services/auth.ts</TerminalLine>

  <TerminalBlock>
    <TerminalLine type="agent">**Analyzing auth.ts...**</TerminalLine>
    <div className="text-xs mt-2">
      Found 4 functions: login, register, verifyToken, resetPassword
    </div>
  </TerminalBlock>

  <TerminalBlock highlight>
    <TerminalLine type="agent">**✅ Tests Generated!**</TerminalLine>
    <div className="text-xs mt-2">
      Created: `tests/auth.test.ts`<br/>
      Test cases: 12<br/>
      Coverage: 95%
    </div>
  </TerminalBlock>
</Terminal>

## Pro Tips

<ProTips>
  <Tip title="Test Behavior">
    Focus on what functions do, not implementation.
  </Tip>
  <Tip title="Edge Cases">
    Always test errors, empty inputs, boundaries.
  </Tip>
</ProTips>

## Next Steps

- Run `/test` to execute your test suite
- See [Deployment](/brain/knowledge/docs_legacy/guide/examples/deployment) which runs tests automatically
```

## File: `web/src/app/brain/knowledge/docs_legacy/guide/examples/ui-design/page.mdx`
```
export const metadata = {
  title: "Example: Advanced UI Design | Antigravity Kit",
  description: "Learn how to build high-conversion landing pages using the /ui-ux-pro-max workflow and style prompts.",
};

import { Callout, StepList, Step, Terminal, TerminalLine, TerminalBlock, ProTips, Tip } from '@/components/mdx'

# Advanced UI Design

Create stunning, high-conversion landing pages instantly with the `/ui-ux-pro-max` workflow.

## Overview

This is a standardized workflow designed specifically for **Rapid Landing Page Development**.

<Callout type="info">
  **Powered by NextLevelBuilder:** This workflow is optimized to work with the curated style prompts from [nextlevelbuilder.io](https://ui-ux-pro-max-skill.nextlevelbuilder.io/#styles). You pick a style, and the AI handles the execution.
</Callout>

## The Process

<StepList>
  <Step number={1} title="Choose Your Style">
    Visit [nextlevelbuilder.io](https://ui-ux-pro-max-skill.nextlevelbuilder.io/#styles) and copy a style prompt (e.g., "Modern SaaS - Dark Mode").
  </Step>
  <Step number={2} title="Run the Command">
    Paste the style prompt and your content requirements.

    ```bash
    /ui-ux-pro-max Create a friendly pet grooming service landing page with claymorphism cards,
    service packages, pet gallery, booking system, and testimonials from pet owners.
    Use playful warm colors.
    ```
  </Step>
  <Step number={3} title="The Construction">
    The agent automatically builds the entire page structure.

    <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-4">
      <div className="bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-lg p-3">
        <h4 className="text-sm font-semibold mb-1">📐 Structure</h4>
        <p className="text-xs text-zinc-500 dark:text-zinc-400 m-0">Semantic HTML5 & SEO hierarchy</p>
      </div>
      <div className="bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-lg p-3">
        <h4 className="text-sm font-semibold mb-1">🧩 Components</h4>
        <p className="text-xs text-zinc-500 dark:text-zinc-400 m-0">Reusable, accessible UI blocks</p>
      </div>
      <div className="bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-lg p-3">
        <h4 className="text-sm font-semibold mb-1">✨ Interactivity</h4>
        <p className="text-xs text-zinc-500 dark:text-zinc-400 m-0">Micro-animations & responsiveness</p>
      </div>
    </div>
  </Step>
</StepList>

## Example Session

<Terminal>
  <TerminalLine type="user">/ui-ux-pro-max Create a friendly pet grooming service landing page with claymorphism cards, service packages, pet gallery, booking system, and testimonials from pet owners. Use playful warm colors</TerminalLine>

  <TerminalBlock>
    <TerminalLine type="agent">**Analyzing Style...**</TerminalLine>
    Loading "Modern SaaS"...<br/>
    <div className="text-xs text-zinc-500 mt-2">
      <div>🎨 <strong>Colors:</strong> Indigo-500 primary, Slate-900 bg</div>
      <div>✨ <strong>Effects:</strong> Glassmorphism cards</div>
    </div>
  </TerminalBlock>

  <TerminalBlock highlight>
    <TerminalLine type="agent">**✅ Page Complete!**</TerminalLine>
    Created `app/page.tsx`<br/>
    <span className="text-green-400">Run `/preview start` to view.</span>
  </TerminalBlock>
</Terminal>

## Pro Tips

<ProTips>
  <Tip title="Be Specific">
    Instead of "nice design", use "glassmorphism dark mode with neon accents".
  </Tip>
  <Tip title="List Sections">
    Explicitly list "Hero, Features, Pricing, FAQ" to ensure a complete layout.
  </Tip>
</ProTips>

## Next Steps

- Browse styles at [NextLevelBuilder Style Gallery](https://ui-ux-pro-max-skill.nextlevelbuilder.io/#styles)
- See [Production Deployment](/brain/knowledge/docs_legacy/guide/examples/deployment) to ship your page
```

## File: `web/src/app/brain/knowledge/docs_legacy/installation/page.tsx`
```tsx
import Link from "next/link";
import { Callout } from "@/components/mdx";

export const metadata = {
  title: "Installation | Antigravity Kit",
  description: "Get started with Antigravity Kit in under a minute.",
};

export default function InstallationPage() {
  return (
    <div className="max-w-3xl">
      <nav className="flex items-center gap-2 text-sm text-zinc-600 dark:text-zinc-400 mb-6">
        <Link href="/docs" className="hover:text-zinc-900 dark:hover:text-zinc-50">Docs</Link>
        <span>/</span>
        <span className="text-zinc-900 dark:text-zinc-50">Installation</span>
      </nav>

      <div className="mb-8 pb-8 border-b border-zinc-200 dark:border-zinc-800">
        <h1 className="text-4xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
          Installation
        </h1>
        <p className="text-lg text-zinc-600 dark:text-zinc-400">
          Get started with Antigravity Kit in under a minute.
        </p>
      </div>

      <section id="quick-start" className="mb-12 scroll-mt-16">
        <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
          Quick Start
        </h2>
        <p className="text-base text-zinc-600 dark:text-zinc-400 mb-6">
          The fastest way to install Antigravity Kit is using <code className="px-1.5 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-sm font-mono">npx</code> in root project:
        </p>

        <pre className="p-4 rounded-lg bg-zinc-900 overflow-x-auto mb-4 text-sm font-mono text-zinc-100">
          npx @vudovn/ag-kit init
        </pre>

        <Callout type="info">
          <strong>Note:</strong> This command will create a <code>.agent</code> folder in your current directory containing all templates.
        </Callout>
      </section>

      <section id="global-install" className="mb-12 scroll-mt-16">
        <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
          Global Installation
        </h2>
        <p className="text-base text-zinc-600 dark:text-zinc-400 mb-6">
          Install the CLI globally to use <code className="px-1.5 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-sm font-mono">ag-kit</code> command anywhere:
        </p>

        <pre className="p-4 rounded-lg bg-zinc-900 overflow-x-auto mb-2 text-sm font-mono text-zinc-100">
          npm install -g @vudovn/ag-kit
        </pre>

        <pre className="p-4 rounded-lg bg-zinc-900 overflow-x-auto mb-4 text-sm font-mono text-zinc-100">
          cd your-project && ag-kit init
        </pre>

        <p className="text-sm text-zinc-600 dark:text-zinc-400 mb-4">
          Read other commands in <Link className="text-blue-500 hover:text-blue-600 dark:text-blue-400 dark:hover:text-blue-300" href="/brain/knowledge/docs_legacy/cli">CLI commands</Link> documentation.
        </p>
      </section>

      <section id="structure" className="mb-12 scroll-mt-16">
        <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
          What Gets Installed
        </h2>
        <p className="text-base text-zinc-600 dark:text-zinc-400 mb-6">
          After running the installation command, you'll have the following structure:
        </p>

        <pre className="p-4 rounded-lg bg-zinc-900 overflow-x-auto mb-4 text-sm font-mono text-zinc-100">
{`.agent/
├── agents/          # 16 Specialist Agents
├── skills/          # 40+ Skills
├── workflows/       # 11 Slash Commands
├── rules/           # Workspace Rules
└── ARCHITECTURE.md  # Full documentation`}
        </pre>

        <div className="space-y-4">
          <div className="p-4 rounded-lg border border-zinc-200 dark:border-zinc-800">
            <h3 className="font-semibold text-zinc-900 dark:text-zinc-50 mb-2">agents/</h3>
            <p className="text-sm text-zinc-600 dark:text-zinc-400">
              Contains 16 specialist AI agent configurations for different domains (frontend, backend, security, etc.)
            </p>
          </div>
          <div className="p-4 rounded-lg border border-zinc-200 dark:border-zinc-800">
            <h3 className="font-semibold text-zinc-900 dark:text-zinc-50 mb-2">skills/</h3>
            <p className="text-sm text-zinc-600 dark:text-zinc-400">
              40+ domain-specific knowledge modules that agents can use
            </p>
          </div>
          <div className="p-4 rounded-lg border border-zinc-200 dark:border-zinc-800">
            <h3 className="font-semibold text-zinc-900 dark:text-zinc-50 mb-2">workflows/</h3>
            <p className="text-sm text-zinc-600 dark:text-zinc-400">
              11 slash command procedures for common development tasks
            </p>
          </div>
          <div className="p-4 rounded-lg border border-zinc-200 dark:border-zinc-800">
            <h3 className="font-semibold text-zinc-900 dark:text-zinc-50 mb-2">rules/</h3>
            <p className="text-sm text-zinc-600 dark:text-zinc-400">
              Workspace configuration including <code className="px-1 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 font-mono text-xs">GEMINI.md</code> for behavior rules
            </p>
          </div>
        </div>
      </section>

      <section id="requirements" className="mb-12 scroll-mt-16">
        <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
          System Requirements
        </h2>
        <ul className="space-y-2 text-base text-zinc-600 dark:text-zinc-400 mb-6">
          <li className="flex items-start gap-2">
            <svg className="w-5 h-5 text-green-600 dark:text-green-500 mt-0.5 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
            </svg>
            <span>Node.js 16.0 or later</span>
          </li>
          <li className="flex items-start gap-2">
            <svg className="w-5 h-5 text-green-600 dark:text-green-500 mt-0.5 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
            </svg>
            <span>npm or yarn package manager</span>
          </li>
          <li className="flex items-start gap-2">
            <svg className="w-5 h-5 text-green-600 dark:text-green-500 mt-0.5 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
            </svg>
            <span>Git (for updates and version control)</span>
          </li>
        </ul>
      </section>

      <section className="mb-12">
        <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
          Next Steps
        </h2>
        <p className="text-base text-zinc-600 dark:text-zinc-400 mb-6">
          Now that you have Antigravity Kit installed, learn about the core concepts:
        </p>
        <div className="grid gap-4 sm:grid-cols-2">
          <Link
            href="/brain/knowledge/docs_legacy/agents"
            className="group p-6 rounded-lg border border-zinc-200 dark:border-zinc-800 hover:border-zinc-300 dark:hover:border-zinc-700 hover:bg-zinc-50 dark:hover:bg-zinc-900 transition-all"
          >
            <h3 className="font-semibold text-zinc-900 dark:text-zinc-50 mb-2">Agents →</h3>
            <p className="text-sm text-zinc-600 dark:text-zinc-400">
              Learn about specialist AI agents
            </p>
          </Link>
          <Link
            href="/brain/knowledge/docs_legacy/skills"
            className="group p-6 rounded-lg border border-zinc-200 dark:border-zinc-800 hover:border-zinc-300 dark:hover:border-zinc-700 hover:bg-zinc-50 dark:hover:bg-zinc-900 transition-all"
          >
            <h3 className="font-semibold text-zinc-900 dark:text-zinc-50 mb-2">Skills →</h3>
            <p className="text-sm text-zinc-600 dark:text-zinc-400">
              Discover 40+ domain-specific skills
            </p>
          </Link>
        </div>
      </section>

      <div className="pt-8 border-t border-zinc-200 dark:border-zinc-800 flex items-center justify-between">
        <Link
          href="/docs"
          className="text-sm font-medium text-zinc-900 dark:text-zinc-50 hover:underline flex items-center gap-1"
        >
          <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
          </svg>
          Introduction
        </Link>
        <Link
          href="/brain/knowledge/docs_legacy/agents"
          className="text-sm font-medium text-zinc-900 dark:text-zinc-50 hover:underline flex items-center gap-1"
        >
          Agents
          <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
          </svg>
        </Link>
      </div>
    </div>
  );
}
```

## File: `web/src/app/brain/knowledge/docs_legacy/skills/page.tsx`
```tsx
import { Lightbulb } from "lucide-react";
import Link from "next/link";
import skillsData from "@/services/skills.json";

export default function SkillsPage() {
    // Group skills by category
    const skillsByCategory = skillsData.reduce((acc, skill) => {
        if (!acc[skill.category]) {
            acc[skill.category] = [];
        }
        acc[skill.category].push(skill);
        return acc;
    }, {} as Record<string, typeof skillsData>);

    // Order of categories to display
    const categoryOrder = [
        "Frontend & UI",
        "Backend & API",
        "Database",
        "TypeScript/JavaScript",
        "Cloud & Infrastructure",
        "Testing & Quality",
        "Security",
        "Architecture & Planning",
        "Mobile",
        "Game Development",
        "SEO & Growth",
        "Shell/CLI",
        "Other"
    ];

    return (
        <div className="max-w-3xl">
            {/* Breadcrumb */}
            <nav className="flex items-center gap-2 text-sm text-zinc-600 dark:text-zinc-400 mb-6">
                <Link href="/docs" className="hover:text-zinc-900 dark:hover:text-zinc-50">Docs</Link>
                <span>/</span>
                <span className="text-zinc-900 dark:text-zinc-50">Skills</span>
            </nav>

            {/* Page Header */}
            <div className="mb-8 pb-8 border-b border-zinc-200 dark:border-zinc-800">
                <h1 className="text-4xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    Skills
                </h1>
                <p className="text-lg text-zinc-600 dark:text-zinc-400">
                    Domain-specific knowledge modules that agents load automatically.
                </p>
            </div>

            {/* What are Skills */}
            <section className="mb-12">
                <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    What are Skills?
                </h2>
                <p className="text-base text-zinc-600 dark:text-zinc-400 mb-4">
                    Skills are modular knowledge packages that contain principles, patterns, and decision-making frameworks for specific domains. They're loaded automatically when an agent needs them.
                </p>
                <p className="text-base text-zinc-600 dark:text-zinc-400 mb-6">
                    Unlike hard-coded templates, skills teach <em>principles</em> — enabling agents to make contextual decisions rather than copying patterns.
                </p>
                <div className="mt-2 p-4 rounded-lg border border-blue-200 dark:border-blue-900 bg-blue-50 dark:bg-blue-950/20 mb-6">
                    <p className="text-sm text-blue-900 dark:text-blue-100 mb-0">
                        <Lightbulb className="w-4 h-4 inline" />
                        <strong className="font-semibold"> Note:</strong> Skills are loaded on-demand based on task context. You don't need to configure anything manually.
                    </p>
                </div>
            </section>

            {/* How Skills Work */}
            <section className="mb-12">
                <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    How Skills Work
                </h2>
                <p className="text-base text-zinc-600 dark:text-zinc-400 mb-6">
                    When you invoke an agent, it automatically loads relevant skills based on:
                </p>

                <ul className="space-y-3 mb-6">
                    <li className="flex items-start gap-3 text-base text-zinc-600 dark:text-zinc-400">
                        <span className="flex items-center justify-center w-6 h-6 rounded-full bg-zinc-900 dark:bg-zinc-100 text-zinc-50 dark:text-zinc-900 text-xs font-bold shrink-0 mt-0.5">1</span>
                        <div>
                            <strong className="font-semibold text-zinc-900 dark:text-zinc-50">Agent Configuration</strong>
                            <p className="text-sm mt-1">Each agent specifies which skills it can access in its frontmatter</p>
                        </div>
                    </li>
                    <li className="flex items-start gap-3 text-base text-zinc-600 dark:text-zinc-400">
                        <span className="flex items-center justify-center w-6 h-6 rounded-full bg-zinc-900 dark:bg-zinc-100 text-zinc-50 dark:text-zinc-900 text-xs font-bold shrink-0 mt-0.5">2</span>
                        <div>
                            <strong className="font-semibold text-zinc-900 dark:text-zinc-50">Task Context</strong>
                            <p className="text-sm mt-1">The AI reads skill descriptions and loads relevant ones</p>
                        </div>
                    </li>
                    <li className="flex items-start gap-3 text-base text-zinc-600 dark:text-zinc-400">
                        <span className="flex items-center justify-center w-6 h-6 rounded-full bg-zinc-900 dark:bg-zinc-100 text-zinc-50 dark:text-zinc-900 text-xs font-bold shrink-0 mt-0.5">3</span>
                        <div>
                            <strong className="font-semibold text-zinc-900 dark:text-zinc-50">Selective Reading</strong>
                            <p className="text-sm mt-1">Only necessary sections are read to optimize context usage</p>
                        </div>
                    </li>
                </ul>
            </section>

            {/* Skill Categories */}
            <section className="mb-12">
                <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    Skill Categories
                </h2>
                <p className="text-base text-zinc-600 dark:text-zinc-400 mb-6">
                    {skillsData.length}+ skills organized by domain:
                </p>

                <div className="space-y-8">
                    {categoryOrder.map((category) => {
                        const skills = skillsByCategory[category];
                        if (!skills) return null;

                        return (
                            <div key={category}>
                                <h3 className="text-lg font-semibold text-zinc-900 dark:text-zinc-50 mb-4 border-b border-zinc-100 dark:border-zinc-800 pb-2 inline-block">
                                    {category}
                                </h3>
                                <div className="grid gap-3 sm:grid-cols-2">
                                    {skills.map((skill) => (
                                        <div key={skill.name} className="p-4 rounded-lg border border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-900/50 hover:border-zinc-300 dark:hover:border-zinc-700 transition-colors">
                                            <code className="text-sm font-mono text-zinc-900 dark:text-zinc-50 font-semibold block mb-1">
                                                {skill.name}
                                            </code>
                                            <p className="text-xs text-zinc-600 dark:text-zinc-400">
                                                {skill.description}
                                            </p>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        );
                    })}
                </div>
            </section>

            {/* Skill Structure */}
            <section className="mb-12">
                <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    Skill Structure
                </h2>
                <p className="text-base text-zinc-600 dark:text-zinc-400 mb-6">
                    Each skill contains:
                </p>

                <div className="relative group mb-6">
                    <pre className="p-4 rounded-lg bg-zinc-900 dark:bg-zinc-900 overflow-x-auto border border-zinc-800 font-mono text-sm">
                        <code className="text-zinc-100">{`skills/
└── react-patterns/
    ├── SKILL.md         # Main documentation
    ├── sections/        # Detailed guides
    ├── examples/        # Reference implementations
    └── scripts/         # Helper utilities (optional)`}</code>
                    </pre>
                </div>
            </section>

            {/* Next Steps */}
            <section className="mb-12">
                <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    Next Steps
                </h2>
                <div className="grid gap-4 sm:grid-cols-2">
                    <Link
                        href="/brain/knowledge/docs_legacy/workflows"
                        className="group p-6 rounded-lg border border-zinc-200 dark:border-zinc-800 hover:border-zinc-300 dark:hover:border-zinc-700 hover:bg-zinc-50 dark:hover:bg-zinc-900 transition-all"
                    >
                        <h3 className="font-semibold text-zinc-900 dark:text-zinc-50 mb-2">Workflows →</h3>
                        <p className="text-sm text-zinc-600 dark:text-zinc-400">
                            Learn about slash command procedures
                        </p>
                    </Link>
                    <Link
                        href="/brain/knowledge/docs_legacy/cli"
                        className="group p-6 rounded-lg border border-zinc-200 dark:border-zinc-800 hover:border-zinc-300 dark:hover:border-zinc-700 hover:bg-zinc-50 dark:hover:bg-zinc-900 transition-all"
                    >
                        <h3 className="font-semibold text-zinc-900 dark:text-zinc-50 mb-2">CLI Reference →</h3>
                        <p className="text-sm text-zinc-600 dark:text-zinc-400">
                            Explore command-line tools
                        </p>
                    </Link>
                </div>
            </section>

            {/* Footer Navigation */}
            <div className="pt-8 border-t border-zinc-200 dark:border-zinc-800 flex items-center justify-between">
                <Link
                    href="/brain/knowledge/docs_legacy/agents"
                    className="text-sm font-medium text-zinc-900 dark:text-zinc-50 hover:underline flex items-center gap-1"
                >
                    <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
                    </svg>
                    Agents
                </Link>
                <Link
                    href="/brain/knowledge/docs_legacy/workflows"
                    className="text-sm font-medium text-zinc-900 dark:text-zinc-50 hover:underline flex items-center gap-1"
                >
                    Workflows
                    <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                    </svg>
                </Link>
            </div>
        </div>
    );
}
```

## File: `web/src/app/brain/knowledge/docs_legacy/workflows/page.tsx`
```tsx
import { Lightbulb } from "lucide-react";
import Link from "next/link";
import workflowsData from "@/services/workflows.json";

export default function WorkflowsPage() {
    // Add default usage examples if not in JSON (since ARCHITECTURE.md didn't have usage)
    const workflows = workflowsData.map(wf => ({
        ...wf,
        usage: wf.command + " [args]", // Simple default usage
    }));

    return (
        <div className="max-w-3xl">
            {/* Breadcrumb */}
            <nav className="flex items-center gap-2 text-sm text-zinc-600 dark:text-zinc-400 mb-6">
                <Link href="/docs" className="hover:text-zinc-900 dark:hover:text-zinc-50">Docs</Link>
                <span>/</span>
                <span className="text-zinc-900 dark:text-zinc-50">Workflows</span>
            </nav>

            {/* Page Header */}
            <div className="mb-8 pb-8 border-b border-zinc-200 dark:border-zinc-800">
                <h1 className="text-4xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    Workflows
                </h1>
                <p className="text-lg text-zinc-600 dark:text-zinc-400">
                    Slash command procedures for common development tasks.
                </p>
            </div>

            {/* What are Workflows */}
            <section className="mb-12">
                <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    What are Workflows?
                </h2>
                <p className="text-base text-zinc-600 dark:text-zinc-400 mb-4">
                    Workflows are well-defined, step-by-step procedures for achieving specific development tasks. They're invoked using slash commands and provide consistent, repeatable processes.
                </p>
                <p className="text-base text-zinc-600 dark:text-zinc-400 mb-6">
                    Each workflow contains specific instructions, decision points, and best practices for its domain.
                </p>
            </section>

            {/* How to Use */}
            <section className="mb-12">
                <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    How to Use Workflows
                </h2>
                <p className="text-base text-zinc-600 dark:text-zinc-400 mb-6">
                    Simply type a slash command followed by your task description:
                </p>

                <div className="relative group mb-6">
                    <pre className="p-4 rounded-lg bg-zinc-900 dark:bg-zinc-900 overflow-x-auto border border-zinc-800 font-mono text-sm">
                        <code className="text-zinc-100">{`/brainstorm authentication system
/create landing page with hero section
/debug why login fails`}</code>
                    </pre>
                </div>

                <div className="bg-blue-50 dark:bg-blue-950/30 border border-blue-200 dark:border-blue-800 rounded-lg p-4 mb-4">
                    <p className="text-sm text-blue-900 dark:text-blue-100 mb-0">
                        <Lightbulb className="w-4 h-4 inline" />
                        <strong className="font-semibold"> Tip:</strong> Some workflows have a <code className="px-1 py-0.5 rounded bg-blue-100 dark:bg-blue-900/40 font-mono text-xs">// turbo</code> annotation that allows auto-running safe commands without user approval.
                    </p>
                </div>
            </section>

            {/* Available Workflows */}
            <section className="mb-12">
                <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    Available Workflows
                </h2>
                <p className="text-base text-zinc-600 dark:text-zinc-400 mb-6">
                    {workflows.length} workflows covering common development scenarios:
                </p>

                <div className="space-y-6">
                    {workflows.map((workflow) => (
                        <div
                            key={workflow.command}
                            className="p-5 rounded-lg border border-zinc-200 dark:border-zinc-800"
                        >
                            <div className="flex items-start justify-between gap-4 mb-3">
                                <code className="text-lg font-mono font-semibold text-zinc-900 dark:text-zinc-50">
                                    {workflow.command}
                                </code>
                            </div>
                            <p className="text-sm text-zinc-600 dark:text-zinc-400 mb-3 leading-relaxed">
                                {workflow.description}
                            </p>
                            <div className="pt-3 border-t border-zinc-200 dark:border-zinc-800">
                                <div className="text-xs font-semibold uppercase tracking-wider text-zinc-500 dark:text-zinc-500 mb-2">
                                    Example Usage
                                </div>
                                <code className="text-sm font-mono text-zinc-700 dark:text-zinc-300 bg-zinc-100 dark:bg-zinc-900 px-2 py-1 rounded">
                                    {workflow.usage}
                                </code>
                            </div>
                        </div>
                    ))}
                </div>
            </section>

            {/* Creating Custom Workflows */}
            <section className="mb-12">
                <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    Creating Custom Workflows
                </h2>
                <p className="text-base text-zinc-600 dark:text-zinc-400 mb-6">
                    You can create your own workflows by adding markdown files to <code className="px-1.5 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-sm font-mono">.agent/workflows/</code>:
                </p>

                <div className="relative group mb-6">
                    <pre className="p-4 rounded-lg bg-zinc-900 dark:bg-zinc-900 overflow-x-auto border border-zinc-800 font-mono text-sm">
                        <code className="text-zinc-100">{`---
description: Deploy application to staging
---

# Deployment Workflow

1. Run tests
2. Build production bundle
3. Deploy to staging server
4. Verify deployment`}</code>
                    </pre>
                </div>

                <p className="text-base text-zinc-600 dark:text-zinc-400">
                    Save as <code className="px-1.5 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-sm font-mono">.agent/workflows/deploy-staging.md</code> and invoke with <code className="px-1.5 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-sm font-mono">/deploy-staging</code>.
                </p>
            </section>

            {/* Next Steps */}
            <section className="mb-12">
                <h2 className="text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 mb-4">
                    Next Steps
                </h2>
                <div className="grid gap-4 sm:grid-cols-2">
                    <Link
                        href="/brain/knowledge/docs_legacy/cli"
                        className="group p-6 rounded-lg border border-zinc-200 dark:border-zinc-800 hover:border-zinc-300 dark:hover:border-zinc-700 hover:bg-zinc-50 dark:hover:bg-zinc-900 transition-all"
                    >
                        <h3 className="font-semibold text-zinc-900 dark:text-zinc-50 mb-2">CLI Reference →</h3>
                        <p className="text-sm text-zinc-600 dark:text-zinc-400">
                            Learn about command-line tools
                        </p>
                    </Link>
                    <Link
                        href="/brain/knowledge/docs_legacy/agents"
                        className="group p-6 rounded-lg border border-zinc-200 dark:border-zinc-800 hover:border-zinc-300 dark:hover:border-zinc-700 hover:bg-zinc-50 dark:hover:bg-zinc-900 transition-all"
                    >
                        <h3 className="font-semibold text-zinc-900 dark:text-zinc-50 mb-2">Back to Agents →</h3>
                        <p className="text-sm text-zinc-600 dark:text-zinc-400">
                            Review specialist agents
                        </p>
                    </Link>
                </div>
            </section>

            {/* Footer Navigation */}
            <div className="pt-8 border-t border-zinc-200 dark:border-zinc-800 flex items-center justify-between">
                <Link
                    href="/brain/knowledge/docs_legacy/skills"
                    className="text-sm font-medium text-zinc-900 dark:text-zinc-50 hover:underline flex items-center gap-1"
                >
                    <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
                    </svg>
                    Skills
                </Link>
                <Link
                    href="/brain/knowledge/docs_legacy/cli"
                    className="text-sm font-medium text-zinc-900 dark:text-zinc-50 hover:underline flex items-center gap-1"
                >
                    CLI Reference
                    <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                    </svg>
                </Link>
            </div>
        </div>
    );
}
```

## File: `web/src/components/theme-provider.tsx`
```tsx
"use client"

import * as React from "react"
import { ThemeProvider as NextThemesProvider } from "next-themes"

export function ThemeProvider({
    children,
    ...props
}: React.ComponentProps<typeof NextThemesProvider>) {
    return <NextThemesProvider {...props}>{children}</NextThemesProvider>
}
```

## File: `web/src/components/typing.tsx`
```tsx
'use client';

import Typewriter from 'typewriter-effect';
import agents from '@/services/agents.json';
import skills from '@/services/skills.json';
import workflows from '@/services/workflows.json';


export default function Typing() {
    return (
        <Typewriter
            options={{
                strings: [`${agents.length}+ Agents`, `${skills.length}+ Skills`, `${workflows.length}+ Workflows`, 'Open Source'],
                autoStart: true,
                loop: true,
                delay: 75,
                deleteSpeed: 50,
            }}
        />
    )
}
```

## File: `web/src/components/brain/knowledge/docs_legacy/code-block.tsx`
```tsx
'use client';

import { useState } from 'react';
import { CheckIcon, CopyIcon } from 'lucide-react';

interface CodeBlockProps {
    code: string;
    language?: string;
    showLineNumbers?: boolean;
    className?: string;
}

export function CodeBlock({ code, language = 'bash', showLineNumbers = false, className }: CodeBlockProps) {
    const [copied, setCopied] = useState(false);

    const copyToClipboard = async () => {
        await navigator.clipboard.writeText(code);
        setCopied(true);
        setTimeout(() => setCopied(false), 2000);
    };

    return (
        <div className={`relative group ${className}`}>
            <pre className={`p-4 rounded-lg bg-zinc-900 dark:bg-zinc-900 overflow-x-auto border border-zinc-800 font-mono text-sm ${showLineNumbers ? 'pl-12' : ''}`}>
                <code className="text-zinc-100">{code}</code>
            </pre>
            <button
                onClick={copyToClipboard}
                className="absolute top-3 right-3 p-2 rounded-md bg-zinc-800 hover:bg-zinc-700 transition-colors opacity-0 group-hover:opacity-100"
                aria-label="Copy code"
            >
                {copied ? (
                    <CheckIcon className="w-4 h-4 text-green-400" />
                ) : (
                    <CopyIcon className="w-4 h-4 text-zinc-400" />
                )}
            </button>
        </div>
    );
}
```

## File: `web/src/components/brain/knowledge/docs_legacy/sidebar.tsx`
```tsx
'use client';

import { useState } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';

const navSections = [
    {
        title: 'Getting Started',
        items: [
            { href: '/docs', label: 'Introduction' },
            { href: '/brain/knowledge/docs_legacy/installation', label: 'Installation' },
        ],
    },
    {
        title: 'Core Concepts',
        items: [
            { href: '/brain/knowledge/docs_legacy/agents', label: 'Agents' },
            { href: '/brain/knowledge/docs_legacy/skills', label: 'Skills' },
            { href: '/brain/knowledge/docs_legacy/workflows', label: 'Workflows' },
        ],
    },
    {
        title: 'Guide',
        items: [
            { href: '/brain/knowledge/docs_legacy/guide/examples/brainstorm', label: 'Structured Brainstorming' },
            { href: '/brain/knowledge/docs_legacy/guide/examples/plan', label: 'Project Planning' },
            { href: '/brain/knowledge/docs_legacy/guide/examples/create', label: 'Create New Application' },
            { href: '/brain/knowledge/docs_legacy/guide/examples/new-feature', label: 'Add a New Feature' },
            { href: '/brain/knowledge/docs_legacy/guide/examples/ui-design', label: 'Advanced UI Design' },
            { href: '/brain/knowledge/docs_legacy/guide/examples/debugging', label: 'Systematic Debugging' },
            { href: '/brain/knowledge/docs_legacy/guide/examples/test', label: 'Test Generation' },
            { href: '/brain/knowledge/docs_legacy/guide/examples/preview', label: 'Preview Management' },
            { href: '/brain/knowledge/docs_legacy/guide/examples/status', label: 'Project Status' },
            { href: '/brain/knowledge/docs_legacy/guide/examples/orchestration', label: 'Multi-Agent Orchestration' },
            { href: '/brain/knowledge/docs_legacy/guide/examples/deployment', label: 'Production Deployment' },
        ],
    },
    {
        title: 'CLI Reference',
        items: [
            { href: '/brain/knowledge/docs_legacy/cli', label: 'Commands & Options' },
        ],
    },
];

export default function DocsSidebar() {
    const pathname = usePathname();

    return (
        <nav className="space-y-1">
            {navSections.map((section) => (
                <div key={section.title} className="pb-6">
                    <h3 className="mb-3 px-2 text-sm font-semibold text-zinc-900 dark:text-zinc-50">
                        {section.title}
                    </h3>
                    <div className="space-y-0.5">
                        {section.items.map((item) => {
                            const isActive = pathname === item.href;
                            return (
                                <Link
                                    key={item.href}
                                    href={item.href}
                                    className={`
                    block px-2 py-1.5 text-sm rounded-md transition-colors
                    ${isActive
                                            ? 'bg-zinc-100 dark:bg-zinc-800 text-zinc-900 dark:text-zinc-50 font-medium'
                                            : 'text-zinc-700 dark:text-zinc-300 hover:text-zinc-900 dark:hover:text-zinc-50 hover:bg-zinc-100 dark:hover:bg-zinc-800'
                                        }
                  `}
                                >
                                    {item.label}
                                </Link>
                            );
                        })}
                    </div>
                </div>
            ))}
        </nav>
    );
}
```

## File: `web/src/components/layout/footer/index.tsx`
```tsx

import Link from "next/link";

export default function Footer() {
    return (
        <footer className="border-t border-zinc-200 dark:border-zinc-800 mt-auto">
            <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-12">
                <div className="grid grid-cols-2 md:grid-cols-4 gap-8 mb-8">
                    {/* Product */}
                    <div>
                        <h3 className="font-semibold text-zinc-900 dark:text-zinc-50 mb-4">Product</h3>
                        <ul className="space-y-3 text-sm">
                            <li>
                                <Link href="/docs" className="text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-50 transition-colors">
                                    Documentation
                                </Link>
                            </li>
                            <li>
                                <Link href="/brain/knowledge/docs_legacy/agents" className="text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-50 transition-colors">
                                    Agents
                                </Link>
                            </li>
                            <li>
                                <Link href="/brain/knowledge/docs_legacy/skills" className="text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-50 transition-colors">
                                    Skills
                                </Link>
                            </li>
                            <li>
                                <Link href="/brain/knowledge/docs_legacy/workflows" className="text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-50 transition-colors">
                                    Workflows
                                </Link>
                            </li>
                        </ul>
                    </div>

                    {/* Resources */}
                    <div>
                        <h3 className="font-semibold text-zinc-900 dark:text-zinc-50 mb-4">Resources</h3>
                        <ul className="space-y-3 text-sm">
                            <li>
                                <Link href="/brain/knowledge/docs_legacy/installation" className="text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-50 transition-colors">
                                    Installation
                                </Link>
                            </li>
                            <li>
                                <Link href="/brain/knowledge/docs_legacy/cli" className="text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-50 transition-colors">
                                    CLI Reference
                                </Link>
                            </li>
                            <li>
                                <a href="https://github.com/vudovn/antigravity-kit" target="_blank" rel="noopener noreferrer" className="text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-50 transition-colors">
                                    Examples
                                </a>
                            </li>
                            <li>
                                <a href="https://github.com/vudovn/antigravity-kit/releases" target="_blank" rel="noopener noreferrer" className="text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-50 transition-colors">
                                    Changelog
                                </a>
                            </li>
                        </ul>
                    </div>

                    {/* Community */}
                    <div>
                        <h3 className="font-semibold text-zinc-900 dark:text-zinc-50 mb-4">Community</h3>
                        <ul className="space-y-3 text-sm">
                            <li>
                                <a href="https://github.com/vudovn/antigravity-kit" target="_blank" rel="noopener noreferrer" className="text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-50 transition-colors">
                                    GitHub
                                </a>
                            </li>
                            <li>
                                <a href="https://github.com/vudovn/antigravity-kit/issues" target="_blank" rel="noopener noreferrer" className="text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-50 transition-colors">
                                    Issues
                                </a>
                            </li>
                            <li>
                                <a href="https://github.com/vudovn/antigravity-kit/discussions" target="_blank" rel="noopener noreferrer" className="text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-50 transition-colors">
                                    Discussions
                                </a>
                            </li>
                            <li>
                                <a href="https://github.com/vudovn/antigravity-kit/blob/main/CONTRIBUTING.md" target="_blank" rel="noopener noreferrer" className="text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-50 transition-colors">
                                    Contributing
                                </a>
                            </li>
                        </ul>
                    </div>

                    {/* Legal */}
                    <div>
                        <h3 className="font-semibold text-zinc-900 dark:text-zinc-50 mb-4">Legal</h3>
                        <ul className="space-y-3 text-sm">
                            <li>
                                <a href="https://github.com/vudovn/antigravity-kit/blob/main/LICENSE" target="_blank" rel="noopener noreferrer" className="text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-50 transition-colors">
                                    License
                                </a>
                            </li>
                            <li>
                                <Link href="#1" className="text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-50 transition-colors">
                                    Privacy Policy
                                </Link>
                            </li>
                            <li>
                                <Link href="#1" className="text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-50 transition-colors">
                                    Terms of Service
                                </Link>
                            </li>
                        </ul>
                    </div>
                </div>

                {/* Bottom Bar */}
                <div className="pt-8 border-t border-zinc-200 dark:border-zinc-800 flex flex-col sm:flex-row items-center justify-between gap-4">
                    {/* Copyright */}
                    <p className="text-sm text-zinc-600 dark:text-zinc-400">
                        © {new Date().getFullYear()} Antigravity Kit by{" "}
                        <a
                            href="https://github.com/vudovn"
                            target="_blank"
                            rel="noopener noreferrer"
                            className="font-medium text-zinc-900 dark:text-zinc-50 hover:underline">
                            @vudovn
                        </a>. All rights reserved.
                    </p>

                    {/* Social Links */}
                    <div className="flex items-center gap-4">
                        <a
                            href="https://github.com/vudovn/antigravity-kit"
                            target="_blank"
                            rel="noopener noreferrer"
                            className="text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-50 transition-colors"
                            aria-label="GitHub"
                        >
                            <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                                <path fillRule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clipRule="evenodd" />
                            </svg>
                        </a>
                        <a
                            href="https://facebook.com/vudovn.354"
                            target="_blank"
                            rel="noopener noreferrer"
                            className="text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-50 transition-colors"
                            aria-label="Facebook"
                        >
                            <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                                <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z" />
                            </svg>
                        </a>
                    </div>
                </div>
            </div>
        </footer>
    );
}
```

## File: `web/src/components/layout/header/index.tsx`
```tsx
import Link from "next/link";
import MobileMenu from "@/components/layout/header/components/mobile-menu";
import SearchDialog from "@/components/layout/header/components/search-dialog";
import ThemeToggle from "@/components/layout/header/components/theme-toggle";
import DonateDialog from "@/components/layout/header/components/donate-dialog";
import { Button } from "@/components/ui/button";
import { GithubIcon } from "lucide-react";

const DiscordIcon = () => {
    return (
<svg
  viewBox="0 -28.5 256 256"
  version="1.1"
  xmlns="http://www.w3.org/2000/svg"
  xmlnsXlink="http://www.w3.org/1999/xlink"
  preserveAspectRatio="xMidYMid"
  fill="#000000"
>
  <g id="SVGRepo_bgCarrier" strokeWidth={0} />
  <g id="SVGRepo_tracerCarrier" strokeLinecap="round" strokeLinejoin="round" />
  <g id="SVGRepo_iconCarrier">
    {" "}
    <g>
      {" "}
      <path
        d="M216.856339,16.5966031 C200.285002,8.84328665 182.566144,3.2084988 164.041564,0 C161.766523,4.11318106 159.108624,9.64549908 157.276099,14.0464379 C137.583995,11.0849896 118.072967,11.0849896 98.7430163,14.0464379 C96.9108417,9.64549908 94.1925838,4.11318106 91.8971895,0 C73.3526068,3.2084988 55.6133949,8.86399117 39.0420583,16.6376612 C5.61752293,67.146514 -3.4433191,116.400813 1.08711069,164.955721 C23.2560196,181.510915 44.7403634,191.567697 65.8621325,198.148576 C71.0772151,190.971126 75.7283628,183.341335 79.7352139,175.300261 C72.104019,172.400575 64.7949724,168.822202 57.8887866,164.667963 C59.7209612,163.310589 61.5131304,161.891452 63.2445898,160.431257 C105.36741,180.133187 151.134928,180.133187 192.754523,160.431257 C194.506336,161.891452 196.298154,163.310589 198.110326,164.667963 C191.183787,168.842556 183.854737,172.420929 176.223542,175.320965 C180.230393,183.341335 184.861538,190.991831 190.096624,198.16893 C211.238746,191.588051 232.743023,181.531619 254.911949,164.955721 C260.227747,108.668201 245.831087,59.8662432 216.856339,16.5966031 Z M85.4738752,135.09489 C72.8290281,135.09489 62.4592217,123.290155 62.4592217,108.914901 C62.4592217,94.5396472 72.607595,82.7145587 85.4738752,82.7145587 C98.3405064,82.7145587 108.709962,94.5189427 108.488529,108.914901 C108.508531,123.290155 98.3405064,135.09489 85.4738752,135.09489 Z M170.525237,135.09489 C157.88039,135.09489 147.510584,123.290155 147.510584,108.914901 C147.510584,94.5396472 157.658606,82.7145587 170.525237,82.7145587 C183.391518,82.7145587 193.761324,94.5189427 193.539891,108.914901 C193.539891,123.290155 183.391518,135.09489 170.525237,135.09489 Z"
        fill="#5865F2"
        fillRule="nonzero"
      >
        {" "}
      </path>{" "}
    </g>{" "}
  </g>
</svg>

    );
};

export default function Header() {
    return (
        <header className="sticky top-0 z-50 w-full border-b border-zinc-200 dark:border-zinc-800 bg-white/95 dark:bg-zinc-950/95 backdrop-blur supports-[backdrop-filter]:bg-white/80 supports-[backdrop-filter]:dark:bg-zinc-950/80">
            <div className="container mx-auto px-4 sm:px-6 lg:px-8 relative">
                <div className="flex h-14 items-center justify-between gap-2 sm:gap-4">
                    {/* Left Section */}
                    <div className="flex items-center gap-2 sm:gap-3 md:gap-6 flex-1 min-w-0">
                        {/* Mobile Menu */}
                        <div className="lg:hidden">
                            <MobileMenu />
                        </div>

                        {/* Logo - Responsive */}
                        <span className="text-zinc-900 dark:text-white before:-inset-x-1 before:-rotate-1 relative z-4 before:pointer-events-none before:absolute before:inset-y-0 before:z-4 before:bg-linear-to-r before:from-blue-500 before:via-cyan-500 before:to-orange-500 before:opacity-16 before:mix-blend-hard-light font-semibold text-sm sm:text-base truncate">
                            <Link href="/" className="flex items-center gap-2 shrink-0 min-w-0">
                                <span className="hidden sm:inline">Antigravity Kit</span>
                                <span className="sm:hidden">AG Kit</span>
                            </Link>
                        </span>

                        {/* Separator */}
                        <div className="hidden sm:block w-px h-6 bg-zinc-200 dark:bg-zinc-800 shrink-0" />

                        {/* Desktop Nav */}
                        <nav className="hidden sm:flex items-center gap-1 flex-1 min-w-0">
                            <DonateDialog />
                            <Link href="https://github.com/vudovn/antigravity-kit" target="_blank" rel="noopener noreferrer">
                                <Button variant="outline" className="hidden md:flex">
                                    <GithubIcon className="w-4 h-4 mr-2" />
                                    GitHub
                                </Button>
                            </Link>
                            {/* <Link href="https://discord.gg/CwpvDdFK" target="_blank" rel="noopener noreferrer">
                                <Button variant="outline" className="hidden md:flex">
                                    <DiscordIcon />
                                    Discord
                                </Button>
                            </Link> */}
                            <Link href="https://unikorn.vn/" target="_blank" rel="noopener noreferrer">
                                <Button variant="outline" className="hidden md:flex">
                                    <svg
                                        width={24}
                                        height={24}
                                        viewBox="0 0 1000 1000"
                                        fill="currentColor"
                                        className="shrink-0"
                                        >
                                        <g transform="matrix(1,0,0,1,0,9.204355)">
                                            <path d="M890.828,5.864C895.373,4.486 900.302,5.343 904.116,8.172C907.93,11.002 910.178,15.47 910.178,20.219C910.178,143.585 910.178,795.144 910.178,961.372C910.178,967.476 906.48,972.971 900.825,975.269C895.17,977.566 888.687,976.208 884.429,971.834C645.13,726.029 399.028,922.802 198.646,716.77C128.914,644.809 89.922,548.538 89.922,448.334C89.822,333.557 89.822,156.891 89.822,111.128C89.822,104.519 94.147,98.689 100.472,96.773C147.714,82.457 338.731,24.573 400.472,5.864C405.016,4.486 409.945,5.343 413.759,8.172C417.573,11.002 419.822,15.47 419.822,20.219C419.822,92.456 419.822,340.356 419.822,469.822C419.822,514.103 455.719,550 500,550L500,550C544.281,550 580.178,514.103 580.178,469.822L580.178,111.128C580.178,104.519 584.504,98.689 590.828,96.773C638.071,82.457 829.088,24.573 890.828,5.864Z" />
                                        </g>
                                        </svg>
                                    Sponsored
                                </Button>
                            </Link>
                        </nav>
                    </div>

                    {/* Right Section */}
                    <div className="flex items-center gap-2 sm:gap-3 shrink-0">
                        {/* Search - Desktop */}
                        <div className="hidden md:block w-64">
                            <SearchDialog />
                        </div>

                        {/* Mobile Search Button */}
                        <div className="md:hidden">
                            <SearchDialog />
                        </div>

                        {/* Separator */}
                        <div className="hidden md:block w-px h-6 bg-zinc-200 dark:bg-zinc-800" />

                        {/* Theme Toggle */}
                        <ThemeToggle />
                    </div>
                </div>
            </div>
        </header>
    )
}
```

## File: `web/src/components/layout/header/components/donate-dialog.tsx`
```tsx
'use client';

import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Dialog, DialogClose, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle, DialogTrigger } from '@/components/ui/dialog';
import { CoffeeIcon, Heart, QrCodeIcon, User } from 'lucide-react';

interface DonateDialogProps {
    className?: string;
}

export default function DonateDialog({ className }: DonateDialogProps) {
    const [showQR, setShowQR] = useState(false);

    return (
        <Dialog>
            <DialogTrigger render={<Button variant="outline" className={className} />}>
                <Heart className="w-3 h-3 mr-1.5 text-red-500" />
                Donate
            </DialogTrigger>
            <DialogContent className="sm:max-w-md">
                <DialogHeader>
                    <DialogTitle className="flex items-center gap-2">
                        <span>Fuel the Developer</span>
                    </DialogTitle>
                    <DialogDescription className="space-y-2 pt-2">
                        Hi! I'm <strong>Vu</strong>. I'm dedicating my full-time work to building this kit. <br />
                        Your support helps me keep shipping and maintaining it. If you find this tool helpful, please consider buying me a coffee.
                    </DialogDescription>
                </DialogHeader>

                <div className="space-y-3 p-4">
                    {/* Buy Me a Coffee */}
                    <a
                        href="https://buymeacoffee.com/vudovn"
                        target="_blank"
                        rel="noopener noreferrer"
                        className="flex items-center gap-3 p-4 rounded-lg border border-zinc-200 dark:border-zinc-800 hover:border-zinc-300 dark:hover:border-zinc-700 hover:bg-zinc-50 dark:hover:bg-zinc-900 transition-all group"
                    >
                        <div className="flex items-center justify-center w-10 h-10 rounded-full bg-amber-100 dark:bg-amber-900/20">
                            <CoffeeIcon className="w-5 h-5 text-amber-600 dark:text-amber-500" />
                        </div>
                        <div className="flex-1">
                            <div className="font-semibold text-zinc-900 dark:text-zinc-50 mb-0.5">Buy Me a Coffee</div>
                            <div className="text-sm text-zinc-600 dark:text-zinc-400">Support via buymeacoffee.com</div>
                        </div>
                        <svg className="w-5 h-5 text-zinc-400 group-hover:text-zinc-600 dark:group-hover:text-zinc-300 transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                        </svg>
                    </a>

                    {/* Bank Transfer with QR */}
                    <button
                        onClick={() => setShowQR(!showQR)}
                        className="w-full flex items-center gap-3 p-4 rounded-lg border border-zinc-200 dark:border-zinc-800 hover:border-zinc-300 dark:hover:border-zinc-700 hover:bg-zinc-50 dark:hover:bg-zinc-900 transition-all group text-left"
                    >
                        <div className="flex items-center justify-center w-10 h-10 rounded-full bg-blue-100 dark:bg-blue-900/20">
                            <QrCodeIcon className="w-5 h-5 text-blue-600 dark:text-blue-500" />
                        </div>
                        <div className="flex-1">
                            <div className="font-semibold text-zinc-900 dark:text-zinc-50 mb-0.5">Bank Transfer</div>
                            <div className="text-sm text-zinc-600 dark:text-zinc-400">Direct transfer via QR code</div>
                        </div>
                        <svg className={`w-5 h-5 text-zinc-400 transition-transform ${showQR ? 'rotate-90' : ''}`} fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                        </svg>
                    </button>

                    {/* QR Code Display */}
                    {showQR && (
                        <div className="p-4 rounded-lg border border-zinc-200 dark:border-zinc-800 bg-zinc-50 dark:bg-zinc-900/50">
                            <div className="flex flex-col items-center gap-4">
                                {/* QR Code Placeholder - Replace with actual QR code image */}
                                <img className="w-48 h-48 rounded-lg" src="https://img.vietqr.io/image/mbbank-0779440918-compact.jpg" alt="" />
                                {/* Bank Details */}
                                <div className="text-center space-y-1">
                                    <div className="text-sm font-medium text-zinc-900 dark:text-zinc-50">
                                        Bank: <span className="font-mono">MB Bank</span>
                                    </div>
                                    <div className="text-sm font-medium text-zinc-900 dark:text-zinc-50">
                                        Account: <span className="font-mono">0779440918</span>
                                    </div>
                                    <div className="text-sm font-medium text-zinc-900 dark:text-zinc-50">
                                        Name: <span className="font-mono">DO VAN VU</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    )}

                    {/* Hire Me Option */}
                    {/* <a
                        href="https://www.linkedin.com/in/vudovn" // Assuming this link based on username, user can update
                        target="_blank"
                        rel="noopener noreferrer"
                        className="flex items-center gap-3 p-4 rounded-lg border border-zinc-200 dark:border-zinc-800 hover:border-blue-500/50 dark:hover:border-blue-500/50 hover:bg-blue-50 dark:hover:bg-blue-900/10 transition-all group"
                    >
                        <div className="flex items-center justify-center w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/20">
                            <span className="text-xl">
                                <User />
                            </span>
                        </div>
                        <div className="flex-1">
                            <div className="font-semibold text-zinc-900 dark:text-zinc-50 mb-0.5">Hire Me!</div>
                            <div className="text-sm text-zinc-600 dark:text-zinc-400">View my profile & portfolio</div>
                        </div>
                        <svg className="w-5 h-5 text-zinc-400 group-hover:text-blue-500 transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                        </svg>
                    </a> */}
                </div>

                <DialogFooter>
                    <DialogClose render={<Button variant="ghost" />}>
                        Close
                    </DialogClose>
                </DialogFooter>
            </DialogContent>
        </Dialog>
    );
}
```

## File: `web/src/components/layout/header/components/mobile-menu.tsx`
```tsx
'use client';

import { useState, useEffect } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import DonateDialog from '@/components/layout/header/components/donate-dialog';
import { GithubIcon } from 'lucide-react';
import { Button } from '@/components/ui/button';

const navSections = [
    {
        title: 'Getting Started',
        items: [
            { href: '/docs', label: 'Introduction' },
            { href: '/brain/knowledge/docs_legacy/installation', label: 'Installation' },
        ],
    },
    {
        title: 'Core Concepts',
        items: [
            { href: '/brain/knowledge/docs_legacy/agents', label: 'Agents' },
            { href: '/brain/knowledge/docs_legacy/skills', label: 'Skills' },
            { href: '/brain/knowledge/docs_legacy/workflows', label: 'Workflows' },
        ],
    },
    {
        title: 'CLI Reference',
        items: [
            { href: '/brain/knowledge/docs_legacy/cli', label: 'Commands & Options' },
        ],
    },
];

export default function MobileMenu() {
    const [isOpen, setIsOpen] = useState(false);
    const pathname = usePathname();

    // Close menu when route changes
    useEffect(() => {
        setIsOpen(false);
    }, [pathname]);

    return (
        <>
            {/* Mobile Menu Button */}
            <button
                onClick={() => setIsOpen(!isOpen)}
                className="lg:hidden p-2 rounded-md text-zinc-600 dark:text-zinc-400 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors"
                aria-label="Toggle menu"
            >
                {isOpen ? (
                    <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                    </svg>
                ) : (
                    <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
                    </svg>
                )}
            </button>

            {/* Mobile Menu Dropdown - Renders in parent header component */}
            {isOpen && (
                <div className="lg:hidden absolute left-0 right-0 top-full border-t border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-950 shadow-lg animate-in slide-in-from-top-2 max-h-[calc(100vh-3.5rem)] overflow-y-auto">
                    <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-6">
                        {/* Navigation */}
                        <nav className="space-y-6">
                            {navSections.map((section) => (
                                <div key={section.title}>
                                    <h3 className="mb-3 text-sm font-semibold text-zinc-900 dark:text-zinc-50">
                                        {section.title}
                                    </h3>
                                    <div className="space-y-1">
                                        {section.items.map((item) => {
                                            const isActive = pathname === item.href;
                                            return (
                                                <Link
                                                    key={item.href}
                                                    href={item.href}
                                                    className={`
                                                        block px-3 py-2 text-sm rounded-md transition-colors
                                                        ${isActive
                                                            ? 'bg-zinc-100 dark:bg-zinc-800 text-zinc-900 dark:text-zinc-50 font-medium'
                                                            : 'text-zinc-700 dark:text-zinc-300 hover:text-zinc-900 dark:hover:text-zinc-50 hover:bg-zinc-100 dark:hover:bg-zinc-800'
                                                        }
                                                    `}
                                                >
                                                    {item.label}
                                                </Link>
                                            );
                                        })}
                                    </div>
                                </div>
                            ))}
                        </nav>

                        {/* Mobile Action Buttons */}
                        <div className="mt-6 pt-6 border-t border-zinc-200 dark:border-zinc-800 flex gap-3">
                            <DonateDialog className="" />
                            <Link href="https://github.com/vudovn/antigravity-kit" target="_blank" rel="noopener noreferrer">
                                <Button variant="outline" className="w-full justify-start">
                                    <GithubIcon className="w-4 h-4 mr-2" />
                                    GitHub
                                </Button>
                            </Link>
                            <Link href="https://unikorn.vn/" target="_blank" rel="noopener noreferrer">
                                <Button variant="outline" className="w-full justify-start">
                                    <svg
                                        width={24}
                                        height={24}
                                        viewBox="0 0 1000 1000"
                                        fill="currentColor"
                                        className="shrink-0"
                                        >
                                        <g transform="matrix(1,0,0,1,0,9.204355)">
                                            <path d="M890.828,5.864C895.373,4.486 900.302,5.343 904.116,8.172C907.93,11.002 910.178,15.47 910.178,20.219C910.178,143.585 910.178,795.144 910.178,961.372C910.178,967.476 906.48,972.971 900.825,975.269C895.17,977.566 888.687,976.208 884.429,971.834C645.13,726.029 399.028,922.802 198.646,716.77C128.914,644.809 89.922,548.538 89.922,448.334C89.822,333.557 89.822,156.891 89.822,111.128C89.822,104.519 94.147,98.689 100.472,96.773C147.714,82.457 338.731,24.573 400.472,5.864C405.016,4.486 409.945,5.343 413.759,8.172C417.573,11.002 419.822,15.47 419.822,20.219C419.822,92.456 419.822,340.356 419.822,469.822C419.822,514.103 455.719,550 500,550L500,550C544.281,550 580.178,514.103 580.178,469.822L580.178,111.128C580.178,104.519 584.504,98.689 590.828,96.773C638.071,82.457 829.088,24.573 890.828,5.864Z" />
                                        </g>
                                        </svg>
                                    Sponsored
                                </Button>
                            </Link>
                        </div>
                    </div>
                </div>
            )}
        </>
    );
}
```

## File: `web/src/components/layout/header/components/search-dialog.tsx`
```tsx
'use client';

import { Fragment, useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import { ArrowDownIcon, ArrowUpIcon, CornerDownLeftIcon, FileTextIcon } from 'lucide-react';
import { Button } from '@/components/ui/button';
import {
    Command,
    CommandCollection,
    CommandDialog,
    CommandDialogPopup,
    CommandDialogTrigger,
    CommandEmpty,
    CommandFooter,
    CommandGroup,
    CommandGroupLabel,
    CommandInput,
    CommandItem,
    CommandList,
    CommandPanel,
    CommandSeparator,
} from '@/components/ui/command';
import { Kbd, KbdGroup } from '@/components/ui/kbd';

interface SearchItem {
    value: string;
    label: string;
    href: string;
    keywords?: string;
}

interface SearchGroup {
    value: string;
    items: SearchItem[];
}

const searchGroups: SearchGroup[] = [
    {
        value: 'Getting Started',
        items: [
            {
                label: 'Introduction',
                value: 'introduction',
                href: '/docs',
                keywords: 'getting started overview what is'
            },
            {
                label: 'Installation',
                value: 'installation',
                href: '/brain/knowledge/docs_legacy/installation',
                keywords: 'install setup init npm npx global cli'
            },
        ],
    },
    {
        value: 'Core Concepts',
        items: [
            {
                label: 'Agents',
                value: 'agents',
                href: '/brain/knowledge/docs_legacy/agents',
                keywords: 'specialist personas orchestrator planner security backend frontend'
            },
            {
                label: 'Skills',
                value: 'skills',
                href: '/brain/knowledge/docs_legacy/skills',
                keywords: 'knowledge modules react nextjs tailwind patterns testing'
            },
            {
                label: 'Workflows',
                value: 'workflows',
                href: '/brain/knowledge/docs_legacy/workflows',
                keywords: 'slash commands brainstorm create debug deploy enhance'
            },
        ],
    },
    {
        value: 'Reference',
        items: [
            {
                label: 'CLI Reference',
                value: 'cli',
                href: '/brain/knowledge/docs_legacy/cli',
                keywords: 'command line interface init update status options'
            },
        ],
    },
];

export default function SearchDialog() {
    const [open, setOpen] = useState(false);
    const router = useRouter();

    function handleItemClick(item: SearchItem) {
        router.push(item.href);
        setOpen(false);
    }

    useEffect(() => {
        const down = (e: KeyboardEvent) => {
            if (e.key === 'k' && (e.metaKey || e.ctrlKey)) {
                e.preventDefault();
                setOpen((open) => !open);
            }
        };

        document.addEventListener('keydown', down);
        return () => document.removeEventListener('keydown', down);
    }, []);

    return (
        <CommandDialog onOpenChange={setOpen} open={open}>
            {/* Mobile/Tablet - Icon Only */}
            <CommandDialogTrigger
                className="md:hidden"
                render={
                    <Button
                        variant="ghost"
                        size="icon"
                        aria-label="Search"
                    />
                }
            >
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
            </CommandDialogTrigger>

            {/* Desktop - Full Search Input */}
            <CommandDialogTrigger
                className="hidden md:flex bg-transparent"
                render={
                    <Button
                        variant="outline"
                        className="w-full justify-start text-sm text-muted-foreground font-normal h-9"
                    />
                }
            >
                <svg className="w-4 h-4 mr-2 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
                <span className="flex-1 text-left">Search docs...</span>
                <KbdGroup className="hidden sm:inline-flex">
                    <Kbd>⌘</Kbd>
                    <Kbd>K</Kbd>
                </KbdGroup>
            </CommandDialogTrigger>

            <CommandDialogPopup>
                <Command items={searchGroups}>
                    <CommandInput placeholder="Search documentation..." />
                    <CommandPanel>
                        <CommandEmpty>
                            <div className="flex flex-col items-center justify-center py-6 text-center">
                                <svg className="w-10 h-10 text-muted-foreground/30 mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                </svg>
                                <p className="text-sm font-medium text-foreground mb-1">No results found</p>
                                <p className="text-xs text-muted-foreground">Try searching for something else</p>
                            </div>
                        </CommandEmpty>
                        <CommandList>
                            {(group: SearchGroup) => (
                                <Fragment key={group.value}>
                                    <CommandGroup items={group.items}>
                                        <CommandGroupLabel>{group.value}</CommandGroupLabel>
                                        <CommandCollection>
                                            {(item: SearchItem) => (
                                                <CommandItem
                                                    key={item.value}
                                                    onClick={() => handleItemClick(item)}
                                                    value={item.value + ' ' + (item.keywords || '')}
                                                >
                                                    <FileTextIcon className="mr-2 h-4 w-4 text-muted-foreground" />
                                                    <span className="flex-1">{item.label}</span>
                                                    <span className="text-xs text-muted-foreground">{item.href}</span>
                                                </CommandItem>
                                            )}
                                        </CommandCollection>
                                    </CommandGroup>
                                    <CommandSeparator />
                                </Fragment>
                            )}
                        </CommandList>
                    </CommandPanel>
                    <CommandFooter>
                        <div className="flex items-center gap-4">
                            <div className="flex items-center gap-2">
                                <KbdGroup>
                                    <Kbd>
                                        <ArrowUpIcon className="h-3 w-3" />
                                    </Kbd>
                                    <Kbd>
                                        <ArrowDownIcon className="h-3 w-3" />
                                    </Kbd>
                                </KbdGroup>
                                <span className="text-xs text-muted-foreground">Navigate</span>
                            </div>
                            <div className="flex items-center gap-2">
                                <Kbd>
                                    <CornerDownLeftIcon className="h-3 w-3" />
                                </Kbd>
                                <span className="text-xs text-muted-foreground">Select</span>
                            </div>
                        </div>
                        <div className="flex items-center gap-2">
                            <Kbd>Esc</Kbd>
                            <span className="text-xs text-muted-foreground">Close</span>
                        </div>
                    </CommandFooter>
                </Command>
            </CommandDialogPopup>
        </CommandDialog>
    );
}
```

## File: `web/src/components/layout/header/components/theme-toggle.tsx`
```tsx
'use client';

import { useTheme } from 'next-themes';
import { useEffect, useState } from 'react';
import { Button } from '../../../ui/button';

export default function ThemeToggle() {
    const [mounted, setMounted] = useState(false);
    const { theme, setTheme } = useTheme();

    useEffect(() => {
        setMounted(true);
    }, []);

    if (!mounted) {
        return (
            <div className="w-9 h-9 rounded-md border border-zinc-200 dark:border-zinc-800" />
        );
    }

    return (
        <Button
            onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
            variant="ghost"
            size="icon"
            aria-label="Toggle theme"
        >
            {theme === 'dark' ? (
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width={24}
                    height={24}
                    viewBox="0 0 24 24"
                    fill="none"
                    className="-rotate-45 size-4 text-zinc-700 dark:text-zinc-300"
                    strokeWidth={2}
                    stroke="currentColor"
                >
                    <path
                        d="M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12Z"
                        stroke="currentColor"
                        strokeWidth={2}
                    />
                    <path
                        d="M5 20L19 5"
                        stroke="currentColor"
                        strokeLinejoin="round"
                        strokeWidth={2}
                    />
                    <path
                        d="M16 9L22 13.8528M12.4128 12.4059L19.3601 18.3634M8 15.6672L15 21.5"
                        stroke="currentColor"
                        strokeLinejoin="round"
                        strokeWidth={2}
                    />
                </svg>
            ) : (
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width={24}
                    height={24}
                    viewBox="0 0 24 24"
                    fill="none"
                    className="-rotate-225 size-4 text-zinc-700 dark:text-zinc-300"
                    strokeWidth={2}
                    stroke="currentColor"
                >
                    <path
                        d="M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12Z"
                        stroke="currentColor"
                        strokeWidth={2}
                    />
                    <path
                        d="M5 20L19 5"
                        stroke="currentColor"
                        strokeLinejoin="round"
                        strokeWidth={2}
                    />
                    <path
                        d="M16 9L22 13.8528M12.4128 12.4059L19.3601 18.3634M8 15.6672L15 21.5"
                        stroke="currentColor"
                        strokeLinejoin="round"
                        strokeWidth={2}
                    />
                </svg>
            )}
        </Button>
    );
}
```

## File: `web/src/components/mdx/Callout.tsx`
```tsx
import { ReactNode } from "react";
import { Info, AlertTriangle, AlertCircle, Lightbulb } from "lucide-react";

type CalloutType = "info" | "warning" | "error" | "tip";

interface CalloutProps {
  type?: CalloutType;
  title?: string;
  children: ReactNode;
}

const calloutStyles: Record<CalloutType, { bg: string; border: string; icon: typeof Info; iconColor: string }> = {
  info: {
    bg: "bg-blue-50 dark:bg-blue-950/30",
    border: "border-blue-200 dark:border-blue-800",
    icon: Info,
    iconColor: "text-blue-600 dark:text-blue-400",
  },
  warning: {
    bg: "bg-yellow-50 dark:bg-yellow-950/30",
    border: "border-yellow-200 dark:border-yellow-800",
    icon: AlertTriangle,
    iconColor: "text-yellow-600 dark:text-yellow-400",
  },
  error: {
    bg: "bg-red-50 dark:bg-red-950/30",
    border: "border-red-200 dark:border-red-800",
    icon: AlertCircle,
    iconColor: "text-red-600 dark:text-red-400",
  },
  tip: {
    bg: "bg-zinc-50 dark:bg-zinc-900/50",
    border: "border-zinc-200 dark:border-zinc-800",
    icon: Lightbulb,
    iconColor: "text-zinc-600 dark:text-zinc-400",
  },
};

export function Callout({ type = "info", title, children }: CalloutProps) {
  const styles = calloutStyles[type];
  const Icon = styles.icon;

  return (
    <div className={`${styles.bg} ${styles.border} border rounded-lg p-4 mb-4`}>
      <div className="flex items-start gap-3">
        <Icon className={`w-5 h-5 mt-0.5 shrink-0 ${styles.iconColor}`} />
        <div className="flex-1">
          {title && (
            <h4 className="text-sm font-semibold text-zinc-900 dark:text-zinc-50 mb-1">
              {title}
            </h4>
          )}
          <div className="text-sm text-zinc-700 dark:text-zinc-300 [&>p]:mb-0">
            {children}
          </div>
        </div>
      </div>
    </div>
  );
}
```

## File: `web/src/components/mdx/FeatureGrid.tsx`
```tsx
import { ReactNode } from "react";

interface FeatureProps {
  title: string;
  description?: string;
  children?: ReactNode;
}

export function Feature({ title, description, children }: FeatureProps) {
  return (
    <div className="p-3 bg-white dark:bg-zinc-900 rounded border border-zinc-100 dark:border-zinc-800 text-center">
      <div className="font-bold text-xs mb-1">{title}</div>
      {description && (
        <div className="text-[10px] text-zinc-500">{description}</div>
      )}
      {children}
    </div>
  );
}

interface FeatureGridProps {
  cols?: 2 | 3 | 4;
  children: ReactNode;
}

export function FeatureGrid({ cols = 4, children }: FeatureGridProps) {
  const colsClass = {
    2: "grid-cols-2",
    3: "grid-cols-3",
    4: "grid-cols-2 md:grid-cols-4",
  };

  return (
    <div className="bg-zinc-50 dark:bg-zinc-900/50 border border-zinc-200 dark:border-zinc-800 rounded-lg p-4 mb-6">
      <div className={`grid ${colsClass[cols]} gap-4`}>{children}</div>
    </div>
  );
}
```

## File: `web/src/components/mdx/index.ts`
```typescript
export { Callout } from "./Callout";
export { StepList, Step } from "./StepList";
export { Terminal, TerminalLine, TerminalBlock } from "./Terminal";
export { ProTips, Tip } from "./ProTips";
export { FeatureGrid, Feature } from "./FeatureGrid";
```

## File: `web/src/components/mdx/ProTips.tsx`
```tsx
import { ReactNode } from "react";

interface TipProps {
  title: string;
  children: ReactNode;
}

export function Tip({ title, children }: TipProps) {
  return (
    <div className="bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-lg p-4">
      <h4 className="text-sm font-semibold text-zinc-900 dark:text-zinc-50 mb-2">
        {title}
      </h4>
      <div className="text-sm text-zinc-600 dark:text-zinc-400 [&>p]:mb-0">
        {children}
      </div>
    </div>
  );
}

interface ProTipsProps {
  children: ReactNode;
}

export function ProTips({ children }: ProTipsProps) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8">{children}</div>
  );
}
```

## File: `web/src/components/mdx/StepList.tsx`
```tsx
import { ReactNode } from "react";

interface StepProps {
  number: number;
  title: string;
  children: ReactNode;
}

export function Step({ number, title, children }: StepProps) {
  return (
    <div className="flex gap-4">
      <div className="flex-none w-8 h-8 rounded-full bg-blue-100 dark:bg-blue-900/30 flex items-center justify-center text-blue-600 dark:text-blue-400 font-bold text-sm">
        {number}
      </div>
      <div className="flex-1 pb-6">
        <h3 className="font-semibold text-zinc-900 dark:text-zinc-50 mt-0 mb-2">
          {title}
        </h3>
        <div className="text-zinc-600 dark:text-zinc-400 text-sm [&>p]:mb-2">
          {children}
        </div>
      </div>
    </div>
  );
}

interface StepListProps {
  children: ReactNode;
}

export function StepList({ children }: StepListProps) {
  return <div className="space-y-2 mb-8">{children}</div>;
}
```

## File: `web/src/components/mdx/Terminal.tsx`
```tsx
import { ReactNode } from "react";

interface TerminalProps {
  children: ReactNode;
}

export function Terminal({ children }: TerminalProps) {
  return (
    <div className="bg-zinc-900 rounded-lg p-4 font-mono text-sm text-zinc-300 mb-6 overflow-x-auto">
      {children}
    </div>
  );
}

interface TerminalLineProps {
  type?: "user" | "agent" | "system";
  children: ReactNode;
}

export function TerminalLine({ type = "system", children }: TerminalLineProps) {
  const colors = {
    user: "text-green-400",
    agent: "text-blue-400",
    system: "text-zinc-400",
  };

  const labels = {
    user: "User:",
    agent: "Agent:",
    system: "",
  };

  return (
    <div className="mb-2">
      {labels[type] && (
        <span className={`${colors[type]} font-semibold`}>{labels[type]} </span>
      )}
      {children}
    </div>
  );
}

interface TerminalBlockProps {
  highlight?: boolean;
  children: ReactNode;
}

export function TerminalBlock({ highlight, children }: TerminalBlockProps) {
  return (
    <div
      className={`pl-4 border-l-2 ${
        highlight ? "border-green-800" : "border-zinc-800"
      } mb-4`}
    >
      {children}
    </div>
  );
}
```

## File: `web/src/components/ui/accordion.tsx`
```tsx
"use client";

import { Accordion as AccordionPrimitive } from "@base-ui/react/accordion";
import { ChevronDownIcon } from "lucide-react";

import { cn } from "@/lib/utils";

function Accordion(props: AccordionPrimitive.Root.Props) {
  return <AccordionPrimitive.Root data-slot="accordion" {...props} />;
}

function AccordionItem({ className, ...props }: AccordionPrimitive.Item.Props) {
  return (
    <AccordionPrimitive.Item
      className={cn("border-b last:border-b-0", className)}
      data-slot="accordion-item"
      {...props}
    />
  );
}

function AccordionTrigger({
  className,
  children,
  ...props
}: AccordionPrimitive.Trigger.Props) {
  return (
    <AccordionPrimitive.Header className="flex">
      <AccordionPrimitive.Trigger
        className={cn(
          "flex flex-1 cursor-pointer items-start justify-between gap-4 rounded-md py-4 text-left font-medium text-sm outline-none transition-all focus-visible:ring-[3px] focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-64 data-panel-open:*:data-[slot=accordion-indicator]:rotate-180",
          className,
        )}
        data-slot="accordion-trigger"
        {...props}
      >
        {children}
        <ChevronDownIcon
          className="pointer-events-none size-4 shrink-0 translate-y-0.5 opacity-80 transition-transform duration-200 ease-in-out"
          data-slot="accordion-indicator"
        />
      </AccordionPrimitive.Trigger>
    </AccordionPrimitive.Header>
  );
}

function AccordionPanel({
  className,
  children,
  ...props
}: AccordionPrimitive.Panel.Props) {
  return (
    <AccordionPrimitive.Panel
      className="h-(--accordion-panel-height) overflow-hidden text-muted-foreground text-sm transition-[height] duration-200 ease-in-out data-ending-style:h-0 data-starting-style:h-0"
      data-slot="accordion-panel"
      {...props}
    >
      <div className={cn("pt-0 pb-4", className)}>{children}</div>
    </AccordionPrimitive.Panel>
  );
}

export {
  Accordion,
  AccordionItem,
  AccordionTrigger,
  AccordionPanel,
  AccordionPanel as AccordionContent,
};
```

## File: `web/src/components/ui/alert-dialog.tsx`
```tsx
"use client";

import { AlertDialog as AlertDialogPrimitive } from "@base-ui/react/alert-dialog";

import { cn } from "@/lib/utils";

const AlertDialogCreateHandle = AlertDialogPrimitive.createHandle;

const AlertDialog = AlertDialogPrimitive.Root;

const AlertDialogPortal = AlertDialogPrimitive.Portal;

function AlertDialogTrigger(props: AlertDialogPrimitive.Trigger.Props) {
  return (
    <AlertDialogPrimitive.Trigger data-slot="alert-dialog-trigger" {...props} />
  );
}

function AlertDialogBackdrop({
  className,
  ...props
}: AlertDialogPrimitive.Backdrop.Props) {
  return (
    <AlertDialogPrimitive.Backdrop
      className={cn(
        "fixed inset-0 z-50 bg-black/32 backdrop-blur-sm transition-all duration-200 ease-out data-ending-style:opacity-0 data-starting-style:opacity-0",
        className,
      )}
      data-slot="alert-dialog-backdrop"
      {...props}
    />
  );
}

function AlertDialogViewport({
  className,
  ...props
}: AlertDialogPrimitive.Viewport.Props) {
  return (
    <AlertDialogPrimitive.Viewport
      className={cn(
        "fixed inset-0 z-50 grid grid-rows-[1fr_auto_3fr] justify-items-center p-4",
        className,
      )}
      data-slot="alert-dialog-viewport"
      {...props}
    />
  );
}

function AlertDialogPopup({
  className,
  bottomStickOnMobile = true,
  ...props
}: AlertDialogPrimitive.Popup.Props & {
  bottomStickOnMobile?: boolean;
}) {
  return (
    <AlertDialogPortal>
      <AlertDialogBackdrop />
      <AlertDialogViewport
        className={cn(
          bottomStickOnMobile &&
            "max-sm:grid-rows-[1fr_auto] max-sm:p-0 max-sm:pt-12",
        )}
      >
        <AlertDialogPrimitive.Popup
          className={cn(
            "-translate-y-[calc(1.25rem*var(--nested-dialogs))] relative row-start-2 flex max-h-full min-h-0 w-full min-w-0 max-w-lg scale-[calc(1-0.1*var(--nested-dialogs))] flex-col rounded-2xl border bg-popover not-dark:bg-clip-padding text-popover-foreground opacity-[calc(1-0.1*var(--nested-dialogs))] shadow-lg/5 transition-[scale,opacity,translate] duration-200 ease-in-out will-change-transform before:pointer-events-none before:absolute before:inset-0 before:rounded-[calc(var(--radius-2xl)-1px)] before:shadow-[0_1px_--theme(--color-black/6%)] data-nested:data-ending-style:translate-y-8 data-nested:data-starting-style:translate-y-8 data-nested-dialog-open:origin-top data-ending-style:scale-98 data-starting-style:scale-98 data-ending-style:opacity-0 data-starting-style:opacity-0 dark:before:shadow-[0_-1px_--theme(--color-white/6%)]",
            bottomStickOnMobile &&
              "max-sm:max-w-none max-sm:rounded-none max-sm:border-x-0 max-sm:border-t max-sm:border-b-0 max-sm:opacity-[calc(1-min(var(--nested-dialogs),1))] max-sm:data-ending-style:translate-y-4 max-sm:data-starting-style:translate-y-4 max-sm:before:hidden max-sm:before:rounded-none",
            className,
          )}
          data-slot="alert-dialog-popup"
          {...props}
        />
      </AlertDialogViewport>
    </AlertDialogPortal>
  );
}

function AlertDialogHeader({
  className,
  ...props
}: React.ComponentProps<"div">) {
  return (
    <div
      className={cn(
        "flex flex-col gap-2 p-6 not-has-[+[data-slot=alert-dialog-footer]]:pb-4 text-center max-sm:pb-4 sm:text-left",
        className,
      )}
      data-slot="alert-dialog-header"
      {...props}
    />
  );
}

function AlertDialogFooter({
  className,
  variant = "default",
  ...props
}: React.ComponentProps<"div"> & {
  variant?: "default" | "bare";
}) {
  return (
    <div
      className={cn(
        "flex flex-col-reverse gap-2 px-6 sm:flex-row sm:justify-end sm:rounded-b-[calc(var(--radius-2xl)-1px)]",
        variant === "default" && "border-t bg-muted/72 py-4",
        variant === "bare" && "pt-4 pb-6",
        className,
      )}
      data-slot="alert-dialog-footer"
      {...props}
    />
  );
}

function AlertDialogTitle({
  className,
  ...props
}: AlertDialogPrimitive.Title.Props) {
  return (
    <AlertDialogPrimitive.Title
      className={cn("font-heading text-xl leading-none", className)}
      data-slot="alert-dialog-title"
      {...props}
    />
  );
}

function AlertDialogDescription({
  className,
  ...props
}: AlertDialogPrimitive.Description.Props) {
  return (
    <AlertDialogPrimitive.Description
      className={cn("text-muted-foreground text-sm", className)}
      data-slot="alert-dialog-description"
      {...props}
    />
  );
}

function AlertDialogClose(props: AlertDialogPrimitive.Close.Props) {
  return (
    <AlertDialogPrimitive.Close data-slot="alert-dialog-close" {...props} />
  );
}

export {
  AlertDialogCreateHandle,
  AlertDialog,
  AlertDialogPortal,
  AlertDialogBackdrop,
  AlertDialogBackdrop as AlertDialogOverlay,
  AlertDialogTrigger,
  AlertDialogPopup,
  AlertDialogPopup as AlertDialogContent,
  AlertDialogHeader,
  AlertDialogFooter,
  AlertDialogTitle,
  AlertDialogDescription,
  AlertDialogClose,
  AlertDialogViewport,
};
```

## File: `web/src/components/ui/alert.tsx`
```tsx
import { cva, type VariantProps } from "class-variance-authority";
import type * as React from "react";

import { cn } from "@/lib/utils";

const alertVariants = cva(
  "relative grid w-full items-start gap-x-2 gap-y-0.5 rounded-xl border px-3.5 py-3 text-card-foreground text-sm has-[>svg]:has-data-[slot=alert-action]:grid-cols-[calc(var(--spacing)*4)_1fr_auto] has-[>svg]:grid-cols-[calc(var(--spacing)*4)_1fr] has-data-[slot=alert-action]:grid-cols-[1fr_auto] has-[>svg]:gap-x-2 [&>svg]:h-lh [&>svg]:w-4",
  {
    defaultVariants: {
      variant: "default",
    },
    variants: {
      variant: {
        default:
          "bg-transparent dark:bg-input/32 [&>svg]:text-muted-foreground",
        error:
          "border-destructive/32 bg-destructive/4 [&>svg]:text-destructive",
        info: "border-info/32 bg-info/4 [&>svg]:text-info",
        success: "border-success/32 bg-success/4 [&>svg]:text-success",
        warning: "border-warning/32 bg-warning/4 [&>svg]:text-warning",
      },
    },
  },
);

function Alert({
  className,
  variant,
  ...props
}: React.ComponentProps<"div"> & VariantProps<typeof alertVariants>) {
  return (
    <div
      className={cn(alertVariants({ variant }), className)}
      data-slot="alert"
      role="alert"
      {...props}
    />
  );
}

function AlertTitle({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      className={cn("font-medium [svg~&]:col-start-2", className)}
      data-slot="alert-title"
      {...props}
    />
  );
}

function AlertDescription({
  className,
  ...props
}: React.ComponentProps<"div">) {
  return (
    <div
      className={cn(
        "flex flex-col gap-2.5 text-muted-foreground [svg~&]:col-start-2",
        className,
      )}
      data-slot="alert-description"
      {...props}
    />
  );
}

function AlertAction({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      className={cn(
        "flex gap-1 max-sm:col-start-2 max-sm:mt-2 sm:row-start-1 sm:row-end-3 sm:self-center sm:[[data-slot=alert-description]~&]:col-start-2 sm:[[data-slot=alert-title]~&]:col-start-2 sm:[svg~&]:col-start-2 sm:[svg~[data-slot=alert-description]~&]:col-start-3 sm:[svg~[data-slot=alert-title]~&]:col-start-3",
        className,
      )}
      data-slot="alert-action"
      {...props}
    />
  );
}

export { Alert, AlertTitle, AlertDescription, AlertAction };
```

## File: `web/src/components/ui/autocomplete.tsx`
```tsx
"use client";

import { Autocomplete as AutocompletePrimitive } from "@base-ui/react/autocomplete";
import { ChevronsUpDownIcon, XIcon } from "lucide-react";

import { cn } from "@/lib/utils";
import { Input } from "@/components/ui/input";
import { ScrollArea } from "@/components/ui/scroll-area";

const Autocomplete = AutocompletePrimitive.Root;

function AutocompleteInput({
  className,
  showTrigger = false,
  showClear = false,
  startAddon,
  size,
  ...props
}: Omit<AutocompletePrimitive.Input.Props, "size"> & {
  showTrigger?: boolean;
  showClear?: boolean;
  startAddon?: React.ReactNode;
  size?: "sm" | "default" | "lg" | number;
  ref?: React.Ref<HTMLInputElement>;
}) {
  const sizeValue = (size ?? "default") as "sm" | "default" | "lg" | number;

  return (
    <div className="relative not-has-[>*.w-full]:w-fit w-full has-disabled:opacity-64">
      {startAddon && (
        <div
          aria-hidden="true"
          className="[&_svg]:-mx-0.5 pointer-events-none absolute inset-y-0 start-px z-10 flex items-center ps-[calc(--spacing(3)-1px)] opacity-80 has-[+[data-size=sm]]:ps-[calc(--spacing(2.5)-1px)] [&_svg:not([class*='size-'])]:size-4.5 sm:[&_svg:not([class*='size-'])]:size-4"
          data-slot="autocomplete-start-addon"
        >
          {startAddon}
        </div>
      )}
      <AutocompletePrimitive.Input
        className={cn(
          startAddon &&
            "data-[size=sm]:*:data-[slot=autocomplete-input]:ps-[calc(--spacing(7.5)-1px)] *:data-[slot=autocomplete-input]:ps-[calc(--spacing(8.5)-1px)] sm:data-[size=sm]:*:data-[slot=autocomplete-input]:ps-[calc(--spacing(7)-1px)] sm:*:data-[slot=autocomplete-input]:ps-[calc(--spacing(8)-1px)]",
          sizeValue === "sm"
            ? "has-[+[data-slot=autocomplete-trigger],+[data-slot=autocomplete-clear]]:*:data-[slot=autocomplete-input]:pe-6.5"
            : "has-[+[data-slot=autocomplete-trigger],+[data-slot=autocomplete-clear]]:*:data-[slot=autocomplete-input]:pe-7",
          className,
        )}
        data-slot="autocomplete-input"
        render={<Input nativeInput size={sizeValue} />}
        {...props}
      />
      {showTrigger && (
        <AutocompleteTrigger
          className={cn(
            "-translate-y-1/2 absolute top-1/2 inline-flex size-8 shrink-0 cursor-pointer items-center justify-center rounded-md border border-transparent opacity-80 outline-none transition-colors pointer-coarse:after:absolute pointer-coarse:after:min-h-11 pointer-coarse:after:min-w-11 hover:opacity-100 has-[+[data-slot=autocomplete-clear]]:hidden sm:size-7 [&_svg:not([class*='size-'])]:size-4.5 sm:[&_svg:not([class*='size-'])]:size-4 [&_svg]:pointer-events-none [&_svg]:shrink-0",
            sizeValue === "sm" ? "end-0" : "end-0.5",
          )}
        >
          <ChevronsUpDownIcon />
        </AutocompleteTrigger>
      )}
      {showClear && (
        <AutocompleteClear
          className={cn(
            "-translate-y-1/2 absolute top-1/2 inline-flex size-8 shrink-0 cursor-pointer items-center justify-center rounded-md border border-transparent opacity-80 outline-none transition-colors pointer-coarse:after:absolute pointer-coarse:after:min-h-11 pointer-coarse:after:min-w-11 hover:opacity-100 has-[+[data-slot=autocomplete-clear]]:hidden sm:size-7 [&_svg:not([class*='size-'])]:size-4.5 sm:[&_svg:not([class*='size-'])]:size-4 [&_svg]:pointer-events-none [&_svg]:shrink-0",
            sizeValue === "sm" ? "end-0" : "end-0.5",
          )}
        >
          <XIcon />
        </AutocompleteClear>
      )}
    </div>
  );
}

function AutocompletePopup({
  className,
  children,
  sideOffset = 4,
  ...props
}: AutocompletePrimitive.Popup.Props & {
  sideOffset?: number;
}) {
  return (
    <AutocompletePrimitive.Portal>
      <AutocompletePrimitive.Positioner
        className="z-50 select-none"
        data-slot="autocomplete-positioner"
        sideOffset={sideOffset}
      >
        <span
          className={cn(
            "relative flex max-h-full origin-(--transform-origin) rounded-lg border bg-popover not-dark:bg-clip-padding shadow-lg/5 transition-[scale,opacity] before:pointer-events-none before:absolute before:inset-0 before:rounded-[calc(var(--radius-lg)-1px)] before:shadow-[0_1px_--theme(--color-black/6%)] dark:before:shadow-[0_-1px_--theme(--color-white/6%)]",
            className,
          )}
        >
          <AutocompletePrimitive.Popup
            className="flex max-h-[min(var(--available-height),23rem)] w-(--anchor-width) max-w-(--available-width) flex-col"
            data-slot="autocomplete-popup"
            {...props}
          >
            {children}
          </AutocompletePrimitive.Popup>
        </span>
      </AutocompletePrimitive.Positioner>
    </AutocompletePrimitive.Portal>
  );
}

function AutocompleteItem({
  className,
  children,
  ...props
}: AutocompletePrimitive.Item.Props) {
  return (
    <AutocompletePrimitive.Item
      className={cn(
        "flex min-h-8 cursor-default select-none items-center rounded-sm px-2 py-1 text-base outline-none data-disabled:pointer-events-none data-highlighted:bg-accent data-highlighted:text-accent-foreground data-disabled:opacity-64 sm:min-h-7 sm:text-sm",
        className,
      )}
      data-slot="autocomplete-item"
      {...props}
    >
      {children}
    </AutocompletePrimitive.Item>
  );
}

function AutocompleteSeparator({
  className,
  ...props
}: AutocompletePrimitive.Separator.Props) {
  return (
    <AutocompletePrimitive.Separator
      className={cn("mx-2 my-1 h-px bg-border last:hidden", className)}
      data-slot="autocomplete-separator"
      {...props}
    />
  );
}

function AutocompleteGroup({
  className,
  ...props
}: AutocompletePrimitive.Group.Props) {
  return (
    <AutocompletePrimitive.Group
      className={cn("[[role=group]+&]:mt-1.5", className)}
      data-slot="autocomplete-group"
      {...props}
    />
  );
}

function AutocompleteGroupLabel({
  className,
  ...props
}: AutocompletePrimitive.GroupLabel.Props) {
  return (
    <AutocompletePrimitive.GroupLabel
      className={cn(
        "px-2 py-1.5 font-medium text-muted-foreground text-xs",
        className,
      )}
      data-slot="autocomplete-group-label"
      {...props}
    />
  );
}

function AutocompleteEmpty({
  className,
  ...props
}: AutocompletePrimitive.Empty.Props) {
  return (
    <AutocompletePrimitive.Empty
      className={cn(
        "not-empty:p-2 text-center text-base text-muted-foreground sm:text-sm",
        className,
      )}
      data-slot="autocomplete-empty"
      {...props}
    />
  );
}

function AutocompleteRow({
  className,
  ...props
}: AutocompletePrimitive.Row.Props) {
  return (
    <AutocompletePrimitive.Row
      className={className}
      data-slot="autocomplete-row"
      {...props}
    />
  );
}

function AutocompleteValue({ ...props }: AutocompletePrimitive.Value.Props) {
  return (
    <AutocompletePrimitive.Value data-slot="autocomplete-value" {...props} />
  );
}

function AutocompleteList({
  className,
  ...props
}: AutocompletePrimitive.List.Props) {
  return (
    <ScrollArea scrollbarGutter scrollFade>
      <AutocompletePrimitive.List
        className={cn(
          "not-empty:scroll-py-1 not-empty:p-1 in-data-has-overflow-y:pe-3",
          className,
        )}
        data-slot="autocomplete-list"
        {...props}
      />
    </ScrollArea>
  );
}

function AutocompleteClear({
  className,
  ...props
}: AutocompletePrimitive.Clear.Props) {
  return (
    <AutocompletePrimitive.Clear
      className={cn(
        "-translate-y-1/2 absolute end-0.5 top-1/2 inline-flex size-8 shrink-0 cursor-pointer items-center justify-center rounded-md border border-transparent opacity-80 outline-none transition-[color,background-color,box-shadow,opacity] pointer-coarse:after:absolute pointer-coarse:after:min-h-11 pointer-coarse:after:min-w-11 hover:opacity-100 sm:size-7 [&_svg:not([class*='size-'])]:size-4.5 sm:[&_svg:not([class*='size-'])]:size-4 [&_svg]:pointer-events-none [&_svg]:shrink-0",
        className,
      )}
      data-slot="autocomplete-clear"
      {...props}
    >
      <XIcon />
    </AutocompletePrimitive.Clear>
  );
}

function AutocompleteStatus({
  className,
  ...props
}: AutocompletePrimitive.Status.Props) {
  return (
    <AutocompletePrimitive.Status
      className={cn(
        "px-3 py-2 font-medium text-muted-foreground text-xs empty:m-0 empty:p-0",
        className,
      )}
      data-slot="autocomplete-status"
      {...props}
    />
  );
}

function AutocompleteCollection({
  ...props
}: AutocompletePrimitive.Collection.Props) {
  return (
    <AutocompletePrimitive.Collection
      data-slot="autocomplete-collection"
      {...props}
    />
  );
}

function AutocompleteTrigger({
  className,
  ...props
}: AutocompletePrimitive.Trigger.Props) {
  return (
    <AutocompletePrimitive.Trigger
      className={className}
      data-slot="autocomplete-trigger"
      {...props}
    />
  );
}

const useAutocompleteFilter = AutocompletePrimitive.useFilter;

export {
  Autocomplete,
  AutocompleteInput,
  AutocompleteTrigger,
  AutocompletePopup,
  AutocompleteItem,
  AutocompleteSeparator,
  AutocompleteGroup,
  AutocompleteGroupLabel,
  AutocompleteEmpty,
  AutocompleteValue,
  AutocompleteList,
  AutocompleteClear,
  AutocompleteStatus,
  AutocompleteRow,
  AutocompleteCollection,
  useAutocompleteFilter,
};
```

## File: `web/src/components/ui/avatar.tsx`
```tsx
"use client";

import { Avatar as AvatarPrimitive } from "@base-ui/react/avatar";

import { cn } from "@/lib/utils";

function Avatar({ className, ...props }: AvatarPrimitive.Root.Props) {
  return (
    <AvatarPrimitive.Root
      className={cn(
        "inline-flex size-8 shrink-0 select-none items-center justify-center overflow-hidden rounded-full bg-background align-middle font-medium text-xs",
        className,
      )}
      data-slot="avatar"
      {...props}
    />
  );
}

function AvatarImage({ className, ...props }: AvatarPrimitive.Image.Props) {
  return (
    <AvatarPrimitive.Image
      className={cn("size-full object-cover", className)}
      data-slot="avatar-image"
      {...props}
    />
  );
}

function AvatarFallback({
  className,
  ...props
}: AvatarPrimitive.Fallback.Props) {
  return (
    <AvatarPrimitive.Fallback
      className={cn(
        "flex size-full items-center justify-center rounded-full bg-muted",
        className,
      )}
      data-slot="avatar-fallback"
      {...props}
    />
  );
}

export { Avatar, AvatarImage, AvatarFallback };
```

## File: `web/src/components/ui/badge.tsx`
```tsx
"use client";

import { mergeProps } from "@base-ui/react/merge-props";
import { useRender } from "@base-ui/react/use-render";
import { cva, type VariantProps } from "class-variance-authority";

import { cn } from "@/lib/utils";

const badgeVariants = cva(
  "relative inline-flex shrink-0 items-center justify-center gap-1 whitespace-nowrap rounded-sm border border-transparent font-medium outline-none transition-shadow focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-1 focus-visible:ring-offset-background disabled:pointer-events-none disabled:opacity-64 [&_svg:not([class*='opacity-'])]:opacity-80 [&_svg:not([class*='size-'])]:size-3.5 sm:[&_svg:not([class*='size-'])]:size-3 [&_svg]:pointer-events-none [&_svg]:shrink-0 [button,a&]:cursor-pointer [button,a&]:pointer-coarse:after:absolute [button,a&]:pointer-coarse:after:size-full [button,a&]:pointer-coarse:after:min-h-11 [button,a&]:pointer-coarse:after:min-w-11",
  {
    defaultVariants: {
      size: "default",
      variant: "default",
    },
    variants: {
      size: {
        default:
          "h-5.5 min-w-5.5 px-[calc(--spacing(1)-1px)] text-sm sm:h-4.5 sm:min-w-4.5 sm:text-xs",
        lg: "h-6.5 min-w-6.5 px-[calc(--spacing(1.5)-1px)] text-base sm:h-5.5 sm:min-w-5.5 sm:text-sm",
        sm: "h-5 min-w-5 rounded-[calc(var(--radius-sm)-2px)] px-[calc(--spacing(1)-1px)] text-xs sm:h-4 sm:min-w-4 sm:text-[.625rem]",
      },
      variant: {
        default:
          "bg-primary text-primary-foreground [button,a&]:hover:bg-primary/90",
        destructive:
          "bg-destructive text-white [button,a&]:hover:bg-destructive/90",
        error:
          "bg-destructive/8 text-destructive-foreground dark:bg-destructive/16",
        info: "bg-info/8 text-info-foreground dark:bg-info/16",
        outline:
          "border-input bg-background dark:bg-input/32 [button,a&]:hover:bg-accent/50 dark:[button,a&]:hover:bg-input/48",
        secondary:
          "bg-secondary text-secondary-foreground [button,a&]:hover:bg-secondary/90",
        success: "bg-success/8 text-success-foreground dark:bg-success/16",
        warning: "bg-warning/8 text-warning-foreground dark:bg-warning/16",
      },
    },
  },
);

interface BadgeProps extends useRender.ComponentProps<"span"> {
  variant?: VariantProps<typeof badgeVariants>["variant"];
  size?: VariantProps<typeof badgeVariants>["size"];
}

function Badge({ className, variant, size, render, ...props }: BadgeProps) {
  const defaultProps = {
    className: cn(badgeVariants({ className, size, variant })),
    "data-slot": "badge",
  };

  return useRender({
    defaultTagName: "span",
    props: mergeProps<"span">(defaultProps, props),
    render,
  });
}

export { Badge, badgeVariants };
```

## File: `web/src/components/ui/breadcrumb.tsx`
```tsx
"use client";

import { mergeProps } from "@base-ui/react/merge-props";
import { useRender } from "@base-ui/react/use-render";
import { ChevronRight, MoreHorizontal } from "lucide-react";
import type * as React from "react";

import { cn } from "@/lib/utils";

function Breadcrumb({ ...props }: React.ComponentProps<"nav">) {
  return <nav aria-label="breadcrumb" data-slot="breadcrumb" {...props} />;
}

function BreadcrumbList({ className, ...props }: React.ComponentProps<"ol">) {
  return (
    <ol
      className={cn(
        "wrap-break-word flex flex-wrap items-center gap-1.5 text-muted-foreground text-sm sm:gap-2.5",
        className,
      )}
      data-slot="breadcrumb-list"
      {...props}
    />
  );
}

function BreadcrumbItem({ className, ...props }: React.ComponentProps<"li">) {
  return (
    <li
      className={cn("inline-flex items-center gap-1.5", className)}
      data-slot="breadcrumb-item"
      {...props}
    />
  );
}

function BreadcrumbLink({
  className,
  render,
  ...props
}: useRender.ComponentProps<"a">) {
  const defaultProps = {
    className: cn("transition-colors hover:text-foreground", className),
    "data-slot": "breadcrumb-link",
  };

  return useRender({
    defaultTagName: "a",
    props: mergeProps<"a">(defaultProps, props),
    render,
  });
}

function BreadcrumbPage({ className, ...props }: React.ComponentProps<"span">) {
  return (
    // biome-ignore lint(a11y/useFocusableInteractive): known
    <span
      aria-current="page"
      aria-disabled="true"
      className={cn("font-normal text-foreground", className)}
      data-slot="breadcrumb-page"
      role="link"
      {...props}
    />
  );
}

function BreadcrumbSeparator({
  children,
  className,
  ...props
}: React.ComponentProps<"li">) {
  return (
    <li
      aria-hidden="true"
      className={cn("opacity-80 [&>svg]:size-4", className)}
      data-slot="breadcrumb-separator"
      role="presentation"
      {...props}
    >
      {children ?? <ChevronRight />}
    </li>
  );
}

function BreadcrumbEllipsis({
  className,
  ...props
}: React.ComponentProps<"span">) {
  return (
    <span
      aria-hidden="true"
      className={className}
      data-slot="breadcrumb-ellipsis"
      role="presentation"
      {...props}
    >
      <MoreHorizontal className="size-4" />
      <span className="sr-only">More</span>
    </span>
  );
}

export {
  Breadcrumb,
  BreadcrumbList,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbPage,
  BreadcrumbSeparator,
  BreadcrumbEllipsis,
};
```

## File: `web/src/components/ui/button.tsx`
```tsx
"use client";

import { mergeProps } from "@base-ui/react/merge-props";
import { useRender } from "@base-ui/react/use-render";
import { cva, type VariantProps } from "class-variance-authority";
import type * as React from "react";

import { cn } from "@/lib/utils";

const buttonVariants = cva(
  "[&_svg]:-mx-0.5 relative inline-flex shrink-0 cursor-pointer items-center justify-center gap-2 whitespace-nowrap rounded-lg border font-medium text-base outline-none transition-shadow before:pointer-events-none before:absolute before:inset-0 before:rounded-[calc(var(--radius-lg)-1px)] pointer-coarse:after:absolute pointer-coarse:after:size-full pointer-coarse:after:min-h-11 pointer-coarse:after:min-w-11 focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-1 focus-visible:ring-offset-background disabled:pointer-events-none disabled:opacity-64 sm:text-sm [&_svg:not([class*='opacity-'])]:opacity-80 [&_svg:not([class*='size-'])]:size-4.5 sm:[&_svg:not([class*='size-'])]:size-4 [&_svg]:pointer-events-none [&_svg]:shrink-0",
  {
    defaultVariants: {
      size: "default",
      variant: "default",
    },
    variants: {
      size: {
        default: "h-9 px-[calc(--spacing(3)-1px)] sm:h-8",
        icon: "size-9 sm:size-8",
        "icon-lg": "size-10 sm:size-9",
        "icon-sm": "size-8 sm:size-7",
        "icon-xl":
          "size-11 sm:size-10 [&_svg:not([class*='size-'])]:size-5 sm:[&_svg:not([class*='size-'])]:size-4.5",
        "icon-xs":
          "size-7 rounded-md before:rounded-[calc(var(--radius-md)-1px)] sm:size-6 not-in-data-[slot=input-group]:[&_svg:not([class*='size-'])]:size-4 sm:not-in-data-[slot=input-group]:[&_svg:not([class*='size-'])]:size-3.5",
        lg: "h-10 px-[calc(--spacing(3.5)-1px)] sm:h-9",
        sm: "h-8 gap-1.5 px-[calc(--spacing(2.5)-1px)] sm:h-7",
        xl: "h-11 px-[calc(--spacing(4)-1px)] text-lg sm:h-10 sm:text-base [&_svg:not([class*='size-'])]:size-5 sm:[&_svg:not([class*='size-'])]:size-4.5",
        xs: "h-7 gap-1 rounded-md px-[calc(--spacing(2)-1px)] text-sm before:rounded-[calc(var(--radius-md)-1px)] sm:h-6 sm:text-xs [&_svg:not([class*='size-'])]:size-4 sm:[&_svg:not([class*='size-'])]:size-3.5",
      },
      variant: {
        default:
          "not-disabled:inset-shadow-[0_1px_--theme(--color-white/16%)] border-primary bg-primary text-primary-foreground shadow-primary/24 shadow-xs [:active,[data-pressed]]:inset-shadow-[0_1px_--theme(--color-black/8%)] [:disabled,:active,[data-pressed]]:shadow-none [:hover,[data-pressed]]:bg-primary/90",
        destructive:
          "not-disabled:inset-shadow-[0_1px_--theme(--color-white/16%)] border-destructive bg-destructive text-white shadow-destructive/24 shadow-xs [:active,[data-pressed]]:inset-shadow-[0_1px_--theme(--color-black/8%)] [:disabled,:active,[data-pressed]]:shadow-none [:hover,[data-pressed]]:bg-destructive/90",
        "destructive-outline":
          "border-input bg-transparent not-dark:bg-clip-padding text-destructive-foreground shadow-xs/5 not-disabled:not-active:not-data-pressed:before:shadow-[0_1px_--theme(--color-black/6%)] dark:bg-input/32 dark:not-disabled:before:shadow-[0_-1px_--theme(--color-white/2%)] dark:not-disabled:not-active:not-data-pressed:before:shadow-[0_-1px_--theme(--color-white/6%)] [:disabled,:active,[data-pressed]]:shadow-none [:hover,[data-pressed]]:border-destructive/32 [:hover,[data-pressed]]:bg-destructive/4",
        ghost:
          "border-transparent data-pressed:bg-accent [:hover,[data-pressed]]:bg-accent",
        link: "border-transparent underline-offset-4 [:hover,[data-pressed]]:underline",
        outline:
          "border-input bg-background not-dark:bg-clip-padding shadow-xs/5 not-disabled:not-active:not-data-pressed:before:shadow-[0_1px_--theme(--color-black/6%)] dark:bg-input/32 dark:not-disabled:before:shadow-[0_-1px_--theme(--color-white/2%)] dark:not-disabled:not-active:not-data-pressed:before:shadow-[0_-1px_--theme(--color-white/6%)] [:disabled,:active,[data-pressed]]:shadow-none [:hover,[data-pressed]]:bg-accent/50 dark:[:hover,[data-pressed]]:bg-input/64",
        secondary:
          "border-transparent bg-secondary text-secondary-foreground [:active,[data-pressed]]:bg-secondary/80 [:hover,[data-pressed]]:bg-secondary/90",
      },
    },
  },
);

interface ButtonProps extends useRender.ComponentProps<"button"> {
  variant?: VariantProps<typeof buttonVariants>["variant"];
  size?: VariantProps<typeof buttonVariants>["size"];
}

function Button({ className, variant, size, render, ...props }: ButtonProps) {
  const typeValue: React.ButtonHTMLAttributes<HTMLButtonElement>["type"] =
    render ? undefined : "button";

  const defaultProps = {
    className: cn(buttonVariants({ className, size, variant })),
    "data-slot": "button",
    type: typeValue,
  };

  return useRender({
    defaultTagName: "button",
    props: mergeProps<"button">(defaultProps, props),
    render,
  });
}

export { Button, buttonVariants };
```

## File: `web/src/components/ui/card.tsx`
```tsx
"use client";

import { mergeProps } from "@base-ui/react/merge-props";
import { useRender } from "@base-ui/react/use-render";

import { cn } from "@/lib/utils";

function Card({
  className,
  render,
  ...props
}: useRender.ComponentProps<"div">) {
  const defaultProps = {
    className: cn(
      "relative flex flex-col gap-6 rounded-2xl border bg-card not-dark:bg-clip-padding py-6 text-card-foreground shadow-xs/5 before:pointer-events-none before:absolute before:inset-0 before:rounded-[calc(var(--radius-2xl)-1px)] before:shadow-[0_1px_--theme(--color-black/6%)] dark:before:shadow-[0_-1px_--theme(--color-white/6%)]",
      className,
    ),
    "data-slot": "card",
  };

  return useRender({
    defaultTagName: "div",
    props: mergeProps<"div">(defaultProps, props),
    render,
  });
}

function CardHeader({
  className,
  render,
  ...props
}: useRender.ComponentProps<"div">) {
  const defaultProps = {
    className: cn(
      "@container/card-header grid auto-rows-min grid-rows-[auto_auto] items-start gap-1.5 px-6 has-data-[slot=card-action]:grid-cols-[1fr_auto] [.border-b]:pb-6",
      className,
    ),
    "data-slot": "card-header",
  };

  return useRender({
    defaultTagName: "div",
    props: mergeProps<"div">(defaultProps, props),
    render,
  });
}

function CardTitle({
  className,
  render,
  ...props
}: useRender.ComponentProps<"div">) {
  const defaultProps = {
    className: cn("font-semibold text-lg leading-none", className),
    "data-slot": "card-title",
  };

  return useRender({
    defaultTagName: "div",
    props: mergeProps<"div">(defaultProps, props),
    render,
  });
}

function CardDescription({
  className,
  render,
  ...props
}: useRender.ComponentProps<"div">) {
  const defaultProps = {
    className: cn("text-muted-foreground text-sm", className),
    "data-slot": "card-description",
  };

  return useRender({
    defaultTagName: "div",
    props: mergeProps<"div">(defaultProps, props),
    render,
  });
}

function CardAction({
  className,
  render,
  ...props
}: useRender.ComponentProps<"div">) {
  const defaultProps = {
    className: cn(
      "col-start-2 row-span-2 row-start-1 self-start justify-self-end",
      className,
    ),
    "data-slot": "card-action",
  };

  return useRender({
    defaultTagName: "div",
    props: mergeProps<"div">(defaultProps, props),
    render,
  });
}

function CardPanel({
  className,
  render,
  ...props
}: useRender.ComponentProps<"div">) {
  const defaultProps = {
    className: cn("px-6", className),
    "data-slot": "card-content",
  };

  return useRender({
    defaultTagName: "div",
    props: mergeProps<"div">(defaultProps, props),
    render,
  });
}

function CardFooter({
  className,
  render,
  ...props
}: useRender.ComponentProps<"div">) {
  const defaultProps = {
    className: cn("flex items-center px-6 [.border-t]:pt-6", className),
    "data-slot": "card-footer",
  };

  return useRender({
    defaultTagName: "div",
    props: mergeProps<"div">(defaultProps, props),
    render,
  });
}

export {
  Card,
  CardAction,
  CardDescription,
  CardFooter,
  CardHeader,
  CardPanel,
  CardPanel as CardContent,
  CardTitle,
};
```

## File: `web/src/components/ui/checkbox-group.tsx`
```tsx
"use client";

import { CheckboxGroup as CheckboxGroupPrimitive } from "@base-ui/react/checkbox-group";

import { cn } from "@/lib/utils";

function CheckboxGroup({ className, ...props }: CheckboxGroupPrimitive.Props) {
  return (
    <CheckboxGroupPrimitive
      className={cn("flex flex-col items-start gap-3", className)}
      {...props}
    />
  );
}

export { CheckboxGroup };
```

## File: `web/src/components/ui/checkbox.tsx`
```tsx
"use client";

import { Checkbox as CheckboxPrimitive } from "@base-ui/react/checkbox";

import { cn } from "@/lib/utils";

function Checkbox({ className, ...props }: CheckboxPrimitive.Root.Props) {
  return (
    <CheckboxPrimitive.Root
      className={cn(
        "relative inline-flex size-4.5 shrink-0 items-center justify-center rounded-[4px] border border-input bg-background not-dark:bg-clip-padding shadow-xs/5 outline-none ring-ring transition-shadow before:pointer-events-none before:absolute before:inset-0 before:rounded-[3px] not-data-disabled:not-data-checked:not-aria-invalid:before:shadow-[0_1px_--theme(--color-black/6%)] focus-visible:ring-2 focus-visible:ring-offset-1 focus-visible:ring-offset-background aria-invalid:border-destructive/36 focus-visible:aria-invalid:border-destructive/64 focus-visible:aria-invalid:ring-destructive/48 data-disabled:opacity-64 sm:size-4 dark:not-data-checked:bg-input/32 dark:aria-invalid:ring-destructive/24 dark:not-data-disabled:not-data-checked:not-aria-invalid:before:shadow-[0_-1px_--theme(--color-white/6%)] [[data-disabled],[data-checked],[aria-invalid]]:shadow-none",
        className,
      )}
      data-slot="checkbox"
      {...props}
    >
      <CheckboxPrimitive.Indicator
        className="-inset-px absolute flex items-center justify-center rounded-[4px] text-primary-foreground data-unchecked:hidden data-checked:bg-primary data-indeterminate:text-foreground"
        data-slot="checkbox-indicator"
        render={(props, state) => (
          <span {...props}>
            {state.indeterminate ? (
              <svg
                className="size-3.5 sm:size-3"
                fill="none"
                height="24"
                stroke="currentColor"
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="3"
                viewBox="0 0 24 24"
                width="24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path d="M5.252 12h13.496" />
              </svg>
            ) : (
              <svg
                className="size-3.5 sm:size-3"
                fill="none"
                height="24"
                stroke="currentColor"
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="3"
                viewBox="0 0 24 24"
                width="24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path d="M5.252 12.7 10.2 18.63 18.748 5.37" />
              </svg>
            )}
          </span>
        )}
      />
    </CheckboxPrimitive.Root>
  );
}

export { Checkbox };
```

## File: `web/src/components/ui/collapsible.tsx`
```tsx
"use client";

import { Collapsible as CollapsiblePrimitive } from "@base-ui/react/collapsible";

import { cn } from "@/lib/utils";

function Collapsible({ ...props }: CollapsiblePrimitive.Root.Props) {
  return <CollapsiblePrimitive.Root data-slot="collapsible" {...props} />;
}

function CollapsibleTrigger({
  className,
  ...props
}: CollapsiblePrimitive.Trigger.Props) {
  return (
    <CollapsiblePrimitive.Trigger
      className={cn("cursor-pointer", className)}
      data-slot="collapsible-trigger"
      {...props}
    />
  );
}

function CollapsiblePanel({
  className,
  ...props
}: CollapsiblePrimitive.Panel.Props) {
  return (
    <CollapsiblePrimitive.Panel
      className={cn(
        "h-(--collapsible-panel-height) overflow-hidden transition-[height] duration-200 data-ending-style:h-0 data-starting-style:h-0",
        className,
      )}
      data-slot="collapsible-panel"
      {...props}
    />
  );
}

export {
  Collapsible,
  CollapsibleTrigger,
  CollapsiblePanel,
  CollapsiblePanel as CollapsibleContent,
};
```

## File: `web/src/components/ui/combobox.tsx`
```tsx
"use client";

import { Combobox as ComboboxPrimitive } from "@base-ui/react/combobox";
import { ChevronsUpDownIcon, XIcon } from "lucide-react";
import * as React from "react";

import { cn } from "@/lib/utils";
import { Input } from "@/components/ui/input";
import { ScrollArea } from "@/components/ui/scroll-area";

const ComboboxContext = React.createContext<{
  chipsRef: React.RefObject<Element | null> | null;
  multiple: boolean;
}>({
  chipsRef: null,
  multiple: false,
});

type ComboboxRootProps<
  ItemValue,
  Multiple extends boolean | undefined,
> = Parameters<typeof ComboboxPrimitive.Root<ItemValue, Multiple>>[0];

function Combobox<ItemValue, Multiple extends boolean | undefined = false>(
  props: ComboboxPrimitive.Root.Props<ItemValue, Multiple>,
) {
  const chipsRef = React.useRef<Element | null>(null);
  return (
    <ComboboxContext.Provider value={{ chipsRef, multiple: !!props.multiple }}>
      <ComboboxPrimitive.Root
        {...(props as ComboboxRootProps<ItemValue, Multiple>)}
      />
    </ComboboxContext.Provider>
  );
}

function ComboboxInput({
  className,
  showTrigger = true,
  showClear = false,
  startAddon,
  size,
  ...props
}: Omit<ComboboxPrimitive.Input.Props, "size"> & {
  showTrigger?: boolean;
  showClear?: boolean;
  startAddon?: React.ReactNode;
  size?: "sm" | "default" | "lg" | number;
  ref?: React.Ref<HTMLInputElement>;
}) {
  const { multiple } = React.useContext(ComboboxContext);
  const sizeValue = (size ?? "default") as "sm" | "default" | "lg" | number;

  // multiple mode
  if (multiple) {
    return (
      <ComboboxPrimitive.Input
        className={cn(
          "min-w-12 flex-1 text-base outline-none sm:text-sm [[data-slot=combobox-chip]+&]:ps-0.5",
          sizeValue === "sm" ? "ps-1.5" : "ps-2",
          className,
        )}
        data-size={typeof sizeValue === "string" ? sizeValue : undefined}
        data-slot="combobox-input"
        size={typeof sizeValue === "number" ? sizeValue : undefined}
        {...props}
      />
    );
  }

  // single mode
  return (
    <div className="relative not-has-[>*.w-full]:w-fit w-full has-disabled:opacity-64">
      {startAddon && (
        <div
          aria-hidden="true"
          className="[&_svg]:-mx-0.5 pointer-events-none absolute inset-y-0 start-px z-10 flex items-center ps-[calc(--spacing(3)-1px)] opacity-80 has-[+[data-size=sm]]:ps-[calc(--spacing(2.5)-1px)] [&_svg:not([class*='size-'])]:size-4.5 sm:[&_svg:not([class*='size-'])]:size-4"
          data-slot="combobox-start-addon"
        >
          {startAddon}
        </div>
      )}
      <ComboboxPrimitive.Input
        className={cn(
          startAddon &&
            "data-[size=sm]:*:data-[slot=combobox-input]:ps-[calc(--spacing(7.5)-1px)] *:data-[slot=combobox-input]:ps-[calc(--spacing(8.5)-1px)] sm:data-[size=sm]:*:data-[slot=combobox-input]:ps-[calc(--spacing(7)-1px)] sm:*:data-[slot=combobox-input]:ps-[calc(--spacing(8)-1px)]",
          sizeValue === "sm"
            ? "has-[+[data-slot=combobox-trigger],+[data-slot=combobox-clear]]:*:data-[slot=combobox-input]:pe-6.5"
            : "has-[+[data-slot=combobox-trigger],+[data-slot=combobox-clear]]:*:data-[slot=combobox-input]:pe-7",
          className,
        )}
        data-slot="combobox-input"
        render={
          <Input
            className="has-disabled:opacity-100"
            nativeInput
            size={sizeValue}
          />
        }
        {...props}
      />
      {showTrigger && (
        <ComboboxTrigger
          className={cn(
            "-translate-y-1/2 absolute top-1/2 inline-flex size-8 shrink-0 cursor-pointer items-center justify-center rounded-md border border-transparent opacity-80 outline-none transition-opacity pointer-coarse:after:absolute pointer-coarse:after:min-h-11 pointer-coarse:after:min-w-11 hover:opacity-100 has-[+[data-slot=combobox-clear]]:hidden sm:size-7 [&_svg:not([class*='size-'])]:size-4.5 sm:[&_svg:not([class*='size-'])]:size-4 [&_svg]:pointer-events-none [&_svg]:shrink-0",
            sizeValue === "sm" ? "end-0" : "end-0.5",
          )}
        >
          <ChevronsUpDownIcon />
        </ComboboxTrigger>
      )}
      {showClear && (
        <ComboboxClear
          className={cn(
            "-translate-y-1/2 absolute top-1/2 inline-flex size-8 shrink-0 cursor-pointer items-center justify-center rounded-md border border-transparent opacity-80 outline-none transition-opacity pointer-coarse:after:absolute pointer-coarse:after:min-h-11 pointer-coarse:after:min-w-11 hover:opacity-100 has-[+[data-slot=combobox-clear]]:hidden sm:size-7 [&_svg:not([class*='size-'])]:size-4.5 sm:[&_svg:not([class*='size-'])]:size-4 [&_svg]:pointer-events-none [&_svg]:shrink-0",
            sizeValue === "sm" ? "end-0" : "end-0.5",
          )}
        >
          <XIcon />
        </ComboboxClear>
      )}
    </div>
  );
}

function ComboboxTrigger({
  className,
  ...props
}: ComboboxPrimitive.Trigger.Props) {
  return (
    <ComboboxPrimitive.Trigger
      className={className}
      data-slot="combobox-trigger"
      {...props}
    />
  );
}

function ComboboxPopup({
  className,
  children,
  sideOffset = 4,
  ...props
}: ComboboxPrimitive.Popup.Props & {
  sideOffset?: number;
}) {
  const { chipsRef } = React.useContext(ComboboxContext);

  return (
    <ComboboxPrimitive.Portal>
      <ComboboxPrimitive.Positioner
        anchor={chipsRef}
        className="z-50 select-none"
        data-slot="combobox-positioner"
        sideOffset={sideOffset}
      >
        <span
          className={cn(
            "relative flex max-h-full origin-(--transform-origin) rounded-lg border bg-popover not-dark:bg-clip-padding shadow-lg/5 transition-[scale,opacity] before:pointer-events-none before:absolute before:inset-0 before:rounded-[calc(var(--radius-lg)-1px)] before:shadow-[0_1px_--theme(--color-black/6%)] dark:before:shadow-[0_-1px_--theme(--color-white/6%)]",
            className,
          )}
        >
          <ComboboxPrimitive.Popup
            className="flex max-h-[min(var(--available-height),23rem)] w-(--anchor-width) max-w-(--available-width) flex-col"
            data-slot="combobox-popup"
            {...props}
          >
            {children}
          </ComboboxPrimitive.Popup>
        </span>
      </ComboboxPrimitive.Positioner>
    </ComboboxPrimitive.Portal>
  );
}

function ComboboxItem({
  className,
  children,
  ...props
}: ComboboxPrimitive.Item.Props) {
  return (
    <ComboboxPrimitive.Item
      className={cn(
        "grid min-h-8 in-data-[side=none]:min-w-[calc(var(--anchor-width)+1.25rem)] cursor-default grid-cols-[1rem_1fr] items-center gap-2 rounded-sm py-1 ps-2 pe-4 text-base outline-none data-disabled:pointer-events-none data-highlighted:bg-accent data-highlighted:text-accent-foreground data-disabled:opacity-64 sm:min-h-7 sm:text-sm [&_svg:not([class*='size-'])]:size-4.5 sm:[&_svg:not([class*='size-'])]:size-4 [&_svg]:pointer-events-none [&_svg]:shrink-0",
        className,
      )}
      data-slot="combobox-item"
      {...props}
    >
      <ComboboxPrimitive.ItemIndicator className="col-start-1">
        <svg
          fill="none"
          height="24"
          stroke="currentColor"
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth="2"
          viewBox="0 0 24 24"
          width="24"
          xmlns="http://www.w3.org/1500/svg"
        >
          <path d="M5.252 12.7 10.2 18.63 18.748 5.37" />
        </svg>
      </ComboboxPrimitive.ItemIndicator>
      <div className="col-start-2">{children}</div>
    </ComboboxPrimitive.Item>
  );
}

function ComboboxSeparator({
  className,
  ...props
}: ComboboxPrimitive.Separator.Props) {
  return (
    <ComboboxPrimitive.Separator
      className={cn("mx-2 my-1 h-px bg-border last:hidden", className)}
      data-slot="combobox-separator"
      {...props}
    />
  );
}

function ComboboxGroup({ className, ...props }: ComboboxPrimitive.Group.Props) {
  return (
    <ComboboxPrimitive.Group
      className={cn("[[role=group]+&]:mt-1.5", className)}
      data-slot="combobox-group"
      {...props}
    />
  );
}

function ComboboxGroupLabel({
  className,
  ...props
}: ComboboxPrimitive.GroupLabel.Props) {
  return (
    <ComboboxPrimitive.GroupLabel
      className={cn(
        "px-2 py-1.5 font-medium text-muted-foreground text-xs",
        className,
      )}
      data-slot="combobox-group-label"
      {...props}
    />
  );
}

function ComboboxEmpty({ className, ...props }: ComboboxPrimitive.Empty.Props) {
  return (
    <ComboboxPrimitive.Empty
      className={cn(
        "not-empty:p-2 text-center text-base text-muted-foreground sm:text-sm",
        className,
      )}
      data-slot="combobox-empty"
      {...props}
    />
  );
}

function ComboboxRow({ className, ...props }: ComboboxPrimitive.Row.Props) {
  return (
    <ComboboxPrimitive.Row
      className={className}
      data-slot="combobox-row"
      {...props}
    />
  );
}

function ComboboxValue({ ...props }: ComboboxPrimitive.Value.Props) {
  return <ComboboxPrimitive.Value data-slot="combobox-value" {...props} />;
}

function ComboboxList({ className, ...props }: ComboboxPrimitive.List.Props) {
  return (
    <ScrollArea scrollbarGutter scrollFade>
      <ComboboxPrimitive.List
        className={cn(
          "not-empty:scroll-py-1 not-empty:px-1 not-empty:py-1 in-data-has-overflow-y:pe-3",
          className,
        )}
        data-slot="combobox-list"
        {...props}
      />
    </ScrollArea>
  );
}

function ComboboxClear({ className, ...props }: ComboboxPrimitive.Clear.Props) {
  return (
    <ComboboxPrimitive.Clear
      className={className}
      data-slot="combobox-clear"
      {...props}
    />
  );
}

function ComboboxStatus({
  className,
  ...props
}: ComboboxPrimitive.Status.Props) {
  return (
    <ComboboxPrimitive.Status
      className={cn(
        "px-3 py-2 font-medium text-muted-foreground text-xs empty:m-0 empty:p-0",
        className,
      )}
      data-slot="combobox-status"
      {...props}
    />
  );
}

function ComboboxCollection(props: ComboboxPrimitive.Collection.Props) {
  return (
    <ComboboxPrimitive.Collection data-slot="combobox-collection" {...props} />
  );
}

function ComboboxChips({
  className,
  children,
  startAddon,
  ...props
}: ComboboxPrimitive.Chips.Props & {
  startAddon?: React.ReactNode;
}) {
  const { chipsRef } = React.useContext(ComboboxContext);

  return (
    <ComboboxPrimitive.Chips
      className={cn(
        "relative inline-flex min-h-9 w-full flex-wrap gap-1 rounded-lg border border-input bg-background not-dark:bg-clip-padding p-[calc(--spacing(1)-1px)] text-base shadow-xs/5 outline-none ring-ring/24 transition-shadow *:min-h-7 before:pointer-events-none before:absolute before:inset-0 before:rounded-[calc(var(--radius-lg)-1px)] not-has-disabled:not-focus-within:not-aria-invalid:before:shadow-[0_1px_--theme(--color-black/6%)] focus-within:border-ring focus-within:ring-[3px] has-disabled:pointer-events-none has-data-[size=lg]:min-h-10 has-data-[size=sm]:min-h-8 has-aria-invalid:border-destructive/36 has-disabled:opacity-64 has-[:disabled,:focus-within,[aria-invalid]]:shadow-none focus-within:has-aria-invalid:border-destructive/64 focus-within:has-aria-invalid:ring-destructive/16 has-data-[size=lg]:*:min-h-8 has-data-[size=sm]:*:min-h-6 sm:min-h-8 sm:text-sm sm:has-data-[size=lg]:min-h-9 sm:has-data-[size=sm]:min-h-7 sm:*:min-h-6 sm:has-data-[size=lg]:*:min-h-7 sm:has-data-[size=sm]:*:min-h-5 dark:not-has-disabled:bg-input/32 dark:has-aria-invalid:ring-destructive/24 dark:not-has-disabled:not-focus-within:not-aria-invalid:before:shadow-[0_-1px_--theme(--color-white/6%)]",
        className,
      )}
      data-slot="combobox-chips"
      onMouseDown={(e) => {
        const target = e.target as HTMLElement;
        const isChip = target.closest('[data-slot="combobox-chip"]');
        if (isChip || !chipsRef?.current) return;
        e.preventDefault();
        const input: HTMLInputElement | null =
          chipsRef.current.querySelector("input");
        if (input && !chipsRef.current.querySelector("input:focus")) {
          input.focus();
        }
      }}
      ref={chipsRef as React.Ref<HTMLDivElement> | null}
      {...props}
    >
      {startAddon && (
        <div
          aria-hidden="true"
          className="[&_svg]:-ms-0.5 [&_svg]:-me-1.5 flex shrink-0 items-center ps-2 opacity-80 has-[~[data-size=sm]]:has-[+[data-slot=combobox-chip]]:pe-1.5 has-[~[data-size=sm]]:ps-1.5 has-[+[data-slot=combobox-chip]]:pe-2 [&_svg:not([class*='size-'])]:size-4.5 sm:[&_svg:not([class*='size-'])]:size-4 [&_svg]:pointer-events-none"
          data-slot="combobox-start-addon"
        >
          {startAddon}
        </div>
      )}
      {children}
    </ComboboxPrimitive.Chips>
  );
}

function ComboboxChip({ children, ...props }: ComboboxPrimitive.Chip.Props) {
  return (
    <ComboboxPrimitive.Chip
      className="flex items-center rounded-[calc(var(--radius-md)-1px)] bg-accent ps-2 font-medium text-accent-foreground text-sm outline-none sm:text-xs/(--text-xs--line-height) [&_svg:not([class*='size-'])]:size-4 sm:[&_svg:not([class*='size-'])]:size-3.5"
      data-slot="combobox-chip"
      {...props}
    >
      {children}
      <ComboboxChipRemove />
    </ComboboxPrimitive.Chip>
  );
}

function ComboboxChipRemove(props: ComboboxPrimitive.ChipRemove.Props) {
  return (
    <ComboboxPrimitive.ChipRemove
      aria-label="Remove"
      className="h-full shrink-0 cursor-pointer px-1.5 opacity-80 hover:opacity-100 [&_svg:not([class*='size-'])]:size-4 sm:[&_svg:not([class*='size-'])]:size-3.5"
      data-slot="combobox-chip-remove"
      {...props}
    >
      <XIcon />
    </ComboboxPrimitive.ChipRemove>
  );
}

const useComboboxFilter = ComboboxPrimitive.useFilter;

export {
  Combobox,
  ComboboxInput,
  ComboboxTrigger,
  ComboboxPopup,
  ComboboxItem,
  ComboboxSeparator,
  ComboboxGroup,
  ComboboxGroupLabel,
  ComboboxEmpty,
  ComboboxValue,
  ComboboxList,
  ComboboxClear,
  ComboboxStatus,
  ComboboxRow,
  ComboboxCollection,
  ComboboxChips,
  ComboboxChip,
  useComboboxFilter,
};
```

## File: `web/src/components/ui/command.tsx`
```tsx
"use client";

import { Dialog as CommandDialogPrimitive } from "@base-ui/react/dialog";
import { SearchIcon } from "lucide-react";
import type * as React from "react";
import { cn } from "@/lib/utils";
import {
  Autocomplete,
  AutocompleteCollection,
  AutocompleteEmpty,
  AutocompleteGroup,
  AutocompleteGroupLabel,
  AutocompleteInput,
  AutocompleteItem,
  AutocompleteList,
  AutocompleteSeparator,
} from "@/components/ui/autocomplete";

const CommandDialog = CommandDialogPrimitive.Root;

const CommandDialogPortal = CommandDialogPrimitive.Portal;

const CommandCreateHandle = CommandDialogPrimitive.createHandle;

function CommandDialogTrigger(props: CommandDialogPrimitive.Trigger.Props) {
  return (
    <CommandDialogPrimitive.Trigger
      data-slot="command-dialog-trigger"
      {...props}
    />
  );
}

function CommandDialogBackdrop({
  className,
  ...props
}: CommandDialogPrimitive.Backdrop.Props) {
  return (
    <CommandDialogPrimitive.Backdrop
      className={cn(
        "fixed inset-0 z-50 bg-black/32 backdrop-blur-sm transition-all duration-200 data-ending-style:opacity-0 data-starting-style:opacity-0",
        className,
      )}
      data-slot="command-dialog-backdrop"
      {...props}
    />
  );
}

function CommandDialogViewport({
  className,
  ...props
}: CommandDialogPrimitive.Viewport.Props) {
  return (
    <CommandDialogPrimitive.Viewport
      className={cn(
        "fixed inset-0 z-50 flex flex-col items-center px-4 py-[max(--spacing(4),4vh)] sm:py-[10vh]",
        className,
      )}
      data-slot="command-dialog-viewport"
      {...props}
    />
  );
}

function CommandDialogPopup({
  className,
  children,
  ...props
}: CommandDialogPrimitive.Popup.Props) {
  return (
    <CommandDialogPortal>
      <CommandDialogBackdrop />
      <CommandDialogViewport>
        <CommandDialogPrimitive.Popup
          className={cn(
            "-translate-y-[calc(1.25rem*var(--nested-dialogs))] relative row-start-2 flex max-h-105 min-h-0 w-full min-w-0 max-w-xl scale-[calc(1-0.1*var(--nested-dialogs))] flex-col rounded-2xl border bg-popover not-dark:bg-clip-padding text-popover-foreground opacity-[calc(1-0.1*var(--nested-dialogs))] shadow-lg/5 outline-none transition-[scale,opacity,translate] duration-200 ease-in-out will-change-transform before:pointer-events-none before:absolute before:inset-0 before:rounded-[calc(var(--radius-2xl)-1px)] before:bg-muted/72 before:shadow-[0_1px_--theme(--color-black/6%)] data-nested:data-ending-style:translate-y-8 data-nested:data-starting-style:translate-y-8 data-nested-dialog-open:origin-top data-ending-style:scale-98 data-starting-style:scale-98 data-ending-style:opacity-0 data-starting-style:opacity-0 **:data-[slot=scroll-area-viewport]:data-has-overflow-y:pe-1 dark:before:shadow-[0_-1px_--theme(--color-white/6%)]",
            className,
          )}
          data-slot="command-dialog-popup"
          {...props}
        >
          {children}
        </CommandDialogPrimitive.Popup>
      </CommandDialogViewport>
    </CommandDialogPortal>
  );
}

function Command({
  autoHighlight = "always",
  keepHighlight = true,
  ...props
}: React.ComponentProps<typeof Autocomplete>) {
  return (
    <Autocomplete
      autoHighlight={autoHighlight}
      inline
      keepHighlight={keepHighlight}
      open
      {...props}
    />
  );
}

function CommandInput({
  className,
  placeholder = undefined,
  ...props
}: React.ComponentProps<typeof AutocompleteInput>) {
  return (
    <div className="px-2.5 py-1.5">
      <AutocompleteInput
        autoFocus
        className={cn(
          "border-transparent! bg-transparent! shadow-none before:hidden has-focus-visible:ring-0",
          className,
        )}
        placeholder={placeholder}
        size="lg"
        startAddon={<SearchIcon />}
        {...props}
      />
    </div>
  );
}

function CommandList({
  className,
  ...props
}: React.ComponentProps<typeof AutocompleteList>) {
  return (
    <AutocompleteList
      className={cn("not-empty:scroll-py-2 not-empty:p-2", className)}
      data-slot="command-list"
      {...props}
    />
  );
}

function CommandEmpty({
  className,
  ...props
}: React.ComponentProps<typeof AutocompleteEmpty>) {
  return (
    <AutocompleteEmpty
      className={cn("not-empty:py-6", className)}
      data-slot="command-empty"
      {...props}
    />
  );
}

function CommandPanel({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      className="-mx-px not-has-[+[data-slot=command-footer]]:-mb-px relative min-h-0 rounded-t-xl not-has-[+[data-slot=command-footer]]:rounded-b-2xl border border-b-0 bg-popover not-dark:bg-clip-padding shadow-xs/5 [clip-path:inset(0_1px)] not-has-[+[data-slot=command-footer]]:[clip-path:inset(0_1px_1px_1px_round_0_0_calc(var(--radius-2xl)-1px)_calc(var(--radius-2xl)-1px))] before:pointer-events-none before:absolute before:inset-0 before:rounded-t-[calc(var(--radius-xl)-1px)] **:data-[slot=scroll-area-scrollbar]:mt-2 dark:before:shadow-[0_-1px_--theme(--color-white/6%)]"
      {...props}
    />
  );
}

function CommandGroup({
  className,
  ...props
}: React.ComponentProps<typeof AutocompleteGroup>) {
  return (
    <AutocompleteGroup
      className={className}
      data-slot="command-group"
      {...props}
    />
  );
}

function CommandGroupLabel({
  className,
  ...props
}: React.ComponentProps<typeof AutocompleteGroupLabel>) {
  return (
    <AutocompleteGroupLabel
      className={className}
      data-slot="command-group-label"
      {...props}
    />
  );
}

function CommandCollection({
  ...props
}: React.ComponentProps<typeof AutocompleteCollection>) {
  return <AutocompleteCollection data-slot="command-collection" {...props} />;
}

function CommandItem({
  className,
  ...props
}: React.ComponentProps<typeof AutocompleteItem>) {
  return (
    <AutocompleteItem
      className={cn("py-1.5", className)}
      data-slot="command-item"
      {...props}
    />
  );
}

function CommandSeparator({
  className,
  ...props
}: React.ComponentProps<typeof AutocompleteSeparator>) {
  return (
    <AutocompleteSeparator
      className={cn("my-2", className)}
      data-slot="command-separator"
      {...props}
    />
  );
}

function CommandShortcut({ className, ...props }: React.ComponentProps<"kbd">) {
  return (
    <kbd
      className={cn(
        "ms-auto font-medium font-sans text-muted-foreground/72 text-xs tracking-widest",
        className,
      )}
      data-slot="command-shortcut"
      {...props}
    />
  );
}

function CommandFooter({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      className={cn(
        "flex items-center justify-between gap-2 rounded-b-[calc(var(--radius-2xl)-1px)] border-t px-5 py-3 text-muted-foreground text-xs",
        className,
      )}
      data-slot="command-footer"
      {...props}
    />
  );
}

export {
  CommandCreateHandle,
  Command,
  CommandCollection,
  CommandDialog,
  CommandDialogPopup,
  CommandDialogTrigger,
  CommandEmpty,
  CommandFooter,
  CommandGroup,
  CommandGroupLabel,
  CommandInput,
  CommandItem,
  CommandList,
  CommandPanel,
  CommandSeparator,
  CommandShortcut,
};
```

## File: `web/src/components/ui/dialog.tsx`
```tsx
"use client";

import { Dialog as DialogPrimitive } from "@base-ui/react/dialog";
import { XIcon } from "lucide-react";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";

const DialogCreateHandle = DialogPrimitive.createHandle;

const Dialog = DialogPrimitive.Root;

const DialogPortal = DialogPrimitive.Portal;

function DialogTrigger(props: DialogPrimitive.Trigger.Props) {
  return <DialogPrimitive.Trigger data-slot="dialog-trigger" {...props} />;
}

function DialogClose(props: DialogPrimitive.Close.Props) {
  return <DialogPrimitive.Close data-slot="dialog-close" {...props} />;
}

function DialogBackdrop({
  className,
  ...props
}: DialogPrimitive.Backdrop.Props) {
  return (
    <DialogPrimitive.Backdrop
      className={cn(
        "fixed inset-0 z-50 bg-black/32 backdrop-blur-sm transition-all duration-200 data-ending-style:opacity-0 data-starting-style:opacity-0",
        className,
      )}
      data-slot="dialog-backdrop"
      {...props}
    />
  );
}

function DialogViewport({
  className,
  ...props
}: DialogPrimitive.Viewport.Props) {
  return (
    <DialogPrimitive.Viewport
      className={cn(
        "fixed inset-0 z-50 grid grid-rows-[1fr_auto_3fr] justify-items-center p-4",
        className,
      )}
      data-slot="dialog-viewport"
      {...props}
    />
  );
}

function DialogPopup({
  className,
  children,
  showCloseButton = true,
  bottomStickOnMobile = true,
  ...props
}: DialogPrimitive.Popup.Props & {
  showCloseButton?: boolean;
  bottomStickOnMobile?: boolean;
}) {
  return (
    <DialogPortal>
      <DialogBackdrop />
      <DialogViewport
        className={cn(
          bottomStickOnMobile &&
            "max-sm:grid-rows-[1fr_auto] max-sm:p-0 max-sm:pt-12",
        )}
      >
        <DialogPrimitive.Popup
          className={cn(
            "-translate-y-[calc(1.25rem*var(--nested-dialogs))] relative row-start-2 flex max-h-full min-h-0 w-full min-w-0 max-w-lg scale-[calc(1-0.1*var(--nested-dialogs))] flex-col rounded-2xl border bg-popover not-dark:bg-clip-padding text-popover-foreground opacity-[calc(1-0.1*var(--nested-dialogs))] shadow-lg/5 transition-[scale,opacity,translate] duration-200 ease-in-out will-change-transform before:pointer-events-none before:absolute before:inset-0 before:rounded-[calc(var(--radius-2xl)-1px)] before:shadow-[0_1px_--theme(--color-black/6%)] data-nested:data-ending-style:translate-y-8 data-nested:data-starting-style:translate-y-8 data-nested-dialog-open:origin-top data-ending-style:scale-98 data-starting-style:scale-98 data-ending-style:opacity-0 data-starting-style:opacity-0 dark:before:shadow-[0_-1px_--theme(--color-white/6%)]",
            bottomStickOnMobile &&
              "max-sm:max-w-none max-sm:rounded-none max-sm:border-x-0 max-sm:border-t max-sm:border-b-0 max-sm:opacity-[calc(1-min(var(--nested-dialogs),1))] max-sm:data-ending-style:translate-y-4 max-sm:data-starting-style:translate-y-4 max-sm:before:hidden max-sm:before:rounded-none",
            className,
          )}
          data-slot="dialog-popup"
          {...props}
        >
          {children}
          {showCloseButton && (
            <DialogPrimitive.Close
              aria-label="Close"
              className="absolute end-2 top-2"
              render={<Button size="icon" variant="ghost" />}
            >
              <XIcon />
            </DialogPrimitive.Close>
          )}
        </DialogPrimitive.Popup>
      </DialogViewport>
    </DialogPortal>
  );
}

function DialogHeader({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      className={cn(
        "flex flex-col gap-2 p-6 in-[[data-slot=dialog-popup]:has([data-slot=dialog-panel])]:pb-3 max-sm:pb-4",
        className,
      )}
      data-slot="dialog-header"
      {...props}
    />
  );
}

function DialogFooter({
  className,
  variant = "default",
  ...props
}: React.ComponentProps<"div"> & {
  variant?: "default" | "bare";
}) {
  return (
    <div
      className={cn(
        "flex flex-col-reverse gap-2 px-6 sm:flex-row sm:justify-end sm:rounded-b-[calc(var(--radius-2xl)-1px)]",
        variant === "default" && "border-t bg-muted/72 py-4",
        variant === "bare" &&
          "in-[[data-slot=dialog-popup]:has([data-slot=dialog-panel])]:pt-3 pt-4 pb-6",
        className,
      )}
      data-slot="dialog-footer"
      {...props}
    />
  );
}

function DialogTitle({ className, ...props }: DialogPrimitive.Title.Props) {
  return (
    <DialogPrimitive.Title
      className={cn("font-heading text-xl leading-none", className)}
      data-slot="dialog-title"
      {...props}
    />
  );
}

function DialogDescription({
  className,
  ...props
}: DialogPrimitive.Description.Props) {
  return (
    <DialogPrimitive.Description
      className={cn("text-muted-foreground text-sm", className)}
      data-slot="dialog-description"
      {...props}
    />
  );
}

function DialogPanel({
  className,
  scrollFade = true,
  ...props
}: React.ComponentProps<"div"> & { scrollFade?: boolean }) {
  return (
    <ScrollArea scrollFade={scrollFade}>
      <div
        className={cn(
          "px-6 in-[[data-slot=dialog-popup]:has([data-slot=dialog-header])]:pt-1 in-[[data-slot=dialog-popup]:not(:has([data-slot=dialog-header]))]:pt-6 in-[[data-slot=dialog-popup]:not(:has([data-slot=dialog-footer]))]:pb-6! in-[[data-slot=dialog-popup]:not(:has([data-slot=dialog-footer].border-t))]:pb-1 pb-6",
          className,
        )}
        data-slot="dialog-panel"
        {...props}
      />
    </ScrollArea>
  );
}

export {
  DialogCreateHandle,
  Dialog,
  DialogTrigger,
  DialogPortal,
  DialogClose,
  DialogBackdrop,
  DialogBackdrop as DialogOverlay,
  DialogPopup,
  DialogPopup as DialogContent,
  DialogHeader,
  DialogFooter,
  DialogTitle,
  DialogDescription,
  DialogPanel,
  DialogViewport,
};
```

## File: `web/src/components/ui/empty.tsx`
```tsx
import { cva, type VariantProps } from "class-variance-authority";

import { cn } from "@/lib/utils";

function Empty({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      className={cn(
        "flex min-w-0 flex-1 flex-col items-center justify-center gap-6 text-balance p-6 text-center md:p-12",
        className,
      )}
      data-slot="empty"
      {...props}
    />
  );
}

function EmptyHeader({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      className={cn(
        "flex max-w-sm flex-col items-center text-center",
        className,
      )}
      data-slot="empty-header"
      {...props}
    />
  );
}

const emptyMediaVariants = cva(
  "flex shrink-0 items-center justify-center [&_svg]:pointer-events-none [&_svg]:shrink-0",
  {
    defaultVariants: {
      variant: "default",
    },
    variants: {
      variant: {
        default: "bg-transparent",
        icon: "relative flex size-9 shrink-0 items-center justify-center rounded-md border bg-card text-foreground shadow-sm/5 before:pointer-events-none before:absolute before:inset-0 before:rounded-[calc(var(--radius-md)-1px)] before:shadow-[0_1px_--theme(--color-black/6%)] dark:before:shadow-[0_-1px_--theme(--color-white/6%)] [&_svg:not([class*='size-'])]:size-4.5",
      },
    },
  },
);

function EmptyMedia({
  className,
  variant = "default",
  ...props
}: React.ComponentProps<"div"> & VariantProps<typeof emptyMediaVariants>) {
  return (
    <div
      className={cn("relative mb-6", className)}
      data-slot="empty-media"
      data-variant={variant}
      {...props}
    >
      {variant === "icon" && (
        <>
          <div
            aria-hidden="true"
            className={cn(
              emptyMediaVariants({ className, variant }),
              "-translate-x-0.5 -rotate-10 pointer-events-none absolute bottom-px origin-bottom-left scale-84 shadow-none",
            )}
          />
          <div
            aria-hidden="true"
            className={cn(
              emptyMediaVariants({ className, variant }),
              "pointer-events-none absolute bottom-px origin-bottom-right translate-x-0.5 rotate-10 scale-84 shadow-none",
            )}
          />
        </>
      )}
      <div
        className={cn(emptyMediaVariants({ className, variant }))}
        {...props}
      />
    </div>
  );
}

function EmptyTitle({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      className={cn("font-heading text-xl", className)}
      data-slot="empty-title"
      {...props}
    />
  );
}

function EmptyDescription({ className, ...props }: React.ComponentProps<"p">) {
  return (
    <div
      className={cn(
        "text-muted-foreground text-sm [&>a:hover]:text-primary [&>a]:underline [&>a]:underline-offset-4 [[data-slot=empty-title]+&]:mt-1",
        className,
      )}
      data-slot="empty-description"
      {...props}
    />
  );
}

function EmptyContent({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      className={cn(
        "flex w-full min-w-0 max-w-sm flex-col items-center gap-4 text-balance text-sm",
        className,
      )}
      data-slot="empty-content"
      {...props}
    />
  );
}

export {
  Empty,
  EmptyHeader,
  EmptyTitle,
  EmptyDescription,
  EmptyContent,
  EmptyMedia,
};
```

## File: `web/src/components/ui/field.tsx`
```tsx
"use client";

import { Field as FieldPrimitive } from "@base-ui/react/field";

import { cn } from "@/lib/utils";

function Field({ className, ...props }: FieldPrimitive.Root.Props) {
  return (
    <FieldPrimitive.Root
      className={cn("flex flex-col items-start gap-2", className)}
      data-slot="field"
      {...props}
    />
  );
}

function FieldLabel({ className, ...props }: FieldPrimitive.Label.Props) {
  return (
    <FieldPrimitive.Label
      className={cn(
        "inline-flex items-center gap-2 font-medium text-base/4.5 sm:text-sm/4",
        className,
      )}
      data-slot="field-label"
      {...props}
    />
  );
}

function FieldItem({ className, ...props }: FieldPrimitive.Item.Props) {
  return (
    <FieldPrimitive.Item
      className={cn("flex", className)}
      data-slot="field-item"
      {...props}
    />
  );
}

function FieldDescription({
  className,
  ...props
}: FieldPrimitive.Description.Props) {
  return (
    <FieldPrimitive.Description
      className={cn("text-muted-foreground text-xs", className)}
      data-slot="field-description"
      {...props}
    />
  );
}

function FieldError({ className, ...props }: FieldPrimitive.Error.Props) {
  return (
    <FieldPrimitive.Error
      className={cn("text-destructive-foreground text-xs", className)}
      data-slot="field-error"
      {...props}
    />
  );
}

const FieldControl = FieldPrimitive.Control;
const FieldValidity = FieldPrimitive.Validity;

export {
  Field,
  FieldLabel,
  FieldDescription,
  FieldError,
  FieldControl,
  FieldItem,
  FieldValidity,
};
```

## File: `web/src/components/ui/fieldset.tsx`
```tsx
"use client";

import { Fieldset as FieldsetPrimitive } from "@base-ui/react/fieldset";

import { cn } from "@/lib/utils";

function Fieldset({ className, ...props }: FieldsetPrimitive.Root.Props) {
  return (
    <FieldsetPrimitive.Root
      className={cn("flex w-full max-w-64 flex-col gap-6", className)}
      data-slot="fieldset"
      {...props}
    />
  );
}
function FieldsetLegend({
  className,
  ...props
}: FieldsetPrimitive.Legend.Props) {
  return (
    <FieldsetPrimitive.Legend
      className={cn("font-semibold", className)}
      data-slot="fieldset-legend"
      {...props}
    />
  );
}

export { Fieldset, FieldsetLegend };
```

## File: `web/src/components/ui/form.tsx`
```tsx
"use client";

import { Form as FormPrimitive } from "@base-ui/react/form";

import { cn } from "@/lib/utils";

function Form({ className, ...props }: FormPrimitive.Props) {
  return (
    <FormPrimitive
      className={cn("flex w-full flex-col gap-4", className)}
      data-slot="form"
      {...props}
    />
  );
}

export { Form };
```

## File: `web/src/components/ui/frame.tsx`
```tsx
import type * as React from "react";

import { cn } from "@/lib/utils";

function Frame({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      className={cn(
        "relative flex flex-col rounded-2xl bg-muted/72 p-1",
        "*:[[data-slot=frame-panel]+[data-slot=frame-panel]]:mt-1",
        className,
      )}
      data-slot="frame"
      {...props}
    />
  );
}

function FramePanel({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      className={cn(
        "relative rounded-xl border bg-background bg-clip-padding p-5 shadow-xs/5 before:pointer-events-none before:absolute before:inset-0 before:rounded-[calc(var(--radius-xl)-1px)] before:shadow-[0_1px_--theme(--color-black/6%)] dark:before:shadow-[0_-1px_--theme(--color-white/6%)]",
        className,
      )}
      data-slot="frame-panel"
      {...props}
    />
  );
}

function FrameHeader({ className, ...props }: React.ComponentProps<"header">) {
  return (
    <header
      className={cn("flex flex-col px-5 py-4", className)}
      data-slot="frame-panel-header"
      {...props}
    />
  );
}

function FrameTitle({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      className={cn("font-semibold text-sm", className)}
      data-slot="frame-panel-title"
      {...props}
    />
  );
}

function FrameDescription({
  className,
  ...props
}: React.ComponentProps<"div">) {
  return (
    <div
      className={cn("text-muted-foreground text-sm", className)}
      data-slot="frame-panel-description"
      {...props}
    />
  );
}

function FrameFooter({ className, ...props }: React.ComponentProps<"footer">) {
  return (
    <footer
      className={cn("flex flex-col gap-1 px-5 py-4", className)}
      data-slot="frame-panel-footer"
      {...props}
    />
  );
}

export {
  Frame,
  FramePanel,
  FrameHeader,
  FrameTitle,
  FrameDescription,
  FrameFooter,
};
```

## File: `web/src/components/ui/group.tsx`
```tsx
"use client";

import { mergeProps } from "@base-ui/react/merge-props";
import { useRender } from "@base-ui/react/use-render";
import { cva, type VariantProps } from "class-variance-authority";
import type * as React from "react";

import { cn } from "@/lib/utils";
import { Separator } from "@/components/ui/separator";

const groupVariants = cva(
  "flex w-fit *:focus-visible:z-1 has-[>[data-slot=group]]:gap-2 *:has-focus-visible:z-1 dark:*:[[data-slot=button]:hover~[data-slot=separator]:not([data-slot]:hover~[data-slot=separator]~[data-slot=separator]),[data-slot][data-pressed]~[data-slot=separator]:not([data-slot][data-pressed]~[data-slot=separator]~[data-slot=separator])]:before:bg-input/64 dark:*:[[data-slot=separator]:has(~[data-slot=button]:hover):not(:has(~[data-slot=separator]~[data-slot]:hover)),[data-slot=separator]:has(~[data-slot][data-pressed]):not(:has(~[data-slot=separator]~[data-slot][data-pressed]))]:before:bg-input/64",
  {
    defaultVariants: {
      orientation: "horizontal",
    },
    variants: {
      orientation: {
        horizontal:
          "*:[[data-slot]~[data-slot]:not([data-slot=separator])]:before:-start-[0.5px] *:data-slot:not-data-[slot=separator]:has-[~[data-slot]]:before:-end-[0.5px] *:pointer-coarse:after:min-w-auto *:data-slot:has-[~[data-slot]]:rounded-e-none *:data-slot:has-[~[data-slot]]:border-e-0 *:data-slot:has-[~[data-slot]]:before:rounded-e-none *:[[data-slot]~[data-slot]]:rounded-s-none *:[[data-slot]~[data-slot]]:border-s-0 *:[[data-slot]~[data-slot]]:before:rounded-s-none",
        vertical:
          "*:[[data-slot]~[data-slot]:not([data-slot=separator])]:before:-top-[0.5px] *:data-slot:not-data-[slot=separator]:has-[~[data-slot]]:before:-bottom-[0.5px] flex-col *:pointer-coarse:after:min-h-auto *:data-slot:has-[~[data-slot]]:rounded-b-none *:data-slot:has-[~[data-slot]]:border-b-0 *:data-slot:not-data-[slot=separator]:has-[~[data-slot]]:before:hidden *:data-slot:has-[~[data-slot]]:before:rounded-b-none dark:*:last:before:hidden dark:*:first:before:block *:[[data-slot]~[data-slot]]:rounded-t-none *:[[data-slot]~[data-slot]]:border-t-0 *:[[data-slot]~[data-slot]]:before:rounded-t-none",
      },
    },
  },
);

function Group({
  className,
  orientation,
  children,
  ...props
}: {
  className?: string;
  orientation?: VariantProps<typeof groupVariants>["orientation"];
  children: React.ReactNode;
} & React.ComponentProps<"div">) {
  return (
    <div
      className={cn(groupVariants({ orientation }), className)}
      data-orientation={orientation}
      data-slot="group"
      role="group"
      {...props}
    >
      {children}
    </div>
  );
}

function GroupText({
  className,
  render,
  ...props
}: useRender.ComponentProps<"div">) {
  const defaultProps = {
    className: cn(
      "relative inline-flex items-center whitespace-nowrap rounded-lg border border-input bg-muted not-dark:bg-clip-padding px-[calc(--spacing(3)-1px)] text-muted-foreground text-base sm:text-sm shadow-xs/5 outline-none transition-shadow before:pointer-events-none before:absolute before:inset-0 before:rounded-[calc(var(--radius-lg)-1px)] before:shadow-[0_1px_--theme(--color-black/6%)] dark:bg-input/64 dark:before:shadow-[0_-1px_--theme(--color-white/6%)] [&_svg:not([class*='size-'])]:size-4.5 sm:[&_svg:not([class*='size-'])]:size-4 [&_svg]:shrink-0 [&_svg]:-mx-0.5",
      className,
    ),
    "data-slot": "group-text",
  };
  return useRender({
    defaultTagName: "div",
    props: mergeProps(defaultProps, props),
    render,
  });
}

function GroupSeparator({
  className,
  orientation = "vertical",
  ...props
}: {
  className?: string;
} & React.ComponentProps<typeof Separator>) {
  return (
    <Separator
      className={cn(
        "[[data-slot=input-control]:focus-within+&,[data-slot=input-group]:focus-within+&,[data-slot=select-trigger]:focus-visible+*+&,[data-slot=number-field]:focus-within+input+&]:-translate-x-px pointer-events-none relative z-2 before:absolute before:inset-0 has-[+[data-slot=input-control]:focus-within,+[data-slot=input-group]:focus-within,+[data-slot=select-trigger]:focus-visible+*,+[data-slot=number-field]:focus-within]:translate-x-px has-[+[data-slot=input-control]:focus-within,+[data-slot=input-group]:focus-within,+[data-slot=select-trigger]:focus-visible+*,+[data-slot=number-field]:focus-within]:bg-ring dark:before:bg-input/32 [[data-slot=input-control]:focus-within+&,[data-slot=input-group]:focus-within+&,[data-slot=select-trigger]:focus-visible+*+&,[data-slot=number-field]:focus-within+&,[data-slot=number-field]:focus-within+input+&]:bg-ring",
        className,
      )}
      orientation={orientation}
      {...props}
    />
  );
}

export {
  Group,
  Group as ButtonGroup,
  GroupText,
  GroupText as ButtonGroupText,
  GroupSeparator,
  GroupSeparator as ButtonGroupSeparator,
  groupVariants,
};
```

## File: `web/src/components/ui/input-group.tsx`
```tsx
"use client";

import { cva, type VariantProps } from "class-variance-authority";
import type * as React from "react";

import { cn } from "@/lib/utils";
import { Input, type InputProps } from "@/components/ui/input";
import { Textarea, type TextareaProps } from "@/components/ui/textarea";

function InputGroup({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      className={cn(
        "relative inline-flex w-full min-w-0 items-center rounded-lg border border-input bg-background not-dark:bg-clip-padding text-base shadow-xs/5 ring-ring/24 transition-shadow before:pointer-events-none before:absolute before:inset-0 before:rounded-[calc(var(--radius-lg)-1px)] not-has-[input:disabled,textarea:disabled]:not-has-[input:focus-visible,textarea:focus-visible]:not-has-[input[aria-invalid],textarea[aria-invalid]]:before:shadow-[0_1px_--theme(--color-black/6%)] has-[input:focus-visible,textarea:focus-visible]:has-[input[aria-invalid],textarea[aria-invalid]]:border-destructive/64 has-[input:focus-visible,textarea:focus-visible]:has-[input[aria-invalid],textarea[aria-invalid]]:ring-destructive/16 has-[textarea]:h-auto has-data-[align=block-end]:h-auto has-data-[align=block-start]:h-auto has-data-[align=block-end]:flex-col has-data-[align=block-start]:flex-col has-[input:focus-visible,textarea:focus-visible]:border-ring has-[input[aria-invalid],textarea[aria-invalid]]:border-destructive/36 has-[input:disabled,textarea:disabled]:opacity-64 has-[input:disabled,textarea:disabled,input:focus-visible,textarea:focus-visible,input[aria-invalid],textarea[aria-invalid]]:shadow-none has-[input:focus-visible,textarea:focus-visible]:ring-[3px] sm:text-sm dark:bg-input/32 dark:has-[input[aria-invalid],textarea[aria-invalid]]:ring-destructive/24 dark:not-has-[input:disabled,textarea:disabled]:not-has-[input:focus-visible,textarea:focus-visible]:not-has-[input[aria-invalid],textarea[aria-invalid]]:before:shadow-[0_-1px_--theme(--color-white/6%)] has-data-[align=inline-start]:**:[[data-size=sm]_input]:ps-1.5 has-data-[align=inline-end]:**:[[data-size=sm]_input]:pe-1.5 *:[[data-slot=input-control],[data-slot=textarea-control]]:contents *:[[data-slot=input-control],[data-slot=textarea-control]]:before:hidden has-[[data-align=block-start],[data-align=block-end]]:**:[input]:h-auto has-data-[align=inline-start]:**:[input]:ps-2 has-data-[align=inline-end]:**:[input]:pe-2 has-data-[align=block-end]:**:[input]:pt-1.5 has-data-[align=block-start]:**:[input]:pb-1.5 **:[textarea]:min-h-20.5 **:[textarea]:resize-none **:[textarea]:py-[calc(--spacing(3)-1px)] **:[textarea]:max-sm:min-h-23.5 **:[textarea_button]:rounded-[calc(var(--radius-md)-1px)]",
        className,
      )}
      data-slot="input-group"
      role="group"
      {...props}
    />
  );
}

const inputGroupAddonVariants = cva(
  "[&_svg]:-mx-0.5 flex h-auto cursor-text select-none items-center justify-center gap-2 leading-none [&>kbd]:rounded-[calc(var(--radius)-5px)] in-[[data-slot=input-group]:has([data-slot=input-control],[data-slot=textarea-control])]:[&_svg:not([class*='size-'])]:size-4.5 sm:in-[[data-slot=input-group]:has([data-slot=input-control],[data-slot=textarea-control])]:[&_svg:not([class*='size-'])]:size-4 not-has-[button]:**:[svg:not([class*='opacity-'])]:opacity-80",
  {
    defaultVariants: {
      align: "inline-start",
    },
    variants: {
      align: {
        "block-end":
          "order-last w-full justify-start px-[calc(--spacing(3)-1px)] pb-[calc(--spacing(3)-1px)] [.border-t]:pt-[calc(--spacing(3)-1px)] [[data-size=sm]+&]:px-[calc(--spacing(2.5)-1px)]",
        "block-start":
          "order-first w-full justify-start px-[calc(--spacing(3)-1px)] pt-[calc(--spacing(3)-1px)] [.border-b]:pb-[calc(--spacing(3)-1px)] [[data-size=sm]+&]:px-[calc(--spacing(2.5)-1px)]",
        "inline-end":
          "has-[>:last-child[data-slot=badge]]:-me-1.5 has-[>button]:-me-2 order-last pe-[calc(--spacing(3)-1px)] has-[>kbd:last-child]:me-[-0.35rem] [[data-size=sm]+&]:pe-[calc(--spacing(2.5)-1px)]",
        "inline-start":
          "has-[>:last-child[data-slot=badge]]:-ms-1.5 has-[>button]:-ms-2 order-first ps-[calc(--spacing(3)-1px)] has-[>kbd:last-child]:ms-[-0.35rem] [[data-size=sm]+&]:ps-[calc(--spacing(2.5)-1px)]",
      },
    },
  },
);

function InputGroupAddon({
  className,
  align = "inline-start",
  ...props
}: React.ComponentProps<"div"> & VariantProps<typeof inputGroupAddonVariants>) {
  return (
    <div
      className={cn(inputGroupAddonVariants({ align }), className)}
      data-align={align}
      data-slot="input-group-addon"
      onMouseDown={(e) => {
        const target = e.target as HTMLElement;
        const isInteractive = target.closest(
          "button, a, input, select, textarea, [role='button'], [role='combobox'], [role='listbox'], [data-slot='select-trigger']",
        );
        if (isInteractive) return;
        e.preventDefault();
        const parent = e.currentTarget.parentElement;
        const input = parent?.querySelector<
          HTMLInputElement | HTMLTextAreaElement
        >("input, textarea");
        if (input && !parent?.querySelector("input:focus, textarea:focus")) {
          input.focus();
        }
      }}
      {...props}
    />
  );
}

function InputGroupText({ className, ...props }: React.ComponentProps<"span">) {
  return (
    <span
      className={cn(
        "[&_svg]:-mx-0.5 line-clamp-1 flex items-center gap-2 text-muted-foreground leading-none in-[[data-slot=input-group]:has([data-slot=input-control],[data-slot=textarea-control])]:[&_svg:not([class*='size-'])]:size-4.5 sm:in-[[data-slot=input-group]:has([data-slot=input-control],[data-slot=textarea-control])]:[&_svg:not([class*='size-'])]:size-4 [&_svg]:pointer-events-none",
        className,
      )}
      {...props}
    />
  );
}

function InputGroupInput({ className, ...props }: InputProps) {
  return <Input className={className} unstyled {...props} />;
}

function InputGroupTextarea({ className, ...props }: TextareaProps) {
  return <Textarea className={className} unstyled {...props} />;
}

export {
  InputGroup,
  InputGroupAddon,
  InputGroupText,
  InputGroupInput,
  InputGroupTextarea,
};
```

## File: `web/src/components/ui/input.tsx`
```tsx
"use client";

import { Input as InputPrimitive } from "@base-ui/react/input";
import type * as React from "react";

import { cn } from "@/lib/utils";

type InputProps = Omit<
  InputPrimitive.Props & React.RefAttributes<HTMLInputElement>,
  "size"
> & {
  size?: "sm" | "default" | "lg" | number;
  unstyled?: boolean;
  nativeInput?: boolean;
};

function Input({
  className,
  size = "default",
  unstyled = false,
  nativeInput = false,
  ...props
}: InputProps) {
  const inputClassName = cn(
    "h-8.5 w-full min-w-0 rounded-[inherit] px-[calc(--spacing(3)-1px)] leading-8.5 outline-none placeholder:text-muted-foreground/72 sm:h-7.5 sm:leading-7.5",
    size === "sm" &&
      "h-7.5 px-[calc(--spacing(2.5)-1px)] leading-7.5 sm:h-6.5 sm:leading-6.5",
    size === "lg" && "h-9.5 leading-9.5 sm:h-8.5 sm:leading-8.5",
    props.type === "search" &&
      "[&::-webkit-search-cancel-button]:appearance-none [&::-webkit-search-decoration]:appearance-none [&::-webkit-search-results-button]:appearance-none [&::-webkit-search-results-decoration]:appearance-none",
    props.type === "file" &&
      "text-muted-foreground file:me-3 file:bg-transparent file:font-medium file:text-foreground file:text-sm",
  );

  return (
    <span
      className={
        cn(
          !unstyled &&
            "relative inline-flex w-full rounded-lg border border-input bg-background not-dark:bg-clip-padding text-base shadow-xs/5 ring-ring/24 transition-shadow before:pointer-events-none before:absolute before:inset-0 before:rounded-[calc(var(--radius-lg)-1px)] not-has-disabled:not-has-focus-visible:not-has-aria-invalid:before:shadow-[0_1px_--theme(--color-black/6%)] has-focus-visible:has-aria-invalid:border-destructive/64 has-focus-visible:has-aria-invalid:ring-destructive/16 has-aria-invalid:border-destructive/36 has-focus-visible:border-ring has-disabled:opacity-64 has-[:disabled,:focus-visible,[aria-invalid]]:shadow-none has-focus-visible:ring-[3px] sm:text-sm dark:bg-input/32 dark:has-aria-invalid:ring-destructive/24 dark:not-has-disabled:not-has-focus-visible:not-has-aria-invalid:before:shadow-[0_-1px_--theme(--color-white/6%)]",
          className,
        ) || undefined
      }
      data-size={size}
      data-slot="input-control"
    >
      {nativeInput ? (
        <input
          className={inputClassName}
          data-slot="input"
          size={typeof size === "number" ? size : undefined}
          {...props}
        />
      ) : (
        <InputPrimitive
          className={inputClassName}
          data-slot="input"
          size={typeof size === "number" ? size : undefined}
          {...props}
        />
      )}
    </span>
  );
}

export { Input, type InputProps };
```

## File: `web/src/components/ui/kbd.tsx`
```tsx
import type * as React from "react";

import { cn } from "@/lib/utils";

function Kbd({ className, ...props }: React.ComponentProps<"kbd">) {
  return (
    <kbd
      className={cn(
        "pointer-events-none inline-flex h-5 min-w-5 select-none items-center justify-center gap-1 rounded bg-muted px-1 font-medium font-sans text-muted-foreground text-xs [&_svg:not([class*='size-'])]:size-3",
        className,
      )}
      data-slot="kbd"
      {...props}
    />
  );
}

function KbdGroup({ className, ...props }: React.ComponentProps<"kbd">) {
  return (
    <kbd
      className={cn("inline-flex items-center gap-1", className)}
      data-slot="kbd-group"
      {...props}
    />
  );
}

export { Kbd, KbdGroup };
```

## File: `web/src/components/ui/label.tsx`
```tsx
"use client";

import { mergeProps } from "@base-ui/react/merge-props";
import { useRender } from "@base-ui/react/use-render";

import { cn } from "@/lib/utils";

function Label({
  className,
  render,
  ...props
}: useRender.ComponentProps<"label">) {
  const defaultProps = {
    className: cn(
      "inline-flex items-center gap-2 text-base/4.5 sm:text-sm/4 font-medium",
      className,
    ),
    "data-slot": "label",
  };

  return useRender({
    defaultTagName: "label",
    props: mergeProps<"label">(defaultProps, props),
    render,
  });
}

export { Label };
```

## File: `web/src/components/ui/llms.txt`
```
# coss ui

**coss ui** is a collection of beautifully designed, accessible, and composable components for your React apps. Built on top of [Base UI](https://base-ui.com/) and styled with [Tailwind CSS](https://tailwindcss.com/), it’s designed for you to copy, paste, and own.

## Overview

- [Introduction](https://coss.com/ui/brain/knowledge/docs_legacy/index.md)
- [Get Started](https://coss.com/ui/brain/knowledge/docs_legacy/get-started.md)
- [Roadmap](https://coss.com/ui/brain/knowledge/docs_legacy/roadmap.md)
- [Radix / shadcn Migration](https://coss.com/ui/brain/knowledge/docs_legacy/radix-shadcn-migration.md): A comprehensive guide for migrating from shadcn/ui and Radix UI to coss ui components.

## Components

- [Accordion](https://coss.com/ui/brain/knowledge/docs_legacy/components/accordion.md): A set of collapsible panels with headings.
- [Alert](https://coss.com/ui/brain/knowledge/docs_legacy/components/alert.md): A callout for displaying important information.
- [Alert Dialog](https://coss.com/ui/brain/knowledge/docs_legacy/components/alert-dialog.md): A modal dialog that interrupts the user workflow for critical confirmations.
- [Autocomplete](https://coss.com/ui/brain/knowledge/docs_legacy/components/autocomplete.md): An input that suggests options as you type.
- [Avatar](https://coss.com/ui/brain/knowledge/docs_legacy/components/avatar.md): A visual representation of a user or entity.
- [Badge](https://coss.com/ui/brain/knowledge/docs_legacy/components/badge.md): A small status indicator or label component.
- [Breadcrumb](https://coss.com/ui/brain/knowledge/docs_legacy/components/breadcrumb.md): Displays the path to the current resource using a hierarchy of links.
- [Button](https://coss.com/ui/brain/knowledge/docs_legacy/components/button.md): A button or a component that looks like a button.
- [Card](https://coss.com/ui/brain/knowledge/docs_legacy/components/card.md): A content container for grouping related information.
- [Checkbox](https://coss.com/ui/brain/knowledge/docs_legacy/components/checkbox.md): A binary toggle input for selecting one or multiple options.
- [Checkbox Group](https://coss.com/ui/brain/knowledge/docs_legacy/components/checkbox-group.md): A collection of related checkboxes with group-level control.
- [Collapsible](https://coss.com/ui/brain/knowledge/docs_legacy/components/collapsible.md): A component that toggles visibility of content sections.
- [Combobox](https://coss.com/ui/brain/knowledge/docs_legacy/components/combobox.md): An input combined with a list of predefined items to select.
- [Command](https://coss.com/ui/brain/knowledge/docs_legacy/components/command.md): A command palette component built with Dialog and Autocomplete for searching and executing commands.
- [Dialog](https://coss.com/ui/brain/knowledge/docs_legacy/components/dialog.md): A modal overlay for displaying content that requires user interaction.
- [Empty](https://coss.com/ui/brain/knowledge/docs_legacy/components/empty.md): A container for displaying empty state information.
- [Field](https://coss.com/ui/brain/knowledge/docs_legacy/components/field.md): A wrapper component for form inputs with labels and validation.
- [Fieldset](https://coss.com/ui/brain/knowledge/docs_legacy/components/fieldset.md): A group of related form fields with a common label.
- [Form](https://coss.com/ui/brain/knowledge/docs_legacy/components/form.md): A complete form implementation with validation and submission handling.
- [Frame](https://coss.com/ui/brain/knowledge/docs_legacy/components/frame.md): A container component for displaying content in a frame.
- [Group](https://coss.com/ui/brain/knowledge/docs_legacy/components/group.md): A container component for grouping related content with consistent styling.
- [Input](https://coss.com/ui/brain/knowledge/docs_legacy/components/input.md): A native input element.
- [Input Group](https://coss.com/ui/brain/knowledge/docs_legacy/components/input-group.md): A flexible component for grouping inputs with addons, buttons, and other elements.
- [Kbd](https://coss.com/ui/brain/knowledge/docs_legacy/components/kbd.md): A component for displaying keyboard keys and shortcuts.
- [Label](https://coss.com/ui/brain/knowledge/docs_legacy/components/label.md): Renders an accessible label associated with controls.
- [Menu](https://coss.com/ui/brain/knowledge/docs_legacy/components/menu.md): A list of actions or options revealed on demand.
- [Meter](https://coss.com/ui/brain/knowledge/docs_legacy/components/meter.md): A visual representation of a value within a known range.
- [Number Field](https://coss.com/ui/brain/knowledge/docs_legacy/components/number-field.md): A specialized input for numeric values with increment/decrement controls.
- [Pagination](https://coss.com/ui/brain/knowledge/docs_legacy/components/pagination.md): A pagination with page navigation, next and previous links.
- [Popover](https://coss.com/ui/brain/knowledge/docs_legacy/components/popover.md): A floating container that appears near a trigger element.
- [Preview Card](https://coss.com/ui/brain/knowledge/docs_legacy/components/preview-card.md): A rich preview component for displaying linked content.
- [Progress](https://coss.com/ui/brain/knowledge/docs_legacy/components/progress.md): A visual indicator showing the completion status of a task.
- [Radio Group](https://coss.com/ui/brain/knowledge/docs_legacy/components/radio-group.md): A set of mutually exclusive options presented as radio buttons.
- [Scroll Area](https://coss.com/ui/brain/knowledge/docs_legacy/components/scroll-area.md): A container with custom scrollbars for overflow content.
- [Select](https://coss.com/ui/brain/knowledge/docs_legacy/components/select.md): A common form component for choosing a predefined value in a dropdown menu.
- [Separator](https://coss.com/ui/brain/knowledge/docs_legacy/components/separator.md): A visual divider for separating content sections.
- [Sheet](https://coss.com/ui/brain/knowledge/docs_legacy/components/sheet.md): A flyout that opens from the side of the screen, based on the dialog component.
- [Skeleton](https://coss.com/ui/brain/knowledge/docs_legacy/components/skeleton.md): A placeholder for loading content.
- [Slider](https://coss.com/ui/brain/knowledge/docs_legacy/components/slider.md): A draggable control for selecting values from a continuous range.
- [Spinner](https://coss.com/ui/brain/knowledge/docs_legacy/components/spinner.md): An indicator that can be used to show a loading state.
- [Switch](https://coss.com/ui/brain/knowledge/docs_legacy/components/switch.md): A toggle control for binary on/off states.
- [Table](https://coss.com/ui/brain/knowledge/docs_legacy/components/table.md): A structured data display component with rows and columns.
- [Tabs](https://coss.com/ui/brain/knowledge/docs_legacy/components/tabs.md): A navigation component for switching between different views or content panels.
- [Textarea](https://coss.com/ui/brain/knowledge/docs_legacy/components/textarea.md): A multi-line text input for longer content.
- [Toast](https://coss.com/ui/brain/knowledge/docs_legacy/components/toast.md): A temporary notification message that appears and disappears automatically.
- [Toggle](https://coss.com/ui/brain/knowledge/docs_legacy/components/toggle.md): A button that switches between two states.
- [Toggle Group](https://coss.com/ui/brain/knowledge/docs_legacy/components/toggle-group.md): A group of toggle buttons where one or multiple can be selected.
- [Toolbar](https://coss.com/ui/brain/knowledge/docs_legacy/components/toolbar.md): A container for grouping related actions or controls.
- [Tooltip](https://coss.com/ui/brain/knowledge/docs_legacy/components/tooltip.md): A small overlay that provides contextual information on hover or focus.
```

## File: `web/src/components/ui/menu.tsx`
```tsx
"use client";

import { Menu as MenuPrimitive } from "@base-ui/react/menu";
import { ChevronRightIcon } from "lucide-react";
import type * as React from "react";
import { cn } from "@/lib/utils";

const MenuCreateHandle = MenuPrimitive.createHandle;

const Menu = MenuPrimitive.Root;

const MenuPortal = MenuPrimitive.Portal;

function MenuTrigger(props: MenuPrimitive.Trigger.Props) {
  return <MenuPrimitive.Trigger data-slot="menu-trigger" {...props} />;
}

function MenuPopup({
  children,
  className,
  sideOffset = 4,
  align = "center",
  alignOffset,
  side = "bottom",
  ...props
}: MenuPrimitive.Popup.Props & {
  align?: MenuPrimitive.Positioner.Props["align"];
  sideOffset?: MenuPrimitive.Positioner.Props["sideOffset"];
  alignOffset?: MenuPrimitive.Positioner.Props["alignOffset"];
  side?: MenuPrimitive.Positioner.Props["side"];
}) {
  return (
    <MenuPrimitive.Portal>
      <MenuPrimitive.Positioner
        align={align}
        alignOffset={alignOffset}
        className="z-50"
        data-slot="menu-positioner"
        side={side}
        sideOffset={sideOffset}
      >
        <MenuPrimitive.Popup
          className={cn(
            "relative flex not-[class*='w-']:min-w-32 origin-(--transform-origin) rounded-lg border bg-popover not-dark:bg-clip-padding shadow-lg/5 outline-none before:pointer-events-none before:absolute before:inset-0 before:rounded-[calc(var(--radius-lg)-1px)] before:shadow-[0_1px_--theme(--color-black/6%)] focus:outline-none dark:before:shadow-[0_-1px_--theme(--color-white/6%)]",
            className,
          )}
          data-slot="menu-popup"
          {...props}
        >
          <div className="max-h-(--available-height) w-full overflow-y-auto p-1">
            {children}
          </div>
        </MenuPrimitive.Popup>
      </MenuPrimitive.Positioner>
    </MenuPrimitive.Portal>
  );
}

function MenuGroup(props: MenuPrimitive.Group.Props) {
  return <MenuPrimitive.Group data-slot="menu-group" {...props} />;
}

function MenuItem({
  className,
  inset,
  variant = "default",
  ...props
}: MenuPrimitive.Item.Props & {
  inset?: boolean;
  variant?: "default" | "destructive";
}) {
  return (
    <MenuPrimitive.Item
      className={cn(
        "[&>svg]:-mx-0.5 flex min-h-8 cursor-default select-none items-center gap-2 rounded-sm px-2 py-1 text-base outline-none data-disabled:pointer-events-none data-highlighted:bg-accent data-inset:ps-8 data-[variant=destructive]:text-destructive-foreground data-highlighted:text-accent-foreground data-disabled:opacity-64 sm:min-h-7 sm:text-sm [&>svg:not([class*='opacity-'])]:opacity-80 [&>svg:not([class*='size-'])]:size-4.5 sm:[&>svg:not([class*='size-'])]:size-4 [&>svg]:pointer-events-none [&>svg]:shrink-0",
        className,
      )}
      data-inset={inset}
      data-slot="menu-item"
      data-variant={variant}
      {...props}
    />
  );
}

function MenuCheckboxItem({
  className,
  children,
  checked,
  variant = "default",
  ...props
}: MenuPrimitive.CheckboxItem.Props & {
  variant?: "default" | "switch";
}) {
  return (
    <MenuPrimitive.CheckboxItem
      checked={checked}
      className={cn(
        "grid min-h-8 in-data-[side=none]:min-w-[calc(var(--anchor-width)+1.25rem)] cursor-default items-center gap-2 rounded-sm py-1 ps-2 text-base outline-none data-disabled:pointer-events-none data-highlighted:bg-accent data-highlighted:text-accent-foreground data-disabled:opacity-64 sm:min-h-7 sm:text-sm [&_svg:not([class*='size-'])]:size-4.5 sm:[&_svg:not([class*='size-'])]:size-4 [&_svg]:pointer-events-none [&_svg]:shrink-0",
        variant === "switch"
          ? "grid-cols-[1fr_auto] gap-4 pe-1.5"
          : "grid-cols-[1rem_1fr] pe-4",
        className,
      )}
      data-slot="menu-checkbox-item"
      {...props}
    >
      {variant === "switch" ? (
        <>
          <span className="col-start-1">{children}</span>
          <MenuPrimitive.CheckboxItemIndicator
            className="inset-shadow-[0_1px_--theme(--color-black/6%)] inline-flex h-[calc(var(--thumb-size)+2px)] w-[calc(var(--thumb-size)*2-2px)] shrink-0 items-center rounded-full p-px outline-none transition-[background-color,box-shadow] duration-200 [--thumb-size:--spacing(4)] focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-1 focus-visible:ring-offset-background data-checked:bg-primary data-unchecked:bg-input data-disabled:opacity-64 sm:[--thumb-size:--spacing(3)]"
            keepMounted
          >
            <span className="pointer-events-none block aspect-square h-full in-[[data-slot=menu-checkbox-item][data-checked]]:origin-[var(--thumb-size)_50%] origin-left in-[[data-slot=menu-checkbox-item][data-checked]]:translate-x-[calc(var(--thumb-size)-4px)] in-[[data-slot=menu-checkbox-item]:active]:not-data-disabled:scale-x-110 in-[[data-slot=menu-checkbox-item]:active]:rounded-[var(--thumb-size)/calc(var(--thumb-size)*1.10)] rounded-(--thumb-size) bg-background shadow-sm/5 will-change-transform [transition:translate_.15s,border-radius_.15s,scale_.1s_.1s,transform-origin_.15s]" />
          </MenuPrimitive.CheckboxItemIndicator>
        </>
      ) : (
        <>
          <MenuPrimitive.CheckboxItemIndicator className="col-start-1">
            <svg
              fill="none"
              height="24"
              stroke="currentColor"
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              viewBox="0 0 24 24"
              width="24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path d="M5.252 12.7 10.2 18.63 18.748 5.37" />
            </svg>
          </MenuPrimitive.CheckboxItemIndicator>
          <span className="col-start-2">{children}</span>
        </>
      )}
    </MenuPrimitive.CheckboxItem>
  );
}

function MenuRadioGroup(props: MenuPrimitive.RadioGroup.Props) {
  return <MenuPrimitive.RadioGroup data-slot="menu-radio-group" {...props} />;
}

function MenuRadioItem({
  className,
  children,
  ...props
}: MenuPrimitive.RadioItem.Props) {
  return (
    <MenuPrimitive.RadioItem
      className={cn(
        "grid min-h-8 in-data-[side=none]:min-w-[calc(var(--anchor-width)+1.25rem)] cursor-default grid-cols-[1rem_1fr] items-center gap-2 rounded-sm py-1 ps-2 pe-4 text-base outline-none data-disabled:pointer-events-none data-highlighted:bg-accent data-highlighted:text-accent-foreground data-disabled:opacity-64 sm:min-h-7 sm:text-sm [&_svg:not([class*='size-'])]:size-4.5 sm:[&_svg:not([class*='size-'])]:size-4 [&_svg]:pointer-events-none [&_svg]:shrink-0",
        className,
      )}
      data-slot="menu-radio-item"
      {...props}
    >
      <MenuPrimitive.RadioItemIndicator className="col-start-1">
        <svg
          fill="none"
          height="24"
          stroke="currentColor"
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth="2"
          viewBox="0 0 24 24"
          width="24"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path d="M5.252 12.7 10.2 18.63 18.748 5.37" />
        </svg>
      </MenuPrimitive.RadioItemIndicator>
      <span className="col-start-2">{children}</span>
    </MenuPrimitive.RadioItem>
  );
}

function MenuGroupLabel({
  className,
  inset,
  ...props
}: MenuPrimitive.GroupLabel.Props & {
  inset?: boolean;
}) {
  return (
    <MenuPrimitive.GroupLabel
      className={cn(
        "px-2 py-1.5 font-medium text-muted-foreground text-xs data-inset:ps-9 sm:data-inset:ps-8",
        className,
      )}
      data-inset={inset}
      data-slot="menu-label"
      {...props}
    />
  );
}

function MenuSeparator({ className, ...props }: MenuPrimitive.Separator.Props) {
  return (
    <MenuPrimitive.Separator
      className={cn("mx-2 my-1 h-px bg-border", className)}
      data-slot="menu-separator"
      {...props}
    />
  );
}

function MenuShortcut({ className, ...props }: React.ComponentProps<"kbd">) {
  return (
    <kbd
      className={cn(
        "ms-auto font-medium font-sans text-muted-foreground/72 text-xs tracking-widest",
        className,
      )}
      data-slot="menu-shortcut"
      {...props}
    />
  );
}

function MenuSub(props: MenuPrimitive.SubmenuRoot.Props) {
  return <MenuPrimitive.SubmenuRoot data-slot="menu-sub" {...props} />;
}

function MenuSubTrigger({
  className,
  inset,
  children,
  ...props
}: MenuPrimitive.SubmenuTrigger.Props & {
  inset?: boolean;
}) {
  return (
    <MenuPrimitive.SubmenuTrigger
      className={cn(
        "flex min-h-8 items-center gap-2 rounded-sm px-2 py-1 text-base outline-none data-disabled:pointer-events-none data-highlighted:bg-accent data-popup-open:bg-accent data-inset:ps-8 data-highlighted:text-accent-foreground data-popup-open:text-accent-foreground data-disabled:opacity-64 sm:min-h-7 sm:text-sm [&_svg:not([class*='size-'])]:size-4.5 sm:[&_svg:not([class*='size-'])]:size-4 [&_svg]:pointer-events-none",
        className,
      )}
      data-inset={inset}
      data-slot="menu-sub-trigger"
      {...props}
    >
      {children}
      <ChevronRightIcon className="-me-0.5 ms-auto opacity-80" />
    </MenuPrimitive.SubmenuTrigger>
  );
}

function MenuSubPopup({
  className,
  sideOffset = 0,
  alignOffset,
  align = "start",
  ...props
}: MenuPrimitive.Popup.Props & {
  align?: MenuPrimitive.Positioner.Props["align"];
  sideOffset?: MenuPrimitive.Positioner.Props["sideOffset"];
  alignOffset?: MenuPrimitive.Positioner.Props["alignOffset"];
}) {
  const defaultAlignOffset = align !== "center" ? -5 : undefined;

  return (
    <MenuPopup
      align={align}
      alignOffset={alignOffset ?? defaultAlignOffset}
      className={className}
      data-slot="menu-sub-content"
      side="inline-end"
      sideOffset={sideOffset}
      {...props}
    />
  );
}

export {
  MenuCreateHandle,
  MenuCreateHandle as DropdownMenuCreateHandle,
  Menu,
  Menu as DropdownMenu,
  MenuPortal,
  MenuPortal as DropdownMenuPortal,
  MenuTrigger,
  MenuTrigger as DropdownMenuTrigger,
  MenuPopup,
  MenuPopup as DropdownMenuContent,
  MenuGroup,
  MenuGroup as DropdownMenuGroup,
  MenuItem,
  MenuItem as DropdownMenuItem,
  MenuCheckboxItem,
  MenuCheckboxItem as DropdownMenuCheckboxItem,
  MenuRadioGroup,
  MenuRadioGroup as DropdownMenuRadioGroup,
  MenuRadioItem,
  MenuRadioItem as DropdownMenuRadioItem,
  MenuGroupLabel,
  MenuGroupLabel as DropdownMenuLabel,
  MenuSeparator,
  MenuSeparator as DropdownMenuSeparator,
  MenuShortcut,
  MenuShortcut as DropdownMenuShortcut,
  MenuSub,
  MenuSub as DropdownMenuSub,
  MenuSubTrigger,
  MenuSubTrigger as DropdownMenuSubTrigger,
  MenuSubPopup,
  MenuSubPopup as DropdownMenuSubContent,
};
```

## File: `web/src/components/ui/meter.tsx`
```tsx
"use client";

import { Meter as MeterPrimitive } from "@base-ui/react/meter";

import { cn } from "@/lib/utils";

function Meter({ className, children, ...props }: MeterPrimitive.Root.Props) {
  return (
    <MeterPrimitive.Root
      className={cn("flex w-full flex-col gap-2", className)}
      {...props}
    >
      {children ? (
        children
      ) : (
        <MeterTrack>
          <MeterIndicator />
        </MeterTrack>
      )}
    </MeterPrimitive.Root>
  );
}

function MeterLabel({ className, ...props }: MeterPrimitive.Label.Props) {
  return (
    <MeterPrimitive.Label
      className={cn("font-medium text-sm", className)}
      data-slot="meter-label"
      {...props}
    />
  );
}

function MeterTrack({ className, ...props }: MeterPrimitive.Track.Props) {
  return (
    <MeterPrimitive.Track
      className={cn("block h-2 w-full overflow-hidden bg-input", className)}
      data-slot="meter-track"
      {...props}
    />
  );
}

function MeterIndicator({
  className,
  ...props
}: MeterPrimitive.Indicator.Props) {
  return (
    <MeterPrimitive.Indicator
      className={cn("bg-primary transition-all duration-500", className)}
      data-slot="meter-indicator"
      {...props}
    />
  );
}

function MeterValue({ className, ...props }: MeterPrimitive.Value.Props) {
  return (
    <MeterPrimitive.Value
      className={cn("text-sm tabular-nums", className)}
      data-slot="meter-value"
      {...props}
    />
  );
}

export { Meter, MeterLabel, MeterTrack, MeterIndicator, MeterValue };
```

## File: `web/src/components/ui/number-field.tsx`
```tsx
"use client";

import { NumberField as NumberFieldPrimitive } from "@base-ui/react/number-field";
import { MinusIcon, PlusIcon } from "lucide-react";
import * as React from "react";

import { cn } from "@/lib/utils";
import { Label } from "@/components/ui/label";

const NumberFieldContext = React.createContext<{
  fieldId: string;
} | null>(null);

function NumberField({
  id,
  className,
  size = "default",
  ...props
}: NumberFieldPrimitive.Root.Props & {
  size?: "sm" | "default" | "lg";
}) {
  const generatedId = React.useId();
  const fieldId = id ?? generatedId;

  return (
    <NumberFieldContext.Provider value={{ fieldId }}>
      <NumberFieldPrimitive.Root
        className={cn("flex w-full flex-col items-start gap-2", className)}
        data-size={size}
        data-slot="number-field"
        id={fieldId}
        {...props}
      />
    </NumberFieldContext.Provider>
  );
}

function NumberFieldGroup({
  className,
  ...props
}: NumberFieldPrimitive.Group.Props) {
  return (
    <NumberFieldPrimitive.Group
      className={cn(
        "relative flex w-full justify-between rounded-lg border border-input bg-background not-dark:bg-clip-padding text-base shadow-xs/5 ring-ring/24 transition-shadow before:pointer-events-none before:absolute before:inset-0 before:rounded-[calc(var(--radius-lg)-1px)] not-data-disabled:not-focus-within:not-aria-invalid:before:shadow-[0_1px_--theme(--color-black/6%)] focus-within:border-ring focus-within:ring-[3px] has-aria-invalid:border-destructive/36 focus-within:has-aria-invalid:border-destructive/64 focus-within:has-aria-invalid:ring-destructive/48 data-disabled:pointer-events-none data-disabled:opacity-64 sm:text-sm dark:bg-input/32 dark:has-aria-invalid:ring-destructive/24 dark:not-data-disabled:not-focus-within:not-aria-invalid:before:shadow-[0_-1px_--theme(--color-white/6%)] [&_svg:not([class*='size-'])]:size-4.5 sm:[&_svg:not([class*='size-'])]:size-4 [&_svg]:pointer-events-none [&_svg]:shrink-0 [[data-disabled],:focus-within,[aria-invalid]]:shadow-none",
        className,
      )}
      data-slot="number-field-group"
      {...props}
    />
  );
}

function NumberFieldDecrement({
  className,
  ...props
}: NumberFieldPrimitive.Decrement.Props) {
  return (
    <NumberFieldPrimitive.Decrement
      className={cn(
        "relative flex shrink-0 cursor-pointer items-center justify-center rounded-s-[calc(var(--radius-lg)-1px)] in-data-[size=sm]:px-[calc(--spacing(2.5)-1px)] px-[calc(--spacing(3)-1px)] transition-colors pointer-coarse:after:absolute pointer-coarse:after:size-full pointer-coarse:after:min-h-11 pointer-coarse:after:min-w-11 hover:bg-accent",
        className,
      )}
      data-slot="number-field-decrement"
      {...props}
    >
      <MinusIcon />
    </NumberFieldPrimitive.Decrement>
  );
}

function NumberFieldIncrement({
  className,
  ...props
}: NumberFieldPrimitive.Increment.Props) {
  return (
    <NumberFieldPrimitive.Increment
      className={cn(
        "relative flex shrink-0 cursor-pointer items-center justify-center rounded-e-[calc(var(--radius-lg)-1px)] in-data-[size=sm]:px-[calc(--spacing(2.5)-1px)] px-[calc(--spacing(3)-1px)] transition-colors pointer-coarse:after:absolute pointer-coarse:after:size-full pointer-coarse:after:min-h-11 pointer-coarse:after:min-w-11 hover:bg-accent",
        className,
      )}
      data-slot="number-field-increment"
      {...props}
    >
      <PlusIcon />
    </NumberFieldPrimitive.Increment>
  );
}

function NumberFieldInput({
  className,
  ...props
}: NumberFieldPrimitive.Input.Props) {
  return (
    <NumberFieldPrimitive.Input
      className={cn(
        "h-8.5 in-data-[size=lg]:h-9.5 in-data-[size=sm]:h-7.5 w-full min-w-0 grow bg-transparent in-data-[size=sm]:px-[calc(--spacing(2.5)-1px)] px-[calc(--spacing(3)-1px)] text-center tabular-nums in-data-[size=lg]:leading-9.5 in-data-[size=sm]:leading-7.5 leading-8.5 outline-none sm:h-7.5 sm:in-data-[size=lg]:h-8.5 sm:in-data-[size=sm]:h-6.5 sm:in-data-[size=lg]:leading-8.5 sm:in-data-[size=sm]:leading-8.5 sm:leading-7.5",
        className,
      )}
      data-slot="number-field-input"
      {...props}
    />
  );
}

function NumberFieldScrubArea({
  className,
  label,
  ...props
}: NumberFieldPrimitive.ScrubArea.Props & {
  label: string;
}) {
  const context = React.useContext(NumberFieldContext);

  if (!context) {
    throw new Error(
      "NumberFieldScrubArea must be used within a NumberField component for accessibility.",
    );
  }

  return (
    <NumberFieldPrimitive.ScrubArea
      className={cn("flex cursor-ew-resize", className)}
      data-slot="number-field-scrub-area"
      {...props}
    >
      <Label className="cursor-ew-resize" htmlFor={context.fieldId}>
        {label}
      </Label>
      <NumberFieldPrimitive.ScrubAreaCursor className="drop-shadow-[0_1px_1px_#0008] filter">
        <CursorGrowIcon />
      </NumberFieldPrimitive.ScrubAreaCursor>
    </NumberFieldPrimitive.ScrubArea>
  );
}

function CursorGrowIcon(props: React.ComponentProps<"svg">) {
  return (
    <svg
      fill="black"
      height="14"
      stroke="white"
      viewBox="0 0 24 14"
      width="26"
      xmlns="http://www.w3.org/2000/svg"
      {...props}
    >
      <path d="M19.5 5.5L6.49737 5.51844V2L1 6.9999L6.5 12L6.49737 8.5L19.5 8.5V12L25 6.9999L19.5 2V5.5Z" />
    </svg>
  );
}

export {
  NumberField,
  NumberFieldScrubArea,
  NumberFieldDecrement,
  NumberFieldIncrement,
  NumberFieldGroup,
  NumberFieldInput,
};
```

## File: `web/src/components/ui/pagination.tsx`
```tsx
"use client";

import { mergeProps } from "@base-ui/react/merge-props";
import { useRender } from "@base-ui/react/use-render";
import {
  ChevronLeftIcon,
  ChevronRightIcon,
  MoreHorizontalIcon,
} from "lucide-react";
import type * as React from "react";

import { cn } from "@/lib/utils";
import { type Button, buttonVariants } from "@/components/ui/button";

function Pagination({ className, ...props }: React.ComponentProps<"nav">) {
  return (
    <nav
      aria-label="pagination"
      className={cn("mx-auto flex w-full justify-center", className)}
      data-slot="pagination"
      {...props}
    />
  );
}

function PaginationContent({
  className,
  ...props
}: React.ComponentProps<"ul">) {
  return (
    <ul
      className={cn("flex flex-row items-center gap-1", className)}
      data-slot="pagination-content"
      {...props}
    />
  );
}

function PaginationItem({ ...props }: React.ComponentProps<"li">) {
  return <li data-slot="pagination-item" {...props} />;
}

type PaginationLinkProps = {
  isActive?: boolean;
  size?: React.ComponentProps<typeof Button>["size"];
} & useRender.ComponentProps<"a">;

function PaginationLink({
  className,
  isActive,
  size = "icon",
  render,
  ...props
}: PaginationLinkProps) {
  const defaultProps = {
    "aria-current": isActive ? ("page" as const) : undefined,
    className: render
      ? className
      : cn(
          buttonVariants({
            size,
            variant: isActive ? "outline" : "ghost",
          }),
          className,
        ),
    "data-active": isActive,
    "data-slot": "pagination-link",
  };

  return useRender({
    defaultTagName: "a",
    props: mergeProps<"a">(defaultProps, props),
    render,
  });
}

function PaginationPrevious({
  className,
  ...props
}: React.ComponentProps<typeof PaginationLink>) {
  return (
    <PaginationLink
      aria-label="Go to previous page"
      className={cn("max-sm:aspect-square max-sm:p-0", className)}
      size="default"
      {...props}
    >
      <ChevronLeftIcon className="sm:-ms-1" />
      <span className="max-sm:hidden">Previous</span>
    </PaginationLink>
  );
}

function PaginationNext({
  className,
  ...props
}: React.ComponentProps<typeof PaginationLink>) {
  return (
    <PaginationLink
      aria-label="Go to next page"
      className={cn("max-sm:aspect-square max-sm:p-0", className)}
      size="default"
      {...props}
    >
      <span className="max-sm:hidden">Next</span>
      <ChevronRightIcon className="sm:-me-1" />
    </PaginationLink>
  );
}

function PaginationEllipsis({
  className,
  ...props
}: React.ComponentProps<"span">) {
  return (
    <span
      aria-hidden
      className={cn("flex min-w-7 justify-center", className)}
      data-slot="pagination-ellipsis"
      {...props}
    >
      <MoreHorizontalIcon className="size-5 sm:size-4" />
      <span className="sr-only">More pages</span>
    </span>
  );
}

export {
  Pagination,
  PaginationContent,
  PaginationLink,
  PaginationItem,
  PaginationPrevious,
  PaginationNext,
  PaginationEllipsis,
};
```

## File: `web/src/components/ui/popover.tsx`
```tsx
"use client";

import { Popover as PopoverPrimitive } from "@base-ui/react/popover";

import { cn } from "@/lib/utils";

const PopoverCreateHandle = PopoverPrimitive.createHandle;

const Popover = PopoverPrimitive.Root;

function PopoverTrigger(props: PopoverPrimitive.Trigger.Props) {
  return <PopoverPrimitive.Trigger data-slot="popover-trigger" {...props} />;
}

function PopoverPopup({
  children,
  className,
  side = "bottom",
  align = "center",
  sideOffset = 4,
  alignOffset = 0,
  tooltipStyle = false,
  ...props
}: PopoverPrimitive.Popup.Props & {
  side?: PopoverPrimitive.Positioner.Props["side"];
  align?: PopoverPrimitive.Positioner.Props["align"];
  sideOffset?: PopoverPrimitive.Positioner.Props["sideOffset"];
  alignOffset?: PopoverPrimitive.Positioner.Props["alignOffset"];
  tooltipStyle?: boolean;
}) {
  return (
    <PopoverPrimitive.Portal>
      <PopoverPrimitive.Positioner
        align={align}
        alignOffset={alignOffset}
        className="z-50 h-(--positioner-height) w-(--positioner-width) max-w-(--available-width) transition-[top,left,right,bottom,transform] data-instant:transition-none"
        data-slot="popover-positioner"
        side={side}
        sideOffset={sideOffset}
      >
        <PopoverPrimitive.Popup
          className={cn(
            "relative flex h-(--popup-height,auto) w-(--popup-width,auto) origin-(--transform-origin) rounded-lg border bg-popover not-dark:bg-clip-padding text-popover-foreground shadow-lg/5 transition-[width,height,scale,opacity] before:pointer-events-none before:absolute before:inset-0 before:rounded-[calc(var(--radius-lg)-1px)] before:shadow-[0_1px_--theme(--color-black/6%)] data-starting-style:scale-98 data-starting-style:opacity-0 dark:before:shadow-[0_-1px_--theme(--color-white/6%)]",
            tooltipStyle &&
              "w-fit text-balance rounded-md text-xs shadow-md/5 before:rounded-[calc(var(--radius-md)-1px)]",
            className,
          )}
          data-slot="popover-popup"
          {...props}
        >
          <PopoverPrimitive.Viewport
            className={cn(
              "relative size-full max-h-(--available-height) overflow-clip px-(--viewport-inline-padding) py-4 outline-none [--viewport-inline-padding:--spacing(4)] data-instant:transition-none **:data-current:data-ending-style:opacity-0 **:data-current:data-starting-style:opacity-0 **:data-previous:data-ending-style:opacity-0 **:data-previous:data-starting-style:opacity-0 **:data-current:w-[calc(var(--popup-width)-2*var(--viewport-inline-padding)-2px)] **:data-previous:w-[calc(var(--popup-width)-2*var(--viewport-inline-padding)-2px)] **:data-current:opacity-100 **:data-previous:opacity-100 **:data-current:transition-opacity **:data-previous:transition-opacity",
              tooltipStyle
                ? "py-1 [--viewport-inline-padding:--spacing(2)]"
                : "not-data-transitioning:overflow-y-auto",
            )}
            data-slot="popover-viewport"
          >
            {children}
          </PopoverPrimitive.Viewport>
        </PopoverPrimitive.Popup>
      </PopoverPrimitive.Positioner>
    </PopoverPrimitive.Portal>
  );
}

function PopoverClose({ ...props }: PopoverPrimitive.Close.Props) {
  return <PopoverPrimitive.Close data-slot="popover-close" {...props} />;
}

function PopoverTitle({ className, ...props }: PopoverPrimitive.Title.Props) {
  return (
    <PopoverPrimitive.Title
      className={cn("font-semibold text-lg leading-none", className)}
      data-slot="popover-title"
      {...props}
    />
  );
}

function PopoverDescription({
  className,
  ...props
}: PopoverPrimitive.Description.Props) {
  return (
    <PopoverPrimitive.Description
      className={cn("text-muted-foreground text-sm", className)}
      data-slot="popover-description"
      {...props}
    />
  );
}

export {
  PopoverCreateHandle,
  Popover,
  PopoverTrigger,
  PopoverPopup,
  PopoverPopup as PopoverContent,
  PopoverTitle,
  PopoverDescription,
  PopoverClose,
};
```

## File: `web/src/components/ui/preview-card.tsx`
```tsx
"use client";

import { PreviewCard as PreviewCardPrimitive } from "@base-ui/react/preview-card";

import { cn } from "@/lib/utils";

const PreviewCard = PreviewCardPrimitive.Root;

function PreviewCardTrigger({ ...props }: PreviewCardPrimitive.Trigger.Props) {
  return (
    <PreviewCardPrimitive.Trigger data-slot="preview-card-trigger" {...props} />
  );
}

function PreviewCardPopup({
  className,
  children,
  align = "center",
  sideOffset = 4,
  ...props
}: PreviewCardPrimitive.Popup.Props & {
  align?: PreviewCardPrimitive.Positioner.Props["align"];
  sideOffset?: PreviewCardPrimitive.Positioner.Props["sideOffset"];
}) {
  return (
    <PreviewCardPrimitive.Portal>
      <PreviewCardPrimitive.Positioner
        align={align}
        className="z-50"
        data-slot="preview-card-positioner"
        sideOffset={sideOffset}
      >
        <PreviewCardPrimitive.Popup
          className={cn(
            "relative flex w-64 origin-(--transform-origin) text-balance rounded-lg border bg-popover not-dark:bg-clip-padding p-4 text-popover-foreground text-sm shadow-lg/5 transition-[scale,opacity] before:pointer-events-none before:absolute before:inset-0 before:rounded-[calc(var(--radius-lg)-1px)] before:shadow-[0_1px_--theme(--color-black/6%)] data-ending-style:scale-98 data-starting-style:scale-98 data-ending-style:opacity-0 data-starting-style:opacity-0 dark:before:shadow-[0_-1px_--theme(--color-white/6%)]",
            className,
          )}
          data-slot="preview-card-content"
          {...props}
        >
          {children}
        </PreviewCardPrimitive.Popup>
      </PreviewCardPrimitive.Positioner>
    </PreviewCardPrimitive.Portal>
  );
}

export {
  PreviewCard,
  PreviewCard as HoverCard,
  PreviewCardTrigger,
  PreviewCardTrigger as HoverCardTrigger,
  PreviewCardPopup,
  PreviewCardPopup as HoverCardContent,
};
```

## File: `web/src/components/ui/progress.tsx`
```tsx
"use client";

import { Progress as ProgressPrimitive } from "@base-ui/react/progress";

import { cn } from "@/lib/utils";

function Progress({
  className,
  children,
  ...props
}: ProgressPrimitive.Root.Props) {
  return (
    <ProgressPrimitive.Root
      className={cn("flex w-full flex-col gap-2", className)}
      data-slot="progress"
      {...props}
    >
      {children ? (
        children
      ) : (
        <ProgressTrack>
          <ProgressIndicator />
        </ProgressTrack>
      )}
    </ProgressPrimitive.Root>
  );
}

function ProgressLabel({ className, ...props }: ProgressPrimitive.Label.Props) {
  return (
    <ProgressPrimitive.Label
      className={cn("font-medium text-sm", className)}
      data-slot="progress-label"
      {...props}
    />
  );
}

function ProgressTrack({ className, ...props }: ProgressPrimitive.Track.Props) {
  return (
    <ProgressPrimitive.Track
      className={cn(
        "block h-1.5 w-full overflow-hidden rounded-full bg-input",
        className,
      )}
      data-slot="progress-track"
      {...props}
    />
  );
}

function ProgressIndicator({
  className,
  ...props
}: ProgressPrimitive.Indicator.Props) {
  return (
    <ProgressPrimitive.Indicator
      className={cn("bg-primary transition-all duration-500", className)}
      data-slot="progress-indicator"
      {...props}
    />
  );
}

function ProgressValue({ className, ...props }: ProgressPrimitive.Value.Props) {
  return (
    <ProgressPrimitive.Value
      className={cn("text-sm tabular-nums", className)}
      data-slot="progress-value"
      {...props}
    />
  );
}

export {
  Progress,
  ProgressLabel,
  ProgressTrack,
  ProgressIndicator,
  ProgressValue,
};
```

## File: `web/src/components/ui/radio-group.tsx`
```tsx
"use client";

import { Radio as RadioPrimitive } from "@base-ui/react/radio";
import { RadioGroup as RadioGroupPrimitive } from "@base-ui/react/radio-group";

import { cn } from "@/lib/utils";

function RadioGroup({ className, ...props }: RadioGroupPrimitive.Props) {
  return (
    <RadioGroupPrimitive
      className={cn("flex flex-col gap-3", className)}
      data-slot="radio-group"
      {...props}
    />
  );
}

function Radio({ className, ...props }: RadioPrimitive.Root.Props) {
  return (
    <RadioPrimitive.Root
      className={cn(
        "relative inline-flex size-4.5 shrink-0 items-center justify-center rounded-full border border-input bg-background not-dark:bg-clip-padding shadow-xs/5 outline-none transition-shadow before:pointer-events-none before:absolute before:inset-0 before:rounded-full not-data-disabled:not-data-checked:not-aria-invalid:before:shadow-[0_1px_--theme(--color-black/6%)] focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-1 focus-visible:ring-offset-background aria-invalid:border-destructive/36 focus-visible:aria-invalid:border-destructive/64 focus-visible:aria-invalid:ring-destructive/48 data-disabled:opacity-64 sm:size-4 dark:not-data-checked:bg-input/32 dark:aria-invalid:ring-destructive/24 dark:not-data-disabled:not-data-checked:not-aria-invalid:before:shadow-[0_-1px_--theme(--color-white/6%)] [[data-disabled],[data-checked],[aria-invalid]]:shadow-none",
        className,
      )}
      data-slot="radio"
      {...props}
    >
      <RadioPrimitive.Indicator
        className="-inset-px absolute flex size-4.5 items-center justify-center rounded-full before:size-2 before:rounded-full before:bg-primary-foreground data-unchecked:hidden data-checked:bg-primary sm:size-4 sm:before:size-1.5"
        data-slot="radio-indicator"
      />
    </RadioPrimitive.Root>
  );
}

export { RadioGroup, Radio, Radio as RadioGroupItem };
```

## File: `web/src/components/ui/scroll-area.tsx`
```tsx
"use client";

import { ScrollArea as ScrollAreaPrimitive } from "@base-ui/react/scroll-area";

import { cn } from "@/lib/utils";

function ScrollArea({
  className,
  children,
  scrollFade = false,
  scrollbarGutter = false,
  ...props
}: ScrollAreaPrimitive.Root.Props & {
  scrollFade?: boolean;
  scrollbarGutter?: boolean;
}) {
  return (
    <ScrollAreaPrimitive.Root
      className={cn("size-full min-h-0", className)}
      {...props}
    >
      <ScrollAreaPrimitive.Viewport
        className={cn(
          "h-full rounded-[inherit] outline-none transition-shadows focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-1 focus-visible:ring-offset-background data-has-overflow-x:overscroll-x-contain",
          scrollFade &&
            "mask-t-from-[calc(100%-min(var(--fade-size),var(--scroll-area-overflow-y-start)))] mask-b-from-[calc(100%-min(var(--fade-size),var(--scroll-area-overflow-y-end)))] mask-l-from-[calc(100%-min(var(--fade-size),var(--scroll-area-overflow-x-start)))] mask-r-from-[calc(100%-min(var(--fade-size),var(--scroll-area-overflow-x-end)))] [--fade-size:1.5rem]",
          scrollbarGutter &&
            "data-has-overflow-y:pe-2.5 data-has-overflow-x:pb-2.5",
        )}
        data-slot="scroll-area-viewport"
      >
        {children}
      </ScrollAreaPrimitive.Viewport>
      <ScrollBar orientation="vertical" />
      <ScrollBar orientation="horizontal" />
      <ScrollAreaPrimitive.Corner data-slot="scroll-area-corner" />
    </ScrollAreaPrimitive.Root>
  );
}

function ScrollBar({
  className,
  orientation = "vertical",
  ...props
}: ScrollAreaPrimitive.Scrollbar.Props) {
  return (
    <ScrollAreaPrimitive.Scrollbar
      className={cn(
        "m-1 flex opacity-0 transition-opacity delay-300 data-[orientation=horizontal]:h-1.5 data-[orientation=vertical]:w-1.5 data-[orientation=horizontal]:flex-col data-hovering:opacity-100 data-scrolling:opacity-100 data-hovering:delay-0 data-scrolling:delay-0 data-hovering:duration-100 data-scrolling:duration-100",
        className,
      )}
      data-slot="scroll-area-scrollbar"
      orientation={orientation}
      {...props}
    >
      <ScrollAreaPrimitive.Thumb
        className="relative flex-1 rounded-full bg-foreground/20"
        data-slot="scroll-area-thumb"
      />
    </ScrollAreaPrimitive.Scrollbar>
  );
}

export { ScrollArea, ScrollBar };
```

## File: `web/src/components/ui/select.tsx`
```tsx
"use client";

import { Select as SelectPrimitive } from "@base-ui/react/select";
import {
  ChevronDownIcon,
  ChevronsUpDownIcon,
  ChevronUpIcon,
} from "lucide-react";

import { cn } from "@/lib/utils";

const Select = SelectPrimitive.Root;

function SelectTrigger({
  className,
  size = "default",
  children,
  ...props
}: SelectPrimitive.Trigger.Props & {
  size?: "sm" | "default" | "lg";
}) {
  return (
    <SelectPrimitive.Trigger
      className={cn(
        "relative inline-flex min-h-9 w-full min-w-36 select-none items-center justify-center gap-2 rounded-lg border border-input bg-background not-dark:bg-clip-padding px-[calc(--spacing(3)-1px)] text-left text-base shadow-xs/5 outline-none ring-ring/24 transition-shadow before:pointer-events-none before:absolute before:inset-0 before:rounded-[calc(var(--radius-lg)-1px)] not-data-disabled:not-focus-visible:not-aria-invalid:not-data-pressed:before:shadow-[0_1px_--theme(--color-black/4%)] pointer-coarse:after:absolute pointer-coarse:after:size-full pointer-coarse:after:min-h-11 focus-visible:border-ring focus-visible:ring-[3px] aria-invalid:border-destructive/36 focus-visible:aria-invalid:border-destructive/64 focus-visible:aria-invalid:ring-destructive/16 data-disabled:pointer-events-none data-disabled:opacity-64 sm:min-h-8 sm:text-sm dark:bg-input/32 dark:aria-invalid:ring-destructive/24 dark:not-data-disabled:not-focus-visible:not-aria-invalid:not-data-pressed:before:shadow-[0_-1px_--theme(--color-white/6%)] [&_svg:not([class*='opacity-'])]:opacity-80 [&_svg:not([class*='size-'])]:size-4.5 sm:[&_svg:not([class*='size-'])]:size-4 [&_svg]:pointer-events-none [&_svg]:shrink-0 [[data-disabled],:focus-visible,[aria-invalid],[data-pressed]]:shadow-none",
        size === "sm" &&
          "min-h-8 gap-1.5 px-[calc(--spacing(2.5)-1px)] sm:min-h-7",
        size === "lg" && "min-h-10 sm:min-h-9",
        className,
      )}
      data-slot="select-trigger"
      {...props}
    >
      {children}
      <SelectPrimitive.Icon data-slot="select-icon">
        <ChevronsUpDownIcon className="-me-1 size-4.5 opacity-80 sm:size-4" />
      </SelectPrimitive.Icon>
    </SelectPrimitive.Trigger>
  );
}

function SelectValue({ className, ...props }: SelectPrimitive.Value.Props) {
  return (
    <SelectPrimitive.Value
      className={cn(
        "flex-1 truncate data-placeholder:text-muted-foreground",
        className,
      )}
      data-slot="select-value"
      {...props}
    />
  );
}

function SelectPopup({
  className,
  children,
  sideOffset = 4,
  alignItemWithTrigger = true,
  ...props
}: SelectPrimitive.Popup.Props & {
  sideOffset?: SelectPrimitive.Positioner.Props["sideOffset"];
  alignItemWithTrigger?: SelectPrimitive.Positioner.Props["alignItemWithTrigger"];
}) {
  return (
    <SelectPrimitive.Portal>
      <SelectPrimitive.Positioner
        alignItemWithTrigger={alignItemWithTrigger}
        className="z-50 select-none"
        data-slot="select-positioner"
        sideOffset={sideOffset}
      >
        <SelectPrimitive.Popup
          className="origin-(--transform-origin)"
          data-slot="select-popup"
          {...props}
        >
          <SelectPrimitive.ScrollUpArrow
            className="top-0 z-50 flex h-6 w-full cursor-default items-center justify-center before:pointer-events-none before:absolute before:inset-x-px before:top-px before:h-[200%] before:rounded-t-[calc(var(--radius-lg)-1px)] before:bg-linear-to-b before:from-50% before:from-popover"
            data-slot="select-scroll-up-arrow"
          >
            <ChevronUpIcon className="relative size-4.5 sm:size-4" />
          </SelectPrimitive.ScrollUpArrow>
          <div className="relative h-full rounded-lg border bg-popover not-dark:bg-clip-padding shadow-lg/5 before:pointer-events-none before:absolute before:inset-0 before:rounded-[calc(var(--radius-lg)-1px)] before:shadow-[0_1px_--theme(--color-black/6%)] dark:before:shadow-[0_-1px_--theme(--color-white/6%)]">
            <SelectPrimitive.List
              className={cn(
                "max-h-(--available-height) min-w-(--anchor-width) overflow-y-auto p-1",
                className,
              )}
              data-slot="select-list"
            >
              {children}
            </SelectPrimitive.List>
          </div>
          <SelectPrimitive.ScrollDownArrow
            className="bottom-0 z-50 flex h-6 w-full cursor-default items-center justify-center before:pointer-events-none before:absolute before:inset-x-px before:bottom-px before:h-[200%] before:rounded-b-[calc(var(--radius-lg)-1px)] before:bg-linear-to-t before:from-50% before:from-popover"
            data-slot="select-scroll-down-arrow"
          >
            <ChevronDownIcon className="relative size-4.5 sm:size-4" />
          </SelectPrimitive.ScrollDownArrow>
        </SelectPrimitive.Popup>
      </SelectPrimitive.Positioner>
    </SelectPrimitive.Portal>
  );
}

function SelectItem({
  className,
  children,
  ...props
}: SelectPrimitive.Item.Props) {
  return (
    <SelectPrimitive.Item
      className={cn(
        "grid min-h-8 in-data-[side=none]:min-w-[calc(var(--anchor-width)+1.25rem)] cursor-default grid-cols-[1rem_1fr] items-center gap-2 rounded-sm py-1 ps-2 pe-4 text-base outline-none data-disabled:pointer-events-none data-highlighted:bg-accent data-highlighted:text-accent-foreground data-disabled:opacity-64 sm:min-h-7 sm:text-sm [&_svg:not([class*='size-'])]:size-4.5 sm:[&_svg:not([class*='size-'])]:size-4 [&_svg]:pointer-events-none [&_svg]:shrink-0",
        className,
      )}
      data-slot="select-item"
      {...props}
    >
      <SelectPrimitive.ItemIndicator className="col-start-1">
        <svg
          fill="none"
          height="24"
          stroke="currentColor"
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth="2"
          viewBox="0 0 24 24"
          width="24"
          xmlns="http://www.w3.org/1500/svg"
        >
          <path d="M5.252 12.7 10.2 18.63 18.748 5.37" />
        </svg>
      </SelectPrimitive.ItemIndicator>
      <SelectPrimitive.ItemText className="col-start-2 min-w-0">
        {children}
      </SelectPrimitive.ItemText>
    </SelectPrimitive.Item>
  );
}

function SelectSeparator({
  className,
  ...props
}: SelectPrimitive.Separator.Props) {
  return (
    <SelectPrimitive.Separator
      className={cn("mx-2 my-1 h-px bg-border", className)}
      data-slot="select-separator"
      {...props}
    />
  );
}

function SelectGroup(props: SelectPrimitive.Group.Props) {
  return <SelectPrimitive.Group data-slot="select-group" {...props} />;
}

function SelectGroupLabel(props: SelectPrimitive.GroupLabel.Props) {
  return (
    <SelectPrimitive.GroupLabel
      className="px-2 py-1.5 font-medium text-muted-foreground text-xs"
      data-slot="select-group-label"
      {...props}
    />
  );
}

export {
  Select,
  SelectTrigger,
  SelectValue,
  SelectPopup,
  SelectPopup as SelectContent,
  SelectItem,
  SelectSeparator,
  SelectGroup,
  SelectGroupLabel,
};
```

## File: `web/src/components/ui/separator.tsx`
```tsx
import { Separator as SeparatorPrimitive } from "@base-ui/react/separator";

import { cn } from "@/lib/utils";

function Separator({
  className,
  orientation = "horizontal",
  ...props
}: SeparatorPrimitive.Props) {
  return (
    <SeparatorPrimitive
      className={cn(
        "shrink-0 bg-input data-[orientation=horizontal]:h-px data-[orientation=horizontal]:w-full data-[orientation=vertical]:w-px data-[orientation=vertical]:not-[[class^='h-']]:not-[[class*='_h-']]:self-stretch",
        className,
      )}
      data-slot="separator"
      orientation={orientation}
      {...props}
    />
  );
}

export { Separator };
```

## File: `web/src/components/ui/sheet.tsx`
```tsx
"use client";

import { Dialog as SheetPrimitive } from "@base-ui/react/dialog";
import { XIcon } from "lucide-react";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";

const Sheet = SheetPrimitive.Root;

const SheetPortal = SheetPrimitive.Portal;

function SheetTrigger(props: SheetPrimitive.Trigger.Props) {
  return <SheetPrimitive.Trigger data-slot="sheet-trigger" {...props} />;
}

function SheetClose(props: SheetPrimitive.Close.Props) {
  return <SheetPrimitive.Close data-slot="sheet-close" {...props} />;
}

function SheetBackdrop({ className, ...props }: SheetPrimitive.Backdrop.Props) {
  return (
    <SheetPrimitive.Backdrop
      className={cn(
        "fixed inset-0 z-50 bg-black/32 backdrop-blur-sm transition-all duration-200 data-ending-style:opacity-0 data-starting-style:opacity-0",
        className,
      )}
      data-slot="sheet-backdrop"
      {...props}
    />
  );
}

function SheetViewport({
  className,
  side,
  inset = false,
  ...props
}: SheetPrimitive.Viewport.Props & {
  side?: "right" | "left" | "top" | "bottom";
  inset?: boolean;
}) {
  return (
    <SheetPrimitive.Viewport
      className={cn(
        "fixed inset-0 z-50 grid",
        side === "bottom" && "grid grid-rows-[1fr_auto] pt-12",
        side === "top" && "grid grid-rows-[auto_1fr] pb-12",
        side === "left" && "flex justify-start",
        side === "right" && "flex justify-end",
        inset && "sm:p-4",
      )}
      data-slot="sheet-viewport"
      {...props}
    />
  );
}

function SheetPopup({
  className,
  children,
  showCloseButton = true,
  side = "right",
  inset = false,
  ...props
}: SheetPrimitive.Popup.Props & {
  showCloseButton?: boolean;
  side?: "right" | "left" | "top" | "bottom";
  inset?: boolean;
}) {
  return (
    <SheetPortal>
      <SheetBackdrop />
      <SheetViewport inset={inset} side={side}>
        <SheetPrimitive.Popup
          className={cn(
            "relative flex max-h-full min-h-0 w-full min-w-0 flex-col bg-popover not-dark:bg-clip-padding text-popover-foreground shadow-lg/5 transition-[opacity,translate] duration-200 ease-in-out will-change-transform before:pointer-events-none before:absolute before:inset-0 before:shadow-[0_1px_--theme(--color-black/6%)] data-ending-style:opacity-0 data-starting-style:opacity-0 max-sm:before:hidden dark:before:shadow-[0_-1px_--theme(--color-white/6%)]",
            side === "bottom" &&
              "row-start-2 border-t data-ending-style:translate-y-8 data-starting-style:translate-y-8",
            side === "top" &&
              "data-ending-style:-translate-y-8 data-starting-style:-translate-y-8 border-b",
            side === "left" &&
              "data-ending-style:-translate-x-8 data-starting-style:-translate-x-8 w-[calc(100%-(--spacing(12)))] max-w-md border-e",
            side === "right" &&
              "col-start-2 w-[calc(100%-(--spacing(12)))] max-w-md border-s data-ending-style:translate-x-8 data-starting-style:translate-x-8",
            inset &&
              "before:hidden sm:rounded-2xl sm:border sm:before:rounded-[calc(var(--radius-2xl)-1px)] sm:**:data-[slot=sheet-footer]:rounded-b-[calc(var(--radius-2xl)-1px)]",
            className,
          )}
          data-slot="sheet-popup"
          {...props}
        >
          {children}
          {showCloseButton && (
            <SheetPrimitive.Close
              aria-label="Close"
              className="absolute end-2 top-2"
              render={<Button size="icon" variant="ghost" />}
            >
              <XIcon />
            </SheetPrimitive.Close>
          )}
        </SheetPrimitive.Popup>
      </SheetViewport>
    </SheetPortal>
  );
}

function SheetHeader({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      className={cn(
        "flex flex-col gap-2 p-6 in-[[data-slot=sheet-popup]:has([data-slot=sheet-panel])]:pb-3 max-sm:pb-4",
        className,
      )}
      data-slot="sheet-header"
      {...props}
    />
  );
}

function SheetFooter({
  className,
  variant = "default",
  ...props
}: React.ComponentProps<"div"> & {
  variant?: "default" | "bare";
}) {
  return (
    <div
      className={cn(
        "flex flex-col-reverse gap-2 px-6 sm:flex-row sm:justify-end",
        variant === "default" && "border-t bg-muted/72 py-4",
        variant === "bare" &&
          "in-[[data-slot=sheet-popup]:has([data-slot=sheet-panel])]:pt-3 pt-4 pb-6",
        className,
      )}
      data-slot="sheet-footer"
      {...props}
    />
  );
}

function SheetTitle({ className, ...props }: SheetPrimitive.Title.Props) {
  return (
    <SheetPrimitive.Title
      className={cn("font-heading text-xl leading-none", className)}
      data-slot="sheet-title"
      {...props}
    />
  );
}

function SheetDescription({
  className,
  ...props
}: SheetPrimitive.Description.Props) {
  return (
    <SheetPrimitive.Description
      className={cn("text-muted-foreground text-sm", className)}
      data-slot="sheet-description"
      {...props}
    />
  );
}

function SheetPanel({
  className,
  scrollFade = true,
  ...props
}: React.ComponentProps<"div"> & { scrollFade?: boolean }) {
  return (
    <ScrollArea scrollFade={scrollFade}>
      <div
        className={cn(
          "px-6 in-[[data-slot=sheet-popup]:has([data-slot=sheet-header])]:pt-1 in-[[data-slot=sheet-popup]:not(:has([data-slot=sheet-header]))]:pt-6 in-[[data-slot=sheet-popup]:not(:has([data-slot=sheet-footer]))]:pb-6! in-[[data-slot=sheet-popup]:not(:has([data-slot=sheet-footer].border-t))]:pb-1 pb-6",
          className,
        )}
        data-slot="sheet-panel"
        {...props}
      />
    </ScrollArea>
  );
}

export {
  Sheet,
  SheetTrigger,
  SheetPortal,
  SheetClose,
  SheetBackdrop,
  SheetBackdrop as SheetOverlay,
  SheetPopup,
  SheetPopup as SheetContent,
  SheetHeader,
  SheetFooter,
  SheetTitle,
  SheetDescription,
  SheetPanel,
};
```

## File: `web/src/components/ui/sidebar.tsx`
```tsx
"use client";

import { mergeProps } from "@base-ui/react/merge-props";
import { useRender } from "@base-ui/react/use-render";
import { cva, type VariantProps } from "class-variance-authority";
import { PanelLeftIcon } from "lucide-react";
import * as React from "react";

import { useIsMobile } from "@/hooks/use-mobile";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Separator } from "@/components/ui/separator";
import {
  Sheet,
  SheetDescription,
  SheetHeader,
  SheetPopup,
  SheetTitle,
} from "@/components/ui/sheet";
import { Skeleton } from "@/components/ui/skeleton";
import {
  Tooltip,
  TooltipPopup,
  TooltipTrigger,
} from "@/components/ui/tooltip";

const SIDEBAR_COOKIE_NAME = "sidebar_state";
const SIDEBAR_COOKIE_MAX_AGE = 60 * 60 * 24 * 7;
const SIDEBAR_WIDTH = "16rem";
const SIDEBAR_WIDTH_MOBILE = "18rem";
const SIDEBAR_WIDTH_ICON = "3rem";
const SIDEBAR_KEYBOARD_SHORTCUT = "b";

type SidebarContextProps = {
  state: "expanded" | "collapsed";
  open: boolean;
  setOpen: (open: boolean) => void;
  openMobile: boolean;
  setOpenMobile: (open: boolean) => void;
  isMobile: boolean;
  toggleSidebar: () => void;
};

const SidebarContext = React.createContext<SidebarContextProps | null>(null);

function useSidebar() {
  const context = React.useContext(SidebarContext);
  if (!context) {
    throw new Error("useSidebar must be used within a SidebarProvider.");
  }

  return context;
}

function SidebarProvider({
  defaultOpen = true,
  open: openProp,
  onOpenChange: setOpenProp,
  className,
  style,
  children,
  ...props
}: React.ComponentProps<"div"> & {
  defaultOpen?: boolean;
  open?: boolean;
  onOpenChange?: (open: boolean) => void;
}) {
  const isMobile = useIsMobile();
  const [openMobile, setOpenMobile] = React.useState(false);

  // This is the internal state of the sidebar.
  // We use openProp and setOpenProp for control from outside the component.
  const [_open, _setOpen] = React.useState(defaultOpen);
  const open = openProp ?? _open;
  const setOpen = React.useCallback(
    async (value: boolean | ((value: boolean) => boolean)) => {
      const openState = typeof value === "function" ? value(open) : value;
      if (setOpenProp) {
        setOpenProp(openState);
      } else {
        _setOpen(openState);
      }

      // This sets the cookie to keep the sidebar state.
      await cookieStore.set({
        expires: Date.now() + SIDEBAR_COOKIE_MAX_AGE * 1000,
        name: SIDEBAR_COOKIE_NAME,
        path: "/",
        value: String(openState),
      });
    },
    [setOpenProp, open],
  );

  // Helper to toggle the sidebar.
  const toggleSidebar = React.useCallback(() => {
    return isMobile ? setOpenMobile((open) => !open) : setOpen((open) => !open);
  }, [isMobile, setOpen]);

  // Adds a keyboard shortcut to toggle the sidebar.
  React.useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      if (
        event.key === SIDEBAR_KEYBOARD_SHORTCUT &&
        (event.metaKey || event.ctrlKey)
      ) {
        event.preventDefault();
        toggleSidebar();
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [toggleSidebar]);

  // We add a state so that we can do data-state="expanded" or "collapsed".
  // This makes it easier to style the sidebar with Tailwind classes.
  const state = open ? "expanded" : "collapsed";

  const contextValue = React.useMemo<SidebarContextProps>(
    () => ({
      isMobile,
      open,
      openMobile,
      setOpen,
      setOpenMobile,
      state,
      toggleSidebar,
    }),
    [state, open, setOpen, isMobile, openMobile, toggleSidebar],
  );

  return (
    <SidebarContext.Provider value={contextValue}>
      <div
        className={cn(
          "group/sidebar-wrapper flex min-h-svh w-full has-data-[variant=inset]:bg-sidebar",
          className,
        )}
        data-slot="sidebar-wrapper"
        style={
          {
            "--sidebar-width": SIDEBAR_WIDTH,
            "--sidebar-width-icon": SIDEBAR_WIDTH_ICON,
            ...style,
          } as React.CSSProperties
        }
        {...props}
      >
        {children}
      </div>
    </SidebarContext.Provider>
  );
}

function Sidebar({
  side = "left",
  variant = "sidebar",
  collapsible = "offcanvas",
  className,
  children,
  ...props
}: React.ComponentProps<"div"> & {
  side?: "left" | "right";
  variant?: "sidebar" | "floating" | "inset";
  collapsible?: "offcanvas" | "icon" | "none";
}) {
  const { isMobile, state, openMobile, setOpenMobile } = useSidebar();

  if (collapsible === "none") {
    return (
      <div
        className={cn(
          "flex h-full w-(--sidebar-width) flex-col bg-sidebar text-sidebar-foreground",
          className,
        )}
        data-slot="sidebar"
        {...props}
      >
        {children}
      </div>
    );
  }

  if (isMobile) {
    return (
      <Sheet onOpenChange={setOpenMobile} open={openMobile} {...props}>
        <SheetPopup
          className="w-(--sidebar-width) bg-sidebar p-0 text-sidebar-foreground [&>button]:hidden"
          data-mobile="true"
          data-sidebar="sidebar"
          data-slot="sidebar"
          side={side}
          style={
            {
              "--sidebar-width": SIDEBAR_WIDTH_MOBILE,
            } as React.CSSProperties
          }
        >
          <SheetHeader className="sr-only">
            <SheetTitle>Sidebar</SheetTitle>
            <SheetDescription>Displays the mobile sidebar.</SheetDescription>
          </SheetHeader>
          <div className="flex h-full w-full flex-col">{children}</div>
        </SheetPopup>
      </Sheet>
    );
  }

  return (
    <div
      className="group peer hidden text-sidebar-foreground md:block"
      data-collapsible={state === "collapsed" ? collapsible : ""}
      data-side={side}
      data-slot="sidebar"
      data-state={state}
      data-variant={variant}
    >
      {/* This is what handles the sidebar gap on desktop */}
      <div
        className={cn(
          "relative w-(--sidebar-width) bg-transparent transition-[width] duration-200 ease-linear",
          "group-data-[collapsible=offcanvas]:w-0",
          "group-data-[side=right]:rotate-180",
          variant === "floating" || variant === "inset"
            ? "group-data-[collapsible=icon]:w-[calc(var(--sidebar-width-icon)+(--spacing(4)))]"
            : "group-data-[collapsible=icon]:w-(--sidebar-width-icon)",
        )}
        data-slot="sidebar-gap"
      />
      <div
        className={cn(
          "fixed inset-y-0 z-10 hidden h-svh w-(--sidebar-width) transition-[left,right,width] duration-200 ease-linear md:flex",
          side === "left"
            ? "left-0 group-data-[collapsible=offcanvas]:left-[calc(var(--sidebar-width)*-1)]"
            : "right-0 group-data-[collapsible=offcanvas]:right-[calc(var(--sidebar-width)*-1)]",
          // Adjust the padding for floating and inset variants.
          variant === "floating" || variant === "inset"
            ? "p-2 group-data-[collapsible=icon]:w-[calc(var(--sidebar-width-icon)+(--spacing(4))+2px)]"
            : "group-data-[collapsible=icon]:w-(--sidebar-width-icon) group-data-[side=left]:border-r group-data-[side=right]:border-l",
          className,
        )}
        data-slot="sidebar-container"
        {...props}
      >
        <div
          className="flex h-full w-full flex-col bg-sidebar group-data-[variant=floating]:rounded-lg group-data-[variant=floating]:border group-data-[variant=floating]:border-sidebar-border group-data-[variant=floating]:shadow-sm/5"
          data-sidebar="sidebar"
          data-slot="sidebar-inner"
        >
          {children}
        </div>
      </div>
    </div>
  );
}

function SidebarTrigger({
  className,
  onClick,
  ...props
}: React.ComponentProps<typeof Button>) {
  const { toggleSidebar } = useSidebar();

  return (
    <Button
      className={cn("size-7", className)}
      data-sidebar="trigger"
      data-slot="sidebar-trigger"
      onClick={(event) => {
        onClick?.(event);
        toggleSidebar();
      }}
      size="icon"
      variant="ghost"
      {...props}
    >
      <PanelLeftIcon />
      <span className="sr-only">Toggle Sidebar</span>
    </Button>
  );
}

function SidebarRail({ className, ...props }: React.ComponentProps<"button">) {
  const { toggleSidebar } = useSidebar();

  return (
    <button
      aria-label="Toggle Sidebar"
      className={cn(
        "-translate-x-1/2 group-data-[side=left]:-right-4 absolute inset-y-0 z-20 hidden w-4 transition-all ease-linear after:absolute after:inset-y-0 after:left-1/2 after:w-[2px] hover:after:bg-sidebar-border group-data-[side=right]:left-0 sm:flex",
        "in-data-[side=left]:cursor-w-resize in-data-[side=right]:cursor-e-resize",
        "[[data-side=left][data-state=collapsed]_&]:cursor-e-resize [[data-side=right][data-state=collapsed]_&]:cursor-w-resize",
        "group-data-[collapsible=offcanvas]:translate-x-0 hover:group-data-[collapsible=offcanvas]:bg-sidebar group-data-[collapsible=offcanvas]:after:left-full",
        "[[data-side=left][data-collapsible=offcanvas]_&]:-right-2",
        "[[data-side=right][data-collapsible=offcanvas]_&]:-left-2",
        className,
      )}
      data-sidebar="rail"
      data-slot="sidebar-rail"
      onClick={toggleSidebar}
      tabIndex={-1}
      title="Toggle Sidebar"
      type="button"
      {...props}
    />
  );
}

function SidebarInset({ className, ...props }: React.ComponentProps<"main">) {
  return (
    <main
      className={cn(
        "relative flex w-full flex-1 flex-col bg-background",
        "md:peer-data-[variant=inset]:peer-data-[state=collapsed]:ms-2 md:peer-data-[variant=inset]:m-2 md:peer-data-[variant=inset]:ms-0 md:peer-data-[variant=inset]:rounded-xl md:peer-data-[variant=inset]:shadow-sm/5",
        className,
      )}
      data-slot="sidebar-inset"
      {...props}
    />
  );
}

function SidebarInput({
  className,
  ...props
}: React.ComponentProps<typeof Input>) {
  return (
    <Input
      className={cn("h-8 w-full bg-background shadow-none", className)}
      data-sidebar="input"
      data-slot="sidebar-input"
      {...props}
    />
  );
}

function SidebarHeader({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      className={cn("flex flex-col gap-2 p-2", className)}
      data-sidebar="header"
      data-slot="sidebar-header"
      {...props}
    />
  );
}

function SidebarFooter({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      className={cn("flex flex-col gap-2 p-2", className)}
      data-sidebar="footer"
      data-slot="sidebar-footer"
      {...props}
    />
  );
}

function SidebarSeparator({
  className,
  ...props
}: React.ComponentProps<typeof Separator>) {
  return (
    <Separator
      className={cn("mx-2 w-auto bg-sidebar-border", className)}
      data-sidebar="separator"
      data-slot="sidebar-separator"
      {...props}
    />
  );
}

function SidebarContent({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <ScrollArea
      className="**:data-[slot=scroll-area-scrollbar]:hidden"
      scrollFade
    >
      <div
        className={cn(
          "flex min-h-0 flex-1 flex-col gap-2 overflow-auto group-data-[collapsible=icon]:overflow-hidden",
          className,
        )}
        data-sidebar="content"
        data-slot="sidebar-content"
        {...props}
      />
    </ScrollArea>
  );
}

function SidebarGroup({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      className={cn("relative flex w-full min-w-0 flex-col p-2", className)}
      data-sidebar="group"
      data-slot="sidebar-group"
      {...props}
    />
  );
}

function SidebarGroupLabel({
  className,
  render,
  ...props
}: useRender.ComponentProps<"div">) {
  const defaultProps = {
    className: cn(
      "flex h-8 shrink-0 items-center rounded-lg px-2 font-medium text-sidebar-foreground/70 text-xs outline-hidden ring-sidebar-ring transition-[margin,opacity] duration-200 ease-linear focus-visible:ring-2 [&>svg]:size-4 [&>svg]:shrink-0",
      "group-data-[collapsible=icon]:-mt-8 group-data-[collapsible=icon]:opacity-0",
      className,
    ),
    "data-sidebar": "group-label",
    "data-slot": "sidebar-group-label",
  };

  return useRender({
    defaultTagName: "div",
    props: mergeProps(defaultProps, props),
    render,
  });
}

function SidebarGroupAction({
  className,
  render,
  ...props
}: useRender.ComponentProps<"button">) {
  const defaultProps = {
    className: cn(
      "absolute top-3.5 right-3 flex aspect-square w-5 items-center justify-center rounded-lg p-0 text-sidebar-foreground outline-hidden ring-sidebar-ring transition-transform hover:bg-sidebar-accent hover:text-sidebar-accent-foreground focus-visible:ring-2 [&>svg:not([class*='size-'])]:size-4 [&>svg]:shrink-0",
      // Increases the hit area of the button on mobile.
      "after:-inset-2 after:absolute md:after:hidden",
      "group-data-[collapsible=icon]:hidden",
      className,
    ),
    "data-sidebar": "group-action",
    "data-slot": "sidebar-group-action",
  };

  return useRender({
    defaultTagName: "button",
    props: mergeProps(defaultProps, props),
    render,
  });
}

function SidebarGroupContent({
  className,
  ...props
}: React.ComponentProps<"div">) {
  return (
    <div
      className={cn("w-full text-sm", className)}
      data-sidebar="group-content"
      data-slot="sidebar-group-content"
      {...props}
    />
  );
}

function SidebarMenu({ className, ...props }: React.ComponentProps<"ul">) {
  return (
    <ul
      className={cn("flex w-full min-w-0 flex-col gap-1", className)}
      data-sidebar="menu"
      data-slot="sidebar-menu"
      {...props}
    />
  );
}

function SidebarMenuItem({ className, ...props }: React.ComponentProps<"li">) {
  return (
    <li
      className={cn("group/menu-item relative", className)}
      data-sidebar="menu-item"
      data-slot="sidebar-menu-item"
      {...props}
    />
  );
}

const sidebarMenuButtonVariants = cva(
  "peer/menu-button flex w-full items-center gap-2 overflow-hidden rounded-lg p-2 text-left text-sm outline-hidden ring-sidebar-ring transition-[width,height,padding] hover:bg-sidebar-accent hover:text-sidebar-accent-foreground focus-visible:ring-2 active:bg-sidebar-accent active:text-sidebar-accent-foreground disabled:pointer-events-none disabled:opacity-50 group-has-data-[sidebar=menu-action]/menu-item:pe-8 aria-disabled:pointer-events-none aria-disabled:opacity-50 data-[active=true]:bg-sidebar-accent data-[active=true]:font-medium data-[active=true]:text-sidebar-accent-foreground data-[state=open]:hover:bg-sidebar-accent data-[state=open]:hover:text-sidebar-accent-foreground group-data-[collapsible=icon]:size-8! group-data-[collapsible=icon]:p-2! [&>span:last-child]:truncate [&>svg:not([class*='size-'])]:size-4 [&>svg]:shrink-0",
  {
    defaultVariants: {
      size: "default",
      variant: "default",
    },
    variants: {
      size: {
        default: "h-8 text-sm",
        lg: "h-12 text-sm group-data-[collapsible=icon]:p-0!",
        sm: "h-7 text-xs",
      },
      variant: {
        default: "hover:bg-sidebar-accent hover:text-sidebar-accent-foreground",
        outline:
          "bg-background shadow-[0_0_0_1px_hsl(var(--sidebar-border))] hover:bg-sidebar-accent hover:text-sidebar-accent-foreground hover:shadow-[0_0_0_1px_hsl(var(--sidebar-accent))]",
      },
    },
  },
);

function SidebarMenuButton({
  isActive = false,
  variant = "default",
  size = "default",
  tooltip,
  className,
  render,
  ...props
}: useRender.ComponentProps<"button"> & {
  isActive?: boolean;
  tooltip?: string | React.ComponentProps<typeof TooltipPopup>;
} & VariantProps<typeof sidebarMenuButtonVariants>) {
  const { isMobile, state } = useSidebar();

  const defaultProps = {
    className: cn(sidebarMenuButtonVariants({ size, variant }), className),
    "data-active": isActive,
    "data-sidebar": "menu-button",
    "data-size": size,
    "data-slot": "sidebar-menu-button",
  };

  const buttonProps = mergeProps<"button">(defaultProps, props);

  const buttonElement = useRender({
    defaultTagName: "button",
    props: buttonProps,
    render,
  });

  if (!tooltip) {
    return buttonElement;
  }

  if (typeof tooltip === "string") {
    tooltip = {
      children: tooltip,
    };
  }

  return (
    <Tooltip>
      <TooltipTrigger
        render={buttonElement as React.ReactElement<Record<string, unknown>>}
      />
      <TooltipPopup
        align="center"
        hidden={state !== "collapsed" || isMobile}
        side="right"
        {...tooltip}
      />
    </Tooltip>
  );
}

function SidebarMenuAction({
  className,
  showOnHover = false,
  render,
  ...props
}: useRender.ComponentProps<"button"> & {
  showOnHover?: boolean;
}) {
  const defaultProps = {
    className: cn(
      "absolute top-1.5 right-1 flex aspect-square w-5 items-center justify-center rounded-lg p-0 text-sidebar-foreground outline-hidden ring-sidebar-ring transition-transform hover:bg-sidebar-accent hover:text-sidebar-accent-foreground focus-visible:ring-2 peer-hover/menu-button:text-sidebar-accent-foreground [&>svg:not([class*='size-'])]:size-4 [&>svg]:shrink-0",
      // Increases the hit area of the button on mobile.
      "after:-inset-2 after:absolute md:after:hidden",
      "peer-data-[size=sm]/menu-button:top-1",
      "peer-data-[size=default]/menu-button:top-1.5",
      "peer-data-[size=lg]/menu-button:top-2.5",
      "group-data-[collapsible=icon]:hidden",
      showOnHover &&
        "group-focus-within/menu-item:opacity-100 group-hover/menu-item:opacity-100 data-[state=open]:opacity-100 peer-data-[active=true]/menu-button:text-sidebar-accent-foreground md:opacity-0",
      className,
    ),
    "data-sidebar": "menu-action",
    "data-slot": "sidebar-menu-action",
  };

  return useRender({
    defaultTagName: "button",
    props: mergeProps<"button">(defaultProps, props),
    render,
  });
}

function SidebarMenuBadge({
  className,
  ...props
}: React.ComponentProps<"div">) {
  return (
    <div
      className={cn(
        "pointer-events-none absolute right-1 flex h-5 min-w-5 select-none items-center justify-center rounded-lg px-1 font-medium text-sidebar-foreground text-xs tabular-nums",
        "peer-hover/menu-button:text-sidebar-accent-foreground peer-data-[active=true]/menu-button:text-sidebar-accent-foreground",
        "peer-data-[size=sm]/menu-button:top-1",
        "peer-data-[size=default]/menu-button:top-1.5",
        "peer-data-[size=lg]/menu-button:top-2.5",
        "group-data-[collapsible=icon]:hidden",
        className,
      )}
      data-sidebar="menu-badge"
      data-slot="sidebar-menu-badge"
      {...props}
    />
  );
}

function SidebarMenuSkeleton({
  className,
  showIcon = false,
  ...props
}: React.ComponentProps<"div"> & {
  showIcon?: boolean;
}) {
  // Random width between 50 to 90%.
  const width = React.useMemo(() => {
    return `${Math.floor(Math.random() * 40) + 50}%`;
  }, []);

  return (
    <div
      className={cn("flex h-8 items-center gap-2 rounded-lg px-2", className)}
      data-sidebar="menu-skeleton"
      data-slot="sidebar-menu-skeleton"
      {...props}
    >
      {showIcon && (
        <Skeleton
          className="size-4 rounded-lg"
          data-sidebar="menu-skeleton-icon"
        />
      )}
      <Skeleton
        className="h-4 max-w-(--skeleton-width) flex-1"
        data-sidebar="menu-skeleton-text"
        style={
          {
            "--skeleton-width": width,
          } as React.CSSProperties
        }
      />
    </div>
  );
}

function SidebarMenuSub({ className, ...props }: React.ComponentProps<"ul">) {
  return (
    <ul
      className={cn(
        "mx-3.5 flex min-w-0 translate-x-px flex-col gap-1 border-sidebar-border border-l px-2.5 py-0.5",
        "group-data-[collapsible=icon]:hidden",
        className,
      )}
      data-sidebar="menu-sub"
      data-slot="sidebar-menu-sub"
      {...props}
    />
  );
}

function SidebarMenuSubItem({
  className,
  ...props
}: React.ComponentProps<"li">) {
  return (
    <li
      className={cn("group/menu-sub-item relative", className)}
      data-sidebar="menu-sub-item"
      data-slot="sidebar-menu-sub-item"
      {...props}
    />
  );
}

function SidebarMenuSubButton({
  size = "md",
  isActive = false,
  className,
  render,
  ...props
}: useRender.ComponentProps<"a"> & {
  size?: "sm" | "md";
  isActive?: boolean;
}) {
  const defaultProps = {
    className: cn(
      "-translate-x-px flex h-7 min-w-0 items-center gap-2 overflow-hidden rounded-lg px-2 text-sidebar-foreground outline-hidden ring-sidebar-ring hover:bg-sidebar-accent hover:text-sidebar-accent-foreground focus-visible:ring-2 active:bg-sidebar-accent active:text-sidebar-accent-foreground disabled:pointer-events-none disabled:opacity-50 aria-disabled:pointer-events-none aria-disabled:opacity-50 [&>span:last-child]:truncate [&>svg:not([class*='size-'])]:size-4 [&>svg]:shrink-0 [&>svg]:text-sidebar-accent-foreground",
      "data-[active=true]:bg-sidebar-accent data-[active=true]:text-sidebar-accent-foreground",
      size === "sm" && "text-xs",
      size === "md" && "text-sm",
      "group-data-[collapsible=icon]:hidden",
      className,
    ),
    "data-active": isActive,
    "data-sidebar": "menu-sub-button",
    "data-size": size,
    "data-slot": "sidebar-menu-sub-button",
  };

  return useRender({
    defaultTagName: "a",
    props: mergeProps<"a">(defaultProps, props),
    render,
  });
}

export {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarGroupAction,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarHeader,
  SidebarInput,
  SidebarInset,
  SidebarMenu,
  SidebarMenuAction,
  SidebarMenuBadge,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarMenuSkeleton,
  SidebarMenuSub,
  SidebarMenuSubButton,
  SidebarMenuSubItem,
  SidebarProvider,
  SidebarRail,
  SidebarSeparator,
  SidebarTrigger,
  useSidebar,
};
```

## File: `web/src/components/ui/skeleton.tsx`
```tsx
import { cn } from "@/lib/utils";

function Skeleton({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      className={cn(
        "animate-skeleton rounded-sm [--skeleton-highlight:--alpha(var(--color-white)/64%)] [background:linear-gradient(120deg,transparent_40%,var(--skeleton-highlight),transparent_60%)_var(--color-muted)_0_0/200%_100%_fixed] dark:[--skeleton-highlight:--alpha(var(--color-white)/4%)]",
        className,
      )}
      data-slot="skeleton"
      {...props}
    />
  );
}

export { Skeleton };
```

## File: `web/src/components/ui/slider.tsx`
```tsx
"use client";

import { Slider as SliderPrimitive } from "@base-ui/react/slider";
import * as React from "react";

import { cn } from "@/lib/utils";

function Slider({
  className,
  children,
  defaultValue,
  value,
  min = 0,
  max = 100,
  ...props
}: SliderPrimitive.Root.Props) {
  const _values = React.useMemo(() => {
    if (value !== undefined) {
      return Array.isArray(value) ? value : [value];
    }
    if (defaultValue !== undefined) {
      return Array.isArray(defaultValue) ? defaultValue : [defaultValue];
    }
    return [min];
  }, [value, defaultValue, min]);

  return (
    <SliderPrimitive.Root
      className="data-[orientation=horizontal]:w-full"
      defaultValue={defaultValue}
      max={max}
      min={min}
      thumbAlignment="edge"
      value={value}
      {...props}
    >
      {children}
      <SliderPrimitive.Control
        className={cn(
          "flex touch-none select-none data-disabled:pointer-events-none data-[orientation=vertical]:h-full data-[orientation=vertical]:min-h-44 data-[orientation=horizontal]:w-full data-[orientation=horizontal]:min-w-44 data-[orientation=vertical]:flex-col data-disabled:opacity-64",
          className,
        )}
        data-slot="slider-control"
      >
        <SliderPrimitive.Track
          className="relative grow select-none before:absolute before:rounded-full before:bg-input data-[orientation=horizontal]:h-1 data-[orientation=vertical]:h-full data-[orientation=horizontal]:w-full data-[orientation=vertical]:w-1 data-[orientation=horizontal]:before:inset-x-0.5 data-[orientation=vertical]:before:inset-x-0 data-[orientation=horizontal]:before:inset-y-0 data-[orientation=vertical]:before:inset-y-0.5"
          data-slot="slider-track"
        >
          <SliderPrimitive.Indicator
            className="select-none rounded-full bg-primary data-[orientation=horizontal]:ms-0.5 data-[orientation=vertical]:mb-0.5"
            data-slot="slider-indicator"
          />
          {Array.from({ length: _values.length }, (_, index) => (
            <SliderPrimitive.Thumb
              className="block size-5 shrink-0 select-none rounded-full border border-input bg-white not-dark:bg-clip-padding shadow-xs/5 outline-none transition-[box-shadow,scale] before:absolute before:inset-0 before:rounded-full before:shadow-[0_1px_--theme(--color-black/6%)] focus-visible:ring-[3px] focus-visible:ring-ring/24 has-focus-visible:ring-[3px] has-focus-visible:ring-ring/24 data-dragging:scale-120 data-dragging:ring-[3px] data-dragging:ring-ring/24 sm:size-4 dark:border-background dark:data-dragging:ring-ring/48 dark:focus-visible:ring-ring/48 [:focus-visible,[data-dragging]]:shadow-none"
              data-slot="slider-thumb"
              key={String(index)}
            />
          ))}
        </SliderPrimitive.Track>
      </SliderPrimitive.Control>
    </SliderPrimitive.Root>
  );
}

function SliderValue({ className, ...props }: SliderPrimitive.Value.Props) {
  return (
    <SliderPrimitive.Value
      className={cn("flex justify-end text-sm", className)}
      data-slot="slider-value"
      {...props}
    />
  );
}

export { Slider, SliderValue };
```

## File: `web/src/components/ui/spinner.tsx`
```tsx
import { Loader2Icon } from "lucide-react";
import { cn } from "@/lib/utils";

function Spinner({
  className,
  ...props
}: React.ComponentProps<typeof Loader2Icon>) {
  return (
    <Loader2Icon
      aria-label="Loading"
      className={cn("animate-spin", className)}
      role="status"
      {...props}
    />
  );
}

export { Spinner };
```

## File: `web/src/components/ui/switch.tsx`
```tsx
"use client";

import { Switch as SwitchPrimitive } from "@base-ui/react/switch";

import { cn } from "@/lib/utils";

function Switch({ className, ...props }: SwitchPrimitive.Root.Props) {
  return (
    <SwitchPrimitive.Root
      className={cn(
        "inset-shadow-[0_1px_--theme(--color-black/6%)] inline-flex h-[calc(var(--thumb-size)+2px)] w-[calc(var(--thumb-size)*2-2px)] shrink-0 items-center rounded-full p-px outline-none transition-[background-color,box-shadow] duration-200 [--thumb-size:--spacing(5)] focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-1 focus-visible:ring-offset-background data-checked:bg-primary data-unchecked:bg-input data-disabled:opacity-64 sm:[--thumb-size:--spacing(4)]",
        className,
      )}
      data-slot="switch"
      {...props}
    >
      <SwitchPrimitive.Thumb
        className={cn(
          "pointer-events-none block aspect-square h-full origin-left in-[[role=switch]:active,[data-slot=label]:active]:not-data-disabled:scale-x-110 in-[[role=switch]:active,[data-slot=label]:active]:rounded-[var(--thumb-size)/calc(var(--thumb-size)*1.1)] rounded-(--thumb-size) bg-background shadow-sm/5 will-change-transform [transition:translate_.15s,border-radius_.15s,scale_.1s_.1s,transform-origin_.15s] data-checked:origin-[var(--thumb-size)_50%] data-checked:translate-x-[calc(var(--thumb-size)-4px)]",
        )}
        data-slot="switch-thumb"
      />
    </SwitchPrimitive.Root>
  );
}

export { Switch };
```

## File: `web/src/components/ui/table.tsx`
```tsx
import type * as React from "react";

import { cn } from "@/lib/utils";

function Table({ className, ...props }: React.ComponentProps<"table">) {
  return (
    <div
      className="relative w-full overflow-x-auto"
      data-slot="table-container"
    >
      <table
        className={cn(
          "w-full caption-bottom in-data-[slot=frame]:border-separate in-data-[slot=frame]:border-spacing-0 text-sm",
          className,
        )}
        data-slot="table"
        {...props}
      />
    </div>
  );
}

function TableHeader({ className, ...props }: React.ComponentProps<"thead">) {
  return (
    <thead
      className={cn(
        "[&_tr]:border-b in-data-[slot=frame]:**:[th]:h-9 in-data-[slot=frame]:*:[tr]:border-none in-data-[slot=frame]:*:[tr]:hover:bg-transparent",
        className,
      )}
      data-slot="table-header"
      {...props}
    />
  );
}

function TableBody({ className, ...props }: React.ComponentProps<"tbody">) {
  return (
    <tbody
      className={cn(
        "relative in-data-[slot=frame]:rounded-xl in-data-[slot=frame]:shadow-xs/5 before:pointer-events-none before:absolute before:inset-px not-in-data-[slot=frame]:before:hidden before:rounded-[calc(var(--radius-xl)-1px)] before:shadow-[0_1px_--theme(--color-black/6%)] dark:before:shadow-[0_-1px_--theme(--color-white/8%)] [&_tr:last-child]:border-0 in-data-[slot=frame]:*:[tr]:border-0 in-data-[slot=frame]:*:[tr]:*:[td]:border-b in-data-[slot=frame]:*:[tr]:*:[td]:bg-background in-data-[slot=frame]:*:[tr]:*:[td]:bg-clip-padding in-data-[slot=frame]:*:[tr]:first:*:[td]:first:rounded-ss-xl in-data-[slot=frame]:*:[tr]:*:[td]:first:border-s in-data-[slot=frame]:*:[tr]:first:*:[td]:border-t in-data-[slot=frame]:*:[tr]:last:*:[td]:last:rounded-ee-xl in-data-[slot=frame]:*:[tr]:*:[td]:last:border-e in-data-[slot=frame]:*:[tr]:first:*:[td]:last:rounded-se-xl in-data-[slot=frame]:*:[tr]:last:*:[td]:first:rounded-es-xl in-data-[slot=frame]:*:[tr]:hover:*:[td]:bg-transparent in-data-[slot=frame]:*:[tr]:data-[state=selected]:*:[td]:bg-muted/72",
        className,
      )}
      data-slot="table-body"
      {...props}
    />
  );
}

function TableFooter({ className, ...props }: React.ComponentProps<"tfoot">) {
  return (
    <tfoot
      className={cn(
        "border-t in-data-[slot=frame]:border-none bg-muted/72 in-data-[slot=frame]:bg-transparent font-medium [&>tr]:last:border-b-0 in-data-[slot=frame]:*:[tr]:hover:bg-transparent",
        className,
      )}
      data-slot="table-footer"
      {...props}
    />
  );
}

function TableRow({ className, ...props }: React.ComponentProps<"tr">) {
  return (
    <tr
      className={cn(
        "border-b transition-colors hover:bg-muted/72 in-data-[slot=frame]:hover:bg-transparent data-[state=selected]:bg-muted/72 in-data-[slot=frame]:data-[state=selected]:bg-transparent",
        className,
      )}
      data-slot="table-row"
      {...props}
    />
  );
}

function TableHead({ className, ...props }: React.ComponentProps<"th">) {
  return (
    <th
      className={cn(
        "h-10 whitespace-nowrap px-2.5 text-left align-middle font-medium text-muted-foreground leading-none has-[[role=checkbox]]:w-px has-[[role=checkbox]]:pe-0",
        className,
      )}
      data-slot="table-head"
      {...props}
    />
  );
}

function TableCell({ className, ...props }: React.ComponentProps<"td">) {
  return (
    <td
      className={cn(
        "whitespace-nowrap p-2.5 align-middle leading-none in-data-[slot=frame]:first:p-[calc(--spacing(2.5)-1px)] in-data-[slot=frame]:last:p-[calc(--spacing(2.5)-1px)] has-[[role=checkbox]]:pe-0",
        className,
      )}
      data-slot="table-cell"
      {...props}
    />
  );
}

function TableCaption({
  className,
  ...props
}: React.ComponentProps<"caption">) {
  return (
    <caption
      className={cn(
        "in-data-[slot=frame]:my-4 mt-4 text-muted-foreground text-sm",
        className,
      )}
      data-slot="table-caption"
      {...props}
    />
  );
}

export {
  Table,
  TableHeader,
  TableBody,
  TableFooter,
  TableHead,
  TableRow,
  TableCell,
  TableCaption,
};
```

## File: `web/src/components/ui/tabs.tsx`
```tsx
"use client";

import { Tabs as TabsPrimitive } from "@base-ui/react/tabs";

import { cn } from "@/lib/utils";

type TabsVariant = "default" | "underline";

function Tabs({ className, ...props }: TabsPrimitive.Root.Props) {
  return (
    <TabsPrimitive.Root
      className={cn(
        "flex flex-col gap-2 data-[orientation=vertical]:flex-row",
        className,
      )}
      data-slot="tabs"
      {...props}
    />
  );
}

function TabsList({
  variant = "default",
  className,
  children,
  ...props
}: TabsPrimitive.List.Props & {
  variant?: TabsVariant;
}) {
  return (
    <TabsPrimitive.List
      className={cn(
        "relative z-0 flex w-fit items-center justify-center gap-x-0.5 text-muted-foreground",
        "data-[orientation=vertical]:flex-col",
        variant === "default"
          ? "rounded-lg bg-muted p-0.5 text-muted-foreground/72"
          : "data-[orientation=vertical]:px-1 data-[orientation=horizontal]:py-1 *:data-[slot=tabs-tab]:hover:bg-accent",
        className,
      )}
      data-slot="tabs-list"
      {...props}
    >
      {children}
      <TabsPrimitive.Indicator
        className={cn(
          "-translate-y-(--active-tab-bottom) absolute bottom-0 left-0 h-(--active-tab-height) w-(--active-tab-width) translate-x-(--active-tab-left) transition-[width,translate] duration-200 ease-in-out",
          variant === "underline"
            ? "data-[orientation=vertical]:-translate-x-px z-10 bg-primary data-[orientation=horizontal]:h-0.5 data-[orientation=vertical]:w-0.5 data-[orientation=horizontal]:translate-y-px"
            : "-z-1 rounded-md bg-background shadow-sm/5 dark:bg-input",
        )}
        data-slot="tab-indicator"
      />
    </TabsPrimitive.List>
  );
}

function TabsTab({ className, ...props }: TabsPrimitive.Tab.Props) {
  return (
    <TabsPrimitive.Tab
      className={cn(
        "[&_svg]:-mx-0.5 flex h-9 shrink-0 grow cursor-pointer items-center justify-center gap-1.5 whitespace-nowrap rounded-md border border-transparent px-[calc(--spacing(2.5)-1px)] font-medium text-base outline-none transition-[color,background-color,box-shadow] hover:text-muted-foreground focus-visible:ring-2 focus-visible:ring-ring data-disabled:pointer-events-none data-[orientation=vertical]:w-full data-[orientation=vertical]:justify-start data-active:text-foreground data-disabled:opacity-64 sm:h-8 sm:text-sm [&_svg:not([class*='size-'])]:size-4.5 sm:[&_svg:not([class*='size-'])]:size-4 [&_svg]:pointer-events-none [&_svg]:shrink-0",
        className,
      )}
      data-slot="tabs-tab"
      {...props}
    />
  );
}

function TabsPanel({ className, ...props }: TabsPrimitive.Panel.Props) {
  return (
    <TabsPrimitive.Panel
      className={cn("flex-1 outline-none", className)}
      data-slot="tabs-content"
      {...props}
    />
  );
}

export {
  Tabs,
  TabsList,
  TabsTab,
  TabsTab as TabsTrigger,
  TabsPanel,
  TabsPanel as TabsContent,
};
```

## File: `web/src/components/ui/textarea.tsx`
```tsx
"use client";

import { Field as FieldPrimitive } from "@base-ui/react/field";
import { mergeProps } from "@base-ui/react/merge-props";
import type * as React from "react";

import { cn } from "@/lib/utils";

type TextareaProps = React.ComponentProps<"textarea"> & {
  size?: "sm" | "default" | "lg" | number;
  unstyled?: boolean;
};

function Textarea({
  className,
  size = "default",
  unstyled = false,
  ...props
}: TextareaProps) {
  return (
    <span
      className={
        cn(
          !unstyled &&
            "relative inline-flex w-full rounded-lg border border-input bg-background not-dark:bg-clip-padding text-base shadow-xs/5 ring-ring/24 transition-shadow before:pointer-events-none before:absolute before:inset-0 before:rounded-[calc(var(--radius-lg)-1px)] has-focus-visible:has-aria-invalid:border-destructive/64 has-focus-visible:has-aria-invalid:ring-destructive/16 has-aria-invalid:border-destructive/36 has-focus-visible:border-ring has-disabled:opacity-64 has-[:disabled,:focus-visible,[aria-invalid]]:shadow-none has-focus-visible:ring-[3px] not-has-disabled:has-not-focus-visible:not-has-aria-invalid:before:shadow-[0_1px_--theme(--color-black/6%)] sm:text-sm dark:bg-input/32 dark:has-aria-invalid:ring-destructive/24 dark:not-has-disabled:has-not-focus-visible:not-has-aria-invalid:before:shadow-[0_-1px_--theme(--color-white/6%)]",
          className,
        ) || undefined
      }
      data-size={size}
      data-slot="textarea-control"
    >
      <FieldPrimitive.Control
        render={(defaultProps) => (
          <textarea
            className={cn(
              "field-sizing-content min-h-17.5 w-full rounded-[inherit] px-[calc(--spacing(3)-1px)] py-[calc(--spacing(1.5)-1px)] outline-none max-sm:min-h-20.5",
              size === "sm" &&
                "min-h-16.5 px-[calc(--spacing(2.5)-1px)] py-[calc(--spacing(1)-1px)] max-sm:min-h-19.5",
              size === "lg" &&
                "min-h-18.5 py-[calc(--spacing(2)-1px)] max-sm:min-h-21.5",
            )}
            data-slot="textarea"
            {...mergeProps(defaultProps, props)}
          />
        )}
      />
    </span>
  );
}

export { Textarea, type TextareaProps };
```

## File: `web/src/components/ui/toast.tsx`
```tsx
"use client";

import { Toast } from "@base-ui/react/toast";
import {
  CircleAlertIcon,
  CircleCheckIcon,
  InfoIcon,
  LoaderCircleIcon,
  TriangleAlertIcon,
} from "lucide-react";

import { cn } from "@/lib/utils";
import { buttonVariants } from "@/components/ui/button";

const toastManager = Toast.createToastManager();
const anchoredToastManager = Toast.createToastManager();

const TOAST_ICONS = {
  error: CircleAlertIcon,
  info: InfoIcon,
  loading: LoaderCircleIcon,
  success: CircleCheckIcon,
  warning: TriangleAlertIcon,
} as const;

type ToastPosition =
  | "top-left"
  | "top-center"
  | "top-right"
  | "bottom-left"
  | "bottom-center"
  | "bottom-right";

interface ToastProviderProps extends Toast.Provider.Props {
  position?: ToastPosition;
}

function ToastProvider({
  children,
  position = "bottom-right",
  ...props
}: ToastProviderProps) {
  return (
    <Toast.Provider toastManager={toastManager} {...props}>
      {children}
      <Toasts position={position} />
    </Toast.Provider>
  );
}

function Toasts({ position = "bottom-right" }: { position: ToastPosition }) {
  const { toasts } = Toast.useToastManager();
  const isTop = position.startsWith("top");

  return (
    <Toast.Portal data-slot="toast-portal">
      <Toast.Viewport
        className={cn(
          "fixed z-50 mx-auto flex w-[calc(100%-var(--toast-inset)*2)] max-w-90 [--toast-inset:--spacing(4)] sm:[--toast-inset:--spacing(8)]",
          // Vertical positioning
          "data-[position*=top]:top-(--toast-inset)",
          "data-[position*=bottom]:bottom-(--toast-inset)",
          // Horizontal positioning
          "data-[position*=left]:left-(--toast-inset)",
          "data-[position*=right]:right-(--toast-inset)",
          "data-[position*=center]:-translate-x-1/2 data-[position*=center]:left-1/2",
        )}
        data-position={position}
        data-slot="toast-viewport"
      >
        {toasts.map((toast) => {
          const Icon = toast.type
            ? TOAST_ICONS[toast.type as keyof typeof TOAST_ICONS]
            : null;

          return (
            <Toast.Root
              className={cn(
                "absolute z-[calc(9999-var(--toast-index))] h-(--toast-calc-height) w-full select-none rounded-lg border bg-popover not-dark:bg-clip-padding text-popover-foreground shadow-lg/5 [transition:transform_.5s_cubic-bezier(.22,1,.36,1),opacity_.5s,height_.15s] before:pointer-events-none before:absolute before:inset-0 before:rounded-[calc(var(--radius-lg)-1px)] before:shadow-[0_1px_--theme(--color-black/6%)] dark:before:shadow-[0_-1px_--theme(--color-white/6%)]",
                // Base positioning using data-position
                "data-[position*=right]:right-0 data-[position*=right]:left-auto",
                "data-[position*=left]:right-auto data-[position*=left]:left-0",
                "data-[position*=center]:right-0 data-[position*=center]:left-0",
                "data-[position*=top]:top-0 data-[position*=top]:bottom-auto data-[position*=top]:origin-top",
                "data-[position*=bottom]:top-auto data-[position*=bottom]:bottom-0 data-[position*=bottom]:origin-bottom",
                // Gap fill for hover
                "after:absolute after:left-0 after:h-[calc(var(--toast-gap)+1px)] after:w-full",
                "data-[position*=top]:after:top-full",
                "data-[position*=bottom]:after:bottom-full",
                // Define some variables
                "[--toast-calc-height:var(--toast-frontmost-height,var(--toast-height))] [--toast-gap:--spacing(3)] [--toast-peek:--spacing(3)] [--toast-scale:calc(max(0,1-(var(--toast-index)*.1)))] [--toast-shrink:calc(1-var(--toast-scale))]",
                // Define offset-y variable
                "data-[position*=top]:[--toast-calc-offset-y:calc(var(--toast-offset-y)+var(--toast-index)*var(--toast-gap)+var(--toast-swipe-movement-y))]",
                "data-[position*=bottom]:[--toast-calc-offset-y:calc(var(--toast-offset-y)*-1+var(--toast-index)*var(--toast-gap)*-1+var(--toast-swipe-movement-y))]",
                // Default state transform
                "data-[position*=top]:transform-[translateX(var(--toast-swipe-movement-x))_translateY(calc(var(--toast-swipe-movement-y)+(var(--toast-index)*var(--toast-peek))+(var(--toast-shrink)*var(--toast-calc-height))))_scale(var(--toast-scale))]",
                "data-[position*=bottom]:transform-[translateX(var(--toast-swipe-movement-x))_translateY(calc(var(--toast-swipe-movement-y)-(var(--toast-index)*var(--toast-peek))-(var(--toast-shrink)*var(--toast-calc-height))))_scale(var(--toast-scale))]",
                // Limited state
                "data-limited:opacity-0",
                // Expanded state
                "data-expanded:h-(--toast-height)",
                "data-position:data-expanded:transform-[translateX(var(--toast-swipe-movement-x))_translateY(var(--toast-calc-offset-y))]",
                // Starting and ending animations
                "data-[position*=top]:data-starting-style:transform-[translateY(calc(-100%-var(--toast-inset)))]",
                "data-[position*=bottom]:data-starting-style:transform-[translateY(calc(100%+var(--toast-inset)))]",
                "data-ending-style:opacity-0",
                // Ending animations (direction-aware)
                "data-ending-style:not-data-limited:not-data-swipe-direction:transform-[translateY(calc(100%+var(--toast-inset)))]",
                "data-ending-style:data-[swipe-direction=left]:transform-[translateX(calc(var(--toast-swipe-movement-x)-100%-var(--toast-inset)))_translateY(var(--toast-calc-offset-y))]",
                "data-ending-style:data-[swipe-direction=right]:transform-[translateX(calc(var(--toast-swipe-movement-x)+100%+var(--toast-inset)))_translateY(var(--toast-calc-offset-y))]",
                "data-ending-style:data-[swipe-direction=up]:transform-[translateY(calc(var(--toast-swipe-movement-y)-100%-var(--toast-inset)))]",
                "data-ending-style:data-[swipe-direction=down]:transform-[translateY(calc(var(--toast-swipe-movement-y)+100%+var(--toast-inset)))]",
                // Ending animations (expanded)
                "data-expanded:data-ending-style:data-[swipe-direction=left]:transform-[translateX(calc(var(--toast-swipe-movement-x)-100%-var(--toast-inset)))_translateY(var(--toast-calc-offset-y))]",
                "data-expanded:data-ending-style:data-[swipe-direction=right]:transform-[translateX(calc(var(--toast-swipe-movement-x)+100%+var(--toast-inset)))_translateY(var(--toast-calc-offset-y))]",
                "data-expanded:data-ending-style:data-[swipe-direction=up]:transform-[translateY(calc(var(--toast-swipe-movement-y)-100%-var(--toast-inset)))]",
                "data-expanded:data-ending-style:data-[swipe-direction=down]:transform-[translateY(calc(var(--toast-swipe-movement-y)+100%+var(--toast-inset)))]",
              )}
              data-position={position}
              key={toast.id}
              swipeDirection={
                position.includes("center")
                  ? [isTop ? "up" : "down"]
                  : position.includes("left")
                    ? ["left", isTop ? "up" : "down"]
                    : ["right", isTop ? "up" : "down"]
              }
              toast={toast}
            >
              <Toast.Content className="pointer-events-auto flex items-center justify-between gap-1.5 overflow-hidden px-3.5 py-3 text-sm transition-opacity duration-250 data-behind:pointer-events-none data-behind:opacity-0 data-expanded:opacity-100">
                <div className="flex gap-2">
                  {Icon && (
                    <div
                      className="[&>svg]:h-lh [&>svg]:w-4 [&_svg]:pointer-events-none [&_svg]:shrink-0"
                      data-slot="toast-icon"
                    >
                      <Icon className="in-data-[type=loading]:animate-spin in-data-[type=error]:text-destructive in-data-[type=info]:text-info in-data-[type=success]:text-success in-data-[type=warning]:text-warning in-data-[type=loading]:opacity-80" />
                    </div>
                  )}

                  <div className="flex flex-col gap-0.5">
                    <Toast.Title
                      className="font-medium"
                      data-slot="toast-title"
                    />
                    <Toast.Description
                      className="text-muted-foreground"
                      data-slot="toast-description"
                    />
                  </div>
                </div>
                {toast.actionProps && (
                  <Toast.Action
                    className={buttonVariants({ size: "xs" })}
                    data-slot="toast-action"
                  >
                    {toast.actionProps.children}
                  </Toast.Action>
                )}
              </Toast.Content>
            </Toast.Root>
          );
        })}
      </Toast.Viewport>
    </Toast.Portal>
  );
}

function AnchoredToastProvider({ children, ...props }: Toast.Provider.Props) {
  return (
    <Toast.Provider toastManager={anchoredToastManager} {...props}>
      {children}
      <AnchoredToasts />
    </Toast.Provider>
  );
}

function AnchoredToasts() {
  const { toasts } = Toast.useToastManager();

  return (
    <Toast.Portal data-slot="toast-portal-anchored">
      <Toast.Viewport
        className="outline-none"
        data-slot="toast-viewport-anchored"
      >
        {toasts.map((toast) => {
          const Icon = toast.type
            ? TOAST_ICONS[toast.type as keyof typeof TOAST_ICONS]
            : null;
          const tooltipStyle =
            (toast.data as { tooltipStyle?: boolean })?.tooltipStyle ?? false;
          const positionerProps = toast.positionerProps;

          if (!positionerProps?.anchor) {
            return null;
          }

          return (
            <Toast.Positioner
              className="z-50 max-w-[min(--spacing(64),var(--available-width))]"
              data-slot="toast-positioner"
              key={toast.id}
              sideOffset={positionerProps.sideOffset ?? 4}
              toast={toast}
            >
              <Toast.Root
                className={cn(
                  "relative text-balance border bg-popover not-dark:bg-clip-padding text-popover-foreground text-xs transition-[scale,opacity] before:pointer-events-none before:absolute before:inset-0 before:shadow-[0_1px_--theme(--color-black/6%)] data-ending-style:scale-98 data-starting-style:scale-98 data-ending-style:opacity-0 data-starting-style:opacity-0 dark:before:shadow-[0_-1px_--theme(--color-white/6%)]",
                  tooltipStyle
                    ? "rounded-md shadow-md/5 before:rounded-[calc(var(--radius-md)-1px)]"
                    : "rounded-lg shadow-lg/5 before:rounded-[calc(var(--radius-lg)-1px)]",
                )}
                data-slot="toast-popup"
                toast={toast}
              >
                {tooltipStyle ? (
                  <Toast.Content className="pointer-events-auto px-2 py-1">
                    <Toast.Title data-slot="toast-title" />
                  </Toast.Content>
                ) : (
                  <Toast.Content className="pointer-events-auto flex items-center justify-between gap-1.5 overflow-hidden px-3.5 py-3 text-sm">
                    <div className="flex gap-2">
                      {Icon && (
                        <div
                          className="[&>svg]:h-lh [&>svg]:w-4 [&_svg]:pointer-events-none [&_svg]:shrink-0"
                          data-slot="toast-icon"
                        >
                          <Icon className="in-data-[type=loading]:animate-spin in-data-[type=error]:text-destructive in-data-[type=info]:text-info in-data-[type=success]:text-success in-data-[type=warning]:text-warning in-data-[type=loading]:opacity-80" />
                        </div>
                      )}

                      <div className="flex flex-col gap-0.5">
                        <Toast.Title
                          className="font-medium"
                          data-slot="toast-title"
                        />
                        <Toast.Description
                          className="text-muted-foreground"
                          data-slot="toast-description"
                        />
                      </div>
                    </div>
                    {toast.actionProps && (
                      <Toast.Action
                        className={buttonVariants({ size: "xs" })}
                        data-slot="toast-action"
                      >
                        {toast.actionProps.children}
                      </Toast.Action>
                    )}
                  </Toast.Content>
                )}
              </Toast.Root>
            </Toast.Positioner>
          );
        })}
      </Toast.Viewport>
    </Toast.Portal>
  );
}

export {
  ToastProvider,
  type ToastPosition,
  toastManager,
  AnchoredToastProvider,
  anchoredToastManager,
};
```

## File: `web/src/components/ui/toggle-group.tsx`
```tsx
"use client";

import type { Toggle as TogglePrimitive } from "@base-ui/react/toggle";
import { ToggleGroup as ToggleGroupPrimitive } from "@base-ui/react/toggle-group";
import type { VariantProps } from "class-variance-authority";
import * as React from "react";

import { cn } from "@/lib/utils";
import { Separator } from "@/components/ui/separator";
import {
  Toggle as ToggleComponent,
  type toggleVariants,
} from "@/components/ui/toggle";

const ToggleGroupContext = React.createContext<
  VariantProps<typeof toggleVariants>
>({
  size: "default",
  variant: "default",
});

function ToggleGroup({
  className,
  variant = "default",
  size = "default",
  orientation = "horizontal",
  children,
  ...props
}: ToggleGroupPrimitive.Props & VariantProps<typeof toggleVariants>) {
  return (
    <ToggleGroupPrimitive
      className={cn(
        "flex w-fit *:focus-visible:z-10 dark:*:[[data-slot=separator]:has(+[data-slot=toggle]:hover)]:before:bg-input/64 dark:*:[[data-slot=separator]:has(+[data-slot=toggle][data-pressed])]:before:bg-input dark:*:[[data-slot=toggle]:hover+[data-slot=separator]]:before:bg-input/64 dark:*:[[data-slot=toggle][data-pressed]+[data-slot=separator]]:before:bg-input",
        orientation === "horizontal"
          ? "*:pointer-coarse:after:min-w-auto"
          : "*:pointer-coarse:after:min-h-auto",
        variant === "default"
          ? "gap-0.5"
          : orientation === "horizontal"
            ? "*:not-first:not-data-[slot=separator]:before:-start-[0.5px] *:not-last:not-data-[slot=separator]:before:-end-[0.5px] *:not-first:rounded-s-none *:not-last:rounded-e-none *:not-first:border-s-0 *:not-last:border-e-0 *:not-first:before:rounded-s-none *:not-last:before:rounded-e-none"
            : "*:not-first:not-data-[slot=separator]:before:-top-[0.5px] *:not-last:not-data-[slot=separator]:before:-bottom-[0.5px] flex-col *:not-first:rounded-t-none *:not-last:rounded-b-none *:not-first:border-t-0 *:not-last:border-b-0 *:not-first:before:rounded-t-none *:not-last:before:rounded-b-none *:data-[slot=toggle]:not-last:before:hidden dark:*:last:before:hidden dark:*:first:before:block",
        className,
      )}
      data-size={size}
      data-slot="toggle-group"
      data-variant={variant}
      orientation={orientation}
      {...props}
    >
      <ToggleGroupContext.Provider value={{ size, variant }}>
        {children}
      </ToggleGroupContext.Provider>
    </ToggleGroupPrimitive>
  );
}

function Toggle({
  className,
  children,
  variant,
  size,
  ...props
}: TogglePrimitive.Props & VariantProps<typeof toggleVariants>) {
  const context = React.useContext(ToggleGroupContext);

  const resolvedVariant = context.variant || variant;
  const resolvedSize = context.size || size;

  return (
    <ToggleComponent
      className={className}
      data-size={resolvedSize}
      data-variant={resolvedVariant}
      size={resolvedSize}
      variant={resolvedVariant}
      {...props}
    >
      {children}
    </ToggleComponent>
  );
}

function ToggleGroupSeparator({
  className,
  orientation = "vertical",
  ...props
}: {
  className?: string;
} & React.ComponentProps<typeof Separator>) {
  return (
    <Separator
      className={cn(
        "pointer-events-none relative before:absolute before:inset-0 dark:before:bg-input/32",
        className,
      )}
      orientation={orientation}
      {...props}
    />
  );
}

export { ToggleGroup, Toggle, Toggle as ToggleGroupItem, ToggleGroupSeparator };
```

## File: `web/src/components/ui/toggle.tsx`
```tsx
"use client";

import { Toggle as TogglePrimitive } from "@base-ui/react/toggle";
import { cva, type VariantProps } from "class-variance-authority";

import { cn } from "@/lib/utils";

const toggleVariants = cva(
  "[&_svg]:-mx-0.5 relative inline-flex shrink-0 cursor-pointer select-none items-center justify-center gap-2 whitespace-nowrap rounded-lg border font-medium text-base outline-none transition-shadow before:pointer-events-none before:absolute before:inset-0 before:rounded-[calc(var(--radius-lg)-1px)] pointer-coarse:after:absolute pointer-coarse:after:size-full pointer-coarse:after:min-h-11 pointer-coarse:after:min-w-11 hover:bg-accent focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-1 focus-visible:ring-offset-background disabled:pointer-events-none disabled:opacity-64 data-pressed:bg-input/64 data-pressed:text-accent-foreground sm:text-sm [&_svg:not([class*='opacity-'])]:opacity-80 [&_svg:not([class*='size-'])]:size-4.5 sm:[&_svg:not([class*='size-'])]:size-4 [&_svg]:pointer-events-none [&_svg]:shrink-0",
  {
    defaultVariants: {
      size: "default",
      variant: "default",
    },
    variants: {
      size: {
        default: "h-9 min-w-9 px-[calc(--spacing(2)-1px)] sm:h-8 sm:min-w-8",
        lg: "h-10 min-w-10 px-[calc(--spacing(2.5)-1px)] sm:h-9 sm:min-w-9",
        sm: "h-8 min-w-8 px-[calc(--spacing(1.5)-1px)] sm:h-7 sm:min-w-7",
      },
      variant: {
        default: "border-transparent",
        outline:
          "border-input bg-background not-dark:bg-clip-padding shadow-xs/5 not-disabled:not-active:not-data-pressed:before:shadow-[0_1px_--theme(--color-black/6%)] dark:bg-input/32 dark:data-pressed:bg-input dark:hover:bg-input/64 dark:not-disabled:not-active:not-data-pressed:before:shadow-[0_-1px_--theme(--color-white/6%)] dark:not-disabled:not-data-pressed:before:shadow-[0_-1px_--theme(--color-white/2%)] [:disabled,:active,[data-pressed]]:shadow-none",
      },
    },
  },
);

function Toggle({
  className,
  variant,
  size,
  ...props
}: TogglePrimitive.Props & VariantProps<typeof toggleVariants>) {
  return (
    <TogglePrimitive
      className={cn(toggleVariants({ className, size, variant }))}
      data-slot="toggle"
      {...props}
    />
  );
}

export { Toggle, toggleVariants };
```

## File: `web/src/components/ui/toolbar.tsx`
```tsx
"use client";

import { Toolbar as ToolbarPrimitive } from "@base-ui/react/toolbar";

import { cn } from "@/lib/utils";

function Toolbar({ className, ...props }: ToolbarPrimitive.Root.Props) {
  return (
    <ToolbarPrimitive.Root
      className={cn(
        "relative flex gap-2 rounded-xl border bg-card not-dark:bg-clip-padding p-1 text-card-foreground",
        className,
      )}
      data-slot="toolbar"
      {...props}
    />
  );
}

function ToolbarButton({ className, ...props }: ToolbarPrimitive.Button.Props) {
  return (
    <ToolbarPrimitive.Button
      className={cn(className)}
      data-slot="toolbar-button"
      {...props}
    />
  );
}

function ToolbarLink({ className, ...props }: ToolbarPrimitive.Link.Props) {
  return (
    <ToolbarPrimitive.Link
      className={cn(className)}
      data-slot="toolbar-link"
      {...props}
    />
  );
}

function ToolbarInput({ className, ...props }: ToolbarPrimitive.Input.Props) {
  return (
    <ToolbarPrimitive.Input
      className={cn(className)}
      data-slot="toolbar-input"
      {...props}
    />
  );
}

function ToolbarGroup({ className, ...props }: ToolbarPrimitive.Group.Props) {
  return (
    <ToolbarPrimitive.Group
      className={cn("flex items-center gap-1", className)}
      data-slot="toolbar-group"
      {...props}
    />
  );
}

function ToolbarSeparator({
  className,
  ...props
}: ToolbarPrimitive.Separator.Props) {
  return (
    <ToolbarPrimitive.Separator
      className={cn(
        "shrink-0 bg-border data-[orientation=horizontal]:my-0.5 data-[orientation=vertical]:my-1.5 data-[orientation=horizontal]:h-px data-[orientation=horizontal]:w-full data-[orientation=vertical]:w-px data-[orientation=vertical]:not-[[class^='h-']]:not-[[class*='_h-']]:self-stretch",
        className,
      )}
      data-slot="toolbar-separator"
      {...props}
    />
  );
}

export {
  Toolbar,
  ToolbarGroup,
  ToolbarSeparator,
  ToolbarButton,
  ToolbarLink,
  ToolbarInput,
};
```

## File: `web/src/components/ui/tooltip.tsx`
```tsx
"use client";

import { Tooltip as TooltipPrimitive } from "@base-ui/react/tooltip";

import { cn } from "@/lib/utils";

const TooltipCreateHandle = TooltipPrimitive.createHandle;

const TooltipProvider = TooltipPrimitive.Provider;

const Tooltip = TooltipPrimitive.Root;

function TooltipTrigger(props: TooltipPrimitive.Trigger.Props) {
  return <TooltipPrimitive.Trigger data-slot="tooltip-trigger" {...props} />;
}

function TooltipPopup({
  className,
  align = "center",
  sideOffset = 4,
  side = "top",
  children,
  ...props
}: TooltipPrimitive.Popup.Props & {
  align?: TooltipPrimitive.Positioner.Props["align"];
  side?: TooltipPrimitive.Positioner.Props["side"];
  sideOffset?: TooltipPrimitive.Positioner.Props["sideOffset"];
}) {
  return (
    <TooltipPrimitive.Portal>
      <TooltipPrimitive.Positioner
        align={align}
        className="z-50 h-(--positioner-height) w-(--positioner-width) max-w-(--available-width) transition-[top,left,right,bottom,transform] data-instant:transition-none"
        data-slot="tooltip-positioner"
        side={side}
        sideOffset={sideOffset}
      >
        <TooltipPrimitive.Popup
          className={cn(
            "relative flex h-(--popup-height,auto) w-(--popup-width,auto) origin-(--transform-origin) text-balance rounded-md border bg-popover not-dark:bg-clip-padding text-popover-foreground text-xs shadow-md/5 transition-[width,height,scale,opacity] before:pointer-events-none before:absolute before:inset-0 before:rounded-[calc(var(--radius-md)-1px)] before:shadow-[0_1px_--theme(--color-black/6%)] data-ending-style:scale-98 data-starting-style:scale-98 data-ending-style:opacity-0 data-starting-style:opacity-0 data-instant:duration-0 dark:before:shadow-[0_-1px_--theme(--color-white/6%)]",
            className,
          )}
          data-slot="tooltip-popup"
          {...props}
        >
          <TooltipPrimitive.Viewport
            className="relative size-full overflow-clip px-(--viewport-inline-padding) py-1 [--viewport-inline-padding:--spacing(2)] data-instant:transition-none **:data-current:data-ending-style:opacity-0 **:data-current:data-starting-style:opacity-0 **:data-previous:data-ending-style:opacity-0 **:data-previous:data-starting-style:opacity-0 **:data-current:w-[calc(var(--popup-width)-2*var(--viewport-inline-padding)-2px)] **:data-previous:w-[calc(var(--popup-width)-2*var(--viewport-inline-padding)-2px)] **:data-previous:truncate **:data-current:opacity-100 **:data-previous:opacity-100 **:data-current:transition-opacity **:data-previous:transition-opacity"
            data-slot="tooltip-viewport"
          >
            {children}
          </TooltipPrimitive.Viewport>
        </TooltipPrimitive.Popup>
      </TooltipPrimitive.Positioner>
    </TooltipPrimitive.Portal>
  );
}

export {
  TooltipCreateHandle,
  TooltipProvider,
  Tooltip,
  TooltipTrigger,
  TooltipPopup,
  TooltipPopup as TooltipContent,
};
```

## File: `web/src/hooks/use-mobile.ts`
```typescript
import * as React from "react";

const MOBILE_BREAKPOINT = 768;

export function useIsMobile() {
  const [isMobile, setIsMobile] = React.useState<boolean | undefined>(
    undefined,
  );

  React.useEffect(() => {
    const mql = window.matchMedia(`(max-width: ${MOBILE_BREAKPOINT - 1}px)`);
    const onChange = () => {
      setIsMobile(window.innerWidth < MOBILE_BREAKPOINT);
    };
    mql.addEventListener("change", onChange);
    setIsMobile(window.innerWidth < MOBILE_BREAKPOINT);
    return () => mql.removeEventListener("change", onChange);
  }, []);

  return !!isMobile;
}
```

## File: `web/src/lib/docs-config.ts`
```typescript
export const docsConfig = {
    mainNav: [
        {
            title: "Documentation",
            href: "/docs",
        },
        {
            title: "Agents",
            href: "/brain/knowledge/docs_legacy/agents",
        },
        {
            title: "Skills",
            href: "/brain/knowledge/docs_legacy/skills",
        },
        {
            title: "Workflows",
            href: "/brain/knowledge/docs_legacy/workflows",
        },
    ],
    sidebarNav: [
        {
            title: "Getting Started",
            items: [
                {
                    title: "Introduction",
                    href: "/docs",
                },
                {
                    title: "Installation",
                    href: "/brain/knowledge/docs_legacy/getting-started/installation",
                },
                {
                    title: "Quick Start",
                    href: "/brain/knowledge/docs_legacy/getting-started/quick-start",
                },
            ],
        },
        {
            title: "Guides & Examples",
            items: [
                {
                    title: "Structured Brainstorming",
                    href: "/brain/knowledge/docs_legacy/guide/examples/brainstorm",
                },
                {
                    title: "Project Planning",
                    href: "/brain/knowledge/docs_legacy/guide/examples/plan",
                },
                {
                    title: "Create New Application",
                    href: "/brain/knowledge/docs_legacy/guide/examples/create",
                },
                {
                    title: "Add a New Feature",
                    href: "/brain/knowledge/docs_legacy/guide/examples/new-feature",
                },
                {
                    title: "Advanced UI Design",
                    href: "/brain/knowledge/docs_legacy/guide/examples/ui-design",
                },
                {
                    title: "Systematic Debugging",
                    href: "/brain/knowledge/docs_legacy/guide/examples/debugging",
                },
                {
                    title: "Test Generation",
                    href: "/brain/knowledge/docs_legacy/guide/examples/test",
                },
                {
                    title: "Preview Management",
                    href: "/brain/knowledge/docs_legacy/guide/examples/preview",
                },
                {
                    title: "Project Status",
                    href: "/brain/knowledge/docs_legacy/guide/examples/status",
                },
                {
                    title: "Multi-Agent Orchestration",
                    href: "/brain/knowledge/docs_legacy/guide/examples/orchestration",
                },
                {
                    title: "Production Deployment",
                    href: "/brain/knowledge/docs_legacy/guide/examples/deployment",
                },
            ],
        },
        {
            title: "Agents",
            items: [
                {
                    title: "Overview",
                    href: "/brain/knowledge/docs_legacy/agents",
                },
                {
                    title: "Orchestrator",
                    href: "/brain/knowledge/docs_legacy/agents/orchestrator",
                },
                {
                    title: "Project Planner",
                    href: "/brain/knowledge/docs_legacy/agents/project-planner",
                },
                {
                    title: "Frontend Specialist",
                    href: "/brain/knowledge/docs_legacy/agents/frontend-specialist",
                },
                {
                    title: "Backend Specialist",
                    href: "/brain/knowledge/docs_legacy/agents/backend-specialist",
                },
                {
                    title: "Mobile Developer",
                    href: "/brain/knowledge/docs_legacy/agents/mobile-developer",
                },
                {
                    title: "Security Auditor",
                    href: "/brain/knowledge/docs_legacy/agents/security-auditor",
                },
                {
                    title: "Debugger",
                    href: "/brain/knowledge/docs_legacy/agents/debugger",
                },
                {
                    title: "Game Developer",
                    href: "/brain/knowledge/docs_legacy/agents/game-developer",
                },
            ],
        },
        {
            title: "Skills",
            items: [
                {
                    title: "Overview",
                    href: "/brain/knowledge/docs_legacy/skills",
                },
                {
                    title: "Clean Code",
                    href: "/brain/knowledge/docs_legacy/skills/clean-code",
                },
                {
                    title: "React Patterns",
                    href: "/brain/knowledge/docs_legacy/skills/react-patterns",
                },
                {
                    title: "Next.js Best Practices",
                    href: "/brain/knowledge/docs_legacy/skills/nextjs-best-practices",
                },
                {
                    title: "Tailwind Patterns",
                    href: "/brain/knowledge/docs_legacy/skills/tailwind-patterns",
                },
                {
                    title: "Frontend Design",
                    href: "/brain/knowledge/docs_legacy/skills/frontend-design",
                },
                {
                    title: "Mobile Design",
                    href: "/brain/knowledge/docs_legacy/skills/mobile-design",
                },
            ],
        },
        {
            title: "Workflows",
            items: [
                {
                    title: "Overview",
                    href: "/brain/knowledge/docs_legacy/workflows",
                },
                {
                    title: "/brainstorm",
                    href: "/brain/knowledge/docs_legacy/workflows/brainstorm",
                },
                {
                    title: "/create",
                    href: "/brain/knowledge/docs_legacy/workflows/create",
                },
                {
                    title: "/debug",
                    href: "/brain/knowledge/docs_legacy/workflows/debug",
                },
                {
                    title: "/deploy",
                    href: "/brain/knowledge/docs_legacy/workflows/deploy",
                },
            ],
        },
    ],
};
```

## File: `web/src/lib/utils.ts`
```typescript
import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
```

## File: `web/src/services/agents.json`
```json
[
    {
        "name": "orchestrator",
        "description": "Multi-agent coordination",
        "skills": [
            "parallel-agents",
            "behavioral-modes"
        ]
    },
    {
        "name": "project-planner",
        "description": "Discovery, task planning",
        "skills": [
            "brainstorming",
            "plan-writing",
            "architecture"
        ]
    },
    {
        "name": "frontend-specialist",
        "description": "Web UI/UX",
        "skills": [
            "frontend-design",
            "react-best-practices",
            "tailwind-patterns",
            "web-design-guidelines"
        ]
    },
    {
        "name": "backend-specialist",
        "description": "API, business logic",
        "skills": [
            "api-patterns",
            "nodejs-best-practices",
            "database-design"
        ]
    },
    {
        "name": "database-architect",
        "description": "Schema, SQL",
        "skills": [
            "database-design",
            "prisma-expert"
        ]
    },
    {
        "name": "mobile-developer",
        "description": "iOS, Android, RN",
        "skills": [
            "mobile-design"
        ]
    },
    {
        "name": "game-developer",
        "description": "Game logic, mechanics",
        "skills": [
            "game-development"
        ]
    },
    {
        "name": "devops-engineer",
        "description": "CI/CD, Docker",
        "skills": [
            "deployment-procedures",
            "docker-expert"
        ]
    },
    {
        "name": "security-auditor",
        "description": "Security compliance",
        "skills": [
            "vulnerability-scanner",
            "red-team-tactics"
        ]
    },
    {
        "name": "penetration-tester",
        "description": "Offensive security",
        "skills": [
            "red-team-tactics"
        ]
    },
    {
        "name": "test-engineer",
        "description": "Testing strategies",
        "skills": [
            "testing-patterns",
            "tdd-workflow",
            "webapp-testing"
        ]
    },
    {
        "name": "debugger",
        "description": "Root cause analysis",
        "skills": [
            "systematic-debugging"
        ]
    },
    {
        "name": "performance-optimizer",
        "description": "Speed, Web Vitals",
        "skills": [
            "performance-profiling"
        ]
    },
    {
        "name": "seo-specialist",
        "description": "Ranking, visibility",
        "skills": [
            "seo-fundamentals",
            "geo-fundamentals"
        ]
    },
    {
        "name": "documentation-writer",
        "description": "Manuals, docs",
        "skills": [
            "documentation-templates"
        ]
    },
    {
        "name": "product-manager",
        "description": "Requirements, user stories",
        "skills": [
            "plan-writing",
            "brainstorming"
        ]
    },
    {
        "name": "product-owner",
        "description": "Strategy, backlog, MVP",
        "skills": [
            "plan-writing",
            "brainstorming"
        ]
    },
    {
        "name": "qa-automation-engineer",
        "description": "E2E testing, CI pipelines",
        "skills": [
            "webapp-testing",
            "testing-patterns"
        ]
    },
    {
        "name": "code-archaeologist",
        "description": "Legacy code, refactoring",
        "skills": [
            "clean-code",
            "code-review-checklist"
        ]
    },
    {
        "name": "explorer-agent",
        "description": "Codebase analysis",
        "skills": []
    }
]
```

## File: `web/src/services/skills.json`
```json
[
    {
        "name": "react-best-practices",
        "description": "Next.js App Router, React hooks, Server Components, performance",
        "category": "Frontend & UI"
    },
    {
        "name": "tailwind-patterns",
        "description": "Tailwind CSS v4 utilities",
        "category": "Frontend & UI"
    },
    {
        "name": "frontend-design",
        "description": "UI/UX patterns, design systems",
        "category": "Frontend & UI"
    },
    {
        "name": "web-design-guidelines",
        "description": "Professional web design standards, 50 styles, 21 palettes",
        "category": "Frontend & UI"
    },
    {
        "name": "api-patterns",
        "description": "REST, GraphQL, tRPC",
        "category": "Backend & API"
    },
    {
        "name": "nodejs-best-practices",
        "description": "Node.js async, modules",
        "category": "Backend & API"
    },
    {
        "name": "python-patterns",
        "description": "Python standards, FastAPI",
        "category": "Backend & API"
    },
    {
        "name": "database-design",
        "description": "Schema design, optimization",
        "category": "Database"
    },
    {
        "name": "deployment-procedures",
        "description": "CI/CD, deploy workflows",
        "category": "Cloud & Infrastructure"
    },
    {
        "name": "server-management",
        "description": "Infrastructure management",
        "category": "Cloud & Infrastructure"
    },
    {
        "name": "testing-patterns",
        "description": "Jest, Vitest, strategies",
        "category": "Testing & Quality"
    },
    {
        "name": "webapp-testing",
        "description": "E2E, Playwright",
        "category": "Testing & Quality"
    },
    {
        "name": "tdd-workflow",
        "description": "Test-driven development",
        "category": "Testing & Quality"
    },
    {
        "name": "code-review-checklist",
        "description": "Code review standards",
        "category": "Testing & Quality"
    },
    {
        "name": "lint-and-validate",
        "description": "Linting, validation",
        "category": "Testing & Quality"
    },
    {
        "name": "vulnerability-scanner",
        "description": "Security auditing, OWASP",
        "category": "Security"
    },
    {
        "name": "red-team-tactics",
        "description": "Offensive security",
        "category": "Security"
    },
    {
        "name": "app-builder",
        "description": "Full-stack app scaffolding",
        "category": "Architecture & Planning"
    },
    {
        "name": "architecture",
        "description": "System design patterns",
        "category": "Architecture & Planning"
    },
    {
        "name": "plan-writing",
        "description": "Task planning, breakdown",
        "category": "Architecture & Planning"
    },
    {
        "name": "brainstorming",
        "description": "Socratic questioning",
        "category": "Architecture & Planning"
    },
    {
        "name": "mobile-design",
        "description": "Mobile UI/UX patterns",
        "category": "Mobile"
    },
    {
        "name": "game-development",
        "description": "Game logic, mechanics",
        "category": "Game Development"
    },
    {
        "name": "seo-fundamentals",
        "description": "SEO, E-E-A-T, Core Web Vitals",
        "category": "SEO & Growth"
    },
    {
        "name": "geo-fundamentals",
        "description": "GenAI optimization",
        "category": "SEO & Growth"
    },
    {
        "name": "bash-linux",
        "description": "Linux commands, scripting",
        "category": "Shell/CLI"
    },
    {
        "name": "powershell-windows",
        "description": "Windows PowerShell",
        "category": "Shell/CLI"
    },
    {
        "name": "clean-code",
        "description": "Coding standards (Global)",
        "category": "Other"
    },
    {
        "name": "behavioral-modes",
        "description": "Agent personas",
        "category": "Other"
    },
    {
        "name": "parallel-agents",
        "description": "Multi-agent patterns",
        "category": "Other"
    },
    {
        "name": "mcp-builder",
        "description": "Model Context Protocol",
        "category": "Other"
    },
    {
        "name": "documentation-templates",
        "description": "Doc formats",
        "category": "Other"
    },
    {
        "name": "i18n-localization",
        "description": "Internationalization",
        "category": "Other"
    },
    {
        "name": "performance-profiling",
        "description": "Web Vitals, optimization",
        "category": "Other"
    },
    {
        "name": "systematic-debugging",
        "description": "Troubleshooting",
        "category": "Other"
    },
    {
        "name": "intelligent-routing",
        "description": "Automatic agent selection and routing",
        "category": "Other"
    },
    {
        "name": "rust-pro",
        "description": "Master Rust 1.75+ with modern async patterns, advanced type system features, and production-ready systems programming.",
        "category": "Backend & API"
    }
]
```

## File: `web/src/services/workflows.json`
```json
[
    {
        "command": "/brainstorm",
        "description": "Socratic discovery"
    },
    {
        "command": "/create",
        "description": "Create new features"
    },
    {
        "command": "/debug",
        "description": "Debug issues"
    },
    {
        "command": "/deploy",
        "description": "Deploy application"
    },
    {
        "command": "/enhance",
        "description": "Improve existing code"
    },
    {
        "command": "/orchestrate",
        "description": "Multi-agent coordination"
    },
    {
        "command": "/plan",
        "description": "Task breakdown"
    },
    {
        "command": "/preview",
        "description": "Preview changes"
    },
    {
        "command": "/status",
        "description": "Check project status"
    },
    {
        "command": "/test",
        "description": "Run tests"
    },
    {
        "command": "/ui-ux-pro-max",
        "description": "Design with 50 styles"
    }
]
```

