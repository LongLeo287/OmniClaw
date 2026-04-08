# Agent Skill Creator: The Complete Guide

## Executive Summary

Agent Skill Creator is an open-source tool that transforms any workflow description into production-ready, cross-platform AI agent software. It removes the barrier between "I have a process" and "I have reusable agent software" — no coding, no prompt engineering, no specification writing required. Users describe what they do in plain language, and the system produces a validated, security-scanned skill that any team member can install and invoke on any AI platform (VS Code Copilot, Claude Code, Cursor, Copilot CLI, Windsurf, and more). Skills are the missing layer that turns powerful but generic AI tools into domain-specific, team-aware assistants that get smarter over time.

---

## Part 1: The Problem

### AI Tools Are Underutilized

Most enterprises pay for AI tooling — GitHub Copilot in VS Code, Copilot CLI, Cursor, Claude Code — but their teams use roughly 10% of available capabilities. The tools are powerful, but they start from zero in every conversation. They don't know your company's deployment process, your CRM data pipeline, your compliance requirements, or your internal API conventions.

### Knowledge Evaporates After Every Session

Every AI agent conversation is ephemeral. When a developer explains the deployment runbook to Copilot, that knowledge lives in a single chat history. The next person asks the same question and re-explains from scratch. New hires get no benefit from months of accumulated team conversations. Knowledge stays trapped in individual sessions and evaporates when the conversation ends.

### The Result: Repeated Work, Inconsistent Outputs

Without a way to persist and share domain knowledge:
- Every colleague re-explains the same workflow in every new session
- The same question produces different answers depending on who asks and how they phrase it
- New team members start from absolute zero, even if the team has been using AI for months
- There is no compounding effect — the organization never gets collectively smarter
- The gap between what AI tools CAN do and what teams ACTUALLY do widens over time

---

## Part 2: What Are Agent Skills

### Definition

A skill is structured knowledge that an AI agent loads automatically — like installing an app on your phone, but for your AI assistant. Once installed, the agent gains a specific capability: it knows when to activate, what steps to follow, what code to run, and what output to produce. Skills turn generic AI tools into specialized, domain-aware assistants.

### The App Analogy

Apps are software you install on your phone to give it new capabilities. Skills are software you install on your AI agent to give it new capabilities. Just as you install a banking app to manage finances on your phone, you install a sales-report-skill to generate weekly reports through your AI agent. The concept is identical — packaged software that extends a platform's functionality.

### Timeline and Open Standard

- **2024**: Anthropic introduces the concept of skills for Claude Code — structured markdown files (SKILL.md) that teach agents specific workflows and behaviors
- **December 2025**: VS Code 1.108 adopts the Agent Skills Open Standard, making skills a cross-platform concept. The `chat.agentSkillsLocations` setting defaults to searching `~/.claude/skills/` and `~/.copilot/skills/`, meaning skills installed for Claude Code are automatically available in VS Code Copilot
- **2026**: A growing ecosystem of skills works across Claude Code, VS Code Copilot, Copilot CLI, Cursor, Windsurf, Cline, Codex CLI, and Gemini CLI. One skill, written once, works on all platforms

### How Skills Activate

Skills activate automatically based on keyword matching. When a user types a query, the AI agent scans installed skills' descriptions and keywords. If there's a match, the skill activates and the agent follows its instructions. Users can also invoke skills directly by name: `/sales-report-skill Generate the Q4 West region report`. The activation is invisible — the agent simply becomes more capable on topics where skills are installed.

---

## Part 3: Anatomy of a Skill

### The Directory Structure

Every skill is a self-contained directory with a standard structure:

```
sales-report-skill/
├── SKILL.md          # The brain — defines behavior and activation
├── scripts/          # The hands — functional Python code
├── references/       # The memory — detailed docs loaded on demand
├── assets/           # Templates, configs, data files
├── install.sh        # Cross-platform installer
└── README.md         # Human-readable installation guide
```

### SKILL.md — The Brain

SKILL.md is the primary file. It is the only file the agent reads first. It defines:

