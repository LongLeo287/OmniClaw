---
id: bmad-code-org-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:58.405690
---

# KNOWLEDGE EXTRACT: bmad-code-org
> **Extracted on:** 2026-03-30 17:31:06
> **Source:** bmad-code-org

---

## File: `bmad-method-test-architecture-enterprise.md`
```markdown
# 📦 bmad-code-org/bmad-method-test-architecture-enterprise [🔖 PENDING/APPROVE]
🔗 https://github.com/bmad-code-org/bmad-method-test-architecture-enterprise


## Meta
- **Stars:** ⭐ 39 | **Forks:** 🍴 10
- **Language:** JavaScript | **License:** NOASSERTION
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Test Architect Full BMad Method Enhancement

## README (trích đầu)
```
# Test Architect (TEA)

TEA (Test Engineering Architect) is a standalone BMAD module that delivers risk-based test strategy, test automation guidance, and release gate decisions. It provides a single expert agent (Murat, Master Test Architect and Quality Advisor) and nine workflows spanning Teach Me Testing (TEA Academy), framework setup, test design, ATDD, automation, traceability, NFR assessment, CI guidance, and test review.

Docs: <https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/>

## Why TEA

- Risk-based testing with measurable quality gates
- Consistent, knowledge-base driven outputs
- Clear prioritization (P0-P3) and traceability
- Optional Playwright Utils, CLI, and MCP browser automation

## How BMad Works

BMad works because it turns big, fuzzy work into **repeatable workflows**. Each workflow is broken into small steps with clear instructions, so the AI follows the same path every time. It also uses a **shared knowledge base** (standards and patterns) so outputs are consistent, not random. In short: **structured steps + shared standards = reliable results**.

## How TEA Fits In

TEA plugs into BMad the same way a specialist plugs into a team. It uses the same step‑by‑step workflow engine and shared standards, but focuses exclusively on testing and quality gates. That means you get a **risk‑based test plan**, **automation guidance**, and **go/no‑go decisions** that align with the rest of the BMad process.

## Architecture & Flow

BMad is a small **agent + workflow engine**. There is no external orchestrator — everything runs inside the LLM context window through structured instructions.

### Building Blocks

Each workflow directory contains these files, and each has a specific job:

| File              | What it does                                                                                                        | When it loads                                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `SKILL.md`        | Expert persona — identity, principles, critical actions, capabilities table                                         | First — always in context                                                 |
| `workflow.yaml`   | Machine-readable metadata — config variables, required tools, tags                                                  | Second — resolves `{project-root}`, `{config_source}`, `{test_artifacts}` |
| `workflow.md`     | Human-readable entry point — goals, mode menu (Create/Edit/Validate), routes to first step                          | Second — presents mode choice                                             |
| `instructions.md` | Workflow-specific rules and context (optional, supplements workflow.md)                                             | On demand                       
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `BMAD-METHOD.md`
```markdown
# 📦 bmad-code-org/BMAD-METHOD [⭐ ACTIVE]
🔗 https://github.com/bmad-code-org/BMAD-METHOD


## Meta
- **Stars:** ⭐ 42480 | **Forks:** 🍴 5108
- **Language:** JavaScript | **License:** NOASSERTION
- **Last updated:** 2026-03-27
- **Topics:** (none)
- **Status trong AI OS:** ⭐ ACTIVE

## Description:
Breakthrough Method for Agile Ai Driven Development

## README (FULL)
```
![BMad Method](banner-bmad-method.png)

