---
id: github.com-phuryn-pm-skills-6c8a6207-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:12.580628
---

# KNOWLEDGE EXTRACT: github.com_phuryn_pm-skills_6c8a6207
> **Extracted on:** 2026-04-01 11:44:39
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007521507/github.com_phuryn_pm-skills_6c8a6207

---

## File: `.gitattributes`
```
# Auto detect text files and perform LF normalization
* text=auto
*.py linguist-detectable=false 
```

## File: `.gitignore`
```
_Internal/
CLAUDE.md
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing

PM Skills Marketplace is maintained by [Paweł Huryn](https://www.productcompass.pm) (pawel@productcompass.pm). Contributions are welcome — whether it's a bug fix, a typo, or a new skill idea.

## How to Contribute

- **Bugs and small fixes** — open a PR directly.
- **New skills, commands, or larger changes** — open an issue first so we can discuss the approach.

## Guidelines

- Keep PRs focused — one change per PR.
- Follow existing patterns: skills are nouns (domain knowledge), commands are verbs (workflows).
- Every skill needs frontmatter with `name` and `description`. Every command needs `description` and `argument-hint`.
- Skill `name` must match its directory name.
- No cross-plugin references in commands. Suggest follow-ups in natural language only.
- Every contributor will be listed publicly.
- Run the validator before submitting: `python3 validate_plugins.py`

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Pawel Huryn

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

## File: `README.md`
```markdown
![GitHub stars](https://img.shields.io/github/stars/phuryn/pm-skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](https://github.com/phuryn/pm-skills/blob/main/LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](https://github.com/phuryn/pm-skills/blob/main/CONTRIBUTING.md)

# PM Skills Marketplace: The AI Operating System for Better Product Decisions

> 65 PM skills and 36 chained workflows across 8 plugins. Claude Code, Cowork, and more. From discovery to strategy, execution, launch, and growth. 

![Plugin overview](.docs/images/plugins-overview.webp)

Designed for Claude Code and Cowork. Skills compatible with other AI assistants.

## Start Here

New idea? → `/discover`  
Need strategic clarity? → `/strategy`  
Writing a PRD? → `/write-prd`  
Planning a launch? → `/plan-launch`  
Defining metrics? → `/north-star`

If this project helps you, ⭐ the repo.

## Why PM Skills Marketplace?

Generic AI gives you text. PM Skills Marketplace gives you structure.

Each skill encodes a proven PM framework — discovery, assumption mapping, prioritization, strategy — and walks you through it step by step. You get the rigor of Teresa Torres, Marty Cagan, and Alberto Savoia built into your daily workflow, not sitting on a bookshelf.

The result: better product decisions, not just faster documents.

## How It Works (Skills, Commands, Plugins)

**Skills** are the building blocks of the marketplace. Each skill gives Claude domain knowledge, analytical frameworks, or a guided workflow for a specific PM task. Some skills also work as reusable foundations that multiple commands share. 

Skills are loaded automatically when relevant to the conversation — no explicit invocation needed. If needed (e.g., prioritizing skills over general knowledge), you can **force loading skills** with `/plugin-name:skill-name` or `/skill-name` (Claude will add the prefix).

**Commands** are user-triggered workflows invoked with `/command-name`. They chain one or more skills into an end-to-end process. For example, `/discover` chains four skills together: brainstorm-ideas → identify-assumptions → prioritize-assumptions → brainstorm-experiments.

**Plugins** group related skills and commands into installable packages. Each plugin covers a PM domain — discovery, strategy, execution, and so on. Installing the marketplace gives you all 8 plugins at once.

![How skills work](.docs/images/how-skills-work.webp)

Commands use skills. Some skills serve multiple commands. Some skills (like `prioritization-frameworks` or `opportunity-solution-tree`) are standalone references that Claude draws on whenever relevant — no command needed.

Commands are designed to flow into each other, matching the PM workflow. After any command completes, it suggests relevant next commands — just follow the prompts.

## Installation

### Claude Cowork (recommended for non-developers)

1. Open **Customize** (bottom-left)
2. Go to **Browse plugins** → **Personal** → **+**
3. Select **Add marketplace from GitHub**
4. Enter: `phuryn/pm-skills`

All 8 plugins install automatically. You get both commands (`/discover`, `/strategy`, etc.) and skills.

![Installing PM Skills in Claude Cowork](.docs/images/pm-skills-install.gif)

### Claude Code (CLI)

```bash
# Step 1: Add the marketplace
claude plugin marketplace add phuryn/pm-skills

# Step 2: Install individual plugins
claude plugin install pm-toolkit@pm-skills
claude plugin install pm-product-strategy@pm-skills
claude plugin install pm-product-discovery@pm-skills 
claude plugin install pm-market-research@pm-skills 
claude plugin install pm-data-analytics@pm-skills
claude plugin install pm-marketing-growth@pm-skills
claude plugin install pm-go-to-market@pm-skills
claude plugin install pm-execution@pm-skills
```

### Other AI assistants (skills only)

The `skills/*/SKILL.md` files follow the universal skill format and work with any tool that reads it. Commands (`/slash-commands`) are Claude-specific.

| Tool | How to use | What works |
|------|-----------|------------|
| **Gemini CLI** | Copy skill folders to `.gemini/skills/` | Skills only |
| **OpenCode** | Copy skill folders to `.opencode/skills/` | Skills only |
| **Cursor** | Copy skill folders to `.cursor/skills/` | Skills only |
| **Codex CLI** | Copy skill folders to `.codex/skills/` | Skills only |
| **Kiro** | Copy skill folders to `.kiro/skills/` | Skills only |

```bash
# Example: copy all skills for OpenCode (project-level)
for plugin in pm-*/; do
  mkdir -p .opencode/skills/
  cp -r "$plugin/skills/"* .opencode/skills/ 2>/dev/null
done

# Example: copy all skills for Gemini CLI (global)
for plugin in pm-*/; do
  cp -r "$plugin/skills/"* ~/.gemini/skills/ 2>/dev/null
done
```

---

## Available Plugins

<details>
<summary><strong>1. pm-product-discovery</strong> — Ideation, experiments, assumption testing, OSTs, interviews (13 skills, 5 commands)</summary>

**Skills (13):**

- `brainstorm-ideas-existing` — Multi-perspective ideation for existing products (PM, Designer, Engineer)
- `brainstorm-ideas-new` — Ideation for new products in initial discovery
- `brainstorm-experiments-existing` — Design experiments to test assumptions for existing products
- `brainstorm-experiments-new` — Design lean startup pretotypes for new products (Alberto Savoia)
- `identify-assumptions-existing` — Identify risky assumptions across Value, Usability, Viability, and Feasibility
- `identify-assumptions-new` — Identify risky assumptions across 8 risk categories including Go-to-Market, Strategy, and Team
- `prioritize-assumptions` — Prioritize assumptions using an Impact × Risk matrix with experiment suggestions
- `prioritize-features` — Prioritize a feature backlog based on impact, effort, risk, and strategic alignment
- `analyze-feature-requests` — Analyze and categorize customer feature requests by theme and strategic fit
- `opportunity-solution-tree` — Build an Opportunity Solution Tree (Teresa Torres) — outcome → opportunities → solutions → experiments
- `interview-script` — Create a structured customer interview script with JTBD probing questions
- `summarize-interview` — Summarize an interview transcript into JTBD, satisfaction signals, and action items
- `metrics-dashboard` — Design a product metrics dashboard with North Star, input metrics, and alert thresholds

**Commands (5):**

- `/discover` — Full discovery cycle: ideation → assumption mapping → prioritization → experiment design
- `/brainstorm` — Multi-perspective ideation (`ideas|experiments` × `existing|new`)
- `/triage-requests` — Analyze and prioritize a batch of feature requests
- `/interview` — Prepare an interview script or summarize a transcript (`prep|summarize`)
- `/setup-metrics` — Design a product metrics dashboard

**Examples:**

Skills:
- `What are the riskiest assumptions for our AI writing assistant idea?`
- `Help me build an Opportunity Solution Tree for improving user activation`
- `Prioritize these 12 feature requests from our enterprise customers [attach CSV]`

Commands:
- `/discover AI-powered meeting summarizer for remote teams`
- `/brainstorm experiments existing — We need to reduce churn in our onboarding flow`
- `/interview prep — We're interviewing enterprise buyers about their procurement workflow`

</details>

<details>
<summary><strong>2. pm-product-strategy</strong> — Vision, business models, pricing, competitive landscape (12 skills, 5 commands)</summary>

Product strategy, vision, business models, pricing, and macro environment analysis. Covers the full strategic toolkit from vision crafting through competitive landscape scanning.

**Skills (12):**

- `product-strategy` — Comprehensive 9-section Product Strategy Canvas (vision → defensibility)
- `startup-canvas` — Startup Canvas combining Product Strategy (9 sections) + Business Model — an alternative to BMC and Lean Canvas for new products
- `product-vision` — Craft an inspiring, achievable, and emotional product vision
- `value-proposition` — 6-part JTBD value proposition (Who, Why, What before, How, What after, Alternatives)
- `lean-canvas` — Lean Canvas business model for startups and new products
- `business-model` — Business Model Canvas with all 9 building blocks
- `monetization-strategy` — Brainstorm 3–5 monetization strategies with validation experiments
- `pricing-strategy` — Pricing models, competitive analysis, willingness-to-pay, and price elasticity
- `swot-analysis` — SWOT analysis with actionable recommendations
- `pestle-analysis` — Macro environment: Political, Economic, Social, Technological, Legal, Environmental
- `porters-five-forces` — Competitive forces analysis (rivalry, suppliers, buyers, substitutes, new entrants)
- `ansoff-matrix` — Growth strategy mapping across markets and products

**Commands (5):**

- `/strategy` — Create a complete 9-section Product Strategy Canvas
- `/business-model` — Explore business models (`lean|full|startup|value-prop|all`)
- `/value-proposition` — Design a value proposition using the 6-part JTBD template
- `/market-scan` — Macro environment analysis combining SWOT + PESTLE + Porter's + Ansoff
- `/pricing` — Design a pricing strategy with competitive analysis and experiments

**Examples:**

Skills:
- `Compare Lean Canvas vs Business Model Canvas vs Startup Canvas for my marketplace startup`
- `Design a value proposition for our AI writing assistant targeting non-native English speakers`
- `Run a Porter's Five Forces analysis for the project management SaaS market`

Commands:
- `/strategy B2B project management tool for agencies`
- `/business-model startup — AI writing tool for non-native English speakers`
- `/value-proposition SaaS onboarding tool for enterprise customers`

</details>

<details>
<summary><strong>3. pm-execution</strong> — PRDs, OKRs, roadmaps, sprints, retros, release notes, stakeholder management (15 skills, 10 commands)</summary>

Day-to-day product management: PRDs, OKRs, roadmaps, sprints, retrospectives, release notes, pre-mortems, stakeholder management, user stories, and prioritization frameworks.

**Skills (15):**

- `create-prd` — Comprehensive 8-section PRD template
- `brainstorm-okrs` — Team-level OKRs aligned with company objectives
- `outcome-roadmap` — Transform a feature list into an outcome-focused roadmap
- `sprint-plan` — Sprint planning with capacity estimation, story selection, and risk identification
- `retro` — Structured sprint retrospective facilitation
- `release-notes` — User-facing release notes from tickets, PRDs, or changelogs
- `pre-mortem` — Risk analysis with Tigers/Paper Tigers/Elephants classification
- `stakeholder-map` — Power × Interest grid with tailored communication plan
- `summarize-meeting` — Meeting transcript → decisions + action items
- `user-stories` — User stories following the 3 C's and INVEST criteria
- `job-stories` — Job stories: When [situation], I want to [motivation], so I can [outcome]
- `wwas` — Product backlog items in Why-What-Acceptance format
- `test-scenarios` — Test scenarios: happy paths, edge cases, error handling
- `dummy-dataset` — Realistic dummy datasets as CSV, JSON, SQL, or Python
- `prioritization-frameworks` — Reference guide to 9 prioritization frameworks (Opportunity Score, ICE, RICE, MoSCoW, Kano, etc.)

**Commands (10):**

- `/write-prd` — Create a PRD from a feature idea or problem statement
- `/plan-okrs` — Brainstorm team-level OKRs
- `/transform-roadmap` — Convert a feature-based roadmap into outcome-focused
- `/sprint` — Sprint lifecycle (`plan|retro|release`)
- `/pre-mortem` — Pre-mortem risk analysis on a PRD or launch plan
- `/meeting-notes` — Summarize a meeting transcript into structured notes
- `/stakeholder-map` — Map stakeholders and create a communication plan
- `/write-stories` — Break features into backlog items (`user|job|wwa`)
- `/test-scenarios` — Generate test scenarios from user stories
- `/generate-data` — Create realistic dummy datasets

**Examples:**

Skills:
- `Which prioritization framework should I use for a 50-item backlog?`
- `Map our stakeholders for the platform migration project`
- `What's the difference between Opportunity Score, ICE, and RICE?`

Commands:
- `/write-prd Smart notification system that reduces alert fatigue`
- `/sprint retro — Here are the notes from our last sprint`
- `/write-stories job — Break down the "team dashboard" feature into job stories`

</details>

<details>
<summary><strong>4. pm-market-research</strong> — Personas, segmentation, journey maps, market sizing, competitor analysis (7 skills, 3 commands)</summary>

User research and competitive analysis: personas, segmentation, journey maps, market sizing, competitor analysis, and feedback analysis.

**Skills (7):**

- `user-personas` — Create refined user personas from research data
- `market-segments` — Identify 3–5 customer segments with demographics, JTBD, and product fit
- `user-segmentation` — Segment users from feedback data based on behavior, JTBD, and needs
- `customer-journey-map` — End-to-end journey map with stages, touchpoints, emotions, and pain points
- `market-sizing` — TAM, SAM, SOM with top-down and bottom-up approaches
- `competitor-analysis` — Competitor strengths, weaknesses, and differentiation opportunities
- `sentiment-analysis` — Sentiment analysis and theme extraction from user feedback

**Commands (3):**

- `/research-users` — Build personas, segment users, and map the customer journey
- `/competitive-analysis` — Analyze the competitive landscape
- `/analyze-feedback` — Sentiment analysis and segment insights from user feedback

**Examples:**

Skills:
- `Estimate TAM/SAM/SOM for an AI code review tool in the US market`
- `Create a customer journey map for our e-commerce checkout flow`
- `Segment these survey respondents by behavior and needs [attach CSV]`

Commands:
- `/research-users We have interview data from 12 users of our fitness app`
- `/competitive-analysis Figma competitors in the design tool space`
- `/analyze-feedback Here's 200 NPS responses from Q4 [attach file]`

</details>

<details>
<summary><strong>5. pm-data-analytics</strong> — SQL generation, cohort analysis, A/B test analysis (3 skills, 3 commands)</summary>

Data analytics for PMs: SQL query generation, cohort analysis, and A/B test analysis.

**Skills (3):**

- `sql-queries` — Generate SQL from natural language (BigQuery, PostgreSQL, MySQL)
- `cohort-analysis` — Retention curves, feature adoption, and engagement trends by cohort
- `ab-test-analysis` — Statistical significance, sample size validation, and ship/extend/stop recommendations

**Commands (3):**

- `/write-query` — Generate SQL queries from natural language
- `/analyze-cohorts` — Cohort analysis on user engagement data
- `/analyze-test` — Analyze A/B test results

**Examples:**

Skills:
- `How large a sample do I need for 95% confidence with a 2% MDE?`
- `What retention metrics should I track for a subscription app?`

Commands:
- `/write-query Show me monthly active users by country for Q4 2025 (BigQuery)`
- `/analyze-test Here are the results from our checkout flow A/B test [attach CSV]`
- `/analyze-cohorts Weekly retention for users who signed up in January vs February`

</details>

<details>
<summary><strong>6. pm-go-to-market</strong> — Beachhead segments, ICPs, messaging, growth loops, GTM motions, battlecards (6 skills, 3 commands)</summary>

Go-to-market strategy: beachhead segments, ideal customer profiles, messaging, growth loops, GTM motions, and competitive battlecards.

**Skills (6):**

- `gtm-strategy` — Full GTM strategy: channels, messaging, success metrics, and launch plan
- `beachhead-segment` — Identify the first beachhead market segment
- `ideal-customer-profile` — ICP with demographics, behaviors, JTBD, and needs
- `growth-loops` — Design sustainable growth loops (flywheels)
- `gtm-motions` — Evaluate GTM motions and tools (product-led, sales-led, etc.)
- `competitive-battlecard` — Sales-ready battlecard with objection handling and win strategies

**Commands (3):**

- `/plan-launch` — Full GTM strategy from beachhead to launch plan
- `/growth-strategy` — Design growth loops and evaluate GTM motions
- `/battlecard` — Create a competitive battlecard

**Examples:**

Skills:
- `What's the best beachhead segment for a developer productivity tool?`
- `Design a growth loop for a B2B SaaS with a freemium tier`
- `Define our ICP for an AI-powered HR screening platform`

Commands:
- `/plan-launch AI code review tool targeting mid-size engineering teams`
- `/battlecard Our CRM vs Salesforce for the SMB market`
- `/growth-strategy Two-sided marketplace for connecting freelancers with startups`

</details>

<details>
<summary><strong>7. pm-marketing-growth</strong> — Marketing ideas, positioning, value props, naming, North Star metrics (5 skills, 2 commands)</summary>

Product marketing and growth: marketing ideas, positioning, value proposition statements, product naming, and North Star metrics.

**Skills (5):**

- `marketing-ideas` — Creative, cost-effective marketing ideas with channels and messaging
- `positioning-ideas` — Product positioning differentiated from competitors
- `value-prop-statements` — Value proposition statements for marketing, sales, and onboarding
- `product-name` — Product name brainstorming aligned to brand values and audience
- `north-star-metric` — North Star Metric + input metrics with business game classification

**Commands (2):**

- `/market-product` — Brainstorm marketing ideas, positioning, value props, and product names
- `/north-star` — Define your North Star Metric and supporting input metrics

**Examples:**

Skills:
- `Brainstorm 5 positioning angles that differentiate us from Notion`
- `What's a good North Star Metric for a two-sided marketplace?`
- `Generate value prop statements for our sales team's pitch deck`

Commands:
- `/market-product B2B analytics dashboard for e-commerce managers`
- `/north-star Two-sided marketplace connecting freelancers with clients`

</details>

<details>
<summary><strong>8. pm-toolkit</strong> — Resume review, legal documents, proofreading (4 skills, 5 commands)</summary>

PM utilities beyond core product work: resume review, legal documents, and proofreading.

**Skills (4):**

- `review-resume` — PM resume review and tailoring against 10 best practices (XYZ+S formula, keywords, structure)
- `draft-nda` — Non-Disclosure Agreement with jurisdiction-appropriate clauses
- `privacy-policy` — Privacy policy covering GDPR/CCPA compliance
- `grammar-check` — Grammar, logic, and flow checking with targeted fixes

**Commands (5):**

- `/review-resume` — Comprehensive PM resume review
- `/tailor-resume` — Tailor a resume to a specific job description
- `/draft-nda` — Draft an NDA
- `/privacy-policy` — Draft a privacy policy
- `/proofread` — Check grammar, logic, and flow

**Examples:**

Skills:
- `Review my PM resume against best practices [attach PDF]`
- `Check this product announcement for grammar and clarity`

Commands:
- `/review-resume [attach your PM resume]`
- `/tailor-resume [attach resume + paste job description]`
- `/proofread Here's the draft of our Q1 investor update`

</details>

---

## About

This marketplace evolves with product practice and AI capabilities.

Selected skills based on the work of:

- Teresa Torres — [*Continuous Discovery Habits*](https://www.amazon.com/Continuous-Discovery-Habits-Discover-Products/dp/1736633309/)
- Marty Cagan — [*INSPIRED*](https://www.amazon.com/INSPIRED-Create-Tech-Products-Customers/dp/1119387507/) and [*TRANSFORMED*](https://www.amazon.com/dp/1119697336/)
- Alberto Savoia — [*The Right It*](https://www.amazon.com/Right-Many-Ideas-Yours-Succeed/dp/0062884654)
- Dan Olsen — [*The Lean Product Playbook*](https://www.amazon.com/dp/1118960874/)
- Roger L. Martin — [*Playing to Win*](https://www.amazon.com/Playing-Win-Expanded-Bonus-Articles/dp/B0F25SDYWV/)
- Ash Maurya — [*Running Lean*](https://www.amazon.com/dp/B004J4XGN6/)
- Strategyzer — [*Business Model Generation*](https://www.amazon.com/dp/0470876417/) and [*Value Proposition Design*](https://www.amazon.com/dp/1118968050/)
- Christina Wodtke — [*Radical Focus*](https://www.amazon.com/Radical-Focus-Achieving-Important-Objectives/dp/0996006052)
- Anthony W. Ulwick — [*Jobs to Be Done*](https://jobs-to-be-done-book.com/)
- Alistair Croll & Benjamin Yoskovitz — [*Lean Analytics*](https://www.amazon.com/Lean-Analytics-Better-Startup-Faster/dp/1449335675/)
- Sean Ellis — [*Hacking Growth*](https://www.amazon.com/Hacking-Growth-Fastest-Growing-Companies-Breakout/dp/045149721X/)
- Maja Voje — [*Go-To-Market Strategist*](https://gtmstrategist.com/)

Curated by Paweł Huryn from [The Product Compass Newsletter](https://www.productcompass.pm).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Known Issue on Windows

If your Cowork is unstable and can't start a VM ([claude-code/issues/27010](https://github.com/anthropics/claude-code/issues/27010)), try:

```powershell
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-WindowStyle Hidden -Command `"if ((Get-Service CoworkVMService).Status -ne 'Running') { Start-Service CoworkVMService }`""

$trigger = New-ScheduledTaskTrigger -RepetitionInterval (New-TimeSpan -Minutes 1) -Once -At (Get-Date)

$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries

Register-ScheduledTask -TaskName "CoworkVMServiceMonitor" `
  -Action $action `
  -Trigger $trigger `
  -Settings $settings `
  -RunLevel Highest `
  -User "SYSTEM"
```

It solves 90% of the issues on Windows.
The remaining 10%: open services.msc > start "Claude" service manually

## License

MIT — see [LICENSE](LICENSE).
```

## File: `validate_plugins.py`
```python
#!/usr/bin/env python3
"""
Plugin Collection Validator
===========================
Validates all plugins in the collection against the Claude Code plugin spec:
- plugin.json manifest: required fields, author attribution, keywords
- Skills: YAML frontmatter (name must match directory, description required)
- Commands: YAML frontmatter (description and argument-hint required)
- Cross-references: commands referencing skills that exist in the same plugin
- README: exists and has expected sections

Based on:
- Anthropic plugin-dev README (https://github.com/anthropics/claude-code/tree/main/plugins/plugin-dev)
- agentskills.io specification
- Claude Code plugins reference (https://code.claude.com/docs/en/plugins-reference)

Author: Paweł Huryn — The Product Compass Newsletter (https://www.productcompass.pm)
"""

import json
import os
import re
import sys
from pathlib import Path
from typing import Optional


# ─── Configuration ───────────────────────────────────────────────────────────

# Required plugin.json fields per spec
REQUIRED_MANIFEST_FIELDS = ["name", "version", "description"]
RECOMMENDED_MANIFEST_FIELDS = ["author", "keywords", "homepage", "license"]
REQUIRED_AUTHOR_FIELDS = ["name", "email"]
RECOMMENDED_AUTHOR_FIELDS = ["url"]

# Required skill frontmatter fields
REQUIRED_SKILL_FIELDS = ["name", "description"]

# Required command frontmatter fields
REQUIRED_COMMAND_FIELDS = ["description"]
RECOMMENDED_COMMAND_FIELDS = ["argument-hint"]

# Expected README sections (case-insensitive substring match)
EXPECTED_README_SECTIONS = ["overview", "install", "skill", "command"]


# ─── ANSI Colors ─────────────────────────────────────────────────────────────

class C:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"


# ─── Helpers ─────────────────────────────────────────────────────────────────

def parse_yaml_frontmatter(content: str) -> Optional[dict]:
    """Extract YAML frontmatter from a markdown file (between --- markers)."""
    if not content.startswith("---"):
        return None
    end = content.find("---", 3)
    if end == -1:
        return None
    fm_text = content[3:end].strip()
    # Simple YAML parser for flat key-value pairs
    result = {}
    for line in fm_text.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        match = re.match(r'^(\S+):\s*(.+)$', line)
        if match:
            key = match.group(1)
            value = match.group(2).strip().strip('"').strip("'")
            result[key] = value
    return result


def count_words(content: str) -> int:
    """Count words in markdown content (excluding frontmatter)."""
    # Strip frontmatter
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            content = content[end + 3:]
    return len(content.split())


# ─── Validators ──────────────────────────────────────────────────────────────

class ValidationResult:
    def __init__(self):
        self.errors: list[str] = []      # Must fix
        self.warnings: list[str] = []    # Should fix
        self.info: list[str] = []        # FYI

    def error(self, msg: str):
        self.errors.append(msg)

    def warn(self, msg: str):
        self.warnings.append(msg)

    def note(self, msg: str):
        self.info.append(msg)

    @property
    def ok(self) -> bool:
        return len(self.errors) == 0


def validate_manifest(plugin_dir: str) -> ValidationResult:
    """Validate plugin.json manifest."""
    result = ValidationResult()
    pj_path = os.path.join(plugin_dir, ".claude-plugin", "plugin.json")

    if not os.path.isfile(pj_path):
        result.error("Missing .claude-plugin/plugin.json")
        return result

    try:
        with open(pj_path, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        result.error(f"Invalid JSON in plugin.json: {e}")
        return result

    # Required fields
    for field in REQUIRED_MANIFEST_FIELDS:
        if field not in data or not data[field]:
            result.error(f"Missing required field: {field}")

    # Name must match directory name
    dir_name = os.path.basename(plugin_dir)
    if data.get("name") and data["name"] != dir_name:
        result.error(f"Name mismatch: plugin.json says '{data['name']}' but directory is '{dir_name}'")

    # Version format
    version = data.get("version", "")
    if version and not re.match(r'^\d+\.\d+\.\d+$', version):
        result.warn(f"Version '{version}' doesn't follow semver (x.y.z)")

    # Recommended fields
    for field in RECOMMENDED_MANIFEST_FIELDS:
        if field not in data:
            result.warn(f"Missing recommended field: {field}")

    # Author validation
    author = data.get("author")
    if isinstance(author, dict):
        for field in REQUIRED_AUTHOR_FIELDS:
            if field not in author or not author[field]:
                result.warn(f"Missing author.{field}")
        for field in RECOMMENDED_AUTHOR_FIELDS:
            if field not in author:
                result.note(f"Missing author.{field}")
    elif author is not None:
        result.warn("Author should be an object with name, email, url fields")

    # Keywords validation
    keywords = data.get("keywords", [])
    if not keywords:
        result.warn("No keywords defined")
    elif not isinstance(keywords, list):
        result.error("Keywords must be an array")

    # Description length check
    desc = data.get("description", "")
    if desc and len(desc) < 20:
        result.warn(f"Description is very short ({len(desc)} chars)")

    result.note(f"Version: {version}")
    result.note(f"Keywords: {len(keywords) if isinstance(keywords, list) else 0}")

    return result


def validate_skill(skill_dir: str) -> ValidationResult:
    """Validate a single skill directory."""
    result = ValidationResult()
    skill_name = os.path.basename(skill_dir)
    skill_md = os.path.join(skill_dir, "SKILL.md")

    if not os.path.isfile(skill_md):
        result.error("Missing SKILL.md")
        return result

    with open(skill_md, "r", encoding="utf-8") as f:
        content = f.read()

    # Frontmatter check
    fm = parse_yaml_frontmatter(content)
    if fm is None:
        result.error("Missing YAML frontmatter (must start with ---)")
        return result

    # Required fields
    for field in REQUIRED_SKILL_FIELDS:
        if field not in fm or not fm[field]:
            result.error(f"Missing required frontmatter field: {field}")

    # Name must match directory name (agentskills.io spec)
    if fm.get("name") and fm["name"] != skill_name:
        result.error(f"Name mismatch: frontmatter says '{fm['name']}' but directory is '{skill_name}'")

    # Description quality
    desc = fm.get("description", "")
    if desc:
        if len(desc) < 30:
            result.warn(f"Description is very short ({len(desc)} chars)")
        # Check for trigger phrases (recommended)
        trigger_keywords = ["trigger", "use when", "use for"]
        has_triggers = any(kw in desc.lower() for kw in trigger_keywords)
        if not has_triggers:
            result.note("Description lacks explicit trigger phrases (e.g., 'Triggers: ...')")

    # Word count
    word_count = count_words(content)
    result.note(f"Word count: {word_count}")
    if word_count > 3000:
        result.warn(f"Skill is quite long ({word_count} words). Consider progressive disclosure with references/")
    elif word_count < 50:
        result.warn(f"Skill is very short ({word_count} words). May need more content.")

    return result


def validate_command(cmd_path: str) -> ValidationResult:
    """Validate a single command file."""
    result = ValidationResult()

    with open(cmd_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Frontmatter check
    fm = parse_yaml_frontmatter(content)
    if fm is None:
        result.error("Missing YAML frontmatter (must start with ---)")
        return result

    # Required fields
    for field in REQUIRED_COMMAND_FIELDS:
        if field not in fm or not fm[field]:
            result.error(f"Missing required frontmatter field: {field}")

    # Recommended fields
    for field in RECOMMENDED_COMMAND_FIELDS:
        if field not in fm or not fm[field]:
            result.warn(f"Missing recommended frontmatter field: {field}")

    # Description quality
    desc = fm.get("description", "")
    if desc and len(desc) < 10:
        result.warn(f"Description is very short ({len(desc)} chars)")

    # Check if command references skills (informational)
    skill_refs = re.findall(r'\*\*(\w[\w-]+)\*\*\s+skill', content)
    if skill_refs:
        result.note(f"References skills: {', '.join(skill_refs)}")

    return result


def validate_readme(plugin_dir: str) -> ValidationResult:
    """Validate plugin README.md."""
    result = ValidationResult()
    readme_path = os.path.join(plugin_dir, "README.md")

    if not os.path.isfile(readme_path):
        result.warn("Missing README.md")
        return result

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read().lower()

    # Check for expected sections
    for section in EXPECTED_README_SECTIONS:
        if section not in content:
            result.note(f"README may be missing '{section}' section")

    result.note(f"README: {count_words(content)} words")
    return result


def validate_cross_references(plugin_dir: str, skill_names: list[str]) -> ValidationResult:
    """Check that commands reference skills that actually exist in this plugin."""
    result = ValidationResult()
    cmds_dir = os.path.join(plugin_dir, "commands")

    if not os.path.isdir(cmds_dir):
        return result

    for cmd_file in sorted(os.listdir(cmds_dir)):
        if not cmd_file.endswith(".md"):
            continue
        cmd_path = os.path.join(cmds_dir, cmd_file)
        with open(cmd_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Find skill references like **skill-name** skill
        refs = re.findall(r'\*\*(\w[\w-]+)\*\*\s+skill', content)
        for ref in refs:
            if ref not in skill_names:
                result.warn(f"Command {cmd_file} references skill '{ref}' not found in this plugin")

    return result


# ─── Main Validator ──────────────────────────────────────────────────────────

def validate_plugin(plugin_dir: str) -> dict:
    """Run all validations on a single plugin."""
    plugin_name = os.path.basename(plugin_dir)
    results = {"name": plugin_name, "sections": {}}

    # 1. Manifest
    results["sections"]["manifest"] = validate_manifest(plugin_dir)

    # 2. Skills
    skills_dir = os.path.join(plugin_dir, "skills")
    skill_names = []
    skill_results = {}
    if os.path.isdir(skills_dir):
        for skill_name in sorted(os.listdir(skills_dir)):
            skill_path = os.path.join(skills_dir, skill_name)
            if os.path.isdir(skill_path):
                skill_names.append(skill_name)
                skill_results[skill_name] = validate_skill(skill_path)
    results["sections"]["skills"] = skill_results
    results["skill_count"] = len(skill_names)

    # 3. Commands
    cmds_dir = os.path.join(plugin_dir, "commands")
    cmd_results = {}
    if os.path.isdir(cmds_dir):
        for cmd_file in sorted(os.listdir(cmds_dir)):
            if cmd_file.endswith(".md"):
                cmd_path = os.path.join(cmds_dir, cmd_file)
                cmd_results[cmd_file] = validate_command(cmd_path)
    results["sections"]["commands"] = cmd_results
    results["command_count"] = len(cmd_results)

    # 4. README
    results["sections"]["readme"] = validate_readme(plugin_dir)

    # 5. Cross-references
    results["sections"]["cross-refs"] = validate_cross_references(plugin_dir, skill_names)

    return results


def print_validation_result(label: str, vr: ValidationResult, indent: int = 4):
    """Print a single validation result."""
    prefix = " " * indent
    if vr.errors:
        for e in vr.errors:
            print(f"{prefix}{C.RED}✗ ERROR:{C.RESET} {e}")
    if vr.warnings:
        for w in vr.warnings:
            print(f"{prefix}{C.YELLOW}⚠ WARN:{C.RESET}  {w}")
    if vr.info:
        for i in vr.info:
            print(f"{prefix}{C.DIM}ℹ {i}{C.RESET}")


def print_report(all_results: list[dict]):
    """Print the full validation report."""
    total_errors = 0
    total_warnings = 0
    total_skills = 0
    total_commands = 0

    print(f"\n{C.BOLD}{'='*70}")
    print(f" Plugin Collection Validator — Report")
    print(f"{'='*70}{C.RESET}\n")

    for plugin in all_results:
        name = plugin["name"]
        sc = plugin["skill_count"]
        cc = plugin["command_count"]
        total_skills += sc
        total_commands += cc

        # Count errors/warnings for this plugin
        p_errors = 0
        p_warnings = 0
        for key, section in plugin["sections"].items():
            if isinstance(section, ValidationResult):
                p_errors += len(section.errors)
                p_warnings += len(section.warnings)
            elif isinstance(section, dict):
                for vr in section.values():
                    p_errors += len(vr.errors)
                    p_warnings += len(vr.warnings)

        total_errors += p_errors
        total_warnings += p_warnings

        # Plugin header
        status = f"{C.GREEN}✓ PASS{C.RESET}" if p_errors == 0 else f"{C.RED}✗ FAIL{C.RESET}"
        warn_str = f" {C.YELLOW}({p_warnings} warnings){C.RESET}" if p_warnings > 0 else ""
        print(f"{C.BOLD}{C.CYAN}┌─ {name}{C.RESET}  [{sc} skills, {cc} commands]  {status}{warn_str}")

        # Manifest
        manifest = plugin["sections"]["manifest"]
        if manifest.errors or manifest.warnings:
            print(f"  {C.BOLD}Manifest:{C.RESET}")
            print_validation_result("manifest", manifest)

        # Skills with issues
        skill_results = plugin["sections"]["skills"]
        skills_with_issues = {k: v for k, v in skill_results.items() if v.errors or v.warnings}
        if skills_with_issues:
            print(f"  {C.BOLD}Skills with issues:{C.RESET}")
            for sname, vr in skills_with_issues.items():
                print(f"    {sname}:")
                print_validation_result(sname, vr, indent=6)

        # Commands with issues
        cmd_results = plugin["sections"]["commands"]
        cmds_with_issues = {k: v for k, v in cmd_results.items() if v.errors or v.warnings}
        if cmds_with_issues:
            print(f"  {C.BOLD}Commands with issues:{C.RESET}")
            for cname, vr in cmds_with_issues.items():
                print(f"    {cname}:")
                print_validation_result(cname, vr, indent=6)

        # README
        readme = plugin["sections"]["readme"]
        if readme.errors or readme.warnings:
            print(f"  {C.BOLD}README:{C.RESET}")
            print_validation_result("readme", readme)

        # Cross-references
        xrefs = plugin["sections"]["cross-refs"]
        if xrefs.errors or xrefs.warnings:
            print(f"  {C.BOLD}Cross-references:{C.RESET}")
            print_validation_result("cross-refs", xrefs)

        print(f"{C.CYAN}└{'─'*69}{C.RESET}\n")

    # Summary
    print(f"{C.BOLD}{'='*70}")
    print(f" Summary")
    print(f"{'='*70}{C.RESET}")
    print(f"  Plugins:   {len(all_results)}")
    print(f"  Skills:    {total_skills}")
    print(f"  Commands:  {total_commands}")
    print(f"  Total:     {total_skills + total_commands} components")
    print()
    if total_errors == 0:
        print(f"  {C.GREEN}{C.BOLD}✓ ALL CHECKS PASSED{C.RESET} ({total_warnings} warnings)")
    else:
        print(f"  {C.RED}{C.BOLD}✗ {total_errors} ERRORS{C.RESET}, {total_warnings} warnings")
    print()

    return total_errors


def main():
    """Find and validate all plugins in the collection."""
    # Ensure UTF-8 output on Windows
    if sys.platform == 'win32':
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # Determine base path
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    if not os.path.isdir(base_path):
        print(f"Error: {base_path} is not a directory")
        sys.exit(1)

    # Find all plugin directories (those containing .claude-plugin/)
    plugin_dirs = []
    for entry in sorted(os.listdir(base_path)):
        full_path = os.path.join(base_path, entry)
        if os.path.isdir(full_path) and os.path.isdir(os.path.join(full_path, ".claude-plugin")):
            plugin_dirs.append(full_path)

    if not plugin_dirs:
        print(f"No plugins found in {base_path}")
        print("(Looking for directories containing .claude-plugin/)")
        sys.exit(1)

    print(f"Found {len(plugin_dirs)} plugins in {base_path}\n")

    # Validate each plugin
    all_results = []
    for pd in plugin_dirs:
        all_results.append(validate_plugin(pd))

    # Print report
    errors = print_report(all_results)

    sys.exit(1 if errors > 0 else 0)


if __name__ == "__main__":
    main()
```

## File: `pm-data-analytics/README.md`
```markdown
# pm-data-analytics

Data analytics skills for PMs: SQL query generation and cohort analysis. Analyze user data, generate queries, and identify retention patterns.

## Skills (3)

- **ab-test-analysis** — Analyze A/B test results with statistical significance, sample size validation, confidence intervals, and actionable recommendations.
- **cohort-analysis** — Perform cohort analysis on user engagement data.
- **sql-queries** — Generate SQL queries from natural language descriptions.

## Commands (3)

- `/pm-data-analytics:analyze-cohorts` — Perform cohort analysis on user data — retention curves, feature adoption, and engagement trends.
- `/pm-data-analytics:analyze-test` — Analyze A/B test results — statistical significance, sample size validation, and ship/extend/stop recommendations.
- `/pm-data-analytics:write-query` — Generate SQL queries from natural language — supports BigQuery, PostgreSQL, MySQL, and more.

## Author

Paweł Huryn — [The Product Compass Newsletter](https://www.productcompass.pm)

## License

MIT
```

## File: `pm-data-analytics/commands/analyze-cohorts.md`
```markdown
---
description: Perform cohort analysis on user data — retention curves, feature adoption, and engagement trends
argument-hint: "<data file or description of what to analyze>"
---

# /analyze-cohorts -- Cohort Analysis

Analyze user retention and engagement patterns by cohort. Upload your data or describe what you need, and get retention curves, feature adoption trends, and actionable insights.

## Invocation

```
/analyze-cohorts [upload a CSV of user activity data]
/analyze-cohorts Monthly retention for users who signed up in Jan-Jun, grouped by acquisition channel
/analyze-cohorts Help me set up a cohort analysis for our onboarding redesign
```

## Workflow

### Step 1: Accept Data or Define Analysis

Two paths:
- **With data**: User uploads a CSV/spreadsheet with user-level data (user_id, signup_date, activity_date, event_type, etc.)
- **Without data**: User describes the analysis they need → generate the SQL query and analysis framework

### Step 2: Define Cohorts

Ask:
- What defines a cohort? (signup week/month, acquisition channel, plan tier, first feature used)
- What is the retention event? (login, core action, any activity, purchase)
- What time granularity? (daily, weekly, monthly)
- What time range?

### Step 3: Analyze

Apply the **cohort-analysis** skill:

**If data is provided:**
- Process the data using Python (pandas) to create cohort tables
- Calculate retention rates per cohort per period
- Generate retention curves
- Identify patterns: improving/declining cohorts, seasonal effects, anomalies
- Compare feature adoption across cohorts

**If describing an analysis:**
- Design the cohort analysis framework
- Generate SQL queries to extract the data
- Create a template spreadsheet for the analysis
- Define the metrics and visualization approach

### Step 4: Generate Report

```
## Cohort Analysis: [Description]

**Date**: [today]
**Cohort definition**: [e.g., signup month]
**Retention event**: [e.g., completed a project]
**Granularity**: [weekly/monthly]

### Retention Table
| Cohort | Size | Week 1 | Week 2 | Week 3 | ... | Week 12 |
|--------|------|--------|--------|--------|-----|---------|

### Key Findings
1. **[Finding]** — [supporting data]
2. ...

### Cohort Comparison
- **Best-performing cohort**: [which, why]
- **Worst-performing cohort**: [which, why]
- **Trend**: [improving/declining/stable over time]

### Retention Benchmarks
| Period | Your Rate | Industry Benchmark | Gap |
|--------|----------|-------------------|-----|

### Recommendations
1. [What to investigate or change based on findings]
2. ...

### Follow-Up Queries
[SQL queries for deeper investigation]
```

If data was provided, save analysis as both markdown report and CSV/spreadsheet.

### Step 5: Offer Next Steps

- "Want me to **segment this further** by another dimension?"
- "Should I **set up metrics alerts** based on these retention thresholds?"
- "Want me to **design experiments** to improve retention for the weakest cohort?"

## Notes

- Cohort analysis is only as good as the retention event definition — push for a meaningful action, not just "logged in"
- Early cohorts often look different due to founding user bias — note this when comparing
- If retention is calculated using a Python script, save the script so the user can re-run with new data
- Seasonal effects can masquerade as trends — flag if cohort differences might be calendar-driven
```

## File: `pm-data-analytics/commands/analyze-test.md`
```markdown
---
description: Analyze A/B test results — statistical significance, sample size validation, and ship/extend/stop recommendations
argument-hint: "<test results as data, screenshot, or description>"
---

# /analyze-test -- A/B Test Analysis

Evaluate experiment results with statistical rigor and translate findings into a clear product decision: ship, extend, or stop.

## Invocation

```
/analyze-test Control: 4.2% conversion (n=5000), Variant: 4.8% conversion (n=5100)
/analyze-test [upload a CSV of test results]
/analyze-test [screenshot from your experimentation platform]
```

## Workflow

### Step 1: Accept Test Data

Accept in any format:
- Summary statistics (conversion rates, sample sizes per variant)
- Raw event data (CSV with user_id, variant, converted, timestamp)
- Screenshot from an experimentation platform (Optimizely, LaunchDarkly, etc.)
- Description of the experiment and results

### Step 2: Validate Test Design

Before analyzing results, check:
- Was sample size sufficient? (run a power analysis)
- Was the test run long enough? (capture weekly cycles, minimum 1-2 business cycles)
- Was randomization clean? (check for sample ratio mismatch)
- Were there any external factors during the test period?

Flag issues if found — results from a flawed test can be misleading.

### Step 3: Analyze Results

Apply the **ab-test-analysis** skill:

- **Statistical significance**: Calculate p-value and confidence interval
- **Effect size**: Absolute and relative difference between variants
- **Practical significance**: Is the effect large enough to matter for the business?
- **Confidence interval**: What's the range of plausible true effects?
- **Segment analysis**: If data allows, check for differential effects by user segment

### Step 4: Generate Analysis

```
## A/B Test Analysis: [Test Name]

**Date**: [today]
**Test duration**: [X days/weeks]
**Total sample**: [N users]

### Results Summary
| Variant | Sample | Metric | Rate | 95% CI |
|---------|--------|--------|------|--------|
| Control | [n] | [metric] | [X%] | [X% - Y%] |
| Variant | [n] | [metric] | [X%] | [X% - Y%] |

### Statistical Analysis
- **Relative lift**: [+X%] ([CI range])
- **P-value**: [X]
- **Statistically significant**: [Yes/No] at 95% confidence
- **Minimum detectable effect**: [X%] (what the test was powered to detect)

### Sample Size Check
- **Required sample**: [N] per variant (for [X%] MDE at 80% power)
- **Actual sample**: [N] per variant
- **Verdict**: [Sufficiently powered / Underpowered / Overpowered]

### Decision

**Recommendation: [SHIP / EXTEND / STOP]**

[Clear explanation of why, considering both statistical and practical significance]

### Business Impact Estimate
If shipped to 100% of users:
- **Expected impact**: [metric change per month/quarter]
- **Revenue impact**: [if applicable]
- **Confidence**: [How certain we are about this estimate]

### Caveats
- [Any concerns about the test validity]
- [Segments where results differ]
- [Novelty effects or other biases to consider]

### Follow-Up
- [What to test next based on learnings]
- [Monitoring plan if shipping the variant]
```

### Step 5: Offer Next Steps

- "Want me to **design a follow-up experiment** based on these findings?"
- "Should I **run the analysis for specific segments**?"
- "Want me to **generate the SQL** to monitor this metric post-launch?"

## Notes

- Statistical significance ≠ practical significance — a 0.1% lift can be significant with enough data but not worth shipping
- Always check for sample ratio mismatch before trusting results
- Novelty effects can inflate short-term results — recommend monitoring for 2-4 weeks post-launch
- If the test is underpowered, the right answer is usually "extend" not "no effect"
- For revenue metrics, use confidence intervals to estimate best-case and worst-case business impact
- If data is provided as CSV, generate the full analysis using Python with scipy.stats
```

## File: `pm-data-analytics/commands/write-query.md`
```markdown
---
description: Generate SQL queries from natural language — supports BigQuery, PostgreSQL, MySQL, and more
argument-hint: "<what you want to know, in plain English>"
---

# /write-query -- SQL Query Generator

Describe what data you need in plain English and get an optimized SQL query. Supports multiple dialects and can read your schema from uploaded files.

## Invocation

```
/write-query Show me daily active users for the last 30 days, broken down by plan tier
/write-query Find users who signed up last month but never completed onboarding
/write-query [upload a schema diagram] What's the conversion rate from trial to paid by cohort?
```

## Workflow

### Step 1: Understand the Question

Parse the user's natural language request to identify:
- What data is being requested (metrics, dimensions, filters)
- Time range and granularity
- Grouping and ordering preferences
- Output expectations (raw data, aggregated, ranked)

### Step 2: Determine Schema

If a schema is available (uploaded diagram, DDL, or description):
- Map the request to specific tables and columns
- Identify necessary joins

If no schema is provided:
- Ask for the database type (BigQuery, PostgreSQL, MySQL, etc.)
- Infer a reasonable schema from the question and ask the user to confirm
- Use common SaaS data model conventions as defaults

### Step 3: Generate Query

Apply the **sql-queries** skill:

- Write the SQL query in the correct dialect
- Optimize for readability and performance
- Include comments explaining key logic
- Add CTEs for complex queries to improve readability
- Handle edge cases (NULLs, timezone considerations, duplicate handling)

### Step 4: Present and Iterate

```
## SQL Query: [What It Does]

**Dialect**: [BigQuery / PostgreSQL / MySQL / etc.]
**Tables used**: [list]

### Query
[SQL code block with comments]

### What This Returns
[Description of the output: columns, rows, expected result shape]

### Assumptions
- [Schema assumptions made]
- [Business logic assumptions]

### Notes
- [Performance considerations for large datasets]
- [Edge cases handled or flagged]
```

Offer:
- "Want me to **modify this** — add filters, change grouping, extend the time range?"
- "Should I **create a companion query** for a related metric?"
- "Want me to **build a dashboard** around this query?"
- "Need a **cohort analysis** version of this?"

## Notes

- Always include comments in the SQL — PMs share queries with analysts who need to understand intent
- Default to readable over clever — CTEs over nested subqueries
- Flag queries that might be slow on large datasets and suggest optimization
- If the request is ambiguous (e.g., "active users"), ask the user to define the metric precisely
- Offer to generate the query in multiple dialects if the user is unsure which database they're using
```

## File: `pm-data-analytics/skills/ab-test-analysis/SKILL.md`
```markdown
---
name: ab-test-analysis
description: "Analyze A/B test results with statistical significance, sample size validation, confidence intervals, and ship/extend/stop recommendations. Use when evaluating experiment results, checking if a test reached significance, interpreting split test data, or deciding whether to ship a variant."
---

## A/B Test Analysis

Evaluate A/B test results with statistical rigor and translate findings into clear product decisions.

### Context

You are analyzing A/B test results for **$ARGUMENTS**.

If the user provides data files (CSV, Excel, or analytics exports), read and analyze them directly. Generate Python scripts for statistical calculations when needed.

### Instructions

1. **Understand the experiment**:
   - What was the hypothesis?
   - What was changed (the variant)?
   - What is the primary metric? Any guardrail metrics?
   - How long did the test run?
   - What is the traffic split?

2. **Validate the test setup**:
   - **Sample size**: Is the sample large enough for the expected effect size?
     - Use the formula: n = (Z²α/2 × 2 × p × (1-p)) / MDE²
     - Flag if the test is underpowered (<80% power)
   - **Duration**: Did the test run for at least 1-2 full business cycles?
   - **Randomization**: Any evidence of sample ratio mismatch (SRM)?
   - **Novelty/primacy effects**: Was there enough time to wash out initial behavior changes?

3. **Calculate statistical significance**:
   - **Conversion rate** for control and variant
   - **Relative lift**: (variant - control) / control × 100
   - **p-value**: Using a two-tailed z-test or chi-squared test
   - **Confidence interval**: 95% CI for the difference
   - **Statistical significance**: Is p < 0.05?
   - **Practical significance**: Is the lift meaningful for the business?

   If the user provides raw data, generate and run a Python script to calculate these.

4. **Check guardrail metrics**:
   - Did any guardrail metrics (revenue, engagement, page load time) degrade?
   - A winning primary metric with degraded guardrails may not be a true win

5. **Interpret results**:

   | Outcome | Recommendation |
   |---|---|
   | Significant positive lift, no guardrail issues | **Ship it** — roll out to 100% |
   | Significant positive lift, guardrail concerns | **Investigate** — understand trade-offs before shipping |
   | Not significant, positive trend | **Extend the test** — need more data or larger effect |
   | Not significant, flat | **Stop the test** — no meaningful difference detected |
   | Significant negative lift | **Don't ship** — revert to control, analyze why |

6. **Provide the analysis summary**:
   ```
   ## A/B Test Results: [Test Name]

   **Hypothesis**: [What we expected]
   **Duration**: [X days] | **Sample**: [N control / M variant]

   | Metric | Control | Variant | Lift | p-value | Significant? |
   |---|---|---|---|---|---|
   | [Primary] | X% | Y% | +Z% | 0.0X | Yes/No |
   | [Guardrail] | ... | ... | ... | ... | ... |

   **Recommendation**: [Ship / Extend / Stop / Investigate]
   **Reasoning**: [Why]
   **Next steps**: [What to do]
   ```

Think step by step. Save as markdown. Generate Python scripts for calculations if raw data is provided.

---

### Further Reading

- [A/B Testing 101 + Examples](https://www.productcompass.pm/p/ab-testing-101-for-pms)
- [Testing Product Ideas: The Ultimate Validation Experiments Library](https://www.productcompass.pm/p/the-ultimate-experiments-library)
- [Are You Tracking the Right Metrics?](https://www.productcompass.pm/p/are-you-tracking-the-right-metrics)
```

## File: `pm-data-analytics/skills/cohort-analysis/SKILL.md`
```markdown
---
name: cohort-analysis
description: "Perform cohort analysis on user engagement data — retention curves, feature adoption trends, and segment-level insights. Use when analyzing user retention by cohort, studying feature adoption over time, investigating churn patterns, or identifying engagement trends."
---

# Cohort Analysis & Retention Explorer

## Purpose
Analyze user engagement and retention patterns by cohort to identify trends in user behavior, feature adoption, and long-term engagement. Combine quantitative insights with qualitative research recommendations.

## How It Works

### Step 1: Read and Validate Your Data
- Accept CSV, Excel, or JSON data files with user cohort information
- Verify data structure: cohort identifier, time periods, engagement metrics
- Check for missing values and data quality issues
- Summarize key statistics (cohort sizes, date ranges, metrics available)

### Step 2: Generate Quantitative Analysis
- Calculate cohort retention rates and engagement trends
- Identify retention curves, drop-off patterns, and anomalies
- Compute feature adoption rates across cohorts
- Calculate month-over-month or period-over-period changes
- Generate Python analysis scripts using pandas and numpy if requested

### Step 3: Create Visualizations
- Generate retention heatmaps (cohorts vs. time periods)
- Create line charts showing cohort progression
- Build comparison charts for feature adoption
- Visualize drop-off points and engagement trends
- Output as interactive charts or static images

### Step 4: Identify Insights & Patterns
- Spot one or more significant patterns:
  - Early churn in specific cohorts
  - Late-stage engagement changes
  - Feature adoption clusters
  - Seasonal or temporal trends
- Highlight surprising findings and deviations
- Compare cohort performance to establish baselines

### Step 5: Suggest Follow-Up Research
- Recommend qualitative research methods:
  - Targeted user interviews with churning users
  - Feature usage surveys with engaged cohorts
  - Session replays of key interaction patterns
  - Win/loss analysis for high vs. low retention cohorts
- Design follow-up quantitative studies
- Suggest A/B tests or feature experiments

## Usage Examples

**Example 1: Upload CSV Data**
```
Upload cohort_engagement.csv with columns: cohort_month, weeks_active,
user_id, feature_x_usage, engagement_score

Request: "Analyze retention patterns and identify why Q4 2025 cohorts
underperform compared to Q3"
```

**Example 2: Describe Data Format**
```
"I have monthly user cohorts from Jan-Dec 2025. Each row shows:
cohort date, user ID, purchase frequency, and support tickets.
Analyze which cohorts show best long-term retention."
```

**Example 3: Feature Adoption Analysis**
```
Upload feature_usage.xlsx with cohort adoption data.

Request: "Compare adoption curves for our new feature across cohorts.
Which cohorts adopted fastest? Any patterns?"
```

## Key Capabilities

- **Data Reading**: Import CSV, Excel, JSON, SQL query results
- **Retention Analysis**: Calculate and visualize retention rates over time
- **Cohort Comparison**: Compare metrics across cohort groups
- **Anomaly Detection**: Flag unusual patterns or drop-offs
- **Python Scripts**: Generate reusable analysis code for ongoing analysis
- **Visualizations**: Create heatmaps, charts, and interactive dashboards
- **Research Design**: Suggest targeted follow-up studies and interview approaches
- **Statistical Summary**: Provide quantitative metrics and correlation analysis

## Tips for Best Results

1. **Include time dimension**: Provide data across multiple time periods
2. **Define cohort clearly**: Make cohort grouping explicit (signup month, feature launch date, etc.)
3. **Provide context**: Explain product changes, launches, or events during the period
4. **Multiple metrics**: Include retention, engagement, feature usage, revenue, etc.
5. **Sufficient data**: At least 3-4 cohorts for meaningful pattern identification
6. **Request specific output**: Ask for visualizations, Python scripts, or research recommendations

## Output Format

You'll receive:
- **Data Summary**: Cohort overview and data quality assessment
- **Quantitative Findings**: Key metrics, retention rates, and trend analysis
- **Visualizations**: Charts showing retention curves, adoption patterns
- **Pattern Identification**: 2-3 significant insights from the data
- **Research Recommendations**: Specific qualitative and quantitative follow-ups
- **Analysis Scripts** (if requested): Python code for reproducible analysis
- **Next Steps**: Prioritized actions based on findings

---

### Further Reading

- [Cohort Analysis 101: How to Reduce Churn and Make Better Product Decisions](https://www.productcompass.pm/p/cohort-analysis)
- [The Product Analytics Playbook: AARRR, HEART, Cohorts & Funnels for PMs](https://www.productcompass.pm/p/the-product-analytics-playbook-aarrr)
- [Are You Tracking the Right Metrics?](https://www.productcompass.pm/p/are-you-tracking-the-right-metrics)
```

## File: `pm-data-analytics/skills/sql-queries/SKILL.md`
```markdown
---
name: sql-queries
description: "Generate SQL queries from natural language descriptions. Supports BigQuery, PostgreSQL, MySQL, and other dialects. Reads database schemas from uploaded diagrams or documentation. Use when writing SQL, building data reports, exploring databases, or translating business questions into queries."
---

# SQL Query Generator

## Purpose
Transform natural language requirements into optimized SQL queries across multiple database platforms. This skill helps product managers, analysts, and engineers generate accurate queries without manual syntax work.

## How It Works

### Step 1: Understand Your Database Schema
- If you provide a schema file (SQL, documentation, or diagram description), I will read and analyze it
- Extract table names, column definitions, data types, and relationships
- Identify primary keys, foreign keys, and indexing strategies

### Step 2: Process Your Request
- Clarify the exact data you need to retrieve or analyze
- Confirm the SQL dialect (BigQuery, PostgreSQL, MySQL, Snowflake, etc.)
- Ask for any additional requirements (filters, aggregations, sorting)

### Step 3: Generate Optimized Query
- Write efficient SQL that leverages your database structure
- Include comments explaining complex logic
- Add performance considerations for large datasets
- Provide alternative approaches if applicable

### Step 4: Explain and Test
- Explain the query logic in plain English
- Suggest how to test or validate results
- Offer tips for performance optimization
- If you want, generate a test script or sample data

## Usage Examples

**Example 1: Query from Schema File**
```
Upload your database_schema.sql file and say:
"Generate a query to find users who signed up in the last 30 days
and had at least 5 active sessions"
```

**Example 2: Query from Diagram Description**
```
"Here's my database: Users table (id, email, created_at), Sessions table
(id, user_id, timestamp, duration). Generate a query for average session
duration per user in January 2026."
```

**Example 3: Complex Analysis Query**
```
"Create a BigQuery query to analyze our revenue by region and customer tier,
including year-over-year growth rates."
```

## Key Capabilities

- **Multi-Dialect Support**: Works with BigQuery, PostgreSQL, MySQL, Snowflake, SQL Server
- **File Reading**: Reads schema files, SQL dumps, and data documentation
- **Query Optimization**: Suggests indexes, partitioning, and performance improvements
- **Explanation**: Breaks down queries for learning and documentation
- **Testing**: Can generate test queries and sample data scripts
- **Script Execution**: Create executable SQL scripts for your database

## Tips for Best Results

1. **Provide context**: Share your database schema or structure
2. **Be specific**: Clearly describe what data you need and any filters
3. **Mention database**: Specify which SQL dialect you're using
4. **Include constraints**: Mention data volume, time ranges, and performance needs
5. **Request format**: Ask for the query result format if you need specific output

## Output Format

You'll receive:
- **SQL Query**: Production-ready SQL code with comments
- **Explanation**: What the query does and how it works
- **Performance Notes**: Optimization tips and considerations
- **Test Script** (if requested): Sample data and validation queries

---

### Further Reading

- [The Product Analytics Playbook: AARRR, HEART, Cohorts & Funnels for PMs](https://www.productcompass.pm/p/the-product-analytics-playbook-aarrr)
- [How to Become a Technology-Literate PM](https://www.productcompass.pm/p/how-to-become-a-technology-literate)
```

## File: `pm-execution/README.md`
```markdown
# pm-execution

Execution and product management skills: PRDs, OKRs, roadmaps, sprints, pre-mortems, stakeholder maps, user stories, prioritization frameworks, and more.

## Skills (15)

- **brainstorm-okrs** — Brainstorm team-level OKRs aligned with company objectives.
- **create-prd** — Create a Product Requirements Document using a comprehensive 8-section template covering summary, background, objectives, market segments, value propositions, solution details, and release planning.
- **dummy-dataset** — Generate realistic dummy datasets for testing with customizable columns, constraints, and output formats (CSV, JSON, SQL, Python script).
- **job-stories** — Create job stories using the 'When [situation], I want to [motivation], so I can [outcome]' format with detailed acceptance criteria.
- **outcome-roadmap** — Transform an output-focused roadmap into an outcome-focused one.
- **pre-mortem** — Run a pre-mortem analysis on a PRD.
- **prioritization-frameworks** — Reference guide to 9 prioritization frameworks with formulas, when-to-use guidance, and templates.
- **release-notes** — Generate user-facing release notes from tickets, PRDs, or changelogs.
- **retro** — Facilitate a structured sprint retrospective.
- **sprint-plan** — Plan a sprint with capacity estimation, story selection, dependency mapping, and risk identification.
- **stakeholder-map** — Build a stakeholder map using a power/interest grid, identify communication strategies per quadrant, and generate a communication plan.
- **summarize-meeting** — Summarize a meeting transcript into a structured template with date, participants, topic, summary points, and action items.
- **test-scenarios** — Create comprehensive test scenarios from user stories with test objectives, starting conditions, user roles, step-by-step actions, and expected outcomes.
- **user-stories** — Create user stories following the 3 C's (Card, Conversation, Confirmation) and INVEST criteria with descriptions, design links, and acceptance criteria.
- **wwas** — Create product backlog items in Why-What-Acceptance format.

## Commands (10)

- `/pm-execution:generate-data` — Generate realistic dummy datasets for testing — CSV, JSON, SQL inserts, or Python scripts.
- `/pm-execution:meeting-notes` — Summarize a meeting transcript into structured notes with decisions, action items, and follow-ups.
- `/pm-execution:plan-okrs` — Brainstorm team-level OKRs aligned with company objectives — qualitative objectives with measurable key results.
- `/pm-execution:pre-mortem` — Run a pre-mortem risk analysis on a PRD, launch plan, or feature — identify what could go wrong before it does.
- `/pm-execution:sprint` — Sprint lifecycle — plan a sprint, run a retrospective, or generate release notes.
- `/pm-execution:stakeholder-map` — Map stakeholders on a Power × Interest grid and create a tailored communication plan.
- `/pm-execution:test-scenarios` — Generate comprehensive test scenarios from user stories or feature specs — happy paths, edge cases, and error handling.
- `/pm-execution:transform-roadmap` — Convert a feature-based roadmap into an outcome-focused roadmap that communicates strategic intent.
- `/pm-execution:write-prd` — Create a comprehensive Product Requirements Document from a feature idea or problem statement.
- `/pm-execution:write-stories` — Break a feature into backlog items — user stories, job stories, or WWA format with acceptance criteria.

## Author

Paweł Huryn — [The Product Compass Newsletter](https://www.productcompass.pm)

## License

MIT
```

## File: `pm-execution/commands/generate-data.md`
```markdown
---
description: Generate realistic dummy datasets for testing — CSV, JSON, SQL inserts, or Python scripts
argument-hint: "<description of the data you need>"
---

# /generate-data -- Test Data Generator

Create realistic dummy datasets for development, testing, demos, or prototyping. Outputs as ready-to-use files in your preferred format.

## Invocation

```
/generate-data 1000 users with names, emails, plan tier, signup date, and activity score
/generate-data E-commerce orders dataset: products, customers, timestamps, amounts
/generate-data Sample data matching this schema: [paste table definition]
```

## Workflow

### Step 1: Define the Dataset

Understand:
- What entities? (users, orders, events, products, etc.)
- What columns? (with data types and constraints)
- How many rows?
- Any relationships between tables?
- Any specific distributions? (e.g., "80% should be on the free plan")
- Any realistic constraints? (emails should be unique, dates should be chronological)

### Step 2: Generate the Data

Apply the **dummy-dataset** skill:

- Create a Python script that generates the dataset
- Use realistic-looking data (not random strings): proper names, valid email formats, real-seeming dates
- Respect constraints: unique IDs, foreign key relationships, chronological ordering
- Apply specified distributions
- Execute the script and produce the output file

### Step 3: Deliver

Output in the requested format (or ask):
- **CSV**: Most common, works everywhere
- **JSON**: For API testing or frontend development
- **SQL INSERT**: For populating test databases
- **Python script**: For reproducible generation (user can tweak and re-run)

```
## Generated Dataset: [Description]

**Rows**: [count]
**Columns**: [list]
**Format**: [CSV / JSON / SQL / Python]

### Schema
| Column | Type | Constraints | Distribution |
|--------|------|-----------|-------------|

### Sample (first 5 rows)
[Preview of the data]

### Files
- [data file]
- [generator script, if applicable]
```

Save data file and generator script to the user's workspace.

### Step 4: Offer Follow-ups

- "Want me to **add more columns** or **increase the dataset size**?"
- "Should I **create related tables** (e.g., orders for these users)?"
- "Want me to **write test scenarios** that use this data?"
- "Should I **create SQL queries** to analyze this dataset?"

## Notes

- Always provide the generator script so the user can regenerate with different parameters
- For demo datasets, make the data tell a story (e.g., seasonal trends, a retention problem, a power user segment)
- Respect realistic cardinality: 1000 users don't have 1000 unique cities
- For financial data, use realistic price distributions — not uniform random
- Never include real personal data — all names, emails, and identifiers must be fake
```

## File: `pm-execution/commands/meeting-notes.md`
```markdown
---
description: Summarize a meeting transcript into structured notes with decisions, action items, and follow-ups
argument-hint: "<transcript or meeting notes>"
---

# /meeting-notes -- Meeting Summary

Transform a raw meeting transcript or rough notes into clear, structured meeting minutes with decisions captured and action items assigned.

## Invocation

```
/meeting-notes [paste transcript]
/meeting-notes [upload transcript file, audio summary, or notes]
```

## Workflow

### Step 1: Accept the Transcript

Accept in any format:
- Full transcript (from Otter, Fireflies, Google Meet, Zoom, etc.)
- Rough notes taken during the meeting
- Audio summary or meeting recap from a transcription tool
- Multiple inputs (e.g., transcript + the user's own notes)

If the input is sparse, work with what's available and flag gaps.

### Step 2: Extract and Structure

Apply the **summarize-meeting** skill:

Parse the content to identify:
- **Participants**: Who was present (from introductions, speaker labels, or mentions)
- **Topics discussed**: Major agenda items or conversation threads
- **Decisions made**: Explicit agreements or conclusions reached
- **Action items**: Tasks assigned, with owner and deadline if mentioned
- **Open questions**: Unresolved items that need follow-up
- **Key quotes**: Important statements worth preserving verbatim
- **Context**: Meeting type, project, and background

### Step 3: Generate Meeting Summary

```
## Meeting Summary

**Date**: [date if known]
**Participants**: [names/roles]
**Meeting type**: [standup, planning, review, 1:1, stakeholder, etc.]
**Topic**: [primary subject]

### Summary
[3-5 sentence overview of what was discussed and concluded]

### Key Decisions
1. **[Decision]** — [context and rationale]
2. ...

### Action Items
| # | Action | Owner | Deadline | Status |
|---|--------|-------|----------|--------|

### Discussion Highlights
**[Topic 1]**: [key points, different perspectives, conclusion]
**[Topic 2]**: [key points, different perspectives, conclusion]

### Open Questions
- [Question] — needs input from [person/team]

### Next Steps
- [What happens next]
- Next meeting: [if mentioned]
```

Save as markdown.

### Step 4: Offer Follow-ups

- "Want me to **email these notes** to participants?"
- "Should I **create tickets** from the action items?"
- "Want me to **draft a stakeholder update** based on the decisions made?"

## Notes

- Decisions are the most valuable output — make sure every decision is captured clearly
- Action items without owners are useless — if no owner was mentioned, flag it
- Keep the summary concise — people who weren't in the meeting should get the gist in 30 seconds
- If the transcript is very long (60+ min meeting), offer a TL;DR before the full summary
- Distinguish between "discussed" and "decided" — many topics are explored without reaching a conclusion
```

## File: `pm-execution/commands/plan-okrs.md`
```markdown
---
description: Brainstorm team-level OKRs aligned with company objectives — qualitative objectives with measurable key results
argument-hint: "<team, product area, or company objective>"
---

# /plan-okrs -- Team OKR Planning

Generate well-structured OKRs that connect team work to company strategy. Produces 3 OKR sets with qualitative objectives and quantitative key results.

## Invocation

```
/plan-okrs Growth team Q2 — company goal is 50% ARR increase
/plan-okrs Onboarding squad aligned to "improve activation rate"
/plan-okrs [upload company OKRs or strategy doc]
```

## Workflow

### Step 1: Gather Context

Ask the user:
- What team or product area are these OKRs for?
- What time period? (quarterly is standard, but could be annual or custom)
- What are the company-level objectives these should ladder up to?
- What happened last quarter? (hits, misses, learnings)
- Any constraints or known priorities?

Accept company OKRs or strategy documents as uploads.

### Step 2: Generate OKRs

Apply the **brainstorm-okrs** skill:

- Create 3 OKR sets (Objective + 3-5 Key Results each)
- **Objectives**: Qualitative, inspiring, ambitious but achievable, action-oriented
- **Key Results**: Quantitative, measurable, time-bound, have clear owners
- Ensure OKRs ladder to company objectives with visible connection
- Balance leading indicators (activity) with lagging indicators (outcomes)

### Step 3: Validate Quality

Check each OKR against best practices:
- Is the Objective inspiring? (Would you rally a team around it?)
- Are Key Results measurable? (Can you check completion with data, not judgment?)
- Are targets ambitious but not demoralizing? (70% achievement = well-calibrated)
- Are there 3-5 KRs per Objective? (More = unfocused)
- Do KRs avoid gaming? (e.g., "ship 5 features" incentivizes shipping junk)

Flag any issues and suggest improvements.

### Step 4: Present and Iterate

```
## Team OKRs: [Team Name] — [Period]

**Aligned to**: [Company Objective(s)]

### Objective 1: [Inspiring qualitative statement]
| # | Key Result | Baseline | Target | Owner |
|---|-----------|----------|--------|-------|
| KR1 | [measurable result] | [current] | [target] | [team/person] |
| KR2 | ... | ... | ... | ... |
| KR3 | ... | ... | ... | ... |

### Objective 2: [Inspiring qualitative statement]
[same format]

### Objective 3: [Inspiring qualitative statement]
[same format]

### Alignment Map
Company Objective → Team Objective → Key Results → Expected Impact

### Scoring Guide
- 0.0-0.3: Significant miss — investigate and learn
- 0.4-0.6: Progress made but fell short
- 0.7-0.9: Well-calibrated stretch goal — this is the target zone
- 1.0: Either nailed it or target wasn't ambitious enough

### Check-in Cadence
- **Weekly**: Quick traffic-light update on each KR
- **Mid-quarter**: Deep review, adjust targets if context changed
- **End of quarter**: Score, reflect, feed into next quarter
```

Offer:
- "Want me to **adjust ambition levels** — make them more/less aggressive?"
- "Should I **create a metrics dashboard** for tracking these?"
- "Want me to **draft a stakeholder update** introducing these OKRs?"

## Notes

- OKRs should describe outcomes, not outputs ("Increase activation by 20%" not "Ship onboarding redesign")
- If the user doesn't have company OKRs, help them derive team objectives from product strategy or business goals
- Maximum 3 objectives per team per quarter — more means less focus
- Key Results should be stretch goals — if you're certain you'll hit them, they're not ambitious enough
- Flag any KR that could be gamed and suggest a counter-metric
```

## File: `pm-execution/commands/pre-mortem.md`
```markdown
---
description: Run a pre-mortem risk analysis on a PRD, launch plan, or feature — identify what could go wrong before it does
argument-hint: "<PRD, plan, or feature description>"
---

# /pre-mortem -- Pre-Launch Risk Analysis

Imagine your launch has failed. Now work backward to figure out why. This command applies the Tigers/Paper Tigers/Elephants framework to surface real risks and create mitigation plans.

## Invocation

```
/pre-mortem [paste or upload a PRD, launch plan, or feature spec]
/pre-mortem We're launching a self-serve billing portal next month
```

## Workflow

### Step 1: Accept the Plan

Accept in any format: PRD, feature spec, launch plan, project brief, or verbal description. The more detail provided, the sharper the risk analysis.

### Step 2: Risk Identification

Apply the **pre-mortem** skill:

Imagine the product has launched and failed. Generate risks across categories:
- **Technical**: Performance, scalability, integration failures, data issues
- **User**: Adoption barriers, usability problems, unmet expectations
- **Business**: Revenue impact, competitive response, market timing
- **Operational**: Support load, documentation gaps, training needs
- **Dependencies**: Third-party services, cross-team handoffs, regulatory

### Step 3: Classify Risks

Categorize each risk:

**Tigers** — Real, substantive risks that could cause failure
- Assess severity: Launch-blocking / Fast-follow / Track
- For launch-blocking Tigers: immediate mitigation required
- For fast-follow Tigers: plan to address within first sprint post-launch
- For track Tigers: monitor but don't delay launch

**Paper Tigers** — Risks that feel scary but are overblown
- Explain why the concern is manageable
- Note what would need to change for this to become a real Tiger

**Elephants** — Unspoken risks the team knows about but avoids discussing
- Surface political, organizational, or uncomfortable risks
- Frame constructively with suggested conversation starters

### Step 4: Generate Pre-Mortem Report

```
## Pre-Mortem: [Feature/Launch]

**Date**: [today]
**Status**: [Draft / Reviewed]

### Risk Summary
- **Tigers**: [count] ([launch-blocking], [fast-follow], [track])
- **Paper Tigers**: [count]
- **Elephants**: [count]

### Launch-Blocking Tigers
| # | Risk | Likelihood | Impact | Mitigation | Owner | Deadline |
|---|------|-----------|--------|-----------|-------|----------|

### Fast-Follow Tigers
| # | Risk | Likelihood | Impact | Planned Response | Owner |
|---|------|-----------|--------|-----------------|-------|

### Track Tigers
[Risks to monitor post-launch with trigger conditions]

### Paper Tigers
[Concerns that seem big but are manageable — with reasoning]

### Elephants in the Room
[Uncomfortable truths the team should discuss]

### Go/No-Go Checklist
- [ ] All launch-blocking Tigers mitigated
- [ ] Fast-follow plan documented and assigned
- [ ] Monitoring in place for Track Tigers
- [ ] Rollback plan defined
- [ ] Support team briefed
```

Save as markdown.

### Step 5: Offer Next Steps

- "Want me to **update the PRD** with risk mitigations?"
- "Should I **create test scenarios** for the riskiest areas?"
- "Want me to **draft a launch checklist** from these findings?"

## Notes

- The best pre-mortems happen when the plan is 80% done — early enough to change course, late enough to have substance
- Push past the obvious risks — the most dangerous risks are the ones nobody mentions
- Elephants are the highest-value output — surfacing what the team avoids discussing
- For each Tiger, the mitigation should be specific and assignable, not "be careful"
- If the pre-mortem reveals too many launch-blocking Tigers, recommend delaying or phasing the launch
```

## File: `pm-execution/commands/sprint.md`
```markdown
---
description: Sprint lifecycle — plan a sprint, run a retrospective, or generate release notes
argument-hint: "[plan|retro|release-notes] <context>"
---

# /sprint -- Sprint Lifecycle

Three modes covering the sprint lifecycle: **plan** for sprint planning, **retro** for retrospectives, **release-notes** for shipping communication.

## Invocation

```
/sprint plan 2-week sprint, 4 engineers, focus on checkout improvements
/sprint retro [paste team feedback or sprint data]
/sprint release-notes [paste tickets, changelog, or PRD]
/sprint                    # asks which phase you're in
```

## Modes

---

### Plan Mode

Prepare for sprint planning with capacity estimation, story selection, and risk identification.

#### Workflow

**Step 1: Gather Sprint Context**
- Sprint duration (1 or 2 weeks)
- Team composition (engineers, designers, QA — and availability)
- Sprint goal or focus area
- Backlog items to consider (paste, upload, or describe)
- Any carry-over from last sprint
- Known interruptions (holidays, on-call, meetings)

**Step 2: Estimate Capacity**

Apply the **sprint-plan** skill:

- Calculate available engineering hours/points after meetings, on-call, PTO
- Apply a velocity adjustment based on historical data (if provided) or industry standard (70% of theoretical capacity)
- Show capacity breakdown per team member

**Step 3: Select and Sequence Stories**

- Recommend which stories fit within capacity
- Flag dependency chains (A must complete before B starts)
- Identify risks: stories that are underspecified, have external dependencies, or need design input
- Balance quick wins with larger items
- Ensure every story has acceptance criteria

**Step 4: Generate Sprint Plan**

```
## Sprint Plan: [Sprint Name/Number]

**Duration**: [dates]
**Sprint Goal**: [one sentence]
**Team**: [members and availability]

### Capacity
| Member | Available Days | Points/Hours | Notes |
|--------|--------------|-------------|-------|

**Total capacity**: [X] points/hours
**Recommended commitment**: [Y] points/hours (with buffer)

### Selected Stories
| # | Story | Points | Owner | Dependencies | Risk |
|---|-------|--------|-------|-------------|------|

### Sprint Risks
1. [Risk] — Mitigation: [action]

### Definition of Done
- [ ] Code reviewed
- [ ] Tests passing
- [ ] Deployed to staging
- [ ] QA approved
- [ ] Documentation updated (if applicable)
```

---

### Retro Mode

Facilitate a structured retrospective that produces actionable improvements.

#### Workflow

**Step 1: Gather Sprint Feedback**

Accept input as:
- Team feedback (pasted from a survey, Slack, or collaborative doc)
- Sprint metrics (velocity, bugs, incidents)
- The user's own observations

Ask: "Which retro format do you prefer?"
- **Start/Stop/Continue** (simple, fast)
- **4Ls** (Liked, Learned, Lacked, Longed for)
- **Sailboat** (Wind = helps, Anchor = slows, Rocks = risks, Island = goals)

**Step 2: Analyze and Structure**

Apply the **retro** skill:

- Categorize feedback into the chosen framework
- Identify themes and patterns
- Separate symptoms from root causes
- Highlight wins worth celebrating

**Step 3: Generate Retro Summary**

```
## Sprint Retrospective: [Sprint Name]

**Date**: [today]
**Format**: [Start/Stop/Continue | 4Ls | Sailboat]
**Participants**: [if known]

### What Went Well
[Grouped themes with supporting evidence]

### What Didn't Go Well
[Grouped themes with root cause analysis]

### Key Insights
[2-3 patterns that emerged]

### Action Items
| # | Action | Owner | Deadline | Priority |
|---|--------|-------|----------|----------|

### Metrics This Sprint
| Metric | This Sprint | Last Sprint | Trend |
|--------|-----------|------------|-------|
```

---

### Release Notes Mode

Generate user-facing release notes from technical artifacts.

#### Workflow

**Step 1: Accept Release Content**

Accept:
- Jira/Linear tickets or changelog
- PRD or feature specs
- Git commit messages or PR descriptions
- Team's internal summary of what shipped

**Step 2: Transform**

Apply the **release-notes** skill:

- Translate technical language into user benefits
- Categorize as: New Features, Improvements, Bug Fixes
- Write in the product's voice (ask about tone if not clear)
- Highlight the most impactful change first

**Step 3: Generate Release Notes**

```
## What's New — [Version/Date]

### Highlights
[1-2 sentence summary of the most important change]

### New Features
- **[Feature Name]** — [user-facing benefit in plain language]

### Improvements
- **[Improvement]** — [what's better now]

### Bug Fixes
- Fixed [issue] that caused [user impact]

### Coming Soon
[Optional teaser for next release]
```

Save as markdown and offer to format for different channels (blog post, in-app, email, Slack announcement).

## Notes

- For plan mode: protect 20% buffer for unplanned work — teams that plan at 100% capacity always miss
- For retro mode: focus on 2-3 high-impact action items, not 10 things nobody will do
- For release notes: always frame changes as user benefits, not technical implementations
- Each mode can chain to the others: plan → (sprint happens) → retro → release-notes
```

## File: `pm-execution/commands/stakeholder-map.md`
```markdown
---
description: Map stakeholders on a Power × Interest grid and create a tailored communication plan
argument-hint: "<project, initiative, or launch>"
---

# /stakeholder-map -- Stakeholder Mapping & Communication Plan

Identify all stakeholders for a project, map them by influence and interest, and generate a communication plan that ensures the right people get the right information at the right time.

## Invocation

```
/stakeholder-map New analytics platform launch
/stakeholder-map Pricing model change affecting all customers
/stakeholder-map [upload a project brief or org chart]
```

## Workflow

### Step 1: Understand the Initiative

Ask:
- What is the project or initiative?
- What phase is it in? (planning, building, launching, post-launch)
- Who are the obvious stakeholders you already know about?
- Are there any politically sensitive dynamics to be aware of?

### Step 2: Identify Stakeholders

Brainstorm stakeholders the user might not have considered:
- **Internal**: Engineering, Design, QA, Data, Legal, Finance, Marketing, Sales, Support, Leadership
- **External**: Customers, partners, vendors, regulators, board members
- **Often missed**: Adjacent teams, on-call engineers, customer success, documentation team

### Step 3: Map to Power × Interest Grid

Apply the **stakeholder-map** skill:

Place each stakeholder in a quadrant:

```
                    HIGH INTEREST
                         │
    KEEP SATISFIED       │      MANAGE CLOSELY
    (High Power,         │      (High Power,
     Low Interest)       │       High Interest)
                         │
   ──────────────────────┼──────────────────────
                         │
    MONITOR              │      KEEP INFORMED
    (Low Power,          │      (Low Power,
     Low Interest)       │       High Interest)
                         │
                    LOW INTEREST
```

### Step 4: Generate Communication Plan

```
## Stakeholder Map: [Initiative]

### Stakeholder Grid
| Stakeholder | Role | Power | Interest | Quadrant | Stance |
|------------|------|-------|----------|----------|--------|

### Communication Plan

#### Manage Closely (High Power, High Interest)
| Stakeholder | Channel | Frequency | Content | Owner |
|------------|---------|-----------|---------|-------|

#### Keep Satisfied (High Power, Low Interest)
| Stakeholder | Channel | Frequency | Content | Owner |
|------------|---------|-----------|---------|-------|

#### Keep Informed (Low Power, High Interest)
| Stakeholder | Channel | Frequency | Content | Owner |
|------------|---------|-----------|---------|-------|

#### Monitor (Low Power, Low Interest)
[Minimal communication — include in broad updates only]

### Potential Conflicts
[Where stakeholder interests may clash — with mitigation strategies]

### Escalation Path
[Who to go to when decisions are blocked]

### RACI Matrix
| Decision Area | Responsible | Accountable | Consulted | Informed |
|--------------|-------------|-------------|-----------|----------|
```

Save as markdown.

### Step 5: Offer Next Steps

- "Want me to **draft the first stakeholder update** for the 'Manage Closely' group?"
- "Should I **create a meeting prep brief** for key stakeholder conversations?"
- "Want me to **set up a communication cadence** as a recurring checklist?"

## Notes

- The "Manage Closely" quadrant is where PMs spend most of their political capital — get these relationships right
- "Stance" (supportive, neutral, resistant) helps prioritize where to invest relationship-building effort
- Don't forget downstream stakeholders: support, docs, and sales enablement teams are often surprised by launches
- Update the map as the project evolves — stakeholder interest shifts with project phase
```

## File: `pm-execution/commands/test-scenarios.md`
```markdown
---
description: Generate comprehensive test scenarios from user stories or feature specs — happy paths, edge cases, and error handling
argument-hint: "<user stories, feature spec, or description>"
---

# /test-scenarios -- Test Scenario Generator

Turn user stories or feature descriptions into comprehensive test scenarios that QA can execute immediately. Covers happy paths, edge cases, error handling, and cross-browser/device considerations.

## Invocation

```
/test-scenarios [paste user stories or acceptance criteria]
/test-scenarios [upload a PRD or feature spec]
/test-scenarios User can reset their password via email link
```

## Workflow

### Step 1: Accept Input

Accept: user stories, acceptance criteria, PRD sections, feature descriptions, or any specification of expected behavior.

### Step 2: Generate Test Scenarios

Apply the **test-scenarios** skill:

For each user story or requirement, generate:

**Happy Path Scenarios**: The expected user flow works correctly
**Edge Cases**: Boundary conditions, unusual inputs, concurrent operations
**Error Scenarios**: What happens when things go wrong
**Security Scenarios**: If applicable (auth, permissions, data access)
**Performance Scenarios**: If applicable (load, timeout, large data)

### Step 3: Structure Output

```
## Test Scenarios: [Feature]

**Source**: [user stories / PRD / description]
**Total scenarios**: [count]
**Coverage**: [happy path / edge cases / errors / security / performance]

### Scenario 1: [Title]
**Tests**: [which story or requirement]
**Preconditions**: [setup needed]
**User role**: [who is performing this]

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | [user action] | [expected system response] |
| 2 | [user action] | [expected system response] |

**Postconditions**: [state after completion]
**Priority**: [Critical / High / Medium / Low]

---
[Repeat for each scenario]

### Coverage Matrix
| Requirement | Happy Path | Edge Cases | Error Handling | Notes |
|------------|-----------|-----------|---------------|-------|

### Test Data Requirements
[What test data is needed to execute these scenarios]
```

Save as markdown.

### Step 4: Offer Next Steps

- "Want me to **generate the test data** for these scenarios?"
- "Should I **add more edge cases** for any specific scenario?"
- "Want me to **create the user stories** that these scenarios test?"

## Notes

- Happy paths first, then layer in edge cases — ensure basic flows work before testing boundaries
- Every acceptance criterion from the original story should map to at least one test scenario
- Include both positive tests (it works) and negative tests (it fails gracefully)
- For APIs, include scenarios for rate limiting, timeout, malformed requests, and auth failures
- Flag scenarios that require specific test environments or third-party service mocking
```

## File: `pm-execution/commands/transform-roadmap.md`
```markdown
---
description: Convert a feature-based roadmap into an outcome-focused roadmap that communicates strategic intent
argument-hint: "<roadmap as text, file, or list of planned features>"
---

# /transform-roadmap -- Outcome-Focused Roadmap

Take a list of planned features or an output-focused roadmap and rewrite it as an outcome-focused roadmap that communicates *why* instead of *what*.

## Invocation

```
/transform-roadmap [paste your feature list or roadmap]
/transform-roadmap [upload a roadmap doc, spreadsheet, or screenshot]
```

## Workflow

### Step 1: Accept the Current Roadmap

Accept in any format:
- Feature list or backlog items
- Roadmap document (Now/Next/Later, quarterly, timeline)
- Spreadsheet or Gantt chart export
- Screenshot of a roadmap tool

Parse each item to extract: feature name, description, target date/timeframe, and any context.

### Step 2: Understand Strategic Context

Ask:
- What are the product goals or OKRs for this period?
- Who is the audience for this roadmap? (execs, engineering, customers, board)
- What format do you prefer? (Now/Next/Later, quarterly, timeline)

### Step 3: Transform Each Item

Apply the **outcome-roadmap** skill:

For each feature/output on the roadmap:
1. Identify the **user or business outcome** it's trying to achieve
2. Rewrite as an outcome statement: "[Verb] [metric/experience] for [user segment]"
3. Group features that serve the same outcome under one initiative
4. Add success metrics to each outcome

**Before → After examples:**
- "Build SSO integration" → "Reduce enterprise onboarding friction — target: 50% faster time-to-first-value for enterprise accounts"
- "Redesign dashboard" → "Help power users find insights faster — target: 30% reduction in time-to-insight"
- "Add CSV export" → "Enable teams to share data outside the product — target: 25% increase in report sharing"

### Step 4: Generate Transformed Roadmap

```
## Outcome-Focused Roadmap: [Product] — [Period]

**Strategic themes**: [2-3 high-level themes]

### Now (Current Quarter)
**Theme: [Strategic Theme]**
| Outcome | Success Metric | Key Initiatives | Status |
|---------|---------------|----------------|--------|

### Next (Next Quarter)
**Theme: [Strategic Theme]**
| Outcome | Success Metric | Key Initiatives | Confidence |
|---------|---------------|----------------|------------|

### Later (Future)
**Theme: [Strategic Theme]**
| Outcome | Success Metric | Key Initiatives | Dependencies |
|---------|---------------|----------------|-------------|

### Transformation Notes
| Original Feature | Transformed Outcome | Why This Framing |
|-----------------|--------------------|-----------------|

### What Changed
[Summary of how the roadmap narrative shifted]
```

Save as a markdown file.

### Step 5: Review

Offer:
- "Want me to **add OKR alignment** for each outcome?"
- "Should I **draft a stakeholder presentation** of this roadmap?"
- "Want me to **identify risks** for the Now items?"

## Notes

- Outcomes should be measurable and have a clear "done" state
- Multiple features can map to one outcome — this is a feature, not a bug
- If an output doesn't clearly serve an outcome, flag it for the user to justify or deprioritize
- The audience matters: exec roadmaps should be outcome-only, engineering roadmaps can include deliverables under each outcome
- "Later" items should be less specific — outcomes without committed solutions
```

## File: `pm-execution/commands/write-prd.md`
```markdown
---
description: Create a comprehensive Product Requirements Document from a feature idea or problem statement
argument-hint: "<feature or problem statement>"
---

# /write-prd -- Product Requirements Document

Create a structured PRD that aligns stakeholders and guides development. Accepts anything from a vague idea to a detailed brief.

## Invocation

```
/write-prd SSO support for enterprise customers
/write-prd Users are dropping off during onboarding — we need to fix step 3
/write-prd [upload a brief, research doc, or strategy deck]
```

## Workflow

### Step 1: Understand the Feature

Accept the input in any form:
- A feature name ("SSO support")
- A problem statement ("Enterprise customers keep asking for centralized auth")
- A user request ("Users want to export their data as CSV")
- A vague idea ("We should do something about onboarding drop-off")
- An uploaded document (brief, research, Slack thread, email)

### Step 2: Gather Context

Ask conversationally — most important questions first, fill gaps as you go:

1. **User problem**: What problem does this solve? Who experiences it? How painful is it?
2. **Target users**: Which user segment(s)? How many? What's their current workaround?
3. **Success metrics**: How will we know this worked? What moves if we nail it?
4. **Constraints**: Technical constraints, timeline, regulatory, dependencies on other teams?
5. **Prior art**: Has this been attempted before? Existing solutions in the market?
6. **Scope preference**: Full solution or phased approach?

If the user provides a document with context, extract what's available and only ask about gaps.

### Step 3: Generate the PRD

Apply the **create-prd** skill to produce an 8-section document:

```
## Product Requirements Document: [Feature Name]

**Author**: [user]
**Date**: [today]
**Status**: Draft
**Stakeholders**: [if known]

### 1. Executive Summary
[2-3 sentences: what, for whom, why now]

### 2. Background & Context
[Problem space, prior research, market context, what prompted this]

### 3. Objectives & Success Metrics
**Goals** (what success looks like):
1. [Specific, measurable goal]
2. [...]

**Non-Goals** (explicitly out of scope):
1. [What we're not doing, and why]
2. [...]

**Success Metrics**:
| Metric | Current | Target | Measurement |
|--------|---------|--------|-------------|

### 4. Target Users & Segments
[Who this serves, user profiles, segment sizing]

### 5. User Stories & Requirements

**P0 — Must Have**:
| # | User Story | Acceptance Criteria |
|---|-----------|-------------------|

**P1 — Should Have**:
| # | User Story | Acceptance Criteria |
|---|-----------|-------------------|

**P2 — Nice to Have / Future**:
| # | User Story | Acceptance Criteria |
|---|-----------|-------------------|

### 6. Solution Overview
[High-level approach, key design decisions, technical approach if known]

### 7. Open Questions
| Question | Owner | Deadline |
|----------|-------|----------|

### 8. Timeline & Phasing
[Milestones, dependencies, phasing if applicable]
```

### Step 4: Review and Iterate

After generating, offer:
- "Want me to **tighten the scope**? I can challenge which P1s should really be P2s."
- "Should I **run a pre-mortem** on this PRD?"
- "Want me to **break this into user stories** for engineering?"
- "Should I **create a stakeholder update** to socialize this?"

Save the PRD as a markdown file to the user's workspace.

## Notes

- Be opinionated about scope — a tight PRD is better than an expansive vague one
- If the idea is too big, proactively suggest phasing and spec only Phase 1
- Non-goals are as important as goals — they prevent scope creep
- Success metrics must be specific: "improve NPS" is bad, "increase NPS from 32 to 45 within 90 days of launch" is good
- Open questions should be genuinely unresolved — don't list things you can answer from context
- If the user provides research, weave insights into the Background section with attribution
```

## File: `pm-execution/commands/write-stories.md`
```markdown
---
description: Break a feature into backlog items — user stories, job stories, or WWA format with acceptance criteria
argument-hint: "[user|job|wwa] <feature description or PRD>"
---

# /write-stories -- Backlog Item Generator

Break a feature into well-structured backlog items. Choose from three formats based on your team's preference, each with full acceptance criteria.

## Invocation

```
/write-stories user Allow users to export reports as PDF and CSV
/write-stories job Notification system for task deadlines
/write-stories wwa Dark mode for the mobile app
/write-stories [upload a PRD or feature spec]      # asks format preference
/write-stories                                      # asks for feature and format
```

## Formats

### User Stories
**Format**: "As a [user type], I want [capability], so that [benefit]"
Apply the **user-stories** skill:
- Follow the 3 C's: Card (brief), Conversation (context), Confirmation (acceptance criteria)
- Validate against INVEST: Independent, Negotiable, Valuable, Estimable, Small, Testable
- Include design links or mockup references where relevant

### Job Stories
**Format**: "When [situation], I want to [motivation], so I can [outcome]"
Apply the **job-stories** skill:
- Focus on the situation and context, not the user role
- Ground in real user scenarios observed in research
- Ideal for JTBD-oriented teams

### WWA (Why-What-Acceptance)
**Format**: Why [strategic context] → What [deliverable] → Acceptance [criteria]
Apply the **wwas** skill:
- Includes strategic reasoning (why we're building this)
- Produces independent, valuable, testable items
- Good for cross-functional teams that need business context

## Workflow

### Step 1: Accept the Feature

Accept in any form: PRD, feature description, user research finding, or verbal idea. If a PRD is provided, extract the requirements to decompose.

### Step 2: Determine Format

If not specified in the invocation, ask:
- "Which format does your team use? **User stories**, **Job stories**, or **WWA**?"
- If unsure, recommend user stories as the default

### Step 3: Decompose the Feature

- Break the feature into 5-15 independent stories (small enough to complete in one sprint)
- Ensure each story is independently valuable (delivers user value on its own)
- Order by dependency and priority
- Write 3-5 acceptance criteria per story
- Flag stories that need design input or technical spikes

### Step 4: Generate Stories

```
## Backlog: [Feature Name]

**Format**: [User Stories / Job Stories / WWA]
**Total stories**: [count]
**Estimated total effort**: [if possible]

### Stories

#### Story 1: [Short title]
**[The story in chosen format]**

Acceptance Criteria:
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

Priority: [P0/P1/P2] | Effort: [S/M/L] | Dependencies: [none or list]

---
[Repeat for each story]

### Story Map
[Visual ordering: must-have → should-have → nice-to-have]

### Technical Notes
[Cross-cutting concerns: API changes, data migration, infrastructure]

### Open Questions
[Things that need answers before implementation can start]
```

Save as markdown.

### Step 5: Offer Next Steps

- "Want me to **generate test scenarios** for these stories?"
- "Should I **create dummy data** for development and testing?"
- "Want me to **estimate sprint capacity** for these stories?"
- "Should I **convert to a different format** (user stories ↔ job stories ↔ WWA)?"

## Notes

- One story = one deployable unit of value — if it needs another story to be useful, they should be combined
- Acceptance criteria should be testable by QA without additional interpretation
- Error handling and edge cases deserve their own stories, not bullet points within a happy-path story
- If the feature is large (15+ stories), suggest grouping into epics or phases
- Flag any story that requires a spike (technical investigation before estimation is possible)
```

## File: `pm-execution/skills/brainstorm-okrs/SKILL.md`
```markdown
---
name: brainstorm-okrs
description: "Brainstorm team-level OKRs aligned with company objectives — qualitative objectives with measurable key results. Use when setting quarterly OKRs, aligning team goals with company strategy, drafting objectives, or learning how to write effective OKRs."
---

# Brainstorm Team OKRs

## Purpose

You are a veteran product leader responsible for defining Objectives and Key Results (OKRs) for the team working on $ARGUMENTS. Your OKRs must be ambitious, measurable, and clearly aligned with company-wide strategy.

## Context

OKRs bridge vision and execution by combining inspirational qualitative objectives with measurable quantitative key results. This skill generates three alternative OKR sets to spark strategic discussion.

## Domain Context

**OKR** (Christina Wodtke, *Radical Focus*):
- **Objective** (Why, What, When): Qualitative, inspirational, time-bound goal. Typically quarterly. Should be SMART.
- **Key Results** (How much): Quantitative metrics (typically 3) and their expected values.

**OKRs, KPIs, and NSM are interconnected — not alternatives.** Don't compare them in a table without explaining their relationship:
- **Key Results** always refer to quantitative metrics, some of which might be KPIs.
- **KPIs** = a few key quantitative metrics tracked over a longer period. Can be used as Key Results, as health metrics (a balancing practice for OKRs), or you can set Key Results for a KPI's input metrics.
- **North Star Metric** = a single, customer-centric KPI. A leading indicator of business success. You can use Key Results to express expected change in NSM.

OKRs are fundamentally about: (1) Setting a single, inspiring goal. (2) Empowering a team to determine the optimal approach. (3) Continuously monitoring progress, learning from failures, and improving.

## Instructions

1. **Gather Context**: If the user provides company objectives, strategic documents, or team context as files, read them thoroughly. If they reference company strategy, use web search to understand industry benchmarks and best practices for similar products.

2. **Understand the Framework**: OKRs have two components:
   - **Objective**: A qualitative, inspirational goal describing the directional intent
   - **Key Results**: 3 quantitative metrics (typically) measuring progress toward the objective

3. **Think Step by Step**:
   - What is the company strategy?
   - What are the 3-5 most impactful areas the team can influence?
   - How do team efforts ladder up to company goals?
   - What would success look like for customers and the business?

4. **Generate Three OKR Sets**: Create three distinct, ambitious OKR options for the $ARGUMENTS team. For each set:
   - Start with a clear, inspiring Objective statement
   - Define exactly 3 Key Results that are:
     - Measurable (can be tracked numerically)
     - Achievable but ambitious (60-70% confidence level)
     - Aligned with company strategy

5. **Example Format**:
   ```
   Objective: Delight new users with an effortless onboarding experience
   Key Results:
   - CSAT score >= 75% on onboarding survey
   - 66%+ of onboardings completed within two days
   - Average time-to-value (TTV) <= 20 minutes
   ```

6. **Structure Output**: Present all three OKR sets with equal weight. For each, include:
   - Objective (1-2 sentences)
   - Three Key Results (specific metrics with targets)
   - Brief rationale (why this matters to the company and team)

7. **Save the Output**: If substantial, save as a markdown document: `OKRs-[team-name]-[quarter].md`

## Notes

- Ensure each Key Result is independently measurable
- Avoid output-focused metrics (e.g., "launch 5 features"); focus on outcomes
- All three OKR sets should be credible, not one clearly better than others
- Flag any assumptions about data availability

---

### Further Reading

- [Objectives and Key Results (OKRs) 101](https://www.productcompass.pm/p/okrs-101-advanced-techniques)
- [OKR vs KPI: What's the Difference?](https://www.productcompass.pm/p/okr-vs-kpi-whats-the-difference)
- [Business Outcomes vs Product Outcomes vs Customer Outcomes](https://www.productcompass.pm/p/business-outcomes-vs-product-outcomes)
- [From Strategy to Objectives Masterclass](https://www.productcompass.pm/p/product-vision-strategy-objectives-course) (video course)
```

## File: `pm-execution/skills/create-prd/SKILL.md`
```markdown
---
name: create-prd
description: "Create a Product Requirements Document using a comprehensive 8-section template covering problem, objectives, segments, value propositions, solution, and release planning. Use when writing a PRD, documenting product requirements, preparing a feature spec, or reviewing an existing PRD."
---

# Create a Product Requirements Document

## Purpose

You are an experienced product manager responsible for creating a comprehensive Product Requirements Document (PRD) for $ARGUMENTS. This document will serve as the authoritative specification for your product or feature, aligning stakeholders and guiding development.

## Context

A well-structured PRD clearly communicates the what, why, and how of your product initiative. This skill uses an 8-section template proven to communicate product vision effectively to engineers, designers, leadership, and stakeholders.

## Instructions

1. **Gather Information**: If the user provides files, read them carefully. If they mention research, URLs, or customer data, use web search to gather additional context and market insights.

2. **Think Step by Step**: Before writing, analyze:
   - What problem are we solving?
   - Who are we solving it for?
   - How will we measure success?
   - What are our constraints and assumptions?

3. **Apply the PRD Template**: Create a document with these 8 sections:

   **1. Summary** (2-3 sentences)
   - What is this document about?

   **2. Contacts**
   - Name, role, and comment for key stakeholders

   **3. Background**
   - Context: What is this initiative about?
   - Why now? Has something changed?
   - Is this something that just recently became possible?

   **4. Objective**
   - What's the objective? Why does it matter?
   - How will it benefit the company and customers?
   - How does it align with vision and strategy?
   - Key Results: How will you measure success? (Use SMART OKR format)

   **5. Market Segment(s)**
   - For whom are we building this?
   - What constraints exist?
   - Note: Markets are defined by people's problems/jobs, not demographics

   **6. Value Proposition(s)**
   - What customer jobs/needs are we addressing?
   - What will customers gain?
   - Which pains will they avoid?
   - Which problems do we solve better than competitors?
   - Consider the Value Curve framework

   **7. Solution**
   - 7.1 UX/Prototypes (wireframes, user flows)
   - 7.2 Key Features (detailed feature descriptions)
   - 7.3 Technology (optional, only if relevant)
   - 7.4 Assumptions (what we believe but haven't proven)

   **8. Release**
   - How long could it take?
   - What goes in the first version vs. future versions?
   - Avoid exact dates; use relative timeframes

4. **Use Accessible Language**: Write for a primary school graduate. Avoid jargon. Use clear, short sentences.

5. **Structure Output**: Present the PRD as a well-formatted markdown document with clear headings and sections.

6. **Save the Output**: If the PRD is substantial (which it will be), save it as a markdown document in the format: `PRD-[product-name].md`

## Notes

- Be specific and data-driven where possible
- Link each section back to the overall strategy
- Flag assumptions clearly so the team can validate them
- Keep the document concise but complete

---

### Further Reading

- [How to Write a Product Requirements Document? The Best PRD Template.](https://www.productcompass.pm/p/prd-template)
- [A Proven AI PRD Template by Miqdad Jaffer (Product Lead @ OpenAI)](https://www.productcompass.pm/p/ai-prd-template)
```

## File: `pm-execution/skills/dummy-dataset/SKILL.md`
```markdown
---
name: dummy-dataset
description: "Generate realistic dummy datasets for testing with customizable columns, constraints, and output formats (CSV, JSON, SQL, Python script). Use when creating test data, building mock datasets, or generating sample data for development and demos."
---
# Dummy Dataset Generation

Generate realistic dummy datasets for testing with customizable columns, constraints, and output formats (CSV, JSON, SQL, Python script). Creates executable scripts or direct data files for immediate use.

**Use when:** Creating test data, generating sample datasets, building realistic mock data for development, or populating test environments.

**Arguments:**
- `$PRODUCT`: The product or system name
- `$DATASET_TYPE`: Type of data (e.g., customer feedback, transactions, user profiles)
- `$ROWS`: Number of rows to generate (default: 100)
- `$COLUMNS`: Specific columns or fields to include
- `$FORMAT`: Output format (CSV, JSON, SQL, Python script)
- `$CONSTRAINTS`: Additional constraints or business rules

## Step-by-Step Process

1. **Identify dataset type** - Understand the data domain
2. **Define column specifications** - Names, data types, and value ranges
3. **Determine row count** - How many sample records needed
4. **Select output format** - CSV, JSON, SQL INSERT, or Python script
5. **Apply realistic patterns** - Ensure data looks authentic and valid
6. **Add business constraints** - Respect business logic and relationships
7. **Generate or script data** - Create executable output
8. **Validate output** - Ensure data quality and completeness

## Template: Python Script Output

```python
import csv
import json
from datetime import datetime, timedelta
import random

# Configuration
ROWS = $ROWS
FILENAME = "$DATASET_TYPE.csv"

# Column definitions with realistic value generators
columns = {
    "id": "auto-increment",
    "name": "first_last_name",
    "email": "email",
    "created_at": "timestamp",
    # Add more columns...
}

def generate_dataset():
    """Generate realistic dummy dataset"""
    data = []
    for i in range(1, ROWS + 1):
        record = {
            "id": f"U{i:06d}",
            # Generate values based on column definitions
        }
        data.append(record)
    return data

def save_as_csv(data, filename):
    """Save dataset as CSV"""
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    dataset = generate_dataset()
    save_as_csv(dataset, FILENAME)
    print(f"Generated {len(dataset)} records in {FILENAME}")
```

## Example Dataset Specification

**Dataset Type:** Customer Feedback

**Columns:**
- feedback_id (auto-increment, U001, U002...)
- customer_name (realistic names)
- email (valid email format)
- feedback_date (dates last 90 days)
- rating (1-5 stars)
- category (Bug, Feature Request, Complaint, Praise)
- text (realistic feedback)
- product (electronics, clothing, home)

**Constraints:**
- Ratings skewed: 40% 5-star, 30% 4-star, 20% 3-star, 10% 1-2 star
- Bug category only with ratings 1-3
- Feature requests only with ratings 3-5
- Email domains realistic (gmail, yahoo, company.com)

## Output Deliverables

- Ready-to-execute Python script OR direct data file
- CSV file with proper headers and formatting
- JSON file with valid structure and types
- SQL INSERT statements for database population
- Data validation and constraint compliance
- Realistic, business-appropriate values
- Documentation of data generation logic
- Quick-start instructions for using the dataset

## Output Formats

**CSV:** Flat tabular format, easy to import into spreadsheets and databases

**JSON:** Nested structure, ideal for APIs and NoSQL databases

**SQL:** INSERT statements, directly executable on relational databases

**Python Script:** Executable generator for custom or large datasets
```

## File: `pm-execution/skills/job-stories/SKILL.md`
```markdown
---
name: job-stories
description: "Create job stories using the 'When [situation], I want to [motivation], so I can [outcome]' format with detailed acceptance criteria. Use when writing job stories, creating JTBD-style backlog items, or expressing user situations and motivations."
---
# Job Stories

Create job stories using the 'When [situation], I want to [motivation], so I can [outcome]' format. Generates stories with detailed acceptance criteria focused on user situations and outcomes.

**Use when:** Writing job stories, expressing user situations and motivations, creating JTBD-style backlog items, or focusing on user context rather than roles.

**Arguments:**
- `$PRODUCT`: The product or system name
- `$FEATURE`: The new feature to break into job stories
- `$DESIGN`: Link to design files (Figma, Miro, etc.)
- `$CONTEXT`: User situations or job scenarios

## Step-by-Step Process

1. **Identify user situations** that trigger the need
2. **Define motivations** underlying the user's behavior
3. **Clarify outcomes** the user wants to achieve
4. **Apply JTBD framework:** Focus on the job, not the role
5. **Create acceptance criteria** that validate the outcome is achieved
6. **Use observable, measurable language**
7. **Link to design mockups** or prototypes
8. **Output job stories** with detailed acceptance criteria

## Story Template

**Title:** [Job outcome or result]

**Description:** When [situation], I want to [motivation], so I can [outcome].

**Design:** [Link to design files]

**Acceptance Criteria:**
1. [Situation is properly recognized]
2. [System enables the desired motivation]
3. [Progress or feedback is visible]
4. [Outcome is achieved efficiently]
5. [Edge cases are handled gracefully]
6. [Integration and notifications work]

## Example Job Story

**Title:** Track Weekly Snack Spending

**Description:** When I'm preparing my weekly allowance for snacks (situation), I want to quickly see how much I've spent so far (motivation), so I can make sure I don't run out of money before the weekend (outcome).

**Design:** [Figma link]

**Acceptance Criteria:**
1. Display Spending Summary with 'Weekly Spending Overview' section
2. Real-Time Update when expense logged
3. Progress Indicator (progress bar showing 0-100% of weekly budget)
4. Remaining Budget Highlight in prominent color
5. Detailed Spending Log with breakdown by category
6. Notifications at 80% budget threshold
7. Weekend-Specific Reminder at 90% by Thursday evening
8. Easy Access and Navigation to detailed breakdown

## Output Deliverables

- Complete set of job stories for the feature
- Each story follows the 'When...I want...so I can' format
- 6-8 acceptance criteria focused on outcomes
- Stories emphasize user situations and motivations
- Clear links to design and prototypes

---

### Further Reading

- [Jobs-to-be-Done Masterclass with Tony Ulwick and Sabeen Sattar](https://www.productcompass.pm/p/jobs-to-be-done-masterclass-with) (video course)
```

## File: `pm-execution/skills/outcome-roadmap/SKILL.md`
```markdown
---
name: outcome-roadmap
description: "Transform an output-focused roadmap into an outcome-focused one that communicates strategic intent. Rewrites initiatives as outcome statements reflecting user and business impacts. Use when shifting to outcome roadmaps, making a roadmap more strategic, or rewriting feature lists as outcomes."
---

# Transform Roadmap to Outcome-Focused Format

## Purpose

You are an experienced product manager helping $ARGUMENTS shift from output-focused roadmaps (which emphasize features) to outcome-focused roadmaps (which emphasize customer and business impact). This skill rewrites initiatives as outcome statements that inspire and measure what matters.

## Context

Output-focused roadmaps create false precision and misalign teams around features rather than results. Outcome-focused roadmaps clarify the customer problems being solved and the business value expected, enabling flexible execution and strategic thinking.

## Instructions

1. **Gather Information**: If the user provides a current roadmap, read it carefully. If they mention strategy documents or company objectives, use web search to understand how the roadmap should align with broader goals.

2. **Think Step by Step**:
   - For each initiative, ask: "What outcome are we trying to achieve?"
   - What customer problem are we solving?
   - What business metric will improve?
   - How will this impact the customer experience or business?
   - Is there a better, different way to achieve the same outcome?

3. **Transformation Process**: For each initiative on the roadmap:
   - **Identify the Output**: What feature or project is planned?
   - **Uncover the Outcome**: Why are we building it? What changes for customers or business?
   - **Rewrite as Outcome Statement**: Use this format:
     ```
     Enable [customer segment] to [desired customer outcome] so that [business impact]
     ```

4. **Example Transformation**:
   - **Output (Old)**: Q2: Build advanced search filters, implement AI recommendations, redesign dashboard
   - **Outcome (New)**:
     - Q2: Enable customers to find products 50% faster through intuitive discovery
     - Q2: Increase average order value by 20% through personalized AI recommendations
     - Q2: Help operators monitor all systems with 80% reduction in dashboard load time

5. **Structure Output**: Present the transformed roadmap with:
   - Original initiatives listed by quarter/phase
   - Outcome statements for each initiative
   - Key metrics that will indicate success
   - Dependencies or sequencing notes

6. **Include Strategic Context**: For the overall roadmap, add:
   - How outcomes align with company strategy
   - Key assumptions about customer needs
   - Flexible release windows (quarters, not specific dates)

7. **Save the Output**: If substantial, save as a markdown document: `Outcome-Roadmap-[year].md`

## Notes

- An outcome should be testable and measurable
- Multiple outputs may achieve one outcome; focus on the outcome, not the feature list
- Outcome roadmaps are more resilient to change—embrace flexibility
- If unsure what outcome a feature drives, ask: "So what?" until you reach real customer/business value

---

### Further Reading

- [Product Vision vs Strategy vs Objectives vs Roadmap: The Advanced Edition](https://www.productcompass.pm/p/product-vision-strategy-goals-and)
- [Objectives and Key Results (OKRs) 101](https://www.productcompass.pm/p/okrs-101-advanced-techniques)
- [Business Outcomes vs Product Outcomes vs Customer Outcomes](https://www.productcompass.pm/p/business-outcomes-vs-product-outcomes)
```

## File: `pm-execution/skills/pre-mortem/SKILL.md`
```markdown
---
name: pre-mortem
description: "Run a pre-mortem risk analysis on a PRD or launch plan. Categorizes risks as Tigers (real problems), Paper Tigers (overblown concerns), and Elephants (unspoken worries), then classifies as launch-blocking, fast-follow, or track. Use when preparing for launch, stress-testing a product plan, or identifying what could go wrong."
---

# Pre-Mortem: Risk Analysis for Product Launch

## Purpose

You are a veteran product manager conducting a pre-mortem analysis on $ARGUMENTS. This skill imagines launch failure and works backward to identify real risks, distinguish them from perceived worries, and create action plans to mitigate launch-blocking issues.

## Context

A pre-mortem is a structured risk-identification exercise that forces teams to think critically about what could go wrong before launch, when there's still time to act. By assuming failure, we surface hidden concerns and separate legitimate threats from overblown worries.

## Instructions

1. **Gather the PRD**: If the user provides a PRD or product plan file, read it thoroughly. Understand the product, target market, key assumptions, and timeline. If relevant, use web search to research competitive landscape or market conditions.

2. **Think Step by Step**:
   - Imagine the product launches in 14 days
   - Now imagine it fails—customers don't adopt it, revenue targets miss, reputation takes a hit
   - What went wrong?
   - What did we miss or not execute well?
   - What were we overconfident about?

3. **Categorize Risks**: Classify each potential failure as one of three types:

   **Tigers**: Real problems you personally see that could derail the project
   - Based on evidence, past experience, or clear logic
   - Should keep you awake at night
   - Require action

   **Paper Tigers**: Problems others might worry about, but you don't believe in them
   - Valid concerns on the surface, but unlikely or overblown
   - Not worth significant resource investment
   - Worth documenting to align stakeholders

   **Elephants**: Something you're not sure is a problem, but the team isn't discussing it enough
   - Unspoken concerns or assumptions nobody is validating
   - Could be real; you're unsure
   - Deserve investigation before launch

4. **Classify Tigers by Urgency**:

   **Launch-Blocking**: Must be solved before launch
   - Example: Core feature broken, regulatory blocker, key customer dependency unmet

   **Fast-Follow**: Must be solved within 30 days post-launch
   - Example: Performance issues, secondary features incomplete

   **Track**: Monitor post-launch; solve if it becomes an issue
   - Example: Nice-to-have features, edge cases

5. **Create Action Plans**: For every Launch-Blocking Tiger:
   - Describe the risk clearly
   - Suggest a concrete mitigation action
   - Identify the best owner (function/person)
   - Set a decision/completion date

6. **Structure Output**: Present the analysis as:

   ```
   ## Pre-Mortem Analysis: [Product Name]

   ### Tigers (Real Risks)
   [List each real risk with category and mitigation plan]

   ### Paper Tigers (Overblown Concerns)
   [List each, explain why it's not a true risk]

   ### Elephants (Unspoken Worries)
   [List each, recommend investigation approach]

   ### Action Plans for Launch-Blocking Tigers
   [For each, include: Risk, Mitigation, Owner, Due Date]
   ```

7. **Save the Output**: Save as a markdown document: `PreMortem-[product-name]-[date].md`

## Notes

- Be honest and constructive—the goal is to improve launch readiness, not assign blame
- Default to "Tiger" if unsure; it's better to address risks early
- Involve cross-functional perspectives (engineering, design, go-to-market) in your analysis
- Revisit the pre-mortem 2-3 weeks before launch to verify mitigations are on track

---

### Further Reading

- [How Meta and Instagram Use Pre-Mortems to Avoid Post-Mortems](https://www.productcompass.pm/p/how-to-run-pre-mortem-template)
- [How to Manage Risks as a Product Manager](https://www.productcompass.pm/p/how-to-manage-risks-as-a-product-manager)
```

## File: `pm-execution/skills/prioritization-frameworks/SKILL.md`
```markdown
---
name: prioritization-frameworks
description: "Reference guide to 9 prioritization frameworks with formulas, when-to-use guidance, and templates — RICE, ICE, Kano, MoSCoW, Opportunity Score, and more. Use when selecting a prioritization method, comparing frameworks like RICE vs ICE, or learning how different prioritization approaches work."
---

## Prioritization Frameworks Reference

A reference guide to help you select and apply the right prioritization framework for your context.

### Core Principle

Never allow customers to design solutions. Prioritize **problems (opportunities)**, not features.

### Opportunity Score (Dan Olsen, *The Lean Product Playbook*)

The recommended framework for prioritizing customer problems.

Survey customers on **Importance** and **Satisfaction** for each need (normalize to 0–1 scale).

Three related formulas:
- **Current value** = Importance × Satisfaction
- **Opportunity Score** = Importance × (1 − Satisfaction)
- **Customer value created** = Importance × (S2 − S1), where S1 = satisfaction before, S2 = satisfaction after

High Importance + low Satisfaction = highest Opportunity Score = best opportunities. Plot on an Importance vs Satisfaction chart — upper-left quadrant is the sweet spot. Prioritizes customer problems, not solutions.

### ICE Framework

Useful for prioritizing initiatives and ideas. Considers not only value but also risk and economic factors.

- **I** (Impact) = Opportunity Score × Number of Customers affected
- **C** (Confidence) = How confident are we? (1-10). Accounts for risk.
- **E** (Ease) = How easy is it to implement? (1-10). Accounts for economic factors.

**Score** = I × C × E. Higher = prioritize first.

### RICE Framework

Splits ICE's Impact into two separate factors. Useful for larger teams that need more granularity.

- **R** (Reach) = Number of customers affected
- **I** (Impact) = Opportunity Score (value per customer)
- **C** (Confidence) = How confident are we? (0-100%)
- **E** (Effort) = How much effort to implement? (person-months)

**Score** = (R × I × C) / E

### 9 Frameworks Overview

| Framework | Best For | Key Insight |
|-----------|----------|-------------|
| Eisenhower Matrix | Personal tasks | Urgent vs Important — for individual PM task management |
| Impact vs Effort | Tasks/initiatives | Simple 2×2 — quick triage, not rigorous for strategic decisions |
| Risk vs Reward | Initiatives | Like Impact vs Effort but accounts for uncertainty |
| **Opportunity Score** | Customer problems | **Recommended.** Importance × (1 − Satisfaction). Normalize to 0–1. |
| Kano Model | Understanding expectations | Must-be, Performance, Attractive, Indifferent, Reverse. For understanding, not prioritizing. |
| Weighted Decision Matrix | Multi-factor decisions | Assign weights to criteria, score each option. Useful for stakeholder buy-in. |
| **ICE** | Ideas/initiatives | Impact × Confidence × Ease. Recommended for quick prioritization. |
| **RICE** | Ideas at scale | (Reach × Impact × Confidence) / Effort. Adds Reach to ICE. |
| MoSCoW | Requirements | Must/Should/Could/Won't. Caution: project management origin. |

### Templates

- [Opportunity Score intro (PDF)](https://drive.google.com/file/d/1ENbYPmk1i1AKO7UnfyTuULL5GucTVufW/view)
- [Importance vs Satisfaction Template — Dan Olsen (Google Slides)](https://docs.google.com/presentation/d/1jg-LuF_3QHsf6f1nE1f98i4C0aulnRNMOO1jftgti8M/edit#slide=id.g796641d975_0_3)
- [ICE Template (Google Sheets)](https://docs.google.com/spreadsheets/d/1LUfnsPolhZgm7X2oij-7EUe0CJT-Dwr-/edit?usp=share_link&ouid=111307342557889008106&rtpof=true&sd=true)
- [RICE Template (Google Sheets)](https://docs.google.com/spreadsheets/d/1S-6QpyOz5MCrV7B67LUWdZkAzn38Eahv/edit?usp=sharing&ouid=111307342557889008106&rtpof=true&sd=true)

---

### Further Reading

- [The Product Management Frameworks Compendium + Templates](https://www.productcompass.pm/p/the-product-frameworks-compendium)
- [Kano Model: How to Delight Your Customers Without Becoming a Feature Factory](https://www.productcompass.pm/p/kano-model-how-to-delight-your-customers)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)
```

## File: `pm-execution/skills/release-notes/SKILL.md`
```markdown
---
name: release-notes
description: "Generate user-facing release notes from tickets, PRDs, or changelogs. Creates clear, engaging summaries organized by category (new features, improvements, fixes). Use when writing release notes, creating changelogs, announcing product updates, or summarizing what shipped."
---

## Release Notes Generator

Transform technical tickets, PRDs, or internal changelogs into polished, user-facing release notes.

### Context

You are writing release notes for **$ARGUMENTS**.

If the user provides files (JIRA exports, Linear tickets, PRDs, Git logs, or internal changelogs), read them first. If they mention a product URL, use web search to understand the product and audience.

### Instructions

1. **Gather raw material**: Read all provided tickets, changelogs, or descriptions. Extract:
   - What changed (feature, improvement, or fix)
   - Who it affects (which user segment)
   - Why it matters (the user benefit)

2. **Categorize changes**:
   - **New Features**: Entirely new capabilities
   - **Improvements**: Enhancements to existing features
   - **Bug Fixes**: Issues resolved
   - **Breaking Changes**: Anything that requires user action (migrations, API changes)
   - **Deprecations**: Features being sunset

3. **Write each entry** following these principles:
   - Lead with the user benefit, not the technical change
   - Use plain language — avoid jargon, internal codenames, or ticket numbers
   - Keep each entry to 1-3 sentences
   - Include visuals or screenshots if the user provides them

   **Example transformations**:
   - Technical: "Implemented Redis caching layer for dashboard API endpoints"
   - User-facing: "Dashboards now load up to 3× faster, so you spend less time waiting and more time analyzing."

   - Technical: "Fixed race condition in concurrent checkout flow"
   - User-facing: "Fixed an issue where some orders could fail during high-traffic periods."

4. **Structure the release notes**:

   ```
   # [Product Name] — [Version / Date]

   ## New Features
   - **[Feature name]**: [1-2 sentence description of what it does and why it matters]

   ## Improvements
   - **[Area]**: [What got better and how it helps]

   ## Bug Fixes
   - Fixed [issue description in user terms]

   ## Breaking Changes (if any)
   - **Action required**: [What users need to do]
   ```

5. **Adjust tone** to match the product's voice — professional for B2B, friendly for consumer, developer-focused for APIs.

Save as a markdown document. If the user wants HTML or another format, convert accordingly.
```

## File: `pm-execution/skills/retro/SKILL.md`
```markdown
---
name: retro
description: "Facilitate a structured sprint retrospective — what went well, what didn't, and prioritized action items with owners and deadlines. Use when running a retrospective, reflecting on a sprint, creating action items from team feedback, or learning how to run effective retros."
---

## Sprint Retrospective Facilitator

Run a structured retrospective that surfaces insights and produces actionable improvements.

### Context

You are facilitating a retrospective for **$ARGUMENTS**.

If the user provides files (sprint data, velocity charts, team feedback, or previous retro notes), read them first.

### Instructions

1. **Choose a retro format** based on context (or let the user pick):

   **Format A — Start / Stop / Continue**:
   - **Start**: What should we begin doing?
   - **Stop**: What should we stop doing?
   - **Continue**: What's working well that we should keep?

   **Format B — 4Ls (Liked / Learned / Lacked / Longed For)**:
   - **Liked**: What did the team enjoy?
   - **Learned**: What new knowledge was gained?
   - **Lacked**: What was missing?
   - **Longed For**: What do we wish we had?

   **Format C — Sailboat**:
   - **Wind (propels us)**: What's driving us forward?
   - **Anchor (holds us back)**: What's slowing us down?
   - **Rocks (risks)**: What dangers lie ahead?
   - **Island (goal)**: Where are we trying to get to?

2. **If the user provides raw feedback** (e.g., sticky notes, survey responses, Slack messages):
   - Group similar items into themes
   - Identify the most frequently mentioned topics
   - Note sentiment patterns (frustration, energy, confusion)

3. **Analyze the sprint performance**:
   - Sprint goal: achieved or not?
   - Velocity vs. commitment (over-committed? under-committed?)
   - Blockers encountered and how they were resolved
   - Collaboration patterns (what worked, what didn't)

4. **Generate prioritized action items**:

   | Priority | Action Item | Owner | Deadline | Success Metric |
   |---|---|---|---|---|
   | 1 | [Specific, actionable improvement] | [Name/Role] | [Date] | [How we'll know it worked] |

   - Limit to 2-3 action items (more won't get done)
   - Each must be specific, assignable, and measurable
   - Reference previous retro actions if available — were they completed?

5. **Create the retro summary**:
   ```
   ## Sprint [X] Retrospective — [Date]

   ### Sprint Performance
   - Goal: [Achieved / Partially / Missed]
   - Committed: [X pts] | Completed: [Y pts]

   ### Key Themes
   1. [Theme] — [summary]

   ### Action Items
   1. [Action] — [Owner] — [By date]

   ### Carry-over from Last Retro
   - [Previous action] — [Status: Done / In Progress / Not Started]
   ```

Save as markdown. Keep the tone constructive — the goal is improvement, not blame.
```

## File: `pm-execution/skills/sprint-plan/SKILL.md`
```markdown
---
name: sprint-plan
description: "Plan a sprint with capacity estimation, story selection, dependency mapping, and risk identification. Use when preparing for sprint planning, estimating team capacity, selecting stories, or balancing sprint scope against velocity."
---

## Sprint Planning

Plan a sprint by estimating team capacity, selecting and sequencing stories, and identifying risks.

### Context

You are helping plan a sprint for **$ARGUMENTS**.

If the user provides files (backlogs, velocity data, team rosters, or previous sprint reports), read them first.

### Instructions

1. **Estimate team capacity**:
   - Number of team members and their availability (PTO, meetings, on-call)
   - Historical velocity (average story points per sprint from last 3 sprints)
   - Capacity buffer: reserve 15-20% for unexpected work, bugs, and tech debt
   - Calculate available capacity in story points or ideal hours

2. **Review and select stories**:
   - Pull from the prioritized backlog (highest priority first)
   - Verify each story meets the Definition of Ready (clear AC, estimated, no blockers)
   - Flag stories that need refinement before committing
   - Stop adding stories when capacity is reached

3. **Map dependencies**:
   - Identify stories that depend on other stories or external teams
   - Sequence dependent stories appropriately
   - Flag external dependencies and owners
   - Identify the critical path

4. **Identify risks and mitigations**:
   - Stories with high uncertainty or complexity
   - External dependencies that could slip
   - Knowledge concentration (only one person can do it)
   - Suggest mitigations for each risk

5. **Create the sprint plan summary**:

   ```
   Sprint Goal: [One sentence describing what success looks like]
   Duration: [2 weeks / 1 week / etc.]
   Team Capacity: [X story points]
   Committed Stories: [Y story points across Z stories]
   Buffer: [remaining capacity]

   Stories:
   1. [Story title] — [points] — [owner] — [dependencies]
   ...

   Risks:
   - [Risk] → [Mitigation]
   ```

6. **Define the sprint goal**: A single, clear sentence that captures the sprint's primary value delivery.

Think step by step. Save as markdown.

---

### Further Reading

- [Product Owner vs Product Manager: What's the difference?](https://www.productcompass.pm/p/product-manager-vs-product-owner)
```

## File: `pm-execution/skills/stakeholder-map/SKILL.md`
```markdown
---
name: stakeholder-map
description: "Build a stakeholder map using a power/interest grid, identify communication strategies per quadrant, and generate a communication plan. Use when managing stakeholders, preparing for a launch, aligning cross-functional teams, or planning stakeholder engagement."
---

## Stakeholder Mapping & Communication Plan

Map stakeholders on a Power × Interest grid and create a tailored communication plan for each group.

### Context

You are helping build a stakeholder map for **$ARGUMENTS**.

If the user provides files (org charts, project briefs, team rosters), read them first. If they describe the product or initiative, use that context to infer likely stakeholders.

### Instructions

1. **Identify stakeholders**: List all relevant individuals and groups — executives, engineering leads, designers, marketing, sales, support, legal, finance, external partners, and end users.

2. **Classify each stakeholder** on two dimensions:
   - **Power** (High/Low): Their ability to influence decisions, resources, or outcomes
   - **Interest** (High/Low): How much the project directly affects them or how engaged they are

3. **Place stakeholders in the Power × Interest grid**:

   | | High Interest | Low Interest |
   |---|---|---|
   | **High Power** | **Manage Closely** — Regular 1:1s, involve in decisions, seek their input early | **Keep Satisfied** — Periodic updates, escalate only critical issues |
   | **Low Power** | **Keep Informed** — Regular status updates, invite to demos, gather feedback | **Monitor** — Light-touch updates, available on request |

4. **For each quadrant**, recommend:
   - Communication frequency (daily, weekly, bi-weekly, monthly)
   - Communication format (1:1, email, Slack, meeting, dashboard)
   - Key messages and framing
   - Potential risks if this stakeholder is neglected

5. **Create a communication plan table**:

   | Stakeholder | Role | Power | Interest | Strategy | Frequency | Channel | Key Message |
   |---|---|---|---|---|---|---|---|

6. **Flag potential conflicts**: Identify stakeholders with competing interests and suggest alignment strategies.

Think step by step. Save the stakeholder map as a markdown document.

---

### Further Reading

- [The Product Management Frameworks Compendium + Templates](https://www.productcompass.pm/p/the-product-frameworks-compendium)
- [Team Topologies: A Handbook to Set and Scale Product Teams](https://www.productcompass.pm/p/team-topologies-a-handbook-to-set)
```

## File: `pm-execution/skills/summarize-meeting/SKILL.md`
```markdown
---
name: summarize-meeting
description: "Summarize a meeting transcript into structured notes with date, participants, topic, key decisions, summary points, and action items. Use when processing meeting recordings, creating meeting notes, writing meeting minutes, or recapping discussions."
---

# Summarize Meeting

## Purpose

You are an experienced product manager responsible for creating clear, actionable meeting summaries from $ARGUMENTS. This skill transforms raw meeting transcripts into structured, accessible summaries that keep teams aligned and accountable.

## Context

Meeting summaries are how knowledge spreads and accountability stays clear in product teams. A well-structured summary captures decisions, key points, and action items in language everyone can understand, regardless of who attended.

## Instructions

1. **Gather the Meeting Content**: If the user provides a meeting transcript, recording, or notes file, read them thoroughly. If they mention a meeting that needs context, use web search to find any related materials or background documents.

2. **Think Step by Step**:
   - Who attended and what were their roles?
   - What was the main topic or agenda?
   - What decisions were made?
   - What are the next steps and who owns them?
   - Are there open questions or blockers?

3. **Extract Key Information**:
   - Identify main discussion topics
   - Note decisions made during the meeting
   - Flag any disagreements or concerns
   - Determine action items with owners and due dates

4. **Create Structured Summary**: Use this template:

   ```
   ## Meeting Summary

   **Date & Time**: [Date and start/end time]

   **Participants**: [Full names and roles, if available]

   **Topic**: [Short title—what was the meeting about?]

   **Summary**

   - **Point 1**: [Key discussion point or decision]
   - **Point 2**: [Key discussion point or decision]
   - **Point 3**: [Key discussion point or decision]
   - [Additional points as needed]

   **Action Items**

   | Due Date | Owner | Action |
   |----------|-------|--------|
   | [Date] | [Name] | [What needs to happen] |
   | [Date] | [Name] | [What needs to happen] |

   **Decisions Made**
   - [Decision 1]
   - [Decision 2]

   **Open Questions**
   - [Unresolved question 1]
   - [Unresolved question 2]
   ```

5. **Use Accessible Language**: Write for a primary school graduate. Use simple terms. Avoid jargon or explain it briefly.

6. **Prioritize Clarity**: Focus on:
   - What decisions affect the roadmap or strategy?
   - What does each person need to do?
   - By when do they need to do it?

7. **Save the Output**: Save as a markdown document: `Meeting-Summary-[date]-[topic].md`

## Notes

- Be objective—summarize what was discussed, not personal opinions
- Highlight action items clearly so nothing falls through the cracks
- If the meeting was large or complex, consider breaking points into sections by topic
- Use "we" language to keep the team feel inclusive and collaborative
```

## File: `pm-execution/skills/test-scenarios/SKILL.md`
```markdown
---
name: test-scenarios
description: "Create comprehensive test scenarios from user stories with test objectives, starting conditions, user roles, step-by-step actions, and expected outcomes. Use when writing QA test cases, creating test plans, defining acceptance tests, or preparing for feature validation."
---
# Test Scenarios

Create comprehensive test scenarios from user stories with test objectives, starting conditions, user roles, step-by-step test actions, and expected outcomes.

**Use when:** Writing QA test cases, creating test plans, defining acceptance test scenarios, or validating user story implementations.

**Arguments:**
- `$PRODUCT`: The product or system name
- `$USER_STORY`: The user story to test (title and acceptance criteria)
- `$CONTEXT`: Additional testing context or constraints

## Step-by-Step Process

1. **Review the user story** and acceptance criteria
2. **Define test objectives** - What specific behavior to validate
3. **Establish starting conditions** - System state, data setup, configurations
4. **Identify user roles** - Who performs the test actions
5. **Create test steps** - Break down interactions step-by-step
6. **Define expected outcomes** - Observable results after each step
7. **Consider edge cases** - Invalid inputs, boundary conditions
8. **Output detailed test scenarios** - Ready for QA execution

## Scenario Template

**Test Scenario:** [Clear scenario name]

**Test Objective:** [What this test validates]

**Starting Conditions:**
- [System state required]
- [Data or configuration needed]
- [User setup or permissions]

**User Role:** [Who performs the test]

**Test Steps:**
1. [First action and its expected result]
2. [Second action and observable outcome]
3. [Third action and system behavior]
4. [Completion action and final state]

**Expected Outcomes:**
- [Observable result 1]
- [Observable result 2]
- [Observable result 3]

## Example Test Scenario

**Test Scenario:** View Recently Viewed Products on Product Page

**Test Objective:** Verify that the 'Recently viewed' section displays correctly and excludes the current product.

**Starting Conditions:**
- User is logged in or has browser history enabled
- User has viewed at least 2 products in the current session
- User is now on a product page different from previously viewed items

**User Role:** Online Shopper

**Test Steps:**
1. Navigate to any product page → Section should appear at bottom with previously viewed items
2. Scroll to bottom of page → "Recently viewed" section is visible with product cards
3. Verify product thumbnails → Images, titles, and prices are displayed correctly
4. Check current product → Current product is NOT in the recently viewed list
5. Click on a product card → User navigates to the corresponding product page

**Expected Outcomes:**
- Recently viewed section appears only after viewing at least 1 prior product
- Section displays 4-8 product cards with complete information
- Current product is excluded from the list
- Each card shows "Viewed X minutes/hours ago" timestamp
- Clicking cards navigates to correct product pages
- Performance: Section loads within 2 seconds

## Output Deliverables

- Comprehensive test scenarios for each acceptance criterion
- Clear test objectives aligned with user story intent
- Detailed step-by-step test actions
- Observable expected outcomes after each step
- Edge case and error scenario coverage
- Ready for QA team execution and documentation
```

## File: `pm-execution/skills/user-stories/SKILL.md`
```markdown
---
name: user-stories
description: "Create user stories following the 3 C's (Card, Conversation, Confirmation) and INVEST criteria with descriptions, design links, and acceptance criteria. Use when writing user stories, breaking down features into backlog items, or defining acceptance criteria."
---
# User Stories

Create user stories following the 3 C's (Card, Conversation, Confirmation) and INVEST criteria. Generates stories with descriptions, design links, and acceptance criteria.

**Use when:** Writing user stories, breaking down features into stories, creating backlog items, or defining acceptance criteria.

**Arguments:**
- `$PRODUCT`: The product or system name
- `$FEATURE`: The new feature to break into stories
- `$DESIGN`: Link to design files (Figma, Miro, etc.)
- `$ASSUMPTIONS`: Key assumptions or context

## Step-by-Step Process

1. **Analyze the feature** based on provided design and context
2. **Identify user roles** and distinct user journeys
3. **Apply 3 C's framework:**
   - Card: Simple title and one-liner
   - Conversation: Detailed discussion of intent
   - Confirmation: Clear acceptance criteria
4. **Respect INVEST criteria:** Independent, Negotiable, Valuable, Estimable, Small, Testable
5. **Use plain language** a primary school graduate can understand
6. **Link to design files** for visual reference
7. **Output user stories** in structured format

## Story Template

**Title:** [Feature name]

**Description:** As a [user role], I want to [action], so that [benefit].

**Design:** [Link to design files]

**Acceptance Criteria:**
1. [Clear, testable criterion]
2. [Observable behavior]
3. [System validates correctly]
4. [Edge case handling]
5. [Performance or accessibility consideration]
6. [Integration point]

## Example User Story

**Title:** Recently Viewed Section

**Description:** As an Online Shopper, I want to see a 'Recently viewed' section on the product page to easily revisit items I considered.

**Design:** [Figma link]

**Acceptance Criteria:**
1. The 'Recently viewed' section is displayed at the bottom of the product page for every user who has previously viewed at least 1 product.
2. It is not displayed for users visiting the first product page of their session.
3. The current product itself is excluded from the displayed items.
4. The section showcases product cards or thumbnails with images, titles, and prices.
5. Each product card indicates when it was viewed (e.g., 'Viewed 5 minutes ago').
6. Clicking on a product card leads the user to the corresponding product page.

## Output Deliverables

- Complete set of user stories for the feature
- Each story includes title, description, design link, and 4-6 acceptance criteria
- Stories are independent and can be developed in any order
- Stories are sized for one sprint cycle
- Stories reference related design documentation

---

### Further Reading

- [How to Write User Stories: The Ultimate Guide](https://www.productcompass.pm/p/how-to-write-user-stories)
```

## File: `pm-execution/skills/wwas/SKILL.md`
```markdown
---
name: wwas
description: "Create product backlog items in Why-What-Acceptance format — independent, valuable, testable items with strategic context. Use when writing structured backlog items, breaking features into work items, or using the WWA format."
---
# Why-What-Acceptance (WWA)

Create product backlog items in Why-What-Acceptance format. Produces independent, valuable, testable items with strategic context.

**Use when:** Writing backlog items, creating product increments, breaking features into work items, or communicating strategic intent to teams.

**Arguments:**
- `$PRODUCT`: The product or system name
- `$FEATURE`: The new feature or capability
- `$DESIGN`: Link to design files (Figma, Miro, etc.)
- `$ASSUMPTIONS`: Key assumptions and strategic context

## Step-by-Step Process

1. **Define the strategic Why** - Connect work to business and team objectives
2. **Describe the What** - Keep descriptions concise, reference designs
3. **Write Acceptance Criteria** - High-level, not detailed specifications
4. **Ensure independence** - Items can be developed in any order
5. **Keep items negotiable** - Invite team conversation, not constraints
6. **Make items valuable** - Each delivers measurable user or business value
7. **Ensure testability** - Outcomes are observable and verifiable
8. **Size appropriately** - Small enough for one sprint estimate

## Item Template

**Title:** [What will be delivered]

**Why:** [1-2 sentences connecting to strategic context and team objectives]

**What:** [Short description and design link. 1-2 paragraphs maximum. A reminder of discussion, not detailed specification.]

**Acceptance Criteria:**
- [Observable outcome 1]
- [Observable outcome 2]
- [Observable outcome 3]
- [Observable outcome 4]

## Example WWA Item

**Title:** Implement Real-Time Spending Tracker

**Why:** Users need immediate feedback on spending to make conscious budget decisions. This directly supports our goal to improve financial awareness and reduce overspending.

**What:** Add a real-time spending tracker that updates as users log expenses. The tracker displays their current week's spending against their set budget. Designs available in [Figma link]. This is a reminder of our discussions - detailed specifications will emerge during development conversations with the team.

**Acceptance Criteria:**
- Spending totals update within 2 seconds of logging an expense
- Budget progress is visually indicated with a progress bar
- Users can see remaining budget amount at a glance
- System handles multiple expense categories correctly

## Output Deliverables

- Complete set of backlog items for the feature
- Each item includes Why, What, and Acceptance Criteria sections
- Items are independent and deliverable in any order
- Items are sized for estimation and completion in one sprint
- Strategic context is clear for team decision-making
- Design references are included for implementation guidance

---

### Further Reading

- [How to Write User Stories: The Ultimate Guide](https://www.productcompass.pm/p/how-to-write-user-stories)
```

## File: `pm-go-to-market/README.md`
```markdown
# pm-go-to-market

Go-to-market skills for PMs: GTM strategy, growth loops, GTM motions, beachhead segments, and ideal customer profiles.

## Skills (6)

- **beachhead-segment** — Identify the first beachhead market segment for a product launch.
- **competitive-battlecard** — Create sales-ready competitive battlecards comparing your product against a specific competitor.
- **growth-loops** — Identify growth loops (flywheels) for sustainable traction.
- **gtm-motions** — Identify the best GTM motions and tools.
- **gtm-strategy** — Create a go-to-market strategy for a product launch covering marketing channels, messaging, success metrics, and launch plan.
- **ideal-customer-profile** — Identify the Ideal Customer Profile (ICP) from research data with demographics, behaviors, JTBD, and needs.

## Commands (3)

- `/pm-go-to-market:battlecard` — Create a sales-ready competitive battlecard — positioning, feature comparison, objection handling, and win strategies.
- `/pm-go-to-market:growth-strategy` — Design sustainable growth mechanisms — growth loops and GTM motions for product-led and sales-led strategies.
- `/pm-go-to-market:plan-launch` — Create a full go-to-market strategy — beachhead segment, ICP, messaging, channels, and launch plan.

## Author

Paweł Huryn — [The Product Compass Newsletter](https://www.productcompass.pm)

## License

MIT
```

## File: `pm-go-to-market/commands/battlecard.md`
```markdown
---
description: Create a sales-ready competitive battlecard — positioning, feature comparison, objection handling, and win strategies
argument-hint: "<your product> vs <competitor>"
---

# /battlecard -- Competitive Battlecard

Create a concise, sales-ready battlecard that helps your team win deals against a specific competitor. Includes positioning, feature comparison, objection handling, and conversation strategies.

## Invocation

```
/battlecard Our CRM vs Salesforce
/battlecard ProjectFlow vs Monday.com for mid-market teams
/battlecard [upload competitor materials or win/loss data]
```

## Workflow

### Step 1: Identify the Matchup

Ask:
- Your product and the specific competitor
- Who is the typical buyer choosing between you?
- Do you have win/loss data or sales feedback?
- What deal stage does this typically come up? (early evaluation, final decision, displacement)

### Step 2: Research the Competitor

Apply the **competitive-battlecard** skill with web research:

- Current product capabilities and recent launches
- Pricing model and published pricing
- Target market and positioning
- Known weaknesses (from reviews, forums, customer feedback)
- Recent company news (funding, leadership, strategy shifts)

### Step 3: Generate Battlecard

```
## Competitive Battlecard: [Your Product] vs [Competitor]

**Last updated**: [today]
**Use when**: [situation where this competitor comes up]

### Quick Summary
**We win when**: [buyer profile and situation where you have advantage]
**We lose when**: [buyer profile and situation where competitor has advantage]
**Key differentiator**: [one sentence]

### Positioning
**How they position**: [their messaging]
**How we position against them**: [our counter-positioning]

### Feature Comparison
| Capability | Us | Them | Verdict |
|-----------|-----|------|---------|
| [capability] | [status] | [status] | [advantage] |

### Pricing Comparison
| Dimension | Us | Them | Notes |
|----------|-----|------|-------|

### Objection Handling
| Objection | Response | Proof Point |
|----------|---------|------------|
| "They have [feature]" | [response] | [evidence] |
| "They're cheaper" | [response] | [TCO analysis] |
| "They're more established" | [response] | [counter] |

### Landmines to Plant
[Questions to ask the prospect that expose competitor weaknesses]
1. "Ask them about [topic] — their answer will reveal [weakness]"

### Trap Questions to Expect
[Questions the competitor will encourage the prospect to ask you]
1. "[Question]" — How to respond: [response]

### Win/Loss Patterns
**We typically win because**: [top 3 reasons]
**We typically lose because**: [top 3 reasons]

### Conversation Starters
**If they're already using [Competitor]**:
- [approach for displacement deals]

**If they're evaluating both**:
- [approach for competitive evaluations]

### Resources
- [Customer story / case study that counters this competitor]
- [Third-party comparison or review]
- [Demo script optimized for this competitive situation]
```

Save as markdown.

### Step 4: Offer Next Steps

- "Want me to **create battlecards for other competitors**?"
- "Should I **run a full competitive analysis** of the market?"
- "Want me to **draft customer-facing comparison content** based on this?"
- "Should I **update the positioning** based on competitive insights?"

## Notes

- Battlecards should be updated quarterly — competitors change fast
- "Landmines" are the most valuable section for sales — teach reps what questions to ask
- Never trash the competitor in front of the prospect — position on your strengths, not their weaknesses
- Win/loss data from real deals is worth 10x any analysis — encourage the user to add it
- Keep it to one page equivalent — sales reps won't read a 10-page document during a call
```

## File: `pm-go-to-market/commands/growth-strategy.md`
```markdown
---
description: Design sustainable growth mechanisms — growth loops and GTM motions for product-led and sales-led strategies
argument-hint: "<product or growth challenge>"
---

# /growth-strategy -- Growth Loops & GTM Motions

Identify and design the growth mechanisms that will drive sustainable traction. Evaluates five growth loop types and seven GTM motions to build a balanced acquisition and expansion strategy.

## Invocation

```
/growth-strategy B2B collaboration tool — growth has stalled at 5K users
/growth-strategy Consumer fitness app looking for viral growth
/growth-strategy [upload product metrics or growth data]
```

## Workflow

### Step 1: Understand Growth Context

Ask:
- What is the product? Who uses it?
- Current growth metrics: user count, growth rate, acquisition channels
- What's working? What's not?
- Business model: how does revenue relate to user growth?
- Team and budget: what resources can you put toward growth?

### Step 2: Evaluate Growth Loops

Apply the **growth-loops** skill:

Analyze five growth loop types for your product:

1. **Viral Loop**: Users invite others as part of natural product use
2. **Usage Loop**: More usage creates more value, bringing users back
3. **Collaboration Loop**: Product becomes more valuable when used with others
4. **User-Generated Content Loop**: Users create content that attracts new users
5. **Referral Loop**: Satisfied users actively recommend to others

For each applicable loop: mechanism, requirements, expected impact, implementation effort.

### Step 3: Evaluate GTM Motions

Apply the **gtm-motions** skill:

Assess seven GTM approaches:

1. **Inbound**: Content, SEO, thought leadership
2. **Outbound**: Sales, cold outreach, account-based
3. **Paid Digital**: SEM, social ads, display, retargeting
4. **Community**: Forums, events, user groups, developer relations
5. **Partners**: Integrations, resellers, co-marketing
6. **ABM (Account-Based Marketing)**: Targeted enterprise acquisition
7. **PLG (Product-Led Growth)**: Free tier, self-serve, product virality

For each: fit for your product, expected CAC, timeline to results, tools needed.

### Step 4: Design Growth Strategy

```
## Growth Strategy: [Product]

**Date**: [today]
**Current state**: [user count, growth rate, key channels]
**Growth goal**: [target]

### Recommended Growth Loops
| Loop Type | Mechanism | Fit | Impact | Effort | Priority |
|----------|-----------|-----|--------|--------|----------|

### Primary Growth Loop: [Type]
**How it works**: [step-by-step mechanism]
**Requirements**: [what needs to be true/built]
**Key metrics**: [how to measure loop health]
**Implementation plan**: [concrete next steps]

### Secondary Growth Loop: [Type]
[same format]

### GTM Motion Mix
| Motion | Investment | Expected ROI | Timeline | Tools |
|--------|-----------|-------------|----------|-------|

### Growth Experiments
| # | Experiment | Tests What | Effort | Expected Learning |
|---|-----------|-----------|--------|------------------|

### Growth Metrics Framework
- **North Star**: [growth metric]
- **Loop health**: [metrics per loop]
- **CAC by channel**: [tracking approach]
- **Payback period**: [target]

### 90-Day Growth Plan
**Month 1**: [focus areas and experiments]
**Month 2**: [scale what works, cut what doesn't]
**Month 3**: [optimize and systematize]
```

Save as markdown.

### Step 5: Offer Next Steps

- "Want me to **plan a specific launch campaign**?"
- "Should I **create marketing content** for the inbound motion?"
- "Want me to **set up metrics** to track growth loop health?"
- "Should I **design a referral program** based on the referral loop?"

## Notes

- Growth loops compound; growth tactics don't — prioritize loops over one-off campaigns
- The best growth loop uses the product itself as the channel (PLG, viral, collaboration)
- Not every loop works for every product — a B2B analytics tool won't go viral on TikTok
- Budget should follow learning: invest small in experiments, then scale what proves out
- CAC should be < 1/3 of LTV for sustainable growth — flag if projected CAC is too high
```

## File: `pm-go-to-market/commands/plan-launch.md`
```markdown
---
description: Create a full go-to-market strategy — beachhead segment, ICP, messaging, channels, and launch plan
argument-hint: "<product or feature to launch>"
---

# /plan-launch -- Go-to-Market Strategy

Build a complete GTM plan from first principles: identify your beachhead market, define the ideal customer, craft messaging, choose channels, and create a launch timeline.

## Invocation

```
/plan-launch AI-powered proposal writer for consulting firms
/plan-launch New enterprise tier for our project management tool
/plan-launch [upload a PRD, strategy doc, or pitch deck]
```

## Workflow

### Step 1: Understand the Launch

Ask:
- What are you launching? (new product, new feature, new tier, market expansion)
- What stage? (pre-launch planning, imminent launch, post-launch optimization)
- Do you have existing customers? Or starting from zero?
- What's the timeline? Any hard deadlines?
- Budget constraints? Team size?

### Step 2: Define Beachhead Segment

Apply the **beachhead-segment** skill:

- Evaluate potential market segments against:
  - Burning pain (how urgently they need this)
  - Willingness to pay (budget and purchase authority)
  - Winnable market share (can you reach and win them)
  - Referral potential (will they tell others)
- Recommend the single best starting segment with rationale
- Map adjacent segments for expansion after beachhead is secured

### Step 3: Define Ideal Customer Profile

Apply the **ideal-customer-profile** skill:

- Demographics: company size, industry, geography, tech stack
- Behaviors: how they discover solutions, buying process, decision makers
- JTBD: specific jobs they're hiring your product for
- Current alternatives: what they use today and why it falls short
- Qualification criteria: how to identify them quickly

### Step 4: Build GTM Strategy

Apply the **gtm-strategy** skill:

- **Positioning**: How you describe yourself to this segment
- **Messaging**: Key messages for different stakeholders (buyer, user, influencer)
- **Channels**: Where and how to reach your ICP (ranked by expected ROI)
- **Launch tactics**: Specific actions for pre-launch, launch day, and post-launch
- **Pricing alignment**: How pricing supports the GTM motion
- **Success metrics**: How you'll know the launch worked

### Step 5: Generate GTM Plan

```
## Go-to-Market Plan: [Product/Feature]

**Launch date**: [target]
**Type**: [new product / feature / tier / market expansion]

### Beachhead Segment
**Who**: [specific segment definition]
**Why them first**: [rationale against criteria]
**Size**: [TAM/SAM/SOM estimate]

### Ideal Customer Profile
| Attribute | Definition |
|-----------|-----------|
| Company size | [range] |
| Industry | [specific] |
| Decision maker | [title/role] |
| Key JTBD | [job they need done] |
| Current solution | [what they use today] |
| Qualification signal | [how to identify them] |

### Positioning & Messaging
**Positioning statement**: For [who] who [need], [product] is [category] that [benefit]. Unlike [alternative], we [differentiator].

**Key messages by stakeholder**:
| Audience | Message | Proof Point |
|----------|---------|------------|

### Channel Strategy
| Channel | Tactic | Reach | Cost | Priority |
|---------|--------|-------|------|----------|

### Launch Timeline
| Phase | Timing | Actions | Owner |
|-------|--------|---------|-------|
| Pre-launch | [dates] | [list] | [who] |
| Launch week | [dates] | [list] | [who] |
| Post-launch | [dates] | [list] | [who] |

### Success Metrics
| Metric | 30-day target | 90-day target |
|--------|-------------|-------------|

### Risks & Mitigations
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|

### Expansion Plan
[After beachhead: which adjacent segments, in what order, with what adaptations]
```

Save as markdown.

### Step 6: Offer Next Steps

- "Want me to **design growth loops** for post-launch traction?"
- "Should I **create competitive battlecards** for sales?"
- "Want me to **draft marketing copy** for the launch?"
- "Should I **build a metrics dashboard** for launch tracking?"

## Notes

- "Everyone" is not a segment — the tighter the beachhead, the faster you learn
- The ICP should be specific enough that sales/marketing can identify prospects in 30 seconds
- Messaging should use the customer's language, not your internal terminology
- Pre-launch activities (waitlist, beta, early access) are as important as launch day
- Plan for post-launch: the first 90 days after launch determine long-term trajectory
```

## File: `pm-go-to-market/skills/beachhead-segment/SKILL.md`
```markdown
---
name: beachhead-segment
description: "Identify the first beachhead market segment for a product launch. Evaluates segments against burning pain, willingness to pay, winnable market share, and referral potential. Use when choosing a first market, targeting an initial customer segment, or planning market entry strategy."
---
# Beachhead Segment

## Overview
Identify the first beachhead market segment for product launch. This skill evaluates potential market segments against key criteria to find your initial winning segment that enables fast PMF validation and adjacent expansion.

## When to Use
- Choosing a first market for your product
- Targeting an initial customer segment
- Planning initial market entry strategy
- Deciding where to focus limited resources
- Validating GTM assumptions with early adopters

## Key Evaluation Criteria

### 1. Burning Pain Point
Does this segment experience an acute, unmet problem?
- Daily frustration with the status quo
- Significant productivity loss or cost impact
- Emotional urgency to find a solution
- Current workarounds are expensive or fragile
- Problem is getting worse over time

### 2. Willingness to Pay
Does this segment have budget and motivation to pay for a solution?
- Documented budget allocation for this problem area
- ROI is clear and compelling (value > cost)
- Economic impact of problem justifies solution cost
- Decision-maker has autonomy or influence over budget
- No free or DIY alternatives that fully satisfy need

### 3. Winnable Market Share
Can you realistically capture 60-70% of this segment in 3-18 months?
- Segment is large enough but not oversaturated
- Limited competition or easy differentiation
- Market players are fragmented or complacent
- Your product has clear competitive advantage
- You have unique access or distribution advantage

### 4. Referral Potential
Will customers naturally refer or recommend to others?
- Segment contains professional communities
- Customers interact with adjacent segments (expansion opportunity)
- High word-of-mouth culture in this industry
- Network effects within the segment
- Solving problem for one creates demand in adjacent segments

## How It Works

### Step 1: List Potential Segments
Brainstorm all possible target segments:
- Industry verticals (SaaS, healthcare, manufacturing, etc.)
- Company size (SMB, mid-market, enterprise)
- Job titles or roles
- Geographic regions
- Use cases or use-case variations
- Customer maturity level

### Step 2: Research Pain Points
Validate burning pain in each segment:
- Customer interviews and discovery calls
- Problem validation through surveys
- Market research and analyst reports
- Competitor positioning and customer reviews
- Quantify cost/impact of the problem
- Identify current workarounds and limitations

### Step 3: Assess Willingness to Pay
Determine budget and economic viability:
- Segment's budget for this problem category
- ROI calculation (value gained vs cost)
- Current spending on solutions or workarounds
- Budget decision-making process
- Typical deal size expectations
- Pricing sensitivity in the segment

### Step 4: Evaluate Winnability
Assess realistic market share potential:
- Total addressable market (TAM) size
- Competitive landscape and positioning
- Your differentiation or unfair advantage
- Distribution access to this segment
- Time and resources required
- Market growth and momentum

### Step 5: Identify Referral Pathways
Map expansion opportunities:
- Adjacent segments that reference segment influences
- Network effects within the segment
- Professional communities and associations
- Customer-to-customer recommendations
- Natural expansion path to adjacent markets
- Viral or network effects from solving core pain

### Step 6: Select Beachhead
Choose your primary launch segment:
- Highest combined score across four criteria
- Most achievable for your current resources
- Shortest path to PMF and revenue
- Best reference for adjacent expansion
- Most enthusiastic early customer cohort

## Input Format
Use $ARGUMENTS to pass:
- Product description and capabilities
- Initial market research and validation data
- Potential segment options
- Constraints and limitations
- Timeline and resource constraints
- Current customer data or feedback

## Output
A beachhead segment analysis including:
- Top 3-5 recommended segments with scoring
- Primary beachhead segment recommendation
- Pain point validation and evidence
- Willingness to pay assessment and pricing guidance
- Realistic market share and revenue projections
- Referral and expansion pathways to adjacent segments
- 90-day customer acquisition plan for beachhead
- Post-beachhead expansion roadmap

## Framework
Based on Geoffrey Moore's beachhead market strategy in "Crossing the Chasm." Focuses on finding the smallest winnable, referenceable market that validates PMF and enables expansion.

## Tips
- Start absurdly specific. A niche beachhead is better than a vague mass market
- Choose the segment most likely to evangelize your solution
- Validate all four criteria with at least 10 customer interviews
- Select segment with fastest path to revenue and references
- Ensure beachhead can reference to adjacent market segments
- Focus all resources on dominating the beachhead (not diluting efforts)
- Plan exit from beachhead only after 60%+ market share

---

### Further Reading

- [5 GTM Principles You Should Know as a PM](https://www.productcompass.pm/p/5-gtm-principles-with-frameworks-templates)
- [Product-Led Growth 101, Part 1/2](https://www.productcompass.pm/p/product-led-growth-101-12)
- [How to Design a Value Proposition Customers Can't Resist?](https://www.productcompass.pm/p/how-to-design-value-proposition-template)
- [How to Achieve Product-Market Fit? Part I: Market and Value Proposition](https://www.productcompass.pm/p/how-to-achieve-the-product-market)
```

## File: `pm-go-to-market/skills/competitive-battlecard/SKILL.md`
```markdown
---
name: competitive-battlecard
description: "Create sales-ready competitive battlecards comparing your product against a specific competitor — positioning, feature comparison, objection handling, and win/loss patterns. Use when preparing sales teams, creating competitive materials, or responding to 'why not competitor X?'"
---

## Competitive Battlecard

Create a concise, sales-ready battlecard for use against a specific competitor.

### Context

You are creating a competitive battlecard for **$ARGUMENTS**.

Use web search to research the competitor's current product, pricing, positioning, and recent changes. If the user provides files (feature lists, win/loss data, sales call notes), read them first.

### Instructions

1. **Research the competitor** (use web search):
   - Current product offerings and features
   - Pricing tiers and model
   - Target market and positioning
   - Recent product launches or changes
   - Known strengths and weaknesses
   - Customer reviews and sentiment (G2, Capterra, Reddit)

2. **Create the battlecard** with these sections:

   ### Company Overview
   - Founded, HQ, funding/revenue (if public)
   - Target market and ICP
   - Positioning in one sentence

   ### Quick Comparison

   | Capability | Us | Them | Winner |
   |---|---|---|---|
   | [Feature area 1] | [Our approach] | [Their approach] | [Us/Them/Tie] |
   | [Feature area 2] | ... | ... | ... |
   | Pricing | ... | ... | ... |
   | Support | ... | ... | ... |

   ### Where We Win
   - [Advantage 1]: [Proof point or customer quote]
   - [Advantage 2]: [Specific capability they lack]
   - [Advantage 3]: [Better approach with reasoning]

   ### Where They Win
   - [Their strength 1]: [Our counter-positioning]
   - [Their strength 2]: [How we mitigate this gap]

   ### Common Objections & Responses

   | Prospect Says | Respond With |
   |---|---|
   | "Competitor X has [feature]" | "[Our alternative approach and why it's better for them]" |
   | "They're cheaper" | "[Value framing: total cost of ownership, ROI, hidden costs]" |
   | "They're more established" | "[Our advantages: speed, innovation, focus, support]" |

   ### Landmines to Plant
   Questions to ask the prospect that highlight competitor weaknesses:
   - "How important is [area where we excel] to your team?"
   - "Have you evaluated [specific capability they lack]?"

   ### Win/Loss Patterns
   - We tend to win when: [pattern]
   - We tend to lose when: [pattern]
   - Key differentiator in competitive deals: [what tips the scale]

3. **Keep it scannable**: Sales reps need to reference this during calls. Use tables, bold text, and short bullets.

Save as markdown. Format for easy printing or sharing in Notion/Confluence.

---

### Further Reading

- [How to Design a Value Proposition Customers Can't Resist?](https://www.productcompass.pm/p/how-to-design-value-proposition-template)
```

## File: `pm-go-to-market/skills/growth-loops/SKILL.md`
```markdown
---
name: growth-loops
description: "Identify growth loops (flywheels) for sustainable traction. Evaluates 5 loop types: Viral, Usage, Collaboration, User-Generated, and Referral. Use when designing growth mechanisms, building product-led traction, or understanding how growth loops work."
---
# Growth Loops

## Overview
Identify and design growth loops (flywheels) that create sustainable traction. This skill evaluates five proven growth loop mechanisms to reduce reliance on paid acquisition and build product-led growth.

## When to Use
- Designing growth mechanisms for a product
- Building sustainable viral or referral traction
- Reducing reliance on paid acquisition
- Analyzing competitor growth strategies
- Optimizing product for product-led growth

## The 5 Growth Loop Types

### 1. Viral Loop
Product content created by users gets shared on external platforms, bringing new users back to the product.
- **Mechanism**: Users create content in-product → Share on social/external platforms → New users discover and signup
- **Example**: Figma designs shared as links, Loom videos shared in emails
- **Strength**: Exponential user acquisition if content is inherently shareable
- **Challenge**: Requires highly shareable output and strong incentive to share

### 2. Usage Loop
Users create content or value within the product, then share it, which invites new users or drives re-engagement.
- **Mechanism**: User creates → Shares creation → Others consume → Become engaged users
- **Example**: Twitter threads, Medium articles, Notion templates shared publicly
- **Strength**: Growth tied directly to product usage and network effects
- **Challenge**: Requires content creation friction to be very low

### 3. Collaboration Loop
Users invite colleagues to co-create or collaborate within the product, expanding the user base within organizations.
- **Mechanism**: User creates → Invites colleagues for collaboration → Colleagues discover product value
- **Example**: Google Docs invitations, Figma team projects, Slack channels
- **Strength**: Deep organizational penetration and high retention
- **Challenge**: Works best for collaborative/team-based products

### 4. User-Generated Loop
Users discover new content or features through other users' creations, then create and share their own content.
- **Mechanism**: User discovers content → Creates similar content → Shares creation → Others discover
- **Example**: TikTok, Pinterest, YouTube trends driving creator participation
- **Strength**: Creates content flywheel and network effects
- **Challenge**: Requires critical mass of quality content to sustain

### 5. Referral Loop
Users invite other potential users in exchange for rewards, incentives, or social recognition.
- **Mechanism**: User refers → Referred user joins → Referrer gets reward → Shares more referrals
- **Example**: Dropbox referral bonus, Uber rider referrals, PayPal signup bonuses
- **Strength**: Directly incentivizes acquisition; easy to measure ROI
- **Challenge**: Requires valuable incentive without eroding unit economics

## How It Works

### Step 1: Define Product Value
Clarify the core value users experience:
- Primary action users take in your product
- Value created per user action
- Network effects present (if any)
- Friction points in the experience

### Step 2: Evaluate Loop Fit
Assess which growth loops align with your product:
- Product type (collaborative, content-based, utility, etc.)
- Target user behavior and sharing habits
- Network effects already present
- Existing user base and engagement

### Step 3: Design Loop Mechanics
Create specific loop implementation:
- Trigger that initiates sharing or invitations
- Incentive for participation (intrinsic or extrinsic)
- Ease of sharing mechanism
- Conversion rate from invite to activation
- Frequency of loop repetition per user

### Step 4: Calculate Loop Coefficient
Estimate growth velocity:
- Invites/shares per user per cycle
- Conversion rate of invites to new users
- Net new users per cycle
- Time per cycle iteration

### Step 5: Build the Loop
Implement the highest-leverage loop first:
- Start with the most natural loop for your product
- Optimize messaging and friction
- Measure loop metrics and conversion rates
- Compound results over time

## Input Format
Use $ARGUMENTS to pass:
- Product description and primary user action
- Target user demographics and behavior
- Existing sharing/collaboration features
- Current growth channels and metrics
- Constraints or opportunities

## Output
A growth loops analysis including:
- Ranked evaluation of all 5 loop types for your product
- Recommended primary growth loop with implementation plan
- Secondary loops to layer over time
- Key metrics and measurement framework
- 30-60-90 day implementation roadmap
- Potential loop coefficient and growth projections

## Framework
Based on growth loops research by Ognjen Bošković. Focuses on compounding user acquisition through built-in, product-native sharing and collaboration mechanisms.

## Tips
- Start with one loop and master it before adding complexity
- Viral loops compound fastest but take time to build
- Collaboration loops create strongest retention and LTV
- Measure loop health weekly during optimization phase
- Combine loops for multiplicative effect once operating at scale

---

### Further Reading

- [Product-Led Growth 101, Part 1/2](https://www.productcompass.pm/p/product-led-growth-101-12)
- [OpenAI’s Product Leader Shares 3-Layer Distribution Framework To Win Mind & Market Share in the AI World](https://www.productcompass.pm/p/distribution-framework-ai-products)
- [How to Design a Value Proposition Customers Can't Resist?](https://www.productcompass.pm/p/how-to-design-value-proposition-template)
```

## File: `pm-go-to-market/skills/gtm-motions/SKILL.md`
```markdown
---
name: gtm-motions
description: "Identify the best GTM motions and tools across 7 motion types: Inbound, Outbound, Paid Digital, Community, Partners, ABM, and PLG. Use when selecting marketing channels, choosing between inbound and outbound strategy, or planning cross-channel campaigns."
---
# GTM Motions

## Overview
Identify and evaluate the best go-to-market motions for your product. This skill analyzes seven proven GTM approaches with specific tools and tactics to help you build a balanced acquisition strategy.

## When to Use
- Selecting marketing channels for your product
- Choosing between inbound vs outbound strategy
- Building your GTM toolkit and tech stack
- Evaluating PLG vs traditional sales motion
- Planning cross-channel marketing campaigns

## The 7 GTM Motions

### 1. Inbound Marketing
Attract customers through valuable content and thought leadership.
- **Tools**: LinkedIn, SEMRush, Grammarly, HubSpot, Airtable
- **Tactics**: Blog content, webinars, whitepapers, SEO, email nurture sequences
- **Best For**: B2B SaaS, technical products, long sales cycles
- **Strength**: Builds brand authority and attracts high-intent prospects
- **Challenge**: Requires consistent content creation; slower to show results

### 2. Outbound Sales
Proactively reach target prospects through direct engagement.
- **Tools**: LinkedIn Sales Navigator, ZoomInfo, Lemlist, Apollo, Hunter
- **Tactics**: Cold email campaigns, LinkedIn outreach, phone prospecting, personalized demos
- **Best For**: Enterprise sales, high-value contracts, niche markets
- **Strength**: Predictable pipeline generation; control over target selection
- **Challenge**: Low response rates; resource-intensive; requires skilled sales team

### 3. Paid Digital Advertising
Reach target audiences through paid channels with precision targeting.
- **Tools**: Google Ads, Meta Ads, LinkedIn Ads, Newswire, Retargeting platforms
- **Tactics**: Search ads, display advertising, social ads, video advertising, retargeting
- **Best For**: Products with clear target demographics, competitive keywords
- **Strength**: Fast results; scalable; measurable ROI; precise targeting
- **Challenge**: Can be expensive; requires continuous optimization; competitive

### 4. Community Marketing
Build engaged communities where customers help each other and spread the word.
- **Tools**: Slack, Reddit, Discord, Circle, Mighty Networks, WhatsApp
- **Tactics**: Community forums, user groups, events, mentorship, ambassador programs
- **Best For**: Developer products, communities of practice, loyal user bases
- **Strength**: Builds loyalty; organic word-of-mouth; valuable feedback; low CAC
- **Challenge**: Requires active moderation; time to build critical mass

### 5. Partner Marketing
Leverage partner networks to co-market and reach new audiences.
- **Tools**: Miro, AWS Startups, Oracle Partners, Stripe, Shopify App Store
- **Tactics**: Partner integrations, co-marketing agreements, channel partnerships, resellers
- **Best For**: Complementary products, platform ecosystems, expanding market reach
- **Strength**: Access to established customer bases; shared costs; credibility
- **Challenge**: Partner alignment; revenue sharing; dependency on partners

### 6. Account-Based Marketing (ABM)
Treat high-value accounts as individual markets with personalized campaigns.
- **Tools**: Pipedrive, Hunter, Clay, 6sense, Terminus, Demandbase
- **Tactics**: Personalized messaging, account-targeted content, coordinated sales/marketing
- **Best For**: Enterprise deals, limited target accounts, high deal values
- **Strength**: Higher conversion rates; larger deal sizes; strong sales-marketing alignment
- **Challenge**: Requires detailed account research; resource intensive; not scalable to SMB

### 7. Product-Led Growth (PLG)
Drive adoption through the product experience itself with minimal sales friction.
- **Tools**: Hotjar, Amplitude, Sentry, PostHog, Intercom, Appcues
- **Tactics**: Free trials, freemium models, in-app onboarding, self-serve demos, product analytics
- **Best For**: Self-service products, SMB market, low ACV, viral potential
- **Strength**: Low CAC; aligns product and growth; strong PMF signals; scalable
- **Challenge**: Requires excellent product experience; lower price points; longer ROI

## How It Works

### Step 1: Understand Your Product
Define product characteristics:
- Price point and ACV (contract value)
- Sales cycle length
- Buyer type and decision-making process
- Product complexity and learning curve
- Target market size and concentration

### Step 2: Evaluate Market Conditions
Assess your market dynamics:
- Competitive intensity of your keywords/channels
- Target audience location and accessibility
- Budget availability for paid channels
- Your team size and capabilities
- Timeline to revenue generation

### Step 3: Score Each Motion
Rate fit for your product (1-10 scale):
- Inbound: Content creation capability, brand building timeline
- Outbound: Prospect list availability, sales team capacity
- Paid: Budget flexibility, target audience clarity, conversion potential
- Community: Existing communities, product network effects
- Partners: Complementary products, channel availability
- ABM: Deal size and account concentration
- PLG: Product trial-ability, pricing flexibility

### Step 4: Design Motion Stack
Select and prioritize 2-4 motions to execute:
- Primary motion (highest potential for your business)
- Secondary motions (complementary acquisition channels)
- Motion sequencing (which to start first)
- Resource allocation across channels

### Step 5: Build Execution Plan
Create 90-day implementation roadmap:
- Quick wins and early validation
- Team and tool requirements
- Success metrics for each motion
- Optimization and scaling strategy
- Budget and resource allocation

## Input Format
Use $ARGUMENTS to pass:
- Product description and positioning
- Target customer profile and market
- Price point and sales cycle
- Team size and capabilities
- Budget and timeline constraints
- Existing channels or data

## Output
A comprehensive GTM motions analysis including:
- Scoring of all 7 motions for your product
- Recommended motion stack (primary and secondary)
- Tool recommendations for each motion
- 90-day execution plan with milestones
- Resource and budget requirements
- Success metrics and measurement framework
- Competitive differentiation through motion choice

## Framework
Based on Product Compass GTM motion analysis. Provides a systematic approach to balancing customer acquisition across multiple channels.

## Tips
- Most successful products use 2-4 complementary motions
- Start with your strongest motion; add complexity gradually
- Paid channels fund growth while organic channels build long-term value
- Revisit motion mix quarterly as company scales
- Combine inbound (brand) with outbound (sales) for B2B strength
- Use PLG to reduce CAC; use paid to accelerate proven channels

---

### Further Reading

- [5 GTM Principles You Should Know as a PM](https://www.productcompass.pm/p/5-gtm-principles-with-frameworks-templates)
- [OpenAI’s Product Leader Shares 3-Layer Distribution Framework To Win Mind & Market Share in the AI World](https://www.productcompass.pm/p/distribution-framework-ai-products)
- [Product Management vs. Product Marketing vs. Product Growth 101](https://www.productcompass.pm/p/product-management-vs-product-marketing)
- [How to Design a Value Proposition Customers Can't Resist?](https://www.productcompass.pm/p/how-to-design-value-proposition-template)
```

## File: `pm-go-to-market/skills/gtm-strategy/SKILL.md`
```markdown
---
name: gtm-strategy
description: "Create a go-to-market strategy covering marketing channels, messaging, success metrics, and launch timeline. Use when planning a product launch, creating a GTM plan from scratch, or defining a launch strategy for a new market."
---
# GTM Strategy

## Overview
Create a comprehensive go-to-market strategy for a product launch. This skill covers marketing channels, messaging development, success metrics definition, and launch planning.

## When to Use
- Planning a product launch
- Creating a GTM plan from scratch
- Defining a launch strategy for a new market
- Developing product-to-market fit strategy
- Preparing a product go-live roadmap

## How It Works

### Step 1: Gather Research Data
The system will help you load and analyze early research about your product and target market. Provide:
- Product description and key features
- Target market segment details
- Market research or validation data
- Competitive landscape information
- Any available customer interviews or survey data

### Step 2: Define Marketing Channels
Evaluate which channels best reach your target audience:
- Digital marketing channels (paid search, social media, display)
- Content and inbound channels (blog, SEO, thought leadership)
- Sales and outbound channels (direct outreach, partnerships)
- Community and grassroots channels
- Product-led and viral channels

### Step 3: Develop Messaging
Create audience-specific messaging that resonates:
- Core value proposition for target segment
- Key differentiators and competitive advantages
- Pain point validation and solution mapping
- Proof points and social proof strategies
- Channel-specific messaging variations

### Step 4: Define Success Metrics
Establish measurable KPIs to track launch success:
- Awareness metrics (impressions, reach, brand recall)
- Engagement metrics (CTR, cost per engagement, time on site)
- Conversion metrics (signups, demos requested, trials started)
- Revenue metrics (MRR, customer acquisition cost, lifetime value)
- Market metrics (market share, segment penetration)

### Step 5: Create Launch Plan
Build a phased launch timeline:
- Pre-launch preparation (messaging, channels, timeline)
- Launch day activities and announcements
- Post-launch momentum (content, partnerships, communities)
- Measurement and optimization cadence
- Success criteria and go/no-go decision points

## Input Format
Use $ARGUMENTS to pass:
- Product name and description
- Target market segment
- Research data or file path
- Launch timeline and constraints
- Budget or resource limitations

## Output
A structured GTM strategy document including:
- Recommended marketing channels with justification
- Channel-specific messaging and positioning
- Launch timeline with key milestones
- KPI targets and measurement framework
- Risk mitigation strategies
- 90-day execution roadmap

## Framework
This skill applies Product Compass GTM strategy methodology, focusing on market selection, channel fit, and message-market fit for sustainable product growth.

## Tips
- Start with your most confident customer segment
- Validate assumptions through customer interviews before full launch
- Focus on a few channels excellently rather than many channels poorly
- Establish baseline metrics before launch to measure impact
- Plan for feedback loops and optimization

---

### Further Reading

- [5 GTM Principles You Should Know as a PM](https://www.productcompass.pm/p/5-gtm-principles-with-frameworks-templates)
- [OpenAI’s Product Leader Shares 3-Layer Distribution Framework To Win Mind & Market Share in the AI World](https://www.productcompass.pm/p/distribution-framework-ai-products)
- [Product-Led Growth 101, Part 1/2](https://www.productcompass.pm/p/product-led-growth-101-12)
- [How to Design a Value Proposition Customers Can't Resist?](https://www.productcompass.pm/p/how-to-design-value-proposition-template)
- [How to Achieve Product-Market Fit? Part I: Market and Value Proposition](https://www.productcompass.pm/p/how-to-achieve-the-product-market)
```

## File: `pm-go-to-market/skills/ideal-customer-profile/SKILL.md`
```markdown
---
name: ideal-customer-profile
description: "Identify the Ideal Customer Profile (ICP) from research data with demographics, behaviors, JTBD, and needs. Use when defining your ICP, analyzing PMF survey data, or understanding who your best customers are."
---
# Ideal Customer Profile

## Overview
Identify your Ideal Customer Profile (ICP) from research and survey data. This skill synthesizes customer research to define the customer most likely to find value, retain, and expand with your product.

## When to Use
- Defining ICP from product-market fit survey data
- Targeting high-value customer segments
- Analyzing customer success and expansion patterns
- Prioritizing sales and marketing efforts
- Evaluating new customer opportunities for fit
- Refining target market definition

## ICP Framework Components

### Demographics
Who are they from a firmographic and personal perspective?
- Company size (employees, revenue)
- Industry or vertical
- Geographic location
- Job title and department
- Years of experience in role
- Education and background
- Organizational structure and reporting

### Behaviors
How do they work and make decisions?
- How they discover and evaluate solutions
- Buying process and decision-making timeline
- Technical literacy and product adoption speed
- Collaboration style (solo decision vs committee)
- Change management and adoption style
- Tool switching frequency
- Community involvement and peer influence

### Jobs to Be Done (JTBD)
What are they trying to accomplish?
- Primary job/goal they're trying to achieve
- Secondary jobs that support the primary job
- Emotional jobs (how they want to feel)
- Social jobs (status and perception)
- Jobs they avoid or want to eliminate
- Frequency and importance of each job
- Success metrics for completing job

### Needs and Pain Points
What problems does your product solve?
- Specific pain points they experience
- Current workarounds and limitations
- Impact on productivity or outcomes
- Cost or time burden of the problem
- Emotional frustration levels
- Barriers to solving the problem
- Available budget to solve
- Competing priorities

## How It Works

### Step 1: Gather Customer Data
Collect research about actual and potential customers:
- Product-market fit survey responses
- Customer interview transcripts
- Trial or freemium user behavior data
- Customer feedback and support tickets
- Churn analysis and customer lifecycle data
- Win/loss analysis from sales
- Competitor customer analysis

### Step 2: Segment by Value
Identify customer cohorts and their value:
- Highest LTV (lifetime value) customers
- Fastest time-to-value customers
- Lowest churn rate customers
- Highest expansion/upsell customers
- Most enthusiastic/engaged customers
- Best reference/case study potential
- Most aligned with product vision

### Step 3: Profile Demographics
Extract firmographic patterns:
- Common company sizes (employee count, revenue)
- Industry verticals and sub-verticals
- Geographic concentrations
- Typical department and reporting structure
- Budget holders and budget available
- Company stage (startup, growth, enterprise)
- Company culture indicators

### Step 4: Identify Behaviors
Map decision-making and adoption patterns:
- How they discovered your product (channel)
- Evaluation process and timeline
- Key stakeholders in decision
- Obstacles during sales process
- Product adoption speed and breadth
- Team involvement in onboarding
- Frequency of feature usage
- Support and service needs

### Step 5: Define JTBD
Articulate what they're trying to accomplish:
- Primary job/goal (functional job)
- Emotional dimensions (how they want to feel)
- Social dimensions (team and stakeholder impact)
- Success metrics (how they measure success)
- Context and constraints (when, where, with whom)
- Competing jobs and priorities
- Importance ranking of various jobs

### Step 6: Document Pain Points and Needs
Synthesize specific problem areas:
- Before state (current situation and frustrations)
- Desired after state (ideal future state)
- Gap size and impact quantification
- Emotional dimensions of the problem
- Resource constraints preventing solutions
- Skepticism or hesitations
- Success criteria for solution

## Input Format
Use $ARGUMENTS to pass:
- Research data (surveys, interviews, transcripts)
- Customer success/metrics data
- Product usage analytics
- Sales activity and win/loss data
- Existing customer database
- Competitive intelligence

## Output
A comprehensive ICP definition including:
- Firmographic profile (company size, industry, location)
- Behavioral profile (buying patterns, adoption style)
- Complete JTBD mapping (functional, emotional, social jobs)
- Top 5-7 pain points and specific needs
- Quantified impact metrics (cost of problem, value of solution)
- Decision-making process and key stakeholders
- Typical customer journey and timeline
- Go-to-market implications and messaging
- Disqualification criteria (who is NOT a good fit)
- High-value segment within ICP (ideal-of-the-ideal)

## Framework
Based on Jobs to Be Done theory by Clayton Christensen and customer profiling methodology. Combines behavioral data with motivational insights to define actionable customer profiles.

## Tips
- Use quantitative and qualitative data together
- Interview 10+ high-value customers for pattern identification
- Look for non-obvious demographic patterns (outliers can be high-value)
- Define both ideal ICP and acceptable secondary segments
- Revisit ICP quarterly as you gather more customer data
- Use ICP to evaluate all new sales opportunities
- Share ICP across entire organization (marketing, sales, product)
- Remember: ICP should drive focus, not exclude all others

---

### Further Reading

- [5 GTM Principles You Should Know as a PM](https://www.productcompass.pm/p/5-gtm-principles-with-frameworks-templates)
- [How to Design a Value Proposition Customers Can't Resist?](https://www.productcompass.pm/p/how-to-design-value-proposition-template)
```

## File: `pm-market-research/README.md`
```markdown
# pm-market-research

Market research skills for PMs: user personas, market segmentation, sentiment analysis, and competitive analysis.

## Skills (7)

- **competitor-analysis** — Analyze competitors with strengths, weaknesses, and differentiation opportunities.
- **customer-journey-map** — Create an end-to-end customer journey map with stages, touchpoints, emotions, pain points, and opportunities.
- **market-segments** — Identify 3-5 potential customer segments with demographics, JTBD, and product fit analysis.
- **market-sizing** — Estimate market size using TAM, SAM, and SOM with top-down and bottom-up approaches.
- **sentiment-analysis** — Analyze user feedback data to identify market segments with sentiment scores, JTBD, and product satisfaction insights.
- **user-personas** — Create refined user personas from research data.
- **user-segmentation** — Segment users from feedback data based on behavior, JTBD, and needs.

## Commands (3)

- `/pm-market-research:analyze-feedback` — Analyze user feedback at scale — sentiment analysis, theme extraction, and segment-level insights.
- `/pm-market-research:competitive-analysis` — Analyze the competitive landscape — identify competitors, compare strengths and weaknesses, find differentiation opportunities.
- `/pm-market-research:research-users` — Comprehensive user research — build personas, segment users, and map the customer journey from research data.

## Author

Paweł Huryn — [The Product Compass Newsletter](https://www.productcompass.pm)

## License

MIT
```

## File: `pm-market-research/commands/analyze-feedback.md`
```markdown
---
description: Analyze user feedback at scale — sentiment analysis, theme extraction, and segment-level insights
argument-hint: "<feedback data as CSV, text, or file>"
---

# /analyze-feedback -- User Feedback Analysis

Process large volumes of user feedback (reviews, surveys, support tickets, NPS responses) into structured insights with sentiment analysis and segment-level patterns.

## Invocation

```
/analyze-feedback [upload a CSV of NPS responses]
/analyze-feedback [paste app store reviews or survey responses]
/analyze-feedback [upload support ticket export]
```

## Workflow

### Step 1: Accept Feedback Data

Accept in any format:
- CSV/Excel with feedback text (and optional metadata: date, segment, rating)
- Pasted text (reviews, survey responses, Slack messages)
- Uploaded documents or exports from feedback tools

Ask:
- What kind of feedback is this? (NPS, reviews, support tickets, survey, etc.)
- Any segments to analyze separately? (user tier, plan, geography)
- What are you looking for? (general themes, specific issues, trends over time)

### Step 2: Analyze

Apply the **sentiment-analysis** skill:

- **Sentiment scoring**: Classify each piece of feedback (positive, neutral, negative)
- **Theme extraction**: Identify recurring topics and cluster related feedback
- **Frequency analysis**: Count how often each theme appears
- **Segment analysis**: Break down sentiment and themes by user segment (if data available)
- **Trend detection**: If dates are available, identify sentiment shifts over time

### Step 3: Generate Analysis Report

```
## Feedback Analysis Report

**Date**: [today]
**Feedback analyzed**: [count] responses
**Source**: [NPS survey / app reviews / support tickets / etc.]
**Period**: [date range if available]

### Overall Sentiment
- Positive: [X%] | Neutral: [Y%] | Negative: [Z%]
- Average sentiment score: [X/10]
- Trend: [improving / stable / declining]

### Top Themes
| # | Theme | Mentions | Sentiment | Segments Most Affected |
|---|-------|----------|-----------|----------------------|

### Theme Deep-Dive

#### Theme 1: [Name] — [X] mentions, [sentiment]
- **What users are saying**: [summary with representative quotes]
- **Root cause**: [what's driving this feedback]
- **Impact**: [how this affects retention, satisfaction, or revenue]
- **Recommendation**: [what to do about it]

[Repeat for top 5-8 themes]

### Segment Analysis
| Segment | Volume | Avg Sentiment | Top Theme | Key Difference |
|---------|--------|-------------|-----------|---------------|

### Notable Quotes
> "[quote]" — [segment, sentiment]

### Trends Over Time
[If date data available: chart-ready data showing sentiment shifts]

### Actionable Insights
1. [Insight + recommended action]
2. ...

### Gaps
[What this feedback doesn't tell you — suggested follow-up research]
```

Save as markdown. If input was structured data (CSV), also save enriched data with sentiment scores as CSV.

### Step 4: Offer Next Steps

- "Want me to **create user personas** from these feedback patterns?"
- "Should I **triage the top themes as feature requests**?"
- "Want me to **design an interview script** to go deeper on a specific theme?"

## Notes

- Sentiment analysis is approximate — flag edge cases (sarcasm, mixed sentiment, non-English text)
- Theme extraction should look for needs behind requests, not just surface-level topics
- If sample sizes are small per segment, note limited confidence
- For NPS data specifically, analyze Detractors (0-6), Passives (7-8), and Promoters (9-10) separately
- Output enriched CSV when input is structured, so the user can use it in their own tools
```

## File: `pm-market-research/commands/competitive-analysis.md`
```markdown
---
description: Analyze the competitive landscape — identify competitors, compare strengths and weaknesses, find differentiation opportunities
argument-hint: "<your product or market>"
---

# /competitive-analysis -- Competitive Landscape Analysis

Research and analyze your competitive landscape. Identifies direct and indirect competitors, maps positioning, and surfaces differentiation opportunities.

## Invocation

```
/competitive-analysis AI-powered project management tools
/competitive-analysis Our product vs Notion, Asana, and Monday.com
/competitive-analysis [upload a competitor list or market brief]
```

## Workflow

### Step 1: Understand the Competitive Context

Ask:
- What is your product? What category does it compete in?
- Any specific competitors you want analyzed? Or should I identify them?
- What's the lens? (feature comparison, positioning, pricing, go-to-market)
- What will you use this analysis for? (strategy, sales enablement, investor pitch, product roadmap)

### Step 2: Identify Competitors

Apply the **competitor-analysis** skill:

- Identify 5 direct competitors (same category, same buyer)
- Identify 2-3 indirect competitors (different approach, same job-to-be-done)
- Note emerging/disruptive players if relevant
- Use web research to gather current information

### Step 3: Analyze Each Competitor

For each competitor:
- **Positioning**: How they describe themselves, target audience, key messaging
- **Strengths**: What they do well, where they win
- **Weaknesses**: Where they fall short, common complaints
- **Pricing**: Model and price points (if public)
- **Market traction**: Funding, team size, customer base signals
- **Recent moves**: New features, partnerships, pivots

### Step 4: Generate Competitive Analysis

```
## Competitive Analysis: [Your Product/Market]

**Date**: [today]
**Analyzed**: [count] competitors

### Market Overview
[2-3 sentences on market dynamics, trends, and where it's heading]

### Competitive Landscape
| Competitor | Category | Target | Positioning | Strength | Weakness |
|-----------|----------|--------|------------|----------|----------|

### Feature Comparison Matrix
| Capability | Your Product | Competitor A | Competitor B | Competitor C |
|-----------|-------------|-------------|-------------|-------------|

### Positioning Map
[2x2 matrix showing competitive positioning on key dimensions]

### Differentiation Opportunities
1. **[Opportunity]** — [why it's defensible and valuable]
2. ...

### Competitive Threats
1. **[Threat]** — [what to watch for, recommended response]
2. ...

### Recommendations
- **Double down on**: [your unique advantages]
- **Close the gap on**: [table-stakes features you're missing]
- **Ignore**: [competitor moves that aren't worth responding to]
```

Save as markdown.

### Step 5: Offer Next Steps

- "Want me to **create a battlecard** for sales against a specific competitor?"
- "Should I **develop positioning** that differentiates from the top competitors?"
- "Want me to **identify feature gaps** to close and add to the roadmap?"

## Notes

- Web research is used for current competitor data — results are as fresh as available sources
- Distinguish between "table stakes" (must-have to compete) and "differentiators" (must-have to win)
- Don't just list features — analyze *why* competitors make the choices they make
- Pricing intelligence should note whether pricing is public, usage-based, or requires sales contact
- Update this analysis quarterly — competitive landscapes shift fast
```

## File: `pm-market-research/commands/research-users.md`
```markdown
---
description: Comprehensive user research — build personas, segment users, and map the customer journey from research data
argument-hint: "<research data, survey results, or product description>"
---

# /research-users -- User Research Synthesis

Turn raw research data into actionable user personas, behavioral segments, and customer journey maps. Accepts survey data, interview notes, feedback, analytics, or a product description for exploratory research.

## Invocation

```
/research-users [upload survey results, interview notes, or feedback data]
/research-users B2B project management tool for agencies — help me understand our users
/research-users [paste user feedback or support ticket data]
```

## Workflow

### Step 1: Accept Research Inputs

Accept from any combination:
- Survey responses (CSV, spreadsheet, pasted)
- Interview notes or transcripts
- Support tickets or feature requests
- Product analytics / behavioral data
- NPS or satisfaction data
- Product description (for exploratory research without data)

Ask:
- What research do you have? What format?
- What do you want to understand? (who are our users, how do they differ, where's the friction)
- What decisions will this inform? (roadmap, positioning, pricing, onboarding)

### Step 2: Build Personas

Apply the **user-personas** skill:

- Identify 3-4 distinct personas from the data
- For each persona: name, role, goals (JTBD), pains, gains, behavioral patterns
- Include unexpected insights — things that surprised you in the data
- Note persona prevalence (what % of your base each represents, if data allows)

### Step 3: Segment Users

Apply the **user-segmentation** and **market-segments** skills:

- Create behavioral segments (not just demographics)
- For each segment: size, JTBD, product fit, willingness to pay, engagement level
- Identify the highest-value segment and the highest-growth segment
- Map segments to personas (how they overlap)

### Step 4: Map the Customer Journey

Apply the **customer-journey-map** skill:

- Map the end-to-end journey: Awareness → Consideration → Onboarding → Active Use → Expansion → Advocacy
- For each stage: touchpoints, emotions, pain points, aha moments
- Identify the biggest drop-off points
- Highlight moments of delight worth amplifying

### Step 5: Generate Research Report

```
## User Research Report: [Product]

**Date**: [today]
**Data sources**: [what was analyzed]
**Sample size**: [if applicable]

### Executive Summary
[3-5 sentences: key findings and implications]

### Personas

#### Persona 1: [Name] — "[Quote that captures them]"
- **Who**: [role, context, experience level]
- **Primary JTBD**: [When..., I want to..., so I can...]
- **Key pains**: [top 3]
- **Key gains**: [what delights them]
- **Behavioral pattern**: [how they use the product]
- **Prevalence**: [X% of user base]

[Repeat for each persona]

### User Segments
| Segment | Size | Primary JTBD | Product Fit | Value | Growth |
|---------|------|-------------|-------------|-------|--------|

### Customer Journey Map
| Stage | Touchpoints | Emotion | Pain Points | Opportunities |
|-------|------------|---------|-------------|---------------|

### Key Insights
1. [Insight with supporting evidence]
2. ...

### Recommendations
1. [Actionable recommendation tied to findings]
2. ...

### Open Questions
[What the data didn't answer — suggested follow-up research]
```

Save as markdown.

### Step 6: Offer Next Steps

- "Want me to **create interview scripts** to go deeper on a specific persona?"
- "Should I **analyze sentiment** across these segments?"
- "Want me to **build a value proposition** for the top persona?"
- "Should I **prioritize the journey map pain points** as feature opportunities?"

## Notes

- If data is thin, be transparent about confidence levels — 5 interviews → hypotheses, not conclusions
- Personas should be useful, not decorative — every persona should influence a product decision
- Behavioral segments are more actionable than demographic segments for product decisions
- The journey map should surface emotions, not just actions — where users feel frustrated vs. delighted drives prioritization
- If no data is provided, generate research-informed hypotheses and recommend how to validate them
```

## File: `pm-market-research/skills/competitor-analysis/SKILL.md`
```markdown
---
name: competitor-analysis
description: "Analyze competitors with strengths, weaknesses, and differentiation opportunities. Identifies direct competitors and maps the competitive landscape. Use when doing competitive research, preparing a competitive brief, or finding differentiation opportunities."
---

# Competitor Analysis

## Purpose
Conduct a comprehensive competitive analysis to understand the landscape, identify 5 direct competitors, and uncover differentiation opportunities. This skill maps competitive positioning, synthesizes competitor strengths and weaknesses, and highlights opportunities for strategic differentiation.

## Instructions

You are a strategic product analyst and competitive intelligence expert specializing in competitive positioning and market landscape mapping.

### Input
Your task is to analyze the competitive landscape for **$ARGUMENTS** in the **[market/industry segment]** (if specified).

Conduct web research to identify direct competitors. If the user provides market research, competitor data, pricing sheets, feature comparisons, or customer feedback about competitors, read and analyze them directly. Synthesize data into a comprehensive competitive view.

### Analysis Steps (Think Step by Step)

1. **Market Scoping**: Define the market, industry, and addressable customer base for $ARGUMENTS
2. **Competitor Identification**: Use web search to identify 5 primary direct competitors
3. **Competitive Intelligence**: Research each competitor's positioning, features, pricing, go-to-market strategy
4. **Strengths & Weaknesses**: Assess competitor capabilities, limitations, and market positioning
5. **Differentiation Mapping**: Identify gaps, overlaps, and opportunities for $ARGUMENTS to differentiate
6. **Strategic Synthesis**: Develop insights about competitive dynamics and future threats

### Output Structure

**Market Overview & Definition**
- Market size and growth trends
- Primary customer segments and use cases
- Key success factors in this market
- Market dynamics and competitive intensity

**Competitive Set Summary**
- 5 primary direct competitors identified
- Market positions: leaders, challengers, niche players
- Estimated market share or positioning
- Notable adjacent or indirect competitors

For each of the 5 competitors:

**Competitor Profile**
- Company name, founding date, funding/status
- Primary market focus and customer segments served
- Estimated market share or customer base size
- Market positioning and go-to-market strategy

**Core Product Strengths**
- Key features and capabilities
- Unique competitive advantages
- Customer value proposition
- Technology differentiation or moats
- Customer satisfaction and retention signals

**Product Weaknesses & Gaps**
- Missing features or use cases
- Known limitations or pain points for customers
- Technical or operational weaknesses
- Market positioning gaps
- Customer dissatisfaction areas

**Business Model & Pricing**
- Pricing structure (per-seat, per-usage, flat-fee, freemium, etc.)
- Price point(s) in market
- Go-to-market channels and sales motion
- Revenue model and growth stage

**Competitive Threats & Advantages**
- How this competitor threatens $ARGUMENTS
- Existing customer base and switching costs
- Strategic partnerships or ecosystems
- Recent product updates or strategic moves

**Differentiation Opportunities for $ARGUMENTS**

- Unmet customer needs across competitive set
- Feature/pricing/UX opportunities to stand out
- Target segments underserved by competitors
- Jobs-to-be-done not effectively solved by competitors
- Channel or go-to-market approaches not yet deployed
- Potential partnerships or integrations competitors lack

**Competitive Positioning Recommendation**
- Recommended competitive positioning for $ARGUMENTS
- Key differentiators to emphasize
- Segments or use cases to target or avoid
- Competitive threats to monitor
- 12-18 month competitive risks and opportunities

## Best Practices

- Research current competitor websites, pricing pages, and customer reviews
- Use web search to identify product launches, funding, executive moves
- Distinguish between direct competitors and adjacent alternatives
- Validate competitive insights across multiple sources
- Identify both obvious and subtle differentiation opportunities
- Consider customer pain points not yet addressed in market
- Look for emerging competitors or new market entrants
- Flag competitors gaining traction or gaining market share
- Consider long-term competitive dynamics and market shifts

---

### Further Reading

- [Market Research: Advanced Techniques](https://www.productcompass.pm/p/market-research-advanced-techniques)
- [User Interviews: The Ultimate Guide to Research Interviews](https://www.productcompass.pm/p/interviewing-customers-the-ultimate)
```

## File: `pm-market-research/skills/customer-journey-map/SKILL.md`
```markdown
---
name: customer-journey-map
description: "Create an end-to-end customer journey map with stages, touchpoints, emotions, pain points, and opportunities. Use when mapping the customer experience, identifying friction points, improving onboarding, or visualizing the user journey."
---

## Customer Journey Map

Map the end-to-end customer experience from awareness through advocacy, identifying emotions, pain points, and improvement opportunities at each stage.

### Context

You are creating a customer journey map for **$ARGUMENTS**.

If the user provides files (interview transcripts, survey data, analytics, support tickets, or existing journey maps), read them first. Use web search to understand the product if a URL is provided.

### Instructions

1. **Define the persona**: Who is traveling this journey? Use a specific persona with JTBD, not a generic user.

2. **Map the journey stages** (adapt to the product):

   | Stage | Description |
   |---|---|
   | **Awareness** | How do they first learn about the product? |
   | **Consideration** | What do they evaluate? What alternatives do they compare? |
   | **Acquisition** | How do they sign up or purchase? |
   | **Onboarding** | First experience with the product — time to value |
   | **Engagement** | Regular usage — building habits |
   | **Retention** | What keeps them coming back? What might cause churn? |
   | **Advocacy** | When and why do they recommend the product to others? |

3. **For each stage, document**:

   - **Touchpoints**: Where the user interacts with the product, brand, or team (website, email, in-app, support, social media)
   - **User actions**: What they do at this stage
   - **Thoughts & questions**: What's on their mind ("Is this worth my time?" "How do I...?")
   - **Emotions**: How they feel (excited, confused, frustrated, delighted) — rate on a scale or use emoji indicators
   - **Pain points**: Friction, confusion, drop-off risks
   - **Opportunities**: How to improve the experience at this point

4. **Identify critical moments**:
   - **Aha moment**: When the user first experiences core value
   - **Moments of truth**: Decision points where they commit or abandon
   - **Churn triggers**: Where users most commonly drop off

5. **Create the journey map table**:

   | Stage | Touchpoint | User Action | Emotion | Pain Point | Opportunity |
   |---|---|---|---|---|---|

6. **Recommend prioritized improvements**:
   - Which pain points have the highest impact on conversion or retention?
   - What quick wins can improve the experience immediately?
   - What requires deeper investment but has the biggest payoff?

Think step by step. Save as a markdown document. For visual journey maps, suggest the user create one in Miro or FigJam using this analysis as the foundation.

---

### Further Reading

- [User Journey Mapping 101](https://www.productcompass.pm/p/user-journey-mapping-101)
- [Funnel Analysis 101: How to Track and Optimize Your User Journey](https://www.productcompass.pm/p/funnel-analysis)
- [Market Research: Advanced Techniques](https://www.productcompass.pm/p/market-research-advanced-techniques)
- [User Interviews: The Ultimate Guide to Research Interviews](https://www.productcompass.pm/p/interviewing-customers-the-ultimate)
```

## File: `pm-market-research/skills/market-segments/SKILL.md`
```markdown
---
name: market-segments
description: "Identify 3-5 potential customer segments with demographics, JTBD, and product fit analysis. Use when exploring market segments, identifying target audiences, evaluating new markets, or learning how to segment a market."
---

# Market Segments

## Purpose
Identify and analyze 3-5 distinct customer segments for your product, understanding their unique jobs-to-be-done, desired outcomes, pain points, and product fit. Use this skill to evaluate market opportunities, prioritize target audiences, or expand into new market segments.

## Instructions

You are a strategic market research expert skilled in market segmentation, customer profiling, and total addressable market (TAM) analysis.

### Input
Your task is to identify and analyze potential customer segments for **$ARGUMENTS**.

If research data, market studies, customer databases, or existing segmentation documents are provided, read and analyze them directly. Look for behavioral patterns, demographic clusters, and distinct needs across segments.

### Analysis Steps (Think Step by Step)

1. **Market Exploration**: Consider the full addressable market for $ARGUMENTS
2. **Segmentation Criteria**: Identify logical segmentation dimensions (behavioral, demographic, firmographic, needs-based)
3. **Segment Definition**: Create 3-5 distinct, non-overlapping customer segments
4. **Characterization**: For each segment, synthesize profiles and validate distinctness
5. **Opportunity Assessment**: Evaluate market size, growth potential, and competitive intensity per segment

### Output Structure

For each of the 3-5 segments, provide:

**Segment Name & Overview**
- Clear, memorable segment identifier
- Size estimate (% of total market or absolute numbers if data available)
- Growth trajectory and market dynamics

**Key Demographics & Firmographics**
- Core characteristics (age, role, company size, industry, geography, etc.)
- Decision-maker profiles if B2B

**Jobs-to-be-Done**
- Primary job and desired outcome for this segment
- Frequency, context, and stakes of the job
- Success criteria and desired outcomes

**Key Pain Points & Obstacles**
- Barriers to job completion specific to this segment
- Consequences of not solving the problem

**Desired Gains & Success Factors**
- What outcomes matter most to this segment
- Preferred solution characteristics
- Cost and time constraints

**Product Fit Analysis**
- How well $ARGUMENTS serves this segment's needs
- Unique value proposition for this segment
- Potential adoption barriers or resistance

**Competitive Landscape**
- Existing solutions or workarounds this segment uses
- Alternative approaches or competitors

## Best Practices

- Ensure segments are measurable, accessible, and distinct
- Prioritize segments with clear jobs-to-be-done and pain points
- Validate segment assumptions with available data
- Consider both greenfield opportunities and underserved segments
- Flag segments requiring additional market research

---

### Further Reading

- [Market Research: Advanced Techniques](https://www.productcompass.pm/p/market-research-advanced-techniques)
- [User Interviews: The Ultimate Guide to Research Interviews](https://www.productcompass.pm/p/interviewing-customers-the-ultimate)
- [Crossing the Chasm: The Ultimate Guide For PMs](https://www.productcompass.pm/p/crossing-the-chasm)
- [How to Achieve Product-Market Fit? Part I: Market and Value Proposition](https://www.productcompass.pm/p/how-to-achieve-the-product-market)
- [Product Innovation Masterclass](https://www.productcompass.pm/p/product-innovation-masterclass) (video course)
```

## File: `pm-market-research/skills/market-sizing/SKILL.md`
```markdown
---
name: market-sizing
description: "Estimate market size using TAM, SAM, and SOM with top-down and bottom-up approaches. Use when sizing a market opportunity, estimating addressable market, preparing for investor pitches, or evaluating market entry."
---

# Estimate Market Size (TAM, SAM, SOM)

## Purpose
Estimate the Total Addressable Market (TAM), Serviceable Addressable Market (SAM), and Serviceable Obtainable Market (SOM) for a product. Includes both top-down and bottom-up estimation approaches, growth projections, and key assumptions to validate.

## Instructions

You are a strategic market analyst specializing in market sizing, opportunity assessment, and growth forecasting.

### Input
Your task is to estimate the market size for **$ARGUMENTS** within the specified market constraints (geography, industry vertical, customer type, etc.).

If the user provides market research, industry reports, financial data, or competitor information, read and analyze them directly. Use web search to find current market data, industry reports, and growth projections.

### Analysis Steps (Think Step by Step)

1. **Market Definition**: Define the market boundaries — what problem space, which customer segments, what geography or constraints apply
2. **Top-Down Estimation**: Start from total industry size and narrow to the relevant slice
3. **Bottom-Up Estimation**: Build from unit economics (customers × price × frequency) to cross-validate
4. **SAM Scoping**: Identify which portion of TAM is realistically serviceable given product capabilities, channels, and constraints
5. **SOM Estimation**: Estimate achievable share in the next 1-3 years based on competitive position and go-to-market capacity
6. **Growth Projection**: Forecast how TAM, SAM, and SOM may evolve over the next 2-3 years
7. **Assumption Mapping**: Surface the key assumptions underlying each estimate

### Output Structure

**Market Definition**
- Problem space and customer need
- Geographic and segment boundaries
- Key constraints or scoping decisions

**TAM (Total Addressable Market)**
- Top-down estimate with sources and reasoning
- Bottom-up estimate for cross-validation
- Reconciliation of the two approaches
- Current TAM value (annual revenue opportunity)

**SAM (Serviceable Addressable Market)**
- Which portion of TAM the product can realistically serve
- Constraints: geography, language, channels, product capabilities, pricing tier
- SAM as percentage of TAM with reasoning

**SOM (Serviceable Obtainable Market)**
- Realistic share achievable in 1-3 years
- Basis: competitive position, go-to-market capacity, current traction
- SOM as percentage of SAM with reasoning

**Market Summary Table**

| Metric | Current Estimate | 2-3 Year Projection |
|--------|-----------------|---------------------|
| TAM    |                 |                     |
| SAM    |                 |                     |
| SOM    |                 |                     |

**Growth Drivers & Trends**
- Key factors that could expand or contract the market
- Technology, regulatory, demographic, or behavioral shifts
- Emerging segments or adjacent markets

**Key Assumptions & Risks**
- Critical assumptions behind each estimate (numbered)
- Confidence level for each (high / medium / low)
- How to validate the most uncertain assumptions
- What would materially change the estimates

## Best Practices

- Always provide both top-down and bottom-up estimates to triangulate
- Use web search for current industry data, analyst reports, and market benchmarks
- Cite sources for market data — avoid unsupported numbers
- Be explicit about assumptions; label estimates vs. data
- Distinguish between value-based (revenue) and volume-based (users/units) sizing
- Consider currency and purchasing power parity for international markets
- Flag where estimates have wide confidence intervals
- Recommend specific data sources or research to sharpen estimates

---

### Further Reading

- [Market Research: Advanced Techniques](https://www.productcompass.pm/p/market-research-advanced-techniques)
- [User Interviews: The Ultimate Guide to Research Interviews](https://www.productcompass.pm/p/interviewing-customers-the-ultimate)
- [Crossing the Chasm: The Ultimate Guide For PMs](https://www.productcompass.pm/p/crossing-the-chasm)
- [Product Innovation Masterclass](https://www.productcompass.pm/p/product-innovation-masterclass) (video course)
```

## File: `pm-market-research/skills/sentiment-analysis/SKILL.md`
```markdown
---
name: sentiment-analysis
description: "Analyze user feedback data to identify segments with sentiment scores, JTBD, and product satisfaction insights. Use when analyzing user feedback at scale, running sentiment analysis on reviews or surveys, or identifying satisfaction patterns."
---

# Sentiment Analysis

## Purpose
Analyze large-scale user feedback data to identify market segments, measure satisfaction, and uncover product improvement opportunities. This skill synthesizes feedback into actionable insights organized by user segment, sentiment, and impact.

## Instructions

You are an expert user researcher and feedback analyst specializing in qualitative data synthesis and sentiment analysis at scale.

### Input
Your task is to analyze user feedback data for **$ARGUMENTS** and identify market segments with associated sentiment insights.

If the user provides CSV files, PDFs, survey responses, review data, social listening reports, or other feedback sources, read and analyze them directly. Extract patterns, themes, and sentiment signals from the data.

### Analysis Steps (Think Step by Step)

1. **Data Ingestion**: Read all feedback sources and create a working inventory
2. **Segment Identification**: Identify at least 3 distinct user segments or personas from the feedback
3. **Thematic Analysis**: Extract recurring themes, pain points, and positive feedback per segment
4. **Sentiment Scoring**: Assign sentiment scores (-1 to +1) for overall satisfaction per segment
5. **Impact Assessment**: Prioritize insights by frequency, severity, and business impact
6. **Synthesis**: Create segment profiles with consolidated insights

### Output Structure

For each identified segment:

**Segment Profile**
- Name/identifier and common characteristics
- User count or proportion in feedback dataset
- Primary use case or context

**Jobs-to-be-Done**
- Core job this segment is trying to accomplish
- Associated desired outcomes

**Sentiment Score & Satisfaction Level**
- Overall sentiment score (-1 to +1)
- Key satisfaction drivers and detractors
- Net Promoter Score (NPS) proxy if applicable

**Top Positive Feedback Themes**
- What this segment loves about $ARGUMENTS
- Key strengths from user perspective
- Examples of successful use cases

**Top Pain Points & Criticism**
- Most frequent complaints or frustrations
- Unmet needs or missing features
- Friction points in user journey
- Direct quotes from feedback when available

**Product-Segment Fit Assessment**
- How well $ARGUMENTS serves this segment's needs
- Potential to improve fit through product changes
- Risk of churn or dissatisfaction

**Actionable Recommendations**
- 2-3 highest-impact improvements per segment
- Quick wins vs. strategic initiatives
- Segments to prioritize or de-prioritize

## Best Practices

- Ground all findings in actual user feedback; cite sources
- Identify both majority and minority perspectives within segments
- Distinguish between feature requests and fundamental pain points
- Consider context and constraints users face
- Flag segments with small sample sizes or uncertain sentiment
- Look for cross-segment patterns and universal pain points
- Provide balanced view of product strengths and weaknesses

---

### Further Reading

- [Market Research: Advanced Techniques](https://www.productcompass.pm/p/market-research-advanced-techniques)
- [User Interviews: The Ultimate Guide to Research Interviews](https://www.productcompass.pm/p/interviewing-customers-the-ultimate)
```

## File: `pm-market-research/skills/user-personas/SKILL.md`
```markdown
---
name: user-personas
description: "Create refined user personas from research data — 3 personas with JTBD, pains, gains, and unexpected insights. Use when building personas from survey data, creating user profiles from research, or segmenting users for product decisions."
---

# User Personas

## Purpose
Create detailed, actionable user personas from research data that capture the true diversity of your user base. This skill generates research-backed personas with jobs-to-be-done, pain points, desired outcomes, and unexpected behavioral insights to guide product decisions.

## Instructions

You are an experienced product researcher specializing in persona development and user research synthesis.

### Input
Your task is to create 3 refined user personas for **$ARGUMENTS**.

If the user provides CSV, Excel, survey responses, interview transcripts, or other research data files, read and analyze them directly using available tools. Extract key patterns, demographics, motivations, and behaviors.

### Analysis Steps (Think Step by Step)

1. **Data Collection**: Read and review all provided research data and documents
2. **Pattern Recognition**: Identify recurring characteristics, goals, pain points, and behaviors across users
3. **Segmentation**: Group similar users into distinct personas based on shared motivations and jobs-to-be-done
4. **Enrichment**: For each persona, synthesize data into a coherent profile
5. **Validation**: Cross-reference insights to ensure personas are grounded in actual research findings

### Output Structure

For each of the 3 personas, provide:

**Persona Name & Demographics**
- Age range, role/title, company size (if B2B), key characteristics

**Primary Job-to-be-Done**
- The core outcome the persona is trying to achieve
- Context and frequency of the job

**Top 3 Pain Points**
- Specific challenges or obstacles preventing job completion
- Impact and severity of each pain

**Top 3 Desired Gains**
- Benefits, outcomes, or solutions the persona seeks
- How they measure success

**One Unexpected Insight**
- A counterintuitive behavioral pattern or motivation derived from the data
- Why this matters for product decisions

**Product Fit Assessment**
- How $ARGUMENTS addresses (or could address) this persona's needs
- Potential friction points or unmet needs

## Best Practices

- Ground all insights in actual data; avoid assumptions
- Use direct quotes from research when available
- Identify behavioral patterns, not just demographic categories
- Make personas distinct and non-overlapping where possible
- Flag any data gaps or areas requiring additional research

---

### Further Reading

- [User Interviews: The Ultimate Guide to Research Interviews](https://www.productcompass.pm/p/interviewing-customers-the-ultimate)
- [Market Research: Advanced Techniques](https://www.productcompass.pm/p/market-research-advanced-techniques)
- [Jobs-to-be-Done Masterclass with Tony Ulwick and Sabeen Sattar](https://www.productcompass.pm/p/jobs-to-be-done-masterclass-with) (video course)
```

## File: `pm-market-research/skills/user-segmentation/SKILL.md`
```markdown
---
name: user-segmentation
description: "Segment users from feedback data based on behavior, JTBD, and needs. Identifies at least 3 distinct user segments. Use when segmenting a user base, analyzing diverse user feedback, or building a segmentation model."
---

# User Segmentation

## Purpose
Analyze diverse user feedback to identify at least 3 distinct behavioral and needs-based user segments. This skill surfaces hidden customer groups based on jobs-to-be-done, behaviors, and motivations rather than demographics alone, enabling targeted product strategy.

## Instructions

You are an expert behavioral researcher and data analyst specializing in user segmentation and behavioral clustering.

### Input
Your task is to segment users for **$ARGUMENTS** based on behavior, jobs-to-be-done, and unmet needs.

If the user provides feedback data, interviews, support tickets, product usage logs, surveys, or other user data, read and analyze them directly. Extract behavioral patterns, motivations, and needs across the user base.

### Analysis Steps (Think Step by Step)

1. **Data Preparation**: Read and organize all provided user feedback and data
2. **Behavior Extraction**: Identify key behavioral patterns, usage modes, and user journeys
3. **Needs Analysis**: Map jobs-to-be-done, desired outcomes, and pain points for each user
4. **Clustering**: Group users into distinct segments based on behavior and needs similarity
5. **Validation**: Ensure segments are coherent, non-overlapping, and actionable
6. **Characterization**: Develop rich profiles for each segment with representative quotes

### Output Structure

For each identified segment (minimum 3):

**Segment Name & Overview**
- Clear, descriptive segment identifier
- Size: estimated number or percentage of user base
- Brief one-sentence characterization

**Behavioral Characteristics**
- How this segment uses $ARGUMENTS (primary use cases, frequency, depth)
- Typical user journey and key touchpoints
- Technical proficiency or sophistication level
- Integration with other tools or workflows

**Jobs-to-be-Done & Motivations**
- Core job(s) this segment is trying to accomplish
- Underlying motivations and desired outcomes
- Context and frequency of the job
- What success looks like for this segment

**Key Needs & Pain Points**
- Unmet needs specific to this segment's behavior
- Obstacles preventing effective job completion
- Current workarounds or alternative solutions they employ
- Severity and frequency of pain points

**Current Product Fit**
- How well $ARGUMENTS currently serves this segment
- Features or capabilities this segment values most
- Gaps or limitations most frustrating to this segment
- Likelihood to continue using vs. churn risk

**Differentiated Value Proposition**
- What unique value could be unlocked for this segment
- Feature or experience improvements that would maximize fit
- Messaging and positioning most resonant with this segment

**Segment Prioritization**
- Strategic importance: growth potential, revenue impact, alignment with vision
- Implementation difficulty: ease of serving this segment's needs
- Recommendation: invest, maintain, or de-prioritize

## Best Practices

- Ground segmentation in behavioral and motivational data, not just demographics
- Use representative quotes and examples from actual user feedback
- Ensure segments are distinct and serve different core needs
- Consider interdependencies between segments and prioritization tradeoffs
- Flag any segments that may be underrepresented in feedback data
- Validate emerging segments against product usage or customer data when available
- Consider adjacent behaviors and cross-segment patterns

---

### Further Reading

- [Market Research: Advanced Techniques](https://www.productcompass.pm/p/market-research-advanced-techniques)
- [User Interviews: The Ultimate Guide to Research Interviews](https://www.productcompass.pm/p/interviewing-customers-the-ultimate)
- [Jobs-to-be-Done Masterclass with Tony Ulwick and Sabeen Sattar](https://www.productcompass.pm/p/jobs-to-be-done-masterclass-with) (video course)
```

## File: `pm-marketing-growth/README.md`
```markdown
# pm-marketing-growth

Product marketing and growth skills: marketing ideas, value proposition statements, North Star metrics, product naming, and positioning.

## Skills (5)

- **marketing-ideas** — Generate 5 creative, cost-effective marketing ideas with channels, messaging, and engagement rationale.
- **north-star-metric** — Identify a North Star Metric and 3-5 Input Metrics.
- **positioning-ideas** — Brainstorm product positioning ideas differentiated from competitors.
- **product-name** — Brainstorm 5 unique, memorable product names with rationale aligned to brand values and target audience.
- **value-prop-statements** — Generate value proposition statements for marketing, sales, and onboarding from existing value propositions.

## Commands (2)

- `/pm-marketing-growth:market-product` — Brainstorm marketing ideas, positioning, value prop statements, and product names — creative marketing toolkit.
- `/pm-marketing-growth:north-star` — Define your North Star Metric and supporting input metrics — classify the business game and validate against best practices.

## Author

Paweł Huryn — [The Product Compass Newsletter](https://www.productcompass.pm)

## License

MIT
```

## File: `pm-marketing-growth/commands/market-product.md`
```markdown
---
description: Brainstorm marketing ideas, positioning, value prop statements, and product names — creative marketing toolkit
argument-hint: "<product or marketing challenge>"
---

# /market-product -- Marketing Creative Toolkit

Generate creative marketing assets: campaign ideas, positioning statements, value prop copy, and product naming options. All in one workflow or pick specific modules.

## Invocation

```
/market-product AI scheduling tool for remote teams — need launch marketing
/market-product Help me position our analytics product against enterprise competitors
/market-product We need a name for our new developer productivity feature
```

## Workflow

### Step 1: Understand the Marketing Need

Ask:
- What is the product? Target audience?
- What do you need? (full marketing toolkit, or specific: ideas, positioning, naming, copy)
- What's the context? (launch, rebrand, campaign, competitive repositioning)
- Any existing brand guidelines or tone of voice?

### Step 2: Generate Based on Need

**Marketing Ideas** — apply **marketing-ideas** skill:
- 5 creative, cost-effective campaign ideas
- Each with: channel, messaging angle, engagement rationale, estimated effort
- Mix of quick wins and bigger bets

**Positioning** — apply **positioning-ideas** skill:
- Identify top 5 competitors for positioning context
- Generate 3-5 positioning statements differentiated from each
- Include rationale for each positioning angle

**Value Proposition Statements** — apply **value-prop-statements** skill:
- Generate copy for marketing, sales, and onboarding contexts
- Segment-specific variations
- Short (tagline), medium (elevator pitch), and long (landing page) versions

**Product Naming** — apply **product-name** skill:
- Brainstorm 5 unique, memorable names
- Each with: rationale, brand alignment, domain availability notes
- Check for unintended meanings or conflicts

### Step 3: Generate Output

```
## Marketing Toolkit: [Product]

**Date**: [today]
**Context**: [launch / rebrand / campaign / etc.]

### Marketing Campaign Ideas
| # | Idea | Channel | Effort | Expected Impact |
|---|------|---------|--------|----------------|

### Positioning Options
| # | Positioning | vs Competitor | Strength | Risk |
|---|-----------|--------------|----------|------|

**Recommended positioning**: [which and why]

### Value Prop Copy
**Tagline**: [one line]
**Elevator pitch**: [2-3 sentences]
**Landing page hero**: [headline + subheading]
**Sales one-liner**: [for sales conversations]

### Product Name Options (if requested)
| # | Name | Rationale | Domain | Risk |
|---|------|----------|--------|------|

### Messaging Matrix
| Audience | Key Message | Proof Point | CTA |
|----------|-----------|------------|-----|
```

Save as markdown.

### Step 4: Offer Next Steps

- "Want me to **draft full marketing content** (blog post, email, social)?"
- "Should I **define the North Star metric** for this campaign?"
- "Want me to **create a competitive battlecard** to support positioning?"
- "Should I **plan the full launch**?"

## Notes

- Positioning should be tested, not assumed — recommend A/B testing headlines
- Value prop copy should use the customer's language, not internal jargon
- Marketing ideas should be specific and actionable, not generic ("use social media")
- Product names should be checked for trademark conflicts before committing
- Always tie marketing back to customer JTBD, not product features
```

## File: `pm-marketing-growth/commands/north-star.md`
```markdown
---
description: Define your North Star Metric and supporting input metrics — classify the business game and validate against best practices
argument-hint: "<product or business>"
---

# /north-star -- North Star Metric Definition

Identify the single metric that best captures the value your product delivers, plus the input metrics that drive it. Classifies your business game and validates against proven criteria.

## Invocation

```
/north-star B2B SaaS for team collaboration
/north-star Consumer fitness app monetized through subscriptions
/north-star Help me fix our North Star — we're tracking DAU but it doesn't feel right
```

## Workflow

### Step 1: Understand the Product

Ask:
- What is the product? What value does it deliver to users?
- What's the business model? (subscription, transaction, advertising, marketplace)
- Current metrics being tracked (if any)
- Why is this needed now? (new product, existing metric feels wrong, team alignment)

### Step 2: Classify the Business Game

Apply the **north-star-metric** skill:

Identify which game the product is playing:
- **Attention**: Revenue from user time/engagement (media, social, ad-supported)
- **Transaction**: Revenue from purchases (e-commerce, marketplace)
- **Productivity**: Revenue from efficiency gains (SaaS, tools, B2B)

The game determines what kind of North Star makes sense.

### Step 3: Define the North Star

- Propose 2-3 North Star candidates
- Validate each against 7 criteria:
  1. Expresses value delivered to customers
  2. Is a leading indicator of revenue
  3. Is measurable and trackable
  4. Is understandable by the whole team
  5. Is actionable (teams can influence it)
  6. Is not a vanity metric
  7. Is not gameable without delivering real value
- Recommend the strongest candidate with rationale

### Step 4: Define Input Metrics

For the selected North Star, identify 3-5 input metrics:
- Each input metric should be a lever that directly drives the North Star
- Each should be ownable by a specific team
- Together, inputs should be MECE in explaining North Star movement

### Step 5: Generate Metrics Framework

```
## North Star Framework: [Product]

**Business Game**: [Attention / Transaction / Productivity]

### North Star Metric
**Metric**: [precise name]
**Definition**: [formula or measurement method]
**Why this metric**: [explains value, leads revenue, is actionable]
**Current value**: [if known]
**Target**: [goal]

### Validation
| Criterion | Pass? | Notes |
|----------|-------|-------|
| Expresses value | [Y/N] | [explanation] |
| Leading indicator | [Y/N] | [explanation] |
| Measurable | [Y/N] | [explanation] |
| Understandable | [Y/N] | [explanation] |
| Actionable | [Y/N] | [explanation] |
| Not vanity | [Y/N] | [explanation] |
| Not gameable | [Y/N] | [explanation] |

### Input Metrics
| Input Metric | Drives North Star By | Owner | Current | Target |
|-------------|---------------------|-------|---------|--------|

### Metrics Constellation
[Visual tree showing North Star → Input Metrics → Team Actions]

### Counter-Metrics
| Metric | Protects Against |
|--------|-----------------|

### Anti-Patterns Avoided
[Why we didn't choose DAU, revenue, or other common but flawed metrics]
```

Save as markdown.

### Step 6: Offer Next Steps

- "Want me to **build a full metrics dashboard** around this?"
- "Should I **create OKRs** based on these metrics?"
- "Want me to **write SQL queries** to compute these metrics?"

## Notes

- The North Star should measure *value delivered*, not just *activity* — "daily active users" is only good if active use = value delivery
- Revenue is never a good North Star — it's a lagging indicator that doesn't capture user value
- Input metrics are what make the framework actionable — without them, the North Star is just a vanity dashboard
- Revisit the North Star annually or when the business model changes significantly
- Counter-metrics prevent Goodhart's Law — when a metric becomes a target, it ceases to be a good metric
```

## File: `pm-marketing-growth/skills/marketing-ideas/SKILL.md`
```markdown
---
name: marketing-ideas
description: "Generate 5 creative, cost-effective marketing ideas with channels, messaging, and engagement rationale. Use when brainstorming marketing campaigns, planning product promotion, or looking for creative marketing tactics."
---
# Marketing Ideas

Generate 5 creative, cost-effective marketing ideas with channels, messaging, and engagement rationale. Use when brainstorming marketing campaigns, planning product promotion, or exploring creative marketing approaches.

## When to Use

- Brainstorming marketing campaigns
- Planning product promotion strategies
- Exploring creative marketing approaches
- Building growth initiatives
- Triggers: marketing ideas, promote product, marketing campaign, creative marketing, growth ideas

## Prompt

You are an experienced product marketer specializing in cost-effective growth strategies and creative campaign development.

Analyze the following product and market context: $ARGUMENTS

Generate 5 creative marketing ideas for promoting this product to the target market segment. For each idea:

1. **Channel**: Identify the primary marketing channel (social media, content, partnerships, community, email, etc.)
2. **Core Message**: Craft a compelling message that resonates with the audience
3. **Why It Works**: Provide a brief explanation of why this approach is likely to engage the target audience
4. **Cost Efficiency**: Highlight what makes this strategy cost-effective or resource-efficient

Prioritize strategies that deliver high impact with limited budget. Consider unconventional approaches and leverage emerging trends where applicable.

## Tips for Best Results

- Provide specific details about your product, target market, and business constraints
- Include any existing brand positioning or messaging guidelines
- Mention your current marketing channels and what's already working
- Share any budget limitations or resource constraints
- Include information about your target audience's preferences and behaviors

---

### Further Reading

- [Product Management vs. Product Marketing vs. Product Growth 101](https://www.productcompass.pm/p/product-management-vs-product-marketing)
```

## File: `pm-marketing-growth/skills/north-star-metric/SKILL.md`
```markdown
---
name: north-star-metric
description: "Define a North Star Metric and 3-5 supporting input metrics that form a metrics constellation. Classify the business game (Attention, Transaction, Productivity) and validate against 7 criteria for an effective North Star. Use when choosing a North Star Metric, setting up a metrics framework, learning about the North Star Framework, or deciding what to measure."
---
# North Star Metric

Identify a North Star Metric and 3-5 Input Metrics that form a metrics constellation. Classifies the business game being played and validates against criteria for an effective North Star. Use when defining key metrics, setting up a metrics framework, or choosing what to measure.

## Domain Context

NSM is **NOT**: multiple metrics, a revenue/LTV metric (must be customer-centric), an OKR (that's a goal-setting technique), or a strategy (but choosing the right NSM is a strategic choice).

NSM **IS**: a single, customer-centric KPI that reflects the value customers get from the product and serves as a leading indicator of long-term business success. You can use Key Results (OKRs) to express expected change in NSM.

Free resource: [The North Star Framework 101 (PDF)](https://learn.productcompass.pm/nsm101)

## When to Use

- Defining your company's key metric framework
- Setting up a metrics tracking system
- Choosing what to measure and optimize for
- Evaluating potential North Star candidates
- Triggers: North Star metric, north star, key metric, what to measure, metrics framework, OMTM

## The Three Business Games

Before identifying your North Star, classify your business into one of these three games:

- **Attention Game**: How much time do customers spend using your product? (Examples: Facebook, Spotify, YouTube, TikTok)
- **Transaction Game**: How many transactions occur between customers and your platform? (Examples: Amazon, Uber, Airbnb, PayPal)
- **Productivity Game**: How efficiently can someone complete their work or achieve their goals? (Examples: Canva, Dropbox, Loom, Notion)

## Prompt

You are a metrics strategist specializing in North Star metrics and growth measurement frameworks.

Given the following business context: $ARGUMENTS

**Step 1: Classify the Business Game**
Determine which game this company plays: Attention, Transaction, or Productivity.

**Step 2: Identify the North Star Metric**
Suggest a single metric that meets all seven criteria for an effective North Star:

1. **Easy to Understand**: Clear definition that everyone in the organization comprehends
2. **Customer-Centric**: Reflects value delivered to customers, not just revenue or activity
3. **Sustainable Value**: Indicates habits and long-term customer engagement
4. **Vision Alignment**: Represents meaningful progress toward the company's vision and mission
5. **Quantitative**: Measurable with clear, numeric tracking
6. **Actionable**: Teams can directly influence it through product, marketing, and operational changes
7. **Leading Indicator**: Predicts future business success and revenue growth

**Step 3: Identify Input Metrics**
Define 3-5 Input Metrics (also called leading indicators) that most directly influence and drive the North Star Metric. Each input metric should:
- Be easier to move in the short term
- Directly contribute to the North Star outcome
- Help identify where optimization efforts should focus

## Tips for Best Results

- Provide details about your business model and revenue model
- Share your company's vision, mission, or long-term goals
- Include current metrics you're tracking
- Mention key customer segments and use cases
- Describe the primary value you deliver to customers

---

### Further Reading

- [The North Star Framework 101](https://www.productcompass.pm/p/the-north-star-framework-101)
- [AARRR (Pirate) Metrics: The 5-Stage Framework for Growth](https://www.productcompass.pm/p/aarrr-pirate-metrics)
- [The Google HEART Framework: Your Guide to Measuring User-Centric Success](https://www.productcompass.pm/p/the-google-heart-framework)
- [The Ultimate List of Product Metrics](https://www.productcompass.pm/p/the-ultimate-list-of-product-metrics)
```

## File: `pm-marketing-growth/skills/positioning-ideas/SKILL.md`
```markdown
---
name: positioning-ideas
description: "Brainstorm product positioning ideas differentiated from competitors. Identifies top competitors and generates positioning statements with rationale. Use when developing product positioning, differentiating from competitors, or crafting brand positioning strategy."
---
# Positioning Ideas

Brainstorm product positioning ideas differentiated from competitors. Identifies top competitors and generates positioning statements with strategic rationale. Use when developing product positioning, differentiating from competitors, or crafting brand positioning strategy.

## When to Use

- Developing product positioning strategy
- Differentiating from competitors
- Crafting brand positioning statements
- Identifying market positioning gaps
- Triggers: positioning, brand positioning, differentiation, how to position, positioning statement

## Prompt

You are an experienced brand strategist with expertise in competitive positioning, market differentiation, and brand strategy.

Given the following product and market context: $ARGUMENTS

Follow these steps:

**Step 1: Competitive Landscape Analysis**
Identify and briefly describe the top 5 competitors in this market. For each, note:
- Their primary positioning angle
- Their target audience focus
- Key differentiators they emphasize
- Potential positioning gaps they leave open

**Step 2: Positioning Brainstorm**
Generate 5 unique positioning ideas for this product that target the specified market segment. Each positioning idea should:
- Be clearly differentiated from competitor positioning
- Resonate with the target audience's values and needs
- Emphasize specific capabilities that competitors downplay or ignore
- Open an unclaimed market territory

**Step 3: Positioning Statements**
For each idea, provide:

1. **Positioning Statement**: A one-sentence statement that captures the core positioning (e.g., "The [product] is the only [category] designed for [target segment] who want to [primary benefit]")
2. **Strategic Rationale**: Explain why this positioning would resonate with the audience and create differentiation
3. **Supporting Message**: Key supporting messages that reinforce this positioning
4. **Competitive Advantage**: What specific advantages enable this positioning claim

## Tips for Best Results

- Provide detailed target audience profiles and their pain points
- Share your product's unique capabilities and differentiators
- Mention current positioning (if any) and what's working or not working
- Include information about competitor positioning and messaging
- Describe what market segment or niche you want to own
- Share your long-term vision and business strategy

---

### Further Reading

- [Product Management vs. Product Marketing vs. Product Growth 101](https://www.productcompass.pm/p/product-management-vs-product-marketing)
- [How to Design a Value Proposition Customers Can't Resist?](https://www.productcompass.pm/p/how-to-design-value-proposition-template)
```

## File: `pm-marketing-growth/skills/product-name/SKILL.md`
```markdown
---
name: product-name
description: "Brainstorm 5 unique, memorable product names with rationale aligned to brand values and target audience. Use when naming a new product, rebranding, or exploring product name ideas."
---
# Product Name

Brainstorm unique, memorable product names with rationale aligned to brand values and target audience. Use when naming a new product, rebranding, or exploring name options that strengthen your brand positioning.

## When to Use

- Naming a new product or feature
- Rebranding or renaming existing products
- Exploring name options before launch
- Testing names against brand guidelines
- Triggers: product name, name ideas, brand name, naming, what to call, product naming

## Prompt

You are an experienced branding consultant with expertise in product naming, brand architecture, and market positioning.

Based on the following company and product context: $ARGUMENTS

Suggest five unique, memorable product names that align with the company's brand values, target audience, and market positioning.

For each name suggestion, provide:

1. **Name**: The proposed product name
2. **Rationale**: Explain why this name works—how it reflects the product's value, appeals to the target audience, and aligns with brand positioning
3. **Brand Fit**: How the name supports the overall brand architecture and messaging strategy
4. **Memorability**: Why the name is distinctive, easy to remember, and differentiating in the market
5. **Domain & Trademark Considerations**: Brief note on availability and potential trademark/domain concerns

Prioritize names that are:
- Easy to pronounce and spell
- Distinctive and differentiated from competitors
- Aligned with brand tone and positioning
- Relevant to the product's core value and use case
- Available for trademark and domain registration

## Tips for Best Results

- Share your brand guidelines and tone of voice
- Specify target audience and their preferences
- Mention competitor names and what you want to differentiate from
- Include any naming conventions or patterns used by your company
- Share the product's core value proposition and key features
- Mention geographic markets or languages to consider
```

## File: `pm-marketing-growth/skills/value-prop-statements/SKILL.md`
```markdown
---
name: value-prop-statements
description: "Generate value proposition statements for marketing, sales, and onboarding from existing value propositions. Use when writing marketing copy, creating sales messaging, or crafting onboarding messages."
---
# Value Proposition Statements

Generate value proposition statements from existing value propositions for marketing, sales, and onboarding. Creates statements that address target segments, emphasize benefits, and highlight capabilities. Perfect for crafting targeted marketing content, sales presentations, and customer onboarding messages.

## When to Use

- Writing marketing copy and promotional content
- Creating sales decks and pitch materials
- Crafting customer onboarding messages
- Developing segment-specific messaging
- Triggers: value proposition statements, marketing copy, sales messaging, value statements, positioning copy

## Prompt

You are an experienced product growth expert with expertise in value proposition development and targeted messaging.

Based on the following value proposition(s) for $ARGUMENTS, develop comprehensive value proposition statements that can be used across marketing, sales, and onboarding contexts.

For each statement, ensure it:
- Directly addresses a specific target market segment or use case
- Emphasizes the primary benefit and desired outcome
- Highlights the key features and capabilities that make it possible
- Uses clear, compelling language that resonates with the audience

## Example Framework (Canva)

To illustrate the approach, here are value proposition statements for Canva:

1. **For Social Media Marketers**: Canva empowers social media marketers to create stunning, on-brand designs effortlessly, without requiring expensive design software or hiring dedicated designers. Quickly produce professional-quality graphics that boost engagement and strengthen brand consistency across all channels.

2. **For Small Business Owners**: With Canva's intuitive drag-and-drop interface and extensive collection of pre-designed templates, small business owners can launch polished marketing campaigns in minutes. Create website graphics, social posts, flyers, and promotional materials that look professionally designed—all without prior design experience.

3. **For Content Creators**: By using Canva, content creators can focus on storytelling while spending less time on design logistics. Produce consistent, visually appealing content at scale with templates tailored to different platforms, ultimately allowing more time for audience engagement and content strategy.

## Tips for Best Results

- Provide existing value propositions or key benefits
- Specify target segments and their pain points
- Include product features and differentiators
- Share distribution channels (marketing, sales, onboarding)
- Mention any brand tone or voice guidelines

---

### Further Reading

- [How to Design a Value Proposition Customers Can't Resist?](https://www.productcompass.pm/p/how-to-design-value-proposition-template)
```

## File: `pm-product-discovery/README.md`
```markdown
# pm-product-discovery

Product discovery skills for PMs: ideation, experiments, assumption testing, feature prioritization, and customer interview synthesis.

## Skills (13)

- **analyze-feature-requests** — Analyze and prioritize a list of feature requests by theme, strategic alignment, impact, effort, and risk.
- **brainstorm-experiments-existing** — Design experiments to test assumptions for an existing product.
- **brainstorm-experiments-new** — Design lean startup experiments (pretotypes) for a new product.
- **brainstorm-ideas-existing** — Brainstorm product ideas for an existing product using multi-perspective ideation (PM, Designer, Engineer).
- **brainstorm-ideas-new** — Brainstorm feature ideas for a new product in initial discovery.
- **identify-assumptions-existing** — Identify risky assumptions for a feature idea in an existing product across Value, Usability, Viability, and Feasibility.
- **identify-assumptions-new** — Identify risky assumptions for a new product idea across 8 risk categories including Go-to-Market, Strategy, and Team.
- **interview-script** — Create a structured customer interview script with JTBD probing questions, warm-up, core exploration, and wrap-up sections.
- **metrics-dashboard** — Define and design a product metrics dashboard with key metrics, data sources, visualization types, and alert thresholds.
- **opportunity-solution-tree** — Build an Opportunity Solution Tree (OST) to structure product discovery — map a desired outcome to opportunities, solutions, and experiments.
- **prioritize-assumptions** — Prioritize assumptions using an Impact × Risk matrix and suggest experiments for each.
- **prioritize-features** — Prioritize a backlog of feature ideas based on impact, effort, risk, and strategic alignment.
- **summarize-interview** — Summarize a customer interview transcript into a structured template with JTBD, satisfaction signals, and action items.

## Commands (5)

- `/pm-product-discovery:brainstorm` — Brainstorm product ideas or experiments from PM, Designer, and Engineer perspectives — for existing or new products.
- `/pm-product-discovery:discover` — Run a full product discovery cycle — from ideation through assumption mapping to experiment design.
- `/pm-product-discovery:interview` — Prepare a customer interview script or summarize an interview transcript into structured insights.
- `/pm-product-discovery:setup-metrics` — Design a product metrics dashboard with North Star metric, input metrics, health metrics, and alert thresholds.
- `/pm-product-discovery:triage-requests` — Analyze, categorize, and prioritize a batch of feature requests from customers or stakeholders.

## Author

Paweł Huryn — [The Product Compass Newsletter](https://www.productcompass.pm)

## License

MIT
```

## File: `pm-product-discovery/commands/brainstorm.md`
```markdown
---
description: Brainstorm product ideas or experiments from PM, Designer, and Engineer perspectives — for existing or new products
argument-hint: "[ideas|experiments] [existing|new] <product or feature description>"
---

# /brainstorm -- Multi-Perspective Ideation

Generate creative product ideas or experiment designs from three perspectives (PM, Designer, Engineer), tailored to whether you're working on an existing product or building something new.

## Invocation

```
/brainstorm ideas existing Mobile banking app engagement
/brainstorm ideas new AI-powered meal planning for busy parents
/brainstorm experiments existing Onboarding flow redesign
/brainstorm experiments new Marketplace for freelance designers
/brainstorm                          # interactive mode — asks what you need
```

## Workflow

### Step 1: Determine Mode

Parse the arguments to identify two dimensions:

1. **What to brainstorm**: `ideas` (feature concepts) or `experiments` (validation tests)
2. **Product stage**: `existing` (continuous discovery) or `new` (initial discovery)

If either dimension is missing, ask the user. If both are missing, ask:
- "Are you brainstorming **ideas** for what to build, or **experiments** to validate assumptions?"
- "Is this for an **existing** product or a **new** product concept?"

### Step 2: Gather Context

Ask the user for context. Be conversational — ask the most critical question first:

**For existing products:**
- What is the product? Who are current users?
- What opportunity area or problem space are you exploring?
- Any constraints (technical debt, platform limitations, team capacity)?
- What has been tried before?

**For new products:**
- What is the product concept? What problem does it solve?
- Who is the target user? What's their current alternative?
- What stage are you at? (napkin sketch, validated problem, early prototype)
- What are the riskiest assumptions?

Accept context from uploaded files (PRDs, research docs, strategy decks), pasted text, or conversation.

### Step 3: Generate Output

**If brainstorming ideas** — apply the **brainstorm-ideas-existing** or **brainstorm-ideas-new** skill:
- Generate ideas from three perspectives: Product Manager (user value, business impact), Designer (UX, delight, accessibility), Engineer (technical innovation, platform leverage, scalability)
- For each idea: name, description, target user impact, feasibility assessment
- Rank the top 5 ideas with rationale
- Flag which ideas could be quick wins vs. strategic bets

**If brainstorming experiments** — apply the **brainstorm-experiments-existing** or **brainstorm-experiments-new** skill:
- For existing products: suggest A/B tests, prototypes, fake-door tests, wizard-of-oz, concierge experiments, and spikes
- For new products: create XYZ+S hypotheses and suggest pretotype experiments (landing pages, explainer videos, pre-orders, concierge MVPs)
- For each experiment: hypothesis, method, success criteria, effort estimate, expected timeline
- Rank by learning-per-effort ratio

### Step 4: Deepen and Iterate

After presenting initial results, offer:
- "Want me to **detail** any of these ideas into a fuller spec?"
- "Should I **identify assumptions** behind the top ideas?" (chains into the `identify-assumptions-existing` or `identify-assumptions-new` skill)
- "Want to **design experiments** to validate the top ideas?" (chains into experiment mode)
- "Should I **prioritize** these against your current backlog?" (chains into the `prioritize-features` skill)

## Output Format

### For Ideas:
```
## Brainstorm: [Product/Feature Area]
**Mode**: Ideas for [existing/new] product
**Context**: [1-2 sentence summary]

### PM Perspective
1. **[Idea Name]** — [description] | Impact: [H/M/L] | Effort: [H/M/L]
2. ...

### Designer Perspective
1. **[Idea Name]** — [description] | Impact: [H/M/L] | Effort: [H/M/L]
2. ...

### Engineer Perspective
1. **[Idea Name]** — [description] | Impact: [H/M/L] | Effort: [H/M/L]
2. ...

### Top 5 Recommendations
| Rank | Idea | Why | Quick Win? |
|------|------|-----|------------|

### Next Steps
[What to do with these ideas]
```

### For Experiments:
```
## Experiment Design: [Product/Feature Area]
**Mode**: Experiments for [existing/new] product

### Hypotheses
1. **[Hypothesis]** — XYZ format: [X]% of [Y] will [Z] within [S timeframe]

### Recommended Experiments
| # | Experiment | Tests Hypothesis | Method | Effort | Timeline |
|---|-----------|-----------------|--------|--------|----------|

### Experiment Details
[For each experiment: setup, success criteria, risks, what you'll learn]
```

## Notes

- For existing products, ground ideas in current user behavior and validated problems
- For new products, focus on desirability and feasibility risks first
- If the user uploads a research doc or interview transcript, extract insights before brainstorming
- Encourage breadth first, then depth — generate many ideas before evaluating
```

## File: `pm-product-discovery/commands/discover.md`
```markdown
---
description: Run a full product discovery cycle — from ideation through assumption mapping to experiment design
argument-hint: "<product or feature idea>"
---

# /discover -- Full Discovery Cycle

Run a structured product discovery process that moves from divergent thinking to focused validation. This command chains multiple skills into a single end-to-end workflow.

## Invocation

```
/discover Smart notification system for our project management tool
/discover New product: AI writing assistant for non-native speakers
/discover                    # asks what you're discovering
```

## Workflow

### Step 1: Understand the Discovery Context

Determine whether this is:
- **Existing product** — continuous discovery on a known product with real users
- **New product** — initial discovery for a concept without validated demand

Ask the user:
- What are you exploring? (product idea, feature area, opportunity space)
- What do you already know? (prior research, customer feedback, data)
- What decisions will this discovery inform? (build/kill, prioritize, pivot)

Accept context from uploaded files (research, PRDs, transcripts, data), links, or conversation.

### Step 2: Brainstorm Ideas (Divergent Phase)

Apply the **brainstorm-ideas-existing** or **brainstorm-ideas-new** skill:

- Generate ideas from PM, Designer, and Engineer perspectives
- Present the top 10 ideas with brief rationale
- Ask the user to select 3-5 ideas to carry forward, or accept all

**Checkpoint**: "Here are 10 ideas. Which ones should we stress-test? Pick 3-5, or I can carry all forward."

### Step 3: Identify Assumptions (Critical Thinking Phase)

For each selected idea, apply the **identify-assumptions-existing** or **identify-assumptions-new** skill:

- Surface assumptions across risk categories:
  - **Value**: Will users want this?
  - **Usability**: Can users figure it out?
  - **Feasibility**: Can we build it?
  - **Viability**: Does the business case work?
  - **Go-to-Market** (new products only): Can we reach and convert users?
- Use devil's advocate multi-perspective analysis
- Compile a master list of all assumptions across all ideas

### Step 4: Prioritize Assumptions (Focus Phase)

Apply the **prioritize-assumptions** skill:

- Map assumptions on an Impact × Risk matrix
- Identify the "leap of faith" assumptions — high impact, high uncertainty
- Rank assumptions by test priority
- Group related assumptions that can be tested together

**Checkpoint**: "Here are your riskiest assumptions. Which ones feel most critical to validate first?"

### Step 5: Design Experiments (Validation Phase)

For the top-priority assumptions, apply **brainstorm-experiments-existing** or **brainstorm-experiments-new** skill:

- Design 1-2 experiments per critical assumption
- For existing products: A/B tests, fake doors, prototypes, user tests, data analysis
- For new products: XYZ hypotheses, pretotypes, landing pages, concierge MVPs
- Include success criteria, timeline, and effort for each
- Sequence experiments by dependency and effort

### Step 6: Create Discovery Plan

Compile everything into a discovery plan document:

```
## Discovery Plan: [Topic]

**Date**: [today]
**Product Stage**: [existing/new]
**Discovery Question**: [what we're trying to learn]

### Ideas Explored
[Summary of brainstormed ideas with brief descriptions]

### Selected Ideas for Validation
[3-5 ideas carried forward with rationale]

### Critical Assumptions
| # | Assumption | Category | Impact | Uncertainty | Priority |
|---|-----------|----------|--------|-------------|----------|

### Validation Experiments
| # | Tests Assumption | Method | Success Criteria | Effort | Timeline |
|---|-----------------|--------|-----------------|--------|----------|

### Experiment Details
[For each experiment: hypothesis, setup, measurement, decision criteria]

### Discovery Timeline
Week 1: [experiments]
Week 2: [experiments]
Week 3: [analysis and decision]

### Decision Framework
- If [experiment] succeeds → proceed to [next step]
- If [experiment] fails → [pivot/kill/investigate further]
```

Save the plan as a markdown file to the user's workspace.

### Step 7: Offer Next Steps

- "Want me to **create a PRD** for the top idea?"
- "Should I **design an interview script** to supplement these experiments?"
- "Want me to **set up metrics** to track the experiments?"
- "Should I **estimate effort** and create user stories for the MVP?"

## Notes

- This is a 15-30 minute structured workflow — let the user know upfront
- At each checkpoint, the user can redirect, skip, or go deeper
- If the user has research data, pull insights from it before brainstorming
- The discovery plan should be a living document — offer to update it as experiments run
- For new products, emphasize desirability validation before feasibility
- For existing products, check if there's usage data that can inform assumptions
```

## File: `pm-product-discovery/commands/interview.md`
```markdown
---
description: Prepare a customer interview script or summarize an interview transcript into structured insights
argument-hint: "[prep|summarize] <topic or transcript>"
---

# /interview -- Customer Interview Prep & Summary

Two modes: **prep** creates a structured interview script before you talk to customers, **summarize** extracts insights after you've done the interview.

## Invocation

```
/interview prep Onboarding experience for enterprise users
/interview summarize [paste transcript or upload file]
/interview                    # asks which mode you need
```

## Modes

---

### Prep Mode

Create a structured interview script tailored to your research question.

#### Workflow

**Step 1: Understand the Research Goal**

Ask the user:
- What are you trying to learn? (specific research question)
- Who are you interviewing? (segment, role, relationship to product)
- How much time do you have? (15 min, 30 min, 60 min)
- What decisions will this research inform?

**Step 2: Generate Interview Script**

Apply the **interview-script** skill:

- Follow "The Mom Test" principles — ask about their life, not your idea
- No leading questions, no pitching, focus on past behavior and real situations
- Structure the script in sections:

```
## Interview Script: [Research Topic]

**Research Question**: [what we're trying to learn]
**Target Participant**: [who]
**Duration**: [X] minutes

### Warm-up (3-5 min)
[Rapport-building questions, role/context understanding]

### Core Exploration (15-40 min)
[JTBD probing, past behavior, current workflow, pain points]
- For each question: the question + why you're asking it + follow-up prompts

### Specific Topics (5-10 min)
[Targeted questions about specific features or concepts — if needed]

### Wrap-up (3-5 min)
[Open-ended closing, referral ask, next steps]

### Note-Taking Template
[Pre-formatted template to capture insights during the interview]

### Red Flags to Watch For
[Signs the conversation is going off-track or the participant is being polite rather than honest]
```

**Step 3: Customize and Review**

- Adjust question count to fit the time slot
- Add probing questions for specific hypotheses the user wants to test
- Flag questions that might lead the witness
- Offer a printable version (markdown file saved to workspace)

---

### Summarize Mode

Transform an interview transcript into structured, actionable insights.

#### Workflow

**Step 1: Accept the Transcript**

Accept in any format:
- **Pasted text**: Raw transcript or notes
- **Uploaded file**: Document, text file, or meeting notes export
- **Audio summary**: If the user describes what was said (not a full transcript)

If the input is rough notes rather than a full transcript, work with what's available and note the limitations.

**Step 2: Extract and Structure**

Apply the **summarize-interview** skill:

Parse the transcript to identify:
- **Participant profile**: Role, experience level, segment, context
- **Jobs to Be Done**: What the participant is trying to accomplish
- **Current workflow**: How they solve the problem today
- **Pain points**: Frustrations, workarounds, time sinks
- **Satisfaction signals**: What works well, moments of delight
- **Quotes**: Verbatim quotes that capture key insights (with timestamps if available)
- **Surprises**: Anything unexpected or that contradicts assumptions
- **Feature reactions**: If specific features/concepts were discussed, capture reactions

**Step 3: Generate Interview Summary**

```
## Interview Summary

**Participant**: [anonymized profile — role, segment, experience]
**Date**: [if known]
**Duration**: [if known]
**Interviewer**: [if known]

### Key Insights
1. **[Insight]** — [supporting evidence/quote]
2. **[Insight]** — [supporting evidence/quote]
3. ...

### Jobs to Be Done
- **Primary JTBD**: [When I..., I want to..., so I can...]
- **Related JTBDs**: [additional jobs]

### Current Workflow
[How the participant currently solves the problem, step by step]

### Pain Points
| Pain Point | Severity | Quote |
|-----------|----------|-------|

### Satisfaction Signals
| What Works | Why | Quote |
|-----------|-----|-------|

### Notable Quotes
> "[quote]" — on [topic]

### Assumptions Validated / Invalidated
| Assumption | Status | Evidence |
|-----------|--------|----------|

### Action Items
- [ ] [Follow-up action from this interview]
- [ ] [Research question to explore further]

### Raw Notes
[If helpful, include annotated key sections]
```

Save the summary as a markdown file.

**Step 4: Connect to Broader Research**

Offer:
- "Want me to **compare this with other interview summaries** you've done?"
- "Should I **update assumptions** based on what this participant said?"
- "Want me to **extract personas** from multiple interviews?"

## Notes

- In prep mode, always include "why you're asking" annotations — they help the interviewer stay on track
- In summarize mode, distinguish between what the participant *said* vs. what they *did* (behavioral > stated)
- Flag contradictions within the same interview (says one thing, describes doing another)
- If the transcript mentions competitor products, capture competitive intelligence
- For summarize mode, if multiple transcripts are provided, synthesize across them with cross-participant patterns
```

## File: `pm-product-discovery/commands/setup-metrics.md`
```markdown
---
description: Design a product metrics dashboard with North Star metric, input metrics, health metrics, and alert thresholds
argument-hint: "<product or feature area>"
---

# /setup-metrics -- Product Metrics Dashboard Design

Design a comprehensive metrics framework for your product or feature — from selecting the right North Star to defining alert thresholds that catch problems early.

## Invocation

```
/setup-metrics SaaS project management tool
/setup-metrics New checkout flow we just launched
/setup-metrics             # asks what you're measuring
```

## Workflow

### Step 1: Understand What to Measure

Ask the user:
- What product or feature area are you setting up metrics for?
- What stage is it in? (pre-launch, recently launched, mature)
- What are the current business goals or OKRs?
- Do you have existing metrics? What's missing or broken?
- What analytics tools are you using? (helps tailor implementation advice)

### Step 2: Define the Metrics Framework

Apply the **metrics-dashboard** skill:

**North Star Metric:**
- Identify the single metric that best captures the value your product delivers to users
- Validate against criteria: measures value delivery, is a leading indicator, is actionable
- Define the metric precisely (formula, data source, time window)

**Input Metrics (3-5):**
- Identify the levers that drive the North Star
- Each input metric should be directly actionable by a team
- Map the causal chain: Input → North Star → Business Outcome

**Health Metrics (3-5):**
- Metrics that should stay stable — if they degrade, something is wrong
- Examples: error rates, latency, support ticket volume, NPS, churn rate
- Define "healthy" ranges and degradation thresholds

**Counter-Metrics (1-2):**
- Metrics that could indicate you're optimizing the wrong way
- Example: if North Star is "daily active users", counter-metric is "session quality" to prevent empty engagement

### Step 3: Design Alert Thresholds

For each metric:

| Metric | Green | Yellow | Red | Check Frequency |
|--------|-------|--------|-----|----------------|
| [metric] | [healthy range] | [warning] | [critical] | [daily/weekly] |

- **Yellow**: Investigate — something may be off
- **Red**: Act immediately — page someone or escalate

### Step 4: Create Dashboard Spec

```
## Metrics Dashboard: [Product/Feature]

**North Star**: [metric name]
**Definition**: [precise formula]
**Current value**: [if known]
**Target**: [goal]

### Input Metrics
| Metric | Definition | Owner | Target | Current |
|--------|-----------|-------|--------|---------|

### Health Metrics
| Metric | Healthy Range | Yellow Threshold | Red Threshold |
|--------|-------------|-----------------|---------------|

### Counter-Metrics
| Metric | Why It Matters | Watch For |
|--------|---------------|-----------|

### Metrics Tree
North Star: [metric]
├── Input: [metric 1] → driven by [team/action]
├── Input: [metric 2] → driven by [team/action]
├── Input: [metric 3] → driven by [team/action]
└── Counter: [metric] → watch for [degradation signal]

### Implementation Notes
- Data sources: [where each metric comes from]
- Refresh frequency: [real-time / hourly / daily]
- Tool recommendations: [based on user's stack]

### Review Cadence
- **Daily**: Glance at North Star and health metrics
- **Weekly**: Review input metrics trends, discuss in team standup
- **Monthly**: Deep dive — are inputs driving the North Star as expected?
- **Quarterly**: Reassess the metrics framework itself
```

Save as a markdown file to the user's workspace.

### Step 5: Offer Next Steps

- "Want me to **write SQL queries** to compute these metrics?"
- "Should I **create OKRs** based on this metrics framework?"
- "Want me to **build a cohort analysis** to set realistic baselines?"
- "Should I **set up a weekly metrics review template**?"

## Notes

- A good North Star is rare — most teams pick vanity metrics. Push for a metric that captures *user value delivered*, not just engagement
- Input metrics should be MECE (mutually exclusive, collectively exhaustive) in explaining the North Star
- If the product is pre-launch, define metrics now but note that baselines will need calibration after launch
- Counter-metrics prevent Goodhart's Law — when a metric becomes a target, it ceases to be a good metric
- Recommend starting with fewer metrics, well-instrumented, over a sprawling dashboard nobody checks
```

## File: `pm-product-discovery/commands/triage-requests.md`
```markdown
---
description: Analyze, categorize, and prioritize a batch of feature requests from customers or stakeholders
argument-hint: "<feature requests as text, file, or paste>"
---

# /triage-requests -- Feature Request Triage

Take a pile of feature requests — from support tickets, sales calls, surveys, or Slack — and turn them into a prioritized, actionable backlog.

## Invocation

```
/triage-requests                           # asks for input
/triage-requests [paste a list of requests]
/triage-requests [upload a CSV/spreadsheet]
```

## Workflow

### Step 1: Accept Feature Requests

Accept requests in any format:
- **Pasted text**: List of requests, one per line or paragraph
- **Uploaded file**: CSV, Excel, or text file with request data
- **Structured data**: If the input has columns (requester, request, date, etc.), preserve them

If no input is provided, ask the user to paste or upload their feature requests.

Parse each request to extract:
- The core ask (what the user wants)
- Context (who asked, when, why — if available)
- Frequency signals (how many people asked for similar things)

### Step 2: Gather Prioritization Context

Ask the user (conversationally, not all at once):
- What is the product? What stage is it in?
- What are the current strategic goals or OKRs? (helps assess alignment)
- Any constraints to consider? (team size, technical debt, upcoming deadlines)
- Are there segments whose requests should carry more weight? (enterprise, churning users, power users)

### Step 3: Categorize and Analyze

Apply the **analyze-feature-requests** skill:

- **Theme clustering**: Group similar requests into themes (e.g., "reporting & analytics", "collaboration", "mobile experience")
- **Request count per theme**: How many unique requests map to each theme
- **Strategic alignment**: Rate each theme against stated goals (High/Medium/Low/None)
- **Segment analysis**: Which user segments are driving which themes
- **Sentiment signals**: Are requests accompanied by frustration, churn threats, or delight?

### Step 4: Prioritize

Apply the **prioritize-features** skill:

For each theme (and the top individual requests within each theme):

| Factor | Assessment |
|--------|-----------|
| **Impact** | How many users affected? How severely? |
| **Strategic alignment** | Does it serve current goals? |
| **Effort estimate** | T-shirt size (S/M/L/XL) |
| **Risk** | What happens if we don't do this? |
| **Revenue signal** | Is this tied to deals, retention, or expansion? |

Rank themes and produce a prioritized list.

### Step 5: Generate Triage Report

```
## Feature Request Triage Report

**Date**: [today]
**Requests analyzed**: [count]
**Themes identified**: [count]

### Theme Summary
| # | Theme | Requests | Top Ask | Alignment | Impact | Effort | Priority |
|---|-------|----------|---------|-----------|--------|--------|----------|

### Priority 1: Act Now
[Themes/requests to include in near-term planning]
- **[Theme]**: [X] requests — [why it's urgent]
  - Top requests: [list]
  - Recommended action: [build / prototype / investigate]

### Priority 2: Plan Next
[Themes worth planning but not urgent]

### Priority 3: Collect More Signal
[Themes with potential but insufficient evidence]

### Priority 4: Decline or Defer
[Requests that don't align with strategy — with rationale]

### Notable Individual Requests
[High-value one-off requests that didn't cluster into themes]

### Patterns and Insights
- [Key insight about what users are telling you]
- [Segment-specific patterns]
- [Gaps between what users ask for and underlying needs]
```

Save the report as a markdown file to the user's workspace.

### Step 6: Offer Next Steps

- "Want me to **create user stories** for the top-priority items?"
- "Should I **brainstorm solutions** for any of these themes?"
- "Want me to **design experiments** to validate demand before building?"
- "Should I **draft a stakeholder update** summarizing this analysis?"

## Notes

- If the user provides a CSV with columns, preserve the data structure and enrich it
- Look for the need behind the request — "add dark mode" might really mean "reduce eye strain during long sessions"
- Flag requests that conflict with each other (e.g., "simplify the UI" vs. "add more configuration options")
- If request volume is large (50+), summarize themes first and offer to drill into specific themes on request
- Output the enriched data as a downloadable CSV if the input was structured data
```

## File: `pm-product-discovery/skills/analyze-feature-requests/SKILL.md`
```markdown
---
name: analyze-feature-requests
description: "Analyze and prioritize a list of feature requests by theme, strategic alignment, impact, effort, and risk. Use when reviewing customer feature requests, triaging a backlog, or making prioritization decisions."
---

## Analyze Feature Requests

Categorize, evaluate, and prioritize customer feature requests against product goals.

### Context

You are analyzing feature requests for **$ARGUMENTS**.

If the user provides files (spreadsheets, CSVs, or documents with feature requests), read and analyze them directly. If data is in a structured format, consider creating a summary table.

### Domain Context

Never allow customers to design solutions. Prioritize **opportunities (problems)**, not features. Use **Opportunity Score** (Dan Olsen) to evaluate customer-reported problems: Opportunity Score = Importance × (1 − Satisfaction), normalized to 0–1. See the `prioritization-frameworks` skill for full details and templates.

### Instructions

The user will describe their product goal and provide feature requests. Work through these steps:

1. **Understand the goal**: Confirm the product objective and desired outcomes that will guide prioritization.

2. **Categorize requests into themes**: Group related requests together and name each theme.

3. **Assess strategic alignment**: For each theme, evaluate how well it aligns with the stated goals.

4. **Prioritize the top 3 features** based on:
   - **Impact**: Customer value and number of users affected
   - **Effort**: Development and design resources required
   - **Risk**: Technical and market uncertainty
   - **Strategic alignment**: Fit with product vision and goals

5. **For each top feature**, provide:
   - Rationale (customer needs, strategic alignment)
   - Alternative solutions worth considering
   - High-risk assumptions
   - How to test those assumptions with minimal effort

Think step by step. Save as markdown or create a structured output document.

---

### Further Reading

- [Kano Model: How to Delight Your Customers Without Becoming a Feature Factory](https://www.productcompass.pm/p/kano-model-how-to-delight-your-customers)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)
```

## File: `pm-product-discovery/skills/brainstorm-experiments-existing/SKILL.md`
```markdown
---
name: brainstorm-experiments-existing
description: "Design experiments to test assumptions for an existing product — prototypes, A/B tests, spikes, and other low-effort validation methods. Use when validating assumptions, testing feature ideas cheaply, or planning product experiments."
---

## Design Experiments (Existing Product)

Design low-effort experiments to test product assumptions before committing to full implementation.

### Context

You are helping a product team design experiments for **$ARGUMENTS**. The team has a feature idea and assumptions that need validation.

If the user provides files (PRDs, assumption lists, designs), read them first.

### Instructions

The user will describe their idea and assumptions. Work through these steps:

1. **Clarify the idea and assumptions**: Confirm what the team wants to build and what they need to validate.

2. **Suggest experiments** for each assumption. Consider methods like:
   - First-click testing or task completion with a prototype
   - Feature stubs or fake door tests
   - Technical spikes
   - A/B tests on production (with risk mitigation)
   - Wizard of Oz approaches
   - Survey-based validation (behavioral, not opinion-based)

3. **Key principles to follow**:
   - Measure actual behavior, not users' opinions
   - Test responsibly — don't put users or the business at risk
   - For production tests (e.g., A/B tests), explain risk mitigation strategies
   - Aim for maximum validated learning with minimal effort

4. **For each experiment**, specify:
   - **Assumption**: What do we believe?
   - **Experiment**: What exactly will we do to validate it?
   - **Metric**: What will be measured?
   - **Success threshold**: The expected value if we are right

Think step by step. Present experiments in a clear table or structured format. Save as markdown if substantial.

---

### Further Reading

- [Testing Product Ideas: The Ultimate Validation Experiments Library](https://www.productcompass.pm/p/the-ultimate-experiments-library)
- [Assumption Prioritization Canvas: How to Identify And Test The Right Assumptions](https://www.productcompass.pm/p/assumption-prioritization-canvas)
- [What Is Product Discovery? The Ultimate Guide Step-by-Step](https://www.productcompass.pm/p/what-exactly-is-product-discovery)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)
```

## File: `pm-product-discovery/skills/brainstorm-experiments-new/SKILL.md`
```markdown
---
name: brainstorm-experiments-new
description: "Design lean startup experiments (pretotypes) for a new product. Creates XYZ hypotheses and suggests low-effort validation methods like landing pages, explainer videos, and pre-orders. Use when validating a new product idea, creating pretotypes, or testing market demand."
---

## Design Lean Startup Experiments (New Product)

Create XYZ hypotheses and design pretotype experiments to validate a new product concept with minimal effort.

### Context

You are helping validate a new product concept: **$ARGUMENTS** using lean startup methodology.

If the user provides files (market research, landing page mockups), read them first.

### Instructions

1. **Create an XYZ Hypothesis** in the form: "At least X% of Y will do Z"
   - **X%**: The percentage of the target market expected to engage
   - **Y**: The specific target market (e.g., "mid-size luxury sedan buyers")
   - **Z**: How they will engage with the product

2. **Suggest 2-3 pretotype experiments** to test the hypothesis with minimal effort. Consider:
   - **Landing Page**: Test interest by measuring sign-ups or clicks
   - **Explainer Video**: Test understanding and appeal through engagement metrics
   - **Email Campaign**: Test demand through response and click-through rates
   - **Pre-Order / Waitlist**: Test willingness to pay through skin-in-the-game commitment
   - **Concierge / Manual MVP**: Deliver the service manually to test value

3. **Key principles** (Alberto Savoia, *The Right It*):
   - **Skin-in-the-Game**: Test willingness to pay — not just interest. Real commitment (time, money, reputation) is the only reliable signal.
   - **Your Own Data (YODA)**: Collect your own data through experiments rather than relying on Others' Data (ODP) like market reports or analogies. "The market for your idea does not care about the market for someone else's idea."
   - Measure actual behavior, not users' opinions

4. **For each experiment**, specify the hypothesis being tested, the method, the metric, and the success threshold.

Think step by step. Save as markdown if substantial.

---

### Further Reading

- [How to Build the Right Product with Alberto Savoia (ex-Innovator at Google)](https://www.productcompass.pm/p/how-to-build-the-right-product-with)
- [Testing Product Ideas: The Ultimate Validation Experiments Library](https://www.productcompass.pm/p/the-ultimate-experiments-library)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)
```

## File: `pm-product-discovery/skills/brainstorm-ideas-existing/SKILL.md`
```markdown
---
name: brainstorm-ideas-existing
description: "Brainstorm product ideas for an existing product using multi-perspective ideation from PM, Designer, and Engineer viewpoints. Use when generating new feature ideas, brainstorming solutions for an identified opportunity, or ideating with a product trio."
---

## Brainstorm Product Ideas (Existing Product)

Multi-perspective ideation for continuous product discovery. Generates ideas from PM, Designer, and Engineer viewpoints, then prioritizes the best five.

### Context

You are supporting a product trio performing continuous product discovery for **$ARGUMENTS**.

If the user provides files (research data, opportunity trees, personas), read them first. If they mention a product URL, use web search to understand the product.

### Domain Context

**Product Trio** (Teresa Torres, *Continuous Discovery Habits*): PM + Designer + Engineer collaborate on discovery together. "Best ideas often come from engineers." Discovery is not linear — loop back if experiments fail. Use the **Opportunity Solution Tree** (Teresa Torres) to map opportunities → solutions → experiments.

### Instructions

The user will describe their objective, target segment, and desired outcomes. Work through these steps:

1. **Understand the opportunity**: Confirm the product, objective, market segment, and desired outcomes. Ask for clarification if anything is ambiguous.

2. **Ideate from three perspectives** — generate 5 ideas each from:
   - **Product Manager**: Focus on business value, strategic alignment, and customer impact
   - **Product Designer**: Focus on user experience, usability, and delight
   - **Software Engineer**: Focus on technical possibilities, data leverage, and scalable solutions

3. **Prioritize the top 5 ideas** across all perspectives based on:
   - Strategic alignment with the stated objective
   - Potential impact on desired outcomes
   - Feasibility and effort required
   - Differentiation from existing solutions

4. **For each prioritized idea**, provide:
   - A clear name and one-sentence description
   - Why it was selected (reasoning)
   - Key assumptions to validate

Think step by step. Present ideas in a clear, structured format.

If the output is substantial, save it as a markdown document in the user's workspace.

---

### Further Reading

- [What Is Product Discovery? The Ultimate Guide Step-by-Step](https://www.productcompass.pm/p/what-exactly-is-product-discovery)
- [Product Trio: Beyond the Obvious](https://www.productcompass.pm/p/product-trio)
- [The Extended Opportunity Solution Tree](https://www.productcompass.pm/p/the-extended-opportunity-solution-tree)
- [Product Model First Principles: Product Discovery, Product Delivery, and Product Culture In Depth](https://www.productcompass.pm/p/product-model-first-principles-discovery-deliver)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)
```

## File: `pm-product-discovery/skills/brainstorm-ideas-new/SKILL.md`
```markdown
---
name: brainstorm-ideas-new
description: "Brainstorm feature ideas for a new product in initial discovery from PM, Designer, and Engineer perspectives. Use when starting product discovery for a new product, exploring features for a startup idea, or doing initial ideation."
---

## Brainstorm Product Ideas (New Product)

Multi-perspective ideation for initial product discovery of a new product. Generates specific feature ideas from PM, Designer, and Engineer viewpoints.

### Context

You are supporting initial product discovery for a new product: **$ARGUMENTS**.

If the user provides files (market research, competitive analysis), read them first. Use web search to understand the market if needed.

### Domain Context

**Initial Discovery vs Continuous Discovery**: Initial Discovery focuses on vision, business model, and market validation — you're testing whether the product should exist. Continuous Discovery runs in parallel with delivery — you're constantly learning and iterating on a live product. This skill is for **initial discovery**.

### Instructions

The user will describe their target segment, opportunity, and desired outcomes. Work through these steps:

1. **Understand the opportunity**: Confirm the product concept, target market segment, and what the users want to achieve.

2. **Ideate from three perspectives** — generate 5 specific feature ideas each from:
   - **Product Manager**: Focus on market fit, value creation, and competitive advantage
   - **Product Designer**: Focus on user experience, onboarding, and engagement
   - **Software Engineer**: Focus on technical innovation, API integrations, and platform capabilities

3. **Prioritize the top 5 ideas** across all perspectives. For a new product, weight heavily toward:
   - Core value delivery (does it solve the primary problem?)
   - Speed to validate (can we test this quickly?)
   - Differentiation potential

4. **For each prioritized idea**, provide reasoning and key assumptions to test.

Think step by step. Save substantial output as a markdown document.

---

### Further Reading

- [Startup Canvas: Product Strategy and a Business Model for a New Product](https://www.productcompass.pm/p/startup-canvas)
- [Product Innovation Masterclass](https://www.productcompass.pm/p/product-innovation-masterclass) (video course)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)
```

## File: `pm-product-discovery/skills/identify-assumptions-existing/SKILL.md`
```markdown
---
name: identify-assumptions-existing
description: "Identify risky assumptions for a feature idea in an existing product across Value, Usability, Viability, and Feasibility. Uses multi-perspective devil's advocate thinking. Use when stress-testing a feature idea, doing risk assessment, or preparing for assumption mapping."
---

## Identify Assumptions (Existing Product)

Devil's advocate analysis to surface risky assumptions across four risk areas.

### Context

You are stress-testing a feature idea for **$ARGUMENTS**.

If the user provides files (designs, PRDs, research), read them first.

### Instructions

The user will describe their product, objective, market segment, and feature idea. Work through these steps:

1. **Think from three perspectives** about why this feature might fail:
   - **Product Manager perspective**: Business viability, market fit, strategic alignment
   - **Designer perspective**: Usability, user experience, adoption barriers
   - **Engineer perspective**: Technical feasibility, performance, integration challenges

2. **Identify assumptions across four risk areas**:
   - **Value**: Will it create value for customers? Does it solve a real problem?
   - **Usability**: Will users figure out how to use it? Is the learning curve acceptable?
   - **Viability**: Can marketing, sales, finance, and legal support it?
   - **Feasibility**: Can it be built with existing technology? Are there integration risks?

3. **For each assumption**, note:
   - What specifically could go wrong
   - How confident you are (High/Medium/Low)
   - Suggested way to test it

Think step by step. Be thorough but constructive — the goal is to strengthen the idea, not kill it.

---

### Further Reading

- [Assumption Prioritization Canvas: How to Identify And Test The Right Assumptions](https://www.productcompass.pm/p/assumption-prioritization-canvas)
- [How to Manage Risks as a Product Manager](https://www.productcompass.pm/p/how-to-manage-risks-as-a-product-manager)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)
```

## File: `pm-product-discovery/skills/identify-assumptions-new/SKILL.md`
```markdown
---
name: identify-assumptions-new
description: "Identify risky assumptions for a new product idea across 8 risk categories including Go-to-Market, Strategy, and Team. Use when evaluating startup risks, assessing a new product concept, or mapping assumptions for a new venture."
---

## Identify Assumptions (New Product)

Comprehensive risk identification across 8 categories — extending the 4 core product risks (Teresa Torres, *Continuous Discovery Habits*) with Ethics, Go-to-Market, Strategy & Objectives, and Team risks that are critical for new products.

### Context

You are evaluating assumptions for a new product: **$ARGUMENTS**.

If the user provides files (business plans, research), read them first.

### Domain Context

**The 4 core product risks** (Teresa Torres, *Continuous Discovery Habits*): Value, Usability, Viability, Feasibility.

**For new products, extend to 8 risk categories.** Good teams assume at least three-quarters of their ideas won't perform as they hope.

### Instructions

The user will describe the product concept, target segment, and feature idea. Work through these steps:

1. **Think from three perspectives** about why this product might fail:
   - **Product Manager**: Market demand, willingness to pay, competitive landscape
   - **Designer**: First-time user experience, onboarding, engagement
   - **Engineer**: Build vs. buy decisions, scalability, technical debt

2. **Identify assumptions across 8 risk categories**:

   - **Value**: Will it create value for customers? Will they keep using it?
   - **Usability**: Will people figure out how to use it? Can we onboard them fast enough? Will it increase cognitive load?
   - **Viability**: Can we sell/monetize/finance it? Is it worth the cost? Can we support customers and help them succeed? Can we scale? Will it be compliant?
   - **Feasibility**: Can we do it with the current technology? Is this integration possible? Can it be efficient? Can we scale it?
   - **Ethics**: Should we do it at all? Are there any ethical considerations? Will it pose a risk for our customers?
   - **Go-to-Market** (especially critical for new products): Can we market it? Do we have the required channels? Can we convince customers to try it? Is this the right messaging for this channel? Is this the right time? Is this the right way to launch it?
   - **Strategy & Objectives**: What are our assumptions? Can others copy our strategy? Have we considered political, economic, legal, technological, and environmental factors? Are those the best problems to solve?
   - **Team**: How well will the team work together? Do we have the right people? Do we have the right tools? Will the entire team stay with us long enough?

3. **For each assumption**, rate confidence and suggest a test.

Think step by step. Save as markdown.

---

### Further Reading

- [Assumption Prioritization Canvas: How to Identify And Test The Right Assumptions](https://www.productcompass.pm/p/assumption-prioritization-canvas)
- [What Is Product Discovery? The Ultimate Guide Step-by-Step](https://www.productcompass.pm/p/what-exactly-is-product-discovery)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)
```

## File: `pm-product-discovery/skills/interview-script/SKILL.md`
```markdown
---
name: interview-script
description: "Create a structured customer interview script with JTBD probing questions, warm-up, core exploration, and wrap-up sections. Follows The Mom Test principles — no leading questions, no pitching, focus on past behavior. Use when preparing for user interviews, creating interview guides, or planning discovery research."
---

## Customer Interview Script

Create a structured interview script that surfaces real insights, not just opinions. Follows "The Mom Test" principles — ask about their life, not your idea.

### Domain Context

Customer interviews are one source in **Stage 1 (Explore)** of continuous discovery. Other sources: stakeholder interviews, usage analytics, data analytics, surveys, market trends, SEO/SEM analysis. The PM needs direct access to users, stakeholders, engineers, and designers — "without proxies." The **Product Trio** (PM + Designer + Engineer — Teresa Torres) should work together on discovery, not just the PM alone.

### Context

You are preparing a customer interview script for research on **$ARGUMENTS**.

If the user provides files (personas, hypothesis lists, product briefs, or previous interview notes), read them first.

### Instructions

1. **Clarify research objectives**:
   - What specific questions does the team need answered?
   - What decisions will this research inform?
   - What assumptions need validation?

2. **Create the interview script** with these sections:

   ### Opening (2-3 min)
   - Introduce yourself and the purpose (learning, not selling)
   - Set expectations: "There are no right or wrong answers. We're here to learn from your experience."
   - Ask permission to record (if applicable)
   - Confirm time available

   ### Warm-Up: Context & Background (5 min)
   - "Tell me about your role and what a typical day/week looks like."
   - "How long have you been doing [activity related to the product area]?"
   - Goal: Build rapport and understand their context

   ### Core Exploration: Jobs to Be Done (15-20 min)

   **Current situation and behavior** (past tense, specific instances):
   - "Walk me through the last time you [did the thing we're exploring]. What happened?"
   - "What tools or methods did you use?"
   - "How long did it take? Who else was involved?"

   **Pain points and frustrations** (observe, don't lead):
   - "What was the hardest part about that?"
   - "If you could wave a magic wand, what would change?"
   - "What have you tried to solve this? What happened?"

   **Desired outcomes** (their words, not yours):
   - "What does 'good' look like for you in this area?"
   - "How would you know if this was working well?"

   **Willingness to pay / priority** (skin in the game):
   - "How much time/money do you currently spend on this?"
   - "Have you looked for a better solution? What did you find?"
   - "What would you give up to have this solved?"

   ### Probing Techniques
   Use these when you hit an interesting thread:
   - **"Tell me more about that"** — opens up any topic
   - **"Why?"** (asked gently, 2-3 times) — gets to root causes
   - **"Can you give me a specific example?"** — moves from opinions to facts
   - **"What happened next?"** — follows the story
   - **"How did that make you feel?"** — captures emotional intensity

   ### The Mom Test Rules
   - Ask about **their life**, not your idea
   - Ask about **the past**, not the future ("Would you use X?" is useless)
   - **Talk less, listen more** — aim for 80/20 split
   - **Never pitch** during the interview
   - Look for **strong emotions** — they signal real pain or delight
   - **Compliments are noise** — "That sounds cool!" tells you nothing

   ### Wrap-Up (3-5 min)
   - "Is there anything I didn't ask that you think is important?"
   - "Who else should I talk to about this?"
   - Thank them for their time
   - Share next steps (if any)

3. **Customize the script**: Adapt questions to the specific product area, persona, and research objectives. Add or remove sections based on the interview length available.

4. **Include a note-taking template**:
   ```
   Participant: [Name / ID]
   Date: [Date]
   Key Jobs: [What they're trying to accomplish]
   Current Solution: [What they use today]
   Biggest Pain: [Their #1 frustration]
   Desired Outcome: [What success looks like]
   Willingness to Pay: [How much they invest / would invest]
   Surprise Finding: [Something unexpected]
   Follow-up: [Next steps]
   ```

Save as markdown. Include both the script and the note-taking template.

---

### Further Reading

- [User Interviews: The Ultimate Guide to Research Interviews](https://www.productcompass.pm/p/interviewing-customers-the-ultimate)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)
```

## File: `pm-product-discovery/skills/metrics-dashboard/SKILL.md`
```markdown
---
name: metrics-dashboard
description: "Define and design a product metrics dashboard with key metrics, data sources, visualization types, and alert thresholds. Use when creating a metrics dashboard, defining KPIs, setting up product analytics, or building a data monitoring plan."
---

## Product Metrics Dashboard

Design a comprehensive product metrics dashboard with the right metrics, visualizations, and alert thresholds.

### Context

You are designing a metrics dashboard for **$ARGUMENTS**.

If the user provides files (existing dashboards, analytics data, OKRs, or strategy docs), read them first.

### Domain Context

**Metrics vs KPIs vs NSM**: Metrics = all measurable things. KPIs = a few key quantitative metrics tracked over a longer period. North Star Metric = a single customer-centric KPI that is a leading indicator of business success.

**4 criteria for a good metric** (Ben Yoskovitz, *Lean Analytics*): (1) Understandable — creates a common language. (2) Comparative — over time, not a snapshot. (3) Ratio or Rate — more revealing than whole numbers. (4) Behavior-changing — the Golden Rule: "If a metric won't change how you behave, it's a bad metric."

**8 metric types**: Vanity vs Actionable (only actionable metrics change behavior), Qualitative vs Quantitative (WHAT vs WHY — you need both; never stop talking to customers), Exploratory vs Reporting (explore data to uncover unexpected insights), Lagging vs Leading (leading indicators enable faster learning cycles, e.g. customer complaints predict churn).

**5 action steps**: (1) Audit metrics against the 4 good-metric criteria. (2) Update dashboards — ensure all key metrics are good ones. (3) Identify vanity metrics — be careful how you use them. (4) Classify leading vs lagging indicators. (5) Pick one problem and dig deep into the data.

For case studies and more detail: [Are You Tracking the Right Metrics?](https://www.productcompass.pm/p/are-you-tracking-the-right-metrics) by Ben Yoskovitz

### Instructions

1. **Identify the metrics framework** — organize metrics into layers:

   **North Star Metric**: The single metric that best captures core value delivery

   **Input Metrics** (3-5): The levers that drive the North Star

   **Health Metrics**: Guardrails that ensure overall product health

   **Business Metrics**: Revenue, cost, and unit economics

2. **For each metric, define**:

   | Metric | Definition | Data Source | Visualization | Target | Alert Threshold |
   |---|---|---|---|---|---|
   | [Name] | [Exact calculation: numerator/denominator, time window] | [Where the data comes from] | [Line chart / Bar / Number / Funnel] | [Goal value] | [When to trigger an alert] |

3. **Design the dashboard layout**:

   ```
   ┌─────────────────────────────────────────────┐
   │  NORTH STAR: [Metric] — [Current Value]     │
   │  Trend: [↑/↓ X% vs last period]             │
   ├──────────────────┬──────────────────────────┤
   │  Input Metric 1  │  Input Metric 2          │
   │  [Sparkline]     │  [Sparkline]             │
   ├──────────────────┼──────────────────────────┤
   │  Input Metric 3  │  Input Metric 4          │
   │  [Sparkline]     │  [Sparkline]             │
   ├──────────────────┴──────────────────────────┤
   │  HEALTH: [Latency] [Error Rate] [NPS]       │
   ├─────────────────────────────────────────────┤
   │  BUSINESS: [MRR] [CAC] [LTV] [Churn]        │
   └─────────────────────────────────────────────┘
   ```

4. **Set review cadence**:
   - **Daily**: Operational health (errors, latency, critical flows)
   - **Weekly**: Input metrics and engagement trends
   - **Monthly**: North Star, business metrics, OKR progress
   - **Quarterly**: Strategic review and metric recalibration

5. **Define alerts**:
   - What thresholds trigger investigation?
   - Who gets alerted and through what channel?
   - What's the expected response time?

6. **Recommend tools** based on the user's context:
   - Amplitude, Mixpanel, PostHog for product analytics
   - Looker, Metabase, Mode for SQL-based dashboards
   - Datadog, Grafana for operational health

Think step by step. Save the dashboard specification as a markdown document.

---

### Further Reading

- [The Ultimate List of Product Metrics](https://www.productcompass.pm/p/the-ultimate-list-of-product-metrics)
- [The North Star Framework 101](https://www.productcompass.pm/p/the-north-star-framework-101)
- [The Product Analytics Playbook: AARRR, HEART, Cohorts & Funnels for PMs](https://www.productcompass.pm/p/the-product-analytics-playbook-aarrr)
- [AARRR (Pirate) Metrics: The 5-Stage Framework for Growth](https://www.productcompass.pm/p/aarrr-pirate-metrics)
- [The Google HEART Framework: Your Guide to Measuring User-Centric Success](https://www.productcompass.pm/p/the-google-heart-framework)
- [Funnel Analysis 101: How to Track and Optimize Your User Journey](https://www.productcompass.pm/p/funnel-analysis)
- [Are You Tracking the Right Metrics?](https://www.productcompass.pm/p/are-you-tracking-the-right-metrics)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)
```

## File: `pm-product-discovery/skills/opportunity-solution-tree/SKILL.md`
```markdown
---
name: opportunity-solution-tree
description: "Build an Opportunity Solution Tree (OST) to structure product discovery — map a desired outcome to opportunities, solutions, and experiments. Based on Teresa Torres' Continuous Discovery Habits. Use when structuring discovery work, mapping opportunities to solutions, or deciding what to build next."
---

## Opportunity Solution Tree (OST)

A visual framework for structuring continuous product discovery. Connects a desired **outcome** to customer **opportunities**, possible **solutions**, and **experiments** to validate them.

### Domain Context

The **Opportunity Solution Tree** (Teresa Torres, *Continuous Discovery Habits*) is the backbone of modern product discovery. It prevents teams from jumping to solutions by forcing them to first map the opportunity space.

**Structure (4 levels):**

1. **Desired Outcome** (top) — The measurable business or product outcome the team is pursuing. Should be a single, clear metric (e.g., "increase 7-day retention to 40%"). This comes from your OKRs or product strategy.

2. **Opportunities** (second level) — Customer needs, pain points, or desires discovered through research. These are problems worth solving — not features. Frame them from the customer's perspective: "I struggle to..." or "I wish I could..." Prioritize using Opportunity Score: **Importance × (1 − Satisfaction)** (Dan Olsen, *The Lean Product Playbook*). Normalize Importance and Satisfaction to 0–1.

3. **Solutions** (third level) — Possible ways to address each opportunity. Generate multiple solutions per opportunity — don't commit to the first idea. The **Product Trio** (PM + Designer + Engineer) should ideate together. "Best ideas often come from engineers."

4. **Experiments** (bottom) — Fast, cheap tests to validate whether a solution actually addresses the opportunity. Use assumption testing (Value, Usability, Viability, Feasibility risks). Prefer experiments with "skin-in-the-game" (Alberto Savoia) over opinion-based validation.

**Key principles:**

- **One outcome at a time.** Don't try to solve everything. Focus the tree on a single desired outcome.
- **Opportunities, not features.** "Never allow customers to design solutions. Prioritize opportunities (problems), not features."
- **Compare and contrast.** Always generate at least 3 solutions per opportunity before choosing. Avoid the "first idea" trap.
- **Discovery is not linear.** Loop back if experiments fail. Kill solutions that don't validate. Explore new branches.
- **Continuous, not periodic.** Update the tree weekly as you learn from interviews, analytics, and experiments.

### Instructions

You are helping a product team build an Opportunity Solution Tree for **$ARGUMENTS**.

### Input Requirements
- A desired outcome or business metric to improve
- Customer research data (interviews, surveys, analytics, feedback)
- Optionally: existing opportunities or solution ideas to organize

### Process

1. **Define the desired outcome** — Confirm or help articulate a single, measurable outcome at the top of the tree.

2. **Map opportunities** — From provided research, identify 3-7 customer opportunities (needs/pains). Group related opportunities. Frame each from the customer's perspective.

3. **Prioritize opportunities** — Use Opportunity Score or qualitative assessment to rank. Focus on the top 2-3.

4. **Generate solutions** — For each prioritized opportunity, brainstorm 3+ solutions from PM, Designer, and Engineer perspectives.

5. **Design experiments** — For the most promising solutions, suggest 1-2 fast experiments. Specify: hypothesis, method, metric, success threshold.

6. **Visualize the tree** — Present the full OST in a clear hierarchical format.

Think step by step. Save as markdown if substantial.

---

### Further Reading

- [The Extended Opportunity Solution Tree](https://www.productcompass.pm/p/the-extended-opportunity-solution-tree)
- [What Is Product Discovery? The Ultimate Guide Step-by-Step](https://www.productcompass.pm/p/what-exactly-is-product-discovery)
- [Product Trio: Beyond the Obvious](https://www.productcompass.pm/p/product-trio)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)
```

## File: `pm-product-discovery/skills/prioritize-assumptions/SKILL.md`
```markdown
---
name: prioritize-assumptions
description: "Prioritize assumptions using an Impact × Risk matrix and suggest experiments for each. Use when triaging a list of assumptions, deciding what to test first, or applying the assumption prioritization canvas."
---

## Prioritize Assumptions

Triage assumptions using an Impact × Risk matrix and suggest targeted experiments.

### Context

You are helping prioritize assumptions for **$ARGUMENTS**.

If the user provides files with assumptions or research data, read them first.

### Domain Context

**ICE** works well for assumption prioritization: Impact (Opportunity Score × # Customers) × Confidence (1–10) × Ease (1–10). Opportunity Score = Importance × (1 − Satisfaction), normalized to 0–1 (Dan Olsen). **RICE** splits Impact into Reach × Impact separately: (R × I × C) / E. See the `prioritization-frameworks` skill for full formulas and templates.

### Instructions

The user will provide a list of assumptions to prioritize. Apply the following framework:

1. **For each assumption**, evaluate two dimensions:
   - **Impact**: The value created by validating this assumption AND the number of customers affected (in ICE: Impact = Opportunity Score × # Customers)
   - **Risk**: Defined as (1 - Confidence) × Effort

2. **Categorize each assumption** using the Impact × Risk matrix:
   - **Low Impact, Low Risk** → Defer testing until higher-priority assumptions are addressed
   - **High Impact, Low Risk** → Proceed to implementation (low risk, high reward)
   - **Low Impact, High Risk** → Reject the idea (not worth the investment)
   - **High Impact, High Risk** → Design an experiment to test it

3. **For each assumption requiring testing**, suggest an experiment that:
   - Maximizes validated learning with minimal effort
   - Measures actual behavior, not opinions
   - Has a clear success metric and threshold

4. **Present results** as a prioritized matrix or table.

Think step by step. Save as markdown if the output is substantial.

---

### Further Reading

- [Assumption Prioritization Canvas: How to Identify And Test The Right Assumptions](https://www.productcompass.pm/p/assumption-prioritization-canvas)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)
```

## File: `pm-product-discovery/skills/prioritize-features/SKILL.md`
```markdown
---
name: prioritize-features
description: "Prioritize a backlog of feature ideas based on impact, effort, risk, and strategic alignment with top 5 recommendations. Use when prioritizing a feature backlog, making scope decisions, or ranking product ideas."
---

## Prioritize Feature Backlog

Evaluate and rank a backlog of feature ideas to identify the top 5 to pursue.

### Context

You are helping prioritize features for **$ARGUMENTS**.

If the user provides files (spreadsheets, backlogs, opportunity assessments), read and analyze them directly.

### Domain Context

For framework selection guidance, see the `prioritization-frameworks` skill. Key recommendations:

**Opportunity Score** (Dan Olsen, *The Lean Product Playbook*) is recommended for evaluating customer problems: Opportunity Score = Importance × (1 − Satisfaction), normalized to 0–1. High Importance + low Satisfaction = best opportunities. Prioritize **problems (opportunities)**, not solutions.

**ICE** is recommended for quick scoring of initiatives: Impact (Opportunity Score × # Customers) × Confidence × Ease. **RICE** adds Reach as a separate factor for larger teams.

### Instructions

The user will describe their product objective, desired outcomes, and provide feature ideas. Work through these steps:

1. **Understand priorities**: Confirm the product objective and success metrics.

2. **Evaluate each feature** against:
   - **Impact**: How much does it move the needle on desired outcomes? Consider Opportunity Score if customer data is available.
   - **Effort**: How much development, design, and coordination is required?
   - **Risk**: How much uncertainty exists? What assumptions need testing?
   - **Strategic alignment**: How well does it fit the product vision and current goals?

3. **Recommend the top 5 features** with:
   - Clear ranking (1-5)
   - Brief rationale for each selection
   - Key trade-offs considered
   - What was deprioritized and why

4. **Present as a prioritization table** if helpful.

Think step by step. Save as markdown if the output is substantial.

---

### Further Reading

- [Kano Model: How to Delight Your Customers Without Becoming a Feature Factory](https://www.productcompass.pm/p/kano-model-how-to-delight-your-customers)
- [The Product Management Frameworks Compendium + Templates](https://www.productcompass.pm/p/the-product-frameworks-compendium)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)
```

## File: `pm-product-discovery/skills/summarize-interview/SKILL.md`
```markdown
---
name: summarize-interview
description: "Summarize a customer interview transcript into a structured template with JTBD, satisfaction signals, and action items. Use when processing interview recordings or transcripts, synthesizing discovery interviews, or creating interview summaries."
---

## Summarize Customer Interview

Transform an interview transcript into a structured summary focused on Jobs to Be Done, satisfaction, and action items.

### Context

You are summarizing a customer interview for the product discovery of **$ARGUMENTS**.

The user will provide an interview transcript — either as an attached file (text, PDF, audio transcription) or pasted directly. Read any attached files first.

### Instructions

1. **Read the full transcript** carefully before summarizing.

2. **Fill in the summary template** below. Use "-" if information is unavailable. Replace numeric values with qualitative descriptions if needed (e.g., "not satisfied").

3. **Use clear, simple language** — a primary school graduate should be able to understand the summary.

### Output Template

```
**Date**: [Date and time of the interview]
**Participants**: [Full names and roles]
**Background**: [Background information about the customer]

**Current Solution**: [What solution they currently use]

**What They Like About Current Solution**:
- [Job to be done, desired outcome, importance, and satisfaction level]

**Problems With Current Solution**:
- [Job to be done, desired outcome, importance, and satisfaction level]

**Key Insights**:
- [Unexpected findings or notable quotes]

**Action Items**:
- [Date, Owner, Action — e.g., "2025-01-15, Paweł Huryn, Follow up with customer about pricing"]
```

Save the summary as a markdown document in the user's workspace.

---

### Further Reading

- [User Interviews: The Ultimate Guide to Research Interviews](https://www.productcompass.pm/p/interviewing-customers-the-ultimate)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)
```

## File: `pm-product-strategy/README.md`
```markdown
# pm-product-strategy

Product strategy skills for PMs: vision, strategy canvas, startup canvas, value propositions, lean canvas, business model canvas, SWOT, PESTLE, Ansoff Matrix, Porter's Five Forces, pricing, and monetization.

## Skills (12)

- **ansoff-matrix** — Generate an Ansoff Matrix analysis mapping growth strategies across market penetration, market development, product development, and diversification.
- **business-model** — Generate a Business Model Canvas with all 9 building blocks.
- **lean-canvas** — Generate a Lean Canvas business model with sections for problem, solution, metrics, cost structure, UVP, unfair advantage, channels, segments, and revenue.
- **monetization-strategy** — Brainstorm 3-5 monetization strategies with audience fit, risks, and validation experiments.
- **pestle-analysis** — Perform a PESTLE analysis covering Political, Economic, Social, Technological, Legal, and Environmental factors.
- **porters-five-forces** — Perform Porter's Five Forces analysis evaluating competitive rivalry, supplier power, buyer power, threat of substitutes, and threat of new entrants.
- **pricing-strategy** — Analyze and design pricing strategies including pricing models, competitive pricing analysis, willingness-to-pay estimation, and price elasticity considerations.
- **product-strategy** — Generate a comprehensive product strategy using the 9-section Product Strategy Canvas covering vision, segments, costs, value propositions, trade-offs, metrics, growth, capabilities, and defensibility.
- **product-vision** — Brainstorm an inspiring, achievable, and emotional product vision that motivates teams.
- **startup-canvas** — Generate a Startup Canvas combining Product Strategy (9 sections) and Business Model (Cost Structure + Revenue Streams) for a new product. An alternative to Business Model Canvas and Lean Canvas that separates strategy from business model.
- **swot-analysis** — Perform a detailed SWOT analysis identifying strengths, weaknesses, opportunities, and threats with actionable recommendations.
- **value-proposition** — Generate a detailed value proposition using a 6-part JTBD template (Who, Why, What before, How, What after, Alternatives).

## Commands (5)

- `/pm-product-strategy:business-model` — Explore business models using Lean Canvas, Business Model Canvas, Startup Canvas, or Value Proposition frameworks.
- `/pm-product-strategy:market-scan` — Comprehensive macro environment analysis — SWOT, PESTLE, Porter's Five Forces, and Ansoff Matrix in one scan.
- `/pm-product-strategy:pricing` — Design a pricing strategy — models, competitive analysis, willingness-to-pay estimation, and pricing experiments.
- `/pm-product-strategy:strategy` — Create a comprehensive product strategy using the 9-section Strategy Canvas — from vision to defensibility.
- `/pm-product-strategy:value-proposition` — Design a value proposition using the 6-part JTBD template — Who, Why, What before, How, What after, Alternatives.

## Author

Paweł Huryn — [The Product Compass Newsletter](https://www.productcompass.pm)

## License

MIT
```

## File: `pm-product-strategy/commands/business-model.md`
```markdown
---
description: Explore business models using Lean Canvas, Business Model Canvas, Startup Canvas, or Value Proposition frameworks
argument-hint: "[lean|full|startup|value-prop] <product or business>"
---

# /business-model -- Business Model Exploration

Build and analyze business models using four complementary frameworks. Choose one or run all for a complete picture.

## Invocation

```
/business-model lean Marketplace connecting freelance PMs with startups
/business-model full Enterprise analytics platform
/business-model startup AI writing tool for non-native English speakers
/business-model value-prop SaaS onboarding tool
/business-model all SaaS onboarding tool        # runs all four
/business-model                                   # asks what you need
```

## Modes

---

### Lean Canvas Mode

Best for: Early-stage ideas, startups, new product lines.

Apply the **lean-canvas** skill to produce a complete Lean Canvas:

```
## Lean Canvas: [Product]

| Problem (Top 3) | Solution | Unique Value Proposition |
|-----------------|----------|------------------------|
| 1. [problem]    | [solution to each] | [single clear message] |
| 2. [problem]    |          |                        |
| 3. [problem]    |          |                        |

| Key Metrics | Unfair Advantage |
|------------|-----------------|
| [what you measure] | [what can't be copied] |

| Channels | Customer Segments |
|---------|------------------|
| [how you reach them] | [who, early adopters first] |

| Cost Structure | Revenue Streams |
|---------------|----------------|
| [fixed + variable] | [how you make money] |

### Riskiest Assumptions
[What must be true for this to work — prioritized by risk]

### Experiments to Run
[How to validate the riskiest assumptions cheaply]
```

---

### Full Business Model Canvas Mode

Best for: Established products, strategic planning, investor materials.

Apply the **business-model** skill to produce all 9 building blocks:

```
## Business Model Canvas: [Product]

| Key Partners | Key Activities | Value Propositions | Customer Relationships | Customer Segments |
|-------------|---------------|-------------------|----------------------|------------------|
| [who helps you] | [core actions] | [why customers choose you] | [how you interact] | [who you serve] |

| Key Resources | | Channels | |
|-------------|---|---------|---|
| [what you need] | | [how you deliver] | |

| Cost Structure | Revenue Streams |
|---------------|----------------|
| [your costs] | [your revenue] |

### Analysis
[Strengths and weaknesses of this model]
[How the pieces reinforce each other]
[Vulnerabilities and dependencies]
```

---

### Startup Canvas Mode

Best for: New products and startups that need both strategy and business model in one artifact. Recommended over Lean Canvas and BMC for new products.

Apply the **startup-canvas** skill to produce a Startup Canvas with 9 strategy sections + business model:

```
## Startup Canvas: [Product]

### Part 1: Product Strategy

| Vision | Market Segments | Relative Costs |
|--------|----------------|---------------|
| [inspiring why] | [JTBD, first segment] | [low cost vs unique value] |

| Value Proposition | Trade-offs | Key Metrics |
|------------------|-----------|------------|
| [What before → How → What after → Alternatives] | [what you won't do] | [North Star + OMTM] |

| Growth | Capabilities | Can't/Won't |
|--------|-------------|------------|
| [PLG vs Sales-Led, channels] | [build vs partner] | [why competitors can't copy] |

### Part 2: Business Model

| Cost Structure | Revenue Streams |
|---------------|----------------|
| [fixed + variable, how they scale] | [pricing model, revenue per channel] |

### Strategy Coherence Check
[Do all elements reinforce each other?]

### Riskiest Assumptions
[What must be true — and how to test it]
```

---

### Value Proposition Mode

Best for: Refining messaging, understanding user value, product-market fit analysis.

Apply the **value-proposition** skill to produce a JTBD-framed value proposition:

```
## Value Proposition: [Product]

### For [Segment]:
1. **Who**: [target user profile]
2. **Why**: [the job they're trying to do]
3. **What Before**: [their current painful reality]
4. **How**: [your solution approach]
5. **What After**: [their improved reality]
6. **Alternatives**: [what they'd use without you, and why you're better]

### Value Proposition Statement
[One sentence: For [who] who [need], [product] is a [category] that [benefit]. Unlike [alternative], we [differentiator].]
```

---

### All Mode

Runs all four frameworks and adds a synthesis section comparing insights across frameworks.

## Workflow (All Modes)

### Step 1: Gather Context

Ask:
- What is the product or business idea?
- What stage? (idea, validated, scaling)
- Any existing business model to refine?
- Who is the target customer?

### Step 2: Generate the Selected Framework(s)

Apply the relevant skill(s) as described above.

### Step 3: Save and Iterate

Save as markdown. Offer:
- "Want me to **stress-test this model** with a SWOT or PESTLE analysis?"
- "Should I **design a pricing strategy** for the revenue streams?"
- "Want me to **build a strategy canvas** around this model?"
- "Should I **identify the beachhead segment**?"

## Notes

- **Startup Canvas** is the recommended starting point for new products — it separates strategy from business model and covers what BMC and Lean Canvas miss (vision, trade-offs, metrics, Can't/Won't)
- **Lean Canvas** is best for speed and hypothesis testing — don't overthink it, but be aware it mixes strategy and business model into one artifact
- **BMC** is better for mature businesses that need to articulate how everything connects, but lacks strategic sections (vision, trade-offs, metrics)
- **Value Proposition** is the sharpest tool for product-market fit conversations
- In "all" mode, highlight where frameworks agree (strong signal) and where they diverge (needs investigation)
```

## File: `pm-product-strategy/commands/market-scan.md`
```markdown
---
description: Comprehensive macro environment analysis — SWOT, PESTLE, Porter's Five Forces, and Ansoff Matrix in one scan
argument-hint: "<product, market, or industry>"
---

# /market-scan -- Macro Environment Analysis

Run multiple strategic analysis frameworks to understand your competitive and macro environment. Combines SWOT, PESTLE, Porter's Five Forces, and Ansoff Matrix into a single strategic overview.

## Invocation

```
/market-scan EdTech market for corporate learning
/market-scan [upload a market brief or strategy doc]
/market-scan Our fintech product — preparing for board strategy review
```

## Workflow

### Step 1: Understand the Context

Ask:
- What product, company, or market are you analyzing?
- What's the purpose? (strategic planning, market entry, investor prep, annual review)
- Any specific frameworks you want to focus on? Or run all four?
- What's your current position in this market?

### Step 2: Run the Analysis

Apply four skills in sequence, each building on insights from the previous:

**SWOT Analysis** (apply **swot-analysis** skill):
- Internal: Strengths and Weaknesses
- External: Opportunities and Threats
- Actionable recommendations for each quadrant

**PESTLE Analysis** (apply **pestle-analysis** skill):
- Political, Economic, Social, Technological, Legal, Environmental factors
- Impact assessment and timeline for each factor

**Porter's Five Forces** (apply **porters-five-forces** skill):
- Competitive rivalry, supplier power, buyer power, threat of substitutes, threat of new entrants
- Overall industry attractiveness rating

**Ansoff Matrix** (apply **ansoff-matrix** skill):
- Market penetration, market development, product development, diversification
- Risk-adjusted growth opportunities

### Step 3: Synthesize

Cross-reference findings across frameworks to identify:
- **Converging signals**: What multiple frameworks agree on
- **Strategic imperatives**: Actions that appear critical across analyses
- **Key risks**: Threats and forces to mitigate
- **Growth opportunities**: Where the best risk-adjusted opportunities lie

### Step 4: Generate Report

```
## Strategic Market Scan: [Market/Product]

**Date**: [today]
**Purpose**: [strategic planning / market entry / etc.]

### Executive Summary
[5-7 sentences covering the strategic situation and key recommendations]

### SWOT Analysis
| Strengths | Weaknesses |
|-----------|-----------|
| [internal positives] | [internal negatives] |

| Opportunities | Threats |
|-------------|---------|
| [external positives] | [external negatives] |

**SWOT Actions**: [leverage S+O, mitigate W+T]

### PESTLE Analysis
| Factor | Current State | Impact | Trend | Timeframe |
|--------|-------------|--------|-------|-----------|

### Porter's Five Forces
| Force | Intensity | Key Drivers | Implications |
|-------|----------|------------|-------------|

**Industry Attractiveness**: [High / Medium / Low]

### Ansoff Growth Matrix
| Strategy | Opportunity | Risk Level | Investment | Priority |
|----------|-----------|-----------|-----------|----------|
| Market Penetration | [specifics] | Low | [est.] | [H/M/L] |
| Market Development | [specifics] | Medium | [est.] | [H/M/L] |
| Product Development | [specifics] | Medium | [est.] | [H/M/L] |
| Diversification | [specifics] | High | [est.] | [H/M/L] |

### Cross-Framework Synthesis
**Converging signals**: [what all frameworks agree on]
**Strategic imperatives**: [must-do actions]
**Key risks**: [highest-priority threats]
**Best opportunities**: [risk-adjusted growth plays]

### Strategic Recommendations
1. [Recommendation with supporting evidence from multiple frameworks]
2. ...
3. ...

### Monitoring Plan
| Signal | What to Watch | Source | Check Frequency |
|--------|-------------|--------|----------------|
```

Save as markdown.

### Step 5: Offer Next Steps

- "Want me to **build a product strategy** based on these findings?"
- "Should I **analyze specific competitors** identified in Porter's analysis?"
- "Want me to **design a pricing strategy** for the market penetration opportunity?"

## Notes

- Use web research to ground the analysis in current market data, not just general knowledge
- PESTLE factors should include specific regulations, market data, and trend signals — not generic observations
- Porter's is most useful when you identify the *specific* forces, not just rate them abstractly
- Ansoff should include concrete opportunities, not just generic "enter new markets"
- The synthesis section is the most valuable part — it's where the frameworks talk to each other
```

## File: `pm-product-strategy/commands/pricing.md`
```markdown
---
description: Design a pricing strategy — models, competitive analysis, willingness-to-pay estimation, and pricing experiments
argument-hint: "<product or pricing question>"
---

# /pricing -- Pricing Strategy Design

Build a pricing strategy from first principles: analyze pricing models, estimate willingness to pay, benchmark against competitors, and design pricing experiments.

## Invocation

```
/pricing SaaS project management tool moving from free to paid
/pricing Should we switch from per-seat to usage-based pricing?
/pricing [upload competitor pricing pages or current pricing data]
```

## Workflow

### Step 1: Understand the Pricing Context

Ask:
- What is the product? What value does it deliver?
- Current pricing (if any): model, price points, packaging
- What's the trigger? (new product, pricing change, competitive pressure, growth stall)
- Target customer profile and their budget context
- Any constraints? (contractual obligations, market expectations, competitive positioning)

### Step 2: Analyze Pricing Models

Apply the **pricing-strategy** and **monetization-strategy** skills:

Evaluate applicable models:
- **Flat-rate**: Simple, predictable — best for commoditized products
- **Per-seat/user**: Scales with adoption — best for collaboration tools
- **Usage-based**: Aligns cost with value — best for infrastructure and API products
- **Tiered**: Captures different willingness to pay — best for segmented markets
- **Freemium**: Drives adoption — best for products with network effects
- **Hybrid**: Combines models — best for complex products with multiple value levers

For each relevant model: pros, cons, fit for your product, revenue projection approach.

### Step 3: Competitive Pricing Analysis

Using web research:
- Benchmark pricing against 3-5 competitors
- Identify pricing model patterns in the category
- Note pricing trends (e.g., shift from per-seat to usage-based in B2B SaaS)
- Find pricing page screenshots and data points

### Step 4: Willingness to Pay Estimation

If the user has survey data or customer feedback:
- Apply Van Westendorp analysis (if data available)
- Segment willingness to pay by user type

If no data:
- Estimate based on value delivered, competitive anchoring, and market norms
- Design a willingness-to-pay survey the user can run

### Step 5: Generate Pricing Recommendation

```
## Pricing Strategy: [Product]

**Date**: [today]
**Current pricing**: [if applicable]

### Recommended Model: [Model Name]

**Why this model**: [rationale tied to product value delivery]

### Pricing Structure
| Tier | Price | Includes | Target Segment | Key Limit |
|------|-------|---------|---------------|-----------|

### Free / Trial Strategy
[What's free, what's gated, conversion triggers]

### Competitive Benchmark
| Competitor | Model | Price Range | Positioning |
|-----------|-------|-----------|------------|

### Revenue Projections
| Scenario | Assumptions | Year 1 ARR | Year 2 ARR |
|----------|-----------|-----------|-----------|
| Conservative | [X] | [Y] | [Z] |
| Expected | [X] | [Y] | [Z] |
| Optimistic | [X] | [Y] | [Z] |

### Migration Plan
[If changing pricing: how to transition existing customers]
- Grandfathering approach
- Communication plan
- Timeline

### Pricing Experiments
| Experiment | What We're Testing | Method | Duration |
|-----------|-------------------|--------|----------|

### Risks and Mitigations
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|

### Key Metrics to Track
- Conversion rate by tier
- Average revenue per user (ARPU)
- Upgrade/downgrade rates
- Churn by price sensitivity
- Price elasticity signals
```

Save as markdown.

### Step 6: Offer Next Steps

- "Want me to **create a monetization strategy** with alternative revenue models?"
- "Should I **run a market scan** to validate pricing assumptions?"
- "Want me to **draft customer communication** for the pricing change?"
- "Should I **design the A/B test** for pricing experiments?"

## Notes

- Pricing is the most powerful lever for revenue growth — a 1% improvement in pricing typically has 3-4x the impact of 1% improvement in customer acquisition
- Value-based pricing always beats cost-plus — start from customer value, not your costs
- The best pricing is simple to understand and predictable for the customer
- Freemium only works if free users generate value (network effects, word of mouth, marketplace liquidity)
- Always design a migration path for existing customers — pricing changes that alienate your base destroy trust
```

## File: `pm-product-strategy/commands/strategy.md`
```markdown
---
description: Create a comprehensive product strategy using the 9-section Strategy Canvas — from vision to defensibility
argument-hint: "<product or company>"
---

# /strategy -- Product Strategy Canvas

Build a complete product strategy document using the 9-section Product Strategy Canvas. Covers vision, segments, value propositions, trade-offs, metrics, growth, capabilities, and defensibility.

## Invocation

```
/strategy AI-powered design tool for non-designers
/strategy [upload existing strategy doc, pitch deck, or business plan]
/strategy                    # asks about your product
```

## Workflow

### Step 1: Understand the Product

Accept context from:
- Product description (verbal or written)
- Uploaded documents (strategy decks, pitch decks, PRDs, business plans)
- Existing strategy to refine or challenge

Ask key questions:
- What does the product do? Who is it for?
- What stage is it in? (idea, MVP, growth, mature)
- What's the business model?
- What triggered the need for a strategy document? (new product, pivot, annual planning, fundraise)

### Step 2: Build the Strategy Canvas

Apply the **product-strategy** and **product-vision** skills:

Work through all 9 sections of the Strategy Canvas:

1. **Vision**: Inspiring north star that motivates the team
2. **Target Segments**: Who you serve (and who you don't)
3. **Pain Points & Value**: Problems you solve and the value you create
4. **Value Propositions**: JTBD-framed value for each segment
5. **Strategic Trade-offs**: What you choose NOT to do (as important as what you do)
6. **Key Metrics**: How you measure success
7. **Growth Engine**: How you acquire and expand users
8. **Core Capabilities**: What you need to build and maintain
9. **Defensibility**: What makes this hard to copy (network effects, data, brand, switching costs)

For each section, provide specific content — not generic advice.

### Step 3: Generate Strategy Document

```
## Product Strategy: [Product Name]

**Date**: [today]
**Stage**: [idea / MVP / growth / mature]
**Author**: [user]

### 1. Vision
[Inspiring, achievable, emotional — 2-3 sentences max]

### 2. Target Segments
| Segment | Size | Pain Level | Current Alternative | Priority |
|---------|------|-----------|-------------------|----------|

**Primary segment**: [who and why]
**Explicitly not serving**: [who and why]

### 3. Pain Points & Value Created
[For each segment: the problem, current cost, and value your solution delivers]

### 4. Value Propositions
**For [Segment A]**: When [situation], they want [motivation], so they can [outcome]
**For [Segment B]**: When [situation], they want [motivation], so they can [outcome]

### 5. Strategic Trade-offs
| We Choose | Over | Because |
|-----------|------|---------|

### 6. Key Metrics
- **North Star**: [metric]
- **Input Metrics**: [3-5 levers]
- **Health Metrics**: [guardrails]

### 7. Growth Engine
[How you acquire, activate, and expand — specific mechanisms, not generic]

### 8. Core Capabilities
| Capability | Build / Buy / Partner | Investment Level | Timeline |
|-----------|---------------------|-----------------|----------|

### 9. Defensibility
[What creates a moat — be specific about which type: network effects, data, brand, switching costs, economies of scale]

### Strategic Risks
[Top 3 things that could invalidate this strategy]

### Next Steps
[What to do with this strategy — socialize, test, build]
```

Save as markdown.

### Step 4: Offer Next Steps

- "Want me to **build a Lean Canvas** or **Business Model Canvas** for this?"
- "Should I **create a roadmap** aligned to this strategy?"
- "Want me to **run a macro environment scan** to stress-test assumptions?"
- "Should I **define OKRs** based on Section 6?"

## Notes

- A good strategy is more about what you say NO to than what you say YES to — push hard on trade-offs
- Vision should be emotional and memorable, not a corporate statement
- Defensibility is the hardest section — most products don't have a real moat yet, and that's OK to acknowledge
- If the product is early-stage, some sections will be hypotheses — label them as such
- Strategy should fit on one page for executives — offer a condensed version
```

## File: `pm-product-strategy/commands/value-proposition.md`
```markdown
---
description: Design a value proposition using the 6-part JTBD template — Who, Why, What before, How, What after, Alternatives
argument-hint: "<product or feature>"
---

# /value-proposition -- Value Proposition Design

Design a clear, compelling value proposition for a product or feature using the 6-part JTBD template. An alternative to Strategyzer's Value Proposition Canvas that starts with the customer and focuses on practical outcomes.

## Invocation

```
/value-proposition AI writing tool for non-native English speakers
/value-proposition [upload pitch deck, PRD, or competitive analysis]
/value-proposition                    # asks about your product
```

## Workflow

### Step 1: Understand the Product and Market

Accept context from:
- Product description (verbal or written)
- Uploaded documents (pitch decks, PRDs, competitive analyses)
- Existing value propositions to refine

Ask key questions:
- What does the product do? Who is it for?
- What alternatives or workarounds exist today?
- What customer insights or research do you have?

### Step 2: Build the Value Proposition

Apply the **value-proposition** skill to produce the 6-part template:

```
## Value Proposition: [Product]

### For [Segment]:

1. **Who**: [target user profile and characteristics]
2. **Why**: [the job they're trying to do, desired outcomes]
3. **What Before**: [their current painful reality — existing tools, friction, workarounds]
4. **How**: [your solution — specific features and capabilities that deliver value]
5. **What After**: [the improved outcome — what becomes possible]
6. **Alternatives**: [what they'd use without you, and why you're better]

### Value Proposition Statement
[One sentence: For [who] who [need], [product] is a [category] that [benefit]. Unlike [alternative], we [differentiator].]

### Value Proposition Statements (Reusable)
- Marketing: [...]
- Sales: [...]
- Onboarding: [...]
```

If the user has multiple segments, create a separate value proposition for each.

### Step 3: Save and Offer Next Steps

Save as markdown. Offer:
- "Want me to **compare this against competitors** with a Value Curve?"
- "Should I **build a full strategy** around this value proposition?"
- "Want me to **create a Lean Canvas** or **Startup Canvas** using this?"
- "Should I **generate marketing messaging** from these value prop statements?"

## Notes

- This template starts with the customer (Who/Why) and works toward the solution — unlike Strategyzer's canvas which places the product on the left
- Each value proposition is segment-specific — different segments get different value props
- Use a Value Curve (Blue Ocean Strategy) to visually compare your offering against competitors across key factors
- Value Proposition is one element of product strategy — use `/strategy` for the full picture
```

## File: `pm-product-strategy/skills/ansoff-matrix/SKILL.md`
```markdown
---
name: ansoff-matrix
description: "Generate an Ansoff Matrix analysis mapping growth strategies across market penetration, market development, product development, and diversification. Use when considering growth options, planning market expansion, or evaluating strategic growth paths."
---
# Ansoff Matrix

## Metadata
- **Name**: ansoff-matrix
- **Description**: Generate an Ansoff Matrix analysis mapping growth strategies across market penetration, market development, product development, and diversification.
- **Triggers**: Ansoff matrix, growth matrix, market expansion, growth strategy options

## Instructions

You are a growth strategist analyzing expansion opportunities using the Ansoff Matrix for $ARGUMENTS.

Your task is to evaluate growth options across product and market dimensions and develop specific strategies for each quadrant.

## Input Requirements
- Current product(s) and market definition
- Current market penetration and performance
- Customer insights and market opportunities
- Company capabilities and constraints
- Growth targets and timelines
- Competitive dynamics

## Ansoff Matrix Framework

### 2x2 Matrix: Products vs. Markets

|  | Current Market | New Market |
|---|---|---|
| **Current Product** | Market Penetration | Market Development |
| **New Product** | Product Development | Diversification |

---

### 1. Market Penetration (Current Product + Current Market)
Grow revenue by increasing usage or sales in your existing market.

**Strategies:**
- Increase frequency of product usage
- Expand use cases within existing customer base
- Acquire competitors' customers
- Reduce churn and improve retention
- Upsell and cross-sell existing customers
- Lower prices to capture price-sensitive segments
- Increase marketing and brand awareness
- Improve customer experience to drive referrals

**Examples:**
- Netflix adding games to increase engagement
- Starbucks encouraging multiple visits per week
- Adobe expanding Adobe Creative Cloud subscriptions

**Risk Level:** Low (familiar market, product, capabilities)

**Typical Timeline:** 6-12 months

---

### 2. Market Development (Current Product + New Market)
Grow by selling your existing product to new customer segments or geographies.

**Strategies:**
- Expand into new geographies or regions
- Target new customer segments or personas
- Sell through new channels or partnerships
- Adapt product for new use cases
- Partner with complementary companies
- Localize product for new markets
- Build brand awareness in new markets

**Examples:**
- Facebook expanding internationally
- Uber moving into new cities and countries
- Slack selling to non-tech industries

**Risk Level:** Medium (new market dynamics, but proven product)

**Typical Timeline:** 12-24 months

---

### 3. Product Development (New Product + Current Market)
Grow by introducing new products or features to your existing customer base.

**Strategies:**
- Add new features to existing product
- Create adjacent product lines
- Bundle products for greater value
- Develop premium/lite versions
- Integrate adjacent capabilities
- Create complementary products
- Upgrade product experience or performance

**Examples:**
- Spotify adding podcasts
- Amazon Prime expanding services (video, music, grocery)
- Figma adding prototyping and FigJam

**Risk Level:** Medium (existing customers but new product)

**Typical Timeline:** 12-18 months

---

### 4. Diversification (New Product + New Market)
Grow by entering entirely new markets with new products.

**Strategies:**
- Related diversification: leveraging existing competencies
- Unrelated diversification: entering new domains
- Acquire companies in new markets/products
- Strategic partnerships or joint ventures
- Build new business units
- Apply capabilities to adjacent problems

**Examples:**
- Amazon expanding from books to cloud services (AWS)
- Apple expanding from computers to phones, wearables, services
- Microsoft moving from software to cloud (Azure) and gaming (Xbox)

**Risk Level:** High (new market, new product, new capabilities)

**Typical Timeline:** 24+ months, requires significant investment

---

## Output Process
1. Define current market and product clearly
2. Analyze each quadrant:
   - Identify 2-3 specific opportunities per quadrant
   - Assess market size and growth potential
   - Estimate required resources and investment
   - Evaluate competitive dynamics
   - Define success metrics
3. Prioritize opportunities by:
   - Strategic fit with company vision
   - Revenue potential and growth rate
   - Resource requirements and feasibility
   - Competitive advantage and defensibility
   - Timeline to profitability
4. Develop go-to-market strategy for top 2-3 opportunities
5. Create phased roadmap and milestones
6. Identify risks and mitigation plans
7. Define success metrics and leading indicators

## Strategic Questions
- Which quadrant offers the best risk-reward profile?
- Where do our capabilities give us competitive advantage?
- Which opportunities align best with our vision and values?
- What partnerships or acquisitions would accelerate growth?
- How does each option impact our brand and positioning?

## Notes
- Market penetration is lowest risk; diversification is highest risk
- Most companies should excel in one quadrant before expanding
- Avoid spreading too thin across all four quadrants simultaneously
- Consider sequential strategy: penetration first, then market development
- Reassess Ansoff Matrix annually or when market conditions shift

---

### Further Reading

- [The Product Management Frameworks Compendium + Templates](https://www.productcompass.pm/p/the-product-frameworks-compendium)
```

## File: `pm-product-strategy/skills/business-model/SKILL.md`
```markdown
---
name: business-model
description: "Generate a Business Model Canvas with all 9 building blocks. Use when creating a business model, documenting how a business creates value, or analyzing an existing business model."
---
# Business Model Canvas

## Metadata
- **Name**: business-model
- **Description**: Generate a Business Model Canvas with all 9 building blocks. Use when creating a business model, documenting how a business creates value, or analyzing an existing business model.
- **Triggers**: business model canvas, BMC, business model, how we make money

## Instructions

You are a business model strategist designing a Business Model Canvas for $ARGUMENTS.

Your task is to create a comprehensive Business Model Canvas that outlines how the business creates, delivers, and captures value.

## Input Requirements
- Product or service description
- Target customer(s) and market
- Current business operations or assumptions
- Competitive context or industry dynamics

## Business Model Canvas Template

### Left Side: Creating Value

**1. Key Partners**
- Who are the key strategic partners and suppliers?
- What partnerships enable our business model?
- Which activities do partners handle?
- Are there joint ventures or co-creation opportunities?

**2. Key Activities**
- What key activities does the business perform?
- What processes are critical to delivering value?
- Are these activities in-house or outsourced?
- Production, problem-solving, platform/network activities?

**3. Key Resources**
- What resources are necessary to create value?
- Physical assets, intellectual property, human capital, financial
- What resources enable key activities and partnerships?
- What's the minimum viable resource set?

### Center: The Value Proposition

**4. Value Propositions**
- What value do we deliver to customers?
- Which customer problems do we solve?
- What needs are satisfied?
- What products/services address each segment?
- Quantitative (price, speed, quality) vs. qualitative (design, status)

### Right Side: Delivering Value

**5. Customer Relationships**
- How do we establish and maintain customer relationships?
- Personal assistance, self-service, automated, community, co-creation
- Cost of customer acquisition and retention
- How do we keep customers engaged?

**6. Channels**
- How do customers discover and access the value?
- Awareness: How do customers learn about us?
- Purchase: How do they buy?
- Delivery: How is value delivered?
- After-sales: How do we support customers?
- Direct vs. indirect, owned vs. partner channels

**7. Customer Segments**
- Who are the key customer segments?
- Mass market, niche market, segmented, multi-sided platform
- What are their defining characteristics?
- Distinct needs, channels, relationships, or profitability

### Bottom: Financial Viability

**8. Cost Structure**
- What are the most important costs?
- Fixed vs. variable costs
- Cost drivers (scale, automation, labor, infrastructure)
- Is this a cost-driven or value-driven business?

**9. Revenue Streams**
- How does the business make money?
- Per customer, per transaction, subscription, licensing, rents
- Pricing mechanisms (fixed, dynamic, value-based)
- Customer lifetime value and unit economics

## Output Process
1. Identify and profile customer segments
2. Define the core value proposition(s)
3. Map customer relationships and channels
4. List key activities and resources
5. Identify key partners
6. Outline cost structure
7. Define revenue streams
8. Ensure all 9 blocks align and support each other
9. Test economic viability (LTV > 3x CAC)
10. Identify key assumptions and risks

### Domain Context

**Business Model Canvas vs Lean Canvas vs Startup Canvas**:

Business Model Canvas (Strategyzer, Alexander Osterwalder) is the most widely used canvas framework. It provides a balanced, holistic view of how value flows through the organization. However, it has known limitations for product strategy:

- **No vision**: Why should your team wake up every day? BMC doesn't address motivation or aspiration.
- **No Can't/Won't test**: What stops competitors from copying you? BMC lacks a defensibility section that goes beyond listing resources.
- **No trade-offs**: What you choose NOT to do creates focus and amplifies value — BMC doesn't address this.
- **No key metrics**: How do you know the strategy is working? BMC has no metrics section.
- **Low-value sections for startups**: Key Partnerships and Key Resources are rarely useful for early-stage products.

**When to use BMC**: Established businesses, corporate strategy, investor materials where you need to articulate how all operational pieces connect.

**Alternatives**:
- **Lean Canvas** (Ash Maurya): Startup-focused, faster, replaces Partners/Activities/Resources with Problem/Solution/Unfair Advantage. Better for hypothesis testing but still mixes strategy and business model.
- **Startup Canvas** (Paweł Huryn): Separates strategy (9 sections from the Product Strategy Canvas) from business model (Cost Structure + Revenue Streams). Recommended for new products where you need strategic clarity alongside the business model.

## Notes
- The Business Model Canvas provides a holistic view of how value flows through the organization
- Each block should reinforce and support the others
- Strong business models have clear, defensible value propositions
- Financial sustainability requires revenue to exceed costs at scale
- Use this to identify opportunities for innovation and optimization

---

### Further Reading

- [Business Model Canvas Examples: Google Maps, Airbnb, Uber](https://www.productcompass.pm/p/business-model-canvas-examples)
- [Startup Canvas: Product Strategy and a Business Model for a New Product](https://www.productcompass.pm/p/startup-canvas)
```

## File: `pm-product-strategy/skills/lean-canvas/SKILL.md`
```markdown
---
name: lean-canvas
description: "Generate a Lean Canvas with problem, solution, metrics, cost structure, UVP, unfair advantage, channels, segments, and revenue. Use when exploring a lean startup canvas, testing a business hypothesis, or modeling a new venture."
---
# Lean Canvas

## Metadata
- **Name**: lean-canvas
- **Description**: Generate a Lean Canvas business model with detailed sections for problem, solution, metrics, cost structure, UVP, unfair advantage, channels, segments, and revenue.
- **Triggers**: lean canvas, startup canvas, lean model, business hypothesis

## Instructions

You are a business model strategist designing a Lean Canvas for $ARGUMENTS.

Your task is to create a comprehensive Lean Canvas that outlines the business hypothesis and key business model assumptions for the product.

## Input Requirements
- Product or feature description
- Target customer segment(s)
- Market context and problem space
- Any available metrics or business constraints

## Lean Canvas Template

### Section 1: Product Definition

**1. Problem**
- Top 3 customer problems or needs
- Customer pains and frustrations
- Current unsatisfactory solutions

**2. Solution**
- Top 3 features or approaches
- How each feature addresses the problem
- Why this solution is novel or better

**3. Unique Value Proposition (UVP)**
- Concise, memorable statement
- Why customers choose you over alternatives
- What makes you different (not just "better")

**4. Unfair Advantage**
- What defensibility exists?
- Barriers to competition (network effects, brand, IP, switching costs)
- What competitors can't easily replicate

### Section 2: Market & Traction

**5. Customer Segments**
- Who is the target customer?
- Early adopters and first segment
- Customer personas or archetypes
- How large is the addressable market?

**6. Channels**
- How do you reach customers?
- Primary acquisition channels
- Distribution and sales approach
- How do customers find you?

**7. Revenue Streams**
- How do you make money?
- Pricing model or revenue per customer
- Customer lifetime value (LTV)
- Revenue growth assumptions

### Section 3: Economics & Validation

**8. Cost Structure**
- Fixed costs (salaries, infrastructure, facilities)
- Variable costs (COGS, transaction costs, support)
- Key cost drivers
- Cost per customer acquisition (CAC)

**9. Key Metrics**
- Activation: How do users get value quickly?
- Retention: How many users stick around?
- Revenue: How do we measure financial success?
- North Star metric for the business

## Output Process
1. Define the core problem(s) being solved
2. Outline 2-3 solution approaches
3. Craft a compelling UVP
4. Identify what creates competitive advantage
5. Target 1-2 customer segments
6. Map acquisition channels
7. Define revenue model and pricing
8. Estimate cost structure
9. Identify 3-5 critical metrics to track
10. Surface key assumptions and hypotheses
11. Suggest validation experiments (landing page, interviews, MVP)

### Domain Context

**Lean Canvas vs Business Model Canvas vs Startup Canvas**:

Lean Canvas (Ash Maurya) is a startup-focused adaptation of the Business Model Canvas that replaces Partners/Activities/Resources with Problem/Solution/Unfair Advantage. It's fast and hypothesis-driven, but has known limitations:

- **Redundancy**: "Problem" overlaps with Market Segments (markets are defined by problems/JTBD), and "Solution" overlaps with Value Proposition (which by definition includes features). This can create confusion about what goes where.
- **Missing strategic sections**: No vision (why should your team wake up every day?), no trade-offs (what you choose NOT to do), no relative costs (low cost vs unique value positioning), no key metrics.
- **Narrow defensibility**: "Unfair Advantage" focuses on one defensive element, but strong strategy is hard to copy as an integrated whole — not because of a single advantage.
- **No coherence check**: Doesn't address whether all strategic choices reinforce each other.

**When to use Lean Canvas**: Quick hypothesis testing when you need speed over completeness. Best as a brainstorming tool, not a strategy document.

**Consider instead**: **Startup Canvas** (Paweł Huryn) separates strategy (9 sections from the Product Strategy Canvas) from business model (Cost Structure + Revenue Streams). Recommended when you need both strategic clarity AND a business model for a new product.

## Notes
- The Lean Canvas is designed for rapid hypothesis testing
- Focus on addressing the riskiest assumptions first
- Update the canvas as you learn and validate
- Each section should be specific and measurable where possible
- This canvas helps align founding teams on business strategy

---

### Further Reading

- [Startup Canvas: Product Strategy and a Business Model for a New Product](https://www.productcompass.pm/p/startup-canvas)
```

## File: `pm-product-strategy/skills/monetization-strategy/SKILL.md`
```markdown
---
name: monetization-strategy
description: "Brainstorm 3-5 monetization strategies with audience fit, risks, and validation experiments. Use when exploring revenue models, evaluating pricing strategies, or deciding how to monetize a product."
---
# Monetization Strategy

## Metadata
- **Name**: monetization-strategy
- **Description**: Brainstorm 3-5 monetization strategies with audience fit, risks, and validation experiments. Use when exploring revenue models, pricing strategies, or business model options.
- **Triggers**: monetization strategy, revenue model, pricing strategy, how to monetize, make money

## Instructions

You are an experienced business model strategist brainstorming monetization strategies for $ARGUMENTS.

Your task is to develop 3-5 distinct monetization approaches that could work for the product or feature, evaluate fit with the target market, and outline low-effort validation experiments.

## Input Requirements
- Product or feature description
- Target market segment(s) and customer profile
- Current willingness to pay or budget constraints
- Competitive monetization approaches
- Company priorities (revenue growth, user growth, profitability)

## Monetization Framework

For each strategy, include:

### 1. Strategy Name & Description
- What is the monetization model?
- How does it work for this product?
- Who pays and what do they get?

### 2. How It Works
- Revenue model and pricing mechanics
- Value exchange between company and customer
- Payment frequency and transaction size
- Lifecycle and retention mechanisms

### 3. Audience Fit
- Why does this resonate with your target customer?
- How does it align with customer needs and preferences?
- What problems does it solve for the customer?
- Addressable market size and revenue potential

### 4. Unit Economics
- Estimated customer acquisition cost (CAC)
- Estimated customer lifetime value (LTV)
- Break-even timeline
- Target gross margin

### 5. Risks & Challenges
- Market adoption risk
- Pricing or feature sensitivity
- Competitive vulnerability
- Customer churn or resistance
- Implementation complexity

### 6. Competitive Position
- How do competitors monetize?
- What makes your approach differentiated?
- Barriers to customer switching
- Defense against competitive pricing

### 7. Validation Experiment
- Low-cost test to validate customer willingness to pay
- Method: survey, landing page, pilot, freemium, waitlist
- Success metric and decision criteria
- Timeline and resources required

## Example Monetization Strategies

### 1. Freemium (Free Base + Paid Premium)
- **How**: Free core features, premium advanced features behind paywall
- **Fit**: Best for high-volume, low-touch products (design tools, productivity, communication)
- **Risks**: Low conversion rates (typically 1-5%), features must be clear to justify upgrade
- **Experiment**: Launch freemium version, track conversion rate, gather upgrade feedback

### 2. Subscription (Recurring Monthly/Annual)
- **How**: Recurring charge for ongoing access and updates
- **Fit**: Best for products with continuous value (software, platforms, services)
- **Risks**: Customer churn, cannibalization from annual vs. monthly
- **Experiment**: Offer subscription to beta customers, measure churn rate and NPS

### 3. Usage-Based (Pay Per Use)
- **How**: Customers pay based on usage volume (API calls, storage, transactions)
- **Fit**: Best for B2B platforms, APIs, services with variable customer needs
- **Risks**: Unpredictable revenue, customer cost anxiety, usage optimization by customers
- **Experiment**: Implement usage tracking, pilot with 5-10 beta customers, model revenue

### 4. Enterprise/Seat-Based (Per User/Seat)
- **How**: Price per user, department, or seat using the product
- **Fit**: Best for B2B SaaS with team/organization adoption
- **Risks**: Sales complexity, contract length, implementation overhead
- **Experiment**: Conduct 5-10 customer interviews, validate pricing per seat, define support model

### 5. One-Time Purchase (Buy Once)
- **How**: Single upfront purchase for permanent or one-time license
- **Fit**: Best for niche products, tools, or templates (not ongoing services)
- **Risks**: Revenue concentration in launch period, no recurring revenue, updates/support questions
- **Experiment**: Launch limited offering, track conversion and customer satisfaction

### 6. Marketplace/Transaction Fee
- **How**: Take a percentage or fixed fee from transactions between buyers and sellers
- **Fit**: Best for platforms connecting supply and demand
- **Risks**: Market liquidity chicken-and-egg problem, trust and safety, competitive pressure
- **Experiment**: MVP with limited sellers, offer free period to drive initial supply, model unit economics

### 7. Advertising/Sponsorship
- **How**: Generate revenue from ads, sponsored content, or brand partnerships
- **Fit**: Best for high-traffic, consumer-facing products
- **Risks**: Brand damage from intrusive ads, user experience degradation, advertiser concentration
- **Experiment**: Test ads with small user segment, measure engagement and revenue impact

## Output Process
1. Brainstorm 3-5 distinct monetization strategies (avoid repeating similar models)
2. For each strategy:
   - Describe how it works specifically for this product
   - Assess fit with target customer and willingness to pay
   - Outline key risks and challenges
   - Estimate unit economics (CAC, LTV, timeline)
   - Compare against competitive approaches
3. For each strategy, design a low-effort validation experiment
4. Prioritize by:
   - Strategic fit (revenue, growth, profitability goals)
   - Ease of implementation
   - Market validation potential
   - Competitive advantage
5. Recommend 1-2 strategies to test first
6. Create testing roadmap and success criteria

## Strategic Considerations
- **Revenue Goals**: How much revenue is needed? By when?
- **Growth Goals**: Does monetization need to support user growth?
- **Market Dynamics**: Are customers ready to pay? For what?
- **Competitive Pressure**: How will competitors respond?
- **Unit Economics**: What gross margin is required for viability?

## Notes
- Best monetization strategies align with customer value and willingness to pay
- Test early and often; don't wait for perfect product to validate pricing
- Most products use hybrid models (e.g., freemium + upgrade, subscription + marketplace fees)
- Pricing can be changed; customer relationships are harder to rebuild
- Monitor competitors but don't race to the bottom on price

---

### Further Reading

- [Product Pricing Strategies 101](https://www.productcompass.pm/p/product-pricing-strategies-101)
```

## File: `pm-product-strategy/skills/pestle-analysis/SKILL.md`
```markdown
---
name: pestle-analysis
description: "Perform a PESTLE analysis covering Political, Economic, Social, Technological, Legal, and Environmental factors. Use when assessing the macro environment, doing strategic planning, or evaluating external factors affecting your business."
---
# PESTLE Analysis

## Metadata
- **Name**: pestle-analysis
- **Description**: Perform a PESTLE analysis covering Political, Economic, Social, Technological, Legal, and Environmental factors. Use when assessing macro-environment, evaluating market entry risks, or doing strategic planning.
- **Triggers**: PESTLE analysis, macro environment, market environment, external factors analysis

## Instructions

You are a strategic analyst conducting a PESTLE analysis for $ARGUMENTS.

Your task is to evaluate the macro-environmental factors that could impact product strategy, market entry, or business viability.

## Input Requirements
- Industry and market context
- Geographic market or region(s)
- Product or business type
- Current strategic challenges or questions
- Any known regulatory or market changes

## PESTLE Analysis Framework

### 1. Political
What government policies, regulations, and political stability affect the business?

- Government policies and incentives
- Tax regulations and tariffs
- Political stability and risk
- Government spending and subsidies
- Trade agreements and regulations
- Licensing and permits required
- Government relationships and lobbying needs

### 2. Economic
What economic conditions and financial factors matter?

- Economic growth and GDP trends
- Interest rates and inflation
- Currency exchange rates
- Consumer spending and confidence
- Employment and labor costs
- Disposable income trends
- Access to financing and capital

### 3. Social
What demographic and cultural trends shape the market?

- Population demographics and trends
- Cultural attitudes and values
- Consumer lifestyle and behaviors
- Education and skills availability
- Health and wellness trends
- Social media and digital adoption
- Diversity and inclusion preferences

### 4. Technological
What technological advances or disruptions are relevant?

- Emerging technologies (AI, blockchain, cloud, etc.)
- Digital transformation trends
- Cybersecurity and data privacy requirements
- Automation and robotics
- Internet of Things (IoT) and connectivity
- Research and development capabilities
- Technology adoption rates and digital literacy

### 5. Legal
What laws, regulations, and compliance requirements apply?

- Data protection and privacy laws (GDPR, CCPA, etc.)
- Employment and labor laws
- Intellectual property and patent laws
- Consumer protection laws
- Industry-specific regulations
- Compliance costs and audit requirements
- Liability and insurance requirements

### 6. Environmental
What environmental, climate, and sustainability factors exist?

- Climate change and environmental regulations
- Carbon emissions and sustainability requirements
- Natural resource availability and scarcity
- Waste management and circular economy trends
- Renewable energy adoption
- ESG (Environmental, Social, Governance) expectations
- Green certification and eco-friendly standards

## Output Process
1. For each PESTLE category, identify 3-5 relevant factors
2. Assess impact on product/business (High, Medium, Low)
3. Assess probability or likelihood (High, Medium, Low)
4. Prioritize factors by impact x probability
5. Develop strategic responses:
   - Which factors are opportunities to leverage?
   - Which factors are threats to mitigate or avoid?
   - Which factors require compliance or adaptation?
6. Identify key metrics or leading indicators to monitor
7. Build contingency plans for high-impact factors
8. Document assumptions and unknowns requiring research

## Strategic Applications
- Market entry assessment: Is this market viable to enter?
- Risk assessment: What macro risks could derail our strategy?
- Opportunity identification: What external shifts create new possibilities?
- Scenario planning: How would strategy change under different conditions?
- Regulatory roadmap: What compliance needs must we plan for?

## Notes
- PESTLE is complementary to SWOT (macro vs. micro analysis)
- Some factors span multiple categories (e.g., regulations affect legal, political, and economic)
- Geographic and industry context matter significantly
- Trends evolve; re-assess PESTLE annually or when markets shift
- Use PESTLE early in strategy development to avoid blind spots

---

### Further Reading

- [The Product Management Frameworks Compendium + Templates](https://www.productcompass.pm/p/the-product-frameworks-compendium)
```

## File: `pm-product-strategy/skills/porters-five-forces/SKILL.md`
```markdown
---
name: porters-five-forces
description: "Perform Porter's Five Forces analysis — competitive rivalry, supplier power, buyer power, threat of substitutes, and threat of new entrants. Use when analyzing industry dynamics, assessing competitive forces, or evaluating market attractiveness."
---
# Porter's Five Forces

## Metadata
- **Name**: porters-five-forces
- **Description**: Perform a Porter's Five Forces analysis evaluating competitive rivalry, supplier power, buyer power, threat of substitutes, and threat of new entrants.
- **Triggers**: Porter's five forces, competitive forces, industry analysis, market forces, competitive dynamics

## Instructions

You are a competitive strategist conducting a Porter's Five Forces analysis for $ARGUMENTS.

Your task is to evaluate the structural attractiveness of an industry and identify the competitive dynamics that will determine profitability.

## Input Requirements
- Industry or market definition
- Current competitors and competitive positioning
- Supplier and customer landscape
- Potential substitutes and new entrants
- Product or service specifics

## Porter's Five Forces Framework

### 1. Competitive Rivalry (How intense is competition?)
The degree to which companies compete directly for market share and customers.

**High Rivalry When:**
- Many competitors of similar size and strength
- Slow industry growth (zero-sum competition)
- Low product differentiation (commoditized)
- High fixed costs (pressure to maintain volume)
- Exit barriers are high (expensive to leave)
- Price competition is intense
- Rivals have diverse strategies and goals
- Emotional or strategic commitments keep rivals fighting

**Low Rivalry When:**
- Few competitors
- High growth market
- High differentiation (less price-sensitive)
- Low fixed costs
- Low switching costs for competitors
- Industry leader has clear dominance
- Rivals are cooperative or have compatible goals

**Strategic Implications:**
- Assess competitive positioning and differentiation
- Define defensible competitive advantages
- Monitor competitor moves and market consolidation
- Invest in differentiation or cost leadership

---

### 2. Supplier Power (How much power do suppliers have?)
The ability of suppliers to increase prices or reduce quality, affecting your profitability.

**High Supplier Power When:**
- Few suppliers or concentrated supplier base
- Switching costs are high (changing suppliers is expensive)
- Backward integration threat (suppliers become competitors)
- Suppliers' product is critical or unique
- Suppliers have strong bargaining position
- No substitutes for supplier offerings
- Suppliers sell to many industries (less dependent on you)

**Low Supplier Power When:**
- Many suppliers available
- Low switching costs
- Suppliers depend on your business
- Commodity products (interchangeable suppliers)
- Threat of forward integration (you become your own supplier)
- Available substitutes for supplier offerings
- You have significant bargaining leverage

**Strategic Implications:**
- Diversify supplier base to reduce dependency
- Build strong supplier relationships
- Consider vertical integration or alternatives
- Negotiate long-term contracts with favorable terms
- Invest in suppliers' success (partnerships)

---

### 3. Buyer Power (How much power do customers have?)
The ability of customers to negotiate lower prices or demand higher quality, affecting your margin.

**High Buyer Power When:**
- Few large customers (concentrated demand)
- Buyers switch easily and often (low switching costs)
- Backwards integration threat (customers become competitors)
- Product is undifferentiated (commoditized)
- Buyers have price sensitivity or tight budgets
- Buyers have full information about alternatives
- Customers can bypass you entirely

**Low Buyer Power When:**
- Many fragmented customers
- High switching costs (lock-in, integration, training)
- High product differentiation (fewer alternatives)
- Customers depend on your product
- You have strong brand or reputation
- Switching to alternatives involves risk
- Customers lack information about alternatives

**Strategic Implications:**
- Build strong customer relationships and loyalty
- Create switching costs through integration
- Invest in brand and differentiation
- Develop customer success programs
- Create network effects or communities
- Segment customers by willingness to pay

---

### 4. Threat of Substitutes (Are there alternative solutions?)
The risk that customers will switch to alternative products that solve the same problem.

**High Threat When:**
- Good substitutes exist and are easily accessible
- Substitutes have similar performance or better value
- Switching costs to substitutes are low
- Customers are willing to try alternatives
- Substitutes are improving faster than your product
- Price-to-performance of substitutes is attractive
- Substitute technology is disruptive or emerging

**Low Threat When:**
- No good substitutes exist
- Substitutes are more expensive or inferior
- Switching costs are high
- Your product is deeply integrated into customer workflows
- Customer preference and loyalty are strong
- Barrier to substitute entry are high
- Your product solves the problem uniquely

**Strategic Implications:**
- Monitor emerging substitutes and disruptive technologies
- Build customer stickiness through integration and loyalty
- Invest in product innovation and improvement
- Create switching costs through ecosystem or community
- Diversify into adjacent or complementary products
- Defend through brand, service, or convenience

---

### 5. Threat of New Entrants (Can new competitors easily enter?)
The risk that new competitors will enter the market and capture share.

**High Threat When:**
- Low barriers to entry (capital, expertise, licensing)
- Attractive industry margins and growth
- Incumbents are vulnerable or complacent
- Distribution or channel access is available
- Economies of scale are limited
- Network effects are weak or absent
- Regulation is permissive
- New technologies enable disruption

**Low Threat When:**
- High barriers to entry (capital, IP, expertise, relationships)
- Entrenched incumbents with scale advantages
- Strong network effects or switching costs
- Brand loyalty is high
- Regulatory or licensing barriers exist
- Economies of scale create cost advantage
- Control of critical resources or distribution
- Retaliation by incumbents is credible

**Strategic Implications:**
- Build defensible barriers (IP, brand, network effects)
- Establish cost leadership and scale advantages
- Create switching costs and customer lock-in
- Invest in brand and customer relationships
- Monitor startups and disruptors in your space
- Build alliances and control key resources

---

## Output Process
1. Assess each of the five forces (High, Medium, Low)
2. Rate industry attractiveness (High rivalry + strong forces = less attractive)
3. For each force, identify:
   - Current state and trend (getting stronger/weaker)
   - Key players or dynamics
   - Implications for profitability
4. Prioritize the 2-3 forces most critical to your strategy
5. Develop strategic responses:
   - How can we reduce threat of high-power forces?
   - How can we leverage weak forces for advantage?
6. Identify competitive positioning opportunities
7. Create strategic initiatives aligned with force analysis

## Industry Attractiveness
- **Attractive**: Low rivalry, weak supplier/buyer power, few substitutes, high entry barriers
- **Unattractive**: High rivalry, strong supplier/buyer power, many substitutes, low entry barriers
- **Moderate**: Mixed dynamics requiring strategic differentiation

## Notes
- No industry is universally attractive or unattractive; position matters
- Same industry can be attractive for some companies, unattractive for others
- Forces change over time; re-assess as market evolves
- Use Porter's Five Forces with SWOT and PESTLE for comprehensive analysis
- Strategy should directly address the highest-force threats

---

### Further Reading

- [The Product Management Frameworks Compendium + Templates](https://www.productcompass.pm/p/the-product-frameworks-compendium)
```

## File: `pm-product-strategy/skills/pricing-strategy/SKILL.md`
```markdown
---
name: pricing-strategy
description: "Analyze and design pricing strategies including pricing models, competitive pricing analysis, willingness-to-pay estimation, and price elasticity. Use when setting prices, evaluating pricing models, preparing for a pricing change, or comparing freemium vs paid approaches."
---

## Pricing Strategy

Design a pricing strategy grounded in value delivery, competitive positioning, and willingness to pay.

### Context

You are developing a pricing strategy for **$ARGUMENTS**.

If the user provides files (competitor pricing, survey data, financial models, or usage data), read them first. Use web search to research competitor pricing if needed.

### Instructions

1. **Understand the value delivered**:
   - What is the core value proposition?
   - What is the customer's alternative (and its cost)?
   - What quantifiable outcomes does the product deliver? (time saved, revenue gained, cost reduced)
   - What is the customer's willingness to pay based on that value?

2. **Evaluate pricing models** — recommend the best fit:

   | Model | Best For | Example |
   |---|---|---|
   | **Flat-rate** | Simple products, predictable costs | Basecamp ($99/mo flat) |
   | **Per-seat** | Collaboration tools, team products | Slack, Figma |
   | **Usage-based** | Infrastructure, API products | AWS, Twilio |
   | **Tiered** | Products with distinct user segments | Most SaaS (Free/Pro/Enterprise) |
   | **Freemium** | Products with viral/network effects | Spotify, Notion |
   | **Freemium + usage** | Platform products | Vercel, OpenAI API |
   | **Value-based** | High-impact enterprise tools | Salesforce, Palantir |

3. **Analyze competitive pricing**:
   - Map competitor pricing tiers and what's included
   - Identify where your product sits (premium, mid-market, budget)
   - Find pricing gaps or opportunities
   - Note any industry pricing conventions

4. **Design the pricing structure**:
   - **Tiers**: Define 2-4 tiers with clear differentiation
   - **Feature gating**: Which features go in which tier? (Use value metrics, not arbitrary limits)
   - **Value metric**: What unit do you charge on? (users, events, storage, API calls)
   - **Anchor pricing**: Set the most popular tier to feel like the obvious choice
   - **Annual discount**: Typically 15-20% off monthly pricing

5. **Estimate price sensitivity**:
   - Van Westendorp Price Sensitivity Meter (if survey data available):
     - Too cheap → quality concerns
     - Cheap → good value
     - Expensive → starting to hesitate
     - Too expensive → won't buy
   - Alternatively, estimate based on competitor pricing and value delivered

6. **Plan pricing experiments**:
   - A/B test pricing pages (different price points, tier names, feature bundles)
   - Founder-led sales conversations to test willingness to pay
   - Landing page tests with different price anchors
   - Cohort analysis of conversion rates by price point

7. **Output a pricing recommendation**:
   ```
   Recommended Model: [Model type]
   Value Metric: [What you charge on]

   | Tier | Price | Target Segment | Key Features | Positioning |
   |---|---|---|---|---|

   Key Assumptions:
   - [Assumption] → [How to test]

   Risks:
   - [Risk] → [Mitigation]
   ```

Think step by step. Save as markdown. Flag any assumptions that need validation before launch.

---

### Further Reading

- [Product Pricing Strategies 101](https://www.productcompass.pm/p/product-pricing-strategies-101)
- [The AI Product Pricing Masterclass: OpenAI Product Lead on Why SaaS Pricing Fails in AI (and How to Fix It)](https://www.productcompass.pm/p/ai-product-pricing) (video course)
```

## File: `pm-product-strategy/skills/product-strategy/SKILL.md`
```markdown
---
name: product-strategy
description: "Create a comprehensive product strategy using the 9-section Product Strategy Canvas — vision, segments, costs, value propositions, trade-offs, metrics, growth, capabilities, and defensibility. Use when building a product strategy, creating a strategic plan, or defining product direction."
---
# Product Strategy Canvas

## Metadata
- **Name**: product-strategy
- **Description**: Generate a comprehensive product strategy using the 9-section Product Strategy Canvas. Covers vision, market segments, costs, value propositions, trade-offs, metrics, growth, capabilities, and defensibility.
- **Triggers**: product strategy, strategy canvas, strategic plan, product strategy document

## Instructions

You are an experienced product strategist developing a comprehensive product strategy for $ARGUMENTS.

Your task is to create a detailed Product Strategy Canvas that outlines how the product will compete, win, and grow in the market.

## Input Requirements
- Product description and current positioning
- Market context, competitors, and customer insights
- Company resources, constraints, and priorities
- Any relevant business or market data

## Product Strategy Canvas Template

### 1. Vision
- How can we inspire people?
- What are we aspiring to achieve?
- What values do we uphold?

### 2. Market Segments
- Market defined by people's problems (not demographics)
- Jobs to Be Done (JTBD), desired outcomes, constraints
- Who is our first segment?
- Why this segment first?

### 3. Relative Costs
- Do we optimize for low cost (like Southwest Airlines)?
- Or do we emphasize unique value (like Starbucks)?
- What's our cost position relative to competitors?

### 4. Value Proposition
For each target segment:
- **What before**: The customer's current situation, pain, or need
- **How**: How your product delivers the solution
- **What after**: The improved outcome or future state
- **Alternatives**: What customers use today instead

### 5. Trade-offs
- What will we NOT do?
- What features or markets are out of scope?
- How does saying "no" create focus and amplify our value?

### 6. Key Metrics
- **North Star Metric**: Single metric that drives overall business success
- **OMTM (One Metric That Matters)**: The one metric we optimize for this quarter

### 7. Growth
- Sales-Led Growth or Product-Led Growth?
- Primary acquisition channels
- How do we scale?
- What's our unit economics?

### 8. Capabilities
- What competencies and resources do we need?
- What do we build vs. partner for?
- What capabilities must we develop to win?

### 9. Can't/Won't
- Why can't competitors easily copy this?
- What defensibility do we have (network effects, switching costs, IP)?
- What barriers to entry exist for new competitors?

## Output Process
1. Define the vision and aspirational impact
2. Identify 2-3 target market segments with their JTBD
3. Establish cost positioning (low cost vs. premium value)
4. Develop value propositions for each segment
5. List explicit trade-offs (what we won't do)
6. Set North Star and quarterly OMTM
7. Outline growth strategy and channels
8. Document required capabilities and partnerships
9. Explain defensibility and barriers to competition
10. Validate strategy coherence: ensure elements reinforce each other
11. Surface critical hypotheses that must be true for success
12. Suggest low-effort experiments to test key assumptions

## Notes
- Ensure all 9 elements fit together logically
- Identify what must be true for this strategy to work (hypotheses)
- Propose validation experiments with minimal effort
- Strategy guides decisions; clarity enables faster execution
- Revisit quarterly as market conditions change

---

### Templates

- [Product Strategy Canvas (PPTX)](https://docs.google.com/presentation/d/1xRBqSOISvAKzwM_z5tC8fiuO5O2YhboB/edit?usp=sharing&ouid=111307342557889008106&rtpof=true&sd=true)

---

### Further Reading

- [Product Strategy Canvas: From Vision to Action](https://www.productcompass.pm/p/product-strategy-canvas)
- [Product Strategy Examples: Google Maps, Netflix, OpenAI](https://www.productcompass.pm/p/product-strategy-examples)
- [Product Vision vs Strategy vs Objectives vs Roadmap: The Advanced Edition](https://www.productcompass.pm/p/product-vision-strategy-goals-and)
- [Product Model First Principles: Product Team and Product Strategy In Depth](https://www.productcompass.pm/p/product-model-first-principles-transformed-cagan)
- [Introducing the Product Strategy Canvas](https://www.productcompass.pm/p/new-product-strategy-canvas)
- [Business Outcomes vs Product Outcomes vs Customer Outcomes](https://www.productcompass.pm/p/business-outcomes-vs-product-outcomes)
- [From Strategy to Objectives Masterclass](https://www.productcompass.pm/p/product-vision-strategy-objectives-course) (video course)
```

## File: `pm-product-strategy/skills/product-vision/SKILL.md`
```markdown
---
name: product-vision
description: "Brainstorm an inspiring, achievable, and emotional product vision that motivates teams and aligns stakeholders. Use when defining or refining a product vision, creating a vision statement, or aligning the team around a shared direction."
---
# Product Vision

## Metadata
- **Name**: product-vision
- **Description**: Brainstorm an inspiring, achievable, and emotional product vision. Use when defining or refining product vision, aligning teams around a north star, or creating a vision statement.
- **Triggers**: product vision, vision statement, create vision, inspiring vision, north star vision

### Domain Context

A product **vision** answers: "How can we inspire people? What are we aspiring to achieve? What values do we uphold?" Vision evolves with strategy — it's a living statement, not a one-time exercise. It should make people feel something, not just understand the direction.

## Instructions

You are a veteran product leader developing a compelling product vision.

Your task is to brainstorm a product vision for $ARGUMENTS.

## Input Requirements
- Information about your company and product (you may read files from the user's workspace)
- Current state, market positioning, or any relevant context

## Output
Provide a vision statement that is:
1. **Inspiring** - Motivates teams to wake up and commit to the goal
2. **Achievable** - Realistic based on resources, market, and capabilities
3. **Emotional** - Creates meaning and connection

## Process
1. Review provided company and product information
2. Identify the core problem being solved
3. Envision the ideal future state for customers and the company
4. Draft multiple vision options (3-5 variations)
5. Select the strongest vision and briefly explain your rationale
6. Highlight how this vision aligns with company values and market opportunity

## Notes
- A great vision is memorable and can be communicated in one sentence
- Balance ambition with credibility
- Consider the perspective of customers, employees, and investors
- Avoid jargon; use clear, emotionally resonant language

---

### Further Reading

- [Product Vision vs Strategy vs Objectives vs Roadmap: The Advanced Edition](https://www.productcompass.pm/p/product-vision-strategy-goals-and)
- [Introducing the Product Strategy Canvas](https://www.productcompass.pm/p/new-product-strategy-canvas)
- [From Strategy to Objectives Masterclass](https://www.productcompass.pm/p/product-vision-strategy-objectives-course) (video course)
```

## File: `pm-product-strategy/skills/startup-canvas/SKILL.md`
```markdown
---
name: startup-canvas
description: "Generate a Startup Canvas combining Product Strategy (9 sections) and Business Model (costs + revenue) for a new product. An alternative to BMC and Lean Canvas that separates strategy from business model. Use when launching a new product or evaluating a startup concept."
---
# Startup Canvas

## Metadata
- **Name**: startup-canvas
- **Description**: Generate a Startup Canvas for a new product. Combines the 9-section Product Strategy Canvas with a Business Model (Cost Structure + Revenue Streams). Designed specifically for startups and new products.
- **Triggers**: startup canvas, new product canvas, startup strategy, startup business model

## Domain Context

### Startup Canvas vs Business Model Canvas vs Lean Canvas

Popular approaches like Business Model Canvas (Strategyzer) and Lean Canvas (Ash Maurya) mix strategy and business model into one artifact. The **Startup Canvas** (Paweł Huryn) separates them: 9 strategy sections from the Product Strategy Canvas + Cost Structure & Revenue Streams.

**Why not Business Model Canvas?**
- No vision — why should your team wake up every day?
- No Can't/Won't test — what stops competitors from copying you?
- No trade-offs — what you choose NOT to do creates focus
- No key metrics — how do you know the strategy is working?
- Key Partnerships and Key Resources are rarely useful for early-stage products

**Why not Lean Canvas?**
- Introduces redundancy: "Problem" overlaps with Market Segments (markets are defined by problems), "Solution" overlaps with Value Proposition (which by definition includes features)
- No vision, no trade-offs, no relative costs
- "Unfair Advantage" is too narrow — the entire strategy should be hard to copy, not just one element
- Doesn't address the holistic fit of strategic choices reinforcing each other

**When to use which:**
- **Business Model Canvas**: Established businesses, corporate strategy, investor materials
- **Lean Canvas**: Quick hypothesis testing when you just need speed
- **Startup Canvas**: New products where you need both strategic clarity AND a business model — the recommended approach

## Instructions

You are a product strategist and startup advisor designing a Startup Canvas for $ARGUMENTS.

Your task is to create a comprehensive Startup Canvas that covers both the strategic choices and the business model for a new product.

## Input Requirements
- Product or startup idea
- Target market and customer insights
- Competitive landscape
- Founder/team constraints and resources

## Startup Canvas Template

### Part 1: Product Strategy (9 Sections)

**1. Vision**
- How can we inspire people? What are we aspiring to achieve? What values do we uphold?
- Start simple. Your vision will evolve alongside the strategy.

**2. Market Segments**
- The market is defined by the problems people have (not demographics).
- Jobs to Be Done (JTBD), desired outcomes, constraints.
- What will be your first customer segment? Why this one first?

**3. Relative Costs**
- Do you optimize for low cost (like Southwest Airlines) or unique value (like Starbucks)?
- Low costs don't necessarily mean low prices.

**4. Value Proposition**
For each market segment:
- **What before**: Existing, problematic state
- **How**: Features and capabilities that change the situation
- **What after**: The benefits and outcomes
- **Alternatives**: Your unique value vs. competitors and substitutes (consider a Value Curve)

**5. Trade-offs**
- What will you NOT do? Trade-offs create focus and amplify value.
- Especially important for startups where it's tempting to chase every opportunity.

**6. Key Metrics**
- A few key metrics to measure if the product and strategy are working.
- North Star Metric and One Metric That Matters (OMTM) for this quarter.

**7. Growth**
- Product-Led Growth or Sales-Led Growth?
- Preferred channels: Social Media, SEO, Influencers, Resellers?

**8. Capabilities**
- What competencies and resources do you need to acquire?
- What do you build vs. partner for?

**9. Can't/Won't**
- What makes you think competitors can't or won't copy your strategy?
- The entire strategy should be difficult to copy — not just one element.
- Do all elements fit together and reinforce each other?

### Part 2: Business Model

**10. Cost Structure**
- Rent, hardware, licenses, technology, marketing, subscriptions, salaries.
- Which are recurring? How will they scale?

**11. Revenue Streams**
- How much money from each channel?
- Pricing approach: penetration, value-based, competitive, usage-based, SaaS?
- Is the revenue model scalable? What are the biggest uncertainties?

## Output Process
1. Define the vision and aspirational impact
2. Identify 2–3 target market segments with JTBD
3. Establish cost positioning (low cost vs premium)
4. Develop value propositions for each segment
5. List explicit trade-offs
6. Set North Star and quarterly OMTM
7. Outline growth strategy and channels
8. Document required capabilities
9. Explain defensibility (Can't/Won't test)
10. Estimate cost structure and revenue streams
11. Validate strategy coherence: do all elements reinforce each other?
12. Surface hypotheses that must be true for success
13. Suggest low-effort experiments to test key assumptions

## Notes
- The Startup Canvas separates strategy from business model — keep them distinct but connected
- Strategy should pass the Can't/Won't test: your competitors can't or won't copy the integrated set of choices
- After drafting the first version, identify and start testing hypotheses
- Mix and adapt approaches to suit your specific needs rather than following any canvas rigidly

---

### Templates

- [Startup Canvas (PPTX)](https://docs.google.com/presentation/d/1lA0SPflj5JT6jFV_jIDsqZJAYYperTFx/edit?usp=sharing&ouid=111307342557889008106&rtpof=true&sd=true)

---

### Further Reading

- [Startup Canvas: Product Strategy and a Business Model for a New Product](https://www.productcompass.pm/p/startup-canvas)
- [Product Strategy Canvas](https://www.productcompass.pm/p/product-strategy-canvas)
- [How to Design a Value Proposition Customers Can't Resist?](https://www.productcompass.pm/p/how-to-design-value-proposition-template)
- [Business Model Canvas Examples: Google Maps, Airbnb, Uber](https://www.productcompass.pm/p/business-model-canvas-examples)
```

## File: `pm-product-strategy/skills/swot-analysis/SKILL.md`
```markdown
---
name: swot-analysis
description: "Perform a detailed SWOT analysis — strengths, weaknesses, opportunities, and threats with actionable recommendations. Use when doing strategic assessment, competitive analysis, or evaluating a product or business position."
---
# SWOT Analysis

## Metadata
- **Name**: swot-analysis
- **Description**: Perform a detailed SWOT analysis for a product. Identifies strengths, weaknesses, opportunities, and threats with actionable recommendations.
- **Triggers**: SWOT analysis, strengths weaknesses, SWOT matrix, strategic assessment

## Instructions

You are a strategic analyst conducting a SWOT analysis for $ARGUMENTS.

Your task is to thoroughly evaluate the internal and external factors that will impact product success and competitive positioning.

## Input Requirements
- Product description and current state
- Competitive landscape and market context
- Company capabilities, resources, and constraints
- Market trends and industry dynamics
- Customer feedback or usage data (optional)

## SWOT Analysis Framework

### 1. Strengths (Internal, Positive)
What internal capabilities and advantages do we have?

- Unique capabilities or expertise
- Brand recognition or reputation
- Customer relationships and loyalty
- Technology or IP advantages
- Cost advantages or operational efficiency
- Team talent and experience
- Existing customer base or distribution

### 2. Weaknesses (Internal, Negative)
What internal limitations or gaps do we have?

- Resource constraints (budget, team size, skills)
- Technology or infrastructure limitations
- Lack of brand awareness or market presence
- Weak customer relationships or high churn
- High cost structure relative to competitors
- Outdated processes or legacy systems
- Dependence on key people or partners

### 3. Opportunities (External, Positive)
What external trends or market dynamics could we leverage?

- Growing market segments or customer needs
- Technological advances enabling new solutions
- Regulatory changes favoring our approach
- Competitor weaknesses or market gaps
- Partnership or acquisition opportunities
- Expansion into adjacent markets or segments
- Shifting customer preferences or behaviors

### 4. Threats (External, Negative)
What external factors could negatively impact us?

- Emerging or stronger competitors
- Changing customer preferences or needs
- Technological disruption or obsolescence
- Regulatory changes or compliance risks
- Economic downturns or market contraction
- Supply chain disruptions
- Supplier or partner consolidation

## Output Process
1. Identify 5-7 strengths (be honest about competitive advantages)
2. List 5-7 weaknesses (avoid minimizing; focus on addressable gaps)
3. Map 5-7 opportunities (prioritize by market size and alignment)
4. Flag 5-7 threats (assess probability and impact)
5. Cross-reference analysis for strategic insights:
   - How do we leverage strengths to capture opportunities?
   - How do we shore up weaknesses to mitigate threats?
   - Which opportunities can overcome weaknesses?
   - Which threats could exploit weaknesses?
6. Develop 3-5 strategic recommendations
7. Prioritize actions and owners
8. Identify metrics to track progress

## Strategic Applications
- **Build**: Double down on strengths + opportunities
- **Defend**: Fortify weaknesses + mitigate threats
- **Pivot**: Explore opportunities that change the competitive dynamic
- **Exit**: If too many threats and weak competitive position

## Notes
- SWOT is internal to external assessment
- Context matters: compare against competitors and industry standards
- Update SWOT quarterly or when market conditions change
- Use SWOT to inform product roadmap, partnerships, and resource allocation
- Opportunities and threats should consider both current and emerging dynamics
```

## File: `pm-product-strategy/skills/value-proposition/SKILL.md`
```markdown
---
name: value-proposition
description: "Design a detailed value proposition using a 6-part JTBD template — Who, Why, What before, How, What after, Alternatives. Use when creating a value proposition, analyzing customer value delivery, or articulating why customers should choose your product."
---
# Value Proposition

## Metadata
- **Name**: value-proposition
- **Description**: Generate a detailed value proposition using a 6-part template with JTBD framing. Includes practical examples for designing compelling customer value.
- **Triggers**: value proposition, value prop, customer value, JTBD value, value map

## Instructions

You are a product strategist designing a clear value proposition for $ARGUMENTS.

Your task is to develop a comprehensive value proposition that articulates the customer value delivered by the product.

## Input Requirements
- Product description and features
- Target customer segment and their problems
- Competitive alternatives and current solutions
- Customer insights or market data

## Value Proposition Template

### 6-Part Structure

**1. Who**
- Who is this value proposition for?
- What customer segment are we addressing?
- What are their characteristics and constraints?

**2. Why (Problem)**
- What is the customer's core problem or need?
- What's the Job to Be Done (JTBD)?
- What desired outcomes are they trying to achieve?

**3. What Before**
- What is the customer's current situation?
- What are they using today to solve this problem?
- What friction or pain exists in the current approach?

**4. How (Solution)**
- How does the product solve the problem?
- What specific features or capabilities deliver value?
- Why is this solution better than alternatives?

**5. What After**
- What is the improved outcome or future state?
- How does the customer's life/work change?
- What becomes possible that wasn't before?

**6. Alternatives**
- What other solutions could customers use?
- Why would they choose us instead?
- What's the switching cost or friction from alternatives?

## Example: Canva
- **Who**: Non-designers who need to create marketing graphics
- **Why**: They need professional-looking designs but can't hire designers or use complex tools
- **What Before**: Using PowerPoint, Photoshop (too complex), or hiring expensive designers
- **How**: Drag-and-drop templates, built-in design elements, AI design assistance, intuitive interface
- **What After**: Create professional designs in minutes, launch campaigns faster, save design costs
- **Alternatives**: Photoshop (complex), Fiverr (slow, expensive), Canva competitors (fewer templates, harder UX)

## Output Process
1. Identify and profile the target customer segment
2. Define the core problem and JTBD
3. Describe the current state and friction points
4. Articulate how the product solves the problem
5. Envision the improved outcome
6. Compare against competitive alternatives
7. Create a concise value prop statement (1-2 sentences)
8. Develop a positioning statement for marketing use

### Domain Context

**This template vs Strategyzer's Value Proposition Canvas**: Strategyzer's canvas (by Alexander Osterwalder) is widely used but has structural limitations. This 6-part JTBD template (by Paweł Huryn and Aatir Abdul Rauf) addresses them:

- **Customer first**: This template starts with the customer (Who/Why) and works toward the solution. Strategyzer's canvas places the product on the left, which often leads teams to start with their solution rather than the customer's problem.
- **One segment at a time**: This template is designed for one segment per pass. Strategyzer's canvas encourages mapping multiple products/services simultaneously, which dilutes focus.
- **Explicit alternatives**: Section 6 (Alternatives) forces you to name what customers would use without you and articulate why you're better. Strategyzer's canvas has no equivalent — you don't directly confront substitutes.
- **Simpler structure**: "What before → How → What after" is easier to fill out than separating Customer Jobs, Pains, and Gains on one side and Pain Relievers, Gain Creators, and Products on the other. The separation often creates confusion about where things go.
- **Actionable output**: The final Value Proposition Statement is ready for marketing, sales, and onboarding. Strategyzer's canvas doesn't produce a reusable statement.

Use Strategyzer's Value Proposition Canvas when you need a detailed pains/gains decomposition for a mature product with complex customer needs. Use this 6-part template for clarity, speed, and actionable output.

## Notes
- Jobs to Be Done (JTBD) framework focuses on the progress the customer is trying to make, not demographics
- Value propositions are segment-specific; you may have different value props for different customer groups
- The stronger your value prop, the easier marketing, sales, and product decisions become
- Test value props with real customers before finalizing
- Use a **Value Curve** (Blue Ocean Strategy) to visually compare your offering against competitors across key factors

---

### Templates

- [Value Proposition Template (PPTX)](https://docs.google.com/presentation/d/1RXH1Udj71aXQJzGeqYSOStnfQ-6dNz14/edit?slide=id.g2a98aeea3b1_0_247#slide=id.g2a98aeea3b1_0_247)

---

### Further Reading

- [How to Design a Value Proposition Customers Can't Resist?](https://www.productcompass.pm/p/how-to-design-value-proposition-template)
- [How to Achieve Product-Market Fit? Part I: Market and Value Proposition](https://www.productcompass.pm/p/how-to-achieve-the-product-market)
- [Jobs-to-be-Done Masterclass with Tony Ulwick and Sabeen Sattar](https://www.productcompass.pm/p/jobs-to-be-done-masterclass-with) (video course)
- [Product Innovation Masterclass](https://www.productcompass.pm/p/product-innovation-masterclass) (video course)
```

## File: `pm-toolkit/README.md`
```markdown
# pm-toolkit

PM utility skills: resume review, NDA drafting, privacy policy generation, and grammar/flow checking. Essential tools for product managers beyond core product work.

## Skills (4)

- **draft-nda** — Draft a detailed Non-Disclosure Agreement between two parties.
- **grammar-check** — Identify grammar, logical, and flow errors in text and suggest targeted fixes without rewriting the entire text.
- **privacy-policy** — Draft a detailed privacy policy for a product covering data types, jurisdiction, compliance considerations, and clauses needing legal review.
- **review-resume** — Comprehensive PM resume review and tailoring against 10 best practices including XYZ+S formula, keyword optimization, job-specific tailoring, and structure.

## Commands (5)

- `/pm-toolkit:draft-nda` — Draft a Non-Disclosure Agreement between two parties with jurisdiction-appropriate clauses.
- `/pm-toolkit:privacy-policy` — Draft a privacy policy covering data collection, usage, storage, and compliance requirements.
- `/pm-toolkit:proofread` — Check grammar, logic, and flow in any text — targeted fixes without rewriting.
- `/pm-toolkit:review-resume` — Comprehensive PM resume review against 10 best practices — structure, impact metrics, keywords, and actionable feedback.
- `/pm-toolkit:tailor-resume` — Tailor a PM resume to a specific job description — keyword alignment, experience reframing, and strategic optimization.

## Author

Paweł Huryn — [The Product Compass Newsletter](https://www.productcompass.pm)

## License

MIT
```

## File: `pm-toolkit/commands/draft-nda.md`
```markdown
---
description: Draft a Non-Disclosure Agreement between two parties with jurisdiction-appropriate clauses
argument-hint: "<parties and context>"
---

# /draft-nda -- NDA Drafting

Draft a professional Non-Disclosure Agreement customized to your situation. Covers information types, jurisdiction, term, and clearly marks clauses that need legal review.

## Invocation

```
/draft-nda Mutual NDA between our startup and a potential enterprise customer
/draft-nda One-way NDA for a freelance contractor accessing our codebase
```

## Workflow

### Step 1: Gather Context

Ask:
- Who are the parties? (company names and roles)
- Mutual or one-way NDA?
- What information is being protected? (trade secrets, code, business data, customer data)
- Jurisdiction? (state/country for governing law)
- Duration? (how long should confidentiality last)
- Any specific concerns? (non-compete, non-solicit, IP ownership)

### Step 2: Draft the NDA

Apply the **draft-nda** skill:

Generate a complete NDA covering:
- Parties and recitals
- Definition of confidential information (with specific examples)
- Obligations of the receiving party
- Exclusions (public knowledge, independent development, etc.)
- Term and survival
- Return/destruction of materials
- Remedies
- Governing law and jurisdiction
- Standard boilerplate (severability, entire agreement, amendments)

### Step 3: Deliver

```
## Non-Disclosure Agreement

[Full NDA text with marked sections]

### Clauses Requiring Legal Review
| Clause | Why It Needs Review | Consideration |
|--------|-------------------|--------------|

### Plain-Language Summary
[What this NDA means in simple terms for non-lawyers]
```

Save as markdown. Offer to export as DOCX for signing.

## Notes

- This is a starting point — always recommend review by qualified legal counsel
- Mark any clause that involves significant legal risk with a ⚠️ flag
- Include plain-language annotations so non-lawyers understand what they're agreeing to
- Mutual NDAs are generally preferred — they're fairer and faster to negotiate
```

## File: `pm-toolkit/commands/privacy-policy.md`
```markdown
---
description: Draft a privacy policy covering data collection, usage, storage, and compliance requirements
argument-hint: "<product and data handling context>"
---

# /privacy-policy -- Privacy Policy Generator

Draft a comprehensive privacy policy for your product. Covers data types, jurisdiction, compliance (GDPR, CCPA), and marks clauses needing legal review.

## Invocation

```
/privacy-policy SaaS analytics tool that collects user behavior data — serving US and EU customers
/privacy-policy Mobile app with location data and third-party integrations
```

## Workflow

### Step 1: Gather Context

Ask:
- What product or service?
- What data is collected? (personal info, usage data, cookies, location, payment)
- Where are your users? (determines applicable regulations: GDPR, CCPA, etc.)
- Any third-party data sharing? (analytics, advertising, integrations)
- Data storage: where and how long?
- Age restrictions? (COPPA considerations)

### Step 2: Draft the Policy

Apply the **privacy-policy** skill:

Generate sections covering:
- What data is collected and how
- How data is used (purposes)
- Legal basis for processing (GDPR)
- Data sharing and third parties
- Data retention and deletion
- User rights (access, deletion, portability, opt-out)
- Cookie policy
- Security measures
- Children's privacy (if applicable)
- International transfers
- Contact information
- Policy update process

### Step 3: Deliver

```
## Privacy Policy: [Product]

[Full policy text]

### Compliance Checklist
| Regulation | Status | Notes |
|-----------|--------|-------|

### Clauses Requiring Legal Review
| Clause | Why | Priority |
|--------|-----|----------|

### Implementation Checklist
- [ ] Cookie consent banner
- [ ] Data subject request process
- [ ] Data processing records
- [ ] DPA with processors
```

Save as markdown. Offer DOCX export.

## Notes

- This is a template — legal counsel should review before publishing
- GDPR and CCPA have specific requirements that can't be approximated — flag where expert review is essential
- Privacy policies should be in plain language, not legalese
- Update the policy when data practices change, not just annually
```

## File: `pm-toolkit/commands/proofread.md`
```markdown
---
description: Check grammar, logic, and flow in any text — targeted fixes without rewriting
argument-hint: "<text to check>"
---

# /proofread -- Grammar & Flow Check

Identify grammar, logical, and flow errors in text. Provides specific, targeted fixes without rewriting the entire document.

## Invocation

```
/proofread [paste text]
/proofread [upload a document]
```

## Workflow

### Step 1: Accept Text

Accept text in any form: pasted, uploaded document (DOCX, PDF, markdown), or email draft.

### Step 2: Analyze

Apply the **grammar-check** skill:

Scan for three categories of issues:

**Grammar**: Spelling, punctuation, subject-verb agreement, tense consistency, article usage
**Logic**: Contradictions, unsupported claims, circular reasoning, unclear references
**Flow**: Awkward transitions, sentence rhythm, paragraph structure, redundancy, readability

### Step 3: Report Issues

```
## Proofread Report

**Text length**: [word count]
**Issues found**: [count by category]

### Issues

#### 1. [Category: Grammar/Logic/Flow]
- **Location**: "[quoted text with issue]"
- **Issue**: [what's wrong]
- **Fix**: "[corrected text]"

[Repeat for each issue]

### Summary
- Grammar: [X] issues
- Logic: [X] issues
- Flow: [X] issues
- Overall quality: [assessment]
```

### Step 4: Offer

- "Want me to **apply all fixes** and return the cleaned text?"
- "Should I **focus on a specific section** in more detail?"

## Notes

- Fix suggestions should be minimal — change only what's needed, preserve the author's voice
- For non-native English speakers, be especially clear about *why* a change is suggested
- Don't over-correct style preferences — there's a difference between wrong and different
- For professional documents, also check for tone consistency and audience appropriateness
```

## File: `pm-toolkit/commands/review-resume.md`
```markdown
---
description: Comprehensive PM resume review against 10 best practices — structure, impact metrics, keywords, and actionable feedback
argument-hint: "<resume as text or file>"
---

# /review-resume -- PM Resume Review

Get a thorough resume review against product management best practices. Evaluates structure, impact metrics, keyword optimization, and provides specific improvement suggestions with examples.

## Invocation

```
/review-resume [paste resume text]
/review-resume [upload resume PDF or DOCX]
```

## Workflow

### Step 1: Accept the Resume

Accept as pasted text, uploaded PDF, or DOCX file. Parse the full content.

### Step 2: Evaluate Against 10 Best Practices

Apply the **review-resume** skill:

1. **Impact Metrics**: Are accomplishments quantified? (revenue, users, conversion rates)
2. **XYZ+S Formula**: "Accomplished [X] as measured by [Y], by doing [Z] using [S skill/tool]"
3. **PM-Specific Language**: Uses product terminology (shipped, led discovery, defined strategy)
4. **Structure & Readability**: Clear sections, consistent formatting, scannable
5. **Keyword Optimization**: Matches common PM job description keywords
6. **Story Arc**: Shows career progression and increasing scope
7. **Brevity**: One page (junior), two pages max (senior). No fluff.
8. **Relevance**: Experience tailored to PM roles, not generic
9. **Technical Credibility**: Demonstrates working with engineering, data, design
10. **Leadership Signals**: Cross-functional influence, stakeholder management, mentoring

### Step 3: Generate Review

```
## Resume Review

**Overall Score**: [X/10]
**Strongest area**: [which best practice]
**Biggest opportunity**: [which best practice]

### Scorecard
| # | Best Practice | Score | Assessment |
|---|-------------|-------|-----------|
| 1 | Impact Metrics | [/10] | [brief assessment] |
| 2 | XYZ+S Formula | [/10] | [brief assessment] |
| ... | ... | ... | ... |

### Top 3 Improvements

**1. [Most impactful change]**
- Current: "[exact text from resume]"
- Suggested: "[improved version]"
- Why: [reasoning]

**2. [Second improvement]**
[same format]

**3. [Third improvement]**
[same format]

### Section-by-Section Feedback
[Specific notes for each resume section: summary, experience, education, skills]

### Missing Elements
[What's absent that should be present for a PM resume]

### Keywords to Add
[PM-relevant keywords missing from the resume that appear in typical job descriptions]
```

### Step 4: Offer Next Steps

- "Want me to **tailor this resume** to a specific job description?"
- "Should I **rewrite specific bullet points** using the XYZ+S formula?"
- "Want me to **generate a cover letter** based on this resume?"

## Notes

- Be specific and constructive — "add metrics" is unhelpful, "change 'improved onboarding' to 'reduced onboarding drop-off by 23% (450 → 347 users/month)'" is actionable
- PM resumes should emphasize outcomes over outputs, influence over authority
- ATS (Applicant Tracking System) optimization matters — mention relevant keywords naturally
- Different PM levels have different expectations: APM = potential, Senior PM = impact, Director+ = scale
```

## File: `pm-toolkit/commands/tailor-resume.md`
```markdown
---
description: Tailor a PM resume to a specific job description — keyword alignment, experience reframing, and strategic optimization
argument-hint: "<resume> + <job description>"
---

# /tailor-resume -- Resume-to-JD Optimization

Take your resume and a target job description, then strategically align your experience to maximize interview chances. Keyword optimization, bullet point rewriting, and gap analysis.

## Invocation

```
/tailor-resume [upload resume] Here's the JD: [paste job description]
/tailor-resume [upload both resume and JD as files]
```

## Workflow

### Step 1: Accept Both Documents

Need two inputs:
- The resume (text, PDF, or DOCX)
- The target job description (text, URL, or file)

If only one is provided, ask for the other.

### Step 2: Analyze the Job Description

Extract:
- Required qualifications and skills
- Preferred qualifications
- Key responsibilities
- Industry and domain signals
- Seniority level indicators
- Cultural and team signals

### Step 3: Tailor the Resume

Apply the **review-resume** skill:

- **Keyword alignment**: Map JD keywords to resume content, add missing keywords naturally
- **Bullet point rewriting**: Reframe experience to emphasize JD-relevant accomplishments using XYZ+S formula
- **Section reordering**: Prioritize the most relevant experience
- **Summary/objective**: Rewrite to directly address the role
- **Skills section**: Align with JD requirements

### Step 4: Generate Tailored Resume + Analysis

```
## Resume Tailoring: [Job Title] at [Company]

### Alignment Score: [X/10]

### Keyword Gap Analysis
| JD Keyword | In Resume? | Recommendation |
|-----------|-----------|---------------|

### Changes Made
1. **[Section]**: [what changed and why]
2. ...

### Tailored Resume
[Full rewritten resume text]

### Gap Analysis
**Strong matches**: [where your experience directly aligns]
**Reframed matches**: [where experience was repositioned to fit]
**Gaps**: [JD requirements you don't clearly address — with suggestions]

### Cover Letter Talking Points
[3-4 points to emphasize in a cover letter that bridge remaining gaps]
```

Save tailored resume as markdown.

## Notes

- Never fabricate experience — reframe truthfully, don't invent
- The summary/objective is the highest-ROI section to customize per application
- Match the JD's language exactly where possible (if they say "cross-functional," use "cross-functional")
- For senior roles, emphasize scale and strategic impact; for IC roles, emphasize hands-on execution
```

## File: `pm-toolkit/skills/draft-nda/SKILL.md`
```markdown
---
name: draft-nda
description: "Draft a detailed Non-Disclosure Agreement between two parties covering information types, jurisdiction, and clauses needing legal review. Use when creating confidentiality agreements or preparing an NDA for a partnership."
---
# NDA (Non-Disclosure Agreement) Drafting

You are an experienced legal document specialist with expertise in confidentiality agreements. Your role is to help draft detailed, clear, and professional Non-Disclosure Agreements between parties.

## Purpose
Draft a comprehensive Non-Disclosure Agreement (NDA) between two parties. The NDA covers information types, jurisdiction, and clearly marks clauses that require legal review. Provide plain-language explanations to make the document accessible.

## Important Disclaimer
**This is for informational purposes only and does not constitute legal advice. Always have a licensed attorney review the final document before execution. NDAs are legally binding contracts; professional legal review is essential.**

## Input Arguments
- `$COMPANY_ONE_NAME`: Name of the first party/company
- `$COMPANY_ONE_ADDRESS`: Address of the first party/company
- `$COMPANY_ONE_REPS`: Names and titles of representatives (e.g., "John Smith, CEO; Jane Doe, General Counsel")
- `$COMPANY_TWO_NAME`: Name of the second party/company
- `$COMPANY_TWO_ADDRESS`: Address of the second party/company
- `$COMPANY_TWO_REPS`: Names and titles of representatives
- `$INFORMATION_TYPES`: Types of information to be shared (e.g., "business plans, customer lists, technical specifications, pricing data, source code")
- `$JURISDICTION`: Governing jurisdiction (e.g., "State of California, United States" or "England and Wales")

## Process

### Step 1: Clarify Requirements
Before drafting, note down:
- Are both parties companies or is one an individual?
- What specific types of information will be shared?
- Is this one-way (only one party shares) or mutual (both parties share)?
- What is the geographic jurisdiction?
- What is the intended duration of the NDA?

### Step 2: Structure the NDA
Organize the NDA in standard sections:

1. **Preamble** (Parties, definitions, effective date)
2. **Definitions** (What is "Confidential Information"?)
3. **Obligation to Maintain Confidentiality** (Core obligation)
4. **Permitted Disclosures** (Exceptions to confidentiality)
5. **Term and Duration** (How long does the NDA last?)
6. **Return or Destruction of Information** (What happens after?)
7. **Remedies** (Consequences for breach)
8. **General Provisions** (Governing law, jurisdiction, severability)

### Step 3: Use Plain Language
Write each section in clear, accessible language. Avoid legal jargon where possible. Define terms the first time they're used.

### Step 4: Highlight Clauses Needing Legal Review
Mark sections with [⚠️ LEGAL REVIEW REQUIRED] where customization or specific legal expertise is needed. Include explanations of what should be reviewed.

### Step 5: Provide Context
Include brief notes explaining:
- Why each section is important
- What decisions need to be made by the parties
- Common pitfalls or considerations

## NDA Template Structure

Present the draft NDA in this order:

**[COVER NOTE]**
A brief note explaining the NDA's purpose, the parties involved, and key provisions.

**[FULL NDA DOCUMENT]**
The complete agreement ready for customization.

**[NOTES ON KEY CLAUSES]**
Explanations of important sections and what may need legal customization.

---

## Key Sections to Include

### Preamble
- Introduce both parties clearly with full legal names and addresses
- State the purpose: exploring a potential business relationship, partnership, merger, etc.
- Define the "Effective Date"

### Definitions
- **Confidential Information**: Specify what is considered confidential (business plans, financial data, technical specs, customer lists, etc.). Include scope.
- **Excluded Information**: Clarify what is NOT confidential (publicly available information, information independently developed, information received from third parties without confidentiality obligations)

### Obligations
- Describe the receiving party's duty to keep information confidential
- Specify approved uses of the information
- Outline permitted disclosures (to employees, advisors, on a need-to-know basis)
- [⚠️ LEGAL REVIEW REQUIRED] Standard of care (e.g., "same care as own confidential information, but no less than reasonable care")

### Permitted Disclosures
- Specify who can be told (employees, advisors, consultants on a need-to-know basis)
- Include a requirement that recipients also agree to confidentiality
- Add exception for legally required disclosures (with notice requirement, if possible)

### Term and Duration
- Define the period during which information is being shared
- Define how long confidentiality obligations survive after the relationship ends
- [⚠️ LEGAL REVIEW REQUIRED] Consider different durations for different information types (trade secrets may require longer protection)

### Return or Destruction
- Specify that the receiving party must return or securely destroy confidential information upon request or upon termination
- Option to certify in writing that destruction is complete
- Consider: does the receiving party keep one copy for legal compliance?

### Remedies
- [⚠️ LEGAL REVIEW REQUIRED] State that breach may cause irreparable harm and that injunctive relief is available
- Clarify that remedies are in addition to other legal remedies available

### General Provisions
- **Governing Law and Jurisdiction**: Specify which state or country's laws govern (e.g., California or England)
- [⚠️ LEGAL REVIEW REQUIRED] Dispute resolution process (litigation, arbitration, mediation)
- **Severability**: If one provision is invalid, others remain in force
- **Entire Agreement**: This NDA supersedes prior discussions
- **Amendments**: Specify that NDA can only be modified in writing, signed by both parties
- **Counterparts**: Parties can sign separate copies

---

## Content Guidelines

- **Plain Language**: Write for a primary-school-educated reader. Avoid Latin phrases, unnecessary legal terms.
- **Clarity over Precision**: Choose clear language first. Legal precision can be refined by attorneys.
- **Examples**: Where helpful, include examples of what is/isn't confidential information.
- **Specific Information Types**: Use the $INFORMATION_TYPES provided to make the agreement specific, not generic.
- **Mutual or One-Way**: If $INFORMATION_TYPES suggests only one party is sharing, note this as a one-way NDA. If both, use mutual language.

---

## Output Format

Present the NDA in three parts:

### Part 1: Summary
Bullet-point overview of:
- Parties involved
- Information types covered
- Key duration and terms
- Jurisdiction

### Part 2: Full NDA Document
A complete, ready-to-customize NDA document.

### Part 3: Customization Notes
Guidance on:
- Sections marked for legal review
- Decisions parties need to make
- Common modifications based on situation
- Next steps (legal review, signing process)

---

## Important Reminders

- This is a starting point, not final legal advice
- Jurisdictions vary widely; have a lawyer in the relevant jurisdiction review
- Some industries (tech, pharma, finance) have specific NDA conventions
- Consider mutual vs. one-way requirements
- Think about duration: How long should the information be protected?
- Always have an attorney review before any party signs
```

## File: `pm-toolkit/skills/grammar-check/SKILL.md`
```markdown
---
name: grammar-check
description: "Identify grammar, logical, and flow errors in text and suggest targeted fixes without rewriting the entire text. Use when proofreading content, checking writing quality, or reviewing a draft."
---
# Grammar and Flow Checking

You are an expert copyeditor and writing specialist. Your role is to identify grammar, logical, and flow errors in text, then provide clear, actionable fix suggestions without rewriting the entire document.

## Purpose
Analyze text for grammar, logical, and flow errors. Provide specific, focused suggestions on how to fix each issue. Focus on clarity, correctness, and readability.

## Input Arguments
- `$OBJECTIVE`: What is the intended purpose or goal of the text? (e.g., "persuade investors to fund our Series A," "explain product features to new users," "communicate company values to employees")
- `$TEXT`: The text to review

## Process

### Step 1: Understand Context
- Note the objective: Is this marketing copy, technical documentation, a presentation, an email, social media content?
- Identify the target audience: Experts, general public, stakeholders, customers?
- Consider tone: Formal, casual, authoritative, friendly?

### Step 2: Scan for Errors
Read through the text once, identifying:
- **Grammar errors**: Spelling, punctuation, subject-verb agreement, tense consistency, modifier placement
- **Logical errors**: Contradictions, unsupported claims, unclear cause-and-effect, incomplete thoughts
- **Flow errors**: Choppy transitions, unclear organization, redundancy, passive voice overuse, vague pronouns, awkward phrasing

### Step 3: Categorize Errors
Organize findings by type:
1. Grammar (spelling, punctuation, syntax)
2. Logic (clarity, coherence, reasoning)
3. Flow (transitions, sentence structure, readability, tone consistency)

### Step 4: Create Fix Suggestions
For each error, provide:
- **Location**: Where in the text (e.g., "Paragraph 3, sentence 2")
- **Error identified**: What's wrong
- **Fix suggested**: How to correct it
- **Rationale**: Why this matters (clarity, grammar rule, flow, tone)

### Step 5: Prioritize
Flag highest-impact issues first:
- Critical: Grammar or logic errors that confuse readers
- Important: Flow issues that hurt readability or persuasiveness
- Minor: Stylistic suggestions or polish

---

## Error Categories and Examples

### Grammar Errors

**Spelling**
- Example error: "buisness" instead of "business"
- Fix: Correct spelling to "business"

**Punctuation**
- Example error: "Lets get started" (apostrophe missing in "Let's")
- Fix: Use "Let's" (contraction of "let us")
- Example error: Run-on sentence with multiple independent clauses not connected properly
- Fix: Break into separate sentences or connect with a conjunction/semicolon

**Subject-Verb Agreement**
- Example error: "The team are working" (treating singular noun as plural)
- Fix: "The team is working" (team is a collective noun, treated as singular in US English)

**Tense Consistency**
- Example error: "We launched the product last month and are seeing great results. Users report high satisfaction and prefer our solution." (mix of past and present)
- Fix: Keep tense consistent based on timeframe

**Pronoun Clarity**
- Example error: "The manager told the designer that she should revise the mockups." (Unclear if "she" refers to manager or designer)
- Fix: Use name or restructure: "The manager told the designer to revise the mockups."

**Modifier Placement**
- Example error: "After reviewing the proposal, the decision seemed obvious." (Who reviewed? Unclear.)
- Fix: "After reviewing the proposal, we saw the decision was obvious."

---

### Logical Errors

**Unsupported Claims**
- Example error: "Our product is the best on the market because customers love it."
- Fix: Provide evidence: "Our product has a 4.8-star rating from 2,000+ customers and achieved 40% market share in the SMB segment."

**Contradictions**
- Example error: Text says "We prioritize user privacy" but also "We share user data with 50+ third parties."
- Fix: Clarify or reconcile the statements with detail

**Incomplete Logic**
- Example error: "The feature was launched in Q3, so adoption increased." (No proof of causation)
- Fix: "The feature was launched in Q3; adoption increased 25% in the following month, driven by improved onboarding."

**Vague Claims**
- Example error: "Our solution saves time and money."
- Fix: Be specific: "Our solution reduces onboarding time from 2 hours to 15 minutes and cuts operational costs by 30%."

---

### Flow Errors

**Weak Transitions**
- Example error: Paragraphs jump between topics without connection
- Fix: Add transitional phrases: "In addition to this benefit," "However," "As a result," "This leads to..."

**Choppy Sentences**
- Example error: "We launched the product. We got great feedback. We iterated quickly. We improved the feature."
- Fix: Combine related ideas: "After launching the product, we received great feedback and iterated quickly to improve the feature."

**Passive Voice Overuse**
- Example error: "The decision was made by the team to move forward with the strategy that was agreed upon." (Passive, wordy)
- Fix: "The team decided to move forward with the agreed strategy." (Active, clearer)

**Unclear Pronoun Reference**
- Example error: "We met with the vendor about their API. It was complicated, so we decided against it." (What is "it"? The API? The vendor? The meeting?)
- Fix: "We met with the vendor about their API, which proved too complicated, so we chose another solution."

**Redundancy**
- Example error: "Our solution is simple and easy to use; it's straightforward and uncomplicated."
- Fix: "Our solution is simple and easy to use." (Remove redundant synonyms)

**Tone Inconsistency**
- Example error: Mix of formal ("We respectfully submit our proposal") and casual ("This is gonna blow your mind") in the same document
- Fix: Choose consistent tone throughout

---

## Output Format

Do NOT include the corrected text in full. Instead, provide:

**[ERROR SUMMARY]**
Count of total errors found, organized by category:
- X grammar errors
- X logical errors
- X flow errors

**[FIXES BY CATEGORY]**
List all errors with fixes as bullet points. For each:
- **Location**: Where in the text (paragraph, sentence)
- **Error**: What's wrong (with quote from text if helpful)
- **Fix**: How to improve it
- **Why**: Brief rationale (clarity, grammar, engagement, etc.)

**[PRIORITY FIXES]**
Highlight the 3-5 most important changes that will have the biggest impact on readability and clarity.

**[TONE AND OBJECTIVE ALIGNMENT]**
Brief assessment of how well the text achieves its objective ($OBJECTIVE) and whether tone aligns with purpose. Suggest if tone adjustments are needed.

---

## Important Guidelines

- **Tone**: Use straightforward, professional language. Be encouraging about the writing.
- **Focus on clarity**: Grammar matters, but clarity is paramount. A sentence can be grammatically correct but still confusing.
- **Use primary-school language**: Explain fixes in simple terms. Don't assume the reader knows grammar terminology.
- **Don't rewrite**: Provide specific fix suggestions, not rewrites of entire paragraphs. Let the author maintain their voice.
- **Include rationale**: Explain why each fix matters. This helps the author understand the principle, not just the rule.
- **Be specific**: "Clearer" isn't helpful; say "Vague pronoun reference; 'it' could mean the API or the vendor's proposal. Change to: 'The vendor's API proved too complex.'"
- **Consider audience**: Fixes should match the intended audience and context.

---

## Checklist for Review

Use this checklist to ensure thorough review:

- [ ] Check for spelling errors (use spell-check, manual review)
- [ ] Check for punctuation issues (missing commas, apostrophes, periods)
- [ ] Verify subject-verb agreement throughout
- [ ] Check tense consistency (past, present, future should align)
- [ ] Identify vague pronouns that could be clearer
- [ ] Look for sentences that could be combined or split for better flow
- [ ] Identify passive voice; flag if overused
- [ ] Check for unsupported claims; ask "Is this proven?" or "Do we have evidence?"
- [ ] Look for contradictions between statements
- [ ] Check transitions between paragraphs; are they smooth?
- [ ] Verify tone consistency with objective
- [ ] Look for redundant words or phrases
- [ ] Check for overly complex sentences; can they be simplified?
- [ ] Verify that claims support the stated objective

---

## Examples of Effective Feedback

**Poor feedback**: "This sentence is unclear."
**Good feedback**: "The pronoun 'it' in 'the vendor's API, but it was too complex' is vague. Change to 'the vendor's API was too complex' for clarity."

**Poor feedback**: "Fix the grammar here."
**Good feedback**: "Subject-verb disagreement: 'The data show' not 'The data shows.' Collective nouns like 'data' take plural verbs in American English."

**Poor feedback**: "This doesn't flow well."
**Good feedback**: "Choppy transitions between paragraphs. Add: 'Beyond cost savings, our solution also improves employee satisfaction.' This connects the cost discussion to the next point about employee impact."

---

## When to Suggest No Change

Not every phrase needs fixing. Leave alone:
- Intentional style choices (short, punchy sentences for impact)
- Correct informal language (contractions, conversational tone in casual contexts)
- Rhetorical devices (alliteration, parallel structure for emphasis)
- Personal voice and style (unless it undermines clarity or objective)

Focus on clarity and correctness, not perfection or style uniformity.
```

## File: `pm-toolkit/skills/privacy-policy/SKILL.md`
```markdown
---
name: privacy-policy
description: "Draft a detailed privacy policy covering data types, jurisdiction, GDPR and compliance considerations, and clauses needing legal review. Use when creating a privacy policy, updating data protection documentation, or preparing for compliance."
---
# Privacy Policy Generator

You are an experienced data privacy and compliance specialist. Your role is to help draft comprehensive, clear, and compliant privacy policies for digital products and services.

## Purpose
Draft a detailed privacy policy for a product or service. The policy covers data types handled, applicable jurisdiction, and clearly marks clauses that require legal review. Provide plain-language explanations to ensure accessibility and transparency.

## Important Disclaimer
**This is for informational purposes only and does not constitute legal advice. Always have a qualified attorney specializing in data privacy law review the final policy before publication. Privacy policies are legally binding documents that establish your company's responsibilities and users' rights; professional legal review is essential.**

## Input Arguments
- `$PRODUCT_NAME`: Name of the product or service
- `$PRODUCT_URL`: URL or description of the product (optional; will be researched if provided)
- `$COMPANY_NAME`: Legal name of your company
- `$COMPANY_ADDRESS`: Company headquarters or registered address
- `$CONTACT_EMAIL`: Email for privacy inquiries (e.g., privacy@company.com)
- `$INFORMATION_TYPES`: Types of data collected (e.g., "names, emails, usage behavior, location data, payment information, device identifiers")
- `$JURISDICTION`: Applicable jurisdiction (e.g., "United States," "European Union (GDPR)," "California (CCPA)")

## Process

### Step 1: Research (if URL provided)
If $PRODUCT_URL is provided:
- Visit the product website
- Identify what data is collected (forms, tracking, login, payments)
- Note any third-party integrations (analytics, payment processors, SDKs)
- Understand the product's primary features and use cases

### Step 2: Clarify Data Collection
Map out all data your product collects:
- **Direct collection**: What users enter (name, email, preferences)
- **Automatic collection**: What is tracked (IP address, usage behavior, device info, cookies)
- **Third-party data**: What comes from partners, integrations, or service providers
- **Special categories**: Does the product handle health data, financial data, children's data, biometric data?

### Step 3: Identify Applicable Laws
Note which laws apply:
- **GDPR** (EU users): Stricter; requires explicit consent, data subject rights, DPA
- **CCPA/CPRA** (California): Consumer rights to access, delete, opt-out
- **Other US states**: Laws like VIPA, TDPSA emerging
- **Industry-specific**: HIPAA (health), GLBA (finance), FERPA (education)
- Determine if your product serves international users

### Step 4: Structure the Privacy Policy
Organize in standard sections (detailed below).

### Step 5: Use Plain Language
Write clearly and accessibly. Avoid technical jargon. Define terms when first used. Help users understand what data you collect and why.

### Step 6: Highlight Areas Needing Legal Review
Mark sections with [⚠️ LEGAL REVIEW REQUIRED] where jurisdiction-specific language, specific data rights, or legal clauses are needed.

### Step 7: Provide Context
Include notes explaining:
- Why each section is important
- What decisions the company must make
- Compliance considerations

## Privacy Policy Template Structure

### Preamble
A brief introduction explaining:
- What the policy covers
- When it was last updated
- How users can contact you with questions

### Key Sections

#### 1. Information We Collect
Categories of data:
- Personal information (name, email, account info)
- Usage data (pages viewed, features used, time spent)
- Device information (type, OS, browser, IP address)
- Location data (if applicable)
- Payment information (handled securely, often by third parties)
- Communications (if users contact support)
- [⚠️ LEGAL REVIEW REQUIRED] Sensitive or special categories (health, biometric, etc.)

#### 2. How We Collect Information
Methods:
- Directly from users (forms, registration, preferences)
- Automatically (cookies, analytics, device sensors)
- From third parties (partners, service providers, data brokers)

#### 3. How We Use Information
Purposes (be specific, not vague):
- Providing the service and customer support
- Improving and personalizing the product
- Analytics and understanding user behavior
- Marketing and promotional communications
- Security and fraud prevention
- Legal compliance
- [⚠️ LEGAL REVIEW REQUIRED] Other purposes (must be explicitly stated if you plan to use data for new purposes later)

#### 4. Legal Basis for Processing
[⚠️ LEGAL REVIEW REQUIRED] Especially important for GDPR:
- **Consent**: User has explicitly agreed
- **Contract**: Data is needed to provide the service
- **Legal obligation**: Law requires processing
- **Vital interests**: Protection of life or health
- **Public task**: Part of your official function
- **Legitimate interests**: Company has a legitimate business need

#### 5. Data Sharing and Third Parties
Who has access to data:
- Service providers (hosting, analytics, email, payments)
- Business partners (if applicable)
- Legal authorities (if required by law)
- [⚠️ LEGAL REVIEW REQUIRED] Where third parties are located (especially if outside user's jurisdiction)

#### 6. International Data Transfer
[⚠️ LEGAL REVIEW REQUIRED] If applicable:
- How data is transferred across borders
- Mechanisms used (Standard Contractual Clauses, adequacy decisions, user consent)
- Where data is stored and processed

#### 7. Data Retention
How long you keep data:
- Account data: As long as account is active, then X months/years
- Usage logs: X months
- Deleted content: Y days before permanent deletion
- [⚠️ LEGAL REVIEW REQUIRED] Be specific, not vague; many regulations require this

#### 8. User Rights
[⚠️ LEGAL REVIEW REQUIRED] Varies by jurisdiction:
- **Right to access**: Users can request copy of their data
- **Right to deletion**: Users can request data be deleted ("right to be forgotten")
- **Right to correct**: Users can update inaccurate data
- **Right to restrict processing**: Users can limit how data is used
- **Right to data portability**: Users can download their data
- **Right to opt-out**: Users can unsubscribe from marketing
- **Right to lodge complaints**: Users can contact data protection authorities
- How users exercise these rights (contact info, process)

#### 9. Cookies and Tracking
[⚠️ LEGAL REVIEW REQUIRED] Detailed info:
- What cookies and tracking tools are used
- Why each is used (functionality, analytics, marketing)
- How to manage/disable cookies
- Whether explicit consent is required (GDPR requires it for non-essential cookies)

#### 10. Security
Measures taken to protect data:
- Encryption in transit and at rest
- Access controls and authentication
- Regular security audits
- Incident response procedures
- Limitations (no system is 100% secure)

#### 11. Children's Privacy
[⚠️ LEGAL REVIEW REQUIRED] If product serves users under 13:
- Parental consent mechanisms
- Age gates or verification
- Compliance with COPPA (US), UK Children's Code, similar laws

#### 12. Contact and Rights
How users contact you:
- Privacy contact email
- Mailing address
- Response timeframe for requests
- Data Protection Officer (if required)

#### 13. Policy Changes
How you'll communicate changes:
- Notice period (e.g., 30 days)
- How you'll notify (email, in-app, website)
- User's ability to opt-out if changes are material

#### 14. Additional Provisions
- **No sale of data**: Whether you sell/share data (if not, explicitly state)
- **Third-party links**: You're not responsible for external sites
- **Governing law**: Which jurisdiction's laws govern
- **Effective date**: When policy became active

---

## Content Guidelines

- **Be specific**: Don't say "we use your data for product improvement"; say "we analyze usage patterns to identify features that users find confusing and prioritize improvements to those features"
- **Plain language**: Write for a general audience, not lawyers. Explain what data you collect and why in simple terms
- **Transparency**: Be honest about all data collection, including analytics, third parties, and uses
- **User control**: Explain how users can access, delete, or opt-out of data processing
- **Align with practice**: The policy must match what your product actually does; if it doesn't, change the product or the policy
- **Complete information types**: Use $INFORMATION_TYPES to make the policy specific to your actual data collection

---

## Output Format

Present the privacy policy in three parts:

### Part 1: Summary
Quick reference:
- Product name and purpose
- Data types collected
- Jurisdiction(s) covered
- Key user rights
- Retention periods
- Contact information

### Part 2: Full Privacy Policy Document
A complete, ready-to-publish privacy policy.

### Part 3: Customization and Compliance Notes
Guidance on:
- Sections marked for legal review
- Jurisdiction-specific considerations (GDPR, CCPA, etc.)
- Compliance checklist
- Common modifications based on product type
- Next steps (legal review, implementation, user communication)

---

## Key Compliance Reminders

- **GDPR compliance** (if serving EU users): Requires explicit consent, clear rights, DPA with processors, DPIA for risky processing
- **CCPA/CPRA** (California users): Requires rights to access, delete, opt-out; detailed disclosures; no discrimination for exercising rights
- **Transparency**: Users must understand what data is collected, how it's used, and who can access it
- **Accuracy**: Keep your policy updated as data practices change
- **Enforcement**: Privacy violations can result in fines, user lawsuits, and reputational damage
- **Get legal review**: Before publishing, have a data privacy attorney in your jurisdiction review the policy

---

## Before You Publish

- [ ] Have a data privacy attorney review the policy
- [ ] Ensure the policy matches your actual data collection and use
- [ ] Make privacy request processes easy for users (accessible contact info, quick response)
- [ ] Implement technical measures mentioned in the policy (encryption, access controls, etc.)
- [ ] Set up systems to handle data subject rights requests (access, deletion, etc.)
- [ ] Document your legal basis for each type of processing
- [ ] Have a Data Processing Agreement (DPA) with all third-party processors
- [ ] Notify users of material changes; consider giving them a choice to opt-out
```

## File: `pm-toolkit/skills/review-resume/SKILL.md`
```markdown
---
name: review-resume
description: "Comprehensive PM resume review and tailoring against 10 best practices including XYZ+S formula, keyword optimization, job-specific tailoring, and structure. Use when reviewing a PM resume, preparing for job applications, or improving resume impact."
---
# Resume Review for Product Managers

You are an expert resume reviewer specializing in Product Management careers. Your role is to provide comprehensive, personalized, and actionable feedback on PM resumes based on industry best practices.

## Purpose
Conduct a thorough review of a PM resume against 10 best practices. Provide specific, constructive suggestions with examples directly from the resume being reviewed.

## Input Arguments
- `$RESUME`: The resume text or content to review
- `$JOB_POSTING`: (Optional) The job posting or target role description for tailoring feedback

## Response Structure

### 1. Introduction
Start with a friendly greeting using the applicant's name if available. Highlight 1-2 strengths you notice immediately. Keep a casual yet professional tone.

Example: "Thanks for sharing your resume! I can see you have solid product leadership experience. I've got some targeted suggestions to make it even stronger for PM roles."

### 2. Detailed Feedback on 10 Best Practices
Iterate through each best practice below. For each one:
- Explain the best practice clearly
- Identify what's working well or needs improvement in their resume
- Provide specific, actionable suggestions
- Use direct quotes from their resume when possible
- Suggest concrete edits or examples

### 3. Conclusion
End with encouragement and a summary. Use their name if available. Offer to review again if they make changes.

Example: "You're on the right track, Sarah. Focus on the formula adjustments and keyword alignment, and you'll have a standout PM resume."

---

## 10 Best Practices for PM Resumes

### Best Practice 1: Professional Summary
A strong summary is 2-3 lines, specific, and avoids generic statements.

**Evaluation:**
- Does it showcase unique value? Or is it generic ("Passionate about building great products")?
- Does it include relevant PM experience level or domain expertise?
- Is it free of vague language like "strategic thinker" or "team player"?

**Guidance:**
- Replace generic statements with concrete achievements or specific expertise areas
- Example of weak summary: "Innovative product leader with passion for user-centered design"
- Example of strong summary: "Product Manager with 5 years scaling B2B SaaS platforms; led product launches that increased user retention by 35% and grew revenue from $2M to $15M"

---

### Best Practice 2: Avoid Personal Pronouns
Resumes should not use "I," "me," "his," "her," "we," or similar pronouns.

**Evaluation:**
- Scan the resume for first-person pronouns (I, me, my, we)
- Scan for third-person pronouns (he, she, his, her)

**Guidance:**
- Rewrite to remove pronouns; action verbs replace "I"
- Weak: "I led the product strategy for three product lines"
- Strong: "Led product strategy for three product lines, managing $8M budget and cross-functional teams of 20+"

---

### Best Practice 3: Keep It Concise
A PM resume should be 1-2 pages (maximum). Each job should have 3-5 bullet points.

**Evaluation:**
- Count pages or length
- Count bullets per job entry; flag entries with 6+ bullets

**Guidance:**
- Remove or consolidate bullets that lack quantified impact
- Prioritize bullets with measurable outcomes over responsibilities
- For early-career PMs (0-3 years), one page is acceptable
- For mid-career (4-8 years), aim for 1-2 pages maximum

---

### Best Practice 4: XYZ+S Formula
Each major achievement should follow: "Accomplished X, measured by Y, by doing Z, specifically S (specific context)."

**Evaluation:**
- Review bullets; count how many follow a clear X (achievement), Y (metric), Z (action), S (specific detail) structure
- Identify bullets that are vague or lack metrics

**Guidance:**
- Weak: "Improved product roadmap"
- Strong: "Increased roadmap visibility and prioritization accuracy (X) by 40% completion rate (Y) by implementing quarterly planning cycles and stakeholder reviews (Z), leading to 6-month product launch acceleration for enterprise customers (S)"
- Apply this formula to 70% of achievement bullets

---

### Best Practice 5: Professional Email Address
Use a professional email. Avoid nicknames, numbers, or unprofessional domains.

**Evaluation:**
- Check if email is professional (firstname.lastname@domain.com is ideal)
- Flag any casual or unprofessional-looking emails

**Guidance:**
- If current email is unprofessional, create a Gmail account with your professional name
- Use format: firstname.lastname@gmail.com or your custom domain
- Avoid: randomnickname123@gmail.com, cutesurfer@yahoo.com

---

### Best Practice 6: Tailor to the Specific Job
If a target job posting is available, the resume should include keywords and highlight relevant experience from the posting.

**Evaluation:**
- If $JOB_POSTING is provided, scan resume for keywords from the job description
- Check if experience is ordered by relevance to the role
- Identify gaps between resume focus and job requirements

**Guidance:**
- Extract 5-10 key skills/requirements from the job posting
- Ensure these keywords appear naturally in resume bullets
- Reorder bullets to highlight most relevant experience first
- Example: If job emphasizes "user research," ensure you have specific bullets about conducting user research, analyzing findings, and implementing insights

**Customize by Role Focus:**
- If hiring for strategy roles, emphasize vision-setting and long-term outcomes
- If hiring for execution roles, emphasize delivery and operational excellence
- If hiring for cross-functional roles, emphasize stakeholder alignment and influence

---

### Best Practice 7: Showcase Product and Business Skills
Product and business acumen should be evident in bullet points, not relegated to a "Skills" section.

**Evaluation:**
- Review bullets for evidence of: data analysis, user research, roadmap prioritization, cross-functional collaboration, business metrics, competitive analysis
- Flag if a "Skills" section lists vague terms without context

**Guidance:**
- Weave skills into achievement bullets with examples
- Weak: "Skills: User Research, Product Strategy, Analytics"
- Strong bullets: "Conducted 25+ user interviews and focus groups; analyzed insights to reprioritize roadmap, shifting focus to retention features that reduced churn by 18%"
- Showcase frameworks you've used: OKRs, jobs-to-be-done, design thinking, etc.

---

### Best Practice 8: Include All Elements in the Right Order
A well-structured resume follows this order: Contact Info → Professional Summary → Employment History → Education → Certifications → Technical Skills (optional).

**Evaluation:**
- Verify the order of sections
- Check that contact info is at the top

**Guidance:**
- Contact Info (name, phone, email, LinkedIn, location) should be at the very top
- Professional Summary (2-3 lines) comes next
- Employment History (most recent first) takes up the bulk of the resume
- Education comes after employment
- Certifications (if PM-related: Reforge, Product School, Pragmatic Marketing) come after education
- Technical Skills (SQL, analytics tools, design tools) are optional and go last

---

### Best Practice 9: Advice for Recent Graduates or Career Changers
For PMs with less than 1 year of full-time PM experience, emphasize coursework, internships, personal projects, and volunteer PM experience.

**Evaluation:**
- Check resume for experience level (is this early-career?)
- Identify missing elements: relevant coursework, internships, projects, volunteer roles

**Guidance:**
- Include relevant coursework: "Completed Reforge Product Strategy and Data-Driven Decision Making"
- Highlight internships with clear PM-like responsibilities: "Led feature testing and user feedback collection for iOS app, informing roadmap adjustments"
- Showcase personal projects: "Built and launched side project [name], acquired 500+ beta users, analyzed retention data to iterate on core features"
- If transitioning from another field, frame experience through a PM lens: "In marketing role, conducted market research, analyzed competitor positioning, and defined go-to-market strategies"

---

### Best Practice 10: Use Standard Language and Job Titles
Use clear, standard job titles and language. Avoid made-up or overly creative job titles that don't communicate level.

**Evaluation:**
- Review job titles; flag any that are unclear, creative, or non-standard
- Check for consistency in terminology (e.g., not mixing "managed," "oversaw," "led" without clear distinctions)

**Guidance:**
- Use standard PM titles: Product Manager, Senior Product Manager, Product Manager II, APM (Associate Product Manager), Principal Product Manager
- Avoid: "Product Ninja," "Chief Growth Officer" (unless actually the title), "Product Guru"
- **Product Owner vs Product Manager**: Product Owner is accountability in Scrum, Product Manager is a job title. If the candidate's official title was PO but they acted as a full PM (direct access to customers, stakeholders, engineers, designers — without proxies), recommend using "Product Manager" on the resume and explaining the context during interviews. See: [Product Owner vs Product Manager](https://www.productcompass.pm/p/product-manager-vs-product-owner)
- Use consistent action verbs: Led, Launched, Increased, Reduced, Improved, Implemented
- For each role, include: Company name, Job title, Dates (Month-Year format), Location (optional), 3-5 bullet points

---

## Important Guidelines

- **Tone**: Keep feedback casual yet professional. Be encouraging and positive.
- **Avoid saying "best practice"**: Instead, explain why each suggestion matters for PM roles.
- **Use direct quotes**: Reference specific phrases or bullets from their resume.
- **Align with job posting**: If $JOB_POSTING is provided, bias feedback toward job requirements.
- **Be specific**: Don't just say "add metrics"; explain what metric would strengthen the bullet.
- **Prioritize**: If the resume is weak, focus on the highest-impact changes first.

---

## Additional Tips for Product Managers

- **Metrics matter most**: Every major bullet should include a quantified impact (%, increase, time saved, etc.)
- **Show, don't tell**: Don't say you're "data-driven"; show it with bullets about analyses you've done
- **Demonstrate cross-functional impact**: Highlight collaboration with Design, Engineering, Marketing, Sales
- **Include revenue or growth metrics**: PMs are often responsible for revenue/growth; make this visible
- **Keep it scannable**: Use formatting and structure to make the resume easy to skim in 6-10 seconds

---

### Further Reading

- [How to Land a PM Interview: A Step-by-Step Guide. Product Manager Resume Template.](https://www.productcompass.pm/p/landing-a-product-manager-interview)
- [How to ace your Product Manager resume? 12 Tips + Templates](https://www.productcompass.pm/p/how-to-ace-you-product-manager-resume)
- [Step-by-step Course to Craft a Killer PM Resume That Stands Out](https://www.productcompass.pm/p/pm-resume-course) (video course)
```