- **Frontmatter**: Machine-readable metadata including the skill name (kebab-case, must end with `-skill`), a description packed with activation keywords (up to 1024 characters), license, author, and version
- **When to Use**: Explicit instructions on when this skill should activate
- **Workflows**: Step-by-step instructions the agent follows, including which scripts to run, in what order, and how to interpret results
- **Error Handling**: What to do when things go wrong
- **Examples**: 5+ complete examples showing input, execution flow, and expected output

SKILL.md must be under 500 lines. All detailed content goes in references/ to keep the primary file focused and fast to load.

### Scripts — The Hands

The scripts/ directory contains functional Python code that performs the actual work. This is not pseudocode or scaffolding — every script is complete, tested, and ready to execute. Scripts handle data fetching, parsing, analysis, formatting, and output generation. They include type hints, docstrings, error handling, and input validation.

### References — The Memory

The references/ directory contains detailed documentation that the agent loads on demand when it needs deeper context. Each reference file is 1000-2500 words of substantive content — not external links, but actual documentation with examples, formulas, and troubleshooting steps. This progressive loading keeps SKILL.md lightweight while making deep knowledge available when needed.

### install.sh — The Installer

Every skill includes a cross-platform installer that auto-detects the user's AI platform and installs the skill to the correct location. It supports Claude Code, VS Code Copilot, Cursor, Windsurf, Cline, Codex CLI, and Gemini CLI. Users can also specify a platform explicitly with the `--platform` flag.

---

## Part 4: Your Tools Are Already Agents

### The Agent Inside Your IDE

Most people think of VS Code with GitHub Copilot as "autocomplete that's really good." It's not. Since VS Code 1.108 (December 2025), Copilot is a full AI agent — it reads entire codebases, writes across multiple files, runs terminal commands, plans multi-step operations, and can be extended with skills. The autocomplete is the 10% surface; the agent underneath is the 90% most teams never use.

### Agents Already on Your Machine

If your organization uses any of these tools, you already have AI agents:

- **VS Code with GitHub Copilot**: An IDE agent that reads, writes, and refactors code across your entire project. It searches files, understands project structure, runs commands, and follows multi-step instructions. Since 1.108+, it natively supports agent skills from `~/.claude/skills/` and `~/.copilot/skills/`.

- **Copilot CLI**: A terminal agent that understands shell commands, fixes errors, generates scripts, and automates command-line workflows. Installed alongside GitHub Copilot.

- **Cursor**: An editor agent that understands your full codebase and generates contextual code. It supports skills via `.cursor/rules/` per project.

- **Claude Code**: A CLI agent that plans, builds, tests, and deploys complete features autonomously. It supports global skills at `~/.claude/skills/`.

### The Vehicle Metaphor

These tools are vehicles. The agent is the engine. Skills are the GPS routes. Without skills, you have a powerful car with no directions — it can go anywhere, but you have to manually navigate every time. With skills installed, the agent knows the route. It knows your company's deployment process, your data pipeline, your compliance requirements. The vehicle is the same; the intelligence is different.

### Shared Global Path

A key discovery: VS Code Copilot and Claude Code share the same global skills directory at `~/.claude/skills/`. Installing a skill once with `git clone ... ~/.claude/skills/my-skill` makes it available on both platforms. This is not a workaround — it's the official default behavior since VS Code 1.108.

---

## Part 5: Agent Skill Creator — The Solution

### What It Is

Agent Skill Creator is itself a skill — installed on your AI agent just like any other. Once installed, you invoke it with `/agent-skill-creator` followed by whatever raw material you have: plain English descriptions, documentation links, existing code, API docs, PDFs, database schemas, meeting transcripts, or vague intentions. The system reads everything, uncovers implicit requirements, and produces a complete, validated skill.

### What It Is Not

Agent Skill Creator is not a template engine, not a code generator, and not a chatbot. It is an autonomous skill factory that:
- Makes its own decisions about architecture, naming, and implementation
- Researches APIs and data sources independently
- Uncovers implicit requirements that humans forget to mention
- Validates and security-scans its own output
- Blocks delivery of anything that fails quality checks

