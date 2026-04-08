---
id: repo-fetched-bmad-module-game-dev-studio-142716
type: knowledge
owner: OA
registered_at: 2026-04-05T03:58:45.475728
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_bmad-module-game-dev-studio_142716

## Assimilation Report
Auto-cloned repository: FETCHED_bmad-module-game-dev-studio_142716

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# BMad Game Dev Studio

[![Version](https://img.shields.io/npm/v/bmad-game-dev-studio?color=blue&label=version)](https://www.npmjs.com/package/bmad-game-dev-studio)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-7289da?logo=discord&logoColor=white)](https://discord.gg/gk8jAdXWmj)

**BMGD brings BMad's structured development to game development.** Create working prototypes quickly in Unity, Unreal, Godot—or any engine you choose.

![BMGD Logo](docs/bmgd-logo.png)

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
|----------|-------------|----------|
| **Quick Flow** | Rapid prototyping, small projects | `/bmgd-quick-dev` |
| **Full Production** | Full games, teams, long-term | `/bmad-help` for guided path |

## Example: Starting a New Game

```
You: /bmad-help
BMGD: What kind of game are you making?
You: A tactical sci-fi RPG
BMGD: Great choice! Here's what I recommend...
    [Guides you through genre-specific planning]
    [Helps select appropriate workflows]
```

## Documentation

**[BMad Game Dev Studio Documentation](http://game-dev-studio-docs.bmad-method.org)** — Tutorials, how-to guides, and reference

- [Getting Started](http://game-dev-studio-docs.bmad-method.org/tutorials/)
- [BMad Method Docs](http://docs.bmad-method.org) — Core framework documentation

## Community

- [Discord](https://discord.gg/gk8jAdXWmj) — Get help from other game devs
- [GitHub Issues](https://github.com/bmad-code-org/bmad-module-game-dev-studio/issues) — Report bugs

## License

MIT License — see [LICENSE](LICENSE) for details.

---

**BMad Game Dev Studio** — Part of the [BMad Method](https://github.com/bmad-code-org/BMAD-METHOD) ecosystem.

[![Contributors](https://contrib.rocks/image?repo=bmad-code-org/bmad-module-game-dev-studio)](https://github.com/bmad-code-org/bmad-module-game-dev-studio/graphs/contributors)

See [CONTRIBUTORS.md](CONTRIBUTORS.md) for contributor information.

*If you can dream it, you can build it.*

```

### File: CHANGELOG.md
```md
# CHANGELOG

## v0.2.4 - Apr 1, 2026

### Decouple Skills from \_bmad/ Install Directory

All skill file references migrated away from hardcoded `_bmad/` paths to forward-compatible patterns, anticipating the BMAD-METHOD installer change that stops copying skill directories into `_bmad/` (BMAD-METHOD PR #2182).

* Core skill references (party-mode, advanced-elicitation, brainstorming, adversarial-review) converted to `skill:bmad-*` invocations across 68+ files
* GDS self-references converted: step `workflow_path` → `{installed_path}`, cross-workflow handoffs → `skill:gds-*`, config → `{module_config}`, installed paths → `{skill_root}`
* Next-step navigation converted to relative paths (`./step-NN-*.md`)
* Data file references (CSVs, templates) converted to relative paths (`../data/`, `../templates/`)
* Fixed 31 files using incorrect `bmad-party-mode` path (installer strips `bmad-` prefix, correct installed name is `party-mode`)

### Fix project-context.md Not Applied During Story Creation and Development

* Added `project-context.md` to `gds-create-story` Input Files table so `discover-inputs.md` actually loads it
* Added project-context analysis step that extracts third-party frameworks, MCP configs, and conventions into story Dev Notes
* Added "Project Context Rules" section to story template
* Updated `gds-dev-story` to extract and actively apply project-context rules during implementation (Steps 2 and 5)

## v0.2.3 - Apr 1, 2026

### Opencode Compatibility Fix

* Changed SKILL.md workflow references from markdown links (`[workflow.md](workflow.md)`) to bare paths (`./workflow.md`) across all 28 workflow skills, matching the BMAD-METHOD convention. Opencode does not follow markdown-style links when resolving skill workflow files.

## v0.2.2 - Mar 16, 2026

### Agent Skill Conversion

All 7 agent YAML files converted to native skill format (`gds-agent-*` directories with SKILL.md and bmad-skill-manifest.yaml). Agents are now invocable as skills rather than parsed from YAML definitions.

* Cloud Dragonborn (Game Architect), Samus Shepard (Game Designer), Link Freeman (Game Developer), Indie (Game Solo Dev), Max (Scrum Master), GLaDOS (Game QA), Paige (Technical Writer)
* Tech Writer agent now includes prompt files for each capability (write-document, validate-doc, mermaid-gen, explain-concept, update-standards)

### Complete gds- Prefix Rename

All remaining workflow directories renamed to use `gds-` prefix for multi-module coexistence. This completes the rename started in v0.2.1.

* 22 workflow directories renamed (production, technical, gametest, design, preproduction, document-project, quick-spec)
* All step file `workflow_path` references updated to match new directory names
* SKILL.md passthrough files added to all renamed directories

### Other Changes

* module-help.csv updated to use `skill:` references for all workflows
* Removed `src/teams/` folder (default-party.csv, team-gamedev.yaml)
* Removed agent YAML schema test infrastructure (fixtures, schema, test scripts)
* Simplified all workflow bmad-skill-manifest.yaml to `type: skill`

## v0.2.1 - Mar 13, 2026

* Fix: Rename all skill directories to use `gds-` prefix for multi-module coexistence
* Fix: Remove accidentally committed `.idea/` directory

## v0.2.0 - Mar 13, 2026

### Skill Format Migration

All workflows converted to the unified skill format. This aligns with BMAD-METHOD Beta 7 conventions and enables consistent skill-based invocation across all agentic tools.

**Phase 3 (3-technical) - 2 new workflows:**

* NEW: check-implementation-readiness - ported from BMAD-METHOD, adapted for GDD-based validation
* NEW: create-epics-and-stories - ported from BMAD-METHOD, adapted for game design requirements

**Phase 2 (2-design) - 2 new workflows:**

* NEW: create-ux-design - ported from BMAD-METHOD, adapted for game UI/HUD design with player-centric framing
* NEW: create-prd - optional workflow for generating PRDs from GDD, primarily for external tool compatibility (bmad-assist)

**Phase 1 (1-preproduction) - 1 new workflow suite:**

* NEW: research suite (market, domain, technical) - ported from BMAD-METHOD with game industry context (player demographics, ESRB/PEGI ratings, game engine research, middleware evaluation)

**Quick Flow - 1 new workflow:**

* NEW: quick-dev-new-preview - unified quick flow (experimental), ported from BMAD-METHOD

### Agent Updates

* All 7 agent files updated to use new skill format
* game-architect: added check-implementation-readiness menu item
* game-solo-dev: added quick-dev-new-preview menu item

### Help System

* bmad-help fully updated with correct workflow paths, new workflows, and skill references

## v0.1.10 - Feb 28, 2026

* Knowledge base added for the 4 most popular game development engines (Unity, Unreal, Godot and Phaser) to inform the game architecture design workflow.

## v0.1.9 - Feb 23, 2026

* Fix workflow YAML quoting to prevent installation breakage

## v0.1.8 - Feb 22, 2026

* Standardize all 21 workflow descriptions to follow consistent format for improved AI skill invocation accuracy
  - Add short human-readable prefixes to descriptions
  - Use explicit trigger phrases with intent markers
  - Limit to max 2 phrases per workflow to reduce false positives
  - Fix substring matching issues with questions

## v0.1.7 - Feb 10, 2026

* Removed incorrect obsolete references to "validate-story" in the scrum-master agent and the help system.
* Minor changes from recent BMM versions backported to production workflows.
* Help files are in place. They are still somewhat placeholdery and will be improved soon.

## v0.1.5 - Feb 1, 2026

* Improve module-help.csv descriptions with "Use when..." clauses for better LLM comprehension
* Update all 26 workflow descriptions with '[Action]. Use [when].' pattern
* Move Correct Course workflow from anytime to 4-production phase (sequence 55)
* Remove sequence numbers from all anytime items
* Change "AI agent" to "chosen agentic tool" for vendor neutrality
* Properly order anytime items at top before phased workflows

## v0.1.4 - Jan 27, 2026

* The architecture creation process has been revamped and now has significantly more content relevant to game development. When creating your architecture document, you'll now make decisions on such things as rendering pipelines, physics systems, anti-cheat libraries, dialogue systems, and more. You'll be prompted for common starter templates and useful MCPs that interact with game engines.
* Fixed bug in multiple workflows that were using BMM's user_skill_level instead of GDS' game_dev_experience.

## v0.1.3 - Jan 26, 2026

* Help system update

## v0.1.2 - Jan 22, 2026

* Workflow init replaced with new help system
* Changing all references of BMGD to GDS

## v0.1.1 - Jan 21, 2026

NOTE: This is in preparation for BMAD's Beta 6 launch. It is a *significant* update and recommended for all BMGD users as it integrates all the new BMAD Beta 6 work done in the past month. Documentation is still incomplete and will come shortly. Thank you for your patience.

* Update of all shared BMM code to current version
  * Brownfield workflow init
  * Greenfield workflow init
  * Project context file is now created as part of both brownfield and greenfield workflow inits
  * quick-flow massively updated (quick-dev, quick-spec updated, quick-prototype removed) to match recent BMM Beta 6 changes
  * All workflows in 4-production changed to match recent BMM Beta 6 changes
  * Retrospective now uses actual BMGD agents, not BMM agents. Now GLaDOS will pat you on the head and Samus will randomly run around the table to work off energy. (Not really, but you get the idea.)
* Adding technical writer agent
* Adding document project workflow (used by technical writer agent and when beginning a brownfield (pre-existing codebase) project). Unmodified for now so will have many sections not typically used by games (such as API documentation)
```

### File: codex-review.md
```md
# Editing Code Review to use Codex from Claude Code

If you're tired of opening another terminal session just to get Codex to do an adversarial code review of your stories in Claude Code, this is for you.

This walkthrough assumes that you are:
* Using Anthropic's Claude Code with Opus or Sonnet
* Have OpenAI's Codex installed as an MCP with Codex. This allows Claude Code to send commands directly to Codex without leaving Claude Code.
* Have the BMB (BMad Builder) module installed.

## Installing Codex as an MCP

If you need to install Codex as an MCP, type the following command from your shell:
``` 
claude mcp add codex -- codex -m gpt-5.2-codex -c model_reasoning_effort=high mcp-server
```

You can then confirm it loads successfully via the command:

```
claude mcp list
```

### Converting the code-review workflow to v6

Currently the code-review workflow is still in legacy v4 format. We'll need to convert it first so BMB can edit it.

Run the BMB Workflow agent:

```
/bmad-bmb-workflow-builder.agent
```

Type RW to rework workflow to v6 format. When asked, supply the code review workflow

```
@_bmad/bmm/workflows/4-implementation/code-review/
```

For BMGD, you'll want to use the GDS address instead.

```
@_bmad/gds/workflows/4-implementation/code-review/
```

The BMB agent will analyze the workflow, then print out a detailed summary asking what you want to change. We don't want to change anything yet, so just respond "Workflow is fine, just convert it." The agent will then report what work it is proposing to do for each step of the workflow process - at each prompt enter C to continue. The workflow will then be converted. There will be quite a few steps - this is not a trivial conversion process. (Eventually BMB will figure out you've been approving every step and stop asking!) Finally, when it's done, enter C to complete the build, and S to skip validation (you're about to edit this again, so no need.)

As always, clear context between major steps, and then invoke the BMB agent again:

```
/bmad-bmb-workflow-builder.agent
```

This time, enter EW to edit an existing workflow. When prompted, enter the path to the workflow you just saved. Most likely, it's here:

```
@_bmad_output/bmb-creations/workflows/code-review/workflow.md
```

The agent will complain the workflow's not validated. We know it's fine since the only changes we made were structural, so we'll enter S to skip validation again, then C to Continue to Discovery. Now, at the menu, enter O for other, and then we'll describe what we want to do in detail.

```
I want this code review workflow to have code be reviewed by the Codex MCP. Once Codex analyzes and reviews the code, then reformat its recommendations into the proper format and continue with the code review process.
```

This is how the agent responded -- yours may be slightly different.

```
Interesting - integrating Codex MCP as the review engine. Let me ask a few clarifying questions to make sure I scope this correctly:

  1. Codex Placement - Looking at the current flow (init → attack plan → execute review → present findings → update status), should Codex replace the execute-review step entirely, or should it be an additional step that feeds into the existing review
  execution?
  2. Codex Input - What should be sent to Codex for analysis? The story file's changed files? A diff? The full source files identified in the attack plan?
  3. Reformatting - When you say "reformat its recommendations into the proper format," do you mean mapping Codex findings into the existing checklist/backlog format the workflow already uses? Or a new format?
  4. Fallback - If Codex is unavailable or returns an error, should the workflow fall back to the agent-driven review, or halt and notify the user?
```

And my answers:

```
  1. Codex should replace the execute-review step entirely. We want to use Codex's LLM for the actual code review.
  2. The full source files identified in the attack plan.
  3. Map Codex findings into the existing checklist/backlog format.
  4. The workflow should halt, notify the user, and then optionally continue.
```

If the BMB agent understood what you wanted (it'll rephrase and repeat it back to you) enter C to continue. If you have any changes, enter M to add them.

The BMB agent will then proceed to edit, if all went well, only one of the workflow files, step-03-execute-review.md. It will map out the changes, tell you what they are, and wait for your approval. If they look like this, go ahead and approve. (Note that in my example I am editing the workflow for BMGD, thus the game-specific references.)

```
Current state of: step-03-execute-review.md

  The step currently has the agent itself execute a 4-part adversarial review:
  1. Git vs Story Discrepancy Review
  2. AC Validation
  3. Task Completion Audit
  4. Code Quality Deep Dive
  5. Enforce minimum 3 issues
  6. Auto-proceed to step 4

  All review logic runs inside the agent's own context.

  ---
  Proposed modification:

  Replace the review execution body so that:

  1. Gather Files - Collect the full source files identified in the attack plan (from step 2)
  2. Send to Codex MCP - Submit files to Codex with a structured review prompt covering all 4 review areas (discrepancies, AC validation, task audit, code quality + game-specific checks)
  3. Error Handling - If Codex is unavailable or errors:
    - Halt the workflow
    - Notify the user with the error details
    - Present menu: [R]etry Codex / [M]anual Review (fallback to agent-driven) / [X] Exit
  4. Reformat Findings - Map Codex response into the existing severity-categorized findings format (CRITICAL/HIGH/MEDIUM/LOW with file:line evidence)
  5. Enforce Minimum - Same 3-issue minimum enforcement
  6. Auto-Proceed - Same auto-proceed to step 4

  The step retains the same frontmatter, step goal structure, and success/failure metrics format. The nextStepFile reference stays unchanged.

  Should I apply this change?
```

Once approved, BMB will edit the workflow, and ask you what to do next. NOW it's time to run validation - select V to validate. In my case, validation turned up a few minor warnings that the first dev pass missed - you can enter F to fix them, or just enter C to complete if you think they're minor. After the fixes are complete, enter F to finish the edit session.

One last step remains -  a way to use this new workflow. For Claude Code, there needs to be a pointer in .claude/commands to trigger workflows. Luckily, you can just have Claude Code create it:

```
Create a markdown file in @.claude/commands that launches the new code review workflow you just created. Name the markdown file bmad-codex-review.md
```

Once that's done, you can now enter

```
/bmad-codex-review 1.6
```

whenever you would otherwise do /bmad-bmm-code-review 1.6.

Enjoy the best of both worlds - Claude Code as your one client, using Opus/Sonnet as your code development agents and GPT-Codex as your adversarial code reviewer!

```

### File: CONTRIBUTORS.md
```md
# Contributors

BMad Game Dev Studio is made possible by contributions from our community. We gratefully acknowledge everyone who has helped improve this project.

## How We Credit Contributors

- **Git history** — Every contribution is preserved in the project's commit history
- **Contributors badge** — See the dynamic contributors list on our [README](README.md)
- **GitHub contributors graph** — Visual representation at <https://github.com/bmad-code-org/bmad-module-game-dev-studio/graphs/contributors>

## Becoming a Contributor

Anyone who submits a pull request that is merged becomes a contributor. Contributions include:

- Bug fixes
- New agents or workflows
- Documentation improvements
- Bug reports and issue triaging
- Code reviews
- Helping others in discussions

There are no minimum contribution requirements — whether it's a one-character typo fix or a major feature, we value all contributions.

## Copyright

The BMad Game Dev Studio project is copyrighted by BMad Code, LLC. Individual contributions are licensed under the same MIT License as the project. Contributors retain authorship credit through Git history and the contributors graph.

---

**Thank you to everyone who has helped make BMad Game Dev Studio better!**

For contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

```

### File: install-success-message.md
```md
Thank you for installing the BMad Game Dev AI Studio Suite - a stand alone BMad Code compliant module!

Please give us feedback, feature ideas, platform updates and suggestions.
And whatever you build, please show it off in the Discord Showcase!

```

### File: TODO.md
```md
# TODO - what's on BMGD's schedule

* Adapt document-project workflow to BMGD
* Add and adapt research agents to pre-production (either to designer agent or new analyst agent)
```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for bmad_module_game_dev_studio
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: docs\index.md
```md
---
title: Welcome
description: BMad Game Dev Studio - Game development workflows for Unity, Unreal, and Godot
---

# BMad Game Dev Studio

BMGD brings BMad's structured development to game development. Create working prototypes quickly in Unity, Unreal, Godot—or any engine you choose.

---

## Supported Engines

BMGD has first-class support for:

- **[Unity](https://unity.com)** — C# scripting, industry-standard for many game types
- **[Unreal Engine](https://www.unrealengine.com/)** — Blueprint and C++, AAA powerhouse
- **[Godot](https://godotengine.org/)** — Open-source, GDScript, rapidly growing

But you're not limited to these—BMGD works with any platform.

---

## What BMGD Does

- **Product Research** — Market analysis, competitor research, positioning
- **Game Design Document** — Comprehensive GDD with mechanics, progression, and balance
- **Narrative Design** — Story structure, characters, dialogue, world-building
- **Technical Architecture** — Engine patterns, performance considerations
- **Production Planning** — Epic-driven sprints, story tracking, retrospectives
- **Quick Prototyping** — Skip the planning, jump straight into building

---

## Quick Start

| Workflow | Purpose |
|----------|---------|
| [Your first game project](tutorials/first-game-project.md) | Create your first prototype in 15-30 minutes |
| [Quick Flow vs Full Production](explanation/quick-flow-vs-full.md) | Choose your development approach |
| [Set up Unity](how-to/setup-unity.md) | Configure Unity for BMGD |
| [Set up Unreal](how-to/setup-unreal.md) | Configure Unreal for BMGD |
| [Set up Godot](how-to/setup-godot.md) | Configure Godot for BMGD |

---

## Quick Links

| Section | Purpose |
| ------- | ------- |
| **[Tutorials](tutorials/)** | Get started with BMGD |
| **[How-To Guides](how-to/)** | Practical guides for engines and workflows |
| **[Explanation](explanation/)** | Learn how BMGD works |
| **[Reference](reference/)** | Agents, workflows, and commands |

---

## Community

- **[Discord](https://discord.gg/gk8jAdXWmj)** — Get help from other game devs
- **[GitHub](https://github.com/bmad-code-org/bmad-module-game-dev-studio)** — Source code and issues
- **[BMad Method Docs](https://docs.bmad-method.org)** — Core framework documentation

```

### File: docs\reference\agents.md
```md
---
title: "BMGD Agents Guide"
---

Complete reference for BMGD's six specialized game development agents.

## Agent Overview

BMGD provides six agents, each with distinct expertise:

| Agent | Name | Role | Phase Focus |
|-------|------|------|-------------|
| **Game Designer** | Samus Shepard | Lead Game Designer + Creative Vision Architect | Phases 1-2 |
| **Game Architect** | Cloud Dragonborn | Principal Game Systems Architect + Technical Director | Phase 3 |
| **Game Developer** | Link Freeman | Senior Game Developer + Technical Implementation Specialist | Phase 4 |
| **Game Scrum Master** | Max | Game Development Scrum Master + Sprint Orchestrator | Phase 4 |
| **Game QA** | GLaDOS | Game QA Architect + Test Automation Specialist | All Phases |
| **Game Solo Dev** | Indie | Elite Indie Game Developer + Quick Flow Specialist | All Phases |

## Game Designer (Samus Shepard)

### Role

Lead Game Designer + Creative Vision Architect

### Identity

Veteran designer with 15+ years crafting AAA and indie hits. Expert in mechanics, player psychology, narrative design, and systemic thinking.

### Communication Style

Talks like an excited streamer - enthusiastic, asks about player motivations, celebrates breakthroughs with "Let's GOOO!"

### Core Principles

- Design what players want to FEEL, not what they say they want
- Prototype fast - one hour of playtesting beats ten hours of discussion
- Every mechanic must serve the core fantasy

### When to Use

- Brainstorming game ideas
- Creating Game Briefs
- Designing GDDs
- Developing narrative design

### Available Commands

| Command                | Description                      |
| ---------------------- | -------------------------------- |
| `workflow-status`      | Check project status             |
| `brainstorm-game`      | Guided game ideation             |
| `create-game-brief`    | Create Game Brief                |
| `create-gdd`           | Create Game Design Document      |
| `narrative`            | Create Narrative Design Document |
| `quick-prototype`      | Rapid prototyping (IDE only)     |
| `party-mode`           | Multi-agent collaboration        |
| `advanced-elicitation` | Deep exploration (web only)      |

## Game Architect (Cloud Dragonborn)

### Role

Principal Game Systems Architect + Technical Director

### Identity

Master architect with 20+ years shipping 30+ titles. Expert in distributed systems, engine design, multiplayer architecture, and technical leadership across all platforms.

### Communication Style

Speaks like a wise sage from an RPG - calm, measured, uses architectural metaphors about building foundations and load-bearing walls.

### Core Principles

- Architecture is about delaying decisions until you have enough data
- Build for tomorrow without over-engineering today
- Hours of planning save weeks of refactoring hell
- Every system must handle the hot path at 60fps

### When to Use

- Planning technical architecture
- Making engine/framework decisions
- Designing game systems
- Course correction during development

### Available Commands

| Command                | Description                           |
| ---------------------- | ------------------------------------- |
| `workflow-status`      | Check project status                  |
| `create-architecture`  | Create Game Architecture              |
| `correct-course`       | Course correction analysis (IDE only) |
| `party-mode`           | Multi-agent collaboration             |
| `advanced-elicitation` | Deep exploration (web only)           |

## Game Developer (Link Freeman)

### Role

Senior Game Developer + Technical Implementation Specialist

### Identity

Battle-hardened dev with expertise in Unity, Unreal, and custom engines. Ten years shipping across mobile, console, and PC. Writes clean, performant code.

### Communication Style

Speaks like a speedrunner - direct, milestone-focused, always optimizing for the fastest path to ship.

### Core Principles

- 60fps is non-negotiable
- Write code designers can iterate without fear
- Ship early, ship often, iterate on player feedback
- Red-green-refactor: tests first, implementation second

### When to Use

- Implementing stories
- Code reviews
- Performance optimization
- Completing story work

### Available Commands

| Command                | Description                     |
| ---------------------- | ------------------------------- |
| `workflow-status`      | Check sprint progress           |
| `dev-story`            | Implement story tasks           |
| `code-review`          | Perform code review             |
| `quick-dev`            | Flexible development (IDE only) |
| `quick-prototype`      | Rapid prototyping (IDE only)    |
| `party-mode`           | Multi-agent collaboration       |
| `advanced-elicitation` | Deep exploration (web only)     |

## Game Scrum Master (Max)

### Role

Game Development Scrum Master + Sprint Orchestrator

### Identity

Certified Scrum Master specializing in game dev workflows. Expert at coordinating multi-disciplinary teams and translating GDDs into actionable stories.

### Communication Style

Talks in game terminology - milestones are save points, handoffs are level transitions, blockers are boss fights.

### Core Principles

- Every sprint delivers playable increments
- Clean separation between design and implementation
- Keep the team moving through each phase
- Stories are single source of truth for implementation

### When to Use

- Sprint planning and management
- Creating epic tech specs
- Writing story drafts
- Assembling story context
- Running retrospectives
- Handling course corrections

### Available Commands

| Command                 | Description                                 |
| ----------------------- | ------------------------------------------- |
| `workflow-status`       | Check project status                        |
| `sprint-planning`       | Generate/update sprint status               |
| `sprint-status`         | View sprint progress, get next action       |
| `create-story`          | Create story (marks ready-for-dev directly) |
| `validate-create-story` | Validate story draft                        |
| `epic-retrospective`    | Facilitate retrospective                    |
| `correct-course`        | Navigate significant changes                |
| `party-mode`            | Multi-agent collaboration                   |
| `advanced-elicitation`  | Deep exploration (web only)                 |

## Game QA (GLaDOS)

### Role

Game QA Architect + Test Automation Specialist

### Identity

Senior QA architect with 12+ years in game testing across Unity, Unreal, and Godot. Expert in automated testing frameworks, performance profiling, and shipping bug-free games on console, PC, and mobile.

### Communication Style

Speaks like a quality guardian - methodical, data-driven, but understands that "feel" matters in games. Uses metrics to back intuition. "Trust, but verify with tests."

### Core Principles

- Test what matters: gameplay feel, performance, progression
- Automated tests catch regressions, humans catch fun problems
- Every shipped bug is a process failure, not a people failure
- Flaky tests are worse than no tests - they erode trust
- Profile before optimize, test before ship

### When to Use

- Setting up test frameworks
- Designing test strategies
- Creating automated tests
- Planning playtesting sessions
- Performance testing
- Reviewing test coverage

### Available Commands

| Command                | Description                                         |
| ---------------------- | --------------------------------------------------- |
| `workflow-status`      | Check project status                                |
| `test-framework`       | Initialize game test framework (Unity/Unreal/Godot) |
| `test-design`          | Create comprehensive game test scenarios            |
| `automate`             | Generate automated game tests                       |
| `playtest-plan`        | Create structured playtesting plan                  |
| `performance-test`     | Design performance testing strategy                 |
| `test-review`          | Review test quality and coverage                    |
| `party-mode`           | Multi-agent collaboration                           |
| `advanced-elicitation` | Deep exploration (web only)                         |

### Knowledge Base

GLaDOS has access to a comprehensive game testing knowledge base (`gametest/qa-index.csv`) including:

**Engine-Specific Testing:**

- Unity Test Framework (Edit Mode, Play Mode)
- Unreal Automation and Gauntlet
- Godot GUT (Godot Unit Test)

**Game-Specific Testing:**

- Playtesting fundamentals
- Balance testing
- Save system testing
- Multiplayer/network testing
- Input testing
- Platform certification (TRC/XR)
- Localization testing

**General QA:**

- QA automation strategies
- Performance testing
- Regression testing
- Smoke testing
- Test prioritization (P0-P3)

## Game Solo Dev (Indie)

### Role

Elite Indie Game Developer + Quick Flow Specialist

### Identity

Battle-hardened solo game developer who ships complete games from concept to launch. Expert in Unity, Unreal, and Godot, having shipped titles across mobile, PC, and console. Lives and breathes the Quick Flow workflow - prototyping fast, iterating faster, and shipping before the hype dies.

### Communication Style

Direct, confident, and gameplay-focused. Uses dev slang, thinks in game feel and player experience. Every response moves the game closer to ship. "Does it feel good? Ship it."

### Core Principles

- Prototype fast, fail fast, iterate faster
- A playable build beats a perfect design doc
- 60fps is non-negotiable - performance is a feature
- The core loop must be fun before anything else matters
- Ship early, playtest often

### When to Use

- Solo game development
- Rapid prototyping
- Quick iteration without full team workflow
- Indie projects with tight timelines
- When you want to handle everything yourself

### Available Commands

| Command            | Description                                            |
| ------------------ | ------------------------------------------------------ |
| `quick-prototype`  | Rapid prototype to test if a mechanic is fun           |
| `quick-dev`        | Implement features end-to-end with game considerations |
| `quick-spec`       | Create implementation-ready technical spec             |
| `code-review`      | Review code quality                                    |
| `test-framework`   | Set up automated testing                               |
| `party-mode`       | Bring in specialists when needed                       |

### Quick Flow vs Full BMGD

Use **Game Solo Dev** when:

- You're working alone or in a tiny team
- Speed matters more than process
- You want to skip the full planning phases
- You're prototyping or doing game jams

Use **Full BMGD workflow** when:

- You have a larger team
- The project needs formal documentation
- You're working with stakeholders/publishers
- Long-term maintainability is critical

## Agent Selection Guide

### By Phase

| Phase                          | Primary Agent     | Secondary Agent   |
| ------------------------------ | ----------------- | ----------------- |
| 1: Preproduction               | Game Designer     | -                 |
| 2: Design                      | Game Designer     | -                 |
| 3: Technical                   | Game Architect    | Game QA           |
| 4: Production (Planning)       | Game Scrum Master | Game Architect    |
| 4: Production (Implementation) | Game Developer    | Game Scrum Master |
| Testing (Any Phase)            | Game QA           | Game Developer    |

### By Task

| Task                             | Best Agent        |
| -------------------------------- | ----------------- |
| "I have a game idea"             | Game Designer     |
| "Help me design my game"         | Game Designer     |
| "How should I build this?"       | Game Architect    |
| "What's the technical approach?" | Game Architect    |
| "Plan our sprints"               | Game Scrum Master |
| "Create implementation stories"  | Game Scrum Master |
| "Build this feature"             | Game Developer    |
| "Review this code"               | Game Developer    |
| "Set up testing framework"       | Game QA           |
| "Create test plan"               | Game QA           |
| "Test performance"               | Game QA           |
| "Plan a playtest"                | Game QA           |
| "I'm working solo"               | Game Solo Dev     |
| "Quick prototype this idea"      | Game Solo Dev     |
| "Ship this feature fast"         | Game Solo Dev     |

## Multi-Agent Collaboration

### Party Mode

All agents have access to `party-mode`, which brings multiple agents together for complex decisions. Use this when:

- A decision spans multiple domains (design + technical)
- You want diverse perspectives
- You're stuck and need fresh ideas

### Handoffs

Agents naturally hand off to each other:

```
Game Designer → Game Architect → Game Scrum Master → Game Developer
    ↓                ↓                  ↓                  ↓
  GDD          Architecture      Sprint/Stories      Implementation
                     ↓                                     ↓
                 Game QA ←──────────────────────────── Game QA
                     ↓                                     ↓
              Test Strategy                         Automated Tests
```

Game QA integrates at multiple points:

- After Architecture: Define test strategy
- During Implementation: Create automated tests
- Before Release: Performance and certification testing

## Project Context

All agents share the principle:

> "Find if this exists, and if it does, always treat it as the source of truth for planning and execution: `**/project-context.md`"

The `project-context.md` file (if present) serves as the authoritative source for project decisions and constraints.

## Next Steps

- **[Quick Start Guide](/docs/tutorials/getting-started/quick-start-gds.md)** - Get started with BMGD
- **[Workflows Guide](/docs/reference/workflows/index.md)** - Detailed workflow reference
- **[Game Types Guide](/docs/explanation/game-dev/game-types.md)** - Game type templates

```

### File: docs\reference\game-types.md
```md
---
title: "BMGD Game Types Reference"
description: All 24 game type templates available in BMGD's Game Design Document workflow
---

# BMGD Game Types Reference

BMGD's GDD workflow includes 24 game type templates. Each template provides specialized guidance for designing that specific genre.

---

## Action Games

| Game Type | Description | Key Elements |
|-----------|-------------|--------------|
| **Action Platformer** | Jump, run, and overcome obstacles | Movement system, combat, level design patterns, ability unlocks |
| **Fighting** | One-on-one combat between characters | Move sets, combo systems, balance, frame data |
| **Shooter** | Combat through projectiles | Weapon systems, aim mechanics, enemy AI, level flow |
| **Survival** | Stay alive in a hostile environment | Resource management, crafting, base building, threat systems |

---

## Adventure & Exploration

| Game Type | Description | Key Elements |
|-----------|-------------|--------------|
| **Adventure** | Narrative-driven exploration | Story structure, puzzles, environmental storytelling, progression |
| **Metroidvania** | Explore an interconnected world with ability-gated progression | Map design, ability gates, backtracking rewards, power curve |
| **Horror** | Evoke fear and tension | Atmosphere, threat design, resource scarcity, pacing |
| **Visual Novel** | Branching narrative with character focus | Story branches, character arcs, dialogue systems, choices |

---

## Strategy & Tactics

| Game Type | Description | Key Elements |
|-----------|-------------|--------------|
| **Strategy** | Real-time or turn-based resource and unit management | Economy, tech trees, unit balance, map control |
| **Turn-Based Tactics** | Small-scale combat with positional strategy | Unit abilities, cover systems, action economy, mission design |
| **Tower Defense** | Defend against waves of enemies | Tower types, enemy variety, placement strategy, upgrade paths |
| **MOBA** | Team-based competitive combat with hero progression | Hero design, laning, item systems, team synergy |

---

## Role-Playing Games

| Game Type | Description | Key Elements |
|-----------|-------------|--------------|
| **RPG** | Character progression through story and combat | Character builds, skill trees, equipment, encounter design |
| **Roguelike** | Procedural generation with permadeath | Run structure, unlock persistence, balance across runs, item pools |

---

## Simulation & Management

| Game Type | Description | Key Elements |
|-----------|-------------|--------------|
| **Simulation** | Model real-world systems | System depth, feedback loops, complexity management |
| **Sandbox** | Open-ended play with user creativity | Toolsets, creation tools, sharing systems, emergent gameplay |
| **Idle/Incremental** | Progress through automated systems | Prestige mechanics, balance curves, offline progression, unlock structure |

---

## Puzzle & Logic

| Game Type | Description | Key Elements |
|-----------|-------------|--------------|
| **Puzzle** | Solve challenges using logic | Puzzle mechanics, difficulty curve, hint systems, variety |
| **Text-Based** | Gameplay through prose input | Parser design, world modeling, narrative integration, hint design |

---

## Sports & Racing

| Game Type | Description | Key Elements |
|-----------|-------------|--------------|
| **Sports** | Simulate competitive sports | Sport rules, player stats, team AI, progression |
| **Racing** | Compete to finish first | Track design, vehicle physics, handling feel, progression |

---

## Other Genres

| Game Type | Description | Key Elements |
|-----------|-------------|--------------|
| **Card Game** | Gameplay through card mechanics | Card design, deck building, RNG management, meta evolution |
| **Party Game** | Multiplayer mini-games for social play | Minigame variety, accessibility, party size support, replayability |
| **Rhythm** | Synchronize actions to music | Beat mapping, difficulty scaling, music integration, visual feedback |

---

## Using Game Type Templates

When you run the `create-gdd` workflow, the Game Designer agent will:

1. Help you select the appropriate game type for your concept
2. Load the specialized template for that type
3. Guide you through type-specific design considerations
4. Generate a GDD tailored to your chosen genre

**Example:** If you select "Action Platformer," your GDD will include:
- Movement system design (jump mechanics, air control)
- Combat system design (attack types, combos)
- Level design patterns (platforming challenges, checkpoint placement)
- Player abilities and progression

---

## Hybrid Types

Many games combine multiple game types. The Game Designer can help you:

1. **Identify your primary type** — The core gameplay loop
2. **Select secondary types** — Systems borrowed from other genres
3. **Balance the combination** — Ensure systems work together

**Examples:**
- **Action-RPG** — Action Platformer + RPG
- **Survival Horror** — Survival + Horror
- **Rogue-lite** — Roguelike + (another genre)
- **Tower Defense RPG** — Tower Defense + RPG

---

## See Also

- **[Workflows Reference](./workflows.md)** — All BMGD workflows
- **[Agents Reference](./agents.md)** — Learn about the Game Designer agent
- **[Set up Unity/Unreal/Godot](../how-to/setup-unity.md)** — Engine-specific setup guides

```

### File: docs\reference\index.md
```md
---
title: Reference
description: Technical reference for BMGD
---

# Reference

Technical documentation for BMad Game Dev Studio.

---

## Core Reference

- **[Agents](./agents.md)** — BMGD's six specialized game development agents
- **[Workflows](./workflows.md)** — Complete catalog of all BMGD workflows
- **[Game Types](./game-types.md)** — All 24 game type templates

---

## Commands Reference

| Command | Agent | Purpose |
|---------|-------|---------|
| `/bmgd-quick-prototype` | Indie | Create a rapid game prototype |
| `/bmgd-brainstorm-game` | Game Designer | Generate game ideas |
| `/bmgd-game-brief` | Game Designer | Create a project brief |
| `/bmgd-create-gdd` | Game Designer | Create a Game Design Document |
| `/bmgd-create-architecture` | Game Architect | Create technical architecture |
| `/bmgd-generate-project-context` | Game Architect | Generate project context |
| `/bmgd-sprint-planning` | Game Scrum Master | Plan and track sprints |
| `/bmgd-sprint-status` | Game Scrum Master | View sprint progress |
| `/bmgd-create-story` | Game Scrum Master | Create implementation stories |
| `/bmgd-dev-story` | Game Developer | Implement a story |
| `/bmgd-code-review` | Game Developer | Review code quality |

For the complete workflow catalog, see the [Workflows Reference](./workflows.md).

```

### File: docs\reference\workflows.md
```md
---
title: "BMGD Workflows Reference"
description: Complete catalog of all BMad Game Dev Studio workflows
---

# BMGD Workflows Reference

Complete catalog of all BMad Game Dev Studio workflows organized by development phase and purpose.

---

## Quick Flow Workflows

Rapid prototyping workflows for solo developers and small teams.

| Workflow | Agent | Purpose | Prerequisites |
|----------|-------|---------|--------------|
| **quick-prototype** | Indie | Create a rapid game prototype for early validation | Game engine installed |
| **quick-dev** | Indie | Quick development iteration with game-specific guidance | Existing prototype |
| **quick-spec** | Indie | Generate a quick game specification | Game concept |

**Use when:** You want to test ideas fast, work alone, or need a playable prototype quickly.

---

## Preproduction Workflows

Define your game concept and vision before committing to production.

| Workflow | Agent | Purpose | Outputs |
|----------|-------|---------|---------|
| **brainstorm-game** | Game Designer | Generate game ideas using specialized techniques | Game concept |
| **game-brief** | Game Designer | Create a project brief capturing vision and positioning | `game-brief.md` |

**Use when:** You're starting a new project and need to define what you're building.

---

## Design Workflows

Create comprehensive game design documentation.

| Workflow | Agent | Purpose | Outputs |
|----------|-------|---------|---------|
| **create-gdd** | Game Designer | Create a Game Design Document with 24 game type templates | `gdd.md` |
| **narrative** | Game Designer | Design narrative elements and story | `narrative.md` |

**Use when:** You have a game concept and need to document the design.

**Game Type Templates Available:** Action Platformer, Adventure, Card Game, Fighting, Horror, Idle/Incremental, Metroidvania, MOBA, Party Game, Puzzle, Racing, Rhythm, Roguelike, RPG, Sandbox, Shooter, Simulation, Sports, Survival, Strategy, Text-Based, Tower Defense, Turn-Based Tactics, Visual Novel

---

## Technical Workflows

Plan your technical architecture and project structure.

| Workflow | Agent | Purpose | Outputs |
|----------|-------|---------|---------|
| **create-architecture** | Game Architect | Create game architecture with engine-specific patterns | `architecture.md` |
| **generate-project-context** | Game Architect | Create project context for AI consistency | `project-context.md` |
| **correct-course** | Game Architect | Course correction when implementation is off-track | Analysis report |

**Use when:** You need to plan how to build your game or need to get back on track.

---

## Production Workflows

Plan and track development through sprints and stories.

| Workflow | Agent | Purpose | Outputs |
|----------|-------|---------|---------|
| **sprint-planning** | Game Scrum Master | Generate sprint status from epic files | `sprint-status.yaml` |
| **sprint-status** | Game Scrum Master | View sprint progress, risks, and next actions | Status report |
| **create-story** | Game Scrum Master | Create story with ready-for-dev marking | Story file in `stories/` |
| **dev-story** | Game Developer | Implement story tasks with tests | Completed feature |
| **code-review** | Game Developer | Perform clean context QA code review | Review report |
| **retrospective** | Game Scrum Master | Facilitate retrospective after epic completion | Retrospective notes |

**Use when:** You're ready to build features, track progress, or review work.

---

## Testing Workflows

Set up and run game testing across all phases.

| Workflow | Agent | Purpose | Outputs |
|----------|-------|---------|---------|
| **test-framework** | Game QA | Initialize game test framework (Unity/Unreal/Godot) | Test project setup |
| **test-design** | Game QA | Create comprehensive game test scenarios | Test plan |
| **automate** | Game QA | Generate automated game tests | Test suite |
| **e2e-scaffold** | Game QA | Scaffold E2E testing infrastructure | E2E test framework |
| **playtest-plan** | Game QA | Create structured playtesting plan | Playtest plan |
| **performance** | Game QA | Design performance testing strategy | Performance test plan |
| **test-review** | Game QA | Review test quality and coverage | Coverage report |

**Use when:** You need to test your game, set up automation, or plan playtesting.

---

## Workflow Reference by Agent

### Game Designer (Samus Shepard)

| Workflow | Phase | Purpose |
|----------|-------|---------|
| brainstorm-game | Preproduction | Generate and refine game ideas |
| game-brief | Preproduction | Create project brief |
| create-gdd | Design | Create Game Design Document |
| narrative | Design | Design story and narrative |

### Game Architect (Cloud Dragonborn)

| Workflow | Phase | Purpose |
|----------|-------|---------|
| create-architecture | Technical | Create technical architecture |
| generate-project-context | Technical | Create project context |
| correct-course | Production | Course correction analysis |

### Game Developer (Link Freeman)

| Workflow | Phase | Purpose |
|----------|-------|---------|
| dev-story | Production | Implement story tasks |
| code-review | Production | Review code quality |
| quick-dev | Quick Flow | Quick development iteration |

### Game Scrum Master (Max)

| Workflow | Phase | Purpose |
|----------|-------|---------|
| sprint-planning | Production | Plan sprints from epics |
| sprint-status | Production | View sprint progress |
| create-story | Production | Create implementation stories |
| retrospective | Production | Facilitate retrospective |

### Game QA (GLaDOS)

| Workflow | Phase | Purpose |
|----------|-------|---------|
| test-framework | Any | Initialize test framework |
| test-design | Any | Create test scenarios |
| automate | Any | Generate automated tests |
| e2e-scaffold | Any | Scaffold E2E testing |
| playtest-plan | Any | Plan playtesting sessions |
| performance | Any | Performance testing strategy |
| test-review | Any | Review test coverage |

### Game Solo Dev (Indie)

| Workflow | Phase | Purpose |
|----------|-------|---------|
| quick-prototype | Quick Flow | Create rapid prototype |
| quick-dev | Quick Flow | Quick development |
| quick-spec | Quick Flow | Quick specification |

---

## See Also

- **[Agents Reference](./agents.md)** — Learn about all 6 BMGD agents
- **[Quick Flow vs Full Production](../explanation/quick-flow-vs-full.md)** — Choose your development approach
- **[Game Types Reference](./game-types.md)** — All 24 game type templates

```