[![Version](https://img.shields.io/npm/v/bmad-method?color=blue&label=version)](https://www.npmjs.com/package/bmad-method)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Node.js Version](https://img.shields.io/badge/node-%3E%3D20.0.0-brightgreen)](https://nodejs.org)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-7289da?logo=discord&logoColor=white)](https://discord.gg/gk8jAdXWmj)

**Build More Architect Dreams** — An AI-driven agile development module for the BMad Method Module Ecosystem, the best and most comprehensive Agile AI Driven Development framework that has true scale-adaptive intelligence that adjusts from bug fixes to enterprise systems.

**100% free and open source.** No paywalls. No gated content. No gated Discord. We believe in empowering everyone, not just those who can pay for a gated community or courses.

## Why the BMad Method?

Traditional AI tools do the thinking for you, producing average results. BMad agents and facilitated workflows act as expert collaborators who guide you through a structured process to bring out your best thinking in partnership with the AI.

- **AI Intelligent Help** — Invoke the `bmad-help` skill anytime for guidance on what's next
- **Scale-Domain-Adaptive** — Automatically adjusts planning depth based on project complexity
- **Structured Workflows** — Grounded in agile best practices across analysis, planning, architecture, and implementation
- **Specialized Agents** — 12+ domain experts (PM, Architect, Developer, UX, Scrum Master, and more)
- **Party Mode** — Bring multiple agent personas into one session to collaborate and discuss
- **Complete Lifecycle** — From brainstorming to deployment

[Learn more at **docs.bmad-method.org**](https://docs.bmad-method.org)

---

## 🚀 What's Next for BMad?

**V6 is here and we're just getting started!** The BMad Method is evolving rapidly with optimizations including Cross Platform Agent Team and Sub Agent inclusion, Skills Architecture, BMad Builder v1, Dev Loop Automation, and so much more in the works.

**[📍 Check out the complete Roadmap →](https://docs.bmad-method.org/roadmap/)**

---

## Quick Start

**Prerequisites**: [Node.js](https://nodejs.org) v20+

```bash
npx bmad-method install
```

> Want the newest prerelease build? Use `npx bmad-method@next install`. Expect higher churn than the default install.

Follow the installer prompts, then open your AI IDE (Claude Code, Cursor, etc.) in your project folder.

**Non-Interactive Installation** (for CI/CD):

```bash
npx bmad-method install --directory /path/to/project --modules bmm --tools claude-code --yes
```

[See all installation options](https://docs.bmad-method.org/how-to/non-interactive-installation/)

> **Not sure what to do?** Ask `bmad-help` — it tells you exactly what's next and what's optional. You can also ask questions like `bmad-help I just finished the architecture, what do I do next?`

## Modules

BMad Method extends with official modules for specialized domains. Available during installation or anytime after.

| Module                                                                                                            | Purpose                                           |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| **[BMad Method (BMM)](https://github.com/bmad-code-org/BMAD-METHOD)**                                             | Core framework with 34+ workflows                 |
| **[BMad Builder (BMB)](https://github.com/bmad-code-org/bmad-builder)**                                           | Create custom BMad agents and workflows           |
| **[Test Architect (TEA)](https://github.com/bmad-code-org/bmad-method-test-architecture-enterprise)**             | Risk-based test strategy and automation           |
| **[Game Dev Studio (BMGD)](https://github.com/bmad-code-org/bmad-module-game-dev-studio)**                        | Game development workflows (Unity, Unreal, Godot) |
| **[Creative Intelligence Suite (CIS)](https://github.com/bmad-code-org/bmad-module-creative-intelligence-suite)** | Innovation, brainstorming, design thinking        |

## Documentation

[BMad Method Docs Site](https://docs.bmad-method.org) — Tutorials, guides, concepts, and reference

**Quick links:**
- [Getting Started Tutorial](https://docs.bmad-method.org/tutorials/getting-started/)
- [Upgrading from Previous Versions](https://docs.bmad-method.org/how-to/upgrade-to-v6/)
- [Test Architect Documentation](https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/)


## Community

- [Discord](https://discord.gg/gk8jAdXWmj) — Get help, share ideas, collaborate
- [Subscribe on YouTube](https://www.youtube.com/@BMadCode) — Tutorials, master class, and podcast (launching Feb 2025)
- [GitHub Issues](https://github.com/bmad-code-org/BMAD-METHOD/issues) — Bug reports and feature requests
- [Discussions](https://github.com/bmad-code-org/BMAD-METHOD/discussions) — Community conversations

## Support BMad

BMad is free for everyone — and always will be. If you'd like to support development:

- ⭐ Please click the star project icon near the top right of this page
- ☕ [Buy Me a Coffee](https://buymeacoffee.com/bmad) — Fuel the development
- 🏢 Corporate sponsorship — DM on Discord
- 🎤 Speaking & Media — Available for conferences, podcasts, interviews (BM on Discord)

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License — see [LICENSE](LICENSE) for details.

---

**BMad** and **BMAD-METHOD** are trademarks of BMad Code, LLC. See [TRADEMARK.md](TRADEMARK.md) for details.

[![Contributors](https://contrib.rocks/image?repo=bmad-code-org/BMAD-METHOD)](https://github.com/bmad-code-org/BMAD-METHOD/graphs/contributors)

See [CONTRIBUTORS.md](CONTRIBUTORS.md) for contributor information.

```

---
*Ingested: 2026-03-27 | Source: GitHub API FULL | Owner: Dept 07 Knowledge*
```

## File: `bmad-module-creative-intelligence-suite.md`
```markdown
# 📦 bmad-code-org/bmad-module-creative-intelligence-suite [🔖 PENDING/APPROVE]
🔗 https://github.com/bmad-code-org/bmad-module-creative-intelligence-suite


## Meta
- **Stars:** ⭐ 48 | **Forks:** 🍴 9
- **Language:** JavaScript | **License:** NOASSERTION
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A BMad Method Compliant stand along module that has agents and workflows to help bring out the creativity of the user through various exercises and disciplines. More will come over time - this was meant as a bmad module tech demo

## README (trích đầu)
```
# Creative Intelligence Suite

[![Version](https://img.shields.io/npm/v/bmad-creative-intelligence-suite?color=blue&label=version)](https://www.npmjs.com/package/bmad-creative-intelligence-suite)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-7289da?logo=discord&logoColor=white)](https://discord.gg/gk8jAdXWmj)

**Think differently.** A collection of agents and workflows for innovation, brainstorming, design thinking, and creative problem-solving.

## About CIS

The Creative Intelligence Suite (CIS) extends BMad Method with tools for the fuzzy front-end of development—where ideas are born, problems are reframed, and solutions emerge through structured creativity.

## Modules Included

| Agent/Workflow | Purpose |
|---------------|---------|
| **Innovation Strategist** | Identify disruption opportunities and business model innovation |
| **Design Thinking Coach** | Human-centered design through empathy, ideation, and prototyping |
| **Brainstorming Coach** | Facilitate creative ideation sessions with proven techniques |
| **Problem Solver** | Systematic problem diagnosis and root cause analysis |
| **Creative Problem Solver** | Generate creative solutions using lateral thinking |
| **Storyteller** | Craft compelling narratives for products and features |
| **Presentation Master** | Structure and deliver persuasive presentations |

## Installation

CIS is installed as a module during BMad Method setup:

```bash
npx bmad-method@alpha install
```

Select **Creative Intelligence Suite** from the modules list.

## Quick Start

After installing BMad Method with CIS, try these workflows:

```
/cis-brainstorm      # Generate ideas with structured techniques
/cis-design-thinking # Human-centered design process
/cis-problem-solve   # Systematic problem analysis
/cis-innovation      # Business model and disruption analysis
```

## When to Use CIS

| Situation | Use This |
|-----------|----------|
| Stuck on a problem | `/cis-problem-solve` |
| Need fresh ideas | `/cis-brainstorm` |
| Designing for users | `/cis-design-thinking` |
| Finding market gaps | `/cis-innovation` |
| Telling your product story | `/cis-storytelling` |
| Preparing a pitch | `/cis-presentation` |

## Example: Brainstorming Session

```
You: /cis-brainstorm
CIS: What would you like to brainstorm about?
You: Ways to improve user onboarding
CIS: Let's use the SCAMPER technique...
    [Guides you through 7 creative angles]
    [Generates diverse, actionable ideas]
```

## Workflow Capabilities

- **Idea Generation** — Multiple ideation frameworks (SCAMPER, Reverse Brainstorming, etc.)
- **Problem Reframing** — Turn obstacles into opportunities
- **User Empathy** — Build deep understanding of user needs
- **Solution Divergence** — Generate many options before converging
- **Narrative Craft** — Shape your product's story

## Team Collaboration

CIS includes team configurations for collaborative c
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `bmad-module-game-dev-studio.md`
```markdown
# 📦 bmad-code-org/bmad-module-game-dev-studio [🔖 PENDING/APPROVE]
🔗 https://github.com/bmad-code-org/bmad-module-game-dev-studio


## Meta
- **Stars:** ⭐ 121 | **Forks:** 🍴 13
- **Language:** JavaScript | **License:** NOASSERTION
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
BMad  Core Game Dev Studio

## README (trích đầu)
```
# BMad Game Dev Studio

[![Version](https://img.shields.io/npm/v/bmad-game-dev-studio?color=blue&label=version)](https://www.npmjs.com/package/bmad-game-dev-studio)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-7289da?logo=discord&logoColor=white)](https://discord.gg/gk8jAdXWmj)

**BMGD brings BMad's structured development to game development.** Create working prototypes quickly in Unity, Unreal, Godot—or any engine you choose.

![BMGD Logo](brain/knowledge/docs_legacy/bmgd-logo.png)

## About BMGD

BMad Game Dev Studio (BMGD) adapts the BMad Method framework for game development. Developed by game industry veterans, BMGD guides you through product research, technical design, narrative design, and a full epic-driven production cycle.

## Supported Engines

BMGD has first-class support for:

- [Unity](https://unity.com) — C# scripting, industry-standard for many game types
- [Unreal Engine](https://www.unrealengine.com/) — Blueprint and C++, AAA powerhouse
- [Godot](https://godotengine.org/) — Open-source, GDScript, rapidly growing

But you're not limited to these—BMGD works with any platform, from pure C to custom engines.

## What You Can Create

BMGD supports **21 game types**, including:

| Genre | Examples |
|-------|----------|
| Action | Platformers, shooters, hack-and-slash |
| RPG | Action RPG, tactical RPG, dungeon crawlers |
| Strategy | Turn-based, RTS, tower defense |
| Simulation | Life sim, tycoon, management |
| Adventure | Visual novels, point-and-click, walking simulators |
| And more... | Survival, horror, puzzle, racing, etc. |

## What BMGD Does

- **Product Research** — Market analysis, competitor research, positioning
- **Game Design Document** — Comprehensive GDD with mechanics, progression, and balance
- **Narrative Design** — Story structure, characters, dialogue, world-building
- **Technical Architecture** — Engine patterns, performance considerations
- **Production Planning** — Epic-driven sprints, story tracking, retrospectives
- **Quick Prototyping** — Skip the planning, jump straight into building

## What BMGD Doesn't Do

BMGD works *with* coding agents like Claude Code, Cursor, or GitHub Copilot—but it can't create everything:

- Art assets (models, textures, sprites)
- Animations
- Music and sound effects
- Full game implementation from scratch

Think of BMGD as your senior game dev colleague—not a replacement for your entire team.

## Installation

BMGD is installed as a module during BMad Method setup:

```bash
npx bmad-method@alpha install
```

Select **Game Dev Studio** from the modules list.

## Quick Start

After installing, run from your project root:

```
/bmad-help          # Get guided help for game development
/bmgd-quick-dev     # Jump straight into prototyping
/bmgd-gdd           # Create a Game Design Document
/bmgd-narrative     # Design your game's story
```

## Two Ways to Work

| Approach | When to Use | Workflow |
|----
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