### Installation (One Command)

For Claude Code and VS Code Copilot (global — works in all projects):
```
git clone https://github.com/FrancyJGLisboa/agent-skill-creator.git ~/.claude/skills/agent-skill-creator
```

For Cursor (per-project):
```
git clone https://github.com/FrancyJGLisboa/agent-skill-creator.git .cursor/rules/agent-skill-creator
```

One install at `~/.claude/skills/` makes agent-skill-creator available on both Claude Code and VS Code Copilot simultaneously.

### How to Use It

Open your AI agent and type:

```
/agent-skill-creator Every week I pull sales data from our CRM,
clean duplicate entries, calculate regional totals, and generate a PDF report.
```

Or point it at existing material:

```
/agent-skill-creator Based on our deployment runbook: https://wiki.internal/deploy-process
```

```
/agent-skill-creator See scripts/invoice_processor.py — turn it into a reusable skill
```

```
/agent-skill-creator Here's our API docs: https://api.internal/docs
Create a skill that queries stock levels and generates reorder reports.
```

You can combine multiple sources in one message. The more context, the better the result.

---

## Part 6: The 5-Phase Creation Pipeline

Agent Skill Creator doesn't just follow your description literally. Humans describe what they DO, not what they NEED. "I pull sales data and make a report" hides a dozen implicit requirements — who reads the report, what format, what happens when data is missing, what edge cases exist. The system reads all your material, uncovers these hidden requirements, and generates its own internal specification before writing any code.

### Phase 1: DISCOVERY

The system researches the domain autonomously:
- Searches for 5-10 candidate APIs and data sources relevant to the workflow
- Evaluates each on coverage, cost, rate limits, data quality, and documentation
- Compares options using a scoring matrix
- Selects the best API with documented justification
- Extracts complete technical specifications from API documentation

This phase ensures the skill is built on the best available data source, not just the first one the user mentioned.

### Phase 2: DESIGN

The system designs the skill's capabilities:
- Brainstorms 15-20 typical use cases from the workflow description
- Groups use cases by analysis type
- Prioritizes 4-6 analyses that cover 80% of use cases
- For each analysis, documents: objective, required inputs, expected outputs, methodology, formulas, validation criteria, and interpretation guidelines
- Designs a comprehensive report function that combines multiple analyses

The specification must surpass the human's understanding of their own workflow — surfacing edge cases, validations, and interpretations they didn't think to mention.

### Phase 3: ARCHITECTURE

The system decides the skill's structure:
- Simple Skill (1-2 workflows, under 1000 lines of code, single developer) vs. Complex Suite (3+ workflows, over 2000 lines, team maintenance)
- Defines directory structure and script responsibilities
- Plans caching strategy and rate limiting
- Generates a spec-compliant skill name (kebab-case, ending with `-skill`, 1-64 characters)

### Phase 4: DETECTION

The system crafts the activation mechanism:
- Lists all domain entities (organizations, objects, geography, metrics, temporality)
- Lists action verbs (query, compare, rank, analyze, forecast, report)
- Generates 50-80+ activation keywords across all metrics
- Maps question variations for each analysis type
- Defines negative scope (what should NOT activate this skill)
- Compresses everything into a 1024-character description field that serves as the activation mechanism

The description field IS the activation system. There is no separate activation file — the packed keywords in the description are how the agent decides when to trigger the skill.

### Phase 5: IMPLEMENTATION

The system builds everything:
1. Creates directory structure
2. Writes SKILL.md with spec-compliant frontmatter and comprehensive instructions
3. Implements all Python scripts with complete, functional code (no placeholders, no TODOs)
4. Writes reference documentation (1000-2500 words per file)
5. Creates asset files with real values (not "YOUR_KEY_HERE")
6. Generates cross-platform install.sh
7. Writes multi-platform README.md
8. Runs spec validation automatically
9. Runs security scan automatically
10. Auto-installs the skill on the current platform
11. Optionally publishes to the team registry

---

## Part 7: Quality Gates

Every skill must pass two automated checks before delivery. Skills that fail are blocked — the system will not deliver incomplete or insecure output.

### Spec Validation

The validator checks:
- SKILL.md exists and has properly formatted YAML frontmatter
- Name field: 1-64 characters, lowercase letters + numbers + hyphens, no consecutive hyphens, no leading/trailing hyphens, must end with `-skill`
- Directory name matches the name field in frontmatter
- Description field: 1-1024 characters, packed with activation keywords
- SKILL.md body: under 500 lines (move details to references/)
- License field present
- Metadata fields present (author, version)
- All local file references resolve to existing files

Run independently:
```
python3 scripts/validate.py ./my-skill/
python3 scripts/validate.py ./my-skill/ --json
```

### Security Scan

The scanner checks:
- No hardcoded API keys (detects patterns for OpenAI, AWS, GitHub, GitLab, Slack, and other services)
- No .env files containing credentials
- No dangerous Python patterns: eval(), exec(), os.system() with string concatenation, subprocess with shell=True
- No sensitive files: credentials.json, secrets.json, api_keys.json

Run independently:
```
python3 scripts/security_scan.py ./my-skill/
python3 scripts/security_scan.py ./my-skill/ --json
```

Both tools use exit code 0 for pass, 1 for failure. Both support `--json` for CI/CD integration.

---

## Part 8: Cross-Platform Support

### Global Installation (Available in All Projects)

These platforms support a global user-level skills directory. Install once, use in every project:

| Platform | Install Path | Notes |
|----------|---|---|
| Claude Code | `~/.claude/skills/` | Native global support |
| VS Code Copilot | `~/.claude/skills/` | Same path as Claude Code since VS Code 1.108+ |
| VS Code Copilot | `~/.copilot/skills/` | Alternative dedicated path |
| Copilot CLI | `~/.copilot/skills/` | Shares with VS Code Copilot |

One `git clone` to `~/.claude/skills/` makes a skill globally available on both Claude Code and VS Code Copilot. This is the officially supported behavior, not a workaround.

### Per-Project Installation

For platforms without global directories, or for project-specific skills:

| Platform | Install Path |
|----------|---|
| VS Code Copilot | `.github/skills/` |
| Cursor | `.cursor/rules/` |
| Windsurf | `.windsurf/skills/` |
| Cline | `.clinerules/` |
| Codex CLI | `.codex/skills/` |
| Gemini CLI | `.gemini/skills/` |

### Cursor Global Workaround

Cursor does not have a global skills directory (most-requested feature on their forum, not yet implemented). Workaround: clone once to `~/agent-skills/`, then symlink into each project:

```
git clone ... ~/agent-skills/agent-skill-creator
mkdir -p .cursor/rules && ln -s ~/agent-skills/agent-skill-creator .cursor/rules/agent-skill-creator
```

### Desktop and Web

For Claude Desktop and claude.ai:
```
python3 scripts/export_utils.py ./skill-name --variant desktop
```
Then upload the generated .zip through Settings > Skills.

---

## Part 9: Sharing Skills Across Teams

### Single Skill Sharing

After the agent builds and installs a skill, it can create a git repository and push the skill so colleagues can install it with one command:

```
git clone https://github.com/your-org/sales-report-skill.git ~/.claude/skills/sales-report-skill
```

The agent detects whether the team uses GitHub or GitLab, creates the repo, pushes, and generates platform-specific install commands. Colleagues paste one line and the skill is ready.

### The Skill Registry

When an organization has more than a few skills, the agent offers to set up a team skill registry — a shared git repo where all team members publish skills and anyone can browse and install them.

**Initialize the registry (once)**:
```
python3 scripts/skill_registry.py init --name "Acme Corp Skills"
```

**Publish a skill**:
```
python3 scripts/skill_registry.py publish ./sales-report-skill/ --tags sales,reports
```

**Browse available skills**:
```
python3 scripts/skill_registry.py list
```

**Search for a skill**:
```
python3 scripts/skill_registry.py search "sales"
```

**Install a skill from the registry**:
```
python3 scripts/skill_registry.py install sales-report-skill
```

The registry is a git repo — no servers, no databases. Git provides version history, access control (repo permissions), and review workflow (pull requests).

### The Compounding Effect Over Time

Each team member creates skills from their own domain expertise and shares them:

- Sales team shares `/sales-report-skill`
- Engineering shares `/deploy-checklist-skill`
- Legal shares `/quarterly-compliance-skill`
- Data science shares `/customer-churn-skill`
- SRE shares `/incident-runbook-skill`

Any colleague installs any skill with one `git clone`. Any agent on any platform can invoke it. After 6 months, the organization has a library of reusable intelligence. Knowledge compounds instead of evaporating. New hires get the accumulated expertise of the entire team on day one.

---

## Part 10: The Consultant Engagement Model

### Teach, Don't Build

The engagement model for AI consultants is teach, not build. The consultant's job is not to build skills for the team — the team knows their workflows better than any outsider ever will. The consultant's job is to remove the friction.

### The 5-Step Process

1. **Install**: Set up agent-skill-creator on each team member's machine (one `git clone` command)
2. **Create Registry**: Initialize a shared `{team}-skills-registry` GitHub/GitLab repo
3. **Demonstrate**: Create one skill live with the team, showing the full process
4. **Teach**: Walk through publishing, searching, and installing from the registry
5. **Hand Over**: Leave a self-sustaining system. After the consultant departs, the team keeps creating and sharing skills independently

### The After State

After the consultant engagement:
- Every team member can create skills from their own workflows
- Skills are automatically validated and security-scanned
- The shared registry grows as each person contributes
- New hires install the registry and gain access to all accumulated knowledge
- The system requires zero ongoing maintenance — it's just git

---

## Part 11: Templates, Interactive Mode, and Advanced Features

### Templates

Pre-built scaffolds for common domains that save 30-50% of creation time:

- **Financial Analysis**: Alpha Vantage + Yahoo Finance, technical indicators, portfolio analysis
- **Climate Analysis**: Open-Meteo + NOAA, weather patterns, forecasting
- **E-commerce Analytics**: Google Analytics + Stripe + Shopify, revenue analysis, cohorts

The system auto-detects when a template matches user input (keyword scoring above 0.70) and suggests it. Teams can also create and register custom templates.

### Interactive Mode

A step-by-step wizard for complex projects:

```
"Create a skill for quarterly compliance interactively"
```

The wizard guides users through: gathering requirements, analyzing relationships, choosing architecture, previewing the plan, and building with progress reporting. The user controls each decision while the system handles implementation.

### Multi-Agent Suites

For complex domains requiring 3+ related skills:

```
"Create a financial analysis suite with agents for
fundamental analysis, technical analysis, portfolio optimization, and risk assessment"
```

The system creates a suite with shared components, orchestration logic, and independent skills that work together or standalone. Suites support intent-based routing, sequential pipelines, parallel aggregation, and conditional routing patterns.

### Export System

Export skills for platforms that don't support directory-based installation:

```
python3 scripts/export_utils.py ./skill-name --variant desktop   # For Claude Desktop
python3 scripts/export_utils.py ./skill-name --variant api       # For Claude API
```

---

## Part 12: The Vision — Knowledge as Compounding Infrastructure

### Short Term (Month 1)

Each person installs agent-skill-creator and creates their first skill from a workflow they repeat weekly. The skill works. They share it. A colleague installs it and stops re-explaining that workflow to their agent.

### Medium Term (Months 2-6)

The team registry grows to 10-20 skills covering the most common workflows. New hires install the registry and are productive on day one. Cross-department skills emerge — engineering skills that help sales, compliance skills that help engineering. The organization starts seeing AI as a knowledge management system, not just a coding assistant.

### Long Term (Months 6-12)

The skill library becomes organizational infrastructure — like an internal wiki, but one that actually executes. Skills encode institutional knowledge that survives employee turnover. The gap between what AI tools can do and what teams actually do closes. The compounding effect accelerates: each new skill makes every agent-user more productive, which motivates more skill creation.

### The Core Insight

Knowledge doesn't depreciate — it compounds. Every skill created makes the next person more productive. Every workflow captured is a workflow that never needs to be re-explained. The organization's collective AI capability grows monotonically. This is the fundamental shift: from AI as a conversation tool to AI as a knowledge infrastructure layer.

---

## Technical Reference

### Naming Convention

- Format: `{domain}-{objective}-skill` (kebab-case)
- Must end with `-skill` (or `-suite` for multi-agent suites)
- 1-64 characters, lowercase letters + numbers + hyphens
- No consecutive hyphens, no leading/trailing hyphens
- Directory name must match the name field in SKILL.md frontmatter
- Examples: `stock-analyzer-skill`, `sales-report-skill`, `deploy-checklist-skill`

### SKILL.md Frontmatter Schema

```yaml
---
name: sales-report-skill
description: >-
  Generate weekly and monthly sales reports from CRM data with
  regional breakdowns, trend analysis, and PDF export...
license: MIT
metadata:
  author: sales-team
  version: 1.0.0
---
```

### Registry JSON Schema

```json
{
  "registry": {
    "name": "Acme Corp Skills",
    "created": "2026-02-27T00:00:00Z",
    "schema_version": "1"
  },
  "skills": [
    {
      "name": "sales-report-skill",
      "description": "Generate weekly sales reports...",
      "version": "1.0.0",
      "author": "sales-team",
      "tags": ["sales", "reports", "crm"],
      "published": "2026-02-27T10:30:00Z",
      "path": "skills/sales-report-skill"
    }
  ]
}
```

### Project Repository Structure

```
agent-skill-creator/
  SKILL.md                      # The skill definition
  README.md                     # Installation and usage guide
  scripts/
    validate.py                 # Spec compliance checker
    security_scan.py            # Security scanner
    export_utils.py             # Cross-platform export
    skill_registry.py           # Team skill registry
    install-template.sh         # Template for generated installers
  references/                   # Detailed documentation
    pipeline-phases.md          # Full creation pipeline
    architecture-guide.md       # Skill structure decisions
    quality-standards.md        # Code and documentation standards
    multi-agent-guide.md        # Multi-skill suite creation
    cross-platform-guide.md     # Platform compatibility
    export-guide.md             # Export documentation
    templates-guide.md          # Template system
    interactive-mode.md         # Interactive wizard
  registry/                     # Shared skill catalog
    registry.json
    skills/
```

---

## Key Statistics and Facts

| Metric | Value |
|--------|-------|
| Supported Platforms | 8+ (Claude Code, VS Code Copilot, Cursor, Windsurf, Cline, Copilot CLI, Codex CLI, Gemini CLI) |
| Global Install Platforms | Claude Code + VS Code Copilot (shared path) |
| Max SKILL.md Body | 500 lines |
| Max Name Length | 64 characters |
| Max Description Length | 1024 characters |
| Activation Keywords | 50-80+ per skill |
| Activation Success Rate | 98% (stock-analyzer example) |
| False Positive Rate | 0% (stock-analyzer example) |
| Template Time Savings | 30-50% |
| Dependencies | Zero (stdlib only for all scripts) |
| License | MIT |
| Version | 4.0.0 |

---

## Tags

`agent-skills` `ai-agents` `cross-platform` `open-standard` `vscode-copilot` `claude-code` `cursor` `skill-registry` `knowledge-management` `enterprise-ai` `workflow-automation` `no-code` `team-collaboration` `git-based` `security-scanning` `spec-validation` `reusable-software` `compounding-knowledge` `consultant-toolkit` `ai-adoption`

---

## Links

- GitHub Repository: https://github.com/FrancyJGLisboa/agent-skill-creator
- Agent Skills Open Standard: https://github.com/anthropics/agent-skills-spec
- VS Code Agent Skills Documentation: https://code.visualstudio.com/docs/copilot/customization/agent-skills
